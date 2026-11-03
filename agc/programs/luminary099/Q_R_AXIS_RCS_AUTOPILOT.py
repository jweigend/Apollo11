"""Q_R-AXIS_RCS_AUTOPILOT.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/Q_R-AXIS_RCS_AUTOPILOT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1442-1459 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('Q_R_AXIS_RCS_AUTOPILOT', 'Q_R-AXIS_RCS_AUTOPILOT.agc', 'Luminary099', pages='1442-1459')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     Q_R-AXIS_RCS_AUTOPILOT.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1442-1459
# Mod history:  2009-05-27 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2009-06-07 RSB  Corrected "DEC 96.0" to "DEC 96", since
# the former is not compatible with yaYUL.
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

# Page 1442
#   BANK 17
#   SETLOC DAPS2
#   BANK

#   EBANK= CDUXD

#   COUNT* $$/DAPQR

W('17,2072', 0o34737, 'CALLQERR', 'CA', 'BIT13', 'CALCULATE Q,R ERRORS UNLESS THESE AXES', line=40)
W('17,2073', 0o00006, '', 'EXTEND', '', 'ARE IN MANUAL RATE COMMAND.', line=41)
W('17,2074', 0o02031, '', 'RAND', 'CHAN31', line=42)
W('17,2075', 0o10000, '', 'CCS', 'A', line=43)
W('17,2076', 0o12103, '', 'TCF', '+5', 'IN AUTO COMPUTE Q,R ERRORS', line=44)
W('17,2077', 0o40111, '', 'CS', 'DAPBOOLS', 'IN MANUAL RATE COMMAND?', line=45)
W('17,2100', 0o74740, '', 'MASK', 'OURRCBIT', line=46)
W('17,2101', 0o00006, '', 'EXTEND', line=47)
W('17,2102', 0o12104, '', 'BZF', 'Q,RORGTS', 'IF SO BYPASS CALCULATION OF ERRORS.', line=48)
W('17,2103', 0o02626, '', 'TC', 'QERRCALC', line=49)

W('17,2104', 0o11631, 'Q,RORGTS', 'CCS', 'COTROLER', 'CHOOSE CONTROL SYSTEM FOR THIS DAP PASS:', line=51)
W('17,2105', 0o12607, '', 'TCF', 'GOTOGTS', '      GTS (ALTERNATES WITH RCS WHEN DOCKED)', line=52)
W('17,2106', 0o12574, '', 'TCF', 'TRYGTS', '      GTS IF ALLOWED, OTHERWISE RCS', line=53)
W('17,2107', 0o34755, 'RCS', 'CAF', 'ZERO', '      RCS (TRYGTS MAY BRANCH TO HERE)', line=54)
W('17,2110', 0o55631, '', 'TS', 'COTROLER', line=55)

W('17,2111', 0o53437, '', 'DXCH', 'EDOTQ', line=57)
W('17,2112', 0o03146, '', 'TC', 'ROT-TOUV', line=58)
W('17,2113', 0o53427, '', 'DXCH', 'OMEGAU', line=59)

# X - TRANSLATION
#
# INPUT:        BITS 7,8 OF CH31 (TRANSLATION CONTROLLER)
# ULLAGER
# APSFLAG, DRIFTBIT
# ACC40R2X, ACRBTRAN
#
# OUTPUT:       NEXTU, NEXTV    CODES OF TRANSLATION FOR AFTER ROTATION
# SENSETYP        TELL ROTATION DIRECTION AND DESIRE
#
# X-TRANS POLICIES ARE EITHER 4 JETS OR A DIAGONAL PAIR.  IN 2-JET TRANSLATION THE SYSTEM IS SPECIFIED.  A FAILURE
# WILL OVERRIDE THIS SPECIFICATION.  AN ALARM RESULTS WHEN NO POLICY IS AVAILABLE BECAUSE OF FAILURES.

W('17,2114', 0o34745, 'SENSEGET', 'CA', 'BIT7', 'INPUT BITS OVERRIDE THE INTERNAL BITS', line=74)
W('17,2115', 0o00006, '', 'EXTEND', '', 'SENSETYP WILL NOT OPPOSE ANYTRANS', line=75)
W('17,2116', 0o02031, '', 'RAND', 'CHAN31', line=76)
W('17,2117', 0o00006, '', 'EXTEND', line=77)
W('17,2120', 0o12146, '', 'BZF', '+X0RULGE', line=78)
# Page 1443
W('17,2121', 0o34744, '', 'CA', 'BIT8', line=80)
W('17,2122', 0o00006, '', 'EXTEND', line=81)
W('17,2123', 0o02031, '', 'RAND', 'CHAN31', line=82)
W('17,2124', 0o00006, '', 'EXTEND', line=83)
W('17,2125', 0o12147, '', 'BZF', '-XTRANS', line=84)

W('17,2126', 0o34746, '', 'CA', 'ULLAGER', line=86)
W('17,2127', 0o70111, '', 'MASK', 'DAPBOOLS', line=87)
W('17,2130', 0o10000, '', 'CCS', 'A', line=88)
W('17,2131', 0o12146, '', 'TCF', '+X0RULGE', line=89)

W('17,2132', 0o55473, '', 'TS', 'NEXTU', 'STORE NULL TRANSLATION POLICIES', line=91)
W('17,2133', 0o55474, '', 'TS', 'NEXTV', line=92)
W('17,2134', 0o40111, '', 'CS', 'DAPBOOLS', 'BURNING OR DRIFTING?', line=93)
W('17,2135', 0o74744, '', 'MASK', 'DRIFTBIT', line=94)
W('17,2136', 0o00006, '', 'EXTEND', line=95)
W('17,2137', 0o12144, '', 'BZF', 'TSENSE', line=96)
W('17,2140', 0o30106, '', 'CA', 'FLGWRD10', 'DPS (INCLUDING DOCKED) OR APS?', line=97)
W('17,2141', 0o74737, '', 'MASK', 'APSFLBIT', line=98)
W('17,2142', 0o10000, '', 'CCS', 'A', line=99)
W('17,2143', 0o34752, '', 'CAF', 'TWO', 'FAVOR +X JETS DURING AN APS BURN.', line=100)
W('17,2144', 0o55500, 'TSENSE', 'TS', 'SENSETYP', line=101)
W('17,2145', 0o12200, '', 'TCF', 'QRCONTRL', line=102)

W('17,2146', 0o34753, '+X0RULGE', 'CAF', 'ONE', line=104)
W('17,2147', 0o64751, '-XTRANS', 'AD', 'FOUR', line=105)
W('17,2150', 0o55744, '', 'TS', 'ROTINDEX', line=106)
W('17,2151', 0o67745, '', 'AD', 'NEG3', line=107)
W('17,2152', 0o55500, '', 'TS', 'SENSETYP', 'FAVOR APPROPRIATE JETS DURING TRANS.', line=108)
W('17,2153', 0o30111, '', 'CA', 'DAPBOOLS', line=109)
W('17,2154', 0o74741, '', 'MASK', 'ACC4OR2X', line=110)
W('17,2155', 0o10000, '', 'CCS', 'A', line=111)
W('17,2156', 0o12321, '', 'TCF', 'TRANS4', line=112)

W('17,2157', 0o30111, '', 'CA', 'DAPBOOLS', line=114)
W('17,2160', 0o74742, '', 'MASK', 'AORBTRAN', line=115)
W('17,2161', 0o10000, '', 'CCS', 'A', line=116)
W('17,2162', 0o34753, '', 'CA', 'ONE', 'THREE FOR B', line=117)
W('17,2163', 0o64752, '', 'AD', 'TWO', 'TWO FOR A SYSTEM 2 JET X TRANS', line=118)
W('17,2164', 0o55743, 'TSNUMBRT', 'TS', 'NUMBERT', line=119)

W('17,2165', 0o03173, '', 'TC', 'SELCTSUB', line=121)

W('17,2166', 0o11741, '', 'CCS', 'POLYTEMP', line=123)
W('17,2167', 0o12172, '', 'TCF', '+3', line=124)
W('17,2170', 0o05567, '', 'TC', 'ALARM', line=125)
W('17,2171', 0o02002, '', 'OCT', '02002', kind='data', line=126)
W('17,2172', 0o35774, '', 'CA', '00314OCT', line=127)
W('17,2173', 0o71741, '', 'MASK', 'POLYTEMP', line=128)
W('17,2174', 0o55473, 'TSNEXTS', 'TS', 'NEXTU', line=129)
# Page 1444
W('17,2175', 0o45774, '', 'CS', '00314OCT', line=131)
W('17,2176', 0o71741, '', 'MASK', 'POLYTEMP', line=132)
W('17,2177', 0o55474, '', 'TS', 'NEXTV', line=133)

# Q,R-AXES RCS CONTROL MODE SELECTION
# SWITCHES        INDICATION WHEN SET
# BIT13/CHAN31    AUTO, GO TO ATTSTEER
# PULSES          MINIMUM IMPULSE MODE
# (OTHERWISE)     RATE COMMAND/ATTITUDE HOLD MODE

W('17,2200', 0o34737, 'QRCONTRL', 'CA', 'BIT13', 'CHECK MODE SELECT SWITCH.', line=141)
W('17,2201', 0o00006, '', 'EXTEND', line=142)
W('17,2202', 0o02031, '', 'RAND', 'CHAN31', 'BITS INVERTED', line=143)
W('17,2203', 0o10000, '', 'CCS', 'A', line=144)
W('17,2204', 0o12661, '', 'TCF', 'ATTSTEER', line=145)
W('17,2205', 0o34735, 'CHKBIT10', 'CAF', 'PULSES', 'PULSES = 1 FOR MIN IMP USE OF RHC', line=146)
W('17,2206', 0o70111, '', 'MASK', 'DAPBOOLS', line=147)
W('17,2207', 0o00006, '', 'EXTEND', line=148)
W('17,2210', 0o12323, '', 'BZF', 'CHEKSTIK', 'IN ATT-HOLD/RATE-COMMAND IF BIT10=0', line=149)

# MINIMUM IMPULSE MODE

W('17,2211', 0o00004, '', 'INHINT', line=153)
W('17,2212', 0o04674, '', 'TC', 'IBNKCALL', line=154)
W('17,2213', 0o40153, '', 'CADR', 'ZATTEROR', kind='data', line=155)
W('17,2214', 0o34755, '', 'CA', 'ZERO', line=156)
W('17,2215', 0o55450, '', 'TS', 'QERROR', line=157)
W('17,2216', 0o55452, '', 'TS', 'RERROR', 'FOR DISPLAYS', line=158)
W('17,2217', 0o00003, '', 'RELINT', line=159)

W('17,2220', 0o00006, '', 'EXTEND', line=161)
W('17,2221', 0o00031, '', 'READ', 'CHAN31', line=162)
W('17,2222', 0o55737, '', 'TS', 'TEMP31', 'IS EQUAL TO DAPTEMP1', line=163)
W('17,2223', 0o11461, '', 'CCS', 'OLDQRMIN', line=164)
W('17,2224', 0o12246, '', 'TCF', 'CHECKIN', line=165)

W('17,2225', 0o31737, 'FIREQR', 'CA', 'TEMP31', line=167)
W('17,2226', 0o74753, '', 'MASK', 'BIT1', line=168)
W('17,2227', 0o00006, '', 'EXTEND', line=169)
W('17,2230', 0o12252, '', 'BZF', '+QMIN', line=170)

W('17,2231', 0o31737, '', 'CA', 'TEMP31', line=172)
W('17,2232', 0o74752, '', 'MASK', 'BIT2', line=173)
W('17,2233', 0o00006, '', 'EXTEND', line=174)
W('17,2234', 0o12256, '', 'BZF', '-QMIN', line=175)

W('17,2235', 0o31737, '', 'CA', 'TEMP31', line=177)
W('17,2236', 0o74747, '', 'MASK', 'BIT5', line=178)
# Page 1445
W('17,2237', 0o00006, '', 'EXTEND', line=180)
W('17,2240', 0o12262, '', 'BZF', '+RMIN', line=181)

W('17,2241', 0o31737, '', 'CA', 'TEMP31', line=183)
W('17,2242', 0o74746, '', 'MASK', 'BIT6', line=184)
W('17,2243', 0o00006, '', 'EXTEND', line=185)
W('17,2244', 0o12264, '', 'BZF', '-RMIN', line=186)

W('17,2245', 0o13063, '', 'TCF', 'XTRANS', line=188)

W('17,2246', 0o41737, 'CHECKIN', 'CS', 'TEMP31', line=190)
W('17,2247', 0o72320, '', 'MASK', 'OCT63', line=191)
W('17,2250', 0o55461, '', 'TS', 'OLDQRMIN', line=192)
W('17,2251', 0o13063, '', 'TCF', 'XTRANS', line=193)

W('17,2252', 0o33107, '+QMIN', 'CA', '14MS', line=195)
W('17,2253', 0o55525, '', 'TS', 'TJU', line=196)
W('17,2254', 0o43107, '', 'CS', '14MS', line=197)
W('17,2255', 0o12266, '', 'TCF', 'MINQR', line=198)
W('17,2256', 0o43107, '-QMIN', 'CS', '14MS', line=199)
W('17,2257', 0o55525, '', 'TS', 'TJU', line=200)
W('17,2260', 0o33107, '', 'CA', '14MS', line=201)
W('17,2261', 0o12266, '', 'TCF', 'MINQR', line=202)
W('17,2262', 0o33107, '+RMIN', 'CA', '14MS', line=203)
W('17,2263', 0o12265, '', 'TCF', '+2', line=204)
W('17,2264', 0o43107, '-RMIN', 'CS', '14MS', line=205)
W('17,2265', 0o55525, '', 'TS', 'TJU', line=206)
W('17,2266', 0o55526, 'MINQR', 'TS', 'TJV', line=207)
W('17,2267', 0o32317, '', 'CA', 'MINADR', line=208)
W('17,2270', 0o55477, '', 'TS', 'RETJADR', line=209)
W('17,2271', 0o34753, '', 'CA', 'ONE', line=210)
W('17,2272', 0o55461, '', 'TS', 'OLDQRMIN', line=211)
W('17,2273', 0o55505, 'MINRTN', 'TS', 'AXISCTR', line=212)
W('17,2274', 0o30111, '', 'CA', 'DAPBOOLS', line=213)
W('17,2275', 0o74737, '', 'MASK', 'CSMDOCKD', line=214)
W('17,2276', 0o00006, '', 'EXTEND', line=215)
W('17,2277', 0o12307, '', 'BZF', 'MIMRET', line=216)
W('17,2300', 0o51505, '', 'INDEX', 'AXISCTR', 'IF DOCKED, USE 60MS MINIMUM IMPULSE', line=217)
W('17,2301', 0o11525, '', 'CCS', 'TJU', line=218)
W('17,2302', 0o32316, '', 'CA', '60MS', line=219)
W('17,2303', 0o12305, '', 'TCF', '+2', line=220)
W('17,2304', 0o42316, '', 'CS', '60MS', line=221)
W('17,2305', 0o51505, '', 'INDEX', 'AXISCTR', line=222)
W('17,2306', 0o55525, '', 'TS', 'TJU', line=223)
W('17,2307', 0o30111, 'MIMRET', 'CA', 'DAPBOOLS', line=224)
W('17,2310', 0o74742, '', 'MASK', 'AORBTRAN', line=225)
W('17,2311', 0o10000, '', 'CCS', 'A', line=226)
W('17,2312', 0o34753, '', 'CA', 'ONE', line=227)
W('17,2313', 0o64752, '', 'AD', 'TWO', line=228)
W('17,2314', 0o55743, '', 'TS', 'NUMBERT', line=229)
# Page 1446
W('17,2315', 0o12727, '', 'TCF', 'AFTERTJ', line=231)

W('17,2316', 0o00140, '60MS', 'DEC', '96', 'RSB 2009 -- was 96.0.', kind='data', line=233)
W('17,2317', 0o02273, 'MINADR', 'GENADR', 'MINRTN', kind='data', line=234)
W('17,2320', 0o00063, 'OCT63', 'OCT', '63', kind='data', line=235)
S('14MS', 'equals', 0o47107, line=236)

W('17,2321', 0o34751, 'TRANS4', 'CA', 'FOUR', line=238)
W('17,2322', 0o12164, '', 'TCF', 'TSNUMBRT', line=239)

# RATE COMMAND MODE:
#
# DESCRIPTION (SAME AS P-AXIS)

W('17,2323', 0o55633, 'CHEKSTIK', 'TS', 'INGTS', 'NOT IN GTS WHEN IN ATT HOLD', line=245)
W('17,2324', 0o44753, '', 'CS', 'ONE', '1/ACCS WILL DO THE NULLING DRIVES', line=246)
W('17,2325', 0o55631, '', 'TS', 'COTROLER', 'COME BACK TO RCS NEXT TIME', line=247)
W('17,2326', 0o34735, '', 'CA', 'BIT15', line=248)
W('17,2327', 0o71443, '', 'MASK', 'CH31TEMP', line=249)
W('17,2330', 0o00006, '', 'EXTEND', line=250)
W('17,2331', 0o12350, '', 'BZF', 'RHCACTIV', 'BRANCH IF OUT OF DETENT.', line=251)
W('17,2332', 0o34740, '', 'CA', 'OURRCBIT', '***********', line=252)
W('17,2333', 0o70111, '', 'MASK', 'DAPBOOLS', '*IN DETENT*   CHECK FOR MANUAL CONTROL', line=253)
W('17,2334', 0o00006, '', 'EXTEND', '', '***********   LAST TIME.', line=254)
W('17,2335', 0o12661, '', 'BZF', 'STILLRCS', line=255)
W('17,2336', 0o44743, '', 'CS', 'BIT9', line=256)
W('17,2337', 0o71273, '', 'MASK', 'RCSFLAGS', line=257)
W('17,2340', 0o55273, '', 'TS', 'RCSFLAGS', 'BIT 9 IS 0.', line=258)
W('17,2341', 0o12345, '', 'TCF', 'DAMPING', line=259)
W('17,2342', 0o00050, '40CYCL', 'OCT', '50', kind='data', line=260)
W('17,2343', 0o00001, '1/10S', 'OCT', '1', kind='data', line=261)
W('17,2344', 0o00056, 'LINRAT', 'DEC', '46', kind='data', line=262)

# ===========================================================

W('17,2345', 0o34755, 'DAMPING', 'CA', 'ZERO', line=266)
W('17,2346', 0o55462, '', 'TS', 'SAVEHAND', line=267)
W('17,2347', 0o55463, '', 'TS', 'SAVEHAND +1', line=268)
W('17,2350', 0o11462, 'RHCACTIV', 'CCS', 'SAVEHAND', '******************', line=269)
W('17,2351', 0o12354, '', 'TCF', '+3', 'Q,R MANUAL CONTROL    WC = A*(B+|D|)*D', line=270)
W('17,2352', 0o12354, '', 'TCF', '+2', '******************', line=271)
W('17,2353', 0o12354, '', 'TCF', '+1', line=272)
W('17,2354', 0o60000, '', 'DOUBLE', '', 'WHERE', line=273)
W('17,2355', 0o60000, '', 'DOUBLE', line=274)
W('17,2356', 0o62344, '', 'AD', 'LINRAT', '      WC  = COMMANDED ROTATIONAL RATE', line=275)
W('17,2357', 0o00006, '', 'EXTEND', '', '      A   = QUADRATIC SENSITIVITY FACTOR', line=276)
W('17,2360', 0o71462, '', 'MP', 'SAVEHAND', '      B   = LINEAR/QUADRATIC SENSITIVITY', line=277)
W('17,2361', 0o30001, '', 'CA', 'L', '      |D| = ABS. VALUE OF DEFLECTION', line=278)
W('17,2362', 0o00006, '', 'EXTEND', '', '      D   = HAND CONTROLLER DEFLECTION', line=279)
W('17,2363', 0o71444, '', 'MP', 'STIKSENS', line=280)
W('17,2364', 0o57455, '', 'XCH', 'QLAST', 'COMMAND Q RATE, SCALED 45 DEG/SEC', line=281)
W('17,2365', 0o40000, '', 'COM', line=282)
# Page 1447
W('17,2366', 0o61455, '', 'AD', 'QLAST', line=284)
W('17,2367', 0o55741, '', 'TS', 'DAPTEMP3', line=285)
W('17,2370', 0o11463, '', 'CCS', 'SAVEHAND +1', line=286)
W('17,2371', 0o12374, '', 'TCF', '+3', line=287)
W('17,2372', 0o12374, '', 'TCF', '+2', line=288)
W('17,2373', 0o12374, '', 'TCF', '+1', line=289)
W('17,2374', 0o60000, '', 'DOUBLE', line=290)
W('17,2375', 0o60000, '', 'DOUBLE', line=291)
W('17,2376', 0o62344, '', 'AD', 'LINRAT', line=292)
W('17,2377', 0o00006, '', 'EXTEND', line=293)
W('17,2400', 0o71463, '', 'MP', 'SAVEHAND +1', line=294)
W('17,2401', 0o30001, '', 'CA', 'L', line=295)
W('17,2402', 0o00006, '', 'EXTEND', line=296)
W('17,2403', 0o71444, '', 'MP', 'STIKSENS', line=297)
W('17,2404', 0o57456, '', 'XCH', 'RLAST', line=298)
W('17,2405', 0o40000, '', 'COM', line=299)
W('17,2406', 0o61456, '', 'AD', 'RLAST', line=300)
W('17,2407', 0o55742, '', 'TS', 'DAPTEMP4', line=301)
W('17,2410', 0o41455, '', 'CS', 'QLAST', 'INTERVAL.', line=302)
W('17,2411', 0o61422, '', 'AD', 'OMEGAQ', line=303)
W('17,2412', 0o55436, '', 'TS', 'QRATEDIF', line=304)
W('17,2413', 0o41456, '', 'CS', 'RLAST', line=305)
W('17,2414', 0o61423, '', 'AD', 'OMEGAR', line=306)
W('17,2415', 0o55437, '', 'TS', 'RRATEDIF', line=307)
W('17,2416', 0o53437, 'ENTERQR', 'DXCH', 'QRATEDIF', 'TRANSFORM RATES FROM Q,R TO U,V AXES', line=308)
W('17,2417', 0o03146, '', 'TC', 'ROT-TOUV', line=309)
W('17,2420', 0o53427, '', 'DXCH', 'URATEDIF', line=310)
W('17,2421', 0o11741, '', 'CCS', 'DAPTEMP3', 'CHECK IF Q COMMAND CHANGE EXCEEDS', line=311)
W('17,2422', 0o02425, '', 'TC', '+3', 'BREAKOUT LEVEL.  IF NOT, CHECK R.', line=312)
W('17,2423', 0o02425, '', 'TC', '+2', line=313)
W('17,2424', 0o02425, '', 'TC', '+1', line=314)
W('17,2425', 0o61476, '', 'AD', '-RATEDB', line=315)
W('17,2426', 0o00006, '', 'EXTEND', line=316)
W('17,2427', 0o62431, '', 'BZMF', '+2', line=317)
W('17,2430', 0o12447, '', 'TCF', 'ENTERUV -2', 'BREAKOUT LEVEL EXCEEDED.  DIRECT RATE.', line=318)
W('17,2431', 0o11742, '', 'CCS', 'DAPTEMP4', 'R COMMAND BREAKOUT CHECK.', line=319)
W('17,2432', 0o02435, '', 'TC', '+3', line=320)
W('17,2433', 0o02435, '', 'TC', '+2', line=321)
W('17,2434', 0o02435, '', 'TC', '+1', line=322)
W('17,2435', 0o61476, '', 'AD', '-RATEDB', line=323)
W('17,2436', 0o00006, '', 'EXTEND', line=324)
W('17,2437', 0o62441, '', 'BZMF', '+2', line=325)
W('17,2440', 0o12447, '', 'TCF', 'ENTERUV -2', 'BREAKOUT LEVEL EXCEEDED.  DIRECT RATE.', line=326)
W('17,2441', 0o31273, '', 'CA', 'RCSFLAGS', 'BREAKOUT LEVEL NOT EXCEEDED.  CHECK FOR', line=327)
W('17,2442', 0o74741, '', 'MASK', 'QRBIT', 'DIRECT RATE CONTROL LAST TIME.', line=328)
W('17,2443', 0o00006, '', 'EXTEND', line=329)
W('17,2444', 0o12446, '', 'BZF', '+2', line=330)
W('17,2445', 0o12451, '', 'TCF', 'ENTERUV', 'CONTINUE DIRECT RATE CONTROL.', line=331)
W('17,2446', 0o12661, '', 'TCF', 'STILLRCS', 'PSEUDO-AUTO CONTROL.', line=332)
W('17,2447', 0o32342, '', 'CA', '40CYCL', line=333)
# Page 1448
W('17,2450', 0o55457, '', 'TS', 'TCQR', line=335)
W('17,2451', 0o00004, 'ENTERUV', 'INHINT', '', 'DIRECT RATE CONTROL', line=336)
W('17,2452', 0o04674, '', 'TC', 'IBNKCALL', line=337)
W('17,2453', 0o40153, '', 'FCADR', 'ZATTEROR', kind='data', line=338)
W('17,2454', 0o00003, '', 'RELINT', line=339)
W('17,2455', 0o34755, '', 'CA', 'ZERO', line=340)
W('17,2456', 0o55450, '', 'TS', 'DYERROR', line=341)
W('17,2457', 0o55451, '', 'TS', 'DYERROR +1', line=342)
W('17,2460', 0o55452, '', 'TS', 'DZERROR', line=343)
W('17,2461', 0o55453, '', 'TS', 'DZERROR +1', line=344)
W('17,2462', 0o11426, '', 'CCS', 'URATEDIF', line=345)
W('17,2463', 0o12466, '', 'TCF', '+3', line=346)
W('17,2464', 0o12466, '', 'TCF', '+2', line=347)
W('17,2465', 0o12466, '', 'TCF', '+1', line=348)
W('17,2466', 0o61476, '', 'AD', 'TARGETDB', 'IF TARGET DB IS EXCEEDED, CONTINUE', line=349)
W('17,2467', 0o00006, '', 'EXTEND', '', 'DIRECT RATE CONTROL.', line=350)
W('17,2470', 0o62504, '', 'BZMF', 'VDB', line=351)
W('17,2471', 0o11427, '', 'CCS', 'VRATEDIF', line=352)
W('17,2472', 0o12475, '', 'TCF', '+3', line=353)
W('17,2473', 0o12475, '', 'TCF', '+2', line=354)
W('17,2474', 0o12475, '', 'TCF', '+1', line=355)
W('17,2475', 0o61476, '', 'AD', 'TARGETDB', line=356)
W('17,2476', 0o00006, '', 'EXTEND', line=357)
W('17,2477', 0o62501, '', 'BZMF', '+2', line=358)
W('17,2500', 0o12515, '', 'TCF', 'QRTIME', line=359)
W('17,2501', 0o34755, '', 'CA', 'ZERO', line=360)
W('17,2502', 0o55427, '', 'TS', 'VRATEDIF', line=361)
W('17,2503', 0o12515, '', 'TCF', 'QRTIME', line=362)
W('17,2504', 0o11427, 'VDB', 'CCS', 'VRATEDIF', line=363)
W('17,2505', 0o02510, '', 'TC', '+3', line=364)
W('17,2506', 0o02510, '', 'TC', '+2', line=365)
W('17,2507', 0o02510, '', 'TC', '+1', line=366)
W('17,2510', 0o61476, '', 'AD', 'TARGETDB', 'IF TARGET DB IS EXCEEDED, CONTINUE', line=367)
W('17,2511', 0o00006, '', 'EXTEND', '', 'DIRECT RATE CONTROL.  IF NOT, FIRE AND', line=368)
W('17,2512', 0o62524, '', 'BZMF', 'TOPSEUDO', 'SWITCH TO PSEUDO-AUTO CONTROL ON NEXT', line=369)
W('17,2513', 0o34755, '', 'CA', 'ZERO', 'PASS.', line=370)
W('17,2514', 0o55426, '', 'TS', 'URATEDIF', line=371)
W('17,2515', 0o31457, 'QRTIME', 'CA', 'TCQR', 'DIRECT RATE TIME CHECK.', line=372)
W('17,2516', 0o00006, '', 'EXTEND', line=373)
W('17,2517', 0o62524, '', 'BZMF', '+5', 'BRANCH IF TIME EXCEEDS 4 SEC.', line=374)
W('17,2520', 0o41273, '', 'CS', 'RCSFLAGS', line=375)
W('17,2521', 0o74741, '', 'MASK', 'QRBIT', line=376)
W('17,2522', 0o27273, '', 'ADS', 'RCSFLAGS', 'BIT 11 IS 1.', line=377)
W('17,2523', 0o02527, '', 'TC', '+4', line=378)
W('17,2524', 0o44741, 'TOPSEUDO', 'CS', 'QRBIT', line=379)
W('17,2525', 0o71273, '', 'MASK', 'RCSFLAGS', line=380)
W('17,2526', 0o55273, '', 'TS', 'RCSFLAGS', 'BIT 11 IS 0.', line=381)
W('17,2527', 0o32573, '', 'CA', 'HANDADR', line=382)
W('17,2530', 0o55477, '', 'TS', 'RETJADR', line=383)
W('17,2531', 0o34753, '', 'CA', 'ONE', line=384)

# Page 1449
W('17,2532', 0o55505, 'BACKHAND', 'TS', 'AXISCTR', line=387)

W('17,2533', 0o34751, '', 'CA', 'FOUR', line=389)
W('17,2534', 0o55743, '', 'TS', 'NUMBERT', line=390)

W('17,2535', 0o51505, '', 'INDEX', 'AXISCTR', line=392)
W('17,2536', 0o51535, '', 'INDEX', 'SKIPU', line=393)
W('17,2537', 0o12540, '', 'TCF', '+1', line=394)
W('17,2540', 0o34751, '', 'CA', 'FOUR', line=395)
W('17,2541', 0o51505, '', 'INDEX', 'AXISCTR', line=396)
W('17,2542', 0o55535, '', 'TS', 'SKIPU', line=397)
W('17,2543', 0o13005, '', 'TCF', 'LOOPER', line=398)

W('17,2544', 0o51505, '', 'INDEX', 'AXISCTR', line=400)
W('17,2545', 0o11426, '', 'CCS', 'URATEDIF', '      INDEX   AXIS    QUANTITY', line=401)
W('17,2546', 0o34755, '', 'CA', 'ZERO', '      0       -U      1/JETACC-AOSU', line=402)
W('17,2547', 0o12551, '', 'TCF', '+2', '      1       +U      1/JETACC+AOSU', line=403)
W('17,2550', 0o34753, '', 'CA', 'ONE', '      16      -V      1/JETACC-AOSV', line=404)
W('17,2551', 0o51505, '', 'INDEX', 'AXISCTR', '      17      +V      1/JETACC+AOSV', line=405)
W('17,2552', 0o63722, '', 'AD', 'AXISDIFF', 'JETACC = 2 JET ACCELERATION (1 FOR FAIL)', line=406)

W('17,2553', 0o50000, '', 'INDEX', 'A', line=408)
W('17,2554', 0o41571, '', 'CS', '1/ANET2 +1', line=409)
W('17,2555', 0o00006, '', 'EXTEND', line=410)
W('17,2556', 0o51505, '', 'INDEX', 'AXISCTR', 'UPRATEDIF IS SCALED AT PI/4 RAD/SEC', line=411)
W('17,2557', 0o71426, '', 'MP', 'URATEDIF', 'JET TIME IN A, SCALED 32 SEC', line=412)
W('17,2560', 0o54002, '', 'TS', 'Q', line=413)
W('17,2561', 0o20001, '', 'DAS', 'A', line=414)
W('17,2562', 0o60002, '', 'AD', 'Q', line=415)
W('17,2563', 0o54000, '', 'TS', 'A', 'OVERFLOW SKIP', line=416)
W('17,2564', 0o12566, '', 'TCF', '+2', line=417)
W('17,2565', 0o30002, '', 'CA', 'Q', 'RIGHT SIGN AND BIGGER THAN 150MS', line=418)
W('17,2566', 0o51505, 'SETTIME', 'INDEX', 'AXISCTR', line=419)
W('17,2567', 0o55525, '', 'TS', 'TJU', 'SCALED AT 10.67 WHICH IS CLOSE TO 10.24', line=420)
W('17,2570', 0o12727, '', 'TCF', 'AFTERTJ', line=421)

W('17,2571', 0o34755, 'ZEROTJ', 'CA', 'ZERO', line=423)
W('17,2572', 0o12566, '', 'TCF', 'SETTIME', line=424)

W('17,2573', 0o02532, 'HANDADR', 'GENADR', 'BACKHAND', kind='data', line=426)

# GTS WILL BE TRIED IF
# 1. USEQRJTS = 0,
# 2. ALLOWGTS POS,
# 3. JETS ARE OFF (Q,R-AXES)

W('17,2574', 0o34736, 'TRYGTS', 'CAF', 'USEQRJTS', 'IS JET USE MANDATORY.         (AS LONG AS', line=433)
W('17,2575', 0o70111, '', 'MASK', 'DAPBOOLS', 'USEQRJTS BIT IS NOT BIT 15, CCS IS SAFE.)', line=434)
W('17,2576', 0o10000, '', 'CCS', 'A', line=435)
W('17,2577', 0o12107, '', 'TCF', 'RCS', line=436)
W('17,2600', 0o11502, '', 'CCS', 'ALLOWGTS', 'NO.  DOES AOSTASK OK CONTROL FOR GTS?', line=437)
# Page 1450
W('17,2601', 0o12603, '', 'TCF', '+2', line=439)
W('17,2602', 0o12107, '', 'TCF', 'RCS', line=440)
W('17,2603', 0o00006, '', 'EXTEND', line=441)
W('17,2604', 0o00005, '', 'READ', 'CHAN5', line=442)
W('17,2605', 0o10000, '', 'CCS', 'A', line=443)
W('17,2606', 0o12612, '', 'TCF', 'CHKINGTS', line=444)
W('17,2607', 0o00006, 'GOTOGTS', 'EXTEND', line=445)
W('17,2610', 0o32625, '', 'DCA', 'GTSCADR', line=446)
W('17,2611', 0o52006, '', 'DTCB', line=447)

W('17,2612', 0o11633, 'CHKINGTS', 'CCS', 'INGTS', 'WAS THE TRIM GIMBAL CONTROLLING', line=449)
W('17,2613', 0o12615, '', 'TCF', '+2', '      YES.  SET UP A DAMPED NULLING DRIVE.', line=450)
W('17,2614', 0o12107, '', 'TCF', 'RCS', '      NO.  NULLING WAS SET UP BEFORE.  DO RCS.', line=451)
W('17,2615', 0o00004, '', 'INHINT', line=452)
W('17,2616', 0o04674, '', 'TC', 'IBNKCALL', line=453)
W('17,2617', 0o43330, '', 'CADR', 'TIMEGMBL', kind='data', line=454)
W('17,2620', 0o00003, '', 'RELINT', line=455)
W('17,2621', 0o34755, '', 'CAF', 'ZERO', line=456)
W('17,2622', 0o55633, '', 'TS', 'INGTS', line=457)
W('17,2623', 0o12107, '', 'TCF', 'RCS', line=458)

#   EBANK= CDUXD
W('17,2624', 0o03077, 'GTSCADR', '2CADR', 'GTS', kind='data', line=461)
W('17,2625', 0o42106, kind='data', line=461)

# Page 1451
# SUBROUTINE TO COMPUTE Q,R-AXES ATTITUDE ERRORS FOR USE IN THE RCS AND GTS CONTROL LAWS AND THE DISPLAYS.

W('17,2626', 0o30033, 'QERRCALC', 'CAE', 'CDUY', 'Q-ERROR CALCULATION', line=466)
W('17,2627', 0o00006, '', 'EXTEND', line=467)
W('17,2630', 0o21636, '', 'MSU', 'CDUYD', 'CDU ANGLE -- ANGLE DESIRED (Y-AXIS)', line=468)
W('17,2631', 0o55737, '', 'TS', 'DAPTEMP1', 'SAVE FOR RERRCALC', line=469)
W('17,2632', 0o00006, '', 'EXTEND', line=470)
W('17,2633', 0o71415, '', 'MP', 'M21', '(CDUY-CDUYD)*M21 SCALED AT PI RADIANS', line=471)
W('17,2634', 0o55752, '', 'TS', 'E', line=472)
W('17,2635', 0o30034, '', 'CAE', 'CDUZ', 'SECOND TERM CALCULATION:', line=473)
W('17,2636', 0o00006, '', 'EXTEND', line=474)
W('17,2637', 0o21637, '', 'MSU', 'CDUZD', 'CDU ANGLE -ANGLE DESIRED (Z-AXIS)', line=475)
W('17,2640', 0o55740, '', 'TS', 'DAPTEMP2', 'SAVE FOR RERRCALC', line=476)
W('17,2641', 0o00006, '', 'EXTEND', line=477)
W('17,2642', 0o71417, '', 'MP', 'M22', '(CDUZ-CDUZD)*M22 SCALED AT PI RADIANS', line=478)
W('17,2643', 0o61300, '', 'AD', 'DELQEROR', 'KALCMANU INERFACE ERROR', line=479)
W('17,2644', 0o61752, '', 'AD', 'E', line=480)
W('17,2645', 0o57450, '', 'XCH', 'QERROR', 'SAVE Q-ERROR FOR EIGHT-BALL DISPLAY.', line=481)

W('17,2646', 0o31737, 'RERRCALC', 'CAE', 'DAPTEMP1', 'R-ERROR CALCULATION:', line=483)
W('17,2647', 0o00006, '', 'EXTEND', '', 'CDU ANGLE -ANGLE DESIRED (Y-AXIS)', line=484)
W('17,2650', 0o71416, '', 'MP', 'M31', '(CDUY-CDUYD)*M31 SCALED AT PI RADIANS', line=485)
W('17,2651', 0o55752, '', 'TS', 'E', line=486)
W('17,2652', 0o31740, '', 'CAE', 'DAPTEMP2', 'SECOND TERM CALCULATION:', line=487)
W('17,2653', 0o00006, '', 'EXTEND', '', 'CDU ANGLE -ANGLE DESIRED (Z-AXIS)', line=488)
W('17,2654', 0o71420, '', 'MP', 'M32', '(CDUZ-CDUZD)*M32 SCALED AT PI RADIANS', line=489)
W('17,2655', 0o61301, '', 'AD', 'DELREROR', 'KALCMANU INERFACE ERROR', line=490)
W('17,2656', 0o61752, '', 'AD', 'E', line=491)
W('17,2657', 0o57452, '', 'XCH', 'RERROR', 'SAVE R-ERROR FOR EIGHT-BALL DISPLAY.', line=492)
W('17,2660', 0o00002, '', 'TC', 'Q', line=493)

# Page 1452
# "ATTSTEER" IS THE ENTRY POINT FOR Q,R-AXES (U,V-AXES) ATTITUDE CONTROL USING THE REACTION CONTROL SYSTEM

S('ATTSTEER', 'equals', 0o46661, line=498)  # "STILLRCS" IS THE RCS EXIT FROM TRYGTS.

W('17,2661', 0o31452, 'STILLRCS', 'CA', 'RERROR', line=500)
W('17,2662', 0o22000, '', 'LXCH', 'A', line=501)
W('17,2663', 0o31450, '', 'CA', 'QERROR', line=502)
W('17,2664', 0o03146, '', 'TC', 'ROT-TOUV', line=503)
W('17,2665', 0o53752, '', 'DXCH', 'UERROR', line=504)

# PREPARES CALL TO TJETLAW (OR SPSRCS(DOCKED))
# PREFORMS SKIP LOGIC ON U OR Y AXIS IF NEEDED.

W('17,2666', 0o33113, 'TJLAW', 'CA', 'TJLAWADR', line=509)
W('17,2667', 0o55477, '', 'TS', 'RETJADR', line=510)
W('17,2670', 0o34753, '', 'CA', 'ONE', line=511)
W('17,2671', 0o55505, '', 'TS', 'AXISCTR', line=512)
W('17,2672', 0o51505, '', 'INDEX', 'AXISCTR', line=513)
W('17,2673', 0o51535, '', 'INDEX', 'SKIPU', line=514)
W('17,2674', 0o12675, '', 'TCF', '+1', line=515)
W('17,2675', 0o34751, '', 'CA', 'FOUR', line=516)
W('17,2676', 0o51505, '', 'INDEX', 'AXISCTR', line=517)
W('17,2677', 0o55535, '', 'TS', 'SKIPU', line=518)
W('17,2700', 0o13005, '', 'TCF', 'LOOPER', line=519)
W('17,2701', 0o51505, '', 'INDEX', 'AXISCTR', line=520)
W('17,2702', 0o31751, '', 'CA', 'UERROR', line=521)
W('17,2703', 0o55752, '', 'TS', 'E', line=522)
W('17,2704', 0o51505, '', 'INDEX', 'AXISCTR', line=523)
W('17,2705', 0o31426, '', 'CA', 'OMEGAU', line=524)
W('17,2706', 0o55427, '', 'TS', 'EDOT', line=525)
W('17,2707', 0o30111, '', 'CA', 'DAPBOOLS', line=526)
W('17,2710', 0o74737, '', 'MASK', 'CSMDOCKD', line=527)
W('17,2711', 0o10000, '', 'CCS', 'A', line=528)
W('17,2712', 0o12715, '', 'TCF', '+3', line=529)
W('17,2713', 0o03252, '', 'TC', 'TJETLAW', line=530)
W('17,2714', 0o12727, '', 'TCF', 'AFTERTJ', line=531)
W('17,2715', 0o40111, '', 'CS', 'DAPBOOLS', 'DOCKED.  IF GIMBAL USABLE DO GTS CONTROL', line=532)
W('17,2716', 0o74736, '', 'MASK', 'USEQRJTS', '      ON THE NEXT PASS.', line=533)
W('17,2717', 0o10000, '', 'CCS', 'A', 'USEQRJTS BIT MUST NOT BE BIT 15.', line=534)
W('17,2720', 0o55631, '', 'TS', 'COTROLER', 'GIMBAL USABLE.  STORE POSITIVE VALUE.', line=535)
W('17,2721', 0o00004, '', 'INHINT', line=536)
W('17,2722', 0o04674, '', 'TC', 'IBNKCALL', line=537)
W('17,2723', 0o43727, '', 'CADR', 'SPSRCS', 'DETERMINE RCS CONTROL', kind='data', line=538)
W('17,2724', 0o00003, '', 'RELINT', line=539)
W('17,2725', 0o34751, '', 'CAF', 'FOUR', 'ALWAYS CALL FOR 2-JET CONTROL ABOUT U,V.', line=540)
W('17,2726', 0o55743, '', 'TS', 'NUMBERT', 'FALL THROUGH TO JET SELECTION, ETC.', line=541)

# Q,R-JET-SELECTION-LOGIC
#
# INPUT:        AXISCTR         0,1 FOR U,V
# SNUFFBIT        ZERO TJETU,V AND TRANS. ONLY IF SET IN A DPS BURN
# Page 1453
# TJU,TJV         JET TIME SCALED 10.24 SEC.
# NUMBERT         INDICATES NUMBER OF JETS AND TYPE OF POLICY
# RETJADR         WHERE TO RETURN TO
#
# OUTPUT:       NO.U(V)JETS     RATE DERIVATION FEEDBACK
# CHANNEL 5
# SKIPU,SKIPV     FOR LESS THAN 150MS FIRING
#
# NOTES:        IN CASE OF FAILURE IN DESIRED ROTATION POLICY, "ALL" UNFAILED
# JETS OF THE DESIRED POLICY ARE SELECTED.  SINCE THERE ARE ONLY
# TWO JETS, THIS MEANS THE OTHER ONE OR NONE.  THE ALARM IS SENT
# IF NONE CAN BE FOUND.
#
# TIMES LESS THAN 14 MSEC ARE TAKEN TO CALL FOR A SINGLE-JET
# MINIMUM IMPULSE, WITH THE JET CHOSEN SEMI-RANDOMLY.

W('17,2727', 0o30101, 'AFTERTJ', 'CA', 'FLAGWRD5', 'IF SNUFFBIT SET DURING A DPS BURN GO TO', line=564)
W('17,2730', 0o74737, '', 'MASK', 'SNUFFBIT', 'XTRANS; THAT IS, INHIBIT CONTROL.', line=565)
W('17,2731', 0o00006, '', 'EXTEND', line=566)
W('17,2732', 0o12743, '', 'BZF', 'DOROTAT', line=567)
W('17,2733', 0o40106, '', 'CS', 'FLGWRD10', line=568)
W('17,2734', 0o74737, '', 'MASK', 'APSFLBIT', line=569)
W('17,2735', 0o00006, '', 'EXTEND', line=570)
W('17,2736', 0o12743, '', 'BZF', 'DOROTAT', line=571)
W('17,2737', 0o30111, '', 'CA', 'DAPBOOLS', line=572)
W('17,2740', 0o74744, '', 'MASK', 'DRIFTBIT', line=573)
W('17,2741', 0o00006, '', 'EXTEND', line=574)
W('17,2742', 0o13063, '', 'BZF', 'XTRANS', line=575)

W('17,2743', 0o34752, 'DOROTAT', 'CAF', 'TWO', line=577)
W('17,2744', 0o54001, '', 'TS', 'L', line=578)
W('17,2745', 0o51505, '', 'INDEX', 'AXISCTR', line=579)
W('17,2746', 0o11525, '', 'CCS', 'TJU', line=580)
W('17,2747', 0o12754, '', 'TCF', '+5', line=581)
W('17,2750', 0o12777, '', 'TCF', 'NOROTAT', line=582)
W('17,2751', 0o12753, '', 'TCF', '+2', line=583)
W('17,2752', 0o12777, '', 'TCF', 'NOROTAT', line=584)
W('17,2753', 0o22007, '', 'ZL', line=585)
W('17,2754', 0o64753, '', 'AD', 'ONE', line=586)
W('17,2755', 0o55737, '', 'TS', 'ABSTJ', line=587)

W('17,2756', 0o31505, '', 'CA', 'AXISCTR', line=589)
W('17,2757', 0o60001, '', 'AD', 'L', line=590)
W('17,2760', 0o55744, '', 'TS', 'ROTINDEX', '0 1 2 3 = -U -V +U +V', line=591)

W('17,2761', 0o31737, '', 'CA', 'ABSTJ', line=593)
W('17,2762', 0o63110, '', 'AD', '-150MS', line=594)
W('17,2763', 0o00006, '', 'EXTEND', line=595)
W('17,2764', 0o63010, '', 'BZMF', 'DOSKIP', line=596)
# Page 1454
W('17,2765', 0o03173, '', 'TC', 'SELCTSUB', line=598)

W('17,2766', 0o51505, '', 'INDEX', 'AXISCTR', line=600)
W('17,2767', 0o33105, '', 'CA', 'INDEXES', line=601)
W('17,2770', 0o54001, '', 'TS', 'L', line=602)

W('17,2771', 0o31741, '', 'CA', 'POLYTEMP', line=604)
W('17,2772', 0o00004, '', 'INHINT', line=605)
W('17,2773', 0o50001, '', 'INDEX', 'L', line=606)
W('17,2774', 0o05754, '', 'TC', 'WRITEP', line=607)

W('17,2775', 0o00003, '', 'RELINT', line=609)
W('17,2776', 0o13051, '', 'TCF', 'FEEDBACK', line=610)

W('17,2777', 0o51505, 'NOROTAT', 'INDEX', 'AXISCTR', line=612)
W('17,3000', 0o33105, '', 'CA', 'INDEXES', line=613)
W('17,3001', 0o00004, '', 'INHINT', line=614)
W('17,3002', 0o50000, '', 'INDEX', 'A', line=615)
W('17,3003', 0o05753, '', 'TC', 'WRITEP -1', line=616)

W('17,3004', 0o00003, '', 'RELINT', line=618)
W('17,3005', 0o11505, 'LOOPER', 'CCS', 'AXISCTR', line=619)
W('17,3006', 0o01477, '', 'TC', 'RETJADR', line=620)
W('17,3007', 0o13236, '', 'TCF', 'CLOSEOUT', line=621)
W('17,3010', 0o41737, 'DOSKIP', 'CS', 'ABSTJ', line=622)
W('17,3011', 0o63107, '', 'AD', '+TJMINT6', '14MS', line=623)
W('17,3012', 0o00006, '', 'EXTEND', line=624)
W('17,3013', 0o63032, '', 'BZMF', 'NOTMIN', line=625)

W('17,3014', 0o27737, '', 'ADS', 'ABSTJ', line=627)
W('17,3015', 0o51505, '', 'INDEX', 'AXISCTR', line=628)
W('17,3016', 0o11525, '', 'CCS', 'TJU', line=629)
W('17,3017', 0o33107, '', 'CA', '+TJMINT6', line=630)
W('17,3020', 0o13022, '', 'TCF', '+2', line=631)
W('17,3021', 0o43107, '', 'CS', '+TJMINT6', line=632)
W('17,3022', 0o51505, '', 'INDEX', 'AXISCTR', line=633)
W('17,3023', 0o55525, '', 'TS', 'TJU', line=634)

W('17,3024', 0o11500, '', 'CCS', 'SENSETYP', 'ENSURE MIN-IMPULSE NOT AGAINST TRANS', line=636)
W('17,3025', 0o13031, '', 'TCF', 'NOTMIN -1', line=637)
W('17,3026', 0o00006, '', 'EXTEND', line=638)
W('17,3027', 0o00004, '', 'READ', 'LOSCALAR', line=639)
W('17,3030', 0o74753, '', 'MASK', 'ONE', line=640)
W('17,3031', 0o55743, '', 'TS', 'NUMBERT', line=641)

W('17,3032', 0o03173, 'NOTMIN', 'TC', 'SELCTSUB', line=643)

W('17,3033', 0o51505, '', 'INDEX', 'AXISCTR', line=645)
W('17,3034', 0o33105, '', 'CA', 'INDEXES', line=646)
W('17,3035', 0o00004, '', 'INHINT', line=647)
# Page 1455
W('17,3036', 0o55471, '', 'TS', 'T6FURTHA +1', line=649)
W('17,3037', 0o31741, '', 'CA', 'POLYTEMP', line=650)
W('17,3040', 0o51471, '', 'INDEX', 'T6FURTHA +1', line=651)
W('17,3041', 0o05754, '', 'TC', 'WRITEP', line=652)

W('17,3042', 0o31737, '', 'CA', 'ABSTJ', line=654)
W('17,3043', 0o55470, '', 'TS', 'T6FURTHA', line=655)
W('17,3044', 0o03114, '', 'TC', 'JTLST', 'IN QR BANK BY NOW', line=656)

W('17,3045', 0o00003, '', 'RELINT', line=658)

W('17,3046', 0o34755, '', 'CA', 'ZERO', line=660)
W('17,3047', 0o51505, '', 'INDEX', 'AXISCTR', line=661)
W('17,3050', 0o55535, '', 'TS', 'SKIPU', line=662)

W('17,3051', 0o46245, 'FEEDBACK', 'CS', 'THREE', line=664)
W('17,3052', 0o61743, '', 'AD', 'NUMBERT', line=665)
W('17,3053', 0o00006, '', 'EXTEND', line=666)
W('17,3054', 0o63057, '', 'BZMF', '+3', line=667)

W('17,3055', 0o34752, '', 'CA', 'TWO', line=669)
W('17,3056', 0o13060, '', 'TCF', '+2', line=670)
W('17,3057', 0o34753, '', 'CA', 'ONE', line=671)
W('17,3060', 0o51505, '', 'INDEX', 'AXISCTR', line=672)
W('17,3061', 0o55522, '', 'TS', 'NO.UJETS', line=673)
W('17,3062', 0o13005, '', 'TCF', 'LOOPER', line=674)

W('17,3063', 0o34755, 'XTRANS', 'CA', 'ZERO', line=676)
W('17,3064', 0o55525, '', 'TS', 'TJU', line=677)
W('17,3065', 0o55526, '', 'TS', 'TJV', line=678)
W('17,3066', 0o34751, '', 'CA', 'FOUR', line=679)
W('17,3067', 0o00004, '', 'INHINT', line=680)
W('17,3070', 0o57535, '', 'XCH', 'SKIPU', line=681)
W('17,3071', 0o00006, '', 'EXTEND', line=682)
W('17,3072', 0o13074, '', 'BZF', '+2', line=683)
W('17,3073', 0o05757, '', 'TC', 'WRITEU -1', line=684)
W('17,3074', 0o34751, '', 'CA', 'FOUR', line=685)
W('17,3075', 0o57536, '', 'XCH', 'SKIPV', line=686)
W('17,3076', 0o00003, '', 'RELINT', line=687)

W('17,3077', 0o00006, '', 'EXTEND', line=689)
W('17,3100', 0o13236, '', 'BZF', 'CLOSEOUT', line=690)
W('17,3101', 0o00004, '', 'INHINT', line=691)
W('17,3102', 0o05770, '', 'TC', 'WRITEV -1', line=692)
W('17,3103', 0o00003, '', 'RELINT', line=693)

W('17,3104', 0o13236, '', 'TCF', 'CLOSEOUT', line=695)
W('17,3105', 0o00004, 'INDEXES', 'DEC', '4', kind='data', line=696)
W('17,3106', 0o00015, '', 'DEC', '13', kind='data', line=697)
W('17,3107', 0o00026, '+TJMINT6', 'DEC', '22', kind='data', line=698)
# Page 1456
W('17,3110', 0o77417, '-150MS', 'DEC', '-240', kind='data', line=700)
W('17,3111', 0o00600, 'BIT8,9', 'OCT', '00600', kind='data', line=701)
W('17,3112', 0o00266, 'SCLNORM', 'OCT', '266', kind='data', line=702)
W('17,3113', 0o02671, 'TJLAWADR', 'GENADR', 'TJLAW +3', 'RETURN ADDRESS FOR RCS ATTITUDE CONTROL', kind='data', line=703)

# THE JET LIST:
# THIS IS A WAITLIST FOR T6RUPTS.
#
# CALLED BY:
# CA      TJ              # TIME WHEN NEXT JETS WILL BE WRITTEN
# TS      T6FURTHA
# CA      INDEX           # AXIS TO BE WRITTEN AT TJ (FROM NOW)
# TS      T6FURTHA +1
# TC      JTLST
#
# EXAMPLE -- U-AXIS AUTOPILOT WILL WRITE ITS ROTATION CODE OF
# JETS INTO CHANNEL 5.  IF IT DESIRES TO TURN OFF THIS POLICY WITHIN
# 150MS AND THEN FIRE NEXTU, A CALL TO JTLST IS MADE WITH T6FURTHA
# CONTAINING THE TIME TO TURN OFF THE POLICY, T6FURTHA +1 THE INDEX
# OF THE U-AXIS(4), AND NEXTU WILL CONTAIN THE "U-TRANS" POLICY OR ZERO.
#
# THE LIST IS EXACTLY 3 LONG.  (THIS LEADS UP TO SKIP LOGIC AND 150MS LIMIT)
# THE INPUT IS THE LAST MEMBER OF THE LIST.
#
# RETURNS BY:
# +       TC      Q
#
# DEFINITIONS:  (OUTPUT)
# TIME6           TIME OF NEXT RUPT
# T6NEXT          DELTA TIME TO NEXT RUPT
# T6FURTHA        DELTA TIME FROM 2ND TO LAST RUPT
# NXT6ADR         AXIS INDEX      0 -- P-AXIS
# T6NEXT +1       AXIS INDEX      4 -- U-AXIS
# T6FURTHA +1     AXIS INDEX      13 -- V-AXIS

W('17,3114', 0o41470, 'JTLST', 'CS', 'T6FURTHA', line=735)
W('17,3115', 0o60031, '', 'AD', 'TIME6', line=736)
W('17,3116', 0o00006, '', 'EXTEND', line=737)
W('17,3117', 0o63131, '', 'BZMF', 'MIDORLST', 'TIME6 -- TI IS IN A', line=738)

W('17,3120', 0o23465, '', 'LXCH', 'NXT6ADR', line=740)
W('17,3121', 0o53467, '', 'DXCH', 'T6NEXT', line=741)
W('17,3122', 0o53471, '', 'DXCH', 'T6FURTHA', line=742)
W('17,3123', 0o54031, '', 'TS', 'TIME6', line=743)
W('17,3124', 0o23465, '', 'LXCH', 'NXT6ADR', line=744)

W('17,3125', 0o34735, 'TURNON', 'CA', 'BIT15', line=746)
W('17,3126', 0o00006, '', 'EXTEND', line=747)
W('17,3127', 0o05013, '', 'WOR', 'CHAN13', line=748)
W('17,3130', 0o00002, '', 'TC', 'Q', line=749)

# Page 1457
W('17,3131', 0o61466, 'MIDORLST', 'AD', 'T6NEXT', line=752)
W('17,3132', 0o00006, '', 'EXTEND', line=753)
W('17,3133', 0o63142, '', 'BZMF', 'LASTCHG', 'TIME6 + T6NEXT - T IS IN A', line=754)

W('17,3134', 0o23467, '', 'LXCH', 'T6NEXT +1', line=756)
W('17,3135', 0o53471, '', 'DXCH', 'T6FURTHA', line=757)
W('17,3136', 0o00006, '', 'EXTEND', line=758)
W('17,3137', 0o60031, '', 'SU', 'TIME6', line=759)
W('17,3140', 0o53467, '', 'DXCH', 'T6NEXT', line=760)

W('17,3141', 0o00002, '', 'TC', 'Q', line=762)

W('17,3142', 0o40000, 'LASTCHG', 'CS', 'A', line=764)
W('17,3143', 0o64754, '', 'AD', 'NEG0', line=765)
W('17,3144', 0o55470, '', 'TS', 'T6FURTHA', line=766)

W('17,3145', 0o00002, '', 'TC', 'Q', line=768)

# ROT-TOUV IS ENTERED WITH THE Q-COMPONENT OF THE QUANTITY TO BE TRANSFORMED IN A AND THE R-COMPONENT IN L.
# ROT-TOUV TRANSFORMS THE QUANTITY INTO THE NON-ORTHOGONAL U-V AXIS SYSTEM.  IN THE U-V SYSTEM NO CROSS-COUPLING IS
# PRODUCED FROM RCS JET FIRINGS.  AT THE COMPLETION OF ROT-TOUV, THE U-COMPONENT OF THE TRANSFORMED QUANTITY IS IN
# A AND THE V-COMPONENT IS IN L.

W('17,3146', 0o23740, 'ROT-TOUV', 'LXCH', 'ROTEMP2', '(R) IS PUT INTO ROTEMP2', line=775)
W('17,3147', 0o00006, '', 'EXTEND', line=776)
W('17,3150', 0o71627, '', 'MP', 'COEFFQ', line=777)
W('17,3151', 0o57740, '', 'XCH', 'ROTEMP2', '(R) GOES TO A AND COEFFQ.(Q) TO ROTEMP2', line=778)
W('17,3152', 0o00006, '', 'EXTEND', line=779)
W('17,3153', 0o71630, '', 'MP', 'COEFFR', line=780)
W('17,3154', 0o54001, '', 'TS', 'L', 'COEFFR.(R) IS PUT INTO L', line=781)
W('17,3155', 0o61740, '', 'AD', 'ROTEMP2', line=782)
W('17,3156', 0o55737, '', 'TS', 'ROTEMP1', 'COEFFQ.(Q)+COEFFR.(R) IS PUT IN ROTEMP1', line=783)
W('17,3157', 0o13163, '', 'TCF', '+4', line=784)
W('17,3160', 0o50000, '', 'INDEX', 'A', 'COEFFQ.(Q) + COEFFR.(R) HAS OVERFLOWED', line=785)
W('17,3161', 0o44734, '', 'CS', 'LIMITS', 'AND IS LIMITED TO POSMAX OR NEGMAX', line=786)
W('17,3162', 0o55737, '', 'TS', 'ROTEMP1', line=787)
W('17,3163', 0o41740, '', 'CS', 'ROTEMP2', line=788)
W('17,3164', 0o60001, '', 'AD', 'L', '-COEFFQ.(Q) + COEFFR.(R) IS NOW IN A', line=789)
W('17,3165', 0o54007, '', 'TS', '7', line=790)
W('17,3166', 0o13171, '', 'TCF', '+3', line=791)
W('17,3167', 0o50000, '', 'INDEX', 'A', '-COEFFQ.(Q) + COEFFR.(R) HAS OVERFLOWED', line=792)
W('17,3170', 0o44734, '', 'CS', 'LIMITS', 'AND IS LIMITED TO POSMAX OR NEGMAX', line=793)
W('17,3171', 0o23737, '', 'LXCH', 'ROTEMP1', 'COEFFQ.(Q) + COEFFR.(R) IS PUT INTO L', line=794)
W('17,3172', 0o00002, '', 'TC', 'Q', line=795)
W('17,3173', 0o51744, 'SELCTSUB', 'INDEX', 'ROTINDEX', line=796)
W('17,3174', 0o33225, '', 'CA', 'ALLJETS', line=797)
W('17,3175', 0o51743, '', 'INDEX', 'NUMBERT', line=798)
W('17,3176', 0o73231, '', 'MASK', 'TYPEPOLY', line=799)
W('17,3177', 0o55741, '', 'TS', 'POLYTEMP', line=800)
# Page 1458
W('17,3200', 0o71262, '', 'MASK', 'CH5MASK', line=802)
W('17,3201', 0o10000, '', 'CCS', 'A', line=803)
W('17,3202', 0o13204, '', 'TCF', '+2', line=804)

W('17,3203', 0o00002, '', 'TC', 'Q', line=806)

W('17,3204', 0o36245, '', 'CA', 'THREE', line=808)
W('17,3205', 0o55743, 'FAILOOP', 'TS', 'NUMBERT', line=809)
W('17,3206', 0o51744, '', 'INDEX', 'ROTINDEX', line=810)
W('17,3207', 0o33225, '', 'CA', 'ALLJETS', line=811)
W('17,3210', 0o51743, '', 'INDEX', 'NUMBERT', line=812)
W('17,3211', 0o73231, '', 'MASK', 'TYPEPOLY', line=813)
W('17,3212', 0o55741, '', 'TS', 'POLYTEMP', line=814)
W('17,3213', 0o71262, '', 'MASK', 'CH5MASK', line=815)
W('17,3214', 0o00006, '', 'EXTEND', line=816)
W('17,3215', 0o13203, '', 'BZF', 'FAILOOP -2', line=817)
W('17,3216', 0o11743, '', 'CCS', 'NUMBERT', line=818)
W('17,3217', 0o13205, '', 'TCF', 'FAILOOP', line=819)
W('17,3220', 0o51505, '', 'INDEX', 'AXISCTR', line=820)
W('17,3221', 0o55525, '', 'TS', 'TJU', line=821)
W('17,3222', 0o05567, '', 'TC', 'ALARM', line=822)
W('17,3223', 0o02004, '', 'OCT', '02004', kind='data', line=823)
W('17,3224', 0o12777, '', 'TCF', 'NOROTAT', line=824)
W('17,3225', 0o00110, 'ALLJETS', 'OCT', '00110', '      -U      6 13', kind='data', line=825)
W('17,3226', 0o00022, '', 'OCT', '00022', '      -V      2 9', kind='data', line=826)
W('17,3227', 0o00204, '', 'OCT', '00204', '      +U      5 14', kind='data', line=827)
W('17,3230', 0o00041, '', 'OCT', '00041', '      +V      1 10', kind='data', line=828)
W('17,3231', 0o00125, 'TYPEPOLY', 'OCT', '00125', '      -X      1 5 9 13', kind='data', line=829)
W('17,3232', 0o00252, '', 'OCT', '00252', '      +X      2 6 10 14', kind='data', line=830)
W('17,3233', 0o00146, '', 'OCT', '00146', '      A       2 5 10 13', kind='data', line=831)
W('17,3234', 0o00231, '', 'OCT', '00231', '      B       1 6 9 14', kind='data', line=832)
W('17,3235', 0o00377, '', 'OCT', '00377', '      ALL     1 2 5 6 9 10 13 14', kind='data', line=833)

# THE FOLLOWING SETS THE INTERRUPT FLIP-FLOP AS SOON AS POSSIBLE, WHICH PERMITS A RETURN TO THE INTERRUPTED JOB.

W('17,3236', 0o33240, 'CLOSEOUT', 'CA', 'ADRRUPT', line=837)
W('17,3237', 0o07754, '', 'TC', 'MAKERUPT', line=838)

W('17,3240', 0o03241, 'ADRRUPT', 'ADRES', 'ENDJASK', kind='data', line=840)

W('17,3241', 0o53754, 'ENDJASK', 'DXCH', 'DAPARUPT', line=842)
W('17,3242', 0o52011, '', 'DXCH', 'ARUPT', line=843)
W('17,3243', 0o53756, '', 'DXCH', 'DAPBQRPT', line=844)
W('17,3244', 0o56017, '', 'XCH', 'BRUPT', line=845)
W('17,3245', 0o22002, '', 'LXCH', 'Q', line=846)
W('17,3246', 0o34735, '', 'CAF', 'NEGMAX', 'NEGATIVE DAPZRUPT SIGNALS JASK IS OVER.', line=847)
W('17,3247', 0o53760, '', 'DXCH', 'DAPZRUPT', line=848)
W('17,3250', 0o52016, '', 'DXCH', 'ZRUPT', line=849)
W('17,3251', 0o15272, '', 'TCF', 'NOQRSM', line=850)
# Page 1459
#   BLOCK 3
#   SETLOC FFTAG6
#   BANK

#   COUNT* $$/DAP

W('7754', 0o00006, 'MAKERUPT', 'EXTEND', line=858)
W('7755', 0o07754, '', 'EDRUPT', 'MAKERUPT', line=859)
