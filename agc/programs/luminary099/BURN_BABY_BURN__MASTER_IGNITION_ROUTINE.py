"""BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 731-751 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('BURN_BABY_BURN__MASTER_IGNITION_ROUTINE', 'BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc', 'Luminary099', pages='731-751')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        731-751
# Mod history:  2009-05-19 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2009-06-07 RSB  Corrected 3 typos.
# 2009-07-23 RSB  Added Onno's notes on the naming
# of this function, which he got from
# Don Eyles.
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

# Page 731
# At the get-together of the AGC developers celebrating the 40th anniversary
# of the first moonwalk, Don Eyles (one of the authors of this routine along
# with Peter Adler) has related to us a little interesting history behind the
# naming of the routine.
#
# It traces back to 1965 and the Los Angeles riots, and was inspired
# by disc jockey extraordinaire and radio station owner Magnificent Montague.
# Magnificent Montague used the phrase "Burn, baby! BURN!" when spinning the
# hottest new records. Magnificent Montague was the charismatic voice of
# soul music in Chicago, New York, and Los Angeles from the mid-1950s to
# the mid-1960s.
# BURN, BABY, BURN -- MASTER IGNITION ROUTINE

#   BANK 36
#   SETLOC P40S
#   BANK
#   EBANK= WHICH
#   COUNT* $$/P40

# THE MASTER IGNITION ROUTINE IS DESIGNED FOR USE BY THE FOLLOWING LEM PROGRAMS:  P12, P40, P42, P61, P63.
# IT PERFORMS ALL FUNCTIONS IMMEDIATELY ASSOCIATED WITH APS OR DPS IGNITION:  IN PARTICULAR, EVERYTHING LYING
# BETWEEN THE PRE-IGNITION TIME CHECK -- ARE WE WITHIN 45 SECONDS OF TIG? -- AND TIG + 26 SECONDS, WHEN DPS
# PROGRAMS THROTTLE UP.
#
# VARIATIONS AMONG PROGRAMS ARE ACCOMODATED BY MEANS OF TABLES CONTAINING CONSTANTS (FOR AVEGEXIT, FOR
# WAITLIST, FOR PINBALL) AND TCF INSTRUCTIONS.  USERS PLACE THE ADRES OF THE HEAD OF THE APPROPRIATE TABLE
# (OF P61TABLE FOR P61LM, FOR EXAMPLE) IN ERASABLE REGISTER `WHICH' (E4).  THE IGNITION ROUTINE THEN INDEXES BY
# WHICH TO OBTAIN OR EXECUTE THE PROPER TABLE ENTRY.  THE IGNITION ROUTINE IS INITIATED BY A TCF BURNBABY,
# THROUGH BANKJUMP IF NECESSARY.  THERE IS NO RETURN.
#
# THE MASTER IGNITION ROUTINE WAS CONCEIVED AND EXECUTED, AND (NOTA BENE) IS MAINTAINED BY ADLER AND EYLES.
#
# HONI SOIT QUI MAL Y PENSE
#
# ***********************************************
# TABLES FOR THE IGNITION ROUTINE
# ***********************************************
#
# NOLI SE TANGERE

W('36,2022', 0o01512, 'P12TABLE', 'VN', '0674', '(0)', kind='data', line=74)
W('36,2023', 0o12325, '', 'TCF', 'ULLGNOT', '(1)', line=75)
W('36,2024', 0o12612, '', 'TCF', 'COMFAIL3', '(2)', line=76)
W('36,2025', 0o13062, '', 'TCF', 'GOCUTOFF', '(3)', line=77)
W('36,2026', 0o15261, '', 'TCF', 'TASKOVER', '(4)', line=78)
W('36,2027', 0o12146, '', 'TCF', 'P12SPOT', '(5)', line=79)
W('36,2030', 0o00000, '', 'DEC', '0', '(6)   NO ULLAGE', kind='data', line=80)
#   EBANK= WHICH
W('36,2031', 0o03770, '', '2CADR', 'SERVEXIT', '(7)', kind='data', line=82)
W('36,2032', 0o64067, kind='data', line=82)

W('36,2033', 0o12376, '', 'TCF', 'DISPCHNG', '(11)', line=84)
W('36,2034', 0o12563, '', 'TCF', 'WAITABIT', '(12)', line=85)
W('36,2035', 0o12521, '', 'TCF', 'P12IGN', '(13)', line=86)

W('36,2036', 0o01450, 'P40TABLE', 'VN', '0640', '(0)', kind='data', line=88)
W('36,2037', 0o12325, '', 'TCF', 'ULLGNOT', '(1)', line=89)
W('36,2040', 0o12614, '', 'TCF', 'COMFAIL4', '(2)', line=90)
W('36,2041', 0o13047, '', 'TCF', 'GOPOST', '(3)', line=91)
W('36,2042', 0o15261, '', 'TCF', 'TASKOVER', '(4)', line=92)
W('36,2043', 0o12146, '', 'TCF', 'P40SPOT', '(5)', line=93)
# Page 732
W('36,2044', 0o04300, '', 'DEC', '2240', '(6)', kind='data', line=95)
#   EBANK= OMEGAQ
W('36,2045', 0o03666, '', '2CADR', 'STEERING', '(7)', kind='data', line=97)
W('36,2046', 0o74066, kind='data', line=97)

W('36,2047', 0o12366, '', 'TCF', 'P40SJUNK', '(11)', line=99)
W('36,2050', 0o12563, '', 'TCF', 'WAITABIT', '(12)', line=100)
W('36,2051', 0o12504, '', 'TCF', 'P40IGN', '(13)', line=101)
W('36,2052', 0o13123, '', 'TCF', 'REP40ALM', '(14)', line=102)

W('36,2053', 0o12151, 'P41TABLE', 'TCF', 'P41SPOT', '(5)', line=104)
W('36,2054', 0o77776, '', 'DEC', '-1', '(6)', kind='data', line=105)
#   EBANK= OMEGAQ
W('36,2055', 0o03376, '', '2CADR', 'CALCN85', '(7)', kind='data', line=107)
W('36,2056', 0o74066, kind='data', line=107)

W('36,2057', 0o12400, '', 'TCF', 'COMMON', '(11)', line=109)
W('36,2060', 0o12567, '', 'TCF', 'TIGTASK', '(12)', line=110)

W('36,2061', 0o01450, 'P42TABLE', 'VN', '0640', '(0)', kind='data', line=112)
W('36,2062', 0o12322, '', 'TCF', 'WANTAPS', '(1)', line=113)
W('36,2063', 0o12614, '', 'TCF', 'COMFAIL4', '(2)', line=114)
W('36,2064', 0o13047, '', 'TCF', 'GOPOST', '(3)', line=115)
W('36,2065', 0o15261, '', 'TCF', 'TASKOVER', '(4)', line=116)
W('36,2066', 0o12146, '', 'TCF', 'P42SPOT', '(5)', line=117)
W('36,2067', 0o05120, '', 'DEC', '2640', '(6)', kind='data', line=118)
#   EBANK= OMEGAQ
W('36,2070', 0o03666, '', '2CADR', 'STEERING', '(7)', kind='data', line=120)
W('36,2071', 0o74066, kind='data', line=120)

W('36,2072', 0o12366, '', 'TCF', 'P40SJUNK', '(11)', line=122)
W('36,2073', 0o12563, '', 'TCF', 'WAITABIT', '(12)', line=123)
W('36,2074', 0o12541, '', 'TCF', 'P42IGN', '(13)', line=124)
W('36,2075', 0o13420, '', 'TCF', 'P42STAGE', '(14)', line=125)

W('36,2076', 0o01476, 'P63TABLE', 'VN', '0662', '(0)', kind='data', line=127)
W('36,2077', 0o12325, '', 'TCF', 'ULLGNOT', '(1)', line=128)
W('36,2100', 0o12612, '', 'TCF', 'COMFAIL3', '(2)', line=129)
W('36,2101', 0o12777, '', 'TCF', 'V99RECYC', '(3)', line=130)
W('36,2102', 0o15261, '', 'TCF', 'TASKOVER', '(4)', line=131)
W('36,2103', 0o12151, '', 'TCF', 'P63SPOT', '(5)', line=132)
W('36,2104', 0o04300, '', 'DEC', '2240', '(6)', kind='data', line=133)
#   EBANK= WHICH
W('36,2105', 0o03770, '', '2CADR', 'SERVEXIT', '(7)', kind='data', line=135)
W('36,2106', 0o64067, kind='data', line=135)

W('36,2107', 0o12376, '', 'TCF', 'DISPCHNG', '(11)', line=137)
W('36,2110', 0o12563, '', 'TCF', 'WAITABIT', '(12)', line=138)
# Page 733
W('36,2111', 0o12455, '', 'TCF', 'P63IGN', '(13)', line=140)

W('36,2112', 0o01477, 'ABRTABLE', 'VN', '0663', '(0)', kind='data', line=142)
W('36,2113', 0o12325, '', 'TCF', 'ULLGNOT', '(1)', line=143)
W('36,2114', 0o12612, '', 'TCF', 'COMFAIL3', '(2)', line=144)
W('36,2115', 0o13062, '', 'TCF', 'GOCUTOFF', '(3)', line=145)
W('36,2116', 0o15261, '', 'TCF', 'TASKOVER', '(4)', line=146)
W('36,2117', 0o12120, '', 'NOOP', '', '(5)', line=147)
W('36,2120', 0o12121, '', 'NOOP', '', '(6)', line=148)
W('36,2121', 0o12122, '', 'NOOP', '', '(7)', line=149)
W('36,2122', 0o12123, '', 'NOOP', line=150)
W('36,2123', 0o12376, '', 'TCF', 'DISPCHNG', '(11)', line=151)
W('36,2124', 0o12563, '', 'TCF', 'WAITABIT', '(12)', line=152)
W('36,2125', 0o12531, '', 'TCF', 'ABRTIGN', '(13)', line=153)

# *********************************
# GENERAL PURPOSE IGNITION ROUTINES
# *********************************

W('36,2126', 0o05353, 'BURNBABY', 'TC', 'PHASCHNG', 'GROUP 4 RESTARTS HERE', line=159)
W('36,2127', 0o04024, '', 'OCT', '04024', kind='data', line=160)

W('36,2130', 0o34755, '', 'CAF', 'ZERO', 'EXTIRPATE JUNK LEFT IN DVTOTAL', line=162)
W('36,2131', 0o55507, '', 'TS', 'DVTOTAL', line=163)
W('36,2132', 0o55510, '', 'TS', 'DVTOTAL +1', line=164)

W('36,2133', 0o04616, '', 'TC', 'BANKCALL', 'P40AUTO MUST BE BANKCALLED EVEN FROM ITS', line=166)
W('36,2134', 0o73747, '', 'CADR', 'P40AUTO', 'OWN BANK TO SET UP RETURN PROPERLY', kind='data', line=167)

W('36,2135', 0o00006, 'B*RNB*B*', 'EXTEND', line=169)
W('36,2136', 0o31442, '', 'DCA', 'TIG', 'STORE NOMINAL TIG FOR OBLATENESS COMP.', line=170)
W('36,2137', 0o53512, '', 'DXCH', 'GOBLTIME', 'AND FOR P70 OR P71.', line=171)

W('36,2140', 0o00004, '', 'INHINT', line=173)
W('36,2141', 0o04674, '', 'TC', 'IBNKCALL', line=174)
W('36,2142', 0o75564, '', 'CADR', 'ENGINOF3', kind='data', line=175)
W('36,2143', 0o00003, '', 'RELINT', line=176)

W('36,2144', 0o51455, '', 'INDEX', 'WHICH', line=178)
W('36,2145', 0o10005, '', 'TCF', '5', line=179)

S('P42SPOT', 'equals', 0o104146, line=181)  # (5)
S('P12SPOT', 'equals', 0o104146, line=182)  # (5)
S('P63SPOT', 'equals', 0o104151, line=183)  # (5)   IN P63 CLOKTASK ALREADY GOING
W('36,2146', 0o44762, 'P40SPOT', 'CS', 'CNTDNDEX', '(5)', line=184)
# Page 734
W('36,2147', 0o04616, '', 'TC', 'BANKCALL', 'MUST BE BANKCALLED FOR GENERALIZED', line=186)
W('36,2150', 0o74664, '', 'CADR', 'STCLOK2', '      RETURN', kind='data', line=187)
W('36,2151', 0o06037, 'P41SPOT', 'TC', 'INTPRET', '(5)', line=188)
W('36,2152', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=189)
W('36,2153', 0o03442, '', '', 'TIG', kind='operand', line=190)
W('36,2154', 0o35143, '', '', 'D29.9SEC', kind='operand', line=191)
W('36,2155', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=192)
W('36,2156', 0o61104, '', '', 'INITCDUW', kind='operand', line=193)
W('36,2157', 0o45014, '', 'BOFF', 'CALL', kind='interp', line=194)
W('36,2160', 0o03347, '', '', 'MUNFLAG', kind='operand', line=195)
W('36,2161', 0o74200, '', '', 'GOMIDAV', kind='operand', line=196)
W('36,2162', 0o27043, '', '', 'CSMPREC', kind='operand', line=197)
W('36,2163', 0o64375, '', 'VLOAD', 'MXV', kind='interp', line=198)
W('36,2164', 0o00025, '', '', 'VATT1', kind='operand', line=199)
W('36,2165', 0o01734, '', '', 'REFSMMAT', kind='operand', line=200)
W('36,2166', 0o77762, '', 'VSR1', kind='interp', line=201)
W('36,2167', 0o25726, '', 'STOVL', 'V(CSM)', 'CSM VELOCITY -- M/CS*2(7)', kind='interp', line=202)
W('36,2170', 0o00017, '', '', 'RATT1', kind='operand', line=203)
W('36,2171', 0o64312, '', 'VSL4', 'MXV', kind='interp', line=204)
W('36,2172', 0o01734, '', '', 'REFSMMAT', kind='operand', line=205)
W('36,2173', 0o35720, '', 'STCALL', 'R(CSM)', 'CSM POSITION -- M*2(24)', kind='interp', line=206)
W('36,2174', 0o67130, '', '', 'MUNGRAV', kind='operand', line=207)
W('36,2175', 0o16317, '', 'STODL', 'G(CSM)', 'CSM GRAVITY VEC. -- M/CS*2(7)', kind='interp', line=208)
W('36,2176', 0o00015, '', '', 'TAT', kind='operand', line=209)
W('36,2177', 0o00041, '', 'STORE', 'TDEC1', 'RELOAD TDEC1 FOR MIDTOAV.', kind='interp', line=210)
W('36,2200', 0o77624, 'GOMIDAV', 'CALRB', kind='interp', line=211)
W('36,2201', 0o27557, '', '', 'MIDTOAV1', kind='operand', line=212)
W('36,2202', 0o12211, '', 'TCF', 'CALLT-35', 'MADE IT IN TIME.', line=213)

W('36,2203', 0o00006, '', 'EXTEND', '', 'TIG WAS SLIPPED, SO RESET TIG TO 29.9', line=215)
W('36,2204', 0o31561, '', 'DCA', 'PIPTIME1', 'SECONDS AFTER THE TIME TO WHICH WE DID', line=216)
W('36,2205', 0o53442, '', 'DXCH', 'TIG', 'INTEGRATE.', line=217)
W('36,2206', 0o00006, '', 'EXTEND', line=218)
W('36,2207', 0o33143, '', 'DCA', 'D29.9SEC', line=219)
W('36,2210', 0o21442, '', 'DAS', 'TIG', line=220)

W('36,2211', 0o52155, 'CALLT-35', 'DXCH', 'MPAC', line=222)
W('36,2212', 0o53500, '', 'DXCH', 'SAVET-30', 'DELTA-T UNTIL TIG-30', line=223)
W('36,2213', 0o00006, '', 'EXTEND', line=224)
W('36,2214', 0o43756, '', 'DCS', '5SECDP', line=225)
W('36,2215', 0o21500, '', 'DAS', 'SAVET-30', 'DELTA-T UNTIL TIG-35', line=226)
W('36,2216', 0o00006, '', 'EXTEND', line=227)
W('36,2217', 0o31500, '', 'DCA', 'SAVET-30', line=228)
W('36,2220', 0o05277, '', 'TC', 'LONGCALL', line=229)
#   EBANK= TTOGO
W('36,2221', 0o02240, '', '2CADR', 'TIG-35', kind='data', line=231)
W('36,2222', 0o74067, kind='data', line=231)

W('36,2223', 0o05353, '', 'TC', 'PHASCHNG', line=233)
W('36,2224', 0o20254, '', 'OCT', '20254', '4.25SPOT FOR TIG-35 RESTART.', kind='data', line=234)
# Page 735
W('36,2225', 0o05321, '', 'TC', 'CHECKMM', line=236)
W('36,2226', 0o00077, '', 'DEC', '63', kind='data', line=237)
W('36,2227', 0o15155, '', 'TCF', 'ENDOFJOB', 'NOT P63', line=238)
W('36,2230', 0o44762, '', 'CS', 'CNTDNDEX', 'P63 CAN START DISPLAYING NOW.', line=239)
W('36,2231', 0o55163, '', 'TS', 'DISPDEX', line=240)
W('36,2232', 0o06037, '', 'TC', 'INTPRET', line=241)
W('36,2233', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=242)
W('36,2234', 0o03553, '', '', 'VN1', kind='operand', line=243)
W('36,2235', 0o03472, '', 'STORE', 'ABVEL', 'INITIALIZE ABVEL FOR P63 DISPLAY', kind='interp', line=244)
W('36,2236', 0o77776, '', 'EXIT', kind='interp', line=245)
W('36,2237', 0o15155, '', 'TCF', 'ENDOFJOB', line=246)

# ********************************

W('36,2240', 0o33756, 'TIG-35', 'CAF', '5SEC', line=250)
W('36,2241', 0o05173, '', 'TC', 'TWIDDLE', line=251)
W('36,2242', 0o02276, '', 'ADRES', 'TIG-30', kind='data', line=252)

W('36,2243', 0o05353, '', 'TC', 'PHASCHNG', line=254)
W('36,2244', 0o40154, '', 'OCT', '40154', '4.15SPOT FOR TIG-30 RESTART', kind='data', line=255)

W('36,2245', 0o44752, '', 'CS', 'BLANKDEX', 'BLANK DSKY FOR 5 SECONDS', line=257)
W('36,2246', 0o55163, '', 'TS', 'DISPDEX', line=258)

W('36,2247', 0o51455, '', 'INDEX', 'WHICH', line=260)
W('36,2250', 0o40006, '', 'CS', '6', 'CHECK ULLAGE TIME.', line=261)
W('36,2251', 0o00006, '', 'EXTEND', line=262)
W('36,2252', 0o65261, '', 'BZMF', 'TASKOVER', line=263)
W('36,2253', 0o33145, '', 'CAF', '4.9SEC', 'SET UP TASK TO RESTORE DISPLAY AT TIG-30', line=264)
W('36,2254', 0o05173, '', 'TC', 'TWIDDLE', line=265)
W('36,2255', 0o02266, '', 'ADRES', 'TIG-30.1', kind='data', line=266)

W('36,2256', 0o35027, '', 'CAF', 'PRIO17', 'A NEGATIVE ULLAGE TIME INDICATES P41, IN', line=268)
W('36,2257', 0o05072, '', 'TC', 'NOVAC', 'WHICH CASE WE HAVE TO SET UP A JOB TO', line=269)
#   EBANK= TTOGO  # BLANK THE DSKY FOR FIVE SECONDS, SINCE
W('36,2260', 0o02263, '', '2CADR', 'P41BLANK', 'CLOKJOB IS NOT RUNNING DURING P41.', kind='data', line=271)
W('36,2261', 0o74067, kind='data', line=271)

W('36,2262', 0o15261, '', 'TCF', 'TASKOVER', line=273)

W('36,2263', 0o04616, 'P41BLANK', 'TC', 'BANKCALL', 'BLANK DSKY.', line=275)
W('36,2264', 0o20456, '', 'CADR', 'CLEANDSP', kind='data', line=276)
W('36,2265', 0o15155, '', 'TCF', 'ENDOFJOB', line=277)

W('36,2266', 0o35027, 'TIG-30.1', 'CAF', 'PRIO17', 'SET UP JOB TO RESTORE DISPLAY AT TIG-30', line=279)
W('36,2267', 0o05072, '', 'TC', 'NOVAC', line=280)
#   EBANK= TTOGO
W('36,2270', 0o02273, '', '2CADR', 'TIG-30A', kind='data', line=282)
W('36,2271', 0o74067, kind='data', line=282)

W('36,2272', 0o15261, '', 'TCF', 'TASKOVER', line=284)
# Page 736
W('36,2273', 0o33761, 'TIG-30A', 'CAF', 'V16N85B', line=286)
W('36,2274', 0o04616, '', 'TC', 'BANKCALL', 'RESTORE DISPLAY.', line=287)
W('36,2275', 0o20465, '', 'CADR', 'REGODSP', 'REGODSP DOES A TCF ENDOFJOB', kind='data', line=288)

# ********************************

W('36,2276', 0o33144, 'TIG-30', 'CAF', 'S24.9SEC', line=292)
W('36,2277', 0o05173, '', 'TC', 'TWIDDLE', line=293)
W('36,2300', 0o02352, '', 'ADRES', 'TIG-5', kind='data', line=294)

W('36,2301', 0o44762, '', 'CS', 'CNTDNDEX', 'START UP CLOKTASK AGAIN', line=296)
W('36,2302', 0o55163, '', 'TS', 'DISPDEX', line=297)

W('36,2303', 0o51455, '', 'INDEX', 'WHICH', 'PICK UP APPROPRIATE ULLAGE -- ON TIME', line=299)
W('36,2304', 0o30006, '', 'CA', '6', 'Was CAF --- RSB 2009.', line=300)
W('36,2305', 0o00006, '', 'EXTEND', line=301)
W('36,2306', 0o62325, '', 'BZMF', 'ULLGNOT', "DON'T SET UP ULLAGE IF DT IS NEG OR ZERO", line=302)
W('36,2307', 0o55477, '', 'TS', 'SAVET-30', 'SAVE DELTA-T FOR RESTART', line=303)
W('36,2310', 0o05173, '', 'TC', 'TWIDDLE', line=304)
W('36,2311', 0o02346, '', 'ADRES', 'ULLGTASK', kind='data', line=305)

W('36,2312', 0o36245, '', 'CA', 'THREE', 'RESTART PROTECT ULLGTASK (1.3SPOT)', line=307)
W('36,2313', 0o54001, '', 'TS', 'L', line=308)
W('36,2314', 0o46245, '', 'CS', 'THREE', line=309)
W('36,2315', 0o52753, '', 'DXCH', '-PHASE1', line=310)
W('36,2316', 0o40025, '', 'CS', 'TIME1', line=311)
W('36,2317', 0o55053, '', 'TS', 'TBASE1', line=312)

W('36,2320', 0o51455, '', 'INDEX', 'WHICH', line=314)
W('36,2321', 0o10001, '', 'TCF', '1', line=315)

W('36,2322', 0o40106, 'WANTAPS', 'CS', 'FLGWRD10', '(1) FOR P42 ENSURE APSFLAG IS SET.  IF IT', line=317)
W('36,2323', 0o74737, '', 'MASK', 'APSFLBIT', "WASN'T SET, DAP WILL BE INITIALIZED TO", line=318)
W('36,2324', 0o26106, '', 'ADS', 'FLGWRD10', 'ASCENT VALUES BY 1/ACCS IN 2 SECONDS.', line=319)

W('36,2325', 0o00006, 'ULLGNOT', 'EXTEND', '', '(1)', line=321)
W('36,2326', 0o51455, '', 'INDEX', 'WHICH', line=322)
W('36,2327', 0o30010, '', 'DCA', '7', 'LOAD AVEGEXIT WITH APPROPRIATE 2CADR', line=323)
W('36,2330', 0o53253, '', 'DXCH', 'AVEGEXIT', line=324)

W('36,2331', 0o34752, '', 'CAF', 'TWO', '4.2SPOT RESTARTS IMMEDIATELY AT REDO4.2', line=326)
W('36,2332', 0o54001, '', 'TS', 'L', line=327)
W('36,2333', 0o44752, '', 'CS', 'TWO', 'AND ALSO AT TIG-5 AT THE CORRECT TIME.', line=328)
W('36,2334', 0o52761, '', 'DXCH', '-PHASE4', line=329)

W('36,2335', 0o40025, '', 'CS', 'TIME1', line=331)
W('36,2336', 0o55061, '', 'TS', 'TBASE4', 'SET TBASE4 FOR TIG-5 RESTART', line=332)

W('36,2337', 0o00006, 'REDO2.17', 'EXTEND', line=334)
# Page 737
W('36,2340', 0o34755, '', 'DCA', 'NEG0', 'CLEAR OUT GROUP 2 SO LAMBERT CAN START', line=336)
W('36,2341', 0o52755, '', 'DXCH', '-PHASE2', 'IF NEEDED.', line=337)

W('36,2342', 0o10763, 'REDO4.2', 'CCS', 'PHASE5', 'IF SERVICER GOING?', line=339)
W('36,2343', 0o15261, '', 'TCF', 'TASKOVER', "YES, DON'T START IT UP AGAIN.", line=340)

W('36,2344', 0o04635, '', 'TC', 'POSTJUMP', line=342)
W('36,2345', 0o77410, '', 'CADR', 'PREREAD', 'PREREAD END THIS TASK', kind='data', line=343)

# *********************************

W('36,2346', 0o02657, 'ULLGTASK', 'TC', 'ONULLAGE', 'THIS COMES AT TIG-7.5 OR TIG-3.5', line=347)
W('36,2347', 0o05353, '', 'TC', 'PHASCHNG', line=348)
W('36,2350', 0o00001, '', 'OCT', '1', kind='data', line=349)
W('36,2351', 0o15261, '', 'TCF', 'TASKOVER', line=350)

# *********************************

W('36,2352', 0o00006, 'TIG-5', 'EXTEND', line=354)
W('36,2353', 0o34755, '', 'DCA', 'NEG0', 'INSURE THAT GROUP 3 IS INACTIVE.', line=355)
W('36,2354', 0o52757, '', 'DXCH', '-PHASE3', line=356)

W('36,2355', 0o33756, '', 'CAF', '5SEC', line=358)
W('36,2356', 0o05173, '', 'TC', 'TWIDDLE', line=359)
W('36,2357', 0o02403, '', 'ADRES', 'TIG-0', kind='data', line=360)

W('36,2360', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET IGNFLAG AND ASINFLAG', line=362)
W('36,2361', 0o00153, '', 'ADRES', 'IGNFLAG', '      FOR LIGHT-UP LOGIC.', kind='data', line=363)
W('36,2362', 0o05516, '', 'TC', 'DOWNFLAG', line=364)
W('36,2363', 0o00154, '', 'ADRES', 'ASTNFLAG', kind='data', line=365)

W('36,2364', 0o51455, '', 'INDEX', 'WHICH', line=367)
W('36,2365', 0o10011, '', 'TCF', '11', line=368)

W('36,2366', 0o10757, 'P40SJUNK', 'CCS', 'PHASE3', '(11) P40 AND P42.  S40.13 IN PROGRESS?', line=370)
W('36,2367', 0o12376, '', 'TCF', 'DISPCHNG', 'YES', line=371)

W('36,2370', 0o34736, '', 'CAF', 'PRIO20', line=373)
W('36,2371', 0o05105, '', 'TC', 'FINDVAC', line=374)
#   EBANK= TTOGO
W('36,2372', 0o02540, '', '2CADR', 'S40.13', kind='data', line=376)
W('36,2373', 0o56067, kind='data', line=376)

W('36,2374', 0o05353, '', 'TC', 'PHASCHNG', '3.5SPOT FOR S40.13', line=378)
W('36,2375', 0o00053, '', 'OCT', '00053', kind='data', line=379)
W('36,2376', 0o44760, 'DISPCHNG', 'CS', 'VB99DEX', '(11)', line=380)
W('36,2377', 0o55163, '', 'TS', 'DISPDEX', line=381)

# Page 738
W('36,2400', 0o05353, 'COMMON', 'TC', 'PHASCHNG', 'RESTART TIG-0 (4.7SPOT)', line=384)
W('36,2401', 0o40074, '', 'OCT', '40074', kind='data', line=385)
W('36,2402', 0o15261, '', 'TCF', 'TASKOVER', line=386)

# *********************************

W('36,2403', 0o40103, 'TIG-0', 'CS', 'FLAGWRD7', 'SET IGNFLAG SINCE TIG HAS ARRIVED', line=390)
W('36,2404', 0o74737, '', 'MASK', 'IGNFLBIT', line=391)
W('36,2405', 0o26103, '', 'ADS', 'FLAGWRD7', line=392)

W('36,2406', 0o05321, '', 'TC', 'CHECKMM', 'IN P63 CASE, THROTTLE-UP IS ZOOMTIME', line=394)
W('36,2407', 0o00077, '', 'DEC', '63', 'AFTER NOMINAL IGNITION, NOT ACTUAL', kind='data', line=395)
W('36,2410', 0o12421, '', 'TCF', 'IGNYET?', line=396)
W('36,2411', 0o31422, '', 'CA', 'ZOOMTIME', line=397)
W('36,2412', 0o05203, '', 'TC', 'WAITLIST', line=398)
#   EBANK= DVCNTR
W('36,2413', 0o02007, '', '2CADR', 'P63ZOOM', kind='data', line=400)
W('36,2414', 0o36067, kind='data', line=400)

W('36,2415', 0o05327, '', 'TC', '2PHSCHNG', line=402)
W('36,2416', 0o40033, '', 'OCT', '40033', kind='data', line=403)

W('36,2417', 0o05014, '', 'OCT', '05014', kind='data', line=405)
W('36,2420', 0o77777, '', 'OCT', '77777', kind='data', line=406)

W('36,2421', 0o34740, 'IGNYET?', 'CAF', 'ASTNBIT', 'CHECK ASTNFLAG:  HAS ASTRONAUT RESPONDED', line=408)
W('36,2422', 0o70103, '', 'MASK', 'FLAGWRD7', 'TO OUR ENGINE ENABLE REQUEST?', line=409)
W('36,2423', 0o00006, '', 'EXTEND', line=410)
W('36,2424', 0o51455, '', 'INDEX', 'WHICH', line=411)
W('36,2425', 0o10012, '', 'BZF', '12', 'BRANCH IF HE HAS NOT RESPONDED YET', line=412)

W('36,2426', 0o40101, 'IGNITION', 'CS', 'FLAGWRD5', 'INSURE ENGONFLG IS SET.', line=414)
W('36,2427', 0o74745, '', 'MASK', 'ENGONBIT', line=415)
W('36,2430', 0o26101, '', 'ADS', 'FLAGWRD5', line=416)
W('36,2431', 0o44355, '', 'CS', 'PRIO30', 'TURN ON THE ENGINE.', line=417)
W('36,2432', 0o00006, '', 'EXTEND', line=418)
W('36,2433', 0o02011, '', 'RAND', 'DSALMOUT', line=419)
W('36,2434', 0o64737, '', 'AD', 'BIT13', line=420)
W('36,2435', 0o00006, '', 'EXTEND', line=421)
W('36,2436', 0o01011, '', 'WRITE', 'DSALMOUT', line=422)
W('36,2437', 0o00006, '', 'EXTEND', '', 'SET TEVENT FOR DOWNLINK', line=423)
W('36,2440', 0o30025, '', 'DCA', 'TIME2', line=424)
W('36,2441', 0o53345, '', 'DXCH', 'TEVENT', line=425)

W('36,2442', 0o00006, '', 'EXTEND', '', 'UPDATE TIG USING TGO FROM S40.13', line=427)
W('36,2443', 0o31517, '', 'DCA', 'TGO', line=428)
W('36,2444', 0o53442, '', 'DXCH', 'TIG', line=429)
W('36,2445', 0o00006, '', 'EXTEND', line=430)
W('36,2446', 0o30025, '', 'DCA', 'TIME2', line=431)
W('36,2447', 0o21442, '', 'DAS', 'TIG', line=432)

# Page 739
W('36,2450', 0o44742, '', 'CS', 'FLUNDBIT', 'PERMIT GUIDANCE LOOP DISPLAYS', line=435)
W('36,2451', 0o70104, '', 'MASK', 'FLAGWRD8', line=436)
W('36,2452', 0o54104, '', 'TS', 'FLAGWRD8', line=437)

W('36,2453', 0o51455, '', 'INDEX', 'WHICH', line=439)
W('36,2454', 0o10013, '', 'TCF', '13', line=440)

W('36,2455', 0o00006, 'P63IGN', 'EXTEND', '', '(13)  INITIATE BURN DISPLAYS', line=442)
W('36,2456', 0o33137, '', 'DCA', 'DSP2CADR', line=443)
W('36,2457', 0o53253, '', 'DXCH', 'AVGEXIT', line=444)

W('36,2460', 0o30005, '', 'CA', 'Z', 'ASSASSINATE CLOKTASK', line=446)
W('36,2461', 0o55163, '', 'TS', 'DISPDEX', line=447)

W('36,2462', 0o40105, '', 'CS', 'FLAGWRD9', 'SET FLAG FOR P70-P71', line=449)
W('36,2463', 0o74743, '', 'MASK', 'LETABBIT', line=450)
W('36,2464', 0o26105, '', 'ADS', 'FLAGWRD9', line=451)

W('36,2465', 0o40103, '', 'CS', 'FLAGWRD7', 'SET SWANDISP TO ENABLE R10.', line=453)
W('36,2466', 0o74741, '', 'MASK', 'SWANDBIT', line=454)
W('36,2467', 0o26103, '', 'ADS', 'FLAGWRD7', line=455)

W('36,2470', 0o44735, '', 'CS', 'PULSES', 'MAKE SURE DAP IS NOT IN MINIMUM-IMPULSE', line=457)
W('36,2471', 0o70111, '', 'MASK', 'DAPBOOLS', 'MODE, IN CASE OF SWITCH TO P66', line=458)
W('36,2472', 0o54111, '', 'TS', 'DAPBOOLS', line=459)

W('36,2473', 0o00006, '', 'EXTEND', '', 'INITIALIZE TIG FOR P70 AND P71.', line=461)
W('36,2474', 0o30025, '', 'DCA', 'TIME2', line=462)
W('36,2475', 0o53442, '', 'DXCH', 'TIG', line=463)

W('36,2476', 0o34755, '', 'CAF', 'ZERO', 'INITIALIZE WCHPHASE, AND FLPASS0', line=465)
W('36,2477', 0o55351, '', 'TS', 'WCHPHASE', line=466)
W('36,2500', 0o55621, '', 'TS', 'WCHPHOLD', 'ALSO WHCPHOLD', line=467)
W('36,2501', 0o34752, '', 'CA', 'TWO', line=468)
W('36,2502', 0o55623, '', 'TS', 'FLPASS0', line=469)

W('36,2503', 0o12541, '', 'TCF', 'P42IGN', line=471)
W('36,2504', 0o40101, 'P40IGN', 'CS', 'FLAGWRD5', '(13)', line=472)
W('36,2505', 0o74740, '', 'MASK', 'NOTHRBIT', line=473)
W('36,2506', 0o00006, '', 'EXTEND', line=474)
W('36,2507', 0o12541, '', 'BZF', 'P42IGN', line=475)
W('36,2510', 0o31422, '', 'CA', 'ZOOMTIME', line=476)
W('36,2511', 0o05203, '', 'TC', 'WAITLIST', line=477)
#   EBANK= DVCNTR
W('36,2512', 0o02015, '', '2CADR', 'P40ZOOM', kind='data', line=479)
W('36,2513', 0o36067, kind='data', line=479)

W('36,2514', 0o05327, 'P63IGN1', 'TC', '2PHSCHNG', line=481)
W('36,2515', 0o40033, '', 'OCT', '40033', '3.3SPOT FOR ZOOM RESTART.', kind='data', line=482)
W('36,2516', 0o05014, '', 'OCT', '05014', 'TYPE C RESTARTS HERE IMMEDIATELY', kind='data', line=483)
W('36,2517', 0o77777, '', 'OCT', '77777', kind='data', line=484)

# Page 740
W('36,2520', 0o12541, '', 'TCF', 'P42IGN', line=487)
W('36,2521', 0o35015, 'P12IGN', 'CAF', 'EBANK6', line=488)
W('36,2522', 0o54003, '', 'TS', 'EBANK', line=489)
#   EBANK= AOSQ

W('36,2523', 0o31412, '', 'CA', 'IGNAOSQ', 'INITIALIZE DAP BIAS ACCELERATION', line=492)
W('36,2524', 0o55537, '', 'TS', 'AOSQ', 'ESTIMATES AT P12 IGNITION.', line=493)
W('36,2525', 0o31413, '', 'CA', 'IGNAOSR', line=494)
W('36,2526', 0o55541, '', 'TS', 'AOSR', line=495)

W('36,2527', 0o35016, '', 'CAF', 'EBANK7', line=497)
W('36,2530', 0o54003, '', 'TS', 'EBANK', line=498)
#   EBANK= DVCNTR

W('36,2531', 0o30005, 'ABRTIGN', 'CA', 'Z', '(13) KILL CLOKTASK', line=501)
W('36,2532', 0o55163, '', 'TS', 'DISPDEX', line=502)

W('36,2533', 0o00006, '', 'EXTEND', '', 'CONNECT ASCENT GYIDANCE TO SERVICER.', line=504)
W('36,2534', 0o33141, '', 'DCA', 'ATMAGADR', line=505)
W('36,2535', 0o53253, '', 'DXCH', 'AVGEXIT', line=506)

W('36,2536', 0o40103, '', 'CS', 'FLAGWRD7', 'ENABLE R10.', line=508)
W('36,2537', 0o74741, '', 'MASK', 'SWANDBIT', line=509)
W('36,2540', 0o26103, '', 'ADS', 'FLAGWRD7', line=510)

W('36,2541', 0o44744, 'P42IGN', 'CS', 'DRIFTBIT', 'ENSURE THAT POWERED-FLIGHT SWITCHING', line=512)
W('36,2542', 0o70111, '', 'MASK', 'DAPBOOLS', 'CURVES ARE USED.', line=513)
W('36,2543', 0o54111, '', 'TS', 'DAPBOOLS', line=514)
W('36,2544', 0o34743, '', 'CAF', 'IMPULBIT', 'EXAMINE IMPULSE SWITCH', line=515)
W('36,2545', 0o70076, '', 'MASK', 'FLAGWRD2', line=516)
W('36,2546', 0o10000, '', 'CCS', 'A', line=517)
W('36,2547', 0o13522, '', 'TCF', 'IMPLBURN', line=518)

W('36,2550', 0o05516, 'DVMONCON', 'TC', 'DOWNFLAG', line=520)
W('36,2551', 0o00153, '', 'ADRES', 'IGNFLAG', 'CONNECT DVMON', kind='data', line=521)
W('36,2552', 0o05516, '', 'TC', 'DOWNFLAG', line=522)
W('36,2553', 0o00154, '', 'ADRES', 'ASTNFLAG', kind='data', line=523)
W('36,2554', 0o05516, '', 'TC', 'DOWNFLAG', line=524)
W('36,2555', 0o00161, '', 'ADRES', 'IDLEFLAG', kind='data', line=525)

W('36,2556', 0o05353, '', 'TC', 'PHASCHNG', line=527)
W('36,2557', 0o40054, '', 'OCT', '40054', kind='data', line=528)

W('36,2560', 0o05221, '', 'TC', 'FIXDELAY', 'TURN ULLAGE OFF HALF A SECOND AFTER', line=530)
W('36,2561', 0o00062, '', 'DEC', '50', 'LIGHT UP.', kind='data', line=531)

W('36,2562', 0o02653, 'ULLAGOFF', 'TC', 'NOULLAGE', line=533)

W('36,2563', 0o00006, 'WAITABIT', 'EXTEND', '', 'KILL GROUP 4', line=535)
W('36,2564', 0o34755, '', 'DCA', 'NEG0', line=536)
# Page 741
W('36,2565', 0o52761, '', 'DXCH', '-PHASE4', line=538)

W('36,2566', 0o15261, '', 'TCF', 'TASKOVER', line=540)

W('36,2567', 0o04635, 'TIGTASK', 'TC', 'POSTJUMP', '(12)', line=542)
W('36,2570', 0o36000, '', 'CADR', 'TIGTASK1', kind='data', line=543)

# ********************************

#   BANK 31
#   SETLOC P40S3
#   BANK
#   COUNT* $$/P40

W('17,2000', 0o35026, 'TIGTASK1', 'CAF', 'PRIO16', line=552)
W('17,2001', 0o05072, '', 'TC', 'NOVAC', line=553)
#   EBANK= TRKMKCNT
W('17,2002', 0o03241, '', '2CADR', 'TIGNOW', kind='data', line=555)
W('17,2003', 0o74067, kind='data', line=555)

W('17,2004', 0o05353, '', 'TC', 'PHASCHNG', line=557)
W('17,2005', 0o00006, '', 'OCT', '6', 'KILL GROUP 6', kind='data', line=558)

W('17,2006', 0o15261, '', 'TCF', 'TASKOVER', line=560)

# ********************************

W('17,2007', 0o00006, 'P63ZOOM', 'EXTEND', line=564)
W('17,2010', 0o32026, '', 'DCA', 'LUNLANAD', line=565)
W('17,2011', 0o53253, '', 'DXCH', 'AVEGEXIT', line=566)

W('17,2012', 0o04674, '', 'TC', 'IBNKCALL', line=568)
W('17,2013', 0o62370, '', 'CADR', 'FLATOUT', kind='data', line=569)
W('17,2014', 0o12022, '', 'TCF', 'P40ZOOMA', line=570)

W('17,2015', 0o34737, 'P40ZOOM', 'CAF', 'BIT13', line=572)
W('17,2016', 0o54055, '', 'TS', 'THRUST', line=573)
W('17,2017', 0o34750, '', 'CAF', 'BIT4', line=574)

W('17,2020', 0o00006, '', 'EXTEND', line=576)
W('17,2021', 0o05014, '', 'WOR', 'CHAN14', line=577)

W('17,2022', 0o05353, 'P40ZOOMA', 'TC', 'PHASCHNG', line=579)
W('17,2023', 0o00003, '', 'OCT', '3', kind='data', line=580)
W('17,2024', 0o15261, '', 'TCF', 'TASKOVER', line=581)

#   EBANK= DVCNTR
W('17,2025', 0o02462, 'LUNLANAD', '2CADR', 'LUNLAND', kind='data', line=584)
W('17,2026', 0o62067, kind='data', line=584)

# Page 742
S('ZOOM', 'equals', 0o46022, line=587)
#   BANK 36
#   SETLOC P40S
#   BANK
#   COUNT* $$/P40

# ********************************

W('36,2571', 0o05504, 'COMFAIL', 'TC', 'UPFLAG', '(15)', line=595)
W('36,2572', 0o00161, '', 'ADRES', 'IDLEFLAG', kind='data', line=596)
W('36,2573', 0o05504, '', 'TC', 'UPFLAG', 'SET FLAG TO SUPPRESS CONFLICTING DISPLAY', line=597)
W('36,2574', 0o00175, '', 'ADRES', 'FLUNDISP', kind='data', line=598)
W('36,2575', 0o34751, '', 'CAF', 'FOUR', 'RESET DVMON', line=599)
W('36,2576', 0o55515, '', 'TS', 'DVCNTR', line=600)
W('36,2577', 0o10765, '', 'CCS', 'PHASE6', 'CLOCKTASK ACTIVE?', line=601)
W('36,2600', 0o12603, '', 'TCF', '+3', 'YES', line=602)
W('36,2601', 0o04616, '', 'TC', 'BANKCALL', 'OTHERWISE, START IT UP', line=603)
W('36,2602', 0o74663, '', 'CADR', 'STCLOK1', kind='data', line=604)
W('36,2603', 0o44765, '', 'CS', 'VB97DEX', line=605)
W('36,2604', 0o55163, '', 'TS', 'DISPDEX', line=606)
W('36,2605', 0o05353, '', 'TC', 'PHASCHNG', 'TURN OFF GROUP 4.', line=607)
W('36,2606', 0o00004, '', 'OCT', '00004', kind='data', line=608)
W('36,2607', 0o15155, '', 'TCF', 'ENDOFJOB', line=609)

W('36,2610', 0o51455, 'COMFAIL1', 'INDEX', 'WHICH', line=611)
W('36,2611', 0o10002, '', 'TCF', '2', line=612)

W('36,2612', 0o30005, 'COMFAIL3', 'CA', 'Z', '(15)  KILL CLOKTASK USING Z', line=614)
W('36,2613', 0o12615, '', 'TCF', '+2', line=615)

W('36,2614', 0o44762, 'COMFAIL4', 'CS', 'CNTDNDEX', line=617)
W('36,2615', 0o55163, '', 'TS', 'DISPDEX', line=618)

W('36,2616', 0o05516, '', 'TC', 'DOWNFLAG', 'RECONNECT DV MONITOR', line=620)
W('36,2617', 0o00161, '', 'ADRES', 'IDLEFLAG', kind='data', line=621)
W('36,2620', 0o05516, '', 'TC', 'DOWNFLAG', 'PERMIT GUIDANCE LOOP DISPLAYS', line=622)
W('36,2621', 0o00175, '', 'ADRES', 'FLUNDISP', kind='data', line=623)
W('36,2622', 0o15155, '', 'TCF', 'ENDOFJOB', line=624)

W('36,2623', 0o05353, 'COMFAIL2', 'TC', 'PHASCHNG', 'KILL ZOOM RESTART PROTECTION', line=626)
W('36,2624', 0o00003, '', 'OCT', '00003', kind='data', line=627)

W('36,2625', 0o00004, '', 'INHINT', line=629)
W('36,2626', 0o06027, '', 'TC', 'KILLTASK', "KILL ZOOM IN CASE IT'S STILL TO COME", line=630)
W('36,2627', 0o36022, '', 'CADR', 'ZOOM', kind='data', line=631)
W('36,2630', 0o04674, '', 'TC', 'IBNKCALL', 'COMMAND ENGINE OFF', line=632)
W('36,2631', 0o75561, '', 'CADR', 'ENGINOF4', kind='data', line=633)
W('36,2632', 0o05504, '', 'TC', 'UPFLAG', 'SET THE DRIFT BIT FOR THE DAP.', line=634)
W('36,2633', 0o00312, '', 'ADRES', 'DRIFTDFL', kind='data', line=635)
# Page 743
W('36,2634', 0o02645, '', 'TC', 'INVFLAG', 'USE OTHER RCS SYSTEM', line=637)
W('36,2635', 0o00310, '', 'ADRES', 'AORBTFLG', kind='data', line=638)
W('36,2636', 0o05504, '', 'TC', 'UPFLAG', 'TURN ON ULLAGE', line=639)
W('36,2637', 0o00314, '', 'ADRES', 'ULLAGFLG', kind='data', line=640)
W('36,2640', 0o34753, '', 'CAF', 'BIT1', line=641)
W('36,2641', 0o00004, '', 'INHINT', line=642)
W('36,2642', 0o05173, '', 'TC', 'TWIDDLE', line=643)
W('36,2643', 0o02352, '', 'ADRES', 'TIG-5', kind='data', line=644)
W('36,2644', 0o15155, '', 'TCF', 'ENDOFJOB', line=645)

# ***********************************
# SUBROUTINES OF THE IGNITION ROUTINE
# ***********************************

W('36,2645', 0o30002, 'INVFLAG', 'CA', 'Q', line=651)
W('36,2646', 0o05522, '', 'TC', 'DEBIT', line=652)
W('36,2647', 0o40000, '', 'COM', line=653)
W('36,2650', 0o00006, '', 'EXTEND', line=654)
W('36,2651', 0o06001, '', 'RXOR', 'LCHAN', line=655)
W('36,2652', 0o15511, '', 'TCF', 'COMFLAG', line=656)

# ***********************************

W('36,2653', 0o44746, 'NOULLAGE', 'CS', 'ULLAGER', 'MUST BE CALLED IN A TASK OR UNDER INHINT', line=660)
W('36,2654', 0o70111, '', 'MASK', 'DAPBOOLS', line=661)
W('36,2655', 0o54111, '', 'TS', 'DAPBOOLS', line=662)
W('36,2656', 0o00002, '', 'TC', 'Q', line=663)

# ***********************************

W('36,2657', 0o40111, 'ONULLAGE', 'CS', 'DAPBOOLS', 'TURN ON ULLAGE.  MUST BE CALLED IN', line=667)
W('36,2660', 0o74746, '', 'MASK', 'ULLAGER', 'A TASK OR WHILE INHINTED.', line=668)
W('36,2661', 0o26111, '', 'ADS', 'DAPBOOLS', line=669)
W('36,2662', 0o00002, '', 'TC', 'Q', line=670)

# ***********************************

W('36,2663', 0o34755, 'STCLOK1', 'CA', 'ZERO', 'THIS ROUTINE STARTS THE COUNT-DOWN', line=674)
W('36,2664', 0o55163, 'STCLOK2', 'TS', 'DISPDEX', '(CLOKTASK AND CLOKJOB).  SETTING', line=675)
W('36,2665', 0o04645, 'STCLOK3', 'TC', 'MAKECADR', 'SETTING DISPDEX POSITIVE KILLS IT.', line=676)
W('36,2666', 0o55061, '', 'TS', 'TBASE4', 'RETURN SAVE (NOT FOR RESTARTS).', line=677)
W('36,2667', 0o00006, '', 'EXTEND', line=678)
W('36,2670', 0o31442, '', 'DCA', 'TIG', line=679)
W('36,2671', 0o52155, '', 'DXCH', 'MPAC', line=680)
W('36,2672', 0o00006, '', 'EXTEND', line=681)
W('36,2673', 0o40025, '', 'DCS', 'TIME2', line=682)
# Page 744
W('36,2674', 0o20155, '', 'DAS', 'MPAC', 'HAVE TIG -- TIME2, UNDOUBTEDLY A + NUMBER', line=684)
W('36,2675', 0o07257, '', 'TC', 'TPAGREE', 'POSITIVE, SINCE WE PASSED THE', line=685)
W('36,2676', 0o34777, '', 'CAF', '1SEC', '45 SECOND CHECK.', line=686)
W('36,2677', 0o54002, '', 'TS', 'Q', line=687)
W('36,2700', 0o52155, '', 'DXCH', 'MPAC', line=688)
W('36,2701', 0o74346, '', 'MASK', 'LOW5', 'RESTRICT MAGNITUDE OF NUMBER IN A', line=689)
W('36,2702', 0o00006, '', 'EXTEND', line=690)
W('36,2703', 0o10002, '', 'DV', 'Q', line=691)
W('36,2704', 0o30001, '', 'CA', 'L', 'GET REMAINDER', line=692)
W('36,2705', 0o64752, '', 'AD', 'TWO', line=693)
W('36,2706', 0o00004, '', 'INHINT', line=694)
W('36,2707', 0o05173, '', 'TC', 'TWIDDLE', line=695)
W('36,2710', 0o02717, '', 'ADRES', 'CLOKTASK', kind='data', line=696)
W('36,2711', 0o05327, '', 'TC', '2PHSCHNG', line=697)
W('36,2712', 0o40036, '', 'OCT', '40036', '6.3SPOT FOR CLOKTASK', kind='data', line=698)
W('36,2713', 0o05024, '', 'OCT', '05024', kind='data', line=699)
W('36,2714', 0o13000, '', 'OCT', '13000', kind='data', line=700)

W('36,2715', 0o31061, '', 'CA', 'TBASE4', line=702)
W('36,2716', 0o04640, '', 'TC', 'BANKJUMP', line=703)

W('36,2717', 0o40025, 'CLOKTASK', 'CS', 'TIME1', 'SET TBASE6 FOR GROUP 6 RESTART', line=705)
W('36,2720', 0o55065, '', 'TS', 'TBASE6', line=706)

W('36,2721', 0o11163, '', 'CCS', 'DISPDEX', line=708)
W('36,2722', 0o12733, '', 'TCF', 'KILLCLOK', line=709)
W('36,2723', 0o12724, '', 'NOOP', line=710)
W('36,2724', 0o37715, '', 'CAF', 'PRIO27', line=711)
W('36,2725', 0o05072, '', 'TC', 'NOVAC', line=712)
#   EBANK= TTOGO
W('36,2726', 0o02737, '', '2CADR', 'CLOKJOB', kind='data', line=714)
W('36,2727', 0o74067, kind='data', line=714)

W('36,2730', 0o05221, '', 'TC', 'FIXDELAY', 'WAIT A SECOND BEFORE STARTING OVER', line=716)
W('36,2731', 0o00144, '', 'DEC', '100', kind='data', line=717)
W('36,2732', 0o12717, '', 'TCF', 'CLOKTASK', line=718)

W('36,2733', 0o00006, 'KILLCLOK', 'EXTEND', '', 'KILL RESTART', line=720)
W('36,2734', 0o34755, '', 'DCA', 'NEG0', line=721)
W('36,2735', 0o52765, '', 'DXCH', '-PHASE6', line=722)
W('36,2736', 0o15261, '', 'TCF', 'TASKOVER', line=723)

W('36,2737', 0o00006, 'CLOKJOB', 'EXTEND', line=725)
W('36,2740', 0o41442, '', 'DCS', 'TIG', line=726)
W('36,2741', 0o53454, '', 'DXCH', 'TTOGO', line=727)
W('36,2742', 0o00006, '', 'EXTEND', line=728)
# Page 745
W('36,2743', 0o30025, '', 'DCA', 'TIME2', line=730)
W('36,2744', 0o21454, '', 'DAS', 'TTOGO', line=731)
W('36,2745', 0o00004, '', 'INHINT', line=732)
W('36,2746', 0o11163, '', 'CCS', 'DISPDEX', 'IF DISPDEX HAS BEEN SET POSITIVE BY A', line=733)
W('36,2747', 0o15155, '', 'TCF', 'ENDOFJOB', 'TASK OR A HIGHER PRIORITY JOB SINCE THE', line=734)
W('36,2750', 0o15155, '', 'TCF', 'ENDOFJOB', 'LAST CLOKTASK, AVOID USING IT AS AN', line=735)
W('36,2751', 0o40000, '', 'COM', '', 'INDEX.', line=736)
W('36,2752', 0o00003, '', 'RELINT', '', '***** DISPDEX MUST NEVER B -0 *****', line=737)
W('36,2753', 0o50000, '', 'INDEX', 'A', line=738)
W('36,2754', 0o13011, '', 'TCF', 'DISPNOT -1', '(-1 DUE TO EFFECT OF CCS)', line=739)

S('VB97DEX', 'equals', 0o4765, line=741)  # NEGATIVE OF THIS IS PROPER FOR DISPDEX

W('36,2755', 0o44755, '', 'CS', 'ZERO', 'INDICATE VERB 97 PASTE', line=743)
W('36,2756', 0o55067, '', 'TS', 'NVWORD1', line=744)
W('36,2757', 0o30371, '', 'CA', 'NVWORD +2', 'NVWORD+2 CONTAINS V06 & APPROPRIATE NOUN', line=745)
W('36,2760', 0o04616, '', 'TC', 'BANKCALL', line=746)
W('36,2761', 0o20473, '', 'CADR', 'CLOCPLAY', kind='data', line=747)
W('36,2762', 0o13013, '', 'TCF', 'STOPCLOK', 'TERMINATE CLOKTASK ON THE WAY TO POOH', line=748)
W('36,2763', 0o12610, '', 'TCF', 'COMFAIL1', line=749)
W('36,2764', 0o12623, '', 'TCF', 'COMFAIL2', line=750)

# THIS DISPLAY IS CALLED VIA ASTNCLOK
W('36,2765', 0o33146, '', 'CAF', 'V06N61', 'IT IS PRIMARILY USED BY THE CREW IN P63', line=753)
W('36,2766', 0o04616, '', 'TC', 'BANKCALL', 'TO RESET HIS EVENT TIMER TO AGREE WITH', line=754)
W('36,2767', 0o20457, '', 'CADR', 'REFLASH', 'TIG.', kind='data', line=755)
W('36,2770', 0o13013, '', 'TCF', 'STOPCLOK', line=756)
W('36,2771', 0o13030, '', 'TCF', 'ASTNRETN', line=757)
W('36,2772', 0o12764, '', 'TCF', '-6', line=758)

S('CNTDNDEX', 'equals', 0o4762, line=760)  # OCT17:  NEGATIVE PROPER FOR DISPDEX

W('36,2773', 0o51455, '', 'INDEX', 'WHICH', 'THIS DISPLAY COMES UP AT ONE SECOND', line=762)
# Was CAF --- RSB 2009
W('36,2774', 0o30000, '', 'CA', '0', 'INTERVALS.  IT IS NORMALLY OPERATED', line=764)
W('36,2775', 0o04616, '', 'TC', 'BANKCALL', 'BETWEEN TIG-30 SECONDS AND TIG-5 SECONDS', line=765)
W('36,2776', 0o20465, '', 'CADR', 'REGODSP', 'REGODSP DOES ITS OWN TCF ENDOFJOB', kind='data', line=766)

S('VB99DEX', 'equals', 0o4760, line=768)  # OCT13:  NEGATIVE PROPER FOR DISPDEX

S('V99RECYC', 'equals', 0o104777, line=770)

W('36,2777', 0o44743, '', 'CS', 'BIT9', 'INDICATE VERB 99 PASTE', line=772)
W('36,3000', 0o55067, '', 'TS', 'NVWORD1', line=773)
W('36,3001', 0o51455, '', 'INDEX', 'WHICH', 'THIS IS THE "PLEASE ENABLE ENGINE"', line=774)
# Was CAF --- RSB 2004
W('36,3002', 0o30000, '', 'CA', '0', 'DISPLAY; IT IS INITIATED AT TIG-5 SEC.', line=776)
W('36,3003', 0o04616, '', 'TC', 'BANKCALL', 'THE DISPLAY IS A V99NXX, WHERE XX IS', line=777)
W('36,3004', 0o20473, '', 'CADR', 'CLOCPLAY', 'NOUN THAT HAD PREVIOUSLY BEEN DISPLAYED', kind='data', line=778)
W('36,3005', 0o13013, '', 'TCF', 'STOPCLOK', 'TERMINATE GOTOPOOH TURNS OFF ULLAGE.', line=779)
W('36,3006', 0o13041, '', 'TCF', '*PROCEED', line=780)
W('36,3007', 0o13044, '', 'TCF', '*ENTER', line=781)

# Page 746
S('BLANKDEX', 'equals', 0o4752, line=784)  # NEGATIVE OF THIS IS PROPER FOR DISPDEX

W('36,3010', 0o04616, '', 'TC', 'BANKCALL', 'BLANK DSKY.  THE DSKY IS BLANKED FOR', line=786)
W('36,3011', 0o20456, '', 'CADR', 'CLEANDSP', '5 SECONDS AT TIG-35 TO INDICATE THAT', kind='data', line=787)
W('36,3012', 0o15155, 'DISPNOT', 'TCF', 'ENDOFJOB', 'AVERAGE G IS STARTING.', line=788)

W('36,3013', 0o03015, 'STOPCLOK', 'TC', 'NULLCLOK', 'STOP CLOKTASK & TURN OFF ULLAGE ON THE', line=790)
W('36,3014', 0o16001, '', 'TCF', 'GOTOPOOH', 'WAY TO P00 (GOTOPOOH RELINTS)', line=791)

W('36,3015', 0o00004, 'NULLCLOK', 'INHINT', line=793)
W('36,3016', 0o00006, '', 'EXTEND', line=794)
W('36,3017', 0o23142, '', 'QXCH', 'P40/RET', line=795)
W('36,3020', 0o02653, '', 'TC', 'NOULLAGE', 'TURN OFF ULLAGE ...', line=796)
W('36,3021', 0o06027, '', 'TC', 'KILLTASK', "      DON'T LET IT COME ON, EITHER ...", line=797)
W('36,3022', 0o74346, '', 'CADR', 'ULLGTASK', kind='data', line=798)
W('36,3023', 0o05353, '', 'TC', 'PHASCHNG', "              NOT EVEN IF THERE'S A RESTART.", line=799)
W('36,3024', 0o00001, '', 'OCT', '1', kind='data', line=800)
W('36,3025', 0o30005, '', 'CA', 'Z', 'KILL CLOKTASK', line=801)
W('36,3026', 0o55163, '', 'TS', 'DISPDEX', line=802)
W('36,3027', 0o01142, '', 'TC', 'P40/RET', line=803)

W('36,3030', 0o05353, 'ASTNRETN', 'TC', 'PHASCHNG', line=805)
W('36,3031', 0o04024, '', 'OCT', '04024', kind='data', line=806)
W('36,3032', 0o34755, '', 'CAF', 'ZERO', 'STOP DISPLAYING BUT KEEP RUNNING', line=807)
W('36,3033', 0o55163, '', 'TS', 'DISPDEX', line=808)
W('36,3034', 0o35023, '', 'CAF', 'PRIO13', line=809)
W('36,3035', 0o05105, '', 'TC', 'FINDVAC', line=810)
#   EBANK= STARIND
W('36,3036', 0o03210, '', '2CADR', 'ASTNRET', kind='data', line=812)
W('36,3037', 0o64065, kind='data', line=812)

W('36,3040', 0o15155, '', 'TCF', 'ENDOFJOB', line=814)

W('36,3041', 0o05504, '*PROCEED', 'TC', 'UPFLAG', line=816)
W('36,3042', 0o00154, '', 'ADRES', 'ASTNFLAG', kind='data', line=817)

W('36,3043', 0o13102, '', 'TCF', 'IGNITE', line=819)

W('36,3044', 0o00004, '*ENTER', 'INHINT', line=821)
W('36,3045', 0o51455, '', 'INDEX', 'WHICH', line=822)
W('36,3046', 0o10003, '', 'TCF', '3', line=823)

W('36,3047', 0o34644, 'GOPOST', 'CAF', 'PRIO12', '(3) MUST BE LOWER PRIORITY THAN CLOKJOB', line=825)
W('36,3050', 0o05105, '', 'TC', 'FINDVAC', line=826)
#   EBANK= TTOGO
W('36,3051', 0o03223, '', '2CADR', 'POSTBURN', kind='data', line=828)
W('36,3052', 0o74067, kind='data', line=828)

# Page 747
W('36,3053', 0o00004, '', 'INHINT', '', 'SET UP THE DAP FOR COASTING FLIGHT.', line=831)
W('36,3054', 0o04674, '', 'TC', 'IBNKCALL', line=832)
W('36,3055', 0o40204, '', 'CADR', 'ALLCOAST', kind='data', line=833)
W('36,3056', 0o03015, '', 'TC', 'NULLCLOK', line=834)
W('36,3057', 0o05353, '', 'TC', 'PHASCHNG', '4.13 RESTART FOR POSTBURN', line=835)
W('36,3060', 0o00134, '', 'OCT', '00134', kind='data', line=836)

W('36,3061', 0o15155, '', 'TCF', 'ENDOFJOB', line=838)

W('36,3062', 0o35027, 'GOCUTOFF', 'CAF', 'PRIO17', '(3)', line=840)
W('36,3063', 0o05105, '', 'TC', 'FINDVAC', line=841)
#   EBANK= TGO
W('36,3064', 0o02424, '', '2CADR', 'CUTOFF', kind='data', line=843)
W('36,3065', 0o30067, kind='data', line=843)

W('36,3066', 0o05516, '', 'TC', 'DOWNFLAG', line=845)
W('36,3067', 0o00175, '', 'ADRES', 'FLUNDISP', kind='data', line=846)

W('36,3070', 0o00004, '', 'INHINT', '', 'SET UP THE DAP FOR COASTING FLIGHT.', line=848)
W('36,3071', 0o04674, '', 'TC', 'IBNKCALL', line=849)
W('36,3072', 0o40204, '', 'CADR', 'ALLCOAST', kind='data', line=850)
W('36,3073', 0o03015, '', 'TC', 'NULLCLOK', line=851)
W('36,3074', 0o05353, '', 'TC', 'PHASCHNG', line=852)
W('36,3075', 0o07024, '', 'OCT', '07024', kind='data', line=853)
W('36,3076', 0o17000, '', 'OCT', '17000', kind='data', line=854)
#   EBANK= TGO
W('36,3077', 0o02424, '', '2CADR', 'CUTOFF', kind='data', line=856)
W('36,3100', 0o30067, kind='data', line=856)

W('36,3101', 0o15155, '', 'TCF', 'ENDOFJOB', line=858)

W('36,3102', 0o40103, 'IGNITE', 'CS', 'FLAGWRD7', '(2)', line=860)
W('36,3103', 0o74737, '', 'MASK', 'IGNFLBIT', line=861)
W('36,3104', 0o10000, '', 'CCS', 'A', line=862)
W('36,3105', 0o13116, '', 'TCF', 'IGNITE1', line=863)
W('36,3106', 0o34753, '', 'CAF', 'BIT1', line=864)
W('36,3107', 0o00004, '', 'INHINT', line=865)
W('36,3110', 0o05173, '', 'TC', 'TWIDDLE', line=866)
W('36,3111', 0o02426, '', 'ADRES', 'IGNITION', kind='data', line=867)

W('36,3112', 0o34360, '', 'CAF', 'OCT23', 'IMMEDIATE RESTART AT IGNITION', line=869)
W('36,3113', 0o54001, '', 'TS', 'L', line=870)
W('36,3114', 0o40000, '', 'COM', line=871)
W('36,3115', 0o52761, '', 'DXCH', '-PHASE4', line=872)

W('36,3116', 0o44762, 'IGNITE1', 'CS', 'CNTDNDEX', 'RESTORE OLD DISPLAY.', line=874)
W('36,3117', 0o55163, '', 'TS', 'DISPDEX', line=875)

W('36,3120', 0o15155, '', 'TCF', 'ENDOFJOB', line=877)

# Page 748
# ********************************

W('36,3121', 0o05567, 'P40ALM', 'TC', 'ALARM', 'PROGRAM SELECTION NOT CONSISTENT WITH', line=882)
W('36,3122', 0o01706, '', 'OCT', '1706', 'VEHICLE CONFIGURATION', kind='data', line=883)

W('36,3123', 0o35006, 'REP40ALM', 'CAF', 'V05N09', '(14)', line=885)
W('36,3124', 0o04616, '', 'TC', 'BANKCALL', line=886)
W('36,3125', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=887)

W('36,3126', 0o16001, '', 'TCF', 'GOTOPOOH', 'V34E          TERMINATE', line=889)
W('36,3127', 0o13131, '', 'TCF', '+2', 'PROCEED       CHECK FOR P42', line=890)
W('36,3130', 0o13123, '', 'TCF', 'REP40ALM', 'V32E          REDISPLAY ALARM', line=891)

W('36,3131', 0o51455, '', 'INDEX', 'WHICH', 'FOR P42, ALLOW CREW TO PROCEED EVEN', line=893)
W('36,3132', 0o10014, '', 'TCF', '14', 'THOUGH VEHICLE IS UNSTAGED.', line=894)

# ********************************

#   BANK 31
#   SETLOC P40S2
#   BANK

#   COUNT* $$/P40

W('35,3747', 0o04645, 'P40AUTO', 'TC', 'MAKECADR', 'HELLO THERE.', line=904)
W('35,3750', 0o55164, '', 'TS', 'TEMPR60', 'FOR GENERALIZED RETURN TO OTHER BANKS.', line=905)
W('35,3751', 0o04616, 'P40A/P', 'TC', 'BANKCALL', 'SUBROUTINE TO CHECK PGNCS CONTROL', line=906)
W('35,3752', 0o54255, '', 'CADR', 'G+N,AUTO', 'AND AUTO STABILIZATION MODES', kind='data', line=907)
W('35,3753', 0o10000, '', 'CCS', 'A', '+0 INDICATES IN PGNCS, IN AUTO', line=908)
W('35,3754', 0o13766, '', 'TCF', 'TURNITON', '+ INDICATES NOT IN PGNCS AND/OR AUTO', line=909)
W('35,3755', 0o34737, '', 'CAF', 'APSFLBIT', 'ARE WE ON THE DESCENT STAGE?', line=910)
W('35,3756', 0o70106, '', 'MASK', 'FLGWRD10', line=911)
W('35,3757', 0o10000, '', 'CCS', 'A', line=912)
W('35,3760', 0o13773, '', 'TCF', 'GOBACK', 'RETURN', line=913)
W('35,3761', 0o34747, '', 'CAF', 'BIT5', 'YES, CHECK FOR AUTO-THROTTLE MODE', line=914)
W('35,3762', 0o00006, '', 'EXTEND', line=915)
W('35,3763', 0o02030, '', 'RAND', 'CHAN30', line=916)
W('35,3764', 0o00006, '', 'EXTEND', line=917)
W('35,3765', 0o13773, '', 'BZF', 'GOBACK', 'IN AUTO-THROTTLE MODE -- RETURN', line=918)
W('35,3766', 0o33775, 'TURNITON', 'CAF', 'P40A/PMD', 'DISPLAYS V50N25 R1=203 PLEASE PERFORM', line=919)
W('35,3767', 0o04616, '', 'TC', 'BANKCALL', 'CHECKLIST 203 TURN ON PGNCS ETC.', line=920)
W('35,3770', 0o20623, '', 'CADR', 'GOPERF1', kind='data', line=921)
W('35,3771', 0o16001, '', 'TCF', 'GOTOPOOH', 'V34E TERMINATE', line=922)
W('35,3772', 0o13751, '', 'TCF', 'P40A/P', 'RECYCLE', line=923)
W('35,3773', 0o31164, 'GOBACK', 'CA', 'TEMPR60', line=924)
W('35,3774', 0o04640, '', 'TC', 'BANKJUMP', 'GOODBYE.  COME AGAIN SOON.', line=925)

W('35,3775', 0o00203, 'P40A/PMD', 'OCT', '00203', kind='data', line=927)

# Page 749
#   BANK 36
#   SETLOC P40S
#   BANK

#   COUNT* $$/P40

# **********************************
# CONSTANTS FOR THE IGNITION ROUTINE
# **********************************

S('SERVCADR', 'equals', 0o104105, line=940)

W('36,3133', 0o02036, 'P40ADRES', 'ADRES', 'P40TABLE', kind='data', line=942)

W('36,3134', 0o02046, 'P41ADRES', 'ADRES', 'P41TABLE -5', kind='data', line=944)

W('36,3135', 0o02061, 'P42ADRES', 'ADRES', 'P42TABLE', kind='data', line=946)

#   EBANK= DVCNTR
W('36,3136', 0o03471, 'DSP2CADR', '2CADR', 'P63DISPS -2', kind='data', line=949)
W('36,3137', 0o62067, kind='data', line=949)

#   EBANK= DVCNTR
W('36,3140', 0o03642, 'ATMAGADR', '2CADR', 'ATMAG', kind='data', line=952)
W('36,3141', 0o70067, kind='data', line=952)

S('?', 'equals', 0o6001, line=954)

W('36,3142', 0o00000, 'D29.9SEC', '2DEC', '2990', kind='data', line=956)
W('36,3143', 0o05656, kind='data', line=956)

W('36,3144', 0o04672, 'S24.9SEC', 'DEC', '2490', kind='data', line=958)

W('36,3145', 0o00752, '4.9SEC', 'DEC', '490', kind='data', line=960)

S('OCT20', 'equals', 0o4747, line=962)

W('36,3146', 0o01475, 'V06N61', 'VN', '0661', kind='data', line=964)

# Page 750
# KILLTASK
# MOD NO:  NEW PROGRAM
# MOD BY:  COVELLI
#
# FUNCTIONAL DESCRIPTION:
#
# KILLTASK IS USED TO REMOVE A TASK FROM THE WAITLIST BY SUBSTITUTING A NULL TASK CALLED `NULLTASK' (OF COURSE),
# WHICH MERELY DOES A TC TASKOVER.  IF THE SAME TASK IS SCHEDULED MORE THAN ONCE, ONLY THE ONE WHICH WILL OCCUR
# FIRST IS REMOVED.  IF THE TASK IS NOT SCHEDULED, KILLTASK TAKES NO ACTION AND RETURNS WITH NO ALARM.  KILLTASK
# LEAVES INTERRUPTS INHIBITED SO CALLER MUST RELINT
#
# CALLING SEQUENCE
# L       TC      KILLTASK        # IN FIXED-FIXED
# L+1     CADR    ????????        # CADR (NOT 2CADR) OF TASK TO BE REMOVED.
# L+2     (RELINT)                # RETURN
#
# EXIT MODE:  AT L+2 OF CALLING SEQUENCE.
#
# ERASABLE INITIALIZATION:  NONE.
#
# OUTPUT:  2CADR OF NULLTASK IN LST2
#
# DEBRIS:  ITEMP1 - ITEMP4, A, L, Q.

#   EBANK= LST2
#   BLOCK 3  # KILLTASK MUST BE IN FIXED-FIXED.
#   SETLOC FFTAG6
#   BANK
#   COUNT* $$/KILL
W('6027', 0o36036, 'KILLTASK', 'CA', 'KILLBB', line=996)
W('6030', 0o00004, '', 'INHINT', line=997)
W('6031', 0o22000, '', 'LXCH', 'A', line=998)
W('6032', 0o50002, '', 'INDEX', 'Q', line=999)
W('6033', 0o30000, '', 'CA', '0', 'GET CADR.', line=1000)
W('6034', 0o22006, '', 'LXCH', 'BBANK', line=1001)
W('6035', 0o12200, '', 'TCF', 'KILLTSK2', 'CONTINUE IN SWITCHED FIXED.', line=1002)

#   EBANK= LST2
W('6036', 0o56063, 'KILLBB', 'BBCON', 'KILLTSK2', kind='data', line=1005)

#   BANK 27

#   SETLOC P40S1
#   BANK
#   COUNT* $$/KILL

W('27,2200', 0o22062, 'KILLTSK2', 'LXCH', 'ITEMP2', "SAVE CALLER'S BBANK", line=1013)
# Page 751
W('27,2201', 0o24002, '', 'INCR', 'Q', line=1015)
W('27,2202', 0o00006, '', 'EXTEND', line=1016)
W('27,2203', 0o22061, '', 'QXCH', 'ITEMP1', 'RETURN 2ADR IN ITEMP1,ITEMP2', line=1017)

W('27,2204', 0o54063, '', 'TS', 'ITEMP3', 'CADR IS IN A', line=1019)
W('27,2205', 0o75012, '', 'MASK', 'LOW10', line=1020)
W('27,2206', 0o64741, '', 'AD', 'BIT11', line=1021)
W('27,2207', 0o54064, '', 'TS', 'ITEMP4', 'GENADR OF TASK', line=1022)

W('27,2210', 0o45012, '', 'CS', 'LOW10', line=1024)
W('27,2211', 0o70063, '', 'MASK', 'ITEMP3', line=1025)
W('27,2212', 0o54063, '', 'TS', 'ITEMP3', 'FBANK OF TASK', line=1026)

W('27,2213', 0o22007, '', 'ZL', line=1028)
W('27,2214', 0o50001, 'ADRSCAN', 'INDEX', 'L', line=1029)
W('27,2215', 0o41410, '', 'CS', 'LST2', line=1030)
W('27,2216', 0o60064, '', 'AD', 'ITEMP4', 'COMPARE GENADRS', line=1031)
W('27,2217', 0o00006, '', 'EXTEND', line=1032)
W('27,2220', 0o12232, '', 'BZF', 'TSTFBANK', 'IF THEY MATCH, COMPARE FBANKS', line=1033)
W('27,2221', 0o44747, 'LETITLIV', 'CS', 'LSTLIM', line=1034)
W('27,2222', 0o60001, '', 'AD', 'L', line=1035)
W('27,2223', 0o00006, '', 'EXTEND', '', 'ARE WE DONE?', line=1036)
W('27,2224', 0o12230, '', 'BZF', 'DEAD', 'YES -- DONE, SO RETURN', line=1037)
W('27,2225', 0o24001, '', 'INCR', 'L', line=1038)
W('27,2226', 0o24001, '', 'INCR', 'L', line=1039)
W('27,2227', 0o12214, '', 'TCF', 'ADRSCAN', 'CONTINUE LOOP.', line=1040)

W('27,2230', 0o52062, 'DEAD', 'DXCH', 'ITEMP1', line=1042)
W('27,2231', 0o52006, '', 'DTCB', line=1043)

W('27,2232', 0o45012, 'TSTFBANK', 'CS', 'LOW10', line=1045)
W('27,2233', 0o50001, '', 'INDEX', 'L', line=1046)
W('27,2234', 0o71411, '', 'MASK', 'LST2 +1', 'COMPARE FBANKS ONLY.', line=1047)
W('27,2235', 0o00006, '', 'EXTEND', line=1048)
W('27,2236', 0o60063, '', 'SU', 'ITEMP3', line=1049)
W('27,2237', 0o00006, '', 'EXTEND', line=1050)
W('27,2240', 0o12242, '', 'BZF', 'KILLDEAD', 'MATCH -- KILL IT.', line=1051)
W('27,2241', 0o12221, '', 'TCF', 'LETITLIV', 'NO MATCH -- CONTINUE.', line=1052)

W('27,2242', 0o34353, 'KILLDEAD', 'CA', 'TCTSKOVR', line=1054)
W('27,2243', 0o50001, '', 'INDEX', 'L', line=1055)
W('27,2244', 0o55410, '', 'TS', 'LST2', 'REMOVE TASK BY INSERTING TASKOVER', line=1056)
W('27,2245', 0o12230, '', 'TCF', 'DEAD', line=1057)

S('LSTLIM', 'equals', 0o4747, line=1059)  # DEC 16
