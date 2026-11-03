"""Differential test against the reference emulator yaAGC (skipped without gcc or the
Virtual AGC sources in external/virtualagc).  tools/diff_trace.sh runs the full scenario."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

YA = ROOT / "external" / "virtualagc" / "yaAGC"
SOURCES = ["agc_engine.c", "agc_engine_init.c", "agc_utilities.c", "rfopen.c", "Backtrace.c",
           "DecodeDigitalDownlink.c"]


@pytest.mark.skipif(shutil.which("gcc") is None or not (YA / "agc_engine.c").exists(),
                    reason="needs gcc and external/virtualagc (see README)")
def test_cpu_matches_yaagc_cycle_by_cycle(tmp_path):
    from agc.program import load_program
    from agc.rope import write_bin
    sys.path.insert(0, str(ROOT / "tools"))
    import my_trace

    ref = tmp_path / "ref_trace"
    subprocess.run(["gcc", "-O2", "-o", str(ref), str(ROOT / "tools" / "ref_trace.c"),
                    *[str(YA / f) for f in SOURCES], f"-I{YA}", "-lm"],
                   check=True, capture_output=True)
    rope = tmp_path / "Luminary099.bin"
    write_bin(load_program("luminary099").fixed, rope)
    # 7 s of AGC time: boot, fresh start, the V35E lamp test at 5 s (charges the warning
    # filter, which must show in channel 33) and the first T4RUPT passes after it.
    n = 600_000
    events = my_trace.scenario()
    ref_out = subprocess.run([str(ref), str(rope), str(n), events], check=True,
                             capture_output=True, text=True).stdout
    my_out = subprocess.run([sys.executable, str(ROOT / "tools" / "my_trace.py"), "luminary099", str(n), events],
                            check=True, capture_output=True, text=True, env={**os.environ, "PYTHONPATH": str(ROOT)}).stdout
    assert ref_out.count("\n") == n
    if ref_out != my_out:
        for i, (a, b) in enumerate(zip(ref_out.splitlines(), my_out.splitlines())):
            assert a == b, f"first difference at cycle {i + 1}: yaAGC {a!r}, cpu.py {b!r}"
        pytest.fail("traces differ in length")
