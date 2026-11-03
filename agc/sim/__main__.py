"""Run the Apollo 11 landing: ``python -m agc.sim land``."""

from __future__ import annotations

import argparse
import sys

from .mission import LandingSimulation


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="agc.sim", description="Lunar landing simulation flown by Luminary 099")
    sub = p.add_subparsers(dest="cmd", required=True)
    land = sub.add_parser("land", help="fly the powered descent from before PDI to touchdown")
    land.add_argument("--until", type=float, default=None, help="stop after this many simulated seconds")
    land.add_argument("--dt", type=float, default=0.02, help="physics time step (s)")
    land.add_argument("--log", default="landing.csv", help="telemetry CSV output ('' to disable)")
    land.add_argument("--status-every", type=float, default=5.0, help="status line interval (simulated s)")
    land.add_argument("--realtime", action="store_true", help="pace the simulation to wall-clock time")
    land.add_argument("--quiet", action="store_true")
    land.add_argument("--no-lr", action="store_true", help="disable the landing radar model (inertial navigation only)")
    land.add_argument("--probe-cache", default="landing_probe.json",
                      help="cache file for the AGC-computed landing site / lunar pole ('' to disable)")
    land.add_argument("--view", action="store_true", help="open the 3D viewer in the browser while flying")
    land.add_argument("--port", type=int, default=8765, help="port for the 3D viewer")
    rep = sub.add_parser("report", help="summarise a telemetry CSV written by 'land'")
    rep.add_argument("csv", nargs="?", default="landing.csv")
    view = sub.add_parser("view", help="3D viewer in the browser (replays or follows a telemetry CSV)")
    view.add_argument("csv", nargs="?", default="landing.csv")
    view.add_argument("--port", type=int, default=8765)
    view.add_argument("--no-browser", action="store_true")
    args = p.parse_args(argv)
    if args.cmd == "report":
        from .report import main as report_main
        return report_main([args.csv])
    if args.cmd == "view":
        from .viewer import serve
        serve(args.csv, port=args.port, open_browser=not args.no_browser)
        return 0
    if args.view and args.log:
        from .viewer import serve
        serve(args.log, port=args.port, open_browser=True, block=False, live=True)

    sim = LandingSimulation(dt=args.dt, verbose=not args.quiet, log_path=args.log or None, realtime=args.realtime,
                            probe_cache=args.probe_cache or None, landing_radar=not args.no_lr)
    result = sim.run(until=args.until, status_every=args.status_every)
    if result:
        print("\nTOUCHDOWN")
        for k, v in result.items():
            print(f"  {k:18} {v}")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
