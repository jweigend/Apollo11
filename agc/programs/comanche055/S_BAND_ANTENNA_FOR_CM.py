"""S-BAND_ANTENNA_FOR_CM.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/S-BAND_ANTENNA_FOR_CM.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 934-935 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('S_BAND_ANTENNA_FOR_CM', 'S-BAND_ANTENNA_FOR_CM.agc', 'Comanche055', pages='934-935')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     S-BAND_ANTENNA_FOR_CM.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Jim Lawton <jim.lawton@gmail.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        934-935
# Mod history:  2009-05-11 JVL  Adapted from the Colossus249/ file
# of the same name, using Comanche055 page
# images.
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

# Page 934
# S-BAND ANTENNA FOR CM

#   BANK 23
#   SETLOC SBAND
#   BANK

#   COUNT* $$/R05
#   EBANK= EMSALT

W('42,3652', 0o04662, 'SBANDANT', 'TC', 'BANKCALL', 'V 64 E GETS US HERE', line=41)
W('42,3653', 0o17653, '', 'CADR', 'R02BOTH', 'CHECK IF IMU IS ON AND ALIGNED', kind='data', line=42)
W('42,3654', 0o06006, '', 'TC', 'INTPRET', line=43)
W('42,3655', 0o45034, '', 'RTB', 'CALL', kind='interp', line=44)
W('42,3656', 0o45510, '', '', 'LOADTIME', 'PICKUP CURRENT TIME SCALED B-28', kind='operand', line=45)
W('42,3657', 0o47477, '', '', 'CDUTRIG', 'COMPUTE SINES AND COSINES OF CDU ANGLES', kind='operand', line=46)
W('42,3660', 0o34041, '', 'STCALL', 'TDEC1', 'ADVANCE INTEGRATION TO TIME IN TDEC1', kind='interp', line=47)
W('42,3661', 0o27114, '', '', 'CSMCONIC', 'USING CONIC INTEGRATION', kind='operand', line=48)
W('42,3662', 0o46135, '', 'SLOAD', 'BHIZ', 'ORIGIN OF REFERENCE INERTIAL SYSTEM IS', kind='interp', line=49)
W('42,3663', 0o00050, '', '', 'X2', 'EARTH = 0, MOON = 2', kind='operand', line=50)
W('42,3664', 0o65677, '', '', 'EISOI', kind='operand', line=51)
W('42,3665', 0o77775, '', 'VLOAD', kind='interp', line=52)
W('42,3666', 0o00001, '', '', 'RATT', kind='operand', line=53)
W('42,3667', 0o00003, '', 'STORE', 'RCM', 'MOVE RATT TO PREVENT WIPEOUT', kind='interp', line=54)
W('42,3670', 0o45145, '', 'DLOAD', 'CALL', 'MOON, PUSH ON', kind='interp', line=55)
W('42,3671', 0o00015, '', '', 'TAT', 'GET ORIGINAL TIME', kind='operand', line=56)
W('42,3672', 0o54115, '', '', 'LUNPOS', 'COMPUTE POSITION VECTOR OF MOON', kind='operand', line=57)
W('42,3673', 0o57455, '', 'VAD', 'VCOMP', 'R= -(REM+RCM) = NEG. OF S/C POS. VEC', kind='interp', line=58)
W('42,3674', 0o00003, '', '', 'RCM', kind='operand', line=59)
W('42,3675', 0o77650, '', 'GOTO', kind='interp', line=60)
W('42,3676', 0o65701, '', '', 'EISOI +2', kind='operand', line=61)
W('42,3677', 0o57575, 'EISOI', 'VLOAD', 'VCOMP', 'EARTH, R= -RCM', kind='interp', line=62)
W('42,3700', 0o00001, '', '', 'RATT', kind='operand', line=63)
W('42,3701', 0o64201, '', 'SETPD', 'MXV', 'RCS TO STABLE MEMBER- B-1X B-29X B+1', kind='interp', line=64)
W('42,3702', 0o00003, '', '', '2D', '2D', kind='operand', line=65)
W('42,3703', 0o01736, '', '', 'REFSMMAT', 'STABLE MEMBER.  B-1X B-29X B+1= B-29', kind='operand', line=66)
W('42,3704', 0o65372, '', 'VSL1', 'PDDL', '8D', kind='interp', line=67)
W('42,3705', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=68)
W('42,3706', 0o24025, '', 'STOVL', 'YAWANG', 'ZERO OUT YAWANG, SET UP FOR SMNB', kind='interp', line=69)
W('42,3707', 0o00003, '', '', 'RCM', 'TRANSFORMATION.  SM COORD.  SCALED B-29', kind='operand', line=70)
W('42,3710', 0o77624, '', 'CALL', kind='interp', line=71)
W('42,3711', 0o47644, '', '', '*SMNB*', kind='operand', line=72)
W('42,3712', 0o00003, '', 'STORE', 'R', 'SAVE NAV. BASE COORDINATES', kind='interp', line=73)
W('42,3713', 0o63256, '', 'UNIT', 'PDVL', '14D', kind='interp', line=74)
W('42,3714', 0o00003, '', '', 'R', kind='operand', line=75)
W('42,3715', 0o72431, '', 'VPROJ', 'VSL2', 'COMPUTE PROJECTION OF VECTOR INTO CM', kind='interp', line=76)
W('42,3716', 0o15327, '', '', 'HIUNITZ', 'XY-PLANE, R-(R.UZ)UZ', kind='operand', line=77)
W('42,3717', 0o40045, '', 'BVSU', 'BOV', 'CLEAR OVERFLOW INDICATOR IF SET', kind='interp', line=78)
W('42,3720', 0o00003, '', '', 'R', kind='operand', line=79)
W('42,3721', 0o65722, '', '', 'COVCNV', kind='operand', line=80)
W('42,3722', 0o40056, 'COVCNV', 'UNIT', 'BOV', 'TEST OVERFLOW FOR INDICATION OF NULL', kind='interp', line=81)
W('42,3723', 0o65737, '', '', 'NOADJUST', 'VECTOR', kind='operand', line=82)
W('42,3724', 0o50206, '', 'PUSH', 'DOT', '20D', kind='interp', line=83)
# Page 935
W('42,3725', 0o15333, '', '', 'HIUNITX', 'COMPUTE YAW ANGLE = ACOS (URP.UX)', kind='operand', line=85)
W('42,3726', 0o65552, '', 'SL1', 'ACOS', 'REVOLUTIONS SCALED B0', kind='interp', line=86)
W('42,3727', 0o50315, '', 'PDVL', 'DOT', '22D YAWANG', kind='interp', line=87)
W('42,3730', 0o00017, '', '', 'URP', kind='operand', line=88)
W('42,3731', 0o15331, '', '', 'HIUNITY', 'COMPUTE FOLLOWING- URP.UY', kind='operand', line=89)
W('42,3732', 0o51152, '', 'SL1', 'BPL', 'POSITIVE', kind='interp', line=90)
W('42,3733', 0o65737, '', '', 'NOADJUST', 'YES, 0- 180 DEGREES', kind='operand', line=91)
W('42,3734', 0o45345, '', 'DLOAD', 'DSU', 'NO, 181-360 DEGREES 20D', kind='interp', line=92)
W('42,3735', 0o15343, '', '', 'DPPOSMAX', 'COMPUTE 2 PI MINUS YAW ANGLE', kind='operand', line=93)
W('42,3736', 0o77606, '', 'PUSH', '', '22D YAWANG', kind='interp', line=94)
W('42,3737', 0o50375, 'NOADJUST', 'VLOAD', 'DOT', 'COMPUTE PITCH ANGLE', kind='interp', line=95)
W('42,3740', 0o00011, '', '', 'UR', 'ACOS (UR.UZ) - PI/2', kind='operand', line=96)
W('42,3741', 0o15327, '', '', 'HIUNITZ', kind='operand', line=97)
W('42,3742', 0o65552, '', 'SL1', 'ACOS', 'REVOLUTIONS B0', kind='interp', line=98)
W('42,3743', 0o77625, '', 'DSU', kind='interp', line=99)
W('42,3744', 0o15325, '', '', 'HIDP1/4', kind='operand', line=100)
W('42,3745', 0o16321, '', 'STODL', 'RHOSB', kind='interp', line=101)
W('42,3746', 0o00025, '', '', 'YAWANG', kind='operand', line=102)
W('42,3747', 0o02323, '', 'STORE', 'GAMMASB', 'PATCH FOR CHECKOUT', kind='interp', line=103)
W('42,3750', 0o77776, '', 'EXIT', kind='interp', line=104)
W('42,3751', 0o31044, '', 'CA', 'EXTVBACT', 'IS BIT 5 STILL ON', line=105)
W('42,3752', 0o75013, '', 'MASK', 'BIT5', line=106)
W('42,3753', 0o00006, '', 'EXTEND', line=107)
W('42,3754', 0o15534, '', 'BZF', 'ENDEXT', 'NO, WE HAVE BEEN ANSWERED', line=108)
W('42,3755', 0o33771, '', 'CAF', 'V06N51', 'DISPLAY ANGLES', line=109)
W('42,3756', 0o04662, '', 'TC', 'BANKCALL', line=110)
W('42,3757', 0o20600, '', 'CADR', 'GOMARKFR', kind='data', line=111)
W('42,3760', 0o05625, '', 'TC', 'B5OFF', 'TERMINATE', line=112)
W('42,3761', 0o05625, '', 'TC', 'B5OFF', line=113)
W('42,3762', 0o05217, '', 'TC', 'ENDOFJOB', 'RECYCLE', line=114)
W('42,3763', 0o35015, '', 'CAF', 'BIT3', 'IMMEDIATE RETURN', line=115)
W('42,3764', 0o05526, '', 'TC', 'BLANKET', 'BLANK R3', line=116)
W('42,3765', 0o35017, '', 'CAF', 'BIT1', 'DELAY MINIMUM TIME TO ALLOW DISPLAY IN', line=117)
W('42,3766', 0o04662, '', 'TC', 'BANKCALL', line=118)
W('42,3767', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=119)
W('42,3770', 0o13654, '', 'TCF', 'SBANDANT +2', line=120)
W('42,3771', 0o01463, 'V06N51', 'VN', '0651', kind='data', line=121)
S('RCM', 'equals', 0o2, line=122)
S('UR', 'equals', 0o10, line=123)
S('URP', 'equals', 0o16, line=124)
S('YAWANG', 'equals', 0o24, line=125)
S('PITCHANG', 'equals', 0o26, line=126)
S('R', 'equals', 0o2, line=127)
#   SBANK= LOWSUPER
