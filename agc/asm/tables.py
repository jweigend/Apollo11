"""Opcode tables for the Block II AGC assembler.

Three kinds of operators appear in the source:

* basic machine instructions (TC, CA, TS, ...),
* pseudo-operators that steer the assembler (BANK, SETLOC, EQUALS, 2DEC, ...),
* interpretive instructions executed by the AGC's built-in "Interpreter"
  (DLOAD, VXSC, STORE, ...).  Two interpretive opcodes are packed in one
  word and their operands follow as separate words.

The flag bits mirror yaYUL so that address-range checks behave identically.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# Flags controlling ParseGeneral behaviour.
KPLUS1 = 0x1        # instruction encodes K+1 (double precision ops)
EXTENDED = 0x2      # requires preceding EXTEND
PC0 = 0x4
QC0 = 0x8
PC1 = 0x10
PC2 = 0x20
QC1 = 0x40
PC3 = 0x80
PC4 = 0x100
QC2 = 0x200
PC5 = 0x400
PC6 = 0x800
QC3 = 0x1000
PC7 = 0x2000
QCNOT0 = 0x4000
FIXED = 0x8000      # operand must be in fixed memory
ERASABLE = 0x10000  # operand must be in erasable memory
ENUMBER = 0x20000   # a plain number operand is a full pseudo-address


class OpType:
    BASIC = "basic"
    INTERPRETER = "interp"
    DOWNLINK = "downlink"
    PSEUDO = "pseudo"


@dataclass
class OpDef:
    name: str
    optype: str
    parser: str | None = None      # name of the Assembler method
    alias_op: str = ""
    alias_operand: str = ""
    adder: int = 0
    xmask: int = 0
    adder2: int = 0
    xmask2: int = 0
    pinch_hit: bool = False        # may stand in for an interpretive operand
    opcode: int = 0                # for "general" instructions
    flags: int = 0


def _general(name, opcode, flags, pinch=False):
    return OpDef(name, OpType.BASIC, "parse_general", opcode=opcode, flags=flags, pinch_hit=pinch)


def _pseudo(name, parser, pinch=False, **kw):
    return OpDef(name, OpType.PSEUDO, parser, pinch_hit=pinch, **kw)


def _alias(name, op, operand, optype=OpType.BASIC):
    return OpDef(name, optype, None, alias_op=op, alias_operand=operand)


OPS: dict[str, OpDef] = {}


def _add(d: OpDef):
    OPS[d.name] = d


for _d in [
    OpDef("-1DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0, xmask=0o77777),
    OpDef("-2CADR", OpType.PSEUDO, "parse_2cadr", adder=0, xmask=0o77777, adder2=0, xmask2=0o77777),
    OpDef("-2DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o04000, xmask=0o77777),
    OpDef("-3DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o10000, xmask=0o77777),
    OpDef("-4DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o14000, xmask=0o77777),
    OpDef("-5DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o20000, xmask=0o77777),
    OpDef("-6DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o24000, xmask=0o77777),
    OpDef("-CCS", OpType.BASIC, "parse_general", opcode=0o10000, flags=QC0 | ENUMBER, xmask=0o77777),
    OpDef("-DNCHAN", OpType.DOWNLINK, "parse_general", opcode=0o34000, flags=PC0 | ENUMBER, xmask=0o77777),
    OpDef("-DNPTR", OpType.DOWNLINK, "parse_genadr", adder=0o30000, xmask=0o77777),
    OpDef("-GENADR", OpType.PSEUDO, "parse_genadr", adder=0, xmask=0o77777),
    _pseudo("=", "parse_equals"),
    _pseudo("=ECADR", "parse_equals_ecadr"),
    _pseudo("=MINUS", "parse_eq_minus"),
    OpDef("1DNADR", OpType.DOWNLINK, "parse_ecadr"),
    _pseudo("2BCADR", "parse_2cadr"),
    _pseudo("2CADR", "parse_2cadr"),
    _pseudo("2DEC", "parse_2dec"),
    _pseudo("2DEC*", "parse_2dec"),
    OpDef("2DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o04000),
    _pseudo("2FCADR", "parse_2fcadr"),
    _pseudo("2OCT", "parse_2oct"),
    OpDef("3DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o10000),
    OpDef("4DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o14000),
    OpDef("5DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o20000),
    OpDef("6DNADR", OpType.DOWNLINK, "parse_ecadr", adder=0o24000),
    _general("AD", 0o60000, ENUMBER),
    _pseudo("ADRES", "parse_genadr"),
    _general("ADS", 0o20000, QC3),
    _general("AUG", 0o20000, EXTENDED | QC2),
    _pseudo("BANK", "parse_bank"),
    _pseudo("BLOCK", "parse_block"),
    _pseudo("BBCON", "parse_bbcon"),
    _pseudo("BBCON*", "parse_bbcon_star"),
    _pseudo("BNKSUM", None),
    _general("BZF", 0o10000, EXTENDED | QCNOT0),
    _general("BZMF", 0o60000, EXTENDED | QCNOT0),
    _general("CA", 0o30000, ENUMBER),
    _general("CAE", 0o30000, ERASABLE | ENUMBER),
    _general("CAF", 0o30000, FIXED | ENUMBER),
    _pseudo("CADR", "parse_cadr", pinch=True),
    _general("CCS", 0o10000, QC0 | ENUMBER),
    _pseudo("CHECK=", "parse_check_equals"),
    _alias("COM", "CS", "A"),
    _pseudo("COUNT", None),
    _pseudo("COUNT*", None),
    _general("CS", 0o40000, ENUMBER),
    _general("DAS", 0o20000, QC0 | KPLUS1),
    _general("DCA", 0o30000, EXTENDED | KPLUS1 | ENUMBER),
    _alias("DCOM", "DCS", "A"),
    _general("DCS", 0o40000, EXTENDED | KPLUS1 | ENUMBER),
    _alias("DDOUBL", "DAS", "A"),
    _pseudo("DEC", "parse_dec", pinch=True),
    _pseudo("DEC*", "parse_dec"),
    _general("DIM", 0o20000, EXTENDED | QC3),
    OpDef("DNCHAN", OpType.DOWNLINK, "parse_general", opcode=0o34000, flags=PC0 | ENUMBER),
    OpDef("DNPTR", OpType.DOWNLINK, "parse_genadr", adder=0o30000),
    _alias("DOUBLE", "AD", "A"),
    _alias("DTCB", "DXCH", "Z"),
    _alias("DTCF", "DXCH", "$4"),
    _general("DV", 0o10000, EXTENDED | QC0),
    _general("DXCH", 0o50000, QC1 | KPLUS1 | ENUMBER),
    _pseudo("EBANK=", "parse_ebank_equals"),
    _pseudo("ECADR", "parse_ecadr", pinch=True),
    _general("EDRUPT", 0o00000, EXTENDED | PC7),
    _pseudo("EQUALS", "parse_equals"),
    _pseudo("ERASE", "parse_erase"),
    _alias("EXTEND", "TC", "$6"),
    _pseudo("FCADR", "parse_cadr", pinch=True),
    _pseudo("GENADR", "parse_genadr"),
    _general("INCR", 0o20000, QC2),
    OpDef("INDEX", OpType.BASIC, "parse_index"),
    _alias("INHINT", "TC", "$4"),
    _general("LXCH", 0o20000, QC1 | ENUMBER),
    _general("MASK", 0o70000, 0),
    _general("MSK", 0o70000, 0),
    _pseudo("MEMORY", None),
    _pseudo("MM", "parse_dec"),
    _general("MP", 0o70000, EXTENDED),
    _general("MSU", 0o20000, EXTENDED | QC0 | ENUMBER),
    OpDef("NDX", OpType.BASIC, "parse_index"),
    _pseudo("NV", "parse_vn", pinch=True),
    _pseudo("OCT", "parse_oct", pinch=True),
    _pseudo("OCTAL", "parse_oct", pinch=True),
    _alias("OVSK", "TS", "A"),
    _general("QXCH", 0o20000, EXTENDED | QC1 | ENUMBER),
    _general("RAND", 0o00000, EXTENDED | PC2 | ENUMBER),
    _general("READ", 0o00000, EXTENDED | PC0 | ENUMBER),
    _alias("RELINT", "TC", "$3"),
    _pseudo("REMADR", "parse_genadr"),
    _alias("RESUME", "INDEX", "$17"),
    _alias("RETURN", "TC", "Q"),
    _general("ROR", 0o00000, EXTENDED | PC4 | ENUMBER),
    _general("RXOR", 0o00000, EXTENDED | PC6 | ENUMBER),
    _pseudo("SBANK=", "parse_sbank_equals"),
    _pseudo("SECSIZ", "parse_secsiz"),
    _pseudo("SETLOC", "parse_setloc"),
    _alias("SQUARE", "MP", "A"),
    OpDef("STCALL", OpType.INTERPRETER, "parse_stcall"),
    OpDef("STODL", OpType.INTERPRETER, "parse_stodl"),
    OpDef("STODL*", OpType.INTERPRETER, "parse_stodl", adder=0o4000),
    OpDef("STORE", OpType.INTERPRETER, "parse_store"),
    OpDef("STOVL", OpType.INTERPRETER, "parse_stovl"),
    OpDef("STOVL*", OpType.INTERPRETER, "parse_stovl", adder=0o4000),
    _general("SU", 0o60000, EXTENDED | QC0 | ENUMBER),
    _pseudo("SUBRO", None),
    _general("TC", 0o00000, ENUMBER),
    _general("TCR", 0o00000, ENUMBER),
    _alias("TCAA", "TS", "Z"),
    OpDef("TCF", OpType.BASIC, "parse_tcf"),
    _general("TS", 0o50000, QC2 | ENUMBER),
    _pseudo("VN", "parse_vn", pinch=True),
    _general("WAND", 0o00000, EXTENDED | PC3 | ENUMBER),
    _general("WOR", 0o00000, EXTENDED | PC5 | ENUMBER),
    _general("WRITE", 0o00000, EXTENDED | PC1 | ENUMBER),
    _general("XCH", 0o50000, QC3 | ENUMBER),
    _alias("XLQ", "TC", "L"),
    _alias("XXALQ", "TC", "A"),
    _alias("ZL", "LXCH", "$7"),
    _alias("ZQ", "QXCH", "$7"),
]:
    _add(_d)


@dataclass
class InterpOp:
    name: str
    code: int
    num_operands: int = 0
    switch: int = 0          # 0 normal, 1 switch instruction, 2 shift instruction
    nnnn: int = 0            # extra bits folded into the first operand
    arg_types: tuple = (0, 0)   # (increment-first-operand?, ...)


_I = InterpOp
INTERP: dict[str, InterpOp] = {}
for _o in [
    _I("ABS", 0o130), _I("ABVAL", 0o130), _I("ARCCOS", 0o050), _I("ACOS", 0o050),
    _I("ARCSIN", 0o040), _I("ASIN", 0o040),
    _I("AXC,1", 0o016, 1), _I("AXC,2", 0o012, 1), _I("AXT,1", 0o006, 1), _I("AXT,2", 0o002, 1),
    _I("BDDV", 0o111, 1, 0, 0, (1, 0)), _I("BDDV*", 0o113, 1, 0, 0, (1, 0)),
    _I("BDSU", 0o155, 1, 0, 0, (1, 0)), _I("BDSU*", 0o157, 1, 0, 0, (1, 0)),
    _I("BHIZ", 0o146, 1), _I("BMN", 0o136, 1),
    _I("BOFCLR", 0o162, 2, 1, 0o241), _I("BOF", 0o162, 2, 1, 0o341), _I("BOFF", 0o162, 2, 1, 0o341),
    _I("BOFINV", 0o162, 2, 1, 0o141), _I("BOFSET", 0o162, 2, 1, 0o041), _I("BON", 0o162, 2, 1, 0o301),
    _I("BONCLR", 0o162, 2, 1, 0o201), _I("BONINV", 0o162, 2, 1, 0o101), _I("BONSET", 0o162, 2, 1, 0o001),
    _I("BOV", 0o176, 1), _I("BOVB", 0o172, 1), _I("BPL", 0o132, 1),
    _I("BVSU", 0o131, 1, 0, 0, (1, 0)), _I("BVSU*", 0o133, 1, 0, 0, (1, 0)),
    _I("BZE", 0o122, 1), _I("CALL", 0o152, 1), _I("CALRB", 0o152, 1),
    _I("CCALL", 0o065, 2, 0, 0, (1, 0)), _I("CCALL*", 0o067, 2, 0, 0, (1, 0)),
    _I("CGOTO", 0o021, 2, 0, 0, (1, 0)), _I("CGOTO*", 0o023, 2, 0, 0, (1, 0)),
    _I("CLEAR", 0o162, 1, 1, 0o261), _I("CLR", 0o162, 1, 1, 0o261), _I("CLRGO", 0o162, 2, 1, 0o221),
    _I("COS", 0o030), _I("COSINE", 0o030),
    _I("DAD", 0o161, 1, 0, 0, (1, 0)), _I("DAD*", 0o163, 1, 0, 0, (1, 0)),
    _I("DCOMP", 0o100),
    _I("DDV", 0o105, 1, 0, 0, (1, 0)), _I("DDV*", 0o107, 1, 0, 0, (1, 0)),
    _I("DLOAD", 0o031, 1, 0, 0, (1, 0)), _I("DLOAD*", 0o033, 1, 0, 0, (1, 0)),
    _I("DMP", 0o171, 1, 0, 0, (1, 0)), _I("DMP*", 0o173, 1, 0, 0, (1, 0)),
    _I("DMPR", 0o101, 1, 0, 0, (1, 0)), _I("DMPR*", 0o103, 1, 0, 0, (1, 0)),
    _I("DOT", 0o135, 1, 0, 0, (1, 0)), _I("DOT*", 0o137, 1, 0, 0, (1, 0)),
    _I("DSQ", 0o060),
    _I("DSU", 0o151, 1, 0, 0, (1, 0)), _I("DSU*", 0o153, 1, 0, 0, (1, 0)),
    _I("EXIT", 0o000), _I("GOTO", 0o126, 1), _I("INCR,1", 0o066, 1), _I("INCR,2", 0o062, 1),
    _I("INVERT", 0o162, 1, 1, 0o161), _I("INVGO", 0o162, 2, 1, 0o121),
    _I("ITA", 0o156, 1), _I("ITCQ", 0o160),
    _I("LXA,1", 0o026, 1), _I("LXA,2", 0o022, 1), _I("LXC,1", 0o036, 1), _I("LXC,2", 0o032, 1),
    _I("MXV", 0o055, 1, 0, 0, (1, 0)), _I("MXV*", 0o057, 1, 0, 0, (1, 0)),
    _I("NORM", 0o075, 1, 0, 0, (1, 0)), _I("NORM*", 0o077, 1, 0, 0, (1, 0)),
    _I("PDDL", 0o051, 1, 0, 0, (1, 0)), _I("PDDL*", 0o053, 1, 0, 0, (1, 0)),
    _I("PDVL", 0o061, 1, 0, 0, (1, 0)), _I("PDVL*", 0o063, 1, 0, 0, (1, 0)),
    _I("PUSH", 0o170), _I("ROUND", 0o070), _I("RTB", 0o142, 1), _I("RVQ", 0o160),
    _I("SET", 0o162, 1, 1, 0o061), _I("SETGO", 0o162, 2, 1, 0o021),
    _I("SETPD", 0o175, 1, 0, 0, (1, 0)),
    _I("SIGN", 0o011, 1, 0, 0, (1, 0)), _I("SIGN*", 0o013, 1, 0, 0, (1, 0)),
    _I("SIN", 0o020), _I("SINE", 0o020),
    _I("SL", 0o115, 1, 2, 0o20202, (1, 0)), _I("SL*", 0o117, 1, 2, 0o20202, (1, 0)),
    _I("SLOAD", 0o041, 1, 0, 0, (1, 0)), _I("SLOAD*", 0o043, 1, 0, 0, (1, 0)),
    _I("SL1", 0o024, 0, 0, 0, (1, 0)), _I("SL1R", 0o004, 0, 0, 0, (1, 0)),
    _I("SL2", 0o064, 0, 0, 0, (1, 0)), _I("SL2R", 0o044, 0, 0, 0, (1, 0)),
    _I("SL3", 0o124, 0, 0, 0, (1, 0)), _I("SL3R", 0o104, 0, 0, 0, (1, 0)),
    _I("SL4", 0o164, 0, 0, 0, (1, 0)), _I("SL4R", 0o144, 0, 0, 0, (1, 0)),
    _I("SLR", 0o115, 1, 2, 0o21202, (1, 0)), _I("SLR*", 0o117, 1, 2, 0o21202, (1, 0)),
    _I("SQRT", 0o010),
    _I("SR", 0o115, 1, 2, 0o20602, (1, 0)), _I("SR*", 0o117, 1, 2, 0o20602, (1, 0)),
    _I("SR1", 0o034, 0, 0, 0, (1, 0)), _I("SR1R", 0o014, 0, 0, 0, (1, 0)),
    _I("SR2", 0o074, 0, 0, 0, (1, 0)), _I("SR2R", 0o054, 0, 0, 0, (1, 0)),
    _I("SR3", 0o134, 0, 0, 0, (1, 0)), _I("SR3R", 0o114, 0, 0, 0, (1, 0)),
    _I("SR4", 0o174, 0, 0, 0, (1, 0)), _I("SR4R", 0o154, 0, 0, 0, (1, 0)),
    _I("SRR", 0o115, 1, 2, 0o21602, (1, 0)), _I("SRR*", 0o117, 1, 2, 0o21602, (1, 0)),
    _I("SSP", 0o045, 2, 0, 0, (1, 0)), _I("SSP*", 0o047, 1, 0, 0, (1, 0)),
    _I("STADR", 0o150), _I("STQ", 0o156, 1),
    _I("SXA,1", 0o046, 1), _I("SXA,2", 0o042, 1),
    _I("TAD", 0o005, 1, 0, 0, (1, 0)), _I("TAD*", 0o007, 1, 0, 0, (1, 0)),
    _I("TIX,1", 0o076, 1), _I("TIX,2", 0o072, 1),
    _I("TLOAD", 0o025, 1, 0, 0, (1, 0)), _I("TLOAD*", 0o027, 1, 0, 0, (1, 0)),
    _I("UNIT", 0o120),
    _I("V/SC", 0o035, 1, 0, 0, (1, 0)), _I("V/SC*", 0o037, 1, 0, 0, (1, 0)),
    _I("VAD", 0o121, 1, 0, 0, (1, 0)), _I("VAD*", 0o123, 1, 0, 0, (1, 0)),
    _I("VCOMP", 0o100), _I("VDEF", 0o110),
    _I("VLOAD", 0o001, 1, 0, 0, (1, 0)), _I("VLOAD*", 0o003, 1, 0, 0, (1, 0)),
    _I("VPROJ", 0o145, 1, 0, 0, (1, 0)), _I("VPROJ*", 0o147, 1, 0, 0, (1, 0)),
    _I("VSL", 0o115, 1, 2, 0o20202, (1, 0)), _I("VSL*", 0o117, 1, 2, 0o20202, (1, 0)),
    _I("VSL1", 0o004, 0, 0, 0, (1, 0)), _I("VSL2", 0o024, 0, 0, 0, (1, 0)),
    _I("VSL3", 0o044, 0, 0, 0, (1, 0)), _I("VSL4", 0o064, 0, 0, 0, (1, 0)),
    _I("VSL5", 0o104, 0, 0, 0, (1, 0)), _I("VSL6", 0o124, 0, 0, 0, (1, 0)),
    _I("VSL7", 0o144, 0, 0, 0, (1, 0)), _I("VSL8", 0o164, 0, 0, 0, (1, 0)),
    _I("VSQ", 0o140),
    _I("VSR", 0o115, 1, 2, 0o20602, (1, 0)), _I("VSR*", 0o117, 1, 2, 0o20602, (1, 0)),
    _I("VSR1", 0o014, 0, 0, 0, (1, 0)), _I("VSR2", 0o034, 0, 0, 0, (1, 0)),
    _I("VSR3", 0o054, 0, 0, 0, (1, 0)), _I("VSR4", 0o074, 0, 0, 0, (1, 0)),
    _I("VSR5", 0o114, 0, 0, 0, (1, 0)), _I("VSR6", 0o134, 0, 0, 0, (1, 0)),
    _I("VSR7", 0o154, 0, 0, 0, (1, 0)), _I("VSR8", 0o174, 0, 0, 0, (1, 0)),
    _I("VSU", 0o125, 1, 0, 0, (1, 0)), _I("VSU*", 0o127, 1, 0, 0, (1, 0)),
    _I("VXM", 0o071, 1, 0, 0, (1, 0)), _I("VXM*", 0o073, 1, 0, 0, (1, 0)),
    _I("VXSC", 0o015, 1, 0, 0, (1, 0)), _I("VXSC*", 0o017, 1, 0, 0, (1, 0)),
    _I("VXV", 0o141, 1, 0, 0, (1, 0)), _I("VXV*", 0o143, 1, 0, 0, (1, 0)),
    _I("XAD,1", 0o106, 1), _I("XAD,2", 0o102, 1),
    _I("XCHX,1", 0o056, 1), _I("XCHX,2", 0o052, 1),
    _I("XSU,1", 0o116, 1), _I("XSU,2", 0o112, 1),
]:
    INTERP[_o.name] = _o


def is_interpretive(name: str) -> bool:
    if name in INTERP:
        return True
    d = OPS.get(name)
    return bool(d and d.optype == OpType.INTERPRETER)


# Mnemonics that the emulator's disassembler should show for basic opcodes.
BASIC_MNEMONICS = {
    0o0: "TC", 0o10: "CCS", 0o12: "TCF", 0o20: "DAS", 0o22: "LXCH", 0o24: "INCR",
    0o26: "ADS", 0o30: "CA", 0o40: "CS", 0o50: "INDEX", 0o52: "DXCH", 0o54: "TS",
    0o56: "XCH", 0o60: "AD", 0o70: "MASK",
}
EXTENDED_MNEMONICS = {
    0o100: "READ", 0o101: "WRITE", 0o102: "RAND", 0o103: "WAND", 0o104: "ROR",
    0o105: "WOR", 0o106: "RXOR", 0o107: "EDRUPT", 0o110: "DV", 0o112: "BZF",
    0o120: "MSU", 0o122: "QXCH", 0o124: "AUG", 0o126: "DIM", 0o130: "DCA",
    0o140: "DCS", 0o150: "INDEX", 0o160: "SU", 0o162: "BZMF", 0o170: "MP",
}
