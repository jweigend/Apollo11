"""AGS_INITIALIZATION.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/AGS_INITIALIZATION.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 206-210 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('AGS_INITIALIZATION', 'AGS_INITIALIZATION.agc', 'Luminary099', pages='206-210')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     AGS_INITIALIZATION.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        206-210
# Mod history:  2009-05-19 HG   Transcribed from page images.
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

# Page 206

# PROGRAM NAME:  AGS INITIALIZATION (R47)
#
# WRITTEN BY:  RHODE/KILROY/FOLLETT
#
# MOD NO.:      0
# DATE:         23 MARCH 1967
# MOD BY:       KILROY
#
# MOD NO.:      1
# DATE:         28 OCTOBER 1967
# MOD BY:       FOLLETT
#
# FUNCT. DESC.: (1) TO PROVIDE THE AGS ABORT ELECTRONICS ASSEMBLY (AEA) WITH THE LEM AND CSM STATE VECTORS
# (POSITION,VELOCITY,TIME) IN LEM IMU COORDINATES BY MEANS OF THE LGC DIGITAL DOWNLINK.
#
# (2) TO ZERO THE ICDU, LGC, AND AEA GIMBAL ANGLE COUNTER SIMULTANEOUSLY IN ORDER TO ESTABLISH A
# COMMON ZERO REFERENCE FOR THE MEASUREMENT OF GIMBAL (EULER) ANGLES WHICH DEFINE LEM ATTITUDE
# (3) TO ESTABLISH THE GROUND ELAPSED TIME OF AEA CLOCK ZERO.  (IF AN AEA CLOCK ZERO IS
# REQUESTED DURING THIS PROGRAM
#
# LOG SECTION:  AGS INITIALIZATION
#
# CALLING SEQ:  PROGRAM IS ENTERED WHEN ASTRONAUT KEYS V47E ON DSKY.
# R47 MAY BE CALLED AT ANY TIME EXCEPT WHEN ANOTHER EXTENDED VERB IS IN PROGRESS
#
# SUBROUTINES
# CALLED:
#
# NORMAL EXIT:  ENDEXT
#
# ALARM/ABORT:  ALARM -- BAD REFSMMAT -- CODE:220
# OPERATOR ERROR IF V47 SELECTED DURING ANOTHER EXTENDED VERB.
#
# ERASABLES
# USED:         SAMPTIME        (2)     TIME OF :ENTER: KEYSTROKE
# AGSK            (2)     GROUND ELAPSED TIME OF THE AEA CLOCK :ZERO:
# AGSBUFF         (14D)   CONTAINS AGS INITIALIZATION DATA (SEE :OUTPUT: BELOW)
# AGSWORD         (1)     PREVIOUS DOWNLIST SAVED HERE

#   EBANK= AGSBUFF

#   BANK 40
#   SETLOC R47
#   BANK

#   COUNT* $$/R47

W('32,2005', 0o34737, 'AGSINIT', 'CAF', 'REFSMBIT', line=76)
W('32,2006', 0o70077, '', 'MASK', 'FLAGWRD3', 'CHECK REFSMFLG.', line=77)
W('32,2007', 0o10000, '', 'CCS', 'A', line=78)
# Page 207
W('32,2010', 0o02017, '', 'TC', 'REDSPTEM', 'REFSMMAT IS OK', line=80)
W('32,2011', 0o05567, '', 'TC', 'ALARM', 'REFSMMAT IS BAD', line=81)
W('32,2012', 0o00220, '', 'OCT', '220', kind='data', line=82)
W('32,2013', 0o05472, '', 'TC', 'ENDEXT', line=83)

W('32,2014', 0o00006, 'NEWAGS', 'EXTEND', line=85)
W('32,2015', 0o30014, '', 'DCA', 'SAMPTIME', 'TIME OF THE :ENTER: KEYSTROKE', line=86)
W('32,2016', 0o53421, '', 'DXCH', 'AGSK', 'BECOMES NEW AEA CLOCK :ZERO:', line=87)

W('32,2017', 0o00006, 'REDSPTEM', 'EXTEND', line=89)
W('32,2020', 0o31421, '', 'DCA', 'AGSK', line=90)
W('32,2021', 0o53052, '', 'DXCH', 'DSPTEMX', line=91)
W('32,2022', 0o32172, 'AGSDISPK', 'CAF', 'V06N16', line=92)
W('32,2023', 0o04616, '', 'TC', 'BANKCALL', 'R1 = 00XXX. HRS., R2 = 000XX MIN.,', line=93)
W('32,2024', 0o20334, '', 'CADR', 'GOMARKF', 'R3 = 0XX.XX SEC.', kind='data', line=94)
W('32,2025', 0o05472, '', 'TC', 'ENDEXT', 'TERMINATE RETURN', line=95)
W('32,2026', 0o02036, '', 'TC', 'AGSVCALC', 'PROCEED RETURN', line=96)
W('32,2027', 0o44746, '', 'CS', 'BIT6', 'IS ENTER VIA A V32', line=97)
W('32,2030', 0o60154, '', 'AD', 'MPAC', line=98)
W('32,2031', 0o00006, '', 'EXTEND', line=99)
W('32,2032', 0o12014, '', 'BZF', 'NEWAGS', 'YES, USE KEYSTROKE TIME FOR NEW AGSK', line=100)

W('32,2033', 0o00006, '', 'EXTEND', '', 'NO, NEW AGSK LOADED VIA V25', line=102)
W('32,2034', 0o31052, '', 'DCA', 'DSPTEMX', 'LOADED INTO DSPTEMX BY KEYING', line=103)
W('32,2035', 0o02016, '', 'TC', 'REDSPTEM -1', 'V25E FOLLOWED BY HRS.,MINS.,SECS.', line=104)
# DISPLAY THE NEW K

W('32,2036', 0o06037, 'AGSVCALC', 'TC', 'INTPRET', line=107)
W('32,2037', 0o77614, '', 'SET', kind='interp', line=108)
W('32,2040', 0o01076, '', '', 'NODOFLAG', "DON'T ALLOW V37", kind='operand', line=109)
W('32,2041', 0o77414, '', 'SET', 'EXIT', kind='interp', line=110)
W('32,2042', 0o02076, '', '', 'XDSPFLAG', kind='operand', line=111)

W('32,2043', 0o32172, '', 'CAF', 'V06N16', line=113)
W('32,2044', 0o04616, '', 'TC', 'BANKCALL', line=114)
W('32,2045', 0o20620, '', 'CADR', 'EXDSPRET', kind='data', line=115)

W('32,2046', 0o06037, '', 'TC', 'INTPRET', 'EXTRAPOLATE LEM AND CSM STATE VECTORS', line=117)
W('32,2047', 0o77634, '', 'RTB', '', 'TO THE PRESENT TIME', kind='interp', line=118)
W('32,2050', 0o21573, '', '', 'LOADTIME', 'LOAD MPAC WITH TIME2,TIME1', kind='operand', line=119)
W('32,2051', 0o34041, '', 'STCALL', 'TDEC1', 'CALCULATE LEM STATE VECTOR', kind='interp', line=120)
W('32,2052', 0o27057, '', '', 'LEMPREC', kind='operand', line=121)
W('32,2053', 0o77624, '', 'CALL', '', 'CALL ROUTINE TO CONVERT TO SM COORDS AND', kind='interp', line=122)
W('32,2054', 0o64132, '', '', 'SCALEVEC', 'PROVIDE PROPER SCALING', kind='operand', line=123)
W('32,2055', 0o16201, '', 'STODL', 'AGSBUFF', '(LEMPREC AND CSMPREC LEAVE TDEC1 IN TAT)', kind='interp', line=124)
W('32,2056', 0o00015, '', '', 'TAT', 'TAT = TIME TO WHICH RATT1 AND VATT1 ARE', kind='operand', line=125)
W('32,2057', 0o34041, '', 'STCALL', 'TDEC1', 'COMPUTED (CSEC SINCE CLOCK START B-28).', kind='interp', line=126)
W('32,2060', 0o27043, '', '', 'CSMPREC', 'CALCULATE CSM STATE VECTOR FOR SAME TIME', kind='operand', line=127)
W('32,2061', 0o77624, '', 'CALL', kind='interp', line=128)
W('32,2062', 0o64132, '', '', 'SCALEVEC', kind='operand', line=129)
# Page 208
W('32,2063', 0o16207, '', 'STODL', 'AGSBUFF +6', kind='interp', line=131)
W('32,2064', 0o00015, '', '', 'TAT', kind='operand', line=132)
W('32,2065', 0o56225, '', 'DSU', 'DDV', 'CALCULATE AND STORE THE TIME', kind='interp', line=133)
W('32,2066', 0o02021, '', '', 'AGSK', kind='operand', line=134)
W('32,2067', 0o24175, '', '', 'TSCALE', kind='operand', line=135)
W('32,2070', 0o02215, '', 'STORE', 'AGSBUFF +12D', kind='interp', line=136)
W('32,2071', 0o77776, '', 'EXIT', kind='interp', line=137)

W('32,2072', 0o34753, '', 'CAF', 'LAGSLIST', line=139)
W('32,2073', 0o54332, '', 'TS', 'DNLSTCOD', line=140)

W('32,2074', 0o32176, '', 'CAF', '20SEC', 'DELAY FOR 20 SEC WHILE THE AGS', line=142)
W('32,2075', 0o04616, '', 'TC', 'BANKCALL', 'DOWNLIST IS TRANSMITTED', line=143)
W('32,2076', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=144)

W('32,2077', 0o31324, '', 'CA', 'AGSWORD', line=146)
W('32,2100', 0o54332, '', 'TS', 'DNLSTCOD', 'RETURN TO THE OLD DOWNLIST', line=147)
W('32,2101', 0o34744, '', 'CAF', 'IMUSEBIT', line=148)
W('32,2102', 0o70074, '', 'MASK', 'FLAGWRD0', 'CHECK IMUSE FLAG.', line=149)
W('32,2103', 0o10000, '', 'CCS', 'A', line=150)
W('32,2104', 0o02122, '', 'TC', 'AGSEND', 'IMU IS BEING USED -- DO NOT ZERO', line=151)
W('32,2105', 0o11304, 'CKSTALL', 'CCS', 'IMUCADR', 'CHECK FOR IMU USAGE WHICH AVOIDS THE', line=152)
W('32,2106', 0o12111, '', 'TCF', '+3', 'IMUSE BIT:  I.E., IMU COMPENSATION.', line=153)
W('32,2107', 0o12115, '', 'TCF', '+6', 'FREE.  GO AHEAD WITH THE IMU ZERO.', line=154)
W('32,2110', 0o12111, '', 'TCF', '+1', line=155)
W('32,2111', 0o34363, '', 'CAF', 'TEN', 'WAIT .1 SEC AND TRY AGAIN.', line=156)
W('32,2112', 0o04616, '', 'TC', 'BANKCALL', line=157)
W('32,2113', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=158)
W('32,2114', 0o12105, '', 'TCF', 'CKSTALL', line=159)

W('32,2115', 0o04616, '', 'TC', 'BANKCALL', 'IMU IS NOT IN USE', line=161)
W('32,2116', 0o16714, '', 'CADR', 'IMUZERO', 'SET IMU ZERO DISCRETE FOR 320 MSECS.', kind='data', line=162)
W('32,2117', 0o04616, '', 'TC', 'BANKCALL', 'WAIT 3 SEC FOR COUNTERS TO INCREMENT', line=163)
W('32,2120', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=164)
W('32,2121', 0o02122, '', 'TC', 'AGSEND', line=165)
W('32,2122', 0o05516, 'AGSEND', 'TC', 'DOWNFLAG', 'ALLOW V37', line=166)
W('32,2123', 0o00054, '', 'ADRES', 'NODOFLAG', kind='data', line=167)

W('32,2124', 0o32173, '', 'CAF', 'V50N16', line=169)
W('32,2125', 0o04616, '', 'TC', 'BANKCALL', line=170)
W('32,2126', 0o20342, '', 'CADR', 'GOMARK3', kind='data', line=171)
W('32,2127', 0o15472, '', 'TCF', 'ENDEXT', line=172)
W('32,2130', 0o15472, '', 'TCF', 'ENDEXT', line=173)
W('32,2131', 0o05472, '', 'TC', 'ENDEXT', line=174)

W('32,2132', 0o64375, 'SCALEVEC', 'VLOAD', 'MXV', kind='interp', line=176)
W('32,2133', 0o00025, '', '', 'VATT1', kind='operand', line=177)
W('32,2134', 0o01734, '', '', 'REFSMMAT', kind='operand', line=178)
W('32,2135', 0o72561, '', 'VXSC', 'VSL2', kind='interp', line=179)
W('32,2136', 0o24202, '', '', 'VSCALE', kind='operand', line=180)
# Page 209
W('32,2137', 0o53255, '', 'VAD', 'VAD', 'THIS SECTION ROUNDS THE VECTOR, AND', kind='interp', line=182)
W('32,2140', 0o24204, '', '', 'AGSRND1', 'CORRECTS FOR THE FACT THAT THE AGS', kind='operand', line=183)
W('32,2141', 0o24212, '', '', 'AGSRND2', 'IS A 2 S COMPLEMENT MACHINE WHILE THE', kind='operand', line=184)
W('32,2142', 0o77634, '', 'RTB', '', 'LGC IS A 1 S COMPLEMENT MACHINE.', kind='interp', line=185)
W('32,2143', 0o21772, '', '', 'VECSGNAG', kind='operand', line=186)
W('32,2144', 0o24025, '', 'STOVL', 'VATT1', kind='interp', line=187)
W('32,2145', 0o00017, '', '', 'RATT1', kind='operand', line=188)
W('32,2146', 0o74321, '', 'MXV', 'VXSC', kind='interp', line=189)
W('32,2147', 0o01734, '', '', 'REFSMMAT', kind='operand', line=190)
W('32,2150', 0o24200, '', '', 'RSCALE', kind='operand', line=191)
W('32,2151', 0o53212, '', 'VSL8', 'VAD', 'AGAIN THIS SECTION ROUNDS.  TWO VECTORS', kind='interp', line=192)
W('32,2152', 0o24204, '', '', 'AGSRND1', 'ARE ADDED TO DEFEAT ALSIGNAG IN THE', kind='operand', line=193)
W('32,2153', 0o47055, '', 'VAD', 'RTB', 'CASE OF A HIGH-ORDER ZERO COUPLED WITH', kind='interp', line=194)
W('32,2154', 0o24212, '', '', 'AGSRND2', 'A LOW ORDER NEGATIVE PART.', kind='operand', line=195)
W('32,2155', 0o21772, '', '', 'VECSGNAG', kind='operand', line=196)
W('32,2156', 0o77750, '', 'LXA,1', kind='interp', line=197)
W('32,2157', 0o00024, '', '', 'VATT1', kind='operand', line=198)
W('32,2160', 0o72130, '', 'SXA,1', 'LXA,1', kind='interp', line=199)
W('32,2161', 0o00155, '', '', 'MPAC +1', kind='operand', line=200)
W('32,2162', 0o00026, '', '', 'VATT1 +2', kind='operand', line=201)
W('32,2163', 0o72130, '', 'SXA,1', 'LXA,1', kind='interp', line=202)
W('32,2164', 0o00160, '', '', 'MPAC +4', kind='operand', line=203)
W('32,2165', 0o00030, '', '', 'VATT1 +4', kind='operand', line=204)
W('32,2166', 0o43530, '', 'SXA,1', 'RVQ', kind='interp', line=205)
W('32,2167', 0o00162, '', '', 'MPAC +6', kind='operand', line=206)

S('LAGSLIST', 'equals', 0o4753, line=208)
W('32,2170', 0o00216, 'V01N14', 'VN', '0114', kind='data', line=209)
W('32,2171', 0o14400, 'V50N00A', 'VN', '5000', kind='data', line=210)
S('V00N25', 'equals', 0o6010, line=211)
W('32,2172', 0o01420, 'V06N16', 'VN', '0616', kind='data', line=212)
S('V00N34', 'equals', 0o4242, line=213)
W('32,2173', 0o14420, 'V50N16', 'VN', '5016', kind='data', line=214)
W('32,2174', 0o03100, 'TSCALE', '2DEC', '100 B-10', 'CSEC TO SEC SCALE FACTOR', kind='data', line=215)
W('32,2175', 0o00000, kind='data', line=215)
W('32,2176', 0o03720, '20SEC', 'DEC', '2000', kind='data', line=216)
W('32,2177', 0o15077, 'RSCALE', '2DEC', '3.280839 B-3', 'METERS TO FEET SCALE FACTOR', kind='data', line=217)
W('32,2200', 0o05041, kind='data', line=217)
W('32,2201', 0o24402, 'VSCALE', '2DEC', '3.280839 E2 B-9', 'METERS/CS TO FEET/SEC SCALE FACTOR', kind='data', line=218)
W('32,2202', 0o25724, kind='data', line=218)
W('32,2203', 0o00000, 'AGSRND1', '2OCT', '0000060000', kind='data', line=219)
W('32,2204', 0o60000, kind='data', line=219)
W('32,2205', 0o00000, '', '2OCT', '0000060000', kind='data', line=220)
W('32,2206', 0o60000, kind='data', line=220)
W('32,2207', 0o00000, '', '2OCT', '0000060000', kind='data', line=221)
W('32,2210', 0o60000, kind='data', line=221)
W('32,2211', 0o00000, 'AGSRND2', '2OCT', '0000037777', kind='data', line=222)
W('32,2212', 0o37777, kind='data', line=222)
W('32,2213', 0o00000, '', '2OCT', '0000037777', kind='data', line=223)
W('32,2214', 0o37777, kind='data', line=223)
# Page 210
W('32,2215', 0o00000, '', '2OCT', '0000037777', kind='data', line=225)
W('32,2216', 0o37777, kind='data', line=225)

#   SBANK= LOWSUPER  # FOR SUBSEQUENT LOW 2CADRS.
