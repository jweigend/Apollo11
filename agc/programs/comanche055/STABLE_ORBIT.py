"""STABLE_ORBIT.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/STABLE_ORBIT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 525-532 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('STABLE_ORBIT', 'STABLE_ORBIT.agc', 'Comanche055', pages='525-532')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     STABLE_ORBIT.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        525-532
# Mod history:  2009-05-10 HG    Started adapting from the Colossus249/ file
# of the same name, using Comanche055 page
# images 0525.jpg - 0532.jpg.
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
# Page 525
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
# DURING TRANSFER FROM TIG TO TIME OF INTERCEPT
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
# Page 526
# (4)  DSPTEM1    TIME OF INTERCEPT OF PASSIVE VEHICLE ORBIT
# (FOR SOI ONLY)
# (5)  POSTTPI    PERIGEE ALTITUDE OF ACTIVE VEHICLE ORBIT AFTER
# THE SOI (SOR) MANEUVER
# (6)  DELVTPI    MAGNITUDE OF DELTA V AT SOI (SOR) TIME
# (7)  DELVTPF    MAGNITUDE OF DELTA V AT INTERCEPT TIME
# (8)  DELVLVC    DELTA VELOCITY AT SOI (AND SOR) - LOCAL VERTICAL
# COORDINATES
#
# SUBROUTINES USED
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

W('04,2742', 0o04627, 'P38', 'TC', 'AVFLAGA', 'THIS VEHICLE ACTIVE', line=113)
W('04,2743', 0o02745, '', 'TC', '+2', line=114)
W('04,2744', 0o04642, 'P78', 'TC', 'AVFLAGP', 'OTHER VEHICLE ACTIVE', line=115)
W('04,2745', 0o04647, '', 'TC', 'P20FLGON', 'SET UPDATFLG, TRACKFLG', line=116)
W('04,2746', 0o33274, '', 'CAF', 'V06N33SR', 'DISPLAY TIG', line=117)
W('04,2747', 0o03263, '', 'TC', 'VNDSPLY', line=118)
W('04,2750', 0o33275, '', 'CAF', 'V06N55SR', 'DISPLAY CENTANG', line=119)
W('04,2751', 0o04662, '', 'TCR', 'BANKCALL', line=120)
W('04,2752', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=121)
W('04,2753', 0o14106, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=122)
W('04,2754', 0o12761, '', 'TCF', '+5', 'PROCEED', line=123)
W('04,2755', 0o12750, '', 'TCF', '-5', 'RECYCLE', line=124)
W('04,2756', 0o36214, '', 'CAF', 'THREE', 'IMMEDIATE RETURN - BLANK R1, R2', line=125)
W('04,2757', 0o05526, '', 'TCR', 'BLANKET', line=126)
W('04,2760', 0o15217, '', 'TCF', 'ENDOFJOB', line=127)
W('04,2761', 0o35022, '', 'CAF', 'FIVE', line=128)
W('04,2762', 0o55131, '', 'TS', 'OPTION1', line=129)
W('04,2763', 0o35017, '', 'CAF', 'ONE', line=130)
W('04,2764', 0o55132, '', 'TS', 'OPTION2', 'OPTION CODE IS SET TO 1', line=131)
# Page 527
W('04,2765', 0o33276, '', 'CAF', 'V04N06SR', 'DISPLAY OPTION CODE - 1 = SOI, 2 = SOR', line=133)
W('04,2766', 0o04662, '', 'TCR', 'BANKCALL', line=134)
W('04,2767', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=135)
W('04,2770', 0o14106, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=136)
W('04,2771', 0o12776, '', 'TCF', '+5', 'PROCEED', line=137)
W('04,2772', 0o12765, '', 'TCF', '-5', 'RECYCLE', line=138)
W('04,2773', 0o35015, '', 'CAF', 'BIT3', 'IMMEDIATE RETURN - BLANK R3', line=139)
W('04,2774', 0o05526, '', 'TCR', 'BLANKET', line=140)
W('04,2775', 0o15217, '', 'TCF', 'ENDOFJOB', line=141)
W('04,2776', 0o06006, '', 'TC', 'INTPRET', line=142)
W('04,2777', 0o77731, '', 'SSP', kind='interp', line=143)
W('04,3000', 0o03766, '', '', 'NN', kind='operand', line=144)
W('04,3001', 0o00002, '', '', '2', kind='operand', line=145)
W('04,3002', 0o70535, '', 'SLOAD', 'SR1', kind='interp', line=146)
W('04,3003', 0o01133, '', '', 'OPTION2', kind='operand', line=147)
W('04,3004', 0o71230, '', 'BHIZ', 'DLOAD', kind='interp', line=148)
W('04,3005', 0o11013, '', '', 'OPTN1', kind='operand', line=149)
W('04,3006', 0o03656, '', '', 'TINT', kind='operand', line=150)
W('04,3007', 0o02611, '', 'STORE', 'TINTSOI', 'STORE FOR SOR PHASE', kind='interp', line=151)
W('04,3010', 0o77614, '', 'CLRGO', kind='interp', line=152)
W('04,3011', 0o01230, '', '', 'OPTNSW', 'OPTNSW; ON = SOI, OFF = SOR', kind='operand', line=153)
W('04,3012', 0o11042, '', '', 'JUNCTN1', kind='operand', line=154)
W('04,3013', 0o43014, 'OPTN1', 'SET', 'CLEAR', 'SOI', kind='interp', line=155)
W('04,3014', 0o01070, '', '', 'OPTNSW', kind='operand', line=156)
W('04,3015', 0o00670, '', '', 'UPDATFLG', kind='operand', line=157)
W('04,3016', 0o77624, '', 'CALL', kind='interp', line=158)
W('04,3017', 0o11216, '', '', 'PREC/TT', kind='operand', line=159)
W('04,3020', 0o43214, '', 'SET', 'DAD', kind='interp', line=160)
W('04,3021', 0o00470, '', '', 'UPDATFLG', kind='operand', line=161)
W('04,3022', 0o03413, '', '', 'TIG', kind='operand', line=162)
W('04,3023', 0o03656, '', 'STORE', 'TINT', 'TI = TIG + TF', kind='interp', line=163)
W('04,3024', 0o01046, '', 'STORE', 'DSPTEM1', 'FOR DISPLAY', kind='interp', line=164)
W('04,3025', 0o77776, '', 'EXIT', kind='interp', line=165)
W('04,3026', 0o33277, '', 'CAF', 'V06N57SR', 'DISPLAY DELTA R', line=166)
W('04,3027', 0o04662, '', 'TCR', 'BANKCALL', line=167)
W('04,3030', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=168)
W('04,3031', 0o14106, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=169)
W('04,3032', 0o13037, '', 'TCF', '+5', 'PROCEED', line=170)
W('04,3033', 0o13026, '', 'TCF', '-5', 'RECYCLE', line=171)
W('04,3034', 0o36211, '', 'CAF', 'SIX', 'IMMEDIATE RETURN - BLANK R2, R3', line=172)
W('04,3035', 0o05526, '', 'TCR', 'BLANKET', line=173)
W('04,3036', 0o15217, '', 'TCF', 'ENDOFJOB', line=174)
W('04,3037', 0o33300, '', 'CAF', 'V06N34SR', 'DISPLAY TIME OF INTERCEPT', line=175)
W('04,3040', 0o03263, '', 'TC', 'VNDSPLY', line=176)
W('04,3041', 0o06006, '', 'TC', 'INTPRET', line=177)
W('04,3042', 0o45014, 'JUNCTN1', 'CLEAR', 'CALL', kind='interp', line=178)
W('04,3043', 0o04266, '', '', 'P39/79SW', kind='operand', line=179)
W('04,3044', 0o10712, '', '', 'SELECTMU', 'SELECT MU, CLEAR FINALFLG, GO TO VN1645', kind='operand', line=180)
W('04,3045', 0o77624, 'RECYCLE', 'CALL', kind='interp', line=181)
W('04,3046', 0o11216, '', '', 'PREC/TT', kind='operand', line=182)
# Page 528
W('04,3047', 0o71214, '', 'BOFF', 'DLOAD', kind='interp', line=184)
W('04,3050', 0o01350, '', '', 'OPTNSW', kind='operand', line=185)
W('04,3051', 0o11071, '', '', 'OPTN2', kind='operand', line=186)
W('04,3052', 0o03656, '', '', 'TINT', kind='operand', line=187)
W('04,3053', 0o34041, '', 'STCALL', 'TDEC1', 'PRECISION UPDATE PASSIVE VEHICLE TO', kind='interp', line=188)
W('04,3054', 0o11247, '', '', 'INTRPVP', '      INTERCEPT TIME', kind='operand', line=189)
W('04,3055', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=190)
W('04,3056', 0o00001, '', '', 'RATT', 'RP/(RP)', kind='operand', line=191)
W('04,3057', 0o47315, '', 'PDVL', 'VXV', kind='interp', line=192)
W('04,3060', 0o00007, '', '', 'VATT', kind='operand', line=193)
W('04,3061', 0o60246, '', 'ABVAL', 'NORM', '(VP X RP/(RP))', kind='interp', line=194)
W('04,3062', 0o00047, '', '', 'X1', kind='operand', line=195)
W('04,3063', 0o56325, '', 'PDDL', 'DDV', kind='interp', line=196)
W('04,3064', 0o02611, '', '', 'DELTAR', kind='operand', line=197)
W('04,3065', 0o77657, '', 'SL*', '', 'DELTA R / (VP X RP/RP)', kind='interp', line=198)
W('04,3066', 0o20172, '', '', '0 -7,1', kind='operand', line=199)
W('04,3067', 0o36613, '', 'STCALL', 'DELTTIME', 'DELTA T = (RP) DELTA R / (VP X RP)', kind='interp', line=200)
W('04,3070', 0o11075, '', '', 'JUNCTN2', kind='operand', line=201)
W('04,3071', 0o43345, 'OPTN2', 'DLOAD', 'DAD', kind='interp', line=202)
W('04,3072', 0o02611, '', '', 'TINTSOI', kind='operand', line=203)
W('04,3073', 0o00037, '', '', 'T', kind='operand', line=204)
W('04,3074', 0o03656, '', 'STORE', 'TINT', 'TI = TI + TF', kind='interp', line=205)
W('04,3075', 0o45345, 'JUNCTN2', 'DLOAD', 'DSU', kind='interp', line=206)
W('04,3076', 0o03656, '', '', 'TINT', kind='operand', line=207)
W('04,3077', 0o02613, '', '', 'DELTTIME', kind='operand', line=208)
W('04,3100', 0o02615, '', 'STORE', 'TARGTIME', 'TT = TI - DELTA T', kind='interp', line=209)

# .... MAINRTNE ....
# SUBROUTINES USED
#
# S3435.25
# PERIAPO1
# SHIFTR1
# VNDSPLY
# BANKCALL
# GOFLASH
# GOTOPOOH
# VN1645

W('04,3101', 0o34041, 'MAINRTNE', 'STCALL', 'TDEC1', 'PRECISION UPDATE PASSIVE VEHICLE TO', kind='interp', line=223)
W('04,3102', 0o11247, '', '', 'INTRPVP', '      TARGET TIME', kind='operand', line=224)
W('04,3103', 0o77745, '', 'DLOAD', kind='interp', line=225)
W('04,3104', 0o03413, '', '', 'TIG', kind='operand', line=226)
W('04,3105', 0o03503, '', 'STORE', 'INTIME', kind='interp', line=227)
W('04,3106', 0o77331, '', 'SSP', 'VLOAD', kind='interp', line=228)
W('04,3107', 0o02371, '', '', 'SUBEXIT', kind='operand', line=229)
W('04,3110', 0o11114, '', '', 'TEST3979', kind='operand', line=230)
W('04,3111', 0o00001, '', '', 'RATT', kind='operand', line=231)
W('04,3112', 0o77624, '', 'CALL', kind='interp', line=232)
W('04,3113', 0o72546, '', '', 'S3435.25', kind='operand', line=233)
W('04,3114', 0o43014, 'TEST3979', 'BOFF', 'BON', kind='interp', line=234)
# Page 529
W('04,3115', 0o04346, '', '', 'P39/79SW', kind='operand', line=236)
W('04,3116', 0o11125, '', '', 'MAINRTN1', kind='operand', line=237)
W('04,3117', 0o01311, '', '', 'FINALFLG', kind='operand', line=238)
W('04,3120', 0o11123, '', '', 'P39P79', kind='operand', line=239)
W('04,3121', 0o77614, '', 'SET', kind='interp', line=240)
W('04,3122', 0o00470, '', '', 'UPDATFLG', kind='operand', line=241)
W('04,3123', 0o77776, 'P39P79', 'EXIT', kind='interp', line=242)
W('04,3124', 0o03152, '', 'TC', 'DSPLY81', 'FOR P39 AND P79', line=243)
W('04,3125', 0o51575, 'MAINRTN1', 'VLOAD', 'ABVAL', kind='interp', line=244)
W('04,3126', 0o03646, '', '', 'DELVEET3', kind='operand', line=245)
W('04,3127', 0o26635, '', 'STOVL', 'DELVTPI', 'DELTA V', kind='interp', line=246)
W('04,3130', 0o03640, '', '', 'VPASS4', kind='operand', line=247)
W('04,3131', 0o51451, '', 'VSU', 'ABVAL', kind='interp', line=248)
W('04,3132', 0o03620, '', '', 'VTPRIME', kind='operand', line=249)
W('04,3133', 0o26637, '', 'STOVL', 'DELVTPF', "DELTA V (FINAL) = V'T - VT", kind='interp', line=250)
W('04,3134', 0o03540, '', '', 'RACT3', kind='operand', line=251)
W('04,3135', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=252)
W('04,3136', 0o03612, '', '', 'VIPRIME', kind='operand', line=253)
W('04,3137', 0o45153, '', '', 'PERIAPO1', 'GET PERIGEE ALTITUDE', kind='operand', line=254)
W('04,3140', 0o77624, '', 'CALL', kind='interp', line=255)
W('04,3141', 0o45263, '', '', 'SHIFTR1', kind='operand', line=256)
W('04,3142', 0o02641, '', 'STORE', 'POSTTPI', kind='interp', line=257)
W('04,3143', 0o43014, '', 'BON', 'SET', kind='interp', line=258)
W('04,3144', 0o01311, '', '', 'FINALFLG', kind='operand', line=259)
W('04,3145', 0o11147, '', '', 'DSPLY58', kind='operand', line=260)
W('04,3146', 0o00470, '', '', 'UPDATFLG', kind='operand', line=261)
W('04,3147', 0o77776, 'DSPLY58', 'EXIT', kind='interp', line=262)
W('04,3150', 0o33301, '', 'CAF', 'V06N58SR', 'DISPLAY HP, DELTA V, DELTA V (FINAL)', line=263)
W('04,3151', 0o03263, '', 'TC', 'VNDSPLY', line=264)
W('04,3152', 0o33302, 'DSPLY81', 'CAF', 'V06N81SR', 'DISPLAY DELTA V (LV)', line=265)
W('04,3153', 0o03263, '', 'TC', 'VNDSPLY', line=266)
W('04,3154', 0o06006, '', 'TC', 'INTPRET', line=267)
W('04,3155', 0o77214, '', 'CLEAR', 'VLOAD', kind='interp', line=268)
W('04,3156', 0o01267, '', '', 'XDELVFLG', kind='operand', line=269)
W('04,3157', 0o03646, '', '', 'DELVEET3', kind='operand', line=270)
W('04,3160', 0o37646, '', 'STCALL', 'DELVSIN', kind='interp', line=271)
W('04,3161', 0o73002, '', '', 'VN1645', 'DISPLAY TRKMKCNT, TTOGO, +MGA', kind='operand', line=272)
W('04,3162', 0o52014, '', 'BON', 'GOTO', kind='interp', line=273)
W('04,3163', 0o04306, '', '', 'P39/79SW', kind='operand', line=274)
W('04,3164', 0o11203, '', '', 'P39/P79B', kind='operand', line=275)
W('04,3165', 0o11045, '', '', 'RECYCLE', kind='operand', line=276)

# STABLE ORBIT MIDCOURSE PROGRAM (P39 AND P79)
#
# MOD NO -1             LOG SECTION - STABLE ORBIT - P38-P39
# MOD BY RUDNICKI, S    DATE 25JAN68
#
# FUNCTIONAL DESCRIPTION
#
# P39 AND P79 CALCULATE THE REQUIRED DELTA V AND OTHER INITIAL
# CONDITIONS REQUIRED BY THE AGC TO MAKE A MIDCOURSE CORRECTION
# Page 530
# MANEUVER AFTER COMPLETING THE SOI MANEUVER BUT BEFORE MAKING
# THE SOR MANEUVER
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
# (1)  TRKMKCNT   NUMBER OF MARKS
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

W('04,3166', 0o04627, 'P39', 'TC', 'AVFLAGA', 'THIS VEHICLE ACTIVE', line=321)
W('04,3167', 0o00006, '', 'EXTEND', line=322)
W('04,3170', 0o31422, '', 'DCA', 'ATIGINC', line=323)
W('04,3171', 0o03175, '', 'TC', 'P39/P79A', line=324)
W('04,3172', 0o04642, 'P79', 'TC', 'AVFLAGP', 'OTHER VEHICLE ACTIVE', line=325)
W('04,3173', 0o00006, '', 'EXTEND', line=326)
W('04,3174', 0o31424, '', 'DCA', 'PTIGINC', line=327)
W('04,3175', 0o53764, 'P39/P79A', 'DXCH', 'KT', 'TIME TO PREPARE FOR BURN', line=328)
W('04,3176', 0o04647, '', 'TC', 'P20FLGON', 'SET UPDATFLG, TRACKFLG', line=329)
W('04,3177', 0o06006, '', 'TC', 'INTPRET', line=330)
W('04,3200', 0o45014, '', 'SET', 'CALL', kind='interp', line=331)
W('04,3201', 0o04066, '', '', 'P39/79SW', kind='operand', line=332)
W('04,3202', 0o10712, '', '', 'SELECTMU', 'SELECT MU, CLEAR FINALFLG, GO TO VN1645', kind='operand', line=333)
W('04,3203', 0o43234, 'P39/P79B', 'RTB', 'DAD', kind='interp', line=334)
W('04,3204', 0o45510, '', '', 'LOADTIME', kind='operand', line=335)
W('04,3205', 0o02364, '', '', 'KT', kind='operand', line=336)
W('04,3206', 0o03413, '', 'STORE', 'TIG', 'TIG = T (PRESENT) + PREPARATION TIME', kind='interp', line=337)
# Page531
W('04,3207', 0o34041, '', 'STCALL', 'TDEC1', 'PRECISION UPDATE ACTIVE AND PASSIVE', kind='interp', line=339)
W('04,3210', 0o45215, '', '', 'PRECSET', '      VEHICLES TO TIG', kind='operand', line=340)
W('04,3211', 0o77624, '', 'CALL', kind='interp', line=341)
W('04,3212', 0o74000, '', '', 'S34/35.1', 'GET UNIT NORMAL', kind='operand', line=342)
W('04,3213', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=343)
W('04,3214', 0o02615, '', '', 'TARGTIME', kind='operand', line=344)
W('04,3215', 0o11101, '', '', 'MAINRTNE', 'CALCULATE DELTA V AND DELTA V (LV)', kind='operand', line=345)

# .... PREC/TT ....
# SUBROUTINES USED
#
# PRECSET
# TIMETHET
# S34/35.1

W('04,3216', 0o71220, 'PREC/TT', 'STQ', 'DLOAD', kind='interp', line=354)
W('04,3217', 0o02367, '', '', 'RTRN', kind='operand', line=355)
W('04,3220', 0o03413, '', '', 'TIG', kind='operand', line=356)
W('04,3221', 0o34041, '', 'STCALL', 'TDEC1', 'PRECISION UPDATE ACTIVE AND PASSIVE', kind='interp', line=357)
W('04,3222', 0o45215, '', '', 'PRECSET', '      VEHICLES TO TIG', kind='operand', line=358)
W('04,3223', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=359)
W('04,3224', 0o03554, '', '', 'RPASS3', kind='operand', line=360)
W('04,3225', 0o57176, '', '', '0,2', kind='operand', line=361)
W('04,3226', 0o16657, '', 'STODL', 'RVEC', kind='interp', line=362)
W('04,3227', 0o03754, '', '', 'CENTANG', kind='operand', line=363)
W('04,3230', 0o71406, '', 'PUSH', 'COS', kind='interp', line=364)
W('04,3231', 0o16734, '', 'STODL', 'CSTH', kind='interp', line=365)
W('04,3232', 0o43156, '', 'SIN', 'SET', kind='interp', line=366)
W('04,3233', 0o03466, '', '', 'RVSW', kind='operand', line=367)
W('04,3234', 0o26732, '', 'STOVL', 'SNTH', kind='interp', line=368)
W('04,3235', 0o03562, '', '', 'VPASS3', kind='operand', line=369)
W('04,3236', 0o77657, '', 'VSR*', kind='interp', line=370)
W('04,3237', 0o57176, '', '', '0,2', kind='operand', line=371)
W('04,3240', 0o36746, '', 'STCALL', 'VVEC', 'GET TRANSFER TIME BASED ON CENTANG OF', kind='interp', line=372)
W('04,3241', 0o24744, '', '', 'TIMETHET', '      PASSIVE VEHICLE', kind='operand', line=373)
W('04,3242', 0o77624, '', 'CALL', kind='interp', line=374)
W('04,3243', 0o74000, '', '', 'S34/35.1', 'GET UNIT NORMAL', kind='operand', line=375)
W('04,3244', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=376)
W('04,3245', 0o00037, '', '', 'T', kind='operand', line=377)
W('04,3246', 0o02367, '', '', 'RTRN', kind='operand', line=378)
# .... INTRPVP ....
# SUBROUTINES USED
#
# CSMPREC
# LEMPREC

W('04,3247', 0o43020, 'INTRPVP', 'STQ', 'BOFF', 'PRECISION UPDATE PASSIVE VEHICLE TO', kind='interp', line=385)
W('04,3250', 0o02367, '', '', 'RTRN', '      TDEC1', kind='operand', line=386)
W('04,3251', 0o01352, '', '', 'AVFLAG', kind='operand', line=387)
W('04,3252', 0o11257, '', '', 'OTHERV', kind='operand', line=388)
W('04,3253', 0o77624, '', 'CALL', kind='interp', line=389)
# Page 532
W('04,3254', 0o27071, '', '', 'CSMPREC', kind='operand', line=391)
W('04,3255', 0o77650, '', 'GOTO', kind='interp', line=392)
W('04,3256', 0o02367, '', '', 'RTRN', kind='operand', line=393)
W('04,3257', 0o77624, 'OTHERV', 'CALL', kind='interp', line=394)
W('04,3260', 0o27105, '', '', 'LEMPREC', kind='operand', line=395)
W('04,3261', 0o77650, '', 'GOTO', kind='interp', line=396)
W('04,3262', 0o02367, '', '', 'RTRN', kind='operand', line=397)
# .... VNDSPLY ....
# SUBROUTINES USED
#
# BANKCALL
# GOFLASH
# GOTOPOOH

W('04,3263', 0o00006, 'VNDSPLY', 'EXTEND', '', 'FLASH DISPLAY', line=405)
W('04,3264', 0o23767, '', 'QXCH', 'RTRN', line=406)
W('04,3265', 0o55765, '', 'TS', 'VERBNOUN', line=407)
W('04,3266', 0o31765, '', 'CA', 'VERBNOUN', line=408)
W('04,3267', 0o04662, '', 'TCR', 'BANKCALL', line=409)
W('04,3270', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=410)
W('04,3271', 0o14106, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=411)
W('04,3272', 0o01767, '', 'TC', 'RTRN', 'PROCEED', line=412)
W('04,3273', 0o13266, '', 'TCF', '-5', 'RECYCLE', line=413)
W('04,3274', 0o01441, 'V06N33SR', 'VN', '0633', kind='data', line=414)
W('04,3275', 0o01467, 'V06N55SR', 'VN', '0655', kind='data', line=415)
W('04,3276', 0o01006, 'V04N06SR', 'VN', '0406', kind='data', line=416)
W('04,3277', 0o01471, 'V06N57SR', 'VN', '0657', kind='data', line=417)
W('04,3300', 0o01442, 'V06N34SR', 'VN', '0634', kind='data', line=418)
W('04,3301', 0o01472, 'V06N58SR', 'VN', '0658', kind='data', line=419)
W('04,3302', 0o01521, 'V06N81SR', 'VN', '0681', kind='data', line=420)

# *** END OF COMEKISS.020 ***
