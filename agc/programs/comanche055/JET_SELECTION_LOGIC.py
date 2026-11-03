"""JET_SELECTION_LOGIC.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/JET_SELECTION_LOGIC.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1039-1062 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('JET_SELECTION_LOGIC', 'JET_SELECTION_LOGIC.agc', 'Comanche055', pages='1039-1062')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     JET_SELECTION_LOGIC.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1039-1062
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

# Page 1039
#   BANK 21
#   SETLOC DAPS4
#   BANK

#   COUNT 17/DAPJS

#   EBANK= KMPAC

# EXAMINE CHANNEL 31 FOR TRANSLATION COMMANDS

W('17,2552', 0o22016, 'JETSLECT', 'LXCH', 'BANKRUPT', line=41)
W('17,2553', 0o32634, '', 'CAF', 'DELTATT3', '= 60 MS  RESET TO EXECUTE PHASE1', line=42)
W('17,2554', 0o61634, '', 'AD', 'T5TIME', line=43)
W('17,2555', 0o54030, '', 'TS', 'TIME5', line=44)
W('17,2556', 0o12561, '', 'TCF', '+3', line=45)
W('17,2557', 0o32635, '', 'CAF', 'DELATT20', '= 20 MS  TO ASSURE A T5RUPT', line=46)
W('17,2560', 0o54030, '', 'TS', 'TIME5', line=47)
W('17,2561', 0o33313, '', 'CAF', '=14MS', 'RESET T6 TO INITIALIZE THE JET CHANNELS', line=48)
W('17,2562', 0o54031, '', 'TS', 'TIME6', 'IN 14 MS', line=49)
W('17,2563', 0o35001, '', 'CAF', 'NEGMAX', line=50)
W('17,2564', 0o00006, '', 'EXTEND', line=51)
W('17,2565', 0o05013, '', 'WOR', 'CHAN13', line=52)
W('17,2566', 0o00006, '', 'EXTEND', line=53)
W('17,2567', 0o22012, '', 'QXCH', 'QRUPT', line=54)
W('17,2570', 0o32633, '', 'CAF', 'XLNMASK', '= 7700 OCT', line=55)
W('17,2571', 0o00006, '', 'EXTEND', '', 'EXAMINE THE TRANSLATION', line=56)
W('17,2572', 0o06031, '', 'RXOR', 'CHAN31', 'HAND CONTROLLER', line=57)
W('17,2573', 0o72633, '', 'MASK', 'XLNMASK', line=58)
W('17,2574', 0o00006, '', 'EXTEND', line=59)
W('17,2575', 0o12636, '', 'BZF', 'NOXLNCMD', line=60)
W('17,2576', 0o55502, '', 'TS', 'T5TEMP', line=61)
W('17,2577', 0o00006, '', 'EXTEND', line=62)
W('17,2600', 0o75007, '', 'MP', 'BIT9', line=63)
W('17,2601', 0o76214, '', 'MASK', 'THREE', line=64)
W('17,2602', 0o55513, '', 'TS', 'XNDX1', 'AC QUAD  X-TRANSLATION INDEX', line=65)
W('17,2603', 0o55514, '', 'TS', 'XNDX2', 'BD QUAD  X-TRANSLATION INDEX', line=66)
W('17,2604', 0o31502, '', 'CA', 'T5TEMP', line=67)
W('17,2605', 0o00006, '', 'EXTEND', '', '1 = + XLN', line=68)
W('17,2606', 0o75011, '', 'MP', 'BIT7', '2 = - XLN', line=69)
W('17,2607', 0o76214, '', 'MASK', 'THREE', '3 = NO XLN', line=70)
W('17,2610', 0o55515, '', 'TS', 'YNDX', 'Y-TRANSLATION INDEX', line=71)

W('17,2611', 0o31502, '', 'CA', 'T5TEMP', line=73)
W('17,2612', 0o00006, '', 'EXTEND', line=74)
W('17,2613', 0o75013, '', 'MP', 'BIT5', line=75)
W('17,2614', 0o76214, '', 'MASK', 'THREE', line=76)
W('17,2615', 0o55516, '', 'TS', 'ZNDX', 'Z-TRANSLATION INDEX', line=77)

W('17,2616', 0o31466, '', 'CA', 'DAPDATR1', 'SET ATTKALMN TO PICK UP FILTER GAINS FOR', line=79)
W('17,2617', 0o75002, '', 'MASK', 'BIT14', 'TRANSLATIONS.', line=80)
W('17,2620', 0o00006, '', 'EXTEND', '', 'CHECK DAPDATR1 BIT 14 FOR LEM ATTACHED.', line=81)
# Page 1040
W('17,2621', 0o12624, '', 'BZF', 'NOLEM', line=83)
W('17,2622', 0o46214, '', 'CS', 'THREE', 'IF LEM IS ON, SET ATTKALMN = -3', line=84)
W('17,2623', 0o12625, '', 'TCF', '+2', line=85)
W('17,2624', 0o45016, 'NOLEM', 'CS', 'TWO', 'IF LEM IS OFF, SET ATTKALMN = -2.', line=86)
W('17,2625', 0o55617, '', 'TS', 'ATTKALMN', line=87)
W('17,2626', 0o11631, '', 'CCS', 'XTRANS', '(+, -1, 0)', line=88)
W('17,2627', 0o55513, '', 'TS', 'XNDX1', 'USING BD-X  ZERO XNDX1', line=89)
W('17,2630', 0o12642, '', 'TCF', 'PWORD', line=90)
W('17,2631', 0o55514, '', 'TS', 'XNDX2', 'USING AC-X  ZERO XNDX2', line=91)
W('17,2632', 0o12642, '', 'TCF', 'PWORD', line=92)
W('17,2633', 0o07700, 'XLNMASK', 'OCT', '7700', kind='data', line=93)

W('17,2634', 0o37772, 'DELTATT3', 'DEC', '16378', '= 60 MS', kind='data', line=95)
W('17,2635', 0o37776, 'DELATT20', 'DEC', '16382', '= 20 MS', kind='data', line=96)

W('17,2636', 0o55513, 'NOXLNCMD', 'TS', 'XNDX1', 'ZERO ALL REQUESTS FOR TRANSLATION', line=98)
W('17,2637', 0o55514, '', 'TS', 'XNDX2', line=99)
W('17,2640', 0o55515, '', 'TS', 'YNDX', line=100)
W('17,2641', 0o55516, '', 'TS', 'ZNDX', line=101)

# PITCH COMMANDS  TIMING(NO X-TRANS, NO QUAD FAILS) 32MCT

W('17,2642', 0o11562, 'PWORD', 'CCS', 'TAU1', 'CHECK FOR PITCH COMMANDS', line=105)
W('17,2643', 0o35017, '', 'CAF', 'ONE', line=106)
W('17,2644', 0o12646, '', 'TCF', '+2', ' 0 = NO PITCH', line=107)
W('17,2645', 0o35016, '', 'CAF', 'TWO', '+1 =  + PITCH', line=108)
W('17,2646', 0o55520, '', 'TS', 'PINDEX', '+2 =  - PITCH', line=109)

W('17,2647', 0o11626, '', 'CCS', 'RACFAIL', 'FLAG FOR REAL AC QUAD FAILURES', line=111)
W('17,2650', 0o12654, '', 'TCF', 'AFAILP', line=112)
W('17,2651', 0o12664, '', 'TCF', 'TABPCOM', '0 = NO REAL AC FAILURES', line=113)
W('17,2652', 0o12656, '', 'TCF', 'CFAILP', '+ = A QUAD FAILED', line=114)
W('17,2653', 0o12664, '', 'TCF', 'TABPCOM', '- = C QUAD FAILED', line=115)
# IF FAILURES ARE PRESENT IGNORE
# X-TRANSLATIONS ON THIS AXIS

W('17,2654', 0o34334, 'AFAILP', 'CAF', 'NINE', 'IF FAILURE IS PRESENT 1JET OPERATION', line=119)
W('17,2655', 0o12666, '', 'TCF', 'TABPCOM +2', 'IS ASSUMED.  IGNORE X-TRANSLATION', line=120)
W('17,2656', 0o35771, 'CFAILP', 'CAF', 'TWELVE', line=121)
W('17,2657', 0o12666, '', 'TCF', 'TABPCOM +2', line=122)

W('17,2660', 0o00000, 'XLNNDX', 'DEC', '0', 'INDICES FOR TRANSLATION COMMANDS', kind='data', line=124)
W('17,2661', 0o00003, '', 'DEC', '3', 'FOR USE IN TABLE LOOK UP', kind='data', line=125)
W('17,2662', 0o00006, '', 'DEC', '6', kind='data', line=126)
W('17,2663', 0o00000, '', 'DEC', '0', kind='data', line=127)

S('TWELVE', 'equals', 0o5771, line=129)
# TABLE LOOK UP FOR PITCH COMMANDS WITH AND WITHOUT X-TRANSLATION AND AC QUAD FAILURES PRESENT.
# BITS 9, 10 CONTAIN THE NUMBER OF PITCH JETS USED TO PERFORM THE PITCH ROTATION
# Page 1041

W('17,2664', 0o51513, 'TABPCOM', 'INDEX', 'XNDX1', line=134)
W('17,2665', 0o32660, '', 'CA', 'XLNNDX', line=135)
W('17,2666', 0o61520, '', 'AD', 'PINDEX', line=136)
W('17,2667', 0o50000, '', 'INDEX', 'A', line=137)
W('17,2670', 0o32714, '', 'CA', 'PYTABLE', line=138)
W('17,2671', 0o72733, '', 'MASK', 'PJETS', '=1417 OCT', line=139)
W('17,2672', 0o55453, '', 'TS', 'PWORD1', line=140)
W('17,2673', 0o00006, '', 'EXTEND', line=141)
W('17,2674', 0o75011, '', 'MP', 'BIT7', line=142)
W('17,2675', 0o55523, '', 'TS', 'NPJETS', '= NO. OF PITCH JETS', line=143)

# YAW JET COMMANDS  TIMING(NO X-TRANS, NO QUAD FAILURES)  32MCT

W('17,2676', 0o11563, 'YWORD', 'CCS', 'TAU2', 'CHECK FOR YAW COMMANDS', line=147)
W('17,2677', 0o35017, '', 'CAF', 'ONE', line=148)
W('17,2700', 0o12702, '', 'TCF', '+2', line=149)
W('17,2701', 0o35016, '', 'CAF', 'TWO', line=150)
W('17,2702', 0o55521, '', 'TS', 'YINDEX', 'YAW ROTATION INDEX', line=151)

W('17,2703', 0o11627, '', 'CCS', 'RBDFAIL', 'FLAG FOR B OR D QUAD FAILURES', line=153)
W('17,2704', 0o12710, '', 'TCF', 'BFAILY', '0 = NO BD FAILURE', line=154)
W('17,2705', 0o12735, '', 'TCF', 'TABYCOM', '+ = B QUAD FAILED', line=155)
W('17,2706', 0o12712, '', 'TCF', 'DFAILY', '- = D QUAD FAILED', line=156)
W('17,2707', 0o12735, '', 'TCF', 'TABYCOM', line=157)

W('17,2710', 0o34334, 'BFAILY', 'CAF', 'NINE', line=159)
W('17,2711', 0o12737, '', 'TCF', 'TABYCOM +2', line=160)
W('17,2712', 0o35771, 'DFAILY', 'CAF', 'TWELVE', line=161)
W('17,2713', 0o12737, '', 'TCF', 'TABYCOM +2', line=162)

# Page 1042
# TABLE FOR PITCH(YAW) COMMANDS
# BITS 4,3,2,1 = PITCH, X-TRANSLATION JETS SELECTED
# BITS     10,9 = NO. PITCH JETS USED TO PERFORM ROTATION
# BITS 8,7,6,5 = YAW, X-TRANSLATION JETS SELECTED
# BITS 12,11 : NO. YAW JETS USED TO PERFORM ROTATION

# ROT   TRANS   QUAD    BIAS
W('17,2714', 0o00000, 'PYTABLE', 'OCT', '0', '0     0               0', kind='data', line=172)
W('17,2715', 0o05125, '', 'OCT', '5125', '+     0               0', kind='data', line=173)
W('17,2716', 0o05252, '', 'OCT', '5252', '-     0               0', kind='data', line=174)
W('17,2717', 0o00231, '', 'OCT', '0231', '0     +               3', kind='data', line=175)
W('17,2720', 0o02421, '', 'OCT', '2421', '+     +               3', kind='data', line=176)
W('17,2721', 0o02610, '', 'OCT', '2610', '-     +               3', kind='data', line=177)
W('17,2722', 0o00146, '', 'OCT', '0146', '0     -               6', kind='data', line=178)
W('17,2723', 0o02504, '', 'OCT', '2504', '+     -               6', kind='data', line=179)
W('17,2724', 0o02442, '', 'OCT', '2442', '-     -               6', kind='data', line=180)
W('17,2725', 0o00000, '', 'OCT', '0', '0             A(B)    9', kind='data', line=181)
W('17,2726', 0o02421, '', 'OCT', '2421', '+             A(B)    9', kind='data', line=182)
W('17,2727', 0o02442, '', 'OCT', '2442', '-             A(B)    9', kind='data', line=183)
W('17,2730', 0o00000, '', 'OCT', '0', '0             C(D)    12', kind='data', line=184)
W('17,2731', 0o02504, '', 'OCT', '2504', '+             C(D)    12', kind='data', line=185)
W('17,2732', 0o02610, '', 'OCT', '2610', '-             C(D)    12', kind='data', line=186)

# MASKS FOR PITCH AND YAW COMMANDS

W('17,2733', 0o01417, 'PJETS', 'OCT', '1417', kind='data', line=190)
W('17,2734', 0o06360, 'YJETS', 'OCT', '6360', kind='data', line=191)

# TABLE LOOK UP FOR YAW COMMANDS WITH AND WITHOUT X-TRANSLATION AND AC QUAD FAILURES PRESENT
# BITS 11, 12 CONTAIN THE NUMBER OF YAW JETS USED TO PERFORM THE YAW ROTATION

W('17,2735', 0o51514, 'TABYCOM', 'INDEX', 'XNDX2', line=196)
W('17,2736', 0o32660, '', 'CA', 'XLNNDX', line=197)
W('17,2737', 0o61521, '', 'AD', 'YINDEX', line=198)
W('17,2740', 0o50000, '', 'INDEX', 'A', line=199)
W('17,2741', 0o32714, '', 'CA', 'PYTABLE', line=200)
W('17,2742', 0o72734, '', 'MASK', 'YJETS', '= 6360 OCT', line=201)
W('17,2743', 0o55455, '', 'TS', 'YWORD1', line=202)
W('17,2744', 0o00006, '', 'EXTEND', line=203)
W('17,2745', 0o75013, '', 'MP', 'BIT5', line=204)
W('17,2746', 0o55524, '', 'TS', 'NYJETS', 'NO. OF YAW JETS USED TO PERFORM ROTATION', line=205)

# Page 1043
# ROLL COMMANDS  TIMING(NO Y,Z TRANS, NO QUAD FAILS)  45MCT

W('17,2747', 0o11561, 'RWORD', 'CCS', 'TAU', 'CHECK FOR ROLL COMMANDS', line=210)
W('17,2750', 0o35017, '', 'CAF', 'ONE', line=211)
W('17,2751', 0o12753, '', 'TCF', '+2', line=212)
W('17,2752', 0o35016, '', 'CAF', 'TWO', line=213)
W('17,2753', 0o55517, '', 'TS', 'RINDEX', line=214)

W('17,2754', 0o11630, '', 'CCS', 'ACORBD', 'FLAG FOR AC OR BD QUAD SELECTION FOR', line=216)
W('17,2755', 0o13046, '', 'TCF', 'BDROLL', 'ROLL COMMANDS', line=217)
W('17,2756', 0o13046, '', 'TCF', 'BDROLL', '+, +0 = BD ROLL', line=218)
W('17,2757', 0o12760, '', 'TCF', '+1', '-, -0 = AC ROLL', line=219)

W('17,2760', 0o11626, 'ACROLL', 'CCS', 'RACFAIL', 'CHECK FOR REAL FAILURES', line=221)
W('17,2761', 0o12765, '', 'TCF', 'RAFAIL', 'ON AC QUADS', line=222)
W('17,2762', 0o12775, '', 'TCF', 'RXLNS', line=223)
W('17,2763', 0o12767, '', 'TCF', 'RCFAIL', line=224)
W('17,2764', 0o12775, '', 'TCF', 'RXLNS', line=225)

W('17,2765', 0o34334, 'RAFAIL', 'CAF', 'NINE', 'QUAD FAILURE WILL GET', line=227)
W('17,2766', 0o12777, '', 'TCF', 'TABRCOM', '1-JET OPERATION', line=228)
W('17,2767', 0o35771, 'RCFAIL', 'CAF', 'TWELVE', line=229)
W('17,2770', 0o12777, '', 'TCF', 'TABRCOM', line=230)

W('17,2771', 0o00000, 'XLN1NDX', 'DEC', '0', kind='data', line=232)
W('17,2772', 0o00001, '', 'DEC', '1', 'INDECES FOR TRANSLATION', kind='data', line=233)
W('17,2773', 0o00002, '', 'DEC', '2', kind='data', line=234)
W('17,2774', 0o00000, '', 'DEC', '0', kind='data', line=235)

# TABLE LOOK UP FOR AC-ROLL COMMANDS WITH AND WITHOUT Y-TRANSLATION AND ACQUAD FAILURES PRESENT
# BITS 9,10,11 CONTAIN THE MAGNITUDE AND DIRECTION OF THE ROLL

W('17,2775', 0o51515, 'RXLNS', 'INDEX', 'YNDX', 'NO AC QUAD FAILURES', line=240)
W('17,2776', 0o32660, '', 'CA', 'XLNNDX', 'INCLUDE +,-,0, Y-TRANSLATION', line=241)
W('17,2777', 0o61517, 'TABRCOM', 'AD', 'RINDEX', line=242)
W('17,3000', 0o50000, '', 'INDEX', 'A', line=243)
W('17,3001', 0o33130, '', 'CA', 'RTABLE', line=244)
W('17,3002', 0o73147, '', 'MASK', 'ACRJETS', '= 3760 OCT', line=245)
W('17,3003', 0o55451, '', 'TS', 'RWORD1', line=246)

# CHECK FOR Z-TRANSLATIONS ON BD

W('17,3004', 0o31516, 'BDZCHECK', 'CA', 'ZNDX', line=250)
W('17,3005', 0o00006, '', 'EXTEND', line=251)
W('17,3006', 0o63040, '', 'BZMF', 'NOBDZ', 'NO Z-TRANSLATION', line=252)

# Page 1044
# TABLE LOOK UP FOR BD Z-TRANSLATION WITH AND WITHOUT REAL BD QUAD FAILURES.  Z-TRANSLATION WILL BE POSS-
# IBLE AS LONG AS ROLL COMMANDS CAN BE SATISFIED WITH THE AC ROLL JETS.  CRITERION..  IF THE RESULTANT NET ROLL
# COMMANDS = 0 (WITH Z-TRANSLATION) AND IF TAU = 0, THEN INCLUDE THE BD Z-TRANSLATION COMMANDS.  IF THE RESULTANT
# ROLL COMMAND = 0, AND IF TAU NZ, THEN IGNORE THE BD Z-TRANSLATION

W('17,3007', 0o11627, '', 'CCS', 'RBDFAIL', line=260)
W('17,3010', 0o36214, '', 'CAF', 'THREE', line=261)
W('17,3011', 0o13013, '', 'TCF', '+2', line=262)
W('17,3012', 0o36211, '', 'CAF', 'SIX', line=263)
W('17,3013', 0o51516, '', 'INDEX', 'ZNDX', line=264)
W('17,3014', 0o62771, '', 'AD', 'XLN1NDX', line=265)
W('17,3015', 0o50000, '', 'INDEX', 'A', line=266)
W('17,3016', 0o33151, '', 'CA', 'YZTABLE', line=267)
W('17,3017', 0o73162, '', 'MASK', 'BDZJETS', '= 3417 OCT', line=268)
W('17,3020', 0o61451, '', 'AD', 'RWORD1', 'ADD TO ROLL COMMANDS', line=269)
W('17,3021', 0o55502, '', 'TS', 'T5TEMP', 'IF POSSIBLE.  MUST CHECK TAU FIRST', line=270)

W('17,3022', 0o00006, '', 'EXTEND', line=272)
W('17,3023', 0o75011, '', 'MP', 'BIT7', 'DETERMINE THE NET ROLL COMMAND WITH', line=273)
W('17,3024', 0o66061, '', 'AD', '=-4', 'Z-TRANSLATION ADDED ON', line=274)
W('17,3025', 0o55522, '', 'TS', 'NRJETS', 'NET NO. OF +,- ROLL JETS ON', line=275)
W('17,3026', 0o00006, '', 'EXTEND', line=276)
W('17,3027', 0o13033, '', 'BZF', 'TAUCHECK', line=277)

W('17,3030', 0o31502, 'ACRBDZ', 'CA', 'T5TEMP', 'Z-TRANSLATION ACCEPTED EVEN THO WE MAY', line=279)
W('17,3031', 0o55451, '', 'TS', 'RWORD1', 'HAVE INTRODUCED AN UNDESIREABLE ROLL', line=280)
W('17,3032', 0o13274, '', 'TCF', 'ROLLTIME', 'BRANCH TO JET ON-TIME CALCULATIONS', line=281)

W('17,3033', 0o11561, 'TAUCHECK', 'CCS', 'TAU', line=283)
W('17,3034', 0o13040, '', 'TCF', 'NOBDZ', line=284)
W('17,3035', 0o13030, '', 'TCF', 'ACRBDZ', line=285)
W('17,3036', 0o13040, '', 'TCF', 'NOBDZ', line=286)
W('17,3037', 0o13030, '', 'TCF', 'ACRBDZ', line=287)

W('17,3040', 0o31451, 'NOBDZ', 'CA', 'RWORD1', 'Z-TRANSLATION NOT ACCEPTED', line=289)
W('17,3041', 0o00006, '', 'EXTEND', line=290)
W('17,3042', 0o75011, '', 'MP', 'BIT7', line=291)
W('17,3043', 0o67715, '', 'AD', '=-2', line=292)
W('17,3044', 0o55522, '', 'TS', 'NRJETS', line=293)
W('17,3045', 0o13274, '', 'TCF', 'ROLLTIME', 'BRANCH TO JET ON-TIME CALCULATION', line=294)

# Page 1045
# BD QUAD SELECTION FOR ROLL COMMANDS

W('17,3046', 0o11627, 'BDROLL', 'CCS', 'RBDFAIL', line=299)
W('17,3047', 0o13053, '', 'TCF', 'RBFAIL', line=300)
W('17,3050', 0o13057, '', 'TCF', 'RZXLNS', line=301)
W('17,3051', 0o13055, '', 'TCF', 'RDFAIL', line=302)
W('17,3052', 0o13057, '', 'TCF', 'RZXLNS', line=303)
W('17,3053', 0o34334, 'RBFAIL', 'CAF', 'NINE', line=304)
W('17,3054', 0o13061, '', 'TCF', 'TABRZCMD', line=305)
W('17,3055', 0o35771, 'RDFAIL', 'CAF', 'TWELVE', line=306)
W('17,3056', 0o13061, '', 'TCF', 'TABRZCMD', line=307)

W('17,3057', 0o51516, 'RZXLNS', 'INDEX', 'ZNDX', 'NO BD FAILURES', line=309)
W('17,3060', 0o32660, '', 'CA', 'XLNNDX', '+,-,0 Z-TRANSLATION PRESENT', line=310)
W('17,3061', 0o61517, 'TABRZCMD', 'AD', 'RINDEX', line=311)
W('17,3062', 0o50000, '', 'INDEX', 'A', line=312)
W('17,3063', 0o33130, '', 'CA', 'RTABLE', line=313)
W('17,3064', 0o73150, '', 'MASK', 'BDRJETS', '= 34017 OCT', line=314)
W('17,3065', 0o55451, '', 'TS', 'RWORD1', line=315)

W('17,3066', 0o31515, 'ACYCHECK', 'CA', 'YNDX', 'ANY Y-TRANSLATION', line=317)
W('17,3067', 0o00006, '', 'EXTEND', line=318)
W('17,3070', 0o13122, '', 'BZF', 'NOACY', 'NO Y-TRANSLATION', line=319)
W('17,3071', 0o11626, '', 'CCS', 'RACFAIL', line=320)
W('17,3072', 0o36214, '', 'CAF', 'THREE', line=321)
W('17,3073', 0o13075, '', 'TCF', '+2', line=322)
W('17,3074', 0o36211, '', 'CAF', 'SIX', line=323)
W('17,3075', 0o51515, '', 'INDEX', 'YNDX', line=324)
W('17,3076', 0o62771, '', 'AD', 'XLN1NDX', line=325)
W('17,3077', 0o50000, '', 'INDEX', 'A', line=326)
W('17,3100', 0o33151, '', 'CA', 'YZTABLE', line=327)
W('17,3101', 0o73163, '', 'MASK', 'ACYJETS', '= 34360 OCT', line=328)
W('17,3102', 0o61451, '', 'AD', 'RWORD1', line=329)
W('17,3103', 0o55502, '', 'TS', 'T5TEMP', line=330)
W('17,3104', 0o00006, '', 'EXTEND', '', 'FOR EXPLANATION SEE CODING ON RTABLE', line=331)
W('17,3105', 0o75014, '', 'MP', 'BIT4', line=332)
W('17,3106', 0o66061, '', 'AD', '=-4', line=333)
W('17,3107', 0o55522, '', 'TS', 'NRJETS', 'NO. OF NET ROLL JETS', line=334)
W('17,3110', 0o00006, '', 'EXTEND', line=335)
W('17,3111', 0o13115, '', 'BZF', 'TAUCHCK', 'IF NRJETS = 0', line=336)

W('17,3112', 0o31502, 'BDRACZ', 'CA', 'T5TEMP', 'Y-TRANSLATION ACCEPTED', line=338)
W('17,3113', 0o55451, '', 'TS', 'RWORD1', line=339)
W('17,3114', 0o13274, '', 'TCF', 'ROLLTIME', 'BRANCH TO JET ON-TIME CALCULATIONS', line=340)

W('17,3115', 0o11561, 'TAUCHCK', 'CCS', 'TAU', line=342)
W('17,3116', 0o13122, '', 'TCF', 'NOACY', line=343)
W('17,3117', 0o13112, '', 'TCF', 'BDRACZ', line=344)
W('17,3120', 0o13122, '', 'TCF', 'NOACY', line=345)
W('17,3121', 0o13112, '', 'TCF', 'BDRACZ', line=346)

# Page 1046
W('17,3122', 0o31451, 'NOACY', 'CA', 'RWORD1', 'Y-TRANSLATION NOT ACCEPTED', line=349)
W('17,3123', 0o00006, '', 'EXTEND', line=350)
W('17,3124', 0o75014, '', 'MP', 'BIT4', line=351)
W('17,3125', 0o67715, '', 'AD', '=-2', line=352)
W('17,3126', 0o55522, '', 'TS', 'NRJETS', line=353)
W('17,3127', 0o13274, '', 'TCF', 'ROLLTIME', line=354)

# Page 1047
# TABLE FOR ROLL, Y AND Z-TRANSLATION COMMANDS

# EITHER AC OR BD ROLL MAY BE SELECTED.  IF AC ROLL IS SELECTED, Y-TRANSLATIONS MAY BE SATISFIED SIMULTANEOUSLY
# PROVIDED THAT THERE ARE NO AC QUAD FAILURES.  IF THERE ARE AC FAILURES, Y-TRANSLATION COMMANDS WILL BE IGNORED,
# IN WHICH CASE THE ASTRONAUT SHOULD SWITCH TO BD ROLL.
# IF BDROLL IS SELECTED, Z-TRANSLATIONS MAY BE SATISFIED SIMULTANEOUSLY PROVIDED THAT THERE ARE NO BD QUAD
# FAILURES.  IF THERE ARE BD FAILURES, Z-TRANSLATION COMMANDS WILL BE IGNORED, IN WHICH CASE THE ASTRONAUT SHOULD
# SWITCH TO AC ROLL.
# NOTE THAT IF ONE QUAD FAILS (E.G. B FAILED), Z-TRANSLATION IS STILL POSSIBLE AND THAT THE UNDESIRABLE ROLL
# INTRODUCED BY THIS TRANSLATION WILL BE COMPENSATED BY THE TWO AC ROLL JETS ACTUATED BY THE AUTOPILOT LOGIC.

# WORD MAKE UP....RTABLE

# TWO WORDS, CORRESPONDING TO AC OR BD ROLL SELECTION, HAVE BEEN COMBINED INTO ONE TABLE.  THE WORD CORRESPOND-
# ING TO AC ROLL HAS THE FOLLOWING INTERPRETATION..
# BITS 9,10,11 ARE CODED TO GIVE THE NET ROLL TORQUE FOR THE WORD SELECTED.  THE CODING IS..
# BIT NO. 11  10   9              NO. OF ROLL JETS

# 0   0   0                      -2
# 0   0   1                      -1
# 0   1   0                       0
# 0   1   1                      +1
# 1   0   0                      +2

# THIS WORD MAY THEN BE ADDED TO THE WORD SELECTED FROM THE YZ-TRANSLATION TABLE, WHICH HAS THE SAME TYPE OF
# CODING AS ABOVE, AND THE NET ROLL DETERMINED BY SHIFTING THE RESULTANT WORD RIGHT 8 PLACES AND SUBTRACTING FOUR.

# THE WORD CORRESPONDING TO THE BD ROLL HAS A SIMILAR INTERPRETATION, EXCEPT THAT BITS 12, 13, 14 ARE CODED
# (AS ABOVE) TO GIVE THE NET ROLL TORQUE.

# ROLL          TRANS           QUADFAIL        BIAS

W('17,3130', 0o11000, 'RTABLE', 'OCT', '11000', '  0                                             0', kind='data', line=389)
W('17,3131', 0o22125, '', 'OCT', '22125', '  +                                             0', kind='data', line=390)
W('17,3132', 0o00252, '', 'OCT', '00252', '  -                                             0', kind='data', line=391)
W('17,3133', 0o11231, '', 'OCT', '11231', '  0           +Y(+Z)                            3', kind='data', line=392)
W('17,3134', 0o15421, '', 'OCT', '15421', '  +           +Y(+Z)                            3', kind='data', line=393)
W('17,3135', 0o04610, '', 'OCT', '04610', '  -           +Y(+Z)                            3', kind='data', line=394)
W('17,3136', 0o11146, '', 'OCT', '11146', '  0           -Y(-Z)                            6', kind='data', line=395)
W('17,3137', 0o15504, '', 'OCT', '15504', '  +           -Y(-Z)                            6', kind='data', line=396)
W('17,3140', 0o04442, '', 'OCT', '04442', '  -           -Y(-Z)                            6', kind='data', line=397)
W('17,3141', 0o11000, '', 'OCT', '11000', '  0                             A(B)            9', kind='data', line=398)
W('17,3142', 0o15504, '', 'OCT', '15504', '  +                             A(B)            9', kind='data', line=399)
W('17,3143', 0o04610, '', 'OCT', '04610', '  -                             A(B)            9', kind='data', line=400)
W('17,3144', 0o11000, '', 'OCT', '11000', '  0                             C(D)           12', kind='data', line=401)
W('17,3145', 0o15421, '', 'OCT', '15421', '  +                             C(D)           12', kind='data', line=402)
W('17,3146', 0o04442, '', 'OCT', '04442', '  -                             C(D)           12', kind='data', line=403)

# Page 1048
# RTABLE MASKS -

W('17,3147', 0o03760, 'ACRJETS', 'OCT', '03760', kind='data', line=408)
W('17,3150', 0o34017, 'BDRJETS', 'OCT', '34017', kind='data', line=409)

# Page 1049
# Y, Z TRANSLATION TABLE

# ONCE AC OR BD ROLL IS SELECTED THE QUAD PAIR WHICH IS NOT BEING USED TO SATISFY THE ROLL COMMANDS MAY BE
# USED TO SATISFY THE REMAINING TRANSLATION COMMANDS.  HOWEVER, WE MUST MAKE SURE THAT ROLL COMMANDS ARE SATISFIED
# WHEN THEY OCCUR.  THEREFORE, THE Y-Z TRANSLATIONS FROM THIS TABLE WILL BE IGNORED IF THE NET ROLL TORQUE OF THE
# COMBINED WORD IS ZERO AND THE ROLL COMMANDS ARE NON-ZERO.  THIS SITUATION WOULD OCCUR, FOR EXAMPLE, IF WE EN-
# COUNTER SIMULTANEOUS +R +Y -Z COMMANDS AND A QUAD D FAILURE WHILE USING AC FOR ROLL.
# TO FACILITATE THE LOGIC, THE Y-Z TRANSLATION TABLE HAS BEEN CODED IN A MANNER SIMILAR TO THE ROLL TABLE
# ABOVE.
# BITS 9,10,11 ARE CODED TO GIVE THE NET ROLL TORQUE INCURRED BY Z-TRANSLATIONS.  THE WORD SELECTED CAN THEN BE
# ADDED TO THE AC-ROLL WORD AND THE RESULTANT ROLL TORQUE DETERMINED FROM THE COMBINED WORD.  SIMILIARLY BITS
# 12,13,14 ARE CODED TO GIVE THE NET ROLL TORQUE INCURRED BY Y-TRANSLATIONS WHEN BD-ROLL IS SELECTED.

# TRANSLATION   QUADFAIL        BIAS
#
W('17,3151', 0o11000, 'YZTABLE', 'OCT', '11000', '      0                       0', kind='data', line=427)
W('17,3152', 0o11231, '', 'OCT', '11231', '   +Z(+Y)                     0', kind='data', line=428)
W('17,3153', 0o11146, '', 'OCT', '11146', '   -Z(-Y)                     0', kind='data', line=429)
W('17,3154', 0o11000, '', 'OCT', '11000', '      0         B(A)          3', kind='data', line=430)
W('17,3155', 0o04610, '', 'OCT', '04610', '   +Z(+Y)       B(A)          3', kind='data', line=431)
W('17,3156', 0o15504, '', 'OCT', '15504', '   -Z(-Y)       B(A)          3', kind='data', line=432)
W('17,3157', 0o11000, '', 'OCT', '11000', '      0         D(C)          6', kind='data', line=433)
W('17,3160', 0o15421, '', 'OCT', '15421', '   +Z(+Y)       D(C)          6', kind='data', line=434)
W('17,3161', 0o04442, '', 'OCT', '04442', '   -Z(-Y)       D(C)          6', kind='data', line=435)

# YZ-TABLE MASKS-

W('17,3162', 0o03417, 'BDZJETS', 'OCT', '03417', kind='data', line=439)
W('17,3163', 0o34360, 'ACYJETS', 'OCT', '34360', kind='data', line=440)

# ADDITIONAL CONSTANTS

S('=-2', 'equals', 0o7715, line=444)
S('=-4', 'equals', 0o6061, line=445)

# Page 1050
# CALCULATION OF JET ON-TIMES
#
# THE ROTATION COMMANDS (TAU:S), WHICH WERE DETERMINED FROM THE JET SWITCHING LOGIC ON THE BASIS OF SINGLE JET
# OPERATION, MUST NOW BE UPDATED BY THE ACTUAL NUMBER OF JETS TO BE USED IN SATISFYING THESE COMMANDS.  TAU MUST
# ALSO BE DECREMENTED ACCORDING TO THE EXPECTED TORQUE GENERATED BY THE NEW COMMANDS ACTING OVER THE NEXT T5 INT-
# ERVAL.
# IN ORDER TO MAINTAIN ACCURATE KNOWLEDGE OF VEHICLE ANGULAR RATES, WE MUST ALSO PROVIDE EXPECTED FIRING TIMES
# (DFT:S, ALSO IN TERMS OF 1-JET OPERATION) FOR THE RATE FILTER.
# NOTE THAT TRANSLATIONS CAN PRODUCE ROTATIONS EVEN THOUGH NO ROTATIONS WERE CALLED FOR.  NEVERTHELESS, WE MUST
# UPDATE DFT.
# WHEN THE ROTATIONS HAVE FINISHED, WE MUST PROVIDE CHANNEL INFORMATION TO THE T6 PROGRAM TO CONTINUE ON WITH
# THE TRANSLATIONS.  THIS WILL BE DONE IN THE NEXT SECTION.  HOWEVER, TO INSURE THAT JETS ARE NOT FIRED FOR LESS
# THAN A MINIMUM IMPULSE (14MS), ALL JET CHANNEL COMMANDS WILL BE HELD FIXED FROM THE START OF THE T5 PROGRAM FOR
# ATLEAST 14MS UNTIL THE INITIALIZATION OF NEW COMMANDS.  MOREOVER, A 14MS ON-TIME WILL BE ADDED TO ANY ROTATIONAL
# COMMANDS GENERATED BY THE MANUAL CONTROLS OR THE JET SWITCHING LOGIC, AND ALL TRANSLATION COMMANDS WILL BE
# ACTIVE FOR ATLEAST ONE CYCLE OF THE T5 PROGRAM (.1SEC)

# PITCH JET ON-TIME CALCULATION

W('17,3164', 0o11562, 'PITCHTIM', 'CCS', 'TAU1', line=467)
W('17,3165', 0o13174, '', 'TCF', 'PTAUPOS', line=468)
W('17,3166', 0o13170, '', 'TCF', '+2', line=469)
W('17,3167', 0o13172, '', 'TCF', 'PTAUNEG', line=470)
W('17,3170', 0o55550, '', 'TS', 'DFT1', 'NO PITCH ROTATION', line=471)
W('17,3171', 0o13372, '', 'TCF', 'PBYPASS', 'COMMANDS', line=472)

W('17,3172', 0o41523, 'PTAUNEG', 'CS', 'NPJETS', line=474)
W('17,3173', 0o55523, '', 'TS', 'NPJETS', line=475)
W('17,3174', 0o31562, 'PTAUPOS', 'CA', 'TAU1', line=476)
W('17,3175', 0o00006, '', 'EXTEND', line=477)
W('17,3176', 0o51523, '', 'INDEX', 'NPJETS', line=478)
W('17,3177', 0o73353, '', 'MP', 'NJET', line=479)
W('17,3200', 0o55461, '', 'TS', 'BLAST1', line=480)
W('17,3201', 0o63306, '', 'AD', '=-.1SEC', line=481)
W('17,3202', 0o00006, '', 'EXTEND', line=482)
W('17,3203', 0o63214, '', 'BZMF', 'AD14MSP', line=483)
W('17,3204', 0o51523, '', 'INDEX', 'NPJETS', line=484)
W('17,3205', 0o33307, '', 'CA', 'DFTMAX', 'THE PITCH ON-TIME IS GREATER THAN .1 SEC', line=485)
W('17,3206', 0o55550, '', 'TS', 'DFT1', line=486)
W('17,3207', 0o40000, '', 'COM', line=487)
W('17,3210', 0o27562, '', 'ADS', 'TAU1', 'UPDATE TAU1', line=488)
W('17,3211', 0o33310, '', 'CAF', '=+.1SEC', 'LIMIT THE LENGTH OF PITCH ROTATION', line=489)
W('17,3212', 0o55461, '', 'TS', 'BLAST1', 'COMMANDS TO 0.1 SEC SO THAT ONLY', line=490)
W('17,3213', 0o13357, '', 'TCF', 'ASMBLWP', 'X-TRANSLATIONS WILL CONTINUE ON SWITCH', line=491)
# OVER TO TVC
W('17,3214', 0o41461, 'AD14MSP', 'CS', 'BLAST1', 'SEE IF JET ON TIME IS LESS THAN', line=493)
W('17,3215', 0o63313, '', 'AD', '=14MS', 'MINIMUM IMPULSE TIME', line=494)
W('17,3216', 0o00006, '', 'EXTEND', line=495)
W('17,3217', 0o63222, '', 'BZMF', 'PBLASTOK', 'IF SO LIMIT MINIMUM ON TIME TO 14 MS', line=496)
W('17,3220', 0o33313, '', 'CAF', '=14MS', line=497)
# Page 1051
W('17,3221', 0o55461, '', 'TS', 'BLAST1', line=499)
W('17,3222', 0o31461, 'PBLASTOK', 'CA', 'BLAST1', line=500)
W('17,3223', 0o00006, '', 'EXTEND', '', 'THE PITCH COMMANDS WILL BE COMPLETED', line=501)
W('17,3224', 0o71523, '', 'MP', 'NPJETS', 'WITHIN THE TS-CYCLE TIME', line=502)
W('17,3225', 0o23550, '', 'LXCH', 'DFT1', 'FOR USE IN UPDATING RATE FILTER', line=503)
W('17,3226', 0o55562, '', 'TS', 'TAU1', 'ZERO TAU1 (ACC CONTAINS ZERO)', line=504)
W('17,3227', 0o13357, '', 'TCF', 'ASMBLWP', line=505)

# Page 1052
# YAW JET ON-TIME CALCULATION

W('17,3230', 0o11563, 'YAWTIME', 'CCS', 'TAU2', line=510)
W('17,3231', 0o13240, '', 'TCF', 'YTAUPOS', line=511)
W('17,3232', 0o13234, '', 'TCF', '+2', line=512)
W('17,3233', 0o13236, '', 'TCF', 'YTAUNEG', line=513)
W('17,3234', 0o55551, '', 'TS', 'DFT2', 'NO YAW ROTATION COMMANDS', line=514)
W('17,3235', 0o13536, '', 'TCF', 'YBYPASS', line=515)

W('17,3236', 0o41524, 'YTAUNEG', 'CS', 'NYJETS', line=517)
W('17,3237', 0o55524, '', 'TS', 'NYJETS', line=518)
W('17,3240', 0o31563, 'YTAUPOS', 'CA', 'TAU2', line=519)
W('17,3241', 0o00006, '', 'EXTEND', line=520)
W('17,3242', 0o51524, '', 'INDEX', 'NYJETS', line=521)
W('17,3243', 0o73353, '', 'MP', 'NJET', line=522)
W('17,3244', 0o55463, '', 'TS', 'BLAST2', line=523)
W('17,3245', 0o63306, '', 'AD', '=-.1SEC', line=524)
W('17,3246', 0o00006, '', 'EXTEND', line=525)
W('17,3247', 0o63260, '', 'BZMF', 'AD14MSY', line=526)
W('17,3250', 0o51524, '', 'INDEX', 'NYJETS', line=527)
W('17,3251', 0o33307, '', 'CA', 'DFTMAX', 'YAW COMMANDS WILL LAST LONGER THAN .1SEC', line=528)
W('17,3252', 0o55551, '', 'TS', 'DFT2', line=529)
W('17,3253', 0o40000, '', 'COM', line=530)
W('17,3254', 0o27563, '', 'ADS', 'TAU2', 'DECREMENT TAU2', line=531)
W('17,3255', 0o33310, '', 'CAF', '=+.1SEC', 'LIMIT THE LENGTH OF YAW ROTATION COMMAND', line=532)
W('17,3256', 0o55463, '', 'TS', 'BLAST2', 'TO 0.1 SEC SO THAT ONLY X-TRANSLATION', line=533)
W('17,3257', 0o13523, '', 'TCF', 'ASMBLWY', 'WILL CONTINUE ON SWITCH OVER TO TVC', line=534)

W('17,3260', 0o41463, 'AD14MSY', 'CS', 'BLAST2', 'SEE IF JET ON-TIME LESS THAN', line=536)
W('17,3261', 0o63313, '', 'AD', '=14MS', 'MINIMUM IMPULSE TIME', line=537)
W('17,3262', 0o00006, '', 'EXTEND', line=538)
W('17,3263', 0o63266, '', 'BZMF', 'YBLASTOK', 'IF SO, LIMIT MINIMUM ON-TIME TO 14 MS', line=539)
W('17,3264', 0o33313, '', 'CAF', '=14MS', line=540)
W('17,3265', 0o55463, '', 'TS', 'BLAST2', line=541)
W('17,3266', 0o31463, 'YBLASTOK', 'CA', 'BLAST2', 'YAW COMMANDS WILL BE COMPLETED WITHIN', line=542)
W('17,3267', 0o00006, '', 'EXTEND', '', 'THE T5CYCLE TIME', line=543)
W('17,3270', 0o71524, '', 'MP', 'NYJETS', line=544)
W('17,3271', 0o23551, '', 'LXCH', 'DFT2', line=545)
W('17,3272', 0o55563, '', 'TS', 'TAU2', 'ZERO TAU2', line=546)
W('17,3273', 0o13523, '', 'TCF', 'ASMBLWY', line=547)

# Page 1053
# ROLL ON-TIME CALCULATION-

W('17,3274', 0o11561, 'ROLLTIME', 'CCS', 'TAU', line=552)
W('17,3275', 0o13314, '', 'TCF', 'RBLAST', line=553)
W('17,3276', 0o13300, '', 'TCF', '+2', line=554)
W('17,3277', 0o13314, '', 'TCF', 'RBLAST', line=555)
W('17,3300', 0o51522, '', 'INDEX', 'NRJETS', line=556)
W('17,3301', 0o33307, '', 'CA', 'DFTMAX', 'UPDATE DFT EVEN THO NO ROLL COMMANDS ARE', line=557)
W('17,3302', 0o55547, '', 'TS', 'DFT', 'PRESENT', line=558)
W('17,3303', 0o13516, '', 'TCF', 'RBYPASS', line=559)

W('17,3304', 0o77037, '', 'DEC', '-480', '= -.3SEC', kind='data', line=561)
W('17,3305', 0o77277, '', 'DEC', '-320', '= -.2SEC', kind='data', line=562)
W('17,3306', 0o77537, '=-.1SEC', 'DEC', '-160', '= -.1SEC', kind='data', line=563)
W('17,3307', 0o00000, 'DFTMAX', 'DEC', '0', '    0', kind='data', line=564)
W('17,3310', 0o00240, '=+.1SEC', 'DEC', '160', '= +.1SEC', kind='data', line=565)
W('17,3311', 0o00500, '', 'DEC', '320', '= +.2SEC', kind='data', line=566)
W('17,3312', 0o00740, '', 'DEC', '480', '= +.3SEC', kind='data', line=567)
W('17,3313', 0o00027, '=14MS', 'DEC', '23', '=14MS', kind='data', line=568)

W('17,3314', 0o31561, 'RBLAST', 'CA', 'TAU', line=570)
W('17,3315', 0o00006, '', 'EXTEND', line=571)
W('17,3316', 0o51522, '', 'INDEX', 'NRJETS', line=572)
W('17,3317', 0o73353, '', 'MP', 'NJET', line=573)
W('17,3320', 0o55457, '', 'TS', 'BLAST', 'BLAST IS AN INTERMEDIATE VARIABLE', line=574)
# USED IN DETERMINING THE JET ON-TIMES
W('17,3321', 0o63306, '', 'AD', '=-.1SEC', line=576)
W('17,3322', 0o00006, '', 'EXTEND', line=577)
W('17,3323', 0o63334, '', 'BZMF', 'AD14MSR', line=578)
W('17,3324', 0o51522, '', 'INDEX', 'NRJETS', 'THE ROLL ROTATION WILL LAST LONGER', line=579)
W('17,3325', 0o33307, '', 'CA', 'DFTMAX', 'THAN THE T5 CYCLE TIME', line=580)
W('17,3326', 0o55547, '', 'TS', 'DFT', line=581)
W('17,3327', 0o40000, '', 'COM', line=582)
W('17,3330', 0o27561, '', 'ADS', 'TAU', line=583)
W('17,3331', 0o33310, '', 'CAF', '=+.1SEC', 'LIMIT THE LENGTH OF ROLL ROTATION', line=584)
W('17,3332', 0o55457, '', 'TS', 'BLAST', 'COMMANDS TO 0.1 SEC SO THAT ONLY Y-Z', line=585)
W('17,3333', 0o13377, '', 'TCF', 'ASMBLWR', 'TRANSLATION COMMANDS CONTINUE', line=586)

W('17,3334', 0o41457, 'AD14MSR', 'CS', 'BLAST', 'SEE IF THE JET ON-TIME LESS THAN', line=588)
W('17,3335', 0o63313, '', 'AD', '=14MS', 'MINIMUM IMPULSE TIME', line=589)
W('17,3336', 0o00006, '', 'EXTEND', line=590)
W('17,3337', 0o63342, '', 'BZMF', 'RBLASTOK', line=591)
W('17,3340', 0o33313, '', 'CAF', '=14MS', 'IF SO, LIMIT MINIMUM ON-TIME TO 14 MS', line=592)
W('17,3341', 0o55457, '', 'TS', 'BLAST', line=593)
W('17,3342', 0o31457, 'RBLASTOK', 'CA', 'BLAST', line=594)
W('17,3343', 0o00006, '', 'EXTEND', line=595)
W('17,3344', 0o71522, '', 'MP', 'NRJETS', line=596)
W('17,3345', 0o23547, '', 'LXCH', 'DFT', line=597)
W('17,3346', 0o55561, '', 'TS', 'TAU', 'ZERO TAU', line=598)
W('17,3347', 0o13377, '', 'TCF', 'ASMBLWR', line=599)

# Page 1054
W('17,3350', 0o65252, '', 'DEC', '-.333333', '= -1/3', kind='data', line=602)
W('17,3351', 0o57777, '', 'DEC', '-.500000', '= -1/2', kind='data', line=603)
W('17,3352', 0o40000, '', 'DEC', '-.999999', '= -1 (NEGMAX)', kind='data', line=604)
W('17,3353', 0o00000, 'NJET', 'DEC', '0', kind='data', line=605)
W('17,3354', 0o37777, '', 'DEC', '.999999', '= +1 (POSMAX)', kind='data', line=606)
W('17,3355', 0o20000, '', 'DEC', '.500000', '= +1/2', kind='data', line=607)
W('17,3356', 0o12525, '', 'DEC', '.333333', '= +1/3', kind='data', line=608)

# Page 1055
# WHEN THE ROTATION COMMANDS ARE COMPLETED, IT IS NECESSARY TO REPLACE THESE COMMANDS BY NEW COMMANDS WHICH
# CONTINUE ON WITH THE TRANSLATIONS IF ANY ARE PRESENT.
# IN THIS SECTION THESE NEW COMMANDS ARE GENERATED AND STORED FOR REPLACEMENT OF THE CHANNEL COMMANDS WHEN THE
# CORRESPONDING ROTATIONS ARE COMPLETED.

# GENERATION OF THE SECOND PITCH(X-TRANS) WORD...PWORD2

W('17,3357', 0o11626, 'ASMBLWP', 'CCS', 'RACFAIL', line=618)
W('17,3360', 0o13366, '', 'TCF', 'FPX2', 'IF FAILURE ON AC IGNORE X-TRANSLATION', line=619)
W('17,3361', 0o13363, '', 'TCF', '+2', line=620)
W('17,3362', 0o13366, '', 'TCF', 'FPX2', line=621)
W('17,3363', 0o51513, '', 'INDEX', 'XNDX1', line=622)
W('17,3364', 0o32660, '', 'CA', 'XLNNDX', line=623)
W('17,3365', 0o50000, '', 'INDEX', 'A', line=624)
W('17,3366', 0o32714, 'FPX2', 'CA', 'PYTABLE', line=625)
W('17,3367', 0o72733, '', 'MASK', 'PJETS', line=626)
W('17,3370', 0o55454, '', 'TS', 'PWORD2', line=627)
W('17,3371', 0o13230, '', 'TCF', 'YAWTIME', line=628)

W('17,3372', 0o31453, 'PBYPASS', 'CA', 'PWORD1', 'THE T6 PROGRAM WILL LOAD PWORD2', line=630)
W('17,3373', 0o55454, '', 'TS', 'PWORD2', 'UPON ENTRY', line=631)
W('17,3374', 0o35021, '', 'CAF', 'ZERO', line=632)
W('17,3375', 0o55461, '', 'TS', 'BLAST1', 'THERE IS NO PWORD2', line=633)
W('17,3376', 0o13230, '', 'TCF', 'YAWTIME', line=634)

# Page 1056
# GENERATION OF THE SECOND ROLL (Y,Z) WORD (RWORD2)

W('17,3377', 0o11515, 'ASMBLWR', 'CCS', 'YNDX', 'CHECK FOR Y-TRANS', line=639)
W('17,3400', 0o13410, '', 'TCF', 'ACBD2Y', line=640)
W('17,3401', 0o35021, 'NO2Y', 'CAF', 'ZERO', line=641)
W('17,3402', 0o55452, '', 'TS', 'RWORD2', line=642)
W('17,3403', 0o11516, '', 'CCS', 'ZNDX', 'CHECK FOR Z-TRANS', line=643)
W('17,3404', 0o13453, '', 'TCF', 'ACBD2Z', line=644)
W('17,3405', 0o35021, 'NO2Z', 'CAF', 'ZERO', line=645)
W('17,3406', 0o27452, '', 'ADS', 'RWORD2', line=646)
W('17,3407', 0o13164, '', 'TCF', 'PITCHTIM', 'RWORD2 ASSEMBLED', line=647)

W('17,3410', 0o11630, 'ACBD2Y', 'CCS', 'ACORBD', line=649)
W('17,3411', 0o13426, '', 'TCF', 'AC2Y', 'CAN DO Y-TRANS', line=650)
W('17,3412', 0o13426, '', 'TCF', 'AC2Y', line=651)
W('17,3413', 0o13414, '', 'TCF', '+1', 'USING AC FOR ROLL', line=652)
W('17,3414', 0o11626, '', 'CCS', 'RACFAIL', line=653)
W('17,3415', 0o13401, '', 'TCF', 'NO2Y', 'USING AC AND AC HAS FAILED', line=654)
W('17,3416', 0o13420, '', 'TCF', '+2', line=655)
W('17,3417', 0o13401, '', 'TCF', 'NO2Y', 'DITTO', line=656)

W('17,3420', 0o51515, '', 'INDEX', 'YNDX', 'NO FAILURES, CAN DO Y', line=658)
W('17,3421', 0o32660, '', 'CA', 'XLNNDX', line=659)
W('17,3422', 0o50000, '', 'INDEX', 'A', line=660)
W('17,3423', 0o33130, '', 'CA', 'RTABLE', line=661)
W('17,3424', 0o73147, '', 'MASK', 'ACRJETS', line=662)
W('17,3425', 0o13402, '', 'TCF', 'NO2Y +1', line=663)

W('17,3426', 0o11626, 'AC2Y', 'CCS', 'RACFAIL', line=665)
W('17,3427', 0o36214, '', 'CAF', 'THREE', line=666)
W('17,3430', 0o13432, '', 'TCF', '+2', line=667)
W('17,3431', 0o36211, '', 'CAF', 'SIX', line=668)
W('17,3432', 0o51515, '', 'INDEX', 'YNDX', line=669)
W('17,3433', 0o62771, '', 'AD', 'XLN1NDX', line=670)
W('17,3434', 0o50000, '', 'INDEX', 'A', line=671)
W('17,3435', 0o33151, '', 'CA', 'YZTABLE', line=672)
W('17,3436', 0o73163, '', 'MASK', 'ACYJETS', line=673)
W('17,3437', 0o55452, '', 'TS', 'RWORD2', line=674)
W('17,3440', 0o00006, '', 'EXTEND', line=675)
W('17,3441', 0o75014, '', 'MP', 'BIT4', line=676)
W('17,3442', 0o67715, '', 'AD', '=-2', line=677)
W('17,3443', 0o55522, '', 'TS', 'NRJETS', line=678)
W('17,3444', 0o41457, '', 'CS', 'BLAST', line=679)
W('17,3445', 0o63310, '', 'AD', '=+.1SEC', line=680)
W('17,3446', 0o00006, '', 'EXTEND', line=681)
W('17,3447', 0o71522, '', 'MP', 'NRJETS', line=682)
W('17,3450', 0o30001, '', 'CA', 'L', line=683)
W('17,3451', 0o27547, '', 'ADS', 'DFT', line=684)
W('17,3452', 0o13403, '', 'TCF', 'NO2Y +2', line=685)
# Page 1057
W('17,3453', 0o11630, 'ACBD2Z', 'CCS', 'ACORBD', line=687)
W('17,3454', 0o13504, '', 'TCF', 'BDF2Z', 'USING BD-ROLL', line=688)
W('17,3455', 0o13504, '', 'TCF', 'BDF2Z', 'MUST CHECK FOR BD FAILURES', line=689)
W('17,3456', 0o13457, '', 'TCF', '+1', line=690)
W('17,3457', 0o11627, '', 'CCS', 'RBDFAIL', 'USING AC FOR ROLL, CAN DO Z-TRANS', line=691)
W('17,3460', 0o36214, '', 'CAF', 'THREE', line=692)
W('17,3461', 0o13463, '', 'TCF', '+2', line=693)
W('17,3462', 0o36211, '', 'CAF', 'SIX', line=694)
W('17,3463', 0o51516, '', 'INDEX', 'ZNDX', line=695)
W('17,3464', 0o62771, '', 'AD', 'XLN1NDX', line=696)
W('17,3465', 0o50000, '', 'INDEX', 'A', line=697)
W('17,3466', 0o33151, '', 'CA', 'YZTABLE', line=698)
W('17,3467', 0o73162, '', 'MASK', 'BDZJETS', line=699)
W('17,3470', 0o27452, '', 'ADS', 'RWORD2', line=700)
W('17,3471', 0o00006, '', 'EXTEND', line=701)
W('17,3472', 0o75011, '', 'MP', 'BIT7', line=702)
W('17,3473', 0o67715, '', 'AD', '=-2', line=703)
W('17,3474', 0o55522, '', 'TS', 'NRJETS', line=704)
W('17,3475', 0o41457, '', 'CS', 'BLAST', line=705)
W('17,3476', 0o63310, '', 'AD', '=+.1SEC', line=706)
W('17,3477', 0o00006, '', 'EXTEND', line=707)
W('17,3500', 0o71522, '', 'MP', 'NRJETS', line=708)
W('17,3501', 0o30001, '', 'CA', 'L', line=709)
W('17,3502', 0o27547, '', 'ADS', 'DFT', line=710)
W('17,3503', 0o13164, '', 'TCF', 'PITCHTIM', line=711)

W('17,3504', 0o11627, 'BDF2Z', 'CCS', 'RBDFAIL', line=713)
W('17,3505', 0o13405, '', 'TCF', 'NO2Z', 'USING BD-ROLL AND BD HAS FAILED', line=714)
W('17,3506', 0o13510, '', 'TCF', '+2', line=715)
W('17,3507', 0o13405, '', 'TCF', 'NO2Z', 'DITTO', line=716)
W('17,3510', 0o51516, '', 'INDEX', 'ZNDX', line=717)
W('17,3511', 0o32660, '', 'CA', 'XLNNDX', line=718)
W('17,3512', 0o50000, '', 'INDEX', 'A', line=719)
W('17,3513', 0o33130, '', 'CA', 'RTABLE', line=720)
W('17,3514', 0o73150, '', 'MASK', 'BDRJETS', line=721)
W('17,3515', 0o13406, '', 'TCF', 'NO2Z +1', line=722)

W('17,3516', 0o31451, 'RBYPASS', 'CA', 'RWORD1', line=724)
W('17,3517', 0o55452, '', 'TS', 'RWORD2', line=725)
W('17,3520', 0o35021, '', 'CAF', 'ZERO', line=726)
W('17,3521', 0o55457, '', 'TS', 'BLAST', line=727)
W('17,3522', 0o13164, '', 'TCF', 'PITCHTIM', line=728)

# Page 1058
# GENERATION OF THE SECOND YAW (X-TRANS) WORD...YWORD2

W('17,3523', 0o11627, 'ASMBLWY', 'CCS', 'RBDFAIL', line=733)
W('17,3524', 0o13532, '', 'TCF', 'FYX2', 'IF FAILURE ON BD IGNORE X-TRANSLATION', line=734)
W('17,3525', 0o13527, '', 'TCF', '+2', line=735)
W('17,3526', 0o13532, '', 'TCF', 'FYX2', line=736)
W('17,3527', 0o51514, '', 'INDEX', 'XNDX2', line=737)
W('17,3530', 0o32660, '', 'CA', 'XLNNDX', line=738)
W('17,3531', 0o50000, '', 'INDEX', 'A', line=739)
W('17,3532', 0o32714, 'FYX2', 'CA', 'PYTABLE', line=740)
W('17,3533', 0o72734, '', 'MASK', 'YJETS', line=741)
W('17,3534', 0o55456, '', 'TS', 'YWORD2', line=742)
W('17,3535', 0o13542, '', 'TCF', 'T6SETUP', line=743)

W('17,3536', 0o31455, 'YBYPASS', 'CA', 'YWORD1', line=745)
W('17,3537', 0o55456, '', 'TS', 'YWORD2', line=746)
W('17,3540', 0o35021, '', 'CAF', 'ZERO', line=747)
W('17,3541', 0o55463, '', 'TS', 'BLAST2', line=748)

# Page 1059
# SORT THE JET ON-TIMES

# AT THIS POINT ALL THE CHANNEL COMMANDS AND JET ON-TIMES HAVE BEEN DETERMINED.  IN SUMMARY THESE ARE-

# RWORD1
# RWORD2          BLAST

# PWORD1
# PWORD2          BLAST1

# YWORD1
# YWORD2          BLAST2

# IN THIS SECTION THE JET ON-TIMES ARE SORTED AND THE SEQUENCE OF T6 INTERRUPTS IS DETERMINED.  TO FACILITATE
# THE SORTING PROCESS AND THE T6 PROGRAM, THE VARIABLES BLAST, BLAST1, BLAST2, ARE RESERVED AS DOUBLE PRECISION
# WORDS.  THE LOWER PART OF THESE WORDS CONTAIN A BRANCH INDEX ASSOCIATED WITH THE ROTATION AXIS OF THE HIGHER
# ORDER WORD.

W('17,3542', 0o35021, 'T6SETUP', 'CAF', 'ZERO', 'BRANCH INDEX FOR ROLL', line=769)
W('17,3543', 0o55460, '', 'TS', 'BLAST +1', line=770)
W('17,3544', 0o35015, '', 'CAF', 'FOUR', 'BRANCH INDEX FOR PITCH', line=771)
W('17,3545', 0o55462, '', 'TS', 'BLAST1 +1', line=772)
W('17,3546', 0o35024, '', 'CAF', 'ELEVEN', 'BRANCH INDEX FOR YAW', line=773)
W('17,3547', 0o55464, '', 'TS', 'BLAST2 +1', line=774)

W('17,3550', 0o41457, '', 'CS', 'BLAST', line=776)
W('17,3551', 0o61461, '', 'AD', 'BLAST1', line=777)
W('17,3552', 0o00006, '', 'EXTEND', line=778)
W('17,3553', 0o63577, '', 'BZMF', 'DXCHT12', 'T1 GR T2', line=779)
W('17,3554', 0o41461, 'CHECKT23', 'CS', 'BLAST1', line=780)
W('17,3555', 0o61463, '', 'AD', 'BLAST2', line=781)
W('17,3556', 0o00006, '', 'EXTEND', line=782)
W('17,3557', 0o63603, '', 'BZMF', 'DXCHT23', line=783)
W('17,3560', 0o41461, 'CALCDT6', 'CS', 'BLAST1', line=784)
W('17,3561', 0o27463, '', 'ADS', 'BLAST2', line=785)
W('17,3562', 0o41457, '', 'CS', 'BLAST', line=786)
W('17,3563', 0o27461, '', 'ADS', 'BLAST1', 'END OF SORTING PROCEDURE', line=787)
W('17,3564', 0o00006, '', 'EXTEND', '', 'RESET T5LOC TO BEGIN PHASE1', line=788)
W('17,3565', 0o33576, '', 'DCA', 'RCS2CADR', line=789)
W('17,3566', 0o53313, '', 'DXCH', 'T5LOC', line=790)
W('17,3567', 0o45017, 'ENDJETS', 'CS', 'BIT1', 'RESET BIT1 FOR INITIALIZATION OF', line=791)
W('17,3570', 0o71501, '', 'MASK', 'RCSFLAGS', 'T6 PROGRAM', line=792)
W('17,3571', 0o55501, '', 'TS', 'RCSFLAGS', line=793)
W('17,3572', 0o45021, '', 'CS', 'ZERO', 'RESET T5PHASE FOR PHASE1', line=794)
W('17,3573', 0o55465, '', 'TS', 'T5PHASE', line=795)
W('17,3574', 0o15333, '', 'TCF', 'RESUME', 'RESUME INTERRUPTED PROGRAM', line=796)

#   EBANK= KMPAC
W('17,3575', 0o02122, 'RCS2CADR', '2CADR', 'RCSATT', kind='data', line=799)
W('17,3576', 0o42066, kind='data', line=799)

# Page 1060
W('17,3577', 0o53460, 'DXCHT12', 'DXCH', 'BLAST', line=802)
W('17,3600', 0o53462, '', 'DXCH', 'BLAST1', line=803)
W('17,3601', 0o53460, '', 'DXCH', 'BLAST', line=804)
W('17,3602', 0o13554, '', 'TCF', 'CHECKT23', line=805)

W('17,3603', 0o53462, 'DXCHT23', 'DXCH', 'BLAST1', line=807)
W('17,3604', 0o53464, '', 'DXCH', 'BLAST2', line=808)
W('17,3605', 0o53462, '', 'DXCH', 'BLAST1', line=809)
W('17,3606', 0o41457, '', 'CS', 'BLAST', line=810)
W('17,3607', 0o61461, '', 'AD', 'BLAST1', line=811)
W('17,3610', 0o00006, '', 'EXTEND', line=812)
W('17,3611', 0o63613, '', 'BZMF', '+2', line=813)
W('17,3612', 0o13560, '', 'TCF', 'CALCDT6', line=814)
W('17,3613', 0o53460, '', 'DXCH', 'BLAST', line=815)
W('17,3614', 0o53462, '', 'DXCH', 'BLAST1', line=816)
W('17,3615', 0o53460, '', 'DXCH', 'BLAST', line=817)
W('17,3616', 0o13560, '', 'TCF', 'CALCDT6', line=818)

# Page 1061
# T6 PROGRAM AND CHANNEL SETUP

#   BANK 21
#   SETLOC DAPS5
#   BANK

W('17,3617', 0o22016, 'T6START', 'LXCH', 'BANKRUPT', line=827)
W('17,3620', 0o00006, '', 'EXTEND', line=828)
W('17,3621', 0o22012, '', 'QXCH', 'QRUPT', line=829)
W('17,3622', 0o10031, '', 'CCS', 'TIME6', 'CHECK TO SEE IF TIME6 WAS RESET', line=830)
W('17,3623', 0o15333, '', 'TCF', 'RESUME', 'AFTER T6RUPT OCCURED(IN T5RUPT)', line=831)
W('17,3624', 0o13626, '', 'TCF', '+2', 'IF SO WAIT FOR NEXT T6RUPT BEFORE', line=832)
W('17,3625', 0o15333, '', 'TCF', 'RESUME', 'TAKING ACTION', line=833)

W('17,3626', 0o41501, '', 'CS', 'RCSFLAGS', line=835)
W('17,3627', 0o75017, '', 'MASK', 'BIT1', 'IF BIT1 IS 0 RESET TO 1', line=836)
W('17,3630', 0o00006, '', 'EXTEND', '', 'AND INITIALIZE CHANNEL', line=837)
W('17,3631', 0o13642, '', 'BZF', 'T6RUPTOR', line=838)
W('17,3632', 0o27501, '', 'ADS', 'RCSFLAGS', line=839)
W('17,3633', 0o31451, '', 'CA', 'RWORD1', line=840)
W('17,3634', 0o00006, '', 'EXTEND', '', 'INITIALIZE CHANNELS 5,6 WITH WORD1', line=841)
W('17,3635', 0o01006, '', 'WRITE', 'CHAN6', line=842)
W('17,3636', 0o31453, '', 'CA', 'PWORD1', line=843)
W('17,3637', 0o61455, '', 'AD', 'YWORD1', line=844)
W('17,3640', 0o00006, '', 'EXTEND', line=845)
W('17,3641', 0o01005, '', 'WRITE', 'CHAN5', line=846)

W('17,3642', 0o11457, 'T6RUPTOR', 'CCS', 'BLAST', line=848)
W('17,3643', 0o13722, '', 'TCF', 'ZBLAST', 'ZERO BLAST1', line=849)
W('17,3644', 0o13661, '', 'TCF', 'REPLACE', 'REPLACE WORD1', line=850)
W('17,3645', 0o13647, '', 'TCF', '+2', line=851)
W('17,3646', 0o13661, '', 'TCF', 'REPLACE', line=852)
W('17,3647', 0o11461, 'T6L1', 'CCS', 'BLAST1', line=853)
W('17,3650', 0o13725, '', 'TCF', 'ZBLAST1', line=854)
W('17,3651', 0o13666, '', 'TCF', 'REPLACE1', line=855)
W('17,3652', 0o13654, '', 'TCF', '+2', line=856)
W('17,3653', 0o13666, '', 'TCF', 'REPLACE1', line=857)
W('17,3654', 0o11463, 'T6L2', 'CCS', 'BLAST2', line=858)
W('17,3655', 0o13730, '', 'TCF', 'ZBLAST2', line=859)
W('17,3656', 0o13673, '', 'TCF', 'REPLACE2', line=860)
W('17,3657', 0o15333, '', 'TCF', 'RESUME', line=861)
W('17,3660', 0o13673, '', 'TCF', 'REPLACE2', line=862)

W('17,3661', 0o51460, 'REPLACE', 'INDEX', 'BLAST +1', line=864)
W('17,3662', 0o03700, '', 'TC', 'REPLACER', line=865)
W('17,3663', 0o45017, '', 'CS', 'ONE', line=866)
W('17,3664', 0o55457, '', 'TS', 'BLAST', line=867)
W('17,3665', 0o13647, '', 'TCF', 'T6L1', line=868)

W('17,3666', 0o51462, 'REPLACE1', 'INDEX', 'BLAST1 +1', line=870)
# Page 1062
W('17,3667', 0o03700, '', 'TC', 'REPLACER', line=872)
W('17,3670', 0o45017, '', 'CS', 'ONE', line=873)
W('17,3671', 0o55461, '', 'TS', 'BLAST1', line=874)
W('17,3672', 0o13654, '', 'TCF', 'T6L2', line=875)

W('17,3673', 0o51464, 'REPLACE2', 'INDEX', 'BLAST2 +1', line=877)
W('17,3674', 0o03700, '', 'TC', 'REPLACER', line=878)
W('17,3675', 0o45017, '', 'CS', 'ONE', line=879)
W('17,3676', 0o55463, '', 'TS', 'BLAST2', line=880)
W('17,3677', 0o15333, '', 'TCF', 'RESUME', line=881)

W('17,3700', 0o31452, 'REPLACER', 'CA', 'RWORD2', line=883)
W('17,3701', 0o00006, '', 'EXTEND', '', 'INITIALIZE CHANNELS 5,6 WITH WORD2', line=884)
W('17,3702', 0o01006, '', 'WRITE', 'CHAN6', line=885)
W('17,3703', 0o00002, '', 'TC', 'Q', line=886)

W('17,3704', 0o32734, 'REPLACEP', 'CA', 'YJETS', line=888)
W('17,3705', 0o00006, '', 'EXTEND', line=889)
W('17,3706', 0o02005, '', 'RAND', 'CHAN5', line=890)
W('17,3707', 0o61454, '', 'AD', 'PWORD2', line=891)
W('17,3710', 0o00006, '', 'EXTEND', line=892)
W('17,3711', 0o01005, '', 'WRITE', 'CHAN5', line=893)
W('17,3712', 0o00002, '', 'TC', 'Q', line=894)

W('17,3713', 0o32733, 'REPLACEY', 'CA', 'PJETS', line=896)
W('17,3714', 0o00006, '', 'EXTEND', line=897)
W('17,3715', 0o02005, '', 'RAND', 'CHAN5', line=898)
W('17,3716', 0o61456, '', 'AD', 'YWORD2', line=899)
W('17,3717', 0o00006, '', 'EXTEND', line=900)
W('17,3720', 0o01005, '', 'WRITE', 'CHAN5', line=901)
W('17,3721', 0o00002, '', 'TC', 'Q', line=902)

W('17,3722', 0o35021, 'ZBLAST', 'CAF', 'ZERO', line=904)
W('17,3723', 0o57457, '', 'XCH', 'BLAST', line=905)
W('17,3724', 0o13732, '', 'TCF', 'ENABT6', line=906)
W('17,3725', 0o35021, 'ZBLAST1', 'CAF', 'ZERO', line=907)
W('17,3726', 0o57461, '', 'XCH', 'BLAST1', line=908)
W('17,3727', 0o13732, '', 'TCF', 'ENABT6', line=909)
W('17,3730', 0o35021, 'ZBLAST2', 'CAF', 'ZERO', line=910)
W('17,3731', 0o57463, '', 'XCH', 'BLAST2', line=911)
W('17,3732', 0o54031, 'ENABT6', 'TS', 'TIME6', line=912)
W('17,3733', 0o35001, '', 'CAF', 'NEGMAX', line=913)
W('17,3734', 0o00006, '', 'EXTEND', line=914)
W('17,3735', 0o05013, '', 'WOR', 'CHAN13', 'ENABLE T6RUPT', line=915)
W('17,3736', 0o15333, '', 'TCF', 'RESUME', line=916)

# END OF T6 INTERRUPT

S('ENDSLECT', 'equals', 0o47737, line=920)
