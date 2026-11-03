"""FINDCDUW--GUIDAP_INTERFACE.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/FINDCDUW--GUIDAP_INTERFACE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 908-925 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('FINDCDUW__GUIDAP_INTERFACE', 'FINDCDUW--GUIDAP_INTERFACE.agc', 'Luminary099', pages='908-925')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     FINDCDUW--GUIDAP_INTERFACE.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        908-925
# Mod history:  2009-05-28 HG   Transcribed from page images.
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

# Page 908
# PROGRAM NAME:  FINDCDUW
# MOD NUMBER:  1        68-07-15
# MOD AUTHOR:  KLUMPP
#
# OBJECTS OF MOD:       1.      TO SUPPLY COMMANDED GIMBAL ANGLES FOR NOUN 22.
# 2.      TO MAINTAIN CORRECT AND CURRENT THRUST
# DIRECTION DATA IN ALL MODES.  THIS IS DONE BY
# FETCHING FOR THE THRUST DIRECTION FILTER THE
# CDUD'S IN PNGCS-AUTO, THE CDU'S IN ALL OTHER
# MODES.
# 3.      TO SUBSTITUDE A STOPRATE FOR THE NORMAL
# AUTOPILOT COMMANDS WHENEVER
# 1) NOT IN PNGCS-AUTO, OR
# 2) ENGINE IS OFF.
#
# FUNCTIONAL DESCRIPTION:
#
# FINDCDUW PROVIDES THE INTERFACES BETWEEN THE VARIOUS POWERED FLITE GUIDANCE PROGRAMS
# AND THE DIGITAL AUTOPILOT.  THE INPUTS TO FINDCDUW ARE THE THRUST COMMAND VECTOR
# AND THE WINDOW COMMAND VECTOR, AND THE OUTPUTS ARE THE GIMBAL ANGLE
# INCREMENTS, THE COMMANDED ATTITUDE ANGLE RATES, AND THE COMMANDED
# ATTITUDE LAG ANGLES (WHICH ACCOUNT FOR THE ANGLES BY WHICH THE BODY WILL
# LAG BEHIND A RAMP COMMAND IN ATTITUDE ANGLE DUE TO THE FINITE ANGULAR
# ACCELERATIONS AVAILABLE).
#
# FINDCDUW ALIGNS THE ESTIMATED THRUST VECTOR FROM THE THRUST DIRECTION
# FILTER WITH THE THRUST COMMAND VECTOR, AND, WHEN XDVINHIB SET,
# ALIGNS THE +Z HALF OF THE LM ZX PLANE WITH THE WINDOW COMMAND VECTOR.
#
# Page 909
# SPECIFICATIONS:
#
# INITIALIZATION:       A SINGLE INTERPRETIVE CALL TO INITCDUW IS REQUIRED
# BEFORE EACH GUIDED MANEUVER USING FINDCDUW.
#
# CALL:                 INTERPRETIVE CALL TO FINDCDUW WITH THE THRUST COMMAND
# VECTOR IN MPAC.  INTERPRETIVE CALL TO FINDCDUW -2 WITH
# THE THRUST COMMAND VECTOR IN UNFC/2 AND NOT IN MPAC.
#
# RETURNS:              NORMAL INTERPRETIVE IN ALL CASES
# 1.      NORMALLY ALL AUTOPILOT CMDS ARE ISSUED.
# 2.      IF NOT PNGCS AUTO, DO STOPRATE AND RETURN
# WITHOUT ISSUING AUTOPILOT CMDS.
# 3.      IF ENGINE OFF, DO STOPRATE AND RETURN WITHOUT
# ISSUING AUTOPILOT CMDS.
#
# ALARMS:               00401   IF INPUTS DETERMINE AN ATTITUDE IN GIMBAL LOCK.
# FINDCDUW DRIVES CDUXD AND CDUYD TO THE RQD VALUES,
# BUT DRIVES CDUZD ONLY TO THE GIMBAL LOCK CONE.
#
# 00402   IF UNFC/2 OR UNWC/2 PRODUCE OVERFLOW WHEN
# UNITIZED USING NORMUNIT.  FINDCDUW ISSUES
# STOPRATE AS ONLY INPUT TO AUTOPILOT.
#
# INPUTS:               UNFC/2          THRUST COMMAND VECTOR, NEED NOT BE SEMI-UNIT.
# UNWC/2          WINDOW COMMAND VECTOR, NEED NOT BE SEMI-UNIT.
# OGABIAS         POSSIBLE BIAS FOR OUTER GIMBAL ANGLE (ZEROED IN INITCDUW), UNITS OF PI.
# XOVINHIB        FLAG DENOTING X AXIS OVERRIDE INHIBITED.
# CSMDOCKD        FLAG DENOTING CSM DOCKED.
# STEERSW         FLAG DENOTING INSUFF THRUST FOR THRUST DIR FLTR.
#
# OUTPUTS:              DELCDUX,Y,Z
# OMEGAPD,+1,+2
# DELPEROR,+1,+2
# CPHI,+1,+2 FOR NOUN22
#
# DEBRIS:               FINDCDUW DESTROYS SINCDUX,Y,Z AND COSCDUX,Y,Z BY
# WRITING INTO THESE LOCATIONS THE SINES AND COSINES
# OF THE CDUD'S IN PNGCS-AUTO, OF THE CDU'S OTHERWISE.

# Page 910
# INITIALIZATION FOR FINDCDUW

#   BANK 30
#   SETLOC FCDUW
#   BANK

#   EBANK= ECDUW
#   COUNT* $$/FCDUW

W('30,3104', 0o77775, 'INITCDUW', 'VLOAD', kind='interp', line=108)
W('30,3105', 0o06520, '', '', 'UNITX', kind='operand', line=109)
W('30,3106', 0o03270, '', 'STORE', 'UNFV/2', kind='interp', line=110)
W('30,3107', 0o03262, '', 'STORE', 'UNWC/2', kind='interp', line=111)
W('30,3110', 0o77616, '', 'RVQ', kind='interp', line=112)

# FINDCDUW PRELIMINARIES

W('30,3111', 0o77775, '', 'VLOAD', '', 'FINDCDUW -2:  ENTRY WHEN UNFC/2 PRE-STORD', kind='interp', line=116)
W('30,3112', 0o03254, '', '', 'UNFC/2', 'INPUT VECTORS NEED NOT BE SEMI-UNIT', kind='operand', line=117)
W('30,3113', 0o40200, 'FINDCDUW', 'BOV', 'SETPD', 'FINDCDUW: ENTRY WHEN UNFC/2 IN MPAC', kind='interp', line=118)
W('30,3114', 0o61113, '', '', 'FINDCDUW', 'INTERPRETER NOW INITIALIZED', kind='operand', line=119)
W('30,3115', 0o00023, '', '', '22', 'LOCS 0 THRU 21 FOR DIRECTION COSINE MAT', kind='operand', line=120)
W('30,3116', 0o77420, '', 'STQ', 'EXIT', kind='interp', line=121)
W('30,3117', 0o03247, '', '', 'QCDUWUSR', 'SAVE RETURN ADDRESS', kind='operand', line=122)

# MORE HAUSKEEPING
W('30,3120', 0o33761, '', 'CA', 'ECDUWL', line=125)
W('30,3121', 0o56003, '', 'XCH', 'EBANK', 'SET EBANK', line=126)
W('30,3122', 0o55646, '', 'TS', 'ECDUWUSR', "SAVE USER'S EBANK", line=127)

W('30,3123', 0o30111, '', 'CA', 'DAPBOOLS', line=129)
W('30,3124', 0o74737, '', 'MASK', 'CSMDOCKD', 'CSMDOCKD MUST NOT BE BIT15', line=130)
W('30,3125', 0o10000, '', 'CCS', 'A', line=131)
W('30,3126', 0o34753, '', 'CA', 'ONE', 'INDEX IF CSM DOCKED', line=132)
W('30,3127', 0o55650, '', 'TS', 'NDXCDUW', line=133)

W('30,3130', 0o34743, '', 'CA', 'XOVINHIB', 'XOVINHIB MUST NOT BE BIT15', line=135)
W('30,3131', 0o55652, '', 'TS', 'FLPAUTNO', 'SET TO POS-NON-ZERO FLAG PNGCS AUTO NOT', line=136)

W('30,3132', 0o70111, '', 'MASK', 'DAPBOOLS', line=138)
W('30,3133', 0o55651, '', 'TS', 'FLAGOODW', 'FLAG0ODW = ANY PNZ NUMBER IF XOV INHIBTD', line=139)

# Page 911
# FETCH BASIC DATA
W('30,3134', 0o00004, '', 'INHINT', '', 'RELINT AT PAUTNO (TC INTPRET)', line=143)

W('30,3135', 0o30032, '', 'CA', 'CDUX', 'FETCH CDUX,CDUY,CDUZ IN ALL CASES, BUT', line=145)
W('30,3136', 0o54772, '', 'TS', 'CDUSPOTX', '      REPLACE BELOW IF PNGCS AUTO', line=146)
W('30,3137', 0o30033, '', 'CA', 'CDUY', line=147)
W('30,3140', 0o54766, '', 'TS', 'CDUSPOTY', line=148)
W('30,3141', 0o30034, '', 'CA', 'CDUZ', line=149)
W('30,3142', 0o54770, '', 'TS', 'CDUSPOTZ', line=150)

W('30,3143', 0o34742, '', 'CA', 'BIT10', 'PNGCS CONTROL BIT', line=152)
W('30,3144', 0o00006, '', 'EXTEND', line=153)
W('30,3145', 0o02030, '', 'RAND', 'CHAN30', line=154)
W('30,3146', 0o10000, '', 'CCS', 'A', line=155)
W('30,3147', 0o13164, '', 'TCF', 'PAUTNO', 'NOT PNGCS (BITS INVERTED)', line=156)

W('30,3150', 0o34736, '', 'CA', 'BIT14', 'AUTO MODE BIT', line=158)
W('30,3151', 0o00006, '', 'EXTEND', line=159)
W('30,3152', 0o02031, '', 'RAND', 'CHAN31', line=160)
W('30,3153', 0o10000, '', 'CCS', 'A', line=161)
W('30,3154', 0o13164, '', 'TCF', 'PAUTNO', 'NOT AUTO (BITS INVERTED)', line=162)

W('30,3155', 0o55652, '', 'TS', 'FLPAUTNO', 'RESET FLAG PNGCS AUTO NOT', line=164)

W('30,3156', 0o31635, '', 'CA', 'CDUXD', 'PNGCS AUTO:  FETCH CDUXD,CDUYD,CDUZD', line=166)
W('30,3157', 0o54772, '', 'TS', 'CDUSPOTX', line=167)
W('30,3160', 0o31636, '', 'CA', 'CDUYD', line=168)
W('30,3161', 0o54766, '', 'TS', 'CDUSPOTY', line=169)
W('30,3162', 0o31637, '', 'CA', 'CDUZD', line=170)
W('30,3163', 0o54770, '', 'TS', 'CDUSPOTZ', line=171)

# Page 912
# FETCH INPUTS
W('30,3164', 0o06037, 'PAUTNO', 'TC', 'INTPRET', 'ENTERING THRUST CMD STILL IN MPAC', line=175)
W('30,3165', 0o77634, '', 'RTB', kind='interp', line=176)
W('30,3166', 0o21726, '', '', 'NORMUNIT', kind='operand', line=177)
W('30,3167', 0o24001, '', 'STOVL', 'UNX/2', 'SEMI-UNIT THRUST CMD AS INITIAL UNX/2', kind='interp', line=178)
W('30,3170', 0o03262, '', '', 'UNWC/2', kind='operand', line=179)
W('30,3171', 0o47034, '', 'RTB', 'RTB', kind='interp', line=180)
W('30,3172', 0o21726, '', '', 'NORMUNIT', kind='operand', line=181)
W('30,3173', 0o47615, '', '', 'QUICTRIG', "ALWAYS RQD TO OBTAIN TRIGS OF CDUD'S", kind='operand', line=182)
W('30,3174', 0o24015, '', 'STOVL', 'UNZ/2', 'SEMI-UNIT WINDOW CMD AS INITIAL UNZ/2', kind='interp', line=183)
W('30,3175', 0o00325, '', '', 'DELV', kind='operand', line=184)
W('30,3176', 0o53404, '', 'BOVB', 'UNIT', kind='interp', line=185)
W('30,3177', 0o61750, '', '', 'NOATTCNT', 'AT LEAST ONE ENTERING CMD VCT ZERO', kind='operand', line=186)
W('30,3200', 0o45000, '', 'BOV', 'CALL', kind='interp', line=187)
W('30,3201', 0o61215, '', '', 'AFTRFLTR', 'IF UNIT DELV OVERFLOWS SKIP FILTER', kind='operand', line=188)
W('30,3202', 0o47671, '', '', '*SMNB*', 'YIELDS UNIT(DELV) IN VEH COORDS FOR FLTR', kind='operand', line=189)

# THRUST DIRECTION FILTER

W('30,3203', 0o77776, '', 'EXIT', kind='interp', line=193)

W('30,3204', 0o31671, '', 'CA', 'UNFVY/2', 'FOR RESTARTS, UNFV/2 ALWAYS INTACT, MPAC', line=195)
W('30,3205', 0o22157, '', 'LXCH', 'MPAC +3', '      RENEWD AFTER RETURN FROM CALLER,', line=196)
W('30,3206', 0o03503, '', 'TC', 'FLTRSUB', '      TWO FILTER UPDATES MAY BE DONE.', line=197)
W('30,3207', 0o55671, '', 'TS', 'UNFVY/2', 'UNFV/2 NEED NOT BE EXACTLY SEMI-UNIT.', line=198)

W('30,3210', 0o31673, '', 'CA', 'UNFVZ/2', line=200)
W('30,3211', 0o22161, '', 'LXCH', 'MPAC +5', line=201)
W('30,3212', 0o03503, '', 'TC', 'FLTRSUB', line=202)
W('30,3213', 0o55673, '', 'TS', 'UNFVZ/2', line=203)

W('30,3214', 0o06037, '', 'TC', 'INTPRET', 'COMPLETES FILTER', line=205)

# Page 913
# FIND A SUITABLE WINDOW POINTING VECTOR

W('30,3215', 0o46135, 'AFTRFLTR', 'SLOAD', 'BHIZ', 'IF XOV NOT INHIBITED, GO FETCH ZNB', kind='interp', line=210)
W('30,3216', 0o03252, '', '', 'FLAGOODW', kind='operand', line=211)
W('30,3217', 0o61223, '', '', 'FETCHZNB', kind='operand', line=212)
W('30,3220', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=213)
W('30,3221', 0o00015, '', '', 'UNZ/2', kind='operand', line=214)
W('30,3222', 0o61523, '', '', 'UNWCTEST', kind='operand', line=215)

W('30,3223', 0o77775, 'FETCHZNB', 'VLOAD', kind='interp', line=217)
W('30,3224', 0o02162, '', '', 'ZNBPIP', kind='operand', line=218)
W('30,3225', 0o34015, '', 'STCALL', 'UNZ/2', kind='interp', line=219)
W('30,3226', 0o61523, '', '', 'UNWCTEST', kind='operand', line=220)

W('30,3227', 0o57575, '', 'VLOAD', 'VCOMP', "Z AND -X CAN'T BOTH PARALLEL UNFC/2", kind='interp', line=222)
W('30,3230', 0o02146, '', '', 'XNBPIP', kind='operand', line=223)
W('30,3231', 0o00015, '', 'STORE', 'UNZ/2', kind='interp', line=224)

# COMPUTE THE REQUIRED DIRECTION COSINE MATRIX

W('30,3232', 0o47375, 'DCMCL', 'VLOAD', 'VXV', kind='interp', line=228)
W('30,3233', 0o00015, '', '', 'UNZ/2', kind='operand', line=229)
W('30,3234', 0o00001, '', '', 'UNX/2', kind='operand', line=230)
W('30,3235', 0o41456, '', 'UNIT', 'PUSH', 'UNY/2 FIRST ITERATION', kind='interp', line=231)
W('30,3236', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=232)
W('30,3237', 0o00001, '', '', 'UNX/2', kind='operand', line=233)
W('30,3240', 0o00015, '', 'STORE', 'UNZ/2', '-UNZ/2 FIRST ITERATION', kind='interp', line=234)
W('30,3241', 0o63361, '', 'VXSC', 'PDVL', 'EXCHANGE -UNFVZ/2 UNZ/2 FOR UNY/2', kind='interp', line=235)
W('30,3242', 0o03274, '', '', 'UNFVZ/2', 'MUST BE SMALL', kind='operand', line=236)
W('30,3243', 0o51361, '', 'VXSC', 'BVSU', 'YIELDS -UNFVY/2 UNY/2-UNFVZ/2 UNZ/2', kind='interp', line=237)
W('30,3244', 0o03272, '', '', 'UNFVY/2', 'MUST BE SMALL', kind='operand', line=238)
W('30,3245', 0o53372, '', 'VSL1', 'VAD', kind='interp', line=239)
W('30,3246', 0o00001, '', '', 'UNX/2', kind='operand', line=240)
W('30,3247', 0o77656, '', 'UNIT', '', 'TOTALLY ELIMINATES THRUST POINTING ERROR', kind='interp', line=241)
W('30,3250', 0o00001, '', 'STORE', 'UNX/2', 'UNX/2', kind='interp', line=242)
W('30,3251', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=243)
W('30,3252', 0o00015, '', '', 'UNZ/2', '-UNZ/2 WAS STORED HERE REMEMBER', kind='operand', line=244)
W('30,3253', 0o00007, '', 'STORE', 'UNY/2', 'UNY/2', kind='interp', line=245)
W('30,3254', 0o47276, '', 'VCOMP', 'VXV', kind='interp', line=246)
W('30,3255', 0o00001, '', '', 'UNX/2', kind='operand', line=247)
W('30,3256', 0o77772, '', 'VSL1', kind='interp', line=248)
W('30,3257', 0o00015, '', 'STORE', 'UNZ/2', 'UNZ/2', kind='interp', line=249)

# Page 914
# COMPUTES THE REQUIRED GIMBAL ANGLES

W('30,3260', 0o77624, '', 'CALL', kind='interp', line=254)
W('30,3261', 0o61533, '', '', 'NB2CDUSP', "YIELDS THE RQD GIMBAL ANGLES, 2'S, PI", kind='operand', line=255)
W('30,3262', 0o77776, '', 'EXIT', kind='interp', line=256)

# LIMIT THE MIDDLE GIMBAL ANGLE & COMPUTE THE UNLIMITED GIMBAL ANGLE CHGS

W('30,3263', 0o30156, '', 'CA', 'MPAC +2', 'LIMIT THE MGA', line=260)
W('30,3264', 0o54001, '', 'TS', 'L', "CAN'T LXCH:  NEED UNLIMITED MGA FOR ALARM", line=261)
W('30,3265', 0o33773, '', 'CA', 'CDUZDLIM', line=262)
W('30,3266', 0o03727, '', 'TC', 'LIMITSUB', 'YIELDS LIMITED MGA.  1 BIT ERROR POSSIBLE', line=263)
W('30,3267', 0o56156, '', 'XCH', 'MPAC +2', "      BECAUSE USING 2'S COMP.  WHO CARES?", line=264)
W('30,3270', 0o00006, '', 'EXTEND', line=265)
W('30,3271', 0o20156, '', 'MSU', 'MPAC +2', 'THIS BETTER YIELD ZERO', line=266)
W('30,3272', 0o00006, '', 'EXTEND', line=267)
W('30,3273', 0o13275, '', 'BZF', '+2', line=268)
W('30,3274', 0o13756, '', 'TCF', 'ALARMMGA', line=269)

W('30,3275', 0o00004, 'MGARET', 'INHINT', '', 'RELINT AT TC INTPRET AFTER TCQCDUW', line=271)

W('30,3276', 0o22007, '', 'ZL', line=273)
W('30,3277', 0o34752, '', 'CA', 'TWO', line=274)
W('30,3300', 0o54142, 'DELGMBLP', 'TS', 'TEM2', line=275)

W('30,3301', 0o30001, '', 'CA', 'L', 'TO PREVENT FALSE STARTS ABOUT X, ZERO', line=277)
W('30,3302', 0o00006, '', 'EXTEND', '', '      FLAGOODW IF DELGMBZ OR Y TOO BIG.', line=278)
W('30,3303', 0o70000, '', 'SQUARE', line=279)
W('30,3304', 0o64350, '', 'AD', 'HI5', 'WITHIN 1 BIT OF -(45 DEG SQUARED)', line=280)
W('30,3305', 0o00006, '', 'EXTEND', line=281)
W('30,3306', 0o63311, '', 'BZMF', '+3', line=282)
W('30,3307', 0o34755, '', 'CA', 'ZERO', line=283)
W('30,3310', 0o55651, '', 'TS', 'FLAGOODW', line=284)

W('30,3311', 0o50142, '', 'INDEX', 'TEM2', line=286)
W('30,3312', 0o30154, '', 'CA', 'MPAC', line=287)
W('30,3313', 0o50142, '', 'INDEX', 'TEM2', line=288)
W('30,3314', 0o54321, '', 'TS', 'CPHI', 'OUTPUTS TO NOUN22', line=289)
W('30,3315', 0o00006, '', 'EXTEND', line=290)
W('30,3316', 0o50142, '', 'INDEX', 'TEM2', line=291)
W('30,3317', 0o21635, '', 'MSU', 'CDUXD', 'NO MATTER THAT THESE SLIGHTLY DIFFERENT', line=292)
W('30,3320', 0o40000, '', 'COM', '', 'FROM WHEN WE INITIALLY FETCHED THEM', line=293)
W('30,3321', 0o50142, '', 'INDEX', 'TEM2', line=294)
W('30,3322', 0o55675, '', 'TS', '-DELGMB', "-UNLIMITED GIMBAL ANGLE CHGS, 1'S, PI", line=295)
W('30,3323', 0o54001, '', 'TS', 'L', 'FOR PRECEDING TEST ON NEXT LOOP PASS', line=296)
W('30,3324', 0o10142, '', 'CCS', 'TEM2', line=297)
W('30,3325', 0o13300, '', 'TCF', 'DELGMBLP', line=298)

# Page 915
# BRANCHES TO NOATTCNT
W('30,3326', 0o11652, '', 'CCS', 'FLPAUTNO', line=302)
W('30,3327', 0o13752, '', 'TCF', 'NOATTCNT +2', 'NO PNGCS AUTO', line=303)

W('30,3330', 0o30101, '', 'CA', 'FLAGWRD5', line=305)
W('30,3331', 0o74745, '', 'MASK', 'ENGONBIT', line=306)
W('30,3332', 0o00006, '', 'EXTEND', line=307)
W('30,3333', 0o13752, '', 'BZF', 'NOATTCNT +2', 'ENGINE NOT ON', line=308)

# Page 916
# LIMIT THE ATTITUDE ANGLE CHANGES
#
# THIS SECTION LIMITS THE ATTITUDE ANGLE CHANGES ABOUT A SET OF ORTHOGONAL VEHICLE AXES X,YPRIME,ZPRIME,
# THESE AXES COINCIDE WITH THE COMMANDED VEHICLE AXES IF AND ONLY IF CDUXD IS ZERO.  THE PRIME SYSTEM IS
# THE COMMANDED VEHICLE SYSTEM ROTATED ABOUT THE X AXIS TO BRING THE Z AXIS INTO ALIGNMENT WITH THE MIDDLE GIMBAL
# AXIS.  ATTITUDE ANGLE CHANGES IN THE PRIME SYSTEM ARE RELATED TO SMALL GIMBAL ANGLE CHANGES BY:
#
# [   -DELATTX    ]   [ 1     SIN(CDUZD)     0 ] [ -DELGMBX ]
# [               ]   [                        ] [          ]
# [ -DELATTYPRIME ] = [ 0     COS(CDUZD)     0 ] [ -DELGMBY ]
# [               ]   [                        ] [          ]
# [ -DELATTZPRIME ]   [ 0         0          1 ] [ -DELGMBZ ]

W('30,3334', 0o23677, '', 'LXCH', '-DELGMB +2', 'SAME AS -DELATTZPRIME UNLIMITED', line=324)
W('30,3335', 0o51650, '', 'INDEX', 'NDXCDUW', line=325)
W('30,3336', 0o33767, '', 'CA', 'DAZMAX', line=326)
W('30,3337', 0o03727, '', 'TC', 'LIMITSUB', line=327)
W('30,3340', 0o55677, '', 'TS', '-DELGMB +2', '-DELGMBZ', line=328)

W('30,3341', 0o31676, '', 'CA', '-DELGMB +1', line=330)
W('30,3342', 0o00006, '', 'EXTEND', line=331)
W('30,3343', 0o70746, '', 'MP', 'COSCDUZ', 'YIELDS -DELATTYPRIME/2 UNLIMITED', line=332)
W('30,3344', 0o54001, '', 'TS', 'L', line=333)
W('30,3345', 0o51650, '', 'INDEX', 'NDXCDUW', line=334)
W('30,3346', 0o33771, '', 'CA', 'DAY/2MAX', line=335)
W('30,3347', 0o03727, '', 'TC', 'LIMITSUB', line=336)
W('30,3350', 0o00006, '', 'EXTEND', line=337)
W('30,3351', 0o10746, '', 'DV', 'COSCDUZ', line=338)
W('30,3352', 0o57676, '', 'XCH', '-DELGMB +1', '-DELGMBY, FETCHING UNLIMITED VALUE', line=339)

W('30,3353', 0o00006, '', 'EXTEND', line=341)
W('30,3354', 0o70740, '', 'MP', 'SINCDUZ', line=342)
W('30,3355', 0o20001, '', 'DDOUBL', line=343)
W('30,3356', 0o40000, '', 'COM', line=344)
W('30,3357', 0o00006, '', 'EXTEND', '', 'YIELDS +DELATTX UNLIMITD, MAG < 180 DEG.', line=345)
W('30,3360', 0o21675, '', 'MSU', '-DELGMB', '      BASED ON UNLIMITED DELGMBV.', line=346)
W('30,3361', 0o54001, '', 'TS', 'L', '      ONE BIT ERROR IF OPERANDS IN MSU', line=347)
W('30,3362', 0o51650, '', 'INDEX', 'NDXCDUW', '      OF MIXED SIGNS.  WHO CARES?', line=348)
W('30,3363', 0o33767, '', 'CA', 'DAXMAX', line=349)
W('30,3364', 0o03727, '', 'TC', 'LIMITSUB', line=350)
W('30,3365', 0o55675, '', 'TS', '-DELGMB', 'SAVE LIMITED +DELATTX', line=351)
W('30,3366', 0o11651, '', 'CCS', 'FLAGOODW', line=352)
W('30,3367', 0o41675, '', 'CS', '-DELGMB', 'FETCH IT BACK CHGING SIGN IF WINDOW GOOD', line=353)
W('30,3370', 0o55675, '', 'TS', '-DELGMB', 'OTHERWISE USE ZERO FOR -DELATTX', line=354)
W('30,3371', 0o41676, '', 'CS', '-DELGMB +1', line=355)
W('30,3372', 0o00006, '', 'EXTEND', line=356)
W('30,3373', 0o70740, '', 'MP', 'SINCDUZ', line=357)
W('30,3374', 0o20001, '', 'DDOUBL', '', 'YIELDS -CNTRIB TO -DELATTX FROM -DELGMBY', line=358)
W('30,3375', 0o27675, '', 'ADS', '-DELGMB', '-DELGMBX.  NO OVERFLOW SINCE LIMITED TO', line=359)
# 20DEG(1+SIN(70DEG)/COS(70DEG)) < 180DEG

# Page 917
# COMPUTE COMMANDED ATTITUDE RATES
#
# [ OMEGAPD ]   [ -2         -4 SINCDUZ              +0    ] [ -DELGMBZ ]
# [         ]   [                                          ] [          ]
# [ OMEGAQD ] = [ +0     -8 COSCDUZ COSCDUX     -4 SINCDUX ] [ -DELGMBY ]
# [         ]   [                                          ] [          ]
# [ OMEGARD ]   [ +0     +8 COSCDUZ SINCDUX     -4 COSCDUX ] [ -DELGMBZ ]
#
# ATTITUDE ANGLE RATES IN UNITS OF PI/4 RAD/SEC = K TRIG FCNS IN UNITS OF 2 X GIMBAL ANGLE RATES IN UNITS OF
# PI/2 RAD/SEC.  THE CONSTANTS ARE BASED ON DELGMB BEING THE GIMBAL ANGLE CHANGES IN UNITS OF PI RADIANS,
# AND 2 SECONDS BEING THE COMPUTATION PERIOD (THE PERIOD BETWEEN SUCCESSIVE PASSES THRU FINDCDUW).

W('30,3376', 0o41675, '', 'CS', '-DELGMB', line=375)
W('30,3377', 0o55643, '', 'TS', 'OMEGAPD', line=376)
W('30,3400', 0o41676, '', 'CS', '-DELGMB +1', line=377)
W('30,3401', 0o00006, '', 'EXTEND', line=378)
W('30,3402', 0o70740, '', 'MP', 'SINCDUZ', line=379)
W('30,3403', 0o20001, '', 'DDOUBL', line=380)
W('30,3404', 0o27643, '', 'ADS', 'OMEGAPD', line=381)
W('30,3405', 0o27643, '', 'ADS', 'OMEGAPD', line=382)

W('30,3406', 0o41676, '', 'CS', '-DELGMB +1', line=384)
W('30,3407', 0o00006, '', 'EXTEND', line=385)
W('30,3410', 0o70750, '', 'MP', 'COSCDUX', line=386)
W('30,3411', 0o20001, '', 'DDOUBL', line=387)
W('30,3412', 0o00006, '', 'EXTEND', line=388)
W('30,3413', 0o70746, '', 'MP', 'COSCDUZ', line=389)
W('30,3414', 0o55644, '', 'TS', 'OMEGAQD', line=390)
W('30,3415', 0o41677, '', 'CS', '-DELGMB +2', line=391)
W('30,3416', 0o00006, '', 'EXTEND', line=392)
W('30,3417', 0o70742, '', 'MP', 'SINCDUX', line=393)
W('30,3420', 0o27644, '', 'ADS', 'OMEGAQD', line=394)
W('30,3421', 0o27644, '', 'ADS', 'OMEGAQD', line=395)
W('30,3422', 0o27644, '', 'ADS', 'OMEGAQD', line=396)

W('30,3423', 0o31676, '', 'CA', '-DELGMB +1', line=398)
W('30,3424', 0o00006, '', 'EXTEND', line=399)
W('30,3425', 0o70742, '', 'MP', 'SINCDUX', line=400)
W('30,3426', 0o20001, '', 'DDOUBL', line=401)
W('30,3427', 0o00006, '', 'EXTEND', line=402)
W('30,3430', 0o70746, '', 'MP', 'COSCDUZ', line=403)
W('30,3431', 0o55645, '', 'TS', 'OMEGARD', line=404)
W('30,3432', 0o41677, '', 'CS', '-DELGMB +2', line=405)
W('30,3433', 0o00006, '', 'EXTEND', line=406)
W('30,3434', 0o70750, '', 'MP', 'COSCDUX', line=407)
W('30,3435', 0o27645, '', 'ADS', 'OMEGARD', line=408)
W('30,3436', 0o27645, '', 'ADS', 'OMEGARD', line=409)
W('30,3437', 0o27645, '', 'ADS', 'OMEGARD', line=410)

# Page 918
# FINAL TRANSFER

W('30,3440', 0o34752, '', 'CA', 'TWO', line=415)
W('30,3441', 0o54142, 'CDUWXFR', 'TS', 'TEM2', line=416)
W('30,3442', 0o50142, '', 'INDEX', 'TEM2', line=417)
W('30,3443', 0o31675, '', 'CA', '-DELGMB', line=418)
W('30,3444', 0o00006, '', 'EXTEND', line=419)
W('30,3445', 0o73774, '', 'MP', 'DT/DELT', 'RATIO OF DAP INTERVAL TO CDUW INTERVAL', line=420)
W('30,3446', 0o03743, '', 'TC', 'ONESTO2S', line=421)
W('30,3447', 0o50142, '', 'INDEX', 'TEM2', line=422)
W('30,3450', 0o55640, '', 'TS', 'DELCDUX', 'ANGLE INTERFACE', line=423)

W('30,3451', 0o50142, '', 'INDEX', 'TEM2', line=425)
W('30,3452', 0o11643, '', 'CCS', 'OMEGAPD', line=426)
W('30,3453', 0o64753, '', 'AD', 'ONE', line=427)
W('30,3454', 0o13456, '', 'TCF', '+2', line=428)
W('30,3455', 0o64753, '', 'AD', 'ONE', line=429)
W('30,3456', 0o00006, '', 'EXTEND', '', 'WE NOW HAVE ABS(OMEGAPD,QD,RD)', line=430)
W('30,3457', 0o50142, '', 'INDEX', 'TEM2', line=431)
W('30,3460', 0o71643, '', 'MP', 'OMEGAPD', line=432)
W('30,3461', 0o00006, '', 'EXTEND', line=433)
W('30,3462', 0o74741, '', 'MP', 'BIT11', '1/16', line=434)
W('30,3463', 0o00006, '', 'EXTEND', line=435)
W('30,3464', 0o50142, '', 'INDEX', 'TEM2', '                 2', line=436)
W('30,3465', 0o11530, '', 'DV', '1JACC', 'UNITS PI/4 RAD/SEC', line=437)
W('30,3466', 0o54001, '', 'TS', 'L', line=438)
W('30,3467', 0o33771, '', 'CA', 'DELERLIM', line=439)
W('30,3470', 0o03727, '', 'TC', 'LIMITSUB', line=440)
W('30,3471', 0o50142, '', 'INDEX', 'TEM2', line=441)
W('30,3472', 0o55277, '', 'TS', 'DELPEROR', 'LAG ANGLE = OMEGA ABS(OMEGA)/2 ACCEL', line=442)
W('30,3473', 0o10142, '', 'CCS', 'TEM2', line=443)
W('30,3474', 0o13441, '', 'TCF', 'CDUWXFR', line=444)

# HAUSKEEPING AND RETURN

W('30,3475', 0o31646, 'TCQCDUW', 'CA', 'ECDUWUSR', line=448)
W('30,3476', 0o54003, '', 'TS', 'EBANK', "RETURN USER'S EBANK", line=449)

W('30,3477', 0o06037, '', 'TC', 'INTPRET', line=451)
W('30,3500', 0o52001, '', 'SETPD', 'GOTO', kind='interp', line=452)
W('30,3501', 0o00001, '', '', '0', kind='operand', line=453)
W('30,3502', 0o03247, '', '', 'QCDUWUSR', 'NORMAL AND ABNORMAL RETURN TO USER', kind='operand', line=454)

# Page 919
# THRUST VECTOR FILTER SUBROUTINE

W('30,3503', 0o00006, 'FLTRSUB', 'EXTEND', line=459)
W('30,3504', 0o22142, '', 'QXCH', 'TEM2', line=460)
W('30,3505', 0o54143, '', 'TS', 'TEM3', 'SAVE ORIGINAL OFFSET', line=461)
W('30,3506', 0o40000, '', 'COM', '', 'ONE MCT, NO WDS, CAN BE SAVED IF NEG OF', line=462)
W('30,3507', 0o60001, '', 'AD', 'L', "      ORIG OFFSET ARRIVES IN A, BUT IT'S", line=463)
W('30,3510', 0o00006, '', 'EXTEND', '', '      NOT WORTH THE INCREASED OBSCURITY.', line=464)
W('30,3511', 0o51650, '', 'INDEX', 'NDXCDUW', line=465)
W('30,3512', 0o73762, '', 'MP', 'GAINFLTR', line=466)
W('30,3513', 0o54001, '', 'TS', 'L', 'INCR TO OFFSET, UNLIMITED', line=467)
W('30,3514', 0o33764, '', 'CA', 'DUNFVLIM', 'SAME LIMIT FOR Y AND Z', line=468)
W('30,3515', 0o03727, '', 'TC', 'LIMITSUB', 'YIELDS INCR TO OFFSET, LIMITED', line=469)
W('30,3516', 0o60143, '', 'AD', 'TEM3', 'ORIGINAL OFFSET', line=470)
W('30,3517', 0o54001, '', 'TS', 'L', 'TOTAL OFFSET, UNLIMITED', line=471)
W('30,3520', 0o33765, '', 'CA', 'UNFVLIM', 'SAME LIMIT FOR Y AND Z', line=472)
W('30,3521', 0o03727, '', 'TC', 'LIMITSUB', 'YIELDS TOTAL OFFSET, LIMITED', line=473)
W('30,3522', 0o00142, '', 'TC', 'TEM2', line=474)

# SUBR TO TEST THE ANGLE BETWEEN THE PROPOSED WINDOW AND THRUST CMD VCTS

W('30,3523', 0o63441, 'UNWCTEST', 'DOT', 'DSQ', kind='interp', line=478)
W('30,3524', 0o00001, '', '', 'UNX/2', kind='operand', line=479)
W('30,3525', 0o50025, '', 'DSU', 'BMN', kind='interp', line=480)
W('30,3526', 0o21767, '', '', 'DOTSWFMX', kind='operand', line=481)
W('30,3527', 0o61232, '', '', 'DCMCL', kind='operand', line=482)
W('30,3530', 0o43531, '', 'SSP', 'RVQ', 'RVQ FOR ALT CHOICE IF DOT MAGN TOO LARGE', kind='interp', line=483)
W('30,3531', 0o03252, '', '', 'FLAGOODW', '      ZEROING WINDOW GOOD FLAG', kind='operand', line=484)
W('30,3532', 0o00000, '', '', '0', kind='operand', line=485)

# Page 920
# NB2CDUSP RETURNS THE 2'S COMPLEMENT, PI, SP CDU ANGLES X,Y,Z IN MPAC,+1,+2 GIVEN THE MATRIX WHOSE ROW VECTORS
# ARE THE SEMI-UNIT NAV BASE VECTORS X,Y,X EXPRESSED IN STABLE MEMBER COORDINATES, LOCATED AT 0 IN THE PUSH LIST.
# NB2CDUSP USES THE ARCTRGSP WHICH HAS A MAXIMUM ERROR OF +-4 BITS.

W('30,3533', 0o63545, 'NB2CDUSP', 'DLOAD', 'DSQ', kind='interp', line=492)
W('30,3534', 0o00003, '', '', '2', kind='operand', line=493)
W('30,3535', 0o51021, '', 'BDSU', 'BPL', kind='interp', line=494)
W('30,3536', 0o06512, '', '', 'DP1/4TH', kind='operand', line=495)
W('30,3537', 0o61542, '', '', '+3', kind='operand', line=496)
W('30,3540', 0o77745, '', 'DLOAD', kind='interp', line=497)
W('30,3541', 0o06522, '', '', 'ZEROVECS', 'IN CASE SIN WAS SLIGHTLY > 1/2', kind='operand', line=498)
W('30,3542', 0o77566, '', 'SQRT', 'EXIT', 'YIELDS COS(CDUZ) IN UNITS OF 2', kind='interp', line=499)

W('30,3543', 0o00006, '', 'EXTEND', line=501)
W('30,3544', 0o30155, '', 'DCA', 'MPAC', line=502)
W('30,3545', 0o20001, '', 'DDOUBL', line=503)
W('30,3546', 0o54145, '', 'TS', 'TEM5', line=504)
W('30,3547', 0o13552, '', 'TCF', '+3', line=505)
W('30,3550', 0o34733, '', 'CA', 'POSMAX', 'OVERFLOW.  FETCH POSMAX, MPAC ALWAYS POS', line=506)
W('30,3551', 0o54145, '', 'TS', 'TEM5', 'COS(CDUZ) IN TEM5, UNITS 1', line=507)

W('30,3552', 0o50120, '', 'INDEX', 'FIXLOC', line=509)
W('30,3553', 0o30002, '', 'CA', '2', line=510)
W('30,3554', 0o22154, '', 'LXCH', 'MPAC', line=511)
W('30,3555', 0o03622, '', 'TC', 'ARCTRGSP', line=512)
W('30,3556', 0o54156, '', 'TS', 'MPAC +2', 'CDUZ', line=513)

W('30,3557', 0o34755, '', 'CA', 'ZERO', line=515)
W('30,3560', 0o03600, '', 'TC', 'DVBYCOSM', line=516)
W('30,3561', 0o34751, '', 'CA', 'FOUR', line=517)
W('30,3562', 0o03600, '', 'TC', 'DVBYCOSM', line=518)
W('30,3563', 0o40141, '', 'CS', 'TEM1', line=519)
W('30,3564', 0o03622, '', 'TC', 'ARCTRGSP', line=520)
W('30,3565', 0o54155, '', 'TS', 'MPAC +1', 'CDUY', line=521)

W('30,3566', 0o34750, '', 'CA', 'BIT4', line=523)
W('30,3567', 0o03600, '', 'TC', 'DVBYCOSM', line=524)
W('30,3570', 0o33577, '', 'CA', '16OCT', line=525)
W('30,3571', 0o03600, '', 'TC', 'DVBYCOSM', line=526)
W('30,3572', 0o40141, '', 'CS', 'TEM1', line=527)
W('30,3573', 0o03622, '', 'TC', 'ARCTRGSP', line=528)
W('30,3574', 0o54154, '', 'TS', 'MPAC', 'CDUX', line=529)

W('30,3575', 0o06037, '', 'TC', 'INTPRET', line=531)
W('30,3576', 0o77616, '', 'RVQ', kind='interp', line=532)

W('30,3577', 0o00016, '16OCT', 'OCT', '16', kind='data', line=534)

# Page 921
# THE ELEMENTS OF THE NAV BASE MATRIX WHICH WE MUST DIVIDE BY COS(MGA)
# ALREADY CONTAIN COS(MGA)/2 AS A FACTOR. THEREFORE THE QUOTIENT SHOULD
# ORDINARILY NEVER EXCEED 1/2 IN MAGNITUDE.  BUT IF THE MGA IS NEAR PI/2
# THEN COS(MGA) IS NEAR ZERO, AND THERE MAY BE SOME CHAFF IN THE OTHER
# ELEMENTS OF THE MATRIX WHICH WOULD PRODUCE CHAOS UNDER DIVISION.
# BEFORE DIVIDING WE MAKE SURE COS(MGA) IS AT LEAST ONE BIT LARGER
# THAN THE MAGNITUDE OF THE HIGH ORDER PART OF THE OPERAND.
#
# IF ONE OR MORE DIVIDES CANNOT BE PERFORMED, THIS MEANS THAT THE
# REQUIRED MGA IS VERY NEARLY +-PI/2 AND THEREFORE THE OTHER GIMBAL
# ANGLES ARE INDETERMINATE.  THE INNER AND OUTER GIMBAL ANGLES RETURNED
# IN THIS CASE WILL BE RANDOM MULTIPLES OF PI/2.

W('30,3600', 0o60120, 'DVBYCOSM', 'AD', 'FIXLOC', line=550)
W('30,3601', 0o54116, '', 'TS', 'ADDRWD', 'ADRES OF OPERAND', line=551)

W('30,3602', 0o50116, '', 'INDEX', 'ADDRWD', 'FETCH NEG ABS OF OPERAND, AD TEM5, AND', line=553)
W('30,3603', 0o30000, '', 'CA', '0', '      SKIP DIVIDE IF RESULT NEG OR ZERO', line=554)
W('30,3604', 0o00006, '', 'EXTEND', line=555)
W('30,3605', 0o63607, '', 'BZMF', '+2', line=556)
W('30,3606', 0o40000, '', 'COM', line=557)
W('30,3607', 0o60145, '', 'AD', 'TEM5', 'C(A) ZERO OR NEG, C(TEM5) ZERO OR POS', line=558)
W('30,3610', 0o00006, '', 'EXTEND', line=559)
W('30,3611', 0o63617, '', 'BZMF', 'TSL&TCQ', 'DIFFERENCE ALWAYS SMALL IF BRANCH', line=560)

W('30,3612', 0o00006, '', 'EXTEND', '', 'TEM5 EXCEEDS ABS HIGH ORDER PART OF', line=562)
W('30,3613', 0o50116, '', 'INDEX', 'ADDRWD', '      OPERAND BY AT LEAST ONE BIT.', line=563)
W('30,3614', 0o30001, '', 'DCA', '0', '      THEREFORE IT EXCEEDS THE DP OPERAND', line=564)
W('30,3615', 0o00006, '', 'EXTEND', '', '      AND DIVISION WILL ALWAYS SUCCEED.', line=565)
W('30,3616', 0o10145, '', 'DV', 'TEM5', line=566)
W('30,3617', 0o54001, 'TSL&TCQ', 'TS', 'L', line=567)
W('30,3620', 0o22141, '', 'LXCH', 'TEM1', line=568)
W('30,3621', 0o00002, '', 'TC', 'Q', line=569)

# Page 922
# ARCTRGSP RETURNS THE 2'S COMPLEMENT, PI, SP ANGLE IN THE A REGISTER GIVEN ITS SINE IN A AND ITS COSINE IN L IN
# UNITS OF 2.  THE RESULT IS AN UNAMBIGUOUS ANGLE ANYWHERE IN THE CIRCLE, WITH A MAXIMUM ERROR OF +-4 BITS.
# THE ERROR IS PRODUCED BY THE SUBROUTINE SPARCSIN WHICH IS USED ONLY IN THE REGION +-45 DEGREES.

W('30,3622', 0o00006, 'ARCTRGSP', 'EXTEND', line=576)
W('30,3623', 0o13665, '', 'BZF', 'SINZERO', 'TO AVOID DIVIDING BY ZERO', line=577)

W('30,3624', 0o00006, '', 'EXTEND', line=579)
W('30,3625', 0o22144, '', 'QXCH', 'TEM4', line=580)
W('30,3626', 0o54142, '', 'TS', 'TEM2', line=581)
W('30,3627', 0o30001, '', 'CA', 'L', line=582)
W('30,3630', 0o54143, '', 'TS', 'TEM3', line=583)
W('30,3631', 0o34755, '', 'CA', 'ZERO', line=584)
W('30,3632', 0o00006, '', 'EXTEND', line=585)
W('30,3633', 0o10142, '', 'DV', 'TEM2', line=586)
W('30,3634', 0o00006, '', 'EXTEND', line=587)
W('30,3635', 0o13654, '', 'BZF', 'USECOS', line=588)

W('30,3636', 0o10143, '', 'CCS', 'TEM3', 'SIN IS SMALLER OR EQUAL', line=590)
W('30,3637', 0o34755, '', 'CA', 'ZERO', line=591)
W('30,3640', 0o13644, '', 'TCF', '+4', line=592)
W('30,3641', 0o40142, '', 'CS', 'TEM2', 'IF COS NEG, REVERSE SIGN OF SIN,', line=593)
W('30,3642', 0o54142, '', 'TS', 'TEM2', '      ANGLE = PI-ARCSIN(SIN)', line=594)
W('30,3643', 0o34735, '', 'CA', 'NEGMAX', "PICK UP PI, 2'S COMPLEMENT", line=595)
W('30,3644', 0o54143, '', 'TS', 'TEM3', 'WE NO LONGER NEED COS', line=596)
W('30,3645', 0o30142, '', 'CA', 'TEM2', line=597)
W('30,3646', 0o03672, '', 'TC', 'SPARCSIN -1', line=598)
W('30,3647', 0o03743, '', 'TC', 'ONESTO2S', line=599)
W('30,3650', 0o00006, '', 'EXTEND', line=600)
W('30,3651', 0o20143, '', 'MSU', 'TEM3', line=601)
W('30,3652', 0o03743, '1TO2&TCQ', 'TC', 'ONESTO2S', line=602)
W('30,3653', 0o00144, '', 'TC', 'TEM4', line=603)

W('30,3654', 0o40143, 'USECOS', 'CS', 'TEM3', 'COS IS SMALLER', line=605)
W('30,3655', 0o03672, '', 'TC', 'SPARCSIN -1', 'ANGLE = SIGN(SIN)(FI/2-ARCSIN(COS))', line=606)
W('30,3656', 0o64736, '', 'AD', 'HALF', line=607)
W('30,3657', 0o54143, '', 'TS', 'TEM3', 'WE NO LONGER NEED COS', line=608)
W('30,3660', 0o10142, '', 'CCS', 'TEM2', line=609)
W('30,3661', 0o30143, '', 'CA', 'TEM3', line=610)
W('30,3662', 0o13652, '', 'TCF', '1TO2&TCQ', line=611)
W('30,3663', 0o40143, '', 'CS', 'TEM3', line=612)
W('30,3664', 0o13652, '', 'TCF', '1TO2&TCQ', line=613)

W('30,3665', 0o10001, 'SINZERO', 'CCS', 'L', line=615)
W('30,3666', 0o34755, '', 'CA', 'ZERO', line=616)
W('30,3667', 0o00002, '', 'TC', 'Q', line=617)
W('30,3670', 0o34735, '', 'CA', 'NEGMAX', "PI, 2'S COMP", line=618)
W('30,3671', 0o00002, '', 'TC', 'Q', line=619)

# Page 923
# SPARCSIN TAKES AN ARGUMENT SCALED UNITY IN A AND RETURNS AN ANGLE SCALED
# 180 DEGREES IN A.  IT HAS BEEN UNIT TESTED IN THE REGION +-.94 (+-70
# DEGREES) AND THE MAXIMUM ERROR IS +-5 BITS WITH AN AVERAGE TIME OF
# 450 MICROSECONDS.  SPARCSIN -1 TAKES THE ARGUMENT SCALED TWO.  (BOB CRISP)

W('30,3672', 0o60000, '', 'DOUBLE', line=627)
W('30,3673', 0o54021, 'SPARCSIN', 'TS', 'SR', line=628)
W('30,3674', 0o13700, '', 'TCF', '+4', line=629)
W('30,3675', 0o50000, '', 'INDEX', 'A', line=630)
W('30,3676', 0o44734, '', 'CS', 'LIMITS', line=631)
W('30,3677', 0o54021, '', 'TS', 'SR', line=632)
W('30,3700', 0o00006, '', 'EXTEND', line=633)
W('30,3701', 0o70000, '', 'MP', 'A', line=634)
W('30,3702', 0o54141, '', 'TS', 'TEM1', line=635)
W('30,3703', 0o00006, '', 'EXTEND', line=636)
W('30,3704', 0o73726, '', 'MP', 'DPL9', line=637)
W('30,3705', 0o63725, '', 'AD', 'DPL7', line=638)
W('30,3706', 0o00006, '', 'EXTEND', line=639)
W('30,3707', 0o70141, '', 'MP', 'TEM1', line=640)
W('30,3710', 0o63724, '', 'AD', 'DPL5', line=641)
W('30,3711', 0o00006, '', 'EXTEND', line=642)
W('30,3712', 0o70141, '', 'MP', 'TEM1', line=643)
W('30,3713', 0o63723, '', 'AD', 'DPL3', line=644)
W('30,3714', 0o00006, '', 'EXTEND', line=645)
W('30,3715', 0o70141, '', 'MP', 'TEM1', line=646)
W('30,3716', 0o63722, '', 'AD', 'DPL1', line=647)
W('30,3717', 0o00006, '', 'EXTEND', line=648)
W('30,3720', 0o70021, '', 'MP', 'SR', line=649)
W('30,3721', 0o00002, '', 'TC', 'Q', line=650)
W('30,3722', 0o24406, 'DPL1', 'DEC', '10502', kind='data', line=651)
W('30,3723', 0o00660, 'DPL3', 'DEC', '432', kind='data', line=652)
W('30,3724', 0o16204, 'DPL5', 'DEC', '7300', kind='data', line=653)
W('30,3725', 0o50744, 'DPL7', 'DEC', '-11803', kind='data', line=654)
W('30,3726', 0o20315, 'DPL9', 'DEC', '8397', kind='data', line=655)

# Page 924
# LIMITSUB LIMITS THE MAGNITUDE OF THE POSITIVE OR NEGATIVE VARIABLE
# ARRIVING IN L TO THE POSITIVE LIMIT ARRIVING IN A.
# THE SIGNED LIMITED VARIABLE IS RETURNED IN A.
#
# VERSION COUTESY HUGH BLAIR-SMITH

W('30,3727', 0o54141, 'LIMITSUB', 'TS', 'TEM1', line=664)
W('30,3730', 0o34755, '', 'CA', 'ZERO', line=665)
W('30,3731', 0o00006, '', 'EXTEND', line=666)
W('30,3732', 0o10141, '', 'DV', 'TEM1', line=667)
W('30,3733', 0o10000, '', 'CCS', 'A', line=668)
W('30,3734', 0o22141, '', 'LXCH', 'TEM1', line=669)
W('30,3735', 0o13737, '', 'TCF', '+2', line=670)
W('30,3736', 0o13741, '', 'TCF', '+3', line=671)
W('30,3737', 0o30001, '', 'CA', 'L', line=672)
W('30,3740', 0o00002, '', 'TC', 'Q', line=673)
W('30,3741', 0o40141, '', 'CS', 'TEM1', line=674)
W('30,3742', 0o00002, '', 'TC', 'Q', line=675)

# SUBROUTINE TO CONVERT 1'S COMP SP TO 2'S COMP

W('30,3743', 0o10000, 'ONESTO2S', 'CCS', 'A', line=679)
W('30,3744', 0o64753, '', 'AD', 'ONE', line=680)
W('30,3745', 0o00002, '', 'TC', 'Q', line=681)
W('30,3746', 0o40000, '', 'CS', 'A', line=682)
W('30,3747', 0o00002, '', 'TC', 'Q', line=683)

# NO ATTITUDE CONTROL

W('30,3750', 0o05567, 'NOATTCNT', 'TC', 'ALARM', line=687)
W('30,3751', 0o00402, '', 'OCT', '00402', 'NO ATTITUDE CONTROL', kind='data', line=688)

W('30,3752', 0o00004, '', 'INHINT', '', 'COME HERE FOR NOATTCNT WITHOUT ALARM', line=690)
W('30,3753', 0o04674, '', 'TC', 'IBNKCALL', 'RELINT AT TC INTPRET AFTER TCQCDUW', line=691)
W('30,3754', 0o40165, '', 'FCADR', 'STOPRATE', kind='data', line=692)
W('30,3755', 0o13475, '', 'TCF', 'TCQCDUW', 'RETURN TO USER SKIPPING AUTOPILOT CMDS', line=693)

# MIDDLE GIMBAL ANGLE ALARM

W('30,3756', 0o05567, 'ALARMMGA', 'TC', 'ALARM', line=697)
W('30,3757', 0o00401, '', 'OCT', '00401', kind='data', line=698)
W('30,3760', 0o13275, '', 'TCF', 'MGARET', line=699)

# Page 925
# ******************************************************************
# CONSTANTS
# ******************************************************************

# ADDRESS CONSTANTS

W('30,3761', 0o03246, 'ECDUWL', 'ECADR', 'ECDUW', kind='data', line=708)

# THRUST DIRECTION FILTER CONSTANTS

W('30,3762', 0o06315, 'GAINFLTR', 'DEC', '.2', 'GAIN FILTER SANS CSM', kind='data', line=712)
W('30,3763', 0o03146, '', 'DEC', '.1', 'GAIN FILTER WITH CSM', kind='data', line=713)

W('30,3764', 0o00071, 'DUNFVLIM', 'DEC', '.007 B-1', '7 MR MAX CHG IN F DIR IN VEH IN 2 SECS.', kind='data', line=715)
# THIS DOES NOT ALLOW FOR S/C ROT RATE.

W('30,3765', 0o02041, 'UNFVLIM', 'DEC', '.129 B-1', '129 MR MAX THRUST OFFSET.  105 MR TRAVEL', kind='data', line=718)
# +10MR DEFL+5MR MECH MOUNT+9MR ABLATION.

# CONSTANT RELATED TO GIMBAL ANGLE COMPUTATIONS

W('30,3766', 0o01673, 'DOTSWFMX', 'DEC', '.93302 B-4', 'LIM COLNRTY OF UNWC/2 & UNFC/2 TO 85 DEG', kind='data', line=723)
# LOWER PART COMES FROM NEXT CONSTANT

W('30,3767', 0o03434, 'DAXMAX', 'DEC', '.11111111111', "DELATTX LIM TO 20 DEG IN 2 SECS, 1'S, PI", kind='data', line=726)
W('30,3770', 0o00266, '', 'DEC', '.0111111111', '2 DEG WHEN CSM DOCKED', kind='data', line=727)

W('30,3771', 0o01616, 'DAY/2MAX', 'DEC', '.05555555555', 'LIKEWISE FOR DELATTY', kind='data', line=729)
W('30,3772', 0o00133, '', 'DEC', '.0055555555', kind='data', line=730)

S('DAZMAX', 'equals', 0o71767, line=732)  # LIKEWISE FOR DELATTZ

W('30,3773', 0o14344, 'CDUZDLIM', 'DEC', '.3888888888', "70 DEG LIMIT FOR MGA, 1'S, PI", kind='data', line=734)

# CONSTANTS FOR DATA TRANSFER

W('30,3774', 0o01463, 'DT/DELT', 'DEC', '.05', '.1 SEC/2 SEC WHICH IS THE AUTOPILOT', kind='data', line=738)
# CONTROL SAMPLE PERIOD/COMPUTATION PERIOD

S('DELERLIM', 'equals', 0o71771, line=741)  #       0 DEG LIMIT FOR LAG ANGLES, 1'S, PI

# *** END OF FLY        .132 ***
