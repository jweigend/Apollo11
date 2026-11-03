"""LATITUDE_LONGITUDE_SUBROUTINES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/LATITUDE_LONGITUDE_SUBROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1133-1139 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('LATITUDE_LONGITUDE_SUBROUTINES', 'LATITUDE_LONGITUDE_SUBROUTINES.agc', 'Luminary099', pages='1133-1139')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     LATITUDE_LONGITUDE_SUBROUTINES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
#
# Assembler:    yaYUL
# Contact:      Jim Lawton <jim DOT lawton AT gmail DOT com>
# Website:      www.ibiblio.org/apollo.
# Pages:        1133-1139
# Mod history:  2009-05-28 JL   Updated from page images.
# 2011-01-06 JL   Fixed interpretive indentation.
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

# Page 1133
# SUBROUTINE TO CONVERT RAD VECTOR AT GIVEN TIME TO LAT,LONG AND ALT
#
# CALLING SEQUENCE
#
# L-1    CALL
# L             LAT-LONG
# SUBROUTINES USED
#
# R-TO-RP,ARCTAN,SETGAMMA,SETRE
# ERASABLE INIT. REQ.
#
# AXO,-AYO,AZO,TEPHEM (SET AT LAUNCH TIME)
# ALPHAV = POSITION VECTOR METERS B-29
# MPAC-- TIME  (CSECS B-28)
# ERADFLAG =1, TO COMPUTE EARTH RADIUS, =0 FOR FIXED EARTH RADIUS
# LUNAFLAG=0 FOR EARTH,1 FOR MOON
# OUTPUT
#
# LATITUDE IN LAT   (REVS. B-0)
# LONGITUDE IN LONG   (REVS. B-0)
# ALTITUDE IN ALT METERS B-29
#   BANK 30
#   SETLOC LATLONG
#   BANK

#   COUNT* $$/LT-LG
#   EBANK= ALPHAV
W('13,2351', 0o40220, 'LAT-LONG', 'STQ', 'SETPD', kind='interp', line=56)
W('13,2352', 0o03674, '', '', 'INCORPEX', kind='operand', line=57)
W('13,2353', 0o00001, '', '', '0D', kind='operand', line=58)
W('13,2354', 0o24007, '', 'STOVL', '6D', 'SAVE TIME IN 6-7D FOR R-TO-RP', kind='interp', line=59)
W('13,2355', 0o02032, '', '', 'ALPHAV', kind='operand', line=60)
W('13,2356', 0o51406, '', 'PUSH', 'ABVAL', '0-5D= R FOR R-TO-RP', kind='interp', line=61)
W('13,2357', 0o16070, '', 'STODL', 'ALPHAM', 'ABS. VALUE OF R FOR ALT FORMULA BELOW', kind='interp', line=62)
W('13,2360', 0o24007, '', '', 'ZEROVEC', 'SET MPAC=0 FOR EARTH,NON-ZERO FOR MOON', kind='operand', line=63)
W('13,2361', 0o71414, '', 'BOFF', 'COS', 'USE COS(0) TO GET NON-ZERO IN MPAC', kind='interp', line=64)
W('13,2362', 0o01743, '', '', 'LUNAFLAG', '0=EARTH,1=MOON', kind='operand', line=65)
W('13,2363', 0o26364, '', '', 'CALLRTRP', kind='operand', line=66)
W('13,2364', 0o77624, 'CALLRTRP', 'CALL', kind='interp', line=67)
W('13,2365', 0o51670, '', '', 'R-TO-RP', 'RP VECTOR CONVERTED FROM R B-29', kind='operand', line=68)
W('13,2366', 0o77656, '', 'UNIT', '', 'UNIT RP B-1', kind='interp', line=69)
W('13,2367', 0o36032, '', 'STCALL', 'ALPHAV', 'U2= 1/2 SINL FOR SETRE SUBR BELOW', kind='interp', line=70)
W('13,2370', 0o26550, '', '', 'SETGAMMA', ' SET GAMMA=B2/A2 FOR EARTH,=1 FOR MOON', kind='operand', line=71)
W('13,2371', 0o77624, '', 'CALL', '', ' SCALED B-1', kind='interp', line=72)
W('13,2372', 0o26560, '', '', 'SETRE', 'CALC RE METERS B-29', kind='operand', line=73)
W('13,2373', 0o63545, '', 'DLOAD', 'DSQ', kind='interp', line=74)
W('13,2374', 0o02032, '', '', 'ALPHAV', kind='operand', line=75)
W('13,2375', 0o63525, '', 'PDDL', 'DSQ', kind='interp', line=76)
W('13,2376', 0o02034, '', '', 'ALPHAV +2', kind='operand', line=77)
W('13,2377', 0o75415, '', 'DAD', 'SQRT', kind='interp', line=78)
# Page 1134
W('13,2400', 0o76405, '', 'DMP', 'SL1R', kind='interp', line=80)
W('13,2401', 0o00011, '', '', 'GAMRP', kind='operand', line=81)
W('13,2402', 0o14021, '', 'STODL', 'COSTH', 'COS(LAT) B-1', kind='interp', line=82)
W('13,2403', 0o02036, '', '', 'ALPHAV +4', kind='operand', line=83)
W('13,2404', 0o34023, '', 'STCALL', 'SINTH', 'SIN(LAT) B-1', kind='interp', line=84)
W('13,2405', 0o26510, '', '', 'ARCTAN', kind='operand', line=85)
W('13,2406', 0o15121, '', 'STODL', 'LAT', 'LAT B0', kind='interp', line=86)
W('13,2407', 0o02032, '', '', 'ALPHAV', kind='operand', line=87)
W('13,2410', 0o14021, '', 'STODL', 'COSTH', 'COS(LONG) B-1', kind='interp', line=88)
W('13,2411', 0o02034, '', '', 'ALPHAV +2', kind='operand', line=89)
W('13,2412', 0o34023, '', 'STCALL', 'SINTH', 'SIN(LONG) B-1', kind='interp', line=90)
W('13,2413', 0o26510, '', '', 'ARCTAN', kind='operand', line=91)
W('13,2414', 0o15123, '', 'STODL', 'LONG', 'LONG. REVS B-0 IN RANGE -1/2 TO 1/2', kind='interp', line=92)
W('13,2415', 0o02070, '', '', 'ALPHAM', kind='operand', line=93)
W('13,2416', 0o77625, '', 'DSU', '', 'ALT= R-RE METERS B-29', kind='interp', line=94)
W('13,2417', 0o03673, '', '', 'ERADM', kind='operand', line=95)
W('13,2420', 0o35125, '', 'STCALL', 'ALT', 'EXIT WITH ALT METERS B-29', kind='interp', line=96)
W('13,2421', 0o03674, '', '', 'INCORPEX', kind='operand', line=97)
# Page 1135
# SUBROUTINE TO CONVERT LAT,LONG,ALT AT GIVEN TIME TO RADIUS VECTOR
# CALLING SEQUENCE
#
# L-1    CALL
# L             LALOTORV
# SUBROUTINES USED
#
# SETGAMMA,SETRE,RP-TO-R
# ERASABLE INIT. REQ.
#
# AXO,AYO,AZO,TEPHEM  SET AT LAUNCH TIME
# LAT-- LATITUDE  (REVS B0)
# LONG-- LONGITUDE  (REVS B0)
# ALT--ALTITUDE (METERS) B-29
# MPAC-- TIME  (CSECS B-28)
# ERADFLAG =1 TO COMPUTE EARTH RADIUS, =0 FOR FIXED EARTH RADIUS
# LUNAFLAG=0 FOR EARTH,1 FOR MOON
# OUTPUT
#
# R-VECTOR IN ALPHAV (METERS B-29)
W('13,2422', 0o40220, 'LALOTORV', 'STQ', 'SETPD', 'LAT,LONG,ALT TO R VECTOR', kind='interp', line=119)
W('13,2423', 0o03674, '', '', 'INCORPEX', kind='operand', line=120)
W('13,2424', 0o00001, '', '', '0D', kind='operand', line=121)
W('13,2425', 0o34007, '', 'STCALL', '6D', '6-7D= TIME FOR RP-TO-R', kind='interp', line=122)
W('13,2426', 0o26550, '', '', 'SETGAMMA', 'GAMMA=B2/A2 FOR EARTH,1 FOR MOON B-1', kind='operand', line=123)
W('13,2427', 0o73545, '', 'DLOAD', 'SIN', '              COS(LONG)COS(LAT) IN MPAC', kind='interp', line=124)
W('13,2430', 0o01121, '', '', 'LAT', '    UNIT RP=  SIN(LONG)COS(LAT)    2-3D', kind='operand', line=125)
W('13,2431', 0o65275, '', 'DMPR', 'PDDL', 'PD 2          GAMMA*SIN(LAT)       0-1D', kind='interp', line=126)
W('13,2432', 0o00011, '', '', 'GAMRP', kind='operand', line=127)
W('13,2433', 0o01121, '', '', 'LAT', '        0-1D= GAMMA*SIN(LAT) B-2', kind='operand', line=128)
W('13,2434', 0o65346, '', 'COS', 'PDDL', 'PD4      2-3D=COS(LAT) B-1 TEMPORARILY', kind='interp', line=129)
W('13,2435', 0o01123, '', '', 'LONG', kind='operand', line=130)
W('13,2436', 0o57356, '', 'SIN', 'DMPR', 'PD 2', kind='interp', line=131)
W('13,2437', 0o71525, '', 'PDDL', 'COS', 'PD 4    2-3D=SIN(LONG)COS(LAT) B-2', kind='interp', line=132)
W('13,2440', 0o01121, '', '', 'LAT', kind='operand', line=133)
W('13,2441', 0o71525, '', 'PDDL', 'COS', 'PD 6     4-5D=COS(LAT) B-1 TEMPORARILY', kind='interp', line=134)
W('13,2442', 0o01123, '', '', 'LONG', kind='operand', line=135)
W('13,2443', 0o55475, '', 'DMPR', 'VDEF', 'PD 4   MPAC=  COS(LONG)COS(LAT) B-2', kind='interp', line=136)
W('13,2444', 0o41456, '', 'UNIT', 'PUSH', '0-5D= UNIT RP FOR RP-TO-R SUBR.', kind='interp', line=137)
W('13,2445', 0o36032, '', 'STCALL', 'ALPHAV', 'ALPHAV +4= SINL FOR SETRE SUBR.', kind='interp', line=138)
W('13,2446', 0o26560, '', '', 'SETRE', 'RE METERS B-29', kind='operand', line=139)
W('13,2447', 0o43145, '', 'DLOAD', 'BOFF', 'SET MPAC=0 FOR EARTH,NON-ZERO FOR MOON', kind='interp', line=140)
W('13,2450', 0o24007, '', '', 'ZEROVEC', kind='operand', line=141)
W('13,2451', 0o01743, '', '', 'LUNAFLAG', kind='operand', line=142)
W('13,2452', 0o26454, '', '', 'CALLRPRT', kind='operand', line=143)
W('13,2453', 0o77746, '', 'COS', '', 'USE COS(0) TO GET NON-ZERO IN MPAC', kind='interp', line=144)
W('13,2454', 0o77624, 'CALLRPRT', 'CALL', kind='interp', line=145)
W('13,2455', 0o55716, '', '', 'RP-TO-R', 'EXIT WITH UNIT R VECTOR IN MPAC', kind='operand', line=146)
W('13,2456', 0o16032, '', 'STODL', 'ALPHAV', kind='interp', line=147)
W('13,2457', 0o03673, '', '', 'ERADM', kind='operand', line=148)
# Page 1136
W('13,2460', 0o74215, '', 'DAD', 'VXSC', '(RE + ALT)(UNIT R) METERS B-30', kind='interp', line=150)
W('13,2461', 0o01125, '', '', 'ALT', kind='operand', line=151)
W('13,2462', 0o02032, '', '', 'ALPHAV', kind='operand', line=152)
W('13,2463', 0o77772, '', 'VSL1', '', 'R METERS B-29', kind='interp', line=153)
W('13,2464', 0o36032, '', 'STCALL', 'ALPHAV', 'EXIT WITH R IN METERS B-29', kind='interp', line=154)
W('13,2465', 0o03674, '', '', 'INCORPEX', kind='operand', line=155)
# SUBROUTINE TO COMPUTE EARTH RADIUS
#
# INPUT
#
# 1/2 SIN LAT IN ALPHAV +4
#
# OUTPUT
#
# EARTH RADIUS IN ERADM AND MPAC (METERS B-29)

W('13,2466', 0o63545, 'GETERAD', 'DLOAD', 'DSQ', kind='interp', line=166)
W('13,2467', 0o02036, '', '', 'ALPHAV +4', 'SIN**2(L)', kind='operand', line=167)
W('13,2470', 0o44352, '', 'SL1', 'BDSU', kind='interp', line=168)
W('13,2471', 0o24005, '', '', 'DP1/2', 'COS**2(L)', kind='operand', line=169)
W('13,2472', 0o44275, '', 'DMPR', 'BDSU', kind='interp', line=170)
W('13,2473', 0o26507, '', '', 'EE', kind='operand', line=171)
W('13,2474', 0o24005, '', '', 'DP1/2', kind='operand', line=172)
W('13,2475', 0o75465, '', 'BDDV', 'SQRT', kind='interp', line=173)
W('13,2476', 0o26503, '', '', 'B2XSC', kind='operand', line=174)
W('13,2477', 0o77622, '', 'SR4R', kind='interp', line=175)
W('13,2500', 0o03673, '', 'STORE', 'ERADM', kind='interp', line=176)
W('13,2501', 0o77616, '', 'RVQ', kind='interp', line=177)

# THE FOLLOWING CONSTANTS WERE COMPUTED WITH A=6378166,B=6356784 METERS
# B2XSC= B**2 SCALED B-51
# B2/A2= B**2/A**2 SCALED B-1
# EE=(1-B**2/A**2) SCALED B-0
W('13,2502', 0o00446, 'B2XSC', '2DEC', '.0179450689', 'B**2 SCALED B-51', kind='data', line=183)
W('13,2503', 0o00305, kind='data', line=183)
S('DP1/2', 'equals', 0o34004, line=184)
W('13,2504', 0o17711, 'B2/A2', '2DEC', '.9933064884 B-1', 'GAMMA= B**2/A**2 B-1', kind='data', line=185)
W('13,2505', 0o05254, kind='data', line=185)
W('13,2506', 0o00155, 'EE', '2DEC', '6.6935116 E-3', '(1-B**2/A**2) B-0', kind='data', line=186)
W('13,2507', 0o25250, kind='data', line=186)

# Page 1137
# ARCTAN SUBROUTINE
#
# CALLING SEQUENCE
#
# SIN THETA IN SINTH B-1
# COS THETA IN COSTH B-1
# CALL ARCTAN
#
# OUTPUT
# ARCTAN THETA IN MPAC AND THETA B-0 IN RANGE -1/2 TO +1/2

W('13,2510', 0o77600, 'ARCTAN', 'BOV', kind='interp', line=200)
W('13,2511', 0o26512, '', '', 'CLROVFLW', kind='operand', line=201)
W('13,2512', 0o63545, 'CLROVFLW', 'DLOAD', 'DSQ', kind='interp', line=202)
W('13,2513', 0o00023, '', '', 'SINTH', kind='operand', line=203)
W('13,2514', 0o63525, '', 'PDDL', 'DSQ', kind='interp', line=204)
W('13,2515', 0o00021, '', '', 'COSTH', kind='operand', line=205)
W('13,2516', 0o77615, '', 'DAD', kind='interp', line=206)
W('13,2517', 0o75454, '', 'BZE', 'SQRT', kind='interp', line=207)
W('13,2520', 0o26536, '', '', 'ARCTANXX', 'ATAN=0/0  SET THETA=0', kind='operand', line=208)
W('13,2521', 0o40065, '', 'BDDV', 'BOV', kind='interp', line=209)
W('13,2522', 0o00023, '', '', 'SINTH', kind='operand', line=210)
W('13,2523', 0o26543, '', '', 'ATAN=90', kind='operand', line=211)
W('13,2524', 0o67542, '', 'SR1', 'ASIN', kind='interp', line=212)
W('13,2525', 0o00025, '', 'STORE', 'THETA', kind='interp', line=213)
W('13,2526', 0o50125, '', 'PDDL', 'BMN', kind='interp', line=214)
W('13,2527', 0o00021, '', '', 'COSTH', kind='operand', line=215)
W('13,2530', 0o26532, '', '', 'NEGCOS', kind='operand', line=216)
W('13,2531', 0o43545, '', 'DLOAD', 'RVQ', kind='interp', line=217)
W('13,2532', 0o57545, 'NEGCOS', 'DLOAD', 'DCOMP', kind='interp', line=218)
W('13,2533', 0o43244, '', 'BPL', 'DAD', kind='interp', line=219)
W('13,2534', 0o26540, '', '', 'NEGOUT', kind='operand', line=220)
W('13,2535', 0o24005, '', '', 'DP1/2', kind='operand', line=221)
W('13,2536', 0o00025, 'ARCTANXX', 'STORE', 'THETA', kind='interp', line=222)
W('13,2537', 0o77616, '', 'RVQ', kind='interp', line=223)

W('13,2540', 0o52025, 'NEGOUT', 'DSU', 'GOTO', kind='interp', line=225)
W('13,2541', 0o24005, '', '', 'DP1/2', kind='operand', line=226)
W('13,2542', 0o26536, '', '', 'ARCTANXX', kind='operand', line=227)
W('13,2543', 0o75345, 'ATAN=90', 'DLOAD', 'SIGN', kind='interp', line=228)
W('13,2544', 0o11037, '', '', 'LODP1/4', kind='operand', line=229)
W('13,2545', 0o00023, '', '', 'SINTH', kind='operand', line=230)
W('13,2546', 0o00025, '', 'STORE', 'THETA', kind='interp', line=231)
W('13,2547', 0o77616, '', 'RVQ', kind='interp', line=232)

S('2DZERO', 'equals', 0o34006, line=234)

# Page 1138
# ..... SETGAMMA SUBROUTINE .....
# SUBROUTINE TO SET GAMMA FOR THE LAT-LONG AND LALOTORV SUBROUTINES
#
# GAMMA = B**2/A**2 FOR EARTH (B-1)
# GAMMA = 1 FOR MOON (B-1)
#
# CALLING SEQUENCE
# L       CALL
# L+1            SETGAMMA
#
# INPUT
# LUNAFLAG=0 FOR EARTH,=1 FOR MOON
#
# OUTPUT
# GAMMA IN GAMRP  (B-1)

W('13,2550', 0o43145, 'SETGAMMA', 'DLOAD', 'BOFF', 'BRANCH FOR EARTH', kind='interp', line=253)
W('13,2551', 0o26505, '', '', 'B2/A2', 'EARTH GAMMA', kind='operand', line=254)
W('13,2552', 0o01743, '', '', 'LUNAFLAG', kind='operand', line=255)
W('13,2553', 0o26556, '', '', 'SETGMEX', kind='operand', line=256)
W('13,2554', 0o77735, '', 'SLOAD', kind='interp', line=257)
W('13,2555', 0o24005, '', '', '1B1', 'MOON GAMMA', kind='operand', line=258)
W('13,2556', 0o00011, 'SETGMEX', 'STORE', 'GAMRP', kind='interp', line=259)
W('13,2557', 0o77616, '', 'RVQ', kind='interp', line=260)
S('GAMRP', 'equals', 0o10, line=261)

# Page 1139
# .....SETRE SUBROUTINE .....
# SUBROUTINE TO SET RE (EARTH OR MOON RADIUS)
#
# RE= RM FOR MOON
# RE= RREF FOR FIXED EARTH RADIUS OR COMPUTED RF FOR FISCHER ELLIPSOID
#
# CALLING SEQUENCE
# L       CALL
# L+1            SETRE
#
# SUBROUTINES USED
# GETERAD
#
# INPUT
# ERADFLAG=0 FOR FIXED RE, 1 FOR COMPUTED RE
# ALPHAV +4= 1/2 SINL IF GETERAD IS CALLED
# LUNAFLAG=0 FOR EARTH,=1 FOR MOON
#
# OUTPUT
# ERADM= 504RM FOR MOON (METERS B-29)
# ERADM= ERAD OR COMPUTED RE FOR EARTH (METERS B-29)

W('13,2560', 0o71220, 'SETRE', 'STQ', 'DLOAD', kind='interp', line=286)
W('13,2561', 0o00051, '', '', 'SETREX', kind='operand', line=287)
W('13,2562', 0o10003, '', '', '504RM', kind='operand', line=288)
W('13,2563', 0o71214, '', 'BON', 'DLOAD', 'BRANCH FOR MOON', kind='interp', line=289)
W('13,2564', 0o01703, '', '', 'LUNAFLAG', kind='operand', line=290)
W('13,2565', 0o26575, '', '', 'TSTRLSRM', kind='operand', line=291)
W('13,2566', 0o10001, '', '', 'ERAD', kind='operand', line=292)
W('13,2567', 0o45014, '', 'BOFF', 'CALL', 'ERADFLAG=0 FOR FIXED RE,1 FOR COMPUTED', kind='interp', line=293)
W('13,2570', 0o00742, '', '', 'ERADFLAG', kind='operand', line=294)
W('13,2571', 0o26573, '', '', 'SETRXX', kind='operand', line=295)
W('13,2572', 0o26466, '', '', 'GETERAD', kind='operand', line=296)
W('13,2573', 0o37673, 'SETRXX', 'STCALL', 'ERADM', 'EXIT WITH RE OR RM METERS B-29', kind='interp', line=297)
W('13,2574', 0o00051, '', '', 'SETREX', kind='operand', line=298)
W('13,2575', 0o77214, 'TSTRLSRM', 'BON', 'VLOAD', 'ERADFLAG=0,SET R0=RLS', kind='interp', line=299)
W('13,2576', 0o00702, '', '', 'ERADFLAG', '        =1     R0=RM', kind='operand', line=300)
W('13,2577', 0o26573, '', '', 'SETRXX', kind='operand', line=301)
W('13,2600', 0o02023, '', '', 'RLS', kind='operand', line=302)
W('13,2601', 0o64446, '', 'ABVAL', 'SR2R', 'SCALE FROM B-27 TO B-29', kind='interp', line=303)
W('13,2602', 0o77650, '', 'GOTO', kind='interp', line=304)
W('13,2603', 0o26573, '', '', 'SETRXX', kind='operand', line=305)
S('SETREX', 'equals', 0o51, line=306)
