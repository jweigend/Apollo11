"""Inertial measurement unit model: gimbals, CDUs and PIPAs.

Frames
------
* REF: the AGC's inertial "basic reference" frame (the simulation's inertial frame).
* SM:  stable member (platform) frame.  ``REFSMMAT`` rows are the SM axes in REF.
* NB:  navigation base = LM body axes (+X up through the ascent hatch / thrust axis,
       +Z forward out the windows, +Y to the right).

Gimbal angles (LM): outer gimbal about X (OGA, "yaw"), inner gimbal about
Y (IGA, "pitch"), middle gimbal about Z (MGA, "roll"; gimbal lock near 90 deg).
The direction cosine matrix from SM to NB is

    C_nb_sm = R1(OGA) . R3(MGA) . R2(IGA)

with Ri the standard passive (frame) rotation matrices.  CDU counters hold
the gimbal angles as 15-bit two's-complement words, 2**15 pulses per
revolution.  The PIPAs integrate the non-gravitational acceleration along the
SM axes; one pulse is 1 cm/s.
"""

from __future__ import annotations

import math

import numpy as np

from ..cpu import CDUX, CDUY, CDUZ, PIPAX, PIPAY, PIPAZ
from .scaling import angle_to_cdu, dp, dp_value

PIPA_CM_PER_PULSE = 1.0


def rot1(a: float) -> np.ndarray:
    c, s = math.cos(a), math.sin(a)
    return np.array([[1, 0, 0], [0, c, s], [0, -s, c]])


def rot2(a: float) -> np.ndarray:
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, 0, -s], [0, 1, 0], [s, 0, c]])


def rot3(a: float) -> np.ndarray:
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, s, 0], [-s, c, 0], [0, 0, 1]])


def dcm_from_gimbals(oga: float, iga: float, mga: float) -> np.ndarray:
    """C_nb_sm for outer/inner/middle gimbal angles (radians)."""
    return rot1(oga) @ rot3(mga) @ rot2(iga)


def gimbals_from_dcm(c: np.ndarray) -> tuple[float, float, float]:
    """Inverse of :func:`dcm_from_gimbals`: returns (oga, iga, mga)."""
    mga = math.asin(max(-1.0, min(1.0, c[0, 1])))
    iga = math.atan2(-c[0, 2], c[0, 0])
    oga = math.atan2(-c[2, 1], c[1, 1])
    return oga, iga, mga


def unit(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


def landing_site_refsmmat(land_ref: np.ndarray, flight_dir_ref: np.ndarray) -> np.ndarray:
    """Platform orientation for the landing: X_sm up at the site, Z_sm along the
    horizontal flight direction, Y_sm = Z x X (right-handed)."""
    x = unit(land_ref)
    z = flight_dir_ref - np.dot(flight_dir_ref, x) * x
    z = unit(z)
    y = np.cross(z, x)
    return np.array([x, y, z])


class IMU:
    """Feeds the AGC's CDU and PIPA counters from the true vehicle state."""

    def __init__(self, cpu, refsmmat: np.ndarray):
        self.cpu = cpu
        self.refsmmat = refsmmat            # C_sm_ref
        self.cdu = [0, 0, 0]                # current counter contents we have driven
        self.pipa_acc = np.zeros(3)         # accumulated velocity (cm/s) not yet pulsed
        self.pipa_counts = np.zeros(3, dtype=int)
        self.gimbals = (0.0, 0.0, 0.0)

    def write_refsmmat(self, prog):
        """Store the REFSMMAT into erasable (half-unit vectors, DP, scaled B1)."""
        ea = prog.symbol("REFSMMAT").erasable_address()
        words = []
        for row in self.refsmmat:
            for comp in row:
                words += dp(comp, 1)
        for i, w in enumerate(words):
            self.cpu.e[ea + i] = w

    def gimbal_angles(self, c_nb_ref: np.ndarray) -> tuple[float, float, float]:
        c_nb_sm = c_nb_ref @ self.refsmmat.T
        return gimbals_from_dcm(c_nb_sm)

    def set_attitude(self, c_nb_ref: np.ndarray):
        """Load the CDU counters directly (initialisation, no pulses)."""
        oga, iga, mga = self.gimbal_angles(c_nb_ref)
        self.gimbals = (oga, iga, mga)
        for reg, ang, i in ((CDUX, oga, 0), (CDUY, iga, 1), (CDUZ, mga, 2)):
            self.cdu[i] = angle_to_cdu(ang)
            self.cpu.e[reg] = self.cdu[i]

    def update_cdus(self, c_nb_ref: np.ndarray, max_pulses: int = 400):
        """Pulse the CDU counters toward the true gimbal angles."""
        oga, iga, mga = self.gimbal_angles(c_nb_ref)
        self.gimbals = (oga, iga, mga)
        for reg, ang, i in ((CDUX, oga, 0), (CDUY, iga, 1), (CDUZ, mga, 2)):
            target = angle_to_cdu(ang)
            delta = (target - self.cdu[i]) % 32768
            if delta > 16384:
                delta -= 32768
            n = min(abs(delta), max_pulses)
            inc_type = 1 if delta > 0 else 3          # PCDU / MCDU
            for _ in range(n):
                self.cpu.unprogrammed_increment(reg, inc_type)
            self.cdu[i] = (self.cdu[i] + (n if delta > 0 else -n)) % 32768

    def update_pipas(self, specific_force_ref: np.ndarray, dt: float):
        """Integrate non-gravitational acceleration (m/s^2, REF frame) into PIPA pulses."""
        dv_sm = self.refsmmat @ specific_force_ref * dt * 100.0     # cm/s
        self.pipa_acc += dv_sm
        for i, reg in enumerate((PIPAX, PIPAY, PIPAZ)):
            n = int(self.pipa_acc[i] / PIPA_CM_PER_PULSE)
            if n == 0:
                continue
            inc_type = 0 if n > 0 else 2                 # PINC / MINC
            for _ in range(abs(n)):
                self.cpu.unprogrammed_increment(reg, inc_type)
            self.pipa_acc[i] -= n * PIPA_CM_PER_PULSE
            self.pipa_counts[i] += n


def read_vector(cpu, prog, name: str, scale: int) -> np.ndarray:
    """Read an interpretive DP vector (6 words) from erasable."""
    ea = prog.symbol(name).erasable_address()
    e = cpu.e
    return np.array([dp_value(e[ea + 2 * i], e[ea + 2 * i + 1], scale) for i in range(3)])


def write_vector(cpu, prog, name: str, values, scale: int):
    ea = prog.symbol(name).erasable_address()
    words = []
    for v in values:
        words += dp(float(v), scale)
    for i, w in enumerate(words):
        cpu.e[ea + i] = w


def write_dp(cpu, prog, name: str, value: float, scale: int):
    ea = prog.symbol(name).erasable_address()
    hi, lo = dp(value, scale)
    cpu.e[ea] = hi
    cpu.e[ea + 1] = lo


def read_dp(cpu, prog, name: str, scale: int) -> float:
    ea = prog.symbol(name).erasable_address()
    return dp_value(cpu.e[ea], cpu.e[ea + 1], scale)
