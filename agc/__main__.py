"""Command line entry point: ``python -m agc <command>``.

Commands
--------
convert   assemble the original source, verify it and generate the Python modules
run       boot a program headless, optionally press DSKY keys, print the DSKY
tui       interactive curses test UI (DSKY, registers, module browser)
modules   list the converted modules and their routines
"""

from __future__ import annotations

import argparse
import sys

from .program import available_programs, load_program


def cmd_run(args) -> int:
    from .cpu import AGC, CYCLES_PER_SECOND
    from .dsky import DSKY

    prog = load_program(args.program)
    cpu = AGC(prog.fixed, check_alarms=not args.no_alarms)
    dsky = DSKY(cpu)
    cpu.run(int(args.boot * CYCLES_PER_SECOND))
    for key in args.keys:
        for k in _split_keys(key):
            dsky.press(k)
            cpu.run(int(args.key_delay * CYCLES_PER_SECOND))
            dsky.release_pro()
    cpu.run(int(args.after * CYCLES_PER_SECOND))
    print(f"{prog.title}")
    print(f"AGC time {cpu.seconds:.2f} s, {cpu.instructions} instructions, {len(cpu.alarm_log)} hardware alarms")
    for line in dsky.render():
        print("  " + line)
    loc = cpu.current_location()
    where = prog.nearest_label(*loc) if loc else "erasable"
    print(f"Z = {cpu.z:04o} ({where})   " + "  ".join(f"{k}={v:05o}" for k, v in cpu.registers().items() if k in ("A", "L", "Q", "EB", "FB")))
    if cpu.alarm_log:
        print("hardware alarms:", cpu.alarm_log[:10])
    for name in args.watch:
        sym = prog.symbol(name)
        if sym is None or sym.erasable_address() is None:
            print(f"{name}: not an erasable symbol")
        else:
            print(f"{name} = {cpu.erasable_flat(sym.erasable_address()):05o}")
    return 0


def _split_keys(text: str) -> list[str]:
    """"V16N36E" -> ["V","1","6","N","3","6","E"]; "PRO" stays one key."""
    t = text.strip().upper()
    if t in ("PRO", "RSET", "ENTR", "CLR", "KEY REL", "KEYREL", "VERB", "NOUN", "RESET", "CLEAR"):
        return [t]
    return list(t)


def cmd_modules(args) -> int:
    prog = load_program(args.program)
    print(f"{prog.title}: {len(prog.modules)} modules, {len(prog.symbols)} symbols")
    for m in prog.modules:
        if args.filter and args.filter.upper() not in m.name.upper():
            continue
        routines = m.routines()
        print(f"{m.name:45} {len(m.words):5d} words  {len(routines):4d} routines  pages {m.pages}")
        if args.routines:
            names = [f"{r.label}@{r.address}" for r in routines]
            for i in range(0, len(names), 6):
                print("      " + "  ".join(names[i:i + 6]))
    return 0


def cmd_tui(args) -> int:
    from .tester.tui import main as tui_main
    return tui_main(args.program)


def cmd_convert(args) -> int:
    from .asm.__main__ import main as asm_main
    argv = ["convert"] + args.rest
    return asm_main(argv)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="agc", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    programs = available_programs() or ["luminary099", "comanche055"]

    r = sub.add_parser("run", help="boot headless and show the DSKY")
    r.add_argument("program", nargs="?", default="luminary099", choices=programs)
    r.add_argument("--boot", type=float, default=3.0, help="AGC seconds to run before pressing keys")
    r.add_argument("--keys", nargs="*", default=[], help='key sequences, e.g. V35E V16N36E PRO')
    r.add_argument("--key-delay", type=float, default=0.3, help="AGC seconds between key presses")
    r.add_argument("--after", type=float, default=1.0, help="AGC seconds to run after the last key")
    r.add_argument("--watch", nargs="*", default=[], help="erasable symbols to print")
    r.add_argument("--no-alarms", action="store_true", help="do not GOJAM on hardware alarms")
    r.set_defaults(func=cmd_run)

    m = sub.add_parser("modules", help="list converted modules")
    m.add_argument("program", nargs="?", default="luminary099", choices=programs)
    m.add_argument("--routines", action="store_true")
    m.add_argument("--filter", default="")
    m.set_defaults(func=cmd_modules)

    t = sub.add_parser("tui", help="interactive test UI")
    t.add_argument("program", nargs="?", default="luminary099", choices=programs)
    t.set_defaults(func=cmd_tui)

    c = sub.add_parser("convert", help="run the agc2py converter (see python -m agc.asm convert --help)")
    c.add_argument("rest", nargs=argparse.REMAINDER)
    c.set_defaults(func=cmd_convert)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
