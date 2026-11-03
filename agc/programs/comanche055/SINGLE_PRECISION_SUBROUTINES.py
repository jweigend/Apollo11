"""SINGLE_PRECISION_SUBROUTINES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/SINGLE_PRECISION_SUBROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1207 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('SINGLE_PRECISION_SUBROUTINES', 'SINGLE_PRECISION_SUBROUTINES.agc', 'Comanche055', pages='1207')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     SINGLE_PRECISION_SUBROUTINES.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1207
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

# Page 1207
#   BLOCK 02
# SINGLE PRECISION SINE AND COSINE

#   COUNT 02/INTER
W('5074', 0o65002, 'SPCOS', 'AD', 'HALF', 'ARGUMENTS SCALED AT PI', line=35)
W('5075', 0o55075, 'SPSIN', 'TS', 'TEMK', line=36)
W('5076', 0o15100, '', 'TCF', 'SPT', line=37)
W('5077', 0o41075, '', 'CS', 'TEMK', line=38)
W('5100', 0o60000, 'SPT', 'DOUBLE', line=39)
W('5101', 0o55075, '', 'TS', 'TEMK', line=40)
W('5102', 0o15113, '', 'TCF', 'POLLEY', line=41)
W('5103', 0o57075, '', 'XCH', 'TEMK', line=42)
W('5104', 0o51075, '', 'INDEX', 'TEMK', line=43)
W('5105', 0o65000, '', 'AD', 'LIMITS', line=44)
W('5106', 0o40000, '', 'COM', line=45)
W('5107', 0o61075, '', 'AD', 'TEMK', line=46)
W('5110', 0o55075, '', 'TS', 'TEMK', line=47)
W('5111', 0o15113, '', 'TCF', 'POLLEY', line=48)
W('5112', 0o15131, '', 'TCF', 'ARG90', line=49)
W('5113', 0o00006, 'POLLEY', 'EXTEND', line=50)
W('5114', 0o71075, '', 'MP', 'TEMK', line=51)
W('5115', 0o55076, '', 'TS', 'SQ', line=52)
W('5116', 0o00006, '', 'EXTEND', line=53)
W('5117', 0o75047, '', 'MP', 'C5/2', line=54)
W('5120', 0o67706, '', 'AD', 'C3/2', line=55)
W('5121', 0o00006, '', 'EXTEND', line=56)
W('5122', 0o71076, '', 'MP', 'SQ', line=57)
W('5123', 0o67666, '', 'AD', 'C1/2', line=58)
W('5124', 0o00006, '', 'EXTEND', line=59)
W('5125', 0o71075, '', 'MP', 'TEMK', line=60)
W('5126', 0o20001, '', 'DDOUBL', line=61)
W('5127', 0o55075, '', 'TS', 'TEMK', line=62)
W('5130', 0o00002, '', 'TC', 'Q', line=63)
W('5131', 0o50000, 'ARG90', 'INDEX', 'A', line=64)
W('5132', 0o45000, '', 'CS', 'LIMITS', line=65)
W('5133', 0o00002, '', 'TC', 'Q', 'RESULT SCALED AT 1', line=66)
# SPROOT WAS DELETED IN REV 51 OF MASTER. ASS. CONT. HAS CARDS.
