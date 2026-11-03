"""DSKY (Display and Keyboard) model.

The AGC drives the DSKY through I/O channels:

* channel 010: display relays.  Bits 15-12 select one of 12 relay rows, bit 11
  is a sign, bits 10-6 and 5-1 are two 5-bit digit codes.
* channel 011: lamps (COMP ACTY, UPLINK ACTY, TEMP, KEY REL, flash, OPR ERR).
* channel 013: bit 10 lights RESTART and STBY for the lamp test.
* channel 015: key code of the pressed key (raises KEYRUPT1).
* channel 032 bit 14: PRO key (active low).

This module decodes those channels into something a UI can show and maps
key names to key codes.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .cpu import AGC

DIGIT_CODES = {
    0o00: " ",
    0o25: "0", 0o03: "1", 0o31: "2", 0o33: "3", 0o17: "4",
    0o36: "5", 0o34: "6", 0o23: "7", 0o35: "8", 0o37: "9",
}

KEY_CODES = {
    "0": 0o20, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "VERB": 0o21, "RSET": 0o22, "KEY REL": 0o31, "+": 0o32, "-": 0o33,
    "ENTR": 0o34, "CLR": 0o36, "NOUN": 0o37,
}
KEY_ALIASES = {"V": "VERB", "N": "NOUN", "E": "ENTR", "ENTER": "ENTR", "R": "RSET", "RESET": "RSET",
               "C": "CLR", "CLEAR": "CLR", "K": "KEY REL", "KEYREL": "KEY REL", "P": "PRO", "PROCEED": "PRO"}

FLASH_PERIOD_CYCLES = int(1.28 * 85333)   # 1.28 s flash period, 75 % duty cycle


@dataclass
class DSKYState:
    prog: str = "  "
    verb: str = "  "
    noun: str = "  "
    r1: str = "      "
    r2: str = "      "
    r3: str = "      "
    flashing: bool = False
    lamps: dict[str, bool] = field(default_factory=dict)


class DSKY:
    """Decodes the AGC's display channels and feeds key presses back."""

    LAMP_NAMES = ["UPLINK ACTY", "NO ATT", "STBY", "KEY REL", "OPR ERR", "TEMP", "GIMBAL LOCK",
                  "PROG", "RESTART", "TRACKER", "ALT", "VEL", "COMP ACTY", "NO DAP", "PRIO DISP"]

    def __init__(self, cpu: AGC):
        self.cpu = cpu
        self.rows = [0] * 16          # latched channel-10 words by relay row
        self.key_log: list[str] = []
        self.pro_pressed = False
        prev = cpu.on_channel_write
        self._prev_hook = prev
        cpu.on_channel_write = self._on_channel_write

    def _on_channel_write(self, ch: int, value: int):
        if ch == 0o10:
            self.rows[(value >> 11) & 0o17] = value
        if self._prev_hook:
            self._prev_hook(ch, value)

    # -- input ------------------------------------------------------------
    def press(self, key: str):
        """Press a DSKY key by name ("VERB", "3", "ENTR", "PRO", ...)."""
        k = key.upper().strip()
        k = KEY_ALIASES.get(k, k)
        self.key_log.append(k)
        if k == "PRO":
            # PRO is a level signal; the AGC samples it.  Pulse it for a while.
            self.cpu.set_proceed_key(True)
            self.pro_pressed = True
            return
        code = KEY_CODES.get(k)
        if code is None:
            raise ValueError(f"unknown key {key!r}")
        self.cpu.key_press(code)

    def release_pro(self):
        if self.pro_pressed:
            self.cpu.set_proceed_key(False)
            self.pro_pressed = False

    def type_sequence(self, text: str):
        """Press keys from a compact string, e.g. "V35E" or "V16N36E"."""
        for ch in text.replace(" ", ""):
            self.press(ch)

    # -- output -----------------------------------------------------------
    @staticmethod
    def _digits(word: int) -> tuple[str, str]:
        hi = DIGIT_CODES.get((word >> 5) & 0o37, "?")
        lo = DIGIT_CODES.get(word & 0o37, "?")
        return hi, lo

    def state(self, flash: bool = True) -> DSKYState:
        """Decode the display.  ``flash=False`` ignores the VERB/NOUN flashing
        (useful for tests and logs that should not depend on the flash phase)."""
        rows = self.rows
        cpu = self.cpu
        flash_off = False
        if flash and cpu.chan[0o11] & 0o40:            # V/N FLASH
            phase = (cpu.cycles % FLASH_PERIOD_CYCLES) / FLASH_PERIOD_CYCLES
            flash_off = phase > 0.75
        d = DSKYState()
        m1, m2 = self._digits(rows[0o13])
        d.prog = m1 + m2
        v1, v2 = self._digits(rows[0o12])
        n1, n2 = self._digits(rows[0o11])
        d.verb = "  " if flash_off else v1 + v2
        d.noun = "  " if flash_off else n1 + n2
        _, r1d1 = self._digits(rows[0o10])
        r1d2, r1d3 = self._digits(rows[0o7])
        r1d4, r1d5 = self._digits(rows[0o6])
        r2d1, r2d2 = self._digits(rows[0o5])
        r2d3, r2d4 = self._digits(rows[0o4])
        r2d5, r3d1 = self._digits(rows[0o3])
        r3d2, r3d3 = self._digits(rows[0o2])
        r3d4, r3d5 = self._digits(rows[0o1])

        def sign(plus_row: int, minus_row: int) -> str:
            plus = bool(rows[plus_row] & 0o2000)
            minus = bool(rows[minus_row] & 0o2000)
            if plus and not minus:
                return "+"
            if minus and not plus:
                return "-"
            return " "

        d.r1 = sign(0o7, 0o6) + r1d1 + r1d2 + r1d3 + r1d4 + r1d5
        d.r2 = sign(0o5, 0o4) + r2d1 + r2d2 + r2d3 + r2d4 + r2d5
        d.r3 = sign(0o2, 0o1) + r3d1 + r3d2 + r3d3 + r3d4 + r3d5

        c11 = cpu.chan[0o11]
        c13 = cpu.chan[0o13]
        row12 = rows[0o14]
        lamp_test = bool(c13 & 0o1000)
        keyrel = bool(c11 & 0o20)
        oprerr = bool(c11 & 0o100)
        if flash_off:
            keyrel = oprerr = False
        d.flashing = bool(cpu.chan[0o11] & 0o40)
        d.lamps = {
            "UPLINK ACTY": bool(c11 & 0o4),
            "NO ATT": bool(row12 & 0o10),
            "STBY": cpu.standby or lamp_test,
            "KEY REL": keyrel,
            "OPR ERR": oprerr,
            "TEMP": bool(c11 & 0o10) or bool(cpu.chan[0o30] & 0o40000),
            "GIMBAL LOCK": bool(row12 & 0o40),
            "PROG": bool(row12 & 0o400),
            "RESTART": cpu.restart_light or lamp_test,
            "TRACKER": bool(row12 & 0o200),
            "ALT": bool(row12 & 0o20),
            "VEL": bool(row12 & 0o4),
            "COMP ACTY": bool(c11 & 0o2),
            "NO DAP": bool(row12 & 0o2),
            "PRIO DISP": bool(row12 & 0o1),
        }
        return d

    def render(self) -> list[str]:
        """A plain-text picture of the DSKY for terminals and logs."""
        s = self.state()
        on = {k: v for k, v in s.lamps.items()}

        def lamp(name: str, width: int = 11) -> str:
            text = name.center(width)
            return f"[{text}]" if on.get(name) else f" {text} "

        lines = [
            f"{lamp('UPLINK ACTY')} {lamp('TEMP')}      COMP     PROG",
            f"{lamp('NO ATT')} {lamp('GIMBAL LOCK')}     ACTY     {s.prog}",
            f"{lamp('STBY')} {lamp('PROG')}      {'[##]' if on.get('COMP ACTY') else '    '}",
            f"{lamp('KEY REL')} {lamp('RESTART')}     VERB     NOUN",
            f"{lamp('OPR ERR')} {lamp('TRACKER')}      {s.verb}       {s.noun}",
            f"{lamp('NO DAP')} {lamp('ALT')}     R1  {s.r1}",
            f"{lamp('PRIO DISP')} {lamp('VEL')}     R2  {s.r2}",
            f"{'':13} {'':13}     R3  {s.r3}",
        ]
        return lines
