"""IMU_PERFORMANCE_TESTS_4.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/IMU_PERFORMANCE_TESTS_4.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 382-389 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('IMU_PERFORMANCE_TESTS_4', 'IMU_PERFORMANCE_TESTS_4.agc', 'Luminary099', pages='382-389')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     IMU_PERFORMANCE_TESTS_4.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        382-389
# Mod history:  2009-05-17 RSB  Adapted from the corresponding
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

# Page 382
# PROGRAM --    IMU PERFORMANCE TESTS 4
# DATE --       NOV 15, 1966
# BY --         GEORGE SCHMIDT IL7-146 EXT 1126
# MOD NO-ZERO
#
# FUNCTIONAL DESCRIPTION
#
# THIS SECTION CONSISTS OF THE FILTER FOR THE GYRO DRIFT TESTS.  NO COMPASS
# IS DONE IN LEM.  FOR A DESCRIPTION OF THE FILTER SEE E-1973.  THIS
# SECTION IS ENTERED FROM IMU 2.  IT RETURNS THERE AT END OF TEST.
#
# EARTHR,OGC ZERO,ERTHRVSE
#
# NORMAL EXIT
#
# LENGTHOT GOES TO ZERO -- RETURN TO IMU PERF TESTS 2 CONTROL
#
# ALARMS
#
# 1600  OVERFLOW IN DRIFT TEST
# 1601  BAD IMU MODING IN ANY ROUTINE THAT USES IMUSTALL
# OUTPUT
#
# FLASHING DISPLAY OF RESULTS -- CONTROLLED IN IMU PERF TESTS 2
#
# DEBRIS
#
# ALL CENTRALS -- ALL OF EBANK XSM

# Page 383
#   BANK 33
#   SETLOC IMU4
#   BANK
#   COUNT* $$/P07

#   EBANK= XSM

W('37,2500', 0o00004, 'ESTIMS', 'INHINT', line=67)
W('37,2501', 0o31572, '', 'CAE', '1SECXT', line=68)
W('37,2502', 0o05173, '', 'TC', 'TWIDDLE', line=69)
#   EBANK= XSM
W('37,2503', 0o02536, '', 'ADRES', 'ALLOOP', kind='data', line=71)
W('37,2504', 0o34755, '', 'CAF', 'ZERO', 'ZERO THE PIPAS', line=72)
W('37,2505', 0o54037, '', 'TS', 'PIPAX', line=73)
W('37,2506', 0o54040, '', 'TS', 'PIPAY', line=74)
W('37,2507', 0o54041, '', 'TS', 'PIPAZ', line=75)
W('37,2510', 0o00003, '', 'RELINT', line=76)
W('37,2511', 0o33075, '', 'CA', '77DECML', line=77)
W('37,2512', 0o55571, '', 'TS', 'ZERONDX', line=78)
W('37,2513', 0o33076, '', 'CA', 'ALXXXZ', line=79)
W('37,2514', 0o02367, '', 'TC', 'ZEROING', line=80)
W('37,2515', 0o06037, '', 'TC', 'INTPRET', line=81)
W('37,2516', 0o77735, '', 'SLOAD', kind='interp', line=82)
W('37,2517', 0o37057, '', '', 'SCHZEROS', kind='operand', line=83)
W('37,2520', 0o25477, '', 'STOVL', 'GCOMPSW -1', kind='interp', line=84)
W('37,2521', 0o37070, '', '', 'INTVAL +2', kind='operand', line=85)
W('37,2522', 0o26445, '', 'STOVL', 'ALX1S', kind='interp', line=86)
W('37,2523', 0o37057, '', '', 'SCHZEROS', kind='operand', line=87)
W('37,2524', 0o00325, '', 'STORE', 'DELVX', kind='interp', line=88)
W('37,2525', 0o01472, '', 'STORE', 'GCOMP', kind='interp', line=89)
W('37,2526', 0o77735, '', 'SLOAD', kind='interp', line=90)
W('37,2527', 0o02441, '', '', 'TORQNDX', kind='operand', line=91)
W('37,2530', 0o50076, '', 'DCOMP', 'BMN', kind='interp', line=92)
W('37,2531', 0o76534, '', '', 'VERTSKIP', kind='operand', line=93)
W('37,2532', 0o77624, '', 'CALL', kind='interp', line=94)
W('37,2533', 0o76401, '', '', 'ERTHRVSE', kind='operand', line=95)
W('37,2534', 0o77776, 'VERTSKIP', 'EXIT', kind='interp', line=96)
W('37,2535', 0o03035, '', 'TC', 'SLEEPIE +1', line=97)

# Page 384
W('37,2536', 0o31576, 'ALLOOP', 'CA', 'OVFLOWCK', line=100)
W('37,2537', 0o00006, '', 'EXTEND', line=101)
W('37,2540', 0o12542, '', 'BZF', '+2', line=102)
W('37,2541', 0o05261, '', 'TC', 'TASKOVER', line=103)
W('37,2542', 0o11530, '', 'CCS', 'ALTIM', line=104)
W('37,2543', 0o30000, '', 'CA', 'A', 'SHOULD NEVER HIT THIS LOCATION', line=105)
W('37,2544', 0o55531, '', 'TS', 'ALTIMS', line=106)
W('37,2545', 0o40000, '', 'CS', 'A', line=107)
W('37,2546', 0o55530, '', 'TS', 'ALTIM', line=108)
W('37,2547', 0o44753, '', 'CS', 'ONE', line=109)
W('37,2550', 0o61562, '', 'AD', 'GEOCOMPS', line=110)
W('37,2551', 0o00006, '', 'EXTEND', line=111)
W('37,2552', 0o12556, '', 'BZF', '+4', line=112)
W('37,2553', 0o31412, '', 'CA', 'LENGTHOT', line=113)
W('37,2554', 0o00006, '', 'EXTEND', line=114)
W('37,2555', 0o62562, '', 'BZMF', '+5', line=115)
W('37,2556', 0o31572, '', 'CAE', '1SECXT', line=116)
W('37,2557', 0o05173, '', 'TC', 'TWIDDLE', line=117)
#   EBANK= XSM
W('37,2560', 0o02536, '', 'ADRES', 'ALLOOP', kind='data', line=119)
W('37,2561', 0o34755, '', 'CAF', 'ZERO', line=120)
W('37,2562', 0o56037, '', 'XCH', 'PIPAX', line=121)
W('37,2563', 0o54324, '', 'TS', 'DELVX', line=122)
W('37,2564', 0o34755, '', 'CAF', 'ZERO', line=123)
W('37,2565', 0o56040, '', 'XCH', 'PIPAY', line=124)
W('37,2566', 0o54326, '', 'TS', 'DELVY', line=125)
W('37,2567', 0o34755, '', 'CAF', 'ZERO', line=126)
W('37,2570', 0o56041, '', 'XCH', 'PIPAZ', line=127)
W('37,2571', 0o54330, '', 'TS', 'DELVZ', line=128)
W('37,2572', 0o34736, 'SPECSTS', 'CAF', 'PRIO20', line=129)
W('37,2573', 0o05105, '', 'TC', 'FINDVAC', line=130)
#   EBANK= XSM
W('37,2574', 0o02577, '', '2CADR', 'ALFLT', 'START THE JOB', kind='data', line=132)
W('37,2575', 0o76065, kind='data', line=132)

W('37,2576', 0o05261, '', 'TC', 'TASKOVER', line=134)

# Page 385
W('37,2577', 0o11562, 'ALFLT', 'CCS', 'GEOCOMPS', line=137)
W('37,2600', 0o02602, '', 'TC', '+2', line=138)
W('37,2601', 0o02604, '', 'TC', 'NORMLOP', line=139)
W('37,2602', 0o04616, '', 'TC', 'BANKCALL', line=140)
W('37,2603', 0o15263, '', 'CADR', '1/PIPA', kind='data', line=141)
W('37,2604', 0o06037, 'NORMLOP', 'TC', 'INTPRET', line=142)
W('37,2605', 0o77745, '', 'DLOAD', kind='interp', line=143)
W('37,2606', 0o37066, '', '', 'INTVAL', kind='operand', line=144)
W('37,2607', 0o24051, '', 'STOVL', 'S1', kind='interp', line=145)
W('37,2610', 0o00325, '', '', 'DELVX', kind='operand', line=146)
W('37,2611', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=147)
W('37,2612', 0o02643, '', '', 'XSM', kind='operand', line=148)
W('37,2613', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=149)
W('37,2614', 0o00160, '', '', 'MPAC +3', kind='operand', line=150)
W('37,2615', 0o16523, '', 'STODL', 'DPIPAY', kind='interp', line=151)
W('37,2616', 0o00162, '', '', 'MPAC +5', kind='operand', line=152)
W('37,2617', 0o02527, '', 'STORE', 'DPIPAZ', kind='interp', line=153)

W('37,2620', 0o76001, '', 'SETPD', 'AXT,1', kind='interp', line=155)
W('37,2621', 0o00001, '', '', '0', kind='operand', line=156)
W('37,2622', 0o00010, '', '', '8D', kind='operand', line=157)
W('37,2623', 0o57535, '', 'SLOAD', 'DCOMP', kind='interp', line=158)
W('37,2624', 0o02563, '', '', 'GEOCOMPS', kind='operand', line=159)
W('37,2625', 0o77640, '', 'BMN', kind='interp', line=160)
W('37,2626', 0o76772, '', '', 'PERFERAS', kind='operand', line=161)
W('37,2627', 0o50135, 'ALCGKK', 'SLOAD', 'BMN', kind='interp', line=162)
W('37,2630', 0o02532, '', '', 'ALTIMS', kind='operand', line=163)
W('37,2631', 0o76644, '', '', 'ALFLT3', kind='operand', line=164)
W('37,2632', 0o72174, 'ALKCG', 'AXT,2', 'LXA,1', 'LOADS SLOPES AND TIME CONSTANTS AT RQST', kind='interp', line=165)
W('37,2633', 0o00014, '', '', '12D', kind='operand', line=166)
W('37,2634', 0o02444, '', '', 'ALX1S', kind='operand', line=167)
W('37,2635', 0o62143, 'ALKCG2', 'DLOAD*', 'INCR,1', kind='interp', line=168)
W('37,2636', 0o02243, '', '', 'ALFDK +144D,1', kind='operand', line=169)
W('37,2637', 0o77775, '', 'DEC', '-2', kind='data', line=170)
W('37,2640', 0o12545, '', 'STORE', 'ALDK +10D,2', kind='interp', line=171)
W('37,2641', 0o66104, '', 'TIX,2', 'SXA,1', kind='interp', line=172)
W('37,2642', 0o76635, '', '', 'ALKCG2', kind='operand', line=173)
W('37,2643', 0o02444, '', '', 'ALX1S', kind='operand', line=174)

W('37,2644', 0o77770, 'ALFLT3', 'AXT,1', kind='interp', line=176)
W('37,2645', 0o00010, '', '', '8D', kind='operand', line=177)
W('37,2646', 0o41343, 'DELMLP', 'DLOAD*', 'DMP', kind='interp', line=178)
W('37,2647', 0o02533, '', '', 'DPIPAY +8D,1', kind='operand', line=179)
W('37,2650', 0o37100, '', '', 'PIPASC', kind='operand', line=180)
W('37,2651', 0o43661, '', 'SLR', 'BDSU*', kind='interp', line=181)
W('37,2652', 0o21212, '', '', '9D', kind='operand', line=182)
W('37,2653', 0o02501, '', '', 'INTY +8D,1', kind='operand', line=183)
W('37,2654', 0o06501, '', 'STORE', 'INTY +8D,1', kind='interp', line=184)
W('37,2655', 0o40725, '', 'PDDL', 'DMP*', kind='interp', line=185)
W('37,2656', 0o37102, '', '', 'VELSC', kind='operand', line=186)
# Page 386
W('37,2657', 0o02521, '', '', 'VLAUN +8D,1', kind='operand', line=188)
W('37,2660', 0o77732, '', 'SL2R', kind='interp', line=189)
W('37,2661', 0o45425, '', 'DSU', 'STADR', kind='interp', line=190)
W('37,2662', 0o71216, '', 'STORE', 'DELM +8D,1', kind='interp', line=191)
W('37,2663', 0o06563, '', 'STORE', 'DELM +10D,1', kind='interp', line=192)
W('37,2664', 0o77100, '', 'TIX,1', 'AXT,2', kind='interp', line=193)
W('37,2665', 0o76646, '', '', 'DELMLP', kind='operand', line=194)
W('37,2666', 0o00004, '', '', '4', kind='operand', line=195)
W('37,2667', 0o56743, 'ALILP', 'DLOAD*', 'DMPR*', kind='interp', line=196)
W('37,2670', 0o75324, '', '', 'ALK +4,2', kind='operand', line=197)
W('37,2671', 0o75240, '', '', 'ALDK +4,2', kind='operand', line=198)
W('37,2672', 0o12453, '', 'STORE', 'ALK +4,2', kind='interp', line=199)
W('37,2673', 0o77104, '', 'TIX,2', 'AXT,2', kind='interp', line=200)
W('37,2674', 0o76667, '', '', 'ALILP', kind='operand', line=201)
W('37,2675', 0o00010, '', '', '8D', kind='operand', line=202)
W('37,2676', 0o66140, 'ALKLP', 'LXC,1', 'SXA,1', kind='interp', line=203)
W('37,2677', 0o02445, '', '', 'CMPX1', kind='operand', line=204)
W('37,2700', 0o02445, '', '', 'CMPX1', kind='operand', line=205)
W('37,2701', 0o56743, '', 'DLOAD*', 'DMPR*', kind='interp', line=206)
W('37,2702', 0o02450, '', '', 'ALK +1,1', kind='operand', line=207)
W('37,2703', 0o75216, '', '', 'DELM +8D,2', kind='operand', line=208)
W('37,2704', 0o77613, '', 'DAD*', kind='interp', line=209)
W('37,2705', 0o75276, '', '', 'INTY +8D,2', kind='operand', line=210)
W('37,2706', 0o12501, '', 'STORE', 'INTY +8D,2', kind='interp', line=211)
W('37,2707', 0o42743, '', 'DLOAD*', 'DAD*', kind='interp', line=212)
W('37,2710', 0o75314, '', '', 'ALK +12D,2', kind='operand', line=213)
W('37,2711', 0o75230, '', '', 'ALDK +12D,2', kind='operand', line=214)
W('37,2712', 0o12463, '', 'STORE', 'ALK +12D,2', kind='interp', line=215)
W('37,2713', 0o42673, '', 'DMPR*', 'DAD*', kind='interp', line=216)
W('37,2714', 0o75216, '', '', 'DELM +8D,2', kind='operand', line=217)
W('37,2715', 0o75266, '', '', 'INTY +16D,2', kind='operand', line=218)
W('37,2716', 0o12511, '', 'STORE', 'INTY +16D,2', kind='interp', line=219)
W('37,2717', 0o40743, '', 'DLOAD*', 'DMP*', kind='interp', line=220)
W('37,2720', 0o37105, '', '', 'ALSK +1,1', kind='operand', line=221)
W('37,2721', 0o75216, '', '', 'DELM +8D,2', kind='operand', line=222)
W('37,2722', 0o42772, '', 'SL1R', 'DAD*', kind='interp', line=223)
W('37,2723', 0o75256, '', '', 'VLAUN +8D,2', kind='operand', line=224)
W('37,2724', 0o12521, '', 'STORE', 'VLAUN +8D,2', kind='interp', line=225)
W('37,2725', 0o76104, '', 'TIX,2', 'AXT,1', kind='interp', line=226)
W('37,2726', 0o76676, '', '', 'ALKLP', kind='operand', line=227)
W('37,2727', 0o00010, '', '', '8D', kind='operand', line=228)

W('37,2730', 0o64743, 'LOOSE', 'DLOAD*', 'PDDL*', kind='interp', line=230)
W('37,2731', 0o02523, '', '', 'ACCWD +8D,1', kind='operand', line=231)
W('37,2732', 0o02521, '', '', 'VLAUN +8D,1', kind='operand', line=232)
W('37,2733', 0o55523, '', 'PDDL*', 'VDEF', kind='interp', line=233)
W('37,2734', 0o02531, '', '', 'POSNV +8D,1', kind='operand', line=234)
W('37,2735', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=235)
W('37,2736', 0o02001, '', '', 'TRANSM1', kind='operand', line=236)
# Page 387
W('37,2737', 0o77745, '', 'DLOAD', kind='interp', line=238)
W('37,2740', 0o00155, '', '', 'MPAC', kind='operand', line=239)
W('37,2741', 0o06531, '', 'STORE', 'POSNV +8D,1', kind='interp', line=240)
W('37,2742', 0o77745, '', 'DLOAD', kind='interp', line=241)
W('37,2743', 0o00160, '', '', 'MPAC +3', kind='operand', line=242)
W('37,2744', 0o06521, '', 'STORE', 'VLAUN +8D,1', kind='interp', line=243)
W('37,2745', 0o77745, '', 'DLOAD', kind='interp', line=244)
W('37,2746', 0o00162, '', '', 'MPAC +5', kind='operand', line=245)
W('37,2747', 0o06523, '', 'STORE', 'ACCWD +8D,1', kind='interp', line=246)
W('37,2750', 0o77700, '', 'TIX,1', kind='interp', line=247)
W('37,2751', 0o76730, '', '', 'LOOSE', kind='operand', line=248)

W('37,2752', 0o76174, '', 'AXT,2', 'AXT,1', 'EVALUATE SINES AND COSINES', kind='interp', line=250)
W('37,2753', 0o00006, '', '', '6', kind='operand', line=251)
W('37,2754', 0o00002, '', '', '2', kind='operand', line=252)
W('37,2755', 0o57343, 'BOOP', 'DLOAD*', 'DMPR', kind='interp', line=253)
W('37,2756', 0o02503, '', '', 'ANGX +2,1', kind='operand', line=254)
W('37,2757', 0o37110, '', '', 'GEORGEJ', kind='operand', line=255)
W('37,2760', 0o77722, '', 'SR2R', kind='interp', line=256)
W('37,2761', 0o73406, '', 'PUSH', 'SIN', kind='interp', line=257)
W('37,2762', 0o56072, '', 'SL3R', 'XAD,1', kind='interp', line=258)
W('37,2763', 0o00046, '', '', 'X1', kind='operand', line=259)
W('37,2764', 0o10021, '', 'STORE', '16D,2', kind='interp', line=260)
W('37,2765', 0o77745, '', 'DLOAD', kind='interp', line=261)
W('37,2766', 0o77746, '', 'COS', kind='interp', line=262)
W('37,2767', 0o10027, '', 'STORE', '22D,2', 'COSINES', kind='interp', line=263)
W('37,2770', 0o77704, '', 'TIX,2', kind='interp', line=264)
W('37,2771', 0o76755, '', '', 'BOOP', kind='operand', line=265)

W('37,2772', 0o77776, 'PERFERAS', 'EXIT', kind='interp', line=267)
W('37,2773', 0o35016, '', 'CA', 'EBANK7', line=268)
W('37,2774', 0o54003, '', 'TS', 'EBANK', line=269)
#   EBANK= ATIGINC
W('37,2775', 0o01400, '', 'TC', 'ATIGINC', 'GOTO ERASABLE TO CALCULATE ONLY TO RETN', line=271)

# CAUTION
#
# THE ERASABLE PROGRAM THAT DOES THE CALCULATIONS MUST BE LOADED
# BEFORE ANY ATTEMPT IS MAKE TO RUN THE IMU PERFORMANCE TEST

#   EBANK= AZIMUTH
W('37,2776', 0o11412, '', 'CCS', 'LENGTHOT', line=279)
W('37,2777', 0o03034, '', 'TC', 'SLEEPIE', line=280)
W('37,3000', 0o11440, '', 'CCS', 'TORQNDX', line=281)
W('37,3001', 0o13003, '', 'TCF', '+2', line=282)
W('37,3002', 0o03005, '', 'TC', 'SETUPER1', line=283)
W('37,3003', 0o30032, '', 'CA', 'CDUX', line=284)
W('37,3004', 0o55414, '', 'TS', 'LOSVEC +1', 'FOR TROUBLESHOOTING VD POSNS 2$4', line=285)

# Page 388
W('37,3005', 0o06037, 'SETUPER1', 'TC', 'INTPRET', line=288)
W('37,3006', 0o65345, '', 'DLOAD', 'PDDL', 'ANGLES FROM DRIFT TEST ONLY', kind='interp', line=289)
W('37,3007', 0o02473, '', '', 'ANGZ', kind='operand', line=290)
W('37,3010', 0o02477, '', '', 'ANGY', kind='operand', line=291)
W('37,3011', 0o55525, '', 'PDDL', 'VDEF', kind='interp', line=292)
W('37,3012', 0o02501, '', '', 'ANGX', kind='operand', line=293)
W('37,3013', 0o74276, '', 'VCOMP', 'VXSC', kind='interp', line=294)
W('37,3014', 0o37110, '', '', 'GEORGEJ', kind='operand', line=295)
W('37,3015', 0o74521, '', 'MXV', 'VSR1', kind='interp', line=296)
W('37,3016', 0o02643, '', '', 'XSM', kind='operand', line=297)
W('37,3017', 0o02740, '', 'STORE', 'OGC', kind='interp', line=298)
W('37,3020', 0o77776, '', 'EXIT', kind='interp', line=299)

W('37,3021', 0o32475, '', 'CA', 'OGCPL', line=301)
W('37,3022', 0o04616, '', 'TC', 'BANKCALL', line=302)
W('37,3023', 0o17323, '', 'CADR', 'IMUPULSE', kind='data', line=303)
W('37,3024', 0o02315, '', 'TC', 'IMUSLLLG', line=304)
W('37,3025', 0o11440, 'GEOSTRT4', 'CCS', 'TORQNDX', 'ONLY POSITIVE IF IN VERTICAL DRIFT TEST', line=305)
W('37,3026', 0o02263, '', 'TC', 'VALMIS', line=306)
W('37,3027', 0o06037, '', 'TC', 'INTPRET', line=307)
W('37,3030', 0o77624, '', 'CALL', kind='interp', line=308)
W('37,3031', 0o76401, '', '', 'ERTHRVSE', kind='operand', line=309)
W('37,3032', 0o77776, '', 'EXIT', kind='interp', line=310)
W('37,3033', 0o02117, '', 'TC', 'TORQUE', line=311)

W('37,3034', 0o55412, 'SLEEPIE', 'TS', 'LENGTHOT', 'TEST NOT OVER-DECREMENT LENGTHOT', line=313)
W('37,3035', 0o11440, '', 'CCS', 'TORQNDX', 'ARE WE DOING VERTDRIFT', line=314)
W('37,3036', 0o02447, '', 'TC', 'EARTHR*', line=315)
W('37,3037', 0o05155, '', 'TC', 'ENDOFJOB', line=316)

W('37,3040', 0o35014, 'SOMEERRR', 'CA', 'EBANK5', line=318)
W('37,3041', 0o54003, '', 'TS', 'EBANK', line=319)
W('37,3042', 0o34753, '', 'CA', 'ONE', line=320)
W('37,3043', 0o55576, '', 'TS', 'OVFLOWCK', 'STOP ALLOOP FROM CALLING ITSELF', line=321)
W('37,3044', 0o05567, '', 'TC', 'ALARM', line=322)
W('37,3045', 0o01600, '', 'OCT', '1600', kind='data', line=323)
W('37,3046', 0o02270, '', 'TC', 'ENDTEST1', line=324)
W('37,3047', 0o33054, 'SOMERR2', 'CAF', 'OCT1601', line=325)
W('37,3050', 0o05744, '', 'TC', 'VARALARM', line=326)
W('37,3051', 0o05516, '', 'TC', 'DOWNFLAG', line=327)
W('37,3052', 0o00007, '', 'ADRES', 'IMUSE', kind='data', line=328)
W('37,3053', 0o05155, '', 'TC', 'ENDOFJOB', line=329)

W('37,3054', 0o01601, 'OCT1601', 'OCT', '01601', kind='data', line=331)
W('37,3055', 0o06200, 'DEC585', 'OCT', '06200', '3200 B+14 ORDER IS IMPORTANT', kind='data', line=332)
W('37,3056', 0o00000, 'SCHZEROS', '2DEC', '.00000000', kind='data', line=333)
W('37,3057', 0o00000, kind='data', line=333)
# Page 389
W('37,3060', 0o00000, '', '2DEC', '.00000000', kind='data', line=335)
W('37,3061', 0o00000, kind='data', line=335)

W('37,3062', 0o00000, '', 'OCT', '00000', kind='data', line=337)
W('37,3063', 0o00000, 'ONEDPP', 'OCT', '00000', 'ORDER IS IMPORTANT', kind='data', line=338)
W('37,3064', 0o00001, '', 'OCT', '00001', kind='data', line=339)

W('37,3065', 0o00004, 'INTVAL', 'OCT', '4', kind='data', line=341)
W('37,3066', 0o00002, '', 'OCT', '2', kind='data', line=342)
W('37,3067', 0o00220, '', 'DEC', '144', kind='data', line=343)
W('37,3070', 0o77776, '', 'DEC', '-1', kind='data', line=344)
W('37,3071', 0o35730, 'SOUPLY', '2DEC', '.93505870', 'INITIAL GAINS FOR PIP OUTPUTS', kind='data', line=345)
W('37,3072', 0o00035, kind='data', line=345)

W('37,3073', 0o10317, '', '2DEC', '.26266423', 'INITIAL GAINS/4 FOR ERECTION ANGLES', kind='data', line=347)
W('37,3074', 0o17550, kind='data', line=347)

W('37,3075', 0o00115, '77DECML', 'DEC', '77', kind='data', line=349)
W('37,3076', 0o01443, 'ALXXXZ', 'GENADR', 'ALX1S -1', kind='data', line=350)
W('37,3077', 0o04133, 'PIPASC', '2DEC', '.13055869', kind='data', line=351)
W('37,3100', 0o02265, kind='data', line=351)

W('37,3101', 0o57223, 'VELSC', '2DEC', '-.52223476', '512/980.402', kind='data', line=353)
W('37,3102', 0o66451, kind='data', line=353)

W('37,3103', 0o05427, 'ALSK', '2DEC', '.17329931', 'SSWAY VEL GAIN X 980.402/4096', kind='data', line=355)
W('37,3104', 0o12577, kind='data', line=355)

W('37,3105', 0o77567, '', '2DEC', '-.00835370', 'SSWAY ACCEL GAIN X 980.402/4096', kind='data', line=357)
W('37,3106', 0o44202, kind='data', line=357)

W('37,3107', 0o24276, 'GEORGEJ', '2DEC', '.63661977', kind='data', line=359)
W('37,3110', 0o14066, kind='data', line=359)

W('37,3111', 0o23073, 'GEORGEK', '2DEC', '.59737013', kind='data', line=361)
W('37,3112', 0o11773, kind='data', line=361)
