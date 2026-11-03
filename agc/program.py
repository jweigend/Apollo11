"""Runtime representation of a converted AGC program.

The converter (``agc.asm.pygen``) turns every ``.agc`` source file into one
Python module that registers its words and symbols on a :class:`Module`.
A :class:`Program` collects all modules of one flight program (Luminary 099
or Comanche 055), builds the 36-bank rope image for the emulator and offers
symbol / address lookups for the test UI.

Addresses
---------
Fixed-memory words are identified by ``(bank, offset)`` with bank 0..0o43 and
offset 0..0o1777.  In the generated source they are written in the AGC
listing style ``"06,3000"`` (bank 06, S-register 3000) or ``"4000"`` for
fixed-fixed memory (banks 02 and 03, addresses 4000-7777).

Erasable symbols carry their flat erasable address 0..0o3777
(bank = value >> 8, offset = value & 0o377).
"""

from __future__ import annotations

import importlib
import pkgutil
from dataclasses import dataclass, field

NUM_BANKS = 0o44
BANK_SIZE = 0o2000


def parse_fixed_address(text: str) -> tuple[int, int]:
    """``"06,3000"`` -> (6, 0o1000); ``"4000"`` -> (2, 0); ``"6123"`` -> (3, 0o123)."""
    if "," in text:
        bank_s, sreg_s = text.split(",")
        bank = int(bank_s, 8)
        sreg = int(sreg_s, 8)
        return bank, sreg - 0o2000
    sreg = int(text, 8)
    return sreg // 0o2000, sreg & 0o1777


def pseudo_address(bank: int, offset: int) -> int:
    """Flat yaYUL-style pseudo address of a fixed-memory word."""
    if bank in (2, 3):
        return bank * 0o2000 + offset
    if bank >= 0o40:
        return 0o110000 + (bank - 0o40) * 0o2000 + offset
    return 0o10000 + bank * 0o2000 + offset


def fixed_location(pseudo: int) -> tuple[int, int] | None:
    """Inverse of :func:`pseudo_address`; None for erasable/constant values."""
    if 0o4000 <= pseudo <= 0o7777:
        return pseudo // 0o2000, pseudo & 0o1777
    if 0o10000 <= pseudo < 0o110000:
        return (pseudo - 0o10000) // 0o2000, pseudo & 0o1777
    if 0o110000 <= pseudo <= 0o117777:
        return 0o40 + (pseudo - 0o110000) // 0o2000, pseudo & 0o1777
    return None


def format_fixed_address(bank: int, offset: int) -> str:
    if bank in (2, 3):
        return f"{bank * 0o2000 + offset:04o}"
    return f"{bank:02o},{0o2000 + offset:04o}"


def format_erasable_address(value: int) -> str:
    if value < 0o1400:
        return f"{value:04o}"
    return f"E{value >> 8:o},{0o1400 + (value & 0o377):04o}"


@dataclass
class Word:
    bank: int
    offset: int
    value: int
    label: str
    operator: str
    operand: str
    comment: str
    kind: str          # "basic", "interp", "operand", "data", "operand?" ...
    module: "Module"
    line: int          # source line number in the .agc file

    @property
    def address(self) -> str:
        return format_fixed_address(self.bank, self.offset)

    @property
    def is_code(self) -> bool:
        return self.kind == "basic"


@dataclass
class SymbolDef:
    name: str
    kind: str          # "label", "erase", "equals", "constant"
    value: int         # pseudo address (fixed), erasable address, or constant
    module: "Module"
    line: int

    def fixed_location(self) -> tuple[int, int] | None:
        """(bank, offset) when the symbol points into fixed memory."""
        if self.kind not in ("label", "equals"):
            return None
        return fixed_location(self.value)

    def erasable_address(self) -> int | None:
        if self.kind in ("erase", "equals", "label") and 0 <= self.value <= 0o3777:
            return self.value
        return None


