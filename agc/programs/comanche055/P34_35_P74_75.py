"""P34-35_P74-75.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P34-35_P74-75.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 460-504 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P34_35_P74_75', 'P34-35_P74-75.agc', 'Comanche055', pages='460-504')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P34-35_P74-75.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 460-504
# Contact:      Onno Hommes <ohommes@cmu.edu>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-10 OH   Batch 2 Assignment Comanche Transcription
# 2009-05-23 RSB  In DISPLAYE, corrected a CADR GOFLASHR
# to CADR GOFLASH.
#
# The contents of the "Comanche055" files, in general, are transcribed
# from scanned documents.
#
# Assemble revision 055 of AGC program Comanche by NASA
# 2021113-051.  April 1, 1969.
#
# This AGC program shall also be referred to as Colossus 2A
#
# Prepared by
# Massachusetts Institute of Technology
# 75 Cambridge Parkway
# Cambridge, Massachusetts
#
# under NASA contract NAS 9-4065.
#
# Refer directly to the online document mentioned above for further
# information.  Please report any errors to info@sandroid.org.

# Page 460
# TRANSFER PHASE INITIATION (TPI) PROGRAMS (P34 AND P74)
# MOD NO -1                     LOG SECTION -- P32-P35, P72-P75
# MOD BY WHITE, P.              DATE: 1 JUNE 67
#
# PURPOSE
# (1)     TO CALCULATE THE REQUIRED DELTA V AND OTHER INITIAL CONDITIONS
# REQUIRED BY THE ACTIVE VEHICLE FOR EXECUTION OF THE TRANSFER
# PHASE INITIATION (TPI) MANEUVER, GIVEN --
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
# Page 461
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
# VEHICLE CENTRAL ANGLE OF TRANSFER IS COMPUTED AND STORED.
# THIS NUMBER WILL BE AVAILABLE FOR DISPLAY TO THE ASTRONAUT
# THROUGH THE USE OF V06N52.
#
# THE ASTRONAUT WILL CALL THIS DISPLAY TO VERIFY THAT THE
# CENTRAL ANGLE OF TRANSFER OF THE ACTIVE VEHICLE IS NOT WITHIN
# Page 462
# 170 TO 190 DEGREES.  IF THE ANGLE IS WITHIN THIS ZONE THE
# ASTRONAUT SHOULD REASSES THE INPUT TARGETING PARAMETERS BASED
# UPON DELTA V AND EXPECTED MANEUVER TIME.
# (8)     THIS PROGRAM IS SELECTED BY THE ASTRONAUT BY DSKY ENTRY --
#
# P34 IF THIS VEHICLE IS ACTIVE VEHICLE.
#
# P74 IF THIS VEHICLE IS PASSIVE VEHICLE.
#
# INPUT
# (1)     TTPI    TIME OF THE TPI MANEUVER.
# (2)     ELEV    DESIRED LOS ANGLE AT TPI
# (3)     CENTANG ORBITAL CENTRAL ANGLE OF THE PASSIVE VEHICLE DURING
# TRANSFER FROM TPI TO TIME OF INTERCEPT
#
# OUTPUT
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
# (1)     TTPI            TIME OF TPI MANEUVER
# (2)     TIG             TIME OF TPI MANEUVER
# (3)     ELEV            DESIRED LOS ANGLE AT TPI
# (4)     CENTANG         ORBITAL CENTRAL ANGLE OF THE PASSIVE VEHICLE DURING
# TRANSFER FROM TPI TO TIME OF INTERCEPT
# (5)     DELVEET3        DELTA VELOCITY AT TPI -- REFERENCE COORDINATES
# (6)     TPASS4          TIME OF INTERCEPT
#
# COMMUNICATION TO THRUSTING PROGRAMS
# (1)     TIG             TIME OF THE TPI MANEUVER
# (2)     RTARG           OFFSET TARGET POSITION
# (3)     TPASS4          TIME OF INTERCEPT
# (4)     XDELVFLG        RESET TO INDICATE LAMBERT (AIMPOINT) VG COMPUTATION
#
# SUBROUTINES USED
# AVFLAGA
# Page 463
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
#   COUNT 35/P3474

W('35,2000', 0o04627, 'P34', 'TC', 'AVFLAGA', line=183)
W('35,2001', 0o02003, '', 'TC', 'P34/P74A', line=184)
W('35,2002', 0o04642, 'P74', 'TC', 'AVFLAGP', line=185)
W('35,2003', 0o04647, 'P34/P74A', 'TC', 'P20FLGON', 'SET UPDATFLG, TRACKFLG', line=186)
W('35,2004', 0o34614, '', 'CAF', 'V06N37', 'TTPI', line=187)
W('35,2005', 0o04575, '', 'TC', 'VNPOOH', 'Onno: The scans look like O not zero', line=188)
W('35,2006', 0o06006, '', 'TC', 'INTPRET', line=189)
W('35,2007', 0o77531, '', 'SSP', 'EXIT', kind='interp', line=190)
W('35,2010', 0o03766, '', '', 'NN', kind='operand', line=191)
W('35,2011', 0o00000, '', '', '0', kind='operand', line=192)
W('35,2012', 0o03070, '', 'TC', 'DISPLAYE', 'ELEV AND CENTANG', line=193)
W('35,2013', 0o06006, '', 'TC', 'INTPRET', line=194)
W('35,2014', 0o71214, '', 'CLEAR', 'DLOAD', kind='interp', line=195)
W('35,2015', 0o01270, '', '', 'ETPIFLAG', kind='operand', line=196)
W('35,2016', 0o03663, '', '', 'TTPI', kind='operand', line=197)
W('35,2017', 0o17413, '', 'STODL', 'TIG', kind='interp', line=198)
W('35,2020', 0o03744, '', '', 'ELEV', kind='operand', line=199)
W('35,2021', 0o43054, '', 'BZE', 'SET', kind='interp', line=200)
W('35,2022', 0o72024, '', '', 'P34/P74B', kind='operand', line=201)
W('35,2023', 0o01070, '', '', 'ETPIFLAG', kind='operand', line=202)
W('35,2024', 0o77624, 'P34/P74B', 'CALL', kind='interp', line=203)
W('35,2025', 0o10712, '', '', 'SELECTMU', kind='operand', line=204)
S('DELELO', 'equals', 0o32, line=205)
W('35,2026', 0o43145, 'P34/P74C', 'DLOAD', 'SET', kind='interp', line=206)
W('35,2027', 0o15335, '', '', 'ZEROVECS', kind='operand', line=207)
W('35,2030', 0o03461, '', '', 'ITSWICH', kind='operand', line=208)
W('35,2031', 0o43014, '', 'BON', 'CLEAR', kind='interp', line=209)
W('35,2032', 0o01310, '', '', 'ETPIFLAG', kind='operand', line=210)
# Page 464
W('35,2033', 0o72035, '', '', 'SWCHSET', kind='operand', line=212)
W('35,2034', 0o03661, '', '', 'ITSWICH', kind='operand', line=213)
W('35,2035', 0o02364, 'SWCHSET', 'STORE', 'NOMTPI', kind='interp', line=214)
W('35,2036', 0o43345, 'INTLOOP', 'DLOAD', 'DAD', kind='interp', line=215)
W('35,2037', 0o03663, '', '', 'TTPI', kind='operand', line=216)
W('35,2040', 0o02364, '', '', 'NOMTPI', kind='operand', line=217)
W('35,2041', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=218)
W('35,2042', 0o45215, '', '', 'PRECSET', kind='operand', line=219)
W('35,2043', 0o77624, '', 'CALL', kind='interp', line=220)
W('35,2044', 0o72216, '', '', 'S33/34.1', kind='operand', line=221)
W('35,2045', 0o77454, '', 'BZE', 'EXIT', kind='interp', line=222)
W('35,2046', 0o72057, '', '', 'SWCHCLR', kind='operand', line=223)
W('35,2047', 0o05650, '', 'TC', 'ALARM', line=224)
W('35,2050', 0o00611, '', 'OCT', '611', kind='data', line=225)
W('35,2051', 0o35050, '', 'CAF', 'V05N09', line=226)
W('35,2052', 0o04662, '', 'TC', 'BANKCALL', line=227)
W('35,2053', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=228)
W('35,2054', 0o04106, '', 'TC', 'GOTOPOOH', line=229)
W('35,2055', 0o02003, '', 'TC', 'P34/P74A', 'PROCEED', line=230)
W('35,2056', 0o02047, '', 'TC', '-7', 'V32', line=231)

W('35,2057', 0o43014, 'SWCHCLR', 'BONCLR', 'BON', kind='interp', line=233)
W('35,2060', 0o03601, '', '', 'ITSWICH', kind='operand', line=234)
W('35,2061', 0o72036, '', '', 'INTLOOP', kind='operand', line=235)
W('35,2062', 0o01310, '', '', 'ETPIFLAG', kind='operand', line=236)
W('35,2063', 0o72067, '', '', 'P34/P74D', 'DISPLAY TTPI', kind='operand', line=237)
W('35,2064', 0o77776, '', 'EXIT', kind='interp', line=238)
W('35,2065', 0o03070, '', 'TC', 'DISPLAYE', 'DISPLAY ELEV AND CENTANG', line=239)
W('35,2066', 0o02072, '', 'TC', 'P34/P74E', line=240)
W('35,2067', 0o77776, 'P34/P74D', 'EXIT', kind='interp', line=241)
W('35,2070', 0o34614, '', 'CAF', 'V06N37', 'TTPI', line=242)
W('35,2071', 0o04575, '', 'TC', 'VNPOOH', line=243)
W('35,2072', 0o06006, 'P34/P74E', 'TC', 'INTPRET', line=244)
W('35,2073', 0o71201, '', 'SETPD', 'DLOAD', kind='interp', line=245)
W('35,2074', 0o00001, '', '', '0D', kind='operand', line=246)
W('35,2075', 0o03746, '', '', 'RTX1', kind='operand', line=247)
W('35,2076', 0o14047, '', 'STODL', 'X1', kind='interp', line=248)
W('35,2077', 0o03754, '', '', 'CENTANG', kind='operand', line=249)
W('35,2100', 0o71406, '', 'PUSH', 'COS', kind='interp', line=250)
W('35,2101', 0o16734, '', 'STODL', 'CSTH', kind='interp', line=251)
W('35,2102', 0o77756, '', 'SIN', kind='interp', line=252)
W('35,2103', 0o26732, '', 'STOVL', 'SNTH', kind='interp', line=253)
W('35,2104', 0o03554, '', '', 'RPASS3', kind='operand', line=254)
W('35,2105', 0o77657, '', 'VSR*', kind='interp', line=255)
W('35,2106', 0o57176, '', '', '0,2', kind='operand', line=256)
W('35,2107', 0o26657, '', 'STOVL', 'RVEC', kind='interp', line=257)
W('35,2110', 0o03562, '', '', 'VPASS3', kind='operand', line=258)
W('35,2111', 0o43057, '', 'VSR*', 'SET', kind='interp', line=259)
W('35,2112', 0o57176, '', '', '0,2', kind='operand', line=260)
W('35,2113', 0o03466, '', '', 'RVSW', kind='operand', line=261)
# Page 465
W('35,2114', 0o36746, '', 'STCALL', 'VVEC', kind='interp', line=263)
W('35,2115', 0o24744, '', '', 'TIMETHET', kind='operand', line=264)
W('35,2116', 0o77745, '', 'DLOAD', kind='interp', line=265)
W('35,2117', 0o03663, '', '', 'TTPI', kind='operand', line=266)
W('35,2120', 0o03503, '', 'STORE', 'INTIME', 'FOR INITVEL', kind='interp', line=267)
W('35,2121', 0o77615, '', 'DAD', kind='interp', line=268)
W('35,2122', 0o00037, '', '', 'T', 'RENDEZVOUS TIME', kind='operand', line=269)
W('35,2123', 0o37656, '', 'STCALL', 'TPASS4', 'FOR INITVEL', kind='interp', line=270)
W('35,2124', 0o72526, '', '', 'S34/35.2', kind='operand', line=271)
W('35,2125', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=272)
W('35,2126', 0o03646, '', '', 'DELVEET3', kind='operand', line=273)
W('35,2127', 0o26635, '', 'STOVL', 'DELVTPI', kind='interp', line=274)
W('35,2130', 0o03640, '', '', 'VPASS4', kind='operand', line=275)
W('35,2131', 0o51451, '', 'VSU', 'ABVAL', kind='interp', line=276)
W('35,2132', 0o03620, '', '', 'VTPRIME', kind='operand', line=277)
W('35,2133', 0o26637, '', 'STOVL', 'DELVTPF', kind='interp', line=278)
W('35,2134', 0o03540, '', '', 'RACT3', kind='operand', line=279)
W('35,2135', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=280)
W('35,2136', 0o03612, '', '', 'VIPRIME', kind='operand', line=281)
W('35,2137', 0o45153, '', '', 'PERIAPO1', kind='operand', line=282)
W('35,2140', 0o77624, '', 'CALL', kind='interp', line=283)
W('35,2141', 0o45263, '', '', 'SHIFTR1', kind='operand', line=284)
W('35,2142', 0o16641, '', 'STODL', 'POSTTPI', kind='interp', line=285)
W('35,2143', 0o03663, '', '', 'TTPI', kind='operand', line=286)
W('35,2144', 0o03413, '', 'STORE', 'TIG', kind='interp', line=287)
W('35,2145', 0o77776, '', 'EXIT', kind='interp', line=288)
W('35,2146', 0o34616, '', 'CAF', 'V06N58', line=289)
W('35,2147', 0o04575, '', 'TC', 'VNPOOH', line=290)
W('35,2150', 0o06006, '', 'TC', 'INTPRET', line=291)
W('35,2151', 0o77624, '', 'CALL', kind='interp', line=292)
W('35,2152', 0o72741, '', '', 'S34/35.5', kind='operand', line=293)
W('35,2153', 0o77624, '', 'CALL', kind='interp', line=294)
W('35,2154', 0o73002, '', '', 'VN1645', kind='operand', line=295)
W('35,2155', 0o77650, '', 'GOTO', kind='interp', line=296)
W('35,2156', 0o72026, '', '', 'P34/P74C', kind='operand', line=297)

# Page 466
# RENDEZVOUS MID-COURSE MANEUVER PROGRAMS (P35 AND P75)
# MOD NO -1                     LOG SECTION -- P32-P35, P72-P75
# MOD BY WHITE, P.              DATE:  1 JUNE 67
#
# PURPOSE
# (1)     TO CALCULATE THE REQUIRED DELTA V AND OTHER INITIAL CONDITIONS
# REQUIRED BY THE ACTIVE VEHICLE FOR EXECUTION OF THE NEXT
# MID-COURSE CORRECTION OF THE TRANSFER PHASE OF AN ACTIVE
# VEHICLE RENDEZVOUS.
# (2)     TO DISPLAY TO THE ASTRONAUT AND THE GROUND CERTAIN DEPENDENT
# VARIABLES ASSOCIATED WITH THE MANEUVER FOR APPROVAL BY THE
# ASTRONAUT/GROUND.
# (3)     TO STORE THE TPM TARGET PARAMETERS FOR USE BY THE DESIRED
# THRUSTING PROGRAM.
#
# ASSUMPTIONS
# (1)     THE ISS NEED NOT BE ON TO COMPLETE THIS PROGRAM.
# (2)     STATE VECTOR UPDATES BY P27 ARE DISALLOWED DURING AUTOMATIC
# STATE VECTOR UPDATING INITIATED BY P20 (SEE ASSUMPTION (3)).
# (3)     THE RENDEZVOUS RADAR IS ON AND IS LOCKED ON THE CSM.  THIS WAS
# DONE DURING PREVIOUS SELECTION OF P20.  RADAR SIGHTING MARKS
# WILL BE MADE AUTOMATICALLY APPROXIMATELY ONCE A MINUTE WHEN
# ENABLED BY THE TRACK AND UPDATE FLAGS (SEE P20).  THE
# RENDEZVOUS TRACKING MARK COUNTER IS ZEROED BY THE SELECTION OF
# P20 AND AFTER EACH THRUSTING MANEUVER.
# (4)     THE OPERATION OF THE PROGRAM UTILIZES THE FOLLOWING FLAGS --
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
# (5)     THE TIME OF INTERCEPT (T(INT)) WAS DEFINED BY PREVIOUS
# COMPLETION OF THE TRANSFER PHASE INITIATION (TPI) PROGRAM
# (P34/P74) AND IS PRESENTLY AVAILABLE IN STORAGE.
# Page 467
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
# (7)     THIS PROGRAM IS SELECTED BY THE ASTRONAUT BY DSKY ENTRY --
#
# P35 IF THIS VEHICLE IS ACTIVE VEHICLE.
#
# P75 IF THIS VEHICLE IS PASSIVE VEHICLE.
#
# INPUT
# (1)     TPASS4          TIME OF INTERCEPT -- SAVED FROM P34/P74
#
# OUTPUT
# (1)     TRKMKCNT        NUMBER OF MARKS
# (2)     TTOGO           TIME TO GO
# (3)     +MGA            MIDDLE GIMBAL ANGLE
# (4)     DVLOS           DELTA VELOCITY AT MID -- LINE OF SIGHT
# (5)     DELVLVC         DELTA VELOCITY AT MID -- LOCAL VERTICAL COORDINATES
#
# DOWNLINK
# (1)     TIG             TIME OF THE TPM MANEUVER
# (2)     DELVEET3        DELTA VELOCITY AT TPM -- REFERENCE COORDINATES
# (3)     TPASS4          TIME OF INTERCEPT
#
# COMMUNICATION TO THRUSTING PROGRAMS
# (1)     TIG             TIME OF THE TPM MANEUVER
# (2)     RTARG           OFFSET TARGET POSITION
# (3)     TPASS4          TIME OF INTERCEPT
# (4)     XDELVFLG        RESET TO INDICATE LAMBERT (AIMPOINT) VG COMPUTATION.
#
# SUBROUTINES USED
# AVFLAGA
# AVFLAGP
# LOADTIME
# SELECTMU
# PRECSET
# S34/35.1
# S34/35.2
# Page 468
# S34/35.5
# VN1645

#   COUNT 35/P3575
#   EBANK= KT

W('35,2157', 0o04627, 'P35', 'TC', 'AVFLAGA', line=396)
W('35,2160', 0o00006, '', 'EXTEND', line=397)
W('35,2161', 0o31422, '', 'DCA', 'ATIGINC', line=398)
W('35,2162', 0o02166, '', 'TC', 'P35/P75A', line=399)
W('35,2163', 0o04642, 'P75', 'TC', 'AVFLAGP', line=400)
W('35,2164', 0o00006, '', 'EXTEND', line=401)
W('35,2165', 0o31424, '', 'DCA', 'PTIGINC', line=402)
W('35,2166', 0o53764, 'P35/P75A', 'DXCH', 'KT', line=403)
W('35,2167', 0o04647, '', 'TC', 'P20FLGON', 'SET UPDATFLG, TRACKFLG', line=404)
W('35,2170', 0o06006, '', 'TC', 'INTPRET', line=405)
W('35,2171', 0o77624, '', 'CALL', kind='interp', line=406)
W('35,2172', 0o10712, '', '', 'SELECTMU', kind='operand', line=407)
W('35,2173', 0o77634, 'P35/P75B', 'RTB', kind='interp', line=408)
W('35,2174', 0o45510, '', '', 'LOADTIME', kind='operand', line=409)
W('35,2175', 0o03665, '', 'STORE', 'TSTRT', kind='interp', line=410)
W('35,2176', 0o77615, '', 'DAD', kind='interp', line=411)
W('35,2177', 0o02364, '', '', 'KT', kind='operand', line=412)
W('35,2200', 0o03413, '', 'STORE', 'TIG', kind='interp', line=413)
W('35,2201', 0o03503, '', 'STORE', 'INTIME', 'FOR INITVEL', kind='interp', line=414)
W('35,2202', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=415)
W('35,2203', 0o45215, '', '', 'PRECSET', 'ADVANCE BOTH VEHICLES', kind='operand', line=416)
W('35,2204', 0o77624, '', 'CALL', kind='interp', line=417)
W('35,2205', 0o74000, '', '', 'S34/35.1', 'GET NORM AND LOS FOR TRANSFORM', kind='operand', line=418)
W('35,2206', 0o77624, '', 'CALL', kind='interp', line=419)
W('35,2207', 0o72526, '', '', 'S34/35.2', 'GET DELTA V(LV)', kind='operand', line=420)
W('35,2210', 0o77624, '', 'CALL', kind='interp', line=421)
W('35,2211', 0o72741, '', '', 'S34/35.5', kind='operand', line=422)
W('35,2212', 0o77624, '', 'CALL', kind='interp', line=423)
W('35,2213', 0o73002, '', '', 'VN1645', kind='operand', line=424)
W('35,2214', 0o77650, '', 'GOTO', kind='interp', line=425)
W('35,2215', 0o72173, '', '', 'P35/P75B', kind='operand', line=426)
# Page 469
# ***** S33/34.1 *****

W('35,2216', 0o66220, 'S33/34.1', 'STQ', 'SSP', kind='interp', line=430)
W('35,2217', 0o01340, '', '', 'NORMEX', kind='operand', line=431)
W('35,2220', 0o03665, '', '', 'TITER', kind='operand', line=432)
W('35,2221', 0o40000, '', 'OCT', '40000', kind='data', line=433)
W('35,2222', 0o40345, '', 'DLOAD', 'SETPD', kind='interp', line=434)
W('35,2223', 0o33111, '', '', 'MAX250', kind='operand', line=435)
W('35,2224', 0o00001, '', '', '0D', kind='operand', line=436)
W('35,2225', 0o27454, '', 'STOVL', 'SECMAX', kind='interp', line=437)
W('35,2226', 0o03540, '', '', 'RACT3', kind='operand', line=438)
W('35,2227', 0o27576, '', 'STOVL', 'RAPREC', kind='interp', line=439)
W('35,2230', 0o03546, '', '', 'VACT3', kind='operand', line=440)
W('35,2231', 0o27570, '', 'STOVL', 'VAPREC', kind='interp', line=441)
W('35,2232', 0o03554, '', '', 'RPASS3', kind='operand', line=442)
W('35,2233', 0o27620, '', 'STOVL', 'RPPREC', kind='interp', line=443)
W('35,2234', 0o03562, '', '', 'VPASS3', kind='operand', line=444)
W('35,2235', 0o03612, '', 'STORE', 'VPPREC', kind='interp', line=445)
W('35,2236', 0o77624, 'ELCALC', 'CALL', kind='interp', line=446)
W('35,2237', 0o74000, '', '', 'S34/35.1', 'NORMAL AND LOS', kind='operand', line=447)
W('35,2240', 0o63235, '', 'VXV', 'PDVL', kind='interp', line=448)
W('35,2241', 0o03540, '', '', 'RACT3', '(RA*VA)*RA 0D', kind='operand', line=449)
W('35,2242', 0o53515, '', 'PDVL', 'UNIT', 'ULOS AT 6D', kind='interp', line=450)
W('35,2243', 0o03540, '', '', 'RACT3', kind='operand', line=451)
W('35,2244', 0o46315, '', 'PDVL', 'VPROJ', 'XCHNJ AND UP', kind='interp', line=452)
W('35,2245', 0o51352, '', 'VSL2', 'BVSU', kind='interp', line=453)
W('35,2246', 0o02625, '', '', 'ULOS', kind='operand', line=454)
W('35,2247', 0o63256, '', 'UNIT', 'PDVL', 'UP AT 0D', kind='interp', line=455)
W('35,2250', 0o63241, '', 'DOT', 'PDVL', 'UP.UN*RA AT 0D', kind='interp', line=456)
W('35,2251', 0o00001, '', '', '0D', 'UP IN MPAC', kind='operand', line=457)
W('35,2252', 0o75241, '', 'DOT', 'SIGN', kind='interp', line=458)
W('35,2253', 0o02625, '', '', 'ULOS', kind='operand', line=459)
W('35,2254', 0o65552, '', 'SL1', 'ACOS', kind='interp', line=460)
W('35,2255', 0o50315, '', 'PDVL', 'DOT', 'EA AT 0D', kind='interp', line=461)
W('35,2256', 0o02625, '', '', 'ULOS', kind='operand', line=462)
W('35,2257', 0o03540, '', '', 'RACT3', kind='operand', line=463)
W('35,2260', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=464)
W('35,2261', 0o72264, '', '', 'TESTY', kind='operand', line=465)
W('35,2262', 0o15343, '', '', 'DPPOSMAX', kind='operand', line=466)
W('35,2263', 0o41425, '', 'DSU', 'PUSH', kind='interp', line=467)
W('35,2264', 0o71214, 'TESTY', 'BOFF', 'DLOAD', kind='interp', line=468)
W('35,2265', 0o03741, '', '', 'ITSWICH', kind='operand', line=469)
W('35,2266', 0o72513, '', '', 'ELEX', kind='operand', line=470)
W('35,2267', 0o03452, '', '', 'DELEL', kind='operand', line=471)
W('35,2270', 0o14033, '', 'STODL', 'DELELO', kind='interp', line=472)
W('35,2271', 0o77625, '', 'DSU', kind='interp', line=473)
W('35,2272', 0o03744, '', '', 'ELEV', kind='operand', line=474)
W('35,2273', 0o03452, '', 'STORE', 'DELEL', kind='interp', line=475)
W('35,2274', 0o45246, '', 'ABS', 'DSU', kind='interp', line=476)
W('35,2275', 0o33115, '', '', 'ELEPS', kind='operand', line=477)
# Page 470
W('35,2276', 0o77640, '', 'BMN', kind='interp', line=479)
W('35,2277', 0o72523, '', '', 'TIMEX', 'COMMERCIALS EVERYWHERE', kind='operand', line=480)
W('35,2300', 0o70535, 'FIGTIME', 'SLOAD', 'SR1', kind='interp', line=481)
W('35,2301', 0o03665, '', '', 'TITER', kind='operand', line=482)
W('35,2302', 0o72030, '', 'BHIZ', 'LXA,1', kind='interp', line=483)
W('35,2303', 0o01340, '', '', 'NORMEX', 'TOO MANY ITERATIONS', kind='operand', line=484)
W('35,2304', 0o00154, '', '', 'MPAC', kind='operand', line=485)
W('35,2305', 0o77330, '', 'SXA,1', 'VLOAD', kind='interp', line=486)
W('35,2306', 0o03664, '', '', 'TITER', kind='operand', line=487)
W('35,2307', 0o03554, '', '', 'RPASS3', kind='operand', line=488)
W('35,2310', 0o65256, '', 'UNIT', 'PDDL', kind='interp', line=489)
W('35,2311', 0o00045, '', '', '36D', kind='operand', line=490)
W('35,2312', 0o53515, '', 'PDVL', 'UNIT', kind='interp', line=491)
W('35,2313', 0o03540, '', '', 'RACT3', kind='operand', line=492)
W('35,2314', 0o77725, '', 'PDDL', kind='interp', line=493)
W('35,2315', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=494)
W('35,2316', 0o00045, '', '', '36D', kind='operand', line=495)
W('35,2317', 0o77621, '', 'BDSU', kind='interp', line=496)
W('35,2320', 0o00015, '', '', '12D', kind='operand', line=497)
W('35,2321', 0o14037, '', 'STODL', '30D', 'RP-RA MAGNITUDES', kind='interp', line=498)
W('35,2322', 0o15333, '', '', 'DPHALF', kind='operand', line=499)
W('35,2323', 0o41425, '', 'DSU', 'PUSH', kind='interp', line=500)
W('35,2324', 0o03744, '', '', 'ELEV', kind='operand', line=501)
W('35,2325', 0o50165, '', 'SIGN', 'BMN', kind='interp', line=502)
W('35,2326', 0o00037, '', '', '30D', kind='operand', line=503)
W('35,2327', 0o01340, '', '', 'NORMEX', kind='operand', line=504)
W('35,2330', 0o71545, '', 'DLOAD', 'COS', kind='interp', line=505)
W('35,2331', 0o56205, '', 'DMP', 'DDV', kind='interp', line=506)
W('35,2332', 0o00017, '', '', '14D', kind='operand', line=507)
W('35,2333', 0o00015, '', '', '12D', kind='operand', line=508)
W('35,2334', 0o77676, '', 'DCOMP', '', 'SINCE COS(180-A)=-COS A', kind='interp', line=509)
W('35,2335', 0o00035, '', 'STORE', '28D', kind='interp', line=510)
W('35,2336', 0o44246, '', 'ABS', 'BDSU', kind='interp', line=511)
W('35,2337', 0o15333, '', '', 'DPHALF', kind='operand', line=512)
W('35,2340', 0o77240, '', 'BMN', 'VLOAD', kind='interp', line=513)
W('35,2341', 0o01340, '', '', 'NORMEX', kind='operand', line=514)
W('35,2342', 0o02617, '', '', 'UNRM', kind='operand', line=515)
W('35,2343', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=516)
W('35,2344', 0o00007, '', '', '6D', 'UN*RA', kind='operand', line=517)
W('35,2345', 0o41241, '', 'DOT', 'DMP', kind='interp', line=518)
W('35,2346', 0o03546, '', '', 'VACT3', kind='operand', line=519)
W('35,2347', 0o00015, '', '', '12D', kind='operand', line=520)
W('35,2350', 0o47315, '', 'PDVL', 'VXV', kind='interp', line=521)
W('35,2351', 0o00001, '', '', '0D', kind='operand', line=522)
W('35,2352', 0o03562, '', '', 'VPASS3', kind='operand', line=523)
W('35,2353', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=524)
W('35,2354', 0o00001, '', '', '0D', '(RP*VP)*RP', kind='operand', line=525)
W('35,2355', 0o41241, '', 'DOT', 'DMP', kind='interp', line=526)
W('35,2356', 0o03562, '', '', 'VPASS3', kind='operand', line=527)
W('35,2357', 0o00017, '', '', '14D', kind='operand', line=528)
# Page 471
W('35,2360', 0o77621, '', 'BDSU', kind='interp', line=530)
W('35,2361', 0o63301, '', 'NORM', 'PDVL', 'NORMALIZED WA-WP 12D', kind='interp', line=531)
W('35,2362', 0o00047, '', '', 'X1', kind='operand', line=532)
W('35,2363', 0o00007, '', '', '6D', kind='operand', line=533)
W('35,2364', 0o50235, '', 'VXV', 'DOT', kind='interp', line=534)
W('35,2365', 0o00001, '', '', '0D', kind='operand', line=535)
W('35,2366', 0o02617, '', '', 'UNRM', 'RA*RP.UN 14D', kind='operand', line=536)
W('35,2367', 0o50315, '', 'PDVL', 'DOT', kind='interp', line=537)
W('35,2370', 0o00001, '', '', '0D', kind='operand', line=538)
W('35,2371', 0o00007, '', '', '6D', kind='operand', line=539)
W('35,2372', 0o65552, '', 'SL1', 'ACOS', kind='interp', line=540)
W('35,2373', 0o77765, '', 'SIGN', kind='interp', line=541)
W('35,2374', 0o43225, '', 'DSU', 'DAD', 'ALPHA PI', kind='interp', line=542)
W('35,2375', 0o15333, '', '', 'DPHALF', kind='operand', line=543)
W('35,2376', 0o03744, '', '', 'ELEV', kind='operand', line=544)
W('35,2377', 0o65525, '', 'PDDL', 'ACOS', kind='interp', line=545)
W('35,2400', 0o00035, '', '', '28D', kind='operand', line=546)
W('35,2401', 0o75221, '', 'BDSU', 'SIGN', kind='interp', line=547)
W('35,2402', 0o15333, '', '', 'DPHALF', kind='operand', line=548)
W('35,2403', 0o00037, '', '', '30D', 'CONTAINS RP-RA', kind='operand', line=549)
W('35,2404', 0o77615, '', 'DAD', kind='interp', line=550)
W('35,2405', 0o56205, '', 'DMP', 'DDV', kind='interp', line=551)
W('35,2406', 0o33107, '', '', 'TWOPI', kind='operand', line=552)
W('35,2407', 0o77605, '', 'DMP', kind='interp', line=553)
W('35,2410', 0o41257, '', 'SL*', 'DMP', kind='interp', line=554)
W('35,2411', 0o20176, '', '', '0 -3,1', kind='operand', line=555)
W('35,2412', 0o51406, '', 'PUSH', 'ABS', kind='interp', line=556)
W('35,2413', 0o50025, '', 'DSU', 'BMN', kind='interp', line=557)
W('35,2414', 0o03454, '', '', 'SECMAX', kind='operand', line=558)
W('35,2415', 0o72421, '', '', 'OKMAX', kind='operand', line=559)
W('35,2416', 0o75345, '', 'DLOAD', 'SIGN', 'REPLACE TIME WITH MAX TIME SIGNED', kind='interp', line=560)
W('35,2417', 0o03454, '', '', 'SECMAX', kind='operand', line=561)
W('35,2420', 0o77606, '', 'PUSH', kind='interp', line=562)
W('35,2421', 0o51135, 'OKMAX', 'SLOAD', 'BPL', 'TEST FIRST ITERATION', kind='interp', line=563)
W('35,2422', 0o03665, '', '', 'TITER', kind='operand', line=564)
W('35,2423', 0o72431, '', '', 'REPETE', kind='operand', line=565)
W('35,2424', 0o71331, '', 'SSP', 'DLOAD', kind='interp', line=566)
W('35,2425', 0o03665, '', '', 'TITER', kind='operand', line=567)
W('35,2426', 0o37777, '', 'OCT', '37777', kind='data', line=568)
W('35,2427', 0o77650, '', 'GOTO', kind='interp', line=569)
W('35,2430', 0o72467, '', '', 'STORDELT', kind='operand', line=570)
W('35,2431', 0o41345, 'REPETE', 'DLOAD', 'DMP', kind='interp', line=571)
W('35,2432', 0o03452, '', '', 'DELEL', kind='operand', line=572)
W('35,2433', 0o00033, '', '', 'DELELO', kind='operand', line=573)
W('35,2434', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=574)
W('35,2435', 0o72445, '', '', 'NEXTES', kind='operand', line=575)
W('35,2436', 0o03454, '', '', 'SECMAX', kind='operand', line=576)
W('35,2437', 0o77605, '', 'DMP', kind='interp', line=577)
W('35,2440', 0o33113, '', '', 'THIRD', kind='operand', line=578)
W('35,2441', 0o17454, '', 'STODL', 'SECMAX', kind='interp', line=579)
# Page 472
W('35,2442', 0o70446, '', 'ABS', 'SR1', 'CROSSED OVER SOLUTION', kind='interp', line=581)
W('35,2443', 0o52076, '', 'DCOMP', 'GOTO', 'DT=(-SIGN(DTO)//DT//)/2', kind='interp', line=582)
W('35,2444', 0o72455, '', '', 'RESIGN', kind='operand', line=583)
W('35,2445', 0o51545, 'NEXTES', 'DLOAD', 'ABS', kind='interp', line=584)
W('35,2446', 0o03452, '', '', 'DELEL', kind='operand', line=585)
W('35,2447', 0o51525, '', 'PDDL', 'ABS', kind='interp', line=586)
W('35,2450', 0o00033, '', '', 'DELELO', kind='operand', line=587)
W('35,2451', 0o77625, '', 'DSU', kind='interp', line=588)
W('35,2452', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=589)
W('35,2453', 0o72460, '', '', 'REVERS', 'WRONG DIRECTION', kind='operand', line=590)
W('35,2454', 0o77646, '', 'ABS', kind='interp', line=591)
W('35,2455', 0o52165, 'RESIGN', 'SIGN', 'GOTO', kind='interp', line=592)
W('35,2456', 0o03450, '', '', 'DELTEEO', kind='operand', line=593)
W('35,2457', 0o72467, '', '', 'STORDELT', kind='operand', line=594)
W('35,2460', 0o57545, 'REVERS', 'DLOAD', 'DCOMP', kind='interp', line=595)
W('35,2461', 0o03450, '', '', 'DELTEEO', kind='operand', line=596)
W('35,2462', 0o70406, '', 'PUSH', 'SR1', kind='interp', line=597)
W('35,2463', 0o03450, '', 'STORE', 'DELTEEO', kind='interp', line=598)
W('35,2464', 0o77615, '', 'DAD', kind='interp', line=599)
W('35,2465', 0o77650, '', 'GOTO', kind='interp', line=600)
W('35,2466', 0o72470, '', '', 'ADTIME', kind='operand', line=601)
W('35,2467', 0o03450, 'STORDELT', 'STORE', 'DELTEEO', kind='interp', line=602)
W('35,2470', 0o77615, 'ADTIME', 'DAD', kind='interp', line=603)
W('35,2471', 0o02364, '', '', 'NOMTPI', 'SUM OF DELTA T:S', kind='operand', line=604)
W('35,2472', 0o02364, '', 'STORE', 'NOMTPI', kind='interp', line=605)
W('35,2473', 0o63375, '', 'VLOAD', 'PDVL', kind='interp', line=606)
W('35,2474', 0o03570, '', '', 'VAPREC', kind='operand', line=607)
W('35,2475', 0o03576, '', '', 'RAPREC', kind='operand', line=608)
W('35,2476', 0o77624, '', 'CALL', kind='interp', line=609)
W('35,2477', 0o72701, '', '', 'GOINT', kind='operand', line=610)
W('35,2500', 0o77624, '', 'CALL', kind='interp', line=611)
W('35,2501', 0o45237, '', '', 'ACTIVE', 'STORE NEW RACT3 VACT3', kind='operand', line=612)
W('35,2502', 0o63375, '', 'VLOAD', 'PDVL', kind='interp', line=613)
W('35,2503', 0o03612, '', '', 'VPPREC', kind='operand', line=614)
W('35,2504', 0o03620, '', '', 'RPPREC', kind='operand', line=615)
W('35,2505', 0o77624, '', 'CALL', kind='interp', line=616)
W('35,2506', 0o72701, '', '', 'GOINT', kind='operand', line=617)
W('35,2507', 0o77624, '', 'CALL', kind='interp', line=618)
W('35,2510', 0o45247, '', '', 'PASSIVE', 'STORE NEW RPASS3 VPASS3', kind='operand', line=619)
W('35,2511', 0o77650, '', 'GOTO', kind='interp', line=620)
W('35,2512', 0o72236, '', '', 'ELCALC', kind='operand', line=621)
W('35,2513', 0o43345, 'ELEX', 'DLOAD', 'DAD', kind='interp', line=622)
W('35,2514', 0o03663, '', '', 'TTPI', kind='operand', line=623)
W('35,2515', 0o02364, '', '', 'NOMTPI', kind='operand', line=624)
W('35,2516', 0o17663, '', 'STODL', 'TTPI', kind='interp', line=625)
W('35,2517', 0o77614, '', 'BON', kind='interp', line=626)
W('35,2520', 0o01310, '', '', 'ETPIFLAG', kind='operand', line=627)
W('35,2521', 0o72523, '', '', 'TIMEX', kind='operand', line=628)
W('35,2522', 0o03744, '', 'STORE', 'ELEV', kind='interp', line=629)
W('35,2523', 0o52145, 'TIMEX', 'DLOAD', 'GOTO', kind='interp', line=630)
# Page 473
W('35,2524', 0o15335, '', '', 'ZEROVECS', kind='operand', line=632)
W('35,2525', 0o01340, '', '', 'NORMEX', kind='operand', line=633)

# Page 474
# ***** S34/35.1 *****

# COMPUTE UNIT NORMAL AND LINE OF SIGHT VECTORS GIVEN THE ACTIVE AND
# PASSIVE POS AND VEL AT TIME T3
#   SETLOC S3435LOC
#   BANK

W('36,2000', 0o52375, 'S34/35.1', 'VLOAD', 'VSU', kind='interp', line=643)
W('36,2001', 0o03554, '', '', 'RPASS3', kind='operand', line=644)
W('36,2002', 0o03540, '', '', 'RACT3', kind='operand', line=645)
W('36,2003', 0o41456, '', 'UNIT', 'PUSH', kind='interp', line=646)
W('36,2004', 0o26625, '', 'STOVL', 'ULOS', kind='interp', line=647)
W('36,2005', 0o03540, '', '', 'RACT3', kind='operand', line=648)
W('36,2006', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=649)
W('36,2007', 0o03546, '', '', 'VACT3', kind='operand', line=650)
W('36,2010', 0o02617, '', 'STORE', 'UNRM', kind='interp', line=651)
W('36,2011', 0o77616, '', 'RVQ', kind='interp', line=652)

# Page 475
# ***** S34/35.2 *****

# ADVANCE PASSIVE VEH TO RENDEZVOUS TIME AND GET REQ VEL FROM LAMBERT
#   SETLOC CSI/CDH
#   BANK

W('35,2526', 0o77220, 'S34/35.2', 'STQ', 'VLOAD', kind='interp', line=661)
W('35,2527', 0o02370, '', '', 'SUBEXIT', kind='operand', line=662)
W('35,2530', 0o03562, '', '', 'VPASS3', kind='operand', line=663)
W('35,2531', 0o65315, '', 'PDVL', 'PDDL', kind='interp', line=664)
W('35,2532', 0o03554, '', '', 'RPASS3', kind='operand', line=665)
W('35,2533', 0o03503, '', '', 'INTIME', kind='operand', line=666)
W('35,2534', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=667)
W('35,2535', 0o03656, '', '', 'TPASS4', kind='operand', line=668)
W('35,2536', 0o33107, '', '', 'TWOPI', 'CONIC', kind='operand', line=669)
W('35,2537', 0o46125, '', 'PDDL', 'BHIZ', kind='interp', line=670)
W('35,2540', 0o03766, '', '', 'NN', kind='operand', line=671)
W('35,2541', 0o72544, '', '', 'S3435.23', kind='operand', line=672)
W('35,2542', 0o65345, '', 'DLOAD', 'PDDL', kind='interp', line=673)
W('35,2543', 0o15335, '', '', 'ZEROVECS', 'PRECISION', kind='operand', line=674)
W('35,2544', 0o77624, 'S3435.23', 'CALL', kind='interp', line=675)
W('35,2545', 0o72705, '', '', 'INTINT', 'GET TARGET VECTOR', kind='operand', line=676)
W('35,2546', 0o27415, 'S3435.25', 'STOVL', 'RTARG', kind='interp', line=677)
W('35,2547', 0o00007, '', '', 'VATT', kind='operand', line=678)
W('35,2550', 0o27640, '', 'STOVL', 'VPASS4', kind='interp', line=679)
W('35,2551', 0o03415, '', '', 'RTARG', kind='operand', line=680)
# COMPUTE PHI = PI + (ACOS(UNIT RA.UNIT RP) - PI) SIGN(RA*RP.U)
W('35,2552', 0o63256, '', 'UNIT', 'PDVL', 'UNIT RP', kind='interp', line=682)
W('35,2553', 0o03540, '', '', 'RACT3', kind='operand', line=683)
W('35,2554', 0o41456, '', 'UNIT', 'PUSH', 'UNIT RA', kind='interp', line=684)
W('35,2555', 0o50235, '', 'VXV', 'DOT', kind='interp', line=685)
W('35,2556', 0o00001, '', '', '0D', kind='operand', line=686)
W('35,2557', 0o02617, '', '', 'UNRM', 'RA*RP.U', kind='operand', line=687)
W('35,2560', 0o77715, '', 'PDVL', kind='interp', line=688)
W('35,2561', 0o72441, '', 'DOT', 'SL1', 'UNIT RA.UNIT RP', kind='interp', line=689)
W('35,2562', 0o00001, '', '', '0D', kind='operand', line=690)
W('35,2563', 0o75326, '', 'ACOS', 'SIGN', kind='interp', line=691)
W('35,2564', 0o43244, '', 'BPL', 'DAD', kind='interp', line=692)
W('35,2565', 0o72567, '', '', 'NOPIE', kind='operand', line=693)
W('35,2566', 0o15343, '', '', 'DPPOSMAX', 'REASONABLE TWO PI', kind='operand', line=694)
W('35,2567', 0o16633, 'NOPIE', 'STODL', 'ACTCENT', kind='interp', line=695)
W('35,2570', 0o03656, '', '', 'TPASS4', kind='operand', line=696)
W('35,2571', 0o77625, '', 'DSU', kind='interp', line=697)
W('35,2572', 0o03503, '', '', 'INTIME', kind='operand', line=698)
W('35,2573', 0o03423, '', 'STORE', 'DELLT4', kind='interp', line=699)
W('35,2574', 0o40335, '', 'SLOAD', 'SETPD', kind='interp', line=700)
W('35,2575', 0o03766, '', '', 'NN', 'NUMBER OF OFFSETS', kind='operand', line=701)
W('35,2576', 0o00001, '', '', '0D', kind='operand', line=702)
W('35,2577', 0o63325, '', 'PDDL', 'PDVL', kind='interp', line=703)
W('35,2600', 0o33122, '', '', 'EPSFOUR', kind='operand', line=704)
# Page 476
W('35,2601', 0o03540, '', '', 'RACT3', kind='operand', line=706)
W('35,2602', 0o27570, '', 'STOVL', 'RINIT', kind='interp', line=707)
W('35,2603', 0o03546, '', '', 'VACT3', kind='operand', line=708)
W('35,2604', 0o37576, '', 'STCALL', 'VINIT', kind='interp', line=709)
W('35,2605', 0o22000, '', '', 'INITVEL', kind='operand', line=710)
W('35,2606', 0o77624, '', 'CALL', kind='interp', line=711)
W('35,2607', 0o72666, '', '', 'LOMAT', kind='operand', line=712)
W('35,2610', 0o64375, '', 'VLOAD', 'MXV', kind='interp', line=713)
W('35,2611', 0o03646, '', '', 'DELVEET3', kind='operand', line=714)
W('35,2612', 0o00001, '', '', '0D', kind='operand', line=715)
W('35,2613', 0o77772, '', 'VSL1', kind='interp', line=716)
W('35,2614', 0o37405, '', 'STCALL', 'DELVLVC', kind='interp', line=717)
W('35,2615', 0o02370, '', '', 'SUBEXIT', kind='operand', line=718)

# Page 477
# ***** S34/35.3 *****

W('35,2616', 0o45020, 'S34/35.3', 'STQ', 'CALL', kind='interp', line=723)
W('35,2617', 0o01340, '', '', 'NORMEX', kind='operand', line=724)
W('35,2620', 0o72666, '', '', 'LOMAT', 'GET MATRIX IN PUSH LIST', kind='operand', line=725)
W('35,2621', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=726)
W('35,2622', 0o03405, '', '', 'DELVLVC', 'NEW DEL V TPI', kind='operand', line=727)
W('35,2623', 0o00001, '', '', '0D', kind='operand', line=728)
W('35,2624', 0o77772, '', 'VSL1', kind='interp', line=729)
W('35,2625', 0o03646, '', 'STORE', 'DELVEET3', 'SAVE FOR TRANSFORM', kind='interp', line=730)
W('35,2626', 0o63255, '', 'VAD', 'PDVL', kind='interp', line=731)
W('35,2627', 0o03546, '', '', 'VACT3', 'NEW V REQ', kind='operand', line=732)
W('35,2630', 0o03540, '', '', 'RACT3', kind='operand', line=733)
W('35,2631', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=734)
W('35,2632', 0o03413, '', '', 'TIG', kind='operand', line=735)
W('35,2633', 0o03656, '', '', 'TPASS4', kind='operand', line=736)
W('35,2634', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=737)
W('35,2635', 0o15343, '', '', 'DPPOSMAX', kind='operand', line=738)
W('35,2636', 0o77624, '', 'CALL', '', 'INTEG. FOR NEW TARGET VEC', kind='interp', line=739)
W('35,2637', 0o72705, '', '', 'INTINT', kind='operand', line=740)
W('35,2640', 0o77775, '', 'VLOAD', kind='interp', line=741)
W('35,2641', 0o00001, '', '', 'RATT', kind='operand', line=742)
W('35,2642', 0o03415, '', 'STORE', 'RTARG', kind='interp', line=743)
W('35,2643', 0o41575, 'NOVRWRT', 'VLOAD', 'PUSH', kind='interp', line=744)
W('35,2644', 0o02625, '', '', 'ULOS', kind='operand', line=745)
W('35,2645', 0o57435, '', 'VXV', 'VCOMP', kind='interp', line=746)
W('35,2646', 0o02617, '', '', 'UNRM', kind='operand', line=747)
W('35,2647', 0o41456, '', 'UNIT', 'PUSH', kind='interp', line=748)
W('35,2650', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=749)
W('35,2651', 0o02625, '', '', 'ULOS', kind='operand', line=750)
W('35,2652', 0o77715, '', 'PDVL', kind='interp', line=751)
W('35,2653', 0o64315, '', 'PDVL', 'MXV', kind='interp', line=752)
W('35,2654', 0o03646, '', '', 'DELVEET3', kind='operand', line=753)
W('35,2655', 0o00001, '', '', '0D', kind='operand', line=754)
W('35,2656', 0o77772, '', 'VSL1', kind='interp', line=755)
W('35,2657', 0o36611, '', 'STCALL', 'DVLOS', kind='interp', line=756)
W('35,2660', 0o01340, '', '', 'NORMEX', kind='operand', line=757)

# Page 478
# ***** S34/35.4 *****

W('35,2661', 0o40220, 'S34/35.4', 'STQ', 'SETPD', 'NO ASTRONAUT OVERWRITE', kind='interp', line=762)
W('35,2662', 0o01340, '', '', 'NORMEX', kind='operand', line=763)
W('35,2663', 0o00001, '', '', '0D', kind='operand', line=764)
W('35,2664', 0o77650, '', 'GOTO', kind='interp', line=765)
W('35,2665', 0o72643, '', '', 'NOVRWRT', kind='operand', line=766)

# Page 479
# ***** LOMAT *****

W('35,2666', 0o57575, 'LOMAT', 'VLOAD', 'VCOMP', kind='interp', line=771)
W('35,2667', 0o02617, '', '', 'UNRM', kind='operand', line=772)
W('35,2670', 0o24007, '', 'STOVL', '6D', 'Y', kind='interp', line=773)
W('35,2671', 0o03540, '', '', 'RACT3', kind='operand', line=774)
W('35,2672', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=775)
W('35,2673', 0o00015, '', 'STORE', '12D', kind='interp', line=776)
W('35,2674', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=777)
W('35,2675', 0o02617, '', '', 'UNRM', 'Z*-Y', kind='operand', line=778)
W('35,2676', 0o00001, '', 'STORE', '0D', kind='interp', line=779)
W('35,2677', 0o43401, '', 'SETPD', 'RVQ', kind='interp', line=780)
W('35,2700', 0o00023, '', '', '18D', kind='operand', line=781)
W('35,2701', 0o65325, 'GOINT', 'PDDL', 'PDDL', 'DO', kind='interp', line=782)
W('35,2702', 0o15335, '', '', 'ZEROVECS', '      NOT', kind='operand', line=783)
W('35,2703', 0o02364, '', '', 'NOMTPI', kind='operand', line=784)
W('35,2704', 0o41406, '', 'PUSH', 'PUSH', '              ORDER OR INSERT BEFORE INTINT', kind='interp', line=785)
W('35,2705', 0o45020, 'INTINT', 'STQ', 'CALL', kind='interp', line=786)
W('35,2706', 0o02367, '', '', 'RTRN', kind='operand', line=787)
W('35,2707', 0o27442, '', '', 'INTSTALL', kind='operand', line=788)
W('35,2710', 0o71214, '', 'CLEAR', 'DLOAD', kind='interp', line=789)
W('35,2711', 0o01673, '', '', 'INTYPFLG', kind='operand', line=790)
W('35,2712', 0o43054, '', 'BZE', 'SET', kind='interp', line=791)
W('35,2713', 0o72715, '', '', '+2', kind='operand', line=792)
W('35,2714', 0o01473, '', '', 'INTYPFLG', kind='operand', line=793)
W('35,2715', 0o45545, '', 'DLOAD', 'STADR', kind='interp', line=794)
W('35,2716', 0o63736, '', 'STODL', 'TDEC1', kind='interp', line=795)
W('35,2717', 0o73014, '', 'SET', 'LXA,2', kind='interp', line=796)
W('35,2720', 0o00063, '', '', 'MOONFLAG', kind='operand', line=797)
W('35,2721', 0o03746, '', '', 'RTX2', kind='operand', line=798)
W('35,2722', 0o43014, '', 'BON', 'CLEAR', kind='interp', line=799)
W('35,2723', 0o04303, '', '', 'CMOONFLG', kind='operand', line=800)
W('35,2724', 0o72726, '', '', 'ALLSET', kind='operand', line=801)
W('35,2725', 0o00263, '', '', 'MOONFLAG', kind='operand', line=802)
W('35,2726', 0o25517, 'ALLSET', 'STOVL', 'TET', kind='interp', line=803)
W('35,2727', 0o77657, '', 'VSR*', kind='interp', line=804)
W('35,2730', 0o57176, '', '', '0,2', kind='operand', line=805)
W('35,2731', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=806)
W('35,2732', 0o77657, '', 'VSR*', kind='interp', line=807)
W('35,2733', 0o57176, '', '', '0,2', kind='operand', line=808)
W('35,2734', 0o35543, '', 'STCALL', 'VCV', kind='interp', line=809)
W('35,2735', 0o27135, '', '', 'INTEGRVS', kind='operand', line=810)
W('35,2736', 0o52175, '', 'VLOAD', 'GOTO', kind='interp', line=811)
W('35,2737', 0o00001, '', '', 'RATT', kind='operand', line=812)
W('35,2740', 0o02367, '', '', 'RTRN', kind='operand', line=813)

# Page 480
# ***** S34/35.5 *****
#
# SUBROUTINES USED
# BANKCALL
# GOFLASH
# GOTOPOOH
# S34/35.3
# S34.35.4
# VNPOOH

W('35,2741', 0o43020, 'S34/35.5', 'STQ', 'BON', kind='interp', line=826)
W('35,2742', 0o02370, '', '', 'SUBEXIT', kind='operand', line=827)
W('35,2743', 0o01311, '', '', 'FINALFLG', kind='operand', line=828)
W('35,2744', 0o72750, '', '', 'FLAGON', kind='operand', line=829)
W('35,2745', 0o52014, '', 'SET', 'GOTO', kind='interp', line=830)
W('35,2746', 0o00470, '', '', 'UPDATFLG', kind='operand', line=831)
W('35,2747', 0o72772, '', '', 'FLAGOFF', kind='operand', line=832)
W('35,2750', 0o77775, 'FLAGON', 'VLOAD', kind='interp', line=833)
W('35,2751', 0o03405, '', '', 'DELVLVC', kind='operand', line=834)
W('35,2752', 0o02611, '', 'STORE', 'DVLOS', 'SAVE DELTA V BEFORE DISPLAY', kind='interp', line=835)
W('35,2753', 0o77776, '', 'EXIT', kind='interp', line=836)
W('35,2754', 0o34620, '', 'CAF', 'V06N81', line=837)
W('35,2755', 0o04575, '', 'TC', 'VNPOOH', line=838)
W('35,2756', 0o06006, '', 'TC', 'INTPRET', line=839)
W('35,2757', 0o52375, '', 'VLOAD', 'VSU', 'TEST FOR OVERWRITE OF COMPUTED', kind='interp', line=840)
W('35,2760', 0o03405, '', '', 'DELVLVC', '                     DELTA V', kind='operand', line=841)
W('35,2761', 0o02611, '', '', 'DVLOS', kind='operand', line=842)
W('35,2762', 0o53046, '', 'ABVAL', 'BZE', kind='interp', line=843)
W('35,2763', 0o72766, '', '', 'NOCHG', 'NO OVERWRITE', kind='operand', line=844)
W('35,2764', 0o77624, '', 'CALL', kind='interp', line=845)
W('35,2765', 0o72616, '', '', 'S34/35.3', kind='operand', line=846)
W('35,2766', 0o77214, 'NOCHG', 'CLEAR', 'VLOAD', kind='interp', line=847)
W('35,2767', 0o01267, '', '', 'XDELVFLG', kind='operand', line=848)
W('35,2770', 0o03646, '', '', 'DELVEET3', kind='operand', line=849)
W('35,2771', 0o03646, '', 'STORE', 'DELVSIN', kind='interp', line=850)
W('35,2772', 0o77624, 'FLAGOFF', 'CALL', kind='interp', line=851)
W('35,2773', 0o72661, '', '', 'S34/35.4', kind='operand', line=852)
W('35,2774', 0o77776, '', 'EXIT', kind='interp', line=853)
W('35,2775', 0o34617, '', 'CAF', 'V06N59', line=854)
W('35,2776', 0o04575, '', 'TC', 'VNPOOH', line=855)
W('35,2777', 0o06006, '', 'TC', 'INTPRET', line=856)
W('35,3000', 0o77650, '', 'GOTO', kind='interp', line=857)
W('35,3001', 0o02370, '', '', 'SUBEXIT', kind='operand', line=858)

# Page 481
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

W('35,3002', 0o71220, 'VN1645', 'STQ', 'DLOAD', kind='interp', line=873)
W('35,3003', 0o02370, '', '', 'SUBEXIT', kind='operand', line=874)
W('35,3004', 0o33120, '', '', 'DP-.01', kind='operand', line=875)
W('35,3005', 0o03626, '', 'STORE', '+MGA', 'MGA = -.01', kind='interp', line=876)
W('35,3006', 0o71214, '', 'BOFF', 'DLOAD', kind='interp', line=877)
W('35,3007', 0o01351, '', '', 'FINALFLG', kind='operand', line=878)
W('35,3010', 0o73030, '', '', 'GET45', kind='operand', line=879)
W('35,3011', 0o33120, '', '', 'DP-.01', kind='operand', line=880)
W('35,3012', 0o77615, '', 'DAD', kind='interp', line=881)
W('35,3013', 0o33120, '', '', 'DP-.01', kind='operand', line=882)
W('35,3014', 0o03626, '', 'STORE', '+MGA', 'MGA = -.02', kind='interp', line=883)
W('35,3015', 0o77414, '', 'BOFF', 'EXIT', kind='interp', line=884)
W('35,3016', 0o01742, '', '', 'REFSMFLG', kind='operand', line=885)
W('35,3017', 0o73030, '', '', 'GET45', kind='operand', line=886)
W('35,3020', 0o03100, '', 'TC', 'P3XORP7X', line=887)
W('35,3021', 0o03023, '', 'TC', '+2', 'P3X', line=888)
W('35,3022', 0o03031, '', 'TC', 'GET45 +1', 'P7X', line=889)
W('35,3023', 0o06006, '', 'TC', 'INTPRET', line=890)
W('35,3024', 0o41575, '', 'VLOAD', 'PUSH', kind='interp', line=891)
W('35,3025', 0o03646, '', '', 'DELVSIN', kind='operand', line=892)
W('35,3026', 0o77624, '', 'CALL', '', 'COMPUTE MGA', kind='interp', line=893)
W('35,3027', 0o10654, '', '', 'GET+MGA', kind='operand', line=894)
W('35,3030', 0o77776, 'GET45', 'EXIT', kind='interp', line=895)
W('35,3031', 0o03304, '', 'TC', 'COMPTGO', 'INITIATE TASK TO UPDATE TTOGO', line=896)
W('35,3032', 0o31770, '', 'CA', 'SUBEXIT', line=897)
W('35,3033', 0o55766, '', 'TS', 'QSAVED', line=898)
W('35,3034', 0o35041, '', 'CAF', '1SEC', line=899)
W('35,3035', 0o04662, '', 'TC', 'BANKCALL', line=900)
W('35,3036', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=901)
W('35,3037', 0o34621, '', 'CAF', 'V16N45', 'TRKMKCNT, TTOGO, +MGA', line=902)
W('35,3040', 0o04662, '', 'TC', 'BANKCALL', line=903)
W('35,3041', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=904)
W('35,3042', 0o03045, '', 'TC', 'KILCLOCK', 'TERMINATE', line=905)
W('35,3043', 0o03050, '', 'TC', 'N45PROC', 'PROCEED', line=906)
W('35,3044', 0o03060, '', 'TC', 'CLUPDATE', 'RECYCLE -- RETURN FOR INITIAL COMPUTATION', line=907)
W('35,3045', 0o30005, 'KILCLOCK', 'CA', 'Z', line=908)
W('35,3046', 0o54000, '', 'TS', 'DISPDEX', line=909)
# Page 482
W('35,3047', 0o04106, '', 'TC', 'GOTOPOOH', line=911)
W('35,3050', 0o40076, 'N45PROC', 'CS', 'FLAGWRD2', line=912)
W('35,3051', 0o75012, '', 'MASK', 'BIT6', line=913)
W('35,3052', 0o00006, '', 'EXTEND', line=914)
W('35,3053', 0o13045, '', 'BZF', 'KILCLOCK', 'FINALFLG IS SET -- FLASH V37 -- AWAIT NEW PGM', line=915)
W('35,3054', 0o05412, '', 'TC', 'PHASCHNG', line=916)
W('35,3055', 0o04024, '', 'OCT', '04024', kind='data', line=917)
W('35,3056', 0o05546, '', 'TC', 'UPFLAG', 'SET', line=918)
W('35,3057', 0o00047, '', 'ADRES', 'FINALFLG', 'FINALFLG', kind='data', line=919)
W('35,3060', 0o30005, 'CLUPDATE', 'CA', 'Z', line=920)
W('35,3061', 0o54000, '', 'TS', 'DISPDEX', line=921)
W('35,3062', 0o05412, '', 'TC', 'PHASCHNG', line=922)
W('35,3063', 0o04024, '', 'OCT', '04024', kind='data', line=923)
W('35,3064', 0o06006, '', 'TC', 'INTPRET', line=924)
W('35,3065', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=925)
W('35,3066', 0o00670, '', '', 'UPDATFLG', kind='operand', line=926)
W('35,3067', 0o02366, '', '', 'QSAVED', kind='operand', line=927)

# Page 483
# ***** DISPLAYE *****
#
# SUBROUTINES USED
# BANKCALL
# GOFLASHR
# GOTOPOOH
# BLANKET
# ENDOFJOB

W('35,3070', 0o00006, 'DISPLAYE', 'EXTEND', line=939)
W('35,3071', 0o23340, '', 'QXCH', 'NORMEX', line=940)
W('35,3072', 0o34615, '', 'CAF', 'V06N55', line=941)
W('35,3073', 0o04662, '', 'TCR', 'BANKCALL', line=942)
W('35,3074', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=943)
W('35,3075', 0o14106, '', 'TCF', 'GOTOPOOH', line=944)
W('35,3076', 0o01340, '', 'TC', 'NORMEX', line=945)
W('35,3077', 0o13072, '', 'TCF', '-5', line=946)

# Page 484
# ***** P3XORP7X *****

W('35,3100', 0o37713, 'P3XORP7X', 'CAF', 'HIGH9', line=951)
W('35,3101', 0o71011, '', 'MASK', 'MODREG', line=952)
W('35,3102', 0o00006, '', 'EXTEND', line=953)
W('35,3103', 0o13105, '', 'BZF', '+2', line=954)
W('35,3104', 0o24002, '', 'INCR', 'Q', line=955)
W('35,3105', 0o00002, '', 'RETURN', line=956)

# ***** VNPOOH *****
#
# SUBROUTINES USED
# BANKCALL
# GOFLASH
# GOTOPOOH

#   SETLOC P30SUBS
#   BANK

W('4575', 0o00006, 'VNPOOH', 'EXTEND', line=968)
W('4576', 0o23767, '', 'QXCH', 'RTRN', line=969)
W('4577', 0o55765, '', 'TS', 'VERBNOUN', line=970)
W('4600', 0o34610, '', 'CAF', 'VNBANK', '***** THIS ROUTINE MUST REMAIN IN', line=971)
W('4601', 0o56004, '', 'XCH', 'FBANK', '      FIXED-FIXED *****', line=972)
W('4602', 0o55063, '', 'TS', 'TBASE5', '* WATCH OUT *', line=973)

W('4603', 0o31765, '', 'CA', 'VERBNOUN', line=975)
W('4604', 0o04662, '', 'TCR', 'BANKCALL', line=976)
W('4605', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=977)
W('4606', 0o14106, '', 'TCF', 'GOTOPOOH', line=978)
W('4607', 0o14611, '', 'TCF', '+2', line=979)
W('4610', 0o04603, 'VNBANK', 'TC', '-5', line=980)

W('4611', 0o31063, '', 'CA', 'TBASE5', line=982)
W('4612', 0o54004, '', 'TS', 'FBANK', line=983)
W('4613', 0o01767, '', 'TC', 'RTRN', line=984)

# Page 485
# ***** CONSTANTS *****

W('4614', 0o01445, 'V06N37', 'VN', '0637', kind='data', line=989)
W('4615', 0o01467, 'V06N55', 'VN', '0655', kind='data', line=990)
W('4616', 0o01472, 'V06N58', 'VN', '0658', kind='data', line=991)
W('4617', 0o01473, 'V06N59', 'VN', '0659', kind='data', line=992)
W('4620', 0o01521, 'V06N81', 'VN', '0681', kind='data', line=993)
W('4621', 0o04055, 'V16N45', 'VN', '1645', kind='data', line=994)
#   SETLOC CSI/CDH
#   BANK

W('35,3106', 0o14441, 'TWOPI', '2DEC', '6.283185307 B-4', kind='data', line=998)
W('35,3107', 0o37325, kind='data', line=998)
W('35,3110', 0o00001, 'MAX250', '2DEC', '25 E3 B-28', 'RSB 2004 added the B-28. OH 2009 leave?', kind='data', line=999)
W('35,3111', 0o20650, kind='data', line=999)
W('35,3112', 0o12525, 'THIRD', '2DEC', '.333333333', kind='data', line=1000)
W('35,3113', 0o12525, kind='data', line=1000)
W('35,3114', 0o00004, 'ELEPS', '2DEC', '.27777777 E-3', kind='data', line=1001)
W('35,3115', 0o21505, kind='data', line=1001)
W('35,3116', 0o00002, 'DECTWO', 'OCT', '2', kind='data', line=1002)
W('35,3117', 0o77777, 'DP-.01', 'OCT', '77777', 'CONSTANTS', kind='data', line=1003)
W('35,3120', 0o61337, '', 'OCT', '61337', 'ADJACENT      -.01 FOR MGA DSP', kind='data', line=1004)
W('35,3121', 0o01252, 'EPSFOUR', '2DEC', '.0416666666', kind='data', line=1005)
W('35,3122', 0o25253, kind='data', line=1005)

# Page 486
# ***** INITVEL *****
# MOD NO -1                     LOG SECTION -- P34-P35, P74-P75
# MOD BY WHITE, P.              DATE:  21 NOV 67
#
# FUNCTIONAL DESCRIPTION
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
# L       CALL
# L+1             INITVEL
# L+2     (RETURN -- ALWAYS)
#
# INPUT
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
# Page 487
# OUTPUT
# (1)     RTARG           OFFSET TARGET POSITION VECTOR
# (2)     VIPRIME         MANEUVER VELOCITY REQUIRED
# (3)     VTPRIME         VELOCITY AT TARGET AFTER MANEUVER
# (4)     DELVEET3        DELTA VELOCITY REQUIRED FOR MANEUVER
#
# SUBROUTINES USED
# LAMBERT
# INTSTALL
# INTEGRVS

#   SETLOC INTVEL
#   BANK

#   COUNT 11/INITV
W('11,2000', 0o77614, 'INITVEL', 'SET', '', 'COGA GUESS NOT AVAILABLE', kind='interp', line=1070)
W('11,2001', 0o00475, '', '', 'GUESSW', kind='operand', line=1071)
W('11,2002', 0o44175, 'HAVEGUES', 'VLOAD', 'STQ', kind='interp', line=1072)
W('11,2003', 0o03415, '', '', 'RTARG', kind='operand', line=1073)
W('11,2004', 0o01340, '', '', 'NORMEX', kind='operand', line=1074)
W('11,2005', 0o03604, '', 'STORE', 'RTARG1', kind='interp', line=1075)
W('11,2006', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=1076)
W('11,2007', 0o03747, '', '', 'RTX2', kind='operand', line=1077)
W('11,2010', 0o22022, '', '', 'INITVEL1', kind='operand', line=1078)
W('11,2011', 0o72575, '', 'VLOAD', 'VSL2', kind='interp', line=1079)
W('11,2012', 0o03570, '', '', 'RINIT', 'B29', kind='operand', line=1080)
W('11,2013', 0o27570, '', 'STOVL', 'RINIT', 'B27', kind='interp', line=1081)
W('11,2014', 0o03576, '', '', 'VINIT', 'B7', kind='operand', line=1082)
W('11,2015', 0o77752, '', 'VSL2', kind='interp', line=1083)
W('11,2016', 0o27576, '', 'STOVL', 'VINIT', 'B5', kind='interp', line=1084)
W('11,2017', 0o03604, '', '', 'RTARG1', kind='operand', line=1085)
W('11,2020', 0o77752, '', 'VSL2', kind='interp', line=1086)
W('11,2021', 0o03604, '', 'STORE', 'RTARG1', kind='interp', line=1087)

# INITIALIZATION

W('11,2022', 0o71331, 'INITVEL1', 'SSP', 'DLOAD', 'SET ITCTR TO -1,LOAD MPAC WITH E4 (PL 2D)', kind='interp', line=1091)
W('11,2023', 0o03505, '', '', 'ITCTR', kind='operand', line=1092)
W('11,2024', 0o77776, '', '', '0 -1', kind='operand', line=1093)
W('11,2025', 0o70546, '', 'COSINE', 'SR1', 'CALCULATE COSINE (E4) (+2)', kind='interp', line=1094)
W('11,2026', 0o17630, '', 'STODL', 'COZY4', 'SET COZY4 TO COSINE (E4) (PL 0D)', kind='interp', line=1095)
W('11,2027', 0o67154, '', 'LXA,2', 'SXA,2', kind='interp', line=1096)
W('11,2030', 0o00154, '', '', 'MPAC', kind='operand', line=1097)
W('11,2031', 0o02703, '', '', 'VTARGTAG', 'SET VTARGTAG TO 0D (SP)', kind='operand', line=1098)
W('11,2032', 0o77775, '', 'VLOAD', kind='interp', line=1099)
W('11,2033', 0o03570, '', '', 'RINIT', kind='operand', line=1100)
W('11,2034', 0o26657, '', 'STOVL', 'R1VEC', 'R1VEC EQ RINIT', kind='interp', line=1101)
W('11,2035', 0o03604, '', '', 'RTARG1', kind='operand', line=1102)
# Page 488
W('11,2036', 0o16665, '', 'STODL', 'R2VEC', 'R2VEC EQ RTARG', kind='interp', line=1104)
W('11,2037', 0o03423, '', '', 'DELLT4', kind='operand', line=1105)
W('11,2040', 0o02673, '', 'STORE', 'TDESIRED', 'TDESIRED EQ DELLT4', kind='interp', line=1106)
W('11,2041', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=1107)
W('11,2042', 0o00001, '', '', '0D', 'INITIALIZE PL TO 0D', kind='operand', line=1108)
W('11,2043', 0o03570, '', '', 'RINIT', 'MPAC EQ RINIT (+29)', kind='operand', line=1109)
W('11,2044', 0o41456, '', 'UNIT', 'PUSH', 'UNIT(RI) (+1)         (PL 6D)', kind='interp', line=1110)
W('11,2045', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1111)
W('11,2046', 0o03576, '', '', 'VINIT', 'MPAC EQ UNIT(RI) X VI (+8)', kind='operand', line=1112)
W('11,2047', 0o26676, '', 'STOVL', 'UN', kind='interp', line=1113)
W('11,2050', 0o03604, '', '', 'RTARG1', kind='operand', line=1114)
W('11,2051', 0o50256, '', 'UNIT', 'DOT', 'TEMP=URT.URI (+2)     (PL 0D)', kind='interp', line=1115)
W('11,2052', 0o43015, '', 'DAD', 'CLEAR', kind='interp', line=1116)
W('11,2053', 0o03630, '', '', 'COZY4', kind='operand', line=1117)
W('11,2054', 0o03665, '', '', 'NORMSW', kind='operand', line=1118)
W('11,2055', 0o03630, '', 'STORE', 'COZY4', kind='interp', line=1119)
W('11,2056', 0o43044, 'INITVEL2', 'BPL', 'SET', kind='interp', line=1120)
W('11,2057', 0o22101, '', '', 'INITVEL3', 'UN CALCULATED IN LAMBERT', kind='operand', line=1121)
W('11,2060', 0o03465, '', '', 'NORMSW', kind='operand', line=1122)

# ROTATE RC INTO YC PLANE -- SET UNIT NORMAL TO YC

W('11,2061', 0o41575, '', 'VLOAD', 'PUSH', '                                 (PL 6D)', kind='interp', line=1126)
W('11,2062', 0o02665, '', '', 'R2VEC', 'RC TO 6D (+29)', kind='operand', line=1127)
W('11,2063', 0o63246, '', 'ABVAL', 'PDVL', 'RC TO MPAC, ABVAL(RC) (+29) TO OD(PL 2D)', kind='interp', line=1128)
W('11,2064', 0o46206, '', 'PUSH', 'VPROJ', '                                 (PL 8D)', kind='interp', line=1129)
W('11,2065', 0o02676, '', '', 'UN', kind='operand', line=1130)
W('11,2066', 0o51352, '', 'VSL2', 'BVSU', kind='interp', line=1131)
W('11,2067', 0o74256, '', 'UNIT', 'VXSC', '                                 (PL 0D)', kind='interp', line=1132)
W('11,2070', 0o77772, '', 'VSL1', kind='interp', line=1133)
W('11,2071', 0o02665, '', 'STORE', 'R2VEC', kind='interp', line=1134)
W('11,2072', 0o67351, '', 'TLOAD', 'SLOAD', kind='interp', line=1135)
W('11,2073', 0o11566, '', '', 'ZEROVEC', kind='operand', line=1136)
W('11,2074', 0o03505, '', '', 'ITCTR', kind='operand', line=1137)
W('11,2075', 0o77244, '', 'BPL', 'VLOAD', kind='interp', line=1138)
W('11,2076', 0o22101, '', '', 'INITVEL3', kind='operand', line=1139)
W('11,2077', 0o02665, '', '', 'R2VEC', kind='operand', line=1140)
W('11,2100', 0o03604, '', 'STORE', 'RTARG1', kind='interp', line=1141)
W('11,2101', 0o63345, 'INITVEL3', 'DLOAD', 'PDVL', '                              (PL 2D)', kind='interp', line=1142)
W('11,2102', 0o27735, '', '', 'MUEARTH', 'POSITIVE VALUE', kind='operand', line=1143)
W('11,2103', 0o02665, '', '', 'R2VEC', kind='operand', line=1144)
W('11,2104', 0o63256, '', 'UNIT', 'PDVL', '2D = UNIT(R2VEC)              (PL 8D)', kind='interp', line=1145)
W('11,2105', 0o02657, '', '', 'R1VEC', kind='operand', line=1146)
W('11,2106', 0o41456, '', 'UNIT', 'PUSH', '8D = UNIT(R1VEC)              (PL 14D)', kind='interp', line=1147)
W('11,2107', 0o57435, '', 'VXV', 'VCOMP', '-N = UNIT(R2VEC) X UNIT(R1VEC)', kind='interp', line=1148)
W('11,2110', 0o00003, '', '', '2D', kind='operand', line=1149)
W('11,2111', 0o77606, '', 'PUSH', '', '                              (PL 20D)', kind='interp', line=1150)
W('11,2112', 0o71350, '', 'LXA,1', 'DLOAD', kind='interp', line=1151)
W('11,2113', 0o03745, '', '', 'RTX1', kind='operand', line=1152)
W('11,2114', 0o00023, '', '', '18D', kind='operand', line=1153)
W('11,2115', 0o62040, '', 'BMN', 'INCR,1', kind='interp', line=1154)
# Page 489
W('11,2116', 0o22120, '', '', '+2', kind='operand', line=1156)
W('11,2117', 0o77767, '', 'DEC', '-8', kind='data', line=1157)
W('11,2120', 0o67310, '', 'INCR,1', 'SLOAD', kind='interp', line=1158)
W('11,2121', 0o00012, '', '', '10D', kind='operand', line=1159)
W('11,2122', 0o00047, '', '', 'X1', kind='operand', line=1160)
W('11,2123', 0o77230, '', 'BHIZ', 'VLOAD', '                      (PL 14D)', kind='interp', line=1161)
W('11,2124', 0o22126, '', '', '+2', kind='operand', line=1162)
W('11,2125', 0o41476, '', 'VCOMP', 'PUSH', '                      (PL 20 D)', kind='interp', line=1163)
W('11,2126', 0o77775, '', 'VLOAD', '', '                      (PL 14D)', kind='interp', line=1164)
W('11,2127', 0o50235, '', 'VXV', 'DOT', '                      (PL 2D)', kind='interp', line=1165)
W('11,2130', 0o71244, '', 'BPL', 'DLOAD', '                      (PL 0D)', kind='interp', line=1166)
W('11,2131', 0o22133, '', '', 'INITVEL4', kind='operand', line=1167)
W('11,2132', 0o41476, '', 'DCOMP', 'PUSH', '                      (PL 2D)', kind='interp', line=1168)
W('11,2133', 0o67154, 'INITVEL4', 'LXA,2', 'SXA,2', kind='interp', line=1169)
W('11,2134', 0o00000, '', '', '0D', kind='operand', line=1170)
W('11,2135', 0o02674, '', '', 'GEOMSGN', kind='operand', line=1171)

# SET INPUTS UP FOR LAMBERT

W('11,2136', 0o45150, '', 'LXA,1', 'CALL', kind='interp', line=1175)
W('11,2137', 0o03745, '', '', 'RTX1', kind='operand', line=1176)
# OPERATE THE LAMBERT CONIC ROUTINE (COASTFLT SUBROUTINE)

W('11,2140', 0o25224, '', '', 'LAMBERT', kind='operand', line=1179)

# ARRIVED AT SOLUTION IS GOOD ENOUGH ACCORDING TO SLIGHTLY WIDER BOUNDS.

W('11,2141', 0o77214, '', 'CLEAR', 'VLOAD', kind='interp', line=1183)
W('11,2142', 0o00675, '', '', 'GUESSW', kind='operand', line=1184)
W('11,2143', 0o02746, '', '', 'VVEC', kind='operand', line=1185)

# STORE CALCULATED INITIAL VELOCITY REQUIRED IN VIPRIME

W('11,2144', 0o17612, '', 'STODL', 'VIPRIME', 'INITIAL VELOCITY REQUIRED (+7)', kind='interp', line=1189)

# IF NUMIT IS ZERO, CONTINUE AT INITVELB, OTHERWISE
# SET UP INPUTS FOR ENCKE INTEGRATION (INTEGRVS).

W('11,2145', 0o02704, '', '', 'VTARGTAG', kind='operand', line=1194)
W('11,2146', 0o45030, '', 'BHIZ', 'CALL', kind='interp', line=1195)
W('11,2147', 0o22224, '', '', 'INITVEL7', kind='operand', line=1196)
W('11,2150', 0o27442, '', '', 'INTSTALL', kind='operand', line=1197)
W('11,2151', 0o43135, '', 'SLOAD', 'CLEAR', kind='interp', line=1198)
W('11,2152', 0o03747, '', '', 'RTX2', kind='operand', line=1199)
W('11,2153', 0o00263, '', '', 'MOONFLAG', kind='operand', line=1200)
W('11,2154', 0o43030, '', 'BHIZ', 'SET', kind='interp', line=1201)
W('11,2155', 0o22157, '', '', 'INITVEL5', kind='operand', line=1202)
W('11,2156', 0o00063, '', '', 'MOONFLAG', kind='operand', line=1203)
W('11,2157', 0o77775, 'INITVEL5', 'VLOAD', kind='interp', line=1204)
W('11,2160', 0o03570, '', '', 'RINIT', kind='operand', line=1205)
W('11,2161', 0o02657, '', 'STORE', 'R1VEC', kind='interp', line=1206)
# Page 490
W('11,2162', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=1208)
W('11,2163', 0o03612, '', '', 'VIPRIME', kind='operand', line=1209)
W('11,2164', 0o15543, '', 'STODL', 'VCV', kind='interp', line=1210)
W('11,2165', 0o03503, '', '', 'INTIME', kind='operand', line=1211)
W('11,2166', 0o01517, '', 'STORE', 'TET', kind='interp', line=1212)
W('11,2167', 0o43015, '', 'DAD', 'CLEAR', kind='interp', line=1213)
W('11,2170', 0o03423, '', '', 'DELLT4', kind='operand', line=1214)
W('11,2171', 0o01673, '', '', 'INTYPFLG', kind='operand', line=1215)
W('11,2172', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1216)
W('11,2173', 0o27135, '', '', 'INTEGRVS', kind='operand', line=1217)
W('11,2174', 0o77775, '', 'VLOAD', kind='interp', line=1218)
W('11,2175', 0o00025, '', '', 'VATT1', kind='operand', line=1219)
W('11,2176', 0o02705, '', 'STORE', 'VTARGET', kind='interp', line=1220)

# IF ITERATION COUNTER (ITCTR) EQ NO. ITERATIONS (NUMIT), CONTINUE AT
# INITVELC, OTHERWISE REITERATE LAMBERT AND ENCKE

W('11,2177', 0o63154, '', 'LXA,2', 'INCR,2', kind='interp', line=1225)
W('11,2200', 0o03504, '', '', 'ITCTR', kind='operand', line=1226)
W('11,2201', 0o00001, '', '', '1D', 'INCREMENT ITCTR', kind='operand', line=1227)
W('11,2202', 0o55134, '', 'SXA,2', 'XSU,2', kind='interp', line=1228)
W('11,2203', 0o03504, '', '', 'ITCTR', kind='operand', line=1229)
W('11,2204', 0o02703, '', '', 'VTARGTAG', kind='operand', line=1230)
W('11,2205', 0o46135, '', 'SLOAD', 'BHIZ', 'IF SP(MPAC) EQ 0, CONTINUE AT INITVELC', kind='interp', line=1231)
W('11,2206', 0o00050, '', '', 'X2', kind='operand', line=1232)
W('11,2207', 0o22221, '', '', 'INITVEL6', kind='operand', line=1233)

# OFFSET CONIC TARGET VECTGOR

W('11,2210', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=1237)
W('11,2211', 0o03604, '', '', 'RTARG1', kind='operand', line=1238)
W('11,2212', 0o00017, '', '', 'RATT1', kind='operand', line=1239)
W('11,2213', 0o77655, '', 'VAD', kind='interp', line=1240)
W('11,2214', 0o02665, '', '', 'R2VEC', kind='operand', line=1241)
W('11,2215', 0o16665, '', 'STODL', 'R2VEC', kind='interp', line=1242)
W('11,2216', 0o03630, '', '', 'COZY4', kind='operand', line=1243)
W('11,2217', 0o77650, '', 'GOTO', kind='interp', line=1244)
W('11,2220', 0o22056, '', '', 'INITVEL2', 'CONTINUE ITERATING AT INITVEL2', kind='operand', line=1245)

# COMPUTE THE DELTA VELOCITY

W('11,2221', 0o77775, 'INITVEL6', 'VLOAD', kind='interp', line=1249)
W('11,2222', 0o02665, '', '', 'R2VEC', kind='operand', line=1250)
W('11,2223', 0o03604, '', 'STORE', 'RTARG1', kind='interp', line=1251)
W('11,2224', 0o52375, 'INITVEL7', 'VLOAD', 'VSU', kind='interp', line=1252)
W('11,2225', 0o03612, '', '', 'VIPRIME', kind='operand', line=1253)
W('11,2226', 0o03576, '', '', 'VINIT', kind='operand', line=1254)
W('11,2227', 0o27646, '', 'STOVL', 'DELVEET3', 'DELVEET3 = VIPRIME-VINIT (+7)', kind='interp', line=1255)
W('11,2230', 0o02705, '', '', 'VTARGET', kind='operand', line=1256)
W('11,2231', 0o03620, '', 'STORE', 'VTPRIME', kind='interp', line=1257)
W('11,2232', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=1258)
W('11,2233', 0o03747, '', '', 'RTX2', kind='operand', line=1259)
# Page 491
W('11,2234', 0o22251, '', '', 'INITVELX', kind='operand', line=1261)
W('11,2235', 0o70575, '', 'VLOAD', 'VSR2', kind='interp', line=1262)
W('11,2236', 0o03620, '', '', 'VTPRIME', kind='operand', line=1263)
W('11,2237', 0o27620, '', 'STOVL', 'VTPRIME', kind='interp', line=1264)
W('11,2240', 0o03612, '', '', 'VIPRIME', kind='operand', line=1265)
W('11,2241', 0o77742, '', 'VSR2', kind='interp', line=1266)
W('11,2242', 0o27612, '', 'STOVL', 'VIPRIME', kind='interp', line=1267)
W('11,2243', 0o03604, '', '', 'RTARG1', kind='operand', line=1268)
W('11,2244', 0o77742, '', 'VSR2', kind='interp', line=1269)
W('11,2245', 0o27604, '', 'STOVL', 'RTARG1', kind='interp', line=1270)
W('11,2246', 0o03646, '', '', 'DELVEET3', kind='operand', line=1271)
W('11,2247', 0o77742, '', 'VSR2', kind='interp', line=1272)
W('11,2250', 0o03646, '', 'STORE', 'DELVEET3', kind='interp', line=1273)
W('11,2251', 0o77201, 'INITVELX', 'SETPD', 'VLOAD', kind='interp', line=1274)
W('11,2252', 0o00001, '', '', '0D', kind='operand', line=1275)
W('11,2253', 0o03604, '', '', 'RTARG1', kind='operand', line=1276)
W('11,2254', 0o37415, '', 'STCALL', 'RTARG', kind='interp', line=1277)
W('11,2255', 0o01340, '', '', 'NORMEX', kind='operand', line=1278)

# ***** END OF INITVEL ROUTINE *****

# Page 492
# ***** MIDGIM *****
# MOD NO. 0, BY WILLMAN, SUBROUTINE RENDGUID, LOG P34-P35, P74-P75
# REVISION 03, 17 FEB 67
#
# IF THE ACTIVE VEHICLE IS DOING THE COMPUTATION, MIDGIM COMPUTES
# THE POSITIVE MIDDLE GIMBAL ANGLE OF THE ACTIVE VEHICLE TO THE INPUT
# DELTA VELOCITY VECTOR (0D IN PUSY LIST), OTHERWISE
# MIDGIM CONVERTS THE INPUT DELTA VELOCITY VECTOR FROM INERTIAL COORDIN-
# ATES TO LOCAL VERTICAL COORDINATES OF THE ACTIVE VEHICLE.
#
# ** INPUTS **
# NAME     MEANING                                            UNITS/SCALING/MODE
# AVFLAG   INT FLAG -- 0 IS CSM ACTIVE, 1 IS LEM ACTIVE       BIT
# COMPUTER INT FLAG -- 0 IS LEM COMPUTER, 1 IS CSM COMPUTER   BIT
# RINIT    ACTIVE VEHICLE RADIUS VECTOR                       METERS/CSEC (+7) VT
# VINIT    ACTIVE VEHICLE VELOCITY VECTOR                     METERS/CSEC (+7) VT
# 0D(PL)   ACTIVE VEHICLE DELTA VELOCITY VECTOR               METERS/CSEC (+7) VT
#
# ** OUTPUTS **
# NAME     MEANING                                            UNITS/SCALING/MODE
# +MGA     + MIDDLE GIMBAL ANGLE                              REVOLUTIONS (+0) DP
# DELVLVC  DELTA VELOCITY VECTOR IN LV COORD.                 METERS/CSEC (+7) VT
# MGLVFLAG INT FLAG: 0 IS +MGA COMUTED, 1 IS DELVLVC COMP.    BIT
#
# ** CALLING SEQUENCE **
# L       CALL
# L+1             MIDGIM
# L+2     (RETURN -- ALWAYS)
#
# ** NO SUBROUTINES CALLED **
#
# ** DEBRIS -- ERASABLE TEMPORARY USAGE **
# A,Q,L, PUSH LIST, MPAC.
#
# ** ALARMS -- NONE **

# Page 493
# MIDDLE GIMBAL ANGLE COMPUTATION
#   SETLOC MIDDGIM
#   BANK

#   COUNT* $$/MIDG

W('04,2645', 0o20000, 'HALFREV', '2DEC', '1 B-1', kind='data', line=1326)
W('04,2646', 0o00000, kind='data', line=1326)

W('04,2647', 0o43014, 'MIDGIM', 'BON', 'BOFF', kind='interp', line=1328)
W('04,2650', 0o01312, '', '', 'AVFLAG', kind='operand', line=1329)
W('04,2651', 0o10667, '', '', 'MIDGIM1', kind='operand', line=1330)
W('04,2652', 0o02747, '', '', 'COMPUTER', kind='operand', line=1331)
W('04,2653', 0o10672, '', '', 'GET.LVC', kind='operand', line=1332)

# COMPUTE +MGA IF AVFLAG AND COMPUTER HAVE OPPOSITE VALUES.

W('04,2654', 0o53575, 'GET+MGA', 'VLOAD', 'UNIT', '(PL 0D) V (+7) TO MPAC UNITIZE UV (+1)', kind='interp', line=1336)
W('04,2655', 0o72441, '', 'DOT', 'SL1', 'DOT UV WITH Y(STABLE MEMBER) AND RESCALE', kind='interp', line=1337)
W('04,2656', 0o01744, '', '', 'REFSMMAT +6', 'FROM +2 TO +1 FOR ASIN ROUTINE', kind='operand', line=1338)
W('04,2657', 0o51136, '', 'ARCSIN', 'BPL', kind='interp', line=1339)
W('04,2660', 0o10664, '', '', 'SETMGA', kind='operand', line=1340)
W('04,2661', 0o43215, '', 'DAD', 'DAD', 'CONVERT -MGA TO +MGA BY', kind='interp', line=1341)
W('04,2662', 0o10646, '', '', 'HALFREV', 'ADDING ONE REVOLUTION', kind='operand', line=1342)
W('04,2663', 0o10646, '', '', 'HALFREV', kind='operand', line=1343)
W('04,2664', 0o03626, 'SETMGA', 'STORE', '+MGA', kind='interp', line=1344)
W('04,2665', 0o43414, '', 'CLR', 'RVQ', 'CLEAR MGLVFLAG TO INDICATE +MGA CALC', kind='interp', line=1345)
W('04,2666', 0o02675, '', '', 'MGLVFLAG', 'AND EXIT', kind='operand', line=1346)

W('04,2667', 0o77614, 'MIDGIM1', 'BOFF', kind='interp', line=1348)
W('04,2670', 0o02747, '', '', 'COMPUTER', kind='operand', line=1349)
W('04,2671', 0o10654, '', '', 'GET+MGA', kind='operand', line=1350)

# COMPUTE DELVLVC IF AVFLAG AND COMPUTER HAVE SAME VALUES

W('04,2672', 0o53575, 'GET.LVC', 'VLOAD', 'UNIT', '(PL 6D) R (+29) IN MPAC UNITZE UR', kind='interp', line=1354)
W('04,2673', 0o03570, '', '', 'RINIT', kind='operand', line=1355)
W('04,2674', 0o77676, '', 'VCOMP', '', 'U(-R)', kind='interp', line=1356)
W('04,2675', 0o00023, '', 'STORE', '18D', 'U(-R) TO 18D', kind='interp', line=1357)
W('04,2676', 0o53435, '', 'VXV', 'UNIT', 'U(-R)*V EQ V*U(R), U(V*R)', kind='interp', line=1358)
W('04,2677', 0o03576, '', '', 'VINIT', kind='operand', line=1359)
W('04,2700', 0o00015, '', 'STORE', '12D', 'U(V*R) TO 12D', kind='interp', line=1360)
W('04,2701', 0o53435, '', 'VXV', 'UNIT', 'U(V*R)*U(-R), U((V*R)*(-R))', kind='interp', line=1361)
W('04,2702', 0o00023, '', '', '18D', kind='operand', line=1362)
W('04,2703', 0o24007, '', 'STOVL', '6D', 'TRANSFORMATION MATRIX IS IN 6D (+1)', kind='interp', line=1363)
W('04,2704', 0o00001, '', '', '0D', 'DELTA V (+7) IN 0D', kind='operand', line=1364)
W('04,2705', 0o76521, '', 'MXV', 'VSL1', 'CONVERT FROM INER COOR TO LV COOR (+8)', kind='interp', line=1365)
W('04,2706', 0o00007, '', '', '6D', 'AND SCALE +7 IN MPAC', kind='operand', line=1366)
W('04,2707', 0o03405, '', 'STORE', 'DELVLVC', 'STORE IN DELVLVC (+7(', kind='interp', line=1367)
W('04,2710', 0o43414, '', 'SET', 'RVQ', 'SET MGLVFLAG TO INDICATE LVC CALC', kind='interp', line=1368)
W('04,2711', 0o02475, '', '', 'MGLVFLAG', 'AND EXIT', kind='operand', line=1369)

# ***** END OF MIDGIM ROUTINE *****

# Page 494
W('04,2712', 0o77160, 'SELECTMU', 'AXC,1', 'AXT,2', kind='interp', line=1374)
W('04,2713', 0o00002, '', '', '2D', kind='operand', line=1375)
W('04,2714', 0o00000, '', '', '0D', kind='operand', line=1376)
W('04,2715', 0o77614, '', 'BOFF', kind='interp', line=1377)
W('04,2716', 0o04343, '', '', 'CMOONFLG', kind='operand', line=1378)
W('04,2717', 0o10723, '', '', 'SETMUER', kind='operand', line=1379)
W('04,2720', 0o77160, '', 'AXC,1', 'AXT,2', kind='interp', line=1380)
W('04,2721', 0o00012, '', '', '10D', kind='operand', line=1381)
W('04,2722', 0o00002, '', '', '2D', kind='operand', line=1382)
W('04,2723', 0o66143, 'SETMUER', 'DLOAD*', 'SXA,1', kind='interp', line=1383)
W('04,2724', 0o11744, '', '', 'MUTABLE +4,1', kind='operand', line=1384)
W('04,2725', 0o03745, '', '', 'RTX1', kind='operand', line=1385)
W('04,2726', 0o23752, '', 'STODL*', 'RTSR1/MU', kind='interp', line=1386)
W('04,2727', 0o11736, '', '', 'MUTABLE -2,1', kind='operand', line=1387)
W('04,2730', 0o54214, '', 'BOFF', 'SR', kind='interp', line=1388)
W('04,2731', 0o04343, '', '', 'CMOONFLG', kind='operand', line=1389)
W('04,2732', 0o10734, '', '', 'RTRNMU', kind='operand', line=1390)
W('04,2733', 0o20607, '', '', '6D', kind='operand', line=1391)
W('04,2734', 0o03750, 'RTRNMU', 'STORE', 'RTMU', kind='interp', line=1392)
W('04,2735', 0o43134, '', 'SXA,2', 'CLEAR', kind='interp', line=1393)
W('04,2736', 0o03746, '', '', 'RTX2', kind='operand', line=1394)
W('04,2737', 0o01271, '', '', 'FINALFLG', kind='operand', line=1395)
W('04,2740', 0o77650, '', 'GOTO', kind='interp', line=1396)
W('04,2741', 0o73002, '', '', 'VN1645', kind='operand', line=1397)

# Page 495
# ***** PERIAPO *****
# MOD NO -1       LOG SECTION - P34-P35, P74-P75
# MOD BY WHITE.P  DATE  18JAN68
#
# FUNCTIONAL DESCRIPTION
# THIS SUBROUTINE COMPUTES THE TWO BODY APOCENTER AND PERICENTER
# ALTITUDES GIVEN THE POSITION AND VELOCITY VECTORS FOR A POINT ON
# THE TRAJECTORY AND THE PRIMARY BODY.
#
# SETRAD IS CALLED TO DETERMINE THE RADIUS OF THE PRIMARY BODY.
#
# APSIDES IS CALLED TO SOVE FOR THE TWO BODY RADII OF APOCENTER AND
# PERICENTER AND THE ECCENTRICITY OF THE TRAJECTORY.
#
# CALLING SEQUENCE
# L       CALL
# L+1             PERIAPO
# L+2     (RETURN -- ALWAYS)
#
# INPUT
# (1)     RVEC    POSITION VECTOR IN METERS
# SCALE FACTOR -- EARTH +29, MOON +27
# (2)     VVEC    VELOCITY VECTOR IN METERS/CENTISECOND
# SCALE FACTOR -- EARTH +7, MOON +5
# (3)     X1      PRIMARY BODY INDICATOR
# EARTH -2, MOON -10
#
# OUTPUT
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
# SETRAD
# Page 496
# APSIDES

#   SETLOC APOPERI
#   BANK

#   COUNT* $$/PERAP

W('22,3151', 0o00302, 'RPAD', '2DEC', '6373338 B-29', 'STANDARD RADIUS OF PAD 37-B.', kind='data', line=1452)
W('22,3152', 0o17755, kind='data', line=1452)
# = 20 909 901.57 FT

W('22,3153', 0o53754, 'PERIAPO1', 'LXA,2', 'VSR*', kind='interp', line=1455)
W('22,3154', 0o03746, '', '', 'RTX2', kind='operand', line=1456)
W('22,3155', 0o57176, '', '', '0,2', kind='operand', line=1457)
W('22,3156', 0o26746, '', 'STOVL', 'VVEC', kind='interp', line=1458)
W('22,3157', 0o53750, '', 'LXA,1', 'VSR*', kind='interp', line=1459)
W('22,3160', 0o03745, '', '', 'RTX1', kind='operand', line=1460)
W('22,3161', 0o57176, '', '', '0,2', kind='operand', line=1461)
W('22,3162', 0o02657, '', 'STORE', 'RVEC', kind='interp', line=1462)
W('22,3163', 0o45020, 'PERIAPO', 'STQ', 'CALL', kind='interp', line=1463)
W('22,3164', 0o01340, '', '', 'NORMEX', kind='operand', line=1464)
W('22,3165', 0o45201, '', '', 'SETRAD', kind='operand', line=1465)
W('22,3166', 0o37456, '', 'STCALL', 'XXXALT', kind='interp', line=1466)
W('22,3167', 0o25703, '', '', 'APSIDES', kind='operand', line=1467)
W('22,3170', 0o41401, '', 'SETPD', 'PUSH', '2D = APOCENTER RADIUS         B29 OR B27', kind='interp', line=1468)
W('22,3171', 0o00003, '', '', '2D', kind='operand', line=1469)
W('22,3172', 0o65225, '', 'DSU', 'PDDL', '4D = APOGEE ALTITUDE          B29 OR B27', kind='interp', line=1470)
W('22,3173', 0o03456, '', '', 'XXXALT', kind='operand', line=1471)
W('22,3174', 0o00001, '', '', '0D', kind='operand', line=1472)
W('22,3175', 0o45206, '', 'PUSH', 'DSU', '6D = PERICENTER RADIUS        B29 OR B27', kind='interp', line=1473)
W('22,3176', 0o03456, '', '', 'XXXALT', kind='operand', line=1474)
W('22,3177', 0o52006, '', 'PUSH', 'GOTO', '8D = PERIGEE ALTITUDE         B29 OR B27', kind='interp', line=1475)
W('22,3200', 0o01340, '', '', 'NORMEX', kind='operand', line=1476)
# Page 497
# SETRAD
W('22,3201', 0o41545, 'SETRAD', 'DLOAD', 'PUSH', kind='interp', line=1479)
W('22,3202', 0o05152, '', '', 'RPAD', kind='operand', line=1480)
W('22,3203', 0o63130, '', 'SXA,1', 'INCR,2', kind='interp', line=1481)
W('22,3204', 0o00047, '', '', 'X2', kind='operand', line=1482)
W('22,3205', 0o00002, '', '', '2D', kind='operand', line=1483)
W('22,3206', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=1484)
W('22,3207', 0o00050, '', '', 'X2', kind='operand', line=1485)
W('22,3210', 0o45214, '', '', 'SETRADX', kind='operand', line=1486)
W('22,3211', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=1487)
W('22,3212', 0o02026, '', '', 'RLS', kind='operand', line=1488)
W('22,3213', 0o77725, '', 'PDDL', kind='interp', line=1489)
W('22,3214', 0o43545, 'SETRADX', 'DLOAD', 'RVQ', kind='interp', line=1490)

# Page 498
# PRECSET
W('22,3215', 0o77620, 'PRECSET', 'STQ', kind='interp', line=1494)
W('22,3216', 0o01340, '', '', 'NORMEX', kind='operand', line=1495)
W('22,3217', 0o36635, '', 'STCALL', 'TDEC2', kind='interp', line=1496)
W('22,3220', 0o27105, '', '', 'LEMPREC', kind='operand', line=1497)
W('22,3221', 0o77624, '', 'CALL', kind='interp', line=1498)
W('22,3222', 0o45233, '', '', 'LEMSTORE', kind='operand', line=1499)
W('22,3223', 0o77745, '', 'DLOAD', kind='interp', line=1500)
W('22,3224', 0o02635, '', '', 'TDEC2', kind='operand', line=1501)
W('22,3225', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1502)
W('22,3226', 0o27071, '', '', 'CSMPREC', kind='operand', line=1503)
W('22,3227', 0o77624, '', 'CALL', kind='interp', line=1504)
W('22,3230', 0o45243, '', '', 'CSMSTORE', kind='operand', line=1505)
W('22,3231', 0o77650, '', 'GOTO', kind='interp', line=1506)
W('22,3232', 0o01340, '', '', 'NORMEX', kind='operand', line=1507)
W('22,3233', 0o43175, 'LEMSTORE', 'VLOAD', 'BOFF', kind='interp', line=1508)
W('22,3234', 0o00001, '', '', 'RATT', kind='operand', line=1509)
W('22,3235', 0o01352, '', '', 'AVFLAG', kind='operand', line=1510)
W('22,3236', 0o45247, '', '', 'PASSIVE', kind='operand', line=1511)
W('22,3237', 0o27540, 'ACTIVE', 'STOVL', 'RACT3', kind='interp', line=1512)
W('22,3240', 0o00007, '', '', 'VATT', kind='operand', line=1513)
W('22,3241', 0o03546, '', 'STORE', 'VACT3', kind='interp', line=1514)
W('22,3242', 0o77616, '', 'RVQ', kind='interp', line=1515)
W('22,3243', 0o43175, 'CSMSTORE', 'VLOAD', 'BOFF', kind='interp', line=1516)
W('22,3244', 0o00001, '', '', 'RATT', kind='operand', line=1517)
W('22,3245', 0o01352, '', '', 'AVFLAG', kind='operand', line=1518)
W('22,3246', 0o45237, '', '', 'ACTIVE', kind='operand', line=1519)
W('22,3247', 0o27554, 'PASSIVE', 'STOVL', 'RPASS3', kind='interp', line=1520)
W('22,3250', 0o00007, '', '', 'VATT', kind='operand', line=1521)
W('22,3251', 0o03562, '', 'STORE', 'VPASS3', kind='interp', line=1522)
W('22,3252', 0o77616, '', 'RVQ', kind='interp', line=1523)

# Page 499
# VECSHIFT
W('22,3253', 0o53754, 'VECSHIFT', 'LXA,2', 'VSR*', kind='interp', line=1527)
W('22,3254', 0o03746, '', '', 'RTX2', kind='operand', line=1528)
W('22,3255', 0o57176, '', '', '0,2', kind='operand', line=1529)
W('22,3256', 0o63350, '', 'LXA,1', 'PDVL', kind='interp', line=1530)
W('22,3257', 0o03745, '', '', 'RTX1', kind='operand', line=1531)
W('22,3260', 0o63257, '', 'VSR*', 'PDVL', kind='interp', line=1532)
W('22,3261', 0o57176, '', '', '0,2', kind='operand', line=1533)
W('22,3262', 0o77616, '', 'RVQ', kind='interp', line=1534)

# Page 500
# SHIFTR1
W('22,3263', 0o53754, 'SHIFTR1', 'LXA,2', 'SL*', kind='interp', line=1538)
W('22,3264', 0o03746, '', '', 'RTX2', kind='operand', line=1539)
W('22,3265', 0o57576, '', '', '0,2', kind='operand', line=1540)
W('22,3266', 0o77616, '', 'RVQ', kind='interp', line=1541)

# Page 501
# PROGRAM DESCRIPTION
#
# SUBROUTINE NAME       R36     OUT-OF-PLANE RENDEZVOUS ROUTINE
# MOD NO. 2             DATE 2 JANUARY 1969
# MOD BY A.W.BANCROFT   LOG SECTION EXTENDED VERBS
#
# FUNCTIONAL DESCRIPTION
#
# TO DISPLAY AT ASTRONAUT REQUEST LGC CALCULATED RENDEZVOUS
# OUT-OF-PLANE PARAMETERS (Y, YDOT, PSI).  (REQUESTED BY DSKY).
#
# CALLING SEQUENCE
# ASTRONAUT REQUEST THROUGH DSKY V 90 E
#
# SUBROUTINES CALLED
# EXDSPRET
# GOMARKF
# CSMPREC
# LEMPREC
# SGNAGREE
# LOADTIME
#
# NORMAL EXIT MODES
# ASTRONAUT REQUEST THROUGH DSKY TO TERMINATE PROGRAM V 34 E
#
# ALARM OR ABORT EXIT MODES
# NONE
#
# OUTPUT
# DECIMAL DISPLAY OF TIME, Y, YDOT AND PSI
#
# DISPLAYED VALUES Y, YDOT, AND PSI, ARE STORED IN ERASABLE
# REGISTERS RANGE, RRATE, AND RTHETA RESPECTIVELY.
#
# ERASABLE INITIALIZATION REQUIRED
# CSM AND LEM STATE VECTORS
#
# DEBRIS
# CENTRALS A,Q,L
# OTHER:  THOSE USED BY THE ABOVE LISTED SUBROUTINES

#   BANK 20
#   SETLOC R36CM
#   BANK
# Page 502
#   EBANK= RPASS36

#   SBANK= R36A
#   COUNT* $$/R36

W('20,2164', 0o35016, 'R36', 'CAF', 'TWO', line=1594)
W('20,2165', 0o55051, '', 'TS', 'OPTIONX', line=1595)
W('20,2166', 0o35017, '', 'CAF', 'ONE', line=1596)
W('20,2167', 0o55052, '', 'TS', 'OPTIONX +1', line=1597)
W('20,2170', 0o32200, '', 'CAF', 'OPTION36', 'V 04 N 12', line=1598)
W('20,2171', 0o04662, '', 'TC', 'BANKCALL', line=1599)
W('20,2172', 0o20561, '', 'CADR', 'GOXDSPF', kind='data', line=1600)
W('20,2173', 0o05534, '', 'TC', 'ENDEXT', 'TERMINATE', line=1601)
W('20,2174', 0o02176, '', 'TC', '+2', 'PROCEED', line=1602)
W('20,2175', 0o02170, '', 'TC', '-5', 'R2 LOADED VIA DSKY', line=1603)
W('20,2176', 0o04701, '', 'TC', 'POSTJUMP', line=1604)
W('20,2177', 0o63727, '', 'CADR', 'R36A', kind='data', line=1605)

W('20,2200', 0o01014, 'OPTION36', 'VN', '0412', kind='data', line=1607)

#   SETLOC R36LM
#   BANK

W('41,3727', 0o22007, 'R36A', 'ZL', line=1612)
W('41,3730', 0o35021, '', 'CAF', 'ZERO', 'SET TIME OF EVENT TO ZERO FOR FIRST', line=1613)
W('41,3731', 0o53052, '', 'DXCH', 'DSPTEMX', 'DISPLAY', line=1614)
W('41,3732', 0o23742, '', 'LXCH', 'OPTIONY', 'SAVE VEH. OPTION', line=1615)
W('41,3733', 0o33775, 'R36P3', 'CAF', 'V06N16N', line=1616)
W('41,3734', 0o04662, '', 'TC', 'BANKCALL', line=1617)
W('41,3735', 0o20561, '', 'CADR', 'GOMARKF', kind='data', line=1618)
W('41,3736', 0o15534, '', 'TCF', 'ENDEXT', 'TERMINATE', line=1619)
W('41,3737', 0o13741, '', 'TCF', '+2', 'PROCEED', line=1620)
W('41,3740', 0o13733, '', 'TCF', '-5', 'RECYCLE FOR ASTRONAUT INPUT TIME', line=1621)
W('41,3741', 0o53052, '', 'DXCH', 'DSPTEMX', line=1622)
W('41,3742', 0o00006, '', 'EXTEND', line=1623)
W('41,3743', 0o13764, '', 'BZF', 'LREGCHK', 'A-REG ZERO GOTO CHECK L-REG FOR ZERO', line=1624)
W('41,3744', 0o52155, 'ASTROTIM', 'DXCH', 'MPAC', 'A-REG NON-ZERO, TIME = ASTRO INPUT TIME', line=1625)
W('41,3745', 0o06006, '', 'TC', 'INTPRET', line=1626)
W('41,3746', 0o52034, '', 'RTB', 'GOTO', kind='interp', line=1627)
W('41,3747', 0o45716, '', '', 'DPMODE', kind='operand', line=1628)
W('41,3750', 0o65521, '', '', 'R36INT', kind='operand', line=1629)

#   SETLOC R36LM1
#   BANK

W('42,3521', 0o00041, 'R36INT', 'STORE', 'TDEC1', kind='interp', line=1634)
W('42,3522', 0o70535, '', 'SLOAD', 'SR1', kind='interp', line=1635)
W('42,3523', 0o02343, '', '', 'OPTIONY', kind='operand', line=1636)
W('42,3524', 0o45030, '', 'BHIZ', 'CALL', kind='interp', line=1637)
W('42,3525', 0o65531, '', '', 'R36PROG2', 'FOR CSM DISPLAY', kind='operand', line=1638)
# Page 503
W('42,3526', 0o27071, '', '', 'THISPREC', 'FOR LEM DISPLAY', kind='operand', line=1640)
W('42,3527', 0o77650, '', 'GOTO', kind='interp', line=1641)
W('42,3530', 0o65533, '', '', 'R36PROG3', kind='operand', line=1642)
W('42,3531', 0o77624, 'R36PROG2', 'CALL', kind='interp', line=1643)
W('42,3532', 0o27105, '', '', 'OTHPREC', kind='operand', line=1644)
W('42,3533', 0o63375, 'R36PROG3', 'VLOAD', 'PDVL', kind='interp', line=1645)
W('42,3534', 0o00007, '', '', 'VATT', kind='operand', line=1646)
W('42,3535', 0o00001, '', '', 'RATT', '_', kind='operand', line=1647)
W('42,3536', 0o02327, '', 'STORE', 'RPASS36', 'R', kind='interp', line=1648)
W('42,3537', 0o63256, '', 'UNIT', 'PDVL', ' P', kind='interp', line=1649)
W('42,3540', 0o53435, '', 'VXV', 'UNIT', '-', kind='interp', line=1650)
W('42,3541', 0o77626, '', 'STADR', kind='interp', line=1651)
W('42,3542', 0o61442, '', 'STODL', 'UNP36', 'U', kind='interp', line=1652)
W('42,3543', 0o00015, '', '', 'TAT', kind='operand', line=1653)
W('42,3544', 0o00041, '', 'STORE', 'TDEC1', kind='interp', line=1654)
W('42,3545', 0o70535, '', 'SLOAD', 'SR1', kind='interp', line=1655)
W('42,3546', 0o02343, '', '', 'OPTIONY', kind='operand', line=1656)
W('42,3547', 0o45030, '', 'BHIZ', 'CALL', kind='interp', line=1657)
W('42,3550', 0o65554, '', '', 'R36PROG4', 'FOR CSM DISPLAY', kind='operand', line=1658)
W('42,3551', 0o27105, '', '', 'OTHPREC', 'FOR LEM DISPLAY', kind='operand', line=1659)
W('42,3552', 0o77650, '', 'GOTO', kind='interp', line=1660)
W('42,3553', 0o65556, '', '', 'R36PROG5', kind='operand', line=1661)
W('42,3554', 0o77624, 'R36PROG4', 'CALL', kind='interp', line=1662)
W('42,3555', 0o27071, '', '', 'THISPREC', kind='operand', line=1663)
W('42,3556', 0o63375, 'R36PROG5', 'VLOAD', 'PDVL', '                      _', kind='interp', line=1664)
W('42,3557', 0o00007, '', '', 'VATT', 'VELOCITY VECTOR       V       00D', kind='operand', line=1665)
W('42,3560', 0o00001, '', '', 'RATT', '                       A', kind='operand', line=1666)
W('42,3561', 0o77725, '', 'PDDL', kind='interp', line=1667)
W('42,3562', 0o00015, '', '', 'TAT', 'SAVE TIME IN LOCATION 30D FOR REDISPLAY', kind='operand', line=1668)
W('42,3563', 0o24037, '', 'STOVL', '30D', '                      _', kind='interp', line=1669)
W('42,3564', 0o41406, '', 'PUSH', 'PUSH', 'POSITION VECTOR       R   IN  06D AND 12D', kind='interp', line=1670)
W('42,3565', 0o63245, '', 'BVSU', 'PDVL', '                      _A  _', kind='interp', line=1671)
W('42,3566', 0o02327, '', '', 'RPASS36', 'LINE OF SIGHT VECTOR  R - R   12D', kind='operand', line=1672)
W('42,3567', 0o72441, '', 'DOT', 'SL1', '                       P   A', kind='interp', line=1673)
W('42,3570', 0o02335, '', '', 'UNP36', '    _   _', kind='operand', line=1674)
W('42,3571', 0o26321, '', 'STOVL', 'RANGE', 'Y = U . R', kind='interp', line=1675)
W('42,3572', 0o00001, '', '', '00D', '         A', kind='operand', line=1676)
W('42,3573', 0o72441, '', 'DOT', 'SL1', kind='interp', line=1677)
W('42,3574', 0o02335, '', '', 'UNP36', '.   _   _', kind='operand', line=1678)
W('42,3575', 0o26323, '', 'STOVL', 'RRATE', 'Y = U . V', kind='interp', line=1679)
W('42,3576', 0o00007, '', '', '06D', '_        A', kind='operand', line=1680)
W('42,3577', 0o41456, '', 'UNIT', 'PUSH', 'U  = UNIT ( R  )              18D', kind='interp', line=1681)
W('42,3600', 0o47235, '', 'VXV', 'VXV', ' RA          A', kind='interp', line=1682)
W('42,3601', 0o00001, '', '', '00D', ' _    _     _     _', kind='operand', line=1683)
W('42,3602', 0o00023, '', '', '18D', '(U  X V ) X U   = U', kind='operand', line=1684)
W('42,3603', 0o53552, '', 'VSL2', 'UNIT', '  RA   A     RA    A', kind='interp', line=1685)
W('42,3604', 0o52056, '', 'UNIT', 'GOTO', kind='interp', line=1686)
W('42,3605', 0o61600, '', '', 'R36B', kind='operand', line=1687)

#   SETLOC R36CM1
# Page 504
#   BANK

W('40,3600', 0o24001, 'R36B', 'STOVL', '00D', 'UNIT HORIZONTAL IN FORWARD DIR. 00D', kind='interp', line=1693)
W('40,3601', 0o00023, '', '', '18D', kind='operand', line=1694)
W('40,3602', 0o74241, '', 'DOT', 'VXSC', '_', kind='interp', line=1695)
W('40,3603', 0o00015, '', '', '12D', 'U', kind='operand', line=1696)
W('40,3604', 0o77752, '', 'VSL2', '', ' L', kind='interp', line=1697)
W('40,3605', 0o53445, '', 'BVSU', 'UNIT', kind='interp', line=1698)
W('40,3606', 0o77656, '', 'UNIT', kind='interp', line=1699)
W('40,3607', 0o50206, '', 'PUSH', 'DOT', 'LOS PROJECTED INTO HORIZONTAL  12D', kind='interp', line=1700)
W('40,3610', 0o00001, '', '', '00D', 'PLANE', kind='operand', line=1701)
W('40,3611', 0o65552, '', 'SL1', 'ARCCOS', '             _   _', kind='interp', line=1702)
W('40,3612', 0o26325, '', 'STOVL', 'RTHETA', 'PSI = ARCCOS(U . U )', kind='interp', line=1703)
W('40,3613', 0o50235, '', 'VXV', 'DOT', '              A   L', kind='interp', line=1704)
W('40,3614', 0o00001, '', '', '00D', kind='operand', line=1705)
W('40,3615', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=1706)
W('40,3616', 0o63751, '', '', 'R36TAG2', kind='operand', line=1707)
W('40,3617', 0o15343, '', '', 'DPPOSMAX', kind='operand', line=1708)
W('40,3620', 0o77625, '', 'DSU', kind='interp', line=1709)
W('40,3621', 0o02325, '', '', 'RTHETA', kind='operand', line=1710)
W('40,3622', 0o36325, '', 'STCALL', 'RTHETA', kind='interp', line=1711)
W('40,3623', 0o63751, '', '', 'R36TAG2', kind='operand', line=1712)

#   SETLOC R36LM
#   BANK

W('41,3751', 0o47145, 'R36TAG2', 'DLOAD', 'RTB', kind='interp', line=1717)
W('41,3752', 0o00037, '', '', '30D', kind='operand', line=1718)
W('41,3753', 0o45544, '', '', 'SGNAGREE', kind='operand', line=1719)
W('41,3754', 0o01052, '', 'STORE', 'DSPTEMX', kind='interp', line=1720)
W('41,3755', 0o77776, '', 'EXIT', kind='interp', line=1721)
W('41,3756', 0o33776, '', 'CAF', 'V06N90N', 'DISPLAY Y, YDOT, AND PSI.', line=1722)
W('41,3757', 0o04662, '', 'TC', 'BANKCALL', line=1723)
W('41,3760', 0o20561, '', 'CADR', 'GOMARKF', kind='data', line=1724)
W('41,3761', 0o15534, '', 'TCF', 'ENDEXT', 'TERMINATE', line=1725)
W('41,3762', 0o15534, '', 'TCF', 'ENDEXT', 'PROCEED, END OF PROGRAM', line=1726)
W('41,3763', 0o13733, '', 'TCF', 'R36P3', 'REDISPLAY OUTPUT', line=1727)
W('41,3764', 0o56001, 'LREGCHK', 'XCH', 'L', line=1728)
W('41,3765', 0o00006, '', 'EXTEND', line=1729)
W('41,3766', 0o13771, '', 'BZF', 'ENTTIM2', 'L-REG ZERO, SET TIME = PRESENT TIME', line=1730)
W('41,3767', 0o56001, '', 'XCH', 'L', 'L-REG NON ZERO, TIME = ASTRO INPUT TIME', line=1731)
W('41,3770', 0o13744, '', 'TCF', 'ASTROTIM', line=1732)
W('41,3771', 0o06006, 'ENTTIM2', 'TC', 'INTPRET', line=1733)
W('41,3772', 0o52034, '', 'RTB', 'GOTO', kind='interp', line=1734)
W('41,3773', 0o45510, '', '', 'LOADTIME', kind='operand', line=1735)
W('41,3774', 0o65521, '', '', 'R36INT', kind='operand', line=1736)
W('41,3775', 0o01420, 'V06N16N', 'VN', '00616', kind='data', line=1737)
W('41,3776', 0o01532, 'V06N90N', 'VN', '00690', kind='data', line=1738)
#   SBANK= LOWSUPER
