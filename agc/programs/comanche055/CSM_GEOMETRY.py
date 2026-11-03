"""CSM_GEOMETRY.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/CSM_GEOMETRY.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 285-296 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('CSM_GEOMETRY', 'CSM_GEOMETRY.agc', 'Comanche055', pages='285-296')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     CSM_GEOMETRY.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        285-296
# Mod history:  2009-05-08 RSB  Adapted from the Colossus249/ file of the
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

# Page 285
#   BANK 22
#   SETLOC COMGEOM1
#   BANK

# THIS ROUTINE TAKES THE SHAFT AND TRUNNION ANGLES AS READ BY THE CM OPTICAL SYSTEM AND CONVERTS THEM INTO A  UNIT
# VECTOR REFERENCED TO THE NAVIGATION BASE COORDINATE SYSTEM AND COINCIDENT WITH THE SEXTANT LINE OF SIGHT.
#
# THE INPUTS ARE  1) THE SEXTANT SHAFT AND TRUNNION ANGLES ARE STORED SP IN LOCATIONS 3 AND 5 RESPECTIVELY OF THE
# MARK VAC AREA.  2) THE COMPLEMENT OF THE BASE ADDRESS OF THE MARK VAC AREA IS STORED SP AT LOCATION X1 OF YOUR
# JOB VAC AREA.
#
# THE OUTPUT IS A HALF-UNIT VECTOR IN NAVIGATION BASE COORDINATES AND STORED AT LOCATION 32D OF THE VAC AREA. THE
# OUTPUT IS ALSO AVAILABLE AT MPAC.

#   COUNT 23/GEOM

W('23,2000', 0o47133, 'SXTNB', 'SLOAD*', 'RTB', 'PUSHDOWN  00,02,04,(17D-19D),32D-36D', kind='interp', line=48)
W('23,2001', 0o00006, '', '', '5,1', 'TRUNNION = TA', kind='operand', line=49)
W('23,2002', 0o45513, '', '', 'CDULOGIC', kind='operand', line=50)
W('23,2003', 0o41434, '', 'RTB', 'PUSH', kind='interp', line=51)
W('23,2004', 0o46027, '', '', 'SXTLOGIC', kind='operand', line=52)
W('23,2005', 0o72556, '', 'SIN', 'SL1', kind='interp', line=53)
W('23,2006', 0o66606, '', 'PUSH', 'SLOAD*', 'PD2 = SIN(TA)', kind='interp', line=54)
W('23,2007', 0o00004, '', '', '3,1', 'SHAFT = SA', kind='operand', line=55)
W('23,2010', 0o41434, '', 'RTB', 'PUSH', 'PD4 = SA', kind='interp', line=56)
W('23,2011', 0o45513, '', '', 'CDULOGIC', kind='operand', line=57)

W('23,2012', 0o41346, '', 'COS', 'DMP', kind='interp', line=59)
W('23,2013', 0o00003, '', '', '2', kind='operand', line=60)
W('23,2014', 0o14041, '', 'STODL', 'STARM', 'COS(SA)SIN(TA)', kind='interp', line=61)

W('23,2015', 0o41356, '', 'SIN', 'DMP', kind='interp', line=63)
W('23,2016', 0o77626, '', 'STADR', kind='interp', line=64)
W('23,2017', 0o63734, '', 'STODL', 'STARM +2', 'SIN(SA)SIN(TA)', kind='interp', line=65)

W('23,2020', 0o77746, '', 'COS', kind='interp', line=67)
W('23,2021', 0o24045, '', 'STOVL', 'STARM +4', kind='interp', line=68)
W('23,2022', 0o00041, '', '', 'STARM', 'STARM = 32D', kind='operand', line=69)
W('23,2023', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=70)
W('23,2024', 0o06302, '', '', 'NB1NB2', kind='operand', line=71)
W('23,2025', 0o00041, '', 'STORE', '32D', kind='interp', line=72)
W('23,2026', 0o77616, '', 'RVQ', kind='interp', line=73)

W('23,2027', 0o32323, 'SXTLOGIC', 'CAF', '10DEGS-', 'CORRECT FOR 19.775 DEGREE OFFSET', line=76)
W('23,2030', 0o26154, '', 'ADS', 'MPAC', line=77)
W('23,2031', 0o35003, '', 'CAF', 'QUARTER', line=78)
W('23,2032', 0o07256, '', 'TC', 'SHORTMP', line=79)
W('23,2033', 0o06030, '', 'TC', 'DANZIG', line=80)
# Page 286
# CALCSXA COMPUTES THE SEXTANT SHAFT AND TRUNNION ANGLES REQUIRED TO POSITION THE OPTICS SUCH THAT A STAR LINE-
# OF-SIGHT LIES ALONG THE STAR VECTOR.  THE ROUTINE TAKES THE GIVEN STAR VECTOR AND EXPRESSES IT AS A VECTOR REF-
# ERENCED TO THE OPTICS COORDINATE SYSTEM.  IN ADDITION IT SETS UP THREE UNIT VECTORS DEFINING THE X,Y, AND Z AXES
# REFERENCED TO THE OPTICS COORDINATE SYSTEM.
#
# THE INPUTS ARE  1) THE STAR VECTOR REFERRED TO PRESENT STABLE MEMBER COORDINATES STORED AT STAR.  2) SAME ANGLE
# INPUT AS *SMNB*, I.E. SINES AND COSINES OF THE CDU ANGLES, IN THE ORDER Y Z X, AT SINCDU AND COSCDU.  A CALL
# TO CDUTRIG WILL PROVIDE THIS INPUT.
#
# THE OUTPUTS ARE THE SEXTANT SHAFT AND TRUNNION ANGLES STORED DP AT SAC AND PAC RESPECTIVELY.  (LOW ORDER PART
# EQUAL TO ZERO).

W('23,2034', 0o77220, 'CALCSXA', 'ITA', 'VLOAD', 'PUSHDOWN 00-26D,28D,30D,32D-36D', kind='interp', line=95)
W('23,2035', 0o00034, '', '', '28D', kind='operand', line=96)
W('23,2036', 0o02766, '', '', 'STAR', kind='operand', line=97)
W('23,2037', 0o77624, '', 'CALL', kind='interp', line=98)
W('23,2040', 0o47644, '', '', '*SMNB*', kind='operand', line=99)
W('23,2041', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=100)
W('23,2042', 0o06260, '', '', 'NB2NB1', kind='operand', line=101)
W('23,2043', 0o26766, '', 'STOVL', 'STAR', kind='interp', line=102)
W('23,2044', 0o15333, '', '', 'HIUNITX', kind='operand', line=103)
W('23,2045', 0o26555, '', 'STOVL', 'XNB1', kind='interp', line=104)
W('23,2046', 0o15331, '', '', 'HIUNITY', kind='operand', line=105)
W('23,2047', 0o26563, '', 'STOVL', 'YNB1', kind='interp', line=106)
W('23,2050', 0o15327, '', '', 'HIUNITZ', kind='operand', line=107)
W('23,2051', 0o36571, '', 'STCALL', 'ZNB1', kind='interp', line=108)
W('23,2052', 0o46076, '', '', 'SXTANG1', kind='operand', line=109)
# Page 287
# SXTANG COMPUTES THE SEXTANT SHAFT AND TRUNNION ANGLES REQUIRED TO POSITION THE OPTICS SUCH THAT A STAR LINE-OF-
# SIGHT LIES ALONG THE STAR VECTOR.
#
# THE INPUTS ARE  1) THE STAR VECTOR REFERRED TO ANY COORDINATE SYSTEM STORED AT STAR.  2) THE NAVIGATION BASE
# COORDINATES REFERRED TO THE SAME COORDINATE SYSTEM.  THESE THREE HALF-UNIT VECTORS ARE STORED AT XNB, YNB, AND
# ZNB.
#
# THE OUTPUTS ARE THE SEXTANT SHAFT AND TRUNNION ANGLES STORED DP AT SAC AND PAC RESPECTIVELY.  (LOW ORDER PART
# EQUAL TO ZERO).

W('23,2053', 0o47020, 'SXTANG', 'ITA', 'RTB', 'PUSHDOWN  16D,18D,22D-26D,28D', kind='interp', line=122)
W('23,2054', 0o00034, '', '', '28D', kind='operand', line=123)
W('23,2055', 0o45662, '', '', 'TRANSP1', 'EREF WRT NB2', kind='operand', line=124)
W('23,2056', 0o64375, '', 'VLOAD', 'MXV', kind='interp', line=125)
W('23,2057', 0o02714, '', '', 'XNB', kind='operand', line=126)
W('23,2060', 0o06260, '', '', 'NB2NB1', kind='operand', line=127)
W('23,2061', 0o77772, '', 'VSL1', kind='interp', line=128)
W('23,2062', 0o26555, '', 'STOVL', 'XNB1', kind='interp', line=129)
W('23,2063', 0o02722, '', '', 'YNB', kind='operand', line=130)
W('23,2064', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=131)
W('23,2065', 0o06260, '', '', 'NB2NB1', kind='operand', line=132)
W('23,2066', 0o26563, '', 'STOVL', 'YNB1', kind='interp', line=133)
W('23,2067', 0o02730, '', '', 'ZNB', kind='operand', line=134)
W('23,2070', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=135)
W('23,2071', 0o06260, '', '', 'NB2NB1', kind='operand', line=136)
W('23,2072', 0o02571, '', 'STORE', 'ZNB1', kind='interp', line=137)

W('23,2073', 0o47034, '', 'RTB', 'RTB', kind='interp', line=139)
W('23,2074', 0o45662, '', '', 'TRANSP1', kind='operand', line=140)
W('23,2075', 0o45676, '', '', 'TRANSP2', kind='operand', line=141)

W('23,2076', 0o47375, 'SXTANG1', 'VLOAD', 'VXV', kind='interp', line=143)
W('23,2077', 0o02571, '', '', 'ZNB1', kind='operand', line=144)
W('23,2100', 0o02766, '', '', 'STAR', kind='operand', line=145)
W('23,2101', 0o77600, '', 'BOV', kind='interp', line=146)
W('23,2102', 0o46103, '', '', '+1', kind='operand', line=147)
W('23,2103', 0o40056, '', 'UNIT', 'BOV', kind='interp', line=148)
W('23,2104', 0o46145, '', '', 'ZNB=S1', kind='operand', line=149)
W('23,2105', 0o00027, '', 'STORE', 'PDA', 'PDA = UNIT(ZNB X S)', kind='interp', line=150)

W('23,2106', 0o57441, '', 'DOT', 'DCOMP', kind='interp', line=152)
W('23,2107', 0o02555, '', '', 'XNB1', kind='operand', line=153)
W('23,2110', 0o24023, '', 'STOVL', 'SINTH', 'SIN(SA) = PDA . -XNB', kind='interp', line=154)
W('23,2111', 0o00027, '', '', 'PDA', kind='operand', line=155)

W('23,2112', 0o77641, '', 'DOT', kind='interp', line=157)
W('23,2113', 0o02563, '', '', 'YNB1', kind='operand', line=158)
W('23,2114', 0o34021, '', 'STCALL', 'COSTH', 'COS(SA) = PDA . YNB', kind='interp', line=159)
W('23,2115', 0o47256, '', '', 'ARCTRIG', kind='operand', line=160)
# Page 288
W('23,2116', 0o77634, '', 'RTB', kind='interp', line=162)
W('23,2117', 0o45546, '', '', '1STO2S', kind='operand', line=163)
W('23,2120', 0o26774, '', 'STOVL', 'SAC', kind='interp', line=164)
W('23,2121', 0o02766, '', '', 'STAR', kind='operand', line=165)
W('23,2122', 0o77600, '', 'BOV', kind='interp', line=166)
W('23,2123', 0o46124, '', '', '+1', kind='operand', line=167)
W('23,2124', 0o72441, '', 'DOT', 'SL1', kind='interp', line=168)
W('23,2125', 0o02571, '', '', 'ZNB1', kind='operand', line=169)
W('23,2126', 0o77726, '', 'ACOS', kind='interp', line=170)
W('23,2127', 0o62440, '', 'BMN', 'SL2', kind='interp', line=171)
W('23,2130', 0o46142, '', '', 'SXTALARM', 'TRUNNION ANGLE NEGATIVE', kind='operand', line=172)
W('23,2131', 0o45200, '', 'BOV', 'DSU', kind='interp', line=173)
W('23,2132', 0o46142, '', '', 'SXTALARM', 'TRUNNION ANGLE GREATER THAN 90 DEGREES', kind='operand', line=174)
W('23,2133', 0o06331, '', '', '20DEG-', kind='operand', line=175)
W('23,2134', 0o77634, '', 'RTB', kind='interp', line=176)
W('23,2135', 0o45546, '', '', '1STO2S', kind='operand', line=177)
W('23,2136', 0o02776, '', 'STORE', 'PAC', 'FOR FLIGHT USE, CULTFLAG IS ON IF', kind='interp', line=178)
W('23,2137', 0o77614, '', 'CLRGO', '', 'TRUNION IS GREATER THAN 90 DEG', kind='interp', line=179)
W('23,2140', 0o01630, '', '', 'CULTFLAG', kind='operand', line=180)
W('23,2141', 0o00034, '', '', '28D', kind='operand', line=181)
W('23,2142', 0o77614, 'SXTALARM', 'SETGO', '', 'ALARM HAS BEEN REMOVED FROM THIS', kind='interp', line=182)
W('23,2143', 0o01430, '', '', 'CULTFLAG', kind='operand', line=183)
W('23,2144', 0o00034, '', '', '28D', 'SUBROUTINE,ALARM WILL BE SET BY MPI', kind='operand', line=184)
W('23,2145', 0o77745, 'ZNB=S1', 'DLOAD', kind='interp', line=185)
W('23,2146', 0o06325, '', '', '270DEG', kind='operand', line=186)
W('23,2147', 0o16774, '', 'STODL', 'SAC', kind='interp', line=187)
W('23,2150', 0o06327, '', '', '20DEGS-', kind='operand', line=188)
W('23,2151', 0o02776, '', 'STORE', 'PAC', kind='interp', line=189)
W('23,2152', 0o77614, '', 'CLRGO', kind='interp', line=190)
W('23,2153', 0o01630, '', '', 'CULTFLAG', kind='operand', line=191)
W('23,2154', 0o00034, '', '', '28D', kind='operand', line=192)
# Page 289
# THESE TWO ROUTINES COMPUTE THE ACTUAL STATE VECTOR FOR LM, CSM BY ADDING
# THE CONIC R,V AND THE DEVIATIONSR,V.  THE STATE VECTORS ARE CONVERTED TO
# METERS B-29 AND METERS/CSEC B-7 AND STORED APPROPRIATELY IN RN,VN OR
# R-OTHER , V-OTHER FOR DOWNLINK.  THE ROUTINES NAMES ARE SWITCHED IN THE
# OTHER VEHICLES COMPUTER.
#
# INPUT
# STATE VECTOR IN TEMPORARY STORAGE AREA
# IF STATE VECTOR IS SCALED POS B27 AND VEL B5
# SET X2 TO +2
# IF STATE VECTOR IS SCALED POS B29 AND VEL B7
# SET X2 TO 0
#
# OUTPUT
# R(T) IN RN, V(T) IN VN, T IN PIPTIME
# OR
# R(T) IN R-OTHER, V(T) IN V-OTHER        (T IS DEFINED BY T-OTHER)

#   BANK 23
#   SETLOC COMGEOM2
#   BANK
#   COUNT 10/GEOM
W('10,2237', 0o43414, 'SVDWN1', 'BOF', 'RVQ', 'SW=1=AVETOMID DOING W-MATRIX INTEG', kind='interp', line=217)
W('10,2240', 0o04756, '', '', 'AVEMIDSW', kind='operand', line=218)
W('10,2241', 0o20242, '', '', '+1', kind='operand', line=219)
W('10,2242', 0o53775, '', 'VLOAD', 'VSL*', kind='interp', line=220)
W('10,2243', 0o01521, '', '', 'TDELTAV', kind='operand', line=221)
W('10,2244', 0o57605, '', '', '0 -7,2', kind='operand', line=222)
W('10,2245', 0o53655, '', 'VAD', 'VSL*', kind='interp', line=223)
W('10,2246', 0o01535, '', '', 'RCV', kind='operand', line=224)
W('10,2247', 0o57576, '', '', '0,2', kind='operand', line=225)
W('10,2250', 0o25171, '', 'STOVL', 'RN', kind='interp', line=226)
W('10,2251', 0o01527, '', '', 'TNUV', kind='operand', line=227)
W('10,2252', 0o53257, '', 'VSL*', 'VAD', kind='interp', line=228)
W('10,2253', 0o57602, '', '', '0 -4,2', kind='operand', line=229)
W('10,2254', 0o01543, '', '', 'VCV', kind='operand', line=230)
W('10,2255', 0o77657, '', 'VSL*', kind='interp', line=231)
W('10,2256', 0o57576, '', '', '0,2', kind='operand', line=232)
W('10,2257', 0o15177, '', 'STODL', 'VN', kind='interp', line=233)
W('10,2260', 0o01517, '', '', 'TET', kind='operand', line=234)
W('10,2261', 0o01205, '', 'STORE', 'PIPTIME', kind='interp', line=235)
W('10,2262', 0o77616, '', 'RVQ', kind='interp', line=236)

W('10,2263', 0o53775, 'SVDWN2', 'VLOAD', 'VSL*', kind='interp', line=238)
W('10,2264', 0o01521, '', '', 'TDELTAV', kind='operand', line=239)
W('10,2265', 0o57605, '', '', '0 -7,2', kind='operand', line=240)
W('10,2266', 0o53655, '', 'VAD', 'VSL*', kind='interp', line=241)
W('10,2267', 0o01535, '', '', 'RCV', kind='operand', line=242)
# Page 290
W('10,2270', 0o57576, '', '', '0,2', kind='operand', line=244)
W('10,2271', 0o25722, '', 'STOVL', 'R-OTHER', kind='interp', line=245)
W('10,2272', 0o01527, '', '', 'TNUV', kind='operand', line=246)
W('10,2273', 0o53257, '', 'VSL*', 'VAD', kind='interp', line=247)
W('10,2274', 0o57602, '', '', '0 -4,2', kind='operand', line=248)
W('10,2275', 0o01543, '', '', 'VCV', kind='operand', line=249)
W('10,2276', 0o77657, '', 'VSL*', kind='interp', line=250)
W('10,2277', 0o57576, '', '', '0,2', kind='operand', line=251)
W('10,2300', 0o01730, '', 'STORE', 'V-OTHER', kind='interp', line=252)
W('10,2301', 0o77616, '', 'RVQ', kind='interp', line=253)
# Page 291
# SUBROUTINE TO COMPUTE THE NATURAL LOG OF C(MPAC, MPAC +1).
#
# ENTRY:  CALL
# LOG
#
# SUBROUTINE RETURNS WITH -LOG IN DP MPAC.
#
# EBANK IS ARBITRARY..

#   BANK 14
#   SETLOC POWFLIT2
#   BANK
#   COUNT 23/GEOM

W('23,2155', 0o44301, 'LOG', 'NORM', 'BDSU', 'GENERATES LOG BY SHIFTING ARG', kind='interp', line=269)
W('23,2156', 0o00160, '', '', 'MPAC +3', 'UNTIL IT LIES BETWEEN .5 AND 1.', kind='operand', line=270)
W('23,2157', 0o06212, '', '', 'NEARLY1', 'THE LOG OF THIS PART IS FOUND AND THE', kind='operand', line=271)
W('23,2160', 0o77776, '', 'EXIT', '', 'LOG OF THE SHIFTED PART IS COMPUTED', kind='interp', line=272)

W('23,2161', 0o07171, '', 'TC', 'POLY', 'AND ADDED IN.  SHIFT COUNT STORED', line=274)

W('23,2162', 0o00002, '', 'DEC', '2', '(N-1, SUPPLIED BY SMERZH)', kind='data', line=276)
W('23,2163', 0o00000, '', '2DEC', '0', 'IN MPAC +3.', kind='data', line=277)
W('23,2164', 0o00000, kind='data', line=277)
W('23,2165', 0o01001, '', '2DEC', '.031335467', kind='data', line=278)
W('23,2166', 0o14636, kind='data', line=278)
W('23,2167', 0o00325, '', '2DEC', '.0130145859', kind='data', line=279)
W('23,2170', 0o07310, kind='data', line=279)
W('23,2171', 0o00541, '', '2DEC', '.0215738898', kind='data', line=280)
W('23,2172', 0o16735, kind='data', line=280)

W('23,2173', 0o35021, '', 'CAF', 'ZERO', line=282)
W('23,2174', 0o54156, '', 'TS', 'MPAC +2', line=283)
W('23,2175', 0o00006, '', 'EXTEND', line=284)
W('23,2176', 0o32214, '', 'DCA', 'CLOG2/32', line=285)
W('23,2177', 0o52155, '', 'DXCH', 'MPAC', line=286)
W('23,2200', 0o52160, '', 'DXCH', 'MPAC +3', line=287)
W('23,2201', 0o40000, '', 'COM', '', 'LOAD POSITIVE SHIFT COUNT IN A.', line=288)
W('23,2202', 0o07256, '', 'TC', 'SHORTMP', 'MULTIPLY BY SHIFT COUNT.', line=289)

W('23,2203', 0o52156, '', 'DXCH', 'MPAC +1', line=291)
W('23,2204', 0o52155, '', 'DXCH', 'MPAC', line=292)
W('23,2205', 0o52160, '', 'DXCH', 'MPAC +3', line=293)
W('23,2206', 0o20155, '', 'DAS', 'MPAC', line=294)
W('23,2207', 0o06006, '', 'TC', 'INTPRET', 'RESULT IN MPAC, MPAC +1', line=295)

W('23,2210', 0o77616, '', 'RVQ', kind='interp', line=297)

W('23,2211', 0o37777, 'NEARLY1', '2DEC', '.999999999', kind='data', line=299)
W('23,2212', 0o37777, kind='data', line=299)

# Page 292
W('23,2213', 0o00542, 'CLOG2/32', '2DEC', '.0216608494', kind='data', line=302)
W('23,2214', 0o34414, kind='data', line=302)

# Page 293
# SUBROUTINE NAME:      EARTH ROTATOR   (EARROT1 OR EARROT2)            DATE:           15 FEB 67
# MOD NO:  N +1                                                         LOG SECTION:    POWERED FLIGHT SUBROS
# MOD BY:  ENTRY GROUP (BAIRNSFATHER)
# FUNCTIONAL DESCRIPTION:       THIS ROUTINE PROJECTS THE INITIAL EARTH TARGET VECTOR RTINIT AHEAD THROUGH
# THE ESTIMATED TIME OF FLIGHT.  INITIAL CALL RESOLVES THE INITIAL TARGET VECTOR RTINIT INTO EASTERLY
# AND NORMAL COMPONENTS RTEAST AND RTNORM .  INITIAL AND SUBSEQUENT CALLS ROTATE THIS VECTOR
# ABOUT THE (FULL) UNIT POLAR AXIS UNITW THROUGH THE ANGLE WIE DTEAROT TO OBTAIN THE ROTATED
# TARGET VECTOR RT .  ALL VECTORS EXCEPT UNITW ARE HALF UNIT.
# THE EQUATIONS ARE
# -    -        -                      -
# RT = RTINIT + RTNORM (COS(WT) - 1) + RTEAST SIN(WT)
# WHERE   WT = WIE DTEAROT
# RTINIT = INITIAL TARGET VECTOR
# -        -       -
# RTEAST = UNITW*RTINIT
# -        -        -
# RTNORM = RTEAST*UNITW
#
# FOR CONTINUOUS UPDATING, ONLY ONE ENTRY TO EARROT1 IS REQUIRED, WITH SUBSEQUENT ENTRIES AT EARROT2.
# CALLING SEQUENCE:     FIRST CALL                      SUBSEQUENT CALL
# STCALL  DTEAROT                 STCALL  DTEAROT
# EARROT1                         EARROT2
# C(MPAC) UNSPECIFIED             C(MPAC) = DTEAROT
# PUSHLOC = PDL+0, ARBITRARY.  6 LOCATIONS USED.
#
# SUBROUTINES USED:  NONE
# NORMAL EXIT MODES:  RVQ
# ALARMS:  NONE
# OUTPUT:  RTEAST (-1)          .5 UNIT VECTOR EAST, COMPNT OF RTINIT   LEFT BY FIRST CALL
# RTNORM (-1)          .5 UNIT VECTOR NORML, COMPNT OF RTINIT  LEFT BY FIRST CALL
# RT     (-1)          .5 UNIT TARGET VECTOR, ROTATED          LEFT BY ALL CALLS
# DTEAROT  (-28) CS    MAY BE CHANGED BY EARROT2, IF OVER 1 DAY
# ERASABLE INITIALIZATION REQUIRED:
# UNITW  (0)           UNIT POLAR VECTOR                       PAD LOADED
# RTINIT (-1)          .5 UNIT INITIAL TARGET VECTOR           LEFT BY ENTRY
# DTEAROT  (-28) CS    TIME OF FLIGHT                          LEFT BY CALLER
# DEBRIS:  QPRET, PDL+0 ... PDL+5
# Page 294
#   EBANK= RTINIT

W('23,2215', 0o47375, 'EARROT1', 'VLOAD', 'VXV', kind='interp', line=345)
W('23,2216', 0o01714, '', '', 'UNITW', 'FULL UNIT VECTOR', kind='operand', line=346)
W('23,2217', 0o03452, '', '', 'RTINIT', '.5 UNIT', kind='operand', line=347)
W('23,2220', 0o03460, '', 'STORE', 'RTEAST', '.5 UNIT', kind='interp', line=348)

W('23,2221', 0o77635, '', 'VXV', kind='interp', line=350)
W('23,2222', 0o01714, '', '', 'UNITW', 'FULL UNIT', kind='operand', line=351)
W('23,2223', 0o17466, '', 'STODL', 'RTNORM', '.5 UNIT', kind='interp', line=352)
W('23,2224', 0o03606, '', '', 'DTEAROT', '(-28) CS', kind='operand', line=353)

W('23,2225', 0o56204, 'EARROT2', 'BOVB', 'DDV', kind='interp', line=355)
W('23,2226', 0o57352, '', '', 'TCDANZIG', 'RESET OVFIND, IF ON', kind='operand', line=356)
W('23,2227', 0o06256, '', '', '1/WIE', kind='operand', line=357)
W('23,2230', 0o41400, '', 'BOV', 'PUSH', kind='interp', line=358)
W('23,2231', 0o46245, '', '', 'OVERADAY', kind='operand', line=359)
W('23,2232', 0o45346, '', 'COS', 'DSU', kind='interp', line=360)
W('23,2233', 0o15333, '', '', 'HIDPHALF', kind='operand', line=361)
W('23,2234', 0o65361, '', 'VXSC', 'PDDL', 'XCH W PUSH LIST', kind='interp', line=362)
W('23,2235', 0o03466, '', '', 'RTNORM', '.5 UNIT', kind='operand', line=363)
W('23,2236', 0o74356, '', 'SIN', 'VXSC', kind='interp', line=364)
W('23,2237', 0o03460, '', '', 'RTEAST', '.5 UNIT', kind='operand', line=365)
W('23,2240', 0o76455, '', 'VAD', 'VSL1', kind='interp', line=366)
W('23,2241', 0o53455, '', 'VAD', 'UNIT', "INSURE THAT RT IS 'UNIT'.", kind='interp', line=367)
W('23,2242', 0o03452, '', '', 'RTINIT', '.5 UNIT', kind='operand', line=368)
W('23,2243', 0o03474, '', 'STORE', 'RT', '.5 UNIT TARGET VECTOR', kind='interp', line=369)

W('23,2244', 0o77616, '', 'RVQ', kind='interp', line=371)

W('23,2245', 0o75345, 'OVERADAY', 'DLOAD', 'SIGN', kind='interp', line=373)
W('23,2246', 0o06256, '', '', '1/WIE', kind='operand', line=374)
W('23,2247', 0o03606, '', '', 'DTEAROT', kind='operand', line=375)
W('23,2250', 0o77621, '', 'BDSU', kind='interp', line=376)
W('23,2251', 0o03606, '', '', 'DTEAROT', kind='operand', line=377)
W('23,2252', 0o03606, '', 'STORE', 'DTEAROT', kind='interp', line=378)

W('23,2253', 0o77650, '', 'GOTO', kind='interp', line=380)
W('23,2254', 0o46225, '', '', 'EARROT2', kind='operand', line=381)

# WIE            2DEC    .1901487997
W('23,2255', 0o01015, '1/WIE', '2DEC', '8616410', kind='data', line=384)
W('23,2256', 0o34732, kind='data', line=384)
W('23,2257', 0o15373, 'NB2NB1', '2DEC', '+.8431756920 B-1', kind='data', line=385)
W('23,2260', 0o11346, kind='data', line=385)
W('23,2261', 0o00000, '', '2DEC', '0', kind='data', line=386)
W('23,2262', 0o00000, kind='data', line=386)
W('23,2263', 0o67313, '', '2DEC', '-.5376381241 B-1', kind='data', line=387)
W('23,2264', 0o65307, kind='data', line=387)
# Page 295
W('23,2265', 0o00000, 'ZERINFLT', '2DEC', '0', kind='data', line=389)
W('23,2266', 0o00000, kind='data', line=389)
W('23,2267', 0o20000, 'HALFNFLT', '2DEC', '.5', kind='data', line=390)
W('23,2270', 0o00000, kind='data', line=390)
W('23,2271', 0o00000, '', '2DEC', '0', kind='data', line=391)
W('23,2272', 0o00000, kind='data', line=391)
W('23,2273', 0o10464, '', '2DEC', '+.5376381241 B-1', kind='data', line=392)
W('23,2274', 0o12470, kind='data', line=392)
W('23,2275', 0o00000, '', '2DEC', '0', kind='data', line=393)
W('23,2276', 0o00000, kind='data', line=393)
W('23,2277', 0o15373, '', '2DEC', '+.8431756920 B-1', kind='data', line=394)
W('23,2300', 0o11346, kind='data', line=394)
W('23,2301', 0o15373, 'NB1NB2', '2DEC', '+.8431756920 B-1', kind='data', line=395)
W('23,2302', 0o11346, kind='data', line=395)
W('23,2303', 0o00000, '', '2DEC', '0', kind='data', line=396)
W('23,2304', 0o00000, kind='data', line=396)
W('23,2305', 0o10464, '', '2DEC', '+.5376381241 B-1', kind='data', line=397)
W('23,2306', 0o12470, kind='data', line=397)
W('23,2307', 0o00000, '', '2DEC', '0', kind='data', line=398)
W('23,2310', 0o00000, kind='data', line=398)
W('23,2311', 0o20000, '', '2DEC', '.5', kind='data', line=399)
W('23,2312', 0o00000, kind='data', line=399)
W('23,2313', 0o00000, '', '2DEC', '0', kind='data', line=400)
W('23,2314', 0o00000, kind='data', line=400)
W('23,2315', 0o67313, '', '2DEC', '-.5376381241 B-1', kind='data', line=401)
W('23,2316', 0o65307, kind='data', line=401)
W('23,2317', 0o00000, '', '2DEC', '0', kind='data', line=402)
W('23,2320', 0o00000, kind='data', line=402)
W('23,2321', 0o15373, '', '2DEC', '+.8431756920 B-1', kind='data', line=403)
W('23,2322', 0o11346, kind='data', line=403)

# Page 296
W('23,2323', 0o07020, '10DEGS-', 'DEC', '3600', kind='data', line=406)

W('23,2324', 0o60000, '270DEG', 'OCT', '60000', 'SHAFT 270 DEGREES     2S COMP.', kind='data', line=408)
W('23,2325', 0o00000, '', 'OCT', '00000', kind='data', line=409)

W('23,2326', 0o61740, '20DEGS-', 'DEC', '-07199', kind='data', line=411)
W('23,2327', 0o77777, '', 'DEC', '-00000', kind='data', line=412)

W('23,2330', 0o07020, '20DEG-', 'DEC', '03600', kind='data', line=414)
W('23,2331', 0o00000, '', 'DEC', '00000', kind='data', line=415)
