"""LATITUDE_LONGITUDE_SUBROUTINES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/LATITUDE_LONGITUDE_SUBROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1236-1242 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('LATITUDE_LONGITUDE_SUBROUTINES', 'LATITUDE_LONGITUDE_SUBROUTINES.agc', 'Comanche055', pages='1236-1242')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     LATITUDE_LONGITUDE_SUBROUTINES.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1236-1242
# Mod history:  2009-05-14 RSB  Adapted from the Colossus249/ file of the
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

# Page 1236
# SUBROUTINE TO CONVERT RAD VECTOR AT GIVEN TIME TO LAT,LONG AND ALT
#
# CALLING SEQUENCE
#
# L-1     CALL
# L               LAT-LONG
# SUBROUTINES USED
#
# R-TO-RP,ARCTAN,SETGAMMA,SETRE
# ERASABLE INIT. REQ.
#
# AXO,-AYO,AZO,TEPHEM (SET AT LAUNCH TIME)
# ALPHAV = POSITION VECTOR METERS B-29
# MPAC-- TIME (CSECS B-28)
# ERADFLAG =1, TO COMPUTE EARTH RADIUS, =0 FOR FIXED EARTH RADIUS
# LUNAFLAG=0 FOR EARTH,1 FOR MOON
# OUTPUT
#
# LATITUDE IN LAT         (REVS. B-0)
# LONGITUDE IN LONG       (REVS. B-0)
# ALTITUDE IN ALT METERS  B-29

#   BANK 30
#   SETLOC LATLONG
#   BANK

#   COUNT 13/LT-LG

#   EBANK= ALPHAV
W('13,2370', 0o40220, 'LAT-LONG', 'STQ', 'SETPD', kind='interp', line=60)
W('13,2371', 0o02242, '', '', 'INCORPEX', kind='operand', line=61)
W('13,2372', 0o00001, '', '', '0D', kind='operand', line=62)
W('13,2373', 0o24007, '', 'STOVL', '6D', 'SAVE TIME IN 6-7D FOR R-TO-RP', kind='interp', line=63)
W('13,2374', 0o02152, '', '', 'ALPHAV', kind='operand', line=64)
W('13,2375', 0o51406, '', 'PUSH', 'ABVAL', '0-5D= R FOR R-TO-RP', kind='interp', line=65)
W('13,2376', 0o16310, '', 'STODL', 'ALPHAM', 'ABS. VALUE OF R FOR ALT FORMULA BELOW', kind='interp', line=66)
W('13,2377', 0o11566, '', '', 'ZEROVEC', 'SET MPAC=0 FOR EARTH,NON-ZERO FOR MOON', kind='operand', line=67)
W('13,2400', 0o71414, '', 'BOFF', 'COS', 'USE COS(0) TO GET NON-ZERO IN MPAC', kind='interp', line=68)
W('13,2401', 0o01743, '', '', 'LUNAFLAG', '0=EARTH,1=MOON', kind='operand', line=69)
W('13,2402', 0o26403, '', '', 'CALLRTRP', kind='operand', line=70)
W('13,2403', 0o77624, 'CALLRTRP', 'CALL', kind='interp', line=71)
W('13,2404', 0o55371, '', '', 'R-TO-RP', 'RP VECTOR CONVERTED FROM R B-29', kind='operand', line=72)
W('13,2405', 0o77656, '', 'UNIT', '', 'UNIT RP B-1', kind='interp', line=73)
W('13,2406', 0o36152, '', 'STCALL', 'ALPHAV', 'U2= 1/2 SINL FOR SETRE SUBR BELOW', kind='interp', line=74)
W('13,2407', 0o26571, '', '', 'SETGAMMA', '      SET GAMMA=B2/A2 FOR EARTH,=1 FOR MOON', kind='operand', line=75)
W('13,2410', 0o77624, '', 'CALL', '', '      SCALED B-1', kind='interp', line=76)
W('13,2411', 0o26601, '', '', 'SETRE', 'CALC RE METERS B-29', kind='operand', line=77)
W('13,2412', 0o63545, '', 'DLOAD', 'DSQ', kind='interp', line=78)
W('13,2413', 0o02152, '', '', 'ALPHAV', kind='operand', line=79)
W('13,2414', 0o63525, '', 'PDDL', 'DSQ', kind='interp', line=80)
W('13,2415', 0o02154, '', '', 'ALPHAV +2', kind='operand', line=81)
# Page 1237
W('13,2416', 0o75415, '', 'DAD', 'SQRT', kind='interp', line=83)
W('13,2417', 0o76405, '', 'DMP', 'SL1R', kind='interp', line=84)
W('13,2420', 0o00011, '', '', 'GAMRP', kind='operand', line=85)
W('13,2421', 0o14021, '', 'STODL', 'COSTH', 'COS(LAT) B-1', kind='interp', line=86)
W('13,2422', 0o02156, '', '', 'ALPHAV +4', kind='operand', line=87)
W('13,2423', 0o34023, '', 'STCALL', 'SINTH', 'SIN(LAT) B-1', kind='interp', line=88)
W('13,2424', 0o26531, '', '', 'ARCTAN', kind='operand', line=89)
W('13,2425', 0o15104, '', 'STODL', 'LAT', 'LAT B0', kind='interp', line=90)
W('13,2426', 0o02152, '', '', 'ALPHAV', kind='operand', line=91)
W('13,2427', 0o14021, '', 'STODL', 'COSTH', 'COS(LONG) B-1', kind='interp', line=92)
W('13,2430', 0o02154, '', '', 'ALPHAV +2', kind='operand', line=93)
W('13,2431', 0o34023, '', 'STCALL', 'SINTH', 'SIN(LONG) B-1', kind='interp', line=94)
W('13,2432', 0o26531, '', '', 'ARCTAN', kind='operand', line=95)
W('13,2433', 0o15106, '', 'STODL', 'LONG', 'LONG. REVS B-0 IN RANGE -1/2 TO 1/2', kind='interp', line=96)
W('13,2434', 0o02310, '', '', 'ALPHAM', kind='operand', line=97)
W('13,2435', 0o77625, '', 'DSU', '', 'ALT= R-RE METERS B-29', kind='interp', line=98)
W('13,2436', 0o02241, '', '', 'ERADM', kind='operand', line=99)
W('13,2437', 0o35110, '', 'STCALL', 'ALT', 'EXIT WITH ALT METERS B-29', kind='interp', line=100)
W('13,2440', 0o02242, '', '', 'INCORPEX', kind='operand', line=101)
# Page 1238
# SUBROUTINE TO CONVERT LAT,LONG.ALT AT GIVEN TIME TO RADIUS VECTOR
# CALLING SEQUENCE

# L-1     CALL
# L               LALOTORV
# SUBROUTINES USED
# SETGAMMA,SETRE,RP-TO-R
# ERASABLE INIT. REQ.

# AXO,AYO,AZO,TEPHEM SET AT LAUNCH TIME
# LAT-- LATITUDE (REVS B0)
# LONG-- LONGITUDE (REVS B0)
# ALT--ALTITUDE (METERS) B-29
# MPAC-- TIME (CSECS B-28)
# ERADFLAG =1 TO COMPUTE EARTH RADIUS, =0 FOR FIXED EARTH RADIUS
# LUNAFLAG=0 FOR EARTH,1 FOR MOON
# OUTPUT

# R-VECTOR IN ALPHAV (METERS B-29)
W('13,2441', 0o40220, 'LALOTORV', 'STQ', 'SETPD', 'LAT,LONG,ALT TO R VECTOR', kind='interp', line=122)
W('13,2442', 0o02242, '', '', 'INCORPEX', kind='operand', line=123)
W('13,2443', 0o00001, '', '', '0D', kind='operand', line=124)
W('13,2444', 0o34007, '', 'STCALL', '6D', '6-7D= TIME FOR RP-TO-R', kind='interp', line=125)
W('13,2445', 0o26571, '', '', 'SETGAMMA', 'GAMMA=B2/A2 FOR EARTH,1 FOR MOON B-1', kind='operand', line=126)
W('13,2446', 0o73545, '', 'DLOAD', 'SIN', '              COS(LONG)COS(LAT) IN MPAC', kind='interp', line=127)
W('13,2447', 0o01104, '', '', 'LAT', '   UNIT RP= SIN(LONG)COS(LAT)    2-3D', kind='operand', line=128)
W('13,2450', 0o65275, '', 'DMPR', 'PDDL', 'PD 2          GAMMA*SIN(LAT)       0-1D', kind='interp', line=129)
W('13,2451', 0o00011, '', '', 'GAMRP', kind='operand', line=130)
W('13,2452', 0o01104, '', '', 'LAT', '      0-1D = GAMMA*SIN(LAT) B-2', kind='operand', line=131)
W('13,2453', 0o65346, '', 'COS', 'PDDL', 'PD4 2-3D=COS(LAT) B-1 TEMPORARILY', kind='interp', line=132)
W('13,2454', 0o01106, '', '', 'LONG', kind='operand', line=133)
W('13,2455', 0o57356, '', 'SIN', 'DMPR', 'PD 2', kind='interp', line=134)
W('13,2456', 0o71525, '', 'PDDL', 'COS', 'PD 4 2-3D=SIN(LONG)COS(LAT) B-2', kind='interp', line=135)
W('13,2457', 0o01104, '', '', 'LAT', kind='operand', line=136)
W('13,2460', 0o71525, '', 'PDDL', 'COS', 'PD 6 4-5D=COS(LAT) B-1 TEMPORARILY', kind='interp', line=137)
W('13,2461', 0o01106, '', '', 'LONG', kind='operand', line=138)
W('13,2462', 0o55475, '', 'DMPR', 'VDEF', 'PD4 MPAC= COS(LONG)COS(LAT) B-2', kind='interp', line=139)
W('13,2463', 0o41456, '', 'UNIT', 'PUSH', '0-5D= UNIT RP FOR RP-TO-R SUBR.', kind='interp', line=140)
W('13,2464', 0o36152, '', 'STCALL', 'ALPHAV', 'ALPHAV +4= SINL FOR SETRE SUBR.', kind='interp', line=141)
W('13,2465', 0o26601, '', '', 'SETRE', 'RE METERS B-29', kind='operand', line=142)
W('13,2466', 0o43145, '', 'DLOAD', 'BOFF', 'SET MPAC=0 FOR EARTH,NON-ZERO FOR MOON', kind='interp', line=143)
W('13,2467', 0o11566, '', '', 'ZEROVEC', kind='operand', line=144)
W('13,2470', 0o01743, '', '', 'LUNAFLAG', kind='operand', line=145)
W('13,2471', 0o26473, '', '', 'CALLRPRT', kind='operand', line=146)
W('13,2472', 0o77746, '', 'COS', '', 'USE COS(0) TO GET NON-ZERO IN MPAC', kind='interp', line=147)
W('13,2473', 0o77624, 'CALLRPRT', 'CALL', kind='interp', line=148)
W('13,2474', 0o55344, '', '', 'RP-TO-R', 'EXIT WITH UNIT R VECTOR IN MPAC', kind='operand', line=149)
W('13,2475', 0o16152, '', 'STODL', 'ALPHAV', kind='interp', line=150)
W('13,2476', 0o02241, '', '', 'ERADM', kind='operand', line=151)
# Page 1239
W('13,2477', 0o74215, '', 'DAD', 'VXSC', '(RE + ALT)(UNIT R) METERS B-30', kind='interp', line=153)
W('13,2500', 0o01110, '', '', 'ALT', kind='operand', line=154)
W('13,2501', 0o02152, '', '', 'ALPHAV', kind='operand', line=155)
W('13,2502', 0o77772, '', 'VSL1', '', 'R METERS B-29', kind='interp', line=156)
W('13,2503', 0o36152, '', 'STCALL', 'ALPHAV', 'EXIT WITH R IN METERS B-29', kind='interp', line=157)
W('13,2504', 0o02242, '', '', 'INCORPEX', kind='operand', line=158)
# SUBROUTINE TO COMPUTE EARTH RADIUS

# INPUT

# 1/2 SIN LAT IN ALPHAV +4

# OUTPUT

# EARTH RADIUS IN ERADM AND MPAC (METERS B-29)

W('13,2505', 0o63545, 'GETERAD', 'DLOAD', 'DSQ', kind='interp', line=169)
W('13,2506', 0o02156, '', '', 'ALPHAV +4', 'SIN**2(L)', kind='operand', line=170)
W('13,2507', 0o44352, '', 'SL1', 'BDSU', kind='interp', line=171)
W('13,2510', 0o11564, '', '', 'DP1/2', 'COS**2(L)', kind='operand', line=172)
W('13,2511', 0o44275, '', 'DMPR', 'BDSU', kind='interp', line=173)
W('13,2512', 0o26526, '', '', 'EE', kind='operand', line=174)
W('13,2513', 0o11564, '', '', 'DP1/2', kind='operand', line=175)
W('13,2514', 0o75465, '', 'BDDV', 'SQRT', kind='interp', line=176)
W('13,2515', 0o26522, '', '', 'B2XSC', kind='operand', line=177)
W('13,2516', 0o77622, '', 'SR4R', kind='interp', line=178)
W('13,2517', 0o02241, '', 'STORE', 'ERADM', kind='interp', line=179)
W('13,2520', 0o77616, '', 'RVQ', kind='interp', line=180)

# THE FOLLOWING CONSTANTS WERE COMPUTED WITH A=6378166,B=6356784 METERS
# B2XSC= B**2 SCALED B-51
# B2/A2= B**2/A**2 SCALED B-1
# EE=(1-B**2/A**2) SCALED B-0

W('13,2521', 0o00446, 'B2XSC', '2DEC', '.0179450689', 'B**2 SCALED B-51', kind='data', line=187)
W('13,2522', 0o00305, kind='data', line=187)

S('DP1/2', 'equals', 0o21563, line=189)
W('13,2523', 0o17711, 'B2/A2', '2DEC', '.9933064884 B-1', 'GAMMA= B**2/A**2 B-1', kind='data', line=190)
W('13,2524', 0o05254, kind='data', line=190)

W('13,2525', 0o00155, 'EE', '2DEC', '6.6935116 E-3', '(1-B**2/A**2) B-0', kind='data', line=192)
W('13,2526', 0o25250, kind='data', line=192)

W('13,2527', 0o00302, 'ERAD', '2DEC', '6373338 B-29', 'PAD RADIUS', kind='data', line=194)
W('13,2530', 0o17755, kind='data', line=194)

# Page 1240
# ARCTAN SUBROUTINE

# CALLING SEQUENCE

# SIN THETA IN SINTH B-1
# COS THETA IN COSTH B-1
# CALL ARCTAN

# OUTPUT
# ARCTAN THETA IN MPAC AND THETA B-0 IN RANGE -1/2 TO +1/2

W('13,2531', 0o77600, 'ARCTAN', 'BOV', kind='interp', line=209)
W('13,2532', 0o26533, '', '', 'CLROVFLW', kind='operand', line=210)
W('13,2533', 0o63545, 'CLROVFLW', 'DLOAD', 'DSQ', kind='interp', line=211)
W('13,2534', 0o00023, '', '', 'SINTH', kind='operand', line=212)
W('13,2535', 0o63525, '', 'PDDL', 'DSQ', kind='interp', line=213)
W('13,2536', 0o00021, '', '', 'COSTH', kind='operand', line=214)
W('13,2537', 0o77615, '', 'DAD', kind='interp', line=215)
W('13,2540', 0o75454, '', 'BZE', 'SQRT', kind='interp', line=216)
W('13,2541', 0o26557, '', '', 'ARCTANXX', 'ATAN=0/0  SET THETA=0', kind='operand', line=217)
W('13,2542', 0o40065, '', 'BDDV', 'BOV', kind='interp', line=218)
W('13,2543', 0o00023, '', '', 'SINTH', kind='operand', line=219)
W('13,2544', 0o26564, '', '', 'ATAN=90', kind='operand', line=220)
W('13,2545', 0o67542, '', 'SR1', 'ASIN', kind='interp', line=221)
W('13,2546', 0o00025, '', 'STORE', 'THETA', kind='interp', line=222)
W('13,2547', 0o50125, '', 'PDDL', 'BMN', kind='interp', line=223)
W('13,2550', 0o00021, '', '', 'COSTH', kind='operand', line=224)
W('13,2551', 0o26553, '', '', 'NEGCOS', kind='operand', line=225)
W('13,2552', 0o43545, '', 'DLOAD', 'RVQ', kind='interp', line=226)
W('13,2553', 0o57545, 'NEGCOS', 'DLOAD', 'DCOMP', kind='interp', line=227)
W('13,2554', 0o43244, '', 'BPL', 'DAD', kind='interp', line=228)
W('13,2555', 0o26561, '', '', 'NEGOUT', kind='operand', line=229)
W('13,2556', 0o11564, '', '', 'DP1/2', kind='operand', line=230)
W('13,2557', 0o00025, 'ARCTANXX', 'STORE', 'THETA', kind='interp', line=231)
W('13,2560', 0o77616, '', 'RVQ', kind='interp', line=232)

W('13,2561', 0o52025, 'NEGOUT', 'DSU', 'GOTO', kind='interp', line=234)
W('13,2562', 0o11564, '', '', 'DP1/2', kind='operand', line=235)
W('13,2563', 0o26557, '', '', 'ARCTANXX', kind='operand', line=236)
W('13,2564', 0o75345, 'ATAN=90', 'DLOAD', 'SIGN', kind='interp', line=237)
W('13,2565', 0o11612, '', '', 'LODP1/4', kind='operand', line=238)
W('13,2566', 0o00023, '', '', 'SINTH', kind='operand', line=239)
W('13,2567', 0o00025, '', 'STORE', 'THETA', kind='interp', line=240)
W('13,2570', 0o77616, '', 'RVQ', kind='interp', line=241)

S('2DZERO', 'equals', 0o21565, line=243)

# Page 1241
# ***** SETGAMMA SUBROUTINE *****
# SUBROUTINE TO SET GAMMA FOR THE LAT-LONG AND LALOTORV SUBROUTINES

# GAMMA = B**2/A**2 FOR EARTH (B-1)
# GAMMA = 1 FOR MOON (B-1)

# CALLING SEQUENCE
# L       CALL
# L+1             SETGAMMA

# INPUT
# LUNAFLAG=0 FOR EARTH,=1 FOR MOON

# OUTPUT
# GAMMA IN GAMRP (B-1)

W('13,2571', 0o43145, 'SETGAMMA', 'DLOAD', 'BOFF', 'BRANCH FOR EARTH', kind='interp', line=262)
W('13,2572', 0o26524, '', '', 'B2/A2', 'EARTH GAMMA', kind='operand', line=263)
W('13,2573', 0o01743, '', '', 'LUNAFLAG', kind='operand', line=264)
W('13,2574', 0o26577, '', '', 'SETGMEX', kind='operand', line=265)
W('13,2575', 0o77735, '', 'SLOAD', kind='interp', line=266)
W('13,2576', 0o11564, '', '', '1B1', 'MOON GAMMA', kind='operand', line=267)
W('13,2577', 0o00011, 'SETGMEX', 'STORE', 'GAMRP', kind='interp', line=268)
W('13,2600', 0o77616, '', 'RVQ', kind='interp', line=269)
S('GAMRP', 'equals', 0o10, line=270)

# Page 1242
# ***** SETRE SUBROUTINE *****
# SUBROUTINE TO SET RE (EARTH OR MOON RADIUS)

# RE= RM FOR MOON
# RE= RREF FOR FIXED EARTH RADIUS OR COMPUTED RF FOR FISCHER ELLIPSOID

# CALLING SEQUENCE
# L       CALL
# L+1             SETRE

# SUBROUTINES USED
# GETERAD

# INPUT
# ERADFLAG=0 FOR FIXED RE, 1 FOR COMPUTED RE
# ALPHAV +4= 1/2 SINL IF GETERAD IS CALLED
# LUNAFLAG=0 FOR EARTH,=1 FOR MOON

# OUTPUT
# ERADM= 504RM FOR MOON (METERS B-29)
# ERADM= ERAD OR COMPUTED RF FOR EARTH (METERS B-29)

W('13,2601', 0o71220, 'SETRE', 'STQ', 'DLOAD', kind='interp', line=295)
W('13,2602', 0o00051, '', '', 'SETREX', kind='operand', line=296)
W('13,2603', 0o26626, '', '', '504RM', kind='operand', line=297)
W('13,2604', 0o71214, '', 'BON', 'DLOAD', 'BRANCH FOR MOON', kind='interp', line=298)
W('13,2605', 0o01703, '', '', 'LUNAFLAG', kind='operand', line=299)
W('13,2606', 0o26616, '', '', 'TSTRLSRM', kind='operand', line=300)
W('13,2607', 0o26530, '', '', 'ERAD', kind='operand', line=301)
W('13,2610', 0o45014, '', 'BOFF', 'CALL', 'ERADFLAG=0 FOR FIXED RE,1 FOR COMPUTED', kind='interp', line=302)
W('13,2611', 0o00742, '', '', 'ERADFLAG', kind='operand', line=303)
W('13,2612', 0o26614, '', '', 'SETRXX', kind='operand', line=304)
W('13,2613', 0o26505, '', '', 'GETERAD', kind='operand', line=305)
W('13,2614', 0o36241, 'SETRXX', 'STCALL', 'ERADM', 'EXIT WITH RE OR RM METERS B-29', kind='interp', line=306)
W('13,2615', 0o00051, '', '', 'SETREX', kind='operand', line=307)
W('13,2616', 0o77214, 'TSTRLSRM', 'BON', 'VLOAD', 'ERADFLAG=0,SET R0=RLS', kind='interp', line=308)
W('13,2617', 0o00702, '', '', 'ERADFLAG', '        =1      R0=RM', kind='operand', line=309)
W('13,2620', 0o26614, '', '', 'SETRXX', kind='operand', line=310)
W('13,2621', 0o02026, '', '', 'RLS', kind='operand', line=311)
W('13,2622', 0o64446, '', 'ABVAL', 'SR2R', 'SCALE FROM B-27 TO B-29', kind='interp', line=312)
W('13,2623', 0o77650, '', 'GOTO', kind='interp', line=313)
W('13,2624', 0o26614, '', '', 'SETRXX', kind='operand', line=314)
S('SETREX', 'equals', 0o51, line=315)
W('13,2625', 0o00065, '504RM', '2DEC', '1738090 B-29', 'METERS B-29 (MOON RADIUS)', kind='data', line=316)
W('13,2626', 0o01265, kind='data', line=316)
