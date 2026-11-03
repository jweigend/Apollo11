"""End-to-end: boot the converted Luminary099 and talk to it through the DSKY."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from agc.cpu import AGC, CYCLES_PER_SECOND  # noqa: E402
from agc.dsky import DSKY  # noqa: E402
from agc.program import load_program  # noqa: E402

pytestmark = pytest.mark.skipif(not (ROOT / "agc" / "programs" / "luminary099" / "__init__.py").exists(),
                                reason="run `python -m agc convert` first")


def press(cpu, dsky, keys, gap=0.3):
    for k in keys:
        dsky.press(k)
        cpu.run(int(gap * CYCLES_PER_SECOND))


def test_luminary_boots_without_hardware_alarms():
    prog = load_program("luminary099")
    cpu = AGC(prog.fixed)
    cpu.run(5 * CYCLES_PER_SECOND)
    assert cpu.alarm_log == []
    assert cpu.erasable_flat(prog.symbol("NEWJOB").value) == 0o77777   # idle: no job waiting
    assert cpu.e[0o25] != 0                                            # TIME1 is counting


def test_lamp_test_v35():
    prog = load_program("luminary099")
    cpu = AGC(prog.fixed)
    dsky = DSKY(cpu)
    cpu.run(3 * CYCLES_PER_SECOND)
    press(cpu, dsky, "V35E")
    cpu.run(2 * CYCLES_PER_SECOND)
    s = dsky.state(flash=False)
    assert s.verb == "88" and s.noun == "88" and s.flashing
    assert s.r1 == "+88888"
    assert s.lamps["UPLINK ACTY"] and s.lamps["GIMBAL LOCK"] and s.lamps["TRACKER"]


def test_clock_display_v16n36():
    prog = load_program("luminary099")
    cpu = AGC(prog.fixed)
    dsky = DSKY(cpu)
    cpu.run(3 * CYCLES_PER_SECOND)
    press(cpu, dsky, "V16N36E")
    cpu.run(2 * CYCLES_PER_SECOND)
    s = dsky.state(flash=False)
    assert s.verb == "16" and s.noun == "36"
    hundredths = int(s.r3.strip("+ "))
    agc_hundredths = int(cpu.seconds * 100)
    # R3 shows seconds in 1/100 s; allow for display latency
    assert abs(hundredths - agc_hundredths) < 150


def test_select_p00_with_v37():
    prog = load_program("luminary099")
    cpu = AGC(prog.fixed)
    dsky = DSKY(cpu)
    cpu.run(3 * CYCLES_PER_SECOND)
    press(cpu, dsky, "V37E00E")
    cpu.run(2 * CYCLES_PER_SECOND)
    assert dsky.state().prog == "00"
    assert cpu.erasable_flat(prog.symbol("MODREG").value) == 0
    assert cpu.alarm_log == []
