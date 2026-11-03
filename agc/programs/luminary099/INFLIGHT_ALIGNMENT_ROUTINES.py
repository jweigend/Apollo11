"""INFLIGHT_ALIGNMENT_ROUTINES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/INFLIGHT_ALIGNMENT_ROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1249-1258 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INFLIGHT_ALIGNMENT_ROUTINES', 'INFLIGHT_ALIGNMENT_ROUTINES.agc', 'Luminary099', pages='1249-1258')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INFLIGHT_ALIGNMENT_ROUTINES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1249-1258
# Mod history:  2009-05-26 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
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

# Page 1249
#   BANK 22
#   SETLOC INFLIGHT
#   BANK

#   EBANK= XSM

# CALCGTA COMPUTES THE GYRO TORQUE ANGLES REQUIRED TO BRING THE STABLE MEMBER INTO THE DESIRED ORIENTATION.
#
# THE INPUT IS THE DESIRED STABLE MEMBER COORDINATES REFERRED TO PRESENT STABLE MEMBER COORDINATES.  THE THREE
# HALF-UNIT VECTORS ARE STORED AT XDC, YDC, AND ZDC.
#
# THE OUTPUTS ARE THE THREE GYRO TORQUE ANGLES TO BE APPLIED TO THE Y, Z, AND X GYROS AND ARE STORED DP AT IGC,
# MGC, AND OGC RESPECTIVELY.

#   COUNT* $$/INFLT
W('23,3247', 0o71220, 'CALCGTA', 'ITA', 'DLOAD', 'PUSHDOWN 00-03, 16D-27D, 34D-37D', kind='interp', line=45)
W('23,3250', 0o00051, '', '', 'S2', 'XDC = (XD1 XD2 XD3)', kind='operand', line=46)
W('23,3251', 0o02665, '', '', 'XDC', 'YDC = (YD1 YD2 YD3)', kind='operand', line=47)
W('23,3252', 0o65325, '', 'PDDL', 'PDDL', 'ZDC = (ZD1 ZD2 ZD3)', kind='interp', line=48)
W('23,3253', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=49)
W('23,3254', 0o02671, '', '', 'XDC +4', kind='operand', line=50)
W('23,3255', 0o55476, '', 'DCOMP', 'VDEF', kind='interp', line=51)
W('23,3256', 0o77656, '', 'UNIT', kind='interp', line=52)
W('23,3257', 0o14027, '', 'STODL', 'ZPRIME', 'ZP = UNIT(-XD3 0 XD1) = (ZP1 ZP2 ZP3)', kind='interp', line=53)
W('23,3260', 0o00027, '', '', 'ZPRIME', kind='operand', line=54)

W('23,3261', 0o77742, '', 'SR1', kind='interp', line=56)
W('23,3262', 0o14023, '', 'STODL', 'SINTH', 'SIN(IGC) = ZP1', kind='interp', line=57)
W('23,3263', 0o00033, '', '', 'ZPRIME +4', kind='operand', line=58)
W('23,3264', 0o77742, '', 'SR1', kind='interp', line=59)
W('23,3265', 0o34021, '', 'STCALL', 'COSTH', 'COS(IGC) = ZP3', kind='interp', line=60)
W('23,3266', 0o47320, '', '', 'ARCTRIG', kind='operand', line=61)

W('23,3267', 0o16742, '', 'STODL', 'IGC', 'Y GYRO TORQUING ANGLE   FRACTION OF REV.', kind='interp', line=63)
W('23,3270', 0o02667, '', '', 'XDC +2', kind='operand', line=64)
W('23,3271', 0o77742, '', 'SR1', kind='interp', line=65)
W('23,3272', 0o14023, '', 'STODL', 'SINTH', 'SIN(MGC) = XD2', kind='interp', line=66)
W('23,3273', 0o00027, '', '', 'ZPRIME', kind='operand', line=67)

W('23,3274', 0o65205, '', 'DMP', 'PDDL', kind='interp', line=69)
W('23,3275', 0o02671, '', '', 'XDC +4', 'PD00 = (ZP1)(XD3)', kind='operand', line=70)
W('23,3276', 0o00033, '', '', 'ZPRIME +4', kind='operand', line=71)

W('23,3277', 0o45205, '', 'DMP', 'DSU', kind='interp', line=73)
W('23,3300', 0o02665, '', '', 'XDC', 'MPAC = (ZP3)(XD1)', kind='operand', line=74)
W('23,3301', 0o77626, '', 'STADR', kind='interp', line=75)
W('23,3302', 0o43756, '', 'STCALL', 'COSTH', 'COS(MGC) = MPAC - PD00', kind='interp', line=76)
W('23,3303', 0o47320, '', '', 'ARCTRIG', kind='operand', line=77)
# Page 1250
W('23,3304', 0o26744, '', 'STOVL', 'MGC', 'Z GYRO TORQUING ANGLE   FRACTION OF REV.', kind='interp', line=79)
W('23,3305', 0o00027, '', '', 'ZPRIME', kind='operand', line=80)
W('23,3306', 0o77641, '', 'DOT', kind='interp', line=81)
W('23,3307', 0o02701, '', '', 'ZDC', kind='operand', line=82)
W('23,3310', 0o24021, '', 'STOVL', 'COSTH', 'COS(OGC) = ZP . ZDC', kind='interp', line=83)
W('23,3311', 0o00027, '', '', 'ZPRIME', kind='operand', line=84)
W('23,3312', 0o77641, '', 'DOT', kind='interp', line=85)
W('23,3313', 0o02673, '', '', 'YDC', kind='operand', line=86)
W('23,3314', 0o34023, '', 'STCALL', 'SINTH', 'SIN(OGC) = ZP . YDC', kind='interp', line=87)
W('23,3315', 0o47320, '', '', 'ARCTRIG', kind='operand', line=88)

W('23,3316', 0o36740, '', 'STCALL', 'OGC', 'X GYRO TORQUING ANGLE   FRACTION OF REV.', kind='interp', line=90)
W('23,3317', 0o00051, '', '', 'S2', kind='operand', line=91)

# Page 1251
# ARCTRIG COMPUTES AN ANGLE GIVEN THE SINE AND COSINE OF THIS ANGLE.
#
# THE INPUTS ARE SIN/4 AND COS/4 STORED DP AT SINTH AND COSTH.
#
# THE OUTPUT IS THE CALCULATED ANGLE BETWEEN +.5 AND -.5 REVOLUTIONS AND STORED AT THETA.  THE OUTPUT IS ALSO
# AVAILABLE AT MPAC.

W('23,3320', 0o51545, 'ARCTRIG', 'DLOAD', 'ABS', 'PUSHDOWN  16D-21D', kind='interp', line=101)
W('23,3321', 0o00023, '', '', 'SINTH', kind='operand', line=102)
W('23,3322', 0o50025, '', 'DSU', 'BMN', kind='interp', line=103)
W('23,3323', 0o07534, '', '', 'QTSN45', 'ABS(SIN/4) - SIN(45)/4', kind='operand', line=104)
W('23,3324', 0o47333, '', '', 'TRIG1', 'IF (-45,45) OR (135,-135)', kind='operand', line=105)

W('23,3325', 0o72545, '', 'DLOAD', 'SL1', '(45,135) OR (-135,-45)', kind='interp', line=107)
W('23,3326', 0o00021, '', '', 'COSTH', kind='operand', line=108)
W('23,3327', 0o75326, '', 'ACOS', 'SIGN', kind='interp', line=109)
W('23,3330', 0o00023, '', '', 'SINTH', kind='operand', line=110)
W('23,3331', 0o00025, '', 'STORE', 'THETA', 'X = ARCCOS(COS) WITH SIGN(SIN)', kind='interp', line=111)
W('23,3332', 0o77616, '', 'RVQ', kind='interp', line=112)

W('23,3333', 0o72545, 'TRIG1', 'DLOAD', 'SL1', '(-45,45) OR (135,-135)', kind='interp', line=114)
W('23,3334', 0o00023, '', '', 'SINTH', kind='operand', line=115)
W('23,3335', 0o77736, '', 'ASIN', kind='interp', line=116)
W('23,3336', 0o14025, '', 'STODL', 'THETA', 'X = ARCSIN(SIN) WITH SIGN(SIN)', kind='interp', line=117)
W('23,3337', 0o00021, '', '', 'COSTH', kind='operand', line=118)
W('23,3340', 0o77640, '', 'BMN', kind='interp', line=119)
W('23,3341', 0o47344, '', '', 'TRIG2', 'IF (135,-135)', kind='operand', line=120)

W('23,3342', 0o43545, '', 'DLOAD', 'RVQ', kind='interp', line=122)
W('23,3343', 0o00025, '', '', 'THETA', 'X = ARCSIN(SIN)   (-45,45)', kind='operand', line=123)

W('23,3344', 0o75345, 'TRIG2', 'DLOAD', 'SIGN', '(135,-135)', kind='interp', line=125)
W('23,3345', 0o06520, '', '', 'HIDPHALF', kind='operand', line=126)
W('23,3346', 0o00023, '', '', 'SINTH', kind='operand', line=127)
W('23,3347', 0o77625, '', 'DSU', kind='interp', line=128)
W('23,3350', 0o00025, '', '', 'THETA', kind='operand', line=129)
W('23,3351', 0o00025, '', 'STORE', 'THETA', 'X = .5 WITH SIGN(SIN) - ARCSIN(SIN)', kind='interp', line=130)
W('23,3352', 0o77616, '', 'RVQ', '', '      (+) - (+) OR (-) - (-)', kind='interp', line=131)

# Page 1252
# SMNB, NBSM, AND AXISROT, WHICH USED TO APPEAR HERE, HAVE BEEN
# COMBINED IN A ROUTINE CALLED AX*SR*T, WHICH APPEARS AMONG THE POWERED
# FLIGHT SUBROUTINES.

# Page 1253
# CALCGA COMPUTES THE CDU DRIVING ANGLES REQUIRED TO BRING THE STABLE MEMBER INTO THE DESIRED ORIENTATION.
#
# THE INPUTS ARE  1) THE NAVIGATION BASE COORDINATES REFERRED TO ANY COORDINATE SYSTEM.  THE THREE HALF-UNIT
# VECTORS ARE STORED AT XNB, YNB, AND ZNB.  2) THE DESIRED STABLE MEMBER COORDINATES REFERRED TO THE SAME
# COORDINATE SYSTEM ARE STORED AT XSM, YSM, AND ZSM.
#
# THE OUTPUTS ARE THE THREE CDU DRIVING ANGLES AND ARE STORED SP AT THETAD, THETAD +1, AND THETAD +2.

W('23,3353', 0o77601, 'CALCGA', 'SETPD', '', 'PUSHDOWN 00-05, 16D-21D, 34D-37D', kind='interp', line=147)
W('23,3354', 0o00001, '', '', '0', kind='operand', line=148)
W('23,3355', 0o47375, '', 'VLOAD', 'VXV', kind='interp', line=149)
W('23,3356', 0o02665, '', '', 'XNB', 'XNB = OGA (OUTER GIMBAL AXIS)', kind='operand', line=150)
W('23,3357', 0o02651, '', '', 'YSM', 'YSM = IGA (INNER GIMBAL AXIS)', kind='operand', line=151)
W('23,3360', 0o41456, '', 'UNIT', 'PUSH', 'PD0 = UNIT(OGA X IGA) = MGA', kind='interp', line=152)

W('23,3361', 0o44041, '', 'DOT', 'ITA', kind='interp', line=154)
W('23,3362', 0o02701, '', '', 'ZNB', kind='operand', line=155)
W('23,3363', 0o00051, '', '', 'S2', kind='operand', line=156)
W('23,3364', 0o24021, '', 'STOVL', 'COSTH', 'COS(OG) = MGA . ZNB', kind='interp', line=157)
W('23,3365', 0o00001, '', '', '0', kind='operand', line=158)
W('23,3366', 0o77641, '', 'DOT', kind='interp', line=159)
W('23,3367', 0o02673, '', '', 'YNB', kind='operand', line=160)
W('23,3370', 0o34023, '', 'STCALL', 'SINTH', 'SIN(OG) = MGA . YNB', kind='interp', line=161)
W('23,3371', 0o47320, '', '', 'ARCTRIG', kind='operand', line=162)
W('23,3372', 0o26740, '', 'STOVL', 'OGC', kind='interp', line=163)
W('23,3373', 0o00001, '', '', '0', kind='operand', line=164)

W('23,3374', 0o50235, '', 'VXV', 'DOT', 'PROVISION FOR MG ANGLE OF 90 DEGREES', kind='interp', line=166)
W('23,3375', 0o02665, '', '', 'XNB', kind='operand', line=167)
W('23,3376', 0o02651, '', '', 'YSM', kind='operand', line=168)
W('23,3377', 0o77752, '', 'SL1', kind='interp', line=169)
W('23,3400', 0o24021, '', 'STOVL', 'COSTH', 'COS(MG) = IGA . (MGA X OGA)', kind='interp', line=170)
W('23,3401', 0o02651, '', '', 'YSM', kind='operand', line=171)
W('23,3402', 0o77641, '', 'DOT', kind='interp', line=172)
W('23,3403', 0o02665, '', '', 'XNB', kind='operand', line=173)
W('23,3404', 0o34023, '', 'STCALL', 'SINTH', 'SIN(MG) = IGA . OGA', kind='interp', line=174)
W('23,3405', 0o47320, '', '', 'ARCTRIG', kind='operand', line=175)
W('23,3406', 0o02744, '', 'STORE', 'MGC', kind='interp', line=176)

W('23,3407', 0o45246, '', 'ABS', 'DSU', kind='interp', line=178)
W('23,3410', 0o07536, '', '', '.166...', kind='operand', line=179)
W('23,3411', 0o77644, '', 'BPL', kind='interp', line=180)
W('23,3412', 0o47431, '', '', 'GIMLOCK1', 'IF ANGLE GREATER THAN 60 DEGREES', kind='operand', line=181)

W('23,3413', 0o50375, 'CALCGA1', 'VLOAD', 'DOT', kind='interp', line=183)
W('23,3414', 0o02657, '', '', 'ZSM', kind='operand', line=184)
W('23,3415', 0o00001, '', '', '0', kind='operand', line=185)
W('23,3416', 0o24021, '', 'STOVL', 'COSTH', 'COS(IG) = ZSM . MGA', kind='interp', line=186)
W('23,3417', 0o02643, '', '', 'XSM', kind='operand', line=187)
# Page 1254
W('23,3420', 0o45441, '', 'DOT', 'STADR', kind='interp', line=189)
W('23,3421', 0o43754, '', 'STCALL', 'SINTH', 'SIN(IG) = XSM . MGA', kind='interp', line=190)
W('23,3422', 0o47320, '', '', 'ARCTRIG', kind='operand', line=191)

W('23,3423', 0o26742, '', 'STOVL', 'IGC', kind='interp', line=193)
W('23,3424', 0o02740, '', '', 'OGC', kind='operand', line=194)
W('23,3425', 0o77634, '', 'RTB', kind='interp', line=195)
W('23,3426', 0o21620, '', '', 'V1STO2S', kind='operand', line=196)
W('23,3427', 0o34322, '', 'STCALL', 'THETAD', kind='interp', line=197)
W('23,3430', 0o00051, '', '', 'S2', kind='operand', line=198)

W('23,3431', 0o77776, 'GIMLOCK1', 'EXIT', kind='interp', line=200)
W('23,3432', 0o05567, '', 'TC', 'ALARM', line=201)
W('23,3433', 0o00401, '', 'OCT', '00401', kind='data', line=202)
W('23,3434', 0o05504, '', 'TC', 'UPFLAG', 'GIMBAL LOCK HAS OCCURRED', line=203)
W('23,3435', 0o00056, '', 'ADRES', 'GLOKFAIL', kind='data', line=204)

W('23,3436', 0o06037, '', 'TC', 'INTPRET', line=206)
W('23,3437', 0o77650, '', 'GOTO', kind='interp', line=207)
W('23,3440', 0o47413, '', '', 'CALCGA1', kind='operand', line=208)

# Page 1255
# AXISGEN COMPUTES THE COORDINATES OF ONE COORDINATE SYSTEM REFERRED TO ANOTHER COORDINATE SYSTEM.
#
# THE INPUTS ARE  1) THE STAR1 VECTOR REFERRED TO COORDINATE SYSTEM A STORED AT STARAD.  2) THE STAR2 VECTOR
# REFERRED TO COORDINATE SYSTEM A STORED AT STARAD +6.  3) THE STAR1 VECTOR REFERRED TO COORDINATE SYSTEM B STORED
# AT LOCATION 6 OF THE VAC AREA.  4) THE STAR2 VECTOR REFERRED TO COORDINATE SYSTEM B STORED AT LOCATION 12D OF
# THE VAC AREA.
#
# THE OUTPUT DEFINES COORDINATE SYSTEM A REFERRED TO COORDINATE SYSTEM B.  THE THREE HALF-UNIT VECTORS ARE STORED
# AT LOCATIONS XDC, XDC +6, XDC +12D, AND STARAD, STARAD +6, STARAD +12D.

W('23,3441', 0o66370, 'AXISGEN', 'AXT,1', 'SSP', 'PUSHDOWN 00-30D, 34D-37D', kind='interp', line=221)
W('23,3442', 0o02714, '', '', 'STARAD +6', kind='operand', line=222)
W('23,3443', 0o00051, '', '', 'S1', kind='operand', line=223)
W('23,3444', 0o02700, '', '', 'STARAD -6', kind='operand', line=224)

W('23,3445', 0o77601, '', 'SETPD', kind='interp', line=226)
W('23,3446', 0o00001, '', '', '0', kind='operand', line=227)
W('23,3447', 0o46773, 'AXISGEN1', 'VLOAD*', 'VXV*', '06D   UA = S1', kind='interp', line=228)
W('23,3450', 0o02723, '', '', 'STARAD +12D,1', '      STARAD +00D     UB = S1', kind='operand', line=229)
W('23,3451', 0o02731, '', '', 'STARAD +18D,1', kind='operand', line=230)
W('23,3452', 0o77656, '', 'UNIT', '', '12D   VA = UNIT(S1 X S2)', kind='interp', line=231)
W('23,3453', 0o06731, '', 'STORE', 'STARAD +18D,1', '      STARAD +06D     VB = UNIT(S1 X S2)', kind='interp', line=232)
W('23,3454', 0o77773, '', 'VLOAD*', kind='interp', line=233)
W('23,3455', 0o02723, '', '', 'STARAD +12D,1', kind='operand', line=234)

W('23,3456', 0o76433, '', 'VXV*', 'VSL1', kind='interp', line=236)
W('23,3457', 0o02731, '', '', 'STARAD +18D,1', '18D   WA = UA X VA', kind='operand', line=237)
W('23,3460', 0o06737, '', 'STORE', 'STARAD +24D,1', '      STARAD +12D     WB = UB X VB', kind='interp', line=238)

W('23,3461', 0o77700, '', 'TIX,1', kind='interp', line=240)
W('23,3462', 0o47447, '', '', 'AXISGEN1', kind='operand', line=241)

W('23,3463', 0o66160, '', 'AXC,1', 'SXA,1', kind='interp', line=243)
W('23,3464', 0o00006, '', '', '6', kind='operand', line=244)
W('23,3465', 0o00036, '', '', '30D', kind='operand', line=245)

W('23,3466', 0o66370, '', 'AXT,1', 'SSP', kind='interp', line=247)
W('23,3467', 0o00022, '', '', '18D', kind='operand', line=248)
W('23,3470', 0o00051, '', '', 'S1', kind='operand', line=249)
W('23,3471', 0o00006, '', '', '6', kind='operand', line=250)

W('23,3472', 0o66374, '', 'AXT,2', 'SSP', kind='interp', line=252)
W('23,3473', 0o00006, '', '', '6', kind='operand', line=253)
W('23,3474', 0o00052, '', '', 'S2', kind='operand', line=254)
W('23,3475', 0o00002, '', '', '2', kind='operand', line=255)

W('23,3476', 0o76720, 'AXISGEN2', 'XCHX,1', 'VLOAD*', kind='interp', line=257)
W('23,3477', 0o00036, '', '', '30D', 'X1=-6 X2=+6   X1=-6 X2=+4     X1=-6 X2=+2', kind='operand', line=258)
W('23,3500', 0o00001, '', '', '0,1', kind='operand', line=259)

# Page 1256
W('23,3501', 0o62757, '', 'VXSC*', 'PDVL*', 'J=(UA)(UB1)   J=(UA)(UB2)     J=(UA)(UB3)', kind='interp', line=262)
W('23,3502', 0o75062, '', '', 'STARAD +6,2', kind='operand', line=263)
W('23,3503', 0o00007, '', '', '6,1', kind='operand', line=264)
W('23,3504', 0o77757, '', 'VXSC*', kind='interp', line=265)
W('23,3505', 0o75054, '', '', 'STARAD +12D,2', kind='operand', line=266)
W('23,3506', 0o30031, '', 'STOVL*', '24D', 'K=(VA)(VB1)   J=(VA)(VB2)     J=(VA)(VB3)', kind='interp', line=267)
W('23,3507', 0o00015, '', '', '12D,1', kind='operand', line=268)

W('23,3510', 0o53357, '', 'VXSC*', 'VAD', kind='interp', line=270)
W('23,3511', 0o75046, '', '', 'STARAD +18D,2', 'L=(WA)(WB1)   J=(WA)(WB2)     J=(WA)(WB3)', kind='operand', line=271)
W('23,3512', 0o76455, '', 'VAD', 'VSL1', kind='interp', line=272)
W('23,3513', 0o00031, '', '', '24D', kind='operand', line=273)
W('23,3514', 0o53520, '', 'XCHX,1', 'UNIT', kind='interp', line=274)
W('23,3515', 0o00036, '', '', '30D', kind='operand', line=275)
W('23,3516', 0o06707, '', 'STORE', 'XDC +18D,1', 'XDC = L+J+K   YDC = L+J+K     ZDC = L+J+K', kind='interp', line=276)

W('23,3517', 0o77700, '', 'TIX,1', kind='interp', line=278)
W('23,3520', 0o47521, '', '', 'AXISGEN3', kind='operand', line=279)

W('23,3521', 0o77704, 'AXISGEN3', 'TIX,2', kind='interp', line=281)
W('23,3522', 0o47476, '', '', 'AXISGEN2', kind='operand', line=282)

W('23,3523', 0o77775, '', 'VLOAD', kind='interp', line=284)
W('23,3524', 0o02665, '', '', 'XDC', kind='operand', line=285)
W('23,3525', 0o26707, '', 'STOVL', 'STARAD', kind='interp', line=286)
W('23,3526', 0o02673, '', '', 'YDC', kind='operand', line=287)
W('23,3527', 0o26715, '', 'STOVL', 'STARAD +6', kind='interp', line=288)
W('23,3530', 0o02701, '', '', 'ZDC', kind='operand', line=289)
W('23,3531', 0o02723, '', 'STORE', 'STARAD +12D', kind='interp', line=290)

W('23,3532', 0o77616, '', 'RVQ', kind='interp', line=292)

# Page 1257
W('23,3533', 0o05520, 'QTSN45', '2DEC', '.1768', kind='data', line=295)
W('23,3534', 0o26075, kind='data', line=295)

W('23,3535', 0o05252, '.166...', '2DEC', '.1666666667', kind='data', line=297)
W('23,3536', 0o25253, kind='data', line=297)

# Page 1258 (empty page)
