#!/usr/bin/env python3
"""Launcher: checks the virtual environment, installs what is missing, starts the simulation or the computer.

Works on Windows, Linux and macOS with any Python 3.10 or newer; needs nothing
outside the standard library.  ``start.sh`` and ``start.bat`` are thin
wrappers that find a Python interpreter and run this file.

Usage:  python start.py <command> [options]        (see ``python start.py help``)
"""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV = ROOT / ".venv"
MIN_PYTHON = (3, 10)
WINDOWS = platform.system() == "Windows"

# package name on PyPI -> module to import for the check
PACKAGES = {"numpy": "numpy", "pytest": "pytest"}
if WINDOWS:
    PACKAGES["windows-curses"] = "curses"   # the interactive test UI needs curses

COMMANDS = {
    # name:      (argv after the venv python, one-line help)
    "land":    (["-m", "agc.sim", "land"],    "fly the powered descent to touchdown (about 13 minutes)"),
    "view":    (["-m", "agc.sim", "view"],    "3D viewer in the browser, replays landing.csv [or another CSV]"),
    "report":  (["-m", "agc.sim", "report"],  "summarise a recorded flight with ASCII plots"),
    "run":     (["-m", "agc", "run"],         "boot the computer headless, press DSKY keys, print the DSKY"),
    "tui":     (["-m", "agc", "tui"],         "interactive DSKY test UI in the terminal"),
    "modules": (["-m", "agc", "modules"],     "list the converted modules and their routines"),
    "convert": (["-m", "agc", "convert"],     "regenerate the Python modules from the AGC listings"),
    "test":    (["-m", "pytest"],             "run the test suite"),
    "python":  ([],                           "run the virtual environment's Python (REPL or a script)"),
    "setup":   (None,                         "only create / repair the virtual environment"),
}

HELP = f"""\
Apollo 11 guidance computer in Python: launcher

usage:  {{launcher}} <command> [options]

The launcher checks the virtual environment in {VENV.name}/, creates it if it
is missing, installs missing packages ({", ".join(PACKAGES)}) and then runs
the command with the virtual environment's Python.  Options after the
command are passed through unchanged; use '<command> --help' to see them.

commands:
"""
HELP += "\n".join(f"  {name:9} {text}" for name, (_, text) in COMMANDS.items())
HELP += """

examples:
  {launcher} land                       fly the landing, telemetry to landing.csv
  {launcher} land --view --realtime     fly it in real time and watch in the browser
  {launcher} view                       replay the recorded flight in the browser
  {launcher} run --keys V16N36E         boot Luminary 099 and show the mission clock
  {launcher} tui                        interactive DSKY
  {launcher} test                       run the tests

environment:
  PYTHON   interpreter used to create the virtual environment (default: the
           one running this script, or python3 / py -3 found on the PATH)
  Delete the .venv directory to start over from scratch.
"""


def say(msg: str) -> None:
    print(f"[start] {msg}", flush=True)


def fail(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    print(f"[start] error: {msg}", file=sys.stderr, flush=True)
    sys.exit(1)


def venv_python() -> Path:
    if WINDOWS:
        return VENV / "Scripts" / "python.exe"
    return VENV / "bin" / "python"


def python_version(exe: Path | str) -> tuple[int, int] | None:
    """(major, minor) of an interpreter, or None if it does not run."""
    try:
        out = subprocess.run([str(exe), "-c", "import sys; print(sys.version_info[0], sys.version_info[1])"],
                             capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    try:
        major, minor = out.stdout.split()
        return int(major), int(minor)
    except ValueError:
        return None


def base_interpreter() -> Path:
    """The interpreter used to create the virtual environment."""
    candidates: list[str] = []
    if os.environ.get("PYTHON"):
        candidates.append(os.environ["PYTHON"])
    candidates.append(sys.executable)
    for name in ("python3.13", "python3.12", "python3.11", "python3.10", "python3", "python"):
        found = shutil.which(name)
        if found:
            candidates.append(found)
    for exe in candidates:
        ver = python_version(exe)
        if ver and ver >= MIN_PYTHON:
            return Path(exe)
    fail(f"no Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or newer found; install one from https://www.python.org "
         "or point the PYTHON environment variable at it")


def ensure_venv() -> Path:
    """Create the virtual environment if it is missing or broken, return its Python."""
    exe = venv_python()
    ver = python_version(exe) if exe.exists() else None
    if ver and ver >= MIN_PYTHON:
        return exe
    if VENV.exists():
        if ver is None:
            say(f"{VENV.name}/ exists but its Python does not run - recreating it")
        else:
            say(f"{VENV.name}/ has Python {ver[0]}.{ver[1]}, need {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ - recreating it")
        shutil.rmtree(VENV)
    base = base_interpreter()
    bver = python_version(base)
    say(f"creating {VENV.name}/ with {base} (Python {bver[0]}.{bver[1]})")
    if Path(base).resolve() == Path(sys.executable).resolve():
        venv.EnvBuilder(with_pip=True, clear=True).create(VENV)
    else:
        subprocess.run([str(base), "-m", "venv", "--clear", str(VENV)], check=True)
    if not exe.exists():
        fail(f"virtual environment created but {exe} is missing")
    return exe


def missing_packages(exe: Path) -> list[str]:
    probe = "import importlib,sys\n" + "".join(
        f"try:\n    importlib.import_module({mod!r})\nexcept Exception:\n    print({pkg!r})\n"
        for pkg, mod in PACKAGES.items())
    out = subprocess.run([str(exe), "-I", "-c", probe], capture_output=True, text=True, cwd=ROOT)
    if out.returncode != 0:
        fail(f"cannot inspect {exe}:\n{out.stderr}")
    return out.stdout.split()


def ensure_packages(exe: Path) -> None:
    missing = missing_packages(exe)
    if not missing:
        return
    say("installing " + ", ".join(missing))
    pip = [str(exe), "-m", "pip", "install", "--disable-pip-version-check"]
    res = subprocess.run(pip + missing, cwd=ROOT)
    if res.returncode != 0:
        fail("pip install failed (see above); check the internet connection or install manually with\n"
             f"    {exe} -m pip install {' '.join(missing)}")
    still = missing_packages(exe)
    if still:
        fail("installed, but still cannot import: " + ", ".join(still))


def launcher_name() -> str:
    return "start.bat" if WINDOWS else "./start.sh"


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("help", "-h", "--help", "/?"):
        print(HELP.replace("{launcher}", launcher_name()))
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd not in COMMANDS:
        print(f"[start] unknown command '{cmd}'\n", file=sys.stderr)
        print(HELP.replace("{launcher}", launcher_name()), file=sys.stderr)
        return 2

    exe = ensure_venv()
    ensure_packages(exe)
    if cmd == "setup":
        ver = python_version(exe)
        say(f"ready: {exe} (Python {ver[0]}.{ver[1]}), packages: {', '.join(PACKAGES)}")
        return 0

    prefix, _ = COMMANDS[cmd]
    command = [str(exe)] + prefix + rest
    os.chdir(ROOT)
    if WINDOWS:
        # subprocess keeps Ctrl+C handling sane on Windows; exec is not available there
        return subprocess.call(command)
    os.execv(command[0], command)
    return 0  # not reached


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        sys.exit(130)
