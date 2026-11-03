"""IMU_COMPENSATION_PACKAGE.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/IMU_COMPENSATION_PACKAGE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 326-337 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('IMU_COMPENSATION_PACKAGE', 'IMU_COMPENSATION_PACKAGE.agc', 'Luminary099', pages='326-337')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     IMU_COMPENSATION_PACKAGE.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        326-337
# Mod history:  2009-05-16 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2009-06-07 RSB  Corrected a typo.
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

# Page 326
#   BANK 7
#   SETLOC IMUCOMP
#   BANK

#   EBANK= NBDX

#   COUNT* $$/ICOMP
W('06,3263', 0o33531, '1/PIPA', 'CAF', 'LGCOMP', 'SAVE EBANK OF CALLING PROGRAM', line=38)
W('06,3264', 0o56003, '', 'XCH', 'EBANK', line=39)
W('06,3265', 0o54163, '', 'TS', 'MODE', line=40)

W('06,3266', 0o11477, '', 'CCS', 'GCOMPSW', 'BYPASS IF GCOMPSW NEGATIVE', line=42)
W('06,3267', 0o13272, '', 'TCF', '+3', line=43)
W('06,3270', 0o13272, '', 'TCF', '+2', line=44)
W('06,3271', 0o13353, '', 'TCF', 'IRIG1', 'RETURN', line=45)

W('06,3272', 0o34751, '1/PIPA1', 'CAF', 'FOUR', 'PIPAZ, PIPAY, PIPAX', line=47)
W('06,3273', 0o54132, '', 'TS', 'BUF +2', line=48)

W('06,3274', 0o50132, '', 'INDEX', 'BUF +2', line=50)
W('06,3275', 0o31453, '', 'CA', 'PIPASCF', '(P.P.M.) X 2(-9)', line=51)
W('06,3276', 0o00006, '', 'EXTEND', line=52)
W('06,3277', 0o50132, '', 'INDEX', 'BUF +2', line=53)
W('06,3300', 0o70324, '', 'MP', 'DELVX', '(PP) X 2(+14) NOW (PIPA PULSES) X 2(+5)', line=54)
W('06,3301', 0o54002, '', 'TS', 'Q', 'SAVE MAJOR PART', line=55)

W('06,3302', 0o30001, '', 'CA', 'L', 'MINOR PART', line=57)
W('06,3303', 0o00006, '', 'EXTEND', line=58)
W('06,3304', 0o74746, '', 'MP', 'BIT6', 'SCALE 2(+9)   SHIFT RIGHT 9', line=59)
W('06,3305', 0o50132, '', 'INDEX', 'BUF +2', line=60)
W('06,3306', 0o54325, '', 'TS', 'DELVX +1', 'FRACTIONAL PIPA PULSES SCALED 2(+14)', line=61)

W('06,3307', 0o30002, '', 'CA', 'Q', 'MAJOR PART', line=63)
W('06,3310', 0o00006, '', 'EXTEND', line=64)
W('06,3311', 0o74746, '', 'MP', 'BIT6', 'SCALE 2(+9)   SHIFT RIGHT 9', line=65)
W('06,3312', 0o50132, '', 'INDEX', 'BUF +2', line=66)
W('06,3313', 0o20325, '', 'DAS', 'DELVX', '(PIPAI) + (PIPAI)(SFE)', line=67)

W('06,3314', 0o50132, '', 'INDEX', 'BUF +2', line=69)
W('06,3315', 0o41452, '', 'CS', 'PIPABIAS', '(PIPA PULSES)/(CS) X 2(-5)             *', line=70)
W('06,3316', 0o00006, '', 'EXTEND', line=71)
W('06,3317', 0o71075, '', 'MP', '1/PIPADT', '(CS) X 2(+8)  NOW (PIPA PULSES) X 2(+3)*', line=72)
W('06,3320', 0o00006, '', 'EXTEND', line=73)
W('06,3321', 0o74750, '', 'MP', 'BIT4', 'SCALE 2(+11)  SHIFT RIGHT 11           *', line=74)
W('06,3322', 0o50132, '', 'INDEX', 'BUF +2', line=75)
W('06,3323', 0o20325, '', 'DAS', 'DELVX', '(PIPAI) + (PIPAI)(SFE) - (BIAS)(DELTAT)', line=76)

W('06,3324', 0o10132, '', 'CCS', 'BUF +2', 'PIPAZ, PIPAY, PIPAX', line=78)
W('06,3325', 0o67747, '', 'AD', 'NEG1', line=79)
W('06,3326', 0o13273, '', 'TCF', '1/PIPA1 +1', line=80)
# Page 327
W('06,3327', 0o13330, '', 'NOOP', '', 'LESS THAN ZERO IMPOSSIBLE', line=82)

# Page 328
W('06,3330', 0o55477, 'IRIGCOMP', 'TS', 'GCOMPSW', 'INDICATE COMMANDS 2 PULSES OR LESS.', line=85)
W('06,3331', 0o54130, '', 'TS', 'BUF', 'INDEX COUNTER .  IRIGX, IRIGY, IRIGZ.', line=86)

W('06,3332', 0o03356, '', 'TC', 'IRIGX', 'COMPENSATE ACCELERATION TERMS', line=88)

W('06,3333', 0o41460, '', 'CS', 'NBDX', '(GYRO PULSES)/(CS) X 2(-5)', line=90)
W('06,3334', 0o03454, '', 'TC', 'DRIFTSUB', '-(NBOX)(DELTAT)   (GYRO PULSES) X 2(+14)', line=91)

W('06,3335', 0o03373, '', 'TC', 'IRIGY', 'COMPENSATE ACCELERATION TERMS', line=93)

W('06,3336', 0o41461, '', 'CS', 'NBDY', '(GYRO PULSES)/(CS) X 2(-5)', line=95)
W('06,3337', 0o03454, '', 'TC', 'DRIFTSUB', '-(NBDY)(DELTAT)   (GYRO PULSES) X 2(+14)', line=96)

W('06,3340', 0o03410, '', 'TC', 'IRIGZ', 'COMPENSATE ACCELERATION TERMS', line=98)

W('06,3341', 0o31462, '', 'CA', 'NBDZ', '(GYRO PULSES)/(CS) X 2(-5)', line=100)
W('06,3342', 0o03454, '', 'TC', 'DRIFTSUB', '+(NBDZ)(DELTAT)   (GYRO PULSES) X 2(+14)', line=101)

W('06,3343', 0o11477, '', 'CCS', 'GCOMPSW', 'ARE GYRO COMMANDS GREATER THAN 2 PULSES', line=103)
W('06,3344', 0o13346, '', 'TCF', '+2', 'YES  SEND OUT GYRO TORQUING COMMANDS.', line=104)
W('06,3345', 0o13353, '', 'TCF', 'IRIG1', 'NO  RETURN', line=105)

W('06,3346', 0o35031, '', 'CA', 'PRIO21', 'PRIO GREATER THAN SERVICER', line=107)
W('06,3347', 0o05072, '', 'TC', 'NOVAC', 'SEND OUT GYRO TORQUING COMMANDS.', line=108)
#   EBANK= NBDX
W('06,3350', 0o03507, '', '2CADR', '1/GYRO', kind='data', line=110)
W('06,3351', 0o14063, kind='data', line=110)

W('06,3352', 0o00003, '', 'RELINT', line=112)
W('06,3353', 0o30163, 'IRIG1', 'CA', 'MODE', 'RESTORE CALLERS EBANK', line=113)
W('06,3354', 0o54003, '', 'TS', 'EBANK', line=114)
W('06,3355', 0o14631, '', 'TCF', 'SWRETURN', line=115)

# Page 329
W('06,3356', 0o00006, 'IRIGX', 'EXTEND', line=118)
W('06,3357', 0o22156, '', 'QXCH', 'MPAC +2', 'SAVE Q', line=119)
W('06,3360', 0o00006, '', 'EXTEND', line=120)
W('06,3361', 0o40325, '', 'DCS', 'DELVX', '(PIPA PULSES) X 2(+14)', line=121)
W('06,3362', 0o52155, '', 'DXCH', 'MPAC', line=122)
W('06,3363', 0o31463, '', 'CA', 'ADIAX', '(GYRO PULSES)/(PIPA PULSE) X 2(-6)     *', line=123)
W('06,3364', 0o03425, '', 'TC', 'GCOMPSUB', '-(ADIAX)(PIPAX)   (GYRO PULSES) X 2(+14)', line=124)

W('06,3365', 0o00006, '', 'EXTEND', line=126)
W('06,3366', 0o40327, '', 'DCS', 'DELVY', '(PIPA PULSES) X 2(+14)', line=127)
W('06,3367', 0o52155, '', 'DXCH', 'MPAC', line=128)
W('06,3370', 0o41466, '', 'CS', 'ADSRAX', '(GYRO PULSES)/(PIPA PULSE) X 2(-6)     *', line=129)
W('06,3371', 0o03425, '', 'TC', 'GCOMPSUB', '+(ADSRAX)(PIPAY)  (GYRO PULSES) X 2(+14)', line=130)

# EXTEND           # ***
# DCS     DELVZ    # ***    (PIPA PULSES) X 2(+14)
# DXCH    MPAC     # ***
# CA      ADOAX    # ***    (GYRO PULSES)/(PIPA PULSE) X 2(-6)     *
# TC      GCOMPSUB # ***    -(ADOAX)(PIPAZ)   (GYRO PULSES) X 2(+14)

W('06,3372', 0o00156, '', 'TC', 'MPAC +2', line=138)

W('06,3373', 0o00006, 'IRIGY', 'EXTEND', line=140)
W('06,3374', 0o22156, '', 'QXCH', 'MPAC +2', 'SAVE Q', line=141)
W('06,3375', 0o00006, '', 'EXTEND', line=142)
W('06,3376', 0o40327, '', 'DCS', 'DELVY', '(PIPA PULSES) X 2(+14)', line=143)
W('06,3377', 0o52155, '', 'DXCH', 'MPAC', line=144)
W('06,3400', 0o31464, '', 'CA', 'ADIAY', '(GYRO PULSES)/(PIPA PULSE) X 2(-6)     *', line=145)
W('06,3401', 0o03425, '', 'TC', 'GCOMPSUB', '-(ADIAY)(PIPAY)   (GYRO PULSES) X 2(+14)', line=146)

W('06,3402', 0o00006, '', 'EXTEND', line=148)
W('06,3403', 0o40331, '', 'DCS', 'DELVZ', '(PIPA PULSES) X 2(+14)', line=149)
W('06,3404', 0o52155, '', 'DXCH', 'MPAC', line=150)
W('06,3405', 0o41467, '', 'CS', 'ADSRAY', '(GYRO PULSES)/(PIPA PULSE) X 2(-6)     *', line=151)
W('06,3406', 0o03425, '', 'TC', 'GCOMPSUB', '+(ADSRAY)(PIPAZ)  (GYRO PULSES) X 2(+14)', line=152)

# EXTEND           # ***
# DCS     DELVX    # ***    (PIPA PULSES) X 2(+14)
# DXCH    MPAC     # ***
# CA      ADOAY    # ***    (GYRO PULSES)/(PIPA PULSE) X 2(-6)     *
# TC      GCOMPSUB # ***    -(ADOAY)(PIPAX)   (GYRO PULSES) X 2(+14)

W('06,3407', 0o00156, '', 'TC', 'MPAC +2', line=160)

W('06,3410', 0o00006, 'IRIGZ', 'EXTEND', line=162)
W('06,3411', 0o22156, '', 'QXCH', 'MPAC +2', 'SAVE Q', line=163)
W('06,3412', 0o00006, '', 'EXTEND', line=164)
W('06,3413', 0o40327, '', 'DCS', 'DELVY', '(PIPA PULSES) X 2(+14)', line=165)
W('06,3414', 0o52155, '', 'DXCH', 'MPAC', line=166)
W('06,3415', 0o31470, '', 'CA', 'ADSRAZ', '(GYRO PULSES)/(PIPA PULSE) X 2(-6)     *', line=167)
# Page 330
W('06,3416', 0o03425, '', 'TC', 'GCOMPSUB', '-(ADSRAZ)(PIPAY)  (GYRO PULSES) X 2(+14)', line=169)

W('06,3417', 0o00006, '', 'EXTEND', line=171)
W('06,3420', 0o40331, '', 'DCS', 'DELVZ', '(PIPA PULSES) X 2(+14)', line=172)
W('06,3421', 0o52155, '', 'DXCH', 'MPAC', line=173)
W('06,3422', 0o31465, '', 'CA', 'ADIAZ', '(GYRO PULSES)/(PIPA PULSE) X 2(-6)     *', line=174)
W('06,3423', 0o03425, '', 'TC', 'GCOMPSUB', '-(ADIAZ)(PIPAZ)   (GYRO PULSES) X 2(+14)', line=175)

# EXTEND           # ***
# DCS     DELVX    # ***    (PIPA PULSE) X 2(+14)
# DXCH    MPAC     # ***
# CS      ADOAZ    # ***    (GYRO PULSES)/(PIPA PULSE) X 2(-6)     *
# TC      GCOMPSUB # ***    +(ADOAZ)(PIPAX)   (GYRO PULSES) X 2(+14)

W('06,3424', 0o00156, '', 'TC', 'MPAC +2', line=183)

# Page 331
W('06,3425', 0o56154, 'GCOMPSUB', 'XCH', 'MPAC', 'ADIA OR ADSRA COEFFICIENT ARRIVES IN A', line=186)
W('06,3426', 0o00006, '', 'EXTEND', '', 'C(MPAC) = (PIPA PULSES) X 2(+14)', line=187)
W('06,3427', 0o70154, '', 'MP', 'MPAC', '(GYRO PULSES)/(PIPA PULSE) X 2(-6)     *', line=188)
W('06,3430', 0o52123, '', 'DXCH', 'VBUF', 'NOW = (GYRO PULSES) X 2(+8)            *', line=189)

W('06,3431', 0o30155, '', 'CA', 'MPAC +1', 'MINOR PART OF PIPA PULSES', line=191)
W('06,3432', 0o00006, '', 'EXTEND', line=192)
W('06,3433', 0o70154, '', 'MP', 'MPAC', 'ADIA OR ADSRA', line=193)
W('06,3434', 0o54001, '', 'TS', 'L', line=194)
W('06,3435', 0o34755, '', 'CAF', 'ZERO', line=195)
W('06,3436', 0o20123, '', 'DAS', 'VBUF', 'NOW = (GYRO PULSES) X 2(+8)            *', line=196)

W('06,3437', 0o30122, '', 'CA', 'VBUF', 'PARTIAL RESULT - MAJOR', line=198)
W('06,3440', 0o00006, '', 'EXTEND', line=199)
W('06,3441', 0o74743, '', 'MP', 'BIT9', 'SCALE 2(+6)      SHIFT RIGHT           *', line=200)
W('06,3442', 0o50130, '', 'INDEX', 'BUF', 'RESULT = (GYRO PULSES) X 2(+14)', line=201)
W('06,3443', 0o21472, '', 'DAS', 'GCOMP', 'HI(ADIA)(PIPAI)  OR  HI(ADSRA)(PIPAI)', line=202)

W('06,3444', 0o30123, '', 'CA', 'VBUF +1', 'PARTIAL RESULT - MINOR', line=204)
W('06,3445', 0o00006, '', 'EXTEND', line=205)
W('06,3446', 0o74743, '', 'MP', 'BIT9', 'SCALE 2(+6)   SHIFT RIGHT 6            *', line=206)
W('06,3447', 0o54001, '', 'TS', 'L', line=207)
W('06,3450', 0o34755, '', 'CAF', 'ZERO', line=208)
W('06,3451', 0o50130, '', 'INDEX', 'BUF', 'RESULT = (GYRO PULSES) X 2(+14)', line=209)
W('06,3452', 0o21472, '', 'DAS', 'GCOMP', '(ADIA)(PIPAI) OR (ADSRA)(PIPAI)', line=210)

W('06,3453', 0o00002, '', 'TC', 'Q', line=212)

# Page 332
W('06,3454', 0o00006, 'DRIFTSUB', 'EXTEND', line=215)
W('06,3455', 0o22131, '', 'QXCH', 'BUF +1', line=216)

W('06,3456', 0o00006, '', 'EXTEND', '', 'C(A) = NBD    (GYRO PULSES)/(CS) X 2(-5)', line=218)
W('06,3457', 0o71075, '', 'MP', '1/PIPADT', '(CS) X 2(+8)   NOW (GYRO PULSES) X 2(+3)', line=219)
W('06,3460', 0o22155, '', 'LXCH', 'MPAC +1', 'SAVE FOR FRACTIONAL COMPENSATION', line=220)
W('06,3461', 0o00006, '', 'EXTEND', line=221)
W('06,3462', 0o74750, '', 'MP', 'BIT4', 'SCALE 2(+11)     SHIFT RIGHT 11', line=222)
W('06,3463', 0o50130, '', 'INDEX', 'BUF', line=223)
W('06,3464', 0o21472, '', 'DAS', 'GCOMP', 'HI(NBD)(DELTAT)   (GYRO PULSES) X 2(+14)', line=224)

W('06,3465', 0o30155, '', 'CA', 'MPAC +1', 'NOW MINOR PART', line=226)
W('06,3466', 0o00006, '', 'EXTEND', line=227)
W('06,3467', 0o74750, '', 'MP', 'BIT4', 'SCALE 2(+11)     SHIFT RIGHT 11', line=228)
W('06,3470', 0o54001, '', 'TS', 'L', line=229)
W('06,3471', 0o34755, '', 'CAF', 'ZERO', line=230)
W('06,3472', 0o50130, '', 'INDEX', 'BUF', 'ADD IN FRACTIONAL COMPENSATION', line=231)
W('06,3473', 0o21472, '', 'DAS', 'GCOMP', '(NBD)(DELTAT)     (GYRO PULSES) X 2(+14)', line=232)

W('06,3474', 0o34752, 'DRFTSUB2', 'CAF', 'TWO', 'PIPAX, PIPAY, PIPAZ', line=234)
W('06,3475', 0o60130, '', 'AD', 'BUF', line=235)
W('06,3476', 0o56130, '', 'XCH', 'BUF', line=236)
W('06,3477', 0o50000, '', 'INDEX', 'A', line=237)
W('06,3500', 0o11471, '', 'CCS', 'GCOMP', 'ARE GYRO COMMANDS 1 PULSE OR GREATER', line=238)
W('06,3501', 0o13503, '', 'TCF', '+2', 'YES', line=239)
W('06,3502', 0o00131, '', 'TC', 'BUF +1', 'NO', line=240)

W('06,3503', 0o73553, '', 'MASK', 'COMPCHK', 'DEC -1', line=242)
W('06,3504', 0o10000, '', 'CCS', 'A', 'ARE GYRO COMMANDS GREATER THAN 2 PULSES', line=243)
W('06,3505', 0o55477, '', 'TS', 'GCOMPSW', 'YES - SET GCOMPSW POSITIVE', line=244)
W('06,3506', 0o00131, '', 'TC', 'BUF +1', 'NO', line=245)

# Page 333
W('06,3507', 0o34751, '1/GYRO', 'CAF', 'FOUR', 'PIPAZ, PIPAY, PIPAX', line=248)
W('06,3510', 0o54130, '', 'TS', 'BUF', line=249)

W('06,3511', 0o50130, '', 'INDEX', 'BUF', 'SCALE GYRO COMMANDS FOR IMUPULSE', line=251)
W('06,3512', 0o31472, '', 'CA', 'GCOMP +1', 'FRACTIONAL PULSES', line=252)
W('06,3513', 0o00006, '', 'EXTEND', line=253)
W('06,3514', 0o74744, '', 'MP', 'BIT8', 'SHIFT RIGHT 7', line=254)
W('06,3515', 0o50130, '', 'INDEX', 'BUF', line=255)
W('06,3516', 0o55472, '', 'TS', 'GCOMP +1', 'FRACTIONAL PULSES SCALED', line=256)

W('06,3517', 0o34755, '', 'CAF', 'ZERO', 'SET GCOMP = 0 FOR DAS INSTRUCTION', line=258)
W('06,3520', 0o50130, '', 'INDEX', 'BUF', line=259)
W('06,3521', 0o57471, '', 'XCH', 'GCOMP', 'GYRO PULSES', line=260)
W('06,3522', 0o00006, '', 'EXTEND', line=261)
W('06,3523', 0o74744, '', 'MP', 'BIT8', 'SHIFT RIGHT 7', line=262)
W('06,3524', 0o50130, '', 'INDEX', 'BUF', line=263)
W('06,3525', 0o21472, '', 'DAS', 'GCOMP', 'ADD THESE TO FRACTIONAL PULSES ABOVE', line=264)

W('06,3526', 0o10130, '', 'CCS', 'BUF', 'PIPAZ, PIPAY, PIPAX', line=266)
W('06,3527', 0o67747, '', 'AD', 'NEG1', line=267)
W('06,3530', 0o13510, '', 'TCF', '1/GYRO +1', line=268)
W('06,3531', 0o01471, 'LGCOMP', 'ECADR', 'GCOMP', 'LESS THAN ZERO IMPOSSIBLE', kind='data', line=269)

W('06,3532', 0o33531, '', 'CAF', 'LGCOMP', line=271)
W('06,3533', 0o04616, '', 'TC', 'BANKCALL', line=272)
W('06,3534', 0o17323, '', 'CADR', 'IMUPULSE', 'CALL GYRO TORQUING ROUTINE', kind='data', line=273)
W('06,3535', 0o04616, '', 'TC', 'BANKCALL', line=274)
W('06,3536', 0o17716, '', 'CADR', 'IMUSTALL', 'WAIT FOR PULSES TO GET OUT', kind='data', line=275)
W('06,3537', 0o15155, '', 'TCF', 'ENDOFJOB', 'TEMPORARY', line=276)

W('06,3540', 0o34751, 'GCOMP1', 'CAF', 'FOUR', 'PIPAZ, PIPAY, PIPAX', line=278)
W('06,3541', 0o54130, '', 'TS', 'BUF', line=279)

W('06,3542', 0o50130, '', 'INDEX', 'BUF', 'RESCALE', line=281)
W('06,3543', 0o31472, '', 'CA', 'GCOMP +1', line=282)
W('06,3544', 0o00006, '', 'EXTEND', line=283)
W('06,3545', 0o74744, '', 'MP', 'BIT8', 'SHIFT MINOR PART LEFT 7 - MAJOR PART = 0', line=284)
W('06,3546', 0o50130, '', 'INDEX', 'BUF', line=285)
W('06,3547', 0o23472, '', 'LXCH', 'GCOMP +1', 'BITS 8-14 OF MINOR PART WERE = 0', line=286)

W('06,3550', 0o10130, '', 'CCS', 'BUF', 'PIPAZ, PIPAY, PIPAX', line=288)
W('06,3551', 0o67747, '', 'AD', 'NEG1', line=289)
W('06,3552', 0o13541, '', 'TCF', 'GCOMP1 +1', line=290)
W('06,3553', 0o77776, 'COMPCHK', 'DEC', '-1', 'LESS THAN ZERO IMPOSSIBLE', kind='data', line=291)
W('06,3554', 0o15155, '', 'TCF', 'ENDOFJOB', line=292)

# Page 334
W('06,3555', 0o11477, 'NBDONLY', 'CCS', 'GCOMPSW', 'BYPASS IF GCOMPSW NEGATIVE', line=295)
W('06,3556', 0o13561, '', 'TCF', '+3', line=296)
W('06,3557', 0o13561, '', 'TCF', '+2', line=297)
W('06,3560', 0o15155, '', 'TCF', 'ENDOFJOB', line=298)

W('06,3561', 0o00004, '', 'INHINT', line=300)
W('06,3562', 0o10076, '', 'CCS', 'FLAGWRD2', 'PREREAD T3RUPT MAY COINCIDE', line=301)
W('06,3563', 0o15155, '', 'TCF', 'ENDOFJOB', line=302)
W('06,3564', 0o15155, '', 'TCF', 'ENDOFJOB', line=303)
W('06,3565', 0o13566, '', 'TCF', '+1', line=304)

W('06,3566', 0o30104, '', 'CA', 'FLAGWRD8', 'IF SURFACE FLAG IS SET, SET TEM1', line=306)
W('06,3567', 0o74744, '', 'MASK', 'BIT8', 'POSITIVE SO THAT THE ACCELERATION TERMS', line=307)
W('06,3570', 0o54141, '', 'TS', 'TEM1', 'WILL BE COMPENSATED.', line=308)
W('06,3571', 0o00006, '', 'EXTEND', line=309)
W('06,3572', 0o13575, '', 'BZF', '+3', 'ARE WE ON THE SURFACE', line=310)

W('06,3573', 0o04674, '', 'TC', 'IBNKCALL', 'ON THE SURFACE', line=312)
W('06,3574', 0o77544, '', 'CADR', 'PIPASR +3', 'READ PIPAS, BUT DO NOT SCALE THEM', kind='data', line=313)

W('06,3575', 0o30025, '', 'CA', 'TIME1', '(CS) X 2(+14)', line=315)
W('06,3576', 0o57075, '', 'XCH', '1/PIPADT', 'PREVIOUS TIME', line=316)
W('06,3577', 0o00003, '', 'RELINT', line=317)
W('06,3600', 0o40000, '', 'COM', line=318)
W('06,3601', 0o61075, '', 'AD', '1/PIPADT', 'PRESENT TIME - PREVIOUS TIME', line=319)
W('06,3602', 0o64736, 'NBD2', 'AD', 'HALF', 'CORRECT FOR POSSIBLE TIME1 TICK', line=320)
W('06,3603', 0o64736, '', 'AD', 'HALF', line=321)
W('06,3604', 0o56001, '', 'XCH', 'L', 'IF TIME1 DID NOT TICK, REMOVE RESULTING', line=322)
W('06,3605', 0o56001, '', 'XCH', 'L', 'OVERFLOW.', line=323)

W('06,3606', 0o00006, 'NBD3', 'EXTEND', '', 'C(A) = DELTAT    (CS) X 2(+14)', line=325)
W('06,3607', 0o74742, '', 'MP', 'BIT10', 'SHIFT RIGHT 5', line=326)
W('06,3610', 0o52125, '', 'DXCH', 'VBUF +2', line=327)

W('06,3611', 0o34755, '', 'CA', 'ZERO', line=329)
W('06,3612', 0o55477, '', 'TS', 'GCOMPSW', 'INDICATE COMMANDS 2 PULSES OR LESS.', line=330)
W('06,3613', 0o54130, '', 'TS', 'BUF', 'INDEX  X, Y, Z.', line=331)

W('06,3614', 0o10141, '', 'CCS', 'TEM1', 'IF SURFACE FLAG IS SET,', line=333)
W('06,3615', 0o03356, '', 'TC', 'IRIGX', 'COMPENSATE ACCELERATION TERMS.', line=334)

W('06,3616', 0o00006, '', 'EXTEND', line=336)
W('06,3617', 0o30125, '', 'DCA', 'VBUF +2', line=337)
W('06,3620', 0o52155, '', 'DXCH', 'MPAC', 'DELTAT NOW SCALED (CS) X 2(+19)', line=338)

W('06,3621', 0o41460, '', 'CS', 'NBDX', '(GYRO PULSES)/(CS) X 2(-5)', line=340)
W('06,3622', 0o03644, '', 'TC', 'FBIASSUB', '-(NBDX)(DELTAT)   (GYRO PULSES) X 2(+14)', line=341)

W('06,3623', 0o10141, '', 'CCS', 'TEM1', 'IF SURFACE FLAG IS SET,', line=343)
W('06,3624', 0o03373, '', 'TC', 'IRIGY', 'COMPENSATE ACCELERATION TERMS.', line=344)
# Page 335
W('06,3625', 0o00006, '', 'EXTEND', line=346)
W('06,3626', 0o40125, '', 'DCS', 'VBUF +2', line=347)
W('06,3627', 0o52155, '', 'DXCH', 'MPAC', 'DELTAT SCALED (CS) X 2(+19)', line=348)
W('06,3630', 0o31461, '', 'CA', 'NBDY', '(GYRO PULSES)/(CS) X 2(-5)', line=349)
W('06,3631', 0o03644, '', 'TC', 'FBIASSUB', '-(NBDY)(DELTAT)   (GYRO PULSES) X 2(+14)', line=350)

W('06,3632', 0o10141, '', 'CCS', 'TEM1', 'IF SURFACE FLAG IS SET.', line=352)
W('06,3633', 0o03410, '', 'TC', 'IRIGZ', 'COMPENSATE ACCELERATION TERMS', line=353)

W('06,3634', 0o00006, '', 'EXTEND', line=355)
W('06,3635', 0o40125, '', 'DCS', 'VBUF +2', line=356)
W('06,3636', 0o52155, '', 'DXCH', 'MPAC', 'DELTAT SCALED (CS) X 2(+19)', line=357)
W('06,3637', 0o41462, '', 'CS', 'NBDZ', '(GYRO PULSES)/(CS) X 2(-5)', line=358)
W('06,3640', 0o03644, '', 'TC', 'FBIASSUB', '+(NBDZ)(DELTAT)   (GYRO PULSES) X 2(+14)', line=359)

W('06,3641', 0o11477, '', 'CCS', 'GCOMPSW', 'ARE GYRO COMMANDS GREATER THAN 2 PULSES', line=361)
W('06,3642', 0o13507, '', 'TCF', '1/GYRO', 'YES', line=362)
W('06,3643', 0o15155, '', 'TCF', 'ENDOFJOB', 'NO', line=363)

# Page 336
W('06,3644', 0o56002, 'FBIASSUB', 'XCH', 'Q', line=366)
W('06,3645', 0o54131, '', 'TS', 'BUF +1', line=367)

W('06,3646', 0o30002, '', 'CA', 'Q', 'NBD SCALED (GYRO PULSES)/(CS) X 2(-5)', line=369)
W('06,3647', 0o00006, '', 'EXTEND', line=370)
W('06,3650', 0o70154, '', 'MP', 'MPAC', 'DELTAT SCALED (CS) X 2(+19)', line=371)
W('06,3651', 0o50130, '', 'INDEX', 'BUF', line=372)
W('06,3652', 0o21472, '', 'DAS', 'GCOMP', 'HI(NBD)(DELTAT)   (GYRO PULSES) X 2(+14)', line=373)

W('06,3653', 0o30002, '', 'CA', 'Q', 'NOW FRACTIONAL PART', line=375)
W('06,3654', 0o00006, '', 'EXTEND', line=376)
W('06,3655', 0o70155, '', 'MP', 'MPAC +1', line=377)
W('06,3656', 0o54001, '', 'TS', 'L', line=378)
W('06,3657', 0o34755, '', 'CAF', 'ZERO', line=379)
W('06,3660', 0o50130, '', 'INDEX', 'BUF', line=380)
W('06,3661', 0o21472, '', 'DAS', 'GCOMP', '(NBD)(DELTAT)     (GYRO PULSES) X 2(+14)', line=381)

W('06,3662', 0o13474, '', 'TCF', 'DRFTSUB2', 'CHECK MAGNITUDE OF COMPENSATION', line=383)

W('06,3663', 0o04616, 'LASTBIAS', 'TC', 'BANKCALL', line=385)
W('06,3664', 0o17277, '', 'CADR', 'PIPUSE1', kind='data', line=386)

W('06,3665', 0o11477, '', 'CCS', 'GCOMPSW', line=388)
W('06,3666', 0o13671, '', 'TCF', '+3', line=389)
W('06,3667', 0o13671, '', 'TCF', '+2', line=390)
W('06,3670', 0o15155, '', 'TCF', 'ENDOFJOB', line=391)

W('06,3671', 0o30104, '', 'CA', 'FLAGWRD8', 'IF SURFACE FLAG IS SET, SET TEM1', line=393)
W('06,3672', 0o74744, '', 'MASK', 'SURFFBIT', 'POSITIVE SO THAT THE ACCELERATION TERMS', line=394)
W('06,3673', 0o54141, '', 'TS', 'TEM1', 'WILL BE COMPENSATED.', line=395)

W('06,3674', 0o37716, '', 'CAF', 'PRIO31', '2 SECONDS SCALED (CS) X 2(+8)', line=397)
W('06,3675', 0o57075, '', 'XCH', '1/PIPADT', line=398)
W('06,3676', 0o40000, '', 'COM', line=399)
W('06,3677', 0o61235, '', 'AD', 'PIPTIME +1', line=400)
W('06,3700', 0o13602, '', 'TCF', 'NBD2', line=401)

W('06,3701', 0o33531, 'GCOMPZER', 'CAF', 'LGCOMP', 'ROUTINE TO ZERO GCOMP BEFORE FIRST', line=403)
W('06,3702', 0o56003, '', 'XCH', 'EBANK', 'CALL TO 1/PIPA', line=404)
W('06,3703', 0o54163, '', 'TS', 'MODE', line=405)

W('06,3704', 0o34755, '', 'CAF', 'ZERO', line=407)
W('06,3705', 0o55477, '', 'TS', 'GCOMPSW', line=408)
W('06,3706', 0o55471, '', 'TS', 'GCOMP', line=409)
W('06,3707', 0o55472, '', 'TS', 'GCOMP +1', line=410)
W('06,3710', 0o55473, '', 'TS', 'GCOMP +2', line=411)
W('06,3711', 0o55474, '', 'TS', 'GCOMP +3', line=412)
W('06,3712', 0o55475, '', 'TS', 'GCOMP +4', line=413)
# Page 337
W('06,3713', 0o55476, '', 'TS', 'GCOMP +5', line=415)

W('06,3714', 0o13353, '', 'TCF', 'IRIG1', 'RESTORE EBANK AND RETURN', line=417)
