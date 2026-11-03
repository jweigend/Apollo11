"""SINGLE_PRECISION_SUBROUTINES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/SINGLE_PRECISION_SUBROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1102 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('SINGLE_PRECISION_SUBROUTINES', 'SINGLE_PRECISION_SUBROUTINES.agc', 'Luminary099', pages='1102')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     SINGLE_PRECISION_SUBROUTINES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1102
# Mod history:  2009-05-25 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2010-12-31 JL   Fixed page number comment.
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

# Page 1102
#   BLOCK 02

# SINGLE PRECISION SINE AND COSINE

#   COUNT* $$/INTER
W('5032', 0o64736, 'SPCOS', 'AD', 'HALF', 'ARGUMENTS SCALED AT PI', line=36)
W('5033', 0o55076, 'SPSIN', 'TS', 'TEMK', line=37)
W('5034', 0o15036, '', 'TCF', 'SPT', line=38)
W('5035', 0o41076, '', 'CS', 'TEMK', line=39)
W('5036', 0o60000, 'SPT', 'DOUBLE', line=40)
W('5037', 0o55076, '', 'TS', 'TEMK', line=41)
W('5040', 0o15051, '', 'TCF', 'POLLEY', line=42)
W('5041', 0o57076, '', 'XCH', 'TEMK', line=43)
W('5042', 0o51076, '', 'INDEX', 'TEMK', line=44)
W('5043', 0o64734, '', 'AD', 'LIMITS', line=45)
W('5044', 0o40000, '', 'COM', line=46)
W('5045', 0o61076, '', 'AD', 'TEMK', line=47)
W('5046', 0o55076, '', 'TS', 'TEMK', line=48)
W('5047', 0o15051, '', 'TCF', 'POLLEY', line=49)
W('5050', 0o15067, '', 'TCF', 'ARG90', line=50)
W('5051', 0o00006, 'POLLEY', 'EXTEND', line=51)
W('5052', 0o71076, '', 'MP', 'TEMK', line=52)
W('5053', 0o55077, '', 'TS', 'SQ', line=53)
W('5054', 0o00006, '', 'EXTEND', line=54)
W('5055', 0o75005, '', 'MP', 'C5/2', line=55)
W('5056', 0o67737, '', 'AD', 'C3/2', line=56)
W('5057', 0o00006, '', 'EXTEND', line=57)
W('5060', 0o71077, '', 'MP', 'SQ', line=58)
W('5061', 0o67717, '', 'AD', 'C1/2', line=59)
W('5062', 0o00006, '', 'EXTEND', line=60)
W('5063', 0o71076, '', 'MP', 'TEMK', line=61)
W('5064', 0o20001, '', 'DDOUBL', line=62)
W('5065', 0o55076, '', 'TS', 'TEMK', line=63)
W('5066', 0o00002, '', 'TC', 'Q', line=64)
W('5067', 0o50000, 'ARG90', 'INDEX', 'A', line=65)
W('5070', 0o44734, '', 'CS', 'LIMITS', line=66)
W('5071', 0o00002, '', 'TC', 'Q', 'RESULT SCALED AT 1', line=67)
