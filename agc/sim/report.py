"""Text report of a landing telemetry CSV: ``python -m agc.sim report landing.csv``."""

from __future__ import annotations

import csv
import sys


def fmt_get(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    return f"{h:03d}:{m:02d}:{seconds % 60:05.2f}"


def ascii_plot(xs, ys, width=70, height=16, label=""):
    if not xs:
        return []
    lo, hi = min(ys), max(ys)
    if hi == lo:
        hi = lo + 1
    grid = [[" "] * width for _ in range(height)]
    x0, x1 = xs[0], xs[-1]
    for x, y in zip(xs, ys):
        c = int((x - x0) / (x1 - x0 or 1) * (width - 1))
        r = int((hi - y) / (hi - lo) * (height - 1))
        grid[r][c] = "*"
    lines = [f"{label}  (max {hi:.0f}, min {lo:.0f})"]
    for r, row in enumerate(grid):
        val = hi - (hi - lo) * r / (height - 1)
        lines.append(f"{val:9.0f} |" + "".join(row))
    lines.append(" " * 10 + "+" + "-" * width)
    lines.append(" " * 11 + f"GET {fmt_get(x0)}" + " " * (width - 32) + f"GET {fmt_get(x1)}")
    return lines


def main(argv=None) -> int:
    path = (argv or sys.argv[1:] or ["landing.csv"])[0]
    rows = list(csv.DictReader(open(path)))
    if not rows:
        print("empty telemetry")
        return 1
    t = [float(r["get"]) for r in rows]
    alt = [float(r["alt_m"]) / 0.3048 for r in rows]
    hdot = [float(r["hdot_mps"]) / 0.3048 for r in rows]
    vh = [float(r["vhor_mps"]) / 0.3048 for r in rows]
    thr = [float(r["thrust_n"]) / 43900.0 * 100 for r in rows]
    burn = [i for i, x in enumerate(thr) if x > 1.0]
    print(f"{len(rows)} samples, GET {fmt_get(t[0])} .. {fmt_get(t[-1])}")
    if burn:
        i0, i1 = burn[0], burn[-1]
        print(f"engine on  GET {fmt_get(t[i0])}  alt {alt[i0]:.0f} ft  speed {vh[i0]:.0f} ft/s")
        print(f"engine off GET {fmt_get(t[i1])}  alt {alt[i1]:.0f} ft  hdot {hdot[i1]:+.1f} ft/s  vh {vh[i1]:.1f} ft/s  "
              f"burn {t[i1] - t[i0]:.0f} s, mass {float(rows[i0]['mass_kg']):.0f} -> {float(rows[i1]['mass_kg']):.0f} kg")
    progs = []
    for r in rows:
        if not progs or progs[-1][1] != r["prog"]:
            progs.append((float(r["get"]), r["prog"]))
    print("program changes: " + ", ".join(f"P{p} at {fmt_get(g)}" for g, p in progs if p.strip()))
    alarms = sorted({r["alarms"] for r in rows if r["alarms"]})
    print("alarm codes seen:", alarms)
    print()
    for line in ascii_plot(t, alt, label="altitude [ft]"):
        print(line)
    print()
    for line in ascii_plot(t, vh, label="horizontal speed [ft/s]"):
        print(line)
    print()
    for line in ascii_plot(t, thr, label="DPS thrust [% of FTP]", height=8):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
