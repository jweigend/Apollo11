"""MAIN.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/MAIN.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages  of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('MAIN', 'MAIN.agc', 'Comanche055', pages='')
W = MODULE.W
S = MODULE.S


# p. 36 contains no code.
# COMERASE

# COMAID

# COMEKISS

# TROUBLE

# TVCDAPS

# CHIEFTAN

# pp. 1517-1751: GAP-generated tables.
