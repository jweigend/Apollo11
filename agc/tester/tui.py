"""Curses test UI: DSKY, CPU state, code view, module browser and watches.

Start with ``python -m agc tui luminary099``.

Keys
----
DSKY:   0-9 + -   v=VERB  n=NOUN  e=ENTR  c=CLR  r=RSET  k=KEY REL  p=PRO
Control: SPACE run/pause   s step one instruction   S step 100   q quit
         TAB switch focus (modules / routines / watches)   ENTER select
         b set breakpoint on selected routine   B clear all breakpoints
         [ ] slower / faster   : command line (see ':help')
"""

from __future__ import annotations

import curses
import time

from ..cpu import AGC, CYCLES_PER_SECOND, INTERRUPT_NAMES
from ..dsky import DSKY
from ..program import Program, Word, format_fixed_address, load_program

DSKY_KEYS = {
    "v": "VERB", "n": "NOUN", "e": "ENTR", "c": "CLR", "r": "RSET", "k": "KEY REL", "p": "PRO",
    "+": "+", "-": "-",
}
for _d in "0123456789":
    DSKY_KEYS[_d] = _d

DEFAULT_WATCHES = ["TIME2", "TIME1", "MODREG", "NEWJOB", "FAILREG", "REDOCTR", "VERBREG", "NOUNREG", "DSPCOUNT", "FLAGWRD0"]
DEFAULT_WATCHES_CM = ["TIME2", "TIME1", "MODREG", "NEWJOB", "FAILREG", "REDOCTR", "VERBREG", "NOUNREG"]


