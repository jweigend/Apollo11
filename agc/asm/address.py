"""AGC address model used by the assembler.

The Block II Apollo Guidance Computer has a peculiar, banked memory layout.
Every symbol the assembler resolves is an ``Address`` that remembers *where*
in that layout it lives:

* erasable memory (RAM): 8 banks of 256 words.  Banks 0..2 are also reachable
  without bank switching ("unswitched", addresses 0000-1377), any bank is
  reachable through the EB register at 1400-1777.
* fixed memory (rope ROM): 36 banks of 1024 words.  Banks 02 and 03 are
  "fixed-fixed" and are always visible at 4000-7777; the others are selected
  with the FB register (and the superbank bit of channel 7) at 2000-3777.

The assembler works with *pseudo addresses*, a flat numbering used by the
original YUL assembler and by yaYUL::

    0000-1377   unswitched erasable
    1400-3777   banked erasable  (E0..E7 at 0400 each, so E3 = 1400..1777)
    4000-7777   fixed-fixed (banks 02, 03)
    10000-      banked fixed: bank n at 10000 + n*2000 (banks 00,01,04..37)
    110000-     superbank fixed banks 40..43

This module is a straight port of the Address_t handling in yaYUL
(IncPc.c / PseudoToSegmented.c), because matching the original rope
bit-for-bit is the acceptance test for the converter.
"""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass
class Address:
    invalid: bool = False
    constant: bool = False
    address: bool = False
    sreg: int = 0
    erasable: bool = False
    fixed: bool = False
    unbanked: bool = False
    banked: bool = False
    eb: int = 0
    fb: int = 0
    super: bool = False
    overflow: bool = False
    value: int = 0

    # -- constructors -----------------------------------------------------
    @classmethod
    def invalid_address(cls) -> "Address":
        return cls(invalid=True)

    @classmethod
    def const(cls, value: int) -> "Address":
        return cls(constant=True, value=value)

    @classmethod
    def reg(cls, n: int) -> "Address":
        return cls(address=True, sreg=n, erasable=True, unbanked=True, value=n)

    def copy(self) -> "Address":
        return replace(self)

    # -- comparison used for "symbol reassigned" detection ------------------
    def same(self, other: "Address") -> bool:
        return self == other

    # -- pretty printing in yaYUL listing style ----------------------------
    def listing(self) -> str:
        if self.invalid:
            return "???????"
        if self.constant:
            return f"{self.value & 0o7777777:07o}"
        if self.unbanked:
            return f"   {self.sreg:04o}"
        if self.banked:
            if self.erasable:
                return f"E{self.eb:1o},{self.sreg:04o}"
            if self.fixed:
                return f"{self.fb + 0o10 * self.super:02o},{self.sreg:04o}"
        return "int-err"

    def bank_number(self) -> int | None:
        """Fixed-memory bank number 0..0o43 (None if not fixed memory)."""
        if self.invalid or not self.address or not self.fixed:
            return None
        if self.banked:
            return self.fb + (0o10 if self.super else 0)
        return self.sreg // 0o2000  # 2 or 3

    def fixed_offset(self) -> int | None:
        """Offset 0..1777 inside the fixed bank."""
        if self.bank_number() is None:
            return None
        return self.sreg & 0o1777

    def __str__(self) -> str:
        return self.listing()


def pseudo_to_struct(value: int) -> Address:
    """Convert a flat pseudo-address to a structured Address (PseudoToStruct)."""
    a = Address()
    if value < 0 or value > 0o117777:
        a.invalid = True
        a.value = value
        return a
    if value <= 0o1377:
        a.address = True
        a.erasable = True
        a.unbanked = True
        a.sreg = value
    elif value <= 0o3777:
        a.address = True
        a.erasable = True
        a.banked = True
        a.sreg = 0o1400 + (value & 0o377)
        a.eb = value // 0o400
    elif value <= 0o7777:
        a.address = True
        a.fixed = True
        a.unbanked = True
        a.sreg = value
    else:
        a.address = True
        a.fixed = True
        a.banked = True
        a.sreg = 0o2000 + (value & 0o1777)
        if 0o4000 <= value <= 0o5777:
            a.fb = 2
        elif 0o6000 <= value <= 0o7777:
            a.fb = 3
        elif value < 0o110000:
            a.fb = (value - 0o10000) // 0o2000
        else:
            a.super = True
            a.fb = (value - 0o30000) // 0o2000
    a.value = value
    return a


