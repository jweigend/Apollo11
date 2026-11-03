"""MAIN.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/MAIN.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages  of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('MAIN', 'MAIN.agc', 'Luminary099', pages='')
W = MODULE.W
S = MODULE.S

# p.  89 is a GAP-generated table
# pp. 1511-1743: GAP-generated tables.
