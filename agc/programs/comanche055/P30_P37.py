"""P30-P37.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P30-P37.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 635-648 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P30_P37', 'P30-P37.agc', 'Comanche055', pages='635-648')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P30-P37.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        635-648
# Mod history:  2009-05-10 RSB  Adapted from the Colossus249/ file
# of the same name, using Comanche055 page
# images.
# 2009-05-20 RSB  Corrected BDV -> BOV.
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

# Page 635
#   BANK 32

#   SETLOC P30S1
#   BANK

#   EBANK= +MGA

#   COUNT 35/P34

W('35,3264', 0o77420, 'DISPMGA', 'STQ', 'EXIT', 'USED IN P30', kind='interp', line=42)

W('35,3265', 0o02370, '', '', 'RGEXIT', kind='operand', line=44)
W('35,3266', 0o03304, '', 'TC', 'COMPTGO', line=45)

W('35,3267', 0o34621, 'DISP45', 'CAF', 'V16N45', line=47)
W('35,3270', 0o04662, '', 'TC', 'BANKCALL', line=48)
W('35,3271', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=49)
W('35,3272', 0o04106, '', 'TC', 'GOTOPOOH', line=50)
W('35,3273', 0o03300, '', 'TC', 'END45', line=51)
W('35,3274', 0o03267, '', 'TC', 'DISP45', line=52)
W('35,3275', 0o05412, 'P30PHSI', 'TC', 'PHASCHNG', line=53)
W('35,3276', 0o00014, '', 'OCT', '14', kind='data', line=54)
W('35,3277', 0o05217, '', 'TCR', 'ENDOFJOB', line=55)
W('35,3300', 0o06006, 'END45', 'TC', 'INTPRET', line=56)
W('35,3301', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=57)
W('35,3302', 0o03664, '', '', 'TIMRFLAG', kind='operand', line=58)
W('35,3303', 0o02370, '', '', 'RGEXIT', kind='operand', line=59)

W('35,3304', 0o00006, 'COMPTGO', 'EXTEND', '', 'USED TO COMPUTE TTOGO', line=61)
W('35,3305', 0o23066, '', 'QXCH', 'PHSPRDT6', '** GROUP 6 TEMPORARY USED .. BEWARE **', line=62)

W('35,3306', 0o05546, '', 'TC', 'UPFLAG', 'SET TIMRFLAG', line=64)
W('35,3307', 0o00155, '', 'ADRES', 'TIMRFLAG', 'BIT 11 FLAG 7', kind='data', line=65)
W('35,3310', 0o35021, '', 'CAF', 'ZERO', line=66)
W('35,3311', 0o55145, '', 'TS', 'NVWORD1', line=67)

W('35,3312', 0o35017, '', 'CAF', 'ONE', line=69)
W('35,3313', 0o05245, '', 'TC', 'WAITLIST', line=70)
#   EBANK= TIG
W('35,3314', 0o03260, '', '2CADR', 'CLOKTASK', kind='data', line=72)
W('35,3315', 0o50067, kind='data', line=72)

W('35,3316', 0o05372, '', 'TC', '2PHSCHNG', line=74)
W('35,3317', 0o40036, '', 'OCT', '40036', '6.3SPOT FOR CLOKTASK', kind='data', line=75)
W('35,3320', 0o05024, '', 'OCT', '05024', 'GROUP 4 CONTINUES HERE', kind='data', line=76)
W('35,3321', 0o13000, '', 'OCT', '13000', kind='data', line=77)

W('35,3322', 0o01066, '', 'TC', 'PHSPRDT6', line=79)
# Page 636
# PROGRAM DESCRIPTION P30       DATE 3-6-67

# MOD.I BY S. ZELDIN-  TO ADD P31 AND AD APT P30 FOR P31 USE.   22DEC67
# FUNCTIONAL DESCRIPTION
# +30(EXTERNAL DELTA-V TARGETTING PROGRAM)
# ACCEPTS ASTRONAUT INPUTS OF TIG,DELV(LV) AND COMPUTES,FOR DISPLAY,
# APOGEE,PERIGEE,DELV(MAG),MGA ASSOCIATED WITH DESIRED MANEUVER

# P31(GENERAL LAMBERT AIMPOINT GUIDANCE)
# A GROUND RULE FOR P31 IS THE ANGLE BETWEEN THE TARGET VECTOR AND
# POSITION VECTOR AT TIG IS NOT 165-195 DEGREES APART
# BASED ON STORED INPUT OF OFFSET TARGET(B+29) AND DELTA T TRANS,AND
# ASTRONAUT ENTRY OF TIG,P31 COMPUTES REQUIRED VELOCITY FOR MANEUVER
# AND,FOR DISPLAY,APOGEE,PERIGEE,DELV(7AG),+MGA ASSOCIATED WITH
# DESIRED MANEUVER

# THE FOLLOWING SUBROUTINES ARE USED IN P30 AND P31
# S30.1 (P30 ONLY)
# S31.1 (P31 ONLY)
# P30/P31 - DISPLAYS TIG
# CNTUP30 - DISPLAYS DELV(LV)
# PARAM30 - DISPLAYS APOGEE,PERIGEE,DELV(MAG),MGA,TIME FROM TIG,
# MARKS SINCE LAST THRUSTING MANEUVER

# CALLING SEQUENCE VIA JOB FROM V37

# EXIT VIA V37 OR GOTOPOOH

# OUTPUT FOR POWERED FLIGHT
# VTIG    X
# RTIG     XSEE S30.1
# DELVSIN  X
# VGDISP
# RTARG   X
# TPASS4   X SEE S31.1
# X

#   COUNT 35/P30

W('35,3323', 0o03355, 'P30', 'TC', 'P30/P31', line=121)
W('35,3324', 0o03374, '', 'TC', 'CNTNUP30', line=122)
W('35,3325', 0o05560, '', 'TC', 'DOWNFLAG', 'RESET UPDATFLG', line=123)
W('35,3326', 0o00027, '', 'ADRES', 'UPDATFLG', 'BIT 7  FLAG 1', kind='data', line=124)
W('35,3327', 0o06006, '', 'TC', 'INTPRET', line=125)
W('35,3330', 0o77624, '', 'CALL', kind='interp', line=126)
W('35,3331', 0o63475, '', '', 'S30.1', kind='operand', line=127)
W('35,3332', 0o77776, '', 'EXIT', kind='interp', line=128)
W('35,3333', 0o03404, '', 'TC', 'PARAM30', line=129)
W('35,3334', 0o05546, '', 'TC', 'UPFLAG', line=130)
# Page 637
W('35,3335', 0o00045, '', 'ADRES', 'XDELVFLG', 'SET XDELVFLG BIT 8 FLAG 2', kind='data', line=132)
W('35,3336', 0o14106, '', 'TCF', 'GOTOPOOH', line=133)

W('35,3337', 0o03355, 'P31', 'TC', 'P30/P31', line=135)
W('35,3340', 0o05560, '', 'TC', 'DOWNFLAG', line=136)
W('35,3341', 0o00027, '', 'ADRES', 'UPDATFLG', 'RESET UPDATFLG BIT 7 FLAG 1', kind='data', line=137)
W('35,3342', 0o05560, '', 'TC', 'DOWNFLAG', line=138)
W('35,3343', 0o00156, '', 'ADRES', 'NORMSW', 'RESET NORMSW          BIT 10 FLAG 7', kind='data', line=139)
W('35,3344', 0o06006, '', 'TC', 'INTPRET', line=140)
W('35,3345', 0o77624, '', 'CALL', kind='interp', line=141)
W('35,3346', 0o63547, '', '', 'S31.1', kind='operand', line=142)
W('35,3347', 0o77776, '', 'EXIT', kind='interp', line=143)
W('35,3350', 0o03374, '', 'TC', 'CNTNUP30', line=144)
W('35,3351', 0o03404, '', 'TC', 'PARAM30', line=145)
W('35,3352', 0o05560, '', 'TC', 'DOWNFLAG', line=146)
W('35,3353', 0o00045, '', 'ADRES', 'XDELVFLG', 'BIT 8 FLAG 2', kind='data', line=147)
W('35,3354', 0o14106, '', 'TCF', 'GOTOPOOH', line=148)

W('35,3355', 0o56002, 'P30/P31', 'XCH', 'Q', line=150)
W('35,3356', 0o55664, '', 'TS', 'P30/31RT', line=151)
W('35,3357', 0o05546, '', 'TC', 'UPFLAG', line=152)
W('35,3360', 0o00027, '', 'ADRES', 'UPDATFLG', 'SET UPDATFLG BIT 7 FLAG 1', kind='data', line=153)
W('35,3361', 0o05546, '', 'TC', 'UPFLAG', line=154)
W('35,3362', 0o00031, '', 'ADRES', 'TRACKFLG', 'SET TRACKFLG BIT 5 FLAG 1', kind='data', line=155)
W('35,3363', 0o33441, '', 'CAF', 'V06N33', 'T OF IGN', line=156)
W('35,3364', 0o04662, '', 'TC', 'BANKCALL', line=157)
W('35,3365', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=158)
W('35,3366', 0o14106, '', 'TCF', 'GOTOPOOH', line=159)
W('35,3367', 0o01664, '', 'TC', 'P30/31RT', line=160)
W('35,3370', 0o13361, '', 'TCF', 'P30/P31 +4', line=161)
W('35,3371', 0o05412, '', 'TC', 'PHASCHNG', line=162)
W('35,3372', 0o00014, '', 'OCT', '00014', kind='data', line=163)
W('35,3373', 0o05217, '', 'TC', 'ENDOFJOB', line=164)

W('35,3374', 0o56002, 'CNTNUP30', 'XCH', 'Q', line=166)
W('35,3375', 0o55127, '', 'TS', 'P30/RET', line=167)
W('35,3376', 0o34620, '', 'CAF', 'V06N81', line=168)
W('35,3377', 0o04662, '', 'TC', 'BANKCALL', line=169)
W('35,3400', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=170)
W('35,3401', 0o14106, '', 'TCF', 'GOTOPOOH', line=171)
W('35,3402', 0o01127, '', 'TC', 'P30/RET', line=172)
W('35,3403', 0o13376, '', 'TCF', 'CNTNUP30 +2', line=173)
W('35,3404', 0o56002, 'PARAM30', 'XCH', 'Q', line=174)
W('35,3405', 0o55664, '', 'TS', 'P30/31RT', line=175)
W('35,3406', 0o33442, '', 'CAF', 'V06N42', line=176)
W('35,3407', 0o04662, '', 'TC', 'BANKCALL', line=177)
W('35,3410', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=178)
W('35,3411', 0o04106, '', 'TC', 'GOTOPOOH', 'ON TERMINATION GOTOPOOH', line=179)
W('35,3412', 0o13414, '', 'TCF', 'REFTEST', 'ON PROCEED GO DO REFTEST', line=180)
# Page 638
W('35,3413', 0o13406, '', 'TCF', 'PARAM30 +2', line=182)
W('35,3414', 0o35003, 'REFTEST', 'CAF', 'BIT13', line=183)
W('35,3415', 0o70077, '', 'MASK', 'STATE +3', 'REFSMFLAG', line=184)
W('35,3416', 0o00006, '', 'EXTEND', line=185)
W('35,3417', 0o13427, '', 'BZF', 'NOTSET', 'REFSMFLAG =0 , THEN BRANCH TO NOTSET', line=186)
W('35,3420', 0o06006, '', 'TC', 'INTPRET', line=187)
W('35,3421', 0o41575, '', 'VLOAD', 'PUSH', kind='interp', line=188)
W('35,3422', 0o03646, '', '', 'DELVSIN', kind='operand', line=189)
W('35,3423', 0o77624, '', 'CALL', kind='interp', line=190)
W('35,3424', 0o10654, '', '', 'GET+MGA', kind='operand', line=191)
W('35,3425', 0o77650, '', 'GOTO', kind='interp', line=192)
W('35,3426', 0o73433, '', '', 'FLASHMGA', kind='operand', line=193)
W('35,3427', 0o00006, 'NOTSET', 'EXTEND', line=194)
W('35,3430', 0o43440, '', 'DCS', 'MARSDP', line=195)
W('35,3431', 0o53626, '', 'DXCH', '+MGA', '+MGA, +MGA+1 CONTAINS (-00001)', line=196)
W('35,3432', 0o06006, '', 'TC', 'INTPRET', line=197)
W('35,3433', 0o77624, 'FLASHMGA', 'CALL', kind='interp', line=198)
W('35,3434', 0o73264, '', '', 'DISPMGA', kind='operand', line=199)
W('35,3435', 0o77776, '', 'EXIT', kind='interp', line=200)
W('35,3436', 0o01664, '', 'TC', 'P30/31RT', line=201)
W('35,3437', 0o00000, 'MARSDP', 'OCT', '00000', '(00000) (16440) = (+00001)', kind='data', line=202)
W('35,3440', 0o35100, '', 'OCT', '35100', kind='data', line=203)
# ( .01 ) DEGREES IN THE LOW ORDER REGISTE

W('35,3441', 0o01441, 'V06N33', 'VN', '0633', kind='data', line=206)
W('35,3442', 0o01452, 'V06N42', 'VN', '0642', kind='data', line=207)
W('35,3443', 0o04043, 'V16N35', 'VN', '1635', kind='data', line=208)
W('35,3444', 0o01455, 'V06N45', 'VN', '0645', kind='data', line=209)

# Page 639
# PROGRAM DESCRIPTION S30.1     DATE 9NOV66

# MOD NO 1                      LOG SECTION P30,P37
# MOD BY RAMA AIYAWAR **
# MOD.2 BY S.ZELDIN - TO CORRECT MOD.1 FOR COLOSSUS             29DEC67
# FUNCTIONAL DESCRIPTION
# BASED ON STORED TARGET PARAMETERS(R OF IGNITION(RTIG),V OF
# IGNITION(VTIG),TIME OF IGNITION(TIG),DELV(LV),COMPUTE PERIGEE ALTITUDE
# A+OGEE ALTITUDE AND DELTA-V REQUIRED IN REF. COORDS.(DELVSIN)
# CALLING SEQUENCE
# L       CALL
# L+1             S30.1
# NORMAL EXIT MODE
# AT L+2 OR CALLING SEQUENCE (GOTO L+2)
# SUBROUTINES CALLED
# THISPREC
# PERIAPO
# ALARM OR ABORT EXIT MODES
# NONE
# ERASABLE INITIALIZATION REQUIRED
# TIG             TIME OF IGNITION        DP      B28CS
# DELVSLV         SPECIFIED DELTA-V IN LOCAL VERT.
# COORDS. OF ACTIVE VEHICLE AT
# TIME OF IGNITION                        VCT.    B+7M/CS
#
# OUTPUT
# RTIG            POSITION AT TIG         VCT.    B+29M
# VTIG            VELOCITY AT TIG         VCT.    B+7M
# HAPO            APOGEE ALT.             DP      B+29M
# HPER            PERIGEE ALT.            DP      B+29M
# DELVSIN         DELVSLV IN REF COORDS   VCT.    B+7M/CS
# VGDISP          MAG. OF DELVSIN         DP      B+7M/CS
# DEBRIS        QTEMP   TEMP. ERASABLE
# QPRET,MPAC
# PUSHLIST

#   SETLOC P30S1A
#   BANK

#   COUNT 35/S30S

W('31,3475', 0o71220, 'S30.1', 'STQ', 'DLOAD', kind='interp', line=253)
W('31,3476', 0o03657, '', '', 'QTEMP', kind='operand', line=254)
W('31,3477', 0o03413, '', '', 'TIG', 'TIME IGNITION SCALED AT 2(+28)CS', kind='operand', line=255)
W('31,3500', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=256)
W('31,3501', 0o27071, '', '', 'THISPREC', 'ENCKE ROUTINE FOR', kind='operand', line=257)

W('31,3502', 0o67175, '', 'VLOAD', 'SXA,2', kind='interp', line=259)
W('31,3503', 0o00007, '', '', 'VATT', kind='operand', line=260)
W('31,3504', 0o03746, '', '', 'RTX2', kind='operand', line=261)
W('31,3505', 0o27640, '', 'STOVL', 'VTIG', kind='interp', line=262)
# Page 640
W('31,3506', 0o00001, '', '', 'RATT', kind='operand', line=264)
W('31,3507', 0o03632, '', 'STORE', 'RTIG', kind='interp', line=265)
W('31,3510', 0o03540, '', 'STORE', 'RACT3', kind='interp', line=266)
W('31,3511', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=267)
W('31,3512', 0o03640, '', '', 'VTIG', kind='operand', line=268)
W('31,3513', 0o36617, '', 'STCALL', 'UNRM', kind='interp', line=269)
W('31,3514', 0o72666, '', '', 'LOMAT', kind='operand', line=270)
W('31,3515', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=271)
W('31,3516', 0o03405, '', '', 'DELVSLV', kind='operand', line=272)
W('31,3517', 0o00001, '', '', '0', kind='operand', line=273)
W('31,3520', 0o66172, '', 'VSL1', 'SXA,1', kind='interp', line=274)
W('31,3521', 0o03745, '', '', 'RTX1', kind='operand', line=275)
W('31,3522', 0o03646, '', 'STORE', 'DELVSIN', kind='interp', line=276)
W('31,3523', 0o77646, '', 'ABVAL', kind='interp', line=277)
W('31,3524', 0o27773, '', 'STOVL', 'VGDISP', 'MAG DELV', kind='interp', line=278)
W('31,3525', 0o03632, '', '', 'RTIG', kind='operand', line=279)
W('31,3526', 0o53315, '', 'PDVL', 'VAD', kind='interp', line=280)
W('31,3527', 0o03646, '', '', 'DELVSIN', kind='operand', line=281)
W('31,3530', 0o03640, '', '', 'VTIG', kind='operand', line=282)
W('31,3531', 0o77624, '', 'CALL', kind='interp', line=283)
W('31,3532', 0o45153, '', '', 'PERIAPO1', kind='operand', line=284)
W('31,3533', 0o77624, '', 'CALL', kind='interp', line=285)
W('31,3534', 0o45263, '', '', 'SHIFTR1', kind='operand', line=286)
W('31,3535', 0o77624, '', 'CALL', kind='interp', line=287)
W('31,3536', 0o46754, '', '', 'MAXCHK', kind='operand', line=288)
W('31,3537', 0o16366, '', 'STODL', 'HPER', 'PERIGEE ALT B+29', kind='interp', line=289)
W('31,3540', 0o00005, '', '', '4D', kind='operand', line=290)
W('31,3541', 0o77624, '', 'CALL', kind='interp', line=291)
W('31,3542', 0o45263, '', '', 'SHIFTR1', kind='operand', line=292)
W('31,3543', 0o77624, '', 'CALL', kind='interp', line=293)
W('31,3544', 0o46754, '', '', 'MAXCHK', kind='operand', line=294)
W('31,3545', 0o36364, '', 'STCALL', 'HAPO', 'APOGEE ALT B+29', kind='interp', line=295)
W('31,3546', 0o03657, '', '', 'QTEMP', kind='operand', line=296)

# Page 641
# S31.1 PROGRAM DESCRIPTION             28DEC67
# MOD.1 BY S.ZELDIN

# S31.1 COMPUTES DELV IN REF AND LV COORDS,MAG OF DELV,INTERCEPT TIME,
# APOGEE AND PERIGEE ALT FOR REQUIRED MANEUVER

# CALLING SEQUENCE
# L       CALL
# L+1             S31.1

# NORMAL EXIT MODE
# AT L +2 OF CALLING SEQUENCE(GOTO L+2)
# SUBROUTINES CALLED
# AGAIN
# PERIAPO1
# SHIFTR1
# MIDGIM
# NO ALARM OR ABORT MODES
# INPUT
# DELLT4          DP      +28
# TIG             DP     +28
# RTARG           VCT     +29
# OUTPUT
# DELVLVC         VCT     +7
# VGDISP          DP      +7
# HAPO            DP      +29
# HPER            DP      +29
# TPASS4          DP      +28
# DEBRIS - QTEMP

W('31,3547', 0o71220, 'S31.1', 'STQ', 'DLOAD', kind='interp', line=329)
W('31,3550', 0o03657, '', '', 'QTEMP', kind='operand', line=330)
W('31,3551', 0o03413, '', '', 'TIG', kind='operand', line=331)
W('31,3552', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=332)
W('31,3553', 0o61651, '', '', 'AGAIN', 'RETURNS RTX2,RTX1,RATT,VATT,VIPRIME', kind='operand', line=333)
W('31,3554', 0o63375, '', 'VLOAD', 'PDVL', 'DELUEET3', kind='interp', line=334)
W('31,3555', 0o03632, '', '', 'RTIG', kind='operand', line=335)
W('31,3556', 0o03612, '', '', 'VIPRIME', kind='operand', line=336)
W('31,3557', 0o77624, '', 'CALL', kind='interp', line=337)
W('31,3560', 0o45153, '', '', 'PERIAPO1', kind='operand', line=338)
W('31,3561', 0o77624, '', 'CALL', kind='interp', line=339)
W('31,3562', 0o45263, '', '', 'SHIFTR1', kind='operand', line=340)
W('31,3563', 0o77624, '', 'CALL', kind='interp', line=341)
W('31,3564', 0o46754, '', '', 'MAXCHK', kind='operand', line=342)
W('31,3565', 0o16366, '', 'STODL', 'HPER', 'B29', kind='interp', line=343)
W('31,3566', 0o00005, '', '', '4D', kind='operand', line=344)
W('31,3567', 0o77624, '', 'CALL', kind='interp', line=345)
W('31,3570', 0o45263, '', '', 'SHIFTR1', kind='operand', line=346)
W('31,3571', 0o77624, '', 'CALL', kind='interp', line=347)
W('31,3572', 0o46754, '', '', 'MAXCHK', kind='operand', line=348)
W('31,3573', 0o26364, '', 'STOVL', 'HAPO', 'B29', kind='interp', line=349)
# Page 642
W('31,3574', 0o03646, '', '', 'DELVEET3', kind='operand', line=351)
W('31,3575', 0o00001, '', 'STORE', '0', kind='interp', line=352)
W('31,3576', 0o45014, '', 'SET', 'CALL', kind='interp', line=353)
W('31,3577', 0o01072, '', '', 'AVFLAG', kind='operand', line=354)
W('31,3600', 0o10647, '', '', 'MIDGIM', 'GET DELVLVC B7 FORDISPLAY', kind='operand', line=355)
W('31,3601', 0o77646, '', 'ABVAL', kind='interp', line=356)
W('31,3602', 0o17773, '', 'STODL', 'VGDISP', 'B+7 FOR DISPLAY', kind='interp', line=357)
W('31,3603', 0o03423, '', '', 'DELLT4', kind='operand', line=358)
W('31,3604', 0o77615, '', 'DAD', kind='interp', line=359)
W('31,3605', 0o03413, '', '', 'TIG', kind='operand', line=360)
W('31,3606', 0o37656, '', 'STCALL', 'TPASS4', 'FOR S40.1', kind='interp', line=361)
W('31,3607', 0o03657, '', '', 'QTEMP', kind='operand', line=362)

# Page 643
# SUBROUTINE NAME:      DELRSPL         (CONTINUATION OF V 82 IN CSM IF P11 ACTI
# TRANSFERRED COMPLETELY FROM SUNDISK, P30S REV 33.  9 SEPT 67.
# MOD NO: 0             MOD BY: ZELDIN          DATE:
# MOD NO: 1             MOD BY: RR BAIRNSFATHER DATE:  11 APR 67
# MOD NO: 2             MOD BY: RR BAIRNSFATHER DATE:  12 MAY 67        ADD UR.RT CALC WHEN BELOW 300K FT
# MOD NO: 2.1           MOD BY: RR BAIRNSFATHER DATE: 5 JULY 67         FIX ERROR ON MOD. 2.
# MOD NO: 3             MOD BY: RR BAIRNSFATHER DATE:  12 JUL 67        CHANGE SIGN OF DISPLAYED ERROR.
# MOD 4                 MOD BY  S.ZELDIN        DATE  3 APRIL 68        CHANGE EQUATIONS FOR L/D=.18 WHICH REPLA
# FUNCTION:             CALCULATE (FOR DISPLAY ON CALL) AN APPROXIMATE MEASURE OF IN-PLANE SPLASH DOWN
# ERROR.  IF THE FREE-FALL TRANSFER ANGLE TO 300K FT ABOVE PAD RADIUS IS POSITIVE:
# SPLASH ERROR= -RANGE TO TARGET + FREE-FALL TRANSFER ANGLE + ESTIMATED ENTRY ANGLE.
# THE TARGET LOCATION AT ESTIMATED TIME OF IMPACT IS USED.  IF THE FREE-FALL TRANSFER
# ANGLE IS NEGATIVE:  SPASH ERROR= -RANGE TO TARGET
# THE PRESENT TARGET LOCATION IS USED.
# CALLING SEQUENCE      CALLED AFTER SR30.1 IF IN CSM AND IF P11 OPERATING (UNDER CONTROL OF V82)
# SUBROUTINES CALLED:  VGAMCALC, TFF/TRIG, LALOTORV.
# EXIT:                 RETURN DIRECTLY TO V 82 PROG. AT SPLRET
# ERASABLE INITIALIZATION  LEFT BY SR30.1 AND V82GON1
# OUTPUT:       RSP-RREC RANGE IN REVOLUTIONS.                          DSKY DISPLAY IN N. MI.
# DEBRIS:       QPRET, PDL0 ...PDL7 ,PDL10

# THETA(1)

#   BANK 32
#   SETLOC DELRSPL1
#   BANK
#   COUNT* $$/P30  # PROGRAMS: P30 EXTERNAL DELTA V

W('32,2017', 0o00011, 'DELRSPL', 'STORE', '8D', kind='interp', line=393)
W('32,2020', 0o45244, '', 'BPL', 'DSU', kind='interp', line=394)
W('32,2021', 0o64067, '', '', 'CANTDO', 'GONE PAST 300K FT ALT', kind='operand', line=395)
W('32,2022', 0o16326, '', '', '1BITDP', kind='operand', line=396)
W('32,2023', 0o45000, '', 'BOV', 'CALL', kind='interp', line=397)
W('32,2024', 0o64067, '', '', 'CANTDO', 'POSMAX INDICATES NO 300K FT SOLUTION.', kind='operand', line=398)
W('32,2025', 0o55051, '', '', 'VGAMCALC', '+GAMMA(REV) IN PMAC,V300 MAG(B-7)=PDL 0', kind='operand', line=399)
W('32,2026', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=400)
W('32,2027', 0o56631, '', '', 'TFF/TRIG', kind='operand', line=401)
W('32,2030', 0o77624, '', 'CALL', kind='interp', line=402)
W('32,2031', 0o64075, '', '', 'AUGEKUGL', kind='operand', line=403)
W('32,2032', 0o65525, '', 'PDDL', 'ACOS', 'T ENTRY PDL 6', kind='interp', line=404)
W('32,2033', 0o00017, '', '', 'CDELF/2', kind='operand', line=405)
W('32,2034', 0o77615, '', 'DAD', kind='interp', line=406)
W('32,2035', 0o00005, '', '', '4', kind='operand', line=407)
W('32,2036', 0o26350, 'GETARG', 'STOVL', 'THETA(1)', kind='interp', line=408)
W('32,2037', 0o03401, '', '', 'LAT(SPL)', kind='operand', line=409)
W('32,2040', 0o15104, '', 'STODL', 'LAT', kind='interp', line=410)
W('32,2041', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=411)
W('32,2042', 0o15110, '', 'STODL', 'ALT', 'ALT=0 = LAT +4', kind='interp', line=412)
W('32,2043', 0o01205, '', '', 'PIPTIME', kind='operand', line=413)
# Page 644
W('32,2044', 0o71214, '', 'BON', 'DLOAD', kind='interp', line=415)
W('32,2045', 0o03711, '', '', 'V37FLAG', kind='operand', line=416)
W('32,2046', 0o64050, '', '', '+2', kind='operand', line=417)
W('32,2047', 0o02325, '', '', 'TSTART82', kind='operand', line=418)
W('32,2050', 0o43225, '', 'DSU', 'DAD', kind='interp', line=419)
W('32,2051', 0o00011, '', '', '8D', kind='operand', line=420)
W('32,2052', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=421)
W('32,2053', 0o00662, '', '', 'ERADFLAG', kind='operand', line=422)
W('32,2054', 0o26441, '', '', 'LALOTORV', 'R RECOV. IN ALPHAV AND MPAC', kind='operand', line=423)

W('32,2055', 0o63256, '', 'UNIT', 'PDVL', kind='interp', line=425)
W('32,2056', 0o02327, '', '', 'RONE', kind='operand', line=426)
W('32,2057', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=427)
W('32,2060', 0o65552, '', 'SL1', 'ARCCOS', kind='interp', line=428)
W('32,2061', 0o77621, '', 'BDSU', '', 'ERROR = THETA EST - THETA TARG', kind='interp', line=429)
# NEGATIVE NUMBER SIGNIFIES THAT WILL FALL SHORT.
# POSITIVE NUMBER SIGNIFIES THAT WILL OVERSHOOT.
W('32,2062', 0o02350, '', '', 'THETA(1)', kind='operand', line=432)
W('32,2063', 0o36356, 'DELRDONE', 'STCALL', 'RSP-RREC', 'DOWNRANGE RECOVERY RANGE ERROR        /360', kind='interp', line=433)
W('32,2064', 0o27455, '', '', 'INTWAKE0', kind='operand', line=434)
W('32,2065', 0o77624, '', 'CALL', kind='interp', line=435)
W('32,2066', 0o46653, '', '', 'SPLRET', kind='operand', line=436)
W('32,2067', 0o65345, 'CANTDO', 'DLOAD', 'PDDL', 'INITIALIZE ERASE TO DOT TARGET AND UR', kind='interp', line=437)
# FOR RANGE ANGLE.
W('32,2070', 0o15333, '', '', 'HIDPHALF', 'TO PDL 0 FOR DEN IN DDV.', kind='operand', line=439)
W('32,2071', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=440)
W('32,2072', 0o77606, '', 'PUSH', '', 'ZERO TO PDL 2 FOR PHI ENTRY', kind='interp', line=441)
W('32,2073', 0o34011, '', 'STCALL', '8D', kind='interp', line=442)
W('32,2074', 0o64036, '', '', 'GETARG', 'GO SET RSP-RREC =0', kind='operand', line=443)

W('32,2075', 0o77775, 'AUGEKUGL', 'VLOAD', kind='interp', line=445)
W('32,2076', 0o24256, '', '', 'X1CON -2', kind='operand', line=446)
W('32,2077', 0o14045, '', 'STODL', 'X1 -2', kind='interp', line=447)
W('32,2100', 0o00001, '', '', '0', kind='operand', line=448)
W('32,2101', 0o50025, '', 'DSU', 'BMN', kind='interp', line=449)
W('32,2102', 0o24250, '', '', 'V(21K)', kind='operand', line=450)
W('32,2103', 0o64130, '', '', 'LOOPSET', kind='operand', line=451)
W('32,2104', 0o65060, '', 'XSU,1', 'XCHX,2', kind='interp', line=452)
W('32,2105', 0o00050, '', '', 'S1', kind='operand', line=453)
W('32,2106', 0o00046, '', '', 'X1', kind='operand', line=454)
W('32,2107', 0o45324, '', 'XCHX,2', 'DSU', kind='interp', line=455)
W('32,2110', 0o00050, '', '', 'S1', kind='operand', line=456)
W('32,2111', 0o24236, '', '', 'V(3K)', kind='operand', line=457)
W('32,2112', 0o65040, '', 'BMN', 'XCHX,2', kind='interp', line=458)
W('32,2113', 0o64130, '', '', 'LOOPSET', kind='operand', line=459)
W('32,2114', 0o00050, '', '', 'S1', kind='operand', line=460)
W('32,2115', 0o50025, '', 'DSU', 'BMN', kind='interp', line=461)
W('32,2116', 0o24246, '', '', 'V(4K)', kind='operand', line=462)
W('32,2117', 0o64130, '', '', 'LOOPSET', kind='operand', line=463)
W('32,2120', 0o65124, '', 'XCHX,2', 'XCHX,2', kind='interp', line=464)
# Page 645
W('32,2121', 0o00050, '', '', 'S1', kind='operand', line=466)
W('32,2122', 0o00046, '', '', 'X1', kind='operand', line=467)
W('32,2123', 0o50025, '', 'DSU', 'BMN', kind='interp', line=468)
W('32,2124', 0o24232, '', '', 'V(400)', kind='operand', line=469)
W('32,2125', 0o64130, '', '', 'LOOPSET', kind='operand', line=470)
W('32,2126', 0o77730, '', 'SXA,1', kind='interp', line=471)
W('32,2127', 0o00050, '', '', 'S1', kind='operand', line=472)
W('32,2130', 0o52110, 'LOOPSET', 'INCR,1', 'GOTO', kind='interp', line=473)
W('32,2131', 0o00001, '', 'DEC', '1', kind='data', line=474)
W('32,2132', 0o64135, '', '', 'K1K2LOOP', kind='operand', line=475)
W('32,2133', 0o77730, 'K2CALC', 'SXA,1', kind='interp', line=476)
W('32,2134', 0o00050, '', '', 'S1', kind='operand', line=477)
W('32,2135', 0o44745, 'K1K2LOOP', 'DLOAD', 'DSU*', kind='interp', line=478)
W('32,2136', 0o00001, '', '', '0', kind='operand', line=479)
W('32,2137', 0o24245, '', '', 'V(32K) +1,1', kind='operand', line=480)
W('32,2140', 0o42603, '', 'DMP*', 'DAD*', kind='interp', line=481)
W('32,2141', 0o24231, '', '', 'YK1K2 +1,1', kind='operand', line=482)
W('32,2142', 0o24215, '', '', 'CK1K2 +1,1', kind='operand', line=483)
W('32,2143', 0o60125, '', 'PDDL', 'TIX,1', kind='interp', line=484)
W('32,2144', 0o00003, '', '', '2', kind='operand', line=485)
W('32,2145', 0o64133, '', '', 'K2CALC', kind='operand', line=486)
W('32,2146', 0o55225, '', 'DSU', 'BDDV', kind='interp', line=487)
W('32,2147', 0o40006, '', 'PUSH', 'BOV', kind='interp', line=488)
W('32,2150', 0o64173, '', '', 'MAXPHI', kind='operand', line=489)
W('32,2151', 0o45240, '', 'BMN', 'DSU', kind='interp', line=490)
W('32,2152', 0o64173, '', '', 'MAXPHI', kind='operand', line=491)
W('32,2153', 0o24200, '', '', 'MAXPHIC', kind='operand', line=492)
W('32,2154', 0o77644, '', 'BPL', kind='interp', line=493)
W('32,2155', 0o64173, '', '', 'MAXPHI', kind='operand', line=494)
W('32,2156', 0o45345, 'PHICALC', 'DLOAD', 'DSU', 'PHI ENTRY PDL 4D', kind='interp', line=495)
W('32,2157', 0o00001, '', '', '0', kind='operand', line=496)
W('32,2160', 0o24256, '', '', 'V(26K)', kind='operand', line=497)
W('32,2161', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=498)
W('32,2162', 0o64170, '', '', 'TGR26', kind='operand', line=499)
W('32,2163', 0o24252, '', '', 'TLESS26', kind='operand', line=500)
W('32,2164', 0o77671, '', 'DDV', kind='interp', line=501)
W('32,2165', 0o00001, '', '', '0', kind='operand', line=502)
W('32,2166', 0o43405, 'TENT', 'DMP', 'RVQ', kind='interp', line=503)
W('32,2167', 0o00005, '', '', '4D', kind='operand', line=504)
W('32,2170', 0o52145, 'TGR26', 'DLOAD', 'GOTO', kind='interp', line=505)
W('32,2171', 0o24254, '', '', 'TGR26CON', kind='operand', line=506)
W('32,2172', 0o64166, '', '', 'TENT', kind='operand', line=507)

W('32,2173', 0o65345, 'MAXPHI', 'DLOAD', 'PDDL', kind='interp', line=509)
W('32,2174', 0o24200, '', '', 'MAXPHIC', kind='operand', line=510)
W('32,2175', 0o77650, '', 'GOTO', kind='interp', line=511)
W('32,2176', 0o64156, '', '', 'PHICALC', kind='operand', line=512)
W('32,2177', 0o02755, 'MAXPHIC', '2DEC', '.09259298', '2000 NM FOR MAXIMUM PHI ENTRY', kind='data', line=513)
W('32,2200', 0o01307, kind='data', line=513)

# Page 646

#   COUNT* $$/P30

# BELOW
# <<<< TABLE IS INDEXED. KEEP IN ORDER >>>>

W('32,2201', 0o00013, '', '2DEC', '7.07304526 E-4', '5500', kind='data', line=522)
W('32,2202', 0o22652, kind='data', line=522)

W('32,2203', 0o00005, '', '2DEC', '3.08641975 E-4', '2400', kind='data', line=524)
W('32,2204', 0o01642, kind='data', line=524)

W('32,2205', 0o00005, '', '2DEC', '3.08641975 E-4', '2400', kind='data', line=526)
W('32,2206', 0o01642, kind='data', line=526)

W('32,2207', 0o77556, '', '2DEC', '-8.8888888 E-3', '-3.2', kind='data', line=528)
W('32,2210', 0o53522, kind='data', line=528)

W('32,2211', 0o00055, '', '2DEC', '2.7777777 E-3', '1', kind='data', line=530)
W('32,2212', 0o20266, kind='data', line=530)

W('32,2213', 0o00155, 'CK1K2', '2DEC', '6.6666666 E-3', '2.4', kind='data', line=532)
W('32,2214', 0o07202, kind='data', line=532)

W('32,2215', 0o00000, '', '2DEC', '0', '0', kind='data', line=534)
W('32,2216', 0o00000, kind='data', line=534)

W('32,2217', 0o77730, '', '2DEC*', '-1.86909989 E-5 B7*', '-.443', kind='data', line=536)
W('32,2220', 0o71525, kind='data', line=536)

W('32,2221', 0o00000, '', '2DEC', '0', kind='data', line=538)
W('32,2222', 0o00000, kind='data', line=538)

W('32,2223', 0o04445, '', '2DEC*', '1.11639691 E-3 B7*', '.001225', kind='data', line=540)
W('32,2224', 0o10102, kind='data', line=540)

W('32,2225', 0o03726, '', '2DEC*', '9.56911636 E-4 B7*', '.00105', kind='data', line=542)
W('32,2226', 0o31201, kind='data', line=542)

W('32,2227', 0o01040, 'YK1K2', '2DEC*', '2.59733157 E-4 B7*', '      .000285', kind='data', line=544)
W('32,2230', 0o26313, kind='data', line=544)

W('32,2231', 0o00234, 'V(400)', '2DEC', '1.2192 B-7', kind='data', line=546)
W('32,2232', 0o01660, kind='data', line=546)

W('32,2233', 0o25254, 'V(28K)', '2DEC', '85.344 B-7', kind='data', line=548)
W('32,2234', 0o01014, kind='data', line=548)

W('32,2235', 0o02222, 'V(3K)', '2DEC', '9.144 B-7', kind='data', line=550)
W('32,2236', 0o15646, kind='data', line=550)

W('32,2237', 0o22223, 'V(24K)', '2DEC', '73.152 B-7', kind='data', line=552)
W('32,2240', 0o16457, kind='data', line=552)

W('32,2241', 0o25254, '', '2DEC', '85.344 B-7', kind='data', line=554)
W('32,2242', 0o01014, kind='data', line=554)

W('32,2243', 0o30304, 'V(32K)', '2DEC', '97.536 B-7', kind='data', line=556)
W('32,2244', 0o23351, kind='data', line=556)

W('32,2245', 0o03030, 'V(4K)', '2DEC', '12.192 B-7', kind='data', line=558)
W('32,2246', 0o22335, kind='data', line=558)

W('32,2247', 0o20000, 'V(21K)', '2DEC', '64.000 B-7', kind='data', line=560)
W('32,2250', 0o00000, kind='data', line=560)

W('32,2251', 0o00033, 'TLESS26', '2DEC*', '5.70146688 E7 B-35*', '8660PHI/V', kind='data', line=562)
W('32,2252', 0o05763, kind='data', line=562)

W('32,2253', 0o00053, 'TGR26CON', '2DEC', '7.2 E5 B-28', 'PHI/3', kind='data', line=564)
W('32,2254', 0o36200, kind='data', line=564)

W('32,2255', 0o23637, 'V(26K)', '2DEC', '79.248 B-7', '26000', kind='data', line=566)
W('32,2256', 0o27636, kind='data', line=566)

# Page 647

W('32,2257', 0o00012, 'X1CON', 'DEC', '10', kind='data', line=570)

W('32,2260', 0o00010, '', 'DEC', '8', kind='data', line=572)

W('32,2261', 0o00006, '', 'DEC', '6', kind='data', line=574)
# <<<< TABLE IS INDEXED.  KEEP IN ORDER >>>>
# ABOVE
# Page 648
# ***** AVFLAGA/P *****

# SUBROUTINES USED

# UPFLAG
# DOWNFLAG
#   SETLOC P30SUBS
#   BANK
#   EBANK= SUBEXIT
W('4627', 0o00006, 'AVFLAGA', 'EXTEND', '', 'AVFLAG = CSM', line=587)
W('4630', 0o23770, '', 'QXCH', 'SUBEXIT', line=588)
W('4631', 0o05560, '', 'TC', 'DOWNFLAG', line=589)
W('4632', 0o00050, '', 'ADRES', 'AVFLAG', 'BIT 5 FLAG 2', kind='data', line=590)
W('4633', 0o35060, '', 'CAF', 'EBANK7', line=591)
W('4634', 0o54003, '', 'TS', 'EBANK', line=592)
#   EBANK= ECSTEER
W('4635', 0o35003, '', 'CAF', 'BIT13', line=594)
W('4636', 0o55424, '', 'TS', 'ECSTEER', 'SET ECSTEER = 1', line=595)
W('4637', 0o35005, '', 'CAF', 'EBANK4', line=596)
W('4640', 0o54003, '', 'TS', 'EBANK', line=597)
#   EBANK= SUBEXIT
W('4641', 0o01770, '', 'TC', 'SUBEXIT', line=599)
W('4642', 0o00006, 'AVFLAGP', 'EXTEND', '', 'AVFLAG = LEM', line=600)
W('4643', 0o23770, '', 'QXCH', 'SUBEXIT', line=601)
W('4644', 0o05546, '', 'TC', 'UPFLAG', line=602)
W('4645', 0o00050, '', 'ADRES', 'AVFLAG', 'BIT 5 FLAG 2', kind='data', line=603)
W('4646', 0o01770, '', 'TC', 'SUBEXIT', line=604)
W('4647', 0o00006, 'P20FLGON', 'EXTEND', line=605)
W('4650', 0o23770, '', 'QXCH', 'SUBEXIT', line=606)
W('4651', 0o05546, '', 'TC', 'UPFLAG', line=607)
W('4652', 0o00031, '', 'ADRES', 'TRACKFLG', kind='data', line=608)
W('4653', 0o05546, '', 'TC', 'UPFLAG', line=609)
W('4654', 0o00027, '', 'ADRES', 'UPDATFLG', kind='data', line=610)
W('4655', 0o01770, '', 'TC', 'SUBEXIT', 'DP    B4', line=611)
