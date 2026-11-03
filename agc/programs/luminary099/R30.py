"""R30.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/R30.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 712-722 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('R30', 'R30.agc', 'Luminary099', pages='712-722')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     R30.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        712-722
# Mod history:  2009-05-19 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2009-06-07 RSB  Removed a space between two components of
# a 2OCT that isn't legal in yaYUL.
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

# Page 712
# SUBROUTINE NAME:  V82CALL
# MOD NO: 0                                                             DATE: 16 FEB 67
# MOD BY: R. R. BAIRNSFATHER                                            LOG SECTION:  R30
# MOD NO: 1     MOD BY:  R. R. BAIRNSFATHER     DATE: 11 APR 67         SR30.1 CHANGED TO ALLOW MONITOR OPERN
# MOD NO: 2     MOD BY:  ALONSO                 DATE: 11 DEC 67         VB82 PROGRAM REWRITTEN
# MOD NO: 3     MOD BY:  ALONSO                 DATE: 26 MAR 68         PROG MOD TO HANDLE DIF EARTH/MOON SCALE
#
# NEW FUNCTIONAL DESCRIPTION:   CALLED BY VERB 82 ENTER.  PRIORITY 10.
# USED THROUGHOUT.              CALCULATE AND DISPLAY ORBITAL PARAMETERS
#
# 1.    IF AVERAGE G IS OFF:
# FLASH DISPLAY V04N06. R2 INDICATES WHICH SHIP'S STATE VECTOR IS
# TO BE UPDATED. INITIAL CHOICE IS THIS SHIP (R2=1). ASTRONAUT
# CAN CHANGE TO OTHER SHIP BY V22EXE, WHERE X NOT EQ 1.
# SELECTED STATE VECTOR UPDATED BY THISPREC (OTHPREC).
# CALLS SR30.1 (WHICH CALLS TFFCONMU + TFFRP/RA) TO CALCULATE
# RPER (PERIGEE RADIUS), RAPO (APOGEE RADIUS), HPER (PERIGEE
# HEIGHT ABOVE LAUNCH PAD OR LUNAR LANDING SITE), HARD (APOGEE
# HEIGHT AS ABOVE), TPER (TIME TO PERIGEE), TFF (TIME TO
# INTERSECT 300 KFT ABOVE PAD OR 35KFT ABOVE LANDING SITE).
# FLASH MONITOR V16N44 (HAPO, HPER, TFF).TFF IS -59M59S IF IT WAS
# NOT COMPUTABLE, OTHERWISE IT INCREMENTS ONCE PER SECOND.
# ASTRONAUT HAS OPTION TO MONITOR TPER BY KEYING IN N 32 E.
# DISPLAY IS IN HMS, IS NEGATIVE (AS WAS TFF), AND INCREMENTS
# ONCE PER SECOND ONLY IF TFF DISPLAY WAS -59M59S.
#
# 2.    IF AVERAGE G IS ON:
# CALLS SR30.1 APPROX EVERY TWO SECS.  STATE VECTOR IS ALWAYS
# FOR THIS VEHICLE. V82 DOES NOT DISTURB STATE VECTOR.  RESULTS
# OF SR30.1 ARE RAPO, RPER, HAPO, HPER, TPER, TFF.
# FLASH MONITOR V16N44 (HAPO, HPER, TFF).
# ADDENDUM: HAPO AND HPER SHOULD BE CHANGED TO READ HAPOX AND HPERX IN THE
# ABOVE REMARKS.
#
# CALLING SEQUENCE:  VERB 82 ENTER.
#
# SUBROUTINES CALLED:  SR30.1, GOXDSPF
# MAYBE - THISPREC , OTHPREC, LOADTIME, DELRSPL
# NORMAL EXIT MODES:  TC ENDEXT
#
# ALARMS:  NONE
#
# OUTPUT:  HAPOX        (-29) M
# HPERX        (-29) M
# RAPO         (-29) M EARTH
# (-27) M MOON
# RPER         (-29) M EARTH
# (-27) M MOON
# TFF          (-28) CS        CONTAINS NEGATIVE QUANTITY
# -TPER        (-28) CS        CONTAINS NEGATIVE QUANTITY
# Page 713
#
# ERASABLE INITIALIZATION REQUIRED: STATE VECTOR.
#
# DEBRIS:       QPRET, RONE, VONE,TFF/RTMU, HPERMIN, RPADTEM, V82EMFLG.
# MAYBE: TSTART82, V82FLAGS, TDEC1.

#   EBANK= HAPOX
#   BANK 31
#   SETLOC R30LOC
#   BANK
#   COUNT* $$/R30

W('22,3242', 0o06037, 'V82CALL', 'TC', 'INTPRET', line=95)
W('22,3243', 0o52014, '', 'BON', 'GOTO', kind='interp', line=96)
W('22,3244', 0o03712, '', '', 'AVEGFLAG', kind='operand', line=97)
W('22,3245', 0o45465, '', '', 'V82GON', 'IF AVERAGE G ON', kind='operand', line=98)
W('22,3246', 0o45247, '', '', 'V82GOFF', 'IF AVERAGE G OFF', kind='operand', line=99)

W('22,3247', 0o77776, 'V82GOFF', 'EXIT', '', 'ALLOW ASTRONAUT TO SELECT VEHICLE', kind='interp', line=101)
W('22,3250', 0o34752, '', 'CAF', 'TWO', 'DESIRED FOR ORBITAL PARAMETERS', line=102)
W('22,3251', 0o55051, '', 'TS', 'OPTIONX', 'CALCULATION AND DISPLAY.', line=103)
W('22,3252', 0o34753, '', 'CAF', 'ONE', line=104)
W('22,3253', 0o55052, '', 'TS', 'OPTIONX +1', line=105)
W('22,3254', 0o33316, '', 'CAF', 'OPTIONVN', 'V 04 N 06', line=106)
W('22,3255', 0o04616, '', 'TC', 'BANKCALL', line=107)
W('22,3256', 0o20334, '', 'CADR', 'GOXDSPF', kind='data', line=108)
W('22,3257', 0o05472, '', 'TC', 'ENDEXT', 'TERMINATE', line=109)
W('22,3260', 0o03262, '', 'TC', '+2', 'PROCEED', line=110)
W('22,3261', 0o03254, '', 'TC', '-5', 'DATA IN. OPTION1+1 = 1 FOR THIS VEHICLE.', line=111)
# UNEQ 1 FOR OTHER VEHICLE.
W('22,3262', 0o34750, '', 'CAF', 'BIT4', '80 MS', line=113)
W('22,3263', 0o05203, '', 'TC', 'WAITLIST', line=114)
#   EBANK= TFF
W('22,3264', 0o03430, '', '2CADR', 'TICKTEST', kind='data', line=116)
W('22,3265', 0o44064, kind='data', line=116)

W('22,3266', 0o00003, '', 'RELINT', line=118)
W('22,3267', 0o33320, 'V82GOFLP', 'CAF', 'TFFBANK', 'MAJOR RECYCLE LOOP ENTRY', line=119)
W('22,3270', 0o54003, '', 'TS', 'EBANK', line=120)
W('22,3271', 0o34755, '', 'CAF', 'ZERO', line=121)
W('22,3272', 0o55537, '', 'TS', 'V82FLAGS', 'ZERO FLAGS FOR TICKTEST, INHIBITS', line=122)
# DECREMENTING OF TFF AND -TPER.
W('22,3273', 0o35021, '', 'CAF', 'PRIO7', line=124)
W('22,3274', 0o05105, '', 'TC', 'FINDVAC', 'V82GOFF1 WILL EXECUTE STATE VECTOR', line=125)
#   EBANK= TFF  # UPDATE AND ORBIT CALCULATIONS FOR
W('22,3275', 0o03321, '', '2CADR', 'V82GOFF1', 'SELECTED VEHICLE ABOUT PROPER BODY.', kind='data', line=127)
W('22,3276', 0o44064, kind='data', line=127)

W('22,3277', 0o00003, '', 'RELINT', line=129)
W('22,3300', 0o36245, 'V82STALL', 'CAF', 'THREE', 'STALL IN THIS LOOP AND WITHOLD V 16 N 44', line=130)
# Page 714
W('22,3301', 0o71537, '', 'MASK', 'V82FLAGS', 'UNTIL STATE VECTOR UPDATE SETS ONE OF', line=132)
W('22,3302', 0o10000, '', 'CCS', 'A', 'OUR FLAG BITS.', line=133)
W('22,3303', 0o03310, '', 'TC', 'FLAGGON', 'EXIT FROM STALL LOOP.', line=134)
W('22,3304', 0o34777, '', 'CAF', '1SEC', line=135)
W('22,3305', 0o04616, '', 'TC', 'BANKCALL', line=136)
W('22,3306', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=137)
W('22,3307', 0o03300, '', 'TC', 'V82STALL', line=138)

W('22,3310', 0o33317, 'FLAGGON', 'CAF', 'V16N44', 'MONITOR HAPO,HPER,TFF.', line=140)
W('22,3311', 0o04616, '', 'TC', 'BANKCALL', line=141)
W('22,3312', 0o20334, '', 'CADR', 'GOXDSPF', kind='data', line=142)
W('22,3313', 0o05563, '', 'TC', 'B5OFF', 'TERM  THIS TELLS TICKTEST TO KILL ITSELF', line=143)
W('22,3314', 0o05563, '', 'TC', 'B5OFF', 'PROCEED  DITTO', line=144)
W('22,3315', 0o03267, '', 'TC', 'V82GOFLP', 'RECYCLE  RECOMPUTE STATE VECT + DISPLAY', line=145)

W('22,3316', 0o01014, 'OPTIONVN', 'VN', '412', kind='data', line=147)
W('22,3317', 0o04054, 'V16N44', 'VN', '1644', kind='data', line=148)
W('22,3320', 0o02140, 'TFFBANK', 'ECADR', 'TFF', kind='data', line=149)

W('22,3321', 0o06037, 'V82GOFF1', 'TC', 'INTPRET', line=151)
W('22,3322', 0o77634, '', 'RTB', kind='interp', line=152)
W('22,3323', 0o21573, '', '', 'LOADTIME', kind='operand', line=153)
W('22,3324', 0o00041, '', 'STORE', 'TDEC1', 'TIME FOR STATE VECTOR UPDATE.', kind='interp', line=154)
W('22,3325', 0o02205, '', 'STORE', 'TSTART82', 'TIME FOR INTERNAL USE.', kind='interp', line=155)
W('22,3326', 0o77776, '', 'EXIT', kind='interp', line=156)
W('22,3327', 0o41052, '', 'CS', 'OPTIONX +1', '1 FOR THIS VEHICLE, NOT 1 FOR OTHER.', line=157)
W('22,3330', 0o64753, '', 'AD', 'ONE', line=158)
W('22,3331', 0o00006, '', 'EXTEND', line=159)
W('22,3332', 0o13356, '', 'BZF', 'THISSHIP', line=160)
W('22,3333', 0o06037, 'OTHSHIP', 'TC', 'INTPRET', line=161)
W('22,3334', 0o77624, '', 'CALL', '', 'CALL STATE VECTOR UPDATE FOR OTHER SHIP.', kind='interp', line=162)
W('22,3335', 0o27043, '', '', 'OTHPREC', kind='operand', line=163)
W('22,3336', 0o77775, 'BOTHSHIP', 'VLOAD', '', 'MOVE RESULTS INTO TFFCONIC STORAGE AREAS', kind='interp', line=164)
W('22,3337', 0o00001, '', '', 'RATT', ' TO BE CALLED BY SR30.1.', kind='operand', line=165)
W('22,3340', 0o26207, '', 'STOVL', 'RONE', 'RATT AT (-29)M FOR EARTH OR MOON', kind='interp', line=166)
W('22,3341', 0o00007, '', '', 'VATT', kind='operand', line=167)
W('22,3342', 0o02215, '', 'STORE', 'VONE', ' VATT AT (-7)M/CS FOR EARTH OR MOON', kind='interp', line=168)
W('22,3343', 0o77743, '', 'DLOAD*', kind='interp', line=169)
W('22,3344', 0o73774, '', '', '1/RTMUE,2', ' X2 IS 0 FOR EARTH CENTERED STATE VEC', kind='operand', line=170)
W('22,3345', 0o00037, '', 'STORE', 'TFF/RTMU', ' X2 IS 2 FOR MOON', kind='interp', line=171)
W('22,3346', 0o77743, '', 'DLOAD*', '', 'AS LEFT BY THISPREC OR OTHPREC.', kind='interp', line=172)
W('22,3347', 0o72411, '', '', 'MINPERE,2', kind='operand', line=173)
W('22,3350', 0o02201, '', 'STORE', 'HPERMIN', '  TFFRTMU, HPERMIN AND RPADTEM ARE ALL', kind='interp', line=174)
W('22,3351', 0o46135, '', 'SLOAD', 'BHIZ', 'EARTH/MOON PARAMETERS AS SET HERE.', kind='interp', line=175)
W('22,3352', 0o00050, '', '', 'X2', kind='operand', line=176)
W('22,3353', 0o45367, '', '', 'EARTHPAD', kind='operand', line=177)
W('22,3354', 0o77650, '', 'GOTO', kind='interp', line=178)
W('22,3355', 0o45373, '', '', 'MOONPAD', kind='operand', line=179)
# Page 715
W('22,3356', 0o06037, 'THISSHIP', 'TC', 'INTPRET', line=181)
W('22,3357', 0o77624, '', 'CALL', '', 'CALL STATE VECTOR UPDATE FOR THIS SHIP.', kind='interp', line=182)
W('22,3360', 0o27057, '', '', 'THISPREC', kind='operand', line=183)
W('22,3361', 0o77650, '', 'GOTO', kind='interp', line=184)
W('22,3362', 0o45336, '', '', 'BOTHSHIP', kind='operand', line=185)

# THE FOLLOWING CONSTANTS ARE PAIRWISE INDEXED. DO NOT SEPARATE PAIRS.

W('22,3363', 0o00001, 'MINPERM', '2DEC', '10668 B-27', '35 KFT MIN PERIGEE HEIGHT FOR MOON(-27)M', kind='data', line=189)
W('22,3364', 0o11530, kind='data', line=189)

W('22,3365', 0o00002, 'MINPERE', '2DEC', '91440 B-29', '300 KFT (-29)M FOR EARTH', kind='data', line=191)
W('22,3366', 0o31230, kind='data', line=191)

W('22,3367', 0o43145, 'EARTHPAD', 'DLOAD', 'CLRGO', ' PAD 37-B RADIUS.  SCALED AT (-29)M.', kind='interp', line=193)
W('22,3370', 0o06315, '', '', 'RPAD', kind='operand', line=194)
W('22,3371', 0o03635, '', '', 'V82EMFLG', ' INDICATE EARTH SCALING FOR SR30.1', kind='operand', line=195)
W('22,3372', 0o45377, '', '', 'BOTHPAD', kind='operand', line=196)

W('22,3373', 0o51575, 'MOONPAD', 'VLOAD', 'ABVAL', 'COMPUTE MOON PAD RADIUS FROM RLS VECTOR.', kind='interp', line=198)
W('22,3374', 0o02023, '', '', 'RLS', ' SCALED AT (-27)M.', kind='operand', line=199)
W('22,3375', 0o77614, '', 'SET', kind='interp', line=200)
W('22,3376', 0o03475, '', '', 'V82EMFLG', ' INDICATE MOON SCALING FOR SR30.1', kind='operand', line=201)
W('22,3377', 0o36203, 'BOTHPAD', 'STCALL', 'RPADTEM', kind='interp', line=202)
W('22,3400', 0o45551, '', '', 'SR30.1', 'CALCULATE ORBITAL PARAMETERS', kind='operand', line=203)
W('22,3401', 0o45234, '', 'RTB', 'DSU', kind='interp', line=204)
W('22,3402', 0o21573, '', '', 'LOADTIME', kind='operand', line=205)
W('22,3403', 0o02205, '', '', 'TSTART82', 'PRESENT TIME - TIME V82GOFF1 BEGAN', kind='operand', line=206)
W('22,3404', 0o02205, '', 'STORE', 'TSTART82', '               SAVE IT', kind='interp', line=207)
W('22,3405', 0o53145, '', 'DLOAD', 'BZE', 'SR30.1 SETS -TPER=0 IF HPER L/', kind='interp', line=208)
W('22,3406', 0o02143, '', '', '-TPER', ' HPERMIN (300 OR 35) KFT.', kind='operand', line=209)
W('22,3407', 0o45420, '', '', 'TICKTIFF', '(-TPER = 0)', kind='operand', line=210)
W('22,3410', 0o43345, 'TICKTPER', 'DLOAD', 'DAD', '(-TPER NON ZERO)  TFF WAS NOT COMPUTED.', kind='interp', line=211)
W('22,3411', 0o02143, '', '', '-TPER', 'BUT WAS SET TO 59M59S.DONT TICK TFF, DO', kind='operand', line=212)
W('22,3412', 0o02205, '', '', 'TSTART82', 'TICK -TPER. DISPLAY BOTH.', kind='operand', line=213)
W('22,3413', 0o02143, '', 'STORE', '-TPER', '-TPER CORRECTED FOR TIME SINCE V82GOFF1', kind='interp', line=214)
W('22,3414', 0o77776, '', 'EXIT', '', 'BEGAN.', kind='interp', line=215)
W('22,3415', 0o34753, '', 'CAF', 'BIT1', line=216)
W('22,3416', 0o55537, '', 'TS', 'V82FLAGS', 'INFORMS TICKTEST TO INCREMENT ONLY -TPER', line=217)
W('22,3417', 0o05155, '', 'TC', 'ENDOFJOB', line=218)

W('22,3420', 0o43345, 'TICKTIFF', 'DLOAD', 'DAD', '(-TPER=0)  TFF WAS COMPUTED.TICK TFF.', kind='interp', line=220)
W('22,3421', 0o02141, '', '', 'TFF', 'DO NOT TICK -TPER.DISPLAY TFF, BUT NOT', kind='operand', line=221)
W('22,3422', 0o02205, '', '', 'TSTART82', '-TPER.', kind='operand', line=222)
W('22,3423', 0o02141, '', 'STORE', 'TFF', 'TFF CORRECTED FOR TIME SINCE V82GOFF1', kind='interp', line=223)
W('22,3424', 0o77776, '', 'EXIT', '', 'BEGAN.', kind='interp', line=224)
W('22,3425', 0o34752, '', 'CAF', 'BIT2', line=225)
W('22,3426', 0o55537, '', 'TS', 'V82FLAGS', 'INFORMS TICKTEST TO INCREMENT ONLY TFF.', line=226)
W('22,3427', 0o05155, '', 'TC', 'ENDOFJOB', line=227)

# Page 716
W('22,3430', 0o34747, 'TICKTEST', 'CAF', 'BIT5', 'THIS WAITLIST PROGRAM PERPETUATES ITSELF', line=230)
W('22,3431', 0o71044, '', 'MASK', 'EXTVBACT', 'ONCE A SEC UNTIL BIT 5 OF EXTVBACT =0.', line=231)
W('22,3432', 0o10000, '', 'CCS', 'A', line=232)
W('22,3433', 0o03441, '', 'TC', 'DOTICK', line=233)
W('22,3434', 0o37713, '', 'CAF', 'PRIO25', line=234)
W('22,3435', 0o05072, '', 'TC', 'NOVAC', 'TERMINATE V 82.CANT CALL ENDEXT IN RUPT.', line=235)
#   EBANK= EXTVBACT
W('22,3436', 0o05472, '', '2CADR', 'ENDEXT', kind='data', line=237)
W('22,3437', 0o04062, kind='data', line=237)

W('22,3440', 0o05261, '', 'TC', 'TASKOVER', line=239)
W('22,3441', 0o34777, 'DOTICK', 'CAF', '1SEC', 'RE-REQUEST TICKTEST.', line=240)
W('22,3442', 0o05203, '', 'TC', 'WAITLIST', line=241)
#   EBANK= TFF
W('22,3443', 0o03430, '', '2CADR', 'TICKTEST', kind='data', line=243)
W('22,3444', 0o44064, kind='data', line=243)

W('22,3445', 0o36245, '', 'CAF', 'THREE', line=245)
W('22,3446', 0o71537, '', 'MASK', 'V82FLAGS', line=246)
W('22,3447', 0o50000, '', 'INDEX', 'A', line=247)
W('22,3450', 0o03451, '', 'TC', '+1', line=248)
W('22,3451', 0o05261, '', 'TC', 'TASKOVER', 'IF NO FLAGBITS SET DONT CHANGE TFF OR', line=249)
# -TPER, BUT CONTINUE LOOP.
W('22,3452', 0o03460, '', 'TC', 'TPERTICK', 'ONLY BIT 1 SET. INCR -TPER BY 1 SEC.', line=251)
W('22,3453', 0o34777, 'TFFTICK', 'CAF', '1SEC', 'ONLY BIT 2 SET. INCR TFF BY 1 SEC.', line=252)
W('22,3454', 0o54001, '', 'TS', 'L', line=253)
W('22,3455', 0o34755, '', 'CAF', 'ZERO', line=254)
W('22,3456', 0o21541, '', 'DAS', 'TFF', line=255)
W('22,3457', 0o05261, '', 'TC', 'TASKOVER', line=256)
W('22,3460', 0o34777, 'TPERTICK', 'CAF', '1SEC', line=257)
W('22,3461', 0o54001, '', 'TS', 'L', line=258)
W('22,3462', 0o34755, '', 'CAF', 'ZERO', line=259)
W('22,3463', 0o21543, '', 'DAS', '-TPER', line=260)
W('22,3464', 0o05261, '', 'TC', 'TASKOVER', line=261)

# Page 717
W('22,3465', 0o77776, 'V82GON', 'EXIT', '', ' AVERAGE G ON. USE CURRENT STATE VECTOR', kind='interp', line=264)
# FOR ORBITAL PARAMETER CALCULATIONS.
W('22,3466', 0o35021, '', 'CAF', 'PRIO7', 'LESS THAN LAMBERT', line=266)
W('22,3467', 0o05105, '', 'TC', 'FINDVAC', 'V82GON1 WILL PERFORM ORBIT CALCULATIONS', line=267)
#   EBANK= TFF  # ABOUT PROPER BODY APPROX ONCE PER SEC.
W('22,3470', 0o03503, '', '2CADR', 'V82GON1', kind='data', line=269)
W('22,3471', 0o44064, kind='data', line=269)

W('22,3472', 0o00003, '', 'RELINT', line=271)
W('22,3473', 0o10067, '', 'CCS', 'NEWJOB', 'WITHOLD V16 N44 UNTIL FIRST ORBIT CALC', line=272)
W('22,3474', 0o05122, '', 'TC', 'CHANG1', 'IS DONE. NOTE: V82GON1 (PRIO7, FINDVAC', line=273)
# JOB) IS COMPLETED BEFORE V82GON (PRIO7,
# NOVAC JOB).
W('22,3475', 0o33317, 'V82REDSP', 'CAF', 'V16N44', 'MONITOR HAPO, HPER, TFF', line=276)
W('22,3476', 0o04616, '', 'TC', 'BANKCALL', line=277)
W('22,3477', 0o20334, '', 'CADR', 'GOXDSPF', kind='data', line=278)
W('22,3500', 0o05563, '', 'TC', 'B5OFF', 'TERM THIS TELLS V82GON1 TO KILL ITSELF.', line=279)
W('22,3501', 0o05563, '', 'TC', 'B5OFF', 'PROC DITTO.', line=280)
W('22,3502', 0o03475, '', 'TC', 'V82REDSP', 'RECYCLE', line=281)

W('22,3503', 0o06037, 'V82GON1', 'TC', 'INTPRET', 'THIS EXEC PROGRAM PERPETUATES ITSELF', line=283)
# ONCE A SEC UNTIL BIT 5 OF EXTVBACT =0.
W('22,3504', 0o52175, '', 'VLOAD', 'GOTO', 'HOLDS OFF CCS NEWJOB BETWEEN RN AND', kind='interp', line=285)
W('22,3505', 0o01221, '', '', 'RN', '  VN FETCH SO RN , VN ARE FROM SAME', kind='operand', line=286)
W('22,3506', 0o45507, '', '', 'NEXTLINE', '  STATE VECTOR UPDATE.', kind='operand', line=287)
W('22,3507', 0o26207, 'NEXTLINE', 'STOVL', 'RONE', ' RN AT (-29)M FOR EARTH OR MOON', kind='interp', line=288)
W('22,3510', 0o01227, '', '', 'VN', kind='operand', line=289)
W('22,3511', 0o02215, '', 'STORE', 'VONE', 'VN AT (-7)M/CS FOR EARTH OR MOON', kind='interp', line=290)
W('22,3512', 0o52014, '', 'BON', 'GOTO', kind='interp', line=291)
W('22,3513', 0o04304, '', '', 'MOONTHIS', 'FLAG INDICATES BODY ABOUT WHICH ORBITAL', kind='operand', line=292)
W('22,3514', 0o45516, '', '', 'MOONGON', '   CALCULATIONS ARE TO BE PERFORMED.', kind='operand', line=293)
W('22,3515', 0o45527, '', '', 'EARTHGON', '  IF SET - MOON , IF RESET - EARTH.', kind='operand', line=294)

W('22,3516', 0o71214, 'MOONGON', 'SET', 'DLOAD', kind='interp', line=296)
W('22,3517', 0o03475, '', '', 'V82EMFLG', 'INDICATE MOON SCALING FOR SR30.1', kind='operand', line=297)
W('22,3520', 0o04001, '', '', '1/RTMUM', 'LUNAR PARAMETERS LOADED HERE FOR SR30.1', kind='operand', line=298)
W('22,3521', 0o14037, '', 'STODL', 'TFF/RTMU', kind='interp', line=299)
W('22,3522', 0o05364, '', '', 'MINPERM', kind='operand', line=300)
W('22,3523', 0o26201, '', 'STOVL', 'HPERMIN', kind='interp', line=301)
W('22,3524', 0o02023, '', '', 'RLS', ' SCALED AT (-27)M.', kind='operand', line=302)
W('22,3525', 0o52046, '', 'ABVAL', 'GOTO', kind='interp', line=303)
W('22,3526', 0o45536, '', '', 'V82GON2', kind='operand', line=304)
W('22,3527', 0o71214, 'EARTHGON', 'CLEAR', 'DLOAD', kind='interp', line=305)
W('22,3530', 0o03675, '', '', 'V82EMFLG', 'INDICATE EARTH SCALING FOR SR30.1', kind='operand', line=306)
W('22,3531', 0o04003, '', '', '1/RTMUE', 'EARTH PARAMETERS LOADED HERE FOR SR30.1', kind='operand', line=307)
W('22,3532', 0o14037, '', 'STODL', 'TFF/RTMU', kind='interp', line=308)
W('22,3533', 0o05366, '', '', 'MINPERE', kind='operand', line=309)
W('22,3534', 0o16201, '', 'STODL', 'HPERMIN', kind='interp', line=310)
W('22,3535', 0o06315, '', '', 'RPAD', kind='operand', line=311)
W('22,3536', 0o36203, 'V82GON2', 'STCALL', 'RPADTEM', 'COMMON CODE FOR EARTH & MOON.', kind='interp', line=312)
W('22,3537', 0o45551, '', '', 'SR30.1', kind='operand', line=313)
# Page 718
W('22,3540', 0o77776, '', 'EXIT', kind='interp', line=315)
W('22,3541', 0o34747, 'V82GON3', 'CAF', 'BIT5', line=316)
W('22,3542', 0o71044, '', 'MASK', 'EXTVBACT', 'SEE IF ASTRONAUT HAS SIGNALLED TERMINATE', line=317)
W('22,3543', 0o00006, '', 'EXTEND', line=318)
W('22,3544', 0o15472, '', 'BZF', 'ENDEXT', 'YES, TERMINATE VB 82 LOOP', line=319)
W('22,3545', 0o34777, '', 'CAF', '1SEC', line=320)
W('22,3546', 0o04616, '', 'TC', 'BANKCALL', 'WAIT ONE SECOND BEFORE REPEATING', line=321)
W('22,3547', 0o01735, '', 'CADR', 'DELAYJOB', '  ORBITAL PARAMETER COMPUTATION.', kind='data', line=322)
W('22,3550', 0o03503, '', 'TC', 'V82GON1', line=323)

S('SPLRET', 'equals', 0o55541, line=325)

# Page 719
# SUBROUTINE NAME: SR30.1
# MOD NO: 0                                                             DATE: 16 FEB 67
# MOD BY: R. R. BAIRNSFATHER                                            LOG SECTION: R32
# MOD NO: 1     MOD BY: R. R. BAIRNSFATHER      DATE: 11 APR 67         SR30.1 CHANGED TO ALLOW MONITOR OPERN
# MOD NO: 2     MOD BY: R. R. BAIRNSFATHER      DATE: 14 APR 67         ADD OVFL CK FOR RAPO
# MOD NO: 3     MOD BY ALONSO                   DATE: 11 DEC 67         SUBROUTINE REWRITTEN
# MOD NO: 4     MOD BY ALONSO                   DATE: 26 MAR 68         PROG MOD TO HANDLE DIF EARTH/MOON SCALE
# MOD NO: 5     MOD BY: R. R. BAIRNSFATHER      DATE: 6 AUG 68          OVFL CK FOR HAPO & HPER. VOIDS MOD #2.
#
# NEW FUNCTIONAL DESCRIPTION:  ORBITAL PARAMETERS DISPLAY FOR NOUNS 32 AND 44.
# SR30.1 CALLS TFFCONMU AND TFFRP/RA TO CALCULATE RPER (PERIGEE RADIUS),
# RAPO (APOGEE RADIUS), HPER (PERIGEE HEIGHT ABOVE LAUNCH PAD OR LUNAR
# LANDING SITE), HAPO (APOGEE HEIGHT AS ABOVE), TPER (TIME TO PERIGEE),
# TFF (TIME TO INTERSECT 300 KFT ABOVE PAD OR 35KFT ABOVE LANDING SITE).
# IF HPER IS GREATER THAN OR EQUAL TO HPERMIN, CALCULATES TPER AND STORES
# NEGATIVE IN -TPER.  OTHERWISE STORES +0 IN -TPER.  WHENEVER TPER IS
# CALCULATED, TFF IS NOT COMPUTABLE AND DEFAULTS TO -59MIN 59SEC.  IF HAPO
# WOULD EXCEED 9999.9 NM, IT IS LIMITED TO THAT VALUE FOR DISPLAY.
#
# ADDENDUM:     HAPO AND HPER SHOULD BE CHANGED TO READ HAPOX AND HPERX IN THE
# ABOVE REMARKS.
#
# CALLING SEQUENCE:     CALL
# SR30.1
#
# SUBROUTINES CALLED:   TFFCONMU, TFFRP/RA, CALCTPER, CALCTFF
#
# NORMAL EXIT MODE:     CALLING LINE +1 (STILL IN INTERPRETIVE MODE)
#
# ALARMS:       NONE
#
# OUTPUT:       RAPO    (-29) M EARTH   APOGEE RADIUS   EARTH CENTERED COORD.
# (-27) M MOON                    MOON CENTERED COORD.
# RPER    (-29) M EARTH   PERIGEE RADIUS  EARTH CENTERED COORD.
# (-27) M MOON                    MOON CENTERED COORD.
# HAPOX   (-29) M         APOGEE ALTITUDE ABOVE PAD OR LAND. SITE MAX VALUE LIMITED TO 9999.9 NM.
# HPERX   (-29) M         PERIGEE ALT. ABOVE PAD OR LAND. SITE    MAX VALUE LIMITED TO 9999.9 NM.
# TFF     (-28) CS        TIME TO 300KFT OR 35KFT ALTITUDE
# -TPER   (-28) CS        TIME TO PERIGEE
#
# ERASABLE INITIALIZATION REQUIRED --
# TFF/RTMU        (+17) EARTH     RECIPROCAL OF PROPER GRAV CONSTANT FOR
# (+14) MOON      EARTH OR MOON = 1/SQRT(MU).
# RONE            (-29) M         STATE VECTOR
# VONE            (-7)  M/CS      STATE VECTOR
# RPADTEM         (-29) M EARTH   RADIUS OF LAUNCH PAD OR LUNAR LANDING
# (-27) M MOON    SITE.
# HPERMIN         (-29) M EARTH   (300 OR 35) KFT MINIMUM PERIGEE ALTITUDE
# (-27) M MOON    ABOVE LAUNCH PAD OR LUNAR LANDING SITE.
# V82EMFLG        (INT SW BIT)    RESET FOR EARTH, SET FOR MOON.
#
# DEBRIS:       QPREG, PDL, S2

# Page 720
#   COUNT* $$/SR30S

W('22,3551', 0o44001, 'SR30.1', 'SETPD', 'STQ', 'INITIALIZE PUSHDOWN LIST.', kind='interp', line=384)
W('22,3552', 0o00001, '', '', '0', kind='operand', line=385)
W('22,3553', 0o00051, '', '', 'S2', kind='operand', line=386)
# SR30.1 INPUT: RONE AT (-29)M EARTH/MOON
# VONE AT (-7)M/CS
# TFFCONMU, TFFRP/RA, CALCTPER, AND CALCTFF
# CALLS REQUIRE:
# EARTH CENTERED (NO RESCALING REQUIRED)
# RONE SCALED TO B-29 M
# VONE SCALED TO B-7  M/CS
# MOON CENTERED (RESCALING REQUIRED)
# RONE SCALED TO B-27 M
# VONE SCALED TO B-5  M/CS
W('22,3554', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=397)
W('22,3555', 0o03755, '', '', 'V82EMFLG', 'OFF FOR EARTH, ON FOR MOON.', kind='operand', line=398)
W('22,3556', 0o45565, '', '', 'TFFCALLS', kind='operand', line=399)
W('22,3557', 0o02207, '', '', 'RONE', kind='operand', line=400)
W('22,3560', 0o77752, '', 'VSL2', kind='interp', line=401)
W('22,3561', 0o26207, '', 'STOVL', 'RONE', kind='interp', line=402)
W('22,3562', 0o02215, '', '', 'VONE', kind='operand', line=403)
W('22,3563', 0o77752, '', 'VSL2', kind='interp', line=404)
W('22,3564', 0o02215, '', 'STORE', 'VONE', kind='interp', line=405)
W('22,3565', 0o77624, 'TFFCALLS', 'CALL', kind='interp', line=406)
W('22,3566', 0o57361, '', '', 'TFFCONMU', kind='operand', line=407)
W('22,3567', 0o77624, '', 'CALL', '', 'TFFRP/RA COMPUTES RAPO,RPER.', kind='interp', line=408)
W('22,3570', 0o57427, '', '', 'TFFRP/RA', kind='operand', line=409)
# RETURNS WITH RAPO IN D(MPAC).
W('22,3571', 0o77625, '', 'DSU', kind='interp', line=411)
W('22,3572', 0o02203, '', '', 'RPADTEM', kind='operand', line=412)
W('22,3573', 0o64414, '', 'BOFF', 'SR2R', 'NEED HAPO AT (-29)M FOR DISPLAY.', kind='interp', line=413)
# IF MOON CENTERED, RESCALE FROM (-27)M.
# IF EARTH CENTERED ALREADY AT (-29)M.
W('22,3574', 0o03755, '', '', 'V82EMFLG', 'OFF FOR EARTH, ON FOR MOON.', kind='operand', line=416)
W('22,3575', 0o45576, '', '', '+1', kind='operand', line=417)
W('22,3576', 0o77624, '', 'CALL', '', 'IF RAPO > MAXNM, SET RAPO =9999.9 NM.', kind='interp', line=418)
W('22,3577', 0o45636, '', '', 'MAXCHK', 'OTHERWISE STORE (RAPO-RPADTEM) IN HAPO.', kind='operand', line=419)
W('22,3600', 0o16120, 'STORHAPO', 'STODL', 'HAPOX', kind='interp', line=420)
W('22,3601', 0o00017, '', '', 'RPER', kind='operand', line=421)
W('22,3602', 0o77625, '', 'DSU', kind='interp', line=422)
W('22,3603', 0o02203, '', '', 'RPADTEM', 'GIVES HPER AT (-29)M EARTH, (-27)M MOON.', kind='operand', line=423)
W('22,3604', 0o00161, '', 'STORE', 'MPAC +4', 'SAVE THIS FOR COMPARISON TO HPERMIN.', kind='interp', line=424)
W('22,3605', 0o64414, '', 'BOFF', 'SR2R', 'NEED HPER AT (-29)M FOR DISPLAY.', kind='interp', line=425)
# IF MOON CENTERED, RESCALE FROM (-27)M.
# IF EARTH CENTERED ALREADY AT (-29)M.
W('22,3606', 0o03755, '', '', 'V82EMFLG', 'OFF FOR EARTH, ON FOR MOON.', kind='operand', line=428)
W('22,3607', 0o45610, '', '', '+1', kind='operand', line=429)
W('22,3610', 0o77624, '', 'CALL', '', 'IF HPER > MAXNM, SET HPER = 9999.9 NM.', kind='interp', line=430)
W('22,3611', 0o45636, '', '', 'MAXCHK', kind='operand', line=431)
# Page 721
W('22,3612', 0o16122, 'STORHPER', 'STODL', 'HPERX', 'STORE (RPER - RPADTEM) INTO HPERX.', kind='interp', line=433)
W('22,3613', 0o00161, '', '', 'MPAC +4', kind='operand', line=434)
W('22,3614', 0o51025, '', 'DSU', 'BPL', 'HPERMIN AT (-29)M FOR EARTH, (-27)M MOON', kind='interp', line=435)
W('22,3615', 0o02201, '', '', 'HPERMIN', 'IF HPER L/   HPERMIN (300 OR 35)KFT,', kind='operand', line=436)
W('22,3616', 0o45622, '', '', 'DOTPER', ' THEN ZERO INTO -TPER.', kind='operand', line=437)
W('22,3617', 0o52145, '', 'DLOAD', 'GOTO', '  OTHERWISE CALCULATE TPER.', kind='interp', line=438)
W('22,3620', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=439)
W('22,3621', 0o45626, '', '', 'SKIPTPER', kind='operand', line=440)
W('22,3622', 0o45145, 'DOTPER', 'DLOAD', 'CALL', kind='interp', line=441)
W('22,3623', 0o00017, '', '', 'RPER', kind='operand', line=442)
W('22,3624', 0o57465, '', '', 'CALCTPER', kind='operand', line=443)
W('22,3625', 0o77676, '', 'DCOMP', '', 'TPER IS PUT NEG INTO -TPER.', kind='interp', line=444)
W('22,3626', 0o16143, 'SKIPTPER', 'STODL', '-TPER', kind='interp', line=445)
W('22,3627', 0o02201, '', '', 'HPERMIN', 'HPERMIN AT (-29)M FOR EARTH, (-27)M MOON', kind='operand', line=446)
W('22,3630', 0o45015, '', 'DAD', 'CALL', kind='interp', line=447)
W('22,3631', 0o02203, '', '', 'RPADTEM', 'RPADTEM AT (-29)M FOR EARTH, (-27)M MOON', kind='operand', line=448)
W('22,3632', 0o57470, '', '', 'CALCTFF', 'GIVES 59M59S FOR TFF IF HPER G/', kind='operand', line=449)
W('22,3633', 0o77676, '', 'DCOMP', '', '  HPERMIN + RPADTEM. (TPER WAS NON ZERO)', kind='interp', line=450)
W('22,3634', 0o36141, '', 'STCALL', 'TFF', 'OTHERWISE COMPUTES TFF.       (GOTO)', kind='interp', line=451)
W('22,3635', 0o00051, '', '', 'S2', kind='operand', line=452)

W('22,3636', 0o51025, 'MAXCHK', 'DSU', 'BPL', 'IF C(MPAC) > 9999.9 NM. MPAC = 9999.9 NM.', kind='interp', line=454)
W('22,3637', 0o05646, '', '', 'MAXNM', kind='operand', line=455)
W('22,3640', 0o45643, '', '', '+3', 'OTHERWISE C(MPAC) = B(MPAC).', kind='operand', line=456)
W('22,3641', 0o43415, '', 'DAD', 'RVQ', kind='interp', line=457)
W('22,3642', 0o05646, '', '', 'MAXNM', kind='operand', line=458)
W('22,3643', 0o43545, '', 'DLOAD', 'RVQ', '(USED BY P30 - P37 ALSO)', kind='interp', line=459)
W('22,3644', 0o05646, '', '', 'MAXNM', kind='operand', line=460)

W('22,3645', 0o01065, 'MAXNM', '2OCT', '0106505603', kind='data', line=462)
W('22,3646', 0o05603, kind='data', line=462)

# Page 722 (empty page)
