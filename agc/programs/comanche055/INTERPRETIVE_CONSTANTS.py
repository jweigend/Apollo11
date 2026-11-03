"""INTERPRETIVE_CONSTANTS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/INTERPRETIVE_CONSTANTS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1205-1206 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INTERPRETIVE_CONSTANTS', 'INTERPRETIVE_CONSTANTS.agc', 'Comanche055', pages='1205-1206')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INTERPRETIVE_CONSTANTS.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1205-1206
# Mod history:  2009-05-13 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
#
# This source code has been transcribed or otherwise adapted from digitized
# images of a hardcopy from the MIT Museum.  The digitization was performed
# by Paul Fjeld, and arranged for by Deborah Douglas of the Museum.  Many
# thanks to both.  The images (with suitable reduction in storage size and
# consequent reduction in image quality as well) are available online at
# www.ibiblio.org/apollo.  If for some reason you find that the images are
# illegible, contact me at info@sandroid.org about getting access to the
# (much) higher-quality images which Paul actually created.
#
# Notations on the hardcopy document read, in part:
#
# Assemble revision 055 of AGC program Comanche by NASA
# 2021113-051.  10:28 APR. 1, 1969
#
# This AGC program shall also be referred to as
# Colossus 2A

# Page 1205
#   SETLOC INTPRET1
#   BANK

#   COUNT 23/ICONS

W('26,3324', 0o10000, 'DP1/4TH', '2DEC', '.25', kind='data', line=36)
W('26,3325', 0o00000, kind='data', line=36)

W('26,3326', 0o00000, 'UNITZ', '2DEC', '0', kind='data', line=38)
W('26,3327', 0o00000, kind='data', line=38)

W('26,3330', 0o00000, 'UNITY', '2DEC', '0', kind='data', line=40)
W('26,3331', 0o00000, kind='data', line=40)

W('26,3332', 0o20000, 'UNITX', '2DEC', '.5', kind='data', line=42)
W('26,3333', 0o00000, kind='data', line=42)

W('26,3334', 0o00000, 'ZEROVECS', '2DEC', '0', kind='data', line=44)
W('26,3335', 0o00000, kind='data', line=44)

W('26,3336', 0o00000, '', '2DEC', '0', kind='data', line=46)
W('26,3337', 0o00000, kind='data', line=46)

W('26,3340', 0o00000, '', '2DEC', '0', kind='data', line=48)
W('26,3341', 0o00000, kind='data', line=48)

S('DPHALF', 'equals', 0o65332, line=50)
W('26,3342', 0o37777, 'DPPOSMAX', 'OCT', '37777', kind='data', line=51)
W('26,3343', 0o37777, '', 'OCT', '37777', kind='data', line=52)

# Page 1206
# INTERPRETIVE CONSTANTS IN THE OTHER HALF-MEMORY

#   SETLOC INTPRET2
#   BANK

#   COUNT 14/ICONS

W('04,3557', 0o00000, 'ZUNIT', '2DEC', '0', kind='data', line=62)
W('04,3560', 0o00000, kind='data', line=62)

W('04,3561', 0o00000, 'YUNIT', '2DEC', '0', kind='data', line=64)
W('04,3562', 0o00000, kind='data', line=64)

W('04,3563', 0o20000, 'XUNIT', '2DEC', '.5', kind='data', line=66)
W('04,3564', 0o00000, kind='data', line=66)

W('04,3565', 0o00000, 'ZEROVEC', '2DEC', '0', kind='data', line=68)
W('04,3566', 0o00000, kind='data', line=68)

W('04,3567', 0o00000, '', '2DEC', '0', kind='data', line=70)
W('04,3570', 0o00000, kind='data', line=70)

W('04,3571', 0o00000, '', '2DEC', '0', kind='data', line=72)
W('04,3572', 0o00000, kind='data', line=72)

W('04,3573', 0o77777, '', 'OCT', '77777', '-0,-6,-12 MUST REMAIN IN THIS ORDER', kind='data', line=74)
W('04,3574', 0o77771, 'DEC-6', 'DEC', '-6', kind='data', line=75)
W('04,3575', 0o77763, 'DEC-12', 'DEC', '-12', kind='data', line=76)
W('04,3576', 0o37777, 'LODPMAX', '2OCT', '3777737777', 'THESE TWO CONSTANTS MUST REMAIN', kind='data', line=77)
W('04,3577', 0o37777, kind='data', line=77)

W('04,3600', 0o37777, 'LODPMAX1', '2OCT', '3777737777', 'ADJACENT AND THE SAME FOR INTEGRATION', kind='data', line=79)
W('04,3601', 0o37777, kind='data', line=79)

S('ZERODP', 'equals', 0o21565, line=81)
S('HALFDP', 'equals', 0o21563, line=82)
