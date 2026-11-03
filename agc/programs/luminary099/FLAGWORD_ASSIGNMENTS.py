"""FLAGWORD_ASSIGNMENTS.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/FLAGWORD_ASSIGNMENTS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 61-89 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('FLAGWORD_ASSIGNMENTS', 'FLAGWORD_ASSIGNMENTS.agc', 'Luminary099', pages='61-89')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     FLAGWORD_ASSIGNMENTS.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Onno Hommes <ohommes@cmu.edu>.
# Website:      www.ibiblio.org/apollo.
# Pages:        0061-0089
# Mod history:  2009-05-15 OH   Transcribed from page images.
# 2009-05-17 RSB  Extended to (blank) p. 89.
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

# Page 61
# FLAGWORDS 0-11        ARE DOWNLINKED AND CAN BE SET AND CLEARED BY UP-FLAG AND DOWN-FLAG INSTRUCTIONS IN THE
# INTERPRETER.  THESE WERE PREVIOUSLY LISTED UNDER "INTERPRETIVE SWITCH BIT ASSIGNMENTS" IN
# THE ERASABLE LOG SECTION.  FLAGWORDS 12 & 13 WERE PREVIOUSLY RADMODES AND DAPBOOLS AND
# ARE STILL DOWNLINKED UNDER THOSE NAMES.

# ALPHABETICAL LIST OF FLAGWORDS

#
# FLAGWORD      DEC. NUMBER     BIT AND FLAG            BIT NAME

# ACCOKFLG      207             BIT  3 FLAG 13          ACCSOKAY
# ACC4-2FL      199             BIT 11 FLAG 13          ACC4OR2X
# ACMODFLG      032             BIT 13 FLAG  2          ACMODBIT
# ALTSCALE      186             BIT  9 FLAG 12          ALTSCBIT
# ANTENFLG      183             BIT 12 FLAG 12          ANTENBIT
# AORBSFLG      205             BIT  5 FLAG 13          AORBSYST
# AORBTFLG      200             BIT 10 FLAG 13          AORBTRAN
# APSESW        130             BIT  5 FLAG  8          APSESBIT
# APSFLAG       152             BIT 13 FLAG 10          APSFLBIT
# ASTNFLAG      108             BIT 12 FLAG  7          ASTNBIT
# ATTFLAG       104             BIT  1 FLAG  6          ATTFLBIT
# AUTOMODE      193             BIT  2 FLAG 12          AUTOMBIT
# AUTR1FLG      209             BIT  1 FLAG 13          AUTRATE1
# AUTR2FLG      208             BIT  2 FLAG 13          AUTRATE2
# AUXFLAG       103             BIT  2 FLAG  6          AUXFLBIT
# AVEGFLAG      115             BIT  5 FLAG  7          AVEGFBIT
# AVEMIDSW      149             BIT  1 FLAG  9          AVEMDBIT
# AVFLAG        040             BIT  5 FLAG  2          AVFLBIT
# CALCMAN2      043             BIT  2 FLAG  2          CALC2BIT
# CALCMAN3      042             BIT  3 FLAG  2          CALC3BIT
# CDESFLAG      180             BIT 15 FLAG 12          CDESBIT
# CMOONFLG      123             BIT 12 FLAG  8          CMOONBIT
# COGAFLAG      131             BIT  4 FLAG  8          COGAFBIT
# CSMDKFLG      197             BIT 13 FLAG 13          CSMDOCKD
# CULTFLAG      053             BIT  7 FLAG  3          CULTBIT
# DAPBOOLS                      FLGWRD13
# DBSELFLG      206             BIT  4 FLAG 13          DBSELECT
# DESIGFLG      185             BIT 10 FLAG 12          DESIGBIT
# DIDFLAG       016             BIT 14 FLAG             DIDFLBIT
# DIMOFLAG      059             BIT  1 FLAG  3          DIMOBIT
# DMENFLG       081             BIT  9 FLAG  5          DMENFBIT
# DRIFTDFL      202             BIT  8 FLAG 13          DRIFTBIT
# DRIFTFLG      030             BIT 15 FLAG  2          DRFTBIT
# DSKYFLAG      075             BIT 15 FLAG  5          DSKYFBIT
# Page 62
# D6OR9FLG      058             BIT  2 FLAG  3          D6OR9BIT
# ENGONFLG      083             BIT  7 FLAG  5          ENGONBIT
# ERADFLAG      017             BIT 13 FLAG  1          ERADFBIT
# ETPIFLAG      038             BIT  7 FLAG  2          ETPIBIT         EQUIVALENT FLAG NAME: DPTNSW
# FINALFLG      039             BIT  6 FLAG  2          FINALBIT
# FLAGWRD0      (000-014)       (STATE +0)
# FLAGWRD1      (015-029)       (STATE +1)
# FLAGWRD2      (030-044)       (STATE +2)
# FLAGWRD3      (045-059)       (STATE +3)
# FLAGWRD4      (060-074)       (STATE +4)
# FLAGWRD5      (075-089)       (STATE +5)
# FLAGWRD6      (090-104)       (STATE +6)
# FLAGWRD7      (105-119)       (STATE +7)
# FLAGWRD8      (120-134)       (STATE +8D)
# FLAGWRD9      (135-149)       (STATE +9D)
# FLAP          142             BIT  8 FLAG  9          FLAPBIT
# FLGWRD10      (150-164)       (STATE +10D)
# FLGWRD11      (165-179)       (STATE +11D)
# FLGWRD12      (180-194)       (STATE +12D)
# FLGWRD13      (195-209)       (STATE +13D)
# FLPC          138             BIT 12 FLAG  9          FLPCBIT
# FLPI          139             BIT 11 FLAG  9          FLPIBIT
# FLRCS         149             BIT 10 FLAG  9          FLRCSBIT
# FLUNDISP      125             BIT 10 FLAG  8          FLUNDBIT
# FLVR          136             BIT 14 FLAG  9          FLVRBIT
# FREEFLAG      012             BIT  3 FLAG  0          FREEFBIT
# FSPASFLG      005             BIT 10 FLAG  0          FSPASBIT
# GLOKFAIL      046             BIT 14 FLAG  3          GLOKFBIT
# GMBDRVSW      095             BIT 10 FLAG  6          GMBDRBIT
# GUESSW        028             BIT  2 FLAG  1          GUESSBIT
# HFLSHFLG      179             BIT  1 FLAG 11          HFLSHBIT
# IDLEFLAG      113             BIT  7 FLAG  7          IDLEFBIT
# IGNFLAG       107             BIT 13 FLAG  7          IGNFLBIT
# IMPULSW       036             BIT  9 FLAG  2          IMPULBIT
# IMUSE         007             BIT  8 FLAG  0          IMUSEBIT
# INFINFLG      128             BIT  7 FLAG  8          INFINBIT
# INITALGN      133             BIT  2 FLAG  8          INITABIT
# INTFLAG       151             BIT 14 FLAG 10          INTFLBIT
# INTYPFLG      056             BIT  4 FLAG  3          INTYPBIT
# ITSWICH       105             BIT 15 FLAG  7          ITSWBIT
# JSWITCH       001             BIT 14 FLAG  0          JSWCHBIT
# LETABORT      141             BIT  9 FLAG  9          LETABBIT
# LMOONFLG      124             BIT 11 FLAG  8          LMOONBIT
# LOKONSW       010             BIT  5 FLAG  0          LOKONBIT
# LOSCMFLG      033             BIT 12 FLAG  2          LOSCMBIT
# LRALTFLG      190             BIT  5 FLAG 12          LRALTBIT
# LRBYPASS      165             BIT 15 FLAG 11          LRBYBIT
# LRINH         172             BIT  8 FLAG 11          LRINHBIT
# LRPOSFLG      189             BIT  6 FLAG 12          LRPOSBIT
# LRVELFLG      187             BIT  8 FLAG 12          LRVELBIT
# Page63
# LUNAFLAG      048             BIT 12 FLAG  3          LUNABIT
# MANUFLAG      106             BIT 14 FLAG  7          MANUFBIT
# MGLVFLAG      088             BIT  2 FLAG  5          MGLVFBIT
# MIDAVFLG      148             BIT  2 FLAG  9          MIDAVBIT
# MIDFLAG       002             BIT 13 FLAG  0          MIDFLBIT
# MID1FLAG      147             BIT  3 FLAG  9          MID1BIT
# MKOVFLAG      072             BIT  3 FLAG  4          MKOVBIT
# MOONFLAG      003             BIT 12 FLAG  0          MOONBIT
# MRKIDFLG      060             BIT 15 FLAG  4          MRKIDBIT
# MRKNVFLG      066             BIT  9 FLAG  4          MRKNVBIT
# MRUPTFLG      070             BIT  5 FLAG  4          MRUPTBIT
# MUNFLAG       097             BIT  8 FLAG  6          MUNFLBIT
# MWAITFLG      064             BIT 11 FLAG  4          MWAITBIT
# NEEDLFLG      011             BIT  4 FLAG  0          NEEDLBIT
# NEWIFLG       122             BIT 13 FLAG  8          NEWIBIT
# NJETSFLG      015             BIT 15 FLAG             NJETSBIT
# NODOFLAG      044             BIT  1 FLAG  2          NODOBIT
# NOLRREAD      170             BIT 10 FLAG 11          NOLRRBIT
# NORMSW        110             BIT 10 FLAG  7          NORMSBIT
# NORRMON       086             BIT  4 FLAG  5          NORRMBIT
# NOR29FLG      049             BIT 11 FLAG  3          NR29FBIT
# NOTHROTL      078             BIT 12 FLAG  5          NOTHRBIT
# NOUPFLAG      024             BIT  6 FLAG  1          NOUPFBIT
# NRMNVFLG      067             BIT  8 FLAG  4          NRMNVBIT
# NRMIDFLG      062             BIT 13 FLAG  4          NRMIDBIT
# NRUPTFLG      071             BIT  4 FLAG  4          NRUPTBIT
# NTARGFLG      102             BIT  3 FLAG  6          NTARGBIT
# NWAITFLG      065             BIT 10 FLAG  4          NWAITBIT
# OLDESFLG      014             BIT  1 FLAG  0          OLDESBIT
# OPTNSW        038             BIT  7 FLAG  2          OPTNBIT         EQUIVALENT FLAG NAME: ETPIFLAG
# ORBWFLAG      054             BIT  6 FLAG  3          ORBWFBIT
# ORDERSW       129             BIT  6 FLAG  8          ORDERBIT
# OURRCFLG      198             BIT 12 FLAG 13          OURRCBIT
# PDSPFLAG      063             BIT 12 FLAG  4          PDSPFBIT
# PFRATFLG      041             BIT  4 FLAG  2          PFRATBIT
# PINBRFLG      069             BIT  6 FLAG  4          PINBRBIT
# PRECIFLG      052             BIT  8 FLAG  3          PRECIBIT
# PRIODFLG      061             BIT 14 FLAG  1          PRIODBIT
# PRONVFLG      068             BIT  7 FLAG  4          PRONVBIT
# PSTHIGAT      169             BIT 11 FLAG 11          PSTHIBIT
# PULSEFLG      195             BIT 15 FLAG 13          PULSES
# P21FLAG       004             BIT 11 FLAG  0          P21FLBIT
# P25FLAG       006             BIT  9 FLAG  0          P25FLBIT
# P39/79SW      126             BIT  9 FLAG  8          P39SWBIT
# QUITFLAG      145             BIT 5 FLAG 9            QUITBIT
# RADMODES                      FLGWRD12
# RASFLAG                       FLGWRD10
# RCDUFAIL      188             BIT  7 FLAG 12          RCDUFBIT
# RCDU0FLG      182             BIT 13 FLAG 12          RCDU0BIT
# READLR        174             BIT  6 FLAG 11          READLBIT
# Page 64
# READRFLG      051             BIT  9 FLAG  3          READRBIT        EQUIVALENT FLAG NAME FOR R04FLAG
# READVEL       175             BIT  5 FLAG 11          READVBIT
# REDFLAG       099             BIT  6 FLAG  6          REDFLBIT
# REFSMFLG      047             BIT 13 FLAG  3          REFSMBIT
# REINTFLG      158             BIT  7 FLAG 10          REINTBIT
# REMODFLG      181             BIT 14 FLAG 12          REMODBIT
# RENDWFLG      089             BIT  1 FLAG  5          RENDWBIT
# REPOSMON      184             BIT 11 FLAG 12          REPOSBIT
# RHCSCFLG      203             BIT  7 FLAG 13          RHCSCALE
# RNDVZFLG      008             BIT  7 FLAG  0          RNDVZBIT
# RNGEDATA      176             BIT  4 FLAG 11          RNGEDBIT
# RNGSCFLG      080             BIT 10 FLAG  5          RNGSCBIT
# RODFLAG       018             BIT 12 FLAG  1          RODFLBIT
# ROTFLAG       144             BIT  6 FLAG  9          ROTFLBIT
# RPQFLAG       120             BIT 15 FLAG  8          RPQFLBIT
# RRDATAFL      191             BIT  4 FLAG 12          RRDATABT
# RRNBSW        009             BIT  6 FLAG  0          RRNBBIT
# RRRSFLAG      192             BIT  3 FLAG 12          RRRSBIT
# RVSW          111             BIT  9 FLAG  7          RVSWBIT
# R04FLAG       051             BIT  9 FLAG  3          R04FLBIT        EQUIVALENT FLAG NAME:  READRFLG
# R10FLAG       013             BIT  2 FLAG  0          R10FLBIT
# R61FLAG       020             BIT 10 FLAG  1          R61FLBIT
# R77FLAG       079             BIT 11 FLAG  5          R77FLBIT
# SCALBAD       177             BIT  3 FLAG 11          SCABBIT
# SLOPESW       027             BIT  3 FLAG  1          SLOPEBIT
# SNUFFER       077             BIT 13 FLAG  5          SNUFFBIT
# SOLNSW        087             BIT  3 FLAG  5          SOLNSBIT
# SRCHOPTN      031             BIT 14 FLAG  2          SRCHOBIT
# STATEFLG      055             BIT  5 FLAG  3          STATEBIT
# STEERSW       034             BIT 11 FLAG  2          STEERBIT
# SURFFLAG      127             BIT  8 FLAG  8          SURFFBIT
# SWANDISP      109             BIT 11 FLAG  7          SWANDBIT
# S32.1F1       090             BIT 15 FLAG  6          S32BIT1
# S32.1F2       091             BIT 14 FLAG  6          S32BIT2
# S32.1F3A      092             BIT 13 FLAG  6          S32BIT3A
# S32.1F3B      093             BIT 12 FLAG  6          S32BIT3B
# TFFSW         119             BIT  1 FLAG  7          TFFSWBIT
# TRACKFLG      025             BIT  5 FLAG  1          TRACKBIT
# TURNONFL      194             BIT  1 FLAG 12          TURNONBT
# ULLAGFLG      204             BIT  6 FLAG 13          ULLAGER
# UPDATFLG      023             BIT  7 FLAG  1          UPDATBIT
# UPLOCKFL      116             BIT  4 FLAG 7           UPLOCBIT
# USEQRFLG      196             BIT 14 FLAG 13          USEQRJTS
# VEHUPFLG      022             BIT  8 FLAG  1          VEHUPBIT
# VELDATA       173             BIT  7 FLAG 11          VELDABIT
# VERIFLAG      117             BIT  3 FLAG  7          VERIFBIT
# VFLAG         050             BIT 10 FLAG  3          VFLAGBIT
# VFLSHFLG      178             BIT  2 FLAG 11          VFLSHBIT
# VINTFLAG      057             BIT  3 FLAG  3          VINTFBIT
# VXINH         168             BIT 12 FLAG 11          VXINHBIT
# Page 65
# V37FLAG       114             BIT  6 FLAG  7          V37FLBIT
# V67FLAG       112             BIT  8 FLAG  7          V67FLBIT
# V82EMFLG      118             BIT  2 FLAG  7          V82EMBIT
# XDELVFLG      037             BIT  8 FLAG  2          XDELVBIT
# XDSPFLAG      074             BIT  1 FLAG  4          XDSPBIT
# XORFLG        171             BIT  9 FLAG 11          XORFLBIT
# XOVINFLG      201             BIT  9 FLAG 13          XOVINHIB
# 3AXISFLG      084             BIT  6 FLAG  5          3AXISBIT
# 360SW         134             BIT  1 FLAG  8          360SWBIT

# ASSIGNMENT AND DESCRIPTION OF FLAGWORDS

S('FLAGWRD0', 'equals', 0o74, line=240)  # (000-014)

# (SET)                   (RESET)

# BIT 15 FLAG 0 (S)
#   = 000D
#   = BIT15

# BIT 14 FLAG 0 (S)
S('JSWITCH', 'equals', 0o1, line=249)  #       INTEGRATION OF W        INTEGRATION OF STATE
S('JSWCHBIT', 'equals', 0o4736, line=250)  #       MATRIX                  VECTOR

# BIT 13 FLAG 0 (S)
S('MIDFLAG', 'equals', 0o2, line=253)  #       INTEGRATION WITH        INTEGRATION WITHOUT
# SECONDARY BODY AND      SOLAR PERTURBATIONS
S('MIDFLBIT', 'equals', 0o4737, line=255)  #       SOLAR PERTURBATIONS

# BIT 12 FLAG 0 (L)
S('MOONFLAG', 'equals', 0o3, line=258)  #       MOON IS SPHERE OF       EARTH IS SPHERE OF
S('MOONBIT', 'equals', 0o4740, line=259)  #       INFLUENCE               INFLUENCE

# BIT 11 FLAG 0
S('P21FLAG', 'equals', 0o4, line=262)  #       USE BASE VECTORS        1ST PASS -- CALC-
S('P21FLBIT', 'equals', 0o4741, line=263)  #       ALREADY CALCULATED      ULATE BASE VECTORS

# BIT 10 FLAG 0
S('FSPASFLG', 'equals', 0o5, line=266)  #       FIRST PASS THROUGH      NOT FIRST PASS THRU
S('FSPASBIT', 'equals', 0o4742, line=267)  #       REPOSITION ROUTINE      REPOSITION ROUTINE

# Page 66
# BIT 9 FLAG 0  (S)
S('P25FLAG', 'equals', 0o6, line=271)  #       P25 OPERATING           P25 NOT OPERATING
S('P25FLBIT', 'equals', 0o4743, line=272)

# BIT 8 FLAG 0  (S)
S('IMUSE', 'equals', 0o7, line=275)  #       IMU IN USE              IMU NOT IN USE
S('IMUSEBIT', 'equals', 0o4744, line=276)

# BIT 7 FLAG 0  (S)
S('RNDVZFLG', 'equals', 0o10, line=279)  #       P20 RUNNING (RADAR      P20 NOT RUNNING
S('RNDVZBIT', 'equals', 0o4745, line=280)  #       IN USE)

# BIT 6 FLAG 0  (S)
S('RRNBSW', 'equals', 0o11, line=283)  #       RADAR TARGET IN         RADAR TARGET IN
S('RRNBBIT', 'equals', 0o4746, line=284)  #       NB COORDINATES          SM COORDINATES

# BIT 5 FLAG 0  (S)
S('LOKONSW', 'equals', 0o12, line=287)  #       RADAR LOCK-ON           RADAR LOCK-ON NOT
S('LOKONBIT', 'equals', 0o4747, line=288)  #       DESIRED                 DESIRED

# BIT 4 FLAG 0  (S)
S('NEEDLFLG', 'equals', 0o13, line=291)  #       TOTAL ATTITUDE          A/P FOLLOWING
S('NEEDLBIT', 'equals', 0o4750, line=292)  #       ERROR DISPLAYED         ERROR DISPLAYED

# BIT 3 FLAG 0
S('FREEFLAG', 'equals', 0o14, line=295)  # (USED BY P51-53 TEMP IN MANY DIFFERENT
# ROUTINES & BY LUNAR + SOLAR EPHEMERIDES)
S('FREEFBIT', 'equals', 0o4751, line=297)

# BIT 2 FLAG 0
S('R10FLAG', 'equals', 0o15, line=300)  #       R10 OUTPUTS DATA TO     BESIDES OUTPUT WHEN
S('R10FLBIT', 'equals', 0o4752, line=301)  #       ALTITUDE & ALTITUDE     SET, R10 ALSO OUTPUT
# RATE METERS ONLY        TO FORWARD & LATERAL
# VELOCITY CROSSPOINTER

# BIT 1 FLAG 0  (L)
S('OLDESFLG', 'equals', 0o16, line=306)  #       R29 GYRO CMD LOOP       R29 GYRO CMD LOOP
S('OLDESBIT', 'equals', 0o4753, line=307)  #       REQUESTED               NOT REQUESTED

S('FLAGWRD1', 'equals', 0o75, line=310)  # (015-029)

# Page 67
# (SET)                   (RESET)

# BIT 15 FLAG 1 (S)
S('NJETSFLG', 'equals', 0o17, line=316)  #       TWO JET RCS BURN        FOUR JET RCS BURN
S('NJETSBIT', 'equals', 0o4735, line=317)

# BIT 14 FLAG 1 (L)
S('DIDFLAG', 'equals', 0o20, line=320)  #       INERTIAL DATA IS        PERFORM DATA DISPLAY
S('DIDFLBIT', 'equals', 0o4736, line=321)  #       AVAILABLE               INITIALIZATION FUNCS

# BIT 13 FLAG 1 (S)
S('ERADFLAG', 'equals', 0o21, line=324)  #       COMPUTE REARTH          USE CONSTANT REARTH
S('ERADFBIT', 'equals', 0o4737, line=325)  #       FISCHER ELLIPSOID       PAD RADIUS

# BIT 12 FLAG 1
S('RODFLAG', 'equals', 0o22, line=328)  #       IF IN P66, NORMAL       IF IN P66, RE-INIT-
S('RODFLBIT', 'equals', 0o4740, line=329)  #       OPERATION CONTINUES.    IALIZATION IS PER-
# RESTART CLEARS FLAG     FORMED AND FLAG IS

# BIT 11 FLAG 1
#   = 019D
#   = BIT11

# BIT 10 FLAG 1 (L)
S('R61FLAG', 'equals', 0o24, line=337)  #       RUN R61 LEM             RUN R65 LEM
S('R61FLBIT', 'equals', 0o4742, line=338)

# BIT 9 FLAG 1
#   = 021D
#   = BIT9

# BIT 8 FLAG 1  (S)
S('VEHUPFLG', 'equals', 0o26, line=345)  #       CSM STATE-VECTOR        LEM STATE VECTOR
S('VEHUPBIT', 'equals', 0o4744, line=346)  #       BEING UPDATED           BEING UPDATED

# BIT 7 FLAG 1  (S)
S('UPDATFLG', 'equals', 0o27, line=349)  #       UPDATING BY MARKS       UPDATING BY MARKS
S('UPDATBIT', 'equals', 0o4745, line=350)  #       ALLOWED                 NOT ALLOWED

# BIT 6 FLAG 1  (S)
S('NOUPFLAG', 'equals', 0o30, line=353)  #       NEITHER CSM             EITHER STATE
# NOR LM STATE VECTOR     VECTOR MAY BE
S('NOUPFBIT', 'equals', 0o4746, line=355)  #       MAY BE UPDATED          UPDATED

# Page 68
# BIT 5 FLAG 1  (S)
S('TRACKFLG', 'equals', 0o31, line=359)  #       TRACKING ALLOWED        TRACKING NOT ALLOWED
S('TRACKBIT', 'equals', 0o4747, line=360)

# BIT 4 FLAG 1
#   = 026D
#   = BIT4

# BIT 3 FLAG 1  (S)
S('SLOPESW', 'equals', 0o33, line=367)  #       ITERATE WITH BIAS       ITERATE WITH REGULAR
# METHOD IN ITERATOR      FALSI METHOD IN
S('SLOPEBIT', 'equals', 0o4751, line=369)  #                               ITERATOR

# BIT 2 FLAG 1  (S)
S('GUESSW', 'equals', 0o34, line=372)  #       NO STARTING VALUE       STARTING VALUE FOR
S('GUESSBIT', 'equals', 0o4752, line=373)  #       FOR ITERATION           ITERATION EXISTS

# BIT 1 FLAG 1
#   = 029D
#   = BIT1  # OH 2009-05-15 Scan does not have this line

S('FLAGWRD2', 'equals', 0o76, line=379)  # (030-044)

# (SET)                   (RESET)

# BIT 15 FLAG 2 (S)
S('DRIFTFLG', 'equals', 0o36, line=384)  #       T3RUPT CALLS GYRO       T3RUPT DOES NO GYRO
S('DRFTBIT', 'equals', 0o4735, line=385)  #       COMPENSATION            COMPENSATION

# BIT 14 FLAG 2 (S)
S('SRCHOPTN', 'equals', 0o37, line=388)  #       RADAR IN AUTOMATIC      RADAR NOT IN AUTO-
S('SRCHOBIT', 'equals', 0o4736, line=389)  #       SEARCH OPTION (R24)     MATIC SEARCH OPTION

# BIT 13 FLAG 2 (S)
S('ACMODFLG', 'equals', 0o40, line=392)  #       MANUAL ACQUISITION      AUTO ACQUISITION
S('ACMODBIT', 'equals', 0o4737, line=393)  #       BY RENDEZVOUS RADAR     BY RENDEZVOUS RADAR

# BIT 12 FLAG 2 (S)
S('LOSCMFLG', 'equals', 0o41, line=396)  #       LINE OF SIGHT BEING     LINE OF SIGHT NOT
# COMPUTED (R21)          BEING COMPUTED
S('LOSCMBIT', 'equals', 0o4740, line=398)

# Page 69
# BIT 11 FLAG 2 (S)
S('STEERSW', 'equals', 0o42, line=402)  #       SUFFICIENT THRUST       INSUFFICIENT THRUST
S('STEERBIT', 'equals', 0o4741, line=403)  #       IS PRESENT              IS PRESENT

# BIT 10 FLAG 2 (S)
#   = 035D  # OH 2009-05-15 These two line don't appear in scan
#   = BIT10

# BIT 9 FLAG 2 (S)
S('IMPULSW', 'equals', 0o44, line=410)  #       MINIMUM IMPULSE         STEERING BURN (NO
# BURN (CUTOFF TIME       CUTOFF TIME YET
S('IMPULBIT', 'equals', 0o4743, line=412)  #       SPECIFIED)              AVAILABLE)

# BIT 8 FLAG 2 (S)
S('XDELVFLG', 'equals', 0o45, line=415)  #       EXTERNAL DELTAV VG      LAMBERT (AIMPOINT)
S('XDELVBIT', 'equals', 0o4744, line=416)  #       COMPUTATION             VG COMPUTATION

# BIT 7 FLAG 2 (S)
S('ETPIFLAG', 'equals', 0o46, line=419)  #       ELEVATION ANGLE         TPI TIME SUPPLIED
# SUPPLIED FOR            FOR P34,74 TO COMPUTE
S('ETPIBIT', 'equals', 0o4745, line=421)  #       P34,74                  ELEVATION

# BIT 7 FLAG 2 (L)
S('OPTNSW', 'equals', 0o46, line=424)  #       SOI PHASE OF P38/78     SOR PHASE OF P38/78
S('OPTNBIT', 'equals', 0o4745, line=425)

# BIT 6 FLAG 2 (S)
S('FINALFLG', 'equals', 0o47, line=428)  #       LAST PASS THROUGH       INTERIM PASS THROUGH
# RENDEZVOUS PROGRAM      RENDEZVOUS PROGRAM
S('FINALBIT', 'equals', 0o4746, line=430)  #       COMPUTATIONS            COMPUTATIONS

# BIT 5 FLAG 2 (S)
S('AVFLAG', 'equals', 0o50, line=433)  #       LEM IS ACTIVE           CSM IS ACTIVE
S('AVFLBIT', 'equals', 0o4747, line=434)  #       VEHICLE                 VEHICLE

# BIT 4 FLAG 2 (S)
S('PFRATFLG', 'equals', 0o51, line=437)  #       PREFERRED ATTITUDE      PREFERRED ATTITUDE
S('PFRATBIT', 'equals', 0o4750, line=438)  #       COMPUTED                NOT COMPUTED

# BIT 3 FLAG 2 (S)

# Page 70
S('CALCMAN3', 'equals', 0o52, line=443)  #       NO FINAL ROLL           FINAL ROLL IS
S('CALC3BIT', 'equals', 0o4751, line=444)  #                               NECESSARY

# BIT 2 FLAG 2 (S)
S('CALCMAN2', 'equals', 0o53, line=447)  #       PERFORM MANEUVER        BYPASS STARTING
S('CALC2BIT', 'equals', 0o4752, line=448)  #       STARTING PROCEDURE      PROCEDURE

# BIT 1 FLAG 2 (S)
S('NODOFLAG', 'equals', 0o54, line=451)  #       V37 NOT PERMITTED       V37 PERMITTED
S('NODOBIT', 'equals', 0o4753, line=452)

S('FLAGWRD3', 'equals', 0o77, line=454)  # (045-059)

# (SET)                   (RESET)

# BIT 15 FLAG 3
#   = 045D
#   = BIT15  # OH 2009-05-15 This line is not in scans

# BIT 14 FLAG 3 (S)
S('GLOKFAIL', 'equals', 0o56, line=463)  #       GIMBAL LOCK HAS         NOT IN GIMBAL LOCK
S('GLOKFBIT', 'equals', 0o4736, line=464)  #       OCCURRED

# BIT 13 FLAG 3 *** PROTECTED FROM FRESH START ***
S('REFSMFLG', 'equals', 0o57, line=467)  #       REFSMMAT GOOD           REFSMMAT NO GOOD
S('REFSMBIT', 'equals', 0o4737, line=468)

# BIT 12 FLAG 3 (S)
S('LUNAFLAG', 'equals', 0o60, line=471)  #       LUNAR LAT-LONG          EARTH LAT-LONG
S('LUNABIT', 'equals', 0o4740, line=472)

# BIT 11 FLAG 3 (L)
S('NOR29FLG', 'equals', 0o61, line=475)  #       R29 NOT ALLOWED         R29 ALLOWED (RR DES-
S('NR29FBIT', 'equals', 0o4741, line=476)  #                               IGNATED POWERED FLT)

# BIT 10 FLAG 3 (S)
S('VFLAG', 'equals', 0o62, line=479)  #       LESS THAN TWO STARS     TWO STARS IN FIELD
S('VFLAGBIT', 'equals', 0o4742, line=480)  #       IN FIELD OF VIEW        OF VIEW

# BIT 9 FLAG 3  (S)
S('R04FLAG', 'equals', 0o63, line=483)  #       ALARM 521               ALARM 521 ALLOWED
# SUPPRESSED
# Page 71
S('R04FLBIT', 'equals', 0o4743, line=486)

# BIT 9 FLAG 3  (L)
S('READRFLG', 'equals', 0o63, line=489)  #       READING RR DATA         NOT READING RR DATA
S('READRBIT', 'equals', 0o4743, line=490)  #       PURSUANT TO R29         PURSUANT TO R29

# BIT 8 FLAG 3  (S)
S('PRECIFLG', 'equals', 0o64, line=493)  #       NORMAL INTEGRATION      ENGAGES 4-TIME STEP
# IN P00                  (P00) LOGIC IN INTE-
S('PRECIBIT', 'equals', 0o4744, line=495)  #                               GRATION

# BIT 7 FLAG 3  (S)
S('CULTFLAG', 'equals', 0o65, line=498)  #       STAR OCCULTED           STAR NOT OCCULTED
S('CULTBIT', 'equals', 0o4745, line=499)

# BIT 6 FLAG 3  (S)
S('ORBWFLAG', 'equals', 0o66, line=502)  #       W MATRIX VALID FOR      W MATRIX INVALID FOR
S('ORBWFBIT', 'equals', 0o4746, line=503)  #       ORBITAL NAVIGATION      ORBITAL NAVIGATION

# BIT 5 FLAG 3  (S)
S('STATEFLG', 'equals', 0o67, line=506)  #       PERMANENT STATE         PERMANENT STATE
S('STATEBIT', 'equals', 0o4747, line=507)  #       VECTOR UPDATED          VECTOR NOT UPDATED

# BIT 4 FLAG 3  (S)
S('INTYPFLG', 'equals', 0o70, line=510)  #       CONIC INTEGRATION       ENCKE INTEGRATION
S('INTYPBIT', 'equals', 0o4750, line=511)

# BIT 3 FLAG 3  (S)
S('VINTFLAG', 'equals', 0o71, line=514)  #       CSM STATE VECTOR        LEM STATE VECTOR
S('VINTFBIT', 'equals', 0o4751, line=515)  #       BEING INTEGRATED        BEING INTEGRATED

# BIT 2 FLAG 3 (S)
S('D6OR9FLG', 'equals', 0o72, line=518)  #       DIMENSION OF W IS 9     DIMENSION OF W IS 6
S('D6OR9BIT', 'equals', 0o4752, line=519)  #       FOR INTEGRATION         FOR INTEGRATION

# BIT 1 FLAG 3  (S)
S('DIM0FLAG', 'equals', 0o73, line=522)  #       W MATRIX IS TO BE       W MATRIX IS NOT TO
S('DIM0BIT', 'equals', 0o4753, line=523)  #       USED                    USED

S('FLAGWRD4', 'equals', 0o100, line=525)  # (060-074)

# Page 72
# (SET)                   (RESET)

# BIT 15 FLAG 4 (S)
S('MRKIDFLG', 'equals', 0o74, line=531)  #       MARK DISPLAY IN         NO MARK DISPLAY IN
S('MRKIDBIT', 'equals', 0o4735, line=532)  #       ENDIDLE                 ENDIDLE

# BIT 14 FLAG 4 (S)
S('PRIODFLG', 'equals', 0o75, line=535)  #       PRIORITY DISPLAY IN     NO PRIORITY DISPLAY
S('PRIODBIT', 'equals', 0o4736, line=536)  #       ENDIDLE                 IN ENDIDLE

# BIT 13 FLAG 4 (S)
S('NRMIDFLG', 'equals', 0o76, line=539)  #       NORMAL DISPLAY IN       NO NORMAL DISPLAY
S('NRMIDBIT', 'equals', 0o4737, line=540)  #       ENDIDLE                 IN ENDIDLE

# BIT 12 FLAG 4 (S)
S('PDSPFLAG', 'equals', 0o77, line=543)  #       P20 SETS SO AS TO       LEAVE AS NORMAL DISP
# TURN A NORMAL DIS-
S('PDSPFBIT', 'equals', 0o4740, line=545)  #       PLAY INTO A PRIORITY
# DISPLAY IN R60

# BIT 11 FLAG 4 (S)
S('MWAITFLG', 'equals', 0o100, line=549)  #       HIGHER PRIORITY         NO HIGHER PRIORITY
# DISPLAY OPERATING       DISPLAY OPERATING
S('MWAITBIT', 'equals', 0o4741, line=551)  #       WHEN MARK               WHEN MARK DISPLAY
# DISPLAY INITIATED       INITIATED

# BIT 10 FLAG 4 (S)
S('NWAITFLG', 'equals', 0o101, line=555)  #       HIGHER PRIORITY         NO HIGHER PRIORITY
# DISPLAY OPERATING       DISPLAY OPERATING
S('NWAITBIT', 'equals', 0o4742, line=557)  #       WHEN NORMAL             WHEN NORMAL DISPLAY
# DISPLAY INITIATED       INITIATED

# BIT 9 FLAG 4  (S)
S('MRKNVFLG', 'equals', 0o102, line=561)  #       ASTRONAUT USING         ASTRONAUT NOT USING
# KEYBOARD WHEN MARK      KEYBOARD WHEN MARK
S('MRKNVBIT', 'equals', 0o4743, line=563)  #       DISPLAY INITIATED       DISPLAY INITIATED

# BIT 8 FLAG 4  (S)
S('NRMNVFLG', 'equals', 0o103, line=566)  #       ASTRONAUT USING         ASTRONAUT NOT USING
# KEYBOARD WHEN           KEYBOARD WHEN
S('NRMNVBIT', 'equals', 0o4744, line=568)  #       NORMAL DISPLAY          NORMAL DISPLAY
# INITIATED               INITIATED

# BIT 7 FLAG 4  (S)
S('PRONVFLG', 'equals', 0o104, line=572)  #       ASTRONAUT USING         ASTRONAUT NOT USING

# Page 73
# KEYBOARD WHEN           KEYBOARD WHEN
S('PRONVBIT', 'equals', 0o4745, line=576)  #       PRIORITY DISPLAY        PRIORITY DISPLAY
# INITIATED               INITIATED

# BIT 6 FLAG 4  (S)
S('PINBRFLG', 'equals', 0o105, line=580)  #       ASTRONAUT HAS           ASTRONAUT HAS NOT
# INTERFERED WITH         INTERFERED WITH
S('PINBRBIT', 'equals', 0o4746, line=582)  #       EXISTING DISPLAY        EXISTING DISPLAY

# BIT 5 FLAG 4  (S)
S('MRUPTFLG', 'equals', 0o106, line=585)  #       MARK DISPLAY            MARK DISPLAY NOT
# INTERRUPTED BY          INTERRUPTED BY
S('MRUPTBIT', 'equals', 0o4747, line=587)  #       PRIORITY DISPLAY        PRIORITY DISPLAY

# BIT 4 FLAG 4  (S)
S('NRUPTFLG', 'equals', 0o107, line=590)  #       NORMAL DISPLAY          NORMAL DISPLAY NOT
# INTERRUPTED BY          INTERRUPTED BY
S('NRUPTBIT', 'equals', 0o4750, line=592)  #       PRIORITY OR MARK        PRIORITY OR MARK
# DISPLAY                 DISPLAY

# BIT 3 FLAG 4  (S)
S('MKOVFLAG', 'equals', 0o110, line=596)  #       MARK DISPLAY OVER       NO MARK DISPLAY OVER
S('MKOVBIT', 'equals', 0o4751, line=597)  #       NORMAL                  NORMAL

# BIT 2 FLAG 4
#   = 073D
#   = BIT2  # OH 2009-05-15 Not in scan.

# BIT 1 FLAG 4  (S)
S('XDSPFLAG', 'equals', 0o112, line=605)  #       MARK DISPLAY NOT        NO SPECIAL MARK
S('XDSPBIT', 'equals', 0o4753, line=606)  #       TO BE INTERRUPTED       INFORMATION

S('FLAGWRD5', 'equals', 0o101, line=608)  # (075-089)

# (SET)                   (RESET)

# BIT 15 FLAG 5 (S)
S('DSKYFLAG', 'equals', 0o113, line=613)  #       DISPLAYS SENT TO        NO DISPLAYS TO DSKY
S('DSKYFBIT', 'equals', 0o4735, line=614)  #       DSKY

# BIT 14 FLAG 5
#   = 076D
#   = BIT14

# Page 74
# BIT 13 FLAG 5 (S,L)
S('SNUFFER', 'equals', 0o115, line=622)  #       U,V JETS DISABLED       U,V JETS ENABLED
# DURING DPS              DURING DPS
S('SNUFFBIT', 'equals', 0o4737, line=624)  #       BURNS (V65)             BURNS (V75)

# BIT 12 FLAG 5 (S)
S('NOTHROTL', 'equals', 0o116, line=627)  #       INHIBIT FULL            PERMIT FULL THROTTLE
S('NOTHRBIT', 'equals', 0o4740, line=628)  #       THROTTLE

# BIT 11 FLAG 5 (S,L)
S('R77FLAG', 'equals', 0o117, line=631)  #       R77 IS ON,              R77 IS NOT ON.
# SUPPRESS ALL RADAR
# ALARMS AND TRACKER
S('R77FLBIT', 'equals', 0o4741, line=634)  #       FAILS

# BIT 10 FLAG 5 (S)
S('RNGSCFLG', 'equals', 0o120, line=637)  #       SCALE CHANGE HAS        NO SCALE CHANGE HAS
# OCCURRED DURING         OCCURRED DURING
S('RNGSCBIT', 'equals', 0o4742, line=639)  #       RR READING              RR READING

# BIT 9 FLAG 5  (S)
S('DMENFLG', 'equals', 0o121, line=642)  #       DIMENSION OF W IS 9     DIMENSION OF W IS 6
S('DMENFBIT', 'equals', 0o4743, line=643)  #       FOR INCORPORATION       FOR INCORPORATION

# BIT 8 FLAG 5  (S)
#   = 082D
#   = BIT8

# BIT 7 FLAG 5  (S)
S('ENGONFLG', 'equals', 0o123, line=650)  #       ENGINE TURNED ON        ENGINE TURNED OFF
S('ENGONBIT', 'equals', 0o4745, line=651)

# BIT 6 FLAG 5  (S)
S('3AXISFLG', 'equals', 0o124, line=654)  #       MANEUVER SPECIFIED      MANEUVER SPECIFIED
# BY THREE AXES           BY ONE AXIS; R60
S('3AXISBIT', 'equals', 0o4746, line=656)  #                               CALLS VECPOINT.

# BIT 5 FLAG 5
#   = 085D
#   = BIT5  # OH 2009-05-15 Not in scan

# BIT 4 FLAG 5  (S)

# Page 75
S('NORRMON', 'equals', 0o126, line=665)  #       BYPASS RR GIMBAL        PERFORM
S('NORRMBIT', 'equals', 0o4750, line=666)  #       MONITOR                 RR GIMBAL MONITOR

# BIT 3 FLAG 5  (S)
S('SOLNSW', 'equals', 0o127, line=669)  #       LAMBERT DOES NOT        LAMBERT CONVERGES OR
# CONVERGE, OR TIME-RAD   TIME-RADIUS NON-
S('SOLNSBIT', 'equals', 0o4751, line=671)  #       NEARLY CIRCULAR         CIRCULAR

# BIT 2 FLAG 5  (S)
S('MGLVFLAG', 'equals', 0o130, line=674)  #       LOCAL VERTICAL          MIDDLE GIMBAL ANGLE
# COORDINATES             COMPUTED
S('MGLVFBIT', 'equals', 0o4752, line=676)  #       COMPUTED

# BIT 1 FLAG 5  (S)
S('RENDWFLG', 'equals', 0o131, line=679)  #       W MATRIX VALID          W MATRIX INVALID
# FOR RENDEZVOUS          FOR RENDEZVOUS
S('RENDWBIT', 'equals', 0o4753, line=681)  #       NAVIGATION              NAVIGATION

S('FLAGWRD6', 'equals', 0o102, line=684)  # (090-104)

# (SET)                   (RESET)

# BIT 15 FLAG 6 (S)
S('S32.1F1', 'equals', 0o132, line=689)  #       DELTA V AT CSI TIME     DVT1 LESS THAN MAX
S('S32BIT1', 'equals', 0o4735, line=690)  #       ONE EXCEEDS MAX

# BIT 14 FLAG 6 (S)
S('S32.1F2', 'equals', 0o133, line=693)  #       FIRST PASS OF           REITERATION OF
S('S32BIT2', 'equals', 0o4736, line=694)  #       NEWTON ITERATION        NEWTON

# BIT 13 FLAG 6 (S)
S('S32.1F3A', 'equals', 0o134, line=697)  # BIT 13 AND BIT 12 FUNCTION AS AN ORDERED
S('S32BIT3A', 'equals', 0o4737, line=698)  # PAIR (13,12) INDICATING THE POSSIBLE OC-
# CURRENCE OF 2 NEWTON ITERATIONS FOR S32.1
# IN THE PROGRAM IN THE FOLLOWING ORDER:
# BIT 12 FLAG 6 (S)                             # (0,1) (I.E. BIT 13 RESET, BIT 12 SET)
S('S32.1F3B', 'equals', 0o135, line=702)  #      = FIRST NEWTON ITERATION BEING DONE
S('S32BIT3B', 'equals', 0o4740, line=703)  # (0,0)= FIRST PASS OF SECOND NEWTON ITERATION
# (1,1)= 50 FT/SEC STAGE OF SECOND NEWTON ITERATION
# (1,0)= REMAINDER OF SECOND NEWTON ITERATION
# BIT 11 FLAG 6 (S)
#   = 094D
#   = BIT11
# Page 76
# BIT 10 FLAG 6 (S)
S('GMBDRVSW', 'equals', 0o137, line=711)  #       TRIMGIMB OVER           TRIMGIMB NOT OVER
S('GMBDRBIT', 'equals', 0o4742, line=712)

# BIT 9 FLAG 6
#   = 096D
#   = BIT9

# BIT 8 FLAG 6  (S)
S('MUNFLAG', 'equals', 0o141, line=719)  #       SERVICER CALLS          SERVICER CALLS
S('MUNFLBIT', 'equals', 0o4744, line=720)  #       MUNRVG                  CALCRVG

# BIT 7 FLAG 6  (L)
#   = 098D
#   = BIT7

# BIT 6 FLAG 6  (L)
S('REDFLAG', 'equals', 0o143, line=727)  #       LANDING SITE            LANDING SITE
# REDESIGNATION           REDESIGNATION NOT
S('REDFLBIT', 'equals', 0o4746, line=729)  #       PERMITTED               PERMITTED

# BIT 5 FLAG 6
#   = 100D
#   = BIT5  # OH 2009-05-15 Not in scan

# BIT 4 FLAG 6
#   = 101D
#   = BIT4  # OH 2009-05-15 Not in scan

# BIT 3 FLAG 6  (S)
S('NTARGFLG', 'equals', 0o146, line=740)  #       ASTRONAUT DID           ASTRONAUT DID NOT
# OVERWRITE DELTA         OVERWRITE DELTA
S('NTARGBIT', 'equals', 0o4751, line=742)  #       VELOCITY AT TPI         VELOCITY
# OR TPM (P34,35)

# BIT 2 FLAG 6
S('AUXFLAG', 'equals', 0o147, line=746)  #       PROVIDING IDLEFLAG      SERVICER WILL SKIP
S('AUXFLBIT', 'equals', 0o4752, line=747)  #       IS NOT SET, SERV-       DVMON ON ITS NEXT
# ICER WILL EXERCISE      PASS EVEN IF THE
# DVMON ON ITS NEXT       IDLEFLAG IS NOT SET.
# PASS.                   IT WILL THEN SET
# AUXFLAG.

# BIT 1 FLAG 6  (L)
S('ATTFLAG', 'equals', 0o150, line=754)  #       LEM ATTITUDE EXISTS     NO LEM ATTITUDE
# IN MOON-FIXED           AVAILABLE IN MOON-

# Page 77
S('ATTFLBIT', 'equals', 0o4753, line=758)  #       COORDINATES             FIXED COORDINATES

S('FLAGWRD7', 'equals', 0o103, line=760)  # (105-119)

# (SET)                   (RESET)

# BIT 15 FLAG 7 (S)
S('ITSWICH', 'equals', 0o151, line=765)  #       R34;TPI TIME TO BE      TPI HAS BEEN
S('ITSWBIT', 'equals', 0o4735, line=766)  #       COMPUTED                COMPUTED

# BIT 14 FLAG 7 (S)
S('MANUFLAG', 'equals', 0o152, line=769)  #       ATTITUDE MANEUVER       NO ATTITUDE MANEUVER
# GOING DURING RR         DURING RR SEARCH
S('MANUFBIT', 'equals', 0o4736, line=771)  #       SEARCH

# BIT 13 FLAG 7 (S)
S('IGNFLAG', 'equals', 0o153, line=774)  #       TIG HAS ARRIVED         TIG HAS NOT ARRIVED
S('IGNFLBIT', 'equals', 0o4737, line=775)

# BIT 12 FLAG 7 (S)
S('ASTNFLAG', 'equals', 0o154, line=778)  #       ASTRONAUT HAS           ASTRONAUT HAS NOT
S('ASTNBIT', 'equals', 0o4740, line=779)  #       OKAYED IGNITION         OKAYED IGNITION

# BIT 11 FLAG 7 (L)
S('SWANDISP', 'equals', 0o155, line=782)  #       LANDING ANALOG          LANDING ANALOG
S('SWANDBIT', 'equals', 0o4741, line=783)  #       DISPLAYS ENABLED        DISPLAYS SUPPRESSED

# BIT 10 FLAG 7 (S)
S('NORMSW', 'equals', 0o156, line=786)  #       UNIT NORMAL INPUT       LAMBERT COMPUTES ITS
S('NORMSBIT', 'equals', 0o4742, line=787)  #       TO LAMBERT              OWN UNIT NORMAL

# BIT 9 FLAG 7  (S)
S('RVSW', 'equals', 0o157, line=790)  #       DO NOT COMPUTE          COMPUTE FINAL STATE
# FINAL STATE VECTOR      VECTOR IN TIME-THETA
S('RVSWBIT', 'equals', 0o4743, line=792)  #       IN TIME-DELTA

# BIT 8 FLAG 7  (S)
S('V67FLAG', 'equals', 0o160, line=795)  #       ASTRONAUT OVERWRITE     ASTRONAUT DOES NOT
# W-MATRIX INITIAL        OVERWRITE W-MATRIX
S('V67FLBIT', 'equals', 0o4744, line=797)  #       VALUES                  INITIAL VALUES

# Page 78
# BIT 7 FLAG 7  (S)
S('IDLEFLAG', 'equals', 0o161, line=801)  #       NO DV MONITOR           CONNECT DV MONITOR
S('IDLEFBIT', 'equals', 0o4745, line=802)

# BIT 6 FLAG 7  (S)
S('V37FLAG', 'equals', 0o162, line=805)  #       AVERAGEG (SERVICER)     AVERAGEG (SERVICER)
S('V37FLBIT', 'equals', 0o4746, line=806)  #       RUNNING                 OFF

# BIT 5 FLAG 7  (S)
S('AVEGFLAG', 'equals', 0o163, line=809)  #       AVERAGEG (SERVICER)     AVERAGEG (SERVICER)
S('AVEGFBIT', 'equals', 0o4747, line=810)  #       DESIRED                 NOT DESIRED

# BIT 4 FLAG 7  (S)
S('UPLOCKFL', 'equals', 0o164, line=813)  #       K-KBAR-K FAIL           NO K-KBAR-K FAIL
S('UPLOCBIT', 'equals', 0o4750, line=814)

# BIT 3 FLAG 7  (S)
S('VERIFLAG', 'equals', 0o165, line=817)  # CHANGED WHEN V33E OCCURS AT END OF P27
S('VERIFBIT', 'equals', 0o4751, line=818)

# BIT 2 FLAG 7  (L,C)
S('V82EMFLG', 'equals', 0o166, line=821)  #       MOON VICINITY           EARTH VICINITY
S('V82EMBIT', 'equals', 0o4752, line=822)

# BIT 1 FLAG 7  (S)
S('TFFSW', 'equals', 0o167, line=825)  #       CALCULATE TPERIGEE      CALCULATE TFF
S('TFFSWBIT', 'equals', 0o4753, line=826)

S('FLAGWRD8', 'equals', 0o104, line=829)  # (120-134)

# (SET)                   (RESET)

# BIT 15 FLAG 8 (S)
S('RPQFLAG', 'equals', 0o170, line=834)  #       RPQ NOT COMPUTED        RPQ COMPUTED
# (RPQ = VECTOR BE-
S('RPQFLBIT', 'equals', 0o4735, line=836)  #       TWEEN SECONDARY BODY
# AND PRIMARY BODY)

# BIT 14 FLAG 8
#   = 121D
#   = BIT14

# Page 79
# BIT 13 FLAG 8 (S)
S('NEWIFLG', 'equals', 0o172, line=845)  #       FIRST PASS THROUGH      SUCCEEDING ITERATION
S('NEWIBIT', 'equals', 0o4737, line=846)  #       INTEGRATION             OF INTEGRATION

# BIT 12 FLAG 8 *** PROTECTED FROM FRESH START ***
S('CMOONFLG', 'equals', 0o173, line=849)  #       PERMANENT CSM STATE     PERMANENT CSM STATE
S('CMOONBIT', 'equals', 0o4740, line=850)  #       IN LUNAR SPHERE         IN EARTH SPHERE

# BIT 11 FLAG 8 *** PROTECTED FROM FRESH START ***
S('LMOONFLG', 'equals', 0o174, line=853)  #       PERMANENT LM STATE      PERMANENT LM STATE
S('LMOONBIT', 'equals', 0o4741, line=854)  #       IN LUNAR SPHERE         IN EARTH SPHERE

# BIT 10 FLAG 8 (L)
S('FLUNDISP', 'equals', 0o175, line=857)  #       CURRENT GUIDANCE        CURRENT GUIDANCE
S('FLUNDBIT', 'equals', 0o4742, line=858)  #       DISPLAYS INHIBITED      DISPLAYS PERMITTED

# BIT 9 FLAG 8  (L)
S('P39/79SW', 'equals', 0o176, line=861)  #       P39/79 OPERATING        P38/78 OPERATING
S('P39SWBIT', 'equals', 0o4743, line=862)

# BIT 8 FLAG 8  *** PROTECTED FROM FRESH START ***
S('SURFFLAG', 'equals', 0o177, line=865)  #       LM ON LUNAR SURFACE     LM NOT ON LUNAR
S('SURFFBIT', 'equals', 0o4744, line=866)  #                               SURFACE

# BIT 7 FLAG 8  (S)
S('INFINFLG', 'equals', 0o200, line=869)  #       NO CONIC SOLUTION       CONIC SOLUTION
# (CLOSURE THROUGH        EXISTS
S('INFINBIT', 'equals', 0o4745, line=871)  #       INFINITY REQUIRED)

# BIT 6 FLAG 8  (S)
S('ORDERSW', 'equals', 0o201, line=874)  #       ITERATOR USES 2ND       ITERATOR USES 1ST
S('ORDERBIT', 'equals', 0o4746, line=875)  #       ORDER MINIMUM MODE      ORDER STANDARD MODE

# BIT 5 FLAG 8  (S)
S('APSESW', 'equals', 0o202, line=878)  #       RDESIRED OUTSIDE        RDESIRED INSIDE
# PERICENTER-APOCENTER    PERICENTER-APOCENTER
S('APSESBIT', 'equals', 0o4747, line=880)  #       RANGE IN TIME-RADIUS    RANGE IN TIME-RADIUS

# BIT 4 FLAG 8  (S)
S('COGAFLAG', 'equals', 0o203, line=883)  #       NO CONIC SOLUTION --    CONIC SOLUTION
# TOO CLOSE TO RECTI-     EXISTS (COGA DOES NOT

# Page 80
S('COGAFBIT', 'equals', 0o4750, line=887)  #       LINEAR (COGA OVERFLWS)  OVERFLOW)

# BIT 3 FLAG 8  (S)
#   = 132D
#   = BIT3  # OH 2009-05-15 Line not in scan

# BIT 2 FLAG 8  (L)
S('INITALGN', 'equals', 0o205, line=894)  #       INITIAL PASS THRU       SECOND PASS THRU P57
S('INITABIT', 'equals', 0o4752, line=895)  #       P57                     (CHECK RESET-MILLARD)

# BIT 1 FLAG 8  (S)
S('360SW', 'equals', 0o206, line=898)  #       TRANSFER ANGLE NEAR     TRANSFER ANGLE NOT
S('360SWBIT', 'equals', 0o4753, line=899)  #       360 DEGREES             NEAR 360 DEGREES

S('FLAGWRD9', 'equals', 0o105, line=902)  # (135-149)

# (SET)                   (RESET)

# BIT 15 FLAG 9
#   = 135D
#   = BIT15

# BIT 14 FLAG 9 (L)
S('FLVR', 'equals', 0o210, line=911)  #       VERTICAL RISE           NON-VERTICAL RISE
S('FLVRBIT', 'equals', 0o4736, line=912)  #       (ASCENT GUIDANCE)

# BIT 13 FLAG 9
#   = 137D
#   = BIT13  # OH 2009-05-15 Line not in scan

# BIT 12 FLAG 9 (L)
S('FLPC', 'equals', 0o212, line=919)  #       NO POSITION CONTROL     POSITION CONTROL
S('FLPCBIT', 'equals', 0o4740, line=920)  #       (ASCENT GUIDANCE)

# BIT 11 FLAG 9 (L)
S('FLPI', 'equals', 0o213, line=923)  #       PRE-IGNITION PHASE      REGULAR GUIDANCE
S('FLPIBIT', 'equals', 0o4741, line=924)  #       (ASCENT GUIDANCE)

# BIT 10 FLAG 9 (L)
S('FLRCS', 'equals', 0o214, line=927)  #       RCS INJECTION MODE      MAIN ENGINE MODE
S('FLRCSBIT', 'equals', 0o4742, line=928)  #       (ASCENT GUIDANCE)

# BIT 9 FLAG 9  (L)

# Page 81
S('LETABORT', 'equals', 0o215, line=933)  #       ABORT PROGRAMS          ABORT PROGRAMS
S('LETABBIT', 'equals', 0o4743, line=934)  #       ARE ENABLED             ARE NOT ENABLED

# BIT 8 FLAG 9  (L)
S('FLAP', 'equals', 0o216, line=937)  #       APS CONTINUED ABORT     APS ABORT IS NOT A
# AFTER DPS STAGING       CONTINUATION
S('FLAPBIT', 'equals', 0o4744, line=939)  #       (ASCENT GUIDANCE)

# BIT 7 FLAG 9  (L)
#   = 143D
#   = BIT7  # OH 2009-05-15 Line not in scan

# BIT 6 FLAG 9  (L)
S('ROTFLAG', 'equals', 0o220, line=947)  #       P70 AND P71 WILL        P70 AND P71 WILL NOT
S('ROTFLBIT', 'equals', 0o4746, line=948)  #       FORCE VEHICLE           FORCE VEHICLE
# ROTATION IN THE         ROTATION IN THE
# PREFERRED DIRECTION     PREFERRED DIRECTION

# BIT 5 FLAG 9  (S)
S('QUITFLAG', 'equals', 0o221, line=953)  #       DISCONTINUE INTEGR.     CONTINUE INTEGRATION
S('QUITBIT', 'equals', 0o4747, line=954)

# BIT 4 FLAG 9
#   = 146D
#   = BIT4

# BIT 3 FLAG 9  (L)
S('MID1FLAG', 'equals', 0o223, line=961)  #       INTEGRAT TO TDEC        INTEGRATE TO THE
S('MID1FBIT', 'equals', 0o4751, line=962)  #                               THEN-PRESENT TIME

# BIT 2 FLAG 9  (L)
S('MIDAVFLG', 'equals', 0o224, line=965)  #       INTEGRATION ENTERED     INTEGRATION WAS
# FROM ONE OF MIDTOAV     NOT ENTERED VIA
S('MIDAVBIT', 'equals', 0o4752, line=967)  #       PORTALS                 MIDTOAV

# BIT 1 FLAG 9  (S)
S('AVEMIDSW', 'equals', 0o225, line=970)  #       AVETOMID CALLING        NO AVETOMID W INTEGR
# FOR W.MATRIX INTEGR     ALLOW SET UP RM, VN
S('AVEMDBIT', 'equals', 0o4753, line=972)  #       DON'T WRITE OVER RN,    PIPTIME
# VN,PIPTIME

S('RASFLAG', 'equals', 0o106, line=976)  # WAS ONLY AN INSTALL-ERASTALL FLAG

# Page 82
S('FLGWRD10', 'equals', 0o106, line=979)  # (150-164)

# (SET)                   (RESET)

# BIT 15 FLAG 10 (S)
#   = 150D
#   = BIT15  # OH 2009-05-15 Line not in scan

# BIT 14 FLAG 10 (L,C)
S('INTFLAG', 'equals', 0o227, line=988)  #       INTEGRATION IN          INTEGRATION NOT IN
S('INTFLBIT', 'equals', 0o4736, line=989)  #       PROGRESS                PROGRESS

# BIT 13 FLAG 10 (S,L)
S('APSFLAG', 'equals', 0o230, line=992)  #       ASCENT STAGE            DESCENT STAGE
S('APSFLBIT', 'equals', 0o4737, line=993)  #        *** PROTECTED FROM FRESH START ***

# BIT 12 FLAG 10
#   = 153D
#   = BIT12  # OH 2009-05-15 Line not in scan

# BIT 11 FLAG 10
#   = 154D
#   = BIT11  # OH 2009-05-15 Line not in scan

# BIT 10 FLAG 10
#   = 155D
#   = BIT10  # OH 2009-05-15 Line not in scan

# BIT 9 FLAG 10
#   = 156D
#   = BIT9  # OH 2009-05-15 Line not in scan

# BIT 8 FLAG 10
#   = 157D
#   = BIT8  # OH 2009-05-15 Line not in scan

# BIT 7 FLAG 10 (L,C)
S('REINTFLG', 'equals', 0o236, line=1016)  #       INTEGRATION ROUTINE     INTEGRATION ROUTINE
S('REINTBIT', 'equals', 0o4745, line=1017)  #       TO BE RESTARTED         NOT TO BE RESTARTED

# BIT 6 FLAG 10
#   = 159D
#   = BIT6  # OH 2009-05-15 Line not in scan

# BIT 5 FLAG 10
#   = 160D
#   = BIT5  # OH 2009-05-15 Line not in scan

# Page 83
# BIT 4 FLAG 10
#   = 161D
#   = BIT4  # OH 2009-05-15 Line not in scan

# BIT 3 FLAG 10
#   = 162D
#   = BIT3  # OH 2009-05-15 Line not in scan

# BIT 2 FLAG 10
#   = 163D
#   = BIT2  # OH 2009-05-15 Line not in scan

# BIT 1 FLAG 10
#   = 164D
#   = BIT1  # OH 2009-05-15 Line not in scan

S('FLGWRD11', 'equals', 0o107, line=1046)  # (165-179)

# (SET)                   (RESET)

# BIT 15 FLAG 11 (L)(R12)
S('LRBYPASS', 'equals', 0o245, line=1051)  #       BYPASS ALL LANDING      DO NOT BYPASS LR
S('LRBYBIT', 'equals', 0o4735, line=1052)  #       RADAR UPDATES           UPDATES

# BIT 14 FLAG 11
#   = 166D
#   = BIT14

# BIT 13 FLAG 11
#   = 167D
#   = BIT13

# BIT 12 FLAG 11 (L)(R12)
S('VXINH', 'equals', 0o250, line=1063)  #       IF Z VELOCITY DATA      UPDATE X AXIS
# UNREASONABLE,           VELOCITY
S('VXINHBIT', 'equals', 0o4740, line=1065)  #       BYPASS X VELOCITY
# UPDATE ON NEXT PASS

# BIT 11 FLAG 11 (L)(R12)
S('PSTHIGAT', 'equals', 0o251, line=1069)  #       PAST HIGATE             PREHIGATE
S('PSTHIBIT', 'equals', 0o4741, line=1070)

# BIT 10 FLAG 11 (L)(R12)

# Page 84
S('NOLRREAD', 'equals', 0o252, line=1075)  #       LANDING RADAR           LR NOT REPOSITIONING
# REPOSITIONING;
S('NOLRRBIT', 'equals', 0o4742, line=1077)  #       BYPASS UPDATE

# BIT 9 FLAG 11 (L)(R12)
S('XORFLG', 'equals', 0o253, line=1080)  #       BELOW LIMIT             ABOVE LIMIT DO
# INHIBIT X AXIS          NOT INHIBIT
S('XORFLBIT', 'equals', 0o4743, line=1082)  #       OVERRIDE

# BIT 8 FLAG 11
S('LRINH', 'equals', 0o254, line=1085)  #       LANDING RADAR UP-       LR UPDATES INHIBITED
S('LRINHBIT', 'equals', 0o4744, line=1086)  #       DATES PERMITTED         BY ASTRONAUT
# BY ASTRONAUT

# BIT 7 FLAG 11 (L)(R12)
S('VELDATA', 'equals', 0o255, line=1090)  #       LR VELOCITY             LR VELOCITY MEASURE
S('VELDABIT', 'equals', 0o4745, line=1091)  #       MEASUREMENT MADE        NOT MADE

# BIT 6 FLAG 11 (L)(R12)
S('READLR', 'equals', 0o256, line=1094)  #       OK TO READ LR           DO NOT READ LR RANGE
S('READLBIT', 'equals', 0o4746, line=1095)  #       RANGE DATA              DATA

# BIT 5 FLAG 11 (L)(R12)
S('READVEL', 'equals', 0o257, line=1098)  #       OK TO READ LR           DO NOT READ LR
S('READVBIT', 'equals', 0o4747, line=1099)  #       VELOCITY DATA           VELOCITY DATA

# BIT 4 FLAG 11 (L)(R12)
S('RNGEDATA', 'equals', 0o260, line=1102)  #       LR ALTITUDE             LR ALTITUDE MEASURE
S('RNGEDBIT', 'equals', 0o4750, line=1103)  #       MEASUREMENT MADE        NOT MADE

# BIT 3 FLAG 11
S('SCALBAD', 'equals', 0o261, line=1106)  #       LR LOW SCALE DISP-      LS SCALE DISCRETE
S('SCABBIT', 'equals', 0o4751, line=1107)  #       CRETE NOT PRESENT       APPEARS OK
# WHEN IT SHOULD

# BIT 2 FLAG 11 (L)(R12)
S('VFLSHFLG', 'equals', 0o262, line=1111)  #       LR VELOCITY FAIL        LR VEL FAIL LAMP
# LAMP SHOULD BE          SHOULDN'T FLASH
S('VFLSHBIT', 'equals', 0o4752, line=1113)  #       FLASHING

# BIT 1 FLAG 11 (L)(R12)
# Page 85
S('HFLSHFLG', 'equals', 0o263, line=1117)  #       LR ALTITUDE FAIL        LR ALTITUDE FAIL
S('HFLSHBIT', 'equals', 0o4753, line=1118)  #       LAMP SHOULD BE          LAMP SHOULD NOT BE
# FLASHING                FLASHING

S('RADMODES', 'equals', 0o110, line=1121)  # RADAR FLAG WORD

S('FLGWRD12', 'equals', 0o110, line=1123)  # (180-194)             WAS RADMODES

# (SET)                   (RESET)

# BIT 15 FLAG 12
S('CDESFLAG', 'equals', 0o264, line=1128)  #       CONTINUOUS DESIG-       LGC CHECKS FOR LOCK-
S('CDESBIT', 'equals', 0o4735, line=1129)  #       NATE, LGC COMMANDS      ON WHEN ANTENNA
# RR REGARDLESS OF        BEING DESIGNATED
# LOCK-ON

# BIT 14 FLAG 12
S('REMODFLG', 'equals', 0o265, line=1134)  #       CHANGE IN ANTENNA       NO REMODE REQUESTED
S('REMODBIT', 'equals', 0o4736, line=1135)  #       MODE BEEN REQUESTED     OR OCCURRING
# I.E., REMODE

# BIT 13 FLAG 12
S('RCDU0FLG', 'equals', 0o266, line=1139)  #       RR CDU'S BEING          RR CDU'S NOT BEING
S('RCDU0BIT', 'equals', 0o4737, line=1140)  #       ZEROED                  ZEROED

# BIT 12 FLAG 12
S('ANTENFLG', 'equals', 0o267, line=1143)  #       RR ANTENNA MODE IS      RR ANTENNA IN MODE 1
S('ANTENBIT', 'equals', 0o4740, line=1144)  #       MODE 2

# BIT 11 FLAG 12
S('REPOSMON', 'equals', 0o270, line=1147)  #       REPOSITION MONITOR.     NO REPOSITION TAKING
S('REPOSBIT', 'equals', 0o4741, line=1148)  #       RR REPOSITION IS        PLACE
# TAKING PLACE

# BIT 10 FLAG 12
S('DESIGFLG', 'equals', 0o271, line=1152)  #       RR DESIGNATE            RR DESIGNATE NOT
S('DESIGBIT', 'equals', 0o4742, line=1153)  #       REQUESTED OR IN         REQUESTED OR IN
# PROGRESS                PROGRESS

# BIT 9 FLAG 12
S('ALTSCALE', 'equals', 0o272, line=1157)  #       LR ALTITUDE READING     LR ALTITUDE READING
S('ALTSCBIT', 'equals', 0o4743, line=1158)  #       IS ON HIGH SCALE        IS ON LOW SCALE

# Page 86
# BIT 8 FLAG 12
S('LRVELFLG', 'equals', 0o273, line=1162)  #       LR VELOCITY DATA        NO LR VELOCITY DATA
S('LRVELBIT', 'equals', 0o4744, line=1163)  #       FAIL                    FAIL

# BIT 7 FLAG 12
S('RCDUFAIL', 'equals', 0o274, line=1166)  #       RR CDU FAIL HAS         RR CDU FAIL OCCURRED
S('RCDUFBIT', 'equals', 0o4745, line=1167)  #       NOT OCCURRED

# BIT 6 FLAG 12
S('LRPOSFLG', 'equals', 0o275, line=1170)  #       LANDING RADAR           LR POSITION 1
S('LRPOSBIT', 'equals', 0o4746, line=1171)  #       POSITION 2

# BIT 5 FLAG 12
S('LRALTFLG', 'equals', 0o276, line=1174)  #       LR ALTITUDE DATA        NO LR ALTITUDE DATA
S('LRALTBIT', 'equals', 0o4747, line=1175)  #       FAIL.  COULD NOT BE     FAIL
# READ SUCCESSFULLY.

# BIT 4 FLAG 12
S('RRDATAFL', 'equals', 0o277, line=1179)  #       RR DATA FAIL.           NO RR DATA FAIL
S('RRDATABT', 'equals', 0o4750, line=1180)  #       DATA COULD NOT BE
# READ SUCCESSFULLY

# BIT 3 FLAG 12
S('RRRSFLAG', 'equals', 0o300, line=1184)  #       RR RANGE READING        RR RANGE READING ON
S('RRRSBIT', 'equals', 0o4751, line=1185)  #       ON THE HIGH SCALE       THE LOW SCALE

# BIT 2 FLAG 12
S('AUTOMODE', 'equals', 0o301, line=1188)  #       RR NOT IN AUTO MODE.    RR IN AUTO MODE
S('AUTOMBIT', 'equals', 0o4752, line=1189)  #       AUTO MODE DISCRETE
# IS NOT PRESENT

# BIT 1 FLAG 12
S('TURNONFL', 'equals', 0o302, line=1193)  #       RR TURN-ON SEQUENCE     NO RR TURN-ON
S('TURNONBT', 'equals', 0o4753, line=1194)  #       IN PROGRESS.  (ZERO     SEQUENCE IN PROGRESS
# CDU'S, FIX ANTENNA
# MODE)

S('DAPBOOLS', 'equals', 0o111, line=1198)  # DIGITAL AUTOPILOT FLAGWORD

# Page 87
S('FLGWRD13', 'equals', 0o111, line=1201)  # (195-209)     WAS DAPBOOLS

# (SET)                   (RESET)

# BIT 15 FLAG 13
S('PULSEFLG', 'equals', 0o303, line=1206)  #       MINIMUM IMPUSE          NOT IN MINIMUM
S('PULSES', 'equals', 0o4735, line=1207)  #       COMMAND MODE IN         IMPULSE COMMAND MODE
# "ATT HOLD" (V76)        (V77)

# BIT 14 FLAG 13
S('USEQRFLG', 'equals', 0o304, line=1211)  #       GIMBAL UNUSABLE.        TRIM GIMBAL MAY BE
S('USEQRJTS', 'equals', 0o4736, line=1212)  #       USE JETS ONLY.          USED.

# BIT 13 FLAG 13
S('CSMDKFLG', 'equals', 0o305, line=1215)  #       CSM DOCKED.  USE        CSM NOT DOCKED TO LM
S('CSMDOCKD', 'equals', 0o4737, line=1216)  #       BACKUP DAP

# BIT 12 FLAG 13
S('OURRCFLG', 'equals', 0o306, line=1219)  #       CURRENT DAP PASS        CURRENT DAP PASS IS
S('OURRCBIT', 'equals', 0o4740, line=1220)  #       IS RATE COMMAND         NOT RATE COMMAND

# BIT 11 FLAG 13
S('ACC4-2FL', 'equals', 0o307, line=1223)  #       4 JET X-AXIS TRANS-     2 JET X-AXIS TRANS-
S('ACC4OR2X', 'equals', 0o4741, line=1224)  #       LATION REQUESTED        LATION REQUESTED

# BIT 10 FLAG 13
S('AORBTFLG', 'equals', 0o310, line=1227)  #       B SYSTEM FOR X-         A SYSTEM FOR X-
S('AORBTRAN', 'equals', 0o4742, line=1228)  #       TRANSLATION             TRANSLATION PREFER'D

# BIT 9 FLAG 13
S('XOVINFLG', 'equals', 0o311, line=1231)  #       X-AXIS OVERRIDE         X-AXIS OVERRIDE OKAY
S('XOVINHIB', 'equals', 0o4743, line=1232)  #       LOCKED OUT

# BIT 8 FLAG 13
S('DRIFTDFL', 'equals', 0o312, line=1235)  #       ASSUME 0 OFFSET         USE OFFSET ACCELERA-
S('DRIFTBIT', 'equals', 0o4744, line=1236)  #       DRIFTING FLIGHT         ION ESTIMATE

# BIT 7 FLAG 13
S('RHCSCFLG', 'equals', 0o313, line=1239)  #       NORMAL RHC SCALING      FINE RHC SCALING
S('RHCSCALE', 'equals', 0o4745, line=1240)  #       REQUESTED               REQUESTED

# Page 88
# BIT 6 FLAG 13
S('ULLAGFLG', 'equals', 0o314, line=1244)  #       ULLAGE REQUEST BY       NO INTERNAL ULLAGE
S('ULLAGER', 'equals', 0o4746, line=1245)  #       MISSION PROGRAM         REQUEST

# BIT 5 FLAG 13
S('AORBSFLG', 'equals', 0o315, line=1248)  #       P-AXIS COUPLES 7.15     P-AXIS COUPLES 4.12
S('AORBSYST', 'equals', 0o4747, line=1249)  #       AND 8.16 PREFERRED      AND 3.11 PREFERRED

# BIT 4 FLAG 13
S('DBSELFLG', 'equals', 0o316, line=1252)  #       MAX DB SELECTED         MIN DB SELECTED BY
S('DBSELECT', 'equals', 0o4750, line=1253)  #       BY CREW (5 DEG)         CREW (0.3 DEG)

# BIT 3 FLAG 13
S('ACCOKFLG', 'equals', 0o317, line=1256)  #       CONTROL AUTHORITY       RESTART OR FRESH ST.
S('ACCSOKAY', 'equals', 0o4751, line=1257)  #       VALUES FROM 1/ACCS      SINCE LAST 1/ACCS;
# USABLE                  OUTPUTS SUSPECT.

# BIT 2 FLAG 13
S('AUTR2FLG', 'equals', 0o320, line=1261)  # THESE FLAGS ARE USED TOGETHER TO INDICATE
S('AUTRATE2', 'equals', 0o4752, line=1262)  # ASTRONAUT-CHOSEN KALCMANU MANEUVER RATES
# (0,0)=(BIT2,BIT1)=    0.2 DEG/SEC
# BIT 1 FLAG 13                                 # (0,1)=                0.5 DEG/SEC
S('AUTR1FLG', 'equals', 0o321, line=1265)  # (1,0)=                2.0 DEG/SEC
S('AUTRATE1', 'equals', 0o4753, line=1266)  # (1,1)=               10.0 DEG/SEC

# Page 89 (nothing on this page)
