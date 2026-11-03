"""MEASUREMENT_INCORPORATION.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/MEASUREMENT_INCORPORATION.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1252-1261 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('MEASUREMENT_INCORPORATION', 'MEASUREMENT_INCORPORATION.agc', 'Comanche055', pages='1252-1261')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     MEASUREMENT_INCORPORATION.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1252-1261
# Mod history:  2009-05-14 RSB  Adapted from the Colossus249/ file of the
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

# Page 1252
# INCORP1--PERFORMS THE SIX DIMENSIONAL STATE VECTOR DEVIATION FOR POSITI
# ON AND VELOCITY OR THE NINE DIMENSIONAL DEVIATION OF POSITION,VELOCITY,A
# ND RADAR OR LANDMARK BIAS.THE OUTPUT OF THE BVECTOR ROUTINE ALONG WITH T
# HE ERROR TRANSITION MATRIX(W) ARE USED AS INPUT TO THE ROUTINE.THE DEVIA
# TION IS OBTAINED BY COMPUTING AN ESTIMATED TRACKING MEASUREMENT FROM THE
# CURRENT STATE VECTOR AND COMPARING IT WITH AN ACTUAL TRACKING MEASUREMEN
# T AND APPLYING A STATISTICAL WEIGHTING VECTOR.
# INPUT
# DMENFLG = 0 6DIMENSIONAL BVECTOR  1= 9DIMENSIONAL
# W = ERROR TRANSITION MATRIX 6X6 OR 9X9
# VARIANCE = VARIANCE (SCALAR)
# DELTAQ = MEASURED DEVIATION(SCALAR)
# BVECTOR = 6 OR 9 DIMENSIONAL BVECTOR
#
# OUTPUT
# DELTAX = STATE VECTOR DEVIATIONS 6 OR 9 DIMENSIONAL
# ZI = VECTOR USED FOR THE INCORPORATION 6 OR 9 DIMENSIONAL
# GAMMA = SCALAR
# OMEGA = OMEGA WEIGHTING VECTOR 6 OR 9 DIMENSIONAL
#
# CALLING SEQUENCE
# L  CALL INCORP1
#
# NORMAL EXIT
# L+1 OF CALLING SEQUENCE

#   BANK 37
#   SETLOC MEASINC
#   BANK

#   COUNT* $$/INCOR

#   EBANK= W

W('36,3254', 0o77620, 'INCORP1', 'STQ', kind='interp', line=65)
W('36,3255', 0o02317, '', '', 'EGRESS', kind='operand', line=66)
W('36,3256', 0o66370, '', 'AXT,1', 'SSP', kind='interp', line=67)
W('36,3257', 0o00066, '', '', '54D', kind='operand', line=68)
W('36,3260', 0o00051, '', '', 'S1', kind='operand', line=69)
W('36,3261', 0o00022, '', '', '18D', 'IX1 = 54      S1= 18', kind='operand', line=70)
W('36,3262', 0o66374, '', 'AXT,2', 'SSP', kind='interp', line=71)
W('36,3263', 0o00022, '', '', '18D', kind='operand', line=72)
W('36,3264', 0o00052, '', '', 'S2', kind='operand', line=73)
W('36,3265', 0o00006, '', '', '6', 'IX2 = 18      S2=6', kind='operand', line=74)
W('36,3266', 0o63775, 'Z123', 'VLOAD', 'MXV*', kind='interp', line=75)
W('36,3267', 0o03502, '', '', 'BVECTOR', 'BVECTOR (0)', kind='operand', line=76)
W('36,3270', 0o02467, '', '', 'W +54D,1', kind='operand', line=77)
W('36,3271', 0o12745, '', 'STORE', 'ZI +18D,2', kind='interp', line=78)
W('36,3272', 0o77775, '', 'VLOAD', kind='interp', line=79)
W('36,3273', 0o03510, '', '', 'BVECTOR +6', 'BVECTOR (1)', kind='operand', line=80)
# Page 1253
W('36,3274', 0o52717, '', 'MXV*', 'VAD*', kind='interp', line=82)
W('36,3275', 0o02555, '', '', 'W +108D,1', kind='operand', line=83)
W('36,3276', 0o75032, '', '', 'ZI +18D,2', kind='operand', line=84)
W('36,3277', 0o12745, '', 'STORE', 'ZI +18D,2', kind='interp', line=85)
W('36,3300', 0o77775, '', 'VLOAD', kind='interp', line=86)
W('36,3301', 0o03516, '', '', 'BVECTOR +12D', 'BVECTOR (2)', kind='operand', line=87)
W('36,3302', 0o52717, '', 'MXV*', 'VAD*', kind='interp', line=88)
W('36,3303', 0o02643, '', '', 'W +162D,1', kind='operand', line=89)
W('36,3304', 0o75032, '', '', 'ZI +18D,2', 'B(0)*W+B(1)*(W+54)+B(2)*(W+108)FIRST PAS', kind='operand', line=90)
W('36,3305', 0o12745, '', 'STORE', 'ZI +18D,2', 'ZI THEN Z2 THEN Z3', kind='interp', line=91)
W('36,3306', 0o77700, '', 'TIX,1', kind='interp', line=92)
W('36,3307', 0o75310, '', '', 'INCOR1', kind='operand', line=93)
W('36,3310', 0o43104, 'INCOR1', 'TIX,2', 'BON', kind='interp', line=94)
W('36,3311', 0o75266, '', '', 'Z123', 'LOOP FOR Z1,Z2,Z3', kind='operand', line=95)
W('36,3312', 0o02706, '', '', 'DMENFLG', kind='operand', line=96)
W('36,3313', 0o75317, '', '', 'INCOR1A', kind='operand', line=97)
W('36,3314', 0o77775, '', 'VLOAD', kind='interp', line=98)
W('36,3315', 0o15335, '', '', 'ZEROVECS', kind='operand', line=99)
W('36,3316', 0o02737, '', 'STORE', 'ZI +12D', kind='interp', line=100)
W('36,3317', 0o77201, 'INCOR1A', 'SETPD', 'VLOAD', kind='interp', line=101)
W('36,3320', 0o00001, '', '', '0', kind='operand', line=102)
W('36,3321', 0o02723, '', '', 'ZI', kind='operand', line=103)
W('36,3322', 0o47036, '', 'VSQ', 'RTB', kind='interp', line=104)
W('36,3323', 0o45565, '', '', 'TPMODE', kind='operand', line=105)
W('36,3324', 0o47515, '', 'PDVL', 'VSQ', kind='interp', line=106)
W('36,3325', 0o02731, '', '', 'ZI +6', kind='operand', line=107)
W('36,3326', 0o76234, '', 'RTB', 'TAD', kind='interp', line=108)
W('36,3327', 0o45565, '', '', 'TPMODE', kind='operand', line=109)
W('36,3330', 0o47515, '', 'PDVL', 'VSQ', kind='interp', line=110)
W('36,3331', 0o02737, '', '', 'ZI +12D', kind='operand', line=111)
W('36,3332', 0o76234, '', 'RTB', 'TAD', kind='interp', line=112)
W('36,3333', 0o45565, '', '', 'TPMODE', kind='operand', line=113)
W('36,3334', 0o77171, '', 'TAD', 'AXT,2', kind='interp', line=114)
W('36,3335', 0o03526, '', '', 'VARIANCE', kind='operand', line=115)
W('36,3336', 0o00000, '', '', '0', kind='operand', line=116)
W('36,3337', 0o01257, '', 'STORE', 'TRIPA', 'ZI*2 + Z2*2 + Z3*2 + VARIANCE', kind='interp', line=117)
W('36,3340', 0o40151, '', 'TLOAD', 'BOV', kind='interp', line=118)
W('36,3341', 0o03526, '', '', 'VARIANCE', 'CLEAR OVFIND', kind='operand', line=119)
W('36,3342', 0o75343, '', '', '+1', kind='operand', line=120)
W('36,3343', 0o01262, '', 'STORE', 'TEMPVAR', 'TEMP STORAGE FOR VARIANCE', kind='interp', line=121)
W('36,3344', 0o77654, '', 'BZE', kind='interp', line=122)
W('36,3345', 0o75354, '', '', 'INCOR1C', kind='operand', line=123)
W('36,3346', 0o40112, 'INCOR1B', 'SL2', 'BOV', kind='interp', line=124)
W('36,3347', 0o75354, '', '', 'INCOR1C', kind='operand', line=125)
W('36,3350', 0o01262, '', 'STORE', 'TEMPVAR', kind='interp', line=126)
W('36,3351', 0o52114, '', 'INCR,2', 'GOTO', kind='interp', line=127)
W('36,3352', 0o00001, '', 'DEC', '1', kind='data', line=128)
W('36,3353', 0o75346, '', '', 'INCOR1B', kind='operand', line=129)
W('36,3354', 0o61551, 'INCOR1C', 'TLOAD', 'ROUND', kind='interp', line=130)
W('36,3355', 0o01257, '', '', 'TRIPA', kind='operand', line=131)
# Page 1254
W('36,3356', 0o75405, '', 'DMP', 'SQRT', kind='interp', line=133)
W('36,3357', 0o01262, '', '', 'TEMPVAR', kind='operand', line=134)
W('36,3360', 0o76257, '', 'SL*', 'TAD', kind='interp', line=135)
W('36,3361', 0o57576, '', '', '0,2', kind='operand', line=136)
W('36,3362', 0o01257, '', '', 'TRIPA', kind='operand', line=137)
W('36,3363', 0o63101, '', 'NORM', 'INCR,2', kind='interp', line=138)
W('36,3364', 0o00050, '', '', 'X2', kind='operand', line=139)
W('36,3365', 0o77775, '', 'DEC', '-2', kind='data', line=140)
W('36,3366', 0o77134, '', 'SXA,2', 'AXT,2', kind='interp', line=141)
W('36,3367', 0o02215, '', '', 'NORMGAM', 'NORMALIZATION COUNT -2 FOR GAMMA', kind='operand', line=142)
W('36,3370', 0o00242, '', '', '162D', kind='operand', line=143)
W('36,3371', 0o40265, '', 'BDDV', 'SETPD', kind='interp', line=144)
W('36,3372', 0o15325, '', '', 'DP1/4TH', kind='operand', line=145)
W('36,3373', 0o00001, '', '', '0', kind='operand', line=146)
W('36,3374', 0o03456, '', 'STORE', 'GAMMA', kind='interp', line=147)
W('36,3375', 0o60351, '', 'TLOAD', 'NORM', kind='interp', line=148)
W('36,3376', 0o01257, '', '', 'TRIPA', kind='operand', line=149)
W('36,3377', 0o00047, '', '', 'X1', kind='operand', line=150)
W('36,3400', 0o65345, '', 'DLOAD', 'PDDL', 'PD 0-1 = NORM (A)', kind='interp', line=151)
W('36,3401', 0o00155, '', '', 'MPAC', kind='operand', line=152)
W('36,3402', 0o03524, '', '', 'DELTAQ', kind='operand', line=153)
W('36,3403', 0o77701, '', 'NORM', kind='interp', line=154)
W('36,3404', 0o00051, '', '', 'S1', kind='operand', line=155)
W('36,3405', 0o70460, '', 'XSU,1', 'SR1', kind='interp', line=156)
W('36,3406', 0o00050, '', '', 'S1', kind='operand', line=157)
W('36,3407', 0o41471, '', 'DDV', 'PUSH', 'PD 0-1 = DELTAQ/A', kind='interp', line=158)
W('36,3410', 0o77650, '', 'GOTO', kind='interp', line=159)
W('36,3411', 0o31377, '', '', 'NEWZCOMP', kind='operand', line=160)
W('36,3412', 0o77731, '', 'SSP', kind='interp', line=161)
W('36,3413', 0o00052, '', '', 'S2', kind='operand', line=162)
W('36,3414', 0o00066, '', '', '54D', kind='operand', line=163)
W('36,3415', 0o60775, 'INCOR2', 'VLOAD', 'VXM*', 'COMPUT OMEGA1,2,3', kind='interp', line=164)
W('36,3416', 0o02723, '', '', 'ZI', kind='operand', line=165)
W('36,3417', 0o75134, '', '', 'W +162D,2', kind='operand', line=166)
W('36,3420', 0o77206, '', 'PUSH', 'VLOAD', kind='interp', line=167)
W('36,3421', 0o02731, '', '', 'ZI +6', kind='operand', line=168)
W('36,3422', 0o53303, '', 'VXM*', 'VAD', kind='interp', line=169)
W('36,3423', 0o75112, '', '', 'W +180D,2', kind='operand', line=170)
W('36,3424', 0o77206, '', 'PUSH', 'VLOAD', kind='interp', line=171)
W('36,3425', 0o02737, '', '', 'ZI +12D', kind='operand', line=172)
W('36,3426', 0o53303, '', 'VXM*', 'VAD', kind='interp', line=173)
W('36,3427', 0o75070, '', '', 'W +198D,2', kind='operand', line=174)
W('36,3430', 0o61006, '', 'PUSH', 'TIX,2', 'PD 2-7=OMEGA1,8-13=OMEGA2,14-19=OMEGA3', kind='interp', line=175)
W('36,3431', 0o75415, '', '', 'INCOR2', kind='operand', line=176)
W('36,3432', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=177)
W('36,3433', 0o74303, '', 'STORE', 'OMEGA +12D', kind='interp', line=178)
W('36,3434', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=179)
W('36,3435', 0o74311, '', 'STORE', 'OMEGA +6', kind='interp', line=180)
W('36,3436', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=181)
W('36,3437', 0o74317, '', 'STORE', 'OMEGA', kind='interp', line=182)
# Page 1255
W('36,3440', 0o77214, '', 'BON', 'VLOAD', kind='interp', line=184)
W('36,3441', 0o02706, '', '', 'DMENFLG', kind='operand', line=185)
W('36,3442', 0o75445, '', '', 'INCOR2AB', kind='operand', line=186)
W('36,3443', 0o15335, '', '', 'ZEROVECS', kind='operand', line=187)
W('36,3444', 0o03474, '', 'STORE', 'OMEGA +12D', kind='interp', line=188)
W('36,3445', 0o66374, 'INCOR2AB', 'AXT,2', 'SSP', kind='interp', line=189)
W('36,3446', 0o00022, '', '', '18D', kind='operand', line=190)
W('36,3447', 0o00052, '', '', 'S2', kind='operand', line=191)
W('36,3450', 0o00006, '', '', '6', kind='operand', line=192)
W('36,3451', 0o77773, 'INCOR3', 'VLOAD*', kind='interp', line=193)
W('36,3452', 0o74275, '', '', 'OMEGA +18D,2', kind='operand', line=194)
W('36,3453', 0o53761, '', 'VXSC', 'VSL*', kind='interp', line=195)
W('36,3454', 0o00001, '', '', '0', 'DELTAQ/A', kind='operand', line=196)
W('36,3455', 0o20201, '', '', '0,1', kind='operand', line=197)
W('36,3456', 0o11301, '', 'STORE', 'DELTAX +18D,2', kind='interp', line=198)
W('36,3457', 0o77304, '', 'TIX,2', 'VLOAD', kind='interp', line=199)
W('36,3460', 0o75451, '', '', 'INCOR3', kind='operand', line=200)
W('36,3461', 0o01265, '', '', 'DELTAX +6', kind='operand', line=201)
W('36,3462', 0o77732, '', 'VSL3', kind='interp', line=202)
W('36,3463', 0o01265, '', 'STORE', 'DELTAX +6', kind='interp', line=203)
W('36,3464', 0o77650, '', 'GOTO', kind='interp', line=204)
W('36,3465', 0o02317, '', '', 'EGRESS', kind='operand', line=205)

# Page 1256
# INCORP2 -INCORPORATES THE COMPUTED STATE VECTOR DEVIATIONS INTO THE
# ESTIMATED STATE VECTOR. THE STATE VECTOR UPDATED MAY BE FOR EITHER THE
# LEM OR THE CSM.DETERMINED BY FLAG VEHUPFLG.(ZERO = LEM) (1 = CSM)
# INPUT
# PERMANENT STATE VECTOR FOR EITHER THE LEM OR CSM
# VEHUPFLG = UPDATE VEHICLE C=LEM  1=CSM
# W =        ERROR TRANSITION MATRIX
# DELTAX  =  COMPUTED STATE VECTOR DEVIATIONS
# DMENFLG =  SIZE OF W MATRIX (ZERO=6X6) (1=9X9)
# GAMMA   =  SCALAR FOR INCORPORATION
# ZI      =  VECTOR USED IN INCORPORATION
# OMEGA   =  WEIGHTING VECTOR
#
# OUTPUT
# UPDATED PERMANENT STATE VECTOR
#
# CALLING SEQUENCE
# L   CALL INCORP2
#
# NORMAL EXIT
# L+1 OF CALLING SEQUENCE
#

#   SETLOC MEASINC1
#   BANK

#   COUNT* $$/INCOR

W('36,3466', 0o45020, 'INCORP2', 'STQ', 'CALL', kind='interp', line=236)
W('36,3467', 0o02317, '', '', 'EGRESS', kind='operand', line=237)
W('36,3470', 0o27442, '', '', 'INTSTALL', kind='operand', line=238)
W('36,3471', 0o74375, '', 'VLOAD', 'VXSC', 'CALC. GAMMA * OMEGA1,2,3', kind='interp', line=239)
W('36,3472', 0o03460, '', '', 'OMEGA', kind='operand', line=240)
W('36,3473', 0o03456, '', '', 'GAMMA', kind='operand', line=241)
W('36,3474', 0o26643, '', 'STOVL', 'OMEGAM1', kind='interp', line=242)
W('36,3475', 0o03466, '', '', 'OMEGA +6', kind='operand', line=243)
W('36,3476', 0o77761, '', 'VXSC', kind='interp', line=244)
W('36,3477', 0o03456, '', '', 'GAMMA', kind='operand', line=245)
W('36,3500', 0o26651, '', 'STOVL', 'OMEGAM2', kind='interp', line=246)
W('36,3501', 0o03474, '', '', 'OMEGA +12D', kind='operand', line=247)
W('36,3502', 0o77761, '', 'VXSC', kind='interp', line=248)
W('36,3503', 0o03456, '', '', 'GAMMA', kind='operand', line=249)
W('36,3504', 0o02657, '', 'STORE', 'OMEGAM3', kind='interp', line=250)
W('36,3505', 0o77776, '', 'EXIT', kind='interp', line=251)
W('36,3506', 0o33767, '', 'CAF', '54DD', 'INITIAL IX 1 SETTING FOR W MATRIX', line=252)
W('36,3507', 0o55252, '', 'TS', 'WIXA', line=253)
W('36,3510', 0o55253, '', 'TS', 'WIXB', line=254)
W('36,3511', 0o35021, '', 'CAF', 'ZERO', line=255)
W('36,3512', 0o55254, '', 'TS', 'ZIXA', 'INITIAL IX 2 SETTING FOR Z COMPONENT', line=256)
W('36,3513', 0o55255, '', 'TS', 'ZIXB', line=257)
W('36,3514', 0o05412, 'FAZA', 'TC', 'PHASCHNG', line=258)
# Page 1257
W('36,3515', 0o04022, '', 'OCT', '04022', kind='data', line=260)
W('36,3516', 0o05546, '', 'TC', 'UPFLAG', line=261)
W('36,3517', 0o00236, '', 'ADRES', 'REINTFLG', kind='data', line=262)
W('36,3520', 0o31253, 'FAZA1', 'CA', 'WIXB', 'START FIRST PHASE OF INCORP2', line=263)
W('36,3521', 0o55252, '', 'TS', 'WIXA', ' TO UPDATE 6 OR 9 DIM. W MATRIX IN TEMP', line=264)
W('36,3522', 0o31255, '', 'CA', 'ZIXB', line=265)
W('36,3523', 0o55254, '', 'TS', 'ZIXA', line=266)
W('36,3524', 0o06006, '', 'TC', 'INTPRET', line=267)
W('36,3525', 0o73150, '', 'LXA,1', 'LXA,2', kind='interp', line=268)
W('36,3526', 0o01252, '', '', 'WIXA', kind='operand', line=269)
W('36,3527', 0o01254, '', '', 'ZIXA', kind='operand', line=270)
W('36,3530', 0o70731, '', 'SSP', 'DLOAD*', kind='interp', line=271)
W('36,3531', 0o00051, '', '', 'S1', kind='operand', line=272)
W('36,3532', 0o00006, '', '', '6', kind='operand', line=273)
W('36,3533', 0o75054, '', '', 'ZI,2', kind='operand', line=274)
W('36,3534', 0o60276, '', 'DCOMP', 'NORM', 'CALC UPPER 3X9 PARTITION OF W MATRIX', kind='interp', line=275)
W('36,3535', 0o00052, '', '', 'S2', kind='operand', line=276)
W('36,3536', 0o65161, '', 'VXSC', 'XCHX,2', kind='interp', line=277)
W('36,3537', 0o02643, '', '', 'OMEGAM1', kind='operand', line=278)
W('36,3540', 0o00051, '', '', 'S2', kind='operand', line=279)
W('36,3541', 0o57144, '', 'LXC,2', 'XAD,2', kind='interp', line=280)
W('36,3542', 0o00047, '', '', 'X2', kind='operand', line=281)
W('36,3543', 0o02215, '', '', 'NORMGAM', kind='operand', line=282)
W('36,3544', 0o65057, '', 'VSL*', 'XCHX,2', kind='interp', line=283)
W('36,3545', 0o57576, '', '', '0,2', kind='operand', line=284)
W('36,3546', 0o00051, '', '', 'S2', kind='operand', line=285)
W('36,3547', 0o77653, '', 'VAD*', kind='interp', line=286)
W('36,3550', 0o02467, '', '', 'W +54D,1', kind='operand', line=287)
W('36,3551', 0o02665, '', 'STORE', 'HOLDW', kind='interp', line=288)
W('36,3552', 0o57543, '', 'DLOAD*', 'DCOMP', 'CALC MIDDLE 3X9 PARTITION OF W MATRIX', kind='interp', line=289)
W('36,3553', 0o75054, '', '', 'ZI,2', kind='operand', line=290)
W('36,3554', 0o74301, '', 'NORM', 'VXSC', kind='interp', line=291)
W('36,3555', 0o00052, '', '', 'S2', kind='operand', line=292)
W('36,3556', 0o02651, '', '', 'OMEGAM2', kind='operand', line=293)
W('36,3557', 0o71124, '', 'XCHX,2', 'LXC,2', kind='interp', line=294)
W('36,3560', 0o00051, '', '', 'S2', kind='operand', line=295)
W('36,3561', 0o00047, '', '', 'X2', kind='operand', line=296)
W('36,3562', 0o53674, '', 'XAD,2', 'VSL*', kind='interp', line=297)
W('36,3563', 0o02215, '', '', 'NORMGAM', kind='operand', line=298)
W('36,3564', 0o57576, '', '', '0,2', kind='operand', line=299)
W('36,3565', 0o52724, '', 'XCHX,2', 'VAD*', kind='interp', line=300)
W('36,3566', 0o00051, '', '', 'S2', kind='operand', line=301)
W('36,3567', 0o02555, '', '', 'W +108D,1', kind='operand', line=302)
W('36,3570', 0o02673, '', 'STORE', 'HOLDW +6', kind='interp', line=303)
W('36,3571', 0o77614, '', 'BOFF', kind='interp', line=304)
W('36,3572', 0o02746, '', '', 'DMENFLG', 'BRANCH IF 6 DIMENSIONAL', kind='operand', line=305)
W('36,3573', 0o75613, '', '', 'FAZB', kind='operand', line=306)
W('36,3574', 0o57543, '', 'DLOAD*', 'DCOMP', 'CALC LOWER 3X9 PARTITION OF W MATRIX', kind='interp', line=307)
W('36,3575', 0o75054, '', '', 'ZI,2', kind='operand', line=308)
W('36,3576', 0o74301, '', 'NORM', 'VXSC', kind='interp', line=309)
# Page 1258
W('36,3577', 0o00052, '', '', 'S2', kind='operand', line=311)
W('36,3600', 0o02657, '', '', 'OMEGAM3', kind='operand', line=312)
W('36,3601', 0o71124, '', 'XCHX,2', 'LXC,2', kind='interp', line=313)
W('36,3602', 0o00051, '', '', 'S2', kind='operand', line=314)
W('36,3603', 0o00047, '', '', 'X2', kind='operand', line=315)
W('36,3604', 0o53674, '', 'XAD,2', 'VSL*', kind='interp', line=316)
W('36,3605', 0o02215, '', '', 'NORMGAM', kind='operand', line=317)
W('36,3606', 0o57576, '', '', '0,2', kind='operand', line=318)
W('36,3607', 0o52724, '', 'XCHX,2', 'VAD*', kind='interp', line=319)
W('36,3610', 0o00051, '', '', 'S2', kind='operand', line=320)
W('36,3611', 0o02643, '', '', 'W +162D,1', kind='operand', line=321)
W('36,3612', 0o02701, '', 'STORE', 'HOLDW +12D', kind='interp', line=322)
W('36,3613', 0o77624, 'FAZB', 'CALL', kind='interp', line=323)
W('36,3614', 0o56750, '', '', 'GRP2PC', kind='operand', line=324)
W('36,3615', 0o77776, '', 'EXIT', kind='interp', line=325)
W('36,3616', 0o31252, 'FAZB1', 'CA', 'WIXA', 'START 2ND PHASE OF INCORP2 TO TRANSFER', line=326)
W('36,3617', 0o63770, '', 'AD', '6DD', '    TEMP REG TO PERM W MATRIX', line=327)
W('36,3620', 0o55253, '', 'TS', 'WIXB', line=328)
W('36,3621', 0o31254, '', 'CA', 'ZIXA', line=329)
W('36,3622', 0o67715, '', 'AD', 'MINUS2', line=330)
W('36,3623', 0o55255, '', 'TS', 'ZIXB', line=331)
W('36,3624', 0o06006, '', 'TC', 'INTPRET', line=332)
W('36,3625', 0o66350, '', 'LXA,1', 'SSP', kind='interp', line=333)
W('36,3626', 0o01252, '', '', 'WIXA', kind='operand', line=334)
W('36,3627', 0o00051, '', '', 'S1', kind='operand', line=335)
W('36,3630', 0o00006, '', '', '6', kind='operand', line=336)
W('36,3631', 0o77775, '', 'VLOAD', kind='interp', line=337)
W('36,3632', 0o02665, '', '', 'HOLDW', kind='operand', line=338)
W('36,3633', 0o06467, '', 'STORE', 'W +54D,1', kind='interp', line=339)
W('36,3634', 0o77775, '', 'VLOAD', kind='interp', line=340)
W('36,3635', 0o02673, '', '', 'HOLDW +6', kind='operand', line=341)
W('36,3636', 0o06555, '', 'STORE', 'W +108D,1', kind='interp', line=342)
W('36,3637', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=343)
W('36,3640', 0o02746, '', '', 'DMENFLG', kind='operand', line=344)
W('36,3641', 0o75651, '', '', 'FAZB5', kind='operand', line=345)
W('36,3642', 0o02701, '', '', 'HOLDW +12D', kind='operand', line=346)
W('36,3643', 0o06643, '', 'STORE', 'W +162D,1', kind='interp', line=347)
W('36,3644', 0o52100, 'FAZB2', 'TIX,1', 'GOTO', kind='interp', line=348)
W('36,3645', 0o75647, '', '', '+2', kind='operand', line=349)
W('36,3646', 0o75657, '', '', 'FAZC', 'DONE WITH W MATRIX. UPDATE STATE VECTOR', kind='operand', line=350)
W('36,3647', 0o77634, '', 'RTB', kind='interp', line=351)
W('36,3650', 0o75514, '', '', 'FAZA', kind='operand', line=352)
W('36,3651', 0o43335, 'FAZB5', 'SLOAD', 'DAD', kind='interp', line=353)
W('36,3652', 0o01256, '', '', 'ZIXB', kind='operand', line=354)
W('36,3653', 0o35772, '', '', '12DD', kind='operand', line=355)
W('36,3654', 0o52030, '', 'BHIZ', 'GOTO', kind='interp', line=356)
W('36,3655', 0o75657, '', '', 'FAZC', kind='operand', line=357)
W('36,3656', 0o75644, '', '', 'FAZB2', kind='operand', line=358)
W('36,3657', 0o77624, 'FAZC', 'CALL', kind='interp', line=359)
W('36,3660', 0o56750, '', '', 'GRP2PC', kind='operand', line=360)
# Page 1259
W('36,3661', 0o53375, '', 'VLOAD', 'VAD', 'START 3RD PHASE OF INCORP2', kind='interp', line=362)
W('36,3662', 0o01701, '', '', 'X789', '7TH,8TH,9TH,COMPONENT OF STATE VECTOR', kind='operand', line=363)
W('36,3663', 0o01273, '', '', 'DELTAX +12D', 'INCORPORATION FOR X789', kind='operand', line=364)
W('36,3664', 0o03450, '', 'STORE', 'TX789', kind='interp', line=365)
W('36,3665', 0o47014, '', 'BON', 'RTB', kind='interp', line=366)
W('36,3666', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=367)
W('36,3667', 0o75757, '', '', 'DOCSM', kind='operand', line=368)
W('36,3670', 0o27014, '', '', 'MOVEPLEM', kind='operand', line=369)
W('36,3671', 0o77004, 'FAZAB', 'BOVB', 'AXT,2', kind='interp', line=370)
W('36,3672', 0o57352, '', '', 'TCDANZIG', kind='operand', line=371)
W('36,3673', 0o00000, '', '', '0', kind='operand', line=372)
W('36,3674', 0o77014, '', 'BOFF', 'AXT,2', kind='interp', line=373)
W('36,3675', 0o04343, '', '', 'MOONTHIS', kind='operand', line=374)
W('36,3676', 0o75700, '', '', '+2', kind='operand', line=375)
W('36,3677', 0o00002, '', '', '2', kind='operand', line=376)
W('36,3700', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=377)
W('36,3701', 0o01257, '', '', 'DELTAX', 'B27 IF MOON ORBIT, B29 IF EARTH', kind='operand', line=378)
W('36,3702', 0o57205, '', '', '0 -7,2', kind='operand', line=379)
W('36,3703', 0o40055, '', 'VAD', 'BOV', kind='interp', line=380)
W('36,3704', 0o01521, '', '', 'TDELTAV', kind='operand', line=381)
W('36,3705', 0o75717, '', '', 'FAZAB1', kind='operand', line=382)
W('36,3706', 0o25521, '', 'STOVL', 'TDELTAV', kind='interp', line=383)
W('36,3707', 0o01265, '', '', 'DELTAX +6', 'B5 IF MOON ORBIT, B7 IF EARTH', kind='operand', line=384)
W('36,3710', 0o53257, '', 'VSR*', 'VAD', kind='interp', line=385)
W('36,3711', 0o57202, '', '', '0 -4,2', kind='operand', line=386)
W('36,3712', 0o01527, '', '', 'TNUV', kind='operand', line=387)
W('36,3713', 0o77600, '', 'BOV', kind='interp', line=388)
W('36,3714', 0o75723, '', '', 'FAZAB2', kind='operand', line=389)
W('36,3715', 0o35527, '', 'STCALL', 'TNUV', kind='interp', line=390)
W('36,3716', 0o75732, '', '', 'FAZAB3', kind='operand', line=391)
W('36,3717', 0o53375, 'FAZAB1', 'VLOAD', 'VAD', kind='interp', line=392)
W('36,3720', 0o01535, '', '', 'RCV', kind='operand', line=393)
W('36,3721', 0o01257, '', '', 'DELTAX', kind='operand', line=394)
W('36,3722', 0o01535, '', 'STORE', 'RCV', kind='interp', line=395)
W('36,3723', 0o53375, 'FAZAB2', 'VLOAD', 'VAD', kind='interp', line=396)
W('36,3724', 0o01543, '', '', 'VCV', kind='operand', line=397)
W('36,3725', 0o01265, '', '', 'DELTAX +6', kind='operand', line=398)
W('36,3726', 0o01543, '', 'STORE', 'VCV', kind='interp', line=399)
W('36,3727', 0o45134, '', 'SXA,2', 'CALL', kind='interp', line=400)
W('36,3730', 0o02150, '', '', 'PBODY', kind='operand', line=401)
W('36,3731', 0o23421, '', '', 'RECTIFY', kind='operand', line=402)
W('36,3732', 0o77624, 'FAZAB3', 'CALL', kind='interp', line=403)
W('36,3733', 0o56750, '', '', 'GRP2PC', kind='operand', line=404)
W('36,3734', 0o47014, '', 'BON', 'RTB', kind='interp', line=405)
W('36,3735', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=406)
W('36,3736', 0o75762, '', '', 'DOCSM1', kind='operand', line=407)
W('36,3737', 0o26773, '', '', 'MOVEALEM', kind='operand', line=408)
W('36,3740', 0o77624, '', 'CALL', kind='interp', line=409)
W('36,3741', 0o20263, '', '', 'SVDWN2', 'STORE DOWNLINK STATE VECTOR', kind='operand', line=410)
W('36,3742', 0o77624, 'FAZAB4', 'CALL', kind='interp', line=411)
# Page 1260
W('36,3743', 0o56750, '', '', 'GRP2PC', 'PHASE CHANGE', kind='operand', line=413)
W('36,3744', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=414)
W('36,3745', 0o02746, '', '', 'DMENFLG', kind='operand', line=415)
W('36,3746', 0o75751, '', '', 'FAZAB5', '6 DIMENSIONAL', kind='operand', line=416)
W('36,3747', 0o03450, '', '', 'TX789', '9 DIMENSIONAL', kind='operand', line=417)
W('36,3750', 0o01701, '', 'STORE', 'X789', kind='interp', line=418)
W('36,3751', 0o66150, 'FAZAB5', 'LXA,1', 'SXA,1', kind='interp', line=419)
W('36,3752', 0o02317, '', '', 'EGRESS', kind='operand', line=420)
W('36,3753', 0o00052, '', '', 'QPRET', kind='operand', line=421)
W('36,3754', 0o77776, '', 'EXIT', kind='interp', line=422)
W('36,3755', 0o04701, '', 'TC', 'POSTJUMP', 'EXIT', line=423)
W('36,3756', 0o27457, '', 'CADR', 'INTWAKE', kind='data', line=424)
W('36,3757', 0o52034, 'DOCSM', 'RTB', 'GOTO', kind='interp', line=425)
W('36,3760', 0o26747, '', '', 'MOVEPCSM', kind='operand', line=426)
W('36,3761', 0o75671, '', '', 'FAZAB', kind='operand', line=427)
W('36,3762', 0o45034, 'DOCSM1', 'RTB', 'CALL', kind='interp', line=428)
W('36,3763', 0o26720, '', '', 'MOVEACSM', kind='operand', line=429)
W('36,3764', 0o20237, '', '', 'SVDWN1', 'STORE DOWNLINK STATE VECTOR', kind='operand', line=430)
W('36,3765', 0o77650, '', 'GOTO', kind='interp', line=431)
W('36,3766', 0o75742, '', '', 'FAZAB4', kind='operand', line=432)
S('ZEROD', 'equals', 0o65334, line=433)
W('36,3767', 0o00066, '54DD', 'DEC', '54', kind='data', line=434)
W('36,3770', 0o77771, '6DD', 'DEC', '-6', kind='data', line=435)
W('36,3771', 0o00014, '12DD', 'DEC', '12', kind='data', line=436)
#   SETLOC MEASINC2
#   BANK
#   COUNT* $$/INCOR

W('14,3377', 0o51575, 'NEWZCOMP', 'VLOAD', 'ABVAL', kind='interp', line=441)
W('14,3400', 0o02723, '', '', 'ZI', kind='operand', line=442)
W('14,3401', 0o24045, '', 'STOVL', 'NORMZI', kind='interp', line=443)
W('14,3402', 0o02731, '', '', 'ZI +6', kind='operand', line=444)
W('14,3403', 0o41446, '', 'ABVAL', 'PUSH', kind='interp', line=445)
W('14,3404', 0o50025, '', 'DSU', 'BMN', kind='interp', line=446)
W('14,3405', 0o00045, '', '', 'NORMZI', kind='operand', line=447)
W('14,3406', 0o31411, '', '', '+3', kind='operand', line=448)
W('14,3407', 0o45545, '', 'DLOAD', 'STADR', kind='interp', line=449)
W('14,3410', 0o77732, '', 'STORE', 'NORMZI', kind='interp', line=450)
W('14,3411', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=451)
W('14,3412', 0o02737, '', '', 'ZI +12D', kind='operand', line=452)
W('14,3413', 0o45206, '', 'PUSH', 'DSU', kind='interp', line=453)
W('14,3414', 0o00045, '', '', 'NORMZI', kind='operand', line=454)
W('14,3415', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=455)
W('14,3416', 0o73635, '', '', 'NEWZCMP1', kind='operand', line=456)
W('14,3417', 0o77626, '', 'STADR', kind='interp', line=457)
W('14,3420', 0o43732, '', 'STCALL', 'NORMZI', 'LARGEST ABVAL', kind='interp', line=458)
W('14,3421', 0o73635, '', '', 'NEWZCMP1', kind='operand', line=459)

#   SETLOC MEASINC3
#   BANK
# Page 1261
W('35,3635', 0o66145, 'NEWZCMP1', 'DLOAD', 'SXA,1', kind='interp', line=464)
W('35,3636', 0o00045, '', '', 'NORMZI', kind='operand', line=465)
W('35,3637', 0o00044, '', '', 'NORMZI', 'SAVE X1', kind='operand', line=466)
W('35,3640', 0o62101, '', 'NORM', 'INCR,1', kind='interp', line=467)
W('35,3641', 0o00047, '', '', 'X1', kind='operand', line=468)
W('35,3642', 0o00002, '', 'DEC', '2', kind='data', line=469)
W('35,3643', 0o53775, '', 'VLOAD', 'VSL*', kind='interp', line=470)
W('35,3644', 0o02723, '', '', 'ZI', kind='operand', line=471)
W('35,3645', 0o20201, '', '', '0,1', kind='operand', line=472)
W('35,3646', 0o26723, '', 'STOVL', 'ZI', kind='interp', line=473)
W('35,3647', 0o02731, '', '', 'ZI +6', kind='operand', line=474)
W('35,3650', 0o77657, '', 'VSL*', kind='interp', line=475)
W('35,3651', 0o20201, '', '', '0,1', kind='operand', line=476)
W('35,3652', 0o26731, '', 'STOVL', 'ZI +6', kind='interp', line=477)
W('35,3653', 0o02737, '', '', 'ZI +12D', kind='operand', line=478)
W('35,3654', 0o66057, '', 'VSL*', 'SXA,1', kind='interp', line=479)
W('35,3655', 0o20201, '', '', '0,1', kind='operand', line=480)
W('35,3656', 0o00045, '', '', 'NORMZI +1', 'SAVE SHIFT', kind='operand', line=481)
W('35,3657', 0o02737, '', 'STORE', 'ZI +12D', kind='interp', line=482)
W('35,3660', 0o54150, '', 'LXA,1', 'XSU,1', kind='interp', line=483)
W('35,3661', 0o02215, '', '', 'NORMGAM', kind='operand', line=484)
W('35,3662', 0o00045, '', '', 'NORMZI +1', kind='operand', line=485)
W('35,3663', 0o77660, '', 'XSU,1', kind='interp', line=486)
W('35,3664', 0o00045, '', '', 'NORMZI +1', kind='operand', line=487)
W('35,3665', 0o70130, '', 'SXA,1', 'LXC,1', kind='interp', line=488)
W('35,3666', 0o02215, '', '', 'NORMGAM', kind='operand', line=489)
W('35,3667', 0o00045, '', '', 'NORMZI +1', kind='operand', line=490)
W('35,3670', 0o40270, '', 'XAD,1', 'SETPD', kind='interp', line=491)
W('35,3671', 0o00044, '', '', 'NORMZI', kind='operand', line=492)
W('35,3672', 0o00003, '', '', '2D', kind='operand', line=493)
W('35,3673', 0o77650, '', 'GOTO', kind='interp', line=494)
W('35,3674', 0o75412, '', '', 'INCOR2 -3', kind='operand', line=495)
S('NORMZI', 'equals', 0o44, line=496)
