"""RESTARTS_ROUTINE.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/RESTARTS_ROUTINE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1303-1308 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('RESTARTS_ROUTINE', 'RESTARTS_ROUTINE.agc', 'Luminary099', pages='1303-1308')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     RESTARTS_ROUTINE.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Onno Hommes <ohommes@cmu.edu>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1303-1309
# Mod history:  2009-05-27 OH   Transcribed from page images.
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

# Page 1303
#   BANK 01
#   SETLOC RESTART
#   BANK

#   EBANK= PHSNAME1  # GOPROG MUST SWITCH TO THIS EBANK

#   COUNT* $$/RSROU
W('01,3526', 0o30161, 'RESTARTS', 'CA', 'MPAC +5', 'GET GROUP NUMBER -1', line=35)
W('01,3527', 0o60000, '', 'DOUBLE', '', 'SAVE FOR INDEXING', line=36)
W('01,3530', 0o54155, '', 'TS', 'TEMP2G', line=37)

W('01,3531', 0o33770, '', 'CA', 'PHS2CADR', 'SET UP EXIT IN CASE IT IS AN EVEN', line=39)
W('01,3532', 0o54157, '', 'TS', 'TEMPSWCH', 'TABLE PHASE', line=40)

W('01,3533', 0o33565, '', 'CA', 'RTRNCADR', 'TO SAVE TIME ASSUME IT WILL GET NEXT', line=42)
W('01,3534', 0o54707, '', 'TS', 'GOLOC +2', 'GROUP AFTER THIS', line=43)

W('01,3535', 0o30154, '', 'CA', 'TEMPPHS', line=45)
W('01,3536', 0o75007, '', 'MASK', 'OCT1400', line=46)
W('01,3537', 0o10000, '', 'CCS', 'A', 'IS IT A VARIABLE OR TABLE RESTART', line=47)
W('01,3540', 0o13551, '', 'TCF', 'ITSAVAR', 'IT:S A VARIABLE RESTART', line=48)

W('01,3541', 0o10154, 'GETPART2', 'CCS', 'TEMPPHS', 'IS IT AN X.1 RESTART', line=50)
W('01,3542', 0o10000, '', 'CCS', 'A', line=51)
W('01,3543', 0o13651, '', 'TCF', 'ITSATBL', 'NO, ITS A TABLE RESTART', line=52)

W('01,3544', 0o35024, '', 'CA', 'PRIO14', 'IT IS AN X.1 RESTART, THEREFORE START', line=54)
W('01,3545', 0o05105, '', 'TC', 'FINDVAC', 'THE DISPLAY RESTART JOB', line=55)
#   EBANK= LST1
W('01,3546', 0o03037, '', '2CADR', 'INITDSP', kind='data', line=57)
W('01,3547', 0o20103, kind='data', line=57)

W('01,3550', 0o03565, '', 'TC', 'RTRNCADR', 'FINISHED WITH THIS GROUP, GET NEXT ONE', line=59)

W('01,3551', 0o75007, 'ITSAVAR', 'MASK', 'OCT1400', 'IS IT TYPE B ?', line=61)
W('01,3552', 0o10000, '', 'CCS', 'A', line=62)
W('01,3553', 0o13622, '', 'TCF', 'ITSLIKEB', 'YES,IT IS TYPE B', line=63)

W('01,3554', 0o00006, '', 'EXTEND', '', 'STORE THE JOB (OR TASK) 2CADR FOR EXIT', line=65)
W('01,3555', 0o50155, '', 'NDX', 'TEMP2G', line=66)
W('01,3556', 0o31437, '', 'DCA', 'PHSNAME1', line=67)
W('01,3557', 0o52706, '', 'DXCH', 'GOLOC', line=68)

W('01,3560', 0o30154, '', 'CA', 'TEMPPHS', 'SEE IF THIS IS A JOB, TASK, OR A LONGCAL', line=70)
W('01,3561', 0o74757, '', 'MASK', 'OCT7', line=71)
W('01,3562', 0o67746, '', 'AD', 'MINUS2', line=72)
W('01,3563', 0o10000, '', 'CCS', 'A', line=73)
W('01,3564', 0o13734, '', 'TCF', 'ITSLNGCL', 'ITS A LONGCALL', line=74)

W('01,3565', 0o04631, 'RTRNCADR', 'TC', 'SWRETURN', 'CANT GET HERE', line=76)
# Page 1304
W('01,3566', 0o13570, '', 'TCF', 'ITSAWAIT', line=78)

W('01,3567', 0o13635, '', 'TCF', 'ITSAJOB', 'ITS A JOB', line=80)

W('01,3570', 0o33774, 'ITSAWAIT', 'CA', 'WTLTCADR', 'SET UP WAITLIST CALL', line=82)
W('01,3571', 0o54704, '', 'TS', 'GOLOC -1', line=83)

W('01,3572', 0o50155, '', 'NDX', 'TEMP2G', 'DIRECTLY STORED', line=85)
W('01,3573', 0o31054, '', 'CA', 'PHSPRDT1', line=86)
W('01,3574', 0o10000, 'TIMETEST', 'CCS', 'A', 'IS IT AN IMMEDIATE RESTART', line=87)
W('01,3575', 0o24000, '', 'INCR', 'A', 'NO.', line=88)
W('01,3576', 0o13601, '', 'TCF', 'FINDTIME', 'FIND OUT WHEN IT SHOULD BEGIN', line=89)

W('01,3577', 0o15436, '', 'TCF', 'ITSINDIR', 'STORED INDIRECTLY', line=91)

W('01,3600', 0o13620, '', 'TCF', 'IMEDIATE', 'IT WANTS AN IMMEDIATE RESTART', line=93)

# ***** THIS MUST BE IN FIXED FIXED *****

#   BLOCK 02
#   SETLOC FFTAG2
#   BANK

#   COUNT* $$/RSROU
W('5436', 0o22706, 'ITSINDIR', 'LXCH', 'GOLOC +1', 'GET THE CORRECT E BANK IN CASE THIS IS', line=102)
W('5437', 0o22006, '', 'LXCH', 'BB', 'SWITCHED ERRASIBLE', line=103)

W('5440', 0o50000, '', 'NDX', 'A', 'GET THE TIME INDIRECTLY', line=105)
W('5441', 0o30001, '', 'CA', '1', line=106)

W('5442', 0o22006, '', 'LXCH', 'BB', 'RESTORE THE BB AND GOLOC', line=108)
W('5443', 0o22706, '', 'LXCH', 'GOLOC +1', line=109)

W('5444', 0o13601, '', 'TCF', 'FINDTIME', 'FIND OUT WHEN IT SHOULD BEGIN', line=111)

# ***** YOU MAY RETURN TO SWITCHED FIXED *****

#   BANK 01
#   SETLOC RESTART
#   BANK

#   COUNT* $$/RSROU
W('01,3601', 0o40000, 'FINDTIME', 'COM', '', 'MAKE NEGITIVE SINCE IT WILL BE SUBTRACTD', line=120)
W('01,3602', 0o54001, '', 'TS', 'L', 'AND SAVE', line=121)
W('01,3603', 0o50155, '', 'NDX', 'TEMP2G', line=122)
W('01,3604', 0o41053, '', 'CS', 'TBASE1', line=123)
W('01,3605', 0o00006, '', 'EXTEND', line=124)
W('01,3606', 0o60025, '', 'SU', 'TIME1', line=125)
W('01,3607', 0o10000, '', 'CCS', 'A', line=126)
W('01,3610', 0o40000, '', 'COM', line=127)
# Page 1305
W('01,3611', 0o67731, '', 'AD', 'OCT37776', line=129)
W('01,3612', 0o64753, '', 'AD', 'ONE', line=130)
W('01,3613', 0o60001, '', 'AD', 'L', line=131)
W('01,3614', 0o10000, '', 'CCS', 'A', line=132)
W('01,3615', 0o34755, '', 'CA', 'ZERO', line=133)
W('01,3616', 0o13620, '', 'TCF', '+2', line=134)
W('01,3617', 0o13620, '', 'TCF', '+1', line=135)
W('01,3620', 0o64753, 'IMEDIATE', 'AD', 'ONE', line=136)
W('01,3621', 0o00704, '', 'TC', 'GOLOC -1', line=137)
W('01,3622', 0o33565, 'ITSLIKEB', 'CA', 'RTRNCADR', 'TYPE B,             SO STORE RETURN IN', line=138)
W('01,3623', 0o54157, '', 'TS', 'TEMPSWCH', 'TEMPSWCH IN CASE OF AN EVEN PHASE', line=139)

W('01,3624', 0o33771, '', 'CA', 'PRT2CADR', 'SET UP EXIT TO GET TABLE PART OF THIS', line=141)
W('01,3625', 0o54707, '', 'TS', 'GOLOC +2', 'VARIABLE TYPE OF PHASE', line=142)

W('01,3626', 0o30154, '', 'CA', 'TEMPPHS', 'MAKE THE PHASE LOOK RIGHT FOR THE TABLE', line=144)
W('01,3627', 0o76074, '', 'MASK', 'OCT177', 'PART OF THIS VARIABLE PHASE', line=145)
W('01,3630', 0o54154, '', 'TS', 'TEMPPHS', line=146)

W('01,3631', 0o00006, '', 'EXTEND', line=148)
W('01,3632', 0o50155, '', 'NDX', 'TEMP2G', 'OBTAIN THE JOB:S 2CADR', line=149)
W('01,3633', 0o31437, '', 'DCA', 'PHSNAME1', line=150)
W('01,3634', 0o52706, '', 'DXCH', 'GOLOC', line=151)

W('01,3635', 0o50155, 'ITSAJOB', 'NDX', 'TEMP2G', 'NOW ADD THE PRIORITY AND LET:S GO', line=153)
W('01,3636', 0o31054, '', 'CA', 'PHSPRDT1', line=154)
W('01,3637', 0o54704, 'CHKNOVAC', 'TS', 'GOLOC -1', 'SAVE PRIO UNTIL WE SEE IF ITS', line=155)
W('01,3640', 0o00006, '', 'EXTEND', '', 'A FINDVAC OR A NOVAC', line=156)
W('01,3641', 0o63645, '', 'BZMF', 'ITSNOVAC', line=157)

W('01,3642', 0o33773, '', 'CAF', 'FVACCADR', 'POSITIVE, SET UP FINDVAC CALL.', line=159)
W('01,3643', 0o56704, '', 'XCH', 'GOLOC -1', 'PICK UP PRIO,', line=160)
W('01,3644', 0o00704, '', 'TC', 'GOLOC -1', 'AND GO', line=161)

W('01,3645', 0o33775, 'ITSNOVAC', 'CAF', 'NOVACADR', 'NEGATIVE,', line=163)
W('01,3646', 0o56704, '', 'XCH', 'GOLOC -1', 'SET UP NOVAC CALL,', line=164)
W('01,3647', 0o40000, '', 'COM', '', 'CORRECT PRIO,', line=165)
W('01,3650', 0o00704, '', 'TC', 'GOLOC -1', 'AND GO', line=166)

W('01,3651', 0o54020, 'ITSATBL', 'TS', 'CYR', 'FIND OUT IF THE PHASE IS ODD OR EVEN', line=168)
W('01,3652', 0o10020, '', 'CCS', 'CYR', line=169)
W('01,3653', 0o13654, '', 'TCF', '+1', 'IT:S EVEN', line=170)
W('01,3654', 0o13752, '', 'TCF', 'ITSEVEN', line=171)

W('01,3655', 0o33565, '', 'CA', 'RTRNCADR', 'IN CASE THIS IS THE SECOND PART OF A', line=173)
W('01,3656', 0o54707, '', 'TS', 'GOLOC +2', 'TYPE B RESTART, WE NEED PROPER EXIT', line=174)

W('01,3657', 0o30154, '', 'CA', 'TEMPPHS', 'SET UP POINTER FOR FINDING OUR PLACE IN', line=176)
W('01,3660', 0o54021, '', 'TS', 'SR', 'THE RESTART TABLES', line=177)
W('01,3661', 0o60021, '', 'AD', 'SR', line=178)
# Page 1306
W('01,3662', 0o50155, '', 'NDX', 'TEMP2G', line=180)
W('01,3663', 0o62003, '', 'AD', 'SIZETAB +1', line=181)
W('01,3664', 0o54156, '', 'TS', 'POINTER', line=182)

W('01,3665', 0o00006, 'CONTBL2', 'EXTEND', '', 'FIND OUT WHAT:S IN THE TABLE', line=184)
W('01,3666', 0o50156, '', 'NDX', 'POINTER', line=185)
W('01,3667', 0o32002, '', 'DCA', 'CADRTAB', 'GET THE 2CADR', line=186)

W('01,3670', 0o22706, '', 'LXCH', 'GOLOC +1', 'STORE THE BB INFORMATION', line=188)

W('01,3671', 0o10000, '', 'CCS', 'A', 'IS IT A JOB OR IS IT  TIMED', line=190)
W('01,3672', 0o24000, '', 'INCR', 'A', 'POSITIVE. MUST BE A JOB', line=191)
W('01,3673', 0o13746, '', 'TCF', 'ITSAJOB2', line=192)

W('01,3674', 0o24000, '', 'INCR', 'A', 'MUST BE EITHER A WAITLIST OR LONGCALL', line=194)
W('01,3675', 0o54705, '', 'TS', 'GOLOC', 'LET-S STORE THE CORRECT CADR', line=195)

W('01,3676', 0o33774, '', 'CA', 'WTLTCADR', 'SET UP OUR EXIT TO WAITLIST', line=197)
W('01,3677', 0o54704, '', 'TS', 'GOLOC -1', line=198)

W('01,3700', 0o30706, '', 'CA', 'GOLOC +1', 'NOW FIND OUT IF IT IS A WAITLIST CALL', line=200)
W('01,3701', 0o74742, '', 'MASK', 'BIT10', 'THIS SHOULD BE ONE IF WE HAVE -BB', line=201)
W('01,3702', 0o10000, '', 'CCS', 'A', 'FOR THAT MATTER SO SHOULD BE BITS 9,8,7,', line=202)
# 6,5, AND LAST BUT NOT LEAST (PERHAPS NOT
# IN IMPORTANCE ANYWAY. BIT 4
W('01,3703', 0o13741, '', 'TCF', 'ITSWTLST', 'IT IS A WAITLIST CALL', line=205)

W('01,3704', 0o50156, '', 'NDX', 'POINTER', 'OBTAIN THE ORIGINAL DELTA T', line=207)
W('01,3705', 0o32000, '', 'CA', 'PRDTTAB', 'ADDRESS FOR THIS LONGCALL', line=208)

W('01,3706', 0o15445, '', 'TCF', 'ITSLGCL1', 'NOW GO GET THE DELTA TIME', line=210)

# ***** THIS MUST BE IN FIXED FIXED *****

#   BLOCK 02
#   SETLOC FFTAG2
#   BANK

#   COUNT* $$/RSROU
W('5445', 0o22706, 'ITSLGCL1', 'LXCH', 'GOLOC +1', 'OBTAIN THE CORRECT E BANK', line=219)
W('5446', 0o22006, '', 'LXCH', 'BB', line=220)
W('5447', 0o22706, '', 'LXCH', 'GOLOC +1', 'AND PRESERVE OUR E AND F BANKS', line=221)

W('5450', 0o00006, '', 'EXTEND', '', 'GET THE DELTA TIME', line=223)
W('5451', 0o50000, '', 'NDX', 'A', line=224)
W('5452', 0o30001, '', 'DCA', '0', line=225)

W('5453', 0o22706, '', 'LXCH', 'GOLOC +1', 'RESTORE OUR E AND F BANK', line=227)
W('5454', 0o22006, '', 'LXCH', 'BB', 'RESTORE THE TASKS E AND F BANKS', line=228)
W('5455', 0o22706, '', 'LXCH', 'GOLOC +1', 'AND PRESERVE OUR L', line=229)
# Page 1307
W('5456', 0o13707, '', 'TCF', 'ITSLGCL2', 'NOT LET:S PROCESS THIS LONGCALL', line=231)

# ***** YOU MAY RETURN TO  SWITCHED FIXED *****

#   BANK 01
#   SETLOC RESTART
#   BANK

#   COUNT* $$/RSROU
W('01,3707', 0o53154, 'ITSLGCL2', 'DXCH', 'LONGTIME', line=240)

W('01,3710', 0o00006, '', 'EXTEND', '', 'CALCULATE TIME LEFT', line=242)
W('01,3711', 0o40025, '', 'DCS', 'TIME2', line=243)
W('01,3712', 0o21154, '', 'DAS', 'LONGTIME', line=244)
W('01,3713', 0o00006, '', 'EXTEND', line=245)
W('01,3714', 0o31152, '', 'DCA', 'LONGBASE', line=246)
W('01,3715', 0o21154, '', 'DAS', 'LONGTIME', line=247)

W('01,3716', 0o11153, '', 'CCS', 'LONGTIME', 'FIND OUT HOW THIS SHOULD BE RESTARTED', line=249)
W('01,3717', 0o13727, '', 'TCF', 'LONGCLCL', line=250)
W('01,3720', 0o13722, '', 'TCF', '+2', line=251)
W('01,3721', 0o13615, '', 'TCF', 'IMEDIATE -3', line=252)
W('01,3722', 0o11154, '', 'CCS', 'LONGTIME +1', line=253)
W('01,3723', 0o13727, '', 'TCF', 'LONGCLCL', line=254)
W('01,3724', 0o13725, '', 'NOOP', '', 'CAN:T GET HERE    *********', line=255)
W('01,3725', 0o13615, '', 'TCF', 'IMEDIATE -3', line=256)
W('01,3726', 0o13620, '', 'TCF', 'IMEDIATE', line=257)

W('01,3727', 0o33772, 'LONGCLCL', 'CA', 'LGCLCADR', 'WE WILL GO TO LONGCALL', line=259)
W('01,3730', 0o54704, '', 'TS', 'GOLOC -1', line=260)

W('01,3731', 0o00006, '', 'EXTEND', '', 'PREPARE OUR ENTRY TO LONGCALL', line=262)
W('01,3732', 0o31154, '', 'DCA', 'LONGTIME', line=263)
W('01,3733', 0o00704, '', 'TC', 'GOLOC -1', line=264)

W('01,3734', 0o33774, 'ITSLNGCL', 'CA', 'WTLTCADR', 'ASSUME IT WILL GO TO WAITLIST', line=266)
W('01,3735', 0o54704, '', 'TS', 'GOLOC -1', line=267)

W('01,3736', 0o50155, '', 'NDX', 'TEMP2G', line=269)
W('01,3737', 0o41054, '', 'CS', 'PHSPRDT1', 'GET THE DELTA T ADDRESS', line=270)

W('01,3740', 0o15445, '', 'TCF', 'ITSLGCL1', 'NOW GET THE DELTA TIME', line=272)

W('01,3741', 0o40706, 'ITSWTLST', 'CS', 'GOLOC +1', 'CORRECT THE BBCON INFORMATION', line=274)
W('01,3742', 0o54706, '', 'TS', 'GOLOC +1', line=275)

W('01,3743', 0o50156, '', 'NDX', 'POINTER', 'GET THE DT AND FIND OUT IF IT WAS STORED', line=277)
W('01,3744', 0o32000, '', 'CA', 'PRDTTAB', 'DIRECTLY OR INDIRECTLY', line=278)

W('01,3745', 0o13574, '', 'TCF', 'TIMETEST', 'FIND OUT HOW THE TIME IS STORED', line=280)

# Page 1308
W('01,3746', 0o56705, 'ITSAJOB2', 'XCH', 'GOLOC', 'STORE THE CADR', line=283)

W('01,3747', 0o50156, '', 'NDX', 'POINTER', 'ADD THE PRIORITY AND LET:S GO', line=285)
W('01,3750', 0o32000, '', 'CA', 'PRDTTAB', line=286)

W('01,3751', 0o13637, '', 'TCF', 'CHKNOVAC', line=288)

W('01,3752', 0o30157, 'ITSEVEN', 'CA', 'TEMPSWCH', 'SET UP FOR EITHER THE SECOND PART OF THE', line=290)
W('01,3753', 0o54707, '', 'TS', 'GOLOC +2', 'TABLE, OR A RETURN FOR THE NEXT GROUP', line=291)

W('01,3754', 0o50155, '', 'NDX', 'TEMP2G', 'SET UP POINTER FOR OUR LOCATION WITHIN', line=293)
W('01,3755', 0o32002, '', 'CA', 'SIZETAB', 'THE TABLE', line=294)
W('01,3756', 0o60154, '', 'AD', 'TEMPPHS', 'THIS MAY LOOK BAD BUT LET:S SEE YOU DO', line=295)
W('01,3757', 0o60154, '', 'AD', 'TEMPPHS', 'BETTER IN TIME OR NUMBERR OF LOCATIONS', line=296)
W('01,3760', 0o60154, '', 'AD', 'TEMPPHS', line=297)
W('01,3761', 0o54156, '', 'TS', 'POINTER', line=298)

W('01,3762', 0o13665, '', 'TCF', 'CONTBL2', 'NOW PROCESS WHAT IS IN THE TABLE', line=300)

W('01,3763', 0o36245, 'PHSPART2', 'CA', 'THREE', 'SET THE POINTER FOR THE SECOND HALF OF', line=302)
W('01,3764', 0o26156, '', 'ADS', 'POINTER', 'THE TABLE', line=303)

W('01,3765', 0o33565, '', 'CA', 'RTRNCADR', 'THIS WILL BE OUR LAST TIME THROUGH THE', line=305)
W('01,3766', 0o54707, '', 'TS', 'GOLOC +2', 'EVEN TABLE , SO AFTER IT GET THE NEXT', line=306)
# GROUP
W('01,3767', 0o13665, '', 'TCF', 'CONTBL2', 'SO LET:S GET THE SECOND ENTRY IN THE TBL', line=308)

S('TEMPPHS', 'equals', 0o154, line=310)
S('TEMP2G', 'equals', 0o155, line=311)
S('POINTER', 'equals', 0o156, line=312)
S('TEMPSWCH', 'equals', 0o157, line=313)
S('GOLOC', 'equals', 0o705, line=314)
S('MINUS2', 'equals', 0o7746, line=315)
S('OCT177', 'equals', 0o6074, line=316)

W('01,3770', 0o03763, 'PHS2CADR', 'GENADR', 'PHSPART2', kind='data', line=318)
W('01,3771', 0o03541, 'PRT2CADR', 'GENADR', 'GETPART2', kind='data', line=319)
W('01,3772', 0o05277, 'LGCLCADR', 'GENADR', 'LONGCALL', kind='data', line=320)
W('01,3773', 0o05105, 'FVACCADR', 'GENADR', 'FINDVAC', kind='data', line=321)
W('01,3774', 0o05203, 'WTLTCADR', 'GENADR', 'WAITLIST', kind='data', line=322)
W('01,3775', 0o05072, 'NOVACADR', 'GENADR', 'NOVAC', kind='data', line=323)
