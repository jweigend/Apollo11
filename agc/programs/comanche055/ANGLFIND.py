"""ANGLFIND.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/ANGLFIND.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 399-411 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('ANGLFIND', 'ANGLFIND.agc', 'Comanche055', pages='399-411')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     ANGLFIND.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        399-411
# Mod history:  2009-05-09 RSB  Adapted from the Colossus249/ file
# of the same name, using Comanche055 page
# images.
# 2009-05-22 RSB  In NOGOM2, TC ZEROEROR corrected to
# CADR ZEROEROR.
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

# Page 399
#   BANK 15
#   SETLOC KALCMON1
#   BANK

#   EBANK= BCDU

#   COUNT 22/KALC

W('22,2000', 0o06006, 'KALCMAN3', 'TC', 'INTPRET', line=42)
W('22,2001', 0o77634, '', 'RTB', kind='interp', line=43)
W('22,2002', 0o44376, '', '', 'READCDUK', 'PICK UP CURRENT CDU ANGLES', kind='operand', line=44)
W('22,2003', 0o03262, '', 'STORE', 'BCDU', 'STORE THE INITIAL S/C ANGLES', kind='interp', line=45)
W('22,2004', 0o72364, '', 'AXC,2', 'TLOAD', 'COMPUTE THE TRANSFORMATION FROM', kind='interp', line=46)
W('22,2005', 0o03320, '', '', 'MIS', 'INITIAL S/C AXES TO STABLE MEMBER AXES', kind='operand', line=47)
W('22,2006', 0o03262, '', '', 'BCDU', '(MIS)', kind='operand', line=48)
W('22,2007', 0o77624, '', 'CALL', kind='interp', line=49)
W('22,2010', 0o44405, '', '', 'CDUTODCM', kind='operand', line=50)
W('22,2011', 0o72364, '', 'AXC,2', 'TLOAD', 'COMPUTE THE TRANSFORMATION FROM', kind='interp', line=51)
W('22,2012', 0o03425, '', '', 'MFS', 'FINAL S/C AXES TO STABLE MEMBER AXES', kind='operand', line=52)
W('22,2013', 0o01156, '', '', 'CPHI', '(MFS)', kind='operand', line=53)
W('22,2014', 0o77624, '', 'CALL', kind='interp', line=54)
W('22,2015', 0o44405, '', '', 'CDUTODCM', kind='operand', line=55)
W('22,2016', 0o45160, 'SECAD', 'AXC,1', 'CALL', 'MIS AND MFS ARRAYS CALCULATED         $2', kind='interp', line=56)
W('22,2017', 0o03320, '', '', 'MIS', kind='operand', line=57)
W('22,2020', 0o44334, '', '', 'TRANSPOS', kind='operand', line=58)
W('22,2021', 0o77775, '', 'VLOAD', kind='interp', line=59)
W('22,2022', 0o77626, '', 'STADR', kind='interp', line=60)
W('22,2023', 0o50474, '', 'STOVL', 'TMIS +12D', kind='interp', line=61)
W('22,2024', 0o77626, '', 'STADR', kind='interp', line=62)
W('22,2025', 0o50502, '', 'STOVL', 'TMIS +6', kind='interp', line=63)
W('22,2026', 0o77626, '', 'STADR', kind='interp', line=64)
W('22,2027', 0o74510, '', 'STORE', 'TMIS', 'TMIS = TRANSPOSE(MIS) SCALED BY 2', kind='interp', line=65)
W('22,2030', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=66)
W('22,2031', 0o03266, '', '', 'TMIS', kind='operand', line=67)
W('22,2032', 0o03425, '', '', 'MFS', kind='operand', line=68)
W('22,2033', 0o77624, '', 'CALL', kind='interp', line=69)
W('22,2034', 0o44304, '', '', 'MXM3', kind='operand', line=70)
W('22,2035', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=71)
W('22,2036', 0o50335, '', 'STOVL', 'MFI +12D', kind='interp', line=72)
W('22,2037', 0o77626, '', 'STADR', kind='interp', line=73)
W('22,2040', 0o50343, '', 'STOVL', 'MFI +6', kind='interp', line=74)
W('22,2041', 0o77626, '', 'STADR', kind='interp', line=75)
W('22,2042', 0o74351, '', 'STORE', 'MFI', 'MFI = TMIS MFS (SCALED BY 4)', kind='interp', line=76)
W('22,2043', 0o45001, '', 'SETPD', 'CALL', 'TRANSPOSE MFI IN PD LIST', kind='interp', line=77)
W('22,2044', 0o00023, '', '', '18D', kind='operand', line=78)
W('22,2045', 0o44343, '', '', 'TRNSPSPD', kind='operand', line=79)
W('22,2046', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=80)
W('22,2047', 0o50474, '', 'STOVL', 'TMFI +12D', kind='interp', line=81)
W('22,2050', 0o77626, '', 'STADR', kind='interp', line=82)
W('22,2051', 0o50502, '', 'STOVL', 'TMFI +6', kind='interp', line=83)
# Page 400
W('22,2052', 0o77626, '', 'STADR', kind='interp', line=85)
W('22,2053', 0o74510, '', 'STORE', 'TMFI', 'TMFI = TRANSPOSE (MFI)  SCALED BY 4', kind='interp', line=86)

# CALCULATE COFSKEW AND MFISYM

W('22,2054', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=90)
W('22,2055', 0o03271, '', '', 'TMFI +2', kind='operand', line=91)
W('22,2056', 0o03430, '', '', 'MFI +2', kind='operand', line=92)
W('22,2057', 0o45325, '', 'PDDL', 'DSU', 'CALCULATE COF SCALED BY 2/SIN(AM)', kind='interp', line=93)
W('22,2060', 0o03432, '', '', 'MFI +4', kind='operand', line=94)
W('22,2061', 0o03273, '', '', 'TMFI +4', kind='operand', line=95)
W('22,2062', 0o45325, '', 'PDDL', 'DSU', kind='interp', line=96)
W('22,2063', 0o03301, '', '', 'TMFI +10D', kind='operand', line=97)
W('22,2064', 0o03440, '', '', 'MFI +10D', kind='operand', line=98)
W('22,2065', 0o77666, '', 'VDEF', kind='interp', line=99)
W('22,2066', 0o03311, '', 'STORE', 'COFSKEW', 'EQUALS MFISKEW', kind='interp', line=100)

# CALCULATE AM AND PROCEED ACCORDING TO ITS MAGNITUDE

W('22,2067', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=104)
W('22,2070', 0o03426, '', '', 'MFI', kind='operand', line=105)
W('22,2071', 0o03446, '', '', 'MFI +16D', kind='operand', line=106)
W('22,2072', 0o43225, '', 'DSU', 'DAD', kind='interp', line=107)
W('22,2073', 0o15325, '', '', 'DP1/4TH', kind='operand', line=108)
W('22,2074', 0o03436, '', '', 'MFI +8D', kind='operand', line=109)
W('22,2075', 0o03317, '', 'STORE', 'CAM', 'CAM = (MFI0+MFI4+MFI8-1)/2 HALF SCALE', kind='interp', line=110)
W('22,2076', 0o77726, '', 'ARCCOS', kind='interp', line=111)
W('22,2077', 0o03365, '', 'STORE', 'AM', 'AM=ARCCOS(CAM)  (AM SCALED BY 2)', kind='interp', line=112)
W('22,2100', 0o51025, '', 'DSU', 'BPL', kind='interp', line=113)
W('22,2101', 0o04367, '', '', 'MINANG', kind='operand', line=114)
W('22,2102', 0o44111, '', '', 'CHECKMAX', kind='operand', line=115)
W('22,2103', 0o77776, '', 'EXIT', '', 'MANEUVER LESS THAN 0.25 DEG', kind='interp', line=116)
W('22,2104', 0o00004, '', 'INHINT', '', 'GO DIRECTLY INTO ATTITUDE HOLD', line=117)
W('22,2105', 0o45017, '', 'CS', 'ONE', 'ABOUT COMMANDED ANGLES', line=118)
W('22,2106', 0o55332, '', 'TS', 'HOLDFLAG', 'NOGO WILL STOP ANY RATE AND SET UP FOR A', line=119)
W('22,2107', 0o03142, '', 'TC', 'LOADCDUD', 'GOOD RETURN', line=120)
W('22,2110', 0o12730, '', 'TCF', 'NOGO', line=121)

W('22,2111', 0o45345, 'CHECKMAX', 'DLOAD', 'DSU', kind='interp', line=123)
W('22,2112', 0o03365, '', '', 'AM', kind='operand', line=124)
W('22,2113', 0o04370, '', '', 'MAXANG', kind='operand', line=125)
W('22,2114', 0o77244, '', 'BPL', 'VLOAD', kind='interp', line=126)
W('22,2115', 0o44123, '', '', 'ALTCALC', 'UNIT', kind='operand', line=127)
W('22,2116', 0o03311, '', '', 'COFSKEW', 'COFSKEW', kind='operand', line=128)
W('22,2117', 0o77656, '', 'UNIT', kind='interp', line=129)
W('22,2120', 0o03343, '', 'STORE', 'COF', 'COF IS THE MANEUVER AXIS', kind='interp', line=130)
W('22,2121', 0o77650, '', 'GOTO', '', 'SEE IF MANEUVER GOES THRU GIMBAL LOCK', kind='interp', line=131)
W('22,2122', 0o44737, '', '', 'LOCSKIRT', kind='operand', line=132)
W('22,2123', 0o53375, 'ALTCALC', 'VLOAD', 'VAD', 'IF AM GREATER THAN 170 DEGREES', kind='interp', line=133)
W('22,2124', 0o03426, '', '', 'MFI', kind='operand', line=134)
# Page 401
W('22,2125', 0o03267, '', '', 'TMFI', kind='operand', line=136)
W('22,2126', 0o77762, '', 'VSR1', kind='interp', line=137)
W('22,2127', 0o27267, '', 'STOVL', 'MFISYM', kind='interp', line=138)
W('22,2130', 0o03434, '', '', 'MFI +6', kind='operand', line=139)
W('22,2131', 0o74455, '', 'VAD', 'VSR1', kind='interp', line=140)
W('22,2132', 0o03275, '', '', 'TMFI +6', kind='operand', line=141)
W('22,2133', 0o27275, '', 'STOVL', 'MFISYM +6', kind='interp', line=142)
W('22,2134', 0o03442, '', '', 'MFI +12D', kind='operand', line=143)
W('22,2135', 0o74455, '', 'VAD', 'VSR1', kind='interp', line=144)
W('22,2136', 0o03303, '', '', 'TMFI +12D', kind='operand', line=145)
W('22,2137', 0o03303, '', 'STORE', 'MFISYM +12D', 'MFISYM=(MFI+TMFI)/2   SCALED BY 4', kind='interp', line=146)

# CALCULATE COF

W('22,2140', 0o70545, '', 'DLOAD', 'SR1', kind='interp', line=150)
W('22,2141', 0o03317, '', '', 'CAM', kind='operand', line=151)
W('22,2142', 0o45325, '', 'PDDL', 'DSU', 'PD0 CAM                              $4', kind='interp', line=152)
W('22,2143', 0o15333, '', '', 'DPHALF', kind='operand', line=153)
W('22,2144', 0o03317, '', '', 'CAM', kind='operand', line=154)
W('22,2145', 0o65204, '', 'BOVB', 'PDDL', 'PD2 1 - CAM                          $2', kind='interp', line=155)
W('22,2146', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=156)
W('22,2147', 0o03307, '', '', 'MFISYM +16D', kind='operand', line=157)
W('22,2150', 0o56225, '', 'DSU', 'DDV', kind='interp', line=158)
W('22,2151', 0o00001, '', '', '0', kind='operand', line=159)
W('22,2152', 0o00003, '', '', '2', kind='operand', line=160)
W('22,2153', 0o65366, '', 'SQRT', 'PDDL', 'COFZ = SQRT(MFISYM8-CAM)/(1-CAM)', kind='interp', line=161)
W('22,2154', 0o03277, '', '', 'MFISYM +8D', '                               $ ROOT 2', kind='operand', line=162)
W('22,2155', 0o56225, '', 'DSU', 'DDV', kind='interp', line=163)
W('22,2156', 0o00001, '', '', '0', kind='operand', line=164)
W('22,2157', 0o00003, '', '', '2', kind='operand', line=165)
W('22,2160', 0o65366, '', 'SQRT', 'PDDL', 'COFY = SQRT(MFISYM4-CAM)/(1-CAM) $ROOT2', kind='interp', line=166)
W('22,2161', 0o03267, '', '', 'MFISYM', kind='operand', line=167)
W('22,2162', 0o56225, '', 'DSU', 'DDV', kind='interp', line=168)
W('22,2163', 0o00001, '', '', '0', kind='operand', line=169)
W('22,2164', 0o00003, '', '', '2', kind='operand', line=170)
W('22,2165', 0o55566, '', 'SQRT', 'VDEF', 'COFX = SQRT(MFISYM-CAM)/(1-CAM) $ROOT 2', kind='interp', line=171)
W('22,2166', 0o77656, '', 'UNIT', kind='interp', line=172)
W('22,2167', 0o03343, '', 'STORE', 'COF', kind='interp', line=173)

# DETERMINE LARGEST COF AND ADJUST ACCORDINGLY

W('22,2170', 0o45345, 'COFMAXGO', 'DLOAD', 'DSU', kind='interp', line=177)
W('22,2171', 0o03343, '', '', 'COF', kind='operand', line=178)
W('22,2172', 0o03345, '', '', 'COF +2', kind='operand', line=179)
W('22,2173', 0o71240, '', 'BMN', 'DLOAD', 'COFY G COFX', kind='interp', line=180)
W('22,2174', 0o44203, '', '', 'COMP12', kind='operand', line=181)
W('22,2175', 0o03343, '', '', 'COF', kind='operand', line=182)
W('22,2176', 0o50025, '', 'DSU', 'BMN', kind='interp', line=183)
W('22,2177', 0o03347, '', '', 'COF +4', kind='operand', line=184)
# Page 402
W('22,2200', 0o44260, '', '', 'METHOD3', 'COFZ G COFX OR COFY', kind='operand', line=186)
W('22,2201', 0o77650, '', 'GOTO', kind='interp', line=187)
W('22,2202', 0o44234, '', '', 'METHOD1', 'COFX G COFY OR COFZ', kind='operand', line=188)
W('22,2203', 0o45345, 'COMP12', 'DLOAD', 'DSU', kind='interp', line=189)
W('22,2204', 0o03345, '', '', 'COF +2', kind='operand', line=190)
W('22,2205', 0o03347, '', '', 'COF +4', kind='operand', line=191)
W('22,2206', 0o77640, '', 'BMN', kind='interp', line=192)
W('22,2207', 0o44260, '', '', 'METHOD3', 'COFZ G COFY OR COFX', kind='operand', line=193)

W('22,2210', 0o51145, 'METHOD2', 'DLOAD', 'BPL', 'COFY MAX', kind='interp', line=195)
W('22,2211', 0o03313, '', '', 'COFSKEW +2', 'UY', kind='operand', line=196)
W('22,2212', 0o44216, '', '', 'U2POS', kind='operand', line=197)
W('22,2213', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=198)
W('22,2214', 0o03343, '', '', 'COF', kind='operand', line=199)
W('22,2215', 0o03343, '', 'STORE', 'COF', kind='interp', line=200)
W('22,2216', 0o51145, 'U2POS', 'DLOAD', 'BPL', kind='interp', line=201)
W('22,2217', 0o03271, '', '', 'MFISYM +2', 'UX UY', kind='operand', line=202)
W('22,2220', 0o44224, '', '', 'OKU21', kind='operand', line=203)
W('22,2221', 0o57545, '', 'DLOAD', 'DCOMP', 'SIGN OF UX OPPOSITE TO UY', kind='interp', line=204)
W('22,2222', 0o03343, '', '', 'COF', kind='operand', line=205)
W('22,2223', 0o03343, '', 'STORE', 'COF', kind='interp', line=206)
W('22,2224', 0o51145, 'OKU21', 'DLOAD', 'BPL', kind='interp', line=207)
W('22,2225', 0o03301, '', '', 'MFISYM +10D', 'UY UZ', kind='operand', line=208)
W('22,2226', 0o44737, '', '', 'LOCSKIRT', kind='operand', line=209)
W('22,2227', 0o57545, '', 'DLOAD', 'DCOMP', 'SIGN OF UZ OPPOSITE TO UY', kind='interp', line=210)
W('22,2230', 0o03347, '', '', 'COF +4', kind='operand', line=211)
W('22,2231', 0o03347, '', 'STORE', 'COF +4', kind='interp', line=212)
W('22,2232', 0o77650, '', 'GOTO', kind='interp', line=213)
W('22,2233', 0o44737, '', '', 'LOCSKIRT', kind='operand', line=214)
W('22,2234', 0o51145, 'METHOD1', 'DLOAD', 'BPL', 'COFX MAX', kind='interp', line=215)
W('22,2235', 0o03311, '', '', 'COFSKEW', 'UX', kind='operand', line=216)
W('22,2236', 0o44242, '', '', 'U1POS', kind='operand', line=217)
W('22,2237', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=218)
W('22,2240', 0o03343, '', '', 'COF', kind='operand', line=219)
W('22,2241', 0o03343, '', 'STORE', 'COF', kind='interp', line=220)
W('22,2242', 0o51145, 'U1POS', 'DLOAD', 'BPL', kind='interp', line=221)
W('22,2243', 0o03271, '', '', 'MFISYM +2', 'UX UY', kind='operand', line=222)
W('22,2244', 0o44250, '', '', 'OKU12', kind='operand', line=223)
W('22,2245', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=224)
W('22,2246', 0o03345, '', '', 'COF +2', 'SIGN OF UY OPPOSITE TO UX', kind='operand', line=225)
W('22,2247', 0o03345, '', 'STORE', 'COF +2', kind='interp', line=226)
W('22,2250', 0o51145, 'OKU12', 'DLOAD', 'BPL', kind='interp', line=227)
W('22,2251', 0o03273, '', '', 'MFISYM +4', 'UX UZ', kind='operand', line=228)
W('22,2252', 0o44737, '', '', 'LOCSKIRT', kind='operand', line=229)
W('22,2253', 0o57545, '', 'DLOAD', 'DCOMP', 'SIGN OF UZ OPPOSITE TO UY', kind='interp', line=230)
W('22,2254', 0o03347, '', '', 'COF +4', kind='operand', line=231)
W('22,2255', 0o03347, '', 'STORE', 'COF +4', kind='interp', line=232)
W('22,2256', 0o77650, '', 'GOTO', kind='interp', line=233)
W('22,2257', 0o44737, '', '', 'LOCSKIRT', kind='operand', line=234)
W('22,2260', 0o51145, 'METHOD3', 'DLOAD', 'BPL', 'COFZ MAX', kind='interp', line=235)
# Page 403
W('22,2261', 0o03315, '', '', 'COFSKEW +4', 'UZ', kind='operand', line=237)
W('22,2262', 0o44266, '', '', 'U3POS', kind='operand', line=238)
W('22,2263', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=239)
W('22,2264', 0o03343, '', '', 'COF', kind='operand', line=240)
W('22,2265', 0o03343, '', 'STORE', 'COF', kind='interp', line=241)
W('22,2266', 0o51145, 'U3POS', 'DLOAD', 'BPL', kind='interp', line=242)
W('22,2267', 0o03273, '', '', 'MFISYM +4', 'UX UZ', kind='operand', line=243)
W('22,2270', 0o44274, '', '', 'OKU31', kind='operand', line=244)
W('22,2271', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=245)
W('22,2272', 0o03343, '', '', 'COF', 'SIGN OF UX OPPOSITE TO UZ', kind='operand', line=246)
W('22,2273', 0o03343, '', 'STORE', 'COF', kind='interp', line=247)
W('22,2274', 0o51145, 'OKU31', 'DLOAD', 'BPL', kind='interp', line=248)
W('22,2275', 0o03301, '', '', 'MFISYM +10D', 'UY UZ', kind='operand', line=249)
W('22,2276', 0o44737, '', '', 'LOCSKIRT', kind='operand', line=250)
W('22,2277', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=251)
W('22,2300', 0o03345, '', '', 'COF +2', 'SIGN OF UY OPPOSITE TO UZ', kind='operand', line=252)
W('22,2301', 0o03345, '', 'STORE', 'COF +2', kind='interp', line=253)
W('22,2302', 0o77650, '', 'GOTO', kind='interp', line=254)
W('22,2303', 0o44737, '', '', 'LOCSKIRT', kind='operand', line=255)

# Page 404
# MATRIX OPERATIONS

W('22,2304', 0o77601, 'MXM3', 'SETPD', '', 'MXM3 MULTIPLIES 2 3X3 MATRICES', kind='interp', line=260)
W('22,2305', 0o00001, '', '', '0', 'AND LEAVES RESULT IN PD LIST', kind='operand', line=261)
W('22,2306', 0o64743, '', 'DLOAD*', 'PDDL*', 'ADDRESS OF 1ST MATRIX IN XR1', kind='interp', line=262)
W('22,2307', 0o77762, '', '', '12D,2', 'ADDRESS OF 2ND MATRIX IN XR2', kind='operand', line=263)
W('22,2310', 0o77770, '', '', '6,2', kind='operand', line=264)
W('22,2311', 0o55523, '', 'PDDL*', 'VDEF', 'DEFINE VECTOR M2(COL 1)', kind='interp', line=265)
W('22,2312', 0o77776, '', '', '0,2', kind='operand', line=266)
W('22,2313', 0o64717, '', 'MXV*', 'PDDL*', 'M1XM2(COL 1) IN PD', kind='interp', line=267)
W('22,2314', 0o00001, '', '', '0,1', kind='operand', line=268)
W('22,2315', 0o77760, '', '', '14D,2', kind='operand', line=269)
W('22,2316', 0o64723, '', 'PDDL*', 'PDDL*', kind='interp', line=270)
W('22,2317', 0o77766, '', '', '8D,2', kind='operand', line=271)
W('22,2320', 0o77774, '', '', '2,2', kind='operand', line=272)
W('22,2321', 0o63666, '', 'VDEF', 'MXV*', 'DEFINE VECTOR M2(COL 2)', kind='interp', line=273)
W('22,2322', 0o00001, '', '', '0,1', kind='operand', line=274)
W('22,2323', 0o64723, '', 'PDDL*', 'PDDL*', 'M1XM2(COL 2) IN PD', kind='interp', line=275)
W('22,2324', 0o77756, '', '', '16D,2', kind='operand', line=276)
W('22,2325', 0o77764, '', '', '10D,2', kind='operand', line=277)
W('22,2326', 0o55523, '', 'PDDL*', 'VDEF', 'DEFINE VECTOR M2(COL 3)', kind='interp', line=278)
W('22,2327', 0o77772, '', '', '4,2', kind='operand', line=279)
W('22,2330', 0o41517, '', 'MXV*', 'PUSH', 'M1XM2(COL 3) IN PD', kind='interp', line=280)
W('22,2331', 0o00001, '', '', '0,1', kind='operand', line=281)
W('22,2332', 0o77650, '', 'GOTO', kind='interp', line=282)
W('22,2333', 0o44343, '', '', 'TRNSPSPD', 'REVERSE ROWS AND COLS IN PD AND', kind='operand', line=283)
# RETURN WITH M1XM2 IN PD LIST

W('22,2334', 0o76601, 'TRANSPOS', 'SETPD', 'VLOAD*', 'TRANSPOS TRANSPOSES A 3X3 MATRIX', kind='interp', line=286)
W('22,2335', 0o00001, '', '', '0', ' AND LEAVES RESULT IN PD LIST', kind='operand', line=287)
W('22,2336', 0o00001, '', '', '0,1', 'MATRIX ADDRESS IN XR1', kind='operand', line=288)
W('22,2337', 0o62713, '', 'PDVL*', 'PDVL*', kind='interp', line=289)
W('22,2340', 0o00007, '', '', '6,1', kind='operand', line=290)
W('22,2341', 0o00015, '', '', '12D,1', kind='operand', line=291)
W('22,2342', 0o77606, '', 'PUSH', '', 'MATRIX IN PD', kind='interp', line=292)
W('22,2343', 0o65345, 'TRNSPSPD', 'DLOAD', 'PDDL', 'ENTER WITH MATRIX IN PD LIST', kind='interp', line=293)
W('22,2344', 0o00003, '', '', '2', kind='operand', line=294)
W('22,2345', 0o00007, '', '', '6', kind='operand', line=295)
W('22,2346', 0o14003, '', 'STODL', '2', kind='interp', line=296)
W('22,2347', 0o77626, '', 'STADR', kind='interp', line=297)
W('22,2350', 0o63770, '', 'STODL', '6', kind='interp', line=298)
W('22,2351', 0o00005, '', '', '4', kind='operand', line=299)
W('22,2352', 0o77725, '', 'PDDL', kind='interp', line=300)
W('22,2353', 0o00015, '', '', '12D', kind='operand', line=301)
W('22,2354', 0o14005, '', 'STODL', '4', kind='interp', line=302)
W('22,2355', 0o77626, '', 'STADR', kind='interp', line=303)
W('22,2356', 0o63762, '', 'STODL', '12D', kind='interp', line=304)
W('22,2357', 0o00013, '', '', '10D', kind='operand', line=305)
W('22,2360', 0o77725, '', 'PDDL', kind='interp', line=306)
# Page 405
W('22,2361', 0o00017, '', '', '14D', kind='operand', line=308)
W('22,2362', 0o14013, '', 'STODL', '10D', kind='interp', line=309)
W('22,2363', 0o77626, '', 'STADR', kind='interp', line=310)
W('22,2364', 0o77760, '', 'STORE', '14D', kind='interp', line=311)
W('22,2365', 0o77616, '', 'RVQ', '', 'RETURN WITH TRANSPOSED MATRIX IN PD LIST', kind='interp', line=312)
W('22,2366', 0o00013, 'MINANG', 'DEC', '.00069375', kind='data', line=313)
W('22,2367', 0o17071, 'MAXANG', 'DEC', '.472222', kind='data', line=314)
# GIMBAL LOCK CONSTANTS

# D = MGA CORRESPONDING TO GIMBAL LOCK = 60 DEGREES
# NGL = BUFFER ANGLE (TO AVOID DIVISIONS BY ZERO) = 2 DEGREES

W('22,2370', 0o15667, 'SD', 'DEC', '.433015', '= SIN(D)                              $2', kind='data', line=320)
W('22,2371', 0o33555, 'K3S1', 'DEC', '.86603', '= SIN(D)                              $2', kind='data', line=321)
W('22,2372', 0o67777, 'K4', 'DEC', '-.25', '= - COS(D)                            $2', kind='data', line=322)
W('22,2373', 0o04000, 'K4SQ', 'DEC', '.125', '= COS(D)COS(D)                        $2', kind='data', line=323)
W('22,2374', 0o00217, 'SNGLCD', 'DEC', '.008725', '= SIN(NGL)COS(D)                      $2', kind='data', line=324)
W('22,2375', 0o17773, 'CNGL', 'DEC', '.499695', '= COS(NGL)                            $2', kind='data', line=325)
W('22,2376', 0o00004, 'READCDUK', 'INHINT', '', 'LOAD T(MPAC) WITH THE CURRENT CDU ANGLES', line=326)
W('22,2377', 0o30034, '', 'CA', 'CDUZ', line=327)
W('22,2400', 0o54156, '', 'TS', 'MPAC +2', line=328)
W('22,2401', 0o00006, '', 'EXTEND', line=329)
W('22,2402', 0o30033, '', 'DCA', 'CDUX', line=330)
W('22,2403', 0o00003, '', 'RELINT', line=331)
W('22,2404', 0o16445, '', 'TCF', 'TLOAD +6', line=332)
#   BANK 16
#   SETLOC KALCMON2
#   BANK

#   COUNT* $$/KALC

W('22,2405', 0o66370, 'CDUTODCM', 'AXT,1', 'SSP', 'SUBROUTINE TO COMPUTE  DIRECTION COSINE', kind='interp', line=339)
W('22,2406', 0o00003, '', 'OCT', '3', 'MATRIX RELATING S/C AXES TO STABLE', kind='data', line=340)
W('22,2407', 0o00051, '', '', 'S1', 'MEMBER AXES FROM 3 CDU ANGLES IN T(MPAC)', kind='operand', line=341)
W('22,2410', 0o00001, '', 'OCT', '1', 'SET XR1, S1 AND PD FOR LOOP', kind='data', line=342)
W('22,2411', 0o00010, '', 'STORE', '7', kind='interp', line=343)
W('22,2412', 0o77601, '', 'SETPD', kind='interp', line=344)
W('22,2413', 0o00001, '', '', '0', kind='operand', line=345)
W('22,2414', 0o47133, 'LOOPSIN', 'SLOAD*', 'RTB', kind='interp', line=346)
W('22,2415', 0o00013, '', '', '10D,1', kind='operand', line=347)
W('22,2416', 0o45513, '', '', 'CDULOGIC', kind='operand', line=348)
W('22,2417', 0o00013, '', 'STORE', '10D', 'LOAD PD WITH 0 SIN(PHI)', kind='interp', line=349)
W('22,2420', 0o65356, '', 'SIN', 'PDDL', '             2 COS(PHI)', kind='interp', line=350)
W('22,2421', 0o00013, '', '', '10D', '             4 SIN(THETA)', kind='operand', line=351)
W('22,2422', 0o41546, '', 'COS', 'PUSH', '             6 COS(THETA)', kind='interp', line=352)
W('22,2423', 0o71300, '', 'TIX,1', 'DLOAD', '             8 SIN(PSI)', kind='interp', line=353)
W('22,2424', 0o44414, '', '', 'LOOPSIN', '            10 COS(PSI)', kind='operand', line=354)
W('22,2425', 0o00007, '', '', '6', kind='operand', line=355)
W('22,2426', 0o72405, '', 'DMP', 'SL1', kind='interp', line=356)
W('22,2427', 0o00013, '', '', '10D', kind='operand', line=357)
# Page 406
W('22,2430', 0o10001, '', 'STORE', '0,2', kind='interp', line=359)
W('22,2431', 0o77745, '', 'DLOAD', kind='interp', line=360)
W('22,2432', 0o00005, '', '', '4', kind='operand', line=361)
W('22,2433', 0o65205, '', 'DMP', 'PDDL', kind='interp', line=362)
W('22,2434', 0o00001, '', '', '0', '(PD6 SIN(THETA)SIN(PHI))', kind='operand', line=363)
W('22,2435', 0o00007, '', '', '6', kind='operand', line=364)
W('22,2436', 0o41205, '', 'DMP', 'DMP', kind='interp', line=365)
W('22,2437', 0o00011, '', '', '8D', kind='operand', line=366)
W('22,2440', 0o00003, '', '', '2', kind='operand', line=367)
W('22,2441', 0o44352, '', 'SL1', 'BDSU', kind='interp', line=368)
W('22,2442', 0o00015, '', '', '12D', kind='operand', line=369)
W('22,2443', 0o77752, '', 'SL1', kind='interp', line=370)
W('22,2444', 0o10003, '', 'STORE', '2,2', kind='interp', line=371)
W('22,2445', 0o77745, '', 'DLOAD', kind='interp', line=372)
W('22,2446', 0o00003, '', '', '2', kind='operand', line=373)
W('22,2447', 0o65205, '', 'DMP', 'PDDL', '(PD7 COS(PHI)SIN(THETA)) SCALED 4', kind='interp', line=374)
W('22,2450', 0o00005, '', '', '4', kind='operand', line=375)
W('22,2451', 0o00007, '', '', '6', kind='operand', line=376)
W('22,2452', 0o41205, '', 'DMP', 'DMP', kind='interp', line=377)
W('22,2453', 0o00011, '', '', '8D', kind='operand', line=378)
W('22,2454', 0o00001, '', '', '0', kind='operand', line=379)
W('22,2455', 0o77752, '', 'SL1', kind='interp', line=380)
W('22,2456', 0o72415, '', 'DAD', 'SL1', kind='interp', line=381)
W('22,2457', 0o00017, '', '', '14D', kind='operand', line=382)
W('22,2460', 0o10005, '', 'STORE', '4,2', kind='interp', line=383)
W('22,2461', 0o77745, '', 'DLOAD', kind='interp', line=384)
W('22,2462', 0o00011, '', '', '8D', kind='operand', line=385)
W('22,2463', 0o10007, '', 'STORE', '6,2', kind='interp', line=386)
W('22,2464', 0o77745, '', 'DLOAD', kind='interp', line=387)
W('22,2465', 0o00013, '', '', '10D', kind='operand', line=388)
W('22,2466', 0o72405, '', 'DMP', 'SL1', kind='interp', line=389)
W('22,2467', 0o00003, '', '', '2', kind='operand', line=390)
W('22,2470', 0o10011, '', 'STORE', '8D,2', kind='interp', line=391)
W('22,2471', 0o77745, '', 'DLOAD', kind='interp', line=392)
W('22,2472', 0o00013, '', '', '10D', kind='operand', line=393)
W('22,2473', 0o57405, '', 'DMP', 'DCOMP', kind='interp', line=394)
W('22,2474', 0o00001, '', '', '0', kind='operand', line=395)
W('22,2475', 0o77752, '', 'SL1', kind='interp', line=396)
W('22,2476', 0o10013, '', 'STORE', '10D,2', kind='interp', line=397)
W('22,2477', 0o77745, '', 'DLOAD', kind='interp', line=398)
W('22,2500', 0o00005, '', '', '4', kind='operand', line=399)
W('22,2501', 0o57405, '', 'DMP', 'DCOMP', kind='interp', line=400)
W('22,2502', 0o00013, '', '', '10D', kind='operand', line=401)
W('22,2503', 0o77752, '', 'SL1', kind='interp', line=402)
W('22,2504', 0o10015, '', 'STORE', '12D,2', kind='interp', line=403)
W('22,2505', 0o77745, '', 'DLOAD', kind='interp', line=404)
W('22,2506', 0o72405, '', 'DMP', 'SL1', '(PUSH UP 7)', kind='interp', line=405)
W('22,2507', 0o00011, '', '', '8D', kind='operand', line=406)
W('22,2510', 0o41325, '', 'PDDL', 'DMP', '(PD7 COS(PHI)SIN(THETA)SIN(PSI)) SCALE4', kind='interp', line=407)
W('22,2511', 0o00007, '', '', '6', kind='operand', line=408)
# Page 407
W('22,2512', 0o00001, '', '', '0', kind='operand', line=410)
W('22,2513', 0o72415, '', 'DAD', 'SL1', ' (PUSH UP 7)', kind='interp', line=411)
W('22,2514', 0o77626, '', 'STADR', '', 'C7=COS(PHI)SIN(THETA)SIN(PSI)', kind='interp', line=412)
W('22,2515', 0o67760, '', 'STORE', '14D,2', kind='interp', line=413)
W('22,2516', 0o77745, '', 'DLOAD', kind='interp', line=414)
W('22,2517', 0o72405, '', 'DMP', 'SL1', ' (PUSH UP 6)', kind='interp', line=415)
W('22,2520', 0o00011, '', '', '8D', kind='operand', line=416)
W('22,2521', 0o41325, '', 'PDDL', 'DMP', ' (PD6 SIN(THETA)SIN(PHI)SIN(PSI)) SCALE4', kind='interp', line=417)
W('22,2522', 0o00007, '', '', '6', kind='operand', line=418)
W('22,2523', 0o00003, '', '', '2', kind='operand', line=419)
W('22,2524', 0o72425, '', 'DSU', 'SL1', ' (PUSH UP 6)', kind='interp', line=420)
W('22,2525', 0o77626, '', 'STADR', kind='interp', line=421)
W('22,2526', 0o67756, '', 'STORE', '16D,2', 'C8=-SIN(THETA)SIN(PHI)SIN(PSI)', kind='interp', line=422)
W('22,2527', 0o77616, '', 'RVQ', '', ' +COS(THETA)COS(PHI)', kind='interp', line=423)
S('ENDOCM', 'equals', 0o54530, line=424)

#   BANK 15
#   SETLOC KALCMON1
#   BANK

# CALCULATION OF THE MATRIX DEL......
#
# *      *               --T           *
# DEL = (IDMATRIX)COS(A)+UU (1-COS(A))+UX SIN(A)          SCALED 1
#
# -
# WHERE U IS A UNIT VECTOR (DP SCALED 2) ALONG THE AXIS OF ROTATION.
# A IS THE ANGLE OF ROTATION (DP SCALED 2)
# -
# UPON ENTRY THE STARTING ADDRESS OF U IS COF, AND A IS IN MPAC

#   COUNT 22/KALC

W('22,2530', 0o41401, 'DELCOMP', 'SETPD', 'PUSH', 'MPAC CONTAINS THE ANGLE A', kind='interp', line=443)
W('22,2531', 0o00001, '', '', '0', kind='operand', line=444)
W('22,2532', 0o65356, '', 'SIN', 'PDDL', 'PD0 = SIN(A)', kind='interp', line=445)
W('22,2533', 0o41546, '', 'COS', 'PUSH', 'PD2 = COS(A)', kind='interp', line=446)
W('22,2534', 0o65302, '', 'SR2', 'PDDL', 'PD2 = COS(A)                          $8', kind='interp', line=447)
W('22,2535', 0o41021, '', 'BDSU', 'BOVB', 'PD4 = 1-COS(A)                        $2', kind='interp', line=448)
W('22,2536', 0o15333, '', '', 'DPHALF', kind='operand', line=449)
W('22,2537', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=450)

# COMPUTE THE DIAGONAL COMPONENTS OF DEL

W('22,2540', 0o77725, '', 'PDDL', kind='interp', line=454)
W('22,2541', 0o03343, '', '', 'COF', kind='operand', line=455)
W('22,2542', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=456)
W('22,2543', 0o00005, '', '', '4', kind='operand', line=457)
W('22,2544', 0o52415, '', 'DAD', 'SL3', kind='interp', line=458)
# Page 408
W('22,2545', 0o00003, '', '', '2', kind='operand', line=460)
W('22,2546', 0o77604, '', 'BOVB', kind='interp', line=461)
W('22,2547', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=462)
W('22,2550', 0o17426, '', 'STODL', 'DEL', 'UX UX(U-COS(A)) +COS(A)               $1', kind='interp', line=463)
W('22,2551', 0o03345, '', '', 'COF +2', kind='operand', line=464)
W('22,2552', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=465)
W('22,2553', 0o00005, '', '', '4', kind='operand', line=466)
W('22,2554', 0o52415, '', 'DAD', 'SL3', kind='interp', line=467)
W('22,2555', 0o00003, '', '', '2', kind='operand', line=468)
W('22,2556', 0o77604, '', 'BOVB', kind='interp', line=469)
W('22,2557', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=470)
W('22,2560', 0o17436, '', 'STODL', 'DEL +8D', 'UY UY(1-COS(A)) +COS(A)               $1', kind='interp', line=471)
W('22,2561', 0o03347, '', '', 'COF +4', kind='operand', line=472)
W('22,2562', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=473)
W('22,2563', 0o00005, '', '', '4', kind='operand', line=474)
W('22,2564', 0o52415, '', 'DAD', 'SL3', kind='interp', line=475)
W('22,2565', 0o00003, '', '', '2', kind='operand', line=476)
W('22,2566', 0o77604, '', 'BOVB', kind='interp', line=477)
W('22,2567', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=478)
W('22,2570', 0o03446, '', 'STORE', 'DEL +16D', 'UZ UZ(1-COS(A)) +COS(A)               $1', kind='interp', line=479)

# COMPUTE THE OFF DIAGONAL TERMS OF DEL

W('22,2571', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=483)
W('22,2572', 0o03343, '', '', 'COF', kind='operand', line=484)
W('22,2573', 0o03345, '', '', 'COF +2', kind='operand', line=485)
W('22,2574', 0o72405, '', 'DMP', 'SL1', kind='interp', line=486)
W('22,2575', 0o00005, '', '', '4', kind='operand', line=487)
W('22,2576', 0o41325, '', 'PDDL', 'DMP', 'D6  UX UY (1-COS A)                   $ 4', kind='interp', line=488)
W('22,2577', 0o03347, '', '', 'COF +4', kind='operand', line=489)
W('22,2600', 0o00001, '', '', '0', kind='operand', line=490)
W('22,2601', 0o43206, '', 'PUSH', 'DAD', 'D8  UZ SIN A                          $ 4', kind='interp', line=491)
W('22,2602', 0o00007, '', '', '6', kind='operand', line=492)
W('22,2603', 0o41112, '', 'SL2', 'BOVB', kind='interp', line=493)
W('22,2604', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=494)
W('22,2605', 0o17434, '', 'STODL', 'DEL +6', kind='interp', line=495)
W('22,2606', 0o62421, '', 'BDSU', 'SL2', kind='interp', line=496)
W('22,2607', 0o77604, '', 'BOVB', kind='interp', line=497)
W('22,2610', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=498)
W('22,2611', 0o17430, '', 'STODL', 'DEL +2', kind='interp', line=499)
W('22,2612', 0o03343, '', '', 'COF', kind='operand', line=500)
W('22,2613', 0o41205, '', 'DMP', 'DMP', kind='interp', line=501)
W('22,2614', 0o03347, '', '', 'COF +4', kind='operand', line=502)
W('22,2615', 0o00005, '', '', '4', kind='operand', line=503)
W('22,2616', 0o65352, '', 'SL1', 'PDDL', 'D6  UX UZ (1-COS A )          $ 4', kind='interp', line=504)
W('22,2617', 0o03345, '', '', 'COF +2', kind='operand', line=505)
W('22,2620', 0o41405, '', 'DMP', 'PUSH', 'D8  UY SIN(A)', kind='interp', line=506)
W('22,2621', 0o00001, '', '', '0', kind='operand', line=507)
W('22,2622', 0o62415, '', 'DAD', 'SL2', kind='interp', line=508)
W('22,2623', 0o00007, '', '', '6', kind='operand', line=509)
# Page 409
W('22,2624', 0o77604, '', 'BOVB', kind='interp', line=511)
W('22,2625', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=512)
W('22,2626', 0o17432, '', 'STODL', 'DEL +4', 'UX UZ (1-COS(A))+UY SIN(A)', kind='interp', line=513)
W('22,2627', 0o62421, '', 'BDSU', 'SL2', kind='interp', line=514)
W('22,2630', 0o77604, '', 'BOVB', kind='interp', line=515)
W('22,2631', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=516)
W('22,2632', 0o17442, '', 'STODL', 'DEL +12D', 'UX UZ (U-COS(A))-UY SIN(A)', kind='interp', line=517)
W('22,2633', 0o03345, '', '', 'COF +2', kind='operand', line=518)
W('22,2634', 0o41205, '', 'DMP', 'DMP', kind='interp', line=519)
W('22,2635', 0o03347, '', '', 'COF +4', kind='operand', line=520)
W('22,2636', 0o00005, '', '', '4', kind='operand', line=521)
W('22,2637', 0o65352, '', 'SL1', 'PDDL', 'D6  UY UZ (1-COS(A))          $ 4', kind='interp', line=522)
W('22,2640', 0o03343, '', '', 'COF', kind='operand', line=523)
W('22,2641', 0o41405, '', 'DMP', 'PUSH', 'D6  UX SIN(A)', kind='interp', line=524)
W('22,2642', 0o00001, '', '', '0', kind='operand', line=525)
W('22,2643', 0o62415, '', 'DAD', 'SL2', kind='interp', line=526)
W('22,2644', 0o00007, '', '', '6', kind='operand', line=527)
W('22,2645', 0o77604, '', 'BOVB', kind='interp', line=528)
W('22,2646', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=529)
W('22,2647', 0o17444, '', 'STODL', 'DEL +14D', 'UY UZ(1-COS(A)) +UX SIN(A)', kind='interp', line=530)
W('22,2650', 0o62421, '', 'BDSU', 'SL2', kind='interp', line=531)
W('22,2651', 0o77604, '', 'BOVB', kind='interp', line=532)
W('22,2652', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=533)
W('22,2653', 0o03440, '', 'STORE', 'DEL +10D', 'UY UZ (1-COS(A)) -UX SIN(A)', kind='interp', line=534)
W('22,2654', 0o77616, '', 'RVQ', kind='interp', line=535)

# DIRECTION COSINE MATRIX TO CDU ANGLE ROUTINE
# X1 CONTAINS THE COMPLEMENT OF THE STARTING ADDRESS FOR MATRIX (SCALED 2)
# LEAVES CDU ANGLES SCALED 2PI IN V(MPAC)
# COS(MGA) WILL BE LEFT IN S1 (SCALED 1)
#
# THE DIRECTION COSINE MATRIX RELATING S/C AXES TO STABLE MEMBER AXES CAN BE WRITTEN AS***
#
# C =COS(THETA)COS(PSI)
# 0
# C =-COS(THETA)SIN(PSI)COS(PHI)+SI (THETA)SIN(PHI)
# 1
# C =COS(THETA)SIN(PSI)SIN(PHI) + S N(THETA)COS(PHI)
# 2
# C =SIN(PSI)
# 3
# C =COS(PSI)COS(PHI)
# 4
# C =-COS(PSI)SIN(PHI)
# 5
# C =-SIN(THETA)COS(PSI)
# 6
# C =SIN(THETA)SIN(PSI)COS(PHI)+COS THETA)SIN(PHI)
# 7
# Page 410
# C =-SIN(THETA)SIN(PSI)SIN(PHI)+COS(THETA)COS(PHI)
# 8
#
# WHERE   PHI = OGA
# THETA = IGA
# PSI = MGA

W('22,2655', 0o67543, 'DCMTOCDU', 'DLOAD*', 'ARCSIN', kind='interp', line=568)
W('22,2656', 0o00007, '', '', '6,1', kind='operand', line=569)
W('22,2657', 0o71406, '', 'PUSH', 'COS', 'PD +0         PSI', kind='interp', line=570)
W('22,2660', 0o41152, '', 'SL1', 'BOVB', kind='interp', line=571)
W('22,2661', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=572)
W('22,2662', 0o00051, '', 'STORE', 'S1', kind='interp', line=573)
W('22,2663', 0o57543, '', 'DLOAD*', 'DCOMP', kind='interp', line=574)
W('22,2664', 0o00015, '', '', '12D,1', kind='operand', line=575)
W('22,2665', 0o67471, '', 'DDV', 'ARCSIN', kind='interp', line=576)
W('22,2666', 0o00051, '', '', 'S1', kind='operand', line=577)
W('22,2667', 0o51123, '', 'PDDL*', 'BPL', 'PD +2         THETA', kind='interp', line=578)
W('22,2670', 0o00001, '', '', '0,1', 'MUST CHECK THE SIGN OF COS(THETA)', kind='operand', line=579)
W('22,2671', 0o44703, '', '', 'OKTHETA', 'TO DETERMINE THE PROPER QUADRANT', kind='operand', line=580)
W('22,2672', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=581)
W('22,2673', 0o43244, '', 'BPL', 'DAD', kind='interp', line=582)
W('22,2674', 0o44700, '', '', 'SUHALFA', kind='operand', line=583)
W('22,2675', 0o15333, '', '', 'DPHALF', kind='operand', line=584)
W('22,2676', 0o77650, '', 'GOTO', kind='interp', line=585)
W('22,2677', 0o44702, '', '', 'CALCPHI', kind='operand', line=586)
W('22,2700', 0o77625, 'SUHALFA', 'DSU', kind='interp', line=587)
W('22,2701', 0o15333, '', '', 'DPHALF', kind='operand', line=588)
W('22,2702', 0o77606, 'CALCPHI', 'PUSH', kind='interp', line=589)
W('22,2703', 0o57543, 'OKTHETA', 'DLOAD*', 'DCOMP', kind='interp', line=590)
W('22,2704', 0o00013, '', '', '10D,1', kind='operand', line=591)
W('22,2705', 0o67471, '', 'DDV', 'ARCSIN', kind='interp', line=592)
W('22,2706', 0o00051, '', '', 'S1', kind='operand', line=593)
W('22,2707', 0o51123, '', 'PDDL*', 'BPL', 'PUSH DOWN PHI', kind='interp', line=594)
W('22,2710', 0o00011, '', '', '8D,1', kind='operand', line=595)
W('22,2711', 0o44723, '', '', 'OKPHI', kind='operand', line=596)
W('22,2712', 0o57545, '', 'DLOAD', 'DCOMP', 'PUSH UP PHI', kind='interp', line=597)
W('22,2713', 0o43244, '', 'BPL', 'DAD', kind='interp', line=598)
W('22,2714', 0o44720, '', '', 'SUHALFAP', kind='operand', line=599)
W('22,2715', 0o15333, '', '', 'DPHALF', kind='operand', line=600)
W('22,2716', 0o77650, '', 'GOTO', kind='interp', line=601)
W('22,2717', 0o44724, '', '', 'VECOFANG', kind='operand', line=602)
W('22,2720', 0o52025, 'SUHALFAP', 'DSU', 'GOTO', kind='interp', line=603)
W('22,2721', 0o15333, '', '', 'DPHALF', kind='operand', line=604)
W('22,2722', 0o44724, '', '', 'VECOFANG', kind='operand', line=605)
W('22,2723', 0o77745, 'OKPHI', 'DLOAD', '', 'PUSH UP PHI', kind='interp', line=606)
W('22,2724', 0o43466, 'VECOFANG', 'VDEF', 'RVQ', kind='interp', line=607)

# Page 411
# ROUTINE FOR TERMINATING AUTOMATIC MANEUVERS

W('22,2725', 0o00004, 'NOGOM2', 'INHINT', '', 'THIS LOCATION ACCESSED BY A BZMF NOGO -2', line=612)
W('22,2726', 0o04662, '', 'TC', 'BANKCALL', line=613)
W('22,2727', 0o40155, '', 'CADR', 'ZEROEROR', kind='data', line=614)

W('22,2730', 0o00004, 'NOGO', 'INHINT', line=616)
W('22,2731', 0o04526, '', 'TC', 'STOPRATE', line=617)

# TERMINATE MANEUVER
W('22,2732', 0o35016, '', 'CAF', 'TWO', 'NOTE - ALL RETURNS ARE NOW MADE VIA', line=620)
W('22,2733', 0o05245, '', 'TC', 'WAITLIST', 'GOODEND', line=621)
#   EBANK= BCDU
W('22,2734', 0o02006, '', '2CADR', 'ENDMANU', kind='data', line=623)
W('22,2735', 0o42066, kind='data', line=623)

W('22,2736', 0o15217, '', 'TCF', 'ENDOFJOB', line=625)
