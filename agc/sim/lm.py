"""Apollo 11 Lunar Module (LM-5 "Eagle") vehicle model.

Six-degree-of-freedom rigid body with the descent propulsion system (DPS),
the 16 reaction control jets, the DPS trim gimbal and the signals exchanged
with the guidance computer:

* channel 11 bit 13 / 14: ENGINE ON / ENGINE OFF
* THRUST counter (055) + channel 14 bit 4: throttle increments, 12.53 N per pulse
* channel 12 bits 9-12: trim gimbal drive, 0.2 deg/s
* channels 5 and 6: RCS jets (see JETS_CH5 / JETS_CH6)
* channel 30 bits 3 and 5: engine armed, auto throttle

Numbers come from the LM Data Book / Luminary constants: FTP thrust 43.9 kN,
throttle range 980-6300 lbf, DPS exhaust velocity 2956 m/s (DPSVEX), RCS
jet thrust 445 N, LM mass at PDI 15.1 t.  The moments of inertia are
chosen so that the one-jet accelerations match the DAP's own curve fits
(1JACC = A/(mass + C) + B in AOSTASK) for a descent-configured vehicle.
"""

from __future__ import annotations

import math

import numpy as np

from ..cpu import THRUST, CYCLES_PER_SECOND

LBF = 4.4482216                       # newton per pound-force

# --- descent propulsion system ------------------------------------------------
DPS_FTP = 9870.0 * LBF                # 43.9 kN, fixed throttle position (92.5 %)
DPS_MIN = 980.0 * LBF                 # minimum throttle (MINFORCE pad load)
DPS_MAX_THROTTLEABLE = 6300.0 * LBF   # above this the engine can only run at FTP
DPS_VEX = 2955.88868                  # m/s exhaust velocity (Luminary DPSVEX)
DPS_LAG = 0.2                         # s, throttle response time constant (THROTLAG)
THRUST_N_PER_PULSE = 1.0 / 0.0797959872   # 12.53 N per THRUST counter pulse (SCALEFAC)
THRUST_PULSE_RATE = 3200.0            # pulses per second drained from the counter
GIMBAL_RATE = math.radians(0.2)       # trim gimbal drive rate
GIMBAL_LIMIT = math.radians(6.0)
ENGINE_BELOW_CG = 1.9                 # m, gimbal pivot below the vehicle CG (descent config)

# --- reaction control system --------------------------------------------------
RCS_THRUST = 445.0                    # N (100 lbf)
RCS_VEX = 2840.0                      # m/s
QUAD_RADIUS = 1.65                    # m from the X axis to each quad
QUAD_ABOVE_CG = 0.75                  # m, quads are above the descent-configuration CG

_A = QUAD_RADIUS / math.sqrt(2.0)
# quad positions (x, y, z) in body axes: 1 front-left (+Z,-Y), 2 aft-left, 3 aft-right, 4 front-right
QUAD_POS = {1: (QUAD_ABOVE_CG, -_A, _A), 2: (QUAD_ABOVE_CG, -_A, -_A),
            3: (QUAD_ABOVE_CG, _A, -_A), 4: (QUAD_ABOVE_CG, _A, _A)}
# force on the vehicle for each nozzle letter (exhaust direction is opposite)
_DIR = {"U": (-1, 0, 0), "D": (1, 0, 0), "F": (0, 0, -1), "A": (0, 0, 1), "L": (0, 1, 0), "R": (0, -1, 0)}
# channel 5 bits 1..8 (vertical jets) and channel 6 bits 1..8 (horizontal jets)
JETS_CH5 = ["B4U", "A4D", "A3U", "B3D", "B2U", "A2D", "A1U", "B1D"]
JETS_CH6 = ["B3A", "B4F", "A1F", "A2A", "B2L", "A3R", "A4R", "B1L"]


def _jet(name: str) -> tuple[np.ndarray, np.ndarray]:
    quad = int(name[1])
    return np.array(QUAD_POS[quad], dtype=float), np.array(_DIR[name[2]], dtype=float)


JET_GEOMETRY = {n: _jet(n) for n in JETS_CH5 + JETS_CH6}

# --- mass properties ------------------------------------------------------------
PDI_MASS = 15103.0                    # kg (33297 lb), Apollo 11 at powered descent initiation
DESCENT_PROPELLANT_AT_PDI = 8200.0    # kg usable DPS propellant at PDI
RCS_PROPELLANT = 270.0                # kg
REF_INERTIA = np.array([23800.0, 23600.0, 23900.0])   # kg m^2 at PDI_MASS (matches DAP 1JACC fits)


