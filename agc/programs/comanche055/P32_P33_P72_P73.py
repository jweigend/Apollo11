"""P32-P33_P72-P73.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P32-P33_P72-P73.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 649-683 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P32_P33_P72_P73', 'P32-P33_P72-P73.agc', 'Comanche055', pages='649-683')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P32-P33_P72-P73.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        649-683
# Mod history:  2009-05-09 RSB  Adapted from the Luminary131/ file
# P32-P35_P72-P75.agc and Comanche055 page
# images.
# 2009-05-20 RSB  Corrected CSI/COM3 -> CSI/CDH3,
# CSI/CDHI -> CSI/CDH1, CDHTAB -> CDHTAG,
# changed a SETLOC from CSI/CDH to CSI/CDH1,
# a SETLOC CSI/CDH1 to CSIPROG.
# 2009-05-21 RSB  Changed a P32/P72D to P32/P72E in
# P32/P72D.  DP1/4TH changed to DP1/4 in
# CDHMVR.
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

# Page 649
# COELLIPTIC SEQUENCE INITIATION (CSI) PROGRAMS (P32 AND P72)

# MOD NO -1             LOG SECTION - P32-P35, P72-P75
# MOD BY WHITE.P        DATE 1JUNE67

# PURPOSE

# (1) TO CALCULATE PARAMETERS ASSOCIATED WITH THE FOLLOWING
# CONCENTRIC FLIGHT PLAN MANEUVERS - THE CO-ELLIPTIC SEQUENCE
# INITIATION (CSI) MANEUVER AND THE CONSTANT DELTA ALTITUDE
# (CDH) MANEUVER.

# (2) TO CALCULATE THESE PARAMETERS BASED UPON MANEUVER DATA
# APPROVED AND KEYED INTO THE DSKY BY THE ASTRONAUT.

# (3) TO DISPLAY TO THE ASTRONAUT AND THE GROUND DEPENDENT VARIABLES
# ASSOCIATED WITH THE CONCENTRIC FLIGHT PLAN MANEUVERS FOR
# APPROVAL BY THE ASTRONAUT/GROUND.

# (4) TO STORE THE CSI TARGET PARAMETERS FOR USE BY THE DESIRED
# THRUSTING PROGRAM.

# ASSUMPTIONS

# (1) AT A SELECTED TPI TIME THE LINE OF SIGHT BETWEEN THE ACTIVE
# AND PASSIVE VEHICLES IS SELECTED TO BE A PRESCRIBED ANGLE (E)
# FROM THE HORIZONTAL PLANE DEFINED BY THE ACTIVE VEHICLE
# POSITION.

# (2) THE TIME BETWEEN CSI IGNITION AND CDH IGNITION MUST BE
# COMPUTED TO BE GREATER THAN 10 MINUTES FOR SUCCESSFUL
# COMPLETION OF THE PROGRAM.

# (3) THE TIME BETWEEN CDH IGNITION AND TPI IGNITION MUST BE
# COMPUTED TO BE GREATER THAN 10 MINUTES FOR SUCCESSFUL
# COMPLETION OF THE PROGRAM.

# (4) CDH DELTA V IS SELECTED TO MINIMIZE THE VARIATION OF THE
# ALTITUDE DIFFERENCE BETWEEN THE ORBITS.

# (5) CSI BURN IS DEFINED SUCH THAT THE IMPULSIVE DELTA V IS IN THE
# HORIZONTAL PLANE DEFINED BY THE ACTIVE VEHICLE POSITION AT CSI
# IGNITION.

# (6) THE PERICENTER ALTITUDE OF THE ORBIT FOLLOWING CSI AND CDH
# MUST BE GREATER THAN 35,000 FT (LUNAR ORBIT) OR 85 NM (EARTH
# ORBIT) FOR SUCCESSFUL COMPLETION OF THIS PROGRAM.

# (7) THE CSI AND CDH MANEUVERS ARE ORIGINALLY ASSUMED TO BE
# PARALLEL TO THE PLANE OF THE CSM ORBIT.  HOWEVER, CREW
# Page 650
# MODIFICATION OF DELTA V (LV) COMPONENTS MAY RESULT IN AN
# OUT-OF-PLANE CSI MANEUVER.

# (8) STATE VECTOR UPDATES BY P27 ARE DISALLOWED DURING AUTOMATIC
# STATE VECTOR UPDATING INITIATED BY P20 (SEE ASSUMPTION 10).

# (9) COMPUTED VARIABLES MAY BE STORED FOR LATER VERIFICATION BY
# THE GROUND.  THESE STORAGE CAPABILITIES ARE NORMALLY LIMITED
# ONLY TO THE PARAMETERS FOR ONE THRUSTING MANEUVER AT A TIME
# EXCEPT FOR CONCENTRIC FLIGHT PLAN MANEUVER SEQUENCES.

# (10) THE RENDEZVOUS RADAR MAY OR MAY NOT BE USED TO UPDATE THE LM
# OR CSM STATE VECTORS FOR THIS PROGRAM.  IF RADAR USE IS
# DESIRED THE RADAR WAS TURNED ON AND LOCKED BY THE CSM BY
# PREVIOUS SELECTION OF P20.  RADAR SIGHTING MARKS WILL BE MADE
# AUTOMATICALLY APPROXIMATELY ONCE A MINUTE WHEN ENABLED BY THE
# TRACK AND UPDATE FLAGS (SEE P20).  THE RENDEZVOUS TRACKING
# MARK COUNTER IS ZEROED BY THE SELECTION OF P20 AND AFTER EACH
# THRUSTING MANEUVER.

# (11) THE ISS NEED NOT BE ON TO COMPLETE THIS PROGRAM.

# (12) THE OPERATION OF THE PROGRAM UTILIZES THE FOLLOWING FLAGS -

# ACTIVE VEHICLE FLAG - DESIGNATES THE VEHICLE WHICH IS
# DOING RENDEZVOUS THRUSTING MANEUVERS TO THE PROGRAM WHICH
# CALCULATES THE MANEUVER PARAMETERS.  SET AT THE START OF
# EACH RENDEZVOUS PRE-THRUSTING PROGRAM.

# FINAL FLAG - SELECTS FINAL PROGRAM DISPLAYS AFTER CREW HAS
# COMPLETED THE FINAL MANEUVER COMPUTATION AND DISPLAY
# CYCLE.

# EXTERNAL DELTA V STEERING FLAG - DESIGNATES THE TYPE OF
# STEERING REQUIRED FOR EXECUTION OF THIS MANEUVER BY THE
# THRUSTING PROGRAM SELECTED AFTER COMPLETION OF THIS
# PROGRAM.

# (13) IT IS NORMALLY REQUIRED THAT THE ISS BE ON FOR 1 HOUR PRIOR TO
# A THRUSTING MANEUVER.

# (14) THIS PROGRAM IS SELECTED BY THE ASTRONAUT BY DSKY ENTRY -

# P32 IF THIS VEHICLE IS ACTIVE VEHICLE.

# P72 IF THIS VEHICLE IS PASSIVE VEHICLE.

# INPUT

# (1) TCSI       TIME OF THE CSI MANEUVER
# Page 651
# (2) NN         NUMBER OF APSIDAL CROSSINGS THRU WHICH THE ACTIVE
# VEHICLE ORBIT CAN BE ADVANCED TO OBTAIN THE CDH
# MANEUVER POINT
# (3) ELEV       DESIRED LOS ANGLE AT TPI
# (4) TTPI       TIME OF THE TPI MANEUVER
# OUTPUT

# (1) TRKMKCNT   NUMBER OF MARKS
# (2) TTOGO      TIME TO GO
# (3) +MGA       MIDDLE GIMBAL ANGLE
# (4) DIFFALT    DELTA ALTITUDE AT CDH
# (5) T1TOT2     DELTA TIME FROM CSI TO CDH
# (6) T2TOT3     DELTA TIME FROM CDH TO TPI
# (7) DELVLVC    DELTA VELOCITY AT CSI - LOCAL VERTICAL COORDINATES
# (8) DELVLVC    DELTA VELOCITY AT CDH - LOCAL VERTICAL COORDINATES

# DOWNLINK

# (1) TCSI       TIME OF THE CSI MANEUVER
# (2) TCDH       TIME OF THE CDH MANEUVER
# (3) TTPI       TIME OF THE TPI MANEUVER
# (4) TIG        TIME OF THE CSI MANEUVER
# (5) DELVEET1   DELTA VELOCITY AT CSI - REFERENCE COORDINATES
# (6) DELVEET2   DELTA VELOCITY AT CDH - REFERENCE COORDINATES
# (7) DIFFALT    DELTA ALTITUDE AT CDH
# (8) NN         NUMBER OF APSIDAL CROSSINGS THRU WHICH THE ACTIVE
# VEHICLE ORBIT CAN BE ADVANCED TO OBTAIN THE CDH
# MANEUVER POINT
# (9) ELEV       DESIRED LOS ANGLE AT TPI

# COMMUNICATION TO THRUSTING PROGRAMS

# (1) TIG        TIME OF THE CSI MANEUVER
# (2) RTIG       POSITION OF ACTIVE VEHICLE AT CSI - BEFORE ROTATION
# INTO PLANE OF PASSIVE VEHICLE
# (3) VTIG       VELOCITY OF ACTIVE VEHICLE AT CSE - BEFORE ROTATION
# INTO PLANE OF PASSIVE VEHICLE
# (4) DELVSIN    DELTA VELOCITY AT CSI - REFERENCE COORDINATES
# (5) DELVSAB    MAGNITUDE OF DELTA VELOCITY AT CSI
# (6) XDELVFLG   SET TO INDICATE EXTERNAL DELTA V VG COMPUTATION

# SUBROUTINES USED

# AVFLAGA
# AVFLAGP
# P20FLGON
# VARALARM
# BANKCALL
# GOFLASH
# GOTOPOOH
# Page 652
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
#   SETLOC CSI/CDH1
#   BANK
#   EBANK= SUBEXIT
#   COUNT 35/P3272

W('04,3303', 0o04627, 'P32', 'TC', 'AVFLAGA', line=211)
W('04,3304', 0o03306, '', 'TC', 'P32STRT', line=212)
W('04,3305', 0o04642, 'P72', 'TC', 'AVFLAGP', line=213)
W('04,3306', 0o06006, 'P32STRT', 'TC', 'INTPRET', line=214)
W('04,3307', 0o77745, '', 'DLOAD', kind='interp', line=215)
W('04,3310', 0o11566, '', '', 'ZEROVEC', kind='operand', line=216)
W('04,3311', 0o03754, '', 'STORE', 'CENTANG', kind='interp', line=217)
W('04,3312', 0o77776, '', 'EXIT', kind='interp', line=218)
W('04,3313', 0o03331, '', 'TC', 'P32/P72A', line=219)
W('04,3314', 0o77734, 'ALMXITA', 'SXA,2', kind='interp', line=220)
W('04,3315', 0o03664, '', '', 'CSIALRM', kind='operand', line=221)
W('04,3316', 0o77740, 'ALMXIT', 'LXC,1', kind='interp', line=222)
W('04,3317', 0o03664, '', '', 'CSIALRM', kind='operand', line=223)
W('04,3320', 0o77533, '', 'SLOAD*', 'EXIT', kind='interp', line=224)
W('04,3321', 0o15653, '', '', 'ALARM/TB -1,1', kind='operand', line=225)
W('04,3322', 0o30154, '', 'CA', 'MPAC', line=226)
W('04,3323', 0o05764, '', 'TC', 'VARALARM', line=227)
W('04,3324', 0o35050, '', 'CAF', 'V05N09', line=228)
W('04,3325', 0o04662, '', 'TC', 'BANKCALL', line=229)
W('04,3326', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=230)
W('04,3327', 0o04106, '', 'TC', 'GOTOPOOH', line=231)
W('04,3330', 0o03324, '', 'TC', '-4', line=232)
W('04,3331', 0o04647, 'P32/P72A', 'TC', 'P20FLGON', line=233)
W('04,3332', 0o06006, '', 'TC', 'INTPRET', line=234)
W('04,3333', 0o77745, '', 'DLOAD', kind='interp', line=235)
W('04,3334', 0o11566, '', '', 'ZEROVEC', kind='operand', line=236)
W('04,3335', 0o03766, '', 'STORE', 'NN', kind='interp', line=237)
W('04,3336', 0o77776, '', 'EXIT', kind='interp', line=238)
W('04,3337', 0o34656, '', 'CAF', 'V06N11', 'TCSI', line=239)
W('04,3340', 0o04575, '', 'TC', 'VNPOOH', line=240)
W('04,3341', 0o34615, '', 'CAF', 'V06N55', 'NN. ELEV(RGL05)', line=241)
# Page 653
W('04,3342', 0o04662, '', 'TC', 'BANKCALL', line=243)
W('04,3343', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=244)
W('04,3344', 0o04106, '', 'TC', 'GOTOPOOH', line=245)
W('04,3345', 0o03347, '', 'TC', '+2', line=246)
W('04,3346', 0o03341, '', 'TC', '-5', line=247)
W('04,3347', 0o34614, '', 'CAF', 'V06N37', 'TTPI', line=248)
W('04,3350', 0o04575, '', 'TC', 'VNPOOH', line=249)
W('04,3351', 0o06006, '', 'TC', 'INTPRET', line=250)
W('04,3352', 0o77745, '', 'DLOAD', kind='interp', line=251)
W('04,3353', 0o02637, '', '', 'TCSI', kind='operand', line=252)
W('04,3354', 0o37413, '', 'STCALL', 'TIG', kind='interp', line=253)
W('04,3355', 0o10712, '', '', 'SELECTMU', kind='operand', line=254)
W('04,3356', 0o77624, 'P32/P72B', 'CALL', kind='interp', line=255)
W('04,3357', 0o76645, '', '', 'ADVANCE', kind='operand', line=256)
W('04,3360', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=257)
W('04,3361', 0o00001, '', '', '0D', kind='operand', line=258)
W('04,3362', 0o03512, '', '', 'VPASS1', kind='operand', line=259)
W('04,3363', 0o65315, '', 'PDVL', 'PDDL', kind='interp', line=260)
W('04,3364', 0o03756, '', '', 'RPASS1', kind='operand', line=261)
W('04,3365', 0o02637, '', '', 'TCSI', kind='operand', line=262)
W('04,3366', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=263)
W('04,3367', 0o03663, '', '', 'TTPI', kind='operand', line=264)
W('04,3370', 0o11630, '', '', '2PISC', kind='operand', line=265)
W('04,3371', 0o41512, '', 'SL2', 'PUSH', kind='interp', line=266)
W('04,3372', 0o77624, '', 'CALL', kind='interp', line=267)
W('04,3373', 0o72705, '', '', 'INTINT', kind='operand', line=268)
W('04,3374', 0o77624, '', 'CALL', kind='interp', line=269)
W('04,3375', 0o45247, '', '', 'PASSIVE', kind='operand', line=270)
W('04,3376', 0o77624, '', 'CALL', kind='interp', line=271)
W('04,3377', 0o15704, '', '', 'CSI/A', kind='operand', line=272)
W('04,3400', 0o43014, 'P32/P72C', 'BON', 'SET', kind='interp', line=273)
W('04,3401', 0o01311, '', '', 'FINALFLG', kind='operand', line=274)
W('04,3402', 0o11404, '', '', 'P32/P72D', kind='operand', line=275)
W('04,3403', 0o00470, '', '', 'UPDATFLG', kind='operand', line=276)
W('04,3404', 0o52145, 'P32/P72D', 'DLOAD', 'GOTO', kind='interp', line=277)
W('04,3405', 0o02547, '', '', 'T1TOT2', kind='operand', line=278)
W('04,3406', 0o30002, '', '', 'P32/P72E', kind='operand', line=279)
#   SETLOC CSI/CDH3
#   BANK
W('14,2002', 0o02547, 'P32/P72E', 'STORE', 'T1TOT2', kind='interp', line=282)
W('14,2003', 0o51025, '', 'DSU', 'BPL', kind='interp', line=283)
W('14,2004', 0o15652, '', '', '60MIN', kind='operand', line=284)
W('14,2005', 0o30002, '', '', 'P32/P72E', kind='operand', line=285)
W('14,2006', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=286)
W('14,2007', 0o03656, '', '', 'T2TOT3', kind='operand', line=287)
W('14,2010', 0o11407, '', '', 'P32/P72F', kind='operand', line=288)
#   SETLOC CSI/CDH1
#   BANK
W('04,3407', 0o03656, 'P32/P72F', 'STORE', 'T2TOT3', kind='interp', line=291)
W('04,3410', 0o51025, '', 'DSU', 'BPL', kind='interp', line=292)
# Page 654
W('04,3411', 0o15652, '', '', '60MIN', kind='operand', line=294)
W('04,3412', 0o11407, '', '', 'P32/P72F', kind='operand', line=295)
W('04,3413', 0o77776, '', 'EXIT', kind='interp', line=296)
W('04,3414', 0o34660, '', 'CAF', 'V06N75', line=297)
W('04,3415', 0o04575, '', 'TC', 'VNPOOH', line=298)
W('04,3416', 0o06006, '', 'TC', 'INTPRET', line=299)
W('04,3417', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=300)
W('04,3420', 0o02445, '', '', 'DELVEET1', kind='operand', line=301)
W('04,3421', 0o73457, '', '', 'S32/33.1', kind='operand', line=302)
W('04,3422', 0o26445, '', 'STOVL', 'DELVEET1', kind='interp', line=303)
W('04,3423', 0o02453, '', '', 'RACT2', kind='operand', line=304)
W('04,3424', 0o26541, '', 'STOVL', 'RACT1', kind='interp', line=305)
W('04,3425', 0o03667, '', '', 'DELVEET2', kind='operand', line=306)
W('04,3426', 0o45170, '', 'AXT,1', 'CALL', kind='interp', line=307)
W('04,3427', 0o01522, '', 'VN', '0682', kind='data', line=308)
W('04,3430', 0o76625, '', '', 'DISDVLVC', kind='operand', line=309)
W('04,3431', 0o77745, '', 'DLOAD', kind='interp', line=310)
W('04,3432', 0o03663, '', '', 'TTPI', kind='operand', line=311)
W('04,3433', 0o36641, '', 'STCALL', 'TTPIO', kind='interp', line=312)
W('04,3434', 0o73002, '', '', 'VN1645', kind='operand', line=313)
W('04,3435', 0o77650, '', 'GOTO', kind='interp', line=314)
W('04,3436', 0o11356, '', '', 'P32/P72B', kind='operand', line=315)
# Page 655
# CONSTANT DELTA HEIGHT (CDH) PROGRAMS (P33 AND P73)

# MOD NO -1             LOC SECTION - P32-P35, P72-P75
# MOD BY WHITE.P        DATE 1JUNE67
# PURPOSE

# (1) TO CALCULATE PARAMETERS ASSOCIATED WITH THE CONSTANT DELTA
# ALTITUDE MANEUVER (CDH).

# (2) TO CALCULATE THESE PARAMETERS BASED UPON MANEUVER DATA
# APPROVED AND KEYED INTO THE DSKY BY THE ASTRONAUT.

# (3) TO DISPLAY TO THE ASTRONAUT AND THE GROUND DEPENDENT VARIABLES
# ASSOCIATED WITH THE CDH MANEUVER FOR APPROVAL BY THE
# ASTRONAUT/GROUND.

# (4) TO STORE THE CDH TARGET PARAMETERS FOR USE BY THE DESIRED
# THRUSTING PROGRAM.

# ASSUMPTIONS

# (1) THIS PROGRAM IS BASED UPON PREVIOUS COMPLETION OF THE
# CO-ELLIPTIC SEQUENCE INITIATION (CSI) PROGRAM (P32/P72).
# THERFORE -

# (A) AT A SELECTED TPI TIME (NOW IN STORAGE) THE LINE OF SIGHT
# BETWEEN THE ACTIVE AND PASSIVE VEHICLES WAS SELECTED TO BE
# A PRESCRIBED ANGLE (E) (NOW IN STORAGE) FROM THE
# HORIZONTAL PLANE DEFINED BY THE ACTIVE VEHICLE POSITION.

# (B) THE TIME BETWEEN CSI IGNITION AND CDH IGNITION WAS
# COMPUTED TO BE GREATER THAN 10 MINUTES.

# (C) THE TIME BETWEEN CDH IGNITION AND TPI IGNITION WAS
# COMPUTED TO BE GREATER THAN 10 MINUTES.

# (D) THE VARIATION OF THE ALTITUDE DIFFERENCE BETWEEN THE
# ORBITS WAS MINIMIZED.

# (E) CSI BURN WAS DEFINED SUCH THAT THE IMPULSIVE DELTA V WAS
# IN THE HORIZONTAL PLANE DEFINED BY ACTIVE VEHICLE

# POSITION AT CSI IGNITION.

# (F) THE PERICENTER ALTITUDES OF THE ORBITS FOLLOWING CSI AND
# CDH WERE COMPUTED TO BE GREATER THAN 35,000 FT FOR LUNAR
# ORBIT OR 85 NM FOR EARTH ORBIT.

# (G) THE CSI AND CDH MANEUVERS WERE ASSUMED TO BE PARALLEL TO
# THE PLANE OF THE PASSIVE VEHICLE ORBIT.  HOWEVER, CREW
# Page 656
# MODIFICATION OF DELTA V (LV) COMPONENTS MAY HAVE RESULTED
# IN AN OUT-OF-PLANE MANEUVER.

# (2) STATE VECTOR UPDATES BY P27 ARE DISALLOWED DURING AUTOMATIC
# STATE VECTOR UPDATING INITIATED BY P20 (SEE ASSUMPTION 4).

# (3) COMPUTED VARIABLES MAY BE STORED FOR LATER VERIFICATION BY
# THE GROUND.  THESE STORAGE CAPABILITIES ARE NORMALLY LIMITED
# ONLY TO THE PARAMETERS FOR ONE THRUSTING MANEUVER AT A TIME
# EXCEPT FOR CONCENTRIC FLIGHT PLAN MANEUVER SEQUENCES.

# (4) THE RENDEZVOUS RADAR MAY OR MAY NOT BE USED TO UPDATE THE LM
# OR CSM STATE VECTORS FOR THIS PROGRAM.  IF RADAR USE IS
# DESIRED THE RADAR WAS TURNED ON AND LOCKED ON THE CSM BY
# PREVIOUS SELECTION OF P20.  RADAR SIGHTING MARKS WILL BE MADE
# AUTOMATICALLY APPROXIMATELY ONCE A MINUTE WHEN ENABLED BY THE
# TRACK AND UPDATE FLAGS (SEE P20).  THE RENDEZVOUS TRACKING
# MARK COUNTER IS ZEROED BY THE SELECTION OF P20 AND AFTER EACH
# THRUSTING MANEUVER.

# (5) THE ISS NEED NOT BE ON TO COMPLETE THIS PROGRAM.

# (6) THE OPERATION OF THE PROGRAM UTILIZES THE FOLLOWING FLAGS -

# ACTIVE VEHICLE FLAG - DESIGNATES THE VEHICLE WHICH IS
# DOING RENDEZVOUS THRUSTING MANEUVERS TO THE PROGRAM WHICH
# CALCULATES THE MANEUVER PARAMETERS.  SET AT THE START OF
# EACH RENDEZVOUS PRE-THRUSTING PROGRAM.

# FINAL FLAG - SELECTS FINAL PROGRAM DISPLAYS AFTER CREW HAS
# COMPLETED THE FINAL MANEUVER COMPUTATION AND DISPLAY
# CYCLE.

# EXTERNAL DELTA V STEERING FLAG - DESIGNATES THE TYPE OF
# STEERING REQUIRED FOR EXECUTION OF THIS MANEUVER BY THE
# THRUSTING PROGRAM SELECTED AFTER COMPLETION OF THIS
# PROGRAM.

# (7) IT IS NORMALLY REQUIRED THAT THE ISS BE ON FOR 1 HOUR PRIOR TO
# A THRUSTING MANEUVER.

# (8) THIS PROGRAM IS SELECTED BY THE ASTRONAUT BY DSKY ENTRY -

# P33 IF THIS VEHICLE IS ACTIVE VEHICLE.

# P73 IF THIS VEHICLE IS PASSIVE VEHICLE.

# INPUT

# (1) TTPIO      TIME OF THE TPI MANEUVER - SAVED FROM P32/P72
# Page 657
# (2) ELEV       DESIRED LOS ANGLE AT TPI - SAVED FROM P32/P72
# (3) TCDH       TIME OF THE CDH MANEUVER

# OUTPUT

# (1) TRKMKCNT   NUMBER OF MARKS
# (2) TTOGO      TIME TO GO
# (3) +MGA       MIDDLE GIMBAL ANGLE
# (4) DIFFALT    DELTA ALTITUDE AT CDH
# (5) T2TOT3     DELTA TIME FROM CDH TO COMPUTED TPI
# (6) NOMTPI     DELTA TIME FROM NOMINAL TPI TO COMPUTED TPI
# (7) DELVLVC    DELTA VELOCITY AT CDH - LOCAL VERTICAL COORDINATES

# DOWNLINK

# (1) TCDH       TIME OF THE CDH MANEUVER
# (2) TTPI       TIME OF THE TPI MANEUVER
# (3) TIG        TIME OF THE CDH MANEUVER
# (4) DELLVEET2  DELTA VELOCITY AT CDH - REFERENCE COORDINATES
# (5) DIFFALT    DELTA ALTITUDE AT CDH
# (6) ELEV       DESIRED LOS ANGLE AT TPI
# COMMUNICATION TO THRUSTING PROGRAMS

# (1) TIG        TIME OF THE CDH MANEUVER
# (2) RTIG       POSITION OF ACTIVE VEHICLE AT CDH - BEFORE ROTATION
# INTO PLANE OF PASSIVE VEHICLE
# (3) VTIG       VELOCITY OF ACTIVE VEHICLE AT CDH - BEFORE ROTATION
# INTO PLANE OF PASSIVE VEHICLE
# (4) DELVSIN    DELTA VELOCITY AT CDH - REFERENCE COORDINATES
# (5) DELVSAB    MAGNITUDE OF DELTA VELOCITY AT CDH
# (6) XDELVFLG   SET TO INDICATE EXTERNAL DELTA V VG COMPUTATION

# SUBROUTINES USED

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
# Page 658
# VN1645

#   COUNT 35/P3373

W('04,3437', 0o04627, 'P33', 'TC', 'AVFLAGA', line=474)
W('04,3440', 0o03442, '', 'TC', 'P33/P73A', line=475)
W('04,3441', 0o04642, 'P73', 'TC', 'AVFLAGP', line=476)
W('04,3442', 0o04647, 'P33/P73A', 'TC', 'P20FLGON', line=477)
W('04,3443', 0o34657, '', 'CAF', 'V06N13', 'TCDH', line=478)
W('04,3444', 0o04575, '', 'TC', 'VNPOOH', line=479)
W('04,3445', 0o06006, '', 'TC', 'INTPRET', line=480)
W('04,3446', 0o77745, '', 'DLOAD', kind='interp', line=481)
W('04,3447', 0o02641, '', '', 'TTPIO', kind='operand', line=482)
W('04,3450', 0o17663, '', 'STODL', 'TTPI', kind='interp', line=483)
W('04,3451', 0o02635, '', '', 'TCDH', kind='operand', line=484)
W('04,3452', 0o37413, '', 'STCALL', 'TIG', kind='interp', line=485)
W('04,3453', 0o10712, '', '', 'SELECTMU', kind='operand', line=486)
W('04,3454', 0o77624, 'P33/P73B', 'CALL', kind='interp', line=487)
W('04,3455', 0o76645, '', '', 'ADVANCE', kind='operand', line=488)
W('04,3456', 0o77624, '', 'CALL', kind='interp', line=489)
W('04,3457', 0o13230, '', '', 'CDHMVR', kind='operand', line=490)
W('04,3460', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=491)
W('04,3461', 0o00001, '', '', '0D', kind='operand', line=492)
W('04,3462', 0o03546, '', '', 'VACT3', kind='operand', line=493)
W('04,3463', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=494)
W('04,3464', 0o02453, '', '', 'RACT2', kind='operand', line=495)
W('04,3465', 0o63671, '', '', 'INTINT3P', kind='operand', line=496)
W('04,3466', 0o77624, '', 'CALL', kind='interp', line=497)
W('04,3467', 0o45237, '', '', 'ACTIVE', kind='operand', line=498)
W('04,3470', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=499)
W('04,3471', 0o00001, '', '', '0D', kind='operand', line=500)
W('04,3472', 0o02617, '', '', 'VPASS2', kind='operand', line=501)
W('04,3473', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=502)
W('04,3474', 0o02625, '', '', 'RPASS2', kind='operand', line=503)
W('04,3475', 0o63671, '', '', 'INTINT3P', kind='operand', line=504)
W('04,3476', 0o77624, '', 'CALL', kind='interp', line=505)
W('04,3477', 0o45247, '', '', 'PASSIVE', kind='operand', line=506)
W('04,3500', 0o43145, '', 'DLOAD', 'SET', kind='interp', line=507)
W('04,3501', 0o11566, '', '', 'ZEROVEC', kind='operand', line=508)
W('04,3502', 0o03461, '', '', 'ITSWICH', kind='operand', line=509)
W('04,3503', 0o36364, '', 'STCALL', 'NOMTPI', kind='interp', line=510)
W('04,3504', 0o72216, '', '', 'S33/34.1', kind='operand', line=511)
W('04,3505', 0o77454, '', 'BZE', 'EXIT', kind='interp', line=512)
W('04,3506', 0o24000, '', '', 'P33/P73C', kind='operand', line=513)
W('04,3507', 0o05650, '', 'TC', 'ALARM', line=514)
W('04,3510', 0o00611, '', 'OCT', '611', kind='data', line=515)
W('04,3511', 0o35050, '', 'CAF', 'V05N09', line=516)
W('04,3512', 0o04662, '', 'TC', 'BANKCALL', line=517)
W('04,3513', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=518)
W('04,3514', 0o04106, '', 'TC', 'GOTOPOOH', line=519)
# Page 659
W('04,3515', 0o03517, '', 'TC', '+2', line=521)
W('04,3516', 0o03442, '', 'TC', 'P33/P73A', line=522)
W('04,3517', 0o06006, '', 'TC', 'INTPRET', line=523)
W('04,3520', 0o77745, '', 'DLOAD', kind='interp', line=524)
W('04,3521', 0o11566, '', '', 'ZEROVEC', kind='operand', line=525)
W('04,3522', 0o36364, '', 'STCALL', 'NOMTPI', kind='interp', line=526)
W('04,3523', 0o24000, '', '', 'P33/P73C', kind='operand', line=527)
#   SETLOC CSI/CDH2
#   BANK

W('12,2000', 0o43014, 'P33/P73C', 'BON', 'SET', kind='interp', line=531)
W('12,2001', 0o01311, '', '', 'FINALFLG', kind='operand', line=532)
W('12,2002', 0o24004, '', '', 'P33/P73D', kind='operand', line=533)
W('12,2003', 0o00470, '', '', 'UPDATFLG', kind='operand', line=534)
W('12,2004', 0o43345, 'P33/P73D', 'DLOAD', 'DAD', kind='interp', line=535)
W('12,2005', 0o02364, '', '', 'NOMTPI', kind='operand', line=536)
W('12,2006', 0o03663, '', '', 'TTPI', kind='operand', line=537)
W('12,2007', 0o03663, '', 'STORE', 'TTPI', kind='interp', line=538)
W('12,2010', 0o52025, '', 'DSU', 'GOTO', kind='interp', line=539)
W('12,2011', 0o02635, '', '', 'TCDH', kind='operand', line=540)
W('12,2012', 0o11524, '', '', 'P33/P73E', kind='operand', line=541)
#   SETLOC CSI/CDH1
#   BANK

W('04,3524', 0o51025, 'P33/P73E', 'DSU', 'BPL', kind='interp', line=545)
W('04,3525', 0o15652, '', '', '60MIN', kind='operand', line=546)
W('04,3526', 0o11524, '', '', 'P33/P73E', kind='operand', line=547)
W('04,3527', 0o77615, '', 'DAD', kind='interp', line=548)
W('04,3530', 0o15652, '', '', '60MIN', kind='operand', line=549)
W('04,3531', 0o16547, '', 'STODL', 'T1TOT2', kind='interp', line=550)
W('04,3532', 0o03663, '', '', 'TTPI', kind='operand', line=551)
W('04,3533', 0o41425, '', 'DSU', 'PUSH', kind='interp', line=552)
W('04,3534', 0o02641, '', '', 'TTPIO', kind='operand', line=553)
W('04,3535', 0o45246, 'P33/P73F', 'ABS', 'DSU', kind='interp', line=554)
W('04,3536', 0o15652, '', '', '60MIN', kind='operand', line=555)
W('04,3537', 0o43244, '', 'BPL', 'DAD', kind='interp', line=556)
W('04,3540', 0o11535, '', '', 'P33/P73F', kind='operand', line=557)
W('04,3541', 0o15652, '', '', '60MIN', kind='operand', line=558)
W('04,3542', 0o45565, '', 'SIGN', 'STADR', kind='interp', line=559)
W('04,3543', 0o74121, '', 'STORE', 'T2TOT3', kind='interp', line=560)
W('04,3544', 0o77776, '', 'EXIT', kind='interp', line=561)
W('04,3545', 0o34660, '', 'CAF', 'V06N75', line=562)
W('04,3546', 0o04575, '', 'TC', 'VNPOOH', line=563)
W('04,3547', 0o06006, '', 'TC', 'INTPRET', line=564)
W('04,3550', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=565)
W('04,3551', 0o03667, '', '', 'DELVEET2', kind='operand', line=566)
W('04,3552', 0o73457, '', '', 'S32/33.1', kind='operand', line=567)
W('04,3553', 0o37667, '', 'STCALL', 'DELVEET2', kind='interp', line=568)
W('04,3554', 0o73002, '', '', 'VN1645', kind='operand', line=569)
W('04,3555', 0o77650, '', 'GOTO', kind='interp', line=570)
# Page 660
W('04,3556', 0o11454, '', '', 'P33/P73B', kind='operand', line=572)
# Page 661
# ..... AVFLAGA/P .....
# Page 662
# ..... DISDVLVC .....

# SUBROUTINES USED

# S32/33.X
# VNPOOH

#   SETLOC CDHTAG3
#   BANK

W('37,2625', 0o03405, 'DISDVLVC', 'STORE', 'DELVLVC', kind='interp', line=586)
W('37,2626', 0o45020, '', 'STQ', 'CALL', kind='interp', line=587)
W('37,2627', 0o01340, '', '', 'NORMEX', kind='operand', line=588)
W('37,2630', 0o26231, '', '', 'S32/33.X', kind='operand', line=589)
W('37,2631', 0o64375, '', 'VLOAD', 'MXV', kind='interp', line=590)
W('37,2632', 0o03405, '', '', 'DELVLVC', kind='operand', line=591)
W('37,2633', 0o00001, '', '', '0D', kind='operand', line=592)
W('37,2634', 0o66172, '', 'VSL1', 'SXA,1', kind='interp', line=593)
W('37,2635', 0o02365, '', '', 'VERBNOUN', kind='operand', line=594)
W('37,2636', 0o03405, '', 'STORE', 'DELVLVC', kind='interp', line=595)
W('37,2637', 0o77776, '', 'EXIT', kind='interp', line=596)
W('37,2640', 0o31765, '', 'CA', 'VERBNOUN', line=597)
W('37,2641', 0o04575, '', 'TC', 'VNPOOH', line=598)
W('37,2642', 0o06006, '', 'TC', 'INTPRET', line=599)
W('37,2643', 0o77650, '', 'GOTO', kind='interp', line=600)
W('37,2644', 0o01340, '', '', 'NORMEX', kind='operand', line=601)
#   SETLOC FFTAG12
#   BANK

W('4656', 0o01413, 'V06N11', 'VN', '0611', kind='data', line=605)
W('4657', 0o01415, 'V06N13', 'VN', '0613', kind='data', line=606)
W('4660', 0o01513, 'V06N75', 'VN', '0675', kind='data', line=607)

W('4661', 0o01462, 'V06N50', 'VN', '0650', kind='data', line=609)
# Page 663
# ..... CSI/A .....

# SUBROUTINES USED

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
#   SETLOC CSIPROG
#   BANK
#   EBANK= SUBEXIT
#   COUNT 34/CSI

W('06,3651', 0o00025, '60MIN', '2DEC', '360000', kind='data', line=631)
W('06,3652', 0o37100, kind='data', line=631)

W('06,3653', 0o00600, 'ALARM/TB', 'OCT', '00600', 'NO 1', kind='data', line=633)
W('06,3654', 0o00601, '', 'OCT', '00601', '   2', kind='data', line=634)
W('06,3655', 0o00602, '', 'OCT', '00602', '   3', kind='data', line=635)
W('06,3656', 0o00603, '', 'OCT', '00603', '   4', kind='data', line=636)
W('06,3657', 0o00604, '', 'OCT', '00604', '   5', kind='data', line=637)
W('06,3660', 0o00605, '', 'OCT', '00605', '   6', kind='data', line=638)
W('06,3661', 0o00606, '', 'OCT', '00606', '   7', kind='data', line=639)
W('06,3662', 0o00000, 'LOOPMX', '2DEC', '16', kind='data', line=640)
W('06,3663', 0o00020, kind='data', line=640)

W('06,3664', 0o00003, 'INITST', '2DEC', '.03048 B-7', 'INITIAL DELDV = 10 FPS', kind='data', line=642)
W('06,3665', 0o34661, kind='data', line=642)

W('06,3666', 0o00606, 'DVMAX1', '2DEC', '3.0480 B-7', 'MAXIMUM DV1 = 1000 FPS', kind='data', line=644)
W('06,3667', 0o04467, kind='data', line=644)

W('06,3670', 0o00601, 'DVMAX2', '2DEC', '3.014472 B-7', '               989 FPS', kind='data', line=646)
W('06,3671', 0o33216, kind='data', line=646)

W('06,3672', 0o10000, '1DPB2', '2DEC', '1.0 B-2', kind='data', line=648)
W('06,3673', 0o00000, kind='data', line=648)

W('06,3674', 0o00000, '1DPB28', '2DEC', '1', kind='data', line=650)
W('06,3675', 0o00001, kind='data', line=650)

W('06,3676', 0o00000, 'EPSILN1', '2DEC', '.0003048 B-7', '.1 FPS', kind='data', line=652)
W('06,3677', 0o01177, kind='data', line=652)

W('06,3700', 0o77754, 'FIFPSDP', '2DEC', '-.152400 B-7', '50  FPS', kind='data', line=654)
W('06,3701', 0o57611, kind='data', line=654)

W('06,3702', 0o00116, 'DELMAX1', '2DEC', '.6096000 B-7', '200 FPS', kind='data', line=656)
W('06,3703', 0o00730, kind='data', line=656)

#   SETLOC CSI/CDH
#   BANK
W('35,3445', 0o00004, 'PMINE', '2DEC', '157420 B-29', '84 NM. - MUST BE 8 WORDS BEFORE PMINM', kind='data', line=660)
W('35,3446', 0o31566, kind='data', line=660)
# Page 664
W('35,3447', 0o00002, 'NICKELDP', '2DEC', '.021336 B-7', '7 FPS', kind='data', line=662)
W('35,3450', 0o27311, kind='data', line=662)

W('35,3451', 0o00003, 'INITST1', '2DEC', '.03048 B-7', 'INITIAL DELDV = 10 FPS', kind='data', line=664)
W('35,3452', 0o34661, kind='data', line=664)

W('35,3453', 0o00000, 'ONETHTH', '2DEC', '.0001 B-3', kind='data', line=666)
W('35,3454', 0o06433, kind='data', line=666)

W('35,3455', 0o00000, 'PMINM', '2DEC', '10668 B-29', '35000 FT - MUST BE 8 WORDS AFTER PMINE.', kind='data', line=668)
W('35,3456', 0o12326, kind='data', line=668)

#   SETLOC CSIPROG
#   BANK

W('06,3704', 0o43014, 'CSI/A', 'CLEAR', 'SET', 'INITIALIZE INDICATORS', kind='interp', line=673)
W('06,3705', 0o05660, '', '', 'S32.1F1', 'DVT1 HAS EXCEEDED MAX INDICATOR', kind='operand', line=674)
W('06,3706', 0o05461, '', '', 'S32.1F2', 'FIRST PASS FOR NEWTON ITERATION INDICATR', kind='operand', line=675)
W('06,3707', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=676)
W('06,3710', 0o05662, '', '', 'S32.1F3A', '00=1ST 2 PASSES 2ND CYCLE 01=FIRST CYCLE', kind='operand', line=677)
W('06,3711', 0o05463, '', '', 'S32.1F3B', '10=2ND CYCLE, 11=50 FPS STAGE 2ND CYCLE', kind='operand', line=678)
W('06,3712', 0o77745, '', 'DLOAD', kind='interp', line=679)
W('06,3713', 0o11566, '', '', 'ZEROVEC', kind='operand', line=680)
W('06,3714', 0o03764, '', 'STORE', 'LOOPCT', kind='interp', line=681)
W('06,3715', 0o03665, '', 'STORE', 'CSIALRM', kind='interp', line=682)
W('06,3716', 0o77201, 'CSI/B', 'SETPD', 'VLOAD', kind='interp', line=683)
W('06,3717', 0o00001, '', '', '0D', kind='operand', line=684)
W('06,3720', 0o02541, '', '', 'RACT1', kind='operand', line=685)
W('06,3721', 0o41446, '', 'ABVAL', 'PUSH', 'RA1                            B29 PL02D', kind='interp', line=686)
W('06,3722', 0o70501, '', 'NORM', 'SR1', kind='interp', line=687)
W('06,3723', 0o00050, '', '', 'X2', '                        B29-N2+ B1 PL04D', kind='operand', line=688)
W('06,3724', 0o51515, '', 'PDVL', 'ABVAL', kind='interp', line=689)
W('06,3725', 0o03554, '', '', 'RPASS3', kind='operand', line=690)
W('06,3726', 0o55301, '', 'NORM', 'BDDV', 'RA1/RP3                         B1 PL02D', kind='interp', line=691)
W('06,3727', 0o00047, '', '', 'X1', kind='operand', line=692)
W('06,3730', 0o53664, '', 'XSU,2', 'SR*', '                                B2', kind='interp', line=693)
W('06,3731', 0o00046, '', '', 'X1', kind='operand', line=694)
W('06,3732', 0o57175, '', '', '1,2', kind='operand', line=695)
W('06,3733', 0o41215, '', 'DAD', 'DMP', '(1+(RA1/RP3))RA1        B29+B2=B31 PL00D', kind='interp', line=696)
W('06,3734', 0o15673, '', '', '1DPB2', kind='operand', line=697)
W('06,3735', 0o65301, '', 'NORM', 'PDDL', '                                   PL02D', kind='interp', line=698)
W('06,3736', 0o00047, '', '', 'X1', kind='operand', line=699)
W('06,3737', 0o03750, '', '', 'RTMU', kind='operand', line=700)
W('06,3740', 0o56342, '', 'SR1', 'DDV', '                       B38-B31= B7 PL00D', kind='interp', line=701)
W('06,3741', 0o75457, '', 'SL*', 'SQRT', '                                B7', kind='interp', line=702)
W('06,3742', 0o20172, '', '', '0 -7,1', kind='operand', line=703)
W('06,3743', 0o53515, '', 'PDVL', 'UNIT', '                                   PL02D', kind='interp', line=704)
W('06,3744', 0o02541, '', '', 'RACT1', kind='operand', line=705)
W('06,3745', 0o47315, '', 'PDVL', 'VXV', kind='interp', line=706)
W('06,3746', 0o02611, '', '', 'UP1', kind='operand', line=707)
W('06,3747', 0o77656, '', 'UNIT', '', 'UNIT(URP1 X UVP1 X URA1) = UH1', kind='interp', line=708)
W('06,3750', 0o72441, '', 'DOT', 'SL1', 'VA1 . UH1                       B7', kind='interp', line=709)
W('06,3751', 0o03504, '', '', 'VACT1', kind='operand', line=710)
W('06,3752', 0o45421, '', 'BDSU', 'STADR', '                                   PL00D', kind='interp', line=711)
# Page 665
W('06,3753', 0o60315, '', 'STODL', 'DELVCSI', kind='interp', line=713)
W('06,3754', 0o15665, '', '', 'INITST', '10 FPS', kind='operand', line=714)
W('06,3755', 0o03464, '', 'STORE', 'DELDV', kind='interp', line=715)
W('06,3756', 0o43345, 'CSI/B1', 'DLOAD', 'DAD', 'IF LOOPCT = 16', kind='interp', line=716)
W('06,3757', 0o03764, '', '', 'LOOPCT', kind='operand', line=717)
W('06,3760', 0o15675, '', '', '1DPB28', kind='operand', line=718)
W('06,3761', 0o03764, '', 'STORE', 'LOOPCT', kind='interp', line=719)
W('06,3762', 0o77025, '', 'DSU', 'AXT,2', kind='interp', line=720)
W('06,3763', 0o15663, '', '', 'LOOPMX', kind='operand', line=721)
W('06,3764', 0o00006, '', '', '6', kind='operand', line=722)
W('06,3765', 0o52044, '', 'BPL', 'GOTO', kind='interp', line=723)
W('06,3766', 0o63642, '', '', 'SCNDSOL', kind='operand', line=724)
W('06,3767', 0o24013, '', '', 'CSI/B2', kind='operand', line=725)

#   SETLOC CSIPROG2
#   BANK

W('12,2013', 0o77601, 'CSI/B2', 'SETPD', kind='interp', line=730)
W('12,2014', 0o00001, '', '', '0D', kind='operand', line=731)
W('12,2015', 0o51545, '', 'DLOAD', 'ABS', kind='interp', line=732)
W('12,2016', 0o03462, '', '', 'DELVCSI', kind='operand', line=733)
W('12,2017', 0o50025, '', 'DSU', 'BMN', kind='interp', line=734)
W('12,2020', 0o15667, '', '', 'DVMAX1', kind='operand', line=735)
W('12,2021', 0o45267, '', '', 'CSI/B23', kind='operand', line=736)
W('12,2022', 0o43174, '', 'AXT,2', 'BON', kind='interp', line=737)
W('12,2023', 0o00007, '', '', '7', kind='operand', line=738)
W('12,2024', 0o05700, '', '', 'S32.1F1', kind='operand', line=739)
W('12,2025', 0o63642, '', '', 'SCNDSOL', kind='operand', line=740)
W('12,2026', 0o43014, '', 'BOFF', 'BON', kind='interp', line=741)
W('12,2027', 0o05742, '', '', 'S32.1F3A', kind='operand', line=742)
W('12,2030', 0o24033, '', '', 'CSI/B22', 'FLAG 3 NEQ 3', kind='operand', line=743)
W('12,2031', 0o05703, '', '', 'S32.1F3B', kind='operand', line=744)
W('12,2032', 0o63642, '', '', 'SCNDSOL', kind='operand', line=745)
W('12,2033', 0o71214, 'CSI/B22', 'SET', 'DLOAD', kind='interp', line=746)
W('12,2034', 0o05460, '', '', 'S32.1F1', kind='operand', line=747)
W('12,2035', 0o15671, '', '', 'DVMAX2', kind='operand', line=748)
W('12,2036', 0o77765, '', 'SIGN', kind='interp', line=749)
W('12,2037', 0o03462, '', '', 'DELVCSI', kind='operand', line=750)
W('12,2040', 0o37462, '', 'STCALL', 'DELVCSI', kind='interp', line=751)
W('12,2041', 0o45267, '', '', 'CSI/B23', kind='operand', line=752)

#   SETLOC CSIPROG3
#   BANK

W('22,3267', 0o41575, 'CSI/B23', 'VLOAD', 'PUSH', kind='interp', line=757)
W('22,3270', 0o02541, '', '', 'RACT1', kind='operand', line=758)
W('22,3271', 0o63256, '', 'UNIT', 'PDVL', kind='interp', line=759)
W('22,3272', 0o02611, '', '', 'UP1', kind='operand', line=760)
W('22,3273', 0o53435, '', 'VXV', 'UNIT', 'UNIT(URP1 X UVP1 X URA1) = UH1', kind='interp', line=761)
W('22,3274', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=762)
# Page 666
W('22,3275', 0o03462, '', '', 'DELVCSI', kind='operand', line=764)
W('22,3276', 0o02445, '', 'STORE', 'DELVEET1', kind='interp', line=765)
W('22,3277', 0o40055, '', 'VAD', 'BOV', kind='interp', line=766)
W('22,3300', 0o03504, '', '', 'VACT1', kind='operand', line=767)
W('22,3301', 0o45302, '', '', 'CSI/B23D', kind='operand', line=768)
W('22,3302', 0o37474, 'CSI/B23D', 'STCALL', 'VACT4', kind='interp', line=769)
W('22,3303', 0o45253, '', '', 'VECSHIFT', kind='operand', line=770)
W('22,3304', 0o26746, '', 'STOVL', 'VVEC', kind='interp', line=771)
W('22,3305', 0o77614, '', 'SET', kind='interp', line=772)
W('22,3306', 0o03466, '', '', 'RVSW', kind='operand', line=773)
W('22,3307', 0o26657, '', 'STOVL', 'RVEC', kind='interp', line=774)
W('22,3310', 0o05426, '', '', 'SN359+', kind='operand', line=775)
W('22,3311', 0o36732, '', 'STCALL', 'SNTH', 'ALSO CSTH', kind='interp', line=776)
W('22,3312', 0o24744, '', '', 'TIMETHET', kind='operand', line=777)
W('22,3313', 0o72142, '', 'SR1', 'LXA,1', kind='interp', line=778)
W('22,3314', 0o03745, '', '', 'RTX1', kind='operand', line=779)
W('22,3315', 0o37472, '', 'STCALL', 'HAFPA1', kind='interp', line=780)
W('22,3316', 0o45163, '', '', 'PERIAPO', kind='operand', line=781)
W('22,3317', 0o77624, '', 'CALL', kind='interp', line=782)
W('22,3320', 0o45263, '', '', 'SHIFTR1', kind='operand', line=783)
W('22,3321', 0o17460, '', 'STODL', 'POSTCSI', kind='interp', line=784)
W('22,3322', 0o03754, '', '', 'CENTANG', kind='operand', line=785)
W('22,3323', 0o52054, '', 'BZE', 'GOTO', kind='interp', line=786)
W('22,3324', 0o45326, '', '', '+2', kind='operand', line=787)
W('22,3325', 0o47145, '', '', 'CIRCL', kind='operand', line=788)
W('22,3326', 0o77745, '', 'DLOAD', kind='interp', line=789)
W('22,3327', 0o02754, '', '', 'ECC', kind='operand', line=790)
W('22,3330', 0o50025, '', 'DSU', 'BMN', kind='interp', line=791)
W('22,3331', 0o33454, '', '', 'ONETHTH', kind='operand', line=792)
W('22,3332', 0o47145, '', '', 'CIRCL', kind='operand', line=793)
W('22,3333', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=794)
W('22,3334', 0o00041, '', '', 'R1', kind='operand', line=795)
W('22,3335', 0o45263, '', '', 'SHIFTR1', kind='operand', line=796)
W('22,3336', 0o60201, '', 'SETPD', 'NORM', kind='interp', line=797)
W('22,3337', 0o00003, '', '', '2D', kind='operand', line=798)
W('22,3340', 0o00047, '', '', 'X1', kind='operand', line=799)
W('22,3341', 0o50315, '', 'PDVL', 'DOT', '                                   PL04D', kind='interp', line=800)
W('22,3342', 0o02541, '', '', 'RACT1', kind='operand', line=801)
W('22,3343', 0o03474, '', '', 'VACT4', kind='operand', line=802)
W('22,3344', 0o56246, '', 'ABS', 'DDV', kind='interp', line=803)
W('22,3345', 0o00003, '', '', '02D', '(/RDOTV/)/R1          B36-B29= B7', kind='operand', line=804)
W('22,3346', 0o45257, '', 'SL*', 'DSU', kind='interp', line=805)
W('22,3347', 0o20201, '', '', '0,1', kind='operand', line=806)
W('22,3350', 0o33450, '', '', 'NICKELDP', kind='operand', line=807)
W('22,3351', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=808)
W('22,3352', 0o47145, '', '', 'CIRCL', kind='operand', line=809)
W('22,3353', 0o02742, '', '', 'P', kind='operand', line=810)
W('22,3354', 0o45312, '', 'SL2', 'DSU', kind='interp', line=811)
W('22,3355', 0o33502, '', '', '1RTEB2', '1.B.2', kind='operand', line=812)
W('22,3356', 0o14017, '', 'STODL', '14D', kind='interp', line=813)
# Page 667
W('22,3357', 0o03752, '', '', 'RTSR1/MU', kind='operand', line=815)
W('22,3360', 0o56342, '', 'SR1', 'DDV', '(1/ROOTMU)/R1      B-16-B29 = B-45 PL02D', kind='interp', line=816)
W('22,3361', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=817)
W('22,3362', 0o02742, '', '', 'P', kind='operand', line=818)
W('22,3363', 0o00041, '', '', 'R1', kind='operand', line=819)
W('22,3364', 0o77624, '', 'CALL', kind='interp', line=820)
W('22,3365', 0o45263, '', '', 'SHIFTR1', kind='operand', line=821)
W('22,3366', 0o72412, '', 'SL4', 'SL1', kind='interp', line=822)
W('22,3367', 0o41366, '', 'SQRT', 'DMP', '((P/MU)**.5)/R1    B14+B-45 = B-31 PL02D', kind='interp', line=823)
W('22,3370', 0o52414, '', 'BOFF', 'SL3', kind='interp', line=824)
W('22,3371', 0o04343, '', '', 'CMOONFLG', kind='operand', line=825)
W('22,3372', 0o45373, '', '', 'CSI/B3', kind='operand', line=826)
W('22,3373', 0o50315, 'CSI/B3', 'PDVL', 'DOT', kind='interp', line=827)
W('22,3374', 0o02541, '', '', 'RACT1', kind='operand', line=828)
W('22,3375', 0o03474, '', '', 'VACT4', kind='operand', line=829)
W('22,3376', 0o03502, '', 'STORE', 'RDOTV', kind='interp', line=830)
W('22,3377', 0o77646, '', 'ABS', kind='interp', line=831)
W('22,3400', 0o41301, '', 'NORM', 'DMP', '((P/MU)**.5)RDOTV/R1               PL02D', kind='interp', line=832)
W('22,3401', 0o00050, '', '', 'X2', kind='operand', line=833)
W('22,3402', 0o53660, '', 'XSU,1', 'SL*', '                      B-31+B36-B3 = B2', kind='interp', line=834)
W('22,3403', 0o00047, '', '', 'X2', kind='operand', line=835)
W('22,3404', 0o20204, '', '', '3,1', kind='operand', line=836)
W('22,3405', 0o14015, '', 'STODL', '12D', kind='interp', line=837)
W('22,3406', 0o15335, '', '', 'ZEROVECS', kind='operand', line=838)
W('22,3407', 0o00021, '', 'STORE', '16D', kind='interp', line=839)
W('22,3410', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=840)
W('22,3411', 0o00015, '', '', '12D', kind='operand', line=841)
W('22,3412', 0o26732, '', 'STOVL', 'SNTH', 'ALSO STORES CSTH AND 0', kind='interp', line=842)
W('22,3413', 0o02541, '', '', 'RACT1', kind='operand', line=843)
W('22,3414', 0o75315, '', 'PDVL', 'SIGN', kind='interp', line=844)
W('22,3415', 0o03474, '', '', 'VACT4', kind='operand', line=845)
W('22,3416', 0o03502, '', '', 'RDOTV', kind='operand', line=846)
W('22,3417', 0o45076, '', 'VCOMP', 'CALL', kind='interp', line=847)
W('22,3420', 0o45253, '', '', 'VECSHIFT', kind='operand', line=848)
W('22,3421', 0o26746, '', 'STOVL', 'VVEC', kind='interp', line=849)
W('22,3422', 0o77614, '', 'SETGO', kind='interp', line=850)
W('22,3423', 0o03426, '', '', 'RVSW', kind='operand', line=851)
W('22,3424', 0o47134, '', '', 'CSINEXT', kind='operand', line=852)

W('22,3425', 0o77776, 'SN359+', '2DEC', '-.000086601', kind='data', line=854)
W('22,3426', 0o62460, kind='data', line=854)

W('22,3427', 0o17777, 'CS359+', '2DEC', '+.499999992', kind='data', line=856)
W('22,3430', 0o37776, kind='data', line=856)

#   SETLOC CSIPROG4
#   BANK

W('23,3134', 0o36657, 'CSINEXT', 'STCALL', 'RVEC', kind='interp', line=861)
W('23,3135', 0o24744, '', '', 'TIMETHET', kind='operand', line=862)
W('23,3136', 0o51125, '', 'PDDL', 'BPL', kind='interp', line=863)
W('23,3137', 0o03502, '', '', 'RDOTV', kind='operand', line=864)
# Page 668
W('23,3140', 0o47151, '', '', 'NTP/2', kind='operand', line=866)
W('23,3141', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=867)
W('23,3142', 0o03472, '', '', 'HAFPA1', kind='operand', line=868)
W('23,3143', 0o52006, '', 'PUSH', 'GOTO', kind='interp', line=869)
W('23,3144', 0o47151, '', '', 'NTP/2', kind='operand', line=870)
W('23,3145', 0o71201, 'CIRCL', 'SETPD', 'DLOAD', kind='interp', line=871)
W('23,3146', 0o00001, '', '', '00D', kind='operand', line=872)
W('23,3147', 0o15335, '', '', 'ZEROVECS', kind='operand', line=873)
W('23,3150', 0o77606, '', 'PUSH', kind='interp', line=874)
W('23,3151', 0o41345, 'NTP/2', 'DLOAD', 'DMP', kind='interp', line=875)
W('23,3152', 0o03766, '', '', 'NN', kind='operand', line=876)
W('23,3153', 0o03472, '', '', 'HAFPA1', kind='operand', line=877)
W('23,3154', 0o45261, '', 'SL', 'DSU', kind='interp', line=878)
W('23,3155', 0o20217, '', '', '14D', kind='operand', line=879)
W('23,3156', 0o77615, '', 'DAD', kind='interp', line=880)
W('23,3157', 0o02637, '', '', 'TCSI', kind='operand', line=881)
W('23,3160', 0o02635, '', 'STORE', 'TCDH', kind='interp', line=882)
W('23,3161', 0o77021, '', 'BDSU', 'AXT,2', kind='interp', line=883)
W('23,3162', 0o03663, '', '', 'TTPI', kind='operand', line=884)
W('23,3163', 0o00005, '', '', '5D', kind='operand', line=885)
W('23,3164', 0o40240, '', 'BMN', 'SETPD', kind='interp', line=886)
W('23,3165', 0o63642, '', '', 'SCNDSOL', kind='operand', line=887)
W('23,3166', 0o00001, '', '', '0D', kind='operand', line=888)
W('23,3167', 0o63375, '', 'VLOAD', 'PDVL', kind='interp', line=889)
W('23,3170', 0o03474, '', '', 'VACT4', kind='operand', line=890)
W('23,3171', 0o02541, '', '', 'RACT1', kind='operand', line=891)
W('23,3172', 0o77624, '', 'CALL', kind='interp', line=892)
W('23,3173', 0o63662, '', '', 'INTINT2C', kind='operand', line=893)
W('23,3174', 0o26453, '', 'STOVL', 'RACT2', kind='interp', line=894)
W('23,3175', 0o00007, '', '', 'VATT', kind='operand', line=895)
W('23,3176', 0o26533, '', 'STOVL', 'VACT2', kind='interp', line=896)
W('23,3177', 0o03512, '', '', 'VPASS1', kind='operand', line=897)
W('23,3200', 0o63201, '', 'SETPD', 'PDVL', kind='interp', line=898)
W('23,3201', 0o00001, '', '', '0D', kind='operand', line=899)
W('23,3202', 0o03756, '', '', 'RPASS1', kind='operand', line=900)
W('23,3203', 0o77650, '', 'GOTO', kind='interp', line=901)
W('23,3204', 0o22256, '', '', 'CSINEXT1', kind='operand', line=902)

#   SETLOC CSIPROG5
#   BANK

W('11,2256', 0o77624, 'CSINEXT1', 'CALL', kind='interp', line=907)
W('11,2257', 0o63662, '', '', 'INTINT2C', kind='operand', line=908)
W('11,2260', 0o26625, '', 'STOVL', 'RPASS2', kind='interp', line=909)
W('11,2261', 0o00007, '', '', 'VATT', kind='operand', line=910)
W('11,2262', 0o36617, '', 'STCALL', 'VPASS2', kind='interp', line=911)
W('11,2263', 0o13230, '', '', 'CDHMVR', kind='operand', line=912)
W('11,2264', 0o40375, '', 'VLOAD', 'SETPD', kind='interp', line=913)
W('11,2265', 0o02453, '', '', 'RACT2', kind='operand', line=914)
W('11,2266', 0o00001, '', '', '0D', kind='operand', line=915)
# Page 669
W('11,2267', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=917)
W('11,2270', 0o03546, '', '', 'VACT3', kind='operand', line=918)
W('11,2271', 0o45153, '', '', 'PERIAPO1', kind='operand', line=919)
W('11,2272', 0o77624, '', 'CALL', kind='interp', line=920)
W('11,2273', 0o45263, '', '', 'SHIFTR1', kind='operand', line=921)
W('11,2274', 0o27472, '', 'STOVL', 'POSTCDH', kind='interp', line=922)
W('11,2275', 0o03546, '', '', 'VACT3', kind='operand', line=923)
W('11,2276', 0o63201, '', 'SETPD', 'PDVL', kind='interp', line=924)
W('11,2277', 0o00001, '', '', '0D', kind='operand', line=925)
W('11,2300', 0o02453, '', '', 'RACT2', kind='operand', line=926)
W('11,2301', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=927)
W('11,2302', 0o02635, '', '', 'TCDH', kind='operand', line=928)
W('11,2303', 0o03663, '', '', 'TTPI', kind='operand', line=929)
W('11,2304', 0o62525, '', 'PDDL', 'SL2', kind='interp', line=930)
W('11,2305', 0o11630, '', '', '2PISC', kind='operand', line=931)
W('11,2306', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=932)
W('11,2307', 0o72705, '', '', 'INTINT', kind='operand', line=933)
W('11,2310', 0o77624, '', 'CALL', kind='interp', line=934)
W('11,2311', 0o45237, '', '', 'ACTIVE', kind='operand', line=935)
W('11,2312', 0o77745, '', 'DLOAD', kind='interp', line=936)
W('11,2313', 0o03744, '', '', 'ELEV', kind='operand', line=937)
W('11,2314', 0o73401, '', 'SETPD', 'SINE', kind='interp', line=938)
W('11,2315', 0o00007, '', '', '6D', kind='operand', line=939)
W('11,2316', 0o53515, '', 'PDVL', 'UNIT', kind='interp', line=940)
W('11,2317', 0o03540, '', '', 'RACT3', kind='operand', line=941)
W('11,2320', 0o00001, '', 'STORE', '00D', 'URA3 AT 00D', kind='interp', line=942)
W('11,2321', 0o47315, '', 'PDVL', 'VXV', 'PL14D,PL08D', kind='interp', line=943)
W('11,2322', 0o02611, '', '', 'UP1', kind='operand', line=944)
W('11,2323', 0o77656, '', 'UNIT', kind='interp', line=945)
W('11,2324', 0o71525, '', 'PDDL', 'COSINE', 'UNIT(URA3XUVA3XURA3) = UH3      B1 PL14D', kind='interp', line=946)
W('11,2325', 0o03744, '', '', 'ELEV', kind='operand', line=947)
W('11,2326', 0o45561, '', 'VXSC', 'STADR', '(COSLOS)(UH3)                   B2 PL08D', kind='interp', line=948)
W('11,2327', 0o43754, '', 'STCALL', '18D', '              PLUS', kind='interp', line=949)
W('11,2330', 0o16517, '', '', 'CSINEXT2', kind='operand', line=950)

#   SETLOC CSIPROG6
#   BANK

W('07,2517', 0o74345, 'CSINEXT2', 'DLOAD', 'VXSC', '(SINLOS)(URA3) = U              B2 PL00D', kind='interp', line=955)
W('07,2520', 0o76455, '', 'VAD', 'VSL1', kind='interp', line=956)
W('07,2521', 0o00023, '', '', '18D', '                                B1', kind='operand', line=957)
W('07,2522', 0o50206, '', 'PUSH', 'DOT', '                                   PL06D', kind='interp', line=958)
W('07,2523', 0o03540, '', '', 'RACT3', '(U . RA3) = TEMP1      B1 +B29=B30', kind='operand', line=959)
W('07,2524', 0o41552, '', 'SL1', 'PUSH', '                               B29 PL08D', kind='interp', line=960)
W('07,2525', 0o72316, '', 'DSQ', 'TLOAD', 'TEMP1**2                       B58', kind='interp', line=961)
W('07,2526', 0o00155, '', '', 'MPAC', kind='operand', line=962)
W('07,2527', 0o50315, '', 'PDVL', 'DOT', '                                   PL11D', kind='interp', line=963)
W('07,2530', 0o03540, '', '', 'RACT3', kind='operand', line=964)
W('07,2531', 0o03540, '', '', 'RACT3', kind='operand', line=965)
W('07,2532', 0o57551, '', 'TLOAD', 'DCOMP', 'RA3.RA3', kind='interp', line=966)
# Page 670
W('07,2533', 0o00155, '', '', 'MPAC', kind='operand', line=968)
W('07,2534', 0o50315, '', 'PDVL', 'DOT', 'RP3.RP3                        B58 PL14D', kind='interp', line=969)
W('07,2535', 0o03554, '', '', 'RPASS3', kind='operand', line=970)
W('07,2536', 0o03554, '', '', 'RPASS3', '                                   PL11D', kind='operand', line=971)
W('07,2537', 0o76371, '', 'TAD', 'TAD', 'TEMP1**2+RA3.RA3+RP3.RP3=TEMP2     PL08D', kind='interp', line=972)
W('07,2540', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=973)
W('07,2541', 0o16557, '', '', 'K10RK2', kind='operand', line=974)
W('07,2542', 0o03764, '', '', 'LOOPCT', kind='operand', line=975)
W('07,2543', 0o77025, '', 'DSU', 'AXT,2', kind='interp', line=976)
W('07,2544', 0o15675, '', '', '1DPB28', kind='operand', line=977)
W('07,2545', 0o00001, '', '', '1D', kind='operand', line=978)
W('07,2546', 0o77654, '', 'BZE', kind='interp', line=979)
W('07,2547', 0o11314, '', '', 'ALMXITA', kind='operand', line=980)
W('07,2550', 0o70545, '', 'DLOAD', 'SR1', kind='interp', line=981)
W('07,2551', 0o03464, '', '', 'DELDV', kind='operand', line=982)
W('07,2552', 0o03464, '', 'STORE', 'DELDV', kind='interp', line=983)
W('07,2553', 0o77621, '', 'BDSU', kind='interp', line=984)
W('07,2554', 0o03470, '', '', 'DVPREV', kind='operand', line=985)
W('07,2555', 0o37462, '', 'STCALL', 'DELVCSI', kind='interp', line=986)
W('07,2556', 0o15756, '', '', 'CSI/B1', kind='operand', line=987)
W('07,2557', 0o41566, 'K10RK2', 'SQRT', 'PUSH', 'TEMP3 = TEMP2**.5              B29 PL10D', kind='interp', line=988)
W('07,2560', 0o45276, '', 'DCOMP', 'DSU', kind='interp', line=989)
W('07,2561', 0o00007, '', '', '06D', '-TEMP1-TEMP3 =K2 AT 10D', kind='operand', line=990)
W('07,2562', 0o14013, '', 'STODL', '10D', '                                   PL08D', kind='interp', line=991)
W('07,2563', 0o45425, '', 'DSU', 'STADR', '                                   PL06D', kind='interp', line=992)
W('07,2564', 0o77762, '', 'STORE', '12D', '-TEMP1+TEMP3 =K1 AT 12D', kind='interp', line=993)
W('07,2565', 0o77646, '', 'ABS', kind='interp', line=994)
W('07,2566', 0o14017, '', 'STODL', '14D', kind='interp', line=995)
W('07,2567', 0o00013, '', '', '10D', kind='operand', line=996)
W('07,2570', 0o45246, '', 'ABS', 'DSU', kind='interp', line=997)
W('07,2571', 0o00017, '', '', '14D', kind='operand', line=998)
W('07,2572', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=999)
W('07,2573', 0o50002, '', '', 'K2.', kind='operand', line=1000)
W('07,2574', 0o00015, '', '', '12D', kind='operand', line=1001)
W('07,2575', 0o34013, '', 'STCALL', '10D', 'K EQUALS K1', kind='interp', line=1002)
W('07,2576', 0o50002, '', '', 'K2.', kind='operand', line=1003)

#   SETLOC CSIPROG7
#   BANK

W('24,2002', 0o77745, 'K2.', 'DLOAD', kind='interp', line=1008)
W('24,2003', 0o00013, '', '', '10D', kind='operand', line=1009)
W('24,2004', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=1010)
W('24,2005', 0o53455, '', 'VAD', 'UNIT', 'V=RA3+KU  UNIT                  B1', kind='interp', line=1011)
W('24,2006', 0o03540, '', '', 'RACT3', kind='operand', line=1012)
W('24,2007', 0o53515, '', 'PDVL', 'UNIT', '                                   PL06D', kind='interp', line=1013)
W('24,2010', 0o03554, '', '', 'RPASS3', kind='operand', line=1014)
W('24,2011', 0o53515, '', 'PDVL', 'UNIT', '                                   PL12D', kind='interp', line=1015)
W('24,2012', 0o03562, '', '', 'VPASS3', kind='operand', line=1016)
W('24,2013', 0o63235, '', 'VXV', 'PDVL', 'UVP3 X URP3                        PL18D', kind='interp', line=1017)
# Page 671
W('24,2014', 0o00007, '', '', '06D', kind='operand', line=1019)
W('24,2015', 0o00007, '', '', '06D', kind='operand', line=1020)
W('24,2016', 0o50235, '', 'VXV', 'DOT', kind='interp', line=1021)
W('24,2017', 0o00001, '', '', '00D', kind='operand', line=1022)
W('24,2020', 0o77626, '', 'STADR', '', '                                   PL12D', kind='interp', line=1023)
W('24,2021', 0o53762, '', 'STOVL', '12D', '(URP3XV).(UVP3XURP3)=TEMP          PL06D', kind='interp', line=1024)
W('24,2022', 0o72441, '', 'DOT', 'SL1', '                                   PL00D', kind='interp', line=1025)
W('24,2023', 0o75326, '', 'ARCCOS', 'SIGN', kind='interp', line=1026)
W('24,2024', 0o00015, '', '', '12D', '                                B0', kind='operand', line=1027)
W('24,2025', 0o41542, '', 'SR1', 'PUSH', 'GAMMA=SIGN(TEMP)ARCOS(UNITV.URP3)  PL02D', kind='interp', line=1028)
W('24,2026', 0o71214, '', 'BON', 'DLOAD', kind='interp', line=1029)
W('24,2027', 0o05701, '', '', 'S32.1F2', kind='operand', line=1030)
W('24,2030', 0o50065, '', '', 'FRSTPAS', kind='operand', line=1031)
W('24,2031', 0o00001, '', '', '00D', 'NOT THE FIRST PASS OF A CYCLE', kind='operand', line=1032)
W('24,2032', 0o65225, '', 'DSU', 'PDDL', 'GAMMA-GAMPREV                   B1 PL04D', kind='interp', line=1033)
W('24,2033', 0o03466, '', '', 'GAMPREV', kind='operand', line=1034)
W('24,2034', 0o03462, '', '', 'DELVCSI', kind='operand', line=1035)
W('24,2035', 0o60225, '', 'DSU', 'NORM', '                                B7', kind='interp', line=1036)
W('24,2036', 0o03470, '', '', 'DVPREV', kind='operand', line=1037)
W('24,2037', 0o00047, '', '', 'X1', kind='operand', line=1038)
W('24,2040', 0o65265, '', 'BDDV', 'PDDL', '(GAM-GAMPREV)/(DV-DVPREV)   B-6+N1 PL06D', kind='interp', line=1039)
W('24,2041', 0o00003, '', '', '02D', '      = SLOPE', kind='operand', line=1040)
W('24,2042', 0o03462, '', '', 'DELVCSI', kind='operand', line=1041)
W('24,2043', 0o03470, '', 'STORE', 'DVPREV', kind='interp', line=1042)
W('24,2044', 0o43014, '', 'BOFF', 'BOFF', kind='interp', line=1043)
W('24,2045', 0o05742, '', '', 'S32.1F3A', kind='operand', line=1044)
W('24,2046', 0o20307, '', '', 'THRDCHK', kind='operand', line=1045)
W('24,2047', 0o05743, '', '', 'S32.1F3B', kind='operand', line=1046)
W('24,2050', 0o20307, '', '', 'THRDCHK', kind='operand', line=1047)
W('24,2051', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=1048)
W('24,2052', 0o00003, '', '', '02D', kind='operand', line=1049)
W('24,2053', 0o03466, '', '', 'GAMPREV', kind='operand', line=1050)
W('24,2054', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=1051)
W('24,2055', 0o20314, '', '', 'FIFTYFPS', kind='operand', line=1052)
W('24,2056', 0o33452, '', '', 'INITST1', kind='operand', line=1053)
W('24,2057', 0o77765, '', 'SIGN', kind='interp', line=1054)
W('24,2060', 0o03464, '', '', 'DELDV', kind='operand', line=1055)
W('24,2061', 0o03464, '', 'STORE', 'DELDV', kind='interp', line=1056)
W('24,2062', 0o43014, '', 'SET', 'CLEAR', kind='interp', line=1057)
W('24,2063', 0o05462, '', '', 'S32.1F3A', kind='operand', line=1058)
W('24,2064', 0o05663, '', '', 'S32.1F3B', kind='operand', line=1059)
W('24,2065', 0o77745, 'FRSTPAS', 'DLOAD', kind='interp', line=1060)
W('24,2066', 0o00001, '', '', '00D', kind='operand', line=1061)
W('24,2067', 0o17466, '', 'STODL', 'GAMPREV', kind='interp', line=1062)
W('24,2070', 0o03462, '', '', 'DELVCSI', kind='operand', line=1063)
W('24,2071', 0o37470, '', 'STCALL', 'DVPREV', kind='interp', line=1064)
W('24,2072', 0o20302, '', '', 'CSINEXT3', kind='operand', line=1065)

#   SETLOC CSIPROG8
#   BANK
# Page 672
W('10,2302', 0o43025, 'CSINEXT3', 'DSU', 'CLEAR', kind='interp', line=1070)
W('10,2303', 0o03464, '', '', 'DELDV', kind='operand', line=1071)
W('10,2304', 0o05661, '', '', 'S32.1F2', kind='operand', line=1072)
W('10,2305', 0o37462, '', 'STCALL', 'DELVCSI', kind='interp', line=1073)
W('10,2306', 0o15756, '', '', 'CSI/B1', kind='operand', line=1074)
W('10,2307', 0o43014, 'THRDCHK', 'BON', 'BON', kind='interp', line=1075)
W('10,2310', 0o05702, '', '', 'S32.1F3A', kind='operand', line=1076)
W('10,2311', 0o20333, '', '', 'NEWTN', kind='operand', line=1077)
W('10,2312', 0o05703, '', '', 'S32.1F3B', kind='operand', line=1078)
W('10,2313', 0o20333, '', '', 'NEWTN', kind='operand', line=1079)
W('10,2314', 0o75345, 'FIFTYFPS', 'DLOAD', 'SIGN', kind='interp', line=1080)
W('10,2315', 0o15701, '', '', 'FIFPSDP', kind='operand', line=1081)
W('10,2316', 0o00005, '', '', '04D', kind='operand', line=1082)
W('10,2317', 0o77765, '', 'SIGN', kind='interp', line=1083)
W('10,2320', 0o03466, '', '', 'GAMPREV', kind='operand', line=1084)
W('10,2321', 0o03464, '', 'STORE', 'DELDV', kind='interp', line=1085)
W('10,2322', 0o43276, '', 'DCOMP', 'DAD', kind='interp', line=1086)
W('10,2323', 0o03462, '', '', 'DELVCSI', kind='operand', line=1087)
W('10,2324', 0o17462, '', 'STODL', 'DELVCSI', kind='interp', line=1088)
W('10,2325', 0o00001, '', '', '00D', kind='operand', line=1089)
W('10,2326', 0o43014, '', 'SET', 'SET', kind='interp', line=1090)
W('10,2327', 0o05463, '', '', 'S32.1F3B', kind='operand', line=1091)
W('10,2330', 0o05462, '', '', 'S32.1F3A', kind='operand', line=1092)
W('10,2331', 0o37466, '', 'STCALL', 'GAMPREV', kind='interp', line=1093)
W('10,2332', 0o24013, '', '', 'CSI/B2', kind='operand', line=1094)
W('10,2333', 0o60345, 'NEWTN', 'DLOAD', 'NORM', kind='interp', line=1095)
W('10,2334', 0o00005, '', '', '04D', kind='operand', line=1096)
W('10,2335', 0o00050, '', '', 'X2', kind='operand', line=1097)
W('10,2336', 0o54065, '', 'BDDV', 'XSU,1', kind='interp', line=1098)
W('10,2337', 0o00001, '', '', '00D', kind='operand', line=1099)
W('10,2340', 0o00047, '', '', 'X2', kind='operand', line=1100)
W('10,2341', 0o77657, '', 'SR*', kind='interp', line=1101)
W('10,2342', 0o20601, '', '', '0,1', kind='operand', line=1102)
W('10,2343', 0o17464, '', 'STODL', 'DELDV', kind='interp', line=1103)
W('10,2344', 0o00001, '', '', '00D', kind='operand', line=1104)
W('10,2345', 0o03466, '', 'STORE', 'GAMPREV', kind='interp', line=1105)
W('10,2346', 0o51545, '', 'DLOAD', 'ABS', kind='interp', line=1106)
W('10,2347', 0o03464, '', '', 'DELDV', kind='operand', line=1107)
W('10,2350', 0o45206, '', 'PUSH', 'DSU', '                                   PL08D', kind='interp', line=1108)
W('10,2351', 0o15677, '', '', 'EPSILN1', kind='operand', line=1109)
W('10,2352', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=1110)
W('10,2353', 0o20370, '', '', 'CSI/SOL', kind='operand', line=1111)
W('10,2354', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1112)
W('10,2355', 0o15703, '', '', 'DELMAX1', kind='operand', line=1113)
W('10,2356', 0o20363, '', '', 'CSISTEP', kind='operand', line=1114)
W('10,2357', 0o75345, '', 'DLOAD', 'SIGN', kind='interp', line=1115)
W('10,2360', 0o15703, '', '', 'DELMAX1', kind='operand', line=1116)
W('10,2361', 0o03464, '', '', 'DELDV', kind='operand', line=1117)
W('10,2362', 0o03464, '', 'STORE', 'DELDV', kind='interp', line=1118)
W('10,2363', 0o45345, 'CSISTEP', 'DLOAD', 'DSU', kind='interp', line=1119)
# Page 673
W('10,2364', 0o03462, '', '', 'DELVCSI', kind='operand', line=1121)
W('10,2365', 0o03464, '', '', 'DELDV', kind='operand', line=1122)
W('10,2366', 0o37462, '', 'STCALL', 'DELVCSI', kind='interp', line=1123)
W('10,2367', 0o15756, '', '', 'CSI/B1', kind='operand', line=1124)
W('10,2370', 0o77145, 'CSI/SOL', 'DLOAD', 'AXT,2', kind='interp', line=1125)
W('10,2371', 0o03460, '', '', 'POSTCSI', kind='operand', line=1126)
W('10,2372', 0o00002, '', '', '2', kind='operand', line=1127)
W('10,2373', 0o52150, '', 'LXA,1', 'GOTO', kind='interp', line=1128)
W('10,2374', 0o03745, '', '', 'RTX1', kind='operand', line=1129)
W('10,2375', 0o63610, '', '', 'CSINEXT4', kind='operand', line=1130)

#   SETLOC CSIPROG9
#   BANK

W('31,3610', 0o50023, 'CSINEXT4', 'DSU*', 'BMN', kind='interp', line=1135)
W('31,3611', 0o33444, '', '', 'PMINE -2,1', kind='operand', line=1136)
W('31,3612', 0o63642, '', '', 'SCNDSOL', kind='operand', line=1137)
W('31,3613', 0o71374, '', 'AXT,2', 'DLOAD', kind='interp', line=1138)
W('31,3614', 0o00003, '', '', '3', kind='operand', line=1139)
W('31,3615', 0o03472, '', '', 'POSTCDH', kind='operand', line=1140)
W('31,3616', 0o50023, '', 'DSU*', 'BMN', kind='interp', line=1141)
W('31,3617', 0o33444, '', '', 'PMINE -2,1', kind='operand', line=1142)
W('31,3620', 0o63642, '', '', 'SCNDSOL', kind='operand', line=1143)
W('31,3621', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=1144)
W('31,3622', 0o02635, '', '', 'TCDH', kind='operand', line=1145)
W('31,3623', 0o02637, '', '', 'TCSI', kind='operand', line=1146)
W('31,3624', 0o02547, '', 'STORE', 'T1TOT2', kind='interp', line=1147)
W('31,3625', 0o45374, '', 'AXT,2', 'DSU', kind='interp', line=1148)
W('31,3626', 0o00004, '', '', '4', kind='operand', line=1149)
W('31,3627', 0o36146, '', '', '600SEC', kind='operand', line=1150)
W('31,3630', 0o77040, '', 'BMN', 'AXT,2', kind='interp', line=1151)
W('31,3631', 0o63642, '', '', 'SCNDSOL', kind='operand', line=1152)
W('31,3632', 0o00005, '', '', '5', kind='operand', line=1153)
W('31,3633', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=1154)
W('31,3634', 0o03663, '', '', 'TTPI', kind='operand', line=1155)
W('31,3635', 0o02635, '', '', 'TCDH', kind='operand', line=1156)
W('31,3636', 0o03656, '', 'STORE', 'T2TOT3', kind='interp', line=1157)
W('31,3637', 0o51025, '', 'DSU', 'BPL', kind='interp', line=1158)
W('31,3640', 0o36146, '', '', '600SEC', kind='operand', line=1159)
W('31,3641', 0o11400, '', '', 'P32/P72C', kind='operand', line=1160)
W('31,3642', 0o43014, 'SCNDSOL', 'BON', 'BOFF', kind='interp', line=1161)
W('31,3643', 0o05702, '', '', 'S32.1F3A', kind='operand', line=1162)
W('31,3644', 0o11316, '', '', 'ALMXIT', kind='operand', line=1163)
W('31,3645', 0o05743, '', '', 'S32.1F3B', kind='operand', line=1164)
W('31,3646', 0o11316, '', '', 'ALMXIT', kind='operand', line=1165)
W('31,3647', 0o71334, '', 'SXA,2', 'DLOAD', kind='interp', line=1166)
W('31,3650', 0o03664, '', '', 'CSIALRM', kind='operand', line=1167)
W('31,3651', 0o15335, '', '', 'ZEROVECS', kind='operand', line=1168)
W('31,3652', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=1169)
W('31,3653', 0o05660, '', '', 'S32.1F1', kind='operand', line=1170)
# Page 674
W('31,3654', 0o05461, '', '', 'S32.1F2', kind='operand', line=1172)
W('31,3655', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=1173)
W('31,3656', 0o05662, '', '', 'S32.1F3A', kind='operand', line=1174)
W('31,3657', 0o05663, '', '', 'S32.1F3B', kind='operand', line=1175)
W('31,3660', 0o37764, '', 'STCALL', 'LOOPCT', kind='interp', line=1176)
W('31,3661', 0o15716, '', '', 'CSI/B', kind='operand', line=1177)
# Page 675
# ..... ADVANCE .....

# SUBROUTINES USED

# PRECSET
# ROTATE

#   SETLOC CDHTAG3
#   BANK

W('37,2645', 0o71220, 'ADVANCE', 'STQ', 'DLOAD', kind='interp', line=1189)
W('37,2646', 0o02370, '', '', 'SUBEXIT', kind='operand', line=1190)
W('37,2647', 0o03413, '', '', 'TIG', kind='operand', line=1191)
W('37,2650', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1192)
W('37,2651', 0o45215, '', '', 'PRECSET', kind='operand', line=1193)
W('37,2652', 0o77214, '', 'SET', 'VLOAD', kind='interp', line=1194)
W('37,2653', 0o01067, '', '', 'XDELVFLG', kind='operand', line=1195)
W('37,2654', 0o03562, '', '', 'VPASS3', kind='operand', line=1196)
W('37,2655', 0o02617, '', 'STORE', 'VPASS2', kind='interp', line=1197)
W('37,2656', 0o27512, '', 'STOVL', 'VPASS1', kind='interp', line=1198)
W('37,2657', 0o03554, '', '', 'RPASS3', kind='operand', line=1199)
W('37,2660', 0o02625, '', 'STORE', 'RPASS2', kind='interp', line=1200)
W('37,2661', 0o03756, '', 'STORE', 'RPASS1', kind='interp', line=1201)
W('37,2662', 0o47256, '', 'UNIT', 'VXV', kind='interp', line=1202)
W('37,2663', 0o03512, '', '', 'VPASS1', kind='operand', line=1203)
W('37,2664', 0o77656, '', 'UNIT', kind='interp', line=1204)
W('37,2665', 0o26611, '', 'STOVL', 'UP1', kind='interp', line=1205)
W('37,2666', 0o03540, '', '', 'RACT3', kind='operand', line=1206)
W('37,2667', 0o37632, '', 'STCALL', 'RTIG', kind='interp', line=1207)
W('37,2670', 0o13220, '', '', 'ROTATE', kind='operand', line=1208)
W('37,2671', 0o02453, '', 'STORE', 'RACT2', kind='interp', line=1209)
W('37,2672', 0o26541, '', 'STOVL', 'RACT1', kind='interp', line=1210)
W('37,2673', 0o03546, '', '', 'VACT3', kind='operand', line=1211)
W('37,2674', 0o37640, '', 'STCALL', 'VTIG', kind='interp', line=1212)
W('37,2675', 0o13220, '', '', 'ROTATE', kind='operand', line=1213)
W('37,2676', 0o02533, '', 'STORE', 'VACT2', kind='interp', line=1214)
W('37,2677', 0o37504, '', 'STCALL', 'VACT1', kind='interp', line=1215)
W('37,2700', 0o02370, '', '', 'SUBEXIT', kind='operand', line=1216)
# Page 676
# ..... ROTATE .....

#   SETLOC CDHTAG
#   BANK

W('05,3220', 0o41406, 'ROTATE', 'PUSH', 'PUSH', kind='interp', line=1223)
W('05,3221', 0o74241, '', 'DOT', 'VXSC', kind='interp', line=1224)
W('05,3222', 0o02611, '', '', 'UP1', kind='operand', line=1225)
W('05,3223', 0o02611, '', '', 'UP1', kind='operand', line=1226)
W('05,3224', 0o51352, '', 'VSL2', 'BVSU', kind='interp', line=1227)
W('05,3225', 0o63256, '', 'UNIT', 'PDVL', kind='interp', line=1228)
W('05,3226', 0o74246, '', 'ABVAL', 'VXSC', kind='interp', line=1229)
W('05,3227', 0o43572, '', 'VSL1', 'RVQ', kind='interp', line=1230)
# Page 677
# ..... INTINTNA .....

#   SETLOC CDHTAG2
#   BANK

W('31,3662', 0o65325, 'INTINT2C', 'PDDL', 'PDDL', kind='interp', line=1237)
W('31,3663', 0o02637, '', '', 'TCSI', kind='operand', line=1238)
W('31,3664', 0o02635, '', '', 'TCDH', kind='operand', line=1239)
W('31,3665', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=1240)
W('31,3666', 0o33107, '', '', 'TWOPI', kind='operand', line=1241)
W('31,3667', 0o77650, '', 'GOTO', kind='interp', line=1242)
W('31,3670', 0o72705, '', '', 'INTINT', kind='operand', line=1243)
W('31,3671', 0o65325, 'INTINT3P', 'PDDL', 'PDDL', kind='interp', line=1244)
W('31,3672', 0o02635, '', '', 'TCDH', kind='operand', line=1245)
W('31,3673', 0o03663, '', '', 'TTPI', kind='operand', line=1246)
W('31,3674', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=1247)
W('31,3675', 0o15335, '', '', 'ZEROVECS', kind='operand', line=1248)
W('31,3676', 0o77650, '', 'GOTO', kind='interp', line=1249)
W('31,3677', 0o72705, '', '', 'INTINT', kind='operand', line=1250)
# Page 678
# ..... S32/33.1 .....

# SUBROUTINES USED
# S32/33.X

#   SETLOC CSI/CDH
#   BANK

W('35,3457', 0o76020, 'S32/33.1', 'STQ', 'AXT,1', kind='interp', line=1260)
W('35,3460', 0o02370, '', '', 'SUBEXIT', kind='operand', line=1261)
W('35,3461', 0o01521, '', 'VN', '0681', kind='data', line=1262)
W('35,3462', 0o77624, '', 'CALL', kind='interp', line=1263)
W('35,3463', 0o76625, '', '', 'DISDVLVC', kind='operand', line=1264)
W('35,3464', 0o77624, '', 'CALL', kind='interp', line=1265)
W('35,3465', 0o26231, '', '', 'S32/33.X', kind='operand', line=1266)
W('35,3466', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=1267)
W('35,3467', 0o03405, '', '', 'DELVLVC', kind='operand', line=1268)
W('35,3470', 0o00001, '', '', '0D', kind='operand', line=1269)
W('35,3471', 0o77772, '', 'VSL1', kind='interp', line=1270)
W('35,3472', 0o03646, '', 'STORE', 'DELVSIN', kind='interp', line=1271)
W('35,3473', 0o51406, '', 'PUSH', 'ABVAL', kind='interp', line=1272)
W('35,3474', 0o27654, '', 'STOVL', 'DELVSAB', kind='interp', line=1273)
W('35,3475', 0o77650, '', 'GOTO', kind='interp', line=1274)
W('35,3476', 0o02370, '', '', 'SUBEXIT', kind='operand', line=1275)
# Page 679
# ..... S32/33.X .....

#   SETLOC CDHTAGS
#   BANK

W('13,2231', 0o77201, 'S32/33.X', 'SETPD', 'VLOAD', kind='interp', line=1282)
W('13,2232', 0o00007, '', '', '6D', kind='operand', line=1283)
W('13,2233', 0o02611, '', '', 'UP1', kind='operand', line=1284)
W('13,2234', 0o63276, '', 'VCOMP', 'PDVL', kind='interp', line=1285)
W('13,2235', 0o02541, '', '', 'RACT1', kind='operand', line=1286)
W('13,2236', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=1287)
W('13,2237', 0o47206, '', 'PUSH', 'VXV', kind='interp', line=1288)
W('13,2240', 0o02611, '', '', 'UP1', kind='operand', line=1289)
W('13,2241', 0o77772, '', 'VSL1', kind='interp', line=1290)
W('13,2242', 0o00001, '', 'STORE', '0D', kind='interp', line=1291)
W('13,2243', 0o77616, '', 'RVQ', kind='interp', line=1292)
# Page 680
# ..... CDHMVR .....

# SUBROUTINES USED

# VECSHIFT
# TIMETHET
# SHIFTR1

#   SETLOC CDHTAG
#   BANK

W('05,3230', 0o77220, 'CDHMVR', 'STQ', 'VLOAD', kind='interp', line=1305)
W('05,3231', 0o02370, '', '', 'SUBEXIT', kind='operand', line=1306)
W('05,3232', 0o02453, '', '', 'RACT2', kind='operand', line=1307)
W('05,3233', 0o53406, '', 'PUSH', 'UNIT', kind='interp', line=1308)
W('05,3234', 0o27546, '', 'STOVL', 'UNVEC', 'UR SUB A', kind='interp', line=1309)
W('05,3235', 0o02625, '', '', 'RPASS2', kind='operand', line=1310)
W('05,3236', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=1311)
W('05,3237', 0o03546, '', '', 'UNVEC', kind='operand', line=1312)
W('05,3240', 0o72406, '', 'PUSH', 'SL1', kind='interp', line=1313)
W('05,3241', 0o16734, '', 'STODL', 'CSTH', kind='interp', line=1314)
W('05,3242', 0o65316, '', 'DSQ', 'PDDL', kind='interp', line=1315)
W('05,3243', 0o23756, '', '', 'DP1/4', kind='operand', line=1316)
W('05,3244', 0o45302, '', 'SR2', 'DSU', kind='interp', line=1317)
W('05,3245', 0o72566, '', 'SQRT', 'SL1', kind='interp', line=1318)
W('05,3246', 0o57515, '', 'PDVL', 'VCOMP', kind='interp', line=1319)
W('05,3247', 0o77635, '', 'VXV', kind='interp', line=1320)
W('05,3250', 0o02625, '', '', 'RPASS2', kind='operand', line=1321)
W('05,3251', 0o65241, '', 'DOT', 'PDDL', kind='interp', line=1322)
W('05,3252', 0o02611, '', '', 'UP1', kind='operand', line=1323)
W('05,3253', 0o45565, '', 'SIGN', 'STADR', kind='interp', line=1324)
W('05,3254', 0o51045, '', 'STOVL', 'SNTH', kind='interp', line=1325)
W('05,3255', 0o02625, '', '', 'RPASS2', kind='operand', line=1326)
W('05,3256', 0o45115, '', 'PDVL', 'CALL', kind='interp', line=1327)
W('05,3257', 0o02617, '', '', 'VPASS2', kind='operand', line=1328)
W('05,3260', 0o45253, '', '', 'VECSHIFT', kind='operand', line=1329)
W('05,3261', 0o26746, '', 'STOVL', 'VVEC', kind='interp', line=1330)
W('05,3262', 0o77614, '', 'CLEAR', kind='interp', line=1331)
W('05,3263', 0o03666, '', '', 'RVSW', kind='operand', line=1332)
W('05,3264', 0o36657, '', 'STCALL', 'RVEC', kind='interp', line=1333)
W('05,3265', 0o24744, '', '', 'TIMETHET', kind='operand', line=1334)
W('05,3266', 0o53754, '', 'LXA,2', 'VSL*', kind='interp', line=1335)
W('05,3267', 0o03746, '', '', 'RTX2', kind='operand', line=1336)
W('05,3270', 0o57576, '', '', '0,2', kind='operand', line=1337)
W('05,3271', 0o00023, '', 'STORE', '18D', kind='interp', line=1338)
W('05,3272', 0o76441, '', 'DOT', 'SL1R', kind='interp', line=1339)
W('05,3273', 0o03546, '', '', 'UNVEC', kind='operand', line=1340)
W('05,3274', 0o51515, '', 'PDVL', 'ABVAL', '0D = V SUB PV', kind='interp', line=1341)
W('05,3275', 0o63257, '', 'SL*', 'PDVL', kind='interp', line=1342)
W('05,3276', 0o57576, '', '', '0,2', kind='operand', line=1343)
# Page 681
W('05,3277', 0o02453, '', '', 'RACT2', kind='operand', line=1345)
W('05,3300', 0o65246, '', 'ABVAL', 'PDDL', '2D = LENGTH OF R SUB A', kind='interp', line=1346)
W('05,3301', 0o77625, '', 'DSU', kind='interp', line=1347)
W('05,3302', 0o00003, '', '', '02D', kind='operand', line=1348)
W('05,3303', 0o16633, '', 'STODL', 'DIFFALT', 'DELTA H IN METERS             B+29', kind='interp', line=1349)
W('05,3304', 0o02744, '', '', 'R1A', kind='operand', line=1350)
W('05,3305', 0o65301, '', 'NORM', 'PDDL', '2 - R V**/MU                          04D', kind='interp', line=1351)
W('05,3306', 0o00047, '', '', 'X1', kind='operand', line=1352)
W('05,3307', 0o00041, '', '', 'R1', kind='operand', line=1353)
W('05,3310', 0o77624, '', 'CALL', kind='interp', line=1354)
W('05,3311', 0o45263, '', '', 'SHIFTR1', kind='operand', line=1355)
W('05,3312', 0o56362, '', 'SR1R', 'DDV', kind='interp', line=1356)
W('05,3313', 0o41457, '', 'SL*', 'PUSH', kind='interp', line=1357)
W('05,3314', 0o20174, '', '', '0 -5,1', kind='operand', line=1358)
W('05,3315', 0o65225, '', 'DSU', 'PDDL', 'A SUB A                       B+29    04D', kind='interp', line=1359)
W('05,3316', 0o02633, '', '', 'DIFFALT', kind='operand', line=1360)
W('05,3317', 0o56302, '', 'SR2', 'DDV', 'A SUB P                       B+31', kind='interp', line=1361)
W('05,3320', 0o00005, '', '', '04D', '                              B+2', kind='operand', line=1362)
W('05,3321', 0o75406, '', 'PUSH', 'SQRT', 'A SUB P/A SUB A                       06D', kind='interp', line=1363)
W('05,3322', 0o41275, '', 'DMPR', 'DMP', kind='interp', line=1364)
W('05,3323', 0o00007, '', '', '06D', kind='operand', line=1365)
W('05,3324', 0o00001, '', '', '00D', kind='operand', line=1366)
W('05,3325', 0o65272, '', 'SL3R', 'PDDL', 'V SUB A V METERS/CS           B+7     08D', kind='interp', line=1367)
W('05,3326', 0o00003, '', '', '02D', 'R SUB A MAGNITUDE             B+29', kind='operand', line=1368)
W('05,3327', 0o65301, '', 'NORM', 'PDDL', kind='interp', line=1369)
W('05,3330', 0o00047, '', '', 'X1', kind='operand', line=1370)
W('05,3331', 0o03750, '', '', 'RTMU', kind='operand', line=1371)
W('05,3332', 0o56342, '', 'SR1', 'DDV', '2MU                           B+38', kind='interp', line=1372)
W('05,3333', 0o65257, '', 'SL*', 'PDDL', '2 MU/R SUBAA                  B+14    10D', kind='interp', line=1373)
W('05,3334', 0o20174, '', '', '0 -5,1', kind='operand', line=1374)
W('05,3335', 0o00005, '', '', '04D', 'ASUBA                         B+29', kind='operand', line=1375)
W('05,3336', 0o65301, '', 'NORM', 'PDDL', kind='interp', line=1376)
W('05,3337', 0o00050, '', '', 'X2', kind='operand', line=1377)
W('05,3340', 0o03750, '', '', 'RTMU', kind='operand', line=1378)
W('05,3341', 0o56342, '', 'SR1', 'DDV', kind='interp', line=1379)
W('05,3342', 0o44257, '', 'SL*', 'BDSU', kind='interp', line=1380)
W('05,3343', 0o57604, '', '', '0 -6,2', '2U/R - U/A             B+14 (METERS/CS)SQ', kind='operand', line=1381)
W('05,3344', 0o63525, '', 'PDDL', 'DSQ', '                                      10D', kind='interp', line=1382)
W('05,3345', 0o00011, '', '', '08D', kind='operand', line=1383)
W('05,3346', 0o75421, '', 'BDSU', 'SQRT', kind='interp', line=1384)
W('05,3347', 0o47315, '', 'PDVL', 'VXV', 'SQRT(MU(2/R SUB A-1/A SUB A)-VSUBA2)  10D', kind='interp', line=1385)
W('05,3350', 0o02611, '', '', 'UP1', kind='operand', line=1386)
W('05,3351', 0o03546, '', '', 'UNVEC', kind='operand', line=1387)
W('05,3352', 0o74256, '', 'UNIT', 'VXSC', kind='interp', line=1388)
W('05,3353', 0o00013, '', '', '10D', kind='operand', line=1389)
W('05,3354', 0o74315, '', 'PDVL', 'VXSC', kind='interp', line=1390)
W('05,3355', 0o03546, '', '', 'UNVEC', kind='operand', line=1391)
W('05,3356', 0o00011, '', '', '08D', kind='operand', line=1392)
W('05,3357', 0o76455, '', 'VAD', 'VSL1', kind='interp', line=1393)
W('05,3360', 0o77626, '', 'STADR', kind='interp', line=1394)
# Page 682
W('05,3361', 0o74231, '', 'STORE', 'VACT3', kind='interp', line=1396)
W('05,3362', 0o77651, '', 'VSU', kind='interp', line=1397)
W('05,3363', 0o02533, '', '', 'VACT2', kind='operand', line=1398)
W('05,3364', 0o37667, '', 'STCALL', 'DELVEET2', 'DELTA VCDH - REFERENCE COORDINATES', kind='interp', line=1399)
W('05,3365', 0o02370, '', '', 'SUBEXIT', kind='operand', line=1400)
# Page 683
# ..... COMPTGO .....

# SUBROUTINES USED

# CLOKTASK
# 2PHSCHNG

#   BANK 35
#   SETLOC CSI/CDH
#   BANK

#   EBANK= RTRN

#   COUNT* $$/P3575
