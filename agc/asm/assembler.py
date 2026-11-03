"""Two-plus-pass assembler for Block II AGC source (Luminary / Colossus).

This is a Python port of the assembly logic of yaYUL (Virtual AGC project,
Ron Burkey, GPL).  The goal of the port is not elegance but *bit-exactness*:
the words it produces are checked against the octal rope listings that were
recovered from the original Apollo 11 program printouts.

Usage::

    asm = Assembler(Path("external/Apollo-11/Luminary099/MAIN.agc"))
    result = asm.assemble()
    result.fixed[bank][offset]      # 36 x 1024 words of rope
    result.lines                    # listing records for every source line
    result.symbols                  # symbol table
"""

from __future__ import annotations

import difflib
import math
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

from .address import (
    Address,
    agc_add,
    calculate_parity,
    get_oct_or_dec,
    inc_pc,
    pseudo_to_struct,
)
from .fixups import FIXUPS
from .tables import (
    ENUMBER,
    ERASABLE,
    EXTENDED,
    FIXED,
    INTERP,
    KPLUS1,
    OPS,
    PC0, PC1, PC2, PC3, PC4, PC5, PC6, PC7,
    QC0, QC1, QC2, QC3, QCNOT0,
    OpType,
)

NUM_FIXED_BANKS = 0o44
BANK_SIZE = 0o2000
MAX_PASSES = 10

SYMBOL_REGISTER = 1
SYMBOL_LABEL = 2
SYMBOL_VARIABLE = 4
SYMBOL_CONSTANT = 8


class AssemblyError(Exception):
    pass


@dataclass
class Symbol:
    name: str
    value: Address = field(default_factory=Address.invalid_address)
    type: int = 0
    file: str = ""
    line: int = 0


@dataclass
class EBank:
    oneshot: bool = False
    current: Address = field(default_factory=Address)
    last: Address = field(default_factory=Address)

    def copy(self):
        return EBank(self.oneshot, self.current.copy(), self.last.copy())


@dataclass
class SBank:
    oneshot: bool = False
    current: int = 0
    last: int = 0

    def copy(self):
        return SBank(self.oneshot, self.current, self.last)


@dataclass
class ParseIn:
    pc: Address
    label: str = ""
    false_label: str = ""
    operator: str = ""
    operand: str = ""
    mod1: str = ""
    mod2: str = ""
    extra: str = ""
    comment: str = ""
    alias: str = ""
    extend: int = 0
    index_valid: bool = False
    ebank: EBank = field(default_factory=EBank)
    sbank: SBank = field(default_factory=SBank)
    comment_column: int = 0


@dataclass
class ParseOut:
    pc: Address
    words: list = field(default_factory=lambda: [0, 0])
    num_words: int = 0
    error: str = ""
    warning: bool = False
    fatal: bool = False
    label_value: Address = field(default_factory=Address.invalid_address)
    label_value_valid: bool = False
    extend: int = 0
    index_valid: bool = False
    ebank: EBank = field(default_factory=EBank)
    sbank: SBank = field(default_factory=SBank)
    equals: bool = False


@dataclass
class LineRecord:
    """One source line as seen in the final pass (the listing)."""

    file: str                 # file name (basename)
    line: int                 # 1-based line number in that file
    text: str                 # raw source text (tabs expanded)
    pc: Address | None        # address before the line (None if no code/label)
    words: list[int]          # assembled words (0..2)
    label: str
    false_label: str
    operator: str
    operand: str
    mod1: str
    mod2: str
    comment: str
    comment_column: int
    error: str = ""
    fatal: bool = False
    warning: bool = False
    kind: str = ""            # "basic", "interp", "operand", "data", "pseudo", ""
    label_value: Address | None = None   # value shown for EQUALS etc.


@dataclass
class AssemblyResult:
    fixed: list[list[int]]
    used: list[list[bool]]
    bank_counts: list[int]
    symbols: dict[str, Symbol]
    lines: list[LineRecord]
    files: list[str]
    fatals: int
    warnings: int
    bugger_words: dict[int, tuple[int, int]]   # bank -> (offset, word)


def is_false_label(s: str) -> bool:
    if not s or s[0] not in "+-":
        return False
    body = s[1:]
    if body.endswith("D"):
        body = body[:-1]
    return body.isdigit() and body != ""


def expand_tabs(s: str) -> str:
    out = []
    pos = 0
    for ch in s:
        if ch == "\t":
            stop = (pos + 8) & ~7
            out.append(" " * (stop - pos))
            pos = stop
        else:
            out.append(ch)
            pos += 1
    return "".join(out)


def _atoi(s: str) -> int:
    """C atoi: parse an optionally signed integer prefix, 0 if none."""
    m = re.match(r"\s*([+-]?\d+)", s)
    return int(m.group(1)) if m else 0


def scale_factor(s: str) -> float:
    if not s:
        return 1.0
    if s[0] == "E":
        return 10.0 ** _atoi(s[1:])
    if s[0] == "B":
        return 2.0 ** _atoi(s[1:])
    return 1.0


def _fuzzed_is_int(x: float) -> bool:
    f = abs(math.fmod(x, 1.0))
    return f < 1e-10 or f > 1.0 - 1e-10


