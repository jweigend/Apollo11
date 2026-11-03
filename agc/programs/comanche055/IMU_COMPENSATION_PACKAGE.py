"""IMU_COMPENSATION_PACKAGE.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/IMU_COMPENSATION_PACKAGE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 297-306 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('IMU_COMPENSATION_PACKAGE', 'IMU_COMPENSATION_PACKAGE.agc', 'Comanche055', pages='297-306')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     IMU_COMPENSATION_PACKAGE.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        297-306
# Mod history:  2009-05-08 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images/
# 2009-05-21 RSB  In IRIGZ, PRIO17 corrected to PRIO21.
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

# Page 297
#   BANK 7
#   SETLOC IMUCOMP
#   BANK
#   EBANK= NBDX

#   COUNT 06/ICOMP

W('06,3262', 0o33516, '1/PIPA', 'CAF', 'LGCOMP', 'SAVE EBANK OF CALLING PROGRAM', line=39)
W('06,3263', 0o56003, '', 'XCH', 'EBANK', line=40)
W('06,3264', 0o54163, '', 'TS', 'MODE', line=41)

W('06,3265', 0o11477, '', 'CCS', 'GCOMPSW', 'BYPASS IF GCOMPSW NEGATIVE', line=43)
W('06,3266', 0o13271, '', 'TCF', '+3', line=44)
W('06,3267', 0o13271, '', 'TCF', '+2', line=45)
W('06,3270', 0o13407, '', 'TCF', 'IRIG1', 'RETURN', line=46)

W('06,3271', 0o00004, '', 'INHINT', '', " ASSURE COMPLETE COMPENSATION OF DELV'S", line=48)
# FOR DOWNLINK.
W('06,3272', 0o35015, '1/PIPA1', 'CAF', 'FOUR', 'PIPAZ, PIPAY, PIPAX', line=50)
W('06,3273', 0o54132, '', 'TS', 'BUF +2', line=51)

W('06,3274', 0o50132, '', 'INDEX', 'BUF +2', line=53)
W('06,3275', 0o31453, '', 'CA', 'PIPASCF', '(P.P.M.) X 2(-9)', line=54)
W('06,3276', 0o00006, '', 'EXTEND', line=55)
W('06,3277', 0o50132, '', 'INDEX', 'BUF +2', line=56)
W('06,3300', 0o71162, '', 'MP', 'DELVX', '(PP) X 2(+14) NOW (PIPA PULSES) X 2(+5)', line=57)
W('06,3301', 0o54002, '', 'TS', 'Q', 'SAVE MAJOR PART', line=58)

W('06,3302', 0o30001, '', 'CA', 'L', 'MINOR PART', line=60)
W('06,3303', 0o00006, '', 'EXTEND', line=61)
W('06,3304', 0o75012, '', 'MP', 'BIT6', 'SCALE 2(+9)   SHIFT RIGHT 9', line=62)
W('06,3305', 0o50132, '', 'INDEX', 'BUF +2', line=63)
W('06,3306', 0o55163, '', 'TS', 'DELVX +1', 'FRACTIONAL PIPA PULSES SCALED 2(+14)', line=64)

W('06,3307', 0o30002, '', 'CA', 'Q', 'MAJOR PART', line=66)
W('06,3310', 0o00006, '', 'EXTEND', line=67)
W('06,3311', 0o75012, '', 'MP', 'BIT6', 'SCALE 2(+9)   SHIFT RIGHT 9', line=68)
W('06,3312', 0o50132, '', 'INDEX', 'BUF +2', line=69)
W('06,3313', 0o21163, '', 'DAS', 'DELVX', '(PIPAI) + (PIPAI)(SFE)', line=70)

W('06,3314', 0o50132, '', 'INDEX', 'BUF +2', line=72)
W('06,3315', 0o41452, '', 'CS', 'PIPABIAS', '(PIPA PULSES)/(CS) X 2(-8)                    *', line=73)
W('06,3316', 0o00006, '', 'EXTEND', line=74)
W('06,3317', 0o71074, '', 'MP', '1/PIPADT', '(CS) X 2(+8) NOW (PIPA PULSES) X 2(+0)        *', line=75)
W('06,3320', 0o00006, '', 'EXTEND', line=76)
W('06,3321', 0o75017, '', 'MP', 'BIT1', 'SCALE 2(+14) SHIFT RIGHT 14                   *', line=77)
W('06,3322', 0o50132, '', 'INDEX', 'BUF +2', line=78)
W('06,3323', 0o21163, '', 'DAS', 'DELVX', '(PIPAI) + (PIPAI)(SFE) - (BIAS)(DELTAT)', line=79)

W('06,3324', 0o10132, '', 'CCS', 'BUF +2', 'PIPAZ, PIPAY, PIPAX', line=81)
# Page 298
W('06,3325', 0o67716, '', 'AD', 'NEG1', line=83)
W('06,3326', 0o13273, '', 'TCF', '1/PIPA1 +1', line=84)
W('06,3327', 0o13330, '', 'NOOP', '', 'LESS THAN ZERO IMPOSSIBLE.', line=85)
W('06,3330', 0o00003, '', 'RELINT', line=86)
# Page 299

W('06,3331', 0o55477, 'IRIGCOMP', 'TS', 'GCOMPSW', 'INDICATE COMMANDS 2 PULSES OR LESS.', line=89)
W('06,3332', 0o54130, '', 'TS', 'BUF', 'INDEX COUNTER - IRIGX, IRIGY, IRIGZ.', line=90)

W('06,3333', 0o00006, 'IRIGX', 'EXTEND', line=92)
W('06,3334', 0o41163, '', 'DCS', 'DELVX', '(PIPA PULSES) X 2(+14)', line=93)
W('06,3335', 0o52155, '', 'DXCH', 'MPAC', line=94)
W('06,3336', 0o31463, '', 'CA', 'ADIAX', '(GYRO PULSES)/(PIPA PULSE) X 2(-3)            *', line=95)
W('06,3337', 0o03412, '', 'TC', 'GCOMPSUB', '-(ADIAX)(PIPAX)       (GYRO PULSES) X 2(+14)', line=96)

W('06,3340', 0o00006, '', 'EXTEND', line=98)
W('06,3341', 0o41165, '', 'DCS', 'DELVY', '(PIPA PULSES) X 2(+14)', line=99)
W('06,3342', 0o52155, '', 'DXCH', 'MPAC', line=100)
W('06,3343', 0o41466, '', 'CS', 'ADSRAX', '(GYRO PULSES)/(PIPA PULSE) X 2(-3)    *', line=101)
W('06,3344', 0o03412, '', 'TC', 'GCOMPSUB', '+(ADSRAX)(PIPAY)      (GYRO PULSES) X 2(+14)', line=102)

# EXTEND                  # ***
# DCS     DELVY           # ***   (PIPA PULSES) X 2(+14)
# DXCH    MPAC            # ***
# CA      ADOAX           # ***   (GYRO PULSES)/(PIPA PULSE) X 2(-3)      *
# TC      GCOMPSUB        # ***   -(ADOAX)(PIPAZ)         (GYRO PULSES) X 2(+14)

W('06,3345', 0o41460, '', 'CS', 'NBDX', '(GYRO PULSES)/(CS) X 2(-5)', line=110)
W('06,3346', 0o03441, '', 'TC', 'DRIFTSUB', '-(NBDX)(DELTAT)       (GYRO PULSES) X 2(+14)', line=111)

W('06,3347', 0o00006, 'IRIGY', 'EXTEND', line=113)
W('06,3350', 0o41165, '', 'DCS', 'DELVY', '(PIPA PULSES) X 2(+14)', line=114)
W('06,3351', 0o52155, '', 'DXCH', 'MPAC', line=115)
W('06,3352', 0o31464, '', 'CA', 'ADIAY', '(GYRO PULSES)/(PIPA PULSE) X 2(-3)            *', line=116)
W('06,3353', 0o03412, '', 'TC', 'GCOMPSUB', '-(ADIAY)(PIPAY)       (GYRO PULSES) X 2(+14)', line=117)

W('06,3354', 0o00006, '', 'EXTEND', line=119)
W('06,3355', 0o41167, '', 'DCS', 'DELVZ', '(PIPA PULSES) X 2(+14)', line=120)
W('06,3356', 0o52155, '', 'DXCH', 'MPAC', line=121)
W('06,3357', 0o41467, '', 'CS', 'ADSRAY', '(GYRO PULSES)/(PIPA PULSE) X 2(-3)            *', line=122)
W('06,3360', 0o03412, '', 'TC', 'GCOMPSUB', '+(ADSRAY)(PIPAZ)      (GYRO PULSES) X 2(+14)', line=123)

# EXTEND                  # ***
# DCS     DELVX           # ***   (PIPA PULSES) X 2(+14)
# DXCH    MPAC            # ***
# CA      ADOAY           # ***   (GYRO PULSES)/(PIPA PULSE) X 2(-3)      *
# TC      GCOMPSUB        # ***   -(ADOAY)(PIPAZ) (GYRO PULSES) X 2(+14)

W('06,3361', 0o41461, '', 'CS', 'NBDY', '(GYRO PULSES)/(CS) X 2(-5)', line=131)
W('06,3362', 0o03441, '', 'TC', 'DRIFTSUB', '-(NBDY)(DELTAT)       (GYRO PULSES) X 2(+14)', line=132)

W('06,3363', 0o00006, 'IRIGZ', 'EXTEND', line=134)
W('06,3364', 0o41165, '', 'DCS', 'DELVY', '(PIPA PULSES) X 2(+14)', line=135)
W('06,3365', 0o52155, '', 'DXCH', 'MPAC', line=136)
W('06,3366', 0o31470, '', 'CA', 'ADSRAZ', '(GYRO PULSES)/(PIPA PULSE) X 2(-3)            *', line=137)
# Page 300
W('06,3367', 0o03412, '', 'TC', 'GCOMPSUB', '-(ADSRAZ)(PIPAY)      (GYRO PULSES) X 2(+14)', line=139)

W('06,3370', 0o00006, '', 'EXTEND', line=141)
W('06,3371', 0o41167, '', 'DCS', 'DELVZ', '(PIPA PULSES) X 2(+14)', line=142)
W('06,3372', 0o52155, '', 'DXCH', 'MPAC', line=143)
W('06,3373', 0o31465, '', 'CA', 'ADIAZ', '(GYRO PULSES)/(PIPA PULSE) X 2(-3)            *', line=144)
W('06,3374', 0o03412, '', 'TC', 'GCOMPSUB', '-(ADIAZ)(PIPAZ)       (GYRO PULSES) X 2(+14)', line=145)

# EXTEND                  # ***
# DCS     DELVX           # ***   (PIPA PULSE) X 2(+14)
# DXCH    MPAC            # ***
# CS      ADOAZ           # ***   (GYRO PULSES)/(PIPA PULSE) X 2(-3)      *
# TC      GCOMPSUB        # ***   +(ADOAZ)(PIPAX) (GYRO PULSES) X 2(+14)

W('06,3375', 0o31462, '', 'CA', 'NBDZ', '(GYRO PULSES)/(CS) X 2(-5)', line=153)
W('06,3376', 0o03441, '', 'TC', 'DRIFTSUB', '+(NBDZ)(DELTAT)       (GYRO PULSES) X 2(+14)', line=154)

# Page 301
W('06,3377', 0o11477, '', 'CCS', 'GCOMPSW', 'ARE GYRO COMMANDS GREATER THAN 2 PULSES', line=157)
W('06,3400', 0o13402, '', 'TCF', '+2', 'YES', line=158)
W('06,3401', 0o13407, '', 'TCF', 'IRIG1', 'NO', line=159)

W('06,3402', 0o35073, '', 'CAF', 'PRIO21', 'HIGHER THAN SERVICER-LESS THAN PRELAUNCH', line=161)
W('06,3403', 0o05134, '', 'TC', 'NOVAC', line=162)
#   EBANK= NBDX
W('06,3404', 0o03474, '', '2CADR', '1/GYRO', kind='data', line=164)
W('06,3405', 0o14063, kind='data', line=164)

W('06,3406', 0o00003, '', 'RELINT', line=166)
W('06,3407', 0o30163, 'IRIG1', 'CA', 'MODE', 'SET EBANK FOR RETURN', line=167)
W('06,3410', 0o54003, '', 'TS', 'EBANK', line=168)
W('06,3411', 0o14675, '', 'TCF', 'SWRETURN', line=169)

W('06,3412', 0o56154, 'GCOMPSUB', 'XCH', 'MPAC', 'ADIA OR ADSRA COEFFICIENT ARRIVES IN A', line=171)
W('06,3413', 0o00006, '', 'EXTEND', '', 'C(MPAC) = (PIPA PULSES) X 2(+14)', line=172)
W('06,3414', 0o70154, '', 'MP', 'MPAC', '(GYRO PULSES)/(PIPA PULSE) X 2(-3)            *', line=173)
W('06,3415', 0o52123, '', 'DXCH', 'VBUF', 'NOW = (GYRO PULSES) X 2(+11)                  *', line=174)

W('06,3416', 0o30155, '', 'CA', 'MPAC +1', 'MINOR PART OF PIPA PULSES', line=176)
W('06,3417', 0o00006, '', 'EXTEND', line=177)
W('06,3420', 0o70154, '', 'MP', 'MPAC', 'ADIA OR ADSRA', line=178)
W('06,3421', 0o54001, '', 'TS', 'L', line=179)
W('06,3422', 0o35021, '', 'CAF', 'ZERO', line=180)
W('06,3423', 0o20123, '', 'DAS', 'VBUF', 'NOW = (GYRO PULSES) X 2(+11)                  *', line=181)

W('06,3424', 0o30122, '', 'CA', 'VBUF', 'PARTIAL RESULT - MAJOR', line=183)
W('06,3425', 0o00006, '', 'EXTEND', line=184)
W('06,3426', 0o75004, '', 'MP', 'BIT12', 'SCALE 2(+3)   SHIFT RIGHT 3                   *', line=185)
W('06,3427', 0o50130, '', 'INDEX', 'BUF', 'RESULT = (GYRO PULSES) X 2(+14)', line=186)
W('06,3430', 0o21472, '', 'DAS', 'GCOMP', 'HI(ADIA)(PIPAI) OR HI(ADSRA)(PIPAI)', line=187)

W('06,3431', 0o30123, '', 'CA', 'VBUF +1', 'PARTIAL RESULT - MINOR', line=189)
W('06,3432', 0o00006, '', 'EXTEND', line=190)
W('06,3433', 0o75004, '', 'MP', 'BIT12', 'SCALE 2(+3)   SHIFT RIGHT 3                   *', line=191)
W('06,3434', 0o54001, '', 'TS', 'L', line=192)
W('06,3435', 0o35021, '', 'CAF', 'ZERO', line=193)
W('06,3436', 0o50130, '', 'INDEX', 'BUF', 'RESULT = (GYRO PULSES) X 2(+14)', line=194)
W('06,3437', 0o21472, '', 'DAS', 'GCOMP', '(ADIA)(PIPAI)  OR  (ADSRA)(PIPAI)', line=195)

W('06,3440', 0o00002, '', 'TC', 'Q', line=197)

# Page 302
W('06,3441', 0o00006, 'DRIFTSUB', 'EXTEND', line=200)
W('06,3442', 0o22131, '', 'QXCH', 'BUF +1', line=201)

W('06,3443', 0o00006, '', 'EXTEND', '', 'C(A) = NBD    (GYRO PULSES)/(CS) X 2(-5)', line=203)
W('06,3444', 0o71074, '', 'MP', '1/PIPADT', '(CS) X 2(+8)  NO (GYRO PULSES) X 2(+3)', line=204)
W('06,3445', 0o22155, '', 'LXCH', 'MPAC +1', 'SAVE FOR FRACTIONAL COMPENSATION', line=205)
W('06,3446', 0o00006, '', 'EXTEND', line=206)
W('06,3447', 0o75014, '', 'MP', 'BIT4', 'SCALE 2(+11)  SHIFT RIGHT 11', line=207)
W('06,3450', 0o50130, '', 'INDEX', 'BUF', line=208)
W('06,3451', 0o21472, '', 'DAS', 'GCOMP', 'HI(NBD)(DELTAT)       (GYRO PULSES) X 2(+14)', line=209)

W('06,3452', 0o30155, '', 'CA', 'MPAC +1', 'NOW MINOR PART', line=211)
W('06,3453', 0o00006, '', 'EXTEND', line=212)
W('06,3454', 0o75014, '', 'MP', 'BIT4', 'SCALE 2(+11)          SHIFT RIGHT 11', line=213)
W('06,3455', 0o54001, '', 'TS', 'L', line=214)
W('06,3456', 0o35021, '', 'CAF', 'ZERO', line=215)
W('06,3457', 0o50130, '', 'INDEX', 'BUF', 'ADD IN FRACTIONAL COMPENSATION', line=216)
W('06,3460', 0o21472, '', 'DAS', 'GCOMP', '(NBD)(DELTAT)         (GYRO PULSES) X 2(+14)', line=217)

W('06,3461', 0o35016, 'DRFTSUB2', 'CAF', 'TWO', 'PIPAX, PIPAY, PIPAZ', line=219)
W('06,3462', 0o60130, '', 'AD', 'BUF', line=220)
W('06,3463', 0o56130, '', 'XCH', 'BUF', line=221)
W('06,3464', 0o50000, '', 'INDEX', 'A', line=222)
W('06,3465', 0o11471, '', 'CCS', 'GCOMP', 'ARE GYRO COMMANDS 1 PULSE OR GREATER', line=223)
W('06,3466', 0o13470, '', 'TCF', '+2', 'YES', line=224)
W('06,3467', 0o00131, '', 'TC', 'BUF +1', 'NO', line=225)

W('06,3470', 0o77716, '', 'MASK', 'NEGONE', line=227)
W('06,3471', 0o10000, '', 'CCS', 'A', 'ARE GYRO COMMANDS GREATER THAN 2 PULSES', line=228)
W('06,3472', 0o55477, '', 'TS', 'GCOMPSW', 'YES - SET GCOMPSW POSITIVE', line=229)
W('06,3473', 0o00131, '', 'TC', 'BUF +1', 'NO', line=230)

# Page 303
W('06,3474', 0o35015, '1/GYRO', 'CAF', 'FOUR', 'PIPAZ, PIPAY, PIPAX', line=233)
W('06,3475', 0o54130, '', 'TS', 'BUF', line=234)

W('06,3476', 0o50130, '', 'INDEX', 'BUF', 'SCALE GYRO COMMANDS FOR IMUPULSE', line=236)
W('06,3477', 0o31472, '', 'CA', 'GCOMP +1', 'FRACTIONAL PULSES', line=237)
W('06,3500', 0o00006, '', 'EXTEND', line=238)
W('06,3501', 0o75010, '', 'MP', 'BIT8', 'SHIFT RIGHT 7', line=239)
W('06,3502', 0o50130, '', 'INDEX', 'BUF', line=240)
W('06,3503', 0o55472, '', 'TS', 'GCOMP +1', 'FRACTIONAL PULSES SCALED', line=241)

W('06,3504', 0o35021, '', 'CAF', 'ZERO', 'SET GCOMP = 0 FOR DAS INSTRUCTION', line=243)
W('06,3505', 0o50130, '', 'INDEX', 'BUF', line=244)
W('06,3506', 0o57471, '', 'XCH', 'GCOMP', 'GYRO PULSES', line=245)
W('06,3507', 0o00006, '', 'EXTEND', line=246)
W('06,3510', 0o75010, '', 'MP', 'BIT8', 'SHIFT RIGHT 7', line=247)
W('06,3511', 0o50130, '', 'INDEX', 'BUF', line=248)
W('06,3512', 0o21472, '', 'DAS', 'GCOMP', 'ADD THESE TO FRACTIONAL PULSES ABOVE', line=249)

W('06,3513', 0o10130, '', 'CCS', 'BUF', 'PIPAZ, PIPAY, PIPAX', line=251)
W('06,3514', 0o67716, '', 'AD', 'NEG1', line=252)
W('06,3515', 0o13475, '', 'TCF', '1/GYRO +1', line=253)
W('06,3516', 0o01471, 'LGCOMP', 'ECADR', 'GCOMP', 'LESS THAN ZERO IMPOSSIBLE', kind='data', line=254)

W('06,3517', 0o33516, '', 'CAF', 'LGCOMP', line=256)
W('06,3520', 0o04662, '', 'TC', 'BANKCALL', line=257)
W('06,3521', 0o17206, '', 'CADR', 'IMUPULSE', 'CALL GYRO TORQUING ROUTINE', kind='data', line=258)
W('06,3522', 0o04662, '', 'TC', 'BANKCALL', line=259)
W('06,3523', 0o17577, '', 'CADR', 'IMUSTALL', 'WAIT FOR PULSES TO GET OUT', kind='data', line=260)
W('06,3524', 0o15217, '', 'TCF', 'ENDOFJOB', 'TEMPORARY', line=261)

W('06,3525', 0o35015, 'GCOMP1', 'CAF', 'FOUR', 'PIPAZ, PIPAY, PIPAX', line=263)
W('06,3526', 0o54130, '', 'TS', 'BUF', line=264)

W('06,3527', 0o50130, '', 'INDEX', 'BUF', 'RESCALE', line=266)
W('06,3530', 0o31472, '', 'CA', 'GCOMP +1', line=267)
W('06,3531', 0o00006, '', 'EXTEND', line=268)
W('06,3532', 0o75010, '', 'MP', 'BIT8', 'SHIFT MINOR PART LEFT 7 - MAJOR PART = 0', line=269)
W('06,3533', 0o50130, '', 'INDEX', 'BUF', line=270)
W('06,3534', 0o23472, '', 'LXCH', 'GCOMP +1', 'BITS 8-14 OF MINOR PART WERE = 0', line=271)

W('06,3535', 0o10130, '', 'CCS', 'BUF', 'PIPAZ, PIPAY, PIPAX', line=273)
W('06,3536', 0o67716, '', 'AD', 'NEG1', line=274)
W('06,3537', 0o13526, '', 'TCF', 'GCOMP1 +1', line=275)
W('06,3540', 0o01436, 'V06N30S', 'VN', '0630', kind='data', line=276)
W('06,3541', 0o15217, '', 'TCF', 'ENDOFJOB', line=277)

# Page 304
W('06,3542', 0o11477, 'NBDONLY', 'CCS', 'GCOMPSW', 'BYPASS IF GCOMPSW NEGATIVE', line=280)
W('06,3543', 0o13546, '', 'TCF', '+3', line=281)
W('06,3544', 0o13546, '', 'TCF', '+2', line=282)
W('06,3545', 0o15217, '', 'TCF', 'ENDOFJOB', line=283)

W('06,3546', 0o00004, '', 'INHINT', line=285)
W('06,3547', 0o10076, '', 'CCS', 'FLAGWRD2', 'PREREAD T3RUPT MAY COINCIDE', line=286)
W('06,3550', 0o15217, '', 'TCF', 'ENDOFJOB', line=287)
W('06,3551', 0o15217, '', 'TCF', 'ENDOFJOB', line=288)
W('06,3552', 0o13553, '', 'TCF', '+1', line=289)

W('06,3553', 0o30025, '', 'CA', 'TIME1', '(CS) X 2(+14)', line=291)
W('06,3554', 0o57074, '', 'XCH', '1/PIPADT', 'PREVIOUS TIME', line=292)
W('06,3555', 0o00003, '', 'RELINT', line=293)
W('06,3556', 0o40000, '', 'COM', line=294)
W('06,3557', 0o61074, '', 'AD', '1/PIPADT', line=295)
W('06,3560', 0o10000, 'NBD2', 'CCS', 'A', 'CALCULATE ELAPSED TIME', line=296)
W('06,3561', 0o65017, '', 'AD', 'ONE', 'NO TIME1 OVERFLOW', line=297)
W('06,3562', 0o13567, '', 'TCF', 'NBD3', 'RESTORE TIME DIFFERENCE AND JUMP', line=298)
W('06,3563', 0o13565, '', 'TCF', '+2', 'TIME1 OVERFLOW', line=299)
W('06,3564', 0o15217, '', 'TCF', 'ENDOFJOB', 'IF ELAPSED TIME = 0 (DIFFERENCE = -0)', line=300)

W('06,3565', 0o40000, '', 'COM', '', 'CALCULATE ABSOLUTE DIFFERENCE', line=302)
W('06,3566', 0o64777, '', 'AD', 'POSMAX', line=303)

W('06,3567', 0o00006, 'NBD3', 'EXTEND', '', 'C(A) = DELTAT         (CS) X 2(+14)', line=305)
W('06,3570', 0o75006, '', 'MP', 'BIT10', 'SHIFT RIGHT 5', line=306)
W('06,3571', 0o52123, '', 'DXCH', 'VBUF', line=307)
W('06,3572', 0o00006, '', 'EXTEND', line=308)
W('06,3573', 0o30123, '', 'DCA', 'VBUF', line=309)
W('06,3574', 0o52155, '', 'DXCH', 'MPAC', 'DELTAT NOW SCALED (CS) X 2(+19)', line=310)

W('06,3575', 0o35021, '', 'CAF', 'ZERO', line=312)
W('06,3576', 0o55477, '', 'TS', 'GCOMPSW', 'INDICATE COMMANDS 2 PULSES OR LESS', line=313)
W('06,3577', 0o54130, '', 'TS', 'BUF', 'PIPAX, PIPAY, PIPAZ', line=314)

W('06,3600', 0o41460, '', 'CS', 'NBDX', '(GYRO PULSES)/(CS) X 2(-5)', line=316)
W('06,3601', 0o03617, '', 'TC', 'FBIASSUB', '-(NBOX)(DELTAT)       (GYRO PULSES) X 2(+14)', line=317)

W('06,3602', 0o00006, '', 'EXTEND', line=319)
W('06,3603', 0o40123, '', 'DCS', 'VBUF', line=320)
W('06,3604', 0o52155, '', 'DXCH', 'MPAC', 'DELTAT SCALED (CS) X 2(+19)', line=321)
W('06,3605', 0o31461, '', 'CA', 'NBDY', '(GYRO PULSES)/(CS) X 2(-5)', line=322)
W('06,3606', 0o03617, '', 'TC', 'FBIASSUB', '-(NBDY)(DELTAT)       (GYRO PULSES) X 2(+14)', line=323)

W('06,3607', 0o00006, '', 'EXTEND', line=325)
W('06,3610', 0o40123, '', 'DCS', 'VBUF', line=326)
W('06,3611', 0o52155, '', 'DXCH', 'MPAC', 'DELTAT SCALED (CS) X 2(+19)', line=327)
W('06,3612', 0o41462, '', 'CS', 'NBDZ', '(GYRO PULSES)/(CS) X 2(-5)', line=328)
W('06,3613', 0o03617, '', 'TC', 'FBIASSUB', '+(NBDZ)(DELTAT)       (GYRO PULSES) X 2(+14)', line=329)
# Page 305
W('06,3614', 0o11477, '', 'CCS', 'GCOMPSW', 'ARE GYRO COMMANDS GREATER THAN 2 PULSES', line=331)
W('06,3615', 0o13474, '', 'TCF', '1/GYRO', 'YES', line=332)
W('06,3616', 0o15217, '', 'TCF', 'ENDOFJOB', 'NO', line=333)

# Page 306
W('06,3617', 0o56002, 'FBIASSUB', 'XCH', 'Q', line=336)
W('06,3620', 0o54131, '', 'TS', 'BUF +1', line=337)

W('06,3621', 0o30002, '', 'CA', 'Q', 'NBD SCALED (GYRO PULSES)/(CS) X 2(-5)', line=339)
W('06,3622', 0o00006, '', 'EXTEND', line=340)
W('06,3623', 0o70154, '', 'MP', 'MPAC', 'DELTAT SCALED (CS) X 2(+19)', line=341)
W('06,3624', 0o50130, '', 'INDEX', 'BUF', line=342)
W('06,3625', 0o21472, '', 'DAS', 'GCOMP', 'HI(NBD)(DELTAT)       (GYRO PULSES) X 2(+14)', line=343)

W('06,3626', 0o30002, '', 'CA', 'Q', 'NO FRACTIONAL PART', line=345)
W('06,3627', 0o00006, '', 'EXTEND', line=346)
W('06,3630', 0o70155, '', 'MP', 'MPAC +1', line=347)
W('06,3631', 0o54001, '', 'TS', 'L', line=348)
W('06,3632', 0o35021, '', 'CAF', 'ZERO', line=349)
W('06,3633', 0o50130, '', 'INDEX', 'BUF', line=350)
W('06,3634', 0o21472, '', 'DAS', 'GCOMP', '(NBD)(DELTAT)         (GYRO PULSES) X 2(+14)', line=351)

W('06,3635', 0o13461, '', 'TCF', 'DRFTSUB2', 'CHECK MAGNITUDE OF COMPENSATION', line=353)

W('06,3636', 0o04662, 'LASTBIAS', 'TC', 'BANKCALL', line=355)
W('06,3637', 0o17156, '', 'CADR', 'PIPUSE', kind='data', line=356)

W('06,3640', 0o11477, '', 'CCS', 'GCOMPSW', 'BYPASS IF GCOMPSW NEGATIVE', line=358)
W('06,3641', 0o13644, '', 'TCF', '+3', line=359)
W('06,3642', 0o13644, '', 'TCF', '+2', line=360)
W('06,3643', 0o15217, '', 'TCF', 'ENDOFJOB', line=361)

W('06,3644', 0o37665, '', 'CAF', 'PRIO31', '2 SECONDS SCALED (CS) X 2(+8)', line=363)
W('06,3645', 0o57074, '', 'XCH', '1/PIPADT', line=364)
W('06,3646', 0o40000, '', 'COM', line=365)
W('06,3647', 0o61246, '', 'AD', 'PIPTIME1 +1', 'TIME AT PIPA1 =0', line=366)
W('06,3650', 0o13560, '', 'TCF', 'NBD2', line=367)
