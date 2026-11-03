"""R31.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/R31.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 703-708 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('R31', 'R31.agc', 'Luminary099', pages='703-708')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     R31.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        703-708
# Mod history:  2009-05-19 RSB  Adapted from the corresponding
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

# Page 703
#   BANK 40
#   SETLOC R31LOC
#   BANK

#   COUNT* $$/R31

W('40,3674', 0o35015, 'R31CALL', 'CAF', 'PRIO3', line=36)
W('40,3675', 0o05105, '', 'TC', 'FINDVAC', line=37)
#   EBANK= SUBEXIT
W('40,3676', 0o03121, '', '2CADR', 'V83CALL', kind='data', line=39)
W('40,3677', 0o76067, kind='data', line=39)

W('40,3700', 0o05221, 'DSPDELAY', 'TC', 'FIXDELAY', line=41)
W('40,3701', 0o00144, '', 'DEC', '100', kind='data', line=42)
W('40,3702', 0o31044, '', 'CA', 'EXTVBACT', line=43)
W('40,3703', 0o74740, '', 'MASK', 'BIT12', line=44)
W('40,3704', 0o00006, '', 'EXTEND', line=45)
W('40,3705', 0o13700, '', 'BZF', 'DSPDELAY', line=46)

W('40,3706', 0o35017, '', 'CAF', 'PRIO5', line=48)
W('40,3707', 0o05072, '', 'TC', 'NOVAC', line=49)
#   EBANK= TSTRT
W('40,3710', 0o03113, '', '2CADR', 'DISPN5X', kind='data', line=51)
W('40,3711', 0o76067, kind='data', line=51)

W('40,3712', 0o15261, '', 'TCF', 'TASKOVER', line=53)

#   BANK 37
#   SETLOC R31
#   BANK
#   COUNT* $$/R31

W('37,3113', 0o33407, 'DISPN5X', 'CAF', 'V16N54', line=60)
W('37,3114', 0o04616, '', 'TC', 'BANKCALL', line=61)
W('37,3115', 0o20334, '', 'CADR', 'GOMARKF', kind='data', line=62)
W('37,3116', 0o05563, '', 'TC', 'B5OFF', line=63)
W('37,3117', 0o05563, '', 'TC', 'B5OFF', line=64)
W('37,3120', 0o13113, '', 'TCF', 'DISPN5X', line=65)

W('37,3121', 0o40103, 'V83CALL', 'CS', 'FLAGWRD7', 'TEST AVERAGE G FLAG', line=67)
W('37,3122', 0o74747, '', 'MASK', 'AVEGFBIT', line=68)
W('37,3123', 0o00006, '', 'EXTEND', line=69)
W('37,3124', 0o13377, '', 'BZF', 'MUNG?', 'ON - TEST MUNFLAG', line=70)

W('37,3125', 0o40104, '', 'CS', 'FLAGWRD8', line=72)
W('37,3126', 0o74744, '', 'MASK', 'SURFFBIT', line=73)
W('37,3127', 0o00006, '', 'EXTEND', line=74)
W('37,3130', 0o13403, '', 'BZF', 'ONEBASE', 'ON SURFACE - BYPASS LEMPREC', line=75)

W('37,3131', 0o06037, '', 'TC', 'INTPRET', 'EXTRAPOLATE BOTH STATE VECTORS', line=77)
W('37,3132', 0o77634, '', 'RTB', kind='interp', line=78)
# Page 704
W('37,3133', 0o21573, '', '', 'LOADTIME', kind='operand', line=80)
W('37,3134', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=81)
W('37,3135', 0o27057, '', '', 'LEMPREC', 'PRECISION BASE VECTOR FOR LM', kind='operand', line=82)
W('37,3136', 0o77775, '', 'VLOAD', kind='interp', line=83)
W('37,3137', 0o00017, '', '', 'RATT1', kind='operand', line=84)
W('37,3140', 0o26170, '', 'STOVL', 'BASETHP', kind='interp', line=85)
W('37,3141', 0o00025, '', '', 'VATT1', kind='operand', line=86)
W('37,3142', 0o16105, '', 'STODL', 'BASETHV', kind='interp', line=87)
W('37,3143', 0o00015, '', '', 'TAT', kind='operand', line=88)
W('37,3144', 0o02114, 'DOCMBASE', 'STORE', 'BASETIME', 'PRECISION BASE VECTOR FOR CM', kind='interp', line=89)
W('37,3145', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=90)
W('37,3146', 0o27043, '', '', 'CSMPREC', kind='operand', line=91)
W('37,3147', 0o77775, '', 'VLOAD', kind='interp', line=92)
W('37,3150', 0o00017, '', '', 'RATT1', kind='operand', line=93)
W('37,3151', 0o26140, '', 'STOVL', 'BASEOTP', kind='interp', line=94)
W('37,3152', 0o00025, '', '', 'VATT1', kind='operand', line=95)
W('37,3153', 0o02120, '', 'STORE', 'BASEOTV', kind='interp', line=96)
W('37,3154', 0o77776, '', 'EXIT', kind='interp', line=97)

W('37,3155', 0o40103, 'REV83', 'CS', 'FLAGWRD7', line=99)
W('37,3156', 0o74747, '', 'MASK', 'AVEGFBIT', line=100)
W('37,3157', 0o00006, '', 'EXTEND', line=101)
W('37,3160', 0o13326, '', 'BZF', 'GETRVN', 'IF AVEGFLAG SET, USE RN,VN', line=102)

W('37,3161', 0o40104, '', 'CS', 'FLAGWRD8', line=104)
W('37,3162', 0o74744, '', 'MASK', 'SURFFBIT', line=105)
W('37,3163', 0o00006, '', 'EXTEND', line=106)
W('37,3164', 0o13370, '', 'BZF', 'R31SURF', 'IF ON SURFACE,USE LEMAREC', line=107)

W('37,3165', 0o06037, '', 'TC', 'INTPRET', 'DO CONIC EXTRAPOLATION FOR BOTH VEHICLES', line=109)
W('37,3166', 0o77634, '', 'RTB', kind='interp', line=110)
W('37,3167', 0o21573, '', '', 'LOADTIME', kind='operand', line=111)
W('37,3170', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=112)
W('37,3171', 0o27414, '', '', 'INTSTALL', kind='operand', line=113)
W('37,3172', 0o43175, '', 'VLOAD', 'CLEAR', kind='interp', line=114)
W('37,3173', 0o02170, '', '', 'BASETHP', kind='operand', line=115)
W('37,3174', 0o00263, '', '', 'MOONFLAG', kind='operand', line=116)
W('37,3175', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=117)
W('37,3176', 0o02105, '', '', 'BASETHV', kind='operand', line=118)
W('37,3177', 0o15543, '', 'STODL', 'VCV', kind='interp', line=119)
W('37,3200', 0o02114, '', '', 'BASETIME', kind='operand', line=120)
W('37,3201', 0o43014, '', 'BOF', 'SET', 'GET APPROPRIATE MOONFLAG SETTING', kind='interp', line=121)
W('37,3202', 0o04344, '', '', 'MOONTHIS', kind='operand', line=122)
W('37,3203', 0o77205, '', '', '+2', kind='operand', line=123)
W('37,3204', 0o00063, '', '', 'MOONFLAG', kind='operand', line=124)
W('37,3205', 0o77614, '', 'SET', kind='interp', line=125)
W('37,3206', 0o01473, '', '', 'INTYPFLG', 'CONIC EXTRAP.', kind='operand', line=126)
W('37,3207', 0o35517, '', 'STCALL', 'TET', kind='interp', line=127)
W('37,3210', 0o27107, '', '', 'INTEGRVS', 'INTEGRATION --- AT LAST---', kind='operand', line=128)
W('37,3211', 0o77775, 'OTHCONIC', 'VLOAD', kind='interp', line=129)
# Page 705
W('37,3212', 0o00001, '', '', 'RATT', kind='operand', line=131)
W('37,3213', 0o26207, '', 'STOVL', 'RONE', kind='interp', line=132)
W('37,3214', 0o00007, '', '', 'VATT', kind='operand', line=133)
W('37,3215', 0o36215, '', 'STCALL', 'VONE', 'GET SET FOR CONIC EXTRAP.,OTHER.', kind='interp', line=134)
W('37,3216', 0o27414, '', '', 'INTSTALL', kind='operand', line=135)
W('37,3217', 0o71214, '', 'SET', 'DLOAD', kind='interp', line=136)
W('37,3220', 0o01473, '', '', 'INTYPFLG', kind='operand', line=137)
W('37,3221', 0o00015, '', '', 'TAT', kind='operand', line=138)
W('37,3222', 0o00041, 'OTHINT', 'STORE', 'TDEC1', kind='interp', line=139)
W('37,3223', 0o43175, '', 'VLOAD', 'CLEAR', kind='interp', line=140)
W('37,3224', 0o02140, '', '', 'BASEOTP', kind='operand', line=141)
W('37,3225', 0o00263, '', '', 'MOONFLAG', kind='operand', line=142)
W('37,3226', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=143)
W('37,3227', 0o02120, '', '', 'BASEOTV', kind='operand', line=144)
W('37,3230', 0o15543, '', 'STODL', 'VCV', kind='interp', line=145)
W('37,3231', 0o02114, '', '', 'BASETIME', kind='operand', line=146)
W('37,3232', 0o43014, '', 'BOF', 'SET', kind='interp', line=147)
W('37,3233', 0o04344, '', '', 'MOONTHIS', kind='operand', line=148)
W('37,3234', 0o77236, '', '', '+2', kind='operand', line=149)
W('37,3235', 0o00063, '', '', 'MOONFLAG', kind='operand', line=150)
W('37,3236', 0o35517, '', 'STCALL', 'TET', kind='interp', line=151)
W('37,3237', 0o27107, '', '', 'INTEGRVS', kind='operand', line=152)
W('37,3240', 0o52375, 'COMPDISP', 'VLOAD', 'VSU', kind='interp', line=153)
W('37,3241', 0o00001, '', '', 'RATT', kind='operand', line=154)
W('37,3242', 0o02207, '', '', 'RONE', kind='operand', line=155)
W('37,3243', 0o65234, '', 'RTB', 'PDDL', kind='interp', line=156)
W('37,3244', 0o21724, '', '', 'NORMUNX1', 'UNIT(RANGE) TO PD 0-5', kind='operand', line=157)
W('37,3245', 0o00045, '', '', '36D', kind='operand', line=158)
W('37,3246', 0o77657, '', 'SL*', '', 'RESCALE AFTER NORMUNIT', kind='interp', line=159)
W('37,3247', 0o20201, '', '', '0,1', kind='operand', line=160)
W('37,3250', 0o26201, '', 'STOVL', 'RANGE', 'SCALED 2(29)M', kind='interp', line=161)
W('37,3251', 0o00007, '', '', 'VATT', kind='operand', line=162)
W('37,3252', 0o50251, '', 'VSU', 'DOT', '(VCM- VLM).UNIT(LOS). PD=0', kind='interp', line=163)
W('37,3253', 0o02215, '', '', 'VONE', kind='operand', line=164)
W('37,3254', 0o77752, '', 'SL1', '', 'SCALED 2(7)M/CS', kind='interp', line=165)
W('37,3255', 0o26203, '', 'STOVL', 'RRATE', kind='interp', line=166)
W('37,3256', 0o02207, '', '', 'RONE', kind='operand', line=167)
W('37,3257', 0o63256, '', 'UNIT', 'PDVL', 'UNIT(R) TO PD 0-5', kind='interp', line=168)
W('37,3260', 0o06514, '', '', 'UNITZ', kind='operand', line=169)
W('37,3261', 0o77624, '', 'CALL', kind='interp', line=170)
W('37,3262', 0o47661, '', '', 'CDU*NBSM', kind='operand', line=171)
W('37,3263', 0o41505, '', 'VXM', 'PUSH', 'UNIT (Z)/4 TO PD 6-11', kind='interp', line=172)
W('37,3264', 0o01734, '', '', 'REFSMMAT', kind='operand', line=173)
W('37,3265', 0o72431, '', 'VPROJ', 'VSL2', 'UNIT(P)=UNIT(UZ -(UZ)PROJ(UR))', kind='interp', line=174)
W('37,3266', 0o00001, '', '', '0D', kind='operand', line=175)
W('37,3267', 0o53445, '', 'BVSU', 'UNIT', kind='interp', line=176)
W('37,3270', 0o00007, '', '', '6D', kind='operand', line=177)
W('37,3271', 0o47315, '', 'PDVL', 'VXV', 'UNIT(P) TO PD 12-17', kind='interp', line=178)
W('37,3272', 0o00001, '', '', '0D', 'UNIT(RL)', kind='operand', line=179)
W('37,3273', 0o02215, '', '', 'VONE', kind='operand', line=180)
# Page 706
W('37,3274', 0o50235, '', 'VXV', 'DOT', '(UR * VL)*UR . U(P)', kind='interp', line=182)
W('37,3275', 0o00001, '', '', '0D', kind='operand', line=183)
W('37,3276', 0o00015, '', '', '12D', kind='operand', line=184)
W('37,3277', 0o77715, '', 'PDVL', '', 'SIGN TO 12-13 , LOAD U(P)', kind='interp', line=185)
W('37,3300', 0o75241, '', 'DOT', 'SIGN', kind='interp', line=186)
W('37,3301', 0o00007, '', '', '6D', kind='operand', line=187)
W('37,3302', 0o00015, '', '', '12D', kind='operand', line=188)
W('37,3303', 0o65512, '', 'SL2', 'ACOS', 'ARCCOS(UP.UZ(SIGN))', kind='interp', line=189)
W('37,3304', 0o26205, '', 'STOVL', 'RTHETA', kind='interp', line=190)
W('37,3305', 0o00001, '', '', '0D', kind='operand', line=191)
W('37,3306', 0o51041, '', 'DOT', 'BPL', 'IF UR.UZ NEG,', kind='interp', line=192)
W('37,3307', 0o00007, '', '', '6D', '  RTHETA = 1 - RTHETA', kind='operand', line=193)
W('37,3310', 0o77315, '', '', '+5', kind='operand', line=194)
W('37,3311', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=195)
W('37,3312', 0o06530, '', '', 'DPPOSMAX', kind='operand', line=196)
W('37,3313', 0o02205, '', '', 'RTHETA', kind='operand', line=197)
W('37,3314', 0o02205, '', 'STORE', 'RTHETA', kind='interp', line=198)
W('37,3315', 0o77776, '', 'EXIT', kind='interp', line=199)

W('37,3316', 0o34747, '', 'CA', 'BIT5', line=201)
W('37,3317', 0o71044, '', 'MASK', 'EXTVBACT', line=202)
W('37,3320', 0o00006, '', 'EXTEND', '', 'IF ANSWERED,', line=203)
W('37,3321', 0o15472, '', 'BZF', 'ENDEXT', '       TERMINATE', line=204)

W('37,3322', 0o41044, '', 'CS', 'EXTVBACT', line=206)
W('37,3323', 0o74740, '', 'MASK', 'BIT12', line=207)
W('37,3324', 0o27044, '', 'ADS', 'EXTVBACT', 'SET BIT 12', line=208)
W('37,3325', 0o13155, '', 'TCF', 'REV83', 'AND START AGAIN.', line=209)

W('37,3326', 0o37710, 'GETRVN', 'CA', 'PRIO22', 'INHIBIT SERVICER', line=211)
W('37,3327', 0o05146, '', 'TC', 'PRIOCHNG', line=212)
W('37,3330', 0o06037, '', 'TC', 'INTPRET', line=213)
W('37,3331', 0o40375, '', 'VLOAD', 'SETPD', kind='interp', line=214)
W('37,3332', 0o01221, '', '', 'RN', 'LM STATE VECTOR IN RN,VN', kind='operand', line=215)
W('37,3333', 0o00001, '', '', '0', kind='operand', line=216)
W('37,3334', 0o26207, '', 'STOVL', 'RONE', kind='interp', line=217)
W('37,3335', 0o01227, '', '', 'VN', kind='operand', line=218)
W('37,3336', 0o26215, '', 'STOVL', 'VONE', 'LOAD R(CSM),V(CSM) IN CASE MUNFLAG SET', kind='interp', line=219)
W('37,3337', 0o01726, '', '', 'V(CSM)', '(TO INSURE TIME COMPATABILITY)', kind='operand', line=220)
W('37,3340', 0o65315, '', 'PDVL', 'PDDL', kind='interp', line=221)
W('37,3341', 0o01720, '', '', 'R(CSM)', kind='operand', line=222)
W('37,3342', 0o01235, '', '', 'PIPTIME', kind='operand', line=223)
W('37,3343', 0o77776, '', 'EXIT', kind='interp', line=224)
W('37,3344', 0o35015, '', 'CA', 'PRIO3', line=225)
W('37,3345', 0o05146, '', 'TC', 'PRIOCHNG', line=226)
W('37,3346', 0o06037, '', 'TC', 'INTPRET', line=227)
W('37,3347', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=228)
W('37,3350', 0o03347, '', '', 'MUNFLAG', kind='operand', line=229)
W('37,3351', 0o77363, '', '', 'GETRVN2', 'IF MUNFLAG RESET, DO CM DELTA PRECISION', kind='operand', line=230)
# Page 707
W('37,3352', 0o60505, '', 'VXM', 'VSR4', 'CHANGE TO REFERENCE SYSTEM AND RESCALE', kind='interp', line=232)
W('37,3353', 0o01734, '', '', 'REFSMMAT', kind='operand', line=233)
W('37,3354', 0o77715, '', 'PDVL', '', 'R TO PD 0-5', kind='interp', line=234)
W('37,3355', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=235)
W('37,3356', 0o01734, '', '', 'REFSMMAT', kind='operand', line=236)
W('37,3357', 0o40206, '', 'PUSH', 'SETPD', 'V TO PD 5-11', kind='interp', line=237)
W('37,3360', 0o00001, '', '', '0', kind='operand', line=238)
W('37,3361', 0o77650, '', 'GOTO', kind='interp', line=239)
W('37,3362', 0o77240, '', '', 'COMPDISP', kind='operand', line=240)

W('37,3363', 0o77624, 'GETRVN2', 'CALL', kind='interp', line=242)
W('37,3364', 0o27414, '', '', 'INTSTALL', kind='operand', line=243)
W('37,3365', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=244)
W('37,3366', 0o01673, '', '', 'INTYPFLG', 'PREC EXTRAP FOR OTHER', kind='operand', line=245)
W('37,3367', 0o77222, '', '', 'OTHINT', kind='operand', line=246)
W('37,3370', 0o06037, 'R31SURF', 'TC', 'INTPRET', line=247)
W('37,3371', 0o77634, '', 'RTB', '', 'LM IS ON SURFACE, SO PRECISION', kind='interp', line=248)
W('37,3372', 0o21573, '', '', 'LOADTIME', 'INTEGRATION USES PLANETARY INERTIAL', kind='operand', line=249)
W('37,3373', 0o34041, '', 'STCALL', 'TDEC1', 'ORIENTATION SUBROUTINE', kind='interp', line=250)
W('37,3374', 0o27057, '', '', 'LEMPREC', kind='operand', line=251)
W('37,3375', 0o77650, '', 'GOTO', '', 'DO CSM CONIC', kind='interp', line=252)
W('37,3376', 0o77211, '', '', 'OTHCONIC', kind='operand', line=253)
W('37,3377', 0o40102, 'MUNG?', 'CS', 'FLAGWRD6', line=254)
W('37,3400', 0o74744, '', 'MASK', 'MUNFLBIT', line=255)
W('37,3401', 0o00006, '', 'EXTEND', line=256)
W('37,3402', 0o13326, '', 'BZF', 'GETRVN', 'IF MUNFLAG SET, CSM BASE NOT NEEDED', line=257)

W('37,3403', 0o06037, 'ONEBASE', 'TC', 'INTPRET', 'GET CSM BASE VECTOR', line=259)
W('37,3404', 0o52034, '', 'RTB', 'GOTO', kind='interp', line=260)
W('37,3405', 0o21573, '', '', 'LOADTIME', kind='operand', line=261)
W('37,3406', 0o77144, '', '', 'DOCMBASE', kind='operand', line=262)

W('37,3407', 0o04066, 'V16N54', 'VN', '1654', kind='data', line=264)

# Page 708 (empty page)
