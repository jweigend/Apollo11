"""Unit tests for the AGC CPU emulator (arithmetic helpers and instructions)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agc.cpu import (  # noqa: E402
    A, L, Q, Z, AGC, AGC_M0, AGC_P0, add_sp16, agc2cpu, cpu2agc, dabs,
    overflow_corrected, sign_extend, decent_to_sp, sp_to_decent, counter_pinc,
)


def make_cpu(words: dict[int, int]) -> AGC:
    """Build a CPU whose fixed-fixed bank 02 (addresses 4000-5777) holds ``words``."""
    fixed = [[0] * 0o2000 for _ in range(0o44)]
    for addr, w in words.items():
        bank = addr // 0o2000
        fixed[bank][addr & 0o1777] = w
    cpu = AGC(fixed, check_alarms=False)
    cpu.e[Z] = 0o4000
    return cpu


def run_instructions(cpu: AGC, n: int):
    for _ in range(n):
        while not cpu.step():
            pass


def test_sign_extend_and_overflow_correction():
    assert sign_extend(0o37777) == 0o037777
    assert sign_extend(0o40000) == 0o140000
    assert overflow_corrected(0o140000) == 0o40000
    assert overflow_corrected(0o037777) == 0o37777


def test_add_sp16_end_around_carry():
    # -1 + +1 = -0 in one's complement (end-around carry produces 177777)
    assert add_sp16(sign_extend(AGC_M0 - 1), 1) & 0o77777 == 0o77777
    assert agc2cpu(cpu2agc(-5)) == -5
    assert agc2cpu(cpu2agc(1234)) == 1234


def test_dabs():
    assert dabs(5) == 4
    assert dabs(0o77772) == 4          # -5 -> 4
    assert dabs(1) == AGC_P0
    assert dabs(AGC_M0) == AGC_P0


def test_decent_roundtrip():
    for msb, lsb in [(0o00001, 0o00000), (0o77776, 0o77777), (0o00000, 0o00005), (0o12345, 0o23456)]:
        v = sp_to_decent(msb, lsb)
        m2, l2 = decent_to_sp(v)
        assert sp_to_decent(m2, l2) == v


def test_counter_pinc_skips_minus_zero():
    assert counter_pinc(0o77777) == (1, False)
    assert counter_pinc(0o37777) == (AGC_P0, True)


def test_ca_ts_ad_sequence():
    # 4000: CA 4010 ; TS 0100 ; AD 4011 ; TS 0101 ; TC 4004 (loop)
    cpu = make_cpu({
        0o4000: 0o30000 | 0o4010,
        0o4001: 0o54000 | 0o100,
        0o4002: 0o60000 | 0o4011,
        0o4003: 0o54000 | 0o101,
        0o4004: 0o4004,              # TC self
        0o4010: 0o00005,
        0o4011: 0o00007,
    })
    run_instructions(cpu, 4)
    assert cpu.e[0o100] == 5
    assert cpu.e[0o101] == 12
    assert cpu.e[A] & 0o177777 == 12


def test_ccs_branches():
    # CCS on +3 at 0100: falls through to 4001 and A = 2
    cpu = make_cpu({0o4000: 0o10000 | 0o100, 0o4001: 0o4001, 0o4002: 0o4002, 0o4003: 0o4003, 0o4004: 0o4004})
    cpu.e[0o100] = 3
    run_instructions(cpu, 1)
    assert cpu.z == 0o4001 and cpu.e[A] == 2
    # CCS on -0 skips three words
    cpu = make_cpu({0o4000: 0o10000 | 0o100, 0o4004: 0o4004})
    cpu.e[0o100] = AGC_M0
    run_instructions(cpu, 1)
    assert cpu.z == 0o4004


def test_extend_dca_and_mp():
    # EXTEND ; DCA 4010 (loads 4010,4011 into A,L) ; EXTEND ; MP 4012
    cpu = make_cpu({
        0o4000: 6, 0o4001: 0o30000 | 0o4011,      # DCA encodes K+1
        0o4002: 6, 0o4003: 0o70000 | 0o4012,
        0o4004: 0o4004,
        0o4010: 0o00003, 0o4011: 0o00004, 0o4012: 0o20000,   # 3 * 0.5 (B-1)
    })
    run_instructions(cpu, 4)
    # 3 * 20000 (=2^13 as fraction 0.5) = DP 00001 20000  (1.5 in units of 2^-14... i.e. 3/2)
    assert (cpu.e[A] & 0o77777, cpu.e[L] & 0o77777) == (0o00001, 0o20000)


def test_dv_simple():
    # A,L = +0, 6 ; EXTEND ; DV 0100 (=3) -> quotient 2, remainder 0.
    # (DV only addresses erasable memory; a fixed address would decode as BZF.)
    cpu = make_cpu({0o4000: 6, 0o4001: 0o10000 | 0o100, 0o4002: 0o4002})
    cpu.e[0o100] = 3
    cpu.e[A] = 0
    cpu.e[L] = 6
    run_instructions(cpu, 2)
    assert cpu.e[A] & 0o77777 == 2
    assert cpu.e[L] & 0o77777 == 0
    # 7 / 2 -> quotient 3, remainder 1
    cpu = make_cpu({0o4000: 6, 0o4001: 0o10000 | 0o100, 0o4002: 0o4002})
    cpu.e[0o100] = 2
    cpu.e[L] = 7
    run_instructions(cpu, 2)
    assert (cpu.e[A] & 0o77777, cpu.e[L] & 0o77777) == (3, 1)


def test_interrupt_vector_and_resume():
    # Program: INHINT? no - keep interrupts enabled; main loop at 4000 (TCF 4000).
    # T3RUPT vector 4014: RESUME (INDEX 17 -> 50017).
    cpu = make_cpu({0o4000: 0o14000, 0o4014: 0o50017})
    cpu.allow_interrupt = True
    cpu.interrupt_requests[8] = 0
    cpu.interrupt_requests[3] = 1
    run_instructions(cpu, 1)      # interrupt taken
    assert cpu.in_isr and cpu.z == 0o4014
    run_instructions(cpu, 1)      # RESUME
    assert not cpu.in_isr
    run_instructions(cpu, 1)      # back in the loop
    assert cpu.z == 0o4000