def inc_pc(old: Address, increment: int) -> Address:
    """Advance an address by ``increment`` words (IncPc.c)."""
    if increment >= 0:
        bank_increment = 7 & (increment >> 12)
        increment &= 0o7777
    else:
        increment = -increment
        bank_increment = -(7 & (increment >> 12))
        increment = -(0o7777 & increment)

    new = old.copy()
    if new.invalid:
        return new
    if new.constant:
        if new.value < 0:
            return new
        if new.value < 0o1400:
            new.constant = False
            new.address = True
            new.erasable = True
            new.fixed = False
            new.banked = False
            new.unbanked = True
            new.eb = 0
            new.fb = 0
            new.super = False
            new.sreg = new.value
        else:
            return new
    if new.overflow:
        return new

    i = new.sreg + increment
    new.sreg = i
    if new.erasable and new.banked:
        new.eb += bank_increment
    elif new.fixed and new.banked:
        new.fb += bank_increment
    if new.fixed and bank_increment != 0 and new.fb == 0:
        new.constant = False
        new.address = True
        new.erasable = True
        new.fixed = False
        new.banked = False
        new.unbanked = True
        new.eb = 0
        new.fb = 0
        new.super = False

    if new.erasable:
        if new.unbanked:
            lo, hi = 0, 0o1377
        elif new.banked:
            lo, hi = 0o1400, 0o1777
            new.eb += bank_increment
        else:
            new.invalid = True
            return new
    elif new.fixed:
        if new.banked:
            lo, hi = 0o2000, 0o3777
            new.fb += bank_increment
        elif new.unbanked:
            lo, hi = 0o4000, 0o7777
        else:
            new.invalid = True
            return new
    else:
        new.invalid = True
        return new

    if i < lo:
        new.overflow = True
        new.sreg = lo
    elif i > hi:
        new.overflow = True
        new.sreg = hi

    if new.unbanked:
        new.value = new.sreg
    elif new.erasable:
        new.value = (new.sreg - 0o1400) + 0o400 * new.eb
    elif new.fixed:
        new.value = 0o10000 + (new.sreg - 0o2000) + 0o2000 * new.fb
        if new.super and new.fb >= 0o30:
            new.value += 0o10 * 0o2000
    else:
        new.invalid = True
    return new


# ---------------------------------------------------------------------------
# Numeric literals
# ---------------------------------------------------------------------------

def get_oct_or_dec(s: str | None) -> int | None:
    """Parse an AGC numeric operand.

    Plain digits 0-7 are octal; a trailing ``D`` or any digit 8/9 makes the
    number decimal.  An optional leading sign is allowed.  Returns None when
    the string is not a number (GetOctOrDec.c).
    """
    if not s:
        return None
    ss = s[1:] if s[0] in "+-" else s
    if ss == "" or ss == "D":
        return None
    if all(c in "01234567" for c in ss):
        v = int(ss, 8)
        return -v if s[0] == "-" else v
    body = ss
    decimal = False
    if body.endswith("D"):
        body = body[:-1]
        decimal = True
        if body == "":
            return None
    if body.isdigit() and body.isascii():
        if decimal or any(c in "89" for c in body):
            v = int(body, 10)
            return -v if s[0] == "-" else v
    return None


def agc_add(a: int, b: int) -> int:
    """15-bit wraparound add used for constant folding (AddAgc)."""
    return 0o77777 & (a + b)


def calculate_parity(value: int) -> int:
    """Odd parity bit of a 15-bit word (1 when the word has an even number of ones)."""
    p = 1
    n = value & 0xFFFF
    while n:
        n &= n - 1
        p ^= 1
    return p
