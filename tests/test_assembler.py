"""Tests for the agc2py assembler: numeric parsing, addresses and (if the
reference listings are available) bit-exactness of the whole rope."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from agc.asm.address import get_oct_or_dec, inc_pc, pseudo_to_struct  # noqa: E402
from agc.asm.assembler import Assembler, expand_tabs, is_false_label  # noqa: E402
from agc.asm.binsource import compare, read_binsource  # noqa: E402

SRC = ROOT / "external" / "Apollo-11"
REF = ROOT / "external" / "virtualagc"


def test_get_oct_or_dec():
    assert get_oct_or_dec("17") == 0o17
    assert get_oct_or_dec("17D") == 17
    assert get_oct_or_dec("19") == 19          # 8/9 force decimal
    assert get_oct_or_dec("-5") == -5
    assert get_oct_or_dec("+0") == 0
    assert get_oct_or_dec("FOO") is None
    assert get_oct_or_dec("") is None
    assert get_oct_or_dec("D") is None


def test_pseudo_to_struct_regions():
    a = pseudo_to_struct(0o100)
    assert a.erasable and a.unbanked and a.sreg == 0o100
    b = pseudo_to_struct(0o1500)
    assert b.erasable and b.banked and b.eb == 3 and b.sreg == 0o1500
    c = pseudo_to_struct(0o5000)
    assert c.fixed and c.unbanked and c.sreg == 0o5000 and c.bank_number() == 2
    d = pseudo_to_struct(0o10000 + 0o21 * 0o2000 + 0o123)
    assert d.fixed and d.banked and d.fb == 0o21 and d.sreg == 0o2123
    e = pseudo_to_struct(0o110000 + 0o2000 + 7)
    assert e.super and e.bank_number() == 0o41 and e.sreg == 0o2007


def test_inc_pc_bank_overflow():
    a = pseudo_to_struct(0o10000 + 4 * 0o2000 + 0o1777)
    b = inc_pc(a, 1)
    assert b.overflow


def test_false_label_and_tabs():
    assert is_false_label("+2") and is_false_label("-16") and is_false_label("+3D")
    assert not is_false_label("+A") and not is_false_label("TCF")
    assert expand_tabs("A\tB") == "A       B"
    assert expand_tabs("\t\tINHINT") == "                INHINT"


@pytest.mark.parametrize("program", ["Luminary099", "Comanche055"])
def test_rope_matches_reference_listing(program):
    main = SRC / program / "MAIN.agc"
    ref = REF / program / f"{program}.binsource"
    if not main.exists() or not ref.exists():
        pytest.skip("original sources / reference listing not cloned")
    result = Assembler(main).assemble()
    assert result.fatals == 0
    diffs = compare(result.fixed, result.used, read_binsource(ref))
    assert diffs == [], f"{len(diffs)} words differ, first: {diffs[:5]}"
