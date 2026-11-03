"""Known transcription errors in the GitHub copy of the Apollo 11 source.

The chrislgarry/Apollo-11 repository is a transcription of the scanned
program listings.  Comparing the assembled rope against the octal listing
recovered from the printouts (Virtual AGC ``*.binsource``) revealed a handful
of typos that change the generated code.  They are corrected here, on the
fly, while the source is read, so the original files stay untouched.

Each entry: ``file -> [(line_number, expected_substring, replacement)]``.
The substring must be present in that line, otherwise the fixup is skipped
and reported, so a changed upstream file cannot be silently mis-patched.
"""

FIXUPS: dict[str, dict[str, list[tuple[int, str, str]]]] = {
    "Comanche055": {
        # "1.08-2" is a scanning error for "1.0 B-2" (= 0.25, rope words 10000 00000).
        "P32-P33_P72-P73.agc": [(648, "1.08-2", "1.0 B-2")],
        # Label misspelled; ANGLFIND.agc refers to ZEROEROR (sic, as in the original).
        "KALCMANU_STEERING.agc": [(248, "ZEROERROR", "ZEROEROR")],
        # Label misspelled; the interpretive operand a few lines above says GETLEWD.
        "REENTRY_CONTROL.agc": [(737, "GETDLEWD", "GETLEWD")],
        # Continuation of a comment lost its '#', so "-16" became an opcode and
        # shifted ALTVAR by one word.
        "ERASABLE_ASSIGNMENTS.agc": [(2094, "-16", "#  -16")],
    },
    "Luminary099": {
        # (no word-changing typos found; the tab-indented "+2"/"+3" pseudo-labels in
        # TRIM_GIMBAL_CONTROL_SYSTEM.agc and SERVICER.agc are handled by the parser)
    },
}
