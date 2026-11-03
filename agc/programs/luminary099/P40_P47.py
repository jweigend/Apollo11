"""P40-P47.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P40-P47.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 752-784 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P40_P47', 'P40-P47.agc', 'Luminary099', pages='752-784')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P40-P47.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        752-784
# Mod history:  2009-05-19 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2011-01-06 JL   Fixed interpretive indentation.
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

# Page 752
# PROGRAM DESCRIPTION: P40BOTH          DECEMBER 22, 1966
# MOD 03 BY PETER ADLER                 MARCH 3, 1967
# CALLED VIA JOB FROM V37E
#
# FUNCTIONAL DESCRIPTION
#
# 1)      TO COMPUTE A PREFERRED IMU ORIENTATION AND A PREFERRED VEHICLE ATTITUDE FOR A LM DPS
# THRUSTING MANEUVER.
# (There is no item #2 in the original program listing --- RSB 2009.)
# 3)      TO DO THE VEHICLE MANEUVER TO THE THRUSTING ATTITUDE.
# 4)      TO CONTROL THE PGNCS DURING COUNTDOWN, IGNITION, THRUSTING, AND THRUST TERMINATION OF A
# PGNCS CONTROLLED DPS MANEUVER.
# 5)      IN POSTBURN --- ZERO RENDEZVOUS COUNTER, MAINTAIN VG CALCULATIONS FOR POSSIBLE RCS MANEUVER,
# SET MAXIMUM DEADBAND IN DAP, RESET STEERLAW CSTEER TO ZERO.
#
# NOTE:   P42, WHICH IS IN THIS LOG SECTION, DOES THE SAME FOR AN APS BURN, AND P41 DOES 1-3 FOR
# RCS PLUS DISPLAYS PARAMETERS FOR MANUAL CONTROL.
#
# SUBROUTINES USED
#
# R02             IMU STATUS CHECK
# S40.1           COMPUTATION OF THRUST DIRECTION
# S40.13          LENGTH OF BURN
# S40.2,3         PREFERRED IMU ORIENTATION
# S40.8           X PRODUCT STEERING
# S40.9           LAMBERT VTOGAIN
# R60LEM          ATTITUDE MANEUVER
# LEMPREC         EXTRAPOLATE STATE VECTOR
# PREREAD         AVERAGE G, SERVICER
# ALLCOAST        DAP COASTING INITIALIZATION
# CLOKTASK        ERGO CLOCKJOB -- COUNT DOWN
# PHASCHANG, INTPRET, FLAGUP, FLAGDOWN, WAITLIST, LONGCALL, GOFLASH, GOFLASHR, GOPERF1, ALARM,
# PRIOLARM, GOTOPOOH, ENDOFJOB, BANKCALL, SETMAXDB, SETMINDB, CHECKMM, FLATOUT, OUTFLAT,
# KILLTASK, SGNAGREE, TPAGREE, ETC.
#
# RESTARTS VIA GROUP 4
#
# DISPLAYS
#
# V50N25  203 A/P TO PGNCS, AUTO-THROTTLE MODE, AUTO ATTITUDE CONTROL
# V06N40  TTI, VG, DELTAVM (DISPLAYED ONCE/SECOND BY CLOKTASK)
# V50N99  PLEASE PERFORM ENGINE ON ENABLE
# V06N40  TG (TIME TO GO TO CUTOFF), VG, DELTAVM -- ONCE/SECOND
# V16N40  FINAL VALUES OF TG, VG, DELTAVM
# V16N85  COMP OF VG (BODY AXES) FOR POSS. RCS MANUAL MANEUVER
# V05N09  POSSIBLE ALARMS
# V50N07  PLEASE SELECT P00
#
# Page 753
# VIA R30
#
# V06N44  HAPO, PERI, TFF
# V06N35  TIME TO PERIGEE, HMS
#
# ALARM OR ABORT EXIT MODES
#
# PROGRAM ALARM, FLASHING DISPLAY OF ALARM CODE 1706 IF P40 SELECTED WITH DESCENT UNIT STAGED.
# V34E (TERMINATE) IS THE ONLY RESPONSE ACCEPTED.  TC GOTOPOOH.
#
# PROGRAM ALARM, FLASH CODE 1703:  TIG LESS THAN 45 SECS AWAY.  V34E= GOTOPOOH OR V33E= SLIP
# TIG BY 45 SECS.
#
# ERASABLE INITIALIZATION
#
# DEBRIS
#
# OUTPUT
#
# SEE SUBROUTINES E.G.:  S40.1, S40.2,3, S40.13, S40.8, S40.9, TRIMGIMB
# XDELVFLG = 1 FOR EXT DELV COMPUTATION
# = 0 FOR AIMPT (LAMBERT COMP

#   COUNT* $$/P40
#   EBANK= WHICH

#   BANK 36
#   SETLOC P40S
#   BANK

W('36,3147', 0o05353, 'P40LM', 'TC', 'PHASCHNG', line=110)
W('36,3150', 0o04024, '', 'OCT', '04024', kind='data', line=111)

W('36,3151', 0o33133, '', 'CAF', 'P40ADRES', 'INITIALIZATION FOR BURNBABY', line=113)
W('36,3152', 0o55455, '', 'TS', 'WHICH', line=114)

W('36,3153', 0o30106, '', 'CA', 'FLGWRD10', line=116)
W('36,3154', 0o74737, '', 'MASK', 'APSFLBIT', line=117)
W('36,3155', 0o10000, '', 'CCS', 'A', line=118)
W('36,3156', 0o13121, '', 'TCF', 'P40ALM', line=119)
W('36,3157', 0o04616, '', 'TC', 'BANKCALL', 'GO DO IMU STATUS CHECK ROUTINE.', line=120)
W('36,3160', 0o11254, '', 'CADR', 'R02BOTH', kind='data', line=121)

W('36,3161', 0o40111, '', 'CS', 'DAPBOOLS', 'INITIALIZE DVMON', line=123)
W('36,3162', 0o74737, '', 'MASK', 'CSMDOCKD', line=124)
W('36,3163', 0o10000, '', 'CCS', 'A', line=125)
W('36,3164', 0o32020, '', 'CAF', 'THRESH1', line=126)
W('36,3165', 0o62021, '', 'AD', 'THRESH3', line=127)
W('36,3166', 0o55251, '', 'TS', 'DVTHRUSH', line=128)
W('36,3167', 0o34751, '', 'CAF', 'FOUR', line=129)
W('36,3170', 0o55515, '', 'TS', 'DVCNTR', line=130)
# Page 754
W('36,3171', 0o06037, '', 'TC', 'INTPRET', 'LOAD CONSTANTS FOR DPS BURN', line=132)
W('36,3172', 0o43175, '', 'VLOAD', 'CLEAR', 'LOAD F, MDOT, TDECAY', kind='interp', line=133)
W('36,3173', 0o34001, '', '', 'FDPS', kind='operand', line=134)
W('36,3174', 0o02663, '', '', 'NOTHROTL', kind='operand', line=135)
W('36,3175', 0o03735, '', 'STORE', 'F', kind='interp', line=136)
W('36,3176', 0o77735, '', 'SLOAD', kind='interp', line=137)
W('36,3177', 0o26002, '', '', 'DPSVEX', kind='operand', line=138)
W('36,3200', 0o70476, 'P40IN', 'DCOMP', 'SR1', kind='interp', line=139)
W('36,3201', 0o37743, '', 'STCALL', 'VEX', 'LOAD EXHAUST VELOCITY FOR TGO COMP.', kind='interp', line=140)
W('36,3202', 0o56246, '', '', 'S40.1', 'COMPUTES UT AND VGTIG', kind='operand', line=141)
W('36,3203', 0o77624, '', 'CALL', kind='interp', line=142)
W('36,3204', 0o56413, '', '', 'S40.2,3', 'COMPUTES PREFERRED IMU ORIENTATION', kind='operand', line=143)
W('36,3205', 0o77776, '', 'EXIT', kind='interp', line=144)

W('36,3206', 0o00004, '', 'INHINT', line=146)
W('36,3207', 0o04674, '', 'TC', 'IBNKCALL', line=147)
W('36,3210', 0o40142, '', 'CADR', 'PFLITEDB', 'ZERO ATTITUDE ERRORS, SET DB TO ONE DEG.', kind='data', line=148)

W('36,3211', 0o03213, '', 'TC', 'P40SXT4', line=150)

# ********************************

W('36,3212', 0o12126, '', 'TCF', 'BURNBABY', line=154)

# ********************************

W('36,3213', 0o00006, 'P40SXT4', 'EXTEND', line=158)
W('36,3214', 0o23142, '', 'QXCH', 'P40/RET', line=159)
W('36,3215', 0o00003, 'P41MANU', 'RELINT', line=160)

W('36,3216', 0o05516, '', 'TC', 'DOWNFLAG', 'CLEAR 3AXISFLG -- R60 USE VECPOINT.', line=162)
W('36,3217', 0o00124, '', 'ADRES', '3AXISFLG', kind='data', line=163)

W('36,3220', 0o04616, '', 'TC', 'BANKCALL', line=165)
W('36,3221', 0o54123, '', 'CADR', 'R60LEM', 'DO ATTITUDE MANEUVER ROUTINE', kind='data', line=166)
W('36,3222', 0o01142, '', 'TC', 'P40/RET', line=167)

#   EBANK= TRKMKCNT
W('36,3223', 0o30005, 'POSTBURN', 'CA', 'Z', line=170)
W('36,3224', 0o55163, '', 'TS', 'DISPDEX', line=171)
W('36,3225', 0o00006, '', 'EXTEND', line=172)
W('36,3226', 0o32056, '', 'DCA', 'ACADN85', line=173)
W('36,3227', 0o53253, '', 'DXCH', 'AVEGEXIT', line=174)
W('36,3230', 0o33760, '', 'CAF', 'V16N40', line=175)
W('36,3231', 0o04616, '', 'TC', 'BANKCALL', line=176)
W('36,3232', 0o20635, '', 'CADR', 'GOFLASHR', kind='data', line=177)
W('36,3233', 0o03256, '', 'TC', 'TERM40', line=178)
W('36,3234', 0o13241, '', 'TCF', 'TIGNOW', line=179)
W('36,3235', 0o03223, '', 'TC', 'POSTBURN', line=180)
# Page 755
W('36,3236', 0o05353, 'P40PHS1', 'TC', 'PHASCHNG', line=182)
W('36,3237', 0o00014, '', 'OCT', '00014', kind='data', line=183)
W('36,3240', 0o15155, '', 'TCF', 'ENDOFJOB', line=184)

W('36,3241', 0o00004, 'TIGNOW', 'INHINT', line=186)
W('36,3242', 0o04674, '', 'TC', 'IBNKCALL', line=187)
W('36,3243', 0o40153, '', 'CADR', 'ZATTEROR', kind='data', line=188)
W('36,3244', 0o04674, '', 'TC', 'IBNKCALL', line=189)
W('36,3245', 0o40140, '', 'CADR', 'SETMINDB', kind='data', line=190)
W('36,3246', 0o00003, '', 'RELINT', line=191)
W('36,3247', 0o33761, '', 'CAF', 'V16N85B', line=192)
W('36,3250', 0o04616, '', 'TC', 'BANKCALL', line=193)
W('36,3251', 0o20462, '', 'CADR', 'REFLASHR', kind='data', line=194)
W('36,3252', 0o03256, '', 'TC', 'TERM40', line=195)
W('36,3253', 0o13256, '', 'TCF', 'TERM40', line=196)
W('36,3254', 0o03247, '', 'TC', '-5', line=197)

W('36,3255', 0o13236, '', 'TCF', 'P40PHS1', line=199)

W('36,3256', 0o00006, 'TERM40', 'EXTEND', line=201)
W('36,3257', 0o32106, '', 'DCA', 'SERVCADR', line=202)
W('36,3260', 0o53253, '', 'DXCH', 'AVEGEXIT', line=203)
W('36,3261', 0o34755, '', 'CAF', 'ZERO', line=204)
W('36,3262', 0o55462, '', 'TS', 'TRKMKCNT', 'ZERO RENDZVS CNTERS', line=205)
W('36,3263', 0o30005, '', 'CA', 'Z', line=206)
W('36,3264', 0o55163, '', 'TS', 'DISPDEX', line=207)
W('36,3265', 0o00004, '', 'INHINT', line=208)
W('36,3266', 0o04674, '', 'TC', 'IBNKCALL', line=209)
W('36,3267', 0o40123, '', 'CADR', 'RESTORDB', kind='data', line=210)
W('36,3270', 0o00003, '', 'RELINT', line=211)
W('36,3271', 0o06001, '', 'TC', 'GOTOPOOH', line=212)

#   EBANK= WHICH
#   COUNT* $$/P41
W('36,3272', 0o33134, 'P41LM', 'CAF', 'P41ADRES', 'INITIALIZATION FOR BURNBABY', line=216)
W('36,3273', 0o55455, '', 'TS', 'WHICH', line=217)

W('36,3274', 0o04616, '', 'TC', 'BANKCALL', line=219)
W('36,3275', 0o11254, '', 'CADR', 'R02BOTH', kind='data', line=220)

W('36,3276', 0o06037, '', 'TC', 'INTPRET', 'BOTH LM', line=222)
W('36,3277', 0o71214, '', 'BON', 'DLOAD', 'IF NJETSFLAG IS SET, LOAD Z JET F', kind='interp', line=223)
W('36,3300', 0o00700, '', '', 'NJETSFLG', kind='operand', line=224)
W('36,3301', 0o75305, '', '', 'P41FJET1', kind='operand', line=225)
W('36,3302', 0o34015, '', '', 'FRCS4', 'IF NJETSFLG IS CLEAR, LOAD 4 JET F', kind='operand', line=226)

W('36,3303', 0o37735, 'P41FJET', 'STCALL', 'F', kind='interp', line=228)
W('36,3304', 0o75310, '', '', 'P41IN', kind='operand', line=229)
W('36,3305', 0o77745, 'P41FJET1', 'DLOAD', kind='interp', line=230)
# Page 756
W('36,3306', 0o34017, '', '', 'FRCS2', kind='operand', line=232)
W('36,3307', 0o03735, '', 'STORE', 'F', kind='interp', line=233)

W('36,3310', 0o77624, 'P41IN', 'CALL', kind='interp', line=235)
W('36,3311', 0o56246, '', '', 'S40.1', 'BOTH', kind='operand', line=236)
W('36,3312', 0o77624, 'P41NORM', 'CALL', kind='interp', line=237)
W('36,3313', 0o56413, '', '', 'S40.2,3', 'CALCULATE PREFERRED IMU ORIENTATION AND', kind='operand', line=238)
W('36,3314', 0o77776, '', 'EXIT', '', 'SET PFRATFLG.', kind='interp', line=239)

W('36,3315', 0o00004, '', 'INHINT', line=241)
W('36,3316', 0o04674, '', 'TC', 'IBNKCALL', line=242)
W('36,3317', 0o40153, '', 'CADR', 'ZATTEROR', 'ZERO ATTITUDE ERRORS', kind='data', line=243)
W('36,3320', 0o04674, '', 'TC', 'IBNKCALL', line=244)
W('36,3321', 0o40140, '', 'CADR', 'SETMINDB', 'SET 0.3 DEGREE DEADBAND', kind='data', line=245)
W('36,3322', 0o03213, '', 'TC', 'P40SXT4', line=246)

W('36,3323', 0o06037, '', 'TC', 'INTPRET', line=248)
W('36,3324', 0o45175, '', 'VLOAD', 'CALL', 'TRANSFORM VELOCITY-TO-BE-GAINED AT TIG', kind='interp', line=249)
W('36,3325', 0o03701, '', '', 'VGTIG', 'FROM REFERENCE COORDINATES TO LM BODY-', kind='operand', line=250)
W('36,3326', 0o57267, '', '', 'S41.1', 'AXIS COORDINATES FOR V16N85 DISPLAY.', kind='operand', line=251)
W('36,3327', 0o03502, '', 'STORE', 'VGBODY', '(SCALED AT 2 (+7) METERS/CENTISECOND)', kind='interp', line=252)
W('36,3330', 0o77776, '', 'EXIT', kind='interp', line=253)

W('36,3331', 0o33761, '', 'CAF', 'V16N85B', line=255)
W('36,3332', 0o04616, '', 'TC', 'BANKCALL', line=256)
W('36,3333', 0o20446, '', 'CADR', 'GODSPRET', kind='data', line=257)

W('36,3334', 0o35017, '', 'CAF', 'PRIO5', line=259)
W('36,3335', 0o55163, '', 'TS', 'DISPDEX', 'FOR SAFETY ONLY', line=260)
W('36,3336', 0o05105, '', 'TC', 'FINDVAC', line=261)
#   EBANK= VGPREV
W('36,3337', 0o03361, '', '2CADR', 'DYNMDISP', kind='data', line=263)
W('36,3340', 0o74067, kind='data', line=263)

W('36,3341', 0o05327, '', 'TC', '2PHSCHNG', line=265)
W('36,3342', 0o00076, '', 'OCT', '00076', 'GROUP 6 RESTARTS AT REDO6.7', kind='data', line=266)
W('36,3343', 0o04024, '', 'OCT', '04024', 'GROUP 4 RESTARTS HERE', kind='data', line=267)

# ********************************

W('36,3344', 0o12135, '', 'TCF', 'B*RNB*B*', line=271)

# ********************************

W('36,3345', 0o34777, 'BLNKWAIT', 'CAF', '1SEC', line=275)
W('36,3346', 0o04616, '', 'TC', 'BANKCALL', line=276)
W('36,3347', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=277)

W('36,3350', 0o31163, 'REDO6.7', 'CA', 'DISPDEX', 'ON A RESTART, DO NOT PUT UP DISPLAY IF', line=279)
W('36,3351', 0o64752, '', 'AD', 'TWO', 'BLANKING (BETWEEN TIG-35 AND TIG-30)', line=280)

# ********************************
# Page 757

W('36,3352', 0o00006, '', 'EXTEND', line=285)
W('36,3353', 0o13345, '', 'BZF', 'BLNKWAIT', line=286)

W('36,3354', 0o33761, '', 'CAF', 'V16N85B', line=288)
W('36,3355', 0o04616, '', 'TC', 'BANKCALL', line=289)
W('36,3356', 0o20446, '', 'CADR', 'GODSPRET', kind='data', line=290)

W('36,3357', 0o35017, '', 'CAF', 'PRIO5', line=292)
W('36,3360', 0o05146, '', 'TC', 'PRIOCHNG', line=293)

W('36,3361', 0o31163, 'DYNMDISP', 'CA', 'DISPDEX', 'A NON-POSITIVE DISPDEX INDICATES PAST', line=295)
W('36,3362', 0o00006, '', 'EXTEND', '', 'TIG-35, SO SERVICER WILL BE DOING THE', line=296)
W('36,3363', 0o65155, '', 'BZMF', 'ENDOFJOB', 'UPDATING OF NOUN 85.  STOP DYNMDISP.', line=297)
W('36,3364', 0o06037, '', 'TC', 'INTPRET', line=298)
W('36,3365', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=299)
W('36,3366', 0o03701, '', '', 'VGPREV', kind='operand', line=300)
W('36,3367', 0o57267, '', '', 'S41.1', kind='operand', line=301)
W('36,3370', 0o03502, '', 'STORE', 'VGBODY', kind='interp', line=302)
W('36,3371', 0o77776, '', 'EXIT', kind='interp', line=303)
W('36,3372', 0o34777, '', 'CAF', '1SEC', line=304)
W('36,3373', 0o04616, '', 'TC', 'BANKCALL', line=305)
W('36,3374', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=306)
W('36,3375', 0o13361, '', 'TCF', 'DYNMDISP', line=307)

W('36,3376', 0o06037, 'CALCN85', 'TC', 'INTPRET', line=309)
W('36,3377', 0o77624, '', 'CALL', kind='interp', line=310)
W('36,3400', 0o75611, '', '', 'UPDATEVG', kind='operand', line=311)
W('36,3401', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=312)
W('36,3402', 0o03701, '', '', 'VGPREV', kind='operand', line=313)
W('36,3403', 0o57267, '', '', 'S41.1', kind='operand', line=314)
W('36,3404', 0o03502, '', 'STORE', 'VGBODY', kind='interp', line=315)
W('36,3405', 0o77776, '', 'EXIT', kind='interp', line=316)
W('36,3406', 0o04635, '', 'TC', 'POSTJUMP', line=317)
W('36,3407', 0o65770, '', 'CADR', 'SERVEXIT', kind='data', line=318)

#   COUNT* $$/P42
#   EBANK= WHICH

W('36,3410', 0o05353, 'P42LM', 'TC', 'PHASCHNG', line=323)
W('36,3411', 0o04024, '', 'OCT', '04024', kind='data', line=324)

W('36,3412', 0o33135, '', 'CAF', 'P42ADRES', 'INITIALIZATION FOR BURNBABY.', line=326)
W('36,3413', 0o55455, '', 'TS', 'WHICH', line=327)

W('36,3414', 0o40106, '', 'CS', 'FLGWRD10', line=329)
W('36,3415', 0o74737, '', 'MASK', 'APSFLBIT', line=330)
W('36,3416', 0o10000, '', 'CCS', 'A', line=331)
W('36,3417', 0o03121, '', 'TC', 'P40ALM', line=332)
W('36,3420', 0o04616, 'P42STAGE', 'TC', 'BANKCALL', line=333)
# Page 758
W('36,3421', 0o11254, '', 'CADR', 'R02BOTH', kind='data', line=335)
W('36,3422', 0o36000, '', 'CAF', 'THRESH2', 'INITIALIZE DVMON', line=336)
W('36,3423', 0o55251, '', 'TS', 'DVTHRUSH', line=337)
W('36,3424', 0o34751, '', 'CAF', 'FOUR', line=338)
W('36,3425', 0o55515, '', 'TS', 'DVCNTR', line=339)

W('36,3426', 0o06037, '', 'TC', 'INTPRET', line=341)
W('36,3427', 0o77214, '', 'SET', 'VLOAD', 'LOAD FAPS, MDOTAPS, AND ATDECAY INTO', kind='interp', line=342)
W('36,3430', 0o01072, '', '', 'AVFLAG', 'F, MDOT, AND TDECAY BY VECTOR LOAD.', kind='operand', line=343)
W('36,3431', 0o34007, '', '', 'FAPS', kind='operand', line=344)
W('36,3432', 0o03735, '', 'STORE', 'F', kind='interp', line=345)
W('36,3433', 0o52135, '', 'SLOAD', 'GOTO', kind='interp', line=346)
W('36,3434', 0o26001, '', '', 'APSVEX', kind='operand', line=347)
W('36,3435', 0o75200, '', '', 'P40IN', kind='operand', line=348)

#   EBANK= WHICH

#   COUNT* $$/P47
W('36,3436', 0o04616, 'P47LM', 'TC', 'BANKCALL', line=353)
W('36,3437', 0o11254, '', 'CADR', 'R02BOTH', kind='data', line=354)
W('36,3440', 0o06037, '', 'TC', 'INTPRET', line=355)
W('36,3441', 0o77624, '', 'CALRB', kind='interp', line=356)
W('36,3442', 0o27553, '', '', 'MIDTOAV2', kind='operand', line=357)

W('36,3443', 0o30155, '', 'CA', 'MPAC +1', line=359)
W('36,3444', 0o05173, '', 'TC', 'TWIDDLE', line=360)
W('36,3445', 0o03447, '', 'ADRES', 'STARTP47', kind='data', line=361)

W('36,3446', 0o15155, '', 'TCF', 'ENDOFJOB', line=363)

W('36,3447', 0o05353, 'STARTP47', 'TC', 'PHASCHNG', line=365)
W('36,3450', 0o05014, '', 'OCT', '05014', kind='data', line=366)
W('36,3451', 0o77777, '', 'OCT', '77777', kind='data', line=367)

W('36,3452', 0o00006, '', 'EXTEND', line=369)
W('36,3453', 0o33764, '', 'DCA', 'ACADN83', line=370)
W('36,3454', 0o53253, '', 'DXCH', 'AVEGEXIT', line=371)
W('36,3455', 0o34736, '', 'CAF', 'PRIO20', line=372)
W('36,3456', 0o05105, '', 'TC', 'FINDVAC', line=373)
#   EBANK= DELVIMU
W('36,3457', 0o03513, '', '2CADR', 'P47BODY', kind='data', line=375)
W('36,3460', 0o74067, kind='data', line=375)

W('36,3461', 0o12342, '', 'TCF', 'REDO4.2', 'CHECKS PHASE 5 AND GOES TO PREREAD', line=377)
# SEE TIG-30 IN BURNBABY

W('36,3462', 0o06037, 'CALCN83', 'TC', 'INTPRET', line=380)
W('36,3463', 0o53375, '', 'VLOAD', 'VAD', kind='interp', line=381)
W('36,3464', 0o03502, '', '', 'DELVCTL', kind='operand', line=382)
W('36,3465', 0o03527, '', '', 'DELVREF', kind='operand', line=383)
W('36,3466', 0o03656, '', 'STORE', 'DELVSIN', 'TEMP STORAGE FOR RESTARTS', kind='interp', line=384)
# Page 759
W('36,3467', 0o77624, '', 'CALL', kind='interp', line=386)
W('36,3470', 0o57267, '', '', 'S41.1', kind='operand', line=387)
W('36,3471', 0o03623, '', 'STORE', 'DELVIMU', kind='interp', line=388)
W('36,3472', 0o77776, '', 'EXIT', kind='interp', line=389)
W('36,3473', 0o05353, '', 'TC', 'PHASCHNG', line=390)
W('36,3474', 0o10035, '', 'OCT', '10035', 'REREADAC AND HERE', kind='data', line=391)

W('36,3475', 0o06037, '', 'TC', 'INTPRET', line=393)
W('36,3476', 0o77775, '', 'VLOAD', kind='interp', line=394)
W('36,3477', 0o03656, '', '', 'DELVSIN', kind='operand', line=395)
W('36,3500', 0o03502, '', 'STORE', 'DELVCTL', kind='interp', line=396)
W('36,3501', 0o77776, '', 'EXIT', kind='interp', line=397)

W('36,3502', 0o04635, '', 'TC', 'POSTJUMP', line=399)
W('36,3503', 0o65770, '', 'CADR', 'SERVEXIT', kind='data', line=400)

W('36,3504', 0o33762, 'P47BOD', 'CAF', 'V1683', line=402)
W('36,3505', 0o04616, '', 'TC', 'BANKCALL', line=403)
W('36,3506', 0o20635, '', 'CADR', 'GOFLASHR', kind='data', line=404)
W('36,3507', 0o06001, '', 'TC', 'GOTOPOOH', line=405)
W('36,3510', 0o06001, '', 'TC', 'GOTOPOOH', line=406)

W('36,3511', 0o13513, '', 'TCF', 'P47BODY', line=408)

W('36,3512', 0o13236, '', 'TCF', 'P40PHS1', line=410)

W('36,3513', 0o06037, 'P47BODY', 'TC', 'INTPRET', line=412)
W('36,3514', 0o77775, '', 'VLOAD', kind='interp', line=413)
W('36,3515', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=414)
W('36,3516', 0o03623, '', 'STORE', 'DELVIMU', kind='interp', line=415)
W('36,3517', 0o03502, '', 'STORE', 'DELVCTL', kind='interp', line=416)
W('36,3520', 0o77776, '', 'EXIT', kind='interp', line=417)
W('36,3521', 0o03504, '', 'TC', 'P47BOD', line=418)

#   COUNT* $$/P40
W('36,3522', 0o31517, 'IMPLBURN', 'CA', 'TGO +1', line=421)
W('36,3523', 0o03735, '', 'TC', 'GETDT', line=422)
W('36,3524', 0o05173, '', 'TC', 'TWIDDLE', line=423)
W('36,3525', 0o03542, '', 'ADRES', 'ENGOFTSK', kind='data', line=424)
W('36,3526', 0o05516, '', 'TC', 'DOWNFLAG', 'TURN OFF IGNFLAG', line=425)
W('36,3527', 0o00153, '', 'ADRES', 'IGNFLAG', kind='data', line=426)
W('36,3530', 0o05516, '', 'TC', 'DOWNFLAG', 'TURN OFF ASTNFLG', line=427)
W('36,3531', 0o00154, '', 'ADRES', 'ASTNFLAG', kind='data', line=428)
W('36,3532', 0o05516, '', 'TC', 'DOWNFLAG', 'TURN OFF IMPULSW', line=429)
W('36,3533', 0o00044, '', 'ADRES', 'IMPULSW', kind='data', line=430)
W('36,3534', 0o05353, '', 'TC', 'PHASCHNG', 'RESTART PROTECT ENGOFTSK (ENGINOFF)', line=431)
W('36,3535', 0o40114, '', 'OCT', '40114', kind='data', line=432)

W('36,3536', 0o05221, '', 'TC', 'FIXDELAY', 'WAIT HALF A SECOND', line=434)
W('36,3537', 0o00062, '', 'DEC', '50', kind='data', line=435)
# Page 760
W('36,3540', 0o02653, '', 'TC', 'NOULLAGE', 'TURN OFF ULLAGE', line=437)

W('36,3541', 0o05261, '', 'TC', 'TASKOVER', line=439)

W('36,3542', 0o04674, 'ENGOFTSK', 'TC', 'IBNKCALL', 'THIS CODING ALLOWS ENGINOFF ET AL TO BE', line=441)
W('36,3543', 0o75545, '', 'CADR', 'ENGINOFF', 'USED BOTH BY WAITLIST AND BY TC IBNKCALL', kind='data', line=442)
W('36,3544', 0o05261, '', 'TC', 'TASKOVER', line=443)

W('36,3545', 0o34644, 'ENGINOFF', 'CAF', 'PRIO12', 'MUST BE LOWER PRIO THAN CLOCKJOB', line=445)
W('36,3546', 0o05105, '', 'TC', 'FINDVAC', line=446)
#   EBANK= TRKMKCNT
W('36,3547', 0o03223, '', '2CADR', 'POSTBURN', kind='data', line=448)
W('36,3550', 0o74067, kind='data', line=448)

W('36,3551', 0o34753, 'ENGINOF2', 'CAF', 'BIT1', line=450)
W('36,3552', 0o05203, '', 'TC', 'WAITLIST', line=451)
#   EBANK= OMEGAQ
W('36,3553', 0o03606, '', '2CADR', 'COASTSET', kind='data', line=453)
W('36,3554', 0o74066, kind='data', line=453)

W('36,3555', 0o40103, 'ENGINOF1', 'CS', 'FLAGWRD7', 'SET THE IDLE BIT.', line=455)
W('36,3556', 0o74745, '', 'MASK', 'IDLEFBIT', line=456)
W('36,3557', 0o26103, '', 'ADS', 'FLAGWRD7', line=457)

W('36,3560', 0o02653, '', 'TC', 'NOULLAGE', line=459)

W('36,3561', 0o00006, 'ENGINOF4', 'EXTEND', line=461)
W('36,3562', 0o30025, '', 'DCA', 'TIME2', line=462)
W('36,3563', 0o53345, '', 'DXCH', 'TEVENT', line=463)

W('36,3564', 0o44745, 'ENGINOF3', 'CS', 'ENGONBIT', 'INSURE ENGONFLG IS CLEAR.', line=465)
W('36,3565', 0o70101, '', 'MASK', 'FLAGWRD5', line=466)
W('36,3566', 0o54101, '', 'TS', 'FLAGWRD5', line=467)
W('36,3567', 0o44355, '', 'CS', 'PRIO30', 'ENGINOF3 IS USED AS A PRE-ENGINE ARM', line=468)
W('36,3570', 0o00006, '', 'EXTEND', '', 'SUBROUTINE.', line=469)
W('36,3571', 0o02011, '', 'RAND', 'DSALMOUT', line=470)
W('36,3572', 0o64736, '', 'AD', 'PRIO20', 'TURN OFF THE ENGINE -- DPS OR APS', line=471)
W('36,3573', 0o00006, '', 'EXTEND', line=472)
W('36,3574', 0o01011, '', 'WRITE', 'DSALMOUT', line=473)

W('36,3575', 0o40111, '', 'CS', 'DAPBOOLS', 'TURN OFF TRIM GIMBAL', line=475)
W('36,3576', 0o74736, '', 'MASK', 'USEQRJTS', line=476)
W('36,3577', 0o26111, '', 'ADS', 'DAPBOOLS', line=477)

W('36,3600', 0o44737, '', 'CS', 'HIRTHROT', 'ZERO AUTO-THROTTLE WHENEVER THE ENGINE', line=479)
W('36,3601', 0o54055, '', 'TS', 'THRUST', 'IS TURNED OFF.', line=480)
W('36,3602', 0o34750, '', 'CAF', 'BIT4', 'THE HARDWARE DOES SO ONLY WHEN THE', line=481)
W('36,3603', 0o00006, '', 'EXTEND', '', 'ENGINE IS DISARMED.', line=482)
W('36,3604', 0o05014, '', 'WOR', 'CHAN14', line=483)

W('36,3605', 0o04707, '', 'TC', 'ISWRETRN', line=485)
# Page 761
W('36,3606', 0o04674, 'COASTSET', 'TC', 'IBNKCALL', 'DO DAP COASTING INITIALIZATION', line=487)
W('36,3607', 0o40204, '', 'CADR', 'ALLCOAST', kind='data', line=488)
W('36,3610', 0o05261, '', 'TC', 'TASKOVER', line=489)

#   EBANK= OMEGAQ
W('36,3611', 0o45020, 'UPDATEVG', 'STQ', 'CALL', kind='interp', line=492)
W('36,3612', 0o03665, '', '', 'QTEMP1', kind='operand', line=493)
W('36,3613', 0o56447, '', '', 'S40.8', 'X-PRODUCT STEERING', kind='operand', line=494)
W('36,3614', 0o43014, '', 'BON', 'BON', kind='interp', line=495)
W('36,3615', 0o01307, '', '', 'XDELVFLG', kind='operand', line=496)
W('36,3616', 0o03665, '', '', 'QTEMP1', kind='operand', line=497)
W('36,3617', 0o03705, '', '', 'NORMSW', kind='operand', line=498)
W('36,3620', 0o75633, '', '', '180SETUP', kind='operand', line=499)
W('36,3621', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=500)
W('36,3622', 0o01235, '', '', 'PIPTIME', kind='operand', line=501)
W('36,3623', 0o03763, '', '', 'TIGSAVE', kind='operand', line=502)
W('36,3624', 0o50025, '', 'DSU', 'BMN', kind='interp', line=503)
W('36,3625', 0o03432, '', '', 'TNEWA', kind='operand', line=504)
W('36,3626', 0o75656, '', '', 'GETRANS', kind='operand', line=505)
W('36,3627', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=506)
W('36,3630', 0o03763, '', '', 'TIGSAVE', kind='operand', line=507)
W('36,3631', 0o03432, '', '', 'TNEWA', kind='operand', line=508)
W('36,3632', 0o03765, '', 'STORE', 'TIGSAVEP', kind='interp', line=509)
W('36,3633', 0o77776, '180SETUP', 'EXIT', kind='interp', line=510)
W('36,3634', 0o10755, '', 'CCS', 'PHASE2', line=511)
W('36,3635', 0o13663, '', 'TCF', 'NO.9', line=512)
W('36,3636', 0o34737, '', 'CAF', 'PRIO10', line=513)
W('36,3637', 0o00004, '', 'INHINT', line=514)
W('36,3640', 0o05105, '', 'TC', 'FINDVAC', line=515)
#   EBANK= VG
W('36,3641', 0o02707, '', '2CADR', 'S40.9', 'LAMBERT VTOGAIN', kind='data', line=517)
W('36,3642', 0o56067, kind='data', line=517)

W('36,3643', 0o05327, '', 'TC', '2PHSCHNG', line=519)
W('36,3644', 0o00172, '', 'OCT', '00172', '2.17SPOT FOR S40.9', kind='data', line=520)
W('36,3645', 0o10035, '', 'OCT', '10035', 'HERE AND REREADAC AFTER RESTART', kind='data', line=521)

W('36,3646', 0o06037, 'ENDSTEER', 'TC', 'INTPRET', line=523)
W('36,3647', 0o77745, '', 'DLOAD', kind='interp', line=524)
W('36,3650', 0o03765, '', '', 'TIGSAVEP', kind='operand', line=525)
W('36,3651', 0o27763, '', 'STOVL', 'TIGSAVE', kind='interp', line=526)
W('36,3652', 0o01221, '', '', 'RN', kind='operand', line=527)
W('36,3653', 0o26323, '', 'STOVL', 'RINIT', kind='interp', line=528)
W('36,3654', 0o01227, '', '', 'VN', kind='operand', line=529)
W('36,3655', 0o02331, '', 'STORE', 'VINIT', kind='interp', line=530)
W('36,3656', 0o45345, 'GETRANS', 'DLOAD', 'DSU', kind='interp', line=531)
W('36,3657', 0o03631, '', '', 'TPASS4', kind='operand', line=532)
W('36,3660', 0o01235, '', '', 'PIPTIME', kind='operand', line=533)
W('36,3661', 0o37452, '', 'STCALL', 'DELLT4', kind='interp', line=534)
W('36,3662', 0o03665, '', '', 'QTEMP1', kind='operand', line=535)

# Page 762
W('36,3663', 0o06037, 'NO.9', 'TC', 'INTPRET', line=538)
W('36,3664', 0o77650, '', 'GOTO', kind='interp', line=539)
W('36,3665', 0o03665, '', '', 'QTEMP1', kind='operand', line=540)
W('36,3666', 0o06037, 'STEERING', 'TC', 'INTPRET', line=541)

W('36,3667', 0o77624, '', 'CALL', kind='interp', line=543)
W('36,3670', 0o75611, '', '', 'UPDATEVG', kind='operand', line=544)
W('36,3671', 0o77776, '', 'EXIT', kind='interp', line=545)

#   EBANK= DVCNTR
W('36,3672', 0o00004, 'NSTEER', 'INHINT', line=548)
W('36,3673', 0o35016, '', 'CA', 'EBANK7', line=549)
W('36,3674', 0o54003, '', 'TS', 'EBANK', line=550)
W('36,3675', 0o40076, '', 'CS', 'FLAGWRD2', 'CHECK IMPULSE SWITCH.  IT IS SET EITHER', line=551)
W('36,3676', 0o74743, '', 'MASK', 'IMPULBIT', 'BY S40.13 IF TBURN<6 SECS OR BY S40.8 IF', line=552)
W('36,3677', 0o10000, '', 'CCS', 'A', 'STEERING IS ALMOST DONE.', line=553)

W('36,3700', 0o13705, '', 'TCF', '+5', 'IMPULSW = 0   EXIT', line=555)
W('36,3701', 0o40103, '', 'CS', 'FLAGWRD7', 'IMPULSW = 1   WHY?  CHECK IDLEFLAG', line=556)
W('36,3702', 0o74745, '', 'MASK', 'IDLEFBIT', '      (IDLEFLAG = 0 --> DVMON ON)', line=557)
W('36,3703', 0o10000, '', 'CCS', 'A', line=558)
W('36,3704', 0o13707, '', 'TCF', '+3', 'DVMON ON --> THRUSTING --> IMPULSW VIA S40.8', line=559)
W('36,3705', 0o04635, '', 'TC', 'POSTJUMP', 'DVMON OFF --> IMPULSW ON VIA S40.13 --> EXIT', line=560)
W('36,3706', 0o65770, '', 'CADR', 'SERVEXIT', kind='data', line=561)

W('36,3707', 0o04674, '', 'TC', 'IBNKCALL', line=563)
W('36,3710', 0o40165, '', 'CADR', 'STOPRATE', kind='data', line=564)

W('36,3711', 0o05516, '', 'TC', 'DOWNFLAG', 'TURN OFF IMPULSW', line=566)
W('36,3712', 0o00044, '', 'ADRES', 'IMPULSW', kind='data', line=567)

W('36,3713', 0o05504, '', 'TC', 'UPFLAG', line=569)
W('36,3714', 0o00161, '', 'ADRES', 'IDLEFLAG', 'TURN OFF DVMON', kind='data', line=570)

W('36,3715', 0o00004, '', 'INHINT', line=572)
W('36,3716', 0o00006, '', 'EXTEND', line=573)
W('36,3717', 0o31442, '', 'DCA', 'TIG', line=574)
W('36,3720', 0o52155, '', 'DXCH', 'MPAC', line=575)
W('36,3721', 0o00006, '', 'EXTEND', line=576)
W('36,3722', 0o40025, '', 'DCS', 'TIME2', line=577)
W('36,3723', 0o20155, '', 'DAS', 'MPAC', line=578)
W('36,3724', 0o07257, '', 'TC', 'TPAGREE', line=579)
W('36,3725', 0o30155, '', 'CAE', 'MPAC +1', line=580)
W('36,3726', 0o03735, '', 'TC', 'GETDT', line=581)
W('36,3727', 0o05173, '', 'TC', 'TWIDDLE', line=582)
W('36,3730', 0o03542, '', 'ADRES', 'ENGOFTSK', kind='data', line=583)
W('36,3731', 0o05327, '', 'TC', '2PHSCHNG', line=584)
W('36,3732', 0o40114, '', 'OCT', '40114', 'ENGOFTSK (ENGINOFF)', kind='data', line=585)
W('36,3733', 0o00035, '', 'OCT', '00035', 'SERVICER -- REREADAC', kind='data', line=586)
# Page 763
W('36,3734', 0o15155, '', 'TCF', 'ENDOFJOB', line=588)

W('36,3735', 0o10000, 'GETDT', 'CCS', 'A', line=590)
W('36,3736', 0o13741, '', 'TCF', '+3', line=591)
W('36,3737', 0o13741, '', 'TCF', '+2', line=592)
W('36,3740', 0o34755, '', 'CAF', 'ZERO', line=593)
W('36,3741', 0o64753, '', 'AD', 'ONE', line=594)
W('36,3742', 0o56001, '', 'XCH', 'L', line=595)
W('36,3743', 0o34755, '', 'CAF', 'ZERO', line=596)
W('36,3744', 0o53517, '', 'DXCH', 'TGO', line=597)
W('36,3745', 0o31517, '', 'CA', 'TGO +1', line=598)
W('36,3746', 0o00002, '', 'TC', 'Q', line=599)

# **************************************

W('36,3747', 0o00000, 'SEC15DP', 'OCT', '00000', "DON'T SEPARATE", kind='data', line=603)
W('36,3750', 0o02734, 'SEC15', 'DEC', '1500', "DON'T SEPARATE", kind='data', line=604)
W('36,3751', 0o00000, 'SEC30DP', '2DEC', '3000', kind='data', line=605)
W('36,3752', 0o05670, kind='data', line=605)

W('36,3753', 0o00000, 'SEC45DP', 'OCT', '00000', "DON'T MOVE FROM JUST BEFORE SEC45", kind='data', line=607)
W('36,3754', 0o10624, 'SEC45', 'DEC', '4500', kind='data', line=608)
W('36,3755', 0o00000, '5SECDP', 'OCT', '00000', "DON'T MOVE FROM JUST BEFORE 5SEC", kind='data', line=609)
W('36,3756', 0o00764, '5SEC', 'DEC', '500', kind='data', line=610)
W('36,3757', 0o05050, '26SECS', 'DEC', '2600', kind='data', line=611)
W('36,3760', 0o04050, 'V16N40', 'VN', '1640', kind='data', line=612)
W('36,3761', 0o04125, 'V16N85B', 'VN', '1685', kind='data', line=613)
W('36,3762', 0o04123, 'V1683', 'VN', '1683', kind='data', line=614)
S('SEC01', 'equals', 0o4777, line=615)
S('ACADN85', 'equals', 0o104055, line=616)

#   EBANK= DELVIMU
W('36,3763', 0o03462, 'ACADN83', '2CADR', 'CALCN83', kind='data', line=619)
W('36,3764', 0o74067, kind='data', line=619)

# ******************************************
# Page 764
# PROGRAM DESCRIPTION: S40.1            DATE: 15 NOV 66
# MOD N02                               LOG SECTION P40-P47
# MOD BY ZELDIN AND ADAPTED BY TALAYCO
#
# FUNCTIONAL DESCRIPTION
# COMPUTE INITIAL THRUST DIRECTION(UT) AND INITIAL VALUE OF VG
# VECTOR(VGTIG).
#
# CALLING SEQUENCE
# L       CALL
# L+1             S40.1
#
# NORMAL EXIT MODE
# AT L+2 OF CALLING SEQUENCE (GOTO L+2) NORMAL RETURN OR
# ERROR RETURN IF NOSOFLAG =1
#
# SUBROUTINES CALLED
# LEMPREC
# INITVEL
# CALCGRAV
# MIDGIM
#
# ALARM OR ABORT EXIT MODES
# L+2 OF CALLING SEQUENCE, UNSOLVABLE CONIC IF NOSOFLAG=1
#
# ERASABLE INITIALIZATION REQUIRED
# WEIGHT/G        ANTICIPATED VEHICLE MASS        DP B16 KGM
# XDELVFLG        1=DELTA-V MANEUVER, 0=AIMPT STEER
# F               THRUST FOR ENGINE USED
# IF DELTA-V MANEUVER:
# DELVSIN         SPECIFIED DELTA-V REQUIRED IN
# INERTIAL COORDS. OF ACTIVE VEHICLE
# AT TIME OF IGNITION             VECTOR B7 M/CS
# DELVSAB         MAG. OF DELVSIN                 DP B7 M/CS
# RTIG            POSITION AT TIME OF IGNITION    VECTOR B29 M
# VTIG            VELOCITY AT TIME OF IGNITION    VECTOR B7 M/CS.
# IF AIMPT STEER:
# TIG             TIME OF IGNITION                DP B28 CS
# RTARG           POSITION TARGET TIME            VECTOR B29 M
# CSTEER          C FOR STEER LAW                 DP B2
# DLTARG          TARGET TIME-IGNITION TIME       DP B28 CS
#
# OUTPUT
# UT              DESIRED THRUST DIRECTION        VECT. B2 M/(CS.CS)
# VGTIG           INITIAL VALUE OF VELOCITY
# TO BE GAINED (INERT. COORD.)    VECTOR B7 M/CS
# DELVLVC         VGTIG IN LOC. VERT. COORDS.     B7 M/CS
# BDT             V REQUIRED AT TIG -V REQUIRED AT (TIG-2SEC)
# -GDT         FOR S40.13                      VECT B7 M/CS
# RTIG            CALC IN S40.1B (AIMPT) FOR S40.2,3      VECTOR B27M
# POSITION AT TIME OF IGNITION
#
# DEBRIS        QTEMP1
# MPAC, QPRET
# PUSHLIST

#   BANK 14
#   SETLOC P40S1
#   BANK
# Page 765
#   COUNT* $$/S40.1
W('27,2246', 0o71220, 'S40.1', 'STQ', 'DLOAD', kind='interp', line=684)
W('27,2247', 0o03632, '', '', 'QTEMP', kind='operand', line=685)
W('27,2250', 0o03442, '', '', 'TIG', kind='operand', line=686)
W('27,2251', 0o03763, '', 'STORE', 'TIGSAVE', kind='interp', line=687)
W('27,2252', 0o77614, 'DELVTEST', 'BOFF', kind='interp', line=688)
W('27,2253', 0o01347, '', '', 'XDELVFLG', kind='operand', line=689)
W('27,2254', 0o56336, '', '', 'S40.1B', kind='operand', line=690)
W('27,2255', 0o77201, 'CALCTHET', 'SETPD', 'VLOAD', kind='interp', line=691)
W('27,2256', 0o00001, '', '', '0', kind='operand', line=692)
W('27,2257', 0o03650, '', '', 'VTIG', kind='operand', line=693)
W('27,2260', 0o02331, '', 'STORE', 'VINIT', kind='interp', line=694)
W('27,2261', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=695)
W('27,2262', 0o03642, '', '', 'RTIG', kind='operand', line=696)
W('27,2263', 0o27673, '', 'STOVL', 'UT', 'UP IN UT', kind='interp', line=697)
W('27,2264', 0o03642, '', '', 'RTIG', kind='operand', line=698)
W('27,2265', 0o02323, '', 'STORE', 'RINIT', kind='interp', line=699)
W('27,2266', 0o65236, '', 'VSQ', 'PDDL', kind='interp', line=700)
W('27,2267', 0o00045, '', '', '36D', kind='operand', line=701)
W('27,2270', 0o56205, '', 'DMP', 'DDV', kind='interp', line=702)
W('27,2271', 0o16412, '', '', 'THETACON', kind='operand', line=703)
W('27,2272', 0o41205, '', 'DMP', 'DMP', kind='interp', line=704)
W('27,2273', 0o03664, '', '', 'DELVSAB', kind='operand', line=705)
W('27,2274', 0o01245, '', '', 'WEIGHT/G', kind='operand', line=706)
W('27,2275', 0o77671, '', 'DDV', kind='interp', line=707)
W('27,2276', 0o03735, '', '', 'F', kind='operand', line=708)
W('27,2277', 0o24017, '', 'STOVL', '14D', kind='interp', line=709)
W('27,2300', 0o03656, '', '', 'DELVSIN', kind='operand', line=710)

W('27,2301', 0o74241, '', 'DOT', 'VXSC', kind='interp', line=712)
W('27,2302', 0o03673, '', '', 'UT', kind='operand', line=713)
W('27,2303', 0o03673, '', '', 'UT', kind='operand', line=714)
W('27,2304', 0o41552, '', 'VSL2', 'PUSH', '(DELTAV.UP)UP SCALED AT 2(+7) P.D.L. 0', kind='interp', line=715)
W('27,2305', 0o65245, '', 'BVSU', 'PDDL', 'DELTA VP SCALED AT 2(+7) P.D.L. 6', kind='interp', line=716)
W('27,2306', 0o03656, '', '', 'DELVSIN', kind='operand', line=717)
W('27,2307', 0o00017, '', '', '14D', kind='operand', line=718)
W('27,2310', 0o63356, '', 'SIN', 'PDVL', kind='interp', line=719)
W('27,2311', 0o00007, '', '', '6D', kind='operand', line=720)
W('27,2312', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=721)
W('27,2313', 0o03673, '', '', 'UT', kind='operand', line=722)
W('27,2314', 0o45561, '', 'VXSC', 'STADR', kind='interp', line=723)
W('27,2315', 0o50076, '', 'STOVL', 'VGTIG', 'UNIT(VP X UP)SIN(THETAT/2) IN VGTIG.', kind='interp', line=724)
W('27,2316', 0o65256, '', 'UNIT', 'PDDL', 'UNIT(DELTA VP) IN P.D.L. 6', kind='interp', line=725)
W('27,2317', 0o00017, '', '', '14D', kind='operand', line=726)
W('27,2320', 0o74346, '', 'COS', 'VXSC', kind='interp', line=727)
W('27,2321', 0o74255, '', 'VAD', 'VXSC', kind='interp', line=728)
W('27,2322', 0o03701, '', '', 'VGTIG', kind='operand', line=729)
W('27,2323', 0o00045, '', '', '36D', kind='operand', line=730)
W('27,2324', 0o53352, '', 'VSL2', 'VAD', kind='interp', line=731)
W('27,2325', 0o77626, '', 'STADR', kind='interp', line=732)
# Page 766
W('27,2326', 0o74076, '', 'STORE', 'VGTIG', 'VG IGNITION SCALED AT 2(+7) M/CS', kind='interp', line=734)

W('27,2327', 0o77656, '', 'UNIT', kind='interp', line=736)
W('27,2330', 0o27673, '', 'STOVL', 'UT', 'THRUST DIRECTION SCALED AT 2(+1)', kind='interp', line=737)
W('27,2331', 0o03701, '', '', 'VGTIG', kind='operand', line=738)
W('27,2332', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=739)
W('27,2333', 0o15733, '', '', 'GET.LVC', 'VGTIG IN LV COOR AT 2(+7) M/CS IN DELVLVC', kind='operand', line=740)
W('27,2334', 0o77650, '', 'GOTO', kind='interp', line=741)
W('27,2335', 0o03632, '', '', 'QTEMP', kind='operand', line=742)
W('27,2336', 0o77745, 'S40.1B', 'DLOAD', kind='interp', line=743)
W('27,2337', 0o03442, '', '', 'TIG', kind='operand', line=744)
W('27,2340', 0o00041, '', 'STORE', 'TDEC1', kind='interp', line=745)
W('27,2341', 0o77621, '', 'BDSU', kind='interp', line=746)
W('27,2342', 0o03631, '', '', 'TPASS4', kind='operand', line=747)
W('27,2343', 0o37452, '', 'STCALL', 'DELLT4', 'INTERCEPT TIME -- TIG.', kind='interp', line=748)
W('27,2344', 0o27057, '', '', 'LEMPREC', kind='operand', line=749)
W('27,2345', 0o40375, '', 'VLOAD', 'SETPD', 'LOAD STATE VECTOR AT TIG FOR INITVEL.', kind='interp', line=750)
W('27,2346', 0o00001, '', '', 'RATT', kind='operand', line=751)
W('27,2347', 0o00001, '', '', '0', kind='operand', line=752)
W('27,2350', 0o03642, '', 'STORE', 'RTIG', kind='interp', line=753)
W('27,2351', 0o02323, '', 'STORE', 'RINIT', kind='interp', line=754)
W('27,2352', 0o77656, '', 'UNIT', kind='interp', line=755)
W('27,2353', 0o27537, '', 'STOVL', 'UNIT/R/', kind='interp', line=756)
W('27,2354', 0o00007, '', '', 'VATT', kind='operand', line=757)
W('27,2355', 0o03650, '', 'STORE', 'VTIG', kind='interp', line=758)
W('27,2356', 0o02331, '', 'STORE', 'VINIT', kind='interp', line=759)
W('27,2357', 0o65345, '', 'DLOAD', 'PDDL', 'NUMIT = 0', kind='interp', line=760)
W('27,2360', 0o06522, '', '', 'ZEROVECS', kind='operand', line=761)
W('27,2361', 0o16406, '', '', 'EPS1', kind='operand', line=762)
W('27,2362', 0o43214, '', 'BOFF', 'DAD', kind='interp', line=763)
W('27,2363', 0o03745, '', '', 'NORMSW', kind='operand', line=764)
W('27,2364', 0o56366, '', '', 'SMALLEPS', kind='operand', line=765)
W('27,2365', 0o16410, '', '', 'EPS2', 'EPSILON4 = 10 DEGREES OR 45 DEGREES.', kind='operand', line=766)
W('27,2366', 0o66006, 'SMALLEPS', 'PUSH', 'SXA,1', kind='interp', line=767)
W('27,2367', 0o02776, '', '', 'RTX1', kind='operand', line=768)
W('27,2370', 0o45134, '', 'SXA,2', 'CALL', kind='interp', line=769)
W('27,2371', 0o02777, '', '', 'RTX2', kind='operand', line=770)
W('27,2372', 0o22000, '', '', 'INITVEL', kind='operand', line=771)
W('27,2373', 0o41575, '', 'VLOAD', 'PUSH', kind='interp', line=772)
W('27,2374', 0o02366, '', '', 'DELVEET3', 'VGTIG = VR - VN.', kind='operand', line=773)
W('27,2375', 0o03701, '', 'STORE', 'VGTIG', kind='interp', line=774)
W('27,2376', 0o77656, '', 'UNIT', '', 'UT = UNIT (VGTIG)', kind='interp', line=775)
W('27,2377', 0o17673, '', 'STODL', 'UT', kind='interp', line=776)
W('27,2400', 0o00045, '', '', '36D', kind='operand', line=777)
W('27,2401', 0o37664, '', 'STCALL', 'VGDISP', 'CONVERT VGTIG (IN PUSHLIST) TO LOCAL', kind='interp', line=778)
W('27,2402', 0o15733, '', '', 'GET.LVC', 'VERTICAL COORDINATES.', kind='operand', line=779)
W('27,2403', 0o77650, '', 'GOTO', kind='interp', line=780)
W('27,2404', 0o03632, '', '', 'QTEMP', kind='operand', line=781)

W('27,2405', 0o00707, 'EPS1', '2DEC*', '2.777777778 E-2*', '10 DEGREES AT 1 REVOLUTION', kind='data', line=783)
W('27,2406', 0o03434, kind='data', line=783)

# Page 767
W('27,2407', 0o03070, 'EPS2', '2DEC*', '9.722222222 E-2*', '35 DEGREES AT 1 REVOLUTION.', kind='data', line=786)
W('27,2410', 0o34344, kind='data', line=786)

W('27,2411', 0o00024, 'THETACON', '2DEC', '.31830989 B-8', kind='data', line=788)
W('27,2412', 0o13714, kind='data', line=788)

# Page 768
# SUBROUTINE NAME:  S40.2,3             MOD. NO. 3, DATE APRIL 4, 1967
# MODIFICATION BY:  JONATHON D. ADDELSTON (ADAMS ASSOCIATES)
# MOD. NO. 4:  JULY 18, 1967: PETER ADLER (MIT/IL)
# MOD. NO. 5:  OCTOBER 18, 1967:  PETER ADLER (MIT/IL)
# ORIGINALLY BY:  SAYDEAN ZELDIN (MIT INSTRUMENTATION LAB) AND RICHARD TALAYCO (SYSTEM DELVELOPMENT CORP)
#
# S40.2,3 COMPUTES "POINTVSM" WHICH IS THE HALF-UNIT DESIRED THRUST VECTOR IN STABLE-MEMBER COORDINATES FROM "UT"
# WHICH IS THE SAME VECTOR IN REFERENCE COORDINATES.  IT DETERMINES THE CORRECT VALUES FOR "SCAXIS" USING THE +X
# AXIS FOR DPS, APS, AND RCS BURNS.  THE "WINGS-LEVEL HEADS-UP" LM ORIENTATION IS THEN COMPUTED IN REFERENCE
# COORDINATES.  THESE VECTORS ALSO DEFINE THE "PREFERRED IMU ORIENTATION".  UPON COMPLETION OF THIS CALCULATION,
# THE "PREFERRED ATTITUDE COMPUTED" FLAG IS SET (PFRATFLG).
#
# CALLING SEQUENCE:
# L       CALL                    # INTERPRETIVE CALL.
# L +1            S40.2,3
# L +2    (RETURN)                # GIMBAL ANGLE VECTOR IN MPAC.
#
# SUBROUTINES CALLED:  NONE.
#
# NORMAL RETURN:  L +2 (SEE CALLING SEQUENCE ABOVE).
#
# ALARM/ABORT MODES:  NONE.
#
# INPUT:
# 1.      REFSMMAT        MATRIX FROM REFERENCE TO STABLE-MEMBER COORDINATES SCALED AT 2.
# 2.      UT              HALF-UNIT DESIRED THRUST DIRECTION.
# 3.      RTIG            POSITION AT TIG IN REFERENCE COORDINATES.
#
# OUTPUT:
# 1.      `XSCREF'        WINGS-LEVEL HEADS-UP LM ORIENTATION
# `YSCREF'        IN REFERENCE COORDINATES
# `ZSCREF'        (PREFERRED IMU ORIENTATION).
# 2.      POINTVSM        DESIRED THRUST DIRECTION IN STABLE-MEMBER COORDINATES.
# 3.      SCAXIS          HALF-UNIT OF AXIS TO ALIGN IN STABLE-MEMBER COORDINATES.
# 4.      PFRATFLG        INTERPRETIVE FLAG.  ON: PREFERRED ORIENTATION COMPUTED; OFF: NOT COMPUTED.
#
# DEBRIS:  NONE
# Page 769

#   COUNT* $$/S40.2
W('27,2413', 0o77775, 'S40.2,3', 'VLOAD', '', 'UT:  DESIRED THRUST DIRECTION (HALF-UNIT)', kind='interp', line=831)
W('27,2414', 0o03673, '', '', 'UT', '(PUT INTO TOP OF PUSH-DOWN-LIST.)', kind='operand', line=832)
W('27,2415', 0o76521, '', 'MXV', 'VSL1', 'TRANSFORM THRUST DIRECTION TO STABLE-', kind='interp', line=833)
W('27,2416', 0o01734, '', '', 'REFSMMAT', 'MEMBER FROM REFERENCE COORDS (RESCALE).', kind='operand', line=834)
W('27,2417', 0o27773, '', 'STOVL', 'POINTVSM', 'SAVE FOR "VECPOINT" ROUTINE (LEMMANU).', kind='interp', line=835)
W('27,2420', 0o06520, '', '', 'UNITX', 'SCAXIS SET TO +X, FOR P40 AND P42 AND', kind='operand', line=836)
W('27,2421', 0o27765, '', 'STOVL', 'SCAXIS', 'FOR P41 IF RCS NOT -X,+Y,-Y,+Z,-Z.', kind='interp', line=837)

W('27,2422', 0o03673, '', '', 'UT', 'ASSUME +X BURN ALWAYS, EVEN FOR RCS.', kind='operand', line=839)
W('27,2423', 0o03607, 'PLUSX', 'STORE', 'XSCREF', 'XSCREF = UT (DESIRED THRUST DIRECTION)', kind='interp', line=840)
W('27,2424', 0o53435, '', 'VXV', 'UNIT', 'RTIG = POSITION AT TIME-OF-IGNITION.', kind='interp', line=841)
W('27,2425', 0o03642, '', '', 'RTIG', 'YSCREF = UNIT(UT X RTIG)', kind='operand', line=842)
W('27,2426', 0o46125, '', 'PDDL', 'BHIZ', kind='interp', line=843)
W('27,2427', 0o00045, '', '', '36D', 'TEST MAGNITUDE OF UT X RTIG', kind='operand', line=844)
W('27,2430', 0o56441, '', '', 'FIXY', 'IF SMALL, USE UT X VTIG AS YSC', kind='operand', line=845)
W('27,2431', 0o45575, 'STORY', 'VLOAD', 'STADR', kind='interp', line=846)
W('27,2432', 0o74162, '', 'STORE', 'YSCREF', kind='interp', line=847)
W('27,2433', 0o76435, '', 'VXV', 'VSL1', 'COMPUTE (YSCREF X XCREF), BUT FOR A', kind='interp', line=848)
W('27,2434', 0o03607, '', '', 'XSCREF', 'RIGHT HANDED SYSTEM, NEED (X CROSS Y).', kind='operand', line=849)
W('27,2435', 0o77676, '', 'VCOMP', '', 'ZSCREF = - (YSCREF X XSCREF)', kind='interp', line=850)
W('27,2436', 0o03623, '', 'STORE', 'ZSCREF', '       = + (XSCREF X YSCREF)', kind='interp', line=851)

W('27,2437', 0o43414, '', 'SET', 'RVQ', kind='interp', line=853)
W('27,2440', 0o01073, '', '', 'PFRATFLG', kind='operand', line=854)
W('27,2441', 0o47375, 'FIXY', 'VLOAD', 'VXV', 'IN THIS CASE,', kind='interp', line=855)
W('27,2442', 0o03607, '', '', 'XSCREF', 'YSCREF = UNIT(XSCREF X VTIG)', kind='operand', line=856)
W('27,2443', 0o03650, '', '', 'VTIG', kind='operand', line=857)
W('27,2444', 0o41456, '', 'UNIT', 'PUSH', kind='interp', line=858)
W('27,2445', 0o77650, '', 'GOTO', kind='interp', line=859)
W('27,2446', 0o56431, '', '', 'STORY', kind='operand', line=860)
# Page 770
# SUBROUTINE S40.8
# MODIFIED APRIL 3, 1968 BY PETER ADLER, MIT/IL
#
# DESCRIPTION
# S40.8 UPDATES THE VELOCITY-TO-BE-GAINED VECTOR, VG, (AND FOR LAMBERT TARGETTED BURNS ALSO EXTRAPOLATES VG
# USING THE BDT VECTOR) COMPUTES THE TIME FOR ISSUING THE ENGINE OFF COMMAND, TGO, AND CALLS THE ROUTINE
# "FINDCDUW", WHICH GENERATES STEERING COMMANDS FOR THE DAP.
#
# CALLING SEQUENCE
# L-1     CALL
# L               S40.8
# L+1                     INTERPRETIVE RETURN
#
# ALARM
# IF VG . DELVREF IS NEGATIVE (VG AND DELVREF OVER 90 DEGREES APART), BYPASS TGO AND STEERING COMPUTATIONS
# AND SET ALARM 1407.  RETURN TO CALLER NORMALLY.
#
# INPUT AND INITIALIZATION
# VGPREV          REFERENCE       2(7) M/CS
# DELVREF         REFERENCE       2(7) M/CS
# BDT             REFERENCE       2(7) M/CS
# TDECAY          TAIL-OFF TIME   2(28) CS
# XDELVFLG        1 = EXTERNAL DELTA-V; 0 = LAMBERT (AIMPOINT)
# STEERSW         1 = DO STEERING AND TGO COMPUTATIONS; 0 = VG UPDATE ONLY
# FIRSTFLG        1 = GONE TO LAMBERT AT LEAST ONCE; 0 = HAVEN'T GONE TO LAMBERT YET.
#
# NOTE:  VGTIG EQUALS VGPREV
#
# OUTPUT
# STEERSW         SEE INPUT
# INPULSW         1 = ENGINE OFF IN TGO CENTISECONDS; 0 = CONTINUE BURN
# TGO             TIME TO CUT-OFF 2(28) CS
# SEE FINDCDUW FOR STEERING OUTPUTS.
#
# SUBROUTINE CALLED
# FINDCDUW
#
# DEBRIS
# MPACS, PUSHLIST

#   COUNT* $$/S40.8
# Page 771
W('27,2447', 0o77614, 'S40.8', 'BOF', '', 'GENERATE VR IF NOT EXTERNAL DELTA-V BURN', kind='interp', line=904)
W('27,2450', 0o01347, '', '', 'XDELVFLG', kind='operand', line=905)
W('27,2451', 0o56731, '', '', 'RASTEER1', kind='operand', line=906)
W('27,2452', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=907)
W('27,2453', 0o03701, '', '', 'VGPREV', kind='operand', line=908)
W('27,2454', 0o03527, '', '', 'DELVREF', kind='operand', line=909)
W('27,2455', 0o03707, 'VGAIN*', 'STORE', 'VG', 'VELOCITY TO BE GAINED SCALED AT (7) M/CS', kind='interp', line=910)
W('27,2456', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=911)
W('27,2457', 0o01734, '', '', 'REFSMMAT', kind='operand', line=912)
W('27,2460', 0o03254, '', 'STORE', 'UNFC/2', kind='interp', line=913)
W('27,2461', 0o51575, 'BDTOK', 'VLOAD', 'ABVAL', kind='interp', line=914)
W('27,2462', 0o03707, '', '', 'VG', kind='operand', line=915)
W('27,2463', 0o03664, '', 'STORE', 'VGDISP', kind='interp', line=916)
W('27,2464', 0o77201, 'TGDCALC', 'SETPD', 'VLOAD', kind='interp', line=917)
W('27,2465', 0o00001, '', '', '0', kind='operand', line=918)
W('27,2466', 0o03707, '', '', 'VG', kind='operand', line=919)
W('27,2467', 0o27701, '', 'STOVL', 'VGPREV', kind='interp', line=920)
W('27,2470', 0o03527, '', '', 'DELVREF', kind='operand', line=921)
W('27,2471', 0o57414, '', 'BOFF', 'VCOMP', kind='interp', line=922)
W('27,2472', 0o01344, '', '', 'STEERSW', kind='operand', line=923)
W('27,2473', 0o00052, '', '', 'QPRET', kind='operand', line=924)
W('27,2474', 0o77656, '', 'UNIT', kind='interp', line=925)
W('27,2475', 0o41441, '', 'DOT', 'PUSH', kind='interp', line=926)
W('27,2476', 0o03707, '', '', 'VG', kind='operand', line=927)
W('27,2477', 0o56244, '', 'BPL', 'DDV', kind='interp', line=928)
W('27,2500', 0o56526, '', '', 'ALARMIT', 'DELV IS MORE THAN 90 DEGREES FROM VG.', kind='operand', line=929)
W('27,2501', 0o03743, '', '', 'VEX', kind='operand', line=930)
W('27,2502', 0o41215, '', 'DAD', 'DMP', kind='interp', line=931)
W('27,2503', 0o06520, '', '', 'DPHALF', kind='operand', line=932)
W('27,2504', 0o56261, '', 'SR', 'DDV', kind='interp', line=933)
W('27,2505', 0o20613, '', '', '10D', kind='operand', line=934)
W('27,2506', 0o00045, '', '', '36D', kind='operand', line=935)
W('27,2507', 0o43205, '', 'DMP', 'DAD', kind='interp', line=936)
W('27,2510', 0o16535, '', '', '-FOURDT', kind='operand', line=937)
W('27,2511', 0o03741, '', '', 'TDECAY', kind='operand', line=938)
W('27,2512', 0o03517, '', 'STORE', 'TGO', kind='interp', line=939)
W('27,2513', 0o77615, '', 'DAD', kind='interp', line=940)
W('27,2514', 0o01235, '', '', 'PIPTIME', kind='operand', line=941)
W('27,2515', 0o17442, '', 'STODL', 'TIG', kind='interp', line=942)
W('27,2516', 0o03517, '', '', 'TGO', kind='operand', line=943)
W('27,2517', 0o51025, '', 'DSU', 'BPL', kind='interp', line=944)
W('27,2520', 0o16537, '', '', 'FOURSECS', '400 CS', kind='operand', line=945)
W('27,2521', 0o61111, '', '', 'FINDCDUW -2', kind='operand', line=946)
W('27,2522', 0o43014, '', 'SET', 'CLRGO', kind='interp', line=947)
W('27,2523', 0o01066, '', '', 'IMPULSW', kind='operand', line=948)
W('27,2524', 0o01224, '', '', 'STEERSW', kind='operand', line=949)
W('27,2525', 0o00052, '', '', 'QPRET', kind='operand', line=950)

W('27,2526', 0o77776, 'ALARMIT', 'EXIT', kind='interp', line=952)

# Page 772
W('27,2527', 0o05567, '', 'TC', 'ALARM', line=955)
W('27,2530', 0o01407, '', 'OCT', '01407', kind='data', line=956)
W('27,2531', 0o06037, '', 'TC', 'INTPRET', line=957)
W('27,2532', 0o77650, '', 'GOTO', '', 'SKIP TGO COMPUTATION BUT CALL FINDCDUW.', kind='interp', line=958)
W('27,2533', 0o61111, '', '', 'FINDCDUW -2', 'FINDCDUW WILL EXIT TO UPDATEVG +3.', kind='operand', line=959)

W('27,2534', 0o77715, '-FOURDT', '2DEC', '-800 B-18', '-4 (200 CS.) B(-18)', kind='data', line=961)
W('27,2535', 0o77777, kind='data', line=961)
W('27,2536', 0o00000, 'FOURSECS', '2DEC', '400', '400 CS SCALED AT 2(+28) CS', kind='data', line=962)
W('27,2537', 0o00620, kind='data', line=962)
S('2VEXHUST', 'equals', 0o3742, line=963)

# Page 773
# NAME:                 S40.13 -- TIMEBURN
#
# FUNCTION              (1) DETERMINE WHETHER A GIVEN COMBINATION OF VELOCITY TO
# BE GAINED AND ENGINE CHOICE RESULT IN A BURN TIME
# SUFFICIENT TO ALLOW STEERING AT THE VEHICLE DURING THE
# BURN
# (2) THE MAGNITUDE OF THE RESULTING BURN TIME -- IF IT
# IS SHORT -- AND THE ASSOCIATED TIME OF THE ENGINE OFF
# SIGNAL
#
# CALLING SEQUENCE      VIA FINDVAC AS A NEW JOB
#
# INPUT                 VGTIG -- VELOCITY TO BE GAINED VECTOR (METERS/CS) AT +7
# WEIGHT/G -- MASS OF VEHICLE IN KGM AT +16
# F -- APS ENGINE THRUST IN M.NEWTONS AT +7
# AND ALSO FOR RCS ENGINE
# MDOT -- RATE OF DECREASE OF VEHICLE MASS DURING ENGINE
# BURN IN KILOGRAMS/CS AT +3.  THIS SCALING MAY
# REQUIRE MODIFICATION FOR SATURN BURNS.
# ENG1FLAG -- SWITCH TO DECIDE WHETHER APS OR DPS ENGINE IS USED
# =0      DPS
# =1      APS
#
# OUTPUT                IMPULSW         ZERO FOR STEERING
# ONE FOR ATTITUDE HOLD
# NOTHROTL        ZERO FOR THROTTLING
# ONE TO INHIBIT THROTTLING
# TGO             TIME TO BURN IN CS
#
# THE QUANTITY M.NEWTON = 10000 NEWTONS WILL BE USED TO EXPRESS
# FORCE.

#   EBANK= TGO
#   COUNT* $$/40.13
W('27,2540', 0o06037, 'S40.13', 'TC', 'INTPRET', line=1000)
W('27,2541', 0o43001, '', 'SETPD', 'CLEAR', kind='interp', line=1001)
W('27,2542', 0o00001, '', '', '00D', kind='operand', line=1002)
W('27,2543', 0o01266, '', '', 'IMPULSW', 'ASSUME NO STEERING UNTIL FOUND OTHERWISE', kind='operand', line=1003)
W('27,2544', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=1004)
W('27,2545', 0o03701, '', '', 'VGTIG', 'VELOCITY TO BE GAINED AT +7', kind='operand', line=1005)
W('27,2546', 0o41325, '', 'PDDL', 'DMP', '00D = MAG OF VGTIG AT +7', kind='interp', line=1006)
W('27,2547', 0o21021, '', '', '4SEC(17)', 'CORRECT VG FOR 4 SECS OF 2 JET ULLAGE', kind='operand', line=1007)
W('27,2550', 0o34017, '', '', 'FRCS2', kind='operand', line=1008)
W('27,2551', 0o72471, '', 'DDV', 'SL1', 'SCALE', kind='interp', line=1009)
W('27,2552', 0o01245, '', '', 'WEIGHT/G', kind='operand', line=1010)
W('27,2553', 0o41421, '', 'BDSU', 'PUSH', kind='interp', line=1011)
W('27,2554', 0o43014, '', 'BOFF', 'SET', kind='interp', line=1012)
W('27,2555', 0o05342, '', '', 'APSFLAG', kind='operand', line=1013)
W('27,2556', 0o56626, '', '', 'S40.13D', 'FOR DPS ENGINE', kind='operand', line=1014)
W('27,2557', 0o02463, '', '', 'NOTHROTL', kind='operand', line=1015)
W('27,2560', 0o56345, '', 'DLOAD', 'DDV', '00D = MAG OF VGTIG CORRECTED', kind='interp', line=1016)
W('27,2561', 0o16001, '', '', 'K1VAL', 'M.NEWTONS-CS AT +24', kind='operand', line=1017)
W('27,2562', 0o01245, '', '', 'WEIGHT/G', kind='operand', line=1018)
W('27,2563', 0o50021, '', 'BDSU', 'BMN', kind='interp', line=1019)
# Page 774
W('27,2564', 0o00001, '', '', '00D', kind='operand', line=1021)
W('27,2565', 0o56610, '', '', 'S40.131', 'TGO LESS THAN 100 CS', kind='operand', line=1022)
W('27,2566', 0o41325, '', 'PDDL', 'DMP', '02D = TEMP1 AT +7', kind='interp', line=1023)
W('27,2567', 0o03737, '', '', 'MDOT', kind='operand', line=1024)

# MDOT REPRESENTS THE RATE OF DECREASE OF VEHICLE MASS DURING ENGINE
# BURN IN KILOGRAMS/CS.  WHEN SATURN IS USED, THE SCALING MAY
# REQUIRE ADJUSTMENT.

W('27,2570', 0o16700, '', '', '3.5SEC', '350 CS AT +14', kind='operand', line=1030)
W('27,2571', 0o65221, '', 'BDSU', 'PDDL', kind='interp', line=1031)
W('27,2572', 0o01245, '', '', 'WEIGHT/G', kind='operand', line=1032)
W('27,2573', 0o03735, '', '', 'F', kind='operand', line=1033)
W('27,2574', 0o60405, '', 'DMP', 'SR2', 'SCALE', kind='interp', line=1034)
W('27,2575', 0o16702, '', '', '5SECS', kind='operand', line=1035)
W('27,2576', 0o41471, '', 'DDV', 'PUSH', '04D = TEMP2', kind='interp', line=1036)
W('27,2577', 0o51021, '', 'BDSU', 'BPL', kind='interp', line=1037)
W('27,2600', 0o00003, '', '', '02D', kind='operand', line=1038)
W('27,2601', 0o56626, '', '', 'S40.13D', kind='operand', line=1039)
W('27,2602', 0o55345, '', 'DLOAD', 'BDDV', kind='interp', line=1040)
W('27,2603', 0o43205, '', 'DMP', 'DAD', kind='interp', line=1041)
W('27,2604', 0o16702, '', '', '5SECS', kind='operand', line=1042)
W('27,2605', 0o16676, '', '', '1SEC2D', '100 CS AT +14', kind='operand', line=1043)
W('27,2606', 0o77650, '', 'GOTO', kind='interp', line=1044)
W('27,2607', 0o56616, '', '', 'S40.132', kind='operand', line=1045)
W('27,2610', 0o41345, 'S40.131', 'DLOAD', 'DMP', kind='interp', line=1046)
W('27,2611', 0o01245, '', '', 'WEIGHT/G', kind='operand', line=1047)
W('27,2612', 0o41542, '', 'SR1', 'PUSH', kind='interp', line=1048)
W('27,2613', 0o56215, '', 'DAD', 'DDV', kind='interp', line=1049)
W('27,2614', 0o16003, '', '', 'K2VAL', 'M.NEWTON CS AT +24', kind='operand', line=1050)
W('27,2615', 0o16005, '', '', 'K3VAL', 'M.NEWTON CS AT +10', kind='operand', line=1051)
W('27,2616', 0o77414, 'S40.132', 'SET', 'EXIT', kind='interp', line=1052)
W('27,2617', 0o01066, '', '', 'IMPULSW', kind='operand', line=1053)
W('27,2620', 0o07257, 'S40.132*', 'TC', 'TPAGREE', line=1054)
W('27,2621', 0o30154, '', 'CA', 'MPAC', line=1055)
W('27,2622', 0o56001, '', 'XCH', 'L', line=1056)
W('27,2623', 0o34755, '', 'CA', 'ZERO', line=1057)
W('27,2624', 0o53517, '', 'DXCH', 'TGO', line=1058)
W('27,2625', 0o12650, '', 'TCF', 'S40.134', line=1059)

W('27,2626', 0o41345, 'S40.13D', 'DLOAD', 'DMP', 'FOR DPS ENGINE', kind='interp', line=1061)
W('27,2627', 0o00001, '', '', '00D', kind='operand', line=1062)
W('27,2630', 0o01245, '', '', 'WEIGHT/G', kind='operand', line=1063)
W('27,2631', 0o43006, '', 'PUSH', 'BON', kind='interp', line=1064)
W('27,2632', 0o05302, '', '', 'APSFLAG', kind='operand', line=1065)
W('27,2633', 0o56671, '', '', 'APSTGO', kind='operand', line=1066)
W('27,2634', 0o43071, '', 'DDV', 'CLEAR', kind='interp', line=1067)
W('27,2635', 0o16007, '', '', 'S40.136', kind='operand', line=1068)
W('27,2636', 0o02663, '', '', 'NOTHROTL', kind='operand', line=1069)
W('27,2637', 0o41400, '', 'BOV', 'PUSH', kind='interp', line=1070)
# Page 775
W('27,2640', 0o56653, '', '', 'S40.130V', kind='operand', line=1072)
W('27,2641', 0o51025, 'S40.127', 'DSU', 'BPL', kind='interp', line=1073)
W('27,2642', 0o16704, '', '', '6SEC', '600.0 CS AT +14', kind='operand', line=1074)
W('27,2643', 0o56661, '', '', 'S40.138', kind='operand', line=1075)
W('27,2644', 0o52015, '', 'DAD', 'GOTO', kind='interp', line=1076)
W('27,2645', 0o16704, '', '', '6SEC', kind='operand', line=1077)
W('27,2646', 0o56616, '', '', 'S40.132', kind='operand', line=1078)
W('27,2647', 0o77776, 'S40.133', 'EXIT', kind='interp', line=1079)
W('27,2650', 0o05353, 'S40.134', 'TC', 'PHASCHNG', line=1080)
W('27,2651', 0o00003, '', 'OCT', '00003', kind='data', line=1081)
W('27,2652', 0o05155, '', 'TC', 'ENDOFJOB', line=1082)
W('27,2653', 0o40545, 'S40.130V', 'DLOAD', 'SR4', 'RECOMPUTED TGO IN TIMER UNITS', kind='interp', line=1083)
W('27,2654', 0o77671, '', 'DDV', kind='interp', line=1084)
W('27,2655', 0o16011, '', '', 'S40.136_', 'S40.136 SHIFTED LEFT 10', kind='operand', line=1085)
W('27,2656', 0o03517, '', 'STORE', 'TGO', kind='interp', line=1086)
W('27,2657', 0o77776, '', 'EXIT', kind='interp', line=1087)
W('27,2660', 0o12650, '', 'TCF', 'S40.134', 'REJOIN COMMON CODING FOR RESTART PROTECT', line=1088)

W('27,2661', 0o51025, 'S40.138', 'DSU', 'BPL', kind='interp', line=1090)
W('27,2662', 0o16706, '', '', '89SECS', kind='operand', line=1091)
W('27,2663', 0o56666, '', '', 'STORETGO', kind='operand', line=1092)
W('27,2664', 0o77614, '', 'SET', kind='interp', line=1093)
W('27,2665', 0o02463, '', '', 'NOTHROTL', kind='operand', line=1094)
W('27,2666', 0o77745, 'STORETGO', 'DLOAD', '', 'LOAD TGO AT 2(14)', kind='interp', line=1095)
W('27,2667', 0o77776, '', 'EXIT', kind='interp', line=1096)
W('27,2670', 0o12620, '', 'TCF', 'S40.132*', line=1097)

W('27,2671', 0o62471, 'APSTGO', 'DDV', 'SL2', kind='interp', line=1099)
W('27,2672', 0o34007, '', '', 'FAPS', kind='operand', line=1100)
W('27,2673', 0o77650, '', 'GOTO', kind='interp', line=1101)
W('27,2674', 0o56667, '', '', 'STORETGO +1', kind='operand', line=1102)
W('27,2675', 0o00144, '1SEC2D', '2DEC', '100.0 B-14', '100.0 CS AT +14', kind='data', line=1103)
W('27,2676', 0o00000, kind='data', line=1103)

W('27,2677', 0o01274, '3.5SEC', '2DEC', '350.0 B-13', '350 CS AT +13', kind='data', line=1105)
W('27,2700', 0o00000, kind='data', line=1105)

W('27,2701', 0o00764, '5SECS', '2DEC', '500.0 B-14', '500.0 CS AT +14', kind='data', line=1107)
W('27,2702', 0o00000, kind='data', line=1107)

W('27,2703', 0o01130, '6SEC', '2DEC', '600.0 B-14', '600.0 CS AT +14', kind='data', line=1109)
W('27,2704', 0o00000, kind='data', line=1109)

W('27,2705', 0o21304, '89SECS', '2DEC', '8900.0 B-14', kind='data', line=1111)
W('27,2706', 0o00000, kind='data', line=1111)

# FUNCTION              (1) GENERATES REQUIRED VELOCITY AND VELOCITY-TO-BE-GAINED
# VECTORS FOR USE DURING AIMPOINT MANEUVERS EVERY TWO
# COMPUTATION CYCLES (4 SECONDS).
# (2) UPDATES THE B VECTOR WHICH IS USED IN THE FINAL
# CALCULATION OF EXTRAPOLATING THE VELOCITY-TO-BE-GAINED
# THROUGH ONE 2-SECOND INTERVAL INTO THE FUTURE.
#
# CALLING SEQUENCE      VIA FINDVAC AS NEW JOB.
#
# INPUT                 RN      ACTIVE VEHICLE RADIUS VECTOR IN METERS AT +29
# VN      ACTIVE VEHICLE VELOCITY VECTOR IN METERS/CS AT +7
# Page 776
# VPREV   LAST COMPUTED VELOCITY REQUIRED VECTOR IN
# METERS/CS AT +7.
# TIG     TIME OF IGNITION IN CS AT +28.
# DLTARG  COMPUTATION CYCLE INTERVAL = 200 CS AT +28.
# PIPTIME TIME OF RN AND VN IN CS AT +28.
# GDT/2   HALF OF VELOCITY GAINED IN DELTA T TIME DUE TO
# ACCELERATION OF GRAVITY IN METERS/CS AT +7.
# DELVREF CHANGE IN VELOCITY DURING LAST 2 SEC IN
# METERS/CS AT +7.
#
# OUTPUT                VGPREV  VELOCITY TO BE GAINED VECTOR IN METERS/CS AT +7.
# VGDISP  MAG OF VGPREV FOR DISPLAY PURPOSES.
# VRPREV  VELOCTY REQUIRED VECTOR IN METERS/CS AT +7.
# BDT     B VECTOR IN METERS/CS AT +7.
#
# SUBROUTINES USED      INITVEL

#   EBANK= VGPREV
#   COUNT* $$/S40.9
W('27,2707', 0o06037, 'S40.9', 'TC', 'INTPRET', line=1144)
W('27,2710', 0o77601, '', 'SETPD', kind='interp', line=1145)
W('27,2711', 0o00001, '', '', '00D', kind='operand', line=1146)
W('27,2712', 0o71214, '', 'SET', 'DLOAD', kind='interp', line=1147)
W('27,2713', 0o01072, '', '', 'AVFLAG', 'SET AVFLAG FOR LEM ACTIVE', kind='operand', line=1148)
W('27,2714', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=1149)
W('27,2715', 0o77725, '', 'PDDL', kind='interp', line=1150)
W('27,2716', 0o16406, '', '', 'EPS1', kind='operand', line=1151)
W('27,2717', 0o43214, '', 'BOFF', 'DAD', 'EPSILON4 = 10 OR 45 DEGREES.', kind='interp', line=1152)
W('27,2720', 0o03745, '', '', 'NORMSW', kind='operand', line=1153)
W('27,2721', 0o56723, '', '', 'EPSSMALL', kind='operand', line=1154)
W('27,2722', 0o16410, '', '', 'EPS2', kind='operand', line=1155)
W('27,2723', 0o45006, 'EPSSMALL', 'PUSH', 'CALL', kind='interp', line=1156)
W('27,2724', 0o22002, '', '', 'HAVEGUES', kind='operand', line=1157)
W('27,2725', 0o77776, 'ENDS40.9', 'EXIT', kind='interp', line=1158)
W('27,2726', 0o05353, '', 'TC', 'PHASCHNG', line=1159)
W('27,2727', 0o00002, '', 'OCT', '2', kind='data', line=1160)
W('27,2730', 0o15155, '', 'TCF', 'ENDOFJOB', line=1161)

W('27,2731', 0o51575, 'RASTEER1', 'VLOAD', 'ABVAL', kind='interp', line=1163)
W('27,2732', 0o01221, '', '', 'RN', kind='operand', line=1164)
W('27,2733', 0o53744, '', 'LXC,2', 'SL*', kind='interp', line=1165)
W('27,2734', 0o02777, '', '', 'RTX2', kind='operand', line=1166)
W('27,2735', 0o57576, '', '', '0,2', kind='operand', line=1167)
W('27,2736', 0o27715, '', 'STOVL', 'RMAG', kind='interp', line=1168)
W('27,2737', 0o03444, '', '', 'RTARG', kind='operand', line=1169)
W('27,2740', 0o47051, '', 'VSU', 'RTB', kind='interp', line=1170)
W('27,2741', 0o01221, '', '', 'RN', kind='operand', line=1171)
W('27,2742', 0o21724, '', '', 'NORMUNX1', kind='operand', line=1172)
W('27,2743', 0o17656, '', 'STODL', 'IC', kind='interp', line=1173)
W('27,2744', 0o00045, '', '', '36D', 'C(36D) = ABVAL(C)', kind='operand', line=1174)
W('27,2745', 0o53674, '', 'XAD,2', 'SL*', kind='interp', line=1175)
W('27,2746', 0o00046, '', '', 'X1', kind='operand', line=1176)
# Page 777
W('27,2747', 0o57576, '', '', '0,2', kind='operand', line=1178)
W('27,2750', 0o00037, '', 'STORE', '30D', kind='interp', line=1179)
W('27,2751', 0o41301, '', 'NORM', 'DMP', kind='interp', line=1180)
W('27,2752', 0o00050, '', '', 'X2', kind='operand', line=1181)
W('27,2753', 0o03715, '', '', 'RMAG', kind='operand', line=1182)
W('27,2754', 0o57101, '', 'NORM', 'XAD,2', kind='interp', line=1183)
W('27,2755', 0o00047, '', '', 'X1', kind='operand', line=1184)
W('27,2756', 0o00046, '', '', 'X1', kind='operand', line=1185)
W('27,2757', 0o77734, '', 'SXA,2', kind='interp', line=1186)
W('27,2760', 0o03766, '', '', 'MUSCALE', kind='operand', line=1187)
W('27,2761', 0o17725, '', 'STODL', 'R1C', '                      2(+56 -X)', kind='interp', line=1188)
W('27,2762', 0o00037, '', '', '30D', kind='operand', line=1189)
W('27,2763', 0o65342, '', 'SR1', 'PDDL', kind='interp', line=1190)
W('27,2764', 0o03715, '', '', 'RMAG', kind='operand', line=1191)
W('27,2765', 0o65342, '', 'SR1', 'PDDL', kind='interp', line=1192)
W('27,2766', 0o03723, '', '', 'RTMAG', kind='operand', line=1193)
W('27,2767', 0o43342, '', 'SR1', 'DAD', kind='interp', line=1194)
W('27,2770', 0o45415, '', 'DAD', 'STADR', kind='interp', line=1195)
W('27,2771', 0o74044, '', 'STORE', 'SS', 'SS = (R1 + R2 + C)/2', kind='interp', line=1196)
W('27,2772', 0o41225, '', 'DSU', 'DMP', kind='interp', line=1197)
W('27,2773', 0o00037, '', '', '30D', kind='operand', line=1198)
W('27,2774', 0o03721, '', '', 'MU/A', kind='operand', line=1199)
W('27,2775', 0o77621, '', 'BDSU', kind='interp', line=1200)
W('27,2776', 0o03717, '', '', 'MUASTEER', kind='operand', line=1201)
W('27,2777', 0o45325, '', 'PDDL', 'DSU', kind='interp', line=1202)
W('27,3000', 0o03733, '', '', 'SS', kind='operand', line=1203)
W('27,3001', 0o03715, '', '', 'RMAG', kind='operand', line=1204)
W('27,3002', 0o70501, '', 'NORM', 'SR1', kind='interp', line=1205)
W('27,3003', 0o00047, '', '', 'X1', kind='operand', line=1206)
W('27,3004', 0o41271, '', 'DDV', 'DMP', kind='interp', line=1207)
W('27,3005', 0o03725, '', '', 'R1C', kind='operand', line=1208)
W('27,3006', 0o53664, '', 'XSU,2', 'SL*', kind='interp', line=1209)
W('27,3007', 0o00046, '', '', 'X1', kind='operand', line=1210)
W('27,3010', 0o57575, '', '', '1,2', kind='operand', line=1211)
W('27,3011', 0o77754, '', 'LXA,2', kind='interp', line=1212)
W('27,3012', 0o03766, '', '', 'MUSCALE', kind='operand', line=1213)
W('27,3013', 0o75366, '', 'SQRT', 'SIGN', kind='interp', line=1214)
W('27,3014', 0o02673, '', '', 'GEOMSGN', kind='operand', line=1215)
W('27,3015', 0o00041, '', 'STORE', '32D', '+ OR - A', kind='interp', line=1216)
W('27,3016', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=1217)
W('27,3017', 0o03733, '', '', 'SS', kind='operand', line=1218)
W('27,3020', 0o03721, '', '', 'MU/A', kind='operand', line=1219)
W('27,3021', 0o77621, '', 'BDSU', kind='interp', line=1220)
W('27,3022', 0o03717, '', '', 'MUASTEER', kind='operand', line=1221)
W('27,3023', 0o45325, '', 'PDDL', 'DSU', kind='interp', line=1222)
W('27,3024', 0o03733, '', '', 'SS', kind='operand', line=1223)
W('27,3025', 0o03723, '', '', 'RTMAG', kind='operand', line=1224)
W('27,3026', 0o70501, '', 'NORM', 'SR1', kind='interp', line=1225)
W('27,3027', 0o00047, '', '', 'X1', kind='operand', line=1226)
W('27,3030', 0o41271, '', 'DDV', 'DMP', kind='interp', line=1227)

# Page 778
W('27,3031', 0o03725, '', '', 'R1C', kind='operand', line=1230)
W('27,3032', 0o53664, '', 'XSU,2', 'SL*', kind='interp', line=1231)
W('27,3033', 0o00046, '', '', 'X1', kind='operand', line=1232)
W('27,3034', 0o57575, '', '', '1,2', kind='operand', line=1233)
W('27,3035', 0o65366, '', 'SQRT', 'PDDL', '-B (NO SIGN)', kind='interp', line=1234)
W('27,3036', 0o03733, '', '', 'SS', kind='operand', line=1235)
W('27,3037', 0o56225, '', 'DSU', 'DDV', kind='interp', line=1236)
W('27,3040', 0o00037, '', '', '30D', kind='operand', line=1237)
W('27,3041', 0o03733, '', '', 'SS', kind='operand', line=1238)
W('27,3042', 0o41566, '', 'SQRT', 'PUSH', kind='interp', line=1239)
W('27,3043', 0o67542, '', 'SR1', 'ASIN', kind='interp', line=1240)
W('27,3044', 0o65205, '', 'DMP', 'PDDL', kind='interp', line=1241)
W('27,3045', 0o17216, '', '', '2PI+3', kind='operand', line=1242)
W('27,3046', 0o56325, '', 'PDDL', 'DDV', kind='interp', line=1243)
W('27,3047', 0o00037, '', '', '30D', kind='operand', line=1244)
W('27,3050', 0o03733, '', '', 'SS', kind='operand', line=1245)
W('27,3051', 0o77600, '', 'BOV', kind='interp', line=1246)
W('27,3052', 0o57053, '', '', '+1', kind='operand', line=1247)
W('27,3053', 0o41366, '', 'SQRT', 'DMP', kind='interp', line=1248)
W('27,3054', 0o44242, '', 'SR3', 'BDSU', kind='interp', line=1249)
W('27,3055', 0o65365, '', 'SIGN', 'PDDL', kind='interp', line=1250)
W('27,3056', 0o02673, '', '', 'GEOMSGN', kind='operand', line=1251)
W('27,3057', 0o17216, '', '', '2PI+3', kind='operand', line=1252)
W('27,3060', 0o45302, '', 'SR2', 'DSU', kind='interp', line=1253)
W('27,3061', 0o65205, '', 'DMP', 'PDDL', kind='interp', line=1254)
W('27,3062', 0o03733, '', '', 'SS', kind='operand', line=1255)
W('27,3063', 0o03733, '', '', 'SS', kind='operand', line=1256)
W('27,3064', 0o75442, '', 'SR3', 'SQRT', kind='interp', line=1257)
W('27,3065', 0o77605, '', 'DMP', kind='interp', line=1258)
W('27,3066', 0o52525, '', 'PDDL', 'SL3', kind='interp', line=1259)
W('27,3067', 0o03717, '', '', 'MUASTEER', kind='operand', line=1260)
W('27,3070', 0o55366, '', 'SQRT', 'BDDV', kind='interp', line=1261)
W('27,3071', 0o43225, '', 'DSU', 'DAD', kind='interp', line=1262)
W('27,3072', 0o03631, '', '', 'TPASS4', kind='operand', line=1263)
W('27,3073', 0o01235, '', '', 'PIPTIME', kind='operand', line=1264)
W('27,3074', 0o14037, '', 'STODL', '30D', kind='interp', line=1265)
W('27,3075', 0o77765, '', 'SIGN', kind='interp', line=1266)
W('27,3076', 0o00037, '', '', '30D', 'B WITH SIGN', kind='operand', line=1267)
W('27,3077', 0o00037, '', 'STORE', '30D', kind='interp', line=1268)
W('27,3100', 0o77214, '', 'BON', 'VLOAD', kind='interp', line=1269)
W('27,3101', 0o03705, '', '', 'NORMSW', kind='operand', line=1270)
W('27,3102', 0o57123, '', '', '180MESS', kind='operand', line=1271)
W('27,3103', 0o03656, '', '', 'IC', kind='operand', line=1272)
W('27,3104', 0o53451, '', 'VSU', 'UNIT', kind='interp', line=1273)
W('27,3105', 0o03537, '', '', 'UNIT/R/', kind='operand', line=1274)
W('27,3106', 0o63361, '', 'VXSC', 'PDVL', kind='interp', line=1275)
W('27,3107', 0o00037, '', '', '30D', kind='operand', line=1276)
W('27,3110', 0o03656, '', '', 'IC', kind='operand', line=1277)
W('27,3111', 0o53455, '', 'VAD', 'UNIT', kind='interp', line=1278)
W('27,3112', 0o03537, '', '', 'UNIT/R/', kind='operand', line=1279)
# Page 779
W('27,3113', 0o53361, 'GETVRVG1', 'VXSC', 'VAD', kind='interp', line=1281)
W('27,3114', 0o00041, '', '', '32D', kind='operand', line=1282)
W('27,3115', 0o53744, 'GETVRVG2', 'LXC,2', 'VSR*', kind='interp', line=1283)
W('27,3116', 0o02777, '', '', 'RTX2', kind='operand', line=1284)
W('27,3117', 0o57177, '', '', '0 -1,2', kind='operand', line=1285)
W('27,3120', 0o02337, '', 'STORE', 'VIPRIME', kind='interp', line=1286)
W('27,3121', 0o77650, '', 'GOTO', kind='interp', line=1287)
W('27,3122', 0o57166, '', '', 'ASTREND -2', kind='operand', line=1288)
W('27,3123', 0o50375, '180MESS', 'VLOAD', 'DOT', kind='interp', line=1289)
W('27,3124', 0o03656, '', '', 'IC', kind='operand', line=1290)
W('27,3125', 0o03537, '', '', 'UNIT/R/', kind='operand', line=1291)
W('27,3126', 0o77240, '', 'BMN', 'VLOAD', kind='interp', line=1292)
W('27,3127', 0o57146, '', '', 'NEGPROD', kind='operand', line=1293)
W('27,3130', 0o03656, '', '', 'IC', kind='operand', line=1294)
W('27,3131', 0o63362, '', 'VSR1', 'PDVL', kind='interp', line=1295)
W('27,3132', 0o03537, '', '', 'UNIT/R/', kind='operand', line=1296)
W('27,3133', 0o53362, '', 'VSR1', 'VAD', kind='interp', line=1297)
W('27,3134', 0o77656, '', 'UNIT', kind='interp', line=1298)
W('27,3135', 0o57406, '', 'PUSH', 'VCOMP', 'FOR A', kind='interp', line=1299)
W('27,3136', 0o75235, '', 'VXV', 'SIGN', kind='interp', line=1300)
W('27,3137', 0o02674, '', '', 'UN', kind='operand', line=1301)
W('27,3140', 0o02673, '', '', 'GEOMSGN', kind='operand', line=1302)
W('27,3141', 0o74256, '', 'UNIT', 'VXSC', kind='interp', line=1303)
W('27,3142', 0o00037, '', '', '30D', kind='operand', line=1304)
W('27,3143', 0o77715, '', 'PDVL', '', 'UNIT(IC-IR)   +-B', kind='interp', line=1305)
W('27,3144', 0o77650, '', 'GOTO', kind='interp', line=1306)
W('27,3145', 0o57113, '', '', 'GETVRVG1', kind='operand', line=1307)
W('27,3146', 0o74575, 'NEGPROD', 'VLOAD', 'VSR1', kind='interp', line=1308)
W('27,3147', 0o03537, '', '', 'UNIT/R/', kind='operand', line=1309)
W('27,3150', 0o74515, '', 'PDVL', 'VSR1', kind='interp', line=1310)
W('27,3151', 0o03656, '', '', 'IC', kind='operand', line=1311)
W('27,3152', 0o53451, '', 'VSU', 'UNIT', kind='interp', line=1312)
W('27,3153', 0o77606, '', 'PUSH', kind='interp', line=1313)
W('27,3154', 0o75235, '', 'VXV', 'SIGN', kind='interp', line=1314)
W('27,3155', 0o02674, '', '', 'UN', 'FOR B', kind='operand', line=1315)
W('27,3156', 0o02673, '', '', 'GEOMSGN', kind='operand', line=1316)
W('27,3157', 0o74256, '', 'UNIT', 'VXSC', kind='interp', line=1317)
W('27,3160', 0o00041, '', '', '32D', kind='operand', line=1318)
W('27,3161', 0o77715, '', 'PDVL', kind='interp', line=1319)
W('27,3162', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=1320)
W('27,3163', 0o00037, '', '', '30D', kind='operand', line=1321)
W('27,3164', 0o77650, '', 'GOTO', kind='interp', line=1322)
W('27,3165', 0o57115, '', '', 'GETVRVG2', kind='operand', line=1323)
W('27,3166', 0o77651, '', 'VSU', kind='interp', line=1324)
W('27,3167', 0o03553, '', '', 'VN1', kind='operand', line=1325)
W('27,3170', 0o02366, 'ASTREND', 'STORE', 'DELVEET3', kind='interp', line=1326)
W('27,3171', 0o53135, 'FIRSTTME', 'SLOAD', 'BZE', kind='interp', line=1327)
W('27,3172', 0o03000, '', '', 'RTX2', kind='operand', line=1328)
W('27,3173', 0o57177, '', '', 'GETGOBL', kind='operand', line=1329)
W('27,3174', 0o52175, '', 'VLOAD', 'GOTO', 'NO OBLATENESS COMP IF IN MOON SPHERE', kind='interp', line=1330)
# Page 780
W('27,3175', 0o02366, '', '', 'DELVEET3', kind='operand', line=1332)
W('27,3176', 0o57212, '', '', 'NOGOBL', kind='operand', line=1333)
W('27,3177', 0o53575, 'GETGOBL', 'VLOAD', 'UNIT', 'CALCULATE OBLATENESS TERM.', kind='interp', line=1334)
W('27,3200', 0o01221, '', '', 'RN', kind='operand', line=1335)
W('27,3201', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=1336)
W('27,3202', 0o01235, '', '', 'PIPTIME', '             2', kind='operand', line=1337)
W('27,3203', 0o03512, '', '', 'GOBLTIME', 'G    = -(MU/R )(UNITGOBL)(T-TIG)', kind='operand', line=1338)
W('27,3204', 0o56205, '', 'DMP', 'DDV', ' OBL', kind='interp', line=1339)
W('27,3205', 0o16023, '', '', 'EARTHMU', kind='operand', line=1340)
W('27,3206', 0o00043, '', '', '34D', '34D = /RN/ (2) FROM UNIT OPERATION.', kind='operand', line=1341)
W('27,3207', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=1342)
W('27,3210', 0o03521, '', '', 'UNITGOBL', kind='operand', line=1343)
W('27,3211', 0o02366, '', '', 'DELVEET3', 'OUTPUT FROM INITVEL VG = VR - VN', kind='operand', line=1344)
W('27,3212', 0o02366, 'NOGOBL', 'STORE', 'DELVEET3', 'VG = VR + GOBL - VN', kind='interp', line=1345)
W('27,3213', 0o77650, '', 'GOTO', kind='interp', line=1346)
W('27,3214', 0o56455, '', '', 'VGAIN*', kind='operand', line=1347)

W('27,3215', 0o31103, '2PI+3', '2DEC', '3.141592653 B-2', kind='data', line=1349)
W('27,3216', 0o36652, kind='data', line=1349)

# Page 781
# TRIMGIMB      (FORMERLY S40.6)
# MOD 0         24 FEB 67       PETER ADLER
#
# FUNCTION:
# TRIMS DPS ENGINE TO MINIMIZE THRUST/CG OFFSET.  ENGINE IS GIMBALLED TO FULL + PITCH AND + ROLL (TO LOCK)
# FOR REFERENCE AND IS THEN BROUGHT BACK TO TRIM POSITION BY RUNNING FOR THE PROPER TIMES (TO BE
# SPECIFIED BY GAEC) IN - PITCH AND - ROLL.
#
# CALLING SEQUENCE:
# VIA WAITLIST FROM R03
#
# INPUT:
# PITTIME         TIME TO RUN FROM FULL + PITCH TO TRIM (CS)
# ROLLTIME        TIME TO RUN FROM FULL + ROLL TO TRIM (CS)
#
# SUBROUTINES USED:
# WAITLIST, FIXDELAY, VARDELAY, FLAGUP, FLAGDOWN, NOVAC

#   COUNT* $$/S40.6
#   EBANK= ROLLTIME  # OCTAL MASKS: PRIO5=05000 EBANK5=02400

W('27,3217', 0o05516, 'TRIMGIMB', 'TC', 'DOWNFLAG', 'GMBDRVSW FLAG IS SET WHEN EITHER ROLL OR', line=1373)
W('27,3220', 0o00137, '', 'ADRES', 'GMBDRVSW', 'PITCH IS COMPLETED, WHICHEVER IS FIRST.', kind='data', line=1374)

W('27,3221', 0o45017, '', 'CS', 'PRIO5', 'TURN OFF - PITCH, - ROLL, IF ON.', line=1376)
W('27,3222', 0o00006, '', 'EXTEND', line=1377)
W('27,3223', 0o03012, '', 'WAND', 'CHAN12', line=1378)
W('27,3224', 0o35014, '', 'CAF', 'EBANK5', 'TURN ON + PITCH, + ROLL.', line=1379)
W('27,3225', 0o00006, '', 'EXTEND', line=1380)
W('27,3226', 0o05012, '', 'WOR', 'CHAN12', line=1381)
W('27,3227', 0o05221, '', 'TC', 'FIXDELAY', 'WAIT ONE MINUTE TO MAKE SURE ENGINE IS', line=1382)
W('27,3230', 0o13560, '', 'DEC', '6000', 'AT FULL + PITCH AND FULL + ROLL', kind='data', line=1383)
W('27,3231', 0o45014, '', 'CS', 'EBANK5', 'TURN OFF + PITCH, + ROLL.', line=1384)
W('27,3232', 0o00006, '', 'EXTEND', line=1385)
W('27,3233', 0o03012, '', 'WAND', 'CHAN12', line=1386)
W('27,3234', 0o35017, '', 'CAF', 'PRIO5', 'TURN ON - PITCH, - ROLL.', line=1387)
W('27,3235', 0o00006, '', 'EXTEND', line=1388)
W('27,3236', 0o05012, '', 'WOR', 'CHAN12', line=1389)
W('27,3237', 0o31402, '', 'CAE', 'PITTIME', 'GET TIME TO SHUT OFF - PITCH AND SET UP', line=1390)
W('27,3240', 0o05173, '', 'TC', 'TWIDDLE', 'TWIDDLE-TASK TO TURN IT OFF THEN', line=1391)
W('27,3241', 0o03260, '', 'ADRES', 'PITCHOFF', kind='data', line=1392)

W('27,3242', 0o31401, '', 'CAE', 'ROLLTIME', 'GET TIME TO SHUT OFF - ROLL AND GO AWAY', line=1394)
W('27,3243', 0o05224, '', 'TC', 'VARDELAY', 'UNTIL THEN', line=1395)
W('27,3244', 0o44740, '', 'CS', 'BIT12', line=1396)
W('27,3245', 0o00006, '', 'EXTEND', line=1397)
W('27,3246', 0o03012, '', 'WAND', 'CHAN12', 'SHUT OFF ROLL', line=1398)
W('27,3247', 0o30102, 'ROLLOVER', 'CA', 'FLAGWRD6', 'IF HERE INLINE (ROLL DONE) IS PITCH DONE', line=1399)
W('27,3250', 0o74742, '', 'MASK', 'GMBDRBIT', 'IF HERE FROM PITCHOFF, IS ROLL DONE?', line=1400)
W('27,3251', 0o00006, '', 'EXTEND', line=1401)
W('27,3252', 0o13264, '', 'BZF', 'PITCHOFF +4', 'NO.  SET FLAG, ROLL OR PITCH DONE.', line=1402)
W('27,3253', 0o34737, '', 'CAF', 'PRIO10', 'RETURN TO R03.', line=1403)
W('27,3254', 0o05072, '', 'TC', 'NOVAC', line=1404)
#   EBANK= WHOCARES
# Page 782
W('27,3255', 0o02323, '', '2CADR', 'TRIMDONE', kind='data', line=1407)
W('27,3256', 0o02067, kind='data', line=1407)

W('27,3257', 0o05261, '', 'TC', 'TASKOVER', line=1409)
W('27,3260', 0o44742, 'PITCHOFF', 'CS', 'BIT10', line=1410)
W('27,3261', 0o00006, '', 'EXTEND', line=1411)
W('27,3262', 0o03012, '', 'WAND', 'CHAN12', 'SHUT OFF PITCH', line=1412)
W('27,3263', 0o13247, '', 'TCF', 'ROLLOVER', 'SEE IF ROLL HAS FINISHED ALSO.', line=1413)
W('27,3264', 0o05504, '', 'TC', 'UPFLAG', 'ROLL DONE; OR PITCH DONE; BUT NOT BOTH.', line=1414)
W('27,3265', 0o00137, '', 'ADRES', 'GMBDRVSW', kind='data', line=1415)
W('27,3266', 0o05261, '', 'TC', 'TASKOVER', line=1416)

# Page 783
# SUBROUTINE NAME:  S41.1       MOD. NO. 0      DATE: FEBRUARY 28, 1967
# MOD. NO. 1    DATE: JANUARY 23, 1968, BY PETER ADLER (MIT/IL)
#
# AUTHOR: JONATHON D. ADDLESTON (ADAMS ASSOCIATES)
#
# S41.1 PERFORMS THE COORDINATE SYSTEM TRANSFORMATION FROM THE REFERENCE FRAME TO THE BODY OF THE LM.
# SPECIFICALLY, IT IS USED TO TRANSFORM A VELOCITY (SCALED AT 2(+7) METERS/CENTISECOND) FROM REFERENCE TO LM AXIS
# COORDINATES.  FIRST THE VECTOR IS TRANSFORMED TO THE STABLE MEMBER COORDINATES BY THE MATRIX REFSMMAT.  THIS
# LEAVES THE VECTOR IN MPAC, SCALED AT 2(+8) METERS/CENTISECOND.  THEN
# THE SUBROUTINE CDUTRIG IS CALLED TO SET UP THE DOUBLE-PRECISION CDU VECTOR ALONG WITH ITS SINES AND COSINES.
# THE VECTOR IS THEN TRANSFORMED FROM STABLE MEMBER COORDINATES TO SPACECRAFT (OR LM) COORDINATES BY THE
# SUBROUTINE *SMNB*.  FINALLY, THE VECTOR IS RESCALED TO 2(+7) METERS/CENTISECOND, AND CONTROL IS RETURNED BO THE
# CALLER WITH C(MPAC) = VELOCITY(LM).
#
# CALLING SEQUENCE:
# L       VLOAD   CALL
# L +1            VELOCITY(REF)           # SCALED AT 2(+7) M/CS IN REFERENCE COORDS.
# L +2            S41.1
# L +3    STORE   VELOCITY(LM)            # SCALED AT 2(+7) M/CS IN LM BODY AXIS SYS.
#
# SUBROUTINES CALLED:
# 1.      CDUTRIG,
# WHICH CALLS CDULOGIC.
# 2.      *SMNB*
#
# NORMAL RETURN:  L +3 (SEE CALLING SEQUENCE, ABOVE.)
#
# ALARM/ABORT MODES:  NONE.
#
# RESTART PROTECTION:  NONE.
#
# Page 784
# INPUT:
# 1.      REFSMMAT.
# 2.      CDUX, CDUY, CDUZ.
# 3.      VELOCITY (REF) IN MPAC.
#
# OUTPUT:
# 1.      CSUSPOT:        DOUBLE PRECISION CDU VECTOR, ORDERED Y,Z,X.
# 2.      SINCDU:         HALF SINES OF CDUSPOT COMPONENTS
# 3.      COSCDU:         HALF COSINES OF CDUSPOT COMPONENTS.
# 4.      MPAC:           VELOCITY(LM) (SCALED AT 2(+7) METERS/CENTISECOND)
#
# DEBRIS:  NONE.
#
# CHECKOUT STATUS:  CODED

#   COUNT* $$/S41.1
W('27,3267', 0o76521, 'S41.1', 'MXV', 'VSL1', 'CONVERT VECTOR IN MPAC FROM REF AT 2(+7)', kind='interp', line=1467)
W('27,3270', 0o01734, '', '', 'REFSMMAT', 'TO SM AND RESCALE DUE TO HALF-UNIT MATRIX', kind='operand', line=1468)
W('27,3271', 0o77650, '', 'GOTO', '', 'CONVERT TO BODY AT 2(+7) USING PRESENT', kind='interp', line=1469)
W('27,3272', 0o47646, '', '', 'CDU*SMNB', 'CDU ANGLES.  CDU*SMNB WILL RETURN', kind='operand', line=1470)
# VIA RVQ TO THE CALLER OF S41.1.
