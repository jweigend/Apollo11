"""GIMBAL_LOCK_AVOIDANCE.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/GIMBAL_LOCK_AVOIDANCE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 364 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('GIMBAL_LOCK_AVOIDANCE', 'GIMBAL_LOCK_AVOIDANCE.agc', 'Luminary099', pages='364')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     GIMBAL_LOCK_AVOIDANCE.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        364
# Mod history:  2009-05-17 RSB  Adapted from the corresponding
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

# Page 364
#   BANK 15

#   SETLOC KALCMON1
#   BANK

# DETECTING GIMBAL LOCK
S('LOCSKIRT', 'equals', 0o54744, line=37)

W('22,2744', 0o77614, 'NOGIMLOC', 'SET', kind='interp', line=39)
W('22,2745', 0o01074, '', '', 'CALCMAN3', kind='operand', line=40)
W('22,2746', 0o70740, 'WCALC', 'LXC,1', 'DLOAD*', kind='interp', line=41)
W('22,2747', 0o01325, '', '', 'RATEINDX', 'CHOOSE THE DESIRED MANEUVER RATE', kind='operand', line=42)
W('22,2750', 0o04772, '', '', 'ARATE,1', 'FROM A LIST OF FOUR', kind='operand', line=43)
W('22,2751', 0o45002, '', 'SR4', 'CALL', 'COMPUTE THE INCREMENTAL ROTATION MATRIX', kind='interp', line=44)
W('22,2752', 0o44527, '', '', 'DELCOMP', 'DEL CORRESPONDING TO A 1 SEC ROTATION', kind='operand', line=45)
# ABOUT COF
W('22,2753', 0o74343, '', 'DLOAD*', 'VXSC', kind='interp', line=47)
W('22,2754', 0o04772, '', '', 'ARATE,1', kind='operand', line=48)
W('22,2755', 0o03271, '', '', 'COF', kind='operand', line=49)
W('22,2756', 0o17326, '', 'STODL', 'BRATE', 'COMPONENT MANEUVER RATES 45 DEG/SEC', kind='interp', line=50)
W('22,2757', 0o03336, '', '', 'AM', kind='operand', line=51)
W('22,2760', 0o55605, '', 'DMP', 'DDV*', kind='interp', line=52)
W('22,2761', 0o05002, '', '', 'ANGLTIME', kind='operand', line=53)
W('22,2762', 0o04772, '', '', 'ARATE,1', kind='operand', line=54)
W('22,2763', 0o77661, '', 'SR', kind='interp', line=55)
W('22,2764', 0o20606, '', '', '5', kind='operand', line=56)
W('22,2765', 0o03334, '', 'STORE', 'TM', 'MANEUVER EXECUTION TIME SCALED AS T2', kind='interp', line=57)
W('22,2766', 0o77614, '', 'SETGO', kind='interp', line=58)
W('22,2767', 0o01035, '', '', 'CALCMAN2', '0(OFF) = CONTINUE MANEUVER', kind='operand', line=59)
W('22,2770', 0o45010, '', '', 'NEWANGL +1', '1(ON) = START MANEUVER', kind='operand', line=60)

# THE FOUR SELECTABLE FREE FALL MANEUVER RATES SELECTED BY
# LOADING RATEINDX WITH 0,2,4,6, RESPECTIVELY

W('22,2771', 0o00221, 'ARATE', '2DEC', '.0088888888', '= 0.2 DEG/SEC         $ 22.5 DEG/SEC', kind='data', line=65)
W('22,2772', 0o24255, kind='data', line=65)

W('22,2773', 0o00554, '', '2DEC', '.0222222222', '= 0.5 DEG/SEC         $ 22.5 DEG/SEC', kind='data', line=67)
W('22,2774', 0o02660, kind='data', line=67)

W('22,2775', 0o02660, '', '2DEC', '.0888888888', '= 2.0 DEG/SEC         $ 22.5 DEG/SEC', kind='data', line=69)
W('22,2776', 0o13301, kind='data', line=69)

W('22,2777', 0o16161, '', '2DEC', '.4444444444', '= 10.0 DEG/SEC        $ 22.5 DEG/SEC', kind='data', line=71)
W('22,3000', 0o30707, kind='data', line=71)

W('22,3001', 0o00003, 'ANGLTIME', '2DEC', '.0001907349', '= 1008-19 FUDGE FACTOR TO CONVERT', kind='data', line=73)
W('22,3002', 0o04000, kind='data', line=73)
# MANEUVER ANGLE TO MANEUVER TIME
