"""TVCMASSPROP.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/TVCMASSPROP.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 951-955 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TVCMASSPROP', 'TVCMASSPROP.agc', 'Comanche055', pages='951-955')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TVCMASSPROP.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        951-955
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

# Page 951
# PROGRAM NAME....MASSPROP
# LOG SECTION....TVCMASSPROP            PROGRAMMER...MELANSON (ENGEL, SCHLUNDT)
#
#
# FUNCTIONAL DESCRIPTION:
#
# MASSPROP OPERATES IN TWO MODES:(1)IF LEM MASS OR CONFIGURATION ARE UPDATED (MASSPROP DOES NOT TEST
# FOR THIS) THE ENTIRE PROGRAM MUST BE RUN THROUGH, BREAKPOINT VALUES AND DERIVATIVES OF THE OUTPUTS WITH
# RESPECT TO CSM MASS BEING CALCULATED PRIOR TO CALCULATION OF THE OUTPUTS.  (2)OTHERWISE, THE OUTPUTS CAN BE
# CALCULATED USING PREVIOUSLY COMPUTED BREAKPOINT VALUES AND DERIVATIVES.
#
# CALLING SEQUENCES
#
# IF LEM MASS OR CONFIGURATION HAS BEEN UPDATED, TRANSFER TO MASSPROP, OTHERWISE TRANSFER TO FIXCW.
# L       TC      BANKCALL OR IBNKCALL
# L+1     CADR    MASSPROP
# OR
# L+1     CADR    FIXCW
#
# L+2     RETURNS VIA Q
#
# CALLED        IN PARTICULAR BY DONOUN47 (JOB) AND TVCEXECUTIVE (TASK)
#
# JOBS OR TASKS INITIATED - NONE
#
# SUBROUTINES CALLED - NONE
#
# ERASABLE INITIALIZATION REQUIRED
#
# LEMMASS MUST CONTAIN LEM MASS SCALED AT B+16 KILOGRAMS
# CSMMASS MUST CONTAIN CSM MASS SCALED AT B+16 KILOGRAMS
#
# DAPDATR1 MUST BE SET TO INDICATE VEHICLE CONFIGURATION.
# BITS (15,14,13)  =  ( 0 , 0 , 1 )       LEM OFF
# ( 0 , 1 , 0 )       LEM ON (ASCNT,DSCNT)
# ( 1 , 1 , 0 )       LEM ON (ASCNT ONLY)
#
#
# ALARMS -      NONE
#
# EXIT -        TC      Q
#
# OUTPUTS:
#
# (1)IXX, SINGLE PRECISION SCALED AT B+20 IN KG-M SQ.
# (2)IAVG, SINGLE PRECISION SCALED AT B+20 IN KG-M SQ.
# (3)IAVG/TLX, SINGLE PRECISION, SCALED AT B+2 SEC-SQD
# THEY ARE STORED IN CONSECUTIVE REGISTERS IXX0, IXX1, IXX2
#
# CONVERSION FACTOR :  (SLUG-FTSQ) = 0.737562 (KG-MSQ)
# Page 952
#
# OUTPUTS ARE CALCULATED AS FOLLOWS:
#
# (1) IF LEM DOCKED, LEMMASS IS FIRST ELIMINATED AS A PARAMETER
#
# VARST0 = INTVALUE0 + LEMMASS(SLOPEVAL0)         IXX             BREAKPOINT VALUE
# VARST1 = INTVALUE1 + LEMMASS(SLOPEVAL1)         IAVG            BREAKPOINT VALUE
# VARST2 = INTVALUE2 + LEMMASS(SLOPEVAL2)         IAVG/TLX        BREAKPOINT VALUE
#
# VARST3 = INTVALUE3 + LEMMASS(SLOPEVAL3)         IAVG/TLX        SLOPE FOR CSMMASS > 33956 LBS ( SPS > 10000 LBS)
# VARST4 = INTVALUE4 + LEMMASS(SLOPEVAL4)         IAVG            SLOPE FOR CSMMASS > 33956 LBS ( SPS > 10000 LBS)
#
# VARST5 = INTVALUE5 + LEMMASS(SLOPEVAL5)         IXX             SLOPE FOR ALL VALUES OF CSMMASS
#
# VARST6 = INTVALUE6 + LEMMASS(SLOPEVAL6)         IAVG            SLOPE FOR CSMMASS < 33956 LBS ( SPS < 10000 LBS)
# VARST7 = INTVALUE7 + LEMMASS(SLOPEVAL7)         IAVG/TLX        SLOPE FOR CSMMASS < 33956 LBS ( SPS < 10000 LBS)
#
# VARST8 = INTVALUE8 + LEMMASS(SLOPEVAL8)         IAVG            DECREMENT TO BRKPT VALUE WHEN LEM DSCNT STAGE OFF
# VARST9 = INTVALUE9 + LEMMASS(SLOPEVAL9)         IAVG/TLX        DECREMENT TO BRKPT VALUE WHEN LEM DSCNT STAGE OFF
#
# (2) IF LEM NOT DOCKED
#
# VARST0 = NOLEMVAL0      WHERE THE MEANING AND SCALING OF VARST0
# .       .       TO VARST9 ARE THE SAME AS GIVEN ABOVE
# .       .
# .       .       NOTE... FOR THIS CASE, VARST8,9 HAVE NO
# VARST9 = NOLEMVAL9      MEANING (THEY ARE COMPUTED BUT NOT USED)
#
# (3) THE FINAL OUTPUT CALCULATIONS ARE THEN DONE
#
# IXX0 = VARST0 + (CSMMASS + NEGBPW)VARST5                IXX
#
# IXX1 = VARST1 + (CSMMASS + NEGBPW)VARST(4 OR 6)         IAVG
#
# IXX2 = VARST2 + (CSMMASS + NEGBPW)VARST(3 OR 7)         IAVG/TLX
#
#
# THE DATA USED CAME FROM CSM/LM SPACECRAFT OPERATIONAL DATA BOOK.
# VOL. 3, NASA DOCUMENT SNA-8-D-027 (MARCH 1968)
#
# PERTINENT MASS DATA :         CSM WEIGHT      (FULL)  64100 LBS.
# (EMPTY) 23956 LBS.
# LEM WEIGHT      (FULL)  32000 LBS.
# (EMPTY) 14116 LBS.
#
# (WEIGHTS ARE FROM AMENDMENT #1 (APRIL 24,1968) TO ABOVE DATA BOOK)
# Page 953

#   BANK 25
#   SETLOC DAPMASS
#   BANK
#   EBANK= BZERO
#   COUNT* $$/MASP

W('05,3366', 0o34334, 'MASSPROP', 'CAF', 'NINE', 'MASSPROP USES TVC/RCS INTERRUPT TEMPS', line=137)
W('05,3367', 0o55506, '', 'TS', 'PHI333', 'SET UP TEN PASSES', line=138)

W('05,3370', 0o31466, 'LEMTEST', 'CAE', 'DAPDATR1', 'DETERMINE LEM STATUS', line=140)
W('05,3371', 0o75003, '', 'MASK', 'BIT13', line=141)
W('05,3372', 0o00006, '', 'EXTEND', line=142)
W('05,3373', 0o13377, '', 'BZF', 'LEMYES', line=143)

W('05,3374', 0o51506, 'LEMNO', 'INDEX', 'PHI333', 'LEM NOT ATTACHED', line=145)
W('05,3375', 0o33463, '', 'CAF', 'NOLEMVAL', line=146)
W('05,3376', 0o13407, '', 'TCF', 'STOINST', line=147)

W('05,3377', 0o31473, 'LEMYES', 'CAE', 'LEMMASS', 'LEM IS ATTACHED', line=149)
W('05,3400', 0o60000, '', 'DOUBLE', line=150)
W('05,3401', 0o00006, '', 'EXTEND', line=151)
W('05,3402', 0o51506, '', 'INDEX', 'PHI333', line=152)
W('05,3403', 0o73505, '', 'MP', 'SLOPEVAL', line=153)
W('05,3404', 0o20001, '', 'DDOUBL', line=154)
W('05,3405', 0o51506, '', 'INDEX', 'PHI333', line=155)
W('05,3406', 0o63473, '', 'AD', 'INTVALUE', line=156)

W('05,3407', 0o51506, 'STOINST', 'INDEX', 'PHI333', 'STORAGE INST BEGIN HERE', line=158)
W('05,3410', 0o55511, '', 'TS', 'VARST0', line=159)
W('05,3411', 0o11506, '', 'CCS', 'PHI333', 'ARE ALL TEN PASSES COMPLETED', line=160)
W('05,3412', 0o13367, '', 'TCF', 'MASSPROP +1', 'NO - GO DECREMENT PHI333', line=161)

W('05,3413', 0o11466, 'DXTEST', 'CCS', 'DAPDATR1', 'IF NEG, BIT15 IS 1, LEM DSCNT STAGE OFF', line=163)
W('05,3414', 0o13422, '', 'TCF', 'FIXCW', line=164)
W('05,3415', 0o13422, '', 'TCF', 'FIXCW', line=165)
W('05,3416', 0o53522, '', 'DXCH', 'VARST0 +8D', line=166)
W('05,3417', 0o21513, '', 'DAS', 'VARST0 +1', line=167)
W('05,3420', 0o33520, '', 'CA', 'DXITFIX', line=168)
W('05,3421', 0o27520, '', 'ADS', 'VARST0 +7', line=169)

W('05,3422', 0o35016, 'FIXCW', 'CAF', 'BIT2', 'COMPUTATION PHASE BEGINS HERE.  SET UP', line=171)
W('05,3423', 0o55506, '', 'TS', 'PHI333', 'THREE PASSES', line=172)
W('05,3424', 0o55507, '', 'TS', 'PSI333', line=173)

W('05,3425', 0o31474, '', 'CAE', 'CSMMASS', 'GET DELTA CSM WEIGHT - SIGN DETERMINES', line=175)
W('05,3426', 0o63517, '', 'AD', 'NEGBPW', 'SLOPE LOCATIONS.', line=176)
W('05,3427', 0o60000, '', 'DOUBLE', line=177)
W('05,3430', 0o55510, '', 'TS', 'TEMP333', line=178)
# Page 954
W('05,3431', 0o00006, '', 'EXTEND', line=180)
W('05,3432', 0o63435, '', 'BZMF', 'PEGGY', 'DETERMINE CORRECT SLOPE', line=181)
W('05,3433', 0o37715, '', 'CAF', 'NEG2', line=182)
W('05,3434', 0o55506, '', 'TS', 'PHI333', line=183)

W('05,3435', 0o51506, 'PEGGY', 'INDEX', 'PHI333', 'ALL IS READY - CALCULATE OUTPUTS NOW', line=185)
W('05,3436', 0o31516, '', 'CAE', 'VARST5', 'GET SLOPE', line=186)
W('05,3437', 0o00006, '', 'EXTEND', line=187)
W('05,3440', 0o71510, '', 'MP', 'TEMP333', 'MULT BY DELTA CSM WEIGHT', line=188)
W('05,3441', 0o60000, '', 'DOUBLE', line=189)
W('05,3442', 0o51507, '', 'INDEX', 'PSI333', line=190)
W('05,3443', 0o61511, '', 'AD', 'VARST0', 'ADD BREAKPOINT VALUE', line=191)
W('05,3444', 0o51507, '', 'INDEX', 'PSI333', line=192)
W('05,3445', 0o55470, '', 'TS', 'IXX', '****** OUTPUTS (IXX0, IXX1, IXX2) ******', line=193)

W('05,3446', 0o11507, '', 'CCS', 'PSI333', 'BOOKKEEPING - MASSPROP FINISHED OR NOT', line=196)
W('05,3447', 0o13457, '', 'TCF', 'BOKKEP2', 'NO - GO TAKE CARE OF INDEXING REGISTERS', line=197)

W('05,3450', 0o31466, '', 'CAE', 'DAPDATR1', 'UPDATE WEIGHT/G', line=199)
W('05,3451', 0o75002, '', 'MASK', 'BIT14', line=200)
W('05,3452', 0o10000, '', 'CCS', 'A', line=201)
W('05,3453', 0o31473, '', 'CA', 'LEMMASS', line=202)
W('05,3454', 0o61474, '', 'AD', 'CSMMASS', line=203)
W('05,3455', 0o55475, '', 'TS', 'WEIGHT/G', 'SCALED AT B+16 KILOGRAMS', line=204)
W('05,3456', 0o00002, 'ENDMASSP', 'TC', 'Q', line=205)

W('05,3457', 0o55507, 'BOKKEP2', 'TS', 'PSI333', 'REDUCE PSI BY ONE', line=207)
W('05,3460', 0o00006, '', 'EXTEND', line=208)
W('05,3461', 0o27506, '', 'DIM', 'PHI333', line=209)
W('05,3462', 0o13435, '', 'TCF', 'PEGGY', line=210)

# Page 955
W('05,3463', 0o00616, 'NOLEMVAL', 'DEC', '25445 B-20', kind='data', line=213)
W('05,3464', 0o02526, '', 'DEC', '87450 B-20', kind='data', line=214)
W('05,3465', 0o02352, '', 'DEC', '.30715 B-2', kind='data', line=215)
W('05,3466', 0o01471, '', 'DEC', '1.22877 E-5 B+12', kind='data', line=216)
W('05,3467', 0o00634, '', 'DEC', '1.6096 B-6', kind='data', line=217)
W('05,3470', 0o00612, '', 'DEC', '1.54 B-6', kind='data', line=218)
W('05,3471', 0o03706, '', 'DEC', '7.77177 B-6', kind='data', line=219)
W('05,3472', 0o04425, '', 'DEC', '3.46458 E-5 B+12', kind='data', line=220)

W('05,3473', 0o00644, 'INTVALUE', 'DEC', '26850 B-20', kind='data', line=222)
W('05,3474', 0o03710, '', 'DEC', '127518 B-20', kind='data', line=223)
W('05,3475', 0o04246, '', 'DEC', '.54059 B-2', kind='data', line=224)
W('05,3476', 0o02011, '', 'DEC', '.153964 E-4 B+12', kind='data', line=225)
W('05,3477', 0o77501, '', 'DEC', '-.742923 B-6', kind='data', line=226)
W('05,3500', 0o00612, '', 'DEC', '1.5398 B-6', kind='data', line=227)
W('05,3501', 0o04656, '', 'DEC', '9.68 B-6', kind='data', line=228)
W('05,3502', 0o10372, '', 'DEC', '.647625 E-4 B+12', kind='data', line=229)
W('05,3503', 0o77126, '', 'DEC', '-27228 B-20', kind='data', line=230)
W('05,3504', 0o76261, '', 'DEC', '-.206476 B-2', kind='data', line=231)

W('05,3505', 0o00767, 'SLOPEVAL', 'DEC', '1.96307 B-6', kind='data', line=233)
W('05,3506', 0o15624, '', 'DEC', '27.5774 B-6', kind='data', line=234)
W('05,3507', 0o03054, '', 'DEC', '2.3548 E-5 B+12', kind='data', line=235)
W('05,3510', 0o04532, '', 'DEC', '2.1777 E-9 B+26', kind='data', line=236)
W('05,3511', 0o10433, '', 'DEC', '1.044 E-3 B+8', kind='data', line=237)
W('05,3512', 0o00000, '', 'DEC', '0', kind='data', line=238)
W('05,3513', 0o22070, '', 'DEC', '2.21068 E-3 B+8', kind='data', line=239)
W('05,3514', 0o03204, '', 'DEC', '1.5166 E-9 B+26', kind='data', line=240)
W('05,3515', 0o77266, '', 'DEC', '-1.284 B-6', kind='data', line=241)
W('05,3516', 0o02476, '', 'DEC', '2 E-5 B+12', kind='data', line=242)

W('05,3517', 0o70364, 'NEGBPW', 'DEC', '-15402.17 B-16', kind='data', line=244)
W('05,3520', 0o75420, 'DXITFIX', 'DEC*', '-1.88275 E-5 B+12*', kind='data', line=245)
