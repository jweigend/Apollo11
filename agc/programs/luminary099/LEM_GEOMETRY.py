"""LEM_GEOMETRY.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/LEM_GEOMETRY.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 320-325 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('LEM_GEOMETRY', 'LEM_GEOMETRY.agc', 'Luminary099', pages='320-325')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     LEM_GEOMETRY.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        320-325
# Mod history:  2009-05-16 RSB  Adapted from the corresponding
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

# Page 320
#   BANK 23
#   SETLOC LEMGEOM
#   BANK

#   SBANK= LOWSUPER
#   EBANK= XSM

# THESE TWO ROUTINES COMPUTE THE ACTUAL STATE VECTOR FOR LM,CSM BY ADDING
# THE CONIC R,V AND THE DEVIATIONSR,V. THE STATE VECTORS ARE CONVERTED TO
# METERS B-29 AND METERS/CSEC B-7 AND STORED APPROPRIATELY IN RN,VN OR
# R-OTHER , V-OTHER FOR DOWNLINK. THE ROUTINES NAMES ARE SWITCHED IN THE
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
# R(T) IN R-OTHER, V(T) IN V-OTHER   (T IS DEFINED BY T-OTHER)

#   COUNT* $$/GEOM
W('13,2070', 0o43414, 'SVDWN2', 'BOF', 'RVQ', 'SW=1=AVETOMID DOING W-MATRIX INTEG.', kind='interp', line=56)
W('13,2071', 0o04756, '', '', 'AVEMIDSW', kind='operand', line=57)
W('13,2072', 0o26073, '', '', '+1', kind='operand', line=58)
W('13,2073', 0o53775, '', 'VLOAD', 'VSL*', kind='interp', line=59)
W('13,2074', 0o01521, '', '', 'TDELTAV', kind='operand', line=60)
W('13,2075', 0o57605, '', '', '0 -7,2', kind='operand', line=61)
W('13,2076', 0o53655, '', 'VAD', 'VSL*', kind='interp', line=62)
W('13,2077', 0o01535, '', '', 'RCV', kind='operand', line=63)
W('13,2100', 0o57576, '', '', '0,2', kind='operand', line=64)
W('13,2101', 0o25221, '', 'STOVL', 'RN', kind='interp', line=65)
W('13,2102', 0o01527, '', '', 'TNUV', kind='operand', line=66)
W('13,2103', 0o53257, '', 'VSL*', 'VAD', kind='interp', line=67)
W('13,2104', 0o57602, '', '', '0 -4,2', kind='operand', line=68)
W('13,2105', 0o01543, '', '', 'VCV', kind='operand', line=69)
W('13,2106', 0o77657, '', 'VSL*', kind='interp', line=70)
W('13,2107', 0o57576, '', '', '0,2', kind='operand', line=71)
W('13,2110', 0o15227, '', 'STODL', 'VN', kind='interp', line=72)
W('13,2111', 0o01517, '', '', 'TET', kind='operand', line=73)
W('13,2112', 0o01235, '', 'STORE', 'PIPTIME', kind='interp', line=74)
W('13,2113', 0o77616, '', 'RVQ', kind='interp', line=75)
# Page 321
W('13,2114', 0o53775, 'SVDWN1', 'VLOAD', 'VSL*', kind='interp', line=77)
W('13,2115', 0o01521, '', '', 'TDELTAV', kind='operand', line=78)
W('13,2116', 0o57605, '', '', '0 -7,2', kind='operand', line=79)
W('13,2117', 0o53655, '', 'VAD', 'VSL*', kind='interp', line=80)
W('13,2120', 0o01535, '', '', 'RCV', kind='operand', line=81)
W('13,2121', 0o57576, '', '', '0,2', kind='operand', line=82)
W('13,2122', 0o25720, '', 'STOVL', 'R-OTHER', kind='interp', line=83)
W('13,2123', 0o01527, '', '', 'TNUV', kind='operand', line=84)
W('13,2124', 0o53257, '', 'VSL*', 'VAD', kind='interp', line=85)
W('13,2125', 0o57602, '', '', '0 -4,2', kind='operand', line=86)
W('13,2126', 0o01543, '', '', 'VCV', kind='operand', line=87)
W('13,2127', 0o77657, '', 'VSL*', kind='interp', line=88)
W('13,2130', 0o57576, '', '', '0,2', kind='operand', line=89)
W('13,2131', 0o01726, '', 'STORE', 'V-OTHER', kind='interp', line=90)
W('13,2132', 0o77616, '', 'RVQ', kind='interp', line=91)

# Page 322
# THE FOLLOWING ROUTINE TAKES A HALF UNIT TARGET VECTOR REFERRED TO NAV BASE COORDINATES AND FINDS BOTH
# GIMBAL ORIENTATIONS AT WHICH THE RR MIGHT SIGHT THE TARGET. THE GIMBAL ANGLES CORRESPONDING TO THE PRESENT MODE
# ARE LEFT IN MODEA AND THOSE WHICH WOULD BE USED AFTER A REMODE IN MODEB. THIS ROUTINE ASSUMES MODE 1 IS TRUNNION
# ANGLE LESS THAN 90 DEGS IN ABS VALUE WITH ARBITRARY SHAFT, WITH A CORRESPONDING DEFINITION FOR MODE 2. MODE
# SELECTION AND LIMIT CHECKING ARE DONE ELSEWHERE.
#
# THE MODE 1 CONFIGURATION IS CALCULATED FROM THE VECTOR AND THEN MODE 2 IS FOUND USING THE RELATIONS
#
# S(2) = 180 + S(1)
# T(2) = 180 - T(1)
#
# THE VECTOR ARRIVES IN MPAC WHERE TRG*SMNB OR *SMNB* WILL HAVE LEFT IT.

W('13,2133', 0o00041, 'RRANGLES', 'STORE', '32D', kind='interp', line=107)
W('13,2134', 0o57545, '', 'DLOAD', 'DCOMP', 'SINCE WE WILL FIND THE MODE 1 SHAFT', kind='interp', line=108)
W('13,2135', 0o00043, '', '', '34D', 'ANGLE LATER, WE CAN FIND THE MODE 1', kind='operand', line=109)
W('13,2136', 0o67401, '', 'SETPD', 'ASIN', 'TRUNNION BY SIMPLY TAKING THE ARCSIN OF', kind='interp', line=110)
W('13,2137', 0o00001, '', '', '0', 'THE Y COMPONENT, THE ASIN GIVIN AN', kind='operand', line=111)
W('13,2140', 0o44206, '', 'PUSH', 'BDSU', 'ANSWER WHOSE ABS VAL IS LESS THAN 90 DEG', kind='interp', line=112)
W('13,2141', 0o24005, '', '', 'LODPHALF', kind='operand', line=113)
W('13,2142', 0o14005, '', 'STODL', '4', 'MODE 2 TRUNNION TO 4.', kind='interp', line=114)

W('13,2143', 0o24007, '', '', 'LO6ZEROS', kind='operand', line=116)
W('13,2144', 0o24043, '', 'STOVL', '34D', 'UNIT THE PROJECTION OF THE VECTOR', kind='interp', line=117)
W('13,2145', 0o00041, '', '', '32D', '  IN THE X-Z PLANE', kind='operand', line=118)
W('13,2146', 0o41056, '', 'UNIT', 'BOVB', 'IF OVERFLOW,TARGET VECTOR IS ALONG Y', kind='interp', line=119)
W('13,2147', 0o52421, '', '', 'LUNDESCH', 'CALL FOR MANEUVER UNLESS ON LUNAR SURF', kind='operand', line=120)
W('13,2150', 0o14041, '', 'STODL', '32D', 'PROJECTION VECTOR.', kind='interp', line=121)
W('13,2151', 0o00041, '', '', '32D', kind='operand', line=122)
W('13,2152', 0o44142, '', 'SR1', 'STQ', kind='interp', line=123)
W('13,2153', 0o00051, '', '', 'S2', kind='operand', line=124)
W('13,2154', 0o14023, '', 'STODL', 'SINTH', 'USE ARCTRIG SINCE SHAFT COULD BE ARB.', kind='interp', line=125)
W('13,2155', 0o00045, '', '', '36D', kind='operand', line=126)
W('13,2156', 0o77742, '', 'SR1', kind='interp', line=127)
W('13,2157', 0o34021, '', 'STCALL', 'COSTH', kind='interp', line=128)
W('13,2160', 0o47320, '', '', 'ARCTRIG', kind='operand', line=129)
# Page 323
W('13,2161', 0o43206, '', 'PUSH', 'DAD', 'MODE 1 SHAFT TO 2.', kind='interp', line=131)
W('13,2162', 0o24005, '', '', 'LODPHALF', kind='operand', line=132)
W('13,2163', 0o24007, '', 'STOVL', '6', kind='interp', line=133)
W('13,2164', 0o00005, '', '', '4', kind='operand', line=134)
W('13,2165', 0o77634, '', 'RTB', '', 'FIND MODE 2 CDU ANGLES.', kind='interp', line=135)
W('13,2166', 0o21635, '', '', '2V1STO2S', kind='operand', line=136)
W('13,2167', 0o25112, '', 'STOVL', 'MODEB', kind='interp', line=137)
W('13,2170', 0o00001, '', '', '0', kind='operand', line=138)
W('13,2171', 0o77634, '', 'RTB', '', 'MODE 1 ANGLES TO MODE A.', kind='interp', line=139)
W('13,2172', 0o21635, '', '', '2V1STO2S', kind='operand', line=140)
W('13,2173', 0o01110, '', 'STORE', 'MODEA', kind='interp', line=141)
W('13,2174', 0o77776, '', 'EXIT', kind='interp', line=142)

W('13,2175', 0o40110, '', 'CS', 'RADMODES', 'SWAP MODEA AND MODEB IF RR IN MODE 2.', line=144)
W('13,2176', 0o74740, '', 'MASK', 'ANTENBIT', line=145)
W('13,2177', 0o10000, '', 'CCS', 'A', line=146)
W('13,2200', 0o12204, '', 'TCF', '+4', line=147)

W('13,2201', 0o53110, '', 'DXCH', 'MODEA', line=149)
W('13,2202', 0o53112, '', 'DXCH', 'MODEB', line=150)
W('13,2203', 0o53110, '', 'DXCH', 'MODEA', line=151)

W('13,2204', 0o06037, '', 'TC', 'INTPRET', line=153)
W('13,2205', 0o77650, '', 'GOTO', kind='interp', line=154)
W('13,2206', 0o00051, '', '', 'S2', kind='operand', line=155)
# Page 324
# GIVEN RR TRUNNION AND SHAFT (T,S) IN TANGNB,+1,FIND THE ASSOCIATED
# LINE OF SIGHT IN NAV BASE AXES.  THE HALF UNIT VECTOR, .5(SIN(S)COS(T),
# -SIN(T),COS(S)COS(T)) IS LEFT IN MPAC AND 32D.

#   SETLOC INFLIGHT
#   BANK

#   COUNT* $$/GEOM

W('23,2041', 0o47135, 'RRNB', 'SLOAD', 'RTB', kind='interp', line=166)
W('23,2042', 0o03753, '', '', 'TANGNB', kind='operand', line=167)
W('23,2043', 0o21576, '', '', 'CDULOGIC', kind='operand', line=168)
W('23,2044', 0o41401, '', 'SETPD', 'PUSH', 'TRUNNION ANGLE TO 0', kind='interp', line=169)
W('23,2045', 0o00001, '', '', '0', kind='operand', line=170)
W('23,2046', 0o57556, '', 'SIN', 'DCOMP', kind='interp', line=171)
W('23,2047', 0o14043, '', 'STODL', '34D', 'Y COMPONENT', kind='interp', line=172)

W('23,2050', 0o41546, '', 'COS', 'PUSH', '.5 COS(T) TO 0', kind='interp', line=174)
W('23,2051', 0o47135, '', 'SLOAD', 'RTB', kind='interp', line=175)
W('23,2052', 0o03754, '', '', 'TANGNB +1', kind='operand', line=176)
W('23,2053', 0o21576, '', '', 'CDULOGIC', kind='operand', line=177)
W('23,2054', 0o71406, 'RRNB1', 'PUSH', 'COS', 'SHAFT ANGLE TO 2', kind='interp', line=178)
W('23,2055', 0o72405, '', 'DMP', 'SL1', kind='interp', line=179)
W('23,2056', 0o00001, '', '', '0', kind='operand', line=180)
W('23,2057', 0o14045, '', 'STODL', '36D', 'Z COMPONENT', kind='interp', line=181)

W('23,2060', 0o41356, '', 'SIN', 'DMP', kind='interp', line=183)
W('23,2061', 0o77752, '', 'SL1', kind='interp', line=184)
W('23,2062', 0o24041, '', 'STOVL', '32D', kind='interp', line=185)
W('23,2063', 0o00041, '', '', '32D', kind='operand', line=186)
W('23,2064', 0o77616, '', 'RVQ', kind='interp', line=187)

# THIS ENTRY TO RRNB REQUIRES THE TRUNNION AND SHAFT ANGLES IN MPAC AND MPAC +1 RESPECTIVELY

W('23,2065', 0o14025, 'RRNBMPAC', 'STODL', '20D', 'SAVE SHAFT CDU IN 21.', kind='interp', line=191)
W('23,2066', 0o00155, '', '', 'MPAC', 'SET MODE TO DP.  (THE PRECEEDING STORE', kind='operand', line=192)
# MAY BE DP. TP OR VECTOR.)
W('23,2067', 0o40234, '', 'RTB', 'SETPD', kind='interp', line=194)
W('23,2070', 0o21576, '', '', 'CDULOGIC', kind='operand', line=195)
W('23,2071', 0o00001, '', '', '0', kind='operand', line=196)
W('23,2072', 0o73406, '', 'PUSH', 'SIN', 'TRUNNION ANGLE TO 0', kind='interp', line=197)
W('23,2073', 0o77676, '', 'DCOMP', kind='interp', line=198)
W('23,2074', 0o14043, '', 'STODL', '34D', 'Y COMPONENT', kind='interp', line=199)
W('23,2075', 0o41546, '', 'COS', 'PUSH', '.5COS(T) TO 0', kind='interp', line=200)
W('23,2076', 0o47135, '', 'SLOAD', 'RTB', "PICK UP CDU'S.", kind='interp', line=201)
W('23,2077', 0o00026, '', '', '21D', kind='operand', line=202)
W('23,2100', 0o21576, '', '', 'CDULOGIC', kind='operand', line=203)
W('23,2101', 0o77650, '', 'GOTO', kind='interp', line=204)
W('23,2102', 0o46054, '', '', 'RRNB1', kind='operand', line=205)
# Page 325 (empty page)
