"""INTER-BANK_COMMUNICATION.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/INTER-BANK_COMMUNICATION.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1103-1106 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INTER_BANK_COMMUNICATION', 'INTER-BANK_COMMUNICATION.agc', 'Comanche055', pages='1103-1106')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INTER-BANK_COMMUNICATION.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 1103-1106
# Contact:      Ron Burkey <info@sandroid.org>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-08 RSB  Adapted from Colossus249/ file of same name
# and page images. Corrected various typos
# in the transcription of program comments,
# and these should be back-ported to
# Colossus249.
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

# Page 1103
# THE FOLLOWING ROUTINE CAN BE USED TO CALL A SUBROUTINE IN ANOTHER BANK. IN THE BANKCALL VERSION, THE
# CADR OF THE SUBROUTINE IMMEDIATELY FOLLOWS THE TC BANKCALL INSTRUCTION, WITH C(A) AND C(L) PRESERVED.

#   BLOCK 02
#   COUNT 02/BANK

W('4662', 0o52134, 'BANKCALL', 'DXCH', 'BUF2', 'SAVE INCOMING A,L.', line=41)
W('4663', 0o50002, '', 'INDEX', 'Q', 'PICK UP CADR.', line=42)
W('4664', 0o30000, '', 'CA', '0', line=43)
W('4665', 0o24002, '', 'INCR', 'Q', 'SO WE RETURN TO THE LOC. AFTER THE CADR.', line=44)

# SWCALL IS  IDENTICAL TO BANKCALL, EXCEPT THAT THE CADR ARRIVES IN A.

W('4666', 0o54001, 'SWCALL', 'TS', 'L', line=48)
W('4667', 0o22004, '', 'LXCH', 'FBANK', 'SWITCH BANKS, SAVING RETURN.', line=49)
W('4670', 0o75054, '', 'MASK', 'LOW10', 'GET SUB-ADDRESS OF CADR.', line=50)
W('4671', 0o56002, '', 'XCH', 'Q', 'A,L NOW CONTAINS DP RETURN.', line=51)
W('4672', 0o52134, '', 'DXCH', 'BUF2', 'RESTORING INPUTS IF THIS IS A BANKCALL.', line=52)
W('4673', 0o50002, '', 'INDEX', 'Q', line=53)
W('4674', 0o02000, '', 'TC', '10000', 'SETTING Q TO SWRETURN', line=54)

W('4675', 0o56134, 'SWRETURN', 'XCH', 'BUF2 +1', 'COMES HERE TO RETURN TO CALLER. C(A,L)', line=56)
W('4676', 0o56004, '', 'XCH', 'FBANK', 'ARE PRESERVED FOR RETURN.', line=57)
W('4677', 0o56134, '', 'XCH', 'BUF2 +1', line=58)
W('4700', 0o00133, '', 'TC', 'BUF2', line=59)

# THE FOLLOWING ROUTINE CAN BE USED AS A UNILATERAL JUMP WITH C(A,L) PRESERVED AND THE CADR IMMEDIATELY
# FOLLOWING THE TC POSTJUMP INSTRUCTION.

W('4701', 0o56002, 'POSTJUMP', 'XCH', 'Q', 'SAVE INCOMING C(A).', line=64)
W('4702', 0o50000, '', 'INDEX', 'A', 'GET CADR.', line=65)
W('4703', 0o30000, '', 'CA', '0', line=66)

# BANKJUMP IS THE SAME AS POSTJUMP, EXCEPT THAT THE CADR ARRIVES IN A.

W('4704', 0o54004, 'BANKJUMP', 'TS', 'FBANK', line=70)
W('4705', 0o75054, '', 'MASK', 'LOW10', line=71)
W('4706', 0o56002, '', 'XCH', 'Q', 'RESTORING INPUT C(A) IF THIS WAS A', line=72)
W('4707', 0o50002, 'Q+10000', 'INDEX', 'Q', 'POSTJUMP.', line=73)
W('4710', 0o12000, 'PRIO12', 'TCF', '10000', 'PRIO12 = TCF  10000 = 12000', line=74)

# Page 1104
# THE FOLLOWING ROUTINE GETS THE RETURN CADR SAVED BY SWCALL OR BANKCALL AND LEAVES IT IN A.

W('4711', 0o35054, 'MAKECADR', 'CAF', 'LOW10', line=79)
W('4712', 0o70133, '', 'MASK', 'BUF2', line=80)
W('4713', 0o60134, '', 'AD', 'BUF2 +1', line=81)
W('4714', 0o00002, '', 'TC', 'Q', line=82)

W('4715', 0o54135, 'SUPDACAL', 'TS', 'MPTEMP', line=84)
W('4716', 0o56004, '', 'XCH', 'FBANK', 'SET FBANK FOR DATA.', line=85)
W('4717', 0o00006, '', 'EXTEND', line=86)
W('4720', 0o04007, '', 'ROR', 'SUPERBNK', 'SAVE FBANK IN BITS 15-11, AND', line=87)
W('4721', 0o56135, '', 'XCH', 'MPTEMP', 'SUPERBANK IN BITS 7-5.', line=88)
W('4722', 0o75054, '', 'MASK', 'LOW10', line=89)
W('4723', 0o56001, '', 'XCH', 'L', 'SAVE REL. ADR. IN BANK, FETCH SUPERBITS.', line=90)
W('4724', 0o00004, '', 'INHINT', '', 'BECAUSE RUPT DOES NOT SAVE SUPERBANK.', line=91)
W('4725', 0o00006, '', 'EXTEND', line=92)
W('4726', 0o01007, '', 'WRITE', 'SUPERBNK', 'SET SUPERBANK FOR DATA.', line=93)
W('4727', 0o50001, '', 'INDEX', 'L', line=94)
W('4730', 0o32000, '', 'CA', '10000', 'PINBALL (FIX MEM DISP) PREVENTS DCA HERE', line=95)
W('4731', 0o56135, '', 'XCH', 'MPTEMP', 'SAVE 1ST WD, FETCH OLD FBANK AND SBANK.', line=96)
W('4732', 0o00006, '', 'EXTEND', line=97)
W('4733', 0o01007, '', 'WRITE', 'SUPERBNK', 'RESTORE SUPERBANK.', line=98)
W('4734', 0o00003, '', 'RELINT', line=99)
W('4735', 0o54004, '', 'TS', 'FBANK', 'RESTORE FBANK.', line=100)
W('4736', 0o30135, '', 'CA', 'MPTEMP', 'RECOVER FIRST WORD OF DATA.', line=101)
W('4737', 0o00002, '', 'RETURN', '', '24 WDS. DATACALL 516 MU, SUPDACAL 432 MU', line=102)

# Page 1105
# THE FOLLOWING ROUTINES ARE IDENTICAL TO BANKCALL AND SWCALL EXCEPT THAT THEY ARE USED IN INTERRUPT.

W('4740', 0o52073, 'IBNKCALL', 'DXCH', 'RUPTREG3', 'USES RUPTREG3,4 FOR DP RETURN ADDRESS.', line=107)
W('4741', 0o50002, '', 'INDEX', 'Q', line=108)
# Was CAF --- RSB 2009
W('4742', 0o30000, '', 'CA', '0', line=110)
W('4743', 0o24002, '', 'INCR', 'Q', line=111)

W('4744', 0o54001, 'ISWCALL', 'TS', 'L', line=113)
W('4745', 0o22004, '', 'LXCH', 'FBANK', line=114)
W('4746', 0o75054, '', 'MASK', 'LOW10', line=115)
W('4747', 0o56002, '', 'XCH', 'Q', line=116)
W('4750', 0o52073, '', 'DXCH', 'RUPTREG3', line=117)
W('4751', 0o50002, '', 'INDEX', 'Q', line=118)
W('4752', 0o02000, '', 'TC', '10000', line=119)

W('4753', 0o56073, 'ISWRETRN', 'XCH', 'RUPTREG4', line=121)
W('4754', 0o56004, '', 'XCH', 'FBANK', line=122)
W('4755', 0o56073, '', 'XCH', 'RUPTREG4', line=123)
W('4756', 0o00072, '', 'TC', 'RUPTREG3', line=124)

# 2. USPRCADR ACCESSES INTERPRETIVE CODING IN OTHER THAN THE USER'S FBANK.  THE CALLING SEQUENCE IS AS FOLLOWS:
# L       TC      USPRCADR
# L+1     CADR    INTPRETX        # INTPRETX IS THE INTERPRETIVE CODING
# # RETURN IS TO L+2

W('4757', 0o54164, 'USPRCADR', 'TS', 'LOC', 'SAVE A', line=131)
W('4760', 0o35010, '', 'CA', 'BIT8', line=132)
W('4761', 0o54023, '', 'TS', 'EDOP', 'EXIT INSTRUCTION TO EDOP', line=133)
W('4762', 0o30006, '', 'CA', 'BBANK', line=134)
W('4763', 0o54165, '', 'TS', 'BANKSET', "USER'S BBANK TO BANKSET", line=135)
W('4764', 0o50002, '', 'INDEX', 'Q', line=136)
W('4765', 0o30000, '', 'CA', '0', line=137)
W('4766', 0o54004, '', 'TS', 'FBANK', 'INTERPRETIVE BANK TO FBANK', line=138)
W('4767', 0o75054, '', 'MASK', 'LOW10', 'YIELDS INTERPRETIVE RELATIVE ADDRESS', line=139)
W('4770', 0o56002, '', 'XCH', 'Q', 'INTERPRETIVE ADDRESS TO Q, FETCHING L+1', line=140)
W('4771', 0o56164, '', 'XCH', 'LOC', 'L+1 TO LOC, RETRIEVING ORIGINAL A', line=141)
W('4772', 0o14707, '', 'TCF', 'Q+10000', line=142)

# Page 1106
# THERE ARE FOUR POSSIBLE SETTINGS FOR CHANNEL 07.  (CHANNEL 07 CONTAINS SUPERBANK SETTING.)
#
# PSEUDO-FIXED     OCTAL PSEUDO
# SUPERBANK     SETTING S-REG. VALUE    BANK NUMBERS     ADDRESSES
# ----------    ------- ------------    ------------      ------------
# SUPERBANK 3     0XX   2000 - 3777        30 - 37       70000 - 107777         (WHERE XX CAN BE ANYTHING AND
# WILL USUALLY BE SEEN AS 11)
# SUPERBANK 4     100   2000 - 3777        40 - 47       110000 - 127777        (AS FAR AS IT CAN BE SEEN,
# ONLY BANKS 40-43 WILL EVER BE
# AND ARE PRESENTLY AVAILABLE)
# SUPERBANK 5     101   2000 - 3777        50 - 57       130000 - 147777        (PRESENTLY NOT AVAILABLE TO
# THE USER)
# SUPERBANK 6     110   2000 - 3777        60 - 67       150000 - 167777        (PRESENTLY NOT AVAILABLE TO
# THE USER)
# ***  THIS ROUTINE MAYBE CALLED BY ANY PROGRAM LOCATED IN BANKS 00 - 27.  I.E., NO PROGRAM LIVING IN ANY
# SUPERBANK SHOULD USE SUPERSW.  ***
#
# SUPERSW MAYBE CALLED IN THIS FASHION:
# CAF     ABBCON          WHERE  --  ABBCON   BBCON  SOMETHIN  --
# TCR     SUPERSW         (THE SUPERBNK BITS ARE IN THE BBCON)
# ...       ...
# .         .
# .         .
# OR IN THIS FASHION :
# CAF     SUPERSET        WHERE SUPERSET IS ONE OF THE FOUR AVAILABLE
# TCR     SUPERSW         SUPERBANK BIT CONSTANTS:
# ...       ...                   SUPER011 OCTAL  60
# .         .                    SUPER100 OCTAL 100
# .         .                    SUPER101 OCTAL 120
# SUPER110 OCTAL 140

W('4773', 0o00006, 'SUPERSW', 'EXTEND', line=176)
W('4774', 0o01007, '', 'WRITE', 'SUPERBNK', 'WRITE BITS 7-6-5 OF THE ACCUMULATOR INTO', line=177)
# CHANNEL 07
W('4775', 0o00002, '', 'TC', 'Q', 'TC TO INSTRUCTION FOLLOWING', line=179)
# TC SUPERSW
