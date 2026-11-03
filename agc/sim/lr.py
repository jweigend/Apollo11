"""Landing radar (LR) model.

The LR antenna has two positions (1 for the braking phase, 2 for approach
and landing).  Its coordinate frame is related to the navigation base by the
pad-loaded angles LRALPHA (rotation about X) and LRBETA (rotation about Y),
exactly like IMU gimbal angles, which is how Luminary treats them (SETPOS).

The radar electronics deliver, on request through channel 13:

* selection 7: slant range along the range beam (HBEAMANT), 1.079 ft per
  count on the low scale (below 2500 ft) and 5.395 ft per count on the high
  scale; channel 33 bit 9 (active low) tells the AGC which scale is in use;
* selections 4, 5, 6: velocity of the vehicle relative to the surface along
  the antenna X, Y and Z axes, as counts = 12288 + v / (-0.644, 1.212, 0.8668 ft/s).

Channel 33 bits 5 and 8 (active low) signal "range data good" and "velocity
data good"; bits 6/7 report antenna position 1/2.
"""

from __future__ import annotations

import math

import numpy as np

from .imu import dcm_from_gimbals

FT = 0.3048
RANGE_LOW_SCALE_FT = 1.079
RANGE_HIGH_SCALE_FT = 5.395
VEL_SCALE_FT = (-0.644, 1.212, 0.8668)           # X, Y, Z antenna axes
VEL_BIAS = 12288
HBEAMANT = np.array([-0.4687018041, 0.0, -0.1741224271]) * 2.0   # range beam, antenna coords (unit)
POS1 = (0.0163371759 * 2 * math.pi, 0.0665287037 * 2 * math.pi)   # LRALPHA, LRBETA (rad), pad load
POS2 = (0.0161680555 * 2 * math.pi, 0.0001361111 * 2 * math.pi)
REPOSITION_TIME = 10.0                            # s from command to position 2
MAX_RANGE_FT = 40000.0                            # acquisition limit (slant range)
MAX_VEL_ALT_FT = 35000.0                          # velocity tracking limit (altitude)
LOW_SCALE_BELOW_FT = 2500.0


class LandingRadar:
    def __init__(self, cpu):
        self.cpu = cpu
        self.position = 1
        self.pos2_cmd_time: float | None = None
        self.range_good = False
        self.vel_good = False
        self.low_scale = False
        self.last_range_m = None
        self.last_vel_ant = np.zeros(3)
        self.reads = 0
        cpu.on_radar_read = self.radar_read
        cpu.chan[0o33] &= ~0o40            # antenna in position 1
        cpu.chan[0o33] |= 0o100 | 0o20 | 0o200 | 0o400   # not pos 2, range/vel not good, high scale

    def antenna_dcm(self) -> np.ndarray:
        alpha, beta = POS1 if self.position == 1 else POS2
        return dcm_from_gimbals(alpha, beta, 0.0)    # C_nb_ant

    def update(self, t: float, r: np.ndarray, v_rel: np.ndarray, c_nb_ref: np.ndarray, site_radius: float):
        """Called every simulation step with the true state (REF frame)."""
        cpu = self.cpu
        if cpu.chan[0o12] & 0o10000:                    # LR position 2 command
            if self.pos2_cmd_time is None:
                self.pos2_cmd_time = t
            elif t - self.pos2_cmd_time > REPOSITION_TIME and self.position != 2:
                self.position = 2
                cpu.chan[0o33] |= 0o40                  # no longer in position 1
                cpu.chan[0o33] &= ~0o100                # in position 2
        c_nb_ant = self.antenna_dcm()
        # range beam direction in REF
        d_nb = c_nb_ant @ HBEAMANT
        d_ref = c_nb_ref.T @ d_nb
        # intersection of the beam with the sphere of the landing site radius
        b = float(np.dot(r, d_ref))
        cc = float(np.dot(r, r)) - site_radius ** 2
        disc = b * b - cc
        rng = None
        if disc >= 0 and cc > 0:
            s = -b - math.sqrt(disc)
            if s > 0:
                rng = s
        alt_ft = (np.linalg.norm(r) - site_radius) / FT
        self.last_range_m = rng
        self.range_good = rng is not None and rng / FT < MAX_RANGE_FT and alt_ft > 5.0
        self.vel_good = 0.0 < alt_ft < MAX_VEL_ALT_FT
        self.low_scale = self.range_good and rng / FT < LOW_SCALE_BELOW_FT
        # velocity relative to the surface in antenna axes
        v_nb = c_nb_ref @ v_rel
        self.last_vel_ant = c_nb_ant.T @ v_nb
        ch33 = cpu.chan[0o33]
        ch33 = (ch33 & ~0o20) if self.range_good else (ch33 | 0o20)
        ch33 = (ch33 & ~0o200) if self.vel_good else (ch33 | 0o200)
        ch33 = (ch33 & ~0o400) if self.low_scale else (ch33 | 0o400)
        cpu.chan[0o33] = ch33

    def radar_read(self, selection: int) -> int:
        """Data word shifted into RNRAD for the selected radar channel."""
        self.reads += 1
        if selection == 7:                              # LR range
            if self.last_range_m is None:
                return 0
            scale = RANGE_LOW_SCALE_FT if self.low_scale else RANGE_HIGH_SCALE_FT
            return max(0, min(0o77777, int(round(self.last_range_m / FT / scale))))
        if selection in (4, 5, 6):                      # LR velocity X, Y, Z
            axis = selection - 4
            v_fts = self.last_vel_ant[axis] / FT
            count = VEL_BIAS + v_fts / VEL_SCALE_FT[axis]
            return max(0, min(0o77777, int(round(count))))
        return 0                                        # rendezvous radar: not modelled
