"""WAITLIST.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/WAITLIST.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1117-1132 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('WAITLIST', 'WAITLIST.agc', 'Luminary099', pages='1117-1132')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     WAITLIST.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1117-1132
# Mod history:  2009-05-25 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2011-01-06 JL   Fixed pseudo-label indentation.
# 2011-05-07 JL   Removed workarounds.
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

# Page 1117
# PROGRAM DESCRIPTION                                                           DATE -- 10 OCTOBER 1966
# MOD NO -- 2                                                                   LOG SECTION -- WAITLIST
# MOD BY -- MILLER      (DTMAX INCREASED TO 162.5 SEC)                          ASSEMBLY -- SUNBURST REV 5
# MOD 3 BY KERNAN       (INHINT INSERTED AT WAITLIST) 2/28/68 SKIPPER REV 4
# MOD 4 BY KERNAN       (TWIDDLE IN 54) 3/28/68 SKIPPER REV 13.
#
# FUNCTIONAL DESCRIPTION --
# PART OF A SECTION OF PROGRAMS -- WAITLIST, TASKOVER, T3RUPT, USED TO CALL A PROGRAM (CALLED A TASK),
# WHICH IS TO BEGIN IN C(A) CENTISECONDS.  WAITLIST UPDATES TIME3, LST1, AND LST2.  THE MEANING OF THESE LISTS
# FOLLOW.
#
# C(TIME3) = 16384 -(T1-T) CENTISECONDS, (T=PRESENT TIME, T1-TIME FOR TASK1)
#
# C(LST1)         =       -(T2-T1)+1
# C(LST1 +1)      =       -(T3-T2)+1
# C(LST1 +2)      =       -(T4-T3)+1
# ...
# C(LST1 +6)      =       -(T8-T7)+1
# C(LST1 +7)      =       -(T9-T8)+1
#
# C(LST2)         =       2CADR OF TASK1
# C(LST2 +2)      =       2CADR OF TASK2
# ...
# C(LST2 +14)     =       2CADR OF TASK8
# C(LST2 +16)     =       2CADR OF TASK9
#
# WARNINGS --
# 1)      1 <= C(A) <= 16250D (1 CENTISECOND TO 162.5 SEC)
# 2)      9 TASKS MAXIMUM
# 3)      TASKS CALLED UNDER INTERRUPT INHIBITED
# 4)      TASKS END BY TC TASKOVER
#
# CALLING SEQUENCE --
# L-1     CA      DELTAT  (TIME IN CENTISECONDS TO TASK START)
# L       TC      WAITLIST
# L+1     2CADR   DESIRED TASK.
# L+2     (MINOR OF 2CADR)
# L+3     RELINT          (RETURNS HERE)
#
# TWIDDLE --
# TWIDDLE IS FOR USE WHEN THE TASK BEING SET UP IS IN THE SAME EBANK AND FBANK AS THE USER.  IN
# SUCH CASES, IT IMPROVES UPON WAITLIST BY ELIMINATING THE NEED FOR THE BBCON HALF OF THE 2CADR,
# Page 1118
# SAVING A WORD.  TWIDDLE IS LIKE WAITLIST IN EVERY RESPECT EXCEPT CALLING SEQUENCE, TO WIT,
# L-1     CA      DELTAT
# L       TC      TWIDDLE
# L+1     ADRES   DESIRED TASK
# L+2     RELINT          (RETURNS HERE)
#
# NORMAL EXIT MODES --
# AT L+3 OF CALLING SEQUENCE.
#
# ALARM OR ABORT EXIT MODES --
# TC      ABORT
# OCT     1203    (WAITLIST OVERFLOW -- TOO MANY TASKS)
#
# ERASABLE INITIALIZATION REQUIRED --
# ACCOMPLISHED BY FRESH START --  LST2, ..., LST2 +16 = ENDTASK
# LST1, ..., LST1 +7  = NEG1/2
#
# OUTPUT --
# LST1 AND LST2 UPDATED WTIH NEW TASK AND ASSOCIATED TIME.
#
# DEBRIS --
# CENTRALS -- A,Q,L
# OTHER    -- WAITEXIT, WAITADR, WAITTEMP, WAITBANK
#
# DETAILED ANALYSIS OF TIMING --
# CONTROL WILL NOT BE RETURNED TO THE SPECIFIED ADDRESS (2CADR) IN EXACTLY DELTA T CENTISECONDS.
# THE APPROXIMATE TIME MAY BE CALCULATED AS FOLLOWS:
# LET T0 = THE TIME OF THE TC WAITLIST
# LET TS = T0 +147U + COUNTER INCREMENTS (SET UP TIME)
# LET X  = TS -(100TS)/100  (VARIANCE FROM COUNTERS)
# LET Y  = LENGTH OF TIME OF INHIBIT INTERRUPT AFTER T3RUPT
# LET Z  = LENGTH OF TIME TO PROCESS TASKS WHICH ARE DUE THIS T3RUPT BUT DISPATCHED EARLIER.
# (Z=0, USUALLY).
# LET DELTD  = THE ACTUAL TIME TAKEN TO GIVE CONTROL TO 2CADR
# THEN DELTD = TS+DELTA T -X +Y +Z +1.05MS* +COUNTERS*
# *THE TIME TAKEN BY WAITLIST ITSELF AND THE COUNTER TICKING DURING THIS WAITLIST TIME.
# IN SHORT, THE ACTUAL TIME TO RETURN CONTROL TO A 2CADR IS AUGMENTED BY THE TIME TO SET UP THE TASK'S
# INTERRUPT, ALL COUNTERS TICKING, THE T3RUPT PROCESSING TIME, THE WAITLIST PROCESSING TIME AND THE POSSIBILITY
# OF OTHER TASKS INHIBITING THE INTERRUPT.

#   BLOCK 02
# Page 1119
#   EBANK= LST1  # TASK LISTS IN SWITCHED E BANK.

#   COUNT* $$/WAIT
W('5173', 0o00004, 'TWIDDLE', 'INHINT', line=120)
W('5174', 0o54001, '', 'TS', 'L', 'SAVE DELAY TIME IN L', line=121)
W('5175', 0o34733, '', 'CA', 'POSMAX', line=122)
W('5176', 0o26002, '', 'ADS', 'Q', 'CREATING OVERFLOW AND Q-1 IN Q', line=123)
W('5177', 0o30006, '', 'CA', 'BBANK', line=124)
W('5200', 0o00006, '', 'EXTEND', line=125)
W('5201', 0o04007, '', 'ROR', 'SUPERBNK', line=126)
W('5202', 0o56001, '', 'XCH', 'L', line=127)

W('5203', 0o00004, 'WAITLIST', 'INHINT', line=129)
W('5204', 0o56002, '', 'XCH', 'Q', 'SAVE DELTA T IN Q AND RETURN IN', line=130)
W('5205', 0o54061, '', 'TS', 'WAITEXIT', 'WAITEXIT.', line=131)
W('5206', 0o00006, '', 'EXTEND', line=132)
W('5207', 0o50061, '', 'INDEX', 'WAITEXIT', 'IF TWIDDLING, THE TS SKIPS TO HERE', line=133)
W('5210', 0o30001, '', 'DCA', '0', 'PICK UP 2CADR OF TASK.', line=134)
W('5211', 0o54063, '', 'TS', 'WAITADR', 'BBCON WILL REMAIN IN L', line=135)
W('5212', 0o35220, 'DLY2', 'CAF', 'WAITBB', 'ENTRY FROM FIXDELAY AND VARDELAY.', line=136)
W('5213', 0o56006, '', 'XCH', 'BBANK', line=137)
W('5214', 0o13231, '', 'TCF', 'WAIT2', line=138)

# RETURN TO CALLER AFTER TASK INSERTION:

W('5215', 0o52062, 'LVWTLIST', 'DXCH', 'WAITEXIT', line=142)
W('5216', 0o64752, '', 'AD', 'TWO', line=143)
W('5217', 0o52006, '', 'DTCB', line=144)

#   EBANK= LST1
W('5220', 0o02063, 'WAITBB', 'BBCON', 'WAIT2', kind='data', line=147)

# RETURN TO CALLER +2 AFTER WAITING DT SPECIFIED AT CALLER +1.

W('5221', 0o50002, 'FIXDELAY', 'INDEX', 'Q', 'BOTH ROUTINES MUST BE CALLED UNDER', line=151)
W('5222', 0o30000, '', 'CAF', '0', 'WAITLIST CONTROL AND TERMINATE THE TASK', line=152)
W('5223', 0o24002, '', 'INCR', 'Q', 'IN WHICH THEY WERE CALLED.', line=153)

# RETURN TO CALLER +1 AFTER WAITING THE DT AS ARRIVING IN A.

W('5224', 0o56002, 'VARDELAY', 'XCH', 'Q', 'DT TO Q.  TASK ADRES TO WAITADR.', line=157)
W('5225', 0o54063, '', 'TS', 'WAITADR', line=158)
W('5226', 0o30006, '', 'CA', 'BBANK', 'BBANK IS SAVED DURING DELAY.', line=159)
W('5227', 0o00006, '', 'EXTEND', line=160)
W('5230', 0o04007, '', 'ROR', 'SUPERBNK', 'ADD SBANK TO BBCON.', line=161)
W('5231', 0o54001, '', 'TS', 'L', line=162)
W('5232', 0o35235, '', 'CAF', 'DELAYEX', line=163)
W('5233', 0o54061, '', 'TS', 'WAITEXIT', 'GO TO TASKOVER AFTER TASK ENTRY.', line=164)
W('5234', 0o15212, '', 'TCF', 'DLY2', line=165)

# Page 1120
W('5235', 0o15257, 'DELAYEX', 'TCF', 'TASKOVER -2', 'RETURNS TO TASKOVER.', line=168)

# Page 1121
# ENDTASK MUST ENTERED IN FIXED-FIXED SO IT IS DISTINGUISHABLE BY ITS ADRES ALONE.

#   EBANK= LST1
W('5236', 0o72537, 'ENDTASK', '-2CADR', 'SVCT3', kind='data', line=174)
W('5237', 0o73714, kind='data', line=174)

W('5240', 0o10076, 'SVCT3', 'CCS', 'FLAGWRD2', 'DRIFT FLAG', line=176)
W('5241', 0o15261, '', 'TCF', 'TASKOVER', line=177)
W('5242', 0o15261, '', 'TCF', 'TASKOVER', line=178)
W('5243', 0o15244, '', 'TCF', '+1', line=179)

W('5244', 0o11304, 'CKIMUSE', 'CCS', 'IMUCADR', "DON'T DO NBDONLY IF SOMEONE ELSE IS IN", line=181)
W('5245', 0o15256, '', 'TCF', 'SVCT3X', 'IMUSTALL.', line=182)
W('5246', 0o15251, '', 'TCF', '+3', line=183)
W('5247', 0o15256, '', 'TCF', 'SVCT3X', line=184)
W('5250', 0o15256, '', 'TCF', 'SVCT3X', line=185)

W('5251', 0o37723, '', 'CAF', 'PRIO35', 'COMPENSATE FOR NBD COEFFICIENTS ONLY.', line=187)
W('5252', 0o05072, '', 'TC', 'NOVAC', '      ENABLE EVERY 81.93 SECONDS', line=188)
#   EBANK= NBDX
W('5253', 0o03555, '', '2CADR', 'NBDONLY', kind='data', line=190)
W('5254', 0o14063, kind='data', line=190)

W('5255', 0o15261, '', 'TCF', 'TASKOVER', line=192)

W('5256', 0o05221, 'SVCT3X', 'TC', 'FIXDELAY', 'DELAY MAX OF 2 TIMES FOR IMUZERO.', line=194)
W('5257', 0o00764, '', 'DEC', '500', kind='data', line=195)
W('5260', 0o05240, '', 'TC', 'SVCT3', 'CHECK DRIFT FLAG AGAIN.', line=196)

# Page 1122
# BEGIN TASK INSERTION.

#   BANK 01
#   COUNT* $$/WAIT
W('01,3231', 0o54062, 'WAIT2', 'TS', 'WAITBANK', 'BBANK OF CALLING PROGRAM.', line=203)
W('01,3232', 0o30002, '', 'CA', 'Q', line=204)
W('01,3233', 0o00006, '', 'EXTEND', line=205)
W('01,3234', 0o63523, '', 'BZMF', 'WAITPOOH', line=206)

W('01,3235', 0o40026, '', 'CS', 'TIME3', line=208)
W('01,3236', 0o64744, '', 'AD', 'BIT8', 'BIT 8 = OCT 200', line=209)
W('01,3237', 0o10000, '', 'CCS', 'A', 'TEST 200 - C(TIME3).  IF POSITIVE,', line=210)
# IT MEANS THAT TIME3 OVERFLOW HAS OCCURRED PRIOR TO CS TIME3 AND THAT
# C(TIME3) = T - T1, INSTEAD OF 1.0 - (T1 - T).  THE FOLLOWING FOUR
# ORDERS SET C(A) = TD - T1 + 1 IN EITHER CASE.

W('01,3240', 0o66107, '', 'AD', 'OCT40001', 'OVERFLOW HAS OCCURRED.  SET C(A) =', line=215)
W('01,3241', 0o40000, '', 'CS', 'A', 'T - T1 + 1.0 - 201', line=216)

# NORMAL CASE (C(A) NNZ) YIELDS SAME C(A):  -( -(1.0-(T1-T)) + 200) - 1

W('01,3242', 0o63370, '', 'AD', 'OCT40201', line=220)
W('01,3243', 0o60002, '', 'AD', 'Q', 'RESULT = TD - T1 + 1.', line=221)

W('01,3244', 0o10000, '', 'CCS', 'A', 'TEST TD - T1 + 1.', line=223)

W('01,3245', 0o61400, '', 'AD', 'LST1', 'IF TD - T1 POS, GO TO WTLST5 WITH', line=225)
W('01,3246', 0o13310, '', 'TCF', 'WTLST5', 'C(A) = (TD - T1) + C(LST1) = TD-T2+1', line=226)

W('01,3247', 0o13250, '', 'NOOP', line=228)
W('01,3250', 0o40002, '', 'CS', 'Q', line=229)

# NOTE THAT THIS PROGRAM SECTION IS NEVER ENTERED WHEN T-T1 G/E -1,
# SINCE TD-T1+1 = (TD-T) + (T-T1+1), AND DELTA T = TD-T G/E +1.  (G/E
# SYMBOL MEANS GREATER THAN OR EQUAL TO).  THUS THERE NEED BE NO CON-
# CERN OVER A PREVIOUS OR IMMINENT OVEFLOW OF TIME3 HERE.

W('01,3251', 0o64736, '', 'AD', 'POS1/2', 'WHEN TD IS NEXT, FORM QUANTITY', line=236)
W('01,3252', 0o64736, '', 'AD', 'POS1/2', '      1.0 - DELTA T = 1.0 - (TD - T)', line=237)
W('01,3253', 0o56026, '', 'XCH', 'TIME3', line=238)
W('01,3254', 0o64735, '', 'AD', 'NEGMAX', line=239)
W('01,3255', 0o60002, '', 'AD', 'Q', '1.0 - DELTAT T NOW COMPLETE.', line=240)
W('01,3256', 0o00006, '', 'EXTEND', '', 'ZERO INDEX Q.', line=241)
W('01,3257', 0o22007, '', 'QXCH', '7', '(ZQ)', line=242)

# Page 1123
W('01,3260', 0o57400, 'WTLST4', 'XCH', 'LST1', line=245)
W('01,3261', 0o57401, '', 'XCH', 'LST1 +1', line=246)
W('01,3262', 0o57402, '', 'XCH', 'LST1 +2', line=247)
W('01,3263', 0o57403, '', 'XCH', 'LST1 +3', line=248)
W('01,3264', 0o57404, '', 'XCH', 'LST1 +4', line=249)
W('01,3265', 0o57405, '', 'XCH', 'LST1 +5', line=250)
W('01,3266', 0o57406, '', 'XCH', 'LST1 +6', line=251)
W('01,3267', 0o57407, '', 'XCH', 'LST1 +7', line=252)

W('01,3270', 0o30063, '', 'CA', 'WAITADR', '(MINOR PART OF TASK CADR HAS BEEN IN L.)', line=254)
W('01,3271', 0o50002, '', 'INDEX', 'Q', line=255)
W('01,3272', 0o13273, '', 'TCF', '+1', line=256)

W('01,3273', 0o53411, '', 'DXCH', 'LST2', line=258)
W('01,3274', 0o53413, '', 'DXCH', 'LST2 +2', line=259)
W('01,3275', 0o53415, '', 'DXCH', 'LST2 +4', line=260)
W('01,3276', 0o53417, '', 'DXCH', 'LST2 +6', line=261)
W('01,3277', 0o53421, '', 'DXCH', 'LST2 +8D', line=262)
W('01,3300', 0o53423, '', 'DXCH', 'LST2 +10D', 'AT END, CHECK THAT C(LST2 +10) IS STD', line=263)
W('01,3301', 0o53425, '', 'DXCH', 'LST2 +12D', line=264)
W('01,3302', 0o53427, '', 'DXCH', 'LST2 +14D', line=265)
W('01,3303', 0o53431, '', 'DXCH', 'LST2 +16D', line=266)
W('01,3304', 0o65236, '', 'AD', 'ENDTASK', 'END ITEM, AS CHECK FOR EXCEEDING', line=267)
# THE LENGTH OF THE LIST.
W('01,3305', 0o00006, '', 'EXTEND', '', 'DUMMY TASK ADRES SHOULD BE IN FIXED-', line=269)
W('01,3306', 0o15215, '', 'BZF', 'LVWTLIST', 'FIXED SO ITS ADRES ALONE DISTINGUISHES', line=270)
W('01,3307', 0o13363, '', 'TCF', 'WTABORT', 'IT.', line=271)

# Page 1124
W('01,3310', 0o10000, 'WTLST5', 'CCS', 'A', 'TEST TD - T2 + 1', line=274)
W('01,3311', 0o61401, '', 'AD', 'LST1 +1', line=275)
W('01,3312', 0o13316, '', 'TCF', '+4', line=276)
W('01,3313', 0o64753, '', 'AD', 'ONE', line=277)
W('01,3314', 0o03374, '', 'TC', 'WTLST2', line=278)
W('01,3315', 0o00001, '', 'OCT', '1', kind='data', line=279)

W('01,3316', 0o10000, '', 'CCS', 'A', 'TEST TD - T3 + 1', line=281)
W('01,3317', 0o61402, '', 'AD', 'LST1 +2', line=282)
W('01,3320', 0o13324, '', 'TCF', '+4', line=283)
W('01,3321', 0o64753, '', 'AD', 'ONE', line=284)
W('01,3322', 0o03374, '', 'TC', 'WTLST2', line=285)
W('01,3323', 0o00002, '', 'OCT', '2', kind='data', line=286)

W('01,3324', 0o10000, '', 'CCS', 'A', 'TEST TD - T4 + 1', line=288)
W('01,3325', 0o61403, '', 'AD', 'LST1 +3', line=289)
W('01,3326', 0o13332, '', 'TCF', '+4', line=290)
W('01,3327', 0o64753, '', 'AD', 'ONE', line=291)
W('01,3330', 0o03374, '', 'TC', 'WTLST2', line=292)
W('01,3331', 0o00003, '', 'OCT', '3', kind='data', line=293)

W('01,3332', 0o10000, '', 'CCS', 'A', 'TEST TD - T5 + 1', line=295)
W('01,3333', 0o61404, '', 'AD', 'LST1 +4', line=296)
W('01,3334', 0o13340, '', 'TCF', '+4', line=297)
W('01,3335', 0o64753, '', 'AD', 'ONE', line=298)
W('01,3336', 0o03374, '', 'TC', 'WTLST2', line=299)
W('01,3337', 0o00004, '', 'OCT', '4', kind='data', line=300)

W('01,3340', 0o10000, '', 'CCS', 'A', 'TEST TD - T6 + 1', line=302)
W('01,3341', 0o61405, '', 'AD', 'LST1 +5', line=303)
W('01,3342', 0o13346, '', 'TCF', '+4', line=304)
W('01,3343', 0o64753, '', 'AD', 'ONE', line=305)
W('01,3344', 0o03374, '', 'TC', 'WTLST2', line=306)
W('01,3345', 0o00005, '', 'OCT', '5', kind='data', line=307)

W('01,3346', 0o10000, '', 'CCS', 'A', 'TEST TD - T7 + 1', line=309)
W('01,3347', 0o61406, '', 'AD', 'LST1 +6', line=310)
W('01,3350', 0o13354, '', 'TCF', '+4', line=311)
W('01,3351', 0o64753, '', 'AD', 'ONE', line=312)
W('01,3352', 0o03374, '', 'TC', 'WTLST2', line=313)
W('01,3353', 0o00006, '', 'OCT', '6', kind='data', line=314)

# Page 1125
W('01,3354', 0o10000, '', 'CCS', 'A', 'TEST TD - T2 + 1', line=317)
W('01,3355', 0o61407, '', 'AD', 'LST1 +7', line=318)
W('01,3356', 0o13362, '', 'TCF', '+4', line=319)
W('01,3357', 0o64753, '', 'AD', 'ONE', line=320)
W('01,3360', 0o03374, '', 'TC', 'WTLST2', line=321)
W('01,3361', 0o00007, '', 'OCT', '7', kind='data', line=322)

W('01,3362', 0o10000, '', 'CCS', 'A', line=324)
W('01,3363', 0o03371, 'WTABORT', 'TC', 'FILLED', line=325)
W('01,3364', 0o13365, '', 'NOOP', '', "CAN'T GET HERE", line=326)
W('01,3365', 0o64753, '', 'AD', 'ONE', line=327)
W('01,3366', 0o03374, '', 'TC', 'WTLST2', line=328)
W('01,3367', 0o00010, '', 'OCT', '10', kind='data', line=329)

W('01,3370', 0o40201, 'OCT40201', 'OCT', '40201', kind='data', line=331)

# Page 1126
W('01,3371', 0o52062, 'FILLED', 'DXCH', 'WAITEXIT', line=334)
W('01,3372', 0o05716, '', 'TC', 'BAILOUT1', 'NO ROOM IN THE INN', line=335)
W('01,3373', 0o01203, '', 'OCT', '01203', kind='data', line=336)

# Page 1127
# THE ENTRY TC WTLST2 JUST PRECEDING OCT N IS FOR T  LE TD LE T   -1.
# N           N+1
# (LE MEANS LESS THAN OR EQUAL TO).  AT ENTRY, C(A) = -(TD - T   + 1)
# N+1
# THE LST1 ENTRY -(T   -T +1) IS TO BE REPLACED BY -(TD - T  + 1), AND
# N+1  N                                 N
# THE ENTRY -(T   - TD + 1) IS TO BE INSERTED IMMEDIATELY FOLLOWING.
# N+1

W('01,3374', 0o54064, 'WTLST2', 'TS', 'WAITTEMP', 'C(A) = -(TD - T + 1)', line=348)
W('01,3375', 0o50002, '', 'INDEX', 'Q', line=349)
W('01,3376', 0o30000, '', 'CAF', '0', line=350)
W('01,3377', 0o54002, '', 'TS', 'Q', 'INDEX VALUE INTO Q.', line=351)

W('01,3400', 0o34753, '', 'CAF', 'ONE', line=353)
W('01,3401', 0o60064, '', 'AD', 'WAITTEMP', line=354)
W('01,3402', 0o50002, '', 'INDEX', 'Q', 'C(A) = -(TD - T ) + 1.', line=355)
W('01,3403', 0o27377, '', 'ADS', 'LST1 -1', '               N', line=356)

W('01,3404', 0o40064, '', 'CS', 'WAITTEMP', line=358)
W('01,3405', 0o50002, '', 'INDEX', 'Q', line=359)
W('01,3406', 0o13260, '', 'TCF', 'WTLST4', line=360)

# C(TIME3)        =       1.0 - (T1 - T)
#
# C(LST1)         =       - (T2 - T1) + 1
# C(LST1+1)       =       - (T3 - T2) + 1
# C(LST1+2)       =       - (T4 - T3) + 1
# C(LST1+3)       =       - (T5 - T4) + 1
# C(LST1+4)       =       - (T6 - T5) + 1
#
# C(LST2)         =       2CADR TASK1
# C(LST2+2)       =       2CADR TASK2
# C(LST2+4)       =       2CADR TASK3
# C(LST2+6)       =       2CADR TASK4
# C(LST2+8)       =       2CADR TASK5
# C(LST2+10)      =       2CADR TASK6

# Page 1128
# ENTERS HERE ON T3 RUPT TO DISPATCH WAITLISTED TASK.

W('01,3407', 0o00006, 'T3RUPT', 'EXTEND', line=380)
W('01,3410', 0o04007, '', 'ROR', 'SUPERBNK', 'READ CURRENT SUPERBANK VALUE AND', line=381)
W('01,3411', 0o54016, '', 'TS', 'BANKRUPT', 'SAVE WITH E AND F BANK VALUES.', line=382)
W('01,3412', 0o00006, '', 'EXTEND', line=383)
W('01,3413', 0o22012, '', 'QXCH', 'QRUPT', line=384)

W('01,3414', 0o34734, 'T3RUPT2', 'CAF', 'NEG1/2', 'DISPATCH WAITLIST TASK.', line=386)
W('01,3415', 0o57407, '', 'XCH', 'LST1 +7', line=387)
W('01,3416', 0o57406, '', 'XCH', 'LST1 +6', line=388)
W('01,3417', 0o57405, '', 'XCH', 'LST1 +5', line=389)
W('01,3420', 0o57404, '', 'XCH', 'LST1 +4', '1. MOVE UP LST1 CONTENTS, ENTERING', line=390)
W('01,3421', 0o57403, '', 'XCH', 'LST1 +3', '   A VALUE OF 1/2 +1 AT THE BOTTOM', line=391)
W('01,3422', 0o57402, '', 'XCH', 'LST1 +2', '   FOR T6-T5, CORRESPONDING TO THE', line=392)
W('01,3423', 0o57401, '', 'XCH', 'LST1 +1', '   INTERVAL 81.91 SEC FOR ENDTASK.', line=393)
W('01,3424', 0o57400, '', 'XCH', 'LST1', line=394)
W('01,3425', 0o64733, '', 'AD', 'POSMAX', '2. SET T3 = 1.0 - T2 - T USING LIST 1.', line=395)
W('01,3426', 0o26026, '', 'ADS', 'TIME3', "   SO T3 WON'T TICK DURING UPDATE.", line=396)
W('01,3427', 0o54734, '', 'TS', 'RUPTAGN', line=397)
W('01,3430', 0o44755, '', 'CS', 'ZERO', line=398)
W('01,3431', 0o54734, '', 'TS', 'RUPTAGN', 'SETS RUPTAGN TO +1 ON OVERFLOW.', line=399)

W('01,3432', 0o00006, '', 'EXTEND', '', 'DISPATCH TASK.', line=401)
W('01,3433', 0o45237, '', 'DCS', 'ENDTASK', line=402)
W('01,3434', 0o53431, '', 'DXCH', 'LST2 +16D', line=403)
W('01,3435', 0o53427, '', 'DXCH', 'LST2 +14D', line=404)
W('01,3436', 0o53425, '', 'DXCH', 'LST2 +12D', line=405)
W('01,3437', 0o53423, '', 'DXCH', 'LST2 +10D', line=406)
W('01,3440', 0o53421, '', 'DXCH', 'LST2 +8D', line=407)
W('01,3441', 0o53417, '', 'DXCH', 'LST2 +6', line=408)
W('01,3442', 0o53415, '', 'DXCH', 'LST2 +4', line=409)
W('01,3443', 0o53413, '', 'DXCH', 'LST2 +2', line=410)
W('01,3444', 0o53411, '', 'DXCH', 'LST2', line=411)

W('01,3445', 0o56001, '', 'XCH', 'L', line=413)
W('01,3446', 0o00006, '', 'EXTEND', line=414)
W('01,3447', 0o01007, '', 'WRITE', 'SUPERBNK', 'SET SUPERBANK FROM BBCON OF 2CADR', line=415)
W('01,3450', 0o56001, '', 'XCH', 'L', 'RESTORE TO L FOR DXCH Z.', line=416)
W('01,3451', 0o52006, '', 'DTCB', line=417)

# Page 1129
# RETURN, AFTER EXECUTION OF T3 OVERFLOW TASK:

#   BLOCK 02
#   COUNT* $$/WAIT
W('5261', 0o10734, 'TASKOVER', 'CCS', 'RUPTAGN', 'IF +1 RETURN TO T3RUPT, IF -0 RESUME.', line=424)
W('5262', 0o35220, '', 'CAF', 'WAITBB', line=425)
W('5263', 0o54006, '', 'TS', 'BBANK', line=426)
W('5264', 0o13414, '', 'TCF', 'T3RUPT2', 'DISPATCH NEXT TASK IF IT WAS DUE.', line=427)

W('5265', 0o30016, '', 'CA', 'BANKRUPT', line=429)
W('5266', 0o00006, '', 'EXTEND', line=430)
W('5267', 0o01007, '', 'WRITE', 'SUPERBNK', 'RESTORE SUPERBANK BEFORE RESUME IS DONE', line=431)

W('5270', 0o00006, 'RESUME', 'EXTEND', line=433)
W('5271', 0o22012, '', 'QXCH', 'QRUPT', line=434)
W('5272', 0o30016, 'NOQRSM', 'CA', 'BANKRUPT', line=435)
W('5273', 0o56006, '', 'XCH', 'BBANK', line=436)
W('5274', 0o52011, 'NOQBRSM', 'DXCH', 'ARUPT', line=437)
W('5275', 0o00003, '', 'RELINT', line=438)
W('5276', 0o50017, '', 'RESUME', line=439)

# Page 1130
# LONGCALL
# PROGRAM DESCRIPTION                           DATE -- 17 MARCH 1967
# PROGRAM WRITTEN BY W.H.VANDEVER               LOG SECTION WAITLIST
# MOD BY -- R. MELANSON TO ADD DOCUMENTATION    ASSEMBLY SUNDISK REV. 100
#
# FUNCTIONAL DESCRIPTION --
# LONGCALL IS CALLED WITH THE DELTA TIME ARRIVING IN A,L SCALED AS TIME2,TIME1 WITH THE 2CADR OF THE TASK
# IMMEDIATELY FOLLOWING THE TC LONGCALL.  FOR EXAMPLE, IT MIGHT BE DONE AS FOLLOWS WHERE TIMELOC IS THE NAME OF
# A DP REGISTER CONTAINING A DELTA TIME AND WHERE TASKTODO IS THE NAME OF THE LOCATION AT WHICH LONGCALL IS TO
# START.
# CALLING SEQUENCE --
# EXTEND
# DCA     TIMELOC
# TC      LONGCALL
# 2CADR   TASKTODO
# NORMAL EXIT MODE --
# 1)      TC      WAITLIST
# 2)      DTCB    (TC L+3 OF CALLING ROUTINE 1ST PASS THRU LONGCYCL)
# 3)      DTCB    (TO TASKOVER ON SUBSEQUENT PASSES THRU LONGCYCL)
# ALARM OR ABORT EXIT MODE --
# NONE
# OUTPUT --
# LONGTIME AND LONGTIME+1 = DELTA TIME
# LONGEXIT AND LONGEXIT+1 = RETURN 2CADR
# LONGCADR AND LONGCADR+1 = TASK 2CADR
# A = SINGLE PRECISION TIME FOR WAITLIST
# ERASABLE INITIALIZATION --
# A = MOST SIGNIFICANT PART OF DELTA TIME
# L = LEAST SIGNIFICANT PART OF DELTA TIME
# Q = ADDRESS OF 2CADR TASK VALUE
# DEBRIS --
# A,Q,L
# LONGCADR AND LONGCADR+1
# LONGEXIT AND LONGEXIT+1
# LONGTIME AND LONGTIME+1
# *** THE FOLLOWING IS TO BE IN FIXED-FIXED AND UNSWITCHED ERRASIBLE **

#   BLOCK 02
#   EBANK= LST1
W('5277', 0o53154, 'LONGCALL', 'DXCH', 'LONGTIME', 'OBTAIN THE DELTA TIME', line=481)

W('5300', 0o00006, '', 'EXTEND', '', 'OBTAIN THE 2CADR', line=483)
# Page 1131
W('5301', 0o50002, '', 'NDX', 'Q', line=485)
W('5302', 0o30001, '', 'DCA', '0', line=486)
W('5303', 0o53150, '', 'DXCH', 'LONGCADR', line=487)

W('5304', 0o00006, '', 'EXTEND', '', 'NOW GO TO THE APPROPRIATE SWITCHED BANK', line=489)
W('5305', 0o35310, '', 'DCA', 'LGCL2CDR', 'FOR THE REST OF LONGCALL', line=490)
W('5306', 0o52006, '', 'DTCB', line=491)

#   EBANK= LST1
W('5307', 0o03452, 'LGCL2CDR', '2CADR', 'LNGCALL2', kind='data', line=494)
W('5310', 0o02063, kind='data', line=494)

# *** THE FOLLOWING MAY BE IN A SWITCHED BANK, INCLUDING ITS ERASABLE ***

#   BANK 01
#   COUNT* $$/WAIT
W('01,3452', 0o23435, 'LNGCALL2', 'LXCH', 'LONGEXIT +1', 'SAVE THE CORRECT BB FOR RETURN', line=500)
W('01,3453', 0o34752, '', 'CA', 'TWO', 'OBTAIN THE RETURN ADDRESS', line=501)
W('01,3454', 0o26002, '', 'ADS', 'Q', line=502)
W('01,3455', 0o55434, '', 'TS', 'LONGEXIT', line=503)

W('01,3456', 0o31153, '', 'CA', 'LONGTIME', 'CHECK FOR LEGITIMATE DELTA-TIME', line=505)
W('01,3457', 0o10000, '', 'CCS', 'A', line=506)
W('01,3460', 0o13466, '', 'TCF', 'LONGCYCL', 'HI-ORDER OK --> ALL IS OK.', line=507)
W('01,3461', 0o13463, '', 'TCF', '+2', 'HI-ORDER ZERO --> CHECK LO-ORDER.', line=508)
W('01,3462', 0o13521, '', 'TCF', 'LONGPOOH', 'HI-ORDER NEG. --> NEG. DT', line=509)
W('01,3463', 0o31154, '', 'CA', 'LONGTIME +1', 'CHECK LO-ORDER FOR ZERO OR NEGATIVE.', line=510)
W('01,3464', 0o00006, '', 'EXTEND', line=511)
W('01,3465', 0o63521, '', 'BZMF', 'LONGPOOH', 'BAD DELTA-TIME.  ABORT', line=512)

# *** WAITLIST TASK LONGCYCL ***

W('01,3466', 0o00006, 'LONGCYCL', 'EXTEND', '', 'CAN WE SUCCESFULLY TAKE ABOUT 1.25', line=516)
W('01,3467', 0o43500, '', 'DCS', 'DPBIT14', 'MINUTES OFF OF LONGTIME', line=517)
W('01,3470', 0o21154, '', 'DAS', 'LONGTIME', line=518)

W('01,3471', 0o11154, '', 'CCS', 'LONGTIME +1', 'THE REASONING BEHIND THIS PART IS', line=520)
W('01,3472', 0o13511, '', 'TCF', 'MUCHTIME', 'INVOLVED, TAKING INTO ACCOUNT THAT THE', line=521)
# WORDS MAY NOT BE SIGNED CORRECTED (DP
# BASIC INSTRUCTIONS
# DO NOT SIGN CORRECT) AND THAT WE SUBTRAC-
# TED BIT14 (1 OVER HALF THE POS. VALUE
# REPRESENTABLE IN SINGLE WORD)
W('01,3473', 0o13474, '', 'NOOP', '', "CAN'T GET HERE *************", line=527)
W('01,3474', 0o13475, '', 'TCF', '+1', line=528)
W('01,3475', 0o11153, '', 'CCS', 'LONGTIME', line=529)
W('01,3476', 0o13511, '', 'TCF', 'MUCHTIME', line=530)
W('01,3477', 0o00000, 'DPBIT14', 'OCT', '00000', kind='data', line=531)
W('01,3500', 0o20000, '', 'OCT', '20000', kind='data', line=532)

# LONGCALL
# Page 1132
W('01,3501', 0o34736, 'LASTTIME', 'CA', 'BIT14', 'GET BACK THE CORRECT DELTA T FOR WAITLIST', line=536)
W('01,3502', 0o27154, '', 'ADS', 'LONGTIME +1', line=537)
W('01,3503', 0o05203, '', 'TC', 'WAITLIST', line=538)
#   EBANK= LST1
W('01,3504', 0o03516, '', '2CADR', 'GETCADR', 'THE ENTRY TO OUR LONGCADR', kind='data', line=540)
W('01,3505', 0o02063, kind='data', line=540)

W('01,3506', 0o33520, 'LONGRTRN', 'CA', 'TSKOVCDR', 'SET IT UP SO THAT ONLY THE FIRST EXIT IS', line=542)
W('01,3507', 0o53435, '', 'DXCH', 'LONGEXIT', 'TO THE CALLER OF LONGCALL', line=543)
W('01,3510', 0o52006, '', 'DTCB', '', 'THE REST ARE TO TASKOVER', line=544)

W('01,3511', 0o34736, 'MUCHTIME', 'CA', 'BIT14', 'WE HAVE OVER OUR ABOUT 1.25 MINUTES', line=546)
W('01,3512', 0o05203, '', 'TC', 'WAITLIST', 'SO SET UP FOR ANOTHER CYCLE THROUGH HERE', line=547)
#   EBANK= LST1
W('01,3513', 0o03466, '', '2CADR', 'LONGCYCL', kind='data', line=549)
W('01,3514', 0o02063, kind='data', line=549)

W('01,3515', 0o13506, '', 'TCF', 'LONGRTRN', 'NOW EXIT PROPERLY', line=551)

# *** WAITLIST TASK GETCADR ***

W('01,3516', 0o53150, 'GETCADR', 'DXCH', 'LONGCADR', 'GET THE LONGCALL THAT WE WISHED TO START', line=555)
W('01,3517', 0o52006, '', 'DTCB', '', 'AND TRANSFER CONTROL TO IT', line=556)

W('01,3520', 0o05261, 'TSKOVCDR', 'GENADR', 'TASKOVER', kind='data', line=558)
W('01,3521', 0o53435, 'LONGPOOH', 'DXCH', 'LONGEXIT', line=559)
W('01,3522', 0o13524, '', 'TCF', '+2', line=560)
W('01,3523', 0o52062, 'WAITPOOH', 'DXCH', 'WAITEXIT', line=561)
W('01,3524', 0o05726, '', 'TC', 'POODOO1', line=562)
W('01,3525', 0o01204, '', 'OCT', '01204', kind='data', line=563)
