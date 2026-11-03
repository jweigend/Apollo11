"""Dump a per-MCT trace of the Python emulator in the same format as ref_trace.c.

Usage: my_trace.py luminary099 NCYCLES [CYCLE:CHANNEL:VALUE,...]  (octal, see ref_trace.c)
"""

import sys

sys.path.insert(0, __file__.rsplit("/tools/", 1)[0])

from agc.program import load_program  # noqa: E402
from agc.cpu import AGC  # noqa: E402


def parse_events(text: str) -> list[tuple[int, int, int]]:
    """'CYCLE:CHANNEL:VALUE,...' (cycle decimal, channel and value octal)."""
    out = []
    for item in text.split(","):
        if item:
            c, ch, v = item.split(":")
            out.append((int(c), int(ch, 8), int(v, 8)))
    return out


KEY_CODES = {"V": 0o21, "N": 0o37, "E": 0o34, "R": 0o22, "0": 0o20,
             **{str(d): d for d in range(1, 10)}}


def scenario() -> str:
    """The standard scenario of tools/diff_trace.sh as an event list."""
    events = [(3.0, 0o30, 0o37777 & ~(0o400 | 0o20000)),     # IMU operate + ISS turn-on request
              (96.0, 0o30, 0o37777 & ~0o400)]                 # request dropped after the 90 s delay
    for t0, keys in ((5.0, "V35E"), (10.0, "V16N36E"), (20.0, "V37E00E"), (110.0, "V37E00E"),
                     (116.0, "V05N09E"), (119.0, "R"), (121.0, "V16N65E")):
        for i, k in enumerate(keys):
            events.append((t0 + 0.25 * i, 0o15, KEY_CODES[k]))
    events.sort()
    return ",".join(f"{int(t * 85333)}:{ch:o}:{v:o}" for t, ch, v in events)


def main():
    if sys.argv[1:] == ["--scenario"]:
        print(scenario())
        return
    prog = sys.argv[1]
    n = int(sys.argv[2])
    p = load_program(prog)
    cpu = AGC(p.fixed)
    e = cpu.e
    out = sys.stdout
    events = parse_events(sys.argv[3]) if len(sys.argv) > 3 else []
    events.reverse()
    for _ in range(n):
        if events and cpu.cycles + 1 == events[-1][0]:
            _, chan, value = events.pop()
            if chan == 0o15:
                cpu.key_press(value)
            else:
                cpu.set_input_channel(chan, value)
        cpu.step()
        out.write(f"{cpu.cycles} {e[5] & 0o7777:04o} {e[0] & 0o177777:06o} {e[1] & 0o177777:06o} "
                  f"{e[2] & 0o177777:06o} {e[3] & 0o77777:05o} {e[4] & 0o77777:05o} {e[6] & 0o77777:05o} "
                  f"{int(cpu.in_isr)} {int(cpu.extracode)}\n")


if __name__ == "__main__":
    main()
