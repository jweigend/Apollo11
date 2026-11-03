"""TIME_OF_FREE_FALL.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/TIME_OF_FREE_FALL.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1373-1388 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TIME_OF_FREE_FALL', 'TIME_OF_FREE_FALL.agc', 'Comanche055', pages='1373-1388')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TIME_OF_FREE_FALL.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1373-1388
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Colossus249/ file of the same
# name, using Comanche055 page images.
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

# Page 1373
# THE TFF SUBROUTINES MAY BE USED IN EITHER EARTH OR MOON CENTERED COORDINATES.  THE TFF ROUTINES NEVER
# KNOW WHICH ORIGIN APPLIES.  IT IS THE USER WHO KNOWS, AND WHO SUPPLIES RONE, VONE AND 1/SQRT(MU) AT THE
# APPROPRIATE SCALE LEVEL FOR THE PROPER PRIMARY BODY.

# EARTH ORIGIN    POSITION        -29     METERS
# VELOCITY        -7      METERS/CENTISECOND
# 1/SQRT(MU)      +17     SQRT(CS SQ/METERS CUBED)

# MOON ORIGIN     POSITION        -27     METERS
# VELOCITY        -5      METERS/CENTISECONDS
# 1/SQRT(MU)      +14     SQRT(CS SQ/METERS CUBED)

# ALL DATA PROVIDED TO AND RECEIVED FROM ANY TFF SUBROUTINE WILL BE AT ONE OF THE LEVELS ABOVE.  IN ALL CASES,
# THE FREE FALL TIME IS RETURNED IN CENTISECONDS AT (-28).  PROGRAM TFF/CONIC WILL GENERATE VONE/RTMU AND
# LEAVE IT IN VONE' AT (+10) IF EARTH ORIGIN AND (+9) IF MOON ORIGIN.
# THE USER MUST STORE THE STATE VECTOR IN RONE, VONE AND MU IN THE FORM 1/SQRT(MU) IN TFF/RTMU
# AT THE PROPER SCALE BEFORE CALLING TFF/CONIC.  SINCE RONE, VONE ARE IN THE EXTENDED VERB STORAGE AREA,
# THE USER MUST ALSO LOCK OUT THE EXTENDED VERBS, AND RELEASE THEM WHEN FINISHED.
# PROGRAMS CALC/TFF AND CALC/TPER ASSUME THAT THE TERMINAL RADIUS IS LESS THAN THE PRESENT
# RADIUS.  THIS RESTRICTION CAN BE REMOVED BY A 15 W CODING CHANGE, BUT AT PRESENT IT IS NOT DEEMED NECESSARY.
#
# THE FOLLOWING ERASABLE QUANTITIES ARE USED BY THE TFF ROUTINES, AND ARE LOCATED IN THE PUSH LIST.
#

# BELOW   E:  IS USED FOR EARTH ORIGIN SCALE
# M:  IS USED FOR MOON  ORIGIN SCALE

# TFFSW          =       119D    # BIT1  0 = CALCTFF             1 = CALCTPER
S('TFFDELQ', 'equals', 0o12, line=60)  #       Q2-Q1                   E: (-16)  M: (-15)
S('RMAG1', 'equals', 0o14, line=61)  #       ABVAL(RN) M             E: (-29)  M: (-27)
# RPER           =       14D     #       PERIGEE RADIUS M        E: (-29)  M: (-27)
S('TFFQ1', 'equals', 0o16, line=63)  #       R.V / SQRT(MUE)         E: (-16)  M: (-15)
# SDELF/2                        #       SIN(THETA) /2
S('CDELF/2', 'equals', 0o16, line=65)  #       COS(THETA) /2
# RAPO           =       16D     #       APOGEE RADIUS M         E: (-29)  M: (-27)
S('NRTERM', 'equals', 0o20, line=67)  #       TERMINAL RADIUS M       E: (-29+NR)
# M: (-27+NR)
S('RTERM', 'equals', 0o22, line=69)  #       TERMINAL RADIUS M       E: (-29)  M: (-27)
S('TFFVSQ', 'equals', 0o24, line=70)  #       -(V SQUARED/MU)       1/M  E: (20)   M: (18)
S('TFF1/ALF', 'equals', 0o26, line=71)  #       SEMI MAJ AXIS  M        E: (-22-2 NA)
# M: (-20-2 NA)
S('TFFRTALF', 'equals', 0o30, line=73)  #       SQRT(ALFA)      E:(10+NA) M: (9+NA)
S('TFFALFA', 'equals', 0o32, line=74)  #       ALFA  1/M       E:(26-NR) M: (24-NR)
S('TFFNP', 'equals', 0o34, line=75)  #       SEMI LATUS RECTUM       M  E: (-38+2 NR)
# M: (-36+2 NR)
S('TFF/RTMU', 'equals', 0o36, line=77)  #       1/SQRT(MU)              E: (17)   M: (14)
S('NRMAG', 'equals', 0o40, line=78)  #       PRESENT RADIUS  M       E: (-29+NR)
# M: (-27+NR)
S('TFFX', 'equals', 0o42, line=80)
S('TFFTEM', 'equals', 0o44, line=81)  #       TEMPORARY
# Page 1374
# REGISTERS S1, S2 ARE UNTOUCHED BY ANY TFF SUBROUTINE
# INDEX REGISTERS X1, X2 ARE USED BY ALL TFF SUBROUTINES.  THEY ARE ESTAB-
# LISHED IN TFF/CONIC AND MUST BE PRESERVED BETWEEN CALLS TO SUBSEQUENT
# SUBROUTINES.
# -NR                             C(X1) = NORM COUNT OF RMAG
# -NA                             C(X2)= NORM COUNT OF SQRT(ABS(ALFA))

# Page 1375
# SUBROUTINE NAME:      TFFCONIC                                                DATE: 01.29.67
# MOD NO: 0                                                                     LOG SECTION: TIME OF FREE FALL
# MOD BY: RR BAIRNSFATHER
# MOD NO: 1             MOD BY: RR BAIRNSFATHER         DATE: 11 APR 67
# MOD NO: 2             MOD BY: RR BAIRNSFATHER         DATE: 21 NOV 67         ADD MOON MU.
# MOD NO: 3             MOD BY: RR BAIRNSFATHER         DATE: 21 MAR 68         ACCEPT DIFFERENT EARTH/MOON SCALES
# FUNCTIONAL DESCRIPTION:       THIS SUBROUTINE IS CALLED TO COMPUTE THOSE CONIC PARAMETERS REQUIRED BY THE TFF
# SUBROUTINES AND TO ESTABLISH THEM IN THE PUSH LIST AREA.  THE PARAMETERS ARE LISTED UNDER OUTPUT.
# THE EQUATIONS ARE:
# -   -  -
# H = RN*VN                       ANGULAR MOMENTUM
# - -
# LCP = H.H / MU                  SEMI LATUS RECTUM
# -  -
# ALFA = 2/RN - VN.VN / MU        RECIPROCAL SEMI MAJ AXIS, SIGNED

# AND ALFA IS POS FOR ELLIPTIC ORBITS
# 0 FOR PARABOLIC ORBITS
# NEG FOR HYPERBOLIC ORBITS.
# SUBROUTINE ALSO COMPUTES AND SAVES RMAG.
# CALLING SEQUENCE:
# TFFCONIC EXPECTS CALLER TO ENTER WITH CORRECT GRAVITATIONAL CONSTANT IN MPAC, IN THE FORM
# 1/SQRT(MU).  THE PROGRAM WILL SAVE IN TFF/RTMU .  THE SCALE IS DETERMINED BY WHETHER EARTH OR MOON
# ORIGIN IS USED.  THE CALLER MUST LOCK OUT THE EXTENDED VERBS BEFORE PROVIDING STATE VECTOR IN RONE,
# VONE AT PROPER SCALE.  THE EXTENDED VERBS MUST BE RESTORED WHEN THE CALLER IS FINISHED USING THE
# TFF ROUTINES.
# ENTRY POINT TFFCONMU EXPECTS THAT TFF/RTMU IS ALREADY LOADED.
# TO SPECIFY MU:  DLOAD   CALL            # IF MU ALREADY STORED:         CALL
# YOURMU  # 1/RTMU        E:(17) M:(14)                   TFFCONMU
# TFFCONIC
# PUSHLOC = PDL+0, ARBITRARY IF LEQ 18D

# SUBROUTINES CALLED:   NONE
# NORMAL EXIT MODES:    RVQ
# ALARMS:       NONE
# OUTPUT:       THE FOLLOWING ARE STORED IN THE PUSH LIST AREA.
# RMAG1   E:(-29) M:(-27) M  RN, PRESENT RADIUS LENGTH.
# NRMAG   E:(-29+NR)      M  RMAG, NORMALIZED
# M:(-27+NR)
# X1                      -NR, NORM COUNT
# TFFNP   E:(-38+2NR)     M  LCP, SEMI LATUS RECTUM, WEIGHTED BY NR.      FOR VGAMCALC
# M:(-36+2NR)
# TFF/RTMU E:(17) M:(14)          1/SQRT(MU)
# TFFVSQ E:(20) M:(18)    1/M  -(V SQ/MU): PRESENT VELOCITY,NORMLIZED.    FOR VGAMCALC
# TFFALFA E:(26-NR)       1/M  ALFA, WEIGHTED BY NR
# M:(24-NR)
# TFFRTALF E:(10+NA)      SQRT(ALFA), NORMALIZED
# M:(9+NA)
# Page 1376
# X2                      -NA, NORM COUNT
# TFF1/ALF E: (-22-2NA)   SIGNED SEMI MAJ AXIS, WEIGHTED BY NA
# M: (-20-2NA)
# PUSHLOC AT PDL+0
# THE FOLLOWING IS STORED IN GENERAL ERASABLE
# VONE'   E:(10) M:(9)    V/RT(MU), NORMALIZED VELOCITY
# ERASABLE INITIALIZATION REQUIRED:
# RONE    E:(-29) M:(-27) M       STATE VECTOR            LEFT BY CALLER
# VONE    E:(-7) M:(-5)   M/CS    STATE VECTOR            LEFT BY CALLER
# TFF/RTMU E:(17) M:(14)  1/RT(CS SQ/M CUBE)              IF ENTER VIA TFFCONMU.
# DEBRIS:       QPRET.          PDL+0 ... PDL+3
#

#   BANK 33
#   SETLOC TOF-FF
#   BANK

#   COUNT* $$/TFF

W('27,2757', 0o00037, 'TFFCONIC', 'STORE', 'TFF/RTMU', '1/SQRT(MU)            E: (17)  M: (14)', kind='interp', line=159)

W('27,2760', 0o53575, 'TFFCONMU', 'VLOAD', 'UNIT', 'COME HERE WITH TFFRTMU LOADED.', kind='interp', line=161)
W('27,2761', 0o02327, '', '', 'RONE', 'SAVED RN.  M          E: (-29) M: (-27)', kind='operand', line=162)
W('27,2762', 0o77725, '', 'PDDL', '', 'UR/2 TO PDL+0, +5', kind='interp', line=163)
W('27,2763', 0o00045, '', '', '36D', 'MAGNITUDE', kind='operand', line=164)
W('27,2764', 0o00015, '', 'STORE', 'RMAG1', 'M     E:(-29) M:(-27)', kind='interp', line=165)

W('27,2765', 0o77701, '', 'NORM', kind='interp', line=167)
W('27,2766', 0o00047, '', '', 'X1', '-NR', kind='operand', line=168)
W('27,2767', 0o24041, '', 'STOVL', 'NRMAG', 'RMAG  M  E: (-29+NR) M: (-27+NR)', kind='interp', line=169)
W('27,2770', 0o02335, '', '', 'VONE', 'SAVED VN.  M/CS       E: (-7) M: (-5)', kind='operand', line=170)
W('27,2771', 0o77761, '', 'VXSC', kind='interp', line=171)
W('27,2772', 0o00037, '', '', 'TFF/RTMU', 'E:(17) M:(14)', kind='operand', line=172)
W('27,2773', 0o02372, '', 'STORE', "VONE'", 'VN/SQRT(MU)  E: (10)  M: (9)', kind='interp', line=173)

W('27,2774', 0o47361, '', 'VXSC', 'VXV', kind='interp', line=175)
W('27,2775', 0o00041, '', '', 'NRMAG', 'E: (-29+NR) M: (-27+NR)', kind='operand', line=176)
# UR/2 FROM PDL
W('27,2776', 0o47572, '', 'VSL1', 'VSQ', 'BEFORE:  E:(-19+NR) M:(-18+NR)', kind='interp', line=178)
W('27,2777', 0o14035, '', 'STODL', 'TFFNP', 'LC P M    E:(-38+2NR) M:(-36+2NR)', kind='interp', line=179)
# SAVE ALSO FOR VGAMCALC
W('27,3000', 0o15325, '', '', 'TFF1/4', kind='operand', line=181)
W('27,3001', 0o63271, '', 'DDV', 'PDVL', '(2/RMAG)  1/M  E:(26-NR)      M:(24-NR)', kind='interp', line=182)
W('27,3002', 0o00041, '', '', 'NRMAG', 'RMAG  M  E:(-29+NR)   M:(-27+NR)', kind='operand', line=183)
W('27,3003', 0o02372, '', '', "VONE'", 'SAVED VN.  E:(10)     M:(9)', kind='operand', line=184)
W('27,3004', 0o57436, '', 'VSQ', 'DCOMP', 'KEEP MPAC+2 HONEST FOR SQRT.', kind='interp', line=185)
W('27,3005', 0o00025, '', 'STORE', 'TFFVSQ', '-(V SQ/MU)  E:(20)    M:(18)', kind='interp', line=186)
# SAVE FOR VGAMCALC
W('27,3006', 0o43257, '', 'SR*', 'DAD', kind='interp', line=188)
# Page 1377
W('27,3007', 0o20573, '', '', '0 -6,1', 'GET -VSQ/MU  E:(26-NR) M:(24-NR)', kind='operand', line=190)
W('27,3010', 0o77626, '', 'STADR', kind='interp', line=191)
# 2/RMAG  FROM PDL+2
W('27,3011', 0o77744, '', 'STORE', 'TFFALFA', 'ALFA  1/M  E:(26-NR) M:(24-NR)', kind='interp', line=193)
W('27,3012', 0o41457, '', 'SL*', 'PUSH', 'TEMP SAVE ALFA  E:(20)  M:(18)', kind='interp', line=194)
W('27,3013', 0o20173, '', '', '0 -6,1', kind='operand', line=195)
W('27,3014', 0o75446, '', 'ABS', 'SQRT', 'E:(10) M:(9)', kind='interp', line=196)
W('27,3015', 0o77701, '', 'NORM', kind='interp', line=197)
W('27,3016', 0o00050, '', '', 'X2', 'X2 = -NA', kind='operand', line=198)
W('27,3017', 0o00031, '', 'STORE', 'TFFRTALF', 'SQRT( ABS(ALFA) )  E:(10+NA) M:(9+NA)', kind='interp', line=199)
W('27,3020', 0o75316, '', 'DSQ', 'SIGN', 'NOT SO ACCURATE, BUT OK', kind='interp', line=200)
# ALFA FROM PDL+2  E:(20) M:(18)
W('27,3021', 0o55254, '', 'BZE', 'BDDV', 'SET 1/ALFA =0, TO SHOW SMALL ALFA', kind='interp', line=202)
W('27,3022', 0o57024, '', '', '+2', kind='operand', line=203)
W('27,3023', 0o15325, '', '', 'TFF1/4', kind='operand', line=204)
W('27,3024', 0o00027, '', 'STORE', 'TFF1/ALF', '1/ALFA  E:(-22-2 NA)  M:(-20-2 NA)', kind='interp', line=205)
W('27,3025', 0o77616, 'DUMPCNIC', 'RVQ', kind='interp', line=206)
# 39 W
# Page 1378
# SUBROUTINE NAME:      TFFRP/RA                                                DATE: 01.17.67
# MOD NO: 0                                                                     LOG SECTION:    TIME OF FREE FALL
# MOD NO: 1             MOD BY: RR BAIRNSFATHER         DATE: 11 APR 67
# MOD NO: 2             MOD BY: RR BAIRNSFATHER         DATE: 21 MAR 68         ACCEPT DIFFERENT EARTH/MOON SCALES
# ALSO IMPROVE ACCURACY OF RAPO.
# FUNCTIONAL DESCRIPTION:       USED BY CALCTPER AND TFF DISPLAYS TO CALCULATE PERIGEE RADIUS AND ALSO
# APOGEE RADIUS FOR A GENERAL CONIC.
# PROGRAM GIVES PERIGEE RADIUS AS         APOGEE RADIUS IS GIVEN BY
# RP = P /(1+E)                           RA = (1+E) / ALFA
# WHERE    2
# E  = 1 - P ALFA
# IF RA IS NEGATIVE OR SHOWS DIVIDE OVERFLOW, THEN RA = POSMAX BECAUSE
# 1. APOGEE RADIUS IS NOT MEANINGFUL FOR HYPERBOLA
# 2. APOGEE RADIUS IS NOT DEFINED FOR PARABOLA
# 3. APOGEE RADIUS EXCEEDS THE SCALING FOR ELLIPSE.
# THIS SUBROUTINE REQUIRED THE SIGNED RECIPROCAL SEMI MAJ AXIS, ALFA, AND SEMI LATUS RECTUM AS DATA.
# CALLING SEQUENCE: CALL
# TFFRP/RA
# PUSHLOC = PDL+0, ARBITRARY IF LEQ 10D
# C(MPAC) UNSPECIFIED

# SUBROUTINES CALLED:   NONE
# NORMAL EXIT MODE:     RVQ
# IF ELLIPSE, WITHIN NORMAL SCALING, RAPO IS CORRECT.
# OTHERWISE, RAPO = POSMAX.
# ALARMS:       NONE
# OUTPUT:       STORED IN PUSH LIST AREA. SCALE OF OUTPUT AGREES WITH DATA SUPPLIED TO TFF/CONIC.
# RPER    E:(-29) M:(-27)  M      PERIGEE RADIUS          DESTROYED BY CALCTFF/CALCTPER, TFFTRIG.
# RAPO    E:(-29) M:(-27)  M      APOGEE RADIUS           WILL BE DESTROYED BY CALCTFF/CALCTPER
# PUSHLOC AT PDL+0
# ERASABLE INITIALIZATION REQUIRED:
# TFFALFA E:(26-NR)       M       1/SEMI MAJ AXIS         LEFT BY TFFCONIC
# M:(24-NR)
# TFFNP   E: (-38+2NR)    M       LC P, SEMI LATUS RECTUM LEFT BY TFFCONIC
# M: (-36+2NR)
# X1                      -NR, NORM COUNT OF RMAG         LEFT BY TFFCONIC
# X2                      -NA, NORM COUNT OF ALFA         LEFT BY TFFCONIC
# DEBRIS:       QPRET, PDL+0 ... PDL+1

# Page 1379
S('RAPO', 'equals', 0o20, line=249)  # APOGEE RADIUS  M  E:(-29) M:(-27)
S('RPER', 'equals', 0o16, line=250)  # PERIGEE RADIUS  M  E:(-29) M:(-27)

W('27,3026', 0o41345, 'TFFRP/RA', 'DLOAD', 'DMP', kind='interp', line=252)
W('27,3027', 0o00033, '', '', 'TFFALFA', 'ALFA  1/M  E:(26-NR) M:(24-NR)', kind='operand', line=253)
W('27,3030', 0o00035, '', '', 'TFFNP', 'LC P  M   E:(-38+2NR) M:(-36+2NR)', kind='operand', line=254)
W('27,3031', 0o57457, '', 'SR*', 'DCOMP', 'ALFA P (-12+NR)', kind='interp', line=255)
W('27,3032', 0o20571, '', '', '0 -8D,1', 'ALFA P (-4)', kind='operand', line=256)
W('27,3033', 0o51415, '', 'DAD', 'ABS', '(DCOMP GIVES VALID TP RESULT FOR SQRT)', kind='interp', line=257)
# (ABS PROTECTS SQRT IF E IS VERY NEAR 0)
W('27,3034', 0o17366, '', '', 'DP2(-4)', kind='operand', line=259)
W('27,3035', 0o43366, '', 'SQRT', 'DAD', 'E SQ = (1- P ALFA)    (-4)', kind='interp', line=260)
W('27,3036', 0o15325, '', '', 'TFF1/4', kind='operand', line=261)
W('27,3037', 0o55206, '', 'PUSH', 'BDDV', '(1+E)  (-2)  TO PDL+0', kind='interp', line=262)
W('27,3040', 0o00035, '', '', 'TFFNP', 'LCP  M E:(-38+2NR)    M:(-36+2NR)', kind='operand', line=263)
W('27,3041', 0o53657, '', 'SR*', 'SR*', '(DOES SR THEN SL TO AVOID OVFL)', kind='interp', line=264)
W('27,3042', 0o20601, '', '', '0,1', 'X1=-NR', kind='operand', line=265)
W('27,3043', 0o20572, '', '', '0 -7,1', '(EFFECTIVE SL)', kind='operand', line=266)
W('27,3044', 0o14017, '', 'STODL', 'RPER', 'PERIGEE RADIUS  M  E:(-29) M:(-27)', kind='interp', line=267)
# (1+E)  (-2)  FROM PDL+0
W('27,3045', 0o41005, '', 'DMP', 'BOVB', kind='interp', line=269)
W('27,3046', 0o00027, '', '', 'TFF1/ALF', 'E:(-22-2NA) M:(-20-2NA)', kind='operand', line=270)
W('27,3047', 0o57352, '', '', 'TCDANZIG', 'CLEAR OVFIND, IF ON.', kind='operand', line=271)
W('27,3050', 0o53654, '', 'BZE', 'SL*', kind='interp', line=272)
W('27,3051', 0o57060, '', '', 'MAXRA', 'SET POSMAX, IF ALFA=0', kind='operand', line=273)
W('27,3052', 0o57603, '', '', '0 -5,2', '-5+NA', kind='operand', line=274)
W('27,3053', 0o40057, '', 'SL*', 'BOV', kind='interp', line=275)
W('27,3054', 0o57576, '', '', '0,2', kind='operand', line=276)
W('27,3055', 0o57060, '', '', 'MAXRA', 'SET POSMAX IF OVFL.', kind='operand', line=277)
W('27,3056', 0o77644, '', 'BPL', '', 'CONTINUE WITH VALID RAPO.', kind='interp', line=278)
W('27,3057', 0o57062, '', '', '+3', kind='operand', line=279)
W('27,3060', 0o77745, 'MAXRA', 'DLOAD', '', 'RAPO CALC IS NOT VALID.  SET RAPO =', kind='interp', line=280)
W('27,3061', 0o17372, '', '', 'NEARONE', 'POSMAX AS A TAG.', kind='operand', line=281)
W('27,3062', 0o00021, '', 'STORE', 'RAPO', 'APOGEE RADIUS  M  E:(-29)     M:(-27)', kind='interp', line=282)
W('27,3063', 0o77616, 'DUMPRPRA', 'RVQ', kind='interp', line=283)

# 30 W
# Page 1380
# SUBROUTINE NAME:      CALCTPER / CALCTFF                                      DATE:   01.29.67
# MOD NO: 0                                                                     LOG SECTION:    TIME OF FREE FALL
# MOD BY: RR BAIRNSFATHER
# MOD NO: 1             MOD BY: RR BAIRNSFATHER         DATE: 21 MAR 67
# MOD NO: 2             MOD BY: RR BAIRNSFATHER         DATE: 14 APR 67
# MOD BY: 3             MOD BY: RR BAIRNSFATHER         DATE: 8 JUL 67          NEAR EARTH MUE AND NEG TFF (GONEPAST)
# MOD BY: 4             MOD BY: RR BAIRNSFATHER         DATE: 21 NOV 67         ADD VARIABLE MU.
# MOD BY: 5             MOD BY: RR BAIRNSFATHER         DATE: 21 MAR 68         ACCEPT DIFFERENT EARTH/MOON SCALES
# FUNCTIONAL DESCRIPTION:       PROGRAM CALCULATES THE FREE-FALL TIME OF FLIGHT FROM PRESENT POSITION RN AND
# VELOCITY VN TO A RADIUS LENGTH SPECIFIED BY RTERM , SUPPLIED BY THE USER.  THE POSITION VECTOR
# RN MAY BE ON EITHER SIDE OF THE CONIC, BUT RTERM IS CONSIDERED ON THE INBOUND SIDE.
# THE EQUATIONS ARE

# Q2 = -SQRT(RTERM (2-RTERM ALFA) - LCP)  (INBOUND SIDE)) LEQ +- LCE/SQRT(ALFA)
# -  -
# Q1 = RN.VN / SQRT(MU)                                   LEQ +- LCE/SQRT(ALFA)

# Z = NUM / DEN                                           LEQ +- 1/SQRT(ALFA)

# WHERE, IF INBOUND
# NUM = RTERM -RN                                         LEQ +- 2 LCE/ALFA
# DEN = Q2+Q1                                             LEQ +- 2 LCE/SQRT(ALFA)

# AND, IF OUTBOUND
# NUM = Q2-Q1                                             LEQ +- 2 LCE/SQRT(ALFA)
# DEN = 2 - ALFA (RTERM + RN) .                           LEQ +- 2 LCE

# IF      ALFA ZZ < 1.0           (FOR ALL CONICS EXCEPT ELLIPSES HAVING ABS(DEL ECC ANOM) G 90 DEG)

# THEN    X = ALFA Z Z
# AND     TFF = (RTERM +RN -2 ZZ T(X) ) Z/SQRT(MU)

# EXCEPT  IF ALFA PNZ, AND IF TFF NEG,
# THEN    TFF = 2 PI /(ALFA SQRT(ALFA)) + TFF

# OR IF   ALFA ZZ GEQ 1.0         (FOR ELLIPSES HAVING ABS(DEL ECC ANOM) GEQ 90 DEG)

# THEN    X = 1/ALFA Z Z
# AND     TFF = (PI/SQRT(ALFA) -Q2 +Q1 +2(X T(X) -1) /ALFA Z) /ALFA SQRT(MU)

# WHERE   T(X) IS A POLYNOMIAL APPROXIMATION TO THE SERIES
# 2     3                        2
# 1/3 -X/5 +X /7 -X /9...                 (X < 1.0)

# CALLING SEQUENCE:     TIME TO RTERM                   TIME TO PERIGEE
# CALL                            CALL
# CALCTFF                         CALCTPER
# C(MPAC) = TERMNL RAD M          C(MPAC) = PERIGEE RAD M
# FOR EITHER,     E: (-29)        M: (-27)
# FOR EITHER, PUSHLOC = PDL+0 , ARBITRARY IF LEQ 8D.
# Page 1381
#
# SUBROUTINES CALLED:   T(X), VIA RTB
# NORMAL EXIT MODE: RVQ
# HOWEVER, PROGRAM EXITS WITH ONE OF THE FOLLOWING VALUES FOR TFF (-28) CS IN MPAC.  USER MUST STORE.
# A. TFF = FLIGHT TIME.  NORMAL CASE FOR POSITIVE FLIGHT TIME LESS THAN ONE ORBITAL PERIOD.
# B. (THIS OPTION IS NO LONGER USED.)
# C. TFF = POSMAX.  THIS INDICATES THAT THE CONIC FROM THE PRESENT POSITION WILL NOT RETURN TO
# THE SPECIFIED ALTITUDE.  ALSO INDICATES OUTBOUND PARABOLA OR HYPERBOLA.
# OUTPUT:       C(MPAC)         (-28) CS        TIME OF FLIGHT, OR TIME TO PERIGEE
# TFFX            (0)             X,                                      LEFT FOR ENTRY DISPLAY TFF ROUTINES
# NRTERM          E: (-29+NR)     M RTERM, WEIGHTED BY NR                 LEFT FOR ENTRY DISPLAY TFF ROUTINES
# M: (-27+NR)
# TFFTEM          E: (-59+2NR)    LCP Z Z SGN(SDELF)                      LEFT FOR ENTRY DISPLAY TFF ROUTINES
# M: (-55+2NR)    LCP /ALFA SGN(SDELF)                    LEFT FOR ENTRY DISPLAY TFF ROUTINES
# NOTE:   TFFTEM = PDL 36D AND WILL BE DESTROYED BY .:UNIT:.
# RMAG1   E:(-29) M:(-27) PDL 12 NOT TOUCHED.
# TFFQ1   E:(-16) M:(-15) PDL 14D
# TFFDELQ E:(-16) M:(-15) PDL 10D
# PUSHLOC AT PDL+0
# ERASABLE INITIALIZATION REQUIRED:
# RONE    E:(-29) M:(-27) M  STATE VECTOR                                 LEFT BY USER
# VONE'   E:(+10) M:(+9)  VN/SQRT(NU)                                     LEFT BY TFF/CONIC
# RMAG1   E:(-29) M:(-27) PRESENT RADIUS, M                               LEFT BY TFFCONIC
# C(MPAC) E:(-29) M:(-27) RTERM, TERMINAL RADIUS LENGTH, M                LEFT BY USER
#
# THE FOLLOWING ARE STORED IN THE PUSH LIST AREA.
# TFF/RTMU        E:(17) M:(14)   1/SQRT(MU)                              LEFT BY TFFCONIC.
# NRMAG   E: (-29+NR)     M RMAG, NORMALIZED                              LEFT BY TFFCONIC
# M: (-27+NR)
# X1                        -NR, NORM COUNT                               LEFT BY TFFCONIC
# TFFNP   E: (-38+2NR)    M   LCP, SEMI LATUS RECTUM, WEIGHT NR           LEFT BY TFFCONIC
# M: (-36+2NR)
# TFFALFA  E: (26-NR)       1/M  ALFA, WEIGHT NR                          LEFT BY TFFCONIC
# M: (24-NR)
# TFFRTALF  E:(10+NA)       SQRT(ALFA), NORMALIZED                        LEFT BY TFFCONIC
# M:(9+NA)
# X2                        -NA, NORM COUNT                               LEFT BY TFFCONIC
# TFF1/ALF        E:(-22-2NA)     SIGNED SEMIMAJ AXIS, WEIGHTED BY NA     LEFT BY TFFCONIC
# M:(-20-2NA)
# DEBRIS:       QPRET, PDL+0 ... PDL+3
# RTERM   E:(-29) M:(-27) RTERM, TERMINAL RADIUS LENGTH
# RAPO    E:(-29) M:(-27) PDL 16D (=NRTERM)
# RPER    E:(-29) M:(-27) PDL 14D  (=TFFQ1)

# Page 1382
W('27,3064', 0o77614, 'CALCTPER', 'SETGO', '', 'ENTER WITH RPER IN MPAC', kind='interp', line=383)
W('27,3065', 0o03436, '', '', 'TFFSW', kind='operand', line=384)
W('27,3066', 0o57071, '', '', '+3', kind='operand', line=385)
W('27,3067', 0o77614, 'CALCTFF', 'CLEAR', '', 'ENTER WITH RTERM IN MPAC', kind='interp', line=386)
W('27,3070', 0o03676, '', '', 'TFFSW', kind='operand', line=387)
W('27,3071', 0o00023, '', 'STORE', 'RTERM', 'E: (-29) M: (-27)', kind='interp', line=388)
W('27,3072', 0o77657, '', 'SL*', kind='interp', line=389)
W('27,3073', 0o20201, '', '', '0,1', 'X1=-NR', kind='operand', line=390)
W('27,3074', 0o00021, '', 'STORE', 'NRTERM', 'RTERM  E: (-29+NR) M: (-27+NR)', kind='interp', line=391)
W('27,3075', 0o44205, '', 'DMP', 'BDSU', kind='interp', line=392)
W('27,3076', 0o00033, '', '', 'TFFALFA', 'ALFA  E:(26-NR) M:(24-NR)', kind='operand', line=393)
W('27,3077', 0o15325, '', '', 'TFF1/4', kind='operand', line=394)
W('27,3100', 0o41206, '', 'PUSH', 'DMP', '(2-ALFA RTERM)  (-3)  TO PDL+0', kind='interp', line=395)
W('27,3101', 0o00021, '', '', 'NRTERM', 'E: (-29+NR) M: (-27+NR)', kind='operand', line=396)
W('27,3102', 0o53725, '', 'PDDL', 'SR*', 'RTERM(2-ALFA RTERM) TO PDL+2', kind='interp', line=397)
# E: (-32+NR) M: (-30+NR)
W('27,3103', 0o00035, '', '', 'TFFNP', 'LC P  E:(-38+2NR) M:(-36+2NR)', kind='operand', line=399)
W('27,3104', 0o20573, '', '', '0 -6,1', 'X1 = -NR', kind='operand', line=400)
W('27,3105', 0o43276, '', 'DCOMP', 'DAD', 'DUE TO SHIFTS, KEEP PRECISION FOR SQRT', kind='interp', line=401)
# RTERM(2-ALFA RTERM) FROM PDL+2
# E: (-32+NR) M: (-30+NR)
W('27,3106', 0o77657, '', 'SR*', '', 'LEAVE  E: (-32) M: (-30)', kind='interp', line=404)
W('27,3107', 0o20601, '', '', '0,1', 'X1 = -NR', kind='operand', line=405)
W('27,3110', 0o71214, '', 'BOFF', 'DLOAD', 'CHECK TFF / TPER SWITCH', kind='interp', line=406)
W('27,3111', 0o03756, '', '', 'TFFSW', kind='operand', line=407)
W('27,3112', 0o57114, '', '', '+2', 'IF TFF, CONTINUE', kind='operand', line=408)
W('27,3113', 0o15335, '', '', 'TFFZEROS', 'IF TPER, SET Q2 = 0', kind='operand', line=409)
W('27,3114', 0o75440, '', 'BMN', 'SQRT', 'E: (-16) M: (-15)', kind='interp', line=410)

W('27,3115', 0o57247, '', '', 'MAXTFF1', 'NO FREE FALL CONIC TO RTERM FROM HERE', kind='operand', line=412)
# RESET PDL, SET TFF=POSMAX, AND EXIT.

W('27,3116', 0o41076, '', 'DCOMP', 'BOVB', 'RT IS ON INBOUND SIDE.  ASSURE OVFIND=0', kind='interp', line=415)
W('27,3117', 0o57352, '', '', 'TCDANZIG', 'ANY PORT IN A STORM.', kind='operand', line=416)
W('27,3120', 0o24045, '', 'STOVL', 'TFFTEM', 'Q2  E: (-16) M: (-15)', kind='interp', line=417)
W('27,3121', 0o02372, '', '', "VONE'", 'VN/SQRT(MU)  E: (10) M: (9)', kind='operand', line=418)
W('27,3122', 0o52441, '', 'DOT', 'SL3', kind='interp', line=419)
W('27,3123', 0o02327, '', '', 'RONE', 'SAVED RN.  E: (-29) M: (-27)', kind='operand', line=420)
W('27,3124', 0o00017, '', 'STORE', 'TFFQ1', 'Q1, SAVE FOR GONEPAST TEST.', kind='interp', line=421)
# E: (-16) M: (-15)
W('27,3125', 0o44240, '', 'BMN', 'BDSU', kind='interp', line=423)
W('27,3126', 0o57147, '', '', 'INBOUND', 'USE ALTERNATE Z', kind='operand', line=424)
W('27,3127', 0o00045, '', '', 'TFFTEM', 'Q2  E: (-16) M: (-15)', kind='operand', line=425)

# OUTBOUND Z CALC CONTINUES HERE

W('27,3130', 0o14043, '', 'STODL', 'TFFX', 'NUM=Q2-Q1  E: (-16) M: (-15)', kind='interp', line=429)
W('27,3131', 0o00033, '', '', 'TFFALFA', 'ALFA  E: (26-NR) M: (24-NR)', kind='operand', line=430)
W('27,3132', 0o44205, '', 'DMP', 'BDSU', kind='interp', line=431)
# Page 1383
W('27,3133', 0o00041, '', '', 'NRMAG', 'RMAG  E: (-29+NR) M: (-27+NR)', kind='operand', line=433)
# (2-RTERM ALFA)  (-3) FROM PDL+0
W('27,3134', 0o51406, 'SAVEDEN', 'PUSH', 'ABS', 'DEN TO PDL+0  E: (-3) OR (-16)', kind='interp', line=435)
# M: (-3) OR (-15)
W('27,3135', 0o40015, '', 'DAD', 'BOV', 'INDETERMINANCY TEST', kind='interp', line=437)
W('27,3136', 0o17360, '', '', 'LIM(-22)', '=1.0-B(-22)', kind='operand', line=438)
W('27,3137', 0o57160, '', '', 'TFFXTEST', 'GO IF DEN >/= B(-22)', kind='operand', line=439)
W('27,3140', 0o65345, '', 'DLOAD', 'PDDL', 'SET DEN=0 OTHERWISE', kind='interp', line=440)
W('27,3141', 0o15335, '', '', 'TFFZEROS', kind='operand', line=441)
# XCH ZERO WITH PDL+0
W('27,3142', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=443)
W('27,3143', 0o00033, '', '', 'TFFALFA', 'ALFA  E: (26-NR) M:( 24-NR)', kind='operand', line=444)
W('27,3144', 0o71240, '', 'BMN', 'DLOAD', 'FOR TPER:  Z INDET AT DELE/2=0 AND 90.', kind='interp', line=445)
W('27,3145', 0o57254, '', '', 'TFFEL1', 'ASSUME 90, AND LEAVE 0 IN PDL: 1/Z=D/N', kind='operand', line=446)

# Z INDET. AT PERIGEE FOR PARAB OR HYPERB.
W('27,3146', 0o77616, 'DUMPTFF1', 'RVQ', '', 'RETURN TFF =0', kind='interp', line=449)

# INBOUND Z CALC CONTINUES HERE
W('27,3147', 0o77745, 'INBOUND', 'DLOAD', '', 'RESET PDL+0', kind='interp', line=452)
W('27,3150', 0o45345, '', 'DLOAD', 'DSU', 'ALTERNATE Z CALC', kind='interp', line=453)
W('27,3151', 0o00023, '', '', 'RTERM', 'E: (-29) M: (-27)', kind='operand', line=454)
W('27,3152', 0o00015, '', '', 'RMAG1', 'E: (-29) M: (-27)', kind='operand', line=455)
W('27,3153', 0o14043, '', 'STODL', 'TFFX', 'NUM=RTERM-RN  E: (-29) M: (-27)', kind='interp', line=456)
W('27,3154', 0o00045, '', '', 'TFFTEM', 'Q2  E: (-16)  M: (-15)', kind='operand', line=457)
W('27,3155', 0o52015, '', 'DAD', 'GOTO', kind='interp', line=458)
W('27,3156', 0o00017, '', '', 'TFFQ1', 'Q1  E: (-16) M: (-15)', kind='operand', line=459)
W('27,3157', 0o57134, '', '', 'SAVEDEN', 'DEN = Q2+Q1  E: (-16) M: (-15)', kind='operand', line=460)

W('27,3160', 0o65215, 'TFFXTEST', 'DAD', 'PDDL', '(ABS(DEN) TO PDL+2))  E: (-3) OR (-16)', kind='interp', line=462)
# M: (-3) OR (-15)
W('27,3161', 0o17362, '', '', 'DP(-22)', 'RESTORE ABS(DEN) TO MPAC', kind='operand', line=464)
W('27,3162', 0o00043, '', '', 'TFFX', 'NUM E:(-16) OR (-29) M:(-15) OR (-27)', kind='operand', line=465)
W('27,3163', 0o53605, '', 'DMP', 'SR*', kind='interp', line=466)
W('27,3164', 0o00031, '', '', 'TFFRTALF', 'SQRT(ALFA)  E:(10+NA) M:(9+NA)', kind='operand', line=467)
W('27,3165', 0o57201, '', '', '0 -3,2', 'X2=-NA', kind='operand', line=468)
W('27,3166', 0o77671, '', 'DDV', '', 'C(MPAC) =NUM SQRT(ALFA)       E:(-3) OR (-16)', kind='interp', line=469)
# M:(-3) OR (-15)
# ABS(DEN) FROM PDL+2   E:(-3) OR (-16)
# M:(-3) OR (-15)
W('27,3167', 0o40145, '', 'DLOAD', 'BOV', '(THE DLOAD IS SHARED WITH TFFELL)', kind='interp', line=473)
W('27,3170', 0o00043, '', '', 'TFFX', 'NUM  E: (-16) OR (-29)  M:(-15) OR (-27)', kind='operand', line=474)
W('27,3171', 0o57252, '', '', 'TFFELL', 'USE EQN FOR DELE GEQ 90, LEQ -90', kind='operand', line=475)

# OTHERWISE, CONTINUE FOR GENERAL CONIC FOR TFF EQN

W('27,3172', 0o45471, '', 'DDV', 'STADR', kind='interp', line=479)
# DEN FROM PDL+0        E: (-3) OR (-16)
# M: (-3) OR (-15)
W('27,3173', 0o77732, '', 'STORE', 'TFFTEM', 'Z SAVE FOR SIGN OF SDELF.', kind='interp', line=482)
# Page 1384
# E: (-13) M: (-12)
W('27,3174', 0o63406, '', 'PUSH', 'DSQ', 'Z TO PDL+0', kind='interp', line=485)
W('27,3175', 0o41206, '', 'PUSH', 'DMP', 'Z SQ TO PDL+2  E: (-26) M: (-24)', kind='interp', line=486)
W('27,3176', 0o00035, '', '', 'TFFNP', 'LC P  E: (-38+2NR) M: (-36+2NR)', kind='operand', line=487)
W('27,3177', 0o75261, '', 'SL', 'SIGN', kind='interp', line=488)
W('27,3200', 0o20206, '', '', '5', kind='operand', line=489)
W('27,3201', 0o00045, '', '', 'TFFTEM', 'AFFIX SIGN FOR SDELF (ENTRY DISPLAY)', kind='operand', line=490)
W('27,3202', 0o14045, '', 'STODL', 'TFFTEM', 'P ZSQ  E: (-59+2NR) M: (-55+2NR)', kind='interp', line=491)
# (ARG IS USED IN TFF/TRIG)
# ZSQ FROM PDL+2  E: (-26) M: (-24)
W('27,3203', 0o41206, '', 'PUSH', 'DMP', 'RESTORE PUSH LOC', kind='interp', line=494)
W('27,3204', 0o00033, '', '', 'TFFALFA', 'ALFA  E: (26-NR) M: (24-NR)', kind='operand', line=495)
W('27,3205', 0o77657, '', 'SL*', kind='interp', line=496)
W('27,3206', 0o20201, '', '', '0,1', 'X1=-NR', kind='operand', line=497)
W('27,3207', 0o00043, '', 'STORE', 'TFFX', 'X', kind='interp', line=498)
W('27,3210', 0o41234, '', 'RTB', 'DMP', kind='interp', line=499)
W('27,3211', 0o57334, '', '', 'T(X)', 'POLY', kind='operand', line=500)
# ZSQ FROM PDL+2  E: (-26) M: (-24)
W('27,3212', 0o44302, '', 'SR2', 'BDSU', '2 ZSQ T(X)  E: (-29) M: (-27)', kind='interp', line=502)
W('27,3213', 0o00023, '', '', 'RTERM', 'RTERM  E: (-29) M: (-27)', kind='operand', line=503)
W('27,3214', 0o41215, '', 'DAD', 'DMP', kind='interp', line=504)
W('27,3215', 0o00015, '', '', 'RMAG1', 'E: (-29) M: (-27)', kind='operand', line=505)
# Z FROM PDL+0  E: (-13) M: (-12)
W('27,3216', 0o51042, '', 'SR3', 'BPL', 'TFF SQRT(MU)  E: (-45) M: (-42)', kind='interp', line=507)
W('27,3217', 0o57240, '', '', 'ENDTFF', '(NO PUSH UP)', kind='operand', line=508)
W('27,3220', 0o75206, '', 'PUSH', 'SIGN', 'TFF SQRT(MU) TO PDL+0', kind='interp', line=509)
W('27,3221', 0o00017, '', '', 'TFFQ1', 'Q1 FOR GONEPAST TEST', kind='operand', line=510)
W('27,3222', 0o71244, '', 'BPL', 'DLOAD', 'GONE PAST ?', kind='interp', line=511)
W('27,3223', 0o57244, '', '', 'NEGTFF', 'YES. TFF < 0 .', kind='operand', line=512)
W('27,3224', 0o00027, '', '', 'TFF1/ALF', '1/ALFA  E: (-22-2NA) M: (-20-2NA)', kind='operand', line=513)
W('27,3225', 0o51076, '', 'DCOMP', 'BPL', 'ALFA > 0 ?', kind='interp', line=514)
W('27,3226', 0o57244, '', '', 'NEGTFF', 'NO. TFF IS NEGATIVE.', kind='operand', line=515)

# CORRECT FOR ORBITAL PERIOD.

W('27,3227', 0o77676, '', 'DCOMP', '', 'YES.  CORRECT FOR ORB PERIOD.', kind='interp', line=519)
W('27,3230', 0o56205, '', 'DMP', 'DDV', kind='interp', line=520)
W('27,3231', 0o17356, '', '', 'PI/16', '2 PI (-5)', kind='operand', line=521)
W('27,3232', 0o00031, '', '', 'TFFRTALF', 'SQRT(ALFA)  E: (10+NA) M: (9+NA)', kind='operand', line=522)
W('27,3233', 0o53657, '', 'SL*', 'SL*', kind='interp', line=523)
W('27,3234', 0o57602, '', '', '0 -4,2', 'X2=-NA', kind='operand', line=524)
W('27,3235', 0o57602, '', '', '0 -4,2', kind='operand', line=525)
W('27,3236', 0o43257, '', 'SL*', 'DAD', kind='interp', line=526)
W('27,3237', 0o57576, '', '', '0,2', kind='operand', line=527)
# TFF SQRT(MU) FROM PDL+0       E:(-45) M:(-42)
W('27,3240', 0o40005, 'ENDTFF', 'DMP', 'BOV', 'TFF SQRT(MU) IN MPAC          E:(-45) M:(-42)', kind='interp', line=529)
W('27,3241', 0o00037, '', '', 'TFF/RTMU', 'E: (17) M: (14)', kind='operand', line=530)
W('27,3242', 0o57250, '', '', 'MAXTFF', 'SET POSMAX IN OVFL.', kind='operand', line=531)

W('27,3243', 0o77616, 'DUMPTFF2', 'RVQ', '', 'RETURN TFF    (-28) CS IN MPAC.', kind='interp', line=533)

# Page 1385
W('27,3244', 0o77745, 'NEGTFF', 'DLOAD', kind='interp', line=536)
# TFF SQRT(MU) FROM PDL+0, NEGATIVE.
W('27,3245', 0o77650, '', 'GOTO', kind='interp', line=538)
W('27,3246', 0o57240, '', '', 'ENDTFF', kind='operand', line=539)

W('27,3247', 0o77745, 'MAXTFF1', 'DLOAD', '', 'RESET PDL', kind='interp', line=541)
W('27,3250', 0o43545, 'MAXTFF', 'DLOAD', 'RVQ', kind='interp', line=542)
W('27,3251', 0o17372, '', '', 'NEARONE', kind='operand', line=543)

# TIME OF FLIGHT ELLIPSE WHEN DEL (ECCENTRIC ANOM) GEQ 90 AND LEQ -90.

# NUM FROM TFFX. E: (-16) OR (-29)
# M: (-15) OR (-27)
W('27,3252', 0o77712, 'TFFELL', 'SL2', '', 'NUM E:(-14) OR (-27)  M:(-13) OR (-25)', kind='interp', line=549)
W('27,3253', 0o41465, '', 'BDDV', 'PUSH', 'TEMP SAVE D/N IN PDL+0', kind='interp', line=550)
# DEN FROM PDL+0  E:(-3)/( 16)  M:(-3)/(-15)
# N/D TO PDL+0  E: (11) M: (10)
W('27,3254', 0o45345, 'TFFEL1', 'DLOAD', 'DSU', '(ENTER WITH D/N=0 IN PDL+0)', kind='interp', line=553)
W('27,3255', 0o00045, '', '', 'TFFTEM', 'Q2  E: (-16) M: (-15)', kind='operand', line=554)
W('27,3256', 0o00017, '', '', 'TFFQ1', 'Q1  E: (-16) M: (-15)', kind='operand', line=555)
W('27,3257', 0o14013, '', 'STODL', 'TFFDELQ', 'Q2-Q1  E: (-16) M: (-15)', kind='interp', line=556)
# D/N FROM PDL+0
W('27,3260', 0o77626, '', 'STADR', kind='interp', line=558)
W('27,3261', 0o77732, '', 'STORE', 'TFFTEM', 'D/N  E: (11) M: (10)', kind='interp', line=559)
W('27,3262', 0o53605, '', 'DMP', 'SL*', kind='interp', line=560)
W('27,3263', 0o00027, '', '', 'TFF1/ALF', '1/ALFA  E: (-22-2NA) M: (-20-2NA)', kind='operand', line=561)
W('27,3264', 0o57576, '', '', '0,2', '1/ALFA Z  E: (-11-NA) M: (-10-NA)', kind='operand', line=562)
W('27,3265', 0o41206, '', 'PUSH', 'DMP', 'TO PDL+0', kind='interp', line=563)
W('27,3266', 0o00045, '', '', 'TFFTEM', '1/Z  E: (11) M: (10)', kind='operand', line=564)
W('27,3267', 0o41057, '', 'SL*', 'BOVB', kind='interp', line=565)
W('27,3270', 0o57576, '', '', '0,2', 'X2= -NA', kind='operand', line=566)
W('27,3271', 0o45712, '', '', 'SIGNMPAC', 'IN CASE X= 1.0, CONTINUE', kind='operand', line=567)
W('27,3272', 0o00043, '', 'STORE', 'TFFX', 'X=1/ALFA ZSQ', kind='interp', line=568)
W('27,3273', 0o41234, '', 'RTB', 'DMP', kind='interp', line=569)
W('27,3274', 0o57334, '', '', 'T(X)', 'POLY', kind='operand', line=570)
W('27,3275', 0o00043, '', '', 'TFFX', kind='operand', line=571)
W('27,3276', 0o45242, '', 'SR3', 'DSU', kind='interp', line=572)
W('27,3277', 0o17364, '', '', 'DP2(-3)', kind='operand', line=573)
W('27,3300', 0o41405, '', 'DMP', 'PUSH', '2(X T(X)-1) /Z ALFA   E:(-15-NA)', kind='interp', line=574)
# M:(-14-NA)
# 1/ALFA Z FROM PDL+0   E:(-11-NA)
# M:(-10-NA)
W('27,3301', 0o41345, '', 'DLOAD', 'DMP', 'GET SIGN FOR SDELF', kind='interp', line=578)
W('27,3302', 0o00045, '', '', 'TFFTEM', '1/Z  E: (11) M: (10)', kind='operand', line=579)
W('27,3303', 0o00015, '', '', 'RMAG1', 'E: (-29) M: (-27)', kind='operand', line=580)
W('27,3304', 0o43312, '', 'SL2', 'DAD', kind='interp', line=581)
W('27,3305', 0o00017, '', '', 'TFFQ1', 'Q1  E: (-16) M: (-15)', kind='operand', line=582)
W('27,3306', 0o14045, '', 'STODL', 'TFFTEM', '(Q1+R 1/Z) =SGN OF SDELF  E:(-16) M:(-15', kind='interp', line=583)
W('27,3307', 0o00035, '', '', 'TFFNP', 'LC P  E: (-38+2NR) M: (-36+2NR)', kind='operand', line=584)
W('27,3310', 0o53605, '', 'DMP', 'SL*', 'CALC FOR ARG FOR TFF/TRIG.', kind='interp', line=585)
# Page 1386
W('27,3311', 0o00027, '', '', 'TFF1/ALF', '1/ALFA  E:(-22-2NA) M:(-20-2NA)', kind='operand', line=587)
W('27,3312', 0o57575, '', '', '1,2', 'X2=-NA', kind='operand', line=588)
W('27,3313', 0o53765, '', 'SIGN', 'SL*', kind='interp', line=589)
W('27,3314', 0o00045, '', '', 'TFFTEM', 'AFFIX SIGN FOR SDELF', kind='operand', line=590)
W('27,3315', 0o57576, '', '', '0,2', kind='operand', line=591)
W('27,3316', 0o14045, '', 'STODL', 'TFFTEM', 'P/ALFA  E:(-59+2NR)   M:(-55+2NR)', kind='interp', line=592)
# (ARG FOR USE IN TFF/TRIG)
W('27,3317', 0o00027, '', '', 'TFF1/ALF', '1/ALFA E:(-22-2NA) M:(-20-2NA)', kind='operand', line=594)
W('27,3320', 0o41366, '', 'SQRT', 'DMP', kind='interp', line=595)
W('27,3321', 0o17356, '', '', 'PI/16', 'PI (-4)', kind='operand', line=596)
W('27,3322', 0o77615, '', 'DAD', kind='interp', line=597)
# 2(XT(X)-1)/Z ALFA FROM PDL    E:(-15-NA)
# M:(-14-NA)
W('27,3323', 0o45257, '', 'SL*', 'DSU', kind='interp', line=600)
W('27,3324', 0o57577, '', '', '0 -1,2', kind='operand', line=601)
W('27,3325', 0o00013, '', '', 'TFFDELQ', 'Q2-Q1  E: (-16) M: (-15)', kind='operand', line=602)
W('27,3326', 0o53605, '', 'DMP', 'SL*', kind='interp', line=603)
W('27,3327', 0o00027, '', '', 'TFF1/ALF', '1/ALFA  E:(-22-2NA) M:(-20-2NA)', kind='operand', line=604)
W('27,3330', 0o57601, '', '', '0 -3,2', kind='operand', line=605)
W('27,3331', 0o52057, '', 'SL*', 'GOTO', kind='interp', line=606)
W('27,3332', 0o57602, '', '', '0 -4,2', kind='operand', line=607)
W('27,3333', 0o57240, '', '', 'ENDTFF', 'TFF SQRT(MU) IN MPAC E:(-45) M:(-42)', kind='operand', line=608)

# Page 1387
# PROGRAM NAME:         T(X)                            DATE:   01.17.67
# MOD NO:       0                                       LOG SECTION:    TIME OF FREE FALL
# MOD BY:       RR BAIRNSFATHER
# FUNCTIONAL DESCRIPTION:       THE POLYNOMIAL T(X) IS USED BY TIME OF FLIGHT SUBROUTINES CALCTFF AND
# CALCTPER TO APPROXIMATE THE SERIES
# 2     3
# 1/3 -X/5 +X /7 -X /9 ...

# WHERE   X = ALFA Z Z            IF ALFA Z Z LEQ 1
# X = 1/(ALFA Z Z )       IF ALFA Z Z  G  1

# ALSO    X IS NEG FOR HYPERBOLIC ORBITS
# X = 0 FOR PARABOLIC ORBITS
# X IS POSITIVE FOR ELLIPTIC ORBITS
# FOR FLIGHT 278, THE POLYNOMIAL T(X) IS FITTED OVER THE RANGE (0,+1) AND HAS A MAXIMUM
# DEVIATION FROM THE SERIES OF 2 E-5      (T(X) IS A CHEBYCHEV TYPE FIT AND WAS OBTAINED USING
# MAC PROGRAM AUTCURFIT294RRB AND IS VALID TO THE SAME TOLERANCE OVER THE RANGE (-.08,+1). )
# CALLING SEQUENCE:     RTB
# T(X)
# C(MPAC) = X

# SUBROUTINE CALLED:    NONE
# NORMAL EXIT MODE:     TC DANZIG
# ALARMS:       NONE
# OUTPUT:       C(MPAC) = T(X)
# ERASABLE INITIALIZATION REQUIRED:
# C(MPAC) = X
# DEBRIS:       NONE

W('27,3334', 0o07171, 'T(X)', 'TC', 'POLY', line=640)
W('27,3335', 0o00004, '', 'DEC', '4', 'N-1', kind='data', line=641)
W('27,3336', 0o12525, '', '2DEC', '3.333333333 E-1', kind='data', line=642)
W('27,3337', 0o12525, kind='data', line=642)
W('27,3340', 0o71463, '', '2DEC*', '-1.999819135 E-1*', kind='data', line=643)
W('27,3341', 0o57703, kind='data', line=643)
W('27,3342', 0o04423, '', '2DEC*', '1.418148467 E-1*', kind='data', line=644)
W('27,3343', 0o17645, kind='data', line=644)
W('27,3344', 0o74604, '', '2DEC*', '-1.01310997 E-1*', kind='data', line=645)
W('27,3345', 0o43667, kind='data', line=645)
W('27,3346', 0o01626, '', '2DEC*', '5.609004986 E-2*', kind='data', line=646)
W('27,3347', 0o37256, kind='data', line=646)
W('27,3350', 0o77404, '', '2DEC*', '-1.536156925 E-2*', kind='data', line=647)
W('27,3351', 0o52071, kind='data', line=647)

W('27,3352', 0o06030, 'ENDT(X)', 'TC', 'DANZIG', line=649)

S('TCDANZIG', 'equals', 0o67352, line=651)

# Page 1388
# TFF CONSTANTS
#   BANK 32

#   SETLOC TOF-FF1
#   BANK

# # NOTE _  NOTE _ ADJUSTED MUE FOR NEAR EARTH TRAJ.

# MUE            =       3.990 815 471 E10 # M CUBE/CS SQ
# RTMUE          =       1.997702549 E5 B-18*    # MODIFIED EARTH MU

W('27,3353', 0o24775, '1/RTMU', '2DEC*', '.5005750271 E-5 B17*', 'MODIFIED EARTH MU', kind='data', line=665)
W('27,3354', 0o30424, kind='data', line=665)

# # NOTE _  NOTE _ ADJUSTED MUE FOR NEAR EARTH TRAJ.

# MUM            =       4.902 778 E8            # M CUBE /CS SQ

# RTMUM          2DEC*   2.21422176 E4 B-18*
W('27,3355', 0o06220, 'PI/16', '2DEC', '3.141592653 B-4', kind='data', line=672)
W('27,3356', 0o37553, kind='data', line=672)
W('27,3357', 0o37777, 'LIM(-22)', '2OCT', '3777737700', '1.0 -B(-22)', kind='data', line=673)
W('27,3360', 0o37700, kind='data', line=673)
W('27,3361', 0o00000, 'DP(-22)', '2OCT', '0000000100', 'B(-22)', kind='data', line=674)
W('27,3362', 0o00100, kind='data', line=674)
W('27,3363', 0o04000, 'DP2(-3)', '2DEC', '1 B-3', kind='data', line=675)
W('27,3364', 0o00000, kind='data', line=675)
W('27,3365', 0o02000, 'DP2(-4)', '2DEC', '1 B-4', '1/16', kind='data', line=676)
W('27,3366', 0o00000, kind='data', line=676)

# RPAD1         2DEC    6373338 B-29            # M (-29) =20 909 901.57 FT
S('RPAD1', 'equals', 0o55151, line=679)
W('27,3367', 0o00305, 'R300K', '2DEC', '6464778 B-29', '(-29) M', kind='data', line=680)
W('27,3370', 0o11205, kind='data', line=680)
W('27,3371', 0o37777, 'NEARONE', '2DEC', '.999999999', kind='data', line=681)
W('27,3372', 0o37777, kind='data', line=681)
S('TFFZEROS', 'equals', 0o65334, line=682)
S('TFF1/4', 'equals', 0o65324, line=683)
