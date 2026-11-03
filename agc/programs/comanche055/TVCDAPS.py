"""TVCDAPS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/TVCDAPS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 961-978 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TVCDAPS', 'TVCDAPS.agc', 'Comanche055', pages='961-978')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TVCDAPS.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        961-978
# Mod history:  2009-05-13 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
# 2009-05-20 RSB  Corrections:  Eliminated an extraneous EXTEND,
# added a missing instruction to PFORWARD.
# 2000-05-21 RSB  Wrong opcode was used with DELBRTMP and
# DELBRTMP +1 operands in 4 places.  Corrected
# an MP operation in 2CASFLTR.
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

# Page 961
# PROGRAM NAME....TVCDAP, CONSISTING OF PITCHDAP, YAWDAP, ETC.
# LOG SECTION...TVCDAPS                         SUBROUTINE...DAPCSM
# MODIFIED BY SCHLUNDT                          21 OCTOBER 1968
# FUNCTIONAL DESCRIPTION....

# SELF-PERPETUATING T5 TASKS WHICH GENERATE THE COMMAND SIGNALS
# FOR THE PITCH AND YAW SPS GIMBAL ACTUATORS DURING TVC (SPS) BURNS,
# IN RESPONSE TO BODY-AXIS RATE COMMANDS FROM CROSS-PRODUCT STEERING
# (S40.8).  IF NO STEERING (IMPULSIVE BURNS) MAINTAINS ATTITUDE-HOLD
# ABOUT THE REFERENCE (INITIAL) DIRECTIONS (ZERO RATE COMMANDS).

# THE PITCH AND YAW LOOPS ARE SEPARATE, BUT STRUCTURED IDENTICALLY.
# EACH ATTITUDE-RATE LOOP INCLUDES GIMBAL ANGLE RATE DERIVATION,
# GIMBAL/BODY AXIS TRANSFORMATION, BODY-AXIS ATTITUDE ERROR
# INTEGRATION WITH ERROR LIMITING, THE GENERALIZED 6TH-ORDER FILTER
# FOR CSM OR CSM/LM OPERATION. A FILTER OUTPUT LIMITER.
# CG-OFFSET TRACKER FILTER, AND THE CG-TRACKER MINOR LOOP.

# THE DAPS ARE CYCLIC, CALLING EACH OTHER AT 1/2 THE DAP SAMPLE
# TIME, AS DETERMINED BY T5TVCDT.  THE ACTUATOR COMMANDS ARE
# REGENERATED AS ANALOG VOLTAGES BY THE OPTICS ERROR COUNTERS, WHICH
# TRANSMIT THE SIGNAL TO THE ACTUATOR SERVOS WHEN THERE IS PROPER CDU
# MODING.

# CALLING SEQUENCE.... (TYPICALLY)

# T5 CALL OF TVCDAPON (TVCINITIALIZE) BY DOTVCON (P40)
# T5 CALL OF DAPINIT (TVCDAPS) BY TVCINIT4 (TVCINITIALIZE)
# T5 CALL OF PITCHDAP BY DAPINIT
# T5 CALL OF YAWDAP BY PITCHDAP
# T5 CALL OF PITCHDAP BY YAWDAP
# ETC.
# (AUTOMATIC SEQUENCING FROM TVCDAPON)

# NORMAL EXIT MODE....RESUME

# ALARM OR ABORT EXIT MODES....NONE

# SUBROUTINES CALLED....

# HACK FOR STROKE TEST (V68) WAVEFORM GENERATION
# PCOPY, YCOPY FOR COPY-CYCLES (USED ALSO BY TVC RESTART PACKAGE)
# DAPINIT FOR INITIAL CDUS FOR RATE MEASUREMENTS
# ERRORLIM, ACTLIM FOR INPUT (ATTITUDE-ERROR INTEGRATION) AND
# OUTPUT (ACTUATOR COMMAND) LIMITING, COMMON TO PITCH AND
# YAW DAPS
# FWDFLTR (INCLUDING OPTVARK) AND PRECOMP, TO COMPUTE FILTER
# OUTPUTS AND STORAGE VALUES
# RESUME

# Page 962
# OTHER INTERFACES....

# S40.8 CROSS-PRODUCT STEERING FOR BODY AXIS RATE COMMANDS OMEGAY,ZC
# S40.15 FOR THE INITIAL DAP GAINS VARK AND 1/CONACC
# TVCEXECUTIVE FOR DAP GAIN UPDATES AND TMC LOOP OPERATIONS
# TVCRESTART PACKAGE FOR TVC RESTART PROTECTION.

# ERASABLE INITIALIZATION REQUIRED....

# PAD-LOAD ERASABLES ( SEE ERASABLE ASSIGNMENTS )
# CONFIGURATION BITS (14, 13) OF DAPDATR1 AS IN R03
# ENGINE-ON BIT (11.13) FOR RESTARTS
# TVCPHASE FOR RESTARTS ( SEE DOTVCON, AND TVCINIT4 )
# T5 BITS (15,14 OF FLAGWRD6) FOR RESTARTS
# MISCELLANEOUS VARIABLES SET UP OR COMPUTED BY TVCDAPON....TVCINIT4,
# INCLUDING THE ZEROING OF TEMPORARIES BY MRCLEAN
# CDUX,Y,Z AND SINCDUX....COSCDUX AS PREPARED BY QUICTRIG (WITH
# UPDATES EVERY 1/2 SECOND)
# ALSO G+N PRIMARY, TVC ENABLE, AND OPTICS ERROR COUNTER ENABLE
# UNLESS BENCH-TESTING.
#
# OUTPUT....
#
# TVCPITCH AND TVCYAW WITH COUNTER RELEASE (11.14 AND 11.13 INCREMEN-
# TAL COMMANDS TO OPTICS ERROR COUNTERS), FILTER NODES, BODY-
# AXIS ATTITUDE ERROR INTEGRATOR, TOTAL ACTUATOR COMMANDS,
# OFFSET-TRACKER-FILTER OUTPUTS, ETC.
# DEBRIS....

# MUCH, SHAREABLE WITH RCS/ENTRY, IN EBANK6 ONLY

#   BANK 17
#   SETLOC DAPS2
#   BANK

#   EBANK= BZERO

#   COUNT* $$/DAPS

# Page 963
# PITCH TVCDAP STARTS HERE....(INCORPORATES CSM/LEM DAP FILTER, MODOR DESIGN)

W('20,2530', 0o22016, 'PITCHDAP', 'LXCH', 'BANKRUPT', 'T5 ENTRY, NORMAL OR VIA DAPINIT', line=129)
W('20,2531', 0o00006, '', 'EXTEND', line=130)
W('20,2532', 0o22012, '', 'QXCH', 'QRUPT', line=131)

W('20,2533', 0o33475, '', 'CAF', 'YAWT5', 'SET UP T5 CALL FOR YAW AUTOPILOT (LOW-', line=133)
W('20,2534', 0o55312, '', 'TS', 'T5LOC', '      ORDER PART OF 2CADR ALREADY THERE)', line=134)
W('20,2535', 0o31625, '', 'CAE', 'T5TVCDT', line=135)
W('20,2536', 0o54030, '', 'TS', 'TIME5', line=136)

W('20,2537', 0o11574, 'PSTROKER', 'CCS', 'STROKER', '(STRKFLG) CHECK FOR STROKE TEST', line=138)
W('20,2540', 0o03533, '', 'TC', 'HACK', 'TEST-START OR TEST-IN-PROGRESS', line=139)
W('20,2541', 0o12543, '', 'TCF', '+2', 'NO-TEST', line=140)
W('20,2542', 0o03533, '', 'TC', 'HACK', 'TEST-IN-PROGRESS', line=141)

W('20,2543', 0o30033, 'PCDUDOTS', 'CAE', 'CDUY', 'COMPUTE CDUYDOT (USED BY PITCH AND YAW)', line=143)
W('20,2544', 0o57645, '', 'XCH', 'PCDUYPST', line=144)
W('20,2545', 0o00006, '', 'EXTEND', line=145)
W('20,2546', 0o21645, '', 'MSU', 'PCDUYPST', line=146)
W('20,2547', 0o02560, '', 'TCR', 'RLIMTEST', '      RATE TEST', line=147)
W('20,2550', 0o55647, '', 'TS', 'MCDUYDOT', '      (MINUS, SC.AT 1/2TVCDT REVS/SEC)', line=148)

W('20,2551', 0o30034, '', 'CAE', 'CDUZ', 'COMPUTE CDUZDOT (USED BY PITCH AND YAW)', line=150)
W('20,2552', 0o57646, '', 'XCH', 'PCDUZPST', line=151)
W('20,2553', 0o00006, '', 'EXTEND', line=152)
W('20,2554', 0o21646, '', 'MSU', 'PCDUZPST', line=153)
W('20,2555', 0o02560, '', 'TCR', 'RLIMTEST', '      RATE TEST', line=154)
W('20,2556', 0o55650, '', 'TS', 'MCDUZDOT', '      (MINUS, SC.AT 1/2TVCDT REVS/SEC)', line=155)
W('20,2557', 0o12571, '', 'TCF', 'PINTEGRL', line=156)

W('20,2560', 0o55611, 'RLIMTEST', 'TS', 'TTMP1', 'TEST FOR EXCESSIVE CDU RATES (GREATER', line=158)
W('20,2561', 0o00006, '', 'EXTEND', '', '      THAN 2.33 DEG IN ONE SAMPLE PERIOD)', line=159)
W('20,2562', 0o73476, '', 'MP', '1/RTLIM', line=160)
W('20,2563', 0o00006, '', 'EXTEND', line=161)
W('20,2564', 0o12567, '', 'BZF', '+3', line=162)
W('20,2565', 0o35021, '', 'CAF', 'ZERO', line=163)
W('20,2566', 0o55611, '', 'TS', 'TTMP1', line=164)
W('20,2567', 0o31611, '', 'CAE', 'TTMP1', line=165)
W('20,2570', 0o00002, '', 'TC', 'Q', line=166)

W('20,2571', 0o00006, 'PINTEGRL', 'EXTEND', '', 'COMPUTE INTEGRAL OF BODY-AXIS PITCH-RATE', line=168)
W('20,2572', 0o31576, '', 'DCA', 'PERRB', '      ERROR, SC.AT B-1 REVS', line=169)
W('20,2573', 0o53703, '', 'DXCH', 'ERRBTMP', line=170)

W('20,2574', 0o00006, '', 'EXTEND', line=172)
W('20,2575', 0o31530, '', 'DCA', 'OMEGAYC', line=173)
W('20,2576', 0o21703, '', 'DAS', 'ERRBTMP', line=174)

# Page 964
W('20,2577', 0o40746, '', 'CS', 'COSCDUZ', 'PREPARE BODY-AXIS PITCH RATE, OMEGAYB', line=177)
W('20,2600', 0o00006, '', 'EXTEND', line=178)
W('20,2601', 0o70750, '', 'MP', 'COSCDUX', line=179)
W('20,2602', 0o20001, '', 'DDOUBL', line=180)
W('20,2603', 0o00006, '', 'EXTEND', line=181)
W('20,2604', 0o71647, '', 'MP', 'MCDUYDOT', line=182)
W('20,2605', 0o20001, '', 'DDOUBL', line=183)
W('20,2606', 0o53536, '', 'DXCH', 'OMEGAYB', line=184)

W('20,2607', 0o41650, '', 'CS', 'MCDUZDOT', line=186)
W('20,2610', 0o00006, '', 'EXTEND', line=187)
W('20,2611', 0o70742, '', 'MP', 'SINCDUX', line=188)
W('20,2612', 0o20001, '', 'DDOUBL', line=189)
W('20,2613', 0o21536, '', 'DAS', 'OMEGAYB', '(COMPLETED OMEGAYB, SC.AT 1/2TVCDT REVS)', line=190)

W('20,2614', 0o00006, '', 'EXTEND', '', 'PICK UP -OMEGAYB (SIGN CHNG, INTEGRATE)', line=192)
W('20,2615', 0o41536, '', 'DCS', 'OMEGAYB', line=193)
W('20,2616', 0o21703, '', 'DAS', 'ERRBTMP', line=194)

W('20,2617', 0o03124, 'PERORLIM', 'TCR', 'ERRORLIM', 'PITCH BODY-AXIS-ERROR INPUT LIMITER', line=196)

W('20,2620', 0o00006, 'PFORWARD', 'EXTEND', '', '      PREPARE THE FILTER STORAGE LOCATIONS', line=198)
W('20,2621', 0o31542, '', 'DCA', 'PTMP1', '      FOR THE PITCH CHANNEL', line=199)
W('20,2622', 0o53707, '', 'DXCH', 'TMP1', line=200)
W('20,2623', 0o00006, '', 'EXTEND', line=201)
W('20,2624', 0o31546, '', 'DCA', 'PTMP3', line=202)
W('20,2625', 0o53713, '', 'DXCH', 'TMP3', line=203)
W('20,2626', 0o00006, '', 'EXTEND', line=204)
W('20,2627', 0o31552, '', 'DCA', 'PTMP5', line=205)
W('20,2630', 0o53717, '', 'DXCH', 'TMP5', line=206)

W('20,2631', 0o03156, '', 'TCR', 'FWDFLTR', 'GO COMPUTE PRESENT OUTPUT', line=208)
# (INCLUDES VARIABLE GAIN PACKAGE)

W('20,2632', 0o00006, 'POFFSET', 'EXTEND', line=211)
W('20,2633', 0o31606, '', 'DCA', 'PDELOFF', line=212)
W('20,2634', 0o21705, '', 'DAS', 'CMDTMP', 'NO SCALED AT B+0 ASCREV', line=213)

W('20,2635', 0o03137, 'PACLIM', 'TCR', 'ACTLIM', 'ROUND OFF & LIMIT PITCH ACTUATOR COMMAND', line=215)

W('20,2636', 0o41623, 'POUT', 'CS', 'PCMD', 'INCREMENTAL PITCH COMMAND', line=217)
W('20,2637', 0o61704, '', 'AD', 'CMDTMP', line=218)
W('20,2640', 0o26054, '', 'ADS', 'TVCPITCH', 'UPDATE THE ERROR COUNTER (NO RESTART-', line=219)
# PROTECT. SINCE ERROR CNTR ZEROED)

W('20,2641', 0o35005, '', 'CAF', 'BIT11', 'BIT FOR TVCPITCH COUNT RELEASE', line=222)
W('20,2642', 0o00006, '', 'EXTEND', line=223)
W('20,2643', 0o05014, '', 'WOR', 'CHAN14', line=224)

W('20,2644', 0o00006, 'PPRECOMP', 'EXTEND', '', '      PREPARE THE FILTER STORAGE FOR PITCH', line=226)
# Page 965
W('20,2645', 0o31544, '', 'DCA', 'PTMP2', line=228)
W('20,2646', 0o53711, '', 'DXCH', 'TMP2', line=229)
W('20,2647', 0o00006, '', 'EXTEND', line=230)
W('20,2650', 0o31550, '', 'DCA', 'PTMP4', line=231)
W('20,2651', 0o53715, '', 'DXCH', 'TMP4', line=232)
W('20,2652', 0o00006, '', 'EXTEND', line=233)
W('20,2653', 0o31554, '', 'DCA', 'PTMP6', line=234)
W('20,2654', 0o53721, '', 'DXCH', 'TMP6', line=235)

W('20,2655', 0o03247, '', 'TCR', 'PRECOMP', '      TO THE FILTER FOR PRECOMPUTATION', line=237)

W('20,2656', 0o31602, 'DELBARP', 'CAE', 'DELPBAR +1', 'UPDATE PITCH OFFSET-TRACKER-FILTER', line=239)
W('20,2657', 0o00006, '', 'EXTEND', line=240)
W('20,2660', 0o73500, '', 'MP', 'E(-AT)', line=241)
W('20,2661', 0o55701, '', 'TS', 'DELBRTMP +1', line=242)
W('20,2662', 0o31601, '', 'CAE', 'DELPBAR', line=243)
W('20,2663', 0o00006, '', 'EXTEND', line=244)
W('20,2664', 0o73500, '', 'MP', 'E(-AT)', line=245)
W('20,2665', 0o21701, '', 'DAS', 'DELBRTMP', line=246)
W('20,2666', 0o31704, '', 'CAE', 'CMDTMP', line=247)
W('20,2667', 0o00006, '', 'EXTEND', line=248)
W('20,2670', 0o73477, '', 'MP', '1-E(-AT)', line=249)
W('20,2671', 0o21701, '', 'DAS', 'DELBRTMP', line=250)

W('20,2672', 0o02674, 'PCOPYCYC', 'TCR', 'PCOPY', 'PITCH COPYCYCLE', line=252)

W('20,2673', 0o15333, 'PDAPEND', 'TCF', 'RESUME', 'PITCH DAP COMPLETED', line=254)
# Page 966
# PITCH TVCDAP COPYCYCLE SUBROUTINE (CALLED VIA PITCH TVCDAP OR TVC RESTART PACKAGE)

W('20,2674', 0o25644, 'PCOPY', 'INCR', 'TVCPHASE', 'RESTART-PROTECT THE COPYCYCLE.        (1)', line=258)
# NOTE POSSIBLE RE-ENTRY FROM RESTART
# PACKAGE, SHOULD A RESTART OCCUR
# DURING PITCH COPYCYCLE.

W('20,2675', 0o00006, '', 'EXTEND', line=263)
W('20,2676', 0o31707, '', 'DCA', 'TMP1', line=264)
W('20,2677', 0o53542, '', 'DXCH', 'PTMP1', line=265)
W('20,2700', 0o00006, '', 'EXTEND', line=266)
W('20,2701', 0o31711, '', 'DCA', 'TMP2', line=267)
W('20,2702', 0o53544, '', 'DXCH', 'PTMP2', line=268)
W('20,2703', 0o00006, '', 'EXTEND', line=269)
W('20,2704', 0o31713, '', 'DCA', 'TMP3', line=270)
W('20,2705', 0o53546, '', 'DXCH', 'PTMP3', line=271)
W('20,2706', 0o00006, '', 'EXTEND', line=272)
W('20,2707', 0o31715, '', 'DCA', 'TMP4', line=273)
W('20,2710', 0o53550, '', 'DXCH', 'PTMP4', line=274)
W('20,2711', 0o00006, '', 'EXTEND', line=275)
W('20,2712', 0o31717, '', 'DCA', 'TMP5', line=276)
W('20,2713', 0o53552, '', 'DXCH', 'PTMP5', line=277)
W('20,2714', 0o00006, '', 'EXTEND', line=278)
W('20,2715', 0o31721, '', 'DCA', 'TMP6', line=279)
W('20,2716', 0o53554, '', 'DXCH', 'PTMP6', line=280)

W('20,2717', 0o00006, 'PMISC', 'EXTEND', '', 'MISC....PITCH-RATE-ERROR INTEGRATOR', line=282)
W('20,2720', 0o31703, '', 'DCA', 'ERRBTMP', line=283)
W('20,2721', 0o55477, '', 'TS', 'AK1', '      FOR PITCH NEEDLES, SC.AT B-1 REVS', line=284)
W('20,2722', 0o53576, '', 'DXCH', 'PERRB', line=285)

W('20,2723', 0o31704, '', 'CAE', 'CMDTMP', '      PITCH ACTUATOR COMMAND', line=287)
W('20,2724', 0o55623, '', 'TS', 'PCMD', line=288)

W('20,2725', 0o00006, '', 'EXTEND', '', '      PITCH OFFSET-TRACKER-FILTER', line=290)
W('20,2726', 0o31701, '', 'DCA', 'DELBRTMP', line=291)
W('20,2727', 0o53602, '', 'DXCH', 'DELPBAR', line=292)

W('20,2730', 0o25644, '', 'INCR', 'TVCPHASE', 'PITCH COPYCYCLE COMPLETED             (2)', line=294)

W('20,2731', 0o00002, '', 'TC', 'Q', line=296)

# Page 967
# YAW TVCDAP STARTS HERE....(INCORPORATES CSM/LEM DAP FILTER, MODOR DESIGN)

W('20,2732', 0o22016, 'YAWDAP', 'LXCH', 'BANKRUPT', 'T5 ENTRY, NORMAL', line=301)
W('20,2733', 0o00006, '', 'EXTEND', line=302)
W('20,2734', 0o22012, '', 'QXCH', 'QRUPT', line=303)

W('20,2735', 0o33473, '', 'CAF', 'PITCHT5', 'SET UP T5 CALL FOR PITCH AUTOPILOT (LOW-', line=305)
W('20,2736', 0o55312, '', 'TS', 'T5LOC', '      ORDER PART OF 2CADR ALREADY THERE)', line=306)
W('20,2737', 0o31625, '', 'CAE', 'T5TVCDT', line=307)
W('20,2740', 0o54030, '', 'TS', 'TIME5', line=308)

W('20,2741', 0o11574, 'YSTROKER', 'CCS', 'STROKER', '(STRKFLG) CHECK FOR STROKE TEST', line=310)
W('20,2742', 0o03533, '', 'TC', 'HACK', 'TEST-START OR TEST-IN-PROGRESS', line=311)
W('20,2743', 0o12745, '', 'TCF', '+2', 'NO-TEST', line=312)
W('20,2744', 0o03533, '', 'TC', 'HACK', 'TEST-IN-PROGRESS', line=313)

# USE BODY RATES FROM PITCHDAP (PCDUDOTS)

W('20,2745', 0o00006, 'YINTEGRL', 'EXTEND', '', 'COMPUTE INTEGRAL OF BODY-AXIS YAW-RATE', line=317)
W('20,2746', 0o31600, '', 'DCA', 'YERRB', '      ERROR, SC.AT B-1 REVS', line=318)
W('20,2747', 0o53703, '', 'DXCH', 'ERRBTMP', line=319)

W('20,2750', 0o00006, '', 'EXTEND', line=321)
W('20,2751', 0o31532, '', 'DCA', 'OMEGAZC', line=322)
W('20,2752', 0o21703, '', 'DAS', 'ERRBTMP', line=323)

W('20,2753', 0o30746, '', 'CAE', 'COSCDUZ', 'PREPARE BODY-AXIS YAW-RATE, OMEGAZB', line=325)
W('20,2754', 0o00006, '', 'EXTEND', line=326)
W('20,2755', 0o70742, '', 'MP', 'SINCDUX', line=327)
W('20,2756', 0o20001, '', 'DDOUBL', line=328)
W('20,2757', 0o00006, '', 'EXTEND', line=329)
W('20,2760', 0o71647, '', 'MP', 'MCDUYDOT', line=330)
W('20,2761', 0o20001, '', 'DDOUBL', line=331)
W('20,2762', 0o53540, '', 'DXCH', 'OMEGAZB', line=332)

W('20,2763', 0o41650, '', 'CS', 'MCDUZDOT', line=334)
W('20,2764', 0o00006, '', 'EXTEND', line=335)
W('20,2765', 0o70750, '', 'MP', 'COSCDUX', line=336)
W('20,2766', 0o20001, '', 'DDOUBL', line=337)
W('20,2767', 0o21540, '', 'DAS', 'OMEGAZB', '(COMPLETED OMEGAZB, SC.AT 1/2TVCDT REVS)', line=338)

W('20,2770', 0o00006, '', 'EXTEND', '', 'PICK UP -OMEGAZB (SIGN CHNG, INTEGRATE)', line=340)
W('20,2771', 0o41540, '', 'DCS', 'OMEGAZB', line=341)
W('20,2772', 0o21703, '', 'DAS', 'ERRBTMP', line=342)

W('20,2773', 0o03124, 'YERORLIM', 'TCR', 'ERRORLIM', 'YAW     BODY-AXIS-ERROR INPUT LIMITER', line=344)

W('20,2774', 0o00006, 'YFORWARD', 'EXTEND', '', '      PREPARE THE FILTER STORAGE LOCATIONS', line=346)
W('20,2775', 0o31556, '', 'DCA', 'YTMP1', '      FOR THE YAW CHANNEL', line=347)
# Page 968
W('20,2776', 0o53707, '', 'DXCH', 'TMP1', line=349)
W('20,2777', 0o00006, '', 'EXTEND', line=350)
W('20,3000', 0o31562, '', 'DCA', 'YTMP3', line=351)
W('20,3001', 0o53713, '', 'DXCH', 'TMP3', line=352)
W('20,3002', 0o00006, '', 'EXTEND', line=353)
W('20,3003', 0o31566, '', 'DCA', 'YTMP5', line=354)
W('20,3004', 0o53717, '', 'DXCH', 'TMP5', line=355)

W('20,3005', 0o03156, '', 'TCR', 'FWDFLTR', 'GO COMPUTE PRESENT OUTPUT', line=357)
# (INCLUDES VARIABLE GAIN PACKAGE)

W('20,3006', 0o00006, 'YOFFSET', 'EXTEND', line=360)
W('20,3007', 0o31610, '', 'DCA', 'YDELOFF', line=361)
W('20,3010', 0o21705, '', 'DAS', 'CMDTMP', 'NOW SCALED AT B+0 ASCREV', line=362)

W('20,3011', 0o03137, 'YACLIM', 'TCR', 'ACTLIM', 'ROUND OFF & LIMIT YAW ACTUATOR COMMAND', line=364)

W('20,3012', 0o41624, 'YOUT', 'CS', 'YCMD', 'INCREMENTAL YAW COMMAND', line=366)
W('20,3013', 0o61704, '', 'AD', 'CMDTMP', line=367)
W('20,3014', 0o26053, '', 'ADS', 'TVCYAW', 'UPDATE THE ERROR COUNTER (NO RESTART-', line=368)
# PROTECT, SINCE ERROR CNTR ZEROED)

W('20,3015', 0o35004, '', 'CAF', 'BIT12', 'BIT FOR TVCYAW COUNT RELEASE', line=371)
W('20,3016', 0o00006, '', 'EXTEND', line=372)
W('20,3017', 0o05014, '', 'WOR', 'CHAN14', line=373)

W('20,3020', 0o00006, 'YPRECOMP', 'EXTEND', '', '      PREPARE THE FILTER STORAGE FOR YAW', line=375)
W('20,3021', 0o31560, '', 'DCA', 'YTMP2', line=376)
W('20,3022', 0o53711, '', 'DXCH', 'TMP2', line=377)
W('20,3023', 0o00006, '', 'EXTEND', line=378)
W('20,3024', 0o31564, '', 'DCA', 'YTMP4', line=379)
W('20,3025', 0o53715, '', 'DXCH', 'TMP4', line=380)
W('20,3026', 0o00006, '', 'EXTEND', line=381)
W('20,3027', 0o31570, '', 'DCA', 'YTMP6', line=382)
W('20,3030', 0o53721, '', 'DXCH', 'TMP6', line=383)

W('20,3031', 0o03247, '', 'TCR', 'PRECOMP', '      TO THE FILTER FOR PRECOMPUTATION', line=385)

W('20,3032', 0o31604, 'DELBARY', 'CAE', 'DELYBAR +1', 'UPDATE YAW OFFSET-TRACKER-FILTER', line=387)
W('20,3033', 0o00006, '', 'EXTEND', line=388)
W('20,3034', 0o73500, '', 'MP', 'E(-AT)', line=389)
W('20,3035', 0o55701, '', 'TS', 'DELBRTMP +1', line=390)
W('20,3036', 0o31603, '', 'CAE', 'DELYBAR', line=391)
W('20,3037', 0o00006, '', 'EXTEND', line=392)
W('20,3040', 0o73500, '', 'MP', 'E(-AT)', line=393)
W('20,3041', 0o21701, '', 'DAS', 'DELBRTMP', line=394)
W('20,3042', 0o31704, '', 'CAE', 'CMDTMP', line=395)
W('20,3043', 0o00006, '', 'EXTEND', line=396)
W('20,3044', 0o73477, '', 'MP', '1-E(-AT)', line=397)
W('20,3045', 0o21701, '', 'DAS', 'DELBRTMP', line=398)

# Page 969
W('20,3046', 0o03050, 'YCOPYCYC', 'TCR', 'YCOPY', 'YAW COPYCYCLE', line=401)

W('20,3047', 0o15333, 'YDAPEND', 'TCF', 'RESUME', 'YAW DAP COMPLETED', line=403)

# Page 970
# TVCDAP COPYCYCLE SUBROUTINE (CALLED VIA YAW   TVCDAP OR TVC RESTART PACKAGE)

W('20,3050', 0o25644, 'YCOPY', 'INCR', 'TVCPHASE', 'RESTART-PROTECT THE COPYCYCLE.        (3)', line=408)
# NOTE POSSIBLE RE-ENTRY FROM RESTART
# PACKAGE, SHOULD A RESTART OCCUR
# DURING YAW   COPYCYCLE.

W('20,3051', 0o00006, '', 'EXTEND', line=413)
W('20,3052', 0o31707, '', 'DCA', 'TMP1', line=414)
W('20,3053', 0o53556, '', 'DXCH', 'YTMP1', line=415)
W('20,3054', 0o00006, '', 'EXTEND', line=416)
W('20,3055', 0o31711, '', 'DCA', 'TMP2', line=417)
W('20,3056', 0o53560, '', 'DXCH', 'YTMP2', line=418)
W('20,3057', 0o00006, '', 'EXTEND', line=419)
W('20,3060', 0o31713, '', 'DCA', 'TMP3', line=420)
W('20,3061', 0o53562, '', 'DXCH', 'YTMP3', line=421)
W('20,3062', 0o00006, '', 'EXTEND', line=422)
W('20,3063', 0o31715, '', 'DCA', 'TMP4', line=423)
W('20,3064', 0o53564, '', 'DXCH', 'YTMP4', line=424)
W('20,3065', 0o00006, '', 'EXTEND', line=425)
W('20,3066', 0o31717, '', 'DCA', 'TMP5', line=426)
W('20,3067', 0o53566, '', 'DXCH', 'YTMP5', line=427)
W('20,3070', 0o00006, '', 'EXTEND', line=428)
W('20,3071', 0o31721, '', 'DCA', 'TMP6', line=429)
W('20,3072', 0o53570, '', 'DXCH', 'YTMP6', line=430)

W('20,3073', 0o00006, 'YMISC', 'EXTEND', '', 'MISC....YAW-RATE-ERROR INTEGRATOR', line=432)
W('20,3074', 0o31703, '', 'DCA', 'ERRBTMP', line=433)
W('20,3075', 0o55500, '', 'TS', 'AK2', '      FOR YAW   NEEDLES, SC.AT B-1 REVS', line=434)
W('20,3076', 0o53600, '', 'DXCH', 'YERRB', line=435)

W('20,3077', 0o31704, '', 'CAE', 'CMDTMP', line=437)
W('20,3100', 0o55624, '', 'TS', 'YCMD', line=438)

W('20,3101', 0o00006, '', 'EXTEND', line=440)
W('20,3102', 0o31701, '', 'DCA', 'DELBRTMP', line=441)
W('20,3103', 0o53604, '', 'DXCH', 'DELYBAR', line=442)

W('20,3104', 0o35021, '', 'CAF', 'ZERO', 'YAW    COPYCYCLE COMPLETED', line=444)
W('20,3105', 0o55644, '', 'TS', 'TVCPHASE', '      RESET TVCPHASE', line=445)

W('20,3106', 0o00002, '', 'TC', 'Q', line=447)

# Page 971
# SUBROUTINES COMMON TO BOTH PITCH AND YAW DAPS....

# INITIALIZATION PACKAGE FOR CDURATES....

W('20,3107', 0o22016, 'DAPINIT', 'LXCH', 'BANKRUPT', 'T5 RUPT ENTRY (CALLED BY TVCINT4)', line=455)

W('20,3110', 0o37716, '', 'CAF', 'NEGONE', '      SET UP', line=457)
W('20,3111', 0o61625, '', 'AD', 'T5TVCDT', '      T5 CALL FOR PITCHDAP IN TVCDT SECS', line=458)
W('20,3112', 0o65001, '', 'AD', 'NEGMAX', '      (T5TVCDT = POSMAX - TVCDT/2 +1)', line=459)
W('20,3113', 0o61625, '', 'AD', 'T5TVCDT', line=460)
W('20,3114', 0o54030, '', 'TS', 'TIME5', line=461)
W('20,3115', 0o33473, '', 'CAF', 'PITCHT5', '      (BBCON ALREADY THERE)', line=462)
W('20,3116', 0o55312, '', 'TS', 'T5LOC', line=463)

W('20,3117', 0o30033, '', 'CAE', 'CDUY', 'READ AND STORE CDUS FOR DIFFERENTIATOR', line=465)
W('20,3120', 0o55645, '', 'TS', 'PCDUYPST', '      PAST-VALUES', line=466)
W('20,3121', 0o30034, '', 'CAE', 'CDUZ', line=467)
W('20,3122', 0o55646, '', 'TS', 'PCDUZPST', line=468)

W('20,3123', 0o15335, '', 'TCF', 'NOQRSM', line=470)

# BODY-AXIS-ERROR   INPUT LIMITER PACKAGE....

W('20,3124', 0o31702, 'ERRORLIM', 'CAE', 'ERRBTMP', 'CHECK FOR INPUT-ERROR LIMIT', line=474)
W('20,3125', 0o00006, '', 'EXTEND', '', '      CHECKS UPPER WORD ONLY', line=475)
W('20,3126', 0o75015, '', 'MP', '1/ERRLIM', line=476)
W('20,3127', 0o00006, '', 'EXTEND', line=477)
W('20,3130', 0o13136, '', 'BZF', '+6', line=478)
W('20,3131', 0o11702, '', 'CCS', 'ERRBTMP', line=479)
W('20,3132', 0o35003, '', 'CAF', 'ERRLIM', line=480)
W('20,3133', 0o13135, '', 'TCF', '+2', line=481)
W('20,3134', 0o45003, '', 'CS', 'ERRLIM', line=482)
W('20,3135', 0o55702, '', 'TS', 'ERRBTMP', 'LIMIT WRITES OVER UPPER WORD ONLY', line=483)

W('20,3136', 0o00002, '', 'TC', 'Q', line=485)

# ACTUATOR-COMMAND LIMITER PACKAGE....

W('20,3137', 0o31705, 'ACTLIM', 'CAE', 'CMDTMP +1', 'ROUND UP FOR OUTPUT', line=490)
W('20,3140', 0o60000, '', 'DOUBLE', line=491)
W('20,3141', 0o54001, '', 'TS', 'L', line=492)
W('20,3142', 0o35021, '', 'CAF', 'ZERO', line=493)
W('20,3143', 0o61704, '', 'AD', 'CMDTMP', line=494)

W('20,3144', 0o00006, '', 'EXTEND', '', 'CHECK FOR ACTUATOR COMMAND LIMIT', line=496)
W('20,3145', 0o73472, '', 'MP', '1/ACTSAT', line=497)
W('20,3146', 0o00006, '', 'EXTEND', line=498)
# Page 972
W('20,3147', 0o13155, '', 'BZF', '+6', line=500)
W('20,3150', 0o11704, '', 'CCS', 'CMDTMP', 'APPLY LIMITS', line=501)
W('20,3151', 0o33471, '', 'CAF', 'ACTSAT', line=502)
W('20,3152', 0o13154, '', 'TCF', '+2', line=503)
W('20,3153', 0o43471, '', 'CS', 'ACTSAT', line=504)
W('20,3154', 0o55704, '', 'TS', 'CMDTMP', 'LIMITS WRITE OVER CMDTMP', line=505)

W('20,3155', 0o00002, '', 'TC', 'Q', line=507)

# FILTER COMPUTATIONS FOR PRESENT OUTPUT................

W('20,3156', 0o35021, 'FWDFLTR', 'CAF', 'ZERO', line=512)
W('20,3157', 0o55615, '', 'TS', 'DAP1', line=513)
W('20,3160', 0o55617, '', 'TS', 'DAP2', line=514)
W('20,3161', 0o55621, '', 'TS', 'DAP3', line=515)
W('20,3162', 0o55704, '', 'TS', 'CMDTMP', line=516)

W('20,3163', 0o55700, '', 'TS', 'DELBRTMP', line=518)

W('20,3164', 0o31703, '1DAPCAS', 'CAE', 'ERRBTMP +1', 'FIRST DAP CASCADE', line=520)
W('20,3165', 0o00006, '', 'EXTEND', line=521)
W('20,3166', 0o71723, '', 'MP', 'N10', '      N10', line=522)
W('20,3167', 0o55616, '', 'TS', 'DAP1 +1', line=523)
W('20,3170', 0o31702, '', 'CA', 'ERRBTMP', line=524)
W('20,3171', 0o00006, '', 'EXTEND', line=525)
W('20,3172', 0o71723, '', 'MP', 'N10', '      N10', line=526)
W('20,3173', 0o21616, '', 'DAS', 'DAP1', line=527)
W('20,3174', 0o53707, '', 'DXCH', 'TMP1', line=528)
W('20,3175', 0o21616, '', 'DAS', 'DAP1', line=529)

W('20,3176', 0o31616, '2DAPCAS', 'CAE', 'DAP1 +1', 'SECOND DAP CASCADE', line=531)
W('20,3177', 0o00006, '', 'EXTEND', line=532)
W('20,3200', 0o71730, '', 'MP', 'N10 +5', '      N20', line=533)
W('20,3201', 0o55620, '', 'TS', 'DAP2 +1', line=534)
W('20,3202', 0o31615, '', 'CA', 'DAP1', line=535)
W('20,3203', 0o00006, '', 'EXTEND', line=536)
W('20,3204', 0o71730, '', 'MP', 'N10 +5', '      N20', line=537)
W('20,3205', 0o21620, '', 'DAS', 'DAP2', line=538)
W('20,3206', 0o53713, '', 'DXCH', 'TMP3', line=539)
W('20,3207', 0o21620, '', 'DAS', 'DAP2', line=540)

W('20,3210', 0o31466, '', 'CAE', 'DAPDATR1', 'TEST FOR LEM ON OR OFF', line=542)
W('20,3211', 0o75002, '', 'MASK', 'BIT14', line=543)
W('20,3212', 0o10000, '', 'CCS', 'A', line=544)
W('20,3213', 0o13220, '', 'TCF', '3DAPCAS', 'LEM ON', line=545)
W('20,3214', 0o00006, '', 'EXTEND', '', 'LEM OFF', line=546)
W('20,3215', 0o31620, '', 'DCA', 'DAP2', line=547)
W('20,3216', 0o53622, '', 'DXCH', 'DAP3', line=548)
W('20,3217', 0o13232, '', 'TCF', 'OPTVARK', line=549)

# Page 973
W('20,3220', 0o31620, '3DAPCAS', 'CAE', 'DAP2 +1', 'THIRD DAP CASCADE', line=552)
W('20,3221', 0o00006, '', 'EXTEND', line=553)
W('20,3222', 0o71735, '', 'MP', 'N10 +10D', '      N30', line=554)
W('20,3223', 0o55622, '', 'TS', 'DAP3 +1', line=555)
W('20,3224', 0o31617, '', 'CA', 'DAP2', line=556)
W('20,3225', 0o00006, '', 'EXTEND', line=557)
W('20,3226', 0o71735, '', 'MP', 'N10 +10D', '      N30', line=558)
W('20,3227', 0o21622, '', 'DAS', 'DAP3', line=559)
W('20,3230', 0o53717, '', 'DXCH', 'TMP5', line=560)
W('20,3231', 0o21622, '', 'DAS', 'DAP3', line=561)

W('20,3232', 0o41622, 'OPTVARK', 'CS', 'DAP3 +1', 'VARIABLE GAIN PACKAGE', line=563)
W('20,3233', 0o00006, '', 'EXTEND', '', '(ALSO, SIGN CHANGE IN FORWARD LOOP)', line=564)
W('20,3234', 0o71641, '', 'MP', 'VARK', 'SCALED AT 1/(8 ASCREV) OF ACTUAL VALUE', line=565)
W('20,3235', 0o55705, '', 'TS', 'CMDTMP +1', line=566)
W('20,3236', 0o41621, '', 'CS', 'DAP3', line=567)
W('20,3237', 0o00006, '', 'EXTEND', line=568)
W('20,3240', 0o71641, '', 'MP', 'VARK', line=569)
W('20,3241', 0o21705, '', 'DAS', 'CMDTMP', line=570)

W('20,3242', 0o53705, '', 'DXCH', 'CMDTMP', 'FIX UP SCALING - SCALED B+3 ASCREVS', line=572)
W('20,3243', 0o20001, '', 'DDOUBL', line=573)
W('20,3244', 0o20001, '', 'DDOUBL', line=574)
W('20,3245', 0o53705, '', 'DXCH', 'CMDTMP', '               - SCALED B+1 ASCREVS', line=575)
# NOTE - THERE IS AN INHERANT GAIN OF
# (B+1 ASCREVS) ON THE OUTPUT DACS.

W('20,3246', 0o00002, '', 'TC', 'Q', line=579)

# FILTER PRECOMPUTATIONS FOR NEXT PASS................

W('20,3247', 0o35021, 'PRECOMP', 'CAF', 'ZERO', '***** FIRST CASCADE FILTER **********', line=584)
W('20,3250', 0o55611, '', 'TS', 'TTMP1', line=585)
W('20,3251', 0o55613, '', 'TS', 'TTMP2', line=586)

W('20,3252', 0o31703, '', 'CA', 'ERRBTMP +1', 'MULTIPLY INPUT BY', line=588)
W('20,3253', 0o00006, '', 'EXTEND', line=589)
W('20,3254', 0o71724, '', 'MP', 'N10 +1', '      N11/2', line=590)
W('20,3255', 0o55612, '', 'TS', 'TTMP1 +1', line=591)
W('20,3256', 0o31702, '', 'CA', 'ERRBTMP', line=592)
W('20,3257', 0o00006, '', 'EXTEND', line=593)
W('20,3260', 0o71724, '', 'MP', 'N10 +1', '      N11/2', line=594)
W('20,3261', 0o21612, '', 'DAS', 'TTMP1', line=595)

W('20,3262', 0o41616, '', 'CS', 'DAP1 +1', 'MULTIPLY OUTPUT BY', line=597)
W('20,3263', 0o00006, '', 'EXTEND', line=598)
W('20,3264', 0o71726, '', 'MP', 'N10 +3', '      D11/2', line=599)
W('20,3265', 0o55614, '', 'TS', 'TTMP2 +1', line=600)
W('20,3266', 0o41615, '', 'CS', 'DAP1', line=601)

# Page 974
W('20,3267', 0o00006, '', 'EXTEND', line=604)
W('20,3270', 0o71726, '', 'MP', 'N10 +3', '      D11/2', line=605)
W('20,3271', 0o21614, '', 'DAS', 'TTMP2', line=606)

W('20,3272', 0o53614, '', 'DXCH', 'TTMP2', line=608)
W('20,3273', 0o21612, '', 'DAS', 'TTMP1', line=609)
W('20,3274', 0o53612, '', 'DXCH', 'TTMP1', line=610)
W('20,3275', 0o20001, '', 'DDOUBL', line=611)
W('20,3276', 0o21711, '', 'DAS', 'TMP2', line=612)

W('20,3277', 0o53711, '', 'DXCH', 'TMP2', line=614)
W('20,3300', 0o53707, '', 'DXCH', 'TMP1', line=615)

W('20,3301', 0o35021, '', 'CAF', 'ZERO', line=617)
W('20,3302', 0o55611, '', 'TS', 'TTMP1', line=618)
W('20,3303', 0o55710, '', 'TS', 'TMP2', line=619)

W('20,3304', 0o31703, '', 'CA', 'ERRBTMP +1', 'MULTIPLY INPUT BY', line=621)
W('20,3305', 0o00006, '', 'EXTEND', '', 'SECOND-ORDER NUMERATOR COEFF.', line=622)
W('20,3306', 0o71725, '', 'MP', 'N10 +2', '      N12', line=623)
W('20,3307', 0o55612, '', 'TS', 'TTMP1 +1', line=624)
W('20,3310', 0o31702, '', 'CA', 'ERRBTMP', line=625)
W('20,3311', 0o00006, '', 'EXTEND', line=626)
W('20,3312', 0o71725, '', 'MP', 'N10 +2', '      N12', line=627)
W('20,3313', 0o21612, '', 'DAS', 'TTMP1', line=628)

W('20,3314', 0o41616, '', 'CS', 'DAP1 +1', 'MULTIPLY OUTPUT BY', line=630)
W('20,3315', 0o00006, '', 'EXTEND', line=631)
W('20,3316', 0o71727, '', 'MP', 'N10 +4', '      D12', line=632)
W('20,3317', 0o55711, '', 'TS', 'TMP2 +1', line=633)
W('20,3320', 0o41615, '', 'CS', 'DAP1', line=634)
W('20,3321', 0o00006, '', 'EXTEND', line=635)
W('20,3322', 0o71727, '', 'MP', 'N10 +4', '      D12', line=636)
W('20,3323', 0o21711, '', 'DAS', 'TMP2', line=637)

W('20,3324', 0o53612, '', 'DXCH', 'TTMP1', line=639)
W('20,3325', 0o21711, '', 'DAS', 'TMP2', line=640)

W('20,3326', 0o35021, '2CASFLTR', 'CAF', 'ZERO', '*****SECOND CASCADE FILTER*****', line=642)
W('20,3327', 0o55611, '', 'TS', 'TTMP1', line=643)
W('20,3330', 0o55613, '', 'TS', 'TTMP2', line=644)

W('20,3331', 0o31616, '', 'CA', 'DAP1 +1', 'MULTIPLY INPUT BY', line=646)
W('20,3332', 0o00006, '', 'EXTEND', line=647)
W('20,3333', 0o71731, '', 'MP', 'N10 +6', '      N21/2', line=648)
W('20,3334', 0o55612, '', 'TS', 'TTMP1 +1', line=649)
W('20,3335', 0o31615, '', 'CA', 'DAP1', line=650)
W('20,3336', 0o00006, '', 'EXTEND', line=651)
W('20,3337', 0o71731, '', 'MP', 'N10 +6', '      N21/2', line=652)
# Page 975
W('20,3340', 0o21612, '', 'DAS', 'TTMP1', line=654)

W('20,3341', 0o41620, '', 'CS', 'DAP2 +1', 'MULTIPLY OUTPUT BY', line=656)
W('20,3342', 0o00006, '', 'EXTEND', line=657)
W('20,3343', 0o71733, '', 'MP', 'N10 +8D', '      D21/2', line=658)
W('20,3344', 0o55614, '', 'TS', 'TTMP2 +1', line=659)
W('20,3345', 0o41617, '', 'CS', 'DAP2', line=660)
W('20,3346', 0o00006, '', 'EXTEND', line=661)
W('20,3347', 0o71733, '', 'MP', 'N10 +8D', '      D21/2', line=662)
W('20,3350', 0o21614, '', 'DAS', 'TTMP2', line=663)

W('20,3351', 0o53614, '', 'DXCH', 'TTMP2', line=665)
W('20,3352', 0o21612, '', 'DAS', 'TTMP1', line=666)
W('20,3353', 0o53612, '', 'DXCH', 'TTMP1', line=667)
W('20,3354', 0o20001, '', 'DDOUBL', line=668)
W('20,3355', 0o21715, '', 'DAS', 'TMP4', line=669)

W('20,3356', 0o53715, '', 'DXCH', 'TMP4', line=671)
W('20,3357', 0o53713, '', 'DXCH', 'TMP3', line=672)

W('20,3360', 0o35021, '', 'CAF', 'ZERO', line=674)
W('20,3361', 0o55611, '', 'TS', 'TTMP1', line=675)
W('20,3362', 0o55714, '', 'TS', 'TMP4', line=676)

W('20,3363', 0o31616, '', 'CA', 'DAP1 +1', 'MULTIPLY INPUT BY', line=678)
W('20,3364', 0o00006, '', 'EXTEND', line=679)
W('20,3365', 0o71732, '', 'MP', 'N10 +7', '      N22', line=680)
W('20,3366', 0o55612, '', 'TS', 'TTMP1 +1', line=681)
W('20,3367', 0o31615, '', 'CA', 'DAP1', line=682)
W('20,3370', 0o00006, '', 'EXTEND', line=683)
W('20,3371', 0o71732, '', 'MP', 'N10 +7', '      N22', line=684)
W('20,3372', 0o21612, '', 'DAS', 'TTMP1', line=685)

W('20,3373', 0o41620, '', 'CS', 'DAP2 +1', 'MULTIPLY OUTPUT BY', line=687)
W('20,3374', 0o00006, '', 'EXTEND', line=688)
W('20,3375', 0o71734, '', 'MP', 'N10 +9D', '      D22', line=689)
W('20,3376', 0o55715, '', 'TS', 'TMP4 +1', line=690)
W('20,3377', 0o41617, '', 'CS', 'DAP2', line=691)
W('20,3400', 0o00006, '', 'EXTEND', line=692)
W('20,3401', 0o71734, '', 'MP', 'N10 +9D', '      D22', line=693)
W('20,3402', 0o21715, '', 'DAS', 'TMP4', line=694)

W('20,3403', 0o53612, '', 'DXCH', 'TTMP1', line=696)
W('20,3404', 0o21715, '', 'DAS', 'TMP4', line=697)

W('20,3405', 0o31466, '', 'CAE', 'DAPDATR1', 'TEST FOR LEM ON OR OFF', line=700)
W('20,3406', 0o75003, '', 'MASK', 'BIT13', line=701)
W('20,3407', 0o10000, '', 'CCS', 'A', line=702)
W('20,3410', 0o00002, '', 'TC', 'Q', 'EXIT IF LEM OFF', line=703)

# Page 976
W('20,3411', 0o35021, '3CASFLTR', 'CAF', 'ZERO', '*****THIRD CASCADE FILTER*****', line=706)
W('20,3412', 0o55611, '', 'TS', 'TTMP1', line=707)
W('20,3413', 0o55613, '', 'TS', 'TTMP2', line=708)

W('20,3414', 0o31620, '', 'CA', 'DAP2 +1', 'MULTIPLY INPUT BY (1/2)', line=710)
W('20,3415', 0o00006, '', 'EXTEND', line=711)
W('20,3416', 0o71736, '', 'MP', 'N10 +11D', '      N31/2', line=712)
W('20,3417', 0o55612, '', 'TS', 'TTMP1 +1', line=713)
W('20,3420', 0o31617, '', 'CA', 'DAP2', line=714)
W('20,3421', 0o00006, '', 'EXTEND', line=715)
W('20,3422', 0o71736, '', 'MP', 'N10 +11D', '      N31/2', line=716)
W('20,3423', 0o21612, '', 'DAS', 'TTMP1', line=717)

W('20,3424', 0o41622, '', 'CS', 'DAP3 +1', line=719)
W('20,3425', 0o00006, '', 'EXTEND', line=720)
W('20,3426', 0o71740, '', 'MP', 'N10 +13D', '      D31/2', line=721)
W('20,3427', 0o55614, '', 'TS', 'TTMP2 +1', line=722)
W('20,3430', 0o41621, '', 'CS', 'DAP3', line=723)
W('20,3431', 0o00006, '', 'EXTEND', line=724)
W('20,3432', 0o71740, '', 'MP', 'N10 +13D', '      D31/2', line=725)
W('20,3433', 0o21614, '', 'DAS', 'TTMP2', line=726)

W('20,3434', 0o53614, '', 'DXCH', 'TTMP2', line=728)
W('20,3435', 0o21612, '', 'DAS', 'TTMP1', line=729)
W('20,3436', 0o53612, '', 'DXCH', 'TTMP1', line=730)
W('20,3437', 0o20001, '', 'DDOUBL', line=731)
W('20,3440', 0o21721, '', 'DAS', 'TMP6', line=732)

W('20,3441', 0o53721, '', 'DXCH', 'TMP6', line=734)
W('20,3442', 0o53717, '', 'DXCH', 'TMP5', line=735)

W('20,3443', 0o35021, '', 'CAF', 'ZERO', line=737)
W('20,3444', 0o55611, '', 'TS', 'TTMP1', line=738)
W('20,3445', 0o55720, '', 'TS', 'TMP6', line=739)

W('20,3446', 0o31620, '', 'CA', 'DAP2 +1', 'MULTIPLY INPUT BY', line=741)
W('20,3447', 0o00006, '', 'EXTEND', line=742)
W('20,3450', 0o71737, '', 'MP', 'N10 +12D', '      N32', line=743)
W('20,3451', 0o55612, '', 'TS', 'TTMP1 +1', line=744)
W('20,3452', 0o31617, '', 'CA', 'DAP2', line=745)
W('20,3453', 0o00006, '', 'EXTEND', line=746)
W('20,3454', 0o71737, '', 'MP', 'N10 +12D', '      N32', line=747)
W('20,3455', 0o21612, '', 'DAS', 'TTMP1', line=748)

W('20,3456', 0o41622, '', 'CS', 'DAP3 +1', line=750)
W('20,3457', 0o00006, '', 'EXTEND', line=751)
W('20,3460', 0o71741, '', 'MP', 'N10 +14D', '      D32', line=752)
W('20,3461', 0o55721, '', 'TS', 'TMP6 +1', line=753)
W('20,3462', 0o41621, '', 'CS', 'DAP3', line=754)
W('20,3463', 0o00006, '', 'EXTEND', line=755)
# Page 977
W('20,3464', 0o71741, '', 'MP', 'N10 +14D', '      D32', line=757)
W('20,3465', 0o21721, '', 'DAS', 'TMP6', line=758)

W('20,3466', 0o53612, '', 'DXCH', 'TTMP1', line=760)
W('20,3467', 0o21721, '', 'DAS', 'TMP6', line=761)

W('20,3470', 0o00002, '', 'TC', 'Q', line=763)

# Page 978
# CONSTANTS FOR AUTOPILOTS

# NOTE....1 ASCREV (ACTUATOR CMD SCALING) = 85.41 ARCSEC/BIT OR 1.07975111 REVS (85.41x16384/3600/360)

# 1 SPASCREV (SPECIAL ACTUATOR CMD SCALING) = 1.04620942 REVS

W('20,3471', 0o00375, 'ACTSAT', 'DEC', '253', 'ACTUATOR LIMIT (6 DEG), SC.AT 1ASCREV', kind='data', line=772)
W('20,3472', 0o00101, '1/ACTSAT', 'DEC', '.0039525692', 'RECIPROCAL (1/253)', kind='data', line=773)

S('ERRLIM', 'equals', 0o5003, line=775)  # FILTER INPUT LIMIT....B-3 REVS (45DEG),
S('1/ERRLIM', 'equals', 0o5015, line=776)  #       SC.AT B-1 REV, AND ITS RECIPROCAL

W('20,3473', 0o02530, 'PITCHT5', 'GENADR', 'PITCHDAP', 'UPPER WORDS OF T5 2CADRS, LOWER WORDS', kind='data', line=778)
W('20,3474', 0o03107, 'DAPT5', 'GENADR', 'DAPINIT', '      (BBCON) ALREADY THERE.  ORDER IS', kind='data', line=779)
W('20,3475', 0o02732, 'YAWT5', 'GENADR', 'YAWDAP', '      REQUIRED.', kind='data', line=780)

W('20,3476', 0o00115, '1/RTLIM', 'DEC', '0.004715', '.004715(CDUDIF) = 0 IF CDUIF < 2.33 DEG', kind='data', line=782)
W('20,3477', 0o00243, '1-E(-AT)', 'OCT', '00243', 'AT = .01SEC....EITHER(1/A=4SEC, T=40MS),', kind='data', line=783)
W('20,3500', 0o37535, 'E(-AT)', 'OCT', '37535', '                   OR(1/A=8SEC, T=80MS)', kind='data', line=784)
