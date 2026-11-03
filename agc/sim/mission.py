"""Apollo 11 powered descent flown by Luminary 099 in the emulator.

Scenario: the LM is in the descent orbit (about 60 x 8 nautical miles) a few
minutes before powered descent initiation (PDI).  The crew (this script)
selects P63; the real flight software computes the ignition time, maneuvers
to the burn attitude, fires the descent engine, flies the braking phase (P63),
the approach phase (P64) and the automatic landing phase (P65) down to the
surface.  The vehicle, its engines and the IMU are simulated here; the
guidance, navigation and control is the original 1969 program.

Nominal landing time TLAND and all guidance targets come from the Apollo 11
pad load; the landing site RLS is the real Tranquility Base coordinates.
"""

from __future__ import annotations

import csv
import hashlib
import inspect
import json
from pathlib import Path
import math
import sys
import time
from dataclasses import dataclass, field

import numpy as np

from ..cpu import AGC, CYCLES_PER_SECOND
from ..dsky import DSKY
from ..program import load_program
from .imu import IMU, landing_site_refsmmat, read_dp, read_vector, write_dp, write_vector, unit
from .lm import LunarModule, PDI_MASS, DPS_FTP
from .lr import LandingRadar
from .padload import apply_padload
from .scaling import ft

MU_MOON = 4.902778e12                 # m^3/s^2 (Luminary MUM)
OMEGA_MOON = 2.66169947e-6            # rad/s (Luminary MOONRATE)
TLAND_CS = 36304920                   # pad load: 100:50:49.20 GET
NOMINAL_PDI_TO_LANDING = 755.0        # s (Apollo 11: 102:33:05 -> 102:45:40)
PERILUNE_ALT = 15240.0                # m (50,000 ft) above the landing site
APOLUNE_ALT = 111120.0                # m (60 nmi) above the landing site
PDI_DOWNRANGE = 436655.0              # m uprange of the site at ignition (RIGNZ pad load)
LEAD_TIME = 480.0                     # s before nominal PDI at which the scenario starts
DAP_CONFIG = "22112"                  # V48: desc+asc, 4-jet X translation system A, normal ACA, 1 deg DB, 2 deg/s


def events_path(log_path) -> str:
    """Event log written next to the telemetry CSV: landing.csv -> landing.events.csv."""
    return str(Path(log_path).with_suffix(".events.csv"))


def rotate_about(v: np.ndarray, k: np.ndarray, ang: float) -> np.ndarray:
    """Rotate v by ang (rad) about the unit axis k (Rodrigues)."""
    kx = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    rot = np.eye(3) + math.sin(ang) * kx + (1 - math.cos(ang)) * kx @ kx
    return rot @ v


def fmt_get(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:03d}:{m:02d}:{s:05.2f}"


@dataclass
class Telemetry:
    t: float
    get: float
    alt: float
    hdot: float
    vhor: float
    thrust: float
    mass: float
    pitch: float
    prog: str
    verb: str
    noun: str
    r1: str
    r2: str
    r3: str
    alarms: str
    enu: tuple = (0.0, 0.0, 0.0)          # position relative to the landing site (east, north, up) [m]
    bx: tuple = (1.0, 0.0, 0.0)           # body +X (thrust axis) in ENU
    bz: tuple = (0.0, 0.0, 1.0)           # body +Z (windows) in ENU
    jets: int = 0                         # channel 5/6 jet bits (16 bits)
    gimbal: tuple = (0.0, 0.0)
    lr: str = ""


CSV_FIELDS = ["t", "get", "alt_m", "hdot_mps", "vhor_mps", "thrust_n", "mass_kg", "pitch_deg",
              "prog", "verb", "noun", "r1", "r2", "r3", "alarms",
              "east_m", "north_m", "up_m", "bx_e", "bx_n", "bx_u", "bz_e", "bz_n", "bz_u",
              "jets", "gimbal_pitch_deg", "gimbal_roll_deg", "lr"]


