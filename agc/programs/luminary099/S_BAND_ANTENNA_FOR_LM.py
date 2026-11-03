"""S-BAND_ANTENNA_FOR_LM.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/S-BAND_ANTENNA_FOR_LM.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 486-489 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('S_BAND_ANTENNA_FOR_LM', 'S-BAND_ANTENNA_FOR_LM.agc', 'Luminary099', pages='486-489')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     S-BAND_ANTENNA_FOR_LM.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        486-489
# Mod history:  2009-05-17 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2009-06-07 RSB  Corrected a misprint.
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

# Page 486
# SUBROUTINE NAME: R05 - S-BAND ANTENNA FOR LM
#
# MOD0 BY T. JAMES
# MOD1 BY P. SHAKIR
#
# FUNCTIONAL DESCRIPTION
#
# THE S-BAND ANTENNA ROUTINE, R05, COMPUTES AND DISPLAYS THE PITCH AND
# YAW ANTENNA GIMBAL ANGLES REQUIRED TO POINT THE LM STEERABLE ANTENNA
# TOWARD THE CENTER OF THE EARTH. THIS ROUTINE IS SELECTED BY THE ASTRO-
# NAUT VIA DSKY ENTRY DURING COASTING FLIGHT OR WHEN THE LM IS ON THE MOON
# SURFACE. THE EARTH OR MOON REFERENCE COORDINATE SYSTEM IS USED DEPENDING
# ON WHETHER THE LM IS ABOUT TO ENTER OR HAS ALREADY ENTERED THE MOON
# SPHERE OF INFLUENCE, RESPECTIVELY
#
# TO CALL SUBROUTINE, ASTRONAUT KEYS IN V 64 E
#
# SUBROUTINES CALLED-
# R02BOTH
# INTPRET
# LOADTIME
# LEMCONIC
# LUNPOS
# CDUTRIG
# *SMNB*
# BANKCALL
# B50OFF
# ENDOFJOB
# BLANKET
#
# RETURNS WITH
# PITCH ANGLE IN PITCHANG         REV. B0
# YAW ANGLE IN YAWANG             REV. B0
#
# ERASABLES USED
# PITCHANG
# YAWANG
# RLM
# VAC AREA

#   BANK 41
#   SETLOC SBAND
#   BANK

#   EBANK= WHOCARES
#   COUNT* $$/R05
W('42,3606', 0o04616, 'SBANDANT', 'TC', 'BANKCALL', line=77)
# Page 487
W('42,3607', 0o11254, '', 'CADR', 'R02BOTH', 'CHECK IF IMU IS ON AND ALIGNED', kind='data', line=79)
W('42,3610', 0o06037, '', 'TC', 'INTPRET', line=80)
W('42,3611', 0o47001, '', 'SETPD', 'RTB', kind='interp', line=81)
W('42,3612', 0o00001, '', '', '0D', kind='operand', line=82)
W('42,3613', 0o21573, '', '', 'LOADTIME', 'PICK UP CURRENT TIME', kind='operand', line=83)
W('42,3614', 0o34041, '', 'STCALL', 'TDEC1', 'ADVANCE INTEGRATION TO TIME IN TDEC1', kind='interp', line=84)
W('42,3615', 0o27100, '', '', 'LEMCONIC', 'USING CONIC INTEGRATION', kind='operand', line=85)
W('42,3616', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=86)
W('42,3617', 0o00050, '', '', 'X2', 'X2 =0 EARTH SPHERE, X2 =2 MOON SPHERE', kind='operand', line=87)
W('42,3620', 0o65636, '', '', 'CONV4', kind='operand', line=88)
W('42,3621', 0o77775, '', 'VLOAD', kind='interp', line=89)
W('42,3622', 0o00001, '', '', 'RATT', kind='operand', line=90)
W('42,3623', 0o16205, '', 'STODL', 'RLM', kind='interp', line=91)
W('42,3624', 0o00015, '', '', 'TAT', kind='operand', line=92)
W('42,3625', 0o77624, 'CONV3', 'CALL', kind='interp', line=93)
W('42,3626', 0o33664, '', '', 'LUNPOS', 'UNIT POSITION VECTOR FROM EARTH TO MOON', kind='operand', line=94)
W('42,3627', 0o74375, '', 'VLOAD', 'VXSC', kind='interp', line=95)
W('42,3630', 0o02723, '', '', 'VMOON', kind='operand', line=96)
W('42,3631', 0o24001, '', '', 'REMDIST', 'MEAN DISTANCE FROM EARTH TO MOON', kind='operand', line=97)
W('42,3632', 0o53372, '', 'VSL1', 'VAD', kind='interp', line=98)
W('42,3633', 0o02205, '', '', 'RLM', kind='operand', line=99)
W('42,3634', 0o77650, '', 'GOTO', kind='interp', line=100)
W('42,3635', 0o65640, '', '', 'CONV5', kind='operand', line=101)
W('42,3636', 0o77775, 'CONV4', 'VLOAD', kind='interp', line=102)
W('42,3637', 0o00001, '', '', 'RATT', 'UE = -UNIT(RATT)  EARTH SPHERE', kind='operand', line=103)
W('42,3640', 0o53401, 'CONV5', 'SETPD', 'UNIT', 'UE = -UNIT((REM)(UEM) + RL)  MOON SPHERE', kind='interp', line=104)
W('42,3641', 0o00001, '', '', '0D', 'SET PL POINTER TO 0', kind='operand', line=105)
W('42,3642', 0o45076, '', 'VCOMP', 'CALL', kind='interp', line=106)
W('42,3643', 0o47537, '', '', 'CDUTRIG', 'COMPUTE SINES AND COSINES OF CDU ANGLES', kind='operand', line=107)
W('42,3644', 0o76521, '', 'MXV', 'VSL1', 'TRANSFORM REF. COORDINATE SYSTEM TO', kind='interp', line=108)
W('42,3645', 0o01734, '', '', 'REFSMMAT', 'STABLE MEMBER  B-1 X B-1 X B+1 = B-1', kind='operand', line=109)
W('42,3646', 0o71206, '', 'PUSH', 'DLOAD', '8D', kind='interp', line=110)
W('42,3647', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=111)
W('42,3650', 0o02201, '', 'STORE', 'PITCHANG', kind='interp', line=112)
W('42,3651', 0o26203, '', 'STOVL', 'YAWANG', 'ZERO OUT ANGLES', kind='interp', line=113)
W('42,3652', 0o77624, '', 'CALL', kind='interp', line=114)
W('42,3653', 0o47671, '', '', '*SMNB*', kind='operand', line=115)
W('42,3654', 0o16205, '', 'STODL', 'RLM', 'PRE-MULTIPLY RLM BY (NBSA) MATRIX(B0)', kind='interp', line=116)
W('42,3655', 0o02207, '', '', 'RLM +2', kind='operand', line=117)
W('42,3656', 0o45206, '', 'PUSH', 'DSU', kind='interp', line=118)
W('42,3657', 0o02205, '', '', 'RLM', kind='operand', line=119)
W('42,3660', 0o77605, '', 'DMP', kind='interp', line=120)
W('42,3661', 0o25771, '', '', '1OVSQRT2', kind='operand', line=121)
W('42,3662', 0o16207, '', 'STODL', 'RLM +2', kind='interp', line=122)
W('42,3663', 0o41215, '', 'DAD', 'DMP', kind='interp', line=123)
W('42,3664', 0o02205, '', '', 'RLM', kind='operand', line=124)
W('42,3665', 0o25771, '', '', '1OVSQRT2', kind='operand', line=125)
W('42,3666', 0o26205, '', 'STOVL', 'RLM', 'R  B-1', kind='interp', line=126)
W('42,3667', 0o02205, '', '', 'RLM', kind='operand', line=127)
W('42,3670', 0o63256, '', 'UNIT', 'PDVL', kind='interp', line=128)
# Page 488
W('42,3671', 0o02205, '', '', 'RLM', kind='operand', line=130)
W('42,3672', 0o72431, '', 'VPROJ', 'VSL2', 'PROJECTION OF R ONTO LM XZ PLANE', kind='interp', line=131)
W('42,3673', 0o06516, '', '', 'HIUNITY', kind='operand', line=132)
W('42,3674', 0o40045, '', 'BVSU', 'BOV', 'CLEAR OVERFLOW INDICATOR IF ON', kind='interp', line=133)
W('42,3675', 0o02205, '', '', 'RLM', kind='operand', line=134)
W('42,3676', 0o65677, '', '', 'COVCNV', kind='operand', line=135)
W('42,3677', 0o40056, 'COVCNV', 'UNIT', 'BOV', 'EXIT ON OVERFLOW', kind='interp', line=136)
W('42,3700', 0o65745, '', '', 'SBANDEX', kind='operand', line=137)
W('42,3701', 0o47206, '', 'PUSH', 'VXV', 'URP VECTOR  B-1', kind='interp', line=138)
W('42,3702', 0o06514, '', '', 'HIUNITZ', kind='operand', line=139)
W('42,3703', 0o57572, '', 'VSL1', 'VCOMP', 'UZ X URP = -(URP X UZ)', kind='interp', line=140)
W('42,3704', 0o02205, '', 'STORE', 'RLM', 'X VEC  B-1', kind='interp', line=141)
W('42,3705', 0o63241, '', 'DOT', 'PDVL', 'SGN(X.UY) UNSCALED', kind='interp', line=142)
W('42,3706', 0o06516, '', '', 'HIUNITY', kind='operand', line=143)
W('42,3707', 0o02205, '', '', 'RLM', kind='operand', line=144)
W('42,3710', 0o75246, '', 'ABVAL', 'SIGN', kind='interp', line=145)
W('42,3711', 0o77736, '', 'ASIN', '', 'ASIN((SGN(X.UY))ABV(X)) REV B0', kind='interp', line=146)
W('42,3712', 0o26201, '', 'STOVL', 'PITCHANG', kind='interp', line=147)
W('42,3713', 0o00007, '', '', 'URP', kind='operand', line=148)
W('42,3714', 0o51041, '', 'DOT', 'BPL', kind='interp', line=149)
W('42,3715', 0o06514, '', '', 'HIUNITZ', kind='operand', line=150)
W('42,3716', 0o65723, '', '', 'NOADJUST', 'YES, -90 TO +90', kind='operand', line=151)
W('42,3717', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=152)
W('42,3720', 0o06520, '', '', 'HIDPHALF', kind='operand', line=153)
W('42,3721', 0o02201, '', '', 'PITCHANG', kind='operand', line=154)
W('42,3722', 0o02201, '', 'STORE', 'PITCHANG', kind='interp', line=155)
W('42,3723', 0o47375, 'NOADJUST', 'VLOAD', 'VXV', kind='interp', line=156)
W('42,3724', 0o00001, '', '', 'UR', 'Z = (UR X URP)', kind='operand', line=157)
W('42,3725', 0o00007, '', '', 'URP', kind='operand', line=158)
W('42,3726', 0o77772, '', 'VSL1', kind='interp', line=159)
W('42,3727', 0o16205, '', 'STODL', 'RLM', 'Z VEC  B-1', kind='interp', line=160)
W('42,3730', 0o02201, '', '', 'PITCHANG', kind='operand', line=161)
W('42,3731', 0o74356, '', 'SIN', 'VXSC', kind='interp', line=162)
W('42,3732', 0o06514, '', '', 'HIUNITZ', kind='operand', line=163)
W('42,3733', 0o71525, '', 'PDDL', 'COS', kind='interp', line=164)
W('42,3734', 0o02201, '', '', 'PITCHANG', kind='operand', line=165)
W('42,3735', 0o52361, '', 'VXSC', 'VSU', kind='interp', line=166)
W('42,3736', 0o06520, '', '', 'HIUNITX', '(UX COS ALPHA) - (UZ SIN ALPHA)', kind='operand', line=167)
W('42,3737', 0o63241, '', 'DOT', 'PDVL', 'YAW.Z', kind='interp', line=168)
W('42,3740', 0o02205, '', '', 'RLM', kind='operand', line=169)
W('42,3741', 0o02205, '', '', 'RLM', kind='operand', line=170)
W('42,3742', 0o75246, '', 'ABVAL', 'SIGN', kind='interp', line=171)
W('42,3743', 0o77736, '', 'ASIN', kind='interp', line=172)
W('42,3744', 0o02203, '', 'STORE', 'YAWANG', kind='interp', line=173)
W('42,3745', 0o77776, 'SBANDEX', 'EXIT', kind='interp', line=174)
W('42,3746', 0o31044, '', 'CA', 'EXTVBACT', line=175)
W('42,3747', 0o74747, '', 'MASK', 'BIT5', 'IS BIT5 STILL ON', line=176)
W('42,3750', 0o00006, '', 'EXTEND', line=177)
W('42,3751', 0o15472, '', 'BZF', 'ENDEXT', 'NO', line=178)
W('42,3752', 0o35017, '', 'CAF', 'PRIO5', line=179)
# Page 489
W('42,3753', 0o05146, '', 'TC', 'PRIOCHNG', line=181)
W('42,3754', 0o33767, '', 'CAF', 'V06N51', 'DISPLAY ANGLES', line=182)
W('42,3755', 0o04616, '', 'TC', 'BANKCALL', line=183)
W('42,3756', 0o20353, '', 'CADR', 'GOMARKFR', kind='data', line=184)
W('42,3757', 0o05563, '', 'TC', 'B5OFF', 'TERMINATE', line=185)
W('42,3760', 0o05563, '', 'TC', 'B5OFF', 'PROCEED', line=186)
W('42,3761', 0o05155, '', 'TC', 'ENDOFJOB', 'RECYCLE', line=187)
W('42,3762', 0o34751, '', 'CAF', 'BIT3', 'IMMEDIATE RETURN', line=188)
W('42,3763', 0o05464, '', 'TC', 'BLANKET', 'BLANK R3', line=189)
W('42,3764', 0o34740, '', 'CAF', 'PRIO4', line=190)
W('42,3765', 0o05146, '', 'TC', 'PRIOCHNG', line=191)
W('42,3766', 0o03610, '', 'TC', 'SBANDANT +2', 'YES, CONTINUE DISPLAYING ANGLES', line=192)
W('42,3767', 0o01463, 'V06N51', 'VN', '0651', kind='data', line=193)
W('42,3770', 0o26501, '1OVSQRT2', '2DEC', '.7071067815', '1/SQRT(2)', kind='data', line=194)
W('42,3771', 0o07463, kind='data', line=194)

S('UR', 'equals', 0o0, line=196)
S('URP', 'equals', 0o6, line=197)
#   SBANK= LOWSUPER

# *** END OF LNYAIDE .001 ***
