"""ALARM_AND_ABORT.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/ALARM_AND_ABORT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1493-1496 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('ALARM_AND_ABORT', 'ALARM_AND_ABORT.agc', 'Comanche055', pages='1493-1496')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     ALARM_AND_ABORT.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 1493-1496
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

# Page 1493
# THE FOLLOWING SUBROUTINE MAY BE CALLED TO DISPLAY A NON-ABORTIVE ALARM CONDITION. IT MAY BE CALLED
# EITHER IN INTERRUPT OR UNDER EXECUTIVE CONTROL.
#
# CALLING SEQUENCE IS AS FOLLOWS:
#
# TC      ALARM
# OCT     NNNNN
# # (RETURNS HERE)
#   BLOCK 02
#   SETLOC FFTAG7
#   BANK

#   EBANK= FAILREG

#   COUNT 02/ALARM

# ALARM TURNS ON THE PROGRAM ALARM LIGHT, BUT DOES NOT DISPLAY.

W('5650', 0o00004, 'ALARM', 'INHINT', line=53)

W('5651', 0o30002, '', 'CA', 'Q', line=55)
W('5652', 0o55363, 'ALARM2', 'TS', 'ALMCADR', line=56)
W('5653', 0o50002, '', 'INDEX', 'Q', line=57)
W('5654', 0o30000, '', 'CA', '0', line=58)
W('5655', 0o54001, 'BORTENT', 'TS', 'L', line=59)

W('5656', 0o30006, 'PRIOENT', 'CA', 'BBANK', line=61)
W('5657', 0o00006, '', 'EXTEND', line=62)
W('5660', 0o04007, '', 'ROR', 'SUPERBNK', 'ADD SUPER BITS.', line=63)
W('5661', 0o55364, '', 'TS', 'ALMCADR +1', line=64)

W('5662', 0o30002, 'LARMENT', 'CA', 'Q', 'STORE RETURN FOR ALARM', line=66)
W('5663', 0o54061, '', 'TS', 'ITEMP1', line=67)

W('5664', 0o30164, '', 'CA', 'LOC', line=69)
W('5665', 0o54057, '', 'TS', 'LOCALARM', line=70)
W('5666', 0o30165, '', 'CA', 'BANKSET', line=71)
W('5667', 0o54060, '', 'TS', 'BANKALRM', line=72)

W('5670', 0o10375, 'CHKFAIL1', 'CCS', 'FAILREG', 'IS ANYTHING IN FAILREG', line=74)
W('5671', 0o15674, '', 'TCF', 'CHKFAIL2', 'YES TRY NEXT REG', line=75)
W('5672', 0o22375, '', 'LXCH', 'FAILREG', line=76)
W('5673', 0o15706, '', 'TCF', 'PROGLARM', 'TURN ALARM LIGHT ON FOR FIRST ALARM', line=77)

W('5674', 0o10376, 'CHKFAIL2', 'CCS', 'FAILREG +1', line=79)
W('5675', 0o15700, '', 'TCF', 'FAIL3', line=80)
W('5676', 0o22376, '', 'LXCH', 'FAILREG +1', line=81)
W('5677', 0o15711, '', 'TCF', 'MULTEXIT', line=82)

W('5700', 0o30377, 'FAIL3', 'CA', 'FAILREG +2', line=84)
# Page 1494
W('5701', 0o74777, '', 'MASK', 'POSMAX', line=86)
W('5702', 0o10000, '', 'CCS', 'A', line=87)
W('5703', 0o15715, '', 'TCF', 'MULTFAIL', line=88)
W('5704', 0o22377, '', 'LXCH', 'FAILREG +2', line=89)
W('5705', 0o15711, '', 'TCF', 'MULTEXIT', line=90)

W('5706', 0o41036, 'PROGLARM', 'CS', 'DSPTAB +11D', line=92)
W('5707', 0o77765, '', 'MASK', 'OCT40400', line=93)
W('5710', 0o27036, '', 'ADS', 'DSPTAB +11D', line=94)

W('5711', 0o56061, 'MULTEXIT', 'XCH', 'ITEMP1', 'OBTAIN RETURN ADDRESS IN A', line=96)
W('5712', 0o00003, '', 'RELINT', line=97)
W('5713', 0o50000, '', 'INDEX', 'A', line=98)
W('5714', 0o00001, '', 'TC', '1', line=99)

W('5715', 0o30001, 'MULTFAIL', 'CA', 'L', line=101)
W('5716', 0o65001, '', 'AD', 'BIT15', line=102)
W('5717', 0o54377, '', 'TS', 'FAILREG +2', line=103)

W('5720', 0o15711, '', 'TCF', 'MULTEXIT', line=105)

# PRIOLARM DISPLAYS V05N09 VIA PRIODSPR WITH 3 RETURNS TO THE USER FROM THE ASTRONAUT AT CALL LOC +1,+2,+3 AND
# AN IMMEDIATE RETURN TO THE USER AT CALL LOC +4. EXAMPLE FOLLOWS,
# CAF     OCTXX           # ALARM CODE
# TC      BANKCALL
# CADR    PRIOLARM
#
# ...     ...
# ...     ...
# ...     ...             # ASTRONAUT RETURN
# TC      PHASCHNG        # IMMEDIATE RETURN TO USER. RESTART
# OCT     X.1             # PHASE CHANGE FOR PRIO DISPLAY

#   BANK 10
#   SETLOC DISPLAYS
#   BANK

#   COUNT 10/DSPLA

W('10,3766', 0o00004, 'PRIOLARM', 'INHINT', '', '* * * KEEP IN DISPLAY ROUTINES BANK', line=125)
W('10,3767', 0o54001, '', 'TS', 'L', 'SAVE ALARM CODE', line=126)

W('10,3770', 0o30133, '', 'CA', 'BUF2', '2 CADR OF PRIOLARM USER', line=128)
W('10,3771', 0o55363, '', 'TS', 'ALMCADR', line=129)
W('10,3772', 0o30134, '', 'CA', 'BUF2 +1', line=130)
W('10,3773', 0o05657, '', 'TC', 'PRIOENT +1', '* LEAVE L ALONE', line=131)
W('10,3774', 0o77467, '-2SEC', 'DEC', '-200', '*** DONT MOVE', kind='data', line=132)
W('10,3775', 0o35050, '', 'CAF', 'V05N09', line=133)
W('10,3776', 0o12726, '', 'TCF', 'PRIODSPR', line=134)

# Page 1495
#   BLOCK 02
#   SETLOC FFTAG13
#   BANK

#   COUNT 02/ALARM

W('7755', 0o00004, 'BAILOUT', 'INHINT', line=143)
W('7756', 0o30002, '', 'CA', 'Q', line=144)
W('7757', 0o55363, '', 'TS', 'ALMCADR', line=145)

W('7760', 0o04662, '', 'TC', 'BANKCALL', line=147)
W('7761', 0o40000, '', 'CADR', 'VAC5STOR', kind='data', line=148)

W('7762', 0o51363, '', 'INDEX', 'ALMCADR', line=150)
W('7763', 0o30000, '', 'CAF', '0', line=151)
W('7764', 0o05655, '', 'TC', 'BORTENT', line=152)
W('7765', 0o40400, 'OCT40400', 'OCT', '40400', kind='data', line=153)

W('7766', 0o00004, '', 'INHINT', line=155)
W('7767', 0o35016, 'WHIMPER', 'CA', 'TWO', line=156)
W('7770', 0o60005, '', 'AD', 'Z', line=157)
W('7771', 0o54017, '', 'TS', 'BRUPT', line=158)
W('7772', 0o50017, '', 'RESUME', line=159)
W('7773', 0o04701, '', 'TC', 'POSTJUMP', 'RESUME SENDS CONTROL HERE', line=160)
W('7774', 0o12651, '', 'CADR', 'ENEMA', kind='data', line=161)

#   SETLOC FFTAG7
#   BANK

W('5721', 0o00004, 'POODOO', 'INHINT', line=166)
W('5722', 0o30002, '', 'CA', 'Q', line=167)
W('5723', 0o55363, '', 'TS', 'ALMCADR', line=168)

W('5724', 0o04662, '', 'TC', 'BANKCALL', line=170)
W('5725', 0o40000, '', 'CADR', 'VAC5STOR', 'STORE ERASABLES FOR DEBUGGING PURPOSES.', kind='data', line=171)

W('5726', 0o51363, '', 'INDEX', 'ALMCADR', line=173)
W('5727', 0o30000, '', 'CAF', '0', line=174)
W('5730', 0o05655, 'ABORT2', 'TC', 'BORTENT', line=175)

W('5731', 0o77770, 'OCT77770', 'OCT', '77770', 'DONT MOVE', kind='data', line=177)
W('5732', 0o35012, '', 'CA', 'V37FLBIT', 'IS AVERAGE G ON', line=178)
W('5733', 0o70103, '', 'MASK', 'FLAGWRD7', line=179)
W('5734', 0o10000, '', 'CCS', 'A', line=180)
W('5735', 0o07766, '', 'TC', 'WHIMPER -1', 'YES.  DONT DO POODOO.  DO BAILOUT.', line=181)

W('5736', 0o05560, '', 'TC', 'DOWNFLAG', line=183)
W('5737', 0o00067, '', 'ADRES', 'STATEFLG', kind='data', line=184)

W('5740', 0o05560, '', 'TC', 'DOWNFLAG', line=186)
# Page 1496
W('5741', 0o00236, '', 'ADRES', 'REINTFLG', kind='data', line=188)

W('5742', 0o05560, '', 'TC', 'DOWNFLAG', line=190)
W('5743', 0o00054, '', 'ADRES', 'NODOFLAG', kind='data', line=191)

W('5744', 0o04662, '', 'TC', 'BANKCALL', line=193)
W('5745', 0o12501, '', 'CADR', 'MR.KLEAN', kind='data', line=194)
W('5746', 0o07767, '', 'TC', 'WHIMPER', line=195)

W('5747', 0o00004, 'CCSHOLE', 'INHINT', line=197)
W('5750', 0o30002, '', 'CA', 'Q', line=198)
W('5751', 0o55363, '', 'TS', 'ALMCADR', line=199)
W('5752', 0o04662, '', 'TC', 'BANKCALL', line=200)
W('5753', 0o40000, '', 'CADR', 'VAC5STOR', kind='data', line=201)
W('5754', 0o35756, '', 'CA', 'OCT1103', line=202)
W('5755', 0o05730, '', 'TC', 'ABORT2', line=203)
W('5756', 0o01103, 'OCT1103', 'OCT', '1103', kind='data', line=204)
W('5757', 0o00004, 'CURTAINS', 'INHINT', line=205)
W('5760', 0o30002, '', 'CA', 'Q', line=206)
W('5761', 0o05652, '', 'TC', 'ALARM2', line=207)
W('5762', 0o00217, 'OCT217', 'OCT', '00217', kind='data', line=208)
W('5763', 0o01363, '', 'TC', 'ALMCADR', 'RETURN TO USER', line=209)

S('DOALARM', 'equals', 0o5217, line=211)
# CALLING SEQUENCE FOR VARALARM
#
# CAF     (ALARM)
# TC      VARALARM
#
# VARALARM TURNS ON PROGRAM ALARM LIGHT BUT DOES NOT DISPLAY
W('5764', 0o00004, 'VARALARM', 'INHINT', line=218)

W('5765', 0o54001, '', 'TS', 'L', 'SAVE USERS ALARM CODE', line=220)

W('5766', 0o30002, '', 'CA', 'Q', 'SAVE USERS Q', line=222)
W('5767', 0o55363, '', 'TS', 'ALMCADR', line=223)

W('5770', 0o05656, '', 'TC', 'PRIOENT', line=225)
W('5771', 0o00014, 'OCT14', 'OCT', '14', 'DONT MOVE', kind='data', line=226)

W('5772', 0o01363, '', 'TC', 'ALMCADR', 'RETURN TO USER', line=228)

S('ABORT', 'equals', 0o7755, line=230)  # *** TEMPORARY UNTIL ABORT CALLS OUT
