"""P32-P35_P72-P75.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P32-P35_P72-P75.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 618-650 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P32_P35_P72_P75', 'P32-P35_P72-P75.agc', 'Luminary099', pages='618-650')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P32-P35_P72-P75.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        618-650
# Mod history:  2009-05-18 RSB  Adapted from the Luminary 131 file of the
# same name, as corrected from Luminary 099
# page images.
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

# Page 618
# COELLIPTIC SEQUENCE INITIATION (CSI) PROGRAMS (P32 AND P72)
#
# MOD NO -1       LOG SECTION -- P32-P35, P72-P75
# MOD BY WHITE.P  DATE 1JUNE67
#
# PURPOSE

# (1)     TO CALCULATE PARAMETERS ASSOCIATED WITH THE TIME FOLLOWING
# CONCENTRIC FLIGHT PLAN MANEUVERS -- THE CO-ELLIPTIC SEQUENCE
# INITIATION (CSI) MANEUVER AND THE CONSTANT DELTA ALTITUDE
# (CDH) MANEUVER.

# (2)     TO CALCULATE THESE PARAMETERS BASED UPON MANEUVER DATA
# APPROVED AND KEYED INTO THE DSKY BY THE ASTRONAUT.

# (3)     TO DISPLAY TO THE ASTRONAUT AND THE GROUND DEPENDENT VARIABLES
# ASSOCIATED WITH THE CONCENTRIC FLIGHT PLAN MANEUVERS FOR
# APPROVAL BY THE ASTRONAUT/GROUND.

# (4)     TO STORE THE CSI TARGET PARAMETERS FOR USE BY THE DESIRED
# THRUSTING PROGRAM.
#
# ASSUMPTIONS

# (1)     AT A SELECTED TPI TIME THE LINE OF SIGHT BETWEEN THE ACTIVE
# AND PASSIVE VEHICLES IS SELECTED TO BE A PRESCRIBED ANGLE (E)
# FROM THE HORIZONTAL PLANE DEFINED BY THE ACTIVE VEHICLE
# POSITION.

# (2)     THE TIME BETWEEN CSI IGNITION AND CDH IGNITION MUST BE
# COMPUTED TO BE GREATER THAN 10 MINUTES FOR SUCCESSFUL
# COMPLETION OF THE PROGRAM.

# (3)     THE TIME BETWEEN CDH IGNITION AND TPI IGNITION MUST BE
# COMPUTED TO BE GREATER THAN 10 MINUTES FOR SUCCESSFUL
# COMPLETION OF THE PROGRAM.

# (4)     CDH DELTA V IS SELECTED TO MINIMIZE THE VARIATION OF THE
# ALTITUDE DIFFERENCE BETWEEN THE ORBITS.

# (5)     CSI BURN IS DEFINED SUCH THAT THE IMPULSIVE DELTA V IS IN THE
# HORIZONTAL PLANE DEFINED BY THE ACTIVE VEHICLE POSITION AT CSI
# IGNITION.

# (6)     THE PERICENTER ALTITUDE OF THE ORBIT FOLLOWING CSI AND CDH
# MUST BE GREATER THAN 35,000 FT (LUNAR ORBIT) OR 85 NM (EARTH
# ORBIT) FOR SUCCESSFUL COMPLETION OF THIS PROGRAM.

# (7)     THE CSI AND CDH MANEUVERS ARE ORIGINALLY ASSUMED TO BE
# PARALLEL TO THE PLANE OF THE CSM ORBIT.  HOWEVER, CREW
# Page 619
# MODIFICATION OF DELTA V (LV) COMPONENTS MAY RESULT IN AN
# OUT-OF-PLANE CSI MANEUVER

# (8)     STATE VECTOR UPDATES BY P27 ARE DISALLOWED DURING AUTOMATIC
# STATE VECTOR UPDATING INITIATED BY P20 (SEE ASSUMPTION 10).

# (9)     COMPUTED VARIABLES MAY BE STORED FOR LATER VERIFICATION BY
# THE GROUND.  THESE STORAGE CAPABILITIES ARE NORMALLY LIMITED
# ONLY TO THE PARAMETERS FOR ONE THRUSTING MANEUVER AT A TIME
# EXCEPT FOR CONCENTRIC FLIGHT PLAN MANEUVER SEQUENCES.

# (10)    THE RENDEZVOUS RADAR MAY OR MAY NOT BE USED TO UPDATE THE LM
# OR CSM STATE VECTORS FOR THIS PROGRAM.  IF RADAR USE IS
# DESIRED THE RADAR WAS TURNED ON AND LOCKED BY THE CSM BY
# PREVIOUS SELECTION OF P20.  RADAR SIGHTING MARKS WILL BE MADE
# AUTOMATICALLY APPROXIMATELY ONCE A MINUTE WHEN ENABLED BY THE
# TRACK AND UPDATE FLAGS (SEE P20).  THE RENDEZVOUS TRACKING
# MARK COUNTER IS ZEROED BY THE SELECTION OF P20 AND AFTER EACH
# THRUSTING MANEUVER.

# (11)    THE ISS NEED NOT BE ON TO COMPLETE THIS PROGRAM.

# (12)    THE OPERATION OF THE PROGRAM UTILIZES THE FOLLOWING FLAGS --
#
# ACTIVE VEHICLE FLAG -- DESIGNATES THE VEHICLE WHICH IS
# DOING RENDEZVOUS THRUSTING MANEUVERS TO THE PROGRAM WHICH
# CALCULATES THE MANEUVER PARAMETERS.  SET AT THE START OF
# EACH RENDEZVOUS PRE-THRUSTING PROGRAM.
#
# FINAL FLAG -- SELECTS FINAL PROGRAM DISPLAYS AFTER CREW HAS
# COMPLETED THE FINAL MANEUVER COMPUTATION AND DISPLAY
# CYCLE.
#
# EXTERNAL DELTA V STEERING FLAG -- DESIGNATES THE TYPE OF
# STEERING REQUIRED FOR EXECUTION OF THIS MANEUVER BY THE
# THRUSTING PROGRAM SELECTED AFTER COMPLETION OF THIS
# PROGRAM.
#
# (13)    IT IS NORMALLY REQUIRED THAT THE ISS BE ON FOR 1 HOUR PRIOR TO
# A THRUSTING MANEUVER.
#
# (14)    THIS PROGRAM IS SELECTED BY THE ASTRONAUT BY DSKY ENTRY
#
# P32 IF THIS VEHICLE IS ACTIVE VEHICLE.
#
# P72 IF THIS VEHICLE IS THE PASSIVE VEHICLE.
#
# INPUT

# (1)     TCSI            TIME OF THE CSI MANEUVER

# Page 620
# (2)     NN              NUMBER OF APSIDAL CROSSINGS THRU WHICH THE ACTIVE
# VEHICLE ORBIT CAN BE ADVANCED TO OBTAIN THE CDH
# MANEUVER POINT.
# (3)     ELEV            DESIRED LOS ANGLE AT TPI
# (4)     TTPI            TIME OF THE TPI MANEUVER
#
# OUTPUT

# (1)     TRKMKCNT        NUMBER OF MARKS
# (2)     TTOGO           TIME TO GO
# (3)     +MGA            MIDDLE GIMBAL ANGLE
# (4)     DIFFALT         DELTA ALTITUDE AT CDH
# (5)     T1TOT2          DELTA TIME FROM CSI TO CDH
# (6)     T2TOT3          DELTA TIME FROM CDH TO TPI
# (7)     DELVLVC         DELTA VELOCITY AT CSI -- LOCAL VERTICAL COORDINATES
# (8)     DELVLVC         DELTA VELOCITY AT CDH -- LOCAL VERTICAL COORDINATES
#
# DOWNLINK

# (1)     TCSI            TIME OF THE CSI MANEUVER
# (2)     TCDH            TIME OF THE CDH MANEUVER
# (3)     TTPI            TIME OF THE TPI MANEUVER
# (4)     TIG             TIME OF THE CSI MANEUVER
# (5)     DELVEET1        DELTA VELOCITY AT CSI -- REFERENCE COORDINATES
# (6)     DELVEET2        DELTA VELOCITY AT CDH -- REFERENCE COORDINATES
# (7)     DIFFALT         DELTA ALTITUDE AT CDH
# (8)     NN              NUMBER OF APSIDAL CROSSINGS THRU WHICH THE ACTIVE
# VEHICLE ORBIT CAN BE ADVANCED TO OBTAIN THE CDH
# MANEUVER POINT
# (9)     ELEV            DESIRED LOS ANGLE AT TPI
#
# COMMUNICATION TO THRUSTING PROGRAM

# (1)     TIG             TIME OF THE CSI MANEUVER
# (2)     RTIG            POSITION OF ACTIVE VEHICLE AT CSI -- BEFORE ROTATION
# INTO PLANE OF PASSIVE VEHICLE
# (3)     VTIG            VELOCITY OF ACTIVE VEHICLE AT CSE -- BEFORE ROTATION
# INTO PLANE OF PASSIVE VEHICLE
# (4)     DELVSIN         DELTA VELOCITY AT CSI -- REFERENCE COORDINATES
# (5)     DELVSAB         MAGNITUDE OF DELTA VELOCITY AT CSI
# (6)     XDELVFLG        SET TO INDICATE EXTERNAL DELTA V VG COMPUTATION
#
# SUBROUTINES USED

# AVFLAGA
# AVFLAGP
# P20FLGON
# VARALARM
# BANKCALL
# GOFLASH
# GOTOPOOH
# Page 621
# VNPOOH
# GOFLASHR
# BLANKET
# ENDOFJOB
# SELECTMU
# ADVANCE
# INTINT
# PASSIVE
# CSI/A
# S32/33.1
# DISDVLVC
# VN1645

#   BANK 35
#   SETLOC CSI/CDH
#   BANK
#   EBANK= SUBEXIT
#   COUNT* $$/P3272
W('35,2027', 0o02347, 'P32', 'TC', 'AVFLAGA', line=203)
W('35,2030', 0o02032, '', 'TC', 'P32STRT', line=204)
W('35,2031', 0o02354, 'P72', 'TC', 'AVFLAGP', line=205)
W('35,2032', 0o00006, 'P32STRT', 'EXTEND', line=206)
W('35,2033', 0o32420, '', 'DCA', 'P30ZERO', line=207)
W('35,2034', 0o53621, '', 'DXCH', 'CENTANG', line=208)
W('35,2035', 0o02053, '', 'TC', 'P32/P72A', line=209)
W('35,2036', 0o77734, 'ALMXITA', 'SXA,2', kind='interp', line=210)
W('35,2037', 0o03613, '', '', 'CSIALRM', kind='operand', line=211)
W('35,2040', 0o77740, 'ALMXIT', 'LXC,1', kind='interp', line=212)
W('35,2041', 0o03613, '', '', 'CSIALRM', kind='operand', line=213)
W('35,2042', 0o77533, '', 'SLOAD*', 'EXIT', kind='interp', line=214)
W('35,2043', 0o32423, '', '', 'ALARM/TB -1,1', kind='operand', line=215)
W('35,2044', 0o30154, '', 'CA', 'MPAC', line=216)
W('35,2045', 0o05744, '', 'TC', 'VARALARM', line=217)
W('35,2046', 0o35006, '', 'CAF', 'V05N09', line=218)
W('35,2047', 0o04616, '', 'TC', 'BANKCALL', line=219)
W('35,2050', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=220)
W('35,2051', 0o06001, '', 'TC', 'GOTOPOOH', line=221)
W('35,2052', 0o02046, '', 'TC', '-4', line=222)
W('35,2053', 0o02361, 'P32/P72A', 'TC', 'P20FLGON', line=223)
W('35,2054', 0o32417, '', 'CAF', 'P30ZERO', line=224)
W('35,2055', 0o55467, '', 'TS', 'NN +1', line=225)
W('35,2056', 0o55633, '', 'TS', 'TCSI', line=226)
W('35,2057', 0o55634, '', 'TS', 'TCSI +1', line=227)
W('35,2060', 0o32410, 'VN0611', 'CAF', 'V06N11', 'TCSI', line=228)
W('35,2061', 0o03712, '', 'TC', 'VNPOOH', line=229)
W('35,2062', 0o06037, '', 'TC', 'INTPRET', line=230)
W('35,2063', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=231)
W('35,2064', 0o03634, '', '', 'TCSI', kind='operand', line=232)
W('35,2065', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=233)
W('35,2066', 0o72113, '', '', 'VN0655', kind='operand', line=234)
# Page 622
W('35,2067', 0o01643, '', '', 'TETLEM', kind='operand', line=236)
W('35,2070', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=237)
W('35,2071', 0o46360, '', '', 'PRECSET', kind='operand', line=238)
W('35,2072', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=239)
W('35,2073', 0o03536, '', '', 'RACT3', kind='operand', line=240)
W('35,2074', 0o57176, '', '', '0,2', kind='operand', line=241)
W('35,2075', 0o26655, '', 'STOVL', 'RVEC', kind='interp', line=242)
W('35,2076', 0o03544, '', '', 'VACT3', kind='operand', line=243)
W('35,2077', 0o43057, '', 'VSR*', 'SET', kind='interp', line=244)
W('35,2100', 0o57176, '', '', '0,2', kind='operand', line=245)
W('35,2101', 0o03466, '', '', 'RVSW', kind='operand', line=246)
W('35,2102', 0o16744, '', 'STODL', 'VVEC', kind='interp', line=247)
W('35,2103', 0o06530, '', '', 'DPPOSMAX', kind='operand', line=248)
W('35,2104', 0o36756, '', 'STCALL', 'RDESIRED', kind='interp', line=249)
W('35,2105', 0o25547, '', '', 'TIMERAD', kind='operand', line=250)
W('35,2106', 0o77615, '', 'DAD', kind='interp', line=251)
W('35,2107', 0o03574, '', '', 'TDEC2', kind='operand', line=252)
W('35,2110', 0o03634, '', 'STORE', 'TCSI', kind='interp', line=253)
W('35,2111', 0o77776, '', 'EXIT', kind='interp', line=254)
W('35,2112', 0o02060, '', 'TC', 'VN0611', line=255)
W('35,2113', 0o77776, 'VN0655', 'EXIT', kind='interp', line=256)
W('35,2114', 0o33724, '', 'CAF', 'V06N55', 'NN, ELEV(RGLOS)', line=257)
W('35,2115', 0o04616, '', 'TC', 'BANKCALL', line=258)
W('35,2116', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=259)
W('35,2117', 0o06001, '', 'TC', 'GOTOPOOH', line=260)
W('35,2120', 0o02122, '', 'TC', '+2', line=261)
W('35,2121', 0o02114, '', 'TC', '-5', line=262)
W('35,2122', 0o33723, '', 'CAF', 'V06N37', 'TTPI', line=263)
W('35,2123', 0o03712, '', 'TC', 'VNPOOH', line=264)
W('35,2124', 0o06037, '', 'TC', 'INTPRET', line=265)
W('35,2125', 0o77745, '', 'DLOAD', kind='interp', line=266)
W('35,2126', 0o03634, '', '', 'TCSI', kind='operand', line=267)
W('35,2127', 0o37442, '', 'STCALL', 'TIG', kind='interp', line=268)
W('35,2130', 0o20000, '', '', 'SELECTMU', kind='operand', line=269)
W('35,2131', 0o77624, 'P32/P72B', 'CALL', kind='interp', line=270)
W('35,2132', 0o71016, '', '', 'ADVANCE', kind='operand', line=271)
W('35,2133', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=272)
W('35,2134', 0o00001, '', '', '0D', kind='operand', line=273)
W('35,2135', 0o03506, '', '', 'VPASS1', kind='operand', line=274)
W('35,2136', 0o65315, '', 'PDVL', 'PDDL', kind='interp', line=275)
W('35,2137', 0o03500, '', '', 'RPASS1', kind='operand', line=276)
W('35,2140', 0o03634, '', '', 'TCSI', kind='operand', line=277)
W('35,2141', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=278)
W('35,2142', 0o03636, '', '', 'TTPI', kind='operand', line=279)
W('35,2143', 0o33732, '', '', 'TWOPI', kind='operand', line=280)
W('35,2144', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=281)
W('35,2145', 0o73466, '', '', 'INTINT', kind='operand', line=282)
W('35,2146', 0o77624, '', 'CALL', kind='interp', line=283)
W('35,2147', 0o46412, '', '', 'PASSIVE', kind='operand', line=284)
W('35,2150', 0o77624, '', 'CALL', kind='interp', line=285)
# Page 623
W('35,2151', 0o70113, '', '', 'CSI/A', kind='operand', line=287)
W('35,2152', 0o43014, 'P32/P72C', 'BON', 'SET', kind='interp', line=288)
W('35,2153', 0o01311, '', '', 'FINALFLG', kind='operand', line=289)
W('35,2154', 0o72156, '', '', 'P32/P72D', kind='operand', line=290)
W('35,2155', 0o00470, '', '', 'UPDATFLG', kind='operand', line=291)
W('35,2156', 0o77745, 'P32/P72D', 'DLOAD', kind='interp', line=292)
W('35,2157', 0o02253, '', '', 'T1TOT2', kind='operand', line=293)
W('35,2160', 0o02253, 'P32/P72E', 'STORE', 'T1TOT2', kind='interp', line=294)
W('35,2161', 0o51025, '', 'DSU', 'BPL', kind='interp', line=295)
W('35,2162', 0o32422, '', '', '60MIN', kind='operand', line=296)
W('35,2163', 0o72160, '', '', 'P32/P72E', kind='operand', line=297)
W('35,2164', 0o77745, '', 'DLOAD', kind='interp', line=298)
W('35,2165', 0o02255, '', '', 'T2TOT3', kind='operand', line=299)
W('35,2166', 0o02255, 'P32/P72F', 'STORE', 'T2TOT3', kind='interp', line=300)
W('35,2167', 0o51025, '', 'DSU', 'BPL', kind='interp', line=301)
W('35,2170', 0o32422, '', '', '60MIN', kind='operand', line=302)
W('35,2171', 0o72166, '', '', 'P32/P72F', kind='operand', line=303)
W('35,2172', 0o77776, '', 'EXIT', kind='interp', line=304)
W('35,2173', 0o32412, '', 'CAF', 'V06N75', line=305)
W('35,2174', 0o03712, '', 'TC', 'VNPOOH', line=306)
W('35,2175', 0o06037, '', 'TC', 'INTPRET', line=307)
W('35,2176', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=308)
W('35,2177', 0o02267, '', '', 'DELVEET1', kind='operand', line=309)
W('35,2200', 0o71100, '', '', 'S32/33.1', kind='operand', line=310)
W('35,2201', 0o26267, '', 'STOVL', 'DELVEET1', kind='interp', line=311)
W('35,2202', 0o02311, '', '', 'RACT2', kind='operand', line=312)
W('35,2203', 0o26303, '', 'STOVL', 'RACT1', kind='interp', line=313)
W('35,2204', 0o02275, '', '', 'DELVEET2', kind='operand', line=314)
W('35,2205', 0o45170, '', 'AXT,1', 'CALL', kind='interp', line=315)
W('35,2206', 0o01522, '', 'VN', '0682', kind='data', line=316)
W('35,2207', 0o72370, '', '', 'DISDVLVC', kind='operand', line=317)
W('35,2210', 0o77745, '', 'DLOAD', kind='interp', line=318)
W('35,2211', 0o03636, '', '', 'TTPI', kind='operand', line=319)
W('35,2212', 0o37640, '', 'STCALL', 'TTPIO', kind='interp', line=320)
W('35,2213', 0o73606, '', '', 'VN1645', kind='operand', line=321)
W('35,2214', 0o77650, '', 'GOTO', kind='interp', line=322)
W('35,2215', 0o72131, '', '', 'P32/P72B', kind='operand', line=323)

# Page 624
# CONSTANT DELTA HEIGHT (CDH) PROGRAMS (P33 AND P73)
# MOD NO -1                     LOC SECTION -- P32-P35, P72-P75
# MOD BY WHITE, P.              DATE: 1 JUNE 67
#
# PURPOSE
#
# (1)     TO CALCULATE PARAMETERS ASSOCIATED WITH THE CONSTANT DELTA
# ALTITUDE MANEUVER (CDH).
#
# (2)     TO CALCULATE THESE PARAMETERS BASED UPON MANEUVER DATA
# APPROVED AND KEYED INTO THE DSKY BY THE ASTRONAUT.
#
# (3)     TO DISPLAY TO THE ASTRONAUT AND THE GROUND DEPENDENT VARIABLES
# ASSOCIATED WITH THE CDH MANEUVER FOR APPROVAL BY THE
# ASTRONAUT/GROUND.
#
# (4)     TO STORE THE CDH TARGET PARAMETERS FOR USE BY THE DESIRED
# THRUSTING PROGRAM.
#
# ASSUMPTIONS
#
# (1)     THIS PROGRAM IS BASED UPON PREVIOUS COMPLETION OF THE
# CO-ELLIPTIC SEQUENCE INITIATION (CSI) PROGRAM (P32/P72).
# THEREFORE --
#
# (A)     AT A SELECTED TPI TIME (NOW IN STORAGE) THE LINE OF SIGHT
# BETWEEN THE ACTIVE AND PASSIVE VEHICLES WAS SELECTED TO BE
# A PRESCRIBED ANGLE (E) (NOW IN STORAGE) FROM THE
# HORIZONTAL PLANE DEFINED BY THE ACTIVE VEHICLE POSITION.
#
# (B)     THE TIME BETWEEN CSI IGNITION AND CDH IGNITION WAS
# COMPUTED TO BE GREATER THAN 10 MINUTES.
#
# (C)     THE TIME BETWEEN CDH IGNITION AND TPI IGNITION WAS
# COMPUTED TO BE GREATER THAN 10 MINUTES.
#
# (D)     THE VARIATION OF THE ALTITUDE DIFFERENCE BETWEEN THE
# ORBITS WAS MINIMIZED.
#
# (E)     CSI BURN WAS DEFINED SUCH THAT THE IMPULSIVE DELTA V WAS
# IN THE HORIZONTAL PLANE DEFINED BY ACTIVE VEHICLE
# POSITION AT CSI IGNITION.
#
# (F)     THE PERICENTER ALTITUDES OF THE ORBITS FOLLOWING CSI AND
# CDH WERE COMPUTED TO BE GREATER THAN 35,000 FT FOR LUNAR
# ORBIT OR 85 NM FOR EARTH ORBIT.
#
# (G)     THE CSI AND CDH MANEUVERS WERE ASSUMED TO BE PARALLEL TO
# THE PLANE OF THE PASSIVE VEHICLE ORBIT.  HOWEVER, CREW
# Page 625
# MODIFICATION OF DELTA V (LV) COMPONENTS MAY HAVE RESULTED
# IN AN OUT-OF-PLANE MANEUVER.
#
# (2)     STATE VECTOR UPDATES BY P27 ARE DISALLOWED DURING AUTOMATIC
# STATE VECTOR UPDATING INITIATED BY P20 (SEE ASSUMPTION 4).
#
# (3)     COMPUTED VARIABLES MAY BE STORED FOR LATER VERIFICATION BY
# THE GROUND.  THESE STORAGE CAPABILITIES ARE NORMALLY LIMITED
# ONLY TO THE PARAMETERS FOR ONE THRUSTING MANEUVER AT A TIME
# EXCEPT FOR CONCENTRIC FLIGHT PLAN MANEUVER SEQUENCES.
#
# (4)     THE RENDEZVOUS RADAR MAY OR MAY NOT BE USED TO UPDATE THE LM.
# OR CSM STATE VECTORS FOR THIS PROGRAM.  IF RADAR USE IS
# DESIRED THE RADAR WAS TURNED ON AND LOCKED ON THE CSM BY
# PREVIOUS SELECTION OF P20.  RADAR SIGHTING MARKS WILL BE MADE
# AUTOMATICALLY APPROXIMATELY ONCE A MINUTE WHEN ENABLED BY THE
# TRACK AND UPDATE FLAGS (SEE P20).  THE RENDEZVOUS TRACKING
# MARK COUNTER IS ZEROED BY THE SELECTION OF P20 AND AFTER EACH
# THRUSTING MANEUVER.
#
# (5)     THE ISS NEED NOT BE ON TO COMPLETE THIS PROGRAM.
#
# (6)     THE OPERATION OF THE PROGRAM UTILIZES THE FOLLOWING FLAGS --
#
# ACTIVE VEHICLE FLAG -- DESIGNATES THE VEHICLE WHICH IS
# DOING RENDEZVOUS THRUSTING MANEUVERS TO THE PROGRAM WHICH
# CALCULATES THE MANEUVER PARAMETERS.  SET AT THE START OF
# EACH RENDEZVOUS PRE-THRUSTING PROGRAM.
#
# FINAL FLAG -- SELECTS FINAL PROGRAM DISPLAYS AFTER CREW HAS
# COMPLETED THE FINAL MANEUVER COMPUTATION AND DISPLAY
# CYCLE.
#
# EXTERNAL DELTA V STEERING FLAG -- DESIGNATES THE TYPE OF
# STEERING REQUIRED FOR EXECUTION OF THIS MANEUVER BY THE
# THRUSTING PROGRAM SELECTED AFTER COMPLETION OF THIS
# PROGRAM.
#
# (7)     IT IS NORMALLY REQUIRED THAT THE ISS BE ON FOR 1 HOUR PRIOR TO
# A THRUSTING MANEUVER.
#
# (8)     THIS PROGRAM IS SELECTED BY THE ASTRONAUT BY DSKY ENTRY.
#
# P33 IF THIS VEHICLE IS ACTIVE VEHICLE.
#
# P73 IF THIS VEHICLE IS PASSIVE VEHICLE.
#
# INPUT
#
# (1)     TTPIO   TIME OF THE TPI MANEUVER -- SAVED FROM P32/P72
# Page 626
# (2)     ELEV    DESIRED LOS ANGLE AT TPI -- SAVED FROM P32/P72
# (3)     TCDH    TIME OF THE CDH MANEUVER
#
# OUTPUT
#
# (1)     TRKMKCNT        NUMBER OF MARKS
# (2)     TTOGO           TIME TO GO
# (3)     +MGA            MIDDLE GIMBAL ANGLE
# (4)     DIFFALT         DELTA ALTITUDE AT CDH
# (5)     T2TOT3          DELTA TIME FROM CDH TO COMPUTED TPI
# (6)     NOMTPI          DELTA TIME FROM NOMINAL TPI TO COMPUTED TPI
# (7)     DELVLVC         DELTA VELOCITY AT CDH -- LOCAL VERTICAL COORDINATES
#
# DOWNLINK
#
# (1)     TCDH            TIME OF THE CDH MANEUVER
# (2)     TTPI            TIME OF THE TPI MANEUVER
# (3)     TIG             TIME OF THE CDH MANEUVER
# (4)     DELLVEET2       DELTA VELOCITY AT CDH -- REFERENCE COORDINATES
# (5)     DIFFALT         DELTA ALTITUDE AT CDH
# (6)     ELEV            DESIRED LOS ANGLE AT TPI
#
# COMMUNICATION TO THRUSTING PROGRAMS
#
# (1)     TIG             TIME OF THE CDH MANEUVER
# (2)     RTIG            POSITION OF ACTIVE VEHICLE AT CDH -- BEFORE ROTATION
# INTO PLANE OF PASSIVE VEHICLE.
# (3)     VTIG            VELOCITY OF ACTIVE VEHICLE AT CDH -- BEFORE ROTATION
# INTO PLANE OF PASSIVE VEHICLE.
# (4)     DELVSIN         DELTA VELOCITY AT CDH -- REFERENCE COORDINATES.
# (5)     DELVSAB         MAGNITUDE OF DELTA VELOCITY AT CDH.
# (6)     XDELVFLG        SET TO INDICATE EXTERNAL DELTA V VG COMPUTATION.
#
# SUBROUTINES USED
#
# AVFLAGA
# AVFLAGP
# P20FLGON
# VNPOOH
# SELECTMU
# ADVANCE
# CDHMVR
# INTINT3P
# ACTIVE
# PASSIVE
# S33/S34.1
# ALARM
# BANKCALL
# GOFLASH
# GOTOPOOH
# S32/33.1
# Page 627
# VN1645

#   COUNT* $$/P3373
W('35,2216', 0o02347, 'P33', 'TC', 'AVFLAGA', line=482)
W('35,2217', 0o02221, '', 'TC', 'P33/P73A', line=483)
W('35,2220', 0o02354, 'P73', 'TC', 'AVFLAGP', line=484)
W('35,2221', 0o02361, 'P33/P73A', 'TC', 'P20FLGON', line=485)
W('35,2222', 0o32411, '', 'CAF', 'V06N13', 'TCDH', line=486)
W('35,2223', 0o03712, '', 'TC', 'VNPOOH', line=487)
W('35,2224', 0o06037, '', 'TC', 'INTPRET', line=488)
W('35,2225', 0o77745, '', 'DLOAD', kind='interp', line=489)
W('35,2226', 0o03640, '', '', 'TTPIO', kind='operand', line=490)
W('35,2227', 0o17636, '', 'STODL', 'TTPI', kind='interp', line=491)
W('35,2230', 0o01777, '', '', 'TCDH', kind='operand', line=492)
W('35,2231', 0o37442, '', 'STCALL', 'TIG', kind='interp', line=493)
W('35,2232', 0o20000, '', '', 'SELECTMU', kind='operand', line=494)
W('35,2233', 0o77624, 'P33/P73B', 'CALL', kind='interp', line=495)
W('35,2234', 0o71016, '', '', 'ADVANCE', kind='operand', line=496)
W('35,2235', 0o77624, '', 'CALL', kind='interp', line=497)
W('35,2236', 0o71133, '', '', 'CDHMVR', kind='operand', line=498)
W('35,2237', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=499)
W('35,2240', 0o00001, '', '', '0D', kind='operand', line=500)
W('35,2241', 0o03544, '', '', 'VACT3', kind='operand', line=501)
W('35,2242', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=502)
W('35,2243', 0o02311, '', '', 'RACT2', kind='operand', line=503)
W('35,2244', 0o71071, '', '', 'INTINT3P', kind='operand', line=504)
W('35,2245', 0o77624, '', 'CALL', kind='interp', line=505)
W('35,2246', 0o46402, '', '', 'ACTIVE', kind='operand', line=506)
W('35,2247', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=507)
W('35,2250', 0o00001, '', '', '0D', kind='operand', line=508)
W('35,2251', 0o03530, '', '', 'VPASS2', kind='operand', line=509)
W('35,2252', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=510)
W('35,2253', 0o03522, '', '', 'RPASS2', kind='operand', line=511)
W('35,2254', 0o71071, '', '', 'INTINT3P', kind='operand', line=512)
W('35,2255', 0o77624, '', 'CALL', kind='interp', line=513)
W('35,2256', 0o46412, '', '', 'PASSIVE', kind='operand', line=514)
W('35,2257', 0o43145, '', 'DLOAD', 'SET', kind='interp', line=515)
W('35,2260', 0o32420, '', '', 'P30ZERO', kind='operand', line=516)
W('35,2261', 0o03460, '', '', 'ITSWICH', kind='operand', line=517)
W('35,2262', 0o36317, '', 'STCALL', 'NOMTPI', kind='interp', line=518)
W('35,2263', 0o72764, '', '', 'S33/34.1', kind='operand', line=519)
W('35,2264', 0o77454, '', 'BZE', 'EXIT', kind='interp', line=520)
W('35,2265', 0o72302, '', '', 'P33/P73C', kind='operand', line=521)
W('35,2266', 0o05567, '', 'TC', 'ALARM', line=522)
W('35,2267', 0o00611, '', 'OCT', '611', kind='data', line=523)
W('35,2270', 0o35006, '', 'CAF', 'V05N09', line=524)
W('35,2271', 0o04616, '', 'TC', 'BANKCALL', line=525)
W('35,2272', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=526)
W('35,2273', 0o06001, '', 'TC', 'GOTOPOOH', line=527)
W('35,2274', 0o02276, '', 'TC', '+2', line=528)
# Page 628
W('35,2275', 0o02221, '', 'TC', 'P33/P73A', line=530)
W('35,2276', 0o06037, '', 'TC', 'INTPRET', line=531)
W('35,2277', 0o77745, '', 'DLOAD', kind='interp', line=532)
W('35,2300', 0o32420, '', '', 'P30ZERO', kind='operand', line=533)
W('35,2301', 0o02317, '', 'STORE', 'NOMTPI', kind='interp', line=534)
W('35,2302', 0o43014, 'P33/P73C', 'BON', 'SET', kind='interp', line=535)
W('35,2303', 0o01311, '', '', 'FINALFLG', kind='operand', line=536)
W('35,2304', 0o72306, '', '', 'P33/P73D', kind='operand', line=537)
W('35,2305', 0o00470, '', '', 'UPDATFLG', kind='operand', line=538)
W('35,2306', 0o43345, 'P33/P73D', 'DLOAD', 'DAD', kind='interp', line=539)
W('35,2307', 0o02317, '', '', 'NOMTPI', kind='operand', line=540)
W('35,2310', 0o03636, '', '', 'TTPI', kind='operand', line=541)
W('35,2311', 0o03636, '', 'STORE', 'TTPI', kind='interp', line=542)
W('35,2312', 0o77625, '', 'DSU', kind='interp', line=543)
W('35,2313', 0o01777, '', '', 'TCDH', kind='operand', line=544)
W('35,2314', 0o51025, 'P33/P73E', 'DSU', 'BPL', kind='interp', line=545)
W('35,2315', 0o32422, '', '', '60MIN', kind='operand', line=546)
W('35,2316', 0o72314, '', '', 'P33/P73E', kind='operand', line=547)
W('35,2317', 0o77615, '', 'DAD', kind='interp', line=548)
W('35,2320', 0o32422, '', '', '60MIN', kind='operand', line=549)
W('35,2321', 0o16253, '', 'STODL', 'T1TOT2', kind='interp', line=550)
W('35,2322', 0o03636, '', '', 'TTPI', kind='operand', line=551)
W('35,2323', 0o41425, '', 'DSU', 'PUSH', kind='interp', line=552)
W('35,2324', 0o03640, '', '', 'TTPIO', kind='operand', line=553)
W('35,2325', 0o45246, 'P33/P73F', 'ABS', 'DSU', kind='interp', line=554)
W('35,2326', 0o32422, '', '', '60MIN', kind='operand', line=555)
W('35,2327', 0o43244, '', 'BPL', 'DAD', kind='interp', line=556)
W('35,2330', 0o72325, '', '', 'P33/P73F', kind='operand', line=557)
W('35,2331', 0o32422, '', '', '60MIN', kind='operand', line=558)
W('35,2332', 0o45565, '', 'SIGN', 'STADR', kind='interp', line=559)
W('35,2333', 0o75522, '', 'STORE', 'T2TOT3', kind='interp', line=560)
W('35,2334', 0o77776, '', 'EXIT', kind='interp', line=561)
W('35,2335', 0o32412, '', 'CAF', 'V06N75', line=562)
W('35,2336', 0o03712, '', 'TC', 'VNPOOH', line=563)
W('35,2337', 0o06037, '', 'TC', 'INTPRET', line=564)
W('35,2340', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=565)
W('35,2341', 0o02275, '', '', 'DELVEET2', kind='operand', line=566)
W('35,2342', 0o71100, '', '', 'S32/33.1', kind='operand', line=567)
W('35,2343', 0o36275, '', 'STCALL', 'DELVEET2', kind='interp', line=568)
W('35,2344', 0o73606, '', '', 'VN1645', kind='operand', line=569)
W('35,2345', 0o77650, '', 'GOTO', kind='interp', line=570)
W('35,2346', 0o72233, '', '', 'P33/P73B', kind='operand', line=571)

# Page 629
# ***** ADFLAG/P *****
#
# SUBROUTINES USED
#
# UPFLAG
# DOWNFLAG

W('35,2347', 0o00006, 'AVFLAGA', 'EXTEND', '', 'AVFLAG = LEM', line=581)
W('35,2350', 0o23470, '', 'QXCH', 'SUBEXIT', line=582)
W('35,2351', 0o05504, '', 'TC', 'UPFLAG', line=583)
W('35,2352', 0o00050, '', 'ADRES', 'AVFLAG', kind='data', line=584)
W('35,2353', 0o01470, '', 'TC', 'SUBEXIT', line=585)
W('35,2354', 0o00006, 'AVFLAGP', 'EXTEND', '', 'AVFLAG = CSM', line=586)
W('35,2355', 0o23470, '', 'QXCH', 'SUBEXIT', line=587)
W('35,2356', 0o05516, '', 'TC', 'DOWNFLAG', line=588)
W('35,2357', 0o00050, '', 'ADRES', 'AVFLAG', kind='data', line=589)
W('35,2360', 0o01470, '', 'TC', 'SUBEXIT', line=590)
W('35,2361', 0o00006, 'P20FLGON', 'EXTEND', line=591)
W('35,2362', 0o23470, '', 'QXCH', 'SUBEXIT', line=592)
W('35,2363', 0o05504, '', 'TC', 'UPFLAG', line=593)
W('35,2364', 0o00027, '', 'ADRES', 'UPDATFLG', 'SET UPDATFLG', kind='data', line=594)
W('35,2365', 0o05504, '', 'TC', 'UPFLAG', line=595)
W('35,2366', 0o00031, '', 'ADRES', 'TRACKFLG', 'SET TRACKFLG', kind='data', line=596)
W('35,2367', 0o01470, '', 'TC', 'SUBEXIT', line=597)

# Page 630
# ***** DISDVLVC *****
#
# SUBROUTINES USED
#
# S32/33.X
# VNPOOH

W('35,2370', 0o03434, 'DISDVLVC', 'STORE', 'DELVLVC', kind='interp', line=607)
W('35,2371', 0o45020, '', 'STQ', 'CALL', kind='interp', line=608)
W('35,2372', 0o03463, '', '', 'NORMEX', kind='operand', line=609)
W('35,2373', 0o71120, '', '', 'S32/33.X', kind='operand', line=610)
W('35,2374', 0o64375, '', 'VLOAD', 'MXV', kind='interp', line=611)
W('35,2375', 0o03434, '', '', 'DELVLVC', kind='operand', line=612)
W('35,2376', 0o00001, '', '', '0D', kind='operand', line=613)
W('35,2377', 0o66172, '', 'VSL1', 'SXA,1', kind='interp', line=614)
W('35,2400', 0o03615, '', '', 'VERBNOUN', kind='operand', line=615)
W('35,2401', 0o03434, '', 'STORE', 'DELVLVC', kind='interp', line=616)
W('35,2402', 0o77776, '', 'EXIT', kind='interp', line=617)
W('35,2403', 0o31615, '', 'CA', 'VERBNOUN', line=618)
W('35,2404', 0o03712, '', 'TC', 'VNPOOH', line=619)
W('35,2405', 0o06037, '', 'TC', 'INTPRET', line=620)
W('35,2406', 0o77650, '', 'GOTO', kind='interp', line=621)
W('35,2407', 0o03463, '', '', 'NORMEX', kind='operand', line=622)

# Page 631
# ***** CONSTANTS *****

W('35,2410', 0o01413, 'V06N11', 'VN', '0611', kind='data', line=627)
W('35,2411', 0o01415, 'V06N13', 'VN', '0613', kind='data', line=628)
W('35,2412', 0o01513, 'V06N75', 'VN', '0675', kind='data', line=629)
W('35,2413', 0o77776, 'SN359+', '2DEC', '-.000086601', kind='data', line=630)
W('35,2414', 0o62460, kind='data', line=630)

W('35,2415', 0o17777, 'CS359+', '2DEC', '+.499999992', kind='data', line=632)
W('35,2416', 0o37776, kind='data', line=632)

W('35,2417', 0o00000, 'P30ZERO', '2DEC', '0', kind='data', line=634)
W('35,2420', 0o00000, kind='data', line=634)

W('35,2421', 0o00025, '60MIN', '2DEC', '360000', kind='data', line=636)
W('35,2422', 0o37100, kind='data', line=636)

W('35,2423', 0o00600, 'ALARM/TB', 'OCT', '00600', 'NO 1', kind='data', line=638)
W('35,2424', 0o00601, '', 'OCT', '00601', '   2', kind='data', line=639)
W('35,2425', 0o00602, '', 'OCT', '00602', '   3', kind='data', line=640)
W('35,2426', 0o00603, '', 'OCT', '00603', '   4', kind='data', line=641)
W('35,2427', 0o00604, '', 'OCT', '00604', '   5', kind='data', line=642)
W('35,2430', 0o00605, '', 'OCT', '00605', '   6', kind='data', line=643)
W('35,2431', 0o00606, '', 'OCT', '00606', '   7', kind='data', line=644)

# Page 632
# ***** CSI/A *****
#
# SUBROUTINES USED
#
# VECSHIFT
# TIMETHET
# PERIAPO
# SHIFTR1
# INTINT2C
# CDHMVR
# PERIAPO1
# INTINT
# ACTIVE

#   BANK 34
#   SETLOC CSI/CDH1
#   BANK
#   EBANK= SUBEXIT
#   COUNT* $$/CSI
W('34,2057', 0o00000, 'LOOPMX', '2DEC', '16', kind='data', line=666)
W('34,2060', 0o00020, kind='data', line=666)

W('34,2061', 0o00003, 'INITST', '2DEC', '.03048 B-7', 'INITIAL DELDV = 10 FPS', kind='data', line=668)
W('34,2062', 0o34661, kind='data', line=668)

W('34,2063', 0o00606, 'DVMAX1', '2DEC', '3.0480 B-7', 'MAXIMUM DV1 = 1000 FPS', kind='data', line=670)
W('34,2064', 0o04467, kind='data', line=670)

W('34,2065', 0o00601, 'DVMAX2', '2DEC', '3.014472 B-7', '               989 FPS', kind='data', line=672)
W('34,2066', 0o33216, kind='data', line=672)

W('34,2067', 0o10000, '1DPB2', '2DEC', '1.0 B-2', kind='data', line=674)
W('34,2070', 0o00000, kind='data', line=674)

W('34,2071', 0o00000, '1DPB28', '2DEC', '1', kind='data', line=676)
W('34,2072', 0o00001, kind='data', line=676)

W('34,2073', 0o00004, 'PMINE', '2DEC', '157420 B-29', '85 NM -- MUST BE 8 WORDS BEFORE PMINM', kind='data', line=678)
W('34,2074', 0o31566, kind='data', line=678)

W('34,2075', 0o00000, 'EPSILN1', '2DEC', '.0003048 B-7', '.1 FPS', kind='data', line=680)
W('34,2076', 0o01177, kind='data', line=680)

W('34,2077', 0o00002, 'NICKELDP', '2DEC', '.021336 B-7', '7 FPS (CHANGED FROM .05 FPS)', kind='data', line=682)
W('34,2100', 0o27311, kind='data', line=682)

W('34,2101', 0o77754, 'FIFPSDP', '2DEC', '-.152400 B-7', '50 FPS', kind='data', line=684)
W('34,2102', 0o57611, kind='data', line=684)

W('34,2103', 0o00000, 'PMINM', '2DEC', '10668 B-29', '35000 FT -- MUST BE 8 WORDS AFTER PMINE', kind='data', line=686)
W('34,2104', 0o12326, kind='data', line=686)

W('34,2105', 0o00116, 'DELMAX1', '2DEC', '.6096000 B-7', '200 FPS', kind='data', line=688)
W('34,2106', 0o00730, kind='data', line=688)

W('34,2107', 0o00000, 'ONETHTH', '2DEC', '.0001 B-3', kind='data', line=690)
W('34,2110', 0o06433, kind='data', line=690)

W('34,2111', 0o00003, 'TMIN', '2DEC', '60000', '10 MIN', kind='data', line=692)
W('34,2112', 0o25140, kind='data', line=692)

W('34,2113', 0o43014, 'CSI/A', 'CLEAR', 'SET', 'INITIALIZE INDICATORS', kind='interp', line=694)
W('34,2114', 0o03260, '', '', 'S32.1F1', 'DVT1 HAS EXCEEDED MAX INDICATOR', kind='operand', line=695)
W('34,2115', 0o03061, '', '', 'S32.1F2', 'FIRST PASS FOR NEWTON ITERATION INDICATOR', kind='operand', line=696)
# Page 633
W('34,2116', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=698)
W('34,2117', 0o03262, '', '', 'S32.1F3A', '00=1ST 2 PASSES 2ND CYCLE, 01=FIRST CYCLE', kind='operand', line=699)
W('34,2120', 0o03063, '', '', 'S32.1F3B', '10=2ND CYCLE, 11=50 FPS STAGE 2ND CYCLE', kind='operand', line=700)
W('34,2121', 0o77745, '', 'DLOAD', kind='interp', line=701)
W('34,2122', 0o32420, '', '', 'P30ZERO', kind='operand', line=702)
W('34,2123', 0o03606, '', 'STORE', 'LOOPCT', kind='interp', line=703)
W('34,2124', 0o03614, '', 'STORE', 'CSIALRM', kind='interp', line=704)
W('34,2125', 0o77201, 'CSI/B', 'SETPD', 'VLOAD', kind='interp', line=705)
W('34,2126', 0o00001, '', '', '0D', kind='operand', line=706)
W('34,2127', 0o02303, '', '', 'RACT1', kind='operand', line=707)
W('34,2130', 0o41446, '', 'ABVAL', 'PUSH', 'RA1                         B29 PL02D', kind='interp', line=708)
W('34,2131', 0o70501, '', 'NORM', 'SR1', kind='interp', line=709)
W('34,2132', 0o00050, '', '', 'X2', '                     B29-N2+ B1 PL04D', kind='operand', line=710)
W('34,2133', 0o51515, '', 'PDVL', 'ABVAL', kind='interp', line=711)
W('34,2134', 0o03552, '', '', 'RPASS3', kind='operand', line=712)
W('34,2135', 0o55301, '', 'NORM', 'BDDV', 'RA1/RP3                      B1 PL02D', kind='interp', line=713)
W('34,2136', 0o00047, '', '', 'X1', kind='operand', line=714)
W('34,2137', 0o53664, '', 'XSU,2', 'SR*', '                             B2', kind='interp', line=715)
W('34,2140', 0o00046, '', '', 'X1', kind='operand', line=716)
W('34,2141', 0o57175, '', '', '1,2', kind='operand', line=717)
W('34,2142', 0o41215, '', 'DAD', 'DMP', '(1+(RA1/RP3))RA1      B29+B2=B31 PL00D', kind='interp', line=718)
W('34,2143', 0o30070, '', '', '1DPB2', kind='operand', line=719)
W('34,2144', 0o65301, '', 'NORM', 'PDDL', '                                 PL02D', kind='interp', line=720)
W('34,2145', 0o00047, '', '', 'X1', kind='operand', line=721)
W('34,2146', 0o02321, '', '', 'RTMU', kind='operand', line=722)
W('34,2147', 0o56342, '', 'SR1', 'DDV', '                     B38-B31= B7 PL00D', kind='interp', line=723)
W('34,2150', 0o75457, '', 'SL*', 'SQRT', '                              B7', kind='interp', line=724)
W('34,2151', 0o20172, '', '', '0 -7,1', kind='operand', line=725)
W('34,2152', 0o53515, '', 'PDVL', 'UNIT', '                                 PL02D', kind='interp', line=726)
W('34,2153', 0o02303, '', '', 'RACT1', kind='operand', line=727)
W('34,2154', 0o47315, '', 'PDVL', 'VXV', kind='interp', line=728)
W('34,2155', 0o02261, '', '', 'UP1', kind='operand', line=729)
W('34,2156', 0o77656, '', 'UNIT', '', 'UNIT(URP1 X UVP1 X URA1) = UH1', kind='interp', line=730)
W('34,2157', 0o72441, '', 'DOT', 'SL1', 'VA1 . UH1                     B7', kind='interp', line=731)
W('34,2160', 0o03472, '', '', 'VACT1', kind='operand', line=732)
W('34,2161', 0o45421, '', 'BDSU', 'STADR', '                                 PL00D', kind='interp', line=733)
W('34,2162', 0o60203, '', 'STODL', 'DELVCSI', kind='interp', line=734)
W('34,2163', 0o30062, '', '', 'INITST', '10 FPS', kind='operand', line=735)
W('34,2164', 0o03612, '', 'STORE', 'DELDV', kind='interp', line=736)
W('34,2165', 0o43345, 'CSI/B1', 'DLOAD', 'DAD', 'IF LOOPCT = 16', kind='interp', line=737)
W('34,2166', 0o03606, '', '', 'LOOPCT', kind='operand', line=738)
W('34,2167', 0o30072, '', '', '1DPB28', kind='operand', line=739)
W('34,2170', 0o03606, '', 'STORE', 'LOOPCT', kind='interp', line=740)
W('34,2171', 0o77025, '', 'DSU', 'AXT,2', kind='interp', line=741)
W('34,2172', 0o30060, '', '', 'LOOPMX', kind='operand', line=742)
W('34,2173', 0o00006, '', '', '6', kind='operand', line=743)
W('34,2174', 0o77644, '', 'BPL', kind='interp', line=744)
W('34,2175', 0o70776, '', '', 'SCNDSOL', kind='operand', line=745)
W('34,2176', 0o77601, 'CSI/B2', 'SETPD', kind='interp', line=746)
W('34,2177', 0o00001, '', '', '0D', kind='operand', line=747)
# Page 634
W('34,2200', 0o51545, '', 'DLOAD', 'ABS', kind='interp', line=749)
W('34,2201', 0o03574, '', '', 'DELVCSI', kind='operand', line=750)
W('34,2202', 0o50025, '', 'DSU', 'BMN', kind='interp', line=751)
W('34,2203', 0o30064, '', '', 'DVMAX1', kind='operand', line=752)
W('34,2204', 0o70224, '', '', 'CSI/B23', kind='operand', line=753)
W('34,2205', 0o43174, '', 'AXT,2', 'BON', kind='interp', line=754)
W('34,2206', 0o00007, '', '', '7', kind='operand', line=755)
W('34,2207', 0o03300, '', '', 'S32.1F1', kind='operand', line=756)
W('34,2210', 0o70776, '', '', 'SCNDSOL', kind='operand', line=757)
W('34,2211', 0o43014, '', 'BOFF', 'BON', kind='interp', line=758)
W('34,2212', 0o03342, '', '', 'S32.1F3A', kind='operand', line=759)
W('34,2213', 0o70216, '', '', 'CSI/B22', 'FLAG 3 NEQ 3', kind='operand', line=760)
W('34,2214', 0o03303, '', '', 'S32.1F3B', kind='operand', line=761)
W('34,2215', 0o70776, '', '', 'SCNDSOL', kind='operand', line=762)
W('34,2216', 0o71214, 'CSI/B22', 'SET', 'DLOAD', kind='interp', line=763)
W('34,2217', 0o03060, '', '', 'S32.1F1', kind='operand', line=764)
W('34,2220', 0o30066, '', '', 'DVMAX2', kind='operand', line=765)
W('34,2221', 0o77765, '', 'SIGN', kind='interp', line=766)
W('34,2222', 0o03574, '', '', 'DELVCSI', kind='operand', line=767)
W('34,2223', 0o03574, '', 'STORE', 'DELVCSI', kind='interp', line=768)
W('34,2224', 0o41575, 'CSI/B23', 'VLOAD', 'PUSH', kind='interp', line=769)
W('34,2225', 0o02303, '', '', 'RACT1', kind='operand', line=770)
W('34,2226', 0o63256, '', 'UNIT', 'PDVL', kind='interp', line=771)
W('34,2227', 0o02261, '', '', 'UP1', kind='operand', line=772)
W('34,2230', 0o53435, '', 'VXV', 'UNIT', 'UNIT (URP1 X UVP1 X URA1) = UH1', kind='interp', line=773)
W('34,2231', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=774)
W('34,2232', 0o03574, '', '', 'DELVCSI', kind='operand', line=775)
W('34,2233', 0o02267, '', 'STORE', 'DELVEET1', kind='interp', line=776)
W('34,2234', 0o40055, '', 'VAD', 'BOV', kind='interp', line=777)
W('34,2235', 0o03472, '', '', 'VACT1', kind='operand', line=778)
W('34,2236', 0o70237, '', '', 'CSI/B23D', kind='operand', line=779)
W('34,2237', 0o37566, 'CSI/B23D', 'STCALL', 'VACT4', kind='interp', line=780)
W('34,2240', 0o46416, '', '', 'VECSHIFT', kind='operand', line=781)
W('34,2241', 0o26744, '', 'STOVL', 'VVEC', kind='interp', line=782)
W('34,2242', 0o77614, '', 'SET', kind='interp', line=783)
W('34,2243', 0o03466, '', '', 'RVSW', kind='operand', line=784)
W('34,2244', 0o26655, '', 'STOVL', 'RVEC', kind='interp', line=785)
W('34,2245', 0o32414, '', '', 'SN359+', kind='operand', line=786)
W('34,2246', 0o36730, '', 'STCALL', 'SNTH', 'ALSO CSTH', kind='interp', line=787)
W('34,2247', 0o24732, '', '', 'TIMETHET', kind='operand', line=788)
W('34,2250', 0o72142, '', 'SR1', 'LXA,1', kind='interp', line=789)
W('34,2251', 0o02776, '', '', 'RTX1', kind='operand', line=790)
W('34,2252', 0o37604, '', 'STCALL', 'HAFPA1', kind='interp', line=791)
W('34,2253', 0o46326, '', '', 'PERIAPO', kind='operand', line=792)
W('34,2254', 0o77624, '', 'CALL', kind='interp', line=793)
W('34,2255', 0o46426, '', '', 'SHIFTR1', kind='operand', line=794)
W('34,2256', 0o17602, '', 'STODL', 'POSTCSI', kind='interp', line=795)
W('34,2257', 0o03621, '', '', 'CENTANG', kind='operand', line=796)
W('34,2260', 0o52054, '', 'BZE', 'GOTO', kind='interp', line=797)
W('34,2261', 0o70263, '', '', '+2', kind='operand', line=798)
# Page 635
W('34,2262', 0o70372, '', '', 'CIRCL', kind='operand', line=800)
W('34,2263', 0o77745, '', 'DLOAD', kind='interp', line=801)
W('34,2264', 0o02752, '', '', 'ECC', kind='operand', line=802)
W('34,2265', 0o50025, '', 'DSU', 'BMN', kind='interp', line=803)
W('34,2266', 0o30110, '', '', 'ONETHTH', kind='operand', line=804)
W('34,2267', 0o70372, '', '', 'CIRCL', kind='operand', line=805)
W('34,2270', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=806)
W('34,2271', 0o00041, '', '', 'R1', kind='operand', line=807)
W('34,2272', 0o46426, '', '', 'SHIFTR1', kind='operand', line=808)
W('34,2273', 0o60201, '', 'SETPD', 'NORM', kind='interp', line=809)
W('34,2274', 0o00003, '', '', '2D', kind='operand', line=810)
W('34,2275', 0o00047, '', '', 'X1', kind='operand', line=811)
W('34,2276', 0o50315, '', 'PDVL', 'DOT', '                                      PL04D', kind='interp', line=812)
W('34,2277', 0o02303, '', '', 'RACT1', kind='operand', line=813)
W('34,2300', 0o03566, '', '', 'VACT4', kind='operand', line=814)
W('34,2301', 0o56246, '', 'ABS', 'DDV', kind='interp', line=815)
W('34,2302', 0o00003, '', '', '02D', '(/RDOTV/)/R1             B38-B29= B7', kind='operand', line=816)
W('34,2303', 0o45257, '', 'SL*', 'DSU', kind='interp', line=817)
W('34,2304', 0o20201, '', '', '0,1', kind='operand', line=818)
W('34,2305', 0o30100, '', '', 'NICKELDP', kind='operand', line=819)
W('34,2306', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=820)
W('34,2307', 0o70372, '', '', 'CIRCL', kind='operand', line=821)
W('34,2310', 0o02740, '', '', 'P', kind='operand', line=822)
W('34,2311', 0o45312, '', 'SL2', 'DSU', kind='interp', line=823)
W('34,2312', 0o30070, '', '', '1DPB2', kind='operand', line=824)
W('34,2313', 0o14017, '', 'STODL', '14D', kind='interp', line=825)
W('34,2314', 0o02317, '', '', 'RTSR1/MU', kind='operand', line=826)
W('34,2315', 0o56342, '', 'SR1', 'DDV', '(1/ROOTMU)/R1         B-16-B29 = B-45 PL02D', kind='interp', line=827)
W('34,2316', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=828)
W('34,2317', 0o02740, '', '', 'P', kind='operand', line=829)
W('34,2320', 0o00041, '', '', 'R1', kind='operand', line=830)
W('34,2321', 0o77624, '', 'CALL', kind='interp', line=831)
W('34,2322', 0o46426, '', '', 'SHIFTR1', kind='operand', line=832)
W('34,2323', 0o72412, '', 'SL4', 'SL1', kind='interp', line=833)
W('34,2324', 0o41366, '', 'SQRT', 'DMP', '((P/MU)**.5)/R1       B14+B-14 = B-31 PL02D', kind='interp', line=834)
W('34,2325', 0o52414, '', 'BOFF', 'SL3', kind='interp', line=835)
W('34,2326', 0o04343, '', '', 'CMOONFLG', kind='operand', line=836)
W('34,2327', 0o70330, '', '', 'CSI/B3', kind='operand', line=837)
W('34,2330', 0o50315, 'CSI/B3', 'PDVL', 'DOT', kind='interp', line=838)
W('34,2331', 0o02303, '', '', 'RACT1', kind='operand', line=839)
W('34,2332', 0o03566, '', '', 'VACT4', kind='operand', line=840)
W('34,2333', 0o03617, '', 'STORE', 'RDOTV', kind='interp', line=841)
W('34,2334', 0o77646, '', 'ABS', kind='interp', line=842)
W('34,2335', 0o41301, '', 'NORM', 'DMP', '((P/MU)**.5)RDOTV/R1                  PL02D', kind='interp', line=843)
W('34,2336', 0o00050, '', '', 'X2', kind='operand', line=844)
W('34,2337', 0o53660, '', 'XSU,1', 'SL*', '                     B-31+B36-B3 = B2', kind='interp', line=845)
W('34,2340', 0o00047, '', '', 'X2', kind='operand', line=846)
W('34,2341', 0o20204, '', '', '3,1', kind='operand', line=847)
W('34,2342', 0o14015, '', 'STODL', '12D', kind='interp', line=848)
W('34,2343', 0o32420, '', '', 'P30ZERO', kind='operand', line=849)
# Page 636
W('34,2344', 0o00021, '', 'STORE', '16D', kind='interp', line=851)
W('34,2345', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=852)
W('34,2346', 0o00015, '', '', '12D', kind='operand', line=853)
W('34,2347', 0o26730, '', 'STOVL', 'SNTH', 'ALSO STORES CSTH AND 0', kind='interp', line=854)
W('34,2350', 0o02303, '', '', 'RACT1', kind='operand', line=855)
W('34,2351', 0o75315, '', 'PDVL', 'SIGN', kind='interp', line=856)
W('34,2352', 0o03566, '', '', 'VACT4', kind='operand', line=857)
W('34,2353', 0o03617, '', '', 'RDOTV', kind='operand', line=858)
W('34,2354', 0o45076, '', 'VCOMP', 'CALL', kind='interp', line=859)
W('34,2355', 0o46416, '', '', 'VECSHIFT', kind='operand', line=860)
W('34,2356', 0o26744, '', 'STOVL', 'VVEC', kind='interp', line=861)
W('34,2357', 0o77614, '', 'SET', kind='interp', line=862)
W('34,2360', 0o03466, '', '', 'RVSW', kind='operand', line=863)
W('34,2361', 0o36655, '', 'STCALL', 'RVEC', kind='interp', line=864)
W('34,2362', 0o24732, '', '', 'TIMETHET', kind='operand', line=865)
W('34,2363', 0o51125, '', 'PDDL', 'BPL', kind='interp', line=866)
W('34,2364', 0o03617, '', '', 'RDOTV', kind='operand', line=867)
W('34,2365', 0o70376, '', '', 'NTP/2', kind='operand', line=868)
W('34,2366', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=869)
W('34,2367', 0o03604, '', '', 'HAFPA1', kind='operand', line=870)
W('34,2370', 0o52006, '', 'PUSH', 'GOTO', kind='interp', line=871)
W('34,2371', 0o70376, '', '', 'NTP/2', kind='operand', line=872)
W('34,2372', 0o71201, 'CIRCL', 'SETPD', 'DLOAD', kind='interp', line=873)
W('34,2373', 0o00001, '', '', '00D', kind='operand', line=874)
W('34,2374', 0o32420, '', '', 'P30ZERO', kind='operand', line=875)
W('34,2375', 0o77606, '', 'PUSH', kind='interp', line=876)
W('34,2376', 0o41345, 'NTP/2', 'DLOAD', 'DMP', kind='interp', line=877)
W('34,2377', 0o03467, '', '', 'NN', kind='operand', line=878)
W('34,2400', 0o03604, '', '', 'HAFPA1', kind='operand', line=879)
W('34,2401', 0o45261, '', 'SL', 'DSU', kind='interp', line=880)
W('34,2402', 0o20217, '', '', '14D', kind='operand', line=881)
W('34,2403', 0o77615, '', 'DAD', kind='interp', line=882)
W('34,2404', 0o03634, '', '', 'TCSI', kind='operand', line=883)
W('34,2405', 0o01777, '', 'STORE', 'TCDH', kind='interp', line=884)
W('34,2406', 0o77021, '', 'BDSU', 'AXT,2', kind='interp', line=885)
W('34,2407', 0o03636, '', '', 'TTPI', kind='operand', line=886)
W('34,2410', 0o00005, '', '', '5D', kind='operand', line=887)
W('34,2411', 0o40240, '', 'BMN', 'SETPD', kind='interp', line=888)
W('34,2412', 0o70776, '', '', 'SCNDSOL', kind='operand', line=889)
W('34,2413', 0o00001, '', '', '0D', kind='operand', line=890)
W('34,2414', 0o63375, '', 'VLOAD', 'PDVL', kind='interp', line=891)
W('34,2415', 0o03566, '', '', 'VACT4', kind='operand', line=892)
W('34,2416', 0o02303, '', '', 'RACT1', kind='operand', line=893)
W('34,2417', 0o77624, '', 'CALL', kind='interp', line=894)
W('34,2420', 0o71062, '', '', 'INTINT2C', kind='operand', line=895)
W('34,2421', 0o26311, '', 'STOVL', 'RACT2', kind='interp', line=896)
W('34,2422', 0o00007, '', '', 'VATT', kind='operand', line=897)
W('34,2423', 0o27514, '', 'STOVL', 'VACT2', kind='interp', line=898)
W('34,2424', 0o03506, '', '', 'VPASS1', kind='operand', line=899)
W('34,2425', 0o63201, '', 'SETPD', 'PDVL', kind='interp', line=900)
# Page 637
W('34,2426', 0o00001, '', '', '0D', kind='operand', line=902)
W('34,2427', 0o03500, '', '', 'RPASS1', kind='operand', line=903)
W('34,2430', 0o77624, '', 'CALL', kind='interp', line=904)
W('34,2431', 0o71062, '', '', 'INTINT2C', kind='operand', line=905)
W('34,2432', 0o27522, '', 'STOVL', 'RPASS2', kind='interp', line=906)
W('34,2433', 0o00007, '', '', 'VATT', kind='operand', line=907)
W('34,2434', 0o37530, '', 'STCALL', 'VPASS2', kind='interp', line=908)
W('34,2435', 0o71133, '', '', 'CDHMVR', kind='operand', line=909)
W('34,2436', 0o40375, '', 'VLOAD', 'SETPD', kind='interp', line=910)
W('34,2437', 0o02311, '', '', 'RACT2', kind='operand', line=911)
W('34,2440', 0o00001, '', '', '0D', kind='operand', line=912)
W('34,2441', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=913)
W('34,2442', 0o03544, '', '', 'VACT3', kind='operand', line=914)
W('34,2443', 0o46316, '', '', 'PERIAPO1', kind='operand', line=915)
W('34,2444', 0o77624, '', 'CALL', kind='interp', line=916)
W('34,2445', 0o46426, '', '', 'SHIFTR1', kind='operand', line=917)
W('34,2446', 0o27604, '', 'STOVL', 'POSTCDH', kind='interp', line=918)
W('34,2447', 0o03544, '', '', 'VACT3', kind='operand', line=919)
W('34,2450', 0o63201, '', 'SETPD', 'PDVL', kind='interp', line=920)
W('34,2451', 0o00001, '', '', '0D', kind='operand', line=921)
W('34,2452', 0o02311, '', '', 'RACT2', kind='operand', line=922)
W('34,2453', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=923)
W('34,2454', 0o01777, '', '', 'TCDH', kind='operand', line=924)
W('34,2455', 0o03636, '', '', 'TTPI', kind='operand', line=925)
W('34,2456', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=926)
W('34,2457', 0o33732, '', '', 'TWOPI', kind='operand', line=927)
W('34,2460', 0o77624, '', 'CALL', kind='interp', line=928)
W('34,2461', 0o73466, '', '', 'INTINT', kind='operand', line=929)
W('34,2462', 0o77624, '', 'CALL', kind='interp', line=930)
W('34,2463', 0o46402, '', '', 'ACTIVE', kind='operand', line=931)
W('34,2464', 0o77745, '', 'DLOAD', kind='interp', line=932)
W('34,2465', 0o02257, '', '', 'ELEV', kind='operand', line=933)
W('34,2466', 0o73401, '', 'SETPD', 'SINE', kind='interp', line=934)
W('34,2467', 0o00007, '', '', '6D', kind='operand', line=935)
W('34,2470', 0o53515, '', 'PDVL', 'UNIT', kind='interp', line=936)
W('34,2471', 0o03536, '', '', 'RACT3', kind='operand', line=937)
W('34,2472', 0o00001, '', 'STORE', '00D', 'URA3 AT 00D', kind='interp', line=938)
W('34,2473', 0o47315, '', 'PDVL', 'VXV', 'PL14D, PL08D', kind='interp', line=939)
W('34,2474', 0o02261, '', '', 'UP1', kind='operand', line=940)
W('34,2475', 0o77656, '', 'UNIT', kind='interp', line=941)
W('34,2476', 0o71525, '', 'PDDL', 'COSINE', 'UNIT(URA3 X UVA3 X URA3) = UH3        B1 PL14D', kind='interp', line=942)
W('34,2477', 0o02257, '', '', 'ELEV', kind='operand', line=943)
W('34,2500', 0o45561, '', 'VXSC', 'STADR', '(COSLOS)(UH3)                         B2 PL08D', kind='interp', line=944)
W('34,2501', 0o77754, '', 'STORE', '18D', '      PLUS', kind='interp', line=945)
W('34,2502', 0o74345, '', 'DLOAD', 'VXSC', '(SINLOS)(URA3) = U                    B2 PL00D', kind='interp', line=946)
W('34,2503', 0o76455, '', 'VAD', 'VSL1', kind='interp', line=947)
W('34,2504', 0o00023, '', '', '18D', '                                      B1', kind='operand', line=948)
W('34,2505', 0o50206, '', 'PUSH', 'DOT', '                                         PL06D', kind='interp', line=949)
W('34,2506', 0o03536, '', '', 'RACT3', '(U . RA3) = TEMP1           B1 +B29 = B30', kind='operand', line=950)
W('34,2507', 0o41552, '', 'SL1', 'PUSH', '                                     B29 PL08D', kind='interp', line=951)
# Page 638
W('34,2510', 0o72316, '', 'DSQ', 'TLOAD', 'TEMP1**2                             B58', kind='interp', line=953)
W('34,2511', 0o00155, '', '', 'MPAC', kind='operand', line=954)
W('34,2512', 0o50315, '', 'PDVL', 'DOT', '                                         PL11D', kind='interp', line=955)
W('34,2513', 0o03536, '', '', 'RACT3', kind='operand', line=956)
W('34,2514', 0o03536, '', '', 'RACT3', kind='operand', line=957)
W('34,2515', 0o57551, '', 'TLOAD', 'DCOMP', 'RA3 . RA3', kind='interp', line=958)
W('34,2516', 0o00155, '', '', 'MPAC', kind='operand', line=959)
W('34,2517', 0o50315, '', 'PDVL', 'DOT', 'RP3 . RP3                            B58 PL14D', kind='interp', line=960)
W('34,2520', 0o03552, '', '', 'RPASS3', kind='operand', line=961)
W('34,2521', 0o03552, '', '', 'RPASS3', '                                         PL11D', kind='operand', line=962)
W('34,2522', 0o76371, '', 'TAD', 'TAD', 'TEMP1**2 + RA3.RA3 + RP3.RP3 = TEMP2     PL08D', kind='interp', line=963)
W('34,2523', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=964)
W('34,2524', 0o70542, '', '', 'K10RK2', kind='operand', line=965)
W('34,2525', 0o03606, '', '', 'LOOPCT', kind='operand', line=966)
W('34,2526', 0o77025, '', 'DSU', 'AXT,2', kind='interp', line=967)
W('34,2527', 0o30072, '', '', '1DPB28', kind='operand', line=968)
W('34,2530', 0o00001, '', '', '1D', kind='operand', line=969)
W('34,2531', 0o77654, '', 'BZE', kind='interp', line=970)
W('34,2532', 0o72036, '', '', 'ALMXITA', kind='operand', line=971)
W('34,2533', 0o70545, '', 'DLOAD', 'SR1', kind='interp', line=972)
W('34,2534', 0o03612, '', '', 'DELDV', kind='operand', line=973)
W('34,2535', 0o03612, '', 'STORE', 'DELDV', kind='interp', line=974)
W('34,2536', 0o77621, '', 'BDSU', kind='interp', line=975)
W('34,2537', 0o03576, '', '', 'DVPREV', kind='operand', line=976)
W('34,2540', 0o37574, '', 'STCALL', 'DELVCSI', kind='interp', line=977)
W('34,2541', 0o70165, '', '', 'CSI/B1', kind='operand', line=978)
W('34,2542', 0o41566, 'K10RK2', 'SQRT', 'PUSH', 'TEMP3 = TEMP2**.5                    B29 PL10D', kind='interp', line=979)
W('34,2543', 0o45276, '', 'DCOMP', 'DSU', kind='interp', line=980)
W('34,2544', 0o00007, '', '', '06D', '-TEMP1-TEMP3 = K2 AT 10D', kind='operand', line=981)
W('34,2545', 0o14013, '', 'STODL', '10D', '                                         PL08D', kind='interp', line=982)
W('34,2546', 0o45425, '', 'DSU', 'STADR', '                                         PL06D', kind='interp', line=983)
W('34,2547', 0o77762, '', 'STORE', '12D', '-TEMP1+TEMP3 = K1 AT 12D', kind='interp', line=984)
W('34,2550', 0o77646, '', 'ABS', kind='interp', line=985)
W('34,2551', 0o14017, '', 'STODL', '14D', kind='interp', line=986)
W('34,2552', 0o00013, '', '', '10D', kind='operand', line=987)
W('34,2553', 0o45246, '', 'ABS', 'DSU', kind='interp', line=988)
W('34,2554', 0o00017, '', '', '14D', kind='operand', line=989)
W('34,2555', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=990)
W('34,2556', 0o70561, '', '', 'K2.', kind='operand', line=991)
W('34,2557', 0o00015, '', '', '12D', kind='operand', line=992)
W('34,2560', 0o00013, '', 'STORE', '10D', 'K = K1', kind='interp', line=993)
W('34,2561', 0o77745, 'K2.', 'DLOAD', kind='interp', line=994)
W('34,2562', 0o00013, '', '', '10D', kind='operand', line=995)
W('34,2563', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=996)
W('34,2564', 0o53455, '', 'VAD', 'UNIT', 'V = RA3 + KU UNIT                     B1', kind='interp', line=997)
W('34,2565', 0o03536, '', '', 'RACT3', kind='operand', line=998)
W('34,2566', 0o53515, '', 'PDVL', 'UNIT', kind='interp', line=999)
W('34,2567', 0o03552, '', '', 'RPASS3', '                                         PL06D', kind='operand', line=1000)
W('34,2570', 0o53515, '', 'PDVL', 'UNIT', kind='interp', line=1001)
W('34,2571', 0o03560, '', '', 'VPASS3', '                                         PL12D', kind='operand', line=1002)
# Page 639
W('34,2572', 0o63235, '', 'VXV', 'PDVL', 'UVP3 X URP3                              PL18D', kind='interp', line=1004)
W('34,2573', 0o00007, '', '', '06D', kind='operand', line=1005)
W('34,2574', 0o00007, '', '', '06D', kind='operand', line=1006)
W('34,2575', 0o50235, '', 'VXV', 'DOT', kind='interp', line=1007)
W('34,2576', 0o00001, '', '', '00D', kind='operand', line=1008)
W('34,2577', 0o77626, '', 'STADR', '', '                                         PL12D', kind='interp', line=1009)
W('34,2600', 0o53762, '', 'STOVL', '12D', '(URP3 X V).(UVP3 X URP3)=TEMP            PL06D', kind='interp', line=1010)
W('34,2601', 0o72441, '', 'DOT', 'SL1', '                                         PL00D', kind='interp', line=1011)
W('34,2602', 0o75326, '', 'ARCCOS', 'SIGN', kind='interp', line=1012)
W('34,2603', 0o00015, '', '', '12D', '                                      B0', kind='operand', line=1013)
W('34,2604', 0o41542, '', 'SR1', 'PUSH', 'GAMMA = SIGN(TEMP)ARCOS(UNITV.URP3)      PL02D', kind='interp', line=1014)
W('34,2605', 0o71214, '', 'BON', 'DLOAD', kind='interp', line=1015)
W('34,2606', 0o03301, '', '', 'S32.1F2', kind='operand', line=1016)
W('34,2607', 0o70644, '', '', 'FRSTPAS', kind='operand', line=1017)
W('34,2610', 0o00001, '', '', '00D', 'NOT THE FIRST PASS OF A CYCLE', kind='operand', line=1018)
W('34,2611', 0o65225, '', 'DSU', 'PDDL', 'GAMMA-GAMPREV                         B1 PL04D', kind='interp', line=1019)
W('34,2612', 0o03610, '', '', 'GAMPREV', kind='operand', line=1020)
W('34,2613', 0o03574, '', '', 'DELVCSI', kind='operand', line=1021)
W('34,2614', 0o60225, '', 'DSU', 'NORM', '                                      B7', kind='interp', line=1022)
W('34,2615', 0o03576, '', '', 'DVPREV', kind='operand', line=1023)
W('34,2616', 0o00047, '', '', 'X1', kind='operand', line=1024)
W('34,2617', 0o65265, '', 'BDDV', 'PDDL', '(GAM-GAMPREV)/(DV-DVPREV)          B-6+N1 PL06D', kind='interp', line=1025)
W('34,2620', 0o00003, '', '', '02D', '      = SLOPE', kind='operand', line=1026)
W('34,2621', 0o03574, '', '', 'DELVCSI', kind='operand', line=1027)
W('34,2622', 0o03576, '', 'STORE', 'DVPREV', kind='interp', line=1028)
W('34,2623', 0o43014, '', 'BOFF', 'BOFF', kind='interp', line=1029)
W('34,2624', 0o03342, '', '', 'S32.1F3A', kind='operand', line=1030)
W('34,2625', 0o70656, '', '', 'THRDCHK', kind='operand', line=1031)
W('34,2626', 0o03343, '', '', 'S32.1F3B', kind='operand', line=1032)
W('34,2627', 0o70656, '', '', 'THRDCHK', kind='operand', line=1033)
W('34,2630', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=1034)
W('34,2631', 0o00003, '', '', '02D', kind='operand', line=1035)
W('34,2632', 0o03610, '', '', 'GAMPREV', kind='operand', line=1036)
W('34,2633', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=1037)
W('34,2634', 0o70663, '', '', 'FIFTYFPS', kind='operand', line=1038)
W('34,2635', 0o30062, '', '', 'INITST', kind='operand', line=1039)
W('34,2636', 0o77765, '', 'SIGN', kind='interp', line=1040)
W('34,2637', 0o03612, '', '', 'DELDV', kind='operand', line=1041)
W('34,2640', 0o03612, '', 'STORE', 'DELDV', kind='interp', line=1042)
W('34,2641', 0o43014, '', 'SET', 'CLEAR', kind='interp', line=1043)
W('34,2642', 0o03062, '', '', 'S32.1F3A', kind='operand', line=1044)
W('34,2643', 0o03263, '', '', 'S32.1F3B', kind='operand', line=1045)
W('34,2644', 0o77745, 'FRSTPAS', 'DLOAD', kind='interp', line=1046)
W('34,2645', 0o00001, '', '', '00D', kind='operand', line=1047)
W('34,2646', 0o17610, '', 'STODL', 'GAMPREV', kind='interp', line=1048)
W('34,2647', 0o03574, '', '', 'DELVCSI', kind='operand', line=1049)
W('34,2650', 0o03576, '', 'STORE', 'DVPREV', kind='interp', line=1050)
W('34,2651', 0o43025, '', 'DSU', 'CLEAR', kind='interp', line=1051)
W('34,2652', 0o03612, '', '', 'DELDV', kind='operand', line=1052)
W('34,2653', 0o03261, '', '', 'S32.1F2', kind='operand', line=1053)
# Page 640
W('34,2654', 0o37574, '', 'STCALL', 'DELVCSI', kind='interp', line=1055)
W('34,2655', 0o70165, '', '', 'CSI/B1', kind='operand', line=1056)
W('34,2656', 0o43014, 'THRDCHK', 'BON', 'BON', kind='interp', line=1057)
W('34,2657', 0o03302, '', '', 'S32.1F3A', kind='operand', line=1058)
W('34,2660', 0o70702, '', '', 'NEWTN', kind='operand', line=1059)
W('34,2661', 0o03303, '', '', 'S32.1F3B', kind='operand', line=1060)
W('34,2662', 0o70702, '', '', 'NEWTN', kind='operand', line=1061)
W('34,2663', 0o75345, 'FIFTYFPS', 'DLOAD', 'SIGN', kind='interp', line=1062)
W('34,2664', 0o30102, '', '', 'FIFPSDP', kind='operand', line=1063)
W('34,2665', 0o00005, '', '', '04D', kind='operand', line=1064)
W('34,2666', 0o77765, '', 'SIGN', kind='interp', line=1065)
W('34,2667', 0o03610, '', '', 'GAMPREV', kind='operand', line=1066)
W('34,2670', 0o03612, '', 'STORE', 'DELDV', kind='interp', line=1067)
W('34,2671', 0o43276, '', 'DCOMP', 'DAD', kind='interp', line=1068)
W('34,2672', 0o03574, '', '', 'DELVCSI', kind='operand', line=1069)
W('34,2673', 0o17574, '', 'STODL', 'DELVCSI', kind='interp', line=1070)
W('34,2674', 0o00001, '', '', '00D', kind='operand', line=1071)
W('34,2675', 0o43014, '', 'SET', 'SET', kind='interp', line=1072)
W('34,2676', 0o03063, '', '', 'S32.1F3B', kind='operand', line=1073)
W('34,2677', 0o03062, '', '', 'S32.1F3A', kind='operand', line=1074)
W('34,2700', 0o37610, '', 'STCALL', 'GAMPREV', kind='interp', line=1075)
W('34,2701', 0o70176, '', '', 'CSI/B2', kind='operand', line=1076)
W('34,2702', 0o60345, 'NEWTN', 'DLOAD', 'NORM', kind='interp', line=1077)
W('34,2703', 0o00005, '', '', '04D', kind='operand', line=1078)
W('34,2704', 0o00050, '', '', 'X2', kind='operand', line=1079)
W('34,2705', 0o54065, '', 'BDDV', 'XSU,1', kind='interp', line=1080)
W('34,2706', 0o00001, '', '', '00D', kind='operand', line=1081)
W('34,2707', 0o00047, '', '', 'X2', kind='operand', line=1082)
W('34,2710', 0o77657, '', 'SR*', kind='interp', line=1083)
W('34,2711', 0o20601, '', '', '0,1', kind='operand', line=1084)
W('34,2712', 0o17612, '', 'STODL', 'DELDV', kind='interp', line=1085)
W('34,2713', 0o00001, '', '', '00D', kind='operand', line=1086)
W('34,2714', 0o03610, '', 'STORE', 'GAMPREV', kind='interp', line=1087)
W('34,2715', 0o51545, '', 'DLOAD', 'ABS', kind='interp', line=1088)
W('34,2716', 0o03612, '', '', 'DELDV', '                                         PL08D', kind='operand', line=1089)
W('34,2717', 0o45206, '', 'PUSH', 'DSU', kind='interp', line=1090)
W('34,2720', 0o30076, '', '', 'EPSILN1', kind='operand', line=1091)
W('34,2721', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=1092)
W('34,2722', 0o70737, '', '', 'CSI/SOL', kind='operand', line=1093)
W('34,2723', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1094)
W('34,2724', 0o30106, '', '', 'DELMAX1', kind='operand', line=1095)
W('34,2725', 0o70732, '', '', 'CSISTEP', kind='operand', line=1096)
W('34,2726', 0o75345, '', 'DLOAD', 'SIGN', kind='interp', line=1097)
W('34,2727', 0o30106, '', '', 'DELMAX1', kind='operand', line=1098)
W('34,2730', 0o03612, '', '', 'DELDV', kind='operand', line=1099)
W('34,2731', 0o03612, '', 'STORE', 'DELDV', kind='interp', line=1100)
W('34,2732', 0o45345, 'CSISTEP', 'DLOAD', 'DSU', kind='interp', line=1101)
W('34,2733', 0o03574, '', '', 'DELVCSI', kind='operand', line=1102)
W('34,2734', 0o03612, '', '', 'DELDV', kind='operand', line=1103)
W('34,2735', 0o37574, '', 'STCALL', 'DELVCSI', kind='interp', line=1104)
# Page 641
W('34,2736', 0o70165, '', '', 'CSI/B1', kind='operand', line=1106)
W('34,2737', 0o77145, 'CSI/SOL', 'DLOAD', 'AXT,2', kind='interp', line=1107)
W('34,2740', 0o03602, '', '', 'POSTCSI', kind='operand', line=1108)
W('34,2741', 0o00002, '', '', '2', kind='operand', line=1109)
W('34,2742', 0o77750, '', 'LXA,1', kind='interp', line=1110)
W('34,2743', 0o02776, '', '', 'RTX1', kind='operand', line=1111)
W('34,2744', 0o50023, '', 'DSU*', 'BMN', kind='interp', line=1112)
W('34,2745', 0o30072, '', '', 'PMINE -2,1', kind='operand', line=1113)
W('34,2746', 0o70776, '', '', 'SCNDSOL', kind='operand', line=1114)
W('34,2747', 0o71374, '', 'AXT,2', 'DLOAD', kind='interp', line=1115)
W('34,2750', 0o00003, '', '', '3', kind='operand', line=1116)
W('34,2751', 0o03604, '', '', 'POSTCDH', kind='operand', line=1117)
W('34,2752', 0o50023, '', 'DSU*', 'BMN', kind='interp', line=1118)
W('34,2753', 0o30072, '', '', 'PMINE -2,1', kind='operand', line=1119)
W('34,2754', 0o70776, '', '', 'SCNDSOL', kind='operand', line=1120)
W('34,2755', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=1121)
W('34,2756', 0o01777, '', '', 'TCDH', kind='operand', line=1122)
W('34,2757', 0o03634, '', '', 'TCSI', kind='operand', line=1123)
W('34,2760', 0o02253, '', 'STORE', 'T1TOT2', kind='interp', line=1124)
W('34,2761', 0o45374, '', 'AXT,2', 'DSU', kind='interp', line=1125)
W('34,2762', 0o00004, '', '', '4', kind='operand', line=1126)
W('34,2763', 0o30112, '', '', 'TMIN', kind='operand', line=1127)
W('34,2764', 0o77040, '', 'BMN', 'AXT,2', kind='interp', line=1128)
W('34,2765', 0o70776, '', '', 'SCNDSOL', kind='operand', line=1129)
W('34,2766', 0o00005, '', '', '5', kind='operand', line=1130)
W('34,2767', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=1131)
W('34,2770', 0o03636, '', '', 'TTPI', kind='operand', line=1132)
W('34,2771', 0o01777, '', '', 'TCDH', kind='operand', line=1133)
W('34,2772', 0o02255, '', 'STORE', 'T2TOT3', kind='interp', line=1134)
W('34,2773', 0o51025, '', 'DSU', 'BPL', kind='interp', line=1135)
W('34,2774', 0o30112, '', '', 'TMIN', kind='operand', line=1136)
W('34,2775', 0o72152, '', '', 'P32/P72C', kind='operand', line=1137)
W('34,2776', 0o43014, 'SCNDSOL', 'BON', 'BOFF', kind='interp', line=1138)
W('34,2777', 0o03302, '', '', 'S32.1F3A', kind='operand', line=1139)
W('34,3000', 0o72040, '', '', 'ALMXIT', kind='operand', line=1140)
W('34,3001', 0o03343, '', '', 'S32.1F3B', kind='operand', line=1141)
W('34,3002', 0o72040, '', '', 'ALMXIT', kind='operand', line=1142)
W('34,3003', 0o71334, '', 'SXA,2', 'DLOAD', kind='interp', line=1143)
W('34,3004', 0o03613, '', '', 'CSIALRM', kind='operand', line=1144)
W('34,3005', 0o32420, '', '', 'P30ZERO', kind='operand', line=1145)
W('34,3006', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=1146)
W('34,3007', 0o03260, '', '', 'S32.1F1', kind='operand', line=1147)
W('34,3010', 0o03061, '', '', 'S32.1F2', kind='operand', line=1148)
W('34,3011', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=1149)
W('34,3012', 0o03262, '', '', 'S32.1F3A', kind='operand', line=1150)
W('34,3013', 0o03263, '', '', 'S32.1F3B', kind='operand', line=1151)
W('34,3014', 0o37606, '', 'STCALL', 'LOOPCT', kind='interp', line=1152)
W('34,3015', 0o70125, '', '', 'CSI/B', kind='operand', line=1153)

# Page 642
# ***** ADVANCE *****
#
# SUBROUTINES USED
# PRECSET
# ROTATE

W('34,3016', 0o71220, 'ADVANCE', 'STQ', 'DLOAD', kind='interp', line=1162)
W('34,3017', 0o03470, '', '', 'SUBEXIT', kind='operand', line=1163)
W('34,3020', 0o03442, '', '', 'TIG', kind='operand', line=1164)
W('34,3021', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1165)
W('34,3022', 0o46360, '', '', 'PRECSET', kind='operand', line=1166)
W('34,3023', 0o77214, '', 'SET', 'VLOAD', kind='interp', line=1167)
W('34,3024', 0o01067, '', '', 'XDELVFLG', kind='operand', line=1168)
W('34,3025', 0o03560, '', '', 'VPASS3', kind='operand', line=1169)
W('34,3026', 0o03530, '', 'STORE', 'VPASS2', kind='interp', line=1170)
W('34,3027', 0o27506, '', 'STOVL', 'VPASS1', kind='interp', line=1171)
W('34,3030', 0o03552, '', '', 'RPASS3', kind='operand', line=1172)
W('34,3031', 0o03522, '', 'STORE', 'RPASS2', kind='interp', line=1173)
W('34,3032', 0o03500, '', 'STORE', 'RPASS1', kind='interp', line=1174)
W('34,3033', 0o47256, '', 'UNIT', 'VXV', kind='interp', line=1175)
W('34,3034', 0o03506, '', '', 'VPASS1', kind='operand', line=1176)
W('34,3035', 0o77656, '', 'UNIT', kind='interp', line=1177)
W('34,3036', 0o26261, '', 'STOVL', 'UP1', kind='interp', line=1178)
W('34,3037', 0o03536, '', '', 'RACT3', kind='operand', line=1179)
W('34,3040', 0o37642, '', 'STCALL', 'RTIG', kind='interp', line=1180)
W('34,3041', 0o71052, '', '', 'ROTATE', kind='operand', line=1181)
W('34,3042', 0o02311, '', 'STORE', 'RACT2', kind='interp', line=1182)
W('34,3043', 0o26303, '', 'STOVL', 'RACT1', kind='interp', line=1183)
W('34,3044', 0o03544, '', '', 'VACT3', kind='operand', line=1184)
W('34,3045', 0o37650, '', 'STCALL', 'VTIG', kind='interp', line=1185)
W('34,3046', 0o71052, '', '', 'ROTATE', kind='operand', line=1186)
W('34,3047', 0o03514, '', 'STORE', 'VACT2', kind='interp', line=1187)
W('34,3050', 0o37472, '', 'STCALL', 'VACT1', kind='interp', line=1188)
W('34,3051', 0o03470, '', '', 'SUBEXIT', kind='operand', line=1189)

# Page 643
# ***** ROTATE *****

W('34,3052', 0o41406, 'ROTATE', 'PUSH', 'PUSH', kind='interp', line=1194)
W('34,3053', 0o74241, '', 'DOT', 'VXSC', kind='interp', line=1195)
W('34,3054', 0o02261, '', '', 'UP1', kind='operand', line=1196)
W('34,3055', 0o02261, '', '', 'UP1', kind='operand', line=1197)
W('34,3056', 0o51352, '', 'VSL2', 'BVSU', kind='interp', line=1198)
W('34,3057', 0o63256, '', 'UNIT', 'PDVL', kind='interp', line=1199)
W('34,3060', 0o74246, '', 'ABVAL', 'VXSC', kind='interp', line=1200)
W('34,3061', 0o43572, '', 'VSL1', 'RVQ', kind='interp', line=1201)

# Page 644
# ***** INTINTNA *****

W('34,3062', 0o65325, 'INTINT2C', 'PDDL', 'PDDL', kind='interp', line=1206)
W('34,3063', 0o03634, '', '', 'TCSI', kind='operand', line=1207)
W('34,3064', 0o01777, '', '', 'TCDH', kind='operand', line=1208)
W('34,3065', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=1209)
W('34,3066', 0o33732, '', '', 'TWOPI', kind='operand', line=1210)
W('34,3067', 0o77650, '', 'GOTO', kind='interp', line=1211)
W('34,3070', 0o73466, '', '', 'INTINT', kind='operand', line=1212)
W('34,3071', 0o65325, 'INTINT3P', 'PDDL', 'PDDL', kind='interp', line=1213)
W('34,3072', 0o01777, '', '', 'TCDH', kind='operand', line=1214)
W('34,3073', 0o03636, '', '', 'TTPI', kind='operand', line=1215)
W('34,3074', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=1216)
W('34,3075', 0o32420, '', '', 'P30ZERO', kind='operand', line=1217)
W('34,3076', 0o77650, '', 'GOTO', kind='interp', line=1218)
W('34,3077', 0o73466, '', '', 'INTINT', kind='operand', line=1219)

# Page 645
# ***** S32/33.1 *****
#
# SUBROUTINES USED
# S32/33.X

W('34,3100', 0o76020, 'S32/33.1', 'STQ', 'AXT,1', kind='interp', line=1227)
W('34,3101', 0o03470, '', '', 'SUBEXIT', kind='operand', line=1228)
W('34,3102', 0o01521, '', 'VN', '0681', kind='data', line=1229)
W('34,3103', 0o77624, '', 'CALL', kind='interp', line=1230)
W('34,3104', 0o72370, '', '', 'DISDVLVC', kind='operand', line=1231)
W('34,3105', 0o77624, '', 'CALL', kind='interp', line=1232)
W('34,3106', 0o71120, '', '', 'S32/33.X', kind='operand', line=1233)
W('34,3107', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=1234)
W('34,3110', 0o03434, '', '', 'DELVLVC', kind='operand', line=1235)
W('34,3111', 0o00001, '', '', '0D', kind='operand', line=1236)
W('34,3112', 0o77772, '', 'VSL1', kind='interp', line=1237)
W('34,3113', 0o03656, '', 'STORE', 'DELVSIN', kind='interp', line=1238)
W('34,3114', 0o51406, '', 'PUSH', 'ABVAL', kind='interp', line=1239)
W('34,3115', 0o27664, '', 'STOVL', 'DELVSAB', kind='interp', line=1240)
W('34,3116', 0o77650, '', 'GOTO', kind='interp', line=1241)
W('34,3117', 0o03470, '', '', 'SUBEXIT', kind='operand', line=1242)

# Page 646
# ***** S32/33.X *****

W('34,3120', 0o77201, 'S32/33.X', 'SETPD', 'VLOAD', kind='interp', line=1247)
W('34,3121', 0o00007, '', '', '6D', kind='operand', line=1248)
W('34,3122', 0o02261, '', '', 'UP1', kind='operand', line=1249)
W('34,3123', 0o63276, '', 'VCOMP', 'PDVL', kind='interp', line=1250)
W('34,3124', 0o02303, '', '', 'RACT1', kind='operand', line=1251)
W('34,3125', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=1252)
W('34,3126', 0o47206, '', 'PUSH', 'VXV', kind='interp', line=1253)
W('34,3127', 0o02261, '', '', 'UP1', kind='operand', line=1254)
W('34,3130', 0o77772, '', 'VSL1', kind='interp', line=1255)
W('34,3131', 0o00001, '', 'STORE', '0D', kind='interp', line=1256)
W('34,3132', 0o77616, '', 'RVQ', kind='interp', line=1257)

# Page 647
# ***** CDHMVR *****
#
# SUBROUTINES USED
# VECSHIFT
# TIMETHET
# SHIFTR1

W('34,3133', 0o77220, 'CDHMVR', 'STQ', 'VLOAD', kind='interp', line=1267)
W('34,3134', 0o03470, '', '', 'SUBEXIT', kind='operand', line=1268)
W('34,3135', 0o02311, '', '', 'RACT2', kind='operand', line=1269)
W('34,3136', 0o53406, '', 'PUSH', 'UNIT', kind='interp', line=1270)
W('34,3137', 0o27544, '', 'STOVL', 'UNVEC', 'UR SUB A', kind='interp', line=1271)
W('34,3140', 0o03522, '', '', 'RPASS2', kind='operand', line=1272)
W('34,3141', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=1273)
W('34,3142', 0o03544, '', '', 'UNVEC', kind='operand', line=1274)
W('34,3143', 0o72406, '', 'PUSH', 'SL1', kind='interp', line=1275)
W('34,3144', 0o16732, '', 'STODL', 'CSTH', kind='interp', line=1276)
W('34,3145', 0o65316, '', 'DSQ', 'PDDL', kind='interp', line=1277)
W('34,3146', 0o06512, '', '', 'DP1/4TH', kind='operand', line=1278)
W('34,3147', 0o45302, '', 'SR2', 'DSU', kind='interp', line=1279)
W('34,3150', 0o72566, '', 'SQRT', 'SL1', kind='interp', line=1280)
W('34,3151', 0o57515, '', 'PDVL', 'VCOMP', kind='interp', line=1281)
W('34,3152', 0o77635, '', 'VXV', kind='interp', line=1282)
W('34,3153', 0o03522, '', '', 'RPASS2', kind='operand', line=1283)
W('34,3154', 0o65241, '', 'DOT', 'PDDL', kind='interp', line=1284)
W('34,3155', 0o02261, '', '', 'UP1', kind='operand', line=1285)
W('34,3156', 0o45565, '', 'SIGN', 'STADR', kind='interp', line=1286)
W('34,3157', 0o51047, '', 'STOVL', 'SNTH', kind='interp', line=1287)
W('34,3160', 0o03522, '', '', 'RPASS2', kind='operand', line=1288)
W('34,3161', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=1289)
W('34,3162', 0o03530, '', '', 'VPASS2', kind='operand', line=1290)
W('34,3163', 0o46416, '', '', 'VECSHIFT', kind='operand', line=1291)
W('34,3164', 0o26744, '', 'STOVL', 'VVEC', kind='interp', line=1292)
W('34,3165', 0o77614, '', 'CLEAR', kind='interp', line=1293)
W('34,3166', 0o03666, '', '', 'RVSW', kind='operand', line=1294)
W('34,3167', 0o36655, '', 'STCALL', 'RVEC', kind='interp', line=1295)
W('34,3170', 0o24732, '', '', 'TIMETHET', kind='operand', line=1296)
W('34,3171', 0o53754, '', 'LXA,2', 'VSL*', kind='interp', line=1297)
W('34,3172', 0o02777, '', '', 'RTX2', kind='operand', line=1298)
W('34,3173', 0o57576, '', '', '0,2', kind='operand', line=1299)
W('34,3174', 0o00023, '', 'STORE', '18D', kind='interp', line=1300)
W('34,3175', 0o76441, '', 'DOT', 'SL1R', kind='interp', line=1301)
W('34,3176', 0o03544, '', '', 'UNVEC', kind='operand', line=1302)
W('34,3177', 0o51515, '', 'PDVL', 'ABVAL', '0D = V SUB PV', kind='interp', line=1303)
W('34,3200', 0o63257, '', 'SL*', 'PDVL', kind='interp', line=1304)
W('34,3201', 0o57576, '', '', '0,2', kind='operand', line=1305)
W('34,3202', 0o02311, '', '', 'RACT2', kind='operand', line=1306)
W('34,3203', 0o65246, '', 'ABVAL', 'PDDL', '2D = LENGTH OF R SUB A', kind='interp', line=1307)
W('34,3204', 0o77625, '', 'DSU', kind='interp', line=1308)
# Page 648
W('34,3205', 0o00003, '', '', '02D', kind='operand', line=1310)
W('34,3206', 0o17600, '', 'STODL', 'DIFFALT', 'DELTA H IN METERS             B+29', kind='interp', line=1311)
W('34,3207', 0o02742, '', '', 'R1A', kind='operand', line=1312)
W('34,3210', 0o65301, '', 'NORM', 'PDDL', '2 - R V**/MU                          04D', kind='interp', line=1313)
W('34,3211', 0o00047, '', '', 'X1', kind='operand', line=1314)
W('34,3212', 0o00041, '', '', 'R1', kind='operand', line=1315)
W('34,3213', 0o77624, '', 'CALL', kind='interp', line=1316)
W('34,3214', 0o46426, '', '', 'SHIFTR1', kind='operand', line=1317)
W('34,3215', 0o56362, '', 'SR1R', 'DDV', kind='interp', line=1318)
W('34,3216', 0o41457, '', 'SL*', 'PUSH', kind='interp', line=1319)
W('34,3217', 0o20174, '', '', '0 -5,1', kind='operand', line=1320)
W('34,3220', 0o65225, '', 'DSU', 'PDDL', 'A SUB A                       B+29    04D', kind='interp', line=1321)
W('34,3221', 0o03600, '', '', 'DIFFALT', kind='operand', line=1322)
W('34,3222', 0o56302, '', 'SR2', 'DDV', 'A SUB P                       B+31', kind='interp', line=1323)
W('34,3223', 0o00005, '', '', '04D', '                              B+2', kind='operand', line=1324)
W('34,3224', 0o75406, '', 'PUSH', 'SQRT', 'A SUB P/A SUB A                       06D', kind='interp', line=1325)
W('34,3225', 0o41275, '', 'DMPR', 'DMP', kind='interp', line=1326)
W('34,3226', 0o00007, '', '', '06D', kind='operand', line=1327)
W('34,3227', 0o00001, '', '', '00D', kind='operand', line=1328)
W('34,3230', 0o65272, '', 'SL3R', 'PDDL', 'V SUB AV METERS/CS            B+7     08D', kind='interp', line=1329)
W('34,3231', 0o00003, '', '', '02D', 'R SUB A MAGNITUDE             B+29', kind='operand', line=1330)
W('34,3232', 0o65301, '', 'NORM', 'PDDL', kind='interp', line=1331)
W('34,3233', 0o00047, '', '', 'X1', kind='operand', line=1332)
W('34,3234', 0o02321, '', '', 'RTMU', kind='operand', line=1333)
W('34,3235', 0o56342, '', 'SR1', 'DDV', '2MU                           B+38', kind='interp', line=1334)
W('34,3236', 0o65257, '', 'SL*', 'PDDL', '2 MU/R SUBAA                  B+14    10D', kind='interp', line=1335)
W('34,3237', 0o20174, '', '', '0 -5,1', kind='operand', line=1336)
W('34,3240', 0o00005, '', '', '04D', 'ASUBA                         B+29', kind='operand', line=1337)
W('34,3241', 0o65301, '', 'NORM', 'PDDL', kind='interp', line=1338)
W('34,3242', 0o00050, '', '', 'X2', kind='operand', line=1339)
W('34,3243', 0o02321, '', '', 'RTMU', kind='operand', line=1340)
W('34,3244', 0o56342, '', 'SR1', 'DDV', kind='interp', line=1341)
W('34,3245', 0o44257, '', 'SL*', 'BDSU', kind='interp', line=1342)
W('34,3246', 0o57604, '', '', '0 -6,2', '2U/R - U/A            B+14 (METERS/CS)SQ', kind='operand', line=1343)
W('34,3247', 0o63525, '', 'PDDL', 'DSQ', '                                      10D', kind='interp', line=1344)
W('34,3250', 0o00011, '', '', '08D', kind='operand', line=1345)
W('34,3251', 0o75421, '', 'BDSU', 'SQRT', kind='interp', line=1346)
W('34,3252', 0o47315, '', 'PDVL', 'VXV', 'SQRT(MU(2/R SUB A-1/A SUB A)-VSUBA2)  10D', kind='interp', line=1347)
W('34,3253', 0o02261, '', '', 'UP1', kind='operand', line=1348)
W('34,3254', 0o03544, '', '', 'UNVEC', kind='operand', line=1349)
W('34,3255', 0o74256, '', 'UNIT', 'VXSC', kind='interp', line=1350)
W('34,3256', 0o00013, '', '', '10D', kind='operand', line=1351)
W('34,3257', 0o74315, '', 'PDVL', 'VXSC', kind='interp', line=1352)
W('34,3260', 0o03544, '', '', 'UNVEC', kind='operand', line=1353)
W('34,3261', 0o00011, '', '', '08D', kind='operand', line=1354)
W('34,3262', 0o76455, '', 'VAD', 'VSL1', kind='interp', line=1355)
W('34,3263', 0o77626, '', 'STADR', kind='interp', line=1356)
W('34,3264', 0o74233, '', 'STORE', 'VACT3', kind='interp', line=1357)
W('34,3265', 0o77651, '', 'VSU', kind='interp', line=1358)
W('34,3266', 0o03514, '', '', 'VACT2', kind='operand', line=1359)
# Page 649
W('34,3267', 0o36275, '', 'STCALL', 'DELVEET2', 'DELTA VCDH -- REFERENCE COORDINATES', kind='interp', line=1361)
W('34,3270', 0o03470, '', '', 'SUBEXIT', kind='operand', line=1362)

# Page 650
# ***** COMPTGO *****
#
# SUBROUTINES USED
# CLOKTASK
# 2PHSCHNG

#   BANK 35
#   SETLOC CSI/CDH
#   BANK

#   EBANK= RTRN

#   COUNT* $$/P3575

W('35,2432', 0o00006, 'COMPTGO', 'EXTEND', line=1379)
W('35,2433', 0o23465, '', 'QXCH', 'RTRN', line=1380)
W('35,2434', 0o34755, '', 'CAF', 'ZERO', line=1381)
W('35,2435', 0o55163, '', 'TS', 'DISPDEX', line=1382)
W('35,2436', 0o34752, '', 'CAF', 'BIT2', line=1383)
W('35,2437', 0o00004, '', 'INHINT', line=1384)
W('35,2440', 0o05203, '', 'TC', 'WAITLIST', line=1385)
#   EBANK= WHICH
W('35,2441', 0o02717, '', '2CADR', 'CLOKTASK', kind='data', line=1387)
W('35,2442', 0o74067, kind='data', line=1387)

W('35,2443', 0o05327, '', 'TC', '2PHSCHNG', line=1389)
W('35,2444', 0o40036, '', 'OCT', '40036', kind='data', line=1390)
W('35,2445', 0o05024, '', 'OCT', '05024', kind='data', line=1391)
W('35,2446', 0o13000, '', 'OCT', '13000', kind='data', line=1392)
W('35,2447', 0o01465, '', 'TC', 'RTRN', line=1393)
