"""RCS-CSM_DAP_EXECUTIVE_PROGRAMS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/RCS-CSM_DAP_EXECUTIVE_PROGRAMS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1037-1038 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('RCS_CSM_DAP_EXECUTIVE_PROGRAMS', 'RCS-CSM_DAP_EXECUTIVE_PROGRAMS.agc', 'Comanche055', pages='1037-1038')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     RCS-CSM_DAP_EXECUTIVE_PROGRAMS.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1037-1038
# Mod history:  2009-05-13 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
# 2009-05-20 RSB  A "Page N" comment was corrected.
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

# Page 1037
# CALCULATION OF  AMGB, AMBG  ONCE EVERY SECOND
#
# AMGB =  1       SIN(PSI)                0
# 0       COS(PSI)COS(PHI)        SIN(PHI)
# 0       -COS(PSI)SIN(PHI)       COS(PHI)
#
# AMBG =  1       -TAN(PSI)COS(PHI)       TAN(PSI)SIN(PHI)
# 0       COS(PHI)/COS(PSI)       -SIN(PHI)/COS(PSI)
# 0       SIN(PHI)                COS(PHI)
#
# WHERE PHI AND PSI ARE CDU ANGLES

#   BANK 20
#   SETLOC DAPS8
#   BANK

#   COUNT* $$/DAPEX
#   EBANK= KMPAC
W('22,3447', 0o30102, 'AMBGUPDT', 'CA', 'FLAGWRD6', 'CHECK FOR RCS AUTOPILOT', line=51)
W('22,3450', 0o00006, '', 'EXTEND', line=52)
W('22,3451', 0o65217, '', 'BZMF', 'ENDOFJOB', 'BIT15 = 0, BIT14 = 1', line=53)
W('22,3452', 0o75002, '', 'MASK', 'BIT14', 'IF NOT RCS, EXIT', line=54)
W('22,3453', 0o00006, '', 'EXTEND', line=55)
W('22,3454', 0o15217, '', 'BZF', 'ENDOFJOB', 'TO PROTECT TVC DAP ON SWITCHOVER', line=56)

W('22,3455', 0o30034, '', 'CA', 'CDUZ', line=58)
W('22,3456', 0o05075, '', 'TC', 'SPSIN2', line=59)
W('22,3457', 0o55640, '', 'TS', 'AMGB1', 'CALCULATE AMGB', line=60)
W('22,3460', 0o30034, '', 'CA', 'CDUZ', line=61)
W('22,3461', 0o05074, '', 'TC', 'SPCOS2', line=62)
W('22,3462', 0o55645, '', 'TS', 'CAPSI', 'MUST CHECK FOR GIMBAL LOCK', line=63)
W('22,3463', 0o33507, '', 'CAF', 'QUADANGL', '= 7.25  DEGREES JET QUAD ANGULAR OFFSET', line=64)
W('22,3464', 0o00006, '', 'EXTEND', line=65)
W('22,3465', 0o20032, '', 'MSU', 'CDUX', line=66)
W('22,3466', 0o40000, '', 'COM', '', 'CDUX - 7.25 DEG', line=67)
W('22,3467', 0o05074, '', 'TC', 'SPCOS1', line=68)
W('22,3470', 0o55644, '', 'TS', 'AMGB8', line=69)
W('22,3471', 0o00006, '', 'EXTEND', line=70)
W('22,3472', 0o71645, '', 'MP', 'CAPSI', line=71)
W('22,3473', 0o55641, '', 'TS', 'AMGB4', line=72)
W('22,3474', 0o33507, '', 'CAF', 'QUADANGL', line=73)
W('22,3475', 0o00006, '', 'EXTEND', line=74)
W('22,3476', 0o20032, '', 'MSU', 'CDUX', line=75)
W('22,3477', 0o40000, '', 'COM', '', 'CDUX - 7.25 DEG', line=76)
W('22,3500', 0o05075, '', 'TC', 'SPSIN1', line=77)
W('22,3501', 0o55642, '', 'TS', 'AMGB5', line=78)
W('22,3502', 0o00006, '', 'EXTEND', line=79)
W('22,3503', 0o71645, '', 'MP', 'CAPSI', line=80)
W('22,3504', 0o40000, '', 'COM', line=81)
# Page 1038
W('22,3505', 0o55643, '', 'TS', 'AMGB7', line=83)
W('22,3506', 0o15217, '', 'TCF', 'ENDOFJOB', line=84)
W('22,3507', 0o01224, 'QUADANGL', 'DEC', '660', '= 7.25 DEGREES', kind='data', line=85)