class Assembler:
    def __init__(self, main_file: str | os.PathLike, verbose: bool = False,
                 fixups: dict[str, list[tuple[int, str, str]]] | None = None):
        self.main_file = Path(main_file)
        self.source_dir = self.main_file.parent
        self.verbose = verbose
        if fixups is None:
            fixups = FIXUPS.get(self.source_dir.name, {})
        self.fixups = fixups
        self.applied_fixups: list[tuple[str, int, str, str]] = []
        self.skipped_fixups: list[tuple[str, int, str]] = []
        self.symbols: dict[str, Symbol] = {}
        self.duplicate_symbols: list[str] = []
        self.fixed = [[0] * BANK_SIZE for _ in range(NUM_FIXED_BANKS)]
        self.used = [[False] * BANK_SIZE for _ in range(NUM_FIXED_BANKS)]
        self.used_in_bank = [0] * NUM_FIXED_BANKS
        self.prior_used_in_bank = [0] * NUM_FIXED_BANKS
        self.lines: list[LineRecord] = []
        self.files: list[str] = []
        self.fatals = 0
        self.warnings = 0
        self.num_symbols_reassigned = 0
        # interpretive-operand state (globals in yaYUL)
        self.num_interp_operands = 0
        self.raw_num_interp_operands = 0
        self.nnnn_fields = [0, 0, 0, 0]
        self.switch_increment = [0, 0, 0, 0]
        self.opcode_offset = 0
        self.arg_type = 0
        self.stadr_invert = 0
        self.current_file = ""
        self.current_line = 0
        self.write_output = False
        self.include_fixups: dict[str, str] = {}

    # ------------------------------------------------------------------
    # Driver
    # ------------------------------------------------------------------
    def assemble(self) -> AssemblyResult:
        self.symbol_pass()
        for name, n in (("$3", 3), ("$4", 4), ("$5", 5), ("$6", 6), ("$7", 7), ("$17", 0o17)):
            self.symbols[name] = Symbol(name, Address.reg(n), SYMBOL_REGISTER)
        last_unresolved = self.unresolved_symbols()
        for i in range(1, MAX_PASSES + 1):
            if self.verbose:
                print(f"Pass #{i}")
            snapshot = {name: sym.value.copy() for name, sym in self.symbols.items()}
            self.run_pass(write_output=False)
            k = self.unresolved_symbols()
            changed = sum(1 for name, sym in self.symbols.items() if snapshot[name] != sym.value)
            if (k == 0 or k >= last_unresolved) and changed == 0:
                if self.verbose:
                    print(f"Pass #{i + 1} (final)")
                self.run_pass(write_output=True)
                break
            last_unresolved = k
        else:
            raise AssemblyError("symbols did not converge")
        bugger = self.add_bugger_words()
        return AssemblyResult(
            fixed=self.fixed,
            used=self.used,
            bank_counts=list(self.used_in_bank),
            symbols=self.symbols,
            lines=self.lines,
            files=self.files,
            fatals=self.fatals,
            warnings=self.warnings,
            bugger_words=bugger,
        )

    def unresolved_symbols(self) -> int:
        return sum(1 for s in self.symbols.values() if s.value.invalid)

    # ------------------------------------------------------------------
    # Source reading (handles $include lines)
    # ------------------------------------------------------------------
    def read_source_file(self, path: Path) -> list[str]:
        """Read one source file, applying the documented transcription fixups."""
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for lineno, needle, replacement in self.fixups.get(path.name, []):
            if 1 <= lineno <= len(lines) and needle in lines[lineno - 1]:
                lines[lineno - 1] = lines[lineno - 1].replace(needle, replacement, 1)
                self.applied_fixups.append((path.name, lineno, needle, replacement))
            else:
                self.skipped_fixups.append((path.name, lineno, needle))
        return lines

    def iter_source(self):
        """Yield (file, lineno, raw_line) for the whole include tree."""
        stack: list[tuple[str, list[str], int]] = []
        fname = self.main_file.name
        lines = self.read_source_file(self.main_file)
        idx = 0
        while True:
            if idx >= len(lines):
                if not stack:
                    return
                fname, lines, idx = stack.pop()
                continue
            raw = lines[idx]
            idx += 1
            if raw.startswith("$"):
                inc = raw[1:].split()[0]
                stack.append((fname, lines, idx))
                fname = inc
                path = self.resolve_include(inc)
                lines = self.read_source_file(path)
                idx = 0
                yield ("$", inc, raw)
                continue
            yield (fname, idx, raw)

    def resolve_include(self, inc: str) -> Path:
        """Find an included file; tolerate small spelling differences.

        The GitHub transcription (chrislgarry/Apollo-11) renamed a few files
        without updating MAIN.agc, so fall back to a fuzzy match.
        """
        path = self.source_dir / inc
        if path.exists():
            return path
        key = re.sub(r"[^A-Z0-9]", "", inc.upper().removesuffix(".AGC"))
        candidates = []
        for f in self.source_dir.glob("*.agc"):
            fkey = re.sub(r"[^A-Z0-9]", "", f.name.upper().removesuffix(".AGC"))
            if fkey == key or key in fkey or fkey in key:
                candidates.append(f)
        if not candidates:
            # last resort: closest name by edit similarity (handles typos such as CNTROL)
            scored = sorted(
                self.source_dir.glob("*.agc"),
                key=lambda f: -difflib.SequenceMatcher(None, key, re.sub(r"[^A-Z0-9]", "", f.name.upper())).ratio(),
            )
            if scored and difflib.SequenceMatcher(None, key, re.sub(r"[^A-Z0-9]", "", scored[0].name.upper())).ratio() > 0.9:
                candidates = [scored[0]]
        if len(candidates) == 1:
            self.include_fixups[inc] = candidates[0].name
            return candidates[0]
        raise AssemblyError(f"include file {inc} does not exist (candidates: {[c.name for c in candidates]})")

    def symbol_pass(self):
        """Collect every label so later passes know which names are symbols."""
        for fname, lineno, raw in self.iter_source():
            if fname == "$":
                continue
            s = expand_tabs(raw)
            s = s.split("#", 1)[0]
            fields = s.split()
            if not fields:
                continue
            label = operator = ""
            i = 0
            if s and not s[0].isspace() and not (is_false_label(fields[0]) and len(fields) > 1):
                label = fields[i]
                i += 1
            elif fields[0][0] in "+-":
                i += 1
            if i < len(fields):
                operator = fields[i]
            if label and operator not in ("MEMORY", "CHECK="):
                if label in self.symbols:
                    self.duplicate_symbols.append(label)
                else:
                    self.symbols[label] = Symbol(label)

    # ------------------------------------------------------------------
    # Symbol helpers
    # ------------------------------------------------------------------
    def get_symbol(self, name: str) -> Symbol | None:
        if len(name) > 10:
            return None
        return self.symbols.get(name)

    def edit_symbol(self, name: str, value: Address, stype: int):
        sym = self.symbols.get(name)
        if sym is None:
            # Should not happen (collected in symbol pass) but be forgiving.
            sym = Symbol(name)
            self.symbols[name] = sym
        if not sym.value.same(value):
            self.num_symbols_reassigned += 1
        sym.value = value.copy()
        sym.type = stype
        sym.file = self.current_file
        sym.line = self.current_line

    def fetch_symbol_plus_offset(self, pc: Address, operand: str, mod1: str) -> Address | None:
        """Resolve ``operand`` (symbol or number) plus optional numeric ``mod1``.

        Returns None when the symbol is unknown.
        """
        if operand == "":
            return pc.copy()
        off = get_oct_or_dec(operand)
        if off is not None:
            return inc_pc(pc, off)
        sym = self.get_symbol(operand)
        if sym is None:
            return None
        value = sym.value.copy()
        off = get_oct_or_dec(mod1)
        if off is not None:
            value = pseudo_to_struct(sym.value.value + off)
        return value

    # ------------------------------------------------------------------
    # Bank bookkeeping
    # ------------------------------------------------------------------
    def update_bank_counts(self, pc: Address):
        if pc.invalid or not pc.address or not pc.fixed or pc.overflow:
            return
        if pc.banked:
            count = pc.sreg - 0o2000
            bank = pc.fb + 0o10 * pc.super
        elif pc.unbanked:
            if 0o4000 <= pc.sreg < 0o6000:
                count = pc.sreg - 0o4000
                bank = 2
            elif 0o6000 <= pc.sreg < 0o10000:
                count = pc.sreg - 0o6000
                bank = 3
            else:
                return
        else:
            return
        if count > self.used_in_bank[bank]:
            self.used_in_bank[bank] = count

    # ------------------------------------------------------------------
    # The pass
    # ------------------------------------------------------------------
    def run_pass(self, write_output: bool):
        self.write_output = write_output
        self.applied_fixups = []
        self.skipped_fixups = []
        self.prior_used_in_bank = list(self.used_in_bank)
        self.used_in_bank = [0] * NUM_FIXED_BANKS
        self.num_symbols_reassigned = 0
        self.num_interp_operands = 0
        self.stadr_invert = 0
        self.fatals = 0
        self.warnings = 0
        if write_output:
            self.lines = []
            self.files = []
            self.fixed = [[0] * BANK_SIZE for _ in range(NUM_FIXED_BANKS)]
            self.used = [[False] * BANK_SIZE for _ in range(NUM_FIXED_BANKS)]

        out = ParseOut(pc=Address.invalid_address())
        out.ebank = EBank(False, Address.const(1), Address.const(1))
        out.sbank = SBank()

        for fname, lineno, raw in self.iter_source():
            if fname == "$":
                if write_output:
                    self.files.append(lineno)
                continue
            self.current_file = fname
            self.current_line = lineno
            self.opcode_offset = 0
            pinch_hitting = False
            self.arg_type = 0

            inp = ParseIn(pc=out.pc.copy())
            inp.ebank = out.ebank.copy()
            inp.sbank = out.sbank.copy()
            inp.index_valid = out.index_valid
            inp.extend = out.extend
            out = ParseOut(pc=Address.invalid_address())
            out.ebank = inp.ebank.copy()
            out.sbank = inp.sbank.copy()

            s = expand_tabs(raw.rstrip("\n"))
            text = s
            # Split off the comment.
            hash_pos = s.find("#")
            comment = ""
            if hash_pos >= 0:
                inp.comment_column = hash_pos
                comment = s[hash_pos + 1:]
                s = s[:hash_pos]
            inp.comment = comment

            fields = s.split()[:6]
            nfields = len(fields)
            no_operator = True
            imatch = None
            match = None
            i = 0
            if nfields >= 1:
                which_column = s.find(fields[0])
                goto_not_offset = False
                if which_column == 0 and not (is_false_label(fields[0]) and nfields > 1):
                    inp.label = fields[i]
                    i += 1
                elif is_false_label(fields[0]) and which_column < 16:
                    # yaYUL only accepts a "+N"/"-N" pseudo-label before column 8.
                    # The GitHub transcription sometimes puts a tab in front of it
                    # (column 8), which would otherwise be mistaken for a numeric
                    # opcode, so accept it anywhere left of the operator column.
                    if nfields == 1:
                        goto_not_offset = True
                    else:
                        inp.false_label = fields[i]
                        i += 1
                elif which_column < 8:
                    i += 1

                fi = fields[i] if i < nfields else ""
                if len(s) >= 16 and fi and s[16:].startswith(fi):
                    no_operator = False

                if not goto_not_offset:
                    imatch = None if no_operator else INTERP.get(fi)
                    match = OPS.get(fi) if fi else None
                    if self.num_interp_operands and not imatch and not match:
                        inp.operator = ""
                    elif match and self.num_interp_operands and i + 1 >= nfields:
                        match = None
                        inp.operator = ""
                    elif match and match.pinch_hit and self.num_interp_operands:
                        self.num_interp_operands -= 1
                        pinch_hitting = True
                        if i < nfields:
                            inp.operator = fields[i]
                            i += 1
                    else:
                        self.num_interp_operands = 0
                        if i < nfields:
                            inp.operator = fields[i]
                            i += 1
                if i < nfields:
                    inp.operand = fields[i]
                    i += 1
                if i < nfields:
                    inp.mod1 = fields[i]
                    i += 1
                if i < nfields:
                    inp.mod2 = fields[i]
                    i += 1
                if i < nfields:
                    inp.extra = fields[i]

            if inp.operand == "" and inp.operator == "TC":
                inp.operand = "-0"

            kind = ""
            if inp.operator == "" and not self.num_interp_operands:
                out.pc = inp.pc.copy()
                out.extend = inp.extend
                out.ebank = inp.ebank.copy()
                out.sbank = inp.sbank.copy()
                out.index_valid = inp.index_valid
            else:
                if inp.operator == "NOOP" and not self.num_interp_operands:
                    if inp.operand:
                        out.error = "Extra fields in line."
                        out.warning = True
                    if inp.pc.erasable:
                        inp.operator, inp.operand = "CA", "A"
                    else:
                        inp.operator, inp.operand = "TCF", "+1"
                    inp.alias = "NOOP"
                kind = self.process_operator(inp, out, pinch_hitting)

            # WriteDoIt:
            if self.stadr_invert and out.num_words > 0:
                if self.stadr_invert == 1:
                    out.words[0] = 0o77777 & ~out.words[0]
                self.stadr_invert -= 1

            self.update_bank_counts(out.pc)
            if (not out.pc.invalid and 0o30 <= out.pc.fb <= 0o37 and out.num_words > 0):
                out.sbank.current = 4 if out.pc.super else 3

            if inp.label and not out.equals and inp.operator not in ("MEMORY", "CHECK="):
                stype = SYMBOL_LABEL
                if inp.operator in ("ERASE", "DEC", "DEC*", "2DEC", "2DEC*", "OCT"):
                    stype = SYMBOL_VARIABLE
                self.edit_symbol(inp.label, inp.pc, stype)

            if write_output:
                self.record_line(inp, out, text, kind, fname, lineno)

    # ------------------------------------------------------------------
    def process_operator(self, inp: ParseIn, out: ParseOut, pinch_hitting: bool) -> str:
        """Dispatch one operator.  Returns the line kind for the listing."""
        while True:  # AliasRetry loop
            imatch = INTERP.get(inp.operator)
            if imatch is not None:
                return self.interpretive_opcode(inp, out, imatch)
            if self.num_interp_operands and not pinch_hitting:
                if inp.operator == "" and inp.operand == "":
                    out.words[0] = 0
                    out.pc = inp.pc.copy()
                    out.ebank = inp.ebank.copy()
                    out.sbank = inp.sbank.copy()
                    return ""
                if inp.operator == "" and inp.operand != "":
                    out.num_words = 1
                    self.parse_interpretive_operand(inp, out)
                    self.num_interp_operands -= 1
                    out.pc = inc_pc(inp.pc, out.num_words)
                    out.ebank = inp.ebank.copy()
                    out.sbank = inp.sbank.copy()
                    return "operand"
                out.error = "Missing interpretive operands."
                out.fatal = True
                out.num_words = 1
                out.words[0] = 0
                self.num_interp_operands = 0
                out.pc = inc_pc(inp.pc, 1)
                out.ebank = inp.ebank.copy()
                out.sbank = inp.sbank.copy()
                return "operand"

            match = OPS.get(inp.operator)
            if match is None:
                num_op = get_oct_or_dec(inp.operator)
                if num_op is not None:
                    flags = 0
                    value = get_oct_or_dec(inp.operand)
                    if value is None:
                        k = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
                        if k is None:
                            out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                            out.fatal = True
                            value = 0
                        else:
                            value = k.sreg
                    if ((not inp.extend and num_op == 2 and (value & 0o6000) == 0)
                            or (not inp.extend and num_op == 5 and (value & 0o6000) == 0o2000)
                            or (inp.extend and num_op == 4)
                            or (inp.extend and num_op == 5)):
                        flags |= KPLUS1
                    self.parse_general(inp, out, num_op << 12, flags)
                    out.words[0] = agc_add(out.words[0], self.opcode_offset)
                    out.ebank.oneshot = False
                    out.sbank.oneshot = False
                    return "basic"
                out.pc = inp.pc.copy()
                out.ebank = inp.ebank.copy()
                out.sbank = inp.sbank.copy()
                out.error = f'Unrecognized opcode/pseudo-op "{inp.operator}".'
                out.fatal = True
                out.pc = inc_pc(inp.pc, 1)
                return ""

            if match.parser is None and match.alias_op == "":
                out.pc = inp.pc.copy()
                return "pseudo"
            if match.parser is None:
                if inp.operand != "":
                    out.error = "Extra fields are present."
                    out.warning = True
                inp.alias = inp.operator
                inp.operator = match.alias_op
                inp.operand = match.alias_operand
                inp.mod1 = inp.mod2 = ""
                continue  # AliasRetry

            parser = getattr(self, match.parser)
            if match.parser == "parse_general":
                parser(inp, out, match.opcode, match.flags)
            else:
                parser(inp, out)
            i = out.words[0]
            out.words[0] = agc_add(out.words[0], self.opcode_offset)
            if (out.words[0] & 0o40000) and not (i & 0o40000):
                out.words[0] -= 1
            out.words[0] = (out.words[0] + match.adder) ^ match.xmask
            out.words[1] = (out.words[1] + match.adder2) ^ match.xmask2
            if inp.ebank.oneshot and match.parser in ("parse_bbcon", "parse_2cadr"):
                out.ebank.current = inp.ebank.last.copy()
            if inp.sbank.oneshot and match.parser in ("parse_bbcon", "parse_2cadr"):
                out.sbank.current = inp.sbank.last
            if match.parser != "parse_ebank_equals":
                out.ebank.oneshot = False
            if match.parser != "parse_sbank_equals":
                out.sbank.oneshot = False
            if match.optype == OpType.BASIC:
                return "basic"
            if match.optype == OpType.INTERPRETER:
                return "interp"
            if out.num_words:
                return "data"
            return "pseudo"

    # ------------------------------------------------------------------
    def interpretive_opcode(self, inp: ParseIn, out: ParseOut, imatch) -> str:
        if inp.operator == "STADR" or inp.operand == "STADR":
            self.stadr_invert = 2
        self.num_interp_operands = 0
        imatch2 = None
        if inp.operand:
            imatch2 = INTERP.get(inp.operand)
            if imatch2 is None:
                out.error = f'Unrecognized interpretive opcode "{inp.operand}".'
                out.fatal = True
        out.num_words = 1
        n = 0
        for m in (imatch, imatch2):
            if m is not None and m.num_operands:
                self.switch_increment[n] = m.arg_types[0]
                self.nnnn_fields[n] = m.nnnn
                n += 1
                if m.num_operands > 1:
                    self.switch_increment[n] = m.arg_types[1]
                    self.nnnn_fields[n] = 0
                    n += 1
        self.num_interp_operands = n
        self.raw_num_interp_operands = n
        w = 0o177 & (imatch.code + 1)
        if imatch2 is not None:
            w |= 0o37600 & ((imatch2.code + 1) << 7)
        out.words[0] = 0o77777 & ~w
        out.pc = inc_pc(inp.pc, out.num_words)
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        return "interp"

    # ------------------------------------------------------------------
    # Generic machine instruction
    # ------------------------------------------------------------------
    def parse_general(self, inp: ParseIn, out: ParseOut, opcode: int, flags: int):
        args = inp.mod1 + inp.mod2
        out.pc = inc_pc(inp.pc, 1)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 1

        if flags & PC1:
            opcode |= 0o1000
        elif flags & PC2:
            opcode |= 0o2000
        elif flags & PC3:
            opcode |= 0o3000
        elif flags & PC4:
            opcode |= 0o4000
        elif flags & PC5:
            opcode |= 0o5000
        elif flags & PC6:
            opcode |= 0o6000
        elif flags & PC7:
            opcode |= 0o7000
        elif flags & QC1:
            opcode |= 0o2000
        elif flags & QC2:
            opcode |= 0o4000
        elif flags & QC3:
            opcode |= 0o6000
        out.words[0] = opcode
        if flags & QCNOT0:
            out.words[0] |= 0o6000

        if inp.extend and not (flags & EXTENDED) and not inp.index_valid:
            if inp.extend != 2:
                out.error = "Illegally preceded by EXTEND."
                out.fatal = True
            out.extend = 0
        elif not inp.extend and (flags & EXTENDED):
            out.error = "Required EXTEND is missing."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.index_valid = False

        k: Address | None = None
        value = get_oct_or_dec(inp.operand)
        if value is not None and (flags & ENUMBER) and inp.operand[0] not in "+-":
            k = pseudo_to_struct(value)
            off = get_oct_or_dec(args)
            if off is not None:
                self.opcode_offset = off
        elif value is not None:
            if inp.operand[0] in "+-":
                k = inc_pc(inp.pc, value)
            else:
                k = pseudo_to_struct(value)
            if args:
                off = get_oct_or_dec(args)
                if off is not None:
                    self.opcode_offset = off
        else:
            k = self.fetch_symbol_plus_offset(inp.pc, inp.operand, args)
            if k is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                k = Address.invalid_address()

        self._general_do_it(inp, out, opcode, flags, k)

        out.extend = 0
        if (opcode == 0 and not (flags & EXTENDED) and not k.invalid
                and (k.constant or (k.erasable and k.unbanked)) and k.sreg == 6):
            out.extend = 2 if inp.alias == "" else 1
        out.index_valid = False

    def _general_do_it(self, inp: ParseIn, out: ParseOut, opcode: int, flags: int, k: Address):
        if k.invalid:
            if not out.fatal:
                out.error = "Destination address not resolved."
                out.fatal = True
            return
        if k.overflow:
            out.error = "Destination address out of range."
            out.fatal = True
            return
        if not k.address and not k.constant:
            out.error = "Destination not an address."
            out.fatal = True
            return
        if k.constant:
            k = pseudo_to_struct(k.value)
        if flags & KPLUS1:
            k = inc_pc(k, 1)
        i = k.sreg
        if not inp.index_valid:
            if (flags & FIXED) and not k.fixed:
                i &= ~0o7000
                out.error = "The address is not in fixed memory."
                out.fatal = True
            elif (flags & ERASABLE) and not k.erasable:
                i &= ~0o7600
                out.error = "The address is not in erasable memory."
                out.fatal = True
            if flags & (PC0 | PC1 | PC2 | PC3 | PC4 | PC5 | PC6 | PC7):
                if (i & 0o7000) != 0 and (i & 0o7000) != (opcode & 0o7000):
                    i &= ~0o7000
                    out.error = "Operand out of range."
                    out.fatal = True
            elif flags & (QC0 | QC1 | QC2 | QC3):
                if (i & 0o6000) != 0 and (i & 0o6000) != (opcode & 0o6000):
                    i &= ~0o6000
                    out.error = f"Operand ({i:o}) out of range."
                    out.fatal = True
            elif flags & QCNOT0:
                if 0 == (k.sreg & 0o6000):
                    i |= 0o6000
                    out.error = "Operand out of range."
                    out.fatal = True
        out.words[0] = opcode | i

    def parse_tcf(self, inp: ParseIn, out: ParseOut):
        if inp.operand == "":
            inp.operand = "+0"
        self.parse_general(inp, out, 0o10000, QCNOT0 | ENUMBER)

    def parse_index(self, inp: ParseIn, out: ParseOut):
        OPCODE = 0o50000
        out.extend = inp.extend
        out.pc = inc_pc(inp.pc, 1)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 1
        out.index_valid = True
        value = get_oct_or_dec(inp.operand)
        if value is not None:
            if inp.operand[0] in "+-":
                offset = inc_pc(inp.pc, value)
            else:
                offset = pseudo_to_struct(value)
            if inp.mod1:
                v2 = get_oct_or_dec(inp.mod1)
                if v2 is not None:
                    self.opcode_offset = v2
        else:
            offset = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
            if offset is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                out.words[0] = OPCODE
                return
        if not offset.address and not offset.constant:
            out.error = "Index is not an address."
            offset.sreg = 0
            out.fatal = True
        if (inp.extend and offset.sreg > 0o7777) or (not inp.extend and offset.sreg > 0o1777):
            out.error = "Index is out of range."
            offset.sreg = 0
            out.fatal = True
        if offset.constant:
            out.words[0] = OPCODE + offset.value
        else:
            out.words[0] = OPCODE + offset.sreg
        if out.words[0] == 0o50017:
            out.index_valid = False

    # ------------------------------------------------------------------
    # Interpretive operands and STORE-family
    # ------------------------------------------------------------------
    def parse_comma(self, inp: ParseIn) -> int:
        def strip(s: str) -> tuple[str, int]:
            if len(s) >= 3 and s.endswith(",1"):
                return s[:-2], 1
            if len(s) >= 3 and s.endswith(",2"):
                return s[:-2], 2
            return s, 0

        if inp.mod1:
            inp.mod1, t = strip(inp.mod1)
            return t
        if inp.operand:
            inp.operand, t = strip(inp.operand)
            return t
        return 0

    def parse_interpretive_operand(self, inp: ParseIn, out: ParseOut):
        self.arg_type = self.parse_comma(inp)
        out.pc = inc_pc(inp.pc, 1)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 1
        out.words[0] = 0
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
            out.index_valid = False

        value = get_oct_or_dec(inp.operand)
        if value is not None:
            if inp.operand[0] in "+-":
                k = inc_pc(inp.pc, value)
            else:
                k = Address.const(value)
        else:
            k = self.fetch_symbol_plus_offset(inp.pc, inp.operand, "")
        if k is None or k.invalid:
            out.error = f'Operand "{inp.operand}" not resolved.'
            out.fatal = True
            return

        kmod = 0
        if inp.mod1:
            args = inp.mod1 + inp.mod2
            v = get_oct_or_dec(args)
            if v is None:
                out.error = f'Modifier "{inp.mod1}" not resolved.'
                out.fatal = True
                return
            kmod = v
        self.opcode_offset = kmod

        while True:  # RetryMem
            if k.constant:
                idx = self.raw_num_interp_operands - self.num_interp_operands
                i = self.nnnn_fields[idx]
                if (i & 3) == 1:
                    out.words[0] = (((k.value // 15) & 0o77) << 8) | (k.value % 15)
                    out.words[0] |= 0o360 & i
                elif (i & 3) == 2:
                    out.words[0] = k.value
                    out.words[0] |= i & ~3
                else:
                    i = k.value + self.opcode_offset
                    if i < 0:
                        i -= 1
                    i &= 0o77777
                    self.opcode_offset = 0
                    if 0o40000 & i:
                        out.words[0] = i
                    else:
                        k = pseudo_to_struct(i)
                        if k.invalid or not k.address:
                            out.error = "Incorrect operand type."
                            out.fatal = True
                            return
                        continue
                break
            elif k.address and k.erasable:
                if not k.banked:
                    out.words[0] = k.sreg
                else:
                    out.words[0] = 0o400 * k.eb + (k.sreg - 0o1400)
                break
            elif k.address and k.fixed:
                if not k.banked:
                    out.words[0] = k.sreg
                else:
                    out.words[0] = 0o2000 * k.fb + (k.sreg - 0o2000)
                break
            else:
                out.error = "Incorrect operand type."
                out.fatal = True
                return

        out.words[0] = out.words[0] + self.opcode_offset
        idx = self.raw_num_interp_operands - self.num_interp_operands
        if self.switch_increment[idx]:
            out.words[0] += 1
            out.words[0] &= 0o37777
            if self.arg_type == 2:
                out.words[0] = 0o77777 & ~out.words[0]

    def _parse_st(self, inp: ParseIn, out: ParseOut, opcode: int, flags: int):
        opcode += 0o4000 * self.arg_type
        out.pc = inc_pc(inp.pc, 1)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 1
        if flags & QC1:
            opcode |= 0o2000
        elif flags & QC2:
            opcode |= 0o4000
        elif flags & QC3:
            opcode |= 0o6000
        out.words[0] = opcode
        if inp.extend and not (flags & EXTENDED) and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.index_valid = False

        value = get_oct_or_dec(inp.operand)
        if value is not None and (flags & ENUMBER) and inp.operand[0] not in "+-":
            k = pseudo_to_struct(value)
            off = get_oct_or_dec(inp.mod1)
            if off is not None:
                self.opcode_offset = off
        elif value is not None and inp.mod1 == "":
            k = inc_pc(inp.pc, value)
        else:
            k = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
            if k is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                return
            if k.constant:
                k = pseudo_to_struct(k.value)

        if k.invalid:
            out.error = "Destination address not resolved."
            out.fatal = True
        elif k.overflow:
            out.error = "Destination address out of range."
            out.fatal = True
        elif not k.address:
            out.error = "Destination not an address."
            out.fatal = True
        else:
            if k.constant:
                k = pseudo_to_struct(k.value)
            if flags & KPLUS1:
                k = inc_pc(k, 1)
            if not k.erasable:
                i = 0
                out.error = "The Address is not in erasable memory."
                out.fatal = True
            elif not k.banked:
                i = k.sreg
            else:
                i = 0o400 * k.eb + (k.sreg - 0o1400)
            out.words[0] = opcode | i
        out.extend = 0
        out.index_valid = False

    def parse_stcall(self, inp: ParseIn, out: ParseOut):
        self.arg_type = self.parse_comma(inp)
        self.switch_increment[0] = 0
        self.nnnn_fields[0] = 0
        self.raw_num_interp_operands = self.num_interp_operands = 1
        self._parse_st(inp, out, 0o34000, ERASABLE | ENUMBER | KPLUS1)

    def parse_stodl(self, inp: ParseIn, out: ParseOut):
        self.arg_type = self.parse_comma(inp)
        self.switch_increment[0] = 1
        self.nnnn_fields[0] = 0
        self.raw_num_interp_operands = self.num_interp_operands = 1
        self._parse_st(inp, out, 0o14000, ERASABLE | ENUMBER | KPLUS1)

    def parse_store(self, inp: ParseIn, out: ParseOut):
        self.arg_type = self.parse_comma(inp)
        self.num_interp_operands = 0
        self._parse_st(inp, out, 0o00000, ERASABLE | ENUMBER | KPLUS1)

    def parse_stovl(self, inp: ParseIn, out: ParseOut):
        self.arg_type = self.parse_comma(inp)
        self.switch_increment[0] = 1
        self.nnnn_fields[0] = 0
        self.raw_num_interp_operands = self.num_interp_operands = 1
        self._parse_st(inp, out, 0o24000, ERASABLE | ENUMBER | KPLUS1)

    # ------------------------------------------------------------------
    # Location counter pseudo-ops
    # ------------------------------------------------------------------
    def parse_bank(self, inp: ParseIn, out: ParseOut):
        out.extend = inp.extend
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
        if inp.operand == "":
            out.pc = inp.pc.copy()
            if out.pc.invalid:
                return
            if not out.pc.address or not out.pc.fixed:
                out.error = "Works only for fixed-memory."
                out.fatal = True
                return
            if out.pc.banked:
                i = out.pc.fb + 0o10 * out.pc.super
                out.pc.sreg = 0o2000 + self.used_in_bank[i]
                out.pc.value = 0o10000 + i * 0o2000 + self.used_in_bank[i]
            elif 0o4000 <= out.pc.value <= 0o5777:
                out.pc.sreg = 0o4000 + self.used_in_bank[2]
                out.pc.value = out.pc.sreg
            elif 0o6000 <= out.pc.value <= 0o7777:
                out.pc.sreg = 0o6000 + self.used_in_bank[3]
                out.pc.value = out.pc.sreg
            out.pc.overflow = False
            inp.pc = out.pc.copy()
            return
        value = get_oct_or_dec(inp.operand)
        if value is not None:
            if 0 <= value <= 0o43:
                pc = Address(address=True, sreg=0o2000, fixed=True, banked=True)
                if value >= 0o40:
                    pc.super = True
                    pc.fb = value - 0o10
                else:
                    pc.super = False
                    pc.fb = value
                if value in (2, 3):
                    pc.value = value * 0o2000
                else:
                    pc.value = 0o10000 + value * 0o2000
                pc.value += self.used_in_bank[value]
                pc.sreg += self.used_in_bank[value]
                out.pc = pc
            else:
                out.error = "BANK operand range is 00 to 43."
                out.fatal = True
                out.pc = Address.invalid_address()
        else:
            out.error = "BANK pseudo-op has an invalid operand."
            out.fatal = True
            out.pc = Address.invalid_address()
        inp.pc = out.pc.copy()

    def parse_block(self, inp: ParseIn, out: ParseOut):
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
        value = get_oct_or_dec(inp.operand)
        if value is not None:
            if value in (0, 2, 3):
                used = self.used_in_bank[value] + value * 0o2000
                pc = Address(address=True, sreg=used, unbanked=True, value=used)
                if value == 0:
                    pc.erasable = True
                else:
                    pc.fixed = True
                out.pc = pc
                if value == 0:
                    out.ebank.current = pc.copy()
            else:
                out.error = "BLOCK operand must be 0, 2, or 3."
                out.pc = Address.invalid_address()
        else:
            out.error = "BLOCK pseudo-op has no operand."
            out.pc = Address.invalid_address()
        inp.pc = out.pc.copy()

    def parse_setloc(self, inp: ParseIn, out: ParseOut):
        out.pc = inp.pc.copy()
        out.sbank = inp.sbank.copy()
        out.extend = inp.extend
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
        value = get_oct_or_dec(inp.operand)
        if value is not None:
            if inp.operand[0] in "+-":
                out.pc = inc_pc(out.pc, value)
            else:
                out.pc = pseudo_to_struct(value)
                if out.pc.invalid:
                    out.error = "Addresses must be between 0 and 0117777."
                    out.fatal = True
        else:
            sym = self.get_symbol(inp.operand)
            if sym is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                out.pc = Address.invalid_address()
            else:
                out.pc = sym.value.copy()
        off = get_oct_or_dec(inp.mod1)
        if off is not None:
            out.pc = inc_pc(out.pc, off)
        inp.pc = out.pc.copy()
        if not out.pc.invalid and out.pc.erasable:
            out.ebank.current = out.pc.copy()
            out.ebank.last = out.pc.copy()
            out.ebank.oneshot = False

    def parse_secsiz(self, inp: ParseIn, out: ParseOut):
        out.pc = inp.pc.copy()
        out.extend = inp.extend
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.index_valid = inp.index_valid
        try:
            size = int(inp.operand, 8)
        except ValueError:
            size = 0
        pc = inp.pc
        if size == 0 or pc.invalid or not pc.address or not pc.fixed or pc.overflow:
            out.error = "Irregular SECSIZ."
            out.warning = True
            return
        if pc.banked:
            count = pc.sreg - 0o2000
            bank = pc.fb + 0o10 * pc.super
        elif 0o4000 <= pc.sreg < 0o6000:
            count, bank = pc.sreg - 0o4000, 2
        elif 0o6000 <= pc.sreg < 0o10000:
            count, bank = pc.sreg - 0o6000, 3
        else:
            out.error = "Irregular SECSIZ."
            out.warning = True
            return
        new = count + size
        if new > 0o2000:
            self.used_in_bank[bank] = 0o2000
            out.error = "Irregular SECSIZ."
            out.warning = True
            return
        if new > self.used_in_bank[bank]:
            self.used_in_bank[bank] = new

    def parse_erase(self, inp: ParseIn, out: ParseOut):
        out.pc = inc_pc(inp.pc, 1)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
            out.index_valid = False
        value = get_oct_or_dec(inp.operand)
        if value is not None:
            if value < 0:
                out.error = "Address increment is negative."
                out.warning = True
            elif inp.mod1 == "-":
                # "ERASE start - end": behaves like EQUALS
                self.parse_equals(inp, out)
            else:
                if inp.mod1 and not out.fatal:
                    out.error = "Extra fields are present."
                    out.warning = True
                out.pc = inc_pc(inp.pc, 1 + value)
                if not out.pc.invalid:
                    if not out.pc.erasable:
                        out.error = "Not in erasable memory."
                        out.fatal = True
                    elif out.pc.overflow:
                        out.error = "May overflow memory bank."
                        out.warning = True
        elif inp.operand != "":
            out.error = "Illegal number."
            out.fatal = True

    # ------------------------------------------------------------------
    # Symbol-defining pseudo-ops
    # ------------------------------------------------------------------
    def parse_equals(self, inp: ParseIn, out: ParseOut):
        out.pc = inp.pc.copy()
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.label_value = Address.invalid_address()
        out.num_words = 0
        out.equals = True
        if inp.label == "":
            out.label_value_valid = False
            return
        if inp.operand == "" and inp.mod1 == "":
            self.edit_symbol(inp.label, inp.pc, SYMBOL_CONSTANT)
            out.label_value = inp.pc.copy()
            return
        value = get_oct_or_dec(inp.operand)
        if value is None:
            if inp.mod1 in ("+", "-"):
                if inp.mod2 != "":
                    label_value = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1 + inp.mod2)
                else:
                    out.error = "Syntax error, invalid offset specified"
                    out.fatal = True
                    return
            else:
                label_value = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
            if label_value is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                return
            if self.opcode_offset:
                if label_value.constant:
                    label_value.value += self.opcode_offset
                else:
                    label_value = inc_pc(label_value, self.opcode_offset)
            self.edit_symbol(inp.label, label_value, SYMBOL_CONSTANT)
            out.label_value_valid = True
        else:
            if inp.operand[0] in "+-":
                label_value = inc_pc(inp.pc, value)
            else:
                if value < -16383 or value > 32767:
                    out.error = "Value out of range---truncating"
                    out.warning = True
                    value = max(-16383, min(32767, value))
                label_value = Address.const(value)
                seg = pseudo_to_struct(value)
                if not seg.invalid:
                    label_value = seg
                    if inp.operator == "ERASE" or (value >= 0o2000 and inp.operator == "EQUALS"):
                        label_value.constant = False
                    else:
                        label_value.constant = True
            self.edit_symbol(inp.label, label_value, SYMBOL_CONSTANT)
        out.label_value = label_value.copy()

    def parse_equals_ecadr(self, inp: ParseIn, out: ParseOut):
        out.pc = inp.pc.copy()
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()

    def parse_eq_minus(self, inp: ParseIn, out: ParseOut):
        out.pc = inp.pc.copy()
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.label_value = Address.invalid_address()
        out.num_words = 0
        out.equals = True
        if inp.label == "":
            return
        if inp.operand == "":
            out.error = "Missing operand."
            out.fatal = True
            return
        lv = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
        if lv is None:
            out.error = f'Symbol "{inp.operand}" undefined or offset bad'
            out.fatal = True
            lv = Address.invalid_address()
        else:
            lv = Address.const(lv.sreg - inp.pc.sreg)
        self.edit_symbol(inp.label, lv, SYMBOL_CONSTANT)
        out.label_value = lv

    def parse_check_equals(self, inp: ParseIn, out: ParseOut):
        out.pc = inp.pc.copy()
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        if inp.label == "":
            out.error = "Label must be supplied for CHECK= directive."
            out.fatal = True
            return
        sym = self.get_symbol(inp.label)
        if sym is None:
            out.error = f'Symbol "{inp.label}" not defined, skipping...'
            out.warning = True
            return
        lh = sym.value.value
        if inp.operand == "" and inp.mod1 == "":
            out.error = "Operand must be supplied for CHECK= directive."
            out.fatal = True
            return
        rh = get_oct_or_dec(inp.operand)
        if rh is None:
            cv = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
            if cv is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.warning = True
                return
            if self.opcode_offset:
                if cv.constant:
                    cv.value += self.opcode_offset
                else:
                    cv = inc_pc(cv, self.opcode_offset)
                rh = cv.value
            else:
                return
        else:
            if inp.operand[0] in "+-":
                cv = inc_pc(inp.pc, rh)
            else:
                cv = Address.const(max(-16383, min(32767, rh)))
            rh = cv.value
        if lh != rh:
            out.error = "Address check failed"
            out.fatal = True

    def parse_ebank_equals(self, inp: ParseIn, out: ParseOut):
        out.extend = inp.extend
        out.index_valid = inp.index_valid
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 0
        out.pc = inp.pc.copy()
        if inp.mod1:
            out.error = "Extra fields."
            out.warning = True
        value = get_oct_or_dec(inp.operand)
        if value is not None:
            if value < 0o10 or value > 0o3777:
                out.error = "EBank address value out of range."
                out.fatal = True
                return
            address = pseudo_to_struct(value)
        else:
            address = self.fetch_symbol_plus_offset(inp.pc, inp.operand, "")
            if address is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                return
            address = inc_pc(address, self.opcode_offset)
        if address.invalid:
            out.error = "Destination address not resolved."
            out.fatal = True
            return
        if not address.erasable:
            out.error = "Destination not erasable."
            out.fatal = True
            return
        if address.sreg < 0 or address.sreg > 0o1777:
            out.error = "Destination address out of range."
            out.fatal = True
            return
        out.ebank.last = out.ebank.current.copy()
        out.ebank.current = address.copy()
        out.ebank.oneshot = True
        out.label_value = address.copy()
        out.label_value_valid = True

    def parse_sbank_equals(self, inp: ParseIn, out: ParseOut):
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 0
        out.pc = inp.pc.copy()
        if inp.operand == "":
            return
        if inp.mod1:
            out.error = "Extra fields."
            out.warning = True
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
            out.index_valid = False
        value = get_oct_or_dec(inp.operand)
        if value is not None:
            address = pseudo_to_struct(value)
        else:
            address = self.fetch_symbol_plus_offset(inp.pc, inp.operand, "")
            if address is None:
                out.error = "Symbol undefined or offset bad"
                out.fatal = True
                return
            address = inc_pc(address, self.opcode_offset)
        if address.invalid:
            out.error = "Destination address not resolved."
            out.fatal = True
            return
        if not address.fixed:
            out.error = "Destination not in fixed memory."
            out.fatal = True
            return
        if address.sreg < 0o2000 or address.sreg > 0o3777:
            out.error = "Destination address out of range."
            out.fatal = True
            return
        if 0o30 <= address.fb <= 0o37:
            out.sbank.last = out.sbank.current
            out.sbank.current = 4 if address.super else 3
        else:
            out.error = "Destination address not in superbank."
            out.sbank.current = 0
            out.fatal = True
            return
        out.sbank.oneshot = True
        out.label_value = address.copy()
        out.label_value_valid = True

    # ------------------------------------------------------------------
    # Constants
    # ------------------------------------------------------------------
    def _common_data_prologue(self, inp: ParseIn, out: ParseOut, nwords: int) -> bool:
        out.pc = inc_pc(inp.pc, nwords)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = nwords
        out.words = [0, 0]
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
            out.index_valid = False
        if inp.operand == "":
            out.error = "Operand is missing."
            out.fatal = True
            return False
        return True

    def parse_dec(self, inp: ParseIn, out: ParseOut):
        if not self._common_data_prologue(inp, out, 1):
            return
        if inp.operand[0] in "EB":
            tmpval = 1.0
            mod1, mod2 = inp.operand, inp.mod1
        else:
            tmpval = _strtod(inp.operand)
            mod1, mod2 = inp.mod1, inp.mod2
        if "." not in inp.operand and inp.mod1 == "" and inp.mod2 == "":
            mod1 = "B-14"
        x = tmpval * scale_factor(mod1) * scale_factor(mod2)
        sign = False
        if inp.operand[0] == "-":
            sign = True
            x = -x
        if _fuzzed_is_int(x):
            value = int(x)
        else:
            if x >= 1.0:
                out.error = "DEC value out of range."
                out.fatal = True
                return
            value = 0
            for _ in range(14):
                value <<= 1
                if x >= 0.5:
                    value += 1
                    x -= 0.5
                x *= 2
            if x >= 0.5 and value < 0o37777:
                value += 1
        if sign:
            value = 0x7FFF & ~value
        out.words[0] = value & 0o77777

    def parse_2dec(self, inp: ParseIn, out: ParseOut):
        if not self._common_data_prologue(inp, out, 2):
            return
        operand = inp.operand
        if operand[0] in "EB":
            tmpval = 1.0
            mod1, mod2 = operand, inp.mod1
        else:
            epos = operand.find("E")
            bpos = operand.find("B")
            if epos >= 0 or bpos >= 0:
                # scale factors glued to the number, e.g. "1.5E3B-4"
                cut = min(p for p in (epos, bpos) if p >= 0)
                number = operand[:cut]
                rest = operand[cut:]
                mod1 = mod2 = ""
                if epos >= 0 and bpos >= 0:
                    if epos < bpos:
                        mod1, mod2 = operand[epos:bpos], operand[bpos:]
                    else:
                        mod1, mod2 = operand[epos:], operand[bpos:epos]
                else:
                    mod1 = rest
                tmpval = _strtod(number)
            else:
                if inp.extra:
                    if inp.mod1 in ("E", "B"):
                        mod1 = inp.mod1 + inp.mod2
                        mod2 = inp.extra
                    else:
                        mod1 = inp.mod1
                        mod2 = inp.mod2 + inp.extra
                else:
                    if inp.mod1 in ("E", "B"):
                        mod1 = inp.mod1 + inp.mod2
                        mod2 = ""
                    else:
                        mod1, mod2 = inp.mod1, inp.mod2
                tmpval = _strtod(operand)
        if "." not in inp.operand and inp.mod1 == "" and inp.mod2 == "":
            mod1 = "B-28"
        x = tmpval * scale_factor(mod1) * scale_factor(mod2)
        sign = False
        if inp.operand[0] == "-":
            sign = True
            x = -x
        if _fuzzed_is_int(x):
            value = int(x)
        else:
            if x >= 1.0:
                out.error = "2DEC value out of range."
                out.fatal = True
                return
            value = 0
            for _ in range(28):
                value <<= 1
                if x >= 0.5:
                    value += 1
                    x -= 0.5
                x *= 2
            if x >= 0.5 and value < 0x0FFFFFFF:
                value += 1
        lo = value & 0x3FFF
        hi = (value >> 14) & 0x3FFF
        if sign:
            hi = (~hi) & 0x7FFF
            lo = (~lo) & 0x7FFF
        out.words[0] = hi
        out.words[1] = lo

    def parse_vn(self, inp: ParseIn, out: ParseOut):
        if not self._common_data_prologue(inp, out, 1):
            return
        if not inp.operand.isdigit():
            out.error = "Operand is not a decimal number."
            out.fatal = True
            return
        v = int(inp.operand, 10)
        out.words[0] = (v % 100) | ((v // 100) << 7)

    def parse_oct(self, inp: ParseIn, out: ParseOut):
        if not self._common_data_prologue(inp, out, 1):
            return
        s = inp.operand
        body = s[1:] if s[0] in "+-" else s
        if body and all(c in "01234567" for c in body):
            value = int(body, 8)
            if value & ~0o77777:
                value &= 0o77777
                out.error = "Value out of range."
                out.warning = True
            if s[0] == "-":
                value = (~value) & 0o77777
            out.words[0] = value
        else:
            out.error = "Not an octal number."
            out.fatal = True

    def parse_2oct(self, inp: ParseIn, out: ParseOut):
        if not self._common_data_prologue(inp, out, 2):
            return
        s = inp.operand
        body = s[1:] if s[0] in "+-" else s
        if body and all(c in "01234567" for c in body):
            v1 = int(body, 8)
            if inp.mod1 and all(c in "01234567" for c in inp.mod1):
                value = ((v1 & 0o77777) << 15) | (int(inp.mod1, 8) & 0o77777)
            else:
                value = v1 & 0o7777777777
            if value & ~0o7777777777:
                value &= 0o7777777777
                out.error = "Value out of range."
                out.warning = True
            if s[0] == "-":
                value = ~value
            out.words[0] = 0o77777 & (value >> 15)
            out.words[1] = 0o77777 & value
        else:
            out.error = "Not an octal number."
            out.fatal = True

    # ------------------------------------------------------------------
    # Address constants
    # ------------------------------------------------------------------
    def parse_cadr(self, inp: ParseIn, out: ParseOut):
        out.pc = inc_pc(inp.pc, 1)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 1
        out.words[0] = 0
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
            out.index_valid = False
        value = get_oct_or_dec(inp.operand)
        if value is not None and inp.mod1 == "":
            address = pseudo_to_struct(value)
        else:
            address = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1 + inp.mod2)
            if address is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                return
        if address.invalid:
            out.error = "Destination address not resolved."
            out.fatal = True
            return
        if not address.address:
            out.error = "Destination is not a memory address."
            out.fatal = True
            return
        if not address.fixed or not address.banked:
            out.error = "Destination not in an F-bank."
            out.fatal = True
            return
        v = address.value
        if address.super and address.fb >= 0o30:
            v -= 0o10 * 0o2000
        if v < 0o10000 or v > 0o107777:
            out.error = "Destination address out of range."
            out.fatal = True
            return
        out.words[0] = v - 0o10000

    def parse_2cadr(self, inp: ParseIn, out: ParseOut):
        out.pc = inc_pc(inp.pc, 2)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 2
        out.words = [0, 0]
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
            out.index_valid = False
        address = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
        if address is None:
            out.error = f'Symbol "{inp.operand}" undefined or offset bad'
            out.fatal = True
            return
        if address.invalid:
            out.error = "Destination address not resolved."
            out.fatal = True
            return
        if not address.address:
            out.error = "Destination is not a memory address."
            out.fatal = True
            return
        out.words[0] = address.sreg
        cur = inp.ebank.current
        if 0 <= cur.sreg < 0o1400:
            out.words[1] = cur.sreg // 0o400
        else:
            out.words[1] = cur.eb
        if address.sreg < 0o2000:
            pass
        elif address.sreg <= 0o7777:
            if address.sreg < 0o4000:
                out.words[1] |= address.fb << 10
            else:
                out.words[1] |= (address.sreg // 0o2000) << 10
        else:
            out.error = "Internal error implementing 2CADR."
            out.fatal = True
            return
        if 0o30 <= address.fb <= 0o37:
            out.words[1] |= (4 if address.super else 3) << 4
        else:
            out.words[1] |= inp.sbank.current << 4

    def parse_2fcadr(self, inp: ParseIn, out: ParseOut):
        out.pc = inc_pc(inp.pc, 2)
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 2
        out.words = [0, 0]
        address = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
        if address is None or address.invalid or not address.address or not address.fixed:
            out.error = f'2FCADR: bad destination "{inp.operand}"'
            out.fatal = True
            return
        if 0o2000 <= address.sreg <= 0o3777:
            out.words[0] = (address.fb << 10) | (address.sreg - 0o2000)
            out.words[1] = address.sreg
        elif 0o4000 <= address.sreg <= 0o7777:
            out.words[0] = address.sreg
            out.words[1] = address.sreg
        else:
            out.error = "Internal error implementing 2FCADR."
            out.fatal = True

    def _parse_bbcon_raw(self, star: bool, inp: ParseIn, out: ParseOut):
        out.pc = inc_pc(inp.pc, 1)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 1
        out.words[0] = 0
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
            out.index_valid = False
        value = get_oct_or_dec(inp.operand)
        if (value is not None and inp.mod1 == "") or star:
            address = inc_pc(inp.pc, value or 0)
        else:
            address = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
            if address is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                return
        if star:
            # BBCON*: refer to the last used location of the last non-empty bank.
            bank = 0
            highest = 0
            for bank in range(0o43, -1, -1):
                highest = self.prior_used_in_bank[bank]
                if highest > 0:
                    break
            address = Address(address=True, banked=True, fixed=True)
            address.fb = bank - 0o10 if bank >= 0o40 else bank
            address.super = bank >= 0o40
            address.sreg = 0o4000 + highest
            address.value = 0o10000 + (address.sreg - 0o2000) + 0o2000 * address.fb
            if address.super and address.fb >= 0o30:
                address.value += 0o10 * 0o2000
        if address.invalid:
            out.error = "Destination address not resolved."
            out.fatal = True
            return
        if not address.address:
            out.error = "Destination is not a memory address."
            out.fatal = True
            return
        if not address.fixed:
            out.error = "Destination is not in fixed memory."
            out.fatal = True
            return
        if address.sreg < 0o2000 or address.sreg > 0o7777:
            out.error = "Destination address out of range."
            out.fatal = True
            return
        if not address.banked:
            v = address.sreg // 0o2000
        else:
            v = address.fb
        ebank = inp.ebank.current
        eb = ebank.eb
        if 0 <= ebank.sreg < 0o1400:
            eb = ebank.sreg // 0o400
        v = (v << 10) | eb
        if 0o30 <= address.fb <= 0o37:
            v |= (4 if address.super else 3) << 4
        else:
            v |= inp.sbank.current << 4
        out.words[0] = v

    def parse_bbcon(self, inp: ParseIn, out: ParseOut):
        self._parse_bbcon_raw(False, inp, out)

    def parse_bbcon_star(self, inp: ParseIn, out: ParseOut):
        self._parse_bbcon_raw(True, inp, out)

    def parse_genadr(self, inp: ParseIn, out: ParseOut):
        out.pc = inc_pc(inp.pc, 1)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 1
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
            out.index_valid = False
        value = get_oct_or_dec(inp.operand)
        if value is not None and inp.mod1 == "":
            address = inc_pc(inp.pc, value)
        else:
            address = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
            if address is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                out.words[0] = 0
                return
        if address.invalid:
            out.error = "Destination address not resolved."
            out.fatal = True
            return
        if address.constant:
            address = pseudo_to_struct(address.value)
        if not address.address:
            out.error = "Destination is not a memory address."
            out.fatal = True
            return
        out.words[0] = address.sreg
        pc = inp.pc
        if inp.operator in ("ADRES", "DNPTR", "-DNPTR"):
            if (pc.erasable and address.erasable and pc.banked and address.banked
                    and pc.eb != address.eb):
                out.error = "Destination must be in current erasable bank."
                out.fatal = True
            elif (pc.fixed and address.fixed and pc.banked and address.banked
                    and (pc.fb != address.fb or pc.super != address.super)):
                out.error = "Destination must be in current fixed bank."
                out.fatal = True
        elif inp.operator == "REMADR":
            if pc.erasable and address.erasable and pc.eb == address.eb:
                out.error = "Destination must not be in current erasable bank."
                out.fatal = True
            elif (pc.fixed and address.fixed and pc.fb == address.fb
                    and pc.super == address.super):
                out.error = "Destination must not be in current fixed bank."
                out.fatal = True

    def parse_ecadr(self, inp: ParseIn, out: ParseOut):
        out.pc = inc_pc(inp.pc, 1)
        if not out.pc.invalid and out.pc.overflow:
            out.error = "Next code may overflow storage."
            out.warning = True
        out.ebank = inp.ebank.copy()
        out.sbank = inp.sbank.copy()
        out.num_words = 1
        out.words[0] = 0
        if inp.extend and not inp.index_valid:
            out.error = "Illegally preceded by EXTEND."
            out.fatal = True
            out.extend = 0
        if inp.index_valid:
            out.error = "Illegally preceded by INDEX."
            out.fatal = True
            out.index_valid = False
        value = get_oct_or_dec(inp.operand)
        if value is not None and inp.mod1 == "":
            address = inc_pc(inp.pc, value)
        else:
            address = self.fetch_symbol_plus_offset(inp.pc, inp.operand, inp.mod1)
            if address is None:
                out.error = f'Symbol "{inp.operand}" undefined or offset bad'
                out.fatal = True
                return
        if address.invalid:
            out.error = "Destination address not resolved."
            out.fatal = True
            return
        if address.constant and not address.address:
            if address.value < 0o1400:
                address.constant = False
                address.address = True
                address.erasable = True
                address.banked = False
                address.sreg = address.value
            elif address.value < 0o4000:
                address.constant = False
                address.address = True
                address.erasable = True
                address.banked = True
                address.eb = address.value // 0o400
                address.sreg = (address.value % 0o400) + 0o1400
        if not address.address:
            out.error = "Destination is not a memory address."
            out.fatal = True
            return
        if not address.erasable:
            out.error = "Destination not in erasable memory."
            out.fatal = True
            return
        if address.value < 0 or address.value > 0o3777:
            out.error = "Destination address out of range."
            out.fatal = True
            return
        out.words[0] = address.value

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------
    def record_line(self, inp: ParseIn, out: ParseOut, text: str, kind: str, fname: str, lineno: int):
        if out.fatal:
            self.fatals += 1
            if self.verbose:
                print(f"{fname}:{lineno}: Fatal Error: {out.error}")
        elif out.warning:
            self.warnings += 1
            if self.verbose:
                print(f"{fname}:{lineno}: Warning: {out.error}")

        has_code = bool(inp.label or inp.false_label or inp.operator or inp.operand)
        words = []
        if out.num_words > 0:
            words = [w & 0o77777 for w in out.words[: out.num_words]]
            if not inp.pc.invalid and inp.pc.address and inp.pc.fixed:
                bank = inp.pc.bank_number()
                for i, w in enumerate(words):
                    offset = (inp.pc.sreg + i) & 0o1777
                    self.fixed[bank][offset] = w
                    self.used[bank][offset] = True
        operator = inp.alias if inp.alias else inp.operator
        operand = "" if inp.alias else inp.operand
        suffix = {1: ",1", 2: ",2"}.get(self.arg_type, "")
        mod1, mod2 = inp.mod1, inp.mod2
        if suffix:
            if mod1:
                mod1 += suffix
            elif operand:
                operand += suffix
        if kind == "" and out.num_words:
            kind = "data"
        if kind == "pseudo" and out.equals:
            kind = "equals"
        if inp.operator == "ERASE":
            kind = "erase"
        rec = LineRecord(
            file=fname,
            line=lineno,
            text=text,
            pc=inp.pc.copy() if has_code else None,
            words=words,
            label=inp.label,
            false_label=inp.false_label,
            operator=operator,
            operand=operand,
            mod1=mod1,
            mod2=mod2,
            comment=inp.comment,
            comment_column=inp.comment_column,
            error=out.error,
            fatal=out.fatal,
            warning=out.warning,
            kind=kind,
            label_value=out.label_value.copy() if out.label_value_valid or out.equals else None,
        )
        self.lines.append(rec)

    def add_bugger_words(self) -> dict[int, tuple[int, int]]:
        """Append bank-id words and the checksum ("bugger word") to each bank.

        The AGC self-check sums each bank including the bugger word and
        expects the bank number as result.  Returns {bank: (offset, word)}.
        """
        result: dict[int, tuple[int, int]] = {}
        for bank in range(NUM_FIXED_BANKS):
            offset_base = {2: 0o4000, 3: 0o6000}.get(bank, 0o2000)
            value = self.used_in_bank[bank]
            if value <= 0:
                continue
            if value < 0o1776 and not self.used[bank][value]:
                self.fixed[bank][value] = value + offset_base
                self.used[bank][value] = True
                value += 1
            if value < 0o1777 and not self.used[bank][value]:
                self.fixed[bank][value] = value + offset_base
                self.used[bank][value] = True
                value += 1
            if value < 0o2000 and not self.used[bank][value]:
                bugger = 0
                for off in range(value):
                    bugger = _agc_sum(bugger, self.fixed[bank][off])
                if 0 == (0o40000 & bugger):
                    guess = _agc_sum(bank, 0o77777 & ~bugger)
                else:
                    guess = _agc_sum(0o77777 & ~bank, 0o77777 & ~bugger)
                self.fixed[bank][value] = guess
                self.used[bank][value] = True
                result[bank] = (value, guess)
        return result


def _agc_to_native(n: int) -> int:
    n &= 0o77777
    if n & 0o40000:
        return -(0o77777 & ~n)
    return n


def _agc_sum(n1: int, n2: int) -> int:
    """One's-complement 15-bit add with end-around carry (yaYUL ``Add``)."""
    total = _agc_to_native(n1) + _agc_to_native(n2)
    if total > 16383:
        total -= 16384
        total += 1
    elif total < -16383:
        total += 16384
        total -= 1
    if total >= 0:
        return total
    return 0o77777 & ~(-total)


def _strtod(s: str) -> float:
    """Behave like C strtod: parse the longest numeric prefix."""
    best = 0.0
    for n in range(len(s), 0, -1):
        try:
            return float(s[:n])
        except ValueError:
            continue
    return best
