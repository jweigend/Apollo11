"""THROTTLE_CONTROL_ROUTINES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/THROTTLE_CONTROL_ROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 793-797 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('THROTTLE_CONTROL_ROUTINES', 'THROTTLE_CONTROL_ROUTINES.agc', 'Luminary099', pages='793-797')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     THROTTLE_CONTROL_ROUTINES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      HARTMUTH GUTSCHE <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        793-797
# Mod history:  2009-05-20 HG   Transcribed from page images.
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

# Page 793
#   BANK 31
#   SETLOC FTHROT
#   BANK
#   EBANK= PIF
#   COUNT* $$/THROT

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# HERE FC, DESIRED THRUST, AND FP, PRESENT THRUST, UNWEIGHTED, ARE COMPUTED.

W('31,2216', 0o31246, 'THROTTLE', 'CA', 'ABDELV', 'COMPUTE PRESENT ACCELERATION IN UNITS OF', line=37)
W('31,2217', 0o00006, '', 'EXTEND', '', '2(-4) M/CS/CS, SAVING SERVICER TROUBLE', line=38)
W('31,2220', 0o72417, '', 'MP', '/AF/CNST', line=39)
W('31,2221', 0o00006, '', 'EXTEND', line=40)
W('31,2222', 0o23607, '', 'QXCH', 'RTNHOLD', line=41)
W('31,2223', 0o02400, 'AFDUMP', 'TC', 'MASSMULT', line=42)
W('31,2224', 0o53470, '', 'DXCH', 'FP', 'FP = PRESENT THRUST', line=43)
W('31,2225', 0o00006, '', 'EXTEND', line=44)
W('31,2226', 0o31464, '', 'DCA', '/AFC/', line=45)
W('31,2227', 0o02400, '', 'TC', 'MASSMULT', line=46)
W('31,2230', 0o55615, '', 'TS', 'FC', 'FC = THRUST DESIRED BY GUIDANCE', line=47)
W('31,2231', 0o53466, '', 'DXCH', 'FCODD', 'FCODD = WHAT IT IS GOING TO GET', line=48)

# IF IT HAS BEEN LESS THAN 3 SECONDS SINCE THE LAST THROTTLING, AUGMENT FP USING THE FWEIGHT CALCULATED THEN.

W('31,2232', 0o41617, '', 'CS', 'TTHROT', 'THIS CODING ASSUMES A FLATOUT WITHIN', line=52)
W('31,2233', 0o60025, '', 'AD', 'TIME1', '  80 SECONDS BEFORE FIRST THROTTLE CALL', line=53)
W('31,2234', 0o74733, '', 'MASK', 'POSMAX', line=54)
W('31,2235', 0o40000, '', 'COM', line=55)
W('31,2236', 0o65002, '', 'AD', '3SECS', line=56)
W('31,2237', 0o00006, '', 'EXTEND', line=57)
W('31,2240', 0o62244, '', 'BZMF', 'WHERETO', 'BRANCH IF (TIME1-TTHROT +1) > 3 SECONDS', line=58)
W('31,2241', 0o00006, '', 'EXTEND', line=59)
W('31,2242', 0o31611, '', 'DCA', 'FWEIGHT', line=60)
W('31,2243', 0o21470, '', 'DAS', 'FP', line=61)

# THIS LOGIC DETERMINES THE THROTTLING IN THE REGION 10% - 94%.  THE MANUAL THROTTLE, NOMINALLY SET AT
# MINIMUM BY ASTRONAUT OR MISSION CONTROL PROGRAMS, PROVIDES THE LOWER BOUND.  A STOP IN THE THROTTLE HARDWARE
# PROVIDES THE UPPER.

W('31,2244', 0o35014, 'WHERETO', 'CA', 'EBANK5', 'INITIALIZE L*WCR*T AND H*GHCR*T FROM', line=67)
W('31,2245', 0o54003, '', 'TS', 'EBANK', '  PAD LOADED ERASABLES IN W-MATRIX', line=68)
# Page 794
#   EBANK= LOWCRIT
W('31,2246', 0o00006, '', 'EXTEND', line=71)
W('31,2247', 0o31507, '', 'DCA', 'LOWCRIT', line=72)
W('31,2250', 0o52131, '', 'DXCH', 'L*WCR*T', line=73)
W('31,2251', 0o35016, '', 'CA', 'EBANK7', line=74)
W('31,2252', 0o54003, '', 'TS', 'EBANK', line=75)
#   EBANK= PIF
W('31,2253', 0o44755, '', 'CS', 'ZERO', 'INITIALIZE PIFPSET', line=77)
W('31,2254', 0o55606, '', 'TS', 'PIFPSET', line=78)
W('31,2255', 0o40131, '', 'CS', 'H*GHCR*T', line=79)
W('31,2256', 0o61620, '', 'AD', 'FCOLD', line=80)
W('31,2257', 0o00006, '', 'EXTEND', line=81)
W('31,2260', 0o62272, '', 'BZMF', 'LOWFCOLD', 'BRANCH IF FCOLD < OR = HIGHCRIT', line=82)
W('31,2261', 0o40130, '', 'CS', 'L*WCR*T', line=83)
W('31,2262', 0o61465, '', 'AD', 'FCODD', line=84)
W('31,2263', 0o00006, '', 'EXTEND', line=85)
W('31,2264', 0o62267, '', 'BZMF', 'FCOMPSET', 'BRANCH IF FC < OR = LOWCRIT', line=86)
W('31,2265', 0o31467, '', 'CA', 'FP', 'SEE NOTE 1', line=87)
W('31,2266', 0o12277, '', 'TCF', 'FLATOUT1', line=88)

W('31,2267', 0o42002, 'FCOMPSET', 'CS', 'FMAXODD', 'SEE NOTE 2', line=90)
W('31,2270', 0o61467, '', 'AD', 'FP', line=91)
W('31,2271', 0o12301, '', 'TCF', 'FLATOUT2', line=92)

W('31,2272', 0o40131, 'LOWFCOLD', 'CS', 'H*GHCR*T', line=94)
W('31,2273', 0o61465, '', 'AD', 'FCODD', line=95)
W('31,2274', 0o00006, '', 'EXTEND', line=96)
W('31,2275', 0o62302, '', 'BZMF', 'DOPIF', 'BRANCH IF FC < OR = HIGHCRIT', line=97)

W('31,2276', 0o32003, '', 'CA', 'FMAXPOS', 'NO:  THROTTLE-UP', line=99)
W('31,2277', 0o53466, 'FLATOUT1', 'DXCH', 'FCODD', line=100)
W('31,2300', 0o34737, '', 'CA', 'FEXTRA', line=101)
W('31,2301', 0o55606, 'FLATOUT2', 'TS', 'PIFPSET', line=102)

# NOTE 1        FC IS SET EQUAL TO FP SO PIF WILL BE ZERO.  THIS IS DESIRABLE
# AS THERE IS ACTUALLY NO THROTTLE CHANGE.
#
# NOTE 2        HERE, SINCE WE ARE ABOUT TO RETURN TO THE THROTTLEABLE REGION
# (BELOW 55%) THE QUANTITY -(FMAXODD - FP) IS COMPUTED AND PUT
# INTO PIFPSET TO COMPENSATE FOR THE DIFFERENCE BETWEEN THE
# NUMBER OF BITS CORRESPONDING TO FULL THROTTLE (FMAXODD) AND THE
# NUMBER CORRESPONDING TO ACTUAL THRUST (FP).  THUS THE TOTAL
# THROTTLE COMMAND PIF = FC - FP - (FMAXODD - FP) = FC - FMAXODD.

W('31,2302', 0o03740, 'DOPIF', 'TC', 'FASTCHNG', line=114)
W('31,2303', 0o00006, '', 'EXTEND', line=115)
W('31,2304', 0o31466, '', 'DCA', 'FCODD', line=116)
W('31,2305', 0o55620, '', 'TS', 'FCOLD', line=117)
W('31,2306', 0o53613, '', 'DXCH', 'PIF', line=118)
W('31,2307', 0o00006, '', 'EXTEND', line=119)
# Page 795
W('31,2310', 0o41470, '', 'DCS', 'FP', line=121)
W('31,2311', 0o21613, '', 'DAS', 'PIF', 'PIF = FC - FP, NEVER EQUALS +0', line=122)

W('31,2312', 0o31612, 'DOIT', 'CA', 'PIF', line=124)
W('31,2313', 0o61606, '', 'AD', 'PIFPSET', 'ADD IN PIFPSET, WITHOUT CHANGING PIF', line=125)
W('31,2314', 0o55614, '', 'TS', 'PSEUDO55', line=126)
W('31,2315', 0o54055, '', 'TS', 'THRUST', line=127)
W('31,2316', 0o34750, '', 'CAF', 'BIT4', line=128)
W('31,2317', 0o00006, '', 'EXTEND', line=129)
W('31,2320', 0o05014, '', 'WOR', 'CHAN14', line=130)
W('31,2321', 0o30025, '', 'CA', 'TIME1', line=131)
W('31,2322', 0o55617, '', 'TS', 'TTHROT', line=132)

# SINCE /AF/ IS NOT AN INSTANTANEOUS ACCELERATION, BUT RATHER AN "AVERAGE" OF THE ACCELERATION LEVELS DURING
# THE PRECEEDING PIPA INTERVAL, AND SINCE FP IS COMPUTED DIRECTLY FROM /AF/, FP IN ORDER TO CORRESPOND TO THE
# ACTUAL THRUST LEVEL AT THE END OF THE INTERVAL MUST BE WEIGHTED BY
#
# PIF(PPROCESS + TL)     PIF /PIF/
# FWEIGHT = ------------------ + -------------
# PGUID           2 PGUID FRATE
#
# WHERE PPROCESS IS THE TIME BETWEEN PIPA READING AND THE START OF THROTTLING, PGUID IS THE GUIDANCE PERIOD, AND
# FRATE IS THE THROTTLING RATE (32 UNITS PER CENTISECOND).  PGUID IS EITHER 1 OR 2 SECONDS.  THE "TL" IN THE
# FIRST TERM REPRESENTS THE ENGINE'S RESPONSE LAG.  HERE FWEIGHT IS COMPUTED FOR USE NEXT PASS.

W('31,2323', 0o31762, '', 'CA', 'THISTPIP +1', 'INITIALIZE FWEIGHT COMP AS IF FOR P66', line=146)
W('31,2324', 0o54130, '', 'TS', 'BUF', line=147)

W('31,2325', 0o41011, '', 'CS', 'MODREG', 'ARE WE IN FACT IN P66?', line=149)
W('31,2326', 0o62501, '', 'AD', 'DEC66', line=150)
W('31,2327', 0o00006, '', 'EXTEND', line=151)
W('31,2330', 0o12335, '', 'BZF', 'FWCOMP', 'YES', line=152)

W('31,2331', 0o31235, '', 'CA', 'PIPTIME +1', 'NO:  INITIALIZE FOR TWO SECOND PERIOD', line=154)
W('31,2332', 0o54130, '', 'TS', 'BUF', line=155)
W('31,2333', 0o35003, '', 'CAF', '4SECS', line=156)
W('31,2334', 0o12336, '', 'TCF', 'FWCOMP +1', line=157)

W('31,2335', 0o35000, 'FWCOMP', 'CAF', '2SECS', line=159)
W('31,2336', 0o54002, '', 'TS', 'Q', line=160)
W('31,2337', 0o00006, '', 'EXTEND', line=161)
W('31,2340', 0o74746, '', 'MP', 'BIT6', line=162)
W('31,2341', 0o22131, '', 'LXCH', 'BUF +1', line=163)
W('31,2342', 0o40130, '', 'CS', 'BUF', 'TIME OF LAST PIPA READING.', line=164)
W('31,2343', 0o60025, '', 'AD', 'TIME1', line=165)
W('31,2344', 0o62004, '', 'AD', 'THROTLAG', 'COMPENSATE FOR ENGINE RESPONSE LAG', line=166)
W('31,2345', 0o74357, '', 'MASK', 'LOW8', 'MAKE SURE SMALL AND POSITIVE', line=167)
W('31,2346', 0o22007, '', 'ZL', line=168)
W('31,2347', 0o00006, '', 'EXTEND', line=169)
# Page 796
W('31,2350', 0o10002, '', 'DV', 'Q', line=171)
W('31,2351', 0o00006, '', 'EXTEND', line=172)
W('31,2352', 0o71612, '', 'MP', 'PIF', line=173)
W('31,2353', 0o60000, '', 'DOUBLE', line=174)
W('31,2354', 0o53611, '', 'DXCH', 'FWEIGHT', line=175)
W('31,2355', 0o11612, '', 'CCS', 'PIF', line=176)
W('31,2356', 0o64753, '', 'AD', 'ONE', line=177)
W('31,2357', 0o12361, '', 'TCF', '+2', line=178)
W('31,2360', 0o64753, '', 'AD', 'ONE', line=179)
W('31,2361', 0o00006, '', 'EXTEND', line=180)
W('31,2362', 0o71612, '', 'MP', 'PIF', line=181)
W('31,2363', 0o00006, '', 'EXTEND', line=182)
W('31,2364', 0o10131, '', 'DV', 'BUF +1', line=183)
W('31,2365', 0o22007, '', 'ZL', line=184)
W('31,2366', 0o21611, '', 'DAS', 'FWEIGHT', line=185)

W('31,2367', 0o01607, 'THDUMP', 'TC', 'RTNHOLD', line=187)

# FLATOUT THROTTLES UP THE DESCENT ENGINE, AND IS CALLED AS A BASIC SUBROUTINE.

W('31,2370', 0o34737, 'FLATOUT', 'CAF', 'BIT13', '4096 PULSES', line=191)
W('31,2371', 0o55606, 'WHATOUT', 'TS', 'PIFPSET', 'USE PIFPSET SO FWEIGHT WILL BE ZERO', line=192)
W('31,2372', 0o44755, '', 'CS', 'ZERO', line=193)
W('31,2373', 0o55620, '', 'TS', 'FCOLD', line=194)
W('31,2374', 0o55612, '', 'TS', 'PIF', line=195)
W('31,2375', 0o00006, '', 'EXTEND', line=196)
W('31,2376', 0o23607, '', 'QXCH', 'RTNHOLD', line=197)
W('31,2377', 0o12312, '', 'TCF', 'DOIT', line=198)

# MASSMULT SCALES ACCELERATION, ARRIVING IN A AND L IN UNITS OF 2(-4) M/CS/CS, TO FORCE IN PULSE UNITS.

W('31,2400', 0o00006, 'MASSMULT', 'EXTEND', line=202)
W('31,2401', 0o22130, '', 'QXCH', 'BUF', line=203)
W('31,2402', 0o52155, '', 'DXCH', 'MPAC', line=204)
W('31,2403', 0o07103, '', 'TC', 'DMP', line=205)
W('31,2404', 0o01244, '', 'ADRES', 'MASS', kind='data', line=206)
W('31,2405', 0o07103, '', 'TC', 'DMP', 'LEAVES PROPERLY SCALED FORCE IN MPAC', line=207)
W('31,2406', 0o02005, '', 'ADRES', 'SCALEFAC', kind='data', line=208)
W('31,2407', 0o07257, '', 'TC', 'TPAGREE', line=209)
W('31,2410', 0o30154, '', 'CA', 'MPAC', line=210)
W('31,2411', 0o00006, '', 'EXTEND', line=211)
W('31,2412', 0o12415, '', 'BZF', '+3', line=212)
W('31,2413', 0o34733, '', 'CAF', 'POSMAX', line=213)
W('31,2414', 0o00130, '', 'TC', 'BUF', line=214)
W('31,2415', 0o52156, '', 'DXCH', 'MPAC +1', line=215)
W('31,2416', 0o00130, '', 'TC', 'BUF', line=216)
# Page 797
# CONSTANTS:-

S('FEXTRA', 'equals', 0o4737, line=220)  # FEXT +5.13309020E+ 4

W('31,2417', 0o04143, '/AF/CNST', 'DEC', '.13107', kind='data', line=222)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
