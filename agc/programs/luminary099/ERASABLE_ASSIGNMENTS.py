"""ERASABLE_ASSIGNMENTS.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/ERASABLE_ASSIGNMENTS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 90-152 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('ERASABLE_ASSIGNMENTS', 'ERASABLE_ASSIGNMENTS.agc', 'Luminary099', pages='90-152')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     ERASABLE ASSIGNMENTS.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Onno Hommes <ohommes@cmu.edu>.
# Website:      www.ibiblio.org/apollo.
# Pages:        0090-0152
# Mod history:  2009-05-16 OH   Transcribed from page images.
# 2009-06-05 RSB  Eliminated a variable that shouldn't have
# survived from Luminary 131.
# 2010-12-31 JL   Fixed page number comment.
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

# Page 90
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

# THE SIZE AND UTILIZATION OF AN ERASABLE ARE OFTEN INCLUDED IN
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
# Page 91
# IT MAY BE SHARED WITHANY OTHER ROUTINE WHICH
# IS NOT ACTIVE IN PARALLEL
# IN      MEANS INPUT TO THE ROUTINE AND IT IS PROBABLY
# TEMPORARY FOR A HIGHER-LEVEL ROUTINE/PROGRAM.
# OUT     MEANS OUTPUT FROM THE ROUTINE, PROBABLY
# TEMPORARY FOR A HIGHER-LEVEL ROUTINE/PROGRAM.

# Page 92
# SPECIAL REGISTERS.

S('A', 'equals', 0o0, line=89)
S('L', 'equals', 0o1, line=90)  # L AND Q ARE BOTH CHANNELS AND REGISTERS
S('Q', 'equals', 0o2, line=91)
S('EBANK', 'equals', 0o3, line=92)
S('FBANK', 'equals', 0o4, line=93)
S('Z', 'equals', 0o5, line=94)  # ADJACENT TO FBANK AND BBANK FOR DXCH Z
S('BBANK', 'equals', 0o6, line=95)  # (DTCB) AND DXCH FBANK (DTCF).
# REGISTER 7 IS A ZERO-SOURCE, USED BY ZL.

S('ARUPT', 'equals', 0o10, line=98)  # INTERRUPT STORAGE
S('LRUPT', 'equals', 0o11, line=99)
S('QRUPT', 'equals', 0o12, line=100)
S('SAMPTIME', 'equals', 0o13, line=101)  # SAMPLED TIME 1 & 2.
S('ZRUPT', 'equals', 0o15, line=102)  # (13 AND 14 ARE SPARES.)
S('BANKRUPT', 'equals', 0o16, line=103)  # USUALLY HOLDS FBANK OR BBANK.
S('BRUPT', 'equals', 0o17, line=104)  # RESUME ADDRESS AS WELL.

S('CYR', 'equals', 0o20, line=106)
S('SR', 'equals', 0o21, line=107)
S('CYL', 'equals', 0o22, line=108)
S('EDOP', 'equals', 0o23, line=109)  # EDITS INTERPRETIVE OPERATION CODE PAIRS.

S('TIME2', 'equals', 0o24, line=111)
S('TIME1', 'equals', 0o25, line=112)
S('TIME3', 'equals', 0o26, line=113)
S('TIME4', 'equals', 0o27, line=114)
S('TIME5', 'equals', 0o30, line=115)
S('TIME6', 'equals', 0o31, line=116)
S('CDUX', 'equals', 0o32, line=117)
S('CDUY', 'equals', 0o33, line=118)
S('CDUZ', 'equals', 0o34, line=119)
S('CDUT', 'equals', 0o35, line=120)  # REND RADAR TRUNNION CDU
S('CDUS', 'equals', 0o36, line=121)  # REND RADAR SHAFT CDU
S('PIPAX', 'equals', 0o37, line=122)
S('PIPAY', 'equals', 0o40, line=123)
S('PIPAZ', 'equals', 0o41, line=124)
S('Q-RHCCTR', 'equals', 0o42, line=125)  # RHC COUNTER REGISTERS
S('P-RHCCTR', 'equals', 0o43, line=126)
S('R-RHCCTR', 'equals', 0o44, line=127)
S('INLINK', 'equals', 0o45, line=128)
S('RNRAD', 'equals', 0o46, line=129)
S('GYROCMD', 'equals', 0o47, line=130)
S('CDUXCMD', 'equals', 0o50, line=131)
S('CDUYCMD', 'equals', 0o51, line=132)
S('CDUZCMD', 'equals', 0o52, line=133)
S('CDUTCMD', 'equals', 0o53, line=134)
S('CDUSCMD', 'equals', 0o54, line=135)
# Page 93
S('THRUST', 'equals', 0o55, line=137)
S('LEMONM', 'equals', 0o56, line=138)
S('OUTLINK', 'equals', 0o57, line=139)
S('ALTM', 'equals', 0o60, line=140)

# INTERPRETIVE REGISTERS ADDRESSED RELATIVE TO VAC AREA.

S('LVSQUARE', 'equals', 0o42, line=144)  # SQUARE OF VECTOR INPUT TO ABVAL AND UNIT
S('LV', 'equals', 0o44, line=145)  # LENGTH OF VECTOR INPUT TO UNIT.
S('X1', 'equals', 0o46, line=146)  # INTERPRETIVE SPECIAL REGISTER RELATIVE
S('X2', 'equals', 0o47, line=147)  # TO THE WORK AREA.
S('S1', 'equals', 0o50, line=148)
S('S2', 'equals', 0o51, line=149)
S('QPRET', 'equals', 0o52, line=150)

# INPUT/OUTPUT CHANNELS

# *** CHANNEL ZERO IS TO BE USED IN AN INDEXED OPERATION ONLY. ***
S('LCHAN', 'equals', 0o1, line=155)
S('QCHAN', 'equals', 0o2, line=156)
S('HISCALAR', 'equals', 0o3, line=157)
S('LOSCALAR', 'equals', 0o4, line=158)
S('CHAN5', 'equals', 0o5, line=159)
S('CHAN6', 'equals', 0o6, line=160)
S('SUPERBNK', 'equals', 0o7, line=161)  # SUPER-BANK.
S('OUT0', 'equals', 0o10, line=162)
S('DSALMOUT', 'equals', 0o11, line=163)
S('CHAN12', 'equals', 0o12, line=164)
S('CHAN13', 'equals', 0o13, line=165)
S('CHAN14', 'equals', 0o14, line=166)
S('MNKEYIN', 'equals', 0o15, line=167)
S('NAVKEYIN', 'equals', 0o16, line=168)
S('CHAN30', 'equals', 0o30, line=169)
S('CHAN31', 'equals', 0o31, line=170)
S('CHAN32', 'equals', 0o32, line=171)
S('CHAN33', 'equals', 0o33, line=172)
S('DNTM1', 'equals', 0o34, line=173)
S('DNTM2', 'equals', 0o35, line=174)

# END OF CHANNEL ASSIGNMENTS

# Page 94
# INTERPRETIVE SWITCH BIT ASSIGNMENTS

# ** FLAGWORDS AND BITS NOW ASSIGNED AND DEFINED IN THEIR OWN LOG SECTION. **

# Page 95
# GENERAL ERASABLE ASSIGNMENTS

#   SETLOC 61
# INTERRUPT TEMPORARY STORAGE POOL.     (11D)

# (ITEMP1 THROUGH RUPTREG4)

# ANY OF THESE MAY BE USED AS TEMPORARIES DURING INTERRUPT OR WITH INTERRUPT INHIBITED. THE ITEMP SERIES
# IS USED DURING CALLS TO THE EXECUTIVE AND WAITLIST -- THE RUPTREGS ARE NOT.

S('ITEMP1', 'erase', 0o61, line=194)
S('WAITEXIT', 'equals', 0o61, line=195)
S('EXECTEM1', 'equals', 0o61, line=196)

S('ITEMP2', 'erase', 0o62, line=198)
S('WAITBANK', 'equals', 0o62, line=199)
S('EXECTEM2', 'equals', 0o62, line=200)

S('ITEMP3', 'erase', 0o63, line=202)
S('RUPTSTOR', 'equals', 0o63, line=203)
S('WAITADR', 'equals', 0o63, line=204)
S('NEWPRIO', 'equals', 0o63, line=205)

S('ITEMP4', 'erase', 0o64, line=207)
S('LOCCTR', 'equals', 0o64, line=208)
S('WAITTEMP', 'equals', 0o64, line=209)

S('ITEMP5', 'erase', 0o65, line=211)
S('NEWLOC', 'equals', 0o65, line=212)

S('ITEMP6', 'erase', 0o66, line=214)
S('NEWLOC+1', 'equals', 0o66, line=215)  # DP ADDRESS.

#   SETLOC 67
S('NEWJOB', 'erase', 0o67, line=218)  # MUST BE AT LOC 67 DUE TO WIRING.

S('RUPTREG1', 'erase', 0o70, line=220)
S('RUPTREG2', 'erase', 0o71, line=221)
S('RUPTREG3', 'erase', 0o72, line=222)
S('RUPTREG4', 'erase', 0o73, line=223)
S('KEYTEMP1', 'equals', 0o73, line=224)
S('DSRUPTEM', 'equals', 0o73, line=225)

# FLAGWORD RESERVATIONS.                (16D)

S('STATE', 'erase', 0o74, line=229)  # +15D FLAGWORD REGISTERS

# P25 RADAR STORAGE.  (MAY BE UNSHARED IN E7)  (TEMP OVERLAY)  (2D)  OVERLAYS FLGWRD 14 & 15
# Page 96
S('LASTYCMD', 'equals', 0o112, line=233)  # B(1)PRM       THESE ARE CALLED BY T4RUPT
S('LASTXCMD', 'equals', 0o113, line=234)  # B(1)PRM       THEY MUST BE CONTIGUOUS, Y FIRST

# EXEC TEMPORARIES WHICH MAY BE USED BETWEEN CCS NEWJOBS (32D) (INTB15+ THROUGH RUPTMXTM)
S('INTB15+', 'erase', 0o114, line=237)  # REFLECTS 15TH BIT OF INDEXABLE ADDRESSES
S('DSEXIT', 'equals', 0o114, line=238)  # RETURN FOR DSPIN
S('EXITEM', 'equals', 0o114, line=239)  # RETURN FOR SCALE FACTOR ROUTINE SELECT
S('BLANKRET', 'equals', 0o114, line=240)  # RETURN FOR 2BLANK

S('INTBIT15', 'erase', 0o115, line=242)  # SIMILAR TO ABOVE.
S('WRDRET', 'equals', 0o115, line=243)  # RETURN FOR 5BLANK
S('WDRET', 'equals', 0o115, line=244)  # RETURN FOR DSPWD
S('DECRET', 'equals', 0o115, line=245)  # RETURN FOR PUTCOM(DEC LOAD)
S('21/22REG', 'equals', 0o115, line=246)  # TEMP FOR CHARIN

# THE REGISTERS BETWEEN ADDRWD AND PRIORITY MUST STAY IN THE FOLLOWING ORDER FOR INTERPRETIVE TRACE.

S('ADDRWD', 'erase', 0o116, line=250)  # 12 BIT INTERPRETIVE OPERAND SUB-ADDRESS.
S('POLISH', 'erase', 0o117, line=251)  # HOLDS CADR MADE FROM POLISH ADDRESS.
S('UPDATRET', 'equals', 0o117, line=252)  # RETURN FOR UPDATNN, UPDATVB
S('CHAR', 'equals', 0o117, line=253)  # TEMP FOR CHARIN
S('ERCNT', 'equals', 0o117, line=254)  # COUNTER FOR ERROR LIGHT RESET
S('DECOUNT', 'equals', 0o117, line=255)  # COUNTER FOR SCALING AND DISPLAY (DEC)

S('FIXLOC', 'erase', 0o120, line=257)  # WORK AREA ADDRESS.
S('OVFIND', 'erase', 0o121, line=258)  # SET NON-ZERO ON OVERFLOW.

S('VBUF', 'erase', 0o122, line=260)  # TEMPORARY STORAGE USED FOR VECTORS.
S('SGNON', 'equals', 0o122, line=261)  # TEMP FOR +,- ON
S('NOUNTEM', 'equals', 0o122, line=262)  # COUNTER FOR MIXNOUN FETCH
S('DISTEM', 'equals', 0o122, line=263)  # COUNTER FOR OCTAL DISPLAY VERB
S('DECTEM', 'equals', 0o122, line=264)  # COUNTER FOR FETCH (DEC DISPLAY VERBS)

S('SGNOFF', 'equals', 0o123, line=266)  # TEMP FOR +,- ON
S('NVTEMP', 'equals', 0o123, line=267)  # TEMP FOR NVSUB
S('SFTEMP1', 'equals', 0o123, line=268)  # STORAGE FOR SF CONST HI PART (=SFTEMP2-1)
S('HITEMIN', 'equals', 0o123, line=269)  # TEMP FOR LOAD OF HRS,MIN,SEC
# MUST = LOTEMIN-1.

S('CODE', 'equals', 0o124, line=272)  # FOR DSPIN
S('SFTEMP2', 'equals', 0o124, line=273)  # STORAGE FOR SF CONST LO PART (=SFTEMP1+1)
S('LOTEMIN', 'equals', 0o124, line=274)  # TEMP FOR LOAD OF HRS,MIN,SEC
# MUST = HITEMIN+1

S('MIXTEMP', 'equals', 0o125, line=277)  # FOR MIXNOUN DATA
S('SIGNRET', 'equals', 0o125, line=278)  # RETURN FOR +,- ON

# ALSO MIXTEMP+1 = VBUF+4, MIXTEMP+2 = VBUF+5

S('BUF', 'erase', 0o130, line=282)  # TEMPORARY SCALAR STORAGE.
# Page 97
S('BUF2', 'erase', 0o133, line=284)
S('INDEXLOC', 'equals', 0o130, line=285)  # CONTAINS ADDRESS OF SPECIFIED INDEX.
S('SWWORD', 'equals', 0o130, line=286)  # ADDRESS OF SWITCH WORD.
S('SWBIT', 'equals', 0o131, line=287)  # SWITCH BIT WITHIN THE SWITCH WORD
S('MPTEMP', 'erase', 0o135, line=288)  # TEMPORARY USED IN MULTIPLY AND SHIFT
S('DMPNTEMP', 'equals', 0o135, line=289)  # DMPSUB TEMPORARY
S('DOTINC', 'erase', 0o136, line=290)  # COMPONENT INCREMENT FOR DOT SUBROUTINE
S('DVSIGN', 'equals', 0o136, line=291)  # DETERMINES SIGN OF DDV RESULT
S('ESCAPE', 'equals', 0o136, line=292)  # USED IN ARCSIN/ARCCOS.
S('ENTRET', 'equals', 0o136, line=293)  # EXIT FROM ENTER

S('DOTRET', 'erase', 0o137, line=295)  # RETURN FROM DOT SUBROUTINE
S('DVNORMCT', 'equals', 0o137, line=296)  # DIVIDENT NORMALIZATION COUNT IN DDV.
S('ESCAPE2', 'equals', 0o137, line=297)  # ALTERNATE ARCSIN/ARCCOS SWITCH
S('WDCNT', 'equals', 0o137, line=298)  # CHAR COUNTER FOR DSPWD
S('INREL', 'equals', 0o137, line=299)  # INPUT BUFFER SELECTION ( X,Y,Z, REG)

S('MATINC', 'erase', 0o140, line=301)  # VECTOR INCREMENT IN MXV AND VXM
S('MAXDVSW', 'equals', 0o140, line=302)  # +0 IF DP QUOTIENT IS NEAR ONE -- ELSE -1.
S('POLYCNT', 'equals', 0o140, line=303)  # POLYNOMIAL LOOP COUNTER
S('DSPMMTEM', 'equals', 0o140, line=304)  # DSPCOUNT SAVE FOR DSPMM
S('MIXBR', 'equals', 0o140, line=305)  # INDICATOR FOR MIXED OR NORMAL NOUN

S('TEM1', 'erase', 0o141, line=307)  # EXEC TEMP
S('POLYRET', 'equals', 0o141, line=308)
S('DSREL', 'equals', 0o141, line=309)  # REL ADDRESS FOR DSPIN

S('TEM2', 'erase', 0o142, line=311)  # EXEC TEMP
S('DSMAG', 'equals', 0o142, line=312)  # MAGNITUDE STORE FOR DSPIN
S('IDADDTEM', 'equals', 0o142, line=313)  # MIXNOUN INDIRECT ADDRESS (garbled)

S('TEM3', 'erase', 0o143, line=315)  # EXEC TEMP
S('COUNT', 'equals', 0o143, line=316)  # FOR DSPIN

S('TEM4', 'erase', 0o144, line=318)  # EXEC TEMP
S('LSTPTR', 'equals', 0o144, line=319)  # LIST POINTER FOR GRABUSY
S('RELRET', 'equals', 0o144, line=320)  # RETURN FOR RELDSP
S('FREERET', 'equals', 0o144, line=321)  # RETURN FOR FREEDSP
S('DSPWDRET', 'equals', 0o144, line=322)  # RETURN FOR DSPSIGN
S('SEPSCRET', 'equals', 0o144, line=323)  # RETURN FOR SEPSEC
S('SEPMNRET', 'equals', 0o144, line=324)  # RETURN FOR SEPMIN

S('TEM5', 'erase', 0o145, line=326)  # EXEC TEMP
S('NOUNADD', 'equals', 0o145, line=327)  # TEMP STORAGE FOR NOUN ADDRESS

S('NNADTEM', 'erase', 0o146, line=329)  # TEMP FOR NOUN ADDRESS TABLE ENTRY
S('NNTYPTEM', 'erase', 0o147, line=330)  # TEMP FOR NOUN TYPE TABLE ENTRY
S('IDAD1TEM', 'erase', 0o150, line=331)  # TEMP FOR INDIR ADDRESS TABLE ENTRY (MIXNN)
# MUST = IDAD2TEM-1, = IDAD3TEM-2
S('IDAD2TEM', 'erase', 0o151, line=333)  # TEMP FOR INDIR ADDRESS TABLE ENTRY (MIXNN)
# Page 98
# MUST = IDAD1TEM+1, = IDAD3TEM-1.
S('IDAD3TEM', 'erase', 0o152, line=336)  # TEMP FOR INDIR ADDRESS TABLE ENTRY (MIXNN)
# MUST = IDAD1TEM+2, = IDAD2TEM+1.
S('RUTMXTEM', 'erase', 0o153, line=338)  # TEMP FOR SF ROUT TABLE ENTRY (MIXNN ONLY)

# AX*SR*T STORAGE.                      (6D)
S('DEXDEX', 'equals', 0o142, line=341)  # B(1)TMP
S('DEX1', 'equals', 0o143, line=342)  # B(1)TMP
S('DEX2', 'equals', 0o144, line=343)  # B(1)TMP
S('RTNSAVER', 'equals', 0o145, line=344)  # B(1)TMP
S('TERM1TMP', 'equals', 0o157, line=345)  # B(2)TMP

S('DEXI', 'equals', 0o143, line=347)

# THE FOLLOWING 10 REGISTERS ARE USED FOR TEMPORARY STORAGE OF THE DERIVATIVE COEFFICIENT TABLE OF
# SUBROUTINE ROOTPSRS.  THEY MUST REMAIN WITHOUT INTERFERENCE WITH ITS SUBROUTINES WHICH ARE POWRSERS (POLY).
# DMPSUB, DMPNSUB, SHORTMP, DDV/BDDV, ABS, AND USPRCADR.

S('DERCOF-8', 'equals', 0o142, line=353)  # ROOTPSRS DER COF N-4 HI ORDER
S('DERCOF-7', 'equals', 0o143, line=354)  # ROOTPSRS DER COF N-4 LO ORDER
S('DERCOF-6', 'equals', 0o144, line=355)  # ROOTPSRS DER COF N-3 HI ORDER
S('DERCOF-5', 'equals', 0o145, line=356)  # ROOTPSRS DER COF N-3 LO ORDER
S('DERCOF-4', 'equals', 0o146, line=357)  # ROOTPSRS DER COF N-2 HI ORDER
S('DERCOF-3', 'equals', 0o147, line=358)  # ROOTPSRS DER COF N-2 LO ORDER
S('DERCOF-2', 'equals', 0o150, line=359)  # ROOTPSRS DER COF N-1 HI ORDER
S('DERCOF-1', 'equals', 0o151, line=360)  # ROOTPSRS DER COF N-1 LO ORDER
S('DERCOFN', 'equals', 0o152, line=361)  # ROOTPSRS DER COF N, HI ORDER
S('DERCOF+1', 'equals', 0o153, line=362)  # ROOTPSRS DER COF N, LO ORDER

S('PWRPTR', 'equals', 0o117, line=364)  # ROOTPSRS POWER TABLE POINTER
S('DXCRIT', 'equals', 0o124, line=365)  # ROOTPSRS CRITERION FOR ENDING ITERS HI
S('DXCRIT+1', 'equals', 0o125, line=366)  # ROOTPSRS CRITERION FOR ENDING ITERS LOW
S('ROOTPS', 'equals', 0o126, line=367)  # ROOTPSRS ROOT HI ORDER
S('ROOTPS+1', 'equals', 0o127, line=368)  # ROOTPSRS ROOT LO ORDER
S('RETROOT', 'equals', 0o132, line=369)  # ROOTPSRS RETURN ADDRESS OF USER
S('PWRCNT', 'equals', 0o140, line=370)  # ROOTPSRS DER TABLE LOOP COUNTER
S('DERPTR', 'equals', 0o141, line=371)  # ROOTPSRS DER TABLE POINTER

# Page 99
# DYNAMICALLY ALLOCATED CORE SETS FOR JOBS      (84D)

S('MPAC', 'erase', 0o154, line=376)  # MULTI-PURPOSE ACCUMULATOR.
S('MODE', 'erase', 0o163, line=377)  # +1 FOR TP, +0 FOR DP, OR -1 FOR VECTOR.
S('LOC', 'erase', 0o164, line=378)  # LOCATION ASSOCIATED WITH JOB.
S('BANKSET', 'erase', 0o165, line=379)  # USUALLY CONTAINS BBANK SETTING.
S('PUSHLOC', 'erase', 0o166, line=380)  # WORD OF PACKED INTERPRETIVE PARAMETERS.
S('PRIORITY', 'erase', 0o167, line=381)  # PRIORITY OF PRESENT JOB AND WORK AREA.

#   ERASE +83D  # EIGHT SETS OF 12 REGISTERS EACH

# INCORP STORAGE:  R22 (N29)    (SHARES WITH FOLLOWING SECTION)         (4D)

S('R22DISP', 'equals', 0o314, line=387)  # I(4) N49 DISPLAY OF DELTA R AND DELTA V

# STANDBY VERB ERASABLES.  REDOCTR BEFORE THETADS.      (14D)

S('TIME2SAV', 'erase', 0o314, line=391)
S('SCALSAVE', 'erase', 0o316, line=392)
S('REDOCTR', 'erase', 0o320, line=393)  # CONTAINS NUMBER OF RESTARTS
S('THETAD', 'erase', 0o321, line=394)
S('CPHI', 'equals', 0o321, line=395)  # O     DESIRED GIMBAL ANGLES
S('CTHETA', 'equals', 0o322, line=396)  # I     FOR
S('CPSI', 'equals', 0o323, line=397)  # M     MANEUVER
S('DELV', 'erase', 0o324, line=398)
S('DELVX', 'equals', 0o324, line=399)
S('DELVY', 'equals', 0o326, line=400)
S('DELVZ', 'equals', 0o330, line=401)

# DOWNLINK STORAGE.                     (28D)

S('DNLSTADR', 'equals', 0o332, line=406)

S('DNLSTCOD', 'erase', 0o332, line=408)  # B(1)PRM DOWNLINK LIST CODE
S('DUMPCNT', 'erase', 0o333, line=409)  # B(1)
S('LDATALST', 'erase', 0o334, line=410)  # (26D)
S('DNTMGOTO', 'equals', 0o335, line=411)  # B(1)
S('TMINDEX', 'equals', 0o336, line=412)  # B(1)
S('DUMPLOC', 'equals', 0o336, line=413)  # CONTAINS ECADR OF AGC DP WORD BEING DUMPED
# AND COUNT OF COMPLETE DUMPS ALREADY
# SENT.
S('DNQ', 'equals', 0o337, line=416)  # B(1)
S('DNTMBUFF', 'equals', 0o340, line=417)  # B(22)PRM DOWNLINK SNAPSHOT BUFFER

# UNSWITCHED FOR DISPLAY INTERFACE ROUTINES.    (10D) FIVE MORE IN EBANK 2.

# Page 100
S('RESTREG', 'erase', 0o366, line=422)  # B(1)PRM FOR DISPLAY RESTARTS
S('NVWORD', 'erase', 0o367, line=423)
S('MARKNV', 'erase', 0o370, line=424)
S('NVSAVE', 'erase', 0o371, line=425)
# (RETAIN THE ORDER OF CADRFLSH TO FAILREG +2 FOR DOWNLINK PURPOSES)
S('CADRFLSH', 'erase', 0o372, line=427)
S('CADRMARK', 'erase', 0o373, line=428)
S('TEMPFLSH', 'erase', 0o374, line=429)
S('FAILREG', 'erase', 0o375, line=430)  # B(3)PRM 3 ALARM CODE REGISTERS

# VAC AREAS. -- BE CAREFUL OF PLACEMENT --      (220D)

S('VAC1USE', 'erase', 0o400, line=434)
S('VAC1', 'erase', 0o401, line=435)
S('VAC2USE', 'erase', 0o454, line=436)
S('VAC2', 'erase', 0o455, line=437)
S('VAC3USE', 'erase', 0o530, line=438)
S('VAC3', 'erase', 0o531, line=439)
S('VAC4USE', 'erase', 0o604, line=440)
S('VAC4', 'erase', 0o605, line=441)
S('VAC5USE', 'erase', 0o660, line=442)
S('VAC5', 'erase', 0o661, line=443)

# WAITLIST REPEAT FLAG.                 (1D)
S('RUPTAGN', 'erase', 0o734, line=446)
S('KEYTEMP2', 'equals', 0o734, line=447)  # TEMP FOR KEYRUPT, UPRUPT

# STARALIGN ERASABLES.                  (13D)

S('STARCODE', 'erase', 0o735, line=451)  # (1)
S('AOTCODE', 'equals', 0o735, line=452)
S('STARALGN', 'erase', 0o736, line=453)
S('SINCDU', 'equals', 0o736, line=454)
S('COSCDU', 'equals', 0o744, line=455)

S('SINCDUX', 'equals', 0o742, line=457)
S('SINCDUY', 'equals', 0o736, line=458)
S('SINCDUZ', 'equals', 0o740, line=459)
S('COSCDUX', 'equals', 0o750, line=460)
S('COSCDUY', 'equals', 0o744, line=461)
S('COSCDUZ', 'equals', 0o746, line=462)

# PHASE TABLE AND RESTART COUNTERS              (12D)

S('-PHASE1', 'erase', 0o752, line=466)

# Page 101
S('PHASE1', 'erase', 0o753, line=469)
S('-PHASE2', 'erase', 0o754, line=470)
S('PHASE2', 'erase', 0o755, line=471)
S('-PHASE3', 'erase', 0o756, line=472)
S('PHASE3', 'erase', 0o757, line=473)
S('-PHASE4', 'erase', 0o760, line=474)
S('PHASE4', 'erase', 0o761, line=475)
S('-PHASE5', 'erase', 0o762, line=476)
S('PHASE5', 'erase', 0o763, line=477)
S('-PHASE6', 'erase', 0o764, line=478)
S('PHASE6', 'erase', 0o765, line=479)

# A**SR*T STORAGE.                      (6D)

S('CDUSPOT', 'erase', 0o766, line=483)  # B(6)

S('CDUSPOTY', 'equals', 0o766, line=485)
S('CDUSPOTZ', 'equals', 0o770, line=486)
S('CDUSPOTX', 'equals', 0o772, line=487)

# VERB 37 STORAGE                       (2D)

S('MINDEX', 'erase', 0o774, line=491)  # B(1)TMP INDEX FOR MAJOR MODE
S('MMNUMBER', 'erase', 0o775, line=492)  # B(1)TMP MAJOR MODE REQUESTED BY V37

# PINBALL INTERRUPT ACTION              (1D)

S('DSPCNT', 'erase', 0o776, line=496)  # B(1)PRM COUNTER FOR DSPOUT

# PINBALL EXECUTIVE ACTION              (44D)

S('DSPCOUNT', 'erase', 0o777, line=500)  # DISPLAY POSITION INDICATOR
S('DECBRNCH', 'erase', 0o1000, line=501)  # +DEC, -DEC, OCT INDICATOR
S('VERBREG', 'erase', 0o1001, line=502)  # VERB CODE
S('NOUNREG', 'erase', 0o1002, line=503)  # NOUN CODE
S('XREG', 'erase', 0o1003, line=504)  # R1 INPUT BUFFER
S('YREG', 'erase', 0o1004, line=505)  # R2 INPUT BUFFER
S('ZREG', 'erase', 0o1005, line=506)  # R3 INPUT BUFFER
S('XREGLP', 'erase', 0o1006, line=507)  # LO PART OF XREG (FOR DEC CONV ONLY)
S('YREGLP', 'erase', 0o1007, line=508)  # LO PART OF YREG (FOR DEC CONV ONLY)
S('HITEMOUT', 'equals', 0o1007, line=509)  # TEMP FOR DISPLAY OF HRS,MIN,SEC
# MUST = LOTEMOUT-1.
S('ZREGLP', 'erase', 0o1010, line=511)  # LO PART OF ZREG (FOR DEC CONV ONLY)
S('LOTEMOUT', 'equals', 0o1010, line=512)  # TEMP FOR DISPLAY OF HRS,MIN,SEC
# MUST = HITEMOUT+1
S('MODREG', 'erase', 0o1011, line=514)  # MODE CODE

# Page 102
S('DSPLOCK', 'erase', 0o1012, line=517)  # KEYBOARD/SUBROUTINE CALL INTERLOCK
S('REQRET', 'erase', 0o1013, line=518)  # RETURN REGISTER FOR LOAD
S('LOADSTAT', 'erase', 0o1014, line=519)  # STATUS INDICATOR FOR LOADTST
S('CLPASS', 'erase', 0o1015, line=520)  # PASS INDICATOR CLEAR
S('NOUT', 'erase', 0o1016, line=521)  # ACTIVITY COUNTER FOR DSPTAB
S('NOUNCADR', 'erase', 0o1017, line=522)  # MACHINE CADR FOR NOUN
S('MONSAVE', 'erase', 0o1020, line=523)  # N/V CODE FOR MONITOR. (= MONSAVE1-1)
S('MONSAVE1', 'erase', 0o1021, line=524)  # NOUNCADR FOR MONITOR (MATBS1) = MONSAVE+1
S('MONSAVE2', 'erase', 0o1022, line=525)  # NVMONOPT OPTIONS
S('DSPTAB', 'erase', 0o1023, line=526)  # 0-10D, DISPLAY PANEL BUFF.  11D, C/S LTS.
S('NVQTEM', 'erase', 0o1037, line=527)  # NVSUB STORAGE FOR CALLING ADDRESS
# MUST = NVBNKTEM-1.
S('NVBNKTEM', 'erase', 0o1040, line=529)  # NVSUB STORAGE FOR CALLING BANK
# MUST = NVQTEM+1
S('VERBSAVE', 'erase', 0o1041, line=531)  # NEEDED FOR RECYCLE
S('CADRSTOR', 'erase', 0o1042, line=532)  # ENDIDLE STORAGE
S('DSPLIST', 'erase', 0o1043, line=533)  # WAITING REG FOR DSP SYST INTERNAL USE
S('EXTVBACT', 'erase', 0o1044, line=534)  # EXTENDED VERB ACTIVITY INTERLOCK
S('DSPTEM1', 'erase', 0o1045, line=535)  # BUFFER STORAGE AREA 1 (MOSTLY FOR TIME)
S('DSPTEM2', 'erase', 0o1050, line=536)  # BUFFER STORAGE AREA 2 (MOSTLY FOR DEG)

S('DSPTEMX', 'equals', 0o1051, line=538)  # B(2) S-S DISPLAY BUFFER FOR EXT. VERBS
S('NORMTEM1', 'equals', 0o1045, line=539)  # B(3)DSP NORMAL DISPLAY REGISTERS.

# DISPLAY FOR EXTENDED VERBS (V82, R04(V62), V41(N72) ) (2D)

S('OPTIONX', 'equals', 0o1051, line=543)  # (2) EXTENDED VERB OPTION CODE

# TBASES AND PHSPRDT S.                 (12D)

S('TBASE1', 'erase', 0o1053, line=547)
S('PHSPRDT1', 'erase', 0o1054, line=548)
S('TBASE2', 'erase', 0o1055, line=549)
S('PHSPRDT2', 'erase', 0o1056, line=550)
S('TBASE3', 'erase', 0o1057, line=551)
S('PHSPRDT3', 'erase', 0o1060, line=552)
S('TBASE4', 'erase', 0o1061, line=553)
S('PHSPRDT4', 'erase', 0o1062, line=554)
S('TBASE5', 'erase', 0o1063, line=555)
S('PHSPRDT5', 'erase', 0o1064, line=556)
S('TBASE6', 'erase', 0o1065, line=557)
S('PHSPRDT6', 'erase', 0o1066, line=558)

# UNSWITCHED FOR DISPLAY INTERFACE ROUTINES.    (6D)

# Page 103
S('NVWORD1', 'erase', 0o1067, line=563)  # B(1) PROBABLY FOR DISPLAY DURING SERVICER
S('EBANKSAV', 'erase', 0o1070, line=564)
S('MARKEBAN', 'erase', 0o1071, line=565)
S('EBANKTEM', 'erase', 0o1072, line=566)
S('MARK2PAC', 'erase', 0o1073, line=567)
S('R1SAVE', 'erase', 0o1074, line=568)

# IMU COMPENSATION UNSWITCHED ERASABLE.         (1D)

S('1/PIPADT', 'erase', 0o1075, line=572)

# SINGLE PRECISION SUBROUTINE TEMPORARIES       (2D)

S('TEMK', 'erase', 0o1076, line=576)  # (1)
S('SQ', 'erase', 0o1077, line=577)  # (1)

# UNSWITCHED RADAR ERASABLE

S('SAMPLIM', 'erase', 0o1100, line=581)
S('SAMPLSUM', 'erase', 0o1101, line=582)
S('TIMEHOLD', 'erase', 0o1105, line=583)
S('RRTARGET', 'equals', 0o1101, line=584)  # HALF U IT VECTOR IN SM OR NB AXES.
S('TANG', 'erase', 0o1107, line=585)  # DESIRE TRUNNION AND SHAFT ANGLES.
S('MODEA', 'equals', 0o1107, line=586)
S('MODEB', 'erase', 0o1111, line=587)  # DODES LOBBERS TANG +2.
S('NSAMP', 'equals', 0o1111, line=588)
S('DESRET', 'erase', 0o1113, line=589)
S('OLDATAGD', 'equals', 0o1113, line=590)  # USED IN DATA READING ROUTINES.
S('DESCOUNT', 'erase', 0o1114, line=591)

# ******   P22  ******                          (6D)

S('RSUBC', 'equals', 0o1101, line=595)  # I(6) S-S CSM POSITION VECTOR.

# Page 104
# UNSWITCHED FOR ORBIT INTEGRATION              (21D)

S('TDEC', 'erase', 0o1115, line=600)  # I(2)
S('COLREG', 'equals', 0o1117, line=601)  # I(1)
S('LAT', 'equals', 0o1120, line=602)  # I(2)
S('LONG', 'equals', 0o1122, line=603)  # I(2)
S('ALT', 'equals', 0o1124, line=604)  # I(2)
S('YV', 'equals', 0o1126, line=605)  # I(6)
S('ZV', 'equals', 0o1134, line=606)  # I(6)

# MISCELLANEOUS UNSWITCHED.                     (20D)

S('P40/RET', 'erase', 0o1142, line=610)  # (WILL BE PUT IN E6 WHEN THERE IS ROOM)
S('GENRET', 'erase', 0o1143, line=611)  # B(1) R61 RETURN CADR.
S('OPTION1', 'erase', 0o1144, line=612)  # B(1) NOUN 06 USES THIS
S('OPTION2', 'erase', 0o1145, line=613)  # B(1) NOUN 06 USES THIS
S('OPTION3', 'erase', 0o1146, line=614)  # B(1) NOUN 06 USES THIS
S('LONGCADR', 'erase', 0o1147, line=615)  # B(2) LONGCALL REGISTER
S('LONGBASE', 'erase', 0o1151, line=616)
S('LONGTIME', 'erase', 0o1153, line=617)  # B(2) LONGCALL REGISTER
S('CDUTEMPX', 'erase', 0o1155, line=618)  # B(1)TMP
S('CDUTEMPY', 'erase', 0o1156, line=619)  # B(1)TMP
S('CDUTEMPZ', 'erase', 0o1157, line=620)  # B(1)TMP
S('PIPATMPX', 'erase', 0o1160, line=621)  # B(1)TMP
S('PIPATMPY', 'erase', 0o1161, line=622)  # B(1)TMP
S('PIPATMPZ', 'erase', 0o1162, line=623)  # B(1)TMP

S('DISPDEX', 'erase', 0o1163, line=625)  # B(1)
S('TEMPR60', 'erase', 0o1164, line=626)  # B(1)
S('PRIOTIME', 'erase', 0o1165, line=627)  # B(1)

# P27 (UPDATE PROGRAM) STORAGE                  (26D)

S('UPVERBSV', 'erase', 0o1166, line=631)  # B(1) UPDATE VERB ATTEMPTED.
S('UPTEMP', 'erase', 0o1167, line=632)  # B(1)TMP SCRATCH
S('INTWAK1Q', 'equals', 0o1167, line=633)  # (BORROWS UPTEMP REGISTERS)
# RETAIN THE ORDER OF COMPNUMB THRU UPBUFF +19D FOR DOWNLINK PURPOSES.
S('COMPNUMB', 'equals', 0o1170, line=635)  # B(1)TMP NUMBER OF ITEMS TO BE UPLINKED
S('UPOLDMOD', 'equals', 0o1171, line=636)  # B(1)TMP INTERRUPTD PROGRAM MM
S('UPVERB', 'equals', 0o1172, line=637)  # B(1)TMP VERB NUMBER
S('UPCOUNT', 'equals', 0o1173, line=638)  # B(1)TMP UPBUFF INDEX
S('UPBUFF', 'equals', 0o1174, line=639)  # B(20D)

# SPECIAL DEFINITION FOR SYSTEM TEST ERASABLE PGMS.     (2D)

S('EBUF2', 'equals', 0o1167, line=643)  # B(2) FOR EXCLUSIVE USE OF SYSTEM TEST.

# Page 105
# PERM STATE VECTORS FOR BOOST AND DOWNLINK -- WHOLE MISSION -- (14D)

S('RN', 'erase', 0o1220, line=648)  # B(6)PRM
S('VN', 'erase', 0o1226, line=649)  # B(6)PRM
S('PIPTIME', 'erase', 0o1234, line=650)  # B(2)PRM (MUST BE FOLLOWED BY GDT/2)

# SERVICER -- MUST FOLLOW PIPTIME --            (19D)

S('GDT/2', 'erase', 0o1236, line=654)  # B(6)TMP       ** MUST FOLLOW PIPTIME **
S('MASS', 'equals', 0o1244, line=655)  # B(2)
S('WEIGHT/G', 'equals', 0o1244, line=656)
S('ABDELV', 'equals', 0o1246, line=657)  # (KALCMANU STORAGE)
S('PGUIDE', 'equals', 0o1247, line=658)  # (2)
S('DVTHRUSH', 'equals', 0o1251, line=659)  # (1)
S('AVEGEXIT', 'equals', 0o1252, line=660)  # (2)
S('AVGEXIT', 'equals', 0o1252, line=661)
S('TEMX', 'equals', 0o1254, line=662)  # (1)
S('TEMY', 'equals', 0o1255, line=663)  # (1)
S('TEMZ', 'equals', 0o1256, line=664)  # (1)
S('PIPAGE', 'equals', 0o1257, line=665)  # B(1)
S('OUTROUTE', 'equals', 0o1260, line=666)  # B(1)

# PERMANENT LEM DAP STORAGE             (12D)

S('CH5MASK', 'erase', 0o1262, line=670)  # B(1)PRM
S('CH6MASK', 'erase', 0o1263, line=671)  # B(1)PRM JET FAILURE MASK.
S('DTHETASM', 'erase', 0o1264, line=672)  #  (6)
S('SPNDX', 'erase', 0o1272, line=673)  # B(1)
S('RCSFLAGS', 'erase', 0o1273, line=674)  # AUTOPILOT FLAG WORD
# BIT ASSIGNMENTS:
# 1) ALTERYZ SWITCH (ZEROOR1)
# 2) NEEDLER SWITCH
# 3) NEEDLER SWITCH
# 4) NEEDLER SWITCH
# 5) NEEDLER SWITCH
# 9) JUST-IN-DETENT SWITCH
# 10) PBIT -- MANUAL CONTROL SWITCH
# 11) QRBIT -- MANUAL CONTROL SWITCH
# 12) PSKIP CONTROL (PJUMPADR)
# 13) 1/ACCJOB CONTROL (ACCSET)
S('T5ADR', 'erase', 0o1274, line=686)  # GENADR OF NEXT LM DAP T5RUPT. * 2CADR *
# BBCON  OF NEXT LM DAP T5RUPT.   2CADR

# ERASABLES FOR P64:  OVERLAY OF DTHETASM, WHICH IS UNUSED      (4D)
S('ZERLINA', 'equals', 0o1264, line=690)  # B(1)  P64

# Page 106
S('ELVIRA', 'equals', 0o1265, line=693)  # B(1)  P64
S('AZINCR1', 'equals', 0o1266, line=694)  # B(1)  P64
S('ELINCR1', 'equals', 0o1267, line=695)  # B(1)  P64

# RCS FAILURE MONITOR STORAGE           (1)

S('PVALVEST', 'erase', 0o1276, line=699)  # B(1)PRM

# KALCMANU/DAP INTERFACE                        (3D)

S('DELPEROR', 'erase', 0o1277, line=703)  # B(1)PRM COMMAND LAGS.
S('DELQEROR', 'erase', 0o1300, line=704)  # B(1)PRM
S('DELREROR', 'erase', 0o1301, line=705)  # B(1)PRM

# MODE SWITCHING ERASABLE.                      (9D)

# RETAIN THE ORDER OF IMODES30 AND IMODES33 FOR DOWNLINK PURPOSES
S('IMODES30', 'erase', 0o1302, line=710)  # B(1)
S('IMODES33', 'erase', 0o1303, line=711)
S('MODECADR', 'erase', 0o1304, line=712)  # B(3)PRM
S('IMUCADR', 'equals', 0o1304, line=713)
S('OPTCADR', 'equals', 0o1305, line=714)
S('RADCADR', 'equals', 0o1306, line=715)
S('ATTCADR', 'erase', 0o1307, line=716)  # B(3)PRM
S('ATTPRIO', 'equals', 0o1311, line=717)
S('MARKSTAT', 'erase', 0o1312, line=718)

# T4RUPT ERASABLE                               (2D)

S('DSRUPTSW', 'erase', 0o1313, line=722)
S('LGYRO', 'erase', 0o1314, line=723)  # (1)

# RENDEZVOUS RADAR TASK STORAGE                 (3D)

S('RRRET', 'erase', 0o1315, line=727)  # B(1)TMP       P20'S, PERHAPS R29 & R12
S('RDES', 'equals', 0o1316, line=728)  # B(1)TMP
S('RRINDEX', 'equals', 0o1317, line=729)  # B(1)TMP

# MEASINC                                       (4D)

S('WIXA', 'erase', 0o1320, line=733)  # B(1)
S('WIXB', 'erase', 0o1321, line=734)  # B(1)
S('ZIXA', 'erase', 0o1322, line=735)  # B(1)
S('ZIXB', 'erase', 0o1323, line=736)  # B(1)

# Page 107

# AGS DUMMY ID WORD.                            (1D)

S('AGSWORD', 'erase', 0o1324, line=742)

# SOME MISCELLANEOUS UNSWITCHED.                (6D)

S('RATEINDX', 'erase', 0o1325, line=746)  # (1) USED BY KALCMANU
S('DELAYLOC', 'erase', 0o1326, line=747)
S('LEMMASS', 'erase', 0o1331, line=748)  # KEEP CONTIGUOUS W. CSMMASS. (1) EACH
S('CSMMASS', 'erase', 0o1332, line=749)

# LESS IS MORE.

# RENDEZVOUS AND LANDING RADAR DOWNLINK STORAGE.        (7D)
#
# (NORMALLY USED DURING P20, BUT MAY ALSO)
# (BE REQUIRED FOR THE V62 SPURIOUS TEST.)
#
# (PLEASE KEEP IN THIS ORDER)

S('DNRRANGE', 'erase', 0o1333, line=760)  # B(1)TMP
S('DNRRDOT', 'equals', 0o1334, line=761)  # B(1)TMP
S('DNINDEX', 'equals', 0o1335, line=762)  # B(1)TMP
S('DNLRVELX', 'equals', 0o1336, line=763)  # B(1)TMP
S('DNLRVELY', 'equals', 0o1337, line=764)  # B(1)TMP
S('DNLRVELZ', 'equals', 0o1340, line=765)  # B(1)TMP
S('DNLRALT', 'equals', 0o1341, line=766)  # B(1)TMP

# INCORPORATION UNSWITCHED                      (2D)

S('W.IND', 'equals', 0o1257, line=770)  # B(1)
S('W.INDI', 'equals', 0o1260, line=771)  # I(1)

# SUBROUTINE BALLANGS OF R60.

S('BALLEXIT', 'erase', 0o1342, line=775)  # B(1) SAVE LOCATION FOR BALLINGS SUBR EXIT

# SOME LEM DAP STORAGE.                         (4D)

S('DAPDATR1', 'erase', 0o1343, line=779)  # B(1)DSP DAP CONFIG.
S('TEVENT', 'erase', 0o1344, line=780)  # B(2)DSP
S('DB', 'erase', 0o1346, line=781)  # B(1)TMP DEAD BAND.

# NOUN 87                                       (2D)
S('AZ', 'erase', 0o1347, line=784)  # B(1) AZ AND EL MUST BE CONTIGUOUS

# Page 108
S('EL', 'equals', 0o1350, line=787)  # B(1)

# P63, P64, P65, P66, AND P67.                  (1D)

S('WCHPHASE', 'erase', 0o1351, line=791)  # B(1)

# ERASABLES FOR THE R2 LUNAR POTENTIAL MODEL    (2D)

S('E3J22R2M', 'erase', 0o1352, line=795)  # I(1)
S('E32C31RM', 'erase', 0o1353, line=796)  # I(1)

S('RADSKAL', 'erase', 0o1354, line=799)  # LR ALT DOPPLER BIAS: 2T/LAMBDA SCALED
# AT 1/(2(7) M/CS)
S('SKALSKAL', 'erase', 0o1356, line=801)  # LR ALT SCALE FACTOR RATIO: .2 NOM

S('END-UE', 'equals', 0o1357, line=803)  # NEXT UNUSED UE ADDRESS

# SELF-CHECK ASSIGNMENTS                        (17D)

S('SELFERAS', 'erase', 0o1357, line=807)  # *** MUST NOT BE MOVED ***
S('SFAIL', 'equals', 0o1357, line=808)  # B(1)
S('ERESTORE', 'equals', 0o1360, line=809)  # B(1)
S('SELFRET', 'equals', 0o1361, line=810)  # B(1) RETURN
S('SMODE', 'equals', 0o1362, line=811)  # B(1)
S('ALMCADR', 'equals', 0o1363, line=812)  # B(2) ALARM-ABORT USER'S 2CADR
S('ERCOUNT', 'equals', 0o1365, line=813)  # B(1)
S('SCOUNT', 'equals', 0o1366, line=814)  # B(3)
S('SKEEP1', 'equals', 0o1371, line=815)  # B(1)
S('SKEEP2', 'equals', 0o1372, line=816)  # B(1)
S('SKEEP3', 'equals', 0o1373, line=817)  # B(1)
S('SKEEP4', 'equals', 0o1374, line=818)  # B(1)
S('SKEEP5', 'equals', 0o1375, line=819)  # B(1)
S('SKEEP6', 'equals', 0o1376, line=820)  # B(1)
S('SKEEP7', 'equals', 0o1377, line=821)  # B(1)
# Page 109
# EBANK-3 ASSIGNMENTS

#   SETLOC 1400

# WAITLIST TASK LISTS.                          (26D)

S('LST1', 'erase', 0o1400, line=829)  # B(8D)PRM DELTA T'S.
S('LST2', 'erase', 0o1410, line=830)  # B(18D)PRM TASK 2CADR ADDRESSES.

# RESTART STORAGE.                              (2D)

S('RSBBQ', 'erase', 0o1432, line=834)  # B(2)PRM SAVE BB AND Q FOR RESTARTS

# MORE LONGCALL STORAGE.  (MUST BE IN LST1'S BANK.      (2D)

S('LONGEXIT', 'erase', 0o1434, line=838)  # B(2)TMP MAY BE SELDOM OVERLAYED.

# PHASE-CHANGE LISTS PART II.                   (12D)

S('PHSNAME1', 'erase', 0o1436, line=843)  # B(1)PRM
S('PHSBB1', 'erase', 0o1437, line=844)  # B(1)PRM
S('PHSNAME2', 'erase', 0o1440, line=845)  # B(1)PRM
S('PHSBB2', 'erase', 0o1441, line=846)  # B(1)PRM
S('PHSNAME3', 'erase', 0o1442, line=847)  # B(1)PRM
S('PHSBB3', 'erase', 0o1443, line=848)  # B(1)PRM
S('PHSNAME4', 'erase', 0o1444, line=849)  # B(1)PRM
S('PHSBB4', 'erase', 0o1445, line=850)  # B(1)PRM
S('PHSNAME5', 'erase', 0o1446, line=851)  # B(1)PRM
S('PHSBB5', 'erase', 0o1447, line=852)  # B(1)PRM
S('PHSNAME6', 'erase', 0o1450, line=853)  # B(1)PRM
S('PHSBB6', 'erase', 0o1451, line=854)  # B(1)PRM

# IMU COMPENSATION PARAMETERS                   (22D)

S('PBIASX', 'erase', 0o1452, line=858)  # B(1) PIPA BIAS, PIPA SCALE FACTOR TERMS
S('PIPABIAS', 'equals', 0o1452, line=859)  # INTERMIXED.
S('PIPASCFX', 'erase', 0o1453, line=860)
S('PIPASCF', 'equals', 0o1453, line=861)
S('PBIASY', 'erase', 0o1454, line=862)
S('PIPASCFY', 'erase', 0o1455, line=863)
S('PBIASZ', 'erase', 0o1456, line=864)
S('PIPASCFZ', 'erase', 0o1457, line=865)

S('NBDX', 'erase', 0o1460, line=867)  # GYRO BIAS DRIFT
S('NBDY', 'erase', 0o1461, line=868)
S('NBDZ', 'erase', 0o1462, line=869)
# Page 110
S('ADIAX', 'erase', 0o1463, line=871)  # ACCELERATION SENSITIVE DRIFT ALONG THE
S('ADIAY', 'erase', 0o1464, line=872)  # INPUT AXIS
S('ADIAZ', 'erase', 0o1465, line=873)

S('ADSRAX', 'erase', 0o1466, line=875)  # ACCELERATION SENSITIVE DRIFT ALONG THE
S('ADSRAY', 'erase', 0o1467, line=876)  # SPIN REFERENCE AXIS
S('ADSRAZ', 'erase', 0o1470, line=877)

S('GCOMP', 'erase', 0o1471, line=879)  # CONTAINS COMPENSATING TORQUES

S('COMMAND', 'equals', 0o1471, line=881)
S('CDUIND', 'equals', 0o1474, line=882)

S('GCOMPSW', 'erase', 0o1477, line=884)

# STATE VECTORS FOR ORBIT INTEGRATION.          (44D)

# (DIFEQCNT THUR XKEP MUST BE IN THE SAME
# EBANK AS RRECTCSM, RRECTLEM ETC
# BECAUSE THE COPY-CYCLES (ATOPCSM,
# PTOACSM ETC) ARE EXECUTED IN BASIC.
# ALL OTHER REFERENCES TO THIS GROUP
# ARE BY INTERPRETIVE INSTRUCTIONS.)
#

S('DIFEQCNT', 'erase', 0o1500, line=896)  # B(1)
# (UPSVFLAG...XKEP MUST BE KEPT IN ORDER)

S('UPSVFLAG', 'equals', 0o1501, line=899)  # B(1)
S('RRECT', 'equals', 0o1502, line=900)  # B(6)
S('VRECT', 'equals', 0o1510, line=901)  # B(6)
S('TET', 'equals', 0o1516, line=902)  # B(2)
S('TDELTAV', 'equals', 0o1520, line=903)  # B(6)
S('TNUV', 'equals', 0o1526, line=904)  # B(6)
S('RCV', 'equals', 0o1534, line=905)  # B(6)
S('VCV', 'equals', 0o1542, line=906)  # B(6)
S('TC', 'equals', 0o1550, line=907)  # B(2)
S('XKEP', 'equals', 0o1552, line=908)  # B(2)

# PERMANENT STATE VECTORS AND TIMES.

# (DO NOT OVERLAY WITH ANYTHING AFTER BOOST)

# (RRECTCSM...XKEPCSM MUST BE KEPT IN THIS ORDER)

S('RRECTCSM', 'erase', 0o1554, line=916)  # B(6)PRM CSM VARIABLES.
S('RRECTOTH', 'equals', 0o1554, line=917)
S('VRECTCSM', 'erase', 0o1562, line=918)  # B(6)PRM
# Page 111
S('TETCSM', 'erase', 0o1570, line=920)  # B(2)PRM
S('TETOTHER', 'equals', 0o1570, line=921)
S('DELTACSM', 'erase', 0o1572, line=922)  # B(6)PRM
S('NUVCSM', 'erase', 0o1600, line=923)  # B(6)PRM
S('RCVCSM', 'erase', 0o1606, line=924)  # B(6)PRM
S('VCVCSM', 'erase', 0o1614, line=925)  # B(6)PRM
S('TCCSM', 'erase', 0o1622, line=926)  # B(2)PRM
S('XKEPCSM', 'erase', 0o1624, line=927)  # B(2)PRM

# (RRECTLEM...XKEPLEM MUST BE KEPT IN THIS ORDER)

S('RRECTLEM', 'erase', 0o1626, line=931)  # B(6)PRM LEM VARIABLES
S('RRECTHIS', 'equals', 0o1626, line=932)
S('VRECTLEM', 'erase', 0o1634, line=933)  # B(6)PRM
S('TETLEM', 'erase', 0o1642, line=934)  # B(2)PRM
S('TETTHIS', 'equals', 0o1642, line=935)
S('DELTALEM', 'erase', 0o1644, line=936)  # B(6)PRM
S('NUVLEM', 'erase', 0o1652, line=937)  # B(6)PRM
S('RCVLEM', 'erase', 0o1660, line=938)  # B(6)PRM
S('VCVLEM', 'erase', 0o1666, line=939)  # B(6)PRM
S('TCLEM', 'erase', 0o1674, line=940)  # B(2)PRM
S('XKEPLEM', 'erase', 0o1676, line=941)  # B(2)PRM

S('X789', 'erase', 0o1700, line=943)
S('TEPHEM', 'erase', 0o1706, line=944)
S('AZO', 'erase', 0o1711, line=945)
S('-AYO', 'erase', 0o1713, line=946)
S('AXO', 'erase', 0o1715, line=947)

# STATE VECTORS FOR DOWNLINK                    (12D)

S('R-OTHER', 'erase', 0o1717, line=951)  # B(6)PRM POS VECT (OTHER VECH) FOR DNLINK
S('V-OTHER', 'erase', 0o1725, line=952)  # B(6)PRM VEL VECT (OTHER VECH) FOR DNLINK

S('T-OTHER', 'equals', 0o1570, line=954)  #             TIME (OTHER VECH) FOR DNLINK

# REFSMMAT.                                     (18D)

S('REFSMMAT', 'erase', 0o1733, line=958)  # I(18D)PRM

# ACTIVE VEHICLE CENTANG.  MUST BE DISPLAYED ANYTIME (ALMOST.)  (2D)

S('ACTCENT', 'erase', 0o1755, line=962)  # I(2) S-S CENTRAL ANGLE BETWEEN ACTIVE
# VEHICLE AT TPI TIG AND TARGET VECTOR.

# **** USED IN CONICSEX (PLAN INERT ORIENT) ****
# Page 112
S('TIMSUBO', 'equals', 0o1706, line=967)  # CSEC B-42 (TRIPLE PRECISION)

# LPS20.1 STORAGE       -- ALL ARE PRM --       (9D)

S('LS21X', 'erase', 0o1757, line=971)  # I(1)
S('LOSVEL', 'erase', 0o1760, line=972)  # I(6)
S('MLOSV', 'erase', 0o1766, line=973)  # I(2) MAGNITUDE OF LOS. METERS B-29

# ***** P22 ***** (OVERLAYS LPS 20.1 STORAGE)   (6D)
S('VSUBC', 'equals', 0o1760, line=976)  # I(6) S-S CSM VELOCITY VECTOR

# PADLOADED ERASABLES FOR P20/P22               (6D)

S('RANGEVAR', 'erase', 0o1770, line=980)  # I(2) RR RANGE ERROR VARIANCE
S('RATEVAR', 'erase', 0o1772, line=981)  # I(2) RR RANGE RATE ERROR VARIANCE
S('RVARMIN', 'erase', 0o1774, line=982)  # I(1) MINIMUM RANGE ERROR VARIANCE
S('VVARMIN', 'erase', 0o1775, line=983)  # I(1) MINIMUM RANGE-RATE ERROR VARIANCE

# P32-P33 STORAGE                               (2D)

S('TCDH', 'erase', 0o1776, line=987)  # I(2) T2 CDH TIME IN CS. (ALSO DOWNLINKED)

S('END-E3', 'equals', 0o1777, line=989)  # ** LAST LOCATION USED IN E3 **

# Page 113
# EBANK-4 ASSIGNMENTS

#   SETLOC 2000

# E4 IS, FOR THE MOST PART RESERVED FOR PAD LOADED AND UNSHARABLE ERASE.

S('AMEMORY', 'equals', 0o2000, line=998)

# P20 STORAGE.  -- PAD LOADED --                (6D)

S('WRENDPOS', 'erase', 0o2000, line=1002)  # B(1)PL        KM*2(-7)
S('WRENDVEL', 'erase', 0o2001, line=1003)  # B(1)PL        KM(-1/2)*2(11)
S('WSHAFT', 'erase', 0o2002, line=1004)  # B(1)PL        KM*2(-7)
S('WTRUN', 'erase', 0o2003, line=1005)  # B(1)PL        KM*2(-7)
S('RMAX', 'erase', 0o2004, line=1006)  # B(1)PL        METERS*2(-19)
S('VMAX', 'erase', 0o2005, line=1007)  # B(1)PL        M/CSEC*2(-7)

# LUNAR SURFACE NAVIGATION                      (2D)

S('WSURFPOS', 'erase', 0o2006, line=1011)  # B(1)PL
S('WSURFVEL', 'erase', 0o2007, line=1012)  # B(1)PL

# P22 STORAGE.  -- PAD LOADED --                (2D)

S('SHAFTVAR', 'erase', 0o2010, line=1016)  # B(1)PL        RAD SQ*2(12)
S('TRUNVAR', 'erase', 0o2011, line=1017)  # B(1)PL        RAD SQ*2(10)

# CONISEX STORAGE.  -- PAD LOADED --

S('504LM', 'erase', 0o2012, line=1021)  # I(6) MOON LIBRATION VECTOR

# V47 (R47) AGS INITIALIZATION STORAGE.  -- PAD LOADED --       (2D)

S('AGSK', 'erase', 0o2020, line=1025)

# LUNAR LANDING STORAGE.  -- PAD LOADED --      (6D)

S('RLS', 'erase', 0o2022, line=1029)  # I(6) LANDING SITE VECTOR -- MOON REF

# INTEGRATION STORAGE.                          (102D)

S('PBODY', 'erase', 0o2030, line=1033)  # I(1)
# Page 114
S('ALPHAV', 'equals', 0o2031, line=1035)  # I(6)
S('BETAV', 'equals', 0o2037, line=1036)  # I(6)
S('PHIV', 'equals', 0o2045, line=1037)  # I(6)
S('PSIV', 'equals', 0o2053, line=1038)  # I(6)
S('FV', 'equals', 0o2061, line=1039)  # I(6)  PERTURBING ACCELERATIONS
S('ALPHAM', 'equals', 0o2067, line=1040)  # I(2)
S('BETAM', 'equals', 0o2071, line=1041)  # I(2)
S('TAU.', 'equals', 0o2073, line=1042)  # I(2)
S('DT/2', 'equals', 0o2075, line=1043)  # I(2)
S('H', 'equals', 0o2077, line=1044)  # I(2)
S('GMODE', 'equals', 0o2101, line=1045)  # I(1)
S('IRETURN', 'equals', 0o2102, line=1046)  # I(1)
S('NORMGAM', 'equals', 0o2103, line=1047)  # I(1)
S('RPQV', 'equals', 0o2104, line=1048)
S('ORIGEX', 'equals', 0o2112, line=1049)  # I(1)
S('KEPRTN', 'equals', 0o2112, line=1050)  # I(1)
S('RQVV', 'equals', 0o2113, line=1051)  # I(6)
S('RPSV', 'equals', 0o2121, line=1052)  # I(6)
S('XKEPNEW', 'equals', 0o2127, line=1053)  # I(2)
S('VECTAB', 'equals', 0o2131, line=1054)  # I(36D)
S('VECTABND', 'equals', 0o2174, line=1055)  # END MARK

# THESE PROBABLY CAN SHARE MID-COURSE VARIABLES.        (6D)

S('VACX', 'equals', 0o2137, line=1059)  # I(2)
S('VACY', 'equals', 0o2141, line=1060)  # I(2)
S('VACZ', 'equals', 0o2143, line=1061)  # I(2)

# SERVICER STORAGE (USED BY ALL POWERED FLIGHT PROGS.)  (18D)

S('XNBPIP', 'equals', 0o2145, line=1065)  # I(6)
S('YNBPIP', 'equals', 0o2153, line=1066)  # I(6)
S('ZNBPIP', 'equals', 0o2161, line=1067)  # I(6)

# SOME VERB 82 STORAGE                          (4D)

S('HAPOX', 'equals', 0o2117, line=1071)  # I(2)
S('HPERX', 'equals', 0o2121, line=1072)  # I(2)

# V82 STORAGE                                   (6D)

S("VONE'", 'equals', 0o2167, line=1076)  # I(T)TMP NORMAL VELOCITY VONE / SQRT. MU

# R32(V83) STORAGE. -- SHARES WITH INTEGRATION STORAGE --       (28D)

# Page 115
S('BASETHV', 'equals', 0o2104, line=1081)  # I(6) BASE VEL VECTOR THIS VEH

S('BASETIME', 'equals', 0o2113, line=1083)  # I(2) TIME ASSOC WITH BASE VECS
S('ORIG', 'equals', 0o2115, line=1084)  # I(1) =0 FOR EARTH     =2 FOR MOON
S('STATEXIT', 'equals', 0o2116, line=1085)  # I(1) STQ ADDRESS FOR STATEXTP
S('BASEOTV', 'equals', 0o2117, line=1086)  # I(6) BASE VEL VECTOR OTHER VEH

S('BASEOTP', 'equals', 0o2137, line=1088)  # I(6) BASE POS VECTOR OTHER VEH

S('BASETHP', 'equals', 0o2167, line=1090)  # I(6) BASE POS VECTOR THIS VEH

# KEPLER STORAGE. (KEPLER IS CALLED BY PRECISION INTEGRATION AND (2D)
# CONICS)

S('EPSILONT', 'erase', 0o2176, line=1095)  # I(2)

# VERB 83 STORAGE                               (18D)

S('RANGE', 'erase', 0o2200, line=1099)  # I(2)DSP NOUN 54 DISTANCE TO OPTICAL SUBJ
S('RRATE', 'equals', 0o2202, line=1100)  # I(2)DSP NOUN 54 RATE OF APPROACH
S('RTHETA', 'equals', 0o2204, line=1101)  # I(2)DSP NOUN 54.
S('RONE', 'equals', 0o2206, line=1102)  # I(6)TMP VECTOR STORAGE.  (SCRATCH)
S('VONE', 'equals', 0o2214, line=1103)  # I(6)TMP VECTOR STORAGE.  (SCRATCH)

# VERB 67 STORAGE

S('WWPOS', 'equals', 0o2200, line=1107)  # NOUN 99 (V67)
S('WWVEL', 'equals', 0o2202, line=1108)  # NOUN 99 (V67)
S('WWBIAS', 'equals', 0o2204, line=1109)  # NOUN 99 (V67)

# V82 STORAGE.  (CANNOT OVERLAY RONE OR VONE)   (11D) TWO SEPARAT LOCATIONS

S('V82FLAGS', 'equals', 0o2137, line=1113)  # (1) FOR V82 BITS.
S('TFF', 'equals', 0o2140, line=1114)  # I(2)
S('-TPER', 'equals', 0o2142, line=1115)  # I(2)

S('HPERMIN', 'equals', 0o2200, line=1117)  # I(2) SET TO 300KFT FOR SR30.1
S('RPADTEM', 'equals', 0o2202, line=1118)  # I(2) PAD OR LANDING RADIUS FOR SR30.1
S('TSTART82', 'equals', 0o2204, line=1119)  # I(2) TEMP TIME STORAGE VOR V82.

# VARIOUS DISPLAY REGISTERS                     (6D) NOUN 84; P76
# Page 116
S('DELVOV', 'erase', 0o2222, line=1123)  # (6)

# ALIGNMENT PLANETARY -- INERTIAL TRANSFORMATION STORAGE.       (18D)

# UNSHARED WHILE LM ON LUNAR SURFACE.

S('GSAV', 'erase', 0o2230, line=1129)  # I(6)
S('YNBSAV', 'equals', 0o2236, line=1130)  # I(6)
S('ZNBSAV', 'equals', 0o2244, line=1131)  # I(6)

# KALCMANU STORAGE, CAN OVERLAY GSAV.           (18D)

S('MFS', 'equals', 0o2230, line=1135)  # I(18)
S('MFI', 'equals', 0o2230, line=1136)  # I
S('KEL', 'equals', 0o2230, line=1137)  # I(18)
S('E01', 'equals', 0o2230, line=1138)  # I(6)
S('E02', 'equals', 0o2236, line=1139)  # I(6)

# LR VEL BEAM VECTORS.                          (26D)

# CAN OVERLAY GSAV WITH CARE, USED DURING POWERED DESCENT ONLY.

S('VZBEAMNB', 'equals', 0o2230, line=1145)  # I(6) LR VELOCITY BEAMS IN NB COORDS.
S('VYBEAMNB', 'equals', 0o2236, line=1146)  # I(6)
S('VXBEAMNB', 'equals', 0o2244, line=1147)  # I(6) PRESERVE Z,Y,X ORDER

S('LRVTIME', 'equals', 0o2252, line=1149)  # B(2) LR
S('LRXCDU', 'equals', 0o2254, line=1150)  # B(1) LR
S('LRYCDU', 'equals', 0o2255, line=1151)  # B(1) LR
S('LRZCDU', 'equals', 0o2256, line=1152)  # B(1) LR
S('PIPTEM', 'equals', 0o2257, line=1153)  # B(3) LR

# P32-P35, P72-P75 STORAGE.                     (40D)

S('T1TOT2', 'erase', 0o2252, line=1157)  # (2)   TIME FROM CSI TO CDH
S('T2TOT3', 'erase', 0o2254, line=1158)  # (2)
S('ELEV', 'erase', 0o2256, line=1159)  # (2)
S('UP1', 'erase', 0o2260, line=1160)  # (6)
S('DELVEET1', 'erase', 0o2266, line=1161)  # I(6)  DV CSI IN REF
S('DELVEET2', 'erase', 0o2274, line=1162)  # I(6)  DV CSH IN REF
S('RACT1', 'erase', 0o2302, line=1163)  # (6)   POS VEC OF ACTIVE AT CSI TIME
S('RACT2', 'erase', 0o2310, line=1164)  # (6)   POS VEC OF ACTIVE AT CDH TIME
# Page 117
S('RTSR1/MU', 'erase', 0o2316, line=1166)  # (2)   SQ ROOT 1/MU STORAGE
S('RTMU', 'erase', 0o2320, line=1167)  # (2)   MU STORAGE

# (THE FOLLOWING ERASABLES OVERLAY PORTIONS OF THE PREVIOUS SECTION)

S('+MGA', 'equals', 0o2252, line=1171)  # (2) S-S + MID GIM ANGL TO DELVEET3

S('UNRM', 'equals', 0o2260, line=1173)  # I(6) S-S

S('DVLOS', 'equals', 0o2302, line=1175)  # I(6) S-S DELTA VELOCITY, LOS COORD-DISPLAY
S('ULOS', 'equals', 0o2310, line=1176)  # I(6) S-S UNIT LINE OF SIGHT VECTOR

S('NOMTPI', 'equals', 0o2316, line=1178)  # (2) S-S NOMINAL TPI-TIME FOR RECYCLE

# SOME P30 STORAGE.                             (4D)

S('HAPO', 'equals', 0o2316, line=1182)  # I(2)
S('HPER', 'equals', 0o2320, line=1183)  # I(2)

# SOME P38-P39,P78-79 STORAGE           #       (6D)

S('DELTAR', 'equals', 0o2302, line=1188)  # I(2)
S('DELTTIME', 'equals', 0o2304, line=1189)  # I(2) TIME REPRESENTATION OF DELTAR
S('TARGTIME', 'equals', 0o2306, line=1190)  # I(2) TINT MINUS DELTTIME

S('TINTSOI', 'equals', 0o2302, line=1192)  # I(2) TIME OF INTERCEPT FOR SOI PHASE

# THE FOLLOWING ARE ERASABLE LOADS DURING A PERFORMANCE TEST.

S('TRANSM1', 'equals', 0o2000, line=1196)  # E4,1400
S('ALFDK', 'equals', 0o2022, line=1197)

# ****** THE FOLLOWING SECTIONS OVERLAY V83 AND DISPLAY STORAGE ******

# V47 (R47) AGS INITIALIZATION PROGRAM STORAGE.  (OVERLAYS V83) (14D)

S('AGSBUFF', 'equals', 0o2200, line=1203)  # B(14D)
S('AGSBUFFE', 'equals', 0o2215, line=1204)  # ENDMARK
# Page 118

# R36 OUT-OF-PLANE RENDEZVOUS DISPLAY STORAGE.  (OVERLAYS V83)  (12D)

S('RPASS36', 'equals', 0o2206, line=1209)  # I(6) S-S
S('UNP36', 'equals', 0o2214, line=1210)  # I(6) S-S

# S-BAND ANTENNA GIMBAL ANGLES.  DISPLAYED BY R05 (V64).  (OVERLAYS V83)        (10D)
# (OPERATES DURING P00 ONLY)
S('ALPHASB', 'equals', 0o2200, line=1214)  # B(2)DSP NOUN 51.  PITCH ANGLE.
S('BETASB', 'equals', 0o2202, line=1215)  # B(2)DSP NOUN 51.  YAW ANGLE.
S('RLM', 'equals', 0o2204, line=1216)  # I(6)S S/C POSITION VECTOR.

# **** USED IN S-BAND ANTENNA FOR LM ****

S('YAWANG', 'equals', 0o2202, line=1220)
S('PITCHANG', 'equals', 0o2200, line=1221)

# NOUN 56 DATA -- COMPUTED AND DISPLAYED BY VERB 85.

S('RR-AZ', 'equals', 0o2200, line=1225)  # I(2) ANGLE BETWEEN LOS AND X-Z PLANE
S('RR-ELEV', 'equals', 0o2202, line=1226)  # I(2) ANGLE BETWEEN LOS AND Y-Z PLANE

# R04 (V62) RADAR TEST STORAGE.
# R04 IS RESTRICTED TO P00.

S('RSTACK', 'equals', 0o2200, line=1231)  # B(8) BUFFER FOR R04 NOUNS.

# INITVEL STORAGE.  ALSO USED BY P31, P34, P35, P74, P75, P10, P11, MIDGIM, S40.1 AND S40.9.    (18D)

# (POSSIBLY RINIT & VINIT CAN OVERLAY DELVEET1 & 2 ABOVE)

S('RINIT', 'erase', 0o2322, line=1237)  # I(6) ACTIVE VEHICLE POSITION
S('VINIT', 'erase', 0o2330, line=1238)  # I(6) ACTIVE VEHICLE VELOCITY
S('VIPRIME', 'erase', 0o2336, line=1239)  # I(6) NEW VEL REQUIRED AT INITIAL RADIUS.

# VARIOUS DISPLAY REGISTERS.  BALLANGS          (3D)

S('FDAIX', 'erase', 0o2344, line=1243)  # I(1)
S('FDAIY', 'erase', 0o2345, line=1244)  # I(1)
S('FDAIZ', 'erase', 0o2346, line=1245)  # I(1)

# P34-P35 STORAGE.  DOWNLINKED.                 (2D)

S('DELVTPF', 'erase', 0o2347, line=1249)  # I(2) DELTA V FOR TPF

# SOME R04(V63)-R77 RADAR TEST STORAGE.         (6D)
# Page 119
S('RTSTDEX', 'erase', 0o2351, line=1253)  # (1)
S('RTSTMAX', 'erase', 0o2352, line=1254)  # (1)
S('RTSTBASE', 'erase', 0o2353, line=1255)  # (1)
S('RTSTLOC', 'erase', 0o2354, line=1256)  # (1)
S('RSTKLOC', 'equals', 0o2354, line=1257)
S('RSAMPDT', 'erase', 0o2355, line=1258)  # (1)
S('RFAILCNT', 'erase', 0o2356, line=1259)  # (1)

# LPS20.1 STORAGE.                              (12D)

S('LMPOS', 'equals', 0o2351, line=1263)  # I(6)TMP  STORAGE FOR LM POS. VECTOR.
S('LMVEL', 'equals', 0o2357, line=1264)  # I(6)TMP  STORAGE FOR LM VEL. VECTOR.

# INITVEL STORAGE.  ALSU USED BY P31,34,35,74,75,S40.1 AND DOWNLINKED.  (6D)

S('DELVEET3', 'equals', 0o2365, line=1268)  # I(6) DELTA V IN INERTIAL COORDINATES

S('END-E4', 'equals', 0o2357, line=1271)  # FIRST UNUSED LOCATION IN E4

# SECOND DPS GUIDANCE (LUNAR LANDING)  (OVERLAY P32-35, INITVEL)        (14D)

S('VHORIZ', 'equals', 0o2262, line=1275)  # I(2) DISPLAY
S('ANGTERM', 'equals', 0o2264, line=1276)  # I(6) GUIDANCE
S('HBEAMNB', 'equals', 0o2272, line=1277)  # I(6) LANDING RADAR

# R12 DOWNLINK QUANTITIES                       (5D)

S('LRXCDUDL', 'equals', 0o2334, line=1281)  # B(1) LANDING RADAR DOWNLINK
S('LRYCDUDL', 'equals', 0o2335, line=1282)  # B(1) LANDING RADAR DOWNLINK
S('LRZCDUDL', 'equals', 0o2336, line=1283)  # B(1) LANDING RADAR DOWNLINK
S('LRVTIMDL', 'equals', 0o2337, line=1284)  # B(2) LANDING RADAR DOWNLINK

# ASCENT GUIDANCE FOR LUNAR LANDING             (54D)

S('AT', 'equals', 0o2262, line=1288)  # I(2)TMP ENGINE DATA -- THRUST ACC*2(9)
S('VE', 'equals', 0o2264, line=1289)  # I(2)TMP EXHAUST VELOCITY * 2(7)M/CS.
S('TTO', 'equals', 0o2266, line=1290)  # I(2)TMP TAILOFF TIME * 2(17)CS.
S('TBUP', 'equals', 0o2270, line=1291)  # I(2)TMP (M/MDOT) * 2(17)CS.
S('RDOTD', 'equals', 0o2272, line=1292)  # I(2)TMP TARGET VELOCITY COMPONENTS
S('YDOTD', 'equals', 0o2274, line=1293)  # I(2)TMP SCALING IS 2(7)M/CS.
S('ZDOTD', 'equals', 0o2276, line=1294)  # I(2)TMP

S('/R/MAG', 'equals', 0o2300, line=1296)  # I(2)TMP
S('LAXIS', 'equals', 0o2302, line=1297)  # I(6)TMP
# Page 120
S('ZAXIS1', 'equals', 0o3725, line=1299)
S('RDOT', 'equals', 0o3473, line=1300)
S('YDOT', 'equals', 0o2310, line=1301)  # I(2)TMP VEL. NORMAL TO REF. PLANE*2(-7)
S('ZDOT', 'equals', 0o2312, line=1302)  # I(2)TMP DOWN RANGE VEL * 2(-7)
S('GEFF', 'equals', 0o2314, line=1303)  # I(2)TMP EFFECTIVE GRAVITY

# THESE TWO GROUPS OF ASCENT GUIDANCE ARE SPLIT BY THE ASCENT-DESCENT SERVICER SECTION FOLLOWING THIS SECTION

S('Y', 'equals', 0o2334, line=1307)  # I(2)TMP OUT-OF-PLANE DIST *2(24)M
S('DRDOT', 'equals', 0o2336, line=1308)  # I(2)TMP RDOTD - RDOT
S('DYDOT', 'equals', 0o2340, line=1309)  # I(2)TMP YDOTD - YDOT
S('DZDOT', 'equals', 0o2342, line=1310)  # I(2)TMP ZDOTD - ZDOT
S('PCONS', 'equals', 0o2344, line=1311)  # I(2)TMP CONSTANT IN ATR EQUATION
S('YCONS', 'equals', 0o2346, line=1312)  # I(2)TMP CONSTANT IN ATY EQUATION
S('PRATE', 'equals', 0o2350, line=1313)  # I(2)TMP RATE COEFF. IN ATR EQUATION
S('YRATE', 'equals', 0o2352, line=1314)  # I(2)TMP RATE COEFF. IN ATY EQUATION
S('ATY', 'equals', 0o2354, line=1315)  # I(2)TMP OUT-OF-PLANE THRUST COMP. *2(9)
S('ATR', 'equals', 0o2356, line=1316)  # I(2)TMP RADIAL THRUST COMP. * 2(9)
S('ATP', 'equals', 0o2360, line=1317)  # I(2)TMP DOWN-RANGE THRUST COMP
S('YAW', 'equals', 0o2362, line=1318)  # I(2)TMP
S('PITCH', 'equals', 0o2364, line=1319)  # I(2)TMP

# SERVICER FOR LUNAR ASCENT AND DESCENT         (14D)

S('G(CSM)', 'equals', 0o2316, line=1323)  # I(6)  FOR UPDATE OF COMMAND MODULE STATE
S('R(CSM)', 'equals', 0o1717, line=1324)  #       VECTORS BY LEM: ANALOGS OF GDT/2,
S('V(CSM)', 'equals', 0o1725, line=1325)  #       R, AND V, RESPECTIVELY OF THE CSM
S('WM', 'equals', 0o2324, line=1326)  # I(6)TMP -- LUNAR ROTATION VECTOR (SM)
S('/LAND/', 'equals', 0o2332, line=1327)  # B(2) LUNAR RADIUS AT LANDING SITE

# Page 121
# EBANK-5 ASSIGNMENTS

#   SETLOC 2400

# W-MATRIX.  ESSENTIALLY UNSHARABLE.            (162D)

S('W', 'erase', 0o2400, line=1336)
S('ENDW', 'equals', 0o2642, line=1337)

# ******* OVERLAY NUMBER 1 IN EBANK 5 *******

# W-MATRIX PADLOADS               (124D)

S('TLAND', 'equals', 0o2400, line=1343)  # I(2)  NOMINAL TIME OF LANDING
S('RBRFG', 'equals', 0o2402, line=1344)  # I(6) BRAKING
S('VBRFG', 'equals', 0o2410, line=1345)  # I(6)      PHASE
S('ABRFG', 'equals', 0o2416, line=1346)  # I(6)           TARGET
S('VBRFG*', 'equals', 0o2424, line=1347)  # I(2)                PARAMETERS:
S('ABRFG*', 'equals', 0o2426, line=1348)  # I(2)                     HIGH
S('JBRFG*', 'equals', 0o2430, line=1349)  # I(2)                          GATE
S('GAINBRAK', 'equals', 0o2432, line=1350)  # B(2)
S('TCGFBRAK', 'equals', 0o2434, line=1351)  # B(1)
S('TCGIBRAK', 'equals', 0o2435, line=1352)  # B(1)
S('RAPFG', 'equals', 0o2436, line=1353)  # I(6) APPROACH
S('VAPFG', 'equals', 0o2444, line=1354)  # I(6)      PHASE
S('AAPFG', 'equals', 0o2452, line=1355)  # I(6)           TARGET
S('VAPFG*', 'equals', 0o2460, line=1356)  # I(2)                PARAMETERS:
S('AAPFG*', 'equals', 0o2462, line=1357)  # I(2)                     LOW
S('JAPFG*', 'equals', 0o2464, line=1358)  # I(2)                          GATE
S('GAINAPPR', 'equals', 0o2466, line=1359)  # B(2)
S('TCGFAPPR', 'equals', 0o2470, line=1360)  # B(1)
S('TCGIAPPR', 'equals', 0o2471, line=1361)  # B(1)
S('VIGN', 'equals', 0o2472, line=1362)  # I(2)  DESIRED SPEED FOR IGNITION
S('RIGNX', 'equals', 0o2474, line=1363)  # I(2)  DESIRED `ALTITUDE' FOR IGNITION
S('RIGNZ', 'equals', 0o2476, line=1364)  # I(2)  DESIRED GROUND RANGE FOR IGNITION
S('KIGNX/B4', 'equals', 0o2500, line=1365)  # I(2)
S('KIGNY/B8', 'equals', 0o2502, line=1366)  # I(2)
S('KIGNV/B4', 'equals', 0o2504, line=1367)  # I(2)
S('LOWCRIT', 'equals', 0o2506, line=1368)  # B(1) (HIGHCRIT MUST FOLLOW LOWCRIT)
S('HIGHCRIT', 'equals', 0o2507, line=1369)  # B(1)
S('V2FG', 'equals', 0o2510, line=1370)  # I(6) DESIRED VELOCITY FOR P65.
S('TAUVERT', 'equals', 0o2516, line=1371)  # I(2) TIME CONSTANT FOR P65 VEL. NULLING.
S('DELQFIX', 'equals', 0o2520, line=1372)  # I(2) LR ALTITUDE DATA REASONABLE PARM.
S('LRALPHA', 'equals', 0o2522, line=1373)  # B(1) POS1 X ROTATION          * MUST *
# Page 122
S('LRBETA1', 'equals', 0o2523, line=1375)  # B(1) POS1 Y ROTATION          *  BE  *
S('LRALPHA2', 'equals', 0o2524, line=1376)  # B(1) POS2 X ROTATION          *  IN  *
S('LRBETA2', 'equals', 0o2525, line=1377)  # B(1) POS2 Y ROTATION          * ORDER*
S('LRVMAX', 'equals', 0o2526, line=1378)  # B(1) LR VEL WEIGHTING FUNCTIONS
S('LRVF', 'equals', 0o2527, line=1379)  # B(1) LR VEL WEIGHTING FUNCTIONS
S('LRWVZ', 'equals', 0o2530, line=1380)  # B(1) LR VEL WEIGHTING FUNCTIONS
S('LRWVY', 'equals', 0o2531, line=1381)  # B(1) LR VEL WEIGHTING FUNCTIONS
S('LRWVX', 'equals', 0o2532, line=1382)  # B(1) LR VEL WEIGHTING FUNCTIONS
S('LRWVFZ', 'equals', 0o2533, line=1383)  # B(1) LR VEL WEIGHTING FUNCTIONS
S('LRWVFY', 'equals', 0o2534, line=1384)  # B(1) LR VEL WEIGHTING FUNCTIONS
S('LRWVFX', 'equals', 0o2535, line=1385)  # B(1) LR VEL WEIGHTING FUNCTIONS
S('LRWVFF', 'equals', 0o2536, line=1386)  # B(1) LR VEL WEIGHTING FUNCTIONS

S('ABVEL*', 'equals', 0o130, line=1388)  # B(1) LR TEMP
S('VSELECT*', 'equals', 0o131, line=1389)  # B(1) LR TEMP

S('RODSCALE', 'equals', 0o2537, line=1391)  # I(1) CLICK SCALE FACTOR FOR ROD
S('TAUROD', 'equals', 0o2540, line=1392)  # I(2) TIME CONSTANT FOR R.O.D.
S('LAG/TAU', 'equals', 0o2542, line=1393)  # I(2) LAG TIME DIVIDED BY TAUROD (P66)
S('MINFORCE', 'equals', 0o2544, line=1394)  # I(2) MINIMUM FORCE P66 WILL COMMAND
S('MAXFORCE', 'equals', 0o2546, line=1395)  # I(2) MAXIMUM FORCE P66 WILL COMMAND.
S('ABTCOF', 'equals', 0o2550, line=1396)  # I(16) COEFFICIENTS FOR ABORT TFI POLYS.
S('VMIN', 'equals', 0o2570, line=1397)  # I(2) MINIMUM VELOCITY FOR ABORT INJ.
S('YLIM', 'equals', 0o2572, line=1398)  # I(2) MAXIMUM CROSS-RANGE DIST. IN ABORTS
S('ABTRDOT', 'equals', 0o2574, line=1399)  # I(2) DESIRED RADIAL VEL. FOR ABORTS.
S('COSTHET1', 'equals', 0o2576, line=1400)  # I(2) COS CONE 1 ANGLE FOR ABORTS.
S('COSTHET2', 'equals', 0o2600, line=1401)  # I(2) COS OF CONE 2 ANGLE FOR ABORTS.

# SOME VARIABLES FOR SECOND DPS GUIDANCE.       (34D)

S('CG', 'equals', 0o2602, line=1405)  # I(18D) GUIDANCE
S('RANGEDSP', 'equals', 0o2624, line=1406)  # B(2) DISPLAY
S('OUTOFPLN', 'equals', 0o2626, line=1407)  # B(2) DISPLAY
S('R60VSAVE', 'equals', 0o2630, line=1408)  # I(6)TMP SAVES VALUE OF POINTVSM THRU R51
S('RGU', 'equals', 0o2636, line=1409)  # I(6) UNSHARED FOR DOWNLINK
S('VBIAS', 'equals', 0o2630, line=1410)  # I(6) PIPA BIAS EQUIV. VELOCITY VECTOR.
S('L*WCR*T', 'equals', 0o130, line=1411)
S('H*GHCR*T', 'equals', 0o131, line=1412)

# ALIGNMENT/SYSTEST/CALCSMSC COMMON STORAGE     (36D)

S('XSM', 'equals', 0o2642, line=1416)  # B(6)
S('YSM', 'equals', 0o2650, line=1417)  # B(6)
S('ZSM', 'equals', 0o2656, line=1418)  # B(6)

S('XDC', 'equals', 0o2664, line=1420)  # B(6)
S('YDC', 'equals', 0o2672, line=1421)  # B(6)
S('ZDC', 'equals', 0o2700, line=1422)  # B(6)
# Page 123
S('XNB', 'equals', 0o2664, line=1424)
S('YNB', 'equals', 0o2672, line=1425)
S('ZNB', 'equals', 0o2700, line=1426)

# OVERLAYS WITHIN ALIGNMENT/SYSTEST/CALCSMSC COMMON STORAGE     (4D)

S('-COSB', 'equals', 0o2644, line=1430)  # (2)TMP
S('SINB', 'equals', 0o2646, line=1431)  # (2)TMP

# MORE OVERLAYS TO ALIGNMENT/SYSTEST (THESE ARE P52)    (6D)

S('LANDLAT', 'equals', 0o2706, line=1435)  # (2) LATTITUDE, LONGITUDE
S('LANDLONG', 'equals', 0o2710, line=1436)  # (2)   AND ALTITUDE
S('LANDALT', 'equals', 0o2712, line=1437)  # (2)   OF LANDING SITE

# ALIGNMENT/SYSTEST COMMON STORAGE.             (31D)

S('STARAD', 'equals', 0o2706, line=1441)  # I(18D)TMP
S('STAR', 'equals', 0o2730, line=1442)  # I(6)
S('GCTR', 'equals', 0o2736, line=1443)  # B(1)
S('OGC', 'equals', 0o2737, line=1444)  # I(2)
S('IGC', 'equals', 0o2741, line=1445)  # I(2)
S('MGC', 'equals', 0o2743, line=1446)  # I(2)

# P57 ALIGNMENT (OVERLAY OF ALIGNMENT/SYSTEST COMMON STORAGE)   (12D)

S('GACC', 'equals', 0o2706, line=1450)  # (6) SS
S('GOUT', 'equals', 0o2714, line=1451)  # (6) SS

# OVERLAYS WITHIN ALIGNMENT/SYSTEST COMMON STORAGE      (24D)

S('VEARTH', 'equals', 0o2706, line=1455)  # (6)TMP
S('VSUN', 'equals', 0o2714, line=1456)  # (6)TMP
S('VMOON', 'equals', 0o2722, line=1457)  # (6)TMP
S('SAX', 'equals', 0o2730, line=1458)  # (6)TMP

# P50'S, R50'S Q STORES                         (2D)

S('QMIN', 'equals', 0o2745, line=1462)  # B(1)TMP
S('QMAJ', 'equals', 0o2746, line=1463)  # B(1)TMP

# **** USED IN P50S **** (SCATTERED OVERLAYS)

S('XSCI', 'equals', 0o2706, line=1467)
S('YSCI', 'equals', 0o2714, line=1468)
# Page 124
S('ZSCI', 'equals', 0o2714, line=1470)
S('CULTRIX', 'equals', 0o2706, line=1471)  # VEARTH, VSUN, VMOON
S('VEC1', 'equals', 0o2722, line=1472)
S('VEC2', 'equals', 0o2730, line=1473)

# ALIGNMENT STORAGE.                            (23D)

S('OGCT', 'equals', 0o2747, line=1477)  # I(6)
S('BESTI', 'equals', 0o2755, line=1478)  # I(1)
S('BESTJ', 'equals', 0o2756, line=1479)
S('STARIND', 'equals', 0o2757, line=1480)
# RETAIN THE ORDER OF STARSAV1 TO STARSAV2 +5 FOR DOWNLINK PURPOSES
S('STARSAV1', 'equals', 0o2760, line=1482)  # I(6)
S('STARSAV2', 'equals', 0o2766, line=1483)  # I(6)
S('TALIGN', 'equals', 0o2774, line=1484)  # B(2) TIME OF IMU ALIGNMENT (DOWNLINKED)

# P32-35 + SERVICER

S('RTX1', 'equals', 0o2776, line=1488)  # I(1) X1       -2 EARTH, -10 MOON
S('RTX2', 'equals', 0o2777, line=1489)  # I(1) X2       0 EARTH, 2 MOON

S('ZPRIME', 'equals', 0o26, line=1491)
S('PDA', 'equals', 0o26, line=1492)
S('COSTH', 'equals', 0o20, line=1493)
S('SINTH', 'equals', 0o22, line=1494)
S('THETA', 'equals', 0o24, line=1495)
S('STARM', 'equals', 0o40, line=1496)

# Page 125
# ******* OVERLAY NUMBER 2 IN EBANK 5 *******

# CONICS ROUTINE STORAGE.                       (85D)

S('DELX', 'equals', 0o2642, line=1503)  # I(2)TMP
S('DELT', 'equals', 0o2644, line=1504)  # I(2)TMP
S('URRECT', 'equals', 0o2646, line=1505)  # I(6)TMP
S('RCNORM', 'equals', 0o42, line=1506)  # I(2)TMP
S('XPREV', 'equals', 0o1552, line=1507)  # I(2)TMP
S('R1VEC', 'equals', 0o2654, line=1508)  # I(6)TMP
S('R2VEC', 'equals', 0o2662, line=1509)  # I(6)TMP
S('TDESIRED', 'equals', 0o2670, line=1510)  # I(2)TMP
S('GEOMSGN', 'equals', 0o2672, line=1511)  # I(1)TMP
S('UN', 'equals', 0o2673, line=1512)  # I(6)TMP
S('VTARGTAG', 'equals', 0o2701, line=1513)  # I(1)TMP
S('VTARGET', 'equals', 0o2702, line=1514)  # I(6)TMP
S('RTNLAMB', 'equals', 0o2710, line=1515)  # I(1)TMP
S('U2', 'equals', 0o2711, line=1516)  # I(6)TMP
S('MAGVEC2', 'equals', 0o2717, line=1517)  # I(2)TMP
S('UR1', 'equals', 0o2721, line=1518)  # I(6)TMP
S('SNTH', 'equals', 0o2727, line=1519)  # I(2)TMP
S('CSTH', 'equals', 0o2731, line=1520)  # I(2)TMP
S('1-CSTH', 'equals', 0o2733, line=1521)  # I(2)TMP
S('CSTH-RHO', 'equals', 0o2735, line=1522)  # I(2)TMP
S('P', 'equals', 0o2737, line=1523)  # I(2)TMP
S('R1A', 'equals', 0o2741, line=1524)  # I(2)TMP
S('RVEC', 'equals', 0o2654, line=1525)  # I(6)TMP
S('VVEC', 'equals', 0o2743, line=1526)  # I(6)TMP
S('RTNTT', 'equals', 0o2710, line=1527)  # I(1)TMP
S('ECC', 'equals', 0o2751, line=1528)  # I(2)TMP
S('RTNTR', 'equals', 0o2710, line=1529)  # I(1)TMP
S('RTNAPSE', 'equals', 0o2710, line=1530)  # I(1)TMP
S('R2', 'equals', 0o2717, line=1531)  # I(2)TMP
S('RTNPRM', 'equals', 0o2753, line=1532)  # I(1)TMP
S('SGNRDOT', 'equals', 0o2754, line=1533)  # I(1)TMP
S('RDESIRED', 'equals', 0o2755, line=1534)  # I(2)TMP
S('DELDEP', 'equals', 0o2757, line=1535)  # I(2)TMP
S('DEPREV', 'equals', 0o2761, line=1536)  # I(2)TMP
S('TERRLAMB', 'equals', 0o2757, line=1537)  # I(2)TMP
S('TPREV', 'equals', 0o2761, line=1538)  # I(2)TMP
S('EPSILONL', 'equals', 0o2763, line=1539)  # I(2)TMP
S('COGA', 'equals', 0o2765, line=1540)  # I(2)  COTAN OF INITIAL FLIGHT PATH ANGLE.
S('INDEP', 'equals', 0o2765, line=1541)  #       USED BY SUBROUTINE `ITERATOR'.

# Page 126
# ******* OVERLAY NUMBER 3 IN EBANK 5 *******

# INCORP STORAGE.                               (18D)

S('ZI', 'equals', 0o2642, line=1548)  # I(18D)TMP

# INCORP/L SR22.3 STORAGE.                      (21D)

S('DELTAX', 'equals', 0o2664, line=1552)  # I(18)
S('VARIANCE', 'equals', 0o2706, line=1553)  # I(3)

# MEASUREMENT INCORPORATION -R22- STORAGE.      (49D)

S('GRP2SVQ', 'equals', 0o2711, line=1557)  # I(1)TMP QSAVE FOR RESTARTS
S('OMEGAM1', 'equals', 0o2712, line=1558)  # I(6)
S('OMEGAM2', 'equals', 0o2720, line=1559)  # I(6)
S('OMEGAM3', 'equals', 0o2726, line=1560)  # I(6)
S('HOLDW', 'equals', 0o2734, line=1561)  # I(18)
S('TDPOS', 'equals', 0o2756, line=1562)  # I(6)
S('TDVEL', 'equals', 0o2764, line=1563)  # I(6)

S('TRIPA', 'equals', 0o2664, line=1565)  # I(3)TMP
S('TEMPVAR', 'equals', 0o2667, line=1566)  # I(3)TMP

# INCORPORATION/INTEGRATION Q STORAGE.          (1D)

S('EGRESS', 'equals', 0o2772, line=1570)  # I(1)

# P30/P31 STORAGE.                              (1D) AND ONE OVERLAY

S('P30EXIT', 'equals', 0o2773, line=1574)  # B(1)TMP

S('ORIGIN', 'equals', 0o2773, line=1576)  # I(1)TMP INTEX DURING INITVEL.

# Page 127
# SYSTEM TEST ERASABLES.  CAN OVERLAY W MATRIX. (127D)

# ******* OVERLAY NUMBER 0 IN EBANK 5 *******

S('AZIMUTH', 'equals', 0o2400, line=1583)  # 2
S('LATITUDE', 'equals', 0o2402, line=1584)  # 2
S('ERVECTOR', 'equals', 0o2404, line=1585)  # 6
S('LENGTHOT', 'equals', 0o2412, line=1586)  # 1
S('LOSVEC', 'equals', 0o2413, line=1587)  # 6
S('NDXCTR', 'equals', 0o2414, line=1588)  # 1
S('PIPINDEX', 'equals', 0o2415, line=1589)  # 1
S('POSITON', 'equals', 0o2416, line=1590)  # 1
S('QPLACE', 'equals', 0o2417, line=1591)  # 1
S('QPLACES', 'equals', 0o2420, line=1592)  # 1
S('SOUTHDR', 'equals', 0o2421, line=1593)  # 7
S('TEMPTIME', 'equals', 0o2430, line=1594)  # 2
S('TMARK', 'equals', 0o2432, line=1595)  # 2
S('GENPL', 'equals', 0o2434, line=1596)
S('CDUTIMEI', 'equals', 0o2434, line=1597)
S('CDUTIMEF', 'equals', 0o2436, line=1598)
S('CDUDANG', 'equals', 0o2440, line=1599)
S('CDUREADF', 'equals', 0o2441, line=1600)
S('CDUREADI', 'equals', 0o2442, line=1601)
S('CDULIMIT', 'equals', 0o2443, line=1602)

S('TEMPADD', 'equals', 0o2440, line=1604)
S('TEMP', 'equals', 0o2441, line=1605)
S('NOBITS', 'equals', 0o2442, line=1606)
S('CHAN', 'equals', 0o2443, line=1607)

S('LOS1', 'equals', 0o2444, line=1609)
S('LOS2', 'equals', 0o2452, line=1610)

S('CALCDIR', 'equals', 0o2460, line=1612)
S('CDUFLAG', 'equals', 0o2461, line=1613)
S('GYTOBETQ', 'equals', 0o2462, line=1614)
S('OPTNREG', 'equals', 0o2463, line=1615)
S('SAVE', 'equals', 0o2464, line=1616)  # THREE ONSEC LOC
S('SFCONST1', 'equals', 0o2467, line=1617)
S('TIMER', 'equals', 0o2470, line=1618)

S('DATAPL', 'equals', 0o2472, line=1620)
S('RDSP', 'equals', 0o2434, line=1621)  # FIX LATER     POSSIBLY KEEP1
S('MASKREG', 'equals', 0o2534, line=1622)
S('CDUNDX', 'equals', 0o2536, line=1623)
S('RESULTCT', 'equals', 0o2537, line=1624)
S('COUNTPL', 'equals', 0o2542, line=1625)

S('CDUANG', 'equals', 0o2543, line=1627)
# Page 128
S('AINLA', 'equals', 0o2434, line=1629)  # 110 DEC OR 156 OCT LOCATIONS

S('WANGO', 'equals', 0o2434, line=1631)  # VERT ERATE
S('WANGI', 'equals', 0o2436, line=1632)  # HORIZONTAL ERATE
S('WANGT', 'equals', 0o2440, line=1633)  # T
S('TORQNDX', 'equals', 0o2440, line=1634)
S('DRIFTT', 'equals', 0o2442, line=1635)
S('ALX1S', 'equals', 0o2444, line=1636)
S('CMPX1', 'equals', 0o2445, line=1637)  # IND
S('ALK', 'equals', 0o2446, line=1638)  # GAINS
S('VLAUNS', 'equals', 0o2462, line=1639)
S('WPLATO', 'equals', 0o2464, line=1640)
S('INTY', 'equals', 0o2470, line=1641)  # SOUTH  IP INTE
S('ANGZ', 'equals', 0o2472, line=1642)  # EAST A IS
S('INTZ', 'equals', 0o2474, line=1643)  # EAST P P I
S('ANGY', 'equals', 0o2476, line=1644)  # SOUTH
S('ANGX', 'equals', 0o2500, line=1645)  # VE
S('DRIFTO', 'equals', 0o2502, line=1646)  # VERT
S('DRIFTI', 'equals', 0o2504, line=1647)  # SOU
S('VLAUN', 'equals', 0o2510, line=1648)
S('ACCWD', 'equals', 0o2512, line=1649)
S('POSNV', 'equals', 0o2520, line=1650)
S('DPIPAY', 'equals', 0o2522, line=1651)  # SOUTH
S('DPIPAZ', 'equals', 0o2526, line=1652)  # NORTH  IP INCREMENT
S('ALTIM', 'equals', 0o2530, line=1653)
S('ALTIMS', 'equals', 0o2531, line=1654)  # INDEX
S('ALDK', 'equals', 0o2532, line=1655)  # TIME  ONSTAN
S('DELM', 'equals', 0o2550, line=1656)
S('WPLATI', 'equals', 0o2560, line=1657)
S('GEOCOMPS', 'equals', 0o2562, line=1658)
S('ERCOMP', 'equals', 0o2563, line=1659)
S('ZERONDX', 'equals', 0o2571, line=1660)

S('THETAN', 'equals', 0o2452, line=1662)
S('FILDELV', 'equals', 0o2460, line=1663)  # AGS ALIGNMENT STORAGE
S('INTVEC', 'equals', 0o2462, line=1664)
S('1SECXT', 'equals', 0o2572, line=1665)
S('ASECXT', 'equals', 0o2573, line=1666)
S('PERFDLAY', 'equals', 0o2574, line=1667)  # B(2) DELAY TIME BEF. START DRIFT MEASURE
S('OVFLOWCK', 'equals', 0o2576, line=1668)  # (1) SET MEANS OVERFLOW IN IMU PERF TEST

S('END-E5', 'equals', 0o2774, line=1670)  # *** FIRST FREE LOCATION IN E5 ***

# Page 129
# EBANK-6 ASSIGNMENTS.

#   SETLOC 3000

# DAP PAD-LOADED DATA.                          (10D)

# ALL OF THE FOLLOWING EXCEPT PITTIME AND ROLLTIME ARE INITIALIZED IN FRESH START TO PERMIT IMMEDIATE USE OF DAP.

S('HIASCENT', 'erase', 0o3000, line=1681)  # (1) MASS AFTER STAGING, SCALE AT B16 KG.
S('ROLLTIME', 'erase', 0o3001, line=1682)  # (1) TIME TO TRIM Z GIMBAL IN R03, CSEC.
S('PITTIME', 'erase', 0o3002, line=1683)  # (1) TIME TO TRIM Y GIMBAL IN R03, CSEC.
S('DKTRAP', 'erase', 0o3003, line=1684)  # (1) DAP STATE            (POSSIBLE 77001
S('DKOMEGAN', 'erase', 0o3004, line=1685)  # (1)   ESTIMATOR PARA-      (VALUES 00012
S('DKKAOSN', 'erase', 0o3005, line=1686)  # (1)     METERS FOR THE             00074
S('LMTRAP', 'erase', 0o3006, line=1687)  # (1)       DOCKED AND               77001
S('LMOMEGAN', 'erase', 0o3007, line=1688)  # (1)         LEM-ALONE CASES        00000
S('LMKAOSN', 'erase', 0o3010, line=1689)  # (1)           RESPECTIVELY         00074
S('DKDB', 'erase', 0o3011, line=1690)  # (1) WIDTH OF DEADBAND FOR DOCKED RCS
# AUTOPILOT (DB=1.4DEG IN FRESH START
# DEADBAND = PI/DKDB RAD.

# PADLOADS FOR INTITIALIZATION OF DAP BIAS ACCELERATION (AT P12 IGNITION)       (2D)

S('IGNAOSQ', 'erase', 0o3012, line=1696)  # B(1)PL
S('IGNAOSR', 'erase', 0o3013, line=1697)  # B(1)PL

# AXIS TRANSFORMATION MATRIX -- GIMBAL TO PILOT AXES:   (5D)

S('M11', 'erase', 0o3014, line=1701)  # SCALED AT 1
S('M21', 'erase', 0o3015, line=1702)  # SCALED AT 1
S('M31', 'erase', 0o3016, line=1703)
S('M22', 'erase', 0o3017, line=1704)  # SCALED AT 1.
S('M32', 'erase', 0o3020, line=1705)  # SCALED AT 1.

# ANGLE MEASUREMENTS

S('OMEGAP', 'erase', 0o3021, line=1709)  # BODY-AXIS ROT. RATES SCALED AT PI/4 AND
S('OMEGAQ', 'equals', 0o3022, line=1710)  # BODY-AXIS ACCELERATIONS SCALED AT PI/8.
S('OMEGAR', 'equals', 0o3023, line=1711)
# RETAIN THE ORDER OF ALPHAQ AND ALPHAR FOR DOWNLINK PURPOSES.
S('ALPHAQ', 'equals', 0o3024, line=1713)
S('ALPHAR', 'equals', 0o3025, line=1714)
S('OMEGAU', 'erase', 0o3026, line=1715)
S('OMEGAV', 'equals', 0o3027, line=1716)

S('TRAPEDP', 'erase', 0o3030, line=1718)
S('TRAPEDQ', 'equals', 0o3031, line=1719)
S('TRAPEDR', 'equals', 0o3032, line=1720)
S('NPTRAPS', 'equals', 0o3033, line=1721)
# Page 130
S('NQTRAPS', 'equals', 0o3034, line=1723)
S('NRTRAPS', 'equals', 0o3035, line=1724)
S('EDOTP', 'equals', 0o3027, line=1725)
S('EDOTQ', 'erase', 0o3036, line=1726)
S('EDOTR', 'equals', 0o3037, line=1727)  # MANY SHAREING NAMES
S('QRATEDIF', 'equals', 0o3036, line=1728)  # ALTERNATIVE NAMES:
S('RRATEDIF', 'equals', 0o3037, line=1729)  # DELETE WHEN NO. OF REFERENCES = 0

S('URATEDIF', 'equals', 0o3026, line=1731)
S('VRATEDIF', 'equals', 0o3027, line=1732)
S('OLDXFORP', 'erase', 0o3040, line=1733)  # STORED CDU READINGS FOR STATE
S('OLDYFORP', 'equals', 0o3041, line=1734)  # DERIVATIONS: SCALED AT PI RADIANS (2'S)
S('OLDZFORQ', 'equals', 0o3042, line=1735)

# RATE-COMMAND AND MINIMUM IMPULSE MODES

S('CH31TEMP', 'erase', 0o3043, line=1739)
S('STIKSENS', 'erase', 0o3044, line=1740)
S('TCP', 'erase', 0o3045, line=1741)
S('DXERROR', 'erase', 0o3046, line=1742)
S('DYERROR', 'equals', 0o3050, line=1743)
S('DZERROR', 'equals', 0o3052, line=1744)
S('PLAST', 'erase', 0o3054, line=1745)
S('QLAST', 'erase', 0o3055, line=1746)
S('RLAST', 'erase', 0o3056, line=1747)
S('TCQR', 'erase', 0o3057, line=1748)

# OTHER VARIABLES                               (5D)

S('OLDPMIN', 'erase', 0o3060, line=1752)  # THESE THREE USED IN MIN IMPUSE MODE
S('OLDQRMIN', 'erase', 0o3061, line=1753)
S('TEMP31', 'equals', 0o3337, line=1754)

S('SAVEHAND', 'erase', 0o3062, line=1756)
S('PERROR', 'erase', 0o3064, line=1757)
S('QERROR', 'equals', 0o3050, line=1758)
S('RERROR', 'equals', 0o3052, line=1759)

# JET STATE CHANGE VARIABLES -- TIME (TOFJTCHG), JET BITS WRITTEN NOW   (10D)
# (JTSONNOW), AND JET BITS WRITTEN AT T6 RUPT (JTSATCHG).

S('NXT6ADR', 'erase', 0o3065, line=1764)
S('T6NEXT', 'erase', 0o3066, line=1765)
S('T6FURTHA', 'erase', 0o3070, line=1766)
S('NEXTP', 'erase', 0o3072, line=1767)
S('NEXTU', 'equals', 0o3073, line=1768)
S('NEXTV', 'equals', 0o3074, line=1769)
S('-2JETLIM', 'erase', 0o3075, line=1770)  # RATE COMMAND 4-JET RATE DIFFERENCE LIMIT
S('-RATEDB', 'equals', 0o3076, line=1771)  # AND RATE DEADBAND FOR ASCENT OR DESCENT

S('TARGETDB', 'equals', 0o3076, line=1773)  # MAN. CONTROL TARGET DB COMPLEMENT.

# ***Q,R AXIS ERASABLES ***             (3)
# Page 131
S('PBIT', 'equals', 0o4742, line=1777)
S('QRBIT', 'equals', 0o4741, line=1778)
S('UERROR', 'equals', 0o3351, line=1779)  # U,V-AXES ATT ERROR FOR RCS CONTROL LAWS.
S('VERROR', 'equals', 0o3352, line=1780)
S('RETJADR', 'erase', 0o3077, line=1781)
S('TEMPNUM', 'equals', 0o3342, line=1782)
S('NUMBERT', 'equals', 0o3343, line=1783)
S('ROTINDEX', 'equals', 0o3344, line=1784)
S('ROTEMP1', 'equals', 0o3337, line=1785)
S('ROTEMP2', 'equals', 0o3340, line=1786)
S('POLYTEMP', 'equals', 0o3341, line=1787)
S('SENSETYP', 'erase', 0o3100, line=1788)
S('ABSTJ', 'equals', 0o3337, line=1789)  # ABS VALUE OF JET-FIRING TIME
S('ABSEDOTP', 'equals', 0o3337, line=1790)

S('DPSBURN', 'equals', 0o3350, line=1792)  # USED WITH SNUFFBIT.  VERY TEMPORARY.

# Page 132
# TRIM GIMBAL CONTROL LAW ERASABLES:            (11D)

S('GTSTEMPS', 'equals', 0o3337, line=1797)  # GTS IS PART OF THE JASK.
S('SHFTFLAG', 'equals', 0o3341, line=1798)  # COUNT BITS FOR GTSQRT SHIFTING.
S('ININDEX', 'equals', 0o3344, line=1799)  # INDEX FOR SHIFT LOOP IN GTSQRT.

S('SAVESR', 'equals', 0o3105, line=1801)  # CANNOT BE A DAPTEMP -- GTS USES THEM ALL.

S('SCRATCH', 'equals', 0o3346, line=1803)  # ROOTCYCL ERASABLE.
S('HALFARG', 'equals', 0o3347, line=1804)  # ROOTCYCL ERASABLE.

S('K2THETA', 'equals', 0o3337, line=1806)  # D,P., K*ERROR, NEGUSUM
S('KCENTRAL', 'equals', 0o3341, line=1807)  # S.P., K FROM KQ OR KRDAP, AT PI/2(8)
S('K2CNTRAL', 'equals', 0o3342, line=1808)  # D.P., GTS SCRATCH CELLS.
S('WCENTRAL', 'equals', 0o3343, line=1809)  # S.P., OMEGA, AT PI/4 RAD/SEC
S('ACENTRAL', 'equals', 0o3344, line=1810)  # S.P., ALPHA, AT PI/4 RAD/SEC(2)
S('DEL', 'equals', 0o3345, line=1811)  # S.P., SGN FUNCTION VALUE.
S('A2CNTRAL', 'equals', 0o3346, line=1812)  # D.P., GTS SCRATCH CELLS.
S('QRCNTR', 'equals', 0o3350, line=1813)  # S.P., INDEX FOR GTS LOOP THROUGH Q,R AXES
S('FUNCTION', 'equals', 0o3351, line=1814)  # D.P., ARGUMENT FOR GRSQRT, SCRATCH FOR GTS.

S('NEGUQ', 'erase', 0o3101, line=1816)  # NEGATIVE OF Q-AXIS GIMBAL DRIVE.
#   EQUALS NEGUQ +1  # DEFINED AND USED ELSEWHERE.
S('NEGUR', 'equals', 0o3103, line=1818)  # NEGATIVE OF R-AXIS GIMBAL DRIVE.

S('KQ', 'erase', 0o3104, line=1820)  # S.P., JERK TERM FOR GTS, AT PI/2(8)
S('AXISCTR', 'equals', 0o3105, line=1821)
S('KRDAP', 'equals', 0o3106, line=1822)  # .3 ACCDOTR SCALED AT PI/2(8)

S('ACCDOTQ', 'erase', 0o3107, line=1824)  # Q-JERK SCALED AT PI/2(7) UNSIGNED
S('QACCDOT', 'equals', 0o3110, line=1825)  # Q-JERK SCALED AT PI/2(7) SIGNED
S('ACCDOTR', 'equals', 0o3111, line=1826)  # R-JERK SCALED AT PI/2(7) UNSIGNED
S('RACCDOT', 'equals', 0o3112, line=1827)  # R-JERK SCALED AT PI/2(7) SIGNED

S('QDIFF', 'equals', 0o3050, line=1829)  # ATTITUDE ERRORS:
S('RDIFF', 'equals', 0o3052, line=1830)  # SCALED AT PI RADIANS.

# TORQUE VECTOR RECONSTRUCTION VARIABLES:       (18D)

S('JETRATE', 'equals', 0o3345, line=1834)
S('JETRATEQ', 'equals', 0o3346, line=1835)  # THE LAST CONTROL SAMPLE PERIOD OF 100 MS.
S('JETRATER', 'equals', 0o3347, line=1836)  # SCALED AT PI/4 RADIANS/SECOND

S('DOWNTORK', 'erase', 0o3113, line=1838)  # ACCUMULATED JET TORQUE COMMANDED ABOUT
S('POSTORKP', 'equals', 0o3113, line=1839)  #       +,-p, +,-u, +,-v RESPECTIVELY.
S('NETTOTKP', 'equals', 0o3114, line=1840)  #       EMPLOYED EXCLUSIVELY FOR DOWNLIST.
S('POSTORKU', 'equals', 0o3115, line=1841)  #       NOT INITIALIZED:  PERMITTED TO OVERFLOW.
# Page 133
S('NEGTORKU', 'equals', 0o3116, line=1843)  #       SCALED AT 32 JET-SEC, OR ABOUT 2.0 JET-
S('POSTORKV', 'equals', 0o3117, line=1844)  #       MSEC. PER BIT.
S('NEGTORKV', 'equals', 0o3120, line=1845)

S('NO.PJETS', 'erase', 0o3121, line=1847)
S('NO.UJETS', 'equals', 0o3122, line=1848)
S('NO.VJETS', 'equals', 0o3123, line=1849)
S('TJP', 'erase', 0o3124, line=1850)
S('TJU', 'equals', 0o3125, line=1851)
S('TJV', 'equals', 0o3126, line=1852)

S('L,PVT-CG', 'erase', 0o3127, line=1854)
S('1JACC', 'erase', 0o3130, line=1855)  # ACCELERATIONS DUE TO 1 JET TORQUING
S('1JACCQ', 'equals', 0o3131, line=1856)  # SCALED AT PI/4 RADIANS/SECOND
S('1JACCR', 'equals', 0o3132, line=1857)
S('1JACCU', 'equals', 0o3133, line=1858)  # FOR U,V-AXES THE SCALE FACTOR IS DOFF:
S('1JACCV', 'equals', 0o3134, line=1859)  # SCALED AT PI/2 RADIANS/SECOND (FOR ASC)

# ASCENT VARIABLES                              (10D)

S('SKIPU', 'erase', 0o3135, line=1863)
S('SKIPV', 'equals', 0o3136, line=1864)

# THE FOLLOWING LM DAP ERASABLES ARE ZEROED IN THE STARTDAP SECTION OF THE DAPIDLER PROGRAM AND THE COASTASC
# SECTION OF THE AOSTASK.  THE ORDER MUST BE PRESERVED FOR THE INDEXING METHODS WHICH ARE EMPLOYED IN THOSE
# SECTIONS AND ELSEWHERE.

S('AOSQ', 'erase', 0o3137, line=1870)  # OFFSET ACC. ESTIMATES, UPDATED IN D.P.,
S('AOSR', 'equals', 0o3141, line=1871)  # AND SCALED AT PI/2.
S('AOSU', 'equals', 0o3143, line=1872)  # UV-AXES OFFSET ACC. FROMED BY VECTOR
S('AOSV', 'equals', 0o3144, line=1873)  # ADDITION OF Q,R. AT PI/2 RAD/SEC(2).

S('AOSQTERM', 'erase', 0o3145, line=1875)  # (.1-.05K)AOS
S('AOSRTERM', 'equals', 0o3146, line=1876)  # SCALED AT PI/4 RADIANS/SECOND.

# FOR TJET LAW SUBROUTINES:                     (TEMPS ONLY)

# NUMBERT        EQUALS  DAPTEMP5        # DEFINED IN QRAXIS.
S('EDOTSQ', 'equals', 0o3337, line=1881)
S('ROTSENSE', 'equals', 0o3340, line=1882)
S('FIREFCT', 'equals', 0o3341, line=1883)  # LOOKED AT BY PAXIS.
S('TTOAXIS', 'equals', 0o3342, line=1884)
S('ADRSDIF2', 'equals', 0o3344, line=1885)
S('HOLDQ', 'equals', 0o3345, line=1886)
S('ADRSDIF1', 'equals', 0o3346, line=1887)
S('HH', 'equals', 0o3347, line=1888)  # DOUBLE PRECISION.
# HH +1         EQUALS  DAPTREG4
S('E', 'equals', 0o3352, line=1890)  # TIME SHARE WITH VERROR
S('EDOT', 'equals', 0o3027, line=1891)

# Page 134
# INPUT TO TJET LAW (PERMANENT ERASABLES).      (48D)

S('TJETU', 'equals', 0o3125, line=1896)  # EQUATE NAMES.  INDEXED BY -1, 0, +1.
S('BLOCKTOP', 'erase', 0o3147, line=1897)
S('1/ANET1', 'equals', 0o3167, line=1898)  # THESE 8 PARAMETERS ARE SET UP BY 1/ACCS
S('1/ANET2', 'equals', 0o3170, line=1899)  # FOR MINIMUM JETS ABOUT THE U-AXIS WHEN
S('1/ACOAST', 'equals', 0o3173, line=1900)  # EDOT IS POSITIVE.  TJETLAW INDEXES BY
S('ACCFCTZ1', 'equals', 0o3175, line=1901)  # ADRSDIFF FROM THESE REGISTERS TO PICK UP
S('ACCFCTZ5', 'equals', 0o3176, line=1902)  # PARAMETERS FOR THE PROPER AXIS, NUMBER
S('FIREDB', 'equals', 0o3201, line=1903)  # OF JETS AND SIGN OF EDOT.  THERE ARE 48
S('COASTDB', 'equals', 0o3203, line=1904)  # REGISTERS IN ALL IN THIS BLOCK.
S('AXISDIST', 'equals', 0o3205, line=1905)  # FOUR NOT REFERENCED (P-AXIS) ARE FILLED
# IN BY THE FOLLOWING:
S('ACCSWU', 'equals', 0o3147, line=1907)  # SET BY 1/ACCS TO SHOW WHETHER MAXIMUM
S('ACCSWV', 'equals', 0o3150, line=1908)  # JETS ARE REQUIRED BECAUSE OF AOS.
S('FLAT', 'equals', 0o3155, line=1909)  # WIDTH OF MINIMUM IMPULSE ZONE.
S('ZONE3LIM', 'equals', 0o3156, line=1910)  # HEIGHT OF MINIMUM IMPULSE ZONE (AT 4 SEC.)

S('COEFFQ', 'erase', 0o3227, line=1912)  # COEFFQ AND COEFFR ARE USED IN ROT-TOUV
S('COEFFR', 'equals', 0o3230, line=1913)  # TO REXOLVE Q,R COMPONENTS INTO U,V COMP.

# VARIABLES FOR GTS-QRAXIS CONTROL EXCHANGE.    (4)

S('ALLOWGTS', 'equals', 0o3102, line=1917)  # INSERT INTO UNUSED LOCATION
S('COTROLER', 'erase', 0o3231, line=1918)  # INDICATES WHICH CONTROL SYSTEM TO USE.
S('QGIMTIMR', 'erase', 0o3232, line=1919)  # Q-GIMBAL DRIVE ITMER, DECISECONDS.
S('INGTS', 'equals', 0o3233, line=1920)  # INDICATOR OF CURRENT GTS CONTROL.
S('RGIMTIMR', 'equals', 0o3234, line=1921)  # R-GIMBAL DRIVE TIMER, DECISECONDS.

# PLEASE RETAIN THE ORDER OF CDUXD THRU CDUZD FOR DOWNLINK PURPOSES.

# KALCMANU:DAP INTERFACE                        (9D)

S('CDUXD', 'erase', 0o3235, line=1927)  # CDU DESIRED REGISTERS:
S('CDUYD', 'equals', 0o3236, line=1928)  # SCALED AT PI RADIANS (180 DEGREES)
S('CDUZD', 'equals', 0o3237, line=1929)  # (STORE IN 2'S COMPLEMENT)

S('DELCDUX', 'erase', 0o3240, line=1931)  # NEGATIVE OF DESIRED 100MS CDU INCREMENT:
S('DELCDUY', 'equals', 0o3241, line=1932)  # SCALED AT PI RADIANS (180 DEGREES)
S('DELCDUZ', 'equals', 0o3242, line=1933)  # (STORE IN 2'S COMPLEMENT)

# RETAIN THE ORDER OF OMEGAPD TO OMEGARD FOR DOWNLINK PURPOSES.

S('OMEGAPD', 'erase', 0o3243, line=1937)  # ATTITUDE MANEUVER DESIRED RATES:
S('OMEGAQD', 'equals', 0o3244, line=1938)  # (NOT EXPLICITLY REFERENCED IN GTS CNTRL)
S('OMEGARD', 'equals', 0o3245, line=1939)  # SCALED AT PI/4 RADIANS/SECOND

# KALCMANU STORAGE.                             (24D)

S('MIS', 'erase', 0o3246, line=1943)  # I(18D)
# Page 135
S('COF', 'equals', 0o3270, line=1945)  # I(6)

# KALCMANU STORAGE.                             (33D)
S('BCDU', 'erase', 0o3276, line=1948)  # B(3)
S('KSPNDX', 'equals', 0o3301, line=1949)  # B(1)
S('KDPNDX', 'equals', 0o3302, line=1950)  # B(1)

S('TMIS', 'equals', 0o3303, line=1952)  # I(18) MUST BE IN SAME BANK AS RCS DAP
S('COFSKEW', 'equals', 0o3325, line=1953)  # I(6)  MUST BE IN THE SAME BANK AS RCS DAP
S('CAM', 'equals', 0o3333, line=1954)  # I(2)  MUST BE IN THE SAME BANK AS RCS DAP

S('AM', 'erase', 0o3335, line=1956)  # I(2) THIS WAS ONCE IN E5 OVERLAYING OGC

# FIRST-ODER OVERLAYS IN KALCMANU               (25D)
S('KV1', 'equals', 0o3303, line=1959)  # I(6)
S('MFISYM', 'equals', 0o3303, line=1960)  # I
S('TMFI', 'equals', 0o3303, line=1961)  # I
S('NCDU', 'equals', 0o3303, line=1962)  # B
S('NEXTIME', 'equals', 0o3306, line=1963)  # B
S('TTEMP', 'equals', 0o3307, line=1964)  # B
S('KV2', 'equals', 0o3311, line=1965)  # I(6)
S('BIASTEMP', 'equals', 0o3311, line=1966)  # B
S('KV3', 'equals', 0o3317, line=1967)  # I(6)
S('OGF', 'equals', 0o3317, line=1968)  # I

S('BRATE', 'equals', 0o3325, line=1970)  # B
S('IG', 'equals', 0o3325, line=1971)  # I

S('TM', 'equals', 0o3333, line=1973)  # B

# SECOND-ORDER OVERLAYS IN KALCMANU             (24D)

S('K1', 'equals', 0o3303, line=1977)
S('K2', 'equals', 0o3311, line=1978)
S('K3', 'equals', 0o3317, line=1979)
S('P21', 'equals', 0o3303, line=1980)  # I(2)
S('D21', 'equals', 0o3305, line=1981)  # I(2)
S('G21', 'equals', 0o3307, line=1982)  # I(2)
S('C2SQP', 'equals', 0o3311, line=1983)  # I(2)
S('C2SQM', 'equals', 0o3313, line=1984)  # I(2)
S('C2PP', 'equals', 0o3315, line=1985)  # I(2)
S('C2MP', 'equals', 0o3317, line=1986)  # I(2)
S('C1PP', 'equals', 0o3321, line=1987)  # I(2)
S('C1MP', 'equals', 0o3323, line=1988)  # I(2)
# Page 136
S('VECQTEMP', 'equals', 0o3325, line=1990)

S('DCDU', 'equals', 0o3235, line=1992)
S('DELDCDU', 'equals', 0o3240, line=1993)
S('DELDCDU1', 'equals', 0o3241, line=1994)
S('DELDCDU2', 'equals', 0o3242, line=1995)

# *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *

# STORAGE FOR FINDCDUW

# OVERLAYING KALCMANU STORAGE:                  (26D)

S('ECDUW', 'equals', 0o3246, line=2003)
S('ECDUWUSR', 'equals', 0o3246, line=2004)  # B(1)TMP
S('QCDUWUSR', 'equals', 0o3247, line=2005)  # I(1)TMP
S('NDXCDUW', 'equals', 0o3250, line=2006)  # B(1)TMP
S('FLAGOODW', 'equals', 0o3251, line=2007)  # B(1)TMP
S('FLPAUTNO', 'equals', 0o3252, line=2008)  # B(1)TMP
S('UNFC/2', 'equals', 0o3253, line=2009)  # I(6)IN
S('UNWC/2', 'equals', 0o3261, line=2010)  # I(6)IN
S('UNFV/2', 'equals', 0o3267, line=2011)  # I(6) S-S
S('UNFVX/2', 'equals', 0o3267, line=2012)
S('UNFVY/2', 'equals', 0o3271, line=2013)
S('UNFVZ/2', 'equals', 0o3273, line=2014)
S('-DELGMB', 'equals', 0o3275, line=2015)  # B(3)TMP

# DEFINED IN THE WORK AREA:                     (18D)

S('UNX/2', 'equals', 0o0, line=2019)
S('UNY/2', 'equals', 0o6, line=2020)
S('UNZ/2', 'equals', 0o14, line=2021)

# END OF FINDCDUW ERASABLES

# *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *

# THE FOLLOWING ARE THE DAP REPLACEMENTS FOR THE ITEMPS AND RUPTREGS, NEEDED BECAUSE DAP IS NOW A TOB,JASK,JAB,TOSK
# ... ANYWAY, THE DAP CAN NOW BE INTERRUPTED.   (18D)

S('DAPTEMP1', 'erase', 0o3337, line=2030)
S('DAPTEMP2', 'equals', 0o3340, line=2031)
S('DAPTEMP3', 'equals', 0o3341, line=2032)
S('DAPTEMP4', 'equals', 0o3342, line=2033)
S('DAPTEMP5', 'equals', 0o3343, line=2034)
S('DAPTEMP6', 'equals', 0o3344, line=2035)
S('DAPTREG1', 'equals', 0o3345, line=2036)
S('DAPTREG2', 'equals', 0o3346, line=2037)
S('DAPTREG3', 'equals', 0o3347, line=2038)
# Page 137
S('DAPTREG4', 'equals', 0o3350, line=2040)
S('DAPTREG5', 'equals', 0o3351, line=2041)
S('DAPTREG6', 'equals', 0o3352, line=2042)

S('DAPARUPT', 'equals', 0o3353, line=2044)
S('DAPLRUPT', 'equals', 0o3354, line=2045)
S('DAPBQRPT', 'equals', 0o3355, line=2046)
S('DAPZRUPT', 'equals', 0o3357, line=2047)
# (DAPZRUPT IS ALSO A JASK-IN-PROGRESS FLAG)

# NEEDLER (ATTITUDE ERROR EIGHT BALL DISPLAY) STORAGE.  (6D)

S('T5TEMP', 'equals', 0o61, line=2052)
S('DINDX', 'equals', 0o63, line=2053)
S('AK', 'erase', 0o3361, line=2054)  # NEEDLER ATTITUDE INPUTS, SCALED AT 180
S('AK1', 'equals', 0o3362, line=2055)  # DEGREES.  P,Q,R AXES IN AK,AK1,AK2.
S('AK2', 'equals', 0o3363, line=2056)

S('EDRIVEX', 'erase', 0o3364, line=2058)  # NEEDLER DISPLAY REGS AT 1800 DEGREES.
S('EDRIVEY', 'equals', 0o3365, line=2059)  # SO THAT 384 BITS REPRESENT 42 3/16 DEGREES.
S('EDRIVEZ', 'equals', 0o3366, line=2060)

# DOCKED JET INHIBITION COUNTERS                (3D)

S('PJETCTR', 'erase', 0o3367, line=2064)
S('UJETCTR', 'equals', 0o3370, line=2065)
S('VJETCTR', 'equals', 0o3371, line=2066)

S('END-E6', 'equals', 0o3371, line=2068)

# Page 138
# EBANK-7 ASSIGNMENTS

#   SETLOC 3400

# P35 CONSTANTS.        -- PAD LOADED --        (4D)

S('ATIGINC', 'erase', 0o3400, line=2077)  # B(2)PL        *MUST BE AT 1400 FOR SYSTEMSTEST
S('PTIGINC', 'erase', 0o3402, line=2078)  # B(2)PL

# AOTMARK STORAGE.      -- PAD LOADED --        (12D)

S('AOTAZ', 'erase', 0o3404, line=2082)  # B(6)PL
S('AOTEL', 'erase', 0o3412, line=2083)  # B(6)PL

# LANDING RADAR         -- PAD LOADED --        (2D)

S('LRHMAX', 'erase', 0o3420, line=2087)  # B(1)
S('LRWH', 'erase', 0o3421, line=2088)  # B(1)

# THROTTLE STORAGE.     -- PAD LOADED --        (1D)

S('ZOOMTIME', 'erase', 0o3422, line=2092)  # B(1)PL TIME OF DPS THROTTLE-UP COMMAND

# P63 AND P64 CONSTANTS.        -- PAD LOADED --        (4D)

S('TENDBRAK', 'erase', 0o3423, line=2096)  # B(1) LANDING PHASE SWITCHING CRITERION.
S('TENDAPPR', 'erase', 0o3424, line=2097)  # B(1) LANDING PHASE SWITCHING CRITERION.
S('DELTTFAP', 'erase', 0o3425, line=2098)  # B(1) INCREMENT ADDED TO TTF/8 WHEN
# SWITCHING FROM P63 TO P64.
S('LEADTIME', 'erase', 0o3426, line=2100)  # B(1) TIME INCREMENT SPECIFYING HOW MUCH
# GUIDANCE IS PROJECTED FORWARD

# LANDING RADAR.        -- PAD LOADED --        (2D)

S('RPCRTIME', 'erase', 0o3427, line=2105)  # B(1) REPOSITIONING CRITERION (TIME)
S('RPCRTQSW', 'erase', 0o3430, line=2106)  # B(1) REPOSITIONING CRITERION (ANGLE)

# ASTEER.               -- PAD LOADED --        (2D)

S('TNEWA', 'erase', 0o3431, line=2110)  # I(2)PL LAMBERT CYCLE PERIOD.

# P22 STORAGE -- OVERLAYS LANDING PADLOADS --   (5D)
# Page 139
S('REPOSCNT', 'equals', 0o3423, line=2114)  # B(1)TMP COUNTS NUMBER OF PASSES THROUGH
# REPOSITION ROUTINE.
S('REPOSTM', 'equals', 0o3424, line=2116)  # I(2)TMP PRESENT TIME PLUS INCREMENTS OF
# TEN SECONDS.
S('DELTATM', 'equals', 0o3426, line=2118)  # I(2)TMP TIME INTERVAL FOR RUNNING
# DESIGNATE TASK.

# *** RETAIN THE ORDER OF DELVSLV, TIG, RTARG, DELLT4 FOR UPDATE. ***

# P32-35 P72-75 STORAGE.                        (6D)

S('DELVLVC', 'erase', 0o3433, line=2125)  # I(6) DELTA VELOCITY -- LOCAL VERTICAL COO
S('DELVSLV', 'equals', 0o3433, line=2126)  # (TEMP STORAGE OF SAME VECTOR)    -RDINATE

# P30-P40 INTERFACE UNSHARED.                   (2D)

S('TIG', 'erase', 0o3441, line=2130)  # B(2)

# INITVEL STORAGE.  ALSO USED BY P34,35,74,75,10,11 OTHERS      (8D)

S('RTARG', 'erase', 0o3443, line=2134)  # I(6) TARGET VECTOR
S('DELLT4', 'erase', 0o3451, line=2135)  # I(2) TIME DIFFERENCE

# P30-P40 INTERFACE UNSHARED.                   (3D)

S('TTOGO', 'erase', 0o3453, line=2139)  # B(2)
S('TFI', 'equals', 0o3453, line=2140)
S('WHICH', 'erase', 0o3455, line=2141)  # B(1)

# *** R21 ***                                   (1D)

S('LOSCOUNT', 'erase', 0o3456, line=2145)  # B(1)

# L SR22.3 (RENDEZVOUS NAVIGATION) STORAGE.             (4D)

# RETAIN THE ORDER OF AIG TO TRKMKCNT FOR DOWNLINK PURPOSES.

S('AIG', 'erase', 0o3457, line=2151)  # B(1)OUT GIMBAL ANGLES
S('AMG', 'erase', 0o3460, line=2152)  # B(1)OUT (MUST BE
S('AOG', 'erase', 0o3461, line=2153)  # B(1)OUT  CONSECUTIVE)

S('TRKMKCNT', 'erase', 0o3462, line=2155)  # B(1)TMP TEMPORARY MARK STORAGE.
S('MARKCTR', 'equals', 0o3462, line=2156)

# Page 140
# P32-P35, P72-P75 STORAGE.  -- PERMANENT --    (6)

S('NORMEX', 'erase', 0o3463, line=2161)  # B(1)PRM SAVE FOR Q
S('QSAVED', 'erase', 0o3464, line=2162)  # B(1)PRM SAVE FOR Q
S('RTRN', 'erase', 0o3465, line=2163)  # B(1)PRM SAVE FOR Q
S('NN', 'erase', 0o3466, line=2164)  # B(2)
S('SUBEXIT', 'erase', 0o3470, line=2165)  # B(1)PRM SAVE Q

S('E7OVERLA', 'equals', 0o3471, line=2167)  # START OF E7 OVERLAYS
S('WHOCARES', 'equals', 0o3471, line=2168)  # DUMMY FOR EBANK INSENSITIVE 2CADRS.

# LUNAR LANDING OVERLAYS                        (6D)

S('/AFC/', 'equals', 0o3463, line=2172)  # B(2)TMP THROTTLE
S('FCODD', 'equals', 0o3465, line=2173)  # B(2)TMP THROTTLE
S('FP', 'equals', 0o3467, line=2174)  # B(2)TMP THROTTLE
# Page 141
# ******* OVERLAY NUMBER 0 IN EBANK 7 *******

# RENDEZVOUS GUIDANCE STORAGE --P32.....P35--   (89D)

S('TSTRT', 'equals', 0o3611, line=2180)  # MIDCOURSE START TIME
S('TDEC2', 'equals', 0o3573, line=2181)  # TEMP STORAGE FOR INTEGRATION TIME INPUT
S('KT', 'equals', 0o3575, line=2182)  # TEMP STORAGE FOR MIDCOURSE DELTA TIME
S('VACT1', 'erase', 0o3471, line=2183)  # VELOCITY VECTOR OF ACTIVE AT CSI TIME
S('RPASS1', 'erase', 0o3477, line=2184)  # POSITION VECTOR OF PASSIVE AT CSI TIME
S('VPASS1', 'erase', 0o3505, line=2185)  # VELOCITY VECTOR OF PASSIVE AT CSI TIME
S('VACT2', 'erase', 0o3513, line=2186)  # VELOCITY VECTOR OF ACTIVE AT CDH TIME
S('RPASS2', 'erase', 0o3521, line=2187)  # POSITION VECTOR OF PASSIVE AT CDH TIME
S('VPASS2', 'erase', 0o3527, line=2188)  # VELOCITY VECTOR OF PASSIVE AT CDH TIME
S('RACT3', 'erase', 0o3535, line=2189)  # POSITION VECTOR OF ACTIVE AT TPI TIME
S('VACT3', 'erase', 0o3543, line=2190)  # VELOCITY VECTOR OF ACTIVE AT TPI TIME
S('RPASS3', 'erase', 0o3551, line=2191)  # POSITION VECTOR OF PASSIVE AT TPI TIME
S('VPASS3', 'erase', 0o3557, line=2192)  # VELOCITY VECTOR OF PASSIVE AT TPI TIME
S('VACT4', 'erase', 0o3565, line=2193)  # VELOCITY VECTOR OF ACTIVE AT INTERCEPT
S('UNVEC', 'equals', 0o3543, line=2194)  # CDHMVR UNIT VECTOR TEMP STORAGE.
S('DELVCSI', 'erase', 0o3573, line=2195)  # THRUST VALUE AT CSI
S('DELVTPI', 'erase', 0o3575, line=2196)  # THRUST VALUE AT TPI OR MID
S('DELVMID', 'equals', 0o3575, line=2197)
S('DIFFALT', 'erase', 0o3577, line=2198)  # ALT DIFFERENT AT CDH
S('POSTCSI', 'erase', 0o3601, line=2199)  # PERIGEE ALTITUDE AFTER CSI MANEUVER
S('POSTCDH', 'erase', 0o3603, line=2200)  # PERIGEE ALTITUDE AFTER CDH MANEUVER
S('POSTTPI', 'erase', 0o3605, line=2201)  # PERIGEE ALTITUDE AFTER TPI MANEUVER
S('LOOPCT', 'equals', 0o3605, line=2202)  # CSI NEWTON ITERATION COUNTER
S('HAFPA1', 'equals', 0o3603, line=2203)  # HALF PERIOD
S('GAMPREV', 'erase', 0o3607, line=2204)  # PREVIOUS GAMMA
S('DVPREV', 'equals', 0o3575, line=2205)  # PREVIOUS DELVCSI
S('DELDV', 'erase', 0o3611, line=2206)
S('CSIALRM', 'erase', 0o3613, line=2207)  # FIRST SOLUTION ALARM
S('VERBNOUN', 'erase', 0o3615, line=2208)
S('TITER', 'equals', 0o3613, line=2209)  # ITERATION COUNTER
S('RDOTV', 'erase', 0o3616, line=2210)
S('VAPREC', 'equals', 0o3505, line=2211)  # I(6) S-S PREC VEC FOR NOM TPI TIME (ACTIVE)
S('RAPREC', 'equals', 0o3477, line=2212)  # I(6) S-S PREC VEC FOR NOM TPI TIME (ACTIVE)
S('VPPREC', 'equals', 0o3527, line=2213)  # I(6) S-S PREC VEC FOR NOM TPI TIME (PASSIVE)
S('RPPREC', 'equals', 0o3521, line=2214)  # I(6) S-S PREC VEC FOR NOM TPI TIME (PASSIVE)
S('DELEL', 'equals', 0o3575, line=2215)  # I(2) S-S
S('DELTEE', 'equals', 0o3611, line=2216)  # I(2) S-S
S('SECMAX', 'equals', 0o3573, line=2217)  # I(2) S-S MAX STOP SIZE FOR ROUTINE
S('DELTEEO', 'equals', 0o3605, line=2218)  # I(2) S-S BACK VALUES OF DELTA TIME
S('CENTANG', 'erase', 0o3620, line=2219)  # I(2) CENTRAL ANGLE COVERED (TPI-TPF)

# Page 142
# SOME P47 STORAGE                              (6D)

S('DELVIMU', 'erase', 0o3622, line=2224)  # I(6)DSP NOUN 83 FOR P47 DELTA V (IMU)

# P30-P40 COMMON STORAGE.                       (3D)

S('TPASS4', 'erase', 0o3630, line=2228)  # INTERCEPT TIME
S('QTEMP', 'erase', 0o3632, line=2229)  # I(1)TMP COMMON RETURN SAVE REGISTER.

# P32,33,34 STORAGE.                            (6D)

S('TCSI', 'erase', 0o3633, line=2233)  # B(2)TMP CSI TIME IN CENTISECONDS
S('TTPI', 'erase', 0o3635, line=2234)  # B(2)TMP TPI TIME IN CENTISECONDS
S('TTPIO', 'erase', 0o3637, line=2235)  # B(2)TMP TTPI STORAGE FOR RECYCLE

# P30,P40 INTERFACE.                            (21D)

S('RTIG', 'erase', 0o3641, line=2239)  # I(6)TMP
S('VTIG', 'equals', 0o3647, line=2240)  # I(6)TMP
S('DELVSIN', 'equals', 0o3655, line=2241)  # I(6)TMP
S('DELVSAB', 'equals', 0o3663, line=2242)  # I(2)TMP
S('VGDISP', 'equals', 0o3663, line=2243)

S('QTEMP1', 'erase', 0o3665, line=2245)  # I(1)TMP HOLDS RETURN.
S('RGEXIT', 'equals', 0o3665, line=2246)  # SAVE Q
S('SAVQR52', 'equals', 0o3665, line=2247)

# INITVEL STORAGE.  (IN OVERLAY 0 AND OVERLAY 1.        (2D)
# (CALLS LAMBERT, CONIC SUBROUTINES)

S('VTPRIME', 'equals', 0o3565, line=2252)  # TOTAL VELOCITY AT DESIRED RADIUS
S('ITCTR', 'equals', 0o3616, line=2253)  # ITERATION COUNTER
S('COZY4', 'erase', 0o3666, line=2254)  # COS OF ANGLE WHEN ROTATION STARTS
S('X1INPUT', 'equals', 0o3611, line=2255)  # X1 TEMP STORAGE
S('INTIME', 'equals', 0o3607, line=2256)  # TIME OF RINIT

# PERIAPO STORAGE.                              (2D)

S('XXXALT', 'erase', 0o3670, line=2260)  # RADIUS TO LAUNCH PAD OR LANDING SITE

S('END-IN/M', 'equals', 0o3672, line=2262)  # NEXT AVAIL ERASABLE AFTER INITVEL/MIDGIM

# Page 143
# S40.1 STORAGE.                                (12D)

S('UT', 'erase', 0o3672, line=2267)  # I(6) THRUST DIRECTION
S('VGTIG', 'equals', 0o3700, line=2268)  # I(6)OUT
S('VGPREV', 'equals', 0o3700, line=2269)

# ASTEER STORAGE.                               (22D)

S('VG', 'erase', 0o3706, line=2273)  # I(6)
S('RMAG', 'equals', 0o3714, line=2274)  # I(2)
S('MUASTEER', 'equals', 0o3716, line=2275)  # I(2)
S('MU/A', 'equals', 0o3720, line=2276)  # I(2)
S('RTMAG', 'equals', 0o3722, line=2277)  # I(2)
S('R1C', 'equals', 0o3724, line=2278)  # I(6)
S('SS', 'equals', 0o3732, line=2279)  # I(2)

S('IC', 'equals', 0o3655, line=2281)
S('TIGSAVE', 'equals', 0o3762, line=2282)
S('TIGSAVEP', 'equals', 0o3764, line=2283)
S('MUSCALE', 'equals', 0o3766, line=2284)

# P40 STORAGE.                                  (6D)

# F, MDOT, AND TDECAY MUST BE CONTIGUOUS FOR WLOAD

S('F', 'erase', 0o3734, line=2290)  # I(2)TMP S40.1 GENERATES THIS FOR S40.3
S('MDOT', 'equals', 0o3736, line=2291)  # I(2)TMP MASS CHNG RATE, KG/CS AT 2**3.
S('TDECAY', 'equals', 0o3740, line=2292)  # I(2)IN DELTA-T TAILOFF, (2**28)CS.
S('VEX', 'erase', 0o3742, line=2293)  # I(2) EXHAUST VELOCITY FOR TGO COMPUTAT'N

# MIDTOAV1(2) STORAGE.  (CALLED BY P40,P41,P42)         (1D)

S('IRETURN1', 'erase', 0o3744, line=2297)  # B(1) RETURN FROM MIDTOAV1 AND 2.

# Page 144
# ******* OVERLAY NUMBER 1 IN EBANK 7 *******

# INITVEL (CALLED BY P34,35,38,39,10,11,S40.9,S40.1)    (6D)

S('RTARG1', 'equals', 0o3471, line=2304)  # I(6)S TEMP STORAGE OF RTARG

# P35-P40 INTERFACE.                            (6D)

S('VPASS4', 'equals', 0o3505, line=2308)  # I(6)TMP VELOCITY OF PASSIVE AT INTERCEPT

# INITVEL OVERLAYS RENDESVOUS GUIDANCE (LISTED IN OVERLAY O)

# SOME P38-30,P78-79 STORAGE                            (2D)
S('TINT', 'equals', 0o3630, line=2313)  # I(2) TIME OF INTERCEPT

# LAT-LONG TEMPORARIES.  CAN OVERLAY WITH S40.1         (3D)

S('ERADM', 'equals', 0o3672, line=2318)  # I(2)
S('INCORPEX', 'equals', 0o3674, line=2319)  # I(1)

# LRS24.1 STORAGE.  (CAN SHARE WITH P30'S)              (40D)

S('RLMSRCH', 'equals', 0o3675, line=2323)  # I(6)TMP LM POSITION VECTOR
S('VXRCM', 'equals', 0o3703, line=2324)  # I(6)    CM V X R VECTOR
S('LOSDESRD', 'equals', 0o3711, line=2325)  # I(6)    DESIRED LOS VECTOR
S('UXVECT', 'equals', 0o3717, line=2326)  # I(6)    X-AXIS SRCH PATTERN COORDS
S('UYVECT', 'equals', 0o3725, line=2327)  # I(6)    Y-AXIS SRCH PATTERN COORDS
S('DATAGOOD', 'equals', 0o3733, line=2328)  # B(1)DSP FOR R1 -- ALL 1-S WHEN LOCKON
S('OMEGDISP', 'equals', 0o3734, line=2329)  # B(2)    ANGLE OMEGA DISPLAYED IN R2
S('OMEGAD', 'equals', 0o3734, line=2330)  #         PINBALL DEFINITION
S('NSRCHPNT', 'equals', 0o3736, line=2331)  # B(1)TMP SEARCH PATTERN POINT COUNTER.
S('SAVLEMV', 'equals', 0o3737, line=2332)  # I(6)S-S SAVES LOSVEL

# Page 145
# ******* OVERLAY NUMBER 2 IN EBANK 7 *******

# INCORP STORAGE IN E7.                         (47D)

S('TX789', 'equals', 0o3471, line=2339)  # I(6)
S('GAMMA', 'equals', 0o3477, line=2340)  # I(3)
S('OMEGA', 'equals', 0o3502, line=2341)  # I(18)
S('BVECTOR', 'equals', 0o3524, line=2342)  # I(18)
S('DELTAQ', 'equals', 0o3546, line=2343)  # I(2)

# AOTMARK STORAGE                               (3D)

S('MARKCNTR', 'equals', 0o3550, line=2347)  # I(1)
S('XYMARK', 'equals', 0o3551, line=2348)  # B(1)
S('MKDEX', 'equals', 0o3552, line=2349)  # B(1)TMP INDEX FOR AOTMARK

# PLANET STORAGE                                (8D)

S('PLANVEC', 'equals', 0o3553, line=2353)  # (6) REFER VECTOR OF PLANET
S('TSIGHT', 'equals', 0o3561, line=2354)  # (2) TIME OF MARK OR EST TIME OF MARK

# LRS22.3 STORAGE.  (CAN SHARE WITH P30'S AND OVERLAY LRS24.1)  (30D)

S('LGRET', 'equals', 0o3675, line=2358)  # I(1)TMP
S('RDRET', 'equals', 0o3675, line=2359)  # B(1) TEMP RETURN.
S('IGRET', 'equals', 0o3675, line=2360)  # B(1) TEMP RETURN.
S('MX', 'equals', 0o3676, line=2361)  # I(6)
S('MY', 'equals', 0o3704, line=2362)  # I(6)
S('MZ', 'equals', 0o3712, line=2363)  # I(6)
S('E0', 'equals', 0o3676, line=2364)  # I(2)
S('E1', 'equals', 0o3700, line=2365)  # I(2)
S('E2', 'equals', 0o3702, line=2366)  # I(2)
S('E3', 'equals', 0o3704, line=2367)  # I(2)
S('SCALSHFT', 'equals', 0o3720, line=2368)  # B(1) SCALE SHIFT FOR EARTH/MOON
S('RXZ', 'equals', 0o3721, line=2369)  # I(2)
S('ULC', 'equals', 0o3723, line=2370)  # I(6)
S('SINTHETA', 'equals', 0o3731, line=2371)  # I(2)

# ***** IN OVERLAY ONE *****

S('N49FLAG', 'equals', 0o3746, line=2375)  # B(1)S FLAG INDICATING V0649 RESPONSE

# LRS22.1 STORAGE.  (MUST NOT SHARE WITH P30'S)         (13D)

# (OUTPUTS ARE TO LRS22.3)

# Page 146
S('RRTRUN', 'equals', 0o3733, line=2382)  # B(2)OUT RR TRUNNION ANGLE
S('RRSHAFT', 'equals', 0o3735, line=2383)  # B(2)OUT RR SHAFT ANGLE
S('LRS22.1X', 'equals', 0o3737, line=2384)  # B(1)TMP
S('RRBORSIT', 'equals', 0o3740, line=2385)  # I(6)TMP RADAR BORESIGHT VECTOR.
S('RDOTMSAV', 'equals', 0o3746, line=2386)  # B(2)S RR RANGE-RATE (FPS)

# LRS22.1 (SAME AS PREVIOUS SECTION) ALSO DOWNLINK FOR RR (R29)         (10D) CANNOT SHARE WITH L.A.D.

S('RDOTM', 'equals', 0o3750, line=2390)  # B(2)OUT RANGE-RATE READING
S('TANGNB', 'equals', 0o3752, line=2391)  # B(2)TMP RR GIMBAL ANGLES
# RETAIN THE ORDER OF MKTIME TO RM FOR DOWNLINK PURPOSES
S('MKTIME', 'equals', 0o3754, line=2393)  # B(2)OUT TIME OF RR READING
S('RM', 'equals', 0o3756, line=2394)  # I(2)OUT RANGE READING
S('RANGRDOT', 'equals', 0o3760, line=2395)  # B(2) DOWNLINKED RAW RANGE AND RRATE

# R61LEM -- PREFERRED TRACKING ATTITUDE ROUTINE **IN OVERLAY ONE**
# (CALLED BY P20, R22LEM, LSR22.3)              (1D)

S('R65CNTR', 'equals', 0o3745, line=2400)  # B(1)SS COUNT NUMBER OF TIMES PREFERRED
# TRACKING ROUTINE IS TO CYCLE
S('WHCHREAD', 'equals', 0o3745, line=2402)  # TELLS WHICH RR DATA TRIGGERED N49 DISPLAY

# P21 STORAGE                                   (2D)

S('P21TIME', 'equals', 0o3762, line=2406)  # I(2)TMP

# KALCMANU, VECPOINT STORAGE.  CALLED BY R63, R61, R65.         (12D)

S('SCAXIS', 'equals', 0o3764, line=2410)  # I(6)
S('POINTVSM', 'equals', 0o3772, line=2411)  # I(6)
# Page 147
# ******* OVERLAY NUMBER 3 IN EBANK 7 *******

# SERVICER STORAGE                              (6D)

S('ABVEL', 'equals', 0o3471, line=2418)  # B(2) DISPLAY
S('HDOTDISP', 'equals', 0o3473, line=2419)  # B(2) DISPLAY
S('TTFDISP', 'equals', 0o3475, line=2420)  # B(2) DISPLAY

# BURN PROG STORAGE.                            (2D)

S('SAVET-30', 'equals', 0o3477, line=2424)  # B(2)TMP TIG-30 RESTART

# SERVICER STORAGE.                             (69D)

S('VGBODY', 'equals', 0o3501, line=2428)  # B(6)OUT SET BY S41.1 VG LEM, SC.COORDS
S('DELVCTL', 'equals', 0o3501, line=2429)
S('DVTOTAL', 'equals', 0o3507, line=2430)  # B(2) DISPLAY NOUN
S('GOBLTIME', 'equals', 0o3511, line=2431)  # B(2) NOMINAL TIG FOR CALC. OF GOBLATE.
S('ABDVCONV', 'equals', 0o3513, line=2432)  # I(2)
S('DVCNTR', 'equals', 0o3515, line=2433)  # B(1)
S('TGO', 'equals', 0o3516, line=2434)  # B(2)
S('R', 'equals', 0o3520, line=2435)  # I(6)
S('UNITGOBL', 'equals', 0o3520, line=2436)  # I(6)
S('V', 'equals', 0o3526, line=2437)
S('DELVREF', 'equals', 0o3526, line=2438)  # I(6)
S('HCALC', 'equals', 0o3534, line=2439)  # B(2) LR
S('UNIT/R/', 'equals', 0o3536, line=2440)  # I(6)

# (THE FOLLOWING SERVICER ERASABLES CAN BE SHARED WITH SECOND DPS GUIDANCE STORAGE)

S('RN1', 'equals', 0o3544, line=2444)  # B(6)
S('VN1', 'equals', 0o3552, line=2445)  # I(6)          ( IN ORDER )
S('PIPTIME1', 'equals', 0o3560, line=2446)  # B(2)          (    FOR   )
S('GDT1/2', 'equals', 0o3562, line=2447)  # I(6)          (   COPY   )
S('MASS1', 'equals', 0o3570, line=2448)  # I(2)          (   CYCLE  )
S('R1S', 'equals', 0o3572, line=2449)  # I(6)
S('V1S', 'equals', 0o3600, line=2450)  # I(6)

# ALIGNMENT/S40.2,3 COMMON STORAGE.             (18D)

S('XSMD', 'equals', 0o3606, line=2454)  # I(6)
S('YSMD', 'equals', 0o3614, line=2455)  # I(6)
S('ZSMD', 'equals', 0o3622, line=2456)  # I(6)

S('XSCREF', 'equals', 0o3606, line=2458)
S('YSCREF', 'equals', 0o3614, line=2459)
# Page 148
S('ZSCREF', 'equals', 0o3622, line=2461)

S('END-ALIG', 'equals', 0o3630, line=2463)  # NEXT AVAIL ERASABLE AFTER ALIGN/S40.2,3

# ****** P22 ******                             (24D)

S('RSUBL', 'equals', 0o3630, line=2467)  # I(6)S-S       LM POSITION VECTOR
S('UCSM', 'equals', 0o3636, line=2468)  # I(6)S-S       VECTOR U
S('NEWVEL', 'equals', 0o3644, line=2469)  # I(6)S-S       TERMINAL VELOCITY VECTOR
S('NEWPOS', 'equals', 0o3652, line=2470)  # I(6)S-S       TERMINAL POSITION VECTOR
S('LNCHTM', 'equals', 0o3660, line=2471)  # I(2)S-S       EST. LAUNCH TIME FOR LEM
S('TRANSTM', 'equals', 0o3662, line=2472)  # I(2)S-S       TRANSFER TIME
S('NCSMVEL', 'equals', 0o3664, line=2473)  # I(6)S-S       NEW CSM VELOCITY

# ****** P21 ******                             (18D)

S('P21ORIG', 'equals', 0o1163, line=2477)
S('P21BASER', 'equals', 0o3675, line=2478)  # I(6)TMP
S('P21BASEV', 'equals', 0o3703, line=2479)  # I(6)TMP
S('P21VEL', 'equals', 0o3711, line=2480)  # I(2)TMP       *** NOUN 91 ***
S('P21GAM', 'equals', 0o3713, line=2481)  # I(2)TMP       *** NOUN 91 ***
S('P21ALT', 'equals', 0o3715, line=2482)  # I(2)TMP       *** NOUN 91 ***

# Page 149
# ******* OVERLAY NUMBER 4 IN EBANK 7 *******

# VARIABLES FOR SECOND DPS GUIDANCE (THE LUNAR LANDING)         (18D)

# THESE ERASABLES MAY BE SHARED WITH CARE

S('OURTEMPS', 'equals', 0o3544, line=2491)  # OVERLAY LAST PART OF SERVICER
S('LANDTEMP', 'equals', 0o3544, line=2492)  # B(6)  GUIDANCE
S('TTF/8TMP', 'equals', 0o3552, line=2493)  # B(2)  GUIDANCE
S('ELINCR', 'equals', 0o3554, line=2494)  # B(2)  GUIDANCE
S('AZINCR', 'equals', 0o3556, line=2495)  # B(2)  GUIDANCE
S('KEEP-2', 'equals', 0o3560, line=2496)  # B(2)  TP PREVENT PIPTIME1 OVERLAY
S('TABLTTF', 'equals', 0o3562, line=2497)  # B(2)  GUIDANCE
S('TPIPOLD', 'equals', 0o3573, line=2498)  # B(2)  GUIDANCE
S('E2DPS', 'equals', 0o3621, line=2499)

# THESE ERASABLES MUST NOT OVERLAY GOBLTIME OR SERVICER

S('PIFPSET', 'equals', 0o3606, line=2503)  # B(1)  THROTTLE
S('RTNHOLD', 'equals', 0o3607, line=2504)  # B(1)  THROTTLE
S('FWEIGHT', 'equals', 0o3610, line=2505)  # B(2)  THROTTLE
S('PIF', 'equals', 0o3612, line=2506)  # B(2)  THROTTLE
S('PSEUDO55', 'equals', 0o3614, line=2507)  # B(1)  THROTTLE DOWNLINK
S('FC', 'equals', 0o3615, line=2508)  # B(2)  THROTTLE
S('TTHROT', 'equals', 0o3617, line=2509)  # B(1)  THROTTLE
S('FCOLD', 'equals', 0o3620, line=2510)  # B(1)  THROTTLE

# THESE ERASABLES SHOULD NOT BE SHARED DURING P63, P64, P65, P66, P67

S('OURPERMS', 'equals', 0o3621, line=2514)  # MUSTN'T OVERLAY OURTEMPS OR SERVICER
S('WCHPHOLD', 'equals', 0o3621, line=2515)  # B(1)  GUIDANCE
S('FILLER', 'equals', 0o3622, line=2516)
S('FLPASS0', 'equals', 0o3623, line=2517)  # B(1)  GUIDANCE
S('TPIP', 'equals', 0o3624, line=2518)  # B(2)
S('VGU', 'equals', 0o3626, line=2519)  # B(6)  GUIDANCE
S('LAND', 'equals', 0o3634, line=2520)  # B(6)  GUIDANCE        CONTIGUOUS
S('TTF/8', 'equals', 0o3642, line=2521)  # B(2)  GUIDANCE        CONTIGUOUS
S('ELIDUMMY', 'equals', 0o3644, line=2522)  # (1)   DUMMY FOR ELINCR1
S('AZIDUMMY', 'equals', 0o3645, line=2523)  # (1)   DUMMY FOR AZINCR1
S('ZERDUMMY', 'equals', 0o3646, line=2524)  # (1)   DUMMY FOR ZERLINA
S('ELVDUMMY', 'equals', 0o3647, line=2525)  # (1)   DUMMY FOR ELVIRA
S('LRADRET', 'equals', 0o3650, line=2526)  # B(1)  LR
S('VSELECT', 'equals', 0o3651, line=2527)  # B(1)  LR
S('VMEAS', 'equals', 0o3652, line=2528)  # B(2)  LR
S('HMEAS', 'equals', 0o3654, line=2529)  # B(2)  LR
S('VN2', 'equals', 0o3656, line=2530)  # B(6)  LR
# Page 150
S('GNUR', 'equals', 0o3656, line=2532)  # B(6)  LR
S('GNUV', 'equals', 0o3656, line=2533)  # B(6)  LR
S('LRADRET1', 'equals', 0o3656, line=2534)  # B(1)  LR
S('DELTAH', 'equals', 0o3664, line=2535)  # B(2)  DISPLAY
S('FUNNYDSP', 'equals', 0o3666, line=2536)  # B(2)  DISPLAY
S('EOURPERM', 'equals', 0o3670, line=2537)  # NEXT AVAILABLE ERASABLE AFTER OURPERMS

# (ERASABLES WHICH OVERLAY THE ABOVE BLOCK)

S('VDGVERT', 'equals', 0o3644, line=2541)  # B(2)  P65,P66
S('NIGNLOOP', 'equals', 0o3646, line=2542)  # B(1)  IGNALG
S('NGUIDSUB', 'equals', 0o3647, line=2543)  # B(1)  IGNALG
S('WCHVERT', 'equals', 0o3647, line=2544)  # B(1)  P65,P66,P67
S('FUELNEED', 'equals', 0o3666, line=2545)  # B(1)  DISPLAY
S('TREDES', 'equals', 0o3666, line=2546)  # B(1)  DISPLAY
S('LOOKANGL', 'equals', 0o3667, line=2547)  # B(1)  DISPLAY

# ERASABLES CONVENIENTLY DEFINABLE IN THE WORK AREA

S('PROJ', 'equals', 0o22, line=2551)  # I(2)  GUIDANCE
S('UNLRB/2', 'equals', 0o24, line=2552)  # I(6)  GUIDANCE (DURING P64 ONLY)
S('UNLR/2', 'equals', 0o24, line=2553)  # I(6)  GUIDANCE

# THE END OF THE LUNAR LANDING ERASABLES

# R12 (FOR LUNAR LANDING)                       (6D)

S('LRLCTR', 'equals', 0o3670, line=2559)  # B(1) LR DATA TEST
S('LRRCTR', 'equals', 0o3671, line=2560)  # B(1)
S('LRMCTR', 'equals', 0o3672, line=2561)  # B(1)
S('LRSCTR', 'equals', 0o3673, line=2562)  # B(1)
S('STILBADH', 'equals', 0o3674, line=2563)  # B(1)
S('STILBADV', 'equals', 0o3675, line=2564)  # B(1)

# LANDING ANALOGS DISPLAY STORAGE.              (40D)

S('LATVMETR', 'equals', 0o3676, line=2568)  # B(1)PRM LATVEL MONITOR METER (AN ORDER)
S('FORVMETR', 'equals', 0o3677, line=2569)  # B(1)PRM FORVEL MONITOR METER (-ED PAIR)
S('LATVEL', 'equals', 0o3700, line=2570)  # B(1)PRM LATERAL VELOCITY (AN ORDER)
S('FORVEL', 'equals', 0o3701, line=2571)  # B(1)PRM FORWARD VELOCITY (-ED PAIR)
S('TRAKLATV', 'equals', 0o3702, line=2572)  # B(1)PRM MONITOR FLG 4 LATVEL (AN ORDER)
S('TRAKFWDV', 'equals', 0o3703, line=2573)  # B(1)PRM MONIT. FLAG FOR FORVEL (ED PAIR)
S('VHY', 'equals', 0o3704, line=2574)  # B(1)PRM VHY=VMP.UHYP (AN ORDER)
# Page 151
S('VHZ', 'equals', 0o3705, line=2576)  # B(1)PRM VHZ=VMP.UHZP (-ED PAIR)
S('VVECT', 'equals', 0o3706, line=2577)  # B(3)PRM UPDATED S.P. VELOCITY VECTOR
S('ALTRATE', 'equals', 0o3711, line=2578)  # B(1)PRM ALTITUDE RATE IN BIT UNITS
S('ALTSAVE', 'equals', 0o3712, line=2579)  # B(2)PRM ALTITUDE IN BIT UNITS
S('LADQSAVE', 'equals', 0o3714, line=2580)  # B(1)PARM SAVE Q IN LAND1SP
S('DT', 'equals', 0o3715, line=2581)  # B(1)PRM TIME 1 MINUS (PIPTIME +1)
S('DALTRATE', 'equals', 0o3716, line=2582)  # B(1)PRM ALTITUDE RATE ERROR CORRECTION
S('UHYP', 'equals', 0o3717, line=2583)  # B(6)PRM SM UNIT VECTOR
S('QAXIS', 'equals', 0o3717, line=2584)
S('UHZP', 'equals', 0o3725, line=2585)  # B(6)PRM SM UNIT VECTOR
S('DELVS', 'equals', 0o3733, line=2586)  # B(6)PRM DELVS = WMXR
S('ALTBITS', 'equals', 0o3741, line=2587)  # B(2)PRM ALTITUDE IN BIT UNITS. 2.34 FT/BIT
S('RUNIT', 'equals', 0o3743, line=2588)  # B(3)PRM SM HALF-UNIT R VECTOR
S('LASTLADW', 'equals', 0o3745, line=2589)  # ONLY A TAG TO SIGNIFY LAST L.A.D. WORD

# P66 ERASABLES (R.O.D.)                        (1D)

S('RODCOUNT', 'equals', 0o3746, line=2593)

# P66 ERASABLES (R.O.D.)                        (14D)

S('RODSCAL1', 'equals', 0o3756, line=2597)  # B(1)
S('LASTTPIP', 'equals', 0o3757, line=2598)  # I(2)
S('THISTPIP', 'equals', 0o3761, line=2599)  # B(2)
S('OLDPIPAX', 'equals', 0o3763, line=2600)  # B(1)
S('OLDPIPAY', 'equals', 0o3764, line=2601)  # B(1)
S('OLDPIPAZ', 'equals', 0o3765, line=2602)  # B(1)
S('DELVROD', 'equals', 0o3766, line=2603)  # B(6)

# NOUN 63 COMPONENT                             (2D)

S('HCALC1', 'equals', 0o3774, line=2607)  # I(2)

# Page 152
# ******* OVERLAY NUMBER 5 IN EBANK 7 *******

# ASCENT GUIDANCE ERASABLES.                    (21D)

S('RCO', 'equals', 0o3630, line=2614)  # I(2)TMP TARGET RADIUS AND OUT-OF-PLANE
S('YCO', 'equals', 0o3632, line=2615)  # I(2)TMP DISTANCE, SCALED AT 2(24).
S('1/DV1', 'equals', 0o3634, line=2616)  # B(2)TMP ATMAG
S('1/DV2', 'equals', 0o3636, line=2617)  # B(2)TMP ATMAG
S('1/DV3', 'equals', 0o3640, line=2618)  # B(2)TMP ATMAG
S('XRANGE', 'equals', 0o3642, line=2619)  # B(2)TMP
S('ENGOFFDT', 'equals', 0o3644, line=2620)  # B(1)TMP
S('VGVECT', 'equals', 0o3645, line=2621)  # I(6)OUT VELOCITY-TO-BE-GAINED.
S('TXO', 'equals', 0o3653, line=2622)  # I(2)TMP TIME AT WHICH X-AXIS OVERRIDE
# IS ALLOWED.

# END OF THE ASCENT GUIDANCE ERASABLES

# THE FOLLOWING CARDS KEEP THE ASSEMBLER HAPPY UNTIL THE SYMBOLS ARE DELETED FROM THE PINBALL NOUN TABLES.

S('END-E7.0', 'equals', 0o3745, line=2629)  # FIRST UNUSED LOCATION IN E7 OVERLAY 0
S('END-E7.1', 'equals', 0o3747, line=2630)  # FIRST UNUSED LOCATION IN E7 OVERLAY 1
S('END-E7.2', 'equals', 0o4000, line=2631)  # FIRST UNUSED LOCATION IN E7 OVERLAY 2
S('END-E7.3', 'equals', 0o3630, line=2632)  # FIRST UNUSED LOCATION IN E7 OVERLAY 3
S('END-E7.4', 'equals', 0o3777, line=2633)  # ** LAST LOCATION USED IN E7 OVERLAY 4 **
S('END-E7.5', 'equals', 0o3655, line=2634)  # FIRST UNUSED LOCATION IN E7 OVERLAY 5
S('END-E7', 'equals', 0o3777, line=2635)  # ** LAST LOCATION USED IN E7 **