class Crew:
    """Automates the crew's DSKY procedures during the descent."""

    def __init__(self, sim: "LandingSimulation"):
        self.sim = sim
        self.last_vn: tuple[str, str, bool] | None = None
        self.vn_since = 0.0
        self.r60_pro_done = False
        self.engine_enabled = False
        self.pro_pending_release = 0.0
        self.lr_permitted = False
        self.lr_good_since: float | None = None

    def permit_landing_radar(self, s):
        """V57: permit incorporation of landing radar data.

        Luminary reads the radar on its own but only *uses* the measurements once
        the crew has keyed V57 (flag LRINH).  Aldrin did that when the LR locked
        on and the AGC's DELTAH (radar altitude minus estimate) was a plausible
        -2900 ft.  Without V57 the LGC flies on inertial navigation only."""
        sim = self.sim
        if self.lr_permitted or sim.lr is None or not sim.lr.range_good:
            self.lr_good_since = None if sim.lr is None or not sim.lr.range_good else self.lr_good_since
            return
        if self.lr_good_since is None:
            self.lr_good_since = sim.t
        if sim.t - self.lr_good_since < 6.0 or s.prog.strip() not in ("63", "64"):
            return
        if s.flashing:                                   # do not interrupt a pending request
            return
        delta_h = read_dp(sim.cpu, sim.prog, "DELTAH", 24)
        if abs(delta_h) > 1600.0:                        # > ~5000 ft: crew would not accept this
            return
        sim.type_keys("V57E")
        sim.event(f"crew: V57E - permit landing radar updates (DELTAH = {delta_h / 0.3048:+.0f} ft)")
        self.lr_permitted = True

    def tick(self):
        sim = self.sim
        s = sim.dsky.state(flash=False)
        self.permit_landing_radar(s)
        vn = (s.verb, s.noun, s.flashing)
        now = sim.t
        if vn != self.last_vn:
            self.last_vn = vn
            self.vn_since = now
            if s.flashing:
                sim.event(f"DSKY flashing V{s.verb} N{s.noun}  R1 {s.r1} R2 {s.r2} R3 {s.r3}")
        dwell = now - self.vn_since
        if not s.flashing or dwell < 1.5:
            return
        v, n = s.verb, s.noun
        if (v, n) == ("06", "61"):                       # TGO/TFI/crossrange from the ignition algorithm
            sim.press("PRO", "P63 ignition algorithm done: accept N61")
            self.vn_since = now + 10
        elif (v, n) == ("50", "18"):                     # please perform attitude maneuver
            if not self.r60_pro_done:
                sim.press("PRO", "start automatic maneuver to burn attitude (R60)")
                self.r60_pro_done = True
            else:
                sim.press("ENTR", "maneuver complete: leave R60")
            self.vn_since = now + 10
        elif (v, n) == ("99", "62"):                     # engine enable request
            if not sim.lm.engine_armed:
                sim.lm.set_engine_armed(True)
                sim.event("crew: DESCENT ENGINE ARM")
            sim.press("PRO", "V99: permit ignition")
            self.engine_enabled = True
            self.vn_since = now + 10
        elif (v, n) == ("50", "25"):                     # checklist code request
            code = s.r1.strip()
            if code == "00014":                          # offer of an IMU fine alignment (R51): decline
                sim.press("ENTR", "checklist 00014: skip the optional fine alignment")
            else:
                sim.press("PRO", f"checklist code {code} acknowledged")
            self.vn_since = now + 10
        elif (v, n) == ("06", "63") or (v, n) == ("06", "64") or (v, n) == ("06", "60"):
            sim.press("PRO", f"acknowledge flashing V{v} N{n}")
            self.vn_since = now + 10
        elif (v, n) == ("37", "00") or v == "37":
            pass
        else:
            if dwell > 20:
                sim.event(f"crew: unexpected flashing V{v} N{n}, pressing PRO")
                sim.press("PRO", "unexpected request")
                self.vn_since = now + 10


