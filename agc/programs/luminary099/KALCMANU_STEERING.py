"""KALCMANU_STEERING.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/KALCMANU_STEERING.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 365-369 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('KALCMANU_STEERING', 'KALCMANU_STEERING.agc', 'Luminary099', pages='365-369')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     KALCMANU_STEERING.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        365-369
# Mod history:  2009-05-17 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2011-01-06 JL   Added missing comment characters.
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

# Page 365
# GENERATION OF STEERING COMMANDS FOR DIGITAL AUTOPILOT FREE FALL MANEUVERS
#
# NEW COMMANDS WILL BE GENERATED EVERY ONE SECOND DURING THE MANEUVER

#   EBANK= TTEMP

W('22,3003', 0o04616, 'NEWDELHI', 'TC', 'BANKCALL', 'CHECK FOR AUTO STABILIZATION', line=37)
W('22,3004', 0o54262, '', 'CADR', 'ISITAUTO', 'ONLY', kind='data', line=38)
W('22,3005', 0o10000, '', 'CCS', 'A', line=39)
W('22,3006', 0o12730, '', 'TCF', 'NOGO -2', line=40)
W('22,3007', 0o06037, 'NEWANGL', 'TC', 'INTPRET', line=41)
W('22,3010', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=42)
W('22,3011', 0o03246, '', '', 'MIS', 'COMPUTE THE NEW MATRIX FROM S/C TO', kind='operand', line=43)
W('22,3012', 0o02230, '', '', 'KEL', 'STABLE MEMBER AXES', kind='operand', line=44)
W('22,3013', 0o77624, '', 'CALL', kind='interp', line=45)
W('22,3014', 0o44312, '', '', 'MXM3', kind='operand', line=46)
W('22,3015', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=47)
W('22,3016', 0o50514, '', 'STOVL', 'MIS +12D', 'CALCULATE NEW DESIRED CDU ANGLES', kind='interp', line=48)
W('22,3017', 0o77626, '', 'STADR', kind='interp', line=49)
W('22,3020', 0o50522, '', 'STOVL', 'MIS +6D', kind='interp', line=50)
W('22,3021', 0o77626, '', 'STADR', kind='interp', line=51)
W('22,3022', 0o74530, '', 'STORE', 'MIS', kind='interp', line=52)
W('22,3023', 0o45160, '', 'AXC,1', 'CALL', kind='interp', line=53)
W('22,3024', 0o03246, '', '', 'MIS', kind='operand', line=54)
W('22,3025', 0o44654, '', '', 'DCMTOCDU', 'PICK UP THE NEW CDU ANGLES FROM MATRIX', kind='operand', line=55)
W('22,3026', 0o77634, '', 'RTB', kind='interp', line=56)
W('22,3027', 0o21620, '', '', 'V1STO2S', kind='operand', line=57)
W('22,3030', 0o03304, '', 'STORE', 'NCDU', 'NEW CDU ANGLES', kind='interp', line=58)
W('22,3031', 0o77414, '', 'BONCLR', 'EXIT', kind='interp', line=59)
W('22,3032', 0o01215, '', '', 'CALCMAN2', kind='operand', line=60)
W('22,3033', 0o45122, '', '', 'MANUSTAT', 'TO START MANEUVER', kind='operand', line=61)
W('22,3034', 0o34752, '', 'CAF', 'TWO', '         +0 OTHERWISE', line=62)
W('22,3035', 0o55272, 'INCRDCDU', 'TS', 'SPNDX', line=63)
W('22,3036', 0o51272, '', 'INDEX', 'SPNDX', line=64)
W('22,3037', 0o31676, '', 'CA', 'BCDU', 'INITIAL CDU ANGLES', line=65)
W('22,3040', 0o00006, '', 'EXTEND', '', 'OR PREVIOUS DESIRED CDU ANGLES', line=66)
W('22,3041', 0o51272, '', 'INDEX', 'SPNDX', line=67)
W('22,3042', 0o21703, '', 'MSU', 'NCDU', line=68)
W('22,3043', 0o00006, '', 'EXTEND', line=69)
#   SETLOC KALCMON1
#   BANK
W('22,3044', 0o73121, '', 'MP', 'DT/TAU', line=72)
W('22,3045', 0o10000, '', 'CCS', 'A', 'CONVERT TO 2S COMPLEMENT', line=73)
W('22,3046', 0o64753, '', 'AD', 'ONE', line=74)
W('22,3047', 0o13051, '', 'TCF', '+2', line=75)
W('22,3050', 0o40000, '', 'COM', line=76)
W('22,3051', 0o51272, '', 'INDEX', 'SPNDX', line=77)
W('22,3052', 0o55640, '', 'TS', 'DELDCDU', 'ANGLE INCREMENTS TO BE ADDED TO', line=78)
W('22,3053', 0o51272, '', 'INDEX', 'SPNDX', 'CDUXD, CDUYD, CDUZD EVERY TENTH SECOND', line=79)
# Page 366
W('22,3054', 0o31703, '', 'CA', 'NCDU', 'BY LEM DAP', line=81)
W('22,3055', 0o51272, '', 'INDEX', 'SPNDX', line=82)
W('22,3056', 0o57676, '', 'XCH', 'BCDU', line=83)
W('22,3057', 0o51272, '', 'INDEX', 'SPNDX', line=84)
W('22,3060', 0o55635, '', 'TS', 'CDUXD', line=85)
W('22,3061', 0o11272, '', 'CCS', 'SPNDX', line=86)
W('22,3062', 0o13035, '', 'TCF', 'INCRDCDU', 'LOOP FOR THREE AXES', line=87)

W('22,3063', 0o00003, '', 'RELINT', line=89)

# COMPARE PRESENT TIME WITH TIME TO TERMINATE MANEUVER

W('22,3064', 0o03075, 'TMANUCHK', 'TC', 'TIMECHK', line=93)
W('22,3065', 0o13170, '', 'TCF', 'CONTMANU', line=94)
W('22,3066', 0o34753, '', 'CAF', 'ONE', line=95)
W('22,3067', 0o00004, 'MANUSTAL', 'INHINT', '', 'END MAJOR PART OF MANEUVER WITHIN 1 SEC', line=96)
W('22,3070', 0o05203, '', 'TC', 'WAITLIST', 'UNDER WAITLIST CALL TO MANUSTOP', line=97)
#   EBANK= TTEMP
W('22,3071', 0o03213, '', '2CADR', 'MANUSTOP', kind='data', line=99)
W('22,3072', 0o44066, kind='data', line=99)

W('22,3073', 0o00003, '', 'RELINT', line=101)
W('22,3074', 0o15155, '', 'TCF', 'ENDOFJOB', line=102)

W('22,3075', 0o00006, 'TIMECHK', 'EXTEND', line=104)
W('22,3076', 0o40025, '', 'DCS', 'TIME2', line=105)
W('22,3077', 0o53710, '', 'DXCH', 'TTEMP', line=106)
W('22,3100', 0o00006, '', 'EXTEND', line=107)
W('22,3101', 0o31734, '', 'DCA', 'TM', line=108)
W('22,3102', 0o21710, '', 'DAS', 'TTEMP', line=109)
W('22,3103', 0o11707, '', 'CCS', 'TTEMP', line=110)
W('22,3104', 0o00002, '', 'TC', 'Q', line=111)
W('22,3105', 0o13107, '', 'TCF', '+2', line=112)
W('22,3106', 0o13117, '', 'TCF', '2NDRETRN', line=113)
W('22,3107', 0o11710, '', 'CCS', 'TTEMP +1', line=114)
W('22,3110', 0o00002, '', 'TC', 'Q', line=115)
W('22,3111', 0o13113, '', 'TCF', 'MANUOFF', line=116)
W('22,3112', 0o40000, '', 'COM', line=117)
W('22,3113', 0o63166, 'MANUOFF', 'AD', 'ONESEK +1', line=118)
W('22,3114', 0o00006, '', 'EXTEND', line=119)
W('22,3115', 0o63117, '', 'BZMF', '2NDRETRN', line=120)
W('22,3116', 0o24002, '', 'INCR', 'Q', line=121)
W('22,3117', 0o24002, '2NDRETRN', 'INCR', 'Q', line=122)
W('22,3120', 0o00002, '', 'TC', 'Q', line=123)

W('22,3121', 0o03146, 'DT/TAU', 'DEC', '.1', kind='data', line=125)

W('22,3122', 0o77776, 'MANUSTAT', 'EXIT', '', 'INITIALIZATION ROUTINE', kind='interp', line=127)
W('22,3123', 0o00006, '', 'EXTEND', '', 'FOR AUTOMATIC MANEUVERS', line=128)
W('22,3124', 0o30025, '', 'DCA', 'TIME2', line=129)
# Page 367
W('22,3125', 0o21734, '', 'DAS', 'TM', 'TM+TO    MANEUVER COMPLETION TIME', line=131)
W('22,3126', 0o00006, '', 'EXTEND', line=132)
W('22,3127', 0o43166, '', 'DCS', 'ONESEK', line=133)
W('22,3130', 0o21734, '', 'DAS', 'TM', '(TM+TO)-1', line=134)
W('22,3131', 0o00004, '', 'INHINT', line=135)
W('22,3132', 0o34752, '', 'CAF', 'TWO', line=136)
W('22,3133', 0o55701, 'RATEBIAS', 'TS', 'KSPNDX', line=137)
W('22,3134', 0o60000, '', 'DOUBLE', line=138)
W('22,3135', 0o55702, '', 'TS', 'KDPNDX', line=139)
W('22,3136', 0o50000, '', 'INDEX', 'A', line=140)
W('22,3137', 0o31725, '', 'CA', 'BRATE', line=141)
W('22,3140', 0o51701, '', 'INDEX', 'KSPNDX', 'STORE MANEUVER RATE IN', line=142)
W('22,3141', 0o55643, '', 'TS', 'OMEGAPD', 'OMEGAPD, OMEGAQD, OMEGARD', line=143)
W('22,3142', 0o00006, '', 'EXTEND', line=144)
W('22,3143', 0o63145, '', 'BZMF', '+2', 'COMPUTE ATTITUDE ERROR', line=145)
W('22,3144', 0o40000, '', 'COM', '', 'OFFSET = (WX)ABS(WX)/2AJX', line=146)
W('22,3145', 0o00006, '', 'EXTEND', '', 'WHERE AJX= 2-JET ACCELERATION', line=147)
W('22,3146', 0o73167, '', 'MP', 'BIASCALE', '= -1/16', line=148)
W('22,3147', 0o00006, '', 'EXTEND', line=149)
W('22,3150', 0o51702, '', 'INDEX', 'KDPNDX', line=150)
W('22,3151', 0o71725, '', 'MP', 'BRATE', line=151)
W('22,3152', 0o00006, '', 'EXTEND', line=152)
W('22,3153', 0o51701, '', 'INDEX', 'KSPNDX', line=153)
W('22,3154', 0o11530, '', 'DV', '1JACC', '=AJX  $ 90 DEG/SEC-SEC', line=154)
W('22,3155', 0o51701, '', 'INDEX', 'KSPNDX', line=155)
W('22,3156', 0o55277, '', 'TS', 'DELPEROR', '    $ 180 DEG', line=156)
W('22,3157', 0o11701, '', 'CCS', 'KSPNDX', line=157)
W('22,3160', 0o13133, '', 'TCF', 'RATEBIAS', line=158)

W('22,3161', 0o30025, '', 'CA', 'TIME1', line=160)
W('22,3162', 0o63166, '', 'AD', 'ONESEK +1', line=161)
W('22,3163', 0o57706, '', 'XCH', 'NEXTIME', line=162)
W('22,3164', 0o13034, '', 'TCF', 'INCRDCDU -1', line=163)

W('22,3165', 0o00000, 'ONESEK', 'DEC', '0', kind='data', line=165)
W('22,3166', 0o00144, '', 'DEC', '100', kind='data', line=166)

W('22,3167', 0o75777, 'BIASCALE', 'OCT', '75777', '= -1/16', kind='data', line=168)

W('22,3170', 0o40025, 'CONTMANU', 'CS', 'TIME1', 'RESET FOR NEXT DCDU UPDATE', line=170)
W('22,3171', 0o61706, '', 'AD', 'NEXTIME', line=171)
W('22,3172', 0o10000, '', 'CCS', 'A', line=172)
W('22,3173', 0o64753, '', 'AD', 'ONE', line=173)
W('22,3174', 0o13177, '', 'TCF', 'MANUCALL', line=174)
W('22,3175', 0o64735, '', 'AD', 'NEGMAX', line=175)
W('22,3176', 0o40000, '', 'COM', line=176)
W('22,3177', 0o00004, 'MANUCALL', 'INHINT', '', 'CALL FOR NEXT UPDATE VIA WAITLIST', line=177)
W('22,3200', 0o05203, '', 'TC', 'WAITLIST', line=178)
#   EBANK= TTEMP
W('22,3201', 0o03206, '', '2CADR', 'UPDTCALL', kind='data', line=180)
W('22,3202', 0o44066, kind='data', line=180)
# Page 368
W('22,3203', 0o33166, '', 'CAF', 'ONESEK +1', 'INCREMENT TIME FOR NEXT UPDATE', line=182)
W('22,3204', 0o27706, '', 'ADS', 'NEXTIME', line=183)
W('22,3205', 0o15155, '', 'TCF', 'ENDOFJOB', line=184)

W('22,3206', 0o37714, 'UPDTCALL', 'CAF', 'PRIO26', 'SATELLITE PROGRAM TO CALL FOR UPDATE', line=186)
W('22,3207', 0o05105, '', 'TC', 'FINDVAC', 'OF STEERING COMMANDS', line=187)
#   EBANK= TTEMP
W('22,3210', 0o03003, '', '2CADR', 'NEWDELHI', kind='data', line=189)
W('22,3211', 0o44066, kind='data', line=189)

W('22,3212', 0o05261, '', 'TC', 'TASKOVER', line=191)

# Page 369
# ROUTINE FOR TERMINATING AUTOMATIC MANEUVERS

W('22,3213', 0o34755, 'MANUSTOP', 'CAF', 'ZERO', 'ZERO MANEUVER RATES', line=196)
W('22,3214', 0o55642, '', 'TS', 'DELDCDU2', line=197)
W('22,3215', 0o55645, '', 'TS', 'OMEGARD', line=198)
W('22,3216', 0o55301, '', 'TS', 'DELREROR', line=199)
W('22,3217', 0o55641, '', 'TS', 'DELDCDU1', line=200)
W('22,3220', 0o55644, '', 'TS', 'OMEGAQD', line=201)
W('22,3221', 0o55300, '', 'TS', 'DELQEROR', line=202)
W('22,3222', 0o30323, '', 'CA', 'CPSI', 'SET DESIRED GIMBAL ANGLES TO', line=203)
W('22,3223', 0o55637, '', 'TS', 'CDUZD', 'DESIRED FINAL GIMBAL ANGLES', line=204)
W('22,3224', 0o30322, '', 'CA', 'CTHETA', line=205)
W('22,3225', 0o55636, '', 'TS', 'CDUYD', line=206)
W('22,3226', 0o30321, 'ENDROLL', 'CA', 'CPHI', 'NO FINAL YAW', line=207)
W('22,3227', 0o55635, '', 'TS', 'CDUXD', line=208)
W('22,3230', 0o34755, '', 'CAF', 'ZERO', line=209)
W('22,3231', 0o55643, '', 'TS', 'OMEGAPD', 'I.E. MANEUVER DID NOT GO THRU', line=210)
W('22,3232', 0o55640, '', 'TS', 'DELDCDU', 'GIMBAL LOCK ORIGINALLY', line=211)
W('22,3233', 0o55277, '', 'TS', 'DELPEROR', line=212)
W('22,3234', 0o31311, 'GOODMANU', 'CA', 'ATTPRIO', 'RESTORE USERS PRIO', line=213)
W('22,3235', 0o54063, '', 'TS', 'NEWPRIO', line=214)

W('22,3236', 0o34755, '', 'CA', 'ZERO', 'ZERO ATTCADR', line=216)
W('22,3237', 0o53310, '', 'DXCH', 'ATTCADR', line=217)

W('22,3240', 0o05116, '', 'TC', 'SPVAC', 'RETURN TO USER', line=219)

W('22,3241', 0o05261, '', 'TC', 'TASKOVER', line=221)
