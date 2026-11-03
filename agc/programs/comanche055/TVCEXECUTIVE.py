"""TVCEXECUTIVE.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/TVCEXECUTIVE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 945-950 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TVCEXECUTIVE', 'TVCEXECUTIVE.agc', 'Comanche055', pages='945-950')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TVCEXECUTIVE.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        945-950
# Mod history:  2009-05-12 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
# 2009-05-20 RSB  Corrections:  CAE -> CAF in one place.
# 2009-05-21 RSB  In 1SHOTCHK, a CAF SEVEN was corrected to
# CAF SIX.
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

# Page 945
# PROGRAM NAME....      TVCEXECUTIVE, CONSISTING OF TVCEXEC, NEEDLEUP, VARGAINS
# 1SHOTCHK, REPCHEK, CG.CORR, COPYCYCLES, ETC.
# LOG SECTION...TVCEXECUTIVE                       SUBROUTINE...DAPCSM
# MODIFIED BY SCHLUNDT                             21 OCTOBER 1968
# FUNCTIONAL DESCRIPTION....
#
# *A SELF-PERPETUATING WAITLIST TASK AT 1/2 SECOND INTERVALS WHICH:
# PREPARES THE ROLL DAP WITH OGA (CDUX)
# PREPARES THE ROLL FDAI NEEDLE (FLY-TO  OGA ERROR)
# PREPARES THE ROLL PHASE PLANE  OGAERR  (FLY-FROM  OGA ERROR)
# PREPARES THE TVC ROLLDAP TASK WAITLIST CALL (3 CS DELAY)
# UPDATES THE NEEDLES DISPLAY
# UPDATES VEHICLE MASS AND CALLS MASSPROP TO UPDATE INERTIA DATA
# UPDATES PITCH, YAW, AND ROLL DAP GAINS FROM MASSPROP DATA
# PERFORMS ONE-SHOT CORRECTION FOR TMC LOOP 0-3 SEC AFTER IGNITION
# PERFORMS REPETITIVE UPDATES FOR TMC LOOP AFTER THE ONE-SHOT CORR.
#
# CALLING SEQUENCE....
#
# *TVCEXEC CALLED AS A WAITLIST TASK, IN PARTICULAR BY TVCINIT4 AND BY
# ITSELF, BOTH AT 1/2 SECOND INTERVALS
#
# NORMAL EXIT MODE.... TASKOVER
#
# ALARM OR ABORT EXIT MODES.... NONE
#
# SUBROUTINES CALLED....NEEDLER, S40.15, MASSPROP, TASKOVER, IBNKCALL
#
# OTHER INTERFACES....
#
# *TVCRESTART PACKAGE FOR RESTARTS
# *PITCHDAP, YAWDAP FOR VARIABLE GAINS AND ENGINE TRIM ANGLES
# ERASABLE INITIALIZATION REQUIRED....
#
# *SEE TVCDAPON....TVCINIT4
# *VARK AND 1/CONACC (S40.15 OF TVCINITIALIZE)
# *PAD LOAD EREPFRAC
# *BITS 15,14 OF FLAGWRD6 (T5 BITS)
# *TVCEXPHS FOR RESTARTS
# *ENGINE-ON BIT (11.13) FOR RESTARTS
# *CDUX, OGAD
#
# OUTPUT....
#
# *ROLL DAP OGANOW, FDAI NEEDLE (AK), AND PHASE PLANE OGAERR
# *VARIABLE GAINS FOR PITCH/YAW AND ROLL TVC DAPS
# *SINGLE-SHOT AND REPETITIVE CORRECTIONS TO ENGINE TRIM ANGLES
# PACTOFF AND YACTOFF
#
# DEBRIS....    MUCH, BUT SHAREABLE WITH RCS/ENTRY, ALL IN EBANK6

# Page 946
#   BANK 16
#   SETLOC DAPROLL
#   BANK
#   EBANK= BZERO
#   COUNT* $$/TVCX

W('16,2720', 0o40102, 'TVCEXEC', 'CS', 'FLAGWRD6', 'CHECK FOR TERMINATION (BITS 15,14 READ', line=92)
W('16,2721', 0o74105, '', 'MASK', 'OCT60000', '     10 FROM TVCDAPON TO RCSDAPON)', line=93)
W('16,2722', 0o00006, '', 'EXTEND', line=94)
W('16,2723', 0o63134, '', 'BZMF', 'TVCEXFIN', 'TERMINATE', line=95)

W('16,2724', 0o35036, '', 'CAF', '.5SEC', 'W.L. CALL TO PERPETUATE TVCEXEC', line=97)
W('16,2725', 0o05245, '', 'TC', 'WAITLIST', line=98)
#   EBANK= BZERO
W('16,2726', 0o02720, '', '2CADR', 'TVCEXEC', kind='data', line=100)
W('16,2727', 0o34066, kind='data', line=100)

W('16,2730', 0o30032, 'ROLLPREP', 'CAE', 'CDUX', 'UPDATE ROLL LADDERS (NO NEED TO RESTART-', line=102)
W('16,2731', 0o57662, '', 'XCH', 'OGANOW', '     PROTECT, SINCE ROLL DAPS RE-START)', line=103)
W('16,2732', 0o57663, '', 'XCH', 'OGAPAST', line=104)

W('16,2733', 0o31450, '', 'CAE', 'OGAD', 'PREPARE ROLL FDAI NEEDLE WITH FLY-TO', line=106)
W('16,2734', 0o00006, '', 'EXTEND', '', '     ERROR (COMMAND - MEASURED)', line=107)
W('16,2735', 0o21662, '', 'MSU', 'OGANOW', line=108)
W('16,2736', 0o55476, '', 'TS', 'AK', 'FLY-TO OGA ERROR, SC.AT B-1 REVS', line=109)

W('16,2737', 0o00006, '', 'EXTEND', '', 'PREPARE ROLL DAP PHASE PLANE  OGAERR', line=111)
W('16,2740', 0o77705, '', 'MP', '-BIT14', line=112)
W('16,2741', 0o55664, '', 'TS', 'OGAERR', 'PHASE-PLANE (FLY-FROM) OGAERROR,', line=113)
# SC.AT B+0 REVS

W('16,2742', 0o36214, '', 'CAF', 'THREE', 'SET UP ROLL DAP TASK (ALLOW SOME TIME)', line=116)
W('16,2743', 0o05245, '', 'TC', 'WAITLIST', line=117)
#   EBANK= BZERO
W('16,2744', 0o03272, '', '2CADR', 'ROLLDAP', kind='data', line=119)
W('16,2745', 0o34066, kind='data', line=119)

W('16,2746', 0o04740, 'NEEDLEUP', 'TC', 'IBNKCALL', 'DO A NEEDLES UPDATE (RETURNS AFTER CADR)', line=121)
W('16,2747', 0o42420, '', 'CADR', 'NEEDLER', '     (NEEDLES RESTARTS ITSELF)', kind='data', line=122)

W('16,2750', 0o35003, 'VARGAINS', 'CAF', 'BIT13', 'CHECK ENGINE-ON BIT TO INHIBIT VARIABLE', line=124)
W('16,2751', 0o00006, '', 'EXTEND', '', '     GAINS AND MASS IF ENGINE OFF', line=125)
W('16,2752', 0o02011, '', 'RAND', 'DSALMOUT', 'CHANNEL 11', line=126)
W('16,2753', 0o10000, '', 'CCS', 'A', line=127)
W('16,2754', 0o12760, '', 'TCF', '+4', '    ON , SO OK TO UPDATE GAINS AND MASS', line=128)
W('16,2755', 0o35016, '', 'CAF', 'TWO', '     OFF, SO BYPASS MASS/GAIN UPDATES,', line=129)
W('16,2756', 0o55651, '', 'TS', 'TVCEXPHS', '          ALSO ENTRY FROM CCS BELOW WITH', line=130)
W('16,2757', 0o13011, '', 'TCF', '1SHOTCHK', '          VCNTR = -0 (V97 R40 ENGFAIL)', line=131)
W('16,2760', 0o11643, '', 'CCS', 'VCNTR', '     TEST FOR GAIN OF UPDATE TIME', line=132)
W('16,2761', 0o12765, '', 'TCF', '+4', '          NOT YET', line=133)
# Page 947
W('16,2762', 0o12771, '', 'TCF', 'GAINCHNG', '              NOW', line=135)
W('16,2763', 0o12763, '', 'TCF', '+0', '              NOT USED', line=136)
W('16,2764', 0o12755, '', 'TCF', 'VARGAINS +5', '              NO, LOTHRUST (S40.8 R40)', line=137)

W('16,2765', 0o55653, '', 'TS', 'VCNTRTMP', '       PROTECT VCNTR AND', line=139)
W('16,2766', 0o31474, '', 'CAE', 'CSMMASS', '      CSMMASS DURING AN IMPULSIVE BURN', line=140)
W('16,2767', 0o55652, '', 'TS', 'MASSTMP', line=141)
W('16,2770', 0o13002, '', 'TCF', 'EXECCOPY', line=142)

W('16,2771', 0o04740, 'GAINCHNG', 'TC', 'IBNKCALL', 'UPDATE IXX, IAVG, IAVG/TLX', line=144)
W('16,2772', 0o13422, '', 'CADR', 'FIXCW', 'MASSPROP ENTRY  (ALREADY INITIALIZED)', kind='data', line=145)
W('16,2773', 0o04740, '', 'TC', 'IBNKCALL', 'UPDATE 1/CONACC, VARK', line=146)
W('16,2774', 0o36462, '', 'CADR', 'S40.15', '     (S40.15 IS IN TVCINITIALIZE)', kind='data', line=147)
W('16,2775', 0o41637, '', 'CS', 'TENMDOT', 'UPDATE MASS FOR NEXT 10 SEC. OF BURN', line=148)
W('16,2776', 0o61474, '', 'AD', 'CSMMASS', line=149)
W('16,2777', 0o55652, '', 'TS', 'MASSTMP', 'KG B+16', line=150)

W('16,3000', 0o34374, '', 'CAF', 'NINETEEN', 'RESET THE VARIABLE-GAIN UPDATE COUNTER', line=152)
W('16,3001', 0o55653, '', 'TS', 'VCNTRTMP', line=153)

W('16,3002', 0o25651, 'EXECCOPY', 'INCR', 'TVCEXPHS', 'RESTART-PROTECT THE COPYCYCLE        (1)', line=155)

W('16,3003', 0o31652, '', 'CAE', 'MASSTMP', 'CSMMASS KG B+16', line=157)
W('16,3004', 0o55474, '', 'TS', 'CSMMASS', line=158)

W('16,3005', 0o31653, '', 'CAE', 'VCNTRTMP', 'VCNTR', line=160)
W('16,3006', 0o55643, '', 'TS', 'VCNTR', line=161)
W('16,3007', 0o55444, '', 'TS', 'V97VCNTR', 'FOR ENGFAIL (R41) MASS UPDATES AT SPSOFF', line=162)

W('16,3010', 0o25651, '', 'INCR', 'TVCEXPHS', 'COPYCYCLE OVER                       (2)', line=164)

W('16,3011', 0o11447, '1SHOTCHK', 'CCS', 'CNTR', 'CHECK TIME FOR ONE-SHOT OR REPCORR', line=166)
W('16,3012', 0o13016, '', 'TCF', '+4', '     NOT YET', line=167)
W('16,3013', 0o13031, '', 'TCF', '1SHOTOK', '     NOW', line=168)
W('16,3014', 0o13022, '', 'TCF', 'REPCHEK', '     ONE-SHOT OVER, ON TO REPCORR', line=169)
W('16,3015', 0o13031, '', 'TCF', '1SHOTOK', '     NOW  (ONE-SHOT ONLY, NO REPCORR)', line=170)

W('16,3016', 0o55676, '', 'TS', 'CNTRTMP', 'COUNT DOWN', line=172)
W('16,3017', 0o36211, '', 'CAF', 'SIX', 'SET UP TVCEXPHS FOR ENTRY AT CNTRCOPY', line=173)
W('16,3020', 0o55651, '', 'TS', 'TVCEXPHS', line=174)
W('16,3021', 0o13132, '', 'TCF', 'CNTRCOPY', line=175)

W('16,3022', 0o31642, 'REPCHEK', 'CAE', 'REPFRAC', 'CHECK FOR REPETITIVE UPDATES', line=177)
W('16,3023', 0o00006, '', 'EXTEND', line=178)
W('16,3024', 0o63134, '', 'BZMF', 'TVCEXFIN', '     NO, OVER-AND-OUT', line=179)
W('16,3025', 0o55446, '', 'TS', 'TEMPDAP +1', '     YES, SET UP CORRECTION FRACTION', line=180)
W('16,3026', 0o35015, '', 'CAF', 'FOUR', 'SET UP TVCEXPHS FOR ENTRY AT CORSETUP', line=181)
W('16,3027', 0o55651, '', 'TS', 'TVCEXPHS', line=182)
W('16,3030', 0o13043, '', 'TCF', 'CORSETUP', line=183)
# Page 948
W('16,3031', 0o35003, '1SHOTOK', 'CAF', 'BIT13', 'CHECK ENGINE-ON BIT, NOT PERMITTING', line=185)
W('16,3032', 0o00006, '', 'EXTEND', '', '     ONE-SHOT DURING ENGINE-SHUTDOWN', line=186)
W('16,3033', 0o02011, '', 'RAND', 'DSALMOUT', line=187)
W('16,3034', 0o10000, '', 'CCS', 'A', line=188)
W('16,3035', 0o13037, '', 'TCF', '+2', '     ONE-SHOT OK', line=189)
W('16,3036', 0o13134, '', 'TCF', 'TVCEXFIN', '     NO, TERMINATE', line=190)

W('16,3037', 0o25651, '', 'INCR', 'TVCEXPHS', '                                      (3)', line=192)

# RSB 2009.  The following instruction was previously "CAE FCORFRAC", but FCORFRAC
# is not in erasable memory as implied by the use of CAE.  I've accordingly changed
# it to CAF instead to indicate fixed memory.
W('16,3040', 0o33137, 'TEMPSET', 'CAF', 'FCORFRAC', '     SET UP CORRECTION FRACTION', line=197)
W('16,3041', 0o55446, '', 'TS', 'TEMPDAP +1', line=198)

W('16,3042', 0o25651, '', 'INCR', 'TVCEXPHS', 'ENTRY FROM REPCHECK AT NEXT LOCATION  (4)', line=200)

W('16,3043', 0o31466, 'CORSETUP', 'CAE', 'DAPDATR1', 'CHECK FOR LEM-OFF/ON', line=202)
W('16,3044', 0o75003, '', 'MASK', 'BIT13', '(NOTE, SHOWS LEM-OFF)', line=203)
W('16,3045', 0o00006, '', 'EXTEND', line=204)
W('16,3046', 0o13050, '', 'BZF', '+2', 'LEM IS ON,  PICK UP   TEMPDAP+1', line=205)
W('16,3047', 0o31446, '', 'CAE', 'TEMPDAP +1', 'LEM IS OFF, PICK UP 2(TEMPDAP+1)', line=206)
W('16,3050', 0o61446, '', 'AD', 'TEMPDAP +1', line=207)
W('16,3051', 0o55445, '', 'TS', 'TEMPDAP', 'CG.CORR USES TEMPDAP', line=208)

W('16,3052', 0o37716, '', 'CAF', 'NEGONE', 'SET UP FOR CNTR = -1 (ONE-SHOT DONE)', line=210)
W('16,3053', 0o55676, '', 'TS', 'CNTRTMP', '     (COPYCYCLE AT  .CNTRCOPY. )', line=211)

W('16,3054', 0o00006, 'CG.CORR', 'EXTEND', '', 'PITCH TMC LOOP', line=213)
W('16,3055', 0o31606, '', 'DCA', 'PDELOFF', line=214)
W('16,3056', 0o53673, '', 'DXCH', 'PACTTMP', line=215)
W('16,3057', 0o00006, '', 'EXTEND', line=216)
W('16,3060', 0o41606, '', 'DCS', 'PDELOFF', line=217)
W('16,3061', 0o20001, '', 'DDOUBL', line=218)
W('16,3062', 0o20001, '', 'DDOUBL', line=219)
W('16,3063', 0o53612, '', 'DXCH', 'TTMP1', line=220)
W('16,3064', 0o00006, '', 'EXTEND', line=221)
W('16,3065', 0o31602, '', 'DCA', 'DELPBAR', line=222)
W('16,3066', 0o20001, '', 'DDOUBL', line=223)
W('16,3067', 0o20001, '', 'DDOUBL', line=224)
W('16,3070', 0o21612, '', 'DAS', 'TTMP1', line=225)
W('16,3071', 0o00006, '', 'EXTEND', line=226)
W('16,3072', 0o31612, '', 'DCA', 'TTMP1', line=227)
W('16,3073', 0o00006, '', 'EXTEND', line=228)
W('16,3074', 0o71445, '', 'MP', 'TEMPDAP', line=229)
W('16,3075', 0o21673, '', 'DAS', 'PACTTMP', line=230)

W('16,3076', 0o00006, '', 'EXTEND', '', 'YAW TMC LOOP', line=232)
W('16,3077', 0o31610, '', 'DCA', 'YDELOFF', line=233)
W('16,3100', 0o53675, '', 'DXCH', 'YACTTMP', line=234)
W('16,3101', 0o00006, '', 'EXTEND', line=235)
W('16,3102', 0o41610, '', 'DCS', 'YDELOFF', line=236)
W('16,3103', 0o20001, '', 'DDOUBL', line=237)
# Page 949
W('16,3104', 0o20001, '', 'DDOUBL', line=239)
W('16,3105', 0o53612, '', 'DXCH', 'TTMP1', line=240)
W('16,3106', 0o00006, '', 'EXTEND', line=241)
W('16,3107', 0o31604, '', 'DCA', 'DELYBAR', line=242)
W('16,3110', 0o20001, '', 'DDOUBL', line=243)
W('16,3111', 0o20001, '', 'DDOUBL', line=244)
W('16,3112', 0o21612, '', 'DAS', 'TTMP1', line=245)
W('16,3113', 0o00006, '', 'EXTEND', line=246)
W('16,3114', 0o31612, '', 'DCA', 'TTMP1', line=247)
W('16,3115', 0o00006, '', 'EXTEND', line=248)
W('16,3116', 0o71445, '', 'MP', 'TEMPDAP', line=249)
W('16,3117', 0o21675, '', 'DAS', 'YACTTMP', line=250)

W('16,3120', 0o25651, 'CORCOPY', 'INCR', 'TVCEXPHS', 'RESTART PROTECT THE COPYCYCLE         (5)', line=252)

W('16,3121', 0o00006, '', 'EXTEND', '', 'TRIM-ESTIMATES, AND', line=254)
W('16,3122', 0o31673, '', 'DCA', 'PACTTMP', line=255)
W('16,3123', 0o55423, '', 'TS', 'PACTOFF', '      TRIMS', line=256)
W('16,3124', 0o53606, '', 'DXCH', 'PDELOFF', line=257)

W('16,3125', 0o00006, '', 'EXTEND', line=259)
W('16,3126', 0o31675, '', 'DCA', 'YACTTMP', line=260)
W('16,3127', 0o55424, '', 'TS', 'YACTOFF', line=261)
W('16,3130', 0o53610, '', 'DXCH', 'YDELOFF', line=262)

W('16,3131', 0o25651, '', 'INCR', 'TVCEXPHS', 'ENTRY FROM 1SHOTCHK AT NEXT LOCATION  (6)', line=264)

W('16,3132', 0o31676, 'CNTRCOPY', 'CAE', 'CNTRTMP', 'UPDATE CNTR (RESTARTS OK, FOLLOWS CPYCY)', line=266)
W('16,3133', 0o55447, '', 'TS', 'CNTR', line=267)

W('16,3134', 0o35021, 'TVCEXFIN', 'CAF', 'ZERO', 'RESET TVCEXPHS', line=269)
W('16,3135', 0o55651, '', 'TS', 'TVCEXPHS', line=270)
W('16,3136', 0o15324, '', 'TCF', 'TASKOVER', 'TVCEXECUTIVE FINISHED', line=271)

W('16,3137', 0o10000, 'FCORFRAC', 'OCT', '10000', 'ONE-SHOT CORRECTION FRACTION', kind='data', line=273)

# Page 950 (page is empty)