def skew(v: np.ndarray) -> np.ndarray:
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def rotate_dcm(c: np.ndarray, w_body: np.ndarray, dt: float) -> np.ndarray:
    """Advance a body<-ref DCM by body rate w over dt (exact rotation)."""
    theta = np.linalg.norm(w_body) * dt
    if theta < 1e-12:
        return c
    k = w_body * dt / theta
    kx = skew(k)
    r = np.eye(3) + math.sin(theta) * kx + (1 - math.cos(theta)) * kx @ kx   # rotates vectors by +theta about k
    # new body axes expressed in old body axes are the rows of r^T; C_new = R^T C
    return r.T @ c


class LunarModule:
    """Vehicle state and actuators.  Positions/velocities in the REF frame (m, m/s)."""

    def __init__(self, cpu, mu: float):
        self.cpu = cpu
        self.mu = mu
        self.r = np.zeros(3)
        self.v = np.zeros(3)
        self.c = np.eye(3)                   # C_nb_ref: rows are body axes in REF
        self.w = np.zeros(3)                 # body angular rate rad/s
        self.mass = PDI_MASS
        self.dps_propellant = DESCENT_PROPELLANT_AT_PDI
        self.rcs_propellant = RCS_PROPELLANT
        # actuators
        self.engine_armed = False
        self.engine_on = False
        self.throttle_cmd_n = 0.0            # accumulated throttle increments from the AGC
        self.thrust = 0.0                    # actual thrust (N)
        self.gimbal_pitch = 0.0              # rad
        self.gimbal_roll = 0.0
        self.jet_on_time = {n: 0.0 for n in JET_GEOMETRY}
        self._jet_state_cycles = cpu.cycles
        self._ch5 = 0
        self._ch6 = 0
        self.engine_on_events = 0
        self.specific_force_ref = np.zeros(3)
        self.touchdown = False
        self.log_rcs_impulse = 0.0
        prev = cpu.on_channel_write
        self._prev_hook = prev
        cpu.on_channel_write = self._on_channel_write

    # ------------------------------------------------------------------
    # AGC output channels
    # ------------------------------------------------------------------
    def _on_channel_write(self, ch: int, value: int):
        if ch == 5 or ch == 6:
            self._account_jets()
            if ch == 5:
                self._ch5 = value & 0xFF
            else:
                self._ch6 = value & 0xFF
        elif ch == 0o11:
            if value & 0o10000 and not self.engine_on and self.engine_armed:   # bit 13 ENGINE ON
                self.engine_on = True
                self.engine_on_events += 1
            if value & 0o20000:                                                  # bit 14 ENGINE OFF
                self.engine_on = False
        if self._prev_hook:
            self._prev_hook(ch, value)

    def _account_jets(self):
        """Accumulate on-time of the currently firing jets since the last change."""
        now = self.cpu.cycles
        dt = (now - self._jet_state_cycles) / CYCLES_PER_SECOND
        self._jet_state_cycles = now
        if dt <= 0:
            return
        for bit in range(8):
            if self._ch5 & (1 << bit):
                self.jet_on_time[JETS_CH5[bit]] += dt
            if self._ch6 & (1 << bit):
                self.jet_on_time[JETS_CH6[bit]] += dt

    def set_engine_armed(self, armed: bool):
        """Crew switch: DESCENT ENGINE ARM (channel 30 bit 3, active low)."""
        self.engine_armed = armed
        if armed:
            self.cpu.chan[0o30] &= ~0o4
        else:
            self.cpu.chan[0o30] |= 0o4
            self.engine_on = False

    def engine_stop(self):
        self.engine_on = False
        self.set_engine_armed(False)

    def service_throttle(self, dt: float):
        """Drain the THRUST counter (DINC pulses) while channel 14 bit 4 is set."""
        cpu = self.cpu
        if cpu.chan[0o14] & 0o10:
            n = int(THRUST_PULSE_RATE * dt) + 1
            for _ in range(n):
                v = cpu.e[THRUST] & 0o77777
                if v in (0, 0o77777):
                    cpu.chan[0o14] &= ~0o10          # hardware drops the activity bit at ZOUT
                    break
                if v & 0o40000:
                    self.throttle_cmd_n -= THRUST_N_PER_PULSE
                else:
                    self.throttle_cmd_n += THRUST_N_PER_PULSE
                # The DECA throttle integrator saturates at the physical limits: the 4096
                # "FLATOUT" pulses drive the throttle to the stop, excess pulses are lost.
                # Luminary relies on this (see PIFPSET in THROTTLE_CONTROL_ROUTINES).
                self.throttle_cmd_n = max(0.0, min(DPS_FTP - DPS_MIN, self.throttle_cmd_n))
                cpu.unprogrammed_increment(THRUST, 4)   # DINC toward zero

    def service_gimbal(self, dt: float):
        # Sign convention: in AOSTASK the AGC treats the "+PITCH" discrete (bit 10)
        # as producing a *negative* Q (pitch) acceleration rate, so +PITCH moves the
        # bell such that the pitch torque decreases; same for +ROLL (bit 12) and R.
        ch12 = self.cpu.chan[0o12]
        if ch12 & 0o1000:                         # bit 10 +PITCH trim
            self.gimbal_pitch -= GIMBAL_RATE * dt
        if ch12 & 0o400:                          # bit 9  -PITCH trim
            self.gimbal_pitch += GIMBAL_RATE * dt
        if ch12 & 0o4000:                         # bit 12 +ROLL trim
            self.gimbal_roll -= GIMBAL_RATE * dt
        if ch12 & 0o2000:                         # bit 11 -ROLL trim
            self.gimbal_roll += GIMBAL_RATE * dt
        self.gimbal_pitch = max(-GIMBAL_LIMIT, min(GIMBAL_LIMIT, self.gimbal_pitch))
        self.gimbal_roll = max(-GIMBAL_LIMIT, min(GIMBAL_LIMIT, self.gimbal_roll))

    def commanded_thrust(self) -> float:
        if not self.engine_on or self.dps_propellant <= 0:
            return 0.0
        cmd = DPS_MIN + self.throttle_cmd_n
        if cmd > DPS_MAX_THROTTLEABLE:
            return DPS_FTP                        # the engine cannot throttle between 60 % and FTP
        return max(DPS_MIN, cmd)

    # ------------------------------------------------------------------
    # Dynamics
    # ------------------------------------------------------------------
    def inertia(self) -> np.ndarray:
        return REF_INERTIA * (self.mass / PDI_MASS)

    def step(self, dt: float):
        """Advance the vehicle by dt seconds (the AGC has already run for dt)."""
        self._account_jets()
        self.service_throttle(dt)
        self.service_gimbal(dt)

        # Descent engine with first-order throttle response.
        target = self.commanded_thrust()
        if target == 0.0:
            self.thrust = 0.0
        else:
            self.thrust += (target - self.thrust) * min(1.0, dt / DPS_LAG)
        # thrust direction in body axes (gimbal tilts the bell)
        sp_, cp_ = math.sin(self.gimbal_pitch), math.cos(self.gimbal_pitch)
        sr_, cr_ = math.sin(self.gimbal_roll), math.cos(self.gimbal_roll)
        d = np.array([cp_ * cr_, -sr_, sp_])
        f_dps = self.thrust * d
        r_eng = np.array([-ENGINE_BELOW_CG, 0.0, 0.0])
        torque = np.cross(r_eng, f_dps)
        force = f_dps.copy()
        mdot = self.thrust / DPS_VEX
        self.dps_propellant -= mdot * dt

        # RCS: impulses accumulated since the previous step
        rcs_impulse = 0.0
        for name, t_on in self.jet_on_time.items():
            if t_on <= 0:
                continue
            pos, direction = JET_GEOMETRY[name]
            impulse = RCS_THRUST * t_on
            rcs_impulse += impulse
            force += direction * impulse / dt
            torque += np.cross(pos, direction) * impulse / dt
            self.jet_on_time[name] = 0.0
        self.rcs_propellant -= rcs_impulse / RCS_VEX
        self.log_rcs_impulse += rcs_impulse
        self.mass -= mdot * dt + rcs_impulse / RCS_VEX

        # translation (RK2 midpoint for gravity, thrust constant over the step)
        a_sf_ref = self.c.T @ (force / self.mass)      # specific force in REF
        self.specific_force_ref = a_sf_ref

        def grav(r):
            return -self.mu * r / np.linalg.norm(r) ** 3

        a1 = grav(self.r) + a_sf_ref
        r_mid = self.r + self.v * dt / 2 + a1 * dt * dt / 8
        v_mid = self.v + a1 * dt / 2
        a2 = grav(r_mid) + a_sf_ref
        self.r = self.r + v_mid * dt                 # midpoint rule
        self.v = self.v + a2 * dt
        # rotation
        inertia = self.inertia()
        w = self.w
        wdot = (torque - np.cross(w, inertia * w)) / inertia
        w_mid = w + 0.5 * wdot * dt
        self.c = rotate_dcm(self.c, w_mid, dt)
        self.w = w + wdot * dt

    # ------------------------------------------------------------------
    def altitude(self, site_radius: float) -> float:
        return float(np.linalg.norm(self.r) - site_radius)

    def body_x_ref(self) -> np.ndarray:
        return self.c[0]

    def pitch_from_vertical_deg(self) -> float:
        up = self.r / np.linalg.norm(self.r)
        return math.degrees(math.acos(max(-1.0, min(1.0, float(np.dot(self.c[0], up))))))
