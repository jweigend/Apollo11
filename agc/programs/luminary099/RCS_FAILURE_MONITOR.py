"""RCS_FAILURE_MONITOR.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/RCS_FAILURE_MONITOR.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 190-192 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('RCS_FAILURE_MONITOR', 'RCS_FAILURE_MONITOR.agc', 'Luminary099', pages='190-192')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     RCS_FAILURE_MONITOR.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        190-192
# Mod history:  2009-05-19 HG   Transcribed from page images.
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

# Page 190
# PROGRAM DESCRIPTION
#
# AUTHOR:  J S MILLER
#
# MODIFIED 6 MARCH 1968 BY P S WEISSMAN TO SET UP JOB FOR 1/ACCS WHEN THE MASKS ARE CHANGED.
#
# THIS ROUTINE IS ATTACHED TO T4RUPT, AND IS ENTERED EVERY 480 MS.  ITS FUNCTION IS TO EXAMINE THE LOW 8 BITS
# OF CHANNEL 32 TO SEE IF ANY ISOLATION-VALVE CLOSURE BITS HAVE APPEARED OR DISAPPEARED (THE CREW IS WARNED OF JET
# FAILURES BY LAMPS LIT BY THE GRUMMAN FAILURE-DETECTION CIRCUITRY; THEY MAY RESPOND BY OPERATING SWITCHES WHICH
# ISOLATE PAIRS OF JETS FROM THE PROPELLANT TANKS AND SET BITS IN CHANNEL 32).  IN THE EVENT THAT CHANNEL 32 BITS
# DIFFER FROM 'PVALVEST', THE RECORD OF ACTIONS TAKEN BY THIS ROUTINE, THE APPROPRIATE BITS IN 'CH5MASK' &
# 'CH6MASK', USED BY THE DAP JET-SELECTION LOGIC, ARE UPDATED, AS IS 'PVALVEST'.  TO SPEED UP & SHORTEN THE
# ROUTINE, NO MORE THAN ONE CHANGE IS ACCEPTED PER ENTRY.  THE HIGHEST-NUMBERED BIT IN CHANNEL 32 WHICH REQUIRES
# ACTION IS THE ONE PROCESSED.
#
# THE CODING IN THE FAILURE MONITOR HAS BEEN WRITTEN SO AS TO HAVE ALMOST COMPLETE RESTART PROTECTION.  FOR
# EXAMPLE, NO ASSUMPTION IS MADE WHEN SETTING A 'CH5MASK' BIT TO 1 THAT THE PREVIOUS STATE IS 0, ALTHOUGH IT OF
# COURSE SHOULD BE.  ONE CASE WHICH MAY BE SEEN TO EVADE PROTECTION IS THE OCCURRENCE OF A RESTART AFTER UPDATING
# ONE OR BOTH DAP MASK-WORDS BUT BEFORE UPDATING 'PVALVEST', COUPLED WITH A CHANGE IN THE VALVE-BIT BACK TO ITS
# FORMER STATE.  THE CONSEQUENCE OF THIS IS THAT THE NEXT ENTRY WOULD NOT SEE THE CHANGE INCOMPLETELY INCORP-
# ORATED BY THE LAST PASS (BECAUSE IT WENT AWAY AT JUST THE RIGHT TIME), BUT THE DAP MASK-WORDS WILL BE INCORRECT.
# THIS COMBINATION OF EVENTS SEEMS QUITE REMOTE, BUT NOT IMPOSSIBLE UNLESS THE CREW OPERATES THE SWITCHES AT HALF-
# SECOND INTERVALS OR LONGER.  IN ANY EVENT, A DISAGREEMENT BETWEEN REALITY AND THE DAP MASKS WILL BE CURED IF
# THE MISINTERPRETED SWITCH IS REVERSED AND THEN RESTORED TO ITS CORRECT POSITION (SLOWLY).
#
# CALLING SEQUENCE:
#
# TCF     RCSMONIT        (IN INTERRUPT MODE, EVERY 480 MS.)
#
# EXIT:  TCF  RCSMONEX  (ALL PATHS EXIT VIA SUCH AN INSTRUCTION)
S('RCSMONEX', 'equals', 0o5270, line=58)

# ERASABLE INITIALIZATION REQUIRED:
#
# VIA FRESH START:  PVALVEST          = +0  (ALL JETS ENABLED)
# CH5MASK, CH6MASK  = +0  (ALL JETS OK)
#
# OUTPUT:  CH5MASK & CH6MASK UPDATED  (1'S WHERE JETS NOT TO BE USED, IN CHANNEL 5 & 6 FORMAT)
# PVALTEST UPDATED  (1.5 WHEN VALVE CLOSURES HAVE BEEN TRANSLATED INTO CH5MASK & CH6MASK; CHAN 32 FORMAT)
# JOB TO DO 1/ACCS.
#
# DEBRIS:  A, L, Q AND DEBRIS OF NOVAC.
#
# SUBROUTINE CALLED:  NOVAC.

#   EBANK= CH5MASK

#   BANK 23
#   SETLOC RCSMONT
#   BANK
# Page 191
#   COUNT* $$/T4RCS

S('RCSMONIT', 'equals', 0o25156, line=81)

W('06,3156', 0o44755, 'RCSMON', 'CS', 'ZERO', line=83)
W('06,3157', 0o00006, '', 'EXTEND', line=84)
W('06,3160', 0o06032, '', 'RXOR', 'CHAN32', 'PICK UP + INVERT INVERTED CHANNEL 32.', line=85)
W('06,3161', 0o74357, '', 'MASK', 'LOW8', 'KEEP JET-FAIL BITS ONLY.', line=86)
W('06,3162', 0o54002, '', 'TS', 'Q', line=87)

W('06,3163', 0o41276, '', 'CS', 'PVALVEST', '      -   -', line=89)
W('06,3164', 0o70002, '', 'MASK', 'Q', 'FORM PC + PC.', line=90)
W('06,3165', 0o54001, '', 'TS', 'L', '  (P = PREVIOUS ISOLATION VALVE STATE,', line=91)
W('06,3166', 0o40002, '', 'CS', 'Q', '   C = CURRENT VALVE STATE (CH 32)).', line=92)
W('06,3167', 0o71276, '', 'MASK', 'PVALVEST', line=93)
W('06,3170', 0o26001, '', 'ADS', 'L', 'RESULT NZ INDICATES ACTION REQUIRED.', line=94)

W('06,3171', 0o00006, '', 'EXTEND', line=96)
W('06,3172', 0o15270, '', 'BZF', 'RCSMONEX', 'QUIT IF NO ACTION REQUIRED.', line=97)

W('06,3173', 0o00006, '', 'EXTEND', line=99)
W('06,3174', 0o74745, '', 'MP', 'BIT7', 'MOVE BITS 8 - 1 OF A TO 14 - 7 OF L.', line=100)
W('06,3175', 0o56001, '', 'XCH', 'L', 'ZERO TO L IN THE PROCESS.', line=101)

W('06,3176', 0o24001, '', 'INCR', 'L', line=103)
W('06,3177', 0o60000, '', 'DOUBLE', '', 'BOUND TO GET OVERFLOW IN THIS LOOP.', line=104)
W('06,3200', 0o54000, '', 'OVSK', '', 'SINCE WE ASSURED INITIAL NZ IN A.', line=105)
W('06,3201', 0o13176, '', 'TCF', '-3', line=106)

W('06,3202', 0o50001, '', 'INDEX', 'L', line=108)
W('06,3203', 0o34743, '', 'CA', 'BIT8 -1', 'SAVE THE RELEVANT BIT (8 - 1).', line=109)
W('06,3204', 0o54002, '', 'TS', 'Q', line=110)
W('06,3205', 0o71276, '', 'MASK', 'PVALVEST', 'LOOK AT PREVIOUS VALVE STATE BIT.', line=111)
W('06,3206', 0o10000, '', 'CCS', 'A', line=112)
W('06,3207', 0o13223, '', 'TCF', 'VOPENED', 'THE VALVE HAS JUST BEEN OPENED.', line=113)

W('06,3210', 0o41262, '', 'CS', 'CH5MASK', 'THE VALVE HAS JUST BEEN CLOSED.', line=115)
W('06,3211', 0o50001, '', 'INDEX', 'L', line=116)
W('06,3212', 0o73242, '', 'MASK', '5FAILTAB', line=117)
W('06,3213', 0o27262, '', 'ADS', 'CH5MASK', 'SET INHIBIT BIT FOR CHANNEL 5 JET.', line=118)

W('06,3214', 0o41263, '', 'CS', 'CH6MASK', line=120)
W('06,3215', 0o50001, '', 'INDEX', 'L', line=121)
W('06,3216', 0o73252, '', 'MASK', '6FAILTAB', line=122)
W('06,3217', 0o27263, '', 'ADS', 'CH6MASK', 'SET INGIBIT BIT FOR CHANNEL 6 JET.', line=123)

W('06,3220', 0o30002, '', 'CA', 'Q', line=125)
W('06,3221', 0o27276, '', 'ADS', 'PVALVEST', 'RECORD ACTION TAKEN.', line=126)

W('06,3222', 0o13236, '', 'TCF', '1/ACCFIX', 'SET UP 1/ACCJOB AND EXIT.', line=128)

# Page 192
W('06,3223', 0o50001, 'VOPENED', 'INDEX', 'L', 'A VALVE HAS JUST BEEN OPENED.', line=131)
W('06,3224', 0o43242, '', 'CS', '5FAILTAB', line=132)
W('06,3225', 0o71262, '', 'MASK', 'CH5MASK', line=133)
W('06,3226', 0o55262, '', 'TS', 'CH5MASK', 'REMOVE INHIBIT BIT FOR CHANNEL 5 JET.', line=134)

W('06,3227', 0o50001, '', 'INDEX', 'L', line=136)
W('06,3230', 0o43252, '', 'CS', '6FAILTAB', line=137)
W('06,3231', 0o71263, '', 'MASK', 'CH6MASK', line=138)
W('06,3232', 0o55263, '', 'TS', 'CH6MASK', 'REMOVE INHIBIT BIT FOR CHANNEL 6 JET.', line=139)

W('06,3233', 0o40002, '', 'CS', 'Q', line=141)
W('06,3234', 0o71276, '', 'MASK', 'PVALVEST', line=142)
W('06,3235', 0o55276, '', 'TS', 'PVALVEST', 'RECORD ACTION TAKEN.', line=143)

W('06,3236', 0o37715, '1/ACCFIX', 'CAF', 'PRIO27', 'SET UP 1/ACCS SO THAT THE SWITCH CURVES', line=145)
W('06,3237', 0o05072, '', 'TC', 'NOVAC', '  FOR TJETLAW CAN BE MODIFIED IF CH5MASK', line=146)
#   EBANK= AOSQ  #   HAS BEEN ALTERED.
W('06,3240', 0o02454, '', '2CADR', '1/ACCJOB', kind='data', line=148)
W('06,3241', 0o40106, kind='data', line=148)

W('06,3242', 0o15270, '', 'TCF', 'RCSMONEX', 'EXIT.', line=150)

S('5FAILTAB', 'equals', 0o25242, line=153)  # CH 5 JET BIT CORRESPONDING TO CH 32 BIT:
W('06,3243', 0o00040, '', 'OCT', '00040', '8', kind='data', line=154)
W('06,3244', 0o00020, '', 'OCT', '00020', '7', kind='data', line=155)
W('06,3245', 0o00100, '', 'OCT', '00100', '6', kind='data', line=156)
W('06,3246', 0o00200, '', 'OCT', '00200', '5', kind='data', line=157)
W('06,3247', 0o00010, '', 'OCT', '00010', '4', kind='data', line=158)
W('06,3250', 0o00001, '', 'OCT', '00001', '3', kind='data', line=159)
W('06,3251', 0o00004, '', 'OCT', '00004', '2', kind='data', line=160)
W('06,3252', 0o00002, '', 'OCT', '00002', '1', kind='data', line=161)

S('6FAILTAB', 'equals', 0o25252, line=163)  # CH 6 JET BIT CORRESPONDING TO CH 32 BIT:
W('06,3253', 0o00010, '', 'OCT', '00010', '8', kind='data', line=164)
W('06,3254', 0o00020, '', 'OCT', '00020', '7', kind='data', line=165)
W('06,3255', 0o00004, '', 'OCT', '00004', '6', kind='data', line=166)
W('06,3256', 0o00200, '', 'OCT', '00200', '5', kind='data', line=167)
W('06,3257', 0o00001, '', 'OCT', '00001', '4', kind='data', line=168)
W('06,3260', 0o00002, '', 'OCT', '00002', '3', kind='data', line=169)
W('06,3261', 0o00040, '', 'OCT', '00040', '2', kind='data', line=170)
W('06,3262', 0o00100, '', 'OCT', '00100', '1', kind='data', line=171)