class Tester:
    def __init__(self, program: Program):
        self.prog = program
        self.cpu = AGC(program.fixed)
        self.dsky = DSKY(self.cpu)
        self.running = False
        self.speed = 1.0                 # multiple of real time; 0 = unlimited
        self.breakpoints: set[tuple[int, int]] = set()
        self.watches = list(DEFAULT_WATCHES if "lum" in program.name.lower() else DEFAULT_WATCHES_CM)
        self.watches = [w for w in self.watches if program.symbol(w)]
        self.focus = 0                   # 0 modules, 1 routines, 2 watches
        # start on the first module that actually contains executable routines
        self.mod_index = next((i for i, m in enumerate(program.modules) if m.routines()), 0)
        self.mod_scroll = 0
        self.rtn_index = 0
        self.rtn_scroll = 0
        self.watch_index = 0
        self.view_loc: tuple[int, int] | None = None   # code view anchor (None = follow Z)
        self.log: list[str] = ["ready - SPACE runs the computer, q quits, :help for commands"]
        self.cmd: str | None = None
        self.last_wall = time.monotonic()
        self.pro_release_at = 0
        self.instr_per_sec = 0.0
        self._ips_count = 0
        self._ips_time = time.monotonic()
        self.hit_breakpoint: str | None = None

    # ------------------------------------------------------------------
    def say(self, msg: str):
        self.log.append(msg)
        if len(self.log) > 200:
            del self.log[0]

    def current_module(self):
        return self.prog.modules[self.mod_index]

    def routines(self) -> list[Word]:
        return self.current_module().routines()

    # ------------------------------------------------------------------
    def advance(self):
        """Run the CPU for the wall-clock time that has elapsed."""
        now = time.monotonic()
        dt = now - self.last_wall
        self.last_wall = now
        if not self.running:
            return
        if self.speed > 0:
            cycles = int(dt * CYCLES_PER_SECOND * self.speed)
        else:
            cycles = int(0.03 * CYCLES_PER_SECOND * 50)
        cycles = min(cycles, CYCLES_PER_SECOND // 2)
        if self.breakpoints:
            self._run_with_breakpoints(cycles)
        else:
            n = self.cpu.run(cycles)
            self._ips_count += n
        if self.pro_release_at and self.cpu.cycles >= self.pro_release_at:
            self.dsky.release_pro()
            self.pro_release_at = 0
        if now - self._ips_time >= 1.0:
            self.instr_per_sec = self._ips_count / (now - self._ips_time)
            self._ips_count = 0
            self._ips_time = now

    def _run_with_breakpoints(self, cycles: int):
        cpu = self.cpu
        step = cpu.step
        for _ in range(cycles):
            if step():
                self._ips_count += 1
                loc = cpu.current_location()
                if loc is not None and loc in self.breakpoints:
                    self.running = False
                    label = self.prog.nearest_label(*loc)
                    self.say(f"breakpoint hit at {format_fixed_address(*loc)} {label}")
                    break

    def step_instructions(self, n: int):
        for _ in range(n):
            self.cpu.run_instructions(1)
        self.view_loc = None

    # ------------------------------------------------------------------
    def handle_key(self, ch: int, stdscr) -> bool:
        """Returns False to quit."""
        if self.cmd is not None:
            return self.handle_cmd_key(ch)
        if ch in (ord("q"), 27):
            return False
        key = chr(ch) if 0 <= ch < 256 else ""
        if key in DSKY_KEYS:
            name = DSKY_KEYS[key]
            self.dsky.press(name)
            if name == "PRO":
                self.pro_release_at = self.cpu.cycles + CYCLES_PER_SECOND // 4
            self.say(f"key {name}")
            return True
        if key == " ":
            self.running = not self.running
            self.last_wall = time.monotonic()
            self.view_loc = None
            self.say("running" if self.running else "paused")
        elif key == "s":
            self.running = False
            self.step_instructions(1)
        elif key == "S":
            self.running = False
            self.step_instructions(100)
        elif key == "\t":
            self.focus = (self.focus + 1) % 3
        elif key == "[":
            self.speed = max(0.1, self.speed / 2) if self.speed else 8.0
            self.say(f"speed {self.speed:g}x")
        elif key == "]":
            if self.speed == 0:
                pass
            elif self.speed >= 8:
                self.speed = 0
                self.say("speed unlimited")
            else:
                self.speed = self.speed * 2
                self.say(f"speed {self.speed:g}x")
        elif key == ":":
            self.cmd = ""
        elif key == "b":
            self.toggle_breakpoint_on_selection()
        elif key == "B":
            self.breakpoints.clear()
            self.say("all breakpoints cleared")
        elif ch == curses.KEY_UP:
            self.move_selection(-1)
        elif ch == curses.KEY_DOWN:
            self.move_selection(1)
        elif ch == curses.KEY_PPAGE:
            self.move_selection(-10)
        elif ch == curses.KEY_NPAGE:
            self.move_selection(10)
        elif ch in (curses.KEY_ENTER, 10, 13):
            self.select()
        elif key == "f":
            self.view_loc = None
            self.say("code view follows Z")
        return True

    def move_selection(self, delta: int):
        if self.focus == 0:
            self.mod_index = max(0, min(len(self.prog.modules) - 1, self.mod_index + delta))
            self.rtn_index = 0
            self.rtn_scroll = 0
        elif self.focus == 1:
            r = self.routines()
            if r:
                self.rtn_index = max(0, min(len(r) - 1, self.rtn_index + delta))
                w = r[self.rtn_index]
                self.view_loc = (w.bank, w.offset)
        else:
            if self.watches:
                self.watch_index = max(0, min(len(self.watches) - 1, self.watch_index + delta))

    def select(self):
        if self.focus == 0:
            self.focus = 1
            r = self.routines()
            if r:
                w = r[self.rtn_index]
                self.view_loc = (w.bank, w.offset)
        elif self.focus == 1:
            r = self.routines()
            if r:
                w = r[self.rtn_index]
                self.view_loc = (w.bank, w.offset)
                self.say(f"viewing {w.label} at {w.address} ({self.current_module().name})")

    def toggle_breakpoint_on_selection(self):
        r = self.routines()
        if self.focus in (0, 1) and r:
            w = r[self.rtn_index]
            loc = (w.bank, w.offset)
            if loc in self.breakpoints:
                self.breakpoints.discard(loc)
                self.say(f"breakpoint removed: {w.label}")
            else:
                self.breakpoints.add(loc)
                self.say(f"breakpoint set: {w.label} at {w.address}")

    # ------------------------------------------------------------------
    def handle_cmd_key(self, ch: int) -> bool:
        if ch in (27,):
            self.cmd = None
        elif ch in (curses.KEY_ENTER, 10, 13):
            line = self.cmd
            self.cmd = None
            self.run_command(line.strip())
        elif ch in (curses.KEY_BACKSPACE, 127, 8):
            self.cmd = self.cmd[:-1]
        elif 32 <= ch < 127:
            self.cmd += chr(ch)
        return True

    def run_command(self, line: str):
        if not line:
            return
        parts = line.split()
        cmd, args = parts[0].lower(), parts[1:]
        prog = self.prog
        if cmd in ("help", "h", "?"):
            self.say("commands: keys V16N36E | w SYMBOL (watch) | uw SYMBOL | b LABEL (breakpoint) | g LABEL (view) | "
                     "run SECONDS | speed N | reset | poke SYMBOL OCTAL | help")
        elif cmd == "keys":
            for k in "".join(args).upper():
                if k in DSKY_KEYS:
                    self.dsky.press(DSKY_KEYS[k])
                    self.cpu.run(int(0.3 * CYCLES_PER_SECOND))
            self.say(f"typed {' '.join(args)}")
        elif cmd == "w" and args:
            for name in args:
                sym = prog.symbol(name.upper())
                if sym is None or sym.erasable_address() is None:
                    self.say(f"{name}: not an erasable symbol")
                elif name.upper() not in self.watches:
                    self.watches.append(name.upper())
        elif cmd == "uw" and args:
            for name in args:
                if name.upper() in self.watches:
                    self.watches.remove(name.upper())
        elif cmd == "b" and args:
            sym = prog.symbol(args[0].upper())
            loc = sym.fixed_location() if sym else None
            if loc is None:
                self.say(f"{args[0]}: not a fixed-memory label")
            else:
                self.breakpoints.add(loc)
                self.say(f"breakpoint set: {args[0].upper()} at {format_fixed_address(*loc)}")
        elif cmd == "g" and args:
            sym = prog.symbol(args[0].upper())
            loc = sym.fixed_location() if sym else None
            if loc is None:
                self.say(f"{args[0]}: not a fixed-memory label")
            else:
                self.view_loc = loc
                w = prog.word_at(*loc)
                if w is not None:
                    self.mod_index = prog.modules.index(w.module)
                    r = self.routines()
                    for i, x in enumerate(r):
                        if (x.bank, x.offset) == loc:
                            self.rtn_index = i
        elif cmd == "run" and args:
            secs = float(args[0])
            self.cpu.run(int(secs * CYCLES_PER_SECOND))
            self.say(f"ran {secs} s of AGC time")
        elif cmd == "speed" and args:
            self.speed = float(args[0])
        elif cmd == "reset":
            self.cpu.reset()
            self.dsky.rows = [0] * 16
            self.say("hardware reset")
        elif cmd == "poke" and len(args) == 2:
            sym = prog.symbol(args[0].upper())
            ea = sym.erasable_address() if sym else None
            if ea is None:
                self.say(f"{args[0]}: not an erasable symbol")
            else:
                self.cpu.e[ea] = int(args[1], 8) & 0o77777
                self.say(f"{args[0].upper()} := {int(args[1], 8):05o}")
        else:
            self.say(f"unknown command: {line}  (:help)")

    # ------------------------------------------------------------------
    # Drawing
    # ------------------------------------------------------------------
    def draw(self, stdscr):
        stdscr.erase()
        h, w = stdscr.getmaxyx()
        title = f" Apollo 11 AGC Tester - {self.prog.title} "
        self._put(stdscr, 0, 0, title[: w - 1], curses.A_REVERSE | curses.A_BOLD)
        status = ("RUNNING" if self.running else "PAUSED") + f"  speed {'max' if self.speed == 0 else f'{self.speed:g}x'}" \
                 f"  t={self.cpu.seconds:8.2f}s  {self.instr_per_sec / 1000:5.0f}k instr/s"
        self._put(stdscr, 0, max(0, w - len(status) - 1), status, curses.A_REVERSE)

        left_w = 34
        self.draw_dsky(stdscr, 1, 0, left_w)
        self.draw_cpu(stdscr, 1, left_w + 1, w - left_w - 1)
        code_top = 8
        code_h = max(3, h // 2 - code_top)
        self.draw_code(stdscr, code_top, left_w + 1, w - left_w - 1, code_h)
        bottom_top = code_top + code_h + 1
        bottom_h = h - bottom_top - 3
        if bottom_h > 2:
            third = w // 3
            self.draw_modules(stdscr, bottom_top, 0, third, bottom_h)
            self.draw_routines(stdscr, bottom_top, third + 1, third, bottom_h)
            self.draw_watches(stdscr, bottom_top, 2 * third + 2, w - 2 * third - 2, bottom_h)
        self.draw_log(stdscr, h - 3, 0, w)
        stdscr.refresh()

    def _put(self, scr, y, x, text, attr=0):
        h, w = scr.getmaxyx()
        if y < 0 or y >= h or x >= w:
            return
        text = text[: max(0, w - x - 1)]
        try:
            scr.addstr(y, x, text, attr)
        except curses.error:
            pass

    def draw_dsky(self, scr, y, x, width):
        s = self.dsky.state()
        on = s.lamps

        def lamp(name):
            return (f"[{name.center(11)}]", curses.A_REVERSE) if on.get(name) else (f" {name.center(11)} ", curses.A_DIM)

        rows = [
            ("UPLINK ACTY", "TEMP"), ("NO ATT", "GIMBAL LOCK"), ("STBY", "PROG"),
            ("KEY REL", "RESTART"), ("OPR ERR", "TRACKER"), ("NO DAP", "ALT"), ("PRIO DISP", "VEL"),
        ]
        self._put(scr, y, x, "DSKY".ljust(width), curses.A_BOLD)
        for i, (a, b) in enumerate(rows):
            ta, aa = lamp(a)
            tb, ab = lamp(b)
            self._put(scr, y + 1 + i, x, ta, aa)
            self._put(scr, y + 1 + i, x + 14, tb, ab)
        big = curses.A_BOLD
        yy = y + 9
        comp = "COMP ACTY" if on.get("COMP ACTY") else "         "
        self._put(scr, yy, x, f"  {comp}      PROG  {s.prog}", big)
        self._put(scr, yy + 1, x, f"  VERB  {s.verb}      NOUN  {s.noun}", big)
        self._put(scr, yy + 2, x, f"  R1  {s.r1}", big)
        self._put(scr, yy + 3, x, f"  R2  {s.r2}", big)
        self._put(scr, yy + 4, x, f"  R3  {s.r3}", big)
        self._put(scr, yy + 6, x, "keys: 0-9 + -  v=VERB n=NOUN e=ENTR", curses.A_DIM)
        self._put(scr, yy + 7, x, "c=CLR r=RSET k=KEY REL p=PRO", curses.A_DIM)
        self._put(scr, yy + 8, x, "SPACE run/pause  s step  : cmd  q quit", curses.A_DIM)
        self._put(scr, yy + 9, x, "TAB focus  ENTER select  b breakpoint", curses.A_DIM)

    def draw_cpu(self, scr, y, x, width):
        cpu = self.cpu
        r = cpu.registers()
        loc = cpu.current_location()
        where = self.prog.nearest_label(*loc) if loc else f"erasable {cpu.z:04o}"
        self._put(scr, y, x, "CPU".ljust(width), curses.A_BOLD)
        self._put(scr, y + 1, x, f"Z {cpu.z:04o} -> {where:20}  A {r['A']:06o}  L {r['L']:06o}  Q {r['Q']:06o}")
        self._put(scr, y + 2, x, f"EB {r['EB'] >> 8:o}  FB {r['FB'] >> 10:02o}  BB {r['BB']:05o}  SB {cpu.out7 >> 4:o}   "
                                 f"INT {'on ' if cpu.allow_interrupt else 'OFF'}  ISR {INTERRUPT_NAMES.get(cpu.interrupt_requests[0], '-') if cpu.in_isr else 'no'}  "
                                 f"EXT {int(cpu.extracode)}  IDX {cpu.index_value:05o}")
        self._put(scr, y + 3, x, f"TIME1 {r['TIME1']:05o} TIME2 {r['TIME2']:05o} TIME3 {r['TIME3']:05o} "
                                 f"TIME4 {r['TIME4']:05o} TIME5 {r['TIME5']:05o} TIME6 {r['TIME6']:05o}")
        pend = ",".join(INTERRUPT_NAMES[i] for i in range(1, 11) if cpu.interrupt_requests[i])
        alarms = f"{len(cpu.alarm_log)} alarms" + (f" (last: {cpu.alarm_log[-1][1]})" if cpu.alarm_log else "")
        self._put(scr, y + 4, x, f"pending rupts: {pend or '-':30} {alarms}")
        ch = cpu.chan
        self._put(scr, y + 5, x, f"CH11 {ch[0o11]:05o} CH12 {ch[0o12]:05o} CH13 {ch[0o13]:05o} CH14 {ch[0o14]:05o} "
                                 f"CH30 {ch[0o30]:05o} CH31 {ch[0o31]:05o} CH32 {ch[0o32]:05o} CH33 {ch[0o33]:05o}")

    def draw_code(self, scr, y, x, width, height):
        prog = self.prog
        cur = self.cpu.current_location()
        anchor = self.view_loc or cur
        title = "CODE" + ("  (following Z)" if self.view_loc is None else "  (f = follow Z)")
        self._put(scr, y, x, title.ljust(width), curses.A_BOLD)
        if anchor is None:
            self._put(scr, y + 1, x, f"executing in erasable memory at {self.cpu.z:04o}")
            return
        bank, off = anchor
        start = max(0, off - height // 3)
        for i in range(height - 1):
            o = start + i
            if o >= 0o2000:
                break
            w = prog.word_at(bank, o)
            addr = format_fixed_address(bank, o)
            mark = ">" if cur == (bank, o) else " "
            bp = "*" if (bank, o) in self.breakpoints else " "
            if w is None:
                line = f"{mark}{bp}{addr:8} {prog.fixed[bank][o]:05o}"
            else:
                label = w.label[:10]
                opnd = w.operand[:18]
                cmt = f"# {w.comment}" if w.comment else ""
                line = f"{mark}{bp}{addr:8} {w.value:05o}  {label:10} {w.operator:8} {opnd:18} {cmt}"
            attr = curses.A_REVERSE if cur == (bank, o) else 0
            if w is not None and w.kind in ("interp", "operand"):
                attr |= curses.A_DIM if not attr else 0
            self._put(scr, y + 1 + i, x, line.ljust(width), attr)

    def draw_modules(self, scr, y, x, width, height):
        mods = self.prog.modules
        self._put(scr, y, x, f"MODULES ({len(mods)})".ljust(width), curses.A_BOLD | (curses.A_UNDERLINE if self.focus == 0 else 0))
        visible = height - 1
        if self.mod_index < self.mod_scroll:
            self.mod_scroll = self.mod_index
        if self.mod_index >= self.mod_scroll + visible:
            self.mod_scroll = self.mod_index - visible + 1
        for i in range(visible):
            idx = self.mod_scroll + i
            if idx >= len(mods):
                break
            m = mods[idx]
            text = f"{m.name[:width - 8]:{width - 8}} {len(m.words):5d}"
            attr = curses.A_REVERSE if idx == self.mod_index and self.focus == 0 else (curses.A_BOLD if idx == self.mod_index else 0)
            self._put(scr, y + 1 + i, x, text, attr)

    def draw_routines(self, scr, y, x, width, height):
        r = self.routines()
        m = self.current_module()
        self._put(scr, y, x, f"ROUTINES in {m.name}"[:width].ljust(width), curses.A_BOLD | (curses.A_UNDERLINE if self.focus == 1 else 0))
        visible = height - 1
        if self.rtn_index < self.rtn_scroll:
            self.rtn_scroll = self.rtn_index
        if self.rtn_index >= self.rtn_scroll + visible:
            self.rtn_scroll = self.rtn_index - visible + 1
        for i in range(visible):
            idx = self.rtn_scroll + i
            if idx >= len(r):
                break
            w = r[idx]
            bp = "*" if (w.bank, w.offset) in self.breakpoints else " "
            text = f"{bp}{w.label:10} {w.address:8} {w.operator:6} {w.operand[:12]:12} {w.comment[:max(0, width - 42)]}"
            attr = curses.A_REVERSE if idx == self.rtn_index and self.focus == 1 else 0
            self._put(scr, y + 1 + i, x, text[:width], attr)

    def draw_watches(self, scr, y, x, width, height):
        self._put(scr, y, x, "WATCH (erasable)".ljust(width), curses.A_BOLD | (curses.A_UNDERLINE if self.focus == 2 else 0))
        for i, name in enumerate(self.watches[: height - 1]):
            sym = self.prog.symbol(name)
            ea = sym.erasable_address() if sym else None
            if ea is None:
                continue
            v = self.cpu.erasable_flat(ea)
            dec = v if v < 0o40000 else -(0o77777 - v)
            text = f"{name:9} {ea:04o}  {v:05o}  {dec:7d}"
            attr = curses.A_REVERSE if i == self.watch_index and self.focus == 2 else 0
            self._put(scr, y + 1 + i, x, text[:width], attr)

    def draw_log(self, scr, y, x, width):
        for i, msg in enumerate(self.log[-2:]):
            self._put(scr, y + i, x, msg[: width - 1], curses.A_DIM)
        if self.cmd is not None:
            self._put(scr, y + 2, x, f":{self.cmd}", curses.A_BOLD)
        else:
            self._put(scr, y + 2, x, "press : for command line", curses.A_DIM)


def _loop(stdscr, program: Program):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)
    tester = Tester(program)
    tester.say(f"loaded {program.title} ({len(program.modules)} modules, {len(program.symbols)} symbols)")
    while True:
        tester.advance()
        tester.draw(stdscr)
        time.sleep(0.02)
        ch = stdscr.getch()
        while ch != -1:
            if not tester.handle_key(ch, stdscr):
                return
            ch = stdscr.getch()


def main(program_name: str = "luminary099") -> int:
    program = load_program(program_name)
    curses.wrapper(_loop, program)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "luminary099"))
