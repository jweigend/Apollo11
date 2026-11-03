"""STABLE_ORBIT.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/STABLE_ORBIT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 723-730 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('STABLE_ORBIT', 'STABLE_ORBIT.agc', 'Luminary099', pages='723-730')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     STABLE_ORBIT.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        723-730
# Mod history:  2009-05-19 RSB  Adapted from the corresponding
# Colossus249 file (there being no corresponding
# Luminary131 source-code file), using page
# images from Luminary 1A.
# 2009-06-07 RSB  Eliminated an extraneous instruction.
# 2011-01-06 JL   Fixed pseudo-label indentation.
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

# Page 723
# STABLE ORBIT RENDEZVOUS PROGRAMS (P38 AND P78)
#
# MOD NO -1             LOG SECTION - STABLE ORBIT - P38-P39
# MOD BY RUDNICKI.S     DATE 25JAN68
#
# FUNCTIONAL DESCRIPTION
#
# P38 AND P78 CALCULATE THE REQUIRED DELTA V AND OTHER INITIAL
# CONDITIONS REQUIRED BY THE AGC TO (1) PUT THE ACTIVE VEHICLE
# ON A TRANSFER TRAJECTORY THAT INTERCEPTS THE PASSIVE VEHICLE
# ORBIT A GIVEN DISTANCE, DELTA R, EITHER AHEAD OF OR BEHIND THE
# PASSIVE VEHICLE AND (2) ACTUALLY PLACE THE ACTIVE VEHICLE IN THE
# PASSIVE VEHICLE ORBIT WITH A DELTA R SEPARATION BETWEEN THE TWO
# VEHICLES
#
# CALLING SEQUENCE
#
# ASTRONAUT REQUEST THRU DSKY
#
# V37E38E         IF THIS VEHICLE IS ACTIVE VEHICLE
# V37E78E         IF OTHER VEHICLE IS ACTIVE VEHICLE
#
# INPUT
#
# (1)     SOI MANEUVER
#
# (A)  TIG        TIME OF SOI MANEUVER
# (B)  CENTANG    ORBITAL CENTRAL ANGLE OF THE PASSIVE VEHICLE
# DURING THE TRANSFER FROM TIG TO TIME OF INTERCEPT
# (C)  DELTAR     THE DESIRED SEPARATION OF THE TWO VEHICLES
# SPECIFIED AS A DISTANCE ALONG THE PASSIVE VEHICLE
# ORBIT
# (D)  OPTION     EQUALS 1 FOR SOI
#
# (2)     SOR MANEUVER
#
# (A)  TIG        TIME OF SOR MANEUVER
# (B)  CENTANG    AN OPTIONAL RESPECIFICATION OF 1 (B) ABOVE
# (C)  OPTION     EQUALS 2 FOR SOR
# (D)  DELTTIME   THE TIME REQUIRED TO TRAVERSE DELTA R WHEN
# TRAVELING AT A VELOCITY EQUAL TO THE HORIZONTAL
# VELOCITY OF THE PASSIVE VEHICLE - SAVED FROM
# SOI PHASE
# (E)  TINT       TIME OF INTERCEPT (SOI) - SAVED FROM SOI PHASE
#
# OUTPUT
#
# (1)  TRKMKCNT   NUMBER OF MARKS
# (2)  TTOGO      TIME TO GO
# (3)  +MGA       MIDDLE GIMBAL ANGLE
# Page 724
# (4)  DSPTEM1    TIME OF INTERCEPT OF PASSIVE VEHICLE ORBIT
# (FOR SOI ONLY)
# (5)  POSTTPI    PERIGEE ALTITUDE OF ACTIVE VEHICLE ORBIT AFTER
# THE SOI (SOR) MANEUVER
# (6)  DELVTPI    MAGNITUDE OF DELTA V AT SOI (SOR) TIME
# (7)  DELVTPF    MAGNITUDE OF DELTA V AT INTERCEPT TIME
# (8)  DELVLVC    DELTA VELOCITY AT SOI (AND SOR) - LOCAL VERTICAL
# COORDINATES
#
# SUBROUTINE USED
#
# AVFLAGA
# AVFLAGP
# VNDSPLY
# BANKCALL
# GOFLASHR
# GOTOPOOH
# BLANKET
# ENDOFJOB
# PREC/TT
# SELECTMU
# INTRPVP
# MAINRTNE

#   BANK 04
#   SETLOC STBLEORB
#   BANK

#   EBANK= SUBEXIT
#   COUNT* $$/P3879

W('34,3271', 0o04616, 'P38', 'TC', 'BANKCALL', line=115)
W('34,3272', 0o72347, '', 'CADR', 'AVFLAGA', 'THIS VEHICLE ACTIVE', kind='data', line=116)
W('34,3273', 0o03276, '', 'TC', '+3', line=117)
W('34,3274', 0o04616, 'P78', 'TC', 'BANKCALL', line=118)
W('34,3275', 0o72354, '', 'CADR', 'AVFLAGP', 'OTHER VEHICLE ACTIVE', kind='data', line=119)
W('34,3276', 0o04616, '', 'TC', 'BANKCALL', line=120)
W('34,3277', 0o72361, '', 'CADR', 'P20FLGON', 'SET UPDATFLG, TRACKFLG', kind='data', line=121)
W('34,3300', 0o33641, '', 'CAF', 'DECTWO', line=122)
W('34,3301', 0o55466, '', 'TS', 'NN', line=123)
W('34,3302', 0o33632, '', 'CAF', 'V06N33SR', 'DISPLAY TIG', line=124)
W('34,3303', 0o03621, '', 'TC', 'VNDSPLY', line=125)
W('34,3304', 0o33633, '', 'CAF', 'V06N55SR', 'DISPLAY CENTANG', line=126)
W('34,3305', 0o04616, '', 'TCR', 'BANKCALL', line=127)
W('34,3306', 0o20635, '', 'CADR', 'GOFLASHR', kind='data', line=128)
W('34,3307', 0o16001, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=129)
W('34,3310', 0o13315, '', 'TCF', '+5', 'PROCEED', line=130)
W('34,3311', 0o13304, '', 'TCF', '-5', 'RECYCLE', line=131)
W('34,3312', 0o36245, '', 'CAF', 'THREE', 'IMMEDIATE RETURN - BLANK R1, R2', line=132)
W('34,3313', 0o05464, '', 'TCR', 'BLANKET', line=133)
# Page 725
W('34,3314', 0o15155, '', 'TCF', 'ENDOFJOB', line=135)
W('34,3315', 0o34756, '', 'CAF', 'FIVE', line=136)
W('34,3316', 0o55144, '', 'TS', 'OPTION1', line=137)
W('34,3317', 0o34753, '', 'CAF', 'ONE', line=138)
W('34,3320', 0o55145, '', 'TS', 'OPTION2', 'OPTION CODE IS SET TO 1', line=139)
W('34,3321', 0o33634, '', 'CAF', 'V04N06SR', 'DISPLAY OPTION CODE - 1 = SOI, 2 = SOR', line=140)
W('34,3322', 0o04616, '', 'TCR', 'BANKCALL', line=141)
W('34,3323', 0o20635, '', 'CADR', 'GOFLASHR', kind='data', line=142)
W('34,3324', 0o16001, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=143)
W('34,3325', 0o13332, '', 'TCF', '+5', 'PROCEED', line=144)
W('34,3326', 0o13321, '', 'TCF', '-5', 'RECYCLE', line=145)
W('34,3327', 0o34751, '', 'CAF', 'BIT3', 'IMMEDIATE RETURN - BLANK R3', line=146)
W('34,3330', 0o05464, '', 'TCR', 'BLANKET', line=147)
W('34,3331', 0o15155, '', 'TCF', 'ENDOFJOB', line=148)
W('34,3332', 0o06037, '', 'TC', 'INTPRET', line=149)
W('34,3333', 0o70535, '', 'SLOAD', 'SR1', kind='interp', line=150)
W('34,3334', 0o01146, '', '', 'OPTION2', kind='operand', line=151)
W('34,3335', 0o71230, '', 'BHIZ', 'DLOAD', kind='interp', line=152)
W('34,3336', 0o71344, '', '', 'OPTN1', kind='operand', line=153)
W('34,3337', 0o03631, '', '', 'TINT', kind='operand', line=154)
W('34,3340', 0o02303, '', 'STORE', 'TINTSOI', 'STORE FOR SOR PHASE', kind='interp', line=155)
W('34,3341', 0o77614, '', 'CLRGO', kind='interp', line=156)
W('34,3342', 0o01230, '', '', 'OPTNSW', 'OPTNSW: ON = SOI, OFF = SOR', kind='operand', line=157)
W('34,3343', 0o71375, '', '', 'JUNCTN1', kind='operand', line=158)
W('34,3344', 0o43014, 'OPTN1', 'SET', 'CLEAR', 'SOI', kind='interp', line=159)
W('34,3345', 0o01070, '', '', 'OPTNSW', kind='operand', line=160)
W('34,3346', 0o00670, '', '', 'UPDATFLG', kind='operand', line=161)
W('34,3347', 0o77624, '', 'CALL', kind='interp', line=162)
W('34,3350', 0o71554, '', '', 'PREC/TT', kind='operand', line=163)
W('34,3351', 0o43015, '', 'DAD', 'SET', kind='interp', line=164)
W('34,3352', 0o03442, '', '', 'TIG', kind='operand', line=165)
W('34,3353', 0o00470, '', '', 'UPDATFLG', kind='operand', line=166)
W('34,3354', 0o03631, '', 'STORE', 'TINT', 'TI = TIG + TF', kind='interp', line=167)
W('34,3355', 0o77776, '', 'EXIT', kind='interp', line=168)
W('34,3356', 0o33635, '', 'CAF', 'V06N57SR', 'DISPLAY DELTA R', line=169)
W('34,3357', 0o04616, '', 'TCR', 'BANKCALL', line=170)
W('34,3360', 0o20635, '', 'CADR', 'GOFLASHR', kind='data', line=171)
W('34,3361', 0o16001, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=172)
W('34,3362', 0o13367, '', 'TCF', '+5', 'PROCEED', line=173)
W('34,3363', 0o13356, '', 'TCF', '-5', 'RECYCLE', line=174)
W('34,3364', 0o36242, '', 'CAF', 'SIX', 'IMMEDIATE RETURN - BLANK R2, R3', line=175)
W('34,3365', 0o05464, '', 'TCR', 'BLANKET', line=176)
W('34,3366', 0o15155, '', 'TCF', 'ENDOFJOB', line=177)
W('34,3367', 0o00006, '', 'EXTEND', line=178)
W('34,3370', 0o31631, '', 'DCA', 'TINT', line=179)
W('34,3371', 0o53046, '', 'DXCH', 'DSPTEM1', 'FOR DISPLAY', line=180)
W('34,3372', 0o33636, '', 'CAF', 'V06N34SR', 'DISPLAY TIME OF INTERCEPT', line=181)
W('34,3373', 0o03621, '', 'TC', 'VNDSPLY', line=182)
W('34,3374', 0o06037, '', 'TC', 'INTPRET', line=183)
W('34,3375', 0o45014, 'JUNCTN1', 'CLEAR', 'CALL', kind='interp', line=184)
# Page 726
W('34,3376', 0o04266, '', '', 'P39/79SW', kind='operand', line=186)
W('34,3377', 0o20000, '', '', 'SELECTMU', 'SELECT MU, CLEAR FINALFLG, GO TO VN1645', kind='operand', line=187)
W('34,3400', 0o77624, 'RECYCLE', 'CALL', kind='interp', line=188)
W('34,3401', 0o71554, '', '', 'PREC/TT', kind='operand', line=189)
W('34,3402', 0o71214, '', 'BOFF', 'DLOAD', kind='interp', line=190)
W('34,3403', 0o01350, '', '', 'OPTNSW', kind='operand', line=191)
W('34,3404', 0o71424, '', '', 'OPTN2', kind='operand', line=192)
W('34,3405', 0o03631, '', '', 'TINT', kind='operand', line=193)
W('34,3406', 0o34041, '', 'STCALL', 'TDEC1', 'PRECISION UPDATE PASSIVE VEHICLE TO', kind='interp', line=194)
W('34,3407', 0o71605, '', '', 'INTRPVP', '      INTERCEPT TIME', kind='operand', line=195)
W('34,3410', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=196)
W('34,3411', 0o00001, '', '', 'RATT', 'RP/(RP)', kind='operand', line=197)
W('34,3412', 0o47315, '', 'PDVL', 'VXV', kind='interp', line=198)
W('34,3413', 0o00007, '', '', 'VATT', kind='operand', line=199)
W('34,3414', 0o60246, '', 'ABVAL', 'NORM', '(VP X RP/(RP))', kind='interp', line=200)
W('34,3415', 0o00047, '', '', 'X1', kind='operand', line=201)
W('34,3416', 0o56325, '', 'PDDL', 'DDV', kind='interp', line=202)
W('34,3417', 0o02303, '', '', 'DELTAR', kind='operand', line=203)
W('34,3420', 0o77657, '', 'SL*', '', 'DELTA R / (VP X RP/RP)', kind='interp', line=204)
W('34,3421', 0o20172, '', '', '0 -7,1', kind='operand', line=205)
W('34,3422', 0o36305, '', 'STCALL', 'DELTTIME', 'DELTA T = (RP) DELTA R / (VP X RP)', kind='interp', line=206)
W('34,3423', 0o71430, '', '', 'JUNCTN2', kind='operand', line=207)
W('34,3424', 0o43345, 'OPTN2', 'DLOAD', 'DAD', kind='interp', line=208)
W('34,3425', 0o02303, '', '', 'TINTSOI', kind='operand', line=209)
W('34,3426', 0o00037, '', '', 'T', kind='operand', line=210)
W('34,3427', 0o03631, '', 'STORE', 'TINT', 'TI = TI + TF', kind='interp', line=211)
W('34,3430', 0o45345, 'JUNCTN2', 'DLOAD', 'DSU', kind='interp', line=212)
W('34,3431', 0o03631, '', '', 'TINT', kind='operand', line=213)
W('34,3432', 0o02305, '', '', 'DELTTIME', kind='operand', line=214)
W('34,3433', 0o02307, '', 'STORE', 'TARGTIME', 'TT = TI - DELTA T', kind='interp', line=215)

# .... MAINRTNE ....
# SUBROUTINES USED:
#
# S3435.25
# PERIAPO1
# SHIFTR1
# VNDSPLY
# BANKCALL
# GOFLASH
# GOTOPOOH
# VN1645

W('34,3434', 0o34041, 'MAINRTNE', 'STCALL', 'TDEC1', 'PRECISION UPDATE PASSIVE VEHICLE TO', kind='interp', line=229)
W('34,3435', 0o71605, '', '', 'INTRPVP', '      TARGET TIME', kind='operand', line=230)
W('34,3436', 0o77745, '', 'DLOAD', kind='interp', line=231)
W('34,3437', 0o03442, '', '', 'TIG', kind='operand', line=232)
W('34,3440', 0o03610, '', 'STORE', 'INTIME', kind='interp', line=233)
W('34,3441', 0o77331, '', 'SSP', 'VLOAD', kind='interp', line=234)
W('34,3442', 0o03471, '', '', 'SUBEXIT', kind='operand', line=235)
W('34,3443', 0o71447, '', '', 'TEST3979', kind='operand', line=236)
# Page 727
W('34,3444', 0o00001, '', '', 'RATT', kind='operand', line=238)
W('34,3445', 0o77624, '', 'CALL', kind='interp', line=239)
W('34,3446', 0o73327, '', '', 'S3435.25', kind='operand', line=240)
W('34,3447', 0o43014, 'TEST3979', 'BOFF', 'BON', kind='interp', line=241)
W('34,3450', 0o04346, '', '', 'P39/79SW', kind='operand', line=242)
W('34,3451', 0o71460, '', '', 'MAINRTN1', kind='operand', line=243)
W('34,3452', 0o01311, '', '', 'FINALFLG', kind='operand', line=244)
W('34,3453', 0o71456, '', '', 'P39P79', kind='operand', line=245)
W('34,3454', 0o77614, '', 'SET', kind='interp', line=246)
W('34,3455', 0o00470, '', '', 'UPDATFLG', kind='operand', line=247)
W('34,3456', 0o77776, 'P39P79', 'EXIT', kind='interp', line=248)
W('34,3457', 0o03505, '', 'TC', 'DSPLY81', 'FOR P39 AND P79', line=249)
W('34,3460', 0o51575, 'MAINRTN1', 'VLOAD', 'ABVAL', kind='interp', line=250)
W('34,3461', 0o02366, '', '', 'DELVEET3', kind='operand', line=251)
W('34,3462', 0o27576, '', 'STOVL', 'DELVTPI', 'DELTA V', kind='interp', line=252)
W('34,3463', 0o03506, '', '', 'VPASS4', kind='operand', line=253)
W('34,3464', 0o51451, '', 'VSU', 'ABVAL', kind='interp', line=254)
W('34,3465', 0o03566, '', '', 'VTPRIME', kind='operand', line=255)
W('34,3466', 0o26350, '', 'STOVL', 'DELVTPF', "DELTA V (FINAL) = V'T - VT", kind='interp', line=256)
W('34,3467', 0o03536, '', '', 'RACT3', kind='operand', line=257)
W('34,3470', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=258)
W('34,3471', 0o02337, '', '', 'VIPRIME', kind='operand', line=259)
W('34,3472', 0o46316, '', '', 'PERIAPO1', 'GET PERIGEE ALTITUDE', kind='operand', line=260)
W('34,3473', 0o77624, '', 'CALL', kind='interp', line=261)
W('34,3474', 0o46426, '', '', 'SHIFTR1', kind='operand', line=262)
W('34,3475', 0o03606, '', 'STORE', 'POSTTPI', kind='interp', line=263)
W('34,3476', 0o43014, '', 'BON', 'SET', kind='interp', line=264)
W('34,3477', 0o01311, '', '', 'FINALFLG', kind='operand', line=265)
W('34,3500', 0o71502, '', '', 'DSPLY58', kind='operand', line=266)
W('34,3501', 0o00470, '', '', 'UPDATFLG', kind='operand', line=267)
W('34,3502', 0o77776, 'DSPLY58', 'EXIT', kind='interp', line=268)
W('34,3503', 0o33637, '', 'CAF', 'V06N58SR', 'DISPLAY HP, DELTA V, DELTA V (FINAL)', line=269)
W('34,3504', 0o03621, '', 'TC', 'VNDSPLY', line=270)
W('34,3505', 0o33640, 'DSPLY81', 'CAF', 'V06N81SR', 'DISPLAY DELTA V (LV)', line=271)
W('34,3506', 0o03621, '', 'TC', 'VNDSPLY', line=272)
W('34,3507', 0o06037, '', 'TC', 'INTPRET', line=273)
W('34,3510', 0o77214, '', 'CLEAR', 'VLOAD', kind='interp', line=274)
W('34,3511', 0o01267, '', '', 'XDELVFLG', kind='operand', line=275)
W('34,3512', 0o02366, '', '', 'DELVEET3', kind='operand', line=276)
W('34,3513', 0o37656, '', 'STCALL', 'DELVSIN', kind='interp', line=277)
W('34,3514', 0o73606, '', '', 'VN1645', 'DISPLAY TRKMKCNT, TTOGO, +MGA', kind='operand', line=278)
W('34,3515', 0o52014, '', 'BON', 'GOTO', kind='interp', line=279)
W('34,3516', 0o04306, '', '', 'P39/79SW', kind='operand', line=280)
W('34,3517', 0o71541, '', '', 'P39/P79B', kind='operand', line=281)
W('34,3520', 0o71400, '', '', 'RECYCLE', kind='operand', line=282)

# STABLE ORBIT MIDCOURSE PROGRAM (P39 AND P79)
#
# MOD NO -1             LOG SECTION - STABLE ORBIT - P38-P39
# MOD BY RUDNICKI.S     DATE 25JAN68
#
# Page 728
# FUNCTIONAL DESCRIPTION
#
# P39 AND P79 CALCULATE THE REQUIRED DELTA V AND OTHER INITIAL
# CONDITIONS REQUIRED BY THE AGC TO MAKE A MIDCOURSE CORRECTION
# MANEUVER AFTER COMPLETING THE SOI MANEUVER BUT BEFORE MAKING
# THE SOR MANEUVER.
#
# CALLING SEQUENCE
#
# ASTRONAUT REQUEST THRU DSKY
#
# V37E39E         IF THIS VEHICLE IS ACTIVE VEHICLE
# V37E79E         IF OTHER VEHICLE IS ACTIVE VEHICLE
#
# INPUT
#
# (1)  TPASS4     TIME OF INTERCEPT - SAVED FROM P38/P78
# (2)  TARGTIME   TIME THAT PASSIVE VEHICLE IS AT INTERCEPT POINT -
# SAVED FROM P38/P78
#
# OUTPUT
#
# (1)  TRKMKCNT   NUMBER OF MARKS.
# (2)  TTOGO      TIME TO GO
# (3)  +MGA       MIDDLE GIMBAL ANGLE
# (4)  DELVLVC    DELTA VELOCITY AT MID - LOCAL VERTICAL COORDINATES
#
# SUBROUTINES USED
#
# AVFLAGA
# AVFLAGP
# LOADTIME
# SELECTMU
# PRECSET
# S34/35.1
# MAINRTNE

W('34,3521', 0o04616, 'P39', 'TC', 'BANKCALL', line=327)
W('34,3522', 0o72347, '', 'CADR', 'AVFLAGA', 'THIS VEHICLE ACTIVE', kind='data', line=328)
W('34,3523', 0o00006, '', 'EXTEND', line=329)
W('34,3524', 0o31401, '', 'DCA', 'ATIGINC', line=330)
W('34,3525', 0o03532, '', 'TC', 'P39/P79A', line=331)
W('34,3526', 0o04616, 'P79', 'TC', 'BANKCALL', line=332)
W('34,3527', 0o72354, '', 'CADR', 'AVFLAGP', 'OTHER VEHICLE ACTIVE', kind='data', line=333)
W('34,3530', 0o00006, '', 'EXTEND', line=334)
W('34,3531', 0o31403, '', 'DCA', 'PTIGINC', line=335)
W('34,3532', 0o53576, 'P39/P79A', 'DXCH', 'KT', 'TIME TO PREPARE FOR BURN', line=336)
W('34,3533', 0o04616, '', 'TC', 'BANKCALL', line=337)
W('34,3534', 0o72361, '', 'CADR', 'P20FLGON', 'SET UPDATFLG, TRACKFLG', kind='data', line=338)
W('34,3535', 0o06037, '', 'TC', 'INTPRET', line=339)
# Page 729
W('34,3536', 0o45014, '', 'SET', 'CALL', kind='interp', line=341)
W('34,3537', 0o04066, '', '', 'P39/79SW', kind='operand', line=342)
W('34,3540', 0o20000, '', '', 'SELECTMU', 'SELECT MU, CLEAR FINALFLG, GO TO VN1645', kind='operand', line=343)
W('34,3541', 0o43234, 'P39/P79B', 'RTB', 'DAD', kind='interp', line=344)
W('34,3542', 0o21573, '', '', 'LOADTIME', kind='operand', line=345)
W('34,3543', 0o03576, '', '', 'KT', kind='operand', line=346)
W('34,3544', 0o03442, '', 'STORE', 'TIG', 'TIG = T (PRESENT) + PREPARATION TIME', kind='interp', line=347)
W('34,3545', 0o34041, '', 'STCALL', 'TDEC1', 'PRECISION UPDATE ACTIVE AND PASSIVE', kind='interp', line=348)
W('34,3546', 0o46360, '', '', 'PRECSET', '      VEHICLES TO TIG', kind='operand', line=349)
W('34,3547', 0o77624, '', 'CALL', kind='interp', line=350)
W('34,3550', 0o73274, '', '', 'S34/35.1', 'GET UNIT NORMAL', kind='operand', line=351)
W('34,3551', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=352)
W('34,3552', 0o02307, '', '', 'TARGTIME', kind='operand', line=353)
W('34,3553', 0o71434, '', '', 'MAINRTNE', 'CALCULATE DELTA V AND DELTA V (LV)', kind='operand', line=354)

# .... PREC/TT ....
# SUBROUTINES USED
#
# PRECSET
# TIMETHET
# S34/35.1

W('34,3554', 0o71220, 'PREC/TT', 'STQ', 'DLOAD', kind='interp', line=363)
W('34,3555', 0o03465, '', '', 'RTRN', kind='operand', line=364)
W('34,3556', 0o03442, '', '', 'TIG', kind='operand', line=365)
W('34,3557', 0o34041, '', 'STCALL', 'TDEC1', 'PRECISION UPDATE ACTIVE AND PASSIVE', kind='interp', line=366)
W('34,3560', 0o46360, '', '', 'PRECSET', '      VEHICLES TO TIG', kind='operand', line=367)
W('34,3561', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=368)
W('34,3562', 0o03552, '', '', 'RPASS3', kind='operand', line=369)
W('34,3563', 0o57176, '', '', '0,2', kind='operand', line=370)
W('34,3564', 0o16655, '', 'STODL', 'RVEC', kind='interp', line=371)
W('34,3565', 0o03621, '', '', 'CENTANG', kind='operand', line=372)
W('34,3566', 0o71406, '', 'PUSH', 'COS', kind='interp', line=373)
W('34,3567', 0o16732, '', 'STODL', 'CSTH', kind='interp', line=374)
W('34,3570', 0o43156, '', 'SIN', 'SET', kind='interp', line=375)
W('34,3571', 0o03466, '', '', 'RVSW', kind='operand', line=376)
W('34,3572', 0o26730, '', 'STOVL', 'SNTH', kind='interp', line=377)
W('34,3573', 0o03560, '', '', 'VPASS3', kind='operand', line=378)
W('34,3574', 0o77657, '', 'VSR*', kind='interp', line=379)
W('34,3575', 0o57176, '', '', '0,2', kind='operand', line=380)
W('34,3576', 0o36744, '', 'STCALL', 'VVEC', 'GET TRANSFER TIME BASED ON CENTANG OF', kind='interp', line=381)
W('34,3577', 0o24732, '', '', 'TIMETHET', '      PASSIVE VEHICLE', kind='operand', line=382)
W('34,3600', 0o77624, '', 'CALL', kind='interp', line=383)
W('34,3601', 0o73274, '', '', 'S34/35.1', 'GET UNIT NORMAL', kind='operand', line=384)
W('34,3602', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=385)
W('34,3603', 0o00037, '', '', 'T', kind='operand', line=386)
W('34,3604', 0o03465, '', '', 'RTRN', kind='operand', line=387)

# .... INTRPVP ....
# SUBROUTINES USED
#
# CSMPREC
# Page 730
# LEMPREC

W('34,3605', 0o43020, 'INTRPVP', 'STQ', 'BOFF', 'PRECISION UPDATE PASSIVE VEHICLE TO', kind='interp', line=396)
W('34,3606', 0o03465, '', '', 'RTRN', '      TDEC1', kind='operand', line=397)
W('34,3607', 0o01352, '', '', 'AVFLAG', kind='operand', line=398)
W('34,3610', 0o71615, '', '', 'OTHERV', kind='operand', line=399)
W('34,3611', 0o77624, '', 'CALL', kind='interp', line=400)
W('34,3612', 0o27043, '', '', 'CSMPREC', kind='operand', line=401)
W('34,3613', 0o77650, '', 'GOTO', kind='interp', line=402)
W('34,3614', 0o03465, '', '', 'RTRN', kind='operand', line=403)
W('34,3615', 0o77624, 'OTHERV', 'CALL', kind='interp', line=404)
W('34,3616', 0o27057, '', '', 'LEMPREC', kind='operand', line=405)
W('34,3617', 0o77650, '', 'GOTO', kind='interp', line=406)
W('34,3620', 0o03465, '', '', 'RTRN', kind='operand', line=407)

# .... VNDSPLY ....
# SUBROUTINES USED
#
# BANKCALL
# GOFLASH
# GOTOPOOH

W('34,3621', 0o00006, 'VNDSPLY', 'EXTEND', '', 'FLASH DISPLAY', line=416)
W('34,3622', 0o23465, '', 'QXCH', 'RTRN', line=417)
W('34,3623', 0o55615, '', 'TS', 'VERBNOUN', line=418)
W('34,3624', 0o31615, '', 'CA', 'VERBNOUN', line=419)
W('34,3625', 0o04616, '', 'TCR', 'BANKCALL', line=420)
W('34,3626', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=421)
W('34,3627', 0o16001, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=422)
W('34,3630', 0o01465, '', 'TC', 'RTRN', 'PROCEED', line=423)
W('34,3631', 0o13624, '', 'TCF', '-5', 'RECYCLE', line=424)
W('34,3632', 0o01441, 'V06N33SR', 'VN', '0633', kind='data', line=425)
W('34,3633', 0o01467, 'V06N55SR', 'VN', '0655', kind='data', line=426)
W('34,3634', 0o01006, 'V04N06SR', 'VN', '0406', kind='data', line=427)
W('34,3635', 0o01471, 'V06N57SR', 'VN', '0657', kind='data', line=428)
W('34,3636', 0o01442, 'V06N34SR', 'VN', '0634', kind='data', line=429)
W('34,3637', 0o01472, 'V06N58SR', 'VN', '0658', kind='data', line=430)
W('34,3640', 0o01521, 'V06N81SR', 'VN', '0681', kind='data', line=431)
W('34,3641', 0o00002, 'DECTWO', 'OCT', '2', kind='data', line=432)

# *** END OF KISSING  .050 ***
