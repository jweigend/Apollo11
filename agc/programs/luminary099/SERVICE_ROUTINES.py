"""SERVICE_ROUTINES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/SERVICE_ROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1374-1380 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('SERVICE_ROUTINES', 'SERVICE_ROUTINES.agc', 'Luminary099', pages='1374-1380')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     SERVICE_ROUTINES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1374-1380
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Luminary131/ file of the same
# name, using Luminary099 page images.
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

# Page 1374
#   BANK 10
#   SETLOC DISPLAYS
#   BANK
#   COUNT* $$/DSPLA

W('10,3544', 0o00004, 'UPENT2', 'INHINT', line=35)
W('10,3545', 0o75660, '', 'MASK', 'OCT77770', line=36)
W('10,3546', 0o54001, '', 'TS', 'L', line=37)
W('10,3547', 0o40100, '', 'CS', 'FLAGWRD4', line=38)
W('10,3550', 0o70001, '', 'MASK', 'L', line=39)
W('10,3551', 0o26100, '', 'ADS', 'FLAGWRD4', line=40)
W('10,3552', 0o00003, 'JOIN', 'RELINT', line=41)
W('10,3553', 0o16737, '', 'TCF', 'Q+1', line=42)

W('10,3554', 0o00004, 'DOWNENT2', 'INHINT', line=44)
W('10,3555', 0o75660, '', 'MASK', 'OCT77770', line=45)
W('10,3556', 0o40000, '', 'COM', line=46)
W('10,3557', 0o70100, '', 'MASK', 'FLAGWRD4', line=47)
W('10,3560', 0o54100, '', 'TS', 'FLAGWRD4', line=48)
W('10,3561', 0o13552, '', 'TCF', 'JOIN', line=49)

S('OCT7', 'equals', 0o4757, line=51)

# Page 1375
# UPFLAG AND DOWNFLAG ARE ENTIRELY GENERAL FLAG SETTING AND CLEARING SUBROUTINES.   USING THEM, WHETHER OR
# NOT IN INTERRUPT, ONE MAY SET OR CLEAR ANY SINGLE, NAMED BIT IN ANY ERASABLE REGISTER, SUBJECT OF COURSE TO
# EBANK SETTING.   A "NAMED" BIT, AS THE WORD IS USED HERE, IS ANY BIT WITH A NAME FORMALLY ASSIGNED BY THE YUL
# ASSEMBLER.
#
# AT PRESENT THE ONLY NAMED BITS ARE THOSE IN THE FLAGWORDS.   ASSEMBLER CHANGES WILL MAKE IT POSSIBLE TO
# NAME ANY BIT IN ERASABLE MEMORY.
#
# CALLING SEQUENCES ARE AS FOLLOWS :-
# TC      UPFLAG                  TC      DOWNFLAG
# ADRES   NAME OF FLAG            ADRES   NAME OF FLAG
#
# RETURN IS TO THE LOCATION FOLLOWING THE "ADRES" ABOUT .58 MS AFTER THE "TC".
# UPON RETURN A CONTAINS THE CURRENT FLAGWRD SETTING.

#   BLOCK 02
#   SETLOC FFTAG1
#   BANK
#   COUNT* $$/FLAG

W('5504', 0o30002, 'UPFLAG', 'CA', 'Q', line=74)
W('5505', 0o05522, '', 'TC', 'DEBIT', line=75)
W('5506', 0o40000, '', 'COM', '', '+(15 - BIT)', line=76)
W('5507', 0o00006, '', 'EXTEND', line=77)
W('5510', 0o04001, '', 'ROR', 'LCHAN', 'SET BIT', line=78)
W('5511', 0o50061, 'COMFLAG', 'INDEX', 'ITEMP1', line=79)
W('5512', 0o54074, '', 'TS', 'FLAGWRD0', line=80)
W('5513', 0o22063, '', 'LXCH', 'ITEMP3', line=81)
W('5514', 0o00003, '', 'RELINT', line=82)
W('5515', 0o00001, '', 'TC', 'L', line=83)

W('5516', 0o30002, 'DOWNFLAG', 'CA', 'Q', line=85)
W('5517', 0o05522, '', 'TC', 'DEBIT', line=86)
W('5520', 0o70001, '', 'MASK', 'L', 'RESET BIT', line=87)
W('5521', 0o15511, '', 'TCF', 'COMFLAG', line=88)

W('5522', 0o64753, 'DEBIT', 'AD', 'ONE', 'CET DE BITS', line=90)
W('5523', 0o00004, '', 'INHINT', line=91)
W('5524', 0o54063, '', 'TS', 'ITEMP3', line=92)
W('5525', 0o34762, '', 'CA', 'LOW4', 'DEC15', line=93)
W('5526', 0o54061, '', 'TS', 'ITEMP1', line=94)
W('5527', 0o50063, '', 'INDEX', 'ITEMP3', line=95)
W('5530', 0o27777, '', 'CA', '0 -1', 'ADRES', line=96)
W('5531', 0o54001, '', 'TS', 'L', line=97)
W('5532', 0o34755, '', 'CA', 'ZERO', line=98)
# Page 1376
W('5533', 0o00006, '', 'EXTEND', line=100)
W('5534', 0o10061, '', 'DV', 'ITEMP1', 'A = FLAGWRD, L = (15 - BIT)', line=101)
W('5535', 0o52062, '', 'DXCH', 'ITEMP1', line=102)
W('5536', 0o50061, '', 'INDEX', 'ITEMP1', line=103)
W('5537', 0o30074, '', 'CA', 'FLAGWRD0', line=104)
W('5540', 0o54001, '', 'TS', 'L', 'CURRENT STATE', line=105)
W('5541', 0o50062, '', 'INDEX', 'ITEMP2', line=106)
W('5542', 0o44735, '', 'CS', 'BIT15', '-(15 - BIT)', line=107)
W('5543', 0o00002, '', 'TC', 'Q', line=108)

# Page 1377
# DELAYJOB- A GENERAL ROUTINE TO DELAY A JOB A SPECIFIC AMOUNT OF TIME BEFORE PICKING UP AGAIN.
#
# ENTRANCE REQUIREMENTS...
# CAF     DT              # DELAY JOB FOR DT CENTISECS
# TC      BANKCALL
# CADR    DELAYJOB

#   BANK 06
#   SETLOC DLAYJOB
#   BANK

# THIS MUST REMAIN IN BANK 0 *****************************************

#   COUNT* $$/DELAY
W('00,3735', 0o00004, 'DELAYJOB', 'INHINT', line=125)
W('00,3736', 0o54002, '', 'TS', 'Q', 'STORE DELAY DT IN Q FOR DLY -1 IN', line=126)
W('00,3737', 0o34752, '', 'CAF', 'DELAYNUM', 'WAITLIST', line=127)
W('00,3740', 0o54070, 'DELLOOP', 'TS', 'RUPTREG1', line=128)
W('00,3741', 0o50000, '', 'INDEX', 'A', line=129)
W('00,3742', 0o31326, '', 'CA', 'DELAYLOC', 'IS THIS DELAYLOC AVAILABLE', line=130)
W('00,3743', 0o00006, '', 'EXTEND', line=131)
W('00,3744', 0o13752, '', 'BZF', 'OK2DELAY', 'YES', line=132)

W('00,3745', 0o10070, '', 'CCS', 'RUPTREG1', 'NO, TRY NEXT DELAYLOC', line=134)
W('00,3746', 0o13740, '', 'TCF', 'DELLOOP', line=135)

W('00,3747', 0o52134, '', 'DXCH', 'BUF2', line=137)
W('00,3750', 0o05716, '', 'TC', 'BAILOUT1', 'NO AVAILABLE LOCS.', line=138)
W('00,3751', 0o01104, '', 'OCT', '1104', kind='data', line=139)

W('00,3752', 0o33772, 'OK2DELAY', 'CA', 'TCSLEEP', 'SET WAITLIST IMMEDIATE RETURN', line=141)
W('00,3753', 0o54061, '', 'TS', 'WAITEXIT', line=142)

W('00,3754', 0o30004, '', 'CA', 'FBANK', line=144)
W('00,3755', 0o60070, '', 'AD', 'RUPTREG1', 'STORE BBANK FOR TASK CALL', line=145)
W('00,3756', 0o54001, '', 'TS', 'L', line=146)

W('00,3757', 0o33773, '', 'CAF', 'WAKECAD', 'STORE CADR FOR TASK CALL', line=148)
W('00,3760', 0o15211, '', 'TCF', 'DLY2 -1', 'DLY IS IN WAITLIST ROUTINE', line=149)

W('00,3761', 0o04645, 'TCGETCAD', 'TC', 'MAKECADR', 'GET CALLERS FCADR', line=151)

W('00,3762', 0o50070, '', 'INDEX', 'RUPTREG1', line=153)
W('00,3763', 0o55326, '', 'TS', 'DELAYLOC', 'SAVE DELAY CADRS', line=154)

W('00,3764', 0o05133, '', 'TC', 'JOBSLEEP', line=156)

W('00,3765', 0o34755, 'WAKER', 'CAF', 'ZERO', line=158)
W('00,3766', 0o50006, '', 'INDEX', 'BBANK', line=159)
W('00,3767', 0o57326, '', 'XCH', 'DELAYLOC', 'MAKE DELAYLOC AVAILABLE', line=160)
# Page 1378
W('00,3770', 0o05137, '', 'TC', 'JOBWAKE', line=162)

W('00,3771', 0o05261, '', 'TC', 'TASKOVER', line=164)

W('00,3772', 0o03757, 'TCSLEEP', 'GENADR', 'TCGETCAD -2', kind='data', line=166)
W('00,3773', 0o03765, 'WAKECAD', 'GENADR', 'WAKER', kind='data', line=167)

# Page 1379
# GENTRAN, A BLOCK TRANSFER ROUTINE.
# WRITTEN BY D. EYLES
# MOD 1 BY KERNAN                                               UTILITYM REV 17 11/18/67
# MOD 2 BY SCHULENBERG (REMOVE RELINT)   SKIPPER REV 4 2/28/68
#
# THIS ROUTINE IS USEFULL FOR TRANSFERING N CONSECUTIVE ERASABLE OR FIXED QUANTITIES TO SOME OTHER N
# CONSECUTIVE ERASABLE LOCATIONS.  IF BOTH BLOCKS OF DATA ARE IN SWITCHABLE EBANKS, THEY MUST BE IN THE SAME ONE.
#
# GENTRAN IS CALLABLE IN A JOB AS WELL AS A RUPT.  THE CALLING SEQUENCE IS:
# I       CA      N-1             # # OF QUANTITIES MINUS ONE.
# I +1    TC      GENTRAN         # IN FIXED-FIXED.
# I +2    ADRES   L               # STARTING ADRES OF DATA TO BE MOVED.
# I +3    ADRES   M               # STARTING ADRES OF DUPLICATION BLOCK.
# I +4                            # RETURNS HERE.
#
# GENTRAN TAKES 25 MCT'S (300 MICROSECONDS) PER ITEM + 5 MCT'S (60 MICS) FOR ENTERING AND EXITING.
# A, L, AND ITEMP1 ARE NOT PRESERVED.

#   BLOCK 02
#   SETLOC FFTAG4
#   BANK

#   EBANK= ITEMP1

#   COUNT* $$/TRAN

W('5544', 0o00004, 'GENTRAN', 'INHINT', line=196)
W('5545', 0o54061, '', 'TS', 'ITEMP1', 'SAVE N-1.', line=197)
W('5546', 0o50002, '', 'INDEX', 'Q', 'C(Q) = ADRES L.', line=198)
W('5547', 0o60000, '', 'AD', '0', 'ADRES (L + N - 1).', line=199)
W('5550', 0o50000, '', 'INDEX', 'A', line=200)
W('5551', 0o30000, '', 'CA', '0', 'C(ABOVE).', line=201)
W('5552', 0o54001, '', 'TS', 'L', 'SAVE DATA.', line=202)
W('5553', 0o30061, '', 'CA', 'ITEMP1', line=203)
W('5554', 0o50002, '', 'INDEX', 'Q', line=204)
W('5555', 0o60001, '', 'AD', '1', 'ADRES (M + N - 1).', line=205)
W('5556', 0o50000, '', 'INDEX', 'A', line=206)
W('5557', 0o22000, '', 'LXCH', '0', 'STUFF IT.', line=207)
W('5560', 0o10061, '', 'CCS', 'ITEMP1', 'LOOP UNTIL N-1 = 0.', line=208)
W('5561', 0o15545, '', 'TCF', 'GENTRAN +1', line=209)
W('5562', 0o16741, '', 'TCF', 'Q+2', 'RETURN TO CALLER.', line=210)

# Page 1380
# B5OFF   ZERO BIT 5 OF EXTVBACT, WHICH IS SET BY TESTXACT.
# MAY BE USED AS NEEDED BY ANY EXTENDED VERB WHICH HAS DONE TESTXACT

#   COUNT* $$/EXTVB

W('5563', 0o44747, 'B5OFF', 'CS', 'BIT5', line=218)
W('5564', 0o71044, '', 'MASK', 'EXTVBACT', line=219)
W('5565', 0o55044, '', 'TS', 'EXTVBACT', line=220)
W('5566', 0o05155, '', 'TC', 'ENDOFJOB', line=221)
