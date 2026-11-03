"""GIMBAL_LOCK_AVOIDANCE.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/GIMBAL_LOCK_AVOIDANCE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 412-413 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('GIMBAL_LOCK_AVOIDANCE', 'GIMBAL_LOCK_AVOIDANCE.agc', 'Comanche055', pages='412-413')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     GIMBAL_LOCK_AVOIDANCE.agc
# Purpose:      Part of the source code for Comanche, build 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 412-413
# Contact:      Onno Hommes <ohommes@cmu.edu>.
# Website:      www.ibiblio.org/apollo.
# Mod history:  05/07/09 OH     Transcription Batch 1 Assignment
#
# The contents of the "Comanche055" files, in general, are transcribed
# from scanned documents.
#
# Assemble revision 055 of AGC program Comanche by NASA
# 2021113-051.  April 1, 1969.
#
# This AGC program shall also be referred to as Colossus 2A
#
# Prepared by
# Massachusetts Institute of Technology
# 75 Cambridge Parkway
# Cambridge, Massachusetts
#
# under NASA contract NAS 9-4065.
#
# Refer directly to the online document mentioned above for further information.
# Please report any errors to info@sandroid.org.

# Page 412
#   BANK 15
#   SETLOC KALCMON1
#   BANK

#   EBANK= BCDU
# DETECTING GIMBAL LOCK
S('LOCSKIRT', 'equals', 0o54737, line=37)
W('22,2737', 0o70740, 'WCALC', 'LXC,1', 'DLOAD*', kind='interp', line=38)
W('22,2740', 0o01130, '', '', 'RATEINDX', kind='operand', line=39)
W('22,2741', 0o04771, '', '', 'ARATE,1', kind='operand', line=40)
W('22,2742', 0o45002, '', 'SR4', 'CALL', 'COMPUTE THE INCREMENTAL ROTATION MATRIX', kind='interp', line=41)
W('22,2743', 0o44530, '', '', 'DELCOMP', 'DEL CORRESPONDING TO A 1 SEC ROTATION', kind='operand', line=42)
# ABOUT COF
W('22,2744', 0o74343, '', 'DLOAD*', 'VXSC', kind='interp', line=44)
W('22,2745', 0o04771, '', '', 'ARATE,1', kind='operand', line=45)
W('22,2746', 0o03343, '', '', 'COF', kind='operand', line=46)
W('22,2747', 0o77721, '', 'MXV', kind='interp', line=47)
W('22,2750', 0o05003, '', '', 'QUADROT', kind='operand', line=48)
W('22,2751', 0o17311, '', 'STODL', 'BRATE', kind='interp', line=49)
W('22,2752', 0o03365, '', '', 'AM', kind='operand', line=50)
W('22,2753', 0o55605, '', 'DMP', 'DDV*', kind='interp', line=51)
W('22,2754', 0o05001, '', '', 'ANGLTIME', kind='operand', line=52)
W('22,2755', 0o04771, '', '', 'ARATE,1', kind='operand', line=53)
W('22,2756', 0o77661, '', 'SR', kind='interp', line=54)
W('22,2757', 0o20606, '', '', '5', kind='operand', line=55)
W('22,2760', 0o27317, '', 'STOVL', 'TM', kind='interp', line=56)
W('22,2761', 0o03311, '', '', 'BRATE', kind='operand', line=57)
W('22,2762', 0o77761, '', 'VXSC', kind='interp', line=58)
W('22,2763', 0o05025, '', '', 'BIASCALE', kind='operand', line=59)
W('22,2764', 0o03275, '', 'STORE', 'BIASTEMP', 'ATTITUDE ERROR BIAS TO PREVENT OVERSHOOT', kind='interp', line=60)
# IN SYSTEM
W('22,2765', 0o77614, '', 'SETGO', '', 'STATE SWITCH CALCMAN2 (43D)', kind='interp', line=62)
W('22,2766', 0o01035, '', '', 'CALCMAN2', '0(OFF) = BYPASS STARTING PROCEDURE', kind='operand', line=63)
W('22,2767', 0o45032, '', '', 'NEWANGL +1', '1(ON) = START MANEUVER', kind='operand', line=64)

W('22,2770', 0o00044, 'ARATE', '2DEC', '.0022222222', '= .05 DEG/SEC', kind='data', line=67)
W('22,2771', 0o15053, kind='data', line=67)

W('22,2772', 0o00221, '', '2DEC', '.0088888889', '= .2 DEG/SEC', kind='data', line=69)
W('22,2773', 0o24255, kind='data', line=69)

W('22,2774', 0o00554, '', '2DEC', '.0222222222', '= .5 DEG/SEC', kind='data', line=71)
W('22,2775', 0o02660, kind='data', line=71)

W('22,2776', 0o02660, '', '2DEC', '.0888888889', '= 2 DEG/SEC                $22.5 DEG/SEC', kind='data', line=73)
W('22,2777', 0o13301, kind='data', line=73)

W('22,3000', 0o00003, 'ANGLTIME', '2DEC', '.000190735', '= 100B - 19', kind='data', line=75)
W('22,3001', 0o04000, kind='data', line=75)

# MANEUVER ANGLE TO MANEUVER TIME

W('22,3002', 0o03146, 'QUADROT', '2DEC', '.1', 'ROTATION MATRIX FROM S/C AXES TO CONTROL', kind='data', line=79)
W('22,3003', 0o14632, kind='data', line=79)

# Page 413
W('22,3004', 0o00000, '', '2DEC', '0', 'AXES  (X ROT = -7.25 DEG)', kind='data', line=82)
W('22,3005', 0o00000, kind='data', line=82)

W('22,3006', 0o00000, '', '2DEC', '0', kind='data', line=84)
W('22,3007', 0o00000, kind='data', line=84)

W('22,3010', 0o00000, '', '2DEC', '0', kind='data', line=86)
W('22,3011', 0o00000, kind='data', line=86)

W('22,3012', 0o03131, '', '2DEC', '.099200', '=(.1)COS7.25', kind='data', line=88)
W('22,3013', 0o11275, kind='data', line=88)

W('22,3014', 0o77461, '', '2DEC', '-.012620', '=-(.1)SIN7.25', kind='data', line=90)
W('22,3015', 0o47370, kind='data', line=90)

W('22,3016', 0o00000, '', '2DEC', '0', kind='data', line=92)
W('22,3017', 0o00000, kind='data', line=92)

W('22,3020', 0o00316, '', '2DEC', '.012620', '(.1)SIN7.25', kind='data', line=94)
W('22,3021', 0o30407, kind='data', line=94)

W('22,3022', 0o03131, '', '2DEC', '.099200', '(.1)COS7.25', kind='data', line=96)
W('22,3023', 0o11275, kind='data', line=96)

W('22,3024', 0o00004, 'BIASCALE', '2DEC', '.0002543132', '= (450/180)(1/0.6)(1/16384)', kind='data', line=98)
W('22,3025', 0o05253, kind='data', line=98)
