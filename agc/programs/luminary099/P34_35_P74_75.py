"""P34-35_P74-75.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P34-35_P74-75.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 658-702 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P34_35_P74_75', 'P34-35_P74-75.agc', 'Luminary099', pages='658-702')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P34-35_P74-75.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        658-702
# Mod history:  2009-05-19 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2009-06-05 RSB  Corrected a typo.
# 2011-01-06 JL   Fixed pseudo-label indentation.
# 2011-01-06 JL   Added missing comment characters.
# 2011-05-07 JL   Removed workaround.

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

# Page 658
# TRANSFER PHASE INITITIATION (TPI) PROGRAMS (P34 AND P74)

# MOD NO -1                     LOG SECTION -- P32-P35, P72-P75
# MOD BY WHITE, P.              DATE: 1 JUNE 67
#
# PURPOSE
#
# (1)     TO CALCULATE THE REQUIRED DELTA V AND OTHER INITIAL CONDITIONS
# REQUIRED BY THE ACTIVE VEHICLE FOR EXECUTION OF THE TRANSFER
# PHASE INITITATION (TPI) MANEUVER, GIVEN --

# (A)     TIME OF IGNITION TIG (TPI) OR THE ELEVATION ANGLE (E) OF
# THE ACTIVE/PASSIVE VEHICLE LOS AT TIG (TPI).

# (B)     CENTRAL ANGLE OF TRANSFER (CENTANG) FROM TIG (TPI) TO
# INTERCEPT TIME (TIG (TPF)).

# (2)     TO CALCULATE TIG (TPI) GIVEN E OR E GIVEN TIG (TPI).

# (3)     TO CALCULATE THESE PARAMETERS BASED UPON MANEUVER DATA
# APPROVED AND KEYED INTO THE DSKY BY THE ASTRONAUT.

# (4)     TO DISPLAY TO THE ASTRONAUT AND THE GROUND CERTAIN DEPENDENT
# VARIABLES ASSOCIATED WITH THE MANEUVER FOR APPROVAL BY THE
# ASTRONAUT/GROUND.

# (5)     TO STORE THE TPI TARGET PARAMETERS FOR USE BY THE DESIRED
# THRUSTING PROGRAM.
#
# ASSUMPTIONS

# (1)     LM ONLY -- THIS PROGRAM IS BASED UPON PREVIOUS COMPLETION OF
# THE CONSTANT DELTA ALTITUDE (CDH) PROGRAM (P33/P73).
# THEREFORE --

# (A)     AT A SELECTED TPI TIME (NOW IN STORAGE) THE LINE OF SIGHT
# BETWEEN THE ACTIVE AND PASSIVE VEHICLES WAS SELECTED TO BE
# A PRESCRIBED ANGLE (E) (NOW IN STORAGE) FROM THE
# HORIZONTAL PLANE DEFINED BY THE ACTIVE VEHICLE POSITION.

# (B)     THE TIME BETWEEN CDH IGNITION AND TPI IGNITION WAS
# COMPUTED TO BE GREATER THAN 10 MINUTES.

# (C)     THE VARIATION OF THE ALTITUDE DIFFERENCE BETWEEN THE
# ORBITS WAS MINIMIZED.

# (D)     THE PERICENTER ALTITUDES OF ORBITS FOLLOWING CSI AND
# CDH WERE COMPUTED TO BE GREATER THAN 35,000 FT FOR LUNAR
# Page 659
# ORBIT OR 85 NM FOR EARTH ORBIT.

# (E)     THE CSI AND CDH MANEUVERS WERE ASSUMED TO BE PARALLEL TO
# THE PLANE OF THE PASSIVE VEHICLE ORBIT.  HOWEVER, CREW
# MODIFICATION OF DELTA V (LV) COMPONENTS MAY HAVE RESULTED
# IN AN OUT-OF-PLANE MANEUVER.

# (2)     STATE VECTOR UPDATED BY P27 ARE DISALLOWED DURING AUTOMATIC
# STATE VECTOR UPDATING INITIATED BY P20 (SEE ASSUMPTION (4)).

# (3)     THIS PROGRAM MUST BE DONE OVER A TRACKING STATION FOR REAL
# TIME GROUND PARTICIPATION IN DATA INPUT AND OUTPUT.  COMPUTED
# VARIABLES MAY BE STORED FOR LATER VERIFICATION BY THE GROUND.
# THESE STORAGE CAPABILITIES ARE LIMITED ONLY TO THE PARAMETERS
# FOR ONE THRUSTING MANEUVER AT A TIME EXCEPT FOR CONCENTRIC
# FLIGHT PLAN MANEUVER SEQUENCES.

# (4)     THE RENDEZVOUS RADAR MAY OR MAY NOT BE USED TO UPDATE THE LM
# OR CSM STATE VECTORS FOR THIS PROGRAM.  IF RADAR USE IS
# DESIRED THE RADAR WAS TURNED ON AND LOCKED ON THE CSM BY
# PREVIOUS SELECTION OF P20.  RADAR SIGHTING MARKS WILL BE MADE
# AUTOMATICALLY APPROXIMATELY ONCE A MINUTE WHEN ENABLED BY THE
# TRACK AND UPDATE FLAGS (SEE P20).  THE RENDEZVOUS TRACKING
# MARK COUNTER IS ZEROED BY THE SELECTION OF P20 AND AFTER EACH
# THRUSTING MANEUVER.

# (5)     THE ISS NEED NOT BE ON TO COMPLETE THIS PROGRAM.

# (6)     THE OPERATION OF THE PROGRAM UTILIZES THE FOLLOWING FLAGS --
#
# ACTIVE VEHICLE FLAG -- DESIGNATES THE VEHICLE WHICH IS
# DOING RENDEZVOUS THRUSTING MANEUVERS TO THE PROGRAM WHICH
# CALCULATES THE MANEUVER PARAMETERS.  SET AT THE START OF
# EACH RENDEZVOUS PRE-THRUSTING PROGRAM.
#
# FINAL FLAG -- SELECTS FINAL PROGRAM DISPLAYS AFTER CREW HAS
# SELECTED THE FINAL MANEUVER COMPUTATION CYCLE.
#
# EXTERNAL DELTA V FLAG -- DESIGNATES THE TYPE OF STEERING
# REQUIRED FOR EXECUTION OF THIS MANEUVER BY THE THRUSTING
# PROGRAM SELECTED AFTER COMPLETION OF THIS PROGRAM.
#
# (7)     ONCE THE PARAMETERS REQUIRED FOR COMPUTATION OF THE MANEUVER
# HAVE BEEN COMPLETELY SPECIFIED, THE VALUE OF THE ACTIVE
# VEHICLE CENTRAL ANGLE OF TRANSFER IS COMPUTED AND STURED.
# THIS NUMBER WILL BE AVAILABLE FOR DISPLAY TO THE ASTRONAUT
# THROUGH THE USE OF V06N52.
#
# THE ASTRONAUT WILL CALL THIS DISPLAY TO VERIFY THAT THE
# CENTRAL ANGLE OF TRANSFER OF THE ACTIVE VEHICLE IS NOT WITHIN
# Page 660
# 170 TO 190 DEGREES.  IF THE ANGLE IS WITHIN THIS ZONE THE
# ASTRONAUT SHOULD REASSES THE INPUT TARGETING PARAMETERS BASED
# UPON DELTA V AND EXPECTED MANEUVER TIME.
#
# (8)     THIS PROGRAM IS SELECTED BY THE ASTRONAUT BY DSKY ENTRY --
#
# P34 IF THIS VEHICLE IS ACTIVE VEHICLE.
#
# P74 IF THIS VEHICLE IS PASSIVE VEHICLE.
#
# INPUT
#
# (1)     TTPI    TIME OF THE TPI MANEUVER.
# (2)     ELEV    DESIRED LOS ANGLE AT TPI
# (3)     CENTANG ORBITAL CENTRAL ANGLE OF THE PASSIVE VEHICLE DURING
# TRANSFER FROM TPI TO TIME OF INTERCEPT
#
# OUTPUT
#
# (1)     TRKMKCNT        NUMBER OF MARKS
# (2)     TTOGO           TIME TO GO
# (3)     +MGA            MIDDLE GIMBAL ANGLE
# (4)     TTPI            COMPUTED TIME OF TPI MANEUVER
# OR
# ELEV            COMPUTED LOS ANGLE AT TPI
# (5)     POSTTPI         PERIGEE ALTITUDE AFTER THE TPI MANEUVER
# (6)     DELVTPI         MAGNITUDE OF DELTA V AT TPI
# (7)     DELVTPF         MAGNITUDE OF DELTA V AT INTERCEPT
# (8)     DVLOS           DELTA VELOCITY AT TPI -- LINE OF SIGHT
# (9)     DELVLVC         DELTA VELOCITY AT TPI -- LOCAL VERTICAL COORDINATES
#
# DOWNLINK
#
# (1)     TTPI            TIME OF TPI MANEUVER
# (2)     TIG             TIME OF TPI MANEUVER
# (3)     ELEV            DESIRED LOS ANGLE AT TPI
# (4)     CENTANG         ORBITAL CENTRAL ANGLE OF THE PASSIVE VEHICLE DURING
# TRANSFER FROM TPI TO TIME OF INTERCEPT
# (5)     DELVEET3        DELTA VELOCITY AT TPI -- REFERENCE COORDINATES
# (6)     TPASS4          TIME OF INTERCEPT
#
# COMMUNICATION TO THRUSTING PROGRAMS
#
# (1)     TIG             TIME OF THE TPI MANEUVER
# (2)     RTARG           OFFSET TARGET POSITION
# (3)     TPASS4          TIME OF INTERCEPT
# (4)     XDELVFLG        RESET TO INDICATE LAMBERT (AIMPOINT) VG COMPUTATION
#
# SUBROUTINES USED
#
# AVFLAGA
# Page 661
# AVFLAGP
# VNPOOH
# DISPLAYE
# SELECTMU
# PRECSET
# S33/34.1
# ALARM
# BANKCALL
# GOFLASH
# GOTOPOOH
# TIMETHET
# S34/35.2
# PERIAPO1
# SHIFTR1
# S34/35.5
# VN1645

#   SETLOC CSI/CDH
#   BANK
#   EBANK= SUBEXIT
#   COUNT* $$/P3474
W('35,2545', 0o02347, 'P34', 'TC', 'AVFLAGA', line=207)
W('35,2546', 0o02550, '', 'TC', 'P34/P74A', line=208)
W('35,2547', 0o02354, 'P74', 'TC', 'AVFLAGP', line=209)
W('35,2550', 0o02361, 'P34/P74A', 'TC', 'P20FLGON', 'SET UPDATFLG, TRACKFLG', line=210)
W('35,2551', 0o33723, '', 'CAF', 'V06N37', 'TTPI', line=211)
W('35,2552', 0o03712, '', 'TC', 'VNPOOH', line=212)
W('35,2553', 0o00006, '', 'EXTEND', line=213)
W('35,2554', 0o33746, '', 'DCA', '130DEG', line=214)
W('35,2555', 0o53621, '', 'DXCH', 'CENTANG', line=215)
W('35,2556', 0o32417, '', 'CAF', 'P30ZERO', line=216)
W('35,2557', 0o55466, '', 'TS', 'NN', line=217)
W('35,2560', 0o03674, '', 'TC', 'DISPLAYE', 'ELEV AND CENTANG', line=218)
W('35,2561', 0o06037, '', 'TC', 'INTPRET', line=219)
W('35,2562', 0o71214, '', 'CLEAR', 'DLOAD', kind='interp', line=220)
W('35,2563', 0o01270, '', '', 'ETPIFLAG', kind='operand', line=221)
W('35,2564', 0o03636, '', '', 'TTPI', kind='operand', line=222)
W('35,2565', 0o17442, '', 'STODL', 'TIG', kind='interp', line=223)
W('35,2566', 0o02257, '', '', 'ELEV', kind='operand', line=224)
W('35,2567', 0o43054, '', 'BZE', 'SET', kind='interp', line=225)
W('35,2570', 0o72572, '', '', 'P34/P74B', kind='operand', line=226)
W('35,2571', 0o01070, '', '', 'ETPIFLAG', kind='operand', line=227)
W('35,2572', 0o77624, 'P34/P74B', 'CALL', kind='interp', line=228)
W('35,2573', 0o20000, '', '', 'SELECTMU', kind='operand', line=229)
S('DELELO', 'equals', 0o32, line=230)
W('35,2574', 0o43145, 'P34/P74C', 'DLOAD', 'SET', kind='interp', line=231)
W('35,2575', 0o06522, '', '', 'ZEROVECS', kind='operand', line=232)
W('35,2576', 0o03460, '', '', 'ITSWICH', kind='operand', line=233)
W('35,2577', 0o43014, '', 'BON', 'CLEAR', kind='interp', line=234)
W('35,2600', 0o01310, '', '', 'ETPIFLAG', kind='operand', line=235)
# Page 662
W('35,2601', 0o72603, '', '', 'SWCHSET', kind='operand', line=237)
W('35,2602', 0o03660, '', '', 'ITSWICH', kind='operand', line=238)
W('35,2603', 0o02317, 'SWCHSET', 'STORE', 'NOMTPI', kind='interp', line=239)
W('35,2604', 0o43345, 'INTLOOP', 'DLOAD', 'DAD', kind='interp', line=240)
W('35,2605', 0o03636, '', '', 'TTPI', kind='operand', line=241)
W('35,2606', 0o02317, '', '', 'NOMTPI', kind='operand', line=242)
W('35,2607', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=243)
W('35,2610', 0o46360, '', '', 'PRECSET', kind='operand', line=244)
W('35,2611', 0o77624, '', 'CALL', kind='interp', line=245)
W('35,2612', 0o72764, '', '', 'S33/34.1', kind='operand', line=246)
W('35,2613', 0o77454, '', 'BZE', 'EXIT', kind='interp', line=247)
W('35,2614', 0o72625, '', '', 'SWCHCLR', kind='operand', line=248)
W('35,2615', 0o05567, '', 'TC', 'ALARM', line=249)
W('35,2616', 0o00611, '', 'OCT', '611', kind='data', line=250)
W('35,2617', 0o35006, '', 'CAF', 'V05N09', line=251)
W('35,2620', 0o04616, '', 'TC', 'BANKCALL', line=252)
W('35,2621', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=253)
W('35,2622', 0o06001, '', 'TC', 'GOTOPOOH', line=254)
W('35,2623', 0o02550, '', 'TC', 'P34/P74A', 'PROCEED', line=255)
W('35,2624', 0o02615, '', 'TC', '-7', 'V32', line=256)

W('35,2625', 0o43014, 'SWCHCLR', 'BONCLR', 'BON', kind='interp', line=258)
W('35,2626', 0o03600, '', '', 'ITSWICH', kind='operand', line=259)
W('35,2627', 0o72604, '', '', 'INTLOOP', kind='operand', line=260)
W('35,2630', 0o01310, '', '', 'ETPIFLAG', kind='operand', line=261)
W('35,2631', 0o72635, '', '', 'P34/P74D', 'DISPLAY TTPI', kind='operand', line=262)
W('35,2632', 0o77776, '', 'EXIT', kind='interp', line=263)
W('35,2633', 0o03674, '', 'TC', 'DISPLAYE', 'DISPLAY ELEV AND CENTANG', line=264)
W('35,2634', 0o02640, '', 'TC', 'P34/P74E', line=265)
W('35,2635', 0o77776, 'P34/P74D', 'EXIT', kind='interp', line=266)
W('35,2636', 0o33723, '', 'CAF', 'V06N37', 'TTPI', line=267)
W('35,2637', 0o03712, '', 'TC', 'VNPOOH', line=268)
W('35,2640', 0o06037, 'P34/P74E', 'TC', 'INTPRET', line=269)
W('35,2641', 0o71201, '', 'SETPD', 'DLOAD', kind='interp', line=270)
W('35,2642', 0o00001, '', '', '0D', kind='operand', line=271)
W('35,2643', 0o02777, '', '', 'RTX1', kind='operand', line=272)
W('35,2644', 0o14047, '', 'STODL', 'X1', kind='interp', line=273)
W('35,2645', 0o03621, '', '', 'CENTANG', kind='operand', line=274)
W('35,2646', 0o71406, '', 'PUSH', 'COS', kind='interp', line=275)
W('35,2647', 0o16732, '', 'STODL', 'CSTH', kind='interp', line=276)
W('35,2650', 0o77756, '', 'SIN', kind='interp', line=277)
W('35,2651', 0o26730, '', 'STOVL', 'SNTH', kind='interp', line=278)
W('35,2652', 0o03552, '', '', 'RPASS3', kind='operand', line=279)
W('35,2653', 0o77657, '', 'VSR*', kind='interp', line=280)
W('35,2654', 0o57176, '', '', '0,2', kind='operand', line=281)
W('35,2655', 0o26655, '', 'STOVL', 'RVEC', kind='interp', line=282)
W('35,2656', 0o03560, '', '', 'VPASS3', kind='operand', line=283)
W('35,2657', 0o43057, '', 'VSR*', 'SET', kind='interp', line=284)
W('35,2660', 0o57176, '', '', '0,2', kind='operand', line=285)
W('35,2661', 0o03466, '', '', 'RVSW', kind='operand', line=286)
# Page 663
W('35,2662', 0o36744, '', 'STCALL', 'VVEC', kind='interp', line=288)
W('35,2663', 0o24732, '', '', 'TIMETHET', kind='operand', line=289)
W('35,2664', 0o77745, '', 'DLOAD', kind='interp', line=290)
W('35,2665', 0o03636, '', '', 'TTPI', kind='operand', line=291)
W('35,2666', 0o03610, '', 'STORE', 'INTIME', 'FOR INITVEL', kind='interp', line=292)
W('35,2667', 0o77615, '', 'DAD', kind='interp', line=293)
W('35,2670', 0o00037, '', '', 'T', 'RENDEZVOUS TIME', kind='operand', line=294)
W('35,2671', 0o37631, '', 'STCALL', 'TPASS4', 'FOR INITVEL', kind='interp', line=295)
W('35,2672', 0o73306, '', '', 'S34/35.2', kind='operand', line=296)
W('35,2673', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=297)
W('35,2674', 0o02366, '', '', 'DELVEET3', kind='operand', line=298)
W('35,2675', 0o27576, '', 'STOVL', 'DELVTPI', kind='interp', line=299)
W('35,2676', 0o03506, '', '', 'VPASS4', kind='operand', line=300)
W('35,2677', 0o51451, '', 'VSU', 'ABVAL', kind='interp', line=301)
W('35,2700', 0o03566, '', '', 'VTPRIME', kind='operand', line=302)
W('35,2701', 0o26350, '', 'STOVL', 'DELVTPF', kind='interp', line=303)
W('35,2702', 0o03536, '', '', 'RACT3', kind='operand', line=304)
W('35,2703', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=305)
W('35,2704', 0o02337, '', '', 'VIPRIME', kind='operand', line=306)
W('35,2705', 0o46316, '', '', 'PERIAPO1', kind='operand', line=307)
W('35,2706', 0o77624, '', 'CALL', kind='interp', line=308)
W('35,2707', 0o46426, '', '', 'SHIFTR1', kind='operand', line=309)
W('35,2710', 0o17606, '', 'STODL', 'POSTTPI', kind='interp', line=310)
W('35,2711', 0o03636, '', '', 'TTPI', kind='operand', line=311)
W('35,2712', 0o03442, '', 'STORE', 'TIG', kind='interp', line=312)
W('35,2713', 0o77776, '', 'EXIT', kind='interp', line=313)
W('35,2714', 0o33725, '', 'CAF', 'V06N58', line=314)
W('35,2715', 0o03712, '', 'TC', 'VNPOOH', line=315)
W('35,2716', 0o06037, '', 'TC', 'INTPRET', line=316)
W('35,2717', 0o77624, '', 'CALL', kind='interp', line=317)
W('35,2720', 0o73522, '', '', 'S34/35.5', kind='operand', line=318)
W('35,2721', 0o77624, '', 'CALL', kind='interp', line=319)
W('35,2722', 0o73606, '', '', 'VN1645', kind='operand', line=320)
W('35,2723', 0o77650, '', 'GOTO', kind='interp', line=321)
W('35,2724', 0o72574, '', '', 'P34/P74C', kind='operand', line=322)
# Page 664
# RENDEZVOUS MID-COURSE MANEUVER PROGRAMS (P35 AND P75)

# MOD NO -1                     LOG SECTION -- P32-P35, P72-P75
# MOD BY WHITE, P.              DATE:  1 JUNE 67
#
# PURPOSE
#
# (1)     TO CALCULATE THE REQUIRED DELTA V AND OTHER INITIAL CONDITIONS
# REQUIRED BY THE ACTIVE VEHICLE FOR EXECUTION OF THE NEXT
# MID-COURSE CORRECTION OF THE TRANSFER PHASE OF AN ACTIVE
# VEHICLE RENDEZVOUS.
#
# (2)     TO DISPLAY TO THE ASTRONAUT AND THE GROUND CERTAIN DEPENDENT
# VARIABLES ASSOCIATED WITH THE MANEUVER FOR APPROVAL BY THE
# ASTRONAUT/GROUND.
#
# (3)     TO STORE THE TPM TARGET PARAMETERS FOR USE BY THE DESIRED
# THRUSTING PROGRAM.
#
# ASSUMPTIONS
#
# (1)     THE ISS NEED NOT BE ON TO COMPLETE THIS PROGRAM.
#
# (2)     STATE VECTOR UPDATES BY P27 ARE DISALLOWED DURING AUTOMATIC
# STATE VECTOR UPDATING INITIATED BY P20 (SEE ASSUMPTION (3)).
#
# (3)     THE RENDEZVOUS RADAR IS ON AND IS LOCKED ON THE CSM.  THIS WAS
# DONE DURING PREVIOUS SELECTION OF P20.  RADAR SIGHTING MARKS
# WILL BE MADE AUTOMATICALLY APPROXIMATELY ONCE A MINUTE WHEN
# ENABLED BY THE TRACK AND UPDATE FLAGS (SEE P20).  THE
# RENDEZVOUS TRACKING MARK COUNTER IS ZEROED BY THE SELECTION OF
# P20 AND AFTER EACH THRUSTING MANEUVER.
#
# (4)     THE OPERATION OF THE PROGRAM UTILIZES THE FOLLOWING FLAGS --
#
# THE ACTIVE VEHICLE FLAG -- DESIGNATES THE VEHICLE WHICH IS
# DOING RENDEZVOUS THRUSTING MANEUVERS TO THE PROGRAM WHICH
# CALCULATES THE MANEUVER PARAMETERS.  SET AT THE START OF
# EACH RENDEZVOUS PRE-THRUSTING PROGRAM.
#
# FINAL FLAG -- SELECTS FINAL PROGRAM DISPLAYS AFTER CREW HAS
# SELECTED THE FINAL MANEUVER COMPUTATION CYCLE.
#
# EXTERNAL DELTA V FLAG -- DESIGNATES THE TYPE OF STEERING
# REQUIRED FOR EXECUTION OF THIS MANEUVER BY THE THRUSTING
# PROGRAM SELECTED AFTER COMPLETION OF THIS PROGRAM.
#
# (5)     THE TIME OF INTERCEPT (T(INT)) WAS DEFINED BY PREVIOUS
# COMPLETION OF THE TRANSFER PHASE INITIATION (TPI) PROGRAM
# (P34/P74) AND IS PRESENTLY AVAILABLE IN STORAGE.
#
# Page 665
# (6)     ONCE THE PARAMETERS REQUIRED FOR COMPUTATION OF THE MANEUVER
# HAVE BEEN COMPLETELY SPECIFIED, THE VALUE OF THE ACTIVE
# VEHICLE CENTRAL ANGLE OF TRANSFER IS COMPUTED AND STORED.
# THIS NUMBER WILL BE AVAILABLE FOR DISPLAY TO THE ASTRONAUT
# THROUGH THE USE OF V06N52
#
# THE ASTRONAUT WILL CALL THIS DISPLAY TO VERIFY THAT THE
# CENTRAL ANGLE OF TRANSFER OF THE ACTIVE VEHICLE IS NOT WITHIN
# 170 TO 190 DEGREES.  IF THE ANGLE IS WITHIN THIS ZONE THE
# ASTRONAUT SHOULD REASSESS THE INPUT TARGETING PARAMETERS BASED
# UPON DELTA V AND EXPECTED MANEUVER TIME.
#
# (7)     THIS PROGRAM IS SELECTED BY THE ASTRONAUT BY DSKY ENTRY --
#
# P35 IF THIS VEHICLE IS ACTIVE VEHICLE.
#
# P75 IF THIS VEHICLE IS PASSIVE VEHICLE.
#
# INPUT
#
# (1)     TPASS4          TIME OF INTERCEPT -- SAVED FROM P34/P74
#
# OUTPUT
#
# (1)     TRKMKCNT        NUMBER OF MARKS
# (2)     TTOGO           TIME TO GO
# (3)     +MGA            MIDOLF GIMBAL ANGLE
# (4)     DVLOS           DELTA VELOCITY AT MID -- LINE OF SIGHT
# (5)     DELVLVC         DELTA VELOCITY AT MID -- LOCAL VERTICAL COORDINATES
#
# DOWNLINK
#
# (1)     TIG             TIME OF THE TPM MANEUVER
# (2)     DELVEET3        DELTA VELOCITY AT TPM -- REFERENCE COORDINATES
# (3)     TPASS4          TIME OF INTERCEPT
#
# COMMUNICATION TO THRUSTING PROGRAMS
#
# (1)     TIG             TIME OF THE TPM MANEUVER
# (2)     RTARG           OFFSET TARGET POSITION
# (3)     TPASS4          TIME OF INTERCEPT
# (4)     XDELVFLG        RESET TO INDICATE LAMBERT (AIMPOINT) VG COMPUTATION.
#
# SUBROUTINES USED
#
# AVFLAGA
# AVFLAGP
# LOADTIME
# SELECTMU
# PRECSET
# S34/35.1
# S34/35.2
# Page 666
# S34/35.5
# VN1645

#   COUNT* $$/P3575
#   EBANK= KT

W('35,2725', 0o02347, 'P35', 'TC', 'AVFLAGA', line=435)
W('35,2726', 0o00006, '', 'EXTEND', line=436)
W('35,2727', 0o31401, '', 'DCA', 'ATIGINC', line=437)
W('35,2730', 0o02734, '', 'TC', 'P35/P75A', line=438)
W('35,2731', 0o02354, 'P75', 'TC', 'AVFLAGP', line=439)
W('35,2732', 0o00006, '', 'EXTEND', line=440)
W('35,2733', 0o31403, '', 'DCA', 'PTIGINC', line=441)
W('35,2734', 0o53576, 'P35/P75A', 'DXCH', 'KT', line=442)
W('35,2735', 0o02361, '', 'TC', 'P20FLGON', 'SET UPDATFLG, TRACKFLG', line=443)
W('35,2736', 0o06037, '', 'TC', 'INTPRET', line=444)
W('35,2737', 0o77624, '', 'CALL', kind='interp', line=445)
W('35,2740', 0o20000, '', '', 'SELECTMU', kind='operand', line=446)
W('35,2741', 0o77634, 'P35/P75B', 'RTB', kind='interp', line=447)
W('35,2742', 0o21573, '', '', 'LOADTIME', kind='operand', line=448)
W('35,2743', 0o03612, '', 'STORE', 'TSTRT', kind='interp', line=449)
W('35,2744', 0o77615, '', 'DAD', kind='interp', line=450)
W('35,2745', 0o03576, '', '', 'KT', kind='operand', line=451)
W('35,2746', 0o03442, '', 'STORE', 'TIG', kind='interp', line=452)
W('35,2747', 0o03610, '', 'STORE', 'INTIME', 'FOR INITVEL', kind='interp', line=453)
W('35,2750', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=454)
W('35,2751', 0o46360, '', '', 'PRECSET', 'ADVANCE BOTH VEHICLES', kind='operand', line=455)
W('35,2752', 0o77624, '', 'CALL', kind='interp', line=456)
W('35,2753', 0o73274, '', '', 'S34/35.1', 'GET NORM AND LOS FOR TRANSFORM', kind='operand', line=457)
W('35,2754', 0o77624, '', 'CALL', kind='interp', line=458)
W('35,2755', 0o73306, '', '', 'S34/35.2', 'GET DELTA V(LV)', kind='operand', line=459)
W('35,2756', 0o77624, '', 'CALL', kind='interp', line=460)
W('35,2757', 0o73522, '', '', 'S34/35.5', kind='operand', line=461)
W('35,2760', 0o77624, '', 'CALL', kind='interp', line=462)
W('35,2761', 0o73606, '', '', 'VN1645', kind='operand', line=463)
W('35,2762', 0o77650, '', 'GOTO', kind='interp', line=464)
W('35,2763', 0o72741, '', '', 'P35/P75B', kind='operand', line=465)
# Page 667
# ***** S33/34.1 *****

W('35,2764', 0o66220, 'S33/34.1', 'STQ', 'SSP', kind='interp', line=469)
W('35,2765', 0o03463, '', '', 'NORMEX', kind='operand', line=470)
W('35,2766', 0o03614, '', '', 'TITER', kind='operand', line=471)
W('35,2767', 0o40000, '', 'OCT', '40000', kind='data', line=472)
W('35,2770', 0o40345, '', 'DLOAD', 'SETPD', kind='interp', line=473)
W('35,2771', 0o33734, '', '', 'MAX250', kind='operand', line=474)
W('35,2772', 0o00001, '', '', '0D', kind='operand', line=475)
W('35,2773', 0o27574, '', 'STOVL', 'SECMAX', kind='interp', line=476)
W('35,2774', 0o03536, '', '', 'RACT3', kind='operand', line=477)
W('35,2775', 0o27500, '', 'STOVL', 'RAPREC', kind='interp', line=478)
W('35,2776', 0o03544, '', '', 'VACT3', kind='operand', line=479)
W('35,2777', 0o27506, '', 'STOVL', 'VAPREC', kind='interp', line=480)
W('35,3000', 0o03552, '', '', 'RPASS3', kind='operand', line=481)
W('35,3001', 0o27522, '', 'STOVL', 'RPPREC', kind='interp', line=482)
W('35,3002', 0o03560, '', '', 'VPASS3', kind='operand', line=483)
W('35,3003', 0o03530, '', 'STORE', 'VPPREC', kind='interp', line=484)
W('35,3004', 0o77624, 'ELCALC', 'CALL', kind='interp', line=485)
W('35,3005', 0o73274, '', '', 'S34/35.1', 'NORMAL AND LOS', kind='operand', line=486)
W('35,3006', 0o63235, '', 'VXV', 'PDVL', kind='interp', line=487)
W('35,3007', 0o03536, '', '', 'RACT3', '(RA*VA)*RA 0D', kind='operand', line=488)
W('35,3010', 0o53515, '', 'PDVL', 'UNIT', 'ULOS AT 6D', kind='interp', line=489)
W('35,3011', 0o03536, '', '', 'RACT3', kind='operand', line=490)
W('35,3012', 0o46315, '', 'PDVL', 'VPROJ', 'XCHNJ AND UP', kind='interp', line=491)
W('35,3013', 0o51352, '', 'VSL2', 'BVSU', kind='interp', line=492)
W('35,3014', 0o02311, '', '', 'ULOS', kind='operand', line=493)
W('35,3015', 0o63256, '', 'UNIT', 'PDVL', 'UP AT 0D', kind='interp', line=494)
W('35,3016', 0o63241, '', 'DOT', 'PDVL', 'UP.UN*RA AT 0D', kind='interp', line=495)
W('35,3017', 0o00001, '', '', '0D', 'UP IN MPAC', kind='operand', line=496)
W('35,3020', 0o75241, '', 'DOT', 'SIGN', kind='interp', line=497)
W('35,3021', 0o02311, '', '', 'ULOS', kind='operand', line=498)
W('35,3022', 0o65552, '', 'SL1', 'ACOS', kind='interp', line=499)
W('35,3023', 0o50315, '', 'PDVL', 'DOT', 'EA AT 0D', kind='interp', line=500)
W('35,3024', 0o02311, '', '', 'ULOS', kind='operand', line=501)
W('35,3025', 0o03536, '', '', 'RACT3', kind='operand', line=502)
W('35,3026', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=503)
W('35,3027', 0o73032, '', '', 'TESTY', kind='operand', line=504)
W('35,3030', 0o06530, '', '', 'DPPOSMAX', kind='operand', line=505)
W('35,3031', 0o41425, '', 'DSU', 'PUSH', kind='interp', line=506)
W('35,3032', 0o71214, 'TESTY', 'BOFF', 'DLOAD', kind='interp', line=507)
W('35,3033', 0o03740, '', '', 'ITSWICH', kind='operand', line=508)
W('35,3034', 0o73261, '', '', 'ELEX', kind='operand', line=509)
W('35,3035', 0o03576, '', '', 'DELEL', kind='operand', line=510)
W('35,3036', 0o14033, '', 'STODL', 'DELELO', kind='interp', line=511)
W('35,3037', 0o77625, '', 'DSU', kind='interp', line=512)
W('35,3040', 0o02257, '', '', 'ELEV', kind='operand', line=513)
W('35,3041', 0o03576, '', 'STORE', 'DELEL', kind='interp', line=514)
W('35,3042', 0o45246, '', 'ABS', 'DSU', kind='interp', line=515)
W('35,3043', 0o33740, '', '', 'ELEPS', kind='operand', line=516)
# Page 668
W('35,3044', 0o77640, '', 'BMN', kind='interp', line=518)
W('35,3045', 0o73271, '', '', 'TIMEX', 'COMMERCIALS EVERYWHERE', kind='operand', line=519)
W('35,3046', 0o70535, 'FIGTIME', 'SLOAD', 'SR1', kind='interp', line=520)
W('35,3047', 0o03614, '', '', 'TITER', kind='operand', line=521)
W('35,3050', 0o72030, '', 'BHIZ', 'LXA,1', kind='interp', line=522)
W('35,3051', 0o03463, '', '', 'NORMEX', 'TOO MANY ITERATIONS', kind='operand', line=523)
W('35,3052', 0o00154, '', '', 'MPAC', kind='operand', line=524)
W('35,3053', 0o77330, '', 'SXA,1', 'VLOAD', kind='interp', line=525)
W('35,3054', 0o03613, '', '', 'TITER', kind='operand', line=526)
W('35,3055', 0o03552, '', '', 'RPASS3', kind='operand', line=527)
W('35,3056', 0o65256, '', 'UNIT', 'PDDL', kind='interp', line=528)
W('35,3057', 0o00045, '', '', '36D', kind='operand', line=529)
W('35,3060', 0o53515, '', 'PDVL', 'UNIT', kind='interp', line=530)
W('35,3061', 0o03536, '', '', 'RACT3', kind='operand', line=531)
W('35,3062', 0o77725, '', 'PDDL', kind='interp', line=532)
W('35,3063', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=533)
W('35,3064', 0o00045, '', '', '36D', kind='operand', line=534)
W('35,3065', 0o77621, '', 'BDSU', kind='interp', line=535)
W('35,3066', 0o00015, '', '', '12D', kind='operand', line=536)
W('35,3067', 0o14037, '', 'STODL', '30D', 'RP - RA MAGNITUDES', kind='interp', line=537)
W('35,3070', 0o06520, '', '', 'DPHALF', kind='operand', line=538)
W('35,3071', 0o41425, '', 'DSU', 'PUSH', kind='interp', line=539)
W('35,3072', 0o02257, '', '', 'ELEV', kind='operand', line=540)
W('35,3073', 0o50165, '', 'SIGN', 'BMN', kind='interp', line=541)
W('35,3074', 0o00037, '', '', '30D', kind='operand', line=542)
W('35,3075', 0o03463, '', '', 'NORMEX', kind='operand', line=543)
W('35,3076', 0o71545, '', 'DLOAD', 'COS', kind='interp', line=544)
W('35,3077', 0o56205, '', 'DMP', 'DDV', kind='interp', line=545)
W('35,3100', 0o00017, '', '', '14D', kind='operand', line=546)
W('35,3101', 0o00015, '', '', '12D', kind='operand', line=547)
W('35,3102', 0o77676, '', 'DCOMP', '', 'SINCE COS(180-A)=-COS A', kind='interp', line=548)
W('35,3103', 0o00035, '', 'STORE', '28D', kind='interp', line=549)
W('35,3104', 0o44246, '', 'ABS', 'BDSU', kind='interp', line=550)
W('35,3105', 0o06520, '', '', 'DPHALF', kind='operand', line=551)
W('35,3106', 0o77240, '', 'BMN', 'VLOAD', kind='interp', line=552)
W('35,3107', 0o03463, '', '', 'NORMEX', kind='operand', line=553)
W('35,3110', 0o02261, '', '', 'UNRM', kind='operand', line=554)
W('35,3111', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=555)
W('35,3112', 0o00007, '', '', '6D', 'UN*RA', kind='operand', line=556)
W('35,3113', 0o41241, '', 'DOT', 'DMP', kind='interp', line=557)
W('35,3114', 0o03544, '', '', 'VACT3', kind='operand', line=558)
W('35,3115', 0o00015, '', '', '12D', kind='operand', line=559)
W('35,3116', 0o47315, '', 'PDVL', 'VXV', kind='interp', line=560)
W('35,3117', 0o00001, '', '', '0D', kind='operand', line=561)
W('35,3120', 0o03560, '', '', 'VPASS3', kind='operand', line=562)
W('35,3121', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=563)
W('35,3122', 0o00001, '', '', '0D', '(RP*VP)*RP', kind='operand', line=564)
W('35,3123', 0o41241, '', 'DOT', 'DMP', kind='interp', line=565)
W('35,3124', 0o03560, '', '', 'VPASS3', kind='operand', line=566)
W('35,3125', 0o00017, '', '', '14D', kind='operand', line=567)
# Page 669
W('35,3126', 0o77621, '', 'BDSU', kind='interp', line=569)
W('35,3127', 0o63301, '', 'NORM', 'PDVL', 'NORMALIZED WA - WP 12D', kind='interp', line=570)
W('35,3130', 0o00047, '', '', 'X1', kind='operand', line=571)
W('35,3131', 0o00007, '', '', '6D', kind='operand', line=572)
W('35,3132', 0o50235, '', 'VXV', 'DOT', kind='interp', line=573)
W('35,3133', 0o00001, '', '', '0D', kind='operand', line=574)
W('35,3134', 0o02261, '', '', 'UNRM', 'RA*RP.UN 14D', kind='operand', line=575)
W('35,3135', 0o50315, '', 'PDVL', 'DOT', kind='interp', line=576)
W('35,3136', 0o00001, '', '', '0D', kind='operand', line=577)
W('35,3137', 0o00007, '', '', '6D', kind='operand', line=578)
W('35,3140', 0o65552, '', 'SL1', 'ACOS', kind='interp', line=579)
W('35,3141', 0o77765, '', 'SIGN', kind='interp', line=580)
W('35,3142', 0o43225, '', 'DSU', 'DAD', 'ALPHA PI', kind='interp', line=581)
W('35,3143', 0o06520, '', '', 'DPHALF', kind='operand', line=582)
W('35,3144', 0o02257, '', '', 'ELEV', kind='operand', line=583)
W('35,3145', 0o65525, '', 'PDDL', 'ACOS', kind='interp', line=584)
W('35,3146', 0o00035, '', '', '28D', kind='operand', line=585)
W('35,3147', 0o75221, '', 'BDSU', 'SIGN', kind='interp', line=586)
W('35,3150', 0o06520, '', '', 'DPHALF', kind='operand', line=587)
W('35,3151', 0o00037, '', '', '30D', 'CONTAINS RP-RA', kind='operand', line=588)
W('35,3152', 0o77615, '', 'DAD', kind='interp', line=589)
W('35,3153', 0o56205, '', 'DMP', 'DDV', kind='interp', line=590)
W('35,3154', 0o33732, '', '', 'TWOPI', kind='operand', line=591)
W('35,3155', 0o77605, '', 'DMP', kind='interp', line=592)
W('35,3156', 0o41257, '', 'SL*', 'DMP', kind='interp', line=593)
W('35,3157', 0o20176, '', '', '0 -3,1', kind='operand', line=594)
W('35,3160', 0o51406, '', 'PUSH', 'ABS', kind='interp', line=595)
W('35,3161', 0o50025, '', 'DSU', 'BMN', kind='interp', line=596)
W('35,3162', 0o03574, '', '', 'SECMAX', kind='operand', line=597)
W('35,3163', 0o73167, '', '', 'OKMAX', kind='operand', line=598)
W('35,3164', 0o75345, '', 'DLOAD', 'SIGN', 'REPLACE TIME WITH MAX TIME SIGNED', kind='interp', line=599)
W('35,3165', 0o03574, '', '', 'SECMAX', kind='operand', line=600)
W('35,3166', 0o77606, '', 'PUSH', kind='interp', line=601)
W('35,3167', 0o51135, 'OKMAX', 'SLOAD', 'BPL', 'TEST FIRST ITERATION', kind='interp', line=602)
W('35,3170', 0o03614, '', '', 'TITER', kind='operand', line=603)
W('35,3171', 0o73177, '', '', 'REPETE', kind='operand', line=604)
W('35,3172', 0o71331, '', 'SSP', 'DLOAD', kind='interp', line=605)
W('35,3173', 0o03614, '', '', 'TITER', kind='operand', line=606)
W('35,3174', 0o37777, '', 'OCT', '37777', kind='data', line=607)
W('35,3175', 0o77650, '', 'GOTO', kind='interp', line=608)
W('35,3176', 0o73235, '', '', 'STORDELT', kind='operand', line=609)
W('35,3177', 0o41345, 'REPETE', 'DLOAD', 'DMP', kind='interp', line=610)
W('35,3200', 0o03576, '', '', 'DELEL', kind='operand', line=611)
W('35,3201', 0o00033, '', '', 'DELELO', kind='operand', line=612)
W('35,3202', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=613)
W('35,3203', 0o73213, '', '', 'NEXTES', kind='operand', line=614)
W('35,3204', 0o03574, '', '', 'SECMAX', kind='operand', line=615)
W('35,3205', 0o77605, '', 'DMP', kind='interp', line=616)
W('35,3206', 0o33736, '', '', 'THIRD', kind='operand', line=617)
W('35,3207', 0o17574, '', 'STODL', 'SECMAX', kind='interp', line=618)
# Page 670
W('35,3210', 0o70446, '', 'ABS', 'SR1', 'CROSSED OVER SOLUTION', kind='interp', line=620)
W('35,3211', 0o52076, '', 'DCOMP', 'GOTO', 'DT=(-SIGN(DTO)//DT//)/2', kind='interp', line=621)
W('35,3212', 0o73223, '', '', 'RESIGN', kind='operand', line=622)
W('35,3213', 0o51545, 'NEXTES', 'DLOAD', 'ABS', kind='interp', line=623)
W('35,3214', 0o03576, '', '', 'DELEL', kind='operand', line=624)
W('35,3215', 0o51525, '', 'PDDL', 'ABS', kind='interp', line=625)
W('35,3216', 0o00033, '', '', 'DELELO', kind='operand', line=626)
W('35,3217', 0o77625, '', 'DSU', kind='interp', line=627)
W('35,3220', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=628)
W('35,3221', 0o73226, '', '', 'REVERS', 'WRONG DIRECTION', kind='operand', line=629)
W('35,3222', 0o77646, '', 'ABS', kind='interp', line=630)
W('35,3223', 0o52165, 'RESIGN', 'SIGN', 'GOTO', kind='interp', line=631)
W('35,3224', 0o03606, '', '', 'DELTEEO', kind='operand', line=632)
W('35,3225', 0o73235, '', '', 'STORDELT', kind='operand', line=633)
W('35,3226', 0o57545, 'REVERS', 'DLOAD', 'DCOMP', kind='interp', line=634)
W('35,3227', 0o03606, '', '', 'DELTEEO', kind='operand', line=635)
W('35,3230', 0o70406, '', 'PUSH', 'SR1', kind='interp', line=636)
W('35,3231', 0o03606, '', 'STORE', 'DELTEEO', kind='interp', line=637)
W('35,3232', 0o77615, '', 'DAD', kind='interp', line=638)
W('35,3233', 0o77650, '', 'GOTO', kind='interp', line=639)
W('35,3234', 0o73236, '', '', 'ADTIME', kind='operand', line=640)
W('35,3235', 0o03606, 'STORDELT', 'STORE', 'DELTEEO', kind='interp', line=641)
W('35,3236', 0o77615, 'ADTIME', 'DAD', kind='interp', line=642)
W('35,3237', 0o02317, '', '', 'NOMTPI', "SUM OF DELTA T'S", kind='operand', line=643)
W('35,3240', 0o02317, '', 'STORE', 'NOMTPI', kind='interp', line=644)
W('35,3241', 0o63375, '', 'VLOAD', 'PDVL', kind='interp', line=645)
W('35,3242', 0o03506, '', '', 'VAPREC', kind='operand', line=646)
W('35,3243', 0o03500, '', '', 'RAPREC', kind='operand', line=647)
W('35,3244', 0o77624, '', 'CALL', kind='interp', line=648)
W('35,3245', 0o73462, '', '', 'GOINT', kind='operand', line=649)
W('35,3246', 0o77624, '', 'CALL', kind='interp', line=650)
W('35,3247', 0o46402, '', '', 'ACTIVE', 'STORE NEW RACT3 VACT3', kind='operand', line=651)
W('35,3250', 0o63375, '', 'VLOAD', 'PDVL', kind='interp', line=652)
W('35,3251', 0o03530, '', '', 'VPPREC', kind='operand', line=653)
W('35,3252', 0o03522, '', '', 'RPPREC', kind='operand', line=654)
W('35,3253', 0o77624, '', 'CALL', kind='interp', line=655)
W('35,3254', 0o73462, '', '', 'GOINT', kind='operand', line=656)
W('35,3255', 0o77624, '', 'CALL', kind='interp', line=657)
W('35,3256', 0o46412, '', '', 'PASSIVE', 'STORE NEW RPASS3 VPASS3', kind='operand', line=658)
W('35,3257', 0o77650, '', 'GOTO', kind='interp', line=659)
W('35,3260', 0o73004, '', '', 'ELCALC', kind='operand', line=660)
W('35,3261', 0o43345, 'ELEX', 'DLOAD', 'DAD', kind='interp', line=661)
W('35,3262', 0o03636, '', '', 'TTPI', kind='operand', line=662)
W('35,3263', 0o02317, '', '', 'NOMTPI', kind='operand', line=663)
W('35,3264', 0o17636, '', 'STODL', 'TTPI', kind='interp', line=664)
W('35,3265', 0o77614, '', 'BON', kind='interp', line=665)
W('35,3266', 0o01310, '', '', 'ETPIFLAG', kind='operand', line=666)
W('35,3267', 0o73271, '', '', 'TIMEX', kind='operand', line=667)
W('35,3270', 0o02257, '', 'STORE', 'ELEV', kind='interp', line=668)
W('35,3271', 0o52145, 'TIMEX', 'DLOAD', 'GOTO', kind='interp', line=669)
# Page 671
W('35,3272', 0o06522, '', '', 'ZEROVECS', kind='operand', line=671)
W('35,3273', 0o03463, '', '', 'NORMEX', kind='operand', line=672)

# Page 672
# ***** S34/35.1 *****

# COMPUTE UNIT NORMAL AND LINE OF SIGHT VECTORS GIVEN THE ACTIVE AND
# PASSIVE POS AND VEL AT TIME T3

W('35,3274', 0o52375, 'S34/35.1', 'VLOAD', 'VSU', kind='interp', line=680)
W('35,3275', 0o03552, '', '', 'RPASS3', kind='operand', line=681)
W('35,3276', 0o03536, '', '', 'RACT3', kind='operand', line=682)
W('35,3277', 0o41456, '', 'UNIT', 'PUSH', kind='interp', line=683)
W('35,3300', 0o26311, '', 'STOVL', 'ULOS', kind='interp', line=684)
W('35,3301', 0o03536, '', '', 'RACT3', kind='operand', line=685)
W('35,3302', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=686)
W('35,3303', 0o03544, '', '', 'VACT3', kind='operand', line=687)
W('35,3304', 0o02261, '', 'STORE', 'UNRM', kind='interp', line=688)
W('35,3305', 0o77616, '', 'RVQ', kind='interp', line=689)

# Page 673
# ***** S34/35.2 *****

# ADVANCE PASSIVE VEH TO RENDEZVOUS TIME AND GET REQ VEL FROM LAMBERT

W('35,3306', 0o77220, 'S34/35.2', 'STQ', 'VLOAD', kind='interp', line=696)
W('35,3307', 0o03470, '', '', 'SUBEXIT', kind='operand', line=697)
W('35,3310', 0o03560, '', '', 'VPASS3', kind='operand', line=698)
W('35,3311', 0o65315, '', 'PDVL', 'PDDL', kind='interp', line=699)
W('35,3312', 0o03552, '', '', 'RPASS3', kind='operand', line=700)
W('35,3313', 0o03610, '', '', 'INTIME', kind='operand', line=701)
W('35,3314', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=702)
W('35,3315', 0o03631, '', '', 'TPASS4', kind='operand', line=703)
W('35,3316', 0o33732, '', '', 'TWOPI', 'CONIC', kind='operand', line=704)
W('35,3317', 0o46125, '', 'PDDL', 'BHIZ', kind='interp', line=705)
W('35,3320', 0o03467, '', '', 'NN', kind='operand', line=706)
W('35,3321', 0o73325, '', '', 'S3435.23', kind='operand', line=707)
W('35,3322', 0o77745, '', 'DLOAD', kind='interp', line=708)
W('35,3323', 0o41545, '', 'DLOAD', 'PUSH', kind='interp', line=709)
W('35,3324', 0o06522, '', '', 'ZEROVECS', 'PRECISION', kind='operand', line=710)
W('35,3325', 0o77624, 'S3435.23', 'CALL', kind='interp', line=711)
W('35,3326', 0o73466, '', '', 'INTINT', 'GET TARGET VECTOR', kind='operand', line=712)
W('35,3327', 0o27444, 'S3435.25', 'STOVL', 'RTARG', kind='interp', line=713)
W('35,3330', 0o00007, '', '', 'VATT', kind='operand', line=714)
W('35,3331', 0o27506, '', 'STOVL', 'VPASS4', kind='interp', line=715)
W('35,3332', 0o03444, '', '', 'RTARG', kind='operand', line=716)
# COMPUTE PHI = PI + (ACOS(UNIT RA.UNIT RP) - PI)SIGN(RA*RP.U)
W('35,3333', 0o63256, '', 'UNIT', 'PDVL', 'UNIT RP', kind='interp', line=718)
W('35,3334', 0o03536, '', '', 'RACT3', kind='operand', line=719)
W('35,3335', 0o41456, '', 'UNIT', 'PUSH', 'UNIT RA', kind='interp', line=720)
W('35,3336', 0o50235, '', 'VXV', 'DOT', kind='interp', line=721)
W('35,3337', 0o00001, '', '', '0D', kind='operand', line=722)
W('35,3340', 0o02261, '', '', 'UNRM', 'RA*RP.U', kind='operand', line=723)
W('35,3341', 0o77715, '', 'PDVL', kind='interp', line=724)
W('35,3342', 0o72441, '', 'DOT', 'SL1', 'UNIT RA.UNIT RP', kind='interp', line=725)
W('35,3343', 0o00001, '', '', '0D', kind='operand', line=726)
W('35,3344', 0o75326, '', 'ACOS', 'SIGN', kind='interp', line=727)
W('35,3345', 0o43244, '', 'BPL', 'DAD', kind='interp', line=728)
W('35,3346', 0o73350, '', '', 'NOPIE', kind='operand', line=729)
W('35,3347', 0o06530, '', '', 'DPPOSMAX', 'REASONABLE TWO PI', kind='operand', line=730)
W('35,3350', 0o15756, 'NOPIE', 'STODL', 'ACTCENT', kind='interp', line=731)
W('35,3351', 0o03631, '', '', 'TPASS4', kind='operand', line=732)
W('35,3352', 0o77625, '', 'DSU', kind='interp', line=733)
W('35,3353', 0o03610, '', '', 'INTIME', kind='operand', line=734)
W('35,3354', 0o03452, '', 'STORE', 'DELLT4', kind='interp', line=735)
W('35,3355', 0o40335, '', 'SLOAD', 'SETPD', kind='interp', line=736)
W('35,3356', 0o03467, '', '', 'NN', 'NUMBER OF OFFSETS', kind='operand', line=737)
W('35,3357', 0o00001, '', '', '0D', kind='operand', line=738)
W('35,3360', 0o63325, '', 'PDDL', 'PDVL', kind='interp', line=739)
W('35,3361', 0o33744, '', '', 'EPSFOUR', kind='operand', line=740)
W('35,3362', 0o03536, '', '', 'RACT3', kind='operand', line=741)
W('35,3363', 0o26323, '', 'STOVL', 'RINIT', kind='interp', line=742)
# Page 674
W('35,3364', 0o03544, '', '', 'VACT3', kind='operand', line=744)
W('35,3365', 0o36331, '', 'STCALL', 'VINIT', kind='interp', line=745)
W('35,3366', 0o22000, '', '', 'INITVEL', kind='operand', line=746)
W('35,3367', 0o77624, '', 'CALL', kind='interp', line=747)
W('35,3370', 0o73447, '', '', 'LOMAT', kind='operand', line=748)
W('35,3371', 0o64375, '', 'VLOAD', 'MXV', kind='interp', line=749)
W('35,3372', 0o02366, '', '', 'DELVEET3', kind='operand', line=750)
W('35,3373', 0o00001, '', '', '0D', kind='operand', line=751)
W('35,3374', 0o77772, '', 'VSL1', kind='interp', line=752)
W('35,3375', 0o37434, '', 'STCALL', 'DELVLVC', kind='interp', line=753)
W('35,3376', 0o03470, '', '', 'SUBEXIT', kind='operand', line=754)

# Page 675
# ***** S34/35.3 *****

W('35,3377', 0o45020, 'S34/35.3', 'STQ', 'CALL', kind='interp', line=759)
W('35,3400', 0o03463, '', '', 'NORMEX', kind='operand', line=760)
W('35,3401', 0o73447, '', '', 'LOMAT', 'GET MATRIX IN PUSH LIST', kind='operand', line=761)
W('35,3402', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=762)
W('35,3403', 0o03434, '', '', 'DELVLVC', 'NEW DEL V TPI', kind='operand', line=763)
W('35,3404', 0o00001, '', '', '0D', kind='operand', line=764)
W('35,3405', 0o77772, '', 'VSL1', kind='interp', line=765)
W('35,3406', 0o02366, '', 'STORE', 'DELVEET3', 'SAVE FOR TRANSFORM', kind='interp', line=766)
W('35,3407', 0o63255, '', 'VAD', 'PDVL', kind='interp', line=767)
W('35,3410', 0o03544, '', '', 'VACT3', 'NEW V REQ', kind='operand', line=768)
W('35,3411', 0o03536, '', '', 'RACT3', kind='operand', line=769)
W('35,3412', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=770)
W('35,3413', 0o03442, '', '', 'TIG', kind='operand', line=771)
W('35,3414', 0o03631, '', '', 'TPASS4', kind='operand', line=772)
W('35,3415', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=773)
W('35,3416', 0o06530, '', '', 'DPPOSMAX', kind='operand', line=774)
W('35,3417', 0o77624, '', 'CALL', '', 'INTEG. FOR NEW TARGET VEC', kind='interp', line=775)
W('35,3420', 0o73466, '', '', 'INTINT', kind='operand', line=776)
W('35,3421', 0o77775, '', 'VLOAD', kind='interp', line=777)
W('35,3422', 0o00001, '', '', 'RATT', kind='operand', line=778)
W('35,3423', 0o03444, '', 'STORE', 'RTARG', kind='interp', line=779)
W('35,3424', 0o41575, 'NOVRWRT', 'VLOAD', 'PUSH', kind='interp', line=780)
W('35,3425', 0o02311, '', '', 'ULOS', kind='operand', line=781)
W('35,3426', 0o57435, '', 'VXV', 'VCOMP', kind='interp', line=782)
W('35,3427', 0o02261, '', '', 'UNRM', kind='operand', line=783)
W('35,3430', 0o41456, '', 'UNIT', 'PUSH', kind='interp', line=784)
W('35,3431', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=785)
W('35,3432', 0o02311, '', '', 'ULOS', kind='operand', line=786)
W('35,3433', 0o77715, '', 'PDVL', kind='interp', line=787)
W('35,3434', 0o64315, '', 'PDVL', 'MXV', kind='interp', line=788)
W('35,3435', 0o02366, '', '', 'DELVEET3', kind='operand', line=789)
W('35,3436', 0o00001, '', '', '0D', kind='operand', line=790)
W('35,3437', 0o77772, '', 'VSL1', kind='interp', line=791)
W('35,3440', 0o36303, '', 'STCALL', 'DVLOS', kind='interp', line=792)
W('35,3441', 0o03463, '', '', 'NORMEX', kind='operand', line=793)

# Page 676
# ***** S34/35.4 *****

W('35,3442', 0o40220, 'S34/35.4', 'STQ', 'SETPD', 'NO ASTRONAUT OVERWRITE', kind='interp', line=798)
W('35,3443', 0o03463, '', '', 'NORMEX', kind='operand', line=799)
W('35,3444', 0o00001, '', '', '0D', kind='operand', line=800)
W('35,3445', 0o77650, '', 'GOTO', kind='interp', line=801)
W('35,3446', 0o73424, '', '', 'NOVRWRT', kind='operand', line=802)

# Page 677
# ***** LOMAT *****

W('35,3447', 0o57575, 'LOMAT', 'VLOAD', 'VCOMP', kind='interp', line=807)
W('35,3450', 0o02261, '', '', 'UNRM', kind='operand', line=808)
W('35,3451', 0o24007, '', 'STOVL', '6D', 'Y', kind='interp', line=809)
W('35,3452', 0o03536, '', '', 'RACT3', kind='operand', line=810)
W('35,3453', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=811)
W('35,3454', 0o00015, '', 'STORE', '12D', kind='interp', line=812)
W('35,3455', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=813)
W('35,3456', 0o02261, '', '', 'UNRM', 'Z*-Y', kind='operand', line=814)
W('35,3457', 0o00001, '', 'STORE', '0D', kind='interp', line=815)
W('35,3460', 0o43401, '', 'SETPD', 'RVQ', kind='interp', line=816)
W('35,3461', 0o00023, '', '', '18D', kind='operand', line=817)
W('35,3462', 0o65325, 'GOINT', 'PDDL', 'PDDL', 'DO', kind='interp', line=818)
W('35,3463', 0o06522, '', '', 'ZEROVECS', '      NOT', kind='operand', line=819)
W('35,3464', 0o02317, '', '', 'NOMTPI', kind='operand', line=820)
W('35,3465', 0o41406, '', 'PUSH', 'PUSH', '              ORDER OR INSERT BEFORE INTINT', kind='interp', line=821)
W('35,3466', 0o45020, 'INTINT', 'STQ', 'CALL', kind='interp', line=822)
W('35,3467', 0o03465, '', '', 'RTRN', kind='operand', line=823)
W('35,3470', 0o27414, '', '', 'INTSTALL', kind='operand', line=824)
W('35,3471', 0o71214, '', 'CLEAR', 'DLOAD', kind='interp', line=825)
W('35,3472', 0o01673, '', '', 'INTYPFLG', kind='operand', line=826)
W('35,3473', 0o43054, '', 'BZE', 'SET', kind='interp', line=827)
W('35,3474', 0o73476, '', '', '+2', kind='operand', line=828)
W('35,3475', 0o01473, '', '', 'INTYPFLG', kind='operand', line=829)
W('35,3476', 0o45545, '', 'DLOAD', 'STADR', kind='interp', line=830)
W('35,3477', 0o63736, '', 'STODL', 'TDEC1', kind='interp', line=831)
W('35,3500', 0o73014, '', 'SET', 'LXA,2', kind='interp', line=832)
W('35,3501', 0o00063, '', '', 'MOONFLAG', kind='operand', line=833)
W('35,3502', 0o02777, '', '', 'RTX2', kind='operand', line=834)
W('35,3503', 0o43014, '', 'BON', 'CLEAR', kind='interp', line=835)
W('35,3504', 0o04303, '', '', 'CMOONFLG', kind='operand', line=836)
W('35,3505', 0o73507, '', '', 'ALLSET', kind='operand', line=837)
W('35,3506', 0o00263, '', '', 'MOONFLAG', kind='operand', line=838)
W('35,3507', 0o25517, 'ALLSET', 'STOVL', 'TET', kind='interp', line=839)
W('35,3510', 0o77657, '', 'VSR*', kind='interp', line=840)
W('35,3511', 0o57176, '', '', '0,2', kind='operand', line=841)
W('35,3512', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=842)
W('35,3513', 0o77657, '', 'VSR*', kind='interp', line=843)
W('35,3514', 0o57176, '', '', '0,2', kind='operand', line=844)
W('35,3515', 0o35543, '', 'STCALL', 'VCV', kind='interp', line=845)
W('35,3516', 0o27107, '', '', 'INTEGRVS', kind='operand', line=846)
W('35,3517', 0o52175, '', 'VLOAD', 'GOTO', kind='interp', line=847)
W('35,3520', 0o00001, '', '', 'RATT', kind='operand', line=848)
W('35,3521', 0o03465, '', '', 'RTRN', kind='operand', line=849)

# Page 678
# ***** S34/35.5 *****
# SUBROUTINES USED
# BANKCALL
# GOFLASH
# GOTOPOOH
# S34/35.3
# S34.35.4
# VNPOOH

W('35,3522', 0o43020, 'S34/35.5', 'STQ', 'BON', kind='interp', line=861)
W('35,3523', 0o03470, '', '', 'SUBEXIT', kind='operand', line=862)
W('35,3524', 0o01311, '', '', 'FINALFLG', kind='operand', line=863)
W('35,3525', 0o73531, '', '', 'FLAGON', kind='operand', line=864)
W('35,3526', 0o52014, '', 'SET', 'GOTO', kind='interp', line=865)
W('35,3527', 0o00470, '', '', 'UPDATFLG', kind='operand', line=866)
W('35,3530', 0o73576, '', '', 'FLAGOFF', kind='operand', line=867)
W('35,3531', 0o77214, 'FLAGON', 'CLEAR', 'VLOAD', kind='interp', line=868)
W('35,3532', 0o03274, '', '', 'NTARGFLG', kind='operand', line=869)
W('35,3533', 0o03434, '', '', 'DELVLVC', kind='operand', line=870)
W('35,3534', 0o01237, '', 'STORE', 'GDT/2', kind='interp', line=871)
W('35,3535', 0o77776, '', 'EXIT', kind='interp', line=872)
W('35,3536', 0o33727, '', 'CAF', 'V06N81', line=873)
W('35,3537', 0o04616, '', 'TC', 'BANKCALL', line=874)
W('35,3540', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=875)
W('35,3541', 0o06001, '', 'TC', 'GOTOPOOH', line=876)
W('35,3542', 0o03544, '', 'TC', '+2', 'PRO', line=877)
W('35,3543', 0o03536, '', 'TC', 'FLAGON +5', 'LOAD', line=878)
W('35,3544', 0o35016, '', 'CA', 'EBANK7', line=879)
W('35,3545', 0o54003, '', 'TS', 'EBANK', 'TO BE SURE', line=880)

W('35,3546', 0o22007, '', 'ZL', line=882)
W('35,3547', 0o34756, '', 'CA', 'FIVE', line=883)
W('35,3550', 0o54002, 'NTARGCHK', 'TS', 'Q', line=884)
W('35,3551', 0o50002, '', 'INDEX', 'Q', line=885)
W('35,3552', 0o41433, '', 'CS', 'DELVLVC', line=886)
W('35,3553', 0o50002, '', 'INDEX', 'Q', line=887)
W('35,3554', 0o61236, '', 'AD', 'GDT/2', line=888)
W('35,3555', 0o26001, '', 'ADS', 'L', line=889)
W('35,3556', 0o10002, '', 'CCS', 'Q', line=890)
W('35,3557', 0o13550, '', 'TCF', 'NTARGCHK', line=891)
W('35,3560', 0o22000, '', 'LXCH', 'A', line=892)
W('35,3561', 0o00006, '', 'EXTEND', line=893)
W('35,3562', 0o13565, '', 'BZF', '+3', line=894)
W('35,3563', 0o05504, '', 'TC', 'UPFLAG', line=895)
W('35,3564', 0o00146, '', 'ADRES', 'NTARGFLG', kind='data', line=896)

W('35,3565', 0o06037, '', 'TC', 'INTPRET', line=898)
W('35,3566', 0o45014, '', 'BOFF', 'CALL', kind='interp', line=899)
W('35,3567', 0o03354, '', '', 'NTARGFLG', kind='operand', line=900)
# Page 679
W('35,3570', 0o73572, '', '', 'NOCHG', kind='operand', line=902)
W('35,3571', 0o73377, '', '', 'S34/35.3', kind='operand', line=903)
W('35,3572', 0o77214, 'NOCHG', 'CLEAR', 'VLOAD', kind='interp', line=904)
W('35,3573', 0o01267, '', '', 'XDELVFLG', kind='operand', line=905)
W('35,3574', 0o02366, '', '', 'DELVEET3', kind='operand', line=906)
W('35,3575', 0o03656, '', 'STORE', 'DELVSIN', kind='interp', line=907)
W('35,3576', 0o77624, 'FLAGOFF', 'CALL', kind='interp', line=908)
W('35,3577', 0o73442, '', '', 'S34/35.4', kind='operand', line=909)
W('35,3600', 0o77776, '', 'EXIT', kind='interp', line=910)
W('35,3601', 0o33726, '', 'CAF', 'V06N59', line=911)
W('35,3602', 0o03712, '', 'TC', 'VNPOOH', line=912)
W('35,3603', 0o06037, '', 'TC', 'INTPRET', line=913)
W('35,3604', 0o77650, '', 'GOTO', kind='interp', line=914)
W('35,3605', 0o03470, '', '', 'SUBEXIT', kind='operand', line=915)

# Page 680
# ***** VN1645 *****
#
# SUBROUTINES USED
# P3XORP7X
# GET+MGA
# BANKCALL
# DELAYJOB
# COMPTGO
# GOFLASHR
# GOTOPOOH
# FLAGUP

W('35,3606', 0o71220, 'VN1645', 'STQ', 'DLOAD', kind='interp', line=930)
W('35,3607', 0o03470, '', '', 'SUBEXIT', kind='operand', line=931)
W('35,3610', 0o33742, '', '', 'DP-.01', kind='operand', line=932)
W('35,3611', 0o02253, '', 'STORE', '+MGA', 'MGA = -.01', kind='interp', line=933)
W('35,3612', 0o71214, '', 'BOFF', 'DLOAD', kind='interp', line=934)
W('35,3613', 0o01351, '', '', 'FINALFLG', kind='operand', line=935)
W('35,3614', 0o73634, '', '', 'GET45', kind='operand', line=936)
W('35,3615', 0o33742, '', '', 'DP-.01', kind='operand', line=937)
W('35,3616', 0o77615, '', 'DAD', kind='interp', line=938)
W('35,3617', 0o33742, '', '', 'DP-.01', kind='operand', line=939)
W('35,3620', 0o02253, '', 'STORE', '+MGA', 'MGA = -.02', kind='interp', line=940)
W('35,3621', 0o77414, '', 'BOFF', 'EXIT', kind='interp', line=941)
W('35,3622', 0o01742, '', '', 'REFSMFLG', kind='operand', line=942)
W('35,3623', 0o73634, '', '', 'GET45', kind='operand', line=943)
W('35,3624', 0o03704, '', 'TC', 'P3XORP7X', line=944)
W('35,3625', 0o03627, '', 'TC', '+2', 'P3X', line=945)
W('35,3626', 0o03635, '', 'TC', 'GET45 +1', 'P7X', line=946)
W('35,3627', 0o06037, '', 'TC', 'INTPRET', line=947)
W('35,3630', 0o41575, '', 'VLOAD', 'PUSH', kind='interp', line=948)
W('35,3631', 0o03656, '', '', 'DELVSIN', kind='operand', line=949)
W('35,3632', 0o77624, '', 'CALL', '', 'COMPUTE MGA', kind='interp', line=950)
W('35,3633', 0o15717, '', '', 'GET+MGA', kind='operand', line=951)
W('35,3634', 0o77776, 'GET45', 'EXIT', kind='interp', line=952)
W('35,3635', 0o02432, '', 'TC', 'COMPTGO', 'INITIATE TASK TO UPDATE TTOGO', line=953)
W('35,3636', 0o31470, '', 'CA', 'SUBEXIT', line=954)
W('35,3637', 0o55464, '', 'TS', 'QSAVED', line=955)
W('35,3640', 0o34777, '', 'CAF', '1SEC', line=956)
W('35,3641', 0o04616, '', 'TC', 'BANKCALL', line=957)
W('35,3642', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=958)
W('35,3643', 0o33730, '', 'CAF', 'V16N45', 'TRKMKCNT, TTOGO, +MGA', line=959)
W('35,3644', 0o04616, '', 'TC', 'BANKCALL', line=960)
W('35,3645', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=961)
W('35,3646', 0o03651, '', 'TC', 'KILCLOCK', 'TERMINATE', line=962)
W('35,3647', 0o03654, '', 'TC', 'N45PROC', 'PROCEED', line=963)
W('35,3650', 0o03664, '', 'TC', 'CLUPDATE', 'RECYCLE -- RETURN FOR INITIAL COMPUTATION', line=964)
W('35,3651', 0o30005, 'KILCLOCK', 'CA', 'Z', line=965)
W('35,3652', 0o55163, '', 'TS', 'DISPDEX', line=966)
# Page 681
W('35,3653', 0o06001, '', 'TC', 'GOTOPOOH', line=968)
W('35,3654', 0o40076, 'N45PROC', 'CS', 'FLAGWRD2', line=969)
W('35,3655', 0o74746, '', 'MASK', 'BIT6', line=970)
W('35,3656', 0o00006, '', 'EXTEND', line=971)
W('35,3657', 0o13651, '', 'BZF', 'KILCLOCK', 'FINALFLG IS SET -- FLASH V37 -- AWAIT NEW PGM', line=972)
W('35,3660', 0o05353, '', 'TC', 'PHASCHNG', line=973)
W('35,3661', 0o04024, '', 'OCT', '04024', kind='data', line=974)
W('35,3662', 0o05504, '', 'TC', 'UPFLAG', 'SET', line=975)
W('35,3663', 0o00047, '', 'ADRES', 'FINALFLG', 'FINALFLG', kind='data', line=976)
W('35,3664', 0o30005, 'CLUPDATE', 'CA', 'Z', line=977)
W('35,3665', 0o55163, '', 'TS', 'DISPDEX', line=978)
W('35,3666', 0o05353, '', 'TC', 'PHASCHNG', line=979)
W('35,3667', 0o04024, '', 'OCT', '04024', kind='data', line=980)
W('35,3670', 0o06037, '', 'TC', 'INTPRET', line=981)
W('35,3671', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=982)
W('35,3672', 0o00670, '', '', 'UPDATFLG', kind='operand', line=983)
W('35,3673', 0o03464, '', '', 'QSAVED', kind='operand', line=984)

# Page 682
# ***** DISPLAYE *****
#
# SUBROUTINES USED
# BANKCALL
# GOFLASHR
# GOTOPOOH
# BLANKET
# ENDOFJOB

W('35,3674', 0o00006, 'DISPLAYE', 'EXTEND', line=996)
W('35,3675', 0o23463, '', 'QXCH', 'NORMEX', line=997)
W('35,3676', 0o33724, '', 'CAF', 'V06N55', line=998)
W('35,3677', 0o04616, '', 'TCR', 'BANKCALL', line=999)
W('35,3700', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=1000)
W('35,3701', 0o16001, '', 'TCF', 'GOTOPOOH', line=1001)
W('35,3702', 0o01463, '', 'TC', 'NORMEX', line=1002)
W('35,3703', 0o13676, '', 'TCF', '-5', line=1003)

# Page 683
# ***** P3XORP7X *****

W('35,3704', 0o37744, 'P3XORP7X', 'CAF', 'HIGH9', line=1008)
W('35,3705', 0o71011, '', 'MASK', 'MODREG', line=1009)
W('35,3706', 0o00006, '', 'EXTEND', line=1010)
W('35,3707', 0o13711, '', 'BZF', '+2', line=1011)
W('35,3710', 0o24002, '', 'INCR', 'Q', line=1012)
W('35,3711', 0o00002, '', 'RETURN', line=1013)

# ***** VNPOOH *****
#
# SUBROUTINES USED
# BANKCALL
# GOFLASH
# GOTOPOOH

W('35,3712', 0o00006, 'VNPOOH', 'EXTEND', line=1022)
W('35,3713', 0o23465, '', 'QXCH', 'RTRN', line=1023)
W('35,3714', 0o55615, '', 'TS', 'VERBNOUN', line=1024)
W('35,3715', 0o31615, '', 'CA', 'VERBNOUN', line=1025)
W('35,3716', 0o04616, '', 'TCR', 'BANKCALL', line=1026)
W('35,3717', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=1027)
W('35,3720', 0o16001, '', 'TCF', 'GOTOPOOH', line=1028)
W('35,3721', 0o01465, '', 'TC', 'RTRN', line=1029)
W('35,3722', 0o13715, '', 'TCF', '-5', line=1030)

# Page 684
# ***** CONSTANTS *****

W('35,3723', 0o01445, 'V06N37', 'VN', '0637', kind='data', line=1035)
W('35,3724', 0o01467, 'V06N55', 'VN', '0655', kind='data', line=1036)
W('35,3725', 0o01472, 'V06N58', 'VN', '0658', kind='data', line=1037)
W('35,3726', 0o01473, 'V06N59', 'VN', '0659', kind='data', line=1038)
W('35,3727', 0o01521, 'V06N81', 'VN', '0681', kind='data', line=1039)
W('35,3730', 0o04055, 'V16N45', 'VN', '1645', kind='data', line=1040)
W('35,3731', 0o14441, 'TWOPI', '2DEC', '6.283185307 B-4', kind='data', line=1041)
W('35,3732', 0o37325, kind='data', line=1041)

W('35,3733', 0o00001, 'MAX250', '2DEC', '25 E3', kind='data', line=1043)
W('35,3734', 0o20650, kind='data', line=1043)

W('35,3735', 0o12525, 'THIRD', '2DEC', '.333333333', kind='data', line=1045)
W('35,3736', 0o12525, kind='data', line=1045)

W('35,3737', 0o00004, 'ELEPS', '2DEC', '.27777777 E-3', kind='data', line=1047)
W('35,3740', 0o21505, kind='data', line=1047)

W('35,3741', 0o77777, 'DP-.01', 'OCT', '77777', 'CONSTANTS', kind='data', line=1049)
W('35,3742', 0o61337, '', 'OCT', '61337', 'ADJACENT      -.01 FOR MGA DSP', kind='data', line=1050)
W('35,3743', 0o01252, 'EPSFOUR', '2DEC', '.0416666666', kind='data', line=1051)
W('35,3744', 0o25253, kind='data', line=1051)

W('35,3745', 0o13434, '130DEG', '2DEC', '.3611111111', kind='data', line=1053)
W('35,3746', 0o16162, kind='data', line=1053)

# Page 685
# ***** INITVEL *****

# MOD NO -1                     LOG SECTION -- P34-P35, P74-P75
# MOD BY WHITE, P.              DATE:  21 NOV 67
#
# FUNCTIONAL
#
# THIS SUBROUTINE COMPUTES THE REQUIRED INITIAL VELOCITY VECTOR FOR
# A TRAJECTORY OF SPECIFIC TRANSFER TIME BETWEEN SPECIFIED INITIAL
# AND TARGET POSITIONS.  THE TRAJECTORY MAY BE EITHER CONIC OR
# PRECISION DEPENDING ON AN INPUT PARAMETER (NAMELY, NUMBER OF
# OFFSETS).  IN ADDITION, IN THE PRECISION TRAJECTORY CASE, THE
# SUBROUTINE ALSO COMPUTES AN OFFSET TARGET VECTOR, TO BE USED
# DURING PURE-CONIC CROSS-PRODUCT STEERING.  THE OFFSET TARGET
# VECTOR IS THE TERMINAL POSITION VECTOR OF A CONIC TRAJECTORY WHICH
# HAS THE SAME INITIAL STATE AS A PRECISION TRAJECTORY WHOSE
# TERMINAL POSITION VECTOR IS THE SPECIFIED TARGET VECTOR.
#
# IN ORDER TO AVOID THE INHERENT SINGULARITIES IN THE 180 DEGREE
# TRANSFER CASE WHEN THE (TRUE OR OFFSET) TARGET VECTOR MAY BE
# SLIGHTLY OUT OF THE ORBITAL PLANE, THIS SUBROUTINE ROTATES THIS
# VECTOR INTO A PLANE DEFINED BY THE INPUT INITIAL POSITION VECTOR
# AND ANOTHER INPUT VECTOR (USUALLY THE INITIAL VELOCITY VECTOR),
# WHENEVER THE INPUT TARGET VECTOR LIES INSIDE A CONE WHOSE VERTEX
# IS THE ORIGIN OF COORDINATES, WHOSE AXIS IS THE 180 DEGREE
# TRANSFER DIRECTION, AND WHOSE CONE ANGLE IS SPECIFIED BY THE USER.
#
# THE LAMBERT SUBROUTINE IS UTILIZED FOR THE CONIC COMPUTATIONS AND
# THE COASTING INTEGRATION SUBROUTINE IS UTILIZED FOR THE PRECISION
# TRAJECTORY COMPUTATIONS.
#
# CALLING SEQUENCE
#
# L       CALL
# L+1             INITVEL
# L+2     (RETURN -- ALWAYS)
#
# INPUT
#
# (1)     RINIT           INITIAL POSITION RADIUS VECTOR
# (2)     VINIT           INITIAL POSITION VELOCITY VECTOR
# (3)     RTARG           TARGET POSITION RADIUS VECTOR
# (4)     DELLT4          DESIRED TIME OF FLIGHT FROM RINIT TO RTARG
# (5)     INTIME          TIME OF RINIT
# (6)     0D              NUMBER OF ITERATIONS OF LAMBERT/INTEGRVS
# (7)     2D              ANGLE TO 180 DEGREES WHEN ROTATION STARTS
# (8)     RTX1            -2 FOR EARTH, -10D FOR LUNAR
# (9)     RTX2            COORDINATE SYSTEM ORIGIN -- 0 FOR EARTH, 2 FOR LUNAR
# PUSHLOC SET AT 4D
#
# Page 686
# OUTPUT
#
# (1)     RTARG           OFFSET TARGET POSITION VECTOR
# (2)     VIPRIME         MANEUVER VELOCITY REQUIRED
# (3)     VTPRIME         VELOCITY AT TARGET AFTER MANEUVER
# (4)     DELVEET3        DELTA VELOCITY REQUIRED FOR MANEUVER
#
# SUBROUTINES USED
#
# LAMBERT
# INTSTALL
# INTEGRVS

#   SETLOC INTVEL
#   BANK

#   COUNT* $$/INITV
W('11,2000', 0o77614, 'INITVEL', 'SET', '', 'COGA GUESS NOT AVAILABLE', kind='interp', line=1124)
W('11,2001', 0o00475, '', '', 'GUESSW', kind='operand', line=1125)
W('11,2002', 0o44175, 'HAVEGUES', 'VLOAD', 'STQ', kind='interp', line=1126)
W('11,2003', 0o03444, '', '', 'RTARG', kind='operand', line=1127)
W('11,2004', 0o03463, '', '', 'NORMEX', kind='operand', line=1128)
W('11,2005', 0o03472, '', 'STORE', 'RTARG1', kind='interp', line=1129)
W('11,2006', 0o77646, '', 'ABVAL', kind='interp', line=1130)
W('11,2007', 0o03723, '', 'STORE', 'RTMAG', kind='interp', line=1131)
W('11,2010', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=1132)
W('11,2011', 0o03000, '', '', 'RTX2', kind='operand', line=1133)
W('11,2012', 0o22026, '', '', 'INITVEL1', kind='operand', line=1134)
W('11,2013', 0o72575, '', 'VLOAD', 'VSL2', kind='interp', line=1135)
W('11,2014', 0o02323, '', '', 'RINIT', 'B29', kind='operand', line=1136)
W('11,2015', 0o26323, '', 'STOVL', 'RINIT', 'B27', kind='interp', line=1137)
W('11,2016', 0o02331, '', '', 'VINIT', 'B7', kind='operand', line=1138)
W('11,2017', 0o77752, '', 'VSL2', kind='interp', line=1139)
W('11,2020', 0o26331, '', 'STOVL', 'VINIT', 'B5', kind='interp', line=1140)
W('11,2021', 0o03472, '', '', 'RTARG1', kind='operand', line=1141)
W('11,2022', 0o77752, '', 'VSL2', kind='interp', line=1142)
W('11,2023', 0o03472, '', 'STORE', 'RTARG1', kind='interp', line=1143)
W('11,2024', 0o77646, '', 'ABVAL', kind='interp', line=1144)
W('11,2025', 0o03723, '', 'STORE', 'RTMAG', kind='interp', line=1145)

# INITIALIZATION

W('11,2026', 0o71331, 'INITVEL1', 'SSP', 'DLOAD', 'SET ITCTR TO -1,LOAD MPAC WITH E4 (PL 2D)', kind='interp', line=1149)
W('11,2027', 0o03617, '', '', 'ITCTR', kind='operand', line=1150)
W('11,2030', 0o77776, '', '', '0 -1', kind='operand', line=1151)
W('11,2031', 0o70546, '', 'COSINE', 'SR1', 'CALCULATE COSINE (E4) (+2)', kind='interp', line=1152)
W('11,2032', 0o17667, '', 'STODL', 'COZY4', 'SET COZY4 TO COSINE (E4)          (PL 0D)', kind='interp', line=1153)
W('11,2033', 0o67154, '', 'LXA,2', 'SXA,2', kind='interp', line=1154)
W('11,2034', 0o00154, '', '', 'MPAC', kind='operand', line=1155)
W('11,2035', 0o02701, '', '', 'VTARGTAG', 'SET VTARGTAG TO 0D (SP)', kind='operand', line=1156)
W('11,2036', 0o77775, '', 'VLOAD', kind='interp', line=1157)
# Page 687
W('11,2037', 0o02323, '', '', 'RINIT', kind='operand', line=1159)
W('11,2040', 0o26655, '', 'STOVL', 'R1VEC', 'R1VEC EQ RINIT', kind='interp', line=1160)
W('11,2041', 0o03472, '', '', 'RTARG1', kind='operand', line=1161)
W('11,2042', 0o16663, '', 'STODL', 'R2VEC', 'R2VEC EQ RTARG', kind='interp', line=1162)
W('11,2043', 0o03452, '', '', 'DELLT4', kind='operand', line=1163)
W('11,2044', 0o02671, '', 'STORE', 'TDESIRED', 'TDESIRED EQ DELLT4', kind='interp', line=1164)
W('11,2045', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=1165)
W('11,2046', 0o00001, '', '', '0D', 'INITIALIZE PL TO 0D', kind='operand', line=1166)
W('11,2047', 0o02323, '', '', 'RINIT', 'MPAC EQ RINIT (+29)', kind='operand', line=1167)
W('11,2050', 0o41456, '', 'UNIT', 'PUSH', 'UNIT(RI) (+1)                     (PL 6D)', kind='interp', line=1168)
W('11,2051', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1169)
W('11,2052', 0o02331, '', '', 'VINIT', 'MPAC EQ UNIT(RI) X VI (+8)', kind='operand', line=1170)
W('11,2053', 0o26674, '', 'STOVL', 'UN', kind='interp', line=1171)
W('11,2054', 0o03472, '', '', 'RTARG1', kind='operand', line=1172)
W('11,2055', 0o50256, '', 'UNIT', 'DOT', 'TEMP*RT.URI (+2)                  (PL 0D)', kind='interp', line=1173)
W('11,2056', 0o43015, '', 'DAD', 'CLEAR', kind='interp', line=1174)
W('11,2057', 0o03667, '', '', 'COZY4', kind='operand', line=1175)
W('11,2060', 0o03665, '', '', 'NORMSW', kind='operand', line=1176)
W('11,2061', 0o03667, '', 'STORE', 'COZY4', kind='interp', line=1177)
W('11,2062', 0o43044, 'INITVEL2', 'BPL', 'SET', kind='interp', line=1178)
W('11,2063', 0o22105, '', '', 'INITVEL3', 'UN CALCULATED IN LAMBERT', kind='operand', line=1179)
W('11,2064', 0o03465, '', '', 'NORMSW', kind='operand', line=1180)

# ROTATE RC INTO YC PLANE -- SET UNIT NORMAL TO YC

W('11,2065', 0o41575, '', 'VLOAD', 'PUSH', '                                  (PL 6D)', kind='interp', line=1184)
W('11,2066', 0o02663, '', '', 'R2VEC', 'RC TO 6D (+29)', kind='operand', line=1185)
W('11,2067', 0o63246, '', 'ABVAL', 'PDVL', 'RC TO MPAC, ABVAL(RC) (+29) TO OD (PL 2D)', kind='interp', line=1186)
W('11,2070', 0o46206, '', 'PUSH', 'VPROJ', '                                  (PL 8D)', kind='interp', line=1187)
W('11,2071', 0o02674, '', '', 'UN', kind='operand', line=1188)
W('11,2072', 0o51352, '', 'VSL2', 'BVSU', kind='interp', line=1189)
W('11,2073', 0o74256, '', 'UNIT', 'VXSC', '                                  (PL 0D)', kind='interp', line=1190)
W('11,2074', 0o77772, '', 'VSL1', kind='interp', line=1191)
W('11,2075', 0o02663, '', 'STORE', 'R2VEC', kind='interp', line=1192)
W('11,2076', 0o67351, '', 'TLOAD', 'SLOAD', kind='interp', line=1193)
W('11,2077', 0o24007, '', '', 'ZEROVEC', kind='operand', line=1194)
W('11,2100', 0o03617, '', '', 'ITCTR', kind='operand', line=1195)
W('11,2101', 0o77244, '', 'BPL', 'VLOAD', kind='interp', line=1196)
W('11,2102', 0o22105, '', '', 'INITVEL3', kind='operand', line=1197)
W('11,2103', 0o02663, '', '', 'R2VEC', kind='operand', line=1198)
W('11,2104', 0o03472, '', 'STORE', 'RTARG1', kind='interp', line=1199)
W('11,2105', 0o63345, 'INITVEL3', 'DLOAD', 'PDVL', '                                  (PL 2D)', kind='interp', line=1200)
W('11,2106', 0o26007, '', '', 'MUEARTH', 'POSITIVE VALUE', kind='operand', line=1201)
W('11,2107', 0o02663, '', '', 'R2VEC', kind='operand', line=1202)
W('11,2110', 0o63256, '', 'UNIT', 'PDVL', '2D = UNIT(R2VEC)                  (PL 8D)', kind='interp', line=1203)
W('11,2111', 0o02655, '', '', 'R1VEC', kind='operand', line=1204)
W('11,2112', 0o41456, '', 'UNIT', 'PUSH', '8D = UNIT(R1VEC)                 (PL 14D)', kind='interp', line=1205)
W('11,2113', 0o57435, '', 'VXV', 'VCOMP', '-N = UNIT(R2VEC) X UNIT(R1VEC)', kind='interp', line=1206)
W('11,2114', 0o00003, '', '', '2D', kind='operand', line=1207)
W('11,2115', 0o77606, '', 'PUSH', '', '                                 (PL 20D)', kind='interp', line=1208)
W('11,2116', 0o71350, '', 'LXA,1', 'DLOAD', kind='interp', line=1209)
# Page 688
W('11,2117', 0o02776, '', '', 'RTX1', kind='operand', line=1211)
W('11,2120', 0o00023, '', '', '18D', kind='operand', line=1212)
W('11,2121', 0o62040, '', 'BMN', 'INCR,1', kind='interp', line=1213)
W('11,2122', 0o22124, '', '', '+2', kind='operand', line=1214)
W('11,2123', 0o77767, '', 'DEC', '-8', kind='data', line=1215)
W('11,2124', 0o67310, '', 'INCR,1', 'SLOAD', kind='interp', line=1216)
W('11,2125', 0o00012, '', '', '10D', kind='operand', line=1217)
W('11,2126', 0o00047, '', '', 'X1', kind='operand', line=1218)
W('11,2127', 0o77230, '', 'BHIZ', 'VLOAD', '                                 (PL 14D)', kind='interp', line=1219)
W('11,2130', 0o22132, '', '', '+2', kind='operand', line=1220)
W('11,2131', 0o41476, '', 'VCOMP', 'PUSH', '                                 (PL 20D)', kind='interp', line=1221)
W('11,2132', 0o77775, '', 'VLOAD', '', '                                 (PL 14D)', kind='interp', line=1222)
W('11,2133', 0o50235, '', 'VXV', 'DOT', '                                  (PL 2D)', kind='interp', line=1223)
W('11,2134', 0o71244, '', 'BPL', 'DLOAD', '                                  (PL 0D)', kind='interp', line=1224)
W('11,2135', 0o22137, '', '', 'INITVEL4', kind='operand', line=1225)
W('11,2136', 0o41476, '', 'DCOMP', 'PUSH', '                                  (PL 2D)', kind='interp', line=1226)
W('11,2137', 0o67154, 'INITVEL4', 'LXA,2', 'SXA,2', kind='interp', line=1227)
W('11,2140', 0o00000, '', '', '0D', kind='operand', line=1228)
W('11,2141', 0o02672, '', '', 'GEOMSGN', kind='operand', line=1229)

# SET INPUTS UP FOR LAMBERT

W('11,2142', 0o45150, '', 'LXA,1', 'CALL', kind='interp', line=1233)
W('11,2143', 0o02776, '', '', 'RTX1', kind='operand', line=1234)

# OPERATE THE LAMBERT CONIC ROUTINE (COASTFLT SUBROUTINE)

W('11,2144', 0o23765, '', '', 'SETITCTR', 'GO TO END OF BANK TO SET ITERCTR BEFORE', kind='operand', line=1238)
# CALLING LAMBER (FOR REMANUFACTURE ONLY)

# ARRIVED AT SOLUTION IS GOOD ENOUGH ACCORDING TO SLIGHTLY WIDER BOUNDS.

W('11,2145', 0o77214, '', 'CLEAR', 'VLOAD', kind='interp', line=1243)
W('11,2146', 0o00675, '', '', 'GUESSW', kind='operand', line=1244)
W('11,2147', 0o02744, '', '', 'VVEC', kind='operand', line=1245)

# STORE CALCULATED INITIAL VELOCITY REQUIRED IN VIPRIME

W('11,2150', 0o16337, '', 'STODL', 'VIPRIME', 'INITIAL VELOCITY REQUIRED (+7)', kind='interp', line=1249)

# IF NUMIT IS ZERO, CONTINUE AT INITVELB, OTHERWISE
# SET UP INPUTS FOR ENCKE INTEGRATION (INTEGRVS).

W('11,2151', 0o02702, '', '', 'VTARGTAG', kind='operand', line=1254)
W('11,2152', 0o45030, '', 'BHIZ', 'CALL', kind='interp', line=1255)
W('11,2153', 0o22230, '', '', 'INITVEL7', kind='operand', line=1256)
W('11,2154', 0o27414, '', '', 'INTSTALL', kind='operand', line=1257)
W('11,2155', 0o43135, '', 'SLOAD', 'CLEAR', kind='interp', line=1258)
W('11,2156', 0o03000, '', '', 'RTX2', kind='operand', line=1259)
W('11,2157', 0o00263, '', '', 'MOONFLAG', kind='operand', line=1260)
W('11,2160', 0o43030, '', 'BHIZ', 'SET', kind='interp', line=1261)
W('11,2161', 0o22163, '', '', 'INITVEL5', kind='operand', line=1262)
# Page 689
W('11,2162', 0o00063, '', '', 'MOONFLAG', kind='operand', line=1264)
W('11,2163', 0o77775, 'INITVEL5', 'VLOAD', kind='interp', line=1265)
W('11,2164', 0o02323, '', '', 'RINIT', kind='operand', line=1266)
W('11,2165', 0o02655, '', 'STORE', 'R1VEC', kind='interp', line=1267)
W('11,2166', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=1268)
W('11,2167', 0o02337, '', '', 'VIPRIME', kind='operand', line=1269)
W('11,2170', 0o15543, '', 'STODL', 'VCV', kind='interp', line=1270)
W('11,2171', 0o03610, '', '', 'INTIME', kind='operand', line=1271)
W('11,2172', 0o01517, '', 'STORE', 'TET', kind='interp', line=1272)
W('11,2173', 0o43015, '', 'DAD', 'CLEAR', kind='interp', line=1273)
W('11,2174', 0o03452, '', '', 'DELLT4', kind='operand', line=1274)
W('11,2175', 0o01673, '', '', 'INTYPFLG', kind='operand', line=1275)
W('11,2176', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1276)
W('11,2177', 0o27107, '', '', 'INTEGRVS', kind='operand', line=1277)
W('11,2200', 0o77775, '', 'VLOAD', kind='interp', line=1278)
W('11,2201', 0o00025, '', '', 'VATT1', kind='operand', line=1279)
W('11,2202', 0o02703, '', 'STORE', 'VTARGET', kind='interp', line=1280)

# IF ITERATION COUNTER (ITCTR) EQ NO. ITERATIONS (NUMIT), CONTINUE AT
# INITVELC, OTHERWISE REITERATE LAMBERT AND ENCKE

W('11,2203', 0o63154, '', 'LXA,2', 'INCR,2', kind='interp', line=1285)
W('11,2204', 0o03616, '', '', 'ITCTR', kind='operand', line=1286)
W('11,2205', 0o00001, '', '', '1D', 'INCREMENT ITCTR', kind='operand', line=1287)
W('11,2206', 0o55134, '', 'SXA,2', 'XSU,2', kind='interp', line=1288)
W('11,2207', 0o03616, '', '', 'ITCTR', kind='operand', line=1289)
W('11,2210', 0o02701, '', '', 'VTARGTAG', kind='operand', line=1290)
W('11,2211', 0o46135, '', 'SLOAD', 'BHIZ', 'IF SP(MPAC) EQ 0, CONTINUE AT INITVELC', kind='interp', line=1291)
W('11,2212', 0o00050, '', '', 'X2', kind='operand', line=1292)
W('11,2213', 0o22225, '', '', 'INITVEL6', kind='operand', line=1293)

# OFFSET CONIC TARGET VECTOR

W('11,2214', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=1297)
W('11,2215', 0o03472, '', '', 'RTARG1', kind='operand', line=1298)
W('11,2216', 0o00017, '', '', 'RATT1', kind='operand', line=1299)
W('11,2217', 0o77655, '', 'VAD', kind='interp', line=1300)
W('11,2220', 0o02663, '', '', 'R2VEC', kind='operand', line=1301)
W('11,2221', 0o16663, '', 'STODL', 'R2VEC', kind='interp', line=1302)
W('11,2222', 0o03667, '', '', 'COZY4', kind='operand', line=1303)
W('11,2223', 0o77650, '', 'GOTO', kind='interp', line=1304)
W('11,2224', 0o22062, '', '', 'INITVEL2', 'CONTINUE ITERATING AT INITVEL2', kind='operand', line=1305)

# COMPUTE THE DELTA VELOCITY

W('11,2225', 0o77775, 'INITVEL6', 'VLOAD', kind='interp', line=1309)
W('11,2226', 0o02663, '', '', 'R2VEC', kind='operand', line=1310)
W('11,2227', 0o03472, '', 'STORE', 'RTARG1', kind='interp', line=1311)
W('11,2230', 0o52375, 'INITVEL7', 'VLOAD', 'VSU', kind='interp', line=1312)
W('11,2231', 0o02337, '', '', 'VIPRIME', kind='operand', line=1313)
W('11,2232', 0o02331, '', '', 'VINIT', kind='operand', line=1314)
W('11,2233', 0o26366, '', 'STOVL', 'DELVEET3', 'DELVEET3 = VIPRIME-VINIT (+7)', kind='interp', line=1315)
# Page 690
W('11,2234', 0o02703, '', '', 'VTARGET', kind='operand', line=1317)
W('11,2235', 0o03566, '', 'STORE', 'VTPRIME', kind='interp', line=1318)
W('11,2236', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=1319)
W('11,2237', 0o03000, '', '', 'RTX2', kind='operand', line=1320)
W('11,2240', 0o22255, '', '', 'INITVELX', kind='operand', line=1321)
W('11,2241', 0o70575, '', 'VLOAD', 'VSR2', kind='interp', line=1322)
W('11,2242', 0o03566, '', '', 'VTPRIME', kind='operand', line=1323)
W('11,2243', 0o27566, '', 'STOVL', 'VTPRIME', kind='interp', line=1324)
W('11,2244', 0o02337, '', '', 'VIPRIME', kind='operand', line=1325)
W('11,2245', 0o77742, '', 'VSR2', kind='interp', line=1326)
W('11,2246', 0o26337, '', 'STOVL', 'VIPRIME', kind='interp', line=1327)
W('11,2247', 0o03472, '', '', 'RTARG1', kind='operand', line=1328)
W('11,2250', 0o77742, '', 'VSR2', kind='interp', line=1329)
W('11,2251', 0o27472, '', 'STOVL', 'RTARG1', kind='interp', line=1330)
W('11,2252', 0o02366, '', '', 'DELVEET3', kind='operand', line=1331)
W('11,2253', 0o77742, '', 'VSR2', kind='interp', line=1332)
W('11,2254', 0o02366, '', 'STORE', 'DELVEET3', kind='interp', line=1333)
W('11,2255', 0o70750, 'INITVELX', 'LXA,1', 'DLOAD*', kind='interp', line=1334)
W('11,2256', 0o02776, '', '', 'RTX1', kind='operand', line=1335)
W('11,2257', 0o10003, '', '', 'MUTABLE -2,1', kind='operand', line=1336)
W('11,2260', 0o41206, '', 'PUSH', 'DMP', kind='interp', line=1337)
W('11,2261', 0o02742, '', '', 'R1A', kind='operand', line=1338)
W('11,2262', 0o56342, '', 'SR1', 'DDV', kind='interp', line=1339)
W('11,2263', 0o00041, '', '', 'R1', kind='operand', line=1340)
W('11,2264', 0o17721, '', 'STODL', 'MU/A', kind='interp', line=1341)
W('11,2265', 0o77661, '', 'SR', kind='interp', line=1342)
W('11,2266', 0o20607, '', '', '6', kind='operand', line=1343)
W('11,2267', 0o03717, '', 'STORE', 'MUASTEER', kind='interp', line=1344)
W('11,2270', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=1345)
W('11,2271', 0o00001, '', '', '0D', kind='operand', line=1346)
W('11,2272', 0o03472, '', '', 'RTARG1', kind='operand', line=1347)
W('11,2273', 0o37444, '', 'STCALL', 'RTARG', kind='interp', line=1348)
W('11,2274', 0o03463, '', '', 'NORMEX', kind='operand', line=1349)

# ***** END OF INITVEL ROUTINE *****

# Page 691
# ***** MIDGIM *****

# MOD NO. 0, BY WILLMAN, SUBROUTINE RENDGUID, LOG P34-P35, P74-P75
# REVISION 03, 17 FEB 67
#
# IF THE ACTIVE VEHICLE IS DOING THE COMPUTATION, MIDGIM COMPUTES
# THE POSITIVE MIDDLE GIMBAL ANGLE OF THE ACTIVE VEHICLE TO THE INPUT
# DELTA VELOCITY VECTOR (0D IN PUSH LIST), OTHERWISE
# MIDGIM CONVERTS THE INPUT DELTA VELOCITY VECTOR FROM INERTIAL COORDIN-
# ATES TO LOCAL VERTICAL COORDINATES OF THE ACTIVE VEHICLE.
#
# ** INPUTS **
#
# NAME    MEANING                                         UNITS/SCALING/MODE
#
# AVFLAG  INT FLAG -- 0 IS CSM ACTIVE, 1 IS LEM ACTIVE                    BIT
# RINIT   ACTIVE VEHICLE RADIUS VECTOR                    METERS/CSEC (+7) VT
# VINIT   ACTIVE VEHICLE VELOCITY VECTOR                  METERS/CSEC (+7) VT
# 0D(PL)  ACTIVE VEHICLE DELTA VELOCITY VECTOR            METERS/CSEC (+7) VT
#
# ** OUTPUTS **
#
# NAME       MEANING                                         UNITS/SCALING/MODE
#
# +MGA       + MIDDLE GIMBAL ANGLE                           REVOLUTIONS (+0) DP
# DELVLVC    DELTA VELOCITY VECTOR IN LV COORD.              METERS/CSEC (+7) VT
# MGLVFLAG   INT FLAG: 0 IS +MGA COMPUTED, 1 IS DELVLVC COMP.                BIT
#
# ** CALLING SEQUENCE **
#
# L       CALL
# L+1             MIDGIM
# L+2     (RETURN -- ALWAYS)
#
# ** NO SUBROUTINES CALLED **
#
# ** DEBRIS -- ERASABLE TEMPORARY USAGE **
#
# A,Q,L, PUSH LIST, MPAC.
#
# ** ALARMS -- NONE **

# Page 692
# MIDDLE GIMBAL ANGLE COMPUTATION.

#   SETLOC MIDDGIM
#   BANK

#   COUNT* $$/MIDG

W('06,3715', 0o20000, 'HALFREV', '2DEC', '1 B-1', kind='data', line=1404)
W('06,3716', 0o00000, kind='data', line=1404)

W('06,3717', 0o53575, 'GET+MGA', 'VLOAD', 'UNIT', '(PL 0D) V (+7) TO MPAC UNITIZE UV (+1)', kind='interp', line=1406)
W('06,3720', 0o77656, '', 'UNIT', kind='interp', line=1407)
W('06,3721', 0o72441, '', 'DOT', 'SL1', 'DOT UV WITH Y(STABLE MEMBER) AND RESCALE', kind='interp', line=1408)
W('06,3722', 0o01742, '', '', 'REFSMMAT +6', 'FROM +2 TO +1 FOR ASIN ROUTINE', kind='operand', line=1409)
W('06,3723', 0o51136, '', 'ARCSIN', 'BPL', kind='interp', line=1410)
W('06,3724', 0o15730, '', '', 'SETMGA', kind='operand', line=1411)
W('06,3725', 0o43215, '', 'DAD', 'DAD', 'CONVERT -MGA TO +MGA BY', kind='interp', line=1412)
W('06,3726', 0o15716, '', '', 'HALFREV', 'ADDING ONE REVOLUTION', kind='operand', line=1413)
W('06,3727', 0o15716, '', '', 'HALFREV', kind='operand', line=1414)
W('06,3730', 0o02253, 'SETMGA', 'STORE', '+MGA', kind='interp', line=1415)
W('06,3731', 0o43414, '', 'CLR', 'RVQ', 'CLEAR MGLVFLAG TO INDICATE +MGA CALC', kind='interp', line=1416)
W('06,3732', 0o02675, '', '', 'MGLVFLAG', 'AND EXIT', kind='operand', line=1417)
W('06,3733', 0o53575, 'GET.LVC', 'VLOAD', 'UNIT', '(PL 6D) R (+29) IN MPAC UNITIZE UR', kind='interp', line=1418)
W('06,3734', 0o02323, '', '', 'RINIT', kind='operand', line=1419)
W('06,3735', 0o77676, '', 'VCOMP', '', 'U(-R)', kind='interp', line=1420)
W('06,3736', 0o00023, '', 'STORE', '18D', 'U(-R) TO 18D', kind='interp', line=1421)
W('06,3737', 0o53435, '', 'VXV', 'UNIT', 'U(-R)*V EQ V*U(R), U(V*R)', kind='interp', line=1422)
W('06,3740', 0o02331, '', '', 'VINIT', kind='operand', line=1423)
W('06,3741', 0o00015, '', 'STORE', '12D', 'U(V*R) TO 12D', kind='interp', line=1424)
W('06,3742', 0o53435, '', 'VXV', 'UNIT', 'U(V*R)*U(-R), U((V*R)*(-R))', kind='interp', line=1425)
W('06,3743', 0o00023, '', '', '18D', kind='operand', line=1426)
W('06,3744', 0o24007, '', 'STOVL', '6D', 'TRANSFORMATION MATRIX IS IN 6D (+1)', kind='interp', line=1427)
W('06,3745', 0o00001, '', '', '0D', 'DELTA V (+7) IN 0D', kind='operand', line=1428)
W('06,3746', 0o76521, '', 'MXV', 'VSL1', 'CONVERT FROM INER COOR TO LV COOR (+8)', kind='interp', line=1429)
W('06,3747', 0o00007, '', '', '6D', 'AND SCALE +7 IN MPAC', kind='operand', line=1430)
W('06,3750', 0o03434, '', 'STORE', 'DELVLVC', 'STORE IN DELVLVC (+7)', kind='interp', line=1431)
W('06,3751', 0o43414, '', 'SET', 'RVQ', 'SET MGLVFLAG TO INDICATE LVC CALC', kind='interp', line=1432)
W('06,3752', 0o02475, '', '', 'MGLVFLAG', 'AND EXIT', kind='operand', line=1433)

# ***** END OF MIDGIM ROUTINE *****

# Page 693
#   BANK 10
#   SETLOC SLCTMU
#   BANK
#   COUNT* $$/MIDG

W('10,2000', 0o77160, 'SELECTMU', 'AXC,1', 'AXT,2', kind='interp', line=1443)
W('10,2001', 0o00002, '', '', '2D', kind='operand', line=1444)
W('10,2002', 0o00000, '', '', '0D', kind='operand', line=1445)
W('10,2003', 0o77614, '', 'BOFF', kind='interp', line=1446)
W('10,2004', 0o04343, '', '', 'CMOONFLG', kind='operand', line=1447)
W('10,2005', 0o20011, '', '', 'SETMUER', kind='operand', line=1448)
W('10,2006', 0o77160, '', 'AXC,1', 'AXT,2', kind='interp', line=1449)
W('10,2007', 0o00012, '', '', '10D', kind='operand', line=1450)
W('10,2010', 0o00002, '', '', '2D', kind='operand', line=1451)
W('10,2011', 0o66143, 'SETMUER', 'DLOAD*', 'SXA,1', kind='interp', line=1452)
W('10,2012', 0o10011, '', '', 'MUTABLE +4,1', kind='operand', line=1453)
W('10,2013', 0o02776, '', '', 'RTX1', kind='operand', line=1454)
W('10,2014', 0o22317, '', 'STODL*', 'RTSR1/MU', kind='interp', line=1455)
W('10,2015', 0o10003, '', '', 'MUTABLE -2,1', kind='operand', line=1456)
W('10,2016', 0o54214, '', 'BOFF', 'SR', kind='interp', line=1457)
W('10,2017', 0o04343, '', '', 'CMOONFLG', kind='operand', line=1458)
W('10,2020', 0o20022, '', '', 'RTRNMU', kind='operand', line=1459)
W('10,2021', 0o20607, '', '', '6D', kind='operand', line=1460)
W('10,2022', 0o02321, 'RTRNMU', 'STORE', 'RTMU', kind='interp', line=1461)
W('10,2023', 0o43134, '', 'SXA,2', 'CLEAR', kind='interp', line=1462)
W('10,2024', 0o02777, '', '', 'RTX2', kind='operand', line=1463)
W('10,2025', 0o01271, '', '', 'FINALFLG', kind='operand', line=1464)
W('10,2026', 0o77650, '', 'GOTO', kind='interp', line=1465)
W('10,2027', 0o73606, '', '', 'VN1645', kind='operand', line=1466)

# Page 694
# ***** PERIAPO *****
#
# MOD NO -1                     LOG SECTION -- P34-P35, P74-P75
# MOD BY WHITE, P.              DATE 18 JAN 68
#
# FUNCTIONAL DESCRIPTION
#
# THIS SUBROUTINE COMPUTES THE TWO BODY APOCENTER AND PERICENTER
# ALTITUDES GIVEN THE POSITION AND VELOCITY VECTORS FOR A POINT ON
# TRAJECTORY AND THE PRIMARY BODY.
#
# SETRAD IS CALLED TO DETERMINE THE RADIUS OF THE PRIMARY BODY.
#
# APSIDES IS CALLED TO SOVE FOR THE TWO BODY RADII OF APOCENTER AND
# PERICENTER AND THE ECCENTRICITY OF THE TRAJECTORY.
#
# CALLING SEQUENCE
#
# L       CALL
# L+1             PERIAPO
# L+2     (RETURN -- ALWAYS)
#
# INPUT
#
# (1)     RVEC    POSITION VECTOR IN METERS
# SCALE FACTOR -- EARTH +29, MOON +27
# (2)     VVEC    VELOCITY VECTOR IN METERS/CENTISECOND
# SCALE FACTOR -- EARTH +7, MOON +5
# (3)     X1      PRIMARY BODY INDICATOR
# EARTH -1, MOON -10
#
# OUTPUT
#
# (1)     2D      APOCENTER RADIUS IN METERS
# SCALE FACTOR -- EARTH +29, MOON +27
# (2)     4D      APOCENTER ALTITUDE IN METERS
# SCALE FACTOR -- EARTH +29, MOON +27
# (3)     6D      PERICENTER RADIUS IN METERS
# SCALE FACTOR -- EARTH +29, MOON +27
# (4)     8D      PERICENTER ALTITUDE IN METERS
# SCALE FACTOR -- EARTH +29, MOON +27
# (5)     ECC     ECCENTRICITY OF CONIC TRAJECTORY
# SCALE FACTOR -- +3
# (6)     XXXALT  RADIUS OF THE PRIMARY BODY IN METERS
# SCALE FACTOR -- EARTH +29, MOON +27
# (7)     PUSHLOC EQUALS 10D
#
# SUBROUTINES USED
#
# SETRAD
# Page 695
# APSIDES

#   SETLOC APOPERI
#   BANK

#   COUNT* $$/PERAP

W('23,2314', 0o00302, 'RPAD', '2DEC', '6373338 B-29', 'STANDARD RADIUS OF PAD 37-B.', kind='data', line=1527)
W('23,2315', 0o17755, kind='data', line=1527)
# = 20 909 901.57 FT

W('23,2316', 0o53754, 'PERIAPO1', 'LXA,2', 'VSR*', kind='interp', line=1530)
W('23,2317', 0o02777, '', '', 'RTX2', kind='operand', line=1531)
W('23,2320', 0o57176, '', '', '0,2', kind='operand', line=1532)
W('23,2321', 0o26744, '', 'STOVL', 'VVEC', kind='interp', line=1533)
W('23,2322', 0o53750, '', 'LXA,1', 'VSR*', kind='interp', line=1534)
W('23,2323', 0o02776, '', '', 'RTX1', kind='operand', line=1535)
W('23,2324', 0o57176, '', '', '0,2', kind='operand', line=1536)
W('23,2325', 0o02655, '', 'STORE', 'RVEC', kind='interp', line=1537)
W('23,2326', 0o45020, 'PERIAPO', 'STQ', 'CALL', kind='interp', line=1538)
W('23,2327', 0o03463, '', '', 'NORMEX', kind='operand', line=1539)
W('23,2330', 0o46344, '', '', 'SETRAD', kind='operand', line=1540)
W('23,2331', 0o37671, '', 'STCALL', 'XXXALT', kind='interp', line=1541)
W('23,2332', 0o25674, '', '', 'APSIDES', kind='operand', line=1542)
W('23,2333', 0o41401, '', 'SETPD', 'PUSH', '2D = APOCENTER RADIUS         B29 OR B27', kind='interp', line=1543)
W('23,2334', 0o00003, '', '', '2D', kind='operand', line=1544)
W('23,2335', 0o65225, '', 'DSU', 'PDDL', '4D = APOGEE ALTITUDE          B29 OR B27', kind='interp', line=1545)
W('23,2336', 0o03671, '', '', 'XXXALT', kind='operand', line=1546)
W('23,2337', 0o00001, '', '', '0D', kind='operand', line=1547)
W('23,2340', 0o45206, '', 'PUSH', 'DSU', '6D = PERICENTER RADIUS        B29 OR B27', kind='interp', line=1548)
W('23,2341', 0o03671, '', '', 'XXXALT', kind='operand', line=1549)
W('23,2342', 0o52006, '', 'PUSH', 'GOTO', '8D = PERIGEE ALTITUDE         B29 OR B27', kind='interp', line=1550)
W('23,2343', 0o03463, '', '', 'NORMEX', kind='operand', line=1551)

# Page 696
W('23,2344', 0o41545, 'SETRAD', 'DLOAD', 'PUSH', kind='interp', line=1554)
W('23,2345', 0o06315, '', '', 'RPAD', kind='operand', line=1555)
W('23,2346', 0o63130, '', 'SXA,1', 'INCR,2', kind='interp', line=1556)
W('23,2347', 0o00047, '', '', 'X2', kind='operand', line=1557)
W('23,2350', 0o00002, '', '', '2D', kind='operand', line=1558)
W('23,2351', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=1559)
W('23,2352', 0o00050, '', '', 'X2', kind='operand', line=1560)
W('23,2353', 0o46357, '', '', 'SETRADX', kind='operand', line=1561)
W('23,2354', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=1562)
W('23,2355', 0o02023, '', '', 'RLS', kind='operand', line=1563)
W('23,2356', 0o77725, '', 'PDDL', kind='interp', line=1564)
W('23,2357', 0o43545, 'SETRADX', 'DLOAD', 'RVQ', kind='interp', line=1565)

# Page 697
W('23,2360', 0o77620, 'PRECSET', 'STQ', kind='interp', line=1568)
W('23,2361', 0o03463, '', '', 'NORMEX', kind='operand', line=1569)
W('23,2362', 0o37574, '', 'STCALL', 'TDEC2', kind='interp', line=1570)
W('23,2363', 0o27057, '', '', 'LEMPREC', kind='operand', line=1571)
W('23,2364', 0o77624, '', 'CALL', kind='interp', line=1572)
W('23,2365', 0o46376, '', '', 'LEMSTORE', kind='operand', line=1573)
W('23,2366', 0o77745, '', 'DLOAD', kind='interp', line=1574)
W('23,2367', 0o03574, '', '', 'TDEC2', kind='operand', line=1575)
W('23,2370', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1576)
W('23,2371', 0o27043, '', '', 'CSMPREC', kind='operand', line=1577)
W('23,2372', 0o77624, '', 'CALL', kind='interp', line=1578)
W('23,2373', 0o46406, '', '', 'CSMSTORE', kind='operand', line=1579)
W('23,2374', 0o77650, '', 'GOTO', kind='interp', line=1580)
W('23,2375', 0o03463, '', '', 'NORMEX', kind='operand', line=1581)
W('23,2376', 0o43175, 'LEMSTORE', 'VLOAD', 'BOFF', kind='interp', line=1582)
W('23,2377', 0o00001, '', '', 'RATT', kind='operand', line=1583)
W('23,2400', 0o01352, '', '', 'AVFLAG', kind='operand', line=1584)
W('23,2401', 0o46412, '', '', 'PASSIVE', kind='operand', line=1585)
W('23,2402', 0o27536, 'ACTIVE', 'STOVL', 'RACT3', kind='interp', line=1586)
W('23,2403', 0o00007, '', '', 'VATT', kind='operand', line=1587)
W('23,2404', 0o03544, '', 'STORE', 'VACT3', kind='interp', line=1588)
W('23,2405', 0o77616, '', 'RVQ', kind='interp', line=1589)
W('23,2406', 0o43175, 'CSMSTORE', 'VLOAD', 'BOFF', kind='interp', line=1590)
W('23,2407', 0o00001, '', '', 'RATT', kind='operand', line=1591)
W('23,2410', 0o01352, '', '', 'AVFLAG', kind='operand', line=1592)
W('23,2411', 0o46402, '', '', 'ACTIVE', kind='operand', line=1593)
W('23,2412', 0o27552, 'PASSIVE', 'STOVL', 'RPASS3', kind='interp', line=1594)
W('23,2413', 0o00007, '', '', 'VATT', kind='operand', line=1595)
W('23,2414', 0o03560, '', 'STORE', 'VPASS3', kind='interp', line=1596)
W('23,2415', 0o77616, '', 'RVQ', kind='interp', line=1597)

# Page 698
W('23,2416', 0o53754, 'VECSHIFT', 'LXA,2', 'VSR*', kind='interp', line=1600)
W('23,2417', 0o02777, '', '', 'RTX2', kind='operand', line=1601)
W('23,2420', 0o57176, '', '', '0,2', kind='operand', line=1602)
W('23,2421', 0o63350, '', 'LXA,1', 'PDVL', kind='interp', line=1603)
W('23,2422', 0o02776, '', '', 'RTX1', kind='operand', line=1604)
W('23,2423', 0o63257, '', 'VSR*', 'PDVL', kind='interp', line=1605)
W('23,2424', 0o57176, '', '', '0,2', kind='operand', line=1606)
W('23,2425', 0o77616, '', 'RVQ', kind='interp', line=1607)

# Page 699
W('23,2426', 0o53754, 'SHIFTR1', 'LXA,2', 'SL*', kind='interp', line=1610)
W('23,2427', 0o02777, '', '', 'RTX2', kind='operand', line=1611)
W('23,2430', 0o57576, '', '', '0,2', kind='operand', line=1612)
W('23,2431', 0o77616, '', 'RVQ', kind='interp', line=1613)

# Page 700
# PROGRAM DESCRIPTION
# SUBROUTINE NAME       R36     OUT-OF-PLANE RENDEZVOUS ROUTINE
# MOD NO. 0             DATE    22 DECEMBER 67
# MOD BY N.M.NEVILLE    LOG SECTION EXTENDED VERBS
# FUNCTIONAL DESCRIPTION
#
# TO DISPLAY AT ASTRONAUT REQUEST LGC CALCULATED RENDEZVOUS
# OUT-OF-PLANE PARAMETERS (Y, YDOT, PSI).  (REQUESTED BY DSKY).
#
# CALLING SEQUENCE
#
# ASTRONAUT REQUEST THROUGH DSKY V 90 E
#
# SUBROUTINES CALLED
#
# EXDSPRET
# GOMARKF
# CSMPREC
# LEMPREC
# SGNAGREE
# LOADTIME
#
# NORMAL EXIT MODES
#
# ASTRONAUT REQUEST THROUGH DSKY TO TERMINATE PROGRAM V 34 E
#
# ALARM OR ABORT EXIT MODES
#
# NONE
#
# OUTPUT
#
# DECIMAL DISPLAY OF TIME, Y, YDOT AND PSI
#
# DISPLAYED VALUES Y, YDOT, AND PSI, ARE STORED IN ERASABLE
# REGISTERS RANGE, RRATE, AND RTHETA RESPECTIVELY.
#
# ERASABLE INITIALIZATION REQUIRED
#
# CSM AND LEM STATE VECTORS
#
# DEBRIS
#
# CENTRALS A,Q,L
# OTHER:  THOSE USED BY THE ABOVE LISTED SUBROUTINES

#   BANK 20
#   SETLOC R36LM
#   BANK
# Page 701
#   EBANK= RPASS36

#   COUNT* $$/R36

W('04,2656', 0o22007, 'R36', 'ZL', line=1670)
W('04,2657', 0o34755, '', 'CAF', 'ZERO', 'SET TIME OF EVENT TO ZERO FOR FIRST', line=1671)
W('04,2660', 0o53052, '', 'DXCH', 'DSPTEMX', 'DISPLAY', line=1672)
W('04,2661', 0o33011, '', 'CAF', 'V06N16N', line=1673)
W('04,2662', 0o04616, '', 'TC', 'BANKCALL', line=1674)
W('04,2663', 0o20334, '', 'CADR', 'GOMARKF', kind='data', line=1675)
W('04,2664', 0o15472, '', 'TCF', 'ENDEXT', 'TERMINATE', line=1676)
W('04,2665', 0o12667, '', 'TCF', '+2', 'PROCEED', line=1677)
W('04,2666', 0o12661, '', 'TCF', '-5', 'RECYCLE FOR ASTRONAUT INPUT TIME', line=1678)
W('04,2667', 0o53052, '', 'DXCH', 'DSPTEMX', line=1679)
W('04,2670', 0o00006, '', 'EXTEND', line=1680)
W('04,2671', 0o13000, '', 'BZF', 'LREGCHK', 'A-REG ZERO GOTO CHECK L-REG FOR ZERO', line=1681)
W('04,2672', 0o52155, 'ASTROTIM', 'DXCH', 'MPAC', 'A-REG NON-ZERO, TIME = ASTRO INPUT TIME', line=1682)
W('04,2673', 0o06037, '', 'TC', 'INTPRET', line=1683)
W('04,2674', 0o77634, '', 'RTB', kind='interp', line=1684)
W('04,2675', 0o21716, '', '', 'DPMODE', kind='operand', line=1685)
W('04,2676', 0o34041, 'R36INT', 'STCALL', 'TDEC1', kind='interp', line=1686)
W('04,2677', 0o27043, '', '', 'OTHPREC', kind='operand', line=1687)
W('04,2700', 0o63375, '', 'VLOAD', 'PDVL', kind='interp', line=1688)
W('04,2701', 0o00007, '', '', 'VATT', kind='operand', line=1689)
W('04,2702', 0o00001, '', '', 'RATT', '_', kind='operand', line=1690)
W('04,2703', 0o02207, '', 'STORE', 'RPASS36', 'R', kind='interp', line=1691)
W('04,2704', 0o63256, '', 'UNIT', 'PDVL', ' P', kind='interp', line=1692)
W('04,2705', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1693)
W('04,2706', 0o77626, '', 'STADR', '', '_', kind='interp', line=1694)
W('04,2707', 0o61562, '', 'STODL', 'UNP36', 'U', kind='interp', line=1695)
W('04,2710', 0o00015, '', '', 'TAT', kind='operand', line=1696)
W('04,2711', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1697)
W('04,2712', 0o27057, '', '', 'THISPREC', kind='operand', line=1698)
W('04,2713', 0o63375, '', 'VLOAD', 'PDVL', '                -', kind='interp', line=1699)
W('04,2714', 0o00007, '', '', 'VATT', 'VELOCITY VECTOR V             00D', kind='operand', line=1700)
W('04,2715', 0o00001, '', '', 'RATT', '                 A', kind='operand', line=1701)
W('04,2716', 0o77725, '', 'PDDL', kind='interp', line=1702)
W('04,2717', 0o00015, '', '', 'TAT', 'SAVE TIME IN LOCATION 30D FOR REDISPLAY', kind='operand', line=1703)
W('04,2720', 0o24037, '', 'STOVL', '30D', '                _', kind='interp', line=1704)
W('04,2721', 0o41406, '', 'PUSH', 'PUSH', 'POSITION VECTOR R  IN 06D AND 12D', kind='interp', line=1705)
W('04,2722', 0o63245, '', 'BVSU', 'PDVL', '                 A   _   _', kind='interp', line=1706)
W('04,2723', 0o02207, '', '', 'RPASS36', 'LINE OF SIGHT VECTOR R - R    12D', kind='operand', line=1707)
W('04,2724', 0o72441, '', 'DOT', 'SL1', '                      P   A', kind='interp', line=1708)
W('04,2725', 0o02215, '', '', 'UNP36', '    _   _', kind='operand', line=1709)
W('04,2726', 0o26201, '', 'STOVL', 'RANGE', 'Y = U . R', kind='interp', line=1710)
W('04,2727', 0o00001, '', '', '00D', '         A', kind='operand', line=1711)
W('04,2730', 0o72441, '', 'DOT', 'SL1', kind='interp', line=1712)
W('04,2731', 0o02215, '', '', 'UNP36', '.   _   _', kind='operand', line=1713)
W('04,2732', 0o26203, '', 'STOVL', 'RRATE', 'Y = U . V', kind='interp', line=1714)
W('04,2733', 0o00007, '', '', '06D', '         A', kind='operand', line=1715)
# Page 702
# _           _
W('04,2734', 0o41456, '', 'UNIT', 'PUSH', 'U  = UNIT ( R  )              18D', kind='interp', line=1718)
W('04,2735', 0o47235, '', 'VXV', 'VXV', ' RA          A', kind='interp', line=1719)
W('04,2736', 0o00001, '', '', '00D', ' _    _     _     _', kind='operand', line=1720)
W('04,2737', 0o00023, '', '', '18D', '(U  X V ) X U   = U', kind='operand', line=1721)
W('04,2740', 0o53552, '', 'VSL2', 'UNIT', '  RA   A     RA    A', kind='interp', line=1722)
W('04,2741', 0o77656, '', 'UNIT', kind='interp', line=1723)
W('04,2742', 0o24001, '', 'STOVL', '00D', 'UNIT HORIZONTAL IN FORWARD DIR. 00D', kind='interp', line=1724)
W('04,2743', 0o00023, '', '', '18D', kind='operand', line=1725)
W('04,2744', 0o74241, '', 'DOT', 'VXSC', '_', kind='interp', line=1726)
W('04,2745', 0o00015, '', '', '12D', 'U', kind='operand', line=1727)
W('04,2746', 0o77752, '', 'VSL2', '', ' L', kind='interp', line=1728)
W('04,2747', 0o53445, '', 'BVSU', 'UNIT', kind='interp', line=1729)
W('04,2750', 0o77656, '', 'UNIT', kind='interp', line=1730)
W('04,2751', 0o50206, '', 'PUSH', 'DOT', 'LOS PROJECTED INTO HORIZONTAL  12D', kind='interp', line=1731)
W('04,2752', 0o00001, '', '', '00D', 'PLANE', kind='operand', line=1732)
W('04,2753', 0o65552, '', 'SL1', 'ARCCOS', '             _   _', kind='interp', line=1733)
W('04,2754', 0o26205, '', 'STOVL', 'RTHETA', 'PSI = ARCCOS(U . U )', kind='interp', line=1734)
W('04,2755', 0o50235, '', 'VXV', 'DOT', '              A   L', kind='interp', line=1735)
W('04,2756', 0o00001, '', '', '00D', kind='operand', line=1736)
W('04,2757', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=1737)
W('04,2760', 0o10765, '', '', 'R36TAG2', kind='operand', line=1738)
W('04,2761', 0o24020, '', '', 'LODPMAX', kind='operand', line=1739)
W('04,2762', 0o77625, '', 'DSU', kind='interp', line=1740)
W('04,2763', 0o02205, '', '', 'RTHETA', kind='operand', line=1741)
W('04,2764', 0o02205, '', 'STORE', 'RTHETA', kind='interp', line=1742)
W('04,2765', 0o47145, 'R36TAG2', 'DLOAD', 'RTB', kind='interp', line=1743)
W('04,2766', 0o00037, '', '', '30D', kind='operand', line=1744)
W('04,2767', 0o21612, '', '', 'SGNAGREE', kind='operand', line=1745)
W('04,2770', 0o01052, '', 'STORE', 'DSPTEMX', kind='interp', line=1746)
W('04,2771', 0o77776, '', 'EXIT', kind='interp', line=1747)
W('04,2772', 0o33012, '', 'CAF', 'V06N90N', 'DISPLAY Y, YDOT, AND PSI.', line=1748)
W('04,2773', 0o04616, '', 'TC', 'BANKCALL', line=1749)
W('04,2774', 0o20334, '', 'CADR', 'GOMARKF', kind='data', line=1750)
W('04,2775', 0o15472, '', 'TCF', 'ENDEXT', 'TERMINATE', line=1751)
W('04,2776', 0o15472, '', 'TCF', 'ENDEXT', 'PROCEED, END OF PROGRAM', line=1752)
W('04,2777', 0o12661, '', 'TCF', 'R36 +3', 'REDISPLAY OUTPUT', line=1753)
W('04,3000', 0o56001, 'LREGCHK', 'XCH', 'L', line=1754)
W('04,3001', 0o00006, '', 'EXTEND', line=1755)
W('04,3002', 0o13005, '', 'BZF', 'ENTTIM2', 'L-REG ZERO, SET TIME = PRESENT TIME', line=1756)
W('04,3003', 0o56001, '', 'XCH', 'L', 'L-REG NON ZERO, TIME = ASTRO INPUT TIME', line=1757)
W('04,3004', 0o12672, '', 'TCF', 'ASTROTIM', line=1758)
W('04,3005', 0o06037, 'ENTTIM2', 'TC', 'INTPRET', line=1759)
W('04,3006', 0o52034, '', 'RTB', 'GOTO', kind='interp', line=1760)
W('04,3007', 0o21573, '', '', 'LOADTIME', kind='operand', line=1761)
W('04,3010', 0o10676, '', '', 'R36INT', kind='operand', line=1762)
W('04,3011', 0o01420, 'V06N16N', 'VN', '00616', kind='data', line=1763)
W('04,3012', 0o01532, 'V06N90N', 'VN', '00690', kind='data', line=1764)
