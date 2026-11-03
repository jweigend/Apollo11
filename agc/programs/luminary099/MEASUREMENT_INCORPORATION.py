"""MEASUREMENT_INCORPORATION.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/MEASUREMENT_INCORPORATION.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1149-1158 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('MEASUREMENT_INCORPORATION', 'MEASUREMENT_INCORPORATION.agc', 'Luminary099', pages='1149-1158')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     MEASUREMENT_INCORPORATION.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
#
# Assembler:    yaYUL
# Contact:      Jim Lawton <jim DOT lawton AT gmail DOT com>
# Website:      www.ibiblio.org/apollo.
# Pages:        1149-1158
# Mod history:  2009-05-28 JL   Updated from page images.
# 2011-01-06 JL   Fixed pseudo-label indentation.
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
# Assemble revision 001 of AGC program LMY99 by NASA 2021112-061
# 16:27 JULY 14, 1969

# Page 1149
# INCORP1 -- PERFORMS THE SIX DIMENSIONAL STATE VECTOR DEVIATION FOR POSITION
# AND VELOCITY OR THE NINE-DIMENSIONAL DEVIATION OF POSITION, VELOCITY, AND
# RADAR OR LANDMARK BIAS. THE OUTPUT OF THE BVECTOR ROUTINE ALONG WITH THE
# ERROR TRANSITION MATRIX (W) ARE USED AS INPU TO THE ROUTINE. THE DEVIATION
# IS OBTAINED BY COMPUTING AN ESTIMATED TRACKING MEASUREMENT FROM THE
# CURRENT STATE VECTOR AND COMPARING IT WITH AN ACTUAL TRACKING MEASUREMENT
# AND APPLYING A STATISTICAL WEIGHTING VECTOR.
#
# INPUT
# DMENFLG = 0 (6-DIMENSIONAL BVECTOR), =1 (9-DIMENSIONAL)
# W = ERROR TRANSITION MATRIX 6X6 OR 9X9
# VARIANCE = VARIANCE (SCALAR)
# DELTAQ = MEASURED DEVIATION (SCALAR)
# BVECTOR = 6 OR 9 DIMENSIONAL BVECTOR
#
# OUTPUT
# DELTAX = STATE VECTOR DEVIATIONS 6 OR 9 DIMENSIONAL
# ZI = VECTOR USED FOR THE INCORPORATION 6 OR 9 DIMENSIONAL
# GAMMA = SCALAR
# OMEGA = OMEGA WEIGHTING VECTOR 6 OR 9 DIMENSIONAL
#
# CALLING SEQUENCE
# L       CALL    INCORP1
#
# NORMAL EXIT
# L+1 OF CALLING SEQUENCE

#   BANK 37
#   SETLOC MEASINC
#   BANK

#   COUNT* $$/INCOR

#   EBANK= W

W('23,2531', 0o77620, 'INCORP1', 'STQ', kind='interp', line=64)
W('23,2532', 0o02772, '', '', 'EGRESS', kind='operand', line=65)
W('23,2533', 0o66370, '', 'AXT,1', 'SSP', kind='interp', line=66)
W('23,2534', 0o00066, '', '', '54D', kind='operand', line=67)
W('23,2535', 0o00051, '', '', 'S1', kind='operand', line=68)
W('23,2536', 0o00022, '', '', '18D', 'IX1 = 54      S1= 18', kind='operand', line=69)
W('23,2537', 0o66374, '', 'AXT,2', 'SSP', kind='interp', line=70)
W('23,2540', 0o00022, '', '', '18D', kind='operand', line=71)
W('23,2541', 0o00052, '', '', 'S2', kind='operand', line=72)
W('23,2542', 0o00006, '', '', '6', 'IX2 = 18      S2=6', kind='operand', line=73)
W('23,2543', 0o63775, 'Z123', 'VLOAD', 'MXV*', kind='interp', line=74)
W('23,2544', 0o03525, '', '', 'BVECTOR', 'BVECTOR (0)', kind='operand', line=75)
W('23,2545', 0o02467, '', '', 'W +54D,1', kind='operand', line=76)
W('23,2546', 0o12665, '', 'STORE', 'ZI +18D,2', kind='interp', line=77)
W('23,2547', 0o77775, '', 'VLOAD', kind='interp', line=78)
W('23,2550', 0o03533, '', '', 'BVECTOR +6', 'BVECTOR (1)', kind='operand', line=79)
# Page 1150
W('23,2551', 0o52717, '', 'MXV*', 'VAD*', kind='interp', line=81)
W('23,2552', 0o02555, '', '', 'W +108D,1', kind='operand', line=82)
W('23,2553', 0o75112, '', '', 'ZI +18D,2', kind='operand', line=83)
W('23,2554', 0o12665, '', 'STORE', 'ZI +18D,2', kind='interp', line=84)
W('23,2555', 0o77775, '', 'VLOAD', kind='interp', line=85)
W('23,2556', 0o03541, '', '', 'BVECTOR +12D', 'BVECTOR (2)', kind='operand', line=86)
W('23,2557', 0o52717, '', 'MXV*', 'VAD*', kind='interp', line=87)
W('23,2560', 0o02643, '', '', 'W +162D,1', kind='operand', line=88)
W('23,2561', 0o75112, '', '', 'ZI +18D,2', 'B(0)*W+B(1)*(W+54)+B(2)*(W+108) FIRST PASS', kind='operand', line=89)
W('23,2562', 0o12665, '', 'STORE', 'ZI +18D,2', 'ZI THEN Z2 THEN Z3', kind='interp', line=90)
W('23,2563', 0o77700, '', 'TIX,1', kind='interp', line=91)
W('23,2564', 0o46565, '', '', 'INCOR1', kind='operand', line=92)
W('23,2565', 0o43104, 'INCOR1', 'TIX,2', 'BON', kind='interp', line=93)
W('23,2566', 0o46543, '', '', 'Z123', 'LOOP FOR Z1,Z2,Z3', kind='operand', line=94)
W('23,2567', 0o02706, '', '', 'DMENFLG', kind='operand', line=95)
W('23,2570', 0o46574, '', '', 'INCOR1A', kind='operand', line=96)
W('23,2571', 0o77775, '', 'VLOAD', kind='interp', line=97)
W('23,2572', 0o06522, '', '', 'ZEROVECS', kind='operand', line=98)
W('23,2573', 0o02657, '', 'STORE', 'ZI +12D', kind='interp', line=99)
W('23,2574', 0o77201, 'INCOR1A', 'SETPD', 'VLOAD', kind='interp', line=100)
W('23,2575', 0o00001, '', '', '0', kind='operand', line=101)
W('23,2576', 0o02643, '', '', 'ZI', kind='operand', line=102)
W('23,2577', 0o47036, '', 'VSQ', 'RTB', kind='interp', line=103)
W('23,2600', 0o21633, '', '', 'TPMODE', kind='operand', line=104)
W('23,2601', 0o47515, '', 'PDVL', 'VSQ', kind='interp', line=105)
W('23,2602', 0o02651, '', '', 'ZI +6', kind='operand', line=106)
W('23,2603', 0o76234, '', 'RTB', 'TAD', kind='interp', line=107)
W('23,2604', 0o21633, '', '', 'TPMODE', kind='operand', line=108)
W('23,2605', 0o47515, '', 'PDVL', 'VSQ', kind='interp', line=109)
W('23,2606', 0o02657, '', '', 'ZI +12D', kind='operand', line=110)
W('23,2607', 0o76234, '', 'RTB', 'TAD', kind='interp', line=111)
W('23,2610', 0o21633, '', '', 'TPMODE', kind='operand', line=112)
W('23,2611', 0o77171, '', 'TAD', 'AXT,2', kind='interp', line=113)
W('23,2612', 0o02707, '', '', 'VARIANCE', kind='operand', line=114)
W('23,2613', 0o00000, '', '', '0', kind='operand', line=115)
W('23,2614', 0o02665, '', 'STORE', 'TRIPA', 'ZI*2 + Z2*2 + Z3*2 + VARIANCE', kind='interp', line=116)
W('23,2615', 0o40151, '', 'TLOAD', 'BOV', kind='interp', line=117)
W('23,2616', 0o02707, '', '', 'VARIANCE', 'CLEAR OVFIND', kind='operand', line=118)
W('23,2617', 0o46620, '', '', '+1', kind='operand', line=119)
W('23,2620', 0o02670, '', 'STORE', 'TEMPVAR', 'TEMP STORAGE FOR VARIANCE', kind='interp', line=120)
W('23,2621', 0o77654, '', 'BZE', kind='interp', line=121)
W('23,2622', 0o46631, '', '', 'INCOR1C', kind='operand', line=122)
W('23,2623', 0o40112, 'INCOR1B', 'SL2', 'BOV', kind='interp', line=123)
W('23,2624', 0o46631, '', '', 'INCOR1C', kind='operand', line=124)
W('23,2625', 0o02670, '', 'STORE', 'TEMPVAR', kind='interp', line=125)
W('23,2626', 0o52114, '', 'INCR,2', 'GOTO', kind='interp', line=126)
W('23,2627', 0o00001, '', 'DEC', '1', kind='data', line=127)
W('23,2630', 0o46623, '', '', 'INCOR1B', kind='operand', line=128)
W('23,2631', 0o61551, 'INCOR1C', 'TLOAD', 'ROUND', kind='interp', line=129)
W('23,2632', 0o02665, '', '', 'TRIPA', kind='operand', line=130)
# Page 1151
W('23,2633', 0o75405, '', 'DMP', 'SQRT', kind='interp', line=132)
W('23,2634', 0o02670, '', '', 'TEMPVAR', kind='operand', line=133)
W('23,2635', 0o76257, '', 'SL*', 'TAD', kind='interp', line=134)
W('23,2636', 0o57576, '', '', '0,2', kind='operand', line=135)
W('23,2637', 0o02665, '', '', 'TRIPA', kind='operand', line=136)
W('23,2640', 0o63101, '', 'NORM', 'INCR,2', kind='interp', line=137)
W('23,2641', 0o00050, '', '', 'X2', kind='operand', line=138)
W('23,2642', 0o77775, '', 'DEC', '-2', kind='data', line=139)
W('23,2643', 0o77134, '', 'SXA,2', 'AXT,2', kind='interp', line=140)
W('23,2644', 0o02103, '', '', 'NORMGAM', 'NORMALIZATION COUNT -2 FOR GAMMA', kind='operand', line=141)
W('23,2645', 0o00242, '', '', '162D', kind='operand', line=142)
W('23,2646', 0o40265, '', 'BDDV', 'SETPD', kind='interp', line=143)
W('23,2647', 0o06512, '', '', 'DP1/4TH', kind='operand', line=144)
W('23,2650', 0o00001, '', '', '0', kind='operand', line=145)
W('23,2651', 0o03500, '', 'STORE', 'GAMMA', kind='interp', line=146)
W('23,2652', 0o60351, '', 'TLOAD', 'NORM', kind='interp', line=147)
W('23,2653', 0o02665, '', '', 'TRIPA', kind='operand', line=148)
W('23,2654', 0o00047, '', '', 'X1', kind='operand', line=149)
W('23,2655', 0o65345, '', 'DLOAD', 'PDDL', 'PD 0-1 = NORM (A)', kind='interp', line=150)
W('23,2656', 0o00155, '', '', 'MPAC', kind='operand', line=151)
W('23,2657', 0o03547, '', '', 'DELTAQ', kind='operand', line=152)
W('23,2660', 0o77701, '', 'NORM', kind='interp', line=153)
W('23,2661', 0o00051, '', '', 'S1', kind='operand', line=154)
W('23,2662', 0o70460, '', 'XSU,1', 'SR1', kind='interp', line=155)
W('23,2663', 0o00050, '', '', 'S1', kind='operand', line=156)
W('23,2664', 0o41471, '', 'DDV', 'PUSH', 'PD 0-1 = DELTAQ/A', kind='interp', line=157)
W('23,2665', 0o77650, '', 'GOTO', kind='interp', line=158)
W('23,2666', 0o45711, '', '', 'NEWZCOMP', kind='operand', line=159)
W('23,2667', 0o77731, '', 'SSP', kind='interp', line=160)
W('23,2670', 0o00052, '', '', 'S2', kind='operand', line=161)
W('23,2671', 0o00066, '', '', '54D', kind='operand', line=162)
W('23,2672', 0o60775, 'INCOR2', 'VLOAD', 'VXM*', 'COMPUT OMEGA1,2,3', kind='interp', line=163)
W('23,2673', 0o02643, '', '', 'ZI', kind='operand', line=164)
W('23,2674', 0o75134, '', '', 'W +162D,2', kind='operand', line=165)
W('23,2675', 0o77206, '', 'PUSH', 'VLOAD', kind='interp', line=166)
W('23,2676', 0o02651, '', '', 'ZI +6', kind='operand', line=167)
W('23,2677', 0o53303, '', 'VXM*', 'VAD', kind='interp', line=168)
W('23,2700', 0o75112, '', '', 'W +180D,2', kind='operand', line=169)
W('23,2701', 0o77206, '', 'PUSH', 'VLOAD', kind='interp', line=170)
W('23,2702', 0o02657, '', '', 'ZI +12D', kind='operand', line=171)
W('23,2703', 0o53303, '', 'VXM*', 'VAD', kind='interp', line=172)
W('23,2704', 0o75070, '', '', 'W +198D,2', kind='operand', line=173)
W('23,2705', 0o61006, '', 'PUSH', 'TIX,2', 'PD 2-7=OMEGA1, 8-13=OMEGA2, 14-19=OMEGA3', kind='interp', line=174)
W('23,2706', 0o46672, '', '', 'INCOR2', kind='operand', line=175)
W('23,2707', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=176)
W('23,2710', 0o74260, '', 'STORE', 'OMEGA +12D', kind='interp', line=177)
W('23,2711', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=178)
W('23,2712', 0o74266, '', 'STORE', 'OMEGA +6', kind='interp', line=179)
W('23,2713', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=180)
W('23,2714', 0o74274, '', 'STORE', 'OMEGA', kind='interp', line=181)
# Page 1152
W('23,2715', 0o77214, '', 'BON', 'VLOAD', kind='interp', line=183)
W('23,2716', 0o02706, '', '', 'DMENFLG', kind='operand', line=184)
W('23,2717', 0o46722, '', '', 'INCOR2AB', kind='operand', line=185)
W('23,2720', 0o06522, '', '', 'ZEROVECS', kind='operand', line=186)
W('23,2721', 0o03517, '', 'STORE', 'OMEGA +12D', kind='interp', line=187)
W('23,2722', 0o66374, 'INCOR2AB', 'AXT,2', 'SSP', kind='interp', line=188)
W('23,2723', 0o00022, '', '', '18D', kind='operand', line=189)
W('23,2724', 0o00052, '', '', 'S2', kind='operand', line=190)
W('23,2725', 0o00006, '', '', '6', kind='operand', line=191)
W('23,2726', 0o77773, 'INCOR3', 'VLOAD*', kind='interp', line=192)
W('23,2727', 0o74252, '', '', 'OMEGA +18D,2', kind='operand', line=193)
W('23,2730', 0o53761, '', 'VXSC', 'VSL*', kind='interp', line=194)
W('23,2731', 0o00001, '', '', '0', 'DELTAQ/A', kind='operand', line=195)
W('23,2732', 0o20201, '', '', '0,1', kind='operand', line=196)
W('23,2733', 0o12707, '', 'STORE', 'DELTAX +18D,2', kind='interp', line=197)
W('23,2734', 0o77304, '', 'TIX,2', 'VLOAD', kind='interp', line=198)
W('23,2735', 0o46726, '', '', 'INCOR3', kind='operand', line=199)
W('23,2736', 0o02673, '', '', 'DELTAX +6', kind='operand', line=200)
W('23,2737', 0o77732, '', 'VSL3', kind='interp', line=201)
W('23,2740', 0o02673, '', 'STORE', 'DELTAX +6', kind='interp', line=202)
W('23,2741', 0o77650, '', 'GOTO', kind='interp', line=203)
W('23,2742', 0o02772, '', '', 'EGRESS', kind='operand', line=204)

# Page 1153
# INCORP2 - INCORPORATES THE COMPUTED STATE VECTOR DEVIATIONS INTO THE
# ESTIMATED STATE VECTOR. THE STATE VECTOR UPDATED MAY BE FOR EITHER THE
# LEM OR THE CSM. DETERMINED BY FLAG VEHUPFLG. (ZERO = LEM) (1 = CSM)
#
# INPUT
# PERMANENT STATE VECTOR FOR EITHER THE LEM OR CSM
# VEHUPFLG = UPDATE VEHICLE 0=LEM  1=CSM
# W = ERROR TRANSITION MATRIX
# DELTAX = COMPUTED STATE VECTOR DEVIATIONS
# DMENFLG = SIZE OF W MATRIX (ZERO=6X6) (1=9X9)
# GAMMA = SCALAR FOR INCORPORATION
# ZI = VECTOR USED IN INCORPORATION
# OMEGA = WEIGHTING VECTOR
#
# OUTPUT
# UPDATED PERMANENT STATE VECTOR
#
# CALLING SEQUENCE
# L       CALL    INCORP2
#
# NORMAL EXIT
# L+1 OF CALLING SEQUENCE
#

#   SETLOC MEASINC1
#   BANK

#   COUNT* $$/INCOR

W('23,2743', 0o45020, 'INCORP2', 'STQ', 'CALL', kind='interp', line=236)
W('23,2744', 0o02772, '', '', 'EGRESS', kind='operand', line=237)
W('23,2745', 0o27414, '', '', 'INTSTALL', kind='operand', line=238)
W('23,2746', 0o74375, '', 'VLOAD', 'VXSC', 'CALC. GAMMA * OMEGA1,2,3', kind='interp', line=239)
W('23,2747', 0o03503, '', '', 'OMEGA', kind='operand', line=240)
W('23,2750', 0o03500, '', '', 'GAMMA', kind='operand', line=241)
W('23,2751', 0o26713, '', 'STOVL', 'OMEGAM1', kind='interp', line=242)
W('23,2752', 0o03511, '', '', 'OMEGA +6', kind='operand', line=243)
W('23,2753', 0o77761, '', 'VXSC', kind='interp', line=244)
W('23,2754', 0o03500, '', '', 'GAMMA', kind='operand', line=245)
W('23,2755', 0o26721, '', 'STOVL', 'OMEGAM2', kind='interp', line=246)
W('23,2756', 0o03517, '', '', 'OMEGA +12D', kind='operand', line=247)
W('23,2757', 0o77761, '', 'VXSC', kind='interp', line=248)
W('23,2760', 0o03500, '', '', 'GAMMA', kind='operand', line=249)
W('23,2761', 0o02727, '', 'STORE', 'OMEGAM3', kind='interp', line=250)
W('23,2762', 0o77776, '', 'EXIT', kind='interp', line=251)
W('23,2763', 0o33244, '', 'CAF', '54DD', 'INITIAL IX 1 SETTING FOR W MATRIX', line=252)
W('23,2764', 0o55320, '', 'TS', 'WIXA', line=253)
W('23,2765', 0o55321, '', 'TS', 'WIXB', line=254)
W('23,2766', 0o34755, '', 'CAF', 'ZERO', line=255)
W('23,2767', 0o55322, '', 'TS', 'ZIXA', 'INITIAL IX 2 SETTING FOR Z COMPONENT', line=256)
W('23,2770', 0o55323, '', 'TS', 'ZIXB', line=257)
W('23,2771', 0o05353, 'FAZA', 'TC', 'PHASCHNG', line=258)
# Page 1154
W('23,2772', 0o04022, '', 'OCT', '04022', kind='data', line=260)
W('23,2773', 0o05504, '', 'TC', 'UPFLAG', line=261)
W('23,2774', 0o00236, '', 'ADRES', 'REINTFLG', kind='data', line=262)
W('23,2775', 0o31321, 'FAZA1', 'CA', 'WIXB', 'START FIRST PHASE OF INCORP2', line=263)
W('23,2776', 0o55320, '', 'TS', 'WIXA', 'TO UPDATE 6 OR 9 DIM. W MATRIX IN TEMP', line=264)
W('23,2777', 0o31323, '', 'CA', 'ZIXB', line=265)
W('23,3000', 0o55322, '', 'TS', 'ZIXA', line=266)
W('23,3001', 0o06037, '', 'TC', 'INTPRET', line=267)
W('23,3002', 0o73150, '', 'LXA,1', 'LXA,2', kind='interp', line=268)
W('23,3003', 0o01320, '', '', 'WIXA', kind='operand', line=269)
W('23,3004', 0o01322, '', '', 'ZIXA', kind='operand', line=270)
W('23,3005', 0o70731, '', 'SSP', 'DLOAD*', kind='interp', line=271)
W('23,3006', 0o00051, '', '', 'S1', kind='operand', line=272)
W('23,3007', 0o00006, '', '', '6', kind='operand', line=273)
W('23,3010', 0o75134, '', '', 'ZI,2', kind='operand', line=274)
W('23,3011', 0o60276, '', 'DCOMP', 'NORM', 'CALC UPPER 3X9 PARTITION OF W MATRIX', kind='interp', line=275)
W('23,3012', 0o00052, '', '', 'S2', kind='operand', line=276)
W('23,3013', 0o65161, '', 'VXSC', 'XCHX,2', kind='interp', line=277)
W('23,3014', 0o02713, '', '', 'OMEGAM1', kind='operand', line=278)
W('23,3015', 0o00051, '', '', 'S2', kind='operand', line=279)
W('23,3016', 0o57144, '', 'LXC,2', 'XAD,2', kind='interp', line=280)
W('23,3017', 0o00047, '', '', 'X2', kind='operand', line=281)
W('23,3020', 0o02103, '', '', 'NORMGAM', kind='operand', line=282)
W('23,3021', 0o65057, '', 'VSL*', 'XCHX,2', kind='interp', line=283)
W('23,3022', 0o57576, '', '', '0,2', kind='operand', line=284)
W('23,3023', 0o00051, '', '', 'S2', kind='operand', line=285)
W('23,3024', 0o77653, '', 'VAD*', kind='interp', line=286)
W('23,3025', 0o02467, '', '', 'W +54D,1', kind='operand', line=287)
W('23,3026', 0o02735, '', 'STORE', 'HOLDW', kind='interp', line=288)
W('23,3027', 0o57543, '', 'DLOAD*', 'DCOMP', 'CALC MIDDLE 3X9 PARTITION OF W MATRIX', kind='interp', line=289)
W('23,3030', 0o75134, '', '', 'ZI,2', kind='operand', line=290)
W('23,3031', 0o74301, '', 'NORM', 'VXSC', kind='interp', line=291)
W('23,3032', 0o00052, '', '', 'S2', kind='operand', line=292)
W('23,3033', 0o02721, '', '', 'OMEGAM2', kind='operand', line=293)
W('23,3034', 0o71124, '', 'XCHX,2', 'LXC,2', kind='interp', line=294)
W('23,3035', 0o00051, '', '', 'S2', kind='operand', line=295)
W('23,3036', 0o00047, '', '', 'X2', kind='operand', line=296)
W('23,3037', 0o53674, '', 'XAD,2', 'VSL*', kind='interp', line=297)
W('23,3040', 0o02103, '', '', 'NORMGAM', kind='operand', line=298)
W('23,3041', 0o57576, '', '', '0,2', kind='operand', line=299)
W('23,3042', 0o52724, '', 'XCHX,2', 'VAD*', kind='interp', line=300)
W('23,3043', 0o00051, '', '', 'S2', kind='operand', line=301)
W('23,3044', 0o02555, '', '', 'W +108D,1', kind='operand', line=302)
W('23,3045', 0o02743, '', 'STORE', 'HOLDW +6', kind='interp', line=303)
W('23,3046', 0o77614, '', 'BOFF', kind='interp', line=304)
W('23,3047', 0o02746, '', '', 'DMENFLG', 'BRANCH IF 6 DIMENSIONAL', kind='operand', line=305)
W('23,3050', 0o47070, '', '', 'FAZB', kind='operand', line=306)
W('23,3051', 0o57543, '', 'DLOAD*', 'DCOMP', 'CALC LOWER 3X9 PARTITION OF W MATRIX', kind='interp', line=307)
W('23,3052', 0o75134, '', '', 'ZI,2', kind='operand', line=308)
W('23,3053', 0o74301, '', 'NORM', 'VXSC', kind='interp', line=309)
# Page 1155
W('23,3054', 0o00052, '', '', 'S2', kind='operand', line=311)
W('23,3055', 0o02727, '', '', 'OMEGAM3', kind='operand', line=312)
W('23,3056', 0o71124, '', 'XCHX,2', 'LXC,2', kind='interp', line=313)
W('23,3057', 0o00051, '', '', 'S2', kind='operand', line=314)
W('23,3060', 0o00047, '', '', 'X2', kind='operand', line=315)
W('23,3061', 0o53674, '', 'XAD,2', 'VSL*', kind='interp', line=316)
W('23,3062', 0o02103, '', '', 'NORMGAM', kind='operand', line=317)
W('23,3063', 0o57576, '', '', '0,2', kind='operand', line=318)
W('23,3064', 0o52724, '', 'XCHX,2', 'VAD*', kind='interp', line=319)
W('23,3065', 0o00051, '', '', 'S2', kind='operand', line=320)
W('23,3066', 0o02643, '', '', 'W +162D,1', kind='operand', line=321)
W('23,3067', 0o02751, '', 'STORE', 'HOLDW +12D', kind='interp', line=322)
W('23,3070', 0o77624, 'FAZB', 'CALL', kind='interp', line=323)
W('23,3071', 0o11244, '', '', 'GRP2PC', kind='operand', line=324)
W('23,3072', 0o77776, '', 'EXIT', kind='interp', line=325)
W('23,3073', 0o31320, 'FAZB1', 'CA', 'WIXA', 'START 2ND PHASE OF INCORP2 TO TRANSFER', line=326)
W('23,3074', 0o63245, '', 'AD', '6DD', '      TEMP REG TO PERM W MATRIX', line=327)
W('23,3075', 0o55321, '', 'TS', 'WIXB', line=328)
W('23,3076', 0o31322, '', 'CA', 'ZIXA', line=329)
W('23,3077', 0o67746, '', 'AD', 'MINUS2', line=330)
W('23,3100', 0o55323, '', 'TS', 'ZIXB', line=331)
W('23,3101', 0o06037, '', 'TC', 'INTPRET', line=332)
W('23,3102', 0o66350, '', 'LXA,1', 'SSP', kind='interp', line=333)
W('23,3103', 0o01320, '', '', 'WIXA', kind='operand', line=334)
W('23,3104', 0o00051, '', '', 'S1', kind='operand', line=335)
W('23,3105', 0o00006, '', '', '6', kind='operand', line=336)
W('23,3106', 0o77775, '', 'VLOAD', kind='interp', line=337)
W('23,3107', 0o02735, '', '', 'HOLDW', kind='operand', line=338)
W('23,3110', 0o06467, '', 'STORE', 'W +54D,1', kind='interp', line=339)
W('23,3111', 0o77775, '', 'VLOAD', kind='interp', line=340)
W('23,3112', 0o02743, '', '', 'HOLDW +6', kind='operand', line=341)
W('23,3113', 0o06555, '', 'STORE', 'W +108D,1', kind='interp', line=342)
W('23,3114', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=343)
W('23,3115', 0o02746, '', '', 'DMENFLG', kind='operand', line=344)
W('23,3116', 0o47126, '', '', 'FAZB5', kind='operand', line=345)
W('23,3117', 0o02751, '', '', 'HOLDW +12D', kind='operand', line=346)
W('23,3120', 0o06643, '', 'STORE', 'W +162D,1', kind='interp', line=347)
W('23,3121', 0o52100, 'FAZB2', 'TIX,1', 'GOTO', kind='interp', line=348)
W('23,3122', 0o47124, '', '', '+2', kind='operand', line=349)
W('23,3123', 0o47134, '', '', 'FAZC', 'DONE WITH W MATRIX.  UPDATE STATE VECTOR', kind='operand', line=350)
W('23,3124', 0o77634, '', 'RTB', kind='interp', line=351)
W('23,3125', 0o46771, '', '', 'FAZA', kind='operand', line=352)
W('23,3126', 0o43335, 'FAZB5', 'SLOAD', 'DAD', kind='interp', line=353)
W('23,3127', 0o01324, '', '', 'ZIXB', kind='operand', line=354)
W('23,3130', 0o07247, '', '', '12DD', kind='operand', line=355)
W('23,3131', 0o52030, '', 'BHIZ', 'GOTO', kind='interp', line=356)
W('23,3132', 0o47134, '', '', 'FAZC', kind='operand', line=357)
W('23,3133', 0o47121, '', '', 'FAZB2', kind='operand', line=358)
W('23,3134', 0o77624, 'FAZC', 'CALL', kind='interp', line=359)
W('23,3135', 0o11244, '', '', 'GRP2PC', kind='operand', line=360)
# Page 1156
W('23,3136', 0o53375, '', 'VLOAD', 'VAD', 'START 3RD PHASE OF INCORP2', kind='interp', line=362)
W('23,3137', 0o01701, '', '', 'X789', '7TH, 8TH, 9TH COMPONENT OF STATE VECTOR', kind='operand', line=363)
W('23,3140', 0o02701, '', '', 'DELTAX +12D', 'INCORPORATION FOR X789', kind='operand', line=364)
W('23,3141', 0o03472, '', 'STORE', 'TX789', kind='interp', line=365)
W('23,3142', 0o47014, '', 'BON', 'RTB', kind='interp', line=366)
W('23,3143', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=367)
W('23,3144', 0o47234, '', '', 'DOCSM', kind='operand', line=368)
W('23,3145', 0o26770, '', '', 'MOVEPLEM', kind='operand', line=369)
W('23,3146', 0o77004, 'FAZAB', 'BOVB', 'AXT,2', kind='interp', line=370)
W('23,3147', 0o57753, '', '', 'TCDANZIG', kind='operand', line=371)
W('23,3150', 0o00000, '', '', '0', kind='operand', line=372)
W('23,3151', 0o77014, '', 'BOFF', 'AXT,2', kind='interp', line=373)
W('23,3152', 0o04344, '', '', 'MOONTHIS', kind='operand', line=374)
W('23,3153', 0o47155, '', '', '+2', kind='operand', line=375)
W('23,3154', 0o00002, '', '', '2', kind='operand', line=376)
W('23,3155', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=377)
W('23,3156', 0o02665, '', '', 'DELTAX', 'B27 IF MOON ORBIT, B29 IF EARTH', kind='operand', line=378)
W('23,3157', 0o57205, '', '', '0 -7,2', kind='operand', line=379)
W('23,3160', 0o40055, '', 'VAD', 'BOV', kind='interp', line=380)
W('23,3161', 0o01521, '', '', 'TDELTAV', kind='operand', line=381)
W('23,3162', 0o47174, '', '', 'FAZAB1', kind='operand', line=382)
W('23,3163', 0o25521, '', 'STOVL', 'TDELTAV', kind='interp', line=383)
W('23,3164', 0o02673, '', '', 'DELTAX +6', 'B5 IF MOON ORBIT, B7 IF EARTH', kind='operand', line=384)
W('23,3165', 0o53257, '', 'VSR*', 'VAD', kind='interp', line=385)
W('23,3166', 0o57202, '', '', '0 -4,2', kind='operand', line=386)
W('23,3167', 0o01527, '', '', 'TNUV', kind='operand', line=387)
W('23,3170', 0o77600, '', 'BOV', kind='interp', line=388)
W('23,3171', 0o47200, '', '', 'FAZAB2', kind='operand', line=389)
W('23,3172', 0o35527, '', 'STCALL', 'TNUV', kind='interp', line=390)
W('23,3173', 0o47207, '', '', 'FAZAB3', kind='operand', line=391)
W('23,3174', 0o53375, 'FAZAB1', 'VLOAD', 'VAD', kind='interp', line=392)
W('23,3175', 0o01535, '', '', 'RCV', kind='operand', line=393)
W('23,3176', 0o02665, '', '', 'DELTAX', kind='operand', line=394)
W('23,3177', 0o01535, '', 'STORE', 'RCV', kind='interp', line=395)
W('23,3200', 0o53375, 'FAZAB2', 'VLOAD', 'VAD', kind='interp', line=396)
W('23,3201', 0o01543, '', '', 'VCV', kind='operand', line=397)
W('23,3202', 0o02673, '', '', 'DELTAX +6', kind='operand', line=398)
W('23,3203', 0o01543, '', 'STORE', 'VCV', kind='interp', line=399)
W('23,3204', 0o45134, '', 'SXA,2', 'CALL', kind='interp', line=400)
W('23,3205', 0o02030, '', '', 'PBODY', kind='operand', line=401)
W('23,3206', 0o23441, '', '', 'RECTIFY', kind='operand', line=402)
W('23,3207', 0o77624, 'FAZAB3', 'CALL', kind='interp', line=403)
W('23,3210', 0o11244, '', '', 'GRP2PC', kind='operand', line=404)
W('23,3211', 0o47014, '', 'BON', 'RTB', kind='interp', line=405)
W('23,3212', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=406)
W('23,3213', 0o47237, '', '', 'DOCSM1', kind='operand', line=407)
W('23,3214', 0o26747, '', '', 'MOVEALEM', kind='operand', line=408)
W('23,3215', 0o77624, '', 'CALL', kind='interp', line=409)
W('23,3216', 0o26070, '', '', 'SVDWN2', 'STORE DOWNLINK STATE VECTOR', kind='operand', line=410)
W('23,3217', 0o77624, 'FAZAB4', 'CALL', kind='interp', line=411)
# Page 1157
W('23,3220', 0o11244, '', '', 'GRP2PC', 'PHASE CHANGE', kind='operand', line=413)
W('23,3221', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=414)
W('23,3222', 0o02746, '', '', 'DMENFLG', kind='operand', line=415)
W('23,3223', 0o47226, '', '', 'FAZAB5', '6 DIMENSIONAL', kind='operand', line=416)
W('23,3224', 0o03472, '', '', 'TX789', '9 DIMENSIONAL', kind='operand', line=417)
W('23,3225', 0o01701, '', 'STORE', 'X789', kind='interp', line=418)
W('23,3226', 0o66150, 'FAZAB5', 'LXA,1', 'SXA,1', kind='interp', line=419)
W('23,3227', 0o02772, '', '', 'EGRESS', kind='operand', line=420)
W('23,3230', 0o00052, '', '', 'QPRET', kind='operand', line=421)
W('23,3231', 0o77776, '', 'EXIT', kind='interp', line=422)
W('23,3232', 0o04635, '', 'TC', 'POSTJUMP', 'EXIT', line=423)
W('23,3233', 0o27425, '', 'CADR', 'INTWAKE', kind='data', line=424)
W('23,3234', 0o52034, 'DOCSM', 'RTB', 'GOTO', kind='interp', line=425)
W('23,3235', 0o26723, '', '', 'MOVEPCSM', kind='operand', line=426)
W('23,3236', 0o47146, '', '', 'FAZAB', kind='operand', line=427)
W('23,3237', 0o45034, 'DOCSM1', 'RTB', 'CALL', kind='interp', line=428)
W('23,3240', 0o26674, '', '', 'MOVEACSM', kind='operand', line=429)
W('23,3241', 0o26114, '', '', 'SVDWN1', 'STORE DOWNLINK STATE VECTOR', kind='operand', line=430)
W('23,3242', 0o77650, '', 'GOTO', kind='interp', line=431)
W('23,3243', 0o47217, '', '', 'FAZAB4', kind='operand', line=432)
S('ZEROD', 'equals', 0o56521, line=433)
W('23,3244', 0o00066, '54DD', 'DEC', '54', kind='data', line=434)
W('23,3245', 0o77771, '6DD', 'DEC', '-6', kind='data', line=435)
W('23,3246', 0o00014, '12DD', 'DEC', '12', kind='data', line=436)

#   SETLOC RENDEZ
#   BANK
#   COUNT* $$/INCOR

W('22,3711', 0o51575, 'NEWZCOMP', 'VLOAD', 'ABVAL', kind='interp', line=442)
W('22,3712', 0o02643, '', '', 'ZI', kind='operand', line=443)
W('22,3713', 0o24045, '', 'STOVL', 'NORMZI', kind='interp', line=444)
W('22,3714', 0o02651, '', '', 'ZI +6', kind='operand', line=445)
W('22,3715', 0o41446, '', 'ABVAL', 'PUSH', kind='interp', line=446)
W('22,3716', 0o50025, '', 'DSU', 'BMN', kind='interp', line=447)
W('22,3717', 0o00045, '', '', 'NORMZI', kind='operand', line=448)
W('22,3720', 0o45723, '', '', '+3', kind='operand', line=449)
W('22,3721', 0o45545, '', 'DLOAD', 'STADR', kind='interp', line=450)
W('22,3722', 0o77732, '', 'STORE', 'NORMZI', kind='interp', line=451)
W('22,3723', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=452)
W('22,3724', 0o02657, '', '', 'ZI +12D', kind='operand', line=453)
W('22,3725', 0o45206, '', 'PUSH', 'DSU', kind='interp', line=454)
W('22,3726', 0o00045, '', '', 'NORMZI', kind='operand', line=455)
W('22,3727', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=456)
W('22,3730', 0o45733, '', '', '+3', kind='operand', line=457)
W('22,3731', 0o77626, '', 'STADR', kind='interp', line=458)
W('22,3732', 0o77732, '', 'STORE', 'NORMZI', 'LARGEST ABVAL', kind='interp', line=459)
W('22,3733', 0o66145, '', 'DLOAD', 'SXA,1', kind='interp', line=460)
W('22,3734', 0o00045, '', '', 'NORMZI', kind='operand', line=461)
W('22,3735', 0o00044, '', '', 'NORMZI', 'SAVE X1', kind='operand', line=462)
W('22,3736', 0o62101, '', 'NORM', 'INCR,1', kind='interp', line=463)
# Page 1158
W('22,3737', 0o00047, '', '', 'X1', kind='operand', line=465)
W('22,3740', 0o00002, '', 'DEC', '2', kind='data', line=466)
W('22,3741', 0o53775, '', 'VLOAD', 'VSL*', kind='interp', line=467)
W('22,3742', 0o02643, '', '', 'ZI', kind='operand', line=468)
W('22,3743', 0o20201, '', '', '0,1', kind='operand', line=469)
W('22,3744', 0o26643, '', 'STOVL', 'ZI', kind='interp', line=470)
W('22,3745', 0o02651, '', '', 'ZI +6', kind='operand', line=471)
W('22,3746', 0o77657, '', 'VSL*', kind='interp', line=472)
W('22,3747', 0o20201, '', '', '0,1', kind='operand', line=473)
W('22,3750', 0o26651, '', 'STOVL', 'ZI +6', kind='interp', line=474)
W('22,3751', 0o02657, '', '', 'ZI +12D', kind='operand', line=475)
W('22,3752', 0o66057, '', 'VSL*', 'SXA,1', kind='interp', line=476)
W('22,3753', 0o20201, '', '', '0,1', kind='operand', line=477)
W('22,3754', 0o00045, '', '', 'NORMZI +1', 'SAVE SHIFT', kind='operand', line=478)
W('22,3755', 0o02657, '', 'STORE', 'ZI +12D', kind='interp', line=479)
W('22,3756', 0o54150, '', 'LXA,1', 'XSU,1', kind='interp', line=480)
W('22,3757', 0o02103, '', '', 'NORMGAM', kind='operand', line=481)
W('22,3760', 0o00045, '', '', 'NORMZI +1', kind='operand', line=482)
W('22,3761', 0o77660, '', 'XSU,1', kind='interp', line=483)
W('22,3762', 0o00045, '', '', 'NORMZI +1', kind='operand', line=484)
W('22,3763', 0o70130, '', 'SXA,1', 'LXC,1', kind='interp', line=485)
W('22,3764', 0o02103, '', '', 'NORMGAM', kind='operand', line=486)
W('22,3765', 0o00045, '', '', 'NORMZI +1', kind='operand', line=487)
W('22,3766', 0o40270, '', 'XAD,1', 'SETPD', kind='interp', line=488)
W('22,3767', 0o00044, '', '', 'NORMZI', kind='operand', line=489)
W('22,3770', 0o00003, '', '', '2D', kind='operand', line=490)
W('22,3771', 0o77650, '', 'GOTO', kind='interp', line=491)
W('22,3772', 0o46667, '', '', 'INCOR2 -3', kind='operand', line=492)
S('NORMZI', 'equals', 0o44, line=493)
