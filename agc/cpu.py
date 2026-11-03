"""Block II Apollo Guidance Computer CPU emulator.

A cycle-level emulation of the AGC: 15-bit one's-complement words, the 16-bit
accumulator with overflow, banked erasable and fixed memory, the editing
registers (CYR, SR, CYL, EDOP), the 1600 pps scaler driving TIME1..TIME6,
interrupts, I/O channels and the hardware alarms (Night Watchman, TC Trap,
Rupt Lock) that trigger a GOJAM restart.

The instruction semantics follow the Virtual AGC ``yaAGC`` engine (Ron
Burkey et al., GPL), which has been validated against the real hardware's
behaviour for decades.  One call of :meth:`AGC.step` is one memory cycle
time (MCT, 11.7 microseconds); multi-MCT instructions simply take several
steps, so wall-clock pacing is a matter of counting steps.
"""

from __future__ import annotations

import copy
from typing import Callable

# --- register addresses --------------------------------------------------
A, L, Q, EB, FB, Z, BB, ZERO = 0, 1, 2, 3, 4, 5, 6, 7
ARUPT, LRUPT, QRUPT, SAMPTIME, _, ZRUPT, BBRUPT, BRUPT = 0o10, 0o11, 0o12, 0o13, 0o14, 0o15, 0o16, 0o17
CYR, SR, CYL, EDOP = 0o20, 0o21, 0o22, 0o23
TIME2, TIME1, TIME3, TIME4, TIME5, TIME6 = 0o24, 0o25, 0o26, 0o27, 0o30, 0o31
CDUX, CDUY, CDUZ, OPTY, OPTX = 0o32, 0o33, 0o34, 0o35, 0o36
PIPAX, PIPAY, PIPAZ = 0o37, 0o40, 0o41
INLINK, RNRAD, GYROCTR = 0o45, 0o46, 0o47
CDUXCMD, CDUYCMD, CDUZCMD, OPTYCMD, OPTXCMD = 0o50, 0o51, 0o52, 0o53, 0o54
THRUST, OUTLINK, ALTM = 0o55, 0o57, 0o60

AGC_P0, AGC_M0, AGC_P1, AGC_M1 = 0o00000, 0o77777, 0o00001, 0o77776

CHAN_SCALER2, CHAN_SCALER1 = 0o3, 0o4
CH77_PARITY_FAIL, CH77_TC_TRAP, CH77_RUPT_LOCK, CH77_NIGHT_WATCHMAN = 0o1, 0o4, 0o10, 0o20

NUM_INTERRUPTS = 10
INTERRUPT_NAMES = {1: "T6RUPT", 2: "T5RUPT", 3: "T3RUPT", 4: "T4RUPT", 5: "KEYRUPT1",
                   6: "KEYRUPT2", 7: "UPRUPT", 8: "DOWNRUPT", 9: "RADARUPT", 10: "HANDRUPT"}

SCALER_OVERFLOW = 80
SCALER_DIVIDER = 3
CYCLES_PER_SECOND = (1024000 + 6) // 12       # 85333 MCT per second

WARNING_FILTER_INCREMENT = 15000
WARNING_FILTER_DECREMENT = 15
WARNING_FILTER_MAX = 140000
WARNING_FILTER_THRESHOLD = 20000

