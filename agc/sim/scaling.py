"""Conversions between engineering values and AGC fixed-point words.

AGC numbers are one's-complement fractions.  A quantity "scaled at B(n)"
means the stored fraction is value / 2**n.  Single precision (SP) uses one
15-bit word (14 magnitude bits), double precision (DP) two words (28 bits),
triple precision (TP) three words (42 bits).  Negative numbers complement
every word of the number.
"""

from __future__ import annotations

import math

MASK14 = 0o37777
MASK15 = 0o77777


def _ones_complement(words: list[int], negative: bool) -> list[int]:
    if negative:
        return [(~w) & MASK15 for w in words]
    return [w & MASK15 for w in words]


def sp(value: float, scale: int) -> int:
    """Single-precision word for ``value`` scaled at B(scale)."""
    frac = value / 2.0 ** scale
    mag = int(round(abs(frac) * 2 ** 14))
    if mag > MASK14:
        raise OverflowError(f"SP overflow: {value} at B{scale}")
    return _ones_complement([mag], frac < 0)[0]


def dp(value: float, scale: int) -> list[int]:
    """Double-precision word pair (high, low) for ``value`` scaled at B(scale)."""
    frac = value / 2.0 ** scale
    mag = int(round(abs(frac) * 2 ** 28))
    if mag >= 2 ** 28:
        raise OverflowError(f"DP overflow: {value} at B{scale}")
    hi, lo = mag >> 14, mag & MASK14
    return _ones_complement([hi, lo], frac < 0)


def tp(value: float, scale: int) -> list[int]:
    """Triple-precision words for ``value`` scaled at B(scale)."""
    frac = value / 2.0 ** scale
    mag = int(round(abs(frac) * 2 ** 42))
    if mag >= 2 ** 42:
        raise OverflowError(f"TP overflow: {value} at B{scale}")
    w = [(mag >> 28) & MASK14, (mag >> 14) & MASK14, mag & MASK14]
    return _ones_complement(w, frac < 0)


def sp_value(word: int, scale: int) -> float:
    word &= MASK15
    if word & 0o40000:
        return -((~word) & MASK14) / 2 ** 14 * 2.0 ** scale
    return word / 2 ** 14 * 2.0 ** scale


def dp_value(hi: int, lo: int, scale: int) -> float:
    """Value of a DP pair.  Handles pairs whose words have different signs."""
    return (sp_value(hi, scale) + sp_value(lo, scale - 14))


def tp_value(w0: int, w1: int, w2: int, scale: int) -> float:
    return sp_value(w0, scale) + sp_value(w1, scale - 14) + sp_value(w2, scale - 28)


def angle_to_cdu(angle_rad: float) -> int:
    """Gimbal angle -> 15-bit two's-complement CDU counter (2**15 pulses per revolution)."""
    pulses = int(round(angle_rad / (2 * math.pi) * 32768.0))
    return pulses % 32768


def cdu_to_angle(word: int) -> float:
    word &= 0o77777
    if word & 0o40000:
        word -= 0o100000
    return word / 32768.0 * 2 * math.pi


def ft(meters: float) -> float:
    return meters / 0.3048


def m(feet: float) -> float:
    return feet * 0.3048