class LandingSimulation:
    def __init__(self, dt: float = 0.02, verbose: bool = True, log_path: str | None = None,
                 realtime: bool = False, probe_cache: str | None = None, landing_radar: bool = True,
                 agc_cache: str | None = None):
        self.dt = dt
        self.probe_cache = probe_cache
        self.agc_cache = agc_cache             # snapshot of the AGC after basic_setup (saves the 90 s turn-on)
        self.use_lr = landing_radar
        self.lr: LandingRadar | None = None
        self.verbose = verbose
        self.realtime = realtime
        self.prog = load_program("luminary099")
        self.cpu: AGC | None = None
        self.dsky: DSKY | None = None
        self.lm: LunarModule | None = None
        self.imu: IMU | None = None
        self.t = 0.0                       # simulation time (s) since scenario start
        self.get0 = 0.0                    # GET (s) at scenario start
        self.cycle_accum = 0.0
        self.site_radius = 0.0
        self.land0 = np.zeros(3)           # landing site in REF at TLAND
        self.pole = np.zeros(3)
        self.events: list[tuple[float, str]] = []
        self.log_rows: list[Telemetry] = []
        self.log_path = log_path
        self.flying = False                # True once the vehicle state and the AGC clock are coupled
        self._events_file = None
        self._events_writer = None
        self.crew = Crew(self)
        self.lr_pos2_cmd_time: float | None = None
        self.last_alarm = ""
        self.touchdown_state: dict | None = None
        self.tig: float | None = None
        self.log_interval = 0.5
        self._log_file = None
        self._log_writer = None

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    @property
    def get(self) -> float:
        return self.get0 + self.t

    def event(self, msg: str):
        self.events.append((self.t, msg))
        if self.verbose:
            print(f"[{fmt_get(self.get)}] {msg}", flush=True)
        if self.log_path:                      # <log>.events.csv, replayed by the 3D viewer
            if self._events_file is None:
                self._events_file = open(events_path(self.log_path), "w", newline="")
                self._events_writer = csv.writer(self._events_file)
                self._events_writer.writerow(["t", "get", "event"])
            self._events_writer.writerow([f"{self.t:.2f}", f"{self.get:.2f}", msg])
            self._events_file.flush()

    def progress(self, msg: str):
        """Setup progress for the terminal only (not an event, not replayed by the viewer)."""
        if self.verbose:
            print(f"[setup] {msg}", flush=True)

    def run_agc(self, seconds: float):
        """Advance only the AGC (used during setup)."""
        self.cpu.run(int(seconds * CYCLES_PER_SECOND))

    def press(self, key: str, why: str = ""):
        self.dsky.press(key)
        if why:
            self.event(f"crew: {key}  ({why})")
        if key.upper() == "PRO":
            self.crew.pro_pending_release = self.t + 0.4

    def type_keys(self, keys: str, gap: float = 0.25):
        """Key a DSKY sequence.  Once the scenario is flying, the whole simulation advances
        between the keystrokes: running only the AGC would put its clock and its state
        vector ahead of the vehicle (1.75 s for V37E63E at 1.7 km/s = 3 km downrange)."""
        for k in keys:
            self.dsky.press(k)
            if self.flying:
                for _ in range(int(round(gap / self.dt))):
                    self.step()
            else:
                self.run_agc(gap)

    def wait_display(self, verb: str, noun: str, timeout: float = 30.0, flashing: bool | None = True) -> bool:
        """Run the AGC until the DSKY shows verb/noun (setup phase only)."""
        deadline = self.cpu.seconds + timeout
        while self.cpu.seconds < deadline:
            self.run_agc(0.1)
            s = self.dsky.state(flash=False)
            if s.verb == verb and s.noun == noun and (flashing is None or s.flashing == flashing):
                return True
        return False

    def alarm_codes(self) -> str:
        e = self.cpu.e
        ea = self.prog.symbol("FAILREG").erasable_address()
        codes = [e[ea + i] & 0o77777 for i in range(3)]
        return " ".join(f"{c:05o}" for c in codes if c)

    # ------------------------------------------------------------------
    # AGC initialisation
    # ------------------------------------------------------------------
    def fresh_agc(self) -> AGC:
        cpu = AGC(self.prog.fixed)
        self.cpu = cpu
        self.dsky = DSKY(cpu)
        return cpu

    def agc_state_key(self, get_seconds: float) -> str:
        """Identifies the AGC state basic_setup produces: the rope, the pad load, the
        setup procedure itself and the clock it sets.  Any change invalidates the cache."""
        h = hashlib.sha256()
        h.update(repr(self.prog.fixed).encode())
        from . import padload
        h.update(inspect.getsource(padload).encode())
        h.update(inspect.getsource(LandingSimulation.basic_setup).encode())
        h.update(f"{get_seconds:.2f}".encode())
        return h.hexdigest()

    def restore_setup(self, get_seconds: float) -> bool:
        """Load the AGC state after basic_setup from the cache file, if it matches."""
        if not self.agc_cache:
            return False
        try:
            with open(self.agc_cache) as f:
                d = json.load(f)
        except OSError:
            return False
        except ValueError:
            self.progress(f"{self.agc_cache} is not valid JSON - fresh start")
            return False
        if not isinstance(d, dict) or d.get("key") != self.agc_state_key(get_seconds):
            self.progress(f"{self.agc_cache} is stale (rope, pad load, setup or clock changed) - fresh start")
            return False
        try:
            self.cpu.load_state(d["cpu"])
            self.dsky.rows = [int(x) for x in d["dsky_rows"]]
        except (KeyError, ValueError, TypeError, AttributeError):
            self.cpu.reset()                        # do not continue from a half-restored machine
            self.dsky.rows = [0] * 16
            self.progress(f"{self.agc_cache} is unreadable - fresh start")
            return False
        self.event(f"AGC state after the IMU turn-on sequence restored from {self.agc_cache} "
                   f"(AGC clock {fmt_get(get_seconds)}; delete the file for a fresh start)")
        return True

    def save_setup(self, get_seconds: float):
        if not self.agc_cache:
            return
        with open(self.agc_cache, "w") as f:
            json.dump({"key": self.agc_state_key(get_seconds), "get": get_seconds,
                       "cpu": self.cpu.save_state(), "dsky_rows": self.dsky.rows}, f)
        self.progress(f"AGC state saved to {self.agc_cache}; the next start skips the turn-on sequence")

    def basic_setup(self, get_seconds: float):
        """Fresh start, P00, pad load, flags, discretes, clock."""
        cpu, prog = self.cpu, self.prog
        self._setup_get = get_seconds
        if self.restore_setup(get_seconds):
            return
        wall0 = time.monotonic()
        self.progress("fresh start of the AGC: self-check, 90 s IMU turn-on sequence, ISS settling, V37E00E "
                      "and the pad load - about 110 s of AGC time, the emulator needs a while for that ...")
        self.run_agc(3.0)
        # IMU turn-on: the AGC runs a 90 s "ISS turn-on delay" when it sees IMU OPERATE
        # together with ISS TURN ON REQUEST; it answers with channel 12 bit 15 and the
        # hardware then drops the request.  (Channels 30-33 are active-low.)
        cpu.chan[0o30] &= ~(0o400 | 0o20000)
        for i in range(1200):
            self.run_agc(0.1)
            if cpu.chan[0o12] & 0o40000:
                break
            if i % 300 == 299:
                self.progress(f"IMU turn-on sequence {(i + 1) // 10:3d}/90 s of AGC time "
                              f"({time.monotonic() - wall0:.0f} s elapsed)")
        else:
            raise RuntimeError("IMU turn-on sequence did not complete")
        self.progress(f"IMU turn-on sequence complete ({time.monotonic() - wall0:.0f} s elapsed); "
                      "ISS settling, V37E00E, pad load ...")
        cpu.chan[0o30] |= 0o20000
        self.run_agc(12.0)
        self.type_keys("V37E00E")
        self.run_agc(2.0)
        for w in apply_padload(cpu, prog):
            self.event("padload: " + w)
        e = cpu.e
        flag3 = prog.symbol("FLAGWRD3").erasable_address()
        e[flag3] |= 0o10000                     # REFSMFLG: REFSMMAT valid
        flag8 = prog.symbol("FLAGWRD8").erasable_address()
        e[flag8] |= 0o2000                      # LMOONFLG: LM state vector is moon-centred
        self.set_clock(get_seconds)
        cpu.chan[0o30] &= ~(0o1000 | 0o20)           # LGC has control, auto throttle
        cpu.chan[0o31] &= ~0o20000                   # mode control switch: AUTO
        cpu.chan[0o33] &= ~0o40                      # LR antenna in position 1
        cpu.chan[0o33] |= 0o200 | 0o20               # LR range/velocity data not good (no radar model yet)
        self.progress(f"AGC in P00 with the pad load after {time.monotonic() - wall0:.0f} s")
        self.save_setup(get_seconds)

    def load_state_vector(self, r: np.ndarray, v: np.ndarray, get_seconds: float):
        """Permanent LM state vector (Encke form).  Moon-centred vectors are scaled
        B27 (m) and B5 (m/cs).  The conic (RCV, VCV, TC) equals the rectified state,
        the deviations (DELTA, NUV) and the Kepler guess (XKEP) are zero."""
        zero = np.zeros(3)
        for name, value, scale in (("RRECTLEM", r, 27), ("VRECTLEM", v / 100.0, 5),
                                   ("DELTALEM", zero, 27), ("NUVLEM", zero, 5),
                                   ("RCVLEM", r, 27), ("VCVLEM", v / 100.0, 5)):
            write_vector(self.cpu, self.prog, name, value, scale)
        write_dp(self.cpu, self.prog, "TETLEM", get_seconds * 100.0, 28)
        write_dp(self.cpu, self.prog, "TCLEM", get_seconds * 100.0, 28)
        write_dp(self.cpu, self.prog, "XKEPLEM", 0.0, 28)

    def load_csm_state_vector(self, r: np.ndarray, v: np.ndarray, get_seconds: float):
        """Permanent CSM state vector (needed by P63, which integrates Columbia's orbit too)."""
        zero = np.zeros(3)
        for name, value, scale in (("RRECTCSM", r, 27), ("VRECTCSM", v / 100.0, 5),
                                   ("DELTACSM", zero, 27), ("NUVCSM", zero, 5),
                                   ("RCVCSM", r, 27), ("VCVCSM", v / 100.0, 5)):
            write_vector(self.cpu, self.prog, name, value, scale)
        write_dp(self.cpu, self.prog, "TETCSM", get_seconds * 100.0, 28)
        write_dp(self.cpu, self.prog, "TCCSM", get_seconds * 100.0, 28)
        write_dp(self.cpu, self.prog, "XKEPCSM", 0.0, 28)
        flag8 = self.prog.symbol("FLAGWRD8").erasable_address()
        self.cpu.e[flag8] |= 0o4000                   # CMOONFLG: CSM state vector is moon-centred

    def set_clock(self, get_seconds: float):
        cs = int(round(get_seconds * 100))
        self.cpu.e[0o24] = (cs >> 14) & 0o37777
        self.cpu.e[0o25] = cs & 0o37777

    def load_dap_data(self, lm_mass_lb: float):
        """R03 (V48): vehicle configuration, mass, gimbal trim - as the crew did it."""
        self.progress("loading the DAP data (V48) ...")
        self.type_keys("V48E")
        if not self.wait_display("01", "46"):
            self.event("WARNING: V48 did not show N46")
            return
        self.type_keys("V21E" + DAP_CONFIG + "E")
        self.wait_display("01", "46")
        self.press("PRO")
        self.run_agc(0.5)
        self.dsky.release_pro()
        if not self.wait_display("06", "47"):
            self.event("WARNING: V48 did not show N47")
            return
        self.type_keys(f"V21E+{int(round(lm_mass_lb)):05d}E")
        self.wait_display("06", "47")
        self.press("PRO")
        self.run_agc(0.5)
        self.dsky.release_pro()
        if self.wait_display("06", "48", timeout=10):
            self.press("PRO")
            self.run_agc(0.5)
            self.dsky.release_pro()
        self.run_agc(2.0)
        mass_kg = read_dp(self.cpu, self.prog, "MASS", 16)
        self.event(f"DAP data loaded: config {DAP_CONFIG}, AGC mass {mass_kg:.0f} kg")

    # ------------------------------------------------------------------
    # Scenario construction
    # ------------------------------------------------------------------
    def probe_landing_site(self) -> tuple[np.ndarray, np.ndarray]:
        """Let the AGC compute the inertial landing site (LAND) and the lunar
        rotation vector (WM) from its own ephemeris routines: start P63 once
        with an identity REFSMMAT and read the results back."""
        self.fresh_agc()
        tland = TLAND_CS / 100.0
        self.basic_setup(tland - NOMINAL_PDI_TO_LANDING - LEAD_TIME)
        ident = np.eye(3)
        IMU(self.cpu, ident).write_refsmmat(self.prog)
        rls = read_vector(self.cpu, self.prog, "RLS", 27)
        r0 = unit(rls) * (np.linalg.norm(rls) + PERILUNE_ALT)
        v0 = np.cross(np.array([0.0, 0.0, 1.0]), unit(rls))
        v0 = unit(v0) * math.sqrt(MU_MOON / np.linalg.norm(r0))
        self.set_clock(self._setup_get)
        self.load_state_vector(r0, v0, self._setup_get)
        self.type_keys("V37E63E")
        land = np.zeros(3)
        tpip = tland
        for _ in range(60):
            self.run_agc(0.5)
            land = read_vector(self.cpu, self.prog, "LAND", 24)
            tpip = read_dp(self.cpu, self.prog, "TPIP", 28) / 100.0
            if abs(np.linalg.norm(land) - np.linalg.norm(rls)) < 5.0:
                break
        wm = read_vector(self.cpu, self.prog, "WM", 0)
        if np.linalg.norm(wm) == 0:
            raise RuntimeError("AGC did not compute WM")
        if abs(np.linalg.norm(land) - np.linalg.norm(rls)) >= 5.0:
            raise RuntimeError(f"AGC did not compute LAND (|LAND|={np.linalg.norm(land):.0f}, |RLS|={np.linalg.norm(rls):.0f})")
        # LAND is the site at time TPIP: the ignition algorithm initialises it at TLAND and
        # every guidance pass (TTFINCR) rotates it with WM by TPIP - TPIPOLD.  Refer it to
        # TLAND so that landing_site_now() can rotate it to any time.
        pole = unit(wm)
        land0 = rotate_about(land, pole, OMEGA_MOON * (tland - tpip))
        self.event(f"probe: LAND read at TPIP = TLAND {tpip - tland:+.1f} s, referred to TLAND")
        return land0, pole

    def build_scenario(self):
        tland = TLAND_CS / 100.0
        land = pole = None
        if self.probe_cache:
            try:
                import json
                with open(self.probe_cache) as f:
                    d = json.load(f)
                if d.get("epoch") != "TLAND":
                    raise ValueError("old cache format (LAND not referred to TLAND)")
                land, pole = np.array(d["land"]), np.array(d["pole"])
                self.event("landing site / lunar pole taken from cache")
            except (OSError, KeyError, ValueError):
                land = pole = None
        if land is None:
            self.event("probing the AGC for the inertial landing site and lunar rotation axis ...")
            land, pole = self.probe_landing_site()
            if self.probe_cache:
                import json
                with open(self.probe_cache, "w") as f:
                    json.dump({"land": land.tolist(), "pole": pole.tolist(), "epoch": "TLAND"}, f)
        self.land0 = land
        self.pole = pole
        self.site_radius = float(np.linalg.norm(land))
        lhat = unit(land)
        east = unit(np.cross(pole, lhat))
        west = -east
        self.event(f"landing site radius {self.site_radius / 1000:.3f} km, lunar pole {np.round(pole, 4)}")

        # descent orbit: perilune at the PDI point, uprange (east) of the site
        theta = PDI_DOWNRANGE / self.site_radius
        p_hat = math.cos(theta) * lhat + math.sin(theta) * east
        v_hat = math.sin(theta) * lhat - math.cos(theta) * east
        rp = self.site_radius + PERILUNE_ALT
        ra = self.site_radius + APOLUNE_ALT
        vp = math.sqrt(MU_MOON * (2.0 / rp - 2.0 / (rp + ra)))
        r_pdi = p_hat * rp
        v_pdi = v_hat * vp
        t_pdi = tland - NOMINAL_PDI_TO_LANDING
        # back-propagate to the scenario start
        r, v = self.propagate(r_pdi, v_pdi, -LEAD_TIME)
        self.get0 = t_pdi - LEAD_TIME
        self.refsmmat = landing_site_refsmmat(land, west)

        # the real computer
        self.fresh_agc()
        self.lm = LunarModule(self.cpu, MU_MOON)
        self.lm.r, self.lm.v = r, v
        # attitude: X axis retrograde (engine toward the direction of flight), windows down
        x = -unit(v)
        z = -unit(r)
        z = unit(z - np.dot(z, x) * x)
        y = np.cross(z, x)
        self.lm.c = np.array([x, y, z])
        self.imu = IMU(self.cpu, self.refsmmat)
        self.basic_setup(self.get0)
        self.imu.write_refsmmat(self.prog)
        self.imu.set_attitude(self.lm.c)
        self.load_dap_data(PDI_MASS / 0.45359237)
        if self.use_lr:
            self.lr = LandingRadar(self.cpu)
        self.run_agc(1.0)
        # the clock and the state vectors are set last so that TETLEM equals the AGC time
        self.set_clock(self.get0)
        self.load_state_vector(r, v, self.get0)
        # Columbia: circular 60 nmi orbit in the same plane, some 150 km ahead of Eagle
        rc = self.site_radius + APOLUNE_ALT
        phi = theta - 150000.0 / rc + (LEAD_TIME * vp / rp)      # LM angle at t0 minus lead
        u = math.cos(phi) * lhat + math.sin(phi) * east
        d = math.sin(phi) * lhat - math.cos(phi) * east
        self.load_csm_state_vector(u * rc, d * math.sqrt(MU_MOON / rc), self.get0)
        alt = np.linalg.norm(r) - self.site_radius
        self.event(f"scenario ready: GET {fmt_get(self.get0)}, altitude {alt / 1000:.1f} km, "
                   f"speed {np.linalg.norm(v):.0f} m/s, nominal PDI in {LEAD_TIME:.0f} s, TLAND {fmt_get(tland)}")

    def propagate(self, r: np.ndarray, v: np.ndarray, duration: float, step: float = 1.0):
        """Two-body propagation with RK4 (negative duration propagates backwards)."""
        n = int(abs(duration) / step)
        h = step if duration > 0 else -step

        def acc(x):
            return -MU_MOON * x / np.linalg.norm(x) ** 3

        for _ in range(n):
            k1v, k1r = acc(r), v
            k2v, k2r = acc(r + 0.5 * h * k1r), v + 0.5 * h * k1v
            k3v, k3r = acc(r + 0.5 * h * k2r), v + 0.5 * h * k2v
            k4v, k4r = acc(r + h * k3r), v + h * k3v
            r = r + h / 6 * (k1r + 2 * k2r + 2 * k3r + k4r)
            v = v + h / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        return r, v

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------
    def landing_site_now(self) -> np.ndarray:
        """Inertial position of the landing site at the current time (moon rotation)."""
        return rotate_about(self.land0, self.pole, OMEGA_MOON * (self.get - TLAND_CS / 100.0))

    def step(self):
        dt = self.dt
        # AGC runs in lock-step with the vehicle
        self.cycle_accum += dt * CYCLES_PER_SECOND
        cycles = int(self.cycle_accum)
        self.cycle_accum -= cycles
        self.cpu.run(cycles)
        # vehicle and sensors
        self.lm.step(dt)
        self.imu.update_cdus(self.lm.c)
        self.imu.update_pipas(self.lm.specific_force_ref, dt)
        self.t += dt
        # landing radar
        if self.cpu.chan[0o12] & 0o10000 and self.lr_pos2_cmd_time is None:
            self.lr_pos2_cmd_time = self.t
            self.event("LR antenna commanded to position 2")
        if self.lr is not None:
            v_rel = self.lm.v - np.cross(self.pole * OMEGA_MOON, self.lm.r)
            was_good = (self.lr.range_good, self.lr.vel_good)
            self.lr.update(self.t, self.lm.r, v_rel, self.lm.c, self.site_radius)
            if (self.lr.range_good, self.lr.vel_good) != was_good:
                self.event(f"LR range data {'good' if self.lr.range_good else 'lost'}, velocity data "
                           f"{'good' if self.lr.vel_good else 'lost'}")
        elif self.cpu.chan[0o12] & 0o10000 and self.t - self.lr_pos2_cmd_time > 10.0:
            self.cpu.chan[0o33] |= 0o40            # no longer in position 1
            self.cpu.chan[0o33] &= ~0o100          # in position 2
        if self.crew.pro_pending_release and self.t >= self.crew.pro_pending_release:
            self.dsky.release_pro()
            self.crew.pro_pending_release = 0.0

    def site_frame(self) -> tuple[np.ndarray, np.ndarray]:
        """Landing site position and the ENU (east, north, up) axes as rows of a 3x3 matrix."""
        site = self.landing_site_now()
        up = unit(site)
        east = unit(np.cross(self.pole, up))
        north = np.cross(up, east)
        return site, np.array([east, north, up])

    def telemetry(self) -> Telemetry:
        lm = self.lm
        r_hat = unit(lm.r)
        hdot = float(np.dot(lm.v, r_hat))
        v_h = lm.v - hdot * r_hat
        s = self.dsky.state(flash=False)
        site, enu = self.site_frame()
        rel = enu @ (lm.r - site)
        bx = enu @ lm.c[0]
        bz = enu @ lm.c[2]
        lr = ""
        if self.lr is not None:
            lr = ("R" if self.lr.range_good else "-") + ("V" if self.lr.vel_good else "-") + str(self.lr.position)
        return Telemetry(self.t, self.get, lm.altitude(self.site_radius), hdot, float(np.linalg.norm(v_h)),
                         lm.thrust, lm.mass, lm.pitch_from_vertical_deg(), s.prog, s.verb, s.noun,
                         s.r1, s.r2, s.r3, self.alarm_codes(),
                         tuple(float(x) for x in rel), tuple(float(x) for x in bx), tuple(float(x) for x in bz),
                         (lm._ch6 << 8) | lm._ch5,
                         (math.degrees(lm.gimbal_pitch), math.degrees(lm.gimbal_roll)), lr)

    def telemetry_row(self, tm: Telemetry) -> list:
        return [f"{tm.t:.1f}", f"{tm.get:.2f}", f"{tm.alt:.1f}", f"{tm.hdot:.2f}", f"{tm.vhor:.2f}",
                f"{tm.thrust:.0f}", f"{tm.mass:.1f}", f"{tm.pitch:.2f}", tm.prog, tm.verb, tm.noun,
                tm.r1, tm.r2, tm.r3, tm.alarms,
                f"{tm.enu[0]:.1f}", f"{tm.enu[1]:.1f}", f"{tm.enu[2]:.1f}",
                f"{tm.bx[0]:.4f}", f"{tm.bx[1]:.4f}", f"{tm.bx[2]:.4f}",
                f"{tm.bz[0]:.4f}", f"{tm.bz[1]:.4f}", f"{tm.bz[2]:.4f}",
                f"{tm.jets:05o}", f"{tm.gimbal[0]:.2f}", f"{tm.gimbal[1]:.2f}", tm.lr]

    def status_line(self, tm: Telemetry) -> str:
        site = self.landing_site_now()
        rng = float(np.linalg.norm(self.lm.r - site))
        return (f"{fmt_get(tm.get)} P{tm.prog} V{tm.verb} N{tm.noun} [{tm.r1}|{tm.r2}|{tm.r3}] "
                f"alt {ft(tm.alt):8.0f} ft  hdot {ft(tm.hdot):7.1f} ft/s  vh {ft(tm.vhor):7.1f} ft/s  "
                f"rng {rng / 1000:6.1f} km  thr {tm.thrust / DPS_FTP * 100:5.1f}%  m {tm.mass:6.0f} kg  "
                f"pitch {tm.pitch:5.1f}  gmb {math.degrees(self.lm.gimbal_pitch):+.2f}/{math.degrees(self.lm.gimbal_roll):+.2f}"
                + (f"  ALARM {tm.alarms}" if tm.alarms else ""))

    def run(self, until: float | None = None, status_every: float = 5.0):
        """Fly the descent.  ``until`` limits simulation time (s) for test runs."""
        self.build_scenario()
        self.flying = True
        self.event("crew: V37E63E - select P63 braking phase")
        self.type_keys("V37E63E")
        next_status = 0.0
        next_log = 0.0
        next_crew = 0.0
        last_prog = None
        wall0 = time.monotonic()
        tig_logged = False
        while True:
            self.step()
            if self.realtime:
                lag = self.t - (time.monotonic() - wall0)
                if lag > 0:
                    time.sleep(min(lag, 0.05))
            if self.t >= next_crew:
                next_crew = self.t + 0.5
                self.crew.tick()
                prog = self.dsky.state(flash=False).prog
                if prog != last_prog and prog.strip():
                    self.event(f"PROG {prog}")
                    last_prog = prog
                alarms = self.alarm_codes()
                if alarms != self.last_alarm:
                    if alarms:
                        self.event(f"program alarm(s): {alarms}")
                    self.last_alarm = alarms
                if not tig_logged:
                    tig = read_dp(self.cpu, self.prog, "TIG", 28) / 100.0
                    if 0 < tig - self.get < 2000:
                        self.tig = tig
                        tig_logged = True
                        self.event(f"AGC computed TIG = {fmt_get(tig)} (in {tig - self.get:.1f} s)")
                if self.tig and not self.lm.engine_armed and self.get >= self.tig - 60 and not self.lm.touchdown:
                    self.lm.set_engine_armed(True)
                    # The LGC positions the trim gimbal before ignition by driving it for the
                    # pad-loaded PITTIME/ROLLTIME from its stowed position.  The simulated
                    # actuator takes the position reached by that procedure as the trim
                    # (thrust through the CG) reference.
                    self.event(f"crew: DESCENT ENGINE ARM (TIG-60 s); gimbal trim reference set "
                               f"(drive so far {math.degrees(self.lm.gimbal_pitch):+.2f}/{math.degrees(self.lm.gimbal_roll):+.2f} deg)")
                    self.lm.gimbal_pitch = 0.0
                    self.lm.gimbal_roll = 0.0
                if self.lm.engine_on and self.lm.engine_on_events == 1 and not getattr(self, "_ign_logged", False):
                    self._ign_logged = True
                    self.event(f"DPS ignition at GET {fmt_get(self.get)}")
            if self.t >= next_log:
                next_log = self.t + self.log_interval
                self.log_telemetry()
            if self.t >= next_status:
                next_status = self.t + status_every
                if self.verbose:
                    print(self.status_line(self.log_rows[-1] if self.log_rows else self.telemetry()), flush=True)
            # Contact is a property of the vehicle geometry, not of the engine
            # state.  In particular, a failed or prematurely terminated burn
            # must end in a reported ballistic impact rather than letting the
            # point-mass vehicle fly through the lunar surface indefinitely.
            if self.lm.altitude(self.site_radius) <= 0.0:
                self.touchdown()
                break
            if until is not None and self.t >= until:
                self.event(f"time limit {until:.0f} s reached")
                break
            if self.cpu.alarm_log and len(self.cpu.alarm_log) > 50:
                self.event("too many hardware alarms, aborting")
                break
        self.close_log()
        return self.touchdown_state

    def touchdown(self):
        lm = self.lm
        powered_at_contact = lm.engine_on
        r_hat = unit(lm.r)
        hdot = float(np.dot(lm.v, r_hat))
        v_h = lm.v - hdot * r_hat
        site = self.landing_site_now()
        miss = lm.r - site
        miss_h = miss - np.dot(miss, r_hat) * r_hat
        lm.engine_stop()
        lm.touchdown = True
        self.touchdown_state = {
            "get": self.get, "vertical_speed": hdot, "horizontal_speed": float(np.linalg.norm(v_h)),
            "miss_distance": float(np.linalg.norm(miss_h)), "mass": lm.mass,
            "dps_propellant": lm.dps_propellant, "prog": self.dsky.state(flash=False).prog,
            "tilt_deg": lm.pitch_from_vertical_deg(),
            "outcome": "powered_touchdown" if powered_at_contact else "ballistic_impact",
        }
        if powered_at_contact:
            self.event("*** CONTACT - engine stop ***")
        else:
            self.event("*** BALLISTIC IMPACT - engine was already off ***")
        self.event(f"contact at GET {fmt_get(self.get)}: vertical {ft(hdot):+.1f} ft/s, horizontal {ft(np.linalg.norm(v_h)):.1f} ft/s, "
                   f"{np.linalg.norm(miss_h):.0f} m from the target, tilt {lm.pitch_from_vertical_deg():.1f} deg, "
                   f"DPS propellant left {lm.dps_propellant:.0f} kg")
        self.run_agc(2.0)

    def log_telemetry(self):
        """Record one telemetry sample and append it to the CSV (flushed, for live viewers)."""
        tm = self.telemetry()
        self.log_rows.append(tm)
        if self.log_path:
            if self._log_file is None:
                self._log_file = open(self.log_path, "w", newline="")
                self._log_writer = csv.writer(self._log_file)
                self._log_writer.writerow(CSV_FIELDS)
            self._log_writer.writerow(self.telemetry_row(tm))
            self._log_file.flush()

    def close_log(self):
        if self._events_file is not None:
            self._events_file.close()
            self._events_file = None
        if self._log_file is not None:
            self._log_file.close()
            self._log_file = None
            if self.verbose:
                print(f"telemetry written to {self.log_path}")
