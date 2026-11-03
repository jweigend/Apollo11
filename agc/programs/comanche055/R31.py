"""R31.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/R31.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 505-510 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('R31', 'R31.agc', 'Comanche055', pages='505-510')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     R31.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 505-510
# Contact:      Onno Hommes <ohommes@cmu.edu>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-11 OH   Batch 2 Assignment Comanche Transcription
# 2009-05-20 RSB  Corrected INSTALL -> INTSTALL
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

# Page 505
#   BANK 34
#   SETLOC R31
#   BANK

#   COUNT* $$/R31

W('31,2000', 0o35057, 'R31CALL', 'CAF', 'PRIO3', line=39)
W('31,2001', 0o05147, '', 'TC', 'FINDVAC', line=40)
#   EBANK= SUBEXIT
W('31,2002', 0o02032, '', '2CADR', 'V83CALL', kind='data', line=42)
W('31,2003', 0o62064, kind='data', line=42)

W('31,2004', 0o35041, 'DSPDELAY', 'CAF', '1SEC', line=44)
W('31,2005', 0o04662, '', 'TC', 'BANKCALL', line=45)
W('31,2006', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=46)
W('31,2007', 0o31044, '', 'CA', 'EXTVBACT', line=47)
W('31,2010', 0o75004, '', 'MASK', 'BIT12', line=48)
W('31,2011', 0o00006, '', 'EXTEND', line=49)
W('31,2012', 0o12004, '', 'BZF', 'DSPDELAY', line=50)

W('31,2013', 0o30105, 'DISPN5X', 'CA', 'FLAGWRD9', 'TEST R31FLAG (IN SUNDANCE R31FLAG WILL', line=52)
W('31,2014', 0o75014, '', 'MASK', 'BIT4', '    ALWAYS BE SET AS R34 DOES NOT EXIST)', line=53)
W('31,2015', 0o00006, '', 'EXTEND', line=54)
W('31,2016', 0o12021, '', 'BZF', '+3', line=55)
W('31,2017', 0o32136, '', 'CAF', 'V16N54', 'R31   USE NOUN 54', line=56)
W('31,2020', 0o02022, '', 'TC', '+2', line=57)
W('31,2021', 0o32137, '', 'CAF', 'V16N53', 'R34   USE NOUN 53', line=58)
W('31,2022', 0o04662, '', 'TC', 'BANKCALL', line=59)
W('31,2023', 0o20561, '', 'CADR', 'GOMARKF', kind='data', line=60)
W('31,2024', 0o05625, '', 'TC', 'B5OFF', line=61)
W('31,2025', 0o05625, '', 'TC', 'B5OFF', line=62)
W('31,2026', 0o12013, '', 'TCF', 'DISPN5X', line=63)

W('31,2027', 0o06006, 'V83', 'TC', 'INTPRET', line=65)
W('31,2030', 0o77650, '', 'GOTO', kind='interp', line=66)
W('31,2031', 0o62171, '', '', 'HAVEBASE', 'INTEG STATE VECTORS', kind='operand', line=67)
W('31,2032', 0o06006, 'V83CALL', 'TC', 'INTPRET', line=68)
W('31,2033', 0o77650, '', 'GOTO', kind='interp', line=69)
W('31,2034', 0o62140, '', '', 'STATEXTP', 'EXTRAPOLATE STATE VECTORS', kind='operand', line=70)
W('31,2035', 0o52375, 'COMPDISP', 'VLOAD', 'VSU', kind='interp', line=71)
W('31,2036', 0o00001, '', '', 'RATT', kind='operand', line=72)
W('31,2037', 0o02327, '', '', 'RONE', kind='operand', line=73)
W('31,2040', 0o51406, '', 'PUSH', 'ABVAL', 'RATT-RONE TO 0D       PD= 6', kind='interp', line=74)
W('31,2041', 0o02321, '', 'STORE', 'RANGE', 'METERS B-29', kind='interp', line=75)
W('31,2042', 0o77301, '', 'NORM', 'VLOAD', kind='interp', line=76)
W('31,2043', 0o00047, '', '', 'X1', 'RATT-RONE             PD= 0', kind='operand', line=77)
W('31,2044', 0o77762, '', 'VSR1', kind='interp', line=78)
W('31,2045', 0o53457, '', 'VSL*', 'UNIT', kind='interp', line=79)
W('31,2046', 0o20201, '', '', '0,1', kind='operand', line=80)
W('31,2047', 0o52315, '', 'PDVL', 'VSU', 'UNIT(LOS) TO 0D       PD= 6', kind='interp', line=81)
# Page 506
W('31,2050', 0o00007, '', '', 'VATT', kind='operand', line=83)
W('31,2051', 0o02335, '', '', 'VONE', kind='operand', line=84)
W('31,2052', 0o77641, '', 'DOT', '', '(VATT-VONE).UNIT(LOS) PD= 0', kind='interp', line=85)
W('31,2053', 0o77752, '', 'SL1', kind='interp', line=86)
W('31,2054', 0o36323, '', 'STCALL', 'RRATE', 'RANGE RATE M/CS B-7', kind='interp', line=87)
W('31,2055', 0o47477, '', '', 'CDUTRIG', 'TO INITIALIZE FOR *NBSM*', kind='operand', line=88)
W('31,2056', 0o77624, '', 'CALL', kind='interp', line=89)
W('31,2057', 0o62311, '', '', 'R34LOS', 'NOTE.  PDL MUST = 0.', kind='operand', line=90)
W('31,2060', 0o53575, 'R34ANG', 'VLOAD', 'UNIT', kind='interp', line=91)
W('31,2061', 0o02327, '', '', 'RONE', kind='operand', line=92)
W('31,2062', 0o77715, '', 'PDVL', '', 'UR TO 0D              PD= 6', kind='interp', line=93)
W('31,2063', 0o15333, '', '', 'THISAXIS', 'UNITX FOR CM, UNITZ FOR LM', kind='operand', line=94)
W('31,2064', 0o77214, '', 'BON', 'VLOAD', 'CHK R31FLAG.  ON=R31 THETA, OFF=R34 PHI', kind='interp', line=95)
W('31,2065', 0o04713, '', '', 'R31FLAG', kind='operand', line=96)
W('31,2066', 0o62070, '', '', '+2', 'R31-THETA', kind='operand', line=97)
W('31,2067', 0o00015, '', '', '12D', kind='operand', line=98)
W('31,2070', 0o77624, '', 'CALL', kind='interp', line=99)
W('31,2071', 0o47646, '', '', '*NBSM*', kind='operand', line=100)
W('31,2072', 0o41505, '', 'VXM', 'PUSH', 'UXORZ TO 6D           PD=12D', kind='interp', line=101)
W('31,2073', 0o01736, '', '', 'REFSMMAT', kind='operand', line=102)
W('31,2074', 0o72431, '', 'VPROJ', 'VSL2', kind='interp', line=103)
W('31,2075', 0o00001, '', '', '0D', kind='operand', line=104)
W('31,2076', 0o53445, '', 'BVSU', 'UNIT', kind='interp', line=105)
W('31,2077', 0o00007, '', '', '6D', kind='operand', line=106)
W('31,2100', 0o47315, '', 'PDVL', 'VXV', 'UP/2 TO 12D           PD=18D', kind='interp', line=107)
W('31,2101', 0o02327, '', '', 'RONE', kind='operand', line=108)
W('31,2102', 0o02335, '', '', 'VONE', kind='operand', line=109)
W('31,2103', 0o47256, '', 'UNIT', 'VXV', kind='interp', line=110)
W('31,2104', 0o02327, '', '', 'RONE', kind='operand', line=111)
W('31,2105', 0o63241, '', 'DOT', 'PDVL', 'SIGN TO 12D, UP/2 TO MPAC     PD=18D', kind='interp', line=112)
W('31,2106', 0o00015, '', '', '12D', kind='operand', line=113)
W('31,2107', 0o50372, '', 'VSL1', 'DOT', 'UP.UXORZ', kind='interp', line=114)
W('31,2110', 0o00007, '', '', '6D', kind='operand', line=115)
W('31,2111', 0o72565, '', 'SIGN', 'SL1', kind='interp', line=116)
W('31,2112', 0o00015, '', '', '12D', kind='operand', line=117)
W('31,2113', 0o77726, '', 'ACOS', kind='interp', line=118)
W('31,2114', 0o26325, '', 'STOVL', 'RTHETA', kind='interp', line=119)
W('31,2115', 0o02327, '', '', 'RONE', kind='operand', line=120)
W('31,2116', 0o51041, '', 'DOT', 'BPL', kind='interp', line=121)
W('31,2117', 0o00007, '', '', '6D', kind='operand', line=122)
W('31,2120', 0o62125, '', '', '+5', kind='operand', line=123)
W('31,2121', 0o44345, '', 'DLOAD', 'BDSU', 'IF UXORZ.R NEG, RTHETA = 1 - RTHETA', kind='interp', line=124)
W('31,2122', 0o02325, '', '', 'RTHETA', kind='operand', line=125)
W('31,2123', 0o15343, '', '', 'DPPOSMAX', kind='operand', line=126)
W('31,2124', 0o02325, '', 'STORE', 'RTHETA', 'RTHETA BETWEEN 0 AND 1 REV.', kind='interp', line=127)
W('31,2125', 0o77776, '', 'EXIT', kind='interp', line=128)
W('31,2126', 0o35013, '', 'CAF', 'BIT5', 'HAVE WE BEEN ANSWERED', line=129)
W('31,2127', 0o71044, '', 'MASK', 'EXTVBACT', line=130)
W('31,2130', 0o00006, '', 'EXTEND', line=131)
W('31,2131', 0o15534, '', 'BZF', 'ENDEXT', 'YES, DIE', line=132)
# Page 507
W('31,2132', 0o41044, '', 'CS', 'EXTVBACT', line=134)
W('31,2133', 0o75004, '', 'MASK', 'BIT12', line=135)
W('31,2134', 0o27044, '', 'ADS', 'EXTVBACT', line=136)

W('31,2135', 0o12027, '', 'TCF', 'V83', line=138)
W('31,2136', 0o04066, 'V16N54', 'VN', '1654', kind='data', line=139)
W('31,2137', 0o04065, 'V16N53', 'VN', '1653', kind='data', line=140)

# Page 508
# STATEXTP DOES AN INITIAL PRECISION EXTRAPOLATION OF THE
# LEM STATE VECTOR TO PRESENT TIME OR TO PIPTIME IF AV G
# IS ON AND SAVES AS BASE VECTOR. IF AV G IS ON RN + VN
# ARE USED AS THE CM STATE VECTOR AND THE INITIAL R RDOT
# RTHETA ARE COMPUTED WITH NO FURTHER INTEGRATION. IF AV
# G IS OFF A PRECISION EXTRAPOLATION IS MADE OF THE CM
# STATE VECTOR TO PRESENT TIME AND.....
#
# THE CM + LM STATE VECTORS ARE INTEGRATED TO PRES TIME
# USING PRECISION OR CONIC AS SURFFLAG IS SET OR CLEAR.
#
# IF AV G IS ON THEN
# SUBSEQUENT PASSES WILL PROVIDE
# USE OF RN + VN AS CM STATE VECTOR AND THE LM STATE
# VECTOR WILL BE PRECISION INTEGRATED USING LEMPREC
#
# IF SURFFLAG IS SET.
# CM STATE VECTOR RONE VONE + LM STATE VECTOR RATT
# VATT ARE USED IN COMPUTING R RDOT RTHETA.
#

W('31,2140', 0o43034, 'STATEXTP', 'RTB', 'BOF', 'INITIAL INTEGRATION', kind='interp', line=164)
W('31,2141', 0o45510, '', '', 'LOADTIME', kind='operand', line=165)
W('31,2142', 0o03751, '', '', 'V37FLAG', kind='operand', line=166)
W('31,2143', 0o62146, '', '', '+3', 'AV G OFF, USE PRES TIME', kind='operand', line=167)
W('31,2144', 0o77624, '', 'CALL', kind='interp', line=168)
W('31,2145', 0o62273, '', '', 'GETRVN', '     ON,  USE RN VN PIPTIME', kind='operand', line=169)
W('31,2146', 0o02343, '', 'STORE', 'BASETIME', 'PRES TIME OR PIPTIME', kind='interp', line=170)
W('31,2147', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=171)
W('31,2150', 0o27105, '', '', 'LEMPREC', kind='operand', line=172)
W('31,2151', 0o77775, '', 'VLOAD', '', 'BASE VECTOR, LM', kind='interp', line=173)
W('31,2152', 0o00017, '', '', 'RATT1', kind='operand', line=174)
W('31,2153', 0o26225, '', 'STOVL', 'BASEOTP', '  POS.', kind='interp', line=175)
W('31,2154', 0o00025, '', '', 'VATT1', kind='operand', line=176)
W('31,2155', 0o02241, '', 'STORE', 'BASEOTV', '  VEL.', kind='interp', line=177)
W('31,2156', 0o71214, '', 'BON', 'DLOAD', kind='interp', line=178)
W('31,2157', 0o03711, '', '', 'V37FLAG', kind='operand', line=179)
W('31,2160', 0o62035, '', '', 'COMPDISP', 'COMPUTE R RDOT RTHETA FROM', kind='operand', line=180)
# RONE(RN) VONE(VN) RATT+VATT(LEMPREC)
W('31,2161', 0o00015, '', '', 'TAT', kind='operand', line=182)
W('31,2162', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=183)
W('31,2163', 0o27071, '', '', 'CSMPREC', kind='operand', line=184)
W('31,2164', 0o77775, '', 'VLOAD', '', 'BASE VECTOR, CM', kind='interp', line=185)
W('31,2165', 0o00017, '', '', 'RATT1', kind='operand', line=186)
W('31,2166', 0o26255, '', 'STOVL', 'BASETHP', ' POS.', kind='interp', line=187)
W('31,2167', 0o00025, '', '', 'VATT1', kind='operand', line=188)
W('31,2170', 0o02263, '', 'STORE', 'BASETHV', ' VEL.', kind='interp', line=189)
W('31,2171', 0o47014, 'HAVEBASE', 'BON', 'RTB', 'SUBSEQUENT INTEGRATIONS', kind='interp', line=190)
W('31,2172', 0o03711, '', '', 'V37FLAG', kind='operand', line=191)
W('31,2173', 0o62256, '', '', 'GETRVN5', kind='operand', line=192)
W('31,2174', 0o45510, '', '', 'LOADTIME', kind='operand', line=193)
W('31,2175', 0o34041, '', 'STCALL', 'TDEC1', 'AV G OFF. SET INTEG. OF CM', kind='interp', line=194)
W('31,2176', 0o27442, '', '', 'INTSTALL', kind='operand', line=195)
W('31,2177', 0o43175, '', 'VLOAD', 'CLEAR', kind='interp', line=196)
W('31,2200', 0o02255, '', '', 'BASETHP', kind='operand', line=197)
# Page 509
W('31,2201', 0o00263, '', '', 'MOONFLAG', kind='operand', line=199)
W('31,2202', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=200)
W('31,2203', 0o02263, '', '', 'BASETHV', kind='operand', line=201)
W('31,2204', 0o15543, '', 'STODL', 'VCV', kind='interp', line=202)
W('31,2205', 0o02343, '', '', 'BASETIME', kind='operand', line=203)
W('31,2206', 0o43014, '', 'BOF', 'SET', 'GET APPROPRIATE MOONFLAG SETTING', kind='interp', line=204)
W('31,2207', 0o04343, '', '', 'MOONTHIS', kind='operand', line=205)
W('31,2210', 0o62212, '', '', '+2', kind='operand', line=206)
W('31,2211', 0o00063, '', '', 'MOONFLAG', kind='operand', line=207)
W('31,2212', 0o77614, '', 'CLEAR', kind='interp', line=208)
W('31,2213', 0o01673, '', '', 'INTYPFLG', kind='operand', line=209)
W('31,2214', 0o43014, '', 'BON', 'SET', kind='interp', line=210)
W('31,2215', 0o04307, '', '', 'SURFFLAG', kind='operand', line=211)
W('31,2216', 0o62220, '', '', '+2', 'PREC. IF LM DOWN', kind='operand', line=212)
W('31,2217', 0o01473, '', '', 'INTYPFLG', 'CONIC IF LM NOT DOWN', kind='operand', line=213)
W('31,2220', 0o35517, '', 'STCALL', 'TET', kind='interp', line=214)
W('31,2221', 0o27135, '', '', 'INTEGRVS', 'INTEGRATION --- AT LAST---', kind='operand', line=215)
W('31,2222', 0o77775, '', 'VLOAD', kind='interp', line=216)
W('31,2223', 0o00001, '', '', 'RATT', kind='operand', line=217)
W('31,2224', 0o26327, '', 'STOVL', 'RONE', kind='interp', line=218)
W('31,2225', 0o00007, '', '', 'VATT', kind='operand', line=219)
W('31,2226', 0o16335, '', 'STODL', 'VONE', 'GET SET FOR CONIC EXTRAP.,OTHER', kind='interp', line=220)
W('31,2227', 0o00015, '', '', 'TAT', kind='operand', line=221)
W('31,2230', 0o45014, '', 'BON', 'CALL', kind='interp', line=222)
W('31,2231', 0o04307, '', '', 'SURFFLAG', kind='operand', line=223)
W('31,2232', 0o62267, '', '', 'GETRVN6', 'LEMPREC IF LM DOWN', kind='operand', line=224)
W('31,2233', 0o27442, '', '', 'INTSTALL', '..CONIC IF NOT DOWN', kind='operand', line=225)
W('31,2234', 0o77614, '', 'SET', kind='interp', line=226)
W('31,2235', 0o01473, '', '', 'INTYPFLG', kind='operand', line=227)
W('31,2236', 0o00041, 'OTHINT', 'STORE', 'TDEC1', 'ENTERED IF AV G ON TO INTEG LM', kind='interp', line=228)
W('31,2237', 0o43175, '', 'VLOAD', 'CLEAR', kind='interp', line=229)
W('31,2240', 0o02225, '', '', 'BASEOTP', kind='operand', line=230)
W('31,2241', 0o00263, '', '', 'MOONFLAG', kind='operand', line=231)
W('31,2242', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=232)
W('31,2243', 0o02241, '', '', 'BASEOTV', kind='operand', line=233)
W('31,2244', 0o15543, '', 'STODL', 'VCV', kind='interp', line=234)
W('31,2245', 0o02343, '', '', 'BASETIME', kind='operand', line=235)
W('31,2246', 0o43014, '', 'BOF', 'SET', kind='interp', line=236)
W('31,2247', 0o04343, '', '', 'MOONTHIS', kind='operand', line=237)
W('31,2250', 0o62252, '', '', '+2', kind='operand', line=238)
W('31,2251', 0o00063, '', '', 'MOONFLAG', kind='operand', line=239)
W('31,2252', 0o35517, '', 'STCALL', 'TET', kind='interp', line=240)
W('31,2253', 0o27135, '', '', 'INTEGRVS', kind='operand', line=241)
W('31,2254', 0o77650, '', 'GOTO', kind='interp', line=242)
W('31,2255', 0o62035, '', '', 'COMPDISP', 'COMPUTE R RDOT RTHETA', kind='operand', line=243)
W('31,2256', 0o77624, 'GETRVN5', 'CALL', '', 'AV G ON', kind='interp', line=244)
W('31,2257', 0o62273, '', '', 'GETRVN', kind='operand', line=245)
W('31,2260', 0o45014, '', 'BON', 'CALL', kind='interp', line=246)
W('31,2261', 0o04307, '', '', 'SURFFLAG', kind='operand', line=247)
W('31,2262', 0o62267, '', '', 'GETRVN6', 'LM DOWN, LMPREC', kind='operand', line=248)
# Page 510
W('31,2263', 0o27442, '', '', 'INTSTALL', kind='operand', line=250)
W('31,2264', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=251)
W('31,2265', 0o01673, '', '', 'INTYPFLG', kind='operand', line=252)
W('31,2266', 0o62236, '', '', 'OTHINT', kind='operand', line=253)
W('31,2267', 0o34041, 'GETRVN6', 'STCALL', 'TDEC1', kind='interp', line=254)
W('31,2270', 0o27105, '', '', 'LEMPREC', kind='operand', line=255)
W('31,2271', 0o77650, '', 'GOTO', kind='interp', line=256)
W('31,2272', 0o62035, '', '', 'COMPDISP', 'COMPUTE R RDOT RTHETA', kind='operand', line=257)
W('31,2273', 0o77620, 'GETRVN', 'STQ', kind='interp', line=258)
W('31,2274', 0o00000, '', '', '0D', kind='operand', line=259)
W('31,2275', 0o52175, '', 'VLOAD', 'GOTO', 'AV G ON, RONE = RN VONE = VN', kind='interp', line=260)
W('31,2276', 0o01171, '', '', 'RN', ' AND USE PIPTIME', kind='operand', line=261)
W('31,2277', 0o62300, '', '', '+1', kind='operand', line=262)
W('31,2300', 0o36327, '', 'STCALL', 'RONE', kind='interp', line=263)
W('31,2301', 0o62302, '', '', '+1', kind='operand', line=264)
W('31,2302', 0o52175, '', 'VLOAD', 'GOTO', kind='interp', line=265)
W('31,2303', 0o01177, '', '', 'VN', kind='operand', line=266)
W('31,2304', 0o62305, '', '', '+1', kind='operand', line=267)
W('31,2305', 0o16335, '', 'STODL', 'VONE', kind='interp', line=268)
W('31,2306', 0o01205, '', '', 'PIPTIME', kind='operand', line=269)
W('31,2307', 0o77650, '', 'GOTO', kind='interp', line=270)
W('31,2310', 0o00000, '', '', '0D', kind='operand', line=271)
#   SETLOC R34
#   BANK
W('31,2311', 0o77776, 'R34LOS', 'EXIT', kind='interp', line=274)
W('31,2312', 0o30036, '', 'CA', 'CDUS', line=275)
W('31,2313', 0o50120, '', 'INDEX', 'FIXLOC', line=276)
W('31,2314', 0o54011, '', 'TS', '9D', line=277)
W('31,2315', 0o30035, '', 'CA', 'CDUT', line=278)
W('31,2316', 0o50120, '', 'INDEX', 'FIXLOC', line=279)
W('31,2317', 0o54013, '', 'TS', '11D', line=280)
W('31,2320', 0o30120, '', 'CA', 'FIXLOC', line=281)
W('31,2321', 0o66211, '', 'AD', 'SIX', line=282)
W('31,2322', 0o40000, '', 'COM', line=283)
W('31,2323', 0o50120, '', 'INDEX', 'FIXLOC', line=284)
W('31,2324', 0o54046, '', 'TS', 'X1', line=285)
W('31,2325', 0o06006, '', 'TC', 'INTPRET', line=286)
W('31,2326', 0o77624, '', 'CALL', kind='interp', line=287)
W('31,2327', 0o46000, '', '', 'SXTNB', kind='operand', line=288)
W('31,2330', 0o34015, '', 'STCALL', '12D', kind='interp', line=289)
W('31,2331', 0o62060, '', '', 'R34ANG', kind='operand', line=290)
