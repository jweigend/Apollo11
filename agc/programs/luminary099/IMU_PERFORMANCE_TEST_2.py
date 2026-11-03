"""IMU_PERFORMANCE_TEST_2.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/IMU_PERFORMANCE_TEST_2.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 373-381 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('IMU_PERFORMANCE_TEST_2', 'IMU_PERFORMANCE_TEST_2.agc', 'Luminary099', pages='373-381')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     IMU_PERFORMANCE_TEST_2.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        373-381
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

# Page 373
# NAME --       IMU PERFORMANCE TESTS 2
#
# DATE --       MARCH 20, 1967
#
# BY --         SYSTEM TEST GROUP 864-6900 EXT. 1274
#
# MODNO. --     ZERO
#
# FUNCTIONAL DESCRIPTION
#
# POSITIONING ROUTINES FOR THE IMU PERFORMANCE TESTS AS WELL AS SOME OF
# THE TESTS THEMSELVES.  FOR A DESCRIPTION OF THESE SUBROUTINES AND THE
# OPERATING PROCEDURES (TYPICALLY) SEE STG MEMO 685.  THEORETICAL REF. E-1973

#   BANK 33
#   SETLOC IMU2
#   BANK
#   EBANK= POSITON
#   COUNT* $$/P07

W('37,2002', 0o05311, 'REDO', 'TC', 'NEWMODEX', line=50)
W('37,2003', 0o00007, '', 'MM', '07', kind='data', line=51)

W('37,2004', 0o02325, 'GEOIMUTT', 'TC', 'IMUZERR', line=53)
W('37,2005', 0o34755, 'IMUBACK', 'CA', 'ZERO', line=54)
W('37,2006', 0o55414, '', 'TS', 'NDXCTR', line=55)
W('37,2007', 0o55440, '', 'TS', 'TORQNDX', line=56)
W('37,2010', 0o55441, '', 'TS', 'TORQNDX +1', line=57)
W('37,2011', 0o55576, '', 'TS', 'OVFLOWCK', line=58)
W('37,2012', 0o34361, 'NBPOSPL', 'CA', 'DEC17', line=59)
W('37,2013', 0o55571, '', 'TS', 'ZERONDX', line=60)
W('37,2014', 0o32476, '', 'CA', 'XNBADR', line=61)
W('37,2015', 0o02367, '', 'TC', 'ZEROING', line=62)
W('37,2016', 0o34736, '', 'CA', 'HALF', line=63)
W('37,2017', 0o55664, '', 'TS', 'XNB', line=64)
W('37,2020', 0o06037, 'GUESS', 'TC', 'INTPRET', line=65)
W('37,2021', 0o62545, 'LATAZCHK', 'DLOAD', 'SL2', kind='interp', line=66)
W('37,2022', 0o02403, '', '', 'LATITUDE', kind='operand', line=67)
W('37,2023', 0o15047, '', 'STODL', 'DSPTEM1 +1', kind='interp', line=68)
W('37,2024', 0o02401, '', '', 'AZIMUTH', kind='operand', line=69)
W('37,2025', 0o77434, '', 'RTB', 'EXIT', kind='interp', line=70)
W('37,2026', 0o21614, '', '', '1STO2S', kind='operand', line=71)
W('37,2027', 0o56154, '', 'XCH', 'MPAC', line=72)
W('37,2030', 0o55045, '', 'TS', 'DSPTEM1', line=73)
W('37,2031', 0o32473, '', 'CAF', 'VN0641', line=74)
W('37,2032', 0o04616, '', 'TC', 'BANKCALL', line=75)
W('37,2033', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=76)
W('37,2034', 0o02270, '', 'TC', 'ENDTEST1', line=77)
W('37,2035', 0o02037, '', 'TC', '+2', line=78)
W('37,2036', 0o02031, '', 'TC', '-5', line=79)
# Page 374
W('37,2037', 0o06037, '', 'TC', 'INTPRET', line=81)
W('37,2040', 0o47135, '', 'SLOAD', 'RTB', kind='interp', line=82)
W('37,2041', 0o01046, '', '', 'DSPTEM1', kind='operand', line=83)
W('37,2042', 0o21576, '', '', 'CDULOGIC', kind='operand', line=84)
W('37,2043', 0o02401, '', 'STORE', 'AZIMUTH', kind='interp', line=85)
W('37,2044', 0o60535, '', 'SLOAD', 'SR2', kind='interp', line=86)
W('37,2045', 0o01047, '', '', 'DSPTEM1 +1', kind='operand', line=87)
W('37,2046', 0o02403, '', 'STORE', 'LATITUDE', kind='interp', line=88)
W('37,2047', 0o57546, '', 'COS', 'DCOMP', kind='interp', line=89)
W('37,2050', 0o77752, '', 'SL1', kind='interp', line=90)
W('37,2051', 0o16437, '', 'STODL', 'WANGI', kind='interp', line=91)
W('37,2052', 0o02403, '', '', 'LATITUDE', kind='operand', line=92)
W('37,2053', 0o72556, '', 'SIN', 'SL1', kind='interp', line=93)
W('37,2054', 0o16435, '', 'STODL', 'WANGO', kind='interp', line=94)
W('37,2055', 0o02401, '', '', 'AZIMUTH', kind='operand', line=95)
W('37,2056', 0o73406, '', 'PUSH', 'SIN', kind='interp', line=96)
W('37,2057', 0o02675, '', 'STORE', 'YNB +2', kind='interp', line=97)
W('37,2060', 0o16705, '', 'STODL', 'ZNB +4', kind='interp', line=98)
W('37,2061', 0o77746, '', 'COS', kind='interp', line=99)
W('37,2062', 0o02677, '', 'STORE', 'YNB +4', kind='interp', line=100)
W('37,2063', 0o77676, '', 'DCOMP', kind='interp', line=101)
W('37,2064', 0o36703, 'POSGMBL', 'STCALL', 'ZNB +2', kind='interp', line=102)
W('37,2065', 0o47353, '', '', 'CALCGA', kind='operand', line=103)
W('37,2066', 0o77776, '', 'EXIT', kind='interp', line=104)
W('37,2067', 0o04616, '', 'TC', 'BANKCALL', line=105)
W('37,2070', 0o17000, '', 'CADR', 'IMUCOARS', kind='data', line=106)
W('37,2071', 0o34736, '', 'CAF', 'BIT14', 'IF BIT14 SET, GIMBAL LOCK', line=107)
W('37,2072', 0o70077, '', 'MASK', 'FLAGWRD3', line=108)
W('37,2073', 0o00006, '', 'EXTEND', line=109)
W('37,2074', 0o12076, '', 'BZF', '+2', line=110)
W('37,2075', 0o25414, '', 'INCR', 'NDXCTR', '+1 IF IN GIMBAL LOCK, OTHERWISE 0', line=111)
W('37,2076', 0o05516, '', 'TC', 'DOWNFLAG', line=112)
W('37,2077', 0o00056, '', 'ADRES', 'GLOKFAIL', 'RESET GIMBAL LOCK FLAG', kind='data', line=113)
W('37,2100', 0o02315, '', 'TC', 'IMUSLLLG', line=114)
W('37,2101', 0o11414, '', 'CCS', 'NDXCTR', 'IF ONE GO AND DO A PIPA TEST ONLY', line=115)
W('37,2102', 0o02126, '', 'TC', 'PIPACHK', 'ALIGN AND MEASURE VERTICAL PIPA RATE', line=116)
W('37,2103', 0o02320, '', 'TC', 'FINIMUDD', line=117)
W('37,2104', 0o00006, '', 'EXTEND', line=118)
W('37,2105', 0o31575, '', 'DCA', 'PERFDLAY', line=119)
W('37,2106', 0o05277, '', 'TC', 'LONGCALL', 'DELAY WHILE SUSPENSION STABILIZES', line=120)
#   EBANK= POSITON
W('37,2107', 0o02113, '', '2CADR', 'GOESTIMS', kind='data', line=122)
W('37,2110', 0o76065, kind='data', line=122)

W('37,2111', 0o32116, '', 'CA', 'ESTICADR', line=124)
W('37,2112', 0o05133, '', 'TC', 'JOBSLEEP', line=125)
W('37,2113', 0o32116, 'GOESTIMS', 'CA', 'ESTICADR', line=126)
W('37,2114', 0o05137, '', 'TC', 'JOBWAKE', line=127)
W('37,2115', 0o05261, '', 'TC', 'TASKOVER', line=128)
W('37,2116', 0o76500, 'ESTICADR', 'CADR', 'ESTIMS', kind='data', line=129)
W('37,2117', 0o34755, 'TORQUE', 'CA', 'ZERO', line=130)
# Page 375
W('37,2120', 0o55050, '', 'TS', 'DSPTEM2', line=132)
W('37,2121', 0o31504, '', 'CA', 'DRIFTI', line=133)
W('37,2122', 0o55051, '', 'TS', 'DSPTEM2 +1', line=134)
W('37,2123', 0o51416, '', 'INDEX', 'POSITON', line=135)
W('37,2124', 0o55420, '', 'TS', 'SOUTHDR -1', line=136)
W('37,2125', 0o02457, '', 'TC', 'SHOW', line=137)

W('37,2126', 0o51414, 'PIPACHK', 'INDEX', 'NDXCTR', 'PIPA TEST', line=139)
W('37,2127', 0o02130, '', 'TC', '+1', line=140)
W('37,2130', 0o02447, '', 'TC', 'EARTHR*', line=141)
W('37,2131', 0o34361, '', 'CA', 'DEC17', 'ALLOW PIP COUNTER TO OVERFLOW 17 TIMES', line=142)
W('37,2132', 0o55476, '', 'TS', 'DATAPL +4', 'IN THE ALLOTTED TIME INTERVAL', line=143)
W('37,2133', 0o32474, '', 'CA', 'DEC58', line=144)
W('37,2134', 0o55412, '', 'TS', 'LENGTHOT', line=145)
W('37,2135', 0o34753, '', 'CA', 'ONE', line=146)
W('37,2136', 0o55537, '', 'TS', 'RESULTCT', line=147)
W('37,2137', 0o34755, '', 'CA', 'ZERO', line=148)
W('37,2140', 0o51415, '', 'INDEX', 'PIPINDEX', line=149)
W('37,2141', 0o54037, '', 'TS', 'PIPAX', line=150)
W('37,2142', 0o55472, '', 'TS', 'DATAPL', line=151)
W('37,2143', 0o02332, '', 'TC', 'CHECKG', line=152)
W('37,2144', 0o00004, '', 'INHINT', line=153)
W('37,2145', 0o34752, '', 'CAF', 'TWO', line=154)
W('37,2146', 0o05173, '', 'TC', 'TWIDDLE', line=155)
#   EBANK= XSM
W('37,2147', 0o02151, '', 'ADRES', 'PIPATASK', kind='data', line=157)
W('37,2150', 0o05155, '', 'TC', 'ENDOFJOB', line=158)

W('37,2151', 0o00006, 'PIPATASK', 'EXTEND', line=160)
W('37,2152', 0o27412, '', 'DIM', 'LENGTHOT', line=161)
W('37,2153', 0o31412, '', 'CA', 'LENGTHOT', line=162)
W('37,2154', 0o00006, '', 'EXTEND', line=163)
W('37,2155', 0o62161, '', 'BZMF', 'STARTPIP', line=164)
W('37,2156', 0o34742, '', 'CAF', 'BIT10', line=165)
W('37,2157', 0o05173, '', 'TC', 'TWIDDLE', line=166)
#   EBANK= XSM
W('37,2160', 0o02151, '', 'ADRES', 'PIPATASK', kind='data', line=168)
W('37,2161', 0o34736, 'STARTPIP', 'CAF', 'PRIO20', line=169)
W('37,2162', 0o05105, '', 'TC', 'FINDVAC', line=170)
#   EBANK= XSM
W('37,2163', 0o02166, '', '2CADR', 'PIPJOBB', kind='data', line=172)
W('37,2164', 0o76065, kind='data', line=172)

W('37,2165', 0o05261, '', 'TC', 'TASKOVER', line=174)

W('37,2166', 0o51414, 'PIPJOBB', 'INDEX', 'NDXCTR', line=176)
W('37,2167', 0o02170, '', 'TC', '+1', line=177)
W('37,2170', 0o02447, '', 'TC', 'EARTHR*', line=178)
W('37,2171', 0o31412, '', 'CA', 'LENGTHOT', line=179)
# Page 376
W('37,2172', 0o00006, '', 'EXTEND', line=181)
W('37,2173', 0o62175, '', 'BZMF', '+2', line=182)
W('37,2174', 0o05155, '', 'TC', 'ENDOFJOB', line=183)

W('37,2175', 0o34756, '', 'CA', 'FIVE', line=185)
W('37,2176', 0o55537, '', 'TS', 'RESULTCT', line=186)
W('37,2177', 0o02332, '', 'TC', 'CHECKG', line=187)
W('37,2200', 0o11473, '', 'CCS', 'DATAPL +1', line=188)
W('37,2201', 0o02205, '', 'TC', '+4', line=189)
W('37,2202', 0o05705, '', 'TC', 'CCSHOLE', line=190)
W('37,2203', 0o41476, '', 'CS', 'DATAPL +4', line=191)
W('37,2204', 0o55476, '', 'TS', 'DATAPL +4', line=192)
W('37,2205', 0o00006, '', 'EXTEND', line=193)
W('37,2206', 0o41473, '', 'DCS', 'DATAPL', line=194)
W('37,2207', 0o21477, '', 'DAS', 'DATAPL +4', line=195)

W('37,2210', 0o06037, '', 'TC', 'INTPRET', line=197)
W('37,2211', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=198)
W('37,2212', 0o02501, '', '', 'DATAPL +6', kind='operand', line=199)
W('37,2213', 0o02475, '', '', 'DATAPL +2', kind='operand', line=200)
W('37,2214', 0o45044, '', 'BPL', 'CALL', kind='interp', line=201)
W('37,2215', 0o76217, '', '', 'AINGOTN', kind='operand', line=202)
W('37,2216', 0o76275, '', '', 'OVERFFIX', kind='operand', line=203)
W('37,2217', 0o56325, 'AINGOTN', 'PDDL', 'DDV', kind='interp', line=204)
W('37,2220', 0o02477, '', '', 'DATAPL +4', kind='operand', line=205)
W('37,2221', 0o47075, '', 'DMPR', 'RTB', kind='interp', line=206)
W('37,2222', 0o37056, '', '', 'DEC585', 'DEC585 HAS BEEN REDEFINED FOR LEM', kind='operand', line=207)
W('37,2223', 0o21612, '', '', 'SGNAGREE', kind='operand', line=208)
W('37,2224', 0o01051, '', 'STORE', 'DSPTEM2', kind='interp', line=209)
W('37,2225', 0o77776, '', 'EXIT', kind='interp', line=210)
W('37,2226', 0o11414, '', 'CCS', 'NDXCTR', line=211)
W('37,2227', 0o02301, '', 'TC', 'COAALIGN', 'TAKE PLATFORM OUT OF GIMBAL LOCK', line=212)
W('37,2230', 0o02457, '', 'TC', 'SHOW', line=213)
W('37,2231', 0o32471, 'VERTDRFT', 'CA', '3990DEC', 'ABOUT 1 HOUR VERTICAL DRIFT TEST', line=214)
W('37,2232', 0o55412, '', 'TS', 'LENGTHOT', line=215)
W('37,2233', 0o51416, '', 'INDEX', 'POSITON', line=216)
W('37,2234', 0o41417, '', 'CS', 'SOUTHDR -2', line=217)
W('37,2235', 0o55442, '', 'TS', 'DRIFTT', line=218)
W('37,2236', 0o11415, '', 'CCS', 'PIPINDEX', 'OFFSET PLATFORM TO MISS PIP DEAD-ZONES', line=219)
W('37,2237', 0o12245, '', 'TCF', 'PON4', 'Z-UP IN POS 4', line=220)
W('37,2240', 0o44747, 'PON2', 'CS', 'BIT5', 'X-UP', line=221)
W('37,2241', 0o27565, '', 'ADS', 'ERCOMP +2', line=222)
W('37,2242', 0o34747, '', 'CA', 'BIT5', line=223)
W('37,2243', 0o27567, '', 'ADS', 'ERCOMP +4', line=224)
W('37,2244', 0o12251, '', 'TCF', 'PON', line=225)
W('37,2245', 0o44747, 'PON4', 'CS', 'BIT5', line=226)
W('37,2246', 0o27565, '', 'ADS', 'ERCOMP +2', line=227)
W('37,2247', 0o34747, '', 'CA', 'BIT5', line=228)
W('37,2250', 0o27563, '', 'ADS', 'ERCOMP', line=229)
W('37,2251', 0o02447, 'PON', 'TC', 'EARTHR*', line=230)
# Page 377
W('37,2252', 0o34755, '', 'CA', 'ZERO', 'ALLOW ONLY SOUTH GYRO EARTH RATE COMPENS', line=232)
W('37,2253', 0o55404, '', 'TS', 'ERVECTOR', line=233)
W('37,2254', 0o55405, '', 'TS', 'ERVECTOR +1', line=234)
W('37,2255', 0o34733, 'GUESS1', 'CAF', 'POSMAX', line=235)
W('37,2256', 0o55440, '', 'TS', 'TORQNDX', line=236)
W('37,2257', 0o55441, '', 'TS', 'TORQNDX +1', line=237)
W('37,2260', 0o30032, '', 'CA', 'CDUX', line=238)
W('37,2261', 0o55413, '', 'TS', 'LOSVEC', line=239)
W('37,2262', 0o02500, '', 'TC', 'ESTIMS', line=240)
W('37,2263', 0o31502, 'VALMIS', 'CA', 'DRIFTO', line=241)
W('37,2264', 0o55051, '', 'TS', 'DSPTEM2 +1', line=242)
W('37,2265', 0o34755, '', 'CA', 'ZERO', line=243)
W('37,2266', 0o55050, '', 'TS', 'DSPTEM2', line=244)
W('37,2267', 0o02457, '', 'TC', 'SHOW', line=245)

W('37,2270', 0o05516, 'ENDTEST1', 'TC', 'DOWNFLAG', line=247)
W('37,2271', 0o00007, '', 'ADRES', 'IMUSE', kind='data', line=248)
W('37,2272', 0o44755, '', 'CS', 'ZERO', line=249)
W('37,2273', 0o05314, '', 'TC', 'NEWMODEA', line=250)
W('37,2274', 0o05472, '', 'TC', 'ENDEXT', line=251)

# Page 378
W('37,2275', 0o43215, 'OVERFFIX', 'DAD', 'DAD', kind='interp', line=254)
W('37,2276', 0o06530, '', '', 'DPPOSMAX', kind='operand', line=255)
W('37,2277', 0o37064, '', '', 'ONEDPP', kind='operand', line=256)
W('37,2300', 0o77616, '', 'RVQ', kind='interp', line=257)

W('37,2301', 0o00006, 'COAALIGN', 'EXTEND', '', 'COARSE ALIGN SUBROUTINE', line=259)
W('37,2302', 0o23571, '', 'QXCH', 'ZERONDX', line=260)
W('37,2303', 0o34755, '', 'CA', 'ZERO', line=261)
W('37,2304', 0o54321, '', 'TS', 'THETAD', line=262)
W('37,2305', 0o54322, '', 'TS', 'THETAD +1', line=263)
W('37,2306', 0o54323, '', 'TS', 'THETAD +2', line=264)
W('37,2307', 0o04616, '', 'TC', 'BANKCALL', line=265)
W('37,2310', 0o17000, '', 'CADR', 'IMUCOARS', kind='data', line=266)
W('37,2311', 0o04616, 'ALIGNCOA', 'TC', 'BANKCALL', line=267)
W('37,2312', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=268)
W('37,2313', 0o03047, '', 'TC', 'SOMERR2', line=269)
W('37,2314', 0o01571, '', 'TC', 'ZERONDX', line=270)

W('37,2315', 0o00006, 'IMUSLLLG', 'EXTEND', line=272)
W('37,2316', 0o23571, '', 'QXCH', 'ZERONDX', line=273)
W('37,2317', 0o02311, '', 'TC', 'ALIGNCOA', line=274)

W('37,2320', 0o00006, 'FINIMUDD', 'EXTEND', line=276)
W('37,2321', 0o23571, '', 'QXCH', 'ZERONDX', line=277)
W('37,2322', 0o04616, '', 'TC', 'BANKCALL', line=278)
W('37,2323', 0o17210, '', 'CADR', 'IMUFINE', kind='data', line=279)
W('37,2324', 0o02311, '', 'TC', 'ALIGNCOA', line=280)

W('37,2325', 0o00006, 'IMUZERR', 'EXTEND', line=282)
W('37,2326', 0o23571, '', 'QXCH', 'ZERONDX', line=283)
W('37,2327', 0o04616, '', 'TC', 'BANKCALL', line=284)
W('37,2330', 0o16714, '', 'CADR', 'IMUZERO', kind='data', line=285)
W('37,2331', 0o02311, '', 'TC', 'ALIGNCOA', line=286)

W('37,2332', 0o00006, 'CHECKG', 'EXTEND', '', 'PIP PULSE CATCHING ROUTINE', line=288)
W('37,2333', 0o23417, '', 'QXCH', 'QPLACE', line=289)
W('37,2334', 0o02342, '', 'TC', '+6', line=290)
W('37,2335', 0o00003, 'CHECKG1', 'RELINT', line=291)
W('37,2336', 0o30067, '', 'CA', 'NEWJOB', line=292)
W('37,2337', 0o00006, '', 'EXTEND', line=293)
W('37,2340', 0o62346, '', 'BZMF', '+6', line=294)
W('37,2341', 0o05122, '', 'TC', 'CHANG1', line=295)
W('37,2342', 0o00004, '', 'INHINT', line=296)
W('37,2343', 0o51415, '', 'INDEX', 'PIPINDEX', line=297)
W('37,2344', 0o40037, '', 'CS', 'PIPAX', line=298)
W('37,2345', 0o55571, '', 'TS', 'ZERONDX', line=299)
W('37,2346', 0o00004, '', 'INHINT', line=300)
# Page 379
W('37,2347', 0o51415, '', 'INDEX', 'PIPINDEX', line=302)
W('37,2350', 0o30037, '', 'CA', 'PIPAX', line=303)
W('37,2351', 0o61571, '', 'AD', 'ZERONDX', line=304)
W('37,2352', 0o00006, '', 'EXTEND', line=305)
W('37,2353', 0o12335, '', 'BZF', 'CHECKG1', line=306)
W('37,2354', 0o51415, '', 'INDEX', 'PIPINDEX', line=307)
W('37,2355', 0o30037, '', 'CA', 'PIPAX', line=308)
W('37,2356', 0o51537, '', 'INDEX', 'RESULTCT', line=309)
W('37,2357', 0o55472, '', 'TS', 'DATAPL', line=310)
W('37,2360', 0o04102, '', 'TC', 'FINETIME', line=311)
W('37,2361', 0o51537, '', 'INDEX', 'RESULTCT', line=312)
W('37,2362', 0o55473, '', 'TS', 'DATAPL +1', line=313)
W('37,2363', 0o51537, '', 'INDEX', 'RESULTCT', line=314)
W('37,2364', 0o23474, '', 'LXCH', 'DATAPL +2', line=315)
W('37,2365', 0o00003, '', 'RELINT', line=316)
W('37,2366', 0o01417, 'ENDCHKG', 'TC', 'QPLACE', line=317)

W('37,2367', 0o54001, 'ZEROING', 'TS', 'L', line=319)
W('37,2370', 0o12372, '', 'TCF', '+2', line=320)
W('37,2371', 0o55571, 'ZEROING1', 'TS', 'ZERONDX', line=321)
W('37,2372', 0o34755, '', 'CAF', 'ZERO', line=322)
W('37,2373', 0o50001, '', 'INDEX', 'L', line=323)
W('37,2374', 0o54000, '', 'TS', '0', line=324)
W('37,2375', 0o24001, '', 'INCR', 'L', line=325)
W('37,2376', 0o11571, '', 'CCS', 'ZERONDX', line=326)
W('37,2377', 0o12371, '', 'TCF', 'ZEROING1', line=327)
W('37,2400', 0o00002, '', 'TC', 'Q', line=328)

# Page 380
W('37,2401', 0o65345, 'ERTHRVSE', 'DLOAD', 'PDDL', kind='interp', line=331)
W('37,2402', 0o37057, '', '', 'SCHZEROS', 'PD24 = (SIN             -COS     0)(OMEG/MS)', kind='operand', line=332)
W('37,2403', 0o02403, '', '', 'LATITUDE', kind='operand', line=333)
W('37,2404', 0o57546, '', 'COS', 'DCOMP', kind='interp', line=334)
W('37,2405', 0o73525, '', 'PDDL', 'SIN', kind='interp', line=335)
W('37,2406', 0o02403, '', '', 'LATITUDE', kind='operand', line=336)
W('37,2407', 0o74266, '', 'VDEF', 'VXSC', kind='interp', line=337)
W('37,2410', 0o36001, '', '', 'OMEG/MS', kind='operand', line=338)
W('37,2411', 0o02405, '', 'STORE', 'ERVECTOR', kind='interp', line=339)
W('37,2412', 0o77634, '', 'RTB', kind='interp', line=340)
W('37,2413', 0o21573, '', '', 'LOADTIME', kind='operand', line=341)
W('37,2414', 0o26433, '', 'STOVL', 'TMARK', kind='interp', line=342)
W('37,2415', 0o37057, '', '', 'SCHZEROS', kind='operand', line=343)
W('37,2416', 0o02564, '', 'STORE', 'ERCOMP', kind='interp', line=344)
W('37,2417', 0o77616, '', 'RVQ', kind='interp', line=345)

W('37,2420', 0o47020, 'EARTHR', 'ITA', 'RTB', kind='interp', line=347)
W('37,2421', 0o00051, '', '', 'S2', kind='operand', line=348)
W('37,2422', 0o21573, '', '', 'LOADTIME', kind='operand', line=349)
W('37,2423', 0o02431, '', 'STORE', 'TEMPTIME', kind='interp', line=350)
W('37,2424', 0o51025, '', 'DSU', 'BPL', kind='interp', line=351)
W('37,2425', 0o02433, '', '', 'TMARK', kind='operand', line=352)
W('37,2426', 0o76431, '', '', 'ERTHR', kind='operand', line=353)
W('37,2427', 0o77624, '', 'CALL', kind='interp', line=354)
W('37,2430', 0o76275, '', '', 'OVERFFIX', kind='operand', line=355)
W('37,2431', 0o74261, 'ERTHR', 'SL', 'VXSC', kind='interp', line=356)
W('37,2432', 0o20212, '', '', '9D', kind='operand', line=357)
W('37,2433', 0o02405, '', '', 'ERVECTOR', kind='operand', line=358)
W('37,2434', 0o53321, '', 'MXV', 'VAD', kind='interp', line=359)
W('37,2435', 0o02643, '', '', 'XSM', kind='operand', line=360)
W('37,2436', 0o02564, '', '', 'ERCOMP', kind='operand', line=361)
W('37,2437', 0o16564, '', 'STODL', 'ERCOMP', kind='interp', line=362)
W('37,2440', 0o02431, '', '', 'TEMPTIME', kind='operand', line=363)
W('37,2441', 0o02433, '', 'STORE', 'TMARK', kind='interp', line=364)
W('37,2442', 0o47170, '', 'AXT,1', 'RTB', kind='interp', line=365)
W('37,2443', 0o02563, '', 'ECADR', 'ERCOMP', kind='data', line=366)
W('37,2444', 0o21705, '', '', 'PULSEIMU', kind='operand', line=367)
W('37,2445', 0o77650, '', 'GOTO', kind='interp', line=368)
W('37,2446', 0o00051, '', '', 'S2', kind='operand', line=369)

W('37,2447', 0o00006, 'EARTHR*', 'EXTEND', line=371)
W('37,2450', 0o23420, '', 'QXCH', 'QPLACES', line=372)
W('37,2451', 0o06037, '', 'TC', 'INTPRET', line=373)
W('37,2452', 0o77624, '', 'CALL', kind='interp', line=374)
W('37,2453', 0o76420, '', '', 'EARTHR', kind='operand', line=375)
W('37,2454', 0o77776, '', 'EXIT', kind='interp', line=376)
W('37,2455', 0o02315, '', 'TC', 'IMUSLLLG', line=377)
W('37,2456', 0o01420, '', 'TC', 'QPLACES', line=378)

W('37,2457', 0o00006, 'SHOW', 'EXTEND', line=380)
# Page 381
W('37,2460', 0o23417, '', 'QXCH', 'QPLACE', line=382)
W('37,2461', 0o31416, 'SHOW1', 'CA', 'POSITON', line=383)
W('37,2462', 0o55052, '', 'TS', 'DSPTEM2 +2', line=384)
W('37,2463', 0o32472, '', 'CA', 'VB06N98', line=385)
W('37,2464', 0o04616, '', 'TC', 'BANKCALL', line=386)
W('37,2465', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=387)
W('37,2466', 0o02270, '', 'TC', 'ENDTEST1', 'V34', line=388)
W('37,2467', 0o01417, '', 'TC', 'QPLACE', 'V33', line=389)
W('37,2470', 0o12461, '', 'TCF', 'SHOW1', line=390)

W('37,2471', 0o07626, '3990DEC', 'DEC', '3990', kind='data', line=392)
W('37,2472', 0o01542, 'VB06N98', 'VN', '0698', kind='data', line=393)
W('37,2473', 0o01451, 'VN0641', 'VN', '0641', kind='data', line=394)
S('DEC17', 'equals', 0o4361, line=395)
W('37,2474', 0o00072, 'DEC58', 'DEC', '58', kind='data', line=396)
W('37,2475', 0o02737, 'OGCPL', 'ECADR', 'OGC', kind='data', line=397)
S('1SECX', 'equals', 0o4777, line=398)
W('37,2476', 0o01664, 'XNBADR', 'GENADR', 'XNB', kind='data', line=399)
W('37,2477', 0o01642, 'XSMADR', 'GENADR', 'XSM', kind='data', line=400)
#   BLOCK 2
#   COUNT* $$/P07
W('4102', 0o00004, 'FINETIME', 'INHINT', '', 'RETURNS WITH INTERRUPT INHIBITED', line=403)
W('4103', 0o00006, '', 'EXTEND', line=404)
W('4104', 0o00004, '', 'READ', 'LOSCALAR', line=405)
W('4105', 0o54001, '', 'TS', 'L', line=406)
W('4106', 0o00006, '', 'EXTEND', line=407)
W('4107', 0o06004, '', 'RXOR', 'LOSCALAR', line=408)
W('4110', 0o00006, '', 'EXTEND', line=409)
W('4111', 0o14115, '', 'BZF', '+4', line=410)
W('4112', 0o00006, '', 'EXTEND', line=411)
W('4113', 0o00004, '', 'READ', 'LOSCALAR', line=412)
W('4114', 0o54001, '', 'TS', 'L', line=413)
W('4115', 0o44733, '', 'CS', 'POSMAX', line=414)
W('4116', 0o60001, '', 'AD', 'L', line=415)
W('4117', 0o00006, '', 'EXTEND', line=416)
W('4120', 0o14103, '', 'BZF', 'FINETIME +1', line=417)
W('4121', 0o00006, '', 'EXTEND', line=418)
W('4122', 0o00003, '', 'READ', 'HISCALAR', line=419)
W('4123', 0o00002, '', 'TC', 'Q', line=420)
