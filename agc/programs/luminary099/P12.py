"""P12.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P12.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 838-842 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P12', 'P12.agc', 'Luminary099', pages='838-842')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P12.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        838-842
# Mod history:  2009-05-23 HG   Transcribed from page images.
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

# Page 838
#   BANK 24
#   SETLOC P12
#   BANK

#   EBANK= DVCNTR
#   COUNT* $$/P12

W('30,2061', 0o05353, 'P12LM', 'TC', 'PHASCHNG', line=35)
W('30,2062', 0o04024, '', 'OCT', '04024', kind='data', line=36)

W('30,2063', 0o04616, '', 'TC', 'BANKCALL', line=38)
W('30,2064', 0o11254, '', 'CADR', 'R02BOTH', 'CHECK THE STATUS OF THE IMU.', kind='data', line=39)

W('30,2065', 0o05504, '', 'TC', 'UPFLAG', line=41)
W('30,2066', 0o00141, '', 'ADRES', 'MUNFLAG', kind='data', line=42)

W('30,2067', 0o05504, '', 'TC', 'UPFLAG', 'INSURE 4-JET TRANSLATION CAPABILITY.', line=44)
W('30,2070', 0o00307, '', 'ADRES', 'ACC4-2FL', kind='data', line=45)

W('30,2071', 0o05504, '', 'TC', 'UPFLAG', 'PREVENT R10 FROM ISSUING CROSS-POINTER', line=47)
W('30,2072', 0o00015, '', 'ADRES', 'R10FLAG', 'OUTPUTS.', kind='data', line=48)

W('30,2073', 0o06011, '', 'TC', 'CLRADMOD', 'INITIALIZE RADMODES FOR R29.', line=50)

W('30,2074', 0o05516, '', 'TC', 'DOWNFLAG', 'CLEAR RENDEZVOUS FLAG FOR P22', line=52)
W('30,2075', 0o00010, '', 'ADRES', 'RNDVZFLG', kind='data', line=53)

W('30,2076', 0o36000, '', 'CAF', 'THRESH2', 'INITIALIZE DVMON', line=55)
W('30,2077', 0o55251, '', 'TS', 'DVTHRUSH', line=56)
W('30,2100', 0o34751, '', 'CAF', 'FOUR', line=57)
W('30,2101', 0o55515, '', 'TS', 'DVCNTR', line=58)

W('30,2102', 0o34755, '', 'CA', 'ZERO', line=60)
W('30,2103', 0o55462, '', 'TS', 'TRKMKCNT', "SHOW THAT R29 DOWNLINK DATA ISN'T READY.", line=61)
W('30,2104', 0o33035, '', 'CAF', 'V06N33A', line=62)
W('30,2105', 0o04616, '', 'TC', 'BANKCALL', 'FLASH TIG', line=63)
W('30,2106', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=64)
W('30,2107', 0o16001, '', 'TCF', 'GOTOPOOH', line=65)
W('30,2110', 0o12112, '', 'TCF', '+2', 'PROCEED', line=66)
W('30,2111', 0o12104, '', 'TCF', '-5', 'ENTER', line=67)

W('30,2112', 0o05353, '', 'TC', 'PHASCHNG', line=69)
W('30,2113', 0o04024, '', 'OCT', '04024', kind='data', line=70)

W('30,2114', 0o06037, '', 'TC', 'INTPRET', line=72)
W('30,2115', 0o77624, '', 'CALL', '', 'INITIALZE WM AND /LAND/', kind='interp', line=73)
W('30,2116', 0o46432, '', '', 'GUIDINIT', kind='operand', line=74)
W('30,2117', 0o45014, '', 'SET', 'CALL', kind='interp', line=75)
W('30,2120', 0o04464, '', '', 'FLPI', kind='operand', line=76)
W('30,2121', 0o60254, '', '', 'P12INIT', kind='operand', line=77)
# Page 839
W('30,2122', 0o77745, 'P12LMB', 'DLOAD', kind='interp', line=79)
W('30,2123', 0o25761, '', '', '(TGO)A', 'SET TGO TO AN INITIAL NOMINAL VALUE.', kind='operand', line=80)
W('30,2124', 0o17517, '', 'STODL', 'TGO', kind='interp', line=81)
W('30,2125', 0o03442, '', '', 'TIG', kind='operand', line=82)
W('30,2126', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=83)
W('30,2127', 0o27057, '', '', 'LEMPREC', 'ROTATE THE STATE VECTORS TO THE', kind='operand', line=84)
W('30,2130', 0o64375, '', 'VLOAD', 'MXV', 'IGNITION TIME.', kind='interp', line=85)
W('30,2131', 0o00007, '', '', 'VATT', kind='operand', line=86)
W('30,2132', 0o01734, '', '', 'REFSMMAT', kind='operand', line=87)
W('30,2133', 0o77772, '', 'VSL1', kind='interp', line=88)
W('30,2134', 0o27601, '', 'STOVL', 'V1S', 'COMPUTE V1S = VEL(TIG)*2(-7)M/CS.', kind='interp', line=89)
W('30,2135', 0o00001, '', '', 'RATT', kind='operand', line=90)
W('30,2136', 0o52521, '', 'MXV', 'VSL6', kind='interp', line=91)
W('30,2137', 0o01734, '', '', 'REFSMMAT', kind='operand', line=92)
W('30,2140', 0o37521, '', 'STCALL', 'R', 'COMPUTE R = POS(TIG)*2(-24)M.', kind='interp', line=93)
W('30,2141', 0o67130, '', '', 'MUNGRAV', 'COMPUTE GDT1/2(TIG)*2(-7)M/CS.', kind='operand', line=94)
W('30,2142', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=95)
W('30,2143', 0o03521, '', '', 'R', kind='operand', line=96)
W('30,2144', 0o37537, '', 'STCALL', 'UNIT/R/', 'COMPUTE UNIT/R/ FOR YCOMP.', kind='interp', line=97)
W('30,2145', 0o57312, '', '', 'YCOMP', kind='operand', line=98)
W('30,2146', 0o57461, '', 'SR', 'DCOMP', kind='interp', line=99)
W('30,2147', 0o20606, '', '', '5D', kind='operand', line=100)
W('30,2150', 0o17643, '', 'STODL', 'XRANGE', 'INITIALIZE XRANGE FOR NOUN 76.', kind='interp', line=101)
W('30,2151', 0o06456, '', '', 'VINJNOM', kind='operand', line=102)
W('30,2152', 0o16277, '', 'STODL', 'ZDOTD', kind='interp', line=103)
W('30,2153', 0o06460, '', '', 'RDOTDNOM', kind='operand', line=104)
W('30,2154', 0o02273, '', 'STORE', 'RDOTD', kind='interp', line=105)
W('30,2155', 0o77776, '', 'EXIT', kind='interp', line=106)

W('30,2156', 0o05353, '', 'TC', 'PHASCHNG', line=108)
W('30,2157', 0o04024, '', 'OCT', '04024', kind='data', line=109)

W('30,2160', 0o33034, 'NEWLOAD', 'CAF', 'V06N76', 'FLASH CROSS-RANGE, AND APOLUNE VALUES.', line=111)
W('30,2161', 0o04616, '', 'TC', 'BANKCALL', line=112)
W('30,2162', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=113)
W('30,2163', 0o16001, '', 'TCF', 'GOTOPOOH', line=114)
W('30,2164', 0o12166, '', 'TCF', '+2', 'PROCEED', line=115)
W('30,2165', 0o12160, '', 'TCF', 'NEWLOAD', 'ENTER NEW DATA.', line=116)

W('30,2166', 0o32320, '', 'CAF', 'P12ADRES', line=118)
W('30,2167', 0o55455, '', 'TS', 'WHICH', line=119)

W('30,2170', 0o05353, '', 'TC', 'PHASCHNG', line=121)
W('30,2171', 0o04024, '', 'OCT', '04024', kind='data', line=122)

W('30,2172', 0o06037, '', 'TC', 'INTPRET', line=124)
W('30,2173', 0o54345, '', 'DLOAD', 'SL', kind='interp', line=125)
W('30,2174', 0o03643, '', '', 'XRANGE', kind='operand', line=126)
W('30,2175', 0o20206, '', '', '5D', kind='operand', line=127)
W('30,2176', 0o77615, '', 'DAD', kind='interp', line=128)
# Page 840
W('30,2177', 0o02335, '', '', 'Y', kind='operand', line=130)
W('30,2200', 0o27633, '', 'STOVL', 'YCO', kind='interp', line=131)
W('30,2201', 0o03537, '', '', 'UNIT/R/', kind='operand', line=132)
W('30,2202', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=133)
W('30,2203', 0o06454, '', '', '49FPS', kind='operand', line=134)
W('30,2204', 0o03601, '', '', 'V1S', kind='operand', line=135)
W('30,2205', 0o03527, '', 'STORE', 'V', 'V(TIPOVER) = V(IGN) + 57FPS (UNIT/R/)', kind='interp', line=136)
W('30,2206', 0o72441, '', 'DOT', 'SL1', kind='interp', line=137)
W('30,2207', 0o03537, '', '', 'UNIT/R/', kind='operand', line=138)
W('30,2210', 0o27474, '', 'STOVL', 'RDOT', 'RDOT * 2(-7)', kind='interp', line=139)
W('30,2211', 0o03537, '', '', 'UNIT/R/', kind='operand', line=140)
W('30,2212', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=141)
W('30,2213', 0o03720, '', '', 'QAXIS', kind='operand', line=142)
W('30,2214', 0o03726, '', 'STORE', 'ZAXIS1', kind='interp', line=143)
W('30,2215', 0o77614, '', 'SETGO', kind='interp', line=144)
W('30,2216', 0o04421, '', '', 'FLVR', kind='operand', line=145)
W('30,2217', 0o60321, '', '', 'ASCENT', kind='operand', line=146)
W('30,2220', 0o77745, 'P12RET', 'DLOAD', kind='interp', line=147)
W('30,2221', 0o02361, '', '', 'ATP', 'ATP(2)*2(18)', kind='operand', line=148)
W('30,2222', 0o65316, '', 'DSQ', 'PDDL', kind='interp', line=149)
W('30,2223', 0o02355, '', '', 'ATY', 'ATY(2)*2(18)', kind='operand', line=150)
W('30,2224', 0o43316, '', 'DSQ', 'DAD', kind='interp', line=151)
W('30,2225', 0o75454, '', 'BZE', 'SQRT', kind='interp', line=152)
W('30,2226', 0o60232, '', '', 'YAWDUN', kind='operand', line=153)
W('30,2227', 0o55352, '', 'SL1', 'BDDV', kind='interp', line=154)
W('30,2230', 0o02355, '', '', 'ATY', kind='operand', line=155)
W('30,2231', 0o77736, '', 'ARCSIN', kind='interp', line=156)
W('30,2232', 0o26363, 'YAWDUN', 'STOVL', 'YAW', kind='interp', line=157)
W('30,2233', 0o03254, '', '', 'UNFC/2', kind='operand', line=158)
W('30,2234', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=159)
W('30,2235', 0o03537, '', '', 'UNIT/R/', kind='operand', line=160)
W('30,2236', 0o65552, '', 'SL1', 'ARCCOS', kind='interp', line=161)
W('30,2237', 0o77676, '', 'DCOMP', kind='interp', line=162)
W('30,2240', 0o02365, '', 'STORE', 'PITCH', kind='interp', line=163)
W('30,2241', 0o77776, '', 'EXIT', kind='interp', line=164)
W('30,2242', 0o05353, '', 'TC', 'PHASCHNG', line=165)
W('30,2243', 0o04024, '', 'OCT', '04024', kind='data', line=166)

W('30,2244', 0o05516, '', 'TC', 'DOWNFLAG', line=168)
W('30,2245', 0o00213, '', 'ADRES', 'FLPI', kind='data', line=169)

W('30,2246', 0o00004, '', 'INHINT', line=171)
W('30,2247', 0o04674, '', 'TC', 'IBNKCALL', line=172)
W('30,2250', 0o40142, '', 'CADR', 'PFLITEDB', kind='data', line=173)
W('30,2251', 0o00003, '', 'RELINT', line=174)

W('30,2252', 0o04635, '', 'TC', 'POSTJUMP', line=176)
W('30,2253', 0o74126, '', 'CADR', 'BURNBABY', kind='data', line=177)

W('30,2254', 0o77745, 'P12INIT', 'DLOAD', '', 'INITIALIZE ENGINE DATA.  USED FOR P12 AND', kind='interp', line=179)
# Page 841
W('30,2255', 0o16013, '', '', '(1/DV)A', 'P71.', kind='operand', line=181)
W('30,2256', 0o03641, '', 'STORE', '1/DV3', kind='interp', line=182)
W('30,2257', 0o03637, '', 'STORE', '1/DV2', kind='interp', line=183)
W('30,2260', 0o17635, '', 'STODL', '1/DV1', kind='interp', line=184)
W('30,2261', 0o16017, '', '', '(AT)A', kind='operand', line=185)
W('30,2262', 0o16263, '', 'STODL', 'AT', kind='interp', line=186)
W('30,2263', 0o16021, '', '', '(TBUP)A', kind='operand', line=187)
W('30,2264', 0o16271, '', 'STODL', 'TBUP', kind='interp', line=188)
W('30,2265', 0o34013, '', '', 'ATDECAY', kind='operand', line=189)
W('30,2266', 0o54276, '', 'DCOMP', 'SL', kind='interp', line=190)
W('30,2267', 0o20214, '', '', '11D', kind='operand', line=191)
W('30,2270', 0o02267, '', 'STORE', 'TTO', kind='interp', line=192)
W('30,2271', 0o57535, '', 'SLOAD', 'DCOMP', kind='interp', line=193)
W('30,2272', 0o26001, '', '', 'APSVEX', kind='operand', line=194)
W('30,2273', 0o77702, '', 'SR2', kind='interp', line=195)
W('30,2274', 0o02265, '', 'STORE', 'VE', kind='interp', line=196)
W('30,2275', 0o43414, '', 'BOFF', 'RVQ', kind='interp', line=197)
W('30,2276', 0o04747, '', '', 'FLAP', kind='operand', line=198)
W('30,2277', 0o60300, '', '', 'COMMINIT', kind='operand', line=199)
W('30,2300', 0o43345, 'COMMINIT', 'DLOAD', 'DAD', 'INITIALIZE TARGET DATA.  USED BY P12, P70', kind='interp', line=200)
W('30,2301', 0o25757, '', '', 'HINJECT', 'AND P71 IF IT DOES NOT FOLLOW P70.', kind='operand', line=201)
W('30,2302', 0o02333, '', '', '/LAND/', kind='operand', line=202)
W('30,2303', 0o17631, '', 'STODL', 'RCO', kind='interp', line=203)
W('30,2304', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=204)
W('30,2305', 0o03654, '', 'STORE', 'TXO', kind='interp', line=205)
W('30,2306', 0o03633, '', 'STORE', 'YCO', kind='interp', line=206)
W('30,2307', 0o02273, '', 'STORE', 'RDOTD', kind='interp', line=207)
W('30,2310', 0o26275, '', 'STOVL', 'YDOTD', kind='interp', line=208)
W('30,2311', 0o01563, '', '', 'VRECTCSM', kind='operand', line=209)
W('30,2312', 0o64235, '', 'VXV', 'MXV', kind='interp', line=210)
W('30,2313', 0o01555, '', '', 'RRECTCSM', kind='operand', line=211)
W('30,2314', 0o01734, '', '', 'REFSMMAT', kind='operand', line=212)
W('30,2315', 0o77656, '', 'UNIT', kind='interp', line=213)
W('30,2316', 0o03720, '', 'STORE', 'QAXIS', kind='interp', line=214)
W('30,2317', 0o77616, '', 'RVQ', kind='interp', line=215)
W('30,2320', 0o02022, 'P12ADRES', 'REMADR', 'P12TABLE', kind='data', line=216)

#   SETLOC P12A
#   BANK
#   COUNT* $$/P12

W('23,2432', 0o40220, 'GUIDINIT', 'STQ', 'SETPD', kind='interp', line=222)
W('23,2433', 0o01164, '', '', 'TEMPR60', kind='operand', line=223)
W('23,2434', 0o00001, '', '', '0D', kind='operand', line=224)
W('23,2435', 0o41575, '', 'VLOAD', 'PUSH', kind='interp', line=225)
W('23,2436', 0o06514, '', '', 'UNITZ', kind='operand', line=226)
W('23,2437', 0o41434, '', 'RTB', 'PUSH', kind='interp', line=227)
W('23,2440', 0o21573, '', '', 'LOADTIME', kind='operand', line=228)
W('23,2441', 0o77624, '', 'CALL', kind='interp', line=229)
W('23,2442', 0o55716, '', '', 'RP-TO-R', kind='operand', line=230)
# Page 842
W('23,2443', 0o74321, '', 'MXV', 'VXSC', kind='interp', line=232)
W('23,2444', 0o01734, '', '', 'REFSMMAT', kind='operand', line=233)
W('23,2445', 0o16027, '', '', 'MOONRATE', kind='operand', line=234)
W('23,2446', 0o26325, '', 'STOVL', 'WM', kind='interp', line=235)
W('23,2447', 0o02023, '', '', 'RLS', kind='operand', line=236)
W('23,2450', 0o52446, '', 'ABVAL', 'SL3', kind='interp', line=237)
W('23,2451', 0o36333, '', 'STCALL', '/LAND/', kind='interp', line=238)
W('23,2452', 0o01164, '', '', 'TEMPR60', kind='operand', line=239)

W('23,2453', 0o00046, '49FPS', '2DEC', '.149352 B-6', 'EXPECTED RDOT AT TIPOVER', kind='data', line=241)
W('23,2454', 0o07374, kind='data', line=241)
W('23,2455', 0o04145, 'VINJNOM', '2DEC', '16.7924 B-7', '5509.5 FPS(APO=30NM WITH RDOT=19.5FPS)', kind='data', line=242)
W('23,2456', 0o15527, kind='data', line=242)
W('23,2457', 0o00007, 'RDOTDNOM', '2DEC', '.059436 B-7', '19.5 FPS', kind='data', line=243)
W('23,2460', 0o23346, kind='data', line=243)
