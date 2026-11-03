"""Unit tests for the landing-simulation helpers (scaling, IMU geometry, pad load)."""

import math
import sys
import errno
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from agc.sim.scaling import dp, dp_value, sp, sp_value, tp, tp_value, angle_to_cdu, cdu_to_angle  # noqa: E402
from agc.sim.imu import dcm_from_gimbals, gimbals_from_dcm, landing_site_refsmmat  # noqa: E402
from agc.sim.padload import PADLOAD  # noqa: E402
from agc.sim.mission import LandingSimulation  # noqa: E402
from agc.sim import viewer  # noqa: E402


def test_dp_roundtrip_and_known_padload_values():
    # TLAND 36304920 cs at B28 -> 04247 34030 (pad load table)
    assert dp(36304920.0, 28) == [0o04247, 0o34030]
    # RLS x component 1588471.994 m at B27 -> 00301 34760
    assert dp(1588471.994, 27) == [0o00301, 0o34760]
    # negative: RIGNX -39782.453328 m at B24 -> 77731 44630
    assert dp(-39782.453328, 24) == [0o77731, 0o44630]
    for v, s in [(1.5e6, 27), (-0.3227, 10), (1e-5, -4), (36304920.0, 28)]:
        hi, lo = dp(v, s)
        assert abs(dp_value(hi, lo, s) - v) < abs(v) * 1e-7 + 2.0 ** (s - 28)


def test_sp_and_tp():
    assert sp(2124.4, 14) == 0o04114          # LOWCRIT
    assert sp(-1.0, 14) == 0o77776
    assert sp_value(0o77776, 14) == -1.0
    assert tp(134472000.0, 42) == [0o00000, 0o20017, 0o20500]   # TEPHEM
    w = tp(134472000.0, 42)
    assert abs(tp_value(*w, 42) - 134472000.0) < 1.0


def test_cdu_angles():
    assert angle_to_cdu(0.0) == 0
    assert angle_to_cdu(math.pi) == 16384
    assert angle_to_cdu(-math.pi / 2) == 24576       # -90 deg -> two's complement 0o60000
    assert abs(cdu_to_angle(angle_to_cdu(1.234)) - 1.234) < 2 * math.pi / 32768


def test_gimbal_dcm_roundtrip():
    for angles in [(0.1, -0.4, 0.2), (2.9, 1.2, -0.3), (-3.0, 0.0, 0.7)]:
        c = dcm_from_gimbals(*angles)
        assert np.allclose(c @ c.T, np.eye(3))
        back = gimbals_from_dcm(c)
        assert np.allclose(dcm_from_gimbals(*back), c, atol=1e-9)


def test_landing_site_refsmmat_is_orthonormal_and_oriented():
    land = np.array([1373511.0, 976378.0, 412837.0])
    west = np.array([0.3, -0.5, 0.1])
    m = landing_site_refsmmat(land, west)
    assert np.allclose(m @ m.T, np.eye(3))
    assert np.allclose(m[0], land / np.linalg.norm(land))
    assert abs(np.dot(m[2], land)) < 1e-6          # Z horizontal
    assert np.dot(m[2], west) > 0                   # Z along the flight direction


def test_padload_words_are_15_bit():
    for name, (addr, words) in PADLOAD.items():
        assert 0 <= addr <= 0o3777, name
        for w in words:
            assert 0 <= w <= 0o77777, name


def test_unpowered_surface_contact_is_reported_as_ballistic_impact():
    """A failed descent must terminate at the surface instead of passing through it."""
    sim = LandingSimulation.__new__(LandingSimulation)
    sim.get0 = 123.0
    sim.t = 0.0
    sim.lm = SimpleNamespace(
        r=np.array([1000.0, 0.0, 0.0]),
        v=np.array([-8.0, 3.0, 0.0]),
        mass=1000.0,
        dps_propellant=25.0,
        engine_on=False,
        touchdown=False,
        pitch_from_vertical_deg=lambda: 4.0,
        engine_stop=lambda: None,
    )
    sim.landing_site_now = lambda: np.array([1000.0, 0.0, 0.0])
    sim.dsky = SimpleNamespace(state=lambda flash=False: SimpleNamespace(prog="65"))
    sim.event = lambda message: None
    sim.run_agc = lambda seconds: None

    sim.touchdown()

    assert sim.lm.touchdown
    assert sim.touchdown_state["outcome"] == "ballistic_impact"
    assert sim.touchdown_state["vertical_speed"] == pytest.approx(-8.0)


def test_viewer_uses_next_port_when_preferred_port_is_busy(monkeypatch):
    attempts = []

    class FakeServer:
        def __init__(self, address, handler):
            attempts.append(address[1])
            if address[1] == 8765:
                raise OSError(errno.EADDRINUSE, "address already in use")

        def serve_forever(self):
            pass

    monkeypatch.setattr(viewer, "HTTPServer", FakeServer)
    viewer.serve("landing.csv", port=8765, open_browser=False, block=False)
    assert attempts == [8765, 8766]


@pytest.mark.skipif(not (ROOT / "agc" / "programs" / "luminary099" / "__init__.py").exists(), reason="no program")
def test_padload_addresses_match_symbol_table():
    from agc.program import load_program
    prog = load_program("luminary099")
    for name, (addr, words) in PADLOAD.items():
        sym = prog.symbol(name)
        assert sym is not None, name
        assert sym.erasable_address() == addr, f"{name}: table {addr:o} != assembled {sym.erasable_address():o}"
