"""TVCSTROKETEST.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/TVCSTROKETEST.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 979-983 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TVCSTROKETEST', 'TVCSTROKETEST.agc', 'Comanche055', pages='979-983')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TVCSTROKETEST.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        979-983
# Mod history:  2009-05-13 RSB  Adapted from the Colossus249/ file of the
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

# Page 979
# NAME          STROKE TEST PACKAGE             (INCLUDING INITIALIZATION PACKAGE)
# LOG SECTION...TVCSTROKETEST                   SUBROUTINE...DAPCSM
# MODIFIED BY SCHLUNDT                          21 OCTOBER 1968
#
# FUNCTIONAL DESCRIPTION....
# STROKE TEST PACKAGE GENERATES A WAVEFORM DESIGNED TO EXCITE BENDING
# STRKTSTI (STROKE TEST INITIALIZATION) IS CALLED AS A JOB BY VB68.
# IT INITIALIZES ALL ERASABLES REQD FOR A STROKE TEST, AND
# THEN TESTS FOR CSM/LM (BIT 13 OF DAPDATR1). IF CSM/LM,
# IN EITHER HIGH OR LOW-BANDWIDTH MODE, THE TEST IS STARTED
# IMMEDIATELY.  IF NOT CSM/LM, PROGRAM EXITS WITH NO ACTION.
# HACK (STROKE TEST) GENERATES THE WAVEFORM BY DUMPING PULSE BURSTS
# OF PROPER SIGN AND IN PROPER SEQUENCE DIRECTLY INTO
# TVCPITCH, WORKING IN CONJUNCTION WITH BOTH PITCH AND YAW
# TVC DAPS, WITH INTERMEDIATE WAITLIST CALLS.  NOTE, HOWEVER
# THAT THE STROKE TEST IS PERFORMED ONLY IN THE PITCH AXIS.
# AN EXAMPLE WAVEFORM IS GIVEN BELOW, TO DEMONSTRATE STROKE-
# TEST PARAMETER SELECTION.
# RESTARTS CAUSE TEST TO BE TERMINATED.  ANOTHER V68 REQD IF TEST
# IS TO BE RE-RUN.
# PULSE BURST SIZE IS PAD-LOADED (ESTROKER) SO THAT AMPLITUDE OF
# WAVEFORM CAN BE CHANGED.  THERE ARE TEN PULSE BURSTS IN
# THE HALF-AMPLITUDE OF THE FIRST FREQUENCY SET IN THE
# STANDARD WAVEFORM.  AMPLITUDE IS 10(ESTROKER)(1/42.15),
# NOMINALLY 50/42.15 = 1.185 DEG
#
# CALLING SEQUENCE....
# EXTENDED VERB 68 SETS UP STRKTSTI JOB
# PITCH AND YAW TVCDAPS, FINDING STROKER NON-ZERO, DO A ..TC HACK..
# AN INTERNALLY-GENERATED WAITLIST CALL ENTERS AT ..HACKWLST..
#
# NORMAL EXIT MODES....
# TC BUNKER (..Q.. IF ENTRY FROM DAP, ..TCTSKOVR.. IF FROM WAITLIST) LIST
#
# SUBROUTINES CALLED....
# WAITLIST
#
# ALARM OR ABORT EXIT MODES....
# NONE
#
# ERASABLE INITIALIZATION REQUIRED....
# ESTROKER (PAD-LOAD)
# STROKER, CADDY, REVS, CARD, N
#
# OUTPUT....
# STRKTSTI...INITIALIZATION FOR STROKE TEST
# HACK, HACKWLST...PULSE BURSTS INTO TVCPITCH VIA..ADS..
# RESETS STROKER = +0 WHEN TEST COMPLETED
#
# DEBRIS....
# N = CADDY = +0, CARD = -0, REVS = -1
# BUNKER
# Page 980
#
# EXAMPLE STROKE TEST WAVE FORM, DEMONSTRATING PARAMETER SELECTION

# NOTE....THIS IS NOT THE OFFICIAL WAVEFORM....
#
# **              **
# **              **
# **              **             EXAMPLE WAVEFORM (EACH * REPRESENTS
# *  *            *  *              (85.41 ARCSEC OF ACTUATOR CMND)
# *  *            *  *
# *  *            *  *
# *    *          *    *          **      **      **      **      **
# *    *          *    *          **      **      **      **      **
# *    *          *    *          **      **      **      **      **
# *      *        *      *        *  *    *  *    *  *    *  *    *  *    **  **  **  **  **
# *      *        *      *        *  *    *  *    *  *    *  *    *  *    **  **  **  **  **
# *      *        *      *        *  *    *  *    *  *    *  *    *  *    **  **  **  **  **
# ----------------------------------------------------------------------------------------------------
# *      *        *      *    *  *    *  *    *  *    *  *    *  *  **  **  **  **  **
# *      *        *      *    *  *    *  *    *  *    *  *    *  *  **  **  **  **  **
# *      *        *      *    *  *    *  *    *  *    *  *    *  *  **  **  **  **  **
# *    *          *    *      **      **      **      **      **
# *    *          *    *      **      **      **      **      **
# *    *          *    *      **      **      **      **      **
# *  *            *  *
# *  *            *  *
# *  *            *  *
# **              **
# **              **
# **              **
#
# FOR THIS (UNOFFICIAL, EXAMPLE) WAVEFORM, THE REQUIRED PARAMETERS ARE AS FOLLOWS....
#
# FCARD    = +3           (NUMBER OF SETS)
# ESTROKER = +3           (PULSE BURST SIZE, SC.AT 85.41 ARCSEC/BIT)
#
# SET1:
# FREVS   = +3    (NUMBER REVERSALS MINUS 1)
# FCADDY  = +4    (NUMBER OF PULSE BURSTS IN 1/2 AMPLITUDE)
# SET2:
# FCARD1  = +9    (NUMBER REVERSALS MINUS 1)
# FCARD4  = +2    (NUMBER OF PULSE BURSTS IN 1/2 AMPLITUDE)
# SET3:
# FCARD2  = +9    (NUMBER REVERSALS MINUS 1)
# FCARD5  = +1    (NUMBER OF PULSE BURSTS IN 1/2 AMPLITUDE)
# SET4:
# FCARD3  = +0    (NUMBER OF REVERSALS MINUS 1)
# FCARD6  = +0    (NUMBER OF PULSE BURSTS IN 1/2 AMPLUTUDE)

# Page 981
# STROKE TEST INITIALIZATION PACKAGE (AS A JOB, FROM VERB 68)

#   BANK 17
#   SETLOC DAPS2
#   BANK

#   COUNT* $$/STRK
#   EBANK= CADDY

W('20,3501', 0o03512, 'STRKTSTI', 'TCR', 'TSTINIT', 'STROKE TEST INITIALIZATION PKG (CALLED', line=143)
# AS A JOB BY VERB68)

W('20,3502', 0o00004, 'STRKCHK', 'INHINT', line=146)

W('20,3503', 0o31466, '', 'CAE', 'DAPDATR1', 'CHECK FOR CSM/LM CONFIGURATION', line=148)
W('20,3504', 0o75002, '', 'MASK', 'BIT14', line=149)
W('20,3505', 0o00006, '', 'EXTEND', line=150)
W('20,3506', 0o13511, '', 'BZF', '+3', line=151)

W('20,3507', 0o31413, '', 'CAE', 'ESTROKER', 'BEGIN ON NEXT DAP PASS (PITCH OR YAW)', line=153)
W('20,3510', 0o55574, '', 'TS', 'STROKER', '(STROKING DONE IN PITCH ONLY, HOWEVER)', line=154)

W('20,3511', 0o15217, '', 'TCF', 'ENDOFJOB', line=156)

W('20,3512', 0o43522, 'TSTINIT', 'CS', 'FCADDY', 'NORMAL ENTRY FROM STRKTSTI', line=158)
W('20,3513', 0o55655, '', 'TS', 'CADDY', line=159)
W('20,3514', 0o55656, '', 'TS', 'N', '      NOTE SGN CHNG FCADDY(+) TO CADDY(-)', line=160)

W('20,3515', 0o33523, '', 'CAF', 'FREVS', line=162)
W('20,3516', 0o55660, '', 'TS', 'REVS', line=163)

W('20,3517', 0o43524, '', 'CS', 'FCARD', '      NOTE SGN CHNG FCARD(+) TO CARD(-)', line=165)
W('20,3520', 0o55661, '', 'TS', 'CARD', line=166)

W('20,3521', 0o00002, '', 'TC', 'Q', 'RETURN TO STRKTSTI+1 (OR CHKSTRK+2OR+4)', line=168)

# Page 982
# THE OFFICIAL STROKE TEST WAVEFORM (3 JAN, 1967) CONSISTS OF FOUR STROKE SETS, AS FOLLOWS....
#
# SET 1...10 BURSTS IN 1/2 AMP,   4 REVERSALS
# SET 2... 6 BURSTS IN 1/2 AMP,   6 REVERSALS
# SET 3... 5 BURSTS IN 1/2 AMP,  10 REVERSALS
# SET 4... 4 BURSTS IN 1/2 AMP,  14 REVERSALS
#
# THE PULSE BURST SIZE (ESTROKER) IS PAD-LOADED (5 BITS AS OF 3JAN,1967)
# THE REMAINING WAVEFORM-GENERATING PARAMETERS ARE AS FOLLOWS....

W('20,3522', 0o00012, 'FCADDY', 'DEC', '10', 'NO. PULSE BURSTS IN 1/2 AMP, SET1..(+10)', kind='data', line=181)
W('20,3523', 0o00003, 'FREVS', 'DEC', '3', 'NO. REVERSALS MINUS 1, SET1........(  3)', kind='data', line=182)

W('20,3524', 0o00004, 'FCARD', 'DEC', '4', 'NO. STROKE SETS....................(+ 4)', kind='data', line=184)

W('20,3525', 0o00005, 'FCARD1', 'DEC', '5', 'NO. REVERSALS MINUS 1, SET2........(  5)', kind='data', line=186)

W('20,3526', 0o00011, 'FCARD2', 'DEC', '9', '                          3........(  9)', kind='data', line=188)
W('20,3527', 0o00015, 'FCARD3', 'DEC', '13', '                          4........( 13)', kind='data', line=189)

W('20,3530', 0o00006, 'FCARD4', 'DEC', '6', 'NO. PULSE BURSTS IN 1/2 AMP, SET2..(+ 6)', kind='data', line=191)
W('20,3531', 0o00005, 'FCARD5', 'DEC', '5', '                             SET3..(+ 5)', kind='data', line=192)
W('20,3532', 0o00004, 'FCARD6', 'DEC', '4', '                             SET4..(+ 4)', kind='data', line=193)

S('20MS', 'equals', 0o5016, line=195)

# STROKE TEST PACKAGE PROPER....

#   EBANK= BUNKER

W('20,3533', 0o00006, 'HACK', 'EXTEND', '', 'ENTRY (IN T5 RUPT) FROM TVCDAPS', line=201)
W('20,3534', 0o23657, '', 'QXCH', 'BUNKER', 'SAVE Q FOR DAP RETURN', line=202)

W('20,3535', 0o35016, '', 'CAF', '20MS', '2DAPSX2(PASSES/DAP)X2(CS/PASS)=8CS=TVCDT', line=204)
W('20,3536', 0o05245, '', 'TC', 'WAITLIST', line=205)
#   EBANK= BUNKER
W('20,3537', 0o03542, '', '2CADR', 'HACKWLST', kind='data', line=207)
W('20,3540', 0o40066, kind='data', line=207)

W('20,3541', 0o13544, '', 'TCF', '+3', line=209)

W('20,3542', 0o34367, 'HACKWLST', 'CAF', 'TCTSKOVR', 'ENTRY FROM WAITLIST', line=211)
W('20,3543', 0o55657, '', 'TS', 'BUNKER', 'BUNKER IS TC TASKOVER', line=212)

W('20,3544', 0o31574, '', 'CA', 'STROKER', 'STROKE', line=214)
W('20,3545', 0o26054, '', 'ADS', 'TVCPITCH', line=215)

W('20,3546', 0o35005, '', 'CAF', 'BIT11', 'RELEASE THE ERROR COUNTERS', line=217)
W('20,3547', 0o00006, '', 'EXTEND', line=218)
W('20,3550', 0o05014, '', 'WOR', 'CHAN14', line=219)
W('20,3551', 0o25655, '', 'INCR', 'CADDY', 'COUNT DOWN THE NO. BURSTS, THIS SLOPE', line=220)
# Page 983
W('20,3552', 0o41655, '', 'CS', 'CADDY', line=222)
W('20,3553', 0o00006, '', 'EXTEND', line=223)
W('20,3554', 0o63556, '', 'BZMF', '+2', line=224)
W('20,3555', 0o01657, '', 'TC', 'BUNKER', 'EXIT, WHILE ON A SLOPE', line=225)

W('20,3556', 0o11660, '', 'CCS', 'REVS', line=227)
W('20,3557', 0o13577, '', 'TCF', 'REVUP', 'POSITIVE REVS', line=228)
W('20,3560', 0o13603, '', 'TCF', 'REVUP +4', 'FINAL REVERSAL, THIS SET', line=229)

W('20,3561', 0o25661, '', 'INCR', 'CARD', 'NEGATIVE REVS SET LAST PASS, READY FOR', line=231)
W('20,3562', 0o41661, '', 'CS', 'CARD', '      THE NEXT SET.  CHECK IF NO MORE SETS', line=232)
W('20,3563', 0o00006, '', 'EXTEND', line=233)
W('20,3564', 0o13575, '', 'BZF', 'STROKILL', 'ALL SETS COMPLETED', line=234)

W('20,3565', 0o51661, '', 'INDEX', 'CARD', line=236)
W('20,3566', 0o33530, '', 'CAF', 'FCARD +4', 'PICK UP NO. REVERSALS (-), NEXT SET', line=237)
W('20,3567', 0o55660, '', 'TS', 'REVS', 'REINITIALIZE', line=238)
W('20,3570', 0o51661, '', 'INDEX', 'CARD', line=239)
W('20,3571', 0o43533, '', 'CS', 'FCARD +7', 'PICK UP NO. BURSTS IN 1/2AMP, NEXT SET', line=240)
W('20,3572', 0o55656, '', 'TS', 'N', 'REINITIALIZE', line=241)
W('20,3573', 0o55655, '', 'TS', 'CADDY', line=242)
W('20,3574', 0o01657, '', 'TC', 'BUNKER', 'EXIT, AT END OF SET', line=243)

W('20,3575', 0o55574, 'STROKILL', 'TS', 'STROKER', 'RESET (TO +0) TO END TEST', line=245)
W('20,3576', 0o01657, '', 'TC', 'BUNKER', 'EXIT, STROKE TEST FINIS', line=246)

W('20,3577', 0o55660, 'REVUP', 'TS', 'REVS', 'ALL REVERSALS EXCEPT LAST OF SET', line=248)
W('20,3600', 0o31656, '', 'CA', 'N', line=249)
W('20,3601', 0o60000, '', 'DOUBLE', '', '2 x 1/2AMP', line=250)
W('20,3602', 0o13606, '', 'TCF', '+4', line=251)

W('20,3603', 0o45017, '', 'CS', 'ONE', 'FINAL REVERSAL, THIS SET', line=253)
W('20,3604', 0o55660, '', 'TS', 'REVS', 'PREPARE TO BRANCH TO NEW BURST', line=254)
W('20,3605', 0o31656, '', 'CA', 'N', 'JUST RETURN TO ZERO, FINAL SLOPE OF SET', line=255)
W('20,3606', 0o55655, '', 'TS', 'CADDY', 'CADUP', line=256)

W('20,3607', 0o41574, '', 'CS', 'STROKER', 'CHANGE SIGN OF SLOPE', line=258)
W('20,3610', 0o55574, '', 'TS', 'STROKER', line=259)
W('20,3611', 0o01657, '', 'TC', 'BUNKER', 'EXIT AT A REVERSAL (SLOPE CHANGE)', line=260)
