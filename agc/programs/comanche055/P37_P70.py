"""P37_P70.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P37_P70.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 890-933 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P37_P70', 'P37_P70.agc', 'Comanche055', pages='890-933')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P37_P70.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Jim Lawton <jim.lawton@gmail.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        890-933
# Mod history:  2009-05-11 JVL  Adapted from the Colossus249/ file
# of the same name, using Comanche055 page
# images.
# 2009-05-20 RSB  Added missing label V2T179.  Fixed POODOO -> POODOO.
# 2009-05-23 RSB  In RTD18, corrected a STOVL DELVLVC to
# STODL DELVLVC and a STODL 02D to STORE 02D.
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

# Page 890
#   BANK 31
#   SETLOC RTE1
#   BANK

#   EBANK= RTEDVD
#   COUNT 31/P37

# PROGRAM DESCRIPTION:  P37, RETURN TO EARTH
#
# DESCRIPTION
# A RETURN TO EARTH TRAJECTORY IS COMPUTED PROVIDED THE CSM IS OUTSIDE THE LUNAR SPHERE OF INFLUENCE AT THE
# TIME OF IGNITION.  INITIALLY A CONIC TRAJECTORY IS DETERMINED AND RESULTING IGNITION AND REENTRY PARAMETERS ARE
# DISPLAYED TO THE ASTRONAUT.  THEN IF THE ASTRONAUT SO DESIRES, A PRECISION TRAJECTORY IS DETERMINED WITH THE
# RESULTING IGNITION AND REENTRY PARAMETERS DISPLAYED.  UPON FINAL ACCEPTANCE BY THE ASTRONAUT, THE PROGRAM
# COMPUTES AND STORES THE TARGET PARAMETERS FOR RETURN TO EARTH FOR USE BY SPS PROGRAM (P40) OR RCS PROGRAM (P41).
#
# CALLING SEQUENCE
# L       TC      P37
#
# SUBROUTINES CALLED
# PREC100
# V2T100
# RTENCK2
# RTENCK3
# TIMERAD
# PARAM
# V2T100
# GAMDV10
# XT1LIM
# DVCALC
# RTENCK1
# INTSTALL
# INTEGRVS
# RTEVN
# RTEDISP
# TMRAD100
# AUGEKUGL
# LAT-LONG
# TMRAD100
# TIMERAD
# INVC100
# CSMPREC
# GETERAD
# TIMETHET
# P370ALRM
# VN1645
# POLY
#
# ERASABLE INITIALIZATION REQUIRED
# CSM STATE VECTOR
# Page 891
# NJETSFLG        NUMBER OF JETS IF THE RCS PROPULSION SYSTEM SELECTED    STATE FLAG      0=4 JETS  1=2 JETS
#
# ASTRONAUT INPUT
# SPRTETIG        TIME OF IGNITION (OVERLAYS TIG)                         DP      B28     CS
# VPRED           DESIRED CHANGE IN VELOCITY AT TIG(PROGRM COMPUTED IF 0) DP      B7      METERS/CS
# GAMMAEI         DESIRED FLIGHT PATH ANGLE AT REENTRY (COMPUTED IF 0)    DP      B0      REVS + ABOVE HORIZ.
# OPTION2         PROPULSION SYSTEM OPTION                                SP      B14     1=SPS, 2=RCS
#
# OUTPUT
# CONIC OR PRECISION TRAJECTORY DISPLAY
# VPRED           VELOCITY MAGNITUDE AT 400,000 FT. ENTRY ALTITUDE        DP      B7      METERS/CS
# T3TOT4          TRANSIT TIME TO 400,000 FT. ENTRY ALTITUDE              DP      B28     CS
# GAMMAEI         FLIGHT PATH ANGLE AT 400,00 FT. ENTRY ALTITUDE          DP      B0      REVS + ABOVE HORIZON
# DELVLVC         INITIAL VELOCITY CHANGE VECTOR IN LOCAL VERTICAL COORD. VECTOR  B7      METERS/CS
# LAT(SPL)        LATITUDE OF THE LANDING SITE                            DP      B0      REVS
# LNG(SPL)        LONGITUDE OF THE LANDING SITE                           DP      B0      REVS
# TARGETING COMPUTATION DISPLAY
# TIG             RECOMPUTED TIG BASED ON THRUST OPTION                   DP      B28     CS
# TTOGO           TIME FROM TIG                                           DP      B28     CS
# +MGA            POSITIVE MIDDLE GIMBAL ANGLE                            DP      B0      REVS -.02 IF REFSMFLG=0
# THRUST PROGRAM COMMUNICATION
# XDELVFLG        EXTERNAL DELTA V FLAG                                   STATE   FLAG    SET 0 FOR LAMBERT AIMPT
# NORMSW          LAMBERT AIMPT ROTATION SWITCH                           STATE   FLAG    SET 0 FOR NO ROTATION
# ECSTEER         CROSS PRODUCT STEERING CONSTANT                         SP      B2      SET 1
# RTARG           CONICALLY INTEGRATED REENTRY POSITION VECTOR            VECTOR  B29     METERS
# TPASS4          REENTRY TIME                                            DP      B28     CS

W('36,2466', 0o05412, 'P37', 'TC', 'PHASCHNG', 'P37 IS NOT RESTARTABLE', line=113)
W('36,2467', 0o00004, '', 'OCT', '4', kind='data', line=114)

W('36,2470', 0o06006, '', 'TC', 'INTPRET', line=116)
W('36,2471', 0o66170, '', 'AXT,1', 'SXA,1', kind='interp', line=117)
W('36,2472', 0o04000, '', 'OCT', '04000', kind='data', line=118)
W('36,2473', 0o03424, '', '', 'ECSTEER', kind='operand', line=119)
W('36,2474', 0o77745, '', 'DLOAD', kind='interp', line=120)
W('36,2475', 0o15335, '', '', 'ZEROVECS', kind='operand', line=121)
W('36,2476', 0o03767, '', 'STORE', 'VPRED', kind='interp', line=122)
W('36,2477', 0o03771, '', 'STORE', 'GAMMAEI', kind='interp', line=123)
W('36,2500', 0o77776, '', 'EXIT', kind='interp', line=124)
W('36,2501', 0o33246, '', 'CAF', 'V6N33RTE', 'INPUT TIG     STORED IN SPRTETIG', line=125)
W('36,2502', 0o03235, '', 'TCR', 'P370GOF', '              OVERLAYED WITH TIG', line=126)
W('36,2503', 0o12501, '', 'TCF', '-2', 'DISPLAY NEW DATA', line=127)
W('36,2504', 0o33252, '', 'CAF', 'V6N60RTE', 'INPUT REENTRY ANGLE IN GAMMAEI', line=128)
W('36,2505', 0o03211, '', 'TCR', 'P37GFRB1', '      AND DESIRED DELTA V IN RTEDVD', line=129)
W('36,2506', 0o12504, '', 'TCF', '-2', 'DISPLAY NEW DATA', line=130)
W('36,2507', 0o06006, 'RTE299', 'TC', 'INTPRET', line=131)
W('36,2510', 0o71331, '', 'SSP', 'DLOAD', kind='interp', line=132)
W('36,2511', 0o00122, '', '', 'OVFIND', kind='operand', line=133)
W('36,2512', 0o00000, '', '', '0', kind='operand', line=134)
W('36,2513', 0o03767, '', '', 'VPRED', kind='operand', line=135)
# Page 892
W('36,2514', 0o17632, '', 'STODL', 'RTEDVD', kind='interp', line=137)
W('36,2515', 0o03771, '', '', 'GAMMAEI', kind='operand', line=138)
W('36,2516', 0o17634, '', 'STODL', 'RTEGAM2D', kind='interp', line=139)
W('36,2517', 0o33514, '', '', '1RTEB13', kind='operand', line=140)
W('36,2520', 0o17735, '', 'STODL', 'CONICX1', kind='interp', line=141)
W('36,2521', 0o33620, '', '', 'C4RTE', kind='operand', line=142)
W('36,2522', 0o37652, '', 'STCALL', 'MAMAX1', kind='interp', line=143)
W('36,2523', 0o64450, '', '', 'INVC100', 'GET R(T1)/,V(T1)/,UR1/,UH/', kind='operand', line=144)
W('36,2524', 0o71214, '', 'CLEAR', 'DLOAD', kind='interp', line=145)
W('36,2525', 0o02662, '', '', 'SLOWFLG', kind='operand', line=146)
W('36,2526', 0o03632, '', '', 'RTEDVD', kind='operand', line=147)
W('36,2527', 0o51444, '', 'BPL', 'ABS', kind='interp', line=148)
W('36,2530', 0o74540, '', '', 'RTE317', kind='operand', line=149)
W('36,2531', 0o03632, '', 'STORE', 'RTEDVD', kind='interp', line=150)
W('36,2532', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=151)
W('36,2533', 0o03646, '', '', 'R(T1)', kind='operand', line=152)
W('36,2534', 0o33622, '', '', 'K1RTE', kind='operand', line=153)
W('36,2535', 0o43040, '', 'BMN', 'SET', kind='interp', line=154)
W('36,2536', 0o74540, '', '', 'RTE317', kind='operand', line=155)
W('36,2537', 0o02462, '', '', 'SLOWFLG', kind='operand', line=156)
W('36,2540', 0o77545, 'RTE317', 'DLOAD', 'EXIT', kind='interp', line=157)
W('36,2541', 0o03646, '', '', 'R(T1)', kind='operand', line=158)
W('36,2542', 0o07171, '', 'TC', 'POLY', line=159)
W('36,2543', 0o00002, '', 'DEC', '2', kind='data', line=160)
W('36,2544', 0o02544, '', '2DEC', '181000434. B-31', kind='data', line=161)
W('36,2545', 0o35436, kind='data', line=161)
W('36,2546', 0o14040, '', '2DEC', '1.50785145 B-2', kind='data', line=162)
W('36,2547', 0o05066, kind='data', line=162)
W('36,2550', 0o44052, '', '2DEC*', '-6.49993057 E-9 B27*', kind='data', line=163)
W('36,2551', 0o60030, kind='data', line=163)
W('36,2552', 0o26415, '', '2DEC*', '9.76938926 E-18 B56*', kind='data', line=164)
W('36,2553', 0o25057, kind='data', line=164)
W('36,2554', 0o06006, '', 'TC', 'INTPRET', line=165)
W('36,2555', 0o77752, '', 'SL1', kind='interp', line=166)
W('36,2556', 0o17654, '', 'STODL', 'MAMAX2', 'C0+C1*R+C2*R**2+C3*R**3=MAMAX2 B30', kind='interp', line=167)
W('36,2557', 0o33544, '', '', 'M9RTEB28', kind='operand', line=168)
W('36,2560', 0o17730, '', 'STODL', 'NN1A', kind='interp', line=169)
W('36,2561', 0o33624, '', '', 'K2RTE', kind='operand', line=170)
W('36,2562', 0o17636, 'RTE320', 'STODL', 'RCON', 'RCON=K2', kind='interp', line=171)
W('36,2563', 0o03634, '', '', 'RTEGAM2D', kind='operand', line=172)
W('36,2564', 0o44254, '', 'BZE', 'BDSU', kind='interp', line=173)
W('36,2565', 0o74574, '', '', 'RTE340', 'GOTORTE340 IF REENTRY ANGLE NOT INPUT', kind='operand', line=174)
W('36,2566', 0o33502, '', '', '1RTEB2', kind='operand', line=175)
W('36,2567', 0o71406, '', 'PUSH', 'COS', '                                      PL02D', kind='interp', line=176)
W('36,2570', 0o73525, '', 'PDDL', 'SIN', kind='interp', line=177)
W('36,2571', 0o45465, '', 'BDDV', 'STADR', '                                      PL00D', kind='interp', line=178)
W('36,2572', 0o40051, '', 'STCALL', 'X(T2)', 'X(T2)=COT(GAM2D)                      B0', kind='interp', line=179)
W('36,2573', 0o74607, '', '', 'RTE360', kind='operand', line=180)
W('36,2574', 0o45345, 'RTE340', 'DLOAD', 'DSU', kind='interp', line=181)
W('36,2575', 0o03646, '', '', 'R(T1)', kind='operand', line=182)
# Page 893
W('36,2576', 0o33622, '', '', 'K1RTE', kind='operand', line=184)
W('36,2577', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=185)
W('36,2600', 0o74604, '', '', 'RTE350', kind='operand', line=186)
W('36,2601', 0o33630, '', '', 'K4RTE', kind='operand', line=187)
W('36,2602', 0o37726, '', 'STCALL', 'X(T2)', 'X(T2)=K4', kind='interp', line=188)
W('36,2603', 0o74607, '', '', 'RTE360', kind='operand', line=189)
W('36,2604', 0o77745, 'RTE350', 'DLOAD', kind='interp', line=190)
W('36,2605', 0o33626, '', '', 'K3RTE', kind='operand', line=191)
W('36,2606', 0o03726, '', 'STORE', 'X(T2)', 'X(T2)=K3', kind='interp', line=192)
W('36,2607', 0o77624, 'RTE360', 'CALL', kind='interp', line=193)
W('36,2610', 0o65075, '', '', 'V2T100', kind='operand', line=194)
W('36,2611', 0o52054, '', 'BZE', 'GOTO', kind='interp', line=195)
W('36,2612', 0o74614, '', '', 'RTE367', kind='operand', line=196)
W('36,2613', 0o74776, '', '', 'RTEALRM', kind='operand', line=197)
W('36,2614', 0o77775, 'RTE367', 'VLOAD', kind='interp', line=198)
W('36,2615', 0o03640, '', '', 'R(T1)/', kind='operand', line=199)
W('36,2616', 0o16657, '', 'STODL', 'RVEC', kind='interp', line=200)
W('36,2617', 0o03636, '', '', 'RCON', kind='operand', line=201)
W('36,2620', 0o26760, '', 'STOVL', 'RDESIRED', kind='interp', line=202)
W('36,2621', 0o03700, '', '', 'V2(T1)/', kind='operand', line=203)
W('36,2622', 0o36746, '', 'STCALL', 'VVEC', kind='interp', line=204)
W('36,2623', 0o64277, '', '', 'TMRAD100', kind='operand', line=205)
W('36,2624', 0o77615, '', 'DAD', kind='interp', line=206)
W('36,2625', 0o03716, '', '', 'T1', kind='operand', line=207)
W('36,2626', 0o17736, '', 'STODL', 'T2', kind='interp', line=208)
W('36,2627', 0o03634, '', '', 'RTEGAM2D', kind='operand', line=209)
W('36,2630', 0o52054, '', 'BZE', 'GOTO', kind='interp', line=210)
W('36,2631', 0o74633, '', '', 'RTE369', kind='operand', line=211)
W('36,2632', 0o74655, '', '', 'RTE372', kind='operand', line=212)
W('36,2633', 0o51575, 'RTE369', 'VLOAD', 'ABVAL', kind='interp', line=213)
W('36,2634', 0o03710, '', '', 'V(T2)/', kind='operand', line=214)
W('36,2635', 0o77776, '', 'EXIT', kind='interp', line=215)
W('36,2636', 0o07171, '', 'TC', 'POLY', line=216)
W('36,2637', 0o00002, '', 'DEC', '2', kind='data', line=217)
W('36,2640', 0o00000, '', '2DEC', '0', kind='data', line=218)
W('36,2641', 0o00000, kind='data', line=218)
W('36,2642', 0o47021, '', '2DEC', '-4.8760771 E-2 B4', kind='data', line=219)
W('36,2643', 0o65002, kind='data', line=219)
W('36,2644', 0o35610, '', '2DEC', '4.5419476 E-4 B11', kind='data', line=220)
W('36,2645', 0o07722, kind='data', line=220)
W('36,2646', 0o63772, '', '2DEC', '-1.4317675 E-6 B18', kind='data', line=221)
W('36,2647', 0o63276, kind='data', line=221)

W('36,2650', 0o06006, '', 'TC', 'INTPRET', line=223)
W('36,2651', 0o77615, '', 'DAD', kind='interp', line=224)
W('36,2652', 0o01352, '', '', 'RTED1', kind='operand', line=225)
W('36,2653', 0o52052, '', 'SL3', 'GOTO', 'X(T2),=D1+D2V2+D3V2**2+D4V2**3', kind='interp', line=226)
W('36,2654', 0o74657, '', '', 'RTE373', kind='operand', line=227)
W('36,2655', 0o77745, 'RTE372', 'DLOAD', '', 'X(T2),=X(T2)', kind='interp', line=228)
W('36,2656', 0o03726, '', '', 'X(T2)', kind='operand', line=229)
W('36,2657', 0o41425, 'RTE373', 'DSU', 'PUSH', 'X(T2)ERR                              B0 PL02D', kind='interp', line=230)
# Page 894
W('36,2660', 0o03726, '', '', 'X(T2)', kind='operand', line=232)
W('36,2661', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=233)
W('36,2662', 0o03656, '', '', 'R(T2)/', '                                      B58', kind='operand', line=234)
W('36,2663', 0o36152, '', 'STCALL', 'ALPHAV', kind='interp', line=235)
W('36,2664', 0o26505, '', '', 'GETERAD', kind='operand', line=236)
W('36,2665', 0o77615, '', 'DAD', kind='interp', line=237)
W('36,2666', 0o33634, '', '', 'E3RTE', kind='operand', line=238)
W('36,2667', 0o45206, '', 'PUSH', 'DSU', 'RCON,=(E1/1+E2BETA11)**.5)+E3         B29 PL04D', kind='interp', line=239)
W('36,2670', 0o03636, '', '', 'RCON', kind='operand', line=240)
W('36,2671', 0o45246, '', 'ABS', 'DSU', kind='interp', line=241)
W('36,2672', 0o33600, '', '', 'EPC2RTE', kind='operand', line=242)
W('36,2673', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=243)
W('36,2674', 0o74676, '', '', 'RTE374', kind='operand', line=244)
W('36,2675', 0o74703, '', '', 'RTE375', kind='operand', line=245)
W('36,2676', 0o51545, 'RTE374', 'DLOAD', 'ABS', kind='interp', line=246)
W('36,2677', 0o00001, '', '', '00D', kind='operand', line=247)
W('36,2700', 0o50025, '', 'DSU', 'BMN', kind='interp', line=248)
W('36,2701', 0o33602, '', '', 'EPC3RTE', kind='operand', line=249)
W('36,2702', 0o74753, '', '', 'P37E', kind='operand', line=250)
W('36,2703', 0o43345, 'RTE375', 'DLOAD', 'DAD', kind='interp', line=251)
W('36,2704', 0o03730, '', '', 'NN1A', kind='operand', line=252)
W('36,2705', 0o33522, '', '', '1RTEB28', kind='operand', line=253)
W('36,2706', 0o67240, '', 'BMN', 'SLOAD', kind='interp', line=254)
W('36,2707', 0o74713, '', '', 'RTE380', kind='operand', line=255)
W('36,2710', 0o33562, '', '', 'OCT605', kind='operand', line=256)
W('36,2711', 0o77650, '', 'GOTO', kind='interp', line=257)
W('36,2712', 0o74776, '', '', 'RTEALRM', 'TOO MANY ITERATIONS', kind='operand', line=258)
W('36,2713', 0o03730, 'RTE380', 'STORE', 'NN1A', kind='interp', line=259)
W('36,2714', 0o53025, '', 'DSU', 'BZE', kind='interp', line=260)
W('36,2715', 0o33546, '', '', 'M8RTEB28', kind='operand', line=261)
W('36,2716', 0o74734, '', '', 'RTE385', kind='operand', line=262)
W('36,2717', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=263)
W('36,2720', 0o00001, '', '', '00D', kind='operand', line=264)
W('36,2721', 0o03666, '', '', 'DRCON', kind='operand', line=265)
W('36,2722', 0o65301, '', 'NORM', 'PDDL', 'X(T2)ERR-X(T2)ERR,=Z1                 PL06D', kind='interp', line=266)
W('36,2723', 0o00047, '', '', 'X1', kind='operand', line=267)
W('36,2724', 0o03670, '', '', "RPRE'", kind='operand', line=268)
W('36,2725', 0o56225, '', 'DSU', 'DDV', 'X(T2)PRI-X(T2)=Z2                     PL04D', kind='interp', line=269)
W('36,2726', 0o03726, '', '', 'X(T2)', kind='operand', line=270)
W('36,2727', 0o53605, '', 'DMP', 'SL*', 'DX(T2)=X(T2)ERR(Z2/Z1)', kind='interp', line=271)
W('36,2730', 0o00001, '', '', '00D', kind='operand', line=272)
W('36,2731', 0o20201, '', '', '0,1', kind='operand', line=273)
W('36,2732', 0o77650, '', 'GOTO', kind='interp', line=274)
W('36,2733', 0o74736, '', '', 'RTE390', kind='operand', line=275)
W('36,2734', 0o77745, 'RTE385', 'DLOAD', '', 'DX(T2)=X(T2)ERR', kind='interp', line=276)
W('36,2735', 0o00001, '', '', '00D', kind='operand', line=277)
W('36,2736', 0o14021, 'RTE390', 'STODL', '16D', 'DX(T2)                                PL02D', kind='interp', line=278)
W('36,2737', 0o77626, '', 'STADR', kind='interp', line=279)
W('36,2740', 0o60141, '', 'STODL', 'RCON', 'RCON=RCON,', kind='interp', line=280)
W('36,2741', 0o77600, '', 'BOV', kind='interp', line=281)
# Page 895
W('36,2742', 0o74607, '', '', 'RTE360', kind='operand', line=283)
W('36,2743', 0o17666, '', 'STODL', 'DRCON', 'X(T2)ERR,=X(T2)ERR', kind='interp', line=284)
W('36,2744', 0o03726, '', '', 'X(T2)', kind='operand', line=285)
W('36,2745', 0o17670, '', 'STODL', "RPRE'", 'X(T2)PRI=X(T2)', kind='interp', line=286)
W('36,2746', 0o00021, '', '', '16D', kind='operand', line=287)
W('36,2747', 0o77615, '', 'DAD', kind='interp', line=288)
W('36,2750', 0o03726, '', '', 'X(T2)', kind='operand', line=289)
W('36,2751', 0o37726, '', 'STCALL', 'X(T2)', 'X(T2)=X(T2)+DX(T2)', kind='interp', line=290)
W('36,2752', 0o74607, '', '', 'RTE360', 'REITERATE', kind='operand', line=291)
W('36,2753', 0o77624, 'P37E', 'CALL', '', 'DISPLAY CONIC SOLUTION', kind='interp', line=292)
W('36,2754', 0o75002, '', '', 'RTEVN', kind='operand', line=293)
W('36,2755', 0o41345, 'RTE505', 'DLOAD', 'DMP', kind='interp', line=294)
W('36,2756', 0o03720, '', '', 'PCON', kind='operand', line=295)
W('36,2757', 0o03754, '', '', 'BETA1', kind='operand', line=296)
W('36,2760', 0o53021, '', 'BDSU', 'BZE', kind='interp', line=297)
W('36,2761', 0o03636, '', '', 'RCON', kind='operand', line=298)
W('36,2762', 0o74770, '', '', 'RTE510', kind='operand', line=299)
W('36,2763', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=300)
W('36,2764', 0o74770, '', '', 'RTE510', kind='operand', line=301)
W('36,2765', 0o33502, '', '', '1RTEB2', kind='operand', line=302)
W('36,2766', 0o77650, '', 'GOTO', '', 'ENTRY NEAR APOGEE', kind='interp', line=303)
W('36,2767', 0o74772, '', '', 'RTE515', kind='operand', line=304)
W('36,2770', 0o57545, 'RTE510', 'DLOAD', 'DCOMP', 'ENTRY NEAR PERIGEE', kind='interp', line=305)
W('36,2771', 0o33502, '', '', '1RTEB2', kind='operand', line=306)
W('36,2772', 0o37761, 'RTE515', 'STCALL', 'PHI2', kind='interp', line=307)
W('36,2773', 0o64541, '', '', 'PREC100', 'PRECISION TRAJECTORY COMPUTATION', kind='operand', line=308)
W('36,2774', 0o77654, 'RTE625', 'BZE', kind='interp', line=309)
W('36,2775', 0o75030, '', '', 'P37G', kind='operand', line=310)
W('36,2776', 0o77624, 'RTEALRM', 'CALL', kind='interp', line=311)
W('36,2777', 0o64262, '', '', 'P370ALRM', kind='operand', line=312)
W('36,3000', 0o77776, '', 'EXIT', kind='interp', line=313)
W('36,3001', 0o12466, '', 'TCF', 'P37', 'RECYCLE AFTER ALARM DISPLAY', line=314)

# RETURN TO EARTH DISPLAY SUBROUTINE

W('36,3002', 0o45020, 'RTEVN', 'STQ', 'CALL', kind='interp', line=318)
W('36,3003', 0o03763, '', '', 'VNSTORE', kind='operand', line=319)
W('36,3004', 0o64316, '', '', 'RTEDISP', 'DISPLAY PREPARATION', kind='operand', line=320)
W('36,3005', 0o77776, '', 'EXIT', kind='interp', line=321)
W('36,3006', 0o33250, '', 'CAF', 'V6N61RTE', 'LATITUDE,LONGITUDE,BLANK', line=322)
W('36,3007', 0o03221, '', 'TCR', 'P370GOFR', '  IN LAT(SPL),LNG(SPL),-', line=323)
W('36,3010', 0o35015, '', 'CAF', 'FOUR', line=324)
W('36,3011', 0o03215, '', 'TCR', '37BLANK +1', line=325)
W('36,3012', 0o13017, '', 'TCF', '+5', line=326)
W('36,3013', 0o12466, '', 'TCF', 'P37', 'RECYCLE', line=327)
W('36,3014', 0o33251, '', 'CAF', 'V6N39RTE', 'T21 HRS,MIN,SEC IN T3TOT4', line=328)
W('36,3015', 0o03235, '', 'TCR', 'P370GOF', line=329)
W('36,3016', 0o12466, '', 'TCF', 'P37', 'RECYCLE', line=330)
W('36,3017', 0o33252, '', 'CAF', 'V6N60RTE', 'DISPLAY BLANK,V(T2),FPA2', line=331)
W('36,3020', 0o03211, '', 'TCR', 'P37GFRB1', '  IN -,VPRED,GAMMAEI', line=332)
# Page 896
W('36,3021', 0o12466, '', 'TCF', 'P37', 'RECYCLE', line=334)
W('36,3022', 0o33253, '', 'CAF', 'V6N81RTE', 'DISPLAY DELTA V (LV) IN DELVLVC', line=335)
W('36,3023', 0o03235, '', 'TCR', 'P370GOF', line=336)
W('36,3024', 0o12466, '', 'TCF', 'P37', 'RECYCLE', line=337)
W('36,3025', 0o06006, '', 'TCR', 'INTPRET', line=338)
W('36,3026', 0o77650, '', 'GOTO', kind='interp', line=339)
W('36,3027', 0o03763, '', '', 'VNSTORE', kind='operand', line=340)

# PRECISION DISPLAY, TARGETING COMPUTATION AND RTE END PROCESSING

W('36,3030', 0o77624, 'P37G', 'CALL', kind='interp', line=344)
W('36,3031', 0o75002, '', '', 'RTEVN', kind='operand', line=345)
W('36,3032', 0o77776, '', 'EXIT', kind='interp', line=346)
W('36,3033', 0o35023, 'P37N', 'CAF', 'SEVEN', line=347)
W('36,3034', 0o55131, '', 'TS', 'OPTION1', line=348)
W('36,3035', 0o35017, '', 'CAF', 'ONE', line=349)
W('36,3036', 0o55132, '', 'TS', 'OPTION2', line=350)
W('36,3037', 0o33247, '', 'CAF', 'V4N06RTE', 'DISPLAY RCS OR SPS OPTION  SPS ASSUMED', line=351)
W('36,3040', 0o03235, '', 'TCR', 'P370GOF', line=352)
W('36,3041', 0o13037, '', 'TCF', '-2', 'RECYCLE', line=353)
W('36,3042', 0o06006, '', 'TC', 'INTPRET', 'PROCEED', line=354)
W('36,3043', 0o67201, '', 'SETPD', 'SLOAD', kind='interp', line=355)
W('36,3044', 0o00001, '', '', '00D', kind='operand', line=356)
W('36,3045', 0o01133, '', '', 'OPTION2', kind='operand', line=357)
W('36,3046', 0o53025, '', 'DSU', 'BZE', kind='interp', line=358)
W('36,3047', 0o33514, '', '', '1RTEB13', kind='operand', line=359)
W('36,3050', 0o75057, '', '', 'P37Q', kind='operand', line=360)
W('36,3051', 0o60335, '', 'SLOAD', 'NORM', 'SPS', kind='interp', line=361)
W('36,3052', 0o00111, '', '', 'EMDOT', kind='operand', line=362)
W('36,3053', 0o00047, '', '', 'X1', kind='operand', line=363)
W('36,3054', 0o52125, '', 'PDDL', 'GOTO', kind='interp', line=364)
W('36,3055', 0o33552, '', '', 'VCSPS', kind='operand', line=365)
W('36,3056', 0o75070, '', '', 'P37T', kind='operand', line=366)
W('36,3057', 0o43145, 'P37Q', 'DLOAD', 'BON', 'RCS', kind='interp', line=367)
W('36,3060', 0o33556, '', '', 'MDOTRCS', kind='operand', line=368)
W('36,3061', 0o00700, '', '', 'NJETSFLG', kind='operand', line=369)
W('36,3062', 0o75064, '', '', 'P37R', kind='operand', line=370)
W('36,3063', 0o77752, '', 'SL1', kind='interp', line=371)
W('36,3064', 0o77752, 'P37R', 'SL1', kind='interp', line=372)
W('36,3065', 0o65301, '', 'NORM', 'PDDL', kind='interp', line=373)
W('36,3066', 0o00047, '', '', 'X1', kind='operand', line=374)
W('36,3067', 0o33554, '', '', 'VCRCS', kind='operand', line=375)
W('36,3070', 0o56325, 'P37T', 'PDDL', 'DDV', 'DV/VC                 B7 -B5 = B2     PL02D', kind='interp', line=376)
W('36,3071', 0o03706, '', '', 'DV', kind='operand', line=377)
W('36,3072', 0o77776, '', 'EXIT', kind='interp', line=378)
W('36,3073', 0o07171, '', 'TC', 'POLY', line=379)
W('36,3074', 0o00001, '', 'DEC', '1', kind='data', line=380)
W('36,3075', 0o00001, '', '2DEC', '5.66240507 E-4 B-3', kind='data', line=381)
W('36,3076', 0o05070, kind='data', line=381)
W('36,3077', 0o17527, '', '2DEC', '9.79487897 E-1 B-1', kind='data', line=382)
W('36,3100', 0o36700, kind='data', line=382)
# Page 897
W('36,3101', 0o47114, '', '2DEC', '-.388281955 B1', kind='data', line=384)
W('36,3102', 0o70670, kind='data', line=384)
W('36,3103', 0o06006, '', 'TC', 'INTPRET', line=385)
W('36,3104', 0o67206, '', 'PUSH', 'SLOAD', '(1-E)**(-DV/VC)=A             B3      PL04D', kind='interp', line=386)
W('36,3105', 0o03076, '', '', 'WEIGHT/G', kind='operand', line=387)
W('36,3106', 0o56205, '', 'DMP', 'DDV', 'DTB=(M0/MDOT)A        B16+B3-B3=B16   PL00D', kind='interp', line=388)
W('36,3107', 0o41257, '', 'SL*', 'DMP', kind='interp', line=389)
W('36,3110', 0o20165, '', '', '0 -12D,1', kind='operand', line=390)
W('36,3111', 0o33560, '', '', 'CSUBT', kind='operand', line=391)
W('36,3112', 0o77621, '', 'BDSU', kind='interp', line=392)
W('36,3113', 0o03716, '', '', 'T1', kind='operand', line=393)
W('36,3114', 0o03413, '', 'STORE', 'TIG', 'TIG=T1-CT*DTB                 B28', kind='interp', line=394)
W('36,3115', 0o77776, '', 'EXIT', kind='interp', line=395)
W('36,3116', 0o33246, '', 'CAF', 'V6N33RTE', 'DISPLAY BIASED TIG', line=396)
W('36,3117', 0o03235, '', 'TCR', 'P370GOF', line=397)
W('36,3120', 0o13116, '', 'TCF', '-2', line=398)
W('36,3121', 0o35021, '', 'CAF', 'ZERO', line=399)
W('36,3122', 0o55125, '', 'TS', 'VHFCNT', line=400)
W('36,3123', 0o55126, '', 'TS', 'TRKMKCNT', line=401)
W('36,3124', 0o06006, '', 'TC', 'INTPRET', line=402)
W('36,3125', 0o77624, '', 'CALL', '', 'CONICALLY INTEGRATE FROM R1,V1 OVER T12', kind='interp', line=403)
W('36,3126', 0o63700, '', '', 'RTENCK1', kind='operand', line=404)
W('36,3127', 0o53575, '', 'VLOAD', 'UNIT', '                                      PL00D', kind='interp', line=405)
W('36,3130', 0o03656, '', '', 'R(T2)/', kind='operand', line=406)
W('36,3131', 0o74315, '', 'PDVL', 'VXSC', 'UR2                           B1      PL06D', kind='interp', line=407)
W('36,3132', 0o03740, '', '', 'UR1/', kind='operand', line=408)
W('36,3133', 0o33564, '', '', 'MCOS7.5', kind='operand', line=409)
W('36,3134', 0o74315, '', 'PDVL', 'VXSC', '-UR1(COS7.5)                  B1      PL12D', kind='interp', line=410)
W('36,3135', 0o03746, '', '', 'UH/', kind='operand', line=411)
W('36,3136', 0o33566, '', '', 'MSIN7.5', kind='operand', line=412)
W('36,3137', 0o50255, '', 'VAD', 'DOT', 'K/=-UR1(COS7.5)-UH(SIN7.5)    B2      PL00D', kind='interp', line=413)
W('36,3140', 0o50015, '', 'DAD', 'BMN', kind='interp', line=414)
W('36,3141', 0o33570, '', '', 'MCOS22.5', kind='operand', line=415)
W('36,3142', 0o75167, '', '', 'P37W', kind='operand', line=416)
W('36,3143', 0o50375, '', 'VLOAD', 'DOT', 'K/ . UR2 GR COS22.5', kind='interp', line=417)
W('36,3144', 0o03746, '', '', 'UH/', kind='operand', line=418)
W('36,3145', 0o03656, '', '', 'R(T2)/', kind='operand', line=419)
W('36,3146', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=420)
W('36,3147', 0o75153, '', '', 'P37U', kind='operand', line=421)
W('36,3150', 0o33572, '', '', 'THETA165', kind='operand', line=422)
W('36,3151', 0o52006, '', 'PUSH', 'GOTO', kind='interp', line=423)
W('36,3152', 0o75155, '', '', 'P37V', kind='operand', line=424)
W('36,3153', 0o41545, 'P37U', 'DLOAD', 'PUSH', kind='interp', line=425)
W('36,3154', 0o33574, '', '', 'THETA210', kind='operand', line=426)
W('36,3155', 0o77756, 'P37V', 'SIN', kind='interp', line=427)
W('36,3156', 0o16732, '', 'STODL', 'SNTH', kind='interp', line=428)
W('36,3157', 0o43146, '', 'COS', 'CLEAR', kind='interp', line=429)
W('36,3160', 0o03666, '', '', 'RVSW', kind='operand', line=430)
W('36,3161', 0o26734, '', 'STOVL', 'CSTH', kind='interp', line=431)
W('36,3162', 0o03640, '', '', 'R(T1)/', kind='operand', line=432)
# Page 898
W('36,3163', 0o26657, '', 'STOVL', 'RVEC', kind='interp', line=434)
W('36,3164', 0o03700, '', '', 'V2(T1)/', kind='operand', line=435)
W('36,3165', 0o36746, '', 'STCALL', 'VVEC', kind='interp', line=436)
W('36,3166', 0o24744, '', '', 'TIMETHET', kind='operand', line=437)
W('36,3167', 0o43014, 'P37W', 'CLEAR', 'CLEAR', kind='interp', line=438)
W('36,3170', 0o01267, '', '', 'XDELVFLG', kind='operand', line=439)
W('36,3171', 0o03665, '', '', 'NORMSW', kind='operand', line=440)
W('36,3172', 0o77214, '', 'SET', 'VLOAD', kind='interp', line=441)
W('36,3173', 0o01071, '', '', 'FINALFLG', kind='operand', line=442)
W('36,3174', 0o77626, '', 'STADR', kind='interp', line=443)
W('36,3175', 0o60362, '', 'STODL', 'RTARG', kind='interp', line=444)
W('36,3176', 0o00037, '', '', 'T', kind='operand', line=445)
W('36,3177', 0o77615, '', 'DAD', kind='interp', line=446)
W('36,3200', 0o03716, '', '', 'T1', kind='operand', line=447)
W('36,3201', 0o27656, '', 'STOVL', 'TPASS4', kind='interp', line=448)
W('36,3202', 0o03700, '', '', 'V2(T1)/', kind='operand', line=449)
W('36,3203', 0o77651, '', 'VSU', kind='interp', line=450)
W('36,3204', 0o03672, '', '', 'V(T1)/', kind='operand', line=451)
W('36,3205', 0o37646, '', 'STCALL', 'DELVSIN', kind='interp', line=452)
W('36,3206', 0o73002, '', '', 'VN1645', kind='operand', line=453)
W('36,3207', 0o77650, '', 'GOTO', kind='interp', line=454)
W('36,3210', 0o75167, '', '', 'P37W', kind='operand', line=455)

# SUBROUTINE TO GO TO GOFLASHR AND BLANK R1

W('36,3211', 0o00006, 'P37GFRB1', 'EXTEND', line=459)
W('36,3212', 0o23762, '', 'QXCH', 'SPRTEX', line=460)
W('36,3213', 0o03221, '', 'TCR', 'P370GOFR', line=461)
W('36,3214', 0o35017, '37BLANK', 'CAF', 'ONE', line=462)
W('36,3215', 0o05526, '', 'TCR', 'BLANKET', line=463)
W('36,3216', 0o15217, '', 'TCF', 'ENDOFJOB', line=464)
W('36,3217', 0o01762, '', 'TC', 'SPRTEX', 'RECYCLE', line=465)
W('36,3220', 0o13244, '', 'TCF', 'P37PROC', 'PROCEED', line=466)

# SUBROUTINE TO GO TO GOFLASHR

W('36,3221', 0o00006, 'P370GOFR', 'EXTEND', line=470)
W('36,3222', 0o23733, '', 'QXCH', 'RTENCKEX', line=471)
W('36,3223', 0o04662, '', 'TCR', 'BANKCALL', line=472)
W('36,3224', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=473)
W('36,3225', 0o14106, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=474)
W('36,3226', 0o13231, '', 'TCF', '+3', line=475)
W('36,3227', 0o13233, '', 'TCF', '+4', line=476)
W('36,3230', 0o01733, '', 'TC', 'RTENCKEX', 'IMMEDIATE RETURN', line=477)
W('36,3231', 0o51733, '', 'INDEX', 'RTENCKEX', 'PROCEED', line=478)
W('36,3232', 0o10004, '', 'TCF', '0 +4', line=479)
W('36,3233', 0o51733, '', 'INDEX', 'RTENCKEX', 'RECYCLE', line=480)
W('36,3234', 0o10003, '', 'TCF', '0 +3', line=481)

# SUBROUTINE TO GO TO GOFLASH

# Page 899
W('36,3235', 0o00006, 'P370GOF', 'EXTEND', line=486)
W('36,3236', 0o23762, '', 'QXCH', 'SPRTEX', line=487)
W('36,3237', 0o04662, '', 'TCR', 'BANKCALL', line=488)
W('36,3240', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=489)
W('36,3241', 0o14106, '', 'TCF', 'GOTOPOOH', line=490)
W('36,3242', 0o13244, '', 'TCF', '+2', line=491)
W('36,3243', 0o01762, '', 'TC', 'SPRTEX', line=492)
W('36,3244', 0o51762, 'P37PROC', 'INDEX', 'SPRTEX', line=493)
W('36,3245', 0o10001, '', 'TCF', '0 +1', line=494)
W('36,3246', 0o01441, 'V6N33RTE', 'VN', '0633', kind='data', line=495)
W('36,3247', 0o01006, 'V4N06RTE', 'VN', '0406', kind='data', line=496)
W('36,3250', 0o01475, 'V6N61RTE', 'VN', '0661', kind='data', line=497)
W('36,3251', 0o01447, 'V6N39RTE', 'VN', '0639', kind='data', line=498)
W('36,3252', 0o01474, 'V6N60RTE', 'VN', '0660', kind='data', line=499)
W('36,3253', 0o01521, 'V6N81RTE', 'VN', '0681', kind='data', line=500)
#   BANK 32
#   SETLOC RTE
#   BANK
#   COUNT 32/RTE

# Page 900
# ALARM DISPLAY SUBROUTINE

W('32,2262', 0o77420, 'P370ALRM', 'STQ', 'EXIT', kind='interp', line=509)
W('32,2263', 0o03762, '', '', 'SPRTEX', kind='operand', line=510)
W('32,2264', 0o30154, '', 'CA', 'MPAC', line=511)
W('32,2265', 0o05764, '', 'TC', 'VARALARM', line=512)
W('32,2266', 0o32276, '', 'CAF', 'V5N09RTE', line=513)
W('32,2267', 0o04662, '', 'TC', 'BANKCALL', line=514)
W('32,2270', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=515)
W('32,2271', 0o14106, '', 'TCF', 'GOTOPOOH', line=516)
W('32,2272', 0o12266, '', 'TCF', '-4', line=517)
W('32,2273', 0o06006, '', 'TC', 'INTPRET', line=518)
W('32,2274', 0o77650, '', 'GOTO', kind='interp', line=519)
W('32,2275', 0o03762, '', '', 'SPRTEX', kind='operand', line=520)
W('32,2276', 0o01211, 'V5N09RTE', 'VN', '0509', kind='data', line=521)

# Page 901
# TIME RADIUS CALLING SUBROUTINE
#
# INPUT
# RVEC            INITIAL POSITION VECTOR                                 VECTOR  B29     METERS
# VVEC            INITIAL VELOCITY VECTOR                                 VECTOR  B7      METERS/CS
# RDESIRED        FINAL RADIUS FOR WHICH TRANSFER TIME IS TO BE COMPUTED  DP      B29     METERS
# CONICX1         X1 SETTING FOR CONIC SUBROUTINES  -2=EARTH              SP      B14
#
# OUTPUT
# R(T2)/          FINAL POSITION VECTOR                                   VECTOR  B29     METERS
# V(T2)/          FINAL VELOCITY VECTOR                                   VECTOR  B7      METERS/CS
# T12             TRANSFER TIME TO FINAL RADIUS                           DP      B28     CS

W('32,2277', 0o43020, 'TMRAD100', 'STQ', 'CLEAR', kind='interp', line=537)
W('32,2300', 0o03733, '', '', 'RTENCKEX', kind='operand', line=538)
W('32,2301', 0o03666, '', '', 'RVSW', kind='operand', line=539)
W('32,2302', 0o67164, '', 'AXC,2', 'SXA,2', kind='interp', line=540)
W('32,2303', 0o20000, '', 'OCT', '20000', kind='data', line=541)
W('32,2304', 0o02756, '', '', 'SGNRDOT', kind='operand', line=542)
W('32,2305', 0o45140, '', 'LXC,1', 'CALL', kind='interp', line=543)
W('32,2306', 0o03734, '', '', 'CONICX1', kind='operand', line=544)
W('32,2307', 0o25556, '', '', 'TIMERAD', kind='operand', line=545)
W('32,2310', 0o27710, '', 'STOVL', 'V(T2)/ PL00D', kind='interp', line=546)
W('32,2311', 0o77626, '', 'STADR', kind='interp', line=547)
W('32,2312', 0o60121, '', 'STODL', 'R(T2)/', kind='interp', line=548)
W('32,2313', 0o00037, '', '', 'T', kind='operand', line=549)
W('32,2314', 0o37724, '', 'STCALL', 'T12', kind='interp', line=550)
W('32,2315', 0o03733, '', '', 'RTENCKEX', kind='operand', line=551)

# Page 902
# DISPLAY CALCULATION SUBROUTINE
#
# DESCRIPTION
# OUTPUT FOR DISPLAY IS CONVERTED TO PROPER UNITS AND PLACED IN OUTPUT STORAGE REGISTERS.  LANDING SITE
# COMPUTATION FOR DETERMINING LANDING SITE LATITUDE AND LONGITUDE IS INCLUDED IN THE ROUTINE.
#
# CALLING SEQUENCE
# L       CALL
# L+1             RTEDISP
#
# SUBROUTINES CALLED
# TMRAD100
# AUGEKUGL
# LAT-LONG
#
# ERASABLE INITIALIZATION REQUIRED
# PUSHLIST
# NONE
# MPAC
# NONE
# OTHER
# R(T2)/          FINAL POSITION VECTOR                                   VECTOR  B29     METERS
# V(T2)/          FINAL VELOCITY VECTOR                                   VECTOR  B7      METERS/CS
# T2              FINAL TIME                                              DP      B28     CS
# V2(T1)/         POST IMPULSE INITIAL VELOCITY VECTOR                    VECTOR  B7      METERS/CS
# V(T1)/          INITIAL VELOCITY VECTOR                                 VECTOR  B7
# UR1/            UNIT INITIAL VECTOR                                     VECTOR  B1
# UH/             UNIT HORIZONTAL VECTOR                                  VECTOR  B1
#
# OUTPUT
# VPRED           VELOCITY MAGNITUDE AT 400,000 FT. ENTRY ALTITUDE        DP      B7      METERS/CS
# T3TOT4          TRANSIT TIME TO 400,000 FT. ENTRY ALTITUDE              DP      B28     CS
# GAMMAEI         FLIGHT PATH ANGLE AT 400,000 FT. ENTRY ALTITUDE         DP      B0      REVS + ABOVE HORIZ
# DELVLVC         INITIAL VELOCITY CHANGE VECTOR IN LOCAL VERTICAL COORD. VECTOR  B7      METERS/CS
# LAT(SPL)        LATITUDE OF THE LANDING SITE                            DP      B0      REVS
# LNG(SPL)        LONGITUDE OF THE LANDING SITE                           DP      B0      REVS

W('32,2316', 0o77220, 'RTEDISP', 'STQ', 'VLOAD', 'DISPLAY', kind='interp', line=591)
W('32,2317', 0o03762, '', '', 'SPRTEX', kind='operand', line=592)
W('32,2320', 0o03710, '', '', 'V(T2)/', kind='operand', line=593)
W('32,2321', 0o65256, '', 'UNIT', 'PDDL', kind='interp', line=594)
W('32,2322', 0o00045, '', '', '36D', kind='operand', line=595)
W('32,2323', 0o17767, '', 'STODL', 'VPRED', 'V(T2)', kind='interp', line=596)
W('32,2324', 0o03736, '', '', 'T2', kind='operand', line=597)
W('32,2325', 0o77625, '', 'DSU', kind='interp', line=598)
W('32,2326', 0o03413, '', '', 'SPRTETIG', kind='operand', line=599)
W('32,2327', 0o26641, '', 'STOVL', 'T3TOT4', 'T21', kind='interp', line=600)
W('32,2330', 0o03656, '', '', 'R(T2)/', kind='operand', line=601)
W('32,2331', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=602)
W('32,2332', 0o77752, '', 'SL1', kind='interp', line=603)

# Page 903
W('32,2333', 0o44326, '', 'ARCCOS', 'BDSU', kind='interp', line=606)
W('32,2334', 0o33502, '', '', '1RTEB2', kind='operand', line=607)
W('32,2335', 0o27771, '', 'STOVL', 'GAMMAEI', 'FLIGHT PATH ANGLE T2', kind='interp', line=608)
W('32,2336', 0o03700, '', '', 'V2(T1)/', kind='operand', line=609)
W('32,2337', 0o41451, '', 'VSU', 'PUSH', kind='interp', line=610)
W('32,2340', 0o03672, '', '', 'V(T1)/', kind='operand', line=611)
W('32,2341', 0o57441, '', 'DOT', 'DCOMP', kind='interp', line=612)
W('32,2342', 0o03740, '', '', 'UR1/', kind='operand', line=613)
W('32,2343', 0o41515, '', 'PDVL', 'PUSH', kind='interp', line=614)
W('32,2344', 0o63345, '', 'DLOAD', 'PDVL', kind='interp', line=615)
W('32,2345', 0o33524, '', '', 'ZERORTE', kind='operand', line=616)
W('32,2346', 0o55441, '', 'DOT', 'VDEF', kind='interp', line=617)
W('32,2347', 0o03746, '', '', 'UH/', kind='operand', line=618)
W('32,2350', 0o77772, '', 'VSL1', kind='interp', line=619)
W('32,2351', 0o17405, '', 'STODL', 'DELVLVC', kind='interp', line=620)
W('32,2352', 0o03405, '', '', 'DELVLVC', kind='operand', line=621)
W('32,2353', 0o57414, '', 'BOFF', 'DCOMP', kind='interp', line=622)
W('32,2354', 0o02741, '', '', 'RETROFLG', kind='operand', line=623)
W('32,2355', 0o64357, '', '', 'RTD18', kind='operand', line=624)
W('32,2356', 0o03405, '', 'STORE', 'DELVLVC', 'NEGATE X COMPONENT, RETROGRADE', kind='interp', line=625)
W('32,2357', 0o51575, 'RTD18', 'VLOAD', 'ABVAL', kind='interp', line=626)
W('32,2360', 0o03405, '', '', 'DELVLVC', kind='operand', line=627)
W('32,2361', 0o27773, '', 'STOVL', 'VGDISP', kind='interp', line=628)
W('32,2362', 0o03656, '', '', 'R(T2)/', kind='operand', line=629)
W('32,2363', 0o02657, '', 'STORE', 'RVEC', '***** LANDING SITE COMPUTATION *****', kind='interp', line=630)
W('32,2364', 0o45246, '', 'ABVAL', 'DSU', kind='interp', line=631)
W('32,2365', 0o33550, '', '', '30480RTE', kind='operand', line=632)
W('32,2366', 0o26760, '', 'STOVL', 'RDESIRED', kind='interp', line=633)
W('32,2367', 0o03710, '', '', 'V(T2)/', kind='operand', line=634)
W('32,2370', 0o36746, '', 'STCALL', 'VVEC', kind='interp', line=635)
W('32,2371', 0o64277, '', '', 'TMRAD100', 'R3,V3,T23 FROM TIMERAD', kind='operand', line=636)
W('32,2372', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=637)
W('32,2373', 0o03656, '', '', 'R(T2)/', kind='operand', line=638)
W('32,2374', 0o53515, '', 'PDVL', 'UNIT', 'UR3                                   PL06D', kind='interp', line=639)
W('32,2375', 0o03710, '', '', 'V(T2)/', kind='operand', line=640)
W('32,2376', 0o72441, '', 'DOT', 'SL1', 'GAMMAE=ARCSIN(UR3 . UV3)              PL00D', kind='interp', line=641)
W('32,2377', 0o65336, '', 'ARCSIN', 'PDDL', 'V(T3)                                 PL02D', kind='interp', line=642)
W('32,2400', 0o00045, '', '', '36D', kind='operand', line=643)
W('32,2401', 0o51525, '', 'PDDL', 'ABS', kind='interp', line=644)
W('32,2402', 0o45006, '', 'PUSH', 'CALL', '/GAMMAE/                              PL04D', kind='interp', line=645)
W('32,2403', 0o64075, '', '', 'AUGEKUGL', 'PHIE                                  PL06D', kind='operand', line=646)
W('32,2404', 0o43215, '', 'DAD', 'DAD', kind='interp', line=647)
W('32,2405', 0o03724, '', '', 'T12', 'T23', kind='operand', line=648)
W('32,2406', 0o03736, '', '', 'T2', kind='operand', line=649)
W('32,2407', 0o00003, '', 'STORE', '02D', 'T(LS)=T2&T23&TE', kind='interp', line=650)
W('32,2410', 0o53135, '', 'SLOAD', 'BZE', kind='interp', line=651)
W('32,2411', 0o03377, '', '', 'P37RANGE', kind='operand', line=652)
W('32,2412', 0o64414, '', '', 'RTD22', kind='operand', line=653)
W('32,2413', 0o00005, '', 'STORE', '04D', 'OVERRIDE RANGE (PCR 261)', kind='interp', line=654)
W('32,2414', 0o73545, 'RTD22', 'DLOAD', 'SIN', kind='interp', line=655)

# Page 904
W('32,2415', 0o00005, '', '', '04D', kind='operand', line=658)
W('32,2416', 0o17403, '', 'STODL', 'LNG(SPL)', 'LNG(SPL)=SIN(PHIE)                    PL04D', kind='interp', line=659)
W('32,2417', 0o77746, '', 'COS', kind='interp', line=660)
W('32,2420', 0o03401, '', 'STORE', 'LAT(SPL)', 'LAT(SPL)=COS(PHIE)', kind='interp', line=661)
W('32,2421', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=662)
W('32,2422', 0o03656, '', '', 'R(T2)/', kind='operand', line=663)
W('32,2423', 0o41406, '', 'PUSH', 'PUSH', kind='interp', line=664)
W('32,2424', 0o53515, '', 'PDVL', 'UNIT', '                                      PL22D', kind='interp', line=665)
W('32,2425', 0o03710, '', '', 'V(T2)/', kind='operand', line=666)
W('32,2426', 0o47315, '', 'PDVL', 'VXV', kind='interp', line=667)
W('32,2427', 0o53435, '', 'VXV', 'UNIT', 'UH3=UNIT(UR3 X UV3 X UR3)             PL10D', kind='interp', line=668)
W('32,2430', 0o63361, '', 'VXSC', 'PDVL', kind='interp', line=669)
W('32,2431', 0o03403, '', '', 'LNG(SPL)', kind='operand', line=670)
W('32,2432', 0o53361, '', 'VXSC', 'VAD', '                                      PL04D', kind='interp', line=671)
W('32,2433', 0o03401, '', '', 'LAT(SPL)', kind='operand', line=672)
W('32,2434', 0o43014, '', 'CLEAR', 'CLEAR', 'T(LS) IN MPAC', kind='interp', line=673)
W('32,2435', 0o00662, '', '', 'ERADFLAG', kind='operand', line=674)
W('32,2436', 0o01663, '', '', 'LUNAFLAG', kind='operand', line=675)
W('32,2437', 0o16152, '', 'STODL', 'ALPHAV', 'ALPHAV=UR3(COSPHIE)+UH3(SINPHIE)      PL02D', kind='interp', line=676)
W('32,2440', 0o77624, '', 'CALL', kind='interp', line=677)
W('32,2441', 0o26370, '', '', 'LAT-LONG', kind='operand', line=678)
W('32,2442', 0o77745, '', 'DLOAD', kind='interp', line=679)
W('32,2443', 0o01104, '', '', 'LAT', kind='operand', line=680)
W('32,2444', 0o17401, '', 'STODL', 'LAT(SPL)', 'LATITUDE LANDING SITE  *****', kind='interp', line=681)
W('32,2445', 0o01106, '', '', 'LONG', kind='operand', line=682)
W('32,2446', 0o37403, '', 'STCALL', 'LNG(SPL)', 'LONGITUDE LANDING SITE *****', kind='interp', line=683)
W('32,2447', 0o03762, '', '', 'SPRTEX', kind='operand', line=684)
#   COUNT* $$/RTE

# Page 905
# INITIAL VECTOR SUBROUTINE
#
# DESCRIPTION
# A PRECISION INTEGRATION OF THE STATE VECTOR TO THE TIME OF IGNITION IS PERFORMED. PRECOMPUTATIONS OCCUR.
#
# CALLING SEQUENCE
# L       CALL
# L+1             INVC100
#
# NORMAL EXIT MODE
# AT L+2 OF CALLING SEQUENCE WITH MPAC = 0
#
# ALARM EXIT MODE
# AT L+2 OF CALLING SEQUENCE WITH MPAC = OCTAL 612 FOR STATE VECTOR IN MOONS SPHERE OF INFLUENCE
#
# SUBROUTINES CALLED
# CSMPREC
#
# ERASABLE INITIALIZATION REQUIRED
# PUSHLIST
# NONE
# MPAC
# NONE
# OTHER
# SPRTETIG        TIME OF IGNITION                                        DP      B28     CS
# CSM STATE VECTOR
#
# OUTPUT
# R(T1)/          INITIAL POSITION VECTOR AT TIG                          VECTOR  B29     METERS
# V(T1)/          INITIAL VELOCITY VECTOR AT TIG                          VECTOR  B7      METERS/CS
# T1              INITIAL VECTOR TIME (TIG)                               DP      B28     CS
# UR1/            UNIT INITIAL VECTOR                                     VECTOR  B1
# UH/             UNIT HORIZONTAL VECTOR                                  VECTOR  B1
# CFPA            COSINE OF INITIAL FLIGHT PATH ANGLE                     DP      B1

W('32,2450', 0o71220, 'INVC100', 'STQ', 'DLOAD', kind='interp', line=723)
W('32,2451', 0o03762, '', '', 'SPRTEX', kind='operand', line=724)
W('32,2452', 0o03413, '', '', 'SPRTETIG', kind='operand', line=725)
W('32,2453', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=726)
W('32,2454', 0o27071, '', '', 'CSMPREC', 'PRECISION INTEGRATION  R0,V0 TO R1,V1', kind='operand', line=727)
W('32,2455', 0o67175, '', 'VLOAD', 'SXA,2', kind='interp', line=728)
W('32,2456', 0o00001, '', '', 'RATT', kind='operand', line=729)
W('32,2457', 0o03755, '', '', 'P(T1)', kind='operand', line=730)
W('32,2460', 0o27640, '', 'STOVL', 'R(T1)/', kind='interp', line=731)
W('32,2461', 0o00007, '', '', 'VATT', kind='operand', line=732)
W('32,2462', 0o17672, '', 'STODL', 'V(T1)/', kind='interp', line=733)
W('32,2463', 0o00015, '', '', 'TAT', kind='operand', line=734)
W('32,2464', 0o03716, '', 'STORE', 'T1', kind='interp', line=735)
W('32,2465', 0o53135, '', 'SLOAD', 'BZE', kind='interp', line=736)
W('32,2466', 0o03756, '', '', 'P(T1)', kind='operand', line=737)
# Page 906
W('32,2467', 0o64473, '', '', 'INVC109', kind='operand', line=739)
W('32,2470', 0o52135, 'INVC107', 'SLOAD', 'GOTO', kind='interp', line=740)
W('32,2471', 0o33563, '', '', 'OCT612', kind='operand', line=741)
W('32,2472', 0o74776, '', '', 'RTEALRM', 'R1,V1 NOT IN PROPER SPHERE OF INFLUENCE', kind='operand', line=742)
W('32,2473', 0o53575, 'INVC109', 'VLOAD', 'UNIT', kind='interp', line=743)
W('32,2474', 0o03640, '', '', 'R(T1)/', kind='operand', line=744)
W('32,2475', 0o17740, '', 'STODL', 'UR1/', 'UR1/                                  B1', kind='interp', line=745)
W('32,2476', 0o00045, '', '', '36D', kind='operand', line=746)
W('32,2477', 0o27646, '', 'STOVL', 'R(T1)', 'R(T1)                                 B29', kind='interp', line=747)
W('32,2500', 0o03672, '', '', 'V(T1)/', kind='operand', line=748)
W('32,2501', 0o77656, '', 'UNIT', kind='interp', line=749)
W('32,2502', 0o03746, '', 'STORE', 'UV1/', kind='interp', line=750)
W('32,2503', 0o72441, '', 'DOT', 'SL1', kind='interp', line=751)
W('32,2504', 0o03740, '', '', 'UR1/', kind='operand', line=752)
W('32,2505', 0o03757, '', 'STORE', 'CFPA', 'CFPA                                  B1', kind='interp', line=753)
W('32,2506', 0o45246, '', 'ABS', 'DSU', kind='interp', line=754)
W('32,2507', 0o33576, '', '', 'EPC1RTE', kind='operand', line=755)
W('32,2510', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=756)
W('32,2511', 0o64520, '', '', 'INVC115', 'NOT NEAR RECTILINEAR', kind='operand', line=757)
W('32,2512', 0o33502, '', '', '1RTEB2', kind='operand', line=758)
W('32,2513', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=759)
W('32,2514', 0o33524, '', '', 'ZERORTE', kind='operand', line=760)
W('32,2515', 0o41466, '', 'VDEF', 'PUSH', 'N/ = (0,0,1)', kind='interp', line=761)
W('32,2516', 0o77650, '', 'GOTO', kind='interp', line=762)
W('32,2517', 0o64524, '', '', 'INVC120', kind='operand', line=763)
W('32,2520', 0o47375, 'INVC115', 'VLOAD', 'VXV', kind='interp', line=764)
W('32,2521', 0o03740, '', '', 'UR1/', kind='operand', line=765)
W('32,2522', 0o03746, '', '', 'UV1/', kind='operand', line=766)
W('32,2523', 0o77606, '', 'PUSH', '', 'N/ = UR X UV                          B2', kind='interp', line=767)
W('32,2524', 0o71214, 'INVC120', 'CLEAR', 'DLOAD', kind='interp', line=768)
W('32,2525', 0o02661, '', '', 'RETROFLG', kind='operand', line=769)
W('32,2526', 0o51006, '', 'PUSH', 'BPL', kind='interp', line=770)
W('32,2527', 0o64533, '', '', 'INVC125', kind='operand', line=771)
W('32,2530', 0o57575, '', 'VLOAD', 'VCOMP', 'RETROGRADE ORBIT', kind='interp', line=772)
W('32,2531', 0o43006, '', 'PUSH', 'SET', kind='interp', line=773)
W('32,2532', 0o02461, '', '', 'RETROFLG', kind='operand', line=774)
W('32,2533', 0o77775, 'INVC125', 'VLOAD', kind='interp', line=775)
W('32,2534', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=776)
W('32,2535', 0o03740, '', '', 'UR1/', kind='operand', line=777)
W('32,2536', 0o03746, '', 'STORE', 'UH/', 'UH/                                   B1', kind='interp', line=778)
W('32,2537', 0o77650, '', 'GOTO', kind='interp', line=779)
W('32,2540', 0o03762, '', '', 'SPRTEX', kind='operand', line=780)

# Page 907
# PRECISION TRAJECTORY COMPUTATION SUBROUTINE
#
# DESCRIPTION
# A NUMERICALLY INTEGRATED TRAJECTORY IS GENERATED WHICH FOR THE RETURN TO EARTH PROBLEM SATISFIES THE REENTRY
# CONSTRAINTS (RCON AND X(T2)) ACHIEVED BY THE INITIAL CONIC TRAJECTORY AND MEETS THE DVD REQUIREMENT AS CLOSELY
# AS POSSIBLE.
#
# CALLING SEQUENCE
# L       CALL
# L+1             PREC100
#
# NORMAL EXIT MODE
# AT L+2 OF CALLING SEQUENCE WITH MPAC = 0
#
# ALARM EXIT MODE
# AT L+2 OF CALLING SEQUENCE WITH MPAC =
# OCTAL 605       FOR EXCESS ITERATIONS
# OCTAL 613       FOR REENTRY ANGLE OUT OF LIMITS
#
# SUBROUTINES CALLED
# INTSTALL
# RTENCK2
# RTENCK3
# TIMERAD
# PARAM
# V2T100
#
# ERASABLE INITIALIZATION REQUIRED
# PUSHLIST
# NONE
# MPAC
# NONE
# OTHER
# R(T1)/          INITIAL POSITION VECTOR                                 VECTOR  B29/B27 METERS
# V2(T1)/         POST IMPULSE INITIAL VELOCITY VECTOR                    VECTOR  B7/B5   METERS/CS
# V(T1)/          INITIAL VELOCITY VECTOR                                 VECTOR  B7/B5   METERS/CS
# T1              INITIAL VECTOR TIME                                     DP      B28     CS
# T12             INITIAL TO FINAL POSITION TIME                          DP      B28     CS
# RCON            CONIC FINAL RADIUS                                      DP      B29/B27 METERS
# R(T1)           MAGNITUDE OF INITIAL POSITION VECTOR                    DP      B29/B27 METERS
# X(T2)           COTANGENT OF FINAL FLIGHT PATH ANGLE                    DP      B0
# X(T1)           COTANGENT OF INITIAL FLIGHT PATH ANGLE                  DP      B5
# RTEDVD          DELTA VELOCITY DESIRED                                  DP      B7/B5   METERS/CS
# MAMAX1          MAJOR AXIS LIMIT FOR LOWER BOUND ON GAMDV ITERATOR      DP      B30/B28 METERS
# MAMAX2          MAJOR AXIS LIMIT FOR UPPER BOUND ON GAMDV ITERATOR      DP      B30/B28 METERS
# UR1/            UNIT INITIAL VECTOR                                     VECTOR  B1
# UH/             UNIT HORIZONTAL VECTOR                                  VECTOR  B1
# BETA1           1+X(T2)**2                                              DP      B1
# PHI2            PERIGEE OR APOGEE INDICATOR                             DP      B2      -1 PERIGEE, +1 APOGEE
#
# Page 908
#
# OUTPUT
# V2(T1)/         POST IMPULSE INITIAL VELOCITY VECTOR                    VECTOR  B7      METERS/CS
# R(T2)/          FINAL POSITION VECTOR                                   VECTOR  B29     METERS
# V(T2)/          FINAL VELOCITY VECTOR                                   VECTOR  B7      METERS/CS
# T2              FINAL TIME                                              DP      B28     CENTISECONDS
#
# DEBRIS
# RD              FINAL R DESIRED                                         DP      B29/B27 METERS
# R/APRE          R/A                                                     DP      B6
# P/RPRE          P/R                                                     DP      B4
# RPRE            MAGNITUDE OF R(T2)/                                     DP      B29/B27 METERS
# X(T2)PRE        COTANGENT OF GAMMA2                                     DP      B0
# DT12            CORRECTION TO FINAL TIME T2                             DP      B28     CENTISECONDS
# RCON            FINAL RADIUS                                            DP      B29/B27 METERS
# DRCON           DELTA RCON                                              DP      B29/B27 METERS

W('32,2541', 0o71220, 'PREC100', 'STQ', 'DLOAD', kind='interp', line=851)
W('32,2542', 0o03762, '', '', 'SPRTEX', kind='operand', line=852)
W('32,2543', 0o33532, '', '', '10RTE', kind='operand', line=853)
W('32,2544', 0o17730, '', 'STODL', 'NN1A', kind='interp', line=854)
W('32,2545', 0o03636, '', '', 'RCON', kind='operand', line=855)
W('32,2546', 0o03664, '', 'STORE', 'RD', kind='interp', line=856)
W('32,2547', 0o77745, 'PREC120', 'DLOAD', kind='interp', line=857)
W('32,2550', 0o33542, '', '', '2RTEB1', kind='operand', line=858)
W('32,2551', 0o17650, '', 'STODL', 'DT21PR', 'DT21PR = POSMAX', kind='interp', line=859)
W('32,2552', 0o33530, '', '', 'M15RTE', kind='operand', line=860)
W('32,2553', 0o37732, '', 'STCALL', 'NN2', kind='interp', line=861)
W('32,2554', 0o63726, '', '', 'RTENCK3', kind='operand', line=862)
W('32,2555', 0o77624, 'PREC125', 'CALL', kind='interp', line=863)
W('32,2556', 0o11637, '', '', 'PARAM', kind='operand', line=864)
W('32,2557', 0o77745, '', 'DLOAD', kind='interp', line=865)
W('32,2560', 0o02742, '', '', 'P', kind='operand', line=866)
W('32,2561', 0o14033, '', 'STODL', 'P/RPRE', kind='interp', line=867)
W('32,2562', 0o02744, '', '', 'R1A', kind='operand', line=868)
W('32,2563', 0o14035, '', 'STODL', 'R/APRE', kind='interp', line=869)
W('32,2564', 0o00041, '', '', 'R1', kind='operand', line=870)
W('32,2565', 0o14031, '', 'STODL', 'RPRE', kind='interp', line=871)
W('32,2566', 0o03775, '', '', 'COGA', kind='operand', line=872)
W('32,2567', 0o77661, '', 'SL', kind='interp', line=873)
W('32,2570', 0o20206, '', '', '5', kind='operand', line=874)
W('32,2571', 0o03724, '', 'STORE', 'X(T2)PRE', kind='interp', line=875)
W('32,2572', 0o43276, '', 'DCOMP', 'DAD', kind='interp', line=876)
W('32,2573', 0o03726, '', '', 'X(T2)', kind='operand', line=877)
W('32,2574', 0o45246, '', 'ABS', 'DSU', kind='interp', line=878)
W('32,2575', 0o33604, '', '', 'EPC4RTE', kind='operand', line=879)
W('32,2576', 0o50000, '', 'BOV', 'BMN', kind='interp', line=880)
W('32,2577', 0o64601, '', '', 'PREC130', kind='operand', line=881)
W('32,2600', 0o64770, '', '', 'PREC175', kind='operand', line=882)

# DESIRED REENTRY ANGLE NOT ACHIEVED

# Page 909
W('32,2601', 0o50145, 'PREC130', 'DLOAD', 'BMN', kind='interp', line=887)
W('32,2602', 0o03732, '', '', 'NN2', kind='operand', line=888)
W('32,2603', 0o64607, '', '', 'PREC140', kind='operand', line=889)
W('32,2604', 0o52135, 'PREC132', 'SLOAD', 'GOTO', 'TOO MANY ITERATIONS', kind='interp', line=890)
W('32,2605', 0o33562, '', '', 'OCT605', '      EXIT WITH ALARM', kind='operand', line=891)
W('32,2606', 0o65073, '', '', 'PRECX', kind='operand', line=892)

# DETERMINE RADIUS AT WHICH THE DESIRED REENTRY ANGLE WILL BE ACHIEVED

W('32,2607', 0o53145, 'PREC140', 'DLOAD', 'BZE', kind='interp', line=896)
W('32,2610', 0o03730, '', '', 'NN1A', kind='operand', line=897)
W('32,2611', 0o64647, '', '', 'PREC162', kind='operand', line=898)
W('32,2612', 0o62545, 'PREC150', 'DLOAD', 'SL2 B2', kind='interp', line=899)
W('32,2613', 0o00033, '', '', 'P/RPRE', kind='operand', line=900)
W('32,2614', 0o72405, '', 'DMP', 'SL1', 'BETA2=BETA1*P/R               B2      PL02', kind='interp', line=901)
W('32,2615', 0o03754, '', '', 'BETA1', kind='operand', line=902)
W('32,2616', 0o71206, '', 'PUSH', 'DLOAD', kind='interp', line=903)
W('32,2617', 0o00035, '', '', 'R/APRE', kind='operand', line=904)
W('32,2620', 0o41212, '', 'SL4', 'DMP', kind='interp', line=905)
W('32,2621', 0o00001, '', '', '00D', kind='operand', line=906)
W('32,2622', 0o50021, '', 'BDSU', 'BMN', 'BETA3=1-BETA2*R/A', kind='interp', line=907)
W('32,2623', 0o33506, '', '', '1RTEB4', kind='operand', line=908)
W('32,2624', 0o64637, '', '', 'PREC160', kind='operand', line=909)
W('32,2625', 0o75512, 'PREC155', 'SL2', 'SQRT', kind='interp', line=910)
W('32,2626', 0o44205, '', 'DMP', 'BDSU', kind='interp', line=911)
W('32,2627', 0o03761, '', '', 'PHI2', kind='operand', line=912)
W('32,2630', 0o33504, '', '', '1RTEB3', kind='operand', line=913)
W('32,2631', 0o65301, '', 'NORM', 'PDDL', kind='interp', line=914)
W('32,2632', 0o00047, '', '', 'X1', kind='operand', line=915)
W('32,2633', 0o56342, '', 'SR1', 'DDV', 'BETA4=BETA2/(1-PHI2*SQRT(BETA3))', kind='interp', line=916)
W('32,2634', 0o52057, '', 'SL*', 'GOTO B1', kind='interp', line=917)
W('32,2635', 0o20200, '', '', '0 -1,1', kind='operand', line=918)
W('32,2636', 0o64655, '', '', 'PREC165', kind='operand', line=919)
W('32,2637', 0o60345, 'PREC160', 'DLOAD', 'NORM', kind='interp', line=920)
W('32,2640', 0o00035, '', '', 'R/APRE', kind='operand', line=921)
W('32,2641', 0o00047, '', '', 'X1', kind='operand', line=922)
W('32,2642', 0o53665, '', 'BDDV', 'SL* B1', kind='interp', line=923)
W('32,2643', 0o33500, '', '', '1RTEB1', kind='operand', line=924)
W('32,2644', 0o20173, '', '', '0 -6,1', kind='operand', line=925)
W('32,2645', 0o77650, '', 'GOTO', kind='interp', line=926)
W('32,2646', 0o64655, '', '', 'PREC165', kind='operand', line=927)
W('32,2647', 0o60345, 'PREC162', 'DLOAD', 'NORM', kind='interp', line=928)
W('32,2650', 0o00031, '', '', 'RPRE', kind='operand', line=929)
W('32,2651', 0o00047, '', '', 'X1', kind='operand', line=930)
W('32,2652', 0o53665, '', 'BDDV', 'SL*', 'BETA4=RD/RPRE                 B1', kind='interp', line=931)
W('32,2653', 0o03664, '', '', 'RD', kind='operand', line=932)
W('32,2654', 0o20200, '', '', '0 -1,1', kind='operand', line=933)
W('32,2655', 0o41401, 'PREC165', 'SETPD', 'PUSH', kind='interp', line=934)
W('32,2656', 0o00001, '', '', '0', kind='operand', line=935)
W('32,2657', 0o57425, '', 'DSU', 'DCOMP', kind='interp', line=936)
# Page 910
W('32,2660', 0o33500, '', '', '1RTEB1', kind='operand', line=938)
W('32,2661', 0o03765, '', 'STORE', 'BETA12', kind='interp', line=939)
W('32,2662', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=940)
W('32,2663', 0o64674, '', '', 'PREC168', kind='operand', line=941)
W('32,2664', 0o03724, '', '', 'X(T2)PRE', kind='operand', line=942)
W('32,2665', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=943)
W('32,2666', 0o64672, '', '', 'PREC167', kind='operand', line=944)
W('32,2667', 0o03765, '', '', 'BETA12', kind='operand', line=945)
W('32,2670', 0o77676, '', 'DCOMP', kind='interp', line=946)
W('32,2671', 0o03765, '', 'STORE', 'BETA12', kind='interp', line=947)
W('32,2672', 0o77745, 'PREC167', 'DLOAD', kind='interp', line=948)
W('32,2673', 0o03765, '', '', 'BETA12', kind='operand', line=949)
W('32,2674', 0o45246, 'PREC168', 'ABS', 'DSU', kind='interp', line=950)
W('32,2675', 0o33610, '', '', 'EPC6RTE', kind='operand', line=951)
W('32,2676', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=952)
W('32,2677', 0o64770, '', '', 'PREC175', kind='operand', line=953)
W('32,2700', 0o72405, '', 'DMP', 'SL1', kind='interp', line=954)
W('32,2701', 0o00031, '', '', 'RPRE', kind='operand', line=955)
W('32,2702', 0o77606, '', 'PUSH', '', 'RF = NEW RADIUS', kind='interp', line=956)
W('32,2703', 0o43345, 'PREC170', 'DLOAD', 'DAD', kind='interp', line=957)
W('32,2704', 0o03732, '', '', 'NN2', kind='operand', line=958)
W('32,2705', 0o33522, '', '', '1RTEB28', kind='operand', line=959)
W('32,2706', 0o03732, '', 'STORE', 'NN2', kind='interp', line=960)
W('32,2707', 0o43175, '', 'VLOAD', 'SET', kind='interp', line=961)
W('32,2710', 0o03656, '', '', 'R(T2)/', kind='operand', line=962)
W('32,2711', 0o03466, '', '', 'RVSW', kind='operand', line=963)
W('32,2712', 0o26657, '', 'STOVL', 'RVEC', kind='interp', line=964)
W('32,2713', 0o03710, '', '', 'V(T2)/', kind='operand', line=965)
W('32,2714', 0o77765, '', 'SIGN', kind='interp', line=966)
W('32,2715', 0o03765, '', '', 'BETA12', kind='operand', line=967)
W('32,2716', 0o16746, '', 'STODL', 'VVEC', kind='interp', line=968)
W('32,2717', 0o33500, '', '', '1RTEB1', kind='operand', line=969)
W('32,2720', 0o57565, '', 'SIGN', 'DCOMP', kind='interp', line=970)
W('32,2721', 0o03765, '', '', 'BETA12', kind='operand', line=971)
W('32,2722', 0o71354, '', 'LXA,2', 'DLOAD', kind='interp', line=972)
W('32,2723', 0o00154, '', '', 'MPAC', kind='operand', line=973)
W('32,2724', 0o67140, '', 'LXC,1', 'SXA,2', kind='interp', line=974)
W('32,2725', 0o03734, '', '', 'CONICX1', kind='operand', line=975)
W('32,2726', 0o02756, '', '', 'SGNRDOT', kind='operand', line=976)
W('32,2727', 0o36760, '', 'STCALL', 'RDESIRED', 'COMPUTED DT12 (CORRECTION TO TIME OF', kind='interp', line=977)
W('32,2730', 0o25556, '', '', 'TIMERAD', '      NEW RADIUS)', kind='operand', line=978)
W('32,2731', 0o75345, '', 'DLOAD', 'SIGN', kind='interp', line=979)
W('32,2732', 0o00037, '', '', 'T', kind='operand', line=980)
W('32,2733', 0o03765, '', '', 'BETA12', kind='operand', line=981)
W('32,2734', 0o60325, '', 'PDDL', 'NORM', 'DT21=(PHI4)DT21                       PL02D', kind='interp', line=982)
W('32,2735', 0o03650, '', '', 'DT21PR', kind='operand', line=983)
W('32,2736', 0o00047, '', '', 'X1', kind='operand', line=984)
W('32,2737', 0o53665, '', 'BDDV', 'SL*', kind='interp', line=985)
W('32,2740', 0o00001, '', '', '00D', kind='operand', line=986)
W('32,2741', 0o20176, '', '', '0 -3,1', kind='operand', line=987)
# Page 911
W('32,2742', 0o50006, '', 'PUSH', 'BMN', 'BETA13=(DT21)/(DT21PR)        R3      PL04D', kind='interp', line=989)
W('32,2743', 0o64750, '', '', 'PREC172', kind='operand', line=990)
W('32,2744', 0o65345, '', 'DLOAD', 'PDDL', 'BETA14=1                      B0      PL04D', kind='interp', line=991)
W('32,2745', 0o33542, '', '', '2RTEB1', kind='operand', line=992)
W('32,2746', 0o77650, '', 'GOTO', kind='interp', line=993)
W('32,2747', 0o64752, '', '', 'PREC173', kind='operand', line=994)
W('32,2750', 0o65345, 'PREC172', 'DLOAD', 'PDDL', 'BETA14=.6                     B0      PL04D', kind='interp', line=995)
W('32,2751', 0o33534, '', '', 'M.6RTE', kind='operand', line=996)
W('32,2752', 0o45271, 'PREC173', 'DDV', 'DSU', kind='interp', line=997)
W('32,2753', 0o00003, '', '', '02D', kind='operand', line=998)
W('32,2754', 0o33504, '', '', '1RTEB3', kind='operand', line=999)
W('32,2755', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=1000)
W('32,2756', 0o64762, '', '', 'PREC174', kind='operand', line=1001)
W('32,2757', 0o77605, '', 'DMP', kind='interp', line=1002)
W('32,2760', 0o03650, '', '', 'DT21PR', kind='operand', line=1003)
W('32,2761', 0o00001, '', 'STORE', '00D', 'DT21=(BETA14)DT21PR           B28', kind='interp', line=1004)
W('32,2762', 0o41545, 'PREC174', 'DLOAD', 'PUSH', kind='interp', line=1005)
W('32,2763', 0o00001, '', '', '00D', kind='operand', line=1006)
W('32,2764', 0o37650, '', 'STCALL', 'DT21PR', kind='interp', line=1007)
W('32,2765', 0o63710, '', '', 'RTENCK2', kind='operand', line=1008)
W('32,2766', 0o77650, '', 'GOTO', kind='interp', line=1009)
W('32,2767', 0o64555, '', '', 'PREC125', kind='operand', line=1010)
W('32,2770', 0o45345, 'PREC175', 'DLOAD', 'DSU', kind='interp', line=1011)
W('32,2771', 0o00031, '', '', 'RPRE', kind='operand', line=1012)
W('32,2772', 0o03664, '', '', 'RD', kind='operand', line=1013)
W('32,2773', 0o51406, '', 'PUSH', 'ABS', 'RPRE-RD = RERR', kind='interp', line=1014)
W('32,2774', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1015)
W('32,2775', 0o33612, '', '', 'EPC7RTE', kind='operand', line=1016)
W('32,2776', 0o34703, '', '', 'PREC220', kind='operand', line=1017)

# DESIRED RADIUS HAS NOT BEEN ACHIEVED

W('32,2777', 0o53145, '', 'DLOAD', 'BZE', kind='interp', line=1021)
W('32,3000', 0o03730, '', '', 'NN1A', kind='operand', line=1022)
W('32,3001', 0o64604, '', '', 'PREC132', 'TOO MANY ITERATIONS', kind='operand', line=1023)
W('32,3002', 0o53025, '', 'DSU', 'BZE', kind='interp', line=1024)
W('32,3003', 0o33532, '', '', '10RTE', kind='operand', line=1025)
W('32,3004', 0o65037, '', '', 'PREC207', kind='operand', line=1026)
W('32,3005', 0o45345, 'PREC205', 'DLOAD', 'DSU', 'NOT FIRST PASS OF ITERATION', kind='interp', line=1027)
W('32,3006', 0o03670, '', '', "RPRE'", kind='operand', line=1028)
W('32,3007', 0o00031, '', '', 'RPRE', "RPRE'-RPRE                    B29/B27", kind='operand', line=1029)
W('32,3010', 0o55301, '', 'NORM', 'BDDV', kind='interp', line=1030)
W('32,3011', 0o00050, '', '', 'X2', kind='operand', line=1031)
W('32,3012', 0o03666, '', '', 'DRCON', kind='operand', line=1032)
W('32,3013', 0o41457, '', 'SL*', 'PUSH', "DRCON/(RPRE'-RPRE)=S          B2", kind='interp', line=1033)
W('32,3014', 0o57600, '', '', '0 -2,2', kind='operand', line=1034)
W('32,3015', 0o40015, '', 'DAD', 'BOV', 'S GR +4 OR LS -4', kind='interp', line=1035)
W('32,3016', 0o33500, '', '', '1RTEB1', kind='operand', line=1036)
W('32,3017', 0o65024, '', '', 'PREC205M', kind='operand', line=1037)
W('32,3020', 0o45246, '', 'ABS', 'DSU', kind='interp', line=1038)
# Page 912
W('32,3021', 0o33500, '', '', '1RTEB1', kind='operand', line=1040)
W('32,3022', 0o77640, '', 'BMN', kind='interp', line=1041)
W('32,3023', 0o65027, '', '', 'PREC206', kind='operand', line=1042)
W('32,3024', 0o57545, 'PREC205M', 'DLOAD', 'DCOMP', 'S GR 0 OR LS -4', kind='interp', line=1043)
W('32,3025', 0o33542, '', '', '2RTEB1', kind='operand', line=1044)
W('32,3026', 0o77725, '', 'PDDL', '', 'S=-4                          B2', kind='interp', line=1045)
W('32,3027', 0o41345, 'PREC206', 'DLOAD', 'DMP', kind='interp', line=1046)
W('32,3030', 0o77712, '', 'SL2', kind='interp', line=1047)
W('32,3031', 0o03666, '', 'STORE', 'DRCON', 'DRCON=S(RERR)                 B29', kind='interp', line=1048)
W('32,3032', 0o77615, '', 'DAD', kind='interp', line=1049)
W('32,3033', 0o03636, '', '', 'RCON', kind='operand', line=1050)
W('32,3034', 0o03636, '', 'STORE', 'RCON', 'RCON+DRCON=RCON', kind='interp', line=1051)
W('32,3035', 0o77650, '', 'GOTO', kind='interp', line=1052)
W('32,3036', 0o65056, '', '', 'PREC210', kind='operand', line=1053)
W('32,3037', 0o63545, 'PREC207', 'DLOAD', 'DSQ', 'FIRST PASS OF ITERATION', kind='interp', line=1054)
W('32,3040', 0o03664, '', '', 'RD', kind='operand', line=1055)
W('32,3041', 0o70501, '', 'NORM', 'SR1', kind='interp', line=1056)
W('32,3042', 0o00047, '', '', 'X1', kind='operand', line=1057)
W('32,3043', 0o60325, '', 'PDDL', 'NORM', kind='interp', line=1058)
W('32,3044', 0o00031, '', '', 'RPRE', kind='operand', line=1059)
W('32,3045', 0o00050, '', '', 'X2', kind='operand', line=1060)
W('32,3046', 0o55260, '', 'XSU,1', 'BDDV', kind='interp', line=1061)
W('32,3047', 0o00047, '', '', 'X2', kind='operand', line=1062)
W('32,3050', 0o77657, '', 'SR*', kind='interp', line=1063)
W('32,3051', 0o20600, '', '', '0 -1,1', kind='operand', line=1064)
W('32,3052', 0o03636, '', 'STORE', 'RCON', 'RD**2/RPRE=RCON', kind='interp', line=1065)
W('32,3053', 0o77625, '', 'DSU', kind='interp', line=1066)
W('32,3054', 0o03664, '', '', 'RD', kind='operand', line=1067)
W('32,3055', 0o03666, '', 'STORE', 'DRCON', 'RCON-RD=DRCON', kind='interp', line=1068)
W('32,3056', 0o77745, 'PREC210', 'DLOAD', '', 'PREPARE FOR NEXT ITERATION', kind='interp', line=1069)
W('32,3057', 0o00031, '', '', 'RPRE', kind='operand', line=1070)
W('32,3060', 0o17670, '', 'STODL', "RPRE'", kind='interp', line=1071)
W('32,3061', 0o03730, '', '', 'NN1A', kind='operand', line=1072)
W('32,3062', 0o77625, '', 'DSU', kind='interp', line=1073)
W('32,3063', 0o33522, '', '', '1RTEB28', kind='operand', line=1074)
W('32,3064', 0o37730, '', 'STCALL', 'NN1A', kind='interp', line=1075)
W('32,3065', 0o65075, '', '', 'V2T100', kind='operand', line=1076)
W('32,3066', 0o52030, '', 'BHIZ', 'GOTO', kind='interp', line=1077)
W('32,3067', 0o64547, '', '', 'PREC120', kind='operand', line=1078)
W('32,3070', 0o65073, '', '', 'PRECX', kind='operand', line=1079)

# DESIRED RADIUS ACHIEVED

#   SETLOC RTE2
#   BANK
W('16,2703', 0o45345, 'PREC220', 'DLOAD', 'DSU', kind='interp', line=1085)
W('16,2704', 0o03726, '', '', 'X(T2)', kind='operand', line=1086)
W('16,2705', 0o03724, '', '', 'X(T2)PRE', kind='operand', line=1087)
W('16,2706', 0o45246, '', 'ABS', 'DSU', kind='interp', line=1088)
W('16,2707', 0o34716, '', '', 'EPC8RTE', kind='operand', line=1089)
# Page 913
W('16,2710', 0o67240, '', 'BMN', 'SLOAD', kind='interp', line=1091)
W('16,2711', 0o65071, '', '', 'PREC225', kind='operand', line=1092)
W('16,2712', 0o34720, '', '', 'OCT613', kind='operand', line=1093)
W('16,2713', 0o77650, '', 'GOTO', kind='interp', line=1094)
W('16,2714', 0o65073, '', '', 'PRECX', 'IF REENTRY ANGLE OUT OF LIMITS', kind='operand', line=1095)

W('16,2715', 0o00040, 'EPC8RTE', '2DEC', '.002', kind='data', line=1097)
W('16,2716', 0o30447, kind='data', line=1097)

W('16,2717', 0o00613, 'OCT613', 'OCT', '613', kind='data', line=1099)

# DESIRED FINAL ANGLE HAS BEEN REACHED.

#   SETLOC RTE
#   BANK
W('32,3071', 0o77745, 'PREC225', 'DLOAD', kind='interp', line=1105)
W('32,3072', 0o33524, '', '', 'ZERORTE', kind='operand', line=1106)
W('32,3073', 0o77650, 'PRECX', 'GOTO', kind='interp', line=1107)
W('32,3074', 0o03762, '', '', 'SPRTEX', kind='operand', line=1108)

# Page 914
# INTEGRATION CALLING SUBROUTINE
#
# DESCRIPTION
# PERFORMS CONIC AND PRECISION INTEGRATIONS USING SUBROUTINE INTEGRVS.  THERE ARE THREE ENTRANCES (RTENCK1,
# RTENCK2, AND RTENCK3) FOR DIFFERENT SOURCES OF INPUT AND DIFFERENT OPTIONS.  THERE IS A COMMON SET OF OUTPUT
# WHICH INCLUDES SET UP OF INPUT FOR THE PARAM SUBROUTINE.
#
# RTENCK1 (CONIC INTEGRATION)
#
# CALLING SEQUENCE
# L       CALL
# L+1             RTENCK1
#
# ERASABLE INITIALIZATION REQUIRED
# SAME AS FOR THE RTENCK3 ENTRANCE
#
# RTENCK2 (PRECISION INTEGRATION)
#
# CALLING SEQUENCE
# L       CALL
# L+1             RTENCK2
#
# ERASABLE INITIALIZATION REQUIRED
# PUSHLIST
# PUSHLOC-2   INTEGRATION TIME DT12 (CORRECTION TO T2)                DP      B28     CS
# OTHER
# R(T2)/      FINAL POSITION VECTOR                                   VECTOR  B29     METERS
# V(T2)/      FINAL VELOCITY VECTOR                                   VECTOR  B7      METERS/CS
# T2          FINAL TIME                                              DP      B28     CS
#
# RTENCK3 (PRECISION INTEGRATION)
#
# CALLING SEQUENCE
# L       CALL
# L+1             RTENCK3
#
# ERASABLE INITIALIZATION REQUIRED
# R(T1)/          INITIAL POSITION VECTOR                                 VECTOR  B29     METERS
# V2(T1)/         POST IMPULSE INITIAL VELOCITY VECTOR                    VECTOR  B7      M/CS
# T1              INITIAL VECTOR TIME                                     DP      B28     CS
# T2              FINAL TIME                                              DP      B28     CS
#
# EXIT MODE
# AT L+2 OF CALLING SEQUENCE
#
# SUBROUTINES CALLED
# INTSTALL
# INTEGRVS
#
# OUTPUT
# PUSHLIST
# Page 915
# PUSHLOC-6       FINAL POSITION VECTOR R(T2)/                            VECTOR  B29     METERS
# X1              CONICS MUTABLE ENTRY FOR EARTH (-2)                     SP      B14
# MPAC
# FINAL VELOCITY VECTOR V(T2)/                            VECTOR  B7      M/CS
# OTHER
# R(T2)/          AS IN PUSHLIST
# V(T2)/          AS IN MPAC
# T2              FINAL TIME                                              DP      B28     CS

#   SETLOC RTE3
#   BANK
W('31,3700', 0o45020, 'RTENCK1', 'STQ', 'CALL', kind='interp', line=1174)
W('31,3701', 0o03733, '', '', 'RTENCKEX', kind='operand', line=1175)
W('31,3702', 0o27442, '', '', 'INTSTALL', kind='operand', line=1176)
W('31,3703', 0o43175, '', 'VLOAD', 'SET', kind='interp', line=1177)
W('31,3704', 0o03640, '', '', 'R(T1)/', kind='operand', line=1178)
W('31,3705', 0o01473, '', '', 'INTYPFLG', kind='operand', line=1179)
W('31,3706', 0o77650, '', 'GOTO', kind='interp', line=1180)
W('31,3707', 0o63734, '', '', 'RTENCK3B', kind='operand', line=1181)

W('31,3710', 0o45020, 'RTENCK2', 'STQ', 'CALL', kind='interp', line=1183)
W('31,3711', 0o03733, '', '', 'RTENCKEX', kind='operand', line=1184)
W('31,3712', 0o27442, '', '', 'INTSTALL', kind='operand', line=1185)
W('31,3713', 0o77214, '', 'CLEAR', 'VLOAD', kind='interp', line=1186)
W('31,3714', 0o01673, '', '', 'INTYPFLG', kind='operand', line=1187)
W('31,3715', 0o03656, '', '', 'R(T2)/', kind='operand', line=1188)
W('31,3716', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=1189)
W('31,3717', 0o03710, '', '', 'V(T2)/', kind='operand', line=1190)
W('31,3720', 0o15543, '', 'STODL', 'VCV', kind='interp', line=1191)
W('31,3721', 0o03736, '', '', 'T2', kind='operand', line=1192)
W('31,3722', 0o01517, '', 'STORE', 'TET', kind='interp', line=1193)
W('31,3723', 0o77615, '', 'DAD', kind='interp', line=1194)
W('31,3724', 0o77650, '', 'GOTO', kind='interp', line=1195)
W('31,3725', 0o63742, '', '', 'RTENCK3D', kind='operand', line=1196)

W('31,3726', 0o45020, 'RTENCK3', 'STQ', 'CALL', kind='interp', line=1198)
W('31,3727', 0o03733, '', '', 'RTENCKEX', kind='operand', line=1199)
W('31,3730', 0o27442, '', '', 'INTSTALL', kind='operand', line=1200)
W('31,3731', 0o43175, 'RTENCK3A', 'VLOAD', 'CLEAR', kind='interp', line=1201)
W('31,3732', 0o03640, '', '', 'R(T1)/', kind='operand', line=1202)
W('31,3733', 0o01673, '', '', 'INTYPFLG', kind='operand', line=1203)
W('31,3734', 0o25535, 'RTENCK3B', 'STOVL', 'RCV', kind='interp', line=1204)
W('31,3735', 0o03700, '', '', 'V2(T1)/', kind='operand', line=1205)
W('31,3736', 0o15543, '', 'STODL', 'VCV', kind='interp', line=1206)
W('31,3737', 0o03716, '', '', 'T1', kind='operand', line=1207)
W('31,3740', 0o15517, '', 'STODL', 'TET', kind='interp', line=1208)
W('31,3741', 0o03736, '', '', 'T2', kind='operand', line=1209)
# Page 916
W('31,3742', 0o00041, 'RTENCK3D', 'STORE', 'TDEC1', kind='interp', line=1211)
W('31,3743', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=1212)
W('31,3744', 0o00263, '', '', 'MOONFLAG', kind='operand', line=1213)
W('31,3745', 0o27135, '', '', 'INTEGRVS', kind='operand', line=1214)
W('31,3746', 0o77775, '', 'VLOAD', kind='interp', line=1215)
W('31,3747', 0o00001, '', '', 'RATT', kind='operand', line=1216)
W('31,3750', 0o03656, '', 'STORE', 'R(T2)/', kind='interp', line=1217)
W('31,3751', 0o70125, '', 'PDDL', 'LXC,1', kind='interp', line=1218)
W('31,3752', 0o00015, '', '', 'TAT', kind='operand', line=1219)
W('31,3753', 0o03734, '', '', 'CONICX1', kind='operand', line=1220)
W('31,3754', 0o27736, '', 'STOVL', 'T2', kind='interp', line=1221)
W('31,3755', 0o00007, '', '', 'VATT', kind='operand', line=1222)
W('31,3756', 0o03710, '', 'STORE', 'V(T2)/', kind='interp', line=1223)
W('31,3757', 0o77650, '', 'GOTO', kind='interp', line=1224)
W('31,3760', 0o03733, '', '', 'RTENCKEX', kind='operand', line=1225)
#   SETLOC RTE
#   BANK

# Page 917
# V2(T1) COMPUTATION SUBROUTINE
#
# DESCRIPTION
# A POST IMPULSE VELOCITY VECTOR (V2(T1)) IS COMPUTED WHICH EITHER
# (1)     MEETS THE INPUT VELOCITY CHANGE DESIRED (RTEDVD) IN A MINIMUM TIME      OR
# (2)     IF A VELOCITY CHANGE ISN'T SPECIFIED (RTEDVD = 0), A V2(T1) IS COMPUTED WHICH MINIMIZES THE IMPULSE (DV)
# AND CONSEQUENTLY FUEL.
#
# CALLING SEQUENCE
# L       CALL
# L+1             V2T100
#
# NORMAL EXIT MODE
# AT L+2 OF CALLING SEQUENCE WITH MPAC = 0
#
# ALARM EXIT MODE
# AT L+2 OF CALLING SEQUENCE WITH MPAC = OCTAL 605 FOR EXCESS ITERATIONS.
#
# SUBROUTINES CALLED
# GAMDV10
# XT1LIM
# DVCALC
#
# ERASABLE INITIALIZATION REQUIRED
# PUSHLIST
# NONE
# MPAC
# NONE
# OTHER
# R(T1)           MAGNITUDE OF INITIAL POSITION VECTOR                    DP      B29/B27 METERS
# RCON            MAGNITUDE OF FINAL POSITION VECTOR                      DP      B29/B27 METERS
# V(T1)/          INITIAL VELOCITY VECTOR                                 VECTOR  B7/B5   METERS/CS
# RTEDVD          DELTA VELOCITY DESIRED                                  DP      B7/B5   METERS/CS
# UR1/            UNIT INITIAL VECTOR                                     VECTOR  B1
# UH/             UNIT HORIZONTAL VECTOR                                  VECTOR  B1
# X(T2)           COTANGENT OF FINAL FLIGHT PATH ANGLE                    DP      B0
# X(T1)           COTANGENT OF INITIAL FLIGHT PATH ANGLE (INPUT FOR PREC) DP      B5
# CFPA            COSINE OF INITIAL FLIGHT PATH ANGLE                     DP      B1
# MAMAX1          MAJOR AXIS LIMIT FOR LOWER BOUND ON GAMDV ITERATOR      DP      B30/B28 METERS
# MAMAX2          MAJOR AXIS LIMIT FOR UPPER BOUND ON GAMDV ITERATOR      DP      B30/B28 METERS
# PHI2            REENTRY NEAR PERIGEE OR APOGEE INDICATE (RTE ONLY)      DP      B2      -1 PERIGEE, +1 APOGEE
# N1              CONIC OR PRECISION ITERATION OPERATOR                   DP      B28     NEGATIVE CONIC, PLUS PREC
#
# OUTPUT
# V2(T1)/         POST IMPULSE INITIAL VELOCITY VECTOR                    VECTOR  B7/B5   METERS/CS
# DV              INITIAL VELOCITY CHANGE                                 DP      B7/B5   METERS/CS
# X(T1)           COTANGENT OF INITIAL FLIGHT PATH ANGLE (POST IMPULSE)   DP      B5
# PCON            SEMI-LATUS RECTUM                                       DP      B28/B26 METERS
# BETA1           1+X(T2)**2                                              DP      B1
#
# Page 918
#
# DEBRIS
# PUSHLIST
# 00D             X(T1),,=PREVIOUS PRECISION X(T1)                        DP      B5
# 02D             THETA1=BETA5*LAMBDA-1                                   TP      B17
# 05D             THETA2=2*R(T1)*(LAMBDA-1)                               TP      B38/B36
# 08D             THETA3=MU**.5/R(T1)                                     DP      B-4/B-5
# 10D             X(T1)MIN=LOWER BOUND ON X(T1) IN GAMDV ITERATOR         DP      B5
# 12D             DX(T1)MAX=MAXIMUM DELTA X(T1)                           DP      B5
# 14D             X(T1)MAX=UPPER BOUND ON X(T1) IN GAMDV ITERATOR         DP      B5
# 16D             DX(T1)=ITERATOR INCREMENT                               DP      B5
# 31D             GAMDV10 SUBROUTINE RETURN ADDRESS
# 32D             DVCALC SUBROUTINE RETURN ADDRESS
# 33D             V2T100 SUBROUTINE RETURN ADDRESS

W('32,3075', 0o71220, 'V2T100', 'STQ', 'DLOAD', kind='interp', line=1296)
W('32,3076', 0o00041, '', '', '33D', kind='operand', line=1297)
W('32,3077', 0o03636, '', '', 'RCON', kind='operand', line=1298)
W('32,3100', 0o45240, '', 'BMN', 'DSU', 'ABORT IF RCON NEGATIVE', kind='interp', line=1299)
W('32,3101', 0o65105, '', '', 'V2TERROR', kind='operand', line=1300)
W('32,3102', 0o03646, '', '', 'R(T1)', kind='operand', line=1301)
W('32,3103', 0o77640, '', 'BMN', kind='interp', line=1302)
W('32,3104', 0o65110, '', '', 'V2T101', kind='operand', line=1303)
W('32,3105', 0o77776, 'V2TERROR', 'EXIT', '', '      OR IF LAMBDA LESS THAN ONE', kind='interp', line=1304)
W('32,3106', 0o05721, '', 'TC', 'POODOO', 'NO SOLUTION IF LAMBDA LESS THAN 1', line=1305)
W('32,3107', 0o00610, '', 'OCT', '00610', kind='data', line=1306)
W('32,3110', 0o43001, 'V2T101', 'SETPD', 'CLEAR', kind='interp', line=1307)
W('32,3111', 0o00001, '', '', '0', '                                      PL00D', kind='operand', line=1308)
W('32,3112', 0o00272, '', '', 'F2RTE', kind='operand', line=1309)
W('32,3113', 0o60345, '', 'DLOAD', 'NORM', kind='interp', line=1310)
W('32,3114', 0o03636, '', '', 'RCON', kind='operand', line=1311)
W('32,3115', 0o00047, '', '', 'X1', kind='operand', line=1312)
W('32,3116', 0o60325, '', 'PDDL', 'NORM', kind='interp', line=1313)
W('32,3117', 0o03646, '', '', 'R(T1)', kind='operand', line=1314)
W('32,3120', 0o00051, '', '', 'S1', kind='operand', line=1315)
W('32,3121', 0o00013, '', 'STORE', '10D', kind='interp', line=1316)
W('32,3122', 0o56342, '', 'SR1', 'DDV', 'R1/RCON = LAMBDA              B1', kind='interp', line=1317)
W('32,3123', 0o65260, '', 'XSU,1', 'PDDL', '                                      PL02D', kind='interp', line=1318)
W('32,3124', 0o00050, '', '', 'S1', kind='operand', line=1319)
W('32,3125', 0o03726, '', '', 'X(T2)', kind='operand', line=1320)
W('32,3126', 0o77716, '', 'DSQ', kind='interp', line=1321)
W('32,3127', 0o43342, '', 'SR1', 'DAD', kind='interp', line=1322)
W('32,3130', 0o33500, '', '', '1RTEB1', kind='operand', line=1323)
W('32,3131', 0o03754, '', 'STORE', 'BETA1', '1+X(T2)**2 = BETA1            B1', kind='interp', line=1324)
W('32,3132', 0o77605, '', 'DMP', kind='interp', line=1325)
W('32,3133', 0o00001, '', '', '00D', kind='operand', line=1326)
W('32,3134', 0o00035, '', 'STORE', '28D', 'BETAI*LAMBDA = BETA5', kind='interp', line=1327)
W('32,3135', 0o53605, '', 'DMP', 'SL*', kind='interp', line=1328)
W('32,3136', 0o00001, '', '', '00D', kind='operand', line=1329)
W('32,3137', 0o20172, '', '', '0 -7,1', kind='operand', line=1330)
W('32,3140', 0o45257, '', 'SL*', 'DSU', kind='interp', line=1331)
# Page 919
W('32,3141', 0o20172, '', '', '0 -7,1', kind='operand', line=1333)
W('32,3142', 0o33516, '', '', '1RTEB17', kind='operand', line=1334)
W('32,3143', 0o65234, '', 'RTB', 'PDDL', 'BETA5*LAMBDA-1 = THETA1       B17     PL05D', kind='interp', line=1335)
W('32,3144', 0o45565, '', '', 'TPMODE', kind='operand', line=1336)
W('32,3145', 0o33500, '', '', '1RTEB1', kind='operand', line=1337)
W('32,3146', 0o57457, '', 'SR*', 'DCOMP', kind='interp', line=1338)
W('32,3147', 0o20601, '', '', '0,1', kind='operand', line=1339)
W('32,3150', 0o41215, '', 'DAD', 'DMP', kind='interp', line=1340)
W('32,3151', 0o00001, '', '', '00D', kind='operand', line=1341)
W('32,3152', 0o03646, '', '', 'R(T1)', kind='operand', line=1342)
W('32,3153', 0o47057, '', 'SL*', 'RTB', kind='interp', line=1343)
W('32,3154', 0o20172, '', '', '0 -7D,1', kind='operand', line=1344)
W('32,3155', 0o45565, '', '', 'TPMODE', kind='operand', line=1345)
W('32,3156', 0o77725, '', 'PDDL', '', '2*R(T1)*(LAMBDA-1)=THETA2     B38/B36 PL08D', kind='interp', line=1346)
W('32,3157', 0o33632, '', '', 'RTMURTE', kind='operand', line=1347)
W('32,3160', 0o70501, '', 'NORM', 'SR1', kind='interp', line=1348)
W('32,3161', 0o00050, '', '', 'X2', kind='operand', line=1349)
W('32,3162', 0o56264, '', 'XSU,2', 'DDV', kind='interp', line=1350)
W('32,3163', 0o00050, '', '', 'S1', kind='operand', line=1351)
W('32,3164', 0o00013, '', '', '10D', kind='operand', line=1352)
W('32,3165', 0o65257, '', 'SR*', 'PDDL', 'MU**.5/R(T1)=THETA3           B-4/B-5 PL10D', kind='interp', line=1353)
W('32,3166', 0o57170, '', '', '6,2', kind='operand', line=1354)
W('32,3167', 0o03652, '', '', 'MAMAX1', kind='operand', line=1355)
W('32,3170', 0o41406, '', 'PUSH', 'PUSH', 'MAMAX1=MA', kind='interp', line=1356)
W('32,3171', 0o77624, '', 'CALL', kind='interp', line=1357)
W('32,3172', 0o65734, '', '', 'XT1LIM', kind='operand', line=1358)
W('32,3173', 0o41476, '', 'DCOMP', 'PUSH', 'X(T1)MIN                      B5      PL12D', kind='interp', line=1359)
W('32,3174', 0o40476, '', 'DCOMP', 'SR4', kind='interp', line=1360)
W('32,3175', 0o41525, '', 'PDDL', 'PUSH', 'DX(T1)MAX                     B5      PL14D', kind='interp', line=1361)
W('32,3176', 0o03654, '', '', 'MAMAX2', kind='operand', line=1362)
W('32,3177', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=1363)
W('32,3200', 0o65734, '', '', 'XT1LIM', kind='operand', line=1364)
W('32,3201', 0o50125, '', 'PDDL', 'BMN', 'X(T1)MAX                      B5      PL16D', kind='interp', line=1365)
W('32,3202', 0o03730, '', '', 'NN1A', kind='operand', line=1366)
W('32,3203', 0o65206, '', '', 'V2T102', kind='operand', line=1367)
W('32,3204', 0o77650, '', 'GOTO', kind='interp', line=1368)
W('32,3205', 0o65220, '', '', 'V2T110', kind='operand', line=1369)

# PROCEED HERE IF NOT PRECISION COMPUTATION

W('32,3206', 0o77745, 'V2T102', 'DLOAD', kind='interp', line=1373)
W('32,3207', 0o03632, '', '', 'RTEDVD', kind='operand', line=1374)
W('32,3210', 0o52054, '', 'BZE', 'GOTO', kind='interp', line=1375)
W('32,3211', 0o65213, '', '', 'V2T105', kind='operand', line=1376)
W('32,3212', 0o65314, '', '', 'V2T140', kind='operand', line=1377)
W('32,3213', 0o50145, 'V2T105', 'DLOAD', 'BMN', kind='interp', line=1378)
W('32,3214', 0o03757, '', '', 'CFPA', kind='operand', line=1379)
W('32,3215', 0o65314, '', '', 'V2T140', kind='operand', line=1380)
W('32,3216', 0o77650, '', 'GOTO', kind='interp', line=1381)
W('32,3217', 0o65322, '', '', 'V2T145', kind='operand', line=1382)
# Page 920
# DURING A PRECISION TRAJECTORY ITERATION CONSTRAIN THE INDEPENDENT
# VARIABLE TO INSURE THAT ALL CONICS PASS THROUGH RCON ON THE SAME PASS
# THROUGH X(T2)

W('32,3220', 0o47145, 'V2T110', 'DLOAD', 'RTB', kind='interp', line=1388)
W('32,3221', 0o33516, '', '', '1RTEB17', kind='operand', line=1389)
W('32,3222', 0o45565, '', '', 'TPMODE', kind='operand', line=1390)
W('32,3223', 0o65276, '', 'DCOMP', 'PDDL', '-1                            B17     PL19D', kind='interp', line=1391)
W('32,3224', 0o33542, '', '', '2RTEB1', kind='operand', line=1392)
W('32,3225', 0o45257, '', 'SR*', 'DSU', kind='interp', line=1393)
W('32,3226', 0o20601, '', '', '0,1', kind='operand', line=1394)
W('32,3227', 0o00001, '', '', '00D', kind='operand', line=1395)
W('32,3230', 0o53605, '', 'DMP', 'SL*', kind='interp', line=1396)
W('32,3231', 0o00035, '', '', '28D', kind='operand', line=1397)
W('32,3232', 0o20172, '', '', '0 -7,1', kind='operand', line=1398)
W('32,3233', 0o76257, '', 'SL*', 'TAD', kind='interp', line=1399)
W('32,3234', 0o20172, '', '', '0 -7,1', kind='operand', line=1400)
W('32,3235', 0o65234, '', 'RTB', 'PDDL', 'BETA5(2-LAMBDA)-1=BETA6       B17     PL19D', kind='interp', line=1401)
W('32,3236', 0o45565, '', '', 'TPMODE', kind='operand', line=1402)
W('32,3237', 0o03722, '', '', 'X(T1)', kind='operand', line=1403)
W('32,3240', 0o00001, '', 'STORE', '00D', 'X(T1),,                       B5', kind='interp', line=1404)
W('32,3241', 0o77751, '', 'TLOAD', '', '                                      PL16D', kind='interp', line=1405)
W('32,3242', 0o53040, '', 'BMN', 'BZE', kind='interp', line=1406)
W('32,3243', 0o65250, '', '', 'V2T115', kind='operand', line=1407)
W('32,3244', 0o65250, '', '', 'V2T115', kind='operand', line=1408)
W('32,3245', 0o52061, '', 'SL', 'GOTO', kind='interp', line=1409)
W('32,3246', 0o20210, '', '', '7', kind='operand', line=1410)
W('32,3247', 0o65261, '', '', 'V2T120', kind='operand', line=1411)
W('32,3250', 0o50145, 'V2T115', 'DLOAD', 'BMN', kind='interp', line=1412)
W('32,3251', 0o03761, '', '', 'PHI2', kind='operand', line=1413)
W('32,3252', 0o65272, '', '', 'V2T125', kind='operand', line=1414)
W('32,3253', 0o77676, '', 'DCOMP', kind='interp', line=1415)
W('32,3254', 0o17761, '', 'STODL', 'PHI2', kind='interp', line=1416)
W('32,3255', 0o33532, '', '', '10RTE', kind='operand', line=1417)
W('32,3256', 0o03730, '', 'STORE', 'NN1A', kind='interp', line=1418)
W('32,3257', 0o77650, '', 'GOTO', kind='interp', line=1419)
W('32,3260', 0o65272, '', '', 'V2T125', kind='operand', line=1420)
W('32,3261', 0o47166, 'V2T120', 'SQRT', 'RTB', kind='interp', line=1421)
W('32,3262', 0o45716, '', '', 'DPMODE', kind='operand', line=1422)
W('32,3263', 0o50125, '', 'PDDL', 'BMN', 'BETA6**.5=X(T1)LIM            B5      PL18D', kind='interp', line=1423)
W('32,3264', 0o03761, '', '', 'PHI2', kind='operand', line=1424)
W('32,3265', 0o65300, '', '', 'V2T130', kind='operand', line=1425)
W('32,3266', 0o45545, '', 'DLOAD', 'STADR', kind='interp', line=1426)
W('32,3267', 0o77760, '', 'STORE', '14D', 'X(T1)LIM = X(T1)MAX', kind='interp', line=1427)
W('32,3270', 0o77676, '', 'DCOMP', kind='interp', line=1428)
W('32,3271', 0o00013, '', 'STORE', '10D', '-X(T1)LIM = X(T1)MIN', kind='interp', line=1429)
W('32,3272', 0o53145, 'V2T125', 'DLOAD', 'BZE', kind='interp', line=1430)
W('32,3273', 0o03722, '', '', 'X(T1)', kind='operand', line=1431)
W('32,3274', 0o65314, '', '', 'V2T140', kind='operand', line=1432)
W('32,3275', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=1433)
# Page 921
W('32,3276', 0o65314, '', '', 'V2T140', kind='operand', line=1435)
W('32,3277', 0o65322, '', '', 'V2T145', kind='operand', line=1436)
W('32,3300', 0o53145, 'V2T130', 'DLOAD', 'BZE', kind='interp', line=1437)
W('32,3301', 0o03722, '', '', 'X(T1)', kind='operand', line=1438)
W('32,3302', 0o65311, '', '', 'V2T135', kind='operand', line=1439)
W('32,3303', 0o71240, '', 'BMN', 'DLOAD', '                                      PL16D', kind='interp', line=1440)
W('32,3304', 0o65311, '', '', 'V2T135', kind='operand', line=1441)
W('32,3305', 0o77626, '', 'STADR', kind='interp', line=1442)
W('32,3306', 0o77764, '', 'STORE', '10D', 'X(T1)LIM = X(T1)MIN', kind='interp', line=1443)
W('32,3307', 0o77650, '', 'GOTO', kind='interp', line=1444)
W('32,3310', 0o65322, '', '', 'V2T145', kind='operand', line=1445)
W('32,3311', 0o57545, 'V2T135', 'DLOAD', 'DCOMP', '                                      PL16D', kind='interp', line=1446)
W('32,3312', 0o77626, '', 'STADR', kind='interp', line=1447)
W('32,3313', 0o77760, '', 'STORE', '14D', '-X(T1)LIM = X(T1)MAX', kind='interp', line=1448)
W('32,3314', 0o77745, 'V2T140', 'DLOAD', kind='interp', line=1449)
W('32,3315', 0o00013, '', '', '10D', kind='operand', line=1450)
W('32,3316', 0o17722, '', 'STODL', 'X(T1)', 'X(T1)MIN = X(T1)', kind='interp', line=1451)
W('32,3317', 0o00015, '', '', '12D', kind='operand', line=1452)
W('32,3320', 0o52006, '', 'PUSH', 'GOTO', 'DX(T1)MAX = DX(T1)                    PL18D', kind='interp', line=1453)
W('32,3321', 0o65327, '', '', 'V2T150', kind='operand', line=1454)
W('32,3322', 0o77745, 'V2T145', 'DLOAD', kind='interp', line=1455)
W('32,3323', 0o00017, '', '', '14D', kind='operand', line=1456)
W('32,3324', 0o17722, '', 'STODL', 'X(T1)', 'X(T1)MAX = X(T1)', kind='interp', line=1457)
W('32,3325', 0o00015, '', '', '12D', kind='operand', line=1458)
W('32,3326', 0o41476, '', 'DCOMP', 'PUSH', '-DX(T1)MAX = DX(T1)                   PL18D', kind='interp', line=1459)
W('32,3327', 0o77624, 'V2T150', 'CALL', '', 'GOTO X(T1)-DV ITERATOR', kind='interp', line=1460)
W('32,3330', 0o65457, '', '', 'GAMDV10', kind='operand', line=1461)
W('32,3331', 0o53145, '', 'DLOAD', 'BZE', 'EXIT IF MINIMUM FUEL MODE', kind='interp', line=1462)
W('32,3332', 0o03632, '', '', 'RTEDVD', kind='operand', line=1463)
W('32,3333', 0o65455, '', '', 'V2T1X', kind='operand', line=1464)

# CONTINUE IF TIME CRITICAL MODE

W('32,3334', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1468)
W('32,3335', 0o03706, '', '', 'DV', kind='operand', line=1469)
W('32,3336', 0o65341, '', '', 'V2T155', kind='operand', line=1470)
W('32,3337', 0o77650, '', 'GOTO', kind='interp', line=1471)
W('32,3340', 0o65374, '', '', 'V2T175', kind='operand', line=1472)
W('32,3341', 0o50145, 'V2T155', 'DLOAD', 'BMN', kind='interp', line=1473)
W('32,3342', 0o03730, '', '', 'NN1A', kind='operand', line=1474)
W('32,3343', 0o65346, '', '', 'V2T160', kind='operand', line=1475)
W('32,3344', 0o77650, '', 'GOTO', kind='interp', line=1476)
W('32,3345', 0o65416, '', '', 'V2T185', kind='operand', line=1477)

# CONIC TRAJECTORY COMPUTATION

W('32,3346', 0o53145, 'V2T160', 'DLOAD', 'BZE', kind='interp', line=1481)
W('32,3347', 0o03722, '', '', 'X(T1)', kind='operand', line=1482)
W('32,3350', 0o65354, '', '', 'V2T165', kind='operand', line=1483)
W('32,3351', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=1484)
# Page 922
W('32,3352', 0o65354, '', '', 'V2T165', kind='operand', line=1486)
W('32,3353', 0o65453, '', '', 'V2T300', kind='operand', line=1487)
W('32,3354', 0o53145, 'V2T165', 'DLOAD', 'BZE', kind='interp', line=1488)
W('32,3355', 0o03757, '', '', 'CFPA', kind='operand', line=1489)
W('32,3356', 0o65453, '', '', 'V2T300', kind='operand', line=1490)
W('32,3357', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=1491)
W('32,3360', 0o65453, '', '', 'V2T300', kind='operand', line=1492)
W('32,3361', 0o00017, '', '', '14D', kind='operand', line=1493)
W('32,3362', 0o17722, '', 'STODL', 'X(T1)', 'X(T1)MAX=X(T1)', kind='interp', line=1494)
W('32,3363', 0o00015, '', '', '12D', kind='operand', line=1495)
W('32,3364', 0o77676, '', 'DCOMP', kind='interp', line=1496)
W('32,3365', 0o34021, '', 'STCALL', '16D', '-DX(T1)MAX=DX(T1)', kind='interp', line=1497)
W('32,3366', 0o65457, '', '', 'GAMDV10', kind='operand', line=1498)
W('32,3367', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=1499)
W('32,3370', 0o03632, '', '', 'RTEDVD', kind='operand', line=1500)
W('32,3371', 0o03706, '', '', 'DV', kind='operand', line=1501)
W('32,3372', 0o77640, '', 'BMN', kind='interp', line=1502)
W('32,3373', 0o65453, '', '', 'V2T300', kind='operand', line=1503)
W('32,3374', 0o71214, 'V2T175', 'SET', 'DLOAD', kind='interp', line=1504)
W('32,3375', 0o00072, '', '', 'F2RTE', kind='operand', line=1505)
W('32,3376', 0o03722, '', '', 'X(T1)', kind='operand', line=1506)
W('32,3377', 0o77614, '', 'BOFF', kind='interp', line=1507)
W('32,3400', 0o02742, '', '', 'SLOWFLG', kind='operand', line=1508)
W('32,3401', 0o65406, '', '', 'V2T177', kind='operand', line=1509)
W('32,3402', 0o14013, '', 'STODL', '10D', 'X(T1)MIN', kind='interp', line=1510)
W('32,3403', 0o00015, '', '', '12D', 'DX(T1)MAX', kind='operand', line=1511)
W('32,3404', 0o77650, '', 'GOTO', kind='interp', line=1512)
W('32,3405', 0o65411, '', '', 'V2T179', kind='operand', line=1513)
W('32,3406', 0o14017, 'V2T177', 'STODL', '14D', kind='interp', line=1514)
W('32,3407', 0o00015, '', '', '12D', kind='operand', line=1515)
W('32,3410', 0o77676, '', 'DCOMP', kind='interp', line=1516)
W('32,3411', 0o34021, 'V2T179', 'STCALL', '16D', 'DX(T1)', kind='interp', line=1517)
W('32,3412', 0o65457, '', '', 'GAMDV10', kind='operand', line=1518)
W('32,3413', 0o50145, '', 'DLOAD', 'BMN', kind='interp', line=1519)
W('32,3414', 0o03730, '', '', 'NN1A', kind='operand', line=1520)
W('32,3415', 0o65453, '', '', 'V2T300', kind='operand', line=1521)

# PREVENT A LARGE CHANGE IN INDEPENDENT VARIABLE DURING AN ITERATION FOR A
# PRECISION TRAJECTORY

W('32,3416', 0o45345, 'V2T185', 'DLOAD', 'DSU', kind='interp', line=1526)
W('32,3417', 0o03722, '', '', 'X(T1)', kind='operand', line=1527)
W('32,3420', 0o00001, '', '', '00D', kind='operand', line=1528)
W('32,3421', 0o65246, '', 'ABS', 'PDDL', '/X(T1)-X(T1),,/ = BETA7', kind='interp', line=1529)
W('32,3422', 0o00015, '', '', '12D', kind='operand', line=1530)
W('32,3423', 0o44352, '', 'SL1', 'BDSU', kind='interp', line=1531)
W('32,3424', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=1532)
W('32,3425', 0o65453, '', '', 'V2T300', kind='operand', line=1533)
W('32,3426', 0o00001, '', '', '00D', 'CONTINUE IF BETA7 LARGER THAN 2DX(T1)MAX', kind='operand', line=1534)
W('32,3427', 0o03722, '', 'STORE', 'X(T1)', 'X(T1),, = X(T1)', kind='interp', line=1535)
# Page 923
W('32,3430', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1537)
W('32,3431', 0o00017, '', '', '14D', kind='operand', line=1538)
W('32,3432', 0o65440, '', '', 'V2T195', kind='operand', line=1539)
W('32,3433', 0o77745, '', 'DLOAD', kind='interp', line=1540)
W('32,3434', 0o00017, '', '', '14D', kind='operand', line=1541)
W('32,3435', 0o03722, '', 'STORE', 'X(T1)', 'X(T1)MAX = X(T1)', kind='interp', line=1542)
W('32,3436', 0o77650, '', 'GOTO', kind='interp', line=1543)
W('32,3437', 0o65451, '', '', 'V2T205', kind='operand', line=1544)
W('32,3440', 0o45345, 'V2T195', 'DLOAD', 'DSU', kind='interp', line=1545)
W('32,3441', 0o03722, '', '', 'X(T1)', kind='operand', line=1546)
W('32,3442', 0o00013, '', '', '10D', kind='operand', line=1547)
W('32,3443', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=1548)
W('32,3444', 0o65446, '', '', 'V2T200', kind='operand', line=1549)
W('32,3445', 0o65451, '', '', 'V2T205', kind='operand', line=1550)
W('32,3446', 0o77745, 'V2T200', 'DLOAD', kind='interp', line=1551)
W('32,3447', 0o00013, '', '', '10D', kind='operand', line=1552)
W('32,3450', 0o03722, '', 'STORE', 'X(T1)', 'X(T1)MIN = X(T1)', kind='interp', line=1553)
W('32,3451', 0o77624, 'V2T205', 'CALL', kind='interp', line=1554)
W('32,3452', 0o65660, '', '', 'DVCALC', kind='operand', line=1555)
W('32,3453', 0o77745, 'V2T300', 'DLOAD', kind='interp', line=1556)
W('32,3454', 0o33524, '', '', 'ZERORTE', kind='operand', line=1557)
W('32,3455', 0o77650, 'V2T1X', 'GOTO', kind='interp', line=1558)
W('32,3456', 0o00041, '', '', '33D', kind='operand', line=1559)

# Page 924
# X(T1)-DV ITERATOR SUBROUTINE
#
# DESCRIPTION
# COMPUTES A POST IMPULSE VELOCITY VECTOR (V2(T1)) WHICH REQUIRES A MINIMUM DV.
#
# CALLING SEQUENCE
# L       CALL
# L+1             GAMDV10
#
# NORMAL EXIT MODE
# AT L+2 OF CALLING SEQUENCE
#
# ALARM EXIT MODE
# AT V2T1X WITH MPAC = OCTAL 605 FOR EXCESS ITERATIONS
#
# SUBROUTINES CALLED
# DVCALC
#
# ERASABLE INITIALIZATION REQUIRED
# PUSHLIST
# 02D             THETA1=BETA5*LAMBDA-1                                   TP      B17
# 05D             THETA2=2*R(T1)*(LAMBDA-1)                               TP      B38/B36
# 08D             THETA3=MU**.5/R(T1)                                     DP      B-4/B-5
# 10D             X(T1)MIN=LOWER BOUND ON INDEPENDENT VARIABLE X(T1)      DP      B5
# 12D             DX(T1)MAX=MAXIMUM DX(T1)                                DP      B5
# 14D             X(T1)MAX=UPPER BOUND ON INDEPENDENT VARIABLE X(T1)      DP      B5
# 16D             DX(T1)=ITERATOR INCREMENT                               DP      B5
# MPAC
# NONE
# OTHER
# V(T1)/          INITIAL VELOCITY VECTOR                                 VECTOR  B7/B5   METERS/CS
# RTEDVD          DELTA VELOCITY DESIRED                                  DP      B7/B5   METERS/CS
# UR1/            UNIT INITIAL VECTOR                                     VECTOR  B1
# UH/             UNIT HORIZONTAL VECTOR                                  VECTOR  B1
# X(T1)           COTANGENT OF INITIAL FLIGHT PATH ANGLE (FROM VERTICAL)  DP      B5
# F2RTE           TIME CRITICAL OR MINIMUM FUEL MODE INDICATOR            STATE AREA      0 MIN. FUEL, 1 MIN. TIME
#
# OUTPUT
# V2(T1)/         POST IMPULSE INITIAL VELOCITY VECTOR                    VECTOR  B7/B5   METERS/CS
# DV              INITIAL VELOCITY CHANGE                                 DP      B7/B5   METERS/CS
# X(T1)           COTANGENT OF INITIAL FPA MEASURED FROM VERTICAL         DP      B5
# PCON            SEMI-LATUS RECTUM                                       DP      B28/B26 METERS
#
# DEBRIS
# PUSHLIST
# 00D             X(T1),,
# 02D             THETA1
# 05D             THETA2
# 08D             THETA3
# 10D             X(T1)MIN
# 12D             DX(T1)MAX
# Page 925
# 14D             X(T1)MAX
# 16D             DX(T1)
# 22D             DV,=PREVIOUS DV                                         DP      B7/B5
# 24D             BETA9=X(T1)+1.1DX(T1)                                   DP      B5
# 31D             GAMDV10 SUBROUTINE RETURN ADDRESS
# 32D             DVCALC SUBROUTINE RETURN ADDRESS
# 33D             V2T100 SUBROUTINE RETURN ADDRESS

W('32,3457', 0o77620, 'GAMDV10', 'STQ', kind='interp', line=1622)
W('32,3460', 0o00037, '', '', '31D', kind='operand', line=1623)
W('32,3461', 0o45001, '', 'SETPD', 'CALL', kind='interp', line=1624)
W('32,3462', 0o00023, '', '', '18D', '                                      PL18D', kind='operand', line=1625)
W('32,3463', 0o65660, '', '', 'DVCALC', kind='operand', line=1626)
W('32,3464', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=1627)
W('32,3465', 0o00017, '', '', '14D', kind='operand', line=1628)
W('32,3466', 0o00013, '', '', '10D', kind='operand', line=1629)
W('32,3467', 0o77600, '', 'BOV', kind='interp', line=1630)
W('32,3470', 0o65510, '', '', 'GAMDV20', kind='operand', line=1631)
W('32,3471', 0o45206, '', 'PUSH', 'DSU', 'X(T1)MAX-X(T1)MIN=BETA8       B5      PL20D', kind='interp', line=1632)
W('32,3472', 0o33614, '', '', 'EPC9RTE', kind='operand', line=1633)
W('32,3473', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=1634)
W('32,3474', 0o65656, '', '', 'GAMDVX', 'BOUNDS CLOSE TOGETHER', kind='operand', line=1635)
W('32,3475', 0o00023, '', '', '18D', kind='operand', line=1636)
W('32,3476', 0o50025, '', 'DSU', 'BMN', 'BETA8-DX(T1)MAX', kind='interp', line=1637)
W('32,3477', 0o00015, '', '', '12D', kind='operand', line=1638)
W('32,3500', 0o65504, '', '', 'GAMDV15', kind='operand', line=1639)
W('32,3501', 0o52001, '', 'SETPD', 'GOTO', '                                      PL18D', kind='interp', line=1640)
W('32,3502', 0o00023, '', '', '18D', kind='operand', line=1641)
W('32,3503', 0o65510, '', '', 'GAMDV20', kind='operand', line=1642)
W('32,3504', 0o77745, 'GAMDV15', 'DLOAD', '', '                                      PL18D', kind='interp', line=1643)
W('32,3505', 0o70565, '', 'SIGN', 'SR1', kind='interp', line=1644)
W('32,3506', 0o00021, '', '', '16D', kind='operand', line=1645)
W('32,3507', 0o00021, '', 'STORE', '16D', 'BETA8(SIGNDX(T1))/2=DX(T1)', kind='interp', line=1646)
W('32,3510', 0o77745, 'GAMDV20', 'DLOAD', kind='interp', line=1647)
W('32,3511', 0o33526, '', '', 'M144RTE', kind='operand', line=1648)
W('32,3512', 0o03732, '', 'STORE', 'NN2', kind='interp', line=1649)
W('32,3513', 0o43345, 'GAMDV25', 'DLOAD', 'DAD', kind='interp', line=1650)
W('32,3514', 0o03732, '', '', 'NN2', kind='operand', line=1651)
W('32,3515', 0o33522, '', '', '1RTEB28', kind='operand', line=1652)
W('32,3516', 0o67240, '', 'BMN', 'SLOAD', kind='interp', line=1653)
W('32,3517', 0o65523, '', '', 'GAMDV30', kind='operand', line=1654)
W('32,3520', 0o33562, '', '', 'OCT605', kind='operand', line=1655)
W('32,3521', 0o77650, '', 'GOTO', kind='interp', line=1656)
W('32,3522', 0o65455, '', '', 'V2T1X', kind='operand', line=1657)
W('32,3523', 0o03732, 'GAMDV30', 'STORE', 'NN2', 'NN2=NN2+1', kind='interp', line=1658)
W('32,3524', 0o65345, '', 'DLOAD', 'PDDL', 'X(T1)=X(T1),                  B5      PL20D', kind='interp', line=1659)
W('32,3525', 0o03722, '', '', 'X(T1)', kind='operand', line=1660)
W('32,3526', 0o03706, '', '', 'DV', kind='operand', line=1661)
W('32,3527', 0o43325, '', 'PDDL', 'DAD', 'DV=DV,                        B7/B5   PL22D', kind='interp', line=1662)
W('32,3530', 0o03722, '', '', 'X(T1)', kind='operand', line=1663)
W('32,3531', 0o00021, '', '', '16D', kind='operand', line=1664)
# Page 926
W('32,3532', 0o37722, '', 'STCALL', 'X(T1)', 'X(T1)+DX(T1)=X(T1)            B5', kind='interp', line=1666)
W('32,3533', 0o65660, '', '', 'DVCALC', kind='operand', line=1667)
W('32,3534', 0o71214, '', 'BON', 'DLOAD', kind='interp', line=1668)
W('32,3535', 0o00312, '', '', 'F2RTE', kind='operand', line=1669)
W('32,3536', 0o65552, '', '', 'GAMDV35', kind='operand', line=1670)
W('32,3537', 0o03706, '', '', 'DV', kind='operand', line=1671)
W('32,3540', 0o50025, '', 'DSU', 'BMN', 'CONTINUE IF FUEL CRITICAL MODE', kind='interp', line=1672)
W('32,3541', 0o00025, '', '', '20D', kind='operand', line=1673)
W('32,3542', 0o65547, '', '', 'GAMDV33', kind='operand', line=1674)
W('32,3543', 0o57545, 'GAMDV32', 'DLOAD', 'DCOMP', kind='interp', line=1675)
W('32,3544', 0o00021, '', '', '16D', kind='operand', line=1676)
W('32,3545', 0o77742, '', 'SR1', kind='interp', line=1677)
W('32,3546', 0o00021, '', 'STORE', '16D', kind='interp', line=1678)
W('32,3547', 0o52001, 'GAMDV33', 'SETPD', 'GOTO', kind='interp', line=1679)
W('32,3550', 0o00023, '', '', '18D', '                                      PL18D', kind='operand', line=1680)
W('32,3551', 0o65615, '', '', 'GAMDV50', kind='operand', line=1681)

# TIME CRITICAL MODE

W('32,3552', 0o45345, 'GAMDV35', 'DLOAD', 'DSU', kind='interp', line=1685)
W('32,3553', 0o03632, '', '', 'RTEDVD', kind='operand', line=1686)
W('32,3554', 0o03706, '', '', 'DV', kind='operand', line=1687)
W('32,3555', 0o41525, '', 'PDDL', 'PUSH', 'DVD-DV=DVERR                  B7/B5   PL22D', kind='interp', line=1688)
W('32,3556', 0o51545, 'GAMDV40', 'DLOAD', 'ABS', 'DV,                                   PL24D', kind='interp', line=1689)
W('32,3557', 0o00025, '', '', '20D', kind='operand', line=1690)
W('32,3560', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1691)
W('32,3561', 0o33616, '', '', 'EPC10RTE', kind='operand', line=1692)
W('32,3562', 0o65656, '', '', 'GAMDVX', kind='operand', line=1693)
W('32,3563', 0o71204, 'GAMDV45', 'BOVB', 'DLOAD', kind='interp', line=1694)
W('32,3564', 0o57352, '', '', 'TCDANZIG', 'ASSURE OVFIND IS 0', kind='operand', line=1695)
W('32,3565', 0o60221, '', 'BDSU', 'NORM', kind='interp', line=1696)
W('32,3566', 0o03706, '', '', 'DV', kind='operand', line=1697)
W('32,3567', 0o00050, '', '', 'X2', kind='operand', line=1698)
W('32,3570', 0o77725, '', 'PDDL', '', 'DV-DV,                        B7/B5-N2 PL22D', kind='interp', line=1699)
W('32,3571', 0o70501, '', 'NORM', 'SR1', 'DVERR                         B8/B6-N1', kind='interp', line=1700)
W('32,3572', 0o00047, '', '', 'X1', kind='operand', line=1701)
W('32,3573', 0o65271, '', 'DDV', 'PDDL', 'DVERR/ DV - DV', kind='interp', line=1702)
W('32,3574', 0o41221, '', 'BDSU', 'DMP', '                                      PL18D', kind='interp', line=1703)
W('32,3575', 0o03722, '', '', 'X(T1)', kind='operand', line=1704)
W('32,3576', 0o77660, '', 'XSU,1', kind='interp', line=1705)
W('32,3577', 0o00047, '', '', 'X2', kind='operand', line=1706)
W('32,3600', 0o00021, '', 'STORE', '16D', 'PRESERVE SIGN IF OVERFLOW', kind='interp', line=1707)
W('32,3601', 0o40057, '', 'SR*', 'BOV', kind='interp', line=1708)
W('32,3602', 0o20600, '', '', '0 -1,1', kind='operand', line=1709)
W('32,3603', 0o65611, '', '', 'GAMDV47', kind='operand', line=1710)
W('32,3604', 0o00021, '', 'STORE', '16D', '(X(T1)-X(T1),)DVERR/(DV-DV,)=DX(T1)', kind='interp', line=1711)
W('32,3605', 0o45246, '', 'ABS', 'DSU', kind='interp', line=1712)
W('32,3606', 0o00015, '', '', '12D', kind='operand', line=1713)
W('32,3607', 0o77640, '', 'BMN', kind='interp', line=1714)
W('32,3610', 0o65615, '', '', 'GAMDV50', kind='operand', line=1715)
# Page 927
W('32,3611', 0o75345, 'GAMDV47', 'DLOAD', 'SIGN', kind='interp', line=1717)
W('32,3612', 0o00015, '', '', '12D', kind='operand', line=1718)
W('32,3613', 0o00021, '', '', '16D', kind='operand', line=1719)
W('32,3614', 0o00021, '', 'STORE', '16D', 'DX(T1)MAX(SIGNDX(T1))=DX(T1)', kind='interp', line=1720)

# CHECK TO KEEP INDEPENDENT VARIABLE IN BOUNDS

W('32,3615', 0o41345, 'GAMDV50', 'DLOAD', 'DMP', kind='interp', line=1724)
W('32,3616', 0o00021, '', '', '16D', kind='operand', line=1725)
W('32,3617', 0o33536, '', '', '1.1RTEB1', kind='operand', line=1726)
W('32,3620', 0o43352, '', 'SL1', 'DAD', kind='interp', line=1727)
W('32,3621', 0o03722, '', '', 'X(T1)', kind='operand', line=1728)
W('32,3622', 0o00031, '', 'STORE', '24D', 'X(T1)+1.1DX(T1)=BETA9         B5', kind='interp', line=1729)
W('32,3623', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1730)
W('32,3624', 0o00017, '', '', '14D', kind='operand', line=1731)
W('32,3625', 0o65634, '', '', 'GAMDV55', kind='operand', line=1732)
W('32,3626', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=1733)
W('32,3627', 0o00017, '', '', '14D', kind='operand', line=1734)
W('32,3630', 0o03722, '', '', 'X(T1)', kind='operand', line=1735)
W('32,3631', 0o77742, '', 'SR1', kind='interp', line=1736)
W('32,3632', 0o34021, '', 'STCALL', '16D', '(X(T1)MAX-X(T1))/2=DX(T1)     B5', kind='interp', line=1737)
W('32,3633', 0o65647, '', '', 'GAMDV65', kind='operand', line=1738)
W('32,3634', 0o45345, 'GAMDV55', 'DLOAD', 'DSU', kind='interp', line=1739)
W('32,3635', 0o00031, '', '', '24D', kind='operand', line=1740)
W('32,3636', 0o00013, '', '', '10D', kind='operand', line=1741)
W('32,3637', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=1742)
W('32,3640', 0o65642, '', '', 'GAMDV60', kind='operand', line=1743)
W('32,3641', 0o65647, '', '', 'GAMDV65', kind='operand', line=1744)
W('32,3642', 0o45345, 'GAMDV60', 'DLOAD', 'DSU', kind='interp', line=1745)
W('32,3643', 0o00013, '', '', '10D', kind='operand', line=1746)
W('32,3644', 0o03722, '', '', 'X(T1)', kind='operand', line=1747)
W('32,3645', 0o77742, '', 'SR1', kind='interp', line=1748)
W('32,3646', 0o00021, '', 'STORE', '16D', '(X(T1)MIN-X(T1))/2=DX(T1)     B5', kind='interp', line=1749)
W('32,3647', 0o51545, 'GAMDV65', 'DLOAD', 'ABS', kind='interp', line=1750)
W('32,3650', 0o00021, '', '', '16D', kind='operand', line=1751)
W('32,3651', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1752)
W('32,3652', 0o33614, '', '', 'EPC9RTE', kind='operand', line=1753)
W('32,3653', 0o65656, '', '', 'GAMDVX', kind='operand', line=1754)
W('32,3654', 0o77650, '', 'GOTO', kind='interp', line=1755)
W('32,3655', 0o65513, '', '', 'GAMDV25', kind='operand', line=1756)
W('32,3656', 0o77650, 'GAMDVX', 'GOTO', kind='interp', line=1757)
W('32,3657', 0o00037, '', '', '31D', kind='operand', line=1758)

# Page 928
# DV CALCULATION SUBROUTINE
#
# INPUT
# PUSHLIST
# 02D             THETA1=BETA5*LAMBDA-1                                   TP      B17
# 05D             THETA2=2*R(T1)*(LAMBDA-1)                               TP      B38/B36
# 08D             THETA3=MU**.5/R(T1)                                     DP      B-4/B-5
# OTHER
# X(T1)           COTANGENT OF POST IMPULSE INITIAL FLIGHT PATH ANGLE     DP      B5
# V(T1)/          INITIAL VELOCITY VECTOR (PRE IMPULSE)                   VECTOR  B7/B5   METERS/CS
# UR1/            UNIT INITIAL VECTOR                                     VECTOR  B1
# UH/             UNIT HORIZONTAL VECTOR                                  VECTOR  B1
#
# OUTPUT
# V2(T1)/         POST IMPULSE INITIAL VELOCITY VECTOR                    VECTOR  B7/B5   METERS/CS
# DV              INITIAL VELOCITY CHANGE                                 DP      B7/B5   METERS/CS
# PCON            SEMI-LATUS RECTUM                                       DP      B28/B26 METERS
#
# DEBRIS
# 28D             THETA3*PCON**.5                                         DP      B10/B8-N1
# C(PUSHLOC)      THETA3(PCON**.5)*X(T1)*UR1/                             VECTOR  B7/B5
# 32D             DVCALC SUBROUTINE RETURN ADDRESS
# X1              NORMALIZATION FACTOR FOR VALUE IN 28D
#
# PUSHLOC IS RESTORED TO ITS ENTRANCE VALUE UPON EXITING DVCALC

W('32,3660', 0o71220, 'DVCALC', 'STQ', 'DLOAD', kind='interp', line=1787)
W('32,3661', 0o00040, '', '', '32D', kind='operand', line=1788)
W('32,3662', 0o03722, '', '', 'X(T1)', kind='operand', line=1789)
W('32,3663', 0o54316, '', 'DSQ', 'SR', kind='interp', line=1790)
W('32,3664', 0o20610, '', '', '7', kind='operand', line=1791)
W('32,3665', 0o76276, '', 'DCOMP', 'TAD', kind='interp', line=1792)
W('32,3666', 0o00003, '', '', '02D', kind='operand', line=1793)
W('32,3667', 0o41501, '', 'NORM', 'PUSH', kind='interp', line=1794)
W('32,3670', 0o00047, '', '', 'X1', kind='operand', line=1795)
W('32,3671', 0o60351, '', 'TLOAD', 'NORM', kind='interp', line=1796)
W('32,3672', 0o00006, '', '', '05D', kind='operand', line=1797)
W('32,3673', 0o00050, '', '', 'X2', kind='operand', line=1798)
W('32,3674', 0o70434, '', 'RTB', 'SR1', kind='interp', line=1799)
W('32,3675', 0o45716, '', '', 'DPMODE', kind='operand', line=1800)
W('32,3676', 0o56264, '', 'XSU,2', 'DDV', kind='interp', line=1801)
W('32,3677', 0o00046, '', '', 'X1', kind='operand', line=1802)
W('32,3700', 0o77657, '', 'SR*', kind='interp', line=1803)
W('32,3701', 0o57170, '', '', '6,2', kind='operand', line=1804)
W('32,3702', 0o03720, '', 'STORE', 'PCON', 'THETA2/(THETA1-X(T1)**2)=PCON B28/26', kind='interp', line=1805)
W('32,3703', 0o41366, '', 'SQRT', 'DMP', kind='interp', line=1806)
W('32,3704', 0o00011, '', '', '08D', kind='operand', line=1807)
W('32,3705', 0o77701, '', 'NORM', kind='interp', line=1808)
W('32,3706', 0o00047, '', '', 'X1', kind='operand', line=1809)
W('32,3707', 0o14035, '', 'STODL', '28D', 'THETA3*PCON**.5               B10/B8 -N1', kind='interp', line=1810)
# Page 929
W('32,3710', 0o03722, '', '', 'X(T1)', kind='operand', line=1812)
W('32,3711', 0o74301, '', 'NORM', 'VXSC', kind='interp', line=1813)
W('32,3712', 0o00050, '', '', 'X2', kind='operand', line=1814)
W('32,3713', 0o03740, '', '', 'UR1/', 'X(T1)*UR1/                    B5+B1 -N2', kind='operand', line=1815)
W('32,3714', 0o74274, '', 'XAD,2', 'VXSC', kind='interp', line=1816)
W('32,3715', 0o00046, '', '', 'X1', kind='operand', line=1817)
W('32,3716', 0o00035, '', '', '28D', kind='operand', line=1818)
W('32,3717', 0o63257, '', 'VSR*', 'PDVL', 'THETA3(PCON**.5)X(T1)*UR1/    B7/B5', kind='interp', line=1819)
W('32,3720', 0o57207, '', '', '0 -9D,2', '              +', kind='operand', line=1820)
W('32,3721', 0o03746, '', '', 'UH/', kind='operand', line=1821)
W('32,3722', 0o53761, '', 'VXSC', 'VSR*', 'THETA3(PCON**.5)UH/           B7/B5', kind='interp', line=1822)
W('32,3723', 0o00035, '', '', '28D', kind='operand', line=1823)
W('32,3724', 0o20575, '', '', '0 -4,1', '              =', kind='operand', line=1824)
W('32,3725', 0o45455, '', 'VAD', 'STADR', kind='interp', line=1825)
W('32,3726', 0o74077, '', 'STORE', 'V2(T1)/', 'V2(T1)/                       B7/B5', kind='interp', line=1826)
W('32,3727', 0o51451, '', 'VSU', 'ABVAL', kind='interp', line=1827)
W('32,3730', 0o03672, '', '', 'V(T1)/', kind='operand', line=1828)
W('32,3731', 0o03706, '', 'STORE', 'DV', 'ABVAL(V2(T1)/-V1(T)/)=DV      B7/B5', kind='interp', line=1829)
W('32,3732', 0o77650, '', 'GOTO', kind='interp', line=1830)
W('32,3733', 0o00040, '', '', '32D', kind='operand', line=1831)

# Page 930
# SUBROUTINE TO COMPUTE BOUNDS ON INDEPENDENT VARIABLE X(T1)
#
# INPUT
# PUSHLIST
# PUSHLOC -4      MAJOR AXIS (MA)                                         DP      B30/B28
# PUSHLOC -2      MAJOR AXIS (MA) AGAIN                                   DP      B30/B28
# 28D             BETA5=LAMBDA*BETA1                                      DP      B9
# OTHER
# RCON                                                                    DP      B29/B27
# R(T1)                                                                   DP      B29/B27
#
# OUTPUT
# MPAC
# X(T1)LIM        LIMIT ON INDEPENDENT VARIABLE X(T1)                     DP      B5
#
# DEBRIS
# PUSHLIST
# C(PUSHLOC)      MA-RCON                                                 DP      (B30/28)-N1
# C(PUSHLOC) +2   MA                                                      DP      B30/B28
# X1              NORMALIZATION FACTOR FOR MA-RCON
# 20D             XT1LIM SUBROUTINE RETURN ADDRESS
#
# PUSHLOC IS RESTORED TO ITS ENTRANCE VALUE UPON EXITING XT1LIM

W('32,3734', 0o71220, 'XT1LIM', 'STQ', 'DLOAD', kind='interp', line=1858)
W('32,3735', 0o00024, '', '', '20D', kind='operand', line=1859)
W('32,3736', 0o03636, '', '', 'RCON', kind='operand', line=1860)
W('32,3737', 0o44342, '', 'SR1', 'BDSU', kind='interp', line=1861)
W('32,3740', 0o65301, '', 'NORM', 'PDDL', 'MA-RCON                       B30-N1', kind='interp', line=1862)
W('32,3741', 0o00050, '', '', 'X2', kind='operand', line=1863)
W('32,3742', 0o70525, '', 'PDDL', 'SR1', kind='interp', line=1864)
W('32,3743', 0o03646, '', '', 'R(T1)', kind='operand', line=1865)
W('32,3744', 0o56221, '', 'BDSU', 'DDV', kind='interp', line=1866)
W('32,3745', 0o41257, '', 'SL*', 'DMP', kind='interp', line=1867)
W('32,3746', 0o57601, '', '', '0 -3,2', kind='operand', line=1868)
W('32,3747', 0o00035, '', '', '28D', kind='operand', line=1869)
W('32,3750', 0o45257, '', 'SL*', 'DSU', 'BETA10=BETA5(MA-RT)/(MA-RC)-1 B11', kind='interp', line=1870)
W('32,3751', 0o20173, '', '', '0 -6,1', kind='operand', line=1871)
W('32,3752', 0o33521, '', '', '1RTEB25 +1', '1.0                           B-11', kind='operand', line=1872)
W('32,3753', 0o40152, '', 'SL1', 'BOV', kind='interp', line=1873)
W('32,3754', 0o65760, '', '', 'XT1LIM2', kind='operand', line=1874)
W('32,3755', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=1875)
W('32,3756', 0o65764, '', '', 'XT1LIM5', kind='operand', line=1876)
W('32,3757', 0o65762, '', '', 'XT1LIM3', kind='operand', line=1877)
W('32,3760', 0o77745, 'XT1LIM2', 'DLOAD', '', 'BETA10=POSMAX IF OVERFLOW', kind='interp', line=1878)
W('32,3761', 0o33542, '', '', '2RTEB1', kind='operand', line=1879)
W('32,3762', 0o52166, 'XT1LIM3', 'SQRT', 'GOTO', 'X(T1)=SQRT(BETA10)', kind='interp', line=1880)
W('32,3763', 0o65766, '', '', 'XT1LIMX', kind='operand', line=1881)
W('32,3764', 0o77745, 'XT1LIM5', 'DLOAD', kind='interp', line=1882)
W('32,3765', 0o33524, '', '', 'ZERORTE', kind='operand', line=1883)
W('32,3766', 0o77650, 'XT1LIMX', 'GOTO', kind='interp', line=1884)
W('32,3767', 0o00024, '', '', '20D', kind='operand', line=1885)

# Page 931
# CONSTANTS FOR THE P37 AND P70 PROGRAMS AND SUBROUTINES

#   BANK 36
#   SETLOC RTECON1
#   BANK

W('35,3477', 0o20000, '1RTEB1', '2DEC', '1. B-1', kind='data', line=1894)
W('35,3500', 0o00000, kind='data', line=1894)
W('35,3501', 0o10000, '1RTEB2', '2DEC', '1. B-2', kind='data', line=1895)
W('35,3502', 0o00000, kind='data', line=1895)
W('35,3503', 0o04000, '1RTEB3', '2DEC', '1. B-3', kind='data', line=1896)
W('35,3504', 0o00000, kind='data', line=1896)
W('35,3505', 0o02000, '1RTEB4', '2DEC', '1. B-4', kind='data', line=1897)
W('35,3506', 0o00000, kind='data', line=1897)
W('35,3507', 0o00020, '1RTEB10', '2DEC', '1. B-10', kind='data', line=1898)
W('35,3510', 0o00000, kind='data', line=1898)
W('35,3511', 0o00004, '1RTEB12', '2DEC', '1. B-12', kind='data', line=1899)
W('35,3512', 0o00000, kind='data', line=1899)
W('35,3513', 0o00002, '1RTEB13', '2DEC', '1. B-13', kind='data', line=1900)
W('35,3514', 0o00000, kind='data', line=1900)
W('35,3515', 0o00000, '1RTEB17', '2DEC', '1. B-17', kind='data', line=1901)
W('35,3516', 0o04000, kind='data', line=1901)
W('35,3517', 0o00000, '1RTEB25', '2DEC', '1. B-25', kind='data', line=1902)
W('35,3520', 0o00010, kind='data', line=1902)
# * * B25 AND B28 MUST BE CONSECUTIVE * *
W('35,3521', 0o00000, '1RTEB28', '2DEC', '1. B-28', kind='data', line=1904)
W('35,3522', 0o00001, kind='data', line=1904)
W('35,3523', 0o00000, 'ZERORTE', '2DEC', '0', kind='data', line=1905)
W('35,3524', 0o00000, kind='data', line=1905)
W('35,3525', 0o77777, 'M144RTE', '2DEC', '-144. B-28', kind='data', line=1906)
W('35,3526', 0o77557, kind='data', line=1906)
W('35,3527', 0o77777, 'M15RTE', '2DEC', '-15', kind='data', line=1907)
W('35,3530', 0o77760, kind='data', line=1907)
W('35,3531', 0o00000, '10RTE', '2DEC', '10', kind='data', line=1908)
W('35,3532', 0o00012, kind='data', line=1908)
W('35,3533', 0o54631, 'M.6RTE', '2DEC', '-.6', kind='data', line=1909)
W('35,3534', 0o63145, kind='data', line=1909)
W('35,3535', 0o21463, '1.1RTEB1', '2DEC', '1.1 B-1', kind='data', line=1910)
W('35,3536', 0o06315, kind='data', line=1910)
W('35,3537', 0o77777, 'M6RTEB28', '2DEC', '-6', kind='data', line=1911)
W('35,3540', 0o77771, kind='data', line=1911)
W('35,3541', 0o37777, '2RTEB1', '2OCT', '3777737777', kind='data', line=1912)
W('35,3542', 0o37777, kind='data', line=1912)
W('35,3543', 0o77777, 'M9RTEB28', '2DEC', '-9', kind='data', line=1913)
W('35,3544', 0o77766, kind='data', line=1913)
W('35,3545', 0o77777, 'M8RTEB28', '2DEC', '-8', kind='data', line=1914)
W('35,3546', 0o77767, kind='data', line=1914)
W('35,3547', 0o00000, '30480RTE', '2DEC', '30480. B-29', kind='data', line=1915)
W('35,3550', 0o35610, kind='data', line=1915)
W('35,3551', 0o37405, 'VCSPS', '2DEC', '31.510396 B-5', '(SEE 2VEXHUST)', kind='data', line=1916)
W('35,3552', 0o12250, kind='data', line=1916)
# Page 932
W('35,3553', 0o33041, 'VCRCS', '2DEC', '27.0664 B-5', kind='data', line=1918)
W('35,3554', 0o37714, kind='data', line=1918)
W('35,3555', 0o00003, 'MDOTRCS', '2DEC', '.0016375 B-3', kind='data', line=1919)
W('35,3556', 0o13241, kind='data', line=1919)
W('35,3557', 0o20000, 'CSUBT', '2DEC', '.5', kind='data', line=1920)
W('35,3560', 0o00000, kind='data', line=1920)
W('35,3561', 0o00605, 'OCT605', 'OCT', '00605', kind='data', line=1921)
W('35,3562', 0o00612, 'OCT612', 'OCT', '00612', kind='data', line=1922)
W('35,3563', 0o40214, 'MCOS7.5', '2DEC', '-.99144486', kind='data', line=1923)
W('35,3564', 0o45266, kind='data', line=1923)
W('35,3565', 0o73645, 'MSIN7.5', '2DEC', '-.13052619', kind='data', line=1924)
W('35,3566', 0o56536, kind='data', line=1924)
W('35,3567', 0o70467, 'MCOS22.5', '2DEC', '-.92387953 B-2', kind='data', line=1925)
W('35,3570', 0o71205, kind='data', line=1925)
W('35,3571', 0o16525, 'THETA165', '2DEC', '.4583333333', kind='data', line=1926)
W('35,3572', 0o12525, kind='data', line=1926)
W('35,3573', 0o22525, 'THETA210', '2DEC', '.5833333333', kind='data', line=1927)
W('35,3574', 0o12525, kind='data', line=1927)
W('35,3575', 0o17775, 'EPC1RTE', '2DEC', '.99966 B-1', kind='data', line=1928)
W('35,3576', 0o06676, kind='data', line=1928)
W('35,3577', 0o00000, 'EPC2RTE', '2DEC', '100. B-29', kind='data', line=1929)
W('35,3600', 0o00062, kind='data', line=1929)
W('35,3601', 0o00020, 'EPC3RTE', '2DEC', '.001', kind='data', line=1930)
W('35,3602', 0o14223, kind='data', line=1930)
W('35,3603', 0o00000, 'EPC4RTE', '2DEC', '.00001', kind='data', line=1931)
W('35,3604', 0o05174, kind='data', line=1931)
W('35,3605', 0o00002, 'EPC5RTE', '2DEC', '.01 B-6', kind='data', line=1932)
W('35,3606', 0o21727, kind='data', line=1932)
W('35,3607', 0o00000, 'EPC6RTE', '2DEC', '.000007 B-1', kind='data', line=1933)
W('35,3610', 0o01654, kind='data', line=1933)
W('35,3611', 0o00000, 'EPC7RTE', '2DEC', '1000. B-29', kind='data', line=1934)
W('35,3612', 0o00764, kind='data', line=1934)
W('35,3613', 0o00000, 'EPC9RTE', '2DEC', '1. B-25', kind='data', line=1935)
W('35,3614', 0o00010, kind='data', line=1935)
W('35,3615', 0o00000, 'EPC10RTE', '2DEC', '.0001 B-7', kind='data', line=1936)
W('35,3616', 0o00322, kind='data', line=1936)

#   BANK 35
#   SETLOC RTECON1
#   BANK

W('35,3617', 0o75725, 'C4RTE', '2DEC', '-6.986643 E7 B-30', kind='data', line=1942)
W('35,3620', 0o75417, kind='data', line=1942)
W('35,3621', 0o00325, 'K1RTE', '2DEC', '7. E6 B-29', kind='data', line=1943)
W('35,3622', 0o23740, kind='data', line=1943)
W('35,3623', 0o00306, 'K2RTE', '2DEC', '6495000. B-29', kind='data', line=1944)
W('35,3624', 0o06614, kind='data', line=1944)
W('35,3625', 0o76027, 'K3RTE', '2DEC', '-.06105', kind='data', line=1945)
W('35,3626', 0o70156, kind='data', line=1945)
W('35,3627', 0o74517, 'K4RTE', '2DEC', '-.10453', kind='data', line=1946)
W('35,3630', 0o54131, kind='data', line=1946)
W('35,3631', 0o30276, 'RTMURTE', '2DEC', '199650.501 B-18', kind='data', line=1947)
W('35,3632', 0o05001, kind='data', line=1947)
# Page 933
W('35,3633', 0o00003, 'E3RTE', '2DEC', '121920. B-29', kind='data', line=1949)
W('35,3634', 0o27040, kind='data', line=1949)
