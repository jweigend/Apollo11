#!/bin/bash
# Differential test of agc/cpu.py against the reference emulator yaAGC.
#
# Builds tools/ref_trace.c around the Virtual AGC engine (external/virtualagc,
# see README), writes the assembled Luminary 099 rope, runs both emulators
# cycle by cycle through the same scenario and compares the traces
# (Z A L Q EB FB BB InIsr ExtraCode after every memory cycle).
#
# Scenario (126 s of AGC time, 10.75 million cycles, about 90 s wall clock):
#   3 s    IMU operate + ISS turn-on request (channel 30)  -> 90 s turn-on sequence
#   5 s    V35E   lamp test (charges the AGC warning filter)
#  10 s    V16N36E   mission clock
#  20 s    V37E00E   refused: alarm 1520 while the IMU turn-on is running
#  96 s    turn-on request dropped (channel 30), CDUs zeroed
# 110 s    V37E00E   accepted, P00
# 116 s    V05N09E   alarm codes
# 119 s    RSET
# 121 s    V16N65E   sampled time
#
# Usage: tools/diff_trace.sh [NCYCLES]   (default 10750000)
set -e
cd "$(dirname "$0")/.."
N=${1:-10750000}
OUT=${TMPDIR:-/tmp}/agc_diff_trace
mkdir -p "$OUT"
YA=external/virtualagc/yaAGC
gcc -O2 -o "$OUT/ref_trace" tools/ref_trace.c \
    $YA/agc_engine.c $YA/agc_engine_init.c $YA/agc_utilities.c $YA/rfopen.c $YA/Backtrace.c $YA/DecodeDigitalDownlink.c \
    -I$YA -lm 2>/dev/null
python3 -c "
from agc.program import load_program
from agc.rope import write_bin
write_bin(load_program('luminary099').fixed, '$OUT/Luminary099.bin')"
EV=$(python3 tools/my_trace.py --scenario)
if cmp <("$OUT/ref_trace" "$OUT/Luminary099.bin" "$N" "$EV") <(python3 tools/my_trace.py luminary099 "$N" "$EV"); then
    echo "IDENTICAL: $N cycles, yaAGC and agc/cpu.py agree after every memory cycle"
else
    echo "DIFFERENT: rerun both with the traces redirected to files and diff them"
    exit 1
fi
