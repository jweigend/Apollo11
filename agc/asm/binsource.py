"""Reader for Virtual AGC ``.binsource`` rope listings.

A binsource file is a hand-proofed transcription of the octal program listing
from the original AGC assembly printout.  It is organised as::

    BANK=2
    00004 34054 56006 12667 52011 00006 34056 52006
    ...

with comment lines starting with ``;``.  Banks are 1024 words long.  Unused
words are written as ``@`` (or ``00000``).
"""

from __future__ import annotations

import re
from pathlib import Path

from .assembler import BANK_SIZE, NUM_FIXED_BANKS


def read_binsource(path: str | Path) -> list[list[int | None]]:
    banks: list[list[int | None]] = [[None] * BANK_SIZE for _ in range(NUM_FIXED_BANKS)]
    bank = None
    offset = 0
    for raw in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith(";"):
            continue
        if line.startswith("BANK="):
            m = re.match(r"BANK=\s*([0-7]+)", line)
            if not m:
                raise ValueError(f"bad bank marker {raw!r}")
            bank = int(m.group(1), 8)
            offset = 0
            continue
        if bank is None:
            continue
        for tok in line.split():
            if tok.startswith(";"):
                break
            if offset >= BANK_SIZE:
                raise ValueError(f"bank {bank:o} overflows at {raw!r}")
            if tok == "@":
                banks[bank][offset] = None
            else:
                banks[bank][offset] = int(tok, 8)
            offset += 1
    return banks


def compare(fixed: list[list[int]], used: list[list[bool]], reference: list[list[int | None]]):
    """Return a list of (bank, offset, ours, theirs) mismatches."""
    diffs = []
    for bank in range(NUM_FIXED_BANKS):
        for off in range(BANK_SIZE):
            ref = reference[bank][off]
            ours = fixed[bank][off] if used[bank][off] else None
            if ref is None and ours is None:
                continue
            if ref is None:
                ref = 0
            if ours is None:
                ours = 0
            if ref != ours:
                diffs.append((bank, off, ours, ref))
    return diffs
