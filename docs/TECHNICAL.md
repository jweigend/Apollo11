# Technical details: from the 1969 listing to a landing in Python

This page walks through what actually happens in this repository, with real
excerpts: a module of the original AGC assembly listing, the Python module
generated from it, a piece of the interpretive guidance language, the
emulator instruction that executes it, the hardware interface the landing
simulation plugs into, how the result is verified, the options and physics
of the simulation, and the layout of the repository.

```
 Luminary099/ALARM_AND_ABORT.agc      original listing (MIT Instrumentation Laboratory, 1969)
            │  agc/asm/assembler.py   port of yaYUL: labels, banks, interpretive packing
            ▼
 36 banks x 1024 words of rope memory, compared word for word with Luminary099.binsource
            │  agc/asm/pygen.py
            ▼
 agc/programs/luminary099/ALARM_AND_ABORT.py     one W(...) call per word, comments kept
            │  agc/program.py  (Program builds the rope image and the symbol table)
            ▼
 agc/cpu.py   executes the words, 85 333 memory cycles per second
            │  counters and I/O channels
            ▼
 agc/sim/     the spacecraft: IMU, landing radar, engine, jets, DSKY keyboard
```

## 1. A module of machine code

The file `ALARM_AND_ABORT.agc` holds the alarm and abort routines, among them
`BAILOUT`, the entry used for the 1201 and 1202 alarms during the real
landing, and `POODOO`, the entry for aborts that send the computer back to
the idle program P00.  Source as transcribed by the Virtual AGC project:
[Luminary099/ALARM_AND_ABORT.agc, line 150](https://github.com/chrislgarry/Apollo-11/blob/master/Luminary099/ALARM_AND_ABORT.agc#L150)
(scanned page images of the printout are at
[ibiblio.org/apollo](https://www.ibiblio.org/apollo/ScansForConversion/Luminary099/)).

```
POODOO		INHINT
		CA	Q
ABORT2		TS	ALMCADR
		INDEX	Q
		CAF	0
		TC	BORTENT
OCT77770	OCT	77770		# DON'T MOVE

		CAF	OCT35		# 4.35SPOT FOR GOPOODOO
		TS	L
		COM
		DXCH	-PHASE4
GOPOODOO	INHINT
		TC	BANKCALL	# RESET STATEFLG, REINTFLG, AND NODOFLAG.
		CADR	FLAGS
		CA	FLAGWRD7	# IS SERVICER CURRENTLY IN OPERATION?
		MASK	V37FLBIT
		CCS	A
		TCF	STRTIDLE
```

The same lines in the generated module
[`agc/programs/luminary099/ALARM_AND_ABORT.py`](../agc/programs/luminary099/ALARM_AND_ABORT.py):

```python
W('5652', 0o00004, 'POODOO', 'INHINT', line=150)
W('5653', 0o30002, '', 'CA', 'Q', line=151)
W('5654', 0o55363, 'ABORT2', 'TS', 'ALMCADR', line=152)
W('5655', 0o50002, '', 'INDEX', 'Q', line=153)
W('5656', 0o30000, '', 'CAF', '0', line=154)
W('5657', 0o05574, '', 'TC', 'BORTENT', line=155)
W('5660', 0o77770, 'OCT77770', 'OCT', '77770', "DON'T MOVE", kind='data', line=156)

W('5661', 0o34765, '', 'CAF', 'OCT35', '4.35SPOT FOR GOPOODOO', line=158)
W('5662', 0o54001, '', 'TS', 'L', line=159)
W('5663', 0o40000, '', 'COM', line=160)
W('5664', 0o52761, '', 'DXCH', '-PHASE4', line=161)
W('5665', 0o00004, 'GOPOODOO', 'INHINT', line=162)
W('5666', 0o04616, '', 'TC', 'BANKCALL', 'RESET STATEFLG, REINTFLG, AND NODOFLAG.', line=163)
W('5667', 0o27755, '', 'CADR', 'FLAGS', kind='data', line=164)
W('5670', 0o30103, '', 'CA', 'FLAGWRD7', 'IS SERVICER CURRENTLY IN OPERATION?', line=165)
W('5671', 0o74746, '', 'MASK', 'V37FLBIT', line=166)
W('5672', 0o10000, '', 'CCS', 'A', line=167)
W('5673', 0o15701, '', 'TCF', 'STRTIDLE', line=168)
```

Each `W(address, word, label, operator, operand, comment)` is one 15-bit word
of fixed memory.  The address `'5652'` is a fixed-fixed location (bank 02 or
03, directly addressable); banked locations look like `'31,3534'`.  The word
is what the assembler produced, and it is all the emulator ever reads.  The
rest is bookkeeping that the emulator does not need but the test UI and the
simulation use: the label becomes a symbol, the operator and operand make the
disassembly readable, `kind='data'` marks constants and `CADR` address words,
and `line` points back into the listing.

Two words decoded by hand, to show that nothing is hidden:

| word | bits | meaning |
|------|------|---------|
| `0o30002` | opcode 3 (`CA`), address 0002 | load the accumulator from register Q (the return address) |
| `0o55363` | opcode 5, quarter-code 2 (`TS`), address 1363 | store the accumulator in erasable 1363, which the symbol table maps to `ALMCADR` |

`INHINT` is `TC 4`, `COM` is `CS A` (`0o40000`), `CAF` is `CA` with a fixed
address.  The assembler port in `agc/asm/` reproduces these encodings
exactly, and the comparison against the octal listing proves it for every
word of the rope.

## 2. The interpretive language

Most of the guidance and navigation code is not written in machine
instructions but in the AGC's interpretive language, a stack-oriented
vector and double-precision arithmetic language whose "instructions" are
data read by the `INTERPRETER` module.  The vertical descent guidance of the
automatic landing phase P65 is four lines:
[LUNAR_LANDING_GUIDANCE_EQUATIONS.agc, line 904](https://github.com/chrislgarry/Apollo-11/blob/master/Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc#L904)

```
# 	THE P65 GUIDANCE EQUATION IS AS FOLLOWS:-
#		      -      -
#		      V2FG - VGU
#		ACG = ----------
#		        TAUVERT

P65VERT		TC	INTPRET
		VLOAD	VSU
			V2FG
			VGU
		V/SC	GOTO
			TAUVERT
			AFCCALC1
```

Load the target velocity vector `V2FG`, subtract the current velocity `VGU`,
divide by the time constant `TAUVERT`, and continue at the acceleration
command routine.  Generated Python:

```python
W('31,3534', 0o06037, 'P65VERT', 'TC', 'INTPRET', line=907)
W('31,3535', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=908)
W('31,3536', 0o02511, '', '', 'V2FG', kind='operand', line=909)
W('31,3537', 0o03627, '', '', 'VGU', kind='operand', line=910)
W('31,3540', 0o52141, '', 'V/SC', 'GOTO', kind='interp', line=911)
W('31,3541', 0o02517, '', '', 'TAUVERT', kind='operand', line=912)
W('31,3542', 0o63204, '', '', 'AFCCALC1', kind='operand', line=913)
```

`TC INTPRET` hands control to the interpreter.  From then on the words are
data: `0o52375` packs two seven-bit interpretive opcodes (`VLOAD` and `VSU`)
into one word, and the following words are their operands, erasable
addresses plus one for `V2FG` and `VGU`.  This is why the project runs the
software in an emulator instead of translating it into Python functions: a
translation would have to reimplement the interpreter, the packing, the
push-down list and the scaling conventions, and it could never be checked
against the original.  Executing the original words can.

`V2FG` itself comes from the pad load, the erasable memory the ground loaded
before the flight.  In [`agc/sim/padload.py`](../agc/sim/padload.py) the Apollo 11
value is kept in the original octal form:

```python
"V2FG": (0o2510, [0o77777, 0o73242, 0o00000, 0o00000, 0o00000, 0o00000]),
```

Six words, a vector of three double-precision numbers scaled at 2^10 m/cs.
The first component decodes to −0.914 m/s: the landing program descends at
3 ft/s with zero horizontal velocity until the probes touch.

## 3. Executing a word

[`agc/program.py`](../agc/program.py) collects the `W(...)` calls of all 91
modules into the 36 banks of rope memory and a symbol table:

```python
def W(self, address, value, label="", operator="", operand="", comment="", kind="basic", line=0):
    bank, offset = parse_fixed_address(address)
    self.words.append(Word(bank, offset, value, label, operator, operand, comment, kind, self, line))
    if label:
        self.symbols[label] = SymbolDef(label, "label", pseudo_address(bank, offset), self, line)
```

[`agc/cpu.py`](../agc/cpu.py) is the Block II computer: ones' complement
arithmetic, the 16-bit accumulator with overflow, the editing registers,
the scaler that drives the timers, interrupts, counters and I/O channels.
`step()` advances one memory cycle time (MCT, 11.72 µs; 85 333 per second),
and when an instruction completes, `_execute()` decodes it.  The first two
cases of that decoder are the instructions from the example above:

```python
if op < 0o10:                                   # TC
    k = addr12
    if k == 3:                                  # RELINT
        self.allow_interrupt = True
    elif k == 4:                                # INHINT
        self.allow_interrupt = False
    elif k == 6:                                # EXTEND
        self.extracode = True
    else:
        if k != Q:                              # not RETURN
            e[Q] = 0o177777 & self.next_z
        self.next_z = addr12
elif op < 0o12:                                 # CCS
    if addr10 < 3:
        vk = 0o177777 & e[addr10]
        operand = overflow_corrected(vk)
        e[A] = odabs(vk)
        ...
```

`TC 4` is `INHINT`, `TC 6` is `EXTEND`, any other `TC` saves the return
address in Q and jumps.  `CCS` is the four-way branch on the sign and zero
state of a register, with the diminished absolute value left in the
accumulator; it is the instruction that makes ones' complement arithmetic
(which has a +0 and a −0) visible everywhere in the code.  Every instruction
of the machine is implemented like this, with its timing in MCTs, so the
software sees the clock it was written for: the 2-second servicer cycle, the
100-millisecond autopilot, the 10-millisecond throttle pulses.

## 4. The spacecraft side

The flight software talks to the vehicle only through counters and I/O
channels, and the simulation in [`agc/sim/`](../agc/sim) provides exactly
those.  Nothing is written into the AGC's memory once the flight has
started.

| Interface | Direction | Content | Simulated by |
|-----------|-----------|---------|--------------|
| counters `CDUX/Y/Z` | in | gimbal angles of the inertial platform, one pulse per 2^-15 rev | `imu.py` |
| counters `PIPAX/Y/Z` | in | integrated non-gravitational acceleration, 1 cm/s per pulse | `imu.py` |
| counter `RNRAD`, channel 13 | in | landing radar range and velocity words, selected by the AGC | `lr.py` |
| channel 33 | in | radar data good, antenna position, scale | `lr.py` |
| channels 30-32 | in | engine armed, auto throttle, mode switch, DSKY keys | `mission.py`, `dsky.py` |
| channel 11 | out | engine on / off | `lm.py` |
| counter `THRUST`, channel 14 | out | throttle increments, 12.53 N per pulse | `lm.py` |
| channels 5, 6 | out | the sixteen RCS jets | `lm.py` |
| channel 12 | out | trim gimbal drive, radar antenna to position 2 | `lm.py`, `lr.py` |
| channel 10 | out | the DSKY display relays | `dsky.py` |

The main loop in `mission.py` runs in lock-step: every 20 ms the emulator
executes 1707 memory cycles, the vehicle moves, the platform gimbals follow
the attitude, the accelerometers emit their pulses, the radar beams are
intersected with the lunar sphere.  A script plays the crew and presses the
DSKY keys the crew pressed.  Everything else, from the ignition time to the
throttle setting at touchdown, is decided by the words in section 1 and 2.

## 5. Verification

The assembled rope is compared word for word with the octal listing that the
Virtual AGC project reconstructed from the original printouts
([Luminary099.binsource](https://github.com/virtualagc/virtualagc/blob/master/Luminary099/Luminary099.binsource)):

```python
def compare(fixed, used, reference):
    """Return a list of (bank, offset, ours, theirs) mismatches."""
```

The list is empty for both Luminary 099 and Comanche 055, including the
"bugger words", the checksums at the end of each bank.  That comparison is
what turned up the transcription errors in the GitHub copy of the source
listed in `agc/asm/fixups.py`.

The emulator is a cycle-level model written after yaAGC: every instruction
takes its documented number of memory cycles, the timers, counters,
interrupts and hardware alarms follow the same rules.  It is verified at the
behaviour level: Luminary boots with the fresh-start alarm 1107 like the real
cold start, runs without hardware alarms, answers the DSKY (`V35E` lamp
test, `V16N36E` clock, `V37E00E` idle), and flies the landing.  `tools/`
contains a cycle-by-cycle trace harness for differential testing against
yaAGC (`ref_trace.c` wraps the Virtual AGC engine, `my_trace.py` prints the
same trace, `diff` shows the first deviation).  That comparison has not been
run to completion, so cycle accuracy is the design and the behaviour is the
evidence.

The landing itself is a third, weaker kind of evidence: it shows that the
guidance, navigation and control of Luminary are internally consistent and
bring a plausible vehicle down softly in a consistent physical world.  It
proves nothing about the real sensors, the real vehicle or the terrain.

## 6. Things learned while making it land

A few findings from debugging the simulation that say something about the
original system:

- Luminary reads the landing radar on its own, but it only uses the data
  after the crew keys `V57`.  Without that single keystroke the computer
  flies the whole descent on inertial navigation, the altitude error grows
  to thousands of feet, P64 ends far too early and P65 hovers until the
  descent stage runs dry.  Aldrin keyed it at "Delta-H minus 2900".
- The computer's state vector is only as good as its clock.  Running the
  AGC for 1.75 seconds while the vehicle stood still (the time it takes to
  key `V37E63E`) put the navigation 3 km downrange and the landing 3.4 km
  east of the target, with the software otherwise perfect.
- Everything the DSKY shows is up to two seconds old, the age of the last
  accelerometer read.  During the braking burn the velocity changes by
  22 ft/s in that time, so comparing a displayed value with the truth of the
  moment produces phantom errors.  The computer's own ΔH (noun 68) is the
  honest number.
- The pre-ignition navigation differs from the simulated world by about
  2 ft/s because the AGC integrates its orbit with the lunar J2 and C22 terms
  of the pad load while the simulation uses a point mass; the radar removes
  the difference within a minute.

## 7. Running the landing simulation

`python3 -m agc.sim land` starts eight minutes before powered descent
initiation in the 60 × 8 nautical mile descent orbit, with the real time of
landing from the pad load (`TLAND` = 100:50:49 GET in this scenario).
Before that the computer gets a fresh start: self-check, the 90 s IMU
turn-on sequence of the flight software, P00 and the pad load, about 110 s
of AGC time, which the emulator (roughly three times real time) needs some
40 s for.  The first run shows this as `[setup]` progress lines and then
saves the machine state to `landing_agc_state.json`; later runs restore it
and are flying within seconds.  A status line every five simulated seconds
shows program, DSKY, altitude, rates, range, throttle, mass and attitude; in
between, the events of the flight appear.  The whole descent takes about
13 minutes of computing for 20 minutes of flight.

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
| `--agc-cache ''` | do not cache the AGC state after its 90 s IMU turn-on sequence (fresh start every time, about 40 s longer) |

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

## 8. Project layout

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
| `tools/` | trace harness for the differential test against yaAGC |
| `tests/` | pytest suite |
| `docs/` | this page, the architecture diagram, screenshots |

The generated Python modules of both programs are in the repository.  To
regenerate them from the original source, fetch the listings and run the
converter (about 25 s per program):

```bash
git clone --depth 1 https://github.com/chrislgarry/Apollo-11.git external/Apollo-11
git clone --depth 1 --filter=blob:none --sparse https://github.com/virtualagc/virtualagc.git external/virtualagc
(cd external/virtualagc && git sparse-checkout set yaYUL yaAGC Luminary099 Comanche055)
python3 -m agc convert Luminary099 Comanche055
```
