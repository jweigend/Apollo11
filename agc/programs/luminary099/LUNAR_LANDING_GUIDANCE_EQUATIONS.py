"""LUNAR_LANDING_GUIDANCE_EQUATIONS.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 798-828 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('LUNAR_LANDING_GUIDANCE_EQUATIONS', 'LUNAR_LANDING_GUIDANCE_EQUATIONS.agc', 'Luminary099', pages='798-828')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     LUNAR_LANDING_GUIDANCE_EQUATIONS.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      HARTMUTH GUTSCHE <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        798-828
# Mod history:  2009-05-23 HG   Transcribed from page images.
# 2009-06-05 RSB  Fixed a goofy thing that was apparently
# legal in GAP but not in yaYUL.  Eliminated
# a couple of lines of code that shouldn't
# have survived from Luminary 131 to here.
# 2009-06-07 RSB  Fixed a typo.
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

# Page 798
#   EBANK= E2DPS
#   COUNT* $$/F2DPS

# ********************************************************
# LUNAR LANDING FLIGHT SEQUENCE TABLES
# ********************************************************

# FLIGHT SEQUENCE TABLES ARE ARRANGED BY FUNCTION.  THEY ARE REFERENCED USING AS AN INDEX THE REGISTER WCHPHASE:
# WCHPHASE = -1 ---> IGNALG
# WCHPHASE =  0 ---> BRAKQUAD
# WCHPHASE =  1 ---> APPRQUAD
# WCHPHASE =  2 ---> VERTICAL

# *********************************************************

# ROUTINES FOR STARTING NEW GUIDANCE PHASES:

W('31,2420', 0o12641, '', 'TCF', 'TTFINCR', 'IGNALG', line=50)
W('31,2421', 0o12641, 'NEWPHASE', 'TCF', 'TTFINCR', 'BRAKQUAD', line=51)
W('31,2422', 0o12630, '', 'TCF', 'STARTP64', 'APPRQUAD', line=52)
W('31,2423', 0o12621, '', 'TCF', 'P65START', 'VERTICAL', line=53)

# PRE-GUIDANCE COMPUTATIONS:

W('31,2424', 0o13003, '', 'TCF', 'CALCRGVG', 'IGNALG', line=57)
W('31,2425', 0o13013, 'PREGUIDE', 'TCF', 'RGVGCALC', 'BRAKQUAD', line=58)
W('31,2426', 0o12704, '', 'TCF', 'REDESIG', 'APPRQUAD', line=59)
W('31,2427', 0o13013, '', 'TCF', 'RGVGCALC', 'VERTICAL', line=60)

# GUIDANCE EQUATIONS:

W('31,2430', 0o13061, '', 'TCF', 'TTF/8CL', 'IGNALG', line=64)
W('31,2431', 0o13061, 'WHATGUID', 'TCF', 'TTF/8CL', 'BRAKQUAD', line=65)
W('31,2432', 0o13061, '', 'TCF', 'TTF/8CL', 'APPRQUAD', line=66)
W('31,2433', 0o13531, '', 'TCF', 'VERTGUID', 'VERTICAL', line=67)

# POST GUIDANCE EQUATION COMPUTATIONS:

W('31,2434', 0o13245, '', 'TCF', 'CGCALC', 'IGNALG', line=71)
W('31,2435', 0o13245, 'AFTRGUID', 'TCF', 'CGCALC', 'BRAKQUAD', line=72)
W('31,2436', 0o13245, '', 'TCF', 'CGCALC', 'APPRQUAD', line=73)
W('31,2437', 0o13432, '', 'TCF', 'STEER?', 'VERTICAL', line=74)

# Page 799
# WINDOW VECTOR COMPUTATIONS:

W('31,2440', 0o13331, '', 'TCF', 'EXGSUB', 'IGNALG', line=79)
W('31,2441', 0o13352, 'WHATEXIT', 'TCF', 'EXBRAK', 'BRAKQUAD', line=80)
W('31,2442', 0o13360, '', 'TCF', 'EXNORM', 'APPRQUAD', line=81)

# DISPLAY ROUTINES:

W('31,2443', 0o13473, 'WHATDISP', 'TCF', 'P63DISPS', 'BRAKQUAD', line=85)
W('31,2444', 0o13477, '', 'TCF', 'P64DISPS', 'APPRQUAD', line=86)
W('31,2445', 0o13527, '', 'TCF', 'VERTDISP', 'VERTICAL', line=87)

# ALARM ROUTINE FOR TTF COMPUTATION:

W('31,2446', 0o13733, '', 'TCF', '1406P00', 'IGNALG', line=91)
W('31,2447', 0o13735, 'WHATALM', 'TCF', '1406ALM', 'BRAKQUAD', line=92)
W('31,2450', 0o13735, '', 'TCF', '1406ALM', 'APPRQUAD', line=93)

# INDICES FOR REFERENCING TARGET PARAMETERS

W('31,2451', 0o00000, '', 'OCT', '0', 'IGNALG', kind='data', line=97)
W('31,2452', 0o00000, 'TARGTDEX', 'OCT', '0', 'BRAKQUAD', kind='data', line=98)
W('31,2453', 0o00034, '', 'OCT', '34', 'APPRQUAD', kind='data', line=99)

# ************************************************************************
# ENTRY POINTS:  ?GUIDSUB FOR THE IGNITION ALGORITHM, LUNLAND FOR SERVOUT
# ************************************************************************

# IGNITION ALGORITHM ENTRY:  DELIVERS N PASSES OF QUADRATIC GUIDANCE

W('31,2454', 0o77776, '?GUIDSUB', 'EXIT', kind='interp', line=107)
W('31,2455', 0o34752, '', 'CAF', 'TWO', 'N = 3', line=108)
W('31,2456', 0o55647, '', 'TS', 'NGUIDSUB', line=109)
W('31,2457', 0o12603, '', 'TCF', 'GUILDRET +2', line=110)

W('31,2460', 0o55647, 'GUIDSUB', 'TS', 'NGUIDSUB', 'ON SUCCEEDING PASSES SKIP TTFINCR', line=112)
W('31,2461', 0o13003, '', 'TCF', 'CALCRGVG', line=113)

# NORMAL ENTRY:  CONTROL COMES HERE FROM SERVOUT

W('31,2462', 0o05353, 'LUNLAND', 'TC', 'PHASCHNG', line=117)
W('31,2463', 0o00035, '', 'OCT', '00035', 'GROUP 5:  RETAIN ONLY PIPA TASK', kind='data', line=118)
W('31,2464', 0o05353, '', 'TC', 'PHASCHNG', line=119)
W('31,2465', 0o05023, '', 'OCT', '05023', 'GROUP 3:  PROTECT GUIDANCE WITH PRIO 21', kind='data', line=120)
W('31,2466', 0o21000, '', 'OCT', '21000', "      JUST HIGHER THAN SERVICER'S PRIORITY", kind='data', line=121)

# Page 800
# *******************************************************************
# GUILDENSTERN:  AUTO-MODES MONITOR (R13)
# *******************************************************************

#   COUNT* $$/R13

# HERE IS THE PHILOSOPHY OF GUILDENSTERN:       ON EVERY APPEARANCE OR DISAPPEARANCE OF THE MANUAL THROTTLE
# DISCRETE TO SELECT P67 OR P66 RESPECTIVELY:   ON EVERY APPEARANCE OF THE ATTITUDE-HOLD DISCRETE TO SELECT P66
# UNLESS THE CURRENT PROGRAM IS P67 IN WHICH CASE THERE IS NO CHANGE

W('31,2467', 0o00006, 'GUILDEN', 'EXTEND', '', 'IS UN-AUTO-THROTTLE DISCRETE PRESENT?', line=134)
# STERN                                 # RSB 2009: Not originally a comment.
W('31,2470', 0o00030, '', 'READ', 'CHAN30', line=136)
W('31,2471', 0o74747, '', 'MASK', 'BIT5', line=137)
W('31,2472', 0o10000, '', 'CCS', 'A', line=138)
W('31,2473', 0o12551, '', 'TCF', 'STARTP67', 'YES', line=139)
W('31,2474', 0o05321, 'P67NOW?', 'TC', 'CHECKMM', 'NO:  ARE WE IN P67 NOW?', line=140)
W('31,2475', 0o00103, '', 'DEC', '67', kind='data', line=141)
W('31,2476', 0o12557, '', 'TCF', 'STABL?', 'NO', line=142)
W('31,2477', 0o03740, 'STARTP66', 'TC', 'FASTCHNG', 'YES', line=143)
W('31,2500', 0o05311, '', 'TC', 'NEWMODEX', line=144)
W('31,2501', 0o00102, 'DEC66', 'DEC', '66', kind='data', line=145)
W('31,2502', 0o00006, '', 'EXTEND', line=146)
W('31,2503', 0o31474, '', 'DCA', 'HDOTDISP', 'SET DESIRED ALTITUDE RATE = CURRENT', line=147)
W('31,2504', 0o53645, '', 'DXCH', 'VDGVERT', '      ALTITUDE RATE.', line=148)
W('31,2505', 0o06037, 'STRTP66A', 'TC', 'INTPRET', line=149)
W('31,2506', 0o41535, '', 'SLOAD', 'PUSH', kind='interp', line=150)
W('31,2507', 0o01457, '', '', 'PBIASZ', kind='operand', line=151)
W('31,2510', 0o41535, '', 'SLOAD', 'PUSH', kind='interp', line=152)
W('31,2511', 0o01455, '', '', 'PBIASY', kind='operand', line=153)
W('31,2512', 0o55535, '', 'SLOAD', 'VDEF', kind='interp', line=154)
W('31,2513', 0o01453, '', '', 'PBIASX', kind='operand', line=155)
W('31,2514', 0o43161, '', 'VXSC', 'SET', kind='interp', line=156)
W('31,2515', 0o25537, '', '', 'BIASFACT', kind='operand', line=157)
W('31,2516', 0o00463, '', '', 'RODFLAG', kind='operand', line=158)
W('31,2517', 0o26631, '', 'STOVL', 'VBIAS', kind='interp', line=159)
W('31,2520', 0o01255, '', '', 'TEMX', kind='operand', line=160)
W('31,2521', 0o77676, '', 'VCOMP', kind='interp', line=161)
W('31,2522', 0o27764, '', 'STOVL', 'OLDPIPAX', kind='interp', line=162)
W('31,2523', 0o06522, '', '', 'ZEROVECS', kind='operand', line=163)
W('31,2524', 0o17767, '', 'STODL', 'DELVROD', kind='interp', line=164)
W('31,2525', 0o02540, '', '', 'RODSCALE', kind='operand', line=165)
W('31,2526', 0o17757, '', 'STODL', 'RODSCAL1', kind='interp', line=166)
W('31,2527', 0o01235, '', '', 'PIPTIME', kind='operand', line=167)
W('31,2530', 0o03760, '', 'STORE', 'LASTTPIP', kind='interp', line=168)
W('31,2531', 0o77776, '', 'EXIT', kind='interp', line=169)
W('31,2532', 0o34755, '', 'CAF', 'ZERO', line=170)
W('31,2533', 0o55620, '', 'TS', 'FCOLD', line=171)
W('31,2534', 0o55610, '', 'TS', 'FWEIGHT', line=172)
W('31,2535', 0o55611, '', 'TS', 'FWEIGHT +1', line=173)
W('31,2536', 0o55647, 'VRTSTART', 'TS', 'WCHVERT', line=174)
# Page 801
W('31,2537', 0o34752, '', 'CAF', 'TWO', 'WCHPHASE = 2 ---> VERTICAL: P65,P66,P67', line=176)
W('31,2540', 0o55621, '', 'TS', 'WCHPHOLD', line=177)
W('31,2541', 0o55351, '', 'TS', 'WCHPHASE', line=178)
W('31,2542', 0o04616, '', 'TC', 'BANKCALL', 'TEMPORARY, I HOPE HOPE HOPE', line=179)
W('31,2543', 0o40165, '', 'CADR', 'STOPRATE', 'TEMPORARY, I HOPE HOPE HOPE', kind='data', line=180)
W('31,2544', 0o05516, '', 'TC', 'DOWNFLAG', 'PERMIT X-AXIS OVERRIDE', line=181)
W('31,2545', 0o00311, '', 'ADRES', 'XOVINFLG', kind='data', line=182)
W('31,2546', 0o05516, '', 'TC', 'DOWNFLAG', line=183)
W('31,2547', 0o00143, '', 'ADRES', 'REDFLAG', kind='data', line=184)
W('31,2550', 0o13531, '', 'TCF', 'VERTGUID', line=185)

W('31,2551', 0o05311, 'STARTP67', 'TC', 'NEWMODEX', 'NO HARM IN "STARTING" P67 OVER AND OVER', line=187)
W('31,2552', 0o00103, '', 'DEC', '67', 'SO NO NEED FOR A FASTCHNG AND NO NEED', kind='data', line=188)
W('31,2553', 0o34755, '', 'CAF', 'ZERO', 'TO SEE IF ALREADY IN P67.', line=189)
W('31,2554', 0o55746, '', 'TS', 'RODCOUNT', line=190)
W('31,2555', 0o34363, '', 'CAF', 'TEN', line=191)
W('31,2556', 0o12536, '', 'TCF', 'VRTSTART', line=192)

W('31,2557', 0o34737, 'STABL?', 'CAF', 'BIT13', 'IS UN-ATTITUDE-HOLD DISCRETE PRESENT?', line=194)
W('31,2560', 0o00006, '', 'EXTEND', line=195)
W('31,2561', 0o02031, '', 'RAND', 'CHAN31', line=196)
W('31,2562', 0o10000, '', 'CCS', 'A', line=197)
W('31,2563', 0o12601, '', 'TCF', 'GUILDRET', "YES ALL'S WELL", line=198)

W('31,2564', 0o41011, 'P66NOW?', 'CS', 'MODREG', line=200)
W('31,2565', 0o62501, '', 'AD', 'DEC66', line=201)
W('31,2566', 0o00006, '', 'EXTEND', line=202)
W('31,2567', 0o12574, '', 'BZF', 'RESTART?', line=203)

W('31,2570', 0o31746, '', 'CA', 'RODCOUNT', 'NO. HAS THE ROD SWITCH BEEN "CLICKED"?', line=205)
W('31,2571', 0o00006, '', 'EXTEND', line=206)
W('31,2572', 0o12601, '', 'BZF', 'GUILDRET', 'NO. CONTINUE WITH AUTOMATIC LANDING', line=207)
W('31,2573', 0o12477, '', 'TCF', 'STARTP66', 'YES. SWITCH INTO THE ROD MODE.', line=208)

W('31,2574', 0o30075, 'RESTART?', 'CA', 'FLAGWRD1', 'HAS THERE BEEN A RESTART?', line=210)
W('31,2575', 0o74740, '', 'MASK', 'RODFLBIT', line=211)
W('31,2576', 0o00006, '', 'EXTEND', line=212)
W('31,2577', 0o12505, '', 'BZF', 'STRTP66A', 'YES.  REINITIALIZE BUT LEAVE VDGVERT AS', line=213)
# IS.

W('31,2600', 0o13531, '', 'TCF', 'VERTGUID', 'NO: CONTINUE WITH R.O.D.', line=216)

# *******************************************************************************
# INITIALIZATION FOR THIS PASS
# *******************************************************************************

#   COUNT* $$/F2DPS

W('31,2601', 0o34755, 'GUILDRET', 'CAF', 'ZERO', line=224)
W('31,2602', 0o55746, '', 'TS', 'RODCOUNT', line=225)

# Page 802
W('31,2603', 0o00006, '', 'EXTEND', line=228)
W('31,2604', 0o31625, '', 'DCA', 'TPIP', line=229)
W('31,2605', 0o53574, '', 'DXCH', 'TPIPOLD', line=230)

W('31,2606', 0o03740, '', 'TC', 'FASTCHNG', line=232)

W('31,2607', 0o00006, '', 'EXTEND', line=234)
W('31,2610', 0o31561, '', 'DCA', 'PIPTIME1', line=235)
W('31,2611', 0o53625, '', 'DXCH', 'TPIP', line=236)

W('31,2612', 0o00006, '', 'EXTEND', line=238)
W('31,2613', 0o31643, '', 'DCA', 'TTF/8', line=239)
W('31,2614', 0o53553, '', 'DXCH', 'TTF/8TMP', line=240)

W('31,2615', 0o11623, '', 'CCS', 'FLPASS0', line=242)
W('31,2616', 0o12641, '', 'TCF', 'TTFINCR', line=243)

W('31,2617', 0o51351, 'BRSPOT1', 'INDEX', 'WCHPHASE', line=245)
W('31,2620', 0o12421, '', 'TCF', 'NEWPHASE', line=246)

# ******************************************************************
# ROUTINES TO START NEW PHASES
# ******************************************************************

W('31,2621', 0o05311, 'P65START', 'TC', 'NEWMODEX', line=252)
W('31,2622', 0o00101, '', 'DEC', '65', kind='data', line=253)
W('31,2623', 0o44752, '', 'CS', 'TWO', line=254)
W('31,2624', 0o55647, '', 'TS', 'WCHVERT', line=255)
W('31,2625', 0o05516, '', 'TC', 'DOWNFLAG', 'PERMIT X-AXIS OVERRIDE', line=256)
W('31,2626', 0o00311, '', 'ADRES', 'XOVINFLG', kind='data', line=257)
W('31,2627', 0o12641, '', 'TCF', 'TTFINCR', line=258)

W('31,2630', 0o05311, 'STARTP64', 'TC', 'NEWMODEX', line=260)
W('31,2631', 0o00100, '', 'DEC', '64', kind='data', line=261)
W('31,2632', 0o31425, '', 'CA', 'DELTTFAP', 'AUGMENT TTF/8', line=262)
W('31,2633', 0o27552, '', 'ADS', 'TTF/8TMP', line=263)
W('31,2634', 0o34740, '', 'CA', 'BIT12', 'ENABLE RUPT10', line=264)
W('31,2635', 0o00006, '', 'EXTEND', line=265)
W('31,2636', 0o05013, '', 'WOR', 'CHAN13', line=266)
W('31,2637', 0o05516, '', 'TC', 'DOWNFLAG', 'INITIALIZE REDESIGNATION FLAG', line=267)
W('31,2640', 0o00143, '', 'ADRES', 'REDFLAG', kind='data', line=268)

# (CONTINUE TO TTFINCR)

# *********************************************************************************
# INCREMENT TTF/8, UPDATE LAND FOR LUNAR ROTATION, DO OTHER USEFUL THINGS
# *********************************************************************************
#
# TTFINCR COMPUTATIONS ARE AS FOLLOWS --
# Page 803
# TTF/8 UPDATED FOR TIME SINCE LAST PASS:
# TTF/8 = TTF/8 + (TPIP - TPIPOLD)/8
# LANDING SITE VECTOR UPDATED FOR LUNAR ROTATION:
# ____               ____   ____                   __
# LAND = /LAND/ UNIT(LAND - LAND(TPIP - TPIPOLD) * WM)
# SLANT RANGE TO LANDING SITE, FOR DISPLAY:
# ____   _
# RANGEDSP = ABVAL(LAND - R)

W('31,2641', 0o06037, 'TTFINCR', 'TC', 'INTPRET', line=288)
W('31,2642', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=289)
W('31,2643', 0o03625, '', '', 'TPIP', kind='operand', line=290)
W('31,2644', 0o03574, '', '', 'TPIPOLD', kind='operand', line=291)
W('31,2645', 0o41461, '', 'SLR', 'PUSH', 'SHIFT SCALES DELTA TIME TO 2(17) CSECS', kind='interp', line=292)
W('31,2646', 0o21214, '', '', '11D', kind='operand', line=293)
W('31,2647', 0o47361, '', 'VXSC', 'VXV', kind='interp', line=294)
W('31,2650', 0o03635, '', '', 'LAND', kind='operand', line=295)
W('31,2651', 0o02325, '', '', 'WM', kind='operand', line=296)
W('31,2652', 0o47045, '', 'BVSU', 'RTB', kind='interp', line=297)
W('31,2653', 0o03635, '', '', 'LAND', kind='operand', line=298)
W('31,2654', 0o21726, '', '', 'NORMUNIT', kind='operand', line=299)
W('31,2655', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=300)
W('31,2656', 0o02333, '', '', '/LAND/', kind='operand', line=301)
W('31,2657', 0o17545, '', 'STODL', 'LANDTEMP', kind='interp', line=302)
W('31,2660', 0o77776, '', 'EXIT', kind='interp', line=303)

W('31,2661', 0o52155, '', 'DXCH', 'MPAC', line=305)
W('31,2662', 0o21553, '', 'DAS', 'TTF/8TMP', 'NOW HAVE INCREMENTED TTF/8 IN TTF/8TMP', line=306)

W('31,2663', 0o03740, '', 'TC', 'FASTCHNG', line=308)

W('31,2664', 0o00006, '', 'EXTEND', line=310)
W('31,2665', 0o31553, '', 'DCA', 'TTF/8TMP', line=311)
W('31,2666', 0o53643, '', 'DXCH', 'TTF/8', line=312)

W('31,2667', 0o00006, '', 'EXTEND', line=314)
W('31,2670', 0o31545, '', 'DCA', 'LANDTEMP', line=315)
W('31,2671', 0o53635, '', 'DXCH', 'LAND', line=316)
W('31,2672', 0o00006, '', 'EXTEND', line=317)
W('31,2673', 0o31547, '', 'DCA', 'LANDTEMP +2', line=318)
W('31,2674', 0o53637, '', 'DXCH', 'LAND +2', line=319)
W('31,2675', 0o00006, '', 'EXTEND', line=320)
W('31,2676', 0o31551, '', 'DCA', 'LANDTEMP +4', line=321)
W('31,2677', 0o53641, '', 'DXCH', 'LAND +4', line=322)

# Page 804
W('31,2700', 0o03704, '', 'TC', 'TDISPSET', line=325)
W('31,2701', 0o03740, '', 'TC', 'FASTCHNG', 'SINCE REDESIG MAY CHANGE LANDTEMP', line=326)

W('31,2702', 0o51351, 'BRSPOT2', 'INDEX', 'WCHPHASE', line=328)
W('31,2703', 0o12425, '', 'TCF', 'PREGUIDE', line=329)

# *********************************************************************
# LANDING SITE PERTURBATION EQUATIONS
# *********************************************************************

W('31,2704', 0o30102, 'REDESIG', 'CA', 'FLAGWRD6', 'IS REDFLAG SET?', line=335)
W('31,2705', 0o74746, '', 'MASK', 'REDFLBIT', line=336)
W('31,2706', 0o00006, '', 'EXTEND', line=337)
W('31,2707', 0o13013, '', 'BZF', 'RGVGCALC', 'NO:  SKIP REDESIGNATION LOGIC', line=338)

W('31,2710', 0o31666, '', 'CA', 'TREDES', 'YES:  HAS TREDES REACHED ZERO?', line=340)
W('31,2711', 0o00006, '', 'EXTEND', line=341)
W('31,2712', 0o13013, '', 'BZF', 'RGVGCALC', 'YES:  SKIP REDESIGNATION LOGIC', line=342)

W('31,2713', 0o00004, '', 'INHINT', line=344)
W('31,2714', 0o31267, '', 'CA', 'ELINCR1', line=345)
W('31,2715', 0o55554, '', 'TS', 'ELINCR', line=346)
W('31,2716', 0o31266, '', 'CA', 'AZINCR1', line=347)
W('31,2717', 0o55556, '', 'TS', 'AZINCR', line=348)
W('31,2720', 0o03740, '', 'TC', 'FASTCHNG', line=349)

W('31,2721', 0o34755, '', 'CA', 'ZERO', line=351)
W('31,2722', 0o55267, '', 'TS', 'ELINCR1', line=352)
W('31,2723', 0o55266, '', 'TS', 'AZINCR1', line=353)
W('31,2724', 0o55555, '', 'TS', 'ELINCR +1', line=354)
W('31,2725', 0o55557, '', 'TS', 'AZINCR +1', line=355)

W('31,2726', 0o30120, '', 'CA', 'FIXLOC', 'SET PD TO 0', line=357)
W('31,2727', 0o54166, '', 'TS', 'PUSHLOC', line=358)

W('31,2730', 0o06037, '', 'TC', 'INTPRET', line=360)
W('31,2731', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=361)
W('31,2732', 0o03635, '', '', 'LAND', kind='operand', line=362)
W('31,2733', 0o03521, '', '', 'R', '                ____   _', kind='operand', line=363)
W('31,2734', 0o41434, '', 'RTB', 'PUSH', 'PUSH DOWN UNIT (LAND - R)', kind='interp', line=364)
W('31,2735', 0o21726, '', '', 'NORMUNIT', kind='operand', line=365)
W('31,2736', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=366)
W('31,2737', 0o02154, '', '', 'YNBPIP', '                   ___        ____   _', kind='operand', line=367)
W('31,2740', 0o65361, '', 'VXSC', 'PDDL', 'PUSH DOWN - ELINCR(YNB * UNIT(LAND - R))', kind='interp', line=368)
W('31,2741', 0o03555, '', '', 'ELINCR', kind='operand', line=369)
W('31,2742', 0o03557, '', '', 'AZINCR', kind='operand', line=370)
W('31,2743', 0o52361, '', 'VXSC', 'VSU', kind='interp', line=371)
W('31,2744', 0o02154, '', '', 'YNBPIP', kind='operand', line=372)
W('31,2745', 0o41455, '', 'VAD', 'PUSH', 'RESULTING VECTOR IS 1/2 REAL SIZE', kind='interp', line=373)

# Page 805

W('31,2746', 0o45345, '', 'DLOAD', 'DSU', 'MAKE SURE REDESIGNATION IS NOT', kind='interp', line=377)
W('31,2747', 0o00001, '', '', '0', '      TOO CLOSE TO THE HORIZON.', kind='operand', line=378)
W('31,2750', 0o05660, '', '', 'DEPRCRIT', kind='operand', line=379)
W('31,2751', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=380)
W('31,2752', 0o62755, '', '', 'REDES1', kind='operand', line=381)
W('31,2753', 0o05660, '', '', 'DEPRCRIT', kind='operand', line=382)
W('31,2754', 0o00001, '', 'STORE', '0', kind='interp', line=383)
W('31,2755', 0o45345, 'REDES1', 'DLOAD', 'DSU', kind='interp', line=384)
W('31,2756', 0o03635, '', '', 'LAND', kind='operand', line=385)
W('31,2757', 0o03521, '', '', 'R', kind='operand', line=386)
W('31,2760', 0o74271, '', 'DDV', 'VXSC', kind='interp', line=387)
W('31,2761', 0o00001, '', '', '0', kind='operand', line=388)
W('31,2762', 0o53455, '', 'VAD', 'UNIT', kind='interp', line=389)
W('31,2763', 0o03521, '', '', 'R', kind='operand', line=390)
W('31,2764', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=391)
W('31,2765', 0o02333, '', '', '/LAND/', kind='operand', line=392)
W('31,2766', 0o03545, '', 'STORE', 'LANDTEMP', kind='interp', line=393)
W('31,2767', 0o77776, '', 'EXIT', '', 'LOOKANGL WILL BE COMPUTED AT RGVGCALC', kind='interp', line=394)

W('31,2770', 0o03740, '', 'TC', 'FASTCHNG', line=396)

W('31,2771', 0o00006, '', 'EXTEND', line=398)
W('31,2772', 0o31545, '', 'DCA', 'LANDTEMP', line=399)
W('31,2773', 0o53635, '', 'DXCH', 'LAND', line=400)
W('31,2774', 0o00006, '', 'EXTEND', line=401)
W('31,2775', 0o31547, '', 'DCA', 'LANDTEMP +2', line=402)
W('31,2776', 0o53637, '', 'DXCH', 'LAND +2', line=403)
W('31,2777', 0o00006, '', 'EXTEND', line=404)
W('31,3000', 0o31551, '', 'DCA', 'LANDTEMP +4', line=405)
W('31,3001', 0o53641, '', 'DXCH', 'LAND +4', line=406)

W('31,3002', 0o13013, '', 'TCF', 'RGVGCALC', line=408)

# *********************************************************************
# COMPUTE STATE IN GUIDANCE COORDINATES
# *********************************************************************
#
# RGVGCALC COMPUTATIONS ARE AS FOLLOWS:--
# VELOCITY RELATIVE TO THE SURFACE:
# _______   _   _   __
# ANGTERM = V + R * WM
# STATE IN GUIDANCE COORDINATES:
# ___   *   _   ____
# RGU = CG (R - LAND)
# ___   *   _   __   _
# VGU = CG (V - WM * R)
# Page 806 actually starts one line earlier but that would separate the markers from their variables
#
# HORIZONTAL VELOCITY FOR DISPLAY
#
# VHORIZ = 8 ABVAL (0, VG , VG )
# 2    1
# DEPRESSION ANGLE FOR DISPLAY:
# _   ____  ______
# LOOKANGL = ARCSIN(UNIT(R - LAND).XMBPIP)

W('31,3003', 0o06037, 'CALCRGVG', 'TC', 'INTPRET', 'IN IGNALG, COMPUTE V FROM INTEGRATION', line=433)
W('31,3004', 0o64375, '', 'VLOAD', 'MXV', '      OUTPUT AND TRIM CORRECTION TERM', kind='interp', line=434)
W('31,3005', 0o00025, '', '', 'VATT1', '      COMPUTED LAST PASS AND LEFT IN UNFC/2', kind='operand', line=435)
W('31,3006', 0o01734, '', '', 'REFSMMAT', kind='operand', line=436)
W('31,3007', 0o53362, '', 'VSR1', 'VAD', kind='interp', line=437)
W('31,3010', 0o03254, '', '', 'UNFC/2', kind='operand', line=438)
W('31,3011', 0o03527, '', 'STORE', 'V', kind='interp', line=439)
W('31,3012', 0o77776, '', 'EXIT', kind='interp', line=440)

W('31,3013', 0o06037, 'RGVGCALC', 'TC', 'INTPRET', 'ENTER HERE TO RECOMPUTE RG AND VG', line=442)
W('31,3014', 0o47375, '', 'VLOAD', 'VXV', kind='interp', line=443)
W('31,3015', 0o03521, '', '', 'R', kind='operand', line=444)
W('31,3016', 0o02325, '', '', 'WM', kind='operand', line=445)
W('31,3017', 0o70455, '', 'VAD', 'VSR2', 'RESCALE TO UNITS OF 2(9) M/CS', kind='interp', line=446)
W('31,3020', 0o03527, '', '', 'V', kind='operand', line=447)
W('31,3021', 0o02265, '', 'STORE', 'ANGTERM', kind='interp', line=448)
W('31,3022', 0o77721, '', 'MXV', kind='interp', line=449)
W('31,3023', 0o02603, '', '', 'CG', 'NO SHIFT SINCE ANGTERM IS DOUBLE SIZED', kind='operand', line=450)
W('31,3024', 0o03627, '', 'STORE', 'VGU', kind='interp', line=451)
W('31,3025', 0o55525, '', 'PDDL', 'VDEF', 'FORM (0,VG ,VG ) IN UNITS OF 2(10) M/CS', kind='interp', line=452)
W('31,3026', 0o06522, '', '', 'ZEROVECS', '          2   1', kind='operand', line=453)
W('31,3027', 0o52446, '', 'ABVAL', 'SL3', kind='interp', line=454)
W('31,3030', 0o26263, '', 'STOVL', 'VHORIZ', 'VHORIZ FOR DISPLAY DURING P65.', kind='interp', line=455)
W('31,3031', 0o03521, '', '', 'R', '          _   ____', kind='operand', line=456)
W('31,3032', 0o41451, '', 'VSU', 'PUSH', 'PUSH DOWN R - LAND', kind='interp', line=457)
W('31,3033', 0o03635, '', '', 'LAND', kind='operand', line=458)
W('31,3034', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=459)
W('31,3035', 0o02603, '', '', 'CG', kind='operand', line=460)
W('31,3036', 0o02637, '', 'STORE', 'RGU', kind='interp', line=461)
W('31,3037', 0o77646, '', 'ABVAL', kind='interp', line=462)
W('31,3040', 0o26625, '', 'STOVL', 'RANGEDSP', kind='interp', line=463)
W('31,3041', 0o50234, '', 'RTB', 'DOT', 'NOW IN MPAC IS SINE(LOOKANGL)/4', kind='interp', line=464)
W('31,3042', 0o21726, '', '', 'NORMUNIT', kind='operand', line=465)
W('31,3043', 0o02146, '', '', 'XNBPIP', kind='operand', line=466)
W('31,3044', 0o77776, '', 'EXIT', kind='interp', line=467)

W('31,3045', 0o30120, '', 'CA', 'FIXLOC', 'RESET PUSH DOWN POINTER', line=469)
W('31,3046', 0o54166, '', 'TS', 'PUSHLOC', line=470)

# Page 807
W('31,3047', 0o30154, '', 'CA', 'MPAC', 'COMPUTE LOOKANGLE ITSELF', line=473)
W('31,3050', 0o60000, '', 'DOUBLE', line=474)
W('31,3051', 0o04616, '', 'TC', 'BANKCALL', line=475)
W('31,3052', 0o61672, '', 'CADR', 'SPARCSIN -1', kind='data', line=476)
W('31,3053', 0o63753, '', 'AD', '1/2DEG', line=477)
W('31,3054', 0o00006, '', 'EXTEND', line=478)
W('31,3055', 0o73752, '', 'MP', '180DEGS', line=479)
W('31,3056', 0o55667, '', 'TS', 'LOOKANGL', 'LOOKANGL FOR DISPLAY DURING P64', line=480)

W('31,3057', 0o51351, 'BRSPOT3', 'INDEX', 'WCHPHASE', line=482)
W('31,3060', 0o12431, '', 'TCF', 'WHATGUID', line=483)

# **************************************************************************
# TTF/8 COMPUTATION
# **************************************************************************

W('31,3061', 0o03677, 'TTF/8CL', 'TC', 'INTPRETX', line=489)
W('31,3062', 0o77743, '', 'DLOAD*', kind='interp', line=490)
W('31,3063', 0o02431, '', '', 'JDG2TTF,1', kind='operand', line=491)
W('31,3064', 0o23571, '', 'STODL*', 'TABLTTF +6', 'A(3) = 8 JDG  TO TABLTTF', kind='interp', line=492)
W('31,3065', 0o02427, '', '', 'ADG2TTF,1', '            2', kind='operand', line=493)
W('31,3066', 0o17567, '', 'STODL', 'TABLTTF +4', 'A(2) = 6 ADG  TO TABLTTF', kind='interp', line=494)
W('31,3067', 0o03633, '', '', 'VGU +4', '            2', kind='operand', line=495)
W('31,3070', 0o42605, '', 'DMP', 'DAD*', kind='interp', line=496)
W('31,3071', 0o05656, '', '', '3/4DP', kind='operand', line=497)
W('31,3072', 0o02425, '', '', 'VDG2TTF,1', kind='operand', line=498)
W('31,3073', 0o23565, '', 'STODL*', 'TABLTTF +2', 'A(1) = (6 VGU  + 18 VDG )/8 TO TABLTTF', kind='interp', line=499)
W('31,3074', 0o02407, '', '', 'RDG +4,1', '             2         2', kind='operand', line=500)
W('31,3075', 0o41225, '', 'DSU', 'DMP', kind='interp', line=501)
W('31,3076', 0o02643, '', '', 'RGU +4', kind='operand', line=502)
W('31,3077', 0o05654, '', '', '3/8DP', kind='operand', line=503)
W('31,3100', 0o03563, '', 'STORE', 'TABLTTF', 'A(0) = -24 (RGU  - RDG )/64 TO TABLTTF', kind='interp', line=504)
W('31,3101', 0o77776, '', 'EXIT', '', '               2      2', kind='interp', line=505)

W('31,3102', 0o34744, '', 'CA', 'BIT8', line=507)
W('31,3103', 0o55572, '', 'TS', 'TABLTTF +10', 'FRACTIONAL PRECISION FOR TTF TO TABLE', line=508)

W('31,3104', 0o00006, '', 'EXTEND', line=510)
W('31,3105', 0o31643, '', 'DCA', 'TTF/8', line=511)
W('31,3106', 0o52155, '', 'DXCH', 'MPAC', 'LOADS TTF/8 (INITIAL GUESS) INTO MPAC', line=512)
W('31,3107', 0o34752, '', 'CAF', 'TWO', 'DEGREE - ONE', line=513)
W('31,3110', 0o54001, '', 'TS', 'L', line=514)
W('31,3111', 0o33746, '', 'CAF', 'TABLTTFL', line=515)
W('31,3112', 0o03553, '', 'TC', 'ROOTPSRS', 'YIELDS TTF/8 IN MPAC', line=516)
W('31,3113', 0o51351, '', 'INDEX', 'WCHPHASE', line=517)
W('31,3114', 0o12447, '', 'TCF', 'WHATALM', line=518)

W('31,3115', 0o00006, '', 'EXTEND', '', 'GOOD RETURN', line=520)
W('31,3116', 0o30155, '', 'DCA', 'MPAC', 'FETCH TTF/8 KEEPING IT IN MPAC', line=521)
W('31,3117', 0o53643, '', 'DXCH', 'TTF/8', 'CORRECTED TTF/8', line=522)

# Page 808
W('31,3120', 0o03704, '', 'TC', 'TDISPSET', line=525)

# (CONTINUE TO QUADGUID)

# *********************************************************************************
# MAIN GUIDANCE EQUATION
# *********************************************************************************
#
# AS PUBLISHED --
# ___   __       ___   __
# ___   ___   6(VDG + VG)   12(RDG - RG)
# ACG = ADG + ----------- + ------------
# TTF        (TTF)(TTF)
# AS HERE PROGRAMMED --
# ___   __
# 3 (1/4(RDG - RG)   ___   __)
# - (------------- + VDG + VG)
# ___   4 (    TTF/8               )   ___
# ACG = ---------------------------- + ADG
# TTF/8

W('31,3121', 0o41642, 'QUADGUID', 'CS', 'TTF/8', line=546)
W('31,3122', 0o61426, '', 'AD', 'LEADTIME', 'LEADTIME IS A NEGATIVE NUMBER', line=547)
W('31,3123', 0o64733, '', 'AD', 'POSMAX', 'SAFEGUARD THE COMPUTATIONS THAT FOLLOW', line=548)
W('31,3124', 0o54001, '', 'TS', 'L', '      BY FORCING -TTF*LEADTIME > OR = ZERO', line=549)
W('31,3125', 0o40001, '', 'CS', 'L', line=550)
W('31,3126', 0o60001, '', 'AD', 'L', line=551)
W('31,3127', 0o22007, '', 'ZL', line=552)
W('31,3130', 0o00006, '', 'EXTEND', line=553)
W('31,3131', 0o11642, '', 'DV', 'TTF/8', line=554)
W('31,3132', 0o54130, '', 'TS', 'BUF', '- RATIO OF LAG-DIMINISHED TTF TO TTF', line=555)
W('31,3133', 0o00006, '', 'EXTEND', line=556)
W('31,3134', 0o70000, '', 'SQUARE', line=557)
W('31,3135', 0o54131, '', 'TS', 'BUF +1', line=558)
W('31,3136', 0o60130, '', 'AD', 'BUF', line=559)
W('31,3137', 0o56131, '', 'XCH', 'BUF +1', 'RATIO SQUARED - RATIO', line=560)
W('31,3140', 0o60131, '', 'AD', 'BUF +1', line=561)
W('31,3141', 0o54154, '', 'TS', 'MPAC', 'COEFFICIENT FOR VGU TERM', line=562)
W('31,3142', 0o60131, '', 'AD', 'BUF +1', line=563)
W('31,3143', 0o50120, '', 'INDEX', 'FIXLOC', line=564)
W('31,3144', 0o54032, '', 'TS', '26D', 'COEFFICIENT FOR RDG-RGU TERM', line=565)
W('31,3145', 0o60131, '', 'AD', 'BUF +1', line=566)
W('31,3146', 0o50120, '', 'INDEX', 'FIXLOC', line=567)
W('31,3147', 0o54034, '', 'TS', '28D', 'COEFFICIENT FOR VDG TERM', line=568)
W('31,3150', 0o60130, '', 'AD', 'BUF', line=569)
W('31,3151', 0o64733, '', 'AD', 'POSMAX', line=570)
# Page 809
W('31,3152', 0o60131, '', 'AD', 'BUF +1', line=572)
W('31,3153', 0o60131, '', 'AD', 'BUF +1', line=573)
W('31,3154', 0o50120, '', 'INDEX', 'FIXLOC', line=574)
W('31,3155', 0o54036, '', 'TS', '30D', 'COEFFICIENT FOR ADG TERM', line=575)

W('31,3156', 0o34755, '', 'CAF', 'ZERO', line=577)
W('31,3157', 0o54163, '', 'TS', 'MODE', line=578)

W('31,3160', 0o03677, '', 'TC', 'INTPRETX', line=580)
W('31,3161', 0o65361, '', 'VXSC', 'PDDL', kind='interp', line=581)
W('31,3162', 0o03627, '', '', 'VGU', kind='operand', line=582)
W('31,3163', 0o00035, '', '', '28D', kind='operand', line=583)
W('31,3164', 0o62757, '', 'VXSC*', 'PDVL*', kind='interp', line=584)
W('31,3165', 0o02411, '', '', 'VDG,1', kind='operand', line=585)
W('31,3166', 0o02403, '', '', 'RDG,1', kind='operand', line=586)
W('31,3167', 0o70251, '', 'VSU', 'V/SC', kind='interp', line=587)
W('31,3170', 0o02637, '', '', 'RGU', kind='operand', line=588)
W('31,3171', 0o03643, '', '', 'TTF/8', kind='operand', line=589)
W('31,3172', 0o74342, '', 'VSR2', 'VXSC', kind='interp', line=590)
W('31,3173', 0o00033, '', '', '26D', kind='operand', line=591)
W('31,3174', 0o53255, '', 'VAD', 'VAD', kind='interp', line=592)
W('31,3175', 0o74341, '', 'V/SC', 'VXSC', kind='interp', line=593)
W('31,3176', 0o03643, '', '', 'TTF/8', kind='operand', line=594)
W('31,3177', 0o05656, '', '', '3/4DP', kind='operand', line=595)
W('31,3200', 0o73725, '', 'PDDL', 'VXSC*', kind='interp', line=596)
W('31,3201', 0o00037, '', '', '30D', kind='operand', line=597)
W('31,3202', 0o02417, '', '', 'ADG,1', kind='operand', line=598)
W('31,3203', 0o77655, '', 'VAD', kind='interp', line=599)
W('31,3204', 0o76505, 'AFCCALC1', 'VXM', 'VSL1', 'VERGUID COMES HERE', kind='interp', line=600)
W('31,3205', 0o02603, '', '', 'CG', kind='operand', line=601)
W('31,3206', 0o70315, '', 'PDVL', 'V/SC', kind='interp', line=602)
W('31,3207', 0o01237, '', '', 'GDT/2', kind='operand', line=603)
W('31,3210', 0o05652, '', '', 'GSCALE', kind='operand', line=604)
W('31,3211', 0o45445, '', 'BVSU', 'STADR', kind='interp', line=605)
W('31,3212', 0o74523, '', 'STORE', 'UNFC/2', 'UNFC/2 NEED NOT BE UNITIZED', kind='interp', line=606)
W('31,3213', 0o77646, '', 'ABVAL', kind='interp', line=607)
W('31,3214', 0o17464, 'AFCCALC2', 'STODL', '/AFC/', 'MAGNITUDE OF AFC FOR THROTTLE', kind='interp', line=608)
W('31,3215', 0o03254, '', '', 'UNFC/2', 'VERTICAL COMPONENT', kind='operand', line=609)
W('31,3216', 0o65316, '', 'DSQ', 'PDDL', kind='interp', line=610)
W('31,3217', 0o03256, '', '', 'UNFC/2 +2', 'OUT-OF-PLANE', kind='operand', line=611)
W('31,3220', 0o65316, '', 'DSQ', 'PDDL', kind='interp', line=612)
W('31,3221', 0o05650, '', '', 'HIGHESTF', kind='operand', line=613)
W('31,3222', 0o63471, '', 'DDV', 'DSQ', kind='interp', line=614)
W('31,3223', 0o01245, '', '', 'MASS', '                       2    2    2', kind='operand', line=615)
W('31,3224', 0o45225, '', 'DSU', 'DSU', 'AMAXHORIZ = SQRT(ATOTAL - A  - A  )', kind='interp', line=616)
W('31,3225', 0o71244, '', 'BPL', 'DLOAD', '                           1    0', kind='interp', line=617)
W('31,3226', 0o63230, '', '', 'AFCCALC3', kind='operand', line=618)
W('31,3227', 0o06522, '', '', 'ZEROVECS', kind='operand', line=619)
W('31,3230', 0o43366, 'AFCCALC3', 'SQRT', 'DAD', kind='interp', line=620)
W('31,3231', 0o03260, '', '', 'UNFC/2 +4', kind='operand', line=621)
# Page 810
W('31,3232', 0o44244, '', 'BPL', 'BDSU', kind='interp', line=623)
W('31,3233', 0o63236, '', '', 'AFCCLEND', kind='operand', line=624)
W('31,3234', 0o03260, '', '', 'UNFC/2 +4', kind='operand', line=625)
W('31,3235', 0o03260, '', 'STORE', 'UNFC/2 +4', kind='interp', line=626)
W('31,3236', 0o77776, 'AFCCLEND', 'EXIT', kind='interp', line=627)
W('31,3237', 0o03740, '', 'TC', 'FASTCHNG', line=628)

W('31,3240', 0o31351, '', 'CA', 'WCHPHASE', 'PREPARE FOR PHASE SWITCHING LOGIC', line=630)
W('31,3241', 0o55621, '', 'TS', 'WCHPHOLD', line=631)
W('31,3242', 0o25623, '', 'INCR', 'FLPASS0', 'INCREMENT PASS COUNTER', line=632)

W('31,3243', 0o51351, 'BRSPOT4', 'INDEX', 'WCHPHASE', line=634)
W('31,3244', 0o12435, '', 'TCF', 'AFTRGUID', line=635)

# ***********************************************************************
# ERECT GUIDANCE-STABLE MEMBER TRANSFORMATION MATRIX
# ***********************************************************************

W('31,3245', 0o35014, 'CGCALC', 'CAF', 'EBANK5', line=641)
W('31,3246', 0o54003, '', 'TS', 'EBANK', line=642)
#   EBANK= TCGIBRAK
W('31,3247', 0o00006, '', 'EXTEND', line=644)
W('31,3250', 0o51351, '', 'INDEX', 'WCHPHASE', line=645)
W('31,3251', 0o52452, '', 'INDEX', 'TARGTDEX', line=646)
W('31,3252', 0o31435, '', 'DCA', 'TCGFBRAK', line=647)
W('31,3253', 0o24006, '', 'INCR', 'BBANK', line=648)
W('31,3254', 0o24006, '', 'INCR', 'BBANK', line=649)
#   EBANK= TTF/8
W('31,3255', 0o61642, '', 'AD', 'TTF/8', line=651)
W('31,3256', 0o56001, '', 'XCH', 'L', line=652)
W('31,3257', 0o61642, '', 'AD', 'TTF/8', line=653)
W('31,3260', 0o10000, '', 'CCS', 'A', line=654)
W('31,3261', 0o10001, '', 'CCS', 'L', line=655)
W('31,3262', 0o13313, '', 'TCF', 'EXTLOGIC', line=656)
W('31,3263', 0o13313, '', 'TCF', 'EXTLOGIC', line=657)
W('31,3264', 0o13265, '', 'NOOP', line=658)

W('31,3265', 0o03677, '', 'TC', 'INTPRETX', line=660)
W('31,3266', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=661)
W('31,3267', 0o03635, '', '', 'LAND', kind='operand', line=662)
W('31,3270', 0o16603, '', 'STODL', 'CG', kind='interp', line=663)
W('31,3271', 0o03643, '', '', 'TTF/8', kind='operand', line=664)
W('31,3272', 0o74203, '', 'DMP*', 'VXSC', kind='interp', line=665)
W('31,3273', 0o02433, '', '', 'GAINBRAK,1', 'NUMERO MYSTERIOSO', kind='operand', line=666)
W('31,3274', 0o02265, '', '', 'ANGTERM', kind='operand', line=667)
W('31,3275', 0o77655, '', 'VAD', kind='interp', line=668)
W('31,3276', 0o03635, '', '', 'LAND', kind='operand', line=669)
W('31,3277', 0o47051, '', 'VSU', 'RTB', kind='interp', line=670)
W('31,3300', 0o03521, '', '', 'R', kind='operand', line=671)
W('31,3301', 0o21726, '', '', 'NORMUNIT', kind='operand', line=672)
# Page 811
W('31,3302', 0o47035, '', 'VXV', 'RTB', kind='interp', line=674)
W('31,3303', 0o03635, '', '', 'LAND', kind='operand', line=675)
W('31,3304', 0o21726, '', '', 'NORMUNIT', kind='operand', line=676)
W('31,3305', 0o26611, '', 'STOVL', 'CG +6', 'SECOND ROW', kind='interp', line=677)
W('31,3306', 0o02603, '', '', 'CG', kind='operand', line=678)
W('31,3307', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=679)
W('31,3310', 0o02611, '', '', 'CG +6', kind='operand', line=680)
W('31,3311', 0o02617, '', 'STORE', 'CG +14', kind='interp', line=681)
W('31,3312', 0o77776, '', 'EXIT', kind='interp', line=682)

# (CONTINUE TO EXTLOGIC)
#
# ***********************************************************************
# PREPARE TO EXIT
# ***********************************************************************
#
# DECIDE (1) HOW TO EXIT, AND (2) WHETHER TO SWITCH PHASES
#
W('31,3313', 0o51351, 'EXTLOGIC', 'INDEX', 'WCHPHASE', 'WCHPHASE = 1   APPRQUAD', line=692)
W('31,3314', 0o31423, '', 'CA', 'TENDBRAK', 'WCHPHASE = 0   BRAKQUAD', line=693)
W('31,3315', 0o61642, '', 'AD', 'TTF/8', line=694)

W('31,3316', 0o00006, 'EXSPOT1', 'EXTEND', line=696)
W('31,3317', 0o51351, '', 'INDEX', 'WCHPHASE', line=697)
W('31,3320', 0o62441, '', 'BZMF', 'WHATEXIT', line=698)

W('31,3321', 0o03740, '', 'TC', 'FASTCHNG', line=700)

W('31,3322', 0o31621, '', 'CA', 'WCHPHOLD', line=702)
W('31,3323', 0o64753, '', 'AD', 'ONE', line=703)
W('31,3324', 0o55351, '', 'TS', 'WCHPHASE', line=704)
W('31,3325', 0o34755, '', 'CA', 'ZERO', line=705)
W('31,3326', 0o55623, '', 'TS', 'FLPASS0', 'RESET FLPASS0', line=706)

W('31,3327', 0o51621, '', 'INDEX', 'WCHPHOLD', line=708)
W('31,3330', 0o12441, '', 'TCF', 'WHATEXIT', line=709)

# ***********************************************************************
# ROUTINES FOR EXITING FROM LANDING GUIDANCE
# ***********************************************************************
#
# 1.    EXGSUB IS THE RETURN WHEN GUIDSUB IS CALLED BY THE IGNITION ALGORITHM.
# 2.    EXBRAK IN THE EXIT USED DURING THE BRAKING PHASE.  IN THIS CASE UNIT(R) IS THE WINDOW POINTING VECTOR.
# 3.    EXNORM IS THE EXIT USED AT OTHER TIMES DURING THE BURN.
# (EXOVFLOW IS A SUBROUTINE OF EXBRAK AND EXNORM CALLED WHEN OVERFLOW OCCURRED ANYWHERE IN GUIDANCE.)

W('31,3331', 0o06037, 'EXGSUB', 'TC', 'INTPRET', 'COMPUTE TRIM VELOCITY CORRECTION TERM.', line=720)
# Page 812
W('31,3332', 0o47175, '', 'VLOAD', 'RTB', kind='interp', line=722)
W('31,3333', 0o03254, '', '', 'UNFC/2', kind='operand', line=723)
W('31,3334', 0o21726, '', '', 'NORMUNIT', kind='operand', line=724)
W('31,3335', 0o74361, '', 'VXSC', 'VXSC', kind='interp', line=725)
W('31,3336', 0o03423, '', '', 'ZOOMTIME', kind='operand', line=726)
W('31,3337', 0o22001, '', '', 'TRIMACCL', kind='operand', line=727)
W('31,3340', 0o03254, '', 'STORE', 'UNFC/2', kind='interp', line=728)
W('31,3341', 0o77776, '', 'EXIT', kind='interp', line=729)

W('31,3342', 0o11647, '', 'CCS', 'NGUIDSUB', line=731)
W('31,3343', 0o12460, '', 'TCF', 'GUIDSUB', line=732)
W('31,3344', 0o11646, '', 'CCS', 'NIGNLOOP', line=733)
W('31,3345', 0o13350, '', 'TCF', '+3', line=734)
W('31,3346', 0o05567, '', 'TC', 'ALARM', line=735)
W('31,3347', 0o01412, '', 'OCT', '01412', kind='data', line=736)

W('31,3350', 0o04635, '', 'TC', 'POSTJUMP', line=738)
W('31,3351', 0o65102, '', 'CADR', 'DDUMCALC', kind='data', line=739)

W('31,3352', 0o06037, 'EXBRAK', 'TC', 'INTPRET', line=741)
W('31,3353', 0o77775, '', 'VLOAD', kind='interp', line=742)
W('31,3354', 0o03537, '', '', 'UNIT/R/', kind='operand', line=743)
W('31,3355', 0o03262, '', 'STORE', 'UNWC/2', kind='interp', line=744)
W('31,3356', 0o77776, '', 'EXIT', kind='interp', line=745)
W('31,3357', 0o13432, '', 'TCF', 'STEER?', line=746)

W('31,3360', 0o06037, 'EXNORM', 'TC', 'INTPRET', line=748)
W('31,3361', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=749)
W('31,3362', 0o03635, '', '', 'LAND', kind='operand', line=750)
W('31,3363', 0o03521, '', '', 'R', kind='operand', line=751)
W('31,3364', 0o77634, '', 'RTB', kind='interp', line=752)
W('31,3365', 0o21726, '', '', 'NORMUNIT', kind='operand', line=753)
W('31,3366', 0o03262, '', 'STORE', 'UNWC/2', 'UNIT(LAND - R) IS TENTATIVE CHOICE', kind='interp', line=754)
W('31,3367', 0o50235, '', 'VXV', 'DOT', kind='interp', line=755)
W('31,3370', 0o02146, '', '', 'XNBPIP', kind='operand', line=756)
W('31,3371', 0o02611, '', '', 'CG +6', kind='operand', line=757)
W('31,3372', 0o77776, '', 'EXIT', '', 'WITH PROJ IN MPAC 1/8 REAL SIZE', kind='interp', line=758)

W('31,3373', 0o40154, '', 'CS', 'MPAC', 'GET COEFFICIENT FOR CG +14', line=760)
W('31,3374', 0o63754, '', 'AD', 'PROJMAX', line=761)
W('31,3375', 0o64733, '', 'AD', 'POSMAX', line=762)
W('31,3376', 0o54130, '', 'TS', 'BUF', line=763)
W('31,3377', 0o40130, '', 'CS', 'BUF', line=764)
W('31,3400', 0o26130, '', 'ADS', 'BUF', 'RESULT IS 0 IF PROJMAX - PROJ NEGATIVE', line=765)

W('31,3401', 0o43755, '', 'CS', 'PROJMIN', 'GET COEFFICIENT FOR UNIT(LAND - R)', line=767)
W('31,3402', 0o60154, '', 'AD', 'MPAC', line=768)
W('31,3403', 0o64733, '', 'AD', 'POSMAX', line=769)
W('31,3404', 0o54131, '', 'TS', 'BUF +1', line=770)
W('31,3405', 0o40131, '', 'CS', 'BUF +1', line=771)
# Page 813
W('31,3406', 0o26131, '', 'ADS', 'BUF +1', 'RESULT IS 0 IF PROJ - PROJMIN NEGATIVE', line=773)

W('31,3407', 0o34751, '', 'CAF', 'FOUR', line=775)
W('31,3410', 0o76242, 'UNWCLOOP', 'MASK', 'SIX', line=776)
W('31,3411', 0o54002, '', 'TS', 'Q', line=777)
W('31,3412', 0o35014, '', 'CA', 'EBANK5', line=778)
W('31,3413', 0o54003, '', 'TS', 'EBANK', line=779)
#   EBANK= CG
W('31,3414', 0o30130, '', 'CA', 'BUF', line=781)
W('31,3415', 0o00006, '', 'EXTEND', line=782)
W('31,3416', 0o50002, '', 'INDEX', 'Q', line=783)
W('31,3417', 0o71616, '', 'MP', 'CG +14', line=784)
W('31,3420', 0o24006, '', 'INCR', 'BBANK', line=785)
#   EBANK= UNWC/2
W('31,3421', 0o50002, '', 'INDEX', 'Q', line=787)
W('31,3422', 0o53662, '', 'DXCH', 'UNWC/2', line=788)
W('31,3423', 0o00006, '', 'EXTEND', line=789)
W('31,3424', 0o70131, '', 'MP', 'BUF +1', line=790)
W('31,3425', 0o50002, '', 'INDEX', 'Q', line=791)
W('31,3426', 0o21662, '', 'DAS', 'UNWC/2', line=792)
W('31,3427', 0o10002, '', 'CCS', 'Q', line=793)
W('31,3430', 0o13410, '', 'TCF', 'UNWCLOOP', line=794)

W('31,3431', 0o24006, '', 'INCR', 'BBANK', line=796)
#   EBANK= PIF

W('31,3432', 0o30076, 'STEER?', 'CA', 'FLAGWRD2', 'IF STEERSW DOWN NO OUTPUTS', line=799)
W('31,3433', 0o74741, '', 'MASK', 'STEERBIT', line=800)
W('31,3434', 0o00006, '', 'EXTEND', line=801)
W('31,3435', 0o13443, '', 'BZF', 'RATESTOP', line=802)

W('31,3436', 0o30121, 'EXVERT', 'CA', 'OVFIND', 'IF OVERFLOW ANYWHERE IN GUIDANCE', line=804)
W('31,3437', 0o00006, '', 'EXTEND', '', "      DON'T CALL THROTTLE OR FINDCDUW", line=805)
W('31,3440', 0o13453, '', 'BZF', '+13', line=806)

W('31,3441', 0o05567, 'EXOVFLOW', 'TC', 'ALARM', 'SOUND THE ALARM NON-ABORTIVELY', line=808)
W('31,3442', 0o01410, '', 'OCT', '01410', kind='data', line=809)

W('31,3443', 0o34737, 'RATESTOP', 'CAF', 'BIT13', 'ARE WE IN ATTITUDE-HOLD?', line=811)
W('31,3444', 0o00006, '', 'EXTEND', line=812)
W('31,3445', 0o02031, '', 'RAND', 'CHAN31', line=813)
W('31,3446', 0o00006, '', 'EXTEND', line=814)
W('31,3447', 0o13460, '', 'BZF', 'DISPEXIT', 'YES', line=815)

W('31,3450', 0o04616, '', 'TC', 'BANKCALL', 'NO:  DO A STOPRATE', line=817)
W('31,3451', 0o40165, '', 'CADR', 'STOPRATE', kind='data', line=818)

W('31,3452', 0o13460, '', 'TCF', 'DISPEXIT', line=820)

W('31,3453', 0o02216, 'GDUMP1', 'TC', 'THROTTLE', line=822)
# Page 814
W('31,3454', 0o06037, '', 'TC', 'INTPRET', line=824)
W('31,3455', 0o77624, '', 'CALL', kind='interp', line=825)
W('31,3456', 0o61111, '', '', 'FINDCDUW -2', kind='operand', line=826)
W('31,3457', 0o77776, '', 'EXIT', kind='interp', line=827)

# (CONTINUE TO DISPEXIT)

# ***********************************************************************
# GUIDANCE LOOP DISPLAYS
# ***********************************************************************

W('31,3460', 0o00006, 'DISPEXIT', 'EXTEND', '', 'KILL GROUP 3:  DISPLAYS WILL BE', line=835)
W('31,3461', 0o34755, '', 'DCA', 'NEG0', '      RESTORED BY NEXT GUIDANCE CYCLE.', line=836)
W('31,3462', 0o52757, '', 'DXCH', '-PHASE3', line=837)

W('31,3463', 0o40104, '', 'CS', 'FLAGWRD8', 'IF FLUNDISP IS SET, NO DISPLAY THIS PASS', line=839)
W('31,3464', 0o74742, '', 'MASK', 'FLUNDBIT', line=840)
W('31,3465', 0o00006, '', 'EXTEND', line=841)
W('31,3466', 0o13476, '', 'BZF', 'ENDLLJOB', 'TO PICK UP THE TAG', line=842)

W('31,3467', 0o51621, '', 'INDEX', 'WCHPHOLD', line=844)
W('31,3470', 0o12443, '', 'TCF', 'WHATDISP', line=845)

W('31,3471', 0o05353, '', 'TC', 'PHASCHNG', 'KILL GROUP 5', line=847)
W('31,3472', 0o00035, '', 'OCT', '00035', kind='data', line=848)

W('31,3473', 0o33756, 'P63DISPS', 'CAF', 'V06N63', line=850)
W('31,3474', 0o04616, 'DISPCOMN', 'TC', 'BANKCALL', line=851)
W('31,3475', 0o20470, '', 'CADR', 'REGODSPR', kind='data', line=852)

W('31,3476', 0o15155, 'ENDLLJOB', 'TCF', 'ENDOFJOB', line=854)

W('31,3477', 0o31666, 'P64DISPS', 'CA', 'TREDES', 'HAS TREDES REACHED ZERO?', line=856)
W('31,3500', 0o00006, '', 'EXTEND', line=857)
W('31,3501', 0o13523, '', 'BZF', 'RED-OVER', 'YES: CLEAR REDESIGNATION FLAG', line=858)

W('31,3502', 0o40102, '', 'CS', 'FLAGWRD6', 'NO:  IS REDFLAG SET?', line=860)
W('31,3503', 0o74746, '', 'MASK', 'REDFLBIT', line=861)
W('31,3504', 0o00006, '', 'EXTEND', line=862)
W('31,3505', 0o13525, '', 'BZF', 'REDES-OK', 'YES:  DO STATIC DISPLAY', line=863)

W('31,3506', 0o33757, '', 'CAF', 'V06N64', 'OTHERWISE USE FLASHING DISPLAY', line=865)
W('31,3507', 0o04616, '', 'TC', 'BANKCALL', line=866)
W('31,3510', 0o20462, '', 'CADR', 'REFLASHR', kind='data', line=867)
W('31,3511', 0o16001, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=868)
W('31,3512', 0o13515, '', 'TCF', 'P64CEED', 'PROCEED       PERMIT REDESIGNATIONS', line=869)
W('31,3513', 0o13477, '', 'TCF', 'P64DISPS', 'RECYCLE', line=870)
# Page 815
W('31,3514', 0o13476, '', 'TCF', 'ENDLLJOB', line=872)

W('31,3515', 0o34755, 'P64CEED', 'CAF', 'ZERO', line=874)
W('31,3516', 0o55267, '', 'TS', 'ELINCR1', line=875)
W('31,3517', 0o55266, '', 'TS', 'AZINCR1', line=876)

W('31,3520', 0o05504, '', 'TC', 'UPFLAG', 'ENABLE REDESIGNATION LOGIC', line=878)
W('31,3521', 0o00143, '', 'ADRES', 'REDFLAG', kind='data', line=879)

W('31,3522', 0o15155, '', 'TCF', 'ENDOFJOB', line=881)

W('31,3523', 0o05516, 'RED-OVER', 'TC', 'DOWNFLAG', line=883)
W('31,3524', 0o00143, '', 'ADRES', 'REDFLAG', kind='data', line=884)
W('31,3525', 0o33757, 'REDES-OK', 'CAF', 'V06N64', line=885)
W('31,3526', 0o13474, '', 'TCF', 'DISPCOMN', line=886)

W('31,3527', 0o33760, 'VERTDISP', 'CAF', 'V06N60', line=889)
W('31,3530', 0o13474, '', 'TCF', 'DISPCOMN', line=890)

# **************************************************************************
# GUIDANCE FOR P65
# **************************************************************************

W('31,3531', 0o11647, 'VERTGUID', 'CCS', 'WCHVERT', line=897)
W('31,3532', 0o13545, '', 'TCF', 'P67VERT', 'POSITIVE NON-ZERO ---> P67', line=898)
W('31,3533', 0o13543, '', 'TCF', 'P66VERT', '+0', line=899)
#
# THE P65 GUIDANCE EQUATION IS AS FOLLOWS --
# ____   ___
# V2FG - VGU
# ACG = ----------
# TAUVERT

W('31,3534', 0o06037, 'P65VERT', 'TC', 'INTPRET', line=907)
W('31,3535', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=908)
W('31,3536', 0o02511, '', '', 'V2FG', kind='operand', line=909)
W('31,3537', 0o03627, '', '', 'VGU', kind='operand', line=910)
W('31,3540', 0o52141, '', 'V/SC', 'GOTO', kind='interp', line=911)
W('31,3541', 0o02517, '', '', 'TAUVERT', kind='operand', line=912)
W('31,3542', 0o63204, '', '', 'AFCCALC1', kind='operand', line=913)
# Page 816
# **********************************************************
# GUIDANCE FOR P66
# **********************************************************

W('31,3543', 0o04635, 'P66VERT', 'TC', 'POSTJUMP', line=919)
W('31,3544', 0o65270, '', 'CADR', 'P66VERTA', kind='data', line=920)

W('31,3545', 0o05353, 'P67VERT', 'TC', 'PHASCHNG', 'TERMINATE GROUP 3.', line=922)
W('31,3546', 0o00003, '', 'OCT', '00003', kind='data', line=923)

W('31,3547', 0o06037, '', 'TC', 'INTPRET', line=925)
W('31,3550', 0o52175, '', 'VLOAD', 'GOTO', kind='interp', line=926)
W('31,3551', 0o03527, '', '', 'V', kind='operand', line=927)
W('31,3552', 0o65517, '', '', 'VHORCOMP', kind='operand', line=928)

#   SETLOC P66LOC
#   BANK
#   COUNT* $$/F2DPS

W('32,3263', 0o37710, 'RODTASK', 'CAF', 'PRIO22', line=934)
W('32,3264', 0o05105, '', 'TC', 'FINDVAC', line=935)
#   EBANK= DVCNTR
W('32,3265', 0o03275, '', '2CADR', 'RODCOMP', kind='data', line=937)
W('32,3266', 0o64067, kind='data', line=937)

W('32,3267', 0o15261, '', 'TCF', 'TASKOVER', line=939)

W('32,3270', 0o05353, 'P66VERTA', 'TC', 'PHASCHNG', 'TERMINATE GROUP 3.', line=941)
W('32,3271', 0o00003, '', 'OCT', '00003', kind='data', line=942)

W('32,3272', 0o34777, '', 'CAF', '1SEC', line=944)
W('32,3273', 0o05173, '', 'TC', 'TWIDDLE', line=945)
W('32,3274', 0o03263, '', 'ADRES', 'RODTASK', kind='data', line=946)

W('32,3275', 0o00004, 'RODCOMP', 'INHINT', line=948)
W('32,3276', 0o34755, '', 'CAF', 'ZERO', line=949)
W('32,3277', 0o57746, '', 'XCH', 'RODCOUNT', line=950)
W('32,3300', 0o00006, '', 'EXTEND', line=951)
W('32,3301', 0o71756, '', 'MP', 'RODSCAL1', line=952)
W('32,3302', 0o21645, '', 'DAS', 'VDGVERT', 'UPDATE DESIRED ALTITUDE RATE.', line=953)

W('32,3303', 0o00006, '', 'EXTEND', '', 'SET OLDPIPAX,Y,Z = PIPAX,Y,Z', line=955)
W('32,3304', 0o30040, '', 'DCA', 'PIPAX', line=956)
W('32,3305', 0o53764, '', 'DXCH', 'OLDPIPAX', line=957)
W('32,3306', 0o52071, '', 'DXCH', 'RUPTREG1', 'SET RUPTREG1,2,3 = OLDPIPAX,Y,Z', line=958)
W('32,3307', 0o30041, '', 'CA', 'PIPAZ', line=959)
W('32,3310', 0o57765, '', 'XCH', 'OLDPIPAZ', line=960)
W('32,3311', 0o56072, '', 'XCH', 'RUPTREG3', line=961)

W('32,3312', 0o00006, '', 'EXTEND', '', 'SNAPSHOT TIME OF PIPA READING.', line=963)
W('32,3313', 0o30025, '', 'DCA', 'TIME2', line=964)
# Page 817
W('32,3314', 0o53762, '', 'DXCH', 'THISTPIP', line=966)

W('32,3315', 0o31763, '', 'CA', 'OLDPIPAX', line=968)
W('32,3316', 0o61160, '', 'AD', 'PIPATMPX', line=969)
W('32,3317', 0o54154, '', 'TS', 'MPAC', 'MPAC(X) = PIPAX + PIPATMPX', line=970)
W('32,3320', 0o31764, '', 'CA', 'OLDPIPAY', line=971)
W('32,3321', 0o61161, '', 'AD', 'PIPATMPY', line=972)
W('32,3322', 0o54157, '', 'TS', 'MPAC +3', 'MPAC(Y) = PIPAY + PIPATMPY', line=973)
W('32,3323', 0o31765, '', 'CA', 'OLDPIPAZ', line=974)
W('32,3324', 0o61162, '', 'AD', 'PIPATMPZ', line=975)
W('32,3325', 0o54161, '', 'TS', 'MPAC +5', 'MPAC(Z) = PIPAZ + PIPATMPZ', line=976)

W('32,3326', 0o41763, '', 'CS', 'OLDPIPAX', line=978)
W('32,3327', 0o61254, '', 'AD', 'TEMX', line=979)
W('32,3330', 0o60070, '', 'AD', 'RUPTREG1', line=980)
W('32,3331', 0o55766, '', 'TS', 'DELVROD', line=981)
W('32,3332', 0o41764, '', 'CS', 'OLDPIPAY', line=982)
W('32,3333', 0o61255, '', 'AD', 'TEMY', line=983)
W('32,3334', 0o60071, '', 'AD', 'RUPTREG2', line=984)
W('32,3335', 0o55770, '', 'TS', 'DELVROD +2', line=985)
W('32,3336', 0o41765, '', 'CS', 'OLDPIPAZ', line=986)
W('32,3337', 0o61256, '', 'AD', 'TEMZ', line=987)
W('32,3340', 0o60072, '', 'AD', 'RUPTREG3', line=988)
W('32,3341', 0o55772, '', 'TS', 'DELVROD +4', line=989)

W('32,3342', 0o34755, '', 'CAF', 'ZERO', line=991)
W('32,3343', 0o54155, '', 'TS', 'MPAC +1', 'ZERO LO-ORDER MPAC COMPONENTS', line=992)
W('32,3344', 0o54160, '', 'TS', 'MPAC +4', line=993)
W('32,3345', 0o54162, '', 'TS', 'MPAC +6', line=994)
W('32,3346', 0o55254, '', 'TS', 'TEMX', 'ZERO TEMX, TEMY, AND TEMZ SO WE WILL', line=995)
W('32,3347', 0o55255, '', 'TS', 'TEMY', '      KNOW WHEN READACCS CHANGES THEM.', line=996)
W('32,3350', 0o55256, '', 'TS', 'TEMZ', line=997)
W('32,3351', 0o44753, '', 'CS', 'ONE', line=998)
W('32,3352', 0o54163, '', 'TS', 'MODE', line=999)
W('32,3353', 0o06037, '', 'TC', 'INTPRET', line=1000)
W('32,3354', 0o65361, 'ITRPNT1', 'VXSC', 'PDDL', 'SCALE MPAC TO M/CS *2(-7) AND PUSH    (6)', kind='interp', line=1001)
W('32,3355', 0o26022, '', '', 'KPIP1', kind='operand', line=1002)
W('32,3356', 0o03762, '', '', 'THISTPIP', kind='operand', line=1003)
W('32,3357', 0o77625, '', 'DSU', kind='interp', line=1004)
W('32,3360', 0o01235, '', '', 'PIPTIME', kind='operand', line=1005)
W('32,3361', 0o00037, '', 'STORE', '30D', '30-31D CONTAINS TIME IN CS SINCE PIPTIME', kind='interp', line=1006)
W('32,3362', 0o63271, '', 'DDV', 'PDVL', '                                      (8)', kind='interp', line=1007)
W('32,3363', 0o27153, '', '', '4SEC(28)', kind='operand', line=1008)
W('32,3364', 0o01237, '', '', 'GDT/2', kind='operand', line=1009)
W('32,3365', 0o74251, '', 'VSU', 'VXSC', '                                      (6)', kind='interp', line=1010)
W('32,3366', 0o02631, '', '', 'VBIAS', kind='operand', line=1011)
W('32,3367', 0o53352, '', 'VSL2', 'VAD', kind='interp', line=1012)
W('32,3370', 0o03527, '', '', 'V', kind='operand', line=1013)
W('32,3371', 0o45455, '', 'VAD', 'STADR', '                                      (0)', kind='interp', line=1014)
W('32,3372', 0o53746, '', 'STOVL', '24D', 'STORE UPDATED VELOCITY IN 24-29D', kind='interp', line=1015)
# Page 818
W('32,3373', 0o03521, '', '', 'R', kind='operand', line=1017)
W('32,3374', 0o77656, '', 'UNIT', kind='interp', line=1018)
W('32,3375', 0o00017, '', 'STORE', '14D', kind='interp', line=1019)
W('32,3376', 0o72441, '', 'DOT', 'SL1', kind='interp', line=1020)
W('32,3377', 0o00031, '', '', '24D', kind='operand', line=1021)
W('32,3400', 0o17474, '', 'STODL', 'HDOTDISP', 'UPDATE HDOTDISP RATE FOR NOUN 63.', kind='interp', line=1022)
W('32,3401', 0o00037, '', '', '30D', kind='operand', line=1023)
W('32,3402', 0o41261, '', 'SL', 'DMP', kind='interp', line=1024)
W('32,3403', 0o20214, '', '', '11D', kind='operand', line=1025)
W('32,3404', 0o03474, '', '', 'HDOTDISP', kind='operand', line=1026)
W('32,3405', 0o45215, '', 'DAD', 'DSU', kind='interp', line=1027)
W('32,3406', 0o00045, '', '', '36D', kind='operand', line=1028)
W('32,3407', 0o02333, '', '', '/LAND/', kind='operand', line=1029)
W('32,3410', 0o17775, '', 'STODL', 'HCALC1', 'UPDATE HCALC1 FOR NOUN 63.', kind='interp', line=1030)
W('32,3411', 0o03474, '', '', 'HDOTDISP', kind='operand', line=1031)
W('32,3412', 0o56221, '', 'BDSU', 'DDV', kind='interp', line=1032)
W('32,3413', 0o03645, '', '', 'VDGVERT', kind='operand', line=1033)
W('32,3414', 0o02541, '', '', 'TAUROD', kind='operand', line=1034)
W('32,3415', 0o51515, '', 'PDVL', 'ABVAL', '                              (2)', kind='interp', line=1035)
W('32,3416', 0o01237, '', '', 'GDT/2', kind='operand', line=1036)
W('32,3417', 0o60471, '', 'DDV', 'SR2', kind='interp', line=1037)
W('32,3420', 0o05652, '', '', 'GSCALE', kind='operand', line=1038)
W('32,3421', 0o00025, '', 'STORE', '20D', kind='interp', line=1039)
W('32,3422', 0o77615, '', 'DAD', '', '                              (0)', kind='interp', line=1040)
W('32,3423', 0o45115, '', 'PDVL', 'CALL', '                              (2)', kind='interp', line=1041)
W('32,3424', 0o06520, '', '', 'UNITX', kind='operand', line=1042)
W('32,3425', 0o47661, '', '', 'CDU*NBSM', kind='operand', line=1043)
W('32,3426', 0o77641, '', 'DOT', kind='interp', line=1044)
W('32,3427', 0o00017, '', '', '14D', kind='operand', line=1045)
W('32,3430', 0o00027, '', 'STORE', '22D', kind='interp', line=1046)
W('32,3431', 0o45465, '', 'BDDV', 'STADR', '                              (0)', kind='interp', line=1047)
W('32,3432', 0o50313, '', 'STOVL', '/AFC/', kind='interp', line=1048)
W('32,3433', 0o03767, '', '', 'DELVROD', kind='operand', line=1049)
W('32,3434', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=1050)
W('32,3435', 0o26022, '', '', 'KPIP1', kind='operand', line=1051)
W('32,3436', 0o02631, '', '', 'VBIAS', kind='operand', line=1052)
W('32,3437', 0o65246, '', 'ABVAL', 'PDDL', '                              (2)', kind='interp', line=1053)
W('32,3440', 0o03762, '', '', 'THISTPIP', kind='operand', line=1054)
W('32,3441', 0o65225, '', 'DSU', 'PDDL', '                              (4)', kind='interp', line=1055)
W('32,3442', 0o03760, '', '', 'LASTTPIP', kind='operand', line=1056)
W('32,3443', 0o03762, '', '', 'THISTPIP', kind='operand', line=1057)
W('32,3444', 0o17760, '', 'STODL', 'LASTTPIP', '                              (2)', kind='interp', line=1058)
W('32,3445', 0o55271, '', 'DDV', 'BDDV', '                              (0)', kind='interp', line=1059)
W('32,3446', 0o25535, '', '', 'SHFTFACT', kind='operand', line=1060)
W('32,3447', 0o41325, '', 'PDDL', 'DMP', '                              (2)', kind='interp', line=1061)
W('32,3450', 0o03611, '', '', 'FWEIGHT', kind='operand', line=1062)
W('32,3451', 0o25534, '', '', 'BIT1H', kind='operand', line=1063)
W('32,3452', 0o56271, '', 'DDV', 'DDV', kind='interp', line=1064)
W('32,3453', 0o01245, '', '', 'MASS', kind='operand', line=1065)
W('32,3454', 0o22006, '', '', 'SCALEFAC', kind='operand', line=1066)
# Page 819
W('32,3455', 0o65215, '', 'DAD', 'PDDL', '                              (4)', kind='interp', line=1068)
W('32,3456', 0o00001, '', '', '0D', kind='operand', line=1069)
W('32,3457', 0o00025, '', '', '20D', kind='operand', line=1070)
W('32,3460', 0o45271, '', 'DDV', 'DSU', '                              (2)', kind='interp', line=1071)
W('32,3461', 0o00027, '', '', '22D', kind='operand', line=1072)
W('32,3462', 0o43205, '', 'DMP', 'DAD', kind='interp', line=1073)
W('32,3463', 0o02543, '', '', 'LAG/TAU', kind='operand', line=1074)
W('32,3464', 0o03464, '', '', '/AFC/', kind='operand', line=1075)
W('32,3465', 0o56325, '', 'PDDL', 'DDV', '                              (4)', kind='interp', line=1076)
W('32,3466', 0o02547, '', '', 'MAXFORCE', kind='operand', line=1077)
W('32,3467', 0o01245, '', '', 'MASS', kind='operand', line=1078)
W('32,3470', 0o56325, '', 'PDDL', 'DDV', '                              (6)', kind='interp', line=1079)
W('32,3471', 0o02545, '', '', 'MINFORCE', kind='operand', line=1080)
W('32,3472', 0o01245, '', '', 'MASS', kind='operand', line=1081)
W('32,3473', 0o44206, '', 'PUSH', 'BDSU', '                              (8)', kind='interp', line=1082)
W('32,3474', 0o00003, '', '', '2D', kind='operand', line=1083)
W('32,3475', 0o71240, '', 'BMN', 'DLOAD', '                              (6)', kind='interp', line=1084)
W('32,3476', 0o65504, '', '', 'AFCSPOT', kind='operand', line=1085)
W('32,3477', 0o41545, '', 'DLOAD', 'PUSH', '                              (6)', kind='interp', line=1086)
W('32,3500', 0o51021, '', 'BDSU', 'BPL', kind='interp', line=1087)
W('32,3501', 0o00003, '', '', '2D', kind='operand', line=1088)
W('32,3502', 0o65504, '', '', 'AFCSPOT', kind='operand', line=1089)
W('32,3503', 0o77745, '', 'DLOAD', '', '                              (4)', kind='interp', line=1090)
W('32,3504', 0o77745, 'AFCSPOT', 'DLOAD', '', '                              (2), (4), OR (6)', kind='interp', line=1091)
W('32,3505', 0o77601, '', 'SETPD', '', '                              (2)', kind='interp', line=1092)
W('32,3506', 0o00003, '', '', '2D', kind='operand', line=1093)
W('32,3507', 0o17464, '', 'STODL', '/AFC/', '                              (0)', kind='interp', line=1094)
W('32,3510', 0o77776, 'ITRPNT2', 'EXIT', kind='interp', line=1095)
W('32,3511', 0o52155, '', 'DXCH', 'MPAC', 'MPAC = MEASURED ACCELERATION.', line=1096)
W('32,3512', 0o04616, '', 'TC', 'BANKCALL', line=1097)
W('32,3513', 0o62221, '', 'CADR', 'THROTTLE +3', kind='data', line=1098)
W('32,3514', 0o06037, '', 'TC', 'INTPRET', line=1099)
W('32,3515', 0o77775, '', 'VLOAD', '', 'PICK UP UPDATED VELOCITY VECTOR.', kind='interp', line=1100)
W('32,3516', 0o00031, '', '', '24D', kind='operand', line=1101)
W('32,3517', 0o53352, 'VHORCOMP', 'VSL2', 'VAD', kind='interp', line=1102)
W('32,3520', 0o03734, '', '', 'DELVS', kind='operand', line=1103)
W('32,3521', 0o63342, '', 'VSR2', 'PDVL', kind='interp', line=1104)
W('32,3522', 0o03521, '', '', 'R', kind='operand', line=1105)
W('32,3523', 0o74256, '', 'UNIT', 'VXSC', kind='interp', line=1106)
W('32,3524', 0o03474, '', '', 'HDOTDISP', kind='operand', line=1107)
W('32,3525', 0o51372, '', 'VSL1', 'BVSU', kind='interp', line=1108)
W('32,3526', 0o77646, '', 'ABVAL', kind='interp', line=1109)
W('32,3527', 0o02263, '', 'STORE', 'VHORIZ', kind='interp', line=1110)
W('32,3530', 0o77776, '', 'EXIT', kind='interp', line=1111)
W('32,3531', 0o04616, '', 'TC', 'BANKCALL', 'PUT UP V06N60 DISPLAY BUT AVOID PHASCHNG', line=1112)
W('32,3532', 0o63463, '', 'CADR', 'DISPEXIT +3', kind='data', line=1113)

W('32,3533', 0o00001, 'BIT1H', 'OCT', '00001', kind='data', line=1115)
W('32,3534', 0o00000, 'SHFTFACT', '2DEC', '1 B-17', kind='data', line=1116)
W('32,3535', 0o04000, kind='data', line=1116)
# Page 820
W('32,3536', 0o00000, 'BIASFACT', '2DEC', '655.36 B-28', kind='data', line=1118)
W('32,3537', 0o01217, kind='data', line=1118)

# *********************************************************************************
# REDESIGNATOR TRAP
# *********************************************************************************

#   BANK 11
#   SETLOC F2DPS*11
#   BANK

#   COUNT* $$/F2DPS

W('11,2275', 0o56016, 'PITFALL', 'XCH', 'BANKRUPT', line=1130)
W('11,2276', 0o00006, '', 'EXTEND', line=1131)
W('11,2277', 0o22012, '', 'QXCH', 'QRUPT', line=1132)

W('11,2300', 0o05321, '', 'TC', 'CHECKMM', 'IF NOT IN P64, NO REASON TO CONTINUE', line=1134)
W('11,2301', 0o00100, '', 'DEC', '64', kind='data', line=1135)
W('11,2302', 0o15270, '', 'TCF', 'RESUME', line=1136)

W('11,2303', 0o00006, '', 'EXTEND', line=1138)
W('11,2304', 0o00031, '', 'READ', 'CHAN31', line=1139)
W('11,2305', 0o40000, '', 'COM', line=1140)
W('11,2306', 0o72373, '', 'MASK', 'ALL4BITS', line=1141)
W('11,2307', 0o55265, '', 'TS', 'ELVIRA', line=1142)
W('11,2310', 0o34752, '', 'CAF', 'TWO', line=1143)
W('11,2311', 0o55264, '', 'TS', 'ZERLINA', line=1144)
W('11,2312', 0o34756, '', 'CAF', 'FIVE', line=1145)
W('11,2313', 0o05173, '', 'TC', 'TWIDDLE', line=1146)
W('11,2314', 0o02321, '', 'ADRES', 'REDESMON', kind='data', line=1147)
W('11,2315', 0o15270, '', 'TCF', 'RESUME', line=1148)

# REDESIGNATOR MONITOR (INITIATED BY PITFALL)

W('11,2316', 0o55264, 'PREMON1', 'TS', 'ZERLINA', line=1152)
W('11,2317', 0o34757, 'PREMON2', 'CAF', 'SEVEN', line=1153)
W('11,2320', 0o05224, '', 'TC', 'VARDELAY', line=1154)
W('11,2321', 0o00006, 'REDESMON', 'EXTEND', line=1155)
W('11,2322', 0o00031, '', 'READ', '31', line=1156)
W('11,2323', 0o40000, '', 'COM', line=1157)
W('11,2324', 0o72373, '', 'MASK', 'ALL4BITS', line=1158)
W('11,2325', 0o57265, '', 'XCH', 'ELVIRA', line=1159)
W('11,2326', 0o54001, '', 'TS', 'L', line=1160)
W('11,2327', 0o11265, '', 'CCS', 'ELVIRA', 'DO ANY BITS APPEAR THIS PASS?', line=1161)
W('11,2330', 0o12317, '', 'TCF', 'PREMON2', 'Y:    CONTINUE MONITOR', line=1162)

W('11,2331', 0o10001, '', 'CCS', 'L', 'N:    ANY LAST PASS?', line=1164)
W('11,2332', 0o12341, '', 'TCF', "COUNT'EM", "      Y:      COUNT 'EM, RESET RUPT, TERMINATE", line=1165)
# Page 821
W('11,2333', 0o11264, '', 'CCS', 'ZERLINA', '      N:      HAS ZERLINA REACHED ZERO YET?', line=1167)
W('11,2334', 0o12316, '', 'TCF', 'PREMON1', '              N:      DIMINISH ZERLINA, CONTINUE', line=1168)
W('11,2335', 0o34740, 'RESETRPT', 'CAF', 'BIT12', '              Y:      RESET RUPT. TERMINATE', line=1169)
W('11,2336', 0o00006, '', 'EXTEND', line=1170)
W('11,2337', 0o05013, '', 'WOR', 'CHAN13', line=1171)
W('11,2340', 0o15261, '', 'TCF', 'TASKOVER', line=1172)

W('11,2341', 0o34737, "COUNT'EM", 'CAF', 'BIT13', 'ARE WE IN ATTITUDE-HOLD?', line=1174)
W('11,2342', 0o00006, '', 'EXTEND', line=1175)
W('11,2343', 0o02031, '', 'RAND', 'CHAN31', line=1176)
W('11,2344', 0o00006, '', 'EXTEND', line=1177)
W('11,2345', 0o12335, '', 'BZF', 'RESETRPT', 'YES: SKIP REDESIGNATION LOGIC.', line=1178)

W('11,2346', 0o30001, '', 'CA', 'L', 'NO.', line=1180)
W('11,2347', 0o74746, '', 'MASK', '-AZBIT', line=1181)
W('11,2350', 0o10000, '', 'CCS', 'A', line=1182)
W('11,2351', 0o42374, '-AZ', 'CS', 'AZEACH', line=1183)
W('11,2352', 0o27266, '', 'ADS', 'AZINCR1', line=1184)
W('11,2353', 0o30001, '', 'CA', 'L', line=1185)
W('11,2354', 0o74747, '', 'MASK', '+AZBIT', line=1186)
W('11,2355', 0o10000, '', 'CCS', 'A', line=1187)
W('11,2356', 0o32374, '+AZ', 'CA', 'AZEACH', line=1188)
W('11,2357', 0o27266, '', 'ADS', 'AZINCR1', line=1189)
W('11,2360', 0o30001, '', 'CA', 'L', line=1190)
W('11,2361', 0o74753, '', 'MASK', '-ELBIT', line=1191)
W('11,2362', 0o10000, '', 'CCS', 'A', line=1192)
W('11,2363', 0o42375, '-EL', 'CS', 'ELEACH', line=1193)
W('11,2364', 0o27267, '', 'ADS', 'ELINCR1', line=1194)
W('11,2365', 0o30001, '', 'CA', 'L', line=1195)
W('11,2366', 0o74752, '', 'MASK', '+ELBIT', line=1196)
W('11,2367', 0o10000, '', 'CCS', 'A', line=1197)
W('11,2370', 0o32375, '+EL', 'CA', 'ELEACH', line=1198)
W('11,2371', 0o27267, '', 'ADS', 'ELINCR1', line=1199)
W('11,2372', 0o12335, '', 'TCF', 'RESETRPT', line=1200)

# THESE EQUIVALENCES ARE BASED ON GSOP CHAPTER 4, REVISION 16 OF P64LM

S('+ELBIT', 'equals', 0o4752, line=1204)  # -PITCH
S('-ELBIT', 'equals', 0o4753, line=1205)  # +PITCH
S('+AZBIT', 'equals', 0o4747, line=1206)
S('-AZBIT', 'equals', 0o4746, line=1207)

# Page 822
W('11,2373', 0o00063, 'ALL4BITS', 'OCT', '00063', kind='data', line=1210)
W('11,2374', 0o01074, 'AZEACH', 'DEC', '.03491', '2 DEGREES', kind='data', line=1211)
W('11,2375', 0o00217, 'ELEACH', 'DEC', '.00873', '1/2 DEGREE', kind='data', line=1212)

# ****************************************************************
# R.O.D. TRAP
# ****************************************************************

#   BANK 20
#   SETLOC RODTRAP
#   BANK
#   COUNT* $$/F2DPS  # ************************

W('20,2115', 0o74745, 'DESCBITS', 'MASK', 'BIT7', 'COME HERE FROM MARKRUPT CODING WITH BIT', line=1223)
W('20,2116', 0o10000, '', 'CCS', 'A', '      7 OR 6 OF CHANNEL 16 IN A; BIT 7 MEANS', line=1224)
W('20,2117', 0o44752, '', 'CS', 'TWO', '      - RATE INCREMENT, BIT 6 + INCREMENT.', line=1225)
W('20,2120', 0o64753, '', 'AD', 'ONE', line=1226)
W('20,2121', 0o27746, '', 'ADS', 'RODCOUNT', line=1227)
W('20,2122', 0o15270, '', 'TCF', 'RESUME', 'TRAP IS RESET WHEN SWITCH IS RELEASED', line=1228)

#   BANK 31
#   SETLOC F2DPS*31
#   BANK

#   COUNT* $$/F2DPS

# ***********************************************************************************
# DOUBLE PRECISION ROOT FINDER SUBROUTINE (BY ALLAN KLUMPP)
# ***********************************************************************************
#
# N        N-1
# ROOTPSRS FINDS ONE ROOT OF THE POWER SERIES A X  + A   X    + ... + A X + A
# N      N-1              1     0
# USING NEWTON'S METHOD STARTING WITH AN INITIAL GUESS FOR THE ROOT.  THE ENTERING DATA MUST BE AS FOLLOWS:
# A       SP      LOC-3           ADRES FOR REFERENCING PWR COF TABL
# L       SP      N-1             N IS THE DEGREE OF THE POWER SERIES
# MPAC    DP      X               INITIAL GUESS FOR ROOT
#
# LOC-2N  DP      A(0)
# ...
# LOC     DP      A(N)
# LOC+2   SP      PRECROOT         PREC RQD OF ROOT (AS FRACT OF 1ST GUESS)
#
# Page 823
# THE DP RESULT IS LEFT IN MPAC UPON EXIT, AND A SP COUNT OF THE ITERATIONS TO CONVERGENCE IS LEFT IN MPAC+2.
# RETURN IS NORMALLY TO LOC(TC ROOTPSRS)+3.  IF ROOTPSRS FAILS TO CONVERGE TO IN 8 PASSES, RETURN IS TO LOC+1 AND
# OUTPUTS ARE NOT TO BE TRUSTED.
#
# PRECAUTION:  ROOTPSRS MAKES NO CHECKS FOR OVERFLOW OR FOR IMPROPER USAGE.  IMPROPER USAGE COULD
# PRECLUDE CONVERGENCE OR REQUIRE EXCESSIVE ITERATIONS.  AS A SPECIFIC EXAMPLE, ROOTPSRS FORMS A DERIVATIVE
# COEFFICIENT TABLE BY MULTIPLYING EACH A(I) BY I, WHERE I RANGES FROM 1 TO N.  IF AN ELEMENT OF THE DERIVATIVE
# COEFFICIENT TABLE = 1 OR >1 IN MAGNITUDE, ONLY THE EXCESS IS RETAINED.  ROOTPSRS MAY CONVERGE ON THE CORRECT
# ROOT NONETHELESS, BUT IT MAY TAKE AN EXCESSIVE NUMBER OF ITERATIONS.  THEREFORE THE USER SHOULD RECOGNIZE:
# 1.  USER'S RESPONSIBILITY TO ASSUR THAT I X A(I) < 1 IN MAGNITUDE FOR ALL I.
# 2.  USER'S RESPONSIBILITY TO ASSURE OVERFLOW WILL NOT OCCUR IN EVALUATING EITHER THE RESIDUAL OR THE DERIVATIVE
# POWER SERIES.  THIS OVERFLOW WOULD BE PRODUCED BY SUBROUTINE POWRSERS, CALLED BY ROOTPSRS, AND MIGHT NOT
# PRECLUDE EVENTUAL CONVERGENCE.
# 3.  AT PRESENT, ERASABLE LOCATIONS ARE RESERVED ONLY FOR N UP TO 5.  AN N IN EXCESS OF 5 WILL PRODUCE CHAOS.
# ALL ERASABLES USED BY ROOTPSRS ARE UNSWITCHED LOCATED IN THE REGION FROM MPAC-33 OCT TO MPAC+7.
# 4.  THE ITERATION COUNT RETURNED IN MPAC+2 MAY BE USED TO DETECT ABNORMAL PERFORMANCE.

# STORE ENTERING DATA, INITIALIZE ERASABLES
W('31,3553', 0o00006, 'ROOTPSRS', 'EXTEND', line=1272)
W('31,3554', 0o22132, '', 'QXCH', 'RETROOT', 'RETURN ADRES', line=1273)
W('31,3555', 0o54117, '', 'TS', 'PWRPTR', 'PWR TABLE POINTER', line=1274)
W('31,3556', 0o52160, '', 'DXCH', 'MPAC +3', 'PWR TABLE ADRES, N-1', line=1275)
W('31,3557', 0o33676, '', 'CA', 'DERTABLL', line=1276)
W('31,3560', 0o54141, '', 'TS', 'DERPTR', 'DER TABL POINTER', line=1277)
W('31,3561', 0o54161, '', 'TS', 'MPAC +5', 'DER TABL ADRES', line=1278)
W('31,3562', 0o10160, '', 'CCS', 'MPAC +4', 'NO POWER SERIES DEGREE 1 OR LESS', line=1279)
W('31,3563', 0o54162, '', 'TS', 'MPAC +6', 'N-2', line=1280)
W('31,3564', 0o34755, '', 'CA', 'ZERO', 'MODE USED AS ITERATION COUNTER.  MODE', line=1281)
W('31,3565', 0o54163, '', 'TS', 'MODE', "MUST BE POS SO ABS WON'T COMP MPAC+3 ETC.", line=1282)

# COMPUTE CRITERION TO STOP ITERATING
W('31,3566', 0o00006, '', 'EXTEND', line=1285)
W('31,3567', 0o30155, '', 'DCA', 'MPAC', 'FETCH ROOT GUESS, KEEPING IT IN MPAC', line=1286)
W('31,3570', 0o52127, '', 'DXCH', 'ROOTPS', 'AND IN ROOTPS', line=1287)
W('31,3571', 0o50157, '', 'INDEX', 'MPAC +3', 'PWR TABLE ADRES', line=1288)
W('31,3572', 0o30005, '', 'CA', '5', 'PRECROOT TO A', line=1289)
W('31,3573', 0o07307, '', 'TC', 'SHORTMP', 'YIELDS DP PRODUCT IN MPAC', line=1290)
W('31,3574', 0o04713, '', 'TC', 'USPRCADR', line=1291)
W('31,3575', 0o01226, '', 'CADR', 'ABS', 'YIELDS ABVAL OF CRITERION ON DX IN MPAC', kind='data', line=1292)
W('31,3576', 0o52155, '', 'DXCH', 'MPAC', line=1293)
W('31,3577', 0o52125, '', 'DXCH', 'DXCRIT', 'CRITERION', line=1294)

# SET UP DER COF TABL
# Page 824
W('31,3600', 0o00006, '', 'EXTEND', line=1298)
W('31,3601', 0o50117, '', 'INDEX', 'PWRPTR', line=1299)
W('31,3602', 0o30004, '', 'DCA', '3', line=1300)
W('31,3603', 0o52155, '', 'DXCH', 'MPAC', 'A(N) TO MPAC', line=1301)

W('31,3604', 0o30160, '', 'CA', 'MPAC +4', 'N-1 TO A', line=1303)

W('31,3605', 0o54140, 'DERCLOOP', 'TS', 'PWRCNT', 'LOOP COUNTER', line=1305)
W('31,3606', 0o64753, '', 'AD', 'ONE', line=1306)
W('31,3607', 0o07316, '', 'TC', 'DMPNSUB', 'YIELDS DERCOF = I X A(I) IN MPAC', line=1307)
W('31,3610', 0o00006, '', 'EXTEND', line=1308)
W('31,3611', 0o50117, '', 'INDEX', 'PWRPTR', line=1309)
W('31,3612', 0o30002, '', 'DCA', '1', line=1310)
W('31,3613', 0o52155, '', 'DXCH', 'MPAC', '(I-1) TO MPAC, FETCHING DERCOF', line=1311)
W('31,3614', 0o50141, '', 'INDEX', 'DERPTR', line=1312)
W('31,3615', 0o52004, '', 'DXCH', '3', 'DERCOF TO DER TABLE', line=1313)
W('31,3616', 0o44752, '', 'CS', 'TWO', line=1314)
W('31,3617', 0o26117, '', 'ADS', 'PWRPTR', 'DECREMENT PWR POINTER', line=1315)
W('31,3620', 0o44752, '', 'CS', 'TWO', line=1316)
W('31,3621', 0o26141, '', 'ADS', 'DERPTR', 'DECREMENT DER POINTER', line=1317)
W('31,3622', 0o10140, '', 'CCS', 'PWRCNT', line=1318)
W('31,3623', 0o13605, '', 'TCF', 'DERCLOOP', line=1319)

# CONVERGE ON ROOT
W('31,3624', 0o00006, 'ROOTLOOP', 'EXTEND', line=1322)
W('31,3625', 0o30127, '', 'DCA', 'ROOTPS', 'FETCH CURRENT ROOT', line=1323)
W('31,3626', 0o52155, '', 'DXCH', 'MPAC', 'LEAVE IN MPAC', line=1324)
W('31,3627', 0o00006, '', 'EXTEND', line=1325)
W('31,3630', 0o30162, '', 'DCA', 'MPAC +5', 'LOAD A, L WITH DER TABL ADRES, N-2', line=1326)
W('31,3631', 0o07215, '', 'TC', 'POWRSERS', 'YIELDS DERIVATIVE IN MPAC', line=1327)

W('31,3632', 0o00006, '', 'EXTEND', line=1329)
W('31,3633', 0o30127, '', 'DCA', 'ROOTPS', line=1330)
W('31,3634', 0o52155, '', 'DXCH', 'MPAC', 'CURRENT ROOT TO MPAC, FETCHING DERIVATIVE', line=1331)
W('31,3635', 0o52131, '', 'DXCH', 'BUF', 'LEAVE DERIVATIVE IN BUF AS DIVISOR', line=1332)
W('31,3636', 0o00006, '', 'EXTEND', line=1333)
W('31,3637', 0o30160, '', 'DCA', 'MPAC +3', 'LOAD A, L WITH PWR TABL ADRES, N-1', line=1334)
W('31,3640', 0o07215, '', 'TC', 'POWRSERS', 'YIELDS RESIDUAL IN MPAC', line=1335)

W('31,3641', 0o04713, '', 'TC', 'USPRCADR', line=1337)
W('31,3642', 0o00353, '', 'CADR', 'DDV/BDDV', 'YIELDS -DX IN MPAC', kind='data', line=1338)

W('31,3643', 0o00006, '', 'EXTEND', line=1340)
W('31,3644', 0o40155, '', 'DCS', 'MPAC', 'FETCH DX, LEAVING -DX IN MPAC', line=1341)
W('31,3645', 0o20127, '', 'DAS', 'ROOTPS', 'CORRECTED ROOT NOW IN ROOTPS', line=1342)

W('31,3646', 0o04713, '', 'TC', 'USPRCADR', line=1344)
W('31,3647', 0o01226, '', 'CADR', 'ABS', 'YIELDS ABS(DX) IN MPAC', kind='data', line=1345)
W('31,3650', 0o00006, '', 'EXTEND', line=1346)
# Page 825
W('31,3651', 0o40125, '', 'DCS', 'DXCRIT', line=1348)
W('31,3652', 0o20155, '', 'DAS', 'MPAC', 'ABS(DX)-ABS(DXCRIT) IN MPAC', line=1349)

W('31,3653', 0o30163, '', 'CA', 'MODE', line=1351)
W('31,3654', 0o74750, '', 'MASK', 'BIT4', 'KLUMPP SAYS GIVE UP AFTER EIGHT PASSES', line=1352)
W('31,3655', 0o10000, '', 'CCS', 'A', line=1353)
W('31,3656', 0o00132, 'BADROOT', 'TC', 'RETROOT', line=1354)

W('31,3657', 0o24163, '', 'INCR', 'MODE', 'INCREMENT ITERATION COUNTER', line=1356)
W('31,3660', 0o10154, '', 'CCS', 'MPAC', 'TEST HI ORDER DX', line=1357)
W('31,3661', 0o13624, '', 'TCF', 'ROOTLOOP', line=1358)
W('31,3662', 0o13664, '', 'TCF', 'TESTLODX', line=1359)
W('31,3663', 0o13670, '', 'TCF', 'ROOTSTOR', line=1360)
W('31,3664', 0o10155, 'TESTLODX', 'CCS', 'MPAC +1', 'TEST LO ORDER DX', line=1361)
W('31,3665', 0o13624, '', 'TCF', 'ROOTLOOP', line=1362)
W('31,3666', 0o13670, '', 'TCF', 'ROOTSTOR', line=1363)
W('31,3667', 0o13670, '', 'TCF', 'ROOTSTOR', line=1364)
W('31,3670', 0o52127, 'ROOTSTOR', 'DXCH', 'ROOTPS', line=1365)
W('31,3671', 0o52155, '', 'DXCH', 'MPAC', line=1366)
W('31,3672', 0o30163, '', 'CA', 'MODE', line=1367)
W('31,3673', 0o54156, '', 'TS', 'MPAC +2', 'STORE SP ITERATION COUNT IN MPAC+2', line=1368)
W('31,3674', 0o50132, '', 'INDEX', 'RETROOT', line=1369)
W('31,3675', 0o10002, '', 'TCF', '2', line=1370)

W('31,3676', 0o00147, 'DERTABLL', 'ADRES', 'DERCOFN -3', kind='data', line=1372)

# ****************************************************************************
# TRASHY LITTLE SUBROUTINES
# ****************************************************************************

W('31,3677', 0o51351, 'INTPRETX', 'INDEX', 'WCHPHASE', 'SET X1 ON THE WAY TO THE INTERPRETER', line=1378)
W('31,3700', 0o42452, '', 'CS', 'TARGTDEX', line=1379)
W('31,3701', 0o50120, '', 'INDEX', 'FIXLOC', line=1380)
W('31,3702', 0o54046, '', 'TS', 'X1', line=1381)
W('31,3703', 0o16037, '', 'TCF', 'INTPRET', line=1382)

W('31,3704', 0o31642, 'TDISPSET', 'CA', 'TTF/8', line=1384)
W('31,3705', 0o00006, '', 'EXTEND', line=1385)
W('31,3706', 0o74750, '', 'MP', 'TSCALINV', line=1386)
W('31,3707', 0o53476, '', 'DXCH', 'TTFDISP', line=1387)

W('31,3710', 0o35014, '', 'CA', 'EBANK5', 'TREDES BECOMES ZERO TWO PASSES', line=1389)
W('31,3711', 0o54003, '', 'TS', 'EBANK', '      BEFORE TCGFAPPR IS REACHED', line=1390)
#   EBANK= TCGFAPPR
W('31,3712', 0o31470, '', 'CA', 'TCGFAPPR', line=1392)
W('31,3713', 0o24006, '', 'INCR', 'BBANK', line=1393)
W('31,3714', 0o24006, '', 'INCR', 'BBANK', line=1394)
#   EBANK= TTF/8
# Page 826
W('31,3715', 0o61642, '', 'AD', 'TTF/8', line=1397)
W('31,3716', 0o00006, '', 'EXTEND', line=1398)
W('31,3717', 0o73751, '', 'MP', 'TREDESCL', line=1399)
W('31,3720', 0o63747, '', 'AD', '-DEC103', line=1400)
W('31,3721', 0o64735, '', 'AD', 'NEGMAX', line=1401)
W('31,3722', 0o54001, '', 'TS', 'L', line=1402)
W('31,3723', 0o40001, '', 'CS', 'L', line=1403)
W('31,3724', 0o60001, '', 'AD', 'L', line=1404)
W('31,3725', 0o63750, '', 'AD', '+DEC99', line=1405)
W('31,3726', 0o64733, '', 'AD', 'POSMAX', line=1406)
W('31,3727', 0o55666, '', 'TS', 'TREDES', line=1407)
W('31,3730', 0o41666, '', 'CS', 'TREDES', line=1408)
W('31,3731', 0o27666, '', 'ADS', 'TREDES', line=1409)
W('31,3732', 0o00002, '', 'TC', 'Q', line=1410)

W('31,3733', 0o05652, '1406P00', 'TC', 'POODOO', line=1412)
W('31,3734', 0o01406, '', 'OCT', '01406', kind='data', line=1413)
W('31,3735', 0o05567, '1406ALM', 'TC', 'ALARM', line=1414)
W('31,3736', 0o01406, '', 'OCT', '01406', kind='data', line=1415)
W('31,3737', 0o13443, '', 'TCF', 'RATESTOP', line=1416)

# *********************************************************************
# SPECIALIZED "PHASCHNG" SUBROUTINE
# *********************************************************************

#   EBANK= PHSNAME2
W('31,3740', 0o35007, 'FASTCHNG', 'CA', 'EBANK3', "SPECIALIZED 'PHASCHNG' ROUTINE", line=1423)
W('31,3741', 0o56003, '', 'XCH', 'EBANK', line=1424)
W('31,3742', 0o52002, '', 'DXCH', 'L', line=1425)
W('31,3743', 0o55442, '', 'TS', 'PHSNAME3', line=1426)
W('31,3744', 0o22003, '', 'LXCH', 'EBANK', line=1427)
#   EBANK= E2DPS
W('31,3745', 0o00000, '', 'TC', 'A', line=1429)

# *************************************************************************************
# PARAMETER TABLE INDIRECT ADDRESSES
# *************************************************************************************

S('RDG', 'equals', 0o2402, line=1435)
S('VDG', 'equals', 0o2410, line=1436)
S('ADG', 'equals', 0o2416, line=1437)
S('VDG2TTF', 'equals', 0o2424, line=1438)
S('ADG2TTF', 'equals', 0o2426, line=1439)
S('JDG2TTF', 'equals', 0o2430, line=1440)

# *************************************************************************************
# LUNAR LANDING CONSTANTS
# *************************************************************************************

# Page 827
W('31,3746', 0o01565, 'TABLTTFL', 'ADRES', 'TABLTTF +3', 'ADDRESS FOR REFERENCING TTF TABLE', kind='data', line=1447)
S('TTFSCALE', 'equals', 0o4740, line=1448)
S('TSCALINV', 'equals', 0o4750, line=1449)
W('31,3747', 0o77630, '-DEC103', 'DEC', '-103', kind='data', line=1450)
W('31,3750', 0o00143, '+DEC99', 'DEC', '+99', kind='data', line=1451)
W('31,3751', 0o75340, 'TREDESCL', 'DEC', '-.08', kind='data', line=1452)
W('31,3752', 0o00264, '180DEGS', 'DEC', '+180', kind='data', line=1453)
W('31,3753', 0o00056, '1/2DEG', 'DEC', '+.00278', kind='data', line=1454)
W('31,3754', 0o01542, 'PROJMAX', 'DEC', '.42262 B-3', "SIN(25')/8 TO COMPARE WITH PROJ", kind='data', line=1455)
W('31,3755', 0o01022, 'PROJMIN', 'DEC', '.25882 B-3', "SIN(15')/8 TO COMPARE WITH PROJ", kind='data', line=1456)
W('31,3756', 0o01477, 'V06N63', 'VN', '0663', 'P63', kind='data', line=1457)
W('31,3757', 0o01500, 'V06N64', 'VN', '0664', 'P64', kind='data', line=1458)
W('31,3760', 0o01474, 'V06N60', 'VN', '0660', 'P65, P66, P67', kind='data', line=1459)

#   BANK 22
#   SETLOC LANDCNST
#   BANK
#   COUNT* $$/F2DPS

W('22,3647', 0o00021, 'HIGHESTF', '2DEC', '4.34546769 B-12', kind='data', line=1466)
W('22,3650', 0o14161, kind='data', line=1466)
W('22,3651', 0o01440, 'GSCALE', '2DEC', '100 B-11', kind='data', line=1467)
W('22,3652', 0o00000, kind='data', line=1467)
W('22,3653', 0o14000, '3/8DP', '2DEC', '.375', kind='data', line=1468)
W('22,3654', 0o00000, kind='data', line=1468)
W('22,3655', 0o30000, '3/4DP', '2DEC', '.750', kind='data', line=1469)
W('22,3656', 0o00000, kind='data', line=1469)
W('22,3657', 0o77534, 'DEPRCRIT', '2DEC', '-.02 B-1', kind='data', line=1470)
W('22,3660', 0o45074, kind='data', line=1470)

# Page 828
# **************************************************************************
# **************************************************************************
