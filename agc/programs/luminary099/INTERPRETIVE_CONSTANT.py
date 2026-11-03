"""INTERPRETIVE_CONSTANT.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/INTERPRETIVE_CONSTANT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1100-1101 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INTERPRETIVE_CONSTANT', 'INTERPRETIVE_CONSTANT.agc', 'Luminary099', pages='1100-1101')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INTERPRETIVE_CONSTANT.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1100-1101
# Mod history:  2009-05-25 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
#
# This source code has been transcribed or otherwise adapted from
# digitized images of a hardcopy from the MIT Museum.  The digitization
# was performed by Paul Fjeld, and arranged for by Deborah Douglas of
# the Museum.  Many thanks to both.  The images (with suitable reduction
# in storage size and consequent reduction in image quality as well) are
# available online at www.ibiblio.org/apollo.  If for some reason you
# find that the images are illegible, contact me at info@sandroid.org
# about getting access to the (much) higher-quality images which Paul
# actually created.
#
# Notations on the hardcopy document read, in part:
#
# Assemble revision 001 of AGC program LMY99 by NASA 2021112-061
# 16:27 JULY 14, 1969

# Page 1100
#   SETLOC INTPRET1
#   BANK

#   COUNT* $$/ICONS
W('23,2511', 0o10000, 'DP1/4TH', '2DEC', '.25', kind='data', line=34)
W('23,2512', 0o00000, kind='data', line=34)

W('23,2513', 0o00000, 'UNITZ', '2DEC', '0', kind='data', line=36)
W('23,2514', 0o00000, kind='data', line=36)

W('23,2515', 0o00000, 'UNITY', '2DEC', '0', kind='data', line=38)
W('23,2516', 0o00000, kind='data', line=38)

W('23,2517', 0o20000, 'UNITX', '2DEC', '.5', kind='data', line=40)
W('23,2520', 0o00000, kind='data', line=40)

W('23,2521', 0o00000, 'ZEROVECS', '2DEC', '0', kind='data', line=42)
W('23,2522', 0o00000, kind='data', line=42)

W('23,2523', 0o00000, '', '2DEC', '0', kind='data', line=44)
W('23,2524', 0o00000, kind='data', line=44)

W('23,2525', 0o00000, '', '2DEC', '0', kind='data', line=46)
W('23,2526', 0o00000, kind='data', line=46)

S('DPHALF', 'equals', 0o56517, line=48)
W('23,2527', 0o37777, 'DPPOSMAX', 'OCT', '37777', kind='data', line=49)
W('23,2530', 0o37777, '', 'OCT', '37777', kind='data', line=50)

# Page 1101
# INTERPRETIVE CONSTANTS IN THE OTHER HALF-MEMORY

#   SETLOC INTPRET2
#   BANK

#   COUNT* $$/ICONS
W('12,2000', 0o00000, 'ZUNIT', '2DEC', '0', kind='data', line=59)
W('12,2001', 0o00000, kind='data', line=59)

W('12,2002', 0o00000, 'YUNIT', '2DEC', '0', kind='data', line=61)
W('12,2003', 0o00000, kind='data', line=61)

W('12,2004', 0o20000, 'XUNIT', '2DEC', '.5', kind='data', line=63)
W('12,2005', 0o00000, kind='data', line=63)

W('12,2006', 0o00000, 'ZEROVEC', '2DEC', '0', kind='data', line=65)
W('12,2007', 0o00000, kind='data', line=65)

W('12,2010', 0o00000, '', '2DEC', '0', kind='data', line=67)
W('12,2011', 0o00000, kind='data', line=67)

W('12,2012', 0o00000, '', '2DEC', '0', kind='data', line=69)
W('12,2013', 0o00000, kind='data', line=69)

W('12,2014', 0o77777, '', 'OCT', '77777', '-0, -6, -12 MUST REMAIN IN THIS ORDER', kind='data', line=71)
W('12,2015', 0o77771, 'DFC-6', 'DEC', '-6', kind='data', line=72)
W('12,2016', 0o77763, 'DFC-12', 'DEC', '-12', kind='data', line=73)
W('12,2017', 0o37777, 'LODPMAX', '2OCT', '3777737777', 'THESE TWO CONSTANTS MUST REMAIN', kind='data', line=74)
W('12,2020', 0o37777, kind='data', line=74)

W('12,2021', 0o37777, 'LODPMAX1', '2OCT', '3777737777', 'ADJACENT AND THE SAME FOR INTEGRATION', kind='data', line=76)
W('12,2022', 0o37777, kind='data', line=76)

S('ZERODP', 'equals', 0o34006, line=78)
S('HALFDP', 'equals', 0o34004, line=79)
