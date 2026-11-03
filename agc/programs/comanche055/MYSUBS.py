"""MYSUBS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/MYSUBS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 999-1001 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('MYSUBS', 'MYSUBS.agc', 'Comanche055', pages='999-1001')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     MYSUBS.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        999-1001
# Mod history:  2009-05-13 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
# 2009-05-20 RSB  Corrections: EBANK= changed from MPAC to KMPAC.
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

# Page 999
#   BANK 20
#   SETLOC MYSUBS
#   BANK

#   EBANK= KMPAC
S('SPCOS1', 'equals', 0o5074, line=37)
S('SPSIN1', 'equals', 0o5075, line=38)
S('SPCOS2', 'equals', 0o5074, line=39)
S('SPSIN2', 'equals', 0o5075, line=40)

#   COUNT 21/DAPMS

# ONE AND ONE HALF PRECISION MULTIPLICATION ROUTINE

W('21,2042', 0o55512, 'SMALLMP', 'TS', 'KMPTEMP', 'A(X+Y)', line=47)
W('21,2043', 0o00006, '', 'EXTEND', line=48)
W('21,2044', 0o71511, '', 'MP', 'KMPAC +1', line=49)
W('21,2045', 0o55511, '', 'TS', 'KMPAC +1', 'AY', line=50)
W('21,2046', 0o35021, '', 'CAF', 'ZERO', line=51)
W('21,2047', 0o57510, '', 'XCH', 'KMPAC', line=52)
W('21,2050', 0o00006, '', 'EXTEND', line=53)
W('21,2051', 0o71512, '', 'MP', 'KMPTEMP', 'AX', line=54)
W('21,2052', 0o21511, '', 'DAS', 'KMPAC', 'AX+AY', line=55)
W('21,2053', 0o00002, '', 'TC', 'Q', line=56)

# SUBROUTINE FOR DOUBLE PRECISION ADDITIONS OF ANGLES
# A AND L CONTAIN A DP(1S) ANGLE SCALED BY 180 DEGS TO BE ADDED TO KMPAC.
# RESULT IS PLACED IN KMPAC.  TIMING = 6 MCT (22 MCT ON OVERFLOW)

W('21,2054', 0o21511, 'DPADD', 'DAS', 'KMPAC', line=63)
W('21,2055', 0o00006, '', 'EXTEND', line=64)
W('21,2056', 0o12073, '', 'BZF', 'TSK +1', 'NO OVERFLOW', line=65)
W('21,2057', 0o11510, '', 'CCS', 'KMPAC', line=66)
W('21,2060', 0o12074, '', 'TCF', 'DPADD+', '+ OVERFLOW', line=67)
W('21,2061', 0o12063, '', 'TCF', '+2', line=68)
W('21,2062', 0o12076, '', 'TCF', 'DPADD-', '- OVERFLOW', line=69)
W('21,2063', 0o11511, '', 'CCS', 'KMPAC +1', line=70)
W('21,2064', 0o12101, '', 'TCF', 'DPADD2+', 'UPPER = 0, LOWER +', line=71)
W('21,2065', 0o12067, '', 'TCF', '+2', line=72)
W('21,2066', 0o40000, '', 'COM', '', 'UPPER = 0, LOWER -', line=73)
W('21,2067', 0o64777, '', 'AD', 'POSMAX', 'LOWER = 0, A=0', line=74)
W('21,2070', 0o55511, '', 'TS', 'KMPAC +1', 'CAN NOT OVERFLOW', line=75)
W('21,2071', 0o34777, '', 'CA', 'POSMAX', 'UPPER WAS = 0', line=76)
W('21,2072', 0o55510, 'TSK', 'TS', 'KMPAC', line=77)
W('21,2073', 0o00002, '', 'TC', 'Q', line=78)

W('21,2074', 0o65001, 'DPADD+', 'AD', 'NEGMAX', 'KMPAC GREATER THAN 0', line=80)
W('21,2075', 0o12072, '', 'TCF', 'TSK', line=81)

# Page 1000
W('21,2076', 0o40000, 'DPADD-', 'COM', line=84)
W('21,2077', 0o64777, '', 'AD', 'POSMAX', 'KMPAC LESS THAN 0', line=85)
W('21,2100', 0o12072, '', 'TCF', 'TSK', line=86)

W('21,2101', 0o65001, 'DPADD2+', 'AD', 'NEGMAX', 'CAN NOT OVERFLOW', line=88)
W('21,2102', 0o55511, '', 'TS', 'KMPAC +1', line=89)
W('21,2103', 0o35001, '', 'CA', 'NEGMAX', 'UPPER WAS = 0', line=90)
W('21,2104', 0o12072, '', 'TCF', 'TSK', line=91)

# Page 1001 (empty page)
