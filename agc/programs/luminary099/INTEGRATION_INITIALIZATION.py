"""INTEGRATION_INITIALIZATION.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/INTEGRATION_INITIALIZATION.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1205-1226 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INTEGRATION_INITIALIZATION', 'INTEGRATION_INITIALIZATION.agc', 'Luminary099', pages='1205-1226')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INTEGRATION_INITIALIZATION.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1205-1226
# Mod history:  2009-05-26 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
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

# Page 1205
# 1.0 INTRODUCTION
# ----------------
#
# FROM A USER'S POINT OF VIEW, ORBITAL INTEGRATION IS ESSENTIALLY THE SAME AS THE 278 INTEGRATION
# PROGRAM.  THE SAME ENTRANCES TO THE PROGRAM WILL BE MAINTAINED, THE SAME STALLING ROUTINE WILL BE USED AND
# OUTPUT WILL STILL BE VIA THE PUSHLIST.  THE PRIMARY DIFFERENCES TO A USER INVOLVE THE ADDED CAPABILITY OF
# TERMINATING INTEGRATION AT A SPECIFIC FINAL RADIUS AND THE DIFFERENCE IN STATE VECTOR SCALING INSIDE AND OUTSIDE
# THE LUNAR SPHERE OF INFLUENCE.
#
# IN ORDER TO MAKE THE CSM(LEM)PREC AND CSM(LEM)CONIC ENTRANCES SIMILAR TO FLIGHT 278, THE INTEGRATION PROGRAM
# WILL ITSELF SET THE FINAL RADIUS (RFINAL) TO 0 SO THAT REACHING THE DESIRED TIME ONLY WILL TERMINATE
# INTEGRATION.  THE DP REGISTER RFINAL MUST BE SET BY USERS OF INTEGRVS AND INTEGRV, AND MUST BE DONE AFTER THE
# CALL TC INTSTALL.
#
# WHEN THE LM IS ON THE LUNAR SURFACE (INDICATED BY LUNAR SURFACE FLAG SET) CALLS TO LEMCONIC, LEMPREC, AND
# INTEGRV WITH VINFLAG = 0 WILL RESULT IN THE USE OF THE PLANETARY INERTIAL ORIENTATION SUBROUTINES TO PROVIDE
# BOTH THE LM'S POSITION AND VELOCITY IN THE REFERENCE COORDINATE SYSTEM.
# THE PROGRAM WILL PROVIDE OUTPUT AS IF INTEGRATION WAS USED.  THAT IS, THE PUSHLIST WILL BE SET AS NOTED BELOW AND
# THE PERMANENT STATE VECTOR UPDATED WHEN SPECIFIED BY AN INTEGRV CALL.
#
# USERS OF INTEGRVS DESIRING INTEGRATION (INTYPFLG = 0) SHOULD NOTE THAT THE OBLATENESS PERTURBATION COMPUTATION
# IN LUNAR ORBIT IS TIME DEPENDENT.  THEREFORE, THE USER SHOULD SUPPLY AN INITIAL STATE VECTOR VALID AT SOME REAL
# TIME AND THE DESIRED TIME (TDEC1) ALSO AT SOME REAL TIME.  FOR CONIC "INTEGRATION" THE USER MAY STILL USE ZERO
# AS THE INITIAL TIME AND DELTA TIME AS THE DESIRED TIME.
#
# 2.0 GENERAL DESCRIPTION
# -----------------------
#
# THE INTEGRATION PROGRAM OPERATES AS A CLOSED INTERPRETIVE SUBROUTINE AND PERFORMS THESE FUNCTIONS --
# 1) INTEGRATES (PRECISION OR CONIC) EITHER CSM OR LM STATE VECTOR
# 2) INTEGRATES THE W-MATRIX
# 3) PERMANENT OR TEMPORARY UPDATE OF THE STATE VECTOR
#
# THERE ARE SIX ENTRANCES TO THE INTEGRATION PROGRAM.  FOUR OF THESE (CSMPREC, LEMPREC, CSMCONIC, LEMCONIC) SET
# ALL THE FLAGS REQUIRED IN THE INTEGRATION PROGRAM ITSELF TO CAUSE THE PRECISION OR CONIC INTEGRATION (KEPLER) OF
# THE LM OR CSM STATE VECTOR, AS THE NAMES SUGGEST.  ONE ENTRANCE (INTEGRVS) PERMITS THE CALLING PROGRAM TO
# PROVIDE A STATE VECTOR TO BE INTEGRATED.  THE CALLING PROGRAM MUST SET THE FLAGS INDICATING (1) PRECISION OR
# CONIC INTEGRATION, (2) IN OR OUT OF LUNAR SPHERE, (3) MIDCOURSE OR NOT, AND THE INTEGRATION PROGRAM COMPLETES
# THE FLAG SETTING TO BYPASS W-MATRIX INTEGRATION.  THE LAST ENTRANCE (INTEGRV, USED IN GENERAL BY THE
# NAVIGATION PROGRAMS) PERMITS THE CALLER TO SET FIVE FLAGS (NOT MOONFLAG OR MIDFLAG) BUT NOT TO INPUT A STATE
# VECTOR.  ANY PROGRAM WHICH CALLS INTEGRVS OR INTEGRV MUST CALL INTSTALL BEFORE IT SETS THE INTEGRATION FLAGS
# AND/OR STATE VECTOR.
#
# THREE SETS OF 42 REGISTERS AND 2 FLAGS ARE USED FOR THE STATE VECTORS.  TWO SETS, WHICH MAY NOT BE OVERLAYED, ARE
# USED FOR THE PERMANENT STATE VECTORS FOR THE CSM AND LM.  THE THIRD SET, WHICH MAY BE OVERLAYED WHEN INTEGRATION
# IS NOT BEING DONE, IS USED IN THE COMPUTATIONS.
#
# THE PERMANENT STATE VECTORS WILL BE PERIODICALLY UPDATED SO THAT THE VECTORS WILL NOT BE OLDER THAN 4 TIMESTEPS.
# THE PERMANENT STATE VECTORS WILL ALSO BE UPDATED WHENEVER THE W-MATRIX IS INTEGRATED OR WHEN A CALLER OF INTEGRV
# SETS STATEFLG (THE NAVIGATION PROGRAMS P20, P22.)
#
# Page 1206
# APPENDIX B OF THE USERS' GUIDE LISTS THE STATE VECTOR QUANTITIES.
#
# 2.1 RESTARTS
#
# PHASE CHANGES WILL BE MADE IN THE INTEGRATION PROGRAM ONLY FOR THE INTEGRV ENTRANCE (I.E., WHEN THE W-MATRIX IS
# INTEGRATED OR PERMANENT STATE VECTOR IS UPDATED.)  THE GROUP NUMBER USED WILL BE THAT FOR THE P20-25 PROGRAMS
# (I.E., GROUP2) WINCE THE INTEGRV ENTRANCE WILL ONLY BE USED BY THESE PROGRAMS.  IF A RESTART OCCURS DURING AN
# INTEGRATION OF THE STATE VECTOR ONLY, THE RECOVERY WILL BE TO THE LAST PHASE IN THE CALLING PROGRAM.  CALLING
# PROGRAMS WHICH USE THE INTEGRV OR INTEGRVS ENTRANCE OF INTEGRATION WHOULD ENSURE THAT IF PHASE CHANGING IS DONE
# THAT IT IS PRIOR TO SETTING THE INTEGRATION INPUTS IN THE PUSHLIST.
# THIS IS BECAUSE THE PUSHLIST IS LOST DURING A RESTART.
#
# 2.2 SCALING
#
# THE INTEGRATION ROUTINE WILL MAINTAIN THE PERMANENT MEMORY STATE VECTORS IN THE SCALING AND UNITS DEFINED IN
# APPENDIX B OF THE USERS GUIDE.  THE SCALING OF THE OUTPUT POSITION VECTOR DEPENDS ON THE ORIGIN OF THE COORDINATE
# SYSTEM AT THE DESIRED INTEGRATION TIME.  THE COORDINATE SYSTEM TRANSFORMATION WILL BE DONE AUTOMATICALLY ON
# MULTIPLE TIMESTEP ENCKE INTEGRATION ONLY.  THUS IT IS POSSIBLE TO HAVE OUTPUT FROM SUCCESSIVE INTEGRATIONS IN
# DIFFERENT SCALING.
# HOWEVER, RATT, VATT WILL ALWAYS BE SCALED THE SAME.
#
# 3.0 INPUT/OUTPUT
# ----------------
#
# PROGRAM INPUTS ARE THE FLAGS DESCRIBED IN APPENDIX A AND THE PERMANENT STATE VECTOR QUANTITIES DESCRIBED IN
# APPENDIX B OF THE USERS GUIDE, PLUS THE DESIRED TIME TO INTEGRATE TO IN TDEC1 (A PUSH LIST LOCATION).
# FOR INTEGRVS, THE RCV,VCV,TET OR THE TEMPORARY STATE VECTOR MUST BE SET, PLUS MOONFLAG AND MIDFLAG
#
# FOR SIMULATION THE FOLLOWING QUANTITIES MUST BE PRESET ---
# EARTH   MOON
# 29      27
# RRECTCSM(LEM)           RECTIFIED POSITION VECTOR       METERS          2       2
#
# 7       5
# VRECTCSM(LEM)           RECTIFIED VELOCITY VECTOR       M/CSEC          2       2
#
# 28      28
# TETCSM(LEM)             TIME STATE VECTOR IS VALID      CSEC            2       2
# CUSTOMARILY 0, BUT NOTE LUNAR
# ORBIT DEPENDENCE ON REAL TIME.
#
# 22      18
# DELTAVCSM(LEM)          POSITION DEVIATION              METERS          2       2
# 0 IF TCCSM(LEM) = 0
#
# 3       -1
# NUVCSM(LEM)             VELOCITY DEVIATION              M/CSEC          2       2
# 0 IF TCCSM(LEM) = 0
# Page 1207
# 29      27
# RCVSM(LEM)              CONIC POSITION                  METERS          2       2
# EQUALS RRECTCSM(LEM) IF
# TCCSM(LEM) = 0
#
# 7       5
# VCVCSM(LEM)             CONIC VELOCITY                  M/CSEC          2       2
# EQUALS VRECTCSM(LEM) IF
# TCCSM(LEM) = 0
#
# 28      28
# TCCSM(LEM)              TIME SINCE RECTIFICATION        CSECS           2       2
# CUSTOMARILY 0
#
# 1/2             17      16
# XKEPCSM(LEM)            ROOT OF KEPLER'S EQUATION       M               2       2
# 0 IF TCCSM(LEM) = 0
#
# CMOONFLG                PERMANENT FLAGS CORRESPONDING                   0       0
# CMIDFLAG                TO MOONFLAG AND MIDFLAG                         0,1     0,1
# LMOONFLG                C = CSM, L = LM                                 0       0
# LMIDFLG                                                                 0,1     0,1
#
# SURFFLAG                LUNAR SURFACE FLAG                              0,1     0,1
#
# IN ADDITION, IF (L)CMIDFLAG IS SET, THE INITIAL INPUT VALUES FOR LUNAR
# SOLAR EPHEMERIDES SUBROUTINE AND PLANETARY INERTIAL ORIENTATION SUB-
# ROUTINE MUST BE PRESET.
#
# OUTPUT
# AFTER EVERY CALL TO INTEGRATION
# EARTH   MOON
# 29      29
# 0D      RATT    POSITION                        METERS          2       2
#
# 7       7
# 6D      VATT    VELOCITY                        M/CSEC          2       2
#
# 28      28
# 12D     TAT     TIME                                            2       2
#
# 29      27
# 14D     RATT1   POSITION                        METERS          2       2
#
# 7       5
# 20D     VATT1   VELOCITY                        M/CSEC          2       2
#
# 3   2           36      30
# 26D     MU(P)   MU                              M /CS           2       2
#
# X1              MUTABLE ENTRY                                   -2      -10D
#
# X2              COORDINT
# X2              COORDINATE SYSTEM ORIGIN                        0       2
# (THIS, NOT MOONFLAG, SHOULD BE
# Page 1208
# USED TO DETERMINE ORIGIN.)
#
# IN ADDITION TO THE ABOVE, THE PERMANENT STATE VECTOR IS UPDATED WHENEVER
# STATEFLG WAS SET AND WHENEVER A W-MATRIX IS TO BE INTEGRATED.  THE PUSH
# COUNTER IS SET TO 0 AND OVERFLOW IS CLEARED BEFORE RETURNING TO THE
# CALLING PROGRAM.
#
# 4.0 CALLING SEQUENCES AND SAMPLE CODE
# -------------------------------------
#
# A) PRECISION ORBITAL INTEGRATION.  CSMPREC, LEMPREC ENTRANCES
# L-X     STORE TIME TO 96T5791T5 T 95 PUS L9ST (T4531)
# L       CALL
# L+1             CSMPREC (OR LEMPREC)
# L+2     RETURN
# INPUT                                                           28
# TDEC1 (PD 32D) TIME TO INTEGRATE TO...CENTISECONDS SCALED 2
# OUTPUT
# THE DATA LISTED IN SECTION 3.0 PLUS
# RQVV    POSITION VECTOR OF VEHICLE WITH RESPECT TO SECONDARY
# BODY... METERS B-29 ONLY IF MIDFLAG = DIM0FLAG = 1
# B) CONIC INTEGRATION.  CSMCONIC, LEMCONIC ENTRANCES
# L-X     STORE TIME IN PUSH LIST (TDEC1)
# L       CALL
# L+1             CSMCONIC (OR LEMCONIC)
# INPUT/OUTPUT
# SAME AS PRECISION INTEGRATION, EXCEPT RQVV NOT SET
# C) INTEGRATE GIVEN STATE VECTOR.  INTEGRVS ENTRANCE
# CALL
# INTSTALL
# VLOAD
# POSITION VECTOR
# STOVL           RCV
# VELOCITY VECTOR
# STODL           VCV
# TIME STATE VECTOR VALID
# STODL           TET
# FINAL RADIUS
# STORE           RFINAL
# SET(CLEAR)      SET(CLEAR)
# INTYPFLAG
# MOONFLAG
# SET(CLEAR)      DLOAD
# DESIRED TIME
# STCALL          TDEC1
# INTEGRVS
# INPUT
# RCV     POSITION VECTOR                 METERS
# VCV     VELOCITY VECTOR                 M/CSEC
# TET     TIME OF STATE VECTOR (MAY = 0)  CSEC B-28
# Page 1209
# TDEC1   TIME TO INTEGRATE TO            CSEC B-28 (PD 32D)
# (MAY BE INCREMENT IF TET=0)
# OUTPUT
# SAME AS FOR PRECISION OR CONIC INTEGRATION,
# DEPENDING ON INTYPFLG.
# D) INTEGRATE STATE VECTOR.  INTGRV ENTRANCE
# L-X     STORE TIME IN PUSH LIST (TDEC1) (MAY BE DONE AFTER CALL TO INTSTALL)
# L-8     CALL
# L-7
# L-6     SET(CLEAR)      SET(CLEAR)
# L-5                     VINTFLAG        1=CSM, 0=LM
# L-4                     INTYPFLAG       1=CONIC, 0=PRECISION
# L-3     SET(CLEAR)      SET(CLEAR)
# L-2                     DIM0FLAG        1=W-MATRIX, 0=NO W-MATRIX
# L-1                     D6OR9FLG        1=9X9, 0=6X6
# L       SET             DLOAD
# L+1                     STATEFLG        DESIRE PERMANENT UPDATE
# L+2                     FINAL RAD.      OF STATE VECTOR
# L+3     STCALL          RFINAL
# L+4                     INTEGRV
# L       CALL                            NORMAL USE -- WILL UPDATE STATE
# L+1                     INTEGRV         VECTOR IF DIM0FLAG=1. (STATEFLG IS
# L+2     RETURN                          ALWAYS RESET IN INTEGRATION AFTER
# IT USED.)
# INPUT
# TDEC1 (PD 32D) TIME TO INTEGRATE TO     CSEC B-28
# OUTPUT
# SAME AS FOR PRECISION OR CONIC INTEGRATION
# THE PROGRAM WILL SET MOONFLAG, MIDFLAG DEPENDING ON
# THE PERMANENT STATE VECTOR REPRESENTATION.

#   BANK 11
#   SETLOC INTINIT
#   BANK
#   EBANK= RRECTCSM
#   COUNT* $$/INTIN
W('13,2604', 0o05353, 'STATEINT', 'TC', 'PHASCHNG', line=275)
W('13,2605', 0o00052, '', 'OCT', '00052', kind='data', line=276)
W('13,2606', 0o35017, '', 'CAF', 'PRIO5', line=277)
W('13,2607', 0o05105, '', 'TC', 'FINDVAC', line=278)
#   EBANK= RRECTCSM
W('13,2610', 0o02613, '', '2CADR', 'STATINT1', kind='data', line=280)
W('13,2611', 0o26063, kind='data', line=280)

W('13,2612', 0o05261, '', 'TC', 'TASKOVER', line=282)
W('13,2613', 0o06037, 'STATINT1', 'TC', 'INTPRET', line=283)
W('13,2614', 0o47014, '', 'BON', 'RTB', kind='interp', line=284)
W('13,2615', 0o04712, '', '', 'QUITFLAG', 'KILL INTEGRATION UNTIL NEXT P00.', kind='operand', line=285)
W('13,2616', 0o26653, '', '', 'NOINT', kind='operand', line=286)
W('13,2617', 0o21573, '', '', 'LOADTIME', kind='operand', line=287)
W('13,2620', 0o00041, '', 'STORE', 'TDEC1', kind='interp', line=288)
# Page 1210
W('13,2621', 0o77624, '', 'CALL', kind='interp', line=290)
W('13,2622', 0o27414, '', '', 'INTSTALL', kind='operand', line=291)
W('13,2623', 0o45014, '', 'SET', 'CALL', kind='interp', line=292)
W('13,2624', 0o01076, '', '', 'NODOFLAG', kind='operand', line=293)
W('13,2625', 0o26644, '', '', 'SETIFLGS', kind='operand', line=294)
W('13,2626', 0o77650, '', 'GOTO', kind='interp', line=295)
W('13,2627', 0o26026, '', '', 'STATEUP', kind='operand', line=296)
W('13,2630', 0o00003, '600SECS', '2DEC', '60000', kind='data', line=297)
W('13,2631', 0o25140, kind='data', line=297)

W('13,2632', 0o77414, 'ENDINT', 'CLEAR', 'EXIT', kind='interp', line=299)
W('13,2633', 0o01672, '', '', 'STATEFLG', kind='operand', line=300)
W('13,2634', 0o05353, '', 'TC', 'PHASCHNG', line=301)
W('13,2635', 0o20032, '', 'OCT', '20032', kind='data', line=302)
W('13,2636', 0o00006, '', 'EXTEND', line=303)
W('13,2637', 0o32631, '', 'DCA', '600SECS', line=304)
W('13,2640', 0o05277, '', 'TC', 'LONGCALL', line=305)
#   EBANK= RRECTHIS
W('13,2641', 0o02604, '', '2CADR', 'STATEINT', kind='data', line=307)
W('13,2642', 0o26063, kind='data', line=307)

W('13,2643', 0o05155, '', 'TC', 'ENDOFJOB', line=309)
W('13,2644', 0o43014, 'SETIFLGS', 'SET', 'CLEAR', kind='interp', line=310)
W('13,2645', 0o01472, '', '', 'STATEFLG', kind='operand', line=311)
W('13,2646', 0o01673, '', '', 'INTYPFLG', kind='operand', line=312)
W('13,2647', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=313)
W('13,2650', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=314)
W('13,2651', 0o01675, '', '', 'D6OR9FLG', kind='operand', line=315)
W('13,2652', 0o77616, '', 'RVQ', kind='interp', line=316)
W('13,2653', 0o77776, 'NOINT', 'EXIT', kind='interp', line=317)
W('13,2654', 0o05353, '', 'TC', 'PHASCHNG', line=318)
W('13,2655', 0o00002, '', 'OCT', '00002', kind='data', line=319)

W('13,2656', 0o05516, '', 'TC', 'DOWNFLAG', line=321)
W('13,2657', 0o00221, '', 'ADRES', 'QUITFLAG', kind='data', line=322)
W('13,2660', 0o05155, '', 'TC', 'ENDOFJOB', line=323)

# ATOPCSM TRANSFERS RRECT TO RRECT +41 TO RRECTCSM TO RRECTCSM +41
#
# CALLING SEQUENCE
# L       CALL
# L+1             ATOPCSM
#
# NORMAL EXIT AT L+2

W('13,2661', 0o47020, 'ATOPCSM', 'STQ', 'RTB', kind='interp', line=333)
W('13,2662', 0o00051, '', '', 'S2', kind='operand', line=334)
W('13,2663', 0o26674, '', '', 'MOVEACSM', kind='operand', line=335)
W('13,2664', 0o45014, '', 'SET', 'CALL', kind='interp', line=336)
W('13,2665', 0o04063, '', '', 'CMOONFLG', kind='operand', line=337)
W('13,2666', 0o26114, '', '', 'SVDWN1', kind='operand', line=338)
W('13,2667', 0o43014, '', 'BON', 'CLRGO', kind='interp', line=339)
# Page 1211
W('13,2670', 0o00303, '', '', 'MOONFLAG', kind='operand', line=341)
W('13,2671', 0o00051, '', '', 'S2', kind='operand', line=342)
W('13,2672', 0o04223, '', '', 'CMOONFLG', kind='operand', line=343)
W('13,2673', 0o00051, '', '', 'S2', kind='operand', line=344)
W('13,2674', 0o03036, 'MOVEACSM', 'TC', 'SETBANK', line=345)
W('13,2675', 0o55500, '', 'TS', 'DIFEQCNT', 'INITIALIZE INDEX', line=346)
W('13,2676', 0o51500, '', 'INDEX', 'DIFEQCNT', line=347)
W('13,2677', 0o31502, '', 'CA', 'RRECT', line=348)
W('13,2700', 0o51500, '', 'INDEX', 'DIFEQCNT', line=349)
W('13,2701', 0o55554, '', 'TS', 'RRECTCSM', line=350)
W('13,2702', 0o11500, '', 'CCS', 'DIFEQCNT', 'IS TRANSFER COMPLETE', line=351)
W('13,2703', 0o12675, '', 'TCF', 'MOVEACSM +1', 'NO-LOOP', line=352)
W('13,2704', 0o06061, '', 'TC', 'DANZIG', 'COMPLETE -- RETURN', line=353)

# PTOACSM TRANSFERS RRECTCSM TO RRECTCSM +41 TO RRECT TO RRECT +41
#
# CALLING SEQUENCE
# L       CALL
# PTOACSM
#
# NORMAL EXIT AT L+2

W('13,2705', 0o43034, 'PTOACSM', 'RTB', 'BON', kind='interp', line=363)
W('13,2706', 0o26723, '', '', 'MOVEPCSM', kind='operand', line=364)
W('13,2707', 0o04303, '', '', 'CMOONFLG', kind='operand', line=365)
W('13,2710', 0o26716, '', '', 'SETMOON', kind='operand', line=366)
W('13,2711', 0o66214, 'CLRMOON', 'CLEAR', 'SSP', kind='interp', line=367)
W('13,2712', 0o00263, '', '', 'MOONFLAG', kind='operand', line=368)
W('13,2713', 0o02031, '', '', 'PBODY', kind='operand', line=369)
W('13,2714', 0o00000, '', '', '0', kind='operand', line=370)
W('13,2715', 0o77616, '', 'RVQ', kind='interp', line=371)
W('13,2716', 0o66214, 'SETMOON', 'SET', 'SSP', kind='interp', line=372)
W('13,2717', 0o00063, '', '', 'MOONFLAG', kind='operand', line=373)
W('13,2720', 0o02031, '', '', 'PBODY', kind='operand', line=374)
W('13,2721', 0o00002, '', '', '2', kind='operand', line=375)
W('13,2722', 0o77616, '', 'RVQ', kind='interp', line=376)
W('13,2723', 0o03036, 'MOVEPCSM', 'TC', 'SETBANK', line=377)
W('13,2724', 0o55500, '', 'TS', 'DIFEQCNT', line=378)
W('13,2725', 0o51500, '', 'INDEX', 'DIFEQCNT', line=379)
W('13,2726', 0o31554, '', 'CA', 'RRECTCSM', line=380)
W('13,2727', 0o51500, '', 'INDEX', 'DIFEQCNT', line=381)
W('13,2730', 0o55502, '', 'TS', 'RRECT', line=382)
W('13,2731', 0o11500, '', 'CCS', 'DIFEQCNT', line=383)
W('13,2732', 0o12724, '', 'TCF', 'MOVEPCSM +1', line=384)
W('13,2733', 0o06061, '', 'TC', 'DANZIG', line=385)

# ATOPLEM TRANSFERS RRECT TO RRECT +41 TO RRECTLEM TO RRECTLEM +41
W('13,2734', 0o47020, 'ATOPLEM', 'STQ', 'RTB', kind='interp', line=388)
# Page 1212
W('13,2735', 0o00051, '', '', 'S2', kind='operand', line=390)
W('13,2736', 0o26747, '', '', 'MOVEALEM', kind='operand', line=391)
W('13,2737', 0o45014, '', 'SET', 'CALL', kind='interp', line=392)
W('13,2740', 0o04064, '', '', 'LMOONFLG', kind='operand', line=393)
W('13,2741', 0o26070, '', '', 'SVDWN2', kind='operand', line=394)
W('13,2742', 0o43014, '', 'BON', 'CLRGO', kind='interp', line=395)
W('13,2743', 0o00303, '', '', 'MOONFLAG', kind='operand', line=396)
W('13,2744', 0o00051, '', '', 'S2', kind='operand', line=397)
W('13,2745', 0o04224, '', '', 'LMOONFLG', kind='operand', line=398)
W('13,2746', 0o00051, '', '', 'S2', kind='operand', line=399)
W('13,2747', 0o03036, 'MOVEALEM', 'TC', 'SETBANK', line=400)
W('13,2750', 0o55500, '', 'TS', 'DIFEQCNT', line=401)
W('13,2751', 0o51500, '', 'INDEX', 'DIFEQCNT', line=402)
W('13,2752', 0o31502, '', 'CA', 'RRECT', line=403)
W('13,2753', 0o51500, '', 'INDEX', 'DIFEQCNT', line=404)
W('13,2754', 0o55626, '', 'TS', 'RRECTLEM', line=405)
W('13,2755', 0o11500, '', 'CCS', 'DIFEQCNT', line=406)
W('13,2756', 0o12750, '', 'TCF', 'MOVEALEM +1', line=407)
W('13,2757', 0o06061, '', 'TC', 'DANZIG', line=408)

# PTOALEM TRANSFERS RRECTLEM TO RRECTLEM +41 TO RRECT TO RRECT +41

W('13,2760', 0o47014, 'PTOALEM', 'BON', 'RTB', kind='interp', line=412)
W('13,2761', 0o04307, '', '', 'SURFFLAG', kind='operand', line=413)
W('13,2762', 0o27001, '', '', 'USEPIOS', kind='operand', line=414)
W('13,2763', 0o26770, '', '', 'MOVEPLEM', kind='operand', line=415)
W('13,2764', 0o52014, '', 'BON', 'GOTO', kind='interp', line=416)
W('13,2765', 0o04304, '', '', 'LMOONFLG', kind='operand', line=417)
W('13,2766', 0o26716, '', '', 'SETMOON', kind='operand', line=418)
W('13,2767', 0o26711, '', '', 'CLRMOON', kind='operand', line=419)
W('13,2770', 0o03036, 'MOVEPLEM', 'TC', 'SETBANK', line=420)
W('13,2771', 0o55500, '', 'TS', 'DIFEQCNT', line=421)
W('13,2772', 0o51500, '', 'INDEX', 'DIFEQCNT', line=422)
W('13,2773', 0o31626, '', 'CA', 'RRECTLEM', line=423)
W('13,2774', 0o51500, '', 'INDEX', 'DIFEQCNT', line=424)
W('13,2775', 0o55502, '', 'TS', 'RRECT', line=425)
W('13,2776', 0o11500, '', 'CCS', 'DIFEQCNT', line=426)
W('13,2777', 0o12771, '', 'TCF', 'MOVEPLEM +1', line=427)
W('13,3000', 0o06061, '', 'TC', 'DANZIG', line=428)

W('13,3001', 0o77201, 'USEPIOS', 'SETPD', 'VLOAD', kind='interp', line=430)
W('13,3002', 0o00001, '', '', '0', kind='operand', line=431)
W('13,3003', 0o02023, '', '', 'RLS', kind='operand', line=432)
W('13,3004', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=433)
W('13,3005', 0o00041, '', '', 'TDEC1', kind='operand', line=434)
W('13,3006', 0o15517, '', 'STODL', 'TET', kind='interp', line=435)
W('13,3007', 0o27712, '', '', '5/8', kind='operand', line=436)
W('13,3010', 0o77624, '', 'CALL', kind='interp', line=437)
# Page 1213
W('13,3011', 0o55716, '', '', 'RP-TO-R', kind='operand', line=439)
W('13,3012', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=440)
W('13,3013', 0o24001, '', '', 'ZUNIT', kind='operand', line=441)
W('13,3014', 0o14001, '', 'STODL', '0D', kind='interp', line=442)
W('13,3015', 0o01517, '', '', 'TET', kind='operand', line=443)
W('13,3016', 0o14007, '', 'STODL', '6D', kind='interp', line=444)
W('13,3017', 0o27712, '', '', '5/8', kind='operand', line=445)
W('13,3020', 0o45014, '', 'SET', 'CALL', 'NEEDED FOR SETTING X1 ON EXIT', kind='interp', line=446)
W('13,3021', 0o00063, '', '', 'MOONFLAG', kind='operand', line=447)
W('13,3022', 0o55716, '', '', 'RP-TO-R', kind='operand', line=448)
W('13,3023', 0o74235, '', 'VXV', 'VXSC', kind='interp', line=449)
W('13,3024', 0o01535, '', '', 'RCV', kind='operand', line=450)
W('13,3025', 0o26001, '', '', 'OMEGMOON', kind='operand', line=451)
W('13,3026', 0o25543, '', 'STOVL', 'VCV', kind='interp', line=452)
W('13,3027', 0o24007, '', '', 'ZEROVEC', kind='operand', line=453)
W('13,3030', 0o01521, '', 'STORE', 'TDELTAV', kind='interp', line=454)
W('13,3031', 0o67174, '', 'AXT,2', 'SXA,2', kind='interp', line=455)
W('13,3032', 0o00002, '', '', '2', kind='operand', line=456)
W('13,3033', 0o02030, '', '', 'PBODY', kind='operand', line=457)
W('13,3034', 0o35527, '', 'STCALL', 'TNUV', kind='interp', line=458)
W('13,3035', 0o27157, '', '', 'A-PCHK', kind='operand', line=459)
W('13,3036', 0o33042, 'SETBANK', 'CAF', 'INTBANK', line=460)
W('13,3037', 0o54006, '', 'TS', 'BBANK', line=461)
W('13,3040', 0o33452, '', 'CAF', 'FORTYONE', line=462)
W('13,3041', 0o00002, '', 'TC', 'Q', line=463)
#   EBANK= RRECTCSM
W('13,3042', 0o26063, 'INTBANK', 'BBCON', 'INTEGRV', kind='data', line=465)

# SPECIAL PURPOSE ENTRIES TO ORBITAL INTEGRATION.  THESE ROUTINES PROVIDE ENTRANCES TO INTEGRATION WITH
# APPROPRIATE SWITCHES SET OR CLEARED FOR THE DESIRED INTEGRATION.
#
# CSMPREC AND LEMPREC PERFORM ORBIT INTEGRATION BY THE ENCKE METHOD TO THE TIME INDICATED IN TDEC1.
# ACCELERATIONS DUE TO OBLATENESS ARE INCLUDED.  NO W-MATRIX INT. IS DONE.
# THE PERMANENT STATE VECTOR IS NOT UPDATED.
#
# CSMCONIC AND LEMCONIC PERFORM ORBIT INTEG. BY KEPLER'S METHOD TO THE TIME INDICATED IN TDEC1.
# NO DISTURBING ACCELERATIONS ARE INCLUDED.  IN THE PROGRAM FLOW THE GIVEN
# STATE VECTOR IS RECTIFIED BEFORE SOLUTION OF KEPLER'S EQUATION.
#
# THE ROUTINES ASSUME THAT THE CSM (LEM) STATE VECTOR IN P-MEM IS VALID.
# SWITCHES SET PRIOR TO ENTRY TO THE MAIN INTEG. PROG ARE AS FOLLOWS:
# CSMPREC         CSMCONIC        LEMPREC         LEMCONIC
# VINTFLAG        SET             SET             CLEAR           CLEAR
# INTYPFLG        CLEAR           SET             CLEAR           SET
# DIM0FLAG        CLEAR           CLEAR           CLEAR           CLEAR
#
# CALLING SEQUENCE
# L-X     STORE   TDEC1
# L       CALL                    (STCALL TDEC1)
# Page 1214
# L+1             CSMPREC         (CSMCONIC, LEMPREC, LEMCONIC)
#
# NORMAL EXIT TO L+2
#
# SUBROUTINES CALLED
# INTEGRV1
# PRECOUT FOR CSMPREC AND LEMPREC
# CONICOUT FOR CSMCONIC AND LEMCONIC
#
# OUTPUT -- SEE PAGE 2 OF THIS LOG SECTION
#
# INPUT
# TDEC1           TIME TO INTEGRATE TO.  CSECS B-28

W('13,3043', 0o45020, 'CSMPREC', 'STQ', 'CALL', kind='interp', line=503)
W('13,3044', 0o00046, '', '', 'X1', kind='operand', line=504)
W('13,3045', 0o27414, '', '', 'INTSTALL', kind='operand', line=505)
W('13,3046', 0o43130, '', 'SXA,1', 'SET', kind='interp', line=506)
W('13,3047', 0o02102, '', '', 'IRETURN', kind='operand', line=507)
W('13,3050', 0o01474, '', '', 'VINTFLAG', kind='operand', line=508)

W('13,3051', 0o43014, 'IFLAGP', 'SET', 'CLEAR', kind='interp', line=510)
W('13,3052', 0o01467, '', '', 'PRECIFLG', kind='operand', line=511)
W('13,3053', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=512)
W('13,3054', 0o77614, '', 'CLRGO', kind='interp', line=513)
W('13,3055', 0o01633, '', '', 'INTYPFLG', kind='operand', line=514)
W('13,3056', 0o27136, '', '', 'INTEGRV1', kind='operand', line=515)
W('13,3057', 0o45020, 'LEMPREC', 'STQ', 'CALL', kind='interp', line=516)
W('13,3060', 0o00046, '', '', 'X1', kind='operand', line=517)
W('13,3061', 0o27414, '', '', 'INTSTALL', kind='operand', line=518)
W('13,3062', 0o43130, '', 'SXA,1', 'CLRGO', kind='interp', line=519)
W('13,3063', 0o02102, '', '', 'IRETURN', kind='operand', line=520)
W('13,3064', 0o01634, '', '', 'VINTFLAG', kind='operand', line=521)
W('13,3065', 0o27051, '', '', 'IFLAGP', kind='operand', line=522)

W('13,3066', 0o45020, 'CSMCONIC', 'STQ', 'CALL', kind='interp', line=524)
W('13,3067', 0o00046, '', '', 'X1', kind='operand', line=525)
W('13,3070', 0o27414, '', '', 'INTSTALL', kind='operand', line=526)
W('13,3071', 0o43130, '', 'SXA,1', 'SET', kind='interp', line=527)
W('13,3072', 0o02102, '', '', 'IRETURN', kind='operand', line=528)
W('13,3073', 0o01474, '', '', 'VINTFLAG', kind='operand', line=529)
W('13,3074', 0o43014, 'IFLAGC', 'CLEAR', 'SETGO', kind='interp', line=530)
W('13,3075', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=531)
W('13,3076', 0o01433, '', '', 'INTYPFLG', kind='operand', line=532)
W('13,3077', 0o27136, '', '', 'INTEGRV1', kind='operand', line=533)
W('13,3100', 0o45020, 'LEMCONIC', 'STQ', 'CALL', kind='interp', line=534)
W('13,3101', 0o00046, '', '', 'X1', kind='operand', line=535)
W('13,3102', 0o27414, '', '', 'INTSTALL', kind='operand', line=536)
W('13,3103', 0o43130, '', 'SXA,1', 'CLRGO', kind='interp', line=537)
W('13,3104', 0o02102, '', '', 'IRETURN', kind='operand', line=538)
# Page 1215
W('13,3105', 0o01634, '', '', 'VINTFLAG', kind='operand', line=540)
W('13,3106', 0o27074, '', '', 'IFLAGC', kind='operand', line=541)

W('13,3107', 0o66214, 'INTEGRVS', 'SET', 'SSP', kind='interp', line=543)
W('13,3110', 0o01467, '', '', 'PRECIFLG', kind='operand', line=544)
W('13,3111', 0o02031, '', '', 'PBODY', kind='operand', line=545)
W('13,3112', 0o00000, '', '', '0', kind='operand', line=546)
W('13,3113', 0o66214, '', 'BOF', 'SSP', kind='interp', line=547)
W('13,3114', 0o00343, '', '', 'MOONFLAG', kind='operand', line=548)
W('13,3115', 0o27120, '', '', '+3', kind='operand', line=549)
W('13,3116', 0o02031, '', '', 'PBODY', kind='operand', line=550)
W('13,3117', 0o00002, '', '', '2', kind='operand', line=551)
W('13,3120', 0o77220, '', 'STQ', 'VLOAD', kind='interp', line=552)
W('13,3121', 0o02102, '', '', 'IRETURN', kind='operand', line=553)
W('13,3122', 0o24007, '', '', 'ZEROVEC', kind='operand', line=554)
W('13,3123', 0o01521, '', 'STORE', 'TDELTAV', kind='interp', line=555)
W('13,3124', 0o35527, '', 'STCALL', 'TNUV', kind='interp', line=556)
W('13,3125', 0o23441, '', '', 'RECTIFY', kind='operand', line=557)
W('13,3126', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=558)
W('13,3127', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=559)
W('13,3130', 0o04062, '', '', 'NEWIFLG', kind='operand', line=560)
W('13,3131', 0o77614, '', 'SETGO', kind='interp', line=561)
W('13,3132', 0o04020, '', '', 'RPQFLAG', kind='operand', line=562)
W('13,3133', 0o27150, '', '', 'ALOADED', kind='operand', line=563)

# INTEGRV IS AN ENTRY TO ORBIT INTEGRATION WHICH PERMITS THE CALLER,
# NORMALLY THE NAVIGATION PROGRAM, TO SET THE INTEG. FLAGS.  THE ROUTINE
# IS ENTERED AT INTEGRV1 BY CSMPREC ET AL. AND AT ALOADED BY INTEGRVS.
# THE ROUTINE SETS UP A-MEMORY IF ENTERED AT INTEGRV,1 AND SETS THE INTEG.
# PROGRAM FOR PRECISION OR CONIC.
#
# THE CALLER MUST FIRST CALL INTSTALL TO CHECK IF INTEG. IS IN USE BEFORE
# SETTING ANY FLAGS.
#
# THE FLAGS WHICH SHOULD BE SET OR CLEARED ARE
# VINTFLAG        (IGNORED WHEN ENTERED FROM INTEGRVS)
# INTYPFLG
# DIM0FLAG
# D6OR9FLG
#
# CALLING SEQUENCE
# L-X     CALL
# L-Y             INTSTALL
# L-1     SET OR CLEAR ALL FOUR FLAGS.  ALSO CAN SET STATEFLG IF DESIRED
# AND DIM0FLAG IS CLEAR.
# L       CALL
# L+1             INTEGRV
#
# INITIALIZATION
# FLAGS AS ABOVE
# STORE TIME TO INTEGRATE TO IN TDEC1
#
# OUTPUT
# RATT    AS
# VATT          DEFINED
# Page 1216
# TAT                     BEFORE

W('13,3134', 0o77620, 'INTEGRV', 'STQ', kind='interp', line=598)
W('13,3135', 0o02102, '', '', 'IRETURN', kind='operand', line=599)
W('13,3136', 0o43014, 'INTEGRV1', 'SET', 'SET', kind='interp', line=600)
W('13,3137', 0o04060, '', '', 'RPQFLAG', kind='operand', line=601)
W('13,3140', 0o04062, '', '', 'NEWIFLG', kind='operand', line=602)
W('13,3141', 0o77731, 'INTEGRV2', 'SSP', kind='interp', line=603)
W('13,3142', 0o00053, '', '', 'QPRET', kind='operand', line=604)
W('13,3143', 0o27150, '', '', 'ALOADED', kind='operand', line=605)
W('13,3144', 0o52014, '', 'BON', 'GOTO', kind='interp', line=606)
W('13,3145', 0o01714, '', '', 'VINTFLAG', kind='operand', line=607)
W('13,3146', 0o26705, '', '', 'PTOACSM', kind='operand', line=608)
W('13,3147', 0o26760, '', '', 'PTOALEM', kind='operand', line=609)
W('13,3150', 0o77745, 'ALOADED', 'DLOAD', kind='interp', line=610)
W('13,3151', 0o00041, '', '', 'TDEC1', kind='operand', line=611)
W('13,3152', 0o01116, '', 'STORE', 'TDEC', kind='interp', line=612)
W('13,3153', 0o52014, '', 'BOFF', 'GOTO', kind='interp', line=613)
W('13,3154', 0o01753, '', '', 'INTYPFLG', kind='operand', line=614)
W('13,3155', 0o27257, '', '', 'TESTLOOP', kind='operand', line=615)
W('13,3156', 0o27243, '', '', 'RVCON', kind='operand', line=616)
W('13,3157', 0o77414, 'A-PCHK', 'BOF', 'EXIT', kind='interp', line=617)
W('13,3160', 0o01752, '', '', 'STATEFLG', kind='operand', line=618)
W('13,3161', 0o27200, '', '', 'RECTOUT', kind='operand', line=619)
W('13,3162', 0o05353, '', 'TC', 'PHASCHNG', line=620)
W('13,3163', 0o04022, '', 'OCT', '04022', kind='data', line=621)
W('13,3164', 0o05504, '', 'TC', 'UPFLAG', 'PHASE CHANGE HAS OCCURRED BETWEEN', line=622)
W('13,3165', 0o00236, '', 'ADRES', 'REINTFLG', 'INTSTALL AND INTWAKE', kind='data', line=623)
W('13,3166', 0o06037, '', 'TC', 'INTPRET', line=624)
W('13,3167', 0o77731, '', 'SSP', kind='interp', line=625)
W('13,3170', 0o00053, '', '', 'QPRET', kind='operand', line=626)
W('13,3171', 0o27176, '', '', 'PHEXIT', kind='operand', line=627)
W('13,3172', 0o52014, '', 'BON', 'GOTO', kind='interp', line=628)
W('13,3173', 0o01714, '', '', 'VINTFLAG', kind='operand', line=629)
W('13,3174', 0o26661, '', '', 'ATOPCSM', kind='operand', line=630)
W('13,3175', 0o26734, '', '', 'ATOPLEM', kind='operand', line=631)
W('13,3176', 0o77624, 'PHEXIT', 'CALL', kind='interp', line=632)
W('13,3177', 0o11244, '', '', 'GRP2PC', kind='operand', line=633)
W('13,3200', 0o45001, 'RECTOUT', 'SETPD', 'CALL', kind='interp', line=634)
W('13,3201', 0o00001, '', '', '0', kind='operand', line=635)
W('13,3202', 0o23441, '', '', 'RECTIFY', kind='operand', line=636)
W('13,3203', 0o53775, '', 'VLOAD', 'VSL*', kind='interp', line=637)
W('13,3204', 0o01503, '', '', 'RRECT', kind='operand', line=638)
W('13,3205', 0o57576, '', '', '0,2', kind='operand', line=639)
W('13,3206', 0o53715, '', 'PDVL', 'VSL*', 'RATT TO PD0', kind='interp', line=640)
W('13,3207', 0o01511, '', '', 'VRECT', kind='operand', line=641)
W('13,3210', 0o57576, '', '', '0,2', kind='operand', line=642)
W('13,3211', 0o63325, '', 'PDDL', 'PDVL', 'VATT TO PD6   TAT TO PD12', kind='interp', line=643)
W('13,3212', 0o01517, '', '', 'TET', kind='operand', line=644)
# Page 1217
W('13,3213', 0o01503, '', '', 'RRECT', kind='operand', line=646)
W('13,3214', 0o64715, '', 'PDVL', 'PDDL*', kind='interp', line=647)
W('13,3215', 0o01511, '', '', 'VRECT', kind='operand', line=648)
W('13,3216', 0o51770, '', '', 'MUEARTH,2', kind='operand', line=649)
W('13,3217', 0o76006, '', 'PUSH', 'AXT,1', kind='interp', line=650)
W('13,3220', 0o77765, '', 'DEC', '-10', kind='data', line=651)
W('13,3221', 0o76014, '', 'BON', 'AXT,1', kind='interp', line=652)
W('13,3222', 0o00303, '', '', 'MOONFLAG', kind='operand', line=653)
W('13,3223', 0o27225, '', '', '+2', kind='operand', line=654)
W('13,3224', 0o77775, '', 'DEC', '-2', kind='data', line=655)
W('13,3225', 0o40001, 'INTEXIT', 'SETPD', 'BOV', kind='interp', line=656)
W('13,3226', 0o00001, '', '', '0', kind='operand', line=657)
W('13,3227', 0o27230, '', '', '+1', kind='operand', line=658)
W('13,3230', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=659)
W('13,3231', 0o04676, '', '', 'AVEMIDSW', 'ALLOW UPDATE OF DOWNLINK STATE VECTOR', kind='operand', line=660)
W('13,3232', 0o01667, '', '', 'PRECIFLG', kind='operand', line=661)
W('13,3233', 0o77614, '', 'CLEAR', kind='interp', line=662)
W('13,3234', 0o01672, '', '', 'STATEFLG', kind='operand', line=663)
W('13,3235', 0o77535, '', 'SLOAD', 'EXIT', kind='interp', line=664)
W('13,3236', 0o02103, '', '', 'IRETURN', kind='operand', line=665)
W('13,3237', 0o30154, '', 'CA', 'MPAC', line=666)
W('13,3240', 0o50120, '', 'INDEX', 'FIXLOC', line=667)
W('13,3241', 0o54052, '', 'TS', 'QPRET', line=668)
W('13,3242', 0o03425, '', 'TC', 'INTWAKE', line=669)

# RVCON SETS UP ORBIT INTEGRATION TO DO A CONIC SOLUTION FOR POSITION AND
# VELOCITY FOR THE INTERVAL (TET-TDEC)

W('13,3243', 0o45345, 'RVCON', 'DLOAD', 'DSU', kind='interp', line=674)
W('13,3244', 0o01116, '', '', 'TDEC', kind='operand', line=675)
W('13,3245', 0o01517, '', '', 'TET', kind='operand', line=676)
W('13,3246', 0o36074, '', 'STCALL', 'TAU.', kind='interp', line=677)
W('13,3247', 0o23441, '', '', 'RECTIFY', kind='operand', line=678)
W('13,3250', 0o77624, '', 'CALL', kind='interp', line=679)
W('13,3251', 0o22376, '', '', 'KEPPREP', kind='operand', line=680)
W('13,3252', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=681)
W('13,3253', 0o01551, '', '', 'TC', kind='operand', line=682)
W('13,3254', 0o01517, '', '', 'TET', kind='operand', line=683)
W('13,3255', 0o35517, '', 'STCALL', 'TET', kind='interp', line=684)
W('13,3256', 0o27200, '', '', 'RECTOUT', kind='operand', line=685)

# Page 1218
W('13,3257', 0o43014, 'TESTLOOP', 'BOF', 'CLRGO', kind='interp', line=688)
W('13,3260', 0o04752, '', '', 'QUITFLAG', kind='operand', line=689)
W('13,3261', 0o27264, '', '', '+3', kind='operand', line=690)
W('13,3262', 0o01632, '', '', 'STATEFLG', kind='operand', line=691)
W('13,3263', 0o27225, '', '', 'INTEXIT', 'STOP INTEGRATION', kind='operand', line=692)
W('13,3264', 0o73001, '', 'SETPD', 'LXA,2', kind='interp', line=693)
W('13,3265', 0o00013, '', '', '10D', kind='operand', line=694)
W('13,3266', 0o02030, '', '', 'PBODY', kind='operand', line=695)
W('13,3267', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=696)
W('13,3270', 0o01535, '', '', 'RCV', kind='operand', line=697)
W('13,3271', 0o43006, '', 'PUSH', 'CLEAR', 'RC TO 10D', kind='interp', line=698)
W('13,3272', 0o00262, '', '', 'MIDFLAG', kind='operand', line=699)
W('13,3273', 0o50023, '', 'DSU*', 'BMN', 'MIDFLAG=0 IF R G.T. RMP', kind='interp', line=700)
W('13,3274', 0o53755, '', '', 'RME,2', kind='operand', line=701)
W('13,3275', 0o27300, '', '', '+3', kind='operand', line=702)
W('13,3276', 0o77614, '', 'SET', kind='interp', line=703)
W('13,3277', 0o00062, '', '', 'MIDFLAG', kind='operand', line=704)
W('13,3300', 0o41345, 'NORFINAL', 'DLOAD', 'DMP', kind='interp', line=705)
W('13,3301', 0o00013, '', '', '10D', kind='operand', line=706)
W('13,3302', 0o00043, '', '', '34D', kind='operand', line=707)
W('13,3303', 0o55762, '', 'SR1R', 'DDV*', kind='interp', line=708)
W('13,3304', 0o51770, '', '', 'MUEARTH,2', kind='operand', line=709)
W('13,3305', 0o41366, '', 'SQRT', 'DMP', kind='interp', line=710)
W('13,3306', 0o25752, '', '', '.3D', kind='operand', line=711)
W('13,3307', 0o40442, '', 'SR3', 'SR4', 'DT IS TRUNCATED TO A MULTIPLE', kind='interp', line=712)
W('13,3310', 0o54345, '', 'DLOAD', 'SL', kind='interp', line=713)
W('13,3311', 0o00155, '', '', 'MPAC', kind='operand', line=714)
W('13,3312', 0o20220, '', '', '15D', '      OF 128 CSECS.', kind='operand', line=715)
W('13,3313', 0o40006, '', 'PUSH', 'BOV', kind='interp', line=716)
W('13,3314', 0o27341, '', '', 'MAXDT', kind='operand', line=717)
W('13,3315', 0o50021, '', 'BDSU', 'BMN', kind='interp', line=718)
W('13,3316', 0o27413, '', '', 'DT/2MAX', kind='operand', line=719)
W('13,3317', 0o27341, '', '', 'MAXDT', kind='operand', line=720)
W('13,3320', 0o45345, 'DT/2COMP', 'DLOAD', 'DSU', kind='interp', line=721)
W('13,3321', 0o01116, '', '', 'TDEC', kind='operand', line=722)
W('13,3322', 0o01517, '', '', 'TET', kind='operand', line=723)
W('13,3323', 0o54234, '', 'RTB', 'SL', kind='interp', line=724)
W('13,3324', 0o21612, '', '', 'SGNAGREE', kind='operand', line=725)
W('13,3325', 0o20211, '', '', '8D', kind='operand', line=726)
W('13,3326', 0o02076, '', 'STORE', 'DT/2', 'B-19', kind='interp', line=727)
W('13,3327', 0o51400, '', 'BOV', 'ABS', kind='interp', line=728)
W('13,3330', 0o27345, '', '', 'GETMAXDT', kind='operand', line=729)
W('13,3331', 0o50025, '', 'DSU', 'BMN', 'IS TIME TO INTEG. TO GR THAN MAXTIME', kind='interp', line=730)
W('13,3332', 0o00015, '', '', '12D', kind='operand', line=731)
W('13,3333', 0o27351, '', '', 'POOHCHK', kind='operand', line=732)
W('13,3334', 0o75345, 'USEMAXDT', 'DLOAD', 'SIGN', kind='interp', line=733)
W('13,3335', 0o00015, '', '', '12D', kind='operand', line=734)
W('13,3336', 0o02076, '', '', 'DT/2', kind='operand', line=735)
# Page 1219
W('13,3337', 0o36076, '', 'STCALL', 'DT/2', kind='interp', line=737)
W('13,3340', 0o27351, '', '', 'POOHCHK', kind='operand', line=738)
W('13,3341', 0o65345, 'MAXDT', 'DLOAD', 'PDDL', 'EXCHANGE DT/2MAX WITH COMPUTED MAX.', kind='interp', line=739)
W('13,3342', 0o27413, '', '', 'DT/2MAX', kind='operand', line=740)
W('13,3343', 0o77650, '', 'GOTO', kind='interp', line=741)
W('13,3344', 0o27320, '', '', 'DT/2COMP', kind='operand', line=742)
W('13,3345', 0o77634, 'GETMAXDT', 'RTB', kind='interp', line=743)
W('13,3346', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=744)
W('13,3347', 0o36076, '', 'STCALL', 'DT/2', kind='interp', line=745)
W('13,3350', 0o27334, '', '', 'USEMAXDT', kind='operand', line=746)
W('13,3351', 0o51545, 'POOHCHK', 'DLOAD', 'ABS', kind='interp', line=747)
W('13,3352', 0o02076, '', '', 'DT/2', kind='operand', line=748)
W('13,3353', 0o50025, '', 'DSU', 'BMN', kind='interp', line=749)
W('13,3354', 0o27411, '', '', 'DT/2MIN', kind='operand', line=750)
W('13,3355', 0o27157, '', '', 'A-PCHK', kind='operand', line=751)
W('13,3356', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=752)
W('13,3357', 0o01012, '', '', 'MODREG', kind='operand', line=753)
W('13,3360', 0o27363, '', '', '+3', kind='operand', line=754)
W('13,3361', 0o77650, '', 'GOTO', kind='interp', line=755)
W('13,3362', 0o23252, '', '', 'TIMESTEP', kind='operand', line=756)
W('13,3363', 0o77614, '', 'BON', '', 'WAS THIS CALL VIA CSM(LEM)PREC', kind='interp', line=757)
W('13,3364', 0o01707, '', '', 'PRECIFLG', kind='operand', line=758)
W('13,3365', 0o23252, '', '', 'TIMESTEP', 'YES', kind='operand', line=759)
W('13,3366', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=760)
W('13,3367', 0o02076, '', '', 'DT/2', kind='operand', line=761)
W('13,3370', 0o00015, '', '', '12D', kind='operand', line=762)
W('13,3371', 0o43040, '', 'BMN', 'BOFCLR', kind='interp', line=763)
W('13,3372', 0o27157, '', '', 'A-PCHK', kind='operand', line=764)
W('13,3373', 0o04242, '', '', 'NEWIFLG', kind='operand', line=765)
W('13,3374', 0o23252, '', '', 'TIMESTEP', kind='operand', line=766)
W('13,3375', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=767)
W('13,3376', 0o01116, '', '', 'TDEC', kind='operand', line=768)
W('13,3377', 0o01517, '', '', 'TET', kind='operand', line=769)
W('13,3400', 0o77640, '', 'BMN', '', 'NO BACKWARD INTEGRATION', kind='interp', line=770)
W('13,3401', 0o27225, '', '', 'INTEXIT', kind='operand', line=771)
W('13,3402', 0o40525, '', 'PDDL', 'SR4', kind='interp', line=772)
W('13,3403', 0o02076, '', '', 'DT/2', 'IS 4(DT) LS (TDEC - TET)', kind='operand', line=773)
W('13,3404', 0o44322, '', 'SR2R', 'BDSU', kind='interp', line=774)
W('13,3405', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=775)
W('13,3406', 0o27225, '', '', 'INTEXIT', kind='operand', line=776)
W('13,3407', 0o23252, '', '', 'TIMESTEP', kind='operand', line=777)
W('13,3410', 0o00000, 'DT/2MIN', '2DEC', '3 B-20', kind='data', line=778)
W('13,3411', 0o01400, kind='data', line=778)

W('13,3412', 0o14152, 'DT/2MAX', '2DEC', '4000 E2 B-20', kind='data', line=780)
W('13,3413', 0o00000, kind='data', line=780)

W('13,3414', 0o77776, 'INTSTALL', 'EXIT', kind='interp', line=782)
W('13,3415', 0o30106, '', 'CA', 'RASFLAG', line=783)
W('13,3416', 0o73466, '', 'MASK', 'INTBITAB', 'IS THIS STALL AREA FREE', line=784)
W('13,3417', 0o00006, '', 'EXTEND', line=785)
W('13,3420', 0o13460, '', 'BZF', 'OKTOGRAB', 'YES', line=786)
# Page 1220
W('13,3421', 0o33465, '', 'CAF', 'WAKESTAL', line=788)
W('13,3422', 0o05133, '', 'TC', 'JOBSLEEP', line=789)
W('13,3423', 0o77776, 'INTWAKE0', 'EXIT', kind='interp', line=790)
W('13,3424', 0o13445, '', 'TCF', 'INTWAKE1', line=791)

W('13,3425', 0o40106, 'INTWAKE', 'CS', 'RASFLAG', 'IS THIS INTSTALLED ROUTINE TO BE', line=793)
W('13,3426', 0o74745, '', 'MASK', 'REINTBIT', '      RESTARTED', line=794)
W('13,3427', 0o10000, '', 'CCS', 'A', line=795)
W('13,3430', 0o03445, '', 'TC', 'INTWAKE1', 'NO', line=796)

W('13,3431', 0o50120, '', 'INDEX', 'FIXLOC', line=798)
W('13,3432', 0o30052, '', 'CA', 'QPRET', line=799)
W('13,3433', 0o55055, '', 'TS', 'TBASE2', "YES, DON'T RESTART WITH SOMEONE ELSE'S Q", line=800)

W('13,3434', 0o05353, '', 'TC', 'PHASCHNG', line=802)
W('13,3435', 0o04022, '', 'OCT', '04022', kind='data', line=803)

W('13,3436', 0o31055, '', 'CA', 'TBASE2', line=805)
W('13,3437', 0o50120, '', 'INDEX', 'FIXLOC', line=806)
W('13,3440', 0o54052, '', 'TS', 'QPRET', line=807)

W('13,3441', 0o34745, '', 'CAF', 'REINTBIT', line=809)
W('13,3442', 0o70106, '', 'MASK', 'RASFLAG', line=810)
W('13,3443', 0o00006, '', 'EXTEND', line=811)
W('13,3444', 0o13463, '', 'BZF', 'GOBAC', "DON'T INTWAKE IF WE CAME HERE VIA RESTART", line=812)

W('13,3445', 0o33465, 'INTWAKE1', 'CAF', 'WAKESTAL', line=814)
W('13,3446', 0o00004, '', 'INHINT', line=815)
W('13,3447', 0o05137, '', 'TC', 'JOBWAKE', line=816)
W('13,3450', 0o10064, '', 'CCS', 'LOCCTR', line=817)
W('13,3451', 0o13445, '', 'TCF', 'INTWAKE1', line=818)
W('13,3452', 0o00051, 'FORTYONE', 'DEC', '41', kind='data', line=819)
W('13,3453', 0o43466, '', 'CS', 'INTBITAB', line=820)
W('13,3454', 0o70106, '', 'MASK', 'RASFLAG', line=821)
W('13,3455', 0o54106, '', 'TS', 'RASFLAG', 'RELEASE STALL AREA', line=822)
W('13,3456', 0o00003, '', 'RELINT', line=823)
W('13,3457', 0o13463, '', 'TCF', 'GOBAC', line=824)
W('13,3460', 0o34736, 'OKTOGRAB', 'CAF', 'INTFLBIT', line=825)
W('13,3461', 0o00004, '', 'INHINT', line=826)
W('13,3462', 0o26106, '', 'ADS', 'RASFLAG', line=827)
W('13,3463', 0o06037, 'GOBAC', 'TC', 'INTPRET', line=828)
W('13,3464', 0o77616, '', 'RVQ', kind='interp', line=829)
W('13,3465', 0o27415, 'WAKESTAL', 'CADR', 'INTSTALL +1', kind='data', line=830)
W('13,3466', 0o20100, 'INTBITAB', 'OCT', '20100', kind='data', line=831)

# Page 1221
# AVETOMID
#
# THIS ROUTINE PERFORMS THE TRANSITION FROM A THRUSTING PHASE TO THE COAST
# PHASE BY INITIALIZING THIS VEHICLE'S PERMANENT STATE VECTOR WITH THE
# VALUES LEFT BY THE AVERAGEG ROUTINE IN RN,VN,PIPTIME.
#
# BEFORE THIS IS DONE THE W-MATRIX, IF ITS VALID (OR WFLAG OR RENDWFLT IS
# SET) IS INTEGRATED FORWARD TO PIPTIME WITH THE PRE-THRUST STATE VECTOR.
#
# IN ADDITION, THE OTHER VEHICLE IS INTEGRATED (PERMANENT) TO PIPTIME.
#
# FINALLY TRKMKCNT IS ZEROED.

#   SETLOC INTINIT
#   BANK

#   COUNT* $$/INTIN
W('13,3467', 0o43020, 'AVETOMID', 'STQ', 'BON', kind='interp', line=851)
W('13,3470', 0o02772, '', '', 'EGRESS', kind='operand', line=852)
W('13,3471', 0o02716, '', '', 'RENDWFLG', kind='operand', line=853)
W('13,3472', 0o27536, '', '', 'INT/W', 'W-MATRIX VALID, GO INTEGRATE IT', kind='operand', line=854)
W('13,3473', 0o77614, '', 'BON', kind='interp', line=855)
W('13,3474', 0o01711, '', '', 'ORBWFLAG', kind='operand', line=856)
W('13,3475', 0o27536, '', '', 'INT/W', 'W-MATRIX VALID, GO INTEGRATE IT.', kind='operand', line=857)

W('13,3476', 0o45145, 'OTHERS', 'DLOAD', 'CALL', 'GET SET FOR OTHER VEHICLE INTEGRATION', kind='interp', line=859)
W('13,3477', 0o01235, '', '', 'PIPTIME', 'DESIRED TIME', kind='operand', line=860)
W('13,3500', 0o27414, '', '', 'INTSTALL', kind='operand', line=861)
W('13,3501', 0o45014, '', 'SET', 'CALL', kind='interp', line=862)
W('13,3502', 0o01474, '', '', 'VINTFLAG', 'CM', kind='operand', line=863)
W('13,3503', 0o26644, '', '', 'SETIFLGS', 'SETS UP NONE W-MAT. PERMANENT INTEG.', kind='operand', line=864)
W('13,3504', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=865)
W('13,3505', 0o27134, '', '', 'INTEGRV', kind='operand', line=866)

W('13,3506', 0o45174, '', 'AXT,2', 'CALL', 'NOW MOVE PROPERLY SCALE RN,UN AS WELL AS', kind='interp', line=868)
W('13,3507', 0o00002, '', '', '2', 'PIPTIME TO INTEGRATION ERASABLES.', kind='operand', line=869)
W('13,3510', 0o27414, '', '', 'INTSTALL', kind='operand', line=870)
W('13,3511', 0o77014, '', 'BON', 'AXT,2', kind='interp', line=871)
W('13,3512', 0o04304, '', '', 'MOONTHIS', kind='operand', line=872)
W('13,3513', 0o27515, '', '', '+2', kind='operand', line=873)
W('13,3514', 0o00000, '', '', '0', kind='operand', line=874)
W('13,3515', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=875)
W('13,3516', 0o01221, '', '', 'RN', kind='operand', line=876)
W('13,3517', 0o57176, '', '', '0,2', kind='operand', line=877)
W('13,3520', 0o01503, '', 'STORE', 'RRECT', kind='interp', line=878)
W('13,3521', 0o15535, '', 'STODL', 'RCV', kind='interp', line=879)
W('13,3522', 0o01235, '', '', 'PIPTIME', kind='operand', line=880)
W('13,3523', 0o25517, '', 'STOVL', 'TET', kind='interp', line=881)
W('13,3524', 0o01227, '', '', 'VN', kind='operand', line=882)
# Page 1222
W('13,3525', 0o45057, '', 'VSR*', 'CALL', kind='interp', line=884)
W('13,3526', 0o57176, '', '', '0,2', kind='operand', line=885)
W('13,3527', 0o23455, '', '', 'MINIRECT', 'FINISH SETTING UP STATE VECTOR', kind='operand', line=886)
W('13,3530', 0o66234, '', 'RTB', 'SSP', kind='interp', line=887)
W('13,3531', 0o26747, '', '', 'MOVATHIS', 'PUT TEMP STATE VECTOR INTO PERMANENT', kind='operand', line=888)
W('13,3532', 0o03463, '', '', 'TRKMKCNT', kind='operand', line=889)
W('13,3533', 0o00000, '', '', '0', kind='operand', line=890)
W('13,3534', 0o77650, '', 'GOTO', kind='interp', line=891)
W('13,3535', 0o47226, '', '', 'FAZAB5', kind='operand', line=892)

W('13,3536', 0o45145, 'INT/W', 'DLOAD', 'CALL', kind='interp', line=894)
W('13,3537', 0o01235, '', '', 'PIPTIME', 'INTEGRATE W THRU BURN', kind='operand', line=895)
W('13,3540', 0o27414, '', '', 'INTSTALL', kind='operand', line=896)
W('13,3541', 0o43014, '', 'SET', 'SET', kind='interp', line=897)
W('13,3542', 0o01476, '', '', 'DIM0FLAG', 'DO W-MATRIX', kind='operand', line=898)
W('13,3543', 0o04476, '', '', 'AVEMIDSW', "SO WON'T CLOBBER RN,VN,PIPTIME", kind='operand', line=899)
W('13,3544', 0o43014, '', 'SET', 'CLEAR', kind='interp', line=900)
W('13,3545', 0o01475, '', '', 'D6OR9FLG', '9X9 FOR LM', kind='operand', line=901)
W('13,3546', 0o01674, '', '', 'VINTFLAG', 'LM', kind='operand', line=902)
W('13,3547', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=903)
W('13,3550', 0o27134, '', '', 'INTEGRV', kind='operand', line=904)
W('13,3551', 0o77650, '', 'GOTO', kind='interp', line=905)
W('13,3552', 0o27476, '', '', 'OTHERS', 'NOW GO DO THE OTHER VEHICLE', kind='operand', line=906)

# Page 1223
# MIDTOAV1
#
# THIS ROUTINE INTEGRATES (PRECISION) TO THE TIME SPECIFIED IN TDEC1.
# IF, AT THE END OF AN INTEGRATION TIME STEP, CURRENT TIME PLUS A DELTA
# TIME (SEE TIMEDELT.....BASED ON THE COMPUTATION TIME FOR ONE TIME STEP)
# IS GREATER THAN THE DESIRED TIME, ALARM 1703 IS SET AND THE INTEGRATION
# IS DONE TO THE CURRENT TIME.
# RETURN IS IN BASIC TO THE RETURN ADDRESS PLUS ONE.
#
# IF THE INTEGRATION IS FINISHED TO THE DESIRED TIME, RETURN IS IN BASIC
# TO THE RETURN ADDRESS.
#
# IN EITHER CASE, BEFORE RETURNING, THE EXTRAPOLATED STATE VECTOR IS TRANSFERRED
# FROM R,VATT TO R,VN1-PIPTIME1 IS SET TO THE FINISHING INTEGRATION
# TIME AND MPAC IS SET TO THE DELTA TIME --
# TAT MINUS CURRENT TIME

# MIDTOAV2
#
# THIS ROUTINE INTEGRATES THIS VEHICLE'S STATE VECTOR TO THE CURRENT TIME.
# NO INPUTS ARE REQUIRED OF THE CALLER.  RETURN IS IN BASIC TO THE RETURN
# ADDRESS WITH THE ABOVE TRANSFERS TO R,VN1-PIPTIME1-AND MPAC DONE

#   EBANK= IRETURN1
W('13,3553', 0o43020, 'MIDTOAV2', 'STQ', 'CLRGO', 'INTEGRATE TO PRESENT TIME PLUS TIMEDELT', kind='interp', line=933)
W('13,3554', 0o03744, '', '', 'IRETURN1', kind='operand', line=934)
W('13,3555', 0o04634, '', '', 'MID1FLAG', kind='operand', line=935)
W('13,3556', 0o27572, '', '', 'ENTMID2', kind='operand', line=936)

W('13,3557', 0o43020, 'MIDTOAV1', 'STQ', 'SET', 'INTEGRATE TO TDEC1', kind='interp', line=938)
W('13,3560', 0o03744, '', '', 'IRETURN1', kind='operand', line=939)
W('13,3561', 0o04474, '', '', 'MID1FLAG', kind='operand', line=940)
W('13,3562', 0o43234, '', 'RTB', 'DAD', 'INITIAL CHECK, IS TDEC1 IN THE FUTURE', kind='interp', line=941)
W('13,3563', 0o21573, '', '', 'LOADTIME', kind='operand', line=942)
W('13,3564', 0o27674, '', '', 'TIMEDELT', kind='operand', line=943)
W('13,3565', 0o51021, '', 'BDSU', 'BPL', kind='interp', line=944)
W('13,3566', 0o00041, '', '', 'TDEC1', kind='operand', line=945)
W('13,3567', 0o27576, '', '', 'ENTMID1', 'Y5S', kind='operand', line=946)
W('13,3570', 0o77624, '', 'CALL', kind='interp', line=947)
W('13,3571', 0o27662, '', '', 'NOTIME', 'NO, SET ALARM, SWITCH TO MIDTOAV2', kind='operand', line=948)

W('13,3572', 0o43234, 'ENTMID2', 'RTB', 'DAD', kind='interp', line=950)
W('13,3573', 0o21573, '', '', 'LOADTIME', kind='operand', line=951)
W('13,3574', 0o27674, '', '', 'TIMEDELT', kind='operand', line=952)
W('13,3575', 0o00041, '', 'STORE', 'TDEC1', kind='interp', line=953)

W('13,3576', 0o77624, 'ENTMID1', 'CALL', kind='interp', line=955)
W('13,3577', 0o27414, '', '', 'INTSTALL', kind='operand', line=956)
W('13,3600', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=957)
# Page 1224
W('13,3601', 0o01676, '', '', 'DIM0FLAG', 'NO W-MATRIX', kind='operand', line=959)
W('13,3602', 0o26066, '', '', 'THISVINT', kind='operand', line=960)
W('13,3603', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=961)
W('13,3604', 0o01673, '', '', 'INTYPFLG', kind='operand', line=962)
W('13,3605', 0o04475, '', '', 'MIDAVFLG', 'LET INTEG. KNOW THE CALL IS FOR MIDTOAV.', kind='operand', line=963)
W('13,3606', 0o77624, '', 'CALL', kind='interp', line=964)
W('13,3607', 0o27134, '', '', 'INTEGRV', 'GO INTEGRATE', kind='operand', line=965)
W('13,3610', 0o77214, '', 'CLEAR', 'VLOAD', kind='interp', line=966)
W('13,3611', 0o04675, '', '', 'MIDAVFLG', kind='operand', line=967)
W('13,3612', 0o00001, '', '', 'RATT', kind='operand', line=968)
W('13,3613', 0o27545, '', 'STOVL', 'RN1', kind='interp', line=969)
W('13,3614', 0o00007, '', '', 'VATT', kind='operand', line=970)
W('13,3615', 0o17553, '', 'STODL', 'VN1', kind='interp', line=971)
W('13,3616', 0o00015, '', '', 'TAT', kind='operand', line=972)
W('13,3617', 0o03561, '', 'STORE', 'PIPTIME1', kind='interp', line=973)
W('13,3620', 0o66134, '', 'SXA,2', 'SXA,1', kind='interp', line=974)
W('13,3621', 0o02777, '', '', 'RTX2', kind='operand', line=975)
W('13,3622', 0o02776, '', '', 'RTX1', kind='operand', line=976)
W('13,3623', 0o77776, '', 'EXIT', kind='interp', line=977)

W('13,3624', 0o00004, '', 'INHINT', line=979)
W('13,3625', 0o00006, '', 'EXTEND', line=980)
W('13,3626', 0o40025, '', 'DCS', 'TIME2', line=981)
W('13,3627', 0o20155, '', 'DAS', 'MPAC', line=982)
W('13,3630', 0o07257, '', 'TC', 'TPAGREE', line=983)

W('13,3631', 0o31744, '', 'CA', 'IRETURN1', line=985)
W('13,3632', 0o04640, '', 'TC', 'BANKJUMP', line=986)
W('13,3633', 0o47014, 'CKMID2', 'BOF', 'RTB', kind='interp', line=987)
W('13,3634', 0o04754, '', '', 'MID1FLAG', kind='operand', line=988)
W('13,3635', 0o27652, '', '', 'MID2', kind='operand', line=989)
W('13,3636', 0o21573, '', '', 'LOADTIME', kind='operand', line=990)
W('13,3637', 0o44215, '', 'DAD', 'BDSU', kind='interp', line=991)
W('13,3640', 0o27674, '', '', 'TIMEDELT', kind='operand', line=992)
W('13,3641', 0o01116, '', '', 'TDEC', kind='operand', line=993)
W('13,3642', 0o45044, '', 'BPL', 'CALL', kind='interp', line=994)
W('13,3643', 0o27257, '', '', 'TESTLOOP', 'YES', kind='operand', line=995)
W('13,3644', 0o27662, '', '', 'NOTIME', kind='operand', line=996)

W('13,3645', 0o43234, 'TIMEINC', 'RTB', 'DAD', kind='interp', line=998)
W('13,3646', 0o21573, '', '', 'LOADTIME', kind='operand', line=999)
W('13,3647', 0o27674, '', '', 'TIMEDELT', kind='operand', line=1000)
W('13,3650', 0o35116, '', 'STCALL', 'TDEC', kind='interp', line=1001)
W('13,3651', 0o27257, '', '', 'TESTLOOP', kind='operand', line=1002)

W('13,3652', 0o45345, 'MID2', 'DLOAD', 'DSU', kind='interp', line=1004)
W('13,3653', 0o01116, '', '', 'TDEC', kind='operand', line=1005)
W('13,3654', 0o01517, '', '', 'TET', kind='operand', line=1006)
W('13,3655', 0o45246, '', 'ABS', 'DSU', kind='interp', line=1007)
W('13,3656', 0o27672, '', '', '3CSECS', kind='operand', line=1008)

# Page 1225
W('13,3657', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=1011)
W('13,3660', 0o27157, '', '', 'A-PCHK', kind='operand', line=1012)
W('13,3661', 0o27645, '', '', 'TIMEINC', kind='operand', line=1013)

W('13,3662', 0o77414, 'NOTIME', 'CLEAR', 'EXIT', 'TOO LATE', kind='interp', line=1015)
W('13,3663', 0o04674, '', '', 'MID1FLAG', kind='operand', line=1016)
W('13,3664', 0o25744, '', 'INCR', 'IRETURN1', 'SET ERROR EXIT (CALLOC +2)', line=1017)
W('13,3665', 0o05567, '', 'TC', 'ALARM', 'INSUFFICIENT TIME FOR INTEGRATION --', line=1018)
W('13,3666', 0o01703, '', 'OCT', '1703', '      TIG WILL BE SLIPPED...', kind='data', line=1019)
W('13,3667', 0o06037, '', 'TC', 'INTPRET', line=1020)
W('13,3670', 0o77616, '', 'RVQ', kind='interp', line=1021)

W('13,3671', 0o00000, '3CSECS', '2DEC', '3', kind='data', line=1023)
W('13,3672', 0o00003, kind='data', line=1023)

W('13,3673', 0o00000, 'TIMEDELT', '2DEC', '2000', kind='data', line=1025)
W('13,3674', 0o03720, kind='data', line=1025)

#   BANK 27
#   SETLOC UPDATE2
#   BANK
#   EBANK= INTWAKUQ

#   COUNT* $$/INTIN

S('INTWAKUQ', 'equals', 0o1167, line=1034)  # TEMPORARY UNTIL NAME OF INTWAK1Q IS CHNG

W('04,3165', 0o00003, 'INTWAKEU', 'RELINT', line=1036)
W('04,3166', 0o00006, '', 'EXTEND', line=1037)
W('04,3167', 0o23167, '', 'QXCH', 'INTWAKUQ', 'SAVE Q FOR RETURN', line=1038)

W('04,3170', 0o06037, '', 'TC', 'INTPRET', line=1040)

W('04,3171', 0o53135, '', 'SLOAD', 'BZE', 'IS THIS A CSM/LEM STATE VECTOR UPDATE', kind='interp', line=1042)
W('04,3172', 0o01502, '', '', 'UPSVFLAG', 'REQUEST.  IF NOT GO TO INTWAKUP.', kind='operand', line=1043)
W('04,3173', 0o11232, '', '', 'INTWAKUP', kind='operand', line=1044)

W('04,3174', 0o77775, '', 'VLOAD', '', 'MOVE PRECT(6) AND VRECT(6) INTO', kind='interp', line=1046)
W('04,3175', 0o01503, '', '', 'RRECT', '      RCV(6) AND VCV(6) RESPECTIVELY.', kind='operand', line=1047)
W('04,3176', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=1048)
W('04,3177', 0o01511, '', '', 'VRECT', "NOW GO TO `RECTIFY +13D' TO", kind='operand', line=1049)
W('04,3200', 0o77624, '', 'CALL', '', 'STORE VRECT INTO VCV AND ZERO OUT', kind='interp', line=1050)
W('04,3201', 0o23456, '', '', 'RECTIFY +13D', 'TDELTAV(6),TNUV(6),TC(2), AND XKEP(2)', kind='operand', line=1051)
W('04,3202', 0o51535, '', 'SLOAD', 'ABS', "COMPARE ABSOLUTE VALUE OF `UPSVFLAG'", kind='interp', line=1052)
W('04,3203', 0o01502, '', '', 'UPSVFLAG', "TO `UPDATE MOON STATE VECTOR CODE'", kind='operand', line=1053)
W('04,3204', 0o53025, '', 'DSU', 'BZE', 'TO DETERMINE WHETHER THE STATE VECTOR TO', kind='interp', line=1054)
W('04,3205', 0o11243, '', '', 'UPMNSVCD', 'BE UPDATED IS IN THE EARTH OR LUNAR', kind='operand', line=1055)
W('04,3206', 0o11213, '', '', 'INTWAKEM', 'SPHERE OF INFLUENCE........', kind='operand', line=1056)
W('04,3207', 0o43174, '', 'AXT,2', 'CLRGO', 'EARTH SPHERE OF INFLUENCE.', kind='interp', line=1057)
W('04,3210', 0o00000, '', 'DEC', '0', kind='data', line=1058)
W('04,3211', 0o00223, '', '', 'MOONFLAG', kind='operand', line=1059)
# Page 1226
W('04,3212', 0o11216, '', '', 'INTWAKEC', kind='operand', line=1061)
W('04,3213', 0o43174, 'INTWAKEM', 'AXT,2', 'SET', 'LUNAR SPHERE OF INFLUENCE.', kind='interp', line=1062)
W('04,3214', 0o00002, '', 'DEC', '2', kind='data', line=1063)
W('04,3215', 0o00063, '', '', 'MOONFLAG', kind='operand', line=1064)
W('04,3216', 0o50135, 'INTWAKEC', 'SLOAD', 'BMN', 'COMMON CODING AFTER X2 INITIALIZED AND', kind='interp', line=1065)
# MOONFLAG SET (OR CLEARED).
W('04,3217', 0o01502, '', '', 'UPSVFLAG', 'IS THIS A REQUEST FOR A LEM OR CSM', kind='operand', line=1067)
W('04,3220', 0o11226, '', '', 'INTWAKLM', '      STATE VECTOR UPDATE......', kind='operand', line=1068)
W('04,3221', 0o77624, '', 'CALL', '', 'UPDATE CSM STATE VECTOR', kind='interp', line=1069)
W('04,3222', 0o26661, '', '', 'ATOPCSM', kind='operand', line=1070)

W('04,3223', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=1072)
W('04,3224', 0o01671, '', '', 'ORBWFLAG', kind='operand', line=1073)
W('04,3225', 0o11230, '', '', 'INTWAKEX', kind='operand', line=1074)

W('04,3226', 0o77624, 'INTWAKLM', 'CALL', '', 'UPDATE LM STATE VECTOR', kind='interp', line=1076)
W('04,3227', 0o26734, '', '', 'ATOPLEM', kind='operand', line=1077)

W('04,3230', 0o77614, 'INTWAKEX', 'CLEAR', kind='interp', line=1079)
W('04,3231', 0o02676, '', '', 'RENDWFLG', kind='operand', line=1080)

W('04,3232', 0o45131, 'INTWAKUP', 'SSP', 'CALL', "REMOVE `UPDATE STATE VECTOR INDICATOR'", kind='interp', line=1082)
W('04,3233', 0o01502, '', '', 'UPSVFLAG', kind='operand', line=1083)
W('04,3234', 0o00000, '', '', '0', kind='operand', line=1084)
W('04,3235', 0o27423, '', '', 'INTWAKE0', "RELEASE `GRAB' OF ORBIT INTEG.", kind='operand', line=1085)
W('04,3236', 0o77776, '', 'EXIT', kind='interp', line=1086)

W('04,3237', 0o05353, '', 'TC', 'PHASCHNG', line=1088)
W('04,3240', 0o04026, '', 'OCT', '04026', kind='data', line=1089)
W('04,3241', 0o01167, '', 'TC', 'INTWAKUQ', line=1090)

W('04,3242', 0o00002, 'UPMNSVCD', 'OCT', '2', kind='data', line=1092)
W('04,3243', 0o00000, '', 'OCT', '0', kind='data', line=1093)

W('04,3244', 0o77420, 'GRP2PC', 'STQ', 'EXIT', kind='interp', line=1095)
W('04,3245', 0o02711, '', '', 'GRP2SVQ', kind='operand', line=1096)
W('04,3246', 0o05353, '', 'TC', 'PHASCHNG', line=1097)
W('04,3247', 0o04022, '', 'OCT', '04022', kind='data', line=1098)
W('04,3250', 0o06037, '', 'TC', 'INTPRET', line=1099)
W('04,3251', 0o77650, '', 'GOTO', kind='interp', line=1100)
W('04,3252', 0o02711, '', '', 'GRP2SVQ', kind='operand', line=1101)
