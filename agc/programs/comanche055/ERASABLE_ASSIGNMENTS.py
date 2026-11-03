"""ERASABLE_ASSIGNMENTS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/ERASABLE_ASSIGNMENTS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 37-130 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('ERASABLE_ASSIGNMENTS', 'ERASABLE_ASSIGNMENTS.agc', 'Comanche055', pages='37-130')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     ERASABLE_ASSIGNMENTS.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Mod history:  2009-05-06 RSB  Started adapting from the Colossus249/ file
# of the same name, using Comanche055 page
# images. Only through page 51 so far.
# 2009-05-07 RSB  Through page 92 so far.
# 2009-05-07 RSB  (Again!) First draft completed.
# 2009-05-20 RSB  Fixed some bugs uncovered in trial assemblies:
# EMDOT, STATEXIT, VGDISP, DVPREV, POSTCDH,
# RETROFLG not defined correctly, changed the
# typing of labels 9X9LOC1 and 9X9LOC2,
# R32FLBIT -> R31FLBIT.
# 2009-05-21 RSB  Corrected definition of DELBRTMP, which
# chained to quite a lot of off-by-one errors.
# Changed a +8 to a +8D.
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

# Page 37
# CONVENTIONS AND NOTATIONS UTILIZED FOR ERASABLE ASSIGNMENTS.

# EQUALS  IS USED IN TWO WAYS.  IT IS OFTEN USED TO CHAIN A GROUP
# OF ASSIGNMENTS SO THAT THE GROUP MAY BE MOVED WITH THE
# CHANGING OF ONLY ONE CARD.  EXAMPLE:
#
# X       EQUALS  START
# Y       EQUALS  X       +SIZE.X
# Z       EQUALS  Y       +SIZE.Y
#
# (X, Y, AND Z ARE CONSECUTIVE AND BEGIN AT START.
# SIZE.X AND SIZE.Y ARE THE RESPECTIVE SIZES OF X AND Y.
# USUALLY NUMERIC, IE. 1, 2, 6, 18D, ETC.)

# EQUALS  OFTEN IMPLIES THE SHARING OF REGISTERS (DIFFERENT NAMES
# AND DIFFERENT DATA).  EXAMPLE:
#
# X       EQUALS  Y

# =       MEANS THAT MULTIPLE NAMES HAVE BEEN GIVEN TO THE SAME DATA.
# (THIS IS LOGICAL EQUIVALENCE, NOT SHARING.)  EXAMPLE:
#
# X       =       Y

# THE SIE AND UTILIZATION OF AN ERASABLE ARE OFTEN INCLUDED IN
# THE COMMENTS IN THE FOLLOWING FORM:  M(SIZE)N.
#
# M       REFERS TO THE MOBILITY OF THE ASSIGNMENT.
# B       MEANS THAT THE SYMBOL IS REFERENCED BY BASIC
# INSTRUCTIONS AND THUS IS E-BANK SENSITIVE.
# I       MEANS THAT THE SYMBOL IS REFERENCED ONLY BY
# INTERPRETIVE INSTRUCTIONS, AND IS THUS E-BANK
# INSENSITIVE AND MAY APPEAR IN ANY E-BANK.
#
# SIZE    IS THE NUMBER OF REGISTERS INCLUDED BY THE SYMBOL.
#
# N       INDICATES THE NATURE OF PERMANENCE OF THE CONTENTS.
# PL      MEANS THAT THE CONTENTS ARE PAD LOADED.
# DSP     MEANS THAT THE REGISTER IS USED FOR A DISPLAY.
# PRM     MEANS THAT THE REGISTER IS PERMANENT.  IE., IT
# IS USED DURING THE ENTIRE MISSION FOR ONE
# PURPOSE AND CANNOT BE SHARED.
# TMP     MEANS THAT THE REGISTER IS USED TEMPORARILY OR
# IS A SCRATCH REGISTER FOR THE ROUTINE TO WHICH
# IT IS ASSIGNED.  THAT IS, IT NEED NOT BE SET
# PRIOR TO INVOCATION OF THE ROUTINE NOR DOES IT
# CONTAIN USEFUL OUTPUT TO ANOTHER ROUTINE.  THUS
# Page 38
# IT MAY BE SHARED WITH ANY OTHER ROUTINE WHICH
# IS NOT ACTIVE IN PARALLEL
# IN      MEANS INPUT TO THE ROUTINE AND IT IS PROBABLY
# TEMPORARY FOR A HIGHER-LEVEL ROUTINE/PROGRAM.
# OUT     MEANS OUTPUT FROM THE ROUTINE, PROBABLY
# TEMPORARY FOR A HIGHER-LEVEL ROUTINE/PROGRAM.

# Page 39

# SPECIAL REGISTERS.

S('A', 'equals', 0o0, line=101)
S('L', 'equals', 0o1, line=102)  # L AND Q ARE BOTH CHANNELS AND REGISTERS
S('Q', 'equals', 0o2, line=103)
S('EBANK', 'equals', 0o3, line=104)
S('FBANK', 'equals', 0o4, line=105)
S('Z', 'equals', 0o5, line=106)  # ADJACENT TO FBANK AND BBANK FOR DXCH Z
S('BBANK', 'equals', 0o6, line=107)  # (DTCB) AND DXCH FBANK (DTCF).
# REGISTER 7 IS A ZERO-SOURCE, USED BY ZL.

S('ARUPT', 'equals', 0o10, line=110)  # INTERRUPT STORAGE
S('LRUPT', 'equals', 0o11, line=111)
S('QRUPT', 'equals', 0o12, line=112)
S('SAMPTIME', 'equals', 0o13, line=113)  # SAMPLED TIME 1 & 2.
S('ZRUPT', 'equals', 0o15, line=114)  # (13 AND 14 ARE SPARES.)
S('BANKRUPT', 'equals', 0o16, line=115)  # USUALLY HOLDS FBANK OR BBANK.
S('BRUPT', 'equals', 0o17, line=116)  # RESUME ADDRESS AS WELL.

S('CYR', 'equals', 0o20, line=118)
S('SR', 'equals', 0o21, line=119)
S('CYL', 'equals', 0o22, line=120)
S('EDOP', 'equals', 0o23, line=121)  # EDITS INTERPRETIVE OPERATION CODE PAIRS.

S('TIME2', 'equals', 0o24, line=123)
S('TIME1', 'equals', 0o25, line=124)
S('TIME3', 'equals', 0o26, line=125)
S('TIME4', 'equals', 0o27, line=126)
S('TIME5', 'equals', 0o30, line=127)
S('TIME6', 'equals', 0o31, line=128)
S('CDUX', 'equals', 0o32, line=129)
S('CDUY', 'equals', 0o33, line=130)
S('CDUZ', 'equals', 0o34, line=131)
S('CDUT', 'equals', 0o35, line=132)  # OPTICS TRUNNION CDU (WAS OPTY).
S('OPTY', 'equals', 0o35, line=133)
S('CDUS', 'equals', 0o36, line=134)  # OPTICS SHAFT CDU (WAS OPTX).
S('OPTX', 'equals', 0o36, line=135)
S('PIPAX', 'equals', 0o37, line=136)
S('PIPAY', 'equals', 0o40, line=137)
S('PIPAZ', 'equals', 0o41, line=138)
S('BMAGX', 'equals', 0o42, line=139)
S('BMAGY', 'equals', 0o43, line=140)
S('BMAGZ', 'equals', 0o44, line=141)
S('INLINK', 'equals', 0o45, line=142)
S('RNRAD', 'equals', 0o46, line=143)
S('GYROCTR', 'equals', 0o47, line=144)
S('GYROCMD', 'equals', 0o47, line=145)
S('CDUXCMD', 'equals', 0o50, line=146)
S('CDUYCMD', 'equals', 0o51, line=147)

# Page 40

S('CDUZCMD', 'equals', 0o52, line=151)
S('CDUTCMD', 'equals', 0o53, line=152)  # OPTICS TRUNNION COMMAND (WAS OPTYCMD)
S('OPTYCMD', 'equals', 0o53, line=153)
S('TVCYAW', 'equals', 0o53, line=154)  # SPS YAW COMMAND IN TVC MODE
S('CDUSCMD', 'equals', 0o54, line=155)  # OPTICS SHAFT COMMAND (WAS OPTXCMD).
S('TVCPITCH', 'equals', 0o54, line=156)  # SPS PITCH COMMAND IN TVC MODE
S('OPTXCMD', 'equals', 0o54, line=157)
S('EMSD', 'equals', 0o55, line=158)
S('THRUST', 'equals', 0o55, line=159)
S('LEMONM', 'equals', 0o56, line=160)
S('LOCALARM', 'equals', 0o57, line=161)
S('BANKALRM', 'equals', 0o60, line=162)

# INTERPRETIVE REGISTERS ADDRESSED RELATIVE TO VAC AREA.

S('LVSQUARE', 'equals', 0o42, line=166)  # SQUARE OF VECTOR INPUT TO ABVAL AND UNIT
S('LV', 'equals', 0o44, line=167)  # LENGTH OF VECTOR INPUT TO UNIT.
S('X1', 'equals', 0o46, line=168)  # INTERPRETIVE SPECIAL REGISTER RELATIVE
S('X2', 'equals', 0o47, line=169)  # TO THE WORK AREA.
S('S1', 'equals', 0o50, line=170)
S('S2', 'equals', 0o51, line=171)
S('QPRET', 'equals', 0o52, line=172)

# Page 41

# INPUT/OUTPUT CHANNELS

# *** CHANNEL ZERO IS TO BE USED IN AN INDEXED OPERATION ONLY. ***
S('LCHAN', 'equals', 0o1, line=179)
S('QCHAN', 'equals', 0o2, line=180)
S('HISCALAR', 'equals', 0o3, line=181)
S('LOSCALAR', 'equals', 0o4, line=182)
S('PYJETS', 'equals', 0o5, line=183)
S('ROLLJETS', 'equals', 0o6, line=184)
S('SUPERBNK', 'equals', 0o7, line=185)
S('OUT0', 'equals', 0o10, line=186)
S('DSALMOUT', 'equals', 0o11, line=187)
S('CHAN12', 'equals', 0o12, line=188)
S('CHAN13', 'equals', 0o13, line=189)
S('CHAN14', 'equals', 0o14, line=190)
S('MNKEYIN', 'equals', 0o15, line=191)
S('NAVKEYIN', 'equals', 0o16, line=192)
S('CHAN30', 'equals', 0o30, line=193)
S('CHAN31', 'equals', 0o31, line=194)
S('CHAN32', 'equals', 0o32, line=195)
S('CHAN33', 'equals', 0o33, line=196)
S('DNTM1', 'equals', 0o34, line=197)
S('DNTM2', 'equals', 0o35, line=198)

# END OF CHANNEL ASSIGNMENTS

# Page 42

# FLAGWORDS
#
# FLAGWRD0      STATE +0        (000-014)
# FLAGWRD1      STATE +1        (015-029)
# FLAGWRD2      STATE +2        (030-044)
# FLAGWRD3      STATE +3        (045-059)
# FLAGWRD4      STATE +4        (060-074)
# FLAGWRD5      STATE +5        (075-089)
# FLAGWRD6      STATE +6        (090-104)
# FLAGWRD7      STATE +7        (105-119)
# FLAGWRD8      STATE +8D       (120-134)
# FLAGWRD9      STATE +9D       (135-149)

# SORTED LIST OF
# INTERPRETIVE SWITCH BIT ASSIGNMENTS

# INTERPRETIVE SWITCH BIT ASSIGNMENTS
#
# FLAGWORD      DEC NUM         BIT & FLAG      EQUIVALENT FLAGWORDS
#
# 22DSPFLG      032D            BIT 13 FLAG 2
# 360SW         134D            BIT 1 FLAG 8
# 3AXISFLG      084D            BIT 6 FLAG 5
# ADVTRK        125D            BIT 10 FLAG 8
# AMOONFLG      13D             BIT 2 FLAG 0
# APSESW        130D            BIT 5 FLAG 8
# ASTNFLAG      108D            BIT 12 FLAG 7
# ATTCHFLG      118D            BIT 2 FLAG 7
# AVEGFLAG      029D            BIT 1 FLAG 1
# AVEMIDSW      149D            BIT 1 FLAG 9
# AVFLAG        040D            BIT 5 FLAG 2
# CALCMAN2      043D            BIT 2 FLAG 2
# CMDAPARM      093D            BIT 12 FLAG 6
# CMOONFLG      123D            BIT 12 FLAG 8
# CM/DSTBY      103D            BIT 2 FLAG 6
# COGAFLAG      131D            BIT 4 FLAG 8
# COMPUTER      082D            BIT 8 FLAG 5
# CPHIFLAG      000D            BIT 15 FLAG 0
# CULTFLAG      053D            BIT 7 FLAG 3
# D6OR9FLG      058D            BIT 2 FLAG 3
# DAPBIT1       090D            BIT 15 FLAG 6
# DAPBIT2       091D            BIT 14 FLAG 6
# DIM0FLAG      059D            BIT 1 FLAG 3
# DMENFLAG      081D            BIT 9 FLAG 5
# DRIFTFLG      030D            BIT 15 FLAG 2
# DSKYFLAG      075D            BIT 15 FLAG 5
# EGSW          097D            BIT 8 FLAG 6    KNOTNFLG R57FLAG

# Page 43

# ENG1FLAG      018D            BIT 12 FLAG 1
# ENG2FLAG      019D            BIT 11 FLAG 1
# ENGONFLG      083D            BIT 7 FLAG 5
# ERADFLAG      017D            BIT 13 FLAG 1
# ETPIFLAG      038D            BIT 7 FLAG 2    FIRSTFLG OPTNSW
# F2RTE         010D            BIT 5 FLAG 0
# FINALFLG      039D            BIT 6 FLAG 2
# FIRSTFLG      038D            BIT 7 FLAG 2    ETPIFLAG OPTNSW
# FREEFLAG      012D            BIT 3 FLAG 0
# GAMDIFSW      094D            BIT 11 FLAG 6
# GLOKFAIL      046D            BIT 14 FLAG 3
# GONEBY        112D            BIT 8 FLAG 7
# GONEPAST      095D            BIT 10 FLAG 6
# GRRBKFLG      085D            BIT 5 FLAG 5
# GUESSW        028D            BIT 2 FLAG 1
# GYMDIFSW      104D            BIT 1 FLAG 6
# .05GSW        102D            BIT 3 FLAG 6
# HIND          099D            BIT 6 FLAG 6
# IDLEFAIL      024D            BIT 6 FLAG 1
# IDLEFLAG      113D            BIT 7 FLAG 7
# IGNFLAG       107D            BIT 13 FLAG 7
# IMPULSW       036D            BIT 9 FLAG 2
# IMUSE         007D            BIT 8 FLAG 0
# INCORFLG      079D            BIT 11 FLAG 5
# INFINFLG      128D            BIT 7 FLAG 8
# INRLSW        100D            BIT 5 FLAG 6
# INTFLAG       151D            BIT 14 FLAG 10
# INTYPFLG      056D            BIT 4 FLAG 3
# ITSWICH       106D            BIT 14 FLAG 7
# KFLAG         014D            BIT 1 FLAG 0
# KNOWNFLG      097D            BIT 8 FLAG 6    EGSW R57FLAG
# LATSW         101D            BIT 4 FLAG 6
# LMOONFLG      124D            BIT 11 FLAG 8
# LUNAFLAG      048D            BIT 12 FLAG 3
# MAXDBFLG      138D            BIT 12 FLAG 9
# MGLVFLAG      088D            BIT 2 FLAG 5
# MID1FLAG      147D            BIT 3 FLAG 9
# MIDAVFLG      148D            BIT 2 FLAG 9
# MIDFLAG       002D            BIT 13 FLAG 0
# MKOVFLAG      072D            BIT 3 FLAG 4
# MOONFLAG      003D            BIT 12 FLAG 0
# MRKIDFLG      060D            BIT 15 FLAG 4
# MRKNVFLG      066D            BIT 9 FLAG 4
# MRUPTFLG      070D            BIT 5 FLAG 4
# MWAITFLG      064D            BIT 11 FLAG 4
# N22ORN17      144D            BIT 6 FLAG 9
# NEEDLFLG      006D            BIT 9 FLAG 0
# NEWIFLG       122D            BIT 13 FLAG 8
# NJETSFLG      015D            BIT 15 FLAG 1
# NODOFLAG      044D            BIT 1 FLAG 2

# Page 44

# NODOP01       018D            BIT 12 FLAG 1
# NORFHOR       004D            BIT 11 FLAG 0
# NORMSW        110D            BIT 10 FLAG 7
# NOSWITCH      098D            BIT 7 FLAG 6
# NRMIDFLG      062D            BIT 13 FLAG 4
# NRMNVFLG      067D            BIT 8 FLAG 4
# NRUPTFLG      071D            BIT 4 FLAG 4
# NWAITFLG      065D            BIT 10 FLAG 4
# OPTNSW        038D            BIT 7 FLAG 2    ETPIFLAG FIRSTFLG
# ORBWFLAG      054D            BIT 6 FLAG 3
# ORDERSW       129D            BIT 6 FLAG 8
# P21FLAG       033D            BIT 12 FLAG 2
# P22MKFLG      049D            BIT 11 FLAG 3
# P39/79SW      126D            BIT 9 FLAG 8
# PDSPFLAG      063D            BIT 12 FLAG 4
# PFRATFLG      041D            BIT 4 FLAG 2
# PINBRFLG      069D            BIT 6 FLAG 4
# PRECIFLG      052D            BIT 8 FLAG 3
# PRFTRKAT      060D            BIT 10 FLAG 5
# PRIODFLG      061D            BIT 14 FLAG 4
# PRONVFLG      068D            BIT 7 FLAG 4
# QUITFLAG      145D            BIT 5 FLAG 9
# R21MARK       031D            BIT 14 FLAG 2
# R22CAFLG      143D            BIT 7 FLAG 9
# R23FLG        021D            BIT 9 FLAG 1
# R31FLAG       146D            BIT 4 FLAG 9
# R53FLAG       009D            BIT 6 FLAG 0
# R57FLAG       097D            BIT 8 FLAG 6    KNOWNFLG EGSW
# R60FLAG       086D            BIT 4 FLAG 5
# REFSMFLG      047D            BIT 13 FLAG 3
# REINTFLG      158D            BIT 7 FLAG 10
# RELVELSW      096D            BIT 9 FLAG 6
# RENDWFLG      089D            BIT 1 FLAG 5
# RNDVZFLG      008D            BIT 7 FLAG 0
# RPQFLAG       120D            BIT 15 FLAG 6
# RVSW          111D            BIT 9 FLAG 7
# SAVECFLG      140D            BIT 10 FLAG 9
# SKIPVHF       035D            BIT 10 FLAG 2
# SLOPESW       027D            BIT 3 FLAG 1
# SOLNSW        087D            BIT 3 FLAG 5
# SOURCFLG      142D            BIT 8 FLAG 9
# STATEFLG      055D            BIT 5 FLAG 3
# STEERSW       034D            BIT 11 FLAG 2
# STIKFLAG      016D            BIT 14 FLAG 1
# STRULLSW      092D            BIT 13 FLAG 6
# SURFFLAG      127D            BIT 8 FLAG 8
# SWTOVER       135D            BIT 15 FLAG 9
# TARG1FLG      020D            BIT 10 FLAG 1

# Page 45

# TARG2FLG      021D            BIT 9 FLAG 1
# TERMIFLG      105D            BIT 15 FLAG 7
# TFFSW         119D            BIT 1 FLAG 7
# TIMRFLAG      109D            BIT 11 FLAG 7
# TRACKFLG      025D            BIT 5 FLAG 1
# TRM03FLG      026D            BIT 4 FLAG 1
# TRUNFLAG      011D            BIT 4 FLAG 0
# UPDATFLG      023D            BIT 7 FLAG 1
# UPLOCKFL      116D            BIT 4 FLAG 7
# V37FLAG       114D            BIT 6 FLAG 7
# V59FLAG       078D            BIT 12 FLAG 5
# V67FLAG       136D            BIT 14 FLAG 9
# V82EMFLG      137D            BIT 13 FLAG 9
# V94FLAG       139D            BIT 11 FLAG 9
# V96ONFLG      132D            BIT 3 FLAG 8
# VEHUPFLG      022D            BIT 8 FLAG 1
# VERIFLAG      117D            BIT 3 FLAG 7
# VFLAG         050D            BIT 10 FLAG 3
# VHFRFLAG      141D            BIT 9 FLAG 9
# VINTFLAG      057D            BIT 3 FLAG 3
# XDELVFLG      037D            BIT 8 FLAG 2
# XDSPFLAG      074D            BIT 1 FLAG 4

# Page 46

# INTERPRETIVE SWITCH BIT ASSIGNMENTS
S('FLAGWRD0', 'equals', 0o74, line=384)  # (000-014)
# (SET)                 (RESET)
# BIT 15 FLAG 0
S('CPHIFLAG', 'equals', 0o0, line=387)  # OUTPUT OF CALCGA IS   OUTPUT OF CALCGA IS
# CPHIX                 THETAD
S('CPHIBIT', 'equals', 0o5001, line=389)

# BIT 14 FLAG 0
S('JSWITCH', 'equals', 0o1, line=392)  # INTEGRATION OF W      INTEGRATION OF STATE
# MATRIX                VECTOR
S('JSWCHBIT', 'equals', 0o5002, line=394)

# BIT 13 FLAG 0
S('MIDFLAG', 'equals', 0o2, line=397)  # INTEGRATION WITH      INTEGRATION WITHOUT
# SOLAR PERTURBATIONS   SOLAR PERTURBATIONS

S('MIDFLBIT', 'equals', 0o5003, line=400)

# BIT 12 FLAG 0
S('MOONFLAG', 'equals', 0o3, line=403)  # MOON IS SPHERE OF     EARTH IS SPHERE OF
# INFLUENCE             INFLUENCE

S('MOONBIT', 'equals', 0o5004, line=406)

# BIT 11 FLAG 0
S('NORFHOR', 'equals', 0o4, line=409)  # FAR HORIZON           NEAR HORIZON

S('NORFBIT', 'equals', 0o5005, line=411)

# BIT 10 FLAG 0
S('ZMEASURE', 'equals', 0o5, line=414)  # MEASUREMENT PLANET    MEASUREMENT PLANET
# AND PRIMARY PLANET    AND PRIMARY PLANET
# DIFFERENT             SAME

S('ZMEASBIT', 'equals', 0o5006, line=418)

# BIT 9 FLAG 0
S('NEEDLFLG', 'equals', 0o6, line=421)  # TOTAL ATTITUDE        A/P FOLLOWING ERROR
# ERROR DISPLAYED       DISPLAYED

S('NEEDLBIT', 'equals', 0o5007, line=424)

# BIT 8 FLAG 0
S('IMUSE', 'equals', 0o7, line=427)  # IMU IN USE            IMU NOT IN USE

# Page 47

S('IMUSEBIT', 'equals', 0o5010, line=431)

# BIT 7 FLAG 0
S('RNDVZFLG', 'equals', 0o10, line=434)  # P20 RUNNING           P20 NOT RUNNING

S('RNDVZBIT', 'equals', 0o5011, line=436)

# BIT 6 FLAG 0
S('R53FLAG', 'equals', 0o11, line=439)  # V51 INITIATED         V51 NOT INITIATED

S('R53FLBIT', 'equals', 0o5010, line=441)

# BIT 5 FLAG 0
S('F2RTE', 'equals', 0o12, line=444)  # IN TIME CRITICAL      NOT IN TIME CRITICAL
# MODE                  MODE

S('F2RTEBIT', 'equals', 0o5013, line=447)

# BIT 4 FLAG 0
S('TRUNFLAG', 'equals', 0o13, line=450)  # DRIVING OF TRUNNION   DRIVING OF TRUNNION
# ALLOWED               NOT ALLOWED

S('TRUNBIT', 'equals', 0o5014, line=453)

# BIT 3 FLAG 0
S('FREEFLAG', 'equals', 0o14, line=456)  # (TEMPORARY FLAG USED IN MANY ROUTINES)

S('FREEFBIT', 'equals', 0o5015, line=458)

# BIT 2 FLAG 0
S('AMOONFLG', 'equals', 0o15, line=461)  # STATE VECTOR IN       STATE VECTOR IN
S('AMOONBIT', 'equals', 0o5016, line=462)  # LUNAR SPHERE AT       EARTH SPHERE AT
# MIDTOAVE              MIDTOAVE

# BIT 1 FLAG 0
S('KFLAG', 'equals', 0o16, line=466)  # SEARCH SECTOR MORE    SEARCH SECTOR LESS
# THAN 180 DEGREES      THAN 180 DEGREES

S('KBIT', 'equals', 0o5017, line=469)

S('FLAGWRD1', 'equals', 0o75, line=471)  # (015-029)
# (SET)                 (RESET)

# BIT 15 FLAG 1
S('NJETSFLG', 'equals', 0o17, line=475)  # TWO JET RCS BURN      FOUR JET RCS BURN

S('NJETSBIT', 'equals', 0o5001, line=477)

# Page 48

# BIT 14 FLAG 1
S('STIKFLAG', 'equals', 0o20, line=482)  # RHC CONTROL           CMC CONTROL
S('STIKBIT', 'equals', 0o5002, line=483)

# BIT 13 FLAG 1
S('ERADFLAG', 'equals', 0o21, line=486)  # EARTH, COMPUTE        EARTH, USED FIXED
# FISCHER ELLIPSOID     RADIUS
# RADIUS
# MOON, USE FIXED       MOON, USE RLS FOR
# RADIUS                LUNAR RADIUS

S('ERADFBIT', 'equals', 0o5003, line=492)

# BIT 12 FLAG 1
S('NODOP01', 'equals', 0o22, line=495)  # P01 NOT ALLOWED       P01 ALLOWED
S('NOP01BIT', 'equals', 0o5004, line=496)

# BIT 11 FLAG 1
S('ENG2FLAG', 'equals', 0o23, line=499)  # RCS BURN              SPS BURN

S('ENG2BIT', 'equals', 0o5005, line=501)

# BIT 10 FLAG 1
S('TARG1FLG', 'equals', 0o24, line=504)  # SIGHTING LEM          NOT SIGHTING LEM

S('TARG1BIT', 'equals', 0o5006, line=506)

# BIT 9 FLAG 1
S('TARG2FLG', 'equals', 0o25, line=509)  # SIGHTING LANDMARK     SIGHTING STAR

S('TARG2BIT', 'equals', 0o5007, line=511)

# BIT 9 FLAG 1
S('R23FLG', 'equals', 0o25, line=514)  # R23 MARKING

S('R23BIT', 'equals', 0o5007, line=516)

# BIT 8 FLAG 1
S('VEHUPFLG', 'equals', 0o26, line=519)  # CSM STATE VECTOR      LEM STATE VECTOR
# BEING UPDATED         BEING UPDATED

S('VEHUPBIT', 'equals', 0o5010, line=522)

# BIT 7 FLAG 1
S('UPDATFLG', 'equals', 0o27, line=525)  # UPDATING BY MARKS     UPDATING BY MARKS
# ALLOWED               NOT ALLOWED
# Page 49

S('UPDATBIT', 'equals', 0o5011, line=529)

# BIT 6 FLAG 1
S('IDLEFAIL', 'equals', 0o30, line=532)  # INHIBIT R41           ENABLE R41 (ENGFAIL)

S('IDLEBIT', 'equals', 0o5012, line=534)

# BIT 5 FLAG 1
S('TRACKFLG', 'equals', 0o31, line=537)  # TRACKING ALLOWED      TRACKING NOT ALLOWED

S('TRACKBIT', 'equals', 0o5013, line=539)

# BIT 4 FLAG 1
S('TRM03FLG', 'equals', 0o32, line=542)  # REQUEST TO            NO REQUEST TO
# TERMINATE P03 HAS     TERMINATE P03 HAS
# BEEN ENTERED          BEEN ENTERED

S('TRM03BIT', 'equals', 0o5014, line=546)

# BIT 3 FLAG 1
S('SLOPESW', 'equals', 0o33, line=549)  # ITERATE WITH BIAS     ITERATE WITH REGULA
# METHOD IN ITERATOR    FALSI METHOD IN
# ITERATOR

S('SLOPEBIT', 'equals', 0o5015, line=553)

# BIT 2 FLAG 1
S('GUESSW', 'equals', 0o34, line=556)  # NO STARTING VALUE     STARTING VALUE FOR
# FOR ITERATION         ITERATION EXISTS

S('GUESSBIT', 'equals', 0o5016, line=559)

# BIT 1 FLAG 1
S('AVEGFLAG', 'equals', 0o35, line=562)  # AVERAGEG (SERVICER)   AVERAGEG (SERVICER)
# TO CONTINUE           TO CEASE

S('AVEGBIT', 'equals', 0o5017, line=565)

S('FLAGWRD2', 'equals', 0o76, line=567)  # (030-044)

# (SET)                 (RESET)

# BIT 15 FLAG 2
S('DRIFTFLG', 'equals', 0o36, line=572)  # T3RUPT CALLS GYRO     T3RUPT DOES NO GYRO
# COMPENSATION          COMPENSATION

S('DRFTBIT', 'equals', 0o5001, line=575)

# Page 50

# BIT 14 FLAG 2
S('R21MARK', 'equals', 0o37, line=580)  # OPTION ONE FOR        OPTION TWO FOR
# MARKRUPT              MARKRUPT

S('R21BIT', 'equals', 0o5002, line=583)

# BIT 13 FLAG 2
S('22DSPFLG', 'equals', 0o40, line=586)  # DISPLAY DR,DV         DO NOT DISPLAY DR,DV

S('22DSPBIT', 'equals', 0o5003, line=588)

# BIT 12 FLAG 2
S('P21FLAG', 'equals', 0o41, line=591)  # SUCCEEDING PASS       1ST PASS THRU P21,
# THRU P21, USE BASE    CALCULATE BASE
S('P21BIT', 'equals', 0o5004, line=593)  # VECTOR FOR CALC.      VECTOR

S('STEERSW', 'equals', 0o42, line=595)  # STEERING TO BE DONE   STEERING OMITTED

S('STEERBIT', 'equals', 0o5005, line=597)

# BIT 10 FLAG 2
S('SKIPVHF', 'equals', 0o43, line=600)  # DISREGARD RADAR       RADAR READ TO
# READ BECAUSE OF       PROCEED NORMALLY
S('SKIPVBIT', 'equals', 0o5006, line=602)  # SFTWRE OR HDWRE
# RESTART

# BIT 9 FLAG 2
S('IMPULSW', 'equals', 0o44, line=606)  # MINIMUM IMPULSE       STEERING BURN (NO
# BURN (CUTOFF TIME     CUTOFF TIME YET
# SPECIFIED)            AVAILABLE)

S('IMPULBIT', 'equals', 0o5007, line=610)

# BIT 8 FLAG 2
S('XDELVFLG', 'equals', 0o45, line=613)  # EXTERNAL DELTAV VG    LAMBERT (AIMPOINT)
# COMPUTATION           VG COMPUTATION

S('XDELVBIT', 'equals', 0o5010, line=616)

# BIT 7 FLAG 2
S('ETPIFLAG', 'equals', 0o46, line=619)  # ELEVATION ANGLE       TPI TIME SUPPLIED
# SUPPLIED FOR P34,74   FOR P34,74

# BIT 7 FLAG 2
S('FIRSTFLG', 'equals', 0o46, line=623)  # FIRST PASS            SUCCEEDING PASS THRU
# THRU S40.9            S40.9

S('FIRSTBIT', 'equals', 0o5011, line=626)

# BIT 7 FLAG 2
# Page 51
S('OPTNSW', 'equals', 0o46, line=630)  # SOI PHASE P38/P78     SOR PHASE OF P38/P78

S('FINALBIT', 'equals', 0o5012, line=632)

# BIT 6 FLAG 2
S('FINALFLG', 'equals', 0o47, line=635)  # LAST PASS THROUGH     INTERIM PASS THROUGH
# RENDEZVOUS PROGRAM    RENDEZVOUS PROGRAM
# COMPUTATIONS          COMPUTATIONS

S('AVFLBIT', 'equals', 0o5013, line=639)

# BIT 5 FLAG 2
S('AVFLAG', 'equals', 0o50, line=642)  # LEM IS ACTIVE         CSM IS ACTIVE
# VEHICLE               VEHICLE

# BIT 4 FLAG 2
S('PFRATFLG', 'equals', 0o51, line=646)  # PREFERRED ATTITUDE    PREFERRED ATTITUDE
# COMPUTED              NOT COMPUTED

S('PFRATBIT', 'equals', 0o5014, line=649)

# BIT 3 FLAG 2
#   = 042D

# BIT 2 FLAG 2
S('CALCMAN2', 'equals', 0o53, line=655)  # PERFORM MANEUVER      BYPASS STARTING
# STARTING PROCEDURE    PROCEDURE

S('CALC2BIT', 'equals', 0o5016, line=658)

# BIT 1 FLAG 2
S('NODOFLAG', 'equals', 0o54, line=661)  # V37 NOT PERMITTED     V37 PERMITTED

S('NODOBIT', 'equals', 0o5017, line=663)

S('FLAGWRD3', 'equals', 0o77, line=665)  # (045-059)
# (SET)                 (RESET)

# BIT 15 FLAG 3
#   = 045D

# BIT 14 FLAG 3
S('GLOKFAIL', 'equals', 0o56, line=672)  # GIMBAL LOCK HAS       NOT IN GIMBAL LOCK
# OCCURRED

S('GLOKFBIT', 'equals', 0o5002, line=675)

# Page 52

# BIT 13 FLAG 3
S('REFSMFLG', 'equals', 0o57, line=680)  # REFSMMAT GOOD         REFSMMAT NO GOOD

S('REFSMBIT', 'equals', 0o5003, line=682)

# BIT 12 FLAG 3
S('LUNAFLAG', 'equals', 0o60, line=685)  # LUNAR LAT-LONG        EARTH LAT-LONG

S('LUNABIT', 'equals', 0o5004, line=687)

# BIT 11 FLAG 3
S('P22MKFLG', 'equals', 0o61, line=690)  # P22 DOWNLINKED MARK   P22 DOWNLINK MARK
# DATA WAS JUST TAKEN   DATA NOT JUST TAKEN

S('P22MKBIT', 'equals', 0o5005, line=693)

# BIT 10 FLAG 3
S('VFLAG', 'equals', 0o62, line=696)  # LESS THAN TWO STARS   TWO STARS IN FIELD
# IN FIELD OF VIEW      OF VIEW

S('VFLAGBIT', 'equals', 0o5006, line=699)

# BIT 9 FLAG 3
#   = 051D

# BIT 8 FLAG 3
S('PRECIFLG', 'equals', 0o64, line=705)  # CSMPREC OR LEMPREC    INTEGRV
# OR INTEGRVS CALLED    CALLED

S('PRECIBIT', 'equals', 0o5010, line=708)

# BIT 7 FLAG 3
S('CULTFLAG', 'equals', 0o65, line=711)  # STAR OCCULTED         STAR NOT OCCULTED

S('CULTBIT', 'equals', 0o5011, line=713)

# BIT 6 FLAG 3
S('ORBWFLAG', 'equals', 0o66, line=716)  # W MATRIX VALID FOR    W MATRIX INVALID FOR
# ORBITAL NAVIGATION    ORBITAL NAVIGATION

S('ORBWFBIT', 'equals', 0o5012, line=719)

# BIT 5 FLAG 3
S('STATEFLG', 'equals', 0o67, line=722)  # PERMANENT STATE       PERMANENT STATE
# VECTOR UPDATED        VECTOR NOT UPDATED

S('STATEBIT', 'equals', 0o5013, line=725)

# BIT 4 FLAG 3
S('INTYPFLG', 'equals', 0o70, line=728)  # CONIC INTEGRATION     ENCKE INTEGRATION
# Page 53
S('INTYBIT', 'equals', 0o5014, line=730)

# BIT 3 FLAG 3
S('VINTFLAG', 'equals', 0o71, line=733)  # CSM STATE VECTOR      LEM STATE VECTOR
# BEING INTEGRATED      BEING INTEGRATED

S('VINTFBIT', 'equals', 0o5015, line=736)

# BIT 2 FLAG 3
S('D6OR9FLG', 'equals', 0o72, line=739)  # DIMENSION OF W IS 9   DIMENSION OF W IS 6
# FOR INTEGRATION       FOR INTEGRATION

S('D6OR9BIT', 'equals', 0o5016, line=742)

# BIT 1 FLAG 3
S('DIM0FLAG', 'equals', 0o73, line=745)  # W MATRIX IS TO BE     W MATRIX IS NOT TO
# USED                  BE USED

S('FLAGWRD4', 'equals', 0o100, line=748)  # (060-074)
# (SET)                 (RESET)

S('DIM0BIT', 'equals', 0o5017, line=751)

# BIT 15 FLAG 4
S('MRKIDFLG', 'equals', 0o74, line=754)  # MARK DISPLAY IN       NO MARK DISPLAY IN
# ENDIDLE               ENDIDLE

S('MRKIDBIT', 'equals', 0o5001, line=757)

# BIT 14 FLAG 4
S('PRIODFLG', 'equals', 0o75, line=760)  # PRIORITY DISPLAY IN   NO PRIORITY DISPLAY
# ENDIDLE               IN ENDIDLE

S('PRIODBIT', 'equals', 0o5002, line=763)

# BIT 13 FLAG 4
S('NRMIDFLG', 'equals', 0o76, line=766)  # NORMAL DISPLAY IN     NO NORMAL DISPLAY
# ENDIDLE               IN ENDIDLE

S('NRMIDBIT', 'equals', 0o5003, line=769)

# BIT 12 FLAG 4
S('PDSPFLAG', 'equals', 0o77, line=772)  # CAN'T INTERRUPT       SEE M. HAMILTON
# PRIORITY DISPLAY

S('PDSPFBIT', 'equals', 0o5004, line=775)

# BIT 11 FLAG 4
S('MWAITFLG', 'equals', 0o100, line=778)  # HIGHER PRIORITY       NO HIGHER PRIORITY
# Page 54
# DISPLAY OPERATING     DISPLAY OPERATING
# WHEN MARK DISPLAY     WHEN MARK DISPLAY
# INITIATED             INITIATED
S('MWAITBIT', 'equals', 0o5005, line=783)

# BIT 10 FLAG 4
S('NWAITFLG', 'equals', 0o101, line=786)  # HIGHER PRIORITY       NO HIGHER PRIORITY
# DISPLAY OPERATING     DISPLAY OPERATING
# WHEN NORMAL           WHEN NORMAL DISPLAY
# DISPLAY INITIATED     INITIATED

S('NWAITBIT', 'equals', 0o5006, line=791)

# BIT 9 FLAG 4
S('MRKNVFLG', 'equals', 0o102, line=794)  # ASTRONAUT USING       ASTRONAUT NOT USING
# KEYBOARD WHEN MARK    KEYBOARD WHEN MARK
# DISPLAY INITIATED     DISPLAY INITIATED

S('MRKNVBIT', 'equals', 0o5007, line=798)

# BIT 8 FLAG 4
S('NRMNVFLG', 'equals', 0o103, line=801)  # ASTRONAUT USING       ASTRONAUT NOT USING
# KEYBOARD WHEN         KEYBOARD WHEN
# NORMAL DISPLAY        NORMAL DISPLAY
# INITIATED             INITIATED

S('NRMNVBIT', 'equals', 0o5010, line=806)

# BIT 7 FLAG 4
S('PRONVFLG', 'equals', 0o104, line=809)  # ASTRONAUT USING       ASTRONAUT NOT USING
# KEYBOARD WHEN         KEYBOARD WHEN
# PRIORITY DISPLAY      PRIORITY DISPLAY
# INITIATED             INITIATED

S('PRONVBIT', 'equals', 0o5011, line=814)

# BIT 6 FLAG 4
S('PINBRFLG', 'equals', 0o105, line=817)  # ASTRONAUT HAS         ASTRONAUT HAS NOT
# INTERFERED WITH       INTERFERED WITH
# EXISTING DISPLAY      EXISTING DISPLAY

S('PINBRBIT', 'equals', 0o5012, line=821)

# BIT 5 FLAG 4
S('MRUPTFLG', 'equals', 0o106, line=824)  # MARK DISPLAY          MARK DISPLAY NOT
# INTERRUPTED BY        INTERRUPTED BY
# PRIORITY DISPLAY      PRIORITY DISPLAY

S('MRUPTBIT', 'equals', 0o5013, line=828)
# Page 55

# BIT 4 FLAG 4
S('NRUPTFLG', 'equals', 0o107, line=832)  # NORMAL DISPLAY        NORMAL DISPLAY NOT
# INTERRUPTED BY        INTERRUPTED BY
# PRIORITY OR MARK      PRIORITY OR MARK
# DISPLAY               DISPLAY

S('NRUPTBIT', 'equals', 0o5014, line=837)

# BIT 3 FLAG 4
S('MKOVFLAG', 'equals', 0o110, line=840)  # MARK DISPLAY OVER     NO MARK DISPLAY OVER
# NORMAL                NORMAL

S('MKOVBIT', 'equals', 0o5015, line=843)

# BIT 2 FLAG 4                          # DISPLAY BIT
#   = 073D  # CLEARED AT INTERVALS

# BIT 1 FLAG 4
S('XDSPFLAG', 'equals', 0o112, line=849)  # MARK DISPLAY NOT TO   NO SPECIAL MARK
# BE INTERRUPTED        INFORMATION

S('XDSPBIT', 'equals', 0o5017, line=852)

S('FLAGWRD5', 'equals', 0o101, line=854)  # (075-099)
# (SET)                 (RESET)

# BIT 15 FLAG 5
S('DSKYFLAG', 'equals', 0o113, line=858)  # DISPLAYS SENT TO      NO DISPLAYS TO DSKY
# DSKY
S('DSKYBIT', 'equals', 0o5001, line=860)

# BIT 14 FLAG 5
S('RETROFLG', 'equals', 0o114, line=863)  # P37 PREMANEUVER       ORBIT NOT RETROGRADE
S('RETROBIT', 'equals', 0o5002, line=864)  # ORBIT IS RETROGRADE

# BIT 13 FLAG 5
S('SLOWFLG', 'equals', 0o115, line=867)  # P37 TRANSEARTH        SLOW DOWN IS NOT
S('SLOWBIT', 'equals', 0o5003, line=868)  # COAST SLOW DOWN       DESIRED
# IS DESIRED

# BIT 12 FLAG 5
S('V59FLAG', 'equals', 0o116, line=872)  # CALIBRATING FOR       NORMAL MARKING FOR
# P23                   P23

S('V59FLBIT', 'equals', 0o5004, line=875)

# BIT 11 FLAG 5
# Page 56
S('INCORFLG', 'equals', 0o117, line=879)  # FIRST INCORPORATION   SECOND INCORPORATION

S('INCORBIT', 'equals', 0o5005, line=881)

# BIT 10 FLAG 5
S('RNGSCFLG', 'equals', 0o120, line=884)  # ANOTHER TAG FOR PRFTRKAT

# BIT 10 FLAG 5
S('PRFTRKAT', 'equals', 0o120, line=887)  # PREF TRACK ATT        +K AXIS TRACK ATT

S('PRFTRBIT', 'equals', 0o5006, line=889)

# BIT 9 FLAG 5
S('DMENFLG', 'equals', 0o121, line=892)  # DIMENSION OF W IS 9   DIMENSION OF W IS 6
# FOR INCORPORATION     FOR INCORPORATION

S('DMENFBIT', 'equals', 0o5007, line=895)

# BIT 8 FLAG 5
S('COMPUTER', 'equals', 0o122, line=898)  # COMPUTER IS CMC       COMPUTER IS LGC

S('COMPTBIT', 'equals', 0o5010, line=900)

# BIT 7 FLAG 5
S('ENGONFLG', 'equals', 0o123, line=903)  # ENGINE TURNED ON      ENGINE TURNED OFF

S('ENGONBIT', 'equals', 0o5011, line=905)

# BIT 6 FLAG 5
S('3AXISFLG', 'equals', 0o124, line=908)  # MANEUVER SPECIFIED    MANEUVER SPECIFIED
# BY THREE AXES         BY ONE AXIS

S('3AXISBIT', 'equals', 0o5012, line=911)

# BIT 5 FLAG 5
S('GRRBKFLG', 'equals', 0o125, line=914)  # BACKUP GRR RECEIVED   BACKUP GRR NOT
# RECEIVED

S('GRRBKBIT', 'equals', 0o5013, line=917)

# BIT 4 FLAG 5
S('R60FLAG', 'equals', 0o126, line=920)  # R61 MUST USE R60      NORMAL R61

S('R60FLBIT', 'equals', 0o5014, line=922)

# BIT 3 FLAG 5
S('SOLNSW', 'equals', 0o127, line=925)  # LAMBERT DOES NOT      LAMBERT CONVERGES OR
# Page 57
# CONVERGE, OR TIME-    TIME-RADIUS NON
# RADIUS NEARLY CIRC.   CIRCULAR.
S('SOLNSBIT', 'equals', 0o5015, line=929)

# BIT 2 FLAG 5
S('MGLVFLAG', 'equals', 0o130, line=932)  # LOCAL VERTICAL        MIDDLE GIMBAL ANGLE
# COORDINATES           COMPUTED
# COMPUTED

S('MGLVFBIT', 'equals', 0o5016, line=936)

# BIT 1 FLAG 5
S('RENDWFLG', 'equals', 0o131, line=939)  # W MATRIX VALID        W MATRIX INVALID
# FOR RENDEZVOUS        FOR RENDEZVOUS
# NAVIGATION            NAVIGATION

S('RENDWBIT', 'equals', 0o5017, line=943)

S('FLAGWRD6', 'equals', 0o102, line=945)  # (090-104)
# (SET)                 (RESET)

# BIT 15 FLAG 6
S('DAPBIT1', 'equals', 0o132, line=949)  # 1 SATURN 1 TVC        0 RCS   0 NO

S('DAP1BIT', 'equals', 0o5001, line=951)

# BIT 14 FLAG 6
S('DAPBIT2', 'equals', 0o133, line=954)  # 1 A/P    0 A/P        1 A/P   0 A/P

S('DAP2BIT', 'equals', 0o5002, line=956)

# BIT 13 FLAG 6
S('STRULLSW', 'equals', 0o134, line=959)  # DO STEERULL           DO ULAGEOFF ONLY

S('STRULBIT', 'equals', 0o5003, line=961)

# BIT 13 FLAG 6
S('ENTRYDSP', 'equals', 0o134, line=964)  # DO ENTRY DISPLAY      OMIT ENTRY DISPLAY
# VIA ENTRYVN.

S('ENDSPBIT', 'equals', 0o5003, line=967)

# BIT 12 FLAG 6
S('CMDAPARM', 'equals', 0o135, line=970)  # ALLOW ENTRY FIRINGS   INHIBIT ENTRY FIRING
# AND CALCULATIONS      AND CONTROL FUNCTION
# Page 58
S('CMDARMBIT', 'equals', 0o5004, line=973)

# BIT 11 FLAG 6
S('GAMDIFSW', 'equals', 0o136, line=976)  # CALCULATE GAMDOT      GAMDOT NOT TO BE
# CALCULATED

S('GMDIFBIT', 'equals', 0o5005, line=979)

# BIT 10 FLAG 6
S('GONEPAST', 'equals', 0o137, line=982)  # LATERAL CONTROL       LATERAL CONTROL
# CALCULATIONS TO BE    CALCULATIONS TO BE
# OMITTED               DONE

S('GONEBIT', 'equals', 0o5006, line=986)

# BIT 9 FLAG 6
S('RELVELSW', 'equals', 0o140, line=989)  # TARGETING USES        TARGETING USES
# EARTH-RELATIVE        INERTIAL VELOCITY
# VELOCITY.

S('RELVBIT', 'equals', 0o5007, line=993)

# BIT 8 FLAG 6
S('EGSW', 'equals', 0o141, line=996)  # IN FINAL PHASE        NOT IN FINAL PHASE

S('EGFLGBIT', 'equals', 0o5010, line=998)

# BIT 8 FLAG 6
S('KNOWNFLG', 'equals', 0o141, line=1001)  # LANDMARK KNOWN        LANDMARK UNKNOWN

S('KNOWNBIT', 'equals', 0o5010, line=1003)

# BIT 8 FLAG 6
S('R57FLAG', 'equals', 0o141, line=1006)  # DO NOT DO R57         DO R57, TRUNION
# TRUNION BIAS HAS      BIAS NEEDED
# BEEN OBTAINED.

S('R57BIT', 'equals', 0o5010, line=1010)

# BIT 7 FLAG 6
S('NOSWITCH', 'equals', 0o142, line=1013)  # LATERAL ROLL          LATERAL ROLL MANEUVER
# MANEUVER INHIBITED    PERMITTED IN ENTRY
# IN ENTRY

S('NOSWBIT', 'equals', 0o5011, line=1017)

# BIT 6 FLAG 6
S('HIND', 'equals', 0o143, line=1020)  # ITERATING HUNTEST     ITERATING OF HUNTEST
# CALCULATIONS TO BE    CALCULATIONS TO BE
# DONE AFTER RANGE      OMITTED AFTER RANGE
# PREDICTION            PREDICTION
# Page 59

S('HINDBIT', 'equals', 0o5012, line=1026)

# BIT 5 FLAG 6
S('INRLSW', 'equals', 0o144, line=1029)  # INITIAL ROLL          INITIAL ROLL
# V(LV)                 V(LV)

S('INRLBIT', 'equals', 0o5013, line=1032)

# ATTITUDE NOT HELD     ATTITUDE HELD

# BIT 4 FLAG 6
S('LATSW', 'equals', 0o145, line=1037)  # DOWNLIFT NOT          DOWNLIFT INHIBITED
# INHIBITED

S('LATSWBIT', 'equals', 0o5014, line=1040)

# BIT 3 FLAG 6
S('.05GSW', 'equals', 0o146, line=1043)  # DRAG OVER .05G        DRAG LESS THAN .05G

S('.05GBIT', 'equals', 0o5015, line=1045)

# BIT 3 FLAG 6
#   = 102D

# BIT 2 FLAG 6
S('CM/DSTBY', 'equals', 0o147, line=1051)  # ENTRY DAP ACTIVATED   ENTRY DAP NOT
# ACTIVATED

S('CM/DSBIT', 'equals', 0o5016, line=1054)

# BIT 1 FLAG 6
S('GYMDIFSW', 'equals', 0o150, line=1057)  # CDU DIFFERENCES AND   CDU DIFFERENCES AND
# BODY RATES COMPUTED   BODY RATES NOT
# COMPUTED

S('GYMDIBIT', 'equals', 0o5017, line=1061)

S('FLAGWRD7', 'equals', 0o103, line=1063)  # (105-119)
# (SET)                 (RESET)

# BIT 15 FLAG 7
S('TERMIFLG', 'equals', 0o151, line=1067)  # TERMINATE R52         DO NOT TERMINATE R52

S('TERMIBIT', 'equals', 0o5001, line=1069)

# BIT 14 FLAG 7
S('ITSWICH', 'equals', 0o152, line=1072)  # ACCEPT NEXT LAMBERT   TEST LAMBERT ANSWER
# TPI SEARCH SOLUTION   AGAINST LIMITS
# Page 60

S('ITSWBIT', 'equals', 0o5002, line=1076)

# BIT 13 FLAG 7
S('IGNFLAG', 'equals', 0o153, line=1079)  # TIG HAS ARRIVED       TIG HAS NOT ARRIVED

S('IGNFLBIT', 'equals', 0o5003, line=1081)

# BIT 12 FLAG 7
S('ASTNFLAG', 'equals', 0o154, line=1084)  # ASTRONAUT HAS         ASTRONAUT HAS NOT
# OKAYED IGNITION       OKAYED IGNITION

S('ASTNBIT', 'equals', 0o5004, line=1087)

# BIT 11 FLAG 7
S('TIMRFLAG', 'equals', 0o155, line=1090)  # CLOKTASK OPERATING    CLOKTASK INOPERATIVE

S('TIMRBIT', 'equals', 0o5005, line=1092)

# BIT 10 FLAG 7
S('NORMSW', 'equals', 0o156, line=1095)  # UNIT NORMAL INPUT     LAMBERT COMPUTE ITS
# TO LAMBERT.           OWN UNIT NORMAL.

S('NORMSBIT', 'equals', 0o5006, line=1098)

# BIT 9 FLAG 7
S('RVSW', 'equals', 0o157, line=1101)  # DO NOT COMPUTE FINAL  COMPUTE FINAL STATE
# STATE VECTOR IN       VECTOR IN TIME-THETA
# TIME-THETA

S('RVSWBIT', 'equals', 0o5007, line=1105)

# BIT 8 FLAG 7
S('GONEBY', 'equals', 0o160, line=1108)  # PASSED TARGET         APPROACHING TARGET

S('GONBYBIT', 'equals', 0o5010, line=1110)

# BIT 7 FLAG 7
#   = 113D

# BIT 6 FLAG 7
S('V37FLAG', 'equals', 0o162, line=1116)  # AVERAGEG (SERVICER)   AVERAGEG (SERVICER)
# RUNNING               OFF

S('V37FLBIT', 'equals', 0o5012, line=1119)

# BIT 5 FLAG 7
#   = 115D
# Page 61
#   = BIT5

# BIT 4 FLAG 7
S('UPLOCKFL', 'equals', 0o164, line=1127)  # K-KBAR-K FAIL         NO K-KBAR-K FAIL

S('UPLOCBIT', 'equals', 0o5014, line=1129)

# BIT 3 FLAG 7
S('VERIFLAG', 'equals', 0o165, line=1132)  # CHANGED WHEN V33E OCCURS AT END OF P27

S('VERIFBIT', 'equals', 0o5015, line=1134)

# BIT 2 FLAG 7
S('ATTCHFLG', 'equals', 0o166, line=1137)  # LM,CM ATTACHED        LM,CM NOT ATTACHED

S('ATTCHBIT', 'equals', 0o5016, line=1139)

# BIT 1 FLAG 7
S('TFFSW', 'equals', 0o167, line=1142)  # CALCULATE TPERIGEE    CALCULATE TFF

S('TFFSWBIT', 'equals', 0o5017, line=1144)

S('FLAGWRD8', 'equals', 0o104, line=1146)  # (120-134)
# (SET)                 (RESET)

# BIT 15 FLAG 8
S('RPQFLAG', 'equals', 0o170, line=1150)  # RPQ NOT COMPUTED      RPQ COMPUTED

S('RPQFLBIT', 'equals', 0o5001, line=1152)

# BIT 14 FLAG 8
#   = 121D

# BIT 13 FLAG 8
S('NEWIFLG', 'equals', 0o172, line=1158)  # FIRST PASS THROUGH    SUCCEEDING ITERATION
# INTEGRATION           OF INTEGRATION

S('NEWIBIT', 'equals', 0o5003, line=1161)

# BIT 12 FLAG 8
S('CMOONFLG', 'equals', 0o173, line=1164)  # PERMANENT CSM STATE   PERMANENT CSM STATE
# IN LUNAR SPHERE       IN EARTH SPHERE

S('CMOONBIT', 'equals', 0o5004, line=1167)

# BIT 11 FLAG 8
S('LMOONFLG', 'equals', 0o174, line=1170)  # PERMANENT LM STATE    PERMANENT LM STATE
# IN LUNAR SPHERE       IN EARTH SPHERE

S('LMOONBIT', 'equals', 0o5005, line=1173)

# Page 62

# BIT 10 FLAG 8
S('ADVTRK', 'equals', 0o175, line=1178)  # ADVANCE GROUND TRACK  NOT ADVANCED
# SIGHTING WANTED       GROUND TRACK

S('ADVTKBIT', 'equals', 0o5006, line=1181)

# BIT 9 FLAG 8
S('P39/79SW', 'equals', 0o176, line=1184)  # P39/79 OPERATING      P38/78 OPERATING

S('P39SWBIT', 'equals', 0o5007, line=1186)

# BIT 8 FLAG 8
S('SURFFLAG', 'equals', 0o177, line=1189)  # LM ON LUNAR SURFACE   LM NOT ON LUNAR
# SURFACE

S('SURFFBIT', 'equals', 0o5010, line=1192)

# BIT 7 FLAG 8
S('INFINFLG', 'equals', 0o200, line=1195)  # NO CONIC SOLUTION     CONIC SOLUTION
# (CLOSURE THROUGH      EXISTS.
# INFINITY REQUIRED).

S('INFINBIT', 'equals', 0o5011, line=1199)

# BIT 6 FLAG 8
S('ORDERSW', 'equals', 0o201, line=1202)  # ITERATOR USES 2ND     ITERATOR USES 1ST
# ORDER MINIMUM MODE    ORDER STANDARD MODE

S('ORDERBIT', 'equals', 0o5012, line=1205)

# BIT 5 FLAG 8
S('APSESW', 'equals', 0o202, line=1208)  # RDESIRED OUTSIDE      RDESIRED INSIDE
# PERICENTER-APOCENTER  PERICENTER-APOCENTER
# RANGE IN TIME-RAD     RANGE IN TIME-RADIUS

S('APSESBIT', 'equals', 0o5013, line=1212)

# BIT 4 FLAG 8
S('COGAFLAG', 'equals', 0o203, line=1215)  # NO CONIC SOLUTION     CONIC SOLUTION
# TOO CLOSE TO          EXISTS (COGA DOES
# RECTILINEAR (COGA     NOT OVERFLOW).
# OVERFLOWS).
S('COGAFBIT', 'equals', 0o5014, line=1219)

# Page 63

# BIT 3 FLAG 8
S('V96ONFLG', 'equals', 0o204, line=1224)  # P00 INTEGRATION HAS   P00 INTEGRATION IS
# BEEN INHIBITED BY     PROCEEDING REGULARLY
# V96

# BIT 2 FLAG 8
#   = 133D

# BIT 1 FLAG 8
S('360SW', 'equals', 0o206, line=1232)  # TRANSFER ANGLE NEAR   TRANSFER ANGLE NOT
# 360 DEGREES           NEAR 360 DEGREES

S('360SWBIT', 'equals', 0o5017, line=1235)

S('FLAGWRD9', 'equals', 0o105, line=1237)  # (135-149)
# (SET)                 (RESET)

# BIT 15 FLAG 9
S('SWTOVER', 'equals', 0o207, line=1241)  # SWITCHOVER HAS        NO SWITCHOVER YET
# OCCURRED.

S('SWTOVBIT', 'equals', 0o5001, line=1244)

# BIT 14 FLAG 9
#   = 136D

S('V67FLBIT', 'equals', 0o5002, line=1249)

# BIT 13 FLAG 9
S('V82EMFLG', 'equals', 0o211, line=1252)  # MOON VICINITY         EARTH VICINITY

S('V82EMBIT', 'equals', 0o5003, line=1254)

# BIT 12 FLAG 9
S('MAXDBFLG', 'equals', 0o212, line=1257)  # MAX DB SELECTED       MIN DB SELECTED

S('MAXDBBIT', 'equals', 0o5004, line=1259)

# BIT 11 FLAG 9
S('V94FLAG', 'equals', 0o213, line=1262)  # V94 ALLOWED DURING    V94 NOT ALLOWED
# P23

S('V94FLBIT', 'equals', 0o5005, line=1265)

# BIT 10 FLAG 9
S('SAVECFLG', 'equals', 0o214, line=1268)  # P23 DISPLAY AND       P23 DISPLAY AND
# DATA STORAGE AFTER    DATA STORAGE BEFORE
# Page 64
# MARK IS DONE          MARK IS DONE

S('SAVECBIT', 'equals', 0o5006, line=1273)

# BIT 9 FLAG 9
S('VHFRFLAG', 'equals', 0o215, line=1276)  # ALLOW R22 TO          STOP ACCEPTANCE
# ACCEPT RANGE          OF RANGE DATA
# DATA

S('VHFRBIT', 'equals', 0o5007, line=1280)

# BIT 8 FLAG 9
S('SOURCFLG', 'equals', 0o216, line=1283)  # SOURCE OF INPUT       SOURCE OF INPUT
# DATA IS FROM          DATA IS FROM
# VHF RADAR             OPTICS MARK

S('SOURCBIT', 'equals', 0o5010, line=1287)

# BIT 7 FLAG 9
S('R22CAFLG', 'equals', 0o217, line=1290)  # R-22 CALCULATIONS     R-22 CALCULATIONS
# ARE GOING ON          ARE NOT GOING ON

S('R22CABIT', 'equals', 0o5011, line=1293)

# BIT 6 FLAG 9
S('N22ORN17', 'equals', 0o220, line=1296)  # COMPUTE TOTAL         COMPUTE TOTAL
# ATTITUDE ERRORS       ATTITUDE ERRORS
# W.R.T. N22 (V62)      W.R.T. N17 (V63)

S('N2217BIT', 'equals', 0o5012, line=1300)

# BIT 5 FLAG 9
S('QUITFLAG', 'equals', 0o221, line=1303)  # TERMINATE AND EXIT    CONTINUE INTEGRATION
S('QUITBIT', 'equals', 0o5013, line=1304)  # FROM INTEGRATION

# BIT 4 FLAG 9
S('R31FLAG', 'equals', 0o222, line=1307)  # R31 SELECTED (V63)    R34 SELECTED (V65)

S('R31FLBIT', 'equals', 0o5014, line=1309)

# BIT 3 FLAG 9
S('MID1FLAG', 'equals', 0o223, line=1312)  # INTEGRATE TO TDEC     INTEGRATE TO THE
# THEN-PRESENT TIME

S('MID1FBIT', 'equals', 0o5015, line=1315)

# BIT 2 FLAG 9
S('MIDAVFLG', 'equals', 0o224, line=1318)  # INTEGRATION ENTERED   INTEGRATION WAS
# FROM ONE OF MIDTOAV   NOT ENTERED VIA
# PORTALS               MIDTOAV
# Page 65

S('MIDAVBIT', 'equals', 0o5016, line=1323)

# BIT 1 FLAG 9
S('AVEMIDSW', 'equals', 0o225, line=1326)  # AVETOMID CALLING      NO AVETOMID W INTEGER
# FOR W MATRIX INTEGR   ALLOW SET UP RN,VN,
# DON'T WRITE OVER RN,  PIPTIME
# VN,PIPTIME

S('AVEMDBIT', 'equals', 0o5017, line=1331)

S('FLGWRD10', 'equals', 0o106, line=1333)  # (150-164)
# (SET)                 (RESET)

S('RASFLAG', 'equals', 0o106, line=1336)

# BIT 15 FLAG 10
#   = 150D

# BIT 14 FLAG 10
S('INTFLAG', 'equals', 0o227, line=1342)  # INTEGRATION IN        INTEGRATION NOT IN
# PROGRESS              PROGRESS

S('INTFLBIT', 'equals', 0o5002, line=1345)

# BIT 13 FLAG 10
#   = 152D

# BIT 12 FLAG 10
#   = 153D

# BIT 11 FLAG 10
#   = 154D

# BIT 10 FLAG 10
#   = 155D

# BIT 9 FLAG 10
#   = 156D

# BIT 8 FLAG 10
#   = 157D
# Page 66

# BIT 7 FLAG 10
S('REINTFLG', 'equals', 0o236, line=1367)  # INTEGRATION ROUTINE   INTEGRATION ROUTINE
# TO BE RESTARTED       NOT TO BE RESTARTED
S('REINTBIT', 'equals', 0o5011, line=1369)

# BIT 6 FLAG 10
#   = 159D

# BIT 5 FLAG 10
#   = 160D

# BIT 4 FLAG 10
#   = 161D

# BIT 3 FLAG 10
#   = 162D

# BIT 2 FLAG 10
#   = 163D

# BIT 1 FLAG 10
#   = 164D

S('FLGWRD11', 'equals', 0o107, line=1389)  # (165-179)
# (SET)                 (RESET)

# BIT 15 FLAG 11
S('S32.1F1', 'equals', 0o245, line=1393)  # DELTAN AT CSI TIME    DVT1 LESS THAN MAX
S('S32BIT1', 'equals', 0o5001, line=1394)  # ONE EXCEEDS MAX

# BIT 14 FLAG 11
S('S32.1F2', 'equals', 0o246, line=1397)  # FIRST PASS OF         REITERATION OF
S('S32BIT2', 'equals', 0o5002, line=1398)  # NEWTON INTEGRATION    NEWTON

# BIT 13 FLAG 11
S('S32.1F3A', 'equals', 0o247, line=1401)  # BIT 13 AND BIT 12 FUNCTION AS AN ORDERED
S('S32BIT3A', 'equals', 0o5003, line=1402)  # PAIR (13,12) INDICATING THE POSSIBLE OC-
# CURRENCE OF 2NEWTON ITERATIONS FOR S32.1
# BIT 12 FLAG 11                        # IN THE PROGRAM IN THE FOLLOWING ORDER:
S('S32.1F3B', 'equals', 0o250, line=1405)  # (0,1) (I.E. BIT 13 RESET, BIT 12 SET)
# Page 67
S('S3229T3B', 'equals', 0o5004, line=1407)  #      = FIRST NEWTON ITERATION BEING DONE
# (0,0)= FIRST PASS OF 2ND NEWTON ITER.
# (1,1)= 50 FPS STAGE OF 2ND NEWT ITER.
# (1,0)= REMAINDER OF 2ND NEWT ITER.

# BIT 11 FLAG 11
#   = 169D

# BIT 10 FLAG 11
#   = 170D

# BIT 9 FLAG 11
#   = 171D

# BIT 8 FLAG 11
#   = 172D

# BIT 7 FLAG 11
#   = 173D

# BIT 6 FLAG 11
#   = 174D

# BIT 5 FLAG 11
#   = 175D

# BIT 4 FLAG 11
#   = 176D

# BIT 3 FLAG 11
#   = 177D

# BIT 2 FLAG 11
#   = 178D

# BIT 1 FLAG 11
#   = 179D

# Page 68
# GENERAL ERASABLE ASSIGNMENTS

#   SETLOC 61
# INTERRUPT TEMPORARY STORAGE POOL.     (11D)

# (ITEMP1 THROUGH RUPTREG4)

# ANY OF THESE MAY BE USED AS TEMPORARIES DURING INTERRUPT OR WITH INTERRUPT INHIBITED. THE ITEMP SERIES
# IS USED DURING CALLS TO THE EXECUTIVE AND WAITLIST -- THE RUPTREGS ARE NOT.

S('ITEMP1', 'erase', 0o61, line=1456)
S('WAITEXIT', 'equals', 0o61, line=1457)
S('EXECTEM1', 'equals', 0o61, line=1458)

S('ITEMP2', 'erase', 0o62, line=1460)
S('WAITBANK', 'equals', 0o62, line=1461)
S('EXECTEM2', 'equals', 0o62, line=1462)

S('ITEMP3', 'erase', 0o63, line=1464)
S('RUPTSTOR', 'equals', 0o63, line=1465)
S('WAITADR', 'equals', 0o63, line=1466)
S('NEWPRIO', 'equals', 0o63, line=1467)

S('ITEMP4', 'erase', 0o64, line=1469)
S('LOCCTR', 'equals', 0o64, line=1470)
S('WAITTEMP', 'equals', 0o64, line=1471)

S('ITEMP5', 'erase', 0o65, line=1473)
S('NEWLOC', 'equals', 0o65, line=1474)

S('ITEMP6', 'erase', 0o66, line=1476)
S('NEWLOC+1', 'equals', 0o66, line=1477)  # DP ADDRESS.

#   SETLOC 67
S('NEWJOB', 'erase', 0o67, line=1480)  # MUST BE AT LOC 67 DUE TO WIRING.

S('RUPTREG1', 'erase', 0o70, line=1482)
S('RUPTREG2', 'erase', 0o71, line=1483)
S('RUPTREG3', 'erase', 0o72, line=1484)
S('RUPTREG4', 'erase', 0o73, line=1485)
S('KEYTEMP1', 'equals', 0o73, line=1486)
S('DSRUPTEM', 'equals', 0o73, line=1487)

# FLAGWORD RESERVATIONS.                (12D)

S('STATE', 'erase', 0o74, line=1491)

# PAD LOAD FOR DAPS
S('EMDOT', 'erase', 0o110, line=1494)  # I(1)PL (SPS FLOW RATE, SC AT B+3 KG/CS)

# Page 69

# EXIT FOR V83
S('STATEXIT', 'erase', 0o111, line=1499)  # I(1) STQ ADDRESS FOR STATEXIT

# UNUSED ERASABLES ********(2)
S('ERASFILL', 'erase', 0o112, line=1502)

# EXEC TEMPORARIES WHICH MAY BE USED BETWEEN CCS NEWJOBS
# (INTB15+ THROUGH RUPTMXTM)            (32D)
S('INTB15+', 'erase', 0o114, line=1506)  # REFLECTS 15TH BIT OF INDEXABLE ADDRESSES
S('DSEXIT', 'equals', 0o114, line=1507)  # RETURN FOR DSPIN
S('EXITEM', 'equals', 0o114, line=1508)  # RETURN FOR SCALE FACTOR ROUTINE SELECT
S('BLANKRET', 'equals', 0o114, line=1509)  # RETURN FOR 2BLANK

S('INTBIT15', 'erase', 0o115, line=1511)  # SIMILAR TO ABOVE.
S('WRDRET', 'equals', 0o115, line=1512)  # RETURN FOR 5BLANK.
S('WDRET', 'equals', 0o115, line=1513)  # RETURN FOR DSPWD
S('DECRET', 'equals', 0o115, line=1514)  # RETURN FOR PUTCOM(DEC LOAD)
S('21/22REG', 'equals', 0o115, line=1515)  # TEMP FOR CHARIN

# THE REGISTERS BETWEEN ADDRWD AND PRIORITY MUST STAY IN THE FOLLOWING ORDER FOR INTERPRETIVE TRACE.

S('ADDRWD', 'erase', 0o116, line=1519)  # 12 BIT INTERPRETIVE OPERAND SUB-ADDRESS.
S('POLISH', 'erase', 0o117, line=1520)  # HOLDS CADR MADE FROM POLISH ADDRESSE.
S('UPDATRET', 'equals', 0o117, line=1521)  # RETURN FOR UPDATNN, UPDATVB
S('CHAR', 'equals', 0o117, line=1522)  # TEMP FOR CHARIN
S('ERCNT', 'equals', 0o117, line=1523)  # COUNTER FOR ERROR LIGHT RESET
S('DECOUNT', 'equals', 0o117, line=1524)  # COUNTER FOR SCALING AND DISPLAY (DEC)

S('FIXLOC', 'erase', 0o120, line=1526)  # WORK AREA ADDRESS
S('OVFIND', 'erase', 0o121, line=1527)  # SET NON-ZERO ON OVERFLOW.

S('VBUF', 'erase', 0o122, line=1529)  # TEMPORARY STORAGE USED FOR VECTORS.
S('SGNON', 'equals', 0o122, line=1530)  # TEMP FOR +,- ON
S('NOUNTEM', 'equals', 0o122, line=1531)  # COUNTER FOR MIXNOUN FETCH
S('DISTEM', 'equals', 0o122, line=1532)  # COUNTER FOR OCTAL DISPLAY VERB
S('DECTEM', 'equals', 0o122, line=1533)  # COUNTER FOR FETCH (DEC DISPLAY VERBS)

S('SGNOFF', 'equals', 0o123, line=1535)  # TEMP FOR +,- ON
S('NVTEMP', 'equals', 0o123, line=1536)  # TEMP FOR NVSUB
S('SFTEMP1', 'equals', 0o123, line=1537)  # STORAGE FOR SF CONST HI PART (=SFTEMP2-1)
S('HITEMIN', 'equals', 0o123, line=1538)  # TEMP FOR LOAD OF HRS,MIN,SEC
# MUST = LOTEMIN-1.

S('CODE', 'equals', 0o124, line=1541)  # FOR DSPIN
S('SFTEMP2', 'equals', 0o124, line=1542)  # STORAGE FOR SF CONST LO PART (=SFTEMP1+1)
S('LOTEMIN', 'equals', 0o124, line=1543)  # TEMP FOR LOAD OF HRS,MIN,SEC
# Page 70
# MUST = HITEMIN+1
S('MIXTEMP', 'equals', 0o125, line=1546)  # FOR MIXNOUN DATA
S('SIGNRET', 'equals', 0o125, line=1547)  # RETURN FOR +,- ON

# ALSO MIXTEMP+1 = VBUF+4, MIXTEMP+2 = VBUF+5

S('BUF', 'erase', 0o130, line=1551)  # TEMPORARY SCALAR STORAGE
S('BUF2', 'erase', 0o133, line=1552)
S('INDEXLOC', 'equals', 0o130, line=1553)  # CONTAINS ADDRESS OF SPECIFIED INDEX.
S('SWWORD', 'equals', 0o130, line=1554)  # ADDRESS OF SWITCH WORD
S('SWBIT', 'equals', 0o131, line=1555)  # SWITCH BIT WITHIN THE SWITCH WORD
S('MPTEMP', 'erase', 0o135, line=1556)  # TEMPORARY USED IN MULTIPLY AND SHIFT
S('DMPNTEMP', 'equals', 0o135, line=1557)  # DMPSUB TEMPORARY
S('DOTINC', 'erase', 0o136, line=1558)  # COMPONENT INCREMENT FOR DOT SUBROUTINE
S('DVSIGN', 'equals', 0o136, line=1559)  # DETERMINES SIGN OF DDV RESULT
S('ESCAPE', 'equals', 0o136, line=1560)  # USED IN ARCSIN/ARCCOS.
S('ENTRET', 'equals', 0o136, line=1561)  # EXIT FROM ENTER

S('DOTRET', 'erase', 0o137, line=1563)  # RETURN FROM DOT SUBROUTINE
S('DVNORMCT', 'equals', 0o137, line=1564)  # DIVIDEND NORMALIZATION COUNT IN DDV.
S('ESCAPE2', 'equals', 0o137, line=1565)  # ALTERNATE ARCSIN/ARCCOS SWITCH
S('WDCNT', 'equals', 0o137, line=1566)  # CHAR COUNTER FOR DSPWD
S('INREL', 'equals', 0o137, line=1567)  # INPUT BUFFER SELECTOR ( X,Y,Z, REG )

S('MATINC', 'erase', 0o140, line=1569)  # VECTOR INCREMENT IN MXV AND VXM
S('MAXDVSW', 'equals', 0o140, line=1570)  # +0 IF DP QUOTIENT IS NEAR ONE -- ELSE -1.
S('POLYCNT', 'equals', 0o140, line=1571)  # POLYNOMIAL LOOP COUNTER
S('DSPMMTEM', 'equals', 0o140, line=1572)  # DSPCOUNT SAVE FOR DSPMM
S('MIXBR', 'equals', 0o140, line=1573)  # INDICATOR FOR MIXED OR NORMAL NOUN

S('TEM1', 'erase', 0o141, line=1575)  # EXEC TEMP
S('POLYRET', 'equals', 0o141, line=1576)
S('DSREL', 'equals', 0o141, line=1577)  # REL ADDRESS FOR DSPIN

S('TEM2', 'erase', 0o142, line=1579)  # EXEC TEMP
S('DSMAG', 'equals', 0o142, line=1580)  # MAGNITUDE STORE FOR DSPIN
S('IDADDTEM', 'equals', 0o142, line=1581)  # MIXNOUN INDIRECT ADDRESS STORAGE

S('TEM3', 'erase', 0o143, line=1583)  # EXEC TEMP
S('COUNT', 'equals', 0o143, line=1584)  # FOR DSPIN

S('TEM4', 'erase', 0o144, line=1586)  # EXEC TEMP
S('LSTPTR', 'equals', 0o144, line=1587)  # LIST POINTER FOR GRABUSY
S('RELRET', 'equals', 0o144, line=1588)  # RETURN FOR RELDSP
S('FREERET', 'equals', 0o144, line=1589)  # RETURN FOR FREEDSP
S('DSPWDRET', 'equals', 0o144, line=1590)  # RETURN FOR DSPSIGN
S('SEPSCRET', 'equals', 0o144, line=1591)  # RETURN FOR SEPSEC
S('SEPMNRET', 'equals', 0o144, line=1592)  # RETURN FOR SEPMIN

S('TEM5', 'erase', 0o145, line=1594)  # EXEC TEMP
# Page 71
S('NOUNADD', 'equals', 0o145, line=1596)  # TEMP STORAGE FOR NOUN ADDRESS

S('NNADTEM', 'erase', 0o146, line=1598)  # TEMP FOR NOUN ADDRESS TABLE ENTRY
S('NNTYPTEM', 'erase', 0o147, line=1599)  # TEMP FOR NOUN TYPE TABLE ENTRY
S('IDAD1TEM', 'erase', 0o150, line=1600)  # TEMP FOR INDIR ADDRESS TABLE ENTRY (MIXNN)
# MUST = IDAD2TEM-1, = IDAD3TEM-2
S('IDAD2TEM', 'erase', 0o151, line=1602)  # TEMP FOR INDIR ADDRESS TABLE ENTRY (MIXNN)
# MUST = IDAD1TEM+1, IDAD3TEM-1.
S('IDAD3TEM', 'erase', 0o152, line=1604)  # TEMP FOR INDIR ADDRESS TABLE ENTRY (MIXNN)
# MUST = IDAD1TEM+2, IDAD2TEM+1.
S('RUTMXTEM', 'erase', 0o153, line=1606)  # TEMP FOR SF ROUT TABLE ENTRY (MIXNN ONLY)

# AX*SR*T STORAGE.                      (6D)
S('DEXDEX', 'equals', 0o142, line=1609)  # B(1)TMP
S('DEX1', 'equals', 0o143, line=1610)  # B(1)TMP
S('DEX2', 'equals', 0o144, line=1611)  # B(1)TMP
S('RTNSAVER', 'equals', 0o145, line=1612)  # B(1)TMP
S('TERM1TMP', 'equals', 0o133, line=1613)  # B(2)TMP

S('DEXI', 'equals', 0o143, line=1615)

# Page 72
# DYNAMICALLY ALLOCATED CORE SETS FOR JOBS      (84D)

S('MPAC', 'erase', 0o154, line=1620)  # MULTI-PURPOSE ACCUMULATOR.
S('MODE', 'erase', 0o163, line=1621)  # +1 FOR TP, +0 FOR DP, OR -1 FOR VECTOR.
S('LOC', 'erase', 0o164, line=1622)  # LOCATION ASSOCIATED WITH JOB.
S('BANKSET', 'erase', 0o165, line=1623)  # USUALLY CONTAINS BBANK SETTING.
S('PUSHLOC', 'erase', 0o166, line=1624)  # WORD OF PACKED INTERPRETIVE PARAMETERS.
S('PRIORITY', 'erase', 0o167, line=1625)  # PRIORITY OF PRESENT JOB AND WORK AREA.

#   ERASE +71D  # SEVEN SETS OF 12 REGISTERS EACH

# SPECIAL DOWNLINK BUFFER. -- OVERLAYED BY P27 STORAGE --

# P27 (UPDATE PROGRAM) STORAGE. -- OVERLAYS SPEC DNLNK BUFF -- (24D)

S('COMPNUMB', 'erase', 0o300, line=1633)  # B(1)TMP NUMBER OF ITEMS TO BE UPLINKED.
S('UPOLDMOD', 'equals', 0o301, line=1634)  # B(1)TMP HOLDS INTERRUPTED PROGRAM NUMBER
S('UPVERB', 'equals', 0o302, line=1635)  # B(1)TMP VERB NUMBER
S('UPCOUNT', 'equals', 0o303, line=1636)  # B(1)TMP UPBUFF INDEX
S('UPBUFF', 'equals', 0o304, line=1637)  # B(20D)

# MORE P27 STORAGE.                     (2D)

S('UPTEMP', 'erase', 0o330, line=1641)  # B(1)TMP SCRATCH
S('UPVERBSV', 'erase', 0o331, line=1642)  # B(1)TMP
S('INTWAK1Q', 'equals', 0o330, line=1643)  # (06D)
# (20 REGISTERS OF ENTRY DOWNLINK WILL GO HERE.)

# THE FOLLOWING ARE INDEXED FOR TM. IN ENTRY DAP.

S('CMTMTIME', 'equals', 0o304, line=1648)  # B(1) (VEHICLE BODY RATE INFO IS
S('SW/NDX', 'equals', 0o305, line=1649)  # B(1)  TELEMETERED EACH 0.2 SEC. DURING
S('ENDBUF', 'equals', 0o324, line=1650)  # B(1)  ENTRY.)

S('V1', 'equals', 0o325, line=1652)  # I(2) REENTRY, P64-P65
S('A0', 'equals', 0o327, line=1653)  # I(2) REENTRY, P64-P65
# HI-ORDER WORD ONLY ON DNLNK.

# ALIGNMENT STORAGE.                    (5D)
# (CANNOT SHARE WITH PRECISION INTEGRATION OR KEPLER STORAGE.)

S('QMAJ', 'equals', 0o300, line=1659)  # B(1)TMP
S('MARKINDX', 'equals', 0o301, line=1660)  # B(1)TMP
S('BESTI', 'equals', 0o302, line=1661)  # I(1)TMP
S('BESTJ', 'equals', 0o303, line=1662)  # I(1)TMP
S('STARIND', 'equals', 0o304, line=1663)  # I(1)TMP

# Page 73
# ALIGNMENT/S40.2,3 COMMON STORAGE.     (18D)

S('XSMD', 'equals', 0o306, line=1668)  # I(6)TMP
S('YSMD', 'equals', 0o314, line=1669)  # I(6)TMP
S('ZSMD', 'equals', 0o322, line=1670)  # I(6)TMP

S('XSCREF', 'equals', 0o306, line=1672)  # SPACE CRAFT AXES IN REF COORDS.
S('YSCREF', 'equals', 0o314, line=1673)
S('ZSCREF', 'equals', 0o322, line=1674)
S('ZPRIME', 'equals', 0o26, line=1675)
S('PDA', 'equals', 0o26, line=1676)
S('COSTH', 'equals', 0o20, line=1677)
S('SINTH', 'equals', 0o22, line=1678)
S('THETA', 'equals', 0o24, line=1679)
S('STARM', 'equals', 0o40, line=1680)

# DOWNLINK STORAGE                      (18D)

S('DNLSTADR', 'equals', 0o332, line=1684)  # CONTENTS NO LONGER AN ADDR BUT A CODE

S('DNLSTCOD', 'erase', 0o332, line=1686)  # B(1)PRM ID CODE OF DOWNLIST
S('DUMPCNT', 'erase', 0o333, line=1687)  # B(1)PRM
S('LDATALST', 'erase', 0o334, line=1688)  # B(1)
S('DNTMGOTO', 'erase', 0o335, line=1689)  # B(1)
S('TMINDEX', 'erase', 0o336, line=1690)  # B(1)
S('DUMPLOC', 'equals', 0o336, line=1691)  # CONTAINS ECADR OF AGC DP WORD BEING DUMPED
# AND COUNT OF COMPLETE DUMPS ALREADY
# SENT.
S('DNQ', 'erase', 0o337, line=1694)  # B(1)
S('DNTMBUFF', 'erase', 0o340, line=1695)  # B(12)PRM DOWNLINK SNAPSHOT BUFFER

# OPTICS MARKING, UNSHARED.             (8D)

S('MKNDX', 'erase', 0o354, line=1699)
S('MKT2T1', 'erase', 0o355, line=1700)
S('MKCDUY', 'erase', 0o357, line=1701)
S('MKCDUS', 'erase', 0o360, line=1702)
S('MKCDUZ', 'erase', 0o361, line=1703)
S('MKCDUT', 'erase', 0o362, line=1704)
S('MKCDUX', 'erase', 0o363, line=1705)

# FOR EXCLUSIVE USE OF SYS TEST STANDARD LEAD INS       (2)
S('EBUF2', 'erase', 0o364, line=1708)  # B(2) UNSHARED

# Page 74
# UNSWITCHED FOR DISPLAY INTERFACE ROUTINES.    (10D)

S('RESTREG', 'erase', 0o366, line=1713)  # B(1)PRM FOR DISPLAY RESTARTS.
S('NVWORD', 'erase', 0o367, line=1714)
S('MARKNV', 'erase', 0o370, line=1715)
S('NVSAVE', 'erase', 0o371, line=1716)
# (RETAIN THE ORDER OF CADRFLSH TO FAILREG +2 FOR DOWNLINK PURPOSES)
S('CADRFLSH', 'erase', 0o372, line=1718)  # B(1)TMP
S('CADRMARK', 'erase', 0o373, line=1719)  # B(1)TMP
S('TEMPFLSH', 'erase', 0o374, line=1720)  # B(1)TMP
S('FAILREG', 'erase', 0o375, line=1721)  # B(3)PRM 3 ALARM CODE REGISTERS

#   SETLOC 400

# VAC AREAS. -- BE CAREFUL OF PLACEMENT --      (220D)

S('VAC1USE', 'erase', 0o400, line=1727)  # B(1)PRM
S('VAC1', 'erase', 0o401, line=1728)  # B(43)PRM
S('VAC2USE', 'erase', 0o454, line=1729)  # B(1)PRM
S('VAC2', 'erase', 0o455, line=1730)  # B(43)PRM
S('VAC3USE', 'erase', 0o530, line=1731)  # B(1)PRM
S('VAC3', 'erase', 0o531, line=1732)  # B(43)PRM
S('VAC4USE', 'erase', 0o604, line=1733)  # B(1)PRM
S('VAC4', 'erase', 0o605, line=1734)  # B(43)PRM
S('VAC5USE', 'erase', 0o660, line=1735)  # B(1)PRM
S('VAC5', 'erase', 0o661, line=1736)  # B(43)PRM

# WAITLIST REPEAT FLAG.                 (1D)
S('RUPTAGN', 'erase', 0o734, line=1739)  # B(1)PRM
S('KEYTEMP2', 'equals', 0o734, line=1740)

# STARALIGN ERASABLES.                          (13D)

S('STARCODE', 'erase', 0o735, line=1744)  # B(1)DSP NOUN 70 FOR P22,51 AND R52,53
S('STARALGN', 'erase', 0o736, line=1745)
S('SINCDU', 'equals', 0o736, line=1746)
S('COSCDU', 'equals', 0o744, line=1747)

S('SINCDUX', 'equals', 0o742, line=1749)
S('SINCDUY', 'equals', 0o736, line=1750)
S('SINCDUZ', 'equals', 0o740, line=1751)
S('COSCDUX', 'equals', 0o750, line=1752)
S('COSCDUY', 'equals', 0o744, line=1753)
S('COSCDUZ', 'equals', 0o746, line=1754)

# PHASE TABLE AND RESTART COUNTERS              (12D)
# Page 75

S('-PHASE1', 'erase', 0o752, line=1759)  # B(1)PRM
S('PHASE1', 'erase', 0o753, line=1760)  # B(1)PRM
S('-PHASE2', 'erase', 0o754, line=1761)  # B(1)PRM
S('PHASE2', 'erase', 0o755, line=1762)  # B(1)PRM
S('-PHASE3', 'erase', 0o756, line=1763)  # B(1)PRM
S('PHASE3', 'erase', 0o757, line=1764)  # B(1)PRM
S('-PHASE4', 'erase', 0o760, line=1765)  # B(1)PRM
S('PHASE4', 'erase', 0o761, line=1766)  # B(1)PRM
S('-PHASE5', 'erase', 0o762, line=1767)  # B(1)PRM
S('PHASE5', 'erase', 0o763, line=1768)  # B(1)PRM
S('-PHASE6', 'erase', 0o764, line=1769)  # B(1)PRM
S('PHASE6', 'erase', 0o765, line=1770)  # B(1)PRM

# A**SR*T STORAGE                       (6D)

S('CDUSPOT', 'erase', 0o766, line=1774)  # B(6)

S('CDUSPOTY', 'equals', 0o766, line=1776)
S('CDUSPOTZ', 'equals', 0o770, line=1777)
S('CDUSPOTX', 'equals', 0o772, line=1778)

# VERB 37 STORAGE                       (2D)

S('MINDEX', 'erase', 0o774, line=1782)  # B(1)TMP INDEX FOR MAJOR MODE
S('MMNUMBER', 'erase', 0o775, line=1783)  # B(1)TMP MAJOR MODE REQUESTED BY V37

# PINBALL INTERRUPT ACTION              (1D)

S('DSPCNT', 'erase', 0o776, line=1787)  # B(1)PRM COUNTER FOR DSPOUT

# PINBALL EXECUTIVE ACTION              (44D)

S('DSPCOUNT', 'erase', 0o777, line=1791)  # DISPLAY POSITION INDICATOR
S('DECBRNCH', 'erase', 0o1000, line=1792)  # +DEC, -DEC, OCT INDICATOR
S('VERBREG', 'erase', 0o1001, line=1793)  # VERB CODE
S('NOUNREG', 'erase', 0o1002, line=1794)  # NOUN CODE
S('XREG', 'erase', 0o1003, line=1795)  # R1 INPUT BUFFER
S('YREG', 'erase', 0o1004, line=1796)  # R2 INPUT BUFFER
S('ZREG', 'erase', 0o1005, line=1797)  # R3 INPUT BUFFER
S('XREGLP', 'erase', 0o1006, line=1798)  # LO PART OF XREG (FOR DEC CONV ONLY)
S('YREGLP', 'erase', 0o1007, line=1799)  # LO PART OF YREG (FOR DEC CONV ONLY)
S('HITEMOUT', 'equals', 0o1007, line=1800)  # TEMP FOR DISPLAY OF HRS,MIN,SEC
# MUST = LOTEMOUT-1.
S('ZREGLP', 'erase', 0o1010, line=1802)  # LO PART OF ZREG (FOR DEC CONV ONLY)
S('LOTEMOUT', 'equals', 0o1010, line=1803)  # TEMP FOR DISPLAY OF HRS,MIN,SEC
# MUST = HITEMOUT+1
# Page 76
S('MODREG', 'erase', 0o1011, line=1806)  # MODE CODE
S('DSPLOCK', 'erase', 0o1012, line=1807)  # KEYBOARD/SUBROUTINE CALL INTERLOCK
S('REQRET', 'erase', 0o1013, line=1808)  # RETURN REGISTER FOR LOAD
S('LOADSTAT', 'erase', 0o1014, line=1809)  # STATUS INDICATOR FOR LOADTST
S('CLPASS', 'erase', 0o1015, line=1810)  # PASS INDICATOR FOR CLEAR
S('NOUT', 'erase', 0o1016, line=1811)  # ACTIVITY COUNTER FOR DSPTAB
S('NOUNCADR', 'erase', 0o1017, line=1812)  # MACHINE CADR FOR NOUN
S('MONSAVE', 'erase', 0o1020, line=1813)  # N/V CODE FOR MONITOR. (= MONSAVE1-1)
S('MONSAVE1', 'erase', 0o1021, line=1814)  # NOUNCADR FOR MONITOR (MATBS) = MONSAVE+1
S('MONSAVE2', 'erase', 0o1022, line=1815)  # B(1)PRM NVMONOPT OPTIONS
S('DSPTAB', 'erase', 0o1023, line=1816)  # 0-10D, DISPLAY PANEL BUFF.  11D, C/S LTS.
S('NVQTEM', 'erase', 0o1037, line=1817)  # NVSUB STORAGE FOR CALLING ADDRESS
# MUST = NVBNKTEM-1.
S('NVBNKTEM', 'erase', 0o1040, line=1819)  # NVSUB STORAGE FOR CALLING BANK
# MUST = NVQTEM+1
S('VERBSAVE', 'erase', 0o1041, line=1821)  # NEEDED FOR RECYCLE
S('CADRSTOR', 'erase', 0o1042, line=1822)  # ENDIDLE STORAGE
S('DSPLIST', 'erase', 0o1043, line=1823)  # WAITING REG FOR DSP SYST INTERNAL USE
S('EXTVBACT', 'erase', 0o1044, line=1824)  # EXTENDED VERB ACTIVITY INTERLOCK
S('DSPTEM1', 'erase', 0o1045, line=1825)  # BUFFER STORAGE AREA 1 (MOSTLY FOR TIME)
S('DSPTEM2', 'erase', 0o1050, line=1826)  # BUFFER STORAGE AREA 2 (MOSTLY FOR DEG)

S('DSPTEMX', 'equals', 0o1051, line=1828)  # B(2) S-S DISPLAY BUFFER FOR EXT. VERBS
S('NORMTEM1', 'equals', 0o1045, line=1829)  # B(3)DSP NORMAL DISPLAY REGISTERS.

# DISPLAY FOR EXTENDED VERBS            (2D)

S('OPTIONX', 'equals', 0o1051, line=1833)  # B(2) EXTENDED VERB OPTION CODE  N12(V82)

# TBASE'S AND PHSPRDT'S.                (12D)

S('TBASE1', 'erase', 0o1053, line=1837)  # B(1)PRM
S('PHSPRDT1', 'erase', 0o1054, line=1838)  # B(1)PRM
S('TBASE2', 'erase', 0o1055, line=1839)  # B(1)PRM
S('PHSPRDT2', 'erase', 0o1056, line=1840)  # B(1)PRM
S('TBASE3', 'erase', 0o1057, line=1841)  # B(1)PRM
S('PHSPRDT3', 'erase', 0o1060, line=1842)  # B(1)PRM
S('TBASE4', 'erase', 0o1061, line=1843)  # B(1)PRM
S('PHSPRDT4', 'erase', 0o1062, line=1844)  # B(1)PRM
S('TBASE5', 'erase', 0o1063, line=1845)  # B(1)PRM
S('PHSPRDT5', 'erase', 0o1064, line=1846)  # B(1)PRM
S('TBASE6', 'erase', 0o1065, line=1847)  # B(1)PRM
S('PHSPRDT6', 'erase', 0o1066, line=1848)  # B(1)PRM

# UNSWITCHED FOR DISPLAY INTERFACE ROUTINES.    (5D)
# Page 77
S('EBANKSAV', 'erase', 0o1067, line=1852)
S('MARKEBAN', 'erase', 0o1070, line=1853)
S('EBANKTEM', 'erase', 0o1071, line=1854)
S('MARK2PAC', 'erase', 0o1072, line=1855)
S('R1SAVE', 'erase', 0o1073, line=1856)

# IMU COMPENSATION UNSWITCHED ERASABLE. (1D)

S('1/PIPADT', 'erase', 0o1074, line=1860)  # B(1)PRM
S('OLDBT1', 'equals', 0o1074, line=1861)

# SINGLE PRECISION SUBROUTINE TEMPORARIES       (3D)
# SPSIN, SPCOS, SPROOT VARIABLES.
# DO NOT SHARE.  THESE ARE USED BY DAPS IN INTERRUPT
# AND CURRENTLY ARE NOT PROTECTED.  IF OTHER USERS
# MATERIALIZE, THEN THIS CAN BE CHANGED.

S('HALFY', 'erase', 0o1075, line=1869)
S('ROOTRET', 'erase', 0o1076, line=1870)
S('SQRARG', 'erase', 0o1077, line=1871)
S('TEMK', 'equals', 0o1075, line=1872)
S('SQ', 'equals', 0o1076, line=1873)

# Page 78
# UNSWITCHED FOR ORBIT INTEGRATION      (21D)

S('TDEC', 'erase', 0o1100, line=1878)  # I(2)
S('COLREG', 'equals', 0o1102, line=1879)  # I(1)
S('LAT', 'equals', 0o1103, line=1880)  # I(2)DSP NOUN 43,67 FOR P20,22,51 R52,53.
S('LANDLAT', 'equals', 0o1103, line=1881)  #         NOUN 89    FOR P22.
S('LONG', 'equals', 0o1105, line=1882)  # I(2)DSP NOUN 43,67 FOR P20,22,51 R52,53
S('ALT', 'equals', 0o1107, line=1883)  # I(2)DSP NOUN 43    FOR P20,22,51 R52,53.
S('YV', 'equals', 0o1111, line=1884)  # I(6)
S('ZV', 'equals', 0o1117, line=1885)  # I(6)

# MARK STORAGE.                         (2)

S('VHFCNT', 'erase', 0o1125, line=1889)  # B(1)PRM NO. OF VHF MARKS (P20 (R22)).
S('TRKMKCNT', 'erase', 0o1126, line=1890)  # B(1)PRM NO. OF VHF MARKS (P20 (R22)).

S('MARKCTR', 'equals', 0o1126, line=1892)  # B(1) MARK COUNTER USED BY R32

# MISCELLANEOUS UNSWITCHED.             (16D)

S('IRETURN1', 'erase', 0o1127, line=1896)  # B(1) RET ADDR USED BY MIDTOAV1 AND 2
# CALLED BY P40,P41,P42, P61,P62
S('RATEINDX', 'erase', 0o1130, line=1898)  #  (1) USED BY KALCMANU
S('OPTION1', 'erase', 0o1131, line=1899)  # B(1) NOUN 06 USES THIS.
S('OPTION2', 'erase', 0o1132, line=1900)  # B(1) NOUN 06 USES THIS.
S('LONGCADR', 'erase', 0o1133, line=1901)  # B(2) LONGCALL REGISTER.
S('LONGBASE', 'erase', 0o1135, line=1902)  # B(2) LONGCALL REGISTER.
S('LONGTIME', 'erase', 0o1137, line=1903)  # B(2) LONGCALL REGISTER.
S('DELAYLOC', 'erase', 0o1141, line=1904)
S('NVWORD1', 'erase', 0o1145, line=1905)  # B(1)
S('TEMPR60', 'erase', 0o1146, line=1906)  # B(1)
S('PRIOTIME', 'erase', 0o1147, line=1907)  # B(1)
S('P30/RET', 'equals', 0o1127, line=1908)

# MISC. INCLUDING RESTART COUNTER, GIMBAL ANGLE SAVE AND
# STANDBY VERB ERASABLES.  REDOCTR BEFORE THETAD (DWNLNK)       (16D)

S('TIME2SAV', 'erase', 0o1150, line=1913)  # B(2)TMP
S('SCALSAVE', 'erase', 0o1152, line=1914)  # B(2)TMP
S('REDOCTR', 'erase', 0o1154, line=1915)  # B(1)PRM CONTAINS NUMBER OF RESTARTS
S('THETAD', 'erase', 0o1155, line=1916)  # B(3)PRM DESIRED GIM ANGLES FOR MANEUVER
S('CPHI', 'equals', 0o1155, line=1917)  #       (OUTER)
S('CTHETA', 'equals', 0o1156, line=1918)  #       (INNER)
S('CPSI', 'equals', 0o1157, line=1919)  #       (MIDDLE)
# Page 79
# ENTRY VARIABLES SHARED FOR TM.
S('RDOTREF', 'equals', 0o1155, line=1922)  # I(2)  P65
S('VREF', 'equals', 0o1157, line=1923)  # I(2)  P65     HI-ORDER WORD ONLY DNLNK'D
S('DESOPTT', 'erase', 0o1160, line=1924)  # B(1)DSP NOUN 92 FOR P20,22,52, R52.
S('DESOPTS', 'erase', 0o1161, line=1925)  # B(1)DSP NOUN 92 FOR P20,22,52, R52.

S('DELV', 'erase', 0o1162, line=1927)  # I(6)
S('DELVX', 'equals', 0o1162, line=1928)
S('DELVY', 'equals', 0o1164, line=1929)
S('DELVZ', 'equals', 0o1166, line=1930)

# P20, CONICS   (SHARING WITH TIME 2 SAV AND SCAL SAV ONLY)     (3D)
S('POINTEX', 'equals', 0o1150, line=1933)  # I(1) POINT AXS EXIT
S('VHFTIME', 'equals', 0o1151, line=1934)  # I(2) DOWNLINK OF VHF RANGE TIME +1M

# PERM STATE VECTORS FOR BOOST AND DOWNLINK -- WHOLE MISSION -- (14D)

S('RN', 'erase', 0o1170, line=1938)  # B(6)PRM
S('VN', 'erase', 0o1176, line=1939)  # B(6)PRM
S('PIPTIME', 'erase', 0o1204, line=1940)  # B(2)PRM (MUST BE FOLLOWED BY GDT/2)

# SERVICER STORAGE.                             (45D)

# (SERVICER STORAGE AND P11 STORAGE IN UNSWITCHED SHOULD NOT
# OVERLAY EACH OTHER AND THE TOTAL ERASABLE REQUIRED SHOULD NOT
# EXCEED THE ERASABLE STORAGE REQUIRED BY RENDEZVOUS GUIDANCE.)

S('GDT/2', 'equals', 0o1206, line=1948)  # B(6)TMP       ** MUST FOLLOW PIPTIME **
S('GOBL/2', 'equals', 0o1214, line=1949)  # B(6)TMP
S('AVEGEXIT', 'equals', 0o1222, line=1950)  # B(2)TMP
S('AVGEXIT', 'equals', 0o1222, line=1951)
S('TEMX', 'equals', 0o1224, line=1952)  # B(1)TMP
S('TEMY', 'equals', 0o1225, line=1953)  # B(1)TMP
S('TEMZ', 'equals', 0o1226, line=1954)  # B(1)TMP
S('PIPCTR', 'equals', 0o1227, line=1955)  # B(1)TMP
S('PIPAGE', 'equals', 0o1230, line=1956)  # B(1)TMP
S('RN1', 'equals', 0o1231, line=1957)  # B(6)TMP
S('VN1', 'equals', 0o1237, line=1958)  # B(6)TMP
S('PIPTIME1', 'equals', 0o1245, line=1959)  # B(2)TMP
S('GDT1/2', 'equals', 0o1247, line=1960)  # B(6)TMP
S('GOBL1/2', 'equals', 0o1255, line=1961)  # B(6)TMP

# Page 80
# ENTRY STORAGE                         (1D)
S('ENTRYVN', 'equals', 0o1263, line=1965)  # B(1)TMP VN CODE FOR ENTRY DISPLAYS P60'S.

# P11 STORAGE.                          (9D)
S('PADLONG', 'equals', 0o1263, line=1968)  # (2)PL LONGITUDE OF LAUNCH PAD.
S('LIFTTEMP', 'equals', 0o1265, line=1969)  # (2)TMP
S('TEPHEM1', 'equals', 0o1267, line=1970)  # (3)TMP
S('PGNCSALT', 'equals', 0o1272, line=1971)  # (2)PL ALTITUDE

# RENDEZVOUS NAVIGATION STORAGE.  (SEE COMMENT IN SERVICER STORAGE)     (58D)
S('CSMPOS', 'erase', 0o1206, line=1974)  # I(6)TMP
S('LEMPOS', 'equals', 0o1214, line=1975)  # I(6)TMP
S('RCL', 'equals', 0o1222, line=1976)  # I(2)TMP
S('MARKTIME', 'equals', 0o1224, line=1977)  # B(2)TMP
S('VTEMP', 'equals', 0o1226, line=1978)  # B(6)TMP
S('UM', 'equals', 0o1234, line=1979)  # I(6)TMP
S('MARKDATA', 'equals', 0o1242, line=1980)  # B(2)TMP
S('USTAR', 'equals', 0o1244, line=1981)  # I(6)TMP
S('WIXA', 'equals', 0o1252, line=1982)  # B(1)TMP
S('WIXB', 'equals', 0o1253, line=1983)  # B(1)TMP
S('ZIXA', 'equals', 0o1254, line=1984)  # B(1)TMP
S('ZIXB', 'equals', 0o1255, line=1985)  # B(1)TMP
S('DELTAX', 'equals', 0o1256, line=1986)  # I(18)TMP

S('VHFRANGE', 'equals', 0o1256, line=1988)  # (2)
S('UCL', 'equals', 0o1272, line=1989)  # (6)   LM-CSM LINE OF SIGHT 1/2 UNIT V

# **** CONICSEX (MEAS INC) ****
S('TRIPA', 'equals', 0o1256, line=1992)
S('TEMPVAR', 'equals', 0o1261, line=1993)

S('TEMPOR1', 'erase', 0o1300, line=1995)  # B(2)TMP

# T4RUPT ERASABLE                       (6D)

S('DSRUPTSW', 'erase', 0o1302, line=1999)
S('OPTIND', 'erase', 0o1303, line=2000)
S('LGYRO', 'erase', 0o1304, line=2001)
S('COMMANDO', 'erase', 0o1305, line=2002)

# Page 81
S('ZONE', 'erase', 0o1307, line=2005)  # B(1)PRM USED IN SHAFT STOP MONITOR
S('LASTYCMD', 'equals', 0o35, line=2006)  # DUMMY TO MAKE RR BENCH TEST ASSEMBLE
S('LASTXCMD', 'equals', 0o35, line=2007)  # DUMMY TO MAKE RR BENCH TEST ASSEMBLE

# UNSWITCHED DAP ERASABLE.              (4D)
S('T6LOC', 'erase', 0o1310, line=2010)
S('T6ADR', 'erase', 0o1311, line=2011)
S('T5LOC', 'erase', 0o1312, line=2012)

# MODE SWITCHING ERASABLE               (14D)
S('SWSAMPLE', 'erase', 0o1314, line=2015)  # B(1)PRM
S('DESOPMOD', 'erase', 0o1315, line=2016)  # B(1)PRM
S('WTOPTION', 'erase', 0o1316, line=2017)  # B(1)PRM
S('ZOPTCNT', 'erase', 0o1317, line=2018)  # B(1)PRM
S('IMODES30', 'erase', 0o1320, line=2019)  # B(1)PRM
S('IMODES33', 'erase', 0o1321, line=2020)  # B(1)PRM
S('MODECADR', 'erase', 0o1322, line=2021)  # B(3)TMP
S('IMUCADR', 'equals', 0o1322, line=2022)
S('OPTCADR', 'equals', 0o1323, line=2023)
S('RADCADR', 'equals', 0o1324, line=2024)
S('ATTCADR', 'erase', 0o1325, line=2025)  # B(3)PRM
S('ATTPRIO', 'equals', 0o1327, line=2026)
S('MARKSTAT', 'erase', 0o1330, line=2027)  # B(1)PRM
S('OPTMODES', 'erase', 0o1331, line=2028)  # B(1)PRM

# RCSDAP ERASABLE                       (1D)
S('HOLDFLAG', 'erase', 0o1332, line=2031)  # B(1)PRM

# CRS61.1 STORAGE.  -- USED IN R63 (VERB 89) -- (5D)
S('CPHIX', 'erase', 0o1333, line=2034)  # B(3)DSP NOUN 95 CALCULATED BY CRS61.1

S('TEVENT', 'erase', 0o1336, line=2036)  # B(2) TIME OF EVENT FOR DOWNLIST
S('TLIFTOFF', 'equals', 0o1336, line=2037)

# Page 82
# P34-P35 STORAGE                       (1D)
S('NORMEX', 'erase', 0o1340, line=2041)

# SELF-CHECK ASSIGNMENTS                (17D)

S('SELFERAS', 'erase', 0o1357, line=2045)  # *** MUST NOT BE MOVED *** #
S('SFAIL', 'equals', 0o1357, line=2046)  # B(1)
S('ERESTORE', 'equals', 0o1360, line=2047)  # B(1)
S('SELFRET', 'equals', 0o1361, line=2048)  # B(1) RETURN
S('SMODE', 'equals', 0o1362, line=2049)  # B(1)
S('ALMCADR', 'equals', 0o1363, line=2050)  # B(2) ALARM ABORD USER'S 2CADR
S('ERCOUNT', 'equals', 0o1365, line=2051)  # B(1)
S('SCOUNT', 'equals', 0o1366, line=2052)  # B(3)
S('SKEEP1', 'equals', 0o1371, line=2053)  # B(1)
S('SKEEP2', 'equals', 0o1372, line=2054)  # B(1)
S('SKEEP3', 'equals', 0o1373, line=2055)  # B(1)
S('SKEEP4', 'equals', 0o1374, line=2056)  # B(1)
S('SKEEP5', 'equals', 0o1375, line=2057)  # B(1)
S('SKEEP6', 'equals', 0o1376, line=2058)  # B(1)
S('SKEEP7', 'equals', 0o1377, line=2059)  # B(1)

# USED BY P30 ROUTINES TO WRITE ONLY NEVER READ IN COLOSSUS

S('DISPDEX', 'equals', 0o0, line=2063)

# ERASABLE FOR SXTMARK CDU CHECK DELAY.  -- PAD LOADED --       (1D)

S('CDUCHKWD', 'erase', 0o1341, line=2067)  # B(1)PL

# R57 STORAGE. -- MUST BE UNSHARED EXCEPT IN BOOST OR ENTRY --  (1D)

S('TRUNBIAS', 'erase', 0o1342, line=2071)  # B(1)PRM RESULT OF R57 CALIBR OF TRUNION

# KEPLER STORAGE                                (6D)

S('XMODULO', 'erase', 0o1343, line=2075)  # I(2) GREATER 2PI KEPLER
S('TMODULO', 'erase', 0o1345, line=2076)  # I(2) GREATER 2 KEPLER
S('EPSILONT', 'erase', 0o1347, line=2077)  # I(2)TMP

# Page 83
# P37   ** RETURN TO EARTH (PAD LOAD ****       (2D)

S('RTED1', 'erase', 0o1351, line=2082)  # I(2)PL VGAMMA POLY COEF               B-3

# P40   *** STEERING ROUTINE *** PAD LOAD       (1D)

S('DVTHRESH', 'erase', 0o1353, line=2086)  # I(1)PL DELTA VTHRESHOLD FOR LOW THRUST
# ROUTINE                        B-2

# P23   *** PAD LOAD ****               (2D)

S('HORIZALT', 'erase', 0o1354, line=2091)  # I(2)PL HORIZON ALTITUDE            M B-29

# P20   ALTERNATE LOS VARIANCE  PAD LOAD ****   (1D)
# -16
S('ALTVAR', 'erase', 0o1356, line=2095)  # I(2)PL MILLARD, SQUARED SCALED 2
S('END-UE', 'equals', 0o1377, line=2096)  # LAST USED UNSWITCHED ERASABLE

# Page 84
# EBANK-3 ASSIGNMENTS

#   SETLOC 1400

# WAITLIST TASK LISTS.                  (26D)

S('LST1', 'erase', 0o1400, line=2105)  # B(8D)PRM DELTA T'S.
S('LST2', 'erase', 0o1410, line=2106)  # B(18D)PRM TASK 2CADR ADDRESSES.

# RESTART STORAGE.                      (2D)

S('RSBBQ', 'erase', 0o1432, line=2110)  # B(2)PRM SAVE BB AND Q FOR RESTARTS

# MORE LONGCALL STORAGE.  (MUST BE IN LST1'S BANK.      (2D)

S('LONGEXIT', 'erase', 0o1434, line=2114)  # B(2)TMP MAY BE SELDOM OVERLAYED

# PHASE-CHANGE LISTS PART II.           (12D)

S('PHSNAME1', 'erase', 0o1436, line=2119)  # B(1)PRM
S('PHSBB1', 'erase', 0o1437, line=2120)  # B(1)PRM
S('PHSNAME2', 'erase', 0o1440, line=2121)  # B(1)PRM
S('PHSBB2', 'erase', 0o1441, line=2122)  # B(1)PRM
S('PHSNAME3', 'erase', 0o1442, line=2123)  # B(1)PRM
S('PHSBB3', 'erase', 0o1443, line=2124)  # B(1)PRM
S('PHSNAME4', 'erase', 0o1444, line=2125)  # B(1)PRM
S('PHSBB4', 'erase', 0o1445, line=2126)  # B(1)PRM
S('PHSNAME5', 'erase', 0o1446, line=2127)  # B(1)PRM
S('PHSBB5', 'erase', 0o1447, line=2128)  # B(1)PRM
S('PHSNAME6', 'erase', 0o1450, line=2129)  # B(1)PRM
S('PHSBB6', 'erase', 0o1451, line=2130)  # B(1)PRM

# IMU COMPENSATION PARAMETERS           (22D)

S('PBIASX', 'erase', 0o1452, line=2134)  # B(1)  PIPA BIAS, PIPA SCALE FACTOR TERMS
S('PIPABIAS', 'equals', 0o1452, line=2135)  #       INTERMIXED.
S('PIPASCFX', 'erase', 0o1453, line=2136)
S('PIPASCF', 'equals', 0o1453, line=2137)
S('PBIASY', 'erase', 0o1454, line=2138)
S('PIPASCFY', 'erase', 0o1455, line=2139)
S('PBIASZ', 'erase', 0o1456, line=2140)
S('PIPASCFZ', 'erase', 0o1457, line=2141)

S('NBDX', 'erase', 0o1460, line=2143)  # GYRO BIAS DRIFT
S('GBIASX', 'equals', 0o1460, line=2144)
S('NBDY', 'erase', 0o1461, line=2145)
# Page 85
S('NBDZ', 'erase', 0o1462, line=2147)

S('ADIAX', 'erase', 0o1463, line=2149)  # ACCELERATION SENSITIVE DRIFT ALONG THE
S('ADIAY', 'erase', 0o1464, line=2150)  # INPUT AXIS
S('ADIAZ', 'erase', 0o1465, line=2151)

S('ADSRAX', 'erase', 0o1466, line=2153)  # ACCELERATION SENSITIVE DRIFT ALONG THE
S('ADSRAY', 'erase', 0o1467, line=2154)  # SPIN REFERENCE AXIS
S('ADSRAZ', 'erase', 0o1470, line=2155)

S('GCOMP', 'erase', 0o1471, line=2157)  # CONTAINS COMPENSATING TORQUES

S('GCOMPSW', 'erase', 0o1477, line=2159)
S('COMMAND', 'equals', 0o1471, line=2160)
S('CDUIND', 'equals', 0o1474, line=2161)

# STATE VECTORS FOR ORBIT INTEGRATION.  (44D)

# (DIFEQCNT THUR XKEP MUST BE IN THE SAME
# EBANK AS RRECTCSM, RRECTLEM ETC
# BECAUSE THE COPY CYCLES (ATOPCSM,
# PTOACSM ETC) ARE EXECUTED IN BASIC.
# ALL OTHER REFERENCES TO THIS GROUP
# ARE BY INTERPRETIVE INSTRUCTIONS.)
#

S('DIFEQCNT', 'erase', 0o1500, line=2173)  # B(1)TMP
# (UPSVFLAG...XKEP MUST BE KEPT IN ORDER).

S('UPSVFLAG', 'equals', 0o1501, line=2176)  # B(1)PRM UPDATE FLAG
S('RRECT', 'equals', 0o1502, line=2177)  # B(6)TMP POS AT RECT           KM*2(-14)
S('VRECT', 'equals', 0o1510, line=2178)  # B(6)TMP VEL AT RECT           KM(-1/2)*2(6)
S('TET', 'equals', 0o1516, line=2179)  # B(2)TMP TIME OF STATE VECT    CSPCS*2(-28)
S('TDELTAV', 'equals', 0o1520, line=2180)  # B(6)TMP POSITION DEVIATION    KM*2(14)
S('TNUV', 'equals', 0o1526, line=2181)  # B(6)TMP VEL DEVIATION         KM(-1/2)*2(14)
S('RCV', 'equals', 0o1534, line=2182)  # B(6)TMP CONIC POSITION        KM*2(-14)
S('VCV', 'equals', 0o1542, line=2183)  # B(6)TMP CONIC VELOCITY        KM(-1/2)*2(6)
S('TC', 'equals', 0o1550, line=2184)  # B(2)TMP TIME SINCE RECTIFICATION
S('XKEP', 'equals', 0o1552, line=2185)  # B(2)TMP ROOT OF KEPLER EQ     KM(1/2)*2(-10)

# **** TEMP -- IN VAC AREA ****
S('RRECT1', 'equals', 0o22, line=2188)
S('VRECT1', 'equals', 0o30, line=2189)
S('TET1', 'equals', 0o36, line=2190)

# PERMANENT STATE VECTORS AND TIMES.    (101D)

# (DO NOT OVERLAY WITH ANYTHING AFTER BOOST)

# Page 86
# (RRECTCSM...XKEPCSM MUST BE KEPT IN THIS ORDER)

S('RRECTCSM', 'erase', 0o1554, line=2199)  # B(6)PRM CSM VARIABLES
S('RRECTHIS', 'equals', 0o1554, line=2200)
S('VRECTCSM', 'erase', 0o1562, line=2201)  # B(6)PRM
S('TETCSM', 'erase', 0o1570, line=2202)  # B(2)PRM
S('TETTHIS', 'equals', 0o1570, line=2203)
S('DELTACSM', 'erase', 0o1572, line=2204)  # B(6)PRM
S('NUVCSM', 'erase', 0o1600, line=2205)  # B(6)PRM
S('RCVCSM', 'erase', 0o1606, line=2206)  # B(6)PRM
S('VCVCSM', 'erase', 0o1614, line=2207)  # B(6)PRM
S('TCCSM', 'erase', 0o1622, line=2208)  # B(2)PRM
S('XKEPCSM', 'erase', 0o1624, line=2209)  # B(2)PRM

# (RRECTLEM...XKEPLEM MUST BE KEPT IN THIS ORDER)

S('RRECTLEM', 'erase', 0o1626, line=2213)  # B(6)PRM LEM VARIABLES
S('RRECTOTH', 'equals', 0o1626, line=2214)
S('VRECTLEM', 'erase', 0o1634, line=2215)  # B(6)PRM
S('TETLEM', 'erase', 0o1642, line=2216)  # B(2)PRM
S('TETOTHER', 'equals', 0o1642, line=2217)
S('DELTALEM', 'erase', 0o1644, line=2218)  # B(6)PRM
S('NUVLEM', 'erase', 0o1652, line=2219)  # B(6)PRM
S('RCVLEM', 'erase', 0o1660, line=2220)  # B(6)PRM
S('VCVLEM', 'erase', 0o1666, line=2221)  # B(6)PRM
S('TCLEM', 'erase', 0o1674, line=2222)  # B(2)PRM
S('XKEPLEM', 'erase', 0o1676, line=2223)  # B(2)PRM

S('X789', 'erase', 0o1700, line=2225)
S('TEPHEM', 'erase', 0o1706, line=2226)
S('AZO', 'erase', 0o1711, line=2227)
S('UNITW', 'erase', 0o1713, line=2228)
S('-AYO', 'equals', 0o1713, line=2229)  # (2)
S('AXO', 'equals', 0o1715, line=2230)  # (2)

# STATE VECTORS FOR DOWNLINK            (12D)

S('R-OTHER', 'erase', 0o1721, line=2234)  # B(6)PRM POS VECT (OTHER VECH) FOR DNLINK
S('V-OTHER', 'erase', 0o1727, line=2235)  # B(6)PRM VEL VECT (OTHER VECH) FOR DNLINK

S('T-OTHER', 'equals', 0o1642, line=2237)  #             TIME (OTHER VECH) FOR DNLINK

# REFSMMAT.                             (18D)

S('REFSMMAT', 'erase', 0o1735, line=2241)  # I(18D)PRM

# Page 87
# AVERAGEG INTEGRATOR STORAGE.          (8D)
S('UNITR', 'erase', 0o1757, line=2245)
S('RMAG', 'erase', 0o1765, line=2246)

# P40 PAD LOADS                         (6D)
S('EK1VAL', 'erase', 0o1767, line=2249)  # I(2)PL 1-SEC SPS IMPULSE NEWTSEC/100/B23
S('EK2VAL', 'erase', 0o1771, line=2250)  # I(2)PL  B+23 NEWTON-SEC/E+2
S('EK3VAL', 'erase', 0o1773, line=2251)  # I(1)PL  B+09 NEWTONS/E+4
S('FANG', 'erase', 0o1774, line=2252)  # I(1)PL SPS THRUST USED BY IMPULSIVE BURN

# **********LUNAR MODULE CHANGE  ***********
S('E3J22R2M', 'equals', 0o1776, line=2255)
S('E32C31RM', 'equals', 0o1777, line=2256)

# **** CONICSEX (PLANETARY INERT. ORIEN.) ****
S('TIMSUBO', 'equals', 0o1706, line=2259)  # CSEC B-14 (TRIPLE PREC)
S('END-E3', 'equals', 0o1777, line=2260)  # NEXT UNUSED E3 ADDRESS

# Page 88
# EBANK-4 ASSIGNMENTS

#   SETLOC 2000

# P20 STORAGE.  -- PAD LOADED --        (4D)

S('WRENDPOS', 'erase', 0o2000, line=2269)  # B(1)PL        M B-14
S('WRENDVEL', 'erase', 0o2001, line=2270)  # B(1)PL        M/CSECB0
S('RMAX', 'erase', 0o2002, line=2271)  # B(1)PL        METERS*2(-19)
S('VMAX', 'erase', 0o2003, line=2272)  # B(1)PL        M/CSEC*2(-7)

# P22 STORAGE.  -- PAD LOADED --        (5D)
S('WORBPOS', 'erase', 0o2004, line=2275)  # B(1)PL        M B-14
S('WORBVEL', 'erase', 0o2005, line=2276)  # B(1)PL        M/CSECB0
S('S22WSUBL', 'erase', 0o2006, line=2277)  # B(1)PL        M B-14
S('RPVAR', 'erase', 0o2007, line=2278)  # B(2)PL

# CONISEX STORAGE.  -- PAD LOADED --    (6D)

S('504LM', 'erase', 0o2011, line=2282)  # I(6) MOON LIBRATION VECTOR

# ENTRY STORAGE     -- PAD LOADED --    (2D)
S('EMSALT', 'erase', 0o2017, line=2285)  # I(2)PL

# P35 CONSTANTS.    -- PAD LOADED --    (4D)
S('ATIGINC', 'erase', 0o2021, line=2288)  # B(2)PL
S('PTIGINC', 'erase', 0o2023, line=2289)  # B(2)PL

# LUNAR LANDING SIGHT DATA.  -- PAD LOADED --   (6D)
# (USED BY INTEGRATION INITIALIZATION, LAT-LONG SUBROUTINES, P30'S)

S('RLS', 'erase', 0o2025, line=2294)  # I(6) LANDING SIGHT VECTOR

# CONISEX (LUNAR AND SOLAR EPHEM) STORAGE.  -- PAD LOADED --    (77D)
S('TIMEMO', 'erase', 0o2033, line=2297)
S('VECOEM', 'equals', 0o2036, line=2298)
S('RESO', 'equals', 0o2132, line=2299)
# Page 89
S('VESO', 'equals', 0o2140, line=2301)
S('OMEGAES', 'equals', 0o2146, line=2302)

# INTEGRATION STORAGE.                  (95D)

S('PBODY', 'erase', 0o2150, line=2306)  # I(1)
S('ALPHAV', 'equals', 0o2151, line=2307)  # I(6)TMP
S('BETAV', 'equals', 0o2157, line=2308)  # I(6)TMP
S('PHIV', 'equals', 0o2165, line=2309)  # I(6)TMP
S('PSIV', 'equals', 0o2173, line=2310)  # I(6)TMP
S('FV', 'equals', 0o2201, line=2311)  # I(6)TMP
S('BETAM', 'equals', 0o2207, line=2312)  # I(6)TMP
S('H', 'equals', 0o2211, line=2313)  # I(2)TMP
S('GMODE', 'equals', 0o2213, line=2314)  # I(1)TMP
S('IRETURN', 'equals', 0o2214, line=2315)  # I(1)TMP
S('NORMGAM', 'equals', 0o2215, line=2316)  # I(1)TMP
S('VECTAB', 'equals', 0o2216, line=2317)  # I(36)TMP
S('RPQV', 'equals', 0o2262, line=2318)  #  (6)TMP VECTOR PRIMARY TO SECONDARY BODY
S('ORIGEX', 'equals', 0o2270, line=2319)  # B(1)TMP QSAVE FOR COORD. SWITCH ROUTINE
S('KEPRTN', 'equals', 0o2270, line=2320)  #         QSAVE FOR KEPLER
S('RQVV', 'equals', 0o2271, line=2321)  #  (6)    SEC. BODY TO VEH.VETOR (USED P23)
S('RPSV', 'equals', 0o2277, line=2322)  #  (6)TMP SUN TO PRIMARY BODY VECTOR
S('XKEPNEW', 'equals', 0o2305, line=2323)  #  (2)TMP ROOT OF KEPLER'S EQU FOR TIME TAU

# THESE PROBABLY CAN SHARE INTEGRATION VARIABLES        (9D)

S('VACX', 'equals', 0o2224, line=2327)  # I(2)TMP
S('VACY', 'equals', 0o2226, line=2328)  # I(2)TMP
S('VACZ', 'equals', 0o2230, line=2329)  # I(2)TMP

S('ERADM', 'equals', 0o2240, line=2331)  # I(2)TMP
S('INCORPEX', 'equals', 0o2242, line=2332)  # I(1)TMP

# R31 (V83) STORAGE. -- SHARES WITH INTEGRATION STORAGE --      (24D)

S('BASEOTP', 'equals', 0o2224, line=2336)  # I(6) BASE POS VECTOR OTHER VEH
S('BASEOTV', 'equals', 0o2240, line=2337)  # I(6) BASE VEL VECTOR OTHER VEH
S('BASETHP', 'equals', 0o2254, line=2338)  # I(6) BASE POS VECTOR THIS VEH
S('BASETHV', 'equals', 0o2262, line=2339)  # I(6) BASE VEL VECTOR THIS VEH

# CONIC INTEGRATION STORAGE. -- MAY NOT SHARE WITH SERVICER --  (6D)
S('ALPHAM', 'equals', 0o2307, line=2342)  # I(2)TMP
S('TAU.', 'equals', 0o2311, line=2343)  # I(2)TMP
S('DT/2', 'equals', 0o2313, line=2344)  # I(2)TMP

# Page 90

# P21, R61 STORAGE.                     (2D)
S('P21TIME', 'equals', 0o2315, line=2349)  # B(2)TMP

# INTEGRATION STORAGE                   (1D)
S('EGRESS', 'equals', 0o2317, line=2352)  # I(1)TMP SAVES RETURNS.

# VERB 83 STORAGE.                      (20D)

S('RANGE', 'equals', 0o2320, line=2356)  # I(2)DSP NOUN 54 DISTANCE TO OPTICAL SUBJ
S('RRATE', 'equals', 0o2322, line=2357)  # I(2)DSP NOUN 54 RATE OF APPROACH
S('RTHETA', 'equals', 0o2324, line=2358)  # I(2)DSP NOUN 54.
S('RONE', 'equals', 0o2326, line=2359)  # I(6)TMP VECTOR STORAGE.  (SCRATCH)
S('VONE', 'equals', 0o2334, line=2360)  # I(6)TMP VECTOR STORAGE.  (SCRATCH)
S('BASETIME', 'equals', 0o2342, line=2361)  # I(2)    BASE TIME ASSOC WITH BASE VECS

# S-BAND ANTENNA GIMBAL ANGLES.  DISPLAYED BY R05 (V64).        (4D)
# (OPERATES DURING P00 ONLY)
S('RHOSB', 'equals', 0o2320, line=2365)  # B(2)DSP NOUN 51. PITCH ANGLE
S('GAMMASB', 'equals', 0o2322, line=2366)  # B(2)DSP NOUN 51. YAWANGLE

# R36 SCRATCHPAD STORAGE                (13D)
S('RPASS36', 'equals', 0o2326, line=2369)  # I(6) S-S
S('UNP36', 'equals', 0o2334, line=2370)  # I(6) S-S
S('OPTIONY', 'equals', 0o2342, line=2371)  # I(1)TMP VEHICLE CODE

# EXTENDED VERB 82 STORAGE.             (6D)

S('HPERMIN', 'equals', 0o2320, line=2375)  # I(2) SET TO 300KFT OR 35KFT FOR SR30.1
S('RPADTEM', 'equals', 0o2322, line=2376)  # I(2) PAD OR LANDING RADIUS FOR SR30.1
S('TSTART82', 'equals', 0o2324, line=2377)  # I(2) TEMP TIME STORAGE VOR V82.

# MORE VERB 82 NOT SHARING WITH VERB 83 (9D)
S('V82FLAGS', 'equals', 0o2342, line=2380)  #  (1) FOR V 82 BITS
S('TFF', 'equals', 0o2343, line=2381)  # I(2)DSP NOUN 50,44
S('-TPER', 'equals', 0o2345, line=2382)  # I(2)DSP NOUN 32
S('THETA(1)', 'equals', 0o2347, line=2383)  # I(2)TMP SET AT END OF V82
# Page 91
S('RSP-RREC', 'equals', 0o2355, line=2385)  # DSP NOUN 50 FOR V82 DURING P00 AND P11

# REENTRY CONICS                        (6D)
S('URONE', 'equals', 0o2342, line=2388)  # I(6) SAVE ACTUAL FOR CALCULATIONS

# V82 DISPLAY                           (4D)
S('HAPOX', 'equals', 0o2351, line=2391)  # I(2)DSP NOUN 44
S('HPERX', 'equals', 0o2353, line=2392)  # I(2)DSP NOUN 44

# P22 DISPLAY REGISTERS                 (06D)
S('AOPTIME', 'equals', 0o2355, line=2395)  # I(2)TMP FOR SR52.1.ADVTRACK
S('LANDLONG', 'equals', 0o2357, line=2396)  # I(2)DSP NOUN 89 FOR P22
S('LANDALT', 'equals', 0o2361, line=2397)  # I(2)DSP NOUN 89 FOR P22

# S34/35.5,P34-P35 STORAGE.             (6D)
S('KT', 'equals', 0o2363, line=2400)  # B(2)
S('VERBNOUN', 'equals', 0o2365, line=2401)  # B(1)TMP
S('QSAVED', 'equals', 0o2366, line=2402)  # B(1)TMP HOLDS RETURN
S('RTRN', 'equals', 0o2367, line=2403)  # B(1) RETURN
S('SUBEXIT', 'equals', 0o2370, line=2404)  # B(1)TMP
# RGEXIT CAN'T SHARE WITH HPER,HAPO
S('RGEXIT', 'equals', 0o2370, line=2406)  # I(1)TMP Q SAVE MODE 1 AND 2 TO RTRN MAIN

# P30 DISPLAY                           (4D)
S('HAPO', 'equals', 0o2363, line=2409)  # I(2)DSP NOUN 42, FOR P30.
S('HPER', 'equals', 0o2365, line=2410)  # I(2)DSP NOUN 42, FOR P30.

# SOME P34 STORAGE.     (OVERLAYS P35.1 STORAGE)        (2D)
S('NOMTPI', 'equals', 0o2363, line=2413)  # I(2)TMP NOMINAL TPI TIME FOR RECYCLE.

# THE FOLLOWING ARE ERASABLES USED BY THE SYSTEM TESTS.  205 USES TRANSM1.  G'S ARE NOT USED IN 205 NOR ARE THEY
# WHILE 504 USES TRANSM1 AND ALFDK.
# Page 92
# RSB 2009.  The definition of TRANSM1 was previously just "TRANSM1 EQUALS 2000",
# this messes up the label typing system in yaYUL.
#   SETLOC 2000
S('TRANSM1', 'equals', 0o2000, line=2421)  # (18) INITIALIZATION FOR IMU TESTS
S('ALFDK', 'equals', 0o2022, line=2422)  # (144) ERASABLE LOAD IN 504

# END OF PERF. TEST ERASABLE IN BANK 4

# *-*-* V82 *-*-*                       (6D)

S("VONE'", 'equals', 0o2371, line=2428)  # I(6)TMP NORMAL VELOCITY VONE/ SQ RT MU

# PAD LOAD INTEGRATION ERROR INCLUDED IN VARIANCE BY P20        (1D)

S('INTVAR', 'equals', 0o2377, line=2432)  # I(1)PL        SQUARE OF EXPECTED INTEGRATION
# POSITION EXTRAPOLATION ERROR.
# SCALED METERS(2) 2(15)
S('END-E4', 'equals', 0o2377, line=2435)  # LAST USED ERASABLE IN E4.

# Page 93
# EBANK-5 ASSIGNMENTS

#   SETLOC 2400

# *-*-*-*- OVERLAY 1 IN EBANK 5 -*-*-*-*

# W-MATRIX STORAGE.                     (162D)

# RSB 2009.  The following 3 lines have been replaced to be consistent with yaYUL's
# label-typing system.  They *were* "W EQUALS 2400", "9X9LOC1 EQUALS 2444",
# "9X9LOC2 EQUALS 2532".
S('W', 'equals', 0o2400, line=2449)  # B(162)
S('9X9LOC1', 'equals', 0o2444, line=2450)
S('9X9LOC2', 'equals', 0o2532, line=2451)

S('EMATRIX', 'equals', 0o2570, line=2453)  # B(42) USED TO CONVERT W TO 6X6
S('END-W', 'equals', 0o2642, line=2454)  # **NEXT AVAILABLE LOC AFTER W MATRIX**

# AUTO-OPTICS STORAGE -R52-

# DO NOT MOVE FROM E5,1554.  A DELICATE BALANCE EXISTS BETWEEN THIS AND P03
S('XNB1', 'equals', 0o2554, line=2459)  # B(6D)TMP
S('YNB1', 'equals', 0o2562, line=2460)  # B(6)TMP
S('ZNB1', 'equals', 0o2570, line=2461)  # B(6)TMP
S('SAVQR52', 'equals', 0o2576, line=2462)  # I(2)TMP
S('PLANVEC', 'equals', 0o2600, line=2463)  # B(6) S-S SIGHTING VECTOR IN REF. COOR.
S('TSIGHT', 'equals', 0o2606, line=2464)  # B(2) S-S TIME OF SIGHTING

# RENDEZVOUS -P34-35                    (26D)
S('DVLOS', 'equals', 0o2610, line=2467)  # I(6) S-S DELTA VELOCITY, LOS COORD-DISPLAY
S('DELTAR', 'equals', 0o2610, line=2468)  # I(2)
S('TINTSOI', 'equals', 0o2610, line=2469)  # I(2) INTERCEPT TIME FOR SOI MANEUVER
S('DELTTIME', 'equals', 0o2612, line=2470)  # I(2)
S('TARGTIME', 'equals', 0o2614, line=2471)  # I(2)
S('UNRM', 'equals', 0o2616, line=2472)  # I(6) S-S
S('ULOS', 'equals', 0o2624, line=2473)  # I(6) S-S UNIT LINE OF SIGHT VECTOR
S('ACTCENT', 'equals', 0o2632, line=2474)  # I(2) S-S CENTRAL ANGLE BETWEEN ACTIVE
# VEH AT TPI IGNITION TIME AND
# TARGET VECTOR.
S('DELVTPI', 'equals', 0o2634, line=2477)  # I(2) NOUN 58 FOR P34
S('DELVTPF', 'equals', 0o2636, line=2478)  # I(2) NOUN 58,59 FOR P34,35
S('POSTTPI', 'equals', 0o2640, line=2479)  # I(2) NOUN 58 FOR P34.
S('TDEC2', 'equals', 0o2634, line=2480)  #  (2)

# ALIGNMENT                             (12D)
# Page 94
S('STARSAV1', 'equals', 0o2610, line=2484)  # I(6)TMP RESTART STAR SAVE.
S('STARSAV2', 'equals', 0o2616, line=2485)  # I(6)TMP RESTART STAR SAVE.
S('US', 'equals', 0o2616, line=2486)  #         (CISLUNAR TAG FOR STARSAV2).

# TPI SEARCH                            (26D)
S('IT', 'equals', 0o2610, line=2489)  #  (6)
S('THETZERO', 'equals', 0o2616, line=2490)  #  (2)
S('TFI', 'equals', 0o2620, line=2491)  #  (2)
S('DELVEE', 'equals', 0o2622, line=2492)  #  (2)
S('HP', 'equals', 0o2624, line=2493)  #  (2)
S('TFO', 'equals', 0o2626, line=2494)  #  (2)
S('HPO', 'equals', 0o2630, line=2495)  #  (2)
S('DELVEO', 'equals', 0o2632, line=2496)  #  (2)
S('MAGVTPI', 'equals', 0o2634, line=2497)  # I(2)TMP MAG OF DELTAVTPI OR VMID
S('RELDELV', 'equals', 0o2636, line=2498)  # I(2)TMP MAG OF DELTAVTPF
S('T3TOT4', 'equals', 0o2640, line=2499)  # I(2)DSP NOUN 39 FOR P34,35.  TPI TO TINT
# (CANNOT SHARE WITH RETURN TO EARTH)
# Page 95
# ALIGNMENT/SYSTEST/CALCSMSC/CRS61.1 COMMON STORAGE     (36D)
# (CALCSMSC IS A SUBSET OF S41.1 AT LEAST)
# (CRS61.1 IS A SUBSET OF P20)

S('XSM', 'equals', 0o2671, line=2506)  # B(6)
S('YSM', 'equals', 0o2677, line=2507)  # B(6)TMP
S('ZSM', 'equals', 0o2705, line=2508)  # B(6)TMP

S('XDC', 'equals', 0o2713, line=2510)  # B(6)TMP
S('YDC', 'equals', 0o2721, line=2511)  # B(6)TMP
S('ZDC', 'equals', 0o2727, line=2512)  # B(6)TMP

S('XNB', 'equals', 0o2713, line=2514)
S('YNB', 'equals', 0o2721, line=2515)
S('ZNB', 'equals', 0o2727, line=2516)

# OVERLAYS WITHIN ALIGNMENT/SYSTEST/CALCSMSC COMMON STORAGE

S('-COSB', 'equals', 0o2673, line=2520)  # (2)TMP
S('SINB', 'equals', 0o2675, line=2521)  # (2)TMP

# ALIGNMENT/SYSTEST COMMON STORAGE      (18D)

S('STARAD', 'equals', 0o2735, line=2525)  # I(18D)TMP

# ALIGNMENT/SYSTEST/AUTO OPTICS COMMON STORAGE. (17D)

S('OGC', 'equals', 0o2757, line=2529)  # I(2)TMP
S('IGC', 'equals', 0o2761, line=2530)  # I(2)TMP
S('MGC', 'equals', 0o2763, line=2531)  # I(2)TMP
S('STAR', 'equals', 0o2765, line=2532)  # I(6)TMP
S('SAC', 'equals', 0o2773, line=2533)  # I(2)TMP
S('PAC', 'equals', 0o2775, line=2534)  # I(2)TMP
S('QMIN', 'equals', 0o2777, line=2535)  # B(1)TMP

# **** COLP50'S ****                    (1D)
S('CULTRIX', 'equals', 0o2735, line=2538)  # VEARTH, VSUN, VMOON

# OVERLAYS WITHIN ALIGNMENT/SYSTEST COMMON STORAGE      (24D)

S('VEARTH', 'equals', 0o2735, line=2542)  # (6)TMP
S('VSUN', 'equals', 0o2743, line=2543)  # (6)TMP
S('VMOON', 'equals', 0o2751, line=2544)  # (6)TMP
S('SAX', 'equals', 0o2757, line=2545)  # (6)TMP

# Page 96
# *-*-*-*- OVERLAY NUMBER 2 IN EBANK 5 -*-*-*-*

# CONICS ROUTINE STORAGE.                       (87D)

S('DELX', 'equals', 0o2642, line=2552)  # I(2)TMP
S('DELT', 'equals', 0o2644, line=2553)  # I(2)TMP
S('URRECT', 'equals', 0o2646, line=2554)  # I(6)TMP
S('RCNORM', 'equals', 0o2654, line=2555)  # I(2)TMP
S('XPREV', 'equals', 0o1552, line=2556)  # I(2)TMP
S('R1VEC', 'equals', 0o2656, line=2557)  # I(6)TMP
S('R2VEC', 'equals', 0o2664, line=2558)  # I(6)TMP
S('TDESIRED', 'equals', 0o2672, line=2559)  # I(2)TMP
S('GEOMSGN', 'equals', 0o2674, line=2560)  # I(1)TMP
S('UN', 'equals', 0o2675, line=2561)  # I(6)TMP
S('VTARGTAG', 'equals', 0o2703, line=2562)  # I(1)TMP
S('VTARGET', 'equals', 0o2704, line=2563)  # I(6)TMP
S('RTNLAMB', 'equals', 0o2712, line=2564)  # I(1)TMP
S('U2', 'equals', 0o2713, line=2565)  # I(6)TMP
S('MAGVEC2', 'equals', 0o2721, line=2566)  # I(2)TMP
S('UR1', 'equals', 0o2723, line=2567)  # I(6)TMP
S('SNTH', 'equals', 0o2731, line=2568)  # I(2)TMP
S('CSTH', 'equals', 0o2733, line=2569)  # I(2)TMP
S('1-CSTH', 'equals', 0o2735, line=2570)  # I(2)TMP
S('CSTH-RHO', 'equals', 0o2737, line=2571)  # I(2)TMP
S('P', 'equals', 0o2741, line=2572)  # I(2)TMP
S('R1A', 'equals', 0o2743, line=2573)  # I(2)TMP
S('RVEC', 'equals', 0o2656, line=2574)  # I(6)TMP
S('VVEC', 'equals', 0o2745, line=2575)  # I(6)TMP
S('RTNTT', 'equals', 0o2712, line=2576)  # I(1)TMP
S('ECC', 'equals', 0o2753, line=2577)  # I(2)TMP
S('RTNTR', 'equals', 0o2712, line=2578)  # I(1)TMP
S('RTNAPSE', 'equals', 0o2712, line=2579)  # I(1)TMP
S('R2', 'equals', 0o2721, line=2580)  # I(2)TMP
S('RTNPRM', 'equals', 0o2755, line=2581)  # I(1)TMP
S('SGNRDOT', 'equals', 0o2756, line=2582)  # I(1)TMP
S('RDESIRED', 'equals', 0o2757, line=2583)  # I(2)TMP
S('DELDEP', 'equals', 0o2761, line=2584)  # I(2)TMP
S('DEPREV', 'equals', 0o2763, line=2585)  # I(2)TMP
S('TERRLAMB', 'equals', 0o2761, line=2586)  # I(2)TMP
S('TPREV', 'equals', 0o2763, line=2587)  # I(2)TMP

# Page 97
# *-*-*-*- OVERLAY NUMBER 3 IN EBANK 5 -*-*-*-*

# MEASUREMENT INCORPORATION STORAGE.    (66D)
# (CALLED BY P20, P22, P23)

S('OMEGAM1', 'equals', 0o2642, line=2595)  # I(6)TMP
S('OMEGAM2', 'equals', 0o2650, line=2596)  # I(6)TMP
S('OMEGAM3', 'equals', 0o2656, line=2597)  # I(6)TMP
S('HOLDW', 'equals', 0o2664, line=2598)  # I(18)TMP
S('TDPOS', 'equals', 0o2706, line=2599)  # I(6)TMP
S('TDVEL', 'equals', 0o2714, line=2600)  # I(6)TMP

S('ZI', 'equals', 0o2722, line=2602)  # I(18)

# P22-P23 STORAGE.                      (8D)

S('22SUBSCL', 'equals', 0o2744, line=2606)  # DE OF ABCDE LANDMARK ID NO.
S('CXOFF', 'equals', 0o2745, line=2607)  # B OF ABCDE OFFSET INDICATOR
S('8KK', 'equals', 0o2746, line=2608)  # B(1)TMP INDEX OF PRESENT MARK
S('8NN', 'equals', 0o2747, line=2609)  # B(1)TMP
S('S22LOC', 'equals', 0o2750, line=2610)  # I(1)TMP MARK DATA LOC
S('LANDMARK', 'equals', 0o2751, line=2611)  # B(1)DSP NOUN 70 FOR P22,51, R52,53
S('HORIZON', 'equals', 0o2752, line=2612)  # B(1)DSP NOUN 70 FOR P22,51, R52,53
S('IDOFLMK', 'equals', 0o2753, line=2613)  # B(1)

# ******P23***                          (1D)
S('TRUNION', 'equals', 0o2754, line=2616)  # B(1)

# Page 98

# *-*-*-*- OVERLAY NUMBER 0 IN EBANK 5 -*-*-*-*

# SYSTEM TEST STORAGE.                          (174)

S('AZIMUTH', 'erase', 0o2400, line=2624)
S('LATITUDE', 'erase', 0o2402, line=2625)

S('TRUNA', 'equals', 0o1160, line=2627)
S('SHAFTA', 'equals', 0o1161, line=2628)

S('ERVECTOR', 'erase', 0o2404, line=2630)
S('LENGTHOT', 'erase', 0o2412, line=2631)
S('LOSVEC', 'erase', 0o2413, line=2632)

S('SXTOPTN', 'equals', 0o2413, line=2634)
S('NDXCTR', 'erase', 0o2421, line=2635)
S('PIPINDEX', 'erase', 0o2422, line=2636)
S('POSITON', 'erase', 0o2423, line=2637)
S('QPLAC', 'erase', 0o2424, line=2638)
S('QPLACE', 'erase', 0o2425, line=2639)
S('QPLACES', 'erase', 0o2426, line=2640)
S('RUN', 'erase', 0o2427, line=2641)
S('STOREPL', 'erase', 0o2430, line=2642)
S('SOUTHDR', 'erase', 0o2431, line=2643)
S('TARG1/2', 'equals', 0o2431, line=2644)
S('TAZEL1', 'erase', 0o2432, line=2645)
S('TEMPTIME', 'erase', 0o2440, line=2646)
S('TMARK', 'erase', 0o2442, line=2647)
S('GENPL', 'erase', 0o2444, line=2648)
S('CDUTIMEI', 'equals', 0o2444, line=2649)
S('CDUTIMEF', 'equals', 0o2446, line=2650)
S('IMU/OPT', 'equals', 0o2450, line=2651)
S('CDUREADF', 'equals', 0o2451, line=2652)
S('CDUREADI', 'equals', 0o2452, line=2653)
S('CDULIMIT', 'equals', 0o2453, line=2654)

S('TEMPADD', 'equals', 0o2450, line=2656)
S('TEMP', 'equals', 0o2451, line=2657)
S('NOBITS', 'equals', 0o2452, line=2658)
S('CHAN', 'equals', 0o2453, line=2659)

S('LOS1', 'equals', 0o2454, line=2661)
S('LOS2', 'equals', 0o2462, line=2662)

S('CALCDIR', 'equals', 0o2470, line=2664)
S('CDUFLAG', 'equals', 0o2471, line=2665)
S('GYTOBETQ', 'equals', 0o2472, line=2666)
S('OPTNREG', 'equals', 0o2473, line=2667)
S('SAVE', 'equals', 0o2474, line=2668)  # THREE CONSEC LOC
S('SFCONST1', 'equals', 0o2477, line=2669)
# Page 99
S('TIMER', 'equals', 0o2500, line=2671)

S('DATAPL', 'equals', 0o2502, line=2673)
S('RDSP', 'equals', 0o2444, line=2674)  # FIX LATER     POSSIBLY KEEP1
S('MASKREG', 'equals', 0o2544, line=2675)
S('CDUNDX', 'equals', 0o2546, line=2676)
S('RESULTCT', 'equals', 0o2547, line=2677)
S('COUNTPL', 'equals', 0o2552, line=2678)

S('CDUANG', 'equals', 0o2553, line=2680)
S('AINLA', 'equals', 0o2444, line=2681)  # OPTIMUM CALIB. AND ALIGNMENT
S('WANGO', 'equals', 0o2444, line=2682)
S('WANGI', 'equals', 0o2446, line=2683)
S('WANGT', 'equals', 0o2450, line=2684)
S('TORQNDX', 'equals', 0o2450, line=2685)
S('DRIFTT', 'equals', 0o2452, line=2686)
S('ALX1S', 'equals', 0o2454, line=2687)
S('CMPX1', 'equals', 0o2455, line=2688)
S('ALK', 'equals', 0o2456, line=2689)
S('VLAUNS', 'equals', 0o2472, line=2690)
S('THETAX', 'equals', 0o2460, line=2691)
S('WPLATO', 'equals', 0o2474, line=2692)
S('INTY', 'equals', 0o2500, line=2693)
S('THETAN', 'equals', 0o2466, line=2694)
S('ANGZ', 'equals', 0o2502, line=2695)
S('INTZ', 'equals', 0o2504, line=2696)
S('ANGY', 'equals', 0o2506, line=2697)
S('ANGX', 'equals', 0o2510, line=2698)
S('DRIFTO', 'equals', 0o2512, line=2699)
S('DRIFTI', 'equals', 0o2514, line=2700)
S('VLAUN', 'equals', 0o2520, line=2701)
S('FILDELV', 'equals', 0o2474, line=2702)
S('ACCWD', 'equals', 0o2522, line=2703)
S('INTVEC', 'equals', 0o2476, line=2704)
S('POSNV', 'equals', 0o2530, line=2705)
S('DPIPAY', 'equals', 0o2532, line=2706)
S('DPIPAZ', 'equals', 0o2536, line=2707)
S('ALTIM', 'equals', 0o2540, line=2708)
S('ALTIMS', 'equals', 0o2541, line=2709)
S('ALDK', 'equals', 0o2542, line=2710)
S('DELM', 'equals', 0o2560, line=2711)
S('WPLATI', 'equals', 0o2570, line=2712)
S('RESTARPT', 'equals', 0o2577, line=2713)
S('GEOSAVED', 'equals', 0o2631, line=2714)
S('PREMTRXC', 'equals', 0o2632, line=2715)
S('LAUNCHAZ', 'equals', 0o2633, line=2716)
S('NEWAZMTH', 'equals', 0o2635, line=2717)
S('OLDAZMTH', 'equals', 0o2637, line=2718)
# Page 100
S('TOLDAZMT', 'equals', 0o2641, line=2720)
S('GEOCOMPS', 'equals', 0o2643, line=2721)
S('1SECXT', 'equals', 0o2644, line=2722)
S('GTSXTLST', 'equals', 0o2645, line=2723)
S('ERECTIME', 'equals', 0o2646, line=2724)
S('ERCOMP', 'equals', 0o2647, line=2725)
S('ZERONDX', 'equals', 0o2655, line=2726)
S('GTSOPNDZ', 'equals', 0o2655, line=2727)

# THE FOLLOWING TAGS ARE USED BY THE 504 IMU CALIBRATION AND ALIGNMENT PROGRAM ONLY.

S('THETAX1', 'equals', 0o2460, line=2731)
S('THETAN1', 'equals', 0o2466, line=2732)
S('FILDELV1', 'equals', 0o2474, line=2733)
S('INTVEC1', 'equals', 0o2476, line=2734)
S('GEOSAVE1', 'equals', 0o2631, line=2735)
S('PREMTRX1', 'equals', 0o2632, line=2736)
S('LUNCHAZ1', 'equals', 0o2633, line=2737)
S('NEWAZ1', 'equals', 0o2635, line=2738)
S('OLDAZ1', 'equals', 0o2637, line=2739)
S('TOLDAZ1', 'equals', 0o2641, line=2740)
S('GEOCOMP1', 'equals', 0o2643, line=2741)
S('1SECXT1', 'equals', 0o2644, line=2742)
S('GTSWTLT1', 'equals', 0o2645, line=2743)
S('ERECTIM1', 'equals', 0o2646, line=2744)
S('ERCOMP1', 'equals', 0o2647, line=2745)  # I(6)
S('ZERONDX1', 'equals', 0o2655, line=2746)
S('PERFDLAY', 'equals', 0o2656, line=2747)  # B(2)..........

# END OF 504 + ALIGN ERASE.

# Page 101

# *-*-*-*-  OVERLAY 4 IN EBANK 5  -*-*-*-*
#
# P32 --- P33                           (26D)
S('UP1', 'equals', 0o2610, line=2756)  # I(6)
S('VPASS2', 'equals', 0o2616, line=2757)  # I(6)
S('RPASS2', 'equals', 0o2624, line=2758)  # I(6)
S('DIFFALT', 'equals', 0o2632, line=2759)  # I(2)
S('TCDH', 'equals', 0o2634, line=2760)  # I(2)
S('TCSI', 'equals', 0o2636, line=2761)  # I(2)
S('TTPIO', 'equals', 0o2640, line=2762)  # I(2)

# P32,P33 STORAGE OVERLAYING 9X9 W-MATRIX LOCATIONS     (26D)
S('DELVEET1', 'equals', 0o2444, line=2765)  # I(6) DELV FOR CSI
S('RACT2', 'equals', 0o2452, line=2766)  # I(6) POS. ACTIVE VEH. AT CDH TIME
S('VACT2', 'equals', 0o2532, line=2767)  # I(6) VEL. ACTIVE VEH. AT CDH TIME
S('RACT1', 'equals', 0o2540, line=2768)  # I(6) POS. ACTIVE VEH. AT CSI TIME
S('T1TOT2', 'equals', 0o2546, line=2769)  # I(2) TCDH - TCSI
S('END-E5', 'equals', 0o2777, line=2770)  # LAST USED E5 ADDRESS

# Page 102

# EBANK-6 ASSIGNMENTS.

#   SETLOC 3000
# P23   PAD LOADS ***                   (2D).
S('WMIDPOS', 'erase', 0o3000, line=2778)  # I(1)PL INITIAL VALUES FOR W-MATRIX IN
S('WMIDVEL', 'erase', 0o3001, line=2779)  # I(1)PL CISLUNAR (P23) NAVIGATION

# R22   PAD LOADS                       (5D).
S('RVAR', 'erase', 0o3002, line=2782)  # I(2)PL VHF RADAR
S('RVARMIN', 'erase', 0o3004, line=2783)  # I(3)PL VHF RADAR

# ***** PAD LOADED ENTRY DAP STEERING VARIABLES *****   (3D)
S('LADPAD', 'erase', 0o3007, line=2786)  # I(1)PL FOR ENTRY. HOLDS CM NOMINAL L/D
S('LODPAD', 'erase', 0o3010, line=2787)  # I(1)PL FOR ENTRY. HOLDS CM NOMINAL LOD
S('ALFAPAD', 'erase', 0o3011, line=2788)  # B(1)PL ALFA TRIM / 180

# ***** PAD LOADED TVC DAP VARIABLES ****************   (26D)
S('ETDECAY', 'erase', 0o3012, line=2791)  # I(1)PL
S('ESTROKER', 'erase', 0o3013, line=2792)  # B(1)PL
S('EKPRIME', 'erase', 0o3014, line=2793)  # B(2)PL
S('EKTLX/I', 'erase', 0o3016, line=2794)  # B(3)PL
S('EREPFRAC', 'erase', 0o3021, line=2795)  # B(2)PL
S('PACTOFF', 'erase', 0o3023, line=2796)  # B(1)PL, DSP N48 R01 = PTRIM, R02 = YTRIM
S('YACTOFF', 'erase', 0o3024, line=2797)  # B(1)PL, CONSECUTIVE WITH PACTOFF
S('HBN10', 'erase', 0o3025, line=2798)  # B(1)
S('HBN11/2', 'erase', 0o3026, line=2799)  # B(1)
S('HBN12', 'erase', 0o3027, line=2800)  # B(1)
S('HBD11/2', 'erase', 0o3030, line=2801)  # B(1)
S('HBD12', 'erase', 0o3031, line=2802)  # B(1)
S('HBN20', 'erase', 0o3032, line=2803)  # B(1)
S('HBN21/2', 'erase', 0o3033, line=2804)  # B(1)
S('HBN22', 'erase', 0o3034, line=2805)  # B(1)
S('HBD21/2', 'erase', 0o3035, line=2806)  # B(1)
S('HBD22', 'erase', 0o3036, line=2807)  # B(1)
S('HBN30', 'erase', 0o3037, line=2808)  # B(1)
S('HBN31/2', 'erase', 0o3040, line=2809)  # B(1)
S('HBN32', 'erase', 0o3041, line=2810)  # B(1)
# Page 103
S('HBD31/2', 'erase', 0o3042, line=2812)  # B(1)
S('HBD32', 'erase', 0o3043, line=2813)  # B(1)

# **** EXCLUSIVE TVC DAP VARIABLES. *****************   (5D)
S('V97VCNTR', 'erase', 0o3044, line=2816)  # B(1)
S('TEMPDAP', 'erase', 0o3045, line=2817)  # B(2)
S('MRKRTMP', 'equals', 0o3045, line=2818)  #       ((B(1)))
S('CNTR', 'erase', 0o3047, line=2819)  # B(1)
S('OGAD', 'erase', 0o3050, line=2820)  # B(1)

# **** EXCLUSIVE RCS DAP VARIABLES ******************   (13D)
S('RWORD1', 'erase', 0o3051, line=2823)  # B(1)
S('RWORD2', 'equals', 0o3052, line=2824)  # B(1)
S('PWORD1', 'equals', 0o3053, line=2825)  # B(1)
S('PWORD2', 'equals', 0o3054, line=2826)  # B(1)
S('YWORD1', 'equals', 0o3055, line=2827)  # B(1)
S('YWORD2', 'equals', 0o3056, line=2828)  # B(1)
S('BLAST', 'equals', 0o3057, line=2829)  # B(2)
S('BLAST1', 'equals', 0o3061, line=2830)  # B(2)
S('BLAST2', 'equals', 0o3063, line=2831)  # B(2)
S('T5PHASE', 'equals', 0o3065, line=2832)  # B(1)

# **** RCS/TVC DAP COMMON STORAGE. ******************   (16D)
S('DAPDATR1', 'erase', 0o3066, line=2835)  # B(1)DSP NOUN 46(R1)
S('DAPDATR2', 'erase', 0o3067, line=2836)  # B(1)DSP NOUN 46(R2)

S('IXX', 'erase', 0o3070, line=2838)  # B(1) CONSECUTIVE WITH IAVG, IAVG/TLX FOR
S('IAVG', 'erase', 0o3071, line=2839)  # B(1)                            MASSPROP
S('IAVG/TLX', 'erase', 0o3072, line=2840)  # B(1)

S('LEMMASS', 'erase', 0o3073, line=2842)  # B(1)DSP NOUN 47 (R2)
S('CSMMASS', 'erase', 0o3074, line=2843)  # B(1)DSP NOUN 47 (R1)
S('WEIGHT/G', 'erase', 0o3075, line=2844)  # B(1)
S('MASS', 'equals', 0o3075, line=2845)

S('AK', 'erase', 0o3076, line=2847)
S('AK1', 'erase', 0o3077, line=2848)
S('AK2', 'erase', 0o3100, line=2849)

S('RCSFLAGS', 'erase', 0o3101, line=2851)  # B(1) CONSECUTIVE WITH AK2 DOWNLINK
S('T5TEMP', 'erase', 0o3102, line=2852)  # B(1)
S('EDRIVEX', 'erase', 0o3103, line=2853)
S('EDRIVEY', 'erase', 0o3104, line=2854)
# Page 104
S('EDRIVEZ', 'erase', 0o3105, line=2856)

# INTEMP THRU INTEMP+14D ARE RESERVED FOR OVERLAYED TVC/RCS INTERUP TRUE TEMPORARIES
S('INTTEMP', 'erase', 0o3106, line=2859)  # (15)

# TVC/RCS THRU TVCRCS +11D RESERVED FOR DOWNLINKED VARIABLES
S('TVCRCS', 'erase', 0o3125, line=2862)  # (12)
# RCS (WBODYS,ADOTS)
# TVC(OMEGACS,OMEGABS)

# TVC DAP TEMPORARY VARIABLES*********************************

# TVC DAP INTERRUPT TRUE TEMPORARIES**************************

S('PHI333', 'equals', 0o3106, line=2870)  # B(1) TEMPORARY REGISTER
S('PSI333', 'equals', 0o3107, line=2871)  # B(1) COUNTING REGISTER
S('TEMP333', 'equals', 0o3110, line=2872)  # B(1) COUNTING REGISTER
S('VARST0', 'equals', 0o3111, line=2873)  # B(8) BREAKPOINTS AND SLOPES
S('VARST5', 'equals', 0o3116, line=2874)
S('LASTMASP', 'equals', 0o3122, line=2875)  # LAST VARST0 WORD
S('TVCTMP1', 'equals', 0o3123, line=2876)  # B(1)

# *******REGULAR TVC TEMPORARIES*************

# TVC ZEROING STARTS HERE

S('OMEGAC', 'equals', 0o3125, line=2882)  # I(6)
S('OMEGAXC', 'equals', 0o3125, line=2883)
S('OMEGAYC', 'equals', 0o3127, line=2884)
S('OMEGAZC', 'equals', 0o3131, line=2885)

S('OMEGAB', 'equals', 0o3133, line=2887)  # B(6)
S('OMEGAXB', 'equals', 0o3133, line=2888)
S('OMEGAYB', 'equals', 0o3135, line=2889)
S('OMEGAZB', 'equals', 0o3137, line=2890)

S('PTMP1', 'equals', 0o3141, line=2892)  # B(2)
S('PTMP2', 'equals', 0o3143, line=2893)  # B(2)
S('PTMP3', 'equals', 0o3145, line=2894)  # B(2)
S('PTMP4', 'equals', 0o3147, line=2895)  # B(2)
S('PTMP5', 'equals', 0o3151, line=2896)  # B(2)
# Page 105
S('PTMP6', 'equals', 0o3153, line=2898)  # B(2)

S('YTMP1', 'equals', 0o3155, line=2900)  # B(2)
S('YTMP2', 'equals', 0o3157, line=2901)  # B(2)
S('YTMP3', 'equals', 0o3161, line=2902)  # B(2)
S('YTMP4', 'equals', 0o3163, line=2903)  # B(2)
S('YTMP5', 'equals', 0o3165, line=2904)  # B(2)
S('YTMP6', 'equals', 0o3167, line=2905)  # B(2)

S('ROLLFIRE', 'equals', 0o3171, line=2907)  # B(1)
S('ROLLWORD', 'equals', 0o3172, line=2908)  # B(1)
S('TEMREG', 'equals', 0o3173, line=2909)  # B(1)

S('STROKER', 'equals', 0o3174, line=2911)  # B(1)

S('PERRB', 'equals', 0o3175, line=2913)  # B(2)
S('YERRB', 'equals', 0o3177, line=2914)  # B(2)

S('DELPBAR', 'equals', 0o3201, line=2916)  # B(2)
S('DELYBAR', 'equals', 0o3203, line=2917)  # B(2)

S('PDELOFF', 'equals', 0o3205, line=2919)  # B(2)
S('YDELOFF', 'equals', 0o3207, line=2920)  # B(2)

# TVC ZEROING LOOP ENDS HERE
S('TTMP1', 'equals', 0o3211, line=2923)  # B(2)
S('TTMP2', 'equals', 0o3213, line=2924)  # B(2)
S('DAP1', 'equals', 0o3215, line=2925)  # B(2)
S('DAP2', 'equals', 0o3217, line=2926)  # B(2)
S('DAP3', 'equals', 0o3221, line=2927)  # B(2)

S('PCMD', 'equals', 0o3223, line=2929)  # B(1)
S('YCMD', 'equals', 0o3224, line=2930)  # B(1), CONSECUTIVE WITH PCMD
S('T5TVCDT', 'equals', 0o3225, line=2931)  # B(1)
S('MDT', 'equals', 0o3226, line=2932)  # I(6)
S('KPRIMEDT', 'equals', 0o3234, line=2933)  # I(2)
S('KTLX/I', 'equals', 0o3236, line=2934)  # B(1)
S('TENMDOT', 'equals', 0o3237, line=2935)  # B(1)
S('1/CONACC', 'equals', 0o3240, line=2936)  # B(1)
S('VARK', 'equals', 0o3241, line=2937)  # B(1)
S('REPFRAC', 'equals', 0o3242, line=2938)  # B(1)
S('VCNTR', 'equals', 0o3243, line=2939)  # B(1)
S('TVCPHASE', 'equals', 0o3244, line=2940)  # B(1)
S('PCDUYPST', 'equals', 0o3245, line=2941)  # B(1)
S('PCDUZPST', 'equals', 0o3246, line=2942)  # B(1)
S('MCDUYDOT', 'equals', 0o3247, line=2943)  # B(1)
S('MCDUZDOT', 'equals', 0o3250, line=2944)  # B(1)
# Page 106
S('TVCEXPHS', 'equals', 0o3251, line=2946)  # B(1)
S('MASSTMP', 'equals', 0o3252, line=2947)  # B(1)  PROTECT
S('VCNTRTMP', 'equals', 0o3253, line=2948)  # B(1)    *PROTECT***

# STROKE TEST VARIABLES
S('STRKTIME', 'equals', 0o3254, line=2951)  # B(1)
S('CADDY', 'equals', 0o3255, line=2952)  # B(1)
S('N', 'equals', 0o3256, line=2953)  # B(1)
S('BUNKER', 'equals', 0o3257, line=2954)  # B(1)
S('REVS', 'equals', 0o3260, line=2955)  # B(1)
S('CARD', 'equals', 0o3261, line=2956)  # B(1)

# TVC ROLL DAP VARIABLES
S('OGANOW', 'equals', 0o3262, line=2959)  # B(1)
S('OGAPAST', 'equals', 0o3263, line=2960)  # B(1)
S('OGA', 'equals', 0o3264, line=2961)  # B(1)TMP
S('OGAERR', 'equals', 0o3264, line=2962)  # (ROLL DAP USES OGA, MEANS OGAERROR)
S('DELOGART', 'equals', 0o3265, line=2963)  # B(1)TMP
S('SGNRT', 'equals', 0o3266, line=2964)  # SIGN OF CGA RATE
S('DELOGA', 'equals', 0o3267, line=2965)  # USED IN ROLL LOGIC
S('I', 'equals', 0o3270, line=2966)  # USED IN ROLL LOGIC
S('IOGARATE', 'equals', 0o3271, line=2967)  # USED IN ROLL LOGIC

# TVC DAP RESTART TEMPORARIES.
S('PACTTMP', 'equals', 0o3272, line=2970)  # B(2)
S('YACTTMP', 'equals', 0o3274, line=2971)  # B(2)
S('CNTRTMP', 'equals', 0o3276, line=2972)  # B(1)
S('STRKTTMP', 'equals', 0o3277, line=2973)  # B(1)
S('DELBRTMP', 'equals', 0o3300, line=2974)  # B(2)
S('ERRBTMP', 'equals', 0o3302, line=2975)  # B(2)
S('CMDTMP', 'equals', 0o3304, line=2976)  # B(2)

S('TMP1', 'equals', 0o3306, line=2978)  # B(2)
S('TMP2', 'equals', 0o3310, line=2979)  # B(2)
S('TMP3', 'equals', 0o3312, line=2980)  # B(2)
S('TMP4', 'equals', 0o3314, line=2981)  # B(2)
S('TMP5', 'equals', 0o3316, line=2982)  # B(2)
S('TMP6', 'equals', 0o3320, line=2983)  # B(2)

# TVC DAP FILTER COEFFICIENTS TEMPORARIES
S('COEFFADR', 'equals', 0o3322, line=2986)  # B(1)
S('N10', 'equals', 0o3323, line=2987)  # I(15)
# Page 107

# OVERLAYS WITHIN TVC DAP

S('OGARATE', 'equals', 0o3133, line=2992)  # B(2)

S('PHASETMP', 'equals', 0o3211, line=2994)  # B(1) RESTART FOR CSM/LM V46 SWITCH-OVER
S('RTRNLOC', 'equals', 0o3213, line=2995)  # B(1) RESTART FOR CSM/LM V46 SWITCH-OVER
S('BZERO', 'equals', 0o3302, line=2996)
S('CZERO', 'equals', 0o3302, line=2997)
S('JZERO', 'equals', 0o3304, line=2998)
S('YZERO', 'equals', 0o3304, line=2999)

# 540.9 STORAGE .............

S('NBRCYCLS', 'equals', 0o3342, line=3003)  # B(1) COUNTER FOR P40,41 STEERING
S('NBRCYCLP', 'equals', 0o3343, line=3004)  # B(1) MAINTAIN ORDER
S('DELVSUM', 'equals', 0o3344, line=3005)  # I(6) P40,P41
S('DELVSUMP', 'equals', 0o3352, line=3006)  # I(6) P40,P41

# Page 108
# **** RCS DAP TEMPORARY VARIABLES. ********************        (95D)

# ** RCS INTERRUPT TRUE TEMPS ***************   (15D)
S('SPNDX', 'equals', 0o3106, line=3012)  # B(1)
S('DPNDX', 'equals', 0o3107, line=3013)  # B(1)TMP
S('KMPAC', 'equals', 0o3110, line=3014)  # B(2)TMP
S('KMPTEMP', 'equals', 0o3112, line=3015)  # B(1)TMP

S('XNDX1', 'equals', 0o3113, line=3017)  # B(1)TMP XNDX1 THRU NYJETS ARE OVERLAYED
S('XNDX2', 'equals', 0o3114, line=3018)  # B(1)TMP BY OTHER DAP ERASABLES SO
S('YNDX', 'equals', 0o3115, line=3019)  # B(1)TMP SHOULD ALWAYS BE DEFINED IN
S('ZNDX', 'equals', 0o3116, line=3020)  # B(1)TMP A BLOCK
S('RINDEX', 'equals', 0o3117, line=3021)  # B(1)TMP
S('PINDEX', 'equals', 0o3120, line=3022)  # B(1)TMP
S('YINDEX', 'equals', 0o3121, line=3023)  # B(1)TMP
S('NRJETS', 'equals', 0o3122, line=3024)  # B(1)TMP
S('NPJETS', 'equals', 0o3123, line=3025)  # B(1)TMP
S('NYJETS', 'equals', 0o3124, line=3026)  # B(1)TMP

S('WTEMP', 'equals', 0o3113, line=3028)  # B(2)TMP WTEMP THRU DELTEMPZ OVERLAY
S('DELTEMPX', 'equals', 0o3115, line=3029)  # B(2)TMP XNDX1 THRU NRJETS AND EDOT THRU
S('DELTEMPY', 'equals', 0o3117, line=3030)  # B(2)TMP ADBVEL
S('DELTEMPZ', 'equals', 0o3121, line=3031)  # B(2)TMP

S('EDOT', 'equals', 0o3115, line=3033)  # B(2)TMP EDOT THRU ADBVEL OVERLAY
S('AERR', 'equals', 0o3117, line=3034)  # B(1)TMP YNDX THRU NPJETS AND DELTEMPX
S('EDOTVEL', 'equals', 0o3120, line=3035)  # B(2)TMP THRU DELTEMPZ
S('AERRVEL', 'equals', 0o3122, line=3036)  # B(1)TMP
S('ADBVEL', 'equals', 0o3123, line=3037)  # B(1)TMP

# *** REGULAR RCS TEMPS *********************   (   ).

# *** RCS ZEROING LOOP STARTS HERE **********   (37)
S('WBODY', 'equals', 0o3125, line=3042)  # B(2)TMP
S('WBODY1', 'equals', 0o3127, line=3043)  # B(2)TMP
S('WBODY2', 'equals', 0o3131, line=3044)  # B(2)TMP
S('ADOT', 'equals', 0o3133, line=3045)  # B(2)TMP
S('ADOT1', 'equals', 0o3135, line=3046)  # B(2)TMP
S('ADOT2', 'equals', 0o3137, line=3047)  # B(2)TMP

S('MERRORX', 'equals', 0o3141, line=3049)  #  (2)
S('MERRORY', 'equals', 0o3143, line=3050)  #  (2)
S('MERRORZ', 'equals', 0o3145, line=3051)  #  (2)
S('DFT', 'equals', 0o3147, line=3052)  # B(1)TMP
S('DFT1', 'equals', 0o3150, line=3053)  # B(1)TMP
S('DFT2', 'equals', 0o3151, line=3054)  # B(1)TMP
S('DRHO', 'equals', 0o3152, line=3055)  # B(2)TMP
S('DRHO1', 'equals', 0o3154, line=3056)  # B(2)TMP
# Page 109
S('DRHO2', 'equals', 0o3156, line=3058)  # B(2)TMP
S('ATTSEC', 'equals', 0o3160, line=3059)  # B(1)TMP
S('TAU', 'equals', 0o3161, line=3060)  # B(1)TMP
S('TAU1', 'equals', 0o3162, line=3061)  # B(1)TMP
S('TAU2', 'equals', 0o3163, line=3062)  # B(1)TMP
S('BIAS', 'equals', 0o3164, line=3063)  # B(1)TMP
S('BIAS1', 'equals', 0o3165, line=3064)  # B(1)TMP
S('BIAS2', 'equals', 0o3166, line=3065)  # B(1)TMP
S('ERRORX', 'equals', 0o3167, line=3066)  # B(1)TMP
S('ERRORY', 'equals', 0o3170, line=3067)  # B(1)TMP
S('ERRORZ', 'equals', 0o3171, line=3068)  # B(1)TMP

# RCS ZERO LOOP ENDS HERE
# MORE RCS                        (69D)
S('THETADX', 'equals', 0o3172, line=3072)  # B(1)TMP MUST BE CONSECUTIVE WITH ERRORZ
S('THETADY', 'equals', 0o3173, line=3073)  # B(1)TMP
S('THETADZ', 'equals', 0o3174, line=3074)  # B(1)TMP

S('DELCDUX', 'equals', 0o3175, line=3076)  # B(2)TMP
S('DELCDUY', 'equals', 0o3177, line=3077)  # B(2)TMP
S('DELCDUZ', 'equals', 0o3201, line=3078)  # B(2)TMP

S('DCDU', 'equals', 0o3203, line=3080)  # B(6)TMP USED DURING P20
S('DTHETASM', 'equals', 0o3211, line=3081)  # B(6)TMP STEER LOW OUTPUT.

S('ATTKALMN', 'equals', 0o3217, line=3083)  # B(1)TMP
S('KMJ', 'equals', 0o3220, line=3084)  # B(1)TMP
S('KMJ1', 'equals', 0o3221, line=3085)  # B(1)TMP
S('KMJ2', 'equals', 0o3222, line=3086)  # B(1)TMP
S('J/M', 'equals', 0o3223, line=3087)  # B(1)TMP
S('J/M1', 'equals', 0o3224, line=3088)  # B(1)TMP
S('J/M2', 'equals', 0o3225, line=3089)  # B(1)TMP
S('RACFAIL', 'equals', 0o3226, line=3090)  # B(1)TMP
S('RBDFAIL', 'equals', 0o3227, line=3091)  # B(1)TMP
S('ACORBD', 'equals', 0o3230, line=3092)  # B(1)TMP
S('XTRANS', 'equals', 0o3231, line=3093)  # B(1)TMP
S('CH31TEMP', 'equals', 0o3232, line=3094)  # B(1)TMP
S('CHANTEMP', 'equals', 0o3233, line=3095)  # B(1)TMP
S('T5TIME', 'equals', 0o3234, line=3096)  # B(1)TMP
S('RHO', 'equals', 0o3235, line=3097)  # B(1)TMP
S('RHO1', 'equals', 0o3236, line=3098)  # B(1)TMP
S('RHO2', 'equals', 0o3237, line=3099)  # B(1)TMP
S('AMGB1', 'equals', 0o3240, line=3100)  # B(1)TMP
S('AMGB4', 'equals', 0o3241, line=3101)  # B(1)TMP
# Page 110
S('AMGB5', 'equals', 0o3242, line=3103)  # B(1)TMP
S('AMGB7', 'equals', 0o3243, line=3104)  # B(1)TMP
S('AMGB8', 'equals', 0o3244, line=3105)  # B(1)TMP
S('CAPSI', 'equals', 0o3245, line=3106)  # B(1)TMP
S('CDUXD', 'equals', 0o3246, line=3107)  # B(2)TMP
S('CDUYD', 'equals', 0o3250, line=3108)  # B(2)TMP
S('CDUZD', 'equals', 0o3252, line=3109)  # B(2)TMP
S('SLOPE', 'equals', 0o3254, line=3110)  # B(1)TMP
S('ADB', 'equals', 0o3255, line=3111)  # B(1)TMP
S('RMANNDX', 'equals', 0o3256, line=3112)  # B(1)TMP
S('PMANNDX', 'equals', 0o3257, line=3113)  # B(1)TMP
S('YMANNDX', 'equals', 0o3260, line=3114)  # B(1)TMP MUST BE LAST VARIABLE IN RCS

# Page 111
# ********** ENTRY DAP TEMPORARY VARIABLES. *********************       (69D)

# ANGLE REGISTERS FOR ENTRY DAPS
S('AOG', 'equals', 0o3261, line=3120)  # 1P
S('AIG', 'equals', 0o3262, line=3121)  # 1P
S('AMG', 'equals', 0o3263, line=3122)  # 1P
S('ROLL/180', 'equals', 0o3264, line=3123)  # 1P
S('ALFA/180', 'equals', 0o3265, line=3124)  # 1P
S('BETA/180', 'equals', 0o3266, line=3125)  # 1P
S('AOG/PIP', 'equals', 0o3267, line=3126)  # 1P
S('AIG/PIP', 'equals', 0o3270, line=3127)  # 1P
S('AMG/PIP', 'equals', 0o3271, line=3128)  # 1P
S('ROLL/PIP', 'equals', 0o3272, line=3129)  # 1P
S('ALFA/PIP', 'equals', 0o3273, line=3130)  # 1P
S('BETA/PIP', 'equals', 0o3274, line=3131)  # 1P

# GYMBAL DIFFERENCES OVER INTERNAL TCDU = .1 SEC.
S('-DELAOG', 'equals', 0o3275, line=3134)  # 1P
S('-DELAIG', 'equals', 0o3276, line=3135)  # 1P
S('-DELAMG', 'equals', 0o3277, line=3136)  # 1P

# ESTIMATED BODY RATES
S('CMDAPMOD', 'equals', 0o3300, line=3139)  # 1P GOES BEFORE PREL FOR TM.

S('PREL', 'equals', 0o3301, line=3141)  # 1P P TCDU/180         (ROLLDOT)
S('QREL', 'equals', 0o3302, line=3142)  # 1P Q TCDU/180         (PITCHDOT)
S('RREL', 'equals', 0o3303, line=3143)  # 1P R TCDU/180         (YAWDOT)

S('BETADOT', 'equals', 0o3304, line=3145)  # 1P MUST FOLLOW RREL. BETADOT TCDU/180
S('PHIDOT', 'equals', 0o3305, line=3146)  # 1P

# OLD (UNAVERAGED) BODY RATE MEASURE
S('OLDELP', 'equals', 0o3306, line=3149)  # 1P
S('OLDELQ', 'equals', 0o3307, line=3150)  # 1P
S('OLDELR', 'equals', 0o3310, line=3151)  # 1P

S('JETAG', 'equals', 0o3311, line=3153)  # 1P
S('TUSED', 'equals', 0o3312, line=3154)  # 1P ELAPSED TIME SINCE NOMINAL UPDATE.

# FOLLOWING 3 SP WORDS IN DOWNLINK.  ROLLTM SENT EACH 1 SEC.
S('PAXERR1', 'equals', 0o3313, line=3157)  # 1P INTEGRATED ROLL ERROR/360.
S('ROLLTM', 'equals', 0o3314, line=3158)  # 1P ROLL/180 FOR TM.
S('ROLLC', 'equals', 0o3315, line=3159)  # 2P ROLLCOM/360 FROM ENTRY (FOR TM)
# KEEP ROLLC & ROLLHOLD ADJACENT FOR TP
# Page 112
S('ROLLHOLD', 'equals', 0o3317, line=3162)  # 1P FOR ATTITUDE HOLD IN CMDAPMOD = +1

# ENTRY DAP QUANTITIES THAT SHARE WITH RCS DAP.
S('ALFACOM', 'equals', 0o3203, line=3165)  # 1P KEEP ADJACENT TO BETACOM. <<
S('BETACOM', 'equals', 0o3204, line=3166)  # 1P

# JET LIST.  DT, JETBITS IN THIS ORDER.
S('TOFF', 'equals', 0o3205, line=3169)  # 1P DP PAIR
S('TBITS', 'equals', 0o3206, line=3170)  # 1P
S('TON2', 'equals', 0o3207, line=3171)  # 1P DP PAIR
S('T2BITS', 'equals', 0o3210, line=3172)  # 1P

# MISCELLANEOUS PERMANENT ERASABLE.
S('OUTTAG', 'equals', 0o3211, line=3175)  # 1P
S('NUJET', 'equals', 0o3212, line=3176)  # 1P

# MORE ENTRY DAP QUANTITIES THAT DO NOT SHARE WITH RCS DAP.
S('JETEM', 'equals', 0o3320, line=3179)  # 2P THIS DP USED IN RATEAVG
S('GAMA', 'equals', 0o3322, line=3180)  # 1P
S('GAMDOT', 'equals', 0o3323, line=3181)  # 1P
S('POSEXIT', 'equals', 0o3324, line=3182)  # 1P
S('CM/GYMDT', 'equals', 0o3325, line=3183)  # 1P
S('HEADSUP', 'equals', 0o3326, line=3184)  # 1P DSP NOUN 61 FOR P62,63,64,67.
S('P63FLAG', 'equals', 0o3327, line=3185)  # 1P INTERLOCK FOR WAKEP62

# >> SHARE BELOW WITH RCS RUPT TEMPS (< 15D) <<<
S('CALFA', 'equals', 0o3106, line=3188)  # 1P
S('SALFA', 'equals', 0o3107, line=3189)  # 1P

S('SINM', 'equals', 0o3110, line=3191)  # 1P
S('COSM', 'equals', 0o3111, line=3192)  # 1P
S('SINO', 'equals', 0o3112, line=3193)  # 1P
S('COSO', 'equals', 0o3113, line=3194)  # 1P
S('SINOCOSM', 'equals', 0o3114, line=3195)  # 1P
S('COSOCOSM', 'equals', 0o3115, line=3196)  # 1P
# >> SHARE ABOVE WITH RCS RUPT TEMPS <<<

# THE FOLLOWING FEW REGISTERS USED ONCE EACH 2 SEC
S('-VT/180', 'equals', 0o3213, line=3200)  # 1P
S('LCX/360', 'equals', 0o3214, line=3201)  # 1P
S('XD/360', 'equals', 0o3215, line=3202)  # 1P
S('VSQ/4API', 'equals', 0o3216, line=3203)  # 1P
S('JNDX', 'equals', 0o3217, line=3204)  # 1P
S('JNDX1', 'equals', 0o3220, line=3205)  # 1P
# Page 113
S('TON1', 'equals', 0o3221, line=3207)  # 1P DP PAIR
S('T1BITS', 'equals', 0o3222, line=3208)  # 1P

# MISCELLANEOUS REGISTERS USED EACH UPDATE.
S('CM/SAVE', 'equals', 0o3223, line=3211)  # 1P
S('JETEM2', 'equals', 0o3224, line=3212)  # 1P TEMPORARY STORAGE

# DAP QUANTITIES SHARED WITH RCS DAP FOR TM & FLIGHT RECORDER.
S('VDT/180', 'equals', 0o3167, line=3215)  # 1P (EDIT)
S('-VT/180E', 'equals', 0o3170, line=3216)  # 1P (EDIT)

S('PAXERR', 'equals', 0o3076, line=3218)  # 1P ROLL ERROR FOR NEEDLES
S('QAXERR', 'equals', 0o3172, line=3219)  # 1P SINCE AK1 IS ZEROED IN ATM DAP.
S('RAXERR', 'equals', 0o3173, line=3220)  # 1P SINCE AK2 IS ZEROED IN TM DAP.

# *** COLMANU (R60,R62) ****
S('VECQTEMP', 'equals', 0o3310, line=3223)

# Page 114
# ******** KALCMANU VARIABLES. (71D) *******************************
S('BCDU', 'equals', 0o3261, line=3227)  # B(3)TMP
S('KSPNDX', 'equals', 0o3264, line=3228)  # B(1)TMP
S('KDPNDX', 'equals', 0o3265, line=3229)  # B(1)TMP

S('TMIS', 'equals', 0o3266, line=3231)  # I(18) MUST BE IN THE SAME BANK AS RCS DAP
S('COFSKEW', 'equals', 0o3310, line=3232)  # I(6) MUST BE IN THE SAME BANK AS RCS DAP
S('CAM', 'equals', 0o3316, line=3233)  # I(2) MUST BE IN THE SAME BANK AS RCS DAP

S('MIS', 'equals', 0o3320, line=3235)  # I(18) (THE REST MAY GO ANYWHERE)
S('COF', 'equals', 0o3342, line=3236)  # I(6)TMP
S('SCAXIS', 'equals', 0o3350, line=3237)  # I(6)TMP
S('POINTVSM', 'equals', 0o3356, line=3238)  # I(6)TMP
S('AM', 'equals', 0o3364, line=3239)  # I(2)TMP
S('RAD', 'equals', 0o3366, line=3240)  # I(2)TMP

# FIRST-ORDER OVERLAYS IN KALCMANU
S('KV1', 'equals', 0o3266, line=3243)  # I(6)TMP
S('MFISYM', 'equals', 0o3266, line=3244)  # I   TMP
S('TMFI', 'equals', 0o3266, line=3245)  # I   TMP
S('NCDU', 'equals', 0o3266, line=3246)  # B   TMP
S('NEXTIME', 'equals', 0o3271, line=3247)  # B   TMP
S('TTEMP', 'equals', 0o3272, line=3248)  # B   TMP
S('KV2', 'equals', 0o3274, line=3249)  # I(6)TMP
S('BIASTEMP', 'equals', 0o3274, line=3250)  # B   TMP
S('KV3', 'equals', 0o3302, line=3251)  # I(6)TMP
S('CGF', 'equals', 0o3302, line=3252)  # I   TMP

S('BRATE', 'equals', 0o3310, line=3254)  # B   TMP
S('TM', 'equals', 0o3316, line=3255)  # B   TMP

# SECOND-ORDER OVERLAYS IN KALCMANU
S('P21', 'equals', 0o3266, line=3258)  # I(2)TMP
S('D21', 'equals', 0o3270, line=3259)  # I(2)TMP
S('G21', 'equals', 0o3272, line=3260)  # I(2)TMP

# SATURN BOOST STORAGE.  SAVE TILL RCS DAP OPERATION.   (17D)
S('POLYNUM', 'equals', 0o3261, line=3263)  # B(15) PAD LOADED
S('POLYLOC', 'equals', 0o3273, line=3264)
S('SATRLRT', 'equals', 0o3300, line=3265)  # B(2)  PAD LOADED

# MORE P11 STORAGE --PAD LOADED--       (2D)
# Page 115
# (NOTE:  THIS PAD LOAD WILL NOT BE PRESERVED THROUGHOUT THE MISSION AS IT SHARES STORAGE WITH KALCMANU,
# ENTRY DAP AND TVC DAP)
S('RPSTART', 'equals', 0o3302, line=3271)  # B(1) PITCH ROLL START TIME
S('POLYSTOP', 'equals', 0o3303, line=3272)  # B(1) POLYCUT OFF MINUS RPSTART SEC

# STORAGE FOR VHHDOT AND ATTDSP
S('BODY3', 'equals', 0o3304, line=3275)  # B(1)OUT
S('BODY2', 'equals', 0o3305, line=3276)  # B(1)OUT
S('BODY1', 'equals', 0o3306, line=3277)  # B(1)OUT
S('SPOLYARG', 'equals', 0o3307, line=3278)  # B(1)TMP ARGUMENT FOR POLLY

S('OLDBODY1', 'equals', 0o3103, line=3280)  # 1 PULSE = 0.0432 DEGREES
S('OLDBODY2', 'equals', 0o3104, line=3281)
S('OLDBODY3', 'equals', 0o3105, line=3282)

# STORAGE FOR S11.1
S('VDISP', 'equals', 0o3310, line=3285)  # I(2)OUT       2(7) M/CS
S('HDISP', 'equals', 0o3312, line=3286)  # I(2)OUT       2(29) M
S('HDOTDISP', 'equals', 0o3314, line=3287)  # I(2)OUT       2(7) M/CS
S('BOOSTEMP', 'equals', 0o3316, line=3288)  # B(3)TEMP

# P11 SATURN I/F                        (9D)
S('SATRATE', 'equals', 0o3321, line=3291)  # B(4)PL MANEUVER RATES FOR SATURN STICK
S('SATSW', 'equals', 0o3325, line=3292)  # B(1)TEM STATUS SW FOR BOOST TAKEOVER
S('BIASAK', 'equals', 0o3326, line=3293)  # B(3)TEM STOR AKBIAS FOR BOOST TAKEOVER
S('SATSCALE', 'equals', 0o3331, line=3294)  # B(1) SCALE FACTOR FOR SATURN STEERING

# P21 STORAGE.                          (1D)
S('GENRET', 'equals', 0o3370, line=3297)  # B(1)TMP

# R61CSM STORAGE.                       (1D)
S('SAVBNK', 'equals', 0o3371, line=3300)  # B(1) S-S SAVE EBANK FOR R61 SUBROUTINE

# CRS61.1 STORAGE FOR AUTOPILOT BANK.   (3D)
S('SAVEDCDU', 'equals', 0o3372, line=3303)  # B(3)TMP

# R61 STORAGE.                          (1D)
# Page 116
S('R61CNTR', 'equals', 0o3375, line=3307)  #  (1)TMP

# ENTRY RESTART PROTECTION STORAGE.  --KEEP TEMPS IN ORDER--    (12D)
S('TEMPROLL', 'equals', 0o3370, line=3310)  # B(1)TMP COPY CYCLE REGISTER
S('TEMPALFA', 'equals', 0o3371, line=3311)  # B(1)TMP COPY CYCLE REGISTER
S('TEMPBETA', 'equals', 0o3372, line=3312)  # B(1)TMP COPY CYCLE REGISTER
S('60GENRET', 'equals', 0o3373, line=3313)  # B(1)TMP QSAVE FOR S61.1 AND ENTRY.
S('S61DT', 'equals', 0o3374, line=3314)  # B(1)TMP VARIABLE DT FOR S61.1 RESTART.

# ENTRY TM SHARING FOR ACCELERATION PROFILE.
S('XPIPBUF', 'equals', 0o3133, line=3317)  # B(1) PIPA BUFFER FOR TM DURING ENTRY.
S('YPIPBUF', 'equals', 0o3134, line=3318)  # B(1) PIPS FILED HERE EACH .5 SEC APPEAR
S('ZPIPBUF', 'equals', 0o3135, line=3319)  # B(1) ON DOWNLIST ONCE PER SECOND DURING
S('XOLDBUF', 'equals', 0o3136, line=3320)  # B(1) ENTRY AFTER RCS DAP HAS BEEN DIS-
S('YOLDBUF', 'equals', 0o3137, line=3321)  # B(1) ABLED.  NEWEST PIP VALUE REPLACES
S('ZOLDBUF', 'equals', 0o3140, line=3322)  # B(1) PIPBUF, WHICH IS MOVED INTO OLDBUF.

# REENTRY VARIABLES SHARED WITH RCS DAP FOR TM & FLIGHT RECORDER.
S('Q7', 'equals', 0o3174, line=3325)  # I(2) HI-WORD ONLY ON DNLIST.
S('ASPS(TM)', 'equals', 0o3125, line=3326)  # I(6)DWN
# ASKEP, ASP1, ASPUP, ASPDN, ASP3, ASP3+1

# P37 PAD LOADS                         (1)
S('P37RANGE', 'equals', 0o3376, line=3330)  # I(1)PL        *****

S('END-E6', 'equals', 0o3377, line=3332)  # FIRST UNUSED ERASABLE LOCATION IN E6

# Page 117
# EBANK-7 ASSIGNMENTS

#   SETLOC 3400

# *-*-*-*- OVERLAY NUMBER 0 IN EBANK 7 -*-*-*-*

# EXTERNAL DELTA-V UPDATE.              (21D)
# (MUST BE IN ORDER FOR UPDATE PROGRAM.  ALSO ENTRY PROGRAM PICK UP 'LAT(SPL' WITH A VLOAD.)

S('LAT(SPL)', 'erase', 0o3400, line=3344)  # I(2)DSP NOUN 61 FOR P62,63,64,67
S('LNG(SPL)', 'equals', 0o3402, line=3345)  # I(2)DSP NOUN 61 FOR P62,63,64,67

S('DELVSLV', 'equals', 0o3404, line=3347)  # I(6)TMP DELTA VEL VECT, LOC VER COORDS
S('TIG', 'equals', 0o3412, line=3348)  # B(2)DSP NOUN 33 FOR X-V84(R32),P30,40.
S('RTARG', 'equals', 0o3414, line=3349)  # I(6)IN DESIRED VEHICLE RADIUS VECTOR
S('DELLT4', 'equals', 0o3422, line=3350)  # I(2)IN TIME DIFFERENCE FOR INITVEL
S('ECSTEER', 'equals', 0o3424, line=3351)  # I(1)PL FOR P40'S
S('DELVLVC', 'equals', 0o3404, line=3352)
S('END-DELV', 'erase', 0o3425, line=3353)  # *NEXT AVAIL LOC AFTER UNSHARED E7*

# SERVICER STORAGE.                     (13D)
S('DVTOTAL', 'equals', 0o3425, line=3356)  # B(2)DSP NOUN 40,99 FOR P30,34,35,40
S('TGO', 'equals', 0o3427, line=3357)  # B(2)
S('DVCNTR', 'equals', 0o3431, line=3358)  # B(1)TMP
S('DELVREF', 'equals', 0o3432, line=3359)  # I(6)TMP

S('NOMTIG', 'equals', 0o3447, line=3361)  # I(2) (CANNOT SHARE WITH KALCMANU
# OR DELVREF)
S('END-SVCR', 'equals', 0o3451, line=3363)  # ***NEXT AVAILABLE AFTER SERVICER

# ALIGNMENT STORAGE.                    (25D)
S('XSCD', 'equals', 0o3451, line=3366)  # I(6)TMP
S('YSCD', 'equals', 0o3457, line=3367)  # I(6)TMP
S('ZSCD', 'equals', 0o3465, line=3368)  # I(6)TMP
S('VEL/C', 'equals', 0o3473, line=3369)  # I(6)TMP
S('R53EXIT', 'equals', 0o3501, line=3370)  # I(1)TMP

# ALIGNMENT MARKDATA (DOWNLINK) ******* (7D)
S('MARK2DWN', 'equals', 0o3502, line=3373)  #  (7) USED BY ALIGNMENT P50'S

# Page 118
# *-*-*-*- OVERLAY NUMBER 1 IN EBANK 7 -*-*-*-*

# REENTRY ERASABLES.                    (206D)
S('RTINIT', 'equals', 0o3451, line=3379)  # 6P
S('RTEAST', 'equals', 0o3457, line=3380)  # 6P
S('RTNORM', 'equals', 0o3465, line=3381)  # 6P
S('RT', 'equals', 0o3473, line=3382)  # 6P
S('UNI', 'equals', 0o3501, line=3383)  # 6P
S('UNITV', 'equals', 0o3507, line=3384)  # 6P
S('VEL', 'equals', 0o3515, line=3385)  # 6P

S('TIME/RTO', 'equals', 0o3523, line=3387)  # 2P TIME OF INITIAL TARGET, RTO.
S('-VREL', 'equals', 0o3525, line=3388)  # 6P
S('OLDUYA', 'equals', 0o3533, line=3389)  # 6P USED BY CM/POSE    (ENTRY DAP)
S('UXA/2', 'equals', 0o3541, line=3390)  # 6P USED BY CM/POSE    (ENTRY DAP) -UVA
S('URH', 'equals', 0o3541, line=3391)  #       P67 DISPLAY NOUN
S('UYA/2', 'equals', 0o3547, line=3392)  # 6P USED BY CM/POSE    (ENTRY DAP) UYA
S('UZA/2', 'equals', 0o3555, line=3393)  # 6P USED BY CM/POSE    (ENTRY DAP) UNA
S('UBX/2', 'equals', 0o3563, line=3394)  # 6P USED BY CM/POSE    (ENTRY DAP)
S('UBY/2', 'equals', 0o3571, line=3395)  # 6P USED BY CM/POSE    (ENTRY DAP)
S('UBZ/2', 'equals', 0o3577, line=3396)  # 6P USED BY CM/POSE    (ENTRY DAP)

S('DTEAROT', 'equals', 0o3605, line=3398)  # 2P
S('DIFF', 'equals', 0o3607, line=3399)  # 2P
S('DIFFOLD', 'equals', 0o3611, line=3400)  # 2P
S('FACTOR', 'equals', 0o3613, line=3401)  # 2P
S('FACT1', 'equals', 0o3615, line=3402)  # 2P
S('FACT2', 'equals', 0o3617, line=3403)  # 2P
# Q7             =       THETAD2         # 2P SHARED FOR TM.  P64-P66
S('VSQUARE', 'equals', 0o3621, line=3405)  # 2P
S('LAD', 'equals', 0o3623, line=3406)  # 2P
S('LOD', 'equals', 0o3625, line=3407)  # 2P
S('L/DCMINR', 'equals', 0o3627, line=3408)  # 2P
S('KLAT', 'equals', 0o3631, line=3409)  # 2P
S('L/D', 'equals', 0o3633, line=3410)  # 2P
S('L/D1', 'equals', 0o3635, line=3411)  # 2P
S('LEWD', 'equals', 0o3724, line=3412)  # 2P SHARED FOR TM.  P64-P65
S('D', 'equals', 0o3637, line=3413)  # 2P DSP NOUN 64,66,68 FOR P63,64,67
# V1             =       ENDBUF  +1      # 2P SHARED FOR TM. P64-P65
S('DLEWD', 'equals', 0o3641, line=3415)  # 2P
S('K2ROLL', 'equals', 0o3643, line=3416)  # 2P
S('GOTOADDR', 'equals', 0o3645, line=3417)  # 1P
S('TEM1B', 'equals', 0o3646, line=3418)  # 2P
S('MM', 'equals', 0o3650, line=3419)  # 2P
S('GRAD', 'equals', 0o3651, line=3420)  # 2P
S('FX', 'equals', 0o3652, line=3421)  # 1P OVERWRITES NEXT 5 LOCS IN P67
S('LEQ', 'equals', 0o3653, line=3422)  # 2P
S('DHOOK', 'equals', 0o3655, line=3423)  # 2P
S('AHOOKDV', 'equals', 0o3657, line=3424)  # 2P
# Page 119
S('DVL', 'equals', 0o3661, line=3426)  # 2P
# A0             =       ENDBUF  +3      # 2P SHARED FOR TM. (HI-WD) P84-P85
S('A1', 'equals', 0o3663, line=3428)  # 2P
S('VBARS', 'equals', 0o3665, line=3429)  # 2P
S('COSG/2', 'equals', 0o3667, line=3430)  # 2P
# GAMMAL         =       GAMMAEI         # 2P SHARED FOR TM.  P64
S('GAMMAL1', 'equals', 0o26, line=3432)  # 2P
S('VS1', 'equals', 0o3671, line=3433)  # 2P
S('VL', 'equals', 0o3766, line=3434)  # 2P SHARED FOR TM.  P64-P65
S('V', 'equals', 0o3673, line=3435)  # 2P
# VREF           =       THETAD  +2      # 2P SHARED FOR TM.  P65
S('LATANG', 'equals', 0o3675, line=3437)  # 2P ADJACENT FOR TM.
S('RDOT', 'equals', 0o3677, line=3438)  # 2P ADJACENT FOR TM.
S('THETAH', 'equals', 0o3701, line=3439)  # 2P DSP NOUN 64,67 FOR P63,64,67
# RDOTREF        =       THETAD          # 2P SHARED FOR TM.  P65
S('ALP', 'equals', 0o3703, line=3441)  # 2P

S('ASKEP', 'equals', 0o3730, line=3443)  # 2P)                THESE ARE STORED IN
S('ASP1', 'equals', 0o3731, line=3444)  # 2P)                SEQUENCE, OVERLAPPING
S('ASPUP', 'equals', 0o3732, line=3445)  # 2P)>HI-WD OF EACH< HI-WORD ONLY APPEARING
S('ASPDWN', 'equals', 0o3733, line=3446)  # 2P)                ON DOWNLIST, EXCEPT
S('ASP3', 'equals', 0o3734, line=3447)  # 2P)                ASP3 IS COMPLETE.

S('C/D0', 'equals', 0o3705, line=3449)  # 2P    -1/D0
S('D0', 'equals', 0o3707, line=3450)  # I(2)  CONSTANT DRAG
S('Q2', 'equals', 0o3711, line=3451)  # 2P

# ROLLC IS LOCATED IN EBANK= AOG TO AID ENTRY DAP.
S('RTGO', 'equals', 0o3713, line=3454)  # 2P DSP NOUN 66 FOR P64,P67
S('DNRNGERR', 'equals', 0o3715, line=3455)  # 2P DSP NOUN 66 FOR P64,67
S('XRNGERR', 'equals', 0o3675, line=3456)  #       FOR DISKY DISPLAY
S('KAT', 'equals', 0o3717, line=3457)  # 2P
S('GMAX', 'equals', 0o3721, line=3458)  # 1P DSP NOUN 60 FOR P61,62,63
# GMAX IS LOADED IN DOUBLE PRECISION.
S('L/DCALC', 'equals', 0o3726, line=3460)  # 2P CALCULATED L/D FOR TM: P64-P67.
S('GAMMAL', 'equals', 0o3770, line=3461)  # 2P SHARED FOR TM.  P64.
S('PREDANG', 'equals', 0o3770, line=3462)  #       FOR TM IN P67.
S('JJ', 'equals', 0o3771, line=3463)  #       FOR TM IN P67.
S('VMAGI', 'equals', 0o3722, line=3464)  # 2P DSP NOUN 62,64,66 FOR P11,63,64.
S('VIO', 'equals', 0o3724, line=3465)  # 2P DSP NOUN 63 FOR P61.
S('TTE', 'equals', 0o3726, line=3466)  # 2P DSP NOUN 63 FOR P61.
S('ASPS', 'equals', 0o3730, line=3467)  # I(2) HI-WORD ONLY ON DNLIST FOR TEMP
S('TTE1', 'equals', 0o3732, line=3468)  # I(2)TMP HOLDS UNDECREMENTED TTE VALUE

# **** P6O'S ****
S('RTGON64', 'equals', 0o3713, line=3471)  # RANGE ERRORS NEGATIVE IF FALLS SHORT
# Page 120
S('RTGON67', 'equals', 0o3713, line=3473)  # DSP NOUN 67

# REENTRY, RETURN TO EARTH COMMON DISPLAY       (4D)
S('VPRED', 'equals', 0o3766, line=3476)  # DSP NOUN 60 FOR P61,62,63
S('GAMMAEI', 'equals', 0o3770, line=3477)  # DSP NOUN 60 FOR P61,62,63

# DISPLAY REGISTER FOR VG               (2D)
S('VGDISP', 'equals', 0o3772, line=3480)  # B(2)DSP N.40,42,99 FOR P30,34,35,37,40,
# 41 VG DISPLAY

# SOME P11 DISPLAY REGISTERS            (6D)
S('ALTI', 'equals', 0o3734, line=3484)  # 2P DSP NOUN 62 FOR P11.
S('HDOT', 'equals', 0o3736, line=3485)  # 2P DSP NOUN 62 FOR P11.

# Page 121
# *-*-*-*- OVERLAY NUMBER 2 IN EBANK 7 -*-*-*-*

# KALCMANU STORAGE.                             (18D)
S('MFS', 'equals', 0o3425, line=3491)  # I(18)
S('MFI', 'equals', 0o3425, line=3492)  # I    TMP
S('DEL', 'equals', 0o3425, line=3493)  # I    TMP
S('END-KALC', 'equals', 0o3447, line=3494)  # **NEXT AVAIL LOC AFTER KALCMANU**

# MEASUREMENT INCORPORATION STORAGE (R22) STORAGE.      (56D)

S('TX789', 'equals', 0o3447, line=3498)  # I(6)TMP
S('GAMMA', 'equals', 0o3455, line=3499)  # I(3)TMP
S('OMEGA', 'equals', 0o3457, line=3500)  # I(18)TMP
S('BVECTOR', 'equals', 0o3501, line=3501)  # I(18)TMP
S('DELTAQ', 'equals', 0o3523, line=3502)  # I(2)TMP
S('VARIANCE', 'equals', 0o3525, line=3503)  # I(3)TMP
S('RCLP', 'equals', 0o3530, line=3504)  # I(6)TMP
S('GRP2SVQ', 'equals', 0o3536, line=3505)  # I(1)TMP QSAVE FOR RESTARTS

# P20, P22, P23 DSP NOUN                (5D)
S('N49DISP', 'equals', 0o3501, line=3508)  # B(5)TMP

# S22.1 STORAGE.                        (36D)
S('SVMRKDAT', 'equals', 0o3537, line=3511)  # I(36)TMP 5 SETS OF MARK DATA +PAD OF ONE

# **** CISLUNAR NAV.  ERAS.  (P20'S) ****       (45D)
S('TRUNX', 'equals', 0o3603, line=3514)
S('DATATEST', 'equals', 0o3603, line=3515)  #  (1)
S('UBAR0', 'equals', 0o3604, line=3516)
S('UBAR1', 'equals', 0o3612, line=3517)
S('UBAR2', 'equals', 0o3620, line=3518)
S('RZC', 'equals', 0o3626, line=3519)
S('VZC', 'equals', 0o3634, line=3520)
S('UCLSTAR', 'equals', 0o3642, line=3521)
S('USSTAR', 'equals', 0o3650, line=3522)
S('SRRETURN', 'equals', 0o3656, line=3523)

# Page 122
# *-*-*-*- OVERLAY NUMBER 3 IN EBANK 7 -*-*-*-*

# RENDEZVOUS GUIDANCE STORAGE. -- P32 ... P35 --        (8D)
S('DELTEEO', 'equals', 0o3447, line=3529)  # I(2) S-S BACK VALUES OF DELTA TIME
S('DELEL', 'equals', 0o3451, line=3530)  # I(2) S-S
S('SECMAX', 'equals', 0o3453, line=3531)  # I(2) S-S MAX STOP SIZE FOR ROUTINE
S('XXXALT', 'equals', 0o3455, line=3532)  # I(2)

# S40.9 STORAGE                         (16D)
S('VG', 'equals', 0o3457, line=3535)  # I(6)TMP
S('VRPREV', 'equals', 0o3465, line=3536)  # I(6)
S('TNIT', 'equals', 0o3473, line=3537)  # I(2)
S('TNITPREV', 'equals', 0o3475, line=3538)  # I(2)

# S40.2,3 STORAGE.                      (1D)
S('AXISCODE', 'equals', 0o3477, line=3541)  # I(1)IN

# P30'S-P17 COMMON STORAGE.             (24D)
S('RACT3', 'equals', 0o3537, line=3544)  # I(6)TMP POSITION OF ACTIVE AT TPI TIME.
S('VACT3', 'equals', 0o3545, line=3545)  # I(6)TMP VELOCITY OF ACTIVE AT TPI TIME.
S('RPASS3', 'equals', 0o3553, line=3546)  # I(6)TMP POSITION OF PASSIVE AT TPI TIME.
S('VPASS3', 'equals', 0o3561, line=3547)  # I(6)TMP VELOCITY OF PASSIVE AT TPI TIME.

# P76, N84 DISPLAY                      (6D)
S('DELVOV', 'equals', 0o3537, line=3550)  # I(6)DSP NOUN 84 FOR X-V84, P34-35

# INITVEL/MIDGIM STORAGE.               (34D)
# (CALLED BY S34.1,2, S35.1,2, AND S40.9)
# (CALLS LAMBERT, CONIC SUBROUTINES)
S('RINIT', 'equals', 0o3567, line=3555)  # I(6)IN ACTIVE VEHICLE RADIUS VECTOR
S('VINIT', 'equals', 0o3575, line=3556)  # I(6)IN ACTIVE VEHICLE VELOCITY VECTOR
S('RTARG1', 'equals', 0o3603, line=3557)  # I(6)TMP SHIFTED RTARG
S('VIPRIME', 'equals', 0o3611, line=3558)  # I(6)OUT NEW VEL REQ AT INITIAL RADIUS
S('VTPRIME', 'equals', 0o3617, line=3559)  # I(6)OUT TOTAL VELOCITY AT DESIRED RADIUS
S('+MGA', 'equals', 0o3625, line=3560)  # I(2)DSP NOUN 45 FOR P30,34,35.  +MID GIM.
S('COZY4', 'equals', 0o3627, line=3561)  # I(2)TMP COSINE OF ANGLE WHEN ROT STARTS

# THE FOLLOWING OVERLAYS MEASUREMENT INCORP AND CANNOT SHARE WITH TPI
# Page 123
S('INTIME', 'equals', 0o3502, line=3565)
S('ITCTR', 'equals', 0o3504, line=3566)  # I(1)TMP ITERATION COUNTER
S('END-IN/M', 'equals', 0o3631, line=3567)  # ** NEXT AVAIL LOC AFTER INITVEL/MIDGIM **

# P34 AND P33 STORAGE.  (OVERLAYS INITVEL/MIDGIM)       (24D)
S('VAPREC', 'equals', 0o3567, line=3570)  # I(6) S-S PREC VEC FOR NOM TPI TIME (ACT V)
S('RAPREC', 'equals', 0o3575, line=3571)  # I(6) S-S PREC VEC FOR NOM TPI TIME (ACT V)
S('VPPREC', 'equals', 0o3611, line=3572)  # I(6) S-S PREC VEC FOR NOM TPI TIME (PASS)
S('RPPREC', 'equals', 0o3617, line=3573)  # I(6) S-S PREC VEC FOR NOM TPI TIME (PASS)

# P30, P40 INTERFACE.                   (20D)
S('RTIG', 'equals', 0o3631, line=3576)  # I(6)TMP
S('VTIG', 'equals', 0o3637, line=3577)  # I(6)TMP
S('DELVSIN', 'equals', 0o3645, line=3578)  # I(6)TMP
S('DELVEET3', 'equals', 0o3645, line=3579)  #     TMP DELTA VEL VECT INERTIAL COORDS.
S('VGTEMP', 'equals', 0o3645, line=3580)
S('DELVSAB', 'equals', 0o3653, line=3581)  # I(2)TMP

# P35-P40 INTERFACE STORAGE.  (OVERLAYS P30-P40 I/F STORAGE)    (12D)
S('RPASS4', 'equals', 0o3631, line=3584)  # I(6)TMP POSITION OF PASSIVE AT INTERCEPT
S('VPASS4', 'equals', 0o3637, line=3585)  # I(6)TMP VELOCITY OF PASSIVE AT INTERCEPT

# TPI SEARCH (P17)                      (6D)
S('E2', 'equals', 0o3645, line=3588)  # I(6)TMP

# P30-P40 COMMON STORAGE.               (3D)
S('TPASS4', 'equals', 0o3655, line=3591)  # I(2)TMP
S('TINT', 'equals', 0o3655, line=3592)  # I(2)
S('QTEMP', 'equals', 0o3657, line=3593)  # I(1)TMP

# P30-P40 STORAGE.                      (4D)
S('TTOGO', 'equals', 0o3660, line=3596)  # B(2)DSP NOUN 35,40,45,59,99
# FOR P30,34,35,40,41,47, R30.
S('TTPI', 'equals', 0o3662, line=3598)  # B(2)DSP NOUN 37 FOR P34 TPI TIME, CSECS.
# Page 124
S('END-P30S', 'equals', 0o3664, line=3600)  # ** NEXT AVAIL LOC AFTER P30-40 STORAGE. **

# P40 STORAGE.                          (8D)
S('VGBODY', 'equals', 0o3664, line=3603)  # B(6)DSP NOUN 85 FOR P40,41,42 VG-SC COOR
S('DELVCTL', 'equals', 0o3664, line=3604)
S('P40TMP', 'equals', 0o3672, line=3605)  # B(2)TMP

# P47 STORAGE.
S('DV47TEMP', 'equals', 0o3457, line=3608)
S('DELVIMU', 'equals', 0o3674, line=3609)  # I(6)DSP NOUN 83 FOR P47 DELTAV(IMU).

# S40.1 STORAGE.                        (23D)
S('CSTEER', 'equals', 0o3702, line=3612)  # I(2)IN
S('BDT', 'equals', 0o3704, line=3613)  # I(6)IN
S('UT', 'equals', 0o3712, line=3614)  # I(6)OUT THRUST DIRECTION
S('VGTIG', 'equals', 0o3720, line=3615)  # I(6)OUT
S('VGPREV', 'equals', 0o3720, line=3616)
S('F', 'equals', 0o3726, line=3617)  # I(2)OUT S40.3 NEEDS THIS

S('QTEMP1', 'equals', 0o3730, line=3619)  # I(1)TMP HOLDS RETURN

# R41                                   (2D)
S('T-TO-ADD', 'equals', 0o3731, line=3622)  # I(1D) FOR MIDTOAVE

# Page 125
# *-*-*-*- OVERLAY NUMBER 4 IN EBANK 7 -*-*-*-*

# S35.1 STORAGE.                        (2D)
S('TSTRT', 'equals', 0o3664, line=3628)  # I(2)IN MIDCOURSE START TIME

# S34.1 STORAGE.  (OVERLAYS S35.1 STORAGE)      (1)
S('TITER', 'equals', 0o3664, line=3631)  # I(1)TMP ITERATION COUNTER

# (P30-31 Q-SAVES)                      (1)
S('P30/31RT', 'equals', 0o3664, line=3634)  # B(1) RETURN POINT

# P22 STORAGE.                          (6D)
S('S22WUNL', 'equals', 0o3666, line=3637)  # 1     WUNL W8 UNKNOWN INIT VALUE.
S('S22TOFF', 'equals', 0o3667, line=3638)  # 2     T SUB OFF
S('S22TPRIM', 'equals', 0o3671, line=3639)  # 2     SAVE TF
S('S22EORM', 'equals', 0o3673, line=3640)  # 0 = EARTH -- NON-ZERO = MOON

# DOWNLINK ERASABLES FOR P22, P20 MARK DATA.    (8D)
S('MARKDOWN', 'equals', 0o3674, line=3643)  # B(1)
S('RM', 'equals', 0o3703, line=3644)  # DOWNLINK OF VHF RANGE

# S22.1                                 (1D)
S('S22RTNEX', 'equals', 0o3703, line=3647)  # B(1)

# P22 STORAGE                           (6D)
S('STARSAV3', 'equals', 0o3704, line=3650)  # I(6)TMP

# CRS61.1 STORAGE.  --A SUBSET OF P20-- (14D)
S('Q611', 'equals', 0o3704, line=3653)  # I(1)TMP QSAVE
S('Q6111', 'equals', 0o3705, line=3654)  # I(1)TMP QSAVE
S('SAVEPOS', 'equals', 0o3706, line=3655)  # I(6)TMP LEM POSITION VECTOR
# Page 126
S('SAVEVEL', 'equals', 0o3714, line=3657)  # I(6)TMP LEM VELOCITY VECTOR

# ATTITUDE MANEUVER -- CALLED BY P20,R61,R63,CRS61.1    (3D)
S('PRAXIS', 'equals', 0o3722, line=3660)  # B(3) S-S DISP RES FOR PREF AXIS N95.

# MARK ROUTINE (R21) STORAGE.  -- IS SUBSET OF R22 --   (14D)
S('MRKBUF1', 'equals', 0o3725, line=3663)  # B(7)TMP R21 MARK BUFFER.
S('MRKBUF2', 'equals', 0o3734, line=3664)  # B(7)TMP R21 MARK BUFFER.

# MORE CONICS STORAGE.                  (4)
S('COGA', 'equals', 0o3774, line=3667)  # I(2) COTAN OF INITIAL FLIGHT PATH ANGLE
S('INDEP', 'equals', 0o3774, line=3668)  # I(1) USED BY SUBROUTINE 'ITERATOR'
S('EPSILONL', 'equals', 0o3776, line=3669)  # I(2)TMP

# RENDEZVOUS GUIDANCE STORAGE.  -- P32...P35 -- (10D)
S('ELEV', 'equals', 0o3743, line=3672)  # I(2)TMP
S('RTX1', 'equals', 0o3745, line=3673)  #  (1)
S('RTX2', 'equals', 0o3746, line=3674)  #  (1)
S('RTMU', 'equals', 0o3747, line=3675)  #  (2)
S('RTSR1/MU', 'equals', 0o3751, line=3676)  #  (2)
S('CENTANG', 'equals', 0o3753, line=3677)  # I(2) S-S CENTRAL ANGLE COVERED (TPI-TFF)

# TPI SEARCH (S17.1, S17.2) P17 STORAGE.(10D)
S('DELTEE', 'equals', 0o3743, line=3680)  # I(2)
S('XRS', 'equals', 0o3745, line=3681)  # I(2)
S('THETL', 'equals', 0o3747, line=3682)  # I(2)
S('TF', 'equals', 0o3751, line=3683)  # I(2)
S('DELHITE', 'equals', 0o3753, line=3684)  #  (2)

# Page 127
# *-*-*-*- OVERLAY NUMBER 5 IN EBANK 7 -*-*-*-*

# P17,P34                               (2D)
S('NN1', 'equals', 0o3765, line=3690)  # I(2)DSP NOUN 55,R1

# ********* THE FOLLOWING ARE FOR FLIGHT 504 ONLY *************

# RETURN-TO-EARTH STORAGE.              (93D)
S('RTEDVD', 'equals', 0o3631, line=3695)  # I(2)IN DELTA VELOCITY DESIRED         M/CS B7
S('RTEGAM2D', 'equals', 0o3633, line=3696)  # I(2)IN REENTRY ANGLE DESIRED          REVS B0
S('RCON', 'equals', 0o3635, line=3697)  # I(2)TMP CONIC R2 RADIUS               M B29
S('R(T1)/', 'equals', 0o3637, line=3698)  # I(6)TMP POSITION VECTOR AT TIG        M B29/B27
S('R(T1)', 'equals', 0o3645, line=3699)  # I(2)TMP MAGNITUDE OF R(T1)/           M B29/B27
S('DT21PR', 'equals', 0o3647, line=3700)  # I(2)TMP PREVIOUS DT21                 CS B30
S('MAMAX1', 'equals', 0o3651, line=3701)  # I(2)TMP MAJ AXIS LOW BOUND LMT        M B30
S('MAMAX2', 'equals', 0o3653, line=3702)  # I(2)TMP MAJ AXIS UP BOUND LMT         M B30
S('R(T2)/', 'equals', 0o3655, line=3703)  # I(6)TMP FINAL POSITION VECTOR         M B29/B27
S('RD', 'equals', 0o3663, line=3704)  # I(2)TMP FINAL R DESIRED               M B29/B27
S('DRCON', 'equals', 0o3665, line=3705)  # I(2)TMP RCON SLOPE ITERATOR           M B29/B27
S("RPRE'", 'equals', 0o3667, line=3706)  # I(2)TMP PREVIOUS RPRE                 M B29/B27
S('V(T1)/', 'equals', 0o3671, line=3707)  # I(6)TMP VEL VECTOR AT TIG             M/CS B7/B5
S('V2(T1)/', 'equals', 0o3677, line=3708)  # I(6)TMP POST IMP VEL AT TIG           M/CS B7/B5
S('DV', 'equals', 0o3705, line=3709)  # I(2)TMP DELTA VELOCITY AT TIG         M/CS B7/B5
S('V(T2)/', 'equals', 0o3707, line=3710)  # I(6)TMP FINAL VELOCITY VECTOR         M/CS B7/B5
S('T1', 'equals', 0o3715, line=3711)  # I(2)TMP INITIAL VECTOR TIME           CS B28
S('PCON', 'equals', 0o3717, line=3712)  # I(2)TMP SEMI-LATUS RECTUM             M B29
S('X(T1)', 'equals', 0o3721, line=3713)  # I(2)TMP COTANGENT GAMMA1              B5
S('T12', 'equals', 0o3723, line=3714)  # I(2)TMP INIT TO FINAL POSIT TIME      CS B28
S('DELTAT', 'equals', 0o3725, line=3715)  # I(2)TMP DELTA T IN SAVE PERILUNE      CS B28
S('NN1A', 'equals', 0o3727, line=3716)  # I(2)TMP ITERATION COUNTER 1
S('NN2', 'equals', 0o3731, line=3717)  # I(2)TMP ITERATION COUNTER 2
S('RTENCKEX', 'equals', 0o3733, line=3718)  # I(1)TMP RTENCK RETURN ADDRESS
S('CONICX1', 'equals', 0o3734, line=3719)  # I(1)TMP CONICS MU TABLE INDEX
S('T2', 'equals', 0o3735, line=3720)  # I(2)TMP FINAL TIME                    CS B28
S('UR1/', 'equals', 0o3737, line=3721)  # I(6)TMP UNIT R(T1)/                   B1
S('UV1/', 'equals', 0o3745, line=3722)  # I(6)TMP UNIT V(T1)/                   B1
S('BETA1', 'equals', 0o3753, line=3723)  # I(2)TMP 1+X(T2)**2                    B1
S('P(T1)', 'equals', 0o3755, line=3724)  # I(1)TMP PRIMARY BODY STATE TIME 1     B14
S('CFPA', 'equals', 0o3756, line=3725)  # I(2)TMP COSINE FLIGHT PATH ANGLE      B1
S('PHI2', 'equals', 0o3760, line=3726)  # I(2)TMP PERI OR APO INDICATOR         B2
S('SPRTEX', 'equals', 0o3762, line=3727)  # I(1)TMP ROUTINE RETURN ADDRESS
S('VNSTORE', 'equals', 0o3763, line=3728)  # I(1)TMP VERBNOUN STORAGE
S('BETA12', 'equals', 0o3764, line=3729)  # I(2)TMP SIGN FOR TIMERAD

# OVERLAYS WITHIN RETURN-TO-EARTH STORAGE.
# Page 128
S('RPRE', 'equals', 0o30, line=3733)  # I(2)TMP COMPUTED PREC RADIUS          M B29/B27
S('P/RPRE', 'equals', 0o32, line=3734)  # I(2)TMP P/R                           B4
S('R/APRE', 'equals', 0o34, line=3735)  # I(2)TMP R/A                           B6
S('X(T2)PRE', 'equals', 0o3723, line=3736)  # I(2)TMP PREC COTAN GAMMA2             B0
S('X(T2)', 'equals', 0o3725, line=3737)  # I(2)TMP COTAN GAMMA2                  B0
S('UH/', 'equals', 0o3745, line=3738)  # I(2)TMP UNIT HORIZONTAL VECTOR.       B1
S('SPRTETIG', 'equals', 0o3412, line=3739)  # I(2)IN TIME OF IGNITION               CS B28

# Page 129
# *-*-*-*- OVERLAY 6 IN EBANK 7 -*-*-*-*
# P32,P33

# THE FOLLOWING OVERLAY MEAS. INCORP. ARE AND IN USE ONLY WHEN (32D)
S('POSTCSI', 'equals', 0o3457, line=3746)  # I(2)
S('DELVCSI', 'equals', 0o3461, line=3747)  # I(2)
S('DELDV', 'equals', 0o3463, line=3748)  # I(2)
S('GAMPREV', 'equals', 0o3465, line=3749)  # I(2)
S('DVPREV', 'equals', 0o3467, line=3750)  # I(2)
S('POSTCDH', 'equals', 0o3471, line=3751)  # I(2)
S('HAFPA1', 'equals', 0o3471, line=3752)
S('VACT4', 'equals', 0o3473, line=3753)  # I(6)
S('RDOTV', 'equals', 0o3501, line=3754)  # I(2)
S('VACT1', 'equals', 0o3503, line=3755)  # I(6)
S('VPASS1', 'equals', 0o3511, line=3756)  # I(6) VEL. PASSIVE VEH. AT CSI TIME

S('UNVEC', 'equals', 0o3545, line=3758)

S('T2TOT3', 'equals', 0o3655, line=3760)  # I(2) TPI - TCDH

S('CSIALRM', 'equals', 0o3664, line=3762)  # I(2) ALARM INDEX

S('DELVEET2', 'equals', 0o3666, line=3764)  # I(6) VACT3 - VACT2 = DVCDH REF. COORD.

# ADDITIONAL CSI - CDH STORAGE.         (10D)
S('RPASS1', 'equals', 0o3755, line=3767)  # I(6) POS. PASSIVE VEH. AT CSI TIME.
S('LOOPCT', 'equals', 0o3763, line=3768)  # I(2) ITERATION COUNTER
S('NN', 'equals', 0o3765, line=3769)  # I(2)

# P21 STORAGE                           (19D)
S('P21ORIG', 'equals', 0o3603, line=3772)  # I(1)
S('P21BASER', 'equals', 0o3604, line=3773)  # I(6)
S('P21BASEV', 'equals', 0o3612, line=3774)  # I(6)
S('P21ALT', 'equals', 0o3620, line=3775)  # I(2) NOUN 73 R1 ALTITUDE
S('P21VEL', 'equals', 0o3622, line=3776)  # I(2) NOUN 73 R2 VELOCITY
S('P21GAM', 'equals', 0o3624, line=3777)  # I(2) NOUN 73 R3 FLIGHT PATH ANGLE

# The following two statements had been just "WHOCARES = 3777".---RSB 2009
#   SETLOC 3777
S('WHOCARES', 'equals', 0o3777, line=3781)  # A DUMMY FOR E-BANK INSENSITIVE 2CADRS.
S('END-E7', 'equals', 0o3777, line=3782)  # ***** LAST LOCATION IN E7

# Page 130 ... is empty.
