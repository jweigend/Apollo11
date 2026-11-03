"""P40-P47.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P40-P47.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 684-736 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P40_P47', 'P40-P47.agc', 'Comanche055', pages='684-736')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P40-P47.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        684-736
# Mod history:  2009-05-11 RSB  Adapted from the Colossus249/ file
# of the same name, using Comanche055 page
# images.
# 2009-05-20 RSB  In S20.1, a DMP DDV was corrected to DMPR DDV.
# 2009-05-22 RSB  In BESTTRIM, TC PACTOFF corrected to
# TS PACTOFF.
# 2009-05-23 RSB  Prior to the 2CADR at T5IDLDAP, added an
# SBANK.
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

# Page 684
# PROGRAM DESCRIPTION ** P40CSM **

#   EBANK= DAPDATR1
#   BANK 31
#   SETLOC P40S
#   BANK

#   COUNT 24/P40

W('24,2073', 0o05560, 'P40CSM', 'TC', 'DOWNFLAG', line=46)
W('24,2074', 0o00023, '', 'ADRES', 'ENG2FLAG', kind='data', line=47)

W('24,2075', 0o06006, '', 'TC', 'INTPRET', line=49)
W('24,2076', 0o43135, '', 'SLOAD', 'BOFF', kind='interp', line=50)
W('24,2077', 0o03425, '', '', 'ECSTEER', 'IS THIS AN EXTERNAL DELTA V BURN', kind='operand', line=51)
W('24,2100', 0o01347, '', '', 'XDELVFLG', kind='operand', line=52)
W('24,2101', 0o50104, '', '', 'P40S/C', 'NO    CSTEER = ECSTEER', kind='operand', line=53)
W('24,2102', 0o77745, '', 'DLOAD', '', 'YES   CSTEER = ZERO', kind='interp', line=54)
W('24,2103', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=55)
W('24,2104', 0o17703, 'P40S/C', 'STODL', 'CSTEER', kind='interp', line=56)
W('24,2105', 0o10411, '', '', 'FENG', 'SET UP THRUST FOR P40 20,000 LBS', kind='operand', line=57)
W('24,2106', 0o17727, 'P40S/F', 'STODL', 'F', 'P41 ENTERS HERE', kind='interp', line=58)
W('24,2107', 0o03413, '', '', 'TIG', 'ORIGINAL TIG MAY BE SLIPPED BY P40S/SV', kind='operand', line=59)
W('24,2110', 0o03450, '', 'STORE', 'NOMTIG', 'SET ORIGINAL TIME OF IGNITION FOR S40.9', kind='interp', line=60)

W('24,2111', 0o77776, '', 'EXIT', kind='interp', line=62)
W('24,2112', 0o04662, '', 'TC', 'BANKCALL', line=63)
W('24,2113', 0o17653, '', 'CADR', 'R02BOTH', 'IMU STATUS CHECK', kind='data', line=64)

W('24,2114', 0o06006, 'P40PVA', 'TC', 'INTPRET', line=66)
W('24,2115', 0o77624, '', 'CALL', kind='interp', line=67)
W('24,2116', 0o34020, '', '', 'S40.1', 'COMPUTE VGTIG,UT', kind='operand', line=68)
W('24,2117', 0o77624, '', 'CALL', kind='interp', line=69)
W('24,2120', 0o51574, '', '', 'S40.2,3', 'COMPUTE PREFERRED ATTITUDE', kind='operand', line=70)
W('24,2121', 0o77414, '', 'SET', 'EXIT', kind='interp', line=71)
W('24,2122', 0o01073, '', '', 'PFRATFLG', kind='operand', line=72)
W('24,2123', 0o02303, 'P40SXTY', 'TCR', 'SETMINDB -1', 'NARROW DEADBAND FOR MANEUVER (EBANK6)', line=73)
W('24,2124', 0o00003, '', 'RELINT', line=74)
W('24,2125', 0o04662, '', 'TC', 'BANKCALL', line=75)
W('24,2126', 0o56000, '', 'CADR', 'R60CSM', 'ATTITUDE MANEUVER', kind='data', line=76)
W('24,2127', 0o45017, '', 'CS', 'ONE', 'FOR UPDATEVG', line=77)
W('24,2130', 0o55742, '', 'TS', 'NBRCYCLS', line=78)
W('24,2131', 0o05546, '', 'TC', 'UPFLAG', line=79)
W('24,2132', 0o00155, '', 'ADRES', 'TIMRFLAG', 'ALLOW CLOCKTASK', kind='data', line=80)

W('24,2133', 0o02326, '', 'TC', 'P41/P40', line=82)
W('24,2134', 0o02343, '', 'TC', 'P41/DSP', 'P41', line=83)

W('24,2135', 0o32425, 'P40TTOG', 'CAF', 'V06N40', 'INITIALIZE FOR CLOCKTASK WHICH IS CALLED', line=85)
# Page 685
W('24,2136', 0o55145, '', 'TS', 'NVWORD1', 'BELOW', line=87)

W('24,2137', 0o06006, '', 'TC', 'INTPRET', line=89)
W('24,2140', 0o51575, '', 'VLOAD', 'ABVAL', 'FOR R2', kind='interp', line=90)
W('24,2141', 0o03721, '', '', 'VGTIG', kind='operand', line=91)
W('24,2142', 0o17773, '', 'STODL', 'VGDISP', kind='interp', line=92)
W('24,2143', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=93)
W('24,2144', 0o03426, '', 'STORE', 'DVTOTAL', kind='interp', line=94)
W('24,2145', 0o77776, '', 'EXIT', kind='interp', line=95)

W('24,2146', 0o00006, '', 'EXTEND', line=97)
W('24,2147', 0o33061, '', 'DCA', 'STEERADS', 'SET FOR UPDATEVG AND TEST FOR STEERING', line=98)
W('24,2150', 0o53223, '', 'DXCH', 'AVEGEXIT', 'AFTER AVERAGE G', line=99)

W('24,2151', 0o32420, 'P40GMB', 'CAF', 'P40CKLS2', '(4.1 PROTECTION)', line=101)
W('24,2152', 0o04662, '', 'TC', 'BANKCALL', line=102)
W('24,2153', 0o21045, '', 'CADR', 'GOPERF1', kind='data', line=103)
W('24,2154', 0o12275, '', 'TCF', 'POST41', 'V34', line=104)
W('24,2155', 0o12435, '', 'TCF', 'TST,TRIM', 'V33', line=105)
W('24,2156', 0o45017, 'TRIMONLY', 'CS', 'BIT1', 'SET MRKRTEMP FOR GIMBAL TRIM (-1)', line=106)
W('24,2157', 0o55445, '', 'TS', 'MRKRTMP', 'ENTRY FROM TST,TRIM', line=107)

W('24,2160', 0o35021, '', 'CAF', 'ZERO', 'SET CNTR      +0 FOR RESTART LOGIC IN S40.6', line=109)
W('24,2161', 0o55447, '', 'TS', 'CNTR', '      +0 SAYS NORMAL ENTRY', line=110)
# +1 (PRE40.6) SAYS RESTART ENTRY

W('24,2162', 0o35017, '', 'CAF', 'ONE', line=113)
W('24,2163', 0o05245, '', 'TC', 'WAITLIST', line=114)
#   EBANK= DAPDATR1
W('24,2164', 0o02252, '', '2CADR', 'S40.6', kind='data', line=116)
W('24,2165', 0o40066, kind='data', line=116)

W('24,2166', 0o11445, '', 'CCS', 'MRKRTMP', 'TEST TO FIND TIME TO WAIT FOR GIMBAL TEST', line=118)
W('24,2167', 0o32417, '', 'CAF', '18SEC', 'PLUS, DELAY FOR 18 SECONDS', line=119)
W('24,2170', 0o12172, '', 'TCF', '+2', 'HOLE', line=120)
W('24,2171', 0o33064, '', 'CAF', '5SEC', 'DELAY FOR TRIM ONLY TASK', line=121)
W('24,2172', 0o04662, '', 'TC', 'BANKCALL', line=122)
W('24,2173', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=123)
W('24,2174', 0o05372, '', 'TC', '2PHSCHNG', line=124)
W('24,2175', 0o40026, '', 'OCT', '40026', '6.2 = PRE40.6(-0CS), CLOKTASK(100CS)', kind='data', line=125)
W('24,2176', 0o00234, '', 'OCT', '00234', '4.23 = P40S/SV (PRIO12)', kind='data', line=126)
W('24,2177', 0o35017, 'P40S/RS', 'CAF', 'ONE', line=127)
W('24,2200', 0o05245, '', 'TC', 'WAITLIST', 'P41/SDP', line=128)
#   EBANK= TIG
W('24,2201', 0o03260, '', '2CADR', 'CLOKTASK', kind='data', line=130)
W('24,2202', 0o50067, kind='data', line=130)

W('24,2203', 0o00003, '', 'RELINT', line=132)

W('24,2204', 0o03366, 'P40S/SV', 'TCR', 'E7SETTER', 'JOB, 4.23 PRETECTS, PREO12', line=134)
#   EBANK= TIG
# Page 686
W('24,2205', 0o06006, '', 'TC', 'INTPRET', line=137)
W('24,2206', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=138)
W('24,2207', 0o03413, '', '', 'TIG', kind='operand', line=139)
W('24,2210', 0o10416, '', '', 'SEC29.96', kind='operand', line=140)
W('24,2211', 0o00041, '', 'STORE', 'TDEC1', kind='interp', line=141)

W('24,2212', 0o77624, '', 'CALRB', '', 'RETURN IN BASIC', kind='interp', line=143)
W('24,2213', 0o27553, '', '', 'MIDTOAV1', kind='operand', line=144)
W('24,2214', 0o12216, '', 'TCF', '+2', line=145)
W('24,2215', 0o02237, '', 'TC', 'P40SNEWM', 'INTEGRATION TIME GREATER THAN ALLOWED', line=146)
W('24,2216', 0o00006, 'P40SET', 'EXTEND', line=147)
W('24,2217', 0o30155, '', 'DCA', 'MPAC', 'DELTA TIME TO PREREAD (INT.INIT.)', line=148)
W('24,2220', 0o53673, '', 'DXCH', 'P40TMP', line=149)
W('24,2221', 0o00006, '', 'EXTEND', line=150)
W('24,2222', 0o43064, '', 'DCS', '5SECDP', 'FOR TIGBLNK', line=151)
W('24,2223', 0o21673, '', 'DAS', 'P40TMP', line=152)
W('24,2224', 0o00006, '', 'EXTEND', line=153)
W('24,2225', 0o31673, '', 'DCA', 'P40TMP', line=154)
W('24,2226', 0o05342, '', 'TC', 'LONGCALL', line=155)
#   EBANK= TIG
W('24,2227', 0o02437, '', '2CADR', 'TIGBLNK', kind='data', line=157)
W('24,2230', 0o50067, kind='data', line=157)

W('24,2231', 0o05412, '', 'TC', 'PHASCHNG', line=159)
W('24,2232', 0o20214, '', 'OCT', '20214', '4.21 = TIGBLNK (P40TMP CS)', kind='data', line=160)

W('24,2233', 0o15217, '', 'TCF', 'ENDOFJOB', line=162)
W('24,2234', 0o04662, 'P40BLNKR', 'TC', 'BANKCALL', line=163)
W('24,2235', 0o20703, '', 'CADR', 'CLEANDSP', 'REMOVE RESIDUE', kind='data', line=164)
W('24,2236', 0o15217, '', 'TCF', 'ENDOFJOB', line=165)
#   EBANK= TIG
W('24,2237', 0o00006, 'P40SNEWM', 'EXTEND', line=167)
W('24,2240', 0o31246, '', 'DCA', 'PIPTIME1', line=168)
W('24,2241', 0o53413, '', 'DXCH', 'TIG', 'SET NEW TIG FOR 06 40', line=169)
W('24,2242', 0o00006, '', 'EXTEND', line=170)
W('24,2243', 0o32416, '', 'DCA', 'SEC29.96', line=171)
W('24,2244', 0o21413, '', 'DAS', 'TIG', line=172)
W('24,2245', 0o12216, '', 'TCF', 'P40SET', 'FOR LONGCALL OF TIG-30 (OR -35)', line=173)

#   EBANK= DAPDATR1
W('24,2246', 0o32426, 'POSTBURN', 'CAF', 'V16N40', line=176)
W('24,2247', 0o04662, '', 'TC', 'BANKCALL', line=177)
W('24,2250', 0o20704, '', 'CADR', 'REFLASH', kind='data', line=178)
W('24,2251', 0o12275, '', 'TCF', 'POST41', 'V34 GO FINISH', line=179)
W('24,2252', 0o12254, '', 'TCF', 'P40RCS', 'PROCEED', line=180)
W('24,2253', 0o12246, '', 'TCF', 'POSTBURN', 'RECYCLE', line=181)
W('24,2254', 0o00006, 'P40RCS', 'EXTEND', '', 'V99N40 ENTERS HERE ON A P40 BYPASS SPS', line=182)
W('24,2255', 0o32462, '', 'DCA', 'ACADN85', line=183)
W('24,2256', 0o53223, '', 'DXCH', 'AVEGEXIT', line=184)
W('24,2257', 0o35042, '', 'CAF', '2SECS', 'WAIT FOR CALCN85 VIA AVEGEXIT', line=185)
W('24,2260', 0o04662, '', 'TC', 'BANKCALL', line=186)
# Page 687
W('24,2261', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=188)

W('24,2262', 0o02303, 'P40MINDB', 'TCR', 'SETMINDB -1', line=190)
W('24,2263', 0o00003, '', 'RELINT', line=191)
W('24,2264', 0o05412, 'TIGNOW', 'TC', 'PHASCHNG', line=192)
W('24,2265', 0o05024, '', 'OCT', '05024', 'TYPE C GROUP 4 BELOW FOR NOUN 85', kind='data', line=193)
W('24,2266', 0o20000, '', 'OCT', '20000', 'PRIO 20', kind='data', line=194)
W('24,2267', 0o32424, '', 'CAF', 'V16N85B', line=195)
W('24,2270', 0o04662, '', 'TC', 'BANKCALL', line=196)
W('24,2271', 0o20704, '', 'CADR', 'REFLASH', kind='data', line=197)
W('24,2272', 0o12275, '', 'TCF', 'POST41', 'FINISH P40/P41', line=198)
W('24,2273', 0o12275, '', 'TCF', 'POST41', 'V03 PROCEED WITH REST OF THE CLEAN-UP', line=199)
W('24,2274', 0o12264, '', 'TCF', 'TIGNOW', 'V32 NOT GSOP RESPONSE BUT REDISPLAY N85', line=200)

W('24,2275', 0o00006, 'POST41', 'EXTEND', line=202)
W('24,2276', 0o32460, '', 'DCA', 'SERVCADR', line=203)
W('24,2277', 0o53223, '', 'DXCH', 'AVEGEXIT', line=204)
W('24,2300', 0o14106, '', 'TCF', 'GOTOPOOH', line=205)

W('24,2301', 0o00056, 'MINDB', 'DEC', '46', kind='data', line=207)
W('24,2302', 0o00707, 'MAXDB', 'DEC', '455', kind='data', line=208)
#   EBANK= DAPDATR1
W('24,2303', 0o00004, '', 'INHINT', line=210)
W('24,2304', 0o30032, 'SETMINDB', 'CA', 'CDUX', 'ROUTINE FOR SETTING', line=211)
W('24,2305', 0o55572, '', 'TS', 'THETADX', 'THE MINIMUM DEADBAND', line=212)
W('24,2306', 0o00006, '', 'EXTEND', '', 'IN AUTOPILOT', line=213)
W('24,2307', 0o30034, '', 'DCA', 'CDUY', line=214)
W('24,2310', 0o53574, '', 'DXCH', 'THETADY', line=215)
W('24,2311', 0o32301, '', 'CA', 'MINDB', 'SHOULD BE CALLED UNDER', line=216)
W('24,2312', 0o55655, '', 'TS', 'ADB', 'INTERRUPT INHIBITED', line=217)
W('24,2313', 0o45014, '', 'CS', 'BIT4', 'EBANK = E6', line=218)
W('24,2314', 0o71466, '', 'MASK', 'DAPDATR1', line=219)
W('24,2315', 0o55466, '', 'TS', 'DAPDATR1', line=220)
W('24,2316', 0o00002, '', 'TC', 'Q', line=221)

#   EBANK= DAPDATR1
W('24,2317', 0o00004, '', 'INHINT', line=224)
W('24,2320', 0o32302, 'SETMAXDB', 'CA', 'MAXDB', 'ROUTINE FOR SETTING', line=225)
W('24,2321', 0o55655, '', 'TS', 'ADB', 'THE MAXIMUM DEADBAND IN AUTOPILOT', line=226)
W('24,2322', 0o41466, '', 'CS', 'DAPDATR1', line=227)
W('24,2323', 0o75014, '', 'MASK', 'BIT4', 'SHOULD BE CALLED UNDER', line=228)
W('24,2324', 0o27466, '', 'ADS', 'DAPDATR1', 'INTERRUPT INHIBITED', line=229)
W('24,2325', 0o00002, '', 'TC', 'Q', 'EBANK = E6', line=230)

# Page 688
# PROGRAM DESCRIPTION ** P41CSM **

#   SETLOC P40S2
#   BANK

#   EBANK= DAPDATR1
#   COUNT 24/P41

W('27,2614', 0o05546, 'P41CSM', 'TC', 'UPFLAG', line=241)
W('27,2615', 0o00023, '', 'ADRES', 'ENG2FLAG', 'SET FOR RCS', kind='data', line=242)

W('27,2616', 0o06006, '', 'TC', 'INTPRET', line=244)
W('27,2617', 0o77745, '', 'DLOAD', kind='interp', line=245)
W('27,2620', 0o15335, '', '', 'HI6ZEROS', 'FOR P41 CSTEER =0', kind='operand', line=246)
W('27,2621', 0o03703, '', 'STORE', 'CSTEER', kind='interp', line=247)

W('27,2622', 0o43145, '', 'DLOAD', 'BON', kind='interp', line=249)
W('27,2623', 0o10413, '', '', 'FRCS2', '2JET THRUST FOR S40.1', kind='operand', line=250)
W('27,2624', 0o00700, '', '', 'NJETSFLG', kind='operand', line=251)
W('27,2625', 0o50106, '', '', 'P40S/F', 'NJETS = 1 2-JET', kind='operand', line=252)
W('27,2626', 0o52015, '', 'DAD', 'GOTO', 'NJETS = 0 4-JET', kind='interp', line=253)
W('27,2627', 0o10413, '', '', 'FRCS2', kind='operand', line=254)
W('27,2630', 0o50106, '', '', 'P40S/F', kind='operand', line=255)

#   SETLOC P40S
#   BANK

W('24,2326', 0o41011, 'P41/P40', 'CS', 'MODREG', line=260)
W('24,2327', 0o75017, '', 'MASK', 'ONE', 'P41EXITS AT CALL LOC +1', line=261)
W('24,2330', 0o00006, '', 'EXTEND', line=262)
W('24,2331', 0o12333, '', 'BZF', '+2', 'P41', line=263)
W('24,2332', 0o24002, '', 'INCR', 'Q', 'P40 EXITS AT CALL LOC +2', line=264)
W('24,2333', 0o00002, '', 'TC', 'Q', line=265)

W('24,2334', 0o35002, 'TTG/0', 'CAF', 'PRIO20', 'TASK (4.4 PROTECTS IN P41)', line=267)
W('24,2335', 0o05134, '', 'TC', 'NOVAC', line=268)
#   EBANK= DAPDATR1
W('24,2336', 0o02264, '', '2CADR', 'TIGNOW', kind='data', line=270)
W('24,2337', 0o50066, kind='data', line=270)

W('24,2340', 0o05560, 'P40CLK', 'TC', 'DOWNFLAG', line=272)
W('24,2341', 0o00155, '', 'ADRES', 'TIMRFLAG', kind='data', line=273)

W('24,2342', 0o15324, '', 'TCF', 'TASKOVER', line=275)

W('24,2343', 0o32423, 'P41/DSP', 'CAF', 'V06N85B', 'SET UP FOR NONFLASH V 06 N85 BY CLOCKJOB', line=277)
W('24,2344', 0o55145, '', 'TS', 'NVWORD1', line=278)

W('24,2345', 0o06006, '', 'TC', 'INTPRET', line=280)
# Page 689
W('24,2346', 0o77624, '', 'CALL', '', 'COMPUTE', kind='interp', line=282)
W('24,2347', 0o50370, '', '', 'P40CNV85', '      VGTIG IN CTRL COORDS', kind='operand', line=283)
W('24,2350', 0o77776, '', 'EXIT', kind='interp', line=284)
W('24,2351', 0o00006, '', 'EXTEND', '', 'DO CONTROL COORD CALCULATION AFTER AVEG', line=285)
W('24,2352', 0o32462, '', 'DCA', 'ACADN85', line=286)
W('24,2353', 0o53223, '', 'DXCH', 'AVEGEXIT', line=287)
W('24,2354', 0o05372, '', 'TC', '2PHSCHNG', line=288)
W('24,2355', 0o40036, '', 'OCT', '40036', '6.3=CLOKTASK(100CS)', kind='data', line=289)
W('24,2356', 0o00234, '', 'OCT', '234', '4.23=P40S/SV(PRIO12)', kind='data', line=290)

W('24,2357', 0o12177, '', 'TCF', 'P40S/RS', line=292)
W('24,2360', 0o32424, 'P41REDSP', 'CAF', 'V16N85B', 'ENTER FROM P41 SIDE OF TIGAVEG', line=293)
W('24,2361', 0o55145, '', 'TS', 'NVWORD1', 'REDISPLAY NONFLASHING', line=294)
W('24,2362', 0o32416, '', 'CAF', 'SEC29.96 +1', line=295)
W('24,2363', 0o05245, '', 'TC', 'WAITLIST', line=296)
#   EBANK= DAPDATR1
W('24,2364', 0o02334, '', '2CADR', 'TTG/0', kind='data', line=298)
W('24,2365', 0o50066, kind='data', line=298)

W('24,2366', 0o45015, '', 'CS', 'BIT3', line=300)
W('24,2367', 0o12566, '', 'TCF', 'TTGPHS', line=301)
W('24,2370', 0o40220, 'P40CNV85', 'STQ', 'SETPD', kind='interp', line=302)
W('24,2371', 0o03730, '', '', 'QTEMP1', kind='operand', line=303)
W('24,2372', 0o00001, '', '', '0', kind='operand', line=304)
W('24,2373', 0o41575, '', 'VLOAD', 'PUSH', kind='interp', line=305)
W('24,2374', 0o03721, '', '', 'VGPREV', 'EQUALS VGTIG (TARGETTING INPUT)', kind='operand', line=306)
W('24,2375', 0o77624, '', 'CALL', kind='interp', line=307)
W('24,2376', 0o45431, '', '', 'S41.1', kind='operand', line=308)
W('24,2377', 0o37665, '', 'STCALL', 'VGBODY', kind='interp', line=309)
W('24,2400', 0o03730, '', '', 'QTEMP1', kind='operand', line=310)

#   EBANK= DAPDATR1
W('24,2401', 0o06006, 'CALCN85', 'TC', 'INTPRET', line=313)
W('24,2402', 0o77624, '', 'CALL', kind='interp', line=314)
W('24,2403', 0o51104, '', '', 'UPDATEVG', 'NEW VG, S40.8 (+MAYBE S40.9)', kind='operand', line=315)
W('24,2404', 0o77624, '', 'CALL', kind='interp', line=316)
W('24,2405', 0o50370, '', '', 'P40CNV85', 'COMPUTE VGBODY', kind='operand', line=317)
W('24,2406', 0o77776, '', 'EXIT', kind='interp', line=318)
W('24,2407', 0o03215, '', 'TC', 'SERVXT', line=319)
W('24,2410', 0o02217, 'FENG', '2DEC', '9.1188544 B-7', 'SPS THRUST (20500LBS), SC.AT B+7 NEWT/E4', kind='data', line=320)
W('24,2411', 0o06650, kind='data', line=320)

W('24,2412', 0o00013, 'FRCS2', '2DEC', '.087437837 B-7', 'RCS ULLAGE (199.6COS10 LBS), SC.AT', kind='data', line=322)
W('24,2413', 0o06112, kind='data', line=322)

# B+7 NEWTONS/E+4
W('24,2414', 0o04700, 'SEC24.96', 'DEC', '2496', kind='data', line=325)
W('24,2415', 0o00000, 'SEC29.96', '2DEC', '2996', kind='data', line=326)
W('24,2416', 0o05664, kind='data', line=326)

W('24,2417', 0o03410, '18SEC', 'DEC', '1800', kind='data', line=328)
W('24,2420', 0o00204, 'P40CKLS2', 'OCT', '204', kind='data', line=329)
W('24,2421', 0o37730, '40CST5', 'OCT', '37730', '40 CS FOR THE T5 CLOCK', kind='data', line=330)
S('OCT12', 'equals', 0o4377, line=331)
# Page 690
W('24,2422', 0o04123, 'V1683', 'VN', '1683', kind='data', line=333)
W('24,2423', 0o01525, 'V06N85B', 'VN', '0685', kind='data', line=334)
W('24,2424', 0o04125, 'V16N85B', 'VN', '1685', kind='data', line=335)
W('24,2425', 0o01450, 'V06N40', 'VN', '0640', kind='data', line=336)
W('24,2426', 0o04050, 'V16N40', 'VN', '1640', kind='data', line=337)
W('24,2427', 0o00027, 'OCT27/24', 'OCT', '27', kind='data', line=338)
W('24,2430', 0o00053, 'OCT53', 'OCT', '53', kind='data', line=339)
W('24,2431', 0o00035, 'OCT35', 'OCT', '35', kind='data', line=340)
#   EBANK= DAPDATR1
W('24,2432', 0o03153, 'T5IDL24', '2CADR', 'T5IDLOC', kind='data', line=342)
W('24,2433', 0o12066, kind='data', line=342)

W('24,2434', 0o00026, '3MDOT', 'DEC', '86.6175796 B-16', '3SEC MASS LOSS (63.8 LBS/SEC), SC.AT', kind='data', line=344)
# B+16 KB/SEC (NOT, EMDOT IS PAD-LOADED,
# BUT 3MDOT IS NOT A CRITICAL QUANTITY, SO
# IT CAN REMAIN IN FIXED MEMORY)
W('24,2435', 0o35017, 'TST,TRIM', 'CAF', 'BIT1', 'SET UP FOR GIMB DRIVE TEST AND TRIM (+1)', line=348)
W('24,2436', 0o12157, '', 'TCF', 'TRIMONLY +1', line=349)
W('24,2437', 0o33064, 'TIGBLNK', 'CAF', '5SEC', 'CALL TIGAVEG IN FIVE SEC AT TIG-30', line=350)
W('24,2440', 0o05245, '', 'TC', 'WAITLIST', line=351)
#   EBANK= TIG
W('24,2441', 0o02555, '', '2CADR', 'TIGAVEG', kind='data', line=353)
W('24,2442', 0o50067, kind='data', line=353)

W('24,2443', 0o35021, '', 'CAF', 'ZERO', 'DISABLE HERE, NOT IN P40BLNKR', line=355)
W('24,2444', 0o55145, '', 'TS', 'NVWORD1', line=356)

W('24,2445', 0o35066, '', 'CAF', 'PRIO14', line=358)
W('24,2446', 0o05134, '', 'TC', 'NOVAC', line=359)
#   EBANK= TIG
W('24,2447', 0o02234, '', '2CADR', 'P40BLNKR', "DON'T PROTECT -- RESTARTS BLANK DSKY", kind='data', line=361)
W('24,2450', 0o50067, kind='data', line=361)

W('24,2451', 0o44362, '', 'CS', 'OCT37', '4.37 = TIGAVEG (500CS)', line=363)
W('24,2452', 0o04114, 'P40TSK', 'TC', 'NEWPHASE', line=364)
W('24,2453', 0o00004, '', 'OCT', '4', kind='data', line=365)
W('24,2454', 0o05324, '', 'TC', 'TASKOVER', line=366)

#   EBANK= TIG
W('24,2455', 0o02511, 'ACADN83', '2CADR', 'CALCN83', kind='data', line=369)
W('24,2456', 0o50067, kind='data', line=369)

#   EBANK= TIG
W('24,2457', 0o03227, 'SERVCADR', '2CADR', 'SERVEXIT', kind='data', line=372)
W('24,2460', 0o76067, kind='data', line=372)

#   EBANK= DAPDATR1
W('24,2461', 0o02401, 'ACADN85', '2CADR', 'CALCN85', kind='data', line=375)
W('24,2462', 0o50066, kind='data', line=375)

# Page 691
# PROGRAM DESCRIPTION ** P47CSM **

#   COUNT 24/P47

#   EBANK= TIG
W('24,2463', 0o04662, 'P47CSM', 'TC', 'BANKCALL', 'IMU STATUS CHECK', line=383)
W('24,2464', 0o17653, '', 'CADR', 'R02BOTH', kind='data', line=384)
W('24,2465', 0o06006, '', 'TC', 'INTPRET', line=385)
W('24,2466', 0o77624, '', 'CALRB', kind='interp', line=386)
W('24,2467', 0o27543, '', '', 'MIDTOAV2', kind='operand', line=387)
W('24,2470', 0o30155, '', 'CA', 'MPAC +1', 'DELTA TIME TO RPEREAD (LESS THAN 100', line=388)
W('24,2471', 0o55672, '', 'TS', 'P40TMP', '      CS, WITH A TPAGREE, INT.INIT.)', line=389)
W('24,2472', 0o05245, '', 'TC', 'WAITLIST', line=390)
#   EBANK= TIG
W('24,2473', 0o02500, '', '2CADR', 'TIGON', 'TIGON IS REQUIRED TO MATHCHTAT AND AVEG', kind='data', line=392)
W('24,2474', 0o50067, kind='data', line=392)

W('24,2475', 0o05412, '', 'TC', 'PHASCHNG', line=394)
W('24,2476', 0o40574, '', 'OCT', '40574', 'A, 4.57 = TIGON (P40TMP CS)', kind='data', line=395)
W('24,2477', 0o15217, '', 'TCF', 'ENDOFJOB', line=396)

#   EBANK= P40TMP
W('24,2500', 0o00006, 'TIGON', 'EXTEND', line=399)
W('24,2501', 0o32456, '', 'DCA', 'ACADN83', line=400)
W('24,2502', 0o53223, '', 'DXCH', 'AVEGEXIT', line=401)
W('24,2503', 0o34371, '', 'CAF', 'PRIO30', 'FORCE ZEROING OF N83 BEFORE SERVICER', line=402)
W('24,2504', 0o05134, '', 'TC', 'NOVAC', line=403)
#   EBANK= TIG
W('24,2505', 0o02534, '', '2CADR', 'P47BODY', kind='data', line=405)
W('24,2506', 0o50067, kind='data', line=405)

W('24,2507', 0o45016, '', 'CS', 'BIT2', '4.2 = PRECHECK (-0CS), P47BODY (PRIO30)', line=407)
W('24,2510', 0o12566, '', 'TCF', 'TTGPHS', line=408)

#   EBANK= TIG
W('24,2511', 0o06006, 'CALCN83', 'TC', 'INTPRET', line=411)
W('24,2512', 0o77601, '', 'SETPD', '', 'SET UP PUSHLIST FOR S41.1', kind='interp', line=412)
W('24,2513', 0o00001, '', '', '0', kind='operand', line=413)
W('24,2514', 0o53375, '', 'VLOAD', 'VAD', kind='interp', line=414)
W('24,2515', 0o03665, '', '', 'DELVCTL', kind='operand', line=415)
W('24,2516', 0o03433, '', '', 'DELVREF', kind='operand', line=416)
W('24,2517', 0o03460, '', 'STORE', 'DV47TEMP', 'FOR COPYCYCLE BELOW', kind='interp', line=417)
W('24,2520', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=418)
W('24,2521', 0o45431, '', '', 'S41.1', kind='operand', line=419)
W('24,2522', 0o37675, '', 'STCALL', 'DELVIMU', kind='interp', line=420)
W('24,2523', 0o70542, '', '', 'S11.1', 'CALC. VI, H, HDOT FOR NOUN 62', kind='operand', line=421)
W('24,2524', 0o77776, '', 'EXIT', kind='interp', line=422)
W('24,2525', 0o05412, '', 'TC', 'PHASCHNG', line=423)
W('24,2526', 0o10035, '', 'OCT', '10035', kind='data', line=424)
# Page 692
W('24,2527', 0o35022, '', 'CAF', 'FIVE', line=426)
W('24,2530', 0o05606, '', 'TC', 'GENTRAN', line=427)
W('24,2531', 0o01457, '', 'ADRES', 'DV47TEMP', kind='data', line=428)
W('24,2532', 0o01664, '', 'ADRES', 'DELVCTL', kind='data', line=429)

W('24,2533', 0o03215, '', 'TC', 'SERVXT', line=431)
W('24,2534', 0o06006, 'P47BODY', 'TC', 'INTPRET', line=432)
W('24,2535', 0o77775, '', 'VLOAD', kind='interp', line=433)
W('24,2536', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=434)
W('24,2537', 0o03675, '', 'STORE', 'DELVIMU', 'CLEAR DISPLAY AND ACCUMULATOR STORAGE', kind='interp', line=435)
W('24,2540', 0o03665, '', 'STORE', 'DELVCTL', 'UPON INITIATION OR ENTER RESPONSE', kind='interp', line=436)
W('24,2541', 0o77776, '', 'EXIT', kind='interp', line=437)
W('24,2542', 0o35067, 'P47BOD', 'CAF', 'PRIO15', 'LOWER PRIO THAN CALCN83 (20)', line=438)
W('24,2543', 0o05210, '', 'TC', 'PRIOCHNG', '      TO PREVENT INTERRUPTION OF CALCN83', line=439)
W('24,2544', 0o05412, '', 'TC', 'PHASCHNG', line=440)
W('24,2545', 0o05024, '', 'OCT', '05024', 'TYPE C GROUP 4 BELOW FOR NOUN 83', kind='data', line=441)
W('24,2546', 0o15000, '', 'OCT', '15000', 'PRIO 15', kind='data', line=442)
W('24,2547', 0o32422, 'P47/DSP', 'CAF', 'V1683', line=443)
W('24,2550', 0o04662, '', 'TC', 'BANKCALL', line=444)
W('24,2551', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=445)
W('24,2552', 0o04106, '', 'TC', 'GOTOPOOH', line=446)
W('24,2553', 0o04106, '', 'TC', 'GOTOPOOH', line=447)
W('24,2554', 0o12534, '', 'TCF', 'P47BODY', 'RECYCLE -- CLEAR ACCUMULATED VELOCITY', line=448)

# Page 693
# ROUTINE ** TIG-30 ** DESCRIPTION

#   EBANK= TIG
#   COUNT 24/P40

W('24,2555', 0o02326, 'TIGAVEG', 'TC', 'P41/P40', 'TASK (4.37 PROTECTS)', line=456)
W('24,2556', 0o12360, '', 'TCF', 'P41REDSP', line=457)

W('24,2557', 0o32425, '', 'CAF', 'V06N40', 'UNBLANK DISPLAY', line=459)
W('24,2560', 0o55145, '', 'TS', 'NVWORD1', line=460)

W('24,2561', 0o32414, '', 'CAF', 'SEC24.96', line=462)
W('24,2562', 0o05245, '', 'TC', 'WAITLIST', line=463)
#   EBANK= TIG
W('24,2563', 0o02574, '', '2CADR', 'TIG-5', kind='data', line=465)
W('24,2564', 0o50067, kind='data', line=465)

W('24,2565', 0o46211, '', 'CS', 'SIX', '4.6 = TIG-5 (2496CS), PRECHECK (-0CS)', line=467)
W('24,2566', 0o04114, 'TTGPHS', 'TC', 'NEWPHASE', 'ENTRY FROM P41REDSP (P41) WITH A=-4, OR', line=468)
W('24,2567', 0o00004, '', 'OCT', '4', '      FROM TIGON    (P47) WITH A=-1', kind='data', line=469)

W('24,2570', 0o10763, 'PRECHECK', 'CCS', 'PHASE5', 'HAS SERVICER BEEN RESTARTED', line=471)
W('24,2571', 0o15324, '', 'TCF', 'TASKOVER', "YES, DON'T START ANOTHER ONE", line=472)
W('24,2572', 0o04701, '', 'TC', 'POSTJUMP', line=473)
W('24,2573', 0o76701, '', 'CADR', 'PREREAD', kind='data', line=474)

# Page 694
# ROUTINE ** TIG-5 ** DESCRIPTION

#   EBANK= TIG
W('24,2574', 0o33064, 'TIG-5', 'CAF', '5SEC', line=480)
W('24,2575', 0o05245, '', 'TC', 'WAITLIST', line=481)
#   EBANK= DAPDATR1
W('24,2576', 0o02612, '', '2CADR', 'TIG-0', kind='data', line=483)
W('24,2577', 0o50066, kind='data', line=483)

W('24,2600', 0o45007, '', 'CS', 'BIT9', 'WILL CAUSE V99 FLASH', line=485)
W('24,2601', 0o55145, '', 'TS', 'NVWORD1', line=486)

W('24,2602', 0o05372, '', 'TC', '2PHSCHNG', line=488)
W('24,2603', 0o40074, '', 'OCT', '40074', 'A, 4.7 = TIG-0 (500CS)', kind='data', line=489)
W('24,2604', 0o00033, '', 'OCT', '00033', 'A, 3.3 = S40.13 (PRIO20)', kind='data', line=490)

W('24,2605', 0o35002, '', 'CAF', 'PRIO20', line=492)
W('24,2606', 0o05147, '', 'TC', 'FINDVAC', line=493)
#   EBANK= TGO
W('24,2607', 0o02427, '', '2CADR', 'S40.13', kind='data', line=495)
W('24,2610', 0o34067, kind='data', line=495)

W('24,2611', 0o15324, '', 'TCF', 'TASKOVER', line=497)

# Page 695
# ROUTINES ** TIG-0 ** AND ** IGNITION ** DESCRIPTION

#   EBANK= DAPDATR1  # TASK, 4.7 PHASE, OR 4.77 (-0CS) IN R40
W('24,2612', 0o40103, 'TIG-0', 'CS', 'FLAGWRD7', 'SET IGN FLAG', line=503)
W('24,2613', 0o75003, '', 'MASK', 'BIT13', line=504)
W('24,2614', 0o26103, '', 'ADS', 'FLAGWRD7', line=505)

W('24,2615', 0o30103, '', 'CAE', 'FLAGWRD7', 'CHECK ASTN FLAG FOR V99 RESPONSE', line=507)
W('24,2616', 0o75004, '', 'MASK', 'BIT12', line=508)
W('24,2617', 0o00006, '', 'EXTEND', line=509)
W('24,2620', 0o15324, '', 'BZF', 'TASKOVER', 'WAIT FOR V99P', line=510)

W('24,2621', 0o32425, '', 'CAF', 'V06N40', 'CLEAR THE V99 (IN CASE OF A RESTART', line=512)
W('24,2622', 0o55145, '', 'TS', 'NVWORD1', '      DURING THE V99 SEQUENCE)', line=513)

W('24,2623', 0o05412, '', 'TC', 'PHASCHNG', 'V99P HAS COME ALREADY, DO IGNITION NOW', line=515)
W('24,2624', 0o00614, '', 'OCT', '00614', 'A, 4.61 = IGNITION (-0CS) TBASE OLD', kind='data', line=516)

W('24,2625', 0o30032, 'IGNITION', 'CAE', 'CDUX', 'SAVE FOR ROLL DAP REFERENCE OGAD', line=518)
W('24,2626', 0o55450, '', 'TS', 'OGAD', '      V99PJOB (CLOCKJOB) SETS UP IGNITION', line=519)
W('24,2627', 0o00006, '', 'EXTEND', '', '      TASK (4.61 PROTECTION)', line=520)
W('24,2630', 0o30025, '', 'DCA', 'TIME2', '      FOR RESTARTS', line=521)
W('24,2631', 0o53337, '', 'DXCH', 'TEVENT', line=522)
W('24,2632', 0o40101, '', 'CS', 'FLAGWRD5', 'SET ENGONFLG', line=523)
W('24,2633', 0o75011, '', 'MASK', 'BIT7', line=524)
W('24,2634', 0o26101, '', 'ADS', 'FLAGWRD5', line=525)
W('24,2635', 0o35003, 'SPSON', 'CAF', 'BIT13', 'TURN ON SPS ENGINE', line=526)
W('24,2636', 0o00006, '', 'EXTEND', line=527)
W('24,2637', 0o05011, '', 'WOR', 'DSALMOUT', line=528)

W('24,2640', 0o35007, 'IMPULCHK', 'CAF', 'BIT9', 'CHECK FOR IMPULSIVE BURN', line=530)
W('24,2641', 0o70076, '', 'MASK', 'FLAGWRD2', line=531)
W('24,2642', 0o10000, '', 'CCS', 'A', line=532)
W('24,2643', 0o12733, '', 'TCF', 'IMPLBURN', 'IMPULSIVE', line=533)
W('24,2644', 0o40102, '', 'CS', 'FLAGWRD6', 'NON-IMPULSIVE, SET STRULLSW FOR STEERULL', line=534)
W('24,2645', 0o75003, '', 'MASK', 'BIT13', line=535)
W('24,2646', 0o26102, '', 'ADS', 'FLAGWRD6', line=536)

W('24,2647', 0o44105, 'PREPTVC', 'CS', 'OCT60000', 'RESET T5 BITS', line=538)
W('24,2650', 0o70102, '', 'MASK', 'FLAGWRD6', line=539)
W('24,2651', 0o54102, '', 'TS', 'FLAGWRD6', line=540)

W('24,2652', 0o00006, '', 'EXTEND', '', 'KILL RCS', line=542)
W('24,2653', 0o32433, '', 'DCA', 'T5IDL24', line=543)
W('24,2654', 0o53313, '', 'DXCH', 'T5LOC', line=544)

W('24,2655', 0o46214, '', 'CS', 'THREE', '4.3 = DOTVCON (40CS)', line=546)
W('24,2656', 0o04114, '', 'TC', 'NEWPHASE', line=547)
W('24,2657', 0o00004, '', 'OCT', '4', kind='data', line=548)

# Page 696
W('24,2660', 0o05267, '', 'TC', 'FIXDELAY', line=551)
W('24,2661', 0o00050, '', 'DEC', '40', '0.4 SECOND DELAY FOR THRUST BUILDUP', kind='data', line=552)

W('24,2662', 0o45017, 'DOTVCON', 'CS', 'BIT1', 'SET TVCPHASE = TVCDAPON CALL (FRESHDAP)', line=554)
W('24,2663', 0o55644, '', 'TS', 'TVCPHASE', line=555)
W('24,2664', 0o35021, '', 'CAF', 'ZERO', 'SET TVCEXECUTIVE PHASE', line=556)
W('24,2665', 0o55651, '', 'TS', 'TVCEXPHS', line=557)
W('24,2666', 0o44105, '', 'CS', 'OCT60000', 'SET T5 BITS TO INDICATE TVC TAKEOVER ....', line=558)
W('24,2667', 0o70102, '', 'MASK', 'FLAGWRD6', '      BITS 15,14 = 10', line=559)
W('24,2670', 0o65001, '', 'AD', 'BIT15', line=560)
W('24,2671', 0o54102, '', 'TS', 'FLAGWRD6', line=561)

W('24,2672', 0o36214, '', 'CAF', 'THREE', '6.3 = CLOKTASK (100CS), DROPPING PRE40.6', line=563)
W('24,2673', 0o54001, '', 'TS', 'L', '      WHICH IS HANDLED NOW BY REDOTVC', line=564)
W('24,2674', 0o40000, '', 'COM', line=565)
W('24,2675', 0o52765, '', 'DXCH', '-PHASE6', line=566)

W('24,2676', 0o00006, '', 'EXTEND', '', 'STORE RCS ATTITUDE ERRORS FOR USE IN', line=568)
W('24,2677', 0o41571, '', 'DCS', 'ERRORY', 'INITIALIZING TVC ATTITUDE ERRORS', line=569)
W('24,2700', 0o53703, '', 'DXCH', 'ERRBTMP', line=570)

W('24,2701', 0o45022, '', 'CS', 'FIVE', '4.5 = DOSTRULL (160 CS)', line=572)
W('24,2702', 0o04114, '', 'TC', 'NEWPHASE', line=573)
W('24,2703', 0o00004, '', 'OCT', '4', kind='data', line=574)

W('24,2704', 0o34777, '', 'CAF', 'POSMAX', 'SET TIME5 FOR STARTING RIGHT AWAY', line=576)
W('24,2705', 0o54030, '', 'TS', 'TIME5', line=577)
W('24,2706', 0o00006, '', 'EXTEND', line=578)
W('24,2707', 0o33067, '', 'DCA', 'TVCON2C', '(TVCDAPON)', line=579)
W('24,2710', 0o53313, '', 'DXCH', 'T5LOC', '(KILLS RCS DAP)', line=580)

W('24,2711', 0o05267, '', 'TC', 'FIXDELAY', '0.4 + 1.6 = 2.0 SEC FOR ULLAGE-OFF AND', line=582)
W('24,2712', 0o00240, '', 'DEC', '160', '      STEERING (IF NON-IMPULSIVE)', kind='data', line=583)

W('24,2713', 0o35003, 'DOSTRULL', 'CAF', 'BIT13', 'CHECK STRULLSW FOR IMPULSIVE BURN', line=585)
W('24,2714', 0o70102, '', 'MASK', 'FLAGWRD6', line=586)
W('24,2715', 0o10000, '', 'CCS', 'A', line=587)
W('24,2716', 0o02724, '', 'TCR', 'STEERULL', 'NON-IMPULSIVE, STEERING AND ULLAGE OFF', line=588)
W('24,2717', 0o02727, '', 'TCR', 'ULAGEOFF', 'ULLAGE OFF (ONLY, OR AGAIN)', line=589)

W('24,2720', 0o00006, '', 'EXTEND', line=591)
W('24,2721', 0o35021, '', 'DCA', 'NEG0', 'KILL GROUP 4 (DP NEG0 = -0,+0)', line=592)
W('24,2722', 0o52761, '', 'DXCH', '-PHASE4', line=593)

W('24,2723', 0o15324, 'ENDIGN', 'TCF', 'TASKOVER', line=595)

W('24,2724', 0o40076, 'STEERULL', 'CS', 'FLAGWRD2', 'SET STEERSW', line=597)
W('24,2725', 0o75005, '', 'MASK', 'BIT11', line=598)
W('24,2726', 0o26076, '', 'ADS', 'FLAGWRD2', line=599)

# Page 697

W('24,2727', 0o35021, 'ULAGEOFF', 'CAF', 'ZERO', line=603)
W('24,2730', 0o00006, '', 'EXTEND', line=604)
W('24,2731', 0o01005, '', 'WRITE', 'CHAN5', 'ZERO CHANNEL 5', line=605)
W('24,2732', 0o00002, '', 'TC', 'Q', line=606)

W('24,2733', 0o45003, 'IMPLBURN', 'CS', 'BIT13', 'RESET STRULLSW (COULD BE AN IMPULSIVE', line=608)
W('24,2734', 0o70102, '', 'MASK', 'FLAGWRD6', '      ENGINE FAIL)', line=609)
W('24,2735', 0o54102, '', 'TS', 'FLAGWRD6', line=610)

W('24,2736', 0o03366, '', 'TCR', 'E7SETTER', line=612)

#   EBANK= TIG
W('24,2737', 0o00006, '', 'EXTEND', '', 'PREPARE FOR R1 OF V06N40 (CLOCKTASK)', line=615)
W('24,2740', 0o31430, '', 'DCA', 'TGO', line=616)
W('24,2741', 0o53413, '', 'DXCH', 'TIG', line=617)
W('24,2742', 0o00006, '', 'EXTEND', line=618)
W('24,2743', 0o30025, '', 'DCA', 'TIME2', line=619)
W('24,2744', 0o21413, '', 'DAS', 'TIG', line=620)

W('24,2745', 0o05372, '', 'TC', '2PHSCHNG', line=622)
W('24,2746', 0o40153, '', 'OCT', '40153', 'A, 3.15 = ENGINOFF (TGO+1) .... NOT GROUP', kind='data', line=623)
W('24,2747', 0o07014, '', 'OCT', '07014', 'C, DELTAT NEXT, TASK BELOW, IN', kind='data', line=624)
W('24,2750', 0o77777, '', 'DEC', '-0', '-0 CS', kind='data', line=625)
#   EBANK= DAPDATR1
W('24,2751', 0o02757, '', '2CADR', 'IMPLCONT', kind='data', line=627)
W('24,2752', 0o50066, kind='data', line=627)

W('24,2753', 0o31430, '', 'CAE', 'TGO +1', '(TPAGREE IN S40.13, LESS THAN 600CS)', line=629)
W('24,2754', 0o05245, '', 'TC', 'WAITLIST', line=630)
#   EBANK= TGO
W('24,2755', 0o02766, '', '2CADR', 'ENGINOFF', kind='data', line=632)
W('24,2756', 0o50067, kind='data', line=632)

W('24,2757', 0o45007, 'IMPLCONT', 'CS', 'BIT9', 'RESET IMPULSW, ENGINOFF IS NOW SET UP', line=634)
W('24,2760', 0o70076, '', 'MASK', 'FLAGWRD2', line=635)
W('24,2761', 0o54076, '', 'TS', 'FLAGWRD2', line=636)

W('24,2762', 0o03371, '', 'TCR', 'E6SETTER', line=638)
#   EBANK= DAPDATR1

W('24,2763', 0o35021, '', 'CAF', 'ZERO', 'SET UP V97VCNTR IN CASE ENGINOFF (MASS-=', line=641)
W('24,2764', 0o55444, '', 'TS', 'V97VCNTR', '      BACK) ARRIVES BEFORE TVCDAPON', line=642)

W('24,2765', 0o12647, '', 'TCF', 'PREPTVC', line=644)

#   EBANK= TGO  # E7 FORCED BY 3.15SPOT VARIABLE DELTA-T
W('24,2766', 0o03371, 'ENGINOFF', 'TCR', 'E6SETTER', 'TASK, 3.15 PHASE (TGO+1 CS)   GET E6', line=647)
#   EBANK= DAPDATR1
W('24,2767', 0o31474, '', 'CAE', 'CSMMASS', line=649)
W('24,2770', 0o55652, '', 'TS', 'MASSTMP', 'COPYCYCLE FOR MASSBACK', line=650)
# Page 698
W('24,2771', 0o05372, '', 'TC', '2PHSCHNG', line=652)
W('24,2772', 0o00003, '', 'OCT', '00003', 'KILL GROUP 3 PROTECTION OF ENGINOFF, DO', kind='data', line=653)
W('24,2773', 0o40634, '', 'OCT', '40634', 'A, 4.63 = DOSPSOFF (-0CS)', kind='data', line=654)
W('24,2774', 0o03017, 'DOSPSOFF', 'TCR', 'SPSOFF', 'SHUTDOWN SPS, MASS UPDATES, ETC.', line=655)
W('24,2775', 0o42427, '', 'CS', 'OCT27/24', '(OCTAL 27)', line=656)
W('24,2776', 0o04114, '', 'TC', 'NEWPHASE', line=657)
W('24,2777', 0o00004, '', 'OCT', '4', '4.27 = DOTVCRCS (250 CS)', kind='data', line=658)

W('24,3000', 0o05267, '', 'TC', 'FIXDELAY', '2.5 SECOND DELAY FOR SPS TAILOFF', line=660)
W('24,3001', 0o00372, '', 'DEC', '250', kind='data', line=661)

W('24,3002', 0o02320, 'DOTVCRCS', 'TCR', 'SETMAXDB', 'WIDE DEADBAND FOR CUTOFF TRANSIENT', line=663)

W('24,3003', 0o04740, '', 'TC', 'IBNKCALL', 'SET UP RCS DAP (KILLS TVCDAPS, SETS T5', line=665)
W('24,3004', 0o42024, '', 'CADR', 'RCSDAPON', '      BITS, WAITS 0.6SEC FOR TVCEXEC DIE)', kind='data', line=666)

W('24,3005', 0o04740, '', 'TC', 'IBNKCALL', 'UPDATE WEIGHT/G AND MASS-PROPERTIES FOR', line=668)
W('24,3006', 0o13366, '', 'CADR', 'MASSPROP', '      RCS DAP STARTUP IN 0.6 SECONDS', kind='data', line=669)

W('24,3007', 0o03071, '', 'TCR', 'TVCZAP', 'WIPE OUT TVC, TURN OFF CLOKTASK', line=671)

W('24,3010', 0o05412, '', 'TC', 'PHASCHNG', line=673)
W('24,3011', 0o00354, '', 'OCT', '00354', 'A, 4.35 = POSTBURN (NOVAC, PRIO12)', kind='data', line=674)
W('24,3012', 0o34710, '', 'CAF', 'PRIO12', 'SET UP POSTBURN V16N40 JOB', line=675)
W('24,3013', 0o05134, '', 'TC', 'NOVAC', line=676)
#   EBANK= DAPDATR1  # (SET MAXDB IN POST41)
W('24,3014', 0o02246, '', '2CADR', 'POSTBURN', kind='data', line=678)
W('24,3015', 0o50066, kind='data', line=678)

W('24,3016', 0o15324, '', 'TCF', 'TASKOVER', line=680)

#   EBANK= DAPDATR1
W('24,3017', 0o00006, 'SPSOFF', 'EXTEND', '', 'ESTABLISH SPSOFF TEVENT', line=683)
W('24,3020', 0o30025, '', 'DCA', 'TIME2', line=684)
W('24,3021', 0o53337, '', 'DXCH', 'TEVENT', line=685)
W('24,3022', 0o45011, '', 'CS', 'BIT7', 'RESET ENGONFLG', line=686)
W('24,3023', 0o70101, '', 'MASK', 'FLAGWRD5', line=687)
W('24,3024', 0o54101, '', 'TS', 'FLAGWRD5', '(RESTARTS WILL SHUT DOWN SPS NOW)', line=688)
W('24,3025', 0o45003, '', 'CS', 'BIT13', 'SHUT DOWN SPS ENGINE', line=689)
W('24,3026', 0o00006, '', 'EXTEND', line=690)
W('24,3027', 0o03011, '', 'WAND', 'DSALMOUT', line=691)

W('24,3030', 0o35002, '', 'CAF', 'BIT14', 'ISSUE SIV CUTOFF COMMAND', line=693)
W('24,3031', 0o00006, '', 'EXTEND', '', 'FOR POSSIBLE BACK-UP USE', line=694)
W('24,3032', 0o05012, '', 'WOR', 'CHAN12', line=695)
W('24,3033', 0o31444, 'MASSBACK', 'CAE', 'V97VCNTR', 'RESTORE PART OF PRE-DECREMENTED MASS', line=696)
# V97CNTR = VCNTR UNLESS V97 IS
# ACTIVE.  ONLY V97CNTR IS THEN RIGHT.
W('24,3034', 0o00006, '', 'EXTEND', '', 'VCNTR COUNTS 1/2-SECONDS IN TVC EXEC', line=699)
W('24,3035', 0o70110, '', 'MP', 'EMDOT', '      MDOT, SC.AT B+3 KG/CS', line=700)
W('24,3036', 0o22000, '', 'LXCH', 'A', line=701)
# Page 699
W('24,3037', 0o00006, '', 'EXTEND', line=703)
W('24,3040', 0o75041, '', 'MP', '1SEC', 'DEC 100', line=704)
W('24,3041', 0o61652, '', 'AD', 'MASSTMP', 'CORRECTION IS ACCURATE TO 5 CS OF FLOW', line=705)
W('24,3042', 0o55474, '', 'TS', 'CSMMASS', '      (1.44 KG OR 0.4 BITS)', line=706)

W('24,3043', 0o31644, '', 'CA', 'TVCPHASE', 'CHECK IF OK FOR TRIM UPDATE', line=708)
W('24,3044', 0o65017, '', 'AD', 'ONE', '      THESE CHECKS ARE ONLY NEEDED', line=709)
W('24,3045', 0o00006, '', 'EXTEND', '', '      FOR A LESS THAN 0.4 SEC BURN', line=710)
W('24,3046', 0o13057, '', 'BZF', 'BTRIMR', 'NO.  INITIALIZATION NOT COMPLETE', line=711)
W('24,3047', 0o40102, '', 'CS', 'FLAGWRD6', 'YES, CHECK IF TVC', line=712)
W('24,3050', 0o74105, '', 'MASK', 'OCT60000', line=713)
W('24,3051', 0o00006, '', 'EXTEND', line=714)
W('24,3052', 0o63057, '', 'BZMF', 'BTRIMR', 'NO, NOT TVC YET', line=715)
W('24,3053', 0o31601, 'BESTTRIM', 'CAE', 'DELPBAR', 'UPDATE TRIMS WITH DELFILTER VALUES', line=716)
W('24,3054', 0o55423, '', 'TS', 'PACTOFF', line=717)
W('24,3055', 0o31603, '', 'CAE', 'DELYBAR', line=718)
W('24,3056', 0o55424, '', 'TS', 'YACTOFF', line=719)
W('24,3057', 0o00002, 'BTRIMR', 'TC', 'Q', line=720)
#   EBANK= DAPDATR1
W('24,3060', 0o03205, 'STEERADS', '2CADR', 'STEERING', kind='data', line=722)
W('24,3061', 0o50066, kind='data', line=722)

W('24,3062', 0o37703, '.6SECT5', 'OCT', '37703', kind='data', line=724)
W('24,3063', 0o00000, '5SECDP', 'DEC', '0', 'MAKE DP 5SEC', kind='data', line=725)
W('24,3064', 0o00764, '5SEC', 'DEC', '500', kind='data', line=726)
W('24,3065', 0o02202, 'OCT02202', 'OCT', '02202', 'BITS 2, 8, 11 FOR CHANNEL 12 TVC/OPTICS', kind='data', line=727)
#   EBANK= DAPDATR1
W('24,3066', 0o02147, 'TVCON2C', '2CADR', 'TVCDAPON', kind='data', line=729)
W('24,3067', 0o36066, kind='data', line=729)

W('24,3070', 0o00004, '', 'INHINT', line=731)
W('24,3071', 0o43065, 'TVCZAP', 'CS', 'OCT02202', 'DISABLE TVC AND OPT ERR CNTRLS, REENGAGE', line=732)
W('24,3072', 0o00006, '', 'EXTEND', '', '      OPTICS DAC', line=733)
W('24,3073', 0o03012, '', 'WAND', 'CHAN12', line=734)
W('24,3074', 0o45017, '', 'CS', 'BIT1', 'ENABLE T4RUPT OPTICS MONITOR .... PERMIT', line=735)
W('24,3075', 0o55303, '', 'TS', 'OPTIND', '      OPTICS-ZERO BUT NOT OPTICS-DRIVE', line=736)
W('24,3076', 0o35021, '', 'CAF', 'ZERO', 'CLEAR NVWORD1 IN CASE CLOCKJOB WAITING', line=737)
W('24,3077', 0o55145, '', 'TS', 'NVWORD1', line=738)
W('24,3100', 0o45005, '', 'CS', 'BIT11', 'CLEAR TIMRFLAG TO STOP CLOKTASK', line=739)
W('24,3101', 0o70103, '', 'MASK', 'FLAGWRD7', line=740)
W('24,3102', 0o54103, '', 'TS', 'FLAGWRD7', line=741)
W('24,3103', 0o00002, '', 'TC', 'Q', line=742)
#   EBANK= DAPDATR1
W('24,3104', 0o43020, 'UPDATEVG', 'STQ', 'BON', kind='interp', line=744)
W('24,3105', 0o03730, '', '', 'QTEMP1', kind='operand', line=745)
W('24,3106', 0o01307, '', '', 'XDELVFLG', kind='operand', line=746)
W('24,3107', 0o51133, '', '', 'CALL40.8', kind='operand', line=747)

W('24,3110', 0o50135, '', 'SLOAD', 'BMN', kind='interp', line=749)
W('24,3111', 0o03343, '', '', 'NBRCYCLS', kind='operand', line=750)
W('24,3112', 0o51137, '', '', 'SETUP.9', kind='operand', line=751)
# Page 700

W('24,3113', 0o53375, '', 'VLOAD', 'VAD', kind='interp', line=754)
W('24,3114', 0o03345, '', '', 'DELVSUM', kind='operand', line=755)
W('24,3115', 0o03433, '', '', 'DELVREF', kind='operand', line=756)
W('24,3116', 0o03353, '', 'STORE', 'DELVSUMP', kind='interp', line=757)
W('24,3117', 0o77776, '', 'EXIT', kind='interp', line=758)
W('24,3120', 0o35017, '', 'CA', 'ONE', line=759)
W('24,3121', 0o61742, '', 'AD', 'NBRCYCLS', line=760)
W('24,3122', 0o55743, '', 'TS', 'NBRCYCLP', line=761)

W('24,3123', 0o05412, '', 'TC', 'PHASCHNG', 'TYPE B RESTART RESTART BELOW AND 5.3 REREADACCS', line=763)
W('24,3124', 0o10035, '', 'OCT', '10035', kind='data', line=764)

W('24,3125', 0o31743, '', 'CA', 'NBRCYCLP', line=766)
W('24,3126', 0o55742, '', 'TS', 'NBRCYCLS', line=767)
W('24,3127', 0o06006, '', 'TC', 'INTPRET', line=768)
W('24,3130', 0o77775, '', 'VLOAD', kind='interp', line=769)
W('24,3131', 0o03353, '', '', 'DELVSUMP', kind='operand', line=770)
W('24,3132', 0o03345, '', 'STORE', 'DELVSUM', kind='interp', line=771)

W('24,3133', 0o77624, 'CALL40.8', 'CALL', kind='interp', line=773)
W('24,3134', 0o34153, '', '', 'S40.8', kind='operand', line=774)
W('24,3135', 0o77650, '', 'GOTO', kind='interp', line=775)
W('24,3136', 0o03730, '', '', 'QTEMP1', kind='operand', line=776)

W('24,3137', 0o67214, 'SETUP.9', 'BON', 'SLOAD', kind='interp', line=778)
W('24,3140', 0o01310, '', '', 'FIRSTFLG', kind='operand', line=779)
W('24,3141', 0o51154, '', '', 'SURELY.9', kind='operand', line=780)
W('24,3142', 0o03344, '', '', 'NBRCYCLP', kind='operand', line=781)
W('24,3143', 0o74301, '', 'NORM', 'VXSC', '(NORM HANDLES ZERO PROPERLY)', kind='interp', line=782)
W('24,3144', 0o00047, '', '', 'X1', kind='operand', line=783)
W('24,3145', 0o03705, '', '', 'BDT', kind='operand', line=784)
W('24,3146', 0o53257, '', 'VSR*', 'VAD', kind='interp', line=785)
W('24,3147', 0o20563, '', '', '0 -14D,1', kind='operand', line=786)
W('24,3150', 0o03646, '', '', 'VGTEMP', kind='operand', line=787)
W('24,3151', 0o77651, '', 'VSU', kind='interp', line=788)
W('24,3152', 0o03345, '', '', 'DELVSUM', kind='operand', line=789)
W('24,3153', 0o03721, '', 'STORE', 'VGPREV', kind='interp', line=790)
W('24,3154', 0o77776, 'SURELY.9', 'EXIT', kind='interp', line=791)
W('24,3155', 0o35003, '', 'CAF', 'PRIO10', line=792)
W('24,3156', 0o05147, '', 'TC', 'FINDVAC', line=793)
#   EBANK= DAPDATR1
W('24,3157', 0o02302, '', '2CADR', 'S40.9', kind='data', line=795)
W('24,3160', 0o34066, kind='data', line=795)

W('24,3161', 0o05372, '', 'TC', '2PHSCHNG', line=797)
W('24,3162', 0o00051, '', 'OCT', '00051', 'A, 1.5 = REDO40.9, PRIO 10', kind='data', line=798)
W('24,3163', 0o10035, '', 'OCT', '10035', kind='data', line=799)
W('24,3164', 0o06006, '', 'TC', 'INTPRET', line=800)
W('24,3165', 0o77775, '', 'VLOAD', kind='interp', line=801)
W('24,3166', 0o01171, '', '', 'RN', 'ACTIVE VEHICLE RADIUS VECTOR AT T1', kind='operand', line=802)
W('24,3167', 0o27570, '', 'STOVL', 'RINIT', kind='interp', line=803)
# Page 701
W('24,3170', 0o01177, '', '', 'VN', 'ACTIVE VEHICLE VELOCITY VECTOR AT T1', kind='operand', line=805)
W('24,3171', 0o17576, '', 'STODL', 'VINIT', kind='interp', line=806)
W('24,3172', 0o01205, '', '', 'PIPTIME', kind='operand', line=807)
W('24,3173', 0o03474, '', 'STORE', 'TNIT', kind='interp', line=808)
W('24,3174', 0o77621, '', 'BDSU', kind='interp', line=809)
W('24,3175', 0o03656, '', '', 'TPASS4', kind='operand', line=810)
W('24,3176', 0o27423, '', 'STOVL', 'DELLT4', kind='interp', line=811)
W('24,3177', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=812)
W('24,3200', 0o17345, '', 'STODL', 'DELVSUM', kind='interp', line=813)
W('24,3201', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=814)
W('24,3202', 0o03343, '', 'STORE', 'NBRCYCLS', kind='interp', line=815)
W('24,3203', 0o77650, '', 'GOTO', kind='interp', line=816)
W('24,3204', 0o51133, '', '', 'CALL40.8', kind='operand', line=817)
#   EBANK= DAPDATR1
W('24,3205', 0o06006, 'STEERING', 'TC', 'INTPRET', line=819)
W('24,3206', 0o77624, '', 'CALL', kind='interp', line=820)
W('24,3207', 0o51104, '', '', 'UPDATEVG', kind='operand', line=821)
W('24,3210', 0o77776, '', 'EXIT', kind='interp', line=822)
W('24,3211', 0o35007, '', 'CAF', 'BIT9', 'CHECK IMPULSW', line=823)
W('24,3212', 0o70076, '', 'MASK', 'FLAGWRD2', line=824)
W('24,3213', 0o10000, '', 'CCS', 'A', line=825)
W('24,3214', 0o13217, '', 'TCF', '+3', 'PRE-IGNITE, REQUEST ENG-OFF, OR POST-OFF', line=826)
W('24,3215', 0o04701, 'SERVXT', 'TC', 'POSTJUMP', line=827)
W('24,3216', 0o77227, '', 'CADR', 'SERVEXIT', kind='data', line=828)
W('24,3217', 0o35003, '', 'CAF', 'BIT13', 'CHECK ENGINE-ON/-OFF', line=829)
W('24,3220', 0o00006, '', 'EXTEND', line=830)
W('24,3221', 0o02011, '', 'RAND', 'DSALMOUT', line=831)
W('24,3222', 0o00006, '', 'EXTEND', line=832)
W('24,3223', 0o13215, '', 'BZF', 'SERVXT', 'ENGINE-OFF, SO PRE-IGNITE OR POST-OFF', line=833)
W('24,3224', 0o03366, '', 'TCR', 'E7SETTER', line=834)
#   EBANK= TIG
W('24,3225', 0o00004, '', 'INHINT', line=836)
W('24,3226', 0o00006, '', 'EXTEND', line=837)
W('24,3227', 0o31413, '', 'DCA', 'TIG', line=838)
W('24,3230', 0o52155, '', 'DXCH', 'MPAC', line=839)
W('24,3231', 0o00006, '', 'EXTEND', line=840)
W('24,3232', 0o40025, '', 'DCS', 'TIME2', line=841)
W('24,3233', 0o20155, '', 'DAS', 'MPAC', line=842)
W('24,3234', 0o07224, '', 'TCR', 'DPAGREE', line=843)
W('24,3235', 0o30155, '', 'CAE', 'MPAC +1', '(LESS THAN 6 (OR 4) SECONDS TO GO)', line=844)
W('24,3236', 0o10000, '', 'CCS', 'A', 'PROTECT AGAINST NEG/ZRO W.L. CALL', line=845)
W('24,3237', 0o13242, '', 'TCF', '+3', line=846)
W('24,3240', 0o13242, '', 'TCF', '+2', line=847)
W('24,3241', 0o35021, '', 'CAF', 'ZERO', line=848)
W('24,3242', 0o65017, '', 'AD', 'ONE', line=849)
W('24,3243', 0o56001, '', 'XCH', 'L', line=850)
W('24,3244', 0o35021, '', 'CA', 'ZERO', line=851)
W('24,3245', 0o53430, '', 'DXCH', 'TGO', line=852)
W('24,3246', 0o31430, '', 'CA', 'TGO +1', line=853)
W('24,3247', 0o05245, '', 'TC', 'WAITLIST', line=854)
# Page 702
#   EBANK= TGO
W('24,3250', 0o02766, '', '2CADR', 'ENGINOFF', kind='data', line=857)
W('24,3251', 0o50067, kind='data', line=857)

W('24,3252', 0o05372, '', 'TC', '2PHSCHNG', line=859)
W('24,3253', 0o40153, '', 'OCT', '40153', 'A, 3.15 = ENGINOFF (TGO+1) .... NOTE GROUP', kind='data', line=860)
W('24,3254', 0o10035, '', 'OCT', '10035', 'B, 5.3 = REREADAC, AND START BELOW', kind='data', line=861)
W('24,3255', 0o05560, '', 'TC', 'DOWNFLAG', 'CLEAR IMPULSW, ENGINOFF IS NOW SET UP', line=862)
W('24,3256', 0o00044, '', 'ADRES', 'IMPULSW', 'RESTARTS OK', kind='data', line=863)
W('24,3257', 0o13215, '', 'TCF', 'SERVXT', line=864)

# Page 703
# ROUTINE ** CLOKTASK ** DESCRIPTION

#   EBANK= TIG
W('24,3260', 0o35005, 'CLOKTASK', 'CAF', 'BIT11', 'IS TIMRFLAG SET', line=870)
W('24,3261', 0o70103, '', 'MASK', 'FLAGWRD7', line=871)
W('24,3262', 0o10000, '', 'CCS', 'A', line=872)
W('24,3263', 0o13267, '', 'TCF', 'CLOCKON', line=873)
W('24,3264', 0o05412, '', 'TC', 'PHASCHNG', line=874)
W('24,3265', 0o00006, '', 'OCT', '00006', 'KILL RESTART', kind='data', line=875)
W('24,3266', 0o05324, '', 'TC', 'TASKOVER', line=876)

W('24,3267', 0o00006, 'CLOCKON', 'EXTEND', line=878)
W('24,3270', 0o30025, '', 'DCA', 'TIME2', line=879)
W('24,3271', 0o53661, '', 'DXCH', 'TTOGO', line=880)
W('24,3272', 0o00006, '', 'EXTEND', line=881)
W('24,3273', 0o41413, '', 'DCS', 'TIG', line=882)
W('24,3274', 0o21661, '', 'DAS', 'TTOGO', line=883)

W('24,3275', 0o35041, 'SETCLOCK', 'CAF', '1SEC', line=885)
W('24,3276', 0o05245, '', 'TC', 'WAITLIST', line=886)
#   EBANK= TIG
W('24,3277', 0o03260, '', '2CADR', 'CLOKTASK', kind='data', line=888)
W('24,3300', 0o50067, kind='data', line=888)

W('24,3301', 0o11145, '', 'CCS', 'NVWORD1', line=890)
W('24,3302', 0o13305, '', 'TCF', '+3', line=891)
W('24,3303', 0o13315, '', 'TCF', 'SETTB6', line=892)

W('24,3304', 0o13305, '', 'TCF', '+1', line=894)
W('24,3305', 0o42423, '', 'CS', 'V06N85B', 'CHECK FOR V06N85B (P41)', line=895)
W('24,3306', 0o61145, '', 'AD', 'NVWORD1', line=896)
W('24,3307', 0o00006, '', 'EXTEND', line=897)
W('24,3310', 0o13320, '', 'BZF', 'SETUPDYN', 'V06N85, SO UPDATE N85 FOR DYNAMIC DISP', line=898)

W('24,3311', 0o37664, '', 'CAF', 'PRIO27', line=900)
W('24,3312', 0o05134, '', 'TC', 'NOVAC', line=901)
#   EBANK= DAPDATR1
W('24,3313', 0o03332, '', '2CADR', 'CLOCKJOB', kind='data', line=903)
W('24,3314', 0o50066, kind='data', line=903)

W('24,3315', 0o40025, 'SETTB6', 'CS', 'TIME1', 'SET GROUP6 TIMEBASE', line=905)
W('24,3316', 0o55065, '', 'TS', 'TBASE6', line=906)
W('24,3317', 0o15324, '', 'TCF', 'TASKOVER', line=907)

W('24,3320', 0o37664, 'SETUPDYN', 'CAF', 'PRIO27', 'SET UP A JOB TO UPDATE N85 (FOR P41=V06)', line=909)
W('24,3321', 0o05147, '', 'TC', 'FINDVAC', line=910)
#   EBANK= DAPDATR1
W('24,3322', 0o03325, '', '2CADR', 'DYNDISP', kind='data', line=912)
W('24,3323', 0o50066, kind='data', line=912)

W('24,3324', 0o13315, '', 'TCF', 'SETTB6', 'CLOSE OUT CLOCKTASK', line=914)
# Page 704
W('24,3325', 0o06006, 'DYNDISP', 'TC', 'INTPRET', 'UPDATE N85 FOR A DYNAMIC V06N85 IN P41.', line=916)
W('24,3326', 0o77624, '', 'CALL', '', '      PRIOR TO BLANKING AND AVEG (V16N85)', kind='interp', line=917)
W('24,3327', 0o50370, '', '', 'P40CNV85', kind='operand', line=918)
W('24,3330', 0o77776, '', 'EXIT', kind='interp', line=919)
W('24,3331', 0o13342, '', 'TCF', 'CKNVWRD1', line=920)

# Page 705
# ROUTINE ** CLOCKJOB ** DESCRIPTION

#   EBANK= DAPDATR1
W('24,3332', 0o30032, 'CLOCKJOB', 'CA', 'CDUX', line=926)
W('24,3333', 0o54772, '', 'TS', 'CDUSPOTX', line=927)
W('24,3334', 0o30033, '', 'CA', 'CDUY', line=928)
W('24,3335', 0o54766, '', 'TS', 'CDUSPOTY', line=929)
W('24,3336', 0o30034, '', 'CA', 'CDUZ', line=930)
W('24,3337', 0o54770, '', 'TS', 'CDUSPOTZ', line=931)
W('24,3340', 0o04662, '', 'TC', 'BANKCALL', line=932)
W('24,3341', 0o47555, '', 'CADR', 'QUICTRIG', kind='data', line=933)
W('24,3342', 0o00004, 'CKNVWRD1', 'INHINT', line=934)
W('24,3343', 0o11145, '', 'CCS', 'NVWORD1', 'DETERMINE FUNCTION, INDICATED BY NVWORD1', line=935)
W('24,3344', 0o13363, '', 'TCF', 'NOFLASH', line=936)
W('24,3345', 0o15217, '', 'TCF', 'ENDOFJOB', line=937)
W('24,3346', 0o13355, '', 'TCF', 'ENGREQST', 'SPS ENGINE-ON-ENABLE V99 FLASH', line=938)
W('24,3347', 0o32425, 'FAILDSP', 'CAF', 'V06N40', 'SPS ENGINE-FAILED V97 FLASH', line=939)
W('24,3350', 0o04662, '', 'TC', 'BANKCALL', line=940)
W('24,3351', 0o20715, '', 'CADR', 'CLOCPLAY', kind='data', line=941)
W('24,3352', 0o13432, '', 'TCF', 'V97T', 'TERMINATE', line=942)
W('24,3353', 0o13465, '', 'TCF', 'V97P', 'PROCEED', line=943)
W('24,3354', 0o13514, '', 'TCF', 'V97E', 'ENTER', line=944)

W('24,3355', 0o32425, 'ENGREQST', 'CAF', 'V06N40', line=946)
W('24,3356', 0o04662, '', 'TC', 'BANKCALL', line=947)
W('24,3357', 0o20715, '', 'CADR', 'CLOCPLAY', 'LINUS MAKES IT A REDO, INHINT OK', kind='data', line=948)
W('24,3360', 0o13402, '', 'TCF', 'V99T', 'TERMINATE', line=949)
W('24,3361', 0o13410, '', 'TCF', 'V99P', 'PROCEED', line=950)
W('24,3362', 0o13374, '', 'TCF', 'V99E', 'ENTER', line=951)

W('24,3363', 0o31145, 'NOFLASH', 'CAE', 'NVWORD1', 'DISPLAY NVWORD1 NORMALLY', line=953)
W('24,3364', 0o04662, '', 'TC', 'BANKCALL', line=954)
W('24,3365', 0o20707, '', 'CADR', 'REGODSP', kind='data', line=955)

W('24,3366', 0o35060, 'E7SETTER', 'CAF', 'EBANK7', line=957)
W('24,3367', 0o54003, '', 'TS', 'EBANK', line=958)
#   EBANK= TIG
W('24,3370', 0o00002, '', 'TC', 'Q', line=960)

W('24,3371', 0o35057, 'E6SETTER', 'CAF', 'EBANK6', 'SET UP EBANK6', line=962)
W('24,3372', 0o54003, '', 'TS', 'EBANK', line=963)
#   EBANK= DAPDATR1
W('24,3373', 0o00002, '', 'TC', 'Q', line=965)

#   EBANK= DAPDATR1
W('24,3374', 0o05372, 'V99E', 'TC', '2PHSCHNG', line=968)
W('24,3375', 0o00006, '', 'OCT', '00006', 'KILL PRE40.6/CLOKTASK PROTECTION', kind='data', line=969)
W('24,3376', 0o05024, '', 'OCT', '05024', 'C, PRIORITY NEXT, JOB BELOW', kind='data', line=970)
# Page 706
W('24,3377', 0o27000, '', 'OCT', '27000', kind='data', line=972)
W('24,3400', 0o03070, 'V99EJOB', 'TCR', 'TVCZAP -1', 'WIPE OUT TVC, CLOKTASK', line=973)
W('24,3401', 0o12254, '', 'TCF', 'P40RCS', 'V16N85 POST-BURN OPERATIONS', line=974)

#   EBANK= DAPDATR1
W('24,3402', 0o05372, 'V99T', 'TC', '2PHSCHNG', '(ENTRY FROM V97T FLOW TOO)', line=977)
W('24,3403', 0o00006, '', 'OCT', '00006', 'KILL PRE40.6/CLOKTASK PROTECTION', kind='data', line=978)
W('24,3404', 0o05024, '', 'OCT', '05024', 'C, PRIORITY NEXT, JOB BELOW', kind='data', line=979)
W('24,3405', 0o27000, '', 'OCT', '27000', kind='data', line=980)
W('24,3406', 0o03070, 'V99TJOB', 'TCR', 'TVCZAP -1', 'WIPE OUT TVC, CLOKTASK', line=981)
W('24,3407', 0o12275, '', 'TCF', 'POST41', 'AVEGEXIT, SETMAXDB, GOTOPOOH', line=982)

W('24,3410', 0o00004, 'V99P', 'INHINT', line=984)
W('24,3411', 0o30103, '', 'CAE', 'FLAGWRD7', 'CHECK ASTN FLAG FOR PRIOR V99P', line=985)
W('24,3412', 0o75004, '', 'MASK', 'BIT12', line=986)
W('24,3413', 0o10000, '', 'CCS', 'A', line=987)
W('24,3414', 0o13427, '', 'TCF', 'V99P/TIG', 'YES, THIS MUST BE A RESTART ENTRY', line=988)

W('24,3415', 0o35004, 'ASTNV99P', 'CAF', 'BIT12', 'SET ASTN FLAG', line=990)
W('24,3416', 0o26103, '', 'ADS', 'FLAGWRD7', line=991)
W('24,3417', 0o30103, '', 'CAE', 'FLAGWRD7', 'CHECK IGN FLAG FOR TIG-0 ARRIVAL', line=992)
W('24,3420', 0o75003, '', 'MASK', 'BIT13', line=993)
W('24,3421', 0o00006, '', 'EXTEND', line=994)
W('24,3422', 0o13427, '', 'BZF', 'V99P/TIG', 'NO, CLEAR THE V99 AND WAIT FOR TIG-0', line=995)

W('24,3423', 0o35017, 'ENDV99PI', 'CAF', 'BIT1', 'TIG-0 HAS COME ALREADY', line=997)
W('24,3424', 0o05245, '', 'TC', 'WAITLIST', 'SET UP IGNITION HERE', line=998)
#   EBANK= DAPDATR1
W('24,3425', 0o02625, '', '2CADR', 'IGNITION', kind='data', line=1000)
W('24,3426', 0o50066, kind='data', line=1000)

W('24,3427', 0o32425, 'V99P/TIG', 'CAF', 'V06N40', 'CLEAR THE V99 FLASH AND WAIT FOR TIG-0', line=1002)
W('24,3430', 0o55145, '', 'TS', 'NVWORD1', line=1003)
W('24,3431', 0o15217, 'ENDV99P', 'TCF', 'ENDOFJOB', line=1004)

#   EBANK= CSMMASS
W('24,3432', 0o05372, 'V97T', 'TC', '2PHSCHNG', line=1007)
W('24,3433', 0o00006, '', 'OCT', '00006', 'KILL GROUP 6 (CLOKTASK)', kind='data', line=1008)
W('24,3434', 0o40674, '', 'OCT', '40674', 'A, 4.67 = V97TTASK (-0 CS), TBASE NOW', kind='data', line=1009)
W('24,3435', 0o35017, '', 'CAF', 'BIT1', line=1010)
W('24,3436', 0o05235, '', 'TC', 'TWIDDLE', line=1011)
W('24,3437', 0o03441, '', 'ADRES', 'V97TTASK', 'KEEP EBANK6 FOR MASSES, SPSOFF, ETC.', kind='data', line=1012)
W('24,3440', 0o15217, '', 'TCF', 'ENDOFJOB', line=1013)

#   EBANK= CSMMASS
W('24,3441', 0o35021, 'V97TTASK', 'CAF', 'ZERO', 'DISABLE CLOCKJOB', line=1016)
W('24,3442', 0o55145, '', 'TS', 'NVWORD1', line=1017)
W('24,3443', 0o32434, '', 'CAF', '3MDOT', '3 SECONDS OF MDOT (2-4 SEC ENGFAIL', line=1018)
W('24,3444', 0o61474, '', 'AD', 'CSMMASS', '      DETECTION) NOT LOST BECAUSE THRUST', line=1019)
W('24,3445', 0o55652, '', 'TS', 'MASSTMP', '      FAILED.  COPYCYCLE FOR MASSBACK', line=1020)
# Page 707
W('24,3446', 0o05412, '', 'TC', 'PHASCHNG', line=1022)
W('24,3447', 0o05014, '', 'OCT', '05014', 'C, DELTAT NEXT, TASK BELOW, IN', kind='data', line=1023)
W('24,3450', 0o77777, '', 'DEC', '-0', '-0 CS', kind='data', line=1024)

W('24,3451', 0o03017, '', 'TCR', 'SPSOFF', 'SHUTDOWN SPS ENGINE, MASS UPDATE, ETC.', line=1026)
W('24,3452', 0o05412, '', 'TC', 'PHASCHNG', line=1027)
W('24,3453', 0o00714, '', 'OCT', '00714', 'A, 4.71 = V97TRCS (250 CS), TBASE OLD', kind='data', line=1028)
W('24,3454', 0o05267, '', 'TC', 'FIXDELAY', 'DELAY 2.5 SECONDS FOR (POSSIBLE) TAIL-', line=1029)
W('24,3455', 0o00372, '', 'DEC', '250', '      OFF (FALSE THRUST-LOSS)', kind='data', line=1030)

#   EBANK= DAPDATR1
W('24,3456', 0o04740, 'V97TRCS', 'TC', 'IBNKCALL', 'RCS DAP IN 0.6SEC, SETTING T5 BITS TO', line=1033)
W('24,3457', 0o42024, '', 'CADR', 'RCSDAPON', '      KILL TVCEXEC/TVCROLLDAP STARTS', kind='data', line=1034)
W('24,3460', 0o37664, '', 'CAF', 'PRIO27', 'SET UP V99T FOR TVCZAP AND POST41 (SET-', line=1035)
W('24,3461', 0o05134, '', 'TC', 'NOVAC', '      MAXDB AND GOTOPOOH)', line=1036)
#   EBANK= DAPDATR1  # EBANK6 FOR SETMAXDB IN POST41
W('24,3462', 0o03402, '', '2CADR', 'V99T', kind='data', line=1038)
W('24,3463', 0o50066, kind='data', line=1038)

W('24,3464', 0o15324, 'ENDV97T', 'TCF', 'TASKOVER', line=1040)

#   EBANK= V97VCNTR
W('24,3465', 0o05412, 'V97P', 'TC', 'PHASCHNG', line=1043)
W('24,3466', 0o40734, '', 'OCT', '40734', 'A, 4.73 = V97PTASK (-0 CS), TBASE NOW', kind='data', line=1044)
W('24,3467', 0o35017, '', 'CAF', 'BIT1', line=1045)
W('24,3470', 0o05235, '', 'TC', 'TWIDDLE', line=1046)
W('24,3471', 0o03473, '', 'ADRES', 'V97PTASK', kind='data', line=1047)
W('24,3472', 0o15217, '', 'TCF', 'ENDOFJOB', line=1048)

#   EBANK= V97VCNTR
W('24,3473', 0o31444, 'V97PTASK', 'CAE', 'V97VCNTR', 'GET MASS UPDATES (TVCEXEC) GOING AGAIN', line=1051)
W('24,3474', 0o55643, '', 'TS', 'VCNTR', '      (ERRORS IF FLASE THRUST-LOSS AND/OR', line=1052)
# POOR SYNC OF MANUAL ENGINE-ON AND
# THE VERB 97 PROCEED)
W('24,3475', 0o32425, '', 'CAF', 'V06N40', 'REDISPLAY V06N40', line=1055)
W('24,3476', 0o55145, '', 'TS', 'NVWORD1', line=1056)
W('24,3477', 0o05546, '', 'TC', 'UPFLAG', 'SET IDLEFAIL TO ALLOW R41-BYPASS, IN', line=1057)
W('24,3500', 0o00030, '', 'ADRES', 'IDLEFAIL', '      CASE OF UNFAVORABLE S40.8 SYNCH', kind='data', line=1058)
W('24,3501', 0o05546, '', 'TC', 'UPFLAG', 'SET STEERSW TO RE-ENABLE STEERING', line=1059)
W('24,3502', 0o00042, '', 'ADRES', 'STEERSW', kind='data', line=1060)
W('24,3503', 0o05412, '', 'TC', 'PHASCHNG', line=1061)
W('24,3504', 0o00134, '', 'OCT', '00134', 'A, 4.13 = R40ENABL (200 CS), TBASE OLD', kind='data', line=1062)
W('24,3505', 0o05267, '', 'TC', 'FIXDELAY', 'WAIT 2 SECONDS, THEN', line=1063)
W('24,3506', 0o00310, '', 'DEC', '200', kind='data', line=1064)

#   EBANK= WHOCARES
W('24,3507', 0o05560, 'R40ENABL', 'TC', 'DOWNFLAG', 'RE-ENABLE R40 BY CLEARING IDLEFAIL', line=1067)
W('24,3510', 0o00030, '', 'ADRES', 'IDLEFAIL', kind='data', line=1068)
W('24,3511', 0o05412, '', 'TC', 'PHASCHNG', line=1069)
W('24,3512', 0o00004, '', 'OCT', '00004', 'KILL GROUP 4', kind='data', line=1070)
# Page 708
W('24,3513', 0o15324, 'ENDV97P', 'TCF', 'TASKOVER', line=1072)

#   EBANK= WHOCARES
W('24,3514', 0o05412, 'V97E', 'TC', 'PHASCHNG', line=1075)
W('24,3515', 0o40534, '', 'OCT', '40534', 'A, 4.53 = V97ETASK (-0 CS), TBASE NOW', kind='data', line=1076)
W('24,3516', 0o35017, '', 'CAF', 'BIT1', line=1077)
W('24,3517', 0o05245, '', 'TC', 'WAITLIST', line=1078)
#   EBANK= TIG
W('24,3520', 0o03523, '', '2CADR', 'V97ETASK', kind='data', line=1080)
W('24,3521', 0o50067, kind='data', line=1080)

W('24,3522', 0o15217, '', 'TCF', 'ENDOFJOB', line=1082)

#   EBANK= TIG
W('24,3523', 0o44112, 'V97ETASK', 'CS', 'OCT24', 'FORCE R1 OF V06N40 TO READ  59X59', line=1085)
W('24,3524', 0o55412, '', 'TS', 'TIG', line=1086)
W('24,3525', 0o32425, '', 'CAF', 'V06N40', 'REDISPLAY V06N40', line=1087)
W('24,3526', 0o55145, '', 'TS', 'NVWORD1', line=1088)
W('24,3527', 0o03371, '', 'TCR', 'E6SETTER', 'RETURN TO EBANK6 FOR REST OF V97ETASK', line=1089)
#   EBANK= CSMMASS
W('24,3530', 0o32434, '', 'CAF', '3MDOT', '3 SECONDS OF MDOT (2-4 SEC ENGFAIL', line=1091)
W('24,3531', 0o61474, '', 'AD', 'CSMMASS', '      DETECTION) NOT LOST BECAUSE THRUST', line=1092)
W('24,3532', 0o55652, '', 'TS', 'MASSTMP', '      FAILED....COPYCYCLE FOR MASSBACK', line=1093)
W('24,3533', 0o05412, '', 'TC', 'PHASCHNG', line=1094)
W('24,3534', 0o00754, '', 'OCT', '00754', 'A, 4.75 = SPSOFF97 (-0 CS), TBASE OLD', kind='data', line=1095)
W('24,3535', 0o03017, 'SPSOFF97', 'TCR', 'SPSOFF', line=1096)
W('24,3536', 0o05412, '', 'TC', 'PHASCHNG', line=1097)
W('24,3537', 0o00114, '', 'OCT', '00114', 'A, 4.11 = V97E40.6 (250 CS), TBASE OLD', kind='data', line=1098)
W('24,3540', 0o05267, '', 'TC', 'FIXDELAY', 'DELAY 2.5 SECONDS FOR (POSSIBLE) TAIL-', line=1099)
W('24,3541', 0o00372, '', 'DEC', '250', '      OFF (FALSE THRUST-LOSS)', kind='data', line=1100)

#   EBANK= DAPDATR1
W('24,3542', 0o35017, 'V97E40.6', 'CAF', 'BIT1', line=1103)
W('24,3543', 0o05245, '', 'TC', 'WAITLIST', line=1104)
#   EBANK= CNTR
W('24,3544', 0o02241, '', '2CADR', 'PRE40.6', 'USE S40.6 RESTART ENTRY TO TRIM ENGINE', kind='data', line=1106)
W('24,3545', 0o40066, kind='data', line=1106)

W('24,3546', 0o04740, '', 'TC', 'IBNKCALL', 'RCS DAP IN 0.6SEC, SETTING T5 BITS TO', line=1108)
W('24,3547', 0o42024, '', 'CADR', 'RCSDAPON', '      KILL TVCEXEC/TVCROLLDAP STARTS.', kind='data', line=1109)
# LEAVE NARROW DEADBAND FOR REIGNITE.

W('24,3550', 0o05372, '', 'TC', '2PHSCHNG', line=1112)
W('24,3551', 0o00026, '', 'OCT', '00026', 'A, 6.2 = PRE40.6 (-0 CS), CLOKTASK (1 SEC)', kind='data', line=1113)
W('24,3552', 0o05014, '', 'OCT', '05014', 'C, DELTAT NEXT, TASK BELOW, IN', kind='data', line=1114)
W('24,3553', 0o77777, '', 'DEC', '-0', '-0 CS.', kind='data', line=1115)

W('24,3554', 0o45066, 'QUICKIGN', 'CS', 'PRIO14', 'CLEAR ASTNFLAG AND SET IGNFLAG FOR', line=1117)
W('24,3555', 0o70103, '', 'MASK', 'FLAGWRD7', '      IMMEDIATE V99 RESPONSE.', line=1118)
W('24,3556', 0o65003, '', 'AD', 'BIT13', line=1119)
W('24,3557', 0o54103, '', 'TS', 'FLAGWRD7', line=1120)
W('24,3560', 0o05267, '', 'TC', 'FIXDELAY', 'DELAY TO ALLOW TIME FOR PRE40.6', line=1121)
# Page 709
W('24,3561', 0o00036, '', 'DEC', '30', kind='data', line=1123)

W('24,3562', 0o45007, 'V99FLASH', 'CS', 'BIT9', 'CAUSE V99 TO FLASH', line=1125)
W('24,3563', 0o55145, '', 'TS', 'NVWORD1', line=1126)
W('24,3564', 0o05372, '', 'TC', '2PHSCHNG', line=1127)
W('24,3565', 0o40774, '', 'OCT', '40774', 'A, 4.77 = TIG-0 (-0 CS) TBASE FOR PREPTVC', kind='data', line=1128)
W('24,3566', 0o00033, '', 'OCT', '00033', 'A, 3.3 = S40.13 (PRIO 20)', kind='data', line=1129)
W('24,3567', 0o35002, '', 'CAF', 'PRIO20', 'SET UP TIMEBURN', line=1130)
W('24,3570', 0o05147, '', 'TC', 'FINDVAC', line=1131)
#   EBANK= TGO
W('24,3571', 0o02427, '', '2CADR', 'S40.13', kind='data', line=1133)
W('24,3572', 0o34067, kind='data', line=1133)

W('24,3573', 0o15324, 'ENDV97E', 'TCF', 'TASKOVER', 'WAIT FOR CLOCKJOB (IMMEDIATE) REACTION', line=1135)
# TO FLASHING V99 RESPONSE.

# MOD N02                               LOG SECTION P40-P47
# MOD BY ZELDIN
#
# FUNCTIONAL DESCRIPTION
# COMPUTE INITIAL THRUST DIRECTION(UT) AND INITIAL VALUE OF VG
# VECTOR(VGTIG).
#
# CALLING SEQUENCE
# L       CALL
# L+1             S40.1
#
# NORMAL EXIT MODE
# AT L+2 OF CALLING SEQUENCE (GOTO L+2) NORMAL RETURN OR
# ERROR RETURN IF NOSOFLAG =1
#
# SUBROUTINES CALLED
# CSMPREC
# INITVEL
# CALCGRAV
# MIDGIM
#
# ALARM OR ABORT EXIT MODES
# L+2 OF CALLING SEQUENCE, UNSOLVABLE CONIC IF NOSOFLAG=1
#
# ERASABLE INITIALIZATION REQUIRED
# WEIGHT/G        ANTICIPATED VEHICLE MASS        SP B16 KGM
# XDELVFLG        1=DELTA-V MANEUVER, 0=AIMPT STEER
# IF DELTA-V MANEUVER:
# DELVSIN         SPECIFIED DELTA-V REQUIRED IN
# INERTIAL COORDS. OF ACTIVE VEHICLE
# AT TIME OF IGNITION             VECTOR B7 M/CS
# DELVSAB         MAG. OF DELVSIN                 DP B7 M/CS
# RTIG            POSITION AT TIME OF IGNITION    VECTOR B29 M
# VTIG            VELOCITY AT TIME OF IGNITION    VECTOR B7 M/CS.
# CSTEER = 0                                      DP
# IF AIMPOINT STEERING:
# IF AIMPT STEER
# TIG             TIME OF IGNITION                DP B28 CS
# RTARG           POSITION TARGET TIME            VECTOR B29 M
# CSTEER = ECSTEER (GR 0)                         DP B1
# Page 710
# TPASS4 -- TIME OF ARRIVAL AT AIMPOINT
#
# OUTPUT
# UT              1/2 UNIT VECTOR ALIGNED WITH THRUST DIRETION IN REF COOR
# VGTIG           INITIAL VALUE OF VELOCITY
# TO BE GAINED (INERT. COORD.)            VECTOR B7 M/CS
# DELVLVC         VGTIG IN LOC. VERT. COORDS.             B7 M/CS
# F               NOMINAL THRUST FOR ENG USED FOR S40.13  DP B7 M-NEWT
# BDT             V REQUIRED AT TIG -V REQUIRED AT (TIG-2SEC)
# -GDT            FOR S40.13                              VECT B7 M/CS
# RTIG            CALC IN S40.1B (AIMPT) FOR S40.2,3      VECTOR B29M
# POSITION AT TIME OF IGNITION
#
# DEBRIS        QTEMP1
# MPAC, QPRET
# PUSHLIST
# RTX2,RTX1

#   BANK 14
#   SETLOC P40S1
#   BANK

#   COUNT 16/S40.1

W('16,2020', 0o77214, 'S40.1', 'SET', 'VLOAD', kind='interp', line=1203)
W('16,2021', 0o01070, '', '', 'FIRSTFLG', kind='operand', line=1204)
W('16,2022', 0o11566, '', '', 'LO6ZEROS', kind='operand', line=1205)
W('16,2023', 0o03705, '', 'STORE', 'BDT', kind='interp', line=1206)
W('16,2024', 0o43020, '', 'STQ', 'BOF', kind='interp', line=1207)
W('16,2025', 0o03657, '', '', 'QTEMP', kind='operand', line=1208)
W('16,2026', 0o01347, '', '', 'XDELVFLG', kind='operand', line=1209)
W('16,2027', 0o34116, '', '', 'S40.1B', 'LAMBERT', kind='operand', line=1210)
W('16,2030', 0o51575, '', 'VLOAD', 'ABVAL', 'EXTERNAL DELTA-V', kind='interp', line=1211)
W('16,2031', 0o03646, '', '', 'DELVSIN', kind='operand', line=1212)
W('16,2032', 0o03654, '', 'STORE', 'DELVSAB', 'COMPUTE FOR P30/P40 INTERFACE', kind='interp', line=1213)
# THUS PERMITTING MODULE-ONLY CHANGE
W('16,2033', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=1215)
W('16,2034', 0o00001, '', '', '0', kind='operand', line=1216)
W('16,2035', 0o03640, '', '', 'VTIG', kind='operand', line=1217)
W('16,2036', 0o03576, '', 'STORE', 'VINIT', kind='interp', line=1218)
W('16,2037', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1219)
W('16,2040', 0o03632, '', '', 'RTIG', kind='operand', line=1220)
W('16,2041', 0o27713, '', 'STOVL', 'UT', 'UP IN UT', kind='interp', line=1221)
W('16,2042', 0o03632, '', '', 'RTIG', kind='operand', line=1222)
W('16,2043', 0o03570, '', 'STORE', 'RINIT', kind='interp', line=1223)
W('16,2044', 0o65236, '', 'VSQ', 'PDDL', kind='interp', line=1224)
W('16,2045', 0o00045, '', '', '36D', kind='operand', line=1225)
W('16,2046', 0o56275, '', 'DMPR', 'DDV', kind='interp', line=1226)
W('16,2047', 0o34152, '', '', 'THETACON', kind='operand', line=1227)
W('16,2050', 0o41205, '', 'DMP', 'DMP', kind='interp', line=1228)
W('16,2051', 0o03654, '', '', 'DELVSAB', kind='operand', line=1229)
W('16,2052', 0o03076, '', '', 'WEIGHT/G', kind='operand', line=1230)
W('16,2053', 0o77671, '', 'DDV', kind='interp', line=1231)
# Page 711
W('16,2054', 0o03727, '', '', 'F', kind='operand', line=1233)
W('16,2055', 0o24017, '', 'STOVL', '14D', kind='interp', line=1234)
W('16,2056', 0o03646, '', '', 'DELVSIN', kind='operand', line=1235)

W('16,2057', 0o74241, '', 'DOT', 'VXSC', kind='interp', line=1237)
W('16,2060', 0o03713, '', '', 'UT', kind='operand', line=1238)
W('16,2061', 0o03713, '', '', 'UT', kind='operand', line=1239)
W('16,2062', 0o41552, '', 'VSL2', 'PUSH', '(DELTAV.UP)UP SCALED AT 2(+7) P.D.L. 0', kind='interp', line=1240)
W('16,2063', 0o65245, '', 'BVSU', 'PDDL', 'DELTA VP SCALED AT 2(+7) P.D.L. 6', kind='interp', line=1241)
W('16,2064', 0o03646, '', '', 'DELVSIN', kind='operand', line=1242)
W('16,2065', 0o00017, '', '', '14D', kind='operand', line=1243)
W('16,2066', 0o63356, '', 'SIN', 'PDVL', kind='interp', line=1244)
W('16,2067', 0o00007, '', '', '6D', kind='operand', line=1245)
W('16,2070', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1246)
W('16,2071', 0o03713, '', '', 'UT', kind='operand', line=1247)
W('16,2072', 0o45561, '', 'VXSC', 'STADR', kind='interp', line=1248)
W('16,2073', 0o50056, '', 'STOVL', 'VGTIG', 'UNIT(VP X UP)SIN(THETAT/2) IN VGTIG.', kind='interp', line=1249)
W('16,2074', 0o65256, '', 'UNIT', 'PDDL', 'UNIT(DELTA VP) IN P.D.L. 6', kind='interp', line=1250)
W('16,2075', 0o00017, '', '', '14D', kind='operand', line=1251)
W('16,2076', 0o74346, '', 'COS', 'VXSC', kind='interp', line=1252)
W('16,2077', 0o74255, '', 'VAD', 'VXSC', kind='interp', line=1253)
W('16,2100', 0o03721, '', '', 'VGTIG', kind='operand', line=1254)
W('16,2101', 0o00045, '', '', '36D', kind='operand', line=1255)
W('16,2102', 0o53352, '', 'VSL2', 'VAD', kind='interp', line=1256)
W('16,2103', 0o77626, '', 'STADR', kind='interp', line=1257)
W('16,2104', 0o74056, '', 'STORE', 'VGTIG', 'VG IGNITION SCALED AT 2(+7) M/CS', kind='interp', line=1258)

W('16,2105', 0o77656, '', 'UNIT', kind='interp', line=1260)
W('16,2106', 0o27713, '', 'STOVL', 'UT', 'THRUST DIRECTION SCALED AT 2(+1)', kind='interp', line=1261)
W('16,2107', 0o03721, '', '', 'VGTIG', kind='operand', line=1262)
W('16,2110', 0o43006, '', 'PUSH', 'SET', kind='interp', line=1263)
W('16,2111', 0o01072, '', '', 'AVFLAG', kind='operand', line=1264)
W('16,2112', 0o77624, '', 'CALL', kind='interp', line=1265)
W('16,2113', 0o10647, '', '', 'MIDGIM', 'VGTIG IN LV COOR AT 2(+7)M/CS IN DELVLVC', kind='operand', line=1266)
W('16,2114', 0o77650, '', 'GOTO', kind='interp', line=1267)
W('16,2115', 0o03657, '', '', 'QTEMP', kind='operand', line=1268)
W('16,2116', 0o45345, 'S40.1B', 'DLOAD', 'DSU', 'LAMBERT', kind='interp', line=1269)
W('16,2117', 0o03413, '', '', 'TIG', kind='operand', line=1270)
W('16,2120', 0o36001, '', '', 'TWODT', kind='operand', line=1271)
W('16,2121', 0o14041, '', 'STODL', 'TDEC1', kind='interp', line=1272)
W('16,2122', 0o03656, '', '', 'TPASS4', kind='operand', line=1273)
W('16,2123', 0o77625, '', 'DSU', kind='interp', line=1274)
W('16,2124', 0o00041, '', '', 'TDEC1', kind='operand', line=1275)
W('16,2125', 0o37423, '', 'STCALL', 'DELLT4', kind='interp', line=1276)
W('16,2126', 0o61651, '', '', 'AGAIN', kind='operand', line=1277)
W('16,2127', 0o77775, '', 'VLOAD', kind='interp', line=1278)
W('16,2130', 0o03612, '', '', 'VIPRIME', kind='operand', line=1279)
W('16,2131', 0o17713, '', 'STODL', 'UT', kind='interp', line=1280)
W('16,2132', 0o03413, '', '', 'TIG', kind='operand', line=1281)
W('16,2133', 0o00041, '', 'STORE', 'TDEC1', kind='interp', line=1282)
# Page 712
W('16,2134', 0o77621, '', 'BDSU', kind='interp', line=1284)
W('16,2135', 0o03656, '', '', 'TPASS4', kind='operand', line=1285)
W('16,2136', 0o37423, '', 'STCALL', 'DELLT4', kind='interp', line=1286)
W('16,2137', 0o61651, '', '', 'AGAIN', kind='operand', line=1287)
W('16,2140', 0o41575, '', 'VLOAD', 'PUSH', kind='interp', line=1288)
W('16,2141', 0o03646, '', '', 'DELVEET3', kind='operand', line=1289)
W('16,2142', 0o03721, '', 'STORE', 'VGTIG', kind='interp', line=1290)
W('16,2143', 0o45014, '', 'SET', 'CALL', kind='interp', line=1291)
W('16,2144', 0o01072, '', '', 'AVFLAG', kind='operand', line=1292)
W('16,2145', 0o10647, '', '', 'MIDGIM', kind='operand', line=1293)
W('16,2146', 0o52001, '', 'SETPD', 'GOTO', kind='interp', line=1294)
W('16,2147', 0o00001, '', '', '0', kind='operand', line=1295)
W('16,2150', 0o61704, '', '', 'CALCUT', kind='operand', line=1296)

W('16,2151', 0o00024, 'THETACON', '2DEC', '.31830989 B-8', kind='data', line=1298)
W('16,2152', 0o13714, kind='data', line=1298)

#   SETLOC P40S3
#   BANK

#   COUNT 24/S40.1

W('30,3645', 0o04000, 'EP4(45)H', '2DEC', '.125', kind='data', line=1305)
W('30,3646', 0o00000, kind='data', line=1305)

W('30,3647', 0o00707, 'EP4(10)H', '2DEC', '.027777777', kind='data', line=1307)
W('30,3650', 0o03434, kind='data', line=1307)

W('30,3651', 0o45020, 'AGAIN', 'STQ', 'CALL', kind='interp', line=1309)
W('30,3652', 0o03730, '', '', 'QTEMP1', kind='operand', line=1310)
W('30,3653', 0o27071, '', '', 'THISPREC', kind='operand', line=1311)
W('30,3654', 0o66134, '', 'SXA,2', 'SXA,1', kind='interp', line=1312)
W('30,3655', 0o03746, '', '', 'RTX2', kind='operand', line=1313)
W('30,3656', 0o03745, '', '', 'RTX1', kind='operand', line=1314)
W('30,3657', 0o77775, '', 'VLOAD', kind='interp', line=1315)
W('30,3660', 0o00001, '', '', 'RATT', kind='operand', line=1316)
W('30,3661', 0o03632, '', 'STORE', 'RTIG', kind='interp', line=1317)
W('30,3662', 0o27570, '', 'STOVL', 'RINIT', kind='interp', line=1318)
W('30,3663', 0o00007, '', '', 'VATT', kind='operand', line=1319)
W('30,3664', 0o03640, '', 'STORE', 'VTIG', kind='interp', line=1320)
W('30,3665', 0o03576, '', 'STORE', 'VINIT', kind='interp', line=1321)
W('30,3666', 0o67201, '', 'SETPD', 'SLOAD', kind='interp', line=1322)
W('30,3667', 0o00001, '', '', '0', kind='operand', line=1323)
W('30,3670', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=1324)
W('30,3671', 0o43125, '', 'PDDL', 'BON', kind='interp', line=1325)
W('30,3672', 0o21646, '', '', 'EP4(45)H', kind='operand', line=1326)
W('30,3673', 0o03705, '', '', 'NORMSW', kind='operand', line=1327)
W('30,3674', 0o61677, '', '', '+3', kind='operand', line=1328)
W('30,3675', 0o77745, '', 'DLOAD', kind='interp', line=1329)
W('30,3676', 0o21650, '', '', 'EP4(10)H', kind='operand', line=1330)
W('30,3677', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=1331)
W('30,3700', 0o22000, '', '', 'INITVEL', kind='operand', line=1332)
W('30,3701', 0o52001, '', 'SETPD', 'GOTO', kind='interp', line=1333)
# Page 713
W('30,3702', 0o00001, '', '', '0', kind='operand', line=1335)
W('30,3703', 0o03730, '', '', 'QTEMP1', kind='operand', line=1336)
W('30,3704', 0o45175, 'CALCUT', 'VLOAD', 'CALL', kind='interp', line=1337)
W('30,3705', 0o03632, '', '', 'RTIG', kind='operand', line=1338)
W('30,3706', 0o77353, '', '', 'CALCGRAV', 'GDELTAT IN MPAC AT 2(+7) M/CS', kind='operand', line=1339)
W('30,3707', 0o70372, '', 'VSL1', 'V/SC', kind='interp', line=1340)
W('30,3710', 0o21747, '', '', '200CS', 'G AT 2(-5) M/CS. CS', kind='operand', line=1341)
W('30,3711', 0o52315, '', 'PDVL', 'VSU', kind='interp', line=1342)
W('30,3712', 0o03612, '', '', 'VIPRIME', kind='operand', line=1343)
W('30,3713', 0o03713, '', '', 'UT', kind='operand', line=1344)
W('30,3714', 0o52341, '', 'V/SC', 'VSU', kind='interp', line=1345)
W('30,3715', 0o21747, '', '', '200CS', kind='operand', line=1346)
W('30,3716', 0o72561, '', 'VXSC', 'VSL2', kind='interp', line=1347)
W('30,3717', 0o03703, '', '', 'CSTEER', kind='operand', line=1348)
W('30,3720', 0o24015, '', 'STOVL', '12D', 'B.C SCALED AT 2(-15) PDL 12D', kind='interp', line=1349)
W('30,3721', 0o03721, '', '', 'VGTIG', kind='operand', line=1350)
W('30,3722', 0o41456, '', 'UNIT', 'PUSH', 'UG PDL 0 SCALED AT 2(+1)', kind='interp', line=1351)

W('30,3723', 0o74241, '', 'DOT', 'VXSC', kind='interp', line=1353)
W('30,3724', 0o00015, '', '', '12D', kind='operand', line=1354)
W('30,3725', 0o00001, '', '', '0', kind='operand', line=1355)
W('30,3726', 0o51352, '', 'VSL2', 'BVSU', kind='interp', line=1356)
W('30,3727', 0o00015, '', '', '12D', kind='operand', line=1357)
W('30,3730', 0o14015, '', 'STODL', '12D', 'Q PDL SCALED AT 2(-5)', kind='interp', line=1358)
W('30,3731', 0o03727, '', '', 'F', kind='operand', line=1359)
W('30,3732', 0o56261, '', 'SRR', 'DDV', kind='interp', line=1360)
W('30,3733', 0o21605, '', '', '4', kind='operand', line=1361)
W('30,3734', 0o03076, '', '', 'WEIGHT/G', kind='operand', line=1362)
W('30,3735', 0o63316, '', 'DSQ', 'PDVL', 'F/MASS SQUARED PDL 6 AT 2(-10M/(CS.CS)', kind='interp', line=1363)
W('30,3736', 0o00015, '', '', '12D', kind='operand', line=1364)
W('30,3737', 0o77636, '', 'VSQ', kind='interp', line=1365)
W('30,3740', 0o75421, '', 'BDSU', 'SQRT', kind='interp', line=1366)
W('30,3741', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=1367)
W('30,3742', 0o53455, '', 'VAD', 'UNIT', kind='interp', line=1368)
W('30,3743', 0o00015, '', '', '12D', kind='operand', line=1369)
W('30,3744', 0o37713, '', 'STCALL', 'UT', kind='interp', line=1370)
W('30,3745', 0o03657, '', '', 'QTEMP', kind='operand', line=1371)
W('30,3746', 0o01440, '200CS', '2DEC', '200 B-12', kind='data', line=1372)
W('30,3747', 0o00000, kind='data', line=1372)

# Page 714
# PROGRAM DESCRIPTION S40.2,3           DATE 15 NOV 66
# MOD NO 2                              LOG SECTIONS P40-P47
# MOD BY ZELDIN
#
# FUNCTIONAL DESCRIPTION
#
# COMPUTE GIMBAL ANGLES IF THRUSTING OCCURRED WITH PRESENT IMU
# ORIENTATION, WINGS LEVEL SPACECRAFT, HEADS UP
# COMPUTE X AXIS OF ENGINE BELL
# COMPUTE PREFERRED IMU ORIENTATION (XSCREF)
# FOR THIS CALCULATION, ASSUME X AXIS OF SC ALONG UT INITIALLY,
# YSC=UNIT(XXR), ZSC=UNIT(XX(XXR)) AND ROTATE ENGINE BELL ALONG UT.
# NEW SC AXES WILL BE APPROX. WINGS LEVEL AND NEW SC AXES IN REF.
# COORDS. WILL BE PREFERRED IMU ORIENTATION.
# COMPUTE DESIRED THRUST DIRECTION IN SM COORDS.
#
# CALLING SEQUENCE
# L       CALL
# L+1             S40.2,3
#
# NORMAL EXIT MODE
# AT L+2 OF CALLING SEQUENCE (GOTO L+2)
#
# SUBROUTINES CALLED
# CALCGA
#
# ALARM OR ABORT MODES
# NONE
#
# ERASABLE INITIALIZATION REQUIRED
# PACTOFF         TOTAL PITCH TRIM ANGLE          SP AT 1.0795111 REV.
# YACTOFF         TOTAL YAW   TRIM ANGLE          SP AT 1.0795111 REV.
# UT              DESIRED THRUST DIRECTION        VECT. B2 M/(CS.CS)
# RTIG            POSITION AT TIME OF IGNITION    VECT. B29 M
# ENG2FLAG        ON=RCS  OFF=SPS
#
# OUTPUT
# SCAXIS          UNIT VECT. ALIGNED WITH ENG BELL IN SC COOR.    B1
# XSCREF          UNIT VECTORS ALIGNED WTH PREFERRED IMU          B1
# YSCREF
# ZSCREF
# GIMBAL ANGLES IN THETAD
# POINTVSM        UNIT VECT ALONG DESIRED THRUST DIRECTION IN SM  B1
#
# DEBRIS
# PUSHLIST, QPRET, MPAC
# QTEMP   TEMP. ERASABLE

#   BANK 24
#   SETLOC P40S
#   BANK
#   COUNT* $$/S40.2
W('24,3574', 0o64375, 'S40.2,3', 'VLOAD', 'MXV', kind='interp', line=1427)
W('24,3575', 0o03713, '', '', 'UT', kind='operand', line=1428)
W('24,3576', 0o01736, '', '', 'REFSMMAT', kind='operand', line=1429)
W('24,3577', 0o44172, '', 'VSL1', 'STQ', kind='interp', line=1430)
W('24,3600', 0o03657, '', '', 'QTEMP', kind='operand', line=1431)
W('24,3601', 0o03357, '', 'STORE', 'POINTVSM', 'THRUST IN SM AT 2', kind='interp', line=1432)
W('24,3602', 0o43001, '', 'SETPD', 'BON', kind='interp', line=1433)
W('24,3603', 0o00001, '', '', '0', kind='operand', line=1434)
# Page 715
W('24,3604', 0o00704, '', '', 'ENG2FLAG', kind='operand', line=1436)
W('24,3605', 0o51715, '', '', 'S40.2,3B', kind='operand', line=1437)
W('24,3606', 0o77745, '', 'DLOAD', kind='interp', line=1438)
W('24,3607', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=1439)
W('24,3610', 0o67206, '', 'PUSH', 'SLOAD', 'ZERO PDL 0', kind='interp', line=1440)
W('24,3611', 0o03025, '', '', 'YACTOFF', kind='operand', line=1441)
W('24,3612', 0o72405, '', 'DMP', 'SL1', kind='interp', line=1442)
W('24,3613', 0o11754, '', '', 'TRIMSCAL', kind='operand', line=1443)
W('24,3614', 0o41415, '', 'DAD', 'PUSH', kind='interp', line=1444)
W('24,3615', 0o11756, '', '', 'YBIAS', kind='operand', line=1445)
W('24,3616', 0o65346, '', 'COS', 'PDDL', 'COS(Y +Y0) PDL 2', kind='interp', line=1446)
W('24,3617', 0o41556, '', 'SIN', 'PUSH', 'SIN(Y +Y0) PDL 4', kind='interp', line=1447)
W('24,3620', 0o77735, '', 'SLOAD', kind='interp', line=1448)
W('24,3621', 0o03024, '', '', 'PACTOFF', kind='operand', line=1449)
W('24,3622', 0o72405, '', 'DMP', 'SL1', kind='interp', line=1450)
W('24,3623', 0o11754, '', '', 'TRIMSCAL', kind='operand', line=1451)
W('24,3624', 0o41415, '', 'DAD', 'PUSH', kind='interp', line=1452)
W('24,3625', 0o11760, '', '', 'PBIAS', kind='operand', line=1453)
W('24,3626', 0o65346, '', 'COS', 'PDDL', 'COS(P +P0) PDL 6', kind='interp', line=1454)
W('24,3627', 0o41556, '', 'SIN', 'PUSH', 'SIN(P +P0) PDL 8D', kind='interp', line=1455)
W('24,3630', 0o14323, '', 'STODL', 'ZSCREF', 'SIN(P +P0)', kind='interp', line=1456)
W('24,3631', 0o00007, '', '', '6', kind='operand', line=1457)
W('24,3632', 0o72405, '', 'DMP', 'SL1', kind='interp', line=1458)
W('24,3633', 0o00005, '', '', '4', kind='operand', line=1459)
W('24,3634', 0o65276, '', 'DCOMP', 'PDDL', '-SIN(Y+Y0)COS(P+P0) PDL 10', kind='interp', line=1460)
W('24,3635', 0o00007, '', '', '6', kind='operand', line=1461)
W('24,3636', 0o72405, '', 'DMP', 'SL1', kind='interp', line=1462)
W('24,3637', 0o00003, '', '', '2', kind='operand', line=1463)
W('24,3640', 0o77666, '', 'VDEF', kind='interp', line=1464)

W('24,3641', 0o14307, '', 'STODL', 'XSCREF', 'PD POINTER AT 6 NEW SC X AXIS SCALED AT', kind='interp', line=1466)
W('24,3642', 0o00323, '', '', 'ZSCREF', kind='operand', line=1467)
W('24,3643', 0o72405, '', 'DMP', 'SL1', kind='interp', line=1468)
W('24,3644', 0o00005, '', '', '4', kind='operand', line=1469)
W('24,3645', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=1470)
W('24,3646', 0o00323, '', '', 'ZSCREF', kind='operand', line=1471)
W('24,3647', 0o00003, '', '', '2', kind='operand', line=1472)
W('24,3650', 0o57552, '', 'SL1', 'DCOMP', kind='interp', line=1473)
W('24,3651', 0o77666, '', 'VDEF', kind='interp', line=1474)

W('24,3652', 0o14323, '', 'STODL', 'ZSCREF', 'PD POINTER AT 4 NEW SC Z AXIS SCALED AT 2', kind='interp', line=1476)
W('24,3653', 0o77666, '', 'VDEF', kind='interp', line=1477)

W('24,3654', 0o14315, '', 'STODL', 'YSCREF', 'PD POINTER AT 0 NEW SC Y AXIS SCALED AT 2', kind='interp', line=1479)
W('24,3655', 0o00323, '', '', 'ZSCREF', kind='operand', line=1480)
W('24,3656', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=1481)
W('24,3657', 0o00315, '', '', 'YSCREF', kind='operand', line=1482)
W('24,3660', 0o00307, '', '', 'XSCREF', kind='operand', line=1483)
W('24,3661', 0o77666, '', 'VDEF', kind='interp', line=1484)
# Page 716
W('24,3662', 0o27351, '', 'STOVL', 'SCAXIS', 'ENGINE BELL SCALED AT 2', kind='interp', line=1486)
W('24,3663', 0o03713, '', '', 'UT', kind='operand', line=1487)
W('24,3664', 0o53515, '', 'PDVL', 'UNIT', kind='interp', line=1488)
W('24,3665', 0o03632, '', '', 'RTIG', kind='operand', line=1489)
W('24,3666', 0o57435, '', 'VXV', 'VCOMP', kind='interp', line=1490)
W('24,3667', 0o00001, '', '', '0', kind='operand', line=1491)
W('24,3670', 0o41456, '', 'UNIT', 'PUSH', kind='interp', line=1492)
W('24,3671', 0o77624, '', 'CALL', kind='interp', line=1493)
W('24,3672', 0o51734, '', '', 'TSTRXUT', kind='operand', line=1494)
W('24,3673', 0o57435, '', 'VXV', 'VCOMP', kind='interp', line=1495)
W('24,3674', 0o00001, '', '', '0', kind='operand', line=1496)
W('24,3675', 0o63372, '', 'VSL1', 'PDVL', '2 RF/SC IN PDL 12D', kind='interp', line=1497)
W('24,3676', 0o00307, '', '', 'XSCREF', kind='operand', line=1498)
W('24,3677', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=1499)
W('24,3700', 0o00001, '', '', '0', kind='operand', line=1500)
W('24,3701', 0o24307, '', 'STOVL', 'XSCREF', 'X OF PREF. IMU,X OF SC IN REF COOR. AT 2', kind='interp', line=1501)
W('24,3702', 0o00315, '', '', 'YSCREF', kind='operand', line=1502)
W('24,3703', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=1503)
W('24,3704', 0o00001, '', '', '0', kind='operand', line=1504)
W('24,3705', 0o24315, '', 'STOVL', 'YSCREF', 'Y OF PREF. IMU,Y OF SC IN REF COOR. AT 2', kind='interp', line=1505)
W('24,3706', 0o00323, '', '', 'ZSCREF', kind='operand', line=1506)
W('24,3707', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=1507)
W('24,3710', 0o00001, '', '', '0', kind='operand', line=1508)
W('24,3711', 0o00323, '', 'STORE', 'ZSCREF', 'Z OF PREF. IMU,Z OF SC IN REF COOR. AT 2', kind='interp', line=1509)
W('24,3712', 0o52001, '', 'SETPD', 'GOTO', kind='interp', line=1510)
W('24,3713', 0o00001, '', '', '0', kind='operand', line=1511)
W('24,3714', 0o03657, '', '', 'QTEMP', kind='operand', line=1512)
W('24,3715', 0o77775, 'S40.2,3B', 'VLOAD', kind='interp', line=1513)
W('24,3716', 0o15333, '', '', 'UNITX', kind='operand', line=1514)
W('24,3717', 0o27351, '', 'STOVL', 'SCAXIS', kind='interp', line=1515)
W('24,3720', 0o03713, '', '', 'UT', kind='operand', line=1516)
W('24,3721', 0o00307, '', 'STORE', 'XSCREF', kind='interp', line=1517)
W('24,3722', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1518)
W('24,3723', 0o03632, '', '', 'RTIG', kind='operand', line=1519)
W('24,3724', 0o34007, '', 'STCALL', '6D', kind='interp', line=1520)
W('24,3725', 0o51734, '', '', 'TSTRXUT', kind='operand', line=1521)
W('24,3726', 0o00315, '', 'STORE', 'YSCREF', kind='interp', line=1522)
W('24,3727', 0o57435, '', 'VXV', 'VCOMP', kind='interp', line=1523)
W('24,3730', 0o00307, '', '', 'XSCREF', kind='operand', line=1524)
W('24,3731', 0o77772, '', 'VSL1', kind='interp', line=1525)
W('24,3732', 0o34323, '', 'STCALL', 'ZSCREF', 'ZNB AXIS IN REF COOR', kind='interp', line=1526)
W('24,3733', 0o03657, '', '', 'QTEMP', kind='operand', line=1527)
W('24,3734', 0o46145, 'TSTRXUT', 'DLOAD', 'BHIZ', kind='interp', line=1528)
W('24,3735', 0o00045, '', '', '36D', kind='operand', line=1529)
W('24,3736', 0o51741, '', '', 'BADVCTOR', kind='operand', line=1530)
W('24,3737', 0o43575, '', 'VLOAD', 'RVQ', kind='interp', line=1531)
W('24,3740', 0o00007, '', '', '6D', kind='operand', line=1532)
W('24,3741', 0o53575, 'BADVCTOR', 'VLOAD', 'UNIT', kind='interp', line=1533)
W('24,3742', 0o03632, '', '', 'RTIG', kind='operand', line=1534)
W('24,3743', 0o53515, '', 'PDVL', 'UNIT', kind='interp', line=1535)
# Page 717
W('24,3744', 0o03640, '', '', 'VTIG', kind='operand', line=1537)
W('24,3745', 0o53322, '', 'VSR3', 'VAD', kind='interp', line=1538)
W('24,3746', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1539)
W('24,3747', 0o03713, '', '', 'UT', kind='operand', line=1540)
W('24,3750', 0o77676, '', 'VCOMP', kind='interp', line=1541)
W('24,3751', 0o00007, '', 'STORE', '6D', kind='interp', line=1542)
W('24,3752', 0o77616, '', 'RVQ', kind='interp', line=1543)
W('24,3753', 0o21215, 'TRIMSCAL', '2DEC', '1.07975111 B-1', kind='data', line=1544)
W('24,3754', 0o12215, kind='data', line=1544)

W('24,3755', 0o00053, 'YBIAS', '2DEC', '+.00263888889', 'YAW   MECH BIAS (+0.95 DEG, THRUST ON)', kind='data', line=1546)
W('24,3756', 0o07423, kind='data', line=1546)

W('24,3757', 0o77636, 'PBIAS', '2DEC', '-.00597222222', 'PITCH MECH BIAS (-2.15 DEG, THRUST ON)', kind='data', line=1548)
W('24,3760', 0o44653, kind='data', line=1548)

# REFERENCE, TRW 68.6520.3.3-40 27 FEB, 1968

# PROGRAM DESCRIPTION S41.1             DATE 8 DEC 66
# MOD NO 1                              LOG SECTION P40-P47
# MOD BY ZELDIN
#
# FUNCTIONAL DESCRIPTION
#
# COMPUTE VELOCITY TO BE GAINED INITIALLY IN REF COORDS.
# TO CONTROL COORDS.
#
# CALLING SEQUENCE
#
# L       CALL
# L+1             S41.1
#
# NORMAL EXIT MODE
#
# AT L +2 OF CALLING SEQUENCE
#
# SUBROUTINES CALLED:
#
# CALCSMSC
# CDUTRIG
#
# ALARM OR ABORT MODES
#
# NONE
#
# ERASABLE INITIALIZATION REQUIRED
#
# VG IN REF. COORD. PDL L POINTER AT L+5.  S41.1 WILL RETURN WITH
# POINTER AT L (L MUST BE LESS THAN OR = TO 14D)
#
# OUTPUT
#
# MPAC CONTAINS VG IN CONTROL COORDS              VECT. B7 M/CS
#
# DEBRIS:
#
# QTEMP           TEMP ERASABLE
# QPRET

#   COUNT 22/S41.1

#   SETLOC P40S5
#   BANK

W('22,3431', 0o45020, 'S41.1', 'STQ', 'CALL', kind='interp', line=1598)
W('22,3432', 0o03657, '', '', 'QTEMP', kind='operand', line=1599)
W('22,3433', 0o47477, '', '', 'CDUTRIG', kind='operand', line=1600)
W('22,3434', 0o77775, '', 'VLOAD', kind='interp', line=1601)
W('22,3435', 0o45121, '', 'MXV', 'CALL', kind='interp', line=1602)
W('22,3436', 0o01736, '', '', 'REFSMMAT', kind='operand', line=1603)
W('22,3437', 0o47644, '', '', '*SMNB*', kind='operand', line=1604)
# Page 718
W('22,3440', 0o74321, '', 'MXV', 'VXSC', kind='interp', line=1606)
W('22,3441', 0o05003, '', '', 'QUADROT', kind='operand', line=1607)
W('22,3442', 0o05446, '', '', 'TENBNK14', 'VG IN CONTROL COORD IN MPAC SCALED AT', kind='operand', line=1608)
W('22,3443', 0o52072, '', 'VSL5', 'GOTO', 'VG IN CONTROL COORDS. IN MPAC AT 2(+7)', kind='interp', line=1609)
W('22,3444', 0o03657, '', '', 'QTEMP', kind='operand', line=1610)
W('22,3445', 0o24000, 'TENBNK14', '2DEC', '10. B-4', kind='data', line=1611)
W('22,3446', 0o00000, kind='data', line=1611)

# Page 719
# NAME          S40.8 -- CROSS PRODUCT STEERING
# FUNCTION      (1) UPDATES THE VELOCITY-TO-BE-GAINED VECTOR.
# (2) GENERATES ANGULAR RATE STEERING COMMANDS FOR AUTOPILOT.
# (3) ESTABLISHES ENGINE CUT-OFF SIGNALS AT APPROPRIATE TIMES.
# (4) INITIATES THRUST-FAIL ROUTINE, R40
# CALLING SEQ   CALL S40.6
# INPUT         VGPREV          LAST VALUE OF THE VELOCITY-TO-BE-GAINED VECTOR
# PRIOR TO UPDATING IN METERS/CS AT +7.
# DELVREF         CHANGE IN VEHICLE VELOCITY SINCE LAST MEASUREMENT
# IN METERS/CS AT +7.
# BDT             EFFECT OF RATE OF CHANGE OF REQUIRED VELOCITY AND
# GRAVITY DURING DT UPON VELOCITY-TO-BE-GAINED IN
# METERS/CS AT +7.
# CSTEER          A SCALAR OF THE STEERING LAW, SC.AT B+1, USED FOR
# SPS AIMPOINT STEERING MANEUVERS.
# IDLEFAIL        A FLAG TO INHIBIT (IDLE) THE THRUST-FAIL ROUTINE.
# STEERSW         A SWITCH TO PRECLUDE NEEDLESS CONDUCT OF STEERING.
# REFSMMAT, DAPDATR1, PIPTIME
# EREPFRAC, ETDECAY, KPRIMEDT FOR TVC.
# OUTPUT        TTOGO           TIME REMAINING FOR ENGINE BURN IN CS AT +28.
# OMEGAC          DP VECTOR RATE COMMAND, SC.AT 1/(2TVCDT) REVS/SEC.
# VG, VGPREV, VGDISP, TGO, TIG, SCALED AS NOTED IN CODING
# STEERSW, IMPULSW, NVWORD1
# REPFRAC, CNTR, VCNTR, VCNTRTMP FOR TVC (R40 INTERFACING)
# DEBRIS        OMEGAXC, +1
# SUBROUTINES USED:  *SMNB*, ALARM

#   SETLOC P40S1
#   BANK
#   EBANK= DAPDATR1
#   COUNT 16/S40.8

W('16,2153', 0o44001, 'S40.8', 'SETPD', 'STQ', kind='interp', line=1646)
W('16,2154', 0o00001, 'SPBIT1', '', '00D', kind='operand', line=1647)
W('16,2155', 0o03657, '', '', 'QTEMP', kind='operand', line=1648)
W('16,2156', 0o51375, '', 'VLOAD', 'BVSU', 'CONSTRUCT DELVG, SC.AT B+7 M/CS', kind='interp', line=1649)
W('16,2157', 0o03433, '', '', 'DELVREF', kind='operand', line=1650)
W('16,2160', 0o03705, '', '', 'BDT', kind='operand', line=1651)
W('16,2161', 0o77655, '', 'VAD', kind='interp', line=1652)
W('16,2162', 0o03721, '', '', 'VGPREV', kind='operand', line=1653)
W('16,2163', 0o03460, '', 'STORE', 'VG', 'VELOCITY-TO-BE-GAINED, SC.AT B+7 M/CS', kind='interp', line=1654)

W('16,2164', 0o77646, '', 'ABVAL', kind='interp', line=1656)
W('16,2165', 0o03773, '', 'STORE', 'VGDISP', 'FOR DISPLAY PURPOSES', kind='interp', line=1657)
W('16,2166', 0o77776, '', 'EXIT', kind='interp', line=1658)
W('16,2167', 0o05412, '', 'TC', 'PHASCHNG', line=1659)
W('16,2170', 0o10035, '', 'OCT', '10035', 'TYPE B RESTART RESTART BELOW AND 5.3 REREADAC', kind='data', line=1660)

W('16,2171', 0o06006, '', 'TC', 'INTPRET', line=1662)
W('16,2172', 0o77775, '', 'VLOAD', kind='interp', line=1663)
# Page 720
W('16,2173', 0o03460, '', '', 'VG', kind='operand', line=1665)
W('16,2174', 0o03721, '', 'STORE', 'VGPREV', kind='interp', line=1666)
W('16,2175', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=1667)
W('16,2176', 0o01344, '', '', 'STEERSW', 'SKIP TGO AND CROSS-PRODUCT', kind='operand', line=1668)
W('16,2177', 0o03657, '', '', 'QTEMP', kind='operand', line=1669)
W('16,2200', 0o03433, '', '', 'DELVREF', kind='operand', line=1670)
W('16,2201', 0o41446, '', 'ABVAL', 'PUSH', 'CHECK FOR LOTHRUST', kind='interp', line=1671)
W('16,2202', 0o41335, '', 'SLOAD', 'DMP', kind='interp', line=1672)
W('16,2203', 0o01354, '', '', 'DVTHRESH', 'SC.AT B-2 M/CS', kind='operand', line=1673)
W('16,2204', 0o36011, '', '', 'DPB-9', kind='operand', line=1674)
W('16,2205', 0o77621, '', 'BDSU', kind='interp', line=1675)
W('16,2206', 0o77440, '', 'BMN', 'EXIT', kind='interp', line=1676)
W('16,2207', 0o40222, '', '', 'LOTHRUST', kind='operand', line=1677)
W('16,2210', 0o31466, '', 'CAE', 'DAPDATR1', 'ENABLE TVCDAP CG TRACKING', line=1678)
W('16,2211', 0o75002, '', 'MASK', 'BIT14', line=1679)
W('16,2212', 0o10000, '', 'CCS', 'A', line=1680)
W('16,2213', 0o35017, '', 'CAF', 'BIT1', line=1681)
W('16,2214', 0o50000, '', 'INDEX', 'A', 'LM-OFF, LM-ON VALUE', line=1682)
W('16,2215', 0o31421, '', 'CAE', 'EREPFRAC', line=1683)
W('16,2216', 0o55642, '', 'TS', 'REPFRAC', line=1684)

W('16,2217', 0o06006, '', 'TC', 'INTPRET', line=1686)
W('16,2220', 0o51375, 'TGOCALC', 'VLOAD', 'BVSU', 'GET DELVG', kind='interp', line=1687)
W('16,2221', 0o03433, '', '', 'DELVREF', kind='operand', line=1688)
W('16,2222', 0o03705, '', '', 'BDT', kind='operand', line=1689)
W('16,2223', 0o77656, '', 'UNIT', kind='interp', line=1690)
W('16,2224', 0o41441, '', 'DOT', 'PUSH', '(00D)', kind='interp', line=1691)
W('16,2225', 0o03460, '', '', 'VG', kind='operand', line=1692)
W('16,2226', 0o56244, '', 'BPL', 'DDV', 'ANGLE SHOULD BE GREATER THAN PI/2', kind='interp', line=1693)
W('16,2227', 0o40214, '', '', 'INCRSVG', '      DISPLAY ALARM IF NOT', kind='operand', line=1694)
W('16,2230', 0o36005, '', '', '2VEXHUST', kind='operand', line=1695)
W('16,2231', 0o41215, '', 'DAD', 'DMP', '(DOT PRODUCT UP FROM 00D)', kind='interp', line=1696)
W('16,2232', 0o11564, '', '', 'LODPHALF', kind='operand', line=1697)
W('16,2233', 0o70501, '', 'NORM', 'SR1', kind='interp', line=1698)
W('16,2234', 0o00047, '', '', 'X1', kind='operand', line=1699)
W('16,2235', 0o60325, '', 'PDDL', 'NORM', kind='interp', line=1700)
W('16,2236', 0o00045, '', '', '36D', '(MAG DELVG)', kind='operand', line=1701)
W('16,2237', 0o00050, '', '', 'X2', kind='operand', line=1702)
W('16,2240', 0o77665, '', 'BDDV', kind='interp', line=1703)
W('16,2241', 0o53664, '', 'XSU,2', 'SL*', kind='interp', line=1704)
W('16,2242', 0o00046, '', '', 'X1', kind='operand', line=1705)
W('16,2243', 0o57607, '', '', '0 -9D,2', kind='operand', line=1706)
W('16,2244', 0o41405, '', 'DMP', 'PUSH', '(00D)', kind='interp', line=1707)
W('16,2245', 0o36003, '', '', '-FOURDT', kind='operand', line=1708)
W('16,2246', 0o54335, '', 'SLOAD', 'SR', kind='interp', line=1709)
W('16,2247', 0o03013, '', '', 'ETDECAY', 'ETDECAY SC.AT B+14 CS', kind='operand', line=1710)
W('16,2250', 0o20617, '', '', '14D', kind='operand', line=1711)
W('16,2251', 0o45421, '', 'BDSU', 'STADR', kind='interp', line=1712)
W('16,2252', 0o74347, '', 'STORE', 'TGO', 'TIME TO GO IN CS. AT +28', kind='interp', line=1713)
W('16,2253', 0o77615, '', 'DAD', kind='interp', line=1714)
# Page 721
W('16,2254', 0o01205, '', '', 'PIPTIME', kind='operand', line=1716)
W('16,2255', 0o17413, '', 'STODL', 'TIG', kind='interp', line=1717)
W('16,2256', 0o03430, '', '', 'TGO', kind='operand', line=1718)
W('16,2257', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1719)
W('16,2260', 0o36007, '', '', 'FOURSEC', kind='operand', line=1720)
W('16,2261', 0o40201, '', '', 'S40.81', kind='operand', line=1721)

W('16,2262', 0o74375, 'XPRODUCT', 'VLOAD', 'VXSC', kind='interp', line=1723)
W('16,2263', 0o03705, '', '', 'BDT', kind='operand', line=1724)
W('16,2264', 0o03703, '', '', 'CSTEER', kind='operand', line=1725)
W('16,2265', 0o52352, '', 'VSL2', 'VSU', kind='interp', line=1726)
W('16,2266', 0o03433, '', '', 'DELVREF', kind='operand', line=1727)
W('16,2267', 0o63256, '', 'UNIT', 'PDVL', kind='interp', line=1728)
W('16,2270', 0o03460, '', '', 'VG', kind='operand', line=1729)
W('16,2271', 0o47256, '', 'UNIT', 'VXV', kind='interp', line=1730)
W('16,2272', 0o45121, '', 'MXV', 'CALL', kind='interp', line=1731)
W('16,2273', 0o01736, '', '', 'REFSMMAT', '(REFSMMAT/2)', kind='operand', line=1732)
W('16,2274', 0o47644, '', '', '*SMNB*', kind='operand', line=1733)
W('16,2275', 0o77761, '', 'VXSC', kind='interp', line=1734)
W('16,2276', 0o03235, '', '', 'KPRIMEDT', '(KPRIMEDT SCIAT PI/8 RAD)', kind='operand', line=1735)
W('16,2277', 0o03126, 'OMEGACLC', 'STORE', 'OMEGAC', kind='interp', line=1736)
W('16,2300', 0o77650, '', 'GOTO', kind='interp', line=1737)
W('16,2301', 0o03657, '', '', 'QTEMP', kind='operand', line=1738)

#   SETLOC DAPS7
#   BANK
#   COUNT 17/S40.8

W('17,2000', 0o00000, 'TWODT', '2DEC', '200.0 B-28', '2 SEC', kind='data', line=1744)
W('17,2001', 0o00310, kind='data', line=1744)

W('17,2002', 0o77715, '-FOURDT', '2DEC', '-800 B-18', '-4(200CS), SC.AT B+18CS (-4 FOR SCALING)', kind='data', line=1746)
W('17,2003', 0o77777, kind='data', line=1746)

W('17,2004', 0o17602, '2VEXHUST', '2DEC', '63.020792 B-7', '2(10338.0564 FPS), SC.AT B+7 M/CS', kind='data', line=1748)
W('17,2005', 0o25124, kind='data', line=1748)

W('17,2006', 0o00000, 'FOURSEC', '2DEC', '400.0 B-28', '4 SEC', kind='data', line=1750)
W('17,2007', 0o00620, kind='data', line=1750)

W('17,2010', 0o00040, 'DPB-9', '2DEC', '1 B-9', kind='data', line=1752)
W('17,2011', 0o00000, kind='data', line=1752)

#   SETLOC DAPS6
#   BANK

#   COUNT 20/S40.8

W('20,2201', 0o77214, 'S40.81', 'SET', 'VLOAD', 'TGO LESS THAN 4 SECONDS', kind='interp', line=1759)
W('20,2202', 0o01066, '', '', 'IMPULSW', 'FOR ENGINE-OFF CALL', kind='operand', line=1760)
W('20,2203', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=1761)
W('20,2204', 0o03126, 'RATEZRO', 'STORE', 'OMEGAC', 'TVC TO ATTITUDE HOLD', kind='interp', line=1762)
W('20,2205', 0o77776, '', 'EXIT', kind='interp', line=1763)
W('20,2206', 0o34777, '', 'CAF', 'POSMAX', 'INHIBIT SWITCHOVER/TVC EG TRACKING', line=1764)
W('20,2207', 0o55447, '', 'TS', 'CNTR', line=1765)
# Page 722
W('20,2210', 0o06006, '', 'TC', 'INTPRET', line=1767)
W('20,2211', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=1768)
W('20,2212', 0o01264, '', '', 'STEERSW', 'RESTARTS OK', kind='operand', line=1769)
W('20,2213', 0o03657, '', '', 'QTEMP', kind='operand', line=1770)
W('20,2214', 0o77776, 'INCRSVG', 'EXIT', '', 'ALARM INDICATING THAT THRUST IS POINTING', kind='interp', line=1771)
W('20,2215', 0o05650, '', 'TC', 'ALARM', 'IN WRONG DIRECTION.', line=1772)
W('20,2216', 0o01407, '', 'OCT', '01407', kind='data', line=1773)
W('20,2217', 0o06006, '', 'TC', 'INTPRET', line=1774)
W('20,2220', 0o77650, '', 'GOTO', kind='interp', line=1775)
W('20,2221', 0o03657, '', '', 'QTEMP', kind='operand', line=1776)

W('20,2222', 0o77214, 'LOTHRUST', 'BON', 'VLOAD', 'THRUST FAILURE (LO-OR-NO) INDICATED', kind='interp', line=1778)
W('20,2223', 0o00711, '', '', 'IDLEFAIL', 'SET BY V97P.  ALLOWS 1 BYPASS IN CASE OF', kind='operand', line=1779)
W('20,2224', 0o03657, '', '', 'QTEMP', '      UNFAVORABLE S40.8 SYNCH.', kind='operand', line=1780)
W('20,2225', 0o15335, '', '', 'HI6ZEROS', 'START OF ENGINE-FAIL (R40) OPERATIONS', kind='operand', line=1781)
W('20,2226', 0o03126, '', 'STORE', 'OMEGAC', 'PUT TVC IN ATTITUDE HOLD', kind='interp', line=1782)
W('20,2227', 0o77776, '', 'EXIT', kind='interp', line=1783)

W('20,2230', 0o45021, '', 'CS', 'ZERO', line=1785)
W('20,2231', 0o55643, '', 'TS', 'VCNTR', 'KILL CSMMASS UPDATING', line=1786)
W('20,2232', 0o55653, '', 'TS', 'VCNTRTMP', '(TVCEXEC LOGIC REQUIRES THIS TOO)', line=1787)
W('20,2233', 0o55642, '', 'TS', 'REPFRAC', 'KILL TVCDAP CG TRIM TRACKING', line=1788)
W('20,2234', 0o55145, '', 'TS', 'NVWORD1', 'SET UP ENGINE-FAIL V97FLASH (CLOCKJOB)', line=1789)

W('20,2235', 0o06006, '', 'TC', 'INTPRET', line=1791)
W('20,2236', 0o52014, '', 'CLEAR', 'GOTO', 'INHIBIT STEERING AND TGO CALC (MANUAL', kind='interp', line=1792)
W('20,2237', 0o01264, '', '', 'STEERSW', '      SHUTDOWN IF NOT SET UP AGAIN)', kind='operand', line=1793)
W('20,2240', 0o03657, '', '', 'QTEMP', 'RESTARTS OK', kind='operand', line=1794)

# Page 723
# NAME          S40.9 -- VTOGAIN (AIMPOINT MANEUVERS ONLY)
# FUNCTION      (1) GENERATES REQUIRED VELOCITY AND VELOCITY-TO-BE-GAINED
# VECTORS FOR USE DURING AIMPOINT MANEUVERS.
# (2) UPDATES THE B VECTOR WHICH IS USED IN THE FINAL
# CALCULATION OF EXTRAPOLATING THE VELOCITY-TO-BE-GAINED.
# CALLING SEQ   VIA FINDVEC AS NEW JOB.
# INPUT         RNIT    ACTIVE VEHICLE RADIUS VECTOR IN METERS AT +29.
# VNIT    ACTIVE VEHICLE VELOCITY VECTOR IN METERS/CS AT +7.
# VRPREV  LAST COMPUTED VELOCITY REQUIRED VECTOR IN
# METERS/CS AT +7.
# NONTIG  TIME OF IGN.  USED IN TARGETTING ROUTINES B+28
# DELLT4  TRANSFER TIME FROM PIPTIME TO TARGET B+28
# TNIT    TIME OF RNIT AND VNIT IN CS AT +28
# GDT/2   HALF OF VELOCITY GAINED IN DELTA T TIME DUE TO
# ACCELERATION OF GRAVITY IN METERS/CS AT +7.
# DELVREF CHANGE IN VELOCITY DURING LAST 2 SEC IN
# METERS/CS AT +7.
# NORMSW  SET=CENTRAL ANGLE BETWEEN RTARG AND RTIG IS BETWEEN
# 165 TO 195 DEGREES.
# RESET=CENTRAL ANGLE OUTSIDE CONE DESCRIBED ABOVE.
# OUTPUT        VGTEMP  VELOCITY TO BE GAINED VECTOR IN METERS/CS AT +7.
# COGA    INPUT OF INITIAL GUESS FOR LAMBERT FROM S40.1
# OR PREVIOUS PASS THRU S40.9.
# GOBL/2  OBLATENESS TERM IN AVG GRAV CALC: GOBL*RSQ/MU
# VRPREV/ VELOCITY REQUIRED VECTOR IN METERS/CS AT +7.
# BDT     B VECTOR IN METERS/CS AT +7.
# SUBROUTINES USED -- INITVEL

#   SETLOC P40S1
#   BANK

#   EBANK= NBRCYCLS
#   COUNT 16/S40.9

W('16,2302', 0o06006, 'S40.9', 'TC', 'INTPRET', line=1831)
W('16,2303', 0o71201, '', 'SETPD', 'DLOAD', kind='interp', line=1832)
W('16,2304', 0o00001, '', '', '00D', kind='operand', line=1833)
W('16,2305', 0o11566, '', '', 'LO6ZEROS', kind='operand', line=1834)
W('16,2306', 0o77725, '', 'PDDL', kind='interp', line=1835)
W('16,2307', 0o34424, '', '', 'EP4(45)L', kind='operand', line=1836)
W('16,2310', 0o71214, '', 'BON', 'DLOAD', kind='interp', line=1837)
W('16,2311', 0o03705, '', '', 'NORMSW', kind='operand', line=1838)
W('16,2312', 0o34314, '', '', '+2', kind='operand', line=1839)
W('16,2313', 0o34426, '', '', 'EP4(10)L', kind='operand', line=1840)
W('16,2314', 0o77606, '', 'PUSH', kind='interp', line=1841)
W('16,2315', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=1842)
W('16,2316', 0o00675, '', '', 'GUESSW', kind='operand', line=1843)
W('16,2317', 0o22002, '', '', 'HAVEGUES', kind='operand', line=1844)
W('16,2320', 0o77776, '', 'EXIT', kind='interp', line=1845)
W('16,2321', 0o05412, '', 'TC', 'PHASCHNG', 'SAVE TIME BY NOT REDOING LAMBERT CALCS', line=1846)
W('16,2322', 0o05021, '', 'OCT', '05021', 'C, PRIORITY NEXT, JOB BELOW', kind='data', line=1847)
# Page 724
W('16,2323', 0o10000, '', 'OCT', '10000', kind='data', line=1849)
W('16,2324', 0o06006, '', 'TC', 'INTPRET', line=1850)
W('16,2325', 0o77614, 'ENDLAMB', 'BON', kind='interp', line=1851)
W('16,2326', 0o01310, '', '', 'FIRSTFLG', kind='operand', line=1852)
W('16,2327', 0o34345, '', '', 'FIRSTTME', kind='operand', line=1853)
W('16,2330', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=1854)
W('16,2331', 0o03612, '', '', 'VIPRIME', kind='operand', line=1855)
W('16,2332', 0o03466, '', '', 'VRPREV', kind='operand', line=1856)
W('16,2333', 0o45325, '', 'PDDL', 'DSU', kind='interp', line=1857)
W('16,2334', 0o03474, '', '', 'TNIT', kind='operand', line=1858)
W('16,2335', 0o03476, '', '', 'TNITPREV', kind='operand', line=1859)
W('16,2336', 0o55261, '', 'SL', 'BDDV', kind='interp', line=1860)
W('16,2337', 0o20222, '', '', '17D', kind='operand', line=1861)
W('16,2340', 0o34420, '', '', '200CSHI', kind='operand', line=1862)
W('16,2341', 0o77761, '', 'VXSC', kind='interp', line=1863)
W('16,2342', 0o76451, '', 'VSU', 'VSL1', kind='interp', line=1864)
W('16,2343', 0o01207, '', '', 'GDT/2', kind='operand', line=1865)
W('16,2344', 0o03705, '', 'STORE', 'BDT', kind='interp', line=1866)
W('16,2345', 0o57535, 'FIRSTTME', 'SLOAD', 'DCOMP', kind='interp', line=1867)
W('16,2346', 0o03747, '', '', 'RTX2', kind='operand', line=1868)
W('16,2347', 0o77640, '', 'BMN', kind='interp', line=1869)
W('16,2350', 0o34365, '', '', 'MOONCASE', kind='operand', line=1870)
W('16,2351', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=1871)
W('16,2352', 0o01171, '', '', 'RN', kind='operand', line=1872)
W('16,2353', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=1873)
W('16,2354', 0o01205, '', '', 'PIPTIME', kind='operand', line=1874)
W('16,2355', 0o03450, '', '', 'NOMTIG', kind='operand', line=1875)
W('16,2356', 0o56205, '', 'DMP', 'DDV', kind='interp', line=1876)
W('16,2357', 0o34422, '', '', 'EARTHMU', kind='operand', line=1877)
W('16,2360', 0o00043, '', '', '34D', kind='operand', line=1878)
W('16,2361', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=1879)
W('16,2362', 0o01215, '', '', 'GOBL/2', kind='operand', line=1880)
W('16,2363', 0o03646, '', '', 'VGTEMP', 'NOTE: NO TEST IS MADE TO SUBTRACT GOBL', kind='operand', line=1881)
W('16,2364', 0o03646, '', 'STORE', 'VGTEMP', 'INSIDE 165-195 DEGREE CONE AREA.', kind='interp', line=1882)
W('16,2365', 0o77776, 'MOONCASE', 'EXIT', kind='interp', line=1883)
W('16,2366', 0o05412, '', 'TC', 'PHASCHNG', line=1884)
W('16,2367', 0o04021, '', 'OCT', '04021', 'C, JOB BELOW', kind='data', line=1885)

W('16,2370', 0o06006, 'COPY40.9', 'TC', 'INTPRET', line=1887)
W('16,2371', 0o77745, '', 'DLOAD', kind='interp', line=1888)
W('16,2372', 0o03474, '', '', 'TNIT', kind='operand', line=1889)
W('16,2373', 0o27476, '', 'STOVL', 'TNITPREV', kind='interp', line=1890)
W('16,2374', 0o03612, '', '', 'VIPRIME', kind='operand', line=1891)
W('16,2375', 0o03466, '', 'STORE', 'VRPREV', kind='interp', line=1892)
W('16,2376', 0o77414, '', 'CLEAR', 'EXIT', kind='interp', line=1893)
W('16,2377', 0o01270, '', '', 'FIRSTFLG', kind='operand', line=1894)
W('16,2400', 0o45017, '', 'CS', 'ONE', 'REDO40.9 (RESTART) ENTRY TO END S40.9', line=1895)
W('16,2401', 0o55742, '', 'TS', 'NBRCYCLS', line=1896)
W('16,2402', 0o05412, 'ENDS40.9', 'TC', 'PHASCHNG', line=1897)
W('16,2403', 0o00001, '', 'OCT', '00001', kind='data', line=1898)
# Page 725
W('16,2404', 0o15217, '', 'TCF', 'ENDOFJOB', line=1900)

W('16,2405', 0o06006, 'REDO40.9', 'TC', 'INTPRET', 'S40.9 RESTARTS COME HERE TO GRACEFULLY', line=1902)
W('16,2406', 0o77775, '', 'VLOAD', '', '      TERMINATE S40.9 SO THAT IT CAN BE', kind='interp', line=1903)
W('16,2407', 0o11566, '', '', 'LO6ZEROS', '      SET UP WITH LATEST R,V,T NEXT PASS', kind='operand', line=1904)
W('16,2410', 0o17345, '', 'STODL', 'DELVSUM', "      (TYPE C PHASE POINTS '04021' WILL", kind='interp', line=1905)
W('16,2411', 0o11566, '', '', 'LO6ZEROS', '      FORCE NORMAL S40.9 TERMINATIONS,', kind='operand', line=1906)
W('16,2412', 0o27343, '', 'STOVL', 'NBRCYCLS', '      RATHER THAN LOSE TIME OF BRAND NEW', kind='interp', line=1907)
W('16,2413', 0o03721, '', '', 'VGPREV', '      PASS -- QUICK OLD DATA BETTER THAN', kind='operand', line=1908)
W('16,2414', 0o03646, '', 'STORE', 'VGTEMP', '      NONE) NOW CAN GO THRU SETUP.9', kind='interp', line=1909)
W('16,2415', 0o77776, '', 'EXIT', '', '      WITHOUT DISTURBING VGPREV.', kind='interp', line=1910)
W('16,2416', 0o12400, '', 'TCF', 'ENDS40.9 -2', 'STORE 0,0 COVERED NBRCYCLS,P -- FIX UP S', line=1911)

W('16,2417', 0o01440, '200CSHI', '2DEC', '200 B-12', kind='data', line=1913)
W('16,2420', 0o00000, kind='data', line=1913)

W('16,2421', 0o55340, 'EARTHMU', '2DEC*', '-3.986032 E10 B-36*', kind='data', line=1915)
W('16,2422', 0o61710, kind='data', line=1915)

W('16,2423', 0o04000, 'EP4(45)L', '2DEC', '.125', kind='data', line=1917)
W('16,2424', 0o00000, kind='data', line=1917)

W('16,2425', 0o00707, 'EP4(10)L', '2DEC', '.027777777', kind='data', line=1919)
W('16,2426', 0o03434, kind='data', line=1919)

# Page 726
# NAME:                 S40.13 -- TIMEBURN
#
# FUNCTION              (1) DETERMINE WHETHER A GIVEN COMBINATION OF VELOCITY-TO-
# BE-GAINED AND ENGINE CHOICE RESULT IN A BURN TIME SUFFICIENT
# TO ALLOW STEERING AT THE VEHICLE DURING THE BURN, AND
# (2) THE MAGNITUDE OF THE RESULTING BURN TIME -- IF IT IS SHORT --
# AND THE ASSOCIATED TIME OF THE ENGINE OFF SIGNAL.
#
# CALLING SEQUENCE      VIA FINDVAC AS A NEW JOB
#
# INPUT                 VGTIG -- VELOCITY TO BE GAINED VECTOR (METERS/CS) AT +7
# WEIGHT/G -- MASS OF VEHICLE IN KGM AT TIG
# F -- ENGINE THRUST IN M.NEWTONS AT +7
# MDOT -- RATE OF DECREASE OF VEHICLE MASS DURING ENGINE BURN
# IN KILOGRAMS/CENTISECOND AT +3.  THIS SCALING MAY
# REQUIRE MODIFICATION FOR SATURN BURNS.
#
# OUTPUT                IMPULSW         ZERO FOR STEERING
# ONE FOR ATTITUDE HOLD
# TGO             TIME TO BURN IN CENTISECONDS AT +14
# THE QUANTITY M.NEWTON SHALL BE USED TO EXPRESS WEIGHT IN TERMS OF
# (KILOGRAM*METER)/(CENTISECOND*CENTISECOND)
# (1) M.NEWTON = (10000) NEWTONS.

#   EBANK= TGO
#   COUNT 16/40.13

W('16,2427', 0o06006, 'S40.13', 'TC', 'INTPRET', line=1949)
W('16,2430', 0o43001, '', 'SETPD', 'SET', kind='interp', line=1950)
W('16,2431', 0o00001, '', '', '00D', kind='operand', line=1951)
W('16,2432', 0o01066, '', '', 'IMPULSW', 'ASSUME NO STEERING UNTIL FOUND OTHERWISE', kind='operand', line=1952)
W('16,2433', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=1953)
W('16,2434', 0o03721, '', '', 'VGTIG', 'VELOCITY TO BE GAINED AT +7', kind='operand', line=1954)
W('16,2435', 0o77776, '', 'EXIT', kind='interp', line=1955)
W('16,2436', 0o35011, '', 'CAF', 'BIT7', 'TEST +X TRANSLATION', line=1956)
W('16,2437', 0o00006, '', 'EXTEND', line=1957)
W('16,2440', 0o06031, '', 'RXOR', 'CHAN31', line=1958)
W('16,2441', 0o75011, '', 'MASK', 'BIT7', line=1959)
W('16,2442', 0o00006, '', 'EXTEND', line=1960)
W('16,2443', 0o12525, '', 'BZF', 'NOTADDUL', line=1961)
W('16,2444', 0o06006, '', 'TC', 'INTPRET', line=1962)
W('16,2445', 0o56325, '', 'PDDL', 'DDV', '00D = MAG OF VGTIG AT +7', kind='interp', line=1963)
W('16,2446', 0o36021, '', '', 'S40.135', 'COMPENSATION FOR 2 JET ULLAGE AT +24', kind='operand', line=1964)
W('16,2447', 0o03076, '', '', 'WEIGHT/G', 'MASS IN KGMS AT +16', kind='operand', line=1965)
W('16,2450', 0o72414, '', 'BON', 'SL1', 'DOUBLE CORRECTION IF FOUR JETS', kind='interp', line=1966)
W('16,2451', 0o00700, '', '', 'NJETSFLG', kind='operand', line=1967)
W('16,2452', 0o34453, '', '', 'S40.130', kind='operand', line=1968)
W('16,2453', 0o77621, 'S40.130', 'BDSU', kind='interp', line=1969)
W('16,2454', 0o56325, '', 'PDDL', 'DDV', '00D = MAG OF VGTIG CORRECTED FOR ULLAGE', kind='interp', line=1970)
W('16,2455', 0o01770, '', '', 'K1VAL', 'M.NEWTON-CS AT +24', kind='operand', line=1971)
W('16,2456', 0o03076, '', '', 'WEIGHT/G', kind='operand', line=1972)
W('16,2457', 0o50021, '', 'BDSU', 'BMN', kind='interp', line=1973)
W('16,2460', 0o00001, '', '', '00D', kind='operand', line=1974)
W('16,2461', 0o34504, '', '', 'S40.131', 'TGO LESS THAN 100 CS', kind='operand', line=1975)
W('16,2462', 0o41325, '', 'PDDL', 'DMP', '02D = TEMP1 AT +7', kind='interp', line=1976)
# Page 727
W('16,2463', 0o00111, '', '', 'EMDOT', 'SPS FLOW RATE SC.AT B+3 KG/CS (SP, NOTE)', kind='operand', line=1978)
W('16,2464', 0o36015, '', '', '3.5SEC', '350 CS AT +14', kind='operand', line=1979)
W('16,2465', 0o65221, '', 'BDSU', 'PDDL', kind='interp', line=1980)
W('16,2466', 0o03076, '', '', 'WEIGHT/G', kind='operand', line=1981)
W('16,2467', 0o01775, '', '', 'FANG', kind='operand', line=1982)
W('16,2470', 0o60405, '', 'DMP', 'SR2', kind='interp', line=1983)
W('16,2471', 0o36017, '', '', '5SECOND', '500 CS AT +14', kind='operand', line=1984)
W('16,2472', 0o41471, '', 'DDV', 'PUSH', '04D = TEMP2', kind='interp', line=1985)
W('16,2473', 0o51021, '', 'BDSU', 'BPL', kind='interp', line=1986)
W('16,2474', 0o00003, '', '', '02D', kind='operand', line=1987)
W('16,2475', 0o34520, '', '', 'S40.133', 'TGO GREATER THAN 600 CS', kind='operand', line=1988)
W('16,2476', 0o55345, '', 'DLOAD', 'BDDV', kind='interp', line=1989)
W('16,2477', 0o43205, '', 'DMP', 'DAD', kind='interp', line=1990)
W('16,2500', 0o36017, '', '', '5SECOND', '500 CS AT +14', kind='operand', line=1991)
W('16,2501', 0o36013, '', '', '1SEC2D', '100 CS AT +14', kind='operand', line=1992)
W('16,2502', 0o77650, '', 'GOTO', kind='interp', line=1993)
W('16,2503', 0o34511, '', '', 'S40.132', kind='operand', line=1994)
W('16,2504', 0o41345, 'S40.131', 'DLOAD', 'DMP', 'TGO LESS THAN 100 CS', kind='interp', line=1995)
W('16,2505', 0o03076, '', '', 'WEIGHT/G', kind='operand', line=1996)
W('16,2506', 0o56215, '', 'DAD', 'DDV', kind='interp', line=1997)
W('16,2507', 0o01772, '', '', 'K2VAL', 'M.NEWTON CS AT +24', kind='operand', line=1998)
W('16,2510', 0o01774, '', '', 'K3VAL', 'M.NEWTON AT +10', kind='operand', line=1999)
W('16,2511', 0o77776, 'S40.132', 'EXIT', kind='interp', line=2000)
#   EBANK= TGO
W('16,2512', 0o07226, '', 'TC', 'TPAGREE', line=2002)
W('16,2513', 0o30154, '', 'CA', 'MPAC', line=2003)
W('16,2514', 0o56001, '', 'XCH', 'L', line=2004)
W('16,2515', 0o35021, '', 'CA', 'ZERO', line=2005)
W('16,2516', 0o53430, '', 'DXCH', 'TGO', 'TGO IN CS AT +28', line=2006)
W('16,2517', 0o02522, '', 'TC', 'S40.134', line=2007)
W('16,2520', 0o77414, 'S40.133', 'CLEAR', 'EXIT', 'WILL STEER VEHICLE', kind='interp', line=2008)
W('16,2521', 0o01266, '', '', 'IMPULSW', kind='operand', line=2009)
W('16,2522', 0o05412, 'S40.134', 'TC', 'PHASCHNG', 'KILL GROUP 3', line=2010)
W('16,2523', 0o00003, '', 'OCT', '3', kind='data', line=2011)

W('16,2524', 0o15217, '', 'TCF', 'ENDOFJOB', line=2013)

W('16,2525', 0o06006, 'NOTADDUL', 'TC', 'INTPRET', line=2015)
W('16,2526', 0o77650, '', 'GOTO', kind='interp', line=2016)
W('16,2527', 0o34454, '', '', 'S40.130 +1', 'DO NOT COMPENSATE FOR 7 SEC OF ULLAGE', kind='operand', line=2017)
#   SETLOC DAPS7
#   BANK

#   COUNT 17/40.13

S('K1VAL', 'equals', 0o1767, line=2023)  # DP PAD LOAD B+23 NEWTON-SEC/E+2
S('K2VAL', 'equals', 0o1771, line=2024)  # DP PAD LOAD B+23 NEWTON-SEC/E+2
S('K3VAL', 'equals', 0o1773, line=2025)  # DP PAD LOAD B+09 NEWTONS/E+4
W('17,2012', 0o00144, '1SEC2D', '2DEC', '100.0 B-14', '100.0 CS AT +14', kind='data', line=2026)
W('17,2013', 0o00000, kind='data', line=2026)
# Page 728
W('17,2014', 0o01274, '3.5SEC', '2DEC', '350.0 B-13', '350 CS AT +13', kind='data', line=2028)
W('17,2015', 0o00000, kind='data', line=2028)

W('17,2016', 0o00764, '5SECOND', '2DEC', '500.0 B-14', '500.0 CS AT +14', kind='data', line=2030)
W('17,2017', 0o00000, kind='data', line=2030)

W('17,2020', 0o00000, 'S40.135', '2DEC', '69.6005183 B-23', 'IMPULSE FROM 7.96 SECS OF 2-JET FIRING', kind='data', line=2032)
W('17,2021', 0o04263, kind='data', line=2032)
# 7.96 (199.6)COS(10) LB-SEC, SC.AT
# B+23 NEWTON-SEC/E+2 (7 SEC ULLAGE
# TO GO, PLUS 0.96 SEC FROM PIPTIME)

# Page 729
# NAME          S40.6 GIMBAL DRIVE TEST AND/OR GIMBAL TRIM
# MOD NO 5                              DATE 9 MARCH, 1967
# MOD BY ENGEL                          LOG SECTION P40-P47
#
# FUNCTIONAL DESCRIPTION
# GIMBAL DRIVE TEST....0,+2,-2,0 DEGREE ENGINE COMMANDS, AT 2 SECOND
# INTERVALS, FIRST IN PITCH, THEN IN YAW.  ASTRONAUT VERIFICATION
# OF GIMBAL MOTION ON GPI
# GIMBAL TRIM....AFTER A 4 SECOND DELAY, ENGINE COMMANDED TO
# PRE-COMPUTED TRIM POSITION.  ASTRONAUT VERIFICATION ON GPI.
# PRE40.6....RESTART ENTRY TO RE-DO S40.6, ONLY IF RCS IS ON --- IF TVC
# IS NOT ON --- PRIMARILY TO GET ACTUATORS TRIMMED FOR IGNITION.
# BYPASS 4 SEC DELAY.  SPEED IS CRITICAL NEAR IGNITION.
# IF TVC IS ON (TVCDAPON OR LATER) THEN REDOTVC WILL TAKE CARE
# OF RESTARTING ACTUATORS.
#
# CALLING SEQUENCE....
# WAITLIST, WITH 2CADR FOR S40.6 (OR PRE40.6), WITH EBANK= CNTR
#
# NORMAL EXIT MODE -- FIXDELAY, TASKOVER
#
# SUBROUTINES CALLED....
# OUTPUT (INTERNAL)
# FIXDELAY
#
# ALARM OR ABORT EXIT MODES --- NONE
#
# ERASABLE INITIALIZATION REQUIRED
# CNTR = +0, NORMALLY SET BY THE P40 CALL AT TST,TRIM.
# MRKRTMP....POSITIVE FOR GIMBAL DRIVE TEST AND GIMBAL TRIM (BOTH)
# NEGATIVE FOR GIMBAL TRIM ONLY
# PACTOFF, YACTOFF SC.AT 85.41 ARCSEC/BIT (V48N48 P, YTRIM)
# "SC CONT" SWITCH AT "CMC" (A/P CONTROL SWITCH AT "GNC")
# ACTIVE SPS GIMBAL MOTOR POWER(S), PITCH, YAW
#
# OUTPUT
# TVCYAW, TVCPITCH (BITS RELEASED)
# TVC ENABLE AND OPTICS ERROR COUNTER ENABLE
#
# DEBRIS
# TBMPR60, CNTR

#   BANK 17
#   SETLOC DAPS6
#   BANK

#   EBANK= CNTR
#   COUNT 20/S40.6

W('20,2241', 0o40102, 'PRE40.6', 'CS', 'FLAGWRD6', 'RESTART ENTRY TO S40.6 (DO NOT PERMIT', line=2087)
W('20,2242', 0o74105, '', 'MASK', 'OCT60000', '      IF TVC, BITS 15,14 = 1,0)', line=2088)
W('20,2243', 0o00006, '', 'EXTEND', line=2089)
W('20,2244', 0o62246, '', 'BZMF', '+2', line=2090)
W('20,2245', 0o15324, '', 'TCF', 'TASKOVER', 'TVC, REDOTVC WILL REESTABLISH INTERFACE', line=2091)

W('20,2246', 0o45017, '', 'CS', 'BIT1', 'RCS, SO DO S40.6, GIMTRIM ONLY', line=2093)
# Page 730
W('20,2247', 0o55445, '', 'TS', 'MRKRTMP', line=2095)

W('20,2250', 0o35017, '', 'CAF', 'BIT1', 'FOR REVISED S40.6 TIMING FOR RESTARTS...', line=2097)
W('20,2251', 0o55447, '', 'TS', 'CNTR', 'TO INDICATE A RESTART ENTRY (CNTR 1S', line=2098)
# NORMALLY +0, BY S40.6)

#   EBANK= CNTR
W('20,2252', 0o45021, 'S40.6', 'CS', 'ZERO', 'INHIBIT OPTICS ACTIVITY', line=2102)
W('20,2253', 0o55303, '', 'TS', 'OPTIND', line=2103)

W('20,2254', 0o45016, '', 'CS', 'BIT2', 'DISENABLE OPTICS ERROR COUNTERS (ZERO,', line=2105)
W('20,2255', 0o00006, '', 'EXTEND', '', '      AND INHIBIT PULSE TRANSMISSION --', line=2106)
W('20,2256', 0o03012, '', 'WAND', 'CHAN12', '      NORMAL STATE)', line=2107)

W('20,2257', 0o32344, '', 'CAF', 'OCT02200', 'TVC ENABLE (SPS SERVO AMPS SEE DAC', line=2109)
W('20,2260', 0o00006, '', 'EXTEND', '', '      VOLTAGES) AND DISENGAGE OPTICS/DAC', line=2110)
W('20,2261', 0o05012, '', 'WOR', 'CHAN12', line=2111)

W('20,2262', 0o05267, '', 'TC', 'FIXDELAY', '60MS PROCEDURAL DELAY (40MS MINIMUM) FOR', line=2113)
W('20,2263', 0o00006, '', 'DEC', '6', '      RELAY LATCHING', kind='data', line=2114)

W('20,2264', 0o35016, '', 'CAF', 'BIT2', 'ENABLE OPTICS ERROR COUNTERS', line=2116)
W('20,2265', 0o00006, '', 'EXTEND', line=2117)
W('20,2266', 0o05012, '', 'WOR', 'CHAN12', line=2118)

W('20,2267', 0o05267, '', 'TC', 'FIXDELAY', '20MS PROCEDURAL DELAY (4MS MINIMUM) FOR', line=2120)
W('20,2270', 0o00002, '', 'DEC', '2', '      RELAY LATCHING', kind='data', line=2121)

W('20,2271', 0o11447, 'RSTRTST', 'CCS', 'CNTR', 'CHECK FOR RESTART ENTRY (PRE40.6)', line=2123)
W('20,2272', 0o12332, '', 'TCF', 'GIMTRIM +2', 'RESTART ENTRY....BYPASS 4 SECOND DELAY', line=2124)
# TST,TRIM SETS +0 ON NORMAL ENTRY

W('20,2273', 0o31445, '', 'CAE', 'MRKRTMP', 'CHECK FOR TEST/TRIM OR TRIM ONLY', line=2127)
W('20,2274', 0o55447, '', 'TS', 'CNTR', '      MRKRTMP SAVES CNTR FOR RESTARTS', line=2128)
W('20,2275', 0o00006, '', 'EXTEND', line=2129)
W('20,2276', 0o62330, '', 'BZMF', 'GIMTRIM', '(TRIM ONLY)', line=2130)

W('20,2277', 0o45021, 'GDTSETUP', 'CS', 'ZERO', 'GIMBAL DRIVE TEST SETUP, FOR PITCH', line=2132)
W('20,2300', 0o55447, '', 'TS', 'CNTR', line=2133)

W('20,2301', 0o32346, 'GIMDTEST', 'CAF', '+2ACTDEG', 'GIMBAL DRIVE TEST, 1ST INCREMENT', line=2135)
W('20,2302', 0o02315, '', 'TC', 'OUTPUT', '      (LEAVES GIMBAL AT +2 DEG)', line=2136)
W('20,2303', 0o32345, '', 'CAF', '-4ACTDEG', '2ND INCREMENT (LEAVES GIMBAL AT -2)', line=2137)
W('20,2304', 0o02315, '', 'TC', 'OUTPUT', line=2138)
W('20,2305', 0o32346, '', 'CAF', '+2ACTDEG', '3RD INCREMENT (LEAVES GIMBAL AT -0)', line=2139)
W('20,2306', 0o02315, '', 'TC', 'OUTPUT', line=2140)

W('20,2307', 0o41447, '', 'CS', 'CNTR', 'CHECK FOR COMPLETION OF YAW TEST.', line=2142)
# Page 731
W('20,2310', 0o10000, '', 'CCS', 'A', line=2144)
W('20,2311', 0o12330, '', 'TCF', 'GIMTRIM', 'COMPLETED, GO TO GIMBAL TRIM ROUTINE', line=2145)
W('20,2312', 0o45017, '', 'CS', 'BIT1', 'SET UP YAW TEST', line=2146)
W('20,2313', 0o55447, '', 'TS', 'CNTR', line=2147)
W('20,2314', 0o12301, '', 'TCF', 'GIMDTEST', 'FOR YAW TEST', line=2148)

W('20,2315', 0o00006, 'OUTPUT', 'EXTEND', '', 'OUTPUT THE INCREMENT....SAVE Q', line=2150)
W('20,2316', 0o23146, '', 'QXCH', 'TEMPR60', line=2151)

W('20,2317', 0o51447, '', 'INDEX', 'CNTR', line=2153)
W('20,2320', 0o54054, '', 'TS', 'TVCPITCH', line=2154)

W('20,2321', 0o51447, '', 'INDEX', 'CNTR', line=2156)
W('20,2322', 0o35005, '', 'CAF', 'BIT11', line=2157)
W('20,2323', 0o00006, '', 'EXTEND', line=2158)
W('20,2324', 0o05014, '', 'WOR', 'CHAN14', line=2159)

W('20,2325', 0o05267, '', 'TC', 'FIXDELAY', 'WAIT 2SEC, WHILE ASTRONAUT VERIFIES', line=2161)
W('20,2326', 0o00310, '', 'DEC', '200', '      GIMBAL MOTION ON GPI', kind='data', line=2162)
W('20,2327', 0o01146, '', 'TC', 'TEMPR60', line=2163)

W('20,2330', 0o05267, 'GIMTRIM', 'TC', 'FIXDELAY', 'WAIT 4 SECONDS BEFORE GIMBAL TRIM', line=2165)
W('20,2331', 0o00620, '', 'DEC', '400', kind='data', line=2166)

W('20,2332', 0o45021, '', 'CS', 'ZERO', 'PICK UP TRIM VALUES AND OUTPUT THEM', line=2168)
W('20,2333', 0o61423, '', 'AD', 'PACTOFF', '      (AVOID +0) ENTRY POINT FROM RSTRTST', line=2169)
W('20,2334', 0o54054, '', 'TS', 'TVCPITCH', '      ON A RESTART, TO AVOID 4SEC DELAY', line=2170)
W('20,2335', 0o45021, '', 'CS', 'ZERO', line=2171)
W('20,2336', 0o61424, '', 'AD', 'YACTOFF', line=2172)
W('20,2337', 0o54053, '', 'TS', 'TVCYAW', line=2173)

W('20,2340', 0o35062, '', 'CAF', 'PRIO6', 'RELEASE THE COUNTERS, BITS 11,12', line=2175)
W('20,2341', 0o00006, '', 'EXTEND', line=2176)
W('20,2342', 0o05014, '', 'WOR', 'CHAN14', line=2177)

W('20,2343', 0o15324, 'ENDS40.6', 'TCF', 'TASKOVER', line=2179)

W('20,2344', 0o02200, 'OCT02200', 'OCT', '02200', 'BITS 8,11 FOR CHANNEL 12 TVC/OPTICS', kind='data', line=2181)
W('20,2345', 0o77527, '-4ACTDEG', 'DEC', '-168', '-2(+2ACTDEG), WHOLE BITS, NO ROUNDUP', kind='data', line=2182)
W('20,2346', 0o00124, '+2ACTDEG', 'DEC', '+84', '+2 DEG, SC.AT 85.41 ARCSEC/BIT (+84D)', kind='data', line=2183)

# CALLED BY "DONOUN46" (VERB 48), OR DIRECTLY BY "FRESHDAP" (RCS DAP) VIA IBNKCALL

#   COUNT 20/S41.2

W('20,2347', 0o31466, 'S41.2', 'CA', 'DAPDATR1', line=2189)
# Page 732
W('20,2350', 0o76214, '', 'MASK', 'THREE', line=2191)
W('20,2351', 0o60000, '', 'AD', 'A', line=2192)
W('20,2352', 0o55130, '', 'TS', 'RATEINDX', line=2193)

W('20,2353', 0o00004, '', 'INHINT', line=2195)
W('20,2354', 0o31466, '', 'CAE', 'DAPDATR1', 'IS LEM ATTACHED (BITS 14,13 OF DAPDATR1', line=2196)
W('20,2355', 0o74371, '', 'MASK', 'PRIO30', '      =10)', line=2197)
W('20,2356', 0o67705, '', 'AD', '-BIT14', '(OCT57777)', line=2198)
W('20,2357', 0o00006, '', 'EXTEND', line=2199)
W('20,2360', 0o12365, '', 'BZF', 'TOGETHER', 'YES', line=2200)

W('20,2361', 0o45016, '', 'CS', 'BIT2', 'NO, UNSET FLAG', line=2202)
W('20,2362', 0o70103, '', 'MASK', 'FLAGWRD7', line=2203)
W('20,2363', 0o54103, '', 'TS', 'FLAGWRD7', line=2204)

W('20,2364', 0o12370, '', 'TCF', '+4', line=2206)

W('20,2365', 0o40103, 'TOGETHER', 'CS', 'FLAGWRD7', 'ATTACHED, SET FLAG FOR INTEGRATION', line=2208)
W('20,2366', 0o75016, '', 'MASK', 'BIT2', line=2209)
W('20,2367', 0o26103, '', 'ADS', 'FLAGWRD7', line=2210)

W('20,2370', 0o00003, '', 'RELINT', line=2212)

W('20,2371', 0o31466, '', 'CA', 'DAPDATR1', line=2214)
W('20,2372', 0o75014, '', 'MASK', 'BIT4', line=2215)
W('20,2373', 0o00006, '', 'EXTEND', line=2216)
W('20,2374', 0o62376, '', 'BZMF', '+2', 'DEC 46 MEANS NARROW DB', line=2217)
W('20,2375', 0o32476, '', 'CA', 'DEC409', line=2218)
W('20,2376', 0o62477, '', 'AD', 'DEC46', 'DEC 455 MEANS WIDE DB', line=2219)
W('20,2377', 0o55655, '', 'TS', 'ADB', line=2220)

W('20,2400', 0o31466, '', 'CA', 'DAPDATR1', line=2222)
W('20,2401', 0o75011, '', 'MASK', 'BIT7', 'QUAD BD', line=2223)
W('20,2402', 0o00006, '', 'EXTEND', line=2224)
W('20,2403', 0o62405, '', 'BZMF', '+2', line=2225)
W('20,2404', 0o35017, '', 'CA', 'ONE', line=2226)
W('20,2405', 0o55631, '', 'TS', 'XTRANS', line=2227)
W('20,2406', 0o31466, '', 'CA', 'DAPDATR1', line=2228)
W('20,2407', 0o75006, '', 'MASK', 'BIT10', 'QUAD AC', line=2229)
W('20,2410', 0o00006, '', 'EXTEND', line=2230)
W('20,2411', 0o62413, '', 'BZMF', '+2', line=2231)
W('20,2412', 0o45017, '', 'CS', 'ONE', line=2232)
W('20,2413', 0o27631, '', 'ADS', 'XTRANS', line=2233)

W('20,2414', 0o00004, '', 'INHINT', line=2235)
W('20,2415', 0o00006, '', 'EXTEND', line=2236)
W('20,2416', 0o12423, '', 'BZF', '+5', 'CLEAR NJETSFLG (4 JETS, OR NO JETS)', line=2237)
W('20,2417', 0o40075, '', 'CS', 'FLAGWRD1', 'SET NJETSFLG (2 JETS, AC OR BD QUADS)', line=2238)
W('20,2420', 0o75001, '', 'MASK', 'BIT15', 'NJETSFLG = 1 FOR 2 JET ULLAGE (AC OR BD)', line=2239)
W('20,2421', 0o26075, '', 'ADS', 'FLAGWRD1', line=2240)
# Page 733
W('20,2422', 0o12426, '', 'TCF', '+4', line=2242)
W('20,2423', 0o45001, '', 'CS', 'BIT15', 'KJETSFLG = 0 FOR 4 JET (OR 0 JET) ULLAGE', line=2243)
W('20,2424', 0o70075, '', 'MASK', 'FLAGWRD1', line=2244)
W('20,2425', 0o54075, '', 'TS', 'FLAGWRD1', line=2245)
W('20,2426', 0o00003, '', 'RELINT', line=2246)
W('20,2427', 0o31467, '', 'CA', 'DAPDATR2', line=2247)
W('20,2430', 0o75003, '', 'MASK', 'BIT13', line=2248)
W('20,2431', 0o00006, '', 'EXTEND', line=2249)
W('20,2432', 0o62434, '', 'BZMF', '+2', line=2250)
W('20,2433', 0o12435, '', 'TCF', '+2', line=2251)
W('20,2434', 0o45017, '', 'CS', 'ONE', line=2252)
W('20,2435', 0o40000, '', 'COM', line=2253)
W('20,2436', 0o55630, '', 'TS', 'ACORBD', 'MINUS FOR A-C, PLUS FOR B-D', line=2254)

W('20,2437', 0o31467, '', 'CA', 'DAPDATR2', line=2256)
W('20,2440', 0o75006, '', 'MASK', 'BIT10', line=2257)
W('20,2441', 0o10000, '', 'CCS', 'A', line=2258)
W('20,2442', 0o12446, '', 'TCF', '+4', line=2259)
W('20,2443', 0o35017, '', 'CA', 'ONE', line=2260)
W('20,2444', 0o55626, '', 'TS', 'RACFAIL', line=2261)
W('20,2445', 0o12456, '', 'TCF', 'BDFAIL', line=2262)
W('20,2446', 0o35021, '', 'CA', 'ZERO', line=2263)
W('20,2447', 0o55626, '', 'TS', 'RACFAIL', line=2264)
W('20,2450', 0o31467, '', 'CA', 'DAPDATR2', line=2265)
W('20,2451', 0o75014, '', 'MASK', 'BIT4', line=2266)
W('20,2452', 0o10000, '', 'CCS', 'A', line=2267)
W('20,2453', 0o12456, '', 'TCF', 'BDFAIL', line=2268)
W('20,2454', 0o45017, '', 'CS', 'ONE', line=2269)
W('20,2455', 0o55626, '', 'TS', 'RACFAIL', line=2270)
W('20,2456', 0o31467, 'BDFAIL', 'CA', 'DAPDATR2', line=2271)
W('20,2457', 0o75011, '', 'MASK', 'BIT7', line=2272)
W('20,2460', 0o10000, '', 'CCS', 'A', line=2273)
W('20,2461', 0o12465, '', 'TCF', '+4', line=2274)
W('20,2462', 0o35017, '', 'CA', 'ONE', line=2275)
W('20,2463', 0o55627, '', 'TS', 'RBDFAIL', line=2276)
W('20,2464', 0o00002, '', 'TC', 'Q', line=2277)
W('20,2465', 0o35021, '', 'CA', 'ZERO', line=2278)
W('20,2466', 0o55627, '', 'TS', 'RBDFAIL', line=2279)
W('20,2467', 0o31467, '', 'CA', 'DAPDATR2', line=2280)
W('20,2470', 0o75017, '', 'MASK', 'BIT1', line=2281)
W('20,2471', 0o10000, '', 'CCS', 'A', line=2282)
W('20,2472', 0o00002, '', 'TC', 'Q', line=2283)
W('20,2473', 0o45017, '', 'CS', 'ONE', line=2284)
W('20,2474', 0o55627, '', 'TS', 'RBDFAIL', line=2285)
W('20,2475', 0o00002, '', 'TC', 'Q', line=2286)

# DAPFIG ENTRY VIA TC POSTJUMP AS JOB FROM "STABLISH" (VERB 46)

#   BANK 42
#   SETLOC EXTVBS
# Page 734
#   BANK

W('42,3606', 0o45007, 'DAPFIG', 'CS', 'BIT9', 'TURN OFF SIVB TAKEOVER', line=2295)
W('42,3607', 0o00006, '', 'EXTEND', line=2296)
W('42,3610', 0o03012, '', 'WAND', 'CHAN12', line=2297)
W('42,3611', 0o31466, '', 'CAE', 'DAPDATR1', 'DETERMINE VEHICLE CONFIGURATION', line=2298)
W('42,3612', 0o00006, '', 'EXTEND', line=2299)
W('42,3613', 0o75015, '', 'MP', 'BIT3', '      RIGHT SHIFT 4 OCTAL DIGITS', line=2300)
W('42,3614', 0o76214, '', 'MASK', 'THREE', '      (IN CASE BIT 15 IS USED)', line=2301)
W('42,3615', 0o50000, '', 'INDEX', 'A', line=2302)
W('42,3616', 0o13617, '', 'TCF', '+1', '      BRANCH BASED ON CONFIG....', line=2303)

W('42,3617', 0o13631, '', 'TCF', 'NODAPUP', 'CM.......ACTIVATE NODAP', line=2305)
W('42,3620', 0o13624, '', 'TCF', 'RCSDAPUP', '      CSM......ACTIVATE RCSDAP', line=2306)
W('42,3621', 0o13624, '', 'TCF', 'RCSDAPUP', '      CSM/LEM..ACTIVATE RCSDAP', line=2307)
W('42,3622', 0o04701, '', 'TC', 'POSTJUMP', line=2308)
W('42,3623', 0o67215, '', 'CADR', 'SATSTKON', kind='data', line=2309)
W('42,3624', 0o00004, 'RCSDAPUP', 'INHINT', '', 'CALL TO ACTIVATE RCSDAP, AND RETURN', line=2310)
W('42,3625', 0o04740, '', 'TCR', 'IBNKCALL', line=2311)
W('42,3626', 0o42024, '', 'CADR', 'RCSDAPON', kind='data', line=2312)
W('42,3627', 0o00003, '', 'RELINT', line=2313)
W('42,3630', 0o13646, '', 'TCF', 'ENDFIG', 'CAME IN VIA V46, GO OUT VIA GOPIN', line=2314)
W('42,3631', 0o00006, 'NODAPUP', 'EXTEND', '', "T5 IDLE FOR NODAP (DON'T WORRY ABOUT T)", line=2315)
W('42,3632', 0o33651, '', 'DCA', 'T5IDLDAP', line=2316)
W('42,3633', 0o53313, '', 'DXCH', 'T5LOC', line=2317)
W('42,3634', 0o05560, '', 'TC', 'DOWNFLAG', 'RESET T5-USAGE FLAGS FOR NODAP', line=2318)
W('42,3635', 0o00132, '', 'ADRES', 'DAPBIT1', 'BIT 15 FLAG 6 = 0', kind='data', line=2319)
W('42,3636', 0o05560, '', 'TC', 'DOWNFLAG', line=2320)
W('42,3637', 0o00133, '', 'ADRES', 'DAPBIT2', 'BIT 14 FLAG 6 = 0', kind='data', line=2321)
W('42,3640', 0o00004, '', 'INHINT', line=2322)
W('42,3641', 0o04740, '', 'TC', 'IBNKCALL', 'ZERO JET CHANNELS IN 14 MS AND THEN', line=2323)
W('42,3642', 0o42632, '', 'CADR', 'ZEROJET', 'LEAVE THE T6 CLOCK DISABLED.', kind='data', line=2324)
W('42,3643', 0o00003, '', 'RELINT', line=2325)
W('42,3644', 0o35017, '', 'CAF', 'BIT1', 'KILL KALCMANU JOB', line=2326)
W('42,3645', 0o55332, '', 'TS', 'HOLDFLAG', line=2327)
W('42,3646', 0o04701, 'ENDFIG', 'TC', 'POSTJUMP', 'CAME IN VIA V46, GO OUT VIA GOPIN', line=2328)
W('42,3647', 0o66121, '', 'CADR', 'GOPIN', kind='data', line=2329)
#   SBANK= PINSUPER  # Added by RSB 2009
#   EBANK= PACTOFF
W('42,3650', 0o03153, 'T5IDLDAP', '2CADR', 'T5IDLOC', kind='data', line=2332)
W('42,3651', 0o12106, kind='data', line=2332)

#   SBANK= LOWSUPER
#   BANK 17
#   SETLOC DAPS6
#   BANK

W('20,2476', 0o00631, 'DEC409', 'DEC', '409', kind='data', line=2339)
W('20,2477', 0o00056, 'DEC46', 'DEC', '46', kind='data', line=2340)

# Page 735

# CALLED BY "DONOUN47" (VERB 48), OR DIRECTLY BY "FRESHDAP" (RCS DAP)
W('20,2500', 0o31470, 'S40.14', 'CAE', 'IXX', 'RCS ENTRY', line=2345)
W('20,2501', 0o00006, '', 'EXTEND', line=2346)
W('20,2502', 0o72525, '', 'MP', 'CONTONE', line=2347)
W('20,2503', 0o55623, '', 'TS', 'J/M', line=2348)

W('20,2504', 0o31471, '', 'CA', 'IAVG', line=2350)
W('20,2505', 0o00006, '', 'EXTEND', line=2351)
W('20,2506', 0o72525, '', 'MP', 'CONTONE', line=2352)
W('20,2507', 0o55624, '', 'TS', 'J/M1', line=2353)

W('20,2510', 0o55625, '', 'TS', 'J/M2', line=2355)

W('20,2511', 0o00006, '', 'EXTEND', line=2357)
W('20,2512', 0o32527, '', 'DCA', 'CONTTWO', line=2358)
W('20,2513', 0o00006, '', 'EXTEND', line=2359)
W('20,2514', 0o11470, '', 'DV', 'IXX', line=2360)
W('20,2515', 0o55620, '', 'TS', 'KMJ', line=2361)

W('20,2516', 0o00006, '', 'EXTEND', line=2363)
W('20,2517', 0o32527, '', 'DCA', 'CONTTWO', line=2364)
W('20,2520', 0o00006, '', 'EXTEND', line=2365)
W('20,2521', 0o11471, '', 'DV', 'IAVG', line=2366)
W('20,2522', 0o55621, '', 'TS', 'KMJ1', line=2367)

W('20,2523', 0o55622, '', 'TS', 'KMJ2', line=2369)

W('20,2524', 0o00002, '', 'TC', 'Q', line=2371)

W('20,2525', 0o25137, 'CONTONE', 'DEC', '.662034', '2PI/M', kind='data', line=2373)
W('20,2526', 0o00023, 'CONTTWO', '2DEC', '.00118', kind='data', line=2374)
W('20,2527', 0o12522, kind='data', line=2374)

#   COUNT 24/TVNG

#   BANK 31
#   SETLOC P40S
#   BANK

W('24,3761', 0o37405, 'POS-2.5', 'OCT', '37405', kind='data', line=2382)
#   EBANK= DAPDATR1
W('24,3762', 0o02014, 'RCSCADR', '2CADR', 'RCSUP', kind='data', line=2384)
W('24,3763', 0o42066, kind='data', line=2384)

W('24,3764', 0o37704, '6SECT5', 'OCT', '37704', kind='data', line=2386)
#   COUNT 21/RCSUP

#   BANK 20

#   SETLOC DAPS3
#   BANK

# Page 736

W('21,2014', 0o22016, 'RCSUP', 'LXCH', 'BANKRUPT', line=2396)
W('21,2015', 0o00006, '', 'EXTEND', line=2397)
W('21,2016', 0o22012, '', 'QXCH', 'QRUPT', line=2398)

W('21,2017', 0o02024, '', 'TCR', 'RCSDAPON', 'ACTIVATE RCS DAP', line=2400)

W('21,2020', 0o15333, '', 'TCF', 'RESUME', line=2402)

#   EBANK= DAPDATR1
W('21,2021', 0o02122, 'RCSADDR', '2CADR', 'RCSATT', kind='data', line=2405)
W('21,2022', 0o42066, kind='data', line=2405)

W('21,2023', 0o37704, '0.6SECT5', 'OCT', '37704', kind='data', line=2407)

# RCSDAPON ENTRY MUST BE UNDER INT-INHIBIT
W('21,2024', 0o32023, 'RCSDAPON', 'CAF', '0.6SECT5', '0.6 SEC ALLOWS TVCEXEC/ROLLDAP TO DIE', line=2410)
W('21,2025', 0o54030, '', 'TS', 'TIME5', 'ENTRY FROM R00TOP00', line=2411)
W('21,2026', 0o55465, '', 'TS', 'T5PHASE', 'WILL CAUSE FRESHDAP (+1)', line=2412)

W('21,2027', 0o41501, '', 'CS', 'RCSFLAGS', 'SET BIT3 TO REINITIALIZE FDAI ERROR', line=2414)
W('21,2030', 0o75015, '', 'MASK', 'BIT3', '      DISPLAY, IN CASE SC CONT SWITCH', line=2415)
W('21,2031', 0o27501, '', 'ADS', 'RCSFLAGS', '      IN SCS NOT GNC (GUIDEMODE PRIMARY)', line=2416)

W('21,2032', 0o00006, '', 'EXTEND', line=2418)
W('21,2033', 0o32022, '', 'DCA', 'RCSADDR', '(RCSATT)', line=2419)
W('21,2034', 0o53313, '', 'DXCH', 'T5LOC', line=2420)

W('21,2035', 0o44105, '', 'CS', 'OCT60000', 'SEE BITS 15,14 TO 01 TO INDICATE', line=2422)
W('21,2036', 0o70102, '', 'MASK', 'FLAGWRD6', '      T5 TAKEOVER BY RCSDAP', line=2423)
W('21,2037', 0o65002, '', 'AD', 'BIT14', line=2424)
W('21,2040', 0o54102, '', 'TS', 'FLAGWRD6', 'KILLS TVCEXEC AND ROLLDAP STARTS', line=2425)

W('21,2041', 0o00002, '', 'TC', 'Q', 'RETURN TO CALLER (TVCDAPOF OR RCSDAPUP)', line=2427)