class Module:
    """One converted source file."""

    def __init__(self, name: str, source: str, program: str, pages: str = ""):
        self.name = name
        self.source = source
        self.program = program
        self.pages = pages
        self.words: list[Word] = []
        self.symbols: dict[str, SymbolDef] = {}
        self._line = 0

    # The generated modules call these.  Short names keep the files compact.
    def W(self, address: str, value: int, label: str = "", operator: str = "",
          operand: str = "", comment: str = "", kind: str = "basic", line: int = 0):
        bank, offset = parse_fixed_address(address)
        self.words.append(Word(bank, offset, value, label, operator, operand, comment, kind, self, line))
        if label:
            self.symbols[label] = SymbolDef(label, "label", pseudo_address(bank, offset), self, line)

    def S(self, name: str, kind: str, value: int, line: int = 0):
        self.symbols[name] = SymbolDef(name, kind, value, self, line)

    # -- queries ----------------------------------------------------------
    def labels(self) -> list[Word]:
        return [w for w in self.words if w.label]

    def routines(self) -> list[Word]:
        """Labelled executable words: natural entry points for testing."""
        return [w for w in self.words if w.label and w.kind == "basic"]

    def __repr__(self):
        return f"<Module {self.name}: {len(self.words)} words, {len(self.symbols)} symbols>"


class Program:
    """A whole flight program: rope image plus symbol information."""

    def __init__(self, package: str):
        self.package = package
        pkg = importlib.import_module(package)
        self.name: str = pkg.NAME
        self.title: str = pkg.TITLE
        self.module_names: list[str] = list(pkg.MODULES)
        self.modules: list[Module] = []
        for modname in self.module_names:
            mod = importlib.import_module(f"{package}.{modname}")
            self.modules.append(mod.MODULE)
        self.fixed: list[list[int]] = [[0] * BANK_SIZE for _ in range(NUM_BANKS)]
        self.words_by_address: dict[tuple[int, int], Word] = {}
        self.symbols: dict[str, SymbolDef] = {}
        for m in self.modules:
            for w in m.words:
                self.fixed[w.bank][w.offset] = w.value
                self.words_by_address[(w.bank, w.offset)] = w
            self.symbols.update(m.symbols)
        self.labels_by_address: dict[tuple[int, int], str] = {}
        for sym in self.symbols.values():
            loc = sym.fixed_location()
            if loc is not None and sym.kind == "label" and loc not in self.labels_by_address:
                self.labels_by_address[loc] = sym.name
        self.erasable_names: dict[int, str] = {}
        for sym in self.symbols.values():
            ea = sym.erasable_address()
            if ea is not None and sym.kind in ("erase", "equals"):
                self.erasable_names.setdefault(ea, sym.name)

    # -- lookups ----------------------------------------------------------
    def word_at(self, bank: int, offset: int) -> Word | None:
        return self.words_by_address.get((bank, offset))

    def symbol(self, name: str) -> SymbolDef | None:
        return self.symbols.get(name)

    def label_for(self, bank: int, offset: int) -> str | None:
        return self.labels_by_address.get((bank, offset))

    def nearest_label(self, bank: int, offset: int) -> str:
        """``LABEL +n`` form for an arbitrary fixed address."""
        for back in range(0, offset + 1):
            lab = self.labels_by_address.get((bank, offset - back))
            if lab:
                return lab if back == 0 else f"{lab} +{back}"
        return format_fixed_address(bank, offset)

    def module(self, name: str) -> Module | None:
        for m in self.modules:
            if m.name == name:
                return m
        return None

    def __repr__(self):
        return f"<Program {self.name}: {len(self.modules)} modules, {len(self.symbols)} symbols>"


def available_programs() -> list[str]:
    import agc.programs as p
    return [m.name for m in pkgutil.iter_modules(p.__path__) if m.ispkg]


def load_program(name: str) -> Program:
    return Program(f"agc.programs.{name.lower()}")
