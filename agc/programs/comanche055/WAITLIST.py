"""WAITLIST.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/WAITLIST.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1221-1235 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('WAITLIST', 'WAITLIST.agc', 'Comanche055', pages='1221-1235')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     WAITLIST.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1221-1235
# Mod history:  2009-05-14 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
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

# Page 1221
# PROGRAM DESCRIPTION                                           DATE - 10 OCTOBER 1966
# MOD NO - 2                                                    LOG SECTION - WAITLIST
# MOD BY - MILLER       (DTMAX INCREASED TO 162.5 SEC)          ASSEMBLY SUNBURST REV 5
# MOD 3 BY KERNAN       (INHINT INSERTED AT WAITLIST) 2/28/68 SKIPPER REV 4
# MOD 4BY KERNAN        (TWIDDLE IN 54) 3/28/68 SKIPPER REV 13.
#
# FUNCTIONAL DESCRIPTION-
# PART OF A SECTION OF PROGRAMS,-WAITLIST, TASKOVER, T3RUPT, USED TO CALL A PROGRAM, (CALLED A TASK),
# WHICH IS TO BEGIN IN C(A) CENTISECONDS.  WAITLIST UPDATES TIME3, LST1 AND LST2. THE MEANING OF THESE LISTS
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
# WARNINGS-
# --------
# 1)      1 <= C(A) <= 16250D (1 CENTISECOND TO 162.5 SEC)
# 2)      9 TASKS MAXIMUM
# 3)      TASKS CALLED UNDER INTERRUPT INHIBITED
# 4)      TASKS END BY TC TASKOVER
#
# CALLING SEQUENCE-
#
# L-1     CA      DELTAT  (TIME IN CENTISECONDS TO TASK START)
# L       TC      WAITLIST
# L+1     2CADR   DESIRED TASK
# L+2     (MINOR OF 2CADR)
# L+3     RELINT          (RETURNS HERE)
#
# TWIDDLE-
# -------
# TWIDDLE IS FOR USE WHEN THE TASK BEING SET UP IS IN THE SAME EBANK AND FBANK AS THE USER.  IN
# SUCH CASES, IT IMPROVES UPON WAITLIST BY ELIMINATING THE NEED FOR THE BBCON HALF OF THE 2CADR,
# Page 1222
# SAVING A WORD.  TWIDDLE IS LIKE WAITLIST IN EVERY RESPECT EXCEPT CALLING SEQUENCE, TO WIT-
#
# L-1     CA      DELTAT
# L       TC      TWIDDLE
# L+1     ADRES   DESIRED TASK
# L+2     RELINT          (RETURNS HERE)
#
# NORMAL EXIT MODES-
#
# AT L+3 OF CALLING SEQUENCE
#
# ALARM OR ABORT EXIT MODES-
#
# TC      ABORT
# OCT     1203    (WAITLIST OVERFLOW - TOO MANY TASKS)
#
# ERASABLE INITIALIZATION REQUIRED-
#
# ACCOMPLISHED BY FRESH START,--  LST2,..., LST2 +16 =ENDTASK
# LST1,..., LST1 +7  =NEG1/2
#
# OUTPUT--
#
# LST1 AND LST2 UPDATED WITH NEW TASK AND ASSOCIATED TIME.
# DEBRIS-
# CENTRALS- A,Q,L
# OTHER   - WAITEXIT, WAITADR, WAITTEMP, WAITBANK
# DETAILED ANALYSIS OF TIMING-
#
# CONTROL WILL NOT BE RETURNED TO THE SPECIFIED ADDRESS (2CADR) IN EXACTLY DELTA T CENTISECONDS.
# THE APPROXIMATE TIME MAY BE CALCULATED AS FOLLOWS
#
# LET T0 = THE TIME OF THE TC WAITLIST
# LET TS = T0 +147U + COUNTER INCREMENTS (SET UP TIME)
# LET X  = TS -(100TS)/100  (VARIANCE FROM COUNTERS)
# LET Y  = LENGTH OF TIME OF INHIBIT INTERRUPT AFTER T3RUPT
# LET Z  = LENGTH OF TIME TO PROCESS TASKS WHICH ARE DUE THIS T3RUPT BUT DISPATCHED EARLIER.
# (Z=0, USUALLY)
# LET DELTD = THE ACTUAL TIME TAKEN TO GIVE CONTROL TO 2CADR
# THEN DELTD = TS+DELTA T -X +Y +Z +1.05MS* +COUNTERS*
# *THE TIME TAKEN BY WAITLIST ITSELF AND THE COUNTER TICKING DURING THIS WAITLIST TIME.
#
# IN SHORT, THE ACTUAL TIME TO RETURN CONTROL TO A 2CADR IS AUGMENTED BY THE TIME TO SET UP THE TASK'S
# INTERRUPT, ALL COUNTERS TICKING, THE T3RUPT PROCESSING TIME, THE WAITLIST PROCESSING TIME AND THE POSSIBILITY
# OF OTHER TASKS INHIBITING THE INTERRUPT.

#   BLOCK 02
# Page 1223
#   EBANK= LST1  # TASK LISTS IN SWITCHED E BANK.

#   COUNT 02/WAIT

W('5235', 0o00004, 'TWIDDLE', 'INHINT', line=129)
W('5236', 0o54001, '', 'TS', 'L', 'SAVE DELAY TIME IN L', line=130)
W('5237', 0o34777, '', 'CA', 'POSMAX', line=131)
W('5240', 0o26002, '', 'ADS', 'Q', 'CREATING OVERFLOW AND Q-1 IN Q', line=132)
W('5241', 0o30006, '', 'CA', 'BBANK', line=133)
W('5242', 0o00006, '', 'EXTEND', line=134)
W('5243', 0o04007, '', 'ROR', 'SUPERBNK', line=135)
W('5244', 0o56001, '', 'XCH', 'L', line=136)

W('5245', 0o00004, 'WAITLIST', 'INHINT', line=138)
W('5246', 0o00006, '', 'EXTEND', line=139)
W('5247', 0o65261, '', 'BZMF', 'WATLST0-', line=140)
W('5250', 0o56002, '', 'XCH', 'Q', 'SAVE DELTA T IN Q AND RETURN IN', line=141)
W('5251', 0o54061, '', 'TS', 'WAITEXIT', 'WAITEXIT.', line=142)
W('5252', 0o00006, '', 'EXTEND', line=143)
W('5253', 0o50061, '', 'INDEX', 'WAITEXIT', 'IF TWIDDLING, THE TS SKIPS TO HERE', line=144)
W('5254', 0o30001, '', 'DCA', '0', 'PICK UP 2CADR OF TASK.', line=145)
W('5255', 0o54063, '', 'TS', 'WAITADR', 'BBCON WILL REMAIN IN L', line=146)
W('5256', 0o35266, 'DLY2', 'CAF', 'WAITBB', 'ENTRY FROM FIXDELAY AND VARDELAY.', line=147)
W('5257', 0o56006, '', 'XCH', 'BBANK', line=148)
W('5260', 0o13246, '', 'TCF', 'WAIT2', line=149)

W('5261', 0o05721, 'WATLST0-', 'TC', 'POODOO', line=151)
W('5262', 0o01204, '', 'OCT', '1204', 'WAITLIST CALL WITH ZERO OR NEG DT', kind='data', line=152)

# RETURN TO CALLER AFTER TASK INSERTION:

W('5263', 0o52062, 'LVWTLIST', 'DXCH', 'WAITEXIT', line=156)
W('5264', 0o65016, '', 'AD', 'TWO', line=157)
W('5265', 0o52006, '', 'DTCB', line=158)

#   EBANK= LST1
W('5266', 0o02063, 'WAITBB', 'BBCON', 'WAIT2', kind='data', line=161)

# RETURN TO CALLER +2 AFTER WAITING DT SPECIFIED AT CALLER +1.

W('5267', 0o50002, 'FIXDELAY', 'INDEX', 'Q', 'BOTH ROUTINES MUST BE CALLED UNDER', line=165)
W('5270', 0o30000, '', 'CAF', '0', 'WAITLIST CONTROL AND TERMINATE THE TASK', line=166)
W('5271', 0o24002, '', 'INCR', 'Q', 'IN WHICH THEY WERE CALLED.', line=167)

# RETURN TO CALLER +1 AFTER WAITING THE DT AS ARRIVING IN A.

W('5272', 0o56002, 'VARDELAY', 'XCH', 'Q', 'DT TO Q.  TASK ADRES TO WAITADR.', line=171)
W('5273', 0o54063, '', 'TS', 'WAITADR', line=172)
W('5274', 0o30006, '', 'CA', 'BBANK', 'BBANK IS SAVED DURING DELAY.', line=173)
W('5275', 0o00006, '', 'EXTEND', line=174)
# Page 1224
W('5276', 0o04007, '', 'ROR', 'SUPERBNK', 'ADD SBANK TO BBCON.', line=176)
W('5277', 0o54001, '', 'TS', 'L', line=177)
W('5300', 0o35303, '', 'CAF', 'DELAYEX', line=178)
W('5301', 0o54061, '', 'TS', 'WAITEXIT', 'GO TO TASKOVER AFTER TASK ENTRY.', line=179)
W('5302', 0o15256, '', 'TCF', 'DLY2', line=180)

W('5303', 0o15322, 'DELAYEX', 'TCF', 'TASKOVER -2', 'RETURNS TO TASKOVER', line=182)

# Page 1225
# ENDTASK MUST ENTERED IN FIXED-FIXED SO IT IS DISTINGUISHABLE BY ITS ADRES ALONE.

#   EBANK= LST1
W('5304', 0o72471, 'ENDTASK', '-2CADR', 'SVCT3', kind='data', line=188)
W('5305', 0o73714, kind='data', line=188)

W('5306', 0o10076, 'SVCT3', 'CCS', 'FLAGWRD2', 'DRIFT FLAG', line=191)
W('5307', 0o15324, '', 'TCF', 'TASKOVER', line=192)
W('5310', 0o15324, '', 'TCF', 'TASKOVER', line=193)
W('5311', 0o15312, '', 'TCF', '+1', line=194)

W('5312', 0o11322, '', 'CCS', 'IMUCADR', "DON'T DO NBDONLY IF SOMEONE ELSE IS IN", line=196)
W('5313', 0o17717, '', 'TCF', 'SVCT3X', line=197)
W('5314', 0o15317, '', 'TCF', '+3', line=198)
W('5315', 0o17717, '', 'TCF', 'SVCT3X', line=199)
W('5316', 0o17717, '', 'TCF', 'SVCT3X', line=200)
W('5317', 0o37672, '', 'CAF', 'PRIO35', 'COMPENSATE FOR NBD COEFFICIENTS ONLY.', line=201)
W('5320', 0o05134, '', 'TC', 'NOVAC', '      ENABLE EVERY 81.93 SECONDS', line=202)
#   EBANK= NBDX
W('5321', 0o03542, '', '2CADR', 'NBDONLY', kind='data', line=204)
W('5322', 0o14063, kind='data', line=204)

W('5323', 0o15324, '', 'TCF', 'TASKOVER', line=206)

#   SETLOC FFTAG6
#   BANK

W('7717', 0o05267, 'SVCT3X', 'TC', 'FIXDELAY', 'DELAY MAX OF 2 TIMES FOR IMU ZERO', line=211)
W('7720', 0o00764, '', 'DEC', '500', kind='data', line=212)
W('7721', 0o05306, '', 'TC', 'SVCT3', 'CHECK DRIFT FLAG AGAIN', line=213)

# Page 1226
# BEGIN TASK INSERTION.

#   BANK 01
#   COUNT 01/WAIT

W('01,3246', 0o54062, 'WAIT2', 'TS', 'WAITBANK', 'BBANK OF CALLING PROGRAM.', line=221)
W('01,3247', 0o40026, '', 'CS', 'TIME3', line=222)
W('01,3250', 0o65010, '', 'AD', 'BIT8', 'BIT 8 = OCT 200', line=223)
W('01,3251', 0o10000, '', 'CCS', 'A', 'TEST 200 - C(TIME3).  IF POSITIVE,', line=224)
# IT MEANS THAT TIME3 OVERFLOW HAS OCCURRED PRIOR TO CS TIME3 AND THAT
# C(TIME3) = T - T1, INSTEAD OF 1.0 - (T1 - T).  THE FOLLOWING FOUR
# ORDERS SET C(A) = TD - T1 + 1 IN EITHER CASE.

W('01,3252', 0o66056, '', 'AD', 'OCT40001', 'OVERFLOW HAS OCCURRED.  SET C(A) =', line=229)
W('01,3253', 0o40000, '', 'CS', 'A', 'T - T1 + 1.0 - 201', line=230)

# NORMAL CASE (C(A) NNZ) YIELDS SAME C(A):  -( -(1.0-(T1-T)) + 200) - 1

W('01,3254', 0o63402, '', 'AD', 'OCT40201', line=234)
W('01,3255', 0o60002, '', 'AD', 'Q', 'RESULT = TD - T1 + 1.', line=235)

W('01,3256', 0o10000, '', 'CCS', 'A', 'TEST TD - T1 + 1', line=237)

W('01,3257', 0o61400, '', 'AD', 'LST1', 'IF TD - T1 POS, GO TO WTLST5 WITH', line=239)
W('01,3260', 0o13322, '', 'TCF', 'WTLST5', 'C(A) = (TD - T1) + C(LST1) = TD-T2+1', line=240)

W('01,3261', 0o13262, '', 'NOOP', line=242)
W('01,3262', 0o40002, '', 'CS', 'Q', line=243)

# NOTE THAT THIS PROGRAM SECTION IS NEVER ENTERED WHEN T-T1 G/E -1,
# SINCE TD-T1+1 = (TD-T) + (T-T1+1), AND DELTA T = TD-T G/E +1.  (G/E
# SYMBOL MEANS GREATER THAN OR EQUAL TO).  THUS THERE NEED BE NO CON-
# CERN OVER A PREVIOUS OR IMMINENT OVERFLOW OF TIME3 HERE.

W('01,3263', 0o65002, '', 'AD', 'POS1/2', 'WHEN TD IS NEXT, FORM QUANTITY', line=250)
W('01,3264', 0o65002, '', 'AD', 'POS1/2', '      1.0 - DELTA T = 1.0 - (TD - T)', line=251)
W('01,3265', 0o56026, '', 'XCH', 'TIME3', line=252)
W('01,3266', 0o65001, '', 'AD', 'NEGMAX', line=253)
W('01,3267', 0o60002, '', 'AD', 'Q', '1.0 - DELTAT T NOW COMPLETE.', line=254)
W('01,3270', 0o00006, '', 'EXTEND', '', 'ZERO INDEX Q.', line=255)
W('01,3271', 0o22007, '', 'QXCH', '7', '(ZQ)', line=256)

# Page 1227
W('01,3272', 0o57400, 'WTLST4', 'XCH', 'LST1', line=259)
W('01,3273', 0o57401, '', 'XCH', 'LST1 +1', line=260)
W('01,3274', 0o57402, '', 'XCH', 'LST1 +2', line=261)
W('01,3275', 0o57403, '', 'XCH', 'LST1 +3', line=262)
W('01,3276', 0o57404, '', 'XCH', 'LST1 +4', line=263)
W('01,3277', 0o57405, '', 'XCH', 'LST1 +5', line=264)
W('01,3300', 0o57406, '', 'XCH', 'LST1 +6', line=265)
W('01,3301', 0o57407, '', 'XCH', 'LST1 +7', line=266)

W('01,3302', 0o30063, '', 'CA', 'WAITADR', '(MINOR PART OF TASK CADR HAS BEEN IN L.)', line=268)
W('01,3303', 0o50002, '', 'INDEX', 'Q', line=269)
W('01,3304', 0o13305, '', 'TCF', '+1', line=270)

W('01,3305', 0o53411, '', 'DXCH', 'LST2', line=272)
W('01,3306', 0o53413, '', 'DXCH', 'LST2 +2', line=273)
W('01,3307', 0o53415, '', 'DXCH', 'LST2 +4', line=274)
W('01,3310', 0o53417, '', 'DXCH', 'LST2 +6', line=275)
W('01,3311', 0o53421, '', 'DXCH', 'LST2 +8D', line=276)
W('01,3312', 0o53423, '', 'DXCH', 'LST2 +10D', 'AT END, CHECK THAT C(LST2 +10) IS STD', line=277)
W('01,3313', 0o53425, '', 'DXCH', 'LST2 +12D', line=278)
W('01,3314', 0o53427, '', 'DXCH', 'LST2 +14D', line=279)
W('01,3315', 0o53431, '', 'DXCH', 'LST2 +16D', line=280)
W('01,3316', 0o65304, '', 'AD', 'ENDTASK', 'END ITEM, AS CHECK FOR EXCEEDING', line=281)
# THE LENGTH OF THE LIST.
W('01,3317', 0o00006, '', 'EXTEND', '', 'DUMMY TASK ADRES SHOULD BE IN FIXED-', line=283)
W('01,3320', 0o15263, '', 'BZF', 'LVWTLIST', 'FIXED SO ITS ADRES ALONE DISTINGUISHES', line=284)
W('01,3321', 0o13375, '', 'TCF', 'WTABORT', 'IT.', line=285)

# Page 1228
W('01,3322', 0o10000, 'WTLST5', 'CCS', 'A', 'TEST TD - T2 + 1', line=288)
W('01,3323', 0o61401, '', 'AD', 'LST1 +1', line=289)
W('01,3324', 0o13330, '', 'TCF', '+4', line=290)
W('01,3325', 0o65017, '', 'AD', 'ONE', line=291)
W('01,3326', 0o03403, '', 'TC', 'WTLST2', line=292)
W('01,3327', 0o00001, '', 'OCT', '1', kind='data', line=293)

W('01,3330', 0o10000, '', 'CCS', 'A', 'TEST TD - T3 + 1', line=295)
W('01,3331', 0o61402, '', 'AD', 'LST1 +2', line=296)
W('01,3332', 0o13336, '', 'TCF', '+4', line=297)
W('01,3333', 0o65017, '', 'AD', 'ONE', line=298)
W('01,3334', 0o03403, '', 'TC', 'WTLST2', line=299)
W('01,3335', 0o00002, '', 'OCT', '2', kind='data', line=300)

W('01,3336', 0o10000, '', 'CCS', 'A', 'TEST TD - T4 + 1', line=302)
W('01,3337', 0o61403, '', 'AD', 'LST1 +3', line=303)
W('01,3340', 0o13344, '', 'TCF', '+4', line=304)
W('01,3341', 0o65017, '', 'AD', 'ONE', line=305)
W('01,3342', 0o03403, '', 'TC', 'WTLST2', line=306)
W('01,3343', 0o00003, '', 'OCT', '3', kind='data', line=307)

W('01,3344', 0o10000, '', 'CCS', 'A', 'TEST TD - T5 + 1', line=309)
W('01,3345', 0o61404, '', 'AD', 'LST1 +4', line=310)
W('01,3346', 0o13352, '', 'TCF', '+4', line=311)
W('01,3347', 0o65017, '', 'AD', 'ONE', line=312)
W('01,3350', 0o03403, '', 'TC', 'WTLST2', line=313)
W('01,3351', 0o00004, '', 'OCT', '4', kind='data', line=314)

W('01,3352', 0o10000, '', 'CCS', 'A', 'TEST TD - T6 + 1', line=316)
W('01,3353', 0o61405, '', 'AD', 'LST1 +5', line=317)
W('01,3354', 0o13360, '', 'TCF', '+4', line=318)
W('01,3355', 0o65017, '', 'AD', 'ONE', line=319)
W('01,3356', 0o03403, '', 'TC', 'WTLST2', line=320)
W('01,3357', 0o00005, '', 'OCT', '5', kind='data', line=321)

W('01,3360', 0o10000, '', 'CCS', 'A', 'TEST TD - T7 + 1', line=323)
W('01,3361', 0o61406, '', 'AD', 'LST1 +6', line=324)
W('01,3362', 0o13366, '', 'TCF', '+4', line=325)
W('01,3363', 0o65017, '', 'AD', 'ONE', line=326)
W('01,3364', 0o03403, '', 'TC', 'WTLST2', line=327)
W('01,3365', 0o00006, '', 'OCT', '6', kind='data', line=328)

# Page 1229
W('01,3366', 0o10000, '', 'CCS', 'A', line=331)
W('01,3367', 0o61407, '', 'AD', 'LST1 +7', line=332)
W('01,3370', 0o13374, '', 'TCF', '+4', line=333)
W('01,3371', 0o65017, '', 'AD', 'ONE', line=334)
W('01,3372', 0o03403, '', 'TC', 'WTLST2', line=335)
W('01,3373', 0o00007, '', 'OCT', '7', kind='data', line=336)

W('01,3374', 0o10000, '', 'CCS', 'A', line=338)
W('01,3375', 0o07755, 'WTABORT', 'TC', 'BAILOUT', 'NO ROOM IN THE INN.', line=339)
W('01,3376', 0o01203, '', 'OCT', '1203', kind='data', line=340)

W('01,3377', 0o65017, '', 'AD', 'ONE', line=342)
W('01,3400', 0o03403, '', 'TC', 'WTLST2', line=343)
W('01,3401', 0o00010, '', 'OCT', '10', kind='data', line=344)

W('01,3402', 0o40201, 'OCT40201', 'OCT', '40201', kind='data', line=346)

# Page 1230
# THE ENTRY TO WTLST2 JUST PRECEDING OCT N IS FOR T  LE TD LE T   -1.
# N           N+1
#
# (LE MEANS LESS THAN OR EQUAL TO).  AT ENTRY, C(A) = -(TD - T   + 1)
# N+1
#
# THE LST1 ENTRY-(T   -T +1) IS TO BE REPLACED BY -(TD - T  + 1), AND
# N+1  N                                 N
#
# THE ENTRY-(T   - TD + 1) IS TO BE INSERTED IMMEDIATELY FOLLOWING.
# N+1

W('01,3403', 0o54064, 'WTLST2', 'TS', 'WAITTEMP', '      C(A) = -(TD - T + 1)', line=361)
W('01,3404', 0o50002, '', 'INDEX', 'Q', line=362)
W('01,3405', 0o30000, '', 'CAF', '0', line=363)
W('01,3406', 0o54002, '', 'TS', 'Q', 'INDEX VALUE INTO Q.', line=364)

W('01,3407', 0o35017, '', 'CAF', 'ONE', line=366)
W('01,3410', 0o60064, '', 'AD', 'WAITTEMP', line=367)
W('01,3411', 0o50002, '', 'INDEX', 'Q', 'C(A) = -(TD - T ) + 1.', line=368)
W('01,3412', 0o27377, '', 'ADS', 'LST1 -1', '               N', line=369)

W('01,3413', 0o40064, '', 'CS', 'WAITTEMP', line=371)
W('01,3414', 0o50002, '', 'INDEX', 'Q', line=372)
W('01,3415', 0o13272, '', 'TCF', 'WTLST4', line=373)

# Page 1231
# ENTERS HERE ON T3 RUPT TO DISPATCH WAITLISTED TASK.

W('01,3416', 0o00006, 'T3RUPT', 'EXTEND', line=378)
W('01,3417', 0o04007, '', 'ROR', 'SUPERBNK', 'READ CURRENT SUPERBANK VALUE AND', line=379)
W('01,3420', 0o54016, '', 'TS', 'BANKRUPT', 'SAVE WITH E AND F BANK VALUES.', line=380)
W('01,3421', 0o00006, '', 'EXTEND', line=381)
W('01,3422', 0o22012, '', 'QXCH', 'QRUPT', line=382)

W('01,3423', 0o35000, 'T3RUPT2', 'CAF', 'NEG1/2', 'DISPATCH WAITLIST TASK.', line=384)
W('01,3424', 0o57407, '', 'XCH', 'LST1 +7', line=385)
W('01,3425', 0o57406, '', 'XCH', 'LST1 +6', line=386)
W('01,3426', 0o57405, '', 'XCH', 'LST1 +5', line=387)
W('01,3427', 0o57404, '', 'XCH', 'LST1 +4', '1. MOVE UP LST1 CONTENTS, ENTERING', line=388)
W('01,3430', 0o57403, '', 'XCH', 'LST1 +3', '   A VALUE OF 1/2 +1 AT THE BOTTOM', line=389)
W('01,3431', 0o57402, '', 'XCH', 'LST1 +2', '   FOR T6-T5, CORRESPONDING TO THE', line=390)
W('01,3432', 0o57401, '', 'XCH', 'LST1 +1', '   INTERVAL 81.91 SEC FOR ENDTASK.', line=391)
W('01,3433', 0o57400, '', 'XCH', 'LST1', line=392)
W('01,3434', 0o64777, '', 'AD', 'POSMAX', '2. SET T3 = 1.0 - T2 - T USING LIST 1.', line=393)
W('01,3435', 0o26026, '', 'ADS', 'TIME3', '   SO T3 WONT TICK DURING UPDATE.', line=394)
W('01,3436', 0o54734, '', 'TS', 'RUPTAGN', line=395)
W('01,3437', 0o45021, '', 'CS', 'ZERO', line=396)
W('01,3440', 0o54734, '', 'TS', 'RUPTAGN', 'SETS RUPTAGN TO +1 ON OVERFLOW.', line=397)

W('01,3441', 0o00006, '', 'EXTEND', '', 'DISPATCH TASK.', line=399)
W('01,3442', 0o45305, '', 'DCS', 'ENDTASK', line=400)
W('01,3443', 0o53431, '', 'DXCH', 'LST2 +16D', line=401)
W('01,3444', 0o53427, '', 'DXCH', 'LST2 +14D', line=402)
W('01,3445', 0o53425, '', 'DXCH', 'LST2 +12D', line=403)
W('01,3446', 0o53423, '', 'DXCH', 'LST2 +10D', line=404)
W('01,3447', 0o53421, '', 'DXCH', 'LST2 +8D', line=405)
W('01,3450', 0o53417, '', 'DXCH', 'LST2 +6', line=406)
W('01,3451', 0o53415, '', 'DXCH', 'LST2 +4', line=407)
W('01,3452', 0o53413, '', 'DXCH', 'LST2 +2', line=408)
W('01,3453', 0o53411, '', 'DXCH', 'LST2', line=409)

W('01,3454', 0o56001, '', 'XCH', 'L', line=411)
W('01,3455', 0o00006, '', 'EXTEND', line=412)
W('01,3456', 0o01007, '', 'WRITE', 'SUPERBNK', 'SET SUPERBANK FROM BBCON OF 2CADR', line=413)
W('01,3457', 0o56001, '', 'XCH', 'L', 'RESTORE TO L FOR DXCH Z.', line=414)
W('01,3460', 0o52006, '', 'DTCB', line=415)

# Page 1232
# RETURN, AFTER EXECUTION OF T3 OVERFLOW TASK:

#   BLOCK 02
#   COUNT 02/WAIT

W('5324', 0o10734, 'TASKOVER', 'CCS', 'RUPTAGN', 'IF +1 RETURN TO T3RUPT, IF -0 RESUME.', line=423)
W('5325', 0o35266, '', 'CAF', 'WAITBB', line=424)
W('5326', 0o54006, '', 'TS', 'BBANK', line=425)
W('5327', 0o13423, '', 'TCF', 'T3RUPT2', 'DISPATCH NEXT TASK IF IT WAS DUE.', line=426)

W('5330', 0o30016, '', 'CA', 'BANKRUPT', line=428)
W('5331', 0o00006, '', 'EXTEND', line=429)
W('5332', 0o01007, '', 'WRITE', 'SUPERBNK', 'RESTORE SUPERBANK BEFORE RESUME IS DONE', line=430)

W('5333', 0o00006, 'RESUME', 'EXTEND', line=432)
W('5334', 0o22012, '', 'QXCH', 'QRUPT', line=433)
W('5335', 0o30016, 'NOQRSM', 'CA', 'BANKRUPT', line=434)
W('5336', 0o56006, '', 'XCH', 'BBANK', line=435)
W('5337', 0o52011, 'NOQBRSM', 'DXCH', 'ARUPT', line=436)
W('5340', 0o00003, '', 'RELINT', line=437)
W('5341', 0o50017, '', 'RESUME', line=438)

# Page 1233
# LONGCALL
#
# PROGRAM DESCRIPTION                                 DATE- 17 MARCH 1967
# PROGRAM WRITTEN BY W.H. VANDEVER                   LOG SECTION WAITLIST
# MOD BY- R. MELANSON TO ADD DOCUMENTATION      ASSEMBLY SUNDISK REV. 100
#
# FUNCTIONAL DESCRIPTION-
# LONGCALL IS CALLED WITH THE DELTA TIME ARRIVING IN A,L SCALED AS TIME2,TIME1 WITH THE 2CADR OF THE TASK
# IMMEDIATELY FOLLOWING THE TC LONGCALL.  FOR EXAMPLE, IT MIGHT BE DONE AS FOLLOWS WHERE TIMELOC IS THE NAME OF
# A DP REGISTER CONTAINING A DELTA TIME AND WHERE TASKTODO IS THE NAME OF THE LOCATION AT WHICH LONGCALL IS TO
# START
#
# CALLING SEQUENCE-
# EXTEND
# DCA     TIMELOC
# TC      LONGCALL
# 2CADR   TASKTODO
#
# NORMAL EXIT MODE-
# 1). TC          WAITLIST
# 2). DTCB        (TC L+3 OF CALLING ROUTINE 1ST PASS THRU LONGCYCL)
# 3). DTCB        (TO TASKOVER ON SUBSEQUENT PASSES THRU LONGCYCL)
#
# ALARM OR ABORT EXIT MODE-
# NONE
#
# OUTPUT-
# LONGTIME AND LONGTIME+1 = DELTA TIME
# LONGEXIT AND LONGEXIT+1 = RETURN 2CADR
# LONGCADR AND LONGCADR+1 = TASK 2CADR
# A = SINGLE PRECISION TIME FOR WAITLIST
#
# ERASABLE INITIALIZATION-
# A = MOST SIGNIFICANT PART OF DELTA TIME
# L = LEAST SIGNIFICANT PART OF DELTA TIME
# Q = ADDRESS OF 2CADR TASK VALUE
#
# DEBRIS-
# A,Q,L
# LONGCADR AND LONGCADR+1
# LONGEXIT AND LONGEXIT+1
# LONGTIME AND LONGTIME+1
#
# *** THE FOLLOWING IS TO BE IN FIXED-FIXED AND UNSWITCHED ERRASIBLE ***

#   BLOCK 02
#   EBANK= LST1
W('5342', 0o53140, 'LONGCALL', 'DXCH', 'LONGTIME', 'OBTAIN THE DELTA TIME', line=488)

W('5343', 0o00006, '', 'EXTEND', '', 'OBTAIN THE 2CADR', line=490)
# Page 1234
W('5344', 0o50002, '', 'NDX', 'Q', line=492)
W('5345', 0o30001, '', 'DCA', '0', line=493)
W('5346', 0o53134, '', 'DXCH', 'LONGCADR', line=494)

W('5347', 0o00006, '', 'EXTEND', '', 'NOW GO TO THE APPROPRIATE SWITCHED BANK', line=496)
W('5350', 0o35353, '', 'DCA', 'LGCL2CDR', 'FOR THE REST OF LONGCALL', line=497)
W('5351', 0o52006, '', 'DTCB', line=498)

#   EBANK= LST1
W('5352', 0o03461, 'LGCL2CDR', '2CADR', 'LNGCALL2', kind='data', line=501)
W('5353', 0o02063, kind='data', line=501)

# *** THE FOLLOWING MAY BE IN A SWITCHED BANK, INCLUDING ITS ERASABLE ***

#   BANK 01
#   COUNT 01/WAIT

W('01,3461', 0o23435, 'LNGCALL2', 'LXCH', 'LONGEXIT +1', 'SAVE THE CORRECT BB FOR RETURN', line=508)
W('01,3462', 0o35016, '', 'CA', 'TWO', 'OBTAIN THE RETURN ADDRESS', line=509)
W('01,3463', 0o26002, '', 'ADS', 'Q', line=510)
W('01,3464', 0o55434, '', 'TS', 'LONGEXIT', line=511)

# *** WAITLIST TASK LONGCYCL ***
W('01,3465', 0o00006, 'LONGCYCL', 'EXTEND', '', 'CAN WE SUCCESFULLY TAKE ABOUT 1.25', line=514)
W('01,3466', 0o43477, '', 'DCS', 'DPBIT14', 'MINUTES OFF OF LONGTIME', line=515)
W('01,3467', 0o21140, '', 'DAS', 'LONGTIME', line=516)

W('01,3470', 0o11140, '', 'CCS', 'LONGTIME +1', 'THE REASONING BEHIND THIS PART IS', line=518)
W('01,3471', 0o13510, '', 'TCF', 'MUCHTIME', 'INVOLVED, TAKING INTO ACCOUNT THAT THE', line=519)
# WORDS MAY NOT BE SIGNED CORRECTED (DP
# BASIC INSTRUCTIONS
# DO NOT SIGN CORRECT) AND THAT WE SUBTRAC-
# TED BIT14 (1 OVER HALF THE POS. VALUE
# REPRESENTABLE IN SINGLE WORD)
W('01,3472', 0o13473, '', 'NOOP', '', "CAN'T GET HERE **********", line=525)
W('01,3473', 0o13474, '', 'TCF', '+1', line=526)
W('01,3474', 0o11137, '', 'CCS', 'LONGTIME', line=527)
W('01,3475', 0o13510, '', 'TCF', 'MUCHTIME', line=528)
W('01,3476', 0o00000, 'DPBIT14', 'OCT', '00000', kind='data', line=529)
W('01,3477', 0o20000, '', 'OCT', '20000', kind='data', line=530)

# LONGCALL
W('01,3500', 0o35002, 'LASTTIME', 'CA', 'BIT14', 'GET BACK THE CORRECT DELTA TFOR WAITLIST', line=533)
W('01,3501', 0o27140, '', 'ADS', 'LONGTIME +1', line=534)
W('01,3502', 0o05245, '', 'TC', 'WAITLIST', line=535)
#   EBANK= LST1
W('01,3503', 0o03515, '', '2CADR', 'GETCADR', 'THE ENTRY TO OUR LONGCADR', kind='data', line=537)
W('01,3504', 0o02063, kind='data', line=537)

W('01,3505', 0o33517, 'LONGRTRN', 'CA', 'TSKOVCDR', 'SET IT UP SO THAT ONLY THE FIRST EXIT IS', line=539)
# Page 1235
W('01,3506', 0o53435, '', 'DXCH', 'LONGEXIT', 'TO THE CALLER OF LONGCALL', line=541)
W('01,3507', 0o52006, '', 'DTCB', '', 'THE REST ARE TO TASKOVER', line=542)

W('01,3510', 0o35002, 'MUCHTIME', 'CA', 'BIT14', 'WE HAVE OVER OUR ABOUT 1.25 MINUTES', line=544)
W('01,3511', 0o05245, '', 'TC', 'WAITLIST', 'SO SET UP FOR ANOTHER CYCLE THROUGH HERE', line=545)
#   EBANK= LST1
W('01,3512', 0o03465, '', '2CADR', 'LONGCYCL', kind='data', line=547)
W('01,3513', 0o02063, kind='data', line=547)

W('01,3514', 0o13505, '', 'TCF', 'LONGRTRN', 'NOW EXIT PROPERLY', line=550)

# *** WAITLIST TASK GETCADR ***
W('01,3515', 0o53134, 'GETCADR', 'DXCH', 'LONGCADR', 'GET THE LONGCALL THAT WE WISHED TO START', line=553)
W('01,3516', 0o52006, '', 'DTCB', '', 'AND TRANSFER CONTROL TO IT', line=554)

W('01,3517', 0o05324, 'TSKOVCDR', 'GENADR', 'TASKOVER', kind='data', line=556)
