"""RESTARTS_ROUTINE.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/RESTARTS_ROUTINE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1414-1419 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('RESTARTS_ROUTINE', 'RESTARTS_ROUTINE.agc', 'Comanche055', pages='1414-1419')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     RESTARTS_ROUTINE.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 1414-1419
# Contact:      Ron Burkey <info@sandroid.org>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-07 RSB  Adapted from Colossus249 file of the same
# name, and page images. Corrected various
# typos in the transcription of program
# comments, and these should be back-ported
# to Colossus249.
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

# Page 1414
#   BANK 01
#   SETLOC RESTART
#   BANK

#   EBANK= PHSNAME1  # GOPROG MUST SWITCH TO THIS EBANK

#   COUNT 01/RSROU

W('01,3520', 0o30161, 'RESTARTS', 'CA', 'MPAC +5', 'GET GROUP NUMBER -1', line=43)
W('01,3521', 0o60000, '', 'DOUBLE', '', 'SAVE FOR INDEXING', line=44)
W('01,3522', 0o54155, '', 'TS', 'TEMP2G', line=45)

W('01,3523', 0o33762, '', 'CA', 'PHS2CADR', 'SET UP EXIT IN CASE IT IS AN EVEN', line=47)
W('01,3524', 0o54157, '', 'TS', 'TEMPSWCH', 'TABLE PHASE', line=48)

W('01,3525', 0o33557, '', 'CA', 'RTRNCADR', 'TO SAVE TIME ASSUME IT WILL GET NEXT', line=50)
W('01,3526', 0o54707, '', 'TS', 'GOLOC +2', 'GROUP AFTER THIS', line=51)

W('01,3527', 0o30154, '', 'CA', 'TEMPPHS', line=53)
W('01,3530', 0o75051, '', 'MASK', 'OCT1400', line=54)
W('01,3531', 0o10000, '', 'CCS', 'A', 'IS IT A VARIABLE OR TABLE RESTART', line=55)
W('01,3532', 0o13543, '', 'TCF', 'ITSAVAR', 'IT:S A VARIABLE RESTART', line=56)

W('01,3533', 0o10154, 'GETPART2', 'CCS', 'TEMPPHS', 'IS IT AN X.1 RESTART', line=58)
W('01,3534', 0o10000, '', 'CCS', 'A', line=59)
W('01,3535', 0o13643, '', 'TCF', 'ITSATBL', 'NO, ITS A TABLE RESTART', line=60)

W('01,3536', 0o35066, '', 'CA', 'PRIO14', 'IT IS AN X.1 RESTART, THEREFORE START', line=62)
W('01,3537', 0o05147, '', 'TC', 'FINDVAC', 'THE DISPLAY RESTART JOB', line=63)
#   EBANK= LST1
W('01,3540', 0o03261, '', '2CADR', 'INITDSP', kind='data', line=65)
W('01,3541', 0o20063, kind='data', line=65)

W('01,3542', 0o03557, '', 'TC', 'RTRNCADR', 'FINISHED WITH THIS GROUP, GET NEXT ONE', line=67)

W('01,3543', 0o75051, 'ITSAVAR', 'MASK', 'OCT1400', 'IS IT TYPE B ?', line=69)
W('01,3544', 0o10000, '', 'CCS', 'A', line=70)
W('01,3545', 0o13614, '', 'TCF', 'ITSLIKEB', 'YES,IT IS TYPE B', line=71)

W('01,3546', 0o00006, '', 'EXTEND', '', 'STORE THE JOB (OR TASK) 2CADR FOR EXIT', line=73)
W('01,3547', 0o50155, '', 'NDX', 'TEMP2G', line=74)
W('01,3550', 0o31437, '', 'DCA', 'PHSNAME1', line=75)
W('01,3551', 0o52706, '', 'DXCH', 'GOLOC', line=76)

W('01,3552', 0o30154, '', 'CA', 'TEMPPHS', 'SEE IF THIS IS A JOB, TASK, OR A LONGCALL', line=78)
W('01,3553', 0o75023, '', 'MASK', 'OCT7', line=79)
W('01,3554', 0o67715, '', 'AD', 'MINUS2', line=80)
W('01,3555', 0o10000, '', 'CCS', 'A', line=81)
W('01,3556', 0o13726, '', 'TCF', 'ITSLNGCL', 'ITS A LONGCALL', line=82)

# Page 1415
W('01,3557', 0o04675, 'RTRNCADR', 'TC', 'SWRETURN', 'CANT GET HERE', line=85)
W('01,3560', 0o13562, '', 'TCF', 'ITSAWAIT', line=86)

W('01,3561', 0o13627, '', 'TCF', 'ITSAJOB', 'ITS A JOB', line=88)

W('01,3562', 0o33766, 'ITSAWAIT', 'CA', 'WTLTCADR', 'SET UP WAITLIST CALL', line=90)
W('01,3563', 0o54704, '', 'TS', 'GOLOC -1', line=91)

W('01,3564', 0o50155, '', 'NDX', 'TEMP2G', 'DIRECTLY STORED', line=93)
W('01,3565', 0o31054, '', 'CA', 'PHSPRDT1', line=94)
W('01,3566', 0o10000, 'TIMETEST', 'CCS', 'A', 'IS IT AN IMMEDIATE RESTART', line=95)
W('01,3567', 0o24000, '', 'INCR', 'A', 'NO.', line=96)
W('01,3570', 0o13573, '', 'TCF', 'FINDTIME', 'FIND OUT WHEN IT SHOULD BEGIN', line=97)

W('01,3571', 0o15500, '', 'TCF', 'ITSINDIR', 'STORED INDIRECTLY', line=99)

W('01,3572', 0o13612, '', 'TCF', 'IMEDIATE', 'IT WANTS AN IMMEDIATE RESTART', line=101)

# ***** THIS MUST BE IN FIXED FIXED *****

#   BLOCK 02
#   SETLOC FFTAG2
#   BANK

#   COUNT 02/RSROU

W('5500', 0o22706, 'ITSINDIR', 'LXCH', 'GOLOC +1', 'GET THE CORRECT E BANK IN CASE THIS IS', line=111)
W('5501', 0o22006, '', 'LXCH', 'BB', 'SWITCHED ERRASIBLE', line=112)

W('5502', 0o50000, '', 'NDX', 'A', 'GET THE TIME INDIRECTLY', line=114)
W('5503', 0o30001, '', 'CA', '1', line=115)

W('5504', 0o22006, '', 'LXCH', 'BB', 'RESTORE THE BB AND GOLOC', line=117)
W('5505', 0o22706, '', 'LXCH', 'GOLOC +1', line=118)

W('5506', 0o13573, '', 'TCF', 'FINDTIME', 'FIND OUT WHEN IT SHOULD BEGIN', line=120)

# ***** YOU MAY RETURN TO SWITCHED FIXED *****

#   BANK 01
#   SETLOC RESTART
#   BANK

#   COUNT 01/RSROU

W('01,3573', 0o40000, 'FINDTIME', 'COM', '', 'MAKE NEGATIVE SINCE IT WILL BE SUBTRACTED', line=130)
W('01,3574', 0o54001, '', 'TS', 'L', 'AND SAVE', line=131)
W('01,3575', 0o50155, '', 'NDX', 'TEMP2G', line=132)
W('01,3576', 0o41053, '', 'CS', 'TBASE1', line=133)
W('01,3577', 0o00006, '', 'EXTEND', line=134)
# Page 1416
W('01,3600', 0o60025, '', 'SU', 'TIME1', line=136)
W('01,3601', 0o10000, '', 'CCS', 'A', line=137)
W('01,3602', 0o40000, '', 'COM', line=138)
W('01,3603', 0o67700, '', 'AD', 'OCT37776', line=139)
W('01,3604', 0o65017, '', 'AD', 'ONE', line=140)
W('01,3605', 0o60001, '', 'AD', 'L', line=141)
W('01,3606', 0o10000, '', 'CCS', 'A', line=142)
W('01,3607', 0o35021, '', 'CA', 'ZERO', line=143)
W('01,3610', 0o13612, '', 'TCF', '+2', line=144)
W('01,3611', 0o13612, '', 'TCF', '+1', line=145)
W('01,3612', 0o65017, 'IMEDIATE', 'AD', 'ONE', line=146)
W('01,3613', 0o00704, '', 'TC', 'GOLOC -1', line=147)
W('01,3614', 0o33557, 'ITSLIKEB', 'CA', 'RTRNCADR', 'TYPE B, SO STORE RETURN IN', line=148)
W('01,3615', 0o54157, '', 'TS', 'TEMPSWCH', 'TEMPSWCH IN CASE OF AN EVEN PHASE', line=149)

W('01,3616', 0o33763, '', 'CA', 'PRT2CADR', 'SET UP EXIT TO GET TABLE PART OF THIS', line=151)
W('01,3617', 0o54707, '', 'TS', 'GOLOC +2', 'VARIABLE TYPE OF PHASE', line=152)

W('01,3620', 0o30154, '', 'CA', 'TEMPPHS', 'MAKE THE PHASE LOOK RIGHT FOR THE TABLE', line=154)
W('01,3621', 0o76043, '', 'MASK', 'OCT177', 'PART OF THIS VARIABLE PHASE', line=155)
W('01,3622', 0o54154, '', 'TS', 'TEMPPHS', line=156)

W('01,3623', 0o00006, '', 'EXTEND', line=158)
W('01,3624', 0o50155, '', 'NDX', 'TEMP2G', 'OBTAIN THE JOB:S 2CADR', line=159)
W('01,3625', 0o31437, '', 'DCA', 'PHSNAME1', line=160)
W('01,3626', 0o52706, '', 'DXCH', 'GOLOC', line=161)

W('01,3627', 0o50155, 'ITSAJOB', 'NDX', 'TEMP2G', 'NOW ADD THE PRIORITY AND LET:S GO', line=163)
W('01,3630', 0o31054, '', 'CA', 'PHSPRDT1', line=164)
W('01,3631', 0o54704, 'CHKNOVAC', 'TS', 'GOLOC -1', 'SAVE PRIO UNTIL WE SEE IF ITS', line=165)
W('01,3632', 0o00006, '', 'EXTEND', '', 'A FINDVAC OR A NOVAC', line=166)
W('01,3633', 0o63637, '', 'BZMF', 'ITSNOVAC', line=167)

W('01,3634', 0o33765, '', 'CAF', 'FVACCADR', 'POSITIVE, SET UP FINDVAC CALL.', line=169)
W('01,3635', 0o56704, '', 'XCH', 'GOLOC -1', 'PICK UP PRIO,', line=170)
W('01,3636', 0o00704, '', 'TC', 'GOLOC -1', 'AND GO', line=171)

W('01,3637', 0o33767, 'ITSNOVAC', 'CAF', 'NOVACADR', 'NEGATIVE,', line=173)
W('01,3640', 0o56704, '', 'XCH', 'GOLOC -1', 'SET UP NOVAC CALL,', line=174)
W('01,3641', 0o40000, '', 'COM', '', 'CORRECT PRIO,', line=175)
W('01,3642', 0o00704, '', 'TC', 'GOLOC -1', 'AND GO', line=176)

W('01,3643', 0o54020, 'ITSATBL', 'TS', 'CYR', 'FIND OUT IF THE PHASE IS ODD OR EVEN', line=178)
W('01,3644', 0o10020, '', 'CCS', 'CYR', line=179)
W('01,3645', 0o13646, '', 'TCF', '+1', 'IT:S EVEN', line=180)
W('01,3646', 0o13744, '', 'TCF', 'ITSEVEN', line=181)

W('01,3647', 0o33557, '', 'CA', 'RTRNCADR', 'IN CASE THIS IS THE SECOND PART OF A', line=183)
W('01,3650', 0o54707, '', 'TS', 'GOLOC +2', 'TYPE B RESTART, WE NEED PROPER EXIT', line=184)
# Page 1417
W('01,3651', 0o30154, '', 'CA', 'TEMPPHS', 'SET UP POINTER FOR FINDING OUR PLACE IN', line=186)
W('01,3652', 0o54021, '', 'TS', 'SR', 'THE RESTART TABLES', line=187)
W('01,3653', 0o60021, '', 'AD', 'SR', line=188)
W('01,3654', 0o50155, '', 'NDX', 'TEMP2G', line=189)
W('01,3655', 0o62001, '', 'AD', 'SIZETAB +1', line=190)
W('01,3656', 0o54156, '', 'TS', 'POINTER', line=191)

W('01,3657', 0o00006, 'CONTBL2', 'EXTEND', '', "FIND OUT WHAT'S IN THE TABLE", line=193)
W('01,3660', 0o50156, '', 'NDX', 'POINTER', line=194)
W('01,3661', 0o32002, '', 'DCA', 'CADRTAB', 'GET THE 2CADR', line=195)

W('01,3662', 0o22706, '', 'LXCH', 'GOLOC +1', 'STORE THE BB INFORMATION', line=197)

W('01,3663', 0o10000, '', 'CCS', 'A', 'IS IT A JOB OR IT IT TIMED', line=199)
W('01,3664', 0o24000, '', 'INCR', 'A', 'POSITIVE, MUST BE A JOB', line=200)
W('01,3665', 0o13740, '', 'TCF', 'ITSAJOB2', line=201)

W('01,3666', 0o24000, '', 'INCR', 'A', 'MUST BE EITHER A WAITLIST OR LONGCALL', line=203)
W('01,3667', 0o54705, '', 'TS', 'GOLOC', 'LET-S STORE THE CORRECT CADR', line=204)

W('01,3670', 0o33766, '', 'CA', 'WTLTCADR', 'SET UP OUR EXIT TO WAITLIST', line=206)
W('01,3671', 0o54704, '', 'TS', 'GOLOC -1', line=207)

W('01,3672', 0o30706, '', 'CA', 'GOLOC +1', 'NOW FIND OUT IF IT IS A WAITLIST CALL', line=209)
W('01,3673', 0o75006, '', 'MASK', 'BIT10', 'THIS SHOULD BE ONE IF WE HAVE -BB', line=210)
W('01,3674', 0o10000, '', 'CCS', 'A', 'FOR THAT MATTER SO SHOULD BE BITS 9,8,7,', line=211)
# 6,5, AND LAST BUT NOT LEAST (PERHAPS NOT
# IN IMPORTANCE ANYWAY. BIT 4
W('01,3675', 0o13733, '', 'TCF', 'ITSWTLST', 'IT IS A WAITLIST CALL', line=214)

W('01,3676', 0o50156, '', 'NDX', 'POINTER', 'OBTAIN THE ORIGINAL DELTA T', line=216)
W('01,3677', 0o32000, '', 'CA', 'PRDTTAB', 'ADDRESS FOR THIS LONGCALL', line=217)

W('01,3700', 0o15507, '', 'TCF', 'ITSLGCL1', 'NOW GO GET THE DELTA TIME', line=219)

# ***** THIS MUST BE IN FIXED FIXED *****

#   BLOCK 02
#   SETLOC FFTAG2
#   BANK

#   COUNT 02/RSROU

W('5507', 0o22706, 'ITSLGCL1', 'LXCH', 'GOLOC +1', 'OBTAIN THE CORRECT E BANK', line=229)
W('5510', 0o22006, '', 'LXCH', 'BB', line=230)
W('5511', 0o22706, '', 'LXCH', 'GOLOC +1', 'AND PRESERVE OUR E AND F BANKS', line=231)

W('5512', 0o00006, '', 'EXTEND', '', 'GET THE DELTA TIME', line=233)
W('5513', 0o50000, '', 'NDX', 'A', line=234)
W('5514', 0o30001, '', 'DCA', '0', line=235)
# Page 1418
W('5515', 0o22706, '', 'LXCH', 'GOLOC +1', 'RESTORE OUR E AND F BANK', line=237)
W('5516', 0o22006, '', 'LXCH', 'BB', 'RESTORE THE TASKS E AND F BANKS', line=238)
W('5517', 0o22706, '', 'LXCH', 'GOLOC +1', 'AND PRESERVE OUR L', line=239)

W('5520', 0o13701, '', 'TCF', 'ITSLGCL2', 'NOW LET:S PROCESS THIS LONGCALL', line=241)

# ***** YOU MAY RETURN TO SWITCHED FIXED *****

#   BANK 01
#   SETLOC RESTART
#   BANK

#   COUNT 01/RSROU

W('01,3701', 0o53140, 'ITSLGCL2', 'DXCH', 'LONGTIME', line=251)

W('01,3702', 0o00006, '', 'EXTEND', '', 'CALCULATE TIME LEFT', line=253)
W('01,3703', 0o40025, '', 'DCS', 'TIME2', line=254)
W('01,3704', 0o21140, '', 'DAS', 'LONGTIME', line=255)
W('01,3705', 0o00006, '', 'EXTEND', line=256)
W('01,3706', 0o31136, '', 'DCA', 'LONGBASE', line=257)
W('01,3707', 0o21140, '', 'DAS', 'LONGTIME', line=258)

W('01,3710', 0o11137, '', 'CCS', 'LONGTIME', 'FIND OUT HOW THIS SHOULD BE RESTARTED', line=260)
W('01,3711', 0o13721, '', 'TCF', 'LONGCLCL', line=261)
W('01,3712', 0o13714, '', 'TCF', '+2', line=262)
W('01,3713', 0o13607, '', 'TCF', 'IMEDIATE -3', line=263)
W('01,3714', 0o11140, '', 'CCS', 'LONGTIME +1', line=264)
W('01,3715', 0o13721, '', 'TCF', 'LONGCLCL', line=265)
W('01,3716', 0o13717, '', 'NOOP', '', 'CAN:T GET HERE        *********', line=266)
W('01,3717', 0o13607, '', 'TCF', 'IMEDIATE -3', line=267)
W('01,3720', 0o13612, '', 'TCF', 'IMEDIATE', line=268)

W('01,3721', 0o33764, 'LONGCLCL', 'CA', 'LGCLCADR', 'WE WILL GO TO LONGCALL', line=270)
W('01,3722', 0o54704, '', 'TS', 'GOLOC -1', line=271)

W('01,3723', 0o00006, '', 'EXTEND', '', 'PREPARE OUR ENTRY TO LONGCALL', line=273)
W('01,3724', 0o31140, '', 'DCA', 'LONGTIME', line=274)
W('01,3725', 0o00704, '', 'TC', 'GOLOC -1', line=275)

W('01,3726', 0o33766, 'ITSLNGCL', 'CA', 'WTLTCADR', 'ASSUME IT WILL GO TO WAITLIST', line=277)
W('01,3727', 0o54704, '', 'TS', 'GOLOC -1', line=278)

W('01,3730', 0o50155, '', 'NDX', 'TEMP2G', line=280)
W('01,3731', 0o41054, '', 'CS', 'PHSPRDT1', 'GET THE DELTA T ADDRESS', line=281)

W('01,3732', 0o15507, '', 'TCF', 'ITSLGCL1', 'NOW GET THE DELTA TIME', line=283)

W('01,3733', 0o40706, 'ITSWTLST', 'CS', 'GOLOC +1', 'CORRECT THE BBCON INFORMATION', line=285)
W('01,3734', 0o54706, '', 'TS', 'GOLOC +1', line=286)
# Page 1419
W('01,3735', 0o50156, '', 'NDX', 'POINTER', 'GET THE DT AND FIND OUT IF IT WAS STORED', line=288)
W('01,3736', 0o32000, '', 'CA', 'PRDTTAB', 'DIRECTLY OR INDIRECTLY', line=289)

W('01,3737', 0o13566, '', 'TCF', 'TIMETEST', 'FIND OUT HOW THE TIME IS STORED', line=291)

W('01,3740', 0o56705, 'ITSAJOB2', 'XCH', 'GOLOC', 'STORE THE CADR', line=293)

W('01,3741', 0o50156, '', 'NDX', 'POINTER', 'ADD THE PRIORITY AND LET:S GO', line=295)
W('01,3742', 0o32000, '', 'CA', 'PRDTTAB', line=296)

W('01,3743', 0o13631, '', 'TCF', 'CHKNOVAC', line=298)

W('01,3744', 0o30157, 'ITSEVEN', 'CA', 'TEMPSWCH', 'SET UP FOR EITHER THE SECOND PART OF THE', line=300)
W('01,3745', 0o54707, '', 'TS', 'GOLOC +2', 'TABLE, OR A RETURN FOR THE NEXT GROUP', line=301)

W('01,3746', 0o50155, '', 'NDX', 'TEMP2G', 'SET UP POINTER FOR OUR LOCATION WITHIN', line=303)
W('01,3747', 0o32000, '', 'CA', 'SIZETAB', 'THE TABLE', line=304)
W('01,3750', 0o60154, '', 'AD', 'TEMPPHS', 'THIS MAY LOOK BAD BUT LET:S SEE YOU DO', line=305)
W('01,3751', 0o60154, '', 'AD', 'TEMPPHS', 'BETTER IN TIME OR NUMBER OF LOCATIONS', line=306)
W('01,3752', 0o60154, '', 'AD', 'TEMPPHS', line=307)
W('01,3753', 0o54156, '', 'TS', 'POINTER', line=308)

W('01,3754', 0o13657, '', 'TCF', 'CONTBL2', 'NOW PROCESS WHAT IS IN THE TABLE', line=310)

W('01,3755', 0o36214, 'PHSPART2', 'CA', 'THREE', 'SET THE POINTER FOR THE SECOND HALF OF', line=312)
W('01,3756', 0o26156, '', 'ADS', 'POINTER', 'THE TABLE', line=313)

W('01,3757', 0o33557, '', 'CA', 'RTRNCADR', 'THIS WILL BE OUR LAST TIME THROUGH THE', line=315)
W('01,3760', 0o54707, '', 'TS', 'GOLOC +2', 'EVEN TABLE , SO AFTER IT  GET THE NEXT', line=316)
# GROUP
W('01,3761', 0o13657, '', 'TCF', 'CONTBL2', 'SO LET:S GET THE SECOND ENTRY IN THE TBL', line=318)

S('TEMPPHS', 'equals', 0o154, line=320)
S('TEMP2G', 'equals', 0o155, line=321)
S('POINTER', 'equals', 0o156, line=322)
S('TEMPSWCH', 'equals', 0o157, line=323)
S('GOLOC', 'equals', 0o705, line=324)
S('MINUS2', 'equals', 0o7715, line=325)
S('OCT177', 'equals', 0o6043, line=326)

W('01,3762', 0o03755, 'PHS2CADR', 'GENADR', 'PHSPART2', kind='data', line=328)
W('01,3763', 0o03533, 'PRT2CADR', 'GENADR', 'GETPART2', kind='data', line=329)
W('01,3764', 0o05342, 'LGCLCADR', 'GENADR', 'LONGCALL', kind='data', line=330)
W('01,3765', 0o05147, 'FVACCADR', 'GENADR', 'FINDVAC', kind='data', line=331)
W('01,3766', 0o05245, 'WTLTCADR', 'GENADR', 'WAITLIST', kind='data', line=332)
W('01,3767', 0o05134, 'NOVACADR', 'GENADR', 'NOVAC', kind='data', line=333)
