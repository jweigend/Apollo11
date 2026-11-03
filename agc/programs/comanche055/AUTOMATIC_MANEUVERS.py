"""AUTOMATIC_MANEUVERS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/AUTOMATIC_MANEUVERS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1025-1036 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('AUTOMATIC_MANEUVERS', 'AUTOMATIC_MANEUVERS.agc', 'Comanche055', pages='1025-1036')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     AUTOMATIC_MANEUVERS.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1025-1036
# Mod history:  2009-05-13 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
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

# Page 1025
#   BANK 21
#   SETLOC DAPS3
#   BANK

#   COUNT 21/DAPAM

#   EBANK= KMPAC
W('21,3250', 0o00006, 'AHFNOROT', 'EXTEND', line=38)
W('21,3251', 0o00031, '', 'READ', 'CHAN31', line=39)
W('21,3252', 0o75002, '', 'MASK', 'BIT14', line=40)
W('21,3253', 0o00006, '', 'EXTEND', line=41)
W('21,3254', 0o63272, '', 'BZMF', 'FREECONT', line=42)
W('21,3255', 0o31501, '', 'CA', 'RCSFLAGS', 'SEE IF RATE FILTER HAS BEEN INITIALIZED', line=43)
W('21,3256', 0o75002, '', 'MASK', 'BIT14', line=44)
W('21,3257', 0o10000, '', 'CCS', 'A', 'IF SO, PROCEED WITH ATTITUDE CONTROL', line=45)
W('21,3260', 0o12534, '', 'TCF', 'REINIT', 'IF NOT, RECYCLE TO INITIALIZE FILTER', line=46)
# AUTOMATIC CONTROL YET
W('21,3261', 0o00006, '', 'EXTEND', line=48)
W('21,3262', 0o00031, '', 'READ', 'CHAN31', line=49)
W('21,3263', 0o75003, '', 'MASK', 'BIT13', line=50)
W('21,3264', 0o00006, '', 'EXTEND', line=51)
W('21,3265', 0o63372, '', 'BZMF', 'HOLDFUNC', line=52)

W('21,3266', 0o31332, 'AUTOCONT', 'CA', 'HOLDFLAG', 'IF HOLDFLAG IS +, GO TO GRABANG.', line=55)
W('21,3267', 0o00006, '', 'EXTEND', '', 'OTHERWISE, GO TO ATTHOLD.', line=56)
W('21,3270', 0o63322, '', 'BZMF', 'ATTHOLD', line=57)
W('21,3271', 0o13376, '', 'TCF', 'GRABANG', line=58)

# MINIMUM IMPULSE CONTROL

W('21,3272', 0o35017, 'FREECONT', 'CAF', 'ONE', line=62)
W('21,3273', 0o55332, '', 'TS', 'HOLDFLAG', 'RESET HOLDFLAG', line=63)
# INHIBIT AUTOMATIC STEERING
W('21,3274', 0o00006, '', 'EXTEND', line=65)
W('21,3275', 0o00032, '', 'READ', 'CHAN32', line=66)
W('21,3276', 0o54001, '', 'TS', 'L', line=67)
W('21,3277', 0o40000, '', 'COM', line=68)
W('21,3300', 0o73036, '', 'MASK', 'MANROT', line=69)
W('21,3301', 0o71633, '', 'MASK', 'CHANTEMP', line=70)
W('21,3302', 0o23633, '', 'LXCH', 'CHANTEMP', line=71)
W('21,3303', 0o03130, '', 'TC', 'STICKCHK', line=72)
W('21,3304', 0o51656, '', 'INDEX', 'RMANNDX', line=73)
W('21,3305', 0o33316, '', 'CA', 'MINTAU', 'MINTAU        +0', line=74)
W('21,3306', 0o55561, '', 'TS', 'TAU', '              +1      +14MS MINIMUM IMPULSE', line=75)
W('21,3307', 0o51657, '', 'INDEX', 'PMANNDX', '              +2      -14MS TIME', line=76)
W('21,3310', 0o33316, '', 'CA', 'MINTAU', '              +3      +0', line=77)
W('21,3311', 0o55562, '', 'TS', 'TAU1', line=78)
W('21,3312', 0o51660, '', 'INDEX', 'YMANNDX', line=79)
W('21,3313', 0o33316, '', 'CA', 'MINTAU', line=80)
# Page 1026
W('21,3314', 0o55563, '', 'TS', 'TAU2', line=82)
W('21,3315', 0o13067, '', 'TCF', 'T6PROGM', line=83)

W('21,3316', 0o00000, 'MINTAU', 'DEC', '0', kind='data', line=86)
W('21,3317', 0o00027, '', 'DEC', '23', '= 14MS', kind='data', line=87)
W('21,3320', 0o77750, '', 'DEC', '-23', '= -14MS', kind='data', line=88)
W('21,3321', 0o00000, '', 'DEC', '0', kind='data', line=89)

# Page 1027
# CALCULATION OF ATTITUDE ERRORS-
# -    *     -      -          -
# AK = AMGB (CDUX - THETADX) + BIAS
#
# IE    *AK *   * 1        SIN(PSI)        0    ** CDUX - THETADX *    *BIAS *
# *   *   *                               **                *    *     *
# *AK1* = * 0   COS(PSI)COS(PHI)  SIN(PHI)** CDUY - THETADY *  + *BIAS1*
# *   *   *                               **                *    *     *
# *AK2*   * 0  -COS(PSI)SIN(PHI)  COS(PHI)** CDUZ - THETADZ *    *BIAS2*
#
# THE BIASES ARE ADDED ONLY WHILE PERFORMING AUTOMATIC MANEUVERS (ESP KALCMANU) TO PROVIDE ADDITIONAL LEAD
# AND PREVENT OVERSHOOT WHEN STARTING AN AUTOMATIC MANEUVER.  NORMALLY THE REQUIRED LEAD IS ONLY 1-2 DEGREES.
# BUT DURING HIGH RATE MANEUVERS IT CAN BE AS MUCH AS 7 DEGREES.  THE BIASES ARE COMPUTED BY KALCMANU AND REMAIN
# FIXED UNTIL THE MANEUVER IS COMPLETED AT WHICH TIME THEY ARE RESET TO ZERO.

W('21,3322', 0o30032, 'ATTHOLD', 'CA', 'CDUX', line=108)
W('21,3323', 0o00006, '', 'EXTEND', line=109)
W('21,3324', 0o21572, '', 'MSU', 'THETADX', line=110)
W('21,3325', 0o55567, '', 'TS', 'ERRORX', line=111)
W('21,3326', 0o30033, '', 'CA', 'CDUY', line=112)
W('21,3327', 0o00006, '', 'EXTEND', line=113)
W('21,3330', 0o21573, '', 'MSU', 'THETADY', line=114)
W('21,3331', 0o55502, '', 'TS', 'T5TEMP', line=115)
W('21,3332', 0o00006, '', 'EXTEND', line=116)
W('21,3333', 0o71640, '', 'MP', 'AMGB1', line=117)
W('21,3334', 0o27567, '', 'ADS', 'ERRORX', line=118)
W('21,3335', 0o31502, '', 'CA', 'T5TEMP', line=119)
W('21,3336', 0o00006, '', 'EXTEND', line=120)
W('21,3337', 0o71641, '', 'MP', 'AMGB4', line=121)
W('21,3340', 0o55570, '', 'TS', 'ERRORY', line=122)
W('21,3341', 0o31502, '', 'CA', 'T5TEMP', line=123)
W('21,3342', 0o00006, '', 'EXTEND', line=124)
W('21,3343', 0o71643, '', 'MP', 'AMGB7', line=125)
W('21,3344', 0o55571, '', 'TS', 'ERRORZ', line=126)
W('21,3345', 0o30034, '', 'CA', 'CDUZ', line=127)
W('21,3346', 0o00006, '', 'EXTEND', line=128)
W('21,3347', 0o21574, '', 'MSU', 'THETADZ', line=129)
W('21,3350', 0o55502, '', 'TS', 'T5TEMP', line=130)
W('21,3351', 0o00006, '', 'EXTEND', line=131)
W('21,3352', 0o71642, '', 'MP', 'AMGB5', line=132)
W('21,3353', 0o27570, '', 'ADS', 'ERRORY', line=133)
W('21,3354', 0o31502, '', 'CA', 'T5TEMP', line=134)
W('21,3355', 0o00006, '', 'EXTEND', line=135)
W('21,3356', 0o71644, '', 'MP', 'AMGB8', line=136)
W('21,3357', 0o27571, '', 'ADS', 'ERRORZ', line=137)
W('21,3360', 0o41332, '', 'CS', 'HOLDFLAG', line=138)
W('21,3361', 0o00006, '', 'EXTEND', line=139)
# Page 1028
W('21,3362', 0o63441, '', 'BZMF', 'JETS', line=141)
W('21,3363', 0o31564, '', 'CA', 'BIAS', 'AD BIASES ONLY IF PERFORMING AUTOMATIC', line=142)
W('21,3364', 0o27567, '', 'ADS', 'ERRORX', line=143)
W('21,3365', 0o31565, '', 'CA', 'BIAS1', line=144)
W('21,3366', 0o27570, '', 'ADS', 'ERRORY', line=145)
W('21,3367', 0o31566, '', 'CA', 'BIAS2', line=146)
W('21,3370', 0o27571, '', 'ADS', 'ERRORZ', line=147)
W('21,3371', 0o13441, '', 'TCF', 'JETS', line=148)

W('21,3372', 0o11332, 'HOLDFUNC', 'CCS', 'HOLDFLAG', line=151)
W('21,3373', 0o13376, '', 'TCF', '+3', line=152)
W('21,3374', 0o13322, '', 'TCF', 'ATTHOLD', line=153)
W('21,3375', 0o13376, '', 'TCF', '+1', line=154)
W('21,3376', 0o35021, 'GRABANG', 'CAF', 'ZERO', 'ZERO WBODYS AND BIASES', line=155)
W('21,3377', 0o55525, '', 'TS', 'WBODY', line=156)
W('21,3400', 0o55526, '', 'TS', 'WBODY +1', line=157)
W('21,3401', 0o55527, '', 'TS', 'WBODY1', line=158)
W('21,3402', 0o55530, '', 'TS', 'WBODY1 +1', line=159)
W('21,3403', 0o55531, '', 'TS', 'WBODY2', line=160)
W('21,3404', 0o55532, '', 'TS', 'WBODY2 +1', line=161)
W('21,3405', 0o55564, '', 'TS', 'BIAS', line=162)
W('21,3406', 0o55565, '', 'TS', 'BIAS1', line=163)
W('21,3407', 0o55566, '', 'TS', 'BIAS2', line=164)

W('21,3410', 0o31501, '', 'CA', 'RCSFLAGS', line=166)
W('21,3411', 0o73037, '', 'MASK', 'OCT16000', line=167)
W('21,3412', 0o00006, '', 'EXTEND', '', 'IS RATE DAMPING COMPLETED', line=168)
W('21,3413', 0o13421, '', 'BZF', 'ENDDAMP', 'IF SO, GO TO ENDDAMP', line=169)
W('21,3414', 0o35021, '', 'CAF', 'ZERO', 'OTHERWISE, ZERO ERRORS', line=170)
W('21,3415', 0o55567, '', 'TS', 'ERRORX', line=171)
W('21,3416', 0o55570, '', 'TS', 'ERRORY', line=172)
W('21,3417', 0o55571, '', 'TS', 'ERRORZ', line=173)
W('21,3420', 0o13441, '', 'TCF', 'JETS', line=174)

W('21,3421', 0o55332, 'ENDDAMP', 'TS', 'HOLDFLAG', 'SET HOLDFLAG +0', line=176)
W('21,3422', 0o00006, '', 'EXTEND', line=177)
W('21,3423', 0o30033, '', 'DCA', 'CDUX', 'PICK UP CDU ANGLES FOR ATTITUDE HOLD', line=178)
W('21,3424', 0o53573, '', 'DXCH', 'THETADX', 'REFERENCES', line=179)
W('21,3425', 0o30034, '', 'CA', 'CDUZ', line=180)
W('21,3426', 0o55574, '', 'TS', 'THETADZ', line=181)
W('21,3427', 0o13322, '', 'TCF', 'ATTHOLD', line=182)

# Page 1029
# JET SWITCHING LOGIC AND CALCULATION OF REQUIRED ROTATION COMMANDS
#
# DETERMINE THE LOCATION OF THE RATE ERROR AND THE ATTITUDE ERROR RELATIVE TO THE SWITCHING LOGIC IN THE PHASE
# PLANE.
# COMPUTE THE CHANGE IN RATE CORRESPONDING TO THE ATTITUDE ERROR NECESSARY TO DRIVE THE THE S/C INTO THE
# APPROPRIATE DEADZONE.
#
# .
# R22                          RATE . ERROR
# WL+H                         .
# *********************************   .                                 ***** SWITCH LINES ENCLOSING DEADZONES
# R23  WL                        *  .
# ----------------------------------* .                                 ----- DESIRED RATE LINES
# R23  WL-H       -                *.
# ****************** -                .                                 R20, R21, R22, ETC REGIONS IN PHASE
# * -               .* R18      R20       R21         PLANE FOF COMPUTING DESIRED RESPONSE
# *                . *
# *-              .  *
# R22             R24*-    R23      .   *
# *             .    *
# *            .     *
# + -ADB      .      * AF              ATTITUDE
# ........................+--+---------------+--+........................
# AF *      .     +ADB  +             ERROR
# *     .            *
# *    .            -*
# *   .             -*
# *  .              -*
# * .                *
# *.               - *
# .                - *****************
# .*                -
# . * --------------------------------
# .  *
# .   ********************************
# .

# FIG. 1  PHASE PLANE SWITCHING LOGIC

# CONSTANTS FOR JET SWITCHING LOGIC

W('21,3430', 0o00114, 'WLH/SLOP', 'DEC', '.00463', '= WL+H/SLOPE = .83333 DEG     $180', kind='data', line=227)
W('21,3431', 0o00055, 'WL-H/SLP', 'DEC', '.00277', '= WL-H/SLOPE = .5 DEG         $180', kind='data', line=228)
W('21,3432', 0o00022, 'WLH', '2DEC', '.0011111111', '= WL+H = 0.5 DEG/SEC          $450', kind='data', line=229)
W('21,3433', 0o06426, kind='data', line=229)

W('21,3434', 0o00012, 'WLMH', '2DEC', '.0006666666', '= WL-H = 0.3 DEG/SEC          $450', kind='data', line=231)
W('21,3435', 0o35415, kind='data', line=231)

W('21,3436', 0o00016, 'WL', '2DEC', '.0008888888', '= WL   = 0.4 DEG/SEC          $450', kind='data', line=233)
W('21,3437', 0o22021, kind='data', line=233)

# Page 1030
W('21,3440', 0o12173, 'SLOPE2', 'DEC', '.32', '= 0.8 DEG/SEC/DEG             $450/180', kind='data', line=236)
W('21,3441', 0o31655, 'JETS', 'CA', 'ADB', line=237)
W('21,3442', 0o65015, '', 'AD', 'FOUR', 'AF = FLAT REGION = .044 DEG', line=238)
W('21,3443', 0o55502, '', 'TS', 'T5TEMP', 'ADB+AF', line=239)
W('21,3444', 0o35016, '', 'CAF', 'TWO', line=240)
W('21,3445', 0o55506, 'JLOOP', 'TS', 'SPNDX', line=241)
W('21,3446', 0o60000, '', 'DOUBLE', line=242)
W('21,3447', 0o55507, '', 'TS', 'DPNDX', line=243)
W('21,3450', 0o00006, '', 'EXTEND', line=244)
W('21,3451', 0o50000, '', 'INDEX', 'A', line=245)
W('21,3452', 0o31534, '', 'DCA', 'ADOT', line=246)
W('21,3453', 0o53516, '', 'DXCH', 'EDOT', line=247)
W('21,3454', 0o31332, '', 'CA', 'HOLDFLAG', 'HOLDFLAG = +0 MEANS THAT DAP IS IN', line=248)
W('21,3455', 0o00006, '', 'EXTEND', '', 'ATTITUDE HOLD AND RATE DAMPING IS OVER.', line=249)
W('21,3456', 0o13463, '', 'BZF', 'INHOLD', 'IF THIS IS THE CASE, BYPASS ADDITION', line=250)
# OF WBODY AND GO TO INHOLD
W('21,3457', 0o00006, '', 'EXTEND', line=252)
W('21,3460', 0o51507, '', 'INDEX', 'DPNDX', line=253)
W('21,3461', 0o41526, '', 'DCS', 'WBODY', line=254)
W('21,3462', 0o21516, '', 'DAS', 'EDOT', '= ADOT-WBODY', line=255)
W('21,3463', 0o51506, 'INHOLD', 'INDEX', 'SPNDX', line=256)
W('21,3464', 0o31567, '', 'CA', 'ERRORX', line=257)
W('21,3465', 0o55517, '', 'TS', 'AERR', 'AERR = BIAS + AK', line=258)

W('21,3466', 0o11515, '', 'CCS', 'EDOT', line=260)
W('21,3467', 0o13477, '', 'TCF', 'POSVEL', line=261)
W('21,3470', 0o13472, '', 'TCF', 'SIGNCK1', line=262)
W('21,3471', 0o13507, '', 'TCF', 'NEGVEL', line=263)
W('21,3472', 0o11516, 'SIGNCK1', 'CCS', 'EDOT +1', line=264)
W('21,3473', 0o13477, '', 'TCF', 'POSVEL', line=265)
W('21,3474', 0o13477, '', 'TCF', 'POSVEL', line=266)
W('21,3475', 0o13507, '', 'TCF', 'NEGVEL', line=267)
W('21,3476', 0o13507, '', 'TCF', 'NEGVEL', line=268)
W('21,3477', 0o00006, 'POSVEL', 'EXTEND', line=269)
W('21,3500', 0o31516, '', 'DCA', 'EDOT', line=270)
W('21,3501', 0o53521, '', 'DXCH', 'EDOTVEL', line=271)
W('21,3502', 0o31502, '', 'CA', 'T5TEMP', line=272)
W('21,3503', 0o55523, '', 'TS', 'ADBVEL', '+(ADB+AF)', line=273)
W('21,3504', 0o31517, '', 'CA', 'AERR', line=274)
W('21,3505', 0o55522, '', 'TS', 'AERRVEL', line=275)
W('21,3506', 0o03516, '', 'TC', 'J6.', line=276)
W('21,3507', 0o00006, 'NEGVEL', 'EXTEND', line=277)
W('21,3510', 0o41516, '', 'DCS', 'EDOT', line=278)
W('21,3511', 0o53521, '', 'DXCH', 'EDOTVEL', line=279)
W('21,3512', 0o41502, '', 'CS', 'T5TEMP', line=280)
W('21,3513', 0o55523, '', 'TS', 'ADBVEL', '-(ADB+AF)', line=281)
W('21,3514', 0o41517, '', 'CS', 'AERR', line=282)
W('21,3515', 0o55522, '', 'TS', 'AERRVEL', line=283)

W('21,3516', 0o00006, 'J6.', 'EXTEND', line=285)
# Page 1031
W('21,3517', 0o61655, '', 'SU', 'ADB', line=287)
W('21,3520', 0o63430, '', 'AD', 'WLH/SLOP', line=288)
W('21,3521', 0o00006, '', 'EXTEND', line=289)
W('21,3522', 0o63551, '', 'BZMF', 'J8', line=290)

W('21,3523', 0o41502, '', 'CS', 'T5TEMP', '(ADB+AF)', line=292)
W('21,3524', 0o61522, '', 'AD', 'AERRVEL', line=293)
W('21,3525', 0o00006, '', 'EXTEND', line=294)
W('21,3526', 0o63530, '', 'BZMF', '+2', line=295)
W('21,3527', 0o13542, '', 'TCF', 'J7', line=296)
W('21,3530', 0o00006, '', 'EXTEND', line=297)
W('21,3531', 0o41521, '', 'DCS', 'EDOTVEL', line=298)
W('21,3532', 0o00006, '', 'EXTEND', line=299)
W('21,3533', 0o11654, '', 'DV', 'SLOPE', line=300)
W('21,3534', 0o00006, '', 'EXTEND', line=301)
W('21,3535', 0o61522, '', 'SU', 'AERRVEL', line=302)
W('21,3536', 0o61655, '', 'AD', 'ADB', line=303)
W('21,3537', 0o00006, '', 'EXTEND', line=304)
W('21,3540', 0o63630, '', 'BZMF', 'J18', line=305)
W('21,3541', 0o13704, '', 'TCF', 'J23', line=306)

W('21,3542', 0o43431, 'J7', 'CS', 'WL-H/SLP', line=308)
W('21,3543', 0o00006, '', 'EXTEND', line=309)
W('21,3544', 0o61502, '', 'SU', 'T5TEMP', '(ADB+AF)', line=310)
W('21,3545', 0o61522, '', 'AD', 'AERRVEL', line=311)
W('21,3546', 0o00006, '', 'EXTEND', line=312)
W('21,3547', 0o63634, '', 'BZMF', 'J20', line=313)
W('21,3550', 0o13645, '', 'TCF', 'J21', line=314)

W('21,3551', 0o00006, 'J8', 'EXTEND', line=316)
W('21,3552', 0o43433, '', 'DCS', 'WLH', line=317)
W('21,3553', 0o53514, '', 'DXCH', 'WTEMP', line=318)
W('21,3554', 0o00006, '', 'EXTEND', line=319)
W('21,3555', 0o31521, '', 'DCA', 'EDOTVEL', line=320)
W('21,3556', 0o21514, '', 'DAS', 'WTEMP', line=321)
W('21,3557', 0o11513, '', 'CCS', 'WTEMP', line=322)
W('21,3560', 0o13673, '', 'TCF', 'J22', line=323)
W('21,3561', 0o13563, '', 'TCF', 'SIGNCK2', line=324)
W('21,3562', 0o13567, '', 'TCF', 'NJ22', line=325)
W('21,3563', 0o11514, 'SIGNCK2', 'CCS', 'WTEMP +1', line=326)
W('21,3564', 0o13673, '', 'TCF', 'J22', line=327)
W('21,3565', 0o13673, '', 'TCF', 'J22', line=328)
W('21,3566', 0o13567, '', 'TCF', 'NJ22', line=329)

W('21,3567', 0o00006, 'NJ22', 'EXTEND', line=331)
W('21,3570', 0o31521, '', 'DCA', 'EDOTVEL', line=332)
W('21,3571', 0o00006, '', 'EXTEND', line=333)
W('21,3572', 0o11654, '', 'DV', 'SLOPE', line=334)
W('21,3573', 0o61502, '', 'AD', 'T5TEMP', '(ADB+AF)', line=335)
W('21,3574', 0o61522, '', 'AD', 'AERRVEL', line=336)
# Page 1032
W('21,3575', 0o10000, '', 'CCS', 'A', line=338)
W('21,3576', 0o13704, '', 'TCF', 'J23', line=339)
W('21,3577', 0o13704, '', 'TCF', 'J23', line=340)
W('21,3600', 0o13602, '', 'TCF', '+2', line=341)
W('21,3601', 0o13704, '', 'TCF', 'J23', line=342)

W('21,3602', 0o00006, '', 'EXTEND', line=344)
W('21,3603', 0o43435, '', 'DCS', 'WLMH', 'WL - H', line=345)
W('21,3604', 0o53514, '', 'DXCH', 'WTEMP', line=346)
W('21,3605', 0o00006, '', 'EXTEND', line=347)
W('21,3606', 0o31521, '', 'DCA', 'EDOTVEL', line=348)
W('21,3607', 0o21514, '', 'DAS', 'WTEMP', line=349)
W('21,3610', 0o11513, '', 'CCS', 'WTEMP', line=350)
W('21,3611', 0o13704, '', 'TCF', 'J23', line=351)
W('21,3612', 0o13614, '', 'TCF', 'SIGNCK3', line=352)
W('21,3613', 0o13620, '', 'TCF', 'NJ23', line=353)
W('21,3614', 0o11514, 'SIGNCK3', 'CCS', 'WTEMP +1', line=354)
W('21,3615', 0o13704, '', 'TCF', 'J23', line=355)
W('21,3616', 0o13704, '', 'TCF', 'J23', line=356)
W('21,3617', 0o13620, '', 'TCF', 'NJ23', line=357)

W('21,3620', 0o31522, 'NJ23', 'CA', 'AERRVEL', line=359)
W('21,3621', 0o61502, '', 'AD', 'T5TEMP', '(ADB+AF)', line=360)
W('21,3622', 0o63431, '', 'AD', 'WL-H/SLP', line=361)
W('21,3623', 0o10000, '', 'CCS', 'A', line=362)
W('21,3624', 0o13716, '', 'TCF', 'J24', line=363)
W('21,3625', 0o13716, '', 'TCF', 'J24', line=364)
W('21,3626', 0o13673, '', 'TCF', 'J22', line=365)
W('21,3627', 0o13673, '', 'TCF', 'J22', line=366)

W('21,3630', 0o00006, 'J18', 'EXTEND', line=368)
W('21,3631', 0o41516, '', 'DCS', 'EDOT', line=369)
W('21,3632', 0o53511, '', 'DXCH', 'KMPAC', line=370)
W('21,3633', 0o13727, '', 'TCF', 'JTIME', line=371)

W('21,3634', 0o41517, 'J20', 'CS', 'AERR', line=373)
W('21,3635', 0o61523, '', 'AD', 'ADBVEL', line=374)
W('21,3636', 0o00006, '', 'EXTEND', line=375)
W('21,3637', 0o73440, '', 'MP', 'SLOPE2', '(HYSTERESIS SLOPE)', line=376)
W('21,3640', 0o53511, '', 'DXCH', 'KMPAC', line=377)
W('21,3641', 0o00006, '', 'EXTEND', line=378)
W('21,3642', 0o41516, '', 'DCS', 'EDOT', line=379)
W('21,3643', 0o21511, '', 'DAS', 'KMPAC', line=380)
W('21,3644', 0o13727, '', 'TCF', 'JTIME', line=381)

W('21,3645', 0o11515, 'J21', 'CCS', 'EDOT', line=383)
W('21,3646', 0o13664, '', 'TCF', 'JP', line=384)
W('21,3647', 0o13651, '', 'TCF', 'SIGNCK4', line=385)
W('21,3650', 0o13655, '', 'TCF', 'JN', line=386)
W('21,3651', 0o11516, 'SIGNCK4', 'CCS', 'EDOT +1', line=387)
# Page 1033
W('21,3652', 0o13664, '', 'TCF', 'JP', line=389)
W('21,3653', 0o13664, '', 'TCF', 'JP', line=390)
W('21,3654', 0o13655, '', 'TCF', 'JN', line=391)
W('21,3655', 0o00006, 'JN', 'EXTEND', line=392)
W('21,3656', 0o41516, '', 'DCS', 'EDOT', line=393)
W('21,3657', 0o53511, '', 'DXCH', 'KMPAC', line=394)
W('21,3660', 0o00006, '', 'EXTEND', line=395)
W('21,3661', 0o33437, '', 'DCA', 'WL', line=396)
W('21,3662', 0o21511, '', 'DAS', 'KMPAC', line=397)
W('21,3663', 0o13727, '', 'TCF', 'JTIME', line=398)

W('21,3664', 0o00006, 'JP', 'EXTEND', line=400)
W('21,3665', 0o41516, '', 'DCS', 'EDOT', line=401)
W('21,3666', 0o53511, '', 'DXCH', 'KMPAC', line=402)
W('21,3667', 0o00006, '', 'EXTEND', line=403)
W('21,3670', 0o43437, '', 'DCS', 'WL', line=404)
W('21,3671', 0o21511, '', 'DAS', 'KMPAC', line=405)
W('21,3672', 0o13727, '', 'TCF', 'JTIME', line=406)

W('21,3673', 0o11515, 'J22', 'CCS', 'EDOT', line=408)
W('21,3674', 0o13655, '', 'TCF', 'JN', line=409)
W('21,3675', 0o13677, '', 'TCF', 'SIGNCK5', line=410)
W('21,3676', 0o13664, '', 'TCF', 'JP', line=411)
W('21,3677', 0o11516, 'SIGNCK5', 'CCS', 'EDOT +1', line=412)
W('21,3700', 0o13655, '', 'TCF', 'JN', line=413)
W('21,3701', 0o13655, '', 'TCF', 'JN', line=414)
W('21,3702', 0o13664, '', 'TCF', 'JP', line=415)
W('21,3703', 0o13664, '', 'TCF', 'JP', line=416)

W('21,3704', 0o51506, 'J23', 'INDEX', 'SPNDX', line=418)
W('21,3705', 0o45003, '', 'CS', 'BIT13', 'RESET RATE DAMPING FLAG', line=419)
W('21,3706', 0o71501, '', 'MASK', 'RCSFLAGS', 'BIT13 FOR ROLL  (SPNDX = 0)', line=420)
W('21,3707', 0o55501, '', 'TS', 'RCSFLAGS', 'BIT12 FOR PITCH (SPNDX = 1)', line=421)
# BIT11 FOR YAW   (SPNDX = 2)

W('21,3710', 0o51506, '', 'INDEX', 'SPNDX', line=424)
W('21,3711', 0o33033, '', 'CAF', 'OCT01400', 'IS THERE TO BE A FORCED FIRING ON THIS', line=425)
W('21,3712', 0o71501, '', 'MASK', 'RCSFLAGS', 'AXIS', line=426)
W('21,3713', 0o00006, '', 'EXTEND', line=427)
W('21,3714', 0o13750, '', 'BZF', 'DOJET +2', 'NO, GO TO DOJET +2 AND DO NOTHING', line=428)

W('21,3715', 0o13630, '', 'TCF', 'J18', 'YES, GO TO J18 AND FORCE A FIRING', line=430)

W('21,3716', 0o41517, 'J24', 'CS', 'AERR', line=432)
W('21,3717', 0o00006, '', 'EXTEND', line=433)
W('21,3720', 0o61523, '', 'SU', 'ADBVEL', line=434)
W('21,3721', 0o00006, '', 'EXTEND', line=435)
W('21,3722', 0o73440, '', 'MP', 'SLOPE2', '(HYSTERESIS SLOPE)', line=436)
W('21,3723', 0o53511, '', 'DXCH', 'KMPAC', line=437)
W('21,3724', 0o00006, '', 'EXTEND', line=438)
# Page 1034
W('21,3725', 0o41516, '', 'DCS', 'EDOT', line=440)
W('21,3726', 0o21511, '', 'DAS', 'KMPAC', line=441)

# Page 1035
# COMPUTE THE JET ON TIME NECESSARY TO ACCOMPLISH THE DESIRED CHANGE IN RATE, IE
#
# T  = J/M(DELTA W)
# J
#
# DELTA W = DESIRED CHANGE IN S/C ANGULAR RATE AS DETERMINED BY THE
# SWITCHING LOGIC, AT THIS POINT STORED IN KMPAC.
#
# J/M = S/C INERTIA TO TORQUE 9ATIO SCALED BY
# (57.3/450)(B24/1600)(1/.8)
# FOR 1 JET OPERATION  (M = 700 FT-LB).
# IE  J/M = J(SLUG-FTFT) x 0.00000085601606
#
# THE CORRESPONDING COMPUTER VARIABLES ESTABLISHED BY
# KEYBOARD ENTRY ARE
# J/M (ROLL)
# J/M1 (PITCH)
# J/M2 (YAW)
#
# T  = JET-ON TIME    SCALED 16384/1600 SEC
# J
#
# THE COMPUTER VARIABLES ARE
# TAU  (ROLL)
# TAU1 (PITCH)
# TAU2 (YAW)

W('21,3727', 0o51506, 'JTIME', 'INDEX', 'SPNDX', 'PICK UP S/C INERTIA/TORQUE RATIO', line=471)
W('21,3730', 0o31623, '', 'CA', 'J/M', 'SCALED (57.3/450)(B24/1600)', line=472)
W('21,3731', 0o02042, '', 'TC', 'SMALLMP', 'FOR 1-JET OPERATION', line=473)
W('21,3732', 0o35005, '', 'CA', 'BIT11', line=474)
W('21,3733', 0o02042, '', 'TC', 'SMALLMP', line=475)
W('21,3734', 0o11510, '', 'CCS', 'KMPAC', line=476)
W('21,3735', 0o13741, '', 'TCF', '+4', line=477)
W('21,3736', 0o13745, '', 'TCF', 'TAUNORM', line=478)
W('21,3737', 0o13743, '', 'TCF', '+4', line=479)
W('21,3740', 0o13745, '', 'TCF', 'TAUNORM', line=480)
W('21,3741', 0o34777, '', 'CA', 'POSMAX', line=481)
W('21,3742', 0o13746, '', 'TCF', 'DOJET', line=482)
W('21,3743', 0o35001, '', 'CA', 'NEGMAX', line=483)
W('21,3744', 0o13746, '', 'TCF', 'DOJET', line=484)

W('21,3745', 0o31511, 'TAUNORM', 'CA', 'KMPAC +1', line=486)
W('21,3746', 0o51506, 'DOJET', 'INDEX', 'SPNDX', line=487)
W('21,3747', 0o55561, '', 'TS', 'TAU', line=488)
W('21,3750', 0o11506, '', 'CCS', 'SPNDX', line=489)
W('21,3751', 0o13445, '', 'TCF', 'JLOOP', line=490)
W('21,3752', 0o13757, '', 'TCF', 'T6PROG', line=491)

# Page 1036
W('21,3753', 0o35021, 'ZEROCMDS', 'CAF', 'ZERO', line=494)
W('21,3754', 0o55561, '', 'TS', 'TAU', line=495)
W('21,3755', 0o55562, '', 'TS', 'TAU1', line=496)
W('21,3756', 0o55563, '', 'TS', 'TAU2', line=497)
W('21,3757', 0o00006, 'T6PROG', 'EXTEND', '', 'WHEN THE ROTATION COMMANDS (TAUS)', line=498)
W('21,3760', 0o33764, '', 'DCA', 'JETADDR', 'HAVE BEEN DETERMINED', line=499)
W('21,3761', 0o53313, '', 'DXCH', 'T5LOC', 'RESET T5LOC FOR PHASE3', line=500)
W('21,3762', 0o15333, '', 'TCF', 'RESUME', line=501)

#   EBANK= KMPAC
W('21,3763', 0o02552, 'JETADDR', '2CADR', 'JETSLECT', kind='data', line=504)
W('21,3764', 0o36066, kind='data', line=504)
