"""Rope image helpers: write/read the Virtual AGC ``.bin`` format.

The .bin format stores the 36 fixed banks as 2-byte big-endian words with the
15-bit value shifted left by one (bit 0 is the parity position).  Banks are
stored in the order 2, 3, 0, 1, 4, 5, ... 43 (fixed-fixed first), which is
the order the hardware addresses them.
"""

from __future__ import annotations

from pathlib import Path

NUM_BANKS = 0o44
BANK_SIZE = 0o2000


def bank_order() -> list[int]:
    return [b ^ 2 if b < 4 else b for b in range(NUM_BANKS)]


def write_bin(fixed: list[list[int]], path: str | Path):
    out = bytearray()
    for bank in bank_order():
        for word in fixed[bank]:
            v = (word & 0o77777) << 1
            out.append(v >> 8)
            out.append(v & 0xFF)
    Path(path).write_bytes(bytes(out))


def read_bin(path: str | Path) -> list[list[int]]:
    data = Path(path).read_bytes()
    fixed = [[0] * BANK_SIZE for _ in range(NUM_BANKS)]
    i = 0
    for bank in bank_order():
        for off in range(BANK_SIZE):
            v = (data[i] << 8) | data[i + 1]
            fixed[bank][off] = (v >> 1) & 0o77777
            i += 2
    return fixed
