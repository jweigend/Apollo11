"""ALARM_AND_ABORT.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/ALARM_AND_ABORT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1381-1385 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('ALARM_AND_ABORT', 'ALARM_AND_ABORT.agc', 'Luminary099', pages='1381-1385')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     ALARM_AND_ABORT.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1381-1385
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Luminary131/ file of the same
# name, using Luminary099 page images.
# 2009-06-05 RSB  Fixed a type.
# 2011-01-06 JL   Fixed pseudo-label indentation.
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

# Page 1381
# THE FOLLOWING SUBROUTINE MAY BE CALLED TO DISPLAY A NON-ABORTIVE ALARM CONDITION.  IT MAY BE CALLED
# EITHER IN INTERRUPT OR UNDER EXECUTIVE CONTROL.
#
# CALLING SEQUENCE IS AS FOLLOWS:
# TC      ALARM
# OCT     AAANN           # ALARM NO. NN IN GENERAL AREA AAA.
# # (RETURNS HERE)

#   BLOCK 02
#   SETLOC FFTAG7
#   BANK

#   EBANK= FAILREG

#   COUNT* $$/ALARM

# ALARM TURNS ON THE PROGRAM ALARM LIGHT, BUT DOES NOT DISPLAY.

W('5567', 0o00004, 'ALARM', 'INHINT', line=50)

W('5570', 0o30002, '', 'CA', 'Q', line=52)
W('5571', 0o55363, 'ALARM2', 'TS', 'ALMCADR', line=53)
W('5572', 0o50002, '', 'INDEX', 'Q', line=54)
W('5573', 0o30000, '', 'CA', '0', line=55)
W('5574', 0o54001, 'BORTENT', 'TS', 'L', line=56)

W('5575', 0o30006, 'PRIOENT', 'CA', 'BBANK', line=58)
W('5576', 0o00006, '', 'EXTEND', line=59)
W('5577', 0o04007, '', 'ROR', 'SUPERBNK', 'ADD SUPER BITS.', line=60)
W('5600', 0o55364, '', 'TS', 'ALMCADR +1', line=61)

W('5601', 0o30002, 'LARMENT', 'CA', 'Q', 'STORE RETURN FOR ALARM', line=63)
W('5602', 0o54061, '', 'TS', 'ITEMP1', line=64)

W('5603', 0o10375, 'CHKFAIL1', 'CCS', 'FAILREG', 'IS ANYTHING IN FAILREG', line=66)
W('5604', 0o15607, '', 'TCF', 'CHKFAIL2', 'YES TRY NEXT REG', line=67)
W('5605', 0o22375, '', 'LXCH', 'FAILREG', line=68)
W('5606', 0o15621, '', 'TCF', 'PROGLARM', 'TURN ALARM LIGHT ON FOR FIRST ALARM', line=69)

W('5607', 0o10376, 'CHKFAIL2', 'CCS', 'FAILREG +1', line=71)
W('5610', 0o15613, '', 'TCF', 'FAIL3', line=72)
W('5611', 0o22376, '', 'LXCH', 'FAILREG +1', line=73)
W('5612', 0o15624, '', 'TCF', 'MULTEXIT', line=74)

W('5613', 0o30377, 'FAIL3', 'CA', 'FAILREG +2', line=76)
W('5614', 0o74733, '', 'MASK', 'POSMAX', line=77)
W('5615', 0o10000, '', 'CCS', 'A', line=78)
W('5616', 0o15630, '', 'TCF', 'MULTFAIL', line=79)
W('5617', 0o22377, '', 'LXCH', 'FAILREG +2', line=80)
W('5620', 0o15624, '', 'TCF', 'MULTEXIT', line=81)

# Page 1382

W('5621', 0o41036, 'PROGLARM', 'CS', 'DSPTAB +11D', line=85)
W('5622', 0o75642, '', 'MASK', 'OCT40400', line=86)
W('5623', 0o27036, '', 'ADS', 'DSPTAB +11D', line=87)

W('5624', 0o56061, 'MULTEXIT', 'XCH', 'ITEMP1', 'OBTAIN RETURN ADDRESS IN A', line=90)
W('5625', 0o00003, '', 'RELINT', line=91)
W('5626', 0o50000, '', 'INDEX', 'A', line=92)
W('5627', 0o00001, '', 'TC', '1', line=93)

W('5630', 0o30001, 'MULTFAIL', 'CA', 'L', line=95)
W('5631', 0o64735, '', 'AD', 'BIT15', line=96)
W('5632', 0o54377, '', 'TS', 'FAILREG +2', line=97)

W('5633', 0o15624, '', 'TCF', 'MULTEXIT', line=99)

# PRIOLARM DISPLAYS V05N09 VIA PRIODSPR WITH 3 RETURNS TO THE USER FROM THE ASTRONAUT AT CALL LOC +1,+2,+3 AND
# AN IMMEDIATE RETURN TO THE USER AT CALL LOC +4.  EXAMPLE FOLLOWS,
# CAF     OCTXX           # ALARM CODE
# TC      BANKCALL
# CADR    PRIOLARM
# ...     ...
# ...     ...
# ...     ...             # ASTRONAUT RETURN
# TC      PHASCHNG        # IMMEDIATE RETURN TO USER.  RESTART
# OCT     X.1             # PHASE CHANGE FOR PRIO DISPLAY

#   BANK 10
#   SETLOC DISPLAYS
#   BANK

#   COUNT* $$/DSPLA
W('10,3562', 0o00004, 'PRIOLARM', 'INHINT', '', '* * * KEEP IN DISPLAY ROUTINES BANK', line=117)
W('10,3563', 0o54001, '', 'TS', 'L', 'SAVE ALARM CODE', line=118)

W('10,3564', 0o30133, '', 'CA', 'BUF2', '2 CADR OF PRIOLARM USER', line=120)
W('10,3565', 0o55363, '', 'TS', 'ALMCADR', line=121)
W('10,3566', 0o30134, '', 'CA', 'BUF2 +1', line=122)
W('10,3567', 0o05576, '', 'TC', 'PRIOENT +1', '* LEAVE L ALONE', line=123)
W('10,3570', 0o77467, '-2SEC', 'DEC', '-200', '*** DONT MOVE', kind='data', line=124)
W('10,3571', 0o35006, '', 'CAF', 'V05N09', line=125)
W('10,3572', 0o12504, '', 'TCF', 'PRIODSPR', line=126)

#   BLOCK 02
#   SETLOC FFTAG7
#   BANK

#   COUNT* $$/ALARM
W('5634', 0o00004, 'BAILOUT', 'INHINT', line=133)
W('5635', 0o30002, '', 'CA', 'Q', line=134)
# Page 1383
W('5636', 0o55363, '', 'TS', 'ALMCADR', line=136)

W('5637', 0o50002, '', 'INDEX', 'Q', line=138)
W('5640', 0o30000, '', 'CAF', '0', line=139)
W('5641', 0o05574, '', 'TC', 'BORTENT', line=140)
W('5642', 0o40400, 'OCT40400', 'OCT', '40400', kind='data', line=141)

W('5643', 0o00004, '', 'INHINT', line=143)
W('5644', 0o34752, 'WHIMPER', 'CA', 'TWO', line=144)
W('5645', 0o60005, '', 'AD', 'Z', line=145)
W('5646', 0o54017, '', 'TS', 'BRUPT', line=146)
W('5647', 0o50017, '', 'RESUME', line=147)
W('5650', 0o04635, '', 'TC', 'POSTJUMP', 'RESUME SENDS CONTROL HERE', line=148)
W('5651', 0o12765, '', 'CADR', 'ENEMA', kind='data', line=149)
W('5652', 0o00004, 'POODOO', 'INHINT', line=150)
W('5653', 0o30002, '', 'CA', 'Q', line=151)
W('5654', 0o55363, 'ABORT2', 'TS', 'ALMCADR', line=152)
W('5655', 0o50002, '', 'INDEX', 'Q', line=153)
W('5656', 0o30000, '', 'CAF', '0', line=154)
W('5657', 0o05574, '', 'TC', 'BORTENT', line=155)
W('5660', 0o77770, 'OCT77770', 'OCT', '77770', "DON'T MOVE", kind='data', line=156)

W('5661', 0o34765, '', 'CAF', 'OCT35', '4.35SPOT FOR GOPOODOO', line=158)
W('5662', 0o54001, '', 'TS', 'L', line=159)
W('5663', 0o40000, '', 'COM', line=160)
W('5664', 0o52761, '', 'DXCH', '-PHASE4', line=161)
W('5665', 0o00004, 'GOPOODOO', 'INHINT', line=162)
W('5666', 0o04616, '', 'TC', 'BANKCALL', 'RESET STATEFLG, REINTFLG, AND NODOFLAG.', line=163)
W('5667', 0o27755, '', 'CADR', 'FLAGS', kind='data', line=164)
W('5670', 0o30103, '', 'CA', 'FLAGWRD7', 'IS SERVICER CURRENTLY IN OPERATION?', line=165)
W('5671', 0o74746, '', 'MASK', 'V37FLBIT', line=166)
W('5672', 0o10000, '', 'CCS', 'A', line=167)
W('5673', 0o15701, '', 'TCF', 'STRTIDLE', line=168)
W('5674', 0o04616, '', 'TC', 'BANKCALL', 'TERMINATE GRPS 1, 3, 5, AND 6', line=169)
W('5675', 0o12652, '', 'CADR', 'V37KLEAN', kind='data', line=170)
W('5676', 0o04616, '', 'TC', 'BANKCALL', 'TERMINATE GRPS 2, 4, 1, 3, 5, AND 6', line=171)
W('5677', 0o12643, '', 'CADR', 'MR.KLEAN', '      (I.E., GRP 4 LAST)', kind='data', line=172)
W('5700', 0o15644, '', 'TCF', 'WHIMPER', line=173)
W('5701', 0o35743, 'STRTIDLE', 'CAF', 'BBSERVDL', line=174)
W('5702', 0o04727, '', 'TC', 'SUPERSW', line=175)
W('5703', 0o04616, '', 'TC', 'BANKCALL', 'PUT SERVICER INTO ITS "GROUND" STATE', line=176)
W('5704', 0o57321, '', 'CADR', 'SERVIDLE', 'AND PROCED TO GOTOPOOH.', kind='data', line=177)
W('5705', 0o00004, 'CCSHOLE', 'INHINT', line=178)
W('5706', 0o30002, '', 'CA', 'Q', line=179)
W('5707', 0o05654, '', 'TC', 'ABORT2', line=180)
W('5710', 0o01103, 'OCT1103', 'OCT', '1103', kind='data', line=181)
W('5711', 0o00004, 'CURTAINS', 'INHINT', line=182)
W('5712', 0o30002, '', 'CA', 'Q', line=183)
W('5713', 0o05571, '', 'TC', 'ALARM2', line=184)
W('5714', 0o00217, 'OCT217', 'OCT', '00217', kind='data', line=185)
# Page 1384
W('5715', 0o01363, '', 'TC', 'ALMCADR', 'RETURN TO USER', line=187)

W('5716', 0o00004, 'BAILOUT1', 'INHINT', line=189)
W('5717', 0o53364, '', 'DXCH', 'ALMCADR', line=190)
W('5720', 0o35742, '', 'CAF', 'ADR40400', line=191)
W('5721', 0o54061, 'BOTHABRT', 'TS', 'ITEMP1', line=192)
W('5722', 0o50002, '', 'INDEX', 'Q', line=193)
W('5723', 0o30000, '', 'CAF', '0', line=194)
W('5724', 0o54001, '', 'TS', 'L', line=195)
W('5725', 0o15603, '', 'TCF', 'CHKFAIL1', line=196)
W('5726', 0o00004, 'POODOO1', 'INHINT', line=197)
W('5727', 0o53364, '', 'DXCH', 'ALMCADR', line=198)
W('5730', 0o35741, '', 'CAF', 'ADR77770', line=199)
W('5731', 0o15721, '', 'TCF', 'BOTHABRT', line=200)

W('5732', 0o00004, 'ALARM1', 'INHINT', line=202)
W('5733', 0o53364, '', 'DXCH', 'ALMCADR', line=203)
W('5734', 0o00004, 'ALMNCADR', 'INHINT', line=204)
W('5735', 0o50002, '', 'INDEX', 'Q', line=205)
W('5736', 0o30000, '', 'CA', '0', line=206)
W('5737', 0o54001, '', 'TS', 'L', line=207)
W('5740', 0o15601, '', 'TCF', 'LARMENT', line=208)

W('5741', 0o15660, 'ADR77770', 'TCF', 'OCT77770', line=210)
W('5742', 0o15642, 'ADR40400', 'TCF', 'OCT40400', line=211)
S('DOALARM', 'equals', 0o5155, line=212)
#   EBANK= DVCNTR
W('5743', 0o56067, 'BBSERVDL', 'BBCON', 'SERVIDLE', kind='data', line=214)

# CALLING SEQUENCE FOR VARALARM
# CAF     (ALARM)
# TC      VARALARM
#
# VARALARM TURNS ON PROGRAM ALARM LIGHT BUT DOES NOT DISPLAY

W('5744', 0o00004, 'VARALARM', 'INHINT', line=222)

W('5745', 0o54001, '', 'TS', 'L', 'SAVE USERS ALARM CODE', line=224)

W('5746', 0o30002, '', 'CA', 'Q', 'SAVE USERS Q', line=226)
W('5747', 0o55363, '', 'TS', 'ALMCADR', line=227)

W('5750', 0o05575, '', 'TC', 'PRIOENT', line=229)
W('5751', 0o00014, 'OCT14', 'OCT', '14', 'DONT MOVE', kind='data', line=230)

W('5752', 0o01363, '', 'TC', 'ALMCADR', 'RETURN TO USER', line=232)

S('ABORT', 'equals', 0o5644, line=234)
#   BANK 13
#   SETLOC ABTFLGS
#   BANK
# Page 1385
#   COUNT* $$/ALARM

W('13,3755', 0o44747, 'FLAGS', 'CS', 'STATEBIT', line=241)
W('13,3756', 0o70077, '', 'MASK', 'FLAGWRD3', line=242)
W('13,3757', 0o54077, '', 'TS', 'FLAGWRD3', line=243)
W('13,3760', 0o44745, '', 'CS', 'REINTBIT', line=244)
W('13,3761', 0o70106, '', 'MASK', 'FLGWRD10', line=245)
W('13,3762', 0o54106, '', 'TS', 'FLGWRD10', line=246)
W('13,3763', 0o44753, '', 'CS', 'NODOBIT', line=247)
W('13,3764', 0o70076, '', 'MASK', 'FLAGWRD2', line=248)
W('13,3765', 0o54076, '', 'TS', 'FLAGWRD2', line=249)
W('13,3766', 0o00002, '', 'TC', 'Q', line=250)
