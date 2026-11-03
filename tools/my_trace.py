"""Dump a per-MCT trace of the Python emulator in the same format as ref_trace.c."""

import sys

sys.path.insert(0, __file__.rsplit("/tools/", 1)[0])

from agc.program import load_program  # noqa: E402
from agc.cpu import AGC  # noqa: E402


def main():
    prog = sys.argv[1]
    n = int(sys.argv[2])
    p = load_program(prog)
    cpu = AGC(p.fixed)
    e = cpu.e
    out = sys.stdout
    for _ in range(n):
        cpu.step()
        out.write(f"{cpu.cycles} {e[5] & 0o7777:04o} {e[0] & 0o177777:06o} {e[1] & 0o177777:06o} "
                  f"{e[2] & 0o177777:06o} {e[3] & 0o77777:05o} {e[4] & 0o77777:05o} {e[6] & 0o77777:05o} "
                  f"{int(cpu.in_isr)} {int(cpu.extracode)}\n")


if __name__ == "__main__":
    main()
