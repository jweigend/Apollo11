"""INTER-BANK_COMMUNICATION.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/INTER-BANK_COMMUNICATION.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 998-1001 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INTER_BANK_COMMUNICATION', 'INTER-BANK_COMMUNICATION.agc', 'Luminary099', pages='998-1001')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INTER-BANK_COMMUNICATION.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        998-1001
# Mod history:  2009-05-24 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2011-05-08 JL   Removed workaround.

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

# Page 998
# THE FOLLOWING ROUTINE CAN BE USED TO CALL A SUBROUTINE IN ANOTHER BANK. IN THE BANKCALL VERSION, THE
# CADR OF THE SUBROUTINE IMMEDIATELY FOLLOWS THE  TC BANKCALL  INSTRUCTION, WITH C(A) AND C(L) PRESERVED.

#   BLOCK 02
#   COUNT* $$/BANK
W('4616', 0o52134, 'BANKCALL', 'DXCH', 'BUF2', 'SAVE INCOMING A,L.', line=36)
W('4617', 0o50002, '', 'INDEX', 'Q', 'PICK UP CADR.', line=37)
W('4620', 0o30000, '', 'CA', '0', line=38)
W('4621', 0o24002, '', 'INCR', 'Q', 'SO WE RETURN TO THE LOC. AFTER THE CADR.', line=39)

# SWCALL IS IDENTICAL TO BANKCALL, EXCEPT THAT THE CADR ARRIVES IN A.

W('4622', 0o54001, 'SWCALL', 'TS', 'L', line=43)
W('4623', 0o22004, '', 'LXCH', 'FBANK', 'SWITCH BANKS, SAVING RETURN.', line=44)
W('4624', 0o75012, '', 'MASK', 'LOW10', 'GET SUB-ADDRESS OF CADR.', line=45)
W('4625', 0o56002, '', 'XCH', 'Q', 'A,L NOW CONTAINS DP RETURN.', line=46)
W('4626', 0o52134, '', 'DXCH', 'BUF2', 'RESTORING INPUTS IF THIS IS A BANKCALL.', line=47)
W('4627', 0o50002, '', 'INDEX', 'Q', line=48)
W('4630', 0o02000, '', 'TC', '10000', 'SETTING Q TO SWRETURN.', line=49)

W('4631', 0o56134, 'SWRETURN', 'XCH', 'BUF2 +1', 'COMES HERE TO RETURN TO CALLER. C(A,L)', line=51)
W('4632', 0o56004, '', 'XCH', 'FBANK', 'ARE PRESERVED FOR RETURN.', line=52)
W('4633', 0o56134, '', 'XCH', 'BUF2 +1', line=53)
W('4634', 0o00133, '', 'TC', 'BUF2', line=54)

# THE FOLLOWING ROUTINE CAN BE USED AS A UNILATERAL JUMP WITH C(A,L) PRESERVED AND THE CADR IMMEDIATELY
# FOLLOWING THE TC POSTJUMP INSTRUCTION.

W('4635', 0o56002, 'POSTJUMP', 'XCH', 'Q', 'SAVE INCOMING C(A).', line=59)
W('4636', 0o50000, '', 'INDEX', 'A', 'GET CADR.', line=60)
W('4637', 0o30000, '', 'CA', '0', line=61)

# BANKJUMP IS THE SAME AS POSTJUMP, EXCEPT THAT THE CADR ARRIVES IN A.

W('4640', 0o54004, 'BANKJUMP', 'TS', 'FBANK', line=65)
W('4641', 0o75012, '', 'MASK', 'LOW10', line=66)
W('4642', 0o56002, '', 'XCH', 'Q', 'RESTORING INPUT C(A) IF THIS WAS A', line=67)
W('4643', 0o50002, 'Q+10000', 'INDEX', 'Q', 'POSTJUMP.', line=68)
W('4644', 0o12000, 'PRIO12', 'TCF', '10000', 'PRIO12 = TCF   10000 = 12000', line=69)

# Page 999
# THE FOLLOWING ROUTINE GETS THE RETURN CADR SAVED BY SWCALL OR BANKCALL AND LEAVES IT IN A.

W('4645', 0o35012, 'MAKECADR', 'CAF', 'LOW10', line=74)
W('4646', 0o70133, '', 'MASK', 'BUF2', line=75)
W('4647', 0o60134, '', 'AD', 'BUF2 +1', line=76)
W('4650', 0o00002, '', 'TC', 'Q', line=77)

W('4651', 0o54135, 'SUPDACAL', 'TS', 'MPTEMP', line=79)
W('4652', 0o56004, '', 'XCH', 'FBANK', 'SET FBANK FOR DATA.', line=80)
W('4653', 0o00006, '', 'EXTEND', line=81)
W('4654', 0o04007, '', 'ROR', 'SUPERBNK', 'SAVE FBANK IN BITS 15-11, AND', line=82)
W('4655', 0o56135, '', 'XCH', 'MPTEMP', ' SUPERBANK IN BITS  7-5.', line=83)
W('4656', 0o75012, '', 'MASK', 'LOW10', line=84)
W('4657', 0o56001, '', 'XCH', 'L', 'SAVE REL. ADR. IN BANK, FETCH SUPERBITS.', line=85)
W('4660', 0o00004, '', 'INHINT', '', 'BECAUSE RUPT DOES NOT SAVE SUPERBANK.', line=86)
W('4661', 0o00006, '', 'EXTEND', line=87)
W('4662', 0o01007, '', 'WRITE', 'SUPERBNK', 'SET SUPERBANK FOR DATA.', line=88)
W('4663', 0o50001, '', 'INDEX', 'L', line=89)
W('4664', 0o32000, '', 'CA', '10000', 'PINBALL (FIX MEM DISP) PREVENTS DCA HERE', line=90)
W('4665', 0o56135, '', 'XCH', 'MPTEMP', 'SAVE 1ST WD, FETCH OLD FBANK AND SBANK.', line=91)
W('4666', 0o00006, '', 'EXTEND', line=92)
W('4667', 0o01007, '', 'WRITE', 'SUPERBNK', 'RESTORE SUPERBANK.', line=93)
W('4670', 0o00003, '', 'RELINT', line=94)
W('4671', 0o54004, '', 'TS', 'FBANK', 'RESTORE FBANK.', line=95)
W('4672', 0o30135, '', 'CA', 'MPTEMP', 'RECOVER FIRST WORD OF DATA.', line=96)
W('4673', 0o00002, '', 'RETURN', '', '24 WDS. DATACALL 516 MU, SUPDACAL 432 MU', line=97)

# Page 1000
# THE FOLLOWING ROUTINES ARE IDENTICAL TO BANKCALL AND SWCALL EXCEPT THAT THEY ARE USED IN INTERRUPT.

W('4674', 0o52073, 'IBNKCALL', 'DXCH', 'RUPTREG3', 'USES RUPTREG3,4 FOR DP RETURN ADDRESS.', line=102)
W('4675', 0o50002, '', 'INDEX', 'Q', line=103)
W('4676', 0o30000, '', 'CAF', '0', line=104)
W('4677', 0o24002, '', 'INCR', 'Q', line=105)

W('4700', 0o54001, 'ISWCALLL', 'TS', 'L', line=107)
W('4701', 0o22004, '', 'LXCH', 'FBANK', line=108)
W('4702', 0o75012, '', 'MASK', 'LOW10', line=109)
W('4703', 0o56002, '', 'XCH', 'Q', line=110)
W('4704', 0o52073, '', 'DXCH', 'RUPTREG3', line=111)
W('4705', 0o50002, '', 'INDEX', 'Q', line=112)
W('4706', 0o02000, '', 'TC', '10000', line=113)

W('4707', 0o56073, 'ISWRETRN', 'XCH', 'RUPTREG4', line=115)
W('4710', 0o56004, '', 'XCH', 'FBANK', line=116)
W('4711', 0o56073, '', 'XCH', 'RUPTREG4', line=117)
W('4712', 0o00072, '', 'TC', 'RUPTREG3', line=118)

# 2. USPRCADR ACCESSES INTERPRETIVE CODING IN OTHER THAN THE USER'S FBANK.  THE CALLING SEQUENCE IS AS FOLLOWS:

# L             TC      USPRCADR
# L+1           CADR    INTPRETX          INTPRETX IS THE INTERPRETIVE CODING
# RETURN IS TO L+2

W('4713', 0o54164, 'USPRCADR', 'TS', 'LOC', 'SAVE A', line=126)
W('4714', 0o34744, '', 'CA', 'BIT8', line=127)
W('4715', 0o54023, '', 'TS', 'EDOP', 'EXIT INSTRUCTION TO EDOP', line=128)
W('4716', 0o30006, '', 'CA', 'BBANK', line=129)
W('4717', 0o54165, '', 'TS', 'BANKSET', "USER'S BBANK TO BANKSET", line=130)
W('4720', 0o50002, '', 'INDEX', 'Q', line=131)
W('4721', 0o30000, '', 'CA', '0', line=132)
W('4722', 0o54004, '', 'TS', 'FBANK', 'INTERPRETIVE BANK TO FBANK', line=133)
W('4723', 0o75012, '', 'MASK', 'LOW10', 'YIELDS INTERPRETIVE RELATIVE ADDRESS', line=134)
W('4724', 0o56002, '', 'XCH', 'Q', 'INTERPRETIVE ADDRESS TO Q, FETCHING L+1', line=135)
W('4725', 0o56164, '', 'XCH', 'LOC', 'L+1 TO LOC, RETRIEVING ORIGINAL A', line=136)
W('4726', 0o14643, '', 'TCF', 'Q+10000', line=137)

# Page 1001
# THERE ARE FOUR POSSIBLE SETTINGS FOR CHANNEL 07. (CHANNEL 07 CONTAINS SUPERBANK SETTING.)
# PSEUDO-FIXED      OCTAL PSEUDO
# SUPERBANK     SETTING     S-REG. VALUE    BANK NUMBERS      ADDRESSES
# ----------    -------     ------------     ------------      ------------
#
# SUPERBANK 3     OXX       2000 - 3777        30 - 37        70000 - 107777    (WHERE XX CAN BE ANYTHING AND
# WILL USUALLY BE SEEN AS 11)
# SUPERBANK 4     100       2000 - 3777        40 - 47        110000 - 127777   (AS FAR AS IT CAN BE SEEN,
# ONLY BANKS 40-43 WILL EVER BE
# AND ARE PRESENTLY AVAILABLE)
# SUPERBANK 5     101       2000 - 3777        50 - 57        130000 - 147777   (PRESENTLY NOT AVAILABLE TO
# THE USER)
# SUPERBANK 6     110       2000 - 3777        60 - 67        150000 - 167777   (PRESENTLY NOT AVAILABLE TO
# THE USER)
# ***  THIS ROUTINE MAYBE CALLED BY ANY PROGRAM LOCATED IN BANKS 00 - 27.  I.E., NO PROGRAM LIVING IN ANY
# SUPERBANK SHOULD USE SUPERSW.  ***
#
# SUPERSW MAYBE CALLED IN THIS FASHION:
#
# CAF    ABBCON          WHERE  --  ABBCON   BBCON  SOMETHIN  --
# TCR    SUPERSW         (THE SUPERBNK BITS ARE IN THE BBCON)
# ...      ...
# .        .
# .        .
# OR IN THIS FASHION :
# CAF    SUPERSET        WHERE SUPERSET IS ONE OF THE FOUR AVAILABLE
# TCR    SUPERSW         SUPERBANK BIT CONSTANTS:
# ...      ...                                   SUPER011 OCTAL  60
# .        .                                    SUPER100 OCTAL 100
# .        .                                    SUPER101 OCTAL 120
# SUPER110 OCTAL 140

W('4727', 0o00006, 'SUPERSW', 'EXTEND', line=172)
W('4730', 0o01007, '', 'WRITE', 'SUPERBNK', 'WRITE BITS 7-6-5 OF THE ACCUMULATOR INTO', line=173)
# CHANNEL 07
W('4731', 0o00002, '', 'TC', 'Q', 'TC TO INSTRUCTION FOLLOWING', line=175)
# TC  SUPERSW
