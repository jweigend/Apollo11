"""TPI_SEARCH.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/TPI_SEARCH.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 551-561 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TPI_SEARCH', 'TPI_SEARCH.agc', 'Comanche055', pages='551-561')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TPI_SEARCH.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        551-561
# Mod history:  2009-05-15 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
# 2009-05-20 RSB  Corrections:  On p. 551, "SETLOC P17S" -> P17S1.
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

# Page 551
# TPI SEARCH

# PROGRAM DESCRIPTION S17.1 AND S17.2

# FUNCTIONAL DESCRIPTION

# THE TPI SEARCH ROUTINE DETERMINES THE MINIMUM TOTAL VELOCITY TRANSFER TRAJECTORY FROM A GIVEN TPI
# MANEUVER TIME WITHIN THE CONSTRAINT OF A SAFE PERICENTER.  THIS VELOCITY IS THE SUM OF THE IMPULSIVE VELOCITIES
# FOR THE TPI AND TPF MANEUVERS.
# THE S17.1 ROUTINE EXTRAPOLATES THE STATE VECTORS OF BOTH VEHICLES TO THE TPI TIME AND COMPUTES THE
# RELATIVE PHASE ANGLE BETWEEN THE VEHICLES, THE ALTITUDE DIFFERENCE(I.E. THE MAGNITUDE DIFFERENCE OF THE
# POSITION VECTORS) AND SELECTS A SEARCH SECTOR BASED ON THE SIGN OF THE ALTITUDE DIFFERENCE.
# THE S17.2 ROUTINE FURTHER DEFINES THE SEARCH SECTOR BY COMPUTING ANGULAR LIMITS AND USES THE TIME THETA
# SUBROUTINE TO COMPUTE THE SEARCH START AND END TIMES.  THE SEARCH IS THEN MADE IN AN ITERATIVE LOOP USING THE
# LAMBERT SUBROUTINE TO COMPUTE THE VELOCITIES REQUIRED AT TPI TIME AND AT TPF TIME.  EXIT FROM THE SEARCH LOOP
# IS MADE WHEN SOLUTION CRITERIA ARE MET (NORMAL EXIT) OR AS SOON AS IT IS EVIDENT THAT NO SOLUTION EXISTS IN
# THE SECTOR SEARCHED.

# CALLING SEQUENCE

# BOTH ROUTINES ARE CALLED IN INTERPRETIVE CODE AND RETURN VIA QPRET.  S17.1 HAS ONLY A NORMAL EXIT.
# S17.2 RETURNS VIA QPRET FOR NORMAL EXIT AND TO ALARUMS FOR ERROR EXIT.
# SUBROUTINES CALLED
#
# CSMCONIC
# LEMCONIC
# TIMETHET
# INITVEL

#   BANK 36
#   SETLOC P17S1
#   BANK

#   COUNT 36/TPI

#   EBANK= RACT3

# **** TEMPORARY ****

W('35,3123', 0o00004, 'HPE', '2DEC', '157420.0 B-29', "EARTH'S MIN. PERICENTER ALTITUDE 85 N.M.", kind='data', line=71)
W('35,3124', 0o31566, kind='data', line=71)

W('35,3125', 0o00000, 'HPL', '2DEC', '10668.0213 B-29', 'MOON:S MIN. PERICENTER ALTITUDE 35000FT', kind='data', line=73)
W('35,3126', 0o12326, kind='data', line=73)

W('35,3127', 0o00002, 'CDSEC', '2DEC', '40000', kind='data', line=75)
W('35,3130', 0o16100, kind='data', line=75)

W('35,3131', 0o00000, 'CLSEC', '2DEC', '15000', kind='data', line=77)
W('35,3132', 0o35230, kind='data', line=77)

W('35,3133', 0o12137, 'PIINVERS', '2DEC', '.3183098862', kind='data', line=79)
W('35,3134', 0o06033, kind='data', line=79)

W('35,3135', 0o06161, 'SEC1THET', '2DEC', '.1944444444', kind='data', line=81)
W('35,3136', 0o30707, kind='data', line=81)

# Page 552
W('35,3137', 0o35252, 'SEC2THET', '2DEC', '.9166666667', kind='data', line=84)
W('35,3140', 0o25253, kind='data', line=84)

W('35,3141', 0o67777, 'MANYFEET', '2DEC', '-1.0 B-2', kind='data', line=86)
W('35,3142', 0o77777, kind='data', line=86)

W('35,3143', 0o00000, 'LIMVEL', '2DEC', '.6096 E-2 B-7', '2FPS', kind='data', line=88)
W('35,3144', 0o30760, kind='data', line=88)

W('35,3145', 0o00000, 'DFTMOON', '2DEC', '.1524 E3 B-29', '500 FEET', kind='data', line=90)
W('35,3146', 0o00114, kind='data', line=90)

W('35,3147', 0o00040, 'DP-.002', '2DEC', '0.002', kind='data', line=92)
W('35,3150', 0o30447, kind='data', line=92)

#   SETLOC P17S
#   BANK
W('36,2012', 0o71220, 'S17.1', 'STQ', 'DLOAD', kind='interp', line=96)
W('36,2013', 0o01340, '', '', 'NORMEX', kind='operand', line=97)
W('36,2014', 0o03663, '', '', 'TTPI', kind='operand', line=98)
W('36,2015', 0o34041, '', 'STCALL', 'TDEC1', 'ADVANCE PASSIVE VEHICLE TO TPI', kind='interp', line=99)
W('36,2016', 0o27126, '', '', 'LEMCONIC', kind='operand', line=100)
W('36,2017', 0o77624, '', 'CALL', kind='interp', line=101)
W('36,2020', 0o45233, '', '', 'LEMSTORE', kind='operand', line=102)
W('36,2021', 0o77745, '', 'DLOAD', kind='interp', line=103)
W('36,2022', 0o03663, '', '', 'TTPI', kind='operand', line=104)
W('36,2023', 0o34041, '', 'STCALL', 'TDEC1', 'ADVANCE ACTIVE VEHICLE TO TPI', kind='interp', line=105)
W('36,2024', 0o27114, '', '', 'CSMCONIC', kind='operand', line=106)
W('36,2025', 0o77624, '', 'CALL', kind='interp', line=107)
W('36,2026', 0o45243, '', '', 'CSMSTORE', kind='operand', line=108)
W('36,2027', 0o77775, '', 'VLOAD', kind='interp', line=109)
W('36,2030', 0o03540, '', '', 'RACT3', kind='operand', line=110)
W('36,2031', 0o63246, '', 'ABVAL', 'PDVL', '/RA/ 0D                       PL 2D', kind='interp', line=111)
W('36,2032', 0o03554, '', '', 'RPASS3', kind='operand', line=112)
W('36,2033', 0o65256, '', 'UNIT', 'PDDL', 'UNIT RP 0D                    PL 6D', kind='interp', line=113)
W('36,2034', 0o43021, '', 'BDSU', 'SET', kind='interp', line=114)
W('36,2035', 0o00045, '', '', '36D', '/RP/ -/RA/', kind='operand', line=115)
W('36,2036', 0o00076, '', '', 'KFLAG', 'OFF = +', kind='operand', line=116)
W('36,2037', 0o43040, '', 'BMN', 'CLEAR', kind='interp', line=117)
W('36,2040', 0o74042, '', '', '+2', kind='operand', line=118)
W('36,2041', 0o00276, '', '', 'KFLAG', 'ON = -', kind='operand', line=119)
W('36,2042', 0o27754, '', 'STOVL', 'DELHITE', kind='interp', line=120)
W('36,2043', 0o00001, '', '', '0D', kind='operand', line=121)
W('36,2044', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=122)
W('36,2045', 0o03562, '', '', 'VPASS3', kind='operand', line=123)
W('36,2046', 0o27646, '', 'STOVL', 'E2', 'ALMOST IT SAVE FOR 17.2', kind='interp', line=124)
W('36,2047', 0o03540, '', '', 'RACT3', kind='operand', line=125)
W('36,2050', 0o46206, '', 'PUSH', 'VPROJ', kind='interp', line=126)
W('36,2051', 0o03646, '', '', 'E2', kind='operand', line=127)
W('36,2052', 0o51352, '', 'VSL2', 'BVSU', 'RPA', kind='interp', line=128)
W('36,2053', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=129)
W('36,2054', 0o00001, '', '', '0D', kind='operand', line=130)
W('36,2055', 0o65552, '', 'SL1', 'ACOS', kind='interp', line=131)
W('36,2056', 0o77715, '', 'PDVL', kind='interp', line=132)
W('36,2057', 0o50235, '', 'VXV', 'DOT', kind='interp', line=133)
# Page 553
W('36,2060', 0o03540, '', '', 'RACT3', kind='operand', line=135)
W('36,2061', 0o03646, '', '', 'E2', kind='operand', line=136)
W('36,2062', 0o75325, '', 'PDDL', 'SIGN', kind='interp', line=137)
W('36,2063', 0o77626, '', 'STADR', kind='interp', line=138)
W('36,2064', 0o61160, '', 'STODL', 'THETZERO', 'CENTRAL ANGLE', kind='interp', line=139)
W('36,2065', 0o00047, '', '', 'X1', kind='operand', line=140)
W('36,2066', 0o37746, '', 'STCALL', 'XRS', 'SAVE INDICES FOR FURTHER USE', kind='interp', line=141)
W('36,2067', 0o01340, '', '', 'NORMEX', '  += ACTIVE AHEAD  -= ACTIVE BEHIND', kind='operand', line=142)
W('36,2070', 0o77220, 'S17.2', 'STQ', 'VLOAD', 'COMPUTE SEARCH SECTOR LIMITS', kind='interp', line=143)
W('36,2071', 0o03657, '', '', 'QTEMP', kind='operand', line=144)
W('36,2072', 0o03540, '', '', 'RACT3', kind='operand', line=145)
W('36,2073', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=146)
W('36,2074', 0o03646, '', '', 'E2', kind='operand', line=147)
W('36,2075', 0o75446, '', 'ABS', 'SQRT', kind='interp', line=148)
W('36,2076', 0o43352, '', 'SL1', 'DAD', kind='interp', line=149)
W('36,2077', 0o33150, '', '', 'DP-.002', 'ADD .002 RADIANS TO IT', kind='operand', line=150)
W('36,2100', 0o57414, '', 'BON', 'DCOMP', 'GIVES CORRECT SINE, COSINE MUST BE', kind='interp', line=151)
W('36,2101', 0o00316, '', '', 'KFLAG', 'COMP. ADD .5 FOR ANGLE', kind='operand', line=152)
W('36,2102', 0o74103, '', '', '+1', kind='operand', line=153)
# PHI(0)=180-(-(THETAZERO +K5IT)), PHI(I)=180-(-THETAZERO+K2IT))
# SIN(180-ALPHA)=SIN(ALPHA) ETC
W('36,2103', 0o40205, '', 'DMP', 'SETPD', kind='interp', line=156)
W('36,2104', 0o33134, '', '', 'PIINVERS', 'REVOLUTIONARY HERES TWO IT', kind='operand', line=157)
W('36,2105', 0o00001, '', '', '0D', kind='operand', line=158)
W('36,2106', 0o45206, '', 'PUSH', 'DSU', kind='interp', line=159)
W('36,2107', 0o02617, '', '', 'THETZERO', kind='operand', line=160)
W('36,2110', 0o02611, '', 'STORE', 'IT', 'PHI(I) , -(THETZERO + K2IT)', kind='interp', line=161)
W('36,2111', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=162)
W('36,2112', 0o43342, '', 'SR1', 'DAD', kind='interp', line=163)
W('36,2113', 0o41415, '', 'DAD', 'PUSH', 'PHI(0) , -(THETZERO + K5IT)', kind='interp', line=164)
W('36,2114', 0o43156, '', 'SIN', 'SET', kind='interp', line=165)
W('36,2115', 0o03466, '', '', 'RVSW', kind='operand', line=166)
W('36,2116', 0o16732, '', 'STODL', 'SNTH', kind='interp', line=167)
W('36,2117', 0o50146, '', 'COS', 'BMN', kind='interp', line=168)
W('36,2120', 0o74122, '', '', '+2', kind='operand', line=169)
W('36,2121', 0o77676, '', 'DCOMP', kind='interp', line=170)
W('36,2122', 0o16734, '', 'STODL', 'CSTH', kind='interp', line=171)
W('36,2123', 0o03746, '', '', 'XRS', kind='operand', line=172)
W('36,2124', 0o24047, '', 'STOVL', 'X1', kind='interp', line=173)
W('36,2125', 0o03554, '', '', 'RPASS3', kind='operand', line=174)
W('36,2126', 0o77657, '', 'VSR*', kind='interp', line=175)
W('36,2127', 0o57176, '', '', '0,2', kind='operand', line=176)
W('36,2130', 0o26657, '', 'STOVL', 'RVEC', kind='interp', line=177)
W('36,2131', 0o03562, '', '', 'VPASS3', kind='operand', line=178)
W('36,2132', 0o77657, '', 'VSR*', kind='interp', line=179)
W('36,2133', 0o57176, '', '', '0,2', kind='operand', line=180)
W('36,2134', 0o36746, '', 'STCALL', 'VVEC', kind='interp', line=181)
W('36,2135', 0o24744, '', '', 'TIMETHET', kind='operand', line=182)
W('36,2136', 0o77745, '', 'DLOAD', '', 'SAVE START TIME AND GET END TIME', kind='interp', line=183)
W('36,2137', 0o00037, '', '', 'T', kind='operand', line=184)
# Page 554
W('36,2140', 0o03752, '', 'STORE', 'TF', kind='interp', line=186)
W('36,2141', 0o16627, '', 'STODL', 'TFO', kind='interp', line=187)
W('36,2142', 0o02611, '', '', 'IT', kind='operand', line=188)
W('36,2143', 0o73406, '', 'PUSH', 'SIN', kind='interp', line=189)
W('36,2144', 0o16732, '', 'STODL', 'SNTH', kind='interp', line=190)
W('36,2145', 0o50146, '', 'COS', 'BMN', kind='interp', line=191)
W('36,2146', 0o74150, '', '', '+2', kind='operand', line=192)
W('36,2147', 0o77676, '', 'DCOMP', kind='interp', line=193)
W('36,2150', 0o02734, '', 'STORE', 'CSTH', kind='interp', line=194)
W('36,2151', 0o45150, '', 'LXA,1', 'CALL', kind='interp', line=195)
W('36,2152', 0o03745, '', '', 'XRS', kind='operand', line=196)
W('36,2153', 0o24744, '', '', 'TIMETHET', kind='operand', line=197)
# INITIALIZE LOOP
W('36,2154', 0o43145, '', 'DLOAD', 'CLEAR', kind='interp', line=199)
W('36,2155', 0o00037, '', '', 'T', kind='operand', line=200)
W('36,2156', 0o03661, '', '', 'ITSWICH', kind='operand', line=201)
W('36,2157', 0o16621, '', 'STODL', 'TFI', 'SAVE TIME FOR LOOP TEST', kind='interp', line=202)
W('36,2160', 0o15343, '', '', 'DPPOSMAX', kind='operand', line=203)
W('36,2161', 0o16623, '', 'STODL', 'DELVEE', kind='interp', line=204)
W('36,2162', 0o33142, '', '', 'MANYFEET', kind='operand', line=205)
W('36,2163', 0o16625, '', 'STODL', 'HP', kind='interp', line=206)
W('36,2164', 0o33136, '', '', 'SEC1THET', '70 DEGREES', kind='operand', line=207)
W('36,2165', 0o71214, '', 'BON', 'DLOAD', kind='interp', line=208)
W('36,2166', 0o00316, '', '', 'KFLAG', kind='operand', line=209)
W('36,2167', 0o74171, '', '', '+2', kind='operand', line=210)
W('36,2170', 0o33140, '', '', 'SEC2THET', '330 DEGREES', kind='operand', line=211)
W('36,2171', 0o37750, '', 'STCALL', 'THETL', kind='interp', line=212)
W('36,2172', 0o74214, '', '', 'CONCAUL', kind='operand', line=213)
W('36,2173', 0o70545, 'BIS', 'DLOAD', 'SR1', kind='interp', line=214)
W('36,2174', 0o02734, '', '', 'CSTH', kind='operand', line=215)
W('36,2175', 0o14021, '', 'STODL', 'COSTH', kind='interp', line=216)
W('36,2176', 0o02732, '', '', 'SNTH', kind='operand', line=217)
W('36,2177', 0o77742, '', 'SR1', kind='interp', line=218)
W('36,2200', 0o34023, '', 'STCALL', 'SINTH', 'GET 4 QUADRANT THETA', kind='interp', line=219)
W('36,2201', 0o47256, '', '', 'ARCTRIG', kind='operand', line=220)
W('36,2202', 0o43244, '', 'BPL', 'DAD', kind='interp', line=221)
W('36,2203', 0o74205, '', '', '+2', kind='operand', line=222)
W('36,2204', 0o15343, '', '', 'DPPOSMAX', 'PUT THETA BETWEEN 0,1', kind='operand', line=223)
W('36,2205', 0o65221, '', 'BDSU', 'PDDL', kind='interp', line=224)
W('36,2206', 0o03750, '', '', 'THETL', kind='operand', line=225)
W('36,2207', 0o03752, '', '', 'TF', kind='operand', line=226)
W('36,2210', 0o75225, '', 'DSU', 'SIGN', 'FAST TIMES', kind='interp', line=227)
W('36,2211', 0o02621, '', '', 'TFI', kind='operand', line=228)
W('36,2212', 0o77640, '', 'BMN', kind='interp', line=229)
W('36,2213', 0o74416, '', '', 'RNGETEST', 'TIME MUST HAVE A STOP', kind='operand', line=230)
# ADVANCE PASSIVE FOR TARGET VECTOR
W('36,2214', 0o77745, 'CONCAUL', 'DLOAD', kind='interp', line=232)
W('36,2215', 0o03663, '', '', 'TTPI', kind='operand', line=233)
W('36,2216', 0o43015, '', 'DAD', 'BON', kind='interp', line=234)
W('36,2217', 0o03752, '', '', 'TF', kind='operand', line=235)
# Page 555
W('36,2220', 0o01312, '', '', 'AVFLAG', kind='operand', line=237)
W('36,2221', 0o74226, '', '', 'ADVCSM', kind='operand', line=238)
W('36,2222', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=239)
W('36,2223', 0o27126, '', '', 'LEMCONIC', kind='operand', line=240)
W('36,2224', 0o77650, '', 'GOTO', kind='interp', line=241)
W('36,2225', 0o74230, '', '', 'JUNCT3', kind='operand', line=242)
W('36,2226', 0o34041, 'ADVCSM', 'STCALL', 'TDEC1', kind='interp', line=243)
W('36,2227', 0o27114, '', '', 'CSMCONIC', kind='operand', line=244)
# SAVE BACK VALUES OF HP AND DELVEE
W('36,2230', 0o77775, 'JUNCT3', 'VLOAD', kind='interp', line=246)
W('36,2231', 0o00007, '', '', 'VATT', kind='operand', line=247)
W('36,2232', 0o27640, '', 'STOVL', 'VPASS4', kind='interp', line=248)
W('36,2233', 0o00001, '', '', 'RATT', kind='operand', line=249)
W('36,2234', 0o03632, '', 'STORE', 'RPASS4', kind='interp', line=250)
W('36,2235', 0o17415, '', 'STODL', 'RTARG', kind='interp', line=251)
W('36,2236', 0o03752, '', '', 'TF', kind='operand', line=252)
W('36,2237', 0o17423, '', 'STODL', 'DELLT4', kind='interp', line=253)
W('36,2240', 0o02625, '', '', 'HP', kind='operand', line=254)
W('36,2241', 0o16631, '', 'STODL', 'HPO', kind='interp', line=255)
W('36,2242', 0o02623, '', '', 'DELVEE', kind='operand', line=256)
W('36,2243', 0o16633, '', 'STODL', 'DELVEO', kind='interp', line=257)
# PREPARE FOR LAMBERT
W('36,2244', 0o03663, '', '', 'TTPI', kind='operand', line=259)
W('36,2245', 0o17503, '', 'STODL', 'INTIME', kind='interp', line=260)
W('36,2246', 0o03746, '', '', 'XRS', kind='operand', line=261)
W('36,2247', 0o17746, '', 'STODL', 'RTX1', kind='interp', line=262)
W('36,2250', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=263)
W('36,2251', 0o65201, '', 'SETPD', 'PDDL', kind='interp', line=264)
W('36,2252', 0o00001, '', '', '0D', kind='operand', line=265)
W('36,2253', 0o33122, '', '', 'EPSFOUR', kind='operand', line=266)
W('36,2254', 0o77715, '', 'PDVL', kind='interp', line=267)
W('36,2255', 0o03540, '', '', 'RACT3', kind='operand', line=268)
W('36,2256', 0o27570, '', 'STOVL', 'RINIT', kind='interp', line=269)
W('36,2257', 0o03546, '', '', 'VACT3', kind='operand', line=270)
W('36,2260', 0o37576, '', 'STCALL', 'VINIT', kind='interp', line=271)
W('36,2261', 0o22000, '', '', 'INITVEL', kind='operand', line=272)
# COMPUTE H ET CETERA
W('36,2262', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=274)
W('36,2263', 0o03620, '', '', 'VTPRIME', kind='operand', line=275)
W('36,2264', 0o03640, '', '', 'VPASS4', kind='operand', line=276)
W('36,2265', 0o41446, '', 'ABVAL', 'PUSH', kind='interp', line=277)
W('36,2266', 0o26637, '', 'STOVL', 'RELDELV', '/V2-VP(TPI+TF)/', kind='interp', line=278)
W('36,2267', 0o03646, '', '', 'DELVEET3', 'V1-VA', kind='operand', line=279)
W('36,2270', 0o77646, '', 'ABVAL', '', '/V1-VA/', kind='interp', line=280)
W('36,2271', 0o02635, '', 'STORE', 'MAGVTPI', kind='interp', line=281)
W('36,2272', 0o45415, '', 'DAD', 'STADR', kind='interp', line=282)
W('36,2273', 0o61154, '', 'STODL', 'DELVEE', kind='interp', line=283)
W('36,2274', 0o03746, '', '', 'XRS', kind='operand', line=284)
W('36,2275', 0o24047, '', 'STOVL', 'X1', kind='interp', line=285)
W('36,2276', 0o03612, '', '', 'VIPRIME', kind='operand', line=286)
# Page 556
W('36,2277', 0o77657, '', 'VSR*', kind='interp', line=288)
W('36,2300', 0o57176, '', '', '0,2', kind='operand', line=289)
W('36,2301', 0o26746, '', 'STOVL', 'VVEC', kind='interp', line=290)
W('36,2302', 0o03540, '', '', 'RACT3', kind='operand', line=291)
W('36,2303', 0o77657, '', 'VSR*', kind='interp', line=292)
W('36,2304', 0o57176, '', '', '0,2', kind='operand', line=293)
W('36,2305', 0o36657, '', 'STCALL', 'RVEC', kind='interp', line=294)
W('36,2306', 0o45163, '', '', 'PERIAPO', kind='operand', line=295)
W('36,2307', 0o71354, '', 'LXA,2', 'DLOAD', kind='interp', line=296)
W('36,2310', 0o03746, '', '', 'XRS +1', kind='operand', line=297)
W('36,2311', 0o77657, '', 'SL*', kind='interp', line=298)
W('36,2312', 0o57576, '', '', '0,2', kind='operand', line=299)
W('36,2313', 0o02625, '', 'STORE', 'HP', kind='interp', line=300)
# ITSWICH DENOTES INTERPOLATION--SOLUTION ACCEPTANCE IS FORCED
W('36,2314', 0o71214, '', 'BON', 'DLOAD', kind='interp', line=302)
W('36,2315', 0o03701, '', '', 'ITSWICH', kind='operand', line=303)
W('36,2316', 0o74427, '', '', 'ENDEN', kind='operand', line=304)
W('36,2317', 0o02321, '', '', 'HPERMIN', kind='operand', line=305)
W('36,2320', 0o50025, '', 'DSU', 'BMN', kind='interp', line=306)
W('36,2321', 0o02625, '', '', 'HP', kind='operand', line=307)
W('36,2322', 0o74365, '', '', 'HALFSAFE', kind='operand', line=308)
W('36,2323', 0o45325, '', 'PDDL', 'DSU', 'WAS PERICENTER ALT SAFE', kind='interp', line=309)
W('36,2324', 0o02321, '', '', 'HPERMIN', kind='operand', line=310)
W('36,2325', 0o02631, '', '', 'HPO', kind='operand', line=311)
W('36,2326', 0o45240, '', 'BMN', 'DSU', '(HPLIM-HPO)-(HPLIM-HP)=HP-HPO', kind='interp', line=312)
W('36,2327', 0o74344, '', '', 'INTERP', 'SOLUTION AT HAND', kind='operand', line=313)
W('36,2330', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=314)
W('36,2331', 0o73254, '', '', 'ALARUMS', "IT'S GETTING WORSE - SOUND THE ALARM", kind='operand', line=315)
W('36,2332', 0o33130, '', '', 'CDSEC', kind='operand', line=316)
W('36,2333', 0o57414, 'JUNCT1', 'BOFF', 'DCOMP', 'OFF IS PLUS ON IS MINUS', kind='interp', line=317)
W('36,2334', 0o00356, '', '', 'KFLAG', kind='operand', line=318)
W('36,2335', 0o74336, '', '', '+1', kind='operand', line=319)
W('36,2336', 0o03744, '', 'STORE', 'DELTEE', kind='interp', line=320)
W('36,2337', 0o43345, 'JUNCT2', 'DLOAD', 'DAD', kind='interp', line=321)
W('36,2340', 0o03744, '', '', 'DELTEE', kind='operand', line=322)
W('36,2341', 0o03752, '', '', 'TF', kind='operand', line=323)
W('36,2342', 0o37752, '', 'STCALL', 'TF', kind='interp', line=324)
W('36,2343', 0o74173, '', '', 'BIS', 'RECYCLE', kind='operand', line=325)
W('36,2344', 0o45214, 'INTERP', 'SET', 'DSU', 'HP-HPO', kind='interp', line=326)
W('36,2345', 0o03461, '', '', 'ITSWICH', kind='operand', line=327)
W('36,2346', 0o65301, '', 'NORM', 'PDDL', kind='interp', line=328)
W('36,2347', 0o00047, '', '', 'X1', kind='operand', line=329)
W('36,2350', 0o33146, '', '', 'DFTMOON', kind='operand', line=330)
W('36,2351', 0o45215, '', 'DAD', 'DSU', kind='interp', line=331)
W('36,2352', 0o02321, '', '', 'HPERMIN', kind='operand', line=332)
W('36,2353', 0o02625, '', '', 'HP', kind='operand', line=333)
W('36,2354', 0o70501, '', 'NORM', 'SR1', kind='interp', line=334)
W('36,2355', 0o00050, '', '', 'X2', kind='operand', line=335)
W('36,2356', 0o56264, '', 'XSU,2', 'DDV', kind='interp', line=336)
W('36,2357', 0o00046, '', '', 'X1', kind='operand', line=337)
# Page 557
W('36,2360', 0o53605, '', 'DMP', 'SR*', kind='interp', line=339)
W('36,2361', 0o03744, '', '', 'DELTEE', kind='operand', line=340)
W('36,2362', 0o57177, '', '', '0 -1,2', kind='operand', line=341)
W('36,2363', 0o37744, '', 'STCALL', 'DELTEE', kind='interp', line=342)
W('36,2364', 0o74337, '', '', 'JUNCT2', kind='operand', line=343)
W('36,2365', 0o45325, 'HALFSAFE', 'PDDL', 'DSU', 'SAVE HP-HPLIM FOR POSSIBLE', kind='interp', line=344)
W('36,2366', 0o02623, '', '', 'DELVEE', kind='operand', line=345)
W('36,2367', 0o02633, '', '', 'DELVEO', 'SAVE THIS TOO', kind='operand', line=346)
W('36,2370', 0o51406, '', 'PUSH', 'ABS', kind='interp', line=347)
W('36,2371', 0o50025, '', 'DSU', 'BMN', kind='interp', line=348)
W('36,2372', 0o33144, '', '', 'LIMVEL', '2 FT PS', kind='operand', line=349)
W('36,2373', 0o74427, '', '', 'ENDEN', kind='operand', line=350)
W('36,2374', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=351)
W('36,2375', 0o02321, '', '', 'HPERMIN', kind='operand', line=352)
W('36,2376', 0o02631, '', '', 'HPO', kind='operand', line=353)
W('36,2377', 0o77725, '', 'PDDL', kind='interp', line=354)
W('36,2400', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=355)
W('36,2401', 0o74410, '', '', 'LRGRDVO', kind='operand', line=356)
W('36,2402', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=357)
W('36,2403', 0o74344, '', '', 'INTERP', kind='operand', line=358)
W('36,2404', 0o03744, '', '', 'DELTEE', kind='operand', line=359)
W('36,2405', 0o57542, '', 'SR1', 'DCOMP', kind='interp', line=360)
W('36,2406', 0o37744, '', 'STCALL', 'DELTEE', kind='interp', line=361)
W('36,2407', 0o74337, '', '', 'JUNCT2', kind='operand', line=362)
W('36,2410', 0o77745, 'LRGRDVO', 'DLOAD', kind='interp', line=363)
W('36,2411', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=364)
W('36,2412', 0o74337, '', '', 'JUNCT2', kind='operand', line=365)
W('36,2413', 0o33132, '', '', 'CLSEC', kind='operand', line=366)
W('36,2414', 0o77650, '', 'GOTO', kind='interp', line=367)
W('36,2415', 0o74333, '', '', 'JUNCT1', kind='operand', line=368)
# TIME RAN OUT ASSUME SOLUTION IF SAVE PERICENTER
W('36,2416', 0o45345, 'RNGETEST', 'DLOAD', 'DSU', kind='interp', line=370)
W('36,2417', 0o02625, '', '', 'HP', kind='operand', line=371)
W('36,2420', 0o02321, '', '', 'HPERMIN', kind='operand', line=372)
W('36,2421', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=373)
W('36,2422', 0o73254, '', '', 'ALARUMS', kind='operand', line=374)
W('36,2423', 0o03752, '', '', 'TF', kind='operand', line=375)
W('36,2424', 0o77625, '', 'DSU', kind='interp', line=376)
W('36,2425', 0o03744, '', '', 'DELTEE', kind='operand', line=377)
W('36,2426', 0o03752, '', 'STORE', 'TF', 'TIME OF SOLUTION', kind='interp', line=378)
W('36,2427', 0o77775, 'ENDEN', 'VLOAD', kind='interp', line=379)
W('36,2430', 0o03620, '', '', 'VTPRIME', kind='operand', line=380)
W('36,2431', 0o65241, '', 'DOT', 'PDDL', 'SG2 WITH MAGNITUDE', kind='interp', line=381)
W('36,2432', 0o03632, '', '', 'RPASS4', kind='operand', line=382)
W('36,2433', 0o02637, '', '', 'RELDELV', kind='operand', line=383)
W('36,2434', 0o45565, '', 'SIGN', 'STADR', 'NOW SIGN(RELDELV)=SIGN(SG2)', kind='interp', line=384)
W('36,2435', 0o41140, '', 'STCALL', 'RELDELV', kind='interp', line=385)
W('36,2436', 0o16441, '', '', 'TRANSANG', 'COMPUTE OMEGA T , CENTRAL ANGLE', kind='operand', line=386)
W('36,2437', 0o50375, '', 'VLOAD', 'DOT', kind='interp', line=387)
W('36,2440', 0o03540, '', '', 'RACT3', kind='operand', line=388)
# Page 558
W('36,2441', 0o03612, '', '', 'VIPRIME', 'SG1', kind='operand', line=390)
W('36,2442', 0o51165, '', 'SIGN', 'BPL', 'IF POSITIVE THEN SG1 = SG2 OTHERWISE', kind='interp', line=391)
W('36,2443', 0o02637, '', '', 'RELDELV', kind='operand', line=392)
W('36,2444', 0o74454, '', '', 'USEKAY', 'SIGN(SG2-SG1)=SIGN(SG2)=SIGN(RELDELV)', kind='operand', line=393)
W('36,2445', 0o57535, '', 'SLOAD', 'DCOMP', kind='interp', line=394)
W('36,2446', 0o33117, '', '', 'DECTWO', kind='operand', line=395)
W('36,2447', 0o51165, '', 'SIGN', 'BPL', kind='interp', line=396)
W('36,2450', 0o02637, '', '', 'RELDELV', kind='operand', line=397)
W('36,2451', 0o74462, '', '', 'NEXUS', kind='operand', line=398)
W('36,2452', 0o52076, '', 'DCOMP', 'GOTO', kind='interp', line=399)
W('36,2453', 0o74460, '', '', 'USEKAY +4', kind='operand', line=400)
W('36,2454', 0o43135, 'USEKAY', 'SLOAD', 'BON', kind='interp', line=401)
W('36,2455', 0o33117, '', '', 'DECTWO', kind='operand', line=402)
W('36,2456', 0o00316, '', '', 'KFLAG', kind='operand', line=403)
W('36,2457', 0o74462, '', '', 'NEXUS', kind='operand', line=404)
W('36,2460', 0o77625, '', 'DSU', kind='interp', line=405)
W('36,2461', 0o36150, '', '', 'P21ONENN', kind='operand', line=406)
W('36,2462', 0o17766, 'NEXUS', 'STODL', 'NN1', kind='interp', line=407)
W('36,2463', 0o02625, '', '', 'HP', kind='operand', line=408)
W('36,2464', 0o36641, '', 'STCALL', 'POSTTPI', kind='interp', line=409)
W('36,2465', 0o03657, '', '', 'QTEMP', kind='operand', line=410)
#   BANK 07
#   SETLOC XANG
#   BANK
#   COUNT 07/XANG

# CENTRAL ANGLE SUBROUTINE
# THIS SUBROUTINE COMPUTES THE CENTRAL ANGLE OF TRAVEL OF THE
# PASSIVE VEHICLE DURING THE TRANSFER.

W('07,2441', 0o40220, 'TRANSANG', 'STQ', 'SETPD', kind='interp', line=420)
W('07,2442', 0o02370, '', '', 'SUBEXIT', kind='operand', line=421)
W('07,2443', 0o00001, '', '', '0', kind='operand', line=422)
W('07,2444', 0o73150, '', 'LXA,1', 'LXA,2', kind='interp', line=423)
W('07,2445', 0o03745, '', '', 'XRS', kind='operand', line=424)
W('07,2446', 0o03746, '', '', 'XRS +1', kind='operand', line=425)
W('07,2447', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=426)
W('07,2450', 0o03640, '', '', 'VPASS4', kind='operand', line=427)
W('07,2451', 0o57176, '', '', '0,2', kind='operand', line=428)
W('07,2452', 0o22746, '', 'STODL*', 'VVEC', kind='interp', line=429)
W('07,2453', 0o11742, '', '', 'MUTABLE +2,1', kind='operand', line=430)
W('07,2454', 0o53715, '', 'PDVL', 'VSR*', 'SQRT MU (+18 OR +15)                  00D', kind='interp', line=431)
W('07,2455', 0o03632, '', '', 'RPASS4', kind='operand', line=432)
W('07,2456', 0o57176, '', '', '0,2', kind='operand', line=433)
W('07,2457', 0o64646, '', 'ABVAL', 'PDDL*', 'MAGNITUDE OF R (+29 OR +27)           02D', kind='interp', line=434)
W('07,2460', 0o11740, '', '', 'MUTABLE,1', kind='operand', line=435)
W('07,2461', 0o47515, '', 'PDVL', 'VSQ', '1/MU (+34 OR +28)                     04D', kind='interp', line=436)
W('07,2462', 0o02746, '', '', 'VVEC', kind='operand', line=437)
W('07,2463', 0o57301, '', 'NORM', 'DMPR', 'PUSH LIST AT 02D', kind='interp', line=438)
W('07,2464', 0o00047, '', '', 'X1', kind='operand', line=439)
# Page 559
W('07,2465', 0o53605, '', 'DMP', 'SRR*', kind='interp', line=441)
W('07,2466', 0o00003, '', '', '02D', kind='operand', line=442)
W('07,2467', 0o21576, '', '', '0 -3,1', kind='operand', line=443)
W('07,2470', 0o77621, '', 'BDSU', '', 'R V**/MU (+6)', kind='interp', line=444)
W('07,2471', 0o11616, '', '', 'D1/32', kind='operand', line=445)
W('07,2472', 0o65301, '', 'NORM', 'PDDL', kind='interp', line=446)
W('07,2473', 0o00047, '', '', 'X1', '(2 - R V**/MU)        (+6-N)', kind='operand', line=447)
W('07,2474', 0o56362, '', 'SR1R', 'DDV', 'MAGNITUDE OF R        (+30 OR +28)', kind='interp', line=448)
W('07,2475', 0o41457, '', 'SL*', 'PUSH', 'R/(2 - R V**/MU)      (+29 OR +27)02D', kind='interp', line=449)
W('07,2476', 0o20174, '', '', '0 -5,1', kind='operand', line=450)
W('07,2477', 0o75542, '', 'SR1', 'SQRT', kind='interp', line=451)
W('07,2500', 0o77605, '', 'DMP', kind='interp', line=452)
W('07,2501', 0o65301, '', 'NORM', 'PDDL', 'ASUBP***                              00D', kind='interp', line=453)
W('07,2502', 0o00047, '', '', 'X1', kind='operand', line=454)
W('07,2503', 0o56342, '', 'SR1', 'DDV', kind='interp', line=455)
W('07,2504', 0o53605, '', 'DMP', 'SL*', kind='interp', line=456)
W('07,2505', 0o03752, '', '', 'TF', kind='operand', line=457)
W('07,2506', 0o20201, '', '', '0,1', kind='operand', line=458)
W('07,2507', 0o60325, '', 'PDDL', 'NORM', kind='interp', line=459)
W('07,2510', 0o11630, '', '', '2PISC', kind='operand', line=460)
W('07,2511', 0o00047, '', '', 'X1', kind='operand', line=461)
W('07,2512', 0o56325, '', 'PDDL', 'DDV', kind='interp', line=462)
W('07,2513', 0o77657, '', 'SL*', kind='interp', line=463)
W('07,2514', 0o20176, '', '', '0 -3,1', 'CENTANG = (SQRT(MU/ASUP***)TF)', kind='operand', line=464)
W('07,2515', 0o37754, '', 'STCALL', 'CENTANG', 'IN REVOLUTIONS B-0', kind='interp', line=465)
W('07,2516', 0o02370, '', '', 'SUBEXIT', kind='operand', line=466)
#   BANK 35
#   SETLOC P17S1
#   BANK
#   COUNT 35/P17

# TPI SEARCH DISPLAY ROUTNE

W('35,3151', 0o04627, 'P17', 'TC', 'AVFLAGA', 'AVFLAG = CSM , SET TRACK + UPDATE FLAGS', line=474)
W('35,3152', 0o03154, '', 'TC', 'P17.1', line=475)
W('35,3153', 0o04642, 'P77', 'TC', 'AVFLAGP', 'AVFLAG = LEM , SET TRACK + UPDATE FLAGS', line=476)
W('35,3154', 0o04647, 'P17.1', 'TC', 'P20FLGON', '      SET UPDATE FLAG', line=477)
W('35,3155', 0o34614, '', 'CAF', 'V06N37', '      DISPLAY TTPI TIME', line=478)
W('35,3156', 0o04575, '', 'TC', 'VNPOOH', line=479)
W('35,3157', 0o06006, '', 'TC', 'INTPRET', line=480)
W('35,3160', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=481)
W('35,3161', 0o00670, '', '', 'UPDATFLG', kind='operand', line=482)
W('35,3162', 0o74012, '', '', 'S17.1', 'UPDATE STATE VECTORS TO TTPI', kind='operand', line=483)
W('35,3163', 0o76014, '', 'SET', 'AXT,1', kind='interp', line=484)
W('35,3164', 0o00470, '', '', 'UPDATFLG', kind='operand', line=485)
W('35,3165', 0o00002, '', 'DEC', '2', 'DELTA H = 2   K POSITIVE , KFLAG OFF', kind='data', line=486)
W('35,3166', 0o76014, '', 'BOFF', 'AXT,1', kind='interp', line=487)
W('35,3167', 0o00356, '', '', 'KFLAG', kind='operand', line=488)
W('35,3170', 0o73172, '', '', '+2', kind='operand', line=489)
W('35,3171', 0o00001, '', 'DEC', '1', 'DELTA H = 1   K NEGATIVE , KFLAG ON', kind='data', line=490)
# Page 560
W('35,3172', 0o77530, '', 'SXA,1', 'EXIT', kind='interp', line=492)
W('35,3173', 0o01132, '', '', 'OPTION2', kind='operand', line=493)
W('35,3174', 0o33263, '', 'CAF', 'V06N72', 'DISPLAY PHI , DELTA H , SEARCH OPTION K', line=494)
W('35,3175', 0o03237, '', 'TC', 'VNCOMP17', line=495)
W('35,3176', 0o06006, '', 'TC', 'INTPRET', line=496)
W('35,3177', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=497)
W('35,3200', 0o00670, '', '', 'UPDATFLG', kind='operand', line=498)
W('35,3201', 0o00076, '', '', 'KFLAG', kind='operand', line=499)
W('35,3202', 0o45335, '', 'SLOAD', 'DSU', kind='interp', line=500)
W('35,3203', 0o01133, '', '', 'OPTION2', 'RESET KFLAG ON FOR OPTION =1', kind='operand', line=501)
W('35,3204', 0o36150, '', '', 'P21ONENN', '           OFF FOR OPTION =2', kind='operand', line=502)
W('35,3205', 0o43030, '', 'BHIZ', 'CLEAR', kind='interp', line=503)
W('35,3206', 0o73210, '', '', '+2', kind='operand', line=504)
W('35,3207', 0o00276, '', '', 'KFLAG', kind='operand', line=505)
W('35,3210', 0o46135, '', 'SLOAD', 'BHIZ', kind='interp', line=506)
W('35,3211', 0o03747, '', '', 'XRS +1', kind='operand', line=507)
W('35,3212', 0o73216, '', '', '+4', kind='operand', line=508)
W('35,3213', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=509)
W('35,3214', 0o33126, '', '', 'HPL', kind='operand', line=510)
W('35,3215', 0o73220, '', '', 'P17.2', kind='operand', line=511)
W('35,3216', 0o77745, '', 'DLOAD', kind='interp', line=512)
W('35,3217', 0o33124, '', '', 'HPE', kind='operand', line=513)
W('35,3220', 0o36321, 'P17.2', 'STCALL', 'HPERMIN', kind='interp', line=514)
W('35,3221', 0o74070, '', '', 'S17.2', kind='operand', line=515)
W('35,3222', 0o77414, '', 'SET', 'EXIT', kind='interp', line=516)
W('35,3223', 0o00470, '', '', 'UPDATFLG', kind='operand', line=517)
W('35,3224', 0o34616, 'P17.3', 'CAF', 'V06N58', 'DISPLAY DELTA VTPI , DELTA VTPF , AND H', line=518)
W('35,3225', 0o03237, '', 'TC', 'VNCOMP17', line=519)
W('35,3226', 0o34615, '', 'CAF', 'V06N55', 'DISPLAY PERICENTER CODE AND CENTRAL ANG.', line=520)
W('35,3227', 0o04662, '', 'TC', 'BANKCALL', line=521)
W('35,3230', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=522)
W('35,3231', 0o04106, '', 'TC', 'GOTOPOOH', 'TERMINATE PROGRAM', line=523)
W('35,3232', 0o04106, '', 'TC', 'GOTOPOOH', 'END PROGRAM', line=524)
W('35,3233', 0o03154, '', 'TC', 'P17.1', 'RECYCLE WITH NEW TTPI OR SEARCH OPTION', line=525)
W('35,3234', 0o35016, '', 'CAF', 'TWO', 'BLANK R2', line=526)
W('35,3235', 0o05526, '', 'TC', 'BLANKET', line=527)
W('35,3236', 0o15217, '', 'TCF', 'ENDOFJOB', line=528)
#   EBANK= RTRN

W('35,3237', 0o00006, 'VNCOMP17', 'EXTEND', line=531)
W('35,3240', 0o23766, '', 'QXCH', 'QSAVED', line=532)
W('35,3241', 0o55765, '', 'TS', 'VERBNOUN', line=533)
W('35,3242', 0o31765, '', 'CA', 'VERBNOUN', line=534)
W('35,3243', 0o04662, '', 'TCR', 'BANKCALL', line=535)
W('35,3244', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=536)
W('35,3245', 0o03242, '', 'TC', '-3', 'TERMINATE ILLEGAL REDISPLAY', line=537)
W('35,3246', 0o01766, '', 'TC', 'QSAVED', 'PROCEED', line=538)
W('35,3247', 0o40154, '', 'CS', 'MPAC', 'RECYCLE WITH NEW TPI TIME', line=539)
W('35,3250', 0o65012, '', 'AD', 'BIT6', 'OR PROCEED WITH NEW SEARCH OPTION', line=540)
W('35,3251', 0o00006, '', 'EXTEND', line=541)
# Page 561
W('35,3252', 0o13154, '', 'BZF', 'P17.1', line=543)
W('35,3253', 0o03242, '', 'TC', 'VNCOMP17 +3', line=544)
W('35,3254', 0o77414, 'ALARUMS', 'SET', 'EXIT', kind='interp', line=545)
W('35,3255', 0o00470, '', '', 'UPDATFLG', kind='operand', line=546)
W('35,3256', 0o05650, '', 'TC', 'ALARM', line=547)
W('35,3257', 0o00124, '', 'OCT', '00124', 'NO SAFE PERICENTER IN THIS SECTOR', kind='data', line=548)
W('35,3260', 0o35050, '', 'CAF', 'V05N09', line=549)
W('35,3261', 0o03237, '', 'TC', 'VNCOMP17', line=550)
W('35,3262', 0o04106, '', 'TC', 'GOTOPOOH', 'PROCEED ILLEGAL TERMINATE PROGRAM', line=551)
W('35,3263', 0o01510, 'V06N72', 'VN', '0672', kind='data', line=552)
