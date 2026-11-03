"""R60_62.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/R60_62.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 472-485 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('R60_62', 'R60_62.agc', 'Luminary099', pages='472-485')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     R60_R62.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        472-485
# Mod history:  2009-05-17 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
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

# Page 472
# MOD NO: 0                     DATE: 1 MAY 1968
# MOD BY: DIGITAL DEVEL GROUP   LOG SECTION R60,R62
#
# FUNCTIONAL DESCRIPTION:
#
# CALLED AS A GENERAL SUBROUTINE TO MANEUVER THE LM TO A SPECIFIED
# ATTITUDE.
#
# 1. IF THE 3-AXIS FLAG IS NOT SET THE FINAL CDU ANGLES ARE
# CALCULATED (VECPOINT).
#
# 2. THE FDAI BALL ANGLES (NOUN 18) ARE CALCULATED (BALLANGS).
#
# 3. REQUEST FLASHING DISPLAY V50 N18 PLEASE PERFORM AUTO MANEUVER.
#
# 4. IF PRIORITY DISPLAY FLAG IS SET DO A PHASECHANGE. THEN AWAIT
# ASTRONAUT RESPONSE.
#
# 5. DISPLAY RESPONSE RETURNS:
#
# A. ENTER - RESET 3-AXIS FLAG AND RETURN TO CLIENT.
#
# B. TERMINATE - IF IN P00 GO TO STEP 5A. OTHERWISE CHECK IF R61 IS
# THE CALLING PROGRAM. IF IN R61 AN EXIT IS MADE TO GOTOV56. IF
# NOT IN R61 AN EXIT IS DONE VIA GOTOPOOH.
#
# C. PROCEED - CONTINUE WITH PROGRAM AT STEP 6.
#
# 6. IF THE 3-AXISFLAG IS NOT SET, THE FINAL CDU ANGLES ARE CALCULATED
# (VECPOINT).
#
# 7. THE FDAI BALL ANGLES (NOUN 18) ARE CALCULATED (BALLANGS).
#
# 8. IF THE G+N SWITCH IS NOT SET GO BACK TO STEP 3.
#
# 9. IF THE AUTO SWITCH IS NOT SET GO BACK TO STEP 3.
#
# 10. NONFLASHING DISPLAY V06N18 (FDAI ANGLES).
#
# 11. DO A PHASECHANGE.
#
# 12. DO A MANEUVER CALCULATION AND ICDU DRIVE ROUTINE TO ACHIEVE FINAL
#
# GIMBAL ANGLES (GOMANUR).
# 13. AT END OF MANEUVER GO TO STEP 3.
#
# IF SATISFACTORY MANEUVER STEP 5A EXITS R60.
# FOR FURTHER ADJUSTMENT OF THE VEHICLE ATTITUDE ABOUT THE
# DESIRED VECTOR, THE ROUTINE MAY BE PERFORMED AGAIN STARTING AT
# Page 473
# STEP 5C.
#
# CALLING SEQUENCE:  TC BANKCALL
# CADR R60LEM
#
# ERASABLE INITIALIZATION REQUIRED : SCAXIS, POINTVSM (FOR VECPOINT)
# 3AXISFLG.
#
# SUBROUTINES CALLED: VECPOINT, BALLANGS, GOPERF2R, LINUS, GODSPER,
# GOMANUR, DOWNFLAG, PHASCHNG, UPFLAG
#
# NORMAL EXIT MODES: CAE TEMPR60   (CALLERS RETURN ADDRESS)
# TC  BANKJUMP
#
# ALARMS: NONE
#
# OUTPUT: NONE
#
# DEBRIS: CPHI, CTHETA, CPSI, 3AXISFLG, TBASE2

#   BANK 34
#   SETLOC MANUVER
#   BANK

#   EBANK= TEMPR60

#   COUNT* $$/R06
W('26,2123', 0o04645, 'R60LEM', 'TC', 'MAKECADR', line=107)
W('26,2124', 0o55164, '', 'TS', 'TEMPR60', line=108)

W('26,2125', 0o34746, 'REDOMANN', 'CAF', '3AXISBIT', line=110)
W('26,2126', 0o70101, '', 'MASK', 'FLAGWRD5', 'IS 3-AXIS FLAG SET', line=111)
W('26,2127', 0o10000, '', 'CCS', 'A', line=112)
W('26,2130', 0o12136, '', 'TCF', 'TOBALL', 'YES', line=113)
W('26,2131', 0o06037, '', 'TC', 'INTPRET', line=114)
W('26,2132', 0o77624, '', 'CALL', kind='interp', line=115)
W('26,2133', 0o56040, '', '', 'VECPOINT', 'TO COMPUTE FINAL ANGLES', kind='operand', line=116)
W('26,2134', 0o00322, '', 'STORE', 'CPHI', 'STORE FINAL ANGLES - CPHI,CTHETA,CPSI', kind='interp', line=117)
W('26,2135', 0o77776, '', 'EXIT', kind='interp', line=118)

W('26,2136', 0o04616, 'TOBALL', 'TC', 'BANKCALL', line=120)
W('26,2137', 0o54266, '', 'CADR', 'BALLANGS', 'TO CONVERT ANGLES TO FDAI', kind='data', line=121)
W('26,2140', 0o32254, 'TOBALLA', 'CAF', 'V06N18', line=122)
W('26,2141', 0o04616, '', 'TC', 'BANKCALL', line=123)
W('26,2142', 0o20710, '', 'CADR', 'GOPERF2R', 'DISPLAY PLEASE PERFORM AUTO MANEUVER', kind='data', line=124)
W('26,2143', 0o02242, '', 'TC', 'R61TEST', line=125)
W('26,2144', 0o02150, '', 'TC', 'REDOMANC', 'PROCEED', line=126)
W('26,2145', 0o02175, '', 'TC', 'ENDMANU1', 'ENTER I.E. FINISHED WITH R60', line=127)
# Page 474
W('26,2146', 0o02201, '', 'TC', 'CHKLINUS', 'TO CHECK FOR PRIORITY DISPLAYS', line=129)
W('26,2147', 0o05155, '', 'TC', 'ENDOFJOB', line=130)

W('26,2150', 0o34746, 'REDOMANC', 'CAF', '3AXISBIT', line=132)
W('26,2151', 0o70101, '', 'MASK', 'FLAGWRD5', 'IS 3-AXIS FLAG SET', line=133)
W('26,2152', 0o10000, '', 'CCS', 'A', line=134)
W('26,2153', 0o12161, '', 'TCF', 'TOBALLC', 'YES', line=135)
W('26,2154', 0o06037, '', 'TC', 'INTPRET', line=136)
W('26,2155', 0o77624, '', 'CALL', kind='interp', line=137)
W('26,2156', 0o56040, '', '', 'VECPOINT', 'TO COMPUTE FINAL ANGLES', kind='operand', line=138)
W('26,2157', 0o00322, '', 'STORE', 'CPHI', 'STORE ANGLES', kind='interp', line=139)
W('26,2160', 0o77776, '', 'EXIT', kind='interp', line=140)

W('26,2161', 0o04616, 'TOBALLC', 'TC', 'BANKCALL', line=142)
W('26,2162', 0o54266, '', 'CADR', 'BALLANGS', 'TO CONVERT ANGLES TO FDAI', kind='data', line=143)
W('26,2163', 0o02255, '', 'TC', 'G+N,AUTO', 'CHECK AUTO MODE', line=144)
W('26,2164', 0o10000, '', 'CCS', 'A', line=145)
W('26,2165', 0o12140, '', 'TCF', 'TOBALLA', 'NOT AUTO, GO REREQUEST AUTO MANEUVER.', line=146)

W('26,2166', 0o32254, 'AUTOMANV', 'CAF', 'V06N18', 'STATIC DISPLAY DURING AUTO MANEUVER', line=148)
W('26,2167', 0o04616, '', 'TC', 'BANKCALL', line=149)
W('26,2170', 0o20451, '', 'CADR', 'GODSPR', kind='data', line=150)
W('26,2171', 0o02201, '', 'TC', 'CHKLINUS', 'TO CHECK FOR PRIORITY DISPLAYS', line=151)

W('26,2172', 0o04616, 'STARTMNV', 'TC', 'BANKCALL', 'PERFORM MANEUVER VIA KALCMANU', line=153)
W('26,2173', 0o17750, '', 'CADR', 'GOMANUR', kind='data', line=154)

W('26,2174', 0o12140, 'ENDMANUV', 'TCF', 'TOBALLA', 'FINISHED MANEUVER.', line=156)
W('26,2175', 0o05516, 'ENDMANU1', 'TC', 'DOWNFLAG', 'RESET 3-AXIS FLAG', line=157)
W('26,2176', 0o00124, '', 'ADRES', '3AXISFLG', kind='data', line=158)
W('26,2177', 0o31164, '', 'CAE', 'TEMPR60', line=159)
W('26,2200', 0o04640, '', 'TC', 'BANKJUMP', line=160)

W('26,2201', 0o40100, 'CHKLINUS', 'CS', 'FLAGWRD4', line=162)
W('26,2202', 0o74740, '', 'MASK', 'PDSPFBIT', 'IS PRIORITY DISPLAY FLAG SET?', line=163)
W('26,2203', 0o10000, '', 'CCS', 'A', line=164)
W('26,2204', 0o00002, '', 'TC', 'Q', 'NO - EXIT', line=165)
W('26,2205', 0o30002, '', 'CA', 'Q', line=166)
W('26,2206', 0o54156, '', 'TS', 'MPAC +2', 'SAVE RETURN', line=167)
W('26,2207', 0o46245, '', 'CS', 'THREE', 'OBTAIN LOCATION FOR RESTART', line=168)
W('26,2210', 0o60133, '', 'AD', 'BUF2', 'HOLDS Q OF LAST DISPLAY', line=169)
W('26,2211', 0o55055, '', 'TS', 'TBASE2', line=170)

W('26,2212', 0o05353, '', 'TC', 'PHASCHNG', line=172)
W('26,2213', 0o00132, '', 'OCT', '00132', kind='data', line=173)

W('26,2214', 0o34745, '', 'CAF', 'BIT7', line=175)
W('26,2215', 0o05464, '', 'TC', 'LINUS', 'GO SET BITS FOR PRIORITY DISPLAY', line=176)
W('26,2216', 0o00156, '', 'TC', 'MPAC +2', line=177)

# Page 475
W('26,2217', 0o37714, 'RELINUS', 'CAF', 'PRIO26', 'RESTORE ORIGINAL PRIORITY', line=180)
W('26,2220', 0o05146, '', 'TC', 'PRIOCHNG', line=181)

W('26,2221', 0o34747, '', 'CAF', 'TRACKBIT', "DON'T CONTINUE R60 UNLESS TRACKFLAG ON.", line=183)
W('26,2222', 0o70075, '', 'MASK', 'FLAGWRD1', line=184)
W('26,2223', 0o10000, '', 'CCS', 'A', line=185)
W('26,2224', 0o12237, '', 'TCF', 'RER60', line=186)

W('26,2225', 0o34745, '', 'CAF', 'RNDVZBIT', 'IS IT P20?', line=188)
W('26,2226', 0o70074, '', 'MASK', 'FLAGWRD0', line=189)
W('26,2227', 0o10000, '', 'CCS', 'A', line=190)
W('26,2230', 0o02234, '', 'TC', '+4', 'YES', line=191)
W('26,2231', 0o05353, '', 'TC', 'PHASCHNG', 'NO, MUST BE P25, SET 2.11 SPOT', line=192)
W('26,2232', 0o40112, '', 'OCT', '40112', kind='data', line=193)

W('26,2233', 0o05155, '', 'TC', 'ENDOFJOB', line=195)

W('26,2234', 0o05353, '', 'TC', 'PHASCHNG', 'SET 2.7 SPOT FOR P20', line=197)
W('26,2235', 0o40072, '', 'OCT', '40072', kind='data', line=198)

W('26,2236', 0o05155, '', 'TC', 'ENDOFJOB', line=200)

W('26,2237', 0o05504, 'RER60', 'TC', 'UPFLAG', 'SET PRIO DISPLAY FLAG AFTER RESTART', line=202)
W('26,2240', 0o00077, '', 'ADRES', 'PDSPFLAG', kind='data', line=203)

W('26,2241', 0o01055, '', 'TC', 'TBASE2', line=205)

W('26,2242', 0o31011, 'R61TEST', 'CA', 'MODREG', 'IF WE ARE IN P00 IT MUST BE V49 OR V89', line=207)
W('26,2243', 0o00006, '', 'EXTEND', line=208)
W('26,2244', 0o12175, '', 'BZF', 'ENDMANU1', 'THUS WE GO TO ENDEXT VIA USER', line=209)

W('26,2245', 0o30100, '', 'CA', 'FLAGWRD4', 'ARE WE IN R61  (P20 OR P25)', line=211)
W('26,2246', 0o74740, '', 'MASK', 'PDSPFBIT', line=212)
W('26,2247', 0o00006, '', 'EXTEND', line=213)
W('26,2250', 0o16001, '', 'BZF', 'GOTOPOOH', 'NO', line=214)
W('26,2251', 0o06022, '', 'TC', 'GOTOV56', 'YES', line=215)

W('26,2252', 0o20100, 'BIT14+7', 'OCT', '20100', kind='data', line=217)
W('26,2253', 0o00203, 'OCT203', 'OCT', '203', kind='data', line=218)
W('26,2254', 0o01422, 'V06N18', 'VN', '0618', kind='data', line=219)

# SUBROUTINE TO CHECK FOR G+N CONTROL. AUTO STABILIZATION
#
# RETURNS WITH C(A) = +  IF NOT SET FOR G+N, AUTO
# RETURNS WITH C(A) = +0 IF SWITCHES ARE SET

W('26,2255', 0o00006, 'G+N,AUTO', 'EXTEND', line=226)
W('26,2256', 0o00030, '', 'READ', 'CHAN30', line=227)
W('26,2257', 0o74742, '', 'MASK', 'BIT10', line=228)
W('26,2260', 0o10000, '', 'CCS', 'A', line=229)
W('26,2261', 0o00002, '', 'TC', 'Q', 'NOT IN G+N  C(A) = +', line=230)
# Page 476
W('26,2262', 0o00006, 'ISITAUTO', 'EXTEND', '', 'CHECK FOR AUTO MODE', line=232)
W('26,2263', 0o00031, '', 'READ', 'CHAN31', line=233)
W('26,2264', 0o74736, '', 'MASK', 'BIT14', line=234)
W('26,2265', 0o00002, '', 'TC', 'Q', '(+) = NOT IN AUTO,  (+0) = AOK', line=235)

# Page 477
# PROGRAM DESCRIPTION BALLANGS
# MOD NO.         LOG SECTION  R60,R62
#
# WRITTEN BY RAMA M.AIYAWAR
# FUNCTIONAL DESCRIPTION
#
# COMPUTES LM FDAI BALL DISPLAY ANGLES
# CALLING SEQUENCE
#
# TC      BALLANGS
# NORMAL EXIT MODE
#
# TC      BALLEXIT        # (SAVED Q)
#
# ALARM OR EXIT MODE  NIL
# SUBROUTINES CALLED
# CD*TR*G
# ARCTAN
#
# INPUT
#
# CPHI,CTHETA,CPSI  ARE  THE ANGLES CORRESPONDING TO AOG,AIG,AMG. THEY ARE
# SP,2S COMPLIMENT SCALED TO HALF REVOLUTION.
# OUTPUT
#
# FDAIX,FDAIY,FDAIZ ARE THE REQUIRED BALL ANGLES SCALED TO HALF REVOLUTION
# SP,2S COMPLIMENT.
# THESE ANGLES WILL BE DISPLAYED AS DEGREES AND HUNDREDTHS. IN THE ORDER  ROLL, PITCH, YAW, USING NOUNS 18 & 19.
#
# ERASABLE INITIALIZATION REQUIRED
#
# CPHI,CTHETA,CPSI EACH A SP REGISTER
# DEBRIS
#
# A,L,Q,MPAC,SINCDU,COSCDU,PUSHLIS,BALLEXIT
#
#
# NOMENCLATURE:  CPHI, CTHETA, & CPSI REPRESENT THE OUTER, INNER, & MIDDLE GIMBAL ANGLES, RESPECTIVELY; OR
# EQUIVALENTLY, CDUX, CDUY, & CDUZ.
#
# NOTE:  ARCTAN CHECKS FOR OVERFLOW AND SHOULD BE ABLE TO HANDLE ANY SINGULARITIES.

#   SETLOC BAWLANGS
#   BANK

#   COUNT* $$/BALL
W('26,2266', 0o04645, 'BALLANGS', 'TC', 'MAKECADR', line=284)
W('26,2267', 0o55342, '', 'TS', 'BALLEXIT', line=285)
W('26,2270', 0o30321, '', 'CA', 'CPHI', line=286)
# Page 478
W('26,2271', 0o54772, '', 'TS', 'CDUSPOT +4', line=288)
W('26,2272', 0o30322, '', 'CA', 'CTHETA', line=289)
W('26,2273', 0o54766, '', 'TS', 'CDUSPOT', line=290)
W('26,2274', 0o30323, '', 'CA', 'CPSI', line=291)
W('26,2275', 0o54770, '', 'TS', 'CDUSPOT +2', line=292)

W('26,2276', 0o06037, '', 'TC', 'INTPRET', line=294)
W('26,2277', 0o45001, '', 'SETPD', 'CALL', kind='interp', line=295)
W('26,2300', 0o00001, '', '', '0D', kind='operand', line=296)
W('26,2301', 0o47543, '', '', 'CD*TR*G', kind='operand', line=297)

W('26,2302', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=299)
W('26,2303', 0o00743, '', '', 'SINCDUX', 'SIN (OGA)', kind='operand', line=300)
W('26,2304', 0o00747, '', '', 'COSCDUZ', 'COS (MGA)', kind='operand', line=301)

W('26,2305', 0o57552, '', 'SL1', 'DCOMP', 'SCALE', kind='interp', line=303)
W('26,2306', 0o65336, '', 'ARCSIN', 'PDDL', 'YAW = ARCSIN(-SXCZ) INTO 0 PD', kind='interp', line=304)
W('26,2307', 0o00741, '', '', 'SINCDUZ', kind='operand', line=305)
W('26,2310', 0o14023, '', 'STODL', 'SINTH', '(SINTH = 18D IN PD)', kind='interp', line=306)
W('26,2311', 0o00747, '', '', 'COSCDUZ', kind='operand', line=307)
W('26,2312', 0o72405, '', 'DMP', 'SL1', 'RESCALE', kind='interp', line=308)
W('26,2313', 0o00751, '', '', 'COSCDUX', kind='operand', line=309)
W('26,2314', 0o34021, '', 'STCALL', 'COSTH', '(COSTH= 16D IN PD)', kind='interp', line=310)
W('26,2315', 0o26510, '', '', 'ARCTAN', kind='operand', line=311)
W('26,2316', 0o41325, '', 'PDDL', 'DMP', 'ROLL = ARCTAN(SZ/CZCX) INTO 2 PD', kind='interp', line=312)
W('26,2317', 0o00741, '', '', 'SINCDUZ', kind='operand', line=313)
W('26,2320', 0o00743, '', '', 'SINCDUX', kind='operand', line=314)
W('26,2321', 0o41512, '', 'SL2', 'PUSH', 'SXSZ INTO 4 PD', kind='interp', line=315)
W('26,2322', 0o65205, '', 'DMP', 'PDDL', 'SXSZCY INTO 4 PD', kind='interp', line=316)
W('26,2323', 0o00745, '', '', 'COSCDUY', kind='operand', line=317)
W('26,2324', 0o65205, '', 'DMP', 'PDDL', 'SXSZSY INTO 6 PD', kind='interp', line=318)
W('26,2325', 0o00737, '', '', 'SINCDUY', kind='operand', line=319)
W('26,2326', 0o00751, '', '', 'COSCDUX', kind='operand', line=320)
W('26,2327', 0o72405, '', 'DMP', 'SL1', 'CXCY', kind='interp', line=321)
W('26,2330', 0o00745, '', '', 'COSCDUY', kind='operand', line=322)
W('26,2331', 0o45425, '', 'DSU', 'STADR', 'PULL UP FROM 6 PD', kind='interp', line=323)
W('26,2332', 0o63756, '', 'STODL', 'COSTH', 'COSTH = CXCY - SXSZSY', kind='interp', line=324)
W('26,2333', 0o00737, '', '', 'SINCDUY', kind='operand', line=325)
W('26,2334', 0o72405, '', 'DMP', 'SL1', kind='interp', line=326)
W('26,2335', 0o00751, '', '', 'COSCDUX', 'CXSY', kind='operand', line=327)
W('26,2336', 0o45415, '', 'DAD', 'STADR', 'PULL UP FROM 4 PD', kind='interp', line=328)
W('26,2337', 0o43754, '', 'STCALL', 'SINTH', 'SINTH = CXSY + SXSZCY', kind='interp', line=329)
W('26,2340', 0o26510, '', '', 'ARCTAN', 'RETURNS WITH D(MPAC) = PITCH', kind='operand', line=330)
W('26,2341', 0o55525, '', 'PDDL', 'VDEF', 'PITCH INTO 2 PD, ROLL INTO MPAC FROM 2PD', kind='interp', line=331)
W('26,2342', 0o77634, '', 'RTB', '', 'VDEF MAKES V(MPAC) = ROLL, PITCH, YAW', kind='interp', line=332)
W('26,2343', 0o21620, '', '', 'V1STO2S', kind='operand', line=333)
W('26,2344', 0o02345, '', 'STORE', 'FDAIX', 'MODE IS TP', kind='interp', line=334)
W('26,2345', 0o77776, '', 'EXIT', kind='interp', line=335)

W('26,2346', 0o31342, 'ENDBALL', 'CA', 'BALLEXIT', line=337)

# Page 479
W('26,2347', 0o04640, '', 'TC', 'BANKJUMP', line=340)

# Page 480
# PROGRAM DESCRIPTION - VECPOINT
#
#
# THIS INTERPRETIVE SUBROUTINE MAY BE USED TO POINT A SPACECRAFT AXIS IN A DESIRED DIRECTION.  THE AXIS
# TO BE POINTED MUST APPEAR AS A HALF UNIT DOUBLE PRECISION VECTOR IN SUCCESSIVE LOCATIONS OF ERASABLE MEMORY
# BEGINNING WITH THE LOCATION CALLED SCAXIS.  THE COMPONENTS OF THIS VECTOR ARE GIVEN IN SPACECRAFT COORDINATES.
# THE DIRECTION IN WHICH THIS AXIS IS TO BE POINTED MUST APPEAR AS A HALF UNIT DOUBLE PRECISION VECTOR IN
# SUCCESSIVE LOCATIONS OF ERASABLE MEMORY BEGINNING WITH THE ADDRESS CALLED POINTVSM.  THE COMPONENTS OF THIS
# VECTOR ARE GIVEN IN STABLE MEMBER COORDINATES.  WITH THIS INFORMATION VECPOINT COMPUTES A SET OF THREE GIMBAL
# ANGLES (2S COMPLEMENT) CORESPONDING TO THE CROSS-PRODUCT ROTATION BETWE EN SCAXIS AND POINTVSM AND STORES THEM
# IN T(MPAC) BEFORE RETURNING TO THE CALLER.
# THIS ROTATION, HOWEVER, MAY BRING THE S/C INTO GIMBAL LOCK.  WHEN POINTING A VECTOR IN THE Y-Z PLANE,
# THE TRANSPONDER AXIS, OR THE AOT FOR THE LEM, THE PROGRAM WILL CORRECT THIS PROBLEM BY ROTATING THE CROSS-
# PRODUCT ATTITUDE ABOUT POINTVSM BY A FIXED AMOUNT SUFFICIENT TO ROTATE THE DESIRED S/C ATTITUDE OUT OF GIMBAL
# LOCK.  IF THE AXIS TO BE POINTED IS MORE THAN 40.6 DEGREES BUT LESS THAN 60.5 DEG FROM THE +X (OR-X) AXIS,
# THE ADDITIONAL ROTATION TO AVOID GIMAL LOCK IS 35 DEGREES.  IF THE AXIS IS MORE THAN 60.5 DEGEES FROM +X (OR -X)
# THE ADDITIONAL ROTATION IS 35 DEGREES.  THE GIMBAL ANGLES CORRESPONDING TO THIS ATTITUDE ARE THEN COMPUTED AND
# STORED AS 2S COMPLIMENT ANGLES IN T(MPAC) BEFORE RETURNING TO THE CALLER.
# WHEN POINTING THE X-AXIS, OR THE THRUST VECTOR, OR ANY VECTOR WITHIN 40.6 DEG OF THE X-AXIS, VECPOINT
# CANNOT CORRECT FOR A CROSS-PRODUCT ROTATION INTO GIMBAL LOCK.  IN THIS CASE A PLATFORM REALIGNMENT WOULD BE
# REQUIRED TO POINT THE VECTOR IN THE DESIRED DIRECTION.  AT PRESENT NO INDICATION IS GIVEN FOR THIS SITUATION
# EXCEPT THAT THE FINAL MIDDLE GIMBAL ANGLE IN MPAC +2 IS GREATER THAN 59 DEGREES.
#
# CALLING SEQUENCE -
# 1) LOAD SCAXIS, POINTVSM
# 2) CALL
# VECPOINT
#
# RETURNS WITH
#
# 1) DESIRED OUTER  GIMBAL ANGLE IN MPAC
# 2) DESIRED INNER  GIMBAL ANGLE IN MPAC +1
# 3) DESIRED MIDDLE GIMBAL ANGLE IN MPAC +2
#
# ERASABLES USED -
#
# 1) SCAXIS           6
# 2) POINTVSM         6
# 3) MIS             18
# 4) DEL             18
# 5) COF              6
# 6) VECQTEMP         1
# 7) ALL OF VAC AREA 43
#
# TOTAL     99

#   SETLOC VECPT
#   BANK
# Page 481
#   COUNT* $$/VECPT

#   EBANK= BCDU

W('27,2032', 0o40020, 'VECPNT1', 'STQ', 'BOV', 'THIS ENTRY USES DESIRED CDUS', kind='interp', line=396)
W('27,2033', 0o03325, '', '', 'VECQTEMP', "NOT PRESENT-ENTER WITH CDUD'S IN MPAC", kind='operand', line=397)
W('27,2034', 0o56035, '', '', 'VECPNT2', kind='operand', line=398)
W('27,2035', 0o52164, 'VECPNT2', 'AXC,2', 'GOTO', kind='interp', line=399)
W('27,2036', 0o03246, '', '', 'MIS', kind='operand', line=400)
W('27,2037', 0o56046, '', '', 'STORANG', kind='operand', line=401)
W('27,2040', 0o40020, 'VECPOINT', 'STQ', 'BOV', 'SAVE RETURN ADDRESS', kind='interp', line=402)
W('27,2041', 0o03325, '', '', 'VECQTEMP', kind='operand', line=403)
W('27,2042', 0o56043, '', '', 'VECLEAR', 'AND CLEAR OVFIND', kind='operand', line=404)
W('27,2043', 0o47164, 'VECLEAR', 'AXC,2', 'RTB', kind='interp', line=405)
W('27,2044', 0o03246, '', '', 'MIS', 'READ THE PRESENT CDU ANGLES AND', kind='operand', line=406)
W('27,2045', 0o44403, '', '', 'READCDUK', 'STORE THEM IN PD25, 26, 27', kind='operand', line=407)
W('27,2046', 0o34032, 'STORANG', 'STCALL', '25D', kind='interp', line=408)
W('27,2047', 0o44410, '', '', 'CDUTODCM', 'S/C AXES TO STABLE MEMBER AXES (MIS)', kind='operand', line=409)
W('27,2050', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=410)
W('27,2051', 0o03773, '', '', 'POINTVSM', 'RESOLVE THE POINTING DIRECTION VF INTO', kind='operand', line=411)
W('27,2052', 0o03247, '', '', 'MIS', 'INITIAL S/C AXES ( VF = POINTVSM)', kind='operand', line=412)
W('27,2053', 0o77656, '', 'UNIT', kind='interp', line=413)
W('27,2054', 0o00035, '', 'STORE', '28D', kind='interp', line=414)
# PD 28 29 30 31 32 33
W('27,2055', 0o53435, '', 'VXV', 'UNIT', 'TAKE THE CROSS PRODUCT VF X VI', kind='interp', line=416)
W('27,2056', 0o03765, '', '', 'SCAXIS', 'WHERE VI = SCAXIS', kind='operand', line=417)
W('27,2057', 0o57400, '', 'BOV', 'VCOMP', kind='interp', line=418)
W('27,2060', 0o56170, '', '', 'PICKAXIS', kind='operand', line=419)
W('27,2061', 0o17271, '', 'STODL', 'COF', 'CHECK MAGNITUDE', kind='interp', line=420)
W('27,2062', 0o00045, '', '', '36D', 'OF CROSS PRODUCT', kind='operand', line=421)
W('27,2063', 0o50025, '', 'DSU', 'BMN', 'VECTOR, IF LESS', kind='interp', line=422)
W('27,2064', 0o14411, '', '', 'DPB-14', 'THAN B-14 ASSUME', kind='operand', line=423)
W('27,2065', 0o56170, '', '', 'PICKAXIS', 'UNIT OPERATION', kind='operand', line=424)
W('27,2066', 0o50375, '', 'VLOAD', 'DOT', '         INVALID.', kind='interp', line=425)
W('27,2067', 0o03765, '', '', 'SCAXIS', kind='operand', line=426)
W('27,2070', 0o00035, '', '', '28D', kind='operand', line=427)
W('27,2071', 0o65552, '', 'SL1', 'ARCCOS', kind='interp', line=428)
W('27,2072', 0o77624, 'COMPMATX', 'CALL', '', 'NOW COMPUTE THE TRANSFORMATION FROM', kind='interp', line=429)
W('27,2073', 0o44527, '', '', 'DELCOMP', 'FINAL S/C AXES TO INITIAL S/C AXES  MFI', kind='operand', line=430)
W('27,2074', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=431)
W('27,2075', 0o03246, '', '', 'MIS', 'COMPUTE THE TRANSFORMATION FROM FINAL', kind='operand', line=432)
W('27,2076', 0o02230, '', '', 'KEL', 'S/C AXES TO STABLE MEMBER AXES', kind='operand', line=433)
W('27,2077', 0o77624, '', 'CALL', '', 'MFS = MIS MFI', kind='interp', line=434)
W('27,2100', 0o44312, '', '', 'MXM3', '(IN PD LIST)', kind='operand', line=435)

W('27,2101', 0o51545, '', 'DLOAD', 'ABS', kind='interp', line=437)
W('27,2102', 0o00007, '', '', '6', 'MFS6 = SIN(CPSI)                     $2', kind='operand', line=438)
W('27,2103', 0o50025, '', 'DSU', 'BMN', kind='interp', line=439)
W('27,2104', 0o14376, '', '', 'SINGIMLC', '= SIN(59 DEGS)                       $2', kind='operand', line=440)
W('27,2105', 0o56160, '', '', 'FINDGIMB', '/CPSI/ LESS THAN 59 DEGS', kind='operand', line=441)
# Page 482
# I.E. DESIRED ATTITUDE NOT IN GIMBAL LOCK

W('27,2106', 0o51545, '', 'DLOAD', 'ABS', 'CHECK TO SEE IF WE ARE POINTING', kind='interp', line=445)
W('27,2107', 0o03765, '', '', 'SCAXIS', 'THE THRUST AXIS', kind='operand', line=446)
W('27,2110', 0o51025, '', 'DSU', 'BPL', kind='interp', line=447)
W('27,2111', 0o14400, '', '', 'SINVEC1', 'SIN 49.4 DEGS                        $2', kind='operand', line=448)
W('27,2112', 0o56160, '', '', 'FINDGIMB', 'IF SO, WE ARE TRYING TO POINT IT INTO', kind='operand', line=449)
W('27,2113', 0o77775, '', 'VLOAD', '', 'GIMBAL LOCK, ABORT COULD GO HERE', kind='interp', line=450)
W('27,2114', 0o77626, '', 'STADR', kind='interp', line=451)
W('27,2115', 0o50514, '', 'STOVL', 'MIS +12D', kind='interp', line=452)
W('27,2116', 0o77626, '', 'STADR', '', 'STORE MFS (IN PD LIST) IN MIS', kind='interp', line=453)
W('27,2117', 0o50522, '', 'STOVL', 'MIS +6', kind='interp', line=454)
W('27,2120', 0o77626, '', 'STADR', kind='interp', line=455)
W('27,2121', 0o50530, '', 'STOVL', 'MIS', kind='interp', line=456)
W('27,2122', 0o03255, '', '', 'MIS +6', 'INNER GIMBAL AXIS IN FINAL S/C AXES', kind='operand', line=457)
W('27,2123', 0o57444, '', 'BPL', 'VCOMP', 'LOCATE THE IG AXIS DIRECTION CLOSEST TO', kind='interp', line=458)
W('27,2124', 0o56125, '', '', 'IGSAMEX', 'FINAL X S/C AXIS', kind='operand', line=459)

W('27,2125', 0o50035, 'IGSAMEX', 'VXV', 'BMN', 'FIND THE SHORTEST WAY OF ROTATING THE', kind='interp', line=461)
W('27,2126', 0o03765, '', '', 'SCAXIS', 'S/C OUT OF GIMBAL LOCK BY A ROTATION', kind='operand', line=462)
W('27,2127', 0o56134, '', '', 'U=SCAXIS', 'ABOUT +- SCAXIS, I.E. IF (IG (SGN MFS3)', kind='operand', line=463)
# X SCAXIS . XF) LESS THAN 0, U = SCAXIS
# OTHERWISE U = -SCAXIS

W('27,2130', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=467)
W('27,2131', 0o03765, '', '', 'SCAXIS', kind='operand', line=468)
W('27,2132', 0o37271, '', 'STCALL', 'COF', 'ROTATE ABOUT -SCAXIS', kind='interp', line=469)
W('27,2133', 0o56137, '', '', 'CHEKAXIS', kind='operand', line=470)
W('27,2134', 0o77775, 'U=SCAXIS', 'VLOAD', kind='interp', line=471)
W('27,2135', 0o03765, '', '', 'SCAXIS', kind='operand', line=472)
W('27,2136', 0o03271, '', 'STORE', 'COF', 'ROTATE ABOUT + SCAXIS', kind='interp', line=473)
W('27,2137', 0o51545, 'CHEKAXIS', 'DLOAD', 'ABS', kind='interp', line=474)
W('27,2140', 0o03765, '', '', 'SCAXIS', 'SEE IF WE ARE POINTING THE AOT', kind='operand', line=475)
W('27,2141', 0o51025, '', 'DSU', 'BPL', kind='interp', line=476)
W('27,2142', 0o14402, '', '', 'SINVEC2', 'SIN 29.5 DEGS                        $2', kind='operand', line=477)
W('27,2143', 0o56147, '', '', 'PICKANG1', 'IF SO, ROTATE 50 DEGS ABOUT +- SCAXIS', kind='operand', line=478)
W('27,2144', 0o52145, '', 'DLOAD', 'GOTO', 'IF NOT, MUST BE POINTING THE TRANSPONDER', kind='interp', line=479)
W('27,2145', 0o14406, '', '', 'VECANG2', 'OR SOME VECTOR IN THE Y, OR Z PLANE', kind='operand', line=480)
W('27,2146', 0o56151, '', '', 'COMPMFSN', 'IN THIS CASE ROTATE 35 DEGS TO GET OUT', kind='operand', line=481)
# OF GIMBAL LOCK (VECANG2  $360)
W('27,2147', 0o77745, 'PICKANG1', 'DLOAD', kind='interp', line=483)
W('27,2150', 0o14404, '', '', 'VECANG1', '= 50 DEGS                          $ 360', kind='operand', line=484)
W('27,2151', 0o77624, 'COMPMFSN', 'CALL', kind='interp', line=485)
W('27,2152', 0o44527, '', '', 'DELCOMP', 'COMPUTE THE ROTATION ABOUT SCAXIS TO', kind='operand', line=486)
W('27,2153', 0o75160, '', 'AXC,1', 'AXC,2', 'BRING MFS OUT OF GIMBAL LOCK', kind='interp', line=487)
W('27,2154', 0o03246, '', '', 'MIS', kind='operand', line=488)
W('27,2155', 0o02230, '', '', 'KEL', kind='operand', line=489)
W('27,2156', 0o77624, '', 'CALL', '', 'COMPUTE THE NEW TRANSFORMATION FROM', kind='interp', line=490)
W('27,2157', 0o44312, '', '', 'MXM3', 'DESIRED S/C AXES TO STABLE MEMBER AXES', kind='operand', line=491)
# WHICH WILL ALIGN VI WITH VF AND AVOID
# Page 483
# GIMBAL LOCK
W('27,2160', 0o45160, 'FINDGIMB', 'AXC,1', 'CALL', kind='interp', line=495)
W('27,2161', 0o00000, '', '', '0', 'EXTRACT THE COMMANDED CDU ANGLES FROM', kind='operand', line=496)
W('27,2162', 0o44654, '', '', 'DCMTOCDU', 'THIS MATRIX', kind='operand', line=497)
W('27,2163', 0o40234, '', 'RTB', 'SETPD', kind='interp', line=498)
W('27,2164', 0o21620, '', '', 'V1STO2S', 'CONVERT TO 2:S COMPLEMENT', kind='operand', line=499)
W('27,2165', 0o00001, '', '', '0', kind='operand', line=500)
W('27,2166', 0o77650, '', 'GOTO', kind='interp', line=501)
W('27,2167', 0o03325, '', '', 'VECQTEMP', 'RETURN TO CALLER', kind='operand', line=502)

W('27,2170', 0o50375, 'PICKAXIS', 'VLOAD', 'DOT', 'IF VF X VI = 0,  FIND VF . VI', kind='interp', line=504)
W('27,2171', 0o00035, '', '', '28D', kind='operand', line=505)
W('27,2172', 0o03765, '', '', 'SCAXIS', kind='operand', line=506)
W('27,2173', 0o72240, '', 'BMN', 'TLOAD', kind='interp', line=507)
W('27,2174', 0o54350, '', '', 'ROT180', kind='operand', line=508)
W('27,2175', 0o00032, '', '', '25D', kind='operand', line=509)
W('27,2176', 0o77650, '', 'GOTO', '', 'IF VF = VI, CDU DESIRED = PRESENT CDU', kind='interp', line=510)
W('27,2177', 0o03325, '', '', 'VECQTEMP', 'PRESENT CDU ANGLES', kind='operand', line=511)

#   BANK 35
#   SETLOC MANUVER1
#   BANK
W('26,2350', 0o47375, 'ROT180', 'VLOAD', 'VXV', 'IF VF, VI ANTIPARALLEL, 180 DEG ROTATION', kind='interp', line=516)
W('26,2351', 0o03255, '', '', 'MIS +6', 'IS REQUIRED. Y STABLE MEMBER AXIS IN', kind='operand', line=517)
W('26,2352', 0o06520, '', '', 'HIDPHALF', 'INITIAL S/C AXES.', kind='operand', line=518)
W('26,2353', 0o47256, '', 'UNIT', 'VXV', 'FIND Y(SM) X X(I)', kind='interp', line=519)
W('26,2354', 0o03765, '', '', 'SCAXIS', 'FIND UNIT(VI X UNIT(Y(SM) X X(I)))', kind='operand', line=520)
W('26,2355', 0o40056, '', 'UNIT', 'BOV', 'I.E. PICK A VECTOR IN THE PLANE OF X(I),', kind='interp', line=521)
W('26,2356', 0o54372, '', '', 'PICKX', 'Y(SM) PERPENDICULAR TO VI', kind='operand', line=522)
W('26,2357', 0o17271, '', 'STODL', 'COF', kind='interp', line=523)
W('26,2360', 0o00045, '', '', '36D', 'CHECK MAGNITUDE', kind='operand', line=524)
W('26,2361', 0o50025, '', 'DSU', 'BMN', 'OF THIS VECTOR.', kind='interp', line=525)
W('26,2362', 0o14411, '', '', 'DPB-14', 'IF LESS THAN B-14,', kind='operand', line=526)
W('26,2363', 0o54372, '', '', 'PICKX', 'PICK X-AXIS.', kind='operand', line=527)
W('26,2364', 0o77775, '', 'VLOAD', kind='interp', line=528)
W('26,2365', 0o03271, '', '', 'COF', kind='operand', line=529)
W('26,2366', 0o17271, 'XROT', 'STODL', 'COF', kind='interp', line=530)
W('26,2367', 0o06520, '', '', 'HIDPHALF', kind='operand', line=531)
W('26,2370', 0o77650, '', 'GOTO', kind='interp', line=532)
W('26,2371', 0o56072, '', '', 'COMPMATX', kind='operand', line=533)
W('26,2372', 0o52175, 'PICKX', 'VLOAD', 'GOTO', 'PICK THE XAXIS IN THIS CASE', kind='interp', line=534)
W('26,2373', 0o06520, '', '', 'HIDPHALF', kind='operand', line=535)
W('26,2374', 0o54366, '', '', 'XROT', kind='operand', line=536)
W('26,2375', 0o15555, 'SINGIMLC', '2DEC', '.4285836003', '=SIN(59)                $2', kind='data', line=537)
W('26,2376', 0o35172, kind='data', line=537)

W('26,2377', 0o14113, 'SINVEC1', '2DEC', '.3796356537', '=SIN(49.4)              $2', kind='data', line=539)
W('26,2400', 0o36326, kind='data', line=539)

W('26,2401', 0o07701, 'SINVEC2', '2DEC', '.2462117800', '=SIN(29.5)              $2', kind='data', line=541)
W('26,2402', 0o35703, kind='data', line=541)

W('26,2403', 0o04343, 'VECANG1', '2DEC', '.1388888889', '= 50 DEGREES                        $360', kind='data', line=543)
W('26,2404', 0o21616, kind='data', line=543)
# Page 484
W('26,2405', 0o03070, 'VECANG2', '2DEC', '.09722222222', '= 35 DEGREES                        $360', kind='data', line=545)
W('26,2406', 0o34344, kind='data', line=545)

W('26,2407', 0o00000, '1BITDP', 'OCT', '0', 'KEEP THIS BEFORE DPB(-14)      *********', kind='data', line=547)
W('26,2410', 0o00001, 'DPB-14', 'OCT', '00001', kind='data', line=548)
W('26,2411', 0o00000, '', 'OCT', '00000', kind='data', line=549)

# Page 485
# ROUTINE FOR INITIATING AUTOMATIC MANEUVER VIA KEYBOARD (V49)

#   BANK 34
#   SETLOC R62
#   BANK
#   EBANK= BCDU

#   COUNT* $$/R62

S('R62DISP', 'equals', 0o56103, line=561)

W('23,2103', 0o35010, 'R62FLASH', 'CAF', 'V06N22', 'FLASH V06N22 AND', line=563)
W('23,2104', 0o04616, '', 'TC', 'BANKCALL', 'ICDU ANGLES', line=564)
W('23,2105', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=565)
W('23,2106', 0o15472, '', 'TCF', 'ENDEXT', 'TERMINATE', line=566)
W('23,2107', 0o12111, '', 'TCF', 'GOMOVE', 'PROCEED', line=567)
W('23,2110', 0o12103, '', 'TCF', 'R62FLASH', 'ENTER', line=568)

# ASTRONAUT MAY LOAD NEW ICDUS AT THIS
# POINT
W('23,2111', 0o05504, 'GOMOVE', 'TC', 'UPFLAG', 'SET FOR 3-AXIS MANEUVER', line=572)
W('23,2112', 0o00124, '', 'ADRES', '3AXISFLG', kind='data', line=573)

W('23,2113', 0o04616, '', 'TC', 'BANKCALL', line=575)
W('23,2114', 0o54123, '', 'CADR', 'R60LEM', kind='data', line=576)
W('23,2115', 0o15472, '', 'TCF', 'ENDEXT', 'END R62', line=577)
