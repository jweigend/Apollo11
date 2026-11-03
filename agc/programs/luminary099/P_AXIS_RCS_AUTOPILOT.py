"""P-AXIS_RCS_AUTOPILOT.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P-AXIS_RCS_AUTOPILOT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1421-1441 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P_AXIS_RCS_AUTOPILOT', 'P-AXIS_RCS_AUTOPILOT.agc', 'Luminary099', pages='1421-1441')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P-AXIS_RCS_AUTOPILOT.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1421-1441
# Mod history:  2009-05-27 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2009-06-05 RSB  Corrected a relative jump from
# +8 to +8D.
# 2009-06-07 RSB  Corrected a typo.
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

# Page 1421
#   BANK 16
#   SETLOC DAPS1
#   BANK

#   EBANK= PERROR
#   COUNT* $$/DAPP

# THE FOLLOWING T5RUPT ENTRY BEGINS THE PROGRAM WHICH CONTROLS THE P-AXIS ACTION OF THE LEM USING THE RCS JETS.
# THE NOMINAL TIME BETWEEN THE P-AXIS RUPTS IS 100 MS IN ALL NON-IDLING MODES OF THE DAP.

W('16,2213', 0o37727, 'PAXIS', 'CA', 'MS100', line=43)
W('16,2214', 0o26030, '', 'ADS', 'TIME5', '*** NECESSARY IN ORDER TO ALLOW', line=44)
# SYNCHRONIZATION WITH OTHER INTERRUPTS ***

W('16,2215', 0o22016, '', 'LXCH', 'BANKRUPT', 'INTERRUPT LEAD IN (CONTINUED)', line=47)
W('16,2216', 0o00006, '', 'EXTEND', line=48)
W('16,2217', 0o22012, '', 'QXCH', 'QRUPT', line=49)

# CHECK IF DAP PASS IS PERMISSIBLE

W('16,2220', 0o11757, '', 'CCS', 'DAPZRUPT', 'IF DAPZRUPT POSITIVE, DAP (JASK) IS', line=53)
W('16,2221', 0o05634, '', 'TC', 'BAILOUT', 'STILL IN PROGRESS AND A RESTART IS', line=54)
W('16,2222', 0o02000, '', 'OCT', '02000', 'CALLED FOR.  IT IS NEVER ZERO', kind='data', line=55)

W('16,2223', 0o02000, '', 'TC', 'CHEKBITS', 'RETURN IS TC I+1 IF DAP SHOULD STAY ON.', line=57)

W('16,2224', 0o30032, '', 'CA', 'CDUX', "READ AND STORE CDU'S", line=59)
W('16,2225', 0o55750, '', 'TS', 'DAPTREG4', line=60)
W('16,2226', 0o30033, '', 'CA', 'CDUY', line=61)
W('16,2227', 0o55751, '', 'TS', 'DAPTREG5', line=62)
W('16,2230', 0o30034, '', 'CA', 'CDUZ', line=63)
W('16,2231', 0o55752, '', 'TS', 'DAPTREG6', line=64)

# ***** KALCMANU-DAP AND "RATE-HOLD"-DAP INTERFACE *****
#
# THE FOLLOWING SECTION IS EXECUTED EVERY 100 MS (10 TIMES A SECOND) WITHIN THE P-AXIS REACTION CONTROL SYSTEM
# AUTOPILOT (WHENEVER THE DAP IS IN OPERATION).

W('16,2232', 0o31635, '', 'CA', 'CDUXD', line=71)
W('16,2233', 0o00006, '', 'EXTEND', line=72)
W('16,2234', 0o21640, '', 'MSU', 'DELCDUX', line=73)
W('16,2235', 0o02256, '', 'TC', '1STOTWOS', line=74)
W('16,2236', 0o55635, '', 'TS', 'CDUXD', line=75)
W('16,2237', 0o31636, '', 'CA', 'CDUYD', line=76)
W('16,2240', 0o00006, '', 'EXTEND', line=77)
W('16,2241', 0o21641, '', 'MSU', 'DELCDUY', line=78)
W('16,2242', 0o02256, '', 'TC', '1STOTWOS', line=79)
W('16,2243', 0o55636, '', 'TS', 'CDUYD', line=80)
W('16,2244', 0o31637, '', 'CA', 'CDUZD', line=81)
W('16,2245', 0o00006, '', 'EXTEND', line=82)
W('16,2246', 0o21642, '', 'MSU', 'DELCDUZ', line=83)
# Page 1422
W('16,2247', 0o02256, '', 'TC', '1STOTWOS', line=85)
W('16,2250', 0o55637, '', 'TS', 'CDUZD', line=86)
W('16,2251', 0o00006, '', 'EXTEND', '', 'DIMINISH MANUAL CONTROL DIRECT RATE', line=87)
W('16,2252', 0o27445, '', 'DIM', 'TCP', 'TIME COUNTERS.', line=88)
W('16,2253', 0o00006, '', 'EXTEND', line=89)
W('16,2254', 0o27457, '', 'DIM', 'TCQR', line=90)

# RATFLOOP COMPUTES JETRATEQ, JRATER, AND 1JACC*NO. PJEETS IN ITEMP1.
# RETURNS TO BACKP.
#
# JETRATE = 1JACC*NO.PJETS*TJP          (NOTE TJ IS THE TIME FIRED DURING CSP)
# JETRATEQ = 1JACCQ(TJU*NO.UJETS - TJV*NO.VJETS)
# JETRATER = 1JACCR(TJU*NO.UJETS + TJV*NO.VJETS)

W('16,2255', 0o12647, '', 'TCF', 'PAXFILT', 'PROCEEDS TO RATELOOP AFTER SUPERJOB', line=99)
W('16,2256', 0o10000, '1STOTWOS', 'CCS', 'A', line=100)
W('16,2257', 0o64753, '', 'AD', 'ONE', line=101)
W('16,2260', 0o00002, '', 'TC', 'Q', line=102)
W('16,2261', 0o40000, '', 'CS', 'A', line=103)
W('16,2262', 0o00002, '', 'TC', 'Q', line=104)
W('16,2263', 0o00006, 'SUBDIVDE', 'EXTEND', '', 'OVERFLOW PROTECTION ROUTINE TO GIVE', line=105)
W('16,2264', 0o71741, '', 'MP', 'DAPTEMP3', 'POSMAX OR NEGMAX IF THE DIVIDE WOULD', line=106)
W('16,2265', 0o21427, '', 'DAS', 'OMEGAU', 'OVERFLOW', line=107)

W('16,2266', 0o00006, '', 'EXTEND', line=109)
W('16,2267', 0o31427, '', 'DCA', 'OMEGAU', line=110)
W('16,2270', 0o53744, '', 'DXCH', 'DAPTEMP5', line=111)
W('16,2271', 0o11426, '', 'CCS', 'OMEGAU', line=112)
W('16,2272', 0o12274, '', 'TCF', '+2', line=113)
W('16,2273', 0o12304, '', 'TCF', 'DIVIDER', line=114)
W('16,2274', 0o62315, '', 'AD', '-OCT630', line=115)
W('16,2275', 0o00006, '', 'EXTEND', line=116)
W('16,2276', 0o62304, '', 'BZMF', 'DIVIDER', line=117)

W('16,2277', 0o11426, '', 'CCS', 'OMEGAU', line=119)
W('16,2300', 0o34733, '', 'CA', 'POSMAX', '45 DEG/SEC', line=120)
W('16,2301', 0o00002, '', 'TC', 'Q', line=121)
W('16,2302', 0o44733, '', 'CS', 'POSMAX', line=122)
W('16,2303', 0o00002, '', 'TC', 'Q', line=123)

W('16,2304', 0o53427, 'DIVIDER', 'DXCH', 'OMEGAU', line=125)
W('16,2305', 0o00006, '', 'EXTEND', line=126)
W('16,2306', 0o11750, '', 'DV', 'DAPTREG4', line=127)
W('16,2307', 0o00002, '', 'TC', 'Q', line=128)

W('16,2310', 0o54007, 'OVERSUB', 'TS', '7', 'RETURNS A UNCHANGED OR LIMITED TO', line=130)
W('16,2311', 0o00002, '', 'TC', 'Q', 'POSMAX OR NEGMAX IF A HAS OVERFLOW', line=131)
W('16,2312', 0o50000, '', 'INDEX', 'A', line=132)
W('16,2313', 0o44734, '', 'CS', 'BIT15 -1', line=133)
# Page 1423
W('16,2314', 0o00002, '', 'TC', 'Q', line=135)

W('16,2315', 0o77147, '-OCT630', 'OCT', '77147', kind='data', line=137)

W('16,2316', 0o31737, 'BACKP', 'CA', 'DAPTEMP1', line=139)
W('16,2317', 0o00006, '', 'EXTEND', line=140)
W('16,2320', 0o71530, '', 'MP', '1JACC', line=141)
W('16,2321', 0o55745, '', 'TS', 'JETRATE', line=142)

# BEGINNING OF THE RATE DERIVATION
# OMEGAP,Q,R      BODY RATES SCALED AT PI/4
# TRAPEDP,Q,R     BODY ANGLE ERRORS FROM PREDICTED ANGLE (PI/40)
# NP(QR)TRAPS     NUMBER OF TIMES ANGLE ERROR HAS BEEN ACCUMULATED
# AOSQ(R)TERM     CHANGE IN RATE DUE TO OFFSET ACCELERATION.  (PI/4)
# JETRATE,Q,R     CHANGE IN RATE DUE TO  JET   ACCELERATION.  (PI/4)
# TRAPSIZE        NEGATIVE LIMIT OF MAGNITUDE OF TRAPEDP, ETC.
# OMEGAU          DP-TEMPORARY STORAGE
# OMEGA = OMEGA + JETRATE + AOSTERM (+TRAPED/NTRAPS IF TRAPED BIG)

W('16,2322', 0o31750, '', 'CAE', 'DAPTREG4', 'CDUX IS STORED HERE', line=154)
W('16,2323', 0o54001, '', 'TS', 'L', line=155)
W('16,2324', 0o00006, '', 'EXTEND', line=156)
W('16,2325', 0o21440, '', 'MSU', 'OLDXFORP', 'SCALED AT PI', line=157)
W('16,2326', 0o23440, '', 'LXCH', 'OLDXFORP', line=158)
W('16,2327', 0o55737, '', 'TS', 'DAPTEMP1', line=159)
W('16,2330', 0o33620, '', 'CA', '1/40', line=160)
W('16,2331', 0o55750, '', 'TS', 'DAPTREG4', line=161)
W('16,2332', 0o41745, '', 'CS', 'JETRATE', line=162)
W('16,2333', 0o00006, '', 'EXTEND', line=163)
W('16,2334', 0o74736, '', 'MP', 'BIT14', line=164)
W('16,2335', 0o27430, '', 'ADS', 'TRAPEDP', line=165)
W('16,2336', 0o31746, '', 'CA', 'JETRATEQ', line=166)
W('16,2337', 0o61545, '', 'AD', 'AOSQTERM', line=167)
W('16,2340', 0o00006, '', 'EXTEND', line=168)
W('16,2341', 0o77736, '', 'MP', '-BIT14', line=169)
W('16,2342', 0o27431, '', 'ADS', 'TRAPEDQ', line=170)
W('16,2343', 0o31747, '', 'CA', 'JETRATER', line=171)
W('16,2344', 0o61546, '', 'AD', 'AOSRTERM', line=172)
W('16,2345', 0o00006, '', 'EXTEND', line=173)
W('16,2346', 0o77736, '', 'MP', '-BIT14', line=174)
W('16,2347', 0o27432, '', 'ADS', 'TRAPEDR', line=175)

W('16,2350', 0o31751, '', 'CA', 'DAPTREG5', 'CDUY IS STORED HERE', line=177)
W('16,2351', 0o54001, '', 'TS', 'L', line=178)
W('16,2352', 0o00006, '', 'EXTEND', line=179)
W('16,2353', 0o21441, '', 'MSU', 'OLDYFORP', 'SCALED AT PI', line=180)
W('16,2354', 0o23441, '', 'LXCH', 'OLDYFORP', line=181)
W('16,2355', 0o55740, '', 'TS', 'DAPTEMP2', line=182)
W('16,2356', 0o00006, '', 'EXTEND', line=183)
W('16,2357', 0o71414, '', 'MP', 'M11', 'M11 SCALED AT 1', line=184)
# Page 1424
W('16,2360', 0o61737, '', 'AD', 'DAPTEMP1', line=186)
W('16,2361', 0o53427, '', 'DXCH', 'OMEGAU', line=187)

W('16,2362', 0o02266, '', 'TC', 'SUBDIVDE +3', 'RETURNS WITH CDU-RATE AT PI/4', line=189)

W('16,2363', 0o00006, '', 'EXTEND', line=191)
W('16,2364', 0o61421, '', 'SU', 'OMEGAP', line=192)
W('16,2365', 0o27430, '', 'ADS', 'TRAPEDP', line=193)
W('16,2366', 0o02310, '', 'TC', 'OVERSUB', line=194)
W('16,2367', 0o55430, '', 'TS', 'TRAPEDP', line=195)
W('16,2370', 0o00006, '', 'EXTEND', line=196)
W('16,2371', 0o31744, '', 'DCA', 'DAPTEMP5', line=197)
W('16,2372', 0o21447, '', 'DAS', 'DXERROR', line=198)
W('16,2373', 0o41454, '', 'CS', 'PLAST', line=199)
W('16,2374', 0o00006, '', 'EXTEND', line=200)
W('16,2375', 0o73620, '', 'MP', '1/40', line=201)
W('16,2376', 0o21447, '', 'DAS', 'DXERROR', 'MANUAL MODE X-ATTITUDE ERROR (DP)', line=202)
W('16,2377', 0o31752, '', 'CA', 'DAPTREG6', 'CDUZ IS STORED HERE', line=203)
W('16,2400', 0o54001, '', 'TS', 'L', line=204)
W('16,2401', 0o00006, '', 'EXTEND', line=205)
W('16,2402', 0o21442, '', 'MSU', 'OLDZFORQ', line=206)
W('16,2403', 0o55741, '', 'TS', 'DAPTEMP3', line=207)
W('16,2404', 0o23442, '', 'LXCH', 'OLDZFORQ', line=208)
W('16,2405', 0o31415, '', 'CA', 'M21', line=209)
W('16,2406', 0o00006, '', 'EXTEND', line=210)
W('16,2407', 0o71740, '', 'MP', 'DAPTEMP2', line=211)
W('16,2410', 0o53427, '', 'DXCH', 'OMEGAU', line=212)
W('16,2411', 0o31417, '', 'CA', 'M22', line=213)
W('16,2412', 0o02263, '', 'TC', 'SUBDIVDE', line=214)

W('16,2413', 0o00006, '', 'EXTEND', line=216)
W('16,2414', 0o61422, '', 'SU', 'OMEGAQ', line=217)
W('16,2415', 0o27431, '', 'ADS', 'TRAPEDQ', line=218)
W('16,2416', 0o02310, '', 'TC', 'OVERSUB', line=219)
W('16,2417', 0o55431, '', 'TS', 'TRAPEDQ', line=220)
W('16,2420', 0o00006, '', 'EXTEND', line=221)
W('16,2421', 0o31744, '', 'DCA', 'DAPTEMP5', line=222)
W('16,2422', 0o21451, '', 'DAS', 'DYERROR', line=223)
W('16,2423', 0o41455, '', 'CS', 'QLAST', line=224)
W('16,2424', 0o00006, '', 'EXTEND', line=225)
W('16,2425', 0o73620, '', 'MP', '1/40', line=226)
W('16,2426', 0o21451, '', 'DAS', 'DYERROR', 'MANUAL MODE Y-ATTITUDE ERROR (DP)', line=227)
W('16,2427', 0o31416, '', 'CA', 'M31', line=228)
W('16,2430', 0o00006, '', 'EXTEND', line=229)
W('16,2431', 0o71740, '', 'MP', 'DAPTEMP2', line=230)
W('16,2432', 0o53427, '', 'DXCH', 'OMEGAU', line=231)
W('16,2433', 0o31420, '', 'CA', 'M32', line=232)

W('16,2434', 0o02263, '', 'TC', 'SUBDIVDE', line=234)
# Page 1425
W('16,2435', 0o00006, '', 'EXTEND', line=236)
W('16,2436', 0o61423, '', 'SU', 'OMEGAR', line=237)
W('16,2437', 0o27432, '', 'ADS', 'TRAPEDR', line=238)
W('16,2440', 0o02310, '', 'TC', 'OVERSUB', line=239)
W('16,2441', 0o55432, '', 'TS', 'TRAPEDR', 'TRAPEDS HAVE ALL BEEN COMPUTED', line=240)

W('16,2442', 0o00006, '', 'EXTEND', line=242)
W('16,2443', 0o31744, '', 'DCA', 'DAPTEMP5', line=243)
W('16,2444', 0o21453, '', 'DAS', 'DZERROR', line=244)
W('16,2445', 0o41456, '', 'CS', 'RLAST', line=245)
W('16,2446', 0o00006, '', 'EXTEND', line=246)
W('16,2447', 0o73620, '', 'MP', '1/40', line=247)
W('16,2450', 0o21453, '', 'DAS', 'DZERROR', 'MANUAL MODE Z-ATTITUDE ERROR (DP)', line=248)
W('16,2451', 0o30111, '', 'CA', 'DAPBOOLS', 'PICK UP PAD LOADED STATE ESTIMATOR GAINS', line=249)
W('16,2452', 0o74737, '', 'MASK', 'CSMDOCKD', line=250)
W('16,2453', 0o00006, '', 'EXTEND', line=251)
W('16,2454', 0o12462, '', 'BZF', 'LMONLY', line=252)
W('16,2455', 0o00006, '', 'EXTEND', '', 'DOCKED', line=253)
W('16,2456', 0o31405, '', 'DCA', 'DKOMEGAN', line=254)
W('16,2457', 0o53751, '', 'DXCH', 'DAPTREG4', line=255)
W('16,2460', 0o31403, '', 'CA', 'DKTRAP', line=256)
W('16,2461', 0o12466, '', 'TCF', '+5', line=257)
W('16,2462', 0o00006, 'LMONLY', 'EXTEND', '', 'UNDOCKED', line=258)
W('16,2463', 0o31410, '', 'DCA', 'LMOMEGAN', line=259)
W('16,2464', 0o53751, '', 'DXCH', 'DAPTREG4', line=260)
W('16,2465', 0o31406, '', 'CA', 'LMTRAP', line=261)
W('16,2466', 0o55752, '', 'TS', 'DAPTREG6', line=262)
W('16,2467', 0o11430, '', 'CCS', 'TRAPEDP', line=263)
W('16,2470', 0o12472, '', 'TCF', '+2', line=264)
W('16,2471', 0o12507, '', 'TCF', 'SMALPDIF', line=265)
W('16,2472', 0o61752, '', 'AD', 'DAPTREG6', 'TRAPSIZE > ABOUT 77001 %-1.4DEG/SEC"', line=266)
W('16,2473', 0o00006, '', 'EXTEND', line=267)
W('16,2474', 0o62507, '', 'BZMF', 'SMALPDIF', line=268)
W('16,2475', 0o22007, '', 'ZL', line=269)
W('16,2476', 0o23430, '', 'LXCH', 'TRAPEDP', line=270)
W('16,2477', 0o34755, '', 'CA', 'ZERO', line=271)
W('16,2500', 0o00006, '', 'EXTEND', line=272)
W('16,2501', 0o11433, '', 'DV', 'NPTRAPS', line=273)
W('16,2502', 0o27421, '', 'ADS', 'OMEGAP', line=274)
W('16,2503', 0o02310, '', 'TC', 'OVERSUB', line=275)
W('16,2504', 0o55421, '', 'TS', 'OMEGAP', line=276)
W('16,2505', 0o31750, '', 'CA', 'DAPTREG4 ABOUT 10', line=277)
W('16,2506', 0o55433, '', 'TS', 'NPTRAPS', line=278)
W('16,2507', 0o25433, 'SMALPDIF', 'INCR', 'NPTRAPS', line=279)
W('16,2510', 0o31745, 'P-RATE', 'CA', 'JETRATE', line=280)
W('16,2511', 0o27421, '', 'ADS', 'OMEGAP', line=281)
W('16,2512', 0o02310, '', 'TC', 'OVERSUB', line=282)
W('16,2513', 0o55421, '', 'TS', 'OMEGAP', line=283)

W('16,2514', 0o11431, '', 'CCS', 'TRAPEDQ', line=285)
# Page 1426
W('16,2515', 0o12517, '', 'TCF', '+2', line=287)
W('16,2516', 0o12544, '', 'TCF', 'Q-RATE', line=288)
W('16,2517', 0o61752, '', 'AD', 'DAPTREG6', 'TRAPSIZE > ABOUT 77001 %-1.4DEG/SEC"', line=289)
W('16,2520', 0o00006, '', 'EXTEND', line=290)
W('16,2521', 0o62544, '', 'BZMF', 'Q-RATE', line=291)
W('16,2522', 0o22007, '', 'ZL', line=292)
W('16,2523', 0o23431, '', 'LXCH', 'TRAPEDQ', line=293)
W('16,2524', 0o34755, '', 'CA', 'ZERO', line=294)
W('16,2525', 0o00006, '', 'EXTEND', line=295)
W('16,2526', 0o11434, '', 'DV', 'NQTRAPS', line=296)
W('16,2527', 0o55737, '', 'TS', 'DAPTEMP1', 'SAVE FOR OFFSET ESTIMATE', line=297)
W('16,2530', 0o27422, '', 'ADS', 'OMEGAQ', line=298)
W('16,2531', 0o02310, '', 'TC', 'OVERSUB', line=299)
W('16,2532', 0o55422, '', 'TS', 'OMEGAQ', line=300)
W('16,2533', 0o31750, '', 'CA', 'DAPTREG4', 'ABOUT 10 OR 0 FOR DOCKED OR UNDOCKED', line=301)
W('16,2534', 0o57434, '', 'XCH', 'NQTRAPS', line=302)
W('16,2535', 0o61751, '', 'AD', 'DAPTREG5', 'KAOS > ABOUT 60D %N/N_60"', line=303)
W('16,2536', 0o57737, '', 'XCH', 'DAPTEMP1', line=304)
W('16,2537', 0o00006, '', 'EXTEND', line=305)
W('16,2540', 0o74756, '', 'MP', 'FIVE', line=306)
W('16,2541', 0o00006, '', 'EXTEND', line=307)
W('16,2542', 0o11737, '', 'DV', 'DAPTEMP1', line=308)
W('16,2543', 0o27537, '', 'ADS', 'AOSQ', line=309)
W('16,2544', 0o25434, 'Q-RATE', 'INCR', 'NQTRAPS', line=310)
W('16,2545', 0o31746, '', 'CA', 'JETRATEQ', line=311)
W('16,2546', 0o61545, '', 'AD', 'AOSQTERM', line=312)
W('16,2547', 0o27422, '', 'ADS', 'OMEGAQ', line=313)
W('16,2550', 0o02310, '', 'TC', 'OVERSUB', line=314)
W('16,2551', 0o55422, '', 'TS', 'OMEGAQ', line=315)

W('16,2552', 0o11432, '', 'CCS', 'TRAPEDR', line=317)
W('16,2553', 0o12555, '', 'TCF', '+2', line=318)
W('16,2554', 0o12602, '', 'TCF', 'R-RATE', line=319)
W('16,2555', 0o61752, '', 'AD', 'DAPTREG6', 'TRAPSIZE > ABOUT 77001 %-1.4DEG/SEC"', line=320)
W('16,2556', 0o00006, '', 'EXTEND', line=321)
W('16,2557', 0o62602, '', 'BZMF', 'R-RATE', line=322)
W('16,2560', 0o22007, '', 'ZL', line=323)
W('16,2561', 0o23432, '', 'LXCH', 'TRAPEDR', line=324)
W('16,2562', 0o34755, '', 'CA', 'ZERO', line=325)
W('16,2563', 0o00006, '', 'EXTEND', line=326)
W('16,2564', 0o11435, '', 'DV', 'NRTRAPS', line=327)
W('16,2565', 0o55740, '', 'TS', 'DAPTEMP2', 'SAVE FOR OFFSET ESTIMATE', line=328)
W('16,2566', 0o27423, '', 'ADS', 'OMEGAR', line=329)
W('16,2567', 0o02310, '', 'TC', 'OVERSUB', line=330)
W('16,2570', 0o55423, '', 'TS', 'OMEGAR', line=331)
W('16,2571', 0o31750, '', 'CA', 'DAPTREG4', 'ABOUT 10 OR 0 FOR DOCKED OR UNDOCKED', line=332)
W('16,2572', 0o57435, '', 'XCH', 'NRTRAPS', line=333)
W('16,2573', 0o61751, '', 'AD', 'DAPTREG5', 'KAOS > ABOUT 60D %N/N_60"', line=334)
W('16,2574', 0o57740, '', 'XCH', 'DAPTEMP2', line=335)
W('16,2575', 0o00006, '', 'EXTEND', line=336)
# Page 1427
W('16,2576', 0o74756, '', 'MP', 'FIVE', line=338)
W('16,2577', 0o00006, '', 'EXTEND', line=339)
W('16,2600', 0o11740, '', 'DV', 'DAPTEMP2', line=340)
W('16,2601', 0o27541, '', 'ADS', 'AOSR', line=341)
W('16,2602', 0o25435, 'R-RATE', 'INCR', 'NRTRAPS', line=342)
W('16,2603', 0o31747, '', 'CA', 'JETRATER', line=343)
W('16,2604', 0o61546, '', 'AD', 'AOSRTERM', line=344)
W('16,2605', 0o27423, '', 'ADS', 'OMEGAR', line=345)
W('16,2606', 0o02310, '', 'TC', 'OVERSUB', line=346)
W('16,2607', 0o55423, '', 'TS', 'OMEGAR', line=347)

# END OF RATE DERIVATION
# BEGIN OFFSET ESTIMATER
# IN POWERED FLIGHT, AOSTASK WILL BE CALLED EVERY 2 SECONDS.
# AOS = AOS + K*SUMRATE

W('16,2610', 0o40111, '', 'CS', 'DAPBOOLS', line=354)
W('16,2611', 0o74744, '', 'MASK', 'DRIFTBIT', line=355)
W('16,2612', 0o10000, '', 'CCS', 'A', line=356)
W('16,2613', 0o12624, '', 'TCF', 'WORKTIME', line=357)
W('16,2614', 0o55424, '', 'TS', 'ALPHAQ', 'ZERO THE OFFSET ACCELERATION VALUES.', line=358)
W('16,2615', 0o55425, '', 'TS', 'ALPHAR', line=359)
W('16,2616', 0o55545, '', 'TS', 'AOSQTERM', line=360)
W('16,2617', 0o55546, '', 'TS', 'AOSRTERM', line=361)
W('16,2620', 0o55537, '', 'TS', 'AOSQ', line=362)
W('16,2621', 0o55541, '', 'TS', 'AOSR', line=363)
W('16,2622', 0o12667, '', 'TCF', 'PRETIMCK', line=364)
W('16,2623', 0o00074, 'KAOS', 'DEC', '60', kind='data', line=365)
W('16,2624', 0o31510, 'WORKTIME', 'CA', 'QACCDOT', line=366)
W('16,2625', 0o00006, '', 'EXTEND', line=367)
W('16,2626', 0o74766, '', 'MP', 'CALLCODE', 'OCTAL 00032 IS DECIMAL .1 AT 2(6).', line=368)
W('16,2627', 0o21540, '', 'DAS', 'AOSQ', line=369)
W('16,2630', 0o31537, '', 'CA', 'AOSQ', line=370)
W('16,2631', 0o55424, '', 'TS', 'ALPHAQ', line=371)
W('16,2632', 0o00006, '', 'EXTEND', line=372)
W('16,2633', 0o73616, '', 'MP', '200MS', '.2 AT 1', line=373)
W('16,2634', 0o55545, '', 'TS', 'AOSQTERM', line=374)
W('16,2635', 0o31512, '', 'CA', 'RACCDOT', line=375)
W('16,2636', 0o00006, '', 'EXTEND', line=376)
W('16,2637', 0o74766, '', 'MP', 'CALLCODE', 'OCTAL 00032 IS DECIMAL .1 AT 2(6).', line=377)
W('16,2640', 0o21542, '', 'DAS', 'AOSR', line=378)
W('16,2641', 0o31541, '', 'CA', 'AOSR', line=379)
W('16,2642', 0o55425, '', 'TS', 'ALPHAR', line=380)
W('16,2643', 0o00006, '', 'EXTEND', line=381)
W('16,2644', 0o73616, '', 'MP', '200MS', '.2 AT 1', line=382)
W('16,2645', 0o55546, '', 'TS', 'AOSRTERM', line=383)
W('16,2646', 0o12667, '', 'TCF', 'PRETIMCK', line=384)

# Page 1428
W('16,2647', 0o34747, 'PAXFILT', 'CA', 'CALLGMBL', 'EXECUTE ACDT+C12, IF NEEDED.', line=387)
W('16,2650', 0o71273, '', 'MASK', 'RCSFLAGS', line=388)
W('16,2651', 0o10000, '', 'CCS', 'A', 'CALLGMBL IS NOT BIT15, SO THIS TEST IS', line=389)
W('16,2652', 0o03736, '', 'TC', 'ACDT+C12', 'VALID.', line=390)

W('16,2653', 0o52011, '', 'DXCH', 'ARUPT', line=392)
W('16,2654', 0o53754, '', 'DXCH', 'DAPARUPT', line=393)
W('16,2655', 0o32666, '', 'CA', 'SUPERJOB', 'SETTING UP THE SUPERJOB', line=394)
W('16,2656', 0o56017, '', 'XCH', 'BRUPT', line=395)
W('16,2657', 0o22012, '', 'LXCH', 'QRUPT', line=396)
W('16,2660', 0o53756, '', 'DXCH', 'DAPBQRPT', line=397)
W('16,2661', 0o32665, '', 'CA', 'SUPERADR', line=398)
W('16,2662', 0o52016, '', 'DXCH', 'ZRUPT', line=399)
W('16,2663', 0o53760, '', 'DXCH', 'DAPZRUPT', line=400)
W('16,2664', 0o15275, '', 'TCF', 'NOQBRSM +1', 'RELINT (JUST IN CASE) AND RESUME, IN THE', line=401)
# FORM OF A JASK, AT SUPERJOB.

W('16,2665', 0o02667, 'SUPERADR', 'GENADR', 'SUPERJOB +1', kind='data', line=404)

# COUNT DOWN GIMBAL DRIVE TIMERS AND TURN OFF DRIVES IF REQUIRED.

W('16,2666', 0o13641, 'SUPERJOB', 'TCF', 'RATELOOP', line=408)
W('16,2667', 0o11632, 'PRETIMCK', 'CCS', 'QGIMTIMR', line=409)
W('16,2670', 0o12710, '', 'TCF', 'DECQTIMR', 'POSITIVE -- COUNTING DOWN', line=410)
W('16,2671', 0o12714, '', 'TCF', 'TURNOFFQ', 'NEGATIVE -- DRIVE SHOULD BE ENDED', line=411)
W('16,2672', 0o11634, 'CHKRTIMR', 'CCS', 'RGIMTIMR', 'NEGATIVE -- INACTIVE', line=412)
W('16,2673', 0o12712, '', 'TCF', 'DECRTIMR', '(NEG ZERO -- IMPOSSIBLE)', line=413)
W('16,2674', 0o12724, '', 'TCF', 'TURNOFFR', 'REPEATED (ABOVE) FOR R AXIS.', line=414)

W('16,2675', 0o00006, '', 'EXTEND', '', 'DECREMENT DOCKED JET INHIBITION COUNTERS', line=416)
W('16,2676', 0o27767, '', 'DIM', 'PJETCTR', line=417)
W('16,2677', 0o00006, '', 'EXTEND', line=418)
W('16,2700', 0o27770, '', 'DIM', 'UJETCTR', line=419)
W('16,2701', 0o00006, '', 'EXTEND', line=420)
W('16,2702', 0o27771, '', 'DIM', 'VJETCTR', line=421)
W('16,2703', 0o34740, '', 'CA', 'BIT12', line=422)
W('16,2704', 0o71273, '', 'MASK', 'RCSFLAGS', line=423)
W('16,2705', 0o00006, '', 'EXTEND', line=424)
W('16,2706', 0o12734, '', 'BZF', 'SKIPPAXS', line=425)
W('16,2707', 0o02740, '', 'TC', 'CHKVISFZ', line=426)
W('16,2710', 0o55632, 'DECQTIMR', 'TS', 'QGIMTIMR', 'COUNT TIMERS DOWN TO POS ZERO.', line=427)
W('16,2711', 0o12672, '', 'TCF', 'CHKRTIMR', line=428)
W('16,2712', 0o55634, 'DECRTIMR', 'TS', 'RGIMTIMR', line=429)
W('16,2713', 0o12675, '', 'TCF', 'CHKRTIMR +3', line=430)

W('16,2714', 0o55501, 'TURNOFFQ', 'TS', 'NEGUQ', 'HALT DRIVES.', line=432)
W('16,2715', 0o55510, '', 'TS', 'QACCDOT', line=433)
W('16,2716', 0o45007, '', 'CS', 'QGIMBITS', line=434)
W('16,2717', 0o00006, '', 'EXTEND', line=435)
# Page 1429
W('16,2720', 0o03012, '', 'WAND', 'CHAN12', line=437)
W('16,2721', 0o34735, '', 'CAF', 'NEGMAX', line=438)
W('16,2722', 0o55632, '', 'TS', 'QGIMTIMR', line=439)
W('16,2723', 0o12672, '', 'TCF', 'CHKRTIMR', line=440)
W('16,2724', 0o55503, 'TURNOFFR', 'TS', 'NEGUR', line=441)
W('16,2725', 0o55512, '', 'TS', 'RACCDOT', line=442)
W('16,2726', 0o45020, '', 'CS', 'RGIMBITS', line=443)
W('16,2727', 0o00006, '', 'EXTEND', line=444)
W('16,2730', 0o03012, '', 'WAND', 'CHAN12', line=445)
W('16,2731', 0o34735, '', 'CAF', 'NEGMAX', line=446)
W('16,2732', 0o55634, '', 'TS', 'RGIMTIMR', line=447)
W('16,2733', 0o12675, '', 'TCF', 'CHKRTIMR +3', line=448)
S('QGIMBITS', 'equals', 0o5007, line=449)  # BITS 9 AND 10 (OF CHANNEL 12).
S('RGIMBITS', 'equals', 0o5020, line=450)  # BITS 11 AND 12 (OF CHANNEL 12).

W('16,2734', 0o41273, 'SKIPPAXS', 'CS', 'RCSFLAGS', line=452)
W('16,2735', 0o74740, '', 'MASK', 'BIT12', line=453)
W('16,2736', 0o27273, '', 'ADS', 'RCSFLAGS', 'BIT 12 SET TO 1.', line=454)
W('16,2737', 0o13624, '', 'TCF', 'QRAXIS', 'GO TO QRAXIS OR TO CTS.', line=455)

# Y-X TRANSLATION
#
# INPUT:        BITS 9-12 OF CH31 (FROM TRANSLATION CONTROLLER)
#
# OUTPUT:       NEXTP
#
# NEXTP IS THE CHANNEL 6 CODE OF JETS FOR THE DESIRED TRANSLATION.
# IF THERE ARE FAILURES IN THE DESIRED POLICY, THEN
# (1) FOR DIAGONAL TRANS:         UNFAILED PAIR
# ALARM (IF NO PAIR)
# (2) FOR PRINCIPAL TRANS:        TRY TO TACK WITH DIAGONAL PAIRS
# ALARM (IF DIAGONAL PAIRS ARE FAILED)

W('16,2740', 0o00006, 'CHKVISFZ', 'EXTEND', line=470)
W('16,2741', 0o00031, '', 'READ', 'CHAN31', line=471)
W('16,2742', 0o40000, '', 'CS', 'A', line=472)
W('16,2743', 0o73613, '', 'MASK', '07400OCT', line=473)
W('16,2744', 0o00006, '', 'EXTEND', line=474)
W('16,2745', 0o13014, '', 'BZF', 'TSNEXTP', line=475)
W('16,2746', 0o00006, '', 'EXTEND', line=476)
W('16,2747', 0o74745, '', 'MP', 'BIT7', line=477)
W('16,2750', 0o50000, '', 'INDEX', 'A', line=478)
W('16,2751', 0o33572, '', 'CA', 'INDXYZ', line=479)
W('16,2752', 0o55744, '', 'TS', 'ROTINDEX', line=480)
W('16,2753', 0o36242, 'TRYUORV', 'CA', 'SIX', line=481)
W('16,2754', 0o03551, '', 'TC', 'SELECTYZ', line=482)
W('16,2755', 0o46242, '', 'CS', 'SIX', line=483)
W('16,2756', 0o61743, '', 'AD', 'NUMBERT', line=484)
W('16,2757', 0o00006, '', 'EXTEND', line=485)
# Page 1430
W('16,2760', 0o13013, '', 'BZF', 'TSNEXTP -1', line=487)
W('16,2761', 0o44756, '', 'CS', 'FIVE', line=488)
W('16,2762', 0o61744, '', 'AD', 'ROTINDEX', line=489)
W('16,2763', 0o00006, '', 'EXTEND', line=490)
W('16,2764', 0o63002, '', 'BZMF', 'ALTERYZ', line=491)
W('16,2765', 0o41743, '', 'CS', 'NUMBERT', line=492)
W('16,2766', 0o64751, '', 'AD', 'FOUR', line=493)
W('16,2767', 0o00006, '', 'EXTEND', line=494)
W('16,2770', 0o63013, '', 'BZMF', 'TSNEXTP -1', line=495)
W('16,2771', 0o05567, 'ABORTYZ', 'TC', 'ALARM', line=496)
W('16,2772', 0o02001, '', 'OCT', '02001', kind='data', line=497)
W('16,2773', 0o34753, '', 'CA', 'BIT1', 'INVERT BIT 1 OF RCSFLAGS.', line=498)
W('16,2774', 0o23273, '', 'LXCH', 'RCSFLAGS', line=499)
W('16,2775', 0o00006, '', 'EXTEND', line=500)
W('16,2776', 0o06001, '', 'RXOR', '1', line=501)
W('16,2777', 0o55273, '', 'TS', 'RCSFLAGS', line=502)
W('16,3000', 0o34755, '', 'CA', 'ZERO', line=503)
W('16,3001', 0o13014, '', 'TCF', 'TSNEXTP', line=504)
W('16,3002', 0o34753, 'ALTERYZ', 'CA', 'BIT1', 'INVERT BIT 1 OF RCSFLAGS.', line=505)
W('16,3003', 0o23273, '', 'LXCH', 'RCSFLAGS', line=506)
W('16,3004', 0o00006, '', 'EXTEND', line=507)
W('16,3005', 0o06001, '', 'RXOR', '1', line=508)
W('16,3006', 0o55273, '', 'TS', 'RCSFLAGS', line=509)
W('16,3007', 0o74753, '', 'MASK', 'BIT1', line=510)
W('16,3010', 0o64751, '', 'AD', 'FOUR', line=511)
W('16,3011', 0o27744, '', 'ADS', 'ROTINDEX', line=512)
W('16,3012', 0o12753, '', 'TCF', 'TRYUORV', line=513)
W('16,3013', 0o31741, '', 'CA', 'POLYTEMP', line=514)
W('16,3014', 0o55472, 'TSNEXTP', 'TS', 'NEXTP', line=515)

# STATE LOGIC
# CHECK IN ORDER:         IF ON
# LPDPHASE                GO TO PURGENCY
# PULSES                  MINIMUM PULSE LOTIC
# DETENT(BIT15 CH31)      RATE COMMAND
# GOTO TO PURGENCY

W('16,3015', 0o34737, '', 'CA', 'BIT13', 'CHECK STICK IF IN ATT. HOLD.', line=524)
W('16,3016', 0o00006, '', 'EXTEND', line=525)
W('16,3017', 0o02031, '', 'RAND', 'CHAN31', line=526)
W('16,3020', 0o00006, '', 'EXTEND', line=527)
W('16,3021', 0o13027, '', 'BZF', 'MANMODE', line=528)

W('16,3022', 0o30111, '', 'CA', 'DAPBOOLS', line=530)
W('16,3023', 0o74743, '', 'MASK', 'XOVINHIB', line=531)
W('16,3024', 0o10000, '', 'CCS', 'A', line=532)
W('16,3025', 0o13463, '', 'TCF', 'PURGENCY', 'ATTITUDE STEER DURING VISIBILITY PHASE', line=533)

W('16,3026', 0o13071, '', 'TCF', 'DETENTCK', line=535)
W('16,3027', 0o34735, 'MANMODE', 'CA', 'PULSES', 'PULSES IS ONE FOR PULSE MODE', line=536)
W('16,3030', 0o70111, '', 'MASK', 'DAPBOOLS', line=537)
# Page 1431
W('16,3031', 0o00006, '', 'EXTEND', line=539)
W('16,3032', 0o13071, '', 'BZF', 'DETENTCK', 'BRANCH FOR RATE COMMAND', line=540)

W('16,3033', 0o34755, '', 'CA', 'ZERO', line=542)
W('16,3034', 0o55464, '', 'TS', 'PERROR', line=543)

# MINIMUM IMPULSE MODE

W('16,3035', 0o30032, '', 'CA', 'CDUX', line=547)
W('16,3036', 0o55635, '', 'TS', 'CDUXD', line=548)

W('16,3037', 0o11460, '', 'CCS', 'OLDPMIN', line=550)
W('16,3040', 0o13054, '', 'TCF', 'CHECKP', line=551)

W('16,3041', 0o34751, 'FIREP', 'CA', 'BIT3', line=553)
W('16,3042', 0o00006, '', 'EXTEND', line=554)
W('16,3043', 0o02031, '', 'RAND', 'CHAN31', line=555)
W('16,3044', 0o00006, '', 'EXTEND', line=556)
W('16,3045', 0o13064, '', 'BZF', '+XMIN', line=557)

W('16,3046', 0o34750, '', 'CA', 'BIT4', line=559)
W('16,3047', 0o00006, '', 'EXTEND', line=560)
W('16,3050', 0o02031, '', 'RAND', 'CHAN31', line=561)
W('16,3051', 0o00006, '', 'EXTEND', line=562)
W('16,3052', 0o13062, '', 'BZF', '-XMIN', line=563)

W('16,3053', 0o13442, '', 'TCF', 'JETSOFF', line=565)

W('16,3054', 0o00006, 'CHECKP', 'EXTEND', line=567)
W('16,3055', 0o00031, '', 'READ', 'CHAN31', line=568)
W('16,3056', 0o40000, '', 'CS', 'A', line=569)
W('16,3057', 0o75751, '', 'MASK', 'OCT14', line=570)
W('16,3060', 0o55460, '', 'TS', 'OLDPMIN', line=571)
W('16,3061', 0o13442, '', 'TCF', 'JETSOFF', line=572)

W('16,3062', 0o44363, '-XMIN', 'CS', 'TEN', 'ANYTHING LESS THAN 14MS. CORRECTED', line=574)
W('16,3063', 0o13065, '', 'TCF', '+2', '      IN JET SELECTION ROUTINE', line=575)
W('16,3064', 0o34363, '+XMIN', 'CA', 'TEN', line=576)
W('16,3065', 0o55524, '', 'TS', 'TJP', line=577)
W('16,3066', 0o34753, '', 'CA', 'ONE', line=578)
W('16,3067', 0o55460, '', 'TS', 'OLDPMIN', line=579)
W('16,3070', 0o13350, '', 'TCF', 'PJETSLEC -6', line=580)

# MANUAL RATE COMMAND MODE
# ========================
# BY ROBERT F. STENGEL
#
# THIS MODE PROVIDES RCAH MANUAL CONTROL THRU 2 CONTROL LAWS:  1) DIRECT RATE AND 2) PSEUDO-AUTO.
# THE DIRECT RATE MODE AFFORDS IMMEDIATE CONTROL WITHOUT OVERSHOOT.  THE PSEUDO-AUTO MODE PROVIDES PRECISE
# RATE CONTROL AND ATTITUDE HOLD.
#
# Page 1432
# IN DIRECT RATE, JETS ARE FIRED WHEN STICK POSITION CHANGES BY A FIXED NUMBER OF INCREMENTS IN ONE DAP CYCLE.
# THE `BREAKOUT LEVEL' IS .6 D/S FOR LM-ONLY AND .3 D/S FOR CSM-DOCKED.  THIS LAW NULLS THE RATE ERROR TO WITHIN
# THE `TARGET DEADBAND', WHICH EQUALS THE BREAKOUT LEVEL.
#
# IN PSEUDO-AUTO, BODY-FIXED RATE AND ATTITUDE ERRORS ARE SUPPLIED TO TJETLAW, WHICH EXERCISES CONTROL.
# CONTROL SWITCHES FROM DIRECT RATE TO PSEUDO-AUTO IF THE TARGET DB IS ACHIEVED OR IF TIME IN (1) EXCEEDS 4 SEC.
# IF THE INITIAL COMMAND DOES NOT EXCEED THE BREAKOUT LEVEL, CONTROL GOES TO PSEUDO-AUTO IMMEDIATELY.
#
# SINCE P-AXIS CONTROL IS SEPARATE FROM Q,R AXES CONTROL, IT IS POSSIBLE TO USE (1) IN P-AXIS AND (2) IN Q,R AXES,
# OR VICE VERSA.  THIS ALLOWS A DEGREE OF ATTITUDE HOLD IN UNCONTROLLED AXES.  DUE TO U,V CONTROL, HOWEVER, Q AND
# R AXES ARE COUPLED AND MUST USE THE SAME CONTROL LAW.
#
# HAND CONTROLLER COMMANDS ARE SCALED BY A LINEAR/QUADRATIC LAW.  FOR THE LM-ALONE, MAXIMUM COMMANDED RATES ARE 20
# AND 4 D/S IN NORMAL AND FINE SCALING; HOWEVER, STICK SENSITIVITY AT ZERO COUNTS (OBTAINED AT A STICK DEFLECTION
# OF 2 DEGREES FROM THE CENTERED POSITION) IS .5 OR .1 D/S PER DEGREE.  NORMAL AND FINE SCALINGS FOR THE CSM-DOCKED
# CASE IS AUTOMATICALLY SET TO 1/10 THE ABOVE VALUES.  SCALING IS DETERMINED IN ROUTINE 3.
#
# ZEROENBL      ENABLES COUNTERS SO THEY CAN BE READ NEXT TIME
# JUSTOUT       FIRST DETECTION OF OUT OF DETENT (BY OURRCBIT)

W('16,3071', 0o00006, 'DETENTCK', 'EXTEND', line=611)
W('16,3072', 0o00031, '', 'READ', 'CHAN31', line=612)
W('16,3073', 0o55443, '', 'TS', 'CH31TEMP', line=613)
W('16,3074', 0o74735, '', 'MASK', 'BIT15', 'CHECK OUT-OF-DETENT BIT.', line=614)
W('16,3075', 0o00006, '', 'EXTEND', line=615)
W('16,3076', 0o13223, '', 'BZF', 'RHCMOVED', 'BRANCH IF OUT OF DETENT.', line=616)
W('16,3077', 0o34740, '', 'CAF', 'OURRCBIT', 'IN DETENT.  CHECK THE RATE COMMAND BIT.', line=617)
W('16,3100', 0o70111, '', 'MASK', 'DAPBOOLS', line=618)
W('16,3101', 0o00006, '', 'EXTEND', line=619)
W('16,3102', 0o13463, '', 'BZF', 'PURGENCY', 'BRANCH IF NOT IN RATE COMMAND LAST PASS.', line=620)

# ................................................................................

W('16,3103', 0o34743, '', 'CA', 'BIT9', 'JUST IN DETENT??', line=624)
W('16,3104', 0o71273, '', 'MASK', 'RCSFLAGS', line=625)
W('16,3105', 0o00006, '', 'EXTEND', line=626)
W('16,3106', 0o13120, '', 'BZF', 'RUTH', line=627)
W('16,3107', 0o34737, '', 'CAF', 'BIT13', 'CHECK FOR ATTITUDE HOLD.', line=628)
W('16,3110', 0o00006, '', 'EXTEND', line=629)
W('16,3111', 0o02031, '', 'RAND', 'CHAN31', line=630)
W('16,3112', 0o00006, '', 'EXTEND', line=631)
W('16,3113', 0o13220, '', 'BZF', 'RATEDAMP', 'BRANCH IF IN ATTITUDE HOLD.', line=632)

W('16,3114', 0o45014, '', 'CS', 'BITS9,11', 'IN AUTO.', line=634)
W('16,3115', 0o71273, '', 'MASK', 'RCSFLAGS', '(X-AXIS OVERRIDE)', line=635)
W('16,3116', 0o55273, '', 'TS', 'RCSFLAGS', 'ZERO ORBIT (BIT 11) AND JUST-IN BIT (9).', line=636)
W('16,3117', 0o13220, '', 'TCF', 'RATEDAMP', line=637)

W('16,3120', 0o31273, 'RUTH', 'CA', 'RCSFLAGS', line=639)
W('16,3121', 0o74742, '', 'MASK', 'PBIT', 'IN ATTITUDE HOLD.', line=640)
W('16,3122', 0o00006, '', 'EXTEND', line=641)
W('16,3123', 0o13125, '', 'BZF', '+2', 'BRANCH IF P-RATE DAMPING IS FINISHED.', line=642)
W('16,3124', 0o13220, '', 'TCF', 'RATEDAMP', line=643)

# Page 1433
W('16,3125', 0o31273, '', 'CA', 'RCSFLAGS', line=646)
W('16,3126', 0o74741, '', 'MASK', 'QRBIT', line=647)
W('16,3127', 0o00006, '', 'EXTEND', line=648)
W('16,3130', 0o13136, '', 'BZF', 'RATEDONE', 'BRANCH IF Q,R RATE DAMPING IS FINISHED.', line=649)
W('16,3131', 0o13220, '', 'TCF', 'RATEDAMP', line=650)

# ============================================

W('16,3132', 0o00001, '1/10SEC', 'OCT', '1', kind='data', line=654)
W('16,3133', 0o00050, '40CYC', 'OCT', '50', kind='data', line=655)
W('16,3134', 0o74777, 'PQRBIT', 'OCT', '74777', kind='data', line=656)
S('BITS9,11', 'equals', 0o5014, line=657)
W('16,3135', 0o00056, 'LINRATP', 'DEC', '46', kind='data', line=658)

# ============================================

W('16,3136', 0o44740, 'RATEDONE', 'CS', 'OURRCBIT', 'MANUAL COMMAND AND DAMPING COMPLETED IN', line=662)
W('16,3137', 0o00004, '', 'INHINT', '', 'ALL AXES.', line=663)
W('16,3140', 0o70111, '', 'MASK', 'DAPBOOLS', line=664)
W('16,3141', 0o54111, '', 'TS', 'DAPBOOLS', line=665)

# READ CDUS INTO CDU DESIRED REGISTERS

W('16,3142', 0o34737, '', 'CAF', 'BIT13', line=669)
W('16,3143', 0o00006, '', 'EXTEND', line=670)
W('16,3144', 0o02031, '', 'RAND', 'CHAN31', line=671)
W('16,3145', 0o00006, '', 'EXTEND', line=672)
W('16,3146', 0o13152, '', 'BZF', '+4', line=673)
W('16,3147', 0o30032, '', 'CA', 'CDUX', '(X-AXIS OVERRIDE)', line=674)
W('16,3150', 0o55635, '', 'TS', 'CDUXD', line=675)
W('16,3151', 0o03154, '', 'TC', '+3', line=676)
W('16,3152', 0o04674, '', 'TC', 'IBNKCALL', line=677)
W('16,3153', 0o40153, '', 'FCADR', 'ZATTEROR', kind='data', line=678)
W('16,3154', 0o00003, '', 'RELINT', line=679)
W('16,3155', 0o13463, '', 'TCF', 'PURGENCY', line=680)

W('16,3156', 0o55464, '', 'TS', 'PERROR', line=682)
W('16,3157', 0o34740, 'JUSTOUT', 'CA', 'OURRCBIT', 'INITIALIZATION -- FIRST MANUAL PASS.', line=683)
W('16,3160', 0o26111, '', 'ADS', 'DAPBOOLS', line=684)
W('16,3161', 0o34755, '', 'CA', 'ZERO', line=685)
W('16,3162', 0o55446, '', 'TS', 'DXERROR', line=686)
W('16,3163', 0o55447, '', 'TS', 'DXERROR +1', line=687)
W('16,3164', 0o55450, '', 'TS', 'DYERROR', line=688)
W('16,3165', 0o55451, '', 'TS', 'DYERROR +1', line=689)
W('16,3166', 0o55452, '', 'TS', 'DZERROR', line=690)
W('16,3167', 0o55453, '', 'TS', 'DZERROR +1', line=691)
W('16,3170', 0o55454, '', 'TS', 'PLAST', line=692)
W('16,3171', 0o55455, '', 'TS', 'QLAST', line=693)
W('16,3172', 0o55456, '', 'TS', 'RLAST', line=694)
W('16,3173', 0o54042, '', 'TS', 'Q-RHCCTR', line=695)
W('16,3174', 0o54044, '', 'TS', 'R-RHCCTR', line=696)
W('16,3175', 0o33134, '', 'CA', 'PQRBIT', line=697)
W('16,3176', 0o71273, '', 'MASK', 'RCSFLAGS', line=698)
W('16,3177', 0o55273, '', 'TS', 'RCSFLAGS', 'BITS 10 AND 11 OF RCSFLAGS ARE 0.', line=699)
# Page 1434
W('16,3200', 0o41273, '', 'CS', 'RCSFLAGS', "SET 'JUST-IN' BIT TO 1.", line=701)
W('16,3201', 0o74743, '', 'MASK', 'BIT9', line=702)
W('16,3202', 0o27273, '', 'ADS', 'RCSFLAGS', line=703)
W('16,3203', 0o03205, '', 'TC', 'ZEROENBL', line=704)
W('16,3204', 0o13442, '', 'TCF', 'JETSOFF', line=705)
W('16,3205', 0o22044, 'ZEROENBL', 'LXCH', 'R-RHCCTR', line=706)
W('16,3206', 0o30042, '', 'CA', 'Q-RHCCTR', line=707)
W('16,3207', 0o53463, '', 'DXCH', 'SAVEHAND', line=708)
W('16,3210', 0o34755, '', 'CA', 'ZERO', line=709)
W('16,3211', 0o54043, '', 'TS', 'P-RHCCTR', line=710)
W('16,3212', 0o54042, '', 'TS', 'Q-RHCCTR', line=711)
W('16,3213', 0o54044, '', 'TS', 'R-RHCCTR', line=712)
W('16,3214', 0o33617, '', 'CA', 'BITS8,9', line=713)
W('16,3215', 0o00006, '', 'EXTEND', line=714)
W('16,3216', 0o05013, '', 'WOR', 'CHAN13', 'COUNTERS ZEROED AND ENABLED', line=715)
W('16,3217', 0o00002, '', 'TC', 'Q', line=716)
W('16,3220', 0o34755, 'RATEDAMP', 'CA', 'ZERO', line=717)
W('16,3221', 0o54043, '', 'TS', 'P-RHCCTR', line=718)
W('16,3222', 0o13227, '', 'TCF', 'RATERROR', line=719)

W('16,3223', 0o34740, 'RHCMOVED', 'CA', 'OURRCBIT', 'P CONTROL', line=721)
W('16,3224', 0o70111, '', 'MASK', 'DAPBOOLS', line=722)
W('16,3225', 0o00006, '', 'EXTEND', line=723)
W('16,3226', 0o13156, '', 'BZF', 'JUSTOUT -1', line=724)
W('16,3227', 0o30032, 'RATERROR', 'CA', 'CDUX', 'FINDCDUW REQUIRES THAT CDUXD=CDUX DURING', line=725)
W('16,3230', 0o55635, '', 'TS', 'CDUXD', 'X-AXIS OVERRIDE', line=726)
W('16,3231', 0o10043, '', 'CCS', 'P-RHCCTR', line=727)
W('16,3232', 0o13235, '', 'TCF', '+3', line=728)
W('16,3233', 0o13235, '', 'TCF', '+2', line=729)
W('16,3234', 0o13235, '', 'TCF', '+1', line=730)
W('16,3235', 0o60000, '', 'DOUBLE', '', 'LINEAR/QUADRATIC CONTROLLER SCALING', line=731)
W('16,3236', 0o60000, '', 'DOUBLE', '', '(SEE EXPLANATION OF Q,R-AXES RCS', line=732)
W('16,3237', 0o63135, '', 'AD', 'LINRATP', 'AUTOPILOT)', line=733)
W('16,3240', 0o00006, '', 'EXTEND', line=734)
W('16,3241', 0o70043, '', 'MP', 'P-RHCCTR', line=735)
W('16,3242', 0o30001, '', 'CA', 'L', line=736)
W('16,3243', 0o00006, '', 'EXTEND', line=737)
W('16,3244', 0o71444, '', 'MP', 'STIKSENS', line=738)
W('16,3245', 0o57454, '', 'XCH', 'PLAST', line=739)
W('16,3246', 0o40000, '', 'COM', line=740)
W('16,3247', 0o61454, '', 'AD', 'PLAST', line=741)
W('16,3250', 0o55737, '', 'TS', 'DAPTEMP1', line=742)
W('16,3251', 0o03205, '', 'TC', 'ZEROENBL', 'INTERVAL.  ZERO AND ENABLE ACA COUNTERS.', line=743)
W('16,3252', 0o41454, '', 'CS', 'PLAST', line=744)
W('16,3253', 0o61421, '', 'AD', 'OMEGAP', line=745)
W('16,3254', 0o55427, '', 'TS', 'EDOTP', line=746)
W('16,3255', 0o11737, '', 'CCS', 'DAPTEMP1', 'IF P COMMAND CHANGE EXCEEDS BREAKOUT', line=747)
W('16,3256', 0o13261, '', 'TCF', '+3', 'LEVEL, GO TO DIRECT RATE CONTROL.  IF NOT', line=748)
W('16,3257', 0o13267, '', 'TCF', '+8D', 'CHECK FOR DIRECT RATE CONTROL LAST TIME.', line=749)
W('16,3260', 0o13261, '', 'TCF', '+1', line=750)
# Page 1435
W('16,3261', 0o61476, '', 'AD', '-RATEDB', line=752)
W('16,3262', 0o00006, '', 'EXTEND', line=753)
W('16,3263', 0o63267, '', 'BZMF', '+4', line=754)
W('16,3264', 0o33133, '', 'CA', '40CYC', line=755)
W('16,3265', 0o55445, '', 'TS', 'TCP', line=756)
W('16,3266', 0o03300, '', 'TC', 'PEGI', line=757)
W('16,3267', 0o31273, '', 'CA', 'RCSFLAGS', 'CHECK FOR DIRECT RATE COMMAND LAST TIME.', line=758)
W('16,3270', 0o74742, '', 'MASK', 'PBIT', line=759)
W('16,3271', 0o00006, '', 'EXTEND', line=760)
W('16,3272', 0o13274, '', 'BZF', '+2', line=761)
W('16,3273', 0o03300, '', 'TC', 'PEGI', 'TO PURE RATE COMMAND', line=762)
W('16,3274', 0o31446, '', 'CA', 'DXERROR', 'PSEUDO-AUTO CONTROL.', line=763)
W('16,3275', 0o55752, '', 'TS', 'E', 'X-ATTITUDE ERROR (SP)', line=764)
W('16,3276', 0o55464, '', 'TS', 'PERROR', 'LOAD P-AXIS ERROR FOR MODE1 FDAI DISPLAY', line=765)
W('16,3277', 0o03467, '', 'TC', 'PURGENCY +4', line=766)
W('16,3300', 0o30032, 'PEGI', 'CA', 'CDUX', 'DIRECT RATE CONTROL.', line=767)
W('16,3301', 0o55635, '', 'TS', 'CDUXD', line=768)
W('16,3302', 0o34755, '', 'CA', 'ZERO', line=769)
W('16,3303', 0o55446, '', 'TS', 'DXERROR', line=770)
W('16,3304', 0o55447, '', 'TS', 'DXERROR +1', line=771)
W('16,3305', 0o55464, '', 'TS', 'PERROR', 'ZERO P-AXIS ERROR FOR MODE1 FDAI DISPLAY', line=772)
W('16,3306', 0o11427, '', 'CCS', 'EDOTP', line=773)
W('16,3307', 0o03312, '', 'TC', '+3', line=774)
W('16,3310', 0o03312, '', 'TC', '+2', line=775)
W('16,3311', 0o03312, '', 'TC', '+1', line=776)
W('16,3312', 0o55737, '', 'TS', 'ABSEDOTP', line=777)
W('16,3313', 0o61476, '', 'AD', 'TARGETDB', line=778)
W('16,3314', 0o00006, '', 'EXTEND', '', 'IF RATE ERROR IS LESS THAN DEADBANK,', line=779)
W('16,3315', 0o63325, '', 'BZMF', 'LAST', 'FIRE, AN SWITCH TO PSEUDO-AUTO.', line=780)
W('16,3316', 0o31445, '', 'CA', 'TCP', line=781)
W('16,3317', 0o00006, '', 'EXTEND', '', 'IF TIME IN RATE COMMAND EXCEEDS 4 SEC.', line=782)
W('16,3320', 0o63325, '', 'BZMF', 'LAST', line=783)
W('16,3321', 0o41273, '', 'CS', 'RCSFLAGS', line=784)
W('16,3322', 0o74742, '', 'MASK', 'PBIT', line=785)
W('16,3323', 0o27273, '', 'ADS', 'RCSFLAGS', 'BIT 10 IS 1.', line=786)
W('16,3324', 0o13330, '', 'TCF', '+4', line=787)
W('16,3325', 0o44742, 'LAST', 'CS', 'PBIT', line=788)
W('16,3326', 0o71273, '', 'MASK', 'RCSFLAGS', line=789)
W('16,3327', 0o55273, '', 'TS', 'RCSFLAGS', 'BIT 10 IS 0.', line=790)
W('16,3330', 0o41427, '', 'CS', 'EDOTP', line=791)
W('16,3331', 0o00006, '', 'EXTEND', line=792)
W('16,3332', 0o71551, '', 'MP', '1/ANETP', '1/2JTACC SCALED AT 2EXP(7)/PI', line=793)
W('16,3333', 0o20001, '', 'DAS', 'A', line=794)
W('16,3334', 0o02310, '', 'TC', 'OVERSUB', line=795)
W('16,3335', 0o00006, '', 'EXTEND', line=796)
W('16,3336', 0o77716, '', 'MP', '25/32', 'A CONTAINS TJET SCALED AT 2EXP(4)(16/25)', line=797)
W('16,3337', 0o55524, '', 'TS', 'TJP', '4.JET TIME', line=798)
W('16,3340', 0o31737, '', 'CA', 'ABSEDOTP', line=799)
W('16,3341', 0o61475, '', 'AD', '-2JETLIM', 'COMPARING DELTA RATE WITH 2 JET LIMIT', line=800)
W('16,3342', 0o00006, '', 'EXTEND', line=801)
# Page 1436
W('16,3343', 0o63346, '', 'BZMF', '+3', line=803)

W('16,3344', 0o36242, '', 'CA', 'SIX', line=805)
W('16,3345', 0o13355, '', 'TCF', '+8D', line=806)
W('16,3346', 0o31524, '', 'CA', 'TJP', line=807)
W('16,3347', 0o27524, '', 'ADS', 'TJP', line=808)

# GOES TO PJETSLEC FOR TWO JETS
# P-JET-SELECTION-ROUTINE (ROTATION)
#
# INPUT:        NUMBERT         4,5,6 FOR WHICH PAIR OR 4 JETS
# TJP             + FOR +P ROTATION
#
# OUTPUT:       CHANNEL 6
# PJUMPADR        FOR P-AXIS SKIP
# (JTLST CALL)    (SMALL TJP)
#
# ORDER OF POLICIES TRIED IN CASE OF FAILURE.
# +P      -P
# 7,15    8,16
# 4,12    3,11
# 4,7     8,11
# 7,12    11,16
# 12,15   3,16
# 4,15    3,8
# ALARM   ALARM

W('16,3350', 0o34747, '', 'CA', 'AORBSYST', line=830)
W('16,3351', 0o70111, '', 'MASK', 'DAPBOOLS', line=831)
W('16,3352', 0o10000, '', 'CCS', 'A', line=832)
W('16,3353', 0o34753, '', 'CA', 'ONE', line=833)
W('16,3354', 0o64751, '', 'AD', 'FOUR', line=834)
W('16,3355', 0o55743, '', 'TS', 'NUMBERT', line=835)
W('16,3356', 0o34753, 'PJETSLEC', 'CA', 'ONE', line=836)
W('16,3357', 0o54001, '', 'TS', 'L', line=837)
W('16,3360', 0o11524, '', 'CCS', 'TJP', line=838)
W('16,3361', 0o13366, '', 'TCF', '+5', line=839)
W('16,3362', 0o13442, '', 'TCF', 'JETSOFF', line=840)
W('16,3363', 0o13365, '', 'TCF', '+2', line=841)
W('16,3364', 0o13442, '', 'TCF', 'JETSOFF', line=842)
W('16,3365', 0o22007, '', 'ZL', line=843)
W('16,3366', 0o64753, '', 'AD', 'ONE', line=844)
W('16,3367', 0o55737, '', 'TS', 'ABSTJ', line=845)
W('16,3370', 0o23744, '', 'LXCH', 'ROTINDEX', line=846)
W('16,3371', 0o03531, '', 'TC', 'SELECTP', line=847)
W('16,3372', 0o46242, '', 'CS', 'SIX', line=848)
W('16,3373', 0o61743, '', 'AD', 'NUMBERT', line=849)
W('16,3374', 0o00006, '', 'EXTEND', line=850)
W('16,3375', 0o13377, '', 'BZF', '+2', line=851)

W('16,3376', 0o44752, '', 'CS', 'TWO', line=853)

# Page 1437
W('16,3377', 0o64751, '', 'AD', 'FOUR', line=856)
W('16,3400', 0o55521, '', 'TS', 'NO.PJETS', line=857)
W('16,3401', 0o31741, '', 'CA', 'POLYTEMP', line=858)
W('16,3402', 0o05754, '', 'TC', 'WRITEP', line=859)
W('16,3403', 0o41737, '', 'CS', 'ABSTJ', line=860)
W('16,3404', 0o63612, '', 'AD', '+150MST6', line=861)
W('16,3405', 0o00006, '', 'EXTEND', line=862)
W('16,3406', 0o63624, '', 'BZMF', 'QRAXIS', 'GO TO QRAXIS OR TO GTS.', line=863)

W('16,3407', 0o63572, '', 'AD', '-136MST6', line=865)
W('16,3410', 0o00006, '', 'EXTEND', line=866)
W('16,3411', 0o63416, '', 'BZMF', '+5', line=867)

W('16,3412', 0o27737, '', 'ADS', 'ABSTJ', line=869)
W('16,3413', 0o51744, '', 'INDEX', 'ROTINDEX', line=870)
W('16,3414', 0o33621, '', 'CA', 'MINTIMES', line=871)
W('16,3415', 0o55524, '', 'TS', 'TJP', line=872)

W('16,3416', 0o31737, '', 'CA', 'ABSTJ', line=874)
W('16,3417', 0o22007, '', 'ZL', line=875)
W('16,3420', 0o00004, '', 'INHINT', line=876)
W('16,3421', 0o53471, '', 'DXCH', 'T6FURTHA', line=877)
W('16,3422', 0o04674, '', 'TC', 'IBNKCALL', line=878)
W('16,3423', 0o37114, '', 'CADR', 'JTLST', kind='data', line=879)
W('16,3424', 0o44740, '', 'CS', 'BIT12', line=880)
W('16,3425', 0o71273, '', 'MASK', 'RCSFLAGS', line=881)
W('16,3426', 0o55273, '', 'TS', 'RCSFLAGS', 'BIT 12 SET TO 0.', line=882)
W('16,3427', 0o03431, '', 'TC', 'ALTSYST', line=883)
W('16,3430', 0o13624, '', 'TCF', 'QRAXIS', line=884)

W('16,3431', 0o30111, 'ALTSYST', 'CA', 'DAPBOOLS', 'ALTERNATE P-AXIS JETS', line=886)
W('16,3432', 0o54001, '', 'TS', 'L', line=887)
W('16,3433', 0o34747, '', 'CA', 'AORBSYST', line=888)
W('16,3434', 0o00006, '', 'EXTEND', line=889)
W('16,3435', 0o06001, '', 'RXOR', 'LCHAN', line=890)
W('16,3436', 0o54111, '', 'TS', 'DAPBOOLS', line=891)
W('16,3437', 0o00003, '', 'RELINT', line=892)
W('16,3440', 0o00002, '', 'TC', 'Q', line=893)

W('16,3441', 0o03431, 'DKALT', 'TC', 'ALTSYST', line=895)

W('16,3442', 0o05753, 'JETSOFF', 'TC', 'WRITEP -1', line=897)
W('16,3443', 0o34755, '', 'CA', 'ZERO', line=898)
W('16,3444', 0o55524, '', 'TS', 'TJP', line=899)
W('16,3445', 0o13624, '', 'TCF', 'QRAXIS', line=900)

# (NOTE -- M13 = 1 IDENTICALLY IMPLIES NULL MULTIPLICATION.)

W('16,3446', 0o30033, 'CALCPERR', 'CA', 'CDUY', 'P-ERROR CALCULATION.', line=904)
W('16,3447', 0o00006, '', 'EXTEND', line=905)
W('16,3450', 0o21636, '', 'MSU', 'CDUYD', 'CDU VALUE -- ANGLE DESIRED (Y-AXIS)', line=906)
# Page 1438
W('16,3451', 0o00006, '', 'EXTEND', line=908)
W('16,3452', 0o71414, '', 'MP', 'M11', '(CDUY-CDUYD)M11 SCALED AT PI RADIANS', line=909)
W('16,3453', 0o57752, '', 'XCH', 'E', 'SAVE FIRST TERM (OF TWO)', line=910)
W('16,3454', 0o30032, '', 'CA', 'CDUX', 'THIRD COMPONENT', line=911)
W('16,3455', 0o00006, '', 'EXTEND', line=912)
W('16,3456', 0o21635, '', 'MSU', 'CDUXD', 'CDU VALUE -- ANGLE DESIRED (X-AXIS)', line=913)
# EXTEND
# MP      M13
W('16,3457', 0o61277, '', 'AD', 'DELPEROR', 'KALCMANU INTERFACE ERROR.', line=916)
W('16,3460', 0o27752, '', 'ADS', 'E', 'SAVE SUM OF TERMS.  COULD BE OVERFLOW.', line=917)
W('16,3461', 0o57464, '', 'XCH', 'PERROR', 'SAVE P-ERROR FOR EIGHT-BALL DISPLAY.', line=918)
W('16,3462', 0o00002, '', 'TC', 'Q', 'RETURN TO CALLER', line=919)

# P-AXIS URGENCY FUNCTION CALCULATION.

W('16,3463', 0o03446, 'PURGENCY', 'TC', 'CALCPERR', 'CALCULATE P-AXIS ERRORS.', line=923)
W('16,3464', 0o41643, '', 'CS', 'OMEGAPD', 'THIS CODING IS COMMON TO BOTH LM DAP AND', line=924)
W('16,3465', 0o61421, '', 'AD', 'OMEGAP', 'SPS-BACKUP MODE.', line=925)
W('16,3466', 0o55427, '', 'TS', 'EDOTP', 'EDOTP = OMEGAP - OMEGAPD AT PI/4 RAD/SEC', line=926)

W('16,3467', 0o44753, '', 'CS', 'ONE', line=928)
W('16,3470', 0o55505, '', 'TS', 'AXISCTR', line=929)
W('16,3471', 0o30111, '', 'CA', 'DAPBOOLS', line=930)
W('16,3472', 0o74737, '', 'MASK', 'CSMDOCKD', line=931)
W('16,3473', 0o00006, '', 'EXTEND', line=932)
W('16,3474', 0o13505, '', 'BZF', 'HEADTJET', line=933)
W('16,3475', 0o00004, '', 'INHINT', '', 'IF CSMDOCKD = 1, GOT TO DOCKED RCS LOGIC', line=934)
W('16,3476', 0o04674, '', 'TC', 'IBNKCALL', line=935)
W('16,3477', 0o43727, '', 'CADR', 'SPSRCS', kind='data', line=936)

W('16,3500', 0o31524, '', 'CA', 'TJP', line=938)
W('16,3501', 0o00006, '', 'EXTEND', line=939)
W('16,3502', 0o13441, '', 'BZF', 'DKALT', 'IF TJP = ZERO, CHANGE AORBSYST.', line=940)
W('16,3503', 0o00003, '', 'RELINT', line=941)
W('16,3504', 0o13350, '', 'TCF', 'PJETSLEC -6', 'SELECT AORBSYST AND USE TWO JETS.', line=942)
W('16,3505', 0o34755, 'HEADTJET', 'CA', 'ZERO', line=943)
W('16,3506', 0o55500, '', 'TS', 'SENSETYP', line=944)
W('16,3507', 0o00004, '', 'INHINT', line=945)
W('16,3510', 0o04674, '', 'TC', 'IBNKCALL', line=946)
W('16,3511', 0o37252, '', 'CADR', 'TJETLAW', kind='data', line=947)
W('16,3512', 0o00003, '', 'RELINT', line=948)

W('16,3513', 0o41741, '', 'CS', 'FIREFCT', line=950)
W('16,3514', 0o63530, '', 'AD', '-FOURDEG', line=951)
W('16,3515', 0o00006, '', 'EXTEND', line=952)
W('16,3516', 0o63350, '', 'BZMF', 'PJETSLEC -6', line=953)
W('16,3517', 0o11524, '', 'CCS', 'TJP', line=954)
W('16,3520', 0o13522, '', 'TCF', '+2', line=955)
W('16,3521', 0o13442, '', 'TCF', 'JETSOFF', line=956)
# Page 1439
W('16,3522', 0o63527, '', 'AD', '-160MST6', line=958)
W('16,3523', 0o00006, '', 'EXTEND', line=959)
W('16,3524', 0o63350, '', 'BZMF', 'PJETSLEC -6', line=960)
W('16,3525', 0o36242, '', 'CA', 'SIX', line=961)
W('16,3526', 0o13355, '', 'TCF', 'PJETSLEC -1', line=962)
W('16,3527', 0o77377, '-160MST6', 'DEC', '-256', kind='data', line=963)
W('16,3530', 0o75117, '-FOURDEG', 'DEC', '-.08888', kind='data', line=964)

# Page 1440
# JET POLICY CONSTRUCTION SUBROUTINE
#
# INPUT:        ROTINDEX, NUMBERT
#
# OUTPUT:       POLYTEMP (JET POLICY)
#
# THIS SUBROUTINE SELECT A SUBSET OF THE DESIRED JETS WHICH HAS NO FAILURE

W('16,3531', 0o36242, 'SELECTP', 'CA', 'SIX', line=975)
W('16,3532', 0o55742, '', 'TS', 'TEMPNUM', line=976)
W('16,3533', 0o51743, '', 'INDEX', 'NUMBERT', line=977)
W('16,3534', 0o33563, '', 'CA', 'TYPEP', line=978)
W('16,3535', 0o51744, '', 'INDEX', 'ROTINDEX', line=979)
W('16,3536', 0o73554, '', 'MASK', 'JETSALL', line=980)
W('16,3537', 0o55741, '', 'TS', 'POLYTEMP', line=981)
W('16,3540', 0o71263, '', 'MASK', 'CH6MASK', line=982)
W('16,3541', 0o10000, '', 'CCS', 'A', line=983)
W('16,3542', 0o13544, '', 'TCF', '+2', line=984)
W('16,3543', 0o00002, '', 'TC', 'Q', line=985)
W('16,3544', 0o11742, '', 'CCS', 'TEMPNUM', line=986)
W('16,3545', 0o13551, '', 'TCF', '+4', line=987)
W('16,3546', 0o05567, '', 'TC', 'ALARM', line=988)
W('16,3547', 0o02003, '', 'OCT', '02003', kind='data', line=989)
W('16,3550', 0o13442, '', 'TCF', 'JETSOFF', '********** TCF ALARMJET **********', line=990)
W('16,3551', 0o55743, 'SELECTYZ', 'TS', 'NUMBERT', line=991)
W('16,3552', 0o13532, '', 'TCF', 'SELECTP +1', line=992)
W('16,3553', 0o12773, '', 'TCF', 'ABORTYZ +2', line=993)
W('16,3554', 0o00252, 'JETSALL', 'OCT', '00252', kind='data', line=994)
W('16,3555', 0o00125, '', 'OCT', '00125', '+P', kind='data', line=995)
W('16,3556', 0o00140, '', 'OCT', '00140', '-Y', kind='data', line=996)
W('16,3557', 0o00006, '', 'OCT', '00006', '-Z', kind='data', line=997)
W('16,3560', 0o00220, '', 'OCT', '00220', '+Y', kind='data', line=998)
W('16,3561', 0o00011, '', 'OCT', '00011', '+Z', kind='data', line=999)
W('16,3562', 0o00151, '', 'OCT', '00151', '+V', kind='data', line=1000)
W('16,3563', 0o00146, 'TYPEP', 'OCT', '00146', '-U', kind='data', line=1001)
W('16,3564', 0o00226, '', 'OCT', '00226', '-V', kind='data', line=1002)
W('16,3565', 0o00231, '', 'OCT', '00231', '+U', kind='data', line=1003)
W('16,3566', 0o00151, '', 'OCT', '00151', '+V', kind='data', line=1004)
W('16,3567', 0o00132, '', 'OCT', '00132', '1-3', kind='data', line=1005)
W('16,3570', 0o00245, '', 'OCT', '00245', '2-4', kind='data', line=1006)
W('16,3571', 0o00377, '', 'OCT', '00377', 'ALL', kind='data', line=1007)
S('INDXYZ', 'equals', 0o45572, line=1008)
W('16,3572', 0o77445, '-136MST6', 'DEC', '-218', kind='data', line=1009)
W('16,3573', 0o00004, '', 'DEC', '4', kind='data', line=1010)
W('16,3574', 0o00002, '', 'DEC', '2', kind='data', line=1011)
W('16,3575', 0o07776, '', 'OCT', '07776', kind='data', line=1012)
W('16,3576', 0o00005, '', 'DEC', '5', kind='data', line=1013)
W('16,3577', 0o00011, '', 'DEC', '9', kind='data', line=1014)
W('16,3600', 0o00012, '', 'DEC', '10', kind='data', line=1015)
W('16,3601', 0o07776, '', 'OCT', '07776', kind='data', line=1016)
W('16,3602', 0o00003, '', 'DEC', '3', kind='data', line=1017)
# Page 1441
W('16,3603', 0o00010, '', 'DEC', '8', kind='data', line=1019)
W('16,3604', 0o00007, '', 'DEC', '7', kind='data', line=1020)
W('16,3605', 0o07776, '', 'OCT', '07776', 'THESE INDEXES OF MASK JETSALL WILL', kind='data', line=1021)
W('16,3606', 0o07776, '', 'OCT', '07776', 'CHANGE THE INSTRUCTION AT SELECTP +4', kind='data', line=1022)
W('16,3607', 0o07776, '', 'OCT', '07776', 'TO BE         TC JETSALL -1', kind='data', line=1023)
W('16,3610', 0o07776, '', 'OCT', '07776', 'ONLY USED FOR TRANSLATION FAILURE', kind='data', line=1024)
W('16,3611', 0o07776, '', 'OCT', '07776', kind='data', line=1025)
W('16,3612', 0o00360, '+150MST6', 'DEC', '240', kind='data', line=1026)
W('16,3613', 0o07400, '07400OCT', 'OCT', '07400', kind='data', line=1027)

# T-JET LAW FIXED CONSTANTS

W('16,3614', 0o00266, 'NORMSCL', 'OCT', '266', kind='data', line=1031)
W('16,3615', 0o74631, '-100MS', 'DEC', '-.1', kind='data', line=1032)
W('16,3616', 0o06315, '200MS', 'DEC', '.2', kind='data', line=1033)
S('25/32', 'equals', 0o7716, line=1034)  # (DEC .78125)
W('16,3617', 0o00600, 'BITS8,9', 'OCTAL', '00600', kind='data', line=1035)
W('16,3620', 0o00632, '1/40', 'DEC', '.02500', kind='data', line=1036)
W('16,3621', 0o77751, 'MINTIMES', 'DEC', '-22', kind='data', line=1037)
W('16,3622', 0o00026, '', 'DEC', '22', kind='data', line=1038)
W('16,3623', 0o02734, 'PSKIPADR', 'GENADR', 'SKIPPAXS', kind='data', line=1039)

# GOES TO Q,R-AXES RCS AUTOPILOT

W('16,3624', 0o41645, 'QRAXIS', 'CS', 'OMEGARD', line=1043)
W('16,3625', 0o61423, '', 'AD', 'OMEGAR', line=1044)
W('16,3626', 0o02310, '', 'TC', 'OVERSUB', line=1045)
W('16,3627', 0o55437, '', 'TS', 'EDOTR', line=1046)
W('16,3630', 0o41644, '', 'CS', 'OMEGAQD', line=1047)
W('16,3631', 0o61422, '', 'AD', 'OMEGAQ', line=1048)
W('16,3632', 0o02310, '', 'TC', 'OVERSUB', line=1049)
W('16,3633', 0o55436, '', 'TS', 'EDOTQ', line=1050)
W('16,3634', 0o00006, '', 'EXTEND', line=1051)
W('16,3635', 0o33640, '', 'DCA', 'QERRCALL', line=1052)
W('16,3636', 0o52006, '', 'DTCB', line=1053)

#   EBANK= AOSQ
W('16,3637', 0o02072, 'QERRCALL', '2CADR', 'CALLQERR', kind='data', line=1056)
W('16,3640', 0o36106, kind='data', line=1056)
