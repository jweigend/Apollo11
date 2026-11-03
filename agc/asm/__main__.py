"""agc2py command line: ``python -m agc.asm convert Luminary099``."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from .assembler import Assembler
from .binsource import compare, read_binsource
from .pygen import generate

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SRC = ROOT / "external" / "Apollo-11"
DEFAULT_REF = ROOT / "external" / "virtualagc"
DEFAULT_OUT = ROOT / "agc" / "programs"


def cmd_convert(args) -> int:
    rc = 0
    for prog in args.programs:
        src_dir = Path(args.source) / prog
        main = src_dir / "MAIN.agc"
        if not main.exists():
            print(f"{prog}: {main} not found", file=sys.stderr)
            return 2
        t0 = time.time()
        asm = Assembler(main, verbose=args.verbose)
        result = asm.assemble()
        dt = time.time() - t0
        used = sum(result.bank_counts)
        print(f"{prog}: assembled {used} words in {dt:.1f}s, "
              f"{len(result.symbols)} symbols, {result.fatals} fatal errors, {result.warnings} warnings")
        for f, lineno, needle, repl in asm.applied_fixups:
            print(f"   fixup applied: {f}:{lineno}: {needle!r} -> {repl!r}")
        for f, lineno, needle in asm.skipped_fixups:
            print(f"   fixup SKIPPED (text not found): {f}:{lineno}: {needle!r}")
        for inc, actual in asm.include_fixups.items():
            print(f"   include {inc} resolved to {actual}")
        for ln in result.lines:
            if ln.fatal:
                print(f"   FATAL {ln.file}:{ln.line}: {ln.error}")
                rc = 1
        ref = Path(args.reference) / prog / f"{prog}.binsource"
        if ref.exists() and not args.no_verify:
            diffs = compare(result.fixed, result.used, read_binsource(ref))
            if diffs:
                rc = 1
                print(f"   VERIFY: {len(diffs)} words differ from {ref.name}:")
                for bank, off, ours, theirs in diffs[:20]:
                    print(f"      bank {bank:02o} offset {off:04o}: ours {ours:05o} reference {theirs:05o}")
            else:
                print(f"   VERIFY: rope is identical to the reference listing {ref.name}")
        if not args.no_output:
            out_dir = Path(args.output) / prog.lower()
            rel = str(src_dir.relative_to(ROOT)) if src_dir.is_relative_to(ROOT) else str(src_dir)
            names = generate(result, prog, src_dir, out_dir, rel)
            print(f"   wrote {len(names)} Python modules to {out_dir.relative_to(ROOT) if out_dir.is_relative_to(ROOT) else out_dir}")
    return rc


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="agc2py", description="Convert AGC assembly source to Python modules.")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("convert", help="assemble, verify against the octal listing and generate Python")
    c.add_argument("programs", nargs="*", default=["Luminary099", "Comanche055"])
    c.add_argument("--source", default=str(DEFAULT_SRC), help="directory containing <Program>/MAIN.agc")
    c.add_argument("--reference", default=str(DEFAULT_REF), help="directory containing <Program>/<Program>.binsource")
    c.add_argument("--output", default=str(DEFAULT_OUT), help="package directory for generated modules")
    c.add_argument("--no-verify", action="store_true")
    c.add_argument("--no-output", action="store_true", help="only assemble and verify")
    c.add_argument("-v", "--verbose", action="store_true")
    c.set_defaults(func=cmd_convert)
    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
