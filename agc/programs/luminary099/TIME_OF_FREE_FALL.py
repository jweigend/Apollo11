"""TIME_OF_FREE_FALL.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/TIME_OF_FREE_FALL.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1268-1283 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TIME_OF_FREE_FALL', 'TIME_OF_FREE_FALL.agc', 'Luminary099', pages='1268-1283')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TIME_OF_FREE_FALL.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1268-1283
# Mod history:  2009-05-26 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2011-01-06 JL   Fixed pseudo-label indentation.
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

# Page 1268
# THE TFF SUBROUTINES MAY BE USED IN EITHER EARTH OR MOON CENTERED COORDINATES.  THE TFF ROUTINES NEVER
# KNOW WHICH ORIGIN APPLIES.  IT IS THE USER WHO KNOWS, AND WHO SUPPLIES RONE, VONE, AND 1/SQRT(MU) AT THE
# APPROPRIATE SCALE LEVEL FOR THE PROPER PRIMARY BODY.
#
# EARTH ORIGIN    POSITION        -29     METERS
# VELOCITY        -7      METERS/CENTISECOND
# 1/SQRT(MU)      +17     SQRT(CS SQ/METERS CUBED)
#
# MOON ORIGIN     POSITION        -27     METERS
# VELOCITY        -5      METERS/CENTISECONDS
# 1/SQRT(MU)      +14     SQRT(CS SQ/METERS CUBED)
#
# ALL DATA PROVIDED TO AND RECEIVED FROM ANY TFF SUBROUTINE WILL BE AT ONE OF THE LEVELS ABOVE.  IN ALL CASES,
# THE FREE FALL TIME IS RETURNED IN CENTISECONDS AT (-28).  PROGRAM TFF/CONIC WILL GENERATE VONE/RTMU AND
# LEAVE IT IN VONE' AT (+10) IF EARTH ORIGIN AND (+9) IF MOON ORIGIN.
#
# THE USER MUST STORE THE STATE VECTOR IN RONE, VONE, AND MU IN THE FORM 1/SQRT(MU) IN TFF/RTMU
# AT THE PROPER SCALE BEFORE CALLING TFF/CONIC.  SINCE RONE, VONE ARE IN THE EXTENDED VERB STORAGE AREA,
# THE USER MUST ALSO LOCK OUT THE EXTENDED VERBS, AND RELEASE THEM WHEN FINISHED.
#
# PROGRAMS CALC/TFF AND CALC/TPER ASSUME THAT THE TERMINAL RADIUS IS LESS THAN THE PRESENT
# RADIUS.  THIS RESTRICTION CAN BE REMOVED BY A 15 W CODING CHANGE, BUT AT PRESENT IT IS NOT DEEMED NECESSARY.
#
# THE FOLLOWING ERASABLE QUANTITIES ARE USED BY THE TFF ROUTINES, AND ARE LOCATED IN THE PUSH LIST.
#
# BELOW   E:  IS USED FOR EARTH ORIGIN SCALE
# M:  IS USED FOR MOON  ORIGIN SCALE
#
# TFFSW          =       119D    # BIT1  0 = CALCTFF             1 = CALCTPER
S('TFFDELQ', 'equals', 0o12, line=60)  #       Q2-Q1                   E: (-16)  M: (-15)
S('RMAG1', 'equals', 0o14, line=61)  #       ABVAL(RN)  M            E: (-29)  M: (-27)
# RPER           =       14D     #       PERIGEE RADIUS  M       E: (-29)  M: (-27)
S('TFFQ1', 'equals', 0o16, line=63)  #       R.V / SQRT(MUE)         E: (-16)  M: (-15)
# SDELF/2                        #       SIN(THETA) /2
S('CDELF/2', 'equals', 0o16, line=65)  #       COS(THETA) /2
# RAPO           =       16D     #       APOGEE RADIUS  M        E: (-29)  M: (-27)
S('NRTERM', 'equals', 0o20, line=67)  #       TERMINAL RADIUS  M      E: (-29+NR)
# M: (-27+NR)
S('RTERM', 'equals', 0o22, line=69)  #       TERMINAL RADIUS  M      E: (-29)  M: (-27)
S('TFFVSQ', 'equals', 0o24, line=70)  #       -(V SQUARED/MU)  1/M    E: (20)   M: (18)
S('TFF1/ALF', 'equals', 0o26, line=71)  #       SEMI MAJ AXIS  M        E: (-22-2 NA)
# M: (-20-2 NA)
S('TFFRTALF', 'equals', 0o30, line=73)  #       SQRT(ALFA)              E:(10+NA) M: (9+NA)
S('TFFALFA', 'equals', 0o32, line=74)  #       ALFA  1/M               E:(26-NR) M: (24-NR)
S('TFFNP', 'equals', 0o34, line=75)  #       SEMI LATUS RECTUM  M    E: (-38+2 NR)
# M: (-36+2 NR)
S('TFF/RTMU', 'equals', 0o36, line=77)  #       1/SQRT(MU)              E: (17)   M: (14)
S('NRMAG', 'equals', 0o40, line=78)  #       PRESENT RADIUS  M       E: (-29+NR)
# M: (-27+NR)
S('TFFX', 'equals', 0o42, line=80)
S('TFFTEM', 'equals', 0o44, line=81)  #       TEMPORARY
# Page 1269
# REGISTERS S1, S2 ARE UNTOUCED BY ANY TFF SUBROUTINE
# INDEX REGISTERS X1, X2 ARE USED BY ALL TFF SUBROUTINES.  THEY ARE ESTAB-
# LISHED IN TFF/CONIC AND MUST BE PRESERVED BETWEEN CALLS TO SUBSEQUENT
# SUBROUTINES.
# -NR                             C(X1) = NORM COUNT OF RMAG
# -NA                             C(X2) = NORM COUNT OF SQRT(ABS(ALFA))

# Page 1270
# SUBROUTINE NAME:  TFFCONIC                                            DATE:  01.29.67
# MOD NO:  0                                                            LOG SECTION:  TIME OF FREE FALL
# MOD BY:  RR BAIRNSFATHER
# MOD NO:  1    MOD BY:  RR BAIRNSFATHER        DATE: 11 APR 67
# MOD NO:  2    MOD BY:  RR BAIRNSFATHER        DATE: 21 NOV 67         ADD MOON MU.
# MOD NO:  3    MOD BY:  RR BAIRNSFATHER        DATE: 21 MAR 68         ACCEPT DIFFERENT EARTH/MOON SCALES
#
# FUNCTIONAL DESCRIPTION:  THIS SUBROUTINE IS CALLED TO COMPUTE THOSE CONIC PARAMETERS REQUIRED BY THE TFF
# SUBROUTINES AND TO ESTABLISH THEM IN THE PUSH LIST AREA.  THE PARAMETERS ARE LISTED UNDER OUTPUT.
# THE EQUATIONS ARE:
# _   __ __
# H = RN*VN                       ANGULAR MOMENTUM
# _ _
# LCP = H.H / MU                  SEMI LATUS RECTUM
# __ __
# ALFA = 2/RN - VN.VN / MU        RECIPROCAL SEMI-MAJOR AXIS, SIGNED
#
# AND ALFA IS POS FOR ELLIPTIC ORBITS
# 0 FOR PARABOLIC ORBITS
# NEG FOR HYPERBOLIC ORBITS
# SUBROUTINE ALSO COMPUTES AND SAVES RMAG.
#
# CALLING SEQUENCE:
# TFFCONIC EXPECTS CALLER TO ENTER WITH CORRECT GRAVITATIONAL CONSTANT IN MPAC, IN THE FORM
# 1/SQRT(MU).  THE PROGRAM WILL SAVE IN TFF/RTMU.  THE SCALE IS DETERMINED BY WHETHER EARTH OR MOON
# ORIGIN IS USED.  THE CALLER MUST LOCK OUT THE EXTENDED VERBS BEFORE PROVIDING STATE VECTOR IN RONE,
# VONE AT PROPER SCALE.  THE EXTENDED VERBS MUST BE RESTORED WHEN THE CALLER IS FINISHED USING THE
# TFF ROUTINES.
#
# ENTRY POINT TFFCONMU EXPECTS THAT TFF/RTMU IS ALREADY LOADED.
#
# TO SPECIFY MU:  DLOAD   CALL                            IF MU ALREADY STORED:   CALL
# YOURMU  1/RTMU E:(17) M:(14)                                    TFFCONMU
# TFFCONIC
# PUSHLOC = PDL+0, ARBITRARY IF LEQ 18D
#
# SUBROUTINES CALLED:  NONE
#
# NORMAL EXIT MODES:  RVQ
#
# ALARMS:  NONE
#
# OUTPUT:       THE FOLLOWING ARE STORED IN THE PUSH LIST AREA.
# RMAG1           E:(-29) M:(-27) M  RN, PRESENT RADIUS LENGTH.
# NRMAG           E:(-29+NR)      M  RMAG, NORMALIZED
# M:(-27+NR)
# X1                              -NR, NORM COUNT
# TFFNP           E:(-38+2NR)     M  LCP, SEMI LATUS RECTUM, WEIGHTED BY NR.      FOR VGAMCALC.
# M:(-36+2NR)
# TFF/RTMU        E:(17) M:(14)   1/SQRT(MU)
# TFFVSQ          E:(20) M:(18)   1/M  -(V SQ/MU):  PRESENT VELOCITY, NORMALIZED. FOR VGAMCALC
# TFFALFA         E:(26-NR)       1/M  ALFA, WEIGHTED BY NR
# M:(24-NR)
# TFFRTALF        E:(10+NA)       SQRT(ALFA), NORMALIZED
# M:(9+NA)
# Page 1271
# X2                              -NA, NORMCOUNT
# TFF1/ALF        E:(-22-2NA)     SIGNED SEMI MAJ AXIS, WEIGHTED BY NA
# M:(-20-2NA)
# PUSHLOC AT PDL+0
#
# THE FOLLOWING IS STORED IN GENERAL ERASABLE
# VONE'           E:(10) M:(9)    V/RT(MU), NORMALIZED VELOCITY
#
# ERASABLE INITIALIZATION REQUIRED:
# RONE            E:(-29) M:(-27) M  STATE VECTOR         LEFT BY CALLER
# VONE            E:(-7) M:(-5)   M/CS  STATE VECTOR      LEFT BY CALLER
# TFF/RTMU        E:(17) M:(14)   1/RT(CS SQ/M CUBE)      IF ENTER VIA TFFCONMU.
#
# DEBRIS:       QPRET           PDL+0 ... PDL+3

#   BANK 33
#   SETLOC TOF-FF
#   BANK

#   COUNT* $$/TFF

W('27,3360', 0o00037, 'TFFCONIC', 'STORE', 'TFF/RTMU', '1/SQRT(MU)    E:(17) M:(14)', kind='interp', line=168)

W('27,3361', 0o53575, 'TFFCONMU', 'VLOAD', 'UNIT', 'COME HERE WITH TFFRTMU LOADED.', kind='interp', line=170)
W('27,3362', 0o02207, '', '', 'RONE', 'SAVED RN.  M  E:(-29) M:(-27)', kind='operand', line=171)
W('27,3363', 0o77725, '', 'PDDL', '', 'UR/2 TO PDL+0, +5', kind='interp', line=172)
W('27,3364', 0o00045, '', '', '36D', 'MAGNITUDE', kind='operand', line=173)
W('27,3365', 0o00015, '', 'STORE', 'RMAG1', 'M  E:(-29) M:(-27)', kind='interp', line=174)

W('27,3366', 0o77701, '', 'NORM', kind='interp', line=176)
W('27,3367', 0o00047, '', '', 'X1', '-NR', kind='operand', line=177)
W('27,3370', 0o24041, '', 'STOVL', 'NRMAG', 'RMAG  M  E:(-29+NR) M:(-27+NR)', kind='interp', line=178)
W('27,3371', 0o02215, '', '', 'VONE', 'SAVED VN.  M/CS  E:(-7) M:(-5)', kind='operand', line=179)
W('27,3372', 0o77761, '', 'VXSC', kind='interp', line=180)
W('27,3373', 0o00037, '', '', 'TFF/RTMU', 'E:(17) M:(14)', kind='operand', line=181)
W('27,3374', 0o02170, '', 'STORE', "VONE'", 'VN/SQRT(MU)  E:(10) M:(9)', kind='interp', line=182)

W('27,3375', 0o47361, '', 'VXSC', 'VXV', kind='interp', line=184)
W('27,3376', 0o00041, '', '', 'NRMAG', 'E:(-29+NR) M:(-27+NR)', kind='operand', line=185)
# UR/2 FROM PDL
W('27,3377', 0o47572, '', 'VSL1', 'VSQ', 'BEFORE:  E:(-19+NR) M:(-18+NR)', kind='interp', line=187)
W('27,3400', 0o14035, '', 'STODL', 'TFFNP', 'LC P  M  E:(-38+2NR) M:(-36+2NR)', kind='interp', line=188)
# SAVE ALSO FOR VGAMCALC
W('27,3401', 0o06512, '', '', 'TFF1/4', kind='operand', line=190)
W('27,3402', 0o63271, '', 'DDV', 'PDVL', '(2/RMAG)  1/M  E:(26-NR) M:(24-NR)', kind='interp', line=191)
W('27,3403', 0o00041, '', '', 'NRMAG', 'RMAG  M  E:(-29+NR) M:(-27+NR)', kind='operand', line=192)
W('27,3404', 0o02170, '', '', "VONE'", 'SAVED VN.  E:(10) M:(9)', kind='operand', line=193)
W('27,3405', 0o57436, '', 'VSQ', 'DCOMP', 'KEEP MPAC+2 HONEST FOR SQRT.', kind='interp', line=194)
W('27,3406', 0o00025, '', 'STORE', 'TFFVSQ', '-(V SQ/MU)  E:(20) M:(18)', kind='interp', line=195)
# SAVE FOR VGAMCALC
W('27,3407', 0o43257, '', 'SR*', 'DAD', kind='interp', line=197)
# Page 1272
W('27,3410', 0o20573, '', '', '0 -6,1', 'GET -VSQ/MU  E:(26-NR) M:(24-NR)', kind='operand', line=199)
W('27,3411', 0o77626, '', 'STADR', kind='interp', line=200)
# 2/RMAG  FROM PDL+2
W('27,3412', 0o77744, '', 'STORE', 'TFFALFA', 'ALFA  1/M  E:(26-NR) M:(24-NR)', kind='interp', line=202)
W('27,3413', 0o41457, '', 'SL*', 'PUSH', 'TEMP SAVE ALFA  E:(20) M:(18)', kind='interp', line=203)
W('27,3414', 0o20173, '', '', '0 -6,1', kind='operand', line=204)
W('27,3415', 0o75446, '', 'ABS', 'SQRT', 'E:(10) M:(9)', kind='interp', line=205)
W('27,3416', 0o77701, '', 'NORM', kind='interp', line=206)
W('27,3417', 0o00050, '', '', 'X2', 'X2 = -NA', kind='operand', line=207)
W('27,3420', 0o00031, '', 'STORE', 'TFFRTALF', 'SQRT( ABS(ALFA) )  E:(10+NA) M:(9+NA)', kind='interp', line=208)
W('27,3421', 0o75316, '', 'DSQ', 'SIGN', 'NOT SO ACCURATE, BUT OK', kind='interp', line=209)
# ALFA FROM PDL+2  E:(20) M:(18)
W('27,3422', 0o55254, '', 'BZE', 'BDDV', 'SET 1/ALFA =0, TO SHOW SMALL ALFA', kind='interp', line=211)
W('27,3423', 0o57425, '', '', '+2', kind='operand', line=212)
W('27,3424', 0o06512, '', '', 'TFF1/4', kind='operand', line=213)
W('27,3425', 0o00027, '', 'STORE', 'TFF1/ALF', '1/ALFA  E:(-22-2NA) M:(-20-2NA)', kind='interp', line=214)
W('27,3426', 0o77616, 'DUMPCNIC', 'RVQ', kind='interp', line=215)

# 39 W
# Page 1273
# SUBROUTINE NAME:  TFFRP/RA                                            DATE: 01.17.67
# MOD NO:  0                                                            LOG SECTION:  TIME OF FREE FALL
# MOD NO:  1    MOD BY:  RR BAIRNSFATHER        DATE: 11 APR 67
# MOD NO:  2    MOD BY:  RR BAIRNSFATHER        DATE: 21 MAR 68         ACCEPT DIFFERENT EARTH/MOON SCALES
# ALSO IMPROVE ACCURACY OF RAPO.
#
# FUNCTIONAL DESCRIPTION:  USED BY CALCTPER AND TFF DISPLAYS TO CALCULATE PERIGEE RADIUS AND ALSO
# APOGEE RADIUS FOR A GENERAL CONIC.
# PROGRAM GIVES PERIGEE RADIUS AS         APOGEE RADIUS IS GIVEN BY
# RP = P/(1+E)                            RA = (1+E) / ALFA
# WHERE    2
# E  = 1 - P ALFA
# IF RA IS NEGATIVE OR SHOWS DIVIDE OVERFLOW, THEN RA = POSMAX BECAUSE
# 1. APOGEE RADIUS IS NOT MEANINGFUL FOR HYPERBOLA
# 2. APOGEE RADIUS IS NOT DEFINED FOR PARABOLA
# 3. APOGEE RADIUS EXCEEDS THE SCALING FOR ELLIPSE.
#
# THIS SUBROUTINE REQUIRED THE SIGNED RECIPROCAL SEMI MAJ AXIS, ALFA, AND SEMI-LATUS RECTUM AS DATA.
#
# CALLING SEQUENCE:     CALL
# TFFRP/RA
# PUSHLOC = PDL+0, ARBITRARY IF LEQ 10D
# C(MPAC) UNSPECIFIED
#
# SUBROUTINES CALLED:   NONE
#
# NORMAL EXIT MODE:     RVQ
# IF ELLIPSE, WITHIN NORMAL SCALING, RAPO IS CORRECT.
# OTHERWISE, RAPO = POSMAX.
#
# ALARMS:       NONE
#
# OUTPUT:       STORED IN PUSH LIST AREA.  SCALE OF OUTPUT AGREES WITH DATA SUPPLIED TO TFF/CONIC.
# RPER    E:(-29) M:(-27)         M       PERIGEE RADIUS          DESTROYED BY CALCTFF/CALCTPER, TFFTRIG.
# RAPO    E:(-29) M:(-27)         M       APOGEE RADIUS           WILL BE DESTROYED BY CALCTFF/CALCTPER
# PUSHLOC AT PDL+0
#
# ERASABLE INITIALIZATION REQUIRED:
# TFFALFA E:(26-NR)               M       1/SEMI MAJ AXIS         LEFT BY TFFCONIC
# M:(24-NR)
# TFFNP   E:(-38+2NR)             M       LC P, SEMI LATUS RECTUM LEFT BY TFFCONIC
# M:(-36+2NR)
# X1                              -NR, NORM COUNT OF RMAG         LEFT BY TFFCONIC
# X2                              -NA, NORM COUNT OF ALFA         LEFT BY TFFCONIC
#
# DEBRIS:       QPRET, PDL+0 ... PDL+1

# Page 1274
S('RAPO', 'equals', 0o20, line=267)  # APOGEE RADIUS  M  E:(-29) M:(-27)
S('RPER', 'equals', 0o16, line=268)  # PERIGEE RADIUS  M  E:(-29) M:(-27)

W('27,3427', 0o41345, 'TFFRP/RA', 'DLOAD', 'DMP', kind='interp', line=270)
W('27,3430', 0o00033, '', '', 'TFFALFA', 'ALFA  1/M  E:(26-NR) M:(24-NR)', kind='operand', line=271)
W('27,3431', 0o00035, '', '', 'TFFNP', 'LC P  M E:(-38+2NR) M:(-36+2NR)', kind='operand', line=272)
W('27,3432', 0o57457, '', 'SR*', 'DCOMP', 'ALFA P (-12+NR)', kind='interp', line=273)
W('27,3433', 0o20571, '', '', '0 -8D,1', 'ALFA P (-4)', kind='operand', line=274)
W('27,3434', 0o51415, '', 'DAD', 'ABS', '(DCOMP GIVES VALID TP RESULT FOR SQRT)', kind='interp', line=275)
# (ABS PROTECTS SQRT IF E IS VERY NEAR 0)
W('27,3435', 0o17765, '', '', 'DP2(-4)', kind='operand', line=277)
W('27,3436', 0o43366, '', 'SQRT', 'DAD', 'E SQ = (1- P ALFA) (-4)', kind='interp', line=278)
W('27,3437', 0o06512, '', '', 'TFF1/4', kind='operand', line=279)
W('27,3440', 0o55206, '', 'PUSH', 'BDDV', '(1+E)  (-2)  TO PDL+0', kind='interp', line=280)
W('27,3441', 0o00035, '', '', 'TFFNP', 'LCP  M  E:(-38+2NR) M:(-36+2NR)', kind='operand', line=281)
W('27,3442', 0o53657, '', 'SR*', 'SR*', '(DOES SR THEN SL TO AVOID OVFL)', kind='interp', line=282)
W('27,3443', 0o20601, '', '', '0,1', 'X1=-NR', kind='operand', line=283)
W('27,3444', 0o20572, '', '', '0 -7,1', '(EFFECTIVE SL)', kind='operand', line=284)
W('27,3445', 0o14017, '', 'STODL', 'RPER', 'PERIGEE RADIUS  M  E:(-29) M:(-27)', kind='interp', line=285)
# (1+E)  (-2)  FROM PDL+0
W('27,3446', 0o41005, '', 'DMP', 'BOVB', kind='interp', line=287)
W('27,3447', 0o00027, '', '', 'TFF1/ALF', 'E:(-22-2NA) M:(-20-2NA)', kind='operand', line=288)
W('27,3450', 0o57753, '', '', 'TCDANZIG', 'CLEAR OVFIND, IF ON.', kind='operand', line=289)
W('27,3451', 0o53654, '', 'BZE', 'SL*', kind='interp', line=290)
W('27,3452', 0o57461, '', '', 'MAXRA', 'SET POSMAX IF ALFA=0', kind='operand', line=291)
W('27,3453', 0o57603, '', '', '0 -5,2', '-5+NA', kind='operand', line=292)
W('27,3454', 0o40057, '', 'SL*', 'BOV', kind='interp', line=293)
W('27,3455', 0o57576, '', '', '0,2', kind='operand', line=294)
W('27,3456', 0o57461, '', '', 'MAXRA', 'SET POSMAX IF OVFL.', kind='operand', line=295)
W('27,3457', 0o77644, '', 'BPL', '', 'CONTINUE WITH VALID RAPO.', kind='interp', line=296)
W('27,3460', 0o57463, '', '', '+3', kind='operand', line=297)
W('27,3461', 0o77745, 'MAXRA', 'DLOAD', '', 'RAPO CALC IS NOT VALID.  SET RAPO =', kind='interp', line=298)
W('27,3462', 0o17771, '', '', 'NEARONE', 'POSMAX AS A TAG.', kind='operand', line=299)
W('27,3463', 0o00021, '', 'STORE', 'RAPO', 'APOGEE RADIUS  M  E:(-29) M:(-27)', kind='interp', line=300)
W('27,3464', 0o77616, 'DUMPRPRA', 'RVQ', kind='interp', line=301)

# 30 W
# Page 1275
# SUBROUTINE NAME:  CALCTPER / CALCTFF                                  DATE:  01.29.67
# MOD NO:  0                                                            LOG SECTION:  TIME OF FREE FALL
# MOD BY:  RR BAIRNSFATHER
# MOD NO:  1    MOD BY:  RR BAIRNSFATHER        DATE: 21 MAR 67
# MOD NO:  2    MOD BY:  RR BAIRNSFATHER        DATE: 14 APR 67
# MOD BY:  3    MOD BY:  RR BAIRNSFATHER        DATE: 8 JUL 67          NEAR EARTH MUE AND NEG TFF (GONEPAST)
# MOD BY:  4    MOD BY:  RR BAIRNSFATHER        DATE: 21 NOV 67         ADD VARIABLE MU.
# MOD BY:  5    MOD BY:  RR BAIRNSFATHER        DATE: 21 MAR 68         ACCEPT DIFFERENT EARTH/MOON SCALES
#
# FUNCTIONAL DESCRIPTION:  PROGRAM CALCULATES THE FREE-FALL TIME OF FLIGHT FROM PRESENT POSITION RN AND
# VELOCITY VN TO A RADIUS LENGTH SPECIFIED BY RTERM, SUPPLIED BY THE USER.  THE POSITION VECTOR
# RN MAY BE ON EITHER SIDE OF THE CONIC, BUT RTERM IS CONSIDERED ON THE INBOUND SIDE.
# THE EQUATIONS ARE:
#
# Q2 = -SQRT(RTERM (2-RTERM ALFA) - LCP)  (INBOUND SIDE)  LEQ +- LCE/SQRT(ALFA)
# __ __
# Q1 = RN.VN / SQRT(MU)                                   LEQ +- LCE/SQRT(ALFA)
#
# Z = NUM / DEN                                           LEQ +- 1/SQRT(ALFA)
#
# WHERE, IF INBOUND
# NUM = RTERM -RN                                         LEQ +- 2 LCE/ALFA
# DEN = Q2+Q1                                             LEQ +- 2 LCE/SQRT(ALFA)
#
# AND, IF OUTBOUND
# NUM = Q2-Q1                                             LEQ +- 2 LCE/SQRT(ALFA)
# DEN = 2 - ALFA (RTERM + RN).                            LEQ +- 2 LCE
#
# IF      ALFA ZZ < 1.0           (FOR ALL CONICS EXCEPT ELLIPSES HAVING ABS(DEL ECC ANOM) G 90 DEG)
# THEN    X = ALFA Z Z
# AND     TFF = (RTERM +RN -2 ZZ T(X) ) Z/SQRT(MU)
# EXCEPT  IF ALFA PNZ, AND IF TFF NEG,
# THEN    TFF = 2 PI /(ALFA SQRT(ALFA)) + TFF
# OR      IF ALFA ZZ GEQ 1.0      (FOR ELLIPSES HAVING ABS(DEL ECC ANOM) GEQ 90 DEG)
# THEN    X = 1/ALFA Z Z
# AND     TFF = (PI/SQRT(ALFA) -Q2 +Q1 +2(X T(X) -1) /ALFA Z) /ALFA SQRT(MU)
# WHERE   T(X) IS A POLYNOMIAL APPROXIMATION TO THE SERIES
# 2      3             2
# 1/3 - X/5 + X /7 - X /8 ...     (X  < 1.0)
#
# CALLING SEQUENC:      TIME TO RTERM                   TIME TO PERIGEE
# CALL                            CALL
# CALCTFF                         CALCTPER
# C(MPAC) = TERMNL RAD M          C(MPAC) = PERIGEE RAD M
# FOR EITHER, E:(-29) M:(-27)
# FOR EITHER, PUSHLOC = PDL+0, ARBITRARY IF LEQ 8D.
# Page 1276
#
# SUBROUTINES CALLED:   T(X), VIA RTB
#
# NORMAL EXIT MODE:     RVQ
# HOWEVER, PROGRAM EXITS WITH ONE OF THE FOLLOWING VALUES FOR TFF (-28) CS IN MPAC.  USER MUST STORE.
# A. TFF = FLIGHT TIME.  NORMAL CASE FOR POSITIVE FLIGHT TIME LESS THAN ONE ORBITAL PERIOD.
# B. (THIS OPTION IS NO LONGER USED.)
# C. TFF = POSMAX.  THIS INDICATES THAT THE CONIC FROM THE PRESENT POSITION WILL NOT RETURN TO
# THE SPECIFIED ALTITUDE.  ALSO INDICATES OUTBOUND PARABOLA OR HYPERBOLA.
#
# OUTPUT:       C(MPAC)         (-28) CS        TIME OF FLIGHT, OR TIME TO PERIGEE
# TFFX            (0)             X                                       LEFT FOR ENTRY DISPLAY TFF ROUTINES
# NRTERM          E:(-29+NR) M    RTERM, WEIGHTED BY NR                   LEFT FOR ENTRY DISPLAY TFF ROUTINES
# M:(-27+NR)
# TFFTEM          E:(-59+2NR)     LCP Z Z SGN(SDELF)                      LEFT FOR ENTRY DISPLAY TFF ROUTINES
# M:(-55+2NR)     LCP /ALFA SGN(SDELF)                    LEFT FOR ENTRY DISPLAY TFF ROUTINES
# NOTE:   TFFTEM = PDL 36D AND WILL BE DESTROYED BY .:UNIT:.
# RMAG1           E:(-29) M:(-27) PDL 12 NOT TOUCHED.
# TFFQ1           E:(-16) M:(-15) PDL 14D
# TFFDELQ         E:(-16) M:(-15) PDL 10D
# PUSHLOC AT PDL+0
#
# ERASABLE INITIALIZATION REQUIRED:
# RONE            E:(-29) M:(-27) M  STATE VECTOR                         LEFT BY USER
# VONE'           E:(+10) M:(+9)  VN/SQRT(NU)                             LEFT BY TFF/CONIC
# RMAG1           E:(-29) M:(-27) PRESENT RADIUS, M                       LEFT BY TFFCONIC
# C(MPAC)         E:(-29) M:(-27) RTERM, TERMINAL RADIUS LENGTH, M        LEFT BY USER
#
# THE FOLLOWING ARE STORED IN THE PUSH LIST AREA.
# TFF/RTMU        E:(17) M:(14)   1/SQRT(MU)                              LEFT BY TFFCONIC.
# NRMAG           E:(-29+NR)      M  RMAG, NORMALIZED                     LEFT BY TFFCONIC
# M:(-27+NR)
# X1                              -NR, NORM COUNT                         LEFT BY TFFCONIC
# TFFNP           E:(-38+2NR)     M  LCP, SEMI LATUS RECTUM, WEIGHT NR    LEFT BY TFFCONIC
# M:(-36+2N4)
# TFFALFA         E:(26-NR)       1/M  ALFA, WEIGHT NR                    LEFT BY TFFCONIC
# M:(24-NR)
# TFFRTALF        E:(10+NA)       SQRT(ALFA), NORMALIZED                  LEFT BY TFFCONIC
# M:(9+NA)
# X2                              -NA, NORMCOUNT                          LEFT BY TFFCONIC
# TFF1/ALF        E:(-22-2NA)     SIGNED SEMI-MAJOR AXIS, WEIGHTED BY NA  LEFT BY TFFCONIC
# M:(-20-2NA)
#
# DEBRIS:       QPRET, PDL+0 ... PDL+3
# RTERM           E:(-29) M(-27)  RTERM, TERMINAL RADIUS LENGTH
# RAPO            E:(-29) M(-27)  PDL 16D (=NRTERM)
# RPER            E:(-29) M(-27)  PDL 14D (=TFFQ1)

# Page 1277
W('27,3465', 0o77614, 'CALCTPER', 'SETGO', '', 'ENTER WITH RPER IN MPAC', kind='interp', line=401)
W('27,3466', 0o03436, '', '', 'TFFSW', kind='operand', line=402)
W('27,3467', 0o57472, '', '', '+3', kind='operand', line=403)
W('27,3470', 0o77614, 'CALCTFF', 'CLEAR', '', 'ENTER WITH RTERM IN MPAC', kind='interp', line=404)
W('27,3471', 0o03676, '', '', 'TFFSW', kind='operand', line=405)
W('27,3472', 0o00023, '', 'STORE', 'RTERM', 'E:(-29) M:(-27)', kind='interp', line=406)
W('27,3473', 0o77657, '', 'SL*', kind='interp', line=407)
W('27,3474', 0o20201, '', '', '0,1', 'X1=-NR', kind='operand', line=408)
W('27,3475', 0o00021, '', 'STORE', 'NRTERM', 'RTERM  E:(-29+NR) M:(-27+NR)', kind='interp', line=409)
W('27,3476', 0o44205, '', 'DMP', 'BDSU', kind='interp', line=410)
W('27,3477', 0o00033, '', '', 'TFFALFA', 'ALFA  E:(26-NR) M:(24-NR)', kind='operand', line=411)
W('27,3500', 0o06512, '', '', 'TFF1/4', kind='operand', line=412)
W('27,3501', 0o41206, '', 'PUSH', 'DMP', '(2-ALFA RTERM)  (-3)  TO PDL+0', kind='interp', line=413)
W('27,3502', 0o00021, '', '', 'NRTERM', 'E:(-29+NR) M:(-27+NR)', kind='operand', line=414)
W('27,3503', 0o53725, '', 'PDDL', 'SR*', 'RTERM(2-ALFA RTERM) TO PDL+2', kind='interp', line=415)
# E:(-32+NR) M:(-30+NR)
W('27,3504', 0o00035, '', '', 'TFFNP', 'LC P  E:(-38+2NR) M:(-36+2NR)', kind='operand', line=417)
W('27,3505', 0o20573, '', '', '0 -6,1', 'X1 = -NR', kind='operand', line=418)
W('27,3506', 0o43276, '', 'DCOMP', 'DAD', 'DUE TO SHIFTS, KEEP PRECISION FOR SQRT', kind='interp', line=419)
# RTERM(2-ALFA RTERM) FROM PDL +2
# E:(-32+NR) M:(-30+NR)
W('27,3507', 0o77657, '', 'SR*', '', 'LEAVE  E:(-32) M:(-30)', kind='interp', line=422)
W('27,3510', 0o20601, '', '', '0,1', 'X1 = -NR', kind='operand', line=423)
W('27,3511', 0o71214, '', 'BOFF', 'DLOAD', 'CHECK TFF /TPER SWITCH', kind='interp', line=424)
W('27,3512', 0o03756, '', '', 'TFFSW', kind='operand', line=425)
W('27,3513', 0o57515, '', '', '+2', 'IF TFF, CONTINUE', kind='operand', line=426)
W('27,3514', 0o06522, '', '', 'TFFZEROS', 'IF TPER, SET Q2 = 0', kind='operand', line=427)
W('27,3515', 0o75440, '', 'BMN', 'SQRT', 'E:(-16) M:(-15)', kind='interp', line=428)

W('27,3516', 0o57650, '', '', 'MAXTFF1', 'NO FREE FALL CONIC TO RTERM FROM HERE', kind='operand', line=430)
# RESET PDL, SET TFF=POSMAX, AND EXIT.

W('27,3517', 0o41076, '', 'DCOMP', 'BOVB', 'RT IS ON INBOUND SIDE.  ASSURE OVFIND=0', kind='interp', line=433)
W('27,3520', 0o57753, '', '', 'TCDANZIG', 'ANY PORT IN A STORM.', kind='operand', line=434)
W('27,3521', 0o24045, '', 'STOVL', 'TFFTEM', 'Q2  E:(-16) M:(-15)', kind='interp', line=435)
W('27,3522', 0o02170, '', '', "VONE'", 'VN/SQRT(MU)  E:(10) M:(9)', kind='operand', line=436)
W('27,3523', 0o52441, '', 'DOT', 'SL3', kind='interp', line=437)
W('27,3524', 0o02207, '', '', 'RONE', 'SAVED RN.  E:(-29) M:(-27)', kind='operand', line=438)
W('27,3525', 0o00017, '', 'STORE', 'TFFQ1', 'Q1, SAVE FOR GONEPAST TEST.', kind='interp', line=439)
# E:(-16) M:(-15)
W('27,3526', 0o44240, '', 'BMN', 'BDSU', kind='interp', line=441)
W('27,3527', 0o57550, '', '', 'INBOUND', 'USE ALTERNATE Z', kind='operand', line=442)
W('27,3530', 0o00045, '', '', 'TFFTEM', 'Q2  E:(-16) M:(-15)', kind='operand', line=443)

# OUTBOUND Z CALC CONTINUES HERE

W('27,3531', 0o14043, '', 'STODL', 'TFFX', 'NUM=Q2-Q1  E:(-16) M:(-15)', kind='interp', line=447)
W('27,3532', 0o00033, '', '', 'TFFALFA', 'ALFA  E:(26-NR) M:(24-NR)', kind='operand', line=448)
W('27,3533', 0o44205, '', 'DMP', 'BDSU', kind='interp', line=449)
# Page 1278
W('27,3534', 0o00041, '', '', 'NRMAG', 'RMAG  E:(-29+NR) M:(-27+NR)', kind='operand', line=451)
# (2-RTERM ALFA)  (-3) FROM PDL+0
W('27,3535', 0o51406, 'SAVEDEN', 'PUSH', 'ABS', 'DEN TO PDL+0  E:(-3) OR (-16)', kind='interp', line=453)
# M:(-3) OR (-15)
W('27,3536', 0o40015, '', 'DAD', 'BOV', 'INDETERMINANCY TEST', kind='interp', line=455)
W('27,3537', 0o17757, '', '', 'LIM(-22)', '=1.0-B(-22)', kind='operand', line=456)
W('27,3540', 0o57561, '', '', 'TFFXTEST', 'GO IF DEN >/= B(-22)', kind='operand', line=457)
W('27,3541', 0o65345, '', 'DLOAD', 'PDDL', 'SET DEN=0 OTHERWISE', kind='interp', line=458)
W('27,3542', 0o06522, '', '', 'TFFZEROS', kind='operand', line=459)
# XCH ZERO WITH PDL+0
W('27,3543', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=461)
W('27,3544', 0o00033, '', '', 'TFFALFA', 'ALFA  E:(26-NR) M:(24-NR)', kind='operand', line=462)
W('27,3545', 0o71240, '', 'BMN', 'DLOAD', 'FOR TPER:  Z INDET AT DELE/2=0 AND 90.', kind='interp', line=463)
W('27,3546', 0o57655, '', '', 'TFFEL1', 'ASSUME 90, AND LEAVE 0 IN PDL: 1/Z=D/N', kind='operand', line=464)

# Z INDET. AT PERIGEE FOR PARAB OR HYPERB.
W('27,3547', 0o77616, 'DUMPTFF1', 'RVQ', '', 'RETURN TFF =0', kind='interp', line=467)

# INBOUND Z CALC CONTINUES HERE

W('27,3550', 0o77745, 'INBOUND', 'DLOAD', '', 'RESET PDL+0', kind='interp', line=471)
W('27,3551', 0o45345, '', 'DLOAD', 'DSU', 'ALTERNATE Z CALC', kind='interp', line=472)
W('27,3552', 0o00023, '', '', 'RTERM', 'E:(-29) M:(-27)', kind='operand', line=473)
W('27,3553', 0o00015, '', '', 'RMAG1', 'E:(-29) M:(-27)', kind='operand', line=474)
W('27,3554', 0o14043, '', 'STODL', 'TFFX', 'NUM=RTERM-RN  E:(-29) M:(-27)', kind='interp', line=475)
W('27,3555', 0o00045, '', '', 'TFFTEM', 'Q2  E:(-16) M:(-15)', kind='operand', line=476)
W('27,3556', 0o52015, '', 'DAD', 'GOTO', kind='interp', line=477)
W('27,3557', 0o00017, '', '', 'TFFQ1', 'Q1  E:(-16) M:(-15)', kind='operand', line=478)
W('27,3560', 0o57535, '', '', 'SAVEDEN', 'DEN = Q2+Q1  E:(-16) M:(-15)', kind='operand', line=479)

W('27,3561', 0o65215, 'TFFXTEST', 'DAD', 'PDDL', '(ABS(DEN) TO PDL+2)   E:(-3) OR (-16)', kind='interp', line=481)
# M:(-3) OR (-15)
W('27,3562', 0o17761, '', '', 'DP(-22)', 'RESTORE ABS(DEN) TO MPAC', kind='operand', line=483)
W('27,3563', 0o00043, '', '', 'TFFX', 'NUM  E:(-16) OR (-29)  M:(-15) OR (-27)', kind='operand', line=484)
W('27,3564', 0o53605, '', 'DMP', 'SR*', kind='interp', line=485)
W('27,3565', 0o00031, '', '', 'TFFRTALF', 'SQRT(ALFA)  E:(10+NA) M:(9+NA)', kind='operand', line=486)
W('27,3566', 0o57201, '', '', '0 -3,2', 'X2=-NA', kind='operand', line=487)
W('27,3567', 0o77671, '', 'DDV', '', 'C(MPAC) =NUM SQRT(ALFA)       E:(-3) OR (-16)', kind='interp', line=488)
# M:(-3) OR (-15)
# ABS(DEN) FROM PDL+2   E:(-3) OR (-16)
# M:(-3) OR (-15)
W('27,3570', 0o40145, '', 'DLOAD', 'BOV', '(THE DLOAD IS SHARED WITH TFFELL)', kind='interp', line=492)
W('27,3571', 0o00043, '', '', 'TFFX', 'NUM  E:(-16) OR (-29)  M:(-15) OR (-27)', kind='operand', line=493)
W('27,3572', 0o57653, '', '', 'TFFELL', 'USE EQN FOR DELE GEQ 90, LEQ -90', kind='operand', line=494)

# OTHERWISE, CONTINUE FOR GENERAL CONIC FOR TFF EQN

W('27,3573', 0o45471, '', 'DDV', 'STADR', kind='interp', line=498)
# DEN FROM PDL+0        E:(-3) OR (-16)
# M:(-3) OR (-15)
W('27,3574', 0o77732, '', 'STORE', 'TFFTEM', 'Z SAVE FOR SIGN OF SDELF.', kind='interp', line=501)
# Page 1279
# E:(-13) M:(-12)
W('27,3575', 0o63406, '', 'PUSH', 'DSQ', 'Z TO PDL+0', kind='interp', line=504)
W('27,3576', 0o41206, '', 'PUSH', 'DMP', 'Z SQ TO PDL+2  E:(-26) M:(-24)', kind='interp', line=505)
W('27,3577', 0o00035, '', '', 'TFFNP', 'LC P  E:(-38+2NR) M:(-36+NR)', kind='operand', line=506)
W('27,3600', 0o75261, '', 'SL', 'SIGN', kind='interp', line=507)
W('27,3601', 0o20206, '', '', '5', kind='operand', line=508)
W('27,3602', 0o00045, '', '', 'TFFTEM', 'AFFIX SIGN FOR SDELF (ENTRY DISPLAY)', kind='operand', line=509)
W('27,3603', 0o14045, '', 'STODL', 'TFFTEM', 'P ZSQ  E:(-59+2NR) M:(-55+2NR)', kind='interp', line=510)
# (ARG IS USED IN TFF/TRIG)
# ZSQ FROM PDL+2  E:(-26) M:(-24)
W('27,3604', 0o41206, '', 'PUSH', 'DMP', 'RESTORE PUSH LOC', kind='interp', line=513)
W('27,3605', 0o00033, '', '', 'TFFALFA', 'ALFA  E:(26-NR) M:(24-NR)', kind='operand', line=514)
W('27,3606', 0o77657, '', 'SL*', kind='interp', line=515)
W('27,3607', 0o20201, '', '', '0,1', 'X1=-NR', kind='operand', line=516)
W('27,3610', 0o00043, '', 'STORE', 'TFFX', 'X', kind='interp', line=517)
W('27,3611', 0o41234, '', 'RTB', 'DMP', kind='interp', line=518)
W('27,3612', 0o57735, '', '', 'T(X)', 'POLY', kind='operand', line=519)
# ZSQ FROM PDL+2  E:(-26) M:(-24)
W('27,3613', 0o44302, '', 'SR2', 'BDSU', '2 ZSQ T(X)  E:(-29) M:(-27)', kind='interp', line=521)
W('27,3614', 0o00023, '', '', 'RTERM', 'RTERM  E:(-29) M:(-27)', kind='operand', line=522)
W('27,3615', 0o41215, '', 'DAD', 'DMP', kind='interp', line=523)
W('27,3616', 0o00015, '', '', 'RMAG1', 'E:(-29) M:(-27)', kind='operand', line=524)
# Z FROM PDL+0  E:(-13) M:(-12)
W('27,3617', 0o51042, '', 'SR3', 'BPL', 'TFF SQRT(MU)  E:(-45) M:(-42)', kind='interp', line=526)
W('27,3620', 0o57641, '', '', 'ENDTFF', '(NO PUSH UP)', kind='operand', line=527)
W('27,3621', 0o75206, '', 'PUSH', 'SIGN', 'TFF SQRT(MU) TO PDL+0', kind='interp', line=528)
W('27,3622', 0o00017, '', '', 'TFFQ1', 'Q1 FOR GONEPAST TEST', kind='operand', line=529)
W('27,3623', 0o71244, '', 'BPL', 'DLOAD', 'GONE PAST ?', kind='interp', line=530)
W('27,3624', 0o57645, '', '', 'NEGTFF', 'YES. TFF < 0.', kind='operand', line=531)
W('27,3625', 0o00027, '', '', 'TFF1/ALF', '1/ALFA  E:(-22-2NA) M:(-20-2NA)', kind='operand', line=532)
W('27,3626', 0o51076, '', 'DCOMP', 'BPL', 'ALFA > 0 ?', kind='interp', line=533)
W('27,3627', 0o57645, '', '', 'NEGTFF', 'NO. TFF IS NEGATIVE.', kind='operand', line=534)

# CORRECT FOR ORBITAL PERIOD.

W('27,3630', 0o77676, '', 'DCOMP', '', 'YES.  CORRECT FOR ORB PERIOD.', kind='interp', line=538)
W('27,3631', 0o56205, '', 'DMP', 'DDV', kind='interp', line=539)
W('27,3632', 0o17755, '', '', 'PI/16', '2 PI (-5)', kind='operand', line=540)
W('27,3633', 0o00031, '', '', 'TFFRTALF', 'SQRT(ALFA)  E:(10+NA) M:(9+NA)', kind='operand', line=541)
W('27,3634', 0o53657, '', 'SL*', 'SL*', kind='interp', line=542)
W('27,3635', 0o57602, '', '', '0 -4,2', 'X2=-NA', kind='operand', line=543)
W('27,3636', 0o57602, '', '', '0 -4,2', kind='operand', line=544)
W('27,3637', 0o43257, '', 'SL*', 'DAD', kind='interp', line=545)
W('27,3640', 0o57576, '', '', '0,2', kind='operand', line=546)
# TFF SQRT(MU) FROM PDL+0       E:(-45) M:(-42)
W('27,3641', 0o40005, 'ENDTFF', 'DMP', 'BOV', 'TFF SQRT(MU) IN MPAC          E:(-45) M:(-42)', kind='interp', line=548)
W('27,3642', 0o00037, '', '', 'TFF/RTMU', 'E:(17) M:(14)', kind='operand', line=549)
W('27,3643', 0o57651, '', '', 'MAXTFF', 'SET POSMAX IN OVFL.', kind='operand', line=550)

W('27,3644', 0o77616, 'DUMPTFF2', 'RVQ', '', 'RETURN TFF (-28) CS IN MPAC.', kind='interp', line=552)

# Page 1280
W('27,3645', 0o77745, 'NEGTFF', 'DLOAD', kind='interp', line=555)
# TFF SQRT(MU) FROM PDL+0, NEGATIVE.
W('27,3646', 0o77650, '', 'GOTO', kind='interp', line=557)
W('27,3647', 0o57641, '', '', 'ENDTFF', kind='operand', line=558)

W('27,3650', 0o77745, 'MAXTFF1', 'DLOAD', '', 'RESET PDL', kind='interp', line=560)
W('27,3651', 0o43545, 'MAXTFF', 'DLOAD', 'RVQ', kind='interp', line=561)
W('27,3652', 0o17771, '', '', 'NEARONE', kind='operand', line=562)

# TIME OF FLIGHT ELLIPSE WHEN DEL (ECCENTRIC ANOM) GEQ 90 AND LEQ -90.

# NUM FROM TFFX.        E:(-16) OR (-29)
# M:(-15) OR (-27)
W('27,3653', 0o77712, 'TFFELL', 'SL2', '', 'NUM  E:(-14) OR (-27)  M:(-13) OR (-25)', kind='interp', line=568)
W('27,3654', 0o41465, '', 'BDDV', 'PUSH', 'TEMP SAVE D/N IN PDL+0', kind='interp', line=569)
# DEN FROM PDL+0  E:(-3)/(-16)  M:(-3)/(-15)
# N/D TO PDL+0  E:(11) M:(10)
W('27,3655', 0o45345, 'TFFEL1', 'DLOAD', 'DSU', '(ENTER WITH D/N=0 IN PDL+0)', kind='interp', line=572)
W('27,3656', 0o00045, '', '', 'TFFTEM', 'Q2  E:(-16) M:(-15)', kind='operand', line=573)
W('27,3657', 0o00017, '', '', 'TFFQ1', 'Q1  E:(-16) M:(-15)', kind='operand', line=574)
W('27,3660', 0o14013, '', 'STODL', 'TFFDELQ', 'Q2-Q1  E:(-16) M:(-15)', kind='interp', line=575)
# D/N FROM PDL+0
W('27,3661', 0o77626, '', 'STADR', kind='interp', line=577)
W('27,3662', 0o77732, '', 'STORE', 'TFFTEM', 'D/N  E:(11) M:(10)', kind='interp', line=578)
W('27,3663', 0o53605, '', 'DMP', 'SL*', kind='interp', line=579)
W('27,3664', 0o00027, '', '', 'TFF1/ALF', '1/ALFA  E:(-22-2NA) M:(-20-2NA)', kind='operand', line=580)
W('27,3665', 0o57576, '', '', '0,2', '1/ALFA Z  E:(-11-NA) M:(-10-NA)', kind='operand', line=581)
W('27,3666', 0o41206, '', 'PUSH', 'DMP', 'TO PDL+0', kind='interp', line=582)
W('27,3667', 0o00045, '', '', 'TFFTEM', '1/Z  E:(11) M:(10', kind='operand', line=583)
W('27,3670', 0o41057, '', 'SL*', 'BOVB', kind='interp', line=584)
W('27,3671', 0o57576, '', '', '0,2', 'X2= -NA', kind='operand', line=585)
W('27,3672', 0o21712, '', '', 'SIGNMPAC', 'IN CASE X= 1.0, CONTINUE', kind='operand', line=586)
W('27,3673', 0o00043, '', 'STORE', 'TFFX', 'X=1/ALFA ZSQ', kind='interp', line=587)
W('27,3674', 0o41234, '', 'RTB', 'DMP', kind='interp', line=588)
W('27,3675', 0o57735, '', '', 'T(X)', 'POLY', kind='operand', line=589)
W('27,3676', 0o00043, '', '', 'TFFX', kind='operand', line=590)
W('27,3677', 0o45242, '', 'SR3', 'DSU', kind='interp', line=591)
W('27,3700', 0o17763, '', '', 'DP2(-3)', kind='operand', line=592)
W('27,3701', 0o41405, '', 'DMP', 'PUSH', '2(X T(X)-1) /Z ALFA   E:(-15-NA)', kind='interp', line=593)
# M:(-14-NA)
# 1/ALFA Z FROM PDL+0   E:(-11-NA)
# M:(-10-NA)
W('27,3702', 0o41345, '', 'DLOAD', 'DMP', 'GET SIGN FOR SDELF', kind='interp', line=597)
W('27,3703', 0o00045, '', '', 'TFFTEM', '1/Z  E:(11) M:(10)', kind='operand', line=598)
W('27,3704', 0o00015, '', '', 'RMAG1', 'E:(-29) M:(-27)', kind='operand', line=599)
W('27,3705', 0o43312, '', 'SL2', 'DAD', kind='interp', line=600)
W('27,3706', 0o00017, '', '', 'TFFQ1', 'Q1  E:(-16) M:(-15)', kind='operand', line=601)
W('27,3707', 0o14045, '', 'STODL', 'TFFTEM', '(Q1+R 1/Z) =SGN OF SDELF  E:(-16) M:(-15)', kind='interp', line=602)
W('27,3710', 0o00035, '', '', 'TFFNP', 'LC P  E:(-38+2NR) M:(-36+2NR)', kind='operand', line=603)
W('27,3711', 0o53605, '', 'DMP', 'SL*', 'CALC FOR ARG FOR TFF/TRIG.', kind='interp', line=604)
# Page 1281
W('27,3712', 0o00027, '', '', 'TFF1/ALF', '1/ALFA  E:(-22-2NA) M:(-20-2NA)', kind='operand', line=606)
W('27,3713', 0o57575, '', '', '1,2', 'X2=-NA', kind='operand', line=607)
W('27,3714', 0o53765, '', 'SIGN', 'SL*', kind='interp', line=608)
W('27,3715', 0o00045, '', '', 'TFFTEM', 'AFFIX SIGN FOR SDELF', kind='operand', line=609)
W('27,3716', 0o57576, '', '', '0,2', kind='operand', line=610)
W('27,3717', 0o14045, '', 'STODL', 'TFFTEM', 'P/ALFA  E:(-59+2NR) M:(-55+2NR)', kind='interp', line=611)
# (ARG FOR USE IN TFF/TRIG)
W('27,3720', 0o00027, '', '', 'TFF1/ALF', '1/ALFA  E:(-22-2NA) M:(-20-2NA)', kind='operand', line=613)
W('27,3721', 0o41366, '', 'SQRT', 'DMP', kind='interp', line=614)
W('27,3722', 0o17755, '', '', 'PI/16', 'PI (-4)', kind='operand', line=615)
W('27,3723', 0o77615, '', 'DAD', kind='interp', line=616)
# 2(XT(X)-1)/Z ALFA FROM PDL    E:(-15-NA)
# M:(-14-NA)
W('27,3724', 0o45257, '', 'SL*', 'DSU', kind='interp', line=619)
W('27,3725', 0o57577, '', '', '0 -1,2', kind='operand', line=620)
W('27,3726', 0o00013, '', '', 'TFFDELQ', 'Q2-Q1  E:(-16) M:(-15)', kind='operand', line=621)
W('27,3727', 0o53605, '', 'DMP', 'SL*', kind='interp', line=622)
W('27,3730', 0o00027, '', '', 'TFF1/ALF', '1/ALFA  E:(-22-2NA) M:(-20-2NA)', kind='operand', line=623)
W('27,3731', 0o57601, '', '', '0 -3,2', kind='operand', line=624)
W('27,3732', 0o52057, '', 'SL*', 'GOTO', kind='interp', line=625)
W('27,3733', 0o57602, '', '', '0 -4,2', kind='operand', line=626)
W('27,3734', 0o57641, '', '', 'ENDTFF', 'TFF SQRT(MU) IN MPAC E:(-45) M:(-42)', kind='operand', line=627)

# Page 1282
# PROGRAM NAME:  T(X)                           DATE:  01.17.67
# MOD NO:  0                                    LOG SECTION:  TIME OF FREE FALL
# MOD BY:  RR BAIRNSFATHER
#
# FUNCTIONAL DESCRIPTION:  THE POLYNOMIAL T(X) IS USED BY TIME OF FLIGHT SUBROUTINES CALCTFF AND
# CALCTPER TO APPROXIMATE THE SERIES
# 2     3
# 1/3 -X/5 +X /7 -X /9 ...
#
# WHERE   X = ALFA Z Z            IF ALFA Z Z LEQ 1
# X = 1/(ALFA Z Z)        IF ALFA Z Z G 1
#
# ALSO    X IS NEG FOR HYPERBOLIC ORBITS
# X = 0 FOR PARABOLIC ORBITS
# X IS POSITIVE FOR ELLIPTIC ORBITS
#
# FOR FLIGHT 278, THE POLYNOMIAL T(X) IS FITTED OVER THE RANGE (0,+1) AND HAS A MAXIMUM
# DEVIATION FROM THE SERIES OF 2 E-5.  (T(X) IS A CHEBYCHEV TYPE FIT AND WAS OBTAINED USING
# MAX PROGRAM AUTOCURFIT294RRB AND IS VALID TO THE SAME TOLERANCE OVER THE RANGE (-.08,+1).)
#
# CALLING SEQUENCE:     RTB
# T(X)
# C(MPAC) = X
#
# SUBROUTINE CALLED:  NONE
#
# NORMAL EXIT MODE:  TC TANZIG
#
# ALARMS:  NONE
#
# OUTPUT:  C(MPAC) = T(X)
#
# ERASABLE INITIALIZATION REQUIRED:
# C(MPAC) = X
#
# DEBRIS:  NONE

W('27,3735', 0o07222, 'T(X)', 'TC', 'POLY', line=667)
W('27,3736', 0o00004, '', 'DEC', '4', 'N-1', kind='data', line=668)
W('27,3737', 0o12525, '', '2DEC', '3.333333333 E-1', kind='data', line=669)
W('27,3740', 0o12525, kind='data', line=669)

W('27,3741', 0o71463, '', '2DEC*', '-1.999819135 E-1*', kind='data', line=671)
W('27,3742', 0o57703, kind='data', line=671)

W('27,3743', 0o04423, '', '2DEC*', '1.418148467 E-1*', kind='data', line=673)
W('27,3744', 0o17645, kind='data', line=673)

W('27,3745', 0o74604, '', '2DEC*', '-1.01310997 E-1*', kind='data', line=675)
W('27,3746', 0o43667, kind='data', line=675)

W('27,3747', 0o01626, '', '2DEC*', '5.609004986 E-2*', kind='data', line=677)
W('27,3750', 0o37256, kind='data', line=677)

W('27,3751', 0o77404, '', '2DEC*', '-1.536156925 E-2*', kind='data', line=679)
W('27,3752', 0o52071, kind='data', line=679)

W('27,3753', 0o06061, 'ENDT(X)', 'TC', 'DANZIG', line=681)

S('TCDANZIG', 'equals', 0o67753, line=683)

# Page 1283
# TFF CONSTANTS

#   BANK 32

#   SETLOC TOF-FF1
#   BANK

# # NOTE:  ADJUSTED MUE FOR NEAR EARTH TRAJ.
# MUE            =       3.990815471 E10         # M CUBE/CS SQ
# RTMUE          =       1.997702549 E5 B-18*    # MODIFIED EARTH MU
#
# # NOTE:  ADJUSTED MUE FOR NEAR EARTH TRAJ.
# MUM            =       4.902778 E8             # M CUBE/CS SQ
# RTMUM          2DEC*   2.21422176 E4 B-18*

W('27,3754', 0o06220, 'PI/16', '2DEC', '3.141592653 B-4', kind='data', line=701)
W('27,3755', 0o37553, kind='data', line=701)

W('27,3756', 0o37777, 'LIM(-22)', '2OCT', '3777737700', '1.0 -B(-22)', kind='data', line=703)
W('27,3757', 0o37700, kind='data', line=703)

W('27,3760', 0o00000, 'DP(-22)', '2OCT', '0000000100', 'B(-22)', kind='data', line=705)
W('27,3761', 0o00100, kind='data', line=705)

W('27,3762', 0o04000, 'DP2(-3)', '2DEC', '1 B-3', kind='data', line=707)
W('27,3763', 0o00000, kind='data', line=707)

W('27,3764', 0o02000, 'DP2(-4)', '2DEC', '1 B-4', '1/16', kind='data', line=709)
W('27,3765', 0o00000, kind='data', line=709)

# RPAD1         2DEC    6373338 B-29            # M (-29) = 20909901.57 FT

S('RPAD1', 'equals', 0o56314, line=713)

W('27,3766', 0o00305, 'R300K', '2DEC', '6464778 B-29', '(-29) M', kind='data', line=715)
W('27,3767', 0o11205, kind='data', line=715)

W('27,3770', 0o37777, 'NEARONE', '2DEC', '.999999999', kind='data', line=717)
W('27,3771', 0o37777, kind='data', line=717)

S('TFFZEROS', 'equals', 0o56521, line=719)
S('TFF1/4', 'equals', 0o56511, line=720)
