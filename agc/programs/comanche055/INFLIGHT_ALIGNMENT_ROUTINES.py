"""INFLIGHT_ALIGNMENT_ROUTINES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/INFLIGHT_ALIGNMENT_ROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1355-1364 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INFLIGHT_ALIGNMENT_ROUTINES', 'INFLIGHT_ALIGNMENT_ROUTINES.agc', 'Comanche055', pages='1355-1364')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INFLIGHT_ALIGNMENT_ROUTINES.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1355-1364
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

# Page 1355
#   BANK 22
#   SETLOC INFLIGHT
#   BANK

#   EBANK= XSM

# CALCGTA COMPUTES THE GYRO TORQUE ANGLES REQUIRED TO BRING THE STABLE MEMBER INTO THE DESIRED ORIENTATION.
#
# THE INPUT IS THE DESIRED STABLE MEMBER COORDINATES REFERRED TO PRESENT STABLE MEMBER COORDINATES. THE THREE
# HALF-UNIT VECTORS ARE STORED AT XDC, YDC, AND ZDC.
#
# THE OUTPUTS ARE THE THREE GYRO TORQUING ANGLES TO BE APPLIED TO THE Y, Z, AND X GYROS AND ARE STORED DP AT IGC,
# MGC, AND OGC RESPECTIVELY.

#   COUNT 23/INFLT

W('23,3205', 0o71220, 'CALCGTA', 'ITA', 'DLOAD', 'PUSHDOWN  00-03,16D-27D,34D-37D', kind='interp', line=47)
W('23,3206', 0o00051, '', '', 'S2', 'XDC = (XD1 XD2 XD3)', kind='operand', line=48)
W('23,3207', 0o02714, '', '', 'XDC', 'YDC = (YD1 YD2 YD3)', kind='operand', line=49)
W('23,3210', 0o65325, '', 'PDDL', 'PDDL', 'ZDC = (ZD1 ZD2 ZD3)', kind='interp', line=50)
W('23,3211', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=51)
W('23,3212', 0o02720, '', '', 'XDC +4', kind='operand', line=52)
W('23,3213', 0o55476, '', 'DCOMP', 'VDEF', kind='interp', line=53)
W('23,3214', 0o77656, '', 'UNIT', kind='interp', line=54)
W('23,3215', 0o14027, '', 'STODL', 'ZPRIME', 'ZP = UNIT(-XD3 0 XD1) = (ZP1 ZP2 ZP3)', kind='interp', line=55)
W('23,3216', 0o00027, '', '', 'ZPRIME', kind='operand', line=56)

W('23,3217', 0o77742, '', 'SR1', kind='interp', line=58)
W('23,3220', 0o14023, '', 'STODL', 'SINTH', 'SIN(IGC) = ZP1', kind='interp', line=59)
W('23,3221', 0o00033, '', '', 'ZPRIME +4', kind='operand', line=60)
W('23,3222', 0o77742, '', 'SR1', kind='interp', line=61)
W('23,3223', 0o34021, '', 'STCALL', 'COSTH', 'COS(IGC) = ZP3', kind='interp', line=62)
W('23,3224', 0o47256, '', '', 'ARCTRIG', kind='operand', line=63)

W('23,3225', 0o16762, '', 'STODL', 'IGC', 'Y GYRO TORQUING ANGLE   FRACTION OF REV.', kind='interp', line=65)
W('23,3226', 0o02716, '', '', 'XDC +2', kind='operand', line=66)
W('23,3227', 0o77742, '', 'SR1', kind='interp', line=67)
W('23,3230', 0o14023, '', 'STODL', 'SINTH', 'SIN(MGC) = XD2', kind='interp', line=68)
W('23,3231', 0o00027, '', '', 'ZPRIME', kind='operand', line=69)

W('23,3232', 0o65205, '', 'DMP', 'PDDL', kind='interp', line=71)
W('23,3233', 0o02720, '', '', 'XDC +4', 'PD00 = (ZP1)(XD3)', kind='operand', line=72)
W('23,3234', 0o00033, '', '', 'ZPRIME +4', kind='operand', line=73)

W('23,3235', 0o45205, '', 'DMP', 'DSU', kind='interp', line=75)
W('23,3236', 0o02714, '', '', 'XDC', 'MPAC = (ZP3)(XD1)', kind='operand', line=76)
W('23,3237', 0o77626, '', 'STADR', kind='interp', line=77)
W('23,3240', 0o43756, '', 'STCALL', 'COSTH', 'COS(MGC) = MPAC - PD00', kind='interp', line=78)
W('23,3241', 0o47256, '', '', 'ARCTRIG', kind='operand', line=79)
# Page 1356
W('23,3242', 0o26764, '', 'STOVL', 'MGC', 'Z GYRO TORQUING ANGLE   FRACTION OF REV.', kind='interp', line=81)
W('23,3243', 0o00027, '', '', 'ZPRIME', kind='operand', line=82)
W('23,3244', 0o77641, '', 'DOT', kind='interp', line=83)
W('23,3245', 0o02730, '', '', 'ZDC', kind='operand', line=84)
W('23,3246', 0o24021, '', 'STOVL', 'COSTH', 'COS(OGC) = ZP . ZDC', kind='interp', line=85)
W('23,3247', 0o00027, '', '', 'ZPRIME', kind='operand', line=86)
W('23,3250', 0o77641, '', 'DOT', kind='interp', line=87)
W('23,3251', 0o02722, '', '', 'YDC', kind='operand', line=88)
W('23,3252', 0o34023, '', 'STCALL', 'SINTH', 'SIN(OGC) = ZP . YDC', kind='interp', line=89)
W('23,3253', 0o47256, '', '', 'ARCTRIG', kind='operand', line=90)

W('23,3254', 0o36760, '', 'STCALL', 'OGC', 'X GYRO TORQUING ANGLE   FRACTION OF REV.', kind='interp', line=92)
W('23,3255', 0o00051, '', '', 'S2', kind='operand', line=93)

# Page 1357
# ARCTRIG COMPUTES AN ANGLE GIVEN THE SINE AND COSINE OF THIS ANGLE.
#
# THE INPUTS ARE SIN/4 AND COS/4 STORED DP AT SINTH AND COSTH.
#
# THE OUTPUT IS THE CALCULATED ANGLE BETWEEN +.5 AND -.5 REVOLUTIONS AND STORED AT THETA. THE OUTPUT IS ALSO
# AVAILABLE AT MPAC.

W('23,3256', 0o51545, 'ARCTRIG', 'DLOAD', 'ABS', 'PUSHDOWN  16D-21D', kind='interp', line=103)
W('23,3257', 0o00023, '', '', 'SINTH', kind='operand', line=104)
W('23,3260', 0o50025, '', 'DSU', 'BMN', kind='interp', line=105)
W('23,3261', 0o07474, '', '', 'QTSN45', 'ABS(SIN/4) - SIN(45)/4', kind='operand', line=106)
W('23,3262', 0o47271, '', '', 'TRIG1', 'IF (-45,45) OR (135,-135)', kind='operand', line=107)

W('23,3263', 0o72545, '', 'DLOAD', 'SL1', '(45,135) OR (-135,-45)', kind='interp', line=109)
W('23,3264', 0o00021, '', '', 'COSTH', kind='operand', line=110)
W('23,3265', 0o75326, '', 'ACOS', 'SIGN', kind='interp', line=111)
W('23,3266', 0o00023, '', '', 'SINTH', kind='operand', line=112)
W('23,3267', 0o00025, '', 'STORE', 'THETA', 'X = ARCCOS(COS) WITH SIGN(SIN)', kind='interp', line=113)
W('23,3270', 0o77616, '', 'RVQ', kind='interp', line=114)

W('23,3271', 0o72545, 'TRIG1', 'DLOAD', 'SL1', '(-45,45) OR (135,-135)', kind='interp', line=116)
W('23,3272', 0o00023, '', '', 'SINTH', kind='operand', line=117)
W('23,3273', 0o77736, '', 'ASIN', kind='interp', line=118)
W('23,3274', 0o14025, '', 'STODL', 'THETA', 'X = ARCSIN(SIN) WITH SIGN(SIN)', kind='interp', line=119)
W('23,3275', 0o00021, '', '', 'COSTH', kind='operand', line=120)
W('23,3276', 0o77640, '', 'BMN', kind='interp', line=121)
W('23,3277', 0o47302, '', '', 'TRIG2', 'IF (135,-135)', kind='operand', line=122)

W('23,3300', 0o43545, '', 'DLOAD', 'RVQ', kind='interp', line=124)
W('23,3301', 0o00025, '', '', 'THETA', 'X = ARCSIN(SIN)   (-45,45)', kind='operand', line=125)

W('23,3302', 0o75345, 'TRIG2', 'DLOAD', 'SIGN', '(135,-135)', kind='interp', line=127)
W('23,3303', 0o15333, '', '', 'HIDPHALF', kind='operand', line=128)
W('23,3304', 0o00023, '', '', 'SINTH', kind='operand', line=129)
W('23,3305', 0o77625, '', 'DSU', kind='interp', line=130)
W('23,3306', 0o00025, '', '', 'THETA', kind='operand', line=131)
W('23,3307', 0o00025, '', 'STORE', 'THETA', 'X = .5 WITH SIGN(SIN) - ARCSIN(SIN)', kind='interp', line=132)
W('23,3310', 0o77616, '', 'RVQ', '', '      (+) - (+) OR (-) - (-)', kind='interp', line=133)

# Page 1358
# SMNB, NBSM, AND AXISROT, WHICH USED TO APPEAR HERE, HAVE BEEN
# COMBINED IN A ROUTINE CALLED AX*SR*T, WHICH APPEARS AMONG THE POWERED
# FLIGHT SUBROUTINES.

# Page 1359
# CALCGA COMPUTES THE CDU DRIVING ANGLES REQUIRED TO BRING THE STABLE MEMBER INTO THE DESIRED ORIENTATION.
#
# THE INPUTS ARE  1) THE NAVIGATION BASE COORDINATES REFERRED TO ANY COORDINATE SYSTEM. THE THREE HALF-UNIT
# VECTORS ARE STORED AT XNB, YNB, AND ZNB.  2) THE DESIRED STABLE MEMBER COORDINATES REFERRED TO THE SAME
# COORDINATE SYSTEM ARE STORED AT XSM, YSM, AND ZSM.
#
# THE OUTPUTS ARE THE THREE CDU DRIVING ANGLES AND ARE STORED SP AT THETAD, THETAD +1, AND THETAD +2.

W('23,3311', 0o77601, 'CALCGA', 'SETPD', '', 'PUSHDOWN  00-05, 16D-21D, 34D-37D', kind='interp', line=149)
W('23,3312', 0o00001, '', '', '0', kind='operand', line=150)
W('23,3313', 0o47375, '', 'VLOAD', 'VXV', kind='interp', line=151)
W('23,3314', 0o02714, '', '', 'XNB', 'XNB = OGA (OUTER GIMBAL AXIS)', kind='operand', line=152)
W('23,3315', 0o02700, '', '', 'YSM', 'YSM = IGA (INNER GIMBAL AXIS)', kind='operand', line=153)
W('23,3316', 0o41456, '', 'UNIT', 'PUSH', 'PD0 = UNIT(OGA X IGA) = MGA', kind='interp', line=154)

W('23,3317', 0o44041, '', 'DOT', 'ITA', kind='interp', line=156)
W('23,3320', 0o02730, '', '', 'ZNB', kind='operand', line=157)
W('23,3321', 0o00051, '', '', 'S2', kind='operand', line=158)
W('23,3322', 0o24021, '', 'STOVL', 'COSTH', 'COS(OG) = MGA . ZNB', kind='interp', line=159)
W('23,3323', 0o00001, '', '', '0', kind='operand', line=160)
W('23,3324', 0o77641, '', 'DOT', kind='interp', line=161)
W('23,3325', 0o02722, '', '', 'YNB', kind='operand', line=162)
W('23,3326', 0o34023, '', 'STCALL', 'SINTH', 'SIN(OG) = MGA . YNB', kind='interp', line=163)
W('23,3327', 0o47256, '', '', 'ARCTRIG', kind='operand', line=164)
W('23,3330', 0o26760, '', 'STOVL', 'OGC', kind='interp', line=165)
W('23,3331', 0o00001, '', '', '0', kind='operand', line=166)

W('23,3332', 0o50235, '', 'VXV', 'DOT', 'PROVISION FOR MG ANGLE OF 90 DEGREES', kind='interp', line=168)
W('23,3333', 0o02714, '', '', 'XNB', kind='operand', line=169)
W('23,3334', 0o02700, '', '', 'YSM', kind='operand', line=170)
W('23,3335', 0o77752, '', 'SL1', kind='interp', line=171)
W('23,3336', 0o24021, '', 'STOVL', 'COSTH', 'COS(MG) = IGA . (MGA X OGA)', kind='interp', line=172)
W('23,3337', 0o02700, '', '', 'YSM', kind='operand', line=173)
W('23,3340', 0o77641, '', 'DOT', kind='interp', line=174)
W('23,3341', 0o02714, '', '', 'XNB', kind='operand', line=175)
W('23,3342', 0o34023, '', 'STCALL', 'SINTH', 'SIN(MG) = IGA . OGA', kind='interp', line=176)
W('23,3343', 0o47256, '', '', 'ARCTRIG', kind='operand', line=177)
W('23,3344', 0o02764, '', 'STORE', 'MGC', kind='interp', line=178)

W('23,3345', 0o45246, '', 'ABS', 'DSU', kind='interp', line=180)
W('23,3346', 0o07476, '', '', '.166...', kind='operand', line=181)
W('23,3347', 0o77644, '', 'BPL', kind='interp', line=182)
W('23,3350', 0o47371, '', '', 'GIMLOCK1', 'IF ANGLE GREATER THAN 60 DEGREES', kind='operand', line=183)

W('23,3351', 0o50375, 'CALCGA1', 'VLOAD', 'DOT', kind='interp', line=185)
W('23,3352', 0o02706, '', '', 'ZSM', kind='operand', line=186)
W('23,3353', 0o00001, '', '', '0', kind='operand', line=187)
W('23,3354', 0o24021, '', 'STOVL', 'COSTH', 'COS(IG) = ZSM . MGA', kind='interp', line=188)
W('23,3355', 0o02672, '', '', 'XSM', kind='operand', line=189)
# Page 1360
W('23,3356', 0o45441, '', 'DOT', 'STADR', kind='interp', line=191)
W('23,3357', 0o43754, '', 'STCALL', 'SINTH', 'SIN(IG) = XSM . MGA', kind='interp', line=192)
W('23,3360', 0o47256, '', '', 'ARCTRIG', kind='operand', line=193)

W('23,3361', 0o26762, '', 'STOVL', 'IGC', kind='interp', line=195)
W('23,3362', 0o02760, '', '', 'OGC', kind='operand', line=196)
W('23,3363', 0o43034, '', 'RTB', 'BONCLR', kind='interp', line=197)
W('23,3364', 0o45552, '', '', 'V1STO2S', kind='operand', line=198)
W('23,3365', 0o00200, '', '', 'CPHIFLAG', kind='operand', line=199)
W('23,3366', 0o00051, '', '', 'S2', kind='operand', line=200)
W('23,3367', 0o35156, '', 'STCALL', 'THETAD', kind='interp', line=201)
W('23,3370', 0o00051, '', '', 'S2', kind='operand', line=202)

W('23,3371', 0o77776, 'GIMLOCK1', 'EXIT', kind='interp', line=204)
W('23,3372', 0o05650, '', 'TC', 'ALARM', line=205)
W('23,3373', 0o00401, '', 'OCT', '00401', kind='data', line=206)
W('23,3374', 0o05546, '', 'TC', 'UPFLAG', 'GIMBAL LOCK HAS OCCURRED', line=207)
W('23,3375', 0o00056, '', 'ADRES', 'GLOKFAIL', kind='data', line=208)

W('23,3376', 0o06006, '', 'TC', 'INTPRET', line=210)
W('23,3377', 0o77650, '', 'GOTO', kind='interp', line=211)
W('23,3400', 0o47351, '', '', 'CALCGA1', kind='operand', line=212)

# Page 1361
# AXISGEN COMPUTES THE COORDINATES OF ONE COORDINATE SYSTEM REFERRED TO ANOTHER COORDINATE SYSTEM.
#
# THE INPUTS ARE  1) THE STAR1 VECTOR REFERRED TO COORDINATE SYSTEM A STORED AT STARAD.  2) THE STAR2 VECTOR
# REFERRED TO COORDINATE SYSTEM A STORED AT STARAD +6.  3) THE STAR1 VECTOR REFERRED TO COORDINATE SYSTEM B STORED
# AT LOCATION 6 OF THE VAC AREA.  4) THE STAR2 VECTOR REFERRED TO COORDINATE SYSTEM B STORED AT LOCATION 12D OF
# THE VAC AREA.
#
# THE OUTPUT DEFINES COORDINATE SYSTEM A REFERRED TO COORDINATE SYSTEM B.  THE THREE HALF-UNIT VECTORS ARE STORED
# AT LOCATIONS XDC, XDC +6, XDC +12D, AND STARAD, STARAD +6, STARAD +12D.

W('23,3401', 0o66370, 'AXISGEN', 'AXT,1', 'SSP', 'PUSHDOWN  00-30D, 34D-37D', kind='interp', line=225)
W('23,3402', 0o02743, '', '', 'STARAD +6', kind='operand', line=226)
W('23,3403', 0o00051, '', '', 'S1', kind='operand', line=227)
W('23,3404', 0o02727, '', '', 'STARAD -6', kind='operand', line=228)

W('23,3405', 0o77601, '', 'SETPD', kind='interp', line=230)
W('23,3406', 0o00001, '', '', '0', kind='operand', line=231)
W('23,3407', 0o46773, 'AXISGEN1', 'VLOAD*', 'VXV*', '06D   UA = S1', kind='interp', line=232)
W('23,3410', 0o02752, '', '', 'STARAD +12D,1', '      STARAD +00D     UB = S1', kind='operand', line=233)
W('23,3411', 0o02760, '', '', 'STARAD +18D,1', kind='operand', line=234)
W('23,3412', 0o77656, '', 'UNIT', '', '12D   VA = UNIT(S1 X S2)', kind='interp', line=235)
W('23,3413', 0o06760, '', 'STORE', 'STARAD +18D,1', '      STARAD +06D     VB = UNIT(S1 X S2)', kind='interp', line=236)
W('23,3414', 0o77773, '', 'VLOAD*', kind='interp', line=237)
W('23,3415', 0o02752, '', '', 'STARAD +12D,1', kind='operand', line=238)

W('23,3416', 0o76433, '', 'VXV*', 'VSL1', kind='interp', line=240)
W('23,3417', 0o02760, '', '', 'STARAD +18D,1', '18D   WA = UA X VA', kind='operand', line=241)
W('23,3420', 0o06766, '', 'STORE', 'STARAD +24D,1', '      STARAD +12D     WB = UB X VB', kind='interp', line=242)

W('23,3421', 0o77700, '', 'TIX,1', kind='interp', line=244)
W('23,3422', 0o47407, '', '', 'AXISGEN1', kind='operand', line=245)

W('23,3423', 0o66160, '', 'AXC,1', 'SXA,1', kind='interp', line=247)
W('23,3424', 0o00006, '', '', '6', kind='operand', line=248)
W('23,3425', 0o00036, '', '', '30D', kind='operand', line=249)

W('23,3426', 0o66370, '', 'AXT,1', 'SSP', kind='interp', line=251)
W('23,3427', 0o00022, '', '', '18D', kind='operand', line=252)
W('23,3430', 0o00051, '', '', 'S1', kind='operand', line=253)
W('23,3431', 0o00006, '', '', '6', kind='operand', line=254)

W('23,3432', 0o66374, '', 'AXT,2', 'SSP', kind='interp', line=256)
W('23,3433', 0o00006, '', '', '6', kind='operand', line=257)
W('23,3434', 0o00052, '', '', 'S2', kind='operand', line=258)
W('23,3435', 0o00002, '', '', '2', kind='operand', line=259)

W('23,3436', 0o76720, 'AXISGEN2', 'XCHX,1', 'VLOAD*', kind='interp', line=261)
W('23,3437', 0o00036, '', '', '30D', 'X1=-6 X2=+6   X1=-6 X2=+4     X1=-6 X2=+2', kind='operand', line=262)
W('23,3440', 0o00001, '', '', '0,1', kind='operand', line=263)

# Page 1362
W('23,3441', 0o62757, '', 'VXSC*', 'PDVL*', 'J=(UA)(UB1)   J=(UA)(UB2)     J=(UA)(UB3)', kind='interp', line=266)
W('23,3442', 0o75033, '', '', 'STARAD +6,2', kind='operand', line=267)
W('23,3443', 0o00007, '', '', '6,1', kind='operand', line=268)
W('23,3444', 0o77757, '', 'VXSC*', kind='interp', line=269)
W('23,3445', 0o75025, '', '', 'STARAD +12D,2', kind='operand', line=270)
W('23,3446', 0o30031, '', 'STOVL*', '24D', 'K=(VA)(VB1)   J=(VA)(VB2)     J=(VA)(VB3)', kind='interp', line=271)
W('23,3447', 0o00015, '', '', '12D,1', kind='operand', line=272)

W('23,3450', 0o53357, '', 'VXSC*', 'VAD', kind='interp', line=274)
W('23,3451', 0o75017, '', '', 'STARAD +18D,2', 'L=(WA)(WB1)   J=(WA)(WB2)     J=(WA)(WB3)', kind='operand', line=275)
W('23,3452', 0o76455, '', 'VAD', 'VSL1', kind='interp', line=276)
W('23,3453', 0o00031, '', '', '24D', kind='operand', line=277)
W('23,3454', 0o53520, '', 'XCHX,1', 'UNIT', kind='interp', line=278)
W('23,3455', 0o00036, '', '', '30D', kind='operand', line=279)
W('23,3456', 0o06736, '', 'STORE', 'XDC +18D,1', 'XDC = L+J+K   YDC = L+J+K     ZDC = L+J+K', kind='interp', line=280)

W('23,3457', 0o77700, '', 'TIX,1', kind='interp', line=282)
W('23,3460', 0o47461, '', '', 'AXISGEN3', kind='operand', line=283)

W('23,3461', 0o77704, 'AXISGEN3', 'TIX,2', kind='interp', line=285)
W('23,3462', 0o47436, '', '', 'AXISGEN2', kind='operand', line=286)

W('23,3463', 0o77775, '', 'VLOAD', kind='interp', line=288)
W('23,3464', 0o02714, '', '', 'XDC', kind='operand', line=289)
W('23,3465', 0o26736, '', 'STOVL', 'STARAD', kind='interp', line=290)
W('23,3466', 0o02722, '', '', 'YDC', kind='operand', line=291)
W('23,3467', 0o26744, '', 'STOVL', 'STARAD +6', kind='interp', line=292)
W('23,3470', 0o02730, '', '', 'ZDC', kind='operand', line=293)
W('23,3471', 0o02752, '', 'STORE', 'STARAD +12D', kind='interp', line=294)

W('23,3472', 0o77616, '', 'RVQ', kind='interp', line=296)

# Page 1363
W('23,3473', 0o05520, 'QTSN45', '2DEC', '.1768', kind='data', line=299)
W('23,3474', 0o26075, kind='data', line=299)
W('23,3475', 0o05252, '.166...', '2DEC', '.1666666667', kind='data', line=300)
W('23,3476', 0o25253, kind='data', line=300)

# Page 1364 (empty page)