# Extra MCTs per instruction (index = top 5 bits of the instruction word).
INSTRUCTION_TIMING = [0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
EXTRACODE_TIMING = [1, 1, 1, 1, 5, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2,
                    2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 2, 2, 2, 2]


# --- arithmetic helpers (operate on 16-bit "accumulator format" ints) ------
def sign_extend(w: int) -> int:
    """15-bit SP word -> 16-bit value with sign duplicated into bit 16."""
    return (w & 0o77777) | ((w << 1) & 0o100000)


def overflow_corrected(v: int) -> int:
    """16-bit value -> 15-bit word (bit 16 moved down to bit 15)."""
    return (v & 0o37777) | ((v >> 1) & 0o40000)


def value_overflowed(v: int) -> int:
    """+1, -1 or +0 (SP format) depending on overflow in a 16-bit value."""
    t = v & 0o140000
    if t == 0o040000:
        return AGC_P1
    if t == 0o100000:
        return AGC_M1
    return AGC_P0


def add_sp16(a: int, b: int) -> int:
    """Add two 16-bit sign-extended values with end-around carry."""
    s = a + b
    if s & 0o200000:
        s = (s + 1) & 0o177777
    return s


def agc2cpu(w: int) -> int:
    if w & 0o40000:
        return -(0o37777 & ~w)
    return 0o37777 & w


def cpu2agc(v: int) -> int:
    if v < 0:
        return 0o77777 & ~(-v)
    return 0o77777 & v


def agc2cpu2(v: int) -> int:
    if v & 0o2000000000:
        return -(0o1777777777 & ~v)
    return 0o1777777777 & v


def cpu2agc2(v: int) -> int:
    if v < 0:
        return 0o3777777777 & ~(0o1777777777 & (-v))
    return 0o1777777777 & v


def sp_to_decent(msb: int, lsb: int) -> int:
    """Combine a DP pair (two SP words) into one 29-bit one's-complement value."""
    msb &= 0o77777
    lsb &= 0o77777
    if msb in (AGC_P0, AGC_M0):
        v = sign_extend(lsb)
        if v & 0o100000:
            v |= ~0o177777
        return 0o7777777777 & v
    if (lsb & 0o40000) != (msb & 0o40000):
        if lsb in (AGC_P0, AGC_M0):
            lsb = AGC_P0 if not (msb & 0o40000) else AGC_M0
        else:
            complement = msb & 0o40000
            if complement:
                msb = 0o77777 & ~msb
                lsb = 0o77777 & ~lsb
            msb -= 1
            lsb = (lsb + 0o40000 + AGC_P1) & 0o77777
            if complement:
                msb = 0o77777 & ~msb
                lsb = 0o77777 & ~lsb
    v = (0o3777740000 & (msb << 14)) | (0o37777 & lsb)
    if v & 0o2000000000:
        v |= 0o4000000000
    return v


def decent_to_sp(decent: int) -> tuple[int, int]:
    """Inverse of sp_to_decent -> (msb, lsb) as 15-bit words."""
    sign = decent & 0o4000000000
    lsb = 0o37777 & decent
    if sign:
        lsb |= 0o40000
    msb = overflow_corrected(0o177777 & (decent >> 14))
    return msb, lsb


def dabs(w: int) -> int:
    """Diminished absolute value of an SP word."""
    if w & 0o40000:
        w = 0o37777 & ~w
    return w - 1 if w > 1 else AGC_P0


def odabs(v: int) -> int:
    """Diminished absolute value of a 16-bit value."""
    if v & 0o100000:
        v = 0o177777 & ~v
    return v - 1 if v > 1 else AGC_P0


def abs_sp(w: int) -> int:
    return (0o77777 & ~w) if (w & 0o40000) else w


def negate_sp(w: int) -> int:
    return 0o77777 & ~w


# --- counter increments (used by the timers and by simulated hardware) -----
def counter_pinc(v: int) -> tuple[int, bool]:
    if v == 0o37777:
        return AGC_P0, True
    v = (v + 1) & 0o77777
    if v == AGC_P0:
        v += 1
    return v, False


def counter_minc(v: int) -> tuple[int, bool]:
    if v == 0o40000:
        return AGC_M0, True
    v = (v - 1) & 0o77777
    if v == AGC_M0:
        v -= 1
    return v, False


def counter_pcdu(v: int) -> tuple[int, bool]:
    return (v + 1) & 0o77777, v == 0o77777


def counter_mcdu(v: int) -> tuple[int, bool]:
    return (v - 1) & 0o77777, v == 0


def counter_shinc(v: int) -> tuple[int, bool]:
    return (v << 1) & 0o37777, bool(v & 0o20000)


def counter_shanc(v: int) -> tuple[int, bool]:
    return ((v << 1) + 1) & 0o37777, bool(v & 0o20000)


class AGC:
    """The emulated computer.  Memory, registers, channels and the clock."""

    def __init__(self, fixed: list[list[int]], check_alarms: bool = True):
        self.fixed = fixed                         # 36 banks x 1024 words
        self.e = [0] * (8 * 0o400)                 # erasable, flat: bank*256 + offset
        self.chan = [0] * 512                      # input channels / latched outputs
        self.out7 = 0                              # superbank bits (channel 7)
        self.chan10 = [0] * 16                     # DSKY relay rows latched from channel 10
        self.check_alarms = check_alarms
        self.on_channel_write: Callable[[int, int], None] | None = None
        self.on_radar_read: Callable[[int], int] | None = None   # selection (ch13 bits 1-3) -> RNRAD word
        self.reset()

    # ------------------------------------------------------------------
    def reset(self):
        for i in range(len(self.e)):
            self.e[i] = 0
        for i in range(512):
            self.chan[i] = 0
        self.chan[0o30] = 0o37777
        self.chan[0o31] = 0o77777
        self.chan[0o32] = 0o77777
        self.chan[0o33] = 0o77777
        self.out7 = 0
        self.chan10 = [0] * 16
        self.e[Z] = 0o4000
        self.cycles = 0
        self.index_value = 0
        self.extracode = False
        self.allow_interrupt = False
        self.in_isr = False
        self.substitute_instruction = False
        self.pend_flag = False
        self.pend_delay = 0
        self.extra_delay = 0
        self.interrupt_requests = [0] * (NUM_INTERRUPTS + 1)
        self.interrupt_requests[8] = 1             # pending DOWNRUPT, like yaAGC
        self.downrupt_time_valid = False
        self.downrupt_time = 0
        self.downlink = 0
        self.next_z = 0
        self.scaler_counter = 0
        self.dsky_timer = 0
        self.dsky_flash = 0
        self.night_watchman = False
        self.night_watchman_tripped = False
        self.rupt_lock = False
        self.no_rupt = False
        self.tc_trap = False
        self.no_tc = False
        self.standby = False
        self.sby_pressed = False
        self.sby_still_pressed = False
        self.restart_light = True
        self.took_bzf = False
        self.took_bzmf = False
        self.generated_warning = False
        self.warning_filter = 0
        self.trap31a = self.trap31b = self.trap32 = False
        self.radar_gate_counter = 0
        self.alarm_log: list[tuple[int, str]] = []
        self.instructions = 0

    # ------------------------------------------------------------------
    # Save / restore (like yaAGC's core dump): everything except the rope and the hooks
    # ------------------------------------------------------------------
    _NOT_STATE = ("fixed", "on_channel_write", "on_radar_read", "check_alarms")

    def save_state(self) -> dict:
        """Snapshot of the machine state (erasable, channels, registers, timers) as plain
        JSON-compatible data.  The rope and the I/O hooks are not part of it."""
        return {k: copy.deepcopy(v) for k, v in self.__dict__.items() if k not in self._NOT_STATE}

    def load_state(self, state: dict):
        """Restore a snapshot taken with save_state() on an AGC running the same rope.
        The snapshot is checked against the live attributes (names, list lengths, scalar
        types) before anything is changed, so a damaged file raises instead of leaving a
        half-restored machine."""
        wanted = {k: v for k, v in self.__dict__.items() if k not in self._NOT_STATE}
        if set(state) - set(self._NOT_STATE) != set(wanted):
            raise KeyError(f"snapshot fields differ: {sorted(set(state) ^ set(wanted) - set(self._NOT_STATE))}")
        checked = {}
        for k, cur in wanted.items():
            v = state[k]
            if k == "alarm_log":
                v = [(int(c), str(r)) for c, r in v]
            elif isinstance(cur, list):
                if not isinstance(v, list) or len(v) != len(cur) or not all(type(x) is int for x in v):
                    raise TypeError(f"snapshot field {k}: expected a list of {len(cur)} integers")
            elif isinstance(cur, bool):
                if not isinstance(v, bool):
                    raise TypeError(f"snapshot field {k}: expected a bool")
            elif isinstance(cur, int):
                if type(v) is not int:
                    raise TypeError(f"snapshot field {k}: expected an int")
            checked[k] = copy.deepcopy(v)
        for k, v in checked.items():
            setattr(self, k, v)

    # ------------------------------------------------------------------
    # Memory access
    # ------------------------------------------------------------------
    def eaddr(self, addr12: int) -> int:
        """Map a 12-bit erasable address to an index into self.e."""
        if addr12 < 0o1400:
            return addr12
        return ((self.e[EB] >> 8) & 7) * 0o400 + (addr12 & 0o377)

    def fbank(self, addr12: int) -> int:
        """Fixed bank selected for a 12-bit address 2000-7777."""
        if addr12 < 0o4000:
            fb = (self.e[FB] >> 10) & 0o37
            if (fb & 0o30) == 0o30 and (self.out7 & 0o100):
                fb += 0o10
            return fb
        return 2 if addr12 < 0o6000 else 3

    def read(self, addr12: int) -> int:
        """Read a 15-bit word from erasable or fixed memory (no side effects)."""
        addr12 &= 0o7777
        if addr12 < 0o2000:
            if addr12 == 0o67:
                self.night_watchman = False
            return self.e[self.eaddr(addr12)] & 0o77777
        return self.fixed[self.fbank(addr12)][addr12 & 0o1777]

    def read16(self, addr12: int) -> int:
        """Read for the CPU: registers A, L, Q keep their 16th bit."""
        if addr12 < 3:
            return self.e[addr12] & 0o177777
        return self.read(addr12)

    def assign(self, eindex: int, value: int):
        """Write to erasable memory, applying the special register behaviour."""
        if eindex < 0o400:
            if eindex == Z:
                self.next_z = value
            elif eindex == CYR:
                value &= 0o77777
                value = (value >> 1) | 0o40000 if value & 1 else value >> 1
            elif eindex == SR:
                value &= 0o77777
                value = (value >> 1) | 0o40000 if value & 0o40000 else value >> 1
            elif eindex == CYL:
                value &= 0o77777
                value = (value << 1) + 1 if value & 0o40000 else value << 1
            elif eindex == EDOP:
                value = ((value & 0o77777) >> 7) & 0o177
            elif eindex == ZERO:
                value = AGC_P0
            if eindex >= 3 or (0o20 <= eindex <= 0o23):
                self.e[eindex] = value & 0o77777
            else:
                self.e[eindex] = value & 0o177777
        else:
            self.e[eindex] = value & 0o77777

    def write(self, addr12: int, value: int):
        """Write a word to a 12-bit address; writes to fixed memory are ignored."""
        addr12 &= 0o7777
        if addr12 < 0o2000:
            if addr12 == 0o67:
                self.night_watchman = False
            self.assign(self.eaddr(addr12), value)

    # convenience for the UI/tests ---------------------------------------
    def erasable(self, bank: int, offset: int) -> int:
        return self.e[bank * 0o400 + offset] & 0o77777

    def set_erasable(self, bank: int, offset: int, value: int):
        self.e[bank * 0o400 + offset] = value & 0o77777

    def erasable_flat(self, ea: int) -> int:
        """Read by flat erasable address 0..3777 (bank = ea >> 8)."""
        return self.e[ea] & 0o77777

    # ------------------------------------------------------------------
    # I/O channels
    # ------------------------------------------------------------------
    def read_io(self, ch: int) -> int:
        if ch in (L, Q):
            return self.e[ch]
        return self.chan[ch]

    def write_io(self, ch: int, value: int):
        value &= 0o77777
        if ch in (L, Q):
            self.e[ch] = value
        if ch == 7:
            # SUPERBNK: only bits 5-7 exist; selects fixed banks 40-43 instead of 30-33.
            value &= 0o160
            self.out7 = value
        elif ch == 0o10:
            self.chan10[(value >> 11) & 0o17] = value
        elif ch in (0o15, 0o16) and value == 0o22:
            self.restart_light = False          # RSET key clears the RESTART lamp directly
        elif ch == 0o33:
            value = (self.chan[ch] & 0o76000) | (value & 0o1777)
        self.chan[ch] = value

    def cpu_write_io(self, ch: int, value: int):
        if ch == 0o13:
            if value & 0o4000:
                self.trap31a = True
            if value & 0o10000:
                self.trap31b = True
            if value & 0o20000:
                self.trap32 = True
            value &= 0o43777
        if ch == 0o33:
            self.chan[ch] |= 0o76000
            if self.warning_filter > WARNING_FILTER_THRESHOLD:
                self.chan[ch] &= 0o57777
            value = self.chan[ch]
        elif ch == 0o77:
            value = CH77_NIGHT_WATCHMAN if self.night_watchman_tripped else 0
        elif ch == 0o11 and (value & 0o1000):
            self.restart_light = False
        self.write_io(ch, value)
        if self.on_channel_write is not None:
            self.on_channel_write(ch, value & 0o77777)
        if ch == 0o34:
            self.downlink |= 1
        elif ch == 0o35:
            self.downlink |= 2
        if self.downlink == 3:
            self.downrupt_time_valid = True
            self.downrupt_time = self.cycles + CYCLES_PER_SECOND // 50
            self.downlink = 0

    # Peripherals call these -------------------------------------------
    def set_input_channel(self, ch: int, value: int):
        self.chan[ch] = value & 0o77777

    def key_press(self, keycode: int):
        """DSKY key: keycode into channel 15 and raise KEYRUPT1."""
        self.chan[0o15] = keycode & 0o37
        self.interrupt_requests[5] = 1

    def set_proceed_key(self, pressed: bool):
        """PRO (STBY) key is bit 14 of channel 32, active low."""
        if pressed:
            self.chan[0o32] &= ~0o20000
        else:
            self.chan[0o32] |= 0o20000

    def unprogrammed_increment(self, counter: int, inc_type: int):
        """Hardware pulse into a counter register (PINC=0, PCDU=1, MINC=2, MCDU=3, DINC=4, SHINC=5, SHANC=6)."""
        counter &= 0o177
        v = self.e[counter] & 0o77777
        if inc_type == 0:
            v, _ = counter_pinc(v)
        elif inc_type in (1, 0o21):
            v, _ = counter_pcdu(v)
        elif inc_type == 2:
            v, _ = counter_minc(v)
        elif inc_type in (3, 0o23):
            v, _ = counter_mcdu(v)
        elif inc_type == 4:
            v = self._dinc(counter, v)
        elif inc_type == 5:
            v, _ = counter_shinc(v)
        elif inc_type == 6:
            v, _ = counter_shanc(v)
        self.e[counter] = v

    def _dinc(self, counter: int, v: int) -> int:
        """Diminish-increment; emits the P/M/Z-OUT pulses as channel writes 0o200|counter."""
        if v in (AGC_P0, AGC_M0):
            if counter and self.on_channel_write:
                self.on_channel_write(0o200 | counter, 0o17)
            return v
        if v & 0o40000:
            v = add_sp16(sign_extend(v), sign_extend(AGC_P1)) & 0o77777
            if counter and self.on_channel_write:
                self.on_channel_write(0o200 | counter, 0o16)
        else:
            v = add_sp16(sign_extend(v), sign_extend(AGC_M1)) & 0o77777
            if counter and self.on_channel_write:
                self.on_channel_write(0o200 | counter, 0o15)
        return v

    # ------------------------------------------------------------------
    # Interrupt requests from INCR/AUG on timer registers
    # ------------------------------------------------------------------
    def _interrupt_requests(self, addr10: int, total: int):
        if value_overflowed(total) == AGC_P0:
            return
        if addr10 == TIME1:
            v, _ = counter_pinc(self.e[TIME2])
            self.e[TIME2] = v
        elif addr10 == TIME5:
            self.interrupt_requests[2] = 1
        elif addr10 == TIME3:
            self.interrupt_requests[3] = 1
        elif addr10 == TIME4:
            self.interrupt_requests[4] = 1

    # ------------------------------------------------------------------
    # GOJAM (hardware restart)
    # ------------------------------------------------------------------
    def gojam(self, reason: str):
        self.alarm_log.append((self.cycles, reason))
        if len(self.alarm_log) > 200:
            del self.alarm_log[0]
        self.extra_delay += 2
        self.e[Q] = self.e[Z]
        self.e[Z] = 0o4000
        self.in_isr = False
        self.allow_interrupt = True
        self.trap31a = self.trap31b = self.trap32 = False
        for i in range(1, NUM_INTERRUPTS + 1):
            self.interrupt_requests[i] = 0
        for ch in (0o5, 0o6, 0o10, 0o11, 0o12, 0o13, 0o14):
            self.cpu_write_io(ch, 0)
        self.chan[0o33] |= 0o2000
        self.cpu_write_io(0o34, 0)
        self.cpu_write_io(0o35, 0)
        self.downrupt_time_valid = False
        self.index_value = AGC_P0
        self.extracode = False
        self.substitute_instruction = False
        self.pend_flag = False
        self.pend_delay = 0
        self.took_bzf = self.took_bzmf = False
        if not self.standby:
            self.restart_light = True
            self.generated_warning = True

    # ------------------------------------------------------------------
    # Clock / scaler: called once per MCT
    # ------------------------------------------------------------------
    def _scaler_tick(self):
        chan = self.chan
        chan[CHAN_SCALER1] += 1
        if chan[CHAN_SCALER1] == 0o40000:
            chan[CHAN_SCALER1] = 0
            chan[CHAN_SCALER2] = (chan[CHAN_SCALER2] + 1) & 0o37777
        s1 = chan[CHAN_SCALER1]
        triggered = None
        if (s1 & 0o7777) == 0o4000:
            if not self.standby:
                self.night_watchman = True
            if self.sby_pressed and ((chan[0o13] & 0o2000) or self.standby):
                if not self.standby:
                    self.standby = True
                    self.sby_still_pressed = True
                    triggered = "STANDBY"
                elif not self.sby_still_pressed:
                    self.standby = False
        elif (s1 & 0o7777) == 0:
            if 0 == (chan[0o32] & 0o20000):
                self.sby_pressed = True
            if not self.standby and self.night_watchman:
                triggered = "NIGHT WATCHMAN"
                chan[0o77] |= CH77_NIGHT_WATCHMAN
                self.night_watchman_tripped = True
            else:
                self.night_watchman_tripped = False
        elif (s1 & 7) == 0:
            if (s1 & 0o777) == 0o400 and (self.generated_warning or (chan[0o13] & 0o1000)):
                self.generated_warning = False
                self.warning_filter = min(self.warning_filter + WARNING_FILTER_INCREMENT, WARNING_FILTER_MAX)
            else:
                self.warning_filter = max(self.warning_filter - WARNING_FILTER_DECREMENT, 0)
        if not self.standby:
            if (s1 & 0o777) == 0o400:
                self.rupt_lock = True
                self.no_rupt = True
            elif (self.rupt_lock or self.no_rupt) and (s1 & 0o777) == 0o300:
                triggered = "RUPT LOCK" if self.rupt_lock else "NO RUPT"
                chan[0o77] |= CH77_RUPT_LOCK
            if (s1 & 0o37) == 0o20:
                self.tc_trap = True
                self.no_tc = True
            elif (self.tc_trap or self.no_tc) and (s1 & 0o37) == 0:
                triggered = "TC TRAP" if self.tc_trap else "NO TC"
                chan[0o77] |= CH77_TC_TRAP
            e = self.e
            if (s1 & 0o37) == 0o20:
                self.extra_delay += 1
                e[TIME1], ovf = counter_pinc(e[TIME1])
                if ovf:
                    self.extra_delay += 1
                    e[TIME2], _ = counter_pinc(e[TIME2])
                self.extra_delay += 1
                e[TIME3], ovf = counter_pinc(e[TIME3])
                if ovf:
                    self.interrupt_requests[3] = 1
            if (s1 & 0o37) == 0:
                self.extra_delay += 1
                e[TIME5], ovf = counter_pinc(e[TIME5])
                if ovf:
                    self.interrupt_requests[2] = 1
                if chan[0o13] & 0o10:
                    self.radar_gate_counter += 1
            if (s1 & 0o37) == 0o10:
                self.extra_delay += 1
                e[TIME4], ovf = counter_pinc(e[TIME4])
                if ovf:
                    self.interrupt_requests[4] = 1
            if (chan[0o13] & 0o40000) and (s1 & 1) == 1:
                self.extra_delay += 1
                v = e[TIME6] & 0o77777
                if v in (AGC_P0, AGC_M0):
                    self.interrupt_requests[1] = 1
                    self.cpu_write_io(0o13, chan[0o13] & 0o37777)
                else:
                    e[TIME6] = self._dinc(0, v)
            if self.trap31a and (chan[0o31] & 0o77) != 0o77:
                self.trap31a = False
                self.interrupt_requests[10] = 1
            if self.trap31b and (chan[0o31] & 0o7700) != 0o7700:
                self.trap31b = False
                self.interrupt_requests[10] = 1
            if self.trap32 and (chan[0o32] & 0o1777) != 0o1777:
                self.trap32 = False
                self.interrupt_requests[10] = 1
            if self.radar_gate_counter == 9 and (s1 & 0o37) == 0o36:
                # radar cycle complete: the selected radar shifts its data into RNRAD
                self.radar_gate_counter = 0
                if self.on_radar_read is not None:
                    e[RNRAD] = self.on_radar_read(chan[0o13] & 7) & 0o77777
                chan[0o13] &= ~0o10
                self.interrupt_requests[9] = 1
        if triggered is not None:
            if self.check_alarms:
                self.gojam(triggered)
            else:
                self.alarm_log.append((self.cycles, triggered + " (ignored)"))
            if self.on_channel_write:
                self.on_channel_write(0o77, chan[0o77])

    # ------------------------------------------------------------------
    # One machine cycle
    # ------------------------------------------------------------------
    def step(self) -> bool:
        """Advance one MCT.  Returns True when an instruction completed."""
        if self.downrupt_time_valid and self.cycles >= self.downrupt_time:
            self.interrupt_requests[8] = 1
            self.downrupt_time_valid = False
        self.cycles += 1
        self.scaler_counter += SCALER_DIVIDER
        self.dsky_timer += SCALER_DIVIDER

        if self.extra_delay:
            self.extra_delay -= 1
            return False
        if self.pend_flag and self.pend_delay > 0:
            self.pend_delay -= 1
            return False
        if self.chan[0o32] & 0o20000:
            self.sby_pressed = False
            self.sby_still_pressed = False
        if self.scaler_counter >= SCALER_OVERFLOW:
            self.scaler_counter -= SCALER_OVERFLOW
            self._scaler_tick()
            if self.extra_delay:
                self.extra_delay -= 1
                return False
        if self.standby:
            return False
        return self._execute()

    def _execute(self) -> bool:
        e = self.e
        current_eb, current_fb, current_bb = e[EB], e[FB], e[BB]
        accumulator = e[A] & 0o177777
        overflow = value_overflowed(accumulator) != AGC_P0
        pc = e[Z] & 0o7777
        if self.substitute_instruction:
            instruction = e[BRUPT]
        else:
            word = self.read(pc)
            instruction = overflow_corrected(add_sp16(sign_extend(self.index_value), sign_extend(word)))
        instruction &= 0o77777
        extended_opcode = instruction >> 9
        if self.extracode:
            extended_opcode |= 0o100
        quarter_code = instruction & ~0o1777
        addr12 = instruction & 0o7777
        addr10 = instruction & 0o1777
        addr9 = instruction & 0o777
        executed_tc = False
        tc_transient = False
        just_bzf = just_bzmf = False
        keep_extracode = False

        # Interrupts ---------------------------------------------------
        if ((not self.in_isr and self.allow_interrupt and not self.extracode
             and not self.pend_flag and not overflow and instruction not in (3, 4, 6))
                or extended_opcode == 0o107):
            requested = False
            for i in range(1, NUM_INTERRUPTS + 1):
                if self.interrupt_requests[i]:
                    self.interrupt_requests[i] = 0
                    self.interrupt_requests[0] = i
                    self.next_z = 0o4000 + 4 * i
                    requested = True
                    break
            if not requested and extended_opcode == 0o107:
                self.next_z = 0
                requested = True
            if requested:
                e[ZRUPT] = (pc + 1) & 0o77777
                e[BRUPT] = instruction
                self.extracode = False
                self.index_value = AGC_P0
                self.substitute_instruction = False
                self.in_isr = True
                self.extra_delay += 1
                self._finish(current_eb, current_fb, current_bb, keep_extracode, executed_tc, tc_transient, just_bzf, just_bzmf)
                return True

        # Multi-MCT instruction timing ---------------------------------
        if not self.pend_flag:
            i = quarter_code >> 10
            t = EXTRACODE_TIMING[i] if self.extracode else INSTRUCTION_TIMING[i]
            if t:
                self.pend_flag = True
                self.pend_delay = t - 1
                return False
        else:
            self.pend_flag = False

        self.index_value = AGC_P0
        self.substitute_instruction = False
        self.next_z = 1 + e[Z]
        e[Z] = self.next_z
        if self.took_bzf and not (extended_opcode == 0 and addr12 == 6):
            tc_transient = True
        self.instructions += 1

        op = extended_opcode
        # --------------------------------------------------------------
        if op < 0o10:                                   # TC
            k = addr12
            if k == 3:                                  # RELINT
                self.allow_interrupt = True
                if self.took_bzf or self.took_bzmf:
                    tc_transient = True
            elif k == 4:                                # INHINT
                self.allow_interrupt = False
                if self.took_bzf or self.took_bzmf:
                    tc_transient = True
            elif k == 6:                                # EXTEND
                self.extracode = True
                keep_extracode = True
            else:
                if k != Q:                              # not RETURN
                    e[Q] = 0o177777 & self.next_z
                self.next_z = addr12
                executed_tc = True
        elif op < 0o12:                                 # CCS
            if addr10 < 3:
                vk = 0o177777 & e[addr10]
                operand = overflow_corrected(vk)
                e[A] = odabs(vk)
                ovf = value_overflowed(vk)
                if ovf == AGC_P1:
                    pass
                elif ovf == AGC_M1:
                    self.next_z += 2
                elif operand == AGC_P0:
                    self.next_z += 1
                elif operand == AGC_M0:
                    self.next_z += 3
                elif operand & 0o40000:
                    self.next_z += 2
            else:
                operand = self.read(addr10) & 0o77777
                e[A] = dabs(operand)
                if addr10 < 0o2000:
                    self.write(addr10, operand)     # re-assign for editing registers
                if operand == AGC_P0:
                    self.next_z += 1
                elif operand == AGC_M0:
                    self.next_z += 3
                elif operand & 0o40000:
                    self.next_z += 2
        elif op < 0o20:                                 # TCF
            self.next_z = addr12
            executed_tc = True
        elif op < 0o22:                                 # DAS
            if addr10 == L:                             # DDOUBL
                lsw = add_sp16(0o177777 & e[L], 0o177777 & e[L])
                msw = add_sp16(accumulator, accumulator)
                if (0o140000 & lsw) == 0o040000:
                    msw = add_sp16(msw, AGC_P1)
                elif (0o140000 & lsw) == 0o100000:
                    msw = add_sp16(msw, sign_extend(AGC_M1))
                lsw = overflow_corrected(lsw)
                e[A] = 0o177777 & msw
                e[L] = 0o177777 & sign_extend(lsw)
            else:
                if addr10 < 3:
                    lsw = add_sp16(0o177777 & e[L], 0o177777 & e[addr10])
                else:
                    lsw = add_sp16(0o177777 & e[L], sign_extend(self.read(addr10)))
                if addr10 < 4:
                    msw = add_sp16(accumulator, 0o177777 & e[addr10 - 1])
                else:
                    msw = add_sp16(accumulator, sign_extend(self.read(addr10 - 1)))
                if (0o140000 & lsw) == 0o040000:
                    msw = add_sp16(msw, AGC_P1)
                elif (0o140000 & lsw) == 0o100000:
                    msw = add_sp16(msw, sign_extend(AGC_M1))
                lsw = overflow_corrected(lsw)
                if (0o140000 & msw) == 0o100000:
                    e[A] = sign_extend(AGC_M1)
                elif (0o140000 & msw) == 0o040000:
                    e[A] = AGC_P1
                else:
                    e[A] = AGC_P0
                e[L] = AGC_P0
                if addr10 < 3:
                    e[addr10] = sign_extend(lsw)
                else:
                    self.write(addr10, lsw)
                if addr10 < 4:
                    e[addr10 - 1] = msw
                else:
                    self.write(addr10 - 1, overflow_corrected(msw))
        elif op < 0o24:                                 # LXCH
            if addr10 == L:
                pass
            elif addr10 == ZERO:                        # ZL
                e[L] = AGC_P0
            elif addr10 < 3:
                tmp = e[L]
                e[L] = e[addr10]
                e[addr10] = tmp
                if addr10 == Z:
                    self.next_z = e[Z]
            else:
                tmp = self.read(addr10)
                self.write(addr10, overflow_corrected(0o177777 & e[L]))
                e[L] = sign_extend(tmp)
        elif op < 0o26:                                 # INCR
            if addr10 < 3:
                e[addr10] = add_sp16(AGC_P1, 0o177777 & e[addr10])
            else:
                total = add_sp16(AGC_P1, sign_extend(self.read(addr10)))
                self.write(addr10, overflow_corrected(total))
                self._interrupt_requests(addr10, total)
        elif op < 0o30:                                 # ADS
            if addr10 == A:
                accumulator = add_sp16(accumulator, accumulator)
            elif addr10 < 3:
                accumulator = add_sp16(accumulator, 0o177777 & e[addr10])
            else:
                accumulator = add_sp16(accumulator, sign_extend(self.read(addr10)))
            e[A] = accumulator
            if addr10 == A:
                pass
            elif addr10 < 3:
                e[addr10] = accumulator
            else:
                self.write(addr10, overflow_corrected(accumulator))
        elif op < 0o40:                                 # CA
            if addr12 == A:
                pass
            elif addr12 < 3:
                e[A] = e[addr12]
            else:
                w = self.read(addr12)
                e[A] = sign_extend(w)
                if addr12 < 0o2000:
                    self.write(addr12, w)
        elif op < 0o50:                                 # CS
            tc_transient = True
            if addr12 == A:
                e[A] = (~accumulator) & 0o177777
            elif addr12 < 3:
                e[A] = (~e[addr12]) & 0o177777
            else:
                w = self.read(addr12)
                e[A] = sign_extend(negate_sp(w))
                if addr12 < 0o2000:
                    self.write(addr12, w)
        elif op < 0o52:                                 # INDEX
            if addr10 == 0o17:
                self._resume()
            elif addr10 < 3:
                self.index_value = overflow_corrected(e[addr10])
            else:
                self.index_value = self.read(addr10)
        elif op < 0o54:                                 # DXCH
            tc_transient = True
            if addr10 == L:
                e[L] = sign_extend(overflow_corrected(e[L]))
            else:
                if addr10 < 3:
                    tmp = e[addr10]
                    e[addr10] = e[L]
                    e[L] = tmp
                    if addr10 == Z:
                        self.next_z = e[Z]
                else:
                    tmp = sign_extend(self.read(addr10))
                    self.write(addr10, overflow_corrected(e[L]))
                    e[L] = tmp
                e[L] = sign_extend(overflow_corrected(e[L]))
                if addr10 < 4:
                    tmp = e[addr10 - 1]
                    e[addr10 - 1] = e[A]
                    e[A] = tmp
                    if addr10 == Z + 1:
                        self.next_z = e[Z]
                else:
                    tmp = sign_extend(self.read(addr10 - 1))
                    self.write(addr10 - 1, overflow_corrected(e[A]))
                    e[A] = tmp
        elif op < 0o56:                                 # TS
            tc_transient = True
            if addr10 == A:                             # OVSK
                if overflow:
                    self.next_z += AGC_P1
            elif addr10 == Z:                           # TCAA
                self.next_z = 0o77777 & accumulator
                if overflow:
                    e[A] = sign_extend(value_overflowed(accumulator))
            else:
                if addr10 < 3:
                    e[addr10] = accumulator
                else:
                    self.write(addr10, overflow_corrected(accumulator))
                if overflow:
                    e[A] = sign_extend(value_overflowed(accumulator))
                    self.next_z += AGC_P1
        elif op < 0o60:                                 # XCH
            tc_transient = True
            if addr10 == A:
                pass
            elif addr10 < 3:
                e[A] = e[addr10]
                e[addr10] = accumulator
                if addr10 == Z:
                    self.next_z = e[Z]
            else:
                w = self.read(addr10)
                e[A] = sign_extend(w)
                self.write(addr10, overflow_corrected(accumulator))
        elif op < 0o70:                                 # AD
            if addr12 == A:
                accumulator = add_sp16(accumulator, accumulator)
            elif addr12 < 3:
                accumulator = add_sp16(accumulator, 0o177777 & e[addr12])
            else:
                w = self.read(addr12)
                accumulator = add_sp16(accumulator, sign_extend(w))
                if addr12 < 0o2000:
                    self.write(addr12, w)
            e[A] = accumulator
        elif op < 0o100:                                # MASK
            if addr12 < 3:
                e[A] = accumulator & e[addr12]
            else:
                e[A] = sign_extend(overflow_corrected(accumulator) & self.read(addr12))
        # ---------------- extracodes ----------------------------------
        elif op == 0o100:                               # READ
            if addr9 in (L, Q):
                e[A] = e[addr9]
            else:
                e[A] = sign_extend(self.read_io(addr9))
        elif op == 0o101:                               # WRITE
            if addr9 in (L, Q):
                e[addr9] = accumulator
            else:
                self.cpu_write_io(addr9, overflow_corrected(accumulator))
        elif op == 0o102:                               # RAND
            if addr9 in (L, Q):
                e[A] = accumulator & e[addr9]
            else:
                e[A] = sign_extend(overflow_corrected(accumulator) & self.read_io(addr9))
        elif op == 0o103:                               # WAND
            if addr9 in (L, Q):
                e[A] = e[addr9] = accumulator & e[addr9]
            else:
                v = overflow_corrected(accumulator) & self.read_io(addr9)
                self.cpu_write_io(addr9, v)
                e[A] = sign_extend(v)
        elif op == 0o104:                               # ROR
            if addr9 in (L, Q):
                e[A] = accumulator | e[addr9]
            else:
                e[A] = sign_extend(overflow_corrected(accumulator) | self.read_io(addr9))
        elif op == 0o105:                               # WOR
            if addr9 in (L, Q):
                e[A] = e[addr9] = accumulator | e[addr9]
            else:
                v = overflow_corrected(accumulator) | self.read_io(addr9)
                self.cpu_write_io(addr9, v)
                e[A] = sign_extend(v)
        elif op == 0o106:                               # RXOR
            if addr9 in (L, Q):
                e[A] = accumulator ^ e[addr9]
            else:
                e[A] = sign_extend(overflow_corrected(accumulator) ^ self.read_io(addr9))
        elif op == 0o107:                               # EDRUPT (handled as interrupt above)
            pass
        elif op < 0o112:                                # DV
            self._dv(addr10, accumulator)
        elif op < 0o120:                                # BZF
            if accumulator == 0 or accumulator == 0o177777:
                self.next_z = addr12
                just_bzf = True
        elif op < 0o122:                                # MSU
            if addr10 < 3:
                ui = 0o177777 & accumulator
                uj = 0o177777 & ~e[addr10]
            else:
                ui = 0o77777 & overflow_corrected(accumulator)
                uj = 0o77777 & ~self.read(addr10)
            diff = ui + uj + 1
            if diff & 0o40000:
                diff |= 0o100000
                diff -= 1
            if addr10 == Q:
                e[A] = 0o177777 & diff
            else:
                e[A] = sign_extend(0o77777 & diff)
            if 0o20 <= addr10 <= 0o23:
                self.write(addr10, self.read(addr10))
        elif op < 0o124:                                # QXCH
            if addr10 == Q:
                pass
            elif addr10 == ZERO:                        # ZQ
                e[Q] = AGC_P0
            elif addr10 < 3:
                tmp = e[Q]
                e[Q] = e[addr10]
                e[addr10] = tmp
                if addr10 == Z:
                    self.next_z = e[Z]
            else:
                tmp = overflow_corrected(e[Q])
                e[Q] = sign_extend(self.read(addr10))
                self.write(addr10, tmp)
        elif op < 0o126:                                # AUG
            if addr10 < 3:
                operand = e[addr10]
            else:
                operand = sign_extend(self.read(addr10))
            operand &= 0o177777
            inc = AGC_P1 if not (operand & 0o100000) else sign_extend(AGC_M1)
            total = add_sp16(0o177777 & inc, operand)
            if addr10 < 3:
                e[addr10] = total
            else:
                self.write(addr10, overflow_corrected(total))
                self._interrupt_requests(addr10, total)
        elif op < 0o130:                                # DIM
            if addr10 < 3:
                operand = e[addr10]
            else:
                operand = sign_extend(self.read(addr10))
            operand &= 0o177777
            if operand not in (AGC_P0, sign_extend(AGC_M0)):
                inc = sign_extend(AGC_M1) if not (operand & 0o100000) else AGC_P1
                total = add_sp16(0o177777 & inc, operand)
                if addr10 < 3:
                    e[addr10] = total
                else:
                    self.write(addr10, overflow_corrected(total))
        elif op < 0o140:                                # DCA
            if addr12 == L:
                e[L] = sign_extend(overflow_corrected(e[L]))
            else:
                if addr12 < 3:
                    e[L] = e[addr12]
                else:
                    e[L] = sign_extend(self.read(addr12))
                e[L] = sign_extend(overflow_corrected(e[L]))
                if addr12 < 4:
                    e[A] = e[addr12 - 1]
                else:
                    e[A] = sign_extend(self.read(addr12 - 1))
                if 0o20 <= addr12 <= 0o23:
                    self.write(addr12, self.read(addr12))
                if 0o21 <= addr12 <= 0o24:
                    self.write(addr12 - 1, self.read(addr12 - 1))
        elif op < 0o150:                                # DCS
            if addr12 == L:                             # DCOM
                e[A] = (~accumulator) & 0o177777
                e[L] = (~e[L]) & 0o177777
                e[L] = sign_extend(overflow_corrected(e[L]))
            else:
                if addr12 < 3:
                    e[L] = (~e[addr12]) & 0o177777
                else:
                    e[L] = (~sign_extend(self.read(addr12))) & 0o177777
                e[L] = sign_extend(overflow_corrected(e[L]))
                if addr12 < 4:
                    e[A] = (~e[addr12 - 1]) & 0o177777
                else:
                    e[A] = (~sign_extend(self.read(addr12 - 1))) & 0o177777
                if 0o20 <= addr12 <= 0o23:
                    self.write(addr12, self.read(addr12))
                if 0o21 <= addr12 <= 0o24:
                    self.write(addr12 - 1, self.read(addr12 - 1))
        elif op < 0o160:                                # INDEX (extended)
            if addr12 == 0o17 << 1:
                self._resume()
            else:
                if addr12 < 3:
                    self.index_value = overflow_corrected(e[addr12])
                else:
                    self.index_value = self.read(addr12)
                keep_extracode = True
        elif op < 0o162:                                # SU
            if addr10 == A:
                accumulator = sign_extend(AGC_M0)
            elif addr10 < 3:
                accumulator = add_sp16(accumulator, 0o177777 & ~e[addr10])
            else:
                w = self.read(addr10)
                accumulator = add_sp16(accumulator, sign_extend(negate_sp(w)))
                if addr10 < 0o2000:
                    self.write(addr10, w)
            e[A] = accumulator
        elif op < 0o170:                                # BZMF
            if accumulator == 0 or (accumulator & 0o100000):
                self.next_z = addr12
                just_bzmf = True
        else:                                           # MP
            operand = overflow_corrected(accumulator)
            if addr12 < 3:
                other = overflow_corrected(e[addr12])
            else:
                other = self.read(addr12)
            if other in (AGC_P0, AGC_M0):
                ms = ls = AGC_P0
            elif operand in (AGC_P0, AGC_M0):
                if (operand == AGC_P0 and (other & 0o40000)) or (operand == AGC_M0 and not (other & 0o40000)):
                    ms = ls = AGC_M0
                else:
                    ms = ls = AGC_P0
            else:
                product = agc2cpu(sign_extend(operand)) * agc2cpu(sign_extend(other))
                product = cpu2agc2(product)
                if product & 0o2000000000:
                    product |= 0o4000000000
                ms, ls = decent_to_sp(product)
            e[A] = sign_extend(ms)
            e[L] = sign_extend(ls)

        self._finish(current_eb, current_fb, current_bb, keep_extracode, executed_tc, tc_transient, just_bzf, just_bzmf)
        return True

    def _resume(self):
        self.next_z = self.e[ZRUPT] - 1
        self.in_isr = False
        self.substitute_instruction = True

    def _finish(self, current_eb, current_fb, current_bb, keep_extracode, executed_tc, tc_transient, just_bzf, just_bzmf):
        e = self.e
        if not self.pend_flag:
            e[ZERO] = AGC_P0
            self.out7 &= 0o160
            self.chan[7] = self.out7
            e[Z] = self.next_z
            if not self.substitute_instruction:
                e[Z] &= 0o7777
            if not keep_extracode:
                self.extracode = False
            if current_bb != e[BB]:
                e[FB] = e[BB] & 0o76000
                e[EB] = (e[BB] & 7) << 8
            elif current_eb != e[EB] or current_fb != e[FB]:
                e[BB] = (e[FB] & 0o76000) | ((e[EB] & 0o3400) >> 8)
            e[EB] &= 0o3400
            e[FB] &= 0o76000
            e[BB] &= 0o76007
            e[L] = sign_extend(overflow_corrected(e[L]))
            if self.in_isr:
                self.no_rupt = False
            else:
                self.rupt_lock = False
            if executed_tc or tc_transient:
                self.no_tc = False
            if not executed_tc:
                self.tc_trap = False
            self.took_bzf = just_bzf
            self.took_bzmf = just_bzmf

    # ------------------------------------------------------------------
    def _dv(self, addr10: int, accumulator: int):
        e = self.e
        acc0 = overflow_corrected(accumulator)
        acc1 = e[L] & 0o77777
        dividend = sp_to_decent(acc0, acc1)
        acc0, acc1 = decent_to_sp(dividend)
        abs_a = abs_sp(acc0)
        abs_l = abs_sp(acc1)
        if addr10 == A:
            div16 = e[A]
            if (e[A] & 0o100000) == 0:
                div16 = 0o177777 & ~div16
        elif addr10 == L:
            div16 = e[L]
            if (abs_a == 0 and (e[L] & 0o100000)) or (abs_a != 0 and (e[A] & 0o100000)):
                div16 = 0o177777 & ~div16
            div16 = sign_extend(overflow_corrected(add_sp16(div16 & 0o177777, 0o40000)))
        elif addr10 == Z:
            div16 = e[Z]
            if (abs_a == 0 and (e[L] & 0o100000)) or (abs_a != 0 and (e[A] & 0o100000)):
                div16 |= 0o100000
        elif addr10 < 3:
            div16 = e[addr10]
        else:
            div16 = sign_extend(self.read(addr10))
        abs_k = abs_sp(overflow_corrected(div16))
        if abs_a > abs_k or (abs_a == abs_k and abs_l != AGC_P0) or value_overflowed(div16) != AGC_P0:
            self._simulate_dv(div16)
        elif abs_a == 0 and abs_l == 0:
            if (0o40000 & e[L]) == (0o40000 & overflow_corrected(div16)):
                v = 0o37777 if abs_k == 0 else AGC_P0
            else:
                v = (0o77777 & ~0o37777) if abs_k == 0 else AGC_M0
            e[A] = sign_extend(v)
        elif abs_a == abs_k and abs_l == AGC_P0:
            v = 0o37777 if acc0 == overflow_corrected(div16) else (0o77777 & ~0o37777)
            e[L] = sign_extend(acc0)
            e[A] = sign_extend(v)
        else:
            dvd = agc2cpu2(dividend)
            dvs = agc2cpu(overflow_corrected(div16))
            quotient = abs(dvd) // abs(dvs)
            if (dvd < 0) != (dvs < 0):
                quotient = -quotient
            remainder = dvd - quotient * dvs
            e[A] = sign_extend(cpu2agc(quotient))
            if remainder == 0:
                e[L] = AGC_P0 if dvd >= 0 else sign_extend(AGC_M0)
            else:
                e[L] = sign_extend(cpu2agc(remainder))

    def _simulate_dv(self, divisor: int):
        """Register-level model of the hardware divide for the out-of-range cases."""
        e = self.e
        a = e[A] & 0o177777
        l = e[L] & 0o177777
        dividend_sign = a & 0o100000
        if not dividend_sign:
            a = (~a) & 0o177777
        if a == 0o177777:
            dividend_sign = l & 0o100000
        if dividend_sign:
            l = (~l) & 0o177777
        l = add_sp16(l, 0o40000)
        if value_overflowed(l) != AGC_P1:
            a = add_sp16(a, 1)
        remainder = a
        divisor &= 0o177777
        divisor_sign = divisor & 0o100000
        if divisor_sign:
            divisor = (~divisor) & 0o177777
        quotient_sign = l & 0o100000
        quotient = quotient_sign | ((l & 0o37777) << 1) | (quotient_sign >> 15)
        for _ in range(14):
            quotient = (quotient << 1) & 0o177777
            remainder_sign = remainder & 0o100000
            remainder = remainder_sign | ((remainder & 0o37777) << 1)
            if (quotient & 0o100000) == 0:
                remainder |= remainder_sign >> 15
            total = add_sp16(remainder, divisor)
            if total & 0o100000:
                quotient |= 1
                remainder = total
        a = quotient_sign | (quotient & 0o77777)
        e[A] = ((~a) & 0o177777) if dividend_sign != divisor_sign else a
        e[L] = remainder if dividend_sign else ((~remainder) & 0o177777)

    # ------------------------------------------------------------------
    # Running
    # ------------------------------------------------------------------
    def run(self, cycles: int) -> int:
        """Run ``cycles`` MCTs; returns number of instructions completed."""
        step = self.step
        n = 0
        for _ in range(cycles):
            if step():
                n += 1
        return n

    def run_instructions(self, count: int, breakpoints: set[int] | None = None) -> int:
        """Execute ``count`` instructions (bounded in cycles).  Stops at a breakpoint (12-bit Z)."""
        done = 0
        limit = count * 12 + 64
        while done < count and limit > 0:
            limit -= 1
            if self.step():
                done += 1
                if breakpoints and (self.e[Z] & 0o7777) in breakpoints:
                    break
        return done

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------
    @property
    def z(self) -> int:
        return self.e[Z] & 0o7777

    def current_location(self) -> tuple[int, int] | None:
        """(bank, offset) of the next instruction when it is in fixed memory."""
        z = self.e[Z] & 0o7777
        if z < 0o2000:
            return None
        return self.fbank(z), z & 0o1777

    def registers(self) -> dict[str, int]:
        e = self.e
        return {
            "A": e[A] & 0o177777, "L": e[L] & 0o177777, "Q": e[Q] & 0o177777,
            "EB": e[EB], "FB": e[FB], "Z": e[Z] & 0o7777, "BB": e[BB],
            "TIME1": e[TIME1], "TIME2": e[TIME2], "TIME3": e[TIME3], "TIME4": e[TIME4],
            "TIME5": e[TIME5], "TIME6": e[TIME6],
        }

    @property
    def seconds(self) -> float:
        return self.cycles / CYCLES_PER_SECOND
