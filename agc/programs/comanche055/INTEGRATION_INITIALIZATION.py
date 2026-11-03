"""INTEGRATION_INITIALIZATION.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/INTEGRATION_INITIALIZATION.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1309-1333 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INTEGRATION_INITIALIZATION', 'INTEGRATION_INITIALIZATION.agc', 'Comanche055', pages='1309-1333')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INTEGRATION_INITIALIZATION.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1309-1333
# Mod history:  2009-05-15 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
# 2009-05-20 RSB  Corrections:  fixed an interpreter instruction,
# fixed a SETLOC.
# 2009-05-23 RSB  In SETCOAST, corrected MOONTHIS to AMOONFLG.
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

# Page 1309
# 1.0 INTRODUCTION
# ----------------
#
# FROM A USER'S POINT OF VIEW, ORBITAL INTEGRATION IS ESSENTIALLY THE SAME AS THE 278 INTEGRATION
# PROGRAM.  THE SAME ENTRANCES TO THE PROGRAM WILL BE MAINTAINED, THE SAME STALLING ROUTINE WILL BE USED AND
# OUTPUT WILL STILL BE VIA THE PUSHLIST.  THE PRIMARY DIFFERENCES TO A USER INVOLVE THE ADDED CAPABILITY OF
# TERMINATING INTEGRATION AT A SPECIFIC FINAL RADIUS AND THE DIFFERENCE IN STATE VECTOR SCALING INSIDE AND OUT-
# SIDE THE LUNAR SPHERE OF INFLUENCE.
#
# IN ORDER TO MAKE THE CSM(LEM)PREC AND CSM(LEM)CONIC ENTRANCES SIMILAR TO FLIGHT 278, THE INTEGRATION PROGRAM
# WILL ITSELF SET THE FINAL RADIUS (RFINAL) TO 0 SO THAT REACHING THE DESIRED TIME ONLY WILL TERMINATE
# INTEGRATION.  THE DP REGISTER RFINAL MUST BE SET BY USERS OF INTEGRVS AND INTEGRV, AND MUST BE DONE AFTER THE
# CALL TO INTSTALL.
#
# WHEN THE LM IS ON THE LUNAR SURFACE (INDICATED BY LUNAR SURFACE FLAG SET) CALLS TO LEMCONIC, LEMPREC, AND
# INTEGRV WITH VINFLAG = 0 WILL RESULT IN THE USE OF THE PLANETARY INERTIAL ORIENTATION SUBROUTINES TO PROVIDE
# BOTH THE LMS POSITION AND VELOCITY IN THE REFERENCE COORDINATE SYSTEM.
# THE PROGRAM WILL PROVIDE OUTPUT AS IF INTEGRATION WAS USED.  THAT IS, THE PUSHLIST WILL BE SET AS NOTED BELOW AND
# THE PERMANENT STATE VECTOR UPDATED WHEN SPECIFIED BY AN INTEGRV CALL.
#
# USERS OF INTEGRVS DESIRING INTEGRATION (INTYPFLG = 0) SHOULD NOTE THAT THE OBLATENESS PERTURBATION COMPUTATION
# IN LUNAR ORBIT IS TIME DEPENDENT.  THEREFORE, THE USER SHOULD SUPPLY AN INITIAL STATE VECTOR VALID AT SOME REAL
# TIME AND THE DESIRED TIME (TDEC1) ALSO AT SOME REAL TIME.  FOR CONIC ,,INTEGRATION,, THE USER MAY STILL USE ZERO
# AS THE INITIAL TIME AND DELTA TIME AS THE DESIRED TIME.
#
# 2.0 CENTRAL DESCRIPTION
# -----------------------
#
# THE INTEGRATION PROGRAM OPERATES AS A CLOSED INTERPRETIVE SUBROUTINE AND PERFORMS THESE FUNCTIONS---
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
# Page 1310
# APPENDIX B OF THE USERS GUIDE LISTS THE STATE VECTOR QUANTITIES.
#
# 2.1 RESTARTS
#
# PHASE CHANGES WILL BE MADE IN THE INTEGRATION PROGRAM ONLY FOR THE INTEGRV ENTRANCE (I.E., WHEN THE W-MATRIX IS
# INTEGRATED OR PERMANENT STATE VECTOR IS UPDATED.)  THE GROUP NUMBER USED WILL BE THAT FOR THE P20-25 PROGRAMS
# (I.E., GROUP2) SINCE THE INTEGRV ENTRANCE WILL ONLY BE USED BY THESE PROGRAMS.  IF A RESTART OCCURS DURING AN
# INTEGRATION OF THE STATE VECTOR ONLY, THE RECOVERY WILL BE TO THE LAST PHASE IN THE CALLING PROGRAM.  CALLING
# PROGRAMS WHICH USE THE INTEGRV OR INTEGRVS ENTRANCE OF INTEGRATION SHOULD ENSURE THAT IF PHASE CHANGING IS DONE
# THAT IT IS PRIOR TO SETTING THE INTEGRATION INPUTS IN THE PUSHLIST.
# THIS IS BECAUSE THE PUSHLIST IS LOST DURING A RESTART.
#
# 2.2 SCALING
#
# THE INTEGRATION ROUTINE WILL MAINTAIN THE PERMANENT MEMORY STATE VECTORS IN THE SCALING AND UNITS DEFINED IN
# APPENDIX B OF THE USERS GUIDE.  THE SCALING OF THE OUTPUT POSITION VECTORDEPENDS ON THE ORIGIN OF THE COORDINATE
# SYSTEM AT THE DESIRED INTEGRATION TIME.  THE COORDINATE SYSTEM TRANSFORMATION WILL BE DONE AUTOMATICALLY ON
# MULTIPLE TIMESTEP ENCKE INTEGRATION ONLY.  THUS IT IS POSSIBLE TO HAVE OUTPUT FROM SUCCESSIVE INTEGRATIONS IN
# DIFFERENT SCALING.
# HOWEVER, RATT, VATT WILL ALWAYS BE SCALED THE SAME.
#
# 3.0 INPUT/OUTPUT
# ----------------
#
# PROGRAM INPUTS ARE THE FLAGS DESCRIBED IN APPENDIX A AND THE PERMANENT STATE VECTOR QUANTITIES DESCRIBED IN AP-
# PENDIX B OF THE USERS GUIDE, PLUS THE DESIRED TIME TO INTEGRATE TO IN TDEC1 (A PUSH LIST LOCATION).
# FOR INTEGRVS, THE RCV,VCV, TET OR THE TEMPORARY STATE VECTOR MUST BE SET, PLUS MOONFLAG AND MIDFLAG
#
# FOR SIMULATION THE FOLLOWING QUANTITIES MUST BE PRESET ---
#
# EARTH   MOON
# 29      27
# RRECTCSM(LEM)         - RECTIFIED POSITION VECTOR       METERS          2       2
#
# 7       5
# VRECTCSM(LEM)         - RECTIFIED VELOCITY VECTOR       M/CSEC          2       2
#
# 28      28
# TETCSM(LEM)           - TIME STATE VECTOR IS VALID      CSEC            2       2
# CUSTOMARILY 0, BUT NOTE LUNAR
# ORBIT DEPENDENCE ON REAL TIME.
#
# 22      18
# DELTAVCSM(LEM)        - POSITION DEVIATION              METERS          2       2
# 0 IF TCCSM(LEM) = 0
#
# 3       -1
# NUVCSM(LEM)           - VELOCITY DEVIATION              M/CSEC          2       2
# 0 IF TCCSM(LEM) = 0
# Page 1311
# 29      27
# RCVCSM(LEM)           - CONIC POSITION                  METERS          2       2
# EQUALS RRECTCSM(LEM) IF
# TCCSM(LEM) = 0
#
# 7       5
# VCVCSM(LEM)           - CONIC VELOCITY                  M/CSEC          2       2
# EQUALS VRECTCSM(LEM) IF
# TCCSM(LEM) = 0
#
# 28      28
# TCCSM(LEM)            - TIME SINCE RECTIFICATION        CSECS           2       2
# CUSTOMARILY 0
#
# 1/2             17      16
# XKEPCSM(LEM)          - RDOT OF KEPLER'S EQUATION       M               2       2
# 0 IF TCCSM(LEM) = 0
#
# CMOONFLG              - PERMANENT FLAGS CORRESPONDING                   0       0
# CMIDFLAG                TO MOONFLAG AND MIDFLAG                         0,1     0,1
# LMOONFLG                C = CSM, L = LM                                 0       0
# LMIDFLG                                                                 0,1     0,1
#
# SURFFLAG              - LUNAR SURFACE FLAG                              0,1     0,1
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
# 7       7
# 6D      VATT    VELOCITY                        M/CSEC          2       2
# 28      28
# 12D      TAT     TIME                                            2       2
# 29      27
# 14D      RATT1   POSITION                        METERS          2       2
# 7       5
# 20D      VATT1   VELOCITY                        M/CSEC          2       2
# 3   2           36      30
# 26D      MU(P)   MU                              M /CS           2       2
#
# X1               MUTABLE ENTRY                                   -2      -10D
#
# X2               COORDINT
# X2               COORDINATE SYSTEM ORIGEN                        0       2
# (THIS, NOT MOONFLAG, SHOULD BE
# Page 1312
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
# A) PRECISION ORBITAL INTEGRATION.  CSMPREC,LEMPREC ENTRANCES
# L-X     STORE TIME TO 96T5791T5 T  95  PUS  L9ST (T4531)
# L       CALL
# L+1             CSMPREC (OR LEMPREC)
# L+2     RETURN
# INPUT                                                           28
# TDEC1 (PD 32D) TIME TO INTEGRATE TO...CENTISECONDS SCALED 2
# OUTPUT
# THE DATA LISTED IN SECTION 3.0 PLUS
# RQVV    POSITION VECTOR OF VEHICLE WITH RESPECT TO SECONDARY
# BODY... METERS B-29 ONLY IF MIDFLAG = DIMOFLAG = 1
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
# TET     TIME OF STATE VECTOR(MAY = 0)   CSEC B-28
# Page 1313
# TDEC1   TIME TO INTEGRATE TO            CSEC B-28 (PD 32D)
# (MAY BE INCREMENT IF TET=0)
# OUTPUT
# SAME AS FOR PRECISION OR CONIC INTEGRATION,
# DEPENDING ON INTYPFLG.
# D) INTEGRATE STATE VECTOR.INTGRV ENTRANCE
# L-X     STORE TIME IN PUSH LIST (TDEC1)(MAY BE DONE AFTER CALL TO INTSTALL)
# L-8     CALL
# L-7
# L-6     SET(CLEAR)      SET(CLEAR)
# L-5                     VINTFLAG        1=CSM, 0=LM
# L-4                     INTYPFLAG       1=CONIC, 0=PRECISION
# L-3     SET(CLEAR)      SET(CLEAR)
# L-2                     DIMOFLAG        1=W-MATRIX, 0=NO W-MATRIX
# L-1                     D6OR9FLG        1=9X9, 0=6X6
# L       SET             DLOAD
# L+1                     STATEFLG        DESIRE PERMANENT UPDATE
# L+2                     FINAL RAD. OF STATE VECTOR
# L+3     STCALL          RFINAL
# L+4                     INTEGRV
# L       CALL                            NORMAL USE-- WILL UPDATE STATE
# L+1                     INTEGRV         VECTOR IF DIMOFLAG=1.(STATEFLG IS
# L+2     RETURN                          ALWAYS RESET IN INTEGRATION AFTER
# IT IS USED.)
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
#   COUNT 13/INTIN

W('13,2627', 0o05412, 'STATEINT', 'TC', 'PHASCHNG', line=275)
W('13,2630', 0o00052, '', 'OCT', '00052', kind='data', line=276)
W('13,2631', 0o35061, '', 'CAF', 'PRIO5', line=277)
W('13,2632', 0o05147, '', 'TC', 'FINDVAC', line=278)
#   EBANK= RRECTCSM
W('13,2633', 0o02636, '', '2CADR', 'STATINT1', kind='data', line=280)
W('13,2634', 0o26063, kind='data', line=280)

W('13,2635', 0o05324, '', 'TC', 'TASKOVER', line=282)
W('13,2636', 0o06006, 'STATINT1', 'TC', 'INTPRET', line=283)
W('13,2637', 0o47014, '', 'BON', 'RTB', kind='interp', line=284)
W('13,2640', 0o04712, '', '', 'QUITFLAG', kind='operand', line=285)
W('13,2641', 0o26677, '', '', 'NOINT', 'NO STATEINT IF V96', kind='operand', line=286)
W('13,2642', 0o45510, '', '', 'LOADTIME', kind='operand', line=287)
# Page 1314
W('13,2643', 0o00041, '', 'STORE', 'TDEC1', kind='interp', line=289)
W('13,2644', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=290)
W('13,2645', 0o04274, '', '', 'V96ONFLG', kind='operand', line=291)
W('13,2646', 0o27442, '', '', 'INTSTALL', kind='operand', line=292)
W('13,2647', 0o45014, '', 'SET', 'CALL', kind='interp', line=293)
W('13,2650', 0o01076, '', '', 'NODOFLAG', kind='operand', line=294)
W('13,2651', 0o26670, '', '', 'SETIFLGS', kind='operand', line=295)
W('13,2652', 0o77650, '', 'GOTO', kind='interp', line=296)
W('13,2653', 0o26000, '', '', 'STATEUP', kind='operand', line=297)
W('13,2654', 0o00003, '600SECS', '2DEC', '60000', kind='data', line=298)
W('13,2655', 0o25140, kind='data', line=298)

W('13,2656', 0o77414, 'ENDINT', 'CLEAR', 'EXIT', kind='interp', line=300)
W('13,2657', 0o01672, '', '', 'STATEFLG', kind='operand', line=301)
W('13,2660', 0o05412, '', 'TC', 'PHASCHNG', line=302)
W('13,2661', 0o20032, '', 'OCT', '20032', kind='data', line=303)
W('13,2662', 0o00006, '', 'EXTEND', line=304)
W('13,2663', 0o32655, '', 'DCA', '600SECS', line=305)
W('13,2664', 0o05342, '', 'TC', 'LONGCALL', line=306)
#   EBANK= RRECTHIS
W('13,2665', 0o02627, '', '2CADR', 'STATEINT', kind='data', line=308)
W('13,2666', 0o26063, kind='data', line=308)

W('13,2667', 0o05217, '', 'TC', 'ENDOFJOB', line=310)
W('13,2670', 0o43014, 'SETIFLGS', 'SET', 'CLEAR', kind='interp', line=311)
W('13,2671', 0o01472, '', '', 'STATEFLG', kind='operand', line=312)
W('13,2672', 0o01673, '', '', 'INTYPFLG', kind='operand', line=313)
W('13,2673', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=314)
W('13,2674', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=315)
W('13,2675', 0o01675, '', '', 'D6OR9FLG', kind='operand', line=316)
W('13,2676', 0o77616, '', 'RVQ', kind='interp', line=317)
W('13,2677', 0o77776, 'NOINT', 'EXIT', kind='interp', line=318)
W('13,2700', 0o05412, '', 'TC', 'PHASCHNG', line=319)
W('13,2701', 0o00002, '', 'OCT', '2', kind='data', line=320)

W('13,2702', 0o05560, '', 'TC', 'DOWNFLAG', line=322)
W('13,2703', 0o00221, '', 'ADRES', 'QUITFLAG', kind='data', line=323)

W('13,2704', 0o05217, '', 'TC', 'ENDOFJOB', line=325)

# ATOPCSM TRANSFERS RRECT TO RRECT +41 TO RRECTCSM TO RRECTCSM +41
#
# CALLING SEQUENCE
# L       CALL
# L+1             ATOPCSM
#
# NORMAL EXIT AT L+2

W('13,2705', 0o47020, 'ATOPCSM', 'STQ', 'RTB', kind='interp', line=335)
W('13,2706', 0o00051, '', '', 'S2', kind='operand', line=336)
W('13,2707', 0o26720, '', '', 'MOVEACSM', kind='operand', line=337)
W('13,2710', 0o45014, '', 'SET', 'CALL', kind='interp', line=338)
# Page 1315
W('13,2711', 0o04063, '', '', 'CMOONFLG', kind='operand', line=340)
W('13,2712', 0o20237, '', '', 'SVDWN1', kind='operand', line=341)
W('13,2713', 0o43014, '', 'BON', 'CLRGO', kind='interp', line=342)
W('13,2714', 0o00303, '', '', 'MOONFLAG', kind='operand', line=343)
W('13,2715', 0o00051, '', '', 'S2', kind='operand', line=344)
W('13,2716', 0o04223, '', '', 'CMOONFLG', kind='operand', line=345)
W('13,2717', 0o00051, '', '', 'S2', kind='operand', line=346)
W('13,2720', 0o03064, 'MOVEACSM', 'TC', 'SETBANK', line=347)
W('13,2721', 0o55500, '', 'TS', 'DIFEQCNT', 'INITIALIZE INDEX', line=348)
W('13,2722', 0o51500, '', 'INDEX', 'DIFEQCNT', line=349)
W('13,2723', 0o31502, '', 'CA', 'RRECT', line=350)
W('13,2724', 0o51500, '', 'INDEX', 'DIFEQCNT', line=351)
W('13,2725', 0o55554, '', 'TS', 'RRECTCSM', line=352)
W('13,2726', 0o11500, '', 'CCS', 'DIFEQCNT', 'IS TRANSFER COMPLETE', line=353)
W('13,2727', 0o12721, '', 'TCF', 'MOVEACSM +1', 'NO-LOOP', line=354)
W('13,2730', 0o06030, '', 'TC', 'DANZIG', 'COMPLETE- RETURN', line=355)

# PTOACSM TRANSFERS RRECTCSM TO RRECTCSM +41 TO RRECT TO RRECT +41
#
# CALLING SEQUENCE
# L       CALL
# PTOACSM
#
# NORMAL EXIT AT L+2

W('13,2731', 0o43034, 'PTOACSM', 'RTB', 'BON', kind='interp', line=365)
W('13,2732', 0o26747, '', '', 'MOVEPCSM', kind='operand', line=366)
W('13,2733', 0o04303, '', '', 'CMOONFLG', kind='operand', line=367)
W('13,2734', 0o26742, '', '', 'SETMOON', kind='operand', line=368)
W('13,2735', 0o66214, 'CLRMOON', 'CLEAR', 'SSP', kind='interp', line=369)
W('13,2736', 0o00263, '', '', 'MOONFLAG', kind='operand', line=370)
W('13,2737', 0o02151, '', '', 'PBODY', kind='operand', line=371)
W('13,2740', 0o00000, '', '', '0', kind='operand', line=372)
W('13,2741', 0o77616, '', 'RVQ', kind='interp', line=373)
W('13,2742', 0o66214, 'SETMOON', 'SET', 'SSP', kind='interp', line=374)
W('13,2743', 0o00063, '', '', 'MOONFLAG', kind='operand', line=375)
W('13,2744', 0o02151, '', '', 'PBODY', kind='operand', line=376)
W('13,2745', 0o00002, '', '', '2', kind='operand', line=377)
W('13,2746', 0o77616, '', 'RVQ', kind='interp', line=378)
W('13,2747', 0o03064, 'MOVEPCSM', 'TC', 'SETBANK', line=379)
W('13,2750', 0o55500, '', 'TS', 'DIFEQCNT', line=380)
W('13,2751', 0o51500, '', 'INDEX', 'DIFEQCNT', line=381)
W('13,2752', 0o31554, '', 'CA', 'RRECTCSM', line=382)
W('13,2753', 0o51500, '', 'INDEX', 'DIFEQCNT', line=383)
W('13,2754', 0o55502, '', 'TS', 'RRECT', line=384)
W('13,2755', 0o11500, '', 'CCS', 'DIFEQCNT', line=385)
W('13,2756', 0o12750, '', 'TCF', 'MOVEPCSM +1', line=386)
W('13,2757', 0o06030, '', 'TC', 'DANZIG', line=387)

# Page 1316
# ATOPLEM TRANSFERS RRECT TO RRECT +41 TO RRECTLEM TO RRECTLEM +41
W('13,2760', 0o47020, 'ATOPLEM', 'STQ', 'RTB', kind='interp', line=391)
W('13,2761', 0o00051, '', '', 'S2', kind='operand', line=392)
W('13,2762', 0o26773, '', '', 'MOVEALEM', kind='operand', line=393)
W('13,2763', 0o45014, '', 'SET', 'CALL', kind='interp', line=394)
W('13,2764', 0o04064, '', '', 'LMOONFLG', kind='operand', line=395)
W('13,2765', 0o20263, '', '', 'SVDWN2', kind='operand', line=396)
W('13,2766', 0o43014, '', 'BON', 'CLRGO', kind='interp', line=397)
W('13,2767', 0o00303, '', '', 'MOONFLAG', kind='operand', line=398)
W('13,2770', 0o00051, '', '', 'S2', kind='operand', line=399)
W('13,2771', 0o04224, '', '', 'LMOONFLG', kind='operand', line=400)
W('13,2772', 0o00051, '', '', 'S2', kind='operand', line=401)
W('13,2773', 0o03064, 'MOVEALEM', 'TC', 'SETBANK', line=402)
W('13,2774', 0o55500, '', 'TS', 'DIFEQCNT', line=403)
W('13,2775', 0o51500, '', 'INDEX', 'DIFEQCNT', line=404)
W('13,2776', 0o31502, '', 'CA', 'RRECT', line=405)
W('13,2777', 0o51500, '', 'INDEX', 'DIFEQCNT', line=406)
W('13,3000', 0o55626, '', 'TS', 'RRECTLEM', line=407)
W('13,3001', 0o11500, '', 'CCS', 'DIFEQCNT', line=408)
W('13,3002', 0o12774, '', 'TCF', 'MOVEALEM +1', line=409)
W('13,3003', 0o06030, '', 'TC', 'DANZIG', line=410)

# PTOALEM TRANSFERS RRECTLEM TO RRECTLEM +41 TO RRECT TO RRECT +41

W('13,3004', 0o47014, 'PTOALEM', 'BON', 'RTB', kind='interp', line=414)
W('13,3005', 0o04307, '', '', 'SURFFLAG', kind='operand', line=415)
W('13,3006', 0o27025, '', '', 'USEPIOS', kind='operand', line=416)
W('13,3007', 0o27014, '', '', 'MOVEPLEM', kind='operand', line=417)
W('13,3010', 0o52014, '', 'BON', 'GOTO', kind='interp', line=418)
W('13,3011', 0o04304, '', '', 'LMOONFLG', kind='operand', line=419)
W('13,3012', 0o26742, '', '', 'SETMOON', kind='operand', line=420)
W('13,3013', 0o26735, '', '', 'CLRMOON', kind='operand', line=421)
W('13,3014', 0o03064, 'MOVEPLEM', 'TC', 'SETBANK', line=422)
W('13,3015', 0o55500, '', 'TS', 'DIFEQCNT', line=423)
W('13,3016', 0o51500, '', 'INDEX', 'DIFEQCNT', line=424)
W('13,3017', 0o31626, '', 'CA', 'RRECTLEM', line=425)
W('13,3020', 0o51500, '', 'INDEX', 'DIFEQCNT', line=426)
W('13,3021', 0o55502, '', 'TS', 'RRECT', line=427)
W('13,3022', 0o11500, '', 'CCS', 'DIFEQCNT', line=428)
W('13,3023', 0o13015, '', 'TCF', 'MOVEPLEM +1', line=429)
W('13,3024', 0o06030, '', 'TC', 'DANZIG', line=430)

W('13,3025', 0o77201, 'USEPIOS', 'SETPD', 'VLOAD', kind='interp', line=432)
W('13,3026', 0o00001, '', '', '0', kind='operand', line=433)
W('13,3027', 0o02026, '', '', 'RLS', kind='operand', line=434)
W('13,3030', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=435)
W('13,3031', 0o00041, '', '', 'TDEC1', kind='operand', line=436)
# Page 1317
W('13,3032', 0o15517, '', 'STODL', 'TET', kind='interp', line=438)
W('13,3033', 0o27755, '', '', '5/8', kind='operand', line=439)
W('13,3034', 0o77624, '', 'CALL', kind='interp', line=440)
W('13,3035', 0o55344, '', '', 'RP-TO-R', kind='operand', line=441)
W('13,3036', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=442)
W('13,3037', 0o11560, '', '', 'ZUNIT', kind='operand', line=443)
W('13,3040', 0o14001, '', 'STODL', '0D', kind='interp', line=444)
W('13,3041', 0o01517, '', '', 'TET', kind='operand', line=445)
W('13,3042', 0o14007, '', 'STODL', '6D', kind='interp', line=446)
W('13,3043', 0o27755, '', '', '5/8', kind='operand', line=447)
W('13,3044', 0o45014, '', 'SET', 'CALL', 'NEEDED FOR SETTING X1 ON EXIT', kind='interp', line=448)
W('13,3045', 0o00063, '', '', 'MOONFLAG', kind='operand', line=449)
W('13,3046', 0o55344, '', '', 'RP-TO-R', kind='operand', line=450)
W('13,3047', 0o74235, '', 'VXV', 'VXSC', kind='interp', line=451)
W('13,3050', 0o01535, '', '', 'RCV', kind='operand', line=452)
W('13,3051', 0o27063, '', '', 'OMEGMOON', kind='operand', line=453)
W('13,3052', 0o25543, '', 'STOVL', 'VCV', kind='interp', line=454)
W('13,3053', 0o11566, '', '', 'ZEROVEC', kind='operand', line=455)
W('13,3054', 0o01521, '', 'STORE', 'TDELTAV', kind='interp', line=456)
W('13,3055', 0o67174, '', 'AXT,2', 'SXA,2', kind='interp', line=457)
W('13,3056', 0o00002, '', '', '2', kind='operand', line=458)
W('13,3057', 0o02150, '', '', 'PBODY', kind='operand', line=459)
W('13,3060', 0o35527, '', 'STCALL', 'TNUV', kind='interp', line=460)
W('13,3061', 0o27176, '', '', 'A-PCHK', kind='operand', line=461)
W('13,3062', 0o07112, 'OMEGMOON', '2DEC*', '2.66169947 E-8 B+23*', kind='data', line=462)
W('13,3063', 0o06620, kind='data', line=462)

W('13,3064', 0o33070, 'SETBANK', 'CAF', 'INTBANK', line=464)
W('13,3065', 0o54006, '', 'TS', 'BBANK', line=465)
W('13,3066', 0o33507, '', 'CAF', 'FORTYONE', line=466)
W('13,3067', 0o00002, '', 'TC', 'Q', line=467)
#   EBANK= RRECTCSM
W('13,3070', 0o26063, 'INTBANK', 'BBCON', 'INTEGRV', kind='data', line=469)

# SPECIAL PURPOSE ENTRIES TO ORBITAL INTEGRATION.  THESE ROUTINES PROVIDE ENTRANCES TO INTEGRATION WITH
# APPROPRIATE SWITCHES SET OR CLEARED FOR THE DESIRED INTEGRATION.
#
# CSMPREC AND LEMPREC PERFORM ORBIT INTEGRATION BY THE ENCKE METHOD TO THE TIME INDICATED IN TDEC1
# ACCELERATIONS DUE TO OBLATENESS ARE INCLUDED.  NO W-MATRIX INT. IS DONE.
# THE PERMANENT STATE VECTOR IS NOT UPDATED.
# CSMCONIC AND LEMCONIC PERFORM ORBIT INTEG. BY KEPLERS METHOD TO THE TIME INDICATED IN TDEC1
# NO DISTURBING ACCELERATIONS ARE INCLUDED.  IN THE PROGRAM FLOW THE GIVEN
# STATE VECTOR IS RECTIFIED BEFORE SOLUTION OF KEPLERS EQUATION
#
# THE ROUTINES ASSUME THAT THE CSM (LEM) STATE VECTOR IN P-MEM IS VALID.
# SWITCHES SET PRIOR TO ENTRY TO THE MAIN INTEG. PROG ARE AS FOLLOWS
# CSMPREC         CSMCONIC        LEMPREC         LEMCONIC
# VINTFLAG        SET             SET             CLEAR           CLEAR
# INTYPFLG        CLEAR           SET             CLEAR           SET
# DIM0FLAG        CLEAR           CLEAR           CLEAR           CLEAR
# Page 1318
#
# CALLING SEQUENCE
# L-X     STORE TDEC1
# L       CALL                    (STCALL TDEC1)
# L+1             CSMPREC         (CSMCONIC, LEMPREC, LEMCONIC)
#
# NORMAL EXIT TO L+2
#
#
# SUBROUTINES CALLED
# INTEGRV1
# PRECOUT FOR CSMPREC AND LEMPREC
# CONICOUT FOR CSMCONIC AND LEMCONIC
#
# OUTPUT - SEE PAGE 2 OF THIS LOG SECTION
#
# INPUT
# TDEC1           TIME TO INTEGRATE TO . CSECS B-28

W('13,3071', 0o45020, 'CSMPREC', 'STQ', 'CALL', kind='interp', line=507)
W('13,3072', 0o00046, '', '', 'X1', kind='operand', line=508)
W('13,3073', 0o27442, '', '', 'INTSTALL', kind='operand', line=509)
W('13,3074', 0o43130, '', 'SXA,1', 'SET', kind='interp', line=510)
W('13,3075', 0o02214, '', '', 'IRETURN', kind='operand', line=511)
W('13,3076', 0o01474, '', '', 'VINTFLAG', kind='operand', line=512)

W('13,3077', 0o43014, 'IFLAGP', 'SET', 'CLEAR', kind='interp', line=514)
W('13,3100', 0o01467, '', '', 'PRECIFLG', kind='operand', line=515)
W('13,3101', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=516)
W('13,3102', 0o77614, '', 'CLRGO', kind='interp', line=517)
W('13,3103', 0o01633, '', '', 'INTYPFLG', kind='operand', line=518)
W('13,3104', 0o27164, '', '', 'INTEGRV1', kind='operand', line=519)
W('13,3105', 0o45020, 'LEMPREC', 'STQ', 'CALL', kind='interp', line=520)
W('13,3106', 0o00046, '', '', 'X1', kind='operand', line=521)
W('13,3107', 0o27442, '', '', 'INTSTALL', kind='operand', line=522)
W('13,3110', 0o43130, '', 'SXA,1', 'CLRGO', kind='interp', line=523)
W('13,3111', 0o02214, '', '', 'IRETURN', kind='operand', line=524)
W('13,3112', 0o01634, '', '', 'VINTFLAG', kind='operand', line=525)
W('13,3113', 0o27077, '', '', 'IFLAGP', kind='operand', line=526)

W('13,3114', 0o45020, 'CSMCONIC', 'STQ', 'CALL', kind='interp', line=528)
W('13,3115', 0o00046, '', '', 'X1', kind='operand', line=529)
W('13,3116', 0o27442, '', '', 'INTSTALL', kind='operand', line=530)
W('13,3117', 0o43130, '', 'SXA,1', 'SET', kind='interp', line=531)
W('13,3120', 0o02214, '', '', 'IRETURN', kind='operand', line=532)
W('13,3121', 0o01474, '', '', 'VINTFLAG', kind='operand', line=533)
W('13,3122', 0o43014, 'IFLAGC', 'CLEAR', 'SETGO', kind='interp', line=534)
W('13,3123', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=535)
W('13,3124', 0o01433, '', '', 'INTYPFLG', kind='operand', line=536)
W('13,3125', 0o27164, '', '', 'INTEGRV1', kind='operand', line=537)
W('13,3126', 0o45020, 'LEMCONIC', 'STQ', 'CALL', kind='interp', line=538)
W('13,3127', 0o00046, '', '', 'X1', kind='operand', line=539)
# Page 1319
W('13,3130', 0o27442, '', '', 'INTSTALL', kind='operand', line=541)
W('13,3131', 0o43130, '', 'SXA,1', 'CLRGO', kind='interp', line=542)
W('13,3132', 0o02214, '', '', 'IRETURN', kind='operand', line=543)
W('13,3133', 0o01634, '', '', 'VINTFLAG', kind='operand', line=544)
W('13,3134', 0o27122, '', '', 'IFLAGC', kind='operand', line=545)

W('13,3135', 0o66214, 'INTEGRVS', 'SET', 'SSP', kind='interp', line=547)
W('13,3136', 0o01467, '', '', 'PRECIFLG', kind='operand', line=548)
W('13,3137', 0o02151, '', '', 'PBODY', kind='operand', line=549)
W('13,3140', 0o00000, '', '', '0', kind='operand', line=550)
W('13,3141', 0o66214, '', 'BOF', 'SSP', kind='interp', line=551)
W('13,3142', 0o00343, '', '', 'MOONFLAG', kind='operand', line=552)
W('13,3143', 0o27146, '', '', '+3', kind='operand', line=553)
W('13,3144', 0o02151, '', '', 'PBODY', kind='operand', line=554)
W('13,3145', 0o00002, '', '', '2', kind='operand', line=555)
W('13,3146', 0o77220, '', 'STQ', 'VLOAD', kind='interp', line=556)
W('13,3147', 0o02214, '', '', 'IRETURN', kind='operand', line=557)
W('13,3150', 0o11566, '', '', 'ZEROVEC', kind='operand', line=558)
W('13,3151', 0o01521, '', 'STORE', 'TDELTAV', kind='interp', line=559)
W('13,3152', 0o35527, '', 'STCALL', 'TNUV', kind='interp', line=560)
W('13,3153', 0o23421, '', '', 'RECTIFY', kind='operand', line=561)
W('13,3154', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=562)
W('13,3155', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=563)
W('13,3156', 0o04062, '', '', 'NEWIFLG', kind='operand', line=564)
W('13,3157', 0o77614, '', 'SETGO', kind='interp', line=565)
W('13,3160', 0o04020, '', '', 'RPQFLAG', kind='operand', line=566)
W('13,3161', 0o22363, '', '', 'ALOADED', kind='operand', line=567)

# INTEGRV IS AN ENTRY TO ORBIT INTEGRATION WHICH PERMITS THE CALLER ,
# NORMALLY THE NAVIGATION PROGRAM ,TO SET THE INTEG. FLAGS.  THE ROUTINE
# IS ENTERED AT INTEGRV1 BY CSMPREC ET.AL. AND AT ALOADED BY INTEGRVS.
# THE ROUTINE SETS UP A-MEMORY IF ENTERED AT INTEGRV,1 AND SETS THE INTEG.
# PROGRAM FOR PRECISION OR CONIC.
#
# THE CALLER MUST FIRST CALL INTSTALL TO CHECK IF INTEG. IS IN USE BEFORE
# SETTING ANY FLAGS.
# THE FLAGS WHICH SHOULD BE SET OR CLEARED ARE
# VINTFLAG        (IGNORED WHEN ENTERED FROM INTEGRVS)
# INTYPFLG
# DIM0FLAG
# D6OR9FLG
# CALLING SEQUENCE
# L-X     CALL
# L-Y             INTSTALL
# L-1     SET OR CLEAR ALL FOUR FLAGS.  ALSO CAN SET STATEFLG IF DESIRED
# AND DIM0FLAG IS CLEAR.
# L       CALL
# L+1             INTEGRV
# INITIALIZATION
# FLAGS AS ABOVE
# STORE TIME TO INTEGRATE TO IN TDEC1
#
# Page 1320
# OUTPUT
# RATT    AS
# VATT          DEFINED
# TAT                     BEFORE

W('13,3162', 0o77620, 'INTEGRV', 'STQ', kind='interp', line=599)
W('13,3163', 0o02214, '', '', 'IRETURN', kind='operand', line=600)
W('13,3164', 0o43014, 'INTEGRV1', 'SET', 'SET', kind='interp', line=601)
W('13,3165', 0o04060, '', '', 'RPQFLAG', kind='operand', line=602)
W('13,3166', 0o04062, '', '', 'NEWIFLG', kind='operand', line=603)
W('13,3167', 0o77731, 'INTEGRV2', 'SSP', kind='interp', line=604)
W('13,3170', 0o00053, '', '', 'QPRET', kind='operand', line=605)
W('13,3171', 0o22363, '', '', 'ALOADED', kind='operand', line=606)
W('13,3172', 0o52014, '', 'BON', 'GOTO', kind='interp', line=607)
W('13,3173', 0o01714, '', '', 'VINTFLAG', kind='operand', line=608)
W('13,3174', 0o26731, '', '', 'PTOACSM', kind='operand', line=609)
W('13,3175', 0o27004, '', '', 'PTOALEM', kind='operand', line=610)
#   SETLOC INTINIT1
#   BANK
W('11,2363', 0o77745, 'ALOADED', 'DLOAD', kind='interp', line=613)
W('11,2364', 0o00041, '', '', 'TDEC1', kind='operand', line=614)
W('11,2365', 0o01101, '', 'STORE', 'TDEC', kind='interp', line=615)
W('11,2366', 0o52014, '', 'BOFF', 'GOTO', kind='interp', line=616)
W('11,2367', 0o01753, '', '', 'INTYPFLG', kind='operand', line=617)
W('11,2370', 0o27305, '', '', 'TESTLOOP', kind='operand', line=618)
W('11,2371', 0o27271, '', '', 'RVCON', kind='operand', line=619)
#   SETLOC INTINIT
#   BANK
W('13,3176', 0o45014, 'A-PCHK', 'BOF', 'CALL', kind='interp', line=622)
W('13,3177', 0o00342, '', '', 'MIDFLAG', kind='operand', line=623)
W('13,3200', 0o27205, '', '', 'ANDOUT', 'DONT MAKE ORIGIN CHANGE CHECK', kind='operand', line=624)
W('13,3201', 0o23320, '', '', 'CHKSWTCH', kind='operand', line=625)
W('13,3202', 0o45044, '', 'BPL', 'CALL', kind='interp', line=626)
W('13,3203', 0o27205, '', '', 'ANDOUT', 'NO ORIGIN CHANGE', kind='operand', line=627)
W('13,3204', 0o23361, '', '', 'ORIGCHNG', 'MAKE THE SWITCH', kind='operand', line=628)
W('13,3205', 0o77414, 'ANDOUT', 'BOFCLR', 'EXIT', kind='interp', line=629)
W('13,3206', 0o01652, '', '', 'STATEFLG', kind='operand', line=630)
W('13,3207', 0o27226, '', '', 'RECTOUT', kind='operand', line=631)
W('13,3210', 0o05412, '', 'TC', 'PHASCHNG', line=632)
W('13,3211', 0o04022, '', 'OCT', '04022', kind='data', line=633)
W('13,3212', 0o05546, '', 'TC', 'UPFLAG', 'PHASE CHANGE HAS OCCURRED BETWEEN', line=634)
W('13,3213', 0o00236, '', 'ADRES', 'REINTFLG', 'INTSTALL AND INTWAKE', kind='data', line=635)
W('13,3214', 0o06006, '', 'TC', 'INTPRET', line=636)
W('13,3215', 0o77731, '', 'SSP', kind='interp', line=637)
W('13,3216', 0o00053, '', '', 'QPRET', kind='operand', line=638)
W('13,3217', 0o27224, '', '', 'PHEXIT', kind='operand', line=639)
W('13,3220', 0o52014, '', 'BON', 'GOTO', kind='interp', line=640)
W('13,3221', 0o01714, '', '', 'VINTFLAG', kind='operand', line=641)
W('13,3222', 0o26705, '', '', 'ATOPCSM', kind='operand', line=642)
# Page 1321
W('13,3223', 0o26760, '', '', 'ATOPLEM', kind='operand', line=644)
W('13,3224', 0o77624, 'PHEXIT', 'CALL', kind='interp', line=645)
W('13,3225', 0o56750, '', '', 'GRP2PC', kind='operand', line=646)
W('13,3226', 0o45001, 'RECTOUT', 'SETPD', 'CALL', kind='interp', line=647)
W('13,3227', 0o00001, '', '', '0', kind='operand', line=648)
W('13,3230', 0o23421, '', '', 'RECTIFY', kind='operand', line=649)
W('13,3231', 0o53775, '', 'VLOAD', 'VSL*', kind='interp', line=650)
W('13,3232', 0o01503, '', '', 'RRECT', kind='operand', line=651)
W('13,3233', 0o57576, '', '', '0,2', kind='operand', line=652)
W('13,3234', 0o53715, '', 'PDVL', 'VSL*', 'RATT TO PD0', kind='interp', line=653)
W('13,3235', 0o01511, '', '', 'VRECT', kind='operand', line=654)
W('13,3236', 0o57576, '', '', '0,2', kind='operand', line=655)
W('13,3237', 0o63325, '', 'PDDL', 'PDVL', 'VATT TO PD6   TAT TO PD12', kind='interp', line=656)
W('13,3240', 0o01517, '', '', 'TET', kind='operand', line=657)
W('13,3241', 0o01503, '', '', 'RRECT', kind='operand', line=658)
W('13,3242', 0o64715, '', 'PDVL', 'PDDL*', kind='interp', line=659)
W('13,3243', 0o01511, '', '', 'VRECT', kind='operand', line=660)
W('13,3244', 0o50042, '', '', 'MUEARTH,2', kind='operand', line=661)
W('13,3245', 0o76006, '', 'PUSH', 'AXT,1', kind='interp', line=662)
W('13,3246', 0o77765, '', 'DEC', '-10', kind='data', line=663)
W('13,3247', 0o76014, '', 'BON', 'AXT,1', kind='interp', line=664)
W('13,3250', 0o00303, '', '', 'MOONFLAG', kind='operand', line=665)
W('13,3251', 0o27253, '', '', '+2', kind='operand', line=666)
W('13,3252', 0o77775, '', 'DEC', '-2', kind='data', line=667)
W('13,3253', 0o40001, 'INTEXIT', 'SETPD', 'BOV', kind='interp', line=668)
W('13,3254', 0o00001, '', '', '0', kind='operand', line=669)
W('13,3255', 0o27256, '', '', '+1', kind='operand', line=670)
W('13,3256', 0o77614, '', 'CLEAR', kind='interp', line=671)
W('13,3257', 0o04675, '', '', 'MIDAVFLG', kind='operand', line=672)
W('13,3260', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=673)
W('13,3261', 0o04676, '', '', 'AVEMIDSW', 'ALLOW UPDATE OF DOWNLINK STATE VECTOR', kind='operand', line=674)
W('13,3262', 0o01667, '', '', 'PRECIFLG', kind='operand', line=675)
W('13,3263', 0o77535, '', 'SLOAD', 'EXIT', kind='interp', line=676)
W('13,3264', 0o02215, '', '', 'IRETURN', kind='operand', line=677)
W('13,3265', 0o30154, '', 'CA', 'MPAC', line=678)
W('13,3266', 0o50120, '', 'INDEX', 'FIXLOC', line=679)
W('13,3267', 0o54052, '', 'TS', 'QPRET', line=680)
W('13,3270', 0o03457, '', 'TC', 'INTWAKE', line=681)

# RVCON SETS UP ORBIT INTEGRATION TO DO A CONIC SOLUTION FOR POSITION AND
# VELOCITY FOR THE INTERVAL (TET-TDEC)

W('13,3271', 0o45345, 'RVCON', 'DLOAD', 'DSU', kind='interp', line=686)
W('13,3272', 0o01101, '', '', 'TDEC', kind='operand', line=687)
W('13,3273', 0o01517, '', '', 'TET', kind='operand', line=688)
W('13,3274', 0o36312, '', 'STCALL', 'TAU.', kind='interp', line=689)
W('13,3275', 0o23421, '', '', 'RECTIFY', kind='operand', line=690)
W('13,3276', 0o77624, '', 'CALL', kind='interp', line=691)
W('13,3277', 0o22372, '', '', 'KEPPREP', kind='operand', line=692)
W('13,3300', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=693)
W('13,3301', 0o01551, '', '', 'TC', kind='operand', line=694)
# Page 1322
W('13,3302', 0o01517, '', '', 'TET', kind='operand', line=696)
W('13,3303', 0o35517, '', 'STCALL', 'TET', kind='interp', line=697)
W('13,3304', 0o27226, '', '', 'RECTOUT', kind='operand', line=698)

# Page 1323
W('13,3305', 0o43014, 'TESTLOOP', 'BOF', 'CLRGO', kind='interp', line=701)
W('13,3306', 0o04752, '', '', 'QUITFLAG', kind='operand', line=702)
W('13,3307', 0o27312, '', '', '+3', kind='operand', line=703)
W('13,3310', 0o01632, '', '', 'STATEFLG', kind='operand', line=704)
W('13,3311', 0o27253, '', '', 'INTEXIT', 'STOP INTEGRATION', kind='operand', line=705)
W('13,3312', 0o73001, '', 'SETPD', 'LXA,2', kind='interp', line=706)
W('13,3313', 0o00013, '', '', '10D', kind='operand', line=707)
W('13,3314', 0o02150, '', '', 'PBODY', kind='operand', line=708)
W('13,3315', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=709)
W('13,3316', 0o01535, '', '', 'RCV', kind='operand', line=710)
W('13,3317', 0o43006, '', 'PUSH', 'CLEAR', 'RC TO 10D', kind='interp', line=711)
W('13,3320', 0o00262, '', '', 'MIDFLAG', kind='operand', line=712)
W('13,3321', 0o50023, '', 'DSU*', 'BMN', 'MIDFLAG=0 IF R G.T. RMP', kind='interp', line=713)
W('13,3322', 0o67212, '', '', 'RME,2', kind='operand', line=714)
W('13,3323', 0o27326, '', '', '+3', kind='operand', line=715)
W('13,3324', 0o77614, '', 'SET', kind='interp', line=716)
W('13,3325', 0o00062, '', '', 'MIDFLAG', kind='operand', line=717)
W('13,3326', 0o41345, 'NORFINAL', 'DLOAD', 'DMP', kind='interp', line=718)
W('13,3327', 0o00013, '', '', '10D', kind='operand', line=719)
W('13,3330', 0o00043, '', '', '34D', kind='operand', line=720)
W('13,3331', 0o55762, '', 'SR1R', 'DDV*', kind='interp', line=721)
W('13,3332', 0o50042, '', '', 'MUEARTH,2', kind='operand', line=722)
W('13,3333', 0o41366, '', 'SQRT', 'DMP', kind='interp', line=723)
W('13,3334', 0o23752, '', '', '.3D', kind='operand', line=724)
W('13,3335', 0o40442, '', 'SR3', 'SR4', 'DT    IS TRUNCATED TO A MULTIPLE', kind='interp', line=725)
W('13,3336', 0o54345, '', 'DLOAD', 'SL', kind='interp', line=726)
W('13,3337', 0o00155, '', '', 'MPAC', kind='operand', line=727)
W('13,3340', 0o20220, '', '', '15D', '      OF 128 CSECS.', kind='operand', line=728)
W('13,3341', 0o40006, '', 'PUSH', 'BOV', kind='interp', line=729)
W('13,3342', 0o27367, '', '', 'MAXDT', kind='operand', line=730)
W('13,3343', 0o50021, '', 'BDSU', 'BMN', kind='interp', line=731)
W('13,3344', 0o27441, '', '', 'DT/2MAX', kind='operand', line=732)
W('13,3345', 0o27367, '', '', 'MAXDT', kind='operand', line=733)
W('13,3346', 0o45345, 'DT/2COMP', 'DLOAD', 'DSU', kind='interp', line=734)
W('13,3347', 0o01101, '', '', 'TDEC', kind='operand', line=735)
W('13,3350', 0o01517, '', '', 'TET', kind='operand', line=736)
W('13,3351', 0o54234, '', 'RTB', 'SL', kind='interp', line=737)
W('13,3352', 0o45544, '', '', 'SGNAGREE', kind='operand', line=738)
W('13,3353', 0o20211, '', '', '8D', kind='operand', line=739)
W('13,3354', 0o02314, '', 'STORE', 'DT/2', 'B-19', kind='interp', line=740)
W('13,3355', 0o51400, '', 'BOV', 'ABS', kind='interp', line=741)
W('13,3356', 0o27373, '', '', 'GETMAXDT', kind='operand', line=742)
W('13,3357', 0o50025, '', 'DSU', 'BMN', 'IS TIME TO INTEG. TO GR THAN MAXTIME', kind='interp', line=743)
W('13,3360', 0o00015, '', '', '12D', kind='operand', line=744)
W('13,3361', 0o27377, '', '', 'POOHCHK', kind='operand', line=745)
W('13,3362', 0o75345, 'USEMAXDT', 'DLOAD', 'SIGN', kind='interp', line=746)
W('13,3363', 0o00015, '', '', '12D', kind='operand', line=747)
W('13,3364', 0o02314, '', '', 'DT/2', kind='operand', line=748)
# Page 1324
W('13,3365', 0o36314, '', 'STCALL', 'DT/2', kind='interp', line=750)
W('13,3366', 0o27377, '', '', 'POOHCHK', kind='operand', line=751)
W('13,3367', 0o65345, 'MAXDT', 'DLOAD', 'PDDL', 'EXCHANGE DT/2MAX WITH COMPUTED MAX.', kind='interp', line=752)
W('13,3370', 0o27441, '', '', 'DT/2MAX', kind='operand', line=753)
W('13,3371', 0o77650, '', 'GOTO', kind='interp', line=754)
W('13,3372', 0o27346, '', '', 'DT/2COMP', kind='operand', line=755)
W('13,3373', 0o77634, 'GETMAXDT', 'RTB', kind='interp', line=756)
W('13,3374', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=757)
W('13,3375', 0o36314, '', 'STCALL', 'DT/2', kind='interp', line=758)
W('13,3376', 0o27362, '', '', 'USEMAXDT', kind='operand', line=759)
W('13,3377', 0o51545, 'POOHCHK', 'DLOAD', 'ABS', kind='interp', line=760)
W('13,3400', 0o02314, '', '', 'DT/2', kind='operand', line=761)
W('13,3401', 0o50025, '', 'DSU', 'BMN', kind='interp', line=762)
W('13,3402', 0o27437, '', '', 'DT/2MIN', kind='operand', line=763)
W('13,3403', 0o27176, '', '', 'A-PCHK', kind='operand', line=764)
W('13,3404', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=765)
W('13,3405', 0o01012, '', '', 'MODREG', kind='operand', line=766)
W('13,3406', 0o27411, '', '', '+3', kind='operand', line=767)
W('13,3407', 0o77650, '', 'GOTO', kind='interp', line=768)
W('13,3410', 0o23240, '', '', 'TIMESTEP', kind='operand', line=769)
W('13,3411', 0o77614, '', 'BON', '', 'WAS THIS CALL VIA CSM(LEM)PREC', kind='interp', line=770)
W('13,3412', 0o01707, '', '', 'PRECIFLG', kind='operand', line=771)
W('13,3413', 0o23240, '', '', 'TIMESTEP', 'YES', kind='operand', line=772)
W('13,3414', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=773)
W('13,3415', 0o02314, '', '', 'DT/2', kind='operand', line=774)
W('13,3416', 0o00015, '', '', '12D', kind='operand', line=775)
W('13,3417', 0o43040, '', 'BMN', 'BOFCLR', kind='interp', line=776)
W('13,3420', 0o27176, '', '', 'A-PCHK', kind='operand', line=777)
W('13,3421', 0o04242, '', '', 'NEWIFLG', kind='operand', line=778)
W('13,3422', 0o23240, '', '', 'TIMESTEP', kind='operand', line=779)
W('13,3423', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=780)
W('13,3424', 0o01101, '', '', 'TDEC', kind='operand', line=781)
W('13,3425', 0o01517, '', '', 'TET', kind='operand', line=782)
W('13,3426', 0o77640, '', 'BMN', '', 'NO BACKWARD INTEGRATION', kind='interp', line=783)
W('13,3427', 0o27253, '', '', 'INTEXIT', kind='operand', line=784)
W('13,3430', 0o40525, '', 'PDDL', 'SR4', kind='interp', line=785)
W('13,3431', 0o02314, '', '', 'DT/2', 'IS 4(DT) LS(TDEC - TET)', kind='operand', line=786)
W('13,3432', 0o44322, '', 'SR2R', 'BDSU', 'NO', kind='interp', line=787)
W('13,3433', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=788)
W('13,3434', 0o27253, '', '', 'INTEXIT', kind='operand', line=789)
W('13,3435', 0o23240, '', '', 'TIMESTEP', kind='operand', line=790)
W('13,3436', 0o00000, 'DT/2MIN', '2DEC', '3 B-20', kind='data', line=791)
W('13,3437', 0o01400, kind='data', line=791)

W('13,3440', 0o14152, 'DT/2MAX', '2DEC', '4000 E2 B-20', kind='data', line=793)
W('13,3441', 0o00000, kind='data', line=793)

W('13,3442', 0o77776, 'INTSTALL', 'EXIT', kind='interp', line=795)
W('13,3443', 0o35021, '', 'CAF', 'ZERO', line=796)
W('13,3444', 0o54001, 'ALLSTALL', 'TS', 'L', line=797)
W('13,3445', 0o30106, '', 'CA', 'RASFLAG', line=798)
W('13,3446', 0o50001, '', 'INDEX', 'L', line=799)
# Page 1325
W('13,3447', 0o73540, '', 'MASK', 'INTBITAB', 'IS THIS STALL AREA FREE', line=801)
W('13,3450', 0o00006, '', 'EXTEND', line=802)
W('13,3451', 0o13516, '', 'BZF', 'OKTOGRAB', 'YES', line=803)
W('13,3452', 0o50001, '', 'INDEX', 'L', line=804)
W('13,3453', 0o33535, '', 'CAF', 'WAKESTAL', line=805)
W('13,3454', 0o05175, '', 'TC', 'JOBSLEEP', line=806)
W('13,3455', 0o77776, 'INTWAKE0', 'EXIT', kind='interp', line=807)
W('13,3456', 0o13477, '', 'TCF', 'INTWAKE1', line=808)

W('13,3457', 0o40106, 'INTWAKE', 'CS', 'RASFLAG', 'IS THIS INTSTALLED ROUTINE TO BE', line=810)
W('13,3460', 0o75011, '', 'MASK', 'REINTBIT', '      RESTARTED', line=811)
W('13,3461', 0o10000, '', 'CCS', 'A', line=812)
W('13,3462', 0o03477, '', 'TC', 'INTWAKE1', 'NO', line=813)

W('13,3463', 0o50120, '', 'INDEX', 'FIXLOC', line=815)
W('13,3464', 0o30052, '', 'CA', 'QPRET', line=816)
W('13,3465', 0o55055, '', 'TS', 'TBASE2', 'YES, DONT RESTART WITH SOMEONE ELSES Q', line=817)

W('13,3466', 0o05412, '', 'TC', 'PHASCHNG', line=819)
W('13,3467', 0o04022, '', 'OCT', '04022', kind='data', line=820)

W('13,3470', 0o31055, '', 'CA', 'TBASE2', line=822)
W('13,3471', 0o50120, '', 'INDEX', 'FIXLOC', line=823)
W('13,3472', 0o54052, '', 'TS', 'QPRET', line=824)

W('13,3473', 0o35011, '', 'CAF', 'REINTBIT', line=826)
W('13,3474', 0o70106, '', 'MASK', 'RASFLAG', line=827)
W('13,3475', 0o00006, '', 'EXTEND', line=828)
W('13,3476', 0o13521, '', 'BZF', 'GOBAC', 'DONT INTWAKE IF WE CAME HERE VIA RESTART', line=829)

W('13,3477', 0o35021, 'INTWAKE1', 'CAF', 'ZERO', line=831)
W('13,3500', 0o54154, 'WAKE', 'TS', 'STALTEM', 'INDEX OF ANY STALL USER', line=832)
W('13,3501', 0o50154, 'WAKE1', 'INDEX', 'STALTEM', line=833)
W('13,3502', 0o33535, '', 'CAF', 'WAKESTAL', line=834)
W('13,3503', 0o00004, '', 'INHINT', line=835)
W('13,3504', 0o05201, '', 'TC', 'JOBWAKE', line=836)
W('13,3505', 0o10064, '', 'CCS', 'LOCCTR', line=837)
W('13,3506', 0o13501, '', 'TCF', 'WAKE1', 'MAY BE MORE TO WAKE UP', line=838)
W('13,3507', 0o00051, 'FORTYONE', 'DEC', '41', kind='data', line=839)
W('13,3510', 0o50154, '', 'INDEX', 'STALTEM', line=840)
W('13,3511', 0o43540, '', 'CS', 'INTBITAB', line=841)
W('13,3512', 0o70106, '', 'MASK', 'RASFLAG', line=842)
W('13,3513', 0o54106, '', 'TS', 'RASFLAG', 'RELEASE STALL AREA', line=843)
W('13,3514', 0o00003, '', 'RELINT', line=844)
W('13,3515', 0o13521, '', 'TCF', 'GOBAC', line=845)
W('13,3516', 0o50001, 'OKTOGRAB', 'INDEX', 'L', 'NO, WAIT UNTIL AVAILABLE', line=846)
W('13,3517', 0o35002, '', 'CAF', 'INTFLBIT', line=847)
W('13,3520', 0o26106, '', 'ADS', 'RASFLAG', line=848)
W('13,3521', 0o06006, 'GOBAC', 'TC', 'INTPRET', line=849)
W('13,3522', 0o77616, '', 'RVQ', kind='interp', line=850)
# Page 1326
W('13,3523', 0o77776, 'ERASTAL1', 'EXIT', kind='interp', line=852)
W('13,3524', 0o35017, '', 'CAF', 'ONE', line=853)
W('13,3525', 0o13444, '', 'TCF', 'ALLSTALL', line=854)
W('13,3526', 0o77776, 'ERASTAL2', 'EXIT', kind='interp', line=855)
W('13,3527', 0o35016, '', 'CAF', 'TWO', line=856)
W('13,3530', 0o13444, '', 'TCF', 'ALLSTALL', line=857)
W('13,3531', 0o35017, 'ERASWAK1', 'CAF', 'ONE', line=858)
W('13,3532', 0o13500, '', 'TCF', 'WAKE', line=859)
W('13,3533', 0o35016, 'ERASWAK2', 'CAF', 'TWO', line=860)
W('13,3534', 0o13500, '', 'TCF', 'WAKE', line=861)
W('13,3535', 0o27443, 'WAKESTAL', 'CADR', 'INTSTALL +1', kind='data', line=862)
W('13,3536', 0o27524, '', 'CADR', 'ERASTAL1 +1', kind='data', line=863)
W('13,3537', 0o27527, '', 'CADR', 'ERASTAL2 +1', kind='data', line=864)
S('STALTEM', 'equals', 0o154, line=865)
W('13,3540', 0o20100, 'INTBITAB', 'OCT', '20100', kind='data', line=866)
W('13,3541', 0o10040, '', 'OCT', '10040', kind='data', line=867)
W('13,3542', 0o04020, '', 'OCT', '04020', kind='data', line=868)

# Page 1327
# AVETOMID
#
# THIS ROUTINE PERFORMS THE TRANSITION FROM A THRUSTING PHASE TO THE COAST
# PHASE BY INITIALIZING THIS VEHICLES PERMANENT STATE VECTOR WITH THE
# VALUES LEFT BY THE AVERAGEG ROUTINE IN RN,VN,PIPTIME.
#
# BEFORE THIS IS DONE THE W-MATRIX, IF ITS VALID (ORWFLAG OR RENDWFLT IS
# SET) IS INTEGRATED FORWARD TO PIPTIME WITH THE PRE-THRUST STATE VECTOR.
#
# IN ADDITION, THE OTHER VEHICLE IS INTEGRATED (PERMANENT) TO PIPTIME.
#
# FINALLY TRKMKCNT IS ZEROED.

#   SETLOC INTINIT2
#   BANK

#   COUNT* $$/INTIN
W('35,3675', 0o43020, 'AVETOMID', 'STQ', 'BON', kind='interp', line=888)
W('35,3676', 0o02317, '', '', 'EGRESS', kind='operand', line=889)
W('35,3677', 0o02716, '', '', 'RENDWFLG', kind='operand', line=890)
W('35,3700', 0o73753, '', '', 'INT/W', 'W-MATRIX VALID ,GO INTEGRATE IT', kind='operand', line=891)
W('35,3701', 0o77614, '', 'BON', kind='interp', line=892)
W('35,3702', 0o01711, '', '', 'ORBWFLAG', kind='operand', line=893)
W('35,3703', 0o73753, '', '', 'INT/W', 'W-MATRIX VALID ,GO INTEGRATE IT', kind='operand', line=894)

W('35,3704', 0o45174, 'SETCOAST', 'AXT,2', 'CALL', 'NOW MOVE PROPERLY SCALED RN,VN AND', kind='interp', line=896)
W('35,3705', 0o00002, '', '', '2', 'PIPTIME TO INTEGRATION ERASABLES.', kind='operand', line=897)
W('35,3706', 0o27442, '', '', 'INTSTALL', kind='operand', line=898)
W('35,3707', 0o77014, '', 'BON', 'AXT,2', kind='interp', line=899)
W('35,3710', 0o00315, '', '', 'AMOONFLG', kind='operand', line=900)
W('35,3711', 0o73713, '', '', '+2', kind='operand', line=901)
W('35,3712', 0o00000, '', '', '0', kind='operand', line=902)
W('35,3713', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=903)
W('35,3714', 0o01171, '', '', 'RN', kind='operand', line=904)
W('35,3715', 0o57176, '', '', '0,2', kind='operand', line=905)
W('35,3716', 0o01503, '', 'STORE', 'RRECT', kind='interp', line=906)
W('35,3717', 0o15535, '', 'STODL', 'RCV', kind='interp', line=907)
W('35,3720', 0o01205, '', '', 'PIPTIME', kind='operand', line=908)
W('35,3721', 0o25517, '', 'STOVL', 'TET', kind='interp', line=909)
W('35,3722', 0o01177, '', '', 'VN', kind='operand', line=910)
W('35,3723', 0o45057, '', 'VSR*', 'CALL', kind='interp', line=911)
W('35,3724', 0o57176, '', '', '0,2', kind='operand', line=912)
W('35,3725', 0o23435, '', '', 'MINIRECT', 'FINISH SETTING UP STATE VECTOR', kind='operand', line=913)
W('35,3726', 0o66234, '', 'RTB', 'SSP', kind='interp', line=914)
W('35,3727', 0o26720, '', '', 'MOVATHIS', 'PUT TEMP STATE VECTOR INTO PERMANENT', kind='operand', line=915)
W('35,3730', 0o01127, '', '', 'TRKMKCNT', kind='operand', line=916)
W('35,3731', 0o00000, '', '', '0', kind='operand', line=917)
W('35,3732', 0o43014, '', 'SET', 'BON', kind='interp', line=918)
W('35,3733', 0o04063, '', '', 'CMOONFLG', kind='operand', line=919)
# Page 1328
W('35,3734', 0o00315, '', '', 'AMOONFLG', kind='operand', line=921)
W('35,3735', 0o73740, '', '', '+3', kind='operand', line=922)
W('35,3736', 0o77614, '', 'CLEAR', kind='interp', line=923)
W('35,3737', 0o04263, '', '', 'CMOONFLG', kind='operand', line=924)

W('35,3740', 0o71214, '', 'BON', 'DLOAD', 'NOW DO LM', kind='interp', line=926)
W('35,3741', 0o04307, '', '', 'SURFFLAG', kind='operand', line=927)
W('35,3742', 0o75751, '', '', 'FAZAB5', 'NO COASTING LM', kind='operand', line=928)
W('35,3743', 0o01205, '', '', 'PIPTIME', kind='operand', line=929)
W('35,3744', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=930)
W('35,3745', 0o26670, '', '', 'SETIFLGS', kind='operand', line=931)
W('35,3746', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=932)
W('35,3747', 0o01674, '', '', 'VINTFLAG', kind='operand', line=933)
W('35,3750', 0o27162, '', '', 'INTEGRV', kind='operand', line=934)
W('35,3751', 0o77650, '', 'GOTO', kind='interp', line=935)
W('35,3752', 0o02317, '', '', 'EGRESS', kind='operand', line=936)
W('35,3753', 0o45145, 'INT/W', 'DLOAD', 'CALL', kind='interp', line=937)
W('35,3754', 0o01205, '', '', 'PIPTIME', 'INTEGRATE W THRU BURN', kind='operand', line=938)
W('35,3755', 0o27442, '', '', 'INTSTALL', kind='operand', line=939)
W('35,3756', 0o43014, '', 'SET', 'SET', kind='interp', line=940)
W('35,3757', 0o01476, '', '', 'DIM0FLAG', 'DO W-MATRIX', kind='operand', line=941)
W('35,3760', 0o04476, '', '', 'AVEMIDSW', 'SO WONT CLOBBER RN,VN,PIPTIME', kind='operand', line=942)
W('35,3761', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=943)
W('35,3762', 0o01675, '', '', 'D6OR9FLG', kind='operand', line=944)
W('35,3763', 0o01474, '', '', 'VINTFLAG', kind='operand', line=945)
W('35,3764', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=946)
W('35,3765', 0o27162, '', '', 'INTEGRV', kind='operand', line=947)
W('35,3766', 0o77650, '', 'GOTO', kind='interp', line=948)
W('35,3767', 0o73704, '', '', 'SETCOAST', kind='operand', line=949)

# Page 1329
# MIDTOAV1
#
# THIS ROUTINE INTEGRATES (PRECISION) TO THE TIME SPECIFIED IN TDEC1.
# IF, AT THE END OF AN INTEGRATION TIME STEP, CURRENT TIME PLUS A DELTA
# TIME (SEE TIMEDELT.....BASED ON THE COMPUTATUON TIME FOR ONE TIME STEP)
# IS GREATER THAN THE DESIRED TIME, ALARM 1703 IS SET AND THE INTEGRATION
# IS DONE AS IT IS FOR MIDTOAV2.
# RETURN IS IN BASIC TO THE RETURN ADDRESS PLUS ONE.
#
# IF THE INTEGRATION IS FINISHED TO THE DESIRED TIME, RETURN IS IN BASIC
# TO THE RETURN ADDRESS.
#
# IN EITHER CASE , BEFORE RETURNING, THE EXTRAPOLATED STATE VECTOR IS TRAN
# FERRED FROM R,VATT TO R,VN1-PIPTIME1 IS SET TO THE FINISHING INTEGRA-
# TION TIME AND MPAC IS SET TO THE DELTA TIME---
# TAT MINUS CURRENT TIME.

# MIDTOAV2
#
# THIS ROUTINE INTEGRATES THE CSM STATE VECTOR TO CURRENT TIME PLUS
# INCREMENTS OF TIMEDELT SUCH THAT THE DIFFERENCE BETWEEN CURRENT TIME
# AND THE STATE VECTOR TIME AT THE END OF THE LAST STEP IS AT LEAST 5.6
# SECS.
# NO INPUTS ARE REQUIRED OF THE CALLER.  RETURN IS IN BASIC TO THE RETURN
# ADDRESS WITH THE ABOVE TRANSFERS TO R,VN1-PIPTIME1-AND MPAC DONE

#   SETLOC INTINIT
#   BANK
#   EBANK= IRETURN1
W('13,3543', 0o45020, 'MIDTOAV2', 'STQ', 'CALL', kind='interp', line=981)
W('13,3544', 0o01127, '', '', 'IRETURN1', kind='operand', line=982)
W('13,3545', 0o27442, '', '', 'INTSTALL', kind='operand', line=983)
W('13,3546', 0o43145, '', 'DLOAD', 'CLEAR', kind='interp', line=984)
W('13,3547', 0o27711, '', '', 'TIMEDELT', kind='operand', line=985)
W('13,3550', 0o04674, '', '', 'MID1FLAG', kind='operand', line=986)
W('13,3551', 0o37732, '', 'STCALL', 'T-TO-ADD', kind='interp', line=987)
W('13,3552', 0o27567, '', '', 'ENTMID2', kind='operand', line=988)

W('13,3553', 0o45020, 'MIDTOAV1', 'STQ', 'CALL', kind='interp', line=990)
W('13,3554', 0o01127, '', '', 'IRETURN1', kind='operand', line=991)
W('13,3555', 0o27442, '', '', 'INTSTALL', kind='operand', line=992)
W('13,3556', 0o47014, '', 'SET', 'RTB', kind='interp', line=993)
W('13,3557', 0o04474, '', '', 'MID1FLAG', kind='operand', line=994)
W('13,3560', 0o45510, '', '', 'LOADTIME', kind='operand', line=995)
W('13,3561', 0o44215, '', 'DAD', 'BDSU', 'INITIAL CHECK.IS TDEC1 IN THE FUTURE.', kind='interp', line=996)
W('13,3562', 0o27711, '', '', 'TIMEDELT', kind='operand', line=997)
W('13,3563', 0o00041, '', '', 'TDEC1', kind='operand', line=998)
W('13,3564', 0o45044, '', 'BPL', 'CALL', kind='interp', line=999)
W('13,3565', 0o27573, '', '', 'ENTMID1', kind='operand', line=1000)
# Page 1330
W('13,3566', 0o27674, '', '', 'NOTIME', 'NO SET ALARM.SWITCH TO MIDTOAV2', kind='operand', line=1002)

W('13,3567', 0o43234, 'ENTMID2', 'RTB', 'DAD', kind='interp', line=1004)
W('13,3570', 0o45510, '', '', 'LOADTIME', kind='operand', line=1005)
W('13,3571', 0o03732, '', '', 'T-TO-ADD', kind='operand', line=1006)
W('13,3572', 0o00041, '', 'STORE', 'TDEC1', kind='interp', line=1007)

W('13,3573', 0o45014, 'ENTMID1', 'CLEAR', 'CALL', kind='interp', line=1009)
W('13,3574', 0o01676, '', '', 'DIM0FLAG', 'NO W-MATRIX', kind='operand', line=1010)
W('13,3575', 0o26034, '', '', 'THISVINT', kind='operand', line=1011)
W('13,3576', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=1012)
W('13,3577', 0o01673, '', '', 'INTYPFLG', kind='operand', line=1013)
W('13,3600', 0o04475, '', '', 'MIDAVFLG', 'LET INTEG. KNOW THE CALL IS FOR MIDTOAV.', kind='operand', line=1014)
W('13,3601', 0o77624, '', 'CALL', kind='interp', line=1015)
W('13,3602', 0o27162, '', '', 'INTEGRV', ' GO INTEGRATE', kind='operand', line=1016)
W('13,3603', 0o66134, '', 'SXA,2', 'SXA,1', kind='interp', line=1017)
W('13,3604', 0o03746, '', '', 'RTX2', kind='operand', line=1018)
W('13,3605', 0o03745, '', '', 'RTX1', kind='operand', line=1019)
W('13,3606', 0o67214, '', 'CLEAR', 'SLOAD', kind='interp', line=1020)
W('13,3607', 0o00275, '', '', 'AMOONFLG', kind='operand', line=1021)
W('13,3610', 0o03747, '', '', 'RTX2', kind='operand', line=1022)
W('13,3611', 0o43054, '', 'BZE', 'SET', kind='interp', line=1023)
W('13,3612', 0o27614, '', '', '+2', kind='operand', line=1024)
W('13,3613', 0o00075, '', '', 'AMOONFLG', kind='operand', line=1025)
W('13,3614', 0o77775, '', 'VLOAD', kind='interp', line=1026)
W('13,3615', 0o00001, '', '', 'RATT', kind='operand', line=1027)
W('13,3616', 0o25232, '', 'STOVL', 'RN1', kind='interp', line=1028)
W('13,3617', 0o00007, '', '', 'VATT', kind='operand', line=1029)
W('13,3620', 0o15240, '', 'STODL', 'VN1', kind='interp', line=1030)
W('13,3621', 0o00015, '', '', 'TAT', kind='operand', line=1031)
W('13,3622', 0o01246, '', 'STORE', 'PIPTIME1', kind='interp', line=1032)
W('13,3623', 0o77776, '', 'EXIT', kind='interp', line=1033)

W('13,3624', 0o00004, '', 'INHINT', line=1035)
W('13,3625', 0o00006, '', 'EXTEND', line=1036)
W('13,3626', 0o40025, '', 'DCS', 'TIME2', line=1037)
W('13,3627', 0o20155, '', 'DAS', 'MPAC', line=1038)
W('13,3630', 0o07226, '', 'TC', 'TPAGREE', line=1039)

W('13,3631', 0o31127, '', 'CA', 'IRETURN1', line=1041)
W('13,3632', 0o04704, '', 'TC', 'BANKJUMP', line=1042)
W('13,3633', 0o47014, 'CKMID2', 'BOF', 'RTB', kind='interp', line=1043)
W('13,3634', 0o04754, '', '', 'MID1FLAG', kind='operand', line=1044)
W('13,3635', 0o27652, '', '', 'MID2', kind='operand', line=1045)
W('13,3636', 0o45510, '', '', 'LOADTIME', kind='operand', line=1046)
W('13,3637', 0o44215, '', 'DAD', 'BDSU', kind='interp', line=1047)
W('13,3640', 0o27711, '', '', 'TIMEDELT', kind='operand', line=1048)
W('13,3641', 0o01101, '', '', 'TDEC', kind='operand', line=1049)
W('13,3642', 0o45044, '', 'BPL', 'CALL', kind='interp', line=1050)
W('13,3643', 0o27305, '', '', 'TESTLOOP', 'YES', kind='operand', line=1051)
# Page 1331
W('13,3644', 0o27674, '', '', 'NOTIME', kind='operand', line=1053)

W('13,3645', 0o43234, 'TIMEINC', 'RTB', 'DAD', kind='interp', line=1055)
W('13,3646', 0o45510, '', '', 'LOADTIME', kind='operand', line=1056)
W('13,3647', 0o03732, '', '', 'T-TO-ADD', kind='operand', line=1057)
W('13,3650', 0o35101, '', 'STCALL', 'TDEC', kind='interp', line=1058)
W('13,3651', 0o27305, '', '', 'TESTLOOP', kind='operand', line=1059)

W('13,3652', 0o45345, 'MID2', 'DLOAD', 'DSU', kind='interp', line=1061)
W('13,3653', 0o01101, '', '', 'TDEC', kind='operand', line=1062)
W('13,3654', 0o01517, '', '', 'TET', kind='operand', line=1063)
W('13,3655', 0o45246, '', 'ABS', 'DSU', kind='interp', line=1064)
W('13,3656', 0o27707, '', '', '3CSECS', kind='operand', line=1065)
W('13,3657', 0o77644, '', 'BPL', kind='interp', line=1066)
W('13,3660', 0o27645, '', '', 'TIMEINC', kind='operand', line=1067)

W('13,3661', 0o44234, '', 'RTB', 'BDSU', 'SEE IF 5.6 SECS. AVAILABLE TO CALLER', kind='interp', line=1069)
W('13,3662', 0o45510, '', '', 'LOADTIME', kind='operand', line=1070)
W('13,3663', 0o01517, '', '', 'TET', kind='operand', line=1071)
W('13,3664', 0o51025, '', 'DSU', 'BPL', kind='interp', line=1072)
W('13,3665', 0o27713, '', '', '5.6SECS', kind='operand', line=1073)
W('13,3666', 0o27176, '', '', 'A-PCHK', 'YES,GET OUT.', kind='operand', line=1074)

W('13,3667', 0o43345, '', 'DLOAD', 'DAD', 'NO,ADD TIMEDELT TO T-TO-ADD AND TRY', kind='interp', line=1076)
W('13,3670', 0o03732, '', '', 'T-TO-ADD', 'AGAIN.', kind='operand', line=1077)
W('13,3671', 0o27711, '', '', 'TIMEDELT', kind='operand', line=1078)
W('13,3672', 0o37732, '', 'STCALL', 'T-TO-ADD', kind='interp', line=1079)
W('13,3673', 0o27645, '', '', 'TIMEINC', kind='operand', line=1080)
W('13,3674', 0o77414, 'NOTIME', 'CLEAR', 'EXIT', 'TOO LATE', kind='interp', line=1081)
W('13,3675', 0o04674, '', '', 'MID1FLAG', kind='operand', line=1082)
W('13,3676', 0o25127, '', 'INCR', 'IRETURN1', 'SET ERROR EXIT (CALLOC +2)', line=1083)
W('13,3677', 0o05650, '', 'TC', 'ALARM', 'INSUFFICIENT TIME FOR INTEGRATION --', line=1084)
W('13,3700', 0o01703, '', 'OCT', '1703', '      TIG WILL BE SLIPPED...', kind='data', line=1085)
W('13,3701', 0o06006, '', 'TC', 'INTPRET', line=1086)
W('13,3702', 0o77745, '', 'DLOAD', kind='interp', line=1087)
W('13,3703', 0o27711, '', '', 'TIMEDELT', kind='operand', line=1088)
W('13,3704', 0o03732, '', 'STORE', 'T-TO-ADD', kind='interp', line=1089)
W('13,3705', 0o77616, '', 'RVQ', kind='interp', line=1090)

W('13,3706', 0o00000, '3CSECS', '2DEC', '3', kind='data', line=1092)
W('13,3707', 0o00003, kind='data', line=1092)

W('13,3710', 0o00000, 'TIMEDELT', '2DEC', '1250', kind='data', line=1094)
W('13,3711', 0o02342, kind='data', line=1094)

W('13,3712', 0o00000, '5.6SECS', '2DEC', '560', kind='data', line=1096)
W('13,3713', 0o01060, kind='data', line=1096)

#   BANK 27
#   SETLOC UPDATE2
#   BANK
#   EBANK= INTWAKUQ

# Page 1332
#   COUNT* $$/INTIN

S('INTWAKUQ', 'equals', 0o330, line=1106)  # TEMPORARY UNTIL NAME OF INTWAK1Q IS CHNG

W('27,2671', 0o00003, 'INTWAKEU', 'RELINT', line=1108)
W('27,2672', 0o00006, '', 'EXTEND', line=1109)
W('27,2673', 0o22330, '', 'QXCH', 'INTWAKUQ', 'SAVE Q FOR RETURN', line=1110)

W('27,2674', 0o06006, '', 'TC', 'INTPRET', line=1112)

W('27,2675', 0o53135, '', 'SLOAD', 'BZE', 'IS THIS A CSM/LEM STATE VECTOR UPDATE', kind='interp', line=1114)
W('27,2676', 0o01502, '', '', 'UPSVFLAG', 'REQUEST.  IF NOT GO TO INTWAKUP.', kind='operand', line=1115)
W('27,2677', 0o56736, '', '', 'INTWAKUP', kind='operand', line=1116)

W('27,2700', 0o77775, '', 'VLOAD', '', 'MOVE RRECT(6) AND VRECT(6) INTO', kind='interp', line=1118)
W('27,2701', 0o01503, '', '', 'RRECT', '     RCV(6)   AND VCV(6)   RESPECTIVELY.', kind='operand', line=1119)
W('27,2702', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=1120)
W('27,2703', 0o01511, '', '', 'VRECT', "NOW GO TO 'RECTIFY +13D' TO", kind='operand', line=1121)
W('27,2704', 0o77624, '', 'CALL', '', 'STORE VRECT INTO VCV  AND ZERO OUT', kind='interp', line=1122)
W('27,2705', 0o23436, '', '', 'RECTIFY +13D', 'TDELTAV(6),TNUV(6),TC(2) AND XKEP(2)', kind='operand', line=1123)
W('27,2706', 0o51535, '', 'SLOAD', 'ABS', "COMPARE ABSOLUTE VALUE OF 'UPSVFLAG'", kind='interp', line=1124)
W('27,2707', 0o01502, '', '', 'UPSVFLAG', "TO 'UPDATE MOON STATE VECTOR CODE'", kind='operand', line=1125)
W('27,2710', 0o53025, '', 'DSU', 'BZE', 'TO DETERMINE WHETHER THE STATE VECTOR TO', kind='interp', line=1126)
W('27,2711', 0o16747, '', '', 'UPMNSVCD', 'BE UPDATED IS IN THE EARTH OR LUNAR', kind='operand', line=1127)
W('27,2712', 0o56717, '', '', 'INTWAKEM', 'SPHERE OF INFLUENCE.........', kind='operand', line=1128)
W('27,2713', 0o43174, '', 'AXT,2', 'CLRGO', 'EARTH SPHERE OF INFLUENCE.', kind='interp', line=1129)
W('27,2714', 0o00000, '', 'DEC', '0', kind='data', line=1130)
W('27,2715', 0o00223, '', '', 'MOONFLAG', kind='operand', line=1131)
W('27,2716', 0o56722, '', '', 'INTWAKEC', kind='operand', line=1132)
W('27,2717', 0o43174, 'INTWAKEM', 'AXT,2', 'SET', 'LUNAR SPHERE OF INFLUENCE.', kind='interp', line=1133)
W('27,2720', 0o00002, '', 'DEC', '2', kind='data', line=1134)
W('27,2721', 0o00063, '', '', 'MOONFLAG', kind='operand', line=1135)
W('27,2722', 0o50135, 'INTWAKEC', 'SLOAD', 'BMN', 'COMMON CODING AFTER X2 INITIALIZED AND', kind='interp', line=1136)
# MOONFLAG SET (OR CLEARED).
W('27,2723', 0o01502, '', '', 'UPSVFLAG', 'IS THIS A REQUEST FOR A LEM OR CSM', kind='operand', line=1138)
W('27,2724', 0o56732, '', '', 'INTWAKLM', ' STATE VECTOR UPDATE......', kind='operand', line=1139)
W('27,2725', 0o77624, '', 'CALL', '', 'UPDATE CSM STATE VECTOR', kind='interp', line=1140)
W('27,2726', 0o26705, '', '', 'ATOPCSM', kind='operand', line=1141)

W('27,2727', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=1143)
W('27,2730', 0o01671, '', '', 'ORBWFLAG', kind='operand', line=1144)
W('27,2731', 0o56734, '', '', 'INTWAKEX', kind='operand', line=1145)

W('27,2732', 0o77624, 'INTWAKLM', 'CALL', '', 'UPDATE  LM STATE VECTOR', kind='interp', line=1147)
W('27,2733', 0o26760, '', '', 'ATOPLEM', kind='operand', line=1148)

W('27,2734', 0o77614, 'INTWAKEX', 'CLEAR', kind='interp', line=1150)
W('27,2735', 0o02676, '', '', 'RENDWFLG', kind='operand', line=1151)

W('27,2736', 0o45131, 'INTWAKUP', 'SSP', 'CALL', 'REMOVE :UPDATE STATE VECTOR INDICATOR:', kind='interp', line=1153)
# Page 1333
W('27,2737', 0o01502, '', '', 'UPSVFLAG', kind='operand', line=1155)
W('27,2740', 0o00000, '', '', '0', kind='operand', line=1156)
W('27,2741', 0o27455, '', '', 'INTWAKE0', 'RELEASE :GRAB: OF ORBIT INTEG', kind='operand', line=1157)
W('27,2742', 0o77776, '', 'EXIT', kind='interp', line=1158)

W('27,2743', 0o05412, '', 'TC', 'PHASCHNG', line=1160)
W('27,2744', 0o04026, '', 'OCT', '04026', kind='data', line=1161)
W('27,2745', 0o00330, '', 'TC', 'INTWAKUQ', line=1162)

W('27,2746', 0o00002, 'UPMNSVCD', 'OCT', '2', kind='data', line=1164)
W('27,2747', 0o00000, '', 'OCT', '0', kind='data', line=1165)

W('27,2750', 0o77420, 'GRP2PC', 'STQ', 'EXIT', kind='interp', line=1167)
W('27,2751', 0o03536, '', '', 'GRP2SVQ', kind='operand', line=1168)
W('27,2752', 0o05412, '', 'TC', 'PHASCHNG', line=1169)
W('27,2753', 0o04022, '', 'OCT', '04022', kind='data', line=1170)
W('27,2754', 0o06006, '', 'TC', 'INTPRET', line=1171)
W('27,2755', 0o77650, '', 'GOTO', kind='interp', line=1172)
W('27,2756', 0o03536, '', '', 'GRP2SVQ', kind='operand', line=1173)
