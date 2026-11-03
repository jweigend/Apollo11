"""SERVICE_ROUTINES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/SERVICE_ROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1485-1492 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('SERVICE_ROUTINES', 'SERVICE_ROUTINES.agc', 'Comanche055', pages='1485-1492')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     SERVICE_ROUTINES.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 1485-1492
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

# Page 1485
#   BLOCK 3
#   SETLOC FFTAG6
#   BANK
#   COUNT 03/FLAG

W('7722', 0o54001, 'UPENT2', 'TS', 'L', 'WHICH FLAGWORD IS IT', line=40)
W('7723', 0o75023, '', 'MASK', 'OCT7', line=41)
W('7724', 0o56001, '', 'XCH', 'L', 'SAVE IN L FOR INDEXING', line=42)

W('7725', 0o75731, '', 'MASK', 'OCT77770', 'OBTAIN THE BIT INFORMATION', line=44)
W('7726', 0o00004, '', 'INHINT', '', 'PREVENT INTERUPTS', line=45)
W('7727', 0o54061, '', 'TS', 'ITEMP1', 'STORE THE BIT INFORMATION TEMPORARIALY', line=46)

W('7730', 0o50001, '', 'NDX', 'L', line=48)
W('7731', 0o40074, '', 'CS', 'FLAGWRD0', line=49)
W('7732', 0o70061, '', 'MASK', 'ITEMP1', line=50)
W('7733', 0o50001, '', 'NDX', 'L', line=51)
W('7734', 0o26074, '', 'ADS', 'FLAGWRD0', line=52)
W('7735', 0o00003, '', 'RELINT', '', 'RELEASE INTERUPT INHIBIT', line=53)

W('7736', 0o24002, '', 'INCR', 'Q', 'OBTAIN THE CORRECT RETURN ADDRESS', line=55)
W('7737', 0o00002, '', 'TC', 'Q', 'RETURN', line=56)

W('7740', 0o54001, 'DOWNENT2', 'TS', 'L', 'WHICH FLAGWORD IS IT', line=58)
W('7741', 0o75023, '', 'MASK', 'OCT7', line=59)
W('7742', 0o56001, '', 'XCH', 'L', 'SAVE IN L FOR INDEXING', line=60)

W('7743', 0o75731, '', 'MASK', 'OCT77770', 'OBTAIN THE BIT INFORMATION', line=62)
W('7744', 0o40000, '', 'COM', '', 'START TO PROCESS THE INFORMATION', line=63)

W('7745', 0o00004, '', 'INHINT', '', 'PREVENT INTERUPTS', line=65)
W('7746', 0o50001, '', 'NDX', 'L', line=66)
W('7747', 0o70074, '', 'MASK', 'FLAGWRD0', line=67)
W('7750', 0o50001, '', 'NDX', 'L', line=68)
W('7751', 0o54074, '', 'TS', 'FLAGWRD0', line=69)
W('7752', 0o00003, '', 'RELINT', '', 'RELEASE INTERUPT INHIBIT', line=70)

W('7753', 0o24002, '', 'INCR', 'Q', 'OBTAIN THE CORRECT RETURN ADDRESS', line=72)
W('7754', 0o00002, '', 'TC', 'Q', 'RETURN', line=73)

S('OCT7', 'equals', 0o5023, line=75)
#   BANK 10

# Page 1486
#
# UPFLAG AND DOWNFLAG ARE ENTIRELY GENERAL FLAG SETTING AND CLEARING SUBROUTINES.  USING THEM, WHETHER OR
# NOT IN INTERRUPT, ONE MAY SET OR CLEAR ANY SINGLE, NAMED BIT IN ANY ERASABLE REGISTER, SUBJECT OF COURSE TO
# EBANK SETTING.  A "NAMED" BIT, AS THE WORD IS USED HERE, IS ANY BIT WITH A NAME FORMALLY ASSIGNED BY THE YUL
# ASSEMBLER.
#
# AT PRESENT THE ONLY NAMED BITS ARE THOSE IN THE FLAGWORDS.  ASSEMBLER CHANGES WILL MAKE IT POSSIBLE TO
# NAME ANY BIT IN ERASABLE MEMORY.
#
# CALLING SEQUENCES ARE AS FOLLOWS:-
#
# TC      UPFLAG                  TC      DOWNFLAG
# ADRES   NAME OF FLAG            ADRES   NAME OF FLAG
#
# RETURN IS TO THE LOCATION FOLLOWING THE "ADRES" ABOUT .58 MS AFTER THE "TC".
#
# UPON RETURN A CONTAINS THE CURRENT FLAGWRD SETTING.

#   BLOCK 02
#   SETLOC FFTAG1
#   BANK
#   COUNT* $$/FLAG

W('5546', 0o30002, 'UPFLAG', 'CA', 'Q', line=102)
W('5547', 0o05564, '', 'TC', 'DEBIT', line=103)
W('5550', 0o40000, '', 'COM', '', '+(15 - BIT)', line=104)
W('5551', 0o00006, '', 'EXTEND', line=105)
W('5552', 0o04001, '', 'ROR', 'LCHAN', 'SET BIT', line=106)
W('5553', 0o50061, 'COMFLAG', 'INDEX', 'ITEMP1', line=107)
W('5554', 0o54074, '', 'TS', 'FLAGWRD0', line=108)
W('5555', 0o22063, '', 'LXCH', 'ITEMP3', line=109)
W('5556', 0o00003, '', 'RELINT', line=110)
W('5557', 0o00001, '', 'TC', 'L', line=111)

W('5560', 0o30002, 'DOWNFLAG', 'CA', 'Q', line=114)
W('5561', 0o05564, '', 'TC', 'DEBIT', line=115)
W('5562', 0o70001, '', 'MASK', 'L', 'RESET BIT', line=116)
W('5563', 0o15553, '', 'TCF', 'COMFLAG', line=117)

W('5564', 0o65017, 'DEBIT', 'AD', 'ONE', 'GET DE BITS', line=120)
W('5565', 0o00004, '', 'INHINT', line=121)
W('5566', 0o54063, '', 'TS', 'ITEMP3', line=122)
W('5567', 0o35026, '', 'CA', 'LOW4', 'DEC15', line=123)
W('5570', 0o54061, '', 'TS', 'ITEMP1', line=124)
W('5571', 0o50063, '', 'INDEX', 'ITEMP3', line=125)
W('5572', 0o27777, '', 'CA', '0 -1', 'ADRES', line=126)
W('5573', 0o54001, '', 'TS', 'L', line=127)
W('5574', 0o35021, '', 'CA', 'ZERO', line=128)
# Page 1487
W('5575', 0o00006, '', 'EXTEND', line=130)
W('5576', 0o10061, '', 'DV', 'ITEMP1', 'A = FLAGWRD, L = (15 - BIT)', line=131)
W('5577', 0o52062, '', 'DXCH', 'ITEMP1', line=132)
W('5600', 0o50061, '', 'INDEX', 'ITEMP1', line=133)
W('5601', 0o30074, '', 'CA', 'FLAGWRD0', line=134)
W('5602', 0o54001, '', 'TS', 'L', 'CURRENT STATE', line=135)
W('5603', 0o50062, '', 'INDEX', 'ITEMP2', line=136)
W('5604', 0o45001, '', 'CS', 'BIT15', '-(15 - BIT)', line=137)
W('5605', 0o00002, '', 'TC', 'Q', line=138)

# Page 1488
# DELAYJOB- A GENERAL ROUTINE TO DELAY A JOB A SPECIFIC AMOUNT OF TIME BEFORE PICKING UP AGAIN.
#
# ENTRANCE REQUIREMENTS...
# CAF     DT              # DELAY JOB FOR DT CENTISECS
# TC      BANKCALL
# CADR    DELAYJOB

#   BANK 06
#   SETLOC DLAYJOB
#   BANK

# THIS MUST REMAIN IN BANK 0 ****************************************

#   COUNT 00/DELAY

W('00,3732', 0o00004, 'DELAYJOB', 'INHINT', line=156)
W('00,3733', 0o54002, '', 'TS', 'Q', 'STORE DELAY DT IN Q FOR DLY -1 IN', line=157)

W('00,3734', 0o36214, '', 'CAF', 'DELAYNUM', 'WAITLIST', line=159)
W('00,3735', 0o54070, 'DELLOOP', 'TS', 'RUPTREG1', line=160)
W('00,3736', 0o50000, '', 'INDEX', 'A', line=161)
W('00,3737', 0o31141, '', 'CA', 'DELAYLOC', 'IS THIS DELAYLOC AVAILABLE', line=162)
W('00,3740', 0o00006, '', 'EXTEND', line=163)
W('00,3741', 0o13746, '', 'BZF', 'OK2DELAY', 'YES', line=164)

W('00,3742', 0o10070, '', 'CCS', 'RUPTREG1', 'NO, TRY NEXT DELAYLOC', line=166)
W('00,3743', 0o13735, '', 'TCF', 'DELLOOP', line=167)

W('00,3744', 0o07755, '', 'TC', 'BAILOUT', 'NO AVAILABLE LOCS AVAILABLE.', line=169)
W('00,3745', 0o01104, '', 'OCT', '1104', kind='data', line=170)

W('00,3746', 0o33766, 'OK2DELAY', 'CA', 'TCSLEEP', 'SET WAITLIST IMMEDIATE RETURN', line=172)
W('00,3747', 0o54061, '', 'TS', 'WAITEXIT', line=173)

W('00,3750', 0o30004, '', 'CA', 'FBANK', line=175)
W('00,3751', 0o60070, '', 'AD', 'RUPTREG1', 'STORE BBANK FOR TASK CALL', line=176)
W('00,3752', 0o54001, '', 'TS', 'L', line=177)

W('00,3753', 0o33767, '', 'CAF', 'WAKECAD', 'STORE CADR FOR TASK CALL', line=179)
W('00,3754', 0o15255, '', 'TCF', 'DLY2 -1', 'DLY IS IN WAITLIST ROUTINE', line=180)

W('00,3755', 0o04711, 'TCGETCAD', 'TC', 'MAKECADR', 'GET CALLERS FCADR', line=182)

W('00,3756', 0o50070, '', 'INDEX', 'RUPTREG1', line=184)
W('00,3757', 0o55141, '', 'TS', 'DELAYLOC', 'SAVE DELAY CADRS', line=185)

W('00,3760', 0o05175, '', 'TC', 'JOBSLEEP', line=187)

W('00,3761', 0o35021, 'WAKER', 'CAF', 'ZERO', line=189)
W('00,3762', 0o50006, '', 'INDEX', 'BBANK', line=190)
W('00,3763', 0o57141, '', 'XCH', 'DELAYLOC', 'MAKE DELAYLOC AVAILABLE', line=191)
# Page 1489
W('00,3764', 0o05201, '', 'TC', 'JOBWAKE', line=193)

W('00,3765', 0o05324, '', 'TC', 'TASKOVER', line=195)

W('00,3766', 0o03753, 'TCSLEEP', 'GENADR', 'TCGETCAD -2', kind='data', line=197)
W('00,3767', 0o03761, 'WAKECAD', 'GENADR', 'WAKER', kind='data', line=198)

# Page 1490
# GENTRAN, A BLOCK TRANSFER ROUTINE.
#
# WRITTEN BY D. EYLES
# MOD 1 BY KERNAN                               UTILITYM REV 17 11/18/67
#
# MOD 2 BY SCHULENBERG (REMOVE RELINT)  SKIPPER REV 4 2/28/68
#
# THIS ROUTINE IS USEFULL FOR TRANSFERING N CONSECUTIVE ERASABLE OR FIXED QUANTITIES TO SOME OTHER N
# CONSECUTIVE ERASABLE LOCATIONS.  IF BOTH BLOCKS OF DATA ARE IN SWITCHABLE EBANKS, THEY MUST BE IN THE SAME ONE.
#
# GENTRAN IS CALLABLE IN A JOB AS WELL AS A RUPT.  THE CALLING SEQUENCE IS:
#
# I       CA      N-1             # # OF QUANTITIES MINUS ONE.
# I +1    TC      GENTRAN         # IN FIXED-FIXED.
# I +2    ADRES   L               # STARTING ADRES OF DATA TO BE MOVED.
# I +3    ADRES   M               # STARTING ADRES OF DUPLICATION BLOCK.
# I +4                            # RETURNS HERE.
#
# GENTRAN TAKES 25 MCT'S (300 MICROSECONDS) PER ITEM + 5 MCT'S (60 MICS) FOR ENTERING AND EXITING.
#
# A, L AND ITEMP1 ARE NOT PRESERVED.

#   BLOCK 02
#   SETLOC FFTAG4
#   BANK

#   EBANK= ITEMP1

#   COUNT* $$/TRAN

W('5606', 0o00004, 'GENTRAN', 'INHINT', line=231)
W('5607', 0o54061, '', 'TS', 'ITEMP1', 'SAVE N-1.', line=232)
W('5610', 0o50002, '', 'INDEX', 'Q', 'C(Q) = ADRES L.', line=233)
W('5611', 0o60000, '', 'AD', '0', 'ADRES (L + N - 1).', line=234)
W('5612', 0o50000, '', 'INDEX', 'A', line=235)
W('5613', 0o30000, '', 'CA', '0', 'C(ABOVE).', line=236)
W('5614', 0o54001, '', 'TS', 'L', 'SAVE DATA.', line=237)
W('5615', 0o30061, '', 'CA', 'ITEMP1', line=238)
W('5616', 0o50002, '', 'INDEX', 'Q', line=239)
W('5617', 0o60001, '', 'AD', '1', 'ADRES (M + N - 1).', line=240)
W('5620', 0o50000, '', 'INDEX', 'A', line=241)
W('5621', 0o22000, '', 'LXCH', '0', 'STUFF IT.', line=242)
W('5622', 0o10061, '', 'CCS', 'ITEMP1', 'LOOP UNTIL N-1 = 0.', line=243)
W('5623', 0o15607, '', 'TCF', 'GENTRAN +1', line=244)
W('5624', 0o16710, '', 'TCF', 'Q+2', 'RETURN TO CALLER.', line=245)

# Page 1491
# B5OFF         ZERO BIT 5 OF EXTVBACT, WHICH IS SET BY TESTXACT.
#
# MAY BE USED AS NEEDED BY ANY EXTENDED VERB WHICH HAS DONE TESTXACT

#   COUNT* $$/EXTVB

W('5625', 0o45013, 'B5OFF', 'CS', 'BIT5', line=254)
W('5626', 0o71044, '', 'MASK', 'EXTVBACT', line=255)
W('5627', 0o55044, '', 'TS', 'EXTVBACT', line=256)
W('5630', 0o05217, '', 'TC', 'ENDOFJOB', line=257)

# Page 1492
# SUBROUTINES TO TURN OFF AND TURN ON TRACKER FAIL LIGHT.

W('5631', 0o00004, 'TRFAILOF', 'INHINT', line=263)
W('5632', 0o47704, '', 'CS', 'OCT40200', 'TURN OFF TRACKER LIGHT', line=264)
W('5633', 0o71036, '', 'MASK', 'DSPTAB +11D', line=265)
W('5634', 0o65001, '', 'AD', 'BIT15', line=266)
W('5635', 0o55036, '', 'TS', 'DSPTAB +11D', line=267)
W('5636', 0o41331, '', 'CS', 'OPTMODES', 'TO INSURE THAT OCDU FAIL WILL GO ON', line=268)
W('5637', 0o75011, '', 'MASK', 'BIT7', 'AGAIN IF IT WAS ON IN ADDITION TO', line=269)
W('5640', 0o27331, '', 'ADS', 'OPTMODES', 'TRACKER FAIL.', line=270)

W('5641', 0o00003, 'REQ', 'RELINT', line=272)
W('5642', 0o00002, '', 'TC', 'Q', line=273)

W('5643', 0o00004, 'TRFAILON', 'INHINT', line=275)
W('5644', 0o41036, '', 'CS', 'DSPTAB +11D', 'TURN ON', line=276)
W('5645', 0o77704, '', 'MASK', 'OCT40200', line=277)
W('5646', 0o27036, '', 'ADS', 'DSPTAB +11D', line=278)
W('5647', 0o15641, '', 'TCF', 'REQ', line=279)
