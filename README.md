# Apollo 11 Guidance Computer in Python

The original Apollo 11 flight software, **Luminary 099** (Lunar Module) and
**Comanche 055** (Command Module), assembled bit-exactly from the 1969
listings, executed by a cycle-accurate emulator of the Apollo Guidance
Computer written in pure Python, and flown through a complete automatic
lunar landing in a six-degree-of-freedom simulation with a 3D viewer.

Nothing in the flight software is modified.  The simulation only provides
what the real hardware provided: the vehicle, the inertial platform, the
landing radar, the DSKY keyboard and the pad load.  Luminary computes the
ignition time, flies the attitude manoeuvre, ignites and throttles the
descent engine, fires the attitude-control jets, steers through the braking
and approach phases and sets the vehicle down on Tranquility Base.

![Final approach in P64, 1.5 km above the Sea of Tranquility](docs/approach.png)

```
contact at GET 100:49:47: vertical -2.9 ft/s, horizontal 15.1 ft/s,
9 m from the target, tilt 0.6 deg, DPS propellant left 605 kg
```

The horizontal speed is measured in the inertial frame and equals the
rotation of the lunar surface at the site; relative to the ground the
vehicle is at rest.

## Contents

- [What is genuine and what is simulated](#what-is-genuine-and-what-is-simulated)
- [Quick start](#quick-start)
- [The landing simulation](#the-landing-simulation)
- [The 3D viewer](#the-3d-viewer)
- [How the AGC runs in Python](#how-the-agc-runs-in-python)
- [Verification](#verification)
- [Test UI](#test-ui)
- [Project layout](#project-layout)
- [Limitations and ideas](#limitations-and-ideas)
- [Credits and license](#credits-and-license)

## What is genuine and what is simulated

**Genuine**

- The flight software.  Luminary 099 assembles to the same 36 × 1024 words as
  the octal listing reconstructed from the original printouts by the Virtual
  AGC project, checksums ("bugger words") included.  The Python modules are
  generated from that rope.  The emulator runs with hardware alarm checking
  enabled, so a real restart would occur if the software tripped one.
- The pad load.  The erasable constants are the Apollo 11 values from the
  Grumman LM Data Book: guidance targets, landing site, landing radar
  weights, DAP gains, ignition algorithm parameters, time of landing.
- The crew procedures.  A script keys exactly what the crew keyed: `V37E63E`,
  `PRO` on the ignition-algorithm display, the R60 attitude manoeuvre, `V99`
  ignition enable, declining the optional fine alignment, and `V57E` to let
  the computer use the landing radar once ΔH is plausible.
- The landing site.  The simulation does not know where Tranquility Base is;
  it lets Luminary compute the inertial site vector and the lunar rotation
  axis from its own ephemeris routines and uses those.

**Simulated**

- The vehicle: a rigid body with the descent engine (throttle counter,
  12.53 N per pulse, 0.2 s lag, 43.9 kN fixed throttle position), the trim
  gimbal, the sixteen RCS jets (445 N each, driven by channels 5 and 6), mass
  and inertia.
- The sensors: an ideal inertial platform (gimbal CDU counters, PIPA
  accelerometer pulses of 1 cm/s) and a geometric landing radar (two antenna
  positions, range beam, three velocity beams, data-good discretes).  No
  noise, no bias.
- The world: a point-mass Moon.  The AGC's own navigation uses the lunar
  J2/C22 terms from its pad load, so the two disagree by about 2 ft/s before
  the landing radar takes over, which is realistic.
- One deliberate deviation in the pad load: the fifteen IMU compensation
  constants (accelerometer bias and scale factor, gyro drifts) are zeroed,
  because the simulated IMU has no errors to compensate.

**Not modelled**

- The rendezvous radar, whose switch setting caused the famous 1201/1202
  executive overflow alarms.  The simulation therefore produces no overload
  and no restarts.
- The abort guidance system, the manual rate-of-descent mode P66 that
  Armstrong used, and the terrain.  Here the automatic landing program P65
  flies to touchdown, which no Apollo commander ever let it do.

## Quick start

Python 3.10 or newer.  The AGC port itself needs only the standard library;
the landing simulation needs `numpy`.

```bash
git clone https://github.com/jweigend/Apollo11.git
cd Apollo11
python3 -m venv .venv && .venv/bin/pip install numpy pytest
source .venv/bin/activate

# boot the Lunar Module computer and talk to it through the DSKY
python3 -m agc run luminary099 --keys V35E        # lamp test
python3 -m agc run luminary099 --keys V16N36E     # mission clock
python3 -m agc run luminary099 --keys V37E00E     # select program P00

# fly the landing (about 13 minutes of computing for 20 minutes of flight)
python3 -m agc.sim land

# fly it in real time and watch in the browser
python3 -m agc.sim land --view --realtime

# replay a recorded flight
python3 -m agc.sim view landing.csv

# interactive test UI with DSKY, registers, code and watches
python3 -m agc tui luminary099

python3 -m pytest
```

The generated Python modules of both programs are in the repository.  To
regenerate them from the original source, fetch the listings and run the
converter (about 25 s per program):

```bash
git clone --depth 1 https://github.com/chrislgarry/Apollo-11.git external/Apollo-11
git clone --depth 1 --filter=blob:none --sparse https://github.com/virtualagc/virtualagc.git external/virtualagc
(cd external/virtualagc && git sparse-checkout set yaYUL yaAGC Luminary099 Comanche055)
python3 -m agc convert Luminary099 Comanche055
```

## The landing simulation

`python3 -m agc.sim land` starts eight minutes before powered descent
initiation in the 60 × 8 nautical mile descent orbit, with the real time of
landing from the pad load (`TLAND` = 100:50:49 GET in this scenario).  A
status line every five simulated seconds shows program, DSKY, altitude,
rates, range, throttle, mass and attitude.  In between, the events of the
flight appear:

```
100:30:14.2  crew: V37E63E - select P63 braking phase
100:30:30.9  AGC computed TIG = 100:37:49.61 (in 438.7 s)
100:30:31.9  DSKY flashing V06 N61  R1 -   50 R2 -07 18 R3 +000
100:30:33.5  crew: PRO  (P63 ignition algorithm done: accept N61)
100:30:34.0  DSKY flashing V50 N25  R1  00014 R2 -   1  R3
100:30:35.6  crew: ENTR  (checklist 00014: skip the optional fine alignment)
100:30:37.1  DSKY flashing V50 N18  R1 +17997 R2 +28631 R3 +00002
100:30:38.7  crew: PRO  (start automatic maneuver to burn attitude (R60))
100:30:54.0  crew: ENTR  (maneuver complete: leave R60)
100:36:49.8  crew: DESCENT ENGINE ARM (TIG-60 s)
100:37:44.9  DSKY flashing V99 N62  R1 +55634 R2 -00 05 R3 +00005
100:37:46.5  crew: PRO  (V99: permit ignition)
100:37:49.6  DPS ignition at GET 100:37:49.62
100:43:55.7  LR range data good, velocity data good
100:44:03.4  crew: V57E - permit landing radar updates (DELTAH = +51 ft)
100:46:16.0  LR antenna commanded to position 2
100:46:16.6  PROG 64
100:46:17.1  DSKY flashing V06 N64  R1 +99 71 R2 -01422 R3 +07883
100:46:18.6  crew: PRO  (acknowledge flashing V06 N64)
100:49:00.9  PROG 65
100:49:47.5  *** CONTACT - engine stop ***
100:49:47.5  contact at GET 100:49:47.46: vertical -2.9 ft/s, horizontal 15.1 ft/s,
             9 m from the target, tilt 0.6 deg, DPS propellant left 605 kg
```

Everything after the keystrokes is Luminary: the ignition time comes out of
its ignition algorithm, the 26 s at 10 % throttle and the throttle-up are
its own, the braking phase P63 ends at high gate where it commands the
landing radar antenna to position 2 and switches to P64, and 12 s before the
approach target it switches to the automatic landing phase P65, which nulls
the horizontal velocity and descends at 3 ft/s until the probes touch.

Telemetry goes to `landing.csv` (two samples per second: state, DSKY
registers, alarms, thrust, jets, gimbal, radar status, attitude vectors)
and the events to `landing.events.csv`.  `python3 -m agc.sim report
landing.csv` summarises a run with ASCII plots.

| Option | Effect |
|--------|--------|
| `--until 600` | stop after 600 simulated seconds |
| `--no-lr` | fly without the landing radar (inertial navigation only) |
| `--realtime` | pace the simulation to wall-clock time |
| `--view` | open the 3D viewer and follow the flight live |
| `--dt 0.02` | physics step (the AGC runs in lock-step) |
| `--probe-cache ''` | do not cache the AGC-computed landing site |

**Physics.**  Point-mass lunar gravity with the AGC's μ, six degrees of
freedom, descent engine with 980–6300 lbf throttle range and fixed throttle
position above that, exhaust velocity 2956 m/s (Luminary `DPSVEX`), moments
of inertia chosen to match the one-jet accelerations the digital autopilot
assumes.  The AGC runs at 85 333 memory cycles per second in lock-step with
the vehicle: every 20 ms the emulator executes the corresponding number of
cycles, the vehicle moves, and the CDU and PIPA counters are pulsed.

| Module | Content |
|--------|---------|
| `agc/sim/mission.py` | scenario, AGC initialisation, crew procedures, main loop, telemetry |
| `agc/sim/padload.py` | the Apollo 11 pad load, checked against the symbol table on load |
| `agc/sim/lm.py` | vehicle: mass, DPS, trim gimbal, RCS jets, rigid-body dynamics |
| `agc/sim/imu.py` | inertial platform: gimbal angles, CDU counters, PIPA pulses, REFSMMAT |
| `agc/sim/lr.py` | landing radar: antenna positions, range and velocity beams, discretes |
| `agc/sim/scaling.py` | AGC fixed-point formats (SP, DP, TP, B-scaling) |
| `agc/sim/viewer.py` | the 3D viewer (a small HTTP server and one HTML page) |
| `agc/sim/report.py` | run summary with ASCII plots |

## The 3D viewer

`python3 -m agc.sim view landing.csv` serves a page on `http://127.0.0.1:8765/`
(three.js from a CDN, everything else inline).  It shows the Moon with
procedural craters under a low morning sun from the east, the landing site
and the ground track, the flown trajectory, the Lunar Module with its
simulated attitude, the descent engine plume and the firing RCS jets, a
head-up display and a DSKY.  The crew and AGC log scrolls on the right and
new entries are announced during playback.  Playback, scrubbing, speed,
camera (chase, side, landing site, free orbit) and true-scale LM size are in
the control bar.  Started with `land --view`, the page follows the running
simulation live.

![Touchdown in P65](docs/touchdown.png)

If Python runs in a container or on a remote machine, forward the port your
IDE reports and open the URL it offers; the viewer must keep running while
the page is open.

## How the AGC runs in Python

```
   external/Apollo-11/*.agc         original source, 1969
            │
            ▼
   agc/asm/   assembler (a port of yaYUL), verified bit-exact against the
              octal listings of the original printouts
            │
            ▼
   agc/programs/luminary099/*.py    91 modules, one .py per .agc file
   agc/programs/comanche055/*.py    86 modules
            │
            ▼
   agc/cpu.py   AGC CPU emulator  ◄──►  agc/dsky.py  DSKY model
            │
            ▼
   agc/sim/    landing simulation       agc/tester/tui.py   test UI
```

Each `.agc` file becomes a Python module that follows the listing line by
line.  The programmers' comments survive as Python comments, every memory
word is a `W(...)` call and every symbol definition an `S(...)` call:

```python
# TO ENTER A JOB REQUEST REQUIRING NO VAC AREA:
W('5072', 0o00004, 'NOVAC', 'INHINT', line=37)
W('5073', 0o65164, '', 'AD', 'FAKEPRET', 'LOC(MPAC +6) - LOC(QPRET)', line=38)
W('5074', 0o54063, '', 'TS', 'NEWPRIO', 'PRIORITY OF NEW JOB + NOVAC C(FIXLOC)', line=39)
```

`W(address, word, label, opcode, operand, comment)`: addresses in listing
style (`'5072'` fixed-fixed, `'32,2776'` bank 32 offset 2776), the word is
the assembled 15-bit value.  Interpreter instructions and their operands are
marked `kind='interp'` and `kind='operand'`, constants `kind='data'`.
`agc.program.Program` builds the rope memory from the modules and offers
symbol lookups:

```python
from agc.program import load_program
from agc.cpu import AGC, CYCLES_PER_SECOND
from agc.dsky import DSKY

prog = load_program("luminary099")
cpu = AGC(prog.fixed)
dsky = DSKY(cpu)
cpu.run(3 * CYCLES_PER_SECOND)        # 3 seconds of AGC time
dsky.type_sequence("V16N36E")         # show the clock
cpu.run(2 * CYCLES_PER_SECOND)
print("\n".join(dsky.render()))
print(prog.symbol("P63LM").fixed_location())      # (26, 510) = bank 32, offset 776
```

**Why an emulator rather than a translation into Python functions?**  The
AGC code is largely data-driven: `INDEX` modifies the following instruction
at run time, jump tables are constants in memory, and much of the flight
software is written in the interpretive language (`VLOAD`, `DLOAD`,
`STORE`, …) that the `INTERPRETER` module reads as data.  A readable
one-to-one translation into Python control flow would be neither correct
nor testable.  So the modules hold the software bit for bit plus all
symbols and comments, and a small CPU in Python executes it with exactly the
arithmetic of the original: ones' complement, the 16-bit accumulator with
overflow, the editing registers, timers, interrupts, counters and I/O
channels.  Routines can be watched symbolically, stopped at breakpoints and
driven through the real DSKY protocol.

## Verification

- Both programs assemble bit-exactly against the octal listings
  reconstructed from the original printouts (`Luminary099.binsource`,
  `Comanche055.binsource` from Virtual AGC): zero differing words in
  36 × 1024, checksums included.
- That comparison exposed transcription errors in the GitHub copy of the
  source that change the code (a `1.08-2` for `1.0 B-2`, two misspelled
  labels, a comment line without `#`, pseudo-labels `+2` after a tab).  They
  are documented in `agc/asm/fixups.py` and corrected on reading.  Luminary
  needed no word-changing fix.
- Luminary boots in the emulator (fresh start with alarm 1107 like the real
  cold start), runs without hardware alarms, answers `V35E` with the lamp
  test, shows the running mission clock on `V16N36E`, and switches to P00.
- The emulator runs at about three times real time on CPython 3.12.
- `tools/` holds a cycle-by-cycle differential test against the reference
  emulator yaAGC (`tools/ref_trace.c` wraps the Virtual AGC engine,
  `tools/my_trace.py` prints the same trace; `diff` shows the first
  deviation).
- `python3 -m pytest` runs 29 tests: assembler bit-exactness, CPU
  arithmetic, boot and DSKY, fixed-point scaling, pad load integrity,
  gimbal maths, ballistic-impact detection and the viewer's port selection.

## Test UI

`python3 -m agc tui luminary099`

- Type DSKY keys directly: digits, `+`, `-`, `v` VERB, `n` NOUN, `e` ENTR,
  `c` CLR, `r` RSET, `k` KEY REL, `p` PRO.
- `SPACE` run/pause, `s` one instruction, `S` 100 instructions, `[` / `]`
  slower/faster, `q` quit.
- `TAB` cycles module list, routines of the module and watch list; `ENTER`
  shows a routine in the code window, `b` sets a breakpoint there.
- `:` commands: `:w SYMBOL` watch an erasable, `:b LABEL`, `:g LABEL`,
  `:keys V16N36E`, `:run 5`, `:poke SYMBOL 12345`, `:reset`, `:help`.

## Project layout

| Path | Content |
|------|---------|
| `agc/asm/address.py` | AGC address model (pseudo addresses, banks), number parsing |
| `agc/asm/tables.py` | opcode tables: machine instructions, pseudo-ops, interpreter instructions |
| `agc/asm/assembler.py` | multi-pass assembler (port of yaYUL), produces the 36 banks of fixed memory |
| `agc/asm/fixups.py` | documented transcription errors of the GitHub copy, corrected on reading |
| `agc/asm/binsource.py` | reader for the octal listings (`*.binsource`) and comparison |
| `agc/asm/pygen.py` | generates the Python modules from the assembly |
| `agc/program.py` | run-time representation: `Program`, `Module`, symbols, address lookups |
| `agc/cpu.py` | the AGC CPU: instructions, timers, interrupts, channels, hardware alarms |
| `agc/dsky.py` | DSKY: display relay decoding, lamps, key codes |
| `agc/rope.py` | read/write the Virtual AGC `.bin` rope format |
| `agc/programs/` | the generated flight software |
| `agc/sim/` | the landing simulation and the viewer |
| `agc/tester/tui.py` | the test UI |
| `tests/` | pytest suite |
| `docs/` | screenshots |

## Limitations and ideas

The automatic landing shows that Luminary's guidance, navigation and
control are internally consistent and capable of a soft landing from the
descent orbit in a consistent physical world.  It does not show what would
have happened on 20 July 1969 without Armstrong: the real navigation was
off by several kilometres at radar acquisition (ΔH was −2900 ft, here it is
+51 ft), the rendezvous radar load triggered restarts, and the automatic
target lay in a boulder field.  Things that would bring the simulation
closer to the historical flight, all feasible with the current structure:

- an initial state-vector error matching the real ΔH,
- sensor noise and the real IMU errors to go with the pad-load compensation,
- a digital terrain model of the landing zone,
- the rendezvous radar interrupt load to provoke the 1201/1202 alarms,
- a scripted P66 for comparison with the manual landing,
- Comanche 055 in the loop for the rendezvous programs.

## Credits and license

The AGC source listings are the work of the MIT Instrumentation Laboratory
(1969), transcribed by Ron Burkey and the Virtual AGC project and mirrored
in `chrislgarry/Apollo-11`.  The assembler and emulator logic follow
`yaYUL` and `yaAGC` from Virtual AGC (GPL v2 or later); this port is
therefore released under the GNU General Public License, version 2 or
later (see `LICENSE`).  Pad-load values come from the Apollo 11 LM Data
Book and the Luminary 1A erasable memory listing.
