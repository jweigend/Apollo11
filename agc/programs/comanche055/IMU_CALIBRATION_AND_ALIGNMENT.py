"""IMU_CALIBRATION_AND_ALIGNMENT.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/IMU_CALIBRATION_AND_ALIGNMENT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 423-455 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('IMU_CALIBRATION_AND_ALIGNMENT', 'IMU_CALIBRATION_AND_ALIGNMENT.agc', 'Comanche055', pages='423-455')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     IMU_CALIBRATION_AND_ALIGNMENT.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 423-455
# Contact:      Onno Hommes <ohommes@cmu.edu>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-10 OH   Batch 1 Assignment Comanche Transcription
# 2009-05-20 RSB  Corrections: P00D00H -> P00DOOH, definition
# of 25DECML fixed.
# 2009-05-23 RSB  At SPECSTS, corrected to PRIO22.
#
# The contents of the "Comanche055" files, in general, are transcribed
# from scanned documents.
#
# Assemble revision 055 of AGC program Comanche by NASA
# 2021113-051.  April 1, 1969.
#
# This AGC program shall also be referred to as Colossus 2A
#
# Prepared by
# Massachusetts Institute of Technology
# 75 Cambridge Parkway
# Cambridge, Massachusetts
#
# under NASA contract NAS 9-4065.
#
# Refer directly to the online document mentioned above for further
# information.  Please report any errors to info@sandroid.org.

# Page 423
# NAME- IMU PERFORMANCE TESTS 2

# DATE- MARCH 20,1967
#
# BY- SYSTEM TEST GROUP 864-6900 EXT. 1274

# MODNO.- ZERO

# FUNCTIONAL DESCRIPTION

# POSITIONING ROUTINES FOR THE IMU PERFORMANCE TESTS AS WELL AS SOME OF
# THE TESTS THEMSELVES.  FOR A DESCRIPTION OF THESE SUBROUTINES AND THE
# OPERATING PROCEDURES (TYPICALLY) SEE STG MEMO 685.THEORETICAL REF.E-1973

#   BANK 33
#   SETLOC IMUCAL
#   BANK

#   EBANK= POSITON
W('33,2004', 0o35021, 'IMUTEST', 'CA', 'ZERO', line=53)
W('33,2005', 0o55452, '', 'TS', 'DRIFTT', line=54)
W('33,2006', 0o55643, '', 'TS', 'GEOCOMP1', line=55)
W('33,2007', 0o32443, '', 'CAF', 'TESTTIME', line=56)
W('33,2010', 0o55412, '', 'TS', 'LENGTHOT', line=57)
W('33,2011', 0o02302, '', 'TC', 'COAALIGN', 'TAKE CARE OF DRIFT FLAG', line=58)
W('33,2012', 0o35041, '', 'CAF', '1SECX', line=59)
W('33,2013', 0o55644, '', 'TS', '1SECXT1', line=60)

W('33,2014', 0o32441, '', 'CA', 'OC14400', line=62)
W('33,2015', 0o55074, '', 'TS', '1/PIPADT', line=63)
W('33,2016', 0o06006, 'GUESS', 'TC', 'INTPRET', 'CALCULATE -COS LATITUDE AND SIN LATITUDE', line=64)
W('33,2017', 0o77624, '', 'CALL', kind='interp', line=65)
W('33,2020', 0o10613, '', '', 'LATAZCHK', kind='operand', line=66)
W('33,2021', 0o57546, '', 'COS', 'DCOMP', kind='interp', line=67)
W('33,2022', 0o77752, '', 'SL1', kind='interp', line=68)
W('33,2023', 0o16447, '', 'STODL', 'WANGI', kind='interp', line=69)
W('33,2024', 0o02403, '', '', 'LATITUDE', kind='operand', line=70)
W('33,2025', 0o72556, '', 'SIN', 'SL1', kind='interp', line=71)
W('33,2026', 0o02445, '', 'STORE', 'WANGO', kind='interp', line=72)
W('33,2027', 0o77776, '', 'EXIT', kind='interp', line=73)
W('33,2030', 0o04662, 'GEOIMUTT', 'TC', 'BANKCALL', 'GYROCOMPASS COMES IN HERE', line=74)
W('33,2031', 0o16577, '', 'CADR', 'IMUZERO', kind='data', line=75)
W('33,2032', 0o02316, '', 'TC', 'IMUSTLLG', line=76)
W('33,2033', 0o35021, 'IMUBACK', 'CA', 'ZERO', line=77)
W('33,2034', 0o55421, '', 'TS', 'NDXCTR', line=78)
W('33,2035', 0o55450, '', 'TS', 'TORQNDX', line=79)
W('33,2036', 0o55451, '', 'TS', 'TORQNDX +1', line=80)
W('33,2037', 0o34375, 'NBPOSPL', 'CA', 'DEC17', line=81)
W('33,2040', 0o55655, '', 'TS', 'ZERONDX1', line=82)
W('33,2041', 0o32445, '', 'CA', 'XNBADR', line=83)
# Page 424
W('33,2042', 0o02356, '', 'TC', 'ZEROING', line=85)
W('33,2043', 0o35002, '', 'CA', 'HALF', line=86)
W('33,2044', 0o55713, '', 'TS', 'XNB', line=87)
W('33,2045', 0o06006, '', 'TC', 'INTPRET', line=88)
W('33,2046', 0o73545, '', 'DLOAD', 'SIN', kind='interp', line=89)
W('33,2047', 0o02401, '', '', 'AZIMUTH', kind='operand', line=90)
W('33,2050', 0o02724, '', 'STORE', 'YNB +2', kind='interp', line=91)
W('33,2051', 0o16734, '', 'STODL', 'ZNB +4', kind='interp', line=92)
W('33,2052', 0o02401, '', '', 'AZIMUTH', kind='operand', line=93)
W('33,2053', 0o77746, '', 'COS', kind='interp', line=94)
W('33,2054', 0o02726, '', 'STORE', 'YNB +4', kind='interp', line=95)
W('33,2055', 0o77676, '', 'DCOMP', kind='interp', line=96)
W('33,2056', 0o02732, '', 'STORE', 'ZNB +2', kind='interp', line=97)
W('33,2057', 0o77776, '', 'EXIT', kind='interp', line=98)
W('33,2060', 0o05364, '', 'TC', 'CHECKMM', line=99)
W('33,2061', 0o00003, '', 'MM', '03', '  SEE IF IN OPTICAL VERIFICATION', kind='data', line=100)
W('33,2062', 0o12064, '', 'TCF', '+2', ' NO', line=101)
W('33,2063', 0o13443, '', 'TCF', 'SETNBPOS +1', '   YES', line=102)
W('33,2064', 0o06006, '', 'TC', 'INTPRET', line=103)
W('33,2065', 0o77624, '', 'CALL', kind='interp', line=104)
W('33,2066', 0o47311, '', '', 'CALCGA', kind='operand', line=105)
W('33,2067', 0o77776, '', 'EXIT', kind='interp', line=106)
W('33,2070', 0o04662, '', 'TC', 'BANKCALL', line=107)
W('33,2071', 0o16663, '', 'CADR', 'IMUCOARS', kind='data', line=108)
W('33,2072', 0o35002, '', 'CAF', 'GLOKFBIT', 'IF GLOKFAIL SET, GIMBAL LOCK', line=109)
W('33,2073', 0o70077, '', 'MASK', 'FLAGWRD3', line=110)
W('33,2074', 0o00006, '', 'EXTEND', line=111)
W('33,2075', 0o12077, '', 'BZF', '+2', line=112)
W('33,2076', 0o25421, '', 'INCR', 'NDXCTR', '+1 IF IN GIMBAL LOCK,OTHERWISE 0', line=113)
W('33,2077', 0o05560, '', 'TC', 'DOWNFLAG', 'RESET GIMBAL LOCK FLAG', line=114)
W('33,2100', 0o00056, '', 'ADRES', 'GLOKFAIL', 'BIT 14 FLAG 3', kind='data', line=115)
W('33,2101', 0o02316, '', 'TC', 'IMUSTLLG', line=116)
W('33,2102', 0o11421, '', 'CCS', 'NDXCTR', 'IF ONE GO AND DO A PIPA TEST ONLY', line=117)
W('33,2103', 0o02131, '', 'TC', 'PIPACHK', 'ALIGN AND MEASURE VERTICAL PIPA RATE', line=118)
W('33,2104', 0o04662, '', 'TC', 'BANKCALL', line=119)
W('33,2105', 0o17073, '', 'CADR', 'IMUFINE', kind='data', line=120)
W('33,2106', 0o02316, '', 'TC', 'IMUSTLLG', line=121)
W('33,2107', 0o00006, '', 'EXTEND', line=122)
W('33,2110', 0o31657, '', 'DCA', 'PERFDLAY', line=123)
W('33,2111', 0o05342, '', 'TC', 'LONGCALL', line=124)
#   EBANK= POSITON
W('33,2112', 0o02116, '', '2CADR', 'GOESTIMS', kind='data', line=126)
W('33,2113', 0o66065, kind='data', line=126)

W('33,2114', 0o32121, '', 'CA', 'ESTICADR', line=128)
W('33,2115', 0o05175, '', 'TC', 'JOBSLEEP', line=129)
W('33,2116', 0o32121, 'GOESTIMS', 'CA', 'ESTICADR', line=130)
W('33,2117', 0o05201, '', 'TC', 'JOBWAKE', line=131)
W('33,2120', 0o05324, '', 'TC', 'TASKOVER', line=132)
W('33,2121', 0o66453, 'ESTICADR', 'CADR', 'ESTIMS', kind='data', line=133)
# Page 425
W('33,2122', 0o35021, 'TORQUE', 'CA', 'ZERO', line=135)
W('33,2123', 0o55050, '', 'TS', 'DSPTEM2', line=136)
W('33,2124', 0o31514, '', 'CA', 'DRIFTI', line=137)
W('33,2125', 0o55051, '', 'TS', 'DSPTEM2 +1', line=138)
W('33,2126', 0o51423, '', 'INDEX', 'POSITON', line=139)
W('33,2127', 0o55430, '', 'TS', 'SOUTHDR -1', line=140)
W('33,2130', 0o02427, '', 'TC', 'SHOW', line=141)

W('33,2131', 0o51421, 'PIPACHK', 'INDEX', 'NDXCTR', 'PIPA TEST', line=143)
W('33,2132', 0o02133, '', 'TC', '+1', line=144)
W('33,2133', 0o02417, '', 'TC', 'EARTHR*', line=145)
W('33,2134', 0o34374, '', 'CA', 'DEC57', line=146)
W('33,2135', 0o55412, '', 'TS', 'LENGTHOT', line=147)
W('33,2136', 0o35017, '', 'CA', 'ONE', line=148)
W('33,2137', 0o55547, '', 'TS', 'RESULTCT', line=149)
W('33,2140', 0o35021, '', 'CA', 'ZERO', line=150)
W('33,2141', 0o51422, '', 'INDEX', 'PIPINDEX', line=151)
W('33,2142', 0o54037, '', 'TS', 'PIPAX', line=152)
W('33,2143', 0o55502, '', 'TS', 'DATAPL', line=153)
W('33,2144', 0o55506, '', 'TS', 'DATAPL +4', line=154)
W('33,2145', 0o02321, '', 'TC', 'CHECKG', 'PIP PULSE CATCHING ROUTINE', line=155)
W('33,2146', 0o00004, '', 'INHINT', line=156)
W('33,2147', 0o35016, '', 'CAF', 'TWO', line=157)
W('33,2150', 0o05235, '', 'TC', 'TWIDDLE', line=158)
#   EBANK= XSM
W('33,2151', 0o02153, '', 'ADRES', 'PIPATASK', kind='data', line=160)
W('33,2152', 0o05217, '', 'TC', 'ENDOFJOB', line=161)
W('33,2153', 0o00006, 'PIPATASK', 'EXTEND', line=162)
W('33,2154', 0o27412, '', 'DIM', 'LENGTHOT', line=163)
W('33,2155', 0o31412, '', 'CA', 'LENGTHOT', line=164)
W('33,2156', 0o00006, '', 'EXTEND', line=165)
W('33,2157', 0o62163, '', 'BZMF', 'STARTPIP', line=166)
W('33,2160', 0o35006, '', 'CAF', 'BIT10', line=167)
W('33,2161', 0o05235, '', 'TC', 'TWIDDLE', line=168)
#   EBANK= XSM
W('33,2162', 0o02153, '', 'ADRES', 'PIPATASK', kind='data', line=170)
W('33,2163', 0o35002, 'STARTPIP', 'CAF', 'PRIO20', line=171)
W('33,2164', 0o05147, '', 'TC', 'FINDVAC', line=172)
#   EBANK= XSM
W('33,2165', 0o02170, '', '2CADR', 'PIPJOBB', kind='data', line=174)
W('33,2166', 0o66065, kind='data', line=174)

W('33,2167', 0o05324, '', 'TC', 'TASKOVER', line=176)

W('33,2170', 0o51421, 'PIPJOBB', 'INDEX', 'NDXCTR', line=178)
W('33,2171', 0o02172, '', 'TC', '+1', line=179)
W('33,2172', 0o02417, '', 'TC', 'EARTHR*', line=180)
W('33,2173', 0o31412, '', 'CA', 'LENGTHOT', line=181)
W('33,2174', 0o00006, '', 'EXTEND', line=182)
W('33,2175', 0o62177, '', 'BZMF', '+2', line=183)
W('33,2176', 0o05217, '', 'TC', 'ENDOFJOB', line=184)
W('33,2177', 0o35022, '', 'CA', 'FIVE', line=185)
# Page 426
W('33,2200', 0o55547, '', 'TS', 'RESULTCT', line=187)
W('33,2201', 0o02321, '', 'TC', 'CHECKG', line=188)
W('33,2202', 0o00006, '', 'EXTEND', line=189)
W('33,2203', 0o41503, '', 'DCS', 'DATAPL', line=190)
W('33,2204', 0o21507, '', 'DAS', 'DATAPL +4', line=191)

W('33,2205', 0o06006, '', 'TC', 'INTPRET', line=193)
W('33,2206', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=194)
W('33,2207', 0o02511, '', '', 'DATAPL +6', kind='operand', line=195)
W('33,2210', 0o02505, '', '', 'DATAPL +2', kind='operand', line=196)
W('33,2211', 0o45044, '', 'BPL', 'CALL', kind='interp', line=197)
W('33,2212', 0o66214, '', '', 'AINGOTN', kind='operand', line=198)
W('33,2213', 0o66276, '', '', 'OVERFFIX', kind='operand', line=199)
W('33,2214', 0o56325, 'AINGOTN', 'PDDL', 'DDV', kind='interp', line=200)
W('33,2215', 0o02507, '', '', 'DATAPL +4', kind='operand', line=201)
W('33,2216', 0o57212, '', 'SL4', 'DMPR', kind='interp', line=202)
W('33,2217', 0o27110, '', '', 'DEC585', 'DEC585 HAS BEEN REDEFINED FOR LEM', kind='operand', line=203)
W('33,2220', 0o77634, '', 'RTB', kind='interp', line=204)
W('33,2221', 0o45544, '', '', 'SGNAGREE', kind='operand', line=205)
W('33,2222', 0o01051, '', 'STORE', 'DSPTEM2', kind='interp', line=206)
W('33,2223', 0o77776, '', 'EXIT', kind='interp', line=207)
W('33,2224', 0o11421, '', 'CCS', 'NDXCTR', line=208)
W('33,2225', 0o02302, '', 'TC', 'COAALIGN', 'TAKE PLATFORM OUT OF GIMBAL LOCK', line=209)
W('33,2226', 0o02427, '', 'TC', 'SHOW', line=210)
W('33,2227', 0o32447, 'VERTDRFT', 'CA', '3990DEC', 'ABOUT 1 HOUR VERTICAL DRIFT TEST', line=211)
W('33,2230', 0o55412, '', 'TS', 'LENGTHOT', line=212)
W('33,2231', 0o51423, '', 'INDEX', 'POSITON', line=213)
W('33,2232', 0o41427, '', 'CS', 'SOUTHDR -2', line=214)
W('33,2233', 0o55452, '', 'TS', 'DRIFTT', line=215)
W('33,2234', 0o31675, '', 'CA', 'XSM +4', '0 IF POSN 4', line=216)
W('33,2235', 0o00006, '', 'EXTEND', line=217)
W('33,2236', 0o12244, '', 'BZF', 'PON2', line=218)
W('33,2237', 0o45013, 'PON4', 'CS', 'BIT5', '      OFFSET PLATFORM', line=219)
W('33,2240', 0o27651, '', 'ADS', 'ERCOMP1 +2', line=220)
W('33,2241', 0o35013, '', 'CA', 'BIT5', line=221)
W('33,2242', 0o27647, '', 'ADS', 'ERCOMP1', line=222)
W('33,2243', 0o12250, '', 'TCF', 'PONG', line=223)
W('33,2244', 0o45013, 'PON2', 'CS', 'BIT5', line=224)
W('33,2245', 0o27651, '', 'ADS', 'ERCOMP1 +2', line=225)
W('33,2246', 0o35013, '', 'CA', 'BIT5', line=226)
W('33,2247', 0o27653, '', 'ADS', 'ERCOMP1 +4', line=227)
W('33,2250', 0o02417, 'PONG', 'TC', 'EARTHR*', line=228)
W('33,2251', 0o35021, '', 'CA', 'ZERO', 'ALLOW ONLY SOUTH GYRO EARTH RATE COMPENS', line=229)
W('33,2252', 0o55404, '', 'TS', 'ERVECTOR', line=230)
W('33,2253', 0o55405, '', 'TS', 'ERVECTOR +1', line=231)
W('33,2254', 0o34777, 'GUESS1', 'CAF', 'POSMAX', line=232)
W('33,2255', 0o55450, '', 'TS', 'TORQNDX', line=233)
W('33,2256', 0o55451, '', 'TS', 'TORQNDX +1', line=234)
W('33,2257', 0o30032, '', 'CA', 'CDUX', line=235)
W('33,2260', 0o55413, '', 'TS', 'LOSVEC', line=236)
# Page 427
W('33,2261', 0o02453, '', 'TC', 'ESTIMS', line=238)
W('33,2262', 0o31512, 'VALMIS', 'CA', 'DRIFTO', line=239)
W('33,2263', 0o55051, '', 'TS', 'DSPTEM2 +1', line=240)
W('33,2264', 0o35021, '', 'CA', 'ZERO', line=241)
W('33,2265', 0o55050, '', 'TS', 'DSPTEM2', line=242)
W('33,2266', 0o02427, '', 'TC', 'SHOW', line=243)

W('33,2267', 0o05560, 'ENDTEST1', 'TC', 'DOWNFLAG', 'IMU NOT IN USE', line=245)
W('33,2270', 0o00007, '', 'ADRES', 'IMUSE', 'BIT 8 FLAG 0', kind='data', line=246)
W('33,2271', 0o45021, '', 'CS', 'ZERO', line=247)
W('33,2272', 0o05357, '', 'TC', 'NEWMODEX +3', line=248)
W('33,2273', 0o04662, '', 'TC', 'BANKCALL', line=249)
W('33,2274', 0o16063, '', 'CADR', 'MKRELEAS', kind='data', line=250)
W('33,2275', 0o05534, '', 'TC', 'ENDEXT', line=251)
# Page 428

W('33,2276', 0o43215, 'OVERFFIX', 'DAD', 'DAD', kind='interp', line=254)
W('33,2277', 0o15343, '', '', 'DPPOSMAX', kind='operand', line=255)
W('33,2300', 0o27116, '', '', 'ONEDPP', kind='operand', line=256)
W('33,2301', 0o77616, '', 'RVQ', kind='interp', line=257)

W('33,2302', 0o00006, 'COAALIGN', 'EXTEND', '', 'COARSE ALIGN SUBROUTINE', line=259)
W('33,2303', 0o23425, '', 'QXCH', 'QPLACE', line=260)
W('33,2304', 0o35021, '', 'CA', 'ZERO', line=261)
W('33,2305', 0o55155, '', 'TS', 'THETAD', line=262)
W('33,2306', 0o55156, '', 'TS', 'THETAD +1', line=263)
W('33,2307', 0o55157, '', 'TS', 'THETAD +2', line=264)
W('33,2310', 0o04662, '', 'TC', 'BANKCALL', line=265)
W('33,2311', 0o16663, '', 'CADR', 'IMUCOARS', kind='data', line=266)
W('33,2312', 0o04662, '', 'TC', 'BANKCALL', line=267)
W('33,2313', 0o17577, '', 'CADR', 'IMUSTALL', kind='data', line=268)
W('33,2314', 0o03102, '', 'TC', 'SOMERR2', line=269)
W('33,2315', 0o01425, '', 'TC', 'QPLACE', line=270)

W('33,2316', 0o00006, 'IMUSTLLG', 'EXTEND', line=272)
W('33,2317', 0o23425, '', 'QXCH', 'QPLACE', line=273)
W('33,2320', 0o02312, '', 'TC', 'COAALIGN +10', line=274)

W('33,2321', 0o00006, 'CHECKG', 'EXTEND', '', 'PIP PULSE CATCHING ROUTINE', line=276)
W('33,2322', 0o23425, '', 'QXCH', 'QPLACE', line=277)
W('33,2323', 0o02331, '', 'TC', '+6', line=278)
W('33,2324', 0o00003, 'CHECKG1', 'RELINT', line=279)
W('33,2325', 0o30067, '', 'CA', 'NEWJOB', line=280)
W('33,2326', 0o00006, '', 'EXTEND', line=281)
W('33,2327', 0o62335, '', 'BZMF', '+6', line=282)
W('33,2330', 0o05164, '', 'TC', 'CHANG1', line=283)
W('33,2331', 0o00004, '', 'INHINT', line=284)
W('33,2332', 0o51422, '', 'INDEX', 'PIPINDEX', line=285)
W('33,2333', 0o40037, '', 'CS', 'PIPAX', line=286)
W('33,2334', 0o55655, '', 'TS', 'ZERONDX', line=287)
W('33,2335', 0o00004, '', 'INHINT', line=288)
W('33,2336', 0o51422, '', 'INDEX', 'PIPINDEX', line=289)
W('33,2337', 0o30037, '', 'CA', 'PIPAX', line=290)
W('33,2340', 0o61655, '', 'AD', 'ZERONDX', line=291)
W('33,2341', 0o00006, '', 'EXTEND', line=292)
W('33,2342', 0o12324, '', 'BZF', 'CHECKG1', line=293)
W('33,2343', 0o51422, '', 'INDEX', 'PIPINDEX', line=294)
W('33,2344', 0o30037, '', 'CA', 'PIPAX', line=295)
W('33,2345', 0o51547, '', 'INDEX', 'RESULTCT', line=296)
W('33,2346', 0o55502, '', 'TS', 'DATAPL', line=297)
W('33,2347', 0o04553, '', 'TC', 'FINETIME', line=298)
W('33,2350', 0o51547, '', 'INDEX', 'RESULTCT', line=299)
W('33,2351', 0o55503, '', 'TS', 'DATAPL +1', line=300)
# Page 429
W('33,2352', 0o51547, '', 'INDEX', 'RESULTCT', line=302)
W('33,2353', 0o23504, '', 'LXCH', 'DATAPL +2', line=303)
W('33,2354', 0o00003, '', 'RELINT', line=304)
W('33,2355', 0o01425, 'ENDCHKG', 'TC', 'QPLACE', line=305)

W('33,2356', 0o54001, 'ZEROING', 'TS', 'L', line=307)
W('33,2357', 0o12361, '', 'TCF', '+2', line=308)
W('33,2360', 0o55655, 'ZEROING1', 'TS', 'ZERONDX1', line=309)
W('33,2361', 0o35021, '', 'CAF', 'ZERO', line=310)
W('33,2362', 0o50001, '', 'INDEX', 'L', line=311)
W('33,2363', 0o54000, '', 'TS', '0', line=312)
W('33,2364', 0o24001, '', 'INCR', 'L', line=313)
W('33,2365', 0o11655, '', 'CCS', 'ZERONDX1', line=314)
W('33,2366', 0o12360, '', 'TCF', 'ZEROING1', line=315)
W('33,2367', 0o00002, '', 'TC', 'Q', line=316)

# Page 430
#   SETLOC IMUCAL3
#   BANK
W('32,2000', 0o65345, 'ERTHRVSE', 'DLOAD', 'PDDL', kind='interp', line=321)
W('32,2001', 0o27111, '', '', 'SCHZEROS', 'PD24 = (SIN           -COS    0)(OMEG/MS)', kind='operand', line=322)
W('32,2002', 0o02403, '', '', 'LATITUDE', kind='operand', line=323)
W('32,2003', 0o57546, '', 'COS', 'DCOMP', kind='interp', line=324)
W('32,2004', 0o73525, '', 'PDDL', 'SIN', kind='interp', line=325)
W('32,2005', 0o02403, '', '', 'LATITUDE', kind='operand', line=326)
W('32,2006', 0o74266, '', 'VDEF', 'VXSC', kind='interp', line=327)
W('32,2007', 0o26450, '', '', 'OMEG/MS', kind='operand', line=328)
W('32,2010', 0o02405, '', 'STORE', 'ERVECTOR', kind='interp', line=329)
W('32,2011', 0o77634, '', 'RTB', kind='interp', line=330)
W('32,2012', 0o45510, '', '', 'LOADTIME', kind='operand', line=331)
W('32,2013', 0o26443, '', 'STOVL', 'TMARK', kind='interp', line=332)
W('32,2014', 0o27111, '', '', 'SCHZEROS', kind='operand', line=333)
W('32,2015', 0o02650, '', 'STORE', 'ERCOMP1', kind='interp', line=334)
W('32,2016', 0o77616, '', 'RVQ', kind='interp', line=335)
#   SETLOC IMUCAL
#   BANK
W('33,2370', 0o47020, 'EARTHR', 'ITA', 'RTB', 'CALCULATES AND COMPENSATES EARTH RATE', kind='interp', line=338)
W('33,2371', 0o00051, '', '', 'S2', kind='operand', line=339)
W('33,2372', 0o45510, '', '', 'LOADTIME', kind='operand', line=340)
W('33,2373', 0o02441, '', 'STORE', 'TEMPTIME', kind='interp', line=341)
W('33,2374', 0o51025, '', 'DSU', 'BPL', kind='interp', line=342)
W('33,2375', 0o02443, '', '', 'TMARK', kind='operand', line=343)
W('33,2376', 0o66401, '', '', 'ERTHR', kind='operand', line=344)
W('33,2377', 0o77624, '', 'CALL', kind='interp', line=345)
W('33,2400', 0o66276, '', '', 'OVERFFIX', kind='operand', line=346)
W('33,2401', 0o74261, 'ERTHR', 'SL', 'VXSC', kind='interp', line=347)
W('33,2402', 0o20212, '', '', '9D', kind='operand', line=348)
W('33,2403', 0o02405, '', '', 'ERVECTOR', kind='operand', line=349)
W('33,2404', 0o53321, '', 'MXV', 'VAD', kind='interp', line=350)
W('33,2405', 0o02672, '', '', 'XSM', kind='operand', line=351)
W('33,2406', 0o02650, '', '', 'ERCOMP1', kind='operand', line=352)
W('33,2407', 0o16650, '', 'STODL', 'ERCOMP1', kind='interp', line=353)
W('33,2410', 0o02441, '', '', 'TEMPTIME', kind='operand', line=354)
W('33,2411', 0o02443, '', 'STORE', 'TMARK', kind='interp', line=355)
W('33,2412', 0o47170, '', 'AXT,1', 'RTB', kind='interp', line=356)
W('33,2413', 0o02647, '', 'ECADR', 'ERCOMP1', kind='data', line=357)
W('33,2414', 0o45653, '', '', 'PULSEIMU', kind='operand', line=358)
W('33,2415', 0o77650, '', 'GOTO', kind='interp', line=359)
W('33,2416', 0o00051, '', '', 'S2', kind='operand', line=360)

W('33,2417', 0o00006, 'EARTHR*', 'EXTEND', line=362)
W('33,2420', 0o23426, '', 'QXCH', 'QPLACES', line=363)
W('33,2421', 0o06006, '', 'TC', 'INTPRET', line=364)
W('33,2422', 0o77624, '', 'CALL', kind='interp', line=365)
W('33,2423', 0o66370, '', '', 'EARTHR', kind='operand', line=366)
W('33,2424', 0o77776, 'PROUT', 'EXIT', kind='interp', line=367)
W('33,2425', 0o02316, '', 'TC', 'IMUSTLLG', line=368)
W('33,2426', 0o01426, '', 'TC', 'QPLACES', line=369)
# Page 431

W('33,2427', 0o00006, 'SHOW', 'EXTEND', line=372)
W('33,2430', 0o23425, '', 'QXCH', 'QPLACE', line=373)
W('33,2431', 0o31423, 'SHOW1', 'CA', 'POSITON', line=374)
W('33,2432', 0o55052, '', 'TS', 'DSPTEM2 +2', line=375)
W('33,2433', 0o32442, '', 'CA', 'VB06N98', line=376)
W('33,2434', 0o04662, '', 'TC', 'BANKCALL', line=377)
W('33,2435', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=378)
W('33,2436', 0o02267, '', 'TC', 'ENDTEST1', 'V 34', line=379)
W('33,2437', 0o01425, '', 'TC', 'QPLACE', ' V33', line=380)
W('33,2440', 0o12431, '', 'TCF', 'SHOW1', line=381)

W('33,2441', 0o14400, 'OC14400', 'OCT', '14400', kind='data', line=384)
S('3990DEC', 'equals', 0o76447, line=385)
W('33,2442', 0o01542, 'VB06N98', 'VN', '0698', kind='data', line=386)
W('33,2443', 0o01602, 'TESTTIME', 'OCT', '01602', kind='data', line=387)
S('DEC17', 'equals', 0o4375, line=388)
W('33,2444', 0o02757, 'OGCPL', 'ECADR', 'OGC', kind='data', line=389)
S('1SECX', 'equals', 0o5041, line=390)
S('DEC57', 'equals', 0o4374, line=391)
W('33,2445', 0o01713, 'XNBADR', 'GENADR', 'XNB', kind='data', line=392)
W('33,2446', 0o01671, 'XSMADR', 'GENADR', 'XSM', kind='data', line=393)
W('33,2447', 0o07623, 'OMEG/MS', '2DEC', '.24339048', kind='data', line=394)
W('33,2450', 0o26552, kind='data', line=394)

W('33,2451', 0o04662, 'P11OUT', 'TC', 'BANKCALL', line=397)
W('33,2452', 0o70117, '', 'CADR', 'MATRXJOB', 'RETURN TO P11', kind='data', line=398)

#   COUNT 02/COMST

#   BLOCK 2
W('4553', 0o00004, 'FINETIME', 'INHINT', '', 'RETURNS WITH INTERRUPT INHIBITED', line=403)
W('4554', 0o00006, '', 'EXTEND', line=404)
W('4555', 0o00004, '', 'READ', 'LOSCALAR', line=405)
W('4556', 0o54001, '', 'TS', 'L', line=406)
W('4557', 0o00006, '', 'EXTEND', line=407)
W('4560', 0o06004, '', 'RXOR', 'LOSCALAR', line=408)
W('4561', 0o00006, '', 'EXTEND', line=409)
W('4562', 0o14566, '', 'BZF', '+4', line=410)
W('4563', 0o00006, '', 'EXTEND', line=411)
W('4564', 0o00004, '', 'READ', 'LOSCALAR', line=412)
W('4565', 0o54001, '', 'TS', 'L', line=413)
W('4566', 0o44777, '', 'CS', 'POSMAX', line=414)
W('4567', 0o60001, '', 'AD', 'L', line=415)
W('4570', 0o00006, '', 'EXTEND', line=416)
W('4571', 0o14554, '', 'BZF', 'FINETIME +1', line=417)
W('4572', 0o00006, '', 'EXTEND', line=418)
W('4573', 0o00003, '', 'READ', 'HISCALAR', line=419)
W('4574', 0o00002, '', 'TC', 'Q', line=420)

# Page 432
# PROGRAM NAME-OPTIMUM PRELAUNCH ALIGNMENT CALIBRATION
# DATE- NOVEMBER 2 1966
# BY- GEORGE SCHMIDT IL 7-146 EXT. 126
# MOD NO 3
# FUNCTIONAL DESCRIPTION

# THIS  SECTION CONSISTS OF PRELAUNCH ALIGNMENT AND GYRO DRIFT TESTS
# INTEGRATED TOGETHER TO SAVE WORDS.  COMPASS IS COMPLETELY RESTART
# PROOFED EXCEPT FOR THE FIRST 30 SECONDS OR SO.  PERFORMANCE TESTS OF
# THE IRIGS IS RESTART PROOFED ENOUGH TO GIVE 75 PERCENT CONFIDENCE THAT
# IF A RESTART OCCURS THE DATA WILL STILL BE GOOD.  GOOD PRACTICE TO RECYCL
# WHEN A RESTART OCCURS UNLESS IT HAPPENS NEAR THE END OF A TEST-THEN WAIT
# FOR THE DATA TO FLASH.
# A RESTART IN GYROCOMPASS DURING GYRO TORQUING CAUSES PULSES TO BE LOST
# THE PRELAUNCH ALIGNMENT TECHNIQUE IS BASICALLY THE SAME AS IN BLOCK 1
# EXCEPT THAT IT HAS BEEN SIMPLIFIED IN THE SENSE THAT SMALL ANGLE APPROX.
# HAVE BEEN USED.  THE DRIFT TESTS USE A UNIQUE IMPLEMENTATION OF THE
# OPTIMUM STATISTICAL FILTER.  FOR A DESCRIPTION SEE E-1973.BOTH OF THESE
# ROUTINES USE STANDARD SYSTEM TEST LEADIN PROCEDURES.  THE INITIALIZATION
# PROCEDURE THE DRIFT TESTS IS IN THE JDC S.  THE INITIALIZATION METHOD
# FOR GYROCOMPASS IS AN ERAS LOAD THEN A MISSION PHASE CALL.
# THE COMPASS ALIGNS TO Z DOWN,X DOWNRANGE, HAS THE CAPABILITY
# CHANGE AZIMUTH WHILE RUNNING , IS COMPENSATED FOR
# COMPONENT ERRORS,IS CAPABLE OF OPTICAL VERIFICATION( CSM ONLY).

# COMPASS ERASABLE LOAD REQUIRED

# 1-LAUNCHAZ -DP AZIMUTH IN REV FROM NORTH OF XSM DESIRED      (NOM=.2)
# 2- LATITUDE -DP-OF LAUNCH PAD
# 3- AZIMUTH-DP-OF ZNB OF VEHICLE
# 4- IMU COMPENSATION PARAMETERS
# 5-AZ AND ELEVATION OF TARGETS 1,2             ****OPTIONAL****

# TO PERFORM AS PART OF COMPASS

# 1-OPTICAL VERIFICATION- V 65 E
# 2-AZIMUTH CHANGE-V 78 E

# SUBROUTINES CALLED

# DURING OPTICAL VERIFICATION (CSM ONLY) ESSENTIALLY ALL OF INFLIGHT ALIGN
# IS CALLED IN ONE WAY OR ANOTHER.  SEE THE LISTING.

# NORMAL EXIT

# DRIFT TESTS-  LENGTHOT GOES TO ZERO-RETURN TO IMU PERF TEST2 CONTROL
# GYROCOMPASS-MANY, SEE THE LISTING
# ALARMS

# 1600  OVERFLOW IN DRIFT TEST
# Page 433
# 1601  BAD IMU TORQUE ABORT
# 1602  BAD OPTICS DURING VERIFICATION-RETURN TO COMPASS        CSM ONLY

# OUTPUT

# DRIFT TESTS- FLASHING DISPLAYS OF RESULTS-CONTROLLED IN IMU PERF TESTS 2
# COMPASS-PROGRAM MODE LIGHTS TELL YOU WHAT PHAS OF PROGRAM YOU ARE IN
# 01  INITIALIZING THE PLATFORM POSITION AND ERASABLE
# 02  GYROCOMPASSING
# 03  DOING OPTICAL VERIFICATION (CSM)
#
#
# DEBRIS

# ALL CENTRALS,ALL OF EBANK XSM

# Page 434
# MOST OF THE ROUTINES COMMON TO ALIGNMENT AND CALIBRATION APPEAR
# ON THE NEXT FEW PAGES.

#   COUNT 33/P02

#   EBANK= XSM
#   BANK 33
#   SETLOC IMUCAL
#   BANK

W('33,2453', 0o05372, 'ESTIMS', 'TC', '2PHSCHNG', 'COMES HERE FROM IMU2', line=502)
W('33,2454', 0o00075, '', 'OCT', '00075', kind='data', line=503)
W('33,2455', 0o00004, '', 'OCT', '00004', 'TURN OFF GROUP 4 IF ON', kind='data', line=504)
W('33,2456', 0o00004, 'RSTGTS1', 'INHINT', '', 'COMES HERE PHASE1 RESTART', line=505)
W('33,2457', 0o30025, '', 'CA', 'TIME1', line=506)
W('33,2460', 0o55645, '', 'TS', 'GTSWTLT1', line=507)
W('33,2461', 0o35021, '', 'CAF', 'ZERO', 'ZERO THE PIPAS', line=508)
W('33,2462', 0o54037, '', 'TS', 'PIPAX', line=509)
W('33,2463', 0o54040, '', 'TS', 'PIPAY', line=510)
W('33,2464', 0o54041, '', 'TS', 'PIPAZ', line=511)
W('33,2465', 0o00003, '', 'RELINT', line=512)
W('33,2466', 0o33127, '', 'CA', '77DECML', 'ZERO ALL NECESSARY LOCATIONS', line=513)
W('33,2467', 0o55655, '', 'TS', 'ZERONDX1', line=514)
W('33,2470', 0o33130, '', 'CA', 'ALXXXZ', line=515)
W('33,2471', 0o02356, '', 'TC', 'ZEROING', line=516)
W('33,2472', 0o06006, '', 'TC', 'INTPRET', line=517)
W('33,2473', 0o77735, '', 'SLOAD', kind='interp', line=518)
W('33,2474', 0o27111, '', '', 'SCHZEROS', kind='operand', line=519)
W('33,2475', 0o25477, '', 'STOVL', 'GCOMPSW -1', kind='interp', line=520)
W('33,2476', 0o27122, '', '', 'INTVAL +2', 'LOAD SOME INITIAL DRIFT GAINS', kind='operand', line=521)
W('33,2477', 0o26455, '', 'STOVL', 'ALX1S', kind='interp', line=522)
W('33,2500', 0o27111, '', '', 'SCHZEROS', kind='operand', line=523)
W('33,2501', 0o01472, '', 'STORE', 'GCOMP', kind='interp', line=524)
W('33,2502', 0o01163, '', 'STORE', 'DELVX', 'GCOMPZER SUBROUTINE NO LONGER NEEDED', kind='interp', line=525)
W('33,2503', 0o77776, '', 'EXIT', kind='interp', line=526)

W('33,2504', 0o11643, '', 'CCS', 'GEOCOMP1', 'NON ZERO IF COMPASS.', line=528)
W('33,2505', 0o02507, '', 'TC', '+2', line=529)
W('33,2506', 0o02523, '', 'TC', 'SLEEPIE +1', line=530)
W('33,2507', 0o06006, '', 'TC', 'INTPRET', line=531)
W('33,2510', 0o77624, '', 'CALL', kind='interp', line=532)
W('33,2511', 0o64000, '', '', 'ERTHRVSE', kind='operand', line=533)
W('33,2512', 0o77776, '', 'EXIT', kind='interp', line=534)
W('33,2513', 0o31412, '', 'CA', 'LENGTHOT', 'TIMES FIVE IS THE NUM OF SEC ERECTING', line=535)
W('33,2514', 0o55646, '', 'TS', 'ERECTIME', line=536)

W('33,2515', 0o05354, '', 'TC', 'NEWMODEX', line=538)
W('33,2516', 0o00002, '', 'MM', '02', kind='data', line=539)
W('33,2517', 0o04662, '', 'TC', 'BANKCALL', 'SET UP PIPA FAIL TO CAUSE ISS ALARM', line=540)
# Page 435
W('33,2520', 0o17156, '', 'CADR', 'PIPUSE', 'COMPASS NEVER TURNS THIS OFF', kind='data', line=542)
W('33,2521', 0o03403, '', 'TC', 'ANNNNNN', 'END OF FIRST TIME THROUGH', line=543)

# Page 436
# COMES HERE AT THE END OF EVERY ITERATION THROUGH DRIFT TEST OR COMPASS

# SET UP WAITLIST SECTION
W('33,2522', 0o55412, 'SLEEPIE', 'TS', 'LENGTHOT', 'TEST NOT OVER-DECREMENT LENGTHOT', line=549)
W('33,2523', 0o05412, '', 'TC', 'PHASCHNG', 'CHANGE PHASE', line=550)
W('33,2524', 0o00135, '', 'OCT', '00135', kind='data', line=551)
W('33,2525', 0o11450, '', 'CCS', 'TORQNDX', 'ARE WE DOING VERTDRIFT', line=552)
W('33,2526', 0o02417, '', 'TC', 'EARTHR*', 'TRUE TORQUE SOUTH GYRO', line=553)
W('33,2527', 0o03406, 'WTLISTNT', 'TC', 'CHKCOMED', '      SEE IF COMPASS OVER', line=554)
W('33,2530', 0o02532, '', 'TC', 'SETGWLST', line=555)
W('33,2531', 0o05217, '', 'TC', 'ENDOFJOB', line=556)

W('33,2532', 0o00006, 'SETGWLST', 'EXTEND', line=558)
W('33,2533', 0o22154, '', 'QXCH', 'MPAC', 'CALLED EVERY WAITLIST OR AZIMUTH CHANGE', line=559)
W('33,2534', 0o00004, '', 'INHINT', line=560)
W('33,2535', 0o40025, '', 'CS', 'TIME1', line=561)
W('33,2536', 0o61645, '', 'AD', 'GTSWTLT1', line=562)
W('33,2537', 0o00006, '', 'EXTEND', line=563)
W('33,2540', 0o62542, '', 'BZMF', '+2', line=564)
W('33,2541', 0o65001, '', 'AD', 'NEGMAX', '10 MS ERROR OK', line=565)
W('33,2542', 0o61644, '', 'AD', '1SECXT1', '1 SEC FOR CALIBRATION, .5 SEC IN COMPASS', line=566)
W('33,2543', 0o00006, '', 'EXTEND', line=567)
W('33,2544', 0o62550, '', 'BZMF', 'RIGHTGTS', line=568)
W('33,2545', 0o05235, 'WTGTSMPL', 'TC', 'TWIDDLE', line=569)
#   EBANK= ALTIM
W('33,2546', 0o02574, '', 'ADRES', 'ALLOOP', kind='data', line=571)
W('33,2547', 0o00154, '', 'TC', 'MPAC', line=572)
W('33,2550', 0o35015, 'RIGHTGTS', 'CAF', 'FOUR', 'SET UP NEXT WAITLIST-ALLOW SOME TIME', line=573)
W('33,2551', 0o02545, '', 'TC', 'WTGTSMPL', 'END OF WAITLIST SECTION', line=574)

# STORE AND LOAD DATA SECTIONS FOR RESTART PROOFING

S('25DECML', 'equals', 0o4113, line=579)
W('33,2552', 0o34113, 'STOREDTA', 'CAF', '25DECML', line=580)
W('33,2553', 0o54154, '', 'TS', 'MPAC', line=581)
W('33,2554', 0o50154, '', 'INDEX', 'MPAC', line=582)
W('33,2555', 0o31460, '', 'CAE', 'THETAX1', line=583)
W('33,2556', 0o50154, '', 'INDEX', 'MPAC', line=584)
W('33,2557', 0o55577, '', 'TS', 'RESTARPT', line=585)
W('33,2560', 0o10154, '', 'CCS', 'MPAC', line=586)
W('33,2561', 0o12553, '', 'TCF', 'STOREDTA +1', line=587)
W('33,2562', 0o00002, '', 'TC', 'Q', line=588)

W('33,2563', 0o34113, 'LOADSTDT', 'CAF', '25DECML', line=590)
W('33,2564', 0o54154, '', 'TS', 'MPAC', line=591)
W('33,2565', 0o50154, '', 'INDEX', 'MPAC', line=592)
W('33,2566', 0o31577, '', 'CA', 'RESTARPT', line=593)
W('33,2567', 0o50154, '', 'INDEX', 'MPAC', line=594)

# Page 437
W('33,2570', 0o55460, '', 'TS', 'THETAX1', line=597)
W('33,2571', 0o10154, '', 'CCS', 'MPAC', line=598)
W('33,2572', 0o12564, '', 'TCF', 'LOADSTDT +1', line=599)
W('33,2573', 0o00002, '', 'TC', 'Q', line=600)

# COMES HERE EVERY ITERATION BY A WAITLIST CALL SET IN SLEEPIE

W('33,2574', 0o30025, 'ALLOOP', 'CA', 'TIME1', line=605)
W('33,2575', 0o55645, '', 'TS', 'GTSWTLT1', 'STORE TIME TO SET UP NEXT WAITLIST.', line=606)
W('33,2576', 0o31540, 'ALLOOP3', 'CA', 'ALTIM', line=607)
W('33,2577', 0o55631, '', 'TS', 'GEOSAVE1', line=608)
W('33,2600', 0o05412, '', 'TC', 'PHASCHNG', line=609)
W('33,2601', 0o00115, '', 'OCT', '00115', kind='data', line=610)
W('33,2602', 0o31631, 'ALLOOP1', 'CAE', 'GEOSAVE1', line=611)
W('33,2603', 0o55540, '', 'TS', 'ALTIM', line=612)
W('33,2604', 0o10000, '', 'CCS', 'A', line=613)
W('33,2605', 0o30000, '', 'CA', 'A', 'SHOULD NEVER HIT THIS LOCATION', line=614)
W('33,2606', 0o55541, '', 'TS', 'ALTIMS', line=615)
W('33,2607', 0o40000, '', 'CS', 'A', line=616)
W('33,2610', 0o55540, '', 'TS', 'ALTIM', line=617)
W('33,2611', 0o35021, '', 'CAF', 'ZERO', line=618)
W('33,2612', 0o56037, '', 'XCH', 'PIPAX', line=619)
W('33,2613', 0o55162, '', 'TS', 'DELVX', line=620)
W('33,2614', 0o35021, '', 'CAF', 'ZERO', line=621)
W('33,2615', 0o56040, '', 'XCH', 'PIPAY', line=622)
W('33,2616', 0o55164, '', 'TS', 'DELVY', line=623)
W('33,2617', 0o35021, '', 'CAF', 'ZERO', line=624)
W('33,2620', 0o56041, '', 'XCH', 'PIPAZ', line=625)
W('33,2621', 0o55166, '', 'TS', 'DELVZ', line=626)
W('33,2622', 0o34374, '', 'CAF', '19DECML', '23 OCT', line=627)
W('33,2623', 0o04114, '', 'TC', 'NEWPHASE', line=628)
W('33,2624', 0o00005, '', 'OCT', '00005', kind='data', line=629)
W('33,2625', 0o37657, 'SPECSTS', 'CAF', 'PRIO22', line=630)
W('33,2626', 0o05147, '', 'TC', 'FINDVAC', line=631)
#   EBANK= GEOSAVE1
W('33,2627', 0o02632, '', '2CADR', 'ALFLT', 'START THE JOB', kind='data', line=633)
W('33,2630', 0o66065, kind='data', line=633)

W('33,2631', 0o05324, '', 'TC', 'TASKOVER', line=635)

# Page 438
# THIS IS PART OF THE JOB DONE EVERY ITERATION

W('33,2632', 0o02552, 'ALFLT', 'TC', 'STOREDTA', 'STORE DATA IN CASE OF RESTART IN JOB', line=640)
W('33,2633', 0o05412, '', 'TC', 'PHASCHNG', 'THIS IS THE JOB DONE EVERY ITERATION', line=641)
W('33,2634', 0o00215, '', 'OCT', '00215', kind='data', line=642)
W('33,2635', 0o12637, '', 'TCF', '+2', line=643)
W('33,2636', 0o02563, 'ALFLT1', 'TC', 'LOADSTDT', 'COMES HERE ON RESTART', line=644)

W('33,2637', 0o11643, '', 'CCS', 'GEOCOMP1', line=646)
W('33,2640', 0o02642, '', 'TC', '+2', line=647)
W('33,2641', 0o02645, '', 'TC', 'NORMLOP', line=648)
W('33,2642', 0o03406, '', 'TC', 'CHKCOMED', '      SEE IF PRELAUNCH OVER', line=649)
W('33,2643', 0o04662, '', 'TC', 'BANKCALL', 'COMPENSATION IF IN COMPASS', line=650)
W('33,2644', 0o15262, '', 'CADR', '1/PIPA', kind='data', line=651)
W('33,2645', 0o06006, 'NORMLOP', 'TC', 'INTPRET', line=652)
W('33,2646', 0o77745, '', 'DLOAD', kind='interp', line=653)
W('33,2647', 0o27120, '', '', 'INTVAL', kind='operand', line=654)
W('33,2650', 0o24051, '', 'STOVL', 'S1', kind='interp', line=655)
W('33,2651', 0o01163, '', '', 'DELVX', kind='operand', line=656)
W('33,2652', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=657)
W('33,2653', 0o02672, '', '', 'XSM', kind='operand', line=658)
W('33,2654', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=659)
W('33,2655', 0o00160, '', '', 'MPAC +3', kind='operand', line=660)
W('33,2656', 0o16533, '', 'STODL', 'DPIPAY', kind='interp', line=661)
W('33,2657', 0o00162, '', '', 'MPAC +5', kind='operand', line=662)
W('33,2660', 0o02537, '', 'STORE', 'DPIPAZ', kind='interp', line=663)

W('33,2661', 0o76001, '', 'SETPD', 'AXT,1', kind='interp', line=665)
W('33,2662', 0o00001, '', '', '0', kind='operand', line=666)
W('33,2663', 0o00010, '', '', '8D', kind='operand', line=667)
W('33,2664', 0o57535, '', 'SLOAD', 'DCOMP', kind='interp', line=668)
W('33,2665', 0o02644, '', '', 'GEOCOMP1', kind='operand', line=669)
W('33,2666', 0o77640, '', 'BMN', kind='interp', line=670)
W('33,2667', 0o67210, '', '', 'ALWAYSG', 'DO A QUICK COMPASS', kind='operand', line=671)

# Page 439
# NOW WE HAVE JUST THE CALIBRATION PARTS OF THE PROGRAM-NEXT PAGES

#   COUNT 33/COMST

W('33,2670', 0o50135, 'ALCGKK', 'SLOAD', 'BMN', kind='interp', line=678)
W('33,2671', 0o02542, '', '', 'ALTIMS', kind='operand', line=679)
W('33,2672', 0o66705, '', '', 'ALFLT3', 'NO NEW GAINS NEEDED', kind='operand', line=680)
W('33,2673', 0o72174, 'ALKCG', 'AXT,2', 'LXA,1', 'LOADS SLOPES AND TIME CONSTANTS AT RQST', kind='interp', line=681)
W('33,2674', 0o00014, '', '', '12D', kind='operand', line=682)
W('33,2675', 0o02454, '', '', 'ALX1S', kind='operand', line=683)
W('33,2676', 0o62143, 'ALKCG2', 'DLOAD*', 'INCR,1', kind='interp', line=684)
W('33,2677', 0o02243, '', '', 'ALFDK +144D,1', kind='operand', line=685)
W('33,2700', 0o77775, '', 'DEC', '-2', kind='data', line=686)
W('33,2701', 0o12555, '', 'STORE', 'ALDK +10D,2', kind='interp', line=687)
W('33,2702', 0o66104, '', 'TIX,2', 'SXA,1', kind='interp', line=688)
W('33,2703', 0o66676, '', '', 'ALKCG2', kind='operand', line=689)
W('33,2704', 0o02454, '', '', 'ALX1S', kind='operand', line=690)

W('33,2705', 0o77770, 'ALFLT3', 'AXT,1', '', 'MEASUREMENT INCORPORATION ROUTINES', kind='interp', line=692)
W('33,2706', 0o00010, '', '', '8D', 'AND GAIN UPDATES', kind='operand', line=693)
W('33,2707', 0o41343, 'DELMLP', 'DLOAD*', 'DMP', kind='interp', line=694)
W('33,2710', 0o02543, '', '', 'DPIPAY +8D,1', kind='operand', line=695)
W('33,2711', 0o27705, '', '', 'PIPASC', kind='operand', line=696)
W('33,2712', 0o43661, '', 'SLR', 'BDSU*', kind='interp', line=697)
W('33,2713', 0o21212, '', '', '9D', kind='operand', line=698)
W('33,2714', 0o02511, '', '', 'INTY +8D,1', kind='operand', line=699)
W('33,2715', 0o06511, '', 'STORE', 'INTY +8D,1', kind='interp', line=700)
W('33,2716', 0o40725, '', 'PDDL', 'DMP*', kind='interp', line=701)
W('33,2717', 0o27707, '', '', 'VELSC', kind='operand', line=702)
W('33,2720', 0o02531, '', '', 'VLAUN +8D,1', kind='operand', line=703)
W('33,2721', 0o77732, '', 'SL2R', kind='interp', line=704)
W('33,2722', 0o45425, '', 'DSU', 'STADR', kind='interp', line=705)
W('33,2723', 0o71206, '', 'STORE', 'DELM +8D,1', kind='interp', line=706)
W('33,2724', 0o06573, '', 'STORE', 'DELM +10D,1', kind='interp', line=707)
W('33,2725', 0o77100, '', 'TIX,1', 'AXT,2', kind='interp', line=708)
W('33,2726', 0o66707, '', '', 'DELMLP', kind='operand', line=709)
W('33,2727', 0o00004, '', '', '4', kind='operand', line=710)
W('33,2730', 0o56743, 'ALILP', 'DLOAD*', 'DMPR*', kind='interp', line=711)
W('33,2731', 0o75314, '', '', 'ALK +4,2', kind='operand', line=712)
W('33,2732', 0o75230, '', '', 'ALDK +4,2', kind='operand', line=713)
W('33,2733', 0o12463, '', 'STORE', 'ALK +4,2', kind='interp', line=714)
W('33,2734', 0o77104, '', 'TIX,2', 'AXT,2', kind='interp', line=715)
W('33,2735', 0o66730, '', '', 'ALILP', kind='operand', line=716)
W('33,2736', 0o00010, '', '', '8D', kind='operand', line=717)
W('33,2737', 0o66140, 'ALKLP', 'LXC,1', 'SXA,1', kind='interp', line=718)
W('33,2740', 0o02455, '', '', 'CMPX1', kind='operand', line=719)
W('33,2741', 0o02455, '', '', 'CMPX1', kind='operand', line=720)
W('33,2742', 0o56743, '', 'DLOAD*', 'DMPR*', kind='interp', line=721)
W('33,2743', 0o02460, '', '', 'ALK +1,1', kind='operand', line=722)
W('33,2744', 0o75206, '', '', 'DELM +8D,2', kind='operand', line=723)
# Page 440
W('33,2745', 0o77613, '', 'DAD*', kind='interp', line=725)
W('33,2746', 0o75266, '', '', 'INTY +8D,2', kind='operand', line=726)
W('33,2747', 0o12511, '', 'STORE', 'INTY +8D,2', kind='interp', line=727)
W('33,2750', 0o42743, '', 'DLOAD*', 'DAD*', kind='interp', line=728)
W('33,2751', 0o75304, '', '', 'ALK +12D,2', kind='operand', line=729)
W('33,2752', 0o75220, '', '', 'ALDK +12D,2', kind='operand', line=730)
W('33,2753', 0o12473, '', 'STORE', 'ALK +12D,2', kind='interp', line=731)
W('33,2754', 0o42673, '', 'DMPR*', 'DAD*', kind='interp', line=732)
W('33,2755', 0o75206, '', '', 'DELM +8D,2', kind='operand', line=733)
W('33,2756', 0o75256, '', '', 'INTY +16D,2', kind='operand', line=734)
W('33,2757', 0o12521, '', 'STORE', 'INTY +16D,2', kind='interp', line=735)
W('33,2760', 0o40743, '', 'DLOAD*', 'DMP*', kind='interp', line=736)
W('33,2761', 0o27712, '', '', 'ALSK +1,1', kind='operand', line=737)
W('33,2762', 0o75206, '', '', 'DELM +8D,2', kind='operand', line=738)
W('33,2763', 0o42772, '', 'SL1R', 'DAD*', kind='interp', line=739)
W('33,2764', 0o75246, '', '', 'VLAUN +8D,2', kind='operand', line=740)
W('33,2765', 0o12531, '', 'STORE', 'VLAUN +8D,2', kind='interp', line=741)
W('33,2766', 0o76104, '', 'TIX,2', 'AXT,1', kind='interp', line=742)
W('33,2767', 0o66737, '', '', 'ALKLP', kind='operand', line=743)
W('33,2770', 0o00010, '', '', '8D', kind='operand', line=744)

W('33,2771', 0o64743, 'LOOSE', 'DLOAD*', 'PDDL*', 'EXTRAPOLATE SWAY VARIABLES', kind='interp', line=747)
W('33,2772', 0o02533, '', '', 'ACCWD +8D,1', kind='operand', line=748)
W('33,2773', 0o02531, '', '', 'VLAUN +8D,1', kind='operand', line=749)
W('33,2774', 0o55523, '', 'PDDL*', 'VDEF', kind='interp', line=750)
W('33,2775', 0o02541, '', '', 'POSNV +8D,1', kind='operand', line=751)
W('33,2776', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=752)
W('33,2777', 0o02001, '', '', 'TRANSM1', kind='operand', line=753)
W('33,3000', 0o77745, '', 'DLOAD', kind='interp', line=754)
W('33,3001', 0o00155, '', '', 'MPAC', kind='operand', line=755)
W('33,3002', 0o06541, '', 'STORE', 'POSNV +8D,1', kind='interp', line=756)
W('33,3003', 0o77745, '', 'DLOAD', kind='interp', line=757)
W('33,3004', 0o00160, '', '', 'MPAC +3', kind='operand', line=758)
W('33,3005', 0o06531, '', 'STORE', 'VLAUN +8D,1', kind='interp', line=759)
W('33,3006', 0o77745, '', 'DLOAD', kind='interp', line=760)
W('33,3007', 0o00162, '', '', 'MPAC +5', kind='operand', line=761)
W('33,3010', 0o06533, '', 'STORE', 'ACCWD +8D,1', kind='interp', line=762)
W('33,3011', 0o77700, '', 'TIX,1', kind='interp', line=763)
W('33,3012', 0o66771, '', '', 'LOOSE', kind='operand', line=764)

W('33,3013', 0o76174, '', 'AXT,2', 'AXT,1', 'EVALUATE SINES AND COSINES', kind='interp', line=767)
W('33,3014', 0o00006, '', '', '6', kind='operand', line=768)
W('33,3015', 0o00002, '', '', '2', kind='operand', line=769)
W('33,3016', 0o57343, 'BOOP', 'DLOAD*', 'DMPR', kind='interp', line=770)
W('33,3017', 0o02513, '', '', 'ANGX +2,1', kind='operand', line=771)
W('33,3020', 0o27715, '', '', 'GEORGEJ', kind='operand', line=772)
W('33,3021', 0o77722, '', 'SR2R', kind='interp', line=773)
W('33,3022', 0o73406, '', 'PUSH', 'SIN', kind='interp', line=774)
# Page 441
W('33,3023', 0o56072, '', 'SL3R', 'XAD,1', kind='interp', line=776)
W('33,3024', 0o00046, '', '', 'X1', kind='operand', line=777)
W('33,3025', 0o10021, '', 'STORE', '16D,2', kind='interp', line=778)
W('33,3026', 0o77745, '', 'DLOAD', kind='interp', line=779)
W('33,3027', 0o77746, '', 'COS', kind='interp', line=780)
W('33,3030', 0o10027, '', 'STORE', '22D,2', 'COSINES', kind='interp', line=781)
W('33,3031', 0o77704, '', 'TIX,2', kind='interp', line=782)
W('33,3032', 0o67016, '', '', 'BOOP', kind='operand', line=783)

W('33,3033', 0o77776, 'PERFERAS', 'EXIT', kind='interp', line=785)
W('33,3034', 0o35060, '', 'CA', 'EBANK7', line=786)
#   EBANK= LAT(SPL)
W('33,3035', 0o54003, '', 'TS', 'EBANK', line=788)
W('33,3036', 0o01400, '', 'TC', 'LAT(SPL)', 'GO TO ERASABLE ONLY TO RETURN', line=789)

# CAUTION

# THE ERASABLE PROGRAM THAT DOES THE CALCULATIONS MUST BE LOADED
# BEFORE ANY ATTEMPT IS MADE TO RUN THE IMU PERFORMANCE TEST

#   EBANK= LENGTHOT
W('33,3037', 0o11412, 'ONCEMORE', 'CCS', 'LENGTHOT', line=797)
W('33,3040', 0o02522, '', 'TC', 'SLEEPIE', 'TEST NOT OVER SET UP NEXT WAITLIST', line=798)
W('33,3041', 0o11450, '', 'CCS', 'TORQNDX', line=799)
W('33,3042', 0o13044, '', 'TCF', '+2', line=800)
W('33,3043', 0o03046, '', 'TC', 'SETUPER1', line=801)
W('33,3044', 0o30032, '', 'CA', 'CDUX', line=802)
W('33,3045', 0o55414, '', 'TS', 'LOSVEC +1', 'FOR TROUBLESHOOTING POSNS 2$4 VD', line=803)
W('33,3046', 0o06006, 'SETUPER1', 'TC', 'INTPRET', 'DRIFT TEST OVER', line=804)
W('33,3047', 0o65345, '', 'DLOAD', 'PDDL', 'ANGLES FROM DRIFT TEST ONLY', kind='interp', line=805)
W('33,3050', 0o02503, '', '', 'ANGZ', kind='operand', line=806)
W('33,3051', 0o02507, '', '', 'ANGY', kind='operand', line=807)
W('33,3052', 0o55525, '', 'PDDL', 'VDEF', kind='interp', line=808)
W('33,3053', 0o02511, '', '', 'ANGX', kind='operand', line=809)
W('33,3054', 0o74276, '', 'VCOMP', 'VXSC', kind='interp', line=810)
W('33,3055', 0o27715, '', '', 'GEORGEJ', kind='operand', line=811)
W('33,3056', 0o74521, '', 'MXV', 'VSR1', kind='interp', line=812)
W('33,3057', 0o02672, '', '', 'XSM', kind='operand', line=813)
W('33,3060', 0o02760, '', 'STORE', 'OGC', kind='interp', line=814)
W('33,3061', 0o77776, '', 'EXIT', kind='interp', line=815)

W('33,3062', 0o05412, 'TORQINCH', 'TC', 'PHASCHNG', line=817)
W('33,3063', 0o00005, '', 'OCT', '00005', kind='data', line=818)
W('33,3064', 0o32444, '', 'CA', 'OGCPL', line=819)
W('33,3065', 0o04662, '', 'TC', 'BANKCALL', line=820)
W('33,3066', 0o17206, '', 'CADR', 'IMUPULSE', kind='data', line=821)
W('33,3067', 0o02316, '', 'TC', 'IMUSTLLG', line=822)
W('33,3070', 0o11450, '', 'CCS', 'TORQNDX', '+ IF IN VERTICAL DRIFT TEST', line=823)
W('33,3071', 0o02262, '', 'TC', 'VALMIS', 'VERT DRIFT TEST OVER', line=824)
W('33,3072', 0o06006, '', 'TC', 'INTPRET', line=825)
# Page 442
W('33,3073', 0o77624, '', 'CALL', '', 'SET UP ERATE FOR PIP TEST OR COMPASS', kind='interp', line=827)
W('33,3074', 0o64000, '', '', 'ERTHRVSE', kind='operand', line=828)
W('33,3075', 0o77776, '', 'EXIT', kind='interp', line=829)
W('33,3076', 0o02122, '', 'TC', 'TORQUE', 'GO TO IMU2 FOR A PIPA TEST AND DISPLAY', line=830)

W('33,3077', 0o05650, 'SOMEERRR', 'TC', 'ALARM', line=833)
W('33,3100', 0o01600, '', 'OCT', '1600', kind='data', line=834)
W('33,3101', 0o03104, '', 'TC', '+3', line=835)
W('33,3102', 0o05650, 'SOMERR2', 'TC', 'ALARM', line=836)
W('33,3103', 0o01601, '', 'OCT', '1601', kind='data', line=837)
W('33,3104', 0o05412, '', 'TC', 'PHASCHNG', line=838)
W('33,3105', 0o00005, '', 'OCT', '00005', kind='data', line=839)
W('33,3106', 0o02267, '', 'TC', 'ENDTEST1', line=840)

# THE FAMOUS MAGIC NUMBERS OF SCHMIDT ARE NOW PART OF AN ERASABLE LOAD.

W('33,3107', 0o02222, 'DEC585', 'OCT', '02222', '1170 B+14 ORDER IS NOW IMPORTANT', kind='data', line=846)
W('33,3110', 0o00000, 'SCHZEROS', '2DEC', '.00000000', kind='data', line=847)
W('33,3111', 0o00000, kind='data', line=847)
W('33,3112', 0o00000, '', '2DEC', '.00000000', kind='data', line=848)
W('33,3113', 0o00000, kind='data', line=848)
W('33,3114', 0o00000, '', 'OCT', '00000', kind='data', line=849)
W('33,3115', 0o00000, 'ONEDPP', 'OCT', '00000', kind='data', line=850)
W('33,3116', 0o00001, '', 'OCT', '00001', '      ABOVE ORDER IS IMPORTANT', kind='data', line=851)

W('33,3117', 0o00004, 'INTVAL', 'OCT', '4', kind='data', line=853)
W('33,3120', 0o00002, '', 'OCT', '2', kind='data', line=854)
W('33,3121', 0o00220, '', 'DEC', '144', kind='data', line=855)
W('33,3122', 0o77776, '', 'DEC', '-1', kind='data', line=856)
W('33,3123', 0o35730, 'SOUPLY', '2DEC', '.93505870', 'INITIAL GAINS FOR PIP OUTPUTS', kind='data', line=857)
W('33,3124', 0o00035, kind='data', line=857)
W('33,3125', 0o10317, '', '2DEC', '.26266423', 'INITIAL GAINS/4 FOR ERECTION ANGLES', kind='data', line=858)
W('33,3126', 0o17550, kind='data', line=858)

W('33,3127', 0o00115, '77DECML', 'DEC', '77', kind='data', line=860)
W('33,3130', 0o01453, 'ALXXXZ', 'GENADR', 'ALX1S -1', kind='data', line=861)
# GYROCOMPASS PORTIONS FINISH THIS LOG SECTION

#   COUNT 33/P01

# INITIALIZATION SECTION

W('33,3131', 0o30075, 'GTSCPSS', 'CA', 'FLAGWRD1', 'CALLED BY V37', line=869)
W('33,3132', 0o75004, '', 'MASK', 'NOP01BIT', line=870)
# Page 443
W('33,3133', 0o00006, '', 'EXTEND', line=872)
W('33,3134', 0o13137, '', 'BZF', 'GTSCPSSA', line=873)
W('33,3135', 0o05721, '', 'TC', 'POODOO', line=874)
W('33,3136', 0o01521, '', 'OCT', '1521', 'NODO ALARM FOR P01 - P11 ALREADY DONE', kind='data', line=875)

W('33,3137', 0o35017, 'GTSCPSSA', 'CAF', 'ONE', line=877)
W('33,3140', 0o55643, '', 'TS', 'GEOCOMP1', 'THIS IS THE LEAD IN FOR COMPASS.', line=878)
W('33,3141', 0o33435, '', 'CA', '1/PIPAGT', line=879)
W('33,3142', 0o55074, '', 'TS', '1/PIPADT', line=880)
W('33,3143', 0o35010, 'NXXTENN', 'CA', 'BIT8', line=881)
W('33,3144', 0o55412, '', 'TS', 'LENGTHOT', line=882)
W('33,3145', 0o35036, '', 'CAF', '1/2SECX', 'COMPASS IS A .5 SEC LOOP', line=883)
W('33,3146', 0o55644, '', 'TS', '1SECXT1', line=884)
W('33,3147', 0o35017, '', 'CAF', 'ONE', line=885)
W('33,3150', 0o55632, '', 'TS', 'PREMTRX1', line=886)
W('33,3151', 0o55657, '', 'TS', 'PERFDLAY +1', line=887)
W('33,3152', 0o35021, '', 'CAF', 'ZERO', line=888)
W('33,3153', 0o55656, '', 'TS', 'PERFDLAY', line=889)
W('33,3154', 0o00006, '', 'EXTEND', line=890)
W('33,3155', 0o31634, '', 'DCA', 'LUNCHAZ1', line=891)
W('33,3156', 0o53636, '', 'DXCH', 'NEWAZ1', line=892)
W('33,3157', 0o00006, '', 'EXTEND', line=893)
W('33,3160', 0o31634, '', 'DCA', 'LUNCHAZ1', line=894)
W('33,3161', 0o53640, '', 'DXCH', 'OLDAZMTH', line=895)
W('33,3162', 0o34375, 'SETUPGC', 'CA', 'DEC17', line=896)
W('33,3163', 0o55655, '', 'TS', 'ZERONDX1', line=897)
W('33,3164', 0o32446, '', 'CA', 'XSMADR', line=898)
W('33,3165', 0o02356, '', 'TC', 'ZEROING', line=899)
W('33,3166', 0o03170, '', 'TC', 'POSN17C', line=900)
W('33,3167', 0o02030, '', 'TC', 'GEOIMUTT', 'GO TO IMU2 FOR FURTHER INITIALIZATION', line=901)

W('33,3170', 0o00006, 'POSN17C', 'EXTEND', '', 'COMPASS POSITION Z DOWN,X DOWNRANGE', line=904)
W('33,3171', 0o23425, '', 'QXCH', 'QPLACE', 'FROM NORTH IN REVOLUTIONS + CLOCKWISE', line=905)
W('33,3172', 0o45002, '', 'CS', 'HALF', 'ALL THIS TO INITIALIZE MATRIX', line=906)
W('33,3173', 0o55705, '', 'TS', 'ZSM', line=907)
W('33,3174', 0o06006, '', 'TC', 'INTPRET', line=908)
W('33,3175', 0o41545, '', 'DLOAD', 'PUSH', kind='interp', line=909)
W('33,3176', 0o02636, '', '', 'NEWAZ1', kind='operand', line=910)
W('33,3177', 0o77756, '', 'SIN', kind='interp', line=911)
W('33,3200', 0o02676, '', 'STORE', 'XSM +4', kind='interp', line=912)
W('33,3201', 0o16702, '', 'STODL', 'YSM +2', kind='interp', line=913)
W('33,3202', 0o77746, '', 'COS', kind='interp', line=914)
W('33,3203', 0o02704, '', 'STORE', 'YSM +4', kind='interp', line=915)
W('33,3204', 0o77676, '', 'DCOMP', kind='interp', line=916)
W('33,3205', 0o02674, '', 'STORE', 'XSM +2', kind='interp', line=917)
W('33,3206', 0o77776, '', 'EXIT', kind='interp', line=918)
W('33,3207', 0o01425, '', 'TC', 'QPLACE', line=919)

# Page 444
# JOB DONE EVERY ITERATION THROUGH COMPASS PROGRAM.SET BY TASK ALLOOP

#   COUNT 33/P02

W('33,3210', 0o44743, 'ALWAYSG', 'DLOAD*', 'DSU*', 'COMPASS AND ERECT', kind='interp', line=926)
W('33,3211', 0o02543, '', '', 'DPIPAY +8D,1', kind='operand', line=927)
W('33,3212', 0o02505, '', '', 'FILDELV1 +8D,1', kind='operand', line=928)
W('33,3213', 0o42675, '', 'DMPR', 'DAD*', kind='interp', line=929)
W('33,3214', 0o27717, '', '', 'GEOCONS1', kind='operand', line=930)
W('33,3215', 0o02505, '', '', 'FILDELV1 +8D,1', kind='operand', line=931)
W('33,3216', 0o06505, '', 'STORE', 'FILDELV1 +8D,1', kind='interp', line=932)
W('33,3217', 0o77613, '', 'DAD*', kind='interp', line=933)
W('33,3220', 0o02507, '', '', 'INTVEC1 +8D,1', kind='operand', line=934)
W('33,3221', 0o06507, '', 'STORE', 'INTVEC1 +8D,1', kind='interp', line=935)
W('33,3222', 0o42675, '', 'DMPR', 'DAD*', kind='interp', line=936)
W('33,3223', 0o27721, '', '', 'GEOCONS2', kind='operand', line=937)
W('33,3224', 0o02505, '', '', 'FILDELV1 +8D,1', kind='operand', line=938)
W('33,3225', 0o41475, '', 'DMPR', 'PUSH', kind='interp', line=939)
W('33,3226', 0o15333, '', '', 'GEOCONS5', kind='operand', line=940)
W('33,3227', 0o67300, '', 'TIX,1', 'SLOAD', kind='interp', line=941)
W('33,3230', 0o67210, '', '', 'ALWAYSG', kind='operand', line=942)
W('33,3231', 0o02647, '', '', 'ERECTIM1', kind='operand', line=943)
W('33,3232', 0o71254, '', 'BZE', 'DLOAD', kind='interp', line=944)
W('33,3233', 0o67244, '', '', 'COMPGS', kind='operand', line=945)
W('33,3234', 0o02471, '', '', 'THETAN1 +2', kind='operand', line=946)
W('33,3235', 0o45425, '', 'DSU', 'STADR', kind='interp', line=947)
W('33,3236', 0o61306, '', 'STODL', 'THETAN1 +2', 'ERECTION ONLY.', kind='interp', line=948)
W('33,3237', 0o77621, '', 'BDSU', kind='interp', line=949)
W('33,3240', 0o02473, '', '', 'THETAN1 +4', kind='operand', line=950)
W('33,3241', 0o02473, '', 'STORE', 'THETAN1 +4', kind='interp', line=951)
W('33,3242', 0o77650, '', 'GOTO', kind='interp', line=952)
W('33,3243', 0o67266, '', '', 'ADDINDRF', kind='operand', line=953)
W('33,3244', 0o43345, 'COMPGS', 'DLOAD', 'DAD', 'COMPASS', kind='interp', line=954)
W('33,3245', 0o02467, '', '', 'THETAN1', kind='operand', line=955)
W('33,3246', 0o02475, '', '', 'FILDELV1', kind='operand', line=956)
W('33,3247', 0o16467, '', 'STODL', 'THETAN1', kind='interp', line=957)
W('33,3250', 0o02475, '', '', 'FILDELV1', kind='operand', line=958)
W('33,3251', 0o44275, '', 'DMPR', 'BDSU', kind='interp', line=959)
W('33,3252', 0o27723, '', '', 'GEOCONS3', kind='operand', line=960)
W('33,3253', 0o02473, '', '', 'THETAN1 +4', kind='operand', line=961)
W('33,3254', 0o16473, '', 'STODL', 'THETAN1 +4', kind='interp', line=962)
W('33,3255', 0o02501, '', '', 'FILDELV1 +4', kind='operand', line=963)
W('33,3256', 0o44275, '', 'DMPR', 'BDSU', kind='interp', line=964)
W('33,3257', 0o27723, '', '', 'GEOCONS3', kind='operand', line=965)
W('33,3260', 0o02471, '', '', 'THETAN1 +2', kind='operand', line=966)
W('33,3261', 0o57325, '', 'PDDL', 'DMPR', kind='interp', line=967)
W('33,3262', 0o02503, '', '', 'INTVEC1 +4', kind='operand', line=968)
W('33,3263', 0o27725, '', '', 'GEOCONS4', kind='operand', line=969)
W('33,3264', 0o45421, '', 'BDSU', 'STADR', kind='interp', line=970)
W('33,3265', 0o75306, '', 'STORE', 'THETAN1 +2', kind='interp', line=971)
# Page 445
W('33,3266', 0o77776, 'ADDINDRF', 'EXIT', kind='interp', line=973)

W('33,3267', 0o11412, 'ENDGTSAL', 'CCS', 'LENGTHOT', 'IS 5 SEC OVER-THE TIME TO TORQ PLATFORM', line=976)
W('33,3270', 0o02522, '', 'TC', 'SLEEPIE', 'NO-SET UP NEXT WAITLIST CALL FOR .5 SEC', line=977)
W('33,3271', 0o03406, '', 'TC', 'CHKCOMED', line=978)
W('33,3272', 0o11304, '', 'CCS', 'LGYRO', 'YES BUT ARE GYROS BUSY', line=979)
W('33,3273', 0o12523, '', 'TCF', 'SLEEPIE +1', 'BUSY-GET THEM .5 SECONDS FROM NOW', line=980)

W('33,3274', 0o06006, 'LASTGTS', 'TC', 'INTPRET', line=982)
W('33,3275', 0o77775, '', 'VLOAD', kind='interp', line=983)
W('33,3276', 0o02650, '', '', 'ERCOMP1', kind='operand', line=984)
W('33,3277', 0o16461, '', 'STODL', 'THETAX1', kind='interp', line=985)
W('33,3300', 0o02443, '', '', 'TMARK', kind='operand', line=986)
W('33,3301', 0o02457, '', 'STORE', 'ALK', kind='interp', line=987)
W('33,3302', 0o77776, '', 'EXIT', '', 'PREVIOUS SECTION WAS FOR RESTARTS', kind='interp', line=988)

W('33,3303', 0o05412, 'RESTAIER', 'TC', 'PHASCHNG', line=990)
W('33,3304', 0o00275, '', 'OCT', '00275', kind='data', line=991)
W('33,3305', 0o06006, '', 'TC', 'INTPRET', 'ADD COMPASS COMMANDS INTO ERATE', line=992)
W('33,3306', 0o64375, '', 'VLOAD', 'MXV', kind='interp', line=993)
W('33,3307', 0o02467, '', '', 'THETAN1', kind='operand', line=994)
W('33,3310', 0o02672, '', '', 'XSM', kind='operand', line=995)
W('33,3311', 0o53372, '', 'VSL1', 'VAD', kind='interp', line=996)
W('33,3312', 0o02461, '', '', 'THETAX1', kind='operand', line=997)
W('33,3313', 0o16650, '', 'STODL', 'ERCOMP1', kind='interp', line=998)
W('33,3314', 0o02457, '', '', 'ALK', kind='operand', line=999)
W('33,3315', 0o02443, '', 'STORE', 'TMARK', kind='interp', line=1000)
W('33,3316', 0o77776, '', 'EXIT', kind='interp', line=1001)
W('33,3317', 0o02417, '', 'TC', 'EARTHR*', 'TORQUE IT ALL IN', line=1002)
W('33,3320', 0o31646, '', 'CAE', 'ERECTIM1', line=1003)
W('33,3321', 0o55631, '', 'TS', 'GEOSAVE1', line=1004)
W('33,3322', 0o05412, '', 'TC', 'PHASCHNG', line=1005)
W('33,3323', 0o00155, '', 'OCT', '00155', kind='data', line=1006)
W('33,3324', 0o06006, 'RESTEST1', 'TC', 'INTPRET', line=1007)
W('33,3325', 0o77775, '', 'VLOAD', kind='interp', line=1008)
W('33,3326', 0o27111, '', '', 'SCHZEROS', kind='operand', line=1009)
W('33,3327', 0o02467, '', 'STORE', 'THETAN1', kind='interp', line=1010)
W('33,3330', 0o77776, '', 'EXIT', kind='interp', line=1011)
W('33,3331', 0o11632, '', 'CCS', 'PREMTRXC', line=1012)
W('33,3332', 0o03401, '', 'TC', 'NOCHORLD', line=1013)
W('33,3333', 0o05412, '', 'TC', 'PHASCHNG', line=1014)
W('33,3334', 0o00255, '', 'OCT', '00255', kind='data', line=1015)
W('33,3335', 0o06006, 'RESTEST3', 'TC', 'INTPRET', line=1016)
W('33,3336', 0o77745, '', 'DLOAD', kind='interp', line=1017)
W('33,3337', 0o02634, '', '', 'LAUNCHAZ', kind='operand', line=1018)
W('33,3340', 0o53025, '', 'DSU', 'BZE', kind='interp', line=1019)
W('33,3341', 0o02640, '', '', 'OLDAZMTH', kind='operand', line=1020)
W('33,3342', 0o67376, '', '', 'NOAZCHGE', kind='operand', line=1021)
W('33,3343', 0o00001, '', 'STORE', '0D', kind='interp', line=1022)
# Page 446
W('33,3344', 0o43335, '', 'SLOAD', 'DAD', kind='interp', line=1024)
W('33,3345', 0o27117, '', '', 'ONEDPP +1', kind='operand', line=1025)
W('33,3346', 0o02633, '', '', 'PREMTRXC', 'DOES NOT CHANGE LAUNCHAZ', kind='operand', line=1026)
W('33,3347', 0o16633, '', 'STODL', 'PREMTRXC', kind='interp', line=1027)
W('33,3350', 0o02634, '', '', 'LAUNCHAZ', kind='operand', line=1028)
W('33,3351', 0o16636, '', 'STODL', 'NEWAZMTH', kind='interp', line=1029)
W('33,3352', 0o00001, '', '', '0D', kind='operand', line=1030)
W('33,3353', 0o02654, 'ADERCOMP', 'STORE', 'ERCOMP +4', kind='interp', line=1031)
W('33,3354', 0o77776, '', 'EXIT', kind='interp', line=1032)
W('33,3355', 0o03170, '', 'TC', 'POSN17C', line=1033)
W('33,3356', 0o05412, '', 'TC', 'PHASCHNG', line=1034)
W('33,3357', 0o00335, '', 'OCT', '00335', kind='data', line=1035)
W('33,3360', 0o00006, 'RESCHNG', 'EXTEND', line=1036)
W('33,3361', 0o31636, '', 'DCA', 'NEWAZMTH', line=1037)
W('33,3362', 0o53640, '', 'DXCH', 'OLDAZMTH', line=1038)
W('33,3363', 0o35011, '', 'CA', 'BIT7', 'SPEND 320 SEC ERECTING', line=1039)
W('33,3364', 0o55412, '', 'TS', 'LENGTHOT', line=1040)
W('33,3365', 0o05412, '', 'TC', 'PHASCHNG', line=1041)
W('33,3366', 0o00075, '', 'OCT', '00075', kind='data', line=1042)
W('33,3367', 0o33434, 'SPITGYRO', 'CA', 'ERCOMPPL', line=1043)
W('33,3370', 0o04662, '', 'TC', 'BANKCALL', line=1044)
W('33,3371', 0o17206, '', 'CADR', 'IMUPULSE', kind='data', line=1045)
W('33,3372', 0o04662, '', 'TC', 'BANKCALL', line=1046)
W('33,3373', 0o17577, '', 'CADR', 'IMUSTALL', kind='data', line=1047)
W('33,3374', 0o03102, '', 'TC', 'SOMERR2', line=1048)
W('33,3375', 0o02453, '', 'TC', 'ESTIMS', 'RE-INITIALIZE', line=1049)

W('33,3376', 0o77776, 'NOAZCHGE', 'EXIT', kind='interp', line=1052)
W('33,3377', 0o35017, '', 'CA', 'ONE', line=1053)
W('33,3400', 0o55632, '', 'TS', 'PREMTRXC', line=1054)
W('33,3401', 0o11631, 'NOCHORLD', 'CCS', 'GEOSAVE1', line=1055)
W('33,3402', 0o55646, '', 'TS', 'ERECTIM1', 'COUNTS DOWN FOR ERECTION.', line=1056)

W('33,3403', 0o34334, 'ANNNNNN', 'CAF', 'NINE', line=1058)
W('33,3404', 0o55412, '', 'TS', 'LENGTHOT', line=1059)
W('33,3405', 0o02523, '', 'TC', 'SLEEPIE +1', line=1060)

W('33,3406', 0o00004, 'CHKCOMED', 'INHINT', line=1063)
W('33,3407', 0o41011, '', 'CS', 'MODREG', 'CHECK FOR MM 07 FIRST', line=1064)
W('33,3410', 0o65023, '', 'AD', 'SEVEN', line=1065)
W('33,3411', 0o00006, '', 'EXTEND', line=1066)
W('33,3412', 0o13426, '', 'BZF', 'GOBKCALB', 'IF MM 07 RETURN TO PERF TEST', line=1067)
W('33,3413', 0o45021, '', 'CS', 'ZERO', line=1068)
W('33,3414', 0o00006, '', 'EXTEND', line=1069)
W('33,3415', 0o06030, '', 'RXOR', 'CHAN30', 'READ AND INVERT BITS IN CHANNEL 30', line=1070)
W('33,3416', 0o75013, '', 'MASK', 'BIT5', 'LIFTOFF BIT', line=1071)
W('33,3417', 0o10000, '', 'CCS', 'A', line=1072)
W('33,3420', 0o13427, '', 'TCF', 'PRELTERM', 'LIFTOFF HAS OCCURRED', line=1073)

# Page 447
W('33,3421', 0o35013, '', 'CA', 'GRRBKBIT', 'CHECK FOR BACKUP LIFTOFF', line=1076)
W('33,3422', 0o70101, '', 'MASK', 'FLAGWRD5', 'BIT5 FLAGWRD5', line=1077)
W('33,3423', 0o10000, '', 'CCS', 'A', line=1078)
W('33,3424', 0o13427, '', 'TCF', 'PRELTERM', 'BACKUP RECEIVED', line=1079)

W('33,3425', 0o00003, '', 'RELINT', line=1081)
W('33,3426', 0o00002, 'GOBKCALB', 'TC', 'Q', line=1082)

W('33,3427', 0o37657, 'PRELTERM', 'CA', 'PRIO22', 'PRELAUNCH DONE - SET UP P11', line=1084)
W('33,3430', 0o05210, '', 'TC', 'PRIOCHNG', 'INCREASE PRIORITY HIGHER THAN SERVICER', line=1085)
W('33,3431', 0o00004, '', 'INHINT', line=1086)
W('33,3432', 0o04701, '', 'TC', 'POSTJUMP', line=1087)
W('33,3433', 0o70002, '', 'CADR', 'P11', kind='data', line=1088)

W('33,3434', 0o02647, 'ERCOMPPL', 'ECADR', 'ERCOMP', kind='data', line=1091)

S('GEOCONS5', 'equals', 0o65332, line=1093)
W('33,3435', 0o06200, '1/PIPAGT', 'OCT', '06200', kind='data', line=1094)
S('17DECML', 'equals', 0o4375, line=1095)  # OCT 21
S('19DECML', 'equals', 0o4374, line=1096)  # OCT 23
S('1/2SECX', 'equals', 0o5036, line=1097)

# Page 448
S('GEOSTRT4', 'equals', 0o5217, line=1101)

# Page 449
# OPTICAL VERIFICATION ROUTINES FOR GYROCOMPASS

#   COUNT 33/P03

W('33,3436', 0o05412, 'GCOMPVER', 'TC', 'PHASCHNG', 'OPTICAL VERIFICATION ROUTINE', line=1108)
W('33,3437', 0o00154, '', 'OCT', '00154', kind='data', line=1109)
W('33,3440', 0o05354, '', 'TC', 'NEWMODEX', 'ENTERED BY VERB 65 ENTER', line=1110)
W('33,3441', 0o00003, '', 'MM', '03', kind='data', line=1111)
W('33,3442', 0o02037, 'SETNBPOS', 'TC', 'NBPOSPL', line=1112)
W('33,3443', 0o04662, '', 'TC', 'BANKCALL', line=1113)
W('33,3444', 0o16063, '', 'CADR', 'MKRELEAS', kind='data', line=1114)
W('33,3445', 0o35017, 'OPTDATA', 'CAF', 'BIT1', 'CALLS FOR AZIMUTH AND ELEVATION OF TARGE', line=1115)
W('33,3446', 0o22007, '', 'ZL', '', 'T 1,THEN TARGET 2', line=1116)
W('33,3447', 0o23427, '', 'LXCH', 'RUN', 'AZIMUTH CLOCKWSE FROM NORTH TO TARGET', line=1117)
W('33,3450', 0o55047, '', 'TS', 'DSPTEM1 +2', 'ELEVATION MEASURED FROM HORIZONTAL', line=1118)
W('33,3451', 0o00006, '', 'EXTEND', line=1119)
W('33,3452', 0o51427, '', 'INDEX', 'RUN', line=1120)
W('33,3453', 0o31433, '', 'DCA', 'TAZEL1', line=1121)
W('33,3454', 0o53046, '', 'DXCH', 'DSPTEM1', line=1122)
W('33,3455', 0o33500, '', 'CAF', 'V05N30E', line=1123)
W('33,3456', 0o04662, '', 'TC', 'BANKCALL', line=1124)
W('33,3457', 0o20673, '', 'CADR', 'GODSPRET', kind='data', line=1125)
W('33,3460', 0o33466, '', 'CAF', 'VN0641', line=1126)
W('33,3461', 0o04662, '', 'TC', 'BANKCALL', line=1127)
W('33,3462', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=1128)
W('33,3463', 0o03620, '', 'TC', 'GCOMP5', line=1129)
W('33,3464', 0o03467, '', 'TC', '+3', line=1130)
W('33,3465', 0o03455, '', 'TC', '-8D', line=1131)
W('33,3466', 0o01451, 'VN0641', 'VN', '0641', kind='data', line=1132)
W('33,3467', 0o53046, '', 'DXCH', 'DSPTEM1', 'TAZEL1 TARGET 1 AZIMUTH', line=1133)
W('33,3470', 0o51427, '', 'INDEX', 'RUN', line=1134)
W('33,3471', 0o53433, '', 'DXCH', 'TAZEL1', 'TAZEL1 +2 TARGET 2 AZIMUTH', line=1135)
W('33,3472', 0o11427, '', 'CCS', 'RUN', line=1136)
W('33,3473', 0o13477, '', 'TCF', '+4', line=1137)
W('33,3474', 0o35016, '', 'CAF', 'TWO', line=1138)
W('33,3475', 0o54001, '', 'TS', 'L', line=1139)
W('33,3476', 0o13447, '', 'TCF', 'OPTDATA +2', 'MPAC  1ST PASS=0 2ND PASS=2', line=1140)

W('33,3477', 0o03541, '', 'TC', 'CONTIN33', line=1143)

W('33,3500', 0o01236, 'V05N30E', 'VN', '0530', kind='data', line=1145)

W('33,3501', 0o06006, '', 'TC', 'INTPRET', 'UNDYNAMIC ASSEMBLER', line=1147)
W('33,3502', 0o77170, 'TAR/EREF', 'AXT,1', 'AXT,2', 'TARGET VECTOR', kind='interp', line=1148)
W('33,3503', 0o00002, '', '', '2', 'SIN(EL)   -COS(AZ)COS(EL)   SIN(AZ)COS(EL', kind='operand', line=1149)
W('33,3504', 0o00014, '', '', '12D', kind='operand', line=1150)
W('33,3505', 0o40331, '', 'SSP', 'SETPD', kind='interp', line=1151)
W('33,3506', 0o00052, '', '', 'S2', kind='operand', line=1152)
W('33,3507', 0o00006, '', '', '6', kind='operand', line=1153)
# Page 450
W('33,3510', 0o00001, '', '', '0', kind='operand', line=1155)
W('33,3511', 0o60533, 'TAR1', 'SLOAD*', 'SR2', 'X1=2 X2=12 S2=6 X1=0 X2=6 S2=6', kind='interp', line=1156)
W('33,3512', 0o02436, '', '', 'TAZEL1 +3,1', kind='operand', line=1157)
W('33,3513', 0o00001, '', 'STORE', '0', 'PD00 ELEVATION PD00', kind='interp', line=1158)
W('33,3514', 0o77756, '', 'SIN', kind='interp', line=1159)
W('33,3515', 0o10023, '', 'STORE', '18D,2', 'PD06 *** SIN(EL) ***PD12', kind='interp', line=1160)
W('33,3516', 0o77745, '', 'DLOAD', kind='interp', line=1161)
W('33,3517', 0o00001, '', '', '0', kind='operand', line=1162)
W('33,3520', 0o41546, '', 'COS', 'PUSH', 'PD00 COS(EL) PD00', kind='interp', line=1163)
W('33,3521', 0o47133, '', 'SLOAD*', 'RTB', kind='interp', line=1164)
W('33,3522', 0o02435, '', '', 'TAZEL1 +2,1', kind='operand', line=1165)
W('33,3523', 0o45513, '', '', 'CDULOGIC', kind='operand', line=1166)
W('33,3524', 0o00003, '', 'STORE', '2', 'PD02 AZIMUTH PD02', kind='interp', line=1167)
W('33,3525', 0o41356, '', 'SIN', 'DMP', kind='interp', line=1168)
W('33,3526', 0o00001, '', '', '0', kind='operand', line=1169)
W('33,3527', 0o77752, '', 'SL1', kind='interp', line=1170)
W('33,3530', 0o10027, '', 'STORE', '22D,2', 'PD10 *** SIN(AZ)COS(EL) ***PD16', kind='interp', line=1171)
W('33,3531', 0o71545, '', 'DLOAD', 'COS', kind='interp', line=1172)
W('33,3532', 0o00003, '', '', '2', kind='operand', line=1173)
W('33,3533', 0o72405, '', 'DMP', 'SL1', kind='interp', line=1174)
W('33,3534', 0o76076, '', 'DCOMP', 'AXT,1', kind='interp', line=1175)
W('33,3535', 0o00000, '', '', '0', kind='operand', line=1176)
W('33,3536', 0o10025, '', 'STORE', '20D,2', 'PD08 *** -COS(AZ)COS(EL) ***PD14', kind='interp', line=1177)
W('33,3537', 0o43504, '', 'TIX,2', 'RVQ', kind='interp', line=1178)
W('33,3540', 0o67511, '', '', 'TAR1', kind='operand', line=1179)

#   BANK 33
#   SETLOC IMUCAL
#   BANK
#   COUNT* $$/P03

W('33,3541', 0o35017, 'CONTIN33', 'CA', 'ONE', line=1187)
W('33,3542', 0o54735, '', 'TS', 'STARCODE', line=1188)
W('33,3543', 0o35021, '', 'CA', 'ZERO', line=1189)
W('33,3544', 0o03635, '', 'TC', 'TARGDRVE', line=1190)
W('33,3545', 0o06006, '', 'TC', 'INTPRET', line=1191)
W('33,3546', 0o77624, '', 'CALL', kind='interp', line=1192)
W('33,3547', 0o67502, '', '', 'TAR/EREF', kind='operand', line=1193)
W('33,3550', 0o64375, 'NEXTBNKS', 'VLOAD', 'MXV', kind='interp', line=1194)
W('33,3551', 0o00007, '', '', '6D', kind='operand', line=1195)
W('33,3552', 0o02672, '', '', 'XSM', kind='operand', line=1196)
W('33,3553', 0o77772, '', 'VSL1', kind='interp', line=1197)
W('33,3554', 0o26736, '', 'STOVL', 'STARAD', kind='interp', line=1198)
W('33,3555', 0o00015, '', '', '12D', kind='operand', line=1199)
W('33,3556', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=1200)
W('33,3557', 0o02672, '', '', 'XSM', kind='operand', line=1201)
W('33,3560', 0o36744, '', 'STCALL', 'STARAD +6', kind='interp', line=1202)
W('33,3561', 0o67726, '', '', 'LITTLSUB', kind='operand', line=1203)
W('33,3562', 0o02414, '', 'STORE', 'LOSVEC', kind='interp', line=1204)
# Page 451
W('33,3563', 0o77776, '', 'EXIT', kind='interp', line=1206)
W('33,3564', 0o04662, '', 'TC', 'BANKCALL', line=1207)
W('33,3565', 0o16063, '', 'CADR', 'MKRELEAS', kind='data', line=1208)

W('33,3566', 0o35016, 'NEXBNKSS', 'CAF', 'TWO', line=1211)
W('33,3567', 0o54735, '', 'TS', 'STARCODE', line=1212)
W('33,3570', 0o36211, '', 'CAF', 'SIX', line=1213)
W('33,3571', 0o03635, '', 'TC', 'TARGDRVE', line=1214)
W('33,3572', 0o06006, '', 'TC', 'INTPRET', line=1215)
W('33,3573', 0o77624, '', 'CALL', kind='interp', line=1216)
W('33,3574', 0o67726, '', '', 'LITTLSUB', kind='operand', line=1217)
W('33,3575', 0o24015, '', 'STOVL', '12D', kind='interp', line=1218)
W('33,3576', 0o02414, '', '', 'LOSVEC', kind='operand', line=1219)
W('33,3577', 0o34007, '', 'STCALL', '06D', kind='interp', line=1220)
W('33,3600', 0o47401, '', '', 'AXISGEN', kind='operand', line=1221)
W('33,3601', 0o77624, '', 'CALL', kind='interp', line=1222)
W('33,3602', 0o47205, '', '', 'CALCGTA', kind='operand', line=1223)
W('33,3603', 0o77776, '', 'EXIT', kind='interp', line=1224)
W('33,3604', 0o33631, 'GCOMP4', 'CAF', 'V06N93S', line=1225)
W('33,3605', 0o04662, '', 'TC', 'BANKCALL', line=1226)
W('33,3606', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=1227)
W('33,3607', 0o03620, '', 'TC', 'GCOMP5', line=1228)
W('33,3610', 0o13612, '', 'TCF', '+2', line=1229)
W('33,3611', 0o13604, '', 'TCF', 'GCOMP4', line=1230)
W('33,3612', 0o06006, '', 'TC', 'INTPRET', line=1231)
W('33,3613', 0o53375, '', 'VLOAD', 'VAD', kind='interp', line=1232)
W('33,3614', 0o02760, '', '', 'OGC', kind='operand', line=1233)
W('33,3615', 0o02650, '', '', 'ERCOMP1', kind='operand', line=1234)
W('33,3616', 0o02650, '', 'STORE', 'ERCOMP1', kind='interp', line=1235)
W('33,3617', 0o77776, '', 'EXIT', kind='interp', line=1236)
W('33,3620', 0o04662, 'GCOMP5', 'TC', 'BANKCALL', line=1237)
W('33,3621', 0o16063, '', 'CADR', 'MKRELEAS', kind='data', line=1238)
W('33,3622', 0o05560, '', 'TC', 'DOWNFLAG', line=1239)
W('33,3623', 0o00032, '', 'ADRES', 'TRM03FLG', kind='data', line=1240)

W('33,3624', 0o05354, '', 'TC', 'NEWMODEX', line=1242)
W('33,3625', 0o00002, '', 'MM', '02', kind='data', line=1243)
W('33,3626', 0o05412, '', 'TC', 'PHASCHNG', line=1244)
W('33,3627', 0o00004, '', 'OCT', '00004', kind='data', line=1245)
W('33,3630', 0o05217, '', 'TC', 'ENDOFJOB', line=1246)
W('33,3631', 0o01535, 'V06N93S', 'VN', '0693', kind='data', line=1247)
W('33,3632', 0o05650, 'GTSOPTCS', 'TC', 'ALARM', line=1248)
W('33,3633', 0o01602, 'GTSOPTSS', 'OCT', '01602', kind='data', line=1249)
W('33,3634', 0o03620, '', 'TC', 'GCOMP5', line=1250)

#   BANK 34
#   SETLOC IMUCAL1
#   BANK
# Page 452

#   COUNT 34/COMST

W('04,2613', 0o62545, 'LATAZCHK', 'DLOAD', 'SL2', 'CALLS FOR AZIMUTH AND LATITUDE', kind='interp', line=1260)
W('04,2614', 0o02403, '', '', 'LATITUDE', kind='operand', line=1261)
W('04,2615', 0o15047, '', 'STODL', 'DSPTEM1 +1', kind='interp', line=1262)
W('04,2616', 0o02401, '', '', 'AZIMUTH', kind='operand', line=1263)
W('04,2617', 0o77434, '', 'RTB', 'EXIT', kind='interp', line=1264)
W('04,2620', 0o45546, '', '', '1STO2S', kind='operand', line=1265)
W('04,2621', 0o56154, '', 'XCH', 'MPAC', line=1266)
W('04,2622', 0o55045, '', 'TS', 'DSPTEM1', line=1267)
W('04,2623', 0o04662, '', 'TC', 'BANKCALL', line=1268)
W('04,2624', 0o20703, '', 'CADR', 'CLEANDSP', kind='data', line=1269)
W('04,2625', 0o32644, '', 'CAF', 'VNG0641', line=1270)
W('04,2626', 0o04662, '', 'TC', 'BANKCALL', line=1271)
W('04,2627', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=1272)
W('04,2630', 0o02632, '', 'TC', '+2', 'NOT ALLOWED', line=1273)
W('04,2631', 0o02633, '', 'TC', '+2', line=1274)
W('04,2632', 0o02625, '', 'TC', '-5', line=1275)
W('04,2633', 0o06006, '', 'TC', 'INTPRET', line=1276)
W('04,2634', 0o47135, '', 'SLOAD', 'RTB', kind='interp', line=1277)
W('04,2635', 0o01046, '', '', 'DSPTEM1', kind='operand', line=1278)
W('04,2636', 0o45513, '', '', 'CDULOGIC', kind='operand', line=1279)
W('04,2637', 0o02401, '', 'STORE', 'AZIMUTH', kind='interp', line=1280)
W('04,2640', 0o60535, '', 'SLOAD', 'SR2', kind='interp', line=1281)
W('04,2641', 0o01047, '', '', 'DSPTEM1 +1', kind='operand', line=1282)
W('04,2642', 0o02403, '', 'STORE', 'LATITUDE', kind='interp', line=1283)
W('04,2643', 0o77616, '', 'RVQ', kind='interp', line=1284)
W('04,2644', 0o01451, 'VNG0641', 'VN', '0641', kind='data', line=1285)
#   BANK 33
#   SETLOC IMUCAL
#   BANK

#   COUNT* $$/P03
W('33,3635', 0o00006, 'TARGDRVE', 'EXTEND', line=1292)
W('33,3636', 0o23424, '', 'QXCH', 'QPLAC', line=1293)
W('33,3637', 0o55431, '', 'TS', 'TARG1/2', line=1294)
W('33,3640', 0o06006, '', 'TC', 'INTPRET', line=1295)
W('33,3641', 0o77624, '', 'CALL', kind='interp', line=1296)
W('33,3642', 0o67502, '', '', 'TAR/EREF', kind='operand', line=1297)
W('33,3643', 0o76740, '', 'LXC,1', 'VLOAD*', kind='interp', line=1298)
W('33,3644', 0o02431, '', '', 'TARG1/2', kind='operand', line=1299)
W('33,3645', 0o00007, '', '', '6D,1', kind='operand', line=1300)
W('33,3646', 0o36766, '', 'STCALL', 'STAR', kind='interp', line=1301)
W('33,3647', 0o46053, '', '', 'SXTANG', kind='operand', line=1302)
W('33,3650', 0o77776, '', 'EXIT', kind='interp', line=1303)
W('33,3651', 0o31773, '', 'CA', 'SAC', line=1304)
W('33,3652', 0o55161, '', 'TS', 'DESOPTS', line=1305)

# Page 453
W('33,3653', 0o31775, '', 'CA', 'PAC', line=1308)
W('33,3654', 0o55160, '', 'TS', 'DESOPTT', line=1309)
W('33,3655', 0o35021, 'RETARG', 'CAF', 'ZERO', line=1310)
W('33,3656', 0o55303, '', 'TS', 'OPTIND', line=1311)
W('33,3657', 0o35017, '', 'CAF', 'ONE', line=1312)
W('33,3660', 0o04662, '', 'TC', 'BANKCALL', line=1313)
W('33,3661', 0o16002, '', 'CADR', 'SXTMARK', kind='data', line=1314)
W('33,3662', 0o04662, '', 'TC', 'BANKCALL', line=1315)
W('33,3663', 0o17573, '', 'CADR', 'OPTSTALL', kind='data', line=1316)
W('33,3664', 0o03632, '', 'TC', 'GTSOPTCS', line=1317)
W('33,3665', 0o30075, '', 'CAE', 'FLAGWRD1', line=1318)
W('33,3666', 0o75014, '', 'MASK', 'TRM03BIT', line=1319)
W('33,3667', 0o10000, '', 'CCS', 'A', line=1320)
W('33,3670', 0o03620, '', 'TC', 'GCOMP5', line=1321)

W('33,3671', 0o51330, '', 'INDEX', 'MARKSTAT', line=1323)
W('33,3672', 0o30052, '', 'CA', 'QPRET', line=1324)
W('33,3673', 0o00006, '', 'EXTEND', line=1325)
W('33,3674', 0o13676, '', 'BZF', 'RETARG1', line=1326)
W('33,3675', 0o01424, '', 'TC', 'QPLAC', line=1327)

W('33,3676', 0o35021, 'RETARG1', 'CA', 'ZERO', 'RELEASE PREVIOUSLY GRABBED VAC AREA', line=1330)
W('33,3677', 0o57330, '', 'XCH', 'MARKSTAT', line=1331)
W('33,3700', 0o10000, '', 'CCS', 'A', line=1332)
W('33,3701', 0o50000, '', 'INDEX', 'A', line=1333)
W('33,3702', 0o54000, '', 'TS', 'A', line=1334)
W('33,3703', 0o13655, '', 'TCF', 'RETARG', 'GO DO SXTMARK AGAIN', line=1335)
#   BANK 33
#   SETLOC IMUCAL
#   BANK
#   COUNT* $$/P03
W('33,3704', 0o30341, 'PIPASC', '2DEC', '.76376833', kind='data', line=1340)
W('33,3705', 0o22444, kind='data', line=1340)

W('33,3706', 0o57223, 'VELSC', '2DEC', '-.52223476', kind='data', line=1342)
W('33,3707', 0o66451, kind='data', line=1342)

W('33,3710', 0o05427, 'ALSK', '2DEC', '.17329931', kind='data', line=1344)
W('33,3711', 0o12577, kind='data', line=1344)

W('33,3712', 0o77567, '', '2DEC', '-.00835370', kind='data', line=1346)
W('33,3713', 0o44202, kind='data', line=1346)

W('33,3714', 0o24276, 'GEORGEJ', '2DEC', '.63661977', kind='data', line=1348)
W('33,3715', 0o14066, kind='data', line=1348)

W('33,3716', 0o03146, 'GEOCONS1', '2DEC', '.1', kind='data', line=1350)
W('33,3717', 0o14632, kind='data', line=1350)

W('33,3720', 0o00121, 'GEOCONS2', '2DEC', '.005', kind='data', line=1352)
W('33,3721', 0o35341, kind='data', line=1352)

W('33,3722', 0o01767, 'GEOCONS3', '2DEC', '.062', kind='data', line=1354)
W('33,3723', 0o31666, kind='data', line=1354)

W('33,3724', 0o00004, 'GEOCONS4', '2DEC', '.0003', kind='data', line=1356)
W('33,3725', 0o35223, kind='data', line=1356)

# Page 454

#   COUNT 33/P02
W('33,3726', 0o77620, 'LITTLSUB', 'STQ', kind='interp', line=1361)
W('33,3727', 0o02424, '', '', 'QPLAC', kind='operand', line=1362)
W('33,3730', 0o76740, '', 'LXC,1', 'VLOAD*', kind='interp', line=1363)
W('33,3731', 0o01330, '', '', 'MARKSTAT', kind='operand', line=1364)
W('33,3732', 0o00003, '', '', '2,1', kind='operand', line=1365)
W('33,3733', 0o34767, '', 'STCALL', 'CDUSPOT', kind='interp', line=1366)
W('33,3734', 0o46000, '', '', 'SXTNB', kind='operand', line=1367)
W('33,3735', 0o77624, '', 'CALL', kind='interp', line=1368)
W('33,3736', 0o47637, '', '', 'TRG*NBSM', kind='operand', line=1369)
W('33,3737', 0o77650, '', 'GOTO', kind='interp', line=1370)
W('33,3740', 0o02424, '', '', 'QPLAC', kind='operand', line=1371)

W('33,3741', 0o77776, '', 'EXIT', kind='interp', line=1374)
W('33,3742', 0o06006, 'AZMTHCG1', 'TC', 'INTPRET', line=1375)
W('33,3743', 0o47145, '', 'DLOAD', 'RTB', kind='interp', line=1376)
W('33,3744', 0o02636, '', '', 'NEWAZMTH', kind='operand', line=1377)
W('33,3745', 0o45546, '', '', '1STO2S', kind='operand', line=1378)
W('33,3746', 0o77776, '', 'EXIT', kind='interp', line=1379)
W('33,3747', 0o56154, '', 'XCH', 'MPAC', line=1380)
W('33,3750', 0o55045, '', 'TS', 'DSPTEM1', line=1381)
W('33,3751', 0o04662, '', 'TC', 'BANKCALL', line=1382)
W('33,3752', 0o20703, '', 'CADR', 'CLEANDSP', kind='data', line=1383)
W('33,3753', 0o33775, '', 'CAF', 'VN0629', line=1384)
W('33,3754', 0o04662, '', 'TC', 'BANKCALL', line=1385)
W('33,3755', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=1386)
W('33,3756', 0o13760, '', 'TCF', '+2', line=1387)
W('33,3757', 0o13761, '', 'TCF', '+2', line=1388)
W('33,3760', 0o13753, '', 'TCF', '-5', line=1389)
W('33,3761', 0o06006, '', 'TC', 'INTPRET', line=1390)
W('33,3762', 0o47135, '', 'SLOAD', 'RTB', kind='interp', line=1391)
W('33,3763', 0o01046, '', '', 'DSPTEM1', kind='operand', line=1392)
W('33,3764', 0o45513, '', '', 'CDULOGIC', kind='operand', line=1393)
W('33,3765', 0o02634, '', 'STORE', 'LAUNCHAZ', kind='interp', line=1394)
W('33,3766', 0o77776, '', 'EXIT', kind='interp', line=1395)
W('33,3767', 0o35021, '', 'CA', 'ZERO', line=1396)
W('33,3770', 0o55632, '', 'TS', 'PREMTRXC', line=1397)
W('33,3771', 0o05412, '', 'TC', 'PHASCHNG', line=1398)
W('33,3772', 0o00004, '', 'OCT', '00004', kind='data', line=1399)
W('33,3773', 0o04701, '', 'TC', 'POSTJUMP', line=1400)
W('33,3774', 0o21272, '', 'CADR', 'PINBRNCH', kind='data', line=1401)

W('33,3775', 0o01435, 'VN0629', 'VN', '0629', kind='data', line=1403)

# Page 455
# *** END OF COMAID .029 ***
