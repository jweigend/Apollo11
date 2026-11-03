"""R30.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/R30.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 514-524 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('R30', 'R30.agc', 'Comanche055', pages='514-524')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     R30.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        514-524
# Mod history:  2009-05-09 HG    Started adapting from the Colossus249/ file
# of the same name, using Comanche055 page
# images 0514.jpg - 0524.jpg.
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

# Page 514
# SUBROUTINE NAME:  V82CALL
# MOD NO: 0                                     DATE: 16 FEB 67
# MOD BY: R. R. BAIRNSFATHER                    LOG SECTION:  R30
# MOD NO: 1     MOD BY:  R. R. BAIRNSFATHER     DATE: 11 APR 67         SR30.1 CHANGED TO ALLOW MONITOR OPERN
# MOD NO: 2     MOD BY:  ALONSO                 DATE: 11 DEC 67         VB82 PROGRAM REWRITTEN
# MOD NO: 3     MOD BY:  ALONSO                 DATE: 26 MAR 68         PROG MOD TO HANDLE DIF EARTH/MOON SCALE
#
# NEW FUNCTIONAL DESCRIPTION:   CALLED BY VERB 82 ENTER.  PRIORITY 10.
# USED THROUGHOUT.              CALCULATE AND DISPLAY ORBITAL PARAMETERS
#
# 1.    IF AVERAGE G IS OFF:
# FLASH DISPLAY V04N06.  R2 INDICATES WHICH SHIP'S STATE VECTOR IS
# TO BE UPDATED.  INITIAL CHOICE IS THIS SHIP (R2=1).  ASTRONAUT
# CAN CHANGE TO OTHER SHIP BY V22EXE. WHERE X IS NOT EQ 1.
# SELECTED STATE VECTOR UPDATED BY THISPREC (OTHPREC).
# CALLS SR30.1 (WHICH CALLS TFFCONMU + TFFRP/RA) TO CALCULATE
# RPER (PERIGEE RADIUS), RAPO (APOGEE RADIUS), HPER (PERIGEE
# HEIGHT ABOVE LAUNCH PAD OR LAUNAR LANDING SITE), HARD (APOGEE
# HEIGHT AS ABOVE), TPER (TIME TO PERIGEE), TFF (TIME TO
# INTERSECT 300 KFT ABOVE PAD OR 35KFT ABOVE LANDING SITE).
# FLASH MONITOR V16N44 (HAPO, HPER, TFF).  TFF IS -59MS59S IF IT WAS
# NOT COMPUTABLE, OTHERWISE IT INCREMENTS ONCE PER SECOND.
# ASTRONAUT HAS OPTION TO MONITOR TPER BY KEYING IN N 32 E.
# DISPLAY IS IN HMS, IS NEGATIVE (AS WAS TFF), AND INCREMENTS
# ONCE PER SECOND ONLY IF TFF DISPLAY WAS -59M59S.
# 2.    IF AVERAGE G IS ON:
# CALLS SR30.1 APPROX EVERY TWO SECS.  STATE VECTOR IS ALWAYS
# FOR THIS VEHICLE.  V82 DOES NOT DISTURB STATE VECTOR.  RESULTS
# OF SR30.1 ARE RAPO, RPER, HAPO, HPER, TPER, TFF.
# FLASH MONITOR V16N44 (HAPO, HPER, TFF).
# IF MODE IS P11, THEN CALL DELRSPL SO ASTRONAUT CAN MONITOR
# RESULTS BY N50E.  SPLASH COMPUTATION DONE ONCE PER TWO SECS.

# ADDENDUM:  HAPO AND HPER SHOULD BE CHANGED TO READ HAPOX AND HPERX IN THE
# ABOVE REMARKS.
#
# CALLING SEQUENCE: VERB 82 ENTER.
#
# SUBROUTINES CALLED:   SR30.1, GOXDSPF
# MAYBE -- THISPREC, OTHPREC, LOADTIME, DELRSPL
#
# NORMAL EXIT MODES:  TC ENDEXT
#
# ALARMS:  NONE
#
# OUTPUT:       HAPOX   (-29) M
# HPERX   (-29) M
# RAPO    (-29) M EARTH
# (-27) M MOON
# Page 515
# RPER    (-29) M EARTH
# (-27) M MOON
# TFF     (-28) CS        CONTAINS NEGATIVE QUANTITY
# -TPER   (-28) CS        CONTAINS NEGATIVE QUANTITY
# RSP-RREC(-29) M         IF DELRSPL CALLED
#
# ERASABLE INITIALIZATION REQUIRED: STATE VECTOR.
#
# DEBRIS:       QPRET, RONE, VONE,TFF/RTMU, HPERMIN, RPADTEM, V82EMFLG.
# MAYBE:  TSTART82, V82FLAGS, TDEC1.

#   EBANK= HAPOX
#   BANK 31
#   SETLOC R30LOC
#   BANK
#   COUNT* $$/R30

W('23,2332', 0o06006, 'V82CALL', 'TC', 'INTPRET', line=99)
W('23,2333', 0o52014, '', 'BON', 'GOTO', kind='interp', line=100)
W('23,2334', 0o00716, '', '', 'AVEGFLAG', kind='operand', line=101)
W('23,2335', 0o46566, '', '', 'V82GON', 'IF AVERAGE G ON', kind='operand', line=102)
W('23,2336', 0o46337, '', '', 'V82GOFF', 'IF AVERAGE G OFF', kind='operand', line=103)

W('23,2337', 0o77776, 'V82GOFF', 'EXIT', '', 'ALLOW ASTRONAUT TO SELECT VEHICLE', kind='interp', line=105)
W('23,2340', 0o35016, '', 'CAF', 'TWO', 'DESIRED FOR ORBITAL PARAMETERS', line=106)
W('23,2341', 0o55051, '', 'TS', 'OPTIONX', line=107)
W('23,2342', 0o35017, '', 'CAF', 'ONE', line=108)
W('23,2343', 0o55052, '', 'TS', 'OPTIONX +1', line=109)
W('23,2344', 0o32406, '', 'CAF', 'OPTIONVN', 'V 04 N 06', line=110)
W('23,2345', 0o04662, '', 'TC', 'BANKCALL', line=111)
W('23,2346', 0o20561, '', 'CADR', 'GOXDSPF', kind='data', line=112)
W('23,2347', 0o05534, '', 'TC', 'ENDEXT', 'TERMINATE', line=113)
W('23,2350', 0o02352, '', 'TC', '+2', 'PROCEED', line=114)
W('23,2351', 0o02344, '', 'TC', '-5', 'DATA IN.  OPTIONX +1 = 1 FOR THIS VEHIC.', line=115)
# UNEQ 1 FOR OTHER VEHICLE.
W('23,2352', 0o35014, '', 'CAF', 'BIT4', '80 MS', line=117)
W('23,2353', 0o05245, '', 'TC', 'WAITLIST', line=118)
#   EBANK= TFF
W('23,2354', 0o02531, '', '2CADR', 'TICKTEST', kind='data', line=120)
W('23,2355', 0o46064, kind='data', line=120)

W('23,2356', 0o00003, '', 'RELINT', line=122)
W('23,2357', 0o32410, 'V82GOFLP', 'CAF', 'TFFBANK', 'MAJOR RECYCLE LOOP ENTRY', line=123)
W('23,2360', 0o54003, '', 'TS', 'EBANK', line=124)
W('23,2361', 0o35021, '', 'CAF', 'ZERO', line=125)
W('23,2362', 0o55742, '', 'TS', 'V82FLAGS', 'ZERO FLAGS FOR TICKTEST, INHIBITS', line=126)
# DECREMENTING OF TFF AND -TPER.
W('23,2363', 0o35063, '', 'CAF', 'PRIO7', line=128)
W('23,2364', 0o05147, '', 'TC', 'FINDVAC', 'V82GOFF1 WILL EXECUTE STATE VECTOR', line=129)
# Page 516
#   EBANK= TFF  # UPDATE AND ORBIT CALCULATIONS FOR
W('23,2365', 0o02411, '', '2CADR', 'V82GOFF1', 'SELECTED VEHICLE ABOUT PROPER BODY.', kind='data', line=132)
W('23,2366', 0o46064, kind='data', line=132)

W('23,2367', 0o00003, '', 'RELINT', line=134)
W('23,2370', 0o36214, 'V82STALL', 'CAF', 'THREE', 'STALL IN THIS LOOP AND WITHOLD V 16 N 44', line=135)
W('23,2371', 0o71742, '', 'MASK', 'V82FLAGS', 'UNTIL STATE VECTOR UPDATE SETS ONE OF', line=136)
W('23,2372', 0o10000, '', 'CCS', 'A', 'OUR FLAG BITS.', line=137)
W('23,2373', 0o02400, '', 'TC', 'FLAGGON', 'EXIT FROM STALL LOOP.', line=138)
W('23,2374', 0o35041, '', 'CAF', '1SEC', line=139)
W('23,2375', 0o04662, '', 'TC', 'BANKCALL', line=140)
W('23,2376', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=141)
W('23,2377', 0o02370, '', 'TC', 'V82STALL', line=142)

W('23,2400', 0o32407, 'FLAGGON', 'CAF', 'V16N44', 'MONITOR HAPO,HPER,TFF.', line=144)
W('23,2401', 0o04662, '', 'TC', 'BANKCALL', line=145)
W('23,2402', 0o20561, '', 'CADR', 'GOXDSPF', kind='data', line=146)
W('23,2403', 0o05625, '', 'TC', 'B5OFF', 'TERM  THIS TELLS TICKTEST TO KILL ITSELF', line=147)
W('23,2404', 0o05625, '', 'TC', 'B5OFF', 'PROCEED  DITTO', line=148)
W('23,2405', 0o02357, '', 'TC', 'V82GOFLP', 'RECYCLE  RECOMPUTE STATE VECT + DISPLAY', line=149)

W('23,2406', 0o01014, 'OPTIONVN', 'VN', '0412', kind='data', line=151)
W('23,2407', 0o04054, 'V16N44', 'VN', '1644', kind='data', line=152)
W('23,2410', 0o02343, 'TFFBANK', 'ECADR', 'TFF', kind='data', line=153)

W('23,2411', 0o06006, 'V82GOFF1', 'TC', 'INTPRET', line=155)
W('23,2412', 0o77634, '', 'RTB', kind='interp', line=156)
W('23,2413', 0o45510, '', '', 'LOADTIME', kind='operand', line=157)
W('23,2414', 0o00041, '', 'STORE', 'TDEC1', 'TIME FOR STATE VECTOR UPDATE.', kind='interp', line=158)
W('23,2415', 0o02325, '', 'STORE', 'TSTART82', 'TIME FOR INTERNAL USE.', kind='interp', line=159)
W('23,2416', 0o77776, '', 'EXIT', kind='interp', line=160)
W('23,2417', 0o41052, '', 'CS', 'OPTIONX +1', '1 FOR THIS VEHICLE, NOT 1 FOR OTHER', line=161)
W('23,2420', 0o65017, '', 'AD', 'ONE', line=162)
W('23,2421', 0o00006, '', 'EXTEND', line=163)
W('23,2422', 0o12446, '', 'BZF', 'THISSHIP', line=164)
W('23,2423', 0o06006, 'OTHSHIP', 'TC', 'INTPRET', line=165)
W('23,2424', 0o77624, '', 'CALL', '', 'CALL STATE VECTOR UPDATE FOR OTHER SHIP.', kind='interp', line=166)
W('23,2425', 0o27105, '', '', 'OTHPREC', kind='operand', line=167)
W('23,2426', 0o77775, 'BOTHSHIP', 'VLOAD', '', 'MOVE RESULTS INTO TFFCONIC STORAGE AREAS', kind='interp', line=168)
W('23,2427', 0o00001, '', '', 'RATT', 'TO BE CALLED BY SR30.1.', kind='operand', line=169)
W('23,2430', 0o26327, '', 'STOVL', 'RONE', 'RATT AT (-29)M FOR EARTH OR MOON', kind='interp', line=170)
W('23,2431', 0o00007, '', '', 'VATT', kind='operand', line=171)
W('23,2432', 0o02335, '', 'STORE', 'VONE', 'VATT AT (-7)M/CS FOR EARTH OR MOON', kind='interp', line=172)
W('23,2433', 0o77743, '', 'DLOAD*', kind='interp', line=173)
W('23,2434', 0o71321, '', '', '1/RTMUE,2', 'X2 IS 0 FOR EARTH CENTERED STATE VEC', kind='operand', line=174)
W('23,2435', 0o00037, '', 'STORE', 'TFF/RTMU', 'X2 IS 2 FOR MOON', kind='interp', line=175)
W('23,2436', 0o77743, '', 'DLOAD*', '', 'AS LEFT BY THISPREC OR OTHPREC.', kind='interp', line=176)
W('23,2437', 0o71315, '', '', 'MINPERE,2', kind='operand', line=177)
W('23,2440', 0o02321, '', 'STORE', 'HPERMIN', 'TFFRTMU, HPERMIN, AND RPADTEM ARE ALL', kind='interp', line=178)
W('23,2441', 0o46135, '', 'SLOAD', 'BHIZ', 'EARTH/MOON PARAMETERS AS SET HERE.', kind='interp', line=179)
# Page 517
W('23,2442', 0o00050, '', '', 'X2', kind='operand', line=181)
W('23,2443', 0o46463, '', '', 'EARTHPAD', kind='operand', line=182)
W('23,2444', 0o77650, '', 'GOTO', kind='interp', line=183)
W('23,2445', 0o46467, '', '', 'MOONPAD', kind='operand', line=184)
W('23,2446', 0o06006, 'THISSHIP', 'TC', 'INTPRET', line=185)
W('23,2447', 0o77624, '', 'CALL', '', 'CALL STATE VECTOR UPDATE FOR THIS SHIP.', kind='interp', line=186)
W('23,2450', 0o27071, '', '', 'THISPREC', kind='operand', line=187)
W('23,2451', 0o77650, '', 'GOTO', kind='interp', line=188)
W('23,2452', 0o46426, '', '', 'BOTHSHIP', kind='operand', line=189)

# THE FOLLOWING CONSTANTS ARE PAIRWISE INDEXED.  DO NOT SEPARATE PAIRS.

W('23,2453', 0o27533, '1/RTMUM', '2DEC*', '.45162595 E-4 B14*', kind='data', line=193)
W('23,2454', 0o07571, kind='data', line=193)
W('23,2455', 0o25004, '1/RTMUE', '2DEC*', '.50087529 E-5 B17*', kind='data', line=194)
W('23,2456', 0o06702, kind='data', line=194)

W('23,2457', 0o00001, 'MINPERM', '2DEC', '10668 B-27', '35 KFT MIN PERIGEE HEIGHT FOR MOON(-27)M', kind='data', line=196)
W('23,2460', 0o11530, kind='data', line=196)
W('23,2461', 0o00002, 'MINPERE', '2DEC', '91440 B-29', '300 KFT (-29)M FOR EARTH', kind='data', line=197)
W('23,2462', 0o31230, kind='data', line=197)

W('23,2463', 0o43145, 'EARTHPAD', 'DLOAD', 'CLRGO', 'PAD 37-B RADIUS.  SCALED AT (-29)M.', kind='interp', line=199)
W('23,2464', 0o05152, '', '', 'RPAD', kind='operand', line=200)
W('23,2465', 0o04622, '', '', 'V82EMFLG', 'INDICATE EARTH SCALING FOR SR30.1', kind='operand', line=201)
W('23,2466', 0o46473, '', '', 'BOTHPAD', kind='operand', line=202)

W('23,2467', 0o51575, 'MOONPAD', 'VLOAD', 'ABVAL', 'COMPUTE MOON PAD RADIUS FROM RLS VECTOR.', kind='interp', line=204)
W('23,2470', 0o02026, '', '', 'RLS', 'SCALED AT (-27)M.', kind='operand', line=205)
W('23,2471', 0o77614, '', 'SET', kind='interp', line=206)
W('23,2472', 0o04462, '', '', 'V82EMFLG', 'INDICATE MOON SCALING FOR SR30.1', kind='operand', line=207)
W('23,2473', 0o36323, 'BOTHPAD', 'STCALL', 'RPADTEM', kind='interp', line=208)
W('23,2474', 0o46667, '', '', 'SR30.1', 'CALCULATE ORBITAL PARAMETERS', kind='operand', line=209)
W('23,2475', 0o77776, '', 'EXIT', kind='interp', line=210)
W('23,2476', 0o31011, '', 'CA', 'MODREG', 'ARE WE IN P00', line=211)
W('23,2477', 0o00006, '', 'EXTEND', line=212)
W('23,2500', 0o12645, '', 'BZF', 'CANDEL', 'YES, DO DELRSPL', line=213)
W('23,2501', 0o06006, 'SPLRET1', 'TC', 'INTPRET', line=214)
W('23,2502', 0o45234, '', 'RTB', 'DSU', kind='interp', line=215)
W('23,2503', 0o45510, '', '', 'LOADTIME', kind='operand', line=216)
W('23,2504', 0o02325, '', '', 'TSTART82', 'PRESENT TIME - TIME V82GOFF1 BEGAN', kind='operand', line=217)
W('23,2505', 0o02325, '', 'STORE', 'TSTART82', '               SAVE IT', kind='interp', line=218)
W('23,2506', 0o53145, '', 'DLOAD', 'BZE', 'SR30.1 SETS -TPER=0 IF HPER L/', kind='interp', line=219)
W('23,2507', 0o02346, '', '', '-TPER', 'HPERMIN (300 OR 35) KFT.', kind='operand', line=220)
W('23,2510', 0o46521, '', '', 'TICKTFF', '(-TPER = 0)', kind='operand', line=221)
W('23,2511', 0o43345, 'TICKTPER', 'DLOAD', 'DAD', '(-TPER NON ZERO)  TFF WAS NOT COMPUTED,', kind='interp', line=222)
W('23,2512', 0o02346, '', '', '-TPER', "BUT WAS SET TO 59M59S.DON'T DICK TFF, DO", kind='operand', line=223)
W('23,2513', 0o02325, '', '', 'TSTART82', 'TICK -TPER. DISPLAY BOTH.', kind='operand', line=224)
W('23,2514', 0o02346, '', 'STORE', '-TPER', '-TPER CORRECTED FOR TIME SINCE V82GOFF1', kind='interp', line=225)
W('23,2515', 0o77776, '', 'EXIT', '', 'BEGAN.', kind='interp', line=226)

# Page 518
W('23,2516', 0o35017, '', 'CAF', 'BIT1', line=229)
W('23,2517', 0o55742, '', 'TS', 'V82FLAGS', 'INFORMS TICKTEST TO INCREMENT ONLY -TPER', line=230)
W('23,2520', 0o05217, '', 'TC', 'ENDOFJOB', line=231)

W('23,2521', 0o43345, 'TICKTFF', 'DLOAD', 'DAD', '(-TPER=0)  TFF WAS COMPUTED.TICK TFF.', kind='interp', line=233)
W('23,2522', 0o02344, '', '', 'TFF', 'DO NOT TICK -TPER.DISPLAY TFF, BUT NOT', kind='operand', line=234)
W('23,2523', 0o02325, '', '', 'TSTART82', '-TPER.', kind='operand', line=235)
W('23,2524', 0o02344, '', 'STORE', 'TFF', 'TFF CORRECTED FOR TIME SINCE V82GOFF1', kind='interp', line=236)
W('23,2525', 0o77776, '', 'EXIT', '', 'BEGAN.', kind='interp', line=237)
W('23,2526', 0o35016, '', 'CAF', 'BIT2', line=238)
W('23,2527', 0o55742, '', 'TS', 'V82FLAGS', 'INFORMS TICKTEST TO INCREMENT ONLY TFF.', line=239)
W('23,2530', 0o05217, '', 'TC', 'ENDOFJOB', line=240)

W('23,2531', 0o35013, 'TICKTEST', 'CAF', 'BIT5', 'THIS WAITLIST PROGRAM PERPETUATES ITSELF', line=242)
W('23,2532', 0o71044, '', 'MASK', 'EXTVBACT', 'ONCE A SEC UNTIL BIT 5 OF EXTVBACT =0.', line=243)
W('23,2533', 0o10000, '', 'CCS', 'A', line=244)
W('23,2534', 0o02542, '', 'TC', 'DOTICK', line=245)
W('23,2535', 0o37662, '', 'CAF', 'PRIO25', line=246)
W('23,2536', 0o05134, '', 'TC', 'NOVAC', "TERMINATE V 82.CAN'T CALL ENDEXT IN RUPT.", line=247)
#   EBANK= EXTVBACT
W('23,2537', 0o05534, '', '2CADR', 'ENDEXT', kind='data', line=249)
W('23,2540', 0o04062, kind='data', line=249)

W('23,2541', 0o05324, '', 'TC', 'TASKOVER', line=251)
W('23,2542', 0o35041, 'DOTICK', 'CAF', '1SEC', 'RE-REQUEST TICKTEST.', line=252)
W('23,2543', 0o05245, '', 'TC', 'WAITLIST', line=253)
#   EBANK= TFF
W('23,2544', 0o02531, '', '2CADR', 'TICKTEST', kind='data', line=255)
W('23,2545', 0o46064, kind='data', line=255)

W('23,2546', 0o36214, '', 'CAF', 'THREE', line=257)
W('23,2547', 0o71742, '', 'MASK', 'V82FLAGS', line=258)
W('23,2550', 0o50000, '', 'INDEX', 'A', line=259)
W('23,2551', 0o02552, '', 'TC', '+1', line=260)
W('23,2552', 0o05324, '', 'TC', 'TASKOVER', 'IF NO FLAGBITS SET DONT CHANGE TFF OR', line=261)
# -TPER, BUT CONTINUE LOOP.
W('23,2553', 0o02561, '', 'TC', 'TPERTICK', 'ONLY BIT 1 SET. INCR -TPER BY 1 SEC.', line=263)
W('23,2554', 0o35041, 'TFFTICK', 'CAF', '1SEC', 'ONLY BIT 2 SET. INCR TFF BY 1 SEC.', line=264)
W('23,2555', 0o54001, '', 'TS', 'L', line=265)
W('23,2556', 0o35021, '', 'CAF', 'ZERO', line=266)
W('23,2557', 0o21744, '', 'DAS', 'TFF', line=267)
W('23,2560', 0o05324, '', 'TC', 'TASKOVER', line=268)
W('23,2561', 0o35041, 'TPERTICK', 'CAF', '1SEC', line=269)
W('23,2562', 0o54001, '', 'TS', 'L', line=270)
W('23,2563', 0o35021, '', 'CAF', 'ZERO', line=271)
W('23,2564', 0o21746, '', 'DAS', '-TPER', line=272)
W('23,2565', 0o05324, '', 'TC', 'TASKOVER', line=273)
# Page 519
W('23,2566', 0o77776, 'V82GON', 'EXIT', '', 'AVERAGE G ON. USE CURRENT STATE VECTOR', kind='interp', line=275)
# FOR ORBITAL PARAMETER CALCULATIONS.
W('23,2567', 0o35063, '', 'CAF', 'PRIO7', 'LESS THAN LAMBERT', line=277)
W('23,2570', 0o05147, '', 'TC', 'FINDVAC', 'V82GON1 WILL PERFORM ORBIT CALCULATIONS', line=278)
#   EBANK= TFF  # ABOUT PROPER BODY APPROX ONCE PER SEC.
W('23,2571', 0o02604, '', '2CADR', 'V82GON1', kind='data', line=280)
W('23,2572', 0o46064, kind='data', line=280)

W('23,2573', 0o00003, '', 'RELINT', line=282)
W('23,2574', 0o10067, '', 'CCS', 'NEWJOB', 'WITHOLD V16 N44 UNTIL FIRST ORBIT CALC', line=283)
W('23,2575', 0o05164, '', 'TC', 'CHANG1', 'IS DONE. NOTE: V82GON1 (PRIO7, FINDVAC', line=284)
# JOB) IS COMPLETED BEFORE V82GON (PRIO7,
# NOVAC JOB).
W('23,2576', 0o32407, 'V82REDSP', 'CAF', 'V16N44', 'MONITOR HAPO, HPER, TFF', line=287)
W('23,2577', 0o04662, '', 'TC', 'BANKCALL', line=288)
W('23,2600', 0o20561, '', 'CADR', 'GOXDSPF', kind='data', line=289)
W('23,2601', 0o05625, '', 'TC', 'B5OFF', 'TERM THIS TELLS V82GON1 TO KILL ITSELF.', line=290)
W('23,2602', 0o05625, '', 'TC', 'B5OFF', 'PROC DITTO.', line=291)
W('23,2603', 0o02576, '', 'TC', 'V82REDSP', 'RECYCLE', line=292)

W('23,2604', 0o06006, 'V82GON1', 'TC', 'INTPRET', 'THIS EXEC PROGRAM PERPETUATES ITSELF', line=294)
# ONCE A SEC UNTIL BIT 5 OF EXTVBACT =0.
W('23,2605', 0o52175, '', 'VLOAD', 'GOTO', 'HOLDS OFF CCS NEWJOB BETWEEN RN AND', kind='interp', line=296)
W('23,2606', 0o01171, '', '', 'RN', 'VN FETCH SO RN , VN ARE FROM SAME', kind='operand', line=297)
W('23,2607', 0o46610, '', '', 'NEXTLINE', 'STATE VECTOR UPDATE.', kind='operand', line=298)
W('23,2610', 0o26327, 'NEXTLINE', 'STOVL', 'RONE', 'RN AT (-29)M FOR EARTH OR MOON', kind='interp', line=299)
W('23,2611', 0o01177, '', '', 'VN', kind='operand', line=300)
W('23,2612', 0o02335, '', 'STORE', 'VONE', 'VN AT (-7)M/CS FOR EARTH OR MOON', kind='interp', line=301)
W('23,2613', 0o52014, '', 'BON', 'GOTO', kind='interp', line=302)
W('23,2614', 0o00315, '', '', 'AMOONFLG', 'FLAG INDICATES BODY ABOUT WHICH ORBITAL', kind='operand', line=303)
W('23,2615', 0o46617, '', '', 'MOONGON', 'CALCULATIONS ARE TO BE PERFORMED.', kind='operand', line=304)
W('23,2616', 0o46630, '', '', 'EARTHGON', 'IF SET - MOON , IF RESET - EARTH.', kind='operand', line=305)

W('23,2617', 0o71214, 'MOONGON', 'SET', 'DLOAD', kind='interp', line=307)
W('23,2620', 0o04462, '', '', 'V82EMFLG', 'INDICATE MOON SCALING FOR SR30.1', kind='operand', line=308)
W('23,2621', 0o06454, '', '', '1/RTMUM', 'LUNAR PARAMETERS LOADED HERE FOR SR30.1', kind='operand', line=309)
W('23,2622', 0o14037, '', 'STODL', 'TFF/RTMU', kind='interp', line=310)
W('23,2623', 0o06460, '', '', 'MINPERM', kind='operand', line=311)
W('23,2624', 0o26321, '', 'STOVL', 'HPERMIN', kind='interp', line=312)
W('23,2625', 0o02026, '', '', 'RLS', 'SCALED AT (-27)M', kind='operand', line=313)
W('23,2626', 0o52046, '', 'ABVAL', 'GOTO', kind='interp', line=314)
W('23,2627', 0o46637, '', '', 'V82GON2', kind='operand', line=315)
W('23,2630', 0o71214, 'EARTHGON', 'CLEAR', 'DLOAD', kind='interp', line=316)
W('23,2631', 0o04662, '', '', 'V82EMFLG', 'INDICATE EARTH SCALING FOR SR30.1', kind='operand', line=317)
W('23,2632', 0o06456, '', '', '1/RTMUE', 'EARTH PARAMETERS LOADED HERE FOR SR30.1', kind='operand', line=318)
W('23,2633', 0o14037, '', 'STODL', 'TFF/RTMU', kind='interp', line=319)
W('23,2634', 0o06462, '', '', 'MINPERE', kind='operand', line=320)
W('23,2635', 0o16321, '', 'STODL', 'HPERMIN', kind='interp', line=321)
W('23,2636', 0o05152, '', '', 'RPAD', kind='operand', line=322)
W('23,2637', 0o36323, 'V82GON2', 'STCALL', 'RPADTEM', 'COMMON CODE FOR EARTH & MOON.', kind='interp', line=323)
W('23,2640', 0o46667, '', '', 'SR30.1', kind='operand', line=324)
# Page 520
W('23,2641', 0o77776, '', 'EXIT', kind='interp', line=326)
W('23,2642', 0o05364, '', 'TC', 'CHECKMM', line=327)
W('23,2643', 0o00013, '', 'DEC', '11', kind='data', line=328)
W('23,2644', 0o02657, '', 'TC', 'V82GON3', 'NOT IN MODE 11.', line=329)
W('23,2645', 0o06006, 'CANDEL', 'TC', 'INTPRET', 'IN MODE 11 OR 00', line=330)
W('23,2646', 0o77624, '', 'CALL', kind='interp', line=331)
W('23,2647', 0o27442, '', '', 'INTSTALL', 'DELRSPL DOES INTWAKE', kind='operand', line=332)
W('23,2650', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=333)
W('23,2651', 0o02344, '', '', 'TFF', kind='operand', line=334)
W('23,2652', 0o64017, '', '', 'DELRSPL', 'RETURN IS TO NEXT LINE ( SPLRET ).', kind='operand', line=335)
W('23,2653', 0o77776, 'SPLRET', 'EXIT', kind='interp', line=336)

W('23,2654', 0o31011, '', 'CA', 'MODREG', line=338)
W('23,2655', 0o00006, '', 'EXTEND', line=339)
W('23,2656', 0o12501, '', 'BZF', 'SPLRET1', line=340)
W('23,2657', 0o35013, 'V82GON3', 'CAF', 'BIT5', line=341)
W('23,2660', 0o71044, '', 'MASK', 'EXTVBACT', 'SEE IF ASTRONAUT HAS SIGNALLED TERMINATE', line=342)
W('23,2661', 0o00006, '', 'EXTEND', line=343)
W('23,2662', 0o15534, '', 'BZF', 'ENDEXT', 'YES, TERMINATE VB 82 LOOP', line=344)
W('23,2663', 0o35041, '', 'CAF', '1SEC', line=345)
W('23,2664', 0o04662, '', 'TC', 'BANKCALL', 'WAIT ONE SECOND BEFORE REPEATING', line=346)
W('23,2665', 0o01732, '', 'CADR', 'DELAYJOB', 'ORBITAL PARAMETER COMPUTATION.', kind='data', line=347)
W('23,2666', 0o02604, '', 'TC', 'V82GON1', line=348)

# Page 521
# SUBROUTINE NAME: SR30.1
# MOD NO: 0                                                             DATE:           16 FEB 67
# MOD BY: R. R. BAIRNSFATHER                                            LOG SECTION:    R32
# MOD NO: 1     MOD BY: R. R. BAIRNSFATHER      DATE: 11 APR 67         SR30.1 CHANGED TO ALLOW MONITOR OPERN
# MOD NO: 2     MOD BY: R. R. BAIRNSFATHER      DATE: 14 APR 67         ADD OVFL CK FOR RAPO
# MOD NO: 3     MOD BY ALONSO                   DATE: 11 DEC 67         SUBROUTINE REWRITTEN
# MOD NO: 4     MOD BY ALONSO                   DATE: 26 MAR 68         PROG MOD TO HANDLE DIF EARTH/MOON SCALE
# MOD NO: 5     MOD BY: RR BAIRNSFATHER         DATE: 6 AUG 68          OVFL CK FOR HAPO & HPER. VOIDS MOD #2.
#
# NEW FUNCTIONAL DESCRIPTION:  ORBITAL PARAMETERS DISPLAY FOR NOUNS 32 AND 44.
# SR30.1 CALLS TFFCONMU AND TFFRP/RA TO CALCULATE RPER (PERIGEE RADIUS),
# RAPO (APOGEE RADIUS), HPER (PERIGEE HEIGHT ABOVE LAUNCH PAD OR LUNAR
# LANDING SITE), HAPO (APOGEE HEIGHT AS ABOVE), TPER (TIME TO PERIGEE),
# TFF (TIME TO INTERSECT 300 KFT ABOVE PAD OR 35KFT ABOVE LANDING SITE).
# IF HPER IS GREATER THAN OR EQUAL TO HPERMIN, CALCULATES TPER AND STORES
# NEGATIVE   IN -TPER.  OTHERWISE STORES +0 IN -TPER.  WHENEVER TPER IS
# CALCULATED, TFF IS NOT COMPUTABLE AND DEFAULTS TO -59MIN 59SEC. IF HAPO
# WOULD EXCEED 9999.9 NM, IT IS LIMITED TO THAT VALUE FOR DISPLAY.
#
# ADDENDUM:     HAPO AND HPER SHOULD BE CHANGED TO READ HAPOX AND HPERX IN THE
# ABOVE REMARKS.
#
# CALLING SEQUENCE:     CALL
# SR30.1
#
# SUBROUTINES CALLED:   TFFCONMU, TFFRP/RA, CALCTPER, CALCTFF
# NORMAL EXIT MODE:     CALLING LINE +1 (STILL IN INTERPRETIVE MODE)
# ALARMS:       NONE
# OUTPUT:       RAPO    (-29) M EARTH   APOGEE RADIUS   EARTH CENTERED COORD.
# (-27) M MOON                    MOON CENTERED COORD.
# RPER    (-29) M EARTH   PERIGEE RADIUS  EARTH CENTERED COORD.
# (-27) M MOON                    MOON CENTERED COORD.
# HAPOX   (-29) M         APOGEE ALTITUDE ABOVE PAD OR LAND. SITE MAX VALUE LIMITED TO 9999.9 NM.
# HPERX   (-29) M         PERIGEE ALT. ABOVE PAD OR LAND. SITE    MAX VALUE LIMITED TO 9999.9 NM.
# TFF     (-28) CS        TIME TO 300KFT OR 35KFT ALTITUDE
# -TPER   (-28) CS        TIME TO PERIGEE
# ERASABLE INITIALIZATION REQUIRED -
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
# DEBRIS:       QPRET, PDL, S2

# Page 522
#   COUNT* $$/SR30S

W('23,2667', 0o44001, 'SR30.1', 'SETPD', 'STQ', 'INITIALIZE PUSHDOWN LIST.', kind='interp', line=403)
W('23,2670', 0o00001, '', '', '0', kind='operand', line=404)
W('23,2671', 0o00051, '', '', 'S2', kind='operand', line=405)
# SR30.1 INPUT: RONE AT (-29)M EARTH/MOON
# VONE AT (-7)M/CS
# TFFCONMU,TFFRP/RA,CALCTPER,AND CALCTFF
# CALLS REQUIRE:
# EARTH CENTERED (NO RESCALING REQUIRED)
# RONE SCALED TO B-29 M
# VONE SCALED TO B-7 M/CS
# MOON CENTERED (RESCALING REQUIRED)
# RONE SCALED TO B-27 M
# VONE SCALED TO B-5 M/CS
W('23,2672', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=416)
W('23,2673', 0o04742, '', '', 'V82EMFLG', 'OFF FOR EARTH , ON FOR MOON.', kind='operand', line=417)
W('23,2674', 0o46703, '', '', 'TFFCALLS', kind='operand', line=418)
W('23,2675', 0o02327, '', '', 'RONE', kind='operand', line=419)
W('23,2676', 0o77752, '', 'VSL2', kind='interp', line=420)
W('23,2677', 0o26327, '', 'STOVL', 'RONE', kind='interp', line=421)
W('23,2700', 0o02335, '', '', 'VONE', kind='operand', line=422)
W('23,2701', 0o77752, '', 'VSL2', kind='interp', line=423)
W('23,2702', 0o02335, '', 'STORE', 'VONE', kind='interp', line=424)
W('23,2703', 0o77624, 'TFFCALLS', 'CALL', kind='interp', line=425)
W('23,2704', 0o56760, '', '', 'TFFCONMU', kind='operand', line=426)
W('23,2705', 0o77624, '', 'CALL', '', 'TFFRP/RA COMPUTES RAPO,RPER.', kind='interp', line=427)
W('23,2706', 0o57026, '', '', 'TFFRP/RA', kind='operand', line=428)
# RETURNS WITH RAPO IN D(MPAC).
W('23,2707', 0o77625, '', 'DSU', kind='interp', line=430)
W('23,2710', 0o02323, '', '', 'RPADTEM', kind='operand', line=431)
W('23,2711', 0o64414, '', 'BOFF', 'SR2R', 'NEED HAPO AT (-29)M FOR DISPLAY.', kind='interp', line=432)
# IF MOON CENTERED, RESCALE FROM (-27)M.
# IF EARTH CENTERED ALREADY AT (-29)M.
W('23,2712', 0o04742, '', '', 'V82EMFLG', 'OFF FOR EARTH , ON FOR MOON.', kind='operand', line=435)
W('23,2713', 0o46714, '', '', '+1', kind='operand', line=436)
W('23,2714', 0o77624, '', 'CALL', '', 'IF HAPO > MAXNM, SET HAPO =9999.9 NM.', kind='interp', line=437)
W('23,2715', 0o46754, '', '', 'MAXCHK', 'OTHERWISE STORE (RAPO-RPADTEM) IN HAPO.', kind='operand', line=438)
W('23,2716', 0o16352, 'STORHAPO', 'STODL', 'HAPOX', kind='interp', line=439)
W('23,2717', 0o00017, '', '', 'RPER', kind='operand', line=440)
W('23,2720', 0o77625, '', 'DSU', kind='interp', line=441)
W('23,2721', 0o02323, '', '', 'RPADTEM', 'GIVES HPER AT (-29)M EARTH, (-27)M MOON.', kind='operand', line=442)
W('23,2722', 0o00161, '', 'STORE', 'MPAC +4', 'SAVE THIS FOR COMPARISON TO HPERMIN.', kind='interp', line=443)
W('23,2723', 0o64414, '', 'BOFF', 'SR2R', 'NEED HPER AT (-29)M FOR DISPLAY.', kind='interp', line=444)
# IF MOON CENTERED, RESCALE FROM (-27)M.
# IF EARTH CENTERED ALREADY AT (-29)M.
W('23,2724', 0o04742, '', '', 'V82EMFLG', 'OFF FOR EARTH, ON FOR MOON.', kind='operand', line=447)
W('23,2725', 0o46726, '', '', '+1', kind='operand', line=448)
W('23,2726', 0o77624, '', 'CALL', '', 'IF HPER > MAXNM, SET HPER = 9999.9 NM.', kind='interp', line=449)
W('23,2727', 0o46754, '', '', 'MAXCHK', kind='operand', line=450)
# Page 523
W('23,2730', 0o16354, 'STORHPER', 'STODL', 'HPERX', 'STORE (RPER - RPADTEM) INTO HPERX.', kind='interp', line=452)
W('23,2731', 0o00161, '', '', 'MPAC +4', kind='operand', line=453)
W('23,2732', 0o51025, '', 'DSU', 'BPL', 'HPERMIN AT (-29)M FOR EARTH, (-27)M MOON', kind='interp', line=454)
W('23,2733', 0o02321, '', '', 'HPERMIN', 'IF HPER L/ HPERMIN (300 OR 35) KFT,', kind='operand', line=455)
W('23,2734', 0o46740, '', '', 'DOTPER', 'THEN ZERO INTO -TPER.', kind='operand', line=456)
W('23,2735', 0o52145, '', 'DLOAD', 'GOTO', 'OTHERWISE CALCULATE TPER.', kind='interp', line=457)
W('23,2736', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=458)
W('23,2737', 0o46744, '', '', 'SKIPTPER', kind='operand', line=459)
W('23,2740', 0o45145, 'DOTPER', 'DLOAD', 'CALL', kind='interp', line=460)
W('23,2741', 0o00017, '', '', 'RPER', kind='operand', line=461)
W('23,2742', 0o57064, '', '', 'CALCTPER', kind='operand', line=462)
W('23,2743', 0o77676, '', 'DCOMP', '', 'TPER IS PUT NEG INTO -TPER.', kind='interp', line=463)
W('23,2744', 0o16346, 'SKIPTPER', 'STODL', '-TPER', kind='interp', line=464)
W('23,2745', 0o02321, '', '', 'HPERMIN', 'HPERMIN AT (-29)M FOR EARTH, (-27)M MOON', kind='operand', line=465)
W('23,2746', 0o45015, '', 'DAD', 'CALL', kind='interp', line=466)
W('23,2747', 0o02323, '', '', 'RPADTEM', 'RPADTEM AT (-29)M FOR EARTH, (-27)M MOON', kind='operand', line=467)
W('23,2750', 0o57067, '', '', 'CALCTFF', 'GIVES 59M59S FOR TFF IF RPER G/', kind='operand', line=468)
W('23,2751', 0o77676, '', 'DCOMP', '', 'HPERMIN + RPADTEM.  (TPER WAS NON ZERO)', kind='interp', line=469)
W('23,2752', 0o36344, '', 'STCALL', 'TFF', 'OTHERWISE COMPUTES TFF.       (GOTO)', kind='interp', line=470)
W('23,2753', 0o00051, '', '', 'S2', kind='operand', line=471)

W('23,2754', 0o51025, 'MAXCHK', 'DSU', 'BPL', 'IF C(MPAC) > 9999.9 NM. MPAC = 9999.9 NM.', kind='interp', line=473)
W('23,2755', 0o06764, '', '', 'MAXNM', kind='operand', line=474)
W('23,2756', 0o46761, '', '', '+3', 'OTHERWISE C(MPAC) = B(MPAC).', kind='operand', line=475)
W('23,2757', 0o43415, '', 'DAD', 'RVQ', kind='interp', line=476)
W('23,2760', 0o06764, '', '', 'MAXNM', kind='operand', line=477)
W('23,2761', 0o43545, '', 'DLOAD', 'RVQ', '(USED BY P30 - P37 ALSO)', kind='interp', line=478)
W('23,2762', 0o06764, '', '', 'MAXNM', kind='operand', line=479)

W('23,2763', 0o01065, 'MAXNM', '2OCT', '0106505603', kind='data', line=481)
W('23,2764', 0o05603, kind='data', line=481)

# Page 524

# There is no source code on this page --- HG 2009
