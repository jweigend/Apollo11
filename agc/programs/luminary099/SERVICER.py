"""SERVICER.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/SERVICER.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 857-897 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('SERVICER', 'SERVICER.agc', 'Luminary099', pages='857-897')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     SERVICER.agc
# Purpose:      Part of the source code for Luminary, build 099. It
# is part of the source code for the Lunar Module's
# (LM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 857-897
# Contact:      Ron Burkey <info@sandroid.org>,
# Fabrizio Bernardini <fabrizio@spacecraft.it>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-06-01 FB   Transcription Batch 4 Assignment.
# 2009-06-05 RSB  Fixed a couple of typos, plus a goofy relative
# label reference from the original source.
#
# The contents of the "Luminary099" files, in general, are transcribed
# from scanned documents.
#
# Assemble revision 001 of AGC program Luminary099 by NASA
# 2021112-061.  July 14, 1969.
#
# Prepared by
# Massachusetts Institute of Technology
# 75 Cambridge Parkway
# Cambridge, Massachusetts
#
# under NASA contract NAS 9-4065.
#
# Refer directly to the online document mentioned above for further
# information.  Please report any errors to info@sandroid.org.

# Page 857
#   BANK 37
#   SETLOC SERV1
#   BANK

#   EBANK= DVCNTR

# ************* PREREAD *******************

#   COUNT* $$/SERV

W('37,3410', 0o34757, 'PREREAD', 'CAF', 'SEVEN', '5.7 SPOT TO SKIP LASTBIAS AFTER', line=42)
W('37,3411', 0o03531, '', 'TC', 'GNUFAZE5', 'RESTART.', line=43)
W('37,3412', 0o35031, '', 'CAF', 'PRIO21', line=44)
W('37,3413', 0o05072, '', 'TC', 'NOVAC', line=45)
#   EBANK= NBDX
W('37,3414', 0o03663, '', '2CADR', 'LASTBIAS', 'DO LAST GYRO COMPENSATION IN FREE FALL', kind='data', line=47)
W('37,3415', 0o14063, kind='data', line=47)

W('37,3416', 0o03544, 'BIBIBIAS', 'TC', 'PIPASR +3', 'CLEAR + READ PIPS LAST TIME IN FRE5+F133', line=49)
# DO NOT DESTROY VALUE OF PIPTIME1

W('37,3417', 0o40103, '', 'CS', 'FLAGWRD7', line=52)
W('37,3420', 0o74773, '', 'MASK', 'SUPER011', 'SET V37FLAG AND AVEGFLAG (BITS 5 AND 6', line=53)
W('37,3421', 0o26103, '', 'ADS', 'FLAGWRD7', '      OF FLAGWRD7)', line=54)

W('37,3422', 0o44735, '', 'CS', 'DRFTBIT', line=56)
W('37,3423', 0o70076, '', 'MASK', 'FLAGWRD2', 'RESET DRIFTFLAG', line=57)
W('37,3424', 0o54076, '', 'TS', 'FLAGWRD2', line=58)

W('37,3425', 0o34751, '', 'CAF', 'FOUR', 'INITIALIZE DV MONITOR', line=60)
W('37,3426', 0o55257, '', 'TS', 'PIPAGE', line=61)

W('37,3427', 0o33537, '', 'CAF', 'ENDJBCAD', 'POINT OUTROUTE TO END-OF-JOB.', line=63)
W('37,3430', 0o55260, '', 'TS', 'OUTROUTE', line=64)

W('37,3431', 0o37710, '', 'CAF', 'PRIO22', line=66)
W('37,3432', 0o05105, '', 'TC', 'FINDVAC', 'TO FIRST ENTRY TO AVERAGE G', line=67)
#   EBANK= DVCNTR
W('37,3433', 0o02461, '', '2CADR', 'NORMLIZE', kind='data', line=69)
W('37,3434', 0o46067, kind='data', line=69)

W('37,3435', 0o34752, '', 'CA', 'TWO', '5.2SPOT FOR REREADAC AND NORMLIZE', line=71)
W('37,3436', 0o03525, 'GOREADAX', 'TC', 'GNUTFAZ5', line=72)
W('37,3437', 0o35000, '', 'CA', '2SECS', 'WAIT TWO SECONDS FOR READACCS', line=73)
W('37,3440', 0o05224, '', 'TC', 'VARDELAY', line=74)

# Page 858
# ************* READACCS ****************

W('37,3441', 0o43540, 'READACCS', 'CS', 'OCT37771', 'THIS PIECE OF CODING ATTEMPTS TO', line=79)
W('37,3442', 0o60030, '', 'AD', 'TIME5', 'SYNCHRONIZE READACCS WITH THE DIGITAL', line=80)
W('37,3443', 0o10000, '', 'CCS', 'A', 'AUTOPILOT SO THAT A PAXIS RUPT WILL', line=81)
W('37,3444', 0o44753, '', 'CS', 'ONE', 'OCCUR APPROXIMATELY 70 MILLISECONDS', line=82)
W('37,3445', 0o13447, '', 'TCF', '+2', 'FOLLOWING THE READACCS RUPT.  THE 70 MS', line=83)
W('37,3446', 0o34753, '', 'CA', 'ONE', 'OFFSET WAS CHOSEN SO THAT THE PAXIS', line=84)
W('37,3447', 0o26030, '', 'ADS', 'TIME5', 'RUPT WOULD NOT OCCUR SIMULTANEOUSLY', line=85)
# WITH ANY OF THE 8 SUBSEQUENT R10,R11
# INTERRUPTS -- THUS MINIMIZING THE POSS-
# IBILITY OF LOSING DOWNRUPTS.

W('37,3450', 0o03541, '', 'TC', 'PIPASR', 'READ THE PIPAS.', line=90)

W('37,3451', 0o34756, 'PIPSDONE', 'CA', 'FIVE', line=92)
W('37,3452', 0o03531, '', 'TC', 'GNUFAZE5', line=93)
W('37,3453', 0o34753, 'REDO5.5', 'CAF', 'ONE', line=94)
W('37,3454', 0o55257, '', 'TS', 'PIPAGE', line=95)

W('37,3455', 0o34736, '', 'CA', 'PRIO20', line=97)
W('37,3456', 0o05105, '', 'TC', 'FINDVAC', line=98)
#   EBANK= DVCNTR
W('37,3457', 0o02206, '', '2CADR', 'SERVICER', 'SET UP SERVICER JOB', kind='data', line=100)
W('37,3460', 0o66067, kind='data', line=100)

W('37,3461', 0o34743, '', 'CA', 'BIT9', line=102)
W('37,3462', 0o00006, '', 'EXTEND', line=103)
W('37,3463', 0o05011, '', 'WOR', 'DSALMOUT', 'TURN ON TEST CONNECTOR OUTBIT', line=104)

W('37,3464', 0o30103, '', 'CA', 'FLAGWRD7', line=106)
W('37,3465', 0o74747, '', 'MASK', 'AVEGFBIT', line=107)
W('37,3466', 0o00006, '', 'EXTEND', line=108)
W('37,3467', 0o13517, '', 'BZF', 'AVEGOUT', 'AVEGFLAG DOWN -- SET UP FINAL EXIT', line=109)

W('37,3470', 0o30102, '', 'CA', 'FLAGWRD6', line=111)
W('37,3471', 0o74744, '', 'MASK', 'MUNFLBIT', line=112)
W('37,3472', 0o00006, '', 'EXTEND', line=113)
W('37,3473', 0o13515, '', 'BZF', 'MAKEACCS', 'MUNFLAG CLEAR -- BYPASS LR AND DISP.', line=114)

W('37,3474', 0o10755, '', 'CCS', 'PHASE2', line=116)
W('37,3475', 0o13515, '', 'TCF', 'MAKEACCS', 'PHASE 2 ACTIVATED -- AVOID MULTIPLE R10.', line=117)

W('37,3476', 0o34757, '', 'CAF', 'SEVEN', 'SET PIPCTR FOR 4X/SEC RATE.', line=119)
W('37,3477', 0o55056, '', 'TS', 'PIPCTR', line=120)

W('37,3500', 0o40025, '', 'CS', 'TIME1', 'SET TBASE2 .05 SECONDS IN THE PAST.', line=122)
W('37,3501', 0o64756, '', 'AD', 'FIVE', line=123)
W('37,3502', 0o64734, '', 'AD', 'NEG1/2', line=124)
W('37,3503', 0o64734, '', 'AD', 'NEG1/2', line=125)
W('37,3504', 0o57055, '', 'XCH', 'TBASE2', line=126)
# Page 859
W('37,3505', 0o34361, '', 'CAF', 'DEC17', '2.21SPOT FOR R10,R11', line=128)
W('37,3506', 0o54001, '', 'TS', 'L', line=129)
W('37,3507', 0o40000, '', 'COM', line=130)
W('37,3510', 0o52755, '', 'DXCH', '-PHASE2', line=131)

W('37,3511', 0o36007, '', 'CAF', 'OCT24', 'FIRST R10,R11 IN .200 SECONDS', line=133)
W('37,3512', 0o05203, '', 'TC', 'WAITLIST', line=134)
#   EBANK= UNIT/R/
W('37,3513', 0o02006, '', '2CADR', 'R10,R11', kind='data', line=136)
W('37,3514', 0o42067, kind='data', line=136)

W('37,3515', 0o34751, 'MAKEACCS', 'CA', 'FOUR', line=138)
W('37,3516', 0o13436, '', 'TCF', 'GOREADAX', 'DO PHASE CHANGE AND RECALL READACCS', line=139)

W('37,3517', 0o00006, 'AVEGOUT', 'EXTEND', line=141)
W('37,3520', 0o33536, '', 'DCA', 'AVOUTCAD', 'SET UP FINAL SERVICER EXIT', line=142)
W('37,3521', 0o53253, '', 'DXCH', 'AVGEXIT', line=143)

W('37,3522', 0o34751, '', 'CA', 'FOUR', 'SET 5.4 SPOT FOR REREADAC AND SERVICER', line=145)
W('37,3523', 0o03525, '', 'TC', 'GNUTFAZ5', 'IF REREADAC IS CALLED, IT WILL EXIT', line=146)
W('37,3524', 0o05261, '', 'TC', 'TASKOVER', 'END TASK WITHOUT CALLING READACCS', line=147)

W('37,3525', 0o54001, 'GNUTFAZ5', 'TS', 'L', 'SAVE INPUT IN L', line=149)
W('37,3526', 0o40025, '', 'CS', 'TIME1', line=150)
W('37,3527', 0o55063, '', 'TS', 'TBASE5', 'SET TBASE5', line=151)
W('37,3530', 0o13532, '', 'TCF', '+2', line=152)

W('37,3531', 0o54001, 'GNUFAZE5', 'TS', 'L', 'SAVE INPUT IN L', line=154)
W('37,3532', 0o40001, '', 'CS', 'L', '-PHASE IN A, PHASE IN L.', line=155)
W('37,3533', 0o52763, '', 'DXCH', '-PHASE5', 'SET -PHASE5,PHASE5', line=156)
W('37,3534', 0o00002, '', 'TC', 'Q', line=157)

#   EBANK= DVCNTR
W('37,3535', 0o03661, 'AVOUTCAD', '2CADR', 'AVGEND', kind='data', line=160)
W('37,3536', 0o44067, kind='data', line=160)

W('37,3537', 0o65772, 'ENDJBCAD', 'CADR', 'SERVEXIT +2', kind='data', line=162)

W('37,3540', 0o37771, 'OCT37771', 'OCT', '37771', kind='data', line=164)

#   BANK 33
#   SETLOC SERVICES
#   BANK

#   COUNT* $$/SERV

# Page 860
# ************* SERVICER ****************

W('33,2206', 0o05353, 'SERVICER', 'TC', 'PHASCHNG', 'RESTART REREADAC + SERVICER', line=175)
W('33,2207', 0o16035, '', 'OCT', '16035', kind='data', line=176)
W('33,2210', 0o20000, '', 'OCT', '20000', kind='data', line=177)
#   EBANK= DVCNTR
W('33,2211', 0o02217, '', '2CADR', 'GETABVAL', kind='data', line=179)
W('33,2212', 0o66067, kind='data', line=179)

W('33,2213', 0o37716, '', 'CAF', 'PRIO31', 'INITIALIZE 1/PIPADT IN CASE RESTART HAS', line=181)
W('33,2214', 0o55075, '', 'TS', '1/PIPADT', 'CAUSED LASTBIAS TO BE SKIPPED.', line=182)

W('33,2215', 0o04616, '', 'TC', 'BANKCALL', 'PIPA COMPENSATION CALL', line=184)
W('33,2216', 0o15263, '', 'CADR', '1/PIPA', kind='data', line=185)

W('33,2217', 0o06037, 'GETABVAL', 'TC', 'INTPRET', line=187)
W('33,2220', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=188)
W('33,2221', 0o00325, '', '', 'DELV', kind='operand', line=189)
W('33,2222', 0o77776, '', 'EXIT', kind='interp', line=190)
W('33,2223', 0o30154, '', 'CA', 'MPAC', line=191)
W('33,2224', 0o55246, '', 'TS', 'ABDELV', 'ABDELV = CM/SEC*2(-14).', line=192)
W('33,2225', 0o00006, '', 'EXTEND', line=193)
W('33,2226', 0o72020, '', 'MP', 'KPIP', line=194)
W('33,2227', 0o53514, '', 'DXCH', 'ABDVCONV', 'ABDVCONV = M/CS * 2(-5).', line=195)
W('33,2230', 0o00006, '', 'EXTEND', line=196)
W('33,2231', 0o31245, '', 'DCA', 'MASS', line=197)
W('33,2232', 0o53571, '', 'DXCH', 'MASS1', 'INITIALIZE MASS1 IN CASE WE SKIP MASSMON', line=198)
W('33,2233', 0o40104, 'MASSMON', 'CS', 'FLAGWRD8', 'ARE WE ON THE SURFACE?', line=199)
W('33,2234', 0o74744, '', 'MASK', 'SURFFBIT', line=200)
W('33,2235', 0o00006, '', 'EXTEND', line=201)
W('33,2236', 0o12254, '', 'BZF', 'MOONSPOT', 'YES:  BYPASS MASS MESS', line=202)

W('33,2237', 0o30106, '', 'CA', 'FLGWRD10', 'NO:  WHICH VEX SHOULD BE USED?', line=204)
W('33,2240', 0o74737, '', 'MASK', 'APSFLBIT', line=205)
W('33,2241', 0o10000, '', 'CCS', 'A', line=206)
W('33,2242', 0o00006, '', 'EXTEND', '', 'IF EXTEND IS EXECUTED, APSVEX --> A,', line=207)
W('33,2243', 0o32001, '', 'DCA', 'APSVEX', '      OTHERWISE DPSVEX --> A', line=208)
W('33,2244', 0o54002, '', 'TS', 'Q', line=209)

W('33,2245', 0o00006, '', 'EXTEND', line=211)
W('33,2246', 0o31514, '', 'DCA', 'ABDVCONV', line=212)
W('33,2247', 0o00006, '', 'EXTEND', line=213)
W('33,2250', 0o10002, 'OCT10002', 'DV', 'Q', 'WHERE APPROPRIATE VEX RESIDES', line=214)
W('33,2251', 0o00006, '', 'EXTEND', line=215)
W('33,2252', 0o71244, '', 'MP', 'MASS', line=216)
W('33,2253', 0o21571, '', 'DAS', 'MASS1', line=217)

W('33,2254', 0o32021, 'MOONSPOT', 'CA', 'KPIP1', 'TP MPAC = ABDELV AT 2(14) CM/SEC', line=219)
W('33,2255', 0o07307, '', 'TC', 'SHORTMP', 'MULTIPLY BY KPIP1 TO GET', line=220)
# Page 861
W('33,2256', 0o52155, '', 'DXCH', 'MPAC', 'ABDELV AT 2(7) M/CS', line=222)
W('33,2257', 0o21510, '', 'DAS', 'DVTOTAL', 'UPDATE DVTOTAL FOR DISPLAY', line=223)

W('33,2260', 0o02440, '', 'TC', 'TMPTOSPT', line=225)

W('33,2261', 0o04616, '', 'TC', 'BANKCALL', line=227)
W('33,2262', 0o47615, '', 'CADR', 'QUICTRIG', kind='data', line=228)

W('33,2263', 0o32414, '', 'CAF', 'XNBPIPAD', line=230)
W('33,2264', 0o04616, '', 'TC', 'BANKCALL', line=231)
W('33,2265', 0o20037, '', 'CADR', 'FLESHPOT', kind='data', line=232)
W('33,2266', 0o06037, '', 'TC', 'INTPRET', line=233)
W('33,2267', 0o45014, 'AVERAGEG', 'BON', 'CALL', kind='interp', line=234)
W('33,2270', 0o03307, '', '', 'MUNFLAG', kind='operand', line=235)
W('33,2271', 0o67032, '', '', 'RVBOTH', kind='operand', line=236)
W('33,2272', 0o66776, '', '', 'CALCRVG', kind='operand', line=237)
W('33,2273', 0o77776, '', 'EXIT', kind='interp', line=238)
W('33,2274', 0o03552, 'GOSERV', 'TC', 'QUIKFAZ5', line=239)

W('33,2275', 0o02423, 'COPYCYCL', 'TC', 'COPYCYC', line=241)

# CA      ZERO            # A IS ZERO ON RETURN FROM COPYCYC
W('33,2276', 0o55160, '', 'TS', 'PIPATMPX', line=244)
W('33,2277', 0o55161, '', 'TS', 'PIPATMPY', line=245)
W('33,2300', 0o55162, '', 'TS', 'PIPATMPZ', line=246)

W('33,2301', 0o44741, '', 'CS', 'STEERBIT', 'CLEAR STEERSW PRIOR TO DVMON.', line=248)
W('33,2302', 0o70076, '', 'MASK', 'FLAGWRD2', line=249)
W('33,2303', 0o54076, '', 'TS', 'FLAGWRD2', line=250)

W('33,2304', 0o34745, '', 'CAF', 'IDLEFBIT', 'IS THE IDLE FLAG SET?', line=252)
W('33,2305', 0o70103, '', 'MASK', 'FLAGWRD7', line=253)
W('33,2306', 0o10000, '', 'CCS', 'A', line=254)
W('33,2307', 0o12342, '', 'TCF', 'NODVMON1', 'IDLEFLAG = 1, HENCE SET AUXFLAG TO 0.', line=255)

W('33,2310', 0o40102, '', 'CS', 'FLAGWRD6', line=257)
W('33,2311', 0o74752, '', 'MASK', 'AUXFLBIT', line=258)
W('33,2312', 0o10000, '', 'CCS', 'A', line=259)
W('33,2313', 0o12346, '', 'TCF', 'NODVMON2', 'AUXFLAG = 0, HENCE SET AUXFLAG TO 1.', line=260)

W('33,2314', 0o41251, 'DVMON', 'CS', 'DVTHRUSH', line=262)
W('33,2315', 0o61246, '', 'AD', 'ABDELV', line=263)
W('33,2316', 0o00006, '', 'EXTEND', line=264)
W('33,2317', 0o62352, '', 'BZMF', 'LOTHRUST', line=265)

W('33,2320', 0o40076, '', 'CS', 'FLAGWRD2', 'SET STEERSW.', line=267)
W('33,2321', 0o74741, '', 'MASK', 'STEERBIT', line=268)
W('33,2322', 0o26076, '', 'ADS', 'FLAGWRD2', line=269)

W('33,2323', 0o34753, 'DVCNTSET', 'CAF', 'ONE', 'ALLOW TWO PASSES MAXIMUM NOW THAT', line=271)
# Page 862
W('33,2324', 0o55515, '', 'TS', 'DVCNTR', 'THRUST HAS BEEN DETECTED.', line=273)

W('33,2325', 0o30106, '', 'CA', 'FLGWRD10', 'BRANCH IF APSFLAG IS SET.', line=275)
W('33,2326', 0o74737, '', 'MASK', 'APSFLBIT', line=276)
W('33,2327', 0o10000, '', 'CCS', 'A', line=277)
W('33,2330', 0o12375, '', 'TCF', 'USEJETS', line=278)

W('33,2331', 0o34743, '', 'CA', 'BIT9', 'CHECK GIMBAL FAIL BIT', line=280)
W('33,2332', 0o00006, '', 'EXTEND', line=281)
W('33,2333', 0o02032, '', 'RAND', 'CHAN32', line=282)
W('33,2334', 0o00006, '', 'EXTEND', line=283)
W('33,2335', 0o12375, '', 'BZF', 'USEJETS', line=284)

W('33,2336', 0o44736, 'USEGTS', 'CS', 'USEQRJTS', line=286)
W('33,2337', 0o70111, '', 'MASK', 'DAPBOOLS', line=287)
W('33,2340', 0o54111, '', 'TS', 'DAPBOOLS', line=288)
W('33,2341', 0o12400, '', 'TCF', 'SERVOUT', line=289)

W('33,2342', 0o44752, 'NODVMON1', 'CS', 'AUXFLBIT', 'SET AUXFLAG TO 0.', line=291)
W('33,2343', 0o70102, '', 'MASK', 'FLAGWRD6', line=292)
W('33,2344', 0o54102, '', 'TS', 'FLAGWRD6', line=293)
W('33,2345', 0o12375, '', 'TCF', 'USEJETS', line=294)
W('33,2346', 0o40102, 'NODVMON2', 'CS', 'FLAGWRD6', 'SET AUXFLAG TO 1.', line=295)
W('33,2347', 0o74752, '', 'MASK', 'AUXFLBIT', line=296)
W('33,2350', 0o26102, '', 'ADS', 'FLAGWRD6', line=297)
W('33,2351', 0o12375, '', 'TCF', 'USEJETS', line=298)

W('33,2352', 0o03552, 'LOTHRUST', 'TC', 'QUIKFAZ5', line=300)
W('33,2353', 0o11515, '', 'CCS', 'DVCNTR', line=301)
W('33,2354', 0o12366, '', 'TCF', 'DECCNTR', line=302)

W('33,2355', 0o10761, '', 'CCS', 'PHASE4', 'COMFAIL JOB ACTIVE?', line=304)
W('33,2356', 0o12400, '', 'TCF', 'SERVOUT', "YES:  WON'T NEED ANOTHER.", line=305)

W('33,2357', 0o05353, '', 'TC', 'PHASCHNG', '4.37SPOT FOR COMFAIL.', line=307)
W('33,2360', 0o00374, '', 'OCT', '00374', kind='data', line=308)

W('33,2361', 0o37713, '', 'CAF', 'PRIO25', line=310)
W('33,2362', 0o05072, '', 'TC', 'NOVAC', line=311)
#   EBANK= WHICH
W('33,2363', 0o02571, '', '2CADR', 'COMFAIL', kind='data', line=313)
W('33,2364', 0o74067, kind='data', line=313)

W('33,2365', 0o12400, '', 'TCF', 'SERVOUT', line=315)

W('33,2366', 0o55570, 'DECCNTR', 'TS', 'DVCNTR1', line=317)
W('33,2367', 0o03552, '', 'TC', 'QUIKFAZ5', line=318)
W('33,2370', 0o31570, '', 'CA', 'DVCNTR1', line=319)
W('33,2371', 0o55515, '', 'TS', 'DVCNTR', line=320)
W('33,2372', 0o00004, '', 'INHINT', line=321)
W('33,2373', 0o04674, '', 'TC', 'IBNKCALL', 'IF THRUST IS LOW, NO STEERING IS DONE', line=322)
# Page 863
W('33,2374', 0o40165, '', 'CADR', 'STOPRATE', 'AND THE DESIRED RATES ARE SET TO ZERO.', kind='data', line=324)
W('33,2375', 0o40111, 'USEJETS', 'CS', 'DAPBOOLS', line=325)
W('33,2376', 0o74736, '', 'MASK', 'USEQRJTS', line=326)
W('33,2377', 0o26111, '', 'ADS', 'DAPBOOLS', line=327)
W('33,2400', 0o00003, 'SERVOUT', 'RELINT', line=328)
W('33,2401', 0o04616, '', 'TC', 'BANKCALL', line=329)
W('33,2402', 0o40457, '', 'CADR', '1/ACCS', kind='data', line=330)

W('33,2403', 0o30167, '', 'CA', 'PRIORITY', line=332)
W('33,2404', 0o75004, '', 'MASK', 'LOW9', line=333)
W('33,2405', 0o54166, '', 'TS', 'PUSHLOC', line=334)
W('33,2406', 0o22007, '', 'ZL', line=335)
W('33,2407', 0o52121, '', 'DXCH', 'FIXLOC', 'FIXLOC AND DVFIND', line=336)

W('33,2410', 0o03552, '', 'TC', 'QUIKFAZ5', line=338)
W('33,2411', 0o00006, '', 'EXTEND', '', 'EXIT TO SELECTED ROUTINE WHETHER THERE', line=339)
W('33,2412', 0o31253, '', 'DCA', 'AVGEXIT', 'IS THRUST OR NOT.  THE STATE OF STEERSW', line=340)
W('33,2413', 0o52006, '', 'DXCH', 'Z', 'WILL CONVEY THIS INFORMATION.', line=341)

W('33,2414', 0o02145, 'XNBPIPAD', 'ECADR', 'XNBPIP', kind='data', line=343)

#   BANK 32
#   SETLOC SERV2
#   BANK
#   COUNT* $$/SERV

W('22,3661', 0o31235, 'AVGEND', 'CA', 'PIPTIME +1', 'FINAL AVERAGE G EXIT', line=350)
W('22,3662', 0o55075, '', 'TS', '1/PIPADT', 'SET UP FREE FALL GYRO COMPENSATION.', line=351)

W('22,3663', 0o05504, '', 'TC', 'UPFLAG', 'SET DRIFT FLAG.', line=353)
W('22,3664', 0o00036, '', 'ADRES', 'DRIFTFLG', kind='data', line=354)

W('22,3665', 0o04616, '', 'TC', 'BANKCALL', line=356)
W('22,3666', 0o17310, '', 'CADR', 'PIPFREE', kind='data', line=357)

W('22,3667', 0o44743, '', 'CS', 'BIT9', line=359)
W('22,3670', 0o00006, '', 'EXTEND', line=360)
W('22,3671', 0o03011, '', 'WAND', 'DSALMOUT', line=361)

W('22,3672', 0o05327, '', 'TC', '2PHSCHNG', line=363)
W('22,3673', 0o00005, '', 'OCT', '5', 'GROUP 5 OFF', kind='data', line=364)
W('22,3674', 0o05022, '', 'OCT', '05022', 'GROUP 2 ON', kind='data', line=365)
W('22,3675', 0o20000, '', 'OCT', '20000', kind='data', line=366)

W('22,3676', 0o06037, '', 'TC', 'INTPRET', line=368)
W('22,3677', 0o43014, '', 'SET', 'CLEAR', kind='interp', line=369)
W('22,3700', 0o01464, '', '', 'NOR29FLG', 'SHUT OFF R29 WHEN SERVICER ENDS.', kind='operand', line=370)
W('22,3701', 0o03664, '', '', 'SWANDISP', 'SHUT OFF R10 WHEN SERVICER ENDS.', kind='operand', line=371)
W('22,3702', 0o45014, '', 'CLEAR', 'CALL', 'RESET MUNFLAG.', kind='interp', line=372)
W('22,3703', 0o03267, '', '', 'MUNFLAG', kind='operand', line=373)
# Page 864
W('22,3704', 0o27467, '', '', 'AVETOMID', kind='operand', line=375)
W('22,3705', 0o77414, '', 'CLEAR', 'EXIT', kind='interp', line=376)
W('22,3706', 0o03671, '', '', 'V37FLAG', kind='operand', line=377)
W('22,3707', 0o31260, 'AVERTRN', 'CA', 'OUTROUTE', 'RETURN TO DESIRED POINT.', line=378)
W('22,3710', 0o04640, '', 'TC', 'BANKJUMP', line=379)

S('OUTGOAVE', 'equals', 0o55707, line=381)
S('DVCNTR1', 'equals', 0o3570, line=382)

# Page 865
#   SETLOC SERV3
#   BANK
#   COUNT* $$/SERV

W('27,3321', 0o00006, 'SERVIDLE', 'EXTEND', '', 'DISCONNECT SERVICER FROM ALL GUIDANCE', line=389)
W('27,3322', 0o33357, '', 'DCA', 'SVEXTADR', line=390)
W('27,3323', 0o53253, '', 'DXCH', 'AVGEXIT', line=391)

W('27,3324', 0o40103, '', 'CS', 'FLAGWRD7', 'DISCONNECT THE DELTA-V MONITOR', line=393)
W('27,3325', 0o74745, '', 'MASK', 'IDLEFBIT', line=394)
W('27,3326', 0o26103, '', 'ADS', 'FLAGWRD7', line=395)

W('27,3327', 0o34735, '', 'CAF', 'LRBYBIT', 'TERMINATE R12 IS RUNNING.', line=397)
W('27,3330', 0o54107, '', 'TS', 'FLGWRD11', line=398)

W('27,3331', 0o00006, '', 'EXTEND', line=400)
W('27,3332', 0o34755, '', 'DCA', 'NEG0', line=401)
W('27,3333', 0o52753, '', 'DXCH', '-PHASE1', line=402)

W('27,3334', 0o30102, '', 'CA', 'FLAGWRD6', 'DO NOT TURN OFF PHASE 2 IF MUNFLAG SET.', line=404)
W('27,3335', 0o74744, '', 'MASK', 'MUNFLBIT', line=405)
W('27,3336', 0o10000, '', 'CCS', 'A', line=406)
W('27,3337', 0o13343, '', 'TCF', '+4', line=407)

W('27,3340', 0o00006, '', 'EXTEND', line=409)
W('27,3341', 0o34755, '', 'DCA', 'NEG0', line=410)
W('27,3342', 0o52755, '', 'DXCH', '-PHASE2', line=411)

W('27,3343', 0o00006, '', 'EXTEND', line=413)
W('27,3344', 0o34755, '', 'DCA', 'NEG0', line=414)
W('27,3345', 0o52757, '', 'DXCH', '-PHASE3', line=415)

W('27,3346', 0o00006, '', 'EXTEND', line=417)
W('27,3347', 0o34755, '', 'DCA', 'NEG0', line=418)
W('27,3350', 0o52765, '', 'DXCH', '-PHASE6', line=419)

W('27,3351', 0o34764, '', 'CAF', 'OCT33', '4.33SPOT FOR GOP00FIX', line=421)
W('27,3352', 0o54001, '', 'TS', 'L', line=422)
W('27,3353', 0o40000, '', 'COM', line=423)
W('27,3354', 0o52761, '', 'DXCH', '-PHASE4', line=424)

W('27,3355', 0o15644, '', 'TCF', 'WHIMPER', 'PERFORM A SOFTWARE RESTART AND PROCEED', line=426)
# TO GOTOPOOH WHILE SERVICER CONTINUES TO
# RUN, ALBEIT IN A GROUND STATE WHERE
# ONLY STATE-VECTOR DEPENDENT FUNCTIONS
# ARE MAINTAINED.

#   EBANK= DVCNTR
# Page 866
W('27,3356', 0o03770, 'SVEXTADR', '2CADR', 'SERVEXIT', kind='data', line=434)
W('27,3357', 0o64067, kind='data', line=434)

#   BANK 32
#   SETLOC SERV
#   BANK
#   COUNT* $$/SERV

W('32,3770', 0o05353, 'SERVEXIT', 'TC', 'PHASCHNG', line=441)
W('32,3771', 0o00035, '', 'OCT', '00035', kind='data', line=442)

W('32,3772', 0o15155, '', 'TCF', 'ENDOFJOB', line=444)

#   BANK 23
#   SETLOC NORMLIZ
#   BANK

#   COUNT* $$/SERV

# Page 867
W('23,2461', 0o06037, 'NORMLIZE', 'TC', 'INTPRET', line=453)
W('23,2462', 0o43175, '', 'VLOAD', 'BOFF', kind='interp', line=454)
W('23,2463', 0o03545, '', '', 'RN1', kind='operand', line=455)
W('23,2464', 0o03347, '', '', 'MUNFLAG', kind='operand', line=456)
W('23,2465', 0o66415, '', '', 'NORMLIZ1', kind='operand', line=457)
W('23,2466', 0o64252, '', 'VSL6', 'MXV', kind='interp', line=458)
W('23,2467', 0o01734, '', '', 'REFSMMAT', kind='operand', line=459)
W('23,2470', 0o37521, '', 'STCALL', 'R', kind='interp', line=460)
W('23,2471', 0o67130, '', '', 'MUNGRAV', kind='operand', line=461)
W('23,2472', 0o76575, '', 'VLOAD', 'VSL1', kind='interp', line=462)
W('23,2473', 0o03553, '', '', 'VN1', kind='operand', line=463)
W('23,2474', 0o77721, '', 'MXV', kind='interp', line=464)
W('23,2475', 0o01734, '', '', 'REFSMMAT', kind='operand', line=465)
W('23,2476', 0o27527, '', 'STOVL', 'V', kind='interp', line=466)
W('23,2477', 0o01726, '', '', 'V(CSM)', kind='operand', line=467)
W('23,2500', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=468)
W('23,2501', 0o01720, '', '', 'R(CSM)', kind='operand', line=469)
W('23,2502', 0o03720, '', 'STORE', 'UHYP', kind='interp', line=470)
W('23,2503', 0o77776, 'ASCSPOT', 'EXIT', kind='interp', line=471)
W('23,2504', 0o00006, '', 'EXTEND', '', 'MAKE SURE GROUP 2 IS OFF', line=472)
W('23,2505', 0o34755, '', 'DCA', 'NEG0', line=473)
W('23,2506', 0o52755, '', 'DXCH', '-PHASE2', line=474)

W('23,2507', 0o04635, '', 'TC', 'POSTJUMP', line=476)
W('23,2510', 0o66420, '', 'CADR', 'NORMLIZ2', kind='data', line=477)

#   BANK 33
#   SETLOC SERVICES
#   BANK
#   COUNT* $$/SERV

W('33,2415', 0o77624, 'NORMLIZ1', 'CALL', kind='interp', line=484)
W('33,2416', 0o66730, '', '', 'CALCGRAV', kind='operand', line=485)
W('33,2417', 0o77776, '', 'EXIT', kind='interp', line=486)

W('33,2420', 0o32437, 'NORMLIZ2', 'CA', 'EIGHTEEN', line=488)
W('33,2421', 0o02424, '', 'TC', 'COPYCYC +1', 'DO NOT COPY MASS IN NORMLIZE', line=489)
W('33,2422', 0o05155, '', 'TC', 'ENDOFJOB', line=490)

W('33,2423', 0o36007, 'COPYCYC', 'CA', 'OCT24', 'DEC 20', line=492)
W('33,2424', 0o00004, '', 'INHINT', line=493)
W('33,2425', 0o77747, '', 'MASK', 'NEG1', 'REDUCE BY 1 IF ODD', line=494)
W('33,2426', 0o54061, '', 'TS', 'ITEMP1', line=495)
W('33,2427', 0o00006, '', 'EXTEND', line=496)
W('33,2430', 0o50061, '', 'INDEX', 'ITEMP1', line=497)
W('33,2431', 0o31545, '', 'DCA', 'RN1', line=498)
W('33,2432', 0o50061, '', 'INDEX', 'ITEMP1', line=499)
# Page 868
W('33,2433', 0o53221, '', 'DXCH', 'RN', line=501)
W('33,2434', 0o10061, '', 'CCS', 'ITEMP1', line=502)
W('33,2435', 0o12425, '', 'TCF', 'COPYCYC +2', line=503)
W('33,2436', 0o00002, '', 'TC', 'Q', 'RETURN UNDER INHINT', line=504)

W('33,2437', 0o00022, 'EIGHTEEN', 'DEC', '18', kind='data', line=506)

# Page 869
# ************* PIPA READER *****************
# MOD NO. 00 BY D. LICKLY, DEC. 9 1966
#
# FUNCTIONAL DESCRIPTION
# SUBROUTINE TO READ PIPA COUNTERS, TRYING TO BE VERY CAREFUL SO THAT WILL BE RESTARTABLE.
# PIPA READINGS ARE STORED IN THE VECTOR DELV.  THE HIGH ORDER PART OF EACH COMPONENT CONTAINS THE PIPA READING,
# RESTARTS BEGIN AT REREADAC.
#
# AT THE END OF THE PIPA READER THE CDUS ARE READ AND STORED AS A
# VECTOR IN CDUTEMP.  THE HIGH ORDER PART OF EACH COMPONENT CONTAINS
# THE CDU READING IN 25 COMP IN THE ORDER CDUX,Y,Z.  THE THRUST
# VECTOR ESTIMATOR IN FINDCDUD REQUIRES THE CDUS BE READ AT PIPTIME.
#
# CALLING SEQUENCE AND EXIT
# CALL VIA TC, ISWCALL, ETC.
# EXIT IS VIA Q.
#
# INPUT
# INPUT IS THROUGH THE COUNTERS PIPAX, PIPAY, PIPAZ, AND TIME2.
#
# OUTPUT
# HIGH ORDER COMPONENTS OF THE VECTOR DELV CONTAIN THE PIPA READINGS.
# PIPTIME CONTAINS TIME OF PIPA READING.
#
# DEBRIS (ERASABLE LOCATIONS DESTROYED BY PROGRAM)
# TEMX, TEMY, TEMZ, PIPAGE

#   BANK 37
#   SETLOC SERV1
#   BANK

#   COUNT* $$/SERV

W('37,3541', 0o00006, 'PIPASR', 'EXTEND', line=542)
# Page 870
W('37,3542', 0o30025, '', 'DCA', 'TIME2', line=544)
W('37,3543', 0o53561, '', 'DXCH', 'PIPTIME1', 'CURRENT TIME POSITIVE VALUE', line=545)
W('37,3544', 0o44755, '', 'CS', 'ZERO', 'INITIALIZE THESE AT NEG. ZERO.', line=546)
W('37,3545', 0o55254, '', 'TS', 'TEMX', line=547)
W('37,3546', 0o55255, '', 'TS', 'TEMY', line=548)
W('37,3547', 0o55256, '', 'TS', 'TEMZ', line=549)

W('37,3550', 0o34755, '', 'CA', 'ZERO', line=551)
W('37,3551', 0o54330, '', 'TS', 'DELVZ', line=552)
W('37,3552', 0o54331, '', 'TS', 'DELVZ +1', line=553)
W('37,3553', 0o54326, '', 'TS', 'DELVY', line=554)
W('37,3554', 0o54327, '', 'TS', 'DELVY +1', line=555)
W('37,3555', 0o54325, '', 'TS', 'DELVX +1', line=556)
W('37,3556', 0o55257, '', 'TS', 'PIPAGE', 'SHOW PIPA READING IN PROGRESS', line=557)

W('37,3557', 0o00006, 'REPIP1', 'EXTEND', line=559)
W('37,3560', 0o40040, '', 'DCS', 'PIPAX', 'X AND Y PIPS READ', line=560)
W('37,3561', 0o53255, '', 'DXCH', 'TEMX', line=561)
W('37,3562', 0o52040, '', 'DXCH', 'PIPAX', 'PIPAS SET TO NEG ZERO AS READ.', line=562)
W('37,3563', 0o54324, '', 'TS', 'DELVX', line=563)
W('37,3564', 0o22326, '', 'LXCH', 'DELVY', line=564)

W('37,3565', 0o40041, 'REPIP3', 'CS', 'PIPAZ', 'REPEAT PROCESS FOR Z PIP', line=566)
W('37,3566', 0o57256, '', 'XCH', 'TEMZ', line=567)
W('37,3567', 0o56041, '', 'XCH', 'PIPAZ', line=568)
W('37,3570', 0o54330, 'DODELVZ', 'TS', 'DELVZ', line=569)

W('37,3571', 0o00006, 'REPIP4', 'EXTEND', '', 'COMPUTE GUIDANCE PERIOD', line=571)
W('37,3572', 0o31561, '', 'DCA', 'PIPTIME1', line=572)
W('37,3573', 0o53250, '', 'DXCH', 'PGUIDE', line=573)
W('37,3574', 0o00006, '', 'EXTEND', line=574)
W('37,3575', 0o41235, '', 'DCS', 'PIPTIME', line=575)
W('37,3576', 0o21250, '', 'DAS', 'PGUIDE', line=576)

W('37,3577', 0o30032, '', 'CA', 'CDUX', 'READ CDUS INTO HIGH ORDER CDUTEMPS', line=578)
W('37,3600', 0o55155, '', 'TS', 'CDUTEMPX', line=579)
W('37,3601', 0o30033, '', 'CA', 'CDUY', line=580)
W('37,3602', 0o55156, '', 'TS', 'CDUTEMPY', line=581)
W('37,3603', 0o30034, '', 'CA', 'CDUZ', line=582)
W('37,3604', 0o55157, '', 'TS', 'CDUTEMPZ', line=583)
W('37,3605', 0o30324, '', 'CA', 'DELVX', line=584)
W('37,3606', 0o55160, '', 'TS', 'PIPATMPX', line=585)
W('37,3607', 0o30326, '', 'CA', 'DELVY', line=586)
W('37,3610', 0o55161, '', 'TS', 'PIPATMPY', line=587)
W('37,3611', 0o30330, '', 'CA', 'DELVZ', line=588)
W('37,3612', 0o55162, '', 'TS', 'PIPATMPZ', line=589)

W('37,3613', 0o00002, '', 'TC', 'Q', line=591)

# Page 871
W('37,3614', 0o11257, 'REREADAC', 'CCS', 'PIPAGE', line=594)
W('37,3615', 0o13441, '', 'TCF', 'READACCS', 'PIP READING NOT STARTED.  GO TO BEGINNING', line=595)

W('37,3616', 0o33654, '', 'CAF', 'DONEADR', 'SET UP RETURN FROM PIPASR', line=597)
W('37,3617', 0o54002, '', 'TS', 'Q', line=598)

W('37,3620', 0o10330, '', 'CCS', 'DELVZ', line=600)
W('37,3621', 0o13571, '', 'TCF', 'REPIP4', 'Z DONE, GO DO CDUS', line=601)
W('37,3622', 0o13625, '', 'TCF', '+3', 'Z NOT DONE, CHECK Y.', line=602)
W('37,3623', 0o13571, '', 'TCF', 'REPIP4', line=603)
W('37,3624', 0o13571, '', 'TCF', 'REPIP4', line=604)

W('37,3625', 0o22007, '', 'ZL', line=606)
W('37,3626', 0o10326, '', 'CCS', 'DELVY', line=607)
W('37,3627', 0o13632, '', 'TCF', '+3', line=608)
W('37,3630', 0o13641, '', 'TCF', 'CHKTEMX', 'Y NOT DONE, CHECK X.', line=609)
W('37,3631', 0o13632, '', 'TCF', '+1', line=610)
W('37,3632', 0o22041, '', 'LXCH', 'PIPAZ', 'Y DONE, ZERO Z PIP.', line=611)

W('37,3633', 0o11256, '', 'CCS', 'TEMZ', line=613)
W('37,3634', 0o41256, '', 'CS', 'TEMZ', 'TEMZ NOT = -0, CONTAINS -PIPAZ VALUE.', line=614)
W('37,3635', 0o13570, '', 'TCF', 'DODELVZ', line=615)
W('37,3636', 0o13634, '', 'TCF', '-2', line=616)
W('37,3637', 0o22330, '', 'LXCH', 'DELVZ', 'TEMZ = -0, L HAS ZPIP VALUE.', line=617)
W('37,3640', 0o13571, '', 'TCF', 'REPIP4', line=618)

W('37,3641', 0o11254, 'CHKTEMX', 'CCS', 'TEMX', 'HAS THIS CHANGED', line=620)
W('37,3642', 0o41254, '', 'CS', 'TEMX', 'YES', line=621)
W('37,3643', 0o13646, '', 'TCF', '+3', 'YES', line=622)
W('37,3644', 0o13642, '', 'TCF', '-2', 'YES', line=623)
W('37,3645', 0o13557, '', 'TCF', 'REPIP1', 'NO', line=624)
W('37,3646', 0o54324, '', 'TS', 'DELVX', line=625)

W('37,3647', 0o41255, '', 'CS', 'TEMY', line=627)
W('37,3650', 0o54326, '', 'TS', 'DELVY', line=628)

W('37,3651', 0o44755, '', 'CS', 'ZERO', 'ZERO X AND Y PIPS', line=630)
W('37,3652', 0o52040, '', 'DXCH', 'PIPAX', 'L STILL ZERO FROM ABOVE', line=631)

W('37,3653', 0o13565, '', 'TCF', 'REPIP3', line=633)

W('37,3654', 0o03451, 'DONEADR', 'GENADR', 'PIPSDONE', kind='data', line=635)

# Page 872
#   BANK 33
#   SETLOC SERVICES
#   BANK

#   COUNT* $$/SERV

W('33,2440', 0o31156, 'TMPTOSPT', 'CA', 'CDUTEMPY', 'THIS SUBROUTINE, CALLED BY AN RTB FROM', line=644)
W('33,2441', 0o54766, '', 'TS', 'CDUSPOTY', 'INTERPRETIVE, LOADS THE CDUS CORRESPON-', line=645)
W('33,2442', 0o31157, '', 'CA', 'CDUTEMPZ', 'DING TO PIPTIME INTO THE CDUSPOT VECTOR.', line=646)
W('33,2443', 0o54770, '', 'TS', 'CDUSPOTZ', line=647)
W('33,2444', 0o31155, '', 'CA', 'CDUTEMPX', line=648)
W('33,2445', 0o54772, '', 'TS', 'CDUSPOTX', line=649)
W('33,2446', 0o00002, '', 'TC', 'Q', line=650)

# LRHTASK IS A WAITLIST TASK SET BY READACCS DURING THE DESCENT BRAKING
# PHASE WHEN THE ALT TO THE LUNAR SURFACE IS LESS THAN 25,000 FT.  THIS
# TASK CLEARS THE ALTITUDE MEASUREMENT MADE DISCRETE AND INITIATES THE
# LANDING RADAR MEASUREMENT JOB (LRHJOB) TO TAKE A ALTITUDE MEASUREMENT
# 50 MS PRIOR TO THE NEXT READACCS TASK.

#   BANK 21
#   SETLOC R10
#   BANK

#   COUNT* $$/SERV

W('21,2130', 0o40107, 'LRHTASK', 'CS', 'FLGWRD11', line=664)
W('21,2131', 0o74735, '', 'MASK', 'LRBYBIT', line=665)
W('21,2132', 0o00006, '', 'EXTEND', line=666)
W('21,2133', 0o12150, '', 'BZF', 'GRP2OFF', 'LR BYPASS SET -- BYPASS ALL LR READING.', line=667)

W('21,2134', 0o34746, '', 'CA', 'READLBIT', line=669)
W('21,2135', 0o70107, '', 'MASK', 'FLGWRD11', 'IS READLR FLAG SET?', line=670)
W('21,2136', 0o00006, '', 'EXTEND', line=671)
W('21,2137', 0o12150, '', 'BZF', 'GRP2OFF', 'NO.  BYPASS LR READ.', line=672)

W('21,2140', 0o40107, '', 'CS', 'FLGWRD11', line=674)
W('21,2141', 0o74742, '', 'MASK', 'NOLRRBIT', 'IS LR READ INHIBITED?', line=675)
W('21,2142', 0o00006, '', 'EXTEND', line=676)
W('21,2143', 0o12150, '', 'BZF', 'GRP2OFF', 'YES.  BYPASS LR READ.', line=677)

W('21,2144', 0o37720, '', 'CA', 'PRIO32', 'LR READ OK.  SET JOB TO DO IT', line=679)
W('21,2145', 0o05072, '', 'TC', 'NOVAC', 'ABOUT 50 MS. PRIOR TO PIPA READ.', line=680)
#   EBANK= HMEAS
W('21,2146', 0o03716, '', '2CADR', 'LRHJOB', kind='data', line=682)
W('21,2147', 0o70067, kind='data', line=682)

W('21,2150', 0o00006, 'GRP2OFF', 'EXTEND', line=684)
W('21,2151', 0o34755, '', 'DCA', 'NEG0', line=685)
W('21,2152', 0o52755, '', 'DXCH', '-PHASE2', line=686)
W('21,2153', 0o12021, '', 'TCF', 'R10,R11A', line=687)

#   BANK 33
#   SETLOC SERVICES
#   BANK
# Page 873
#   COUNT* $$/SERV

# HIGATASK IS ENTERED APPROXIMATELY 6 SECS PRIOR TO HIGATE DURING THE
# DESCENT PHASE.  HIGATASK SETS THE HIGATE FLAG (BIT11) AND THE LR INHIBIT
# FLAG (BIT10) IN LRSTAT.  THE HIGATJOB IS SET UP TO REPOSITION THE LR
# ANTENNA FROM POSITION 1 TO POSITION 2.  IF THE REPOSITIONING IS
# SUCCESSFUL THE ALT BEAM AND VELOCITY BEAMS ARE TRANSFORMED TO THE NEW
# ORIENTATION IN NB COORDINATES AND STORED IN ERASABLE.

W('33,2447', 0o00004, 'HIGATASK', 'INHINT', line=702)
W('33,2450', 0o45015, '', 'CS', 'PRIO3', 'SET HIGATE AND LR INHIBIT FLAGS', line=703)
W('33,2451', 0o70107, '', 'MASK', 'FLGWRD11', line=704)
W('33,2452', 0o65015, '', 'AD', 'PRIO3', line=705)
W('33,2453', 0o54107, '', 'TS', 'FLGWRD11', line=706)
W('33,2454', 0o37720, '', 'CAF', 'PRIO32', line=707)
W('33,2455', 0o05105, '', 'TC', 'FINDVAC', 'SET LR POSITIONING JOB (POS2)', line=708)
#   EBANK= HMEAS
W('33,2456', 0o03670, '', '2CADR', 'HIGATJOB', kind='data', line=710)
W('33,2457', 0o66067, kind='data', line=710)

W('33,2460', 0o12540, '', 'TCF', 'CONTSERV', 'CONTINUE SERVICER', line=712)

# Page 874
# MUNRETRN IS THE RETURN LOC FROM SPECIAL AVE G ROUTINE (MUNRVG)

W('33,2461', 0o77776, 'MUNRETRN', 'EXIT', kind='interp', line=717)

W('33,2462', 0o40107, '', 'CS', 'FLGWRD11', line=719)
W('33,2463', 0o74735, '', 'MASK', 'LRBYBIT', line=720)
W('33,2464', 0o00006, '', 'EXTEND', line=721)
W('33,2465', 0o12546, '', 'BZF', 'COPYCYC1', 'BYPASS LR LOGIC IF BIT15 IS SET.', line=722)

W('33,2466', 0o34746, '', 'CA', 'READLBIT', 'SEE IF ALT < 35000 FT LAST CYCLE', line=724)
W('33,2467', 0o70107, '', 'MASK', 'FLGWRD11', line=725)
W('33,2470', 0o00006, '', 'EXTEND', line=726)
W('33,2471', 0o12721, '', 'BZF', '35KCHK', 'ALT WAS > 35000 FT LAST CYCLE   CHK NOW', line=727)

W('33,2472', 0o34743, '', 'CAF', 'XORFLBIT', 'WERE WE BELOW 30000 FT LAST PASS?', line=729)
W('33,2473', 0o70107, '', 'MASK', 'FLGWRD11', line=730)
W('33,2474', 0o00006, '', 'EXTEND', line=731)
W('33,2475', 0o12710, '', 'BZF', 'XORCHK', 'NO -- TEST THIS PASS', line=732)
W('33,2476', 0o34741, 'HITEST', 'CAF', 'PSTHIBIT', 'CHECK FOR HIGATE', line=733)
W('33,2477', 0o70107, '', 'MASK', 'FLGWRD11', line=734)
W('33,2500', 0o00006, '', 'EXTEND', line=735)
W('33,2501', 0o12515, '', 'BZF', 'HIGATCHK', 'NOT AT HIGATE LAST CYCLE -- CHK THIS CYCLE', line=736)

W('33,2502', 0o34745, 'POS2CHK', 'CAF', 'BIT7', 'VERIFY LR IN POS2', line=738)
W('33,2503', 0o00006, '', 'EXTEND', line=739)
W('33,2504', 0o02033, '', 'RAND', 'CHAN33', line=740)
W('33,2505', 0o00006, '', 'EXTEND', line=741)
W('33,2506', 0o13155, '', 'BZF', 'UPDATCHK', 'IT IS -- CHECK FOR LR UPDATE', line=742)
W('33,2507', 0o34737, '', 'CAF', 'BIT13', line=743)
W('33,2510', 0o00006, '', 'EXTEND', line=744)
W('33,2511', 0o02012, '', 'RAND', 'CHAN12', line=745)
W('33,2512', 0o00006, '', 'EXTEND', line=746)
W('33,2513', 0o12536, '', 'BZF', 'LRPOSALM', 'LR NOT IN POS2 OR REPOSITIONING -- BAD', line=747)
W('33,2514', 0o12540, '', 'TCF', 'CONTSERV', 'LR BEING REPOSITIONED -- CONTINUE SERV', line=748)

W('33,2515', 0o31642, 'HIGATCHK', 'CA', 'TTF/8', 'IS TTF > CRITERION?  (TTF IS NEGATIVE)', line=750)
W('33,2516', 0o61427, '', 'AD', 'RPCRTIME', line=751)
W('33,2517', 0o00006, '', 'EXTEND', line=752)
W('33,2520', 0o62531, '', 'BZMF', 'POS1CHK', 'NO', line=753)

W('33,2521', 0o34741, '', 'CA', 'EBANK4', 'MUST SWITCH EBANKS', line=755)
W('33,2522', 0o56003, '', 'XCH', 'EBANK', line=756)
W('33,2523', 0o54001, '', 'TS', 'L', 'SAVE IN L', line=757)

#   EBANK= XNBPIP
W('33,2524', 0o41545, '', 'CS', 'XNBPIP', 'UXBXP IN GSOP CH5', line=760)
#   EBANK= DVCNTR
W('33,2525', 0o22003, '', 'LXCH', 'EBANK', 'RESTORE EBANK', line=762)
W('33,2526', 0o61430, '', 'AD', 'RPCRTQSW', 'QSW - UXBXP', line=763)
# Page 875

W('33,2527', 0o00006, '', 'EXTEND', line=766)
W('33,2530', 0o62447, '', 'BZMF', 'HIGATASK', 'IF UXBXP > QSW, THEN REPOSITION', line=767)

W('33,2531', 0o34746, 'POS1CHK', 'CAF', 'BIT6', 'HIGATE NOT IN SIGHT -- DO POS1 CHK', line=769)
W('33,2532', 0o00006, '', 'EXTEND', line=770)
W('33,2533', 0o02033, '', 'RAND', '33', line=771)
W('33,2534', 0o00006, '', 'EXTEND', line=772)
W('33,2535', 0o13155, '', 'BZF', 'UPDATCHK', 'LR IN POS1 -- CHECK FOR LR UPDATE', line=773)

W('33,2536', 0o05567, 'LRPOSALM', 'TC', 'ALARM', 'LR NOT IN PROPER POS-ALARM-BYPASS UPDATE', line=775)
W('33,2537', 0o00511, '', 'OCT', '511', 'AND CONTINUE SERVICER', kind='data', line=776)
W('33,2540', 0o00004, 'CONTSERV', 'INHINT', line=777)
W('33,2541', 0o43154, '', 'CS', 'BITS4-7', line=778)
W('33,2542', 0o70107, '', 'MASK', 'FLGWRD11', 'CLEAR LR MEASUREMENT MADE DISCRETES.', line=779)
W('33,2543', 0o54107, '', 'TS', 'FLGWRD11', line=780)

W('33,2544', 0o04674, '', 'TC', 'IBNKCALL', 'SET LR LITES PROPERLY', line=782)
W('33,2545', 0o53607, '', 'CADR', 'R12LITES', kind='data', line=783)

# Page 876
W('33,2546', 0o03552, 'COPYCYC1', 'TC', 'QUIKFAZ5', line=786)

W('33,2547', 0o30077, 'R29?', 'CA', 'FLAGWRD3', line=788)
W('33,2550', 0o75014, '', 'MASK', 'NR29&RDR', line=789)
W('33,2551', 0o10000, '', 'CCS', 'A', 'IS NOR29FLG OR READRFLG SET?', line=790)
W('33,2552', 0o12564, '', 'TCF', 'R29NODES', "YES, SO DON'T DESIGNATE.", line=791)

W('33,2553', 0o30110, '', 'CA', 'RADMODES', 'NO, SO R29 IS CALLED FOR.', line=793)
W('33,2554', 0o72250, '', 'MASK', 'OCT10002', 'IS THE RR NOT ZEROING ITS CDUS, AND', line=794)
W('33,2555', 0o10000, '', 'CCS', 'A', 'IS THE RENDEZVOUS RADAR IN AUTO MODE?', line=795)
W('33,2556', 0o12564, '', 'TCF', 'R29NODES', "NO, SO DON'T DESIGNATE.", line=796)

W('33,2557', 0o30110, '', 'CA', 'RADMODES', line=798)
W('33,2560', 0o77710, '', 'MASK', 'PRIO22', line=799)
W('33,2561', 0o10000, '', 'CCS', 'A', 'IS RR REPOSITIONING OR REMODING?', line=800)
W('33,2562', 0o12570, '', 'TCF', 'NOR29NOW', 'YES:  COME BACK IN 2 SECONDS & TRY AGAIN.', line=801)

W('33,2563', 0o12045, '', 'TCF', 'R29', line=803)

W('33,2564', 0o00004, 'R29NODES', 'INHINT', '', 'R29 NOT ALLOWED THIS CYCLE.', line=805)
W('33,2565', 0o44742, '', 'CS', 'DESIGBIT', 'SHOW THAT DESIGNATION IS OFF.', line=806)
W('33,2566', 0o70110, '', 'MASK', 'RADMODES', line=807)
W('33,2567', 0o54110, '', 'TS', 'RADMODES', line=808)

W('33,2570', 0o06037, 'NOR29NOW', 'TC', 'INTPRET', 'INTPRET DOES A RELINT.', line=810)
W('33,2571', 0o51575, '', 'VLOAD', 'ABVAL', 'MPAC = ABVAL( NEW SM. POSITION VECTOR )', kind='interp', line=811)
W('33,2572', 0o03573, '', '', 'R1S', kind='operand', line=812)
W('33,2573', 0o45206, '', 'PUSH', 'DSU', '                              (2)', kind='interp', line=813)
W('33,2574', 0o02333, '', '', '/LAND/', kind='operand', line=814)
W('33,2575', 0o03535, '', 'STORE', 'HCALC', 'NEW HCALC*2(24)M.', kind='interp', line=815)
W('33,2576', 0o03775, '', 'STORE', 'HCALC1', kind='interp', line=816)
W('33,2577', 0o47075, '', 'DMPR', 'RTB', kind='interp', line=817)
W('33,2600', 0o26026, '', '', 'ALTCONV', kind='operand', line=818)
W('33,2601', 0o21612, '', '', 'SGNAGREE', kind='operand', line=819)
W('33,2602', 0o27742, '', 'STOVL', 'ALTBITS', 'ALTITUDE FOR R10 IN BIT UNITS.', kind='interp', line=820)
W('33,2603', 0o03537, '', '', 'UNIT/R/', kind='operand', line=821)
W('33,2604', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=822)
W('33,2605', 0o03720, '', '', 'UHYP', kind='operand', line=823)
W('33,2606', 0o27726, '', 'STOVL', 'UHZP', 'DOWNRANGE HALF-UNIT VECTOR FOR R10.', kind='interp', line=824)
W('33,2607', 0o03573, '', '', 'R1S', kind='operand', line=825)
W('33,2610', 0o60505, '', 'VXM', 'VSR4', kind='interp', line=826)
W('33,2611', 0o01734, '', '', 'REFSMMAT', kind='operand', line=827)
W('33,2612', 0o27545, '', 'STOVL', 'RN1', 'TEMP. REF. POSITION VECTOR*2(29)M.', kind='interp', line=828)
W('33,2613', 0o03601, '', '', 'V1S', kind='operand', line=829)
W('33,2614', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=830)
W('33,2615', 0o01734, '', '', 'REFSMMAT', kind='operand', line=831)
W('33,2616', 0o27553, '', 'STOVL', 'VN1', 'TEMP. REF. VELOCITY VECTOR 2(7) M/CS.', kind='interp', line=832)
W('33,2617', 0o03537, '', '', 'UNIT/R/', kind='operand', line=833)
W('33,2620', 0o51435, '', 'VXV', 'ABVAL', kind='interp', line=834)
# Page 877
W('33,2621', 0o03601, '', '', 'V1S', kind='operand', line=836)
W('33,2622', 0o63552, '', 'SL1', 'DSQ', kind='interp', line=837)
W('33,2623', 0o77671, '', 'DDV', kind='interp', line=838)
W('33,2624', 0o47075, '', 'DMPR', 'RTB', kind='interp', line=839)
W('33,2625', 0o26030, '', '', 'ARCONV1', kind='operand', line=840)
W('33,2626', 0o21612, '', '', 'SGNAGREE', kind='operand', line=841)
W('33,2627', 0o77776, 'COPYCYC2', 'EXIT', '', 'LEAVE ALTITUDE RATE COMPENSATION IN MPAC', kind='interp', line=842)
W('33,2630', 0o00004, '', 'INHINT', line=843)
W('33,2631', 0o31536, '', 'CA', 'UNIT/R/', 'UPDATE RUNIT FOR R10.', line=844)
W('33,2632', 0o55743, '', 'TS', 'RUNIT', line=845)
W('33,2633', 0o31540, '', 'CA', 'UNIT/R/ +2', line=846)
W('33,2634', 0o55744, '', 'TS', 'RUNIT +1', line=847)
W('33,2635', 0o31542, '', 'CA', 'UNIT/R/ +4', line=848)
W('33,2636', 0o55745, '', 'TS', 'RUNIT +2', line=849)
W('33,2637', 0o30154, '', 'CA', 'MPAC', 'LOAD NEW DALTRATE FOR R10.', line=850)
W('33,2640', 0o55716, '', 'TS', 'DALTRATE', line=851)

W('33,2641', 0o00006, '', 'EXTEND', line=853)
W('33,2642', 0o31573, '', 'DCA', 'R1S', line=854)
W('33,2643', 0o53521, '', 'DXCH', 'R', line=855)
W('33,2644', 0o00006, '', 'EXTEND', line=856)
W('33,2645', 0o31575, '', 'DCA', 'R1S +2', line=857)
W('33,2646', 0o53523, '', 'DXCH', 'R +2', line=858)
W('33,2647', 0o00006, '', 'EXTEND', line=859)
W('33,2650', 0o31577, '', 'DCA', 'R1S +4', line=860)
W('33,2651', 0o53525, '', 'DXCH', 'R +4', line=861)
W('33,2652', 0o00006, '', 'EXTEND', line=862)
W('33,2653', 0o31601, '', 'DCA', 'V1S', line=863)
W('33,2654', 0o53527, '', 'DXCH', 'V', line=864)
W('33,2655', 0o00006, '', 'EXTEND', line=865)
W('33,2656', 0o31603, '', 'DCA', 'V1S +2', line=866)
W('33,2657', 0o53531, '', 'DXCH', 'V +2', line=867)
W('33,2660', 0o00006, '', 'EXTEND', line=868)
W('33,2661', 0o31605, '', 'DCA', 'V1S +4', line=869)
W('33,2662', 0o53533, '', 'DXCH', 'V +4', line=870)

W('33,2663', 0o12275, '', 'TCF', 'COPYCYCL', 'COMPLETE THE COPYCYCL.', line=872)

# Page 878
# ALTCHK COMPARES CURRENT ALTITUDE (IN HCALC) WITH A SPECIFIED ALTITUDE FROM A TABLE BEGINNING AT ALTCRIT.
# ITS CALLING SEQUENCE IS AS FOLLOWS:-
#
# L       CAF     N
# L+1     TC      BANKCALL
# L+2     CADR    ALTCHK
# L+3     RETURN HERE IF HCALC STILL > SPECIFIED CRITERION.   C(L) = +0.
# L+4     RETURN HERE IF HCALC < OR = SPECIFIED CRITERION.   C(A) = C(L) = +0
#
# ALTCHK MUST BE BANKCALLED EVEN FROM ITS OWN BANK.   N IS THE LOCATION, RELATIVE TO THE TAG ALTCRIT,
# OF THE BEGINNING OF THE DP CONSTANT TO BE USED AS A CRITERION.

W('33,2664', 0o00006, 'ALTCHK', 'EXTEND', line=887)
W('33,2665', 0o50000, '', 'INDEX', 'A', line=888)
W('33,2666', 0o32700, '', 'DCA', 'ALTCRIT', line=889)
W('33,2667', 0o52156, '', 'DXCH', 'MPAC +1', line=890)
W('33,2670', 0o00006, '', 'EXTEND', line=891)
W('33,2671', 0o41535, '', 'DCS', 'HCALC', line=892)
W('33,2672', 0o20156, '', 'DAS', 'MPAC +1', line=893)
W('33,2673', 0o06727, '', 'TC', 'BRANCH +4', line=894)
W('33,2674', 0o34755, '', 'CAF', 'ZERO', 'BETTER THAN A NOOP, PERHAPS', line=895)
W('33,2675', 0o24133, '', 'INCR', 'BUF2', line=896)
W('33,2676', 0o14631, '', 'TCF', 'SWRETURN', line=897)

S('ALTCRIT', 'equals', 0o76677, line=899)

W('33,2677', 0o00007, '25KFT', '2DEC', '7620 B-24', '(0)', kind='data', line=901)
W('33,2700', 0o16100, kind='data', line=901)

W('33,2701', 0o00016, '50KFT', '2DEC', '15240 B-24', '(2)', kind='data', line=903)
W('33,2702', 0o34200, kind='data', line=903)

W('33,2703', 0o00000, '50FT', '2DEC', '15.24 B-24', '(4)', kind='data', line=905)
W('33,2704', 0o00364, kind='data', line=905)

W('33,2705', 0o00010, '30KFT', '2DEC', '9144 B-24', '(6)', kind='data', line=907)
W('33,2706', 0o35600, kind='data', line=907)

W('33,2707', 0o01414, '2KFT/SEC', 'DEC', '6.096 B-7', '2000 FT/SEC AT 2(7) M/CS', kind='data', line=909)

# (A remark was likely to be needed here to explain XORCHK) 4/Jun/09,FB

W('33,2710', 0o36242, 'XORCHK', 'CAF', 'SIX', 'ARE WE BELOW 30000 FT?', line=914)
W('33,2711', 0o04616, '', 'TC', 'BANKCALL', line=915)
W('33,2712', 0o66664, '', 'CADR', 'ALTCHK', kind='data', line=916)
W('33,2713', 0o12476, '', 'TCF', 'HITEST', 'CONTINUE LR UPDATE', line=917)
W('33,2714', 0o05504, '', 'TC', 'UPFLAG', 'YES: INHIBIT X-AXIS OVERRIDE', line=918)
W('33,2715', 0o00311, '', 'ADRES', 'XOVINFLG', kind='data', line=919)
W('33,2716', 0o05504, '', 'TC', 'UPFLAG', line=920)
W('33,2717', 0o00253, '', 'ADRES', 'XORFLG', kind='data', line=921)
W('33,2720', 0o12476, '', 'TCF', 'HITEST', 'CONTINUE LR UPDATE', line=922)

W('33,2721', 0o34752, '35KCHK', 'CAF', 'TWO', 'ARE WE BELOW 35000 FT?', line=924)

# Page 879
W('33,2722', 0o04616, '', 'TC', 'BANKCALL', line=927)
W('33,2723', 0o66664, '', 'CADR', 'ALTCHK', kind='data', line=928)
W('33,2724', 0o12540, '', 'TCF', 'CONTSERV', line=929)
W('33,2725', 0o05504, '', 'TC', 'UPFLAG', line=930)
W('33,2726', 0o00256, '', 'ADRES', 'READLR', 'SET READLR FLAG TO ENABLE LR READING.', kind='data', line=931)
W('33,2727', 0o12540, '', 'TCF', 'CONTSERV', line=932)

# Page 880
# ***************************************************************

W('33,2730', 0o41456, 'CALCGRAV', 'UNIT', 'PUSH', 'SAVE UNIT/R/ IN PUSHLIST      (18)', kind='interp', line=937)
W('33,2731', 0o03537, '', 'STORE', 'UNIT/R/', kind='interp', line=938)
W('33,2732', 0o67340, '', 'LXC,1', 'SLOAD', 'RTX2 = 0 IF EARTH ORBIT, =2 IF LUNAR.', kind='interp', line=939)
W('33,2733', 0o02777, '', '', 'RTX2', kind='operand', line=940)
W('33,2734', 0o03000, '', '', 'RTX2', kind='operand', line=941)
W('33,2735', 0o50076, '', 'DCOMP', 'BMN', kind='interp', line=942)
W('33,2736', 0o66765, '', '', 'CALCGRV1', kind='operand', line=943)
W('33,2737', 0o50375, '', 'VLOAD', 'DOT', '                              (12)', kind='interp', line=944)
W('33,2740', 0o06514, '', '', 'UNITZ', kind='operand', line=945)
W('33,2741', 0o03537, '', '', 'UNIT/R/', kind='operand', line=946)
W('33,2742', 0o41552, '', 'SL1', 'PUSH', '                              (14)', kind='interp', line=947)
W('33,2743', 0o44316, '', 'DSQ', 'BDSU', kind='interp', line=948)
W('33,2744', 0o27027, '', '', 'DP1/20', kind='operand', line=949)
W('33,2745', 0o56325, '', 'PDDL', 'DDV', kind='interp', line=950)
W('33,2746', 0o26040, '', '', 'RESQ', kind='operand', line=951)
W('33,2747', 0o00043, '', '', '34D', '(RN)SQ', kind='operand', line=952)
W('33,2750', 0o00041, '', 'STORE', '32D', 'TEMP FOR (RE/RN)SQ', kind='interp', line=953)
W('33,2751', 0o41205, '', 'DMP', 'DMP', kind='interp', line=954)
W('33,2752', 0o26042, '', '', '20J', kind='operand', line=955)
W('33,2753', 0o65361, '', 'VXSC', 'PDDL', kind='interp', line=956)
W('33,2754', 0o03537, '', '', 'UNIT/R/', kind='operand', line=957)
W('33,2755', 0o41205, '', 'DMP', 'DMP', kind='interp', line=958)
W('33,2756', 0o26044, '', '', '2J', kind='operand', line=959)
W('33,2757', 0o00041, '', '', '32D', kind='operand', line=960)
W('33,2760', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=961)
W('33,2761', 0o06514, '', '', 'UNITZ', kind='operand', line=962)
W('33,2762', 0o45455, '', 'VAD', 'STADR', kind='interp', line=963)
W('33,2763', 0o74256, '', 'STORE', 'UNITGOBL', kind='interp', line=964)
W('33,2764', 0o41455, '', 'VAD', 'PUSH', 'MPAC = UNIT GRAVITY VECTOR.   (18)', kind='interp', line=965)
W('33,2765', 0o60345, 'CALCGRV1', 'DLOAD', 'NORM', 'PERFORM A NORMALIZATION ON RMAGSQ IN', kind='interp', line=966)
W('33,2766', 0o00043, '', '', '34D', 'ORDER TO BE ABLE TO SCALE THE MU FOR', kind='operand', line=967)
W('33,2767', 0o00050, '', '', 'X2', 'MAXIMUM PRECISION.', kind='operand', line=968)
W('33,2770', 0o53663, '', 'BDDV*', 'SLR*', kind='interp', line=969)
W('33,2771', 0o26032, '', '', '-MUDT,1', kind='operand', line=970)
W('33,2772', 0o56623, '', '', '0 -21D,2', kind='operand', line=971)
W('33,2773', 0o45561, '', 'VXSC', 'STADR', kind='interp', line=972)
W('33,2774', 0o74214, '', 'STORE', 'GDT1/2', 'SCALED AT 2(+7) M/CS', kind='interp', line=973)
W('33,2775', 0o77616, '', 'RVQ', kind='interp', line=974)

W('33,2776', 0o61375, 'CALCRVG', 'VLOAD', 'VXM', kind='interp', line=976)
W('33,2777', 0o00325, '', '', 'DELV', kind='operand', line=977)
W('33,3000', 0o01734, '', '', 'REFSMMAT', kind='operand', line=978)
W('33,3001', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=979)
W('33,3002', 0o26022, '', '', 'KPIP1', kind='operand', line=980)
W('33,3003', 0o03527, '', 'STORE', 'DELVREF', kind='interp', line=981)
W('33,3004', 0o41562, '', 'VSR1', 'PUSH', kind='interp', line=982)
W('33,3005', 0o41455, '', 'VAD', 'PUSH', '(DV-OLDGDT)/2 TO PD SCALED AT 2(+7) M/CS.', kind='interp', line=983)
# Page 881
W('33,3006', 0o01237, '', '', 'GDT/2', kind='operand', line=985)
W('33,3007', 0o65255, '', 'VAD', 'PDDL', kind='interp', line=986)
W('33,3010', 0o01227, '', '', 'VN', kind='operand', line=987)
W('33,3011', 0o01250, '', '', 'PGUIDE', kind='operand', line=988)
W('33,3012', 0o74261, '', 'SL', 'VXSC', kind='interp', line=989)
W('33,3013', 0o20207, '', '', '6D', kind='operand', line=990)
W('33,3014', 0o44055, '', 'VAD', 'STQ', kind='interp', line=991)
W('33,3015', 0o01221, '', '', 'RN', kind='operand', line=992)
W('33,3016', 0o00037, '', '', '31D', kind='operand', line=993)
W('33,3017', 0o37545, '', 'STCALL', 'RN1', 'TEMP STORAGE OF RN SCALED 2(+29) M', kind='interp', line=994)
W('33,3020', 0o66730, '', '', 'CALCGRAV', kind='operand', line=995)

W('33,3021', 0o53255, '', 'VAD', 'VAD', kind='interp', line=997)
W('33,3022', 0o77655, '', 'VAD', kind='interp', line=998)
W('33,3023', 0o01227, '', '', 'VN', kind='operand', line=999)
W('33,3024', 0o37553, '', 'STCALL', 'VN1', 'TEMP STORAGE OF VN SCALED 2(+7) M/CS', kind='interp', line=1000)
W('33,3025', 0o00037, '', '', '31D', kind='operand', line=1001)

W('33,3026', 0o01463, 'DP1/20', '2DEC', '0.05', kind='data', line=1003)
W('33,3027', 0o06315, kind='data', line=1003)
W('33,3030', 0o00010, 'SHIFT11', '2DEC', '1 B-11', kind='data', line=1004)
W('33,3031', 0o00000, kind='data', line=1004)

# Page 882
# *****************************************************************************
# MUNRVG IS A SPECIAL AVERAGE G INTEGRATION ROUTINE USED BY THRUSTING
# PROGRAMS WHICH FUNCTION IN THE VICINITY OF AN ASSUMED SPHERICAL MOON.
# THE INPUT AND OUTPUT QUANTITIES ARE REFERENCED TO THE STABLE MEMBER
# COORDINATE SYSTEM.

W('33,3032', 0o41575, 'RVBOTH', 'VLOAD', 'PUSH', kind='interp', line=1013)
W('33,3033', 0o02317, '', '', 'G(CSM)', kind='operand', line=1014)
W('33,3034', 0o65255, '', 'VAD', 'PDDL', kind='interp', line=1015)
W('33,3035', 0o01726, '', '', 'V(CSM)', kind='operand', line=1016)
W('33,3036', 0o01250, '', '', 'PGUIDE', kind='operand', line=1017)
W('33,3037', 0o74271, '', 'DDV', 'VXSC', kind='interp', line=1018)
W('33,3040', 0o27031, '', '', 'SHIFT11', kind='operand', line=1019)
W('33,3041', 0o77655, '', 'VAD', kind='interp', line=1020)
W('33,3042', 0o01720, '', '', 'R(CSM)', kind='operand', line=1021)
W('33,3043', 0o37573, '', 'STCALL', 'R1S', kind='interp', line=1022)
W('33,3044', 0o67130, '', '', 'MUNGRAV', kind='operand', line=1023)
W('33,3045', 0o53255, '', 'VAD', 'VAD', kind='interp', line=1024)
W('33,3046', 0o01726, '', '', 'V(CSM)', kind='operand', line=1025)
W('33,3047', 0o77626, '', 'STADR', kind='interp', line=1026)
W('33,3050', 0o74176, '', 'STORE', 'V1S', kind='interp', line=1027)
W('33,3051', 0o77776, '', 'EXIT', kind='interp', line=1028)
W('33,3052', 0o03552, '', 'TC', 'QUIKFAZ5', line=1029)
W('33,3053', 0o06037, '', 'TC', 'INTPRET', line=1030)
W('33,3054', 0o77775, '', 'VLOAD', kind='interp', line=1031)
W('33,3055', 0o03563, '', '', 'GDT1/2', kind='operand', line=1032)
W('33,3056', 0o26317, '', 'STOVL', 'G(CSM)', kind='interp', line=1033)
W('33,3057', 0o03573, '', '', 'R1S', kind='operand', line=1034)
W('33,3060', 0o25720, '', 'STOVL', 'R(CSM)', kind='interp', line=1035)
W('33,3061', 0o03601, '', '', 'V1S', kind='operand', line=1036)
W('33,3062', 0o01726, '', 'STORE', 'V(CSM)', kind='interp', line=1037)
W('33,3063', 0o77776, '', 'EXIT', kind='interp', line=1038)
W('33,3064', 0o03552, '', 'TC', 'QUIKFAZ5', line=1039)
W('33,3065', 0o06037, '', 'TC', 'INTPRET', line=1040)
W('33,3066', 0o74375, 'MUNRVG', 'VLOAD', 'VXSC', kind='interp', line=1041)
W('33,3067', 0o00325, '', '', 'DELV', kind='operand', line=1042)
W('33,3070', 0o26024, '', '', 'KPIP2', kind='operand', line=1043)
W('33,3071', 0o53206, '', 'PUSH', 'VAD', '1ST PUSH:  DELV IN UNITS OF 2(8) M/CS', kind='interp', line=1044)
W('33,3072', 0o01237, '', '', 'GDT/2', kind='operand', line=1045)
W('33,3073', 0o53206, '', 'PUSH', 'VAD', '2ND PUSH:  (DELV + GDT)/2, UNITS OF 2(7)', kind='interp', line=1046)
W('33,3074', 0o03527, '', '', 'V', '                              (12)', kind='operand', line=1047)
W('33,3075', 0o56325, '', 'PDDL', 'DDV', kind='interp', line=1048)
W('33,3076', 0o01250, '', '', 'PGUIDE', kind='operand', line=1049)
W('33,3077', 0o27031, '', '', 'SHIFT11', kind='operand', line=1050)
W('33,3100', 0o77761, '', 'VXSC', kind='interp', line=1051)
W('33,3101', 0o77655, '', 'VAD', kind='interp', line=1052)
W('33,3102', 0o03521, '', '', 'R', kind='operand', line=1053)
W('33,3103', 0o37573, '', 'STCALL', 'R1S', 'STORE R SCALED AT 2(+24) M', kind='interp', line=1054)
W('33,3104', 0o67130, '', '', 'MUNGRAV', kind='operand', line=1055)
# Page 883
W('33,3105', 0o53255, '', 'VAD', 'VAD', kind='interp', line=1057)
W('33,3106', 0o77655, '', 'VAD', kind='interp', line=1058)
W('33,3107', 0o03527, '', '', 'V', kind='operand', line=1059)
W('33,3110', 0o03601, '', 'STORE', 'V1S', 'STORE V SCALED AT 2(+7) M/CS.', kind='interp', line=1060)
W('33,3111', 0o77646, '', 'ABVAL', kind='interp', line=1061)
W('33,3112', 0o27472, '', 'STOVL', 'ABVEL', 'STORE SPEED FOR LR AND DISPLAYS.', kind='interp', line=1062)
W('33,3113', 0o03537, '', '', 'UNIT/R/', kind='operand', line=1063)
W('33,3114', 0o72441, '', 'DOT', 'SL1', kind='interp', line=1064)
W('33,3115', 0o03601, '', '', 'V1S', kind='operand', line=1065)
W('33,3116', 0o27474, '', 'STOVL', 'HDOTDISP', 'HDOT = V. UNIT(R)*2(7) M/CS.', kind='interp', line=1066)
W('33,3117', 0o03573, '', '', 'R1S', kind='operand', line=1067)
W('33,3120', 0o72435, '', 'VXV', 'VSL2', kind='interp', line=1068)
W('33,3121', 0o02325, '', '', 'WM', kind='operand', line=1069)
W('33,3122', 0o17734, '', 'STODL', 'DELVS', 'LUNAR ROTATION CORRECTION TERM*2(5) M/CS.', kind='interp', line=1070)
W('33,3123', 0o00045, '', '', '36D', kind='operand', line=1071)
W('33,3124', 0o77625, '', 'DSU', kind='interp', line=1072)
W('33,3125', 0o02333, '', '', '/LAND/', kind='operand', line=1073)
W('33,3126', 0o37535, '', 'STCALL', 'HCALC', 'FOR NOW, DISPLAY WHETHER POS OR NEG', kind='interp', line=1074)
W('33,3127', 0o66461, '', '', 'MUNRETRN', kind='operand', line=1075)
W('33,3130', 0o77656, 'MUNGRAV', 'UNIT', '', 'AT 36D HAVE ABVAL(R), AT 34D R.R', kind='interp', line=1076)
W('33,3131', 0o17537, '', 'STODL', 'UNIT/R/', kind='interp', line=1077)
W('33,3132', 0o00043, '', '', '34D', kind='operand', line=1078)
W('33,3133', 0o55261, '', 'SL', 'BDDV', kind='interp', line=1079)
W('33,3134', 0o20207, '', '', '6D', kind='operand', line=1080)
W('33,3135', 0o26036, '', '', '-MUDTMUN', kind='operand', line=1081)
W('33,3136', 0o74205, '', 'DMP', 'VXSC', kind='interp', line=1082)
W('33,3137', 0o27031, '', '', 'SHIFT11', kind='operand', line=1083)
W('33,3140', 0o03537, '', '', 'UNIT/R/', kind='operand', line=1084)
W('33,3141', 0o03563, '', 'STORE', 'GDT1/2', '1/2GDT SCALED AT 2(7) M/CS.', kind='interp', line=1085)
W('33,3142', 0o77616, '', 'RVQ', kind='interp', line=1086)

W('33,3143', 0o00303, '1.95SECS', 'DEC', '195', kind='data', line=1088)
W('33,3144', 0o00005, '7.5', '2DEC', '.02286 B-6', '7.5 FT/SEC AT 2(6) M/CS', kind='data', line=1089)
W('33,3145', 0o33212, kind='data', line=1089)

W('33,3146', 0o00014, '2SEC(18)', '2DEC', '200 B-18', kind='data', line=1091)
W('33,3147', 0o20000, kind='data', line=1091)

W('33,3150', 0o00000, '2SEC(28)', '2OCT', '0000000310', '2SEC AT 2(28)', kind='data', line=1093)
W('33,3151', 0o00310, kind='data', line=1093)

W('33,3152', 0o00000, '4SEC(28)', '2DEC', '400 B-28', kind='data', line=1095)
W('33,3153', 0o00620, kind='data', line=1095)

W('33,3154', 0o00110, 'BITS4-7', 'OCT', '110', kind='data', line=1097)

# Page 884
W('33,3155', 0o34742, 'UPDATCHK', 'CAF', 'NOLRRBIT', 'SEE IF LR UPDATE INHIBITED.', line=1101)
W('33,3156', 0o70107, '', 'MASK', 'FLGWRD11', line=1102)
W('33,3157', 0o10000, '', 'CCS', 'A', line=1103)
W('33,3160', 0o12540, '', 'TCF', 'CONTSERV', 'IT IS -- NO LR UPDATE', line=1104)
W('33,3161', 0o34750, '', 'CAF', 'RNGEDBIT', 'NO INHIBIT -- SEE ALT MEAS. THIS CYCLE.', line=1105)
W('33,3162', 0o70107, '', 'MASK', 'FLGWRD11', line=1106)
W('33,3163', 0o00006, '', 'EXTEND', line=1107)
W('33,3164', 0o13310, '', 'BZF', 'VMEASCHK', 'NO ALT MEAS THIS CYCLE -- CHECK FOR VEL', line=1108)

W('33,3165', 0o30120, 'POSUPDAT', 'CA', 'FIXLOC', 'SET PUSHLIST TO ZERO', line=1110)
W('33,3166', 0o54166, '', 'TS', 'PUSHLOC', line=1111)

W('33,3167', 0o06037, '', 'TC', 'INTPRET', line=1113)
W('33,3170', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=1114)
W('33,3171', 0o02273, '', '', 'HBEAMNB', kind='operand', line=1115)
W('33,3172', 0o02146, '', '', 'XNBPIP', 'HBEAM SM AT 2(2)', kind='operand', line=1116)
W('33,3173', 0o72515, '', 'PDVL', 'VSL2', 'STORE HBEAM IN PD 0-5', kind='interp', line=1117)
W('33,3174', 0o03601, '', '', 'V1S', 'SCALE V AT 2(5) M/CS', kind='operand', line=1118)
W('33,3175', 0o50255, '', 'VAD', 'DOT', kind='interp', line=1119)
W('33,3176', 0o03734, '', '', 'DELVS', 'V RELATIVE TO SURFACE AT 2(5) M/CS', kind='operand', line=1120)
W('33,3177', 0o00001, '', '', '0D', 'V ALONG HBEAM AT 2(7) M/CS.', kind='operand', line=1121)
W('33,3200', 0o77405, '', 'DMP', 'EXIT', kind='interp', line=1122)
W('33,3201', 0o01355, '', '', 'RADSKAL', 'SCALE TO RADAR COUNTS X 5', kind='operand', line=1123)

W('33,3202', 0o40110, '', 'CS', 'FLGWRD12', 'TEST LR ALTITUDE SCALE FACTOR', line=1125)
W('33,3203', 0o74743, '', 'MASK', 'ALTSCBIT', line=1126)
W('33,3204', 0o00006, '', 'EXTEND', line=1127)
W('33,3205', 0o13210, '', 'BZF', '+3', 'BRANCH IF HIGH SCALE', line=1128)

W('33,3206', 0o31356, '', 'CA', 'SKALSKAL', 'RESCALE IF LOW SCALE', line=1130)
W('33,3207', 0o07307, '', 'TC', 'SHORTMP', line=1131)

W('33,3210', 0o06037, '', 'TC', 'INTPRET', line=1133)
W('33,3211', 0o54215, '', 'DAD', 'SL', 'CORRECT HMEAS FOR DOPPLER EFFECT', kind='interp', line=1134)
W('33,3212', 0o03655, '', '', 'HMEAS', kind='operand', line=1135)
W('33,3213', 0o20210, '', '', '7D', kind='operand', line=1136)
W('33,3214', 0o74205, '', 'DMP', 'VXSC', 'SLANT RANGE AT 2(21), PUSH UP FOR HBEAM', kind='interp', line=1137)
W('33,3215', 0o26011, '', '', 'HSCAL', 'SLANT RANGE VECTOR AT 2(23) M', kind='operand', line=1138)
W('33,3216', 0o45241, '', 'DOT', 'DSU', kind='interp', line=1139)
W('33,3217', 0o03537, '', '', 'UNIT/R/', 'ALTITUDE AT 2(24) M', kind='operand', line=1140)
W('33,3220', 0o03535, '', '', 'HCALC', 'DELTA H AT 2(24) M', kind='operand', line=1141)
W('33,3221', 0o03665, '', 'STORE', 'DELTAH', kind='interp', line=1142)
W('33,3222', 0o77776, '', 'EXIT', kind='interp', line=1143)

W('33,3223', 0o30107, '', 'CA', 'FLGWRD11', line=1145)
W('33,3224', 0o74741, '', 'MASK', 'PSTHIBIT', line=1146)
W('33,3225', 0o00006, '', 'EXTEND', '', 'DO NOT PERFORM DATA REASONABLENESS TEST', line=1147)
W('33,3226', 0o13243, '', 'BZF', 'NOREASON', 'UNTIL AFTER HIGATE', line=1148)
# Page 885
W('33,3227', 0o06037, '', 'TC', 'INTPRET', line=1150)
W('33,3230', 0o45246, '', 'ABS', 'DSU', kind='interp', line=1151)
W('33,3231', 0o02521, '', '', 'DELQFIX', 'ABS(DELTAH) - DQFIX   50 FT NOM', kind='operand', line=1152)
W('33,3232', 0o45252, '', 'SL3', 'DSU', 'SCALE TO 2(21)', kind='interp', line=1153)
W('33,3233', 0o03535, '', '', 'HCALC', 'ABS(DELTAH) - (50 + HCALC/8) AT 2(21)', kind='operand', line=1154)
W('33,3234', 0o77776, '', 'EXIT', kind='interp', line=1155)

W('33,3235', 0o25670, '', 'INCR', 'LRLCTR', line=1157)
W('33,3236', 0o06723, '', 'TC', 'BRANCH', line=1158)
W('33,3237', 0o13560, '', 'TCF', 'HFAIL', 'DELTA H TOO LARGE', line=1159)
W('33,3240', 0o13560, '', 'TCF', 'HFAIL', 'DELTA H TOO LARGE', line=1160)
W('33,3241', 0o05516, '', 'TC', 'DOWNFLAG', 'TURN OFF ALT FAIL LAMP', line=1161)
W('33,3242', 0o00263, '', 'ADRES', 'HFLSHFLG', kind='data', line=1162)

W('33,3243', 0o40107, 'NOREASON', 'CS', 'FLGWRD11', line=1164)
W('33,3244', 0o74744, '', 'MASK', 'LRINHBIT', line=1165)
W('33,3245', 0o10000, '', 'CCS', 'A', line=1166)
W('33,3246', 0o13310, '', 'TCF', 'VMEASCHK', 'UPDATE INHIBITED -- TEST VELOCITY ANYWAY', line=1167)

W('33,3247', 0o06037, '', 'TC', 'INTPRET', 'DO POSITION UPDATE', line=1169)
W('33,3250', 0o40545, '', 'DLOAD', 'SR4', kind='interp', line=1170)
W('33,3251', 0o03535, '', '', 'HCALC', 'RESCALE H TO 2(28)M', kind='operand', line=1171)
W('33,3252', 0o77776, '', 'EXIT', kind='interp', line=1172)
W('33,3253', 0o00006, '', 'EXTEND', line=1173)
W('33,3254', 0o31665, '', 'DCA', 'DELTAH', 'STORE DELTAH IN MPAC AND', line=1174)
W('33,3255', 0o52155, '', 'DXCH', 'MPAC', 'BRING HCALC INTO A,L', line=1175)
W('33,3256', 0o07544, '', 'TC', 'ALSIGNAG', line=1176)
W('33,3257', 0o00006, '', 'EXTEND', '', 'IF HIGH PART OF HCALC IS NON-ZERO, THEN', line=1177)
W('33,3260', 0o13262, '', 'BZF', '+2', 'HCALC > HMAX,', line=1178)
W('33,3261', 0o13310, '', 'TCF', 'VMEASCHK', 'SO UPDATE IS BYPASSED', line=1179)
W('33,3262', 0o54156, '', 'TS', 'MPAC +2', '      FOR LATER SHORTMP', line=1180)

W('33,3263', 0o40001, '', 'CS', 'L', '-H AT 2(14) M', line=1182)
W('33,3264', 0o61420, '', 'AD', 'LRHMAX', 'HMAX - H', line=1183)
W('33,3265', 0o00006, '', 'EXTEND', line=1184)
W('33,3266', 0o63310, '', 'BZMF', 'VMEASCHK', 'IF H >HMAX, BYPASS UPDATE', line=1185)
W('33,3267', 0o00006, '', 'EXTEND', line=1186)
W('33,3270', 0o71421, '', 'MP', 'LRWH', 'WH(HMAX - H)', line=1187)
W('33,3271', 0o00006, '', 'EXTEND', line=1188)
W('33,3272', 0o11420, '', 'DV', 'LRHMAX', 'WH(1 - H/HMAX)', line=1189)
W('33,3273', 0o54135, '', 'TS', 'MPTEMP', line=1190)
W('33,3274', 0o07313, '', 'TC', 'SHORTMP2', 'DELTAH (WH)(1 - H/HMAX) IN MPAC', line=1191)
W('33,3275', 0o06037, '', 'TC', 'INTPRET', 'MODE IS DP FROM ABOVE', line=1192)
W('33,3276', 0o77752, '', 'SL1', kind='interp', line=1193)
W('33,3277', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=1194)
W('33,3300', 0o03537, '', '', 'UNIT/R/', 'DELTAR = DH(WH)(1 - H/HMAX) UNIT/R/', kind='operand', line=1195)
W('33,3301', 0o03573, '', '', 'R1S', kind='operand', line=1196)
W('33,3302', 0o37657, '', 'STCALL', 'GNUR', kind='interp', line=1197)
W('33,3303', 0o67130, '', '', 'MUNGRAV', kind='operand', line=1198)
W('33,3304', 0o77776, '', 'EXIT', kind='interp', line=1199)
# Page 886
W('33,3305', 0o03552, '', 'TC', 'QUIKFAZ5', line=1201)

W('33,3306', 0o34755, '', 'CA', 'ZERO', line=1203)
W('33,3307', 0o03534, 'RUPDATED', 'TC', 'GNURVST', line=1204)

W('33,3310', 0o03552, 'VMEASCHK', 'TC', 'QUIKFAZ5', 'RESTART AT NEXT LOCATION', line=1206)
W('33,3311', 0o40107, '', 'CS', 'FLGWRD11', line=1207)
W('33,3312', 0o74745, '', 'MASK', 'VELDABIT', 'IS V READING AVAILABLE?', line=1208)
W('33,3313', 0o10000, '', 'CCS', 'A', line=1209)
W('33,3314', 0o13514, '', 'TCF', 'VALTCHK', 'NO:  SEE IF V READING TO BE TAKEN', line=1210)

W('33,3315', 0o41651, 'VELUPDAT', 'CS', 'VSELECT', 'PROCESS VELOCITY DATA', line=1212)
W('33,3316', 0o54001, '', 'TS', 'L', line=1213)
W('33,3317', 0o26001, '', 'ADS', 'L', '-2 VSELECT IN L', line=1214)
W('33,3320', 0o60001, '', 'AD', 'L', line=1215)
W('33,3321', 0o60001, '', 'AD', 'L', '-6 VSELECT IN A', line=1216)
W('33,3322', 0o50120, '', 'INDEX', 'FIXLOC', line=1217)
W('33,3323', 0o52047, '', 'DXCH', 'X1', 'X1 = -6 VSELECT, X2 = -2 VSELECT', line=1218)

W('33,3324', 0o34741, '', 'CA', 'EBANK4', line=1220)
W('33,3325', 0o54003, '', 'TS', 'EBANK', line=1221)
#   EBANK= LRXCDU

W('33,3326', 0o31655, '', 'CA', 'LRYCDU', 'STORE LRCDUS IN CDUSPOTS', line=1224)
W('33,3327', 0o54766, '', 'TS', 'CDUSPOT', line=1225)
W('33,3330', 0o31656, '', 'CA', 'LRZCDU', line=1226)
W('33,3331', 0o54770, '', 'TS', 'CDUSPOT +2', line=1227)
W('33,3332', 0o31654, '', 'CA', 'LRXCDU', line=1228)
W('33,3333', 0o54772, '', 'TS', 'CDUSPOT +4', line=1229)

W('33,3334', 0o04616, '', 'TC', 'BANKCALL', line=1231)
W('33,3335', 0o47615, '', 'CADR', 'QUICTRIG', 'GET SINES AND COSINES FOR NBSM', kind='data', line=1232)

W('33,3336', 0o30120, '', 'CA', 'FIXLOC', line=1234)
W('33,3337', 0o54166, '', 'TS', 'PUSHLOC', 'SET PD TO ZERO', line=1235)

W('33,3340', 0o06037, '', 'TC', 'INTPRET', line=1237)
W('33,3341', 0o45173, '', 'VLOAD*', 'CALL', kind='interp', line=1238)
W('33,3342', 0o02231, '', '', 'VZBEAMNB,1', 'CONVERT VBEAM FROM NB TO SM', kind='operand', line=1239)
W('33,3343', 0o47673, '', '', '*NBSM*', kind='operand', line=1240)
W('33,3344', 0o54325, '', 'PDDL', 'SL', 'STORE IN PD 0-5', kind='interp', line=1241)
W('33,3345', 0o03653, '', '', 'VMEAS', 'LOAD VELOCITY MEASUREMENT', kind='operand', line=1242)
W('33,3346', 0o20215, '', '', '12D', kind='operand', line=1243)
W('33,3347', 0o41403, '', 'DMP*', 'PUSH', 'SCALE TO M/CS AT 2(6)', kind='interp', line=1244)
W('33,3350', 0o51764, '', '', 'VZSCAL,2', 'AND STORE IN PD 6-7', kind='operand', line=1245)
W('33,3351', 0o77776, '', 'EXIT', kind='interp', line=1246)
W('33,3352', 0o44753, '', 'CS', 'ONE', line=1247)
W('33,3353', 0o54163, '', 'TS', 'MODE', 'CHANGE STORE MODE TO VECTOR', line=1248)

W('33,3354', 0o31657, '', 'CA', 'PIPTEM', 'STORE DELV IN MPAC', line=1250)
# Page 887
W('33,3355', 0o22007, '', 'ZL', line=1252)
W('33,3356', 0o52155, '', 'DXCH', 'MPAC', line=1253)

W('33,3357', 0o31660, '', 'CA', 'PIPTEM +1', line=1255)
W('33,3360', 0o22007, '', 'ZL', line=1256)
W('33,3361', 0o52160, '', 'DXCH', 'MPAC +3', line=1257)

W('33,3362', 0o31661, '', 'CA', 'PIPTEM +2', line=1259)
W('33,3363', 0o22007, '', 'ZL', line=1260)
W('33,3364', 0o52162, '', 'DXCH', 'MPAC +5', line=1261)

W('33,3365', 0o35016, '', 'CA', 'EBANK7', line=1263)
W('33,3366', 0o54003, '', 'TS', 'EBANK', 'RESTORE EBANK 7', line=1264)
#   EBANK= DVCNTR
W('33,3367', 0o06037, '', 'TC', 'INTPRET', line=1266)
W('33,3370', 0o65361, '', 'VXSC', 'PDDL', kind='interp', line=1267)
W('33,3371', 0o26022, '', '', 'KPIP1', 'SCALE DELV TO 2(7) M/CS AND PUSH', kind='operand', line=1268)
W('33,3372', 0o02253, '', '', 'LRVTIME', 'TIME OF DELV AT 2(28) CS', kind='operand', line=1269)
W('33,3373', 0o56225, '', 'DSU', 'DDV', kind='interp', line=1270)
W('33,3374', 0o01235, '', '', 'PIPTIME', 'TU - T(N-1)', kind='operand', line=1271)
W('33,3375', 0o27151, '', '', '2SEC(28)', kind='operand', line=1272)
W('33,3376', 0o76561, '', 'VXSC', 'VSL1', 'G(N-1)(TU - T(N-1))', kind='interp', line=1273)
W('33,3377', 0o01237, '', '', 'GDT/2', 'SCALED AT 2(7) M/CS', kind='operand', line=1274)
W('33,3400', 0o53255, '', 'VAD', 'VAD', 'PUSH UP FOR DELV', kind='interp', line=1275)
W('33,3401', 0o03527, '', '', 'V', 'VU = V(N-1) + DELVU + G(N-1) DTU', kind='operand', line=1276)
W('33,3402', 0o53352, '', 'VSL2', 'VAD', 'SCALE TO 2(5) M/CS AND SUBTRACT', kind='interp', line=1277)
W('33,3403', 0o03734, '', '', 'DELVS', '      MOON ROTATION.', kind='operand', line=1278)
W('33,3404', 0o51406, '', 'PUSH', 'ABVAL', 'STORE IN PD', kind='interp', line=1279)
W('33,3405', 0o43202, '', 'SR4', 'DAD', 'ABS(VM)/8 + 7.5 AT 2(6)', kind='interp', line=1280)
W('33,3406', 0o27145, '', '', '7.5', kind='operand', line=1281)
W('33,3407', 0o24025, '', 'STOVL', '20D', 'STORE IN 20D AND PICK UP VM', kind='interp', line=1282)
W('33,3410', 0o44241, '', 'DOT', 'BDSU', 'V(EST) AT 2(6)', kind='interp', line=1283)
W('33,3411', 0o00001, '', '', '0', 'DELTAV = VMEAS - V(EST)', kind='operand', line=1284)
W('33,3412', 0o51406, '', 'PUSH', 'ABS', kind='interp', line=1285)
W('33,3413', 0o77425, '', 'DSU', 'EXIT', 'ABS(DV) - (7.5 + ABS(VM)/8))', kind='interp', line=1286)
W('33,3414', 0o00025, '', '', '20D', kind='operand', line=1287)

W('33,3415', 0o25672, '', 'INCR', 'LRMCTR', line=1289)
W('33,3416', 0o06723, '', 'TC', 'BRANCH', line=1290)
W('33,3417', 0o13575, '', 'TCF', 'VFAIL', 'DELTA V TOO LARGE.    ALARM', line=1291)
W('33,3420', 0o13575, '', 'TCF', 'VFAIL', 'DELTA V TOO LARGE.    ALARM', line=1292)

W('33,3421', 0o05516, '', 'TC', 'DOWNFLAG', 'TURN OFF VEL FAIL LAMP', line=1294)
W('33,3422', 0o00262, '', 'ADRES', 'VFLSHFLG', kind='data', line=1295)

W('33,3423', 0o30107, '', 'CA', 'FLGWRD11', line=1297)
W('33,3424', 0o74740, '', 'MASK', 'VXINHBIT', line=1298)
W('33,3425', 0o00006, '', 'EXTEND', line=1299)
W('33,3426', 0o13435, '', 'BZF', 'VUPDAT', 'IF VX INHIBIT RESET, INCORPORATE DATA.', line=1300)
# Page 888
W('33,3427', 0o05516, '', 'TC', 'DOWNFLAG', line=1302)
W('33,3430', 0o00250, '', 'ADRES', 'VXINH', 'RESET VX INHIBIT', kind='data', line=1303)

W('33,3431', 0o31651, '', 'CA', 'VSELECT', line=1305)
W('33,3432', 0o67746, '', 'AD', 'NEG2', 'IF VSELECT = 2 (X AXIS).', line=1306)
W('33,3433', 0o00006, '', 'EXTEND', '', 'BYPASS UPDATE', line=1307)
W('33,3434', 0o13514, '', 'BZF', 'ENDVDAT', line=1308)

W('33,3435', 0o40107, 'VUPDAT', 'CS', 'FLGWRD11', line=1310)
W('33,3436', 0o74744, '', 'MASK', 'LRINHBIT', line=1311)
W('33,3437', 0o10000, '', 'CCS', 'A', line=1312)
W('33,3440', 0o13514, '', 'TCF', 'VALTCHK', 'UPDATE INHIBITED', line=1313)

W('33,3441', 0o54155, '', 'TS', 'MPAC +1', line=1315)

W('33,3442', 0o31471, '', 'CA', 'ABVEL', 'STORE E7 ERASABLES NEEDED IN TEMPS', line=1317)
W('33,3443', 0o54130, '', 'TS', 'ABVEL*', line=1318)
W('33,3444', 0o31651, '', 'CA', 'VSELECT', line=1319)
W('33,3445', 0o54131, '', 'TS', 'VSELECT*', line=1320)
W('33,3446', 0o35014, '', 'CA', 'EBANK5', line=1321)
W('33,3447', 0o54003, '', 'TS', 'EBANK', 'CHANGE EBANKS', line=1322)

#   EBANK= LRVF
W('33,3450', 0o41527, '', 'CS', 'LRVF', line=1325)
W('33,3451', 0o60130, '', 'AD', 'ABVEL*', 'IF V < VF, USE WVF', line=1326)
W('33,3452', 0o00006, '', 'EXTEND', line=1327)
W('33,3453', 0o63466, '', 'BZMF', 'USEVF', line=1328)

W('33,3454', 0o40130, '', 'CS', 'ABVEL*', line=1330)
W('33,3455', 0o61526, '', 'AD', 'LRVMAX', 'VMAX - V', line=1331)
W('33,3456', 0o00006, '', 'EXTEND', line=1332)
W('33,3457', 0o63471, '', 'BZMF', 'WSTOR -1', 'IF V > VMAX, W = 0', line=1333)

W('33,3460', 0o00006, '', 'EXTEND', line=1335)
W('33,3461', 0o50131, '', 'INDEX', 'VSELECT*', line=1336)
W('33,3462', 0o71530, '', 'MP', 'LRWVZ', 'WV(VMAX - V)', line=1337)

W('33,3463', 0o00006, '', 'EXTEND', line=1339)
W('33,3464', 0o11526, '', 'DV', 'LRVMAX', 'WV( 1 - V/VMAX )', line=1340)
W('33,3465', 0o13472, '', 'TCF', 'WSTOR', line=1341)

W('33,3466', 0o50131, 'USEVF', 'INDEX', 'VSELECT*', line=1343)
W('33,3467', 0o31533, '', 'CA', 'LRWVFZ', 'USE APPROPRIATE CONSTANT WEIGHT', line=1344)
W('33,3470', 0o13472, '', 'TCF', 'WSTOR', line=1345)

W('33,3471', 0o34755, '', 'CA', 'ZERO', line=1347)
W('33,3472', 0o54154, 'WSTOR', 'TS', 'MPAC', line=1348)
W('33,3473', 0o44745, '', 'CS', 'BIT7', '(=64D)', line=1349)
W('33,3474', 0o61011, '', 'AD', 'MODREG', line=1350)
W('33,3475', 0o00006, '', 'EXTEND', line=1351)
# Page 889
W('33,3476', 0o63501, '', 'BZMF', '+3', 'IF IN P65,P66,P67, USE ANOTHER CONSTANT', line=1353)

W('33,3477', 0o31536, '', 'CA', 'LRWVFF', line=1355)
W('33,3500', 0o54154, '', 'TS', 'MPAC', line=1356)

W('33,3501', 0o35016, '', 'CA', 'EBANK7', line=1358)
W('33,3502', 0o54003, '', 'TS', 'EBANK', 'CHANGE EBANKS', line=1359)

#   EBANK= ABVEL
W('33,3503', 0o06037, '', 'TC', 'INTPRET', line=1362)
W('33,3504', 0o74205, '', 'DMP', 'VXSC', 'W(DELTA V)(VBEAMSM) UP 6-7, 0-5', kind='interp', line=1363)
W('33,3505', 0o77655, '', 'VAD', kind='interp', line=1364)
W('33,3506', 0o03601, '', '', 'V1S', 'ADD WEIGHTED DELTA V TO VELOCITY', kind='operand', line=1365)
W('33,3507', 0o03657, '', 'STORE', 'GNUV', kind='interp', line=1366)
W('33,3510', 0o77776, '', 'EXIT', kind='interp', line=1367)

W('33,3511', 0o03552, '', 'TC', 'QUIKFAZ5', 'DO NOT RE-UPDATE', line=1369)

W('33,3512', 0o36242, '', 'CA', 'SIX', line=1371)
W('33,3513', 0o03534, 'VUPDATED', 'TC', 'GNURVST', 'STORE NEW VELOCITY VECTOR', line=1372)
S('ENDVDAT', 'equals', 0o77514, line=1373)

W('33,3514', 0o03552, 'VALTCHK', 'TC', 'QUIKFAZ5', 'DO NOT REPEAT ABOVE', line=1375)

W('33,3515', 0o34747, '', 'CAF', 'READVBIT', 'TEST READVEL TO SEE IF VELOCITY READING', line=1377)
W('33,3516', 0o70107, '', 'MASK', 'FLGWRD11', 'IS DESIRED.', line=1378)
W('33,3517', 0o10000, '', 'CCS', 'A', line=1379)
W('33,3520', 0o13527, '', 'TCF', 'READV', 'YES -- READ VELOCITY', line=1380)
W('33,3521', 0o41471, '', 'CS', 'ABVEL', 'NO -- SEE IF VELOCITY < 2000 FT/SEC', line=1381)
W('33,3522', 0o62707, '', 'AD', '2KFT/SEC', line=1382)
W('33,3523', 0o00006, '', 'EXTEND', line=1383)
W('33,3524', 0o62540, '', 'BZMF', 'CONTSERV', 'V > 2000 FT/SEC  DO NOT READ VEL', line=1384)

W('33,3525', 0o05504, '', 'TC', 'UPFLAG', 'V < 2000 FT/SEC  SET READVEL AND READ.', line=1386)
W('33,3526', 0o00257, '', 'ADRES', 'READVEL', kind='data', line=1387)

W('33,3527', 0o37720, 'READV', 'CAF', 'PRIO32', 'SET UP JOB TO READ VELOCITY BEAMS.', line=1389)
W('33,3530', 0o05072, '', 'TC', 'NOVAC', line=1390)
#   EBANK= HMEAS
W('33,3531', 0o03616, '', '2CADR', 'LRVJOB', kind='data', line=1392)
W('33,3532', 0o66067, kind='data', line=1392)

W('33,3533', 0o12540, '', 'TCF', 'CONTSERV', 'CONTINUE WITH SERVICER', line=1394)

W('33,3534', 0o54130, 'GNURVST', 'TS', 'BUF', 'STORE GNUR (=GNUV) IN R1S OR V1S', line=1396)
W('33,3535', 0o00006, '', 'EXTEND', '', 'A = 0 FOR R, A = 6 FOR V', line=1397)
W('33,3536', 0o31657, '', 'DCA', 'GNUR', line=1398)
W('33,3537', 0o50130, '', 'INDEX', 'BUF', line=1399)
W('33,3540', 0o53573, '', 'DXCH', 'R1S', line=1400)
W('33,3541', 0o00006, '', 'EXTEND', line=1401)
# Page 890
W('33,3542', 0o31661, '', 'DCA', 'GNUR +2', line=1403)
W('33,3543', 0o50130, '', 'INDEX', 'BUF', line=1404)
W('33,3544', 0o53575, '', 'DXCH', 'R1S +2', line=1405)
W('33,3545', 0o00006, '', 'EXTEND', line=1406)
W('33,3546', 0o31663, '', 'DCA', 'GNUR +4', line=1407)
W('33,3547', 0o50130, '', 'INDEX', 'BUF', line=1408)
W('33,3550', 0o53577, '', 'DXCH', 'R1S +4', line=1409)
W('33,3551', 0o00002, '', 'TC', 'Q', line=1410)

W('33,3552', 0o35007, 'QUIKFAZ5', 'CA', 'EBANK3', line=1412)
W('33,3553', 0o56003, '', 'XCH', 'EBANK', 'SET EBANK 3', line=1413)
W('33,3554', 0o52002, '', 'DXCH', 'L', 'Q TO A, A TO L', line=1414)
#   EBANK= PHSNAME5
W('33,3555', 0o55446, '', 'TS', 'PHSNAME5', line=1416)
W('33,3556', 0o22003, '', 'LXCH', 'EBANK', line=1417)
#   EBANK= DVCNTR
W('33,3557', 0o00000, '', 'TC', 'A', line=1419)

W('33,3560', 0o41671, 'HFAIL', 'CS', 'LRRCTR', line=1421)
W('33,3561', 0o00006, '', 'EXTEND', line=1422)
W('33,3562', 0o13572, '', 'BZF', 'NORLITE', 'IF R = 0, DO NOT TURN ON TRK FAIL', line=1423)
W('33,3563', 0o61670, '', 'AD', 'LRLCTR', line=1424)
W('33,3564', 0o77745, '', 'MASK', 'NEG3', line=1425)
W('33,3565', 0o00006, '', 'EXTEND', '', 'IF L-R LT 4, DO NOT TURN ON TRK FAIL', line=1426)
W('33,3566', 0o13570, '', 'BZF', '+2', line=1427)
W('33,3567', 0o13572, '', 'TCF', 'NORLITE', line=1428)

W('33,3570', 0o05504, '', 'TC', 'UPFLAG', 'AND SET BIT TO TURN ON TRACKER FAIL LITE', line=1430)
W('33,3571', 0o00263, '', 'ADRES', 'HFLSHFLG', kind='data', line=1431)

W('33,3572', 0o31670, 'NORLITE', 'CA', 'LRLCTR', line=1433)
W('33,3573', 0o55671, '', 'TS', 'LRRCTR', 'SET R = L', line=1434)

W('33,3574', 0o13310, '', 'TCF', 'VMEASCHK', line=1436)

W('33,3575', 0o41673, 'VFAIL', 'CS', 'LRSCTR', 'DELTA Q LARGE', line=1438)
W('33,3576', 0o00006, '', 'EXTEND', '', 'IF S = 0, DO NOT TURN ON TRACKER FAIL', line=1439)
W('33,3577', 0o13607, '', 'BZF', 'NOLITE', line=1440)
W('33,3600', 0o61672, '', 'AD', 'LRMCTR', 'M-S', line=1441)
W('33,3601', 0o77745, '', 'MASK', 'NEG3', 'TEST FOR M-S > 3', line=1442)
W('33,3602', 0o00006, '', 'EXTEND', '', 'IF M-S > 3, THEN TWO OR MORE OF THE', line=1443)
W('33,3603', 0o13605, '', 'BZF', '+2', '      LAST FOUR V READINGS WERE BAD,', line=1444)
W('33,3604', 0o13607, '', 'TCF', 'NOLITE', '      SO TURN ON VELOCITY FAIL LIGHT', line=1445)

W('33,3605', 0o05504, '', 'TC', 'UPFLAG', 'AND SET BIT TO TURN ON TRACKER FAIL LITE', line=1447)
W('33,3606', 0o00262, '', 'ADRES', 'VFLSHFLG', kind='data', line=1448)

# Page 891
W('33,3607', 0o31672, 'NOLITE', 'CA', 'LRMCTR', 'SET S = M', line=1451)
W('33,3610', 0o55673, '', 'TS', 'LRSCTR', line=1452)

W('33,3611', 0o11651, '', 'CCS', 'VSELECT', 'TEST FOR Z COMPONENT', line=1454)
W('33,3612', 0o13514, '', 'TCF', 'ENDVDAT', 'NOT Z, DO NOT SET VX INHIBIT', line=1455)

W('33,3613', 0o05504, '', 'TC', 'UPFLAG', 'Z COMPONENT - SET FLAG TO SKIP X', line=1457)
W('33,3614', 0o00250, '', 'ADRES', 'VXINH', 'COMPONENT, AS ERROR MAY BE DUE TO CROSS', kind='data', line=1458)
W('33,3615', 0o13514, '', 'TCF', 'ENDVDAT', 'LOBE LOCK UP NOT DETECTED ON X AXIS.', line=1459)

# Page 892
# ********************************************************************************
# LRVJOB IS SET WHEN THE LEM IS BELOW 15000 FT DURING THE LANDING PHASE
# THIS JOB INITIALIZES THE LANDING RADAR READ ROUTINE FOR 5 VELOCITY
# SAMPLES AND GOES TO SLEEP WHILE THE SAMPLING IS DONE -- ABOUT 500 MS.
# WITH A GOODEND RETURN THE DATA IS STORED IN VMEAS AND BIT7 OF LRSTAT
# IS SET.  THE GIMBAL ANGLES ARE READ ABOUT MIDWAY IN THE SAMPLINGS.

S('170MS', 'equals', 0o4361, line=1469)

W('33,3616', 0o34361, 'LRVJOB', 'CA', '170MS', 'SET TASK TO READ CDUS + PIPAS', line=1471)
W('33,3617', 0o05203, '', 'TC', 'WAITLIST', line=1472)
#   EBANK= LRVTIME
W('33,3620', 0o03757, '', '2CADR', 'RDGIMS', kind='data', line=1474)
W('33,3621', 0o70064, kind='data', line=1474)

W('33,3622', 0o11651, '', 'CCS', 'VSELECT', 'SEQUENCE LR VEL BEAM SELECTOR', line=1476)
W('33,3623', 0o13625, '', 'TCF', '+2', line=1477)
W('33,3624', 0o34752, '', 'CAF', 'TWO', 'IF ZERO, RESET TO TWO', line=1478)
W('33,3625', 0o60000, '', 'DOUBLE', '', '2XVSELECT USED FOR VBEAM INDEX IN LRVEL', line=1479)
W('33,3626', 0o04616, '', 'TC', 'BANKCALL', 'GO INITIALIZE LR VEL READ ROUTINE', line=1480)
W('33,3627', 0o53107, '', 'CADR', 'LRVEL', kind='data', line=1481)
W('33,3630', 0o04616, '', 'TC', 'BANKCALL', 'PUT LRVJOB TO SLEEP ABOUT 500 MS', line=1482)
W('33,3631', 0o17714, '', 'CADR', 'RADSTALL', kind='data', line=1483)
W('33,3632', 0o13665, '', 'TCF', 'VBAD', line=1484)
W('33,3633', 0o11675, '', 'CCS', 'STILBADV', 'IS DATA GOOD JUST PRESENT?', line=1485)
W('33,3634', 0o13666, '', 'TCF', 'VSTILBAD', 'JUST GOOD -- MUST WAIT 4 SECONDS.', line=1486)

W('33,3635', 0o00004, '', 'INHINT', line=1488)
W('33,3636', 0o00006, '', 'EXTEND', '', 'GOOD RETURN -- STOW AWAY VMEAS', line=1489)
W('33,3637', 0o31102, '', 'DCA', 'SAMPLSUM', line=1490)
W('33,3640', 0o53653, '', 'DXCH', 'VMEAS', line=1491)
W('33,3641', 0o34741, '', 'CA', 'EBANK4', 'FOR DOWNLINK', line=1492)
W('33,3642', 0o54003, '', 'TS', 'EBANK', line=1493)
#   EBANK= LRVTIME

W('33,3643', 0o00006, '', 'EXTEND', line=1496)
W('33,3644', 0o31653, '', 'DCA', 'LRVTIME', line=1497)
W('33,3645', 0o53740, '', 'DXCH', 'LRVTIMDL', line=1498)
W('33,3646', 0o00006, '', 'EXTEND', line=1499)
W('33,3647', 0o31655, '', 'DCA', 'LRXCDU', line=1500)
W('33,3650', 0o53735, '', 'DXCH', 'LRXCDUDL', line=1501)
W('33,3651', 0o31656, '', 'CA', 'LRZCDU', line=1502)
W('33,3652', 0o55736, '', 'TS', 'LRZCDUDL', line=1503)
W('33,3653', 0o35016, '', 'CA', 'EBANK7', line=1504)
W('33,3654', 0o54003, '', 'TS', 'EBANK', line=1505)
#   EBANK= VSELECT

W('33,3655', 0o40107, '', 'CS', 'FLGWRD11', 'SET BIT TO INDICATE VELOCITY', line=1508)
W('33,3656', 0o74745, '', 'MASK', 'VELDABIT', 'MEASUREMENT MADE', line=1509)
# Page 893
W('33,3657', 0o26107, '', 'ADS', 'FLGWRD11', line=1511)
W('33,3660', 0o11651, 'ENDLRV', 'CCS', 'VSELECT', 'UPDATE VSELECT', line=1512)
W('33,3661', 0o13663, '', 'TCF', '+2', line=1513)
W('33,3662', 0o34752, '', 'CA', 'TWO', line=1514)
W('33,3663', 0o55651, '', 'TS', 'VSELECT', line=1515)
W('33,3664', 0o15155, '', 'TCF', 'ENDOFJOB', line=1516)

W('33,3665', 0o34752, 'VBAD', 'CAF', 'TWO', 'SET STILBAD TO WAIT 4 SECONDS', line=1518)
W('33,3666', 0o55675, 'VSTILBAD', 'TS', 'STILBADV', line=1519)
W('33,3667', 0o13660, '', 'TCF', 'ENDLRV', line=1520)

# LRHJOB IS SET BY LRHTASK WHEN LEM IS BELOW 25000 FT.  THIS JOB
# INITIALIZES THE LR READ ROUTINE FOR AN ALT MEASUREMENT AND GOES TO
# SLEEP WHILE THE SAMPLING IS DONE -- ABOUT 95 MS.  WITH A GOODEND RETURN
# THE ALT DATA IS STORED IN HMEAS AND BIT7 OF LRSTAT IS SET.

#   BANK 34
#   SETLOC R12STUFF
#   BANK

#   COUNT* $$/SERV

W('34,3716', 0o04616, 'LRHJOB', 'TC', 'BANKCALL', 'INITIATE LR ALT MEASUREMENT', line=1533)
W('34,3717', 0o53073, '', 'CADR', 'LRALT', kind='data', line=1534)
W('34,3720', 0o04616, '', 'TC', 'BANKCALL', 'LRHJOB TO SLEEP ABOUT 95MS', line=1535)
W('34,3721', 0o17714, '', 'CADR', 'RADSTALL', kind='data', line=1536)
W('34,3722', 0o13745, '', 'TCF', 'HBAD', line=1537)
W('34,3723', 0o11674, '', 'CCS', 'STILBADH', 'IS DATA GOOD JUST PRESENT?', line=1538)
W('34,3724', 0o13755, '', 'TCF', 'HSTILBAD', 'JUST GOOD -- MUST WAIT 4 SECONDS.', line=1539)

W('34,3725', 0o00004, '', 'INHINT', line=1541)
W('34,3726', 0o00006, '', 'EXTEND', line=1542)
W('34,3727', 0o31102, '', 'DCA', 'SAMPLSUM', 'GOOD RETURN -- STORE AWAY LRH DATA', line=1543)
W('34,3730', 0o53655, '', 'DXCH', 'HMEAS', 'LRH DATA 1.079 FT/BIT', line=1544)
W('34,3731', 0o00006, '', 'EXTEND', '', 'FOR DOWNLINK', line=1545)
W('34,3732', 0o31561, '', 'DCA', 'PIPTIME1', line=1546)
W('34,3733', 0o53755, '', 'DXCH', 'MKTIME', line=1547)

W('34,3734', 0o00006, '', 'EXTEND', line=1549)
W('34,3735', 0o31157, '', 'DCA', 'CDUTEMPY', 'CDUY,Z = AIG,AMG', line=1550)
W('34,3736', 0o53460, '', 'DXCH', 'AIG', line=1551)

W('34,3737', 0o31155, '', 'CA', 'CDUTEMPX', 'CDUX = AOG', line=1553)
W('34,3740', 0o55461, '', 'TS', 'AOG', line=1554)

W('34,3741', 0o40107, '', 'CS', 'FLGWRD11', 'SET BIT TO INDICATE RANGE', line=1556)
W('34,3742', 0o74750, '', 'MASK', 'RNGEDBIT', 'MEASUREMENT MADE.', line=1557)
W('34,3743', 0o26107, '', 'ADS', 'FLGWRD11', line=1558)
W('34,3744', 0o05155, 'ENDLRH', 'TC', 'ENDOFJOB', 'TERMATE LRHJOB', line=1559)

# Page 894
W('34,3745', 0o30101, 'HBAD', 'CA', 'FLAGWRD5', line=1562)
W('34,3746', 0o74742, '', 'MASK', 'RNGSCBIT', 'IS BAD RETURN DUE TO SCALE CHANGE?', line=1563)
W('34,3747', 0o00006, '', 'EXTEND', line=1564)
W('34,3750', 0o13754, '', 'BZF', 'HSTILBAD -1', 'NO  RESET HSTILBAD', line=1565)
W('34,3751', 0o05516, '', 'TC', 'DOWNFLAG', 'YES  RESET SCALE CHANGE BIT AND IGNORE', line=1566)
W('34,3752', 0o00120, '', 'ADRES', 'RNGSCFLG', kind='data', line=1567)
W('34,3753', 0o05155, '', 'TC', 'ENDOFJOB', line=1568)

W('34,3754', 0o34752, '', 'CAF', 'TWO', 'SET STILBAD TO WAIT 4 SECONDS', line=1570)
W('34,3755', 0o55674, 'HSTILBAD', 'TS', 'STILBADH', line=1571)
W('34,3756', 0o05155, '', 'TC', 'ENDOFJOB', line=1572)

#   BANK 34
#   SETLOC SERV4
#   BANK

#   COUNT* $$/SERV

# RDGIMS IS A TASK SET UP BY LRVJOB TO PICK UP THE IMU CDUS AND TIME
# AT ABOUT THE MIDPOINT OF THE LR VEL READ ROUTINE WHEN 5 VEL SAMPLES
# ARE SPECIFIED.

#   EBANK= LRVTIME
W('34,3757', 0o00006, 'RDGIMS', 'EXTEND', line=1585)
W('34,3760', 0o30025, '', 'DCA', 'TIME2', 'PICK UP TIME2, TIME1', line=1586)
W('34,3761', 0o53653, '', 'DXCH', 'LRVTIME', '      AND SAVE IN LRVTIME', line=1587)

W('34,3762', 0o00006, '', 'EXTEND', line=1589)
W('34,3763', 0o30033, '', 'DCA', 'CDUX', 'PICK UP CDUX AND CDUY', line=1590)
W('34,3764', 0o53655, '', 'DXCH', 'LRXCDU', '      AND SAVE IN LRXCDU AND LRYCDU', line=1591)

W('34,3765', 0o30034, '', 'CA', 'CDUZ', line=1593)
W('34,3766', 0o55656, '', 'TS', 'LRZCDU', 'SAVE CDUZ IN LRZCDU', line=1594)

W('34,3767', 0o30037, '', 'CA', 'PIPAX', line=1596)
W('34,3770', 0o55657, '', 'TS', 'PIPTEM', 'SAVE PIPAX IN PIPTEM', line=1597)

W('34,3771', 0o00006, '', 'EXTEND', line=1599)
W('34,3772', 0o30041, '', 'DCA', 'PIPAY', 'PICK UP PIPAY AND PIPAZ', line=1600)
W('34,3773', 0o53661, '', 'DXCH', 'PIPTEM +1', '      AND SAVE IN PIPTEM +1 AND PIPTEM +2', line=1601)
W('34,3774', 0o05261, '', 'TC', 'TASKOVER', line=1602)

#   BANK 33
#   SETLOC SERVICES
#   BANK

#   COUNT* $$/SERV

#   EBANK= DVCNTR
# Page 895
# HIGATJOB IS SET APPROXIMATELY 6 SECONDS PRIOR TO HIGH GATE DURING
# THE DESCENT BURN PHASE OF LUNAR LANDING.  THIS JOB INITIATES THE
# LANDING RADAR REPOSITIONING ROUTINE AND GOES TO SLEEP UNTIL THE
# LR ANTENNA MOVES FROM POSITION 1 TO POSITION 2.  IF THE LR ANTENNA
# ACHIEVES POSITION 2 WITHIN 22 SECONDS THE ALTITUDE AND VELOCITY
# BEAM VECTORS ARE RECOMPUTED TO REFLECT THE NEW ORIENTATION WITH
# RESPECT TO THE NB.  BIT10 OF LRSTAT IS CLEARED TO ALLOW LR
# MEASUREMENTS AND THE JOB TERMINATES.

W('33,3670', 0o04616, 'HIGATJOB', 'TC', 'BANKCALL', 'START LRPOS2 JOB', line=1621)
W('33,3671', 0o53471, '', 'CADR', 'LRPOS2', kind='data', line=1622)
W('33,3672', 0o04616, '', 'TC', 'BANKCALL', 'PUT HIGATJOB TO SLEEP UNTIL JOB IS DONE', line=1623)
W('33,3673', 0o17714, '', 'CADR', 'RADSTALL', kind='data', line=1624)
W('33,3674', 0o13703, '', 'TCF', 'POSALARM', 'BAD END    ALARM', line=1625)

W('33,3675', 0o37711, 'POSGOOD', 'CA', 'PRIO23', 'REDUCE PRIORITY FOR INTERPRETIVE COMPS.', line=1627)
W('33,3676', 0o05146, '', 'TC', 'PRIOCHNG', line=1628)

W('33,3677', 0o03737, '', 'TC', 'SETPOS2', 'LR IN POS2 -- SET UP TRANSFORMATIONS', line=1630)

W('33,3700', 0o05516, '', 'TC', 'DOWNFLAG', line=1632)
W('33,3701', 0o00252, '', 'ADRES', 'NOLRREAD', 'RESET NOLRREAD FLAG TO ENABLE LR READING', kind='data', line=1633)
W('33,3702', 0o05155, '', 'TC', 'ENDOFJOB', line=1634)

W('33,3703', 0o33720, 'POSALARM', 'CA', 'OCT523', line=1636)
W('33,3704', 0o04616, '', 'TC', 'BANKCALL', line=1637)
W('33,3705', 0o21562, '', 'CADR', 'PRIOLARM', 'FLASH ALARM CODE', kind='data', line=1638)
W('33,3706', 0o16001, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=1639)
W('33,3707', 0o13712, '', 'TCF', '+3', 'PROCEED -- TRY AGAIN', line=1640)
W('33,3710', 0o15155, '', 'TCF', 'ENDOFJOB', 'V 32 E    TERMINATE R12', line=1641)
W('33,3711', 0o05155, '', 'TC', 'ENDOFJOB', line=1642)

W('33,3712', 0o34745, '', 'CA', 'BIT7', 'SEE IF IN POS2 YET', line=1644)
W('33,3713', 0o00006, '', 'EXTEND', line=1645)
W('33,3714', 0o02033, '', 'RAND', 'CHAN33', line=1646)
W('33,3715', 0o00006, '', 'EXTEND', line=1647)
W('33,3716', 0o13675, '', 'BZF', 'POSGOOD', 'POS2 ACHIEVED   SET UP ANTENNA BEAMS', line=1648)
W('33,3717', 0o13703, '', 'TCF', 'POSALARM', "STILL DIDN'T MAKE IT   REALARM", line=1649)

W('33,3720', 0o00523, 'OCT523', 'OCT', '00523', kind='data', line=1651)

W('33,3721', 0o04645, 'SETPOS1', 'TC', 'MAKECADR', 'MUST BE CALLED BY BANKCALL', line=1655)
W('33,3722', 0o55656, '', 'TS', 'LRADRET1', 'SAVE RETURN CADR.  SINCE BUP2 CLOBBERED', line=1656)

W('33,3723', 0o34752, '', 'CAF', 'TWO', line=1658)
W('33,3724', 0o55674, '', 'TS', 'STILBADH', 'INITIALIZE STILBAD', line=1659)
W('33,3725', 0o55675, '', 'TS', 'STILBADV', 'INITIALIZE STILBAD', line=1660)

W('33,3726', 0o34755, '', 'CA', 'ZERO', 'INDEX FOR LRALPHA, LRBETA IN POS 1.', line=1662)
# Page 896
W('33,3727', 0o55670, '', 'TS', 'LRLCTR', 'SET L,M,R, ANS S TO ZERO', line=1664)
W('33,3730', 0o55672, '', 'TS', 'LRMCTR', line=1665)
W('33,3731', 0o55671, '', 'TS', 'LRRCTR', line=1666)
W('33,3732', 0o55673, '', 'TS', 'LRSCTR', line=1667)
W('33,3733', 0o55651, '', 'TS', 'VSELECT', 'INITIALIZE VSELECT', line=1668)

W('33,3734', 0o03740, '', 'TC', 'SETPOS', 'CONTINUE WITH COMPUTATIONS.', line=1670)

W('33,3735', 0o31656, '', 'CA', 'LRADRET1', line=1672)
W('33,3736', 0o04640, '', 'TC', 'BANKJUMP', 'RETURN TO CALLER', line=1673)

W('33,3737', 0o34752, 'SETPOS2', 'CA', 'TWO', 'INDEX FOR POS2', line=1675)
W('33,3740', 0o56002, 'SETPOS', 'XCH', 'Q', 'SAVE INDEX IN Q', line=1676)
W('33,3741', 0o55650, '', 'TS', 'LRADRET', 'SAVE RETURN', line=1677)

W('33,3742', 0o35014, '', 'CA', 'EBANK5', line=1679)
W('33,3743', 0o54003, '', 'TS', 'EBANK', line=1680)
#   EBANK= LRALPHA

W('33,3744', 0o00006, '', 'EXTEND', line=1683)
W('33,3745', 0o50002, '', 'INDEX', 'Q', line=1684)
W('33,3746', 0o31523, '', 'DCA', 'LRALPHA', 'LRALPHA IN A, LRBETA IN L', line=1685)
W('33,3747', 0o54772, '', 'TS', 'CDUSPOT +4', 'ROTATION ABOUT X', line=1686)
W('33,3750', 0o22766, '', 'LXCH', 'CDUSPOT', 'ROTATION ABOUT Y', line=1687)
W('33,3751', 0o34755, '', 'CA', 'ZERO', line=1688)
W('33,3752', 0o54770, '', 'TS', 'CDUSPOT +2', 'ZERO ROTATION ABOUT Z.', line=1689)

W('33,3753', 0o35016, '', 'CA', 'EBANK7', line=1691)
W('33,3754', 0o54003, '', 'TS', 'EBANK', line=1692)
#   EBANK= LRADRET

W('33,3755', 0o06037, '', 'TC', 'INTPRET', line=1695)
W('33,3756', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=1696)
W('33,3757', 0o06516, '', '', 'UNITY', 'CONVERT UNITY(ANTENNA) TO NB', kind='operand', line=1697)
W('33,3760', 0o47651, '', '', 'TRG*SMNB', kind='operand', line=1698)
W('33,3761', 0o26237, '', 'STOVL', 'VYBEAMNB', kind='interp', line=1699)
W('33,3762', 0o06520, '', '', 'UNITX', 'CONVERT UNITX(ANTENNA) TO NB', kind='operand', line=1700)
W('33,3763', 0o77624, '', 'CALL', kind='interp', line=1701)
W('33,3764', 0o47671, '', '', '*SMNB*', kind='operand', line=1702)
W('33,3765', 0o02245, '', 'STORE', 'VXBEAMNB', kind='interp', line=1703)
W('33,3766', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=1704)
W('33,3767', 0o02237, '', '', 'VYBEAMNB', kind='operand', line=1705)
W('33,3770', 0o26231, '', 'STOVL', 'VZBEAMNB', 'Z = X * Y', kind='interp', line=1706)
W('33,3771', 0o26003, '', '', 'HBEAMANT', kind='operand', line=1707)
W('33,3772', 0o77624, '', 'CALL', kind='interp', line=1708)
W('33,3773', 0o47671, '', '', '*SMNB*', 'CONVERT TO NB', kind='operand', line=1709)
W('33,3774', 0o02273, '', 'STORE', 'HBEAMNB', kind='interp', line=1710)
W('33,3775', 0o77776, '', 'EXIT', kind='interp', line=1711)

# Page 897
W('33,3776', 0o01650, '', 'TC', 'LRADRET', line=1714)
