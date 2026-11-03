"""LAMBERT_AIMPOINT_GUIDANCE.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/LAMBERT_AIMPOINT_GUIDANCE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 651-653 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('LAMBERT_AIMPOINT_GUIDANCE', 'LAMBERT_AIMPOINT_GUIDANCE.agc', 'Luminary099', pages='651-653')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     LAMBERT_AIMPOINT_GUIDANCE.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        651-653
# Mod history:  2009-05-18 RSB  Transcribed from Luminary 099
# page images.
# 2009-06-05 RSB  Corrected 4 typos.
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
# 16:27 JULY 14,1969

# Page 651

# GENERAL  LAMBERT AIMPOINT GUIDANCE **
# WRITTEN  BY RAMA M AIYAWAR

# PROGRAM P-31 DESCRIPTION **
#
# 1.       TO ACCEPT TARGETING PARAMETERS OBTAINED FROM A SOURCE EXTERNAL
# TO THE LEM AND COMPUTE THERE FROM THE REQUIRED-VELOCITY AND
# OTHER INITIAL CONDITIONS REQUIRED BY LM FOR DESIRED MANEUVER.
# THE TARGETING PARAMETERS ARE TIG (TIME OF IGNITION), TARGET
# VECTOR (RTARG), AND THE TIME FROM TIG UNTIL THE TARGET IS
# REACHED(DELLT4),DESIRED TIME OF FLIGHT FROM  RINIT TO RTARG..

# ASSUMPTIONS **
#
# 1.       THE TARGET PARAMETERS MAY HAVE BEEN LOADED PRIOR TO THE
# EXECUTION OF THIS PROGRAM.
# 2.       THIS PROGRAM IS APPLICABLE IN EITHER EARTH OR LUNAR ORBIT.
# 3.       THIS PROGRAM IS DESIGNED FOR ONE-MAN OPERATION, AND SHOULD
# BE SELECTED BY THE ASTRONAUT BY DSKY ENTRY  V37 E31.

# SUBROUTINES USED **
#
# MANUPARM, TTG/N35, R02BOTH, MIDGIM, DISPMGA, FLAGDOWN, BANKCALL,
# GOTOPOOH, ENDOFJOB, PHASCHNG, GOFLASHR, GOFLASH.
#
# MANUPARM        CALCULATES APOGEE, PERIGEE ALTITUDES AND DELTAV DESIRED
# FOR THE MANEUVER.
#
# TTG/N35         CLOCKTASK - UPDATES CLOCK.
#
# MIDGIM          CALCULATES MIDDLE GIMBAL ANGLE FOR DISPLAY.
#
# R02BOTH         IMU - STATUS CHECK ROUTINE.

# DISPLAYS USED IN P-31LM **
#
# V06N33          DISPLAY SOTRED  TIG (IN HRS. MINS. SECS)
# V06N42          DISPLAY APOGEE, PERIGEE, DELTAV.
# V16N35          DISPLAY TIME FROM TIG.
# V06N45          TIME FROM IGNITION AND MIDDLE GIMBAL ANGLE.

# ERASABLE INITIALIZATION REQUIRED **
#
# TIG             TIME OF IGNITION    DP    (B+28) CS.
#
# DELLT4          DESIRED TIME OF FLIGHT   DP  (B+28) CS
# FROM RINIT TO RTARG .
#
# RTARG           RADIUS VECTOR OF TARGET POSITION VECTOR
# RADIUS VECTOR   SCALED TO  (B+29)METERS IF EARTH ORBIT
# Page 652
# RADIUS VECTOR SCALED TO    (B+27)METERS IF MOON  ORBIT

# OUTPUT **
#
# HAPO            APOGEE ALTITUDE
# HPER            PERIGEE ALTITUDE
# VGDISP          MAG.OF DELTAV FOR DISPLAY ,SCALING      B+7 M/CS EARTH
# MAG.OF DELTAV FOR DISPLAY,SCALING       B+5 M/CS MOON
# MIDGIM          MIDDLE GIMBAL ANGLE
# XDELVFLG        RESETS XDELVFLG FOR LAMBERT VG COMPUTATIONS

# ALARMS OR ABORTS  NONE **

# RESTARTS  ARE VIA GROUP 4 **

#   SETLOC GLM
#   BANK

#   EBANK= SUBEXIT

#   COUNT* $$/P31
W('35,2450', 0o02361, 'P31', 'TC', 'P20FLGON', line=104)
W('35,2451', 0o32025, '', 'CAF', 'V06N33', 'TIG', line=105)
W('35,2452', 0o03712, '', 'TC', 'VNPOOH', line=106)
W('35,2453', 0o06037, '', 'TC', 'INTPRET', line=107)
W('35,2454', 0o71214, '', 'CLEAR', 'DLOAD', kind='interp', line=108)
W('35,2455', 0o00670, '', '', 'UPDATFLG', kind='operand', line=109)
W('35,2456', 0o03442, '', '', 'TIG', kind='operand', line=110)
W('35,2457', 0o34041, '', 'STCALL', 'TDEC1', 'INTEGRATE STATE VECTORS TO TIG', kind='interp', line=111)
W('35,2460', 0o27057, '', '', 'LEMPREC', kind='operand', line=112)
W('35,2461', 0o40375, '', 'VLOAD', 'SETPD', kind='interp', line=113)
W('35,2462', 0o00001, '', '', 'RATT', kind='operand', line=114)
W('35,2463', 0o00001, '', '', '0D', kind='operand', line=115)
W('35,2464', 0o03642, '', 'STORE', 'RTIG', kind='interp', line=116)
W('35,2465', 0o26323, '', 'STOVL', 'RINIT', kind='interp', line=117)
W('35,2466', 0o00007, '', '', 'VATT', kind='operand', line=118)
W('35,2467', 0o03650, '', 'STORE', 'VTIG', kind='interp', line=119)
W('35,2470', 0o16331, '', 'STODL', 'VINIT', kind='interp', line=120)
W('35,2471', 0o32420, '', '', 'P30ZERO', kind='operand', line=121)
W('35,2472', 0o65206, '', 'PUSH', 'PDDL', 'E4 AND NUMIT = 0', kind='interp', line=122)
W('35,2473', 0o03452, '', '', 'DELLT4', kind='operand', line=123)
W('35,2474', 0o66015, '', 'DAD', 'SXA,1', kind='interp', line=124)
W('35,2475', 0o03442, '', '', 'TIG', kind='operand', line=125)
W('35,2476', 0o02776, '', '', 'RTX1', kind='operand', line=126)
W('35,2477', 0o03631, '', 'STORE', 'TPASS4', kind='interp', line=127)
W('35,2500', 0o45134, '', 'SXA,2', 'CALL', kind='interp', line=128)
W('35,2501', 0o02777, '', '', 'RTX2', kind='operand', line=129)
W('35,2502', 0o22000, '', '', 'INITVEL', kind='operand', line=130)
W('35,2503', 0o41575, '', 'VLOAD', 'PUSH', kind='interp', line=131)
# Page 653
W('35,2504', 0o02366, '', '', 'DELVEET3', kind='operand', line=133)
W('35,2505', 0o03656, '', 'STORE', 'DELVSIN', kind='interp', line=134)
W('35,2506', 0o43046, '', 'ABVAL', 'CLEAR', kind='interp', line=135)
W('35,2507', 0o01267, '', '', 'XDELVFLG', kind='operand', line=136)
W('35,2510', 0o37664, '', 'STCALL', 'VGDISP', kind='interp', line=137)
W('35,2511', 0o15733, '', '', 'GET.LVC', kind='operand', line=138)
W('35,2512', 0o63375, '', 'VLOAD', 'PDVL', kind='interp', line=139)
W('35,2513', 0o03642, '', '', 'RTIG', kind='operand', line=140)
W('35,2514', 0o02337, '', '', 'VIPRIME', kind='operand', line=141)
W('35,2515', 0o77624, '', 'CALL', kind='interp', line=142)
W('35,2516', 0o46316, '', '', 'PERIAPO1', kind='operand', line=143)
W('35,2517', 0o77624, '', 'CALL', kind='interp', line=144)
W('35,2520', 0o46426, '', '', 'SHIFTR1', kind='operand', line=145)
W('35,2521', 0o77624, '', 'CALL', '', 'LIMIT DISPLAY TO 9999.9 N. MI.', kind='interp', line=146)
W('35,2522', 0o45636, '', '', 'MAXCHK', kind='operand', line=147)
W('35,2523', 0o16321, '', 'STODL', 'HPER', kind='interp', line=148)
W('35,2524', 0o00005, '', '', '4D', kind='operand', line=149)
W('35,2525', 0o77624, '', 'CALL', kind='interp', line=150)
W('35,2526', 0o46426, '', '', 'SHIFTR1', kind='operand', line=151)
W('35,2527', 0o77624, '', 'CALL', '', 'LIMIT DISPLAY TO 9999.9 N. MI.', kind='interp', line=152)
W('35,2530', 0o45636, '', '', 'MAXCHK', kind='operand', line=153)
W('35,2531', 0o02317, '', 'STORE', 'HAPO', kind='interp', line=154)
W('35,2532', 0o77776, '', 'EXIT', kind='interp', line=155)
W('35,2533', 0o33727, '', 'CAF', 'V06N81', 'DELVLVC', line=156)
W('35,2534', 0o03712, '', 'TC', 'VNPOOH', line=157)
W('35,2535', 0o32026, '', 'CAF', 'V06N42', 'HAPO, HPER, VGDISP', line=158)
W('35,2536', 0o03712, '', 'TC', 'VNPOOH', line=159)
W('35,2537', 0o06037, '', 'TC', 'INTPRET', line=160)
W('35,2540', 0o45014, 'REVN1645', 'SET', 'CALL', 'TRKMKCNT, TTOGO, +MGA', kind='interp', line=161)
W('35,2541', 0o01071, '', '', 'FINALFLG', kind='operand', line=162)
W('35,2542', 0o73606, '', '', 'VN1645', kind='operand', line=163)
W('35,2543', 0o77650, '', 'GOTO', kind='interp', line=164)
W('35,2544', 0o72540, '', '', 'REVN1645', kind='operand', line=165)

# *** END OF LEMP30S .103 ***
