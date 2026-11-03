"""P20-P25.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P20-P25.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 492-613 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P20_P25', 'P20-P25.agc', 'Luminary099', pages='492-613')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P20-P25.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Onno Hommes <ohommes@cmu.edu>.
# Website:      www.ibiblio.org/apollo.
# Pages:        0492-0613
# Mod history:  2009-05-26 OH   Transcribed from page images.
# 2009-06-05 RSB  Corrected a typos.
# 2009-06-06 RSB  Added a missing instruction, and a block
# of 3 missing instructions.
# 2009-06-07 RSB  Fixed a misprint.
# 2009-06-07 RSB  Changed the construct "2DEC E-6 B12"
# (which isn't legal in yaYUL) to
# "2DEC 1.0 E-6 B12".
# 2011-05-07 JL   Removed workarounds.

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

# Page 492
# RENDEZVOUS NAVIGATION PROGRAM 20
#
# PROGRAM DESCRIPTION
#
# MOD NO -- 2
# BY P. VOLANTE
#
# FUNCTIONAL DESCRIPTION
#
# THE PURPOSE OF THIS PROGRAM IS TO CONTROL THE RENDEZVOUS RADAR FROM
# STARTUP THROUGH ACQUISITION AND LOCKON TO THE CSM AND TO UPDATE EITHER
# THE LM OR CSM STATE VECTOR (AS SPECIFIED BY THE ASTRONAUT BY DSKY ENTRY)
# ON THE BASIS OF THE RR TRACKING DATA.
#
# CALLING SEQUENCE --
#
# ASTRONAUT REQUEST THROUGH DSKY V37E20E
#
# SUBROUTINES CALLED
#
# R02BOTH (IMU STATUS CHECK)                      FLAGUP
# GOFLASH (PINBALL-DISPLAY)                       FLAGDOWN
# R23LEM  (MANUAL ACQUISITION)                    BANKCALL
# LS201   (LOS DETERMINATION)                     TASKOVER
# LS202   (RANGE LIMIT TEST)
# R61LEM  (PREFERRED TRACKING ATTITUDE)
# R21LEM  (RR DESIGNATE)                          ENDOFJOB
# R22LEM  (DATA READ)                             GOPERF1
# R31LEM  (RENDEZVOUS PARAMETER DISPLAY)
# PRIOLARM (PRIORITY DISPLAY)
#
# NORMAL EXIT MODES --
#
# P20 MAY BE TERMINATED IN TWO WAYS -- ASTRONAUT SELECTION OF IDLING
# PROGRAM (P00) BY KEYING V37E00E OR BY KEYING IN V56E
#
# ALARM OR ABORT EXIT MODES --
#
# RANGE GREATER THAN 400 NM DISPLAY
#
# OUTPUT
#
# TRKMKCNT = NO OF RENDEZVOUS TRACKING MARKS TAKEN (COUNTER)
#
# ERASABLE INITIALIZATION REQUIRED
#
# FLAGS SET + RESET
#
# SRCHOPT, RNDVZFLG, ACMODFLG, VEHUPFLG, UPDATFLG, TRACKFLG
#
# DEBRIS
#
# CENTRALS -- A,Q,L

#   SBANK= LOWSUPER  # FOR LOW 2CADR'S.

#   BANK 33
#   SETLOC P20S
#   BANK

#   EBANK= LOSCOUNT
#   COUNT* $$/P20
S('PROG22', 'equals', 0o60000, line=98)
W('24,2000', 0o05327, 'PROG20', 'TC', '2PHSCHNG', line=99)
W('24,2001', 0o00004, '', 'OCT', '4', kind='data', line=100)
W('24,2002', 0o05022, '', 'OCT', '05022', kind='data', line=101)
W('24,2003', 0o26000, '', 'OCT', '26000', 'PRIORITY 26', kind='data', line=102)
W('24,2004', 0o02667, '', 'TC', 'LUNSFCHK', 'CHECK IF ON LUNAR SURFACE', line=103)
# Page 493
W('24,2005', 0o02007, '', 'TC', 'ORBCHGO', 'YES', line=105)
W('24,2006', 0o02036, '', 'TC', 'PROG20A -2', 'NO -- CONTINUE WITH P20', line=106)
W('24,2007', 0o05504, 'ORBCHGO', 'TC', 'UPFLAG', 'SET VEHUPFLG -- CSM STATE', line=107)
W('24,2010', 0o00026, '', 'ADRES', 'VEHUPFLG', 'VECTOR TO BE UPDATED', kind='data', line=108)
W('24,2011', 0o34753, '', 'CAF', 'ONE', 'SET R2 FOR OPTION CSM WILL NOT', line=109)
W('24,2012', 0o55145, '', 'TS', 'OPTION2', 'CHANGE PRESENT ORBIT', line=110)
W('24,2013', 0o32311, '', 'CAF', 'OCT00012', line=111)
W('24,2014', 0o04616, '', 'TC', 'BANKCALL', 'DISPLAY ASSUMED CSM ORBIT OPTION', line=112)
W('24,2015', 0o20633, '', 'CADR', 'GOPERF4', kind='data', line=113)
W('24,2016', 0o06001, '', 'TC', 'GOTOPOOH', 'TERMINATE', line=114)
W('24,2017', 0o02021, '', 'TC', 'ORBCHG1', 'PROCEED VALUE OF ASSUMED OPTION OK', line=115)
W('24,2020', 0o02013, '', 'TC', '-5', 'R2 LOADED THRU DSKY', line=116)
W('24,2021', 0o42312, 'ORBCHG1', 'CS', 'P22ONE', line=117)
W('24,2022', 0o61145, '', 'AD', 'OPTION2', line=118)
W('24,2023', 0o00006, '', 'EXTEND', line=119)
W('24,2024', 0o12040, '', 'BZF', 'PROG20A', line=120)
W('24,2025', 0o32315, '', 'CAF', 'V06N33*', line=121)
W('24,2026', 0o04616, '', 'TC', 'BANKCALL', 'FLASH VERB-NOUN TO REQUEST ESTIMATED', line=122)
W('24,2027', 0o20476, '', 'CADR', 'GOFLASH', 'TIME OF LAUNCH', kind='data', line=123)
W('24,2030', 0o06001, '', 'TC', 'GOTOPOOH', 'TERMINATE', line=124)
W('24,2031', 0o02033, '', 'TC', 'ORBCHG2', 'PROCEED VALUES OK', line=125)
W('24,2032', 0o02025, '', 'TC', '-5', 'TIME LOADED THRU DSKY', line=126)
W('24,2033', 0o06037, 'ORBCHG2', 'TC', 'INTPRET', line=127)
W('24,2034', 0o77650, '', 'GOTO', kind='interp', line=128)
W('24,2035', 0o64217, '', '', 'ORBCHG3', kind='operand', line=129)
#   BANK 32
#   SETLOC P20S4
#   BANK
#   COUNT* $$/P20

W('32,2217', 0o77624, 'ORBCHG3', 'CALL', kind='interp', line=135)
W('32,2220', 0o27414, '', '', 'INTSTALL', kind='operand', line=136)
W('32,2221', 0o77745, '', 'DLOAD', kind='interp', line=137)
W('32,2222', 0o03442, '', '', 'TIG', kind='operand', line=138)
W('32,2223', 0o03661, '', 'STORE', 'LNCHTM', kind='interp', line=139)
W('32,2224', 0o00041, '', 'STORE', 'TDEC1', 'ESTIMATED LAUNCH TIME', kind='interp', line=140)
W('32,2225', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=141)
W('32,2226', 0o01674, '', '', 'VINTFLAG', 'LM INTEGRATION', kind='operand', line=142)
W('32,2227', 0o01673, '', '', 'INTYPFLG', 'PRECISION -- ENCKE', kind='operand', line=143)
W('32,2230', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=144)
W('32,2231', 0o01676, '', '', 'DIM0FLAG', 'NO W-MATRIX', kind='operand', line=145)
W('32,2232', 0o01675, '', '', 'D6OR9FLG', kind='operand', line=146)
W('32,2233', 0o77624, '', 'CALL', kind='interp', line=147)
W('32,2234', 0o27134, '', '', 'INTEGRV', 'PLANETARY INERTIAL ORIENTATION', kind='operand', line=148)
W('32,2235', 0o77624, '', 'CALL', kind='interp', line=149)
W('32,2236', 0o11244, '', '', 'GRP2PC', kind='operand', line=150)
W('32,2237', 0o77775, '', 'VLOAD', kind='interp', line=151)
W('32,2240', 0o00017, '', '', 'RATT1', kind='operand', line=152)
W('32,2241', 0o17631, '', 'STODL', 'RSUBL', 'SAVE LM POSITION', kind='interp', line=153)
W('32,2242', 0o00015, '', '', 'TAT', kind='operand', line=154)
# Page 494
W('32,2243', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=156)
W('32,2244', 0o27414, '', '', 'INTSTALL', kind='operand', line=157)
W('32,2245', 0o43014, '', 'SET', 'CLEAR', kind='interp', line=158)
W('32,2246', 0o01474, '', '', 'VINTFLAG', 'CSM INTEGRATION', kind='operand', line=159)
W('32,2247', 0o01673, '', '', 'INTYPFLG', kind='operand', line=160)
W('32,2250', 0o43014, '', 'CLEAR', 'BOFF', kind='interp', line=161)
W('32,2251', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=162)
W('32,2252', 0o02756, '', '', 'RENDWFLG', 'W MATRIX VALID', kind='operand', line=163)
W('32,2253', 0o64257, '', '', 'NOWMATX', 'NO', kind='operand', line=164)
W('32,2254', 0o43014, '', 'SET', 'SET', 'YES -- SET FOR W MATRIX', kind='interp', line=165)
W('32,2255', 0o01476, '', '', 'DIM0FLAG', kind='operand', line=166)
W('32,2256', 0o01475, '', '', 'D6OR9FLG', kind='operand', line=167)
W('32,2257', 0o77624, 'NOWMATX', 'CALL', kind='interp', line=168)
W('32,2260', 0o27134, '', '', 'INTEGRV', 'CSM INTEGRATION', kind='operand', line=169)
W('32,2261', 0o77624, '', 'CALL', kind='interp', line=170)
W('32,2262', 0o11244, '', '', 'GRP2PC', kind='operand', line=171)
W('32,2263', 0o77775, '', 'VLOAD', kind='interp', line=172)
W('32,2264', 0o00025, '', '', 'VATT1', kind='operand', line=173)
W('32,2265', 0o25761, '', 'STOVL', 'VSUBC', 'SAVE CSM POSITION', kind='interp', line=174)
W('32,2266', 0o00017, '', '', 'RATT1', kind='operand', line=175)
W('32,2267', 0o01102, '', 'STORE', 'RSUBC', 'SAVE CSM POSITION', kind='interp', line=176)
W('32,2270', 0o53435, '', 'VXV', 'UNIT', 'COMPUTE NORMAL TO CSM ORBITAL PLANE', kind='interp', line=177)
W('32,2271', 0o01761, '', '', 'VSUBC', 'NSUB1=UNIT(R(CM) CROSS V(CM))', kind='operand', line=178)
W('32,2272', 0o24025, '', 'STOVL', '20D', 'SAVE NSUB1', kind='interp', line=179)
W('32,2273', 0o03631, '', '', 'RSUBL', 'COMPUTE ESTIMATED ORBITAL', kind='operand', line=180)
W('32,2274', 0o53435, '', 'VXV', 'UNIT', 'PLANE CHANGE', kind='interp', line=181)
W('32,2275', 0o00025, '', '', '20D', 'UCSM = UNIT(R(LM) CROSS NSUB1)', kind='operand', line=182)
W('32,2276', 0o27637, '', 'STOVL', 'UCSM', kind='interp', line=183)
W('32,2277', 0o01102, '', '', 'RSUBC', 'COMPUTE ANGLE BETWEEN UCSM', kind='operand', line=184)
W('32,2300', 0o50256, '', 'UNIT', 'DOT', 'AND RSUBC', kind='interp', line=185)
W('32,2301', 0o03637, '', '', 'UCSM', 'COS A = UCSM DOT UNIT (R(CM))', kind='operand', line=186)
W('32,2302', 0o77752, '', 'SL1', kind='interp', line=187)
W('32,2303', 0o02732, '', 'STORE', 'CSTH', 'SAVE DOE TIME-THETA SUBROUTINE', kind='interp', line=188)
W('32,2304', 0o44316, '', 'DSQ', 'BDSU', 'COMPUTE SINE A', kind='interp', line=189)
W('32,2305', 0o10314, '', '', 'ONEB-2', kind='operand', line=190)
W('32,2306', 0o77766, '', 'SQRT', kind='interp', line=191)
W('32,2307', 0o26730, '', 'STOVL', 'SNTH', 'SAVE FOR TIME-THETA SUBROUTINE', kind='interp', line=192)
W('32,2310', 0o01102, '', '', 'RSUBC', 'POSITION OF CSM AT EST. LAUNCH', kind='operand', line=193)
W('32,2311', 0o26655, '', 'STOVL', 'RVEC', 'TIME FOR TIME-THETHA  B-27', kind='interp', line=194)
W('32,2312', 0o01761, '', '', 'VSUBC', 'VELOCITY OF CSM AT EST. LAUNCH.', kind='operand', line=195)
W('32,2313', 0o77676, '', 'VCOMP', kind='interp', line=196)
W('32,2314', 0o02744, '', 'STORE', 'VVEC', 'TIME FOR TIME THETA   B-5', kind='interp', line=197)
W('32,2315', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=198)
W('32,2316', 0o03666, '', '', 'RVSW', kind='operand', line=199)
W('32,2317', 0o24732, '', '', 'TIMETHET', kind='operand', line=200)
W('32,2320', 0o77676, '', 'VCOMP', kind='interp', line=201)
W('32,2321', 0o03645, '', 'STORE', 'NEWVEL', 'TERMINAL VELOCITY OF CSM', kind='interp', line=202)
W('32,2322', 0o77745, '', 'DLOAD', kind='interp', line=203)
W('32,2323', 0o00037, '', '', 'T', kind='operand', line=204)
W('32,2324', 0o27663, '', 'STOVL', 'TRANSTM', 'TRANSFER TIME', kind='interp', line=205)
# Page 495
W('32,2325', 0o03645, '', '', 'NEWVEL', kind='operand', line=207)
W('32,2326', 0o77646, '', 'ABVAL', kind='interp', line=208)
W('32,2327', 0o24025, '', 'STOVL', '20D', kind='interp', line=209)
W('32,2330', 0o00001, '', '', '0D', kind='operand', line=210)
W('32,2331', 0o03653, '', 'STORE', 'NEWPOS', 'TERMINAL POSITION OF CSM', kind='interp', line=211)
W('32,2332', 0o53435, '', 'VXV', 'UNIT', 'COMPUTE NORMAL TO SCM ORBITAL PLANE', kind='interp', line=212)
W('32,2333', 0o03631, '', '', 'RSUBL', 'NSUB2 = UNIT(NEWPOS CROSS R(LM))', kind='operand', line=213)
W('32,2334', 0o53435, '', 'VXV', 'UNIT', 'ROTATE TERMINAL VEL INTO DESIRED', kind='interp', line=214)
W('32,2335', 0o03653, '', '', 'NEWPOS', 'ORBITAL PLANE', kind='operand', line=215)
W('32,2336', 0o76561, '', 'VXSC', 'VSL1', 'VSUBC = ABVAL(NEWVEL) $ UNIT (NSUB2', kind='interp', line=216)
W('32,2337', 0o00025, '', '', '20D', kind='operand', line=217)
W('32,2340', 0o37665, '', 'STCALL', 'NCSMVEL', 'NEW CSM VELOCITY', kind='interp', line=218)
W('32,2341', 0o11244, '', '', 'GRP2PC', kind='operand', line=219)
W('32,2342', 0o77624, '', 'CALL', kind='interp', line=220)
W('32,2343', 0o27414, '', '', 'INTSTALL', kind='operand', line=221)
W('32,2344', 0o44345, '', 'DLOAD', 'BDSU', kind='interp', line=222)
W('32,2345', 0o03663, '', '', 'TRANSTM', 'LAUNCH TIME -- TRANSFER TIME', kind='operand', line=223)
W('32,2346', 0o03661, '', '', 'LNCHTM', kind='operand', line=224)
W('32,2347', 0o25517, '', 'STOVL', 'TET', kind='interp', line=225)
W('32,2350', 0o03653, '', '', 'NEWPOS', kind='operand', line=226)
W('32,2351', 0o01535, '', 'STORE', 'RCV', kind='interp', line=227)
W('32,2352', 0o25503, '', 'STOVL', 'RRECT', kind='interp', line=228)
W('32,2353', 0o03665, '', '', 'NCSMVEL', kind='operand', line=229)
W('32,2354', 0o35511, '', 'STCALL', 'VRECT', kind='interp', line=230)
W('32,2355', 0o23455, '', '', 'MINIRECT', kind='operand', line=231)
W('32,2356', 0o45174, '', 'AXT,2', 'CALL', kind='interp', line=232)
W('32,2357', 0o00002, '', '', '2', kind='operand', line=233)
W('32,2360', 0o26661, '', '', 'ATOPCSM', kind='operand', line=234)
W('32,2361', 0o77624, '', 'CALL', kind='interp', line=235)
W('32,2362', 0o27423, '', '', 'INTWAKE0', kind='operand', line=236)
W('32,2363', 0o77776, '', 'EXIT', kind='interp', line=237)
W('32,2364', 0o04616, '', 'TC', 'BANKCALL', line=238)
W('32,2365', 0o50040, '', 'CADR', 'PROG20A', kind='data', line=239)

#   BANK 24
#   SETLOC P20S
#   BANK
#   COUNT* $$/P20

W('24,2036', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET VEHUPFLG -- LM STATE VECTOR', line=246)
W('24,2037', 0o00026, '', 'ADRES', 'VEHUPFLG', 'TO BE UPDATED', kind='data', line=247)
W('24,2040', 0o04616, 'PROG20A', 'TC', 'BANKCALL', line=248)
W('24,2041', 0o11254, '', 'CADR', 'R02BOTH', kind='data', line=249)
W('24,2042', 0o05504, '', 'TC', 'UPFLAG', line=250)
W('24,2043', 0o00027, '', 'ADRES', 'UPDATFLG', 'SET UPDATE FLAG', kind='data', line=251)
W('24,2044', 0o05504, '', 'TC', 'UPFLAG', line=252)
W('24,2045', 0o00031, '', 'ADRES', 'TRACKFLG', 'SET TRACK FLAG', kind='data', line=253)
W('24,2046', 0o05504, '', 'TC', 'UPFLAG', line=254)
W('24,2047', 0o00010, '', 'ADRES', 'RNDVZFLG', 'SET RENDEZVOUS FLAG', kind='data', line=255)
W('24,2050', 0o05516, '', 'TC', 'DOWNFLAG', line=256)
W('24,2051', 0o00037, '', 'ADRES', 'SRCHOPTN', 'INSURE SEARCH OPTION OFF', kind='data', line=257)
# Page 496
W('24,2052', 0o05516, '', 'TC', 'DOWNFLAG', 'ALSO MANUAL ACQUISITION FLAG RESET', line=259)
W('24,2053', 0o00040, '', 'ADRES', 'ACMODFLG', kind='data', line=260)
W('24,2054', 0o05516, '', 'TC', 'DOWNFLAG', 'TURN OFF R04FLAG TO ENSURE GETTING', line=261)
W('24,2055', 0o00063, '', 'ADRES', 'R04FLAG', "ALARM 521 IF CAN'T READ RADAR", kind='data', line=262)
W('24,2056', 0o05516, '', 'TC', 'DOWNFLAG', 'ENSURE R25 GIMBAL MONITOR IS ENABLED', line=263)
W('24,2057', 0o00126, '', 'ADRES', 'NORRMON', '(RESET NORRMON FLAG)', kind='data', line=264)
W('24,2060', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET LOS BEING COMPUTED FLAG', line=265)
W('24,2061', 0o00041, '', 'ADRES', 'LOSCMFLG', kind='data', line=266)
W('24,2062', 0o06011, '', 'TC', 'CLRADMOD', line=267)
W('24,2063', 0o05353, 'P20LEM1', 'TC', 'PHASCHNG', line=268)
W('24,2064', 0o04022, '', 'OCT', '04022', kind='data', line=269)
W('24,2065', 0o34755, '', 'CAF', 'ZERO', 'ZERO MARK COUNTER', line=270)
W('24,2066', 0o55462, '', 'TS', 'MARKCTR', line=271)
W('24,2067', 0o06037, '', 'TC', 'INTPRET', 'LOS DETERMINATION ROUTINE', line=272)
W('24,2070', 0o77634, '', 'RTB', kind='interp', line=273)
W('24,2071', 0o21573, '', '', 'LOADTIME', kind='operand', line=274)
W('24,2072', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=275)
W('24,2073', 0o51255, '', '', 'LPS20.1', kind='operand', line=276)
W('24,2074', 0o77624, '', 'CALL', kind='interp', line=277)
W('24,2075', 0o53565, '', '', 'LPS20.2', 'TEST RANGE R/UTINE', kind='operand', line=278)
W('24,2076', 0o77776, '', 'EXIT', kind='interp', line=279)
W('24,2077', 0o50154, '', 'INDEX', 'MPAC', line=280)
W('24,2100', 0o02101, '', 'TC', '+1', line=281)
W('24,2101', 0o02111, '', 'TC', 'P20LEMA', 'NORMAL RETURN WITHIN 400 N M', line=282)
W('24,2102', 0o32305, '526ALARM', 'CAF', 'ALRM526', 'ERROR EXIT -- RANGE > 400 N. MI.', line=283)
W('24,2103', 0o04616, '', 'TC', 'BANKCALL', line=284)
W('24,2104', 0o21562, '', 'CADR', 'PRIOLARM', kind='data', line=285)
W('24,2105', 0o06022, '', 'TC', 'GOTOV56', 'TERMINATE EXITS P20 VIA V56 CODING', line=286)
W('24,2106', 0o02102, '', 'TC', '-4', 'PROC (ILLEGAL)', line=287)
W('24,2107', 0o02063, '', 'TC', 'P20LEM1', 'ENTER RECYCLE', line=288)
W('24,2110', 0o05155, '', 'TC', 'ENDOFJOB', line=289)

W('24,2111', 0o05353, 'P20LEMA', 'TC', 'PHASCHNG', line=291)
W('24,2112', 0o04022, '', 'OCT', '04022', kind='data', line=292)
W('24,2113', 0o02667, '', 'TC', 'LUNSFCHK', 'CHECK LUNAR SURFACE FLAG (P22 FLAG)', line=293)
W('24,2114', 0o02117, '', 'TC', 'P20LEMB', line=294)
W('24,2115', 0o04616, '', 'TC', 'BANKCALL', line=295)
W('24,2116', 0o46116, '', 'CADR', 'R61LEM', 'PREFERRED TRACKING ATTITUDE ROUTINE', kind='data', line=296)
W('24,2117', 0o05353, 'P20LEMB', 'TC', 'PHASCHNG', line=297)
W('24,2120', 0o05022, '', 'OCT', '05022', 'RESTART AT PRIORITY 10 TO ALLOW V37', kind='data', line=298)
W('24,2121', 0o10000, '', 'OCT', '10000', 'REQUESTED PROGRAM TO RUN FIRST', kind='data', line=299)
W('24,2122', 0o37714, '', 'CAF', 'PRIO26', 'RESTORE PRIORITY 26', line=300)
W('24,2123', 0o05146, '', 'TC', 'PRIOCHNG', line=301)
W('24,2124', 0o30075, '', 'CA', 'FLAGWRD1', 'IS THE TRACK FLAG SET', line=302)
W('24,2125', 0o74747, '', 'MASK', 'TRACKBIT', line=303)
W('24,2126', 0o00006, '', 'EXTEND', line=304)
W('24,2127', 0o12232, '', 'BZF', 'P20LEMWT', 'BRANCH -- NO -- WAIT FOR IT TO BE SET', line=305)
W('24,2130', 0o34752, 'P20LEMB7', 'CAF', 'BIT2', 'IS RR AUTO MODE DISCRETE PRESENT', line=306)
W('24,2131', 0o00006, '', 'EXTEND', line=307)
# Page 497
W('24,2132', 0o02033, '', 'RAND', 'CHAN33', line=309)
W('24,2133', 0o00006, '', 'EXTEND', line=310)
W('24,2134', 0o12170, '', 'BZF', 'P20LEMB3', 'YES -- DO AUTOMATIC ACQUISITION (R21)', line=311)

W('24,2135', 0o46007, 'P20LEMB5', 'CS', 'OCT24', 'RADAR NOT IN AUTO CHECK IF', line=313)
W('24,2136', 0o61011, '', 'AD', 'MODREG', 'MAJOR MODE IS 20', line=314)
W('24,2137', 0o00006, '', 'EXTEND', line=315)
W('24,2140', 0o12153, '', 'BZF', 'P20LEMB6', 'BRANCH -- YES -- OKAY TO DO PLEASE PERFORM', line=316)

W('24,2141', 0o67746, '', 'AD', 'NEG2', 'ALSO CHECK FOR P22', line=318)
W('24,2142', 0o00006, '', 'EXTEND', line=319)
W('24,2143', 0o12153, '', 'BZF', 'P20LEMB6', 'BRANCH -- YES OK TO DO PLEASE PERFORM', line=320)
W('24,2144', 0o32307, '', 'CAF', 'ALRM514', 'TRACK FLAG SET -- FLASH PRIORITY ALARM 514 --', line=321)
W('24,2145', 0o04616, '', 'TC', 'BANKCALL', 'RADAR GOES OUT OF AUTO MODE WHILE IN USE', line=322)
W('24,2146', 0o21562, '', 'CADR', 'PRIOLARM', kind='data', line=323)
W('24,2147', 0o06022, '', 'TC', 'GOTOV56', 'TERMINATE EXITS VIA V56', line=324)
W('24,2150', 0o02117, '', 'TC', 'P20LEMB', 'PROCEED AND ENTER BOTH GO BACK', line=325)
W('24,2151', 0o02117, '', 'TC', 'P20LEMB', 'TO CHECK AUTO MODE AGAIN', line=326)
W('24,2152', 0o05155, '', 'TC', 'ENDOFJOB', line=327)
W('24,2153', 0o32306, 'P20LEMB6', 'CAF', 'OCT201', 'REQUEST RR AUTO MODE SELECTION', line=328)
W('24,2154', 0o04616, '', 'TC', 'BANKCALL', line=329)
W('24,2155', 0o20623, '', 'CADR', 'GOPERF1', kind='data', line=330)
W('24,2156', 0o06022, '', 'TC', 'GOTOV56', 'TERMINATE EXITS P20 VIA V56 CODING', line=331)
W('24,2157', 0o02117, '', 'TC', 'P20LEMB', 'PROCEED CHECKS AUTO MODE DISCRETE AGAIN', line=332)
W('24,2160', 0o02667, '', 'TC', 'LUNSFCHK', 'ENTER INDICATES MANUAL ACQUISITION (R23)', line=333)
W('24,2161', 0o02166, '', 'TC', 'P20LEMB2', 'YES -- R23 NOT ALLOWED -- TURN ON OPR ERROR', line=334)
W('24,2162', 0o03135, '', 'TC', 'R23LEM', 'NO -- DO MANUAL ACQUISITION', line=335)

W('24,2163', 0o05504, 'P20LEMB1', 'TC', 'UPFLAG', 'RETURN FROM R23 -- LOCKON ACHIEVED', line=337)
W('24,2164', 0o00040, '', 'ADRES', 'ACMODFLG', 'SET MANUAL FLAG AND GO BACK TO CHECK', kind='data', line=338)
W('24,2165', 0o02117, '', 'TC', 'P20LEMB', 'RR AUTO MODE', line=339)

W('24,2166', 0o04364, 'P20LEMB2', 'TC', 'FALTON', 'TURNS ON OPERATOR ERROR LIGHT ON DSKY', line=341)
W('24,2167', 0o02117, '', 'TC', 'P20LEMB', 'AND GOES BACK TO CHECK AUTO MODE', line=342)

W('24,2170', 0o40110, 'P20LEMB3', 'CS', 'RADMODES', 'ARE RR CDUS BEING ZEROED', line=344)
W('24,2171', 0o74737, '', 'MASK', 'RCDU0BIT', line=345)
W('24,2172', 0o00006, '', 'EXTEND', line=346)
W('24,2173', 0o12205, '', 'BZF', 'P20LEMB4', 'BRANCH -- YES -- WAIT', line=347)
W('24,2174', 0o34355, '', 'CAF', 'BIT13-14', 'IS SEARCH OR MANUAL ACQUISITION FLAG SET', line=348)
W('24,2175', 0o70076, '', 'MASK', 'FLAGWRD2', line=349)
W('24,2176', 0o00006, '', 'EXTEND', line=350)
W('24,2177', 0o12211, '', 'BZF', 'P20LEMC3', 'ZERO MEANS AUTOMATIC RR ACQUISITION', line=351)
W('24,2200', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET TO AUTO MODE', line=352)
W('24,2201', 0o00037, '', 'ADRES', 'SRCHOPTN', kind='data', line=353)
# Page 498
W('24,2202', 0o05516, '', 'TC', 'DOWNFLAG', line=355)
W('24,2203', 0o00040, '', 'ADRES', 'ACMODFLG', kind='data', line=356)
W('24,2204', 0o02232, '', 'TC', 'P20LEMWT', 'WAIT 2.5 SECONDS THEN GO TO RR DATA READ', line=357)

W('24,2205', 0o32304, 'P20LEMB4', 'CAF', '250DEC', line=359)
W('24,2206', 0o04616, '', 'TC', 'BANKCALL', 'WAIT 2.5 SECONDS WHILE RR CDUS ARE BEING', line=360)
W('24,2207', 0o01735, '', 'CADR', 'DELAYJOB', 'ZEROED -- THEN GO BACK AND CHECK AGAIN', kind='data', line=361)
W('24,2210', 0o02170, '', 'TC', 'P20LEMB3', line=362)

W('24,2211', 0o06037, 'P20LEMC3', 'TC', 'INTPRET', line=364)
W('24,2212', 0o77634, '', 'RTB', kind='interp', line=365)
W('24,2213', 0o21573, '', '', 'LOADTIME', kind='operand', line=366)
W('24,2214', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=367)
W('24,2215', 0o50316, '', '', 'UPPSV', kind='operand', line=368)
W('24,2216', 0o77776, 'P20LEMC4', 'EXIT', kind='interp', line=369)
W('24,2217', 0o05353, 'P20LEMC', 'TC', 'PHASCHNG', line=370)
W('24,2220', 0o04022, '', 'OCT', '04022', kind='data', line=371)
W('24,2221', 0o30074, '', 'CAE', 'FLAGWRD0', 'IS THE RENDEZVOUS FLAG SET', line=372)
W('24,2222', 0o74745, '', 'MASK', 'RNDVZBIT', line=373)
W('24,2223', 0o00006, '', 'EXTEND', line=374)
W('24,2224', 0o15155, '', 'BZF', 'ENDOFJOB', 'NO -- EXIT P20', line=375)
W('24,2225', 0o30075, '', 'CAE', 'FLAGWRD1', 'IS TRACK FLAG SET (BIT 5 FLAGWORD 1)', line=376)
W('24,2226', 0o74747, '', 'MASK', 'TRACKBIT', line=377)
W('24,2227', 0o00006, '', 'EXTEND', line=378)
W('24,2230', 0o12264, '', 'BZF', 'P20LEMD', 'BRANCH -- TRACK FLAG NOT ON -- WAIT 15 SECONDS', line=379)
W('24,2231', 0o02674, 'P20LEMF', 'TC', 'R21LEM', line=380)

W('24,2232', 0o32304, 'P20LEMWT', 'CAF', '250DEC', line=382)
W('24,2233', 0o05173, '', 'TC', 'TWIDDLE', 'USE INSTEAD OF WAITLIST SINCE SAME BANK', line=383)
W('24,2234', 0o02244, '', 'ADRES', 'P20LEMC1', 'WAIT 2.5 SECONDS', kind='data', line=384)
W('24,2235', 0o30075, '', 'CAE', 'FLAGWRD1', 'IS TRACK FLAG SET', line=385)
W('24,2236', 0o74747, '', 'MASK', 'TRACKBIT', line=386)
W('24,2237', 0o00006, '', 'EXTEND', line=387)
W('24,2240', 0o15155, '', 'BZF', 'ENDOFJOB', 'NO -- EXIT WITHOUT DOING 2.7 PHASE CHANGE', line=388)
W('24,2241', 0o05353, 'P20LMWT1', 'TC', 'PHASCHNG', line=389)
W('24,2242', 0o40072, '', 'OCT', '40072', kind='data', line=390)
W('24,2243', 0o05155, '', 'TC', 'ENDOFJOB', line=391)

W('24,2244', 0o30074, 'P20LEMC1', 'CAE', 'FLAGWRD0', 'IS RENDEZVOUS FLAG SET', line=393)
W('24,2245', 0o74745, '', 'MASK', 'RNDVZBIT', line=394)
W('24,2246', 0o00006, '', 'EXTEND', line=395)
W('24,2247', 0o15261, '', 'BZF', 'TASKOVER', 'NO -- EXIT P20/R22', line=396)
W('24,2250', 0o30075, '', 'CAE', 'FLAGWRD1', 'IS TRACK FLAG SET', line=397)
W('24,2251', 0o74747, '', 'MASK', 'TRACKBIT', line=398)
W('24,2252', 0o00006, '', 'EXTEND', line=399)
W('24,2253', 0o12261, '', 'BZF', 'P20LEMC2', "NO -- DON'T SCHEDULE R22 JOB", line=400)
# Page 499
W('24,2254', 0o37714, '', 'CAF', 'PRIO26', 'YES -- SCHEDULE R22 JOB (RR DATA READ)', line=402)
W('24,2255', 0o05105, '', 'TC', 'FINDVAC', line=403)
#   EBANK= LOSCOUNT
W('24,2256', 0o02627, '', '2CADR', 'R22LEM42', kind='data', line=405)
W('24,2257', 0o50067, kind='data', line=405)

W('24,2260', 0o05261, '', 'TC', 'TASKOVER', line=407)

W('24,2261', 0o05221, 'P20LEMC2', 'TC', 'FIXDELAY', 'TRACK FLAG NOT SET, WAIT 15 SECONDS', line=409)
W('24,2262', 0o02734, '', 'DEC', '1500', 'AND CHECK AGAIN', kind='data', line=410)

W('24,2263', 0o02244, '', 'TC', 'P20LEMC1', line=412)

W('24,2264', 0o32666, 'P20LEMD', 'CAF', '1500DEC', line=414)
W('24,2265', 0o05173, '', 'TC', 'TWIDDLE', 'WAITLIST FOR 15 SECONDS', line=415)
W('24,2266', 0o02270, '', 'ADRES', 'P20LEMD1', kind='data', line=416)
W('24,2267', 0o05155, '', 'TC', 'ENDOFJOB', line=417)

W('24,2270', 0o30075, 'P20LEMD1', 'CAE', 'FLAGWRD1', 'IS TRACK FLAG SET', line=419)
W('24,2271', 0o74747, '', 'MASK', 'TRACKBIT', line=420)
W('24,2272', 0o10000, '', 'CCS', 'A', line=421)
W('24,2273', 0o12277, '', 'TCF', 'P20LEMD2', 'YES -- SCHEDULE DESIGNATE JOB', line=422)
W('24,2274', 0o05221, '', 'TC', 'FIXDELAY', 'NO -- WAIT 15 SECONDS', line=423)
W('24,2275', 0o02734, '', 'DEC', '1500', kind='data', line=424)
W('24,2276', 0o02270, '', 'TC', 'P20LEMD1', line=425)

W('24,2277', 0o37714, 'P20LEMD2', 'CAF', 'PRIO26', 'SCHEDULE JOB TO DO R21', line=427)
W('24,2300', 0o05105, '', 'TC', 'FINDVAC', line=428)
#   EBANK= LOSCOUNT
W('24,2301', 0o02211, '', '2CADR', 'P20LEMC3', 'START AT PERM.  MEMORY INTEGRATION', kind='data', line=430)
W('24,2302', 0o50067, kind='data', line=430)

W('24,2303', 0o05261, '', 'TC', 'TASKOVER', line=432)

W('24,2304', 0o00372, '250DEC', 'DEC', '250', kind='data', line=434)
W('24,2305', 0o00526, 'ALRM526', 'OCT', '00526', kind='data', line=435)
W('24,2306', 0o00201, 'OCT201', 'OCT', '00201', kind='data', line=436)
W('24,2307', 0o00514, 'ALRM514', 'OCT', '514', kind='data', line=437)
W('24,2310', 0o00074, 'MAXTRIES', 'DEC', '60', kind='data', line=438)
W('24,2311', 0o00012, 'OCT00012', 'OCT', '00012', kind='data', line=439)
W('24,2312', 0o00001, 'P22ONE', 'OCT', '00001', kind='data', line=440)
W('24,2313', 0o10000, 'ONEB-2', '2DEC', '1.0 B-2', kind='data', line=441)
W('24,2314', 0o00000, kind='data', line=441)

W('24,2315', 0o01441, 'V06N33*', 'VN', '0633', kind='data', line=443)
W('24,2316', 0o45020, 'UPPSV', 'STQ', 'CALL', 'UPDATES PERMANENT STATE VECTORS', kind='interp', line=444)
W('24,2317', 0o01757, '', '', 'LS21X', '      TO PRESENT TIME', kind='operand', line=445)
W('24,2320', 0o27414, '', '', 'INTSTALL', kind='operand', line=446)
W('24,2321', 0o77624, '', 'CALL', kind='interp', line=447)
# Page 500
W('24,2322', 0o26644, '', '', 'SETIFLGS', kind='operand', line=449)
W('24,2323', 0o43014, '', 'BOF', 'SET', "IF W-MATRIX INVALID, DON'T INTEGRATE IT", kind='interp', line=450)
W('24,2324', 0o02756, '', '', 'RENDWFLG', kind='operand', line=451)
W('24,2325', 0o50336, '', '', 'UPPSV1', kind='operand', line=452)
W('24,2326', 0o01476, '', '', 'DIM0FLAG', 'SET DIM0FLAG TO INTEGRATE W-MATRIX', kind='operand', line=453)
W('24,2327', 0o43014, '', 'BON', 'SET', kind='interp', line=454)
W('24,2330', 0o04307, '', '', 'SURFFLAG', 'IF ON LUNAR SURFACE W IS 6X6', kind='operand', line=455)
W('24,2331', 0o50333, '', '', 'UPPSV5', kind='operand', line=456)
W('24,2332', 0o01475, '', '', 'D6OR9FLG', 'OTHERWISE 9X9', kind='operand', line=457)
W('24,2333', 0o77614, 'UPPSV5', 'BOF', kind='interp', line=458)
W('24,2334', 0o00747, '', '', 'VEHUPFLG', kind='operand', line=459)
W('24,2335', 0o50370, '', '', 'UPPSV3', kind='operand', line=460)
W('24,2336', 0o77614, 'UPPSV1', 'SET', kind='interp', line=461)
W('24,2337', 0o01474, '', '', 'VINTFLAG', kind='operand', line=462)
W('24,2340', 0o77624, '', 'CALL', kind='interp', line=463)
W('24,2341', 0o27134, '', '', 'INTEGRV', kind='operand', line=464)
W('24,2342', 0o77624, '', 'CALL', '', 'GROUP 2 PHASE CHANGE', kind='interp', line=465)
W('24,2343', 0o11244, '', '', 'GRP2PC', 'TO PROTECT INTEGRATION', kind='operand', line=466)
W('24,2344', 0o77624, '', 'CALL', kind='interp', line=467)
W('24,2345', 0o27414, '', '', 'INTSTALL', kind='operand', line=468)
W('24,2346', 0o43145, '', 'DLOAD', 'CLEAR', 'GET TETCSM TO STORE IN TDEC FOR LM INT.', kind='interp', line=469)
W('24,2347', 0o01571, '', '', 'TETCSM', kind='operand', line=470)
W('24,2350', 0o01674, '', '', 'VINTFLAG', kind='operand', line=471)
W('24,2351', 0o77624, 'UPPSV4', 'CALL', '', 'INTEGRATE OTHER VEHICLE', kind='interp', line=472)
W('24,2352', 0o26644, '', '', 'SETIFLGS', '      WITHOUT W-MATRIX', kind='operand', line=473)
W('24,2353', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=474)
W('24,2354', 0o27134, '', '', 'INTEGRV', kind='operand', line=475)
W('24,2355', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=476)
W('24,2356', 0o04347, '', '', 'SURFFLAG', kind='operand', line=477)
W('24,2357', 0o50216, '', '', 'P20LEMC4', kind='operand', line=478)
W('24,2360', 0o01661, '', '', 'RCVLEM', kind='operand', line=479)
W('24,2361', 0o77742, '', 'VSR2', kind='interp', line=480)
W('24,2362', 0o26352, '', 'STOVL', 'LMPOS', kind='interp', line=481)
W('24,2363', 0o01667, '', '', 'VCVLEM', kind='operand', line=482)
W('24,2364', 0o77742, '', 'VSR2', kind='interp', line=483)
W('24,2365', 0o02360, '', 'STORE', 'LMVEL', kind='interp', line=484)
W('24,2366', 0o77650, '', 'GOTO', kind='interp', line=485)
W('24,2367', 0o01757, '', '', 'LS21X', kind='operand', line=486)

W('24,2370', 0o45014, 'UPPSV3', 'CLEAR', 'CALL', kind='interp', line=488)
W('24,2371', 0o01674, '', '', 'VINTFLAG', kind='operand', line=489)
W('24,2372', 0o27134, '', '', 'INTEGRV', kind='operand', line=490)
W('24,2373', 0o77624, '', 'CALL', kind='interp', line=491)
W('24,2374', 0o11244, '', '', 'GRP2PC', kind='operand', line=492)
W('24,2375', 0o77624, '', 'CALL', kind='interp', line=493)
W('24,2376', 0o27414, '', '', 'INTSTALL', kind='operand', line=494)
W('24,2377', 0o71214, '', 'SET', 'DLOAD', kind='interp', line=495)
W('24,2400', 0o01474, '', '', 'VINTFLAG', kind='operand', line=496)
W('24,2401', 0o01643, '', '', 'TETLEM', 'GET TETLEM TO STORE IN TDEC FOR CSM INT.', kind='operand', line=497)
# Page 501
W('24,2402', 0o77650, '', 'GOTO', kind='interp', line=499)
W('24,2403', 0o50351, '', '', 'UPPSV4', kind='operand', line=500)
#   EBANK= LOSCOUNT
#   COUNT* $$/P22

# Page 502
# PROGRAM DESCRIPTION
#
# PREFERRED TRACKING ATTITUDE PROGRAM P25
# MOD NO -- 3
# BY P. VOLANTE
#
# FUNCTIONAL DESCRIPTION
#
# THE PURPOSE OF THIS PROGRAM IS TO COMPUTE THE PREFERRED TRACKING
# ATTITUDE OF THE LM TO CONTINUOUSLY POINT THE LM TRTACKING BEACON AT THE
# CSM AND TO PERFORM THE MANEUVER TO THE PREFERRED TRACKING ATTITUDE AND
# CONTINUOUSLY MAINTAIN THIS ATTITUDE WITHIN PRESCRIBED LIMITS.
#
# CALLING SEQUENCE --
#
# ASTRONAUT REQUEST THROUGH DSKY V37E25E
#
# SUBROUTINES CALLED --
#
# BANKCALL                                        FLAGUP
# R02BOTH (IMU STATUS CHECK)                      ENDOFJOB
# R61LEM  (PREF TRK ATT ROUT)                     WAITLIST
# TASKOVER                                        FINDVAC
#
# NORMAL EXIT MODES --
#
# P25 MAY BE TERMINATED IN TWO WAYS -- ASTRONAUT SELECTION OF IDLING
# PROGRAM (P00) BY KEYING V37E00E OR BY KEYING IN V56E
#
# ALARM OR ABORT EXIT MODES --
#
# NONE
#
# OUTPUT
#
# ERASABLE INITIALIZATION REQUIRED
#
# FLAGS SET + RESET
#
# TRACKFLG, P25FLAG
#
# DEBRIS
#
# NONE

#   EBANK= LOSCOUNT
#   COUNT* $$/P25
W('24,2404', 0o05327, 'PROG25', 'TC', '2PHSCHNG', line=552)
W('24,2405', 0o00004, '', 'OCT', '4', 'MAKE GROUP 4 INACTIVE (VERB 37)', kind='data', line=553)
W('24,2406', 0o05022, '', 'OCT', '05022', kind='data', line=554)
W('24,2407', 0o26000, '', 'OCT', '26000', 'PRIORITY 26', kind='data', line=555)

W('24,2410', 0o04616, '', 'TC', 'BANKCALL', line=557)
W('24,2411', 0o11254, '', 'CADR', 'R02BOTH', 'IMU STATUS CHECK', kind='data', line=558)
W('24,2412', 0o05504, '', 'TC', 'UPFLAG', line=559)
W('24,2413', 0o00031, '', 'ADRES', 'TRACKFLG', 'SET TRACK FLAG', kind='data', line=560)
W('24,2414', 0o05504, '', 'TC', 'UPFLAG', line=561)
W('24,2415', 0o00006, '', 'ADRES', 'P25FLAG', 'SET P25FLAG', kind='data', line=562)
W('24,2416', 0o05353, 'P25LEM1', 'TC', 'PHASCHNG', line=563)
W('24,2417', 0o04022, '', 'OCT', '04022', kind='data', line=564)
W('24,2420', 0o34743, '', 'CAF', 'P25FLBIT', line=565)
W('24,2421', 0o70074, '', 'MASK', 'STATE', 'IS P25FLAG SET', line=566)
W('24,2422', 0o00006, '', 'EXTEND', line=567)
W('24,2423', 0o15155, '', 'BZF', 'ENDOFJOB', line=568)
W('24,2424', 0o34747, '', 'CAF', 'TRACKBIT', 'IS TRACKFLAG SET?', line=569)
W('24,2425', 0o70075, '', 'MASK', 'STATE +1', line=570)
W('24,2426', 0o00006, '', 'EXTEND', line=571)
# Page 503
W('24,2427', 0o12437, '', 'BZF', 'P25LMWT1', 'NO -- SKIP PHASE CHANGE AND WAIT 1 MINUTE', line=573)
W('24,2430', 0o34757, '', 'CAF', 'SEVEN', 'CALL R65 -- FINE PREFERRED', line=574)
W('24,2431', 0o55745, '', 'TS', 'R65CNTR', line=575)
W('24,2432', 0o04616, '', 'TC', 'BANKCALL', 'TRACKING ATTITUDE ROUTINE', line=576)
W('24,2433', 0o46123, '', 'CADR', 'R65LEM', kind='data', line=577)
W('24,2434', 0o02416, '', 'TC', 'P25LEM1', 'THEN GO CHECK FLAGS', line=578)
W('24,2435', 0o05353, 'P25LEMWT', 'TC', 'PHASCHNG', line=579)
W('24,2436', 0o00112, '', 'OCT', '00112', kind='data', line=580)
W('24,2437', 0o32450, 'P25LMWT1', 'CAF', '60SCNDS', line=581)
W('24,2440', 0o05173, '', 'TC', 'TWIDDLE', 'WAIT ONE MINUTE THEN CHECK AGAIN', line=582)
W('24,2441', 0o02443, '', 'ADRES', 'P25LEM2', kind='data', line=583)
W('24,2442', 0o05155, '', 'TC', 'ENDOFJOB', line=584)
W('24,2443', 0o35024, 'P25LEM2', 'CAF', 'PRIO14', line=585)
W('24,2444', 0o05105, '', 'TC', 'FINDVAC', line=586)
#   EBANK= LOSCOUNT
W('24,2445', 0o02416, '', '2CADR', 'P25LEM1', kind='data', line=588)
W('24,2446', 0o50067, kind='data', line=588)

W('24,2447', 0o05261, '', 'TC', 'TASKOVER', line=590)
W('24,2450', 0o13560, '60SCNDS', 'DEC', '6000', kind='data', line=591)

# Page 504
# DATA READ ROUTINE 22 (LEM)
# PROGRAM DESCRIPTION
#
# MOD NO -- 2
# BY P. VOLANTE
#
# FUNCTIONAL DESCRIPTION
#
# TO PROCESS AUTOMATIC RR MARK DATA TO UPDATE THE STATE VECTOR OF EITHER
# LM OR CSM AS DEFINED IN THE RENDEZVOUS NAVIGATION PROGRAM (P20)
#
# CALLING SEQUENCE --
#
# TC      BANKCALL
# CADR    R22LEM
#
# SUBROUTINES CALLED --
#
# LSR22.1         GOFLASH         WAITLIST
# LSR22.2         PRIOLARM        BANKCALL
# LSR22.3         R61LEM
#
# NORMAL EXIT MODES --
#
# R22 WILL CONTINUE TO RECYCLE, UPDATING STATE VECTORS WITH RADAR DATA
# UNTIL P20 CEASES TO OPERATE (RENDEZVOUS FLAG SET TO ZERO) AT WHICH TIME
# R22 WILL TERMINATE SELF.
#
# ALARM OR ABORT EXIT MODES --
#
# PRIORITY ALARM
# PRIORITY ALARM 525 LOS NOT WITHIN 3 DEGREE LIMIT
#
# OUTPUT
#
# SEE OUTPUT FROM LSR22.3
#
# ERASABLE INITIALIZATION REQUIRED
#
# SEE LSR22.1, LSR22.2, LSR22.3
#
# FLAGS SET + RESET
#
# NOANGFLG
#
# DEBRIS
#
# SEE LSR22.1, LSR22.2, LSR22.3

#   EBANK= LRS22.1X
#   COUNT* $$/R22
W('24,2451', 0o05353, 'R22LEM', 'TC', 'PHASCHNG', line=645)
W('24,2452', 0o04022, '', 'OCT', '04022', kind='data', line=646)
W('24,2453', 0o34745, '', 'CAF', 'RNDVZBIT', 'IS RENDEZVOUS FLAG SET?', line=647)
W('24,2454', 0o70074, '', 'MASK', 'STATE', line=648)
W('24,2455', 0o00006, '', 'EXTEND', line=649)
W('24,2456', 0o15155, '', 'BZF', 'ENDOFJOB', 'NO -- EXIT R22 AND P20', line=650)
W('24,2457', 0o34747, '', 'CAF', 'TRACKBIT', 'IS TRACKFLAG SET?', line=651)
W('24,2460', 0o70075, '', 'MASK', 'STATE +1', line=652)
W('24,2461', 0o00006, '', 'EXTEND', line=653)
W('24,2462', 0o12636, '', 'BZF', 'R22WAIT', 'NO WAIT', line=654)
W('24,2463', 0o34736, 'R22LEM12', 'CAF', 'BIT14', 'IS RR AUTO TRACK ENABLE DISCRETE STILL', line=655)
W('24,2464', 0o00006, '', 'EXTEND', '', 'ON (A MONITOR REPOSITION BY R25 CLEARS IT)', line=656)
W('24,2465', 0o02012, '', 'RAND', 'CHAN12', line=657)
W('24,2466', 0o00006, '', 'EXTEND', line=658)
W('24,2467', 0o12111, '', 'BZF', 'P20LEMA', 'NO -- RETURN TO P20', line=659)
W('24,2470', 0o34752, '', 'CAF', 'BIT2', 'YES', line=660)
W('24,2471', 0o00006, '', 'EXTEND', '', 'IS RR AUTO MODE DISCRETE PRESENT', line=661)
W('24,2472', 0o02033, '', 'RAND', 'CHAN33', line=662)
# Page 505
W('24,2473', 0o00006, '', 'EXTEND', line=664)
W('24,2474', 0o12476, '', 'BZF', '+2', 'YES CONTINUE', line=665)
W('24,2475', 0o02135, '', 'TC', 'P20LEMB5', 'NO -- SET IT', line=666)
W('24,2476', 0o40110, '', 'CS', 'RADMODES', 'ARE RR CDUS BEING ZEROED', line=667)
W('24,2477', 0o74737, '', 'MASK', 'RCDU0BIT', line=668)
W('24,2500', 0o00006, '', 'EXTEND', line=669)
W('24,2501', 0o12627, '', 'BZF', 'R22LEM42', 'CDUS BEING ZEROED', line=670)
W('24,2502', 0o05353, '', 'TC', 'PHASCHNG', 'IF A RESTART OCCURS, AND EXTRA RADAR', line=671)
W('24,2503', 0o00152, '', 'OCT', '00152', "READING IS TAKEN, SO BAD DATA ISN'T USED", kind='data', line=672)
W('24,2504', 0o04616, '', 'TC', 'BANKCALL', 'YES READ DATA + CALCULATE LOS', line=673)
W('24,2505', 0o64366, '', 'CADR', 'LRS22.1', 'DATA READ SUBROUTINE', kind='data', line=674)
W('24,2506', 0o50154, '', 'INDEX', 'MPAC', line=675)
W('24,2507', 0o02510, '', 'TC', '+1', line=676)
W('24,2510', 0o02531, '', 'TC', 'R22LEM2', 'NORMAL RETURN (GOOD DATA)', line=677)
W('24,2511', 0o02217, '', 'TC', 'P20LEMC', 'COULD NOT READ RADAR -- TRY TO REDESIGNATE', line=678)
W('24,2512', 0o32663, '', 'CAF', 'ALRM525', 'RR LOS NOT WITHIN 3 DEGREES (ALARM)', line=679)
W('24,2513', 0o04616, '', 'TC', 'BANKCALL', line=680)
W('24,2514', 0o21562, '', 'CADR', 'PRIOLARM', kind='data', line=681)
W('24,2515', 0o06022, '', 'TC', 'GOTOV56', 'TERMINATE EXITS P20 VIA V56 CODING', line=682)
W('24,2516', 0o02521, '', 'TC', 'R22LEM1', 'PROC (DISPLAY DELTA THETA)', line=683)
W('24,2517', 0o02512, '', 'TC', '-5', 'ENTER (ILLEGAL OPTION)', line=684)
W('24,2520', 0o05155, '', 'TC', 'ENDOFJOB', line=685)

W('24,2521', 0o05353, 'R22LEM1', 'TC', 'PHASCHNG', line=687)
W('24,2522', 0o04022, '', 'OCT', '04022', kind='data', line=688)
W('24,2523', 0o32664, '', 'CAF', 'V06N05', 'DISPLAY DELTA THETA', line=689)
W('24,2524', 0o04616, '', 'TC', 'BANKCALL', line=690)
W('24,2525', 0o20507, '', 'CADR', 'PRIODSP', kind='data', line=691)
W('24,2526', 0o06022, '', 'TC', 'GOTOV56', 'TERMINATE EXITS P20 VIA V56 CODING', line=692)
W('24,2527', 0o02531, '', 'TC', 'R22LEM2', 'PROC (OK CONTINUE)', line=693)
W('24,2530', 0o02217, '', 'TC', 'P20LEMC', 'ENTER (RECYCLE)', line=694)
W('24,2531', 0o05353, 'R22LEM2', 'TC', 'PHASCHNG', line=695)
W('24,2532', 0o04022, '', 'OCT', '04022', kind='data', line=696)
W('24,2533', 0o02667, '', 'TC', 'LUNSFCHK', 'CHECK IF ON LUNAR SURFACE (P22FLAG SET)', line=697)
W('24,2534', 0o02551, '', 'TC', 'R22LEM3', 'YES -- BYPASS FLAG CHECKS AND LRS22.2', line=698)
W('24,2535', 0o30075, '', 'CA', 'FLAGWRD1', 'IS TRACK FLAG SET', line=699)
W('24,2536', 0o74747, '', 'MASK', 'TRACKBIT', line=700)
W('24,2537', 0o00006, '', 'EXTEND', line=701)
W('24,2540', 0o12636, '', 'BZF', 'R22WAIT', 'NO -- WAIT', line=702)
W('24,2541', 0o04616, '', 'TC', 'BANKCALL', 'YES', line=703)
W('24,2542', 0o51333, '', 'CADR', 'LRS22.2', 'CHECKS RR BORESIGHT WITHIN 30 DEG OF +Z', kind='data', line=704)
W('24,2543', 0o50154, '', 'INDEX', 'MPAC', line=705)
W('24,2544', 0o02545, '', 'TC', '+1', line=706)
W('24,2545', 0o02551, '', 'TC', 'R22LEM3', 'NORMAL RETURN (LOS WITHIN 30 OF Z-AXIS)', line=707)
W('24,2546', 0o04616, '', 'TC', 'BANKCALL', line=708)
W('24,2547', 0o46116, '', 'CADR', 'R61LEM', kind='data', line=709)
W('24,2550', 0o02636, '', 'TC', 'R22WAIT', 'NOT WITHIN 30 DEG OF Z-AXIS', line=710)
W('24,2551', 0o40075, 'R22LEM3', 'CS', 'FLAGWRD1', 'SHOULD WE BYPASS STATE VECTOR UPDATE', line=711)
W('24,2552', 0o74746, '', 'MASK', 'NOUPFBIT', '(IS NO UPDATE FLAG SET?)', line=712)
# Page 506
W('24,2553', 0o00006, '', 'EXTEND', line=714)
W('24,2554', 0o12627, '', 'BZF', 'R22LEM42', 'BRANCH -- YES', line=715)
W('24,2555', 0o30075, '', 'CA', 'FLAGWRD1', 'IS UPDATE FLAG SET', line=716)
W('24,2556', 0o74745, '', 'MASK', 'UPDATBIT', line=717)
W('24,2557', 0o00006, '', 'EXTEND', line=718)
W('24,2560', 0o12627, '', 'BZF', 'R22LEM42', 'UPDATE FLAG NOT SET', line=719)
W('24,2561', 0o37714, '', 'CAF', 'PRIO26', 'INSURE HIGH PRIO IN RESTART', line=720)
W('24,2562', 0o55056, '', 'TS', 'PHSPRDT2', line=721)

W('24,2563', 0o06037, '', 'TC', 'INTPRET', line=723)
W('24,2564', 0o77650, '', 'GOTO', kind='interp', line=724)
W('24,2565', 0o54412, '', '', 'LSR22.3', kind='operand', line=725)
W('24,2566', 0o77776, 'R22LEM93', 'EXIT', '', 'NORMAL EXIT FROM LSR22.3', kind='interp', line=726)
W('24,2567', 0o05353, '', 'TC', 'PHASCHNG', 'PHASE CHANGE TO PROTECT AGAINST', line=727)
W('24,2570', 0o04022, '', 'OCT', '04022', 'CONFLICT WITH GRP2PC ERASEABLE', kind='data', line=728)
W('24,2571', 0o12622, '', 'TCF', 'R22LEM44', line=729)
W('24,2572', 0o77776, 'R22LEM96', 'EXIT', kind='interp', line=730)
W('24,2573', 0o34755, '', 'CAF', 'ZERO', 'SET N49FLAG = ZERO TO INDICATE', line=731)
W('24,2574', 0o55746, '', 'TS', 'N49FLAG', "V06 N49 DISPLAY HASN'T BEEN ANSWERED", line=732)
W('24,2575', 0o05353, '', 'TC', 'PHASCHNG', line=733)
W('24,2576', 0o04022, '', 'OCT', '04022', 'TO PROTECT DISPLAY', kind='data', line=734)
W('24,2577', 0o37715, '', 'CAF', 'PRIO27', 'PROTECT DISPLAY', line=735)
W('24,2600', 0o05072, '', 'TC', 'NOVAC', line=736)
#   EBANK= N49FLAG
W('24,2601', 0o02644, '', '2CADR', 'N49DSP', kind='data', line=738)
W('24,2602', 0o50067, kind='data', line=738)

W('24,2603', 0o06037, '', 'TC', 'INTPRET', line=740)
W('24,2604', 0o77735, '', 'SLOAD', kind='interp', line=741)
W('24,2605', 0o03747, '', '', 'N49FLAG', kind='operand', line=742)
W('24,2606', 0o50054, '', 'BZE', 'BMN', 'LOOP TO CHECK IF FLAG', kind='interp', line=743)
W('24,2607', 0o50604, '', '', '-3', 'SETTING CHANGED -- BRANCH -- NO', kind='operand', line=744)
W('24,2610', 0o50616, '', '', 'R22LEM7', 'PROCEED', kind='operand', line=745)
W('24,2611', 0o77776, '', 'EXIT', '', 'DISPLAY ANSERED BY RECYCLE', kind='interp', line=746)
W('24,2612', 0o02667, '', 'TC', 'LUNSFCHK', 'ARE WE ON LUNAR SURFACE', line=747)
W('24,2613', 0o02636, '', 'TC', 'R22WAIT', 'YES -- 15 SECOND DELAY', line=748)
W('24,2614', 0o34755, '', 'CA', 'ZERO', 'NO -- SET R65COUNTER = 0, DO FINE', line=749)
W('24,2615', 0o02632, '', 'TC', 'R22LEM45', 'TRACKING TAKE ANOTHER RADAR READING', line=750)
W('24,2616', 0o77624, 'R22LEM7', 'CALL', '', 'PROCEED', kind='interp', line=751)
W('24,2617', 0o11244, '', '', 'GRP2PC', 'PHASE CHANGE AND', kind='operand', line=752)
W('24,2620', 0o77650, '', 'GOTO', '', 'GO TO INCOPORATE DATA.', kind='interp', line=753)
W('24,2621', 0o55431, '', '', 'ASTOK', kind='operand', line=754)
W('24,2622', 0o25462, 'R22LEM44', 'INCR', 'MARKCTR', 'INCREMENT COUNT OF MARKS INCORPORATED.', line=755)
W('24,2623', 0o02667, '', 'TC', 'LUNSFCHK', 'ARE WE ON LUNAR SURFACE', line=756)
W('24,2624', 0o02640, '', 'TC', 'R22LEM46', 'YES -- WAIT 2 SECONDS', line=757)
W('24,2625', 0o34756, '', 'CA', 'FIVE', 'NOT ON LUNAR SURFACE', line=758)
W('24,2626', 0o02632, '', 'TC', 'R22LEM45', 'R65COUNTER = 5', line=759)
W('24,2627', 0o02667, 'R22LEM42', 'TC', 'LUNSFCHK', 'CHECK IF ON LUNAR SURFACE (P22FLAG SET)', line=760)
W('24,2630', 0o02640, '', 'TC', 'R22LEM46', 'YES -- WAIT 2 SECONDS', line=761)
W('24,2631', 0o34752, '', 'CA', 'TWO', 'NO -- SET R65COUNTER = 2', line=762)
W('24,2632', 0o55745, 'R22LEM45', 'TS', 'R65CNTR', line=763)
# Page 507
W('24,2633', 0o04616, '', 'TC', 'BANKCALL', line=765)
W('24,2634', 0o46123, '', 'CADR', 'R65LEM', 'FINE PREFERRED TRACKING ATTITUDE', kind='data', line=766)
W('24,2635', 0o02451, '', 'TC', 'R22LEM', line=767)
W('24,2636', 0o32666, 'R22WAIT', 'CAF', '1500DEC', line=768)
W('24,2637', 0o02233, '', 'TC', 'P20LEMWT +1', line=769)

W('24,2640', 0o35000, 'R22LEM46', 'CAF', '2SECS', line=771)
W('24,2641', 0o04616, '', 'TC', 'BANKCALL', 'WAIT 2 SECONDS AND TAKE ANOTHER MARK', line=772)
W('24,2642', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=773)
W('24,2643', 0o02451, '', 'TC', 'R22LEM', line=774)

W('24,2644', 0o32665, 'N49DSP', 'CAF', 'V06N49NB', line=776)
W('24,2645', 0o04616, '', 'TC', 'BANKCALL', 'EXCESSIVE STATE VECTOR UPDATE -- FLASH', line=777)
W('24,2646', 0o20507, '', 'CADR', 'PRIODSP', 'VERB 06 NOUN 49 R1=DELTA R, R2=DELTA V', kind='data', line=778)
W('24,2647', 0o06022, '', 'TC', 'GOTOV56', 'TERMINATE -- EXIT R22 AND P20', line=779)
W('24,2650', 0o44753, '', 'CS', 'ONE', 'PROCEED -- N49FLAG = -1', line=780)
W('24,2651', 0o55746, '', 'TS', 'N49FLAG', 'RECYCLE -- N49FLAG = + VALUE', line=781)
W('24,2652', 0o05155, '', 'TC', 'ENDOFJOB', line=782)
W('24,2653', 0o05353, 'R22RSTRT', 'TC', 'PHASCHNG', 'IF A RESTART OCCURS WHILE READING RADAR', line=783)
W('24,2654', 0o00152, '', 'OCT', '00152', 'COME HERE TO TAKE A RANGE-RATE READING', kind='data', line=784)
W('24,2655', 0o04616, '', 'TC', 'BANKCALL', "WHICH ISN'T USED TO PREVENT TAKING A BAD", line=785)
W('24,2656', 0o53103, '', 'CADR', 'RRRDOT', 'READING AND TRYING TO INCORPORATE THE', kind='data', line=786)
W('24,2657', 0o04616, '', 'TC', 'BANKCALL', 'BAD DATA', line=787)
W('24,2660', 0o17714, '', 'CADR', 'RADSTALL', 'WAIT FOR READ COMPLETE', kind='data', line=788)
W('24,2661', 0o02217, '', 'TC', 'P20LEMC', 'COULD NOT READ RADAR -- TRY TO REDISGNATE', line=789)
W('24,2662', 0o02451, '', 'TC', 'R22LEM', 'READ SUCCESSFUL -- CONTINUE AT R22', line=790)

W('24,2663', 0o00525, 'ALRM525', 'OCT', '00525', kind='data', line=792)
W('24,2664', 0o01405, 'V06N05', 'VN', '00605', kind='data', line=793)
W('24,2665', 0o01461, 'V06N49NB', 'VN', '00649', kind='data', line=794)
W('24,2666', 0o02734, '1500DEC', 'DEC', '1500', kind='data', line=795)

# LUNSFCHECK -- CLOSED SUBROUTINE TO CHECK IF ON LUNAR SURFACE (P22FLAG)
# RETURNS TO CALLER +1 IF P22FLAG SET
# TO CALLER +2 IF P22FLAG NOT SET

#   COUNT* $$/P22
W('24,2667', 0o40104, 'LUNSFCHK', 'CS', 'FLAGWRD8', 'CHECK IF ON LUNAR SURFACE', line=802)
W('24,2670', 0o74744, '', 'MASK', 'SURFFBIT', 'IS SURFFLAG SET?', line=803)
W('24,2671', 0o10000, '', 'CCS', 'A', 'BRANCH -- P22FLAG SET', line=804)
W('24,2672', 0o24002, '', 'INCR', 'Q', 'NOT SET', line=805)
W('24,2673', 0o00002, '', 'TC', 'Q', 'RETURN', line=806)

# Page 508
# RR DESIGNATE ROUTINE (R21LEM)
# PROGRAM DESCRIPTION
#
# MOD NO -- 2
# BY P. VOLANTE
#
# FUNCTIONAL DESCRIPTION
#
# TO POINT THE RENDEZVOUS RADAR AT THE CSM UNTIL AUTOMATIC ACQUISITION
# OF THE CSM IS ACCOMPLISHED BY THE RADAR.  ROUTINE IS CALLED BY P20.
#
# CALLING SEQUENCE --
#
# TC      BANKCALL
# CADR    R21LEM
#
# SUBROUTINES CALLED --
#
# FINDVAC         FLAGUP          ENDOFJOB        PRIOLARM
# NOVAC           INTPRET         LPS20.1         PHASCHNG
# WAITLIST        JOBSLEEP        JOBWAKE         FLAGDOWN
# TASKOVER        BANKCALL        RADSTALL        RRDESSM
#
# NORMAL EXIT MODES
#
# WHEN LOCK-ON IS ACHIEVED, BRANCH WILL BE TO P20 WHERE R22 (DATA READ
# WILL BE SELECTED OR A NEED FOR A MANEUVER (BRANCH TO P20LEMA)
#
# ALARM OR ABORT EXIT MODES --
#
# PRIORITY ALARM 503 WHEN LOCK-ON HASN'T BEEN ACHIEVED AFTER 30SECS --
# THIS REQUIRES ASTRONAUT INTERFACE: SELECTION OF SEARCH OPTION OF
# ACQUISITION
#
# OUTPUT
#
# SEE LPS20.1, RRDESSM
#
# ERASABLE INITIALIZATION REQUIRED
#
# RRTARGET, RADMODES ARE USED BY LPS20.1 AND RRDESSM
#
# FLAGS SET + RESET
#
# LOSCMFLG        LOKONSW
#
# DEBRIS
#
# SEE LPS20.1, RRSESSM

#   EBANK= LOSCOUNT
#   COUNT* $$/R21
W('24,2674', 0o44736, 'R21LEM', 'CS', 'BIT14', 'REMOVE RR SELF TRACK ENABLE', line=861)
W('24,2675', 0o00006, '', 'EXTEND', line=862)
W('24,2676', 0o03012, '', 'WAND', 'CHAN12', line=863)
W('24,2677', 0o02667, '', 'TC', 'LUNSFCHK', line=864)
W('24,2700', 0o02705, '', 'TC', 'R21LEM5', line=865)
W('24,2701', 0o34755, '', 'CAF', 'ZERO', 'COMMAND ANTENNA TO MODE CENTER', line=866)
W('24,2702', 0o55107, '', 'TS', 'TANG', 'IF NOT ON SURFACE -- MODE 1 -- (T=0,S=0)', line=867)
W('24,2703', 0o55110, '', 'TS', 'TANG +1', line=868)
W('24,2704', 0o02715, '', 'TC', 'R21LEM6', line=869)
W('24,2705', 0o34740, 'R21LEM5', 'CAF', 'BIT12', line=870)
W('24,2706', 0o70110, '', 'MASK', 'RADMODES', line=871)
W('24,2707', 0o10000, '', 'CCS', 'A', line=872)
W('24,2710', 0o02725, '', 'TC', 'R21LEM10', line=873)
W('24,2711', 0o34735, '', 'CAF', 'BIT15', line=874)
W('24,2712', 0o55107, '', 'TS', 'TANG', line=875)
W('24,2713', 0o44736, '', 'CS', 'HALF', line=876)
W('24,2714', 0o55110, '', 'TS', 'TANG +1', line=877)

# Page 509
W('24,2715', 0o05516, 'R21LEM6', 'TC', 'DOWNFLAG', line=880)
W('24,2716', 0o00012, '', 'ADRES', 'LOKONSW', kind='data', line=881)
W('24,2717', 0o04616, '', 'TC', 'BANKCALL', line=882)
W('24,2720', 0o52475, '', 'CADR', 'RRDESNB', kind='data', line=883)
W('24,2721', 0o02722, '', 'TC', '+1', line=884)
W('24,2722', 0o04616, '', 'TC', 'BANKCALL', line=885)
W('24,2723', 0o17714, '', 'CADR', 'RADSTALL', kind='data', line=886)
W('24,2724', 0o02760, '', 'TC', 'R21-503', 'BAD RETURN FROM DESIGNATE -- ISSUE ALARM', line=887)
W('24,2725', 0o05504, 'R21LEM10', 'TC', 'UPFLAG', line=888)
W('24,2726', 0o00041, '', 'ADRES', 'LOSCMFLG', 'EVERY FOURTH PASS THRU DODES', kind='data', line=889)
W('24,2727', 0o32310, '', 'CAF', 'MAXTRIES', 'ALLOW 60 PASSES (APPROX 45 SECONDS)', line=890)
W('24,2730', 0o55114, '', 'TS', 'DESCOUNT', 'TO DESIGNATE AND LOCK ON', line=891)
W('24,2731', 0o36245, 'R21LEM2', 'CAF', 'THREE', line=892)
W('24,2732', 0o55456, '', 'TS', 'LOSCOUNT', line=893)
W('24,2733', 0o06037, 'R21LEM1', 'TC', 'INTPRET', line=894)
W('24,2734', 0o43234, '', 'RTB', 'DAD', kind='interp', line=895)
W('24,2735', 0o21573, '', '', 'LOADTIME', kind='operand', line=896)
W('24,2736', 0o11120, '', '', 'HALFSEC', 'EXTRAPOLATE TO PRESENT TIME + .5 SEC.', kind='operand', line=897)
W('24,2737', 0o34041, '', 'STCALL', 'TDEC1', 'LOS DETERMINATION ROUTINE', kind='interp', line=898)
W('24,2740', 0o51255, '', '', 'LPS20.1', kind='operand', line=899)
W('24,2741', 0o77776, '', 'EXIT', kind='interp', line=900)
W('24,2742', 0o05504, 'R21LEM3', 'TC', 'UPFLAG', 'SET LOKONSW TO RADAR -- ON DESIRED', line=901)
W('24,2743', 0o00012, '', 'ADRES', 'LOKONSW', kind='data', line=902)
W('24,2744', 0o05516, '', 'TC', 'DOWNFLAG', line=903)
W('24,2745', 0o00126, '', 'ADRES', 'NORRMON', kind='data', line=904)
W('24,2746', 0o06037, '', 'TC', 'INTPRET', line=905)
W('24,2747', 0o77624, '', 'CALL', '', 'INPUT (RRTARGET UPDATED BY LPS20.1)', kind='interp', line=906)
W('24,2750', 0o52373, '', '', 'RRDESSM', 'DESIGNATE ROUTINE', kind='operand', line=907)
W('24,2751', 0o77776, '', 'EXIT', kind='interp', line=908)
W('24,2752', 0o02777, '', 'TC', 'R21LEM4', 'LOS NOT IN MODE 2 COVERAGE', line=909)
# ON LUNAR SURFACE
W('24,2753', 0o02111, '', 'TC', 'P20LEMA', 'VEHICLE MANEUVER REQUIRED.', line=911)
W('24,2754', 0o04616, '', 'TC', 'BANKCALL', 'NO VEHICLE MANEUVER REQUIRED', line=912)
W('24,2755', 0o17714, '', 'CADR', 'RADSTALL', 'WAIT FOR DESIGNATE COMPLETE -- LOCKON OR', kind='data', line=913)
W('24,2756', 0o02760, '', 'TC', '+2', 'BAD END -- LOCKON NOT ACHIEVED IN 60 TRIES', line=914)
W('24,2757', 0o02767, '', 'TC', 'R21END', 'EXIT ROUTINE RETURN TO P20 (LOCK-ON)', line=915)
W('24,2760', 0o32775, 'R21-503', 'CAF', 'ALRM503', 'ISSUE ALARM 503', line=916)
W('24,2761', 0o04616, '', 'TC', 'BANKCALL', line=917)
W('24,2762', 0o21562, '', 'CADR', 'PRIOLARM', kind='data', line=918)
W('24,2763', 0o06022, '', 'TC', 'GOTOV56', 'TERMINATE EXITS P20 VIA V56 CODING', line=919)
W('24,2764', 0o02772, '', 'TC', 'R21SRCH', 'PROC', line=920)
W('24,2765', 0o02211, '', 'TC', 'P20LEMC3', line=921)
W('24,2766', 0o05155, '', 'TC', 'ENDOFJOB', line=922)
W('24,2767', 0o05516, 'R21END', 'TC', 'DOWNFLAG', line=923)
W('24,2770', 0o00041, '', 'ADRES', 'LOSCMFLG', 'RESET LOSCMFLG', kind='data', line=924)
W('24,2771', 0o03121, '', 'TC', 'R21DISP', 'PUT UP VERIFY MAIN LOBE LOCKON DISPLAY', line=925)
W('24,2772', 0o05353, 'R21SRCH', 'TC', 'PHASCHNG', line=926)
W('24,2773', 0o04022, '', 'OCT', '04022', kind='data', line=927)
W('24,2774', 0o03206, '', 'TC', 'R24LEM', 'SEARCH ROUTINE', line=928)
W('24,2775', 0o00503, 'ALRM503', 'OCT', '00503', kind='data', line=929)
# Page 510
W('24,2776', 0o00527, 'ALRM527', 'OCT', '527', kind='data', line=931)

W('24,2777', 0o32310, 'R21LEM4', 'CAF', 'MAXTRIES', 'SET UP COUNTER FOR', line=933)
W('24,3000', 0o55423, '', 'TS', 'REPOSCNT', '60 PASSES (APPROX 600 SECS.)', line=934)
W('24,3001', 0o05504, '', 'TC', 'UPFLAG', line=935)
W('24,3002', 0o00005, '', 'ADRES', 'FSPASFLG', 'SET FIRST PASS FLAG', kind='data', line=936)
W('24,3003', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET LOS BEING', line=937)
W('24,3004', 0o00041, '', 'ADRES', 'LOSCMFLG', 'COMPUTED FLAG', kind='data', line=938)
W('24,3005', 0o06037, '', 'TC', 'INTPRET', line=939)
W('24,3006', 0o77634, 'R21LEM12', 'RTB', kind='interp', line=940)
W('24,3007', 0o21573, '', '', 'LOADTIME', kind='operand', line=941)
W('24,3010', 0o77615, '', 'DAD', kind='interp', line=942)
W('24,3011', 0o11116, '', '', 'TENSEC', 'TIME T = T + 10 SECS.', kind='operand', line=943)
W('24,3012', 0o03425, '', 'STORE', 'REPOSTM', 'SAVE FOR LONGCALL AND UPPSV', kind='interp', line=944)
W('24,3013', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=945)
W('24,3014', 0o51255, '', '', 'LPS20.1', 'COMPUTE LOS AT TIME T', kind='operand', line=946)
W('24,3015', 0o77624, '', 'CALL', kind='interp', line=947)
W('24,3016', 0o52373, '', '', 'RRDESSM', kind='operand', line=948)
W('24,3017', 0o77776, '', 'EXIT', kind='interp', line=949)
W('24,3020', 0o03033, '', 'TC', 'R21LEM13', 'LOS NOT IN MODE 2 COVERAGE', line=950)
W('24,3021', 0o05155, '', 'TC', 'ENDOFJOB', 'VEHICLE MANEUVER REQUIRED', line=951)
W('24,3022', 0o06027, '', 'TC', 'KILLTASK', line=952)
W('24,3023', 0o52573, '', 'CADR', 'BEGDES', kind='data', line=953)
W('24,3024', 0o06037, '', 'TC', 'INTPRET', line=954)
W('24,3025', 0o77614, '', 'BOF', kind='interp', line=955)
W('24,3026', 0o00345, '', '', 'FSPASFLG', 'FIRST PASS THRU REPOSITION', kind='operand', line=956)
W('24,3027', 0o51043, '', '', 'R21LEMB', 'NO -- GO TO CONTINUOUS DESIGNATE', kind='operand', line=957)
W('24,3030', 0o77614, '', 'CLRGO', kind='interp', line=958)
W('24,3031', 0o00225, '', '', 'FSPASFLG', 'YES -- RESET FIRST PASS FLAG', kind='operand', line=959)
W('24,3032', 0o51037, '', '', 'R21LEM7 +1', kind='operand', line=960)
W('24,3033', 0o11423, 'R21LEM13', 'CCS', 'REPOSCNT', 'HAVE WE TRIED 60 TIMES?', line=961)
W('24,3034', 0o03036, '', 'TC', 'R21LEM7', 'NO -- ADD 10 SECS.  RECOMPUTE LOS', line=962)
W('24,3035', 0o03105, '', 'TC', 'R21LEM11', 'YES -- PUT OUT ALARM 530', line=963)
W('24,3036', 0o55423, 'R21LEM7', 'TS', 'REPOSCNT', line=964)
W('24,3037', 0o06037, '', 'TC', 'INTPRET', line=965)
W('24,3040', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=966)
W('24,3041', 0o03425, '', '', 'REPOSTM', kind='operand', line=967)
W('24,3042', 0o51010, '', '', 'R21LEM12 +2', kind='operand', line=968)
W('24,3043', 0o77745, 'R21LEMB', 'DLOAD', kind='interp', line=969)
W('24,3044', 0o03425, '', '', 'REPOSTM', kind='operand', line=970)
W('24,3045', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=971)
W('24,3046', 0o50316, '', '', 'UPPSV', kind='operand', line=972)
W('24,3047', 0o77776, '', 'EXIT', kind='interp', line=973)
W('24,3050', 0o05504, '', 'TC', 'UPFLAG', 'SET RADMODES BIT 15 FOR', line=974)
W('24,3051', 0o00264, '', 'ADRES', 'CDESFLAG', 'CONTINUOUS DESIGNATION', kind='data', line=975)
W('24,3052', 0o05516, '', 'TC', 'DOWNFLAG', line=976)
W('24,3053', 0o00012, '', 'ADRES', 'LOKONSW', kind='data', line=977)
W('24,3054', 0o05504, '', 'TC', 'UPFLAG', line=978)
W('24,3055', 0o00126, '', 'ADRES', 'NORRMON', kind='data', line=979)
# Page 511
W('24,3056', 0o04616, '', 'TC', 'BANKCALL', line=981)
W('24,3057', 0o52475, '', 'CADR', 'RRDESNB', kind='data', line=982)
W('24,3060', 0o03061, '', 'TC', '+1', line=983)
W('24,3061', 0o06037, '', 'TC', 'INTPRET', line=984)
W('24,3062', 0o44234, '', 'RTB', 'BDSU', kind='interp', line=985)
W('24,3063', 0o21573, '', '', 'LOADTIME', 'COMPUTE DELTA TIME', kind='operand', line=986)
W('24,3064', 0o03425, '', '', 'REPOSTM', 'FOR LONGCALL', kind='operand', line=987)
W('24,3065', 0o03427, '', 'STORE', 'DELTATM', kind='interp', line=988)
W('24,3066', 0o77776, '', 'EXIT', kind='interp', line=989)
W('24,3067', 0o00006, '', 'EXTEND', line=990)
W('24,3070', 0o31427, '', 'DCA', 'DELTATM', line=991)
W('24,3071', 0o05277, '', 'TC', 'LONGCALL', line=992)
#   EBANK= LOSCOUNT
W('24,3072', 0o03075, '', '2CADR', 'R21LEM9', kind='data', line=994)
W('24,3073', 0o50067, kind='data', line=994)

W('24,3074', 0o05155, '', 'TC', 'ENDOFJOB', line=996)
W('24,3075', 0o06027, 'R21LEM9', 'TC', 'KILLTASK', line=997)
W('24,3076', 0o52602, '', 'CADR', 'STDESIG', kind='data', line=998)
W('24,3077', 0o06011, '', 'TC', 'CLRADMOD', line=999)
W('24,3100', 0o37714, '', 'CAF', 'PRIO26', line=1000)
W('24,3101', 0o05105, '', 'TC', 'FINDVAC', line=1001)
#   EBANK= LOSCOUNT
W('24,3102', 0o02725, '', '2CADR', 'R21LEM10', kind='data', line=1003)
W('24,3103', 0o50067, kind='data', line=1003)

W('24,3104', 0o05261, '', 'TC', 'TASKOVER', line=1005)
W('24,3105', 0o33114, 'R21LEM11', 'CAF', 'ALRM530', 'ALARM 530 -- LOS NOT IN COVERAGE', line=1006)
W('24,3106', 0o04616, '', 'TC', 'BANKCALL', 'AFTER TRYING TO DESIGNATE FOR', line=1007)
W('24,3107', 0o21562, '', 'CADR', 'PRIOLARM', '600 SECS.', kind='data', line=1008)
W('24,3110', 0o06022, '', 'TC', 'GOTOV56', line=1009)
W('24,3111', 0o06022, '', 'TC', 'GOTOV56', line=1010)
W('24,3112', 0o06022, '', 'TC', 'GOTOV56', line=1011)
W('24,3113', 0o05155, '', 'TC', 'ENDOFJOB', line=1012)
W('24,3114', 0o00530, 'ALRM530', 'OCT', '00530', kind='data', line=1013)
W('24,3115', 0o00000, 'TENSEC', '2DEC', '1000 B-28', kind='data', line=1014)
W('24,3116', 0o01750, kind='data', line=1014)

W('24,3117', 0o00000, 'HALFSEC', '2DEC', '50', kind='data', line=1016)
W('24,3120', 0o00062, kind='data', line=1016)

W('24,3121', 0o05353, 'R21DISP', 'TC', 'PHASCHNG', line=1018)
W('24,3122', 0o04022, '', 'OCT', '04022', kind='data', line=1019)
W('24,3123', 0o33134, '', 'CAF', 'V06N72PV', 'FLASH V 50 N 72 -- PLEASE PERFORM RR', line=1020)
W('24,3124', 0o04616, '', 'TC', 'BANKCALL', 'MAIN LOBE LOCKON VERIFICATION', line=1021)
W('24,3125', 0o20710, '', 'CADR', 'GOPERF2R', kind='data', line=1022)
W('24,3126', 0o06022, '', 'TC', 'GOTOV56', 'TERMINATE EXITS VIA V 56', line=1023)
W('24,3127', 0o02232, '', 'TC', 'P20LEMWT', 'PROCEED CONTINUES TO R22', line=1024)
W('24,3130', 0o03123, '', 'TC', '-5', 'ENTER ILLEGAL', line=1025)
W('24,3131', 0o34745, '', 'CAF', 'BIT7', line=1026)
W('24,3132', 0o05464, '', 'TC', 'LINUS', 'SET BITS TO MAKE THIS A PRIORITY DISPLAY', line=1027)
W('24,3133', 0o05155, '', 'TC', 'ENDOFJOB', line=1028)

# Page 512
W('24,3134', 0o01510, 'V06N72PV', 'VN', '00672', kind='data', line=1031)

# Page 513
# MANUAL ACQUISITION ROUTINE R23LEM
# PROGRAM DESCRIPTION
#
# MOD NO -- 2
# BY P. VOLANTE
#
# FUNCTIONAL DESCRIPTION
#
# TO ACQUIRE THE CSM BY MANUAL OPERATION OF THE RENDEZVOUS RADAR
#
# CALLING SEQUENCE --
#
# TC      R23LEM
#
# SUBROUTINES CALLED
#
# BANKCALL        R61LEM
# SETMINDB        GOPERF1
#
# NORMAL EXIT MODES --
#
# IN RESPONSE TO THE GOPERF1,     SELECTION OF ENTER WILL RECYCLE R23
# SELECTION OF PROC WILL CONTINUE R23
# SELECTION OF TERM WILL TERMINATE R23 + P20
#
# ALARM OR ABORT EXIT MODES --
#
# SEE NORMAL EXIT MODES ABOVE
#
# OUTPUT
#
# N.A.
#
# ERASABLE INITIALIZATION REQUIRED --
#
# ACMODFLG MUST BE SET TO 1 (MANUAL MODE)

#   EBANK= GENRET
#   COUNT* $$/R23
W('24,3135', 0o05504, 'R23LEM', 'TC', 'UPFLAG', 'SET NO ANGLE MONITOR FLAG', line=1073)
W('24,3136', 0o00126, '', 'ADRES', 'NORRMON', kind='data', line=1074)
W('24,3137', 0o00004, '', 'INHINT', line=1075)
W('24,3140', 0o04674, '', 'TC', 'IBNKCALL', 'SELECT MINIMUM DEADBAND', line=1076)
W('24,3141', 0o40140, '', 'CADR', 'SETMINDB', kind='data', line=1077)
W('24,3142', 0o00003, '', 'RELINT', line=1078)
W('24,3143', 0o34736, 'R23LEM1', 'CAF', 'BIT14', 'ENABLE TRACKER', line=1079)
W('24,3144', 0o00006, '', 'EXTEND', line=1080)
W('24,3145', 0o05012, '', 'WOR', 'CHAN12', line=1081)
W('24,3146', 0o33205, '', 'CAF', 'OCT205', line=1082)
W('24,3147', 0o04616, '', 'TC', 'BANKCALL', line=1083)
W('24,3150', 0o20623, '', 'CADR', 'GOPERF1', kind='data', line=1084)
W('24,3151', 0o03176, '', 'TC', 'R23LEM2', 'TERMINATE', line=1085)
W('24,3152', 0o03154, '', 'TC', 'R23LEM11', 'PROCEDE', line=1086)
W('24,3153', 0o03201, '', 'TC', 'R23LEM3', 'ENTER -- DO ANOTHER MANEUVER', line=1087)
W('24,3154', 0o00004, 'R23LEM11', 'INHINT', line=1088)
W('24,3155', 0o04523, '', 'TC', 'RRLIMCHK', 'YES -- CHECK IF ANTENNA IS WITHIN LIMITS', line=1089)
W('24,3156', 0o00035, '', 'ADRES', 'CDUT', kind='data', line=1090)
W('24,3157', 0o03166, '', 'TC', 'OUTOFLIM', 'NOT WITHIN LIMITS', line=1091)
W('24,3160', 0o04674, '', 'TC', 'IBNKCALL', 'RESTORE DEADBAND TO', line=1092)
W('24,3161', 0o40123, '', 'CADR', 'RESTORDB', 'ASTRONAUT SELECTED VALUE', kind='data', line=1093)
W('24,3162', 0o00003, '', 'RELINT', line=1094)
W('24,3163', 0o05516, '', 'TC', 'DOWNFLAG', 'CLEAR NO ANGLE MONITOR FLAG', line=1095)
W('24,3164', 0o00126, '', 'ADRES', 'NORRMON', kind='data', line=1096)
W('24,3165', 0o02163, '', 'TC', 'P20LEMB1', 'RADAR IS LOCKED ON CONTINUE IN P20', line=1097)
W('24,3166', 0o00003, 'OUTOFLIM', 'RELINT', line=1098)
# Page 514
W('24,3167', 0o33204, '', 'CAF', 'OCT501PV', line=1100)
W('24,3170', 0o04616, '', 'TC', 'BANKCALL', 'ISSUE ALARM -- RR ANTENNA NOT WITHIN', line=1101)
W('24,3171', 0o21562, '', 'CADR', 'PRIOLARM', 'LIMITS', kind='data', line=1102)
W('24,3172', 0o03176, '', 'TC', 'R23LEM2', 'TERMINATE -- EXIT R23 TO R00 (GO TO POOH)', line=1103)
W('24,3173', 0o03167, '', 'TC', 'OUTOFLIM +1', 'PROCEED ILLEGAL', line=1104)
W('24,3174', 0o03201, '', 'TC', 'R23LEM3', 'RECYCLE -- TO ANOTHER MANEUVER', line=1105)
W('24,3175', 0o05155, '', 'TC', 'ENDOFJOB', line=1106)
W('24,3176', 0o05516, 'R23LEM2', 'TC', 'DOWNFLAG', 'CLEAR NO ANGLE MONITOR FLAG', line=1107)
W('24,3177', 0o00126, '', 'ADRES', 'NORRMON', kind='data', line=1108)
W('24,3200', 0o06022, '', 'TC', 'GOTOV56', 'AND EXIT VIA V56', line=1109)
W('24,3201', 0o04616, 'R23LEM3', 'TC', 'BANKCALL', line=1110)
W('24,3202', 0o46116, '', 'CADR', 'R61LEM', kind='data', line=1111)
W('24,3203', 0o03143, '', 'TC', 'R23LEM1', line=1112)

W('24,3204', 0o00501, 'OCT501PV', 'OCT', '501', kind='data', line=1114)
W('24,3205', 0o00205, 'OCT205', 'OCT', '205', kind='data', line=1115)

# Page 515
# SEARCH ROUTINE R24LEM
# PROGRAM DESCRIPTION
#
# MOD NO -- 2
# BY P. VOLANTE
#
# FUNCTIONAL DESCRIPTION
#
# TO ACQUIRE THE CSM BY A SEARCH PATTERN WHEN THE RENDEZVOUS RADAR HAS
# FAILED TO ACQUIRE TEH CSM IN THE AUTOMATIC TRACKING MODE AND TO ALLOW
# THE ASTRONAUT TO CONFIRM THAT REACQUISITION HAS NOT BEEN IN SIDELOBE.
#
# CALLING SEQUENCE
#
# CAF     PRIONN
# TC      FINDVAC
# EBANK=  DATAGOOD
# 2CADR   R24LEM
#
# SUBROUTINES CALLED
#
# FLAGUP          FLAGDOWN        BANKCALL
# R61LEM          GOFLASHR        FINDVAC
# ENDOFJOB        NOVAC           LSR24.1
#
# NORMAL EXIT MODES --
#
# ASTRONAUT RESPONSE TO DISPLAY OF OMEGA AND DATAGOOD.  HE CAN EITHER
# REJECT BY TERMINATING (SEARCH OPTION AND RESELECTING P20) OR ACCEPT BY
# PROCEEDING (EXIT ROUTINE AND RETURN TO AUTO MODE IN P20)
#
# ALARM OR ABORT EXIT MODES --
#
# SEE NORMAL EXIT MODES ABOVE
#
# OUTPUT --
#
# SEE OUTPUT FROM LSR24.1 + R61LEM
#
# ERASABLE INITIALIZATION REQUIRED
#
# SET INPUT FOR LSR24.1
#
# FLAGS SET + RESET
#
# SRCHOPT, ACMODFLG

#   EBANK= DATAGOOD
#   COUNT* $$/R24
W('24,3206', 0o05504, 'R24LEM', 'TC', 'UPFLAG', line=1167)
W('24,3207', 0o00037, '', 'ADRES', 'SRCHOPTN', 'SET SRCHOPT FLAG', kind='data', line=1168)
W('24,3210', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET LOS BEING COMPUTED FLAG TO MAKE', line=1169)
W('24,3211', 0o00041, '', 'ADRES', 'LOSCMFLG', "SURE DODES DOESN'T GO TO R21", kind='data', line=1170)
W('24,3212', 0o34755, 'R24LEM1', 'CAF', 'ZERO', line=1171)
W('24,3213', 0o55733, '', 'TS', 'DATAGOOD', 'ZERO OUT DATA INDICATOR', line=1172)
W('24,3214', 0o55734, '', 'TS', 'OMEGAD', 'ZERO OMEGA DISPLAY REGS', line=1173)
W('24,3215', 0o55735, '', 'TS', 'OMEGAD +1', 'ZERO OMEGA DISPLAY REGS', line=1174)
W('24,3216', 0o05353, 'R24LEM2', 'TC', 'PHASCHNG', line=1175)
W('24,3217', 0o04022, '', 'OCT', '04022', kind='data', line=1176)
W('24,3220', 0o33254, '', 'CAF', 'V16N80', line=1177)
W('24,3221', 0o04616, '', 'TC', 'BANKCALL', line=1178)
W('24,3222', 0o20504, '', 'CADR', 'PRIODSPR', kind='data', line=1179)
W('24,3223', 0o06022, '', 'TC', 'GOTOV56', line=1180)
W('24,3224', 0o03230, '', 'TC', 'R24END', 'PROCEED EXIT R24 TO P20LEM1', line=1181)

W('24,3225', 0o03234, '', 'TC', 'R24LEM3', 'RECYCLE -- CALL R61 TO MANEUVER S/C', line=1183)
# Page 516
W('24,3226', 0o04616, '', 'TC', 'BANKCALL', line=1185)
W('24,3227', 0o55442, '', 'CADR', 'LRS24.1', kind='data', line=1186)
W('24,3230', 0o06027, 'R24END', 'TC', 'KILLTASK', line=1187)
W('24,3231', 0o55643, '', 'CADR', 'CALLDGCH', kind='data', line=1188)
W('24,3232', 0o06011, '', 'TC', 'CLRADMOD', 'CLEAR BITS 10 & 15 OF RADMODES.', line=1189)
W('24,3233', 0o12063, '', 'TCF', 'P20LEM1', 'AND GO TO 400 MI. RANGE CHECK IN P20', line=1190)

#   BLOCK 3
#   SETLOC FFTAG6
#   BANK
#   COUNT* $$/R24

W('6011', 0o46021, 'CLRADMOD', 'CS', 'BIT10+15', line=1197)
W('6012', 0o00004, '', 'INHINT', line=1198)
W('6013', 0o70110, '', 'MASK', 'RADMODES', line=1199)
W('6014', 0o54110, '', 'TS', 'RADMODES', line=1200)
W('6015', 0o44752, '', 'CS', 'BIT2', 'DISABLE RR ERROR COUNTERS', line=1201)
W('6016', 0o00006, '', 'EXTEND', line=1202)
W('6017', 0o03012, '', 'WAND', 'CHAN12', 'USER WILL RELINT', line=1203)

W('6020', 0o00002, '', 'TC', 'Q', line=1205)

W('6021', 0o41000, 'BIT10+15', 'OCT', '41000', kind='data', line=1207)
#   BANK 24
#   SETLOC P20S
#   BANK
#   COUNT* $$/R24

W('24,3234', 0o05353, 'R24LEM3', 'TC', 'PHASCHNG', line=1213)
W('24,3235', 0o04022, '', 'OCT', '04022', kind='data', line=1214)
W('24,3236', 0o06027, '', 'TC', 'KILLTASK', line=1215)
W('24,3237', 0o55643, '', 'CADR', 'CALLDGCH', 'KILL WAITLIST FOR NEXT POINT IN PATTERN', kind='data', line=1216)
W('24,3240', 0o06011, '', 'TC', 'CLRADMOD', 'CLEAR BITS 10 + 15 OF RADMODES TO KILL', line=1217)
W('24,3241', 0o00003, '', 'RELINT', '', 'HALF SECOND DESIGNATE LOOP', line=1218)
W('24,3242', 0o34774, '', 'CAF', '.5SEC', line=1219)
W('24,3243', 0o04616, '', 'TC', 'BANKCALL', 'WAIT FOR DESIGNATE LOOP TO DIE', line=1220)
W('24,3244', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=1221)
W('24,3245', 0o02667, '', 'TC', 'LUNSFCHK', 'CHECK IF ON LUNAR SURFACE', line=1222)
W('24,3246', 0o03251, '', 'TC', 'R24LEM4', "YES -- DON'T DO ATTITUDE MANEUVER", line=1223)
W('24,3247', 0o04616, '', 'TC', 'BANKCALL', 'CALL R61 TO DO PREFERRED TRACKING', line=1224)
W('24,3250', 0o46116, '', 'CADR', 'R61LEM', 'ATTITUDE MANEUVER', kind='data', line=1225)
W('24,3251', 0o34755, 'R24LEM4', 'CAF', 'ZERO', 'ZERO OUT RADCADR (WHICH WAS SET BY', line=1226)
W('24,3252', 0o55306, '', 'TS', 'RADCADR', 'ENDRADAR WHEN DESIGNATE STOPPED) SO THAT', line=1227)
# RRDESSM WILL RETURN TO CALLER
W('24,3253', 0o03216, '', 'TC', 'R24LEM2', 'AND GO BACK TO PUT UP V16 N80 DISPLAY', line=1229)

W('24,3254', 0o04120, 'V16N80', 'VN', '01680', kind='data', line=1231)

# Page 517
# PREFERRED TRACKING ATTITUDE ROUTINE R61LEM
# PROGRAM DESCRIPTION
#
# MOD NO: 3               DATE: 4-11-67
# MOD BY: P. VOLANTE, SDC
#
# FUNCTIONAL DESCRIPTION --
#
# TO COMPUTE THE PREFERRED TRACKING ATTITUDE OF THE LM TO ENABLE RR
# TRACKING OF THE CSM AND TO PERFORM THE MANEUVER TO THE PREFERRED
# ATTITUDE.
#
# CALLING SEQUENCE --
#
# TC      BANKCALL
# CADR    R61LEM
#
# SUBROUTINES CALLED
#
# LPS20.1         VECPOINT
# KALCMAN3
#
# NORMAL EXIT MODES --
#
# NORMAL RETURN IS TO CALLER + 1
#
# ALARM OR ABORT EXIT MODES --
#
# TERMINATE P20 + R61 BY BRANCHING TO P20END IF BOTH TRACKFLAG +
# RENDEZVOUS FLAG ARE NOT SET.
#
# OUTPUT --
#
# SEE OUTPUT FOR LPS20.1 + ATTITUDE MANEUVER ROUTINE (R60)
#
# ERASABLE INITIALIZATION REQUIRED
#
# GENRET USED TO SAVE Q FOR RETURN
#
# FLAGS SET + RESET
#
# 3AXISFLG
#
# DEBRIS
#
# SEE SUBROUTINES

#   SETLOC R61
#   BANK
#   EBANK= LOSCOUNT
#   COUNT* $$/R61
W('23,2116', 0o04645, 'R61LEM', 'TC', 'MAKECADR', line=1285)
W('23,2117', 0o55143, '', 'TS', 'GENRET', line=1286)
W('23,2120', 0o05504, '', 'TC', 'UPFLAG', 'SET R61 FLAG', line=1287)
W('23,2121', 0o00024, '', 'ADRES', 'R61FLAG', kind='data', line=1288)
W('23,2122', 0o02127, '', 'TC', 'R61C+L01', line=1289)
W('23,2123', 0o04645, 'R65LEM', 'TC', 'MAKECADR', line=1290)
W('23,2124', 0o55143, '', 'TS', 'GENRET', line=1291)
W('23,2125', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET R61 FLAG', line=1292)
W('23,2126', 0o00024, '', 'ADRES', 'R61FLAG', kind='data', line=1293)
W('23,2127', 0o34747, 'R61C+L01', 'CAF', 'TRACKBIT', 'TRACKFLAG', line=1294)
W('23,2130', 0o70075, '', 'MASK', 'STATE +1', line=1295)
W('23,2131', 0o00006, '', 'EXTEND', line=1296)
W('23,2132', 0o12271, '', 'BZF', 'R65WAIT', 'NOT SET', line=1297)
W('23,2133', 0o06037, 'R61C+L03', 'TC', 'INTPRET', line=1298)
W('23,2134', 0o77775, '', 'VLOAD', kind='interp', line=1299)
# Page 518
W('23,2135', 0o06514, '', '', 'HIUNITZ', kind='operand', line=1301)
W('23,2136', 0o03765, '', 'STORE', 'SCAXIS', 'TRACK AXIS UNIT VECTOR', kind='interp', line=1302)
W('23,2137', 0o43234, 'R61LEM1', 'RTB', 'DAD', kind='interp', line=1303)
W('23,2140', 0o21573, '', '', 'LOADTIME', 'EXTRAPOLATE FORWARD TO CENTER', kind='operand', line=1304)
W('23,2141', 0o15712, '', '', '3SECONDS', 'SIX SECOND PERIOD.', kind='operand', line=1305)
W('23,2142', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1306)
W('23,2143', 0o51255, '', '', 'LPS20.1', 'LOS DETERMINATION + VEH ATTITUDE', kind='operand', line=1307)
W('23,2144', 0o77775, '', 'VLOAD', kind='interp', line=1308)
W('23,2145', 0o01102, '', '', 'RRTARGET', kind='operand', line=1309)
W('23,2146', 0o03773, '', 'STORE', 'POINTVSM', kind='interp', line=1310)
W('23,2147', 0o45034, '', 'RTB', 'CALL', "GET DESIRED CDU'S FOR VECPNT1", kind='interp', line=1311)
W('23,2150', 0o46277, '', '', 'READCDUD', kind='operand', line=1312)
W('23,2151', 0o56032, '', '', 'VECPNT1', 'COMPUTES FINAL ANGLES FROM PRESENT CDUDS', kind='operand', line=1313)
W('23,2152', 0o00322, '', 'STORE', 'CPHI', 'STORE FINAL ANGLES -- CPHI, CTHETA, CPSI', kind='interp', line=1314)
W('23,2153', 0o77776, '', 'EXIT', kind='interp', line=1315)
W('23,2154', 0o05353, '', 'TC', 'PHASCHNG', line=1316)
W('23,2155', 0o04022, '', 'OCT', '04022', kind='data', line=1317)
W('23,2156', 0o34747, '', 'CAF', 'TRACKBIT', 'IS TRACK FLAG SET', line=1318)
W('23,2157', 0o70075, '', 'MASK', 'FLAGWRD1', line=1319)
W('23,2160', 0o00006, '', 'EXTEND', line=1320)
W('23,2161', 0o12271, '', 'BZF', 'R65WAIT', line=1321)
W('23,2162', 0o04616, '', 'TC', 'BANKCALL', line=1322)
W('23,2163', 0o54255, '', 'CADR', 'G+N,AUTO', 'CHECK FOR AUTO MODE', kind='data', line=1323)
W('23,2164', 0o10000, '', 'CCS', 'A', line=1324)
W('23,2165', 0o02257, '', 'TC', 'R61C+L04', 'NOT IN AUTO', line=1325)
W('23,2166', 0o06037, '', 'TC', 'INTPRET', line=1326)
W('23,2167', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=1327)
W('23,2170', 0o01102, '', '', 'RRTARGET', kind='operand', line=1328)
W('23,2171', 0o47646, '', '', 'CDU*SMNB', kind='operand', line=1329)
W('23,2172', 0o45345, '', 'DLOAD', 'DSU', 'GET PHI -- ARCCOS OF Z-COMPONENT OF LOS', kind='interp', line=1330)
W('23,2173', 0o00162, '', '', 'MPAC +5', kind='operand', line=1331)
W('23,2174', 0o06275, '', '', 'COS15DEG', kind='operand', line=1332)
W('23,2175', 0o77440, 'R61LEM2', 'BMN', 'EXIT', 'BRANCH -- PHI > 15 DEGREES', kind='interp', line=1333)
W('23,2176', 0o46213, '', '', 'R61C+L05', 'PHI GRE 10DEG', kind='operand', line=1334)
#   EBANK= CDUXD
W('23,2177', 0o35015, '', 'CAF', 'EBANK6', line=1336)
W('23,2200', 0o54003, '', 'TS', 'EBANK', line=1337)
W('23,2201', 0o00004, '', 'INHINT', line=1338)
W('23,2202', 0o00006, '', 'EXTEND', line=1339)
W('23,2203', 0o30322, '', 'DCA', 'CPHI', line=1340)
W('23,2204', 0o53636, '', 'DXCH', 'CDUXD', line=1341)
W('23,2205', 0o30323, '', 'CA', 'CPSI', line=1342)
W('23,2206', 0o55637, '', 'TS', 'CDUZD', line=1343)
W('23,2207', 0o00003, '', 'RELINT', line=1344)
#   EBANK= LOSCOUNT
W('23,2210', 0o35016, '', 'CAF', 'EBANK7', line=1346)
W('23,2211', 0o54003, '', 'TS', 'EBANK', line=1347)
W('23,2212', 0o02236, '', 'TC', 'R61C+L06', line=1348)
W('23,2213', 0o77776, 'R61C+L05', 'EXIT', kind='interp', line=1349)
W('23,2214', 0o00004, '', 'INHINT', line=1350)
# Page 519
W('23,2215', 0o04674, '', 'TC', 'IBNKCALL', line=1352)
W('23,2216', 0o40153, '', 'FCADR', 'ZATTEROR', kind='data', line=1353)
W('23,2217', 0o04674, '', 'TC', 'IBNKCALL', line=1354)
W('23,2220', 0o40140, '', 'FCADR', 'SETMINDB', 'REDUCE ATTITUDE ERROR', kind='data', line=1355)
W('23,2221', 0o05516, '', 'TC', 'DOWNFLAG', line=1356)
W('23,2222', 0o00124, '', 'ADRES', '3AXISFLG', kind='data', line=1357)
W('23,2223', 0o05504, '', 'TC', 'UPFLAG', line=1358)
W('23,2224', 0o00077, '', 'ADRES', 'PDSPFLAG', 'SET PRIORITY DISPLAY FLAG', kind='data', line=1359)
W('23,2225', 0o04616, '', 'TC', 'BANKCALL', line=1360)
W('23,2226', 0o54123, '', 'CADR', 'R60LEM', kind='data', line=1361)
W('23,2227', 0o00004, '', 'INHINT', line=1362)
W('23,2230', 0o04674, '', 'TC', 'IBNKCALL', line=1363)
W('23,2231', 0o40123, '', 'FCADR', 'RESTORDB', kind='data', line=1364)
W('23,2232', 0o05353, '', 'TC', 'PHASCHNG', line=1365)
W('23,2233', 0o04022, '', 'OCT', '04022', kind='data', line=1366)
W('23,2234', 0o05516, '', 'TC', 'DOWNFLAG', line=1367)
W('23,2235', 0o00077, '', 'ADRES', 'PDSPFLAG', 'RESET PRIORITY DISPLAY FLAG', kind='data', line=1368)
W('23,2236', 0o30075, 'R61C+L06', 'CA', 'FLAGWRD1', line=1369)
W('23,2237', 0o74742, '', 'MASK', 'R61FLBIT', line=1370)
W('23,2240', 0o10000, '', 'CCS', 'A', line=1371)
W('23,2241', 0o02262, '', 'TC', 'R61C+L4', line=1372)
W('23,2242', 0o11745, '', 'CCS', 'R65CNTR', line=1373)
W('23,2243', 0o02245, '', 'TC', '+2', line=1374)
W('23,2244', 0o02262, '', 'TC', 'R61C+L4', 'R65CNTR = 0 - EXIT ROUTINE', line=1375)
W('23,2245', 0o55745, '', 'TS', 'R65CNTR', line=1376)
W('23,2246', 0o32276, '', 'CAF', '06SEC', line=1377)
W('23,2247', 0o05173, '', 'TC', 'TWIDDLE', line=1378)
W('23,2250', 0o02252, '', 'ADRES', 'R61C+L2', kind='data', line=1379)
W('23,2251', 0o05155, '', 'TC', 'ENDOFJOB', line=1380)
W('23,2252', 0o37714, 'R61C+L2', 'CAF', 'PRIO26', line=1381)
W('23,2253', 0o05105, '', 'TC', 'FINDVAC', line=1382)
#   EBANK= LOSCOUNT
W('23,2254', 0o02127, '', '2CADR', 'R61C+L01', kind='data', line=1384)
W('23,2255', 0o46067, kind='data', line=1384)

W('23,2256', 0o05261, '', 'TC', 'TASKOVER', line=1386)
W('23,2257', 0o04616, 'R61C+L04', 'TC', 'BANKCALL', 'TO CONVERT ANGLES TO FDAI', line=1387)
W('23,2260', 0o54266, '', 'CADR', 'BALLANGS', kind='data', line=1388)
W('23,2261', 0o02236, '', 'TC', 'R61C+L06', line=1389)
W('23,2262', 0o31143, 'R61C+L4', 'CAE', 'GENRET', line=1390)
W('23,2263', 0o14640, '', 'TCF', 'BANKJUMP', 'EXIT R61', line=1391)
W('23,2264', 0o32273, 'R61C+L1', 'CAF', 'BIT7+9PV', 'IS RENDEZVOUS OR P25FLAG SET', line=1392)
W('23,2265', 0o70074, '', 'MASK', 'STATE', line=1393)
W('23,2266', 0o00006, '', 'EXTEND', line=1394)
W('23,2267', 0o15155, '', 'BZF', 'ENDOFJOB', 'NO -- EXIT ROUTINE AND PROGRAM.', line=1395)
W('23,2270', 0o02236, '', 'TC', 'R61C+L06', 'YES EXIT ROUTINE', line=1396)
W('23,2271', 0o04635, 'R65WAIT', 'TC', 'POSTJUMP', line=1397)
W('23,2272', 0o50232, '', 'CADR', 'P20LEMWT', kind='data', line=1398)

W('23,2273', 0o00500, 'BIT7+9PV', 'OCT', '00500', kind='data', line=1400)
# Page 520
W('23,2274', 0o17350, 'COS15DEG', '2DEC', '0.96593 B-1', kind='data', line=1402)
W('23,2275', 0o34602, kind='data', line=1402)

W('23,2276', 0o01130, '06SEC', 'DEC', '600', kind='data', line=1404)
S('PHI', 'equals', 0o24, line=1405)
W('23,2277', 0o00004, 'READCDUD', 'INHINT', '', "READS DESIRED CDU'S AND STORES IN", line=1406)
W('23,2300', 0o35015, '', 'CAF', 'EBANK6', 'MPAC TP EXITS WITH MODE SET TO TP', line=1407)
W('23,2301', 0o56003, '', 'XCH', 'EBANK', line=1408)
W('23,2302', 0o54070, '', 'TS', 'RUPTREG1', line=1409)
#   EBANK= CDUXD
W('23,2303', 0o31635, '', 'CA', 'CDUXD', line=1411)
W('23,2304', 0o54154, '', 'TS', 'MPAC', line=1412)
W('23,2305', 0o00006, '', 'EXTEND', line=1413)
W('23,2306', 0o31637, '', 'DCA', 'CDUYD', line=1414)
W('23,2307', 0o52156, '', 'DXCH', 'MPAC +1', line=1415)
W('23,2310', 0o30070, '', 'CA', 'RUPTREG1', line=1416)
W('23,2311', 0o54003, '', 'TS', 'EBANK', line=1417)
W('23,2312', 0o00003, '', 'RELINT', line=1418)
W('23,2313', 0o16477, '', 'TCF', 'TMODE', line=1419)
#   BLOCK 02
#   SETLOC RADARFF
#   BANK

#   EBANK= LOSCOUNT
#   COUNT* $$/RRSUB

# Page 521
# THE FOLLOWING SUBROUTINE RETURNS TO CALLER +2 IF THE ABSOLUTE VALUE OF VALUE OF C(A) IS GREATER THAN THE
# NEGATIVE OF THE NUMBER AT CALLER +1.  OTHERWISE IT RETURNS TO CALLER +3.  MAY BE CALLED IN RUPT OR UNDER EXEC.

W('4512', 0o00006, 'MAGSUB', 'EXTEND', line=1431)
W('4513', 0o64515, '', 'BZMF', '+2', line=1432)
W('4514', 0o14516, '', 'TCF', '+2', line=1433)
W('4515', 0o40000, '', 'COM', line=1434)

W('4516', 0o50002, '', 'INDEX', 'Q', line=1436)
W('4517', 0o60000, '', 'AD', '0', line=1437)
W('4520', 0o00006, '', 'EXTEND', line=1438)
W('4521', 0o66741, '', 'BZMF', 'Q+2', 'ABS(A) <= CONST GO TO L+3', line=1439)
W('4522', 0o16737, '', 'TCF', 'Q+1', 'ABS(A) > CONST GO TO L+2', line=1440)

# Page 522
# PROGRAM NAME: RRLIMCHK
#
# FUNCTIONAL DESCRIPTION:
#
# RRLIMCHK CHECKS RR DESIRED GIMBAL ANGLES TO SEE IF THEY ARE WITHIN
# THE LIMITS OF THE CURRENT MODE.  INITIALLY THE DESIRED TRUNNION AND
# SHAFT ANGLES ARE STORED IN ITEMP1 AND ITEMP2.  THE CURRENT RR
# ANTENNAE MODE (RADMODES BIT 12) IS CHECKED WHICH IS = 0 FOR
# MODE 1 AND =1 FOR MODE 2.
#
# MODE 1 -- THE TRUNNION ANGLE IS CHECKED AT MAGSUB TO SEE IF IT IS
# BETWEEN -55 AND +55 DEGREES.  IF NOT, RETURN TO L +2.  IF WITHIN LIMITS,
# THE SHAFT ANGLE IS CHECKED TO SEE IF IT IS BETWEEN -70 AND +59 DEGREES.
# IF NOT, RETURN TO L +2.  IF IN LIMITS, RETURN TO L +3.
#
# MODE 2 -- THE SHAFT ANGLE IS CHECKED AT MAGSUB TO SEE IF IT IS
# BETWEEN -139 AND -25 DEGREES.  IF NOT, RETURN TO L +2.  IF WITHIN
# LIMITS, THE TRUNNION ANGLE IS CHECKED TO SEE IF IT IS BETWEEN +125
# AND -125 (+235) DEGREES.  IF NOT, RETURN TO L +2.  IF IN LIMITS, RETURN
# TO L +3.
#
# CALLING SEQUENCE:
#
# L  TC  RLIMCHK (WITH INTERRUPT INHIBITED)
# L  +1  ADRES  T,S  (DESIRED TRUNNION ANGLE ADDRESS)
#
# ERASABLE INITIALIZATION REQUIRED:
#
# RADMODES, MODEA, MODEB (OR DESIRED TRUNNION AND SHAFT
# ANGLES ELSEWHERE IN CONSECUTIVE LOCATIONS -- UNSWITCHED ERASABLE OR
# CURRENT EBANK).
#
# SUBROUTINES CALLED:   MAGSUB
#
# JOBS OR TASKS INITIATED:  NONE
#
# ALARMS:  NONE
#
# EXIT:         L + 2   (EITHER OR BOTH ANGLES NOT WITHIN LIMITS OF CURRENT MODE)
# L + 3   (BOTH ANGLES WITHIN LIMITS OF CURRENT MODE)

W('4523', 0o00006, 'RRLIMCHK', 'EXTEND', line=1484)
W('4524', 0o50002, '', 'INDEX', 'Q', line=1485)
W('4525', 0o50000, '', 'INDEX', '0', line=1486)
W('4526', 0o30001, '', 'DCA', '0', line=1487)
W('4527', 0o24002, '', 'INCR', 'Q', line=1488)
W('4530', 0o52062, '', 'DXCH', 'ITEMP1', line=1489)
W('4531', 0o22002, '', 'LXCH', 'Q', 'L(CALLER +2) TO L.', line=1490)

W('4532', 0o34740, '', 'CAF', 'ANTENBIT', 'SEE WHICH MODE RR IS IN.', line=1492)
W('4533', 0o70110, '', 'MASK', 'RADMODES', line=1493)
W('4534', 0o10000, '', 'CCS', 'A', line=1494)
W('4535', 0o14550, '', 'TCF', 'MODE2CHK', line=1495)

W('4536', 0o30061, '', 'CA', 'ITEMP1', 'MODE 1 IS DEFINED AS', line=1497)
# Page 523
W('4537', 0o04512, '', 'TC', 'MAGSUB', '      1. ABS(T) L 55 DEGS.', line=1499)
W('4540', 0o66161, '', 'DEC', '-.30555', '      2. ABS(S + 5.5 DEGS) L 64.5 DEGS', kind='data', line=1500)
W('4541', 0o00001, '', 'TC', 'L', '              (SHAFT LIMITS AT +59, -70 DEGS)', line=1501)

W('4542', 0o34562, '', 'CAF', '5.5DEGS', line=1503)
W('4543', 0o60062, '', 'AD', 'ITEMP2', line=1504)
W('4544', 0o04512, '', 'TC', 'MAGSUB', line=1505)
W('4545', 0o64420, '', 'DEC', '-.35833', '64.5 DEGS', kind='data', line=1506)
W('4546', 0o00001, '', 'TC', 'L', line=1507)
W('4547', 0o04560, '', 'TC', 'RRLIMOK', 'IN LIMITS.', line=1508)

W('4550', 0o34563, 'MODE2CHK', 'CAF', '82DEGS', 'MODE 2 IS DEFINED AS', line=1510)
W('4551', 0o60062, '', 'AD', 'ITEMP2', '      1. ABS(T) G 125 DEGS.', line=1511)
W('4552', 0o04512, '', 'TC', 'MAGSUB', '      2. ABS(S + 82 DEGS) L 57 DEGS', line=1512)
W('4553', 0o65673, '', 'DEC', '-.31667', '              (SHAFT LIMITS AT -25, -139 DEGS)', kind='data', line=1513)
W('4554', 0o00001, '', 'TC', 'L', line=1514)

W('4555', 0o30061, '', 'CA', 'ITEMP1', line=1516)
W('4556', 0o04512, '', 'TC', 'MAGSUB', line=1517)
W('4557', 0o51615, '', 'DEC', '-.69444', '125 DEGS', kind='data', line=1518)

W('4560', 0o50001, 'RRLIMOK', 'INDEX', 'L', line=1520)
W('4561', 0o00001, '', 'TC', 'L', '( = TC 1 )', line=1521)

W('4562', 0o00765, '5.5DEGS', 'DEC', '.03056', kind='data', line=1523)
W('4563', 0o16450, '82DEGS', 'DEC', '.45556', kind='data', line=1524)

# Page 524
# PROGRAM NAME: SETTRKF
#
# FUNCTIONAL DESCRIPTION:
#
# SETTRKF UPDATES THE TRACKER FAIL LAMP ON THE DSKY.
# INITIALLY THE LAMP TEST FLAG (IMODES33 BIT 1) IS CHECKED.
# IF A LAMP TEST IS IN PROGRESS, THE PROGRAM EXITS TO L +1.
# IF NO LAMP TEST THE FOLLOWING IS CHECKED SEQUENTIALLY:
# 1) RR CDU'S BEING ZEROED, RR CDU OK, AND RR NOT IN
# AUTO MODE (RADMODES BITS 13, 7, 2).
# 2) LR VEL DATA FAIL AND NO LR POS DATA (RADMODES BITS
# 8,5)
# 3) NO RR DATA (RADMODES BIT 4)
# THE ABSENCE OF ALL THREE SIMULTANEOUSLY IN (1), THE PRESENCE OF BOTH
# IN (2), AND THE PRESENCE OF (3) RESULTS IN EITHER THE TRACKER FAIL
# LAMP (DSPTAB +11D BIT 8) BEING TURNED OFF OR IS LEFT OFF.  THEREFORE, THE
# TRACKER FAIL LAMP IS TURN ON IF:
# A) RR CDU FAILED WITH RR IN AUTO MODE AND RR CDU'S NOT BEING ZEROED
# B) N SAMPLES OF LR DATA COULD NOT BE TAKEN IN 2N TRIES WITH
# EITHER THE ALT OR VEL INFORMATION
# C) N SAMPLES OF RR DATA COULD NOT BE OBTAINED FROM 2N TRIES
# WITH EITHER THE AL
#
# CALLING SEQUENCE:
#
# L       TC      SETTRKF
#
# ERASABLE INITIALIZATION REQUIRED:  IMODES33, RADMODES, DSPTAB +11D
#
# SUBROUTINES CALLED:  NONE
#
# JOBS OR TASKS INITIATED:  NONE
#
# ALARMS:  TRACKER FAIL LAMP
#
# EXIT:  L +1 (ALWAYS)

W('4564', 0o34753, 'SETTRKF', 'CAF', 'BIT1', 'NO ACTION IF DURING LAMP TEST', line=1564)
W('4565', 0o71303, '', 'MASK', 'IMODES33', line=1565)
W('4566', 0o10000, '', 'CCS', 'A', line=1566)
W('4567', 0o00002, '', 'TC', 'Q', line=1567)

W('4570', 0o34744, 'RRTRKF', 'CA', 'BIT8', line=1569)
W('4571', 0o54001, '', 'TS', 'L', line=1570)

W('4572', 0o34615, '', 'CAF', '13,7,2', 'SEE IF CDU FAILED.', line=1572)
W('4573', 0o70110, '', 'MASK', 'RADMODES', line=1573)
W('4574', 0o00006, '', 'EXTEND', line=1574)
W('4575', 0o14601, '', 'BZF', 'TRKFLON', 'CONDITION 3 ABOVE.', line=1575)

W('4576', 0o34750, 'RRCHECK', 'CAF', 'RRDATABT', 'SEE IF RR DATA FAILED.', line=1577)
W('4577', 0o70110, '', 'MASK', 'RADMODES', line=1578)
# Page 525
W('4600', 0o10000, '', 'CCS', 'A', line=1580)
W('4601', 0o30001, 'TRKFLON', 'CA', 'L', line=1581)
W('4602', 0o61036, '', 'AD', 'DSPTAB +11D', 'HALF ADD DESIRED AND PRESENT STATES.', line=1582)
W('4603', 0o70001, '', 'MASK', 'L', line=1583)
W('4604', 0o00006, '', 'EXTEND', line=1584)
W('4605', 0o16742, '', 'BZF', 'TCQ', 'NO CHANGE.', line=1585)

W('4606', 0o31036, 'FLIP', 'CA', 'DSPTAB +11D', "CAN'T USE LXCH DSPTAB +11D (RESTART PROB)", line=1587)
W('4607', 0o00006, '', 'EXTEND', line=1588)
W('4610', 0o06001, '', 'RXOR', 'LCHAN', line=1589)
W('4611', 0o74733, '', 'MASK', 'POSMAX', line=1590)
W('4612', 0o64735, '', 'AD', 'BIT15', line=1591)
W('4613', 0o55036, '', 'TS', 'DSPTAB +11D', line=1592)
W('4614', 0o00002, '', 'TC', 'Q', line=1593)

W('4615', 0o10102, '13,7,2', 'OCT', '10102', kind='data', line=1595)
S('ENDRMODF', 'equals', 0o4616, line=1596)

# Page 526
# PROGRAM NAME:  RRTURNON
#
# FUNCTIONAL DESCRIPTION:
#
# RRTURNON IS THE TURN-ON SEQUENCE WHICH, ALONG WTIH
# RRZEROSB, ZEROES THE CDU'S AND DETERMINES THE RR MODE.
# INITIALLY, CONTROL IS TRANSFERRED TO RRZEROSB FOR THE
# ACTUAL TURN-ON SEQUENCE.  UPON RETURN THE PROGRAM
# WAITS 1 SECOND BEFORE REMOVING THE TURN-ON FLAG
# (RADMODES BIT1) SO THE REPOSITION ROUTINE WON'T
# INITIATE PROGRAM ALARM 00501.  A CHECK IS THEN MADE
# TO SEE IF A PROGRAM IS USING THE RR (STATE BIT 7).  IF
# SO, THE PROGRAM EXITS TO ENDRADAR SO THAT THE RR CDU
# FAIL FLAG (RADMODES BIT 7) CAN BE CHECKED BEFORE
# RETURNING TO THE WAITING PROGRAM.  IF NOT, THE PROGRAM EXITS
# TO TASKOVER.
#
# CALLING SEQUENCE:  WAITLIST TASK FROM RRAUTCHK IF THE RR POWER-ON AUTO
# BIT (CHAN 33 BIT 2) CHANGES TO 0 AND NO PROGRAM WAS USING
# THE RR (STATE BIT 7).
#
# ERASABLE INITIALIZATION REQUIRED:
#
# RADMODES, STATE
#
# SUBROUTINES CALLED:  RRZEROSB, FIXDELAY, TASKOVER, ENDRADAR
#
# JOBS OR TASKS INITIATED:
#
# NONE
#
# ALARMS:  NONE (SEE RRZEROSB)
#
# EXIT:  TASKOVER, ENDRADAR (WAITING PROGRAM)

#   BANK 24
#   SETLOC P20S1
#   BANK

#   EBANK= LOSCOUNT
#   COUNT* $$/RSUB
W('25,2062', 0o02071, 'RRTURNON', 'TC', 'RRZEROSB', line=1640)
W('25,2063', 0o05221, '', 'TC', 'FIXDELAY', 'WAIT 1 SEC BEFORE REMOVING TURN ON FLAG', line=1641)
W('25,2064', 0o00144, '', 'DEC', '100', "SO A MONITOR REPOSITION WON'T ALARM.", kind='data', line=1642)
W('25,2065', 0o44753, '', 'CS', 'TURNONBT', line=1643)
W('25,2066', 0o70110, '', 'MASK', 'RADMODES', line=1644)
W('25,2067', 0o54110, '', 'TS', 'RADMODES', line=1645)
W('25,2070', 0o15261, '', 'TCF', 'TASKOVER', line=1646)
# Page 527
# PROGRAM NAME:  RRZEROSB
#
# FUNCTIONAL DESCRIPTION:
#
# RRZEROSB IS A CLOSED SUBROUTINE TO ZERO THE RR CDU'S,
# DETERMINE THE RR MODE, AND TURN ON THE TRACKER FAIL
# LAMP IF REQUIRED.  INITIALLY THE RR CDU ZERO BIT (CHAN 12
# BIT 1) IS SET.  FOLLOWING A 20 MILLISECOND WAIT, THE LGC
# RR CDU COUNTERS (OPTY, OPTX) ARE SET = 0 AFTER
# WHICH THE RR CDU ZERO DISCRETE (CHAN 12 BIT 1) IS
# REMOVED.  A 4 SECOND WAIT IS SET TO ALL THE RR CDU'S
# TO REPEAT THE ACTUAL TRUNNION AND SHAFT ANGLES.  THE
# RR CDU ZERO FLAG (RADMODES BIT 13) IS REMOVED.  THE
# CONTENTS OF OPTY IS THEN CHECKED TO SEE IF THE TRUNNION
# ANGLE IS LESS THAN 90 DEGREES.  IF NOT, BIT 12 OF
# RADMODES IS SET = 1 TO INDICATE RR ANTENNA MODE 2.
# IF LESS THAN 90 DEGREES, BIT 12 OF RADMODES IS SET = 0 TO
# INDICATE RR ANTENNA MODE 1.  SETTRKF IS THEN CALLED TO
# SEE IF THE TRACKER FAIL LAMP SHOULD BE TURNED ON.
#
# CALLING SEQUENCE:  L  TC  RRZEROSB  (FROM RRTURNON AND RRZERO)
#
# ERASABLE INITIALIZATION REQUIRED:
#
# RADMODES (BIT 13 SET), DSPTAB +11D
#
# SUBROUTINES CALLED:  FIXDELAY, MAGSUB, SETTRKF
#
# JOBS OR TASKS INITIATED:
#
# NONE
#
# ALARMS:  TRAKCER FAIL
#
# EXIT:  L +1 (ALWAYS)

W('25,2071', 0o00006, 'RRZEROSB', 'EXTEND', line=1684)
W('25,2072', 0o23315, '', 'QXCH', 'RRRET', line=1685)
W('25,2073', 0o34753, '', 'CAF', 'BIT1', 'BIT 13 OF RADMODES MUST BE SET BEFORE', line=1686)
W('25,2074', 0o00006, '', 'EXTEND', '', 'COMING HERE.', line=1687)
W('25,2075', 0o05012, '', 'WOR', 'CHAN12', 'TURN ON ZERO RR CDU', line=1688)
W('25,2076', 0o05221, '', 'TC', 'FIXDELAY', line=1689)
W('25,2077', 0o00002, '', 'DEC', '2', kind='data', line=1690)

W('25,2100', 0o34755, '', 'CAF', 'ZERO', line=1692)
W('25,2101', 0o54035, '', 'TS', 'CDUT', line=1693)
W('25,2102', 0o54036, '', 'TS', 'CDUS', line=1694)
W('25,2103', 0o44753, '', 'CS', 'ONE', 'REMOVE ZEROING BIT.', line=1695)
W('25,2104', 0o00006, '', 'EXTEND', line=1696)
W('25,2105', 0o03012, '', 'WAND', 'CHAN12', line=1697)
W('25,2106', 0o05221, '', 'TC', 'FIXDELAY', line=1698)
W('25,2107', 0o01750, '', 'DEC', '1000', 'RESET FAIL INHIBIT IN 10 SECS. -- D.281', kind='data', line=1699)

W('25,2110', 0o44737, '', 'CS', 'RCDU0BIT', 'REMOVE ZEROING IN PROCESS BIT', line=1701)
# Page 528
W('25,2111', 0o70110, '', 'MASK', 'RADMODES', line=1703)
W('25,2112', 0o54110, '', 'TS', 'RADMODES', line=1704)

W('25,2113', 0o30035, '', 'CA', 'CDUT', line=1706)
W('25,2114', 0o04512, '', 'TC', 'MAGSUB', line=1707)
W('25,2115', 0o57777, '', 'DEC', '-.5', kind='data', line=1708)
W('25,2116', 0o12121, '', 'TCF', '+3', 'IF MODE 2.', line=1709)

W('25,2117', 0o34755, '', 'CAF', 'ZERO', line=1711)
W('25,2120', 0o12122, '', 'TCF', '+2', line=1712)
W('25,2121', 0o34740, '', 'CAF', 'ANTENBIT', line=1713)
W('25,2122', 0o56110, '', 'XCH', 'RADMODES', line=1714)
W('25,2123', 0o77741, '', 'MASK', '-BIT12', line=1715)
W('25,2124', 0o26110, '', 'ADS', 'RADMODES', line=1716)

W('25,2125', 0o04564, '', 'TC', 'SETTRKF', 'TRACKER LAMP MIGHT GO ON NOW.', line=1718)

W('25,2126', 0o01315, '', 'TC', 'RRRET', 'DONE.', line=1720)

S('-BIT12', 'equals', 0o7741, line=1722)  # IN SPROOT

# Page 529
# PROGRAM NAME:  DORREPOS
#
# FUNCTIONAL DESCRIPTION:
#
# DORREPOS IS A SEQUENCE OF TASKS TO DRIVE THE RENDEZVOUS RADAR
# TO A SAFE POSITION.  INIITALLY SETRRECR IS CALLED WHERE THE RR
# ERROR COUNTERS (CHAN 12 BIT 2) ARE ENABLED AND LASTYCMD
# AND LASTXCMD SET = 0 TO INDICATE THE DIFFERENCE BETWEEN THE
# DESIRED STATE AND PRESENT STATE OF THE COMMANDS.  THE RR
# TURN-ON FLAG (RADMODES BIT 1) IS CHECKED AND IF NOT PRESENT,
# PROGRAM ALARM 00501 IS REQUESTED BEFORE CONTINUING.  IN EITHER
# CASE, FOLLOWING A 20 MILLISECOND WAIT THE PROGRAM CHECKS THE CURRENT
# RR ANTENNA MODE (RADMODES BIT 12).  RRTONLY IS THEN CALLED
# TO DRIVE THE TRUNNION ANGLE TO 0 DEGREES IF IN MODE 1 AND TO 180
# DEGREES IF IN MODE 2.  UPON RETURN, THE CURRENT RR ANTENNA
# MODE (RADMODES BIT 12) IS AGAIN CHECKED.  RRSONLY IS THEN
# CALLED TO DRIVE THE SHAFT ANGLE TO 0 DEGREES IF IN MODE 1 AND TO
# -90 DEGREES IF IN MODE 2.  IF DURING RRTONLY OR RRSONLY A
# REMODE HAS BEEN REQUESTED (RADMODES BIT 14), AND ALWAYS
# FOLLOWING COMPLETION OF RRSONLY, CONTROL IS TRANFERRED TO
# REPOSRPT.  HERE THE REPOSITION FLAG (RADMODES BIT 11) IS
# REMOVED.  A CHECK IS THEN MADE ON THE DESIGNATE FLAG (RADMODES
# BIT 10).  IF PRESENT, CONTROL IS TRANSFERRED TO BEGDES.  IF NOT PRESENT
# INDICATING NO FURTHER ANTENNA CONTROL REQUIRED, THE RR ERROR
# COUNTER BIT (CHAN 12 BIT 2) IS REMOVED AND THE ROUTINE EXITS TO
# TASKOVER.
#
# CALLING SEQUENCE:
#
# WAITLIST CALL FROM RRGIMON IF TRUNNION AND SHAFT CDU ANGLES
# NOT WITHIN LIMITS OF CURRENT MODE.
#
# ERASABLE INITIALIZATION REQUIRED:
#
# RADMODES
#
# SUBROUTINES CALLED
#
# RRTONLY, RRSONLY, BEGDES (EXIT)
#
# JOBS OR TASKS INITIATED:
#
# NONE
#
# ALARMS:  NONE
#
# EXIT:  TASKOVER, BEGDES

W('25,2127', 0o02156, 'DORREPOS', 'TC', 'SETRRECR', 'SET UP RR CDU ERROR COUNTERS.', line=1773)

# ALARM 501 DELETED IN DANCE 279 PER PCR 97.

W('25,2130', 0o05221, '', 'TC', 'FIXDELAY', line=1777)
W('25,2131', 0o00002, '', 'DEC', '2', kind='data', line=1778)

W('25,2132', 0o34740, '', 'CAF', 'ANTENBIT', 'MANEUVER TRUNNION ANGLE TO NOMINAL POS.', line=1780)
# Page 530
W('25,2133', 0o70110, '', 'MASK', 'RADMODES', line=1782)
W('25,2134', 0o10000, '', 'CCS', 'A', line=1783)
W('25,2135', 0o34735, '', 'CAF', 'BIT15', '0 FOR MODE 1 AND 180 FOR MODE 2.', line=1784)
W('25,2136', 0o02241, '', 'TC', 'RRTONLY', line=1785)

W('25,2137', 0o34740, '', 'CAF', 'ANTENBIT', 'NOT PUT SHAFT IN RIGHT POSITION', line=1787)
W('25,2140', 0o70110, '', 'MASK', 'RADMODES', line=1788)
W('25,2141', 0o10000, '', 'CCS', 'A', line=1789)
W('25,2142', 0o44736, '', 'CS', 'HALF', '-90 FOR MODE 2.', line=1790)
W('25,2143', 0o02244, '', 'TC', 'RRSONLY', line=1791)

W('25,2144', 0o44741, 'REPOSRPT', 'CS', 'REPOSBIT', 'RETURNS HERE FROM RR1AXIS IN REMODE', line=1793)
# REQUESTED DURING REPOSITION.
W('25,2145', 0o70110, '', 'MASK', 'RADMODES', 'REMOVE REPOSITION BIT.', line=1795)
W('25,2146', 0o54110, '', 'TS', 'RADMODES', line=1796)
W('25,2147', 0o74742, '', 'MASK', 'DESIGBIT', 'SEE IF SOMEONE IS WAITING TO DESIGNATE.', line=1797)
W('25,2150', 0o10000, '', 'CCS', 'A', line=1798)
W('25,2151', 0o12573, '', 'TCF', 'BEGDES', line=1799)
W('25,2152', 0o44752, '', 'CS', 'BIT2', 'IF NO FURTHER ANTENNA CONTROL REQUIRED,', line=1800)
W('25,2153', 0o00006, '', 'EXTEND', '', 'REMOVE ERROR COUNTER ENABLE.', line=1801)
W('25,2154', 0o03012, '', 'WAND', 'CHAN12', line=1802)
W('25,2155', 0o15261, '', 'TCF', 'TASKOVER', line=1803)

W('25,2156', 0o34752, 'SETRRECR', 'CAF', 'BIT2', 'SET UP RR ERROR COUNTERS', line=1805)
W('25,2157', 0o00006, '', 'EXTEND', line=1806)
W('25,2160', 0o02012, '', 'RAND', 'CHAN12', line=1807)
W('25,2161', 0o10000, '', 'CCS', 'A', 'DO NOT CLEAR LAST COMMAND IF', line=1808)
W('25,2162', 0o00002, '', 'TC', 'Q', 'ERROR COUNTERS ARE ENABLED', line=1809)

W('25,2163', 0o54112, '', 'TS', 'LASTYCMD', line=1811)
W('25,2164', 0o54113, '', 'TS', 'LASTXCMD', line=1812)
W('25,2165', 0o34752, '', 'CAF', 'BIT2', line=1813)
W('25,2166', 0o00006, '', 'EXTEND', line=1814)
W('25,2167', 0o05012, '', 'WOR', 'CHAN12', 'ENABLE RR CDU ERROR COUNTERS.', line=1815)
W('25,2170', 0o00002, '', 'TC', 'Q', line=1816)
# Page 531
# PROGRAM NAME:  REMODE
#
# FUNCTIONAL DESCRIPTION
#
# REMODE IS THE GENERAL REMODING SUBROUTINE.  IT DRIVES THE
# TRUNNION ANGLE TO 0 DEGREES IF THE CURRENT MODE IS MODE 1,
# 180 DEGREES FOR MODE 2, THEN DRIVES THE SHAFT ANGLE TO -45
# DEGREES, AND FINALLY DRIVES THE TRUNNION ANGLE TO -130 DEGREES,
# TO PLACE THE RR IN MODE 2, -50 DEGREES FOR MODE 1, BEFORE
# INITIATING 2-AXIS CONTROL.  ALL REMODING IS DONE WITH SINGLE
# AXIS ROTATIONS (RR1AXIS).  INITIALLY THE RR ANTENNA MODE FLAG
# (RADMODES BIT 12) IS CHECKED.  CONTROL IS THEN TRANSFERRED TO
# RRTONLY TO DRIVE THR TRUNNION ANGLE TO 0 DEGREES IF IN MODE 1
# OR 180 DEGREES IF IN MODE 2.  RRSONLY IS THEN CALLED TO DRIVE
# THE SHAFT ANGLE TO -45 DEGREES. THE RR ANTENNA MODE FLAG
# (RADMODES BIT 12) IS CHECKED AGAIN.  CONTROL IS AGAIN
# TRANSFERRED TO RRTONLY TO DRIVE THE TRUNNION ANGLE TO -130
# DEGREES TO PLACE THE RR IN MODE 2 IF CURRENTLY IN MODE 1 OR TO
# -50 DEGREES IF IN MODE 2 TO PLACE THE RR IN MODE 1.  RMODINV
# IS THEN CALLED TO SET RADMODES BIT 12 TO INDICATE THE NEW
# RR ANTENNA MODE.  THE REMODE FLAG (RADMODES BIT 14)
# IS REMOVED TO INDICATE THAT REMODING IS COMPLETE.  THE PROGRAM
# THEN EXITS TO STDESIG TO BEGIN 2-AXIS CONTROL.
#
# CALLIN SEQUENCE:
#
# FROM BEGDES WHEN REMODE FLAG (RADMODES BIT 14) IS SET.
# THIS FLAG MAY BE SET IN RRDESSM AND RRDESNB IF RRLIMCHK
# DETERMINES THAT THE DESIRED ANGLES ARE WITHIN THE LIMITS OF THE
# OTHER MODE.
#
# ERASABLE INIITIALIZATION REQUIRED:
#
# RADMODES
#
# SUBROUTINES CALLED:
#
# RRTONLY, RRSONL, RMODINV (ACTUALLY PART OF)
#
# JOBS OR TASKS INITIATED:
#
# NONE
#
# ALARMS:  NONE
#
# EXIT:  STDESIG

W('25,2171', 0o34740, 'REMODE', 'CAF', 'ANTENBIT', 'DRIVE TRUNNION TO 0 (180)', line=1865)
W('25,2172', 0o70110, '', 'MASK', 'RADMODES', '(ERROR COUNTER ALREADY ENABLED)', line=1866)
W('25,2173', 0o10000, '', 'CCS', 'A', line=1867)
W('25,2174', 0o34735, '', 'CAF', 'BIT15', line=1868)
W('25,2175', 0o02241, '', 'TC', 'RRTONLY', line=1869)

W('25,2176', 0o37740, '', 'CAF', '-45DEGSR', line=1871)
W('25,2177', 0o02244, '', 'TC', 'RRSONLY', line=1872)
# Page 532
W('25,2200', 0o40110, '', 'CS', 'RADMODES', line=1874)
W('25,2201', 0o74740, '', 'MASK', 'ANTENBIT', line=1875)
W('25,2202', 0o10000, '', 'CCS', 'A', line=1876)
W('25,2203', 0o32232, '', 'CAF', '-80DEGSR', 'GO TO T = -130 (-50).', line=1877)
W('25,2204', 0o62231, '', 'AD', '-50DEGSR', line=1878)
W('25,2205', 0o02241, '', 'TC', 'RRTONLY', line=1879)

W('25,2206', 0o40110, '', 'CS', 'RADMODES', line=1881)
W('25,2207', 0o74740, '', 'MASK', 'ANTENBIT', line=1882)
W('25,2210', 0o10000, '', 'CCS', 'A', line=1883)
W('25,2211', 0o34735, '', 'CAF', 'BIT15', 'GO TO T = -180 (+0).', line=1884)
W('25,2212', 0o02241, '', 'TC', 'RRTONLY', line=1885)

W('25,2213', 0o40110, '', 'CS', 'RADMODES', 'GO TO S = -90 (+0).', line=1887)
W('25,2214', 0o74740, '', 'MASK', 'ANTENBIT', line=1888)
W('25,2215', 0o10000, '', 'CCS', 'A', line=1889)
W('25,2216', 0o44736, '', 'CS', 'HALF', line=1890)
W('25,2217', 0o02244, '', 'TC', 'RRSONLY', line=1891)

W('25,2220', 0o02233, '', 'TC', 'RMODINV', line=1893)

W('25,2221', 0o44736, '', 'CS', 'REMODBIT', 'END OF REMODE.', line=1895)
W('25,2222', 0o70110, '', 'MASK', 'RADMODES', line=1896)
W('25,2223', 0o54110, '', 'TS', 'RADMODES', line=1897)

W('25,2224', 0o34742, '', 'CAF', 'DESIGBIT', 'WAS REMODE CALLED DURING DESIGNATE?', line=1899)
W('25,2225', 0o70110, '', 'MASK', 'RADMODES', '(BIT10 RADMODES = 1)', line=1900)
W('25,2226', 0o00006, '', 'EXTEND', line=1901)
W('25,2227', 0o13555, '', 'BZF', 'RGOODEND', 'NO -- RETURN TO CALLER WAITING IN RADSTALL', line=1902)
W('25,2230', 0o02602, '', 'TC', 'STDESIG', 'YES -- RETURN TO DESIGNATE', line=1903)
S('-45DEGSR', 'equals', 0o7740, line=1904)
W('25,2231', 0o67070, '-50DEGSR', 'DEC', '-.27778', kind='data', line=1905)
W('25,2232', 0o61615, '-80DEGSR', 'DEC', '-.44444', kind='data', line=1906)

W('25,2233', 0o22110, 'RMODINV', 'LXCH', 'RADMODES', 'INVERT THE MODE STATUS.', line=1908)
W('25,2234', 0o34740, '', 'CAF', 'ANTENBIT', line=1909)
W('25,2235', 0o00006, '', 'EXTEND', line=1910)
W('25,2236', 0o06001, '', 'RXOR', 'LCHAN', line=1911)
W('25,2237', 0o54110, '', 'TS', 'RADMODES', line=1912)
W('25,2240', 0o00002, '', 'TC', 'Q', line=1913)

# Page 533
# PROGRAM NAMES:        RRTONLY, RRSONLY
#
# FUNCTIONAL DESCRIPTION:
#
# RRTONLY AND RRSONLY ARE SUBROUTINES FOR DOING SINGLE AXIS
# RR MANEUVERS FOR REMODE AND REPOSITION.  IT DRIVES TO
# WITHIN 1 DEGREE.  INITIALLY, AT RR1AX2, THE REMODE AND REPOSITION
# FLAGS (RADMODES BITS 14, 11) ARE CHECKED.  IF BOTH EXIST,
# THE PROGRAM EXITS TO REPOSRPT (SEE DORREPOS).  THIS INDICATES
# THAT SOMEONE POSSIBLY REQUESTED A DESIGNATE (RADMODES BIT 10)
# WHICH REQUIRES A REMODE (RADMODES BIT 14) AND THAT A
# REPOSITION IS IN PROGRESS (RADMODES BIT 11).  IF NONE
# OR ONLY ONE OF THE FLAGS EXIST, REMODE OR REPOSITION, MAGSUB
# IS CALLED TO SEE IF THE APPROPRIATE ANGLE IS WITHIN 1 DEGREE.  IF YES,
# CONTROL RETURNS TO THE CALLING ROUTINE.  IF NOT, CONTROL IS
# TRANSFERRED TO RROUT FOR SINGLE AXIS MANEUVERS WITH THE OTHER
# ANGLE SET = 0.  FOLLOWING A .5 SECOND WAIT, THE ABOVE PROCEDURE IS
# REPEATED.
#
# CALLING SEQUENCE:     L-1     CAF     *ANGLE*         (DESIRED ANGLE SCALED PI)
# L       TC      RRTONLY         (TRUNNION ONLY)
# RRSONLY                         (SHAFT ONLY)
# RRTONLY IS CALLED BY PREPOS29;
# RRTONLY AND RRSONLY ARE CALLED BY DORREPOS AND REMODE
#
# ERASABLE INITIALIZATION REQUIRED:
#
# C(A) = DESIRED ANGLE, RADMODES
#
# SUBROUTINES CALLED:
#
# FIXDELAY, REPOSRPT, MAGSUB, RROUT
#
# JOBS OR TASKS INITIATED:
#
# NONE
#
# ALARMS:  NONE
#
# EXIT: REPOSRPT (REMODE AND REPOSITION FLAGS PRESENT -- RADMODES
# BITS 14, 11)
# L+1 (ANGLE WITHIN ONE DEGREE OR RR OUT OF AUTO MODE)

W('25,2241', 0o55316, 'RRTONLY', 'TS', 'RDES', 'DESIRED TRUNNION ANGLE.', line=1959)
W('25,2242', 0o34755, '', 'CAF', 'ZERO', line=1960)
W('25,2243', 0o12246, '', 'TCF', 'RR1AXIS', line=1961)

W('25,2244', 0o55316, 'RRSONLY', 'TS', 'RDES', 'SHAFT COMMANDS ARE UNRESOLVED SINCE THIS', line=1963)
W('25,2245', 0o34753, '', 'CAF', 'ONE', 'ROUTINE ENTERED ONLY WHEN T = 0 OR 180.', line=1964)

W('25,2246', 0o55317, 'RR1AXIS', 'TS', 'RRINDEX', line=1966)
W('25,2247', 0o00006, '', 'EXTEND', line=1967)
W('25,2250', 0o23315, '', 'QXCH', 'RRRET', line=1968)
W('25,2251', 0o12254, '', 'TCF', 'RR1AX2', line=1969)

# Page 534
W('25,2252', 0o05221, 'NXTRR1AX', 'TC', 'FIXDELAY', line=1972)
W('25,2253', 0o00062, '', 'DEC', '50', '2 SAMPLES PER SECOND.', kind='data', line=1973)

W('25,2254', 0o40110, 'RR1AX2', 'CS', 'RADMODES', 'IF SOMEONE REQUESTS A DESIGNATE WHICH', line=1975)
W('25,2255', 0o77710, '', 'MASK', 'PRIO22', 'REQUIRES A REMODE AND A REPOSITION IS IN', line=1976)
W('25,2256', 0o00006, '', 'EXTEND', '', 'PROGRESS, INTERRUPT IT AND START THE', line=1977)
W('25,2257', 0o12144, '', 'BZF', 'REPOSRPT', 'REMODE IMMEDIATELY.', line=1978)

W('25,2260', 0o31316, '', 'CA', 'RDES', line=1980)
W('25,2261', 0o00006, '', 'EXTEND', line=1981)
W('25,2262', 0o51317, '', 'INDEX', 'RRINDEX', line=1982)
W('25,2263', 0o20035, '', 'MSU', 'CDUT', line=1983)
W('25,2264', 0o54061, '', 'TS', 'ITEMP1', 'SAVE ERROR SIGNAL.', line=1984)
W('25,2265', 0o00006, '', 'EXTEND', line=1985)
W('25,2266', 0o72305, '', 'MP', 'RRSPGAIN', 'TRIES TO NULL .7 OF ERROR OVER NEXT .5', line=1986)
W('25,2267', 0o54001, '', 'TS', 'L', line=1987)
W('25,2270', 0o30110, '', 'CA', 'RADMODES', line=1988)
W('25,2271', 0o74752, '', 'MASK', 'AUTOMBIT', line=1989)
W('25,2272', 0o56061, '', 'XCH', 'ITEMP1', 'STORE RR-OUT-OF-AUTO-MODE BIT.', line=1990)
W('25,2273', 0o04512, '', 'TC', 'MAGSUB', 'SEE IF WITHIN ONE DEGREE.', line=1991)
W('25,2274', 0o77644, '', 'DEC', '-.00555', 'SCALED IN HALF-REVS.', kind='data', line=1992)

W('25,2275', 0o10061, '', 'CCS', 'ITEMP1', 'NO.  IF RR OUT OF AUTO MODE, EXIT.', line=1994)
W('25,2276', 0o01315, '', 'TC', 'RRRET', 'RETURN TO CALLER.', line=1995)

W('25,2277', 0o11317, '', 'CCS', 'RRINDEX', 'COMMAND FOR OTHER AXIS IS ZERO.', line=1997)
W('25,2300', 0o12302, '', 'TCF', '+2', 'SETTING A TO 0.', line=1998)
W('25,2301', 0o56001, '', 'XCH', 'L', line=1999)
W('25,2302', 0o53110, '', 'DXCH', 'TANG', line=2000)

W('25,2303', 0o02306, '', 'TC', 'RROUT', line=2002)

W('25,2304', 0o12252, '', 'TCF', 'NXTRR1AX', 'COME BACK IN .5 SECONDS.', line=2004)

W('25,2305', 0o22715, 'RRSPGAIN', 'DEC', '.59062', 'NULL .7 ERROR IN .5 SEC.', kind='data', line=2006)

# Page 535
# PROGRAM NAME:  RROUT
#
# FUNCTIONAL DESCRIPTION:
#
# RROUT RECEIVES RR GYRO COMMANDS IN TANG, TANG +1 IN RR
# ERROR COUNTER SCALING.  RROUT THEN LIMITS THEM AND
# GENERATES COMMANDS TO THE CDU TO ADJUST THE ERROR COUNTERS
# TO THE DESIRED VALUES.  INITIALLY MAGSUB CHECKS THE MAGNITUDE OF
# THE COMMAND (SHAFT ON 1ST PASS) TO SEE IF IT IS GREATER THAN
# 384 PULSES.  IF NOT, CONTROL IS TRANFERRED TO RROUTLIM TO
# LIMIT THE COMMAND TO +384 OR -384 PULSES.  THE DIFFERENCE IS
# THEN CALCULATED BETWEEN THE DESIRED STATE AND TEH PRESENT STATE OF
# THE ERROR COUNTER AS RECORDED IN LASTYCMD AND LASTXCMD.
# THE RESULT IS STORED IN OPTXCMD (1ST PASS) AND OPTYCMD (2ND
# PASS).  FOLLOWING THE SECOND PASS, FOR THE TRUNNION COMMAND, THE
# OCDUT AND OCDUS ERROR COUNTER DRIVE BITS (CHAN 14 BITS 12, 11)
# ARE SET.  THIS PROGRAM THEN EXITS TO THE CALLING PROGRAM.
#
# CALLING SEQUENCE:
#
# L TC RROUT (WITH RUPT INHIBITED) RROUT IS CALLED BY
# RRTONLY, RRSONLY, AND DODES
#
# ERASABLE INITIALIZATION REQURIED:
#
# TANG, TANG +1 (DESIRED COMMANDS), LASTYCMD, LASTXCMD
# (1ST PASS = 0), RR ERROR COUNTER ENAGLE SET (CHAN 12 BIT 2).
#
# SUBROUTINES CALLED:
#
# MAGSUB
#
# JOBS OR TASKS INITIATED:
#
# NONE
#
# ALARMS:  NONE
#
# EXIT:  L+1 (ALWAYS)

W('25,2306', 0o22002, 'RROUT', 'LXCH', 'Q', 'SAVE RETURN', line=2049)
W('25,2307', 0o34753, '', 'CAF', 'ONE', 'LOOP TWICE.', line=2050)
W('25,2310', 0o54062, 'RROUT2', 'TS', 'ITEMP2', line=2051)
W('25,2311', 0o50000, '', 'INDEX', 'A', line=2052)
W('25,2312', 0o31107, '', 'CA', 'TANG', line=2053)
W('25,2313', 0o54061, '', 'TS', 'ITEMP1', 'SAVE SIGN COMMAND FOR LIMITING.', line=2054)

W('25,2314', 0o04512, '', 'TC', 'MAGSUB', 'SEE IF WITHIN LIMITS.', line=2056)
W('25,2315', 0o77177, '-RRLIMIT', 'DEC', '-384', kind='data', line=2057)
W('25,2316', 0o12335, '', 'TCF', 'RROUTLIM', 'LIMIT COMMAND TO MAG OF 384.', line=2058)

W('25,2317', 0o30061, 'SETRRCTR', 'CA', 'ITEMP1', 'COUNT OUT DIFFERENCE BETWEEN DESIRED', line=2060)
W('25,2320', 0o50062, '', 'INDEX', 'ITEMP2', 'STATE AND PRESENT STATE AS RECORDED IN', line=2061)
W('25,2321', 0o56112, '', 'XCH', 'LASTYCMD', 'LASTYCMD AND LASTXCMD', line=2062)
W('25,2322', 0o40000, '', 'COM', line=2063)
# Page 536
W('25,2323', 0o60061, '', 'AD', 'ITEMP1', line=2065)
W('25,2324', 0o64754, '', 'AD', 'NEG0', 'PREVENT +0 IN OUTCOUNTER', line=2066)
W('25,2325', 0o50062, '', 'INDEX', 'ITEMP2', line=2067)
W('25,2326', 0o54053, '', 'TS', 'CDUTCMD', line=2068)

W('25,2327', 0o10062, '', 'CCS', 'ITEMP2', 'PROCESS BOTH INPUTS.', line=2070)
W('25,2330', 0o12310, '', 'TCF', 'RROUT2', line=2071)

W('25,2331', 0o35020, '', 'CAF', 'PRIO6', 'ENABLE COUNTERS.', line=2073)
W('25,2332', 0o00006, '', 'EXTEND', line=2074)
W('25,2333', 0o05014, '', 'WOR', 'CHAN14', 'PUT ON CDU DRIVES S AND T', line=2075)
W('25,2334', 0o00001, '', 'TC', 'L', 'RETURN.', line=2076)

W('25,2335', 0o10061, 'RROUTLIM', 'CCS', 'ITEMP1', 'LIMIT COMMAND TO ABS VAL OF 384.', line=2078)
W('25,2336', 0o42315, '', 'CS', '-RRLIMIT', line=2079)
W('25,2337', 0o12341, '', 'TCF', '+2', line=2080)
W('25,2340', 0o32315, '', 'CA', '-RRLIMIT', line=2081)
W('25,2341', 0o54061, '', 'TS', 'ITEMP1', line=2082)
W('25,2342', 0o12320, '', 'TCF', 'SETRRCTR +1', line=2083)

# Page 537
# ROUTINE TO ZERO THE RR CDUS AND DETERMINE THE ANTENNA MODE.

W('25,2343', 0o32372, 'RRZERO', 'CAF', 'BIT11+1', 'SEE IF MONITOR REPOSITION OR NOT IN AUTO', line=2088)
W('25,2344', 0o70110, '', 'MASK', 'RADMODES', "IF SO, DON'T RE-ZERO CDUS.", line=2089)
W('25,2345', 0o10000, '', 'CCS', 'A', line=2090)
W('25,2346', 0o13530, '', 'TCF', 'RADNOOP', '(IMMEDIATE TASK TO RGOODEND).', line=2091)

W('25,2347', 0o00004, '', 'INHINT', line=2093)
W('25,2350', 0o44737, '', 'CS', 'RCDU0BIT', 'SET FLAG TO SHOW ZEROING IN PROGRESS.', line=2094)
W('25,2351', 0o70110, '', 'MASK', 'RADMODES', line=2095)
W('25,2352', 0o64737, '', 'AD', 'RCDU0BIT', line=2096)
W('25,2353', 0o54110, '', 'TS', 'RADMODES', line=2097)

W('25,2354', 0o34753, '', 'CAF', 'ONE', line=2099)
W('25,2355', 0o05203, '', 'TC', 'WAITLIST', line=2100)
#   EBANK= LOSCOUNT
W('25,2356', 0o02370, '', '2CADR', 'RRZ2', kind='data', line=2102)
W('25,2357', 0o52067, kind='data', line=2102)

W('25,2360', 0o40110, '', 'CS', 'RADMODES', 'SEE IF IN AUTO MODE.', line=2104)
W('25,2361', 0o74752, '', 'MASK', 'AUTOMBIT', line=2105)
W('25,2362', 0o10000, '', 'CCS', 'A', line=2106)
W('25,2363', 0o12366, '', 'TCF', 'ROADBACK', line=2107)
W('25,2364', 0o05567, '', 'TC', 'ALARM', 'AUTO DISCRETE NOT PRESENT -- TRYING', line=2108)
W('25,2365', 0o00510, '', 'OCT', '510', kind='data', line=2109)
W('25,2366', 0o00003, 'ROADBACK', 'RELINT', line=2110)
W('25,2367', 0o14631, '', 'TCF', 'SWRETURN', line=2111)

W('25,2370', 0o02071, 'RRZ2', 'TC', 'RRZEROSB', 'COMMON TO TURNON AND RRZERO.', line=2113)
W('25,2371', 0o13546, '', 'TCF', 'ENDRADAR', line=2114)

W('25,2372', 0o02001, 'BIT11+1', 'OCT', '02001', kind='data', line=2116)

# Page 538
# PROGRAM NAME:  RRDESSM
#
# FUNCTIONAL DESCRIPTION:
#
# THIS INTERPRETIVE ROUTINE WILL DESIGNATE, IF DESIRED ANGLES ARE
# WITHIN THE LIMITS OF EITHER MODE, TO A LINE-OF-SIGHT (LOS) VECTOR
# (HALF-UNIT) KNOWN WITH RESPECT TO THE STABLE MEMBER PRESENT
# ORIENTATION.  INITIALLY THE IMU CDU'S ARE READ AND CONTROL
# TRANSFERRED TO SMNB TO TRANSFORM THE LOS VECTOR FROM STABLE
# MEMBER TO NAVIGATION BASE COORDINATES (SEE STG MEMO 699)
# RRANGLES IS THEN CALLED TO CALCULATE THE RR GIMBAL ANGLES,
# TRUNNION AND SHAFT, FOR BOT THE PRESENT AND ALTERNATE MODE.
# RRLIMCHK IS CALLED TO SEE IF THE ANGLES CALCULATED FOR THE
# PRESENT MODE ARE WITHIN LIMITS.  IF WITHIN LIMITS, THE RETUREN
# LOCATION IS INCREMENTED, INASMUCH AS NO VEHICLE MANEUVER IS
# REQUIRED, BEFORE EXITING TO STARTDES.  IF NOT WITHIN THE LIMITS OF THE
# CURRENT MODE, TRYSWS IS CALLED.  FOLLOWING INVERTING OF THE RR
# ANTENNA MODE FLAG (RADMODES BIT 12), RRLIMCHK IS CALLED
# TO SEE IF THE ANGLES CALCULATED FOR THE ALTERNATE MODE ARE WITHIN
# LIMITS.  IF YES, THE RR ANTENNA MODE FLAG IS AGAIN INVERTED,
# THE REMODE FLAG (RADMODES BIT 14) SET, AND THE RETURN LOCATION
# INCREMENTED, TO INDICATE NO VEHICLE MANEUVER IS REQUIRED, BEFORE
# EXITING TO STARTDES.  IF THESE ANGLES ARE NOT WITHIN LIMITS
# OF THE ALTERNATE MODE, THE RR ANTENNA MODE FLAG (RADMODES
# BIT 12) IS INVERTED BEFORE RETURNING DIRECTLY TO THE CALLING PROGRAM
# TO INDICATE THAT A VEHICLE MANEUVER IS REQUIRED.
#
# CALLING SEQUENCE:
#
# L       STCALL  RRTARGET        (LOS HALF-UNIT VECTOR IN SM COORDINATES)
# L+1     RRDESM
# L+2     BASIC                   (VEHICLE MANEUVER REQUIRED)
# L+3     BASIC                   (NO VEHICLE MANEUVER REQUIRED)
#
# ERASABLE INITIALIZATION REQUIRED:
#
# RRTARGET, RADMODES
#
# SUBROUTINES CALLED:
#
# READCDUS, SMNB, RRANGLES, RRLIMCHK, TRYSWS (ACTUALLY
# PART OF), RMODINV
#
# JOBS OR TASKS INITIATED:
#
# NONE
#
# ALARMS:  NONE
#
# EXIT:  L+2 (NEITHER SET OF ANGLES ARE WITHIN LIMITS OF RELATED MODE)
# STARTDES (DESIGNATE POSSIBLE AT PRESENT VEHICLES ATTITUDE -- RETURNS
# TO L+3 FROM STARTDES)

W('25,2373', 0o43020, 'RRDESSM', 'STQ', 'CLEAR', kind='interp', line=2172)
W('25,2374', 0o01113, '', '', 'DESRET', kind='operand', line=2173)
# Page 539
W('25,2375', 0o00271, '', '', 'RRNBSW', kind='operand', line=2175)
W('25,2376', 0o77624, '', 'CALL', '', 'COMPUTES SINES AND COSINES, ORDER Y Z X', kind='interp', line=2176)
W('25,2377', 0o47537, '', '', 'CDUTRIG', kind='operand', line=2177)
W('25,2400', 0o45175, '', 'VLOAD', 'CALL', 'LOAD VECTOR AND CALL TRANSFORMATION', kind='interp', line=2178)
W('25,2401', 0o01102, '', '', 'RRTARGET', kind='operand', line=2179)
W('25,2402', 0o47671, '', '', '*SMNB*', kind='operand', line=2180)

W('25,2403', 0o77624, '', 'CALL', '', 'GET RR GIMBAL ANGLES IN PRESENT AND', kind='interp', line=2182)
W('25,2404', 0o26133, '', '', 'RRANGLES', 'ALTERNATE MODE.', kind='operand', line=2183)
W('25,2405', 0o77776, '', 'EXIT', kind='interp', line=2184)

W('25,2406', 0o00004, '', 'INHINT', line=2186)
W('25,2407', 0o04523, '', 'TC', 'RRLIMCHK', line=2187)
W('25,2410', 0o01107, '', 'ADRES', 'MODEA', 'CONFIGURATION FOR CURRENT MODE.', kind='data', line=2188)
W('25,2411', 0o02414, '', 'TC', '+3', 'NOT IN CURRENT MODE', line=2189)
W('25,2412', 0o25113, 'OKDESSM', 'INCR', 'DESRET', 'INCREMENT SAYS NO VEHICLE MANEUVER REQ.', line=2190)
W('25,2413', 0o02432, '', 'TC', 'STARTDES', 'SHOW DESIGNATE REQUIRED', line=2191)
W('25,2414', 0o40104, '', 'CS', 'FLAGWRD8', line=2192)
W('25,2415', 0o74744, '', 'MASK', 'SURFFBIT', 'CHECK IF ON LUNAR SURFACE (SURFFLAG=P22F)', line=2193)
W('25,2416', 0o00006, '', 'EXTEND', line=2194)
W('25,2417', 0o12456, '', 'BZF', 'NORDSTAL', 'BRANCH -- YES -- CANNOT DESIGNATE IN MODE 2', line=2195)
W('25,2420', 0o02461, '', 'TC', 'TRYSWS', line=2196)

W('25,2421', 0o40104, 'LUNDESCH', 'CS', 'FLAGWRD8', 'OVERFLOW RETURN FROM RRANGLES', line=2198)
W('25,2422', 0o74744, '', 'MASK', 'SURFFBIT', 'CHECK IF ON LUNAR SURFACE', line=2199)
W('25,2423', 0o00006, '', 'EXTEND', line=2200)
W('25,2424', 0o12456, '', 'BZF', 'NORDSTAL', 'BRANCH -- YES -- RETURN TO CALLER -- ALARM 527', line=2201)
W('25,2425', 0o30074, '', 'CA', 'STATE', line=2202)
W('25,2426', 0o74745, '', 'MASK', 'RNDVZBIT', line=2203)
W('25,2427', 0o10000, '', 'CCS', 'A', 'TEST RNDVZFLG', line=2204)
W('25,2430', 0o02471, '', 'TC', 'NODESSM', 'NOT ON MOON -- CALL FOR ATTITUDE MANEUVER', line=2205)
W('25,2431', 0o15155, '', 'TCF', 'ENDOFJOB', '... BUT NOT IN R29.', line=2206)

# Page 540
# PROGRAM NAME:  STARTDES
#
# FUNCTIONAL DESCRIPTION:
#
# STARTDES IS ENTERED WHEN WE ARE READY TO BEGIN DESIGNATION.
# BIT 14 OF RADMODES IS ALREADY SET IF A REMODE IS REQUIRED.
# AT THIS TIME, THE RR ANTENNA MAY BE IN A REPOSITON
# OPERATION.  IN THIS CASE, IF A REMODE IS REQUIRED IT MAY HAVE
# ALREADY BEGUN BUT IN ANY CASE THE REPOSITION WILL BE INTERRUPTED.
# OTHERWISE, THE REPOSITION WILL BE COMPLETED BEFORE 2-AXIS
# DESIGNATION BEGINS.  INITIALLY DESCOUNT IS SET = 60 TO INDICATE
# THAT 30 SECONDS WILL BE ALLOWED FOR THE RR DATA GOOD INBIT
# (CHAN 33 BIT 4) IF LOCK-ON IS DESIRED (STATE BIT 5).  BIT 10
# OF RADMODES IS SET TO SHOW THAT A DESIGNATE IS REQUIRED.
# THE REPOSITON FLAG (RADMODES BIT 11) IS CHECKED.  IF SET,
# THE PROGRAM EXITS TO L+3 OF THE CALLING PROGRAM (SEE RRDESSM
# AND RRDESNB).  THE PROGRAM WILL BEGIN DESIGNATING TO THE DESIRED
# ANGLES FOLLOWING THE REPOSITON OR REMODE IF ONE WAS
# REQUESTED.  IF THE REPOSITON FLAG IS NOT SET, SETRRECR IS CALLED
# WITH SETS THE RR ERROR COUNTER ENABLE BIT (CHAN 12 BIT 2)
# AND SETS LASTYCMD AND LASTXCMD = 0 TO INDICATE THE
# DIFFERENCE BETWEEN THE PRESENT AND DESIRED STATE OF THE ERROR
# COUNTERS.  A 20 MILLISECOND WAITLIST CALL IS SET FOR BEGDES
# AFTER WHICH THE PROGRAM EXITS TO L+3 OF TEH CALLING PROGRAM.
#
# CALLING SEQUENCE:
#
# FROM RRDESSM AND RRDESNB WHEN ANGLES WITHIN LIMITS.
#
# ERASABLE INITIALIZATION REQUIRED:
#
# RADMODES, (SEE DODES)
#
# SUBROUTINES CALLED
#
# SETRRECR, WAITLIST
#
# JOBS OR TASKS INITIATED:
#
# BEGDES
#
# ALARMS:  NONE
#
# EXIT: L+3 OF CALLING PROGRAM (SEE RRDESSM)
# L+2 OF CALLING PROGRAM (SEE RRDESNB)

W('25,2432', 0o25113, 'STARTDES', 'INCR', 'DESRET', line=2255)
W('25,2433', 0o40110, '', 'CS', 'RADMODES', line=2256)
W('25,2434', 0o74742, '', 'MASK', 'DESIGBIT', line=2257)
W('25,2435', 0o26110, '', 'ADS', 'RADMODES', line=2258)
W('25,2436', 0o74741, '', 'MASK', 'REPOSBIT', 'SEE IF REPOSITIONING IN PROGRESS.', line=2259)
W('25,2437', 0o10000, '', 'CCS', 'A', line=2260)
W('25,2440', 0o12446, '', 'TCF', 'DESRETRN', 'ECTR ALREADY SET UP.', line=2261)

W('25,2441', 0o02156, '', 'TC', 'SETRRECR', 'SET UP ERROR COUNTERS.', line=2263)
# Page 541
W('25,2442', 0o34752, '', 'CAF', 'TWO', line=2265)
W('25,2443', 0o05203, '', 'TC', 'WAITLIST', line=2266)
#   EBANK= LOSCOUNT
W('25,2444', 0o02573, '', '2CADR', 'BEGDES', kind='data', line=2268)
W('25,2445', 0o52067, kind='data', line=2268)

W('25,2446', 0o31306, 'DESRETRN', 'CA', 'RADCADR', 'FIRST PASS THRU DESIGNATE', line=2270)
W('25,2447', 0o00006, '', 'EXTEND', line=2271)
W('25,2450', 0o12452, '', 'BZF', 'DESRTRN', 'YES   SET EXIT', line=2272)
W('25,2451', 0o05155, '', 'TC', 'ENDOFJOB', 'NO', line=2273)
W('25,2452', 0o00003, 'DESRTRN', 'RELINT', line=2274)
W('25,2453', 0o25113, '', 'INCR', 'DESRET', line=2275)
W('25,2454', 0o31113, '', 'CA', 'DESRET', line=2276)
W('25,2455', 0o14640, '', 'TCF', 'BANKJUMP', line=2277)

W('25,2456', 0o34755, 'NORDSTAL', 'CAF', 'ZERO', 'ZERO RADCADR TO WIPE OUT ANYONE', line=2279)
W('25,2457', 0o55306, '', 'TS', 'RADCADR', 'WAITING IN RADSTALL SINCE WE ARE NOW', line=2280)
W('25,2460', 0o12452, '', 'TCF', 'DESRTRN', 'RETURNING TO P20 AND MAY DO NEW RADSTALL', line=2281)

# Page 542
# SEE IF RRDESSM CAN BE ACCOMPLISHED AFTER A REMODE.

W('25,2461', 0o02233, 'TRYSWS', 'TC', 'RMODINV', '(NOTE RUPT INHIBIT)', line=2286)
W('25,2462', 0o04523, '', 'TC', 'RRLIMCHK', 'TRY DIFFERENT MODE.', line=2287)
W('25,2463', 0o01111, '', 'ADRES', 'MODEB', kind='data', line=2288)
W('25,2464', 0o12471, '', 'TCF', 'NODESSM', 'VEHICLE MANEUVER REQUIRED', line=2289)

W('25,2465', 0o02233, '', 'TC', 'RMODINV', 'RESET BIT12', line=2291)
W('25,2466', 0o34736, '', 'CAF', 'REMODBIT', 'SET FLAG FOR REMODE.', line=2292)
W('25,2467', 0o26110, '', 'ADS', 'RADMODES', line=2293)

W('25,2470', 0o12412, '', 'TCF', 'OKDESSM', line=2295)

W('25,2471', 0o02233, 'NODESSM', 'TC', 'RMODINV', 'RE-INVERT MODE AND RETURN', line=2297)
W('25,2472', 0o25113, '', 'INCR', 'DESRET', 'TO CALLER +2', line=2298)
W('25,2473', 0o12456, '', 'TCF', 'NORDSTAL', line=2299)

W('25,2474', 0o00074, 'MAXTRYS', 'DEC', '60', kind='data', line=2301)

# Page 543
# DESIGNATE TO SPECIFIC RR GIMBAL ANGLES (INDEPENDENT OF VEHICLE MOTION).  ENTER WITH DESIRED ANGLES IN
# TANG AND TANG +1.

W('25,2475', 0o04645, 'RRDESNB', 'TC', 'MAKECADR', line=2307)
W('25,2476', 0o55113, '', 'TS', 'DESRET', line=2308)

W('25,2477', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET FLAG TO PREVENT DODES FROM GOING', line=2310)
W('25,2500', 0o00041, '', 'ADRES', 'LOSCMFLG', 'BACK TO R21', kind='data', line=2311)
W('25,2501', 0o32474, '', 'CA', 'MAXTRYS', 'SET TIME LIMIT COUNTER', line=2312)
W('25,2502', 0o55114, '', 'TS', 'DESCOUNT', 'FOR DESIGNATE', line=2313)
W('25,2503', 0o00004, '', 'INHINT', '', 'SEE IF CURRENT MODE OK.', line=2314)
W('25,2504', 0o02540, '', 'TC', 'RRLIMNB', 'DO SPECIAL V41 LIMIT CHECK', line=2315)
W('25,2505', 0o01107, '', 'ADRES', 'TANG', kind='data', line=2316)
W('25,2506', 0o12523, '', 'TCF', 'TRYSWN', 'SEE IF IN OTHER MODE.', line=2317)

W('25,2507', 0o00003, 'OKDESNB', 'RELINT', line=2319)
W('25,2510', 0o00006, '', 'EXTEND', line=2320)
W('25,2511', 0o31110, '', 'DCA', 'TANG', line=2321)
W('25,2512', 0o53753, '', 'DXCH', 'TANGNB', line=2322)
W('25,2513', 0o06037, '', 'TC', 'INTPRET', line=2323)

W('25,2514', 0o77624, '', 'CALL', '', 'GET LOS IN NB COORDS.', kind='interp', line=2325)
W('25,2515', 0o46041, '', '', 'RRNB', kind='operand', line=2326)
W('25,2516', 0o01102, '', 'STORE', 'RRTARGET', kind='interp', line=2327)

W('25,2517', 0o77414, '', 'SET', 'EXIT', kind='interp', line=2329)
W('25,2520', 0o00071, '', '', 'RRNBSW', kind='operand', line=2330)

W('25,2521', 0o00004, '', 'INHINT', line=2332)
W('25,2522', 0o12433, '', 'TCF', 'STARTDES +1', line=2333)
W('25,2523', 0o02233, 'TRYSWN', 'TC', 'RMODINV', 'SEE IF OTHER MODE WILL DO.', line=2334)
W('25,2524', 0o02540, '', 'TC', 'RRLIMNB', 'DO SPECIAL V41 LIMIT CHECK', line=2335)
W('25,2525', 0o01107, '', 'ADRES', 'TANG', kind='data', line=2336)
W('25,2526', 0o12533, '', 'TCF', 'NODESNB', 'NOT POSSIBLE.', line=2337)

W('25,2527', 0o02233, '', 'TC', 'RMODINV', line=2339)
W('25,2530', 0o34736, '', 'CAF', 'REMODBIT', 'CALL FOR REMODE.', line=2340)
W('25,2531', 0o26110, '', 'ADS', 'RADMODES', line=2341)
W('25,2532', 0o12507, '', 'TCF', 'OKDESNB', line=2342)

W('25,2533', 0o02233, 'NODESNB', 'TC', 'RMODINV', 'REINVERT MODE BIT.', line=2344)
W('25,2534', 0o05567, '', 'TC', 'ALARM', 'BAD INPUT ANGLES.', line=2345)
W('25,2535', 0o00502, '', 'OCT', '502', kind='data', line=2346)
W('25,2536', 0o06011, '', 'TC', 'CLRADMOD', line=2347)
W('25,2537', 0o05155, '', 'TC', 'ENDOFJOB', 'AVOID 503 ALARM.', line=2348)

W('25,2540', 0o50002, 'RRLIMNB', 'INDEX', 'Q', 'THIS ROUTINE IS IDENTICAL TO RRLIMCHK', line=2350)
W('25,2541', 0o30000, '', 'CAF', '0', 'EXCEPT THAT THE MODE 1 SHAFT LOWER', line=2351)
W('25,2542', 0o24002, '', 'INCR', 'Q', 'LIMIT IS -85 INSTEAD OF -70 DEGREES', line=2352)
W('25,2543', 0o00006, '', 'EXTEND', line=2353)
# Page 544
W('25,2544', 0o50000, '', 'INDEX', 'A', 'READ GIMBAL ANGLES INTO ITEMP STORAGE', line=2355)
W('25,2545', 0o30001, '', 'DCA', '0', line=2356)
W('25,2546', 0o52062, '', 'DXCH', 'ITEMP1', line=2357)
W('25,2547', 0o22002, '', 'LXCH', 'Q', 'L(CALLER +2) TO L', line=2358)

W('25,2550', 0o34740, '', 'CAF', 'ANTENBIT', 'SEE WHICH MODE RR IS IN', line=2360)
W('25,2551', 0o70110, '', 'MASK', 'RADMODES', line=2361)
W('25,2552', 0o10000, '', 'CCS', 'A', line=2362)
W('25,2553', 0o14550, '', 'TCF', 'MODE2CHK', 'MODE 2 CAN USE RRLIMCHK CODING', line=2363)
W('25,2554', 0o30061, '', 'CA', 'ITEMP1', line=2364)
W('25,2555', 0o04512, '', 'TC', 'MAGSUB', 'MODE 1 IS DEFINED AS', line=2365)
W('25,2556', 0o66161, '', 'DEC', '-.30555', '1     ABS(T) L 55 DEGS', kind='data', line=2366)
W('25,2557', 0o00001, '', 'TC', 'L', '2     SHAFT LIMITS AT +59, -85 DEGS', line=2367)

W('25,2560', 0o30062, '', 'CA', 'ITEMP2', 'LOAD SHAFT ANGLE', line=2369)
W('25,2561', 0o00006, '', 'EXTEND', line=2370)
W('25,2562', 0o62570, '', 'BZMF', 'NEGSHAFT', 'IF NEGATIVE SHAFT ANGLE, ADD 20.5 DEGS', line=2371)
W('25,2563', 0o64562, '', 'AD', '5.5DEGS', line=2372)
W('25,2564', 0o04512, 'SHAFTLIM', 'TC', 'MAGSUB', line=2373)
W('25,2565', 0o64420, '', 'DEC', '-.35833', '64.5 DEGREES', kind='data', line=2374)
W('25,2566', 0o00001, '', 'TC', 'L', 'NOT IN LIMITS', line=2375)
W('25,2567', 0o04560, '', 'TC', 'RRLIMOK', 'IN LIMITS', line=2376)
W('25,2570', 0o62572, 'NEGSHAFT', 'AD', '20.5DEGS', 'MAKE NEGATIVE SHAFT LIMIT -85 DEGREES', line=2377)
W('25,2571', 0o12564, '', 'TCF', 'SHAFTLIM', line=2378)

W('25,2572', 0o03512, '20.5DEGS', 'DEC', '.11389', kind='data', line=2380)

# Page 545
# PROGRAM NAME:  BEGDES
#
# FUNCTIONAL DESCRIPTION:
#
# BEGDES CHECKS VARIOUS DESIGNATE REQUESTS AND REQUESTS THE
# ACTUAL RR DESIGNATION.  INITIALLY A CHECK IS MADE TO SEE IF A
# REMODE (RADMODES BIT 14) IS REQUESTED OR IN PROGRESS.  IF SO,
# CONTROL IS TRANFERRED TO STDESIG AFTER ROUTINE REMODE IS
# EXECUTED.  IF NO REMODE, STDESIG IS IMMEDIATELY CALLED WHERE
# FIRST THE REPOSITION FLAG (RADMODES BIT 11) IS CHECKED.  IF
# PRESENT, THE DESIGNATE FLAG (RADMODES BIT 10) IS REMOVED
# AFTER WHICH THE PROGRAM EXITS TO RDBADEND.  IF THE REPOSITION
# FLAG IS NOT PRESET, THE CONTINUOUS DESIGNATE FLAG (RADMODES
# BIT 15) IS CHECKED.  IF PRESENT, AN EXECUTIVE CALL IS IMMEDIATELY
# MADE FOR DODES AFTER WHICH A .5 SECOND WAIT IS INITIATED BEFORE
# REPEATING AT STDESIG.  IF THE RR SEARCH ROUTINE (LRS24.1) IS DESIGNATING
# TO A NEW POINT (NEWPTFLG SET) THE CURRENT DESIGNATE TASK IS TERMINATED.
# IF CONTINUOUS DESIGNATE IS NOT WANTED, THE DESIGNATE FLAG (RADMODES
# BIT 10) IS CHECKED.  IF NOT PRESENT, THE PROGRAM EXITS TO ENDRADAR TO
# CHECK RR CDU FAIL BEFORE RETURNING TO THE CALLING PROGRAM.  IF DESIGNATE
# IS STILL REQUIRED, DESCOUNT IS CHECKED TO SEE IF THE 30 SECONDS HAS
# EXPIRED BEFORE RECEIVING THE RR DATA GOOD (CHAN 33 BIT 4)
# SIGNAL.  IF OUT OF TIME, PROGRAM ALARM 00503 IS REQUESTED, THE
# RR AUTO TRACKER ENABLE AND RR ERROR COUNTER ENABLE
# (CHAN 12 BITS 14,2) BITS REMOVED, AND THE DESIGNATE FLAG
# (RADMODES BIT 10) REMOVED BEFORE EEXITING TO RDBADEND.  IF
# TIME HAS NOT EXPIRED, DESCOUNT IS DECREMENTED, THE
# EXECUTIVE CALL MADE FOR DODES, AND A .5 SECOND WAIT INITIATED
# BEFORE REPEATING THIS PROCEDURE AT STDESIG.
#
# CALLING SEQUENCE:
#
# WAITLIST CALL FROM STARTDES
# TCF BEGDES FROM DORREPOS
# TC STDESIG RETURNING, FROM REMODE
#
# ERASABLE INITIALIZATION REQUIRED:
#
# DESCOUNT, FINDVAC
#
# JOBS OR TASKS INITIATED:  DODES
#
# ALARMS:  PROGRAM ALARM 00503 (30 SECONDS HAVE EXPIRED) WITH NO RR DATA
# GOOD (CHAN 33 BIT 4) RECEIVED WHEN LOCK-ON (STATE BIT 5) WAS REQUESTED.
#
# EXIT:         TASKOVER (SEARCH PATTERN DESIGNATING TO NEW POINT)
# ENDRADAR (NO DESIGNATE -- RADMODES BIT 10)
# RDBADEND (REPOSITION OR 30 SECONDS EXPIRED)

W('25,2573', 0o40110, 'BEGDES', 'CS', 'RADMODES', line=2432)
# Page 546
W('25,2574', 0o74736, '', 'MASK', 'REMODBIT', line=2434)
W('25,2575', 0o10000, '', 'CCS', 'A', line=2435)
W('25,2576', 0o02602, '', 'TC', 'STDESIG', line=2436)
W('25,2577', 0o02171, '', 'TC', 'REMODE', line=2437)
W('25,2600', 0o05221, 'DESLOOP', 'TC', 'FIXDELAY', '2 SAMPLES PER SECOND.', line=2438)
W('25,2601', 0o00062, '', 'DEC', '50', kind='data', line=2439)

W('25,2602', 0o34741, 'STDESIG', 'CAF', 'REPOSBIT', line=2441)
W('25,2603', 0o70110, '', 'MASK', 'RADMODES', 'SEE IF GIMBAL LIMIT MONITOR HAS FOUND US', line=2442)
W('25,2604', 0o10000, '', 'CCS', 'A', 'OUT OF BOUNDS.  IF SO, THIS BIT SHOWS A', line=2443)
W('25,2605', 0o12623, '', 'TCF', 'BADDES', 'REPOSITION TO BE IN PROGRESS.', line=2444)

W('25,2606', 0o10110, '', 'CCS', 'RADMODES', 'SEE IF CONTINUOUS DESIGNATE WANTED.', line=2446)
W('25,2607', 0o12612, '', 'TCF', '+3', "IF SO, DON'T CHECK BIT 10 TO SEE IF IN", line=2447)
W('25,2610', 0o12612, '', 'TCF', '+2', 'LIMITS BUT GO RIGHT TO FINDVAC ENTRY.', line=2448)
W('25,2611', 0o12630, '', 'TCF', 'MOREDES +1', line=2449)

W('25,2612', 0o40110, '', 'CS', 'RADMODES', 'IF NON-CONTINUOUS, SEE IF END OF', line=2451)
W('25,2613', 0o74742, '', 'MASK', 'DESIGBIT', 'PROBLEM (DATA GOOD IF LOCK-ON WANTED OR', line=2452)
W('25,2614', 0o10000, '', 'CCS', 'A', 'WITHIN LIMITS IF NOT).  IF SO, EXIT AFTER', line=2453)
W('25,2615', 0o13546, '', 'TCF', 'ENDRADAR', 'CHECKING RR CDU FAIL.', line=2454)

W('25,2616', 0o11114, 'STDESIG1', 'CCS', 'DESCOUNT', 'SEE IF THE TIME LIMIT HAS EXPIRED', line=2456)
W('25,2617', 0o12627, '', 'TCF', 'MOREDES', line=2457)

W('25,2620', 0o42635, '', 'CS', 'B14+B2', 'IF OUT OF TIME, REMOVE ECR ENABLE + TRKR', line=2459)
W('25,2621', 0o00006, '', 'EXTEND', line=2460)
W('25,2622', 0o03012, '', 'WAND', 'CHAN12', line=2461)
W('25,2623', 0o44742, 'BADDES', 'CS', 'DESIGBIT', 'REMOVE DESIGNATE FLAG', line=2462)
W('25,2624', 0o70110, '', 'MASK', 'RADMODES', line=2463)
W('25,2625', 0o54110, '', 'TS', 'RADMODES', line=2464)
W('25,2626', 0o13562, '', 'TCF', 'RDBADEND', line=2465)

W('25,2627', 0o55114, 'MOREDES', 'TS', 'DESCOUNT', line=2467)
W('25,2630', 0o37714, '', 'CAF', 'PRIO26', 'UPDATE GYRO TORQUE COMMANDS.', line=2468)
W('25,2631', 0o05105, '', 'TC', 'FINDVAC', line=2469)
#   EBANK= LOSCOUNT
W('25,2632', 0o02636, '', '2CADR', 'DODES', kind='data', line=2471)
W('25,2633', 0o52067, kind='data', line=2471)

W('25,2634', 0o12600, '', 'TCF', 'DESLOOP', line=2473)

W('25,2635', 0o20002, 'B14+B2', 'OCT', '20002', kind='data', line=2475)

# Page 547
# PROGRAM NAME:  DODES
#
# FUNCTIONAL DESCRIPTION:
#
# DODES CALCULATES AND REQUESTS ISSUANCE OF RR GYRO TORQUE
# COMMANDS.  INITIALLY THE CURRENT RR CDU ANGLES ARE STORED AND
# THE LOS HALF-UNIT VECTOR TRANSFORMED FROM STABLE MEMBER TO
# NAVIGATION BASE COORDINATES VIA SMNB IF NECESSARY.  THE
# SHAFT AND TRUNNION COMMANDS ARE THEN CALCULATED AS FOLLOWS:
# + SHAFT = LOS . (COS(S), 0, -SIN(S))  (DOT PRODUCT)
# - TRUNNION = LOS . (SIN(T)SIN(S), COS(T), SIN(T)COS(S))
# THE SIGN OF THE SHAFT COMMAND IS THEN REVERSED IF IN MODE 2
# (RADMODES BIT 12) BECAUSE A RELAY IN THE RR REVERSES THE
# POLARITY OF THE COMMAND.  AT RRSCALUP EACH COMMAND IS
# SCALED AND IF EITHER, OR BOTH, OF THE COMMANDS IS GREATER THAN
# .5 DEGREES, MPAC +1 IS SET POSITIVE.  IF A CONTINUOUS DESIGNATE
# (RADMODES BIT 15) IS DESIRED AND THE SEARCH ROUTINE IS NOT OPERATING,
# THE RR AUTO TRACKER ENABLE BIT (CHAN 12 BIT 14) IS CLEARED AND RROUT
# CALLED TO PUT OUT THE COMMANDS PROVIDED NO REPOSITION (RADMODES BIT 11)
# IS IN PROGRESS.  IF A CONTINUOUS DESIGNATE AND THE SEARCH ROUTINE IS
# OPERATING (SRCHOPT FLAT SET) THE TRACK ENABLE IS NOT CLEARED.  IF NO
# CONTINUOUS DESIGNATE AND BOTH COMMANDS ARE NOT LESS THAN .5 DEGREES AS
# INDICATED BY MPAC +1, THE RR AUTO TRACKER ENABLE BIT (CHAN 12 BIT 14) IS
# CLEARED AND RROUT CALLED TO PUT OUT THE COMMANDS PROVIDED NO REPOSITON
# (RADMODES BIT 11) IS IN PROGRESS.  IF BOTH COMMANDS ARE LESS THAN .5
# DEGREES AS INDICATED BY MPAC+1, THE RR AUTO TRACKER ENABLE BIT
# (CHAN 12 BIT 14) IS CLEARED AND RROUT CALLED TO PUT OUT THE
# COMMANDS PROVIDED NO REPOSITION (RADMODES BIT 11) IS IN
# PROGRESS.  IF BOTH COMMANDS ARE LESS THAN .5 DEGREES, THE
# LOCK-ON FLAG (STATE BIT 5) IS CHECKED.  IF NOT PRESETN, THE
# DESIGNATE FLAG (RADMODES BIT 10) IS CLEARED, AND ENDOFJOB
# CALLED.  IF LOCK-ON IS DESIRED, THE RR AUTO TRACKER (CHAN 12
# BIT 14) IS ENABLED FOLLOWED BY A CHECK OF THE RECEIPT OF THE
# RR DATA GOOD (CHAN 33 BIT 4) SIGNAL.  IF RR DATA GOOD
# PRESENT, THE DESIGNATE FLAG (RADMODES BIT 10) IS CLEARED,
# THE RR ERROR COUNTER ENABLE BIT (CHAN 12 BIT 2) IS CLEARED,
# AND ENDOFJOB CALLED.  IF RR DATA GOOD IS NOT PRESENT, RROUT
# IS CALLED TO PUT OUT THE COMMANDS PROVIDED NO REPOSITION
# (RADMODES BIT 11) IS IN PROGRESS AFTER WHICH THE JOB IS TERMINATED
# VIA ENDOFJOB.
#
# CALLING SEQUENCE:
#
# EXECUTIVE CALL EVERY .5 SECONDS FROM BEGDES.
#
# ERASABLE INITIALIZATION REQUIRED:
#
# RRTARGET (HALF-UNIT LOS VECTOR IN EITHER SM OR NB COORDINATES),
# LOKONSW (STATE BIT 5), RRNBSW (STATE BIT 6), RADMODES
#
# SUBROUTINES CALLED:
#
# READCDUS, SMNB, CDULOGIC, MAGSUB, RROUT
# Page 548
#
# JOBS OR TASKS INITIATED:
#
# NONE
#
# ALARMS:  NONE
#
# EXIT:  ENDOFJOB (ALWAYS)

W('25,2636', 0o00006, 'DODES', 'EXTEND', line=2541)
W('25,2637', 0o30036, '', 'DCA', 'CDUT', line=2542)
W('25,2640', 0o53110, '', 'DXCH', 'TANG', line=2543)

W('25,2641', 0o06037, '', 'TC', 'INTPRET', line=2545)

W('25,2642', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=2547)
W('25,2643', 0o00001, '', '', '0', kind='operand', line=2548)
W('25,2644', 0o01102, '', '', 'RRTARGET', kind='operand', line=2549)
W('25,2645', 0o74214, '', 'BON', 'VXSC', kind='interp', line=2550)
W('25,2646', 0o00311, '', '', 'RRNBSW', kind='operand', line=2551)
W('25,2647', 0o52661, '', '', 'DONBRD', 'TARGET IN NAV-BASE COORDINATES', kind='operand', line=2552)
W('25,2650', 0o01767, '', '', 'MLOSV', 'MULTIPLY UNIT LOS BY MAGNITUDE', kind='operand', line=2553)
W('25,2651', 0o63372, '', 'VSL1', 'PDVL', kind='interp', line=2554)
W('25,2652', 0o01761, '', '', 'LOSVEL', kind='operand', line=2555)
W('25,2653', 0o53361, '', 'VXSC', 'VAD', 'ADD ONE SECOND RELATIVE VELOCITY TO LOS', kind='interp', line=2556)
W('25,2654', 0o13072, '', '', 'MCTOMS', kind='operand', line=2557)
W('25,2655', 0o45056, '', 'UNIT', 'CALL', kind='interp', line=2558)
W('25,2656', 0o47537, '', '', 'CDUTRIG', kind='operand', line=2559)
W('25,2657', 0o77624, '', 'CALL', kind='interp', line=2560)
W('25,2660', 0o47671, '', '', '*SMNB*', kind='operand', line=2561)

W('25,2661', 0o14041, 'DONBRD', 'STODL', '32D', kind='interp', line=2563)
W('25,2662', 0o01111, '', '', 'TANG +1', kind='operand', line=2564)
W('25,2663', 0o41434, '', 'RTB', 'PUSH', 'SHAFT COMMAND = V(32D).(COS(S), 0,', kind='interp', line=2565)
W('25,2664', 0o21576, '', '', 'CDULOGIC', '      -SIN(S)).', kind='operand', line=2566)
W('25,2665', 0o65356, '', 'SIN', 'PDDL', 'SIN(S) TO 0 AND COS(S) TO 2.', kind='interp', line=2567)
W('25,2666', 0o41546, '', 'COS', 'PUSH', kind='interp', line=2568)
W('25,2667', 0o65205, '', 'DMP', 'PDDL', kind='interp', line=2569)
W('25,2670', 0o00041, '', '', '32D', kind='operand', line=2570)
W('25,2671', 0o00045, '', '', '36D', kind='operand', line=2571)
W('25,2672', 0o44205, '', 'DMP', 'BDSU', kind='interp', line=2572)
W('25,2673', 0o00001, '', '', '0', kind='operand', line=2573)
W('25,2674', 0o77626, '', 'STADR', kind='interp', line=2574)
W('25,2675', 0o76666, '', 'STORE', 'TANG +1', 'SHAFT COMMAND', kind='interp', line=2575)

W('25,2676', 0o47135, '', 'SLOAD', 'RTB', kind='interp', line=2577)
W('25,2677', 0o01110, '', '', 'TANG', kind='operand', line=2578)
W('25,2700', 0o21576, '', '', 'CDULOGIC', kind='operand', line=2579)
W('25,2701', 0o71406, '', 'PUSH', 'COS', 'COS(T) TO 4.', kind='interp', line=2580)
W('25,2702', 0o73525, '', 'PDDL', 'SIN', kind='interp', line=2581)
W('25,2703', 0o41206, '', 'PUSH', 'DMP', 'SIN(T) TO 6.', kind='interp', line=2582)
W('25,2704', 0o00003, '', '', '2', kind='operand', line=2583)
# Page 549
W('25,2705', 0o65352, '', 'SL1', 'PDDL', 'DEFINE VECTOR U =     [SIN(T)SIN(S)]', kind='interp', line=2585)
W('25,2706', 0o00005, '', '', '4', '                      [   COS(T)   ]', kind='operand', line=2586)
W('25,2707', 0o41325, '', 'PDDL', 'DMP', '                      [SIN(T)COS(S)]', kind='interp', line=2587)
W('25,2710', 0o00007, '', '', '6', kind='operand', line=2588)
W('25,2711', 0o00001, '', '', '0', kind='operand', line=2589)
W('25,2712', 0o55552, '', 'SL1', 'VDEF', kind='interp', line=2590)
W('25,2713', 0o77441, '', 'DOT', 'EXIT', 'DOT U WITH LOS TO GET TRUNNION COMMAND.', kind='interp', line=2591)
W('25,2714', 0o00041, '', '', '32D', kind='operand', line=2592)

# Page 550
# AT THIS POINT WE HAVE A ROTATION VECTOR IN DISH AXES LYING IN THE TS PLANE.  CONVERT THIS TO A
# COMMANDED RATE AND ENABLE THE TRACKER IF WE ARE WITHIN .5 DEGREES OF THE TARGET.

W('25,2715', 0o40154, '', 'CS', 'MPAC', 'DOT WAS NEGATIVE OF DESREG ANGLE.', line=2598)
W('25,2716', 0o00006, '', 'EXTEND', line=2599)
W('25,2717', 0o73066, '', 'MP', 'RDESGAIN', 'SCALING ON INPUT ANGLE WAS 4 RADIANS.', line=2600)
W('25,2720', 0o55107, '', 'TS', 'TANG', 'TRUNNION COMMAND.', line=2601)
W('25,2721', 0o40110, '', 'CS', 'RADMODES', 'A RELAY IN THE RR REVERSES POLARITY OF', line=2602)
W('25,2722', 0o74740, '', 'MASK', 'BIT12', 'THE SHAFT COMMANDS IN MODE 2 SO THAT A', line=2603)
W('25,2723', 0o00006, '', 'EXTEND', '', 'POSITIVE TORQUE APPLIED TO THE SHAFT', line=2604)
W('25,2724', 0o12727, '', 'BZF', '+3', 'GYRO CAUSES A POSITIVE CHANGE IN THE', line=2605)
W('25,2725', 0o31110, '', 'CA', 'TANG +1', 'SHAFT ANGLE.  COMPENSATE FOR THIS SWITCH', line=2606)
W('25,2726', 0o12730, '', 'TCF', '+2', 'BY CHANGING THE POLARITY OF OUR COMMAND.', line=2607)
W('25,2727', 0o41110, '', 'CS', 'TANG +1', line=2608)
W('25,2730', 0o00006, '', 'EXTEND', line=2609)
W('25,2731', 0o73066, '', 'MP', 'RDESGAIN', 'SCALING ON INPUT ANGLE WAS 4 RADIANS.', line=2610)
W('25,2732', 0o55110, '', 'TS', 'TANG +1', 'SHAFT COMMAND FOR RROUT', line=2611)
W('25,2733', 0o06037, '', 'TC', 'INTPRET', line=2612)

W('25,2734', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=2614)
W('25,2735', 0o00003, '', '', '2', 'COS(S).', kind='operand', line=2615)
W('25,2736', 0o00005, '', '', '4', 'COS(T).', kind='operand', line=2616)
W('25,2737', 0o65352, '', 'SL1', 'PDDL', 'Z COMPONENT OF URR.', kind='interp', line=2617)
W('25,2740', 0o65276, '', 'DCOMP', 'PDDL', 'Y COMPONENT = -SIN(T)', kind='interp', line=2618)
W('25,2741', 0o00001, '', '', '0', 'SIN(S).', kind='operand', line=2619)
W('25,2742', 0o72405, '', 'DMP', 'SL1', kind='interp', line=2620)
W('25,2743', 0o00005, '', '', '4', 'COS(T).', kind='operand', line=2621)
W('25,2744', 0o43066, '', 'VDEF', 'BON', 'FORM URR IN NB AXES.', kind='interp', line=2622)
W('25,2745', 0o00311, '', '', 'RRNBSW', 'BYPASS NBSM CONVERSION IN VERB 41', kind='operand', line=2623)
W('25,2746', 0o52751, '', '', '+3', kind='operand', line=2624)
W('25,2747', 0o77624, '', 'CALL', kind='interp', line=2625)
W('25,2750', 0o47673, '', '', '*NBSM*', 'GET URR IN SM AXES.', kind='operand', line=2626)
W('25,2751', 0o77441, '', 'DOT', 'EXIT', kind='interp', line=2627)
W('25,2752', 0o01102, '', '', 'RRTARGET', 'GET COSIN OF ANGLE BETWEEN RR AND LOS', kind='operand', line=2628)

W('25,2753', 0o00006, '', 'EXTEND', line=2630)
W('25,2754', 0o43070, '', 'DCS', 'COS1/2DG', line=2631)
W('25,2755', 0o20155, '', 'DAS', 'MPAC', 'DIFFERENCE OF COSINES, SCALED B-2.', line=2632)
W('25,2756', 0o10154, '', 'CCS', 'MPAC', line=2633)
W('25,2757', 0o34755, '', 'CA', 'ZERO', 'IF COS ERROR BIGGER, ERROR IS SMALLER', line=2634)
W('25,2760', 0o12762, '', 'TCF', '+2', line=2635)
W('25,2761', 0o34753, '', 'CA', 'ONE', line=2636)
W('25,2762', 0o54155, '', 'TS', 'MPAC +1', 'ZERO IF RR IS POINTED OK, ONE IF NOT.', line=2637)
# Page 551
# SEE IF TRACKER SHOULD BE ENABLED OR DISABLED.

W('25,2763', 0o10110, '', 'CCS', 'RADMODES', 'IF CONTINUOUS DESIGNATE WANTED, PUT OUT', line=2641)
W('25,2764', 0o12767, '', 'TCF', 'SIGNLCHK', 'COMMANDS WITHOUT CHECKING MAGNITUDE OF', line=2642)
W('25,2765', 0o12767, '', 'TCF', 'SIGNLCHK', 'ERROR SIGNALS', line=2643)
W('25,2766', 0o13017, '', 'TCF', 'DORROUT', line=2644)
W('25,2767', 0o10155, 'SIGNLCHK', 'CCS', 'MPAC +1', 'SEE IF BOTH AXES WERE WITHIN .5 DEGS.', line=2645)
W('25,2770', 0o13000, '', 'TCF', 'DGOODCHK', line=2646)
W('25,2771', 0o40074, '', 'CS', 'STATE', 'IF WITHIN LIMITS AND NO LOCK-ON WANTED,', line=2647)
W('25,2772', 0o74747, '', 'MASK', 'LOKONBIT', 'PROBLEM IS FINISHED.', line=2648)
W('25,2773', 0o10000, '', 'CCS', 'A', line=2649)
W('25,2774', 0o13005, '', 'TCF', 'RRDESDUN', line=2650)

W('25,2775', 0o34736, '', 'CAF', 'BIT14', 'ENABLE THE TRACKER', line=2652)
W('25,2776', 0o00006, '', 'EXTEND', line=2653)
W('25,2777', 0o05012, '', 'WOR', 'CHAN12', line=2654)

W('25,3000', 0o34750, 'DGOODCHK', 'CAF', 'BIT4', 'SEE IF DATA GOOD RECEIVED YET', line=2656)
W('25,3001', 0o00006, '', 'EXTEND', line=2657)
W('25,3002', 0o02033, '', 'RAND', 'CHAN33', line=2658)
W('25,3003', 0o10000, '', 'CCS', 'A', line=2659)
W('25,3004', 0o13017, '', 'TCF', 'DORROUT', line=2660)

W('25,3005', 0o44742, 'RRDESDUN', 'CS', 'BIT10', 'WHEN PROBLEM DONE, REMOVE BIT 10 SO NEXT', line=2662)
W('25,3006', 0o70110, '', 'MASK', 'RADMODES', 'WAITLIST TASK WE WILL GO TO RGOODEND.', line=2663)
W('25,3007', 0o00004, '', 'INHINT', line=2664)
W('25,3010', 0o54110, '', 'TS', 'RADMODES', line=2665)

W('25,3011', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET LOSCMFLG TO PREENT A', line=2667)
W('25,3012', 0o00041, '', 'ADRES', 'LOSCMFLG', 'RECOMPUTATION OF LOS AFTER DATA GOOD', kind='data', line=2668)
W('25,3013', 0o44752, '', 'CS', 'BIT2', 'TURN OFF ENABLE RR ERROR COUNTER', line=2669)
W('25,3014', 0o00006, '', 'EXTEND', line=2670)
W('25,3015', 0o03012, '', 'WAND', 'CHAN12', line=2671)
W('25,3016', 0o15155, '', 'TCF', 'ENDOFJOB', 'WITH ECTR DISABLED.', line=2672)

W('25,3017', 0o30076, 'DORROUT', 'CA', 'FLAGWRD2', 'IF BOTH LOSCMFLAG AND SEARCH FLAG ARE', line=2674)
W('25,3020', 0o77712, '', 'MASK', 'BIT12,14', 'ZERO, BYPASS VELOCITY ADJUSTMENT TO LOS', line=2675)
W('25,3021', 0o00006, '', 'EXTEND', line=2676)
W('25,3022', 0o13041, '', 'BZF', 'NOTP20', line=2677)
W('25,3023', 0o06037, '', 'TC', 'INTPRET', line=2678)
W('25,3024', 0o74375, '', 'VLOAD', 'VXSC', 'MULTIPLY UNIT LOS BY MAGNITUDE', kind='interp', line=2679)
W('25,3025', 0o01102, '', '', 'RRTARGET', kind='operand', line=2680)
W('25,3026', 0o01767, '', '', 'MLOSV', kind='operand', line=2681)
W('25,3027', 0o41572, '', 'VSL1', 'PUSH', kind='interp', line=2682)
W('25,3030', 0o74375, '', 'VLOAD', 'VXSC', 'ADD .5 SEC. OF VELOCITY', kind='interp', line=2683)
W('25,3031', 0o01761, '', '', 'LOSVEL', 'TO LOS VECTOR', kind='operand', line=2684)
W('25,3032', 0o13072, '', '', 'MCTOMS', kind='operand', line=2685)
W('25,3033', 0o53362, '', 'VSR1', 'VAD', kind='interp', line=2686)
W('25,3034', 0o77656, '', 'UNIT', kind='interp', line=2687)
W('25,3035', 0o15102, '', 'STODL', 'RRTARGET', 'STORE VELOCITY-CORRECTED LOS (UNIT)', kind='interp', line=2688)
# Page 552
W('25,3036', 0o00045, '', '', '36D', kind='operand', line=2690)
W('25,3037', 0o01767, '', 'STORE', 'MLOSV', 'AND STORE MAGNITUDE', kind='interp', line=2691)
W('25,3040', 0o77776, '', 'EXIT', kind='interp', line=2692)
W('25,3041', 0o00004, 'NOTP20', 'INHINT', line=2693)
W('25,3042', 0o40110, '', 'CS', 'RADMODES', 'PUT OUT COMMAND UNLESS MONITOR', line=2694)
W('25,3043', 0o74741, '', 'MASK', 'REPOSBIT', 'REPOSITION HAS TAKEN OVER', line=2695)
W('25,3044', 0o10000, '', 'CCS', 'A', line=2696)
W('25,3045', 0o02306, '', 'TC', 'RROUT', line=2697)

W('25,3046', 0o30076, '', 'CA', 'FLAGWRD2', line=2699)
W('25,3047', 0o74740, '', 'MASK', 'LOSCMBIT', "IF LOSCMFLG NOT SET, DON'T TEST", line=2700)
W('25,3050', 0o00006, '', 'EXTEND', '', 'LOS COUNTER', line=2701)
W('25,3051', 0o15155, '', 'BZF', 'ENDOFJOB', line=2702)
W('25,3052', 0o11456, '', 'CCS', 'LOSCOUNT', 'TEST LOS COUNTER TO SEE IF TIME TO GET', line=2703)
W('25,3053', 0o03064, '', 'TC', 'DODESEND', 'A NEW LOS', line=2704)
W('25,3054', 0o00004, '', 'INHINT', line=2705)
W('25,3055', 0o06027, '', 'TC', 'KILLTASK', 'YES -- KILL TASK WHICH SCHEDULES DODES', line=2706)
W('25,3056', 0o52602, '', 'CADR', 'DESLOOP +2', kind='data', line=2707)
W('25,3057', 0o00003, '', 'RELINT', line=2708)
W('25,3060', 0o10067, '', 'CCS', 'NEWJOB', line=2709)
W('25,3061', 0o05122, '', 'TC', 'CHANG1', line=2710)
W('25,3062', 0o04616, '', 'TC', 'BANKCALL', line=2711)
W('25,3063', 0o50731, '', 'CADR', 'R21LEM2', kind='data', line=2712)

W('25,3064', 0o55456, 'DODESEND', 'TS', 'LOSCOUNT', line=2714)
W('25,3065', 0o05155, '', 'TC', 'ENDOFJOB', line=2715)

W('25,3066', 0o21122, 'RDESGAIN', 'DEC', '.53624', 'TRIES TO NULL .5 ERROR IN .5 SEC.', kind='data', line=2717)
S('BIT12,14', 'equals', 0o7712, line=2718)  # OCT 24000
W('25,3067', 0o07777, 'COS1/2DG', '2DEC', '.999961923 B-2', 'COSINE OF 0.5 DEGREES.', kind='data', line=2719)
W('25,3070', 0o33005, kind='data', line=2719)
W('25,3071', 0o00310, 'MCTOMS', '2DEC', '100 B-13', kind='data', line=2720)
W('25,3072', 0o00000, kind='data', line=2720)

# Page 553
# RADAR READ INITIALIZATION
#
# RADAR DATA READ BY A BANKCALL FOR THE APPROPRIATE LEAD-IN BELOW.

W('25,3073', 0o03113, 'LRALT', 'TC', 'INITREAD -1', 'ONE SAMPLE PER READING.', line=2727)
W('25,3074', 0o00017, 'ALLREAD', 'OCT', '17', kind='data', line=2728)

W('25,3075', 0o03114, 'LRVELZ', 'TC', 'INITREAD', line=2730)
W('25,3076', 0o00016, '', 'OCT', '16', kind='data', line=2731)

W('25,3077', 0o03114, 'LRVELY', 'TC', 'INITREAD', line=2733)
W('25,3100', 0o00015, '', 'OCT', '15', kind='data', line=2734)

W('25,3101', 0o03114, 'LRVELX', 'TC', 'INITREAD', line=2736)
W('25,3102', 0o00014, '', 'OCT', '14', kind='data', line=2737)

W('25,3103', 0o03113, 'RRRDOT', 'TC', 'INITREAD -1', line=2739)
W('25,3104', 0o00012, '', 'OCT', '12', kind='data', line=2740)

W('25,3105', 0o03113, 'RRRANGE', 'TC', 'INITREAD -1', line=2742)
W('25,3106', 0o00011, '', 'OCT', '11', kind='data', line=2743)

# LRVEL IS THE ENTRY TO THE LR VELOCITY READ ROUTINE WHEN 5 SAMPLES ARE
# WANTED.  ENTER WITH C(A)= 0,2,4 FOR LRVELZ,LRVELY,LRVELX RESP.

W('25,3107', 0o55105, 'LRVEL', 'TS', 'TIMEHOLD', 'STORE VBEAM INDEX HERE MOMENTARILY', line=2748)
W('25,3110', 0o34756, '', 'CAF', 'FIVE', 'SPECIFY FIVE SAMPLES', line=2749)
W('25,3111', 0o51105, '', 'INDEX', 'TIMEHOLD', line=2750)
W('25,3112', 0o13075, '', 'TCF', 'LRVELZ', line=2751)

# Page 554
W('25,3113', 0o34753, '', 'CAF', 'ONE', 'ENTRY TO TAKE ONLY 1 SAMPLE', line=2754)
W('25,3114', 0o00004, 'INITREAD', 'INHINT', line=2755)

W('25,3115', 0o55105, '', 'TS', 'TIMEHOLD', 'GET DT OF MIDPOINT OF NOMINAL SAMPLING', line=2757)
W('25,3116', 0o00006, '', 'EXTEND', '', 'INTERVAL (ASSUMES NO BAD SAMPLES WILL BE', line=2758)
W('25,3117', 0o74751, '', 'MP', 'BIT3', 'ENCOUNTERED).', line=2759)
W('25,3120', 0o53106, '', 'DXCH', 'TIMEHOLD', line=2760)

W('25,3121', 0o10000, '', 'CCS', 'A', line=2762)
W('25,3122', 0o55111, '', 'TS', 'NSAMP', line=2763)
W('25,3123', 0o64753, '', 'AD', 'ONE', line=2764)
# INSERT FOLLOWING INSTRUCTION TO GET 2N TRIES FOR N SAMPLES.
# DOUBLE
W('25,3124', 0o55100, '', 'TS', 'SAMPLIM', line=2767)

W('25,3125', 0o33147, '', 'CAF', 'DGBITS', 'READ CURRENT VALUE OF DATA GOOD BITS.', line=2769)
W('25,3126', 0o00006, '', 'EXTEND', line=2770)
W('25,3127', 0o02033, '', 'RAND', 'CHAN33', line=2771)
W('25,3130', 0o55113, '', 'TS', 'OLDATAGD', line=2772)

W('25,3131', 0o43074, '', 'CS', 'ALLREAD', line=2774)
W('25,3132', 0o00006, '', 'EXTEND', line=2775)
W('25,3133', 0o03013, '', 'WAND', 'CHAN13', 'REMOVE ALL RADAR BITS', line=2776)

W('25,3134', 0o50002, '', 'INDEX', 'Q', line=2778)
W('25,3135', 0o30000, '', 'CAF', '0', line=2779)
W('25,3136', 0o00006, '', 'EXTEND', line=2780)
W('25,3137', 0o05013, '', 'WOR', 'CHAN13', 'SET NEW RADAR BITS', line=2781)

W('25,3140', 0o00006, '', 'EXTEND', line=2783)
W('25,3141', 0o30025, '', 'DCA', 'TIME2', line=2784)
W('25,3142', 0o21106, '', 'DAS', 'TIMEHOLD', 'TIME OF NOMINAL MIDPOINT', line=2785)

W('25,3143', 0o34755, '', 'CAF', 'ZERO', line=2787)
W('25,3144', 0o54001, '', 'TS', 'L', line=2788)
W('25,3145', 0o53102, '', 'DXCH', 'SAMPLSUM', line=2789)
W('25,3146', 0o12366, '', 'TCF', 'ROADBACK', line=2790)

W('25,3147', 0o00230, 'DGBITS', 'OCT', '230', kind='data', line=2792)

# Page 555
# RADAR RUPT READER
#
# THIS ROUTINE STARTS FROM A RADARUPT.  IT READS THE DATA & LOTS MORE.

#   SETLOC RADARUPT
#   BANK

#   COUNT* $$/RRUPT
W('25,3150', 0o00006, 'RADAREAD', 'EXTEND', '', 'MUST SAVE SBANK BECAUSE OF RUPT EXITS', line=2803)
W('25,3151', 0o04007, '', 'ROR', 'SUPERBNK', 'VIA TASKOVER (BADEND OR GOODEND).', line=2804)
W('25,3152', 0o54016, '', 'TS', 'BANKRUPT', line=2805)
W('25,3153', 0o00006, '', 'EXTEND', line=2806)
W('25,3154', 0o22012, '', 'QXCH', 'QRUPT', line=2807)

W('25,3155', 0o34757, '', 'CAF', 'SEVEN', line=2809)
W('25,3156', 0o00006, '', 'EXTEND', line=2810)
W('25,3157', 0o02013, '', 'RAND', 'CHAN13', line=2811)
W('25,3160', 0o55335, '', 'TS', 'DNINDEX', line=2812)
W('25,3161', 0o00006, '', 'EXTEND', '', 'IF RADAR SELECT BITS ZERO, DO NOT STORE', line=2813)
W('25,3162', 0o13166, '', 'BZF', 'TRYCOUNT', 'DATA FOR DOWNLIST (ERASABLE PROBLEMS)', line=2814)
W('25,3163', 0o30046, '', 'CA', 'RNRAD', line=2815)
W('25,3164', 0o51335, '', 'INDEX', 'DNINDEX', line=2816)
W('25,3165', 0o55332, '', 'TS', 'DNRRANGE -1', line=2817)
W('25,3166', 0o11100, 'TRYCOUNT', 'CCS', 'SAMPLIM', line=2818)
W('25,3167', 0o13211, '', 'TCF', 'PLENTY', line=2819)
W('25,3170', 0o13174, '', 'TCF', 'NOMORE', line=2820)
W('25,3171', 0o05567, '', 'TC', 'ALARM', line=2821)
W('25,3172', 0o00520, '', 'OCT', '520', kind='data', line=2822)
W('25,3173', 0o05270, '', 'TC', 'RESUME', line=2823)

W('25,3174', 0o30107, 'NOMORE', 'CA', 'FLGWRD11', 'IS LRBYPASS SET?', line=2825)
W('25,3175', 0o74735, '', 'MASK', 'LRBYBIT', line=2826)
W('25,3176', 0o00006, '', 'EXTEND', line=2827)
W('25,3177', 0o13206, '', 'BZF', 'BADRAD', 'NO.  R12 IS ON -- BYPASS 521 ALARM.', line=2828)

W('25,3200', 0o40077, '', 'CS', 'FLAGWRD3', 'CHECK R04FLAG.', line=2830)
W('25,3201', 0o74743, '', 'MASK', 'R04FLBIT', 'IF 1, R04 IS RUNNING.  DO NOT ALARM', line=2831)
W('25,3202', 0o00006, '', 'EXTEND', line=2832)
W('25,3203', 0o13206, '', 'BZF', 'BADRAD', line=2833)

W('25,3204', 0o05567, '', 'TC', 'ALARM', 'P20 WANTS THE ALARM.', line=2835)
W('25,3205', 0o00521, '', 'OCT', '521', kind='data', line=2836)
W('25,3206', 0o44753, 'BADRAD', 'CS', 'ONE', line=2837)
W('25,3207', 0o55100, '', 'TS', 'SAMPLIM', line=2838)
W('25,3210', 0o03560, '', 'TC', 'RDBADEND -2', line=2839)
W('25,3211', 0o55100, 'PLENTY', 'TS', 'SAMPLIM', line=2840)
W('25,3212', 0o34751, '', 'CAF', 'BIT3', line=2841)
W('25,3213', 0o00006, '', 'EXTEND', line=2842)
W('25,3214', 0o02013, '', 'RAND', 'CHAN13', 'TO FIND OUT WHICH RADAR', line=2843)
W('25,3215', 0o00006, '', 'EXTEND', line=2844)
# Page 556
W('25,3216', 0o13276, '', 'BZF', 'RENDRAD', line=2846)

W('25,3217', 0o03364, '', 'TC', 'R77CHECK', 'R77 QUITS HERE.', line=2848)
W('25,3220', 0o30110, 'LRPOSCHK', 'CA', 'RADMODES', 'SEE IF LR IN DESIRED POSITION', line=2849)
W('25,3221', 0o00006, '', 'EXTEND', line=2850)
W('25,3222', 0o06033, '', 'RXOR', 'CHAN33', line=2851)
W('25,3223', 0o74746, '', 'MASK', 'BIT6', line=2852)
W('25,3224', 0o00006, '', 'EXTEND', line=2853)
W('25,3225', 0o13231, '', 'BZF', 'VELCHK', line=2854)

W('25,3226', 0o05567, '', 'TC', 'ALARM', line=2856)
W('25,3227', 0o00522, '', 'OCT', '522', kind='data', line=2857)
W('25,3230', 0o03206, '', 'TC', 'BADRAD', line=2858)

W('25,3231', 0o36245, 'VELCHK', 'CAF', 'BIN3', '= 00003 OCT', line=2860)
W('25,3232', 0o00006, '', 'EXTEND', line=2861)
W('25,3233', 0o06013, '', 'RXOR', 'CHAN13', 'RESET ACTIVITY BIT', line=2862)
W('25,3234', 0o76245, '', 'MASK', 'BIN3', line=2863)
W('25,3235', 0o00006, '', 'EXTEND', line=2864)
W('25,3236', 0o13272, '', 'BZF', 'LRHEIGHT', 'TAKE A LR RANGE READING', line=2865)

W('25,3237', 0o34733, '', 'CAF', 'POSMAX', line=2867)
W('25,3240', 0o70046, '', 'MASK', 'RNRAD', line=2868)
W('25,3241', 0o62000, '', 'AD', 'LVELBIAS', line=2869)
W('25,3242', 0o54001, '', 'TS', 'L', line=2870)
W('25,3243', 0o30046, '', 'CAE', 'RNRAD', line=2871)
W('25,3244', 0o60000, '', 'DOUBLE', line=2872)
W('25,3245', 0o74753, '', 'MASK', 'BIT1', line=2873)
W('25,3246', 0o52064, '', 'DXCH', 'ITEMP3', line=2874)

W('25,3247', 0o34744, '', 'CAF', 'BIT8', "DATA GOOD ISN'T CHECKED UNTIL AFTER READ-", line=2876)
W('25,3250', 0o03442, '', 'TC', 'DGCHECK', 'ING DATA SO SOME RADAR TESTS WILL WORK', line=2877)
# INDEPENDENT OF DATA GOOD.

W('25,3251', 0o11111, '', 'CCS', 'NSAMP', line=2880)
W('25,3252', 0o03262, '', 'TC', 'NOEND', line=2881)
W('25,3253', 0o44753, 'GOODRAD', 'CS', 'ONE', line=2882)
W('25,3254', 0o55100, '', 'TS', 'SAMPLIM', line=2883)
W('25,3255', 0o40061, '', 'CS', 'ITEMP1', 'WHEN ENOUGH GOOD DATA HAS BEEN GATHERED,', line=2884)
W('25,3256', 0o70110, '', 'MASK', 'RADMODES', 'RESET DATA FAIL FLAGS FOR SETTRKF.', line=2885)
W('25,3257', 0o54110, '', 'TS', 'RADMODES', line=2886)
W('25,3260', 0o03616, '', 'TC', 'RADLITES', 'LAMPS MAY GO OFF IF DATA JUST GOOD.', line=2887)
W('25,3261', 0o03553, '', 'TC', 'RGOODEND -2', line=2888)

W('25,3262', 0o55111, 'NOEND', 'TS', 'NSAMP', line=2890)
W('25,3263', 0o11100, 'RESAMPLE', 'CCS', 'SAMPLIM', 'SEE IF ANY MORE TRIES SHOULD BE MADE.', line=2891)
W('25,3264', 0o13266, '', 'TCF', '+2', line=2892)
W('25,3265', 0o13461, '', 'TCF', 'DATAFAIL', 'N SAMPLES NOT AVAILABLE.', line=2893)
W('25,3266', 0o34750, '', 'CAF', 'BIT4', 'RESET ACTIVITY BIT.', line=2894)
W('25,3267', 0o00006, '', 'EXTEND', line=2895)
# Page 557
W('25,3270', 0o05013, '', 'WOR', 'CHAN13', 'RESET ACTIVITY BIT', line=2897)
W('25,3271', 0o05270, '', 'TC', 'RESUME', line=2898)

W('25,3272', 0o34747, 'LRHEIGHT', 'CAF', 'BIT5', line=2901)
W('25,3273', 0o54061, '', 'TS', 'ITEMP1', '(POSITION OF DATA GOOD BIT IN CHAN 33)', line=2902)

W('25,3274', 0o34743, '', 'CAF', 'BIT9', line=2904)
W('25,3275', 0o03320, '', 'TC', 'SCALECHK -1', line=2905)

W('25,3276', 0o34741, 'RENDRAD', 'CAF', 'REPOSBIT', 'MAKE SURE ANTENNA HAS NOT GONE OUT OF', line=2907)
W('25,3277', 0o70110, '', 'MASK', 'RADMODES', 'LIMITS.', line=2908)
W('25,3300', 0o10000, '', 'CCS', 'A', line=2909)
W('25,3301', 0o13206, '', 'TCF', 'BADRAD', line=2910)

W('25,3302', 0o40110, '', 'CS', 'RADMODES', "BE SURE RR CDU HASN'T FAILED.", line=2912)
W('25,3303', 0o74745, '', 'MASK', 'RCDUFBIT', line=2913)
W('25,3304', 0o10000, '', 'CCS', 'A', line=2914)
W('25,3305', 0o13206, '', 'TCF', 'BADRAD', line=2915)

W('25,3306', 0o34750, '', 'CAF', 'BIT4', 'SEE IF DATA HAS BEEN GOOD.', line=2917)
W('25,3307', 0o54061, '', 'TS', 'ITEMP1', '(POSITION OF DATA GOOD BIT IN CHAN 33)', line=2918)

W('25,3310', 0o34753, '', 'CAF', 'BIT1', 'SEE IF RR RDOT.', line=2920)
W('25,3311', 0o00006, '', 'EXTEND', line=2921)
W('25,3312', 0o02013, '', 'RAND', 'CHAN13', line=2922)
W('25,3313', 0o54002, '', 'TS', 'Q', 'FOR LATER TESTING.', line=2923)
W('25,3314', 0o10000, '', 'CCS', 'A', line=2924)
W('25,3315', 0o13317, '', 'TCF', '+2', line=2925)
W('25,3316', 0o13331, '', 'TCF', 'RADIN', 'NO SCALE CHECK FOR RR RDOT.', line=2926)
W('25,3317', 0o34751, '', 'CAF', 'BIT3', line=2927)
W('25,3320', 0o54001, '', 'TS', 'L', line=2928)

W('25,3321', 0o00006, 'SCALECHK', 'EXTEND', line=2930)
W('25,3322', 0o02033, '', 'RAND', 'CHAN33', 'SCALE STATUS NOW', line=2931)
W('25,3323', 0o56001, '', 'XCH', 'L', line=2932)
W('25,3324', 0o70110, '', 'MASK', 'RADMODES', 'SCALE STATUS BEFORE', line=2933)
W('25,3325', 0o00006, '', 'EXTEND', line=2934)
W('25,3326', 0o06001, '', 'RXOR', 'LCHAN', 'SEE IF THEY DIFFER', line=2935)
W('25,3327', 0o10000, '', 'CCS', 'A', line=2936)
W('25,3330', 0o03350, '', 'TC', 'SCALCHNG', 'THEY DIFFER.', line=2937)

W('25,3331', 0o34733, 'RADIN', 'CAF', 'POSMAX', line=2939)
W('25,3332', 0o70046, '', 'MASK', 'RNRAD', line=2940)
W('25,3333', 0o54064, '', 'TS', 'ITEMP4', line=2941)

W('25,3334', 0o30046, '', 'CAE', 'RNRAD', line=2943)
W('25,3335', 0o60000, '', 'DOUBLE', line=2944)
W('25,3336', 0o74753, '', 'MASK', 'BIT1', line=2945)
W('25,3337', 0o54063, '', 'TS', 'ITEMP3', line=2946)
# Page 558
W('25,3340', 0o10002, '', 'CCS', 'Q', 'SEE IF RR RDOT.', line=2948)
W('25,3341', 0o13402, '', 'TCF', 'SCALADJ', 'NO, BUT SCALE CHANGING MAY BE NEEDED.', line=2949)

W('25,3342', 0o00006, '', 'EXTEND', '', 'IF RR RANGE RATE, THROW OUT BIAS', line=2951)
W('25,3343', 0o42002, '', 'DCS', 'RDOTBIAS', line=2952)
W('25,3344', 0o20064, 'DASAMPL', 'DAS', 'ITEMP3', line=2953)
W('25,3345', 0o30061, 'DGCHECK2', 'CA', 'ITEMP1', 'SEE THAT DATA HAS BEEN GOOD BEFORE AND', line=2954)
W('25,3346', 0o03443, '', 'TC', 'DGCHECK +1', 'AFTER TAKING SAMPLE.', line=2955)
W('25,3347', 0o03253, '', 'TC', 'GOODRAD', line=2956)

W('25,3350', 0o22110, 'SCALCHNG', 'LXCH', 'RADMODES', line=2958)
W('25,3351', 0o64753, '', 'AD', 'BIT1', line=2959)
W('25,3352', 0o00006, '', 'EXTEND', line=2960)
W('25,3353', 0o06001, '', 'RXOR', 'LCHAN', line=2961)
W('25,3354', 0o54110, '', 'TS', 'RADMODES', line=2962)
W('25,3355', 0o33147, '', 'CAF', 'DGBITS', 'UPDATE LAST VALUE OF DATA GOOD BITS.', line=2963)
W('25,3356', 0o00006, '', 'EXTEND', line=2964)
W('25,3357', 0o02033, '', 'RAND', 'CHAN33', line=2965)
W('25,3360', 0o55113, '', 'TS', 'OLDATAGD', line=2966)
W('25,3361', 0o05504, '', 'TC', 'UPFLAG', 'SET RNGSCFLG', line=2967)
W('25,3362', 0o00120, '', 'ADRES', 'RNGSCFLG', 'FOR LRS24.1', kind='data', line=2968)
W('25,3363', 0o13206, '', 'TCF', 'BADRAD', line=2969)

# R77 MUST IGNORE DATA FAILS SO AS NOT TO DISTURB THE ASTRONAUT.

W('25,3364', 0o40101, 'R77CHECK', 'CS', 'FLAGWRD5', line=2973)
W('25,3365', 0o74741, '', 'MASK', 'R77FLBIT', line=2974)
W('25,3366', 0o10000, '', 'CCS', 'A', line=2975)
W('25,3367', 0o00002, '', 'TC', 'Q', 'NOT R77', line=2976)
W('25,3370', 0o43401, '', 'CS', 'BITS5,8', 'UPDATE LR DATA GOOD BITS IN RADMODES', line=2977)
W('25,3371', 0o70110, '', 'MASK', 'RADMODES', line=2978)
W('25,3372', 0o54001, '', 'TS', 'L', line=2979)
W('25,3373', 0o33401, '', 'CA', 'BITS5,8', line=2980)
W('25,3374', 0o00006, '', 'EXTEND', line=2981)
W('25,3375', 0o02033, '', 'RAND', 'CHAN33', line=2982)
W('25,3376', 0o60001, '', 'AD', 'L', line=2983)
W('25,3377', 0o54110, '', 'TS', 'RADMODES', line=2984)
W('25,3400', 0o03553, '', 'TC', 'RGOODEND -2', line=2985)
W('25,3401', 0o00220, 'BITS5,8', 'OCT', '220', kind='data', line=2986)

# Page 559
# THE FOLLOWING ROUTINE INCORPORATES RR RANGE AND LR ALT SCALE INFORMATION AND LEAVES DATA AT LO SCALE.

W('25,3402', 0o10001, 'SCALADJ', 'CCS', 'L', 'L HAS SCALE INBIT FOR THIS RADAR.', line=2991)
W('25,3403', 0o13405, '', 'TCF', '+2', 'ON HIGH SCALE.', line=2992)
W('25,3404', 0o13345, '', 'TCF', 'DGCHECK2', line=2993)

W('25,3405', 0o31335, '', 'CA', 'DNINDEX', line=2995)
W('25,3406', 0o74751, '', 'MASK', 'BIT3', line=2996)
W('25,3407', 0o10000, '', 'CCS', 'A', line=2997)
W('25,3410', 0o13417, '', 'TCF', 'LRSCK', line=2998)

W('25,3411', 0o52064, '', 'DXCH', 'ITEMP3', line=3000)
W('25,3412', 0o20001, '', 'DDOUBL', line=3001)
W('25,3413', 0o20001, '', 'DDOUBL', line=3002)
W('25,3414', 0o20001, '', 'DDOUBL', line=3003)
W('25,3415', 0o52064, '', 'DXCH', 'ITEMP3', line=3004)

W('25,3416', 0o13345, '', 'TCF', 'DGCHECK2', line=3006)

W('25,3417', 0o10063, 'LRSCK', 'CCS', 'ITEMP3', line=3008)
W('25,3420', 0o13431, '', 'TCF', '+11', line=3009)
W('25,3421', 0o40064, '', 'CS', 'ITEMP4', line=3010)
W('25,3422', 0o63441, '', 'AD', 'HISCALIM', line=3011)
W('25,3423', 0o00006, '', 'EXTEND', line=3012)
W('25,3424', 0o63431, '', 'BZMF', '+5', line=3013)

W('25,3425', 0o40107, '', 'CS', 'FLGWRD11', line=3015)
W('25,3426', 0o74751, '', 'MASK', 'SCABBIT', line=3016)
W('25,3427', 0o26107, '', 'ADS', 'FLGWRD11', line=3017)
W('25,3430', 0o13434, '', 'TCF', '+4', line=3018)

W('25,3431', 0o44751, '', 'CS', 'SCABBIT', line=3020)
W('25,3432', 0o70107, '', 'MASK', 'FLGWRD11', line=3021)
W('25,3433', 0o54107, '', 'TS', 'FLGWRD11', line=3022)

W('25,3434', 0o00006, '', 'EXTEND', line=3024)
W('25,3435', 0o30064, '', 'DCA', 'ITEMP3', line=3025)
W('25,3436', 0o20001, '', 'DDOUBL', line=3026)
W('25,3437', 0o20001, '', 'DDOUBL', line=3027)
W('25,3440', 0o13344, '', 'TCF', 'DASAMPL', line=3028)

W('25,3441', 0o00714, 'HISCALIM', 'DEC', '460', '2481.7 FT ******************************', kind='data', line=3030)
# Page 560
W('25,3442', 0o54061, 'DGCHECK', 'TS', 'ITEMP1', 'UPDATE DATA GOOD BIT IN OLDATAGD AND', line=3032)
W('25,3443', 0o00006, '', 'EXTEND', '', 'MAKE SURE IT WAS ON BEFORE AND AFTER THE', line=3033)
W('25,3444', 0o02033, '', 'RAND', 'CHAN33', 'SAMPLE WAS TAKEN BEFORE RETURNING.  IF', line=3034)
W('25,3445', 0o54001, '', 'TS', 'L', 'NOT, GOES TO RESAMPLE TO TRY AGAIN.  IF', line=3035)
W('25,3446', 0o40061, '', 'CS', 'ITEMP1', 'MAX NUMBER OF TRIES HAS BEEN REACHED,', line=3036)
W('25,3447', 0o71113, '', 'MASK', 'OLDATAGD', 'THE BIT CORRESPONDING TO THE DATA GOOD', line=3037)
W('25,3450', 0o60001, '', 'AD', 'L', 'WHICH FAILED TO APPEAR IS IN ITEMP1 AND', line=3038)
W('25,3451', 0o57113, '', 'XCH', 'OLDATAGD', 'CAN BE USED TO SET RADMODES WHICH VIA', line=3039)
W('25,3452', 0o70061, '', 'MASK', 'ITEMP1', 'SETTRKF SETS THE TRACKER FAIL LAMP.', line=3040)
W('25,3453', 0o60001, '', 'AD', 'L', line=3041)
W('25,3454', 0o10000, '', 'CCS', 'A', 'SHOULD BOTH BE ZERO.', line=3042)
W('25,3455', 0o03263, '', 'TC', 'RESAMPLE', line=3043)
W('25,3456', 0o52064, '', 'DXCH', 'ITEMP3', 'IF DATA GOOD BEFORE AND AFTER, ADD TO', line=3044)
W('25,3457', 0o21102, '', 'DAS', 'SAMPLSUM', 'ACCUMULATION.', line=3045)
W('25,3460', 0o00002, '', 'TC', 'Q', line=3046)

W('25,3461', 0o40061, 'DATAFAIL', 'CS', 'ITEMP1', 'IN THE ABOVE CASE, SET RADMODES BIT', line=3048)
W('25,3462', 0o70110, '', 'MASK', 'RADMODES', 'SHOWING SOME RADAR DATA FAILED.', line=3049)
W('25,3463', 0o60061, '', 'AD', 'ITEMP1', line=3050)
W('25,3464', 0o54110, '', 'TS', 'RADMODES', line=3051)

W('25,3465', 0o52064, '', 'DXCH', 'ITEMP3', 'IF WE HAVE BEEN UNABLE TO GATHER N', line=3053)
W('25,3466', 0o53102, '', 'DXCH', 'SAMPLSUM', 'SAMPLES, USE LAST ONE ONLY.', line=3054)
W('25,3467', 0o03616, '', 'TC', 'RADLITES', line=3055)
W('25,3470', 0o13174, '', 'TCF', 'NOMORE', line=3056)
# Page 561
# THIS ROUTINE CHANGES THE LR POSITION, AND CHECKS THAT IT GOT THERE.

#   SETLOC P20S1
#   BANK

#   COUNT* $$/RSUB
W('25,3471', 0o00004, 'LRPOS2', 'INHINT', line=3064)

W('25,3472', 0o40110, '', 'CS', 'RADMODES', line=3066)
W('25,3473', 0o74746, '', 'MASK', 'LRPOSBIT', 'SHOW DESIRED LR POSITION IS 2', line=3067)
W('25,3474', 0o26110, '', 'ADS', 'RADMODES', line=3068)

W('25,3475', 0o34745, '', 'CAF', 'BIT7', line=3070)
W('25,3476', 0o00006, '', 'EXTEND', line=3071)
W('25,3477', 0o02033, '', 'RAND', 'CHAN33', 'SEE IF ALREADY THERE.', line=3072)
W('25,3500', 0o00006, '', 'EXTEND', line=3073)
W('25,3501', 0o13530, '', 'BZF', 'RADNOOP', line=3074)

W('25,3502', 0o34737, '', 'CAF', 'BIT13', line=3076)
W('25,3503', 0o00006, '', 'EXTEND', line=3077)
W('25,3504', 0o05012, '', 'WOR', 'CHAN12', 'COMMAND TO POSITION 2', line=3078)
W('25,3505', 0o33545, '', 'CAF', '6SECS', 'START SCANNING FOR INBIT AFTER 7 SECS.', line=3079)
W('25,3506', 0o05203, '', 'TC', 'WAITLIST', line=3080)
#   EBANK= LOSCOUNT
W('25,3507', 0o03543, '', '2CADR', 'LRPOSCAN', kind='data', line=3082)
W('25,3510', 0o52067, kind='data', line=3082)

W('25,3511', 0o02366, '', 'TC', 'ROADBACK', line=3084)

W('25,3512', 0o55100, 'LRPOSNXT', 'TS', 'SAMPLIM', line=3086)
W('25,3513', 0o05221, '', 'TC', 'FIXDELAY', 'SCAN ONCE PER SECOND 15 TIMES MAX AFTER', line=3087)
W('25,3514', 0o00144, '', 'DEC', '100', 'INITIAL DELAY OF 7 SECONDS.', kind='data', line=3088)

W('25,3515', 0o34745, '', 'CAF', 'BIT7', 'SEE IF LR POS2 IS ON', line=3090)
W('25,3516', 0o00006, '', 'EXTEND', line=3091)
W('25,3517', 0o02033, '', 'RAND', 'CHAN33', line=3092)
W('25,3520', 0o00006, '', 'EXTEND', line=3093)
W('25,3521', 0o13535, '', 'BZF', 'LASTLRDT', 'IF THERE, WAIT FINAL SECOND FOR BOUNCE.', line=3094)

W('25,3522', 0o11100, '', 'CCS', 'SAMPLIM', 'SEE IF MAX TIME UP.', line=3096)
W('25,3523', 0o13512, '', 'TCF', 'LRPOSNXT', line=3097)

W('25,3524', 0o44737, '', 'CS', 'BIT13', 'IF TIME UP, DISABLE COMMAND AND ALARM.', line=3099)
W('25,3525', 0o00006, '', 'EXTEND', line=3100)
W('25,3526', 0o03012, '', 'WAND', 'CHAN12', line=3101)
W('25,3527', 0o13562, '', 'TCF', 'RDBADEND', line=3102)

W('25,3530', 0o34753, 'RADNOOP', 'CAF', 'ONE', 'NO FURTHER ACTION REQUESTED.', line=3104)
W('25,3531', 0o05203, '', 'TC', 'WAITLIST', line=3105)
#   EBANK= LOSCOUNT
W('25,3532', 0o03555, '', '2CADR', 'RGOODEND', kind='data', line=3107)
W('25,3533', 0o52067, kind='data', line=3107)
# Page 562
W('25,3534', 0o02366, '', 'TC', 'ROADBACK', line=3109)

W('25,3535', 0o35000, 'LASTLRDT', 'CA', '2SECS', 'WAIT TWO SECONDS AFTER RECEIPT OF INBIT', line=3111)
W('25,3536', 0o05224, '', 'TC', 'VARDELAY', 'TO WAIT FOR ANTENNA BOUNCE TO DIE OUT.', line=3112)

W('25,3537', 0o44737, '', 'CS', 'BIT13', 'REMOVE COMMAND', line=3114)
W('25,3540', 0o00006, '', 'EXTEND', line=3115)
W('25,3541', 0o03012, '', 'WAND', 'CHAN12', line=3116)
W('25,3542', 0o13555, '', 'TCF', 'RGOODEND', line=3117)

W('25,3543', 0o34317, 'LRPOSCAN', 'CAF', 'FOURTEEN', 'SET UP FOR 15 SAMPLES.', line=3119)
W('25,3544', 0o13512, '', 'TCF', 'LRPOSNXT', line=3120)
W('25,3545', 0o01130, '6SECS', 'DEC', '600', kind='data', line=3121)
# Page 563
# SEQUENCES TO TERMINATE RR OPERATIONS.

W('25,3546', 0o34745, 'ENDRADAR', 'CAF', 'RCDUFBIT', 'PROLOG TO CHECK RR CDU FAIL BEFORE END.', line=3125)
W('25,3547', 0o70110, '', 'MASK', 'RADMODES', line=3126)
W('25,3550', 0o10000, '', 'CCS', 'A', line=3127)
W('25,3551', 0o13555, '', 'TCF', 'RGOODEND', line=3128)
W('25,3552', 0o13562, '', 'TCF', 'RDBADEND', line=3129)
W('25,3553', 0o44755, '', 'CS', 'ZERO', 'RGOODEND WHEN NOT UNDER WAITLIST CONTROL', line=3130)
W('25,3554', 0o54734, '', 'TS', 'RUPTAGN', line=3131)

W('25,3555', 0o34752, 'RGOODEND', 'CAF', 'TWO', line=3133)
W('25,3556', 0o04635, '', 'TC', 'POSTJUMP', line=3134)
W('25,3557', 0o17665, '', 'CADR', 'GOODEND', kind='data', line=3135)

W('25,3560', 0o44755, '', 'CS', 'ZERO', 'RDBADEND WHEN NOT UNDER WIATLIST.', line=3137)
W('25,3561', 0o54734, '', 'TS', 'RUPTAGN', line=3138)
W('25,3562', 0o34752, 'RDBADEND', 'CAF', 'TWO', line=3139)
W('25,3563', 0o04635, '', 'TC', 'POSTJUMP', line=3140)
W('25,3564', 0o17662, '', 'CADR', 'BADEND', kind='data', line=3141)

S('BIN3', 'equals', 0o6245, line=3143)

# Page 564
# PROGRAM NAME:  LPS20.1 VECTOR EXTRAPOLATION AND LOS COMPUTATION
# MOD. NO. 2    BY J.D. COYNE   SDC     DATE 12-7-66
#
# FUNCTIONAL DESCRPIPTION:
# 1)      EXTRAPOLATE THE LEM AND CSM VECTORS IN ACCORDANCE WITH THE TIME REFERRED TO IN CALLER + 1.
# 2)      COMPUTES THE LOS VECTOR TO THE CSM, CONVERTS IT TO STABLE MEMBER COORDINATES AND STORES IT IN RRTARGET.
# 3)      COMPUTES THE MAGNITUDE OF TEH LOS VECTOR AND STORES IT IN MLOSV
#
# CALLING SEQUENCE:     CALL
# LPS20.1
#
# SUBROUTINES CALLED:
# LEMPREC, CSMPREC
#
# NORMAL EXIT:  RETURN TO CALLER + 2.
#
# ERROR EXITS:  NONE
#
# ALARMS:  NONE
#
# OUTPUT:
# LOS VECTOR (HALF UNIT) IN SM COORDINATES STORED IN RRTARGET
# MAGNITUDE OF TEH LOS VECTOR (METERS SCALED B-29) STORED IN MSLOV
# RRNBSW CLEARED.
#
# INITIALIZED ERASABLE
# TDEC1 MUST CONTAIN THE TIME FOR EXTRAPOLATION
# SEE ORBITAL INTEGRATION ROUTINE
#
# DEBRIS:
# MPAC DESTROYED BY THE ROUTINE

#   BANK 23
#   SETLOC P20S
#   BANK
# Page 565
#   COUNT* $$/LPS20

W('24,3255', 0o43020, 'LPS20.1', 'STQ', 'BOFF', kind='interp', line=3184)
W('24,3256', 0o01757, '', '', 'LS21X', kind='operand', line=3185)
W('24,3257', 0o01343, '', '', 'LOSCMFLG', 'LOSCMFLG = 0 MEANS NOT CALLED BY R21', kind='operand', line=3186)
W('24,3260', 0o51264, '', '', 'LMINT', 'SO CALL LEMCONIC TO GET LM STATE', kind='operand', line=3187)
W('24,3261', 0o77614, '', 'BON', '', 'IF IN R21 AND ON LUNAR SURFACE', kind='interp', line=3188)
W('24,3262', 0o04307, '', '', 'SURFFLAG', "DON'T CALL LEMCONIC", kind='operand', line=3189)
W('24,3263', 0o51274, '', '', 'CSMINT', kind='operand', line=3190)
W('24,3264', 0o77624, 'LMINT', 'CALL', kind='interp', line=3191)
W('24,3265', 0o27100, '', '', 'LEMCONIC', 'EXTRAPOLATE LEM', kind='operand', line=3192)
W('24,3266', 0o77775, '', 'VLOAD', kind='interp', line=3193)
W('24,3267', 0o00001, '', '', 'RATT', kind='operand', line=3194)
W('24,3270', 0o26352, '', 'STOVL', 'LMPOS', 'SAVE LM POSITION B-29', kind='interp', line=3195)
W('24,3271', 0o00007, '', '', 'VATT', kind='operand', line=3196)
W('24,3272', 0o16360, '', 'STODL', 'LMVEL', 'SAVE LM VELOCITY B-7', kind='interp', line=3197)
W('24,3273', 0o00015, '', '', 'TAT', kind='operand', line=3198)
W('24,3274', 0o34041, 'CSMINT', 'STCALL', 'TDEC1', kind='interp', line=3199)
W('24,3275', 0o27066, '', '', 'CSMCONIC', 'EXTRAPOLATE CSM', kind='operand', line=3200)
W('24,3276', 0o52375, '', 'VLOAD', 'VSU', 'COMPUTE RELATIVE VELOCITY V(CSM) - V(LM)', kind='interp', line=3201)
W('24,3277', 0o00007, '', '', 'VATT', kind='operand', line=3202)
W('24,3300', 0o02360, '', '', 'LMVEL', kind='operand', line=3203)
W('24,3301', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=3204)
W('24,3302', 0o01734, '', '', 'REFSMMAT', kind='operand', line=3205)
W('24,3303', 0o77776, '', 'EXIT', kind='interp', line=3206)
W('24,3304', 0o06027, '', 'TC', 'KILLTASK', 'KILL THE TASK WHICH CALLS DODES SINCE', line=3207)
W('24,3305', 0o52602, '', 'CADR', 'DESLOOP +2', 'STORING INTO ERASEABLES DODES USES', kind='data', line=3208)
W('24,3306', 0o06037, '', 'TC', 'INTPRET', line=3209)
W('24,3307', 0o25761, '', 'STOVL', 'LOSVEL', kind='interp', line=3210)
W('24,3310', 0o00001, '', '', 'RATT', kind='operand', line=3211)
W('24,3311', 0o43051, '', 'VSU', 'BOFF', kind='interp', line=3212)
W('24,3312', 0o02352, '', '', 'LMPOS', kind='operand', line=3213)
W('24,3313', 0o00350, '', '', 'RNDVZFLG', kind='operand', line=3214)
W('24,3314', 0o51321, '', '', 'NOTSHIFT', kind='operand', line=3215)
W('24,3315', 0o77604, '', 'BOVB', kind='interp', line=3216)
W('24,3316', 0o57753, '', '', 'TCDANZIG', kind='operand', line=3217)
W('24,3317', 0o77661, '', 'VSL', kind='interp', line=3218)
W('24,3320', 0o20212, '', '', '9D', kind='operand', line=3219)
W('24,3321', 0o41056, 'NOTSHIFT', 'UNIT', 'BOVB', 'IF OVERFLOW, RANGE MUST BE GREATER', kind='interp', line=3220)
W('24,3322', 0o50102, '', '', '526ALARM', 'THAN 400 N. M.', kind='operand', line=3221)
W('24,3323', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=3222)
W('24,3324', 0o01734, '', '', 'REFSMMAT', 'CONVERT TO STABLE MEMBER', kind='operand', line=3223)
W('24,3325', 0o15102, '', 'STODL', 'RRTARGET', kind='interp', line=3224)
W('24,3326', 0o00045, '', '', '36D', 'SAVE MAGNITUDE OF LOS VECTOR FOR', kind='operand', line=3225)
W('24,3327', 0o01767, '', 'STORE', 'MLOSV', 'VELOCITY CORRECTION IN DESIGNATE', kind='interp', line=3226)
W('24,3330', 0o77614, '', 'CLRGO', kind='interp', line=3227)
W('24,3331', 0o00231, '', '', 'RRNBSW', kind='operand', line=3228)
W('24,3332', 0o01757, '', '', 'LS21X', kind='operand', line=3229)

# Page 566
# PROGRAM NAME:  LPS20.2  400 NM RANGE CHECK
# MOD. NO. 2    BY J.D. COYNE   SDC     DATE 12-7-66
#
# FUNCTIONAL DESCRIPTION:
# COMPARES THE MAGNITUDE OF THE LOS VECTOR TO 400 NM.
#
# CALLING SEQUENCE:     CALL
# LPS20.2
#
# SUBROUTINES CALLED:  NONE
#
# NORMAL EXIT:  RETURN TO CALLER +1, MPAC EQ 0 (RANGE 400NM OR LESS.)
#
# ERROR EXITS:  RETURN TO CALLER +1, MPAC EQ 1 (RANGE GREATER THAN 400NM)
#
# ALARMS:  NONE
#
# OUTPUT:  NONE
#
# INITIALIZED ERASEABLE:
# PDL 36D MUST CONTAIN THE MAGNITUDE OF THE VECTOR
#
# DEBRIS:
# MPAC DESTROYED BY THIS ROUTINE

#   SETLOC P20S1
#   BANK
#   COUNT* $$/LPS20

W('25,3565', 0o45345, 'LPS20.2', 'DLOAD', 'DSU', kind='interp', line=3261)
W('25,3566', 0o01767, '', '', 'MLOSV', 'MAGNITUDE OF LOS', kind='operand', line=3262)
W('25,3567', 0o13600, '', '', 'FHNM', 'OVER 400NM', kind='operand', line=3263)
W('25,3570', 0o77644, '', 'BPL', kind='interp', line=3264)
W('25,3571', 0o53574, '', '', 'TOFAR', kind='operand', line=3265)
W('25,3572', 0o43535, '', 'SLOAD', 'RVQ', kind='interp', line=3266)
W('25,3573', 0o06522, '', '', 'ZERO/SP', kind='operand', line=3267)
W('25,3574', 0o43535, 'TOFAR', 'SLOAD', 'RVQ', kind='interp', line=3268)
W('25,3575', 0o13577, '', '', 'ONE/SP', kind='operand', line=3269)
W('25,3576', 0o00001, 'ONE/SP', 'DEC', '1', kind='data', line=3270)
# Page 567
W('25,3577', 0o26467, 'FHNM', '2DEC', '740800 B-20', '400 NAUTICAL MILES IN METERS B-20', kind='data', line=3272)
W('25,3600', 0o00000, kind='data', line=3272)

# Page 568
# PROGRAM NAME:  LRS22.1 (DATA READ SUBROUTINE 1)
# MOD. NO.: 1           BY: P. VOLANTE  SDC             DATE:  11-15-66
#
# FUNCTIONAL DESCRIPTION:
# 1)      READS RENDEZVOUS RADAR RANGE AND RANGE-RATE, TRUNNION AND SHAFT ANGLES, THREE CDU VALUES AND TIME.  CONVERTS THIS
# DATA AND LEAVES IT FOR THE MEASUREMENT INCORPORATION ROUTINE (LSR22.3).  CHECKS FOR THE RR DATA GOOD DISCRETE, FOR
# RR REPOSITION AND RR CDU FAIL
# 2)      COMPARES RADAR LOS WITH LOS COMPUTED FROM STATE VECTORS TO SEE IF THEY ARE WITHIN THREE DEGREES
#
# CALLING SEQUENCE:  BANKCALL FOR LRS22.1
#
# SUBROUTINES CALLED:
# RRDOT           LPS20.1
# RRRANGE         BANKCALL
# RADSTALL        CDULOGIC
# RRNB            SMNB
#
# NORMAL EXIT:  RETURN TO CALLER+1 WITH MPAC SET TO +0
#
# ERROR EXITS:  RETURN TO CALLER+1 WITH ERROR CODE STORED IN MPAC AS FOLLOWS:
# 00001 -- ERROR EXIT 1 -- RR DATA NO GOOD (NO RR DATA GOOD DISCRETE OR RR CDU FAIL OR RR REPOSITION)
# 00002 -- ERROR EXIT 2 -- RR LOS NOT WITHIN THREE DEGREES OF LOS COMPUTED FROM STATE VECTORS
#
# ALARMS:  521 -- COULD NOT READ RADAR DATA (RR DATA GOOD DISCRETE NOT PRESENT BEFORE AND AFTER READING THE RADAR)
# (THIS ALARM IS ISSUED BY RADARREAD SUBROUTINE WHICH IS ENTERED FROM A RADARUPT)
#
# OUTPUT:  RRLOSVEC -- THE RR LINE-OF-SIGHT VECTOR (USED BY LRS22.2) -- A HALF-UNIT VECTOR
# RM -- THE RR RANGE READING (TO THE CSM) DP, IN METERS SCALED BY B-29 (USED BY LRS22.2 AND LRS22.3)
#
# ALL OF THE FOLLOWING OUTPUTS ARE USED BY LRS22.3:
# RDOTM -- THE RR RANGE-RATE READING, DP, IN METERS PER CENTISECOND, SCALED BY B-7
# RRTRUN -- THE RR TRUNNION ANGLE, DP, IN REVOLUTIONS, SCALED B0
# RRSHAFT -- RR SHAFT ANGLE, DP, IN REVOLUTIONS, SCALED B0
# AIG,AMG,AOG -- THE CDU ANGLES, THREE SP WORDS
# MKTIME -- THE TIME OF THE RR READING, DP, IN CENTISECONDS
#
# ERASABLE INITIALIZATION REQUIRED:
# RNRAD, THE RADAR READ COUNTER FROM WHICH IS OBTAINED:
# Page 569
# 1) RR RANGE SCALED 9.38 FT. PER BIT ON THE LOW SCALE AND 75.04 FT. PER BIT ON THE HIGH SCALE
# 2) RR RANGE RATE, SCALED .6278 FT./SEC. PER BIT
# THE CDU ANGLES FROM CDUX, CDUY, CDUZ, AND TIME1 AND TIME2
#
# DEBRIS:  LRS22.1X, A, L, Q, PUSHLIST

#   BANK 32
#   SETLOC LRS22
#   BANK
#   COUNT* $$/LRS22

W('32,2366', 0o04645, 'LRS22.1', 'TC', 'MAKECADR', line=3325)
W('32,2367', 0o55737, '', 'TS', 'LRS22.1X', line=3326)
W('32,2370', 0o05516, '', 'TC', 'DOWNFLAG', line=3327)
W('32,2371', 0o00120, '', 'ADRES', 'RNGSCFLG', kind='data', line=3328)
W('32,2372', 0o00004, '', 'INHINT', line=3329)
W('32,2373', 0o34751, '', 'CAF', 'BIT3', line=3330)
W('32,2374', 0o00006, '', 'EXTEND', '', 'GET RR RANGE SCALE', line=3331)
W('32,2375', 0o02033, '', 'RAND', 'CHAN33', 'FROM CHANNEL 33 BIT 3', line=3332)
W('32,2376', 0o54001, '', 'TS', 'L', line=3333)
W('32,2377', 0o44751, '', 'CS', 'RRRSBIT', line=3334)
W('32,2400', 0o70110, '', 'MASK', 'RADMODES', line=3335)
W('32,2401', 0o60001, '', 'AD', 'L', line=3336)
W('32,2402', 0o54110, '', 'TS', 'RADMODES', line=3337)
W('32,2403', 0o00003, '', 'RELINT', line=3338)
W('32,2404', 0o04616, 'READRDOT', 'TC', 'BANKCALL', line=3339)
W('32,2405', 0o53103, '', 'CADR', 'RRRDOT', 'READ RANGE-RATE (ONE SAMPLE)', kind='data', line=3340)
W('32,2406', 0o04616, '', 'TC', 'BANKCALL', line=3341)
W('32,2407', 0o17714, '', 'CADR', 'RADSTALL', 'WAIT FOR DATA READ COMPLETION', kind='data', line=3342)
W('32,2410', 0o12542, '', 'TCF', 'EREXIT1', 'COULD NOT READ RADAR-ERROR EXIT 1', line=3343)

W('32,2411', 0o00004, '', 'INHINT', '', 'NO INTERRUPTS WHILE READING TIME AND CDU', line=3345)
W('32,2412', 0o53106, '', 'DXCH', 'TIMEHOLD', 'SET MARK TIME EQUAL TO THE MID-POINT', line=3346)
W('32,2413', 0o52162, '', 'DXCH', 'MPAC +5', 'TEMP BUFFER FOR DOWNLINK', line=3347)
W('32,2414', 0o53102, '', 'DXCH', 'SAMPLSUM', 'SAVE RANGE-RATE READING', line=3348)
W('32,2415', 0o53747, '', 'DXCH', 'RDOTMSAV', line=3349)
W('32,2416', 0o00006, '', 'EXTEND', line=3350)
W('32,2417', 0o30034, '', 'DCA', 'CDUY', 'SAVE ICDU ANGLES', line=3351)
W('32,2420', 0o52160, '', 'DXCH', 'MPAC +3', 'TEMP BUFFER FOR DOWNLINK', line=3352)
W('32,2421', 0o30032, '', 'CA', 'CDUX', line=3353)
W('32,2422', 0o54156, '', 'TS', 'MPAC +2', 'TEMP BUFFER FOR DOWNLINK', line=3354)
W('32,2423', 0o00006, '', 'EXTEND', line=3355)
W('32,2424', 0o30025, '', 'DCA', 'TIME2', 'SAVE TIME', line=3356)
W('32,2425', 0o52155, '', 'DXCH', 'MPAC', 'SAVE TIME OF CDUY READINGS IN MPAC', line=3357)
W('32,2426', 0o00006, '', 'EXTEND', line=3358)
W('32,2427', 0o30036, '', 'DCA', 'CDUT', 'SAVE TRUNNION AND SHAFT ANGLES FOR RRNB', line=3359)
W('32,2430', 0o53110, '', 'DXCH', 'TANG', line=3360)
# Page 570
W('32,2431', 0o00003, '', 'RELINT', line=3362)
W('32,2432', 0o04616, '', 'TC', 'BANKCALL', line=3363)
W('32,2433', 0o53105, '', 'CADR', 'RRRANGE', 'READ RR RANGE (ONE SAMPLE)', kind='data', line=3364)
W('32,2434', 0o04616, '', 'TC', 'BANKCALL', line=3365)
W('32,2435', 0o17714, '', 'CADR', 'RADSTALL', 'WAIT FOR READ COMPLETE', kind='data', line=3366)
W('32,2436', 0o02536, '', 'TC', 'CHEXERR', 'CHECK FOR ERRORS DURING READ', line=3367)
W('32,2437', 0o00004, '', 'INHINT', '', 'COPY CYCLE FOR MARK DATA ON DOWNLINK', line=3368)
W('32,2440', 0o53334, '', 'DXCH', 'DNRRANGE', 'RANGE, RANGE RATE (RAW DATA)', line=3369)
W('32,2441', 0o53761, '', 'DXCH', 'RANGRDOT', line=3370)
W('32,2442', 0o52162, '', 'DXCH', 'MPAC +5', line=3371)
W('32,2443', 0o53755, '', 'DXCH', 'MKTIME', 'MARK TIME', line=3372)
W('32,2444', 0o52160, '', 'DXCH', 'MPAC +3', line=3373)
W('32,2445', 0o53460, '', 'DXCH', 'AIG', 'CDUY, CDUZ', line=3374)
W('32,2446', 0o00006, '', 'EXTEND', line=3375)
W('32,2447', 0o31110, '', 'DCA', 'TANG', 'PRESERVE TANG', line=3376)
W('32,2450', 0o53753, '', 'DXCH', 'TANGNB', 'TRUNNION AND SHAFT ANGLES', line=3377)
W('32,2451', 0o30156, '', 'CA', 'MPAC +2', line=3378)
W('32,2452', 0o55461, '', 'TS', 'AOG', 'CDUX', line=3379)
W('32,2453', 0o06037, '', 'TC', 'INTPRET', line=3380)
W('32,2454', 0o14025, '', 'STODL', '20D', 'SAVE TIME OF CDU READINGS IN 20D', kind='interp', line=3381)
W('32,2455', 0o03747, '', '', 'RDOTMSAV', 'CONVERT RDOT UNITS AND SCALING', kind='operand', line=3382)
W('32,2456', 0o57261, '', 'SL', 'DMPR', 'START WITH READING SCALED B-28, -.6278', kind='interp', line=3383)
W('32,2457', 0o20217, '', '', '14D', 'FT./SECOND PER BIT', kind='operand', line=3384)
W('32,2460', 0o24002, '', '', 'RDOTCONV', 'END WITH METERS/CENTISECOND, B-7', kind='operand', line=3385)
W('32,2461', 0o03751, '', 'STORE', 'RDOTM', kind='interp', line=3386)
W('32,2462', 0o47135, '', 'SLOAD', 'RTB', kind='interp', line=3387)
W('32,2463', 0o01110, '', '', 'TANG', 'GET TRUNNION ANGLE', kind='operand', line=3388)
W('32,2464', 0o21576, '', '', 'CDULOGIC', 'CONVERT TO DP ONES COMP. IN REVOLUTIOINS', kind='operand', line=3389)
W('32,2465', 0o03734, '', 'STORE', 'RRTRUN', 'AND SAVE FOR TMI ROUTINE (LSR22.3)', kind='interp', line=3390)
W('32,2466', 0o47135, '', 'SLOAD', 'RTB', kind='interp', line=3391)
W('32,2467', 0o01111, '', '', 'TANG +1', 'DITTO FOR SHAFT ANGLE', kind='operand', line=3392)
W('32,2470', 0o21576, '', '', 'CDULOGIC', kind='operand', line=3393)
W('32,2471', 0o17736, '', 'STODL', 'RRSHAFT', kind='interp', line=3394)
W('32,2472', 0o01102, '', '', 'SAMPLSUM', kind='operand', line=3395)
W('32,2473', 0o66405, '', 'DMP', 'SL2R', 'CONVERT UNITS AND SCALING DP RANGE', kind='interp', line=3396)
W('32,2474', 0o24004, '', '', 'RANGCONV', 'PER BIT, END WITH METERS, SCALED -29', kind='operand', line=3397)
W('32,2475', 0o37757, '', 'STCALL', 'RM', kind='interp', line=3398)
W('32,2476', 0o46041, '', '', 'RRNB', 'COMPUTE RADAR LOS USING RRNB', kind='operand', line=3399)
W('32,2477', 0o17741, '', 'STODL', 'RRBORSIT', 'AND SAVE', kind='interp', line=3400)
W('32,2500', 0o00025, '', '', '20D', kind='operand', line=3401)
W('32,2501', 0o34041, '', 'STCALL', 'TDEC1', 'GET STATE VECTOR LOS AT TIME OF CDU READ', kind='interp', line=3402)
W('32,2502', 0o51255, '', '', 'LPS20.1', kind='operand', line=3403)
W('32,2503', 0o77776, '', 'EXIT', kind='interp', line=3404)
W('32,2504', 0o31457, '', 'CA', 'AIG', 'STORE IMU CDU ANGLES AT MARKTIME', line=3405)
W('32,2505', 0o54766, '', 'TS', 'CDUSPOT', 'IN CDUSPOT FOR TRG*SMNB', line=3406)
W('32,2506', 0o31460, '', 'CA', 'AMG', line=3407)
W('32,2507', 0o54770, '', 'TS', 'CDUSPOT +2', line=3408)
W('32,2510', 0o31461, '', 'CA', 'AOG', line=3409)
W('32,2511', 0o54772, '', 'TS', 'CDUSPOT +4', line=3410)
W('32,2512', 0o06037, '', 'TC', 'INTPRET', line=3411)
# Page 571
W('32,2513', 0o45175, '', 'VLOAD', 'CALL', 'LOAD VECTOR AND CALL TRANSFORMATION', kind='interp', line=3413)
W('32,2514', 0o01102, '', '', 'RRTARGET', kind='operand', line=3414)
W('32,2515', 0o47651, '', '', 'TRG*SMNB', 'ROTATE LOS AT MARKTIME FROM SM TO NB.', kind='operand', line=3415)
W('32,2516', 0o77641, '', 'DOT', '', 'DOT WITH RADAR LOS TO GET ANGLE', kind='interp', line=3416)
W('32,2517', 0o03741, '', '', 'RRBORSIT', kind='operand', line=3417)
W('32,2520', 0o65552, '', 'SL1', 'ACOS', 'BETWEEN THEM', kind='interp', line=3418)
W('32,2521', 0o01046, '', 'STORE', 'DSPTEM1', 'STORE FOR POSSIBLE DISPLAY', kind='interp', line=3419)
W('32,2522', 0o50025, '', 'DSU', 'BMN', 'IS IT LESS THAN 3 DEGREES', kind='interp', line=3420)
W('32,2523', 0o24546, '', '', 'THREEDEG', kind='operand', line=3421)
W('32,2524', 0o64531, '', '', 'NORMEXIT', 'YES -- NORMAL EXIT', kind='operand', line=3422)

W('32,2525', 0o77776, '', 'EXIT', '', 'ERROR EXIT 2', kind='interp', line=3424)
W('32,2526', 0o34752, '', 'CAF', 'BIT2', 'SET ERROR CODE', line=3425)
W('32,2527', 0o54154, '', 'TS', 'MPAC', line=3426)
W('32,2530', 0o12534, '', 'TCF', 'OUT22.1', line=3427)

W('32,2531', 0o77776, 'NORMEXIT', 'EXIT', '', 'NORMAL EXIT -- SET MPAC EQUAL ZERO', kind='interp', line=3429)
W('32,2532', 0o34755, '', 'CAF', 'ZERO', line=3430)
W('32,2533', 0o54154, '', 'TS', 'MPAC', line=3431)
W('32,2534', 0o31737, 'OUT22.1', 'CAE', 'LRS22.1X', 'EXIT FROM LRS22.1', line=3432)
W('32,2535', 0o04640, '', 'TC', 'BANKJUMP', line=3433)
W('32,2536', 0o30101, 'CHEXERR', 'CAE', 'FLAGWRD5', line=3434)
W('32,2537', 0o74742, '', 'MASK', 'RNGSCBIT', line=3435)
W('32,2540', 0o10000, '', 'CCS', 'A', 'CHECK IF RANGE SCALE CHANGED', line=3436)
W('32,2541', 0o12404, '', 'TCF', 'READRDOT', 'YES -- TAKE ANOTHER READING', line=3437)

W('32,2542', 0o34753, 'EREXIT1', 'CA', 'BIT1', 'SET ERROR CODE', line=3439)
W('32,2543', 0o54154, '', 'TS', 'MPAC', line=3440)
W('32,2544', 0o02534, '', 'TC', 'OUT22.1', line=3441)
W('32,2545', 0o00210, 'THREEDEG', '2DEC', '.008333333', 'THREE DEGREES, SCALED REVS, B0', kind='data', line=3442)
W('32,2546', 0o21042, kind='data', line=3442)

S('RRLOSVEC', 'equals', 0o1101, line=3444)

# Page 572
# PROGRAM NAME -- LRS22.2 (DATA READ SUBROUTINE 2)
# MOD. NO.: 1           BY: P. VOLANTE  SDC             DATE: 4-11-67
#
# FUNCTIONAL DESCRIPTION:
# (Yes, I know point #1 is missing.  It is missing from the program listing -- RSB 2003)
# 2)  CHECKS IF THE RR LOS (I.E., THE RADAR BORESIGHT VECTOR) IS WITHIN 30 DEGREES OF THE LM +Z AXIS
#
# CALLING SEQUENCE:  BANKCALL FOR LRS22.2
#
# SUBROUTINES CALLED:  G+N, AUTO, SETMAXDB
#
# NORMAL EXIT:  RETURN TO CALLER WITH MPAC SET TO +0 (VIA SWRETURN)
#
# ERROR EXIT:  RETURN TO CALLER WITH MPAC SET TO 00001 -- RADAR LOS NOT WITHIN 30 DEGREES OF LM +Z AXIS.
#
# ALARMS:  NONE
#
# ERASABLE INITIALIZATION REQUIRED:
# RRLOSVEC -- THE RR LINE-OF-SIGHT VECTOR -- A HALF UNIT VECTOR COMPUTED BY LRS22.1
# RM -- RR RANGE, METERS B-29, FROM LRS22.1
# BIT 14 CHANNEL 31 -- INDICATES AUTOPILOT IS IN AUTO MODE
#
# DEBRIS -- A,L,Q,MPAC -- PUSHLIST AND PUSHLOC ARE NOT CHANGED BY THIS ROUTINE

#   SETLOC P20S
#   BANK
W('24,3333', 0o04645, 'LRS22.2', 'TC', 'MAKECADR', line=3473)
W('24,3334', 0o55737, '', 'TS', 'LRS22.1X', line=3474)
W('24,3335', 0o06037, '', 'TC', 'INTPRET', line=3475)
# CHECK IF RR LOS IS WITHIN 30 DEG OF
W('24,3336', 0o65545, '30DEGCHK', 'DLOAD', 'ACOS', 'THE SPACECRAFT +Z AXIT', kind='interp', line=3477)
W('24,3337', 0o03745, '', '', 'RRBORSIT +4', 'BY TAKING ARCCOS OF Z-COMP. OF THE RR', kind='operand', line=3478)
# LOS VECTOR, A HALF UNIT VECTOR
# IN NAV BASE AXES)
W('24,3340', 0o50025, '', 'DSU', 'BMN', kind='interp', line=3481)
W('24,3341', 0o11355, '', '', '30DEG', kind='operand', line=3482)
W('24,3342', 0o51347, '', '', 'OKEXIT', 'NORMAL EXIT -- WITHIN 30 DEG.', kind='operand', line=3483)
W('24,3343', 0o77776, '', 'EXIT', '', 'ERROR EXIT -- NOT WITHIN 30 DEG.', kind='interp', line=3484)
W('24,3344', 0o34753, '', 'CAF', 'BIT1', 'SETS ERROR CODE IN MPAC', line=3485)
W('24,3345', 0o54154, '', 'TS', 'MPAC', line=3486)
W('24,3346', 0o13352, '', 'TCF', 'OUT22.2', line=3487)
W('24,3347', 0o77776, 'OKEXIT', 'EXIT', '', 'NORMAL EXIT -- SET MPAC = ZERO', kind='interp', line=3488)

# Page 573
W('24,3350', 0o34755, '', 'CAF', 'ZERO', line=3491)
W('24,3351', 0o54154, '', 'TS', 'MPAC', line=3492)
W('24,3352', 0o31737, 'OUT22.2', 'CAE', 'LRS22.1X', line=3493)
W('24,3353', 0o04640, '', 'TC', 'BANKJUMP', line=3494)

W('24,3354', 0o02525, '30DEG', '2DEC', '.083333333', 'THIRTY DEGREES, SCALED REVS, B0', kind='data', line=3496)
W('24,3355', 0o12525, kind='data', line=3496)

# Page 574
# PROGRAM NAME -- LSR22.3                               DATE -- 29 MAY 1967
# MOD. NO 3                                             LOG SECTION -- P20-P25
# MOD. BY -- DANFORTH                                   ASSEMBLY LEMP20S REV 10
#
# FUNCTIONAL DESCRIPTION:
# THIS ROUTINE COMPUTES THE B-VECTORS ADN DELTA Q FOR EACH OF THE QUANTITIES MEASURED BY THE RENDEZVOUS
# RADAR.  (RANGE, RANGE RATE, SHAFT AND TRUNNION ANGLES).  THE ROUTINE CALLS THE INCORP1 AND INCORP2 ROUTINES
# WHICH COMPUTE THE DEVIATIONS AND CORRECT THE STATE VECTOR.
#
# CALLING SEQUENCE:
# THIS ROUTINE IS PART OF P20 RENDEZVOUS NAVIGATION FOR THE LM COMPUTER ONLY.  THE ROUTINE IS ENTERED FROM
# R22 LEM ONLY AND RETURNS DIRECTLY TO R22LEM FOLLOWING SUCCESSFUL INCORPORATION OF MEASURED DATA.  IF THE
# COMPUTED STATE VECTOR DEVATIONS EXCEED THE MAXIMUM PERMITTED.  THE ROUTINE RETURNS TO R22LEM TO DISPLAY
# THE DEVIATIONS.  IF THE ASTRONAUT ACCEPTS THE DATA R22LEM RETURNS TO LSR22.3 TO INCORPORATE THE
# DEVIATIONS INTO THE STATE VECTOR.  IF THE ASTRONAUT REJECTS THE DEVIATIONS, NO MORE MEASUREMENTS ARE
# PROCESSED FOR THIS MARK, I.E.,  R22LEM GETS THE NEXT MARK.
#
# SUBROUTINES CALLED:
# WLINIT          LGCUPDTE        INTEGRV         INCORP1         ARCTAN
# GETULC          RADARANG        INCORP2         NBSM            INTSTALL
#
# OUTPUT:
# CORRECTED LM OR CSM STATE VECTOR (PERMANENT)
# NUMBER OF MARKS INCORPORATED IN MARKCTR
# MAGNITUDE OF POSITION DEVIATION (FOR DISPLAY) IN R22DISP METERS B-29
# MAGNITUDE OF VELOCITY DEVIATION (FOR DISPLAY) IN R22DISP +2 M/CSEC B-7
# UPDATED W-MATRIX
#
# ERASABLE INITIALIZATION REQUIRED:
# LM AND CSM STATE VECTORS
# W-MATRIX
# MARK TIME IN MKTIME
# RADAR RANGE IN RM METERS B-29
# RANGE RATE IN RDOTM METERS/CSES B-7
# SHAFT ANGLE IN RRSHAFT REVS. B0
# TRUNNION ANGLE IN RRTRUN REVS. B0
# GIMBAL ANGLES   INNER IN AIG
# MIDDLE IN AMG
# OUTER IN ACG
# REFSMMAT
# RENDWFLG
# NOANGFLG
# VEHUPFLG
#
# DEBRIS:
# PUSHLIST -- ALL
# MX, MY, MZ (VECTORS)
# Page 575
# ULC, RXZ, SINTHETA, LGRET, RDRET, BVECTOR, W.IND, X78T

#   BANK 13
#   SETLOC P20S3
#   BANK

#   EBANK= LOSCOUNT
#   COUNT* $$/LSR22
W('26,2412', 0o77624, 'LSR22.3', 'CALL', kind='interp', line=3555)
W('26,2413', 0o11244, '', '', 'GRP2PC', kind='operand', line=3556)
W('26,2414', 0o43014, '', 'BON', 'SET', kind='interp', line=3557)
W('26,2415', 0o04307, '', '', 'SURFFLAG', 'ARE WE ON LUNAR SURFACE', kind='operand', line=3558)
W('26,2416', 0o55200, '', '', 'LSR22.4', 'YES', kind='operand', line=3559)
W('26,2417', 0o02466, '', '', 'DMENFLG', kind='operand', line=3560)
W('26,2420', 0o45014, '', 'BOFF', 'CALL', kind='interp', line=3561)
W('26,2421', 0o00747, '', '', 'VEHUPFLG', kind='operand', line=3562)
W('26,2422', 0o54454, '', '', 'DOLEM', kind='operand', line=3563)
W('26,2423', 0o27414, '', '', 'INTSTALL', kind='operand', line=3564)
W('26,2424', 0o45014, '', 'CLEAR', 'CALL', 'LM PRECISION INTEGRATION', kind='interp', line=3565)
W('26,2425', 0o01674, '', '', 'VINTFLAG', kind='operand', line=3566)
W('26,2426', 0o26644, '', '', 'SETIFLGS', kind='operand', line=3567)
W('26,2427', 0o77624, '', 'CALL', kind='interp', line=3568)
W('26,2430', 0o55242, '', '', 'INTGRCAL', kind='operand', line=3569)
W('26,2431', 0o77624, '', 'CALL', kind='interp', line=3570)
W('26,2432', 0o11244, '', '', 'GRP2PC', kind='operand', line=3571)
W('26,2433', 0o77624, '', 'CALL', kind='interp', line=3572)
W('26,2434', 0o27414, '', '', 'INTSTALL', kind='operand', line=3573)
W('26,2435', 0o43014, '', 'CLEAR', 'BOFF', kind='interp', line=3574)
W('26,2436', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=3575)
W('26,2437', 0o02756, '', '', 'RENDWFLG', kind='operand', line=3576)
W('26,2440', 0o54444, '', '', 'NOTWCSM', kind='operand', line=3577)
W('26,2441', 0o43014, '', 'SET', 'SET', 'CSM WITH W-MATRIX INTEGRATION', kind='interp', line=3578)
W('26,2442', 0o01476, '', '', 'DIM0FLAG', kind='operand', line=3579)
W('26,2443', 0o01475, '', '', 'D6OR9FLG', kind='operand', line=3580)
W('26,2444', 0o43014, 'NOTWCSM', 'SET', 'CLEAR', kind='interp', line=3581)
W('26,2445', 0o01474, '', '', 'VINTFLAG', kind='operand', line=3582)
W('26,2446', 0o01673, '', '', 'INTYPFLG', kind='operand', line=3583)
W('26,2447', 0o45014, '', 'SET', 'CALL', kind='interp', line=3584)
W('26,2450', 0o01472, '', '', 'STATEFLG', kind='operand', line=3585)
W('26,2451', 0o55242, '', '', 'INTGRCAL', kind='operand', line=3586)
W('26,2452', 0o77650, '', 'GOTO', kind='interp', line=3587)
W('26,2453', 0o54504, '', '', 'MARKTEST', kind='operand', line=3588)
W('26,2454', 0o77624, 'DOLEM', 'CALL', kind='interp', line=3589)
W('26,2455', 0o27414, '', '', 'INTSTALL', kind='operand', line=3590)
W('26,2456', 0o45014, '', 'SET', 'CALL', kind='interp', line=3591)
W('26,2457', 0o01474, '', '', 'VINTFLAG', kind='operand', line=3592)
W('26,2460', 0o26644, '', '', 'SETIFLGS', kind='operand', line=3593)
W('26,2461', 0o77624, '', 'CALL', kind='interp', line=3594)
W('26,2462', 0o55242, '', '', 'INTGRCAL', kind='operand', line=3595)
# Page 576
W('26,2463', 0o77624, '', 'CALL', kind='interp', line=3597)
W('26,2464', 0o11244, '', '', 'GRP2PC', kind='operand', line=3598)
W('26,2465', 0o77624, '', 'CALL', kind='interp', line=3599)
W('26,2466', 0o27414, '', '', 'INTSTALL', kind='operand', line=3600)
W('26,2467', 0o43014, '', 'CLEAR', 'BOFF', kind='interp', line=3601)
W('26,2470', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=3602)
W('26,2471', 0o02756, '', '', 'RENDWFLG', kind='operand', line=3603)
W('26,2472', 0o54476, '', '', 'NOTWLEM', kind='operand', line=3604)
W('26,2473', 0o43014, '', 'SET', 'SET', 'LM WITH W-MATRIX INTEGRATION', kind='interp', line=3605)
W('26,2474', 0o01476, '', '', 'DIM0FLAG', kind='operand', line=3606)
W('26,2475', 0o01475, '', '', 'D6OR9FLG', kind='operand', line=3607)
W('26,2476', 0o43014, 'NOTWLEM', 'CLEAR', 'CLEAR', kind='interp', line=3608)
W('26,2477', 0o01673, '', '', 'INTYPFLG', kind='operand', line=3609)
W('26,2500', 0o01674, '', '', 'VINTFLAG', kind='operand', line=3610)
W('26,2501', 0o45014, '', 'SET', 'CALL', kind='interp', line=3611)
W('26,2502', 0o01472, '', '', 'STATEFLG', kind='operand', line=3612)
W('26,2503', 0o55242, '', '', 'INTGRCAL', kind='operand', line=3613)
W('26,2504', 0o45014, 'MARKTEST', 'BON', 'CALL', 'HAS W-MATRIX BEEN INVALIDATED', kind='interp', line=3614)
W('26,2505', 0o02716, '', '', 'RENDWFLG', 'HAS W-MATRIX BEEN INVALIDATED', kind='operand', line=3615)
W('26,2506', 0o54510, '', '', 'RANGEBQ', kind='operand', line=3616)
W('26,2507', 0o55251, '', '', 'WLINIT', 'YES -- REINITIALIZE', kind='operand', line=3617)
W('26,2510', 0o77414, 'RANGEBQ', 'BON', 'EXIT', "DON'T CALL R65 IF ON SURFACE", kind='interp', line=3618)
W('26,2511', 0o04307, '', '', 'SURFFLAG', kind='operand', line=3619)
W('26,2512', 0o54520, '', '', 'RANGEBQ1', kind='operand', line=3620)
W('26,2513', 0o34755, '', 'CA', 'ZERO', line=3621)
W('26,2514', 0o55745, '', 'TS', 'R65CNTR', line=3622)
W('26,2515', 0o04616, '', 'TC', 'BANKCALL', line=3623)
W('26,2516', 0o46123, '', 'CADR', 'R65LEM', kind='data', line=3624)
W('26,2517', 0o06037, '', 'TC', 'INTPRET', line=3625)
W('26,2520', 0o43174, 'RANGEBQ1', 'AXT,2', 'BON', 'CLEAR X2', kind='interp', line=3626)
W('26,2521', 0o00000, '', '', '0', kind='operand', line=3627)
W('26,2522', 0o04304, '', '', 'LMOONFLG', 'IS MOON SPHERE OF INFLUENCE', kind='operand', line=3628)
W('26,2523', 0o54526, '', '', 'SETX2', 'YES.  STORE ZERO IN SCALSHFT REGISTER', kind='operand', line=3629)
W('26,2524', 0o77714, '', 'INCR,2', kind='interp', line=3630)
W('26,2525', 0o00002, '', '', '2', kind='operand', line=3631)
W('26,2526', 0o45134, 'SETX2', 'SXA,2', 'CALL', kind='interp', line=3632)
W('26,2527', 0o03720, '', '', 'SCALSHFT', '0 -- MOON.  2 -- EARTH.', kind='operand', line=3633)
W('26,2530', 0o11244, '', '', 'GRP2PC', kind='operand', line=3634)
W('26,2531', 0o66170, '', 'AXT,1', 'SXA,1', 'STORE RANGE CODE (1) FOR R3 IN NOUN 49', kind='interp', line=3635)
W('26,2532', 0o00001, '', '', '1', kind='operand', line=3636)
W('26,2533', 0o03745, '', '', 'WHCHREAD', kind='operand', line=3637)
W('26,2534', 0o54335, '', 'SLOAD', 'SR', 'GET SINGLE PRECISION RVARMIN (B-12)', kind='interp', line=3638)
W('26,2535', 0o01775, '', '', 'RVARMIN', 'SHIFT TO TRIPLE PRECISION (B-40)', kind='operand', line=3639)
W('26,2536', 0o20635, '', '', '28D', kind='operand', line=3640)
W('26,2537', 0o77634, '', 'RTB', kind='interp', line=3641)
W('26,2540', 0o21633, '', '', 'TPMODE', 'AND SAVE IN 20D', kind='operand', line=3642)
W('26,2541', 0o00025, '', 'STORE', '20D', kind='interp', line=3643)
W('26,2542', 0o77624, '', 'CALL', '', 'BEGIN COMPUTING THE B-VECTORS, DELTAQ', kind='interp', line=3644)
W('26,2543', 0o55333, '', '', 'GETULC', 'B-VECTORS FOR RANGE', kind='operand', line=3645)
W('26,2544', 0o57414, '', 'BON', 'VCOMP', 'B0, COMP. IF LM BEING CORRECTED', kind='interp', line=3646)
# Page 577
W('26,2545', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=3648)
W('26,2546', 0o54547, '', '', '+1', kind='operand', line=3649)
W('26,2547', 0o27525, '', 'STOVL', 'BVECTOR', kind='interp', line=3650)
W('26,2550', 0o06522, '', '', 'ZEROVECS', kind='operand', line=3651)
W('26,2551', 0o03533, '', 'STORE', 'BVECTOR +6', 'B1', kind='interp', line=3652)
W('26,2552', 0o17541, '', 'STODL', 'BVECTOR +12D', 'B2', kind='interp', line=3653)
W('26,2553', 0o00045, '', '', '36D', kind='operand', line=3654)
W('26,2554', 0o44257, '', 'SRR*', 'BDSU', kind='interp', line=3655)
W('26,2555', 0o56174, '', '', '2,2', 'SHIFT FROM EARTH/MOON SPHERE TO B-29', kind='operand', line=3656)
W('26,2556', 0o03757, '', '', 'RM', 'RM - (MAGNITUDE RCSM-RLM)', kind='operand', line=3657)
W('26,2557', 0o77657, '', 'SLR*', kind='interp', line=3658)
W('26,2560', 0o56574, '', '', '2,2', 'SHIFT TO EARTH/MOON SPHERE', kind='operand', line=3659)
W('26,2561', 0o17547, '', 'STODL', 'DELTAQ', 'EARTH B-29.  MOON B-27', kind='interp', line=3660)
W('26,2562', 0o00045, '', '', '36D', 'RLC B-29/B-27', kind='operand', line=3661)
W('26,2563', 0o63501, '', 'NORM', 'DSQ', 'NORMALIZE AND SQUARE', kind='interp', line=3662)
W('26,2564', 0o00047, '', '', 'X1', kind='operand', line=3663)
W('26,2565', 0o53605, '', 'DMP', 'SR*', kind='interp', line=3664)
W('26,2566', 0o01771, '', '', 'RANGEVAR', 'MULTIPLY BY RANGEVAR (B12) THEN', kind='operand', line=3665)
W('26,2567', 0o20577, '', '', '0 -2,1', 'UNNORMALIZE', kind='operand', line=3666)
W('26,2570', 0o53657, '', 'SR*', 'SR*', kind='interp', line=3667)
W('26,2571', 0o20601, '', '', '0,1', kind='operand', line=3668)
W('26,2572', 0o57176, '', '', '0,2', kind='operand', line=3669)
W('26,2573', 0o47057, '', 'SR*', 'RTB', kind='interp', line=3670)
W('26,2574', 0o57176, '', '', '0,2', kind='operand', line=3671)
W('26,2575', 0o21633, '', '', 'TPMODE', kind='operand', line=3672)
W('26,2576', 0o02707, '', 'STORE', 'VARIANCE', 'B-40', kind='interp', line=3673)
W('26,2577', 0o76276, '', 'DCOMP', 'TAD', kind='interp', line=3674)
W('26,2600', 0o00025, '', '', '20D', 'B-40', kind='operand', line=3675)
W('26,2601', 0o72240, '', 'BMN', 'TLOAD', kind='interp', line=3676)
W('26,2602', 0o54605, '', '', 'QOK', kind='operand', line=3677)
W('26,2603', 0o00025, '', '', '20D', 'B-40', kind='operand', line=3678)
W('26,2604', 0o02707, '', 'STORE', 'VARIANCE', kind='interp', line=3679)
W('26,2605', 0o77624, 'QOK', 'CALL', kind='interp', line=3680)
W('26,2606', 0o55401, '', '', 'LGCUPDTE', kind='operand', line=3681)

W('26,2607', 0o45131, '', 'SSP', 'CALL', kind='interp', line=3683)
W('26,2610', 0o03746, '', '', 'WHCHREAD', kind='operand', line=3684)
W('26,2611', 0o00002, '', 'DEC', '2', 'STORE R-RATE CODE (2) FOR R3 IN NOUN 49', kind='data', line=3685)
W('26,2612', 0o11244, '', '', 'GRP2PC', kind='operand', line=3686)
W('26,2613', 0o77624, '', 'CALL', '', 'B-VECTOR, DELTAQ FOR RANGE RATE', kind='interp', line=3687)
W('26,2614', 0o55333, '', '', 'GETULC', kind='operand', line=3688)
W('26,2615', 0o53725, '', 'PDDL', 'SR*', 'GET RLC SCALED B-29/B-27', kind='interp', line=3689)
W('26,2616', 0o00045, '', '', '36D', 'AND SHIFT TO B-23', kind='operand', line=3690)
W('26,2617', 0o57202, '', '', '0 -4,2', kind='operand', line=3691)
W('26,2620', 0o24045, '', 'STOVL', '36D', 'THEN STORE BACK IN 36D', kind='interp', line=3692)
W('26,2621', 0o57414, '', 'BON', 'VCOMP', 'B1, COMP. IF LM BEING CORRECTED', kind='interp', line=3693)
W('26,2622', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=3694)
W('26,2623', 0o54624, '', '', '+1', kind='operand', line=3695)
W('26,2624', 0o77761, '', 'VXSC', kind='interp', line=3696)
W('26,2625', 0o00045, '', '', '36D', 'B1 = RLC (B-24/B-22)', kind='operand', line=3697)
# Page 578
W('26,2626', 0o27533, '', 'STOVL', 'BVECTOR +6', kind='interp', line=3699)
W('26,2627', 0o01653, '', '', 'NUVLEM', kind='operand', line=3700)
W('26,2630', 0o53257, '', 'VSR*', 'VAD', kind='interp', line=3701)
W('26,2631', 0o57170, '', '', '6,2', 'SHIFT FOR EARTH/MOON SPHERE', kind='operand', line=3702)
W('26,2632', 0o01667, '', '', 'VCVLEM', 'EARTH B-7. MOON B-5', kind='operand', line=3703)
W('26,2633', 0o53715, '', 'PDVL', 'VSR*', 'VL TO PD6', kind='interp', line=3704)
W('26,2634', 0o01601, '', '', 'NUVCSM', kind='operand', line=3705)
W('26,2635', 0o57170, '', '', '6,2', 'SHIFT FOR EARTH/MOON SPHERE', kind='operand', line=3706)
W('26,2636', 0o52255, '', 'VAD', 'VSU', kind='interp', line=3707)
W('26,2637', 0o01615, '', '', 'VCVCSM', kind='operand', line=3708)
W('26,2640', 0o50315, '', 'PDVL', 'DOT', 'VC - VL = VLC TO PD6', kind='interp', line=3709)
W('26,2641', 0o00001, '', '', '0', kind='operand', line=3710)
W('26,2642', 0o00007, '', '', '6', kind='operand', line=3711)
W('26,2643', 0o53606, '', 'PUSH', 'SRR*', 'RDOT B-8/B-6 TO PD12', kind='interp', line=3712)
W('26,2644', 0o56174, '', '', '2,2', 'SHIFT FROM EARTH/MOON SPHERE TO B-8', kind='operand', line=3713)
W('26,2645', 0o57316, '', 'DSQ', 'DMPR', 'RDOT**2 B-16 X RATEVAR B12', kind='interp', line=3714)
W('26,2646', 0o01773, '', '', 'RATEVAR', kind='operand', line=3715)
W('26,2647', 0o02707, '', 'STORE', 'VARIANCE', kind='interp', line=3716)
W('26,2650', 0o54335, '', 'SLOAD', 'SR', kind='interp', line=3717)
W('26,2651', 0o01776, '', '', 'VVARMIN', 'GET SINGLE PRECISION VVARMIN (B+12)', kind='operand', line=3718)
W('26,2652', 0o20621, '', '', '16D', 'SHIFT TO DP (B-4)', kind='operand', line=3719)
W('26,2653', 0o00031, '', 'STORE', '24D', 'AND SAVE IN 24D', kind='interp', line=3720)
W('26,2654', 0o50025, '', 'DSU', 'BMN', 'IS MIN. VARIANCE > COMPUTED VARIANCE', kind='interp', line=3721)
W('26,2655', 0o02707, '', '', 'VARIANCE', kind='operand', line=3722)
W('26,2656', 0o54662, '', '', 'VOK', 'BRANCH -- NO', kind='operand', line=3723)
W('26,2657', 0o77745, '', 'DLOAD', '', 'YES -- USE MINIMUM VARIANCE', kind='interp', line=3724)
W('26,2660', 0o00031, '', '', '24D', kind='operand', line=3725)
W('26,2661', 0o02707, '', 'STORE', 'VARIANCE', kind='interp', line=3726)
W('26,2662', 0o60545, 'VOK', 'DLOAD', 'SR2', 'RDOT (PD12) FROM B-8/B-6', kind='interp', line=3727)
W('26,2663', 0o53725, '', 'PDDL', 'SLR*', 'TO B-10/B-8', kind='interp', line=3728)
W('26,2664', 0o03751, '', '', 'RDOTM', 'SHIFT TO EARTH/MOON SPHERE', kind='operand', line=3729)
W('26,2665', 0o56577, '', '', '0 -1,2', 'B-7 TO B-10/B-8', kind='operand', line=3730)
W('26,2666', 0o77625, '', 'DSU', kind='interp', line=3731)
W('26,2667', 0o77675, '', 'DMPR', kind='interp', line=3732)
W('26,2670', 0o00045, '', '', '36D', kind='operand', line=3733)
W('26,2671', 0o27547, '', 'STOVL', 'DELTAQ', 'B-33', kind='interp', line=3734)
W('26,2672', 0o00001, '', '', '0', 'NOW GET B0', kind='operand', line=3735)
W('26,2673', 0o47235, '', 'VXV', 'VXV', '(ULC X VLC) X ULC', kind='interp', line=3736)
W('26,2674', 0o57414, '', 'BON', 'VCOMP', 'B0, COMP. IF LM BEING CORRECTED', kind='interp', line=3737)
W('26,2675', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=3738)
W('26,2676', 0o54677, '', '', '+1', kind='operand', line=3739)
W('26,2677', 0o77657, '', 'VSR*', kind='interp', line=3740)
W('26,2700', 0o57200, '', '', '0 -2,2', 'SCALED B-5', kind='operand', line=3741)
W('26,2701', 0o27525, '', 'STOVL', 'BVECTOR', kind='interp', line=3742)
W('26,2702', 0o06522, '', '', 'ZEROVECS', kind='operand', line=3743)
W('26,2703', 0o00025, '', 'STORE', '20D', 'ZERO OUT 20 TO 25 IN PUSHLIST', kind='interp', line=3744)
W('26,2704', 0o27541, '', 'STOVL', 'BVECTOR +12D', kind='interp', line=3745)
W('26,2705', 0o03525, '', '', 'BVECTOR', kind='operand', line=3746)
W('26,2706', 0o60246, '', 'ABVAL', 'NORM', 'LOAD B0, GET MAGNITUDE AND NORMALIZE', kind='interp', line=3747)
W('26,2707', 0o00025, '', '', '20D', 'SHIFT COUNT IN 20D', kind='operand', line=3748)
# Page 579
W('26,2710', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=3750)
W('26,2711', 0o03533, '', '', 'BVECTOR +6D', 'LOAD B1, GET MAGNITUDE AND NORMALIZE', kind='operand', line=3751)
W('26,2712', 0o71301, '', 'NORM', 'DLOAD', kind='interp', line=3752)
W('26,2713', 0o00027, '', '', '22D', 'SHIFT COUNT IN 22D', kind='operand', line=3753)
W('26,2714', 0o00027, '', '', '22D', 'FIND WHICH SHIFT IS SMALLER', kind='operand', line=3754)
W('26,2715', 0o50025, '', 'DSU', 'BMN', 'BRANCH -- B0 HAS A SMALLER SHIFT COUNT', kind='interp', line=3755)
W('26,2716', 0o00025, '', '', '20D', kind='operand', line=3756)
W('26,2717', 0o54723, '', '', 'VOK1', kind='operand', line=3757)
W('26,2720', 0o52150, '', 'LXA,1', 'GOTO', kind='interp', line=3758)
W('26,2721', 0o00026, '', '', '22D', 'LOAD X2 WITH THE SMALLER SHIFT COUNT', kind='operand', line=3759)
W('26,2722', 0o54725, '', '', 'VOK2', kind='operand', line=3760)
W('26,2723', 0o77750, 'VOK1', 'LXA,1', kind='interp', line=3761)
W('26,2724', 0o00024, '', '', '20D', kind='operand', line=3762)
W('26,2725', 0o53775, 'VOK2', 'VLOAD', 'VSL*', 'THEN ADJUST B0, B1, DELTAQ AND VARIANCE', kind='interp', line=3763)
W('26,2726', 0o03525, '', '', 'BVECTOR', 'WITH THI SSHIFT COUNT', kind='operand', line=3764)
W('26,2727', 0o20201, '', '', '0,1', kind='operand', line=3765)
W('26,2730', 0o27525, '', 'STOVL', 'BVECTOR', kind='interp', line=3766)
W('26,2731', 0o03533, '', '', 'BVECTOR +6', kind='operand', line=3767)
W('26,2732', 0o77657, '', 'VSL*', kind='interp', line=3768)
W('26,2733', 0o20201, '', '', '0,1', kind='operand', line=3769)
W('26,2734', 0o17533, '', 'STODL', 'BVECTOR +6', kind='interp', line=3770)
W('26,2735', 0o03547, '', '', 'DELTAQ', kind='operand', line=3771)
W('26,2736', 0o77657, '', 'SL*', kind='interp', line=3772)
W('26,2737', 0o20201, '', '', '0,1', kind='operand', line=3773)
W('26,2740', 0o03547, '', 'STORE', 'DELTAQ', kind='interp', line=3774)
W('26,2741', 0o53745, '', 'DLOAD', 'SL*', 'GET RLC AND ADJUST FOR SCALE SHIFT', kind='interp', line=3775)
W('26,2742', 0o00045, '', '', '36D', kind='operand', line=3776)
W('26,2743', 0o20200, '', '', '0 -1,1', kind='operand', line=3777)
W('26,2744', 0o41316, '', 'DSQ', 'DMP', 'MULTIPLY RLC**2 BY VARIANCE', kind='interp', line=3778)
W('26,2745', 0o02707, '', '', 'VARIANCE', kind='operand', line=3779)
W('26,2746', 0o47012, '', 'SL4', 'RTB', 'SHIFT TO CONFORM TO BVECTORS AND DELTAQ', kind='interp', line=3780)
W('26,2747', 0o21633, '', '', 'TPMODE', kind='operand', line=3781)
W('26,2750', 0o36707, '', 'STCALL', 'VARIANCE', 'AND STORE TP VARIANCE', kind='interp', line=3782)
W('26,2751', 0o55401, '', '', 'LGCUPDTE', kind='operand', line=3783)

W('26,2752', 0o77624, '', 'CALL', kind='interp', line=3785)
W('26,2753', 0o11244, '', '', 'GRP2PC', kind='operand', line=3786)
W('26,2754', 0o77414, '', 'BON', 'EXIT', 'ARE ANGLES TO BE DONE', kind='interp', line=3787)
W('26,2755', 0o04307, '', '', 'SURFFLAG', kind='operand', line=3788)
W('26,2756', 0o55176, '', '', 'RENDEND', 'NO', kind='operand', line=3789)
#   EBANK= AIG
W('26,2757', 0o33332, 'MXMYMZ', 'CAF', 'AIGBANK', line=3791)
W('26,2760', 0o54006, '', 'TS', 'BBANK', line=3792)
W('26,2761', 0o31457, '', 'CA', 'AIG', 'YES, COMPUTE  MX, MY, MZ', line=3793)
W('26,2762', 0o54766, '', 'TS', 'CDUSPOT', line=3794)
W('26,2763', 0o31460, '', 'CA', 'AMG', line=3795)
W('26,2764', 0o54770, '', 'TS', 'CDUSPOT +2', line=3796)
W('26,2765', 0o31461, '', 'CA', 'AOG', line=3797)
W('26,2766', 0o54772, '', 'TS', 'CDUSPOT +4', 'GIMBAL ANGLES NOW IN CDUSPOT FOR TRG*NBSM', line=3798)
W('26,2767', 0o06037, '', 'TC', 'INTPRET', line=3799)
# Page 580
W('26,2770', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=3801)
W('26,2771', 0o06520, '', '', 'UNITX', kind='operand', line=3802)
W('26,2772', 0o47664, '', '', 'TRG*NBSM', kind='operand', line=3803)
W('26,2773', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=3804)
W('26,2774', 0o01734, '', '', 'REFSMMAT', kind='operand', line=3805)
W('26,2775', 0o27677, '', 'STOVL', 'MX', kind='interp', line=3806)
W('26,2776', 0o06516, '', '', 'UNITY', kind='operand', line=3807)
W('26,2777', 0o77624, '', 'CALL', kind='interp', line=3808)
W('26,3000', 0o47673, '', '', '*NBSM*', kind='operand', line=3809)
W('26,3001', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=3810)
W('26,3002', 0o01734, '', '', 'REFSMMAT', kind='operand', line=3811)
W('26,3003', 0o27705, '', 'STOVL', 'MY', kind='interp', line=3812)
W('26,3004', 0o06514, '', '', 'UNITZ', kind='operand', line=3813)
W('26,3005', 0o77624, '', 'CALL', kind='interp', line=3814)
W('26,3006', 0o47673, '', '', '*NBSM*', kind='operand', line=3815)
W('26,3007', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=3816)
W('26,3010', 0o01734, '', '', 'REFSMMAT', kind='operand', line=3817)
W('26,3011', 0o37713, 'SHAFTBQ', 'STCALL', 'MZ', kind='interp', line=3818)
W('26,3012', 0o55361, '', '', 'RADARANG', kind='operand', line=3819)
W('26,3013', 0o45131, '', 'SSP', 'CALL', 'STORE SHAFT CODE (3) FOR R3 IN NOUN 49', kind='interp', line=3820)
W('26,3014', 0o03746, '', '', 'WHCHREAD', kind='operand', line=3821)
W('26,3015', 0o00003, '', 'DEC', '3', kind='data', line=3822)
W('26,3016', 0o11244, '', '', 'GRP2PC', kind='operand', line=3823)
W('26,3017', 0o50375, '', 'VLOAD', 'DOT', 'COMPUTE DELTAQ,B VECTORS FOR SHAFT ANG.', kind='interp', line=3824)
W('26,3020', 0o03724, '', '', 'ULC', kind='operand', line=3825)
W('26,3021', 0o03677, '', '', 'MX', kind='operand', line=3826)
W('26,3022', 0o77752, '', 'SL1', kind='interp', line=3827)
W('26,3023', 0o24023, '', 'STOVL', 'SINTH', '18D', kind='interp', line=3828)
W('26,3024', 0o03724, '', '', 'ULC', kind='operand', line=3829)
W('26,3025', 0o72441, '', 'DOT', 'SL1', kind='interp', line=3830)
W('26,3026', 0o03713, '', '', 'MZ', kind='operand', line=3831)
W('26,3027', 0o34021, '', 'STCALL', 'COSTH', '16D', kind='interp', line=3832)
W('26,3030', 0o26510, '', '', 'ARCTAN', kind='operand', line=3833)
W('26,3031', 0o41221, '', 'BDSU', 'DMP', kind='interp', line=3834)
W('26,3032', 0o03736, '', '', 'RRSHAFT', kind='operand', line=3835)
W('26,3033', 0o15441, '', '', '2PI/8', kind='operand', line=3836)
W('26,3034', 0o41472, '', 'SL3R', 'PUSH', kind='interp', line=3837)
W('26,3035', 0o52545, '', 'DLOAD', 'SL3', kind='interp', line=3838)
W('26,3036', 0o01701, '', '', 'X789', kind='operand', line=3839)
W('26,3037', 0o44257, '', 'SRR*', 'BDSU', 'SHIFT FROM -5/-3 TO B0', kind='interp', line=3840)
W('26,3040', 0o56176, '', '', '0,2', kind='operand', line=3841)
W('26,3041', 0o53605, '', 'DMP', 'SRR*', kind='interp', line=3842)
W('26,3042', 0o03722, '', '', 'RXZ', kind='operand', line=3843)
W('26,3043', 0o21601, '', '', '0,1', 'SHIFT TO EARTH/MOON SPHERE', kind='operand', line=3844)
W('26,3044', 0o27547, '', 'STOVL', 'DELTAQ', 'EARTH B-29.  MOON B-27', kind='interp', line=3845)
W('26,3045', 0o03724, '', '', 'ULC', kind='operand', line=3846)
W('26,3046', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=3847)
W('26,3047', 0o03705, '', '', 'MY', kind='operand', line=3848)
W('26,3050', 0o77656, '', 'UNIT', kind='interp', line=3849)
W('26,3051', 0o57414, '', 'BOFF', 'VCOMP', 'B0, COMP. IF CSM BEING CORRECTED', kind='interp', line=3850)
# Page 581
W('26,3052', 0o00747, '', '', 'VEHUPFLG', kind='operand', line=3852)
W('26,3053', 0o55054, '', '', '+1', kind='operand', line=3853)
W('26,3054', 0o27525, '', 'STOVL', 'BVECTOR', kind='interp', line=3854)
W('26,3055', 0o06522, '', '', 'ZEROVECS', kind='operand', line=3855)
W('26,3056', 0o03533, '', 'STORE', 'BVECTOR +6', kind='interp', line=3856)
W('26,3057', 0o17541, '', 'STODL', 'BVECTOR +12D', kind='interp', line=3857)
W('26,3060', 0o03722, '', '', 'RXZ', kind='operand', line=3858)
W('26,3061', 0o53657, '', 'SR*', 'SRR*', 'SHIFT FROM EARTH/MOON SPHERE TO B-25', kind='interp', line=3859)
W('26,3062', 0o20577, '', '', '0 -2,1', kind='operand', line=3860)
W('26,3063', 0o56176, '', '', '0,2', kind='operand', line=3861)
W('26,3064', 0o03541, '', 'STORE', 'BVECTOR +12D', kind='interp', line=3862)
W('26,3065', 0o77735, '', 'SLOAD', kind='interp', line=3863)
W('26,3066', 0o02011, '', '', 'SHAFTVAR', kind='operand', line=3864)
W('26,3067', 0o41215, '', 'DAD', 'DMP', kind='interp', line=3865)
W('26,3070', 0o15436, '', '', 'IMUVAR', 'RAD**2 B12', kind='operand', line=3866)
W('26,3071', 0o03722, '', '', 'RXZ', kind='operand', line=3867)
W('26,3072', 0o41257, '', 'SRR*', 'DMP', kind='interp', line=3868)
W('26,3073', 0o21601, '', '', '0,1', 'SHIFT TO EARTH/MOON SPHERE', kind='operand', line=3869)
W('26,3074', 0o03722, '', '', 'RXZ', kind='operand', line=3870)
W('26,3075', 0o53657, '', 'SR*', 'SR*', kind='interp', line=3871)
W('26,3076', 0o20577, '', '', '0 -2,1', kind='operand', line=3872)
W('26,3077', 0o57176, '', '', '0,2', kind='operand', line=3873)
W('26,3100', 0o47057, '', 'SR*', 'RTB', kind='interp', line=3874)
W('26,3101', 0o57176, '', '', '0,2', kind='operand', line=3875)
W('26,3102', 0o21633, '', '', 'TPMODE', 'STORE VARIANCE TRIPLE PRECISION', kind='operand', line=3876)
W('26,3103', 0o36707, '', 'STCALL', 'VARIANCE', 'B-40', kind='interp', line=3877)
W('26,3104', 0o55401, '', '', 'LGCUPDTE', kind='operand', line=3878)

W('26,3105', 0o77624, '', 'CALL', kind='interp', line=3880)
W('26,3106', 0o11244, '', '', 'GRP2PC', kind='operand', line=3881)
W('26,3107', 0o77624, 'TRUNBQ', 'CALL', kind='interp', line=3882)
W('26,3110', 0o55361, '', '', 'RADARANG', kind='operand', line=3883)
W('26,3111', 0o45131, '', 'SSP', 'CALL', 'STORE TRUNNION CODE (4) FOR R3 IN N49', kind='interp', line=3884)
W('26,3112', 0o03746, '', '', 'WHCHREAD', kind='operand', line=3885)
W('26,3113', 0o00004, '', 'DEC', '4', kind='data', line=3886)
W('26,3114', 0o11244, '', '', 'GRP2PC', kind='operand', line=3887)
W('26,3115', 0o47375, '', 'VLOAD', 'VXV', kind='interp', line=3888)
W('26,3116', 0o03724, '', '', 'ULC', kind='operand', line=3889)
W('26,3117', 0o03705, '', '', 'MY', kind='operand', line=3890)
W('26,3120', 0o47372, '', 'VSL1', 'VXV', kind='interp', line=3891)
W('26,3121', 0o03724, '', '', 'ULC', kind='operand', line=3892)
W('26,3122', 0o77772, '', 'VSL1', '', '(ULC X MY) X ULC', kind='interp', line=3893)
W('26,3123', 0o57414, '', 'BOFF', 'VCOMP', 'B0, COMP. IF CSM BEING CORRECTED', kind='interp', line=3894)
W('26,3124', 0o00747, '', '', 'VEHUPFLG', kind='operand', line=3895)
W('26,3125', 0o55126, '', '', '+1', kind='operand', line=3896)
W('26,3126', 0o27525, '', 'STOVL', 'BVECTOR', kind='interp', line=3897)
W('26,3127', 0o06522, '', '', 'ZEROVECS', kind='operand', line=3898)
W('26,3130', 0o03533, '', 'STORE', 'BVECTOR +6', kind='interp', line=3899)
W('26,3131', 0o17541, '', 'STODL', 'BVECTOR +12D', kind='interp', line=3900)
W('26,3132', 0o03722, '', '', 'RXZ', kind='operand', line=3901)
# Page 582
W('26,3133', 0o53657, '', 'SR*', 'SRR*', 'SHIFT FROM EARTH/MOON SPHERE TO B-25', kind='interp', line=3903)
W('26,3134', 0o20577, '', '', '0 -2,1', kind='operand', line=3904)
W('26,3135', 0o56176, '', '', '0,2', kind='operand', line=3905)
W('26,3136', 0o03543, '', 'STORE', 'BVECTOR +14D', kind='interp', line=3906)
W('26,3137', 0o77735, '', 'SLOAD', kind='interp', line=3907)
W('26,3140', 0o02012, '', '', 'TRUNVAR', kind='operand', line=3908)
W('26,3141', 0o41215, '', 'DAD', 'DMP', kind='interp', line=3909)
W('26,3142', 0o15436, '', '', 'IMUVAR', kind='operand', line=3910)
W('26,3143', 0o03722, '', '', 'RXZ', kind='operand', line=3911)
W('26,3144', 0o41257, '', 'SRR*', 'DMP', kind='interp', line=3912)
W('26,3145', 0o21601, '', '', '0,1', 'SHIFT TO EARTH/MOON SPHERE', kind='operand', line=3913)
W('26,3146', 0o03722, '', '', 'RXZ', kind='operand', line=3914)
W('26,3147', 0o53657, '', 'SR*', 'SR*', kind='interp', line=3915)
W('26,3150', 0o20577, '', '', '0 -2,1', kind='operand', line=3916)
W('26,3151', 0o57176, '', '', '0,2', kind='operand', line=3917)
W('26,3152', 0o47057, '', 'SR*', 'RTB', kind='interp', line=3918)
W('26,3153', 0o57176, '', '', '0,2', kind='operand', line=3919)
W('26,3154', 0o21633, '', '', 'TPMODE', 'STORE VARIANCE TRIPLE PRECISION', kind='operand', line=3920)
W('26,3155', 0o16707, '', 'STODL', 'VARIANCE', kind='interp', line=3921)
W('26,3156', 0o03732, '', '', 'SINTHETA', kind='operand', line=3922)
W('26,3157', 0o44336, '', 'ASIN', 'BDSU', 'SIN THETA IN PD6', kind='interp', line=3923)
W('26,3160', 0o03734, '', '', 'RRTRUN', kind='operand', line=3924)
W('26,3161', 0o56405, '', 'DMP', 'SL3R', kind='interp', line=3925)
W('26,3162', 0o15441, '', '', '2PI/8', kind='operand', line=3926)
W('26,3163', 0o52525, '', 'PDDL', 'SL3', kind='interp', line=3927)
W('26,3164', 0o01703, '', '', 'X789 +2', kind='operand', line=3928)
W('26,3165', 0o44257, '', 'SRR*', 'BDSU', 'SHIFT FROM -5/-3 TO B0', kind='interp', line=3929)
W('26,3166', 0o56176, '', '', '0,2', kind='operand', line=3930)
W('26,3167', 0o53605, '', 'DMP', 'SRR*', kind='interp', line=3931)
W('26,3170', 0o03722, '', '', 'RXZ', kind='operand', line=3932)
W('26,3171', 0o21601, '', '', '0,1', kind='operand', line=3933)
W('26,3172', 0o37547, '', 'STCALL', 'DELTAQ', 'EARTH B-29.  MOON B-27', kind='interp', line=3934)
W('26,3173', 0o55401, '', '', 'LGCUPDTE', kind='operand', line=3935)
W('26,3174', 0o77624, '', 'CALL', kind='interp', line=3936)
W('26,3175', 0o11244, '', '', 'GRP2PC', kind='operand', line=3937)
W('26,3176', 0o77650, 'RENDEND', 'GOTO', kind='interp', line=3938)
W('26,3177', 0o50566, '', '', 'R22LEM93', kind='operand', line=3939)

# FUNCTIONAL DESCRIPTION:
# LSR22.4 IS THE ENTRY TO PERFORM LUNAR SURFACE NAVIGATION FOR THE LM
# COMPUTER ONLY.  THIS ROUTINE COMPUTES THE BE-VECTORS AND DELTA Q FOR RANGE
# AND RANGE RATE MEASURED BY THE RENDEZVOUS RADAR
#
# SUBROUTINES CALLED:
# INTSTALL        LGCUPDTE        INCORP1         RP-TO-R
# INTEGRV         GETULC          INCORP2
#
# OUTPUT
# CORRECTED CSM STATE VECTOR (PERMANENT)
# NUMBER OF MARKS INCORPORATED IN MARKCTR
# Page 583
# MAGNITUDE OF POSITION DEVIATION (FOR DISPLAY) IN R22 DISP METERS B-29
# MAGNITUDE OF VELOCITY DEVIATION (FOR DISPLAY) IN R22DISP +2 M/CSEC B-7
# UPDATED W-MATRIX

# ERASABLE INITIALIZATION REQUIRED
# LM AND CSM STATE VECTORS
# W-MATRIX
# MARK TIME IN MKTIME
# RADAR RANGE IN RM METERS B-29
# RANGE RATE IN RDOTM METERS/CSEC B-7
# VEHUPFLG

W('26,3200', 0o77624, 'LSR22.4', 'CALL', kind='interp', line=3966)
W('26,3201', 0o27414, '', '', 'INTSTALL', kind='operand', line=3967)
W('26,3202', 0o43014, '', 'SET', 'CLEAR', kind='interp', line=3968)
W('26,3203', 0o01472, '', '', 'STATEFLG', kind='operand', line=3969)
W('26,3204', 0o01674, '', '', 'VINTFLAG', 'CALL TO GET LM POS + VEL IN REF COORD.', kind='operand', line=3970)
W('26,3205', 0o77624, '', 'CALL', kind='interp', line=3971)
W('26,3206', 0o55242, '', '', 'INTGRCAL', kind='operand', line=3972)
W('26,3207', 0o77624, '', 'CALL', kind='interp', line=3973)
W('26,3210', 0o11244, '', '', 'GRP2PC', kind='operand', line=3974)
W('26,3211', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=3975)
W('26,3212', 0o02666, '', '', 'DMENFLG', 'SET MATRIX SIZE TO 6X6 FOR INCORP', kind='operand', line=3976)
W('26,3213', 0o27414, '', '', 'INTSTALL', kind='operand', line=3977)
W('26,3214', 0o46145, '', 'DLOAD', 'BHIZ', 'IS THIS FIRST TIME THROUGH', kind='interp', line=3978)
W('26,3215', 0o03463, '', '', 'MARKCTR', kind='operand', line=3979)
W('26,3216', 0o55231, '', '', 'INITWMX6', 'YES, INITIALIZE 6X6 W-MATRIX', kind='operand', line=3980)
W('26,3217', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=3981)
W('26,3220', 0o01675, '', '', 'D6OR9FLG', kind='operand', line=3982)
W('26,3221', 0o01476, '', '', 'DIM0FLAG', kind='operand', line=3983)
W('26,3222', 0o43014, '', 'SET', 'CLEAR', kind='interp', line=3984)
W('26,3223', 0o01474, '', '', 'VINTFLAG', kind='operand', line=3985)
W('26,3224', 0o01673, '', '', 'INTYPFLG', kind='operand', line=3986)
W('26,3225', 0o77624, '', 'CALL', kind='interp', line=3987)
W('26,3226', 0o55242, '', '', 'INTGRCAL', kind='operand', line=3988)
W('26,3227', 0o77650, '', 'GOTO', kind='interp', line=3989)
W('26,3230', 0o54510, '', '', 'RANGEBQ', kind='operand', line=3990)

W('26,3231', 0o77624, 'INITWMX6', 'CALL', kind='interp', line=3992)
W('26,3232', 0o55251, '', '', 'WLINIT', 'INITIALIZE W-MATRIX', kind='operand', line=3993)
W('26,3233', 0o45014, '', 'SET', 'CALL', kind='interp', line=3994)
W('26,3234', 0o01474, '', '', 'VINTFLAG', kind='operand', line=3995)
W('26,3235', 0o26644, '', '', 'SETIFLGS', kind='operand', line=3996)
W('26,3236', 0o77624, '', 'CALL', kind='interp', line=3997)
W('26,3237', 0o55242, '', '', 'INTGRCAL', kind='operand', line=3998)
W('26,3240', 0o77650, '', 'GOTO', kind='interp', line=3999)
W('26,3241', 0o54510, '', '', 'RANGEBQ', kind='operand', line=4000)

# THIS ROUTINE CLEARS RFINAL (DP) AND CALLS INTEGRV
# Page 584
W('26,3242', 0o71220, 'INTGRCAL', 'STQ', 'DLOAD', kind='interp', line=4004)
W('26,3243', 0o03675, '', '', 'IGRET', kind='operand', line=4005)
W('26,3244', 0o03755, '', '', 'MKTIME', kind='operand', line=4006)
W('26,3245', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=4007)
W('26,3246', 0o27134, '', '', 'INTEGRV', kind='operand', line=4008)
W('26,3247', 0o77650, '', 'GOTO', kind='interp', line=4009)
W('26,3250', 0o03675, '', '', 'IGRET', kind='operand', line=4010)

# THIS ROUTINE INITIALIZES THE W-MATRIX BY ZEROING ALL W THEN SETTING
# DIAGONAL ELEMENTS TO INITIAL STORED VALUES.

#   EBANK= W
W('26,3251', 0o77776, 'WLINIT', 'EXIT', kind='interp', line=4016)
W('26,3252', 0o33331, '', 'CAF', 'WBANK', line=4017)
W('26,3253', 0o54006, '', 'TS', 'BBANK', line=4018)
W('26,3254', 0o33437, '', 'CAF', 'WSIZE', line=4019)
W('26,3255', 0o55257, '', 'TS', 'W.IND', line=4020)
W('26,3256', 0o34755, '', 'CAF', 'ZERO', line=4021)
W('26,3257', 0o51257, '', 'INDEX', 'W.IND', line=4022)
W('26,3260', 0o55400, '', 'TS', 'W', line=4023)
W('26,3261', 0o11257, '', 'CCS', 'W.IND', line=4024)
W('26,3262', 0o03255, '', 'TC', '-5', line=4025)
W('26,3263', 0o33332, '', 'CAF', 'AIGBANK', 'RESTORE EBANK 7', line=4026)
W('26,3264', 0o54006, '', 'TS', 'BBANK', line=4027)
W('26,3265', 0o06037, '', 'TC', 'INTPRET', line=4028)
W('26,3266', 0o67214, '', 'BON', 'SLOAD', 'IF ON LUNAR SURFACE, INITIALIZE WITH', kind='interp', line=4029)
W('26,3267', 0o04307, '', '', 'SURFFLAG', 'WSURFPOS AND WSURFVEL INSTEAD OF', kind='operand', line=4030)
W('26,3270', 0o55274, '', '', 'WLSRFPOS', 'WRENDPOS AND WRENDVEL', kind='operand', line=4031)
W('26,3271', 0o02001, '', '', 'WRENDPOS', kind='operand', line=4032)
W('26,3272', 0o77650, '', 'GOTO', kind='interp', line=4033)
W('26,3273', 0o55276, '', '', 'WPOSTORE', kind='operand', line=4034)
W('26,3274', 0o77735, 'WLSRFPOS', 'SLOAD', kind='interp', line=4035)
W('26,3275', 0o02007, '', '', 'WSURFPOS', kind='operand', line=4036)
W('26,3276', 0o77661, 'WPOSTORE', 'SR', '', 'SHIFT TO B-19 SCALE', kind='interp', line=4037)
W('26,3277', 0o20606, '', '', '5', kind='operand', line=4038)
W('26,3300', 0o02401, '', 'STORE', 'W', kind='interp', line=4039)
W('26,3301', 0o02411, '', 'STORE', 'W +8D', kind='interp', line=4040)
W('26,3302', 0o02421, '', 'STORE', 'W +16D', kind='interp', line=4041)
W('26,3303', 0o67214, '', 'BON', 'SLOAD', kind='interp', line=4042)
W('26,3304', 0o04307, '', '', 'SURFFLAG', kind='operand', line=4043)
W('26,3305', 0o55311, '', '', 'WLSRFVEL', kind='operand', line=4044)
W('26,3306', 0o02002, '', '', 'WRENDVEL', kind='operand', line=4045)
W('26,3307', 0o77650, '', 'GOTO', kind='interp', line=4046)
W('26,3310', 0o55313, '', '', 'WVELSTOR', kind='operand', line=4047)
W('26,3311', 0o77735, 'WLSRFVEL', 'SLOAD', kind='interp', line=4048)
W('26,3312', 0o02010, '', '', 'WSURFVEL', kind='operand', line=4049)
W('26,3313', 0o02511, 'WVELSTOR', 'STORE', 'W +72D', kind='interp', line=4050)
W('26,3314', 0o02521, '', 'STORE', 'W +80D', kind='interp', line=4051)
W('26,3315', 0o02531, '', 'STORE', 'W +88D', kind='interp', line=4052)
W('26,3316', 0o77735, '', 'SLOAD', kind='interp', line=4053)
# Page 585
W('26,3317', 0o02003, '', '', 'WSHAFT', kind='operand', line=4055)
W('26,3320', 0o02621, '', 'STORE', 'W +144D', kind='interp', line=4056)
W('26,3321', 0o77735, '', 'SLOAD', kind='interp', line=4057)
W('26,3322', 0o02004, '', '', 'WTRUN', kind='operand', line=4058)
W('26,3323', 0o02631, '', 'STORE', 'W +152D', kind='interp', line=4059)
W('26,3324', 0o66214, '', 'SET', 'SSP', 'SET RENDWFLG -- W-MATRIX VALID', kind='interp', line=4060)
W('26,3325', 0o02476, '', '', 'RENDWFLG', kind='operand', line=4061)
W('26,3326', 0o03463, '', '', 'MARKCTR', 'SET MARK COUNTER EQUAL ZERO', kind='operand', line=4062)
W('26,3327', 0o00000, '', '', '0', kind='operand', line=4063)
W('26,3330', 0o77616, '', 'RVQ', kind='interp', line=4064)

#   EBANK= W
W('26,3331', 0o54065, 'WBANK', 'BBCON', 'WLINIT', kind='data', line=4067)
#   EBANK= AIG
W('26,3332', 0o54067, 'AIGBANK', 'BBCON', 'LSR22.3', kind='data', line=4069)

# GETULC
#
# THIS SUBROUTINE COMPUTES THE RELATIVE POSITION VECTOR BETWEEN THE CSM
# AND THE LM, LEAVING THE UNIT VECTOR IN THE PUSHLIST AND MPAC AND THE
# MAGNITUDE IN 36D.

W('26,3333', 0o77201, 'GETULC', 'SETPD', 'VLOAD', kind='interp', line=4077)
W('26,3334', 0o00001, '', '', '0', kind='operand', line=4078)
W('26,3335', 0o01645, '', '', 'DELTALEM', kind='operand', line=4079)
W('26,3336', 0o77754, '', 'LXA,2', kind='interp', line=4080)
W('26,3337', 0o03720, '', '', 'SCALSHFT', 'LOAD X2 WITH SCALE SHIFT', kind='operand', line=4081)
W('26,3340', 0o53257, '', 'VSR*', 'VAD', kind='interp', line=4082)
W('26,3341', 0o57165, '', '', '9D,2', 'SHIFT FOR EARTH/MOON SPHERE', kind='operand', line=4083)
W('26,3342', 0o01661, '', '', 'RCVLEM', kind='operand', line=4084)
W('26,3343', 0o53715, '', 'PDVL', 'VSR*', kind='interp', line=4085)
W('26,3344', 0o01573, '', '', 'DELTACSM', kind='operand', line=4086)
W('26,3345', 0o57165, '', '', '9D,2', 'SHIFT FOR EARTH/MOON SPHERE', kind='operand', line=4087)
W('26,3346', 0o52255, '', 'VAD', 'VSU', kind='interp', line=4088)
W('26,3347', 0o01607, '', '', 'RCVCSM', kind='operand', line=4089)
W('26,3350', 0o41434, '', 'RTB', 'PUSH', 'USE NORMUNIT TO PRESERVE ACCURACY', kind='interp', line=4090)
W('26,3351', 0o21724, '', '', 'NORMUNX1', kind='operand', line=4091)
W('26,3352', 0o17724, '', 'STODL', 'ULC', kind='interp', line=4092)
W('26,3353', 0o00045, '', '', '36D', kind='operand', line=4093)
W('26,3354', 0o77657, '', 'SL*', '', 'ADJUST MAGNITUDE FROM NORMUNIT', kind='interp', line=4094)
W('26,3355', 0o20201, '', '', '0,1', kind='operand', line=4095)
W('26,3356', 0o24045, '', 'STOVL', '36D', 'ULC IN PD0 AND MPAC,RLC IN 36D', kind='interp', line=4096)
W('26,3357', 0o03724, '', '', 'ULC', kind='operand', line=4097)
W('26,3360', 0o77616, '', 'RVQ', kind='interp', line=4098)

# RADARANG
#
# THIS SUBROUTINE COMPUTS SINTHETA = -ULC DOT MY
# RXZ = (SQRT (1-SINTHETA**2))RLC
# OUTPUT
# ULC IN ULC, PD0
# Page 586
# RLC IN PD36D
# SIN THETA IN SINTHETA AND PD6
# RXZ NORM IN RXZ (N IN X1)

W('26,3361', 0o45020, 'RADARANG', 'STQ', 'CALL', kind='interp', line=4111)
W('26,3362', 0o03675, '', '', 'RDRET', kind='operand', line=4112)
W('26,3363', 0o55333, '', '', 'GETULC', kind='operand', line=4113)
W('26,3364', 0o50276, '', 'VCOMP', 'DOT', kind='interp', line=4114)
W('26,3365', 0o03705, '', '', 'MY', kind='operand', line=4115)
W('26,3366', 0o41572, '', 'SL1R', 'PUSH', 'SIN THETA TO PD6', kind='interp', line=4116)
W('26,3367', 0o03732, '', 'STORE', 'SINTHETA', kind='interp', line=4117)
W('26,3370', 0o44316, '', 'DSQ', 'BDSU', kind='interp', line=4118)
W('26,3371', 0o06512, '', '', 'DP1/4TH', '1-(SIN THETA)**2', kind='operand', line=4119)
W('26,3372', 0o41366, '', 'SQRT', 'DMP', kind='interp', line=4120)
W('26,3373', 0o00045, '', '', '36D', kind='operand', line=4121)
W('26,3374', 0o60352, '', 'SL1', 'NORM', kind='interp', line=4122)
W('26,3375', 0o00047, '', '', 'X1', 'SET SHIFT COUNTER IN X1', kind='operand', line=4123)
W('26,3376', 0o03722, '', 'STORE', 'RXZ', kind='interp', line=4124)
W('26,3377', 0o77650, '', 'GOTO', '', 'EXIT', kind='interp', line=4125)
W('26,3400', 0o03675, '', '', 'RDRET', kind='operand', line=4126)
W('26,3401', 0o45020, 'LGCUPDTE', 'STQ', 'CALL', kind='interp', line=4127)
W('26,3402', 0o03675, '', '', 'LGRET', kind='operand', line=4128)
W('26,3403', 0o46531, '', '', 'INCORP1', kind='operand', line=4129)
W('26,3404', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=4130)
W('26,3405', 0o02673, '', '', 'DELTAX +6', kind='operand', line=4131)
W('26,3406', 0o53754, '', 'LXA,2', 'SRR*', kind='interp', line=4132)
W('26,3407', 0o03720, '', '', 'SCALSHFT', '0 -- MOON.  2 -- EARTH', kind='operand', line=4133)
W('26,3410', 0o56174, '', '', '2,2', 'SET VEL DISPLAY TO B-7', kind='operand', line=4134)
W('26,3411', 0o24317, '', 'STOVL', 'R22DISP +2', kind='interp', line=4135)
W('26,3412', 0o02665, '', '', 'DELTAX', kind='operand', line=4136)
W('26,3413', 0o53646, '', 'ABVAL', 'SRR*', kind='interp', line=4137)
W('26,3414', 0o56174, '', '', '2,2', 'SET POS DISPLAY TO B-29', kind='operand', line=4138)
W('26,3415', 0o00315, '', 'STORE', 'R22DISP', kind='interp', line=4139)
W('26,3416', 0o54335, '', 'SLOAD', 'SR', kind='interp', line=4140)
W('26,3417', 0o02005, '', '', 'RMAX', kind='operand', line=4141)
W('26,3420', 0o20613, '', '', '10D', kind='operand', line=4142)
W('26,3421', 0o50025, '', 'DSU', 'BMN', kind='interp', line=4143)
W('26,3422', 0o00315, '', '', 'R22DISP', kind='operand', line=4144)
W('26,3423', 0o50572, '', '', 'R22LEM96', 'GO DISPLAY', kind='operand', line=4145)
W('26,3424', 0o45335, '', 'SLOAD', 'DSU', kind='interp', line=4146)
W('26,3425', 0o02006, '', '', 'VMAX', kind='operand', line=4147)
W('26,3426', 0o00317, '', '', 'R22DISP +2', 'VMAX MINUS VEL. DEVIATION', kind='operand', line=4148)
W('26,3427', 0o77640, '', 'BMN', kind='interp', line=4149)
W('26,3430', 0o50572, '', '', 'R22LEM96', 'GO DISPLAY', kind='operand', line=4150)
W('26,3431', 0o77624, 'ASTOK', 'CALL', kind='interp', line=4151)
W('26,3432', 0o46743, '', '', 'INCORP2', kind='operand', line=4152)
W('26,3433', 0o77650, '', 'GOTO', kind='interp', line=4153)
W('26,3434', 0o03675, '', '', 'LGRET', kind='operand', line=4154)
W('26,3435', 0o00103, 'IMUVAR', '2DEC', 'E-6 B12', 'RAD**2', kind='data', line=4155)
W('26,3436', 0o03370, kind='data', line=4155)

W('26,3437', 0o00241, 'WSIZE', 'DEC', '161', kind='data', line=4157)
# Page 587
W('26,3440', 0o31103, '2PI/8', '2DEC', '3.141592653 B-2', kind='data', line=4159)
W('26,3441', 0o36652, kind='data', line=4159)

#   EBANK= LOSCOUNT
# Page 588

# PROGRAM NAME LRS24.1          RR SEARCH ROUTINE
# MCD NO. 0                     BY P. VOLANTE, SDC              DATE 1-15-67
#
# FUNCTIONAL DESCRIPTION
#
# DRIVES THE RENDEZVOUS RADAR IN A HEXAGONAL SEARCH PATTERN ABOUT THE LOS TO THE CSM (COMPUTED FROM THE CSM AND LM
# STATE VECTORS) CHECKING FOR THE DATA GOOD DISCRETE AND MONITORING THE ANGLE BETWEEN THE RADAR BORESIGHT AND THE
# LM +Z AXIS.  IF THIS ANGLE EXCEEDS 30 DEGREES THE PREFERRED TRACKING ATTITUDE ROUTINE IS CALLED TO PERFORM AN
# ATTITUDE MANEUVER.
#
# CALLING SEQUENCE -- BANKCALL FOR LRS24.1
#
# SUBROUTINES CALLED
#
# LEMCONIC        R61LEM
# CSMCONIC        RRDESSM
# JOBDELAY        FLAGDOWN
# WAITLIST        FLAGUP
# RRNB            BANKCALL
#
# EXIT -- TO ENDOFJOB WHEN THE SEARCH FLAG (SRCHOPT) IS NOT SET
#
# OUTPUT
#
# DATAGOOD (SP) -- FOR DISPLAY IN R1 --   00000 INDICATES NO LOCKON
# 11111 INDICATES LOCKON ACHIEVED
# OMEGAD (SP)   -- FOR DISPLAY IN R2 --   ANGLE BETWEEN RR BORESIGNT VECTOR AND THE SPACECRAFT +Z AXIS
#
# ERASABLE INITIALIZATION REQUIRED:
#
# SEARCH FLAG MUST BE SET
# LM AND CSM STATE VECTORS AND REFSMMAT MATRIX
#
# DEBRIS
#
# RLMSRCH         UXVECT
# VXRLM           UYVECT
# LOSDESRD        NSRCHPNT
# DATAGOOD        OMEGAD
# MPAC            PUSHLIST

#   COUNT* $$/LRS24
W('26,3442', 0o34755, 'LRS24.1', 'CAF', 'ZERO', line=4206)
W('26,3443', 0o55736, '', 'TS', 'NSRCHPNT', 'SET SEARCH PATTERN POINT COUNTER TO ZERO', line=4207)
W('26,3444', 0o34736, 'CHKSRCH', 'CAF', 'BIT14', 'ISSUE AUTO TRACK ENABLE TO RADAR', line=4208)
W('26,3445', 0o00006, '', 'EXTEND', line=4209)
# Page 589
W('26,3446', 0o05012, '', 'WOR', 'CHAN12', line=4211)
W('26,3447', 0o34736, '', 'CAF', 'SRCHOBIT', 'CHECK IF SEARCH STILL REQUESTED', line=4212)
W('26,3450', 0o70076, '', 'MASK', 'FLAGWRD2', '(SRCHOPT FLAG SET)', line=4213)
W('26,3451', 0o00006, '', 'EXTEND', line=4214)
W('26,3452', 0o15155, '', 'BZF', 'ENDOFJOB', 'NO-TERMINATE JOB', line=4215)

W('26,3453', 0o33713, '', 'CAF', '6SECONDS', 'SCHEDULE TASK TO DRIVE RADAR TO NEXT PT.', line=4217)
W('26,3454', 0o00004, '', 'INHINT', line=4218)
W('26,3455', 0o05203, '', 'TC', 'WAITLIST', 'IN 6 SECONDS', line=4219)
#   EBANK= LOSCOUNT
W('26,3456', 0o03643, '', '2CADR', 'CALLDGCH', kind='data', line=4221)
W('26,3457', 0o54067, kind='data', line=4221)

W('26,3460', 0o00003, '', 'RELINT', line=4223)
W('26,3461', 0o40110, '', 'CS', 'RADMODES', 'IS REMODE IN PROGRESS', line=4224)
W('26,3462', 0o74736, '', 'MASK', 'REMODBIT', line=4225)
W('26,3463', 0o00006, '', 'EXTEND', line=4226)
W('26,3464', 0o15155, '', 'BZF', 'ENDOFJOB', 'YES -- WAIT SIX SECONDS', line=4227)
W('26,3465', 0o06037, '', 'TC', 'INTPRET', line=4228)

W('26,3466', 0o43234, '', 'RTB', 'DAD', 'COMPUTE LOS AT PRESENT TIME + 1.5 SEC.', kind='interp', line=4230)
W('26,3467', 0o21573, '', '', 'LOADTIME', kind='operand', line=4231)
W('26,3470', 0o15715, '', '', '1.5SECS', kind='operand', line=4232)
W('26,3471', 0o34041, 'LRS24.11', 'STCALL', 'TDEC1', kind='interp', line=4233)
W('26,3472', 0o27100, '', '', 'LEMCONIC', 'EXTRAPOLATE LM STATE VECTOR', kind='operand', line=4234)
W('26,3473', 0o77775, '', 'VLOAD', kind='interp', line=4235)
W('26,3474', 0o00001, '', '', 'RATT', kind='operand', line=4236)
W('26,3475', 0o27676, '', 'STOVL', 'RLMSRCH', 'SAVE LEM POSITION', kind='interp', line=4237)
W('26,3476', 0o00007, '', '', 'VATT', kind='operand', line=4238)
W('26,3477', 0o17740, '', 'STODL', 'SAVLEMV', 'SAVE LEM VELOCITY', kind='interp', line=4239)
W('26,3500', 0o00015, '', '', 'TAT', kind='operand', line=4240)
W('26,3501', 0o34041, '', 'STCALL', 'TDEC1', 'EXTRAPOLATE CSM STATE VECTOR', kind='interp', line=4241)
W('26,3502', 0o27066, '', '', 'CSMCONIC', 'EXTRAPOLATE CSM STATE VECTOR', kind='operand', line=4242)
W('26,3503', 0o52375, '', 'VLOAD', 'VSU', 'LOS VECTOR = R(CSM) - R(LM)', kind='interp', line=4243)
W('26,3504', 0o00001, '', '', 'RATT', kind='operand', line=4244)
W('26,3505', 0o03676, '', '', 'RLMSRCH', kind='operand', line=4245)
W('26,3506', 0o77656, '', 'UNIT', kind='interp', line=4246)
W('26,3507', 0o27712, '', 'STOVL', 'LOSDESRD', 'STORE DESIRED LOS', kind='interp', line=4247)
W('26,3510', 0o00007, '', '', 'VATT', 'COMPUTE UNIT(V(CM) CROSS R(CM))', kind='operand', line=4248)
W('26,3511', 0o47256, '', 'UNIT', 'VXV', kind='interp', line=4249)
W('26,3512', 0o00001, '', '', 'RATT', kind='operand', line=4250)
W('26,3513', 0o77656, '', 'UNIT', kind='interp', line=4251)
W('26,3514', 0o03704, '', 'STORE', 'VXRCM', kind='interp', line=4252)
W('26,3515', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=4253)
W('26,3516', 0o00007, '', '', 'VATT', kind='operand', line=4254)
W('26,3517', 0o03740, '', '', 'SAVLEMV', kind='operand', line=4255)
W('26,3520', 0o76521, '', 'MXV', 'VSL1', 'CONVERT FROM REFERENCE TO STABLE MEMBER', kind='interp', line=4256)
W('26,3521', 0o01734, '', '', 'REFSMMAT', kind='operand', line=4257)
W('26,3522', 0o03740, '', 'STORE', 'SAVLEMV', 'VLC = V(CSM) - V(LM)', kind='interp', line=4258)
W('26,3523', 0o53135, '', 'SLOAD', 'BZE', 'CHECK IF N=0', kind='interp', line=4259)
# Page 590
W('26,3524', 0o03737, '', '', 'NSRCHPNT', kind='operand', line=4261)
W('26,3525', 0o55636, '', '', 'DESGLOS', 'YES -- DESIGNATE ALONG LOS', kind='operand', line=4262)
W('26,3526', 0o53025, '', 'DSU', 'BZE', 'IS N=1', kind='interp', line=4263)
W('26,3527', 0o15711, '', '', 'ONEOCT', 'YES -- CALCULATE X AND Y AXES OF', kind='operand', line=4264)
W('26,3530', 0o55623, '', '', 'CALCXY', 'SEARCH PATTERN COORDINATE SYSTEM', kind='operand', line=4265)
W('26,3531', 0o77775, '', 'VLOAD', '', 'NO -- ROTATE X-Y AXES TO NEXT SEARCH POINT', kind='interp', line=4266)
W('26,3532', 0o03720, '', '', 'UXVECT', kind='operand', line=4267)
W('26,3533', 0o24015, '', 'STOVL', 'UXVECTPR', 'SAVE ORIGINAL X AND Y VECTORS', kind='interp', line=4268)
W('26,3534', 0o03726, '', '', 'UYVECT', 'UXPRIME = ORIGINAL UX', kind='operand', line=4269)
W('26,3535', 0o00023, '', 'STORE', 'UYVECTPR', 'UYPRIME = ORIGINAL UY', kind='interp', line=4270)
W('26,3536', 0o77761, '', 'VXSC', kind='interp', line=4271)
W('26,3537', 0o15705, '', '', 'SIN60DEG', 'UX = (COS 60)UXPR + (SIN 60)UYPR', kind='operand', line=4272)
W('26,3540', 0o27720, '', 'STOVL', 'UXVECT', kind='interp', line=4273)
W('26,3541', 0o00015, '', '', 'UXVECTPR', kind='operand', line=4274)
W('26,3542', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=4275)
W('26,3543', 0o06520, '', '', 'COS60DEG', kind='operand', line=4276)
W('26,3544', 0o03720, '', '', 'UXVECT', kind='operand', line=4277)
W('26,3545', 0o77656, '', 'UNIT', kind='interp', line=4278)
W('26,3546', 0o27720, '', 'STOVL', 'UXVECT', kind='interp', line=4279)
W('26,3547', 0o00015, '', '', 'UXVECTPR', 'UY = (-SIN 60)UXPR + (COS 60)UYPR', kind='operand', line=4280)
W('26,3550', 0o77761, '', 'VXSC', kind='interp', line=4281)
W('26,3551', 0o15705, '', '', 'SIN60DEG', kind='operand', line=4282)
W('26,3552', 0o27726, '', 'STOVL', 'UYVECT', kind='interp', line=4283)
W('26,3553', 0o00023, '', '', 'UYVECTPR', kind='operand', line=4284)
W('26,3554', 0o52361, '', 'VXSC', 'VSU', kind='interp', line=4285)
W('26,3555', 0o06520, '', '', 'COS60DEG', kind='operand', line=4286)
W('26,3556', 0o03726, '', '', 'UYVECT', kind='operand', line=4287)
W('26,3557', 0o77656, '', 'UNIT', kind='interp', line=4288)
W('26,3560', 0o03726, '', 'STORE', 'UYVECT', kind='interp', line=4289)
W('26,3561', 0o53361, 'OFFCALC', 'VXSC', 'VAD', 'OFFSET VECTOR = K(UY)', kind='interp', line=4290)
W('26,3562', 0o15707, '', '', 'OFFSTFAC', 'LOS VECTOR + OFFSET VECTOR DEFINES', kind='operand', line=4291)
W('26,3563', 0o03712, '', '', 'LOSDESRD', 'DESIRED POINT IN SEARCH PATTERN', kind='operand', line=4292)
W('26,3564', 0o64256, '', 'UNIT', 'MXV', kind='interp', line=4293)
W('26,3565', 0o01734, '', '', 'REFSMMAT', 'CONVERT TO STABLE MEMBER COORDINATES', kind='operand', line=4294)
W('26,3566', 0o77772, '', 'VSL1', kind='interp', line=4295)
W('26,3567', 0o25102, 'CONTDESG', 'STOVL', 'RRTARGET', kind='interp', line=4296)
W('26,3570', 0o03740, '', '', 'SAVLEMV', kind='operand', line=4297)
W('26,3571', 0o01761, '', 'STORE', 'LOSVEL', kind='interp', line=4298)
W('26,3572', 0o77776, '', 'EXIT', kind='interp', line=4299)
W('26,3573', 0o00004, '', 'INHINT', line=4300)
W('26,3574', 0o06027, '', 'TC', 'KILLTASK', 'KILL ANY PRESENTLY WAITLISTED TASK', line=4301)
W('26,3575', 0o52602, '', 'CADR', 'DESLOOP +2', 'WHICH WOULD DESIGNATE TO THE LAST', kind='data', line=4302)
# POINT IN THE PATTERN
W('26,3576', 0o44735, 'CONTDES2', 'CS', 'CDESBIT', line=4304)
W('26,3577', 0o70110, '', 'MASK', 'RADMODES', 'SET BIT 15 OF RADMODES TO INDICATE', line=4305)
W('26,3600', 0o64735, '', 'AD', 'CDESBIT', 'A CONTINUOUS DESIGNATE WANTED.', line=4306)
W('26,3601', 0o54110, '', 'TS', 'RADMODES', line=4307)
W('26,3602', 0o06037, '', 'TC', 'INTPRET', line=4308)

W('26,3603', 0o77624, '', 'CALL', kind='interp', line=4310)
# Page 591
W('26,3604', 0o52373, '', '', 'RRDESSM', 'DESIGNATE RADAR TO RRTARGET VECTOR', kind='operand', line=4312)

W('26,3605', 0o77776, '', 'EXIT', kind='interp', line=4314)
W('26,3606', 0o03675, '', 'TC', 'LIMALARM', 'LOS NOT IN MODE 2 COVERAGE (P22)', line=4315)
W('26,3607', 0o03675, '', 'TC', 'LIMALARM', 'VEHICLE MANEUVER REQUIRED (P20)', line=4316)

# COMPUTE OMEGA,ANGLE BETWEEN RR LOS AND
# SPACECRAFT +Z AXIS
W('26,3610', 0o00006, 'OMEGCALC', 'EXTEND', line=4320)
W('26,3611', 0o30036, '', 'DCA', 'CDUT', line=4321)
W('26,3612', 0o53753, '', 'DXCH', 'TANGNB', line=4322)
W('26,3613', 0o06037, '', 'TC', 'INTPRET', line=4323)
W('26,3614', 0o77624, '', 'CALL', kind='interp', line=4324)
W('26,3615', 0o46041, '', '', 'RRNB', kind='operand', line=4325)
W('26,3616', 0o65545, '', 'DLOAD', 'ACOS', 'OMEGA IS ARCCOSINE OF Z-COMPONENT OF', kind='interp', line=4326)
W('26,3617', 0o00045, '', '', '36D', 'VECTOR COMPUTED BY RRNB (LEFT AT 32D)', kind='operand', line=4327)
W('26,3620', 0o03735, '', 'STORE', 'OMEGDISP', 'STORE FOR DISPLAY IN R2', kind='interp', line=4328)
W('26,3621', 0o77776, '', 'EXIT', kind='interp', line=4329)
W('26,3622', 0o05155, '', 'TC', 'ENDOFJOB', line=4330)
# Page 592
# CALCULATE X AND Y VECTORS FOR SEARCH PATTERN COORDINATE SYSTEM.

W('26,3623', 0o47375, 'CALCXY', 'VLOAD', 'VXV', kind='interp', line=4334)
W('26,3624', 0o03704, '', '', 'VXRCM', kind='operand', line=4335)
W('26,3625', 0o03712, '', '', 'LOSDESRD', kind='operand', line=4336)
W('26,3626', 0o77656, '', 'UNIT', kind='interp', line=4337)
W('26,3627', 0o27720, '', 'STOVL', 'UXVECT', 'UX = (VLM X RLM) X LOS', kind='interp', line=4338)
W('26,3630', 0o03712, '', '', 'LOSDESRD', kind='operand', line=4339)
W('26,3631', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=4340)
W('26,3632', 0o03720, '', '', 'UXVECT', kind='operand', line=4341)
W('26,3633', 0o03726, '', 'STORE', 'UYVECT', 'UY = LOS X UX', kind='interp', line=4342)
W('26,3634', 0o77650, '', 'GOTO', kind='interp', line=4343)
W('26,3635', 0o55561, '', '', 'OFFCALC', kind='operand', line=4344)

W('26,3636', 0o64375, 'DESGLOS', 'VLOAD', 'MXV', 'WHEN N= 0,DESIGNATE ALONG LOS', kind='interp', line=4346)
W('26,3637', 0o03712, '', '', 'LOSDESRD', kind='operand', line=4347)
W('26,3640', 0o01734, '', '', 'REFSMMAT', 'CONVERT LOS FROM REFERENCE TO SM COORDS', kind='operand', line=4348)
W('26,3641', 0o52172, '', 'VSL1', 'GOTO', kind='interp', line=4349)
W('26,3642', 0o55567, '', '', 'CONTDESG', kind='operand', line=4350)

W('26,3643', 0o30074, 'CALLDGCH', 'CAE', 'FLAGWRD0', 'IS RENDEZVOUS FLAG SET', line=4352)
W('26,3644', 0o74745, '', 'MASK', 'RNDVZBIT', line=4353)
W('26,3645', 0o00006, '', 'EXTEND', line=4354)
W('26,3646', 0o15261, '', 'BZF', 'TASKOVER', 'NO -- EXIT R24', line=4355)
W('26,3647', 0o37713, '', 'CAF', 'PRIO25', 'YES -- SCHEDULE JOB TO DRIVE RADAR TO NEXT', line=4356)
W('26,3650', 0o05105, '', 'TC', 'FINDVAC', 'PONT IN SEARCH PATTERN', line=4357)
#   EBANK= RLMSRCH
W('26,3651', 0o03654, '', '2CADR', 'DATGDCHK', kind='data', line=4359)
W('26,3652', 0o54067, kind='data', line=4359)

W('26,3653', 0o05261, '', 'TC', 'TASKOVER', line=4361)

W('26,3654', 0o34750, 'DATGDCHK', 'CAF', 'BIT4', line=4363)
W('26,3655', 0o00006, '', 'EXTEND', '', 'CHECK IF DATA GOOD DISCRETE PRESENT', line=4364)
W('26,3656', 0o02033, '', 'RAND', 'CHAN33', line=4365)
W('26,3657', 0o00006, '', 'EXTEND', line=4366)
W('26,3660', 0o13667, '', 'BZF', 'STORE1S', 'YES -- GO TO STORE 11111 FOR DISPLAY IN R1', line=4367)
W('26,3661', 0o46242, '', 'CS', 'SIX', line=4368)
W('26,3662', 0o61736, '', 'AD', 'NSRCHPNT', 'IS N GREATER THAN 6', line=4369)
W('26,3663', 0o00006, '', 'EXTEND', line=4370)
W('26,3664', 0o13442, '', 'BZF', 'LRS24.1', 'YES -- RESET N = 0 AND START AROUND AGAIN', line=4371)
W('26,3665', 0o25736, '', 'INCR', 'NSRCHPNT', 'NO -- SET N = N+1 AND GO TO', line=4372)
W('26,3666', 0o13444, '', 'TCF', 'CHKSRCH', 'NEXT POINT IN PATTERN', line=4373)

W('26,3667', 0o33703, 'STORE1S', 'CAF', 'ALL1S', 'STORE 11111 FOR DISPLAY IN R1', line=4375)
W('26,3670', 0o55733, '', 'TS', 'DATAGOOD', line=4376)
# Page 593
W('26,3671', 0o00004, '', 'INHINT', line=4378)
W('26,3672', 0o06027, '', 'TC', 'KILLTASK', 'DELETE DESIGNATE TASK FROM', line=4379)
W('26,3673', 0o52602, '', 'CADR', 'DESLOOP +2', 'WAITLIST USING KILLTASK', kind='data', line=4380)
W('26,3674', 0o05155, '', 'TC', 'ENDOFJOB', line=4381)

W('26,3675', 0o05567, 'LIMALARM', 'TC', 'ALARM', 'ISSUE ALARM 527 -- LOS NOT IN MODE2', line=4383)
W('26,3676', 0o00527, '', 'OCT', '527', 'COVERAGE IN P22 OR VEHICLE MANEUVER', kind='data', line=4384)
W('26,3677', 0o00004, '', 'INHINT', '', 'REQUIRED IN P20', line=4385)
W('26,3700', 0o06027, '', 'TC', 'KILLTASK', 'KILL WAITLIST CALL FOR NEXT', line=4386)
W('26,3701', 0o55643, '', 'CADR', 'CALLDGCH', 'POINT IN SEARCH PATTERN', kind='data', line=4387)
W('26,3702', 0o05155, '', 'TC', 'ENDOFJOB', line=4388)

W('26,3703', 0o25547, 'ALL1S', 'DEC', '11111', kind='data', line=4390)
W('26,3704', 0o33555, 'SIN60DEG', '2DEC', '.86603', kind='data', line=4391)
W('26,3705', 0o01106, kind='data', line=4391)
S('COS60DEG', 'equals', 0o56517, line=4392)  # (2DEC .50)
S('UXVECTPR', 'equals', 0o14, line=4393)  # PREVIOUS
S('UYVECTPR', 'equals', 0o22, line=4394)
S('RLMUNIT', 'equals', 0o14, line=4395)
W('26,3706', 0o01642, 'OFFSTFAC', '2DEC', '0.05678', 'TANGENT OF 3.25 DEGREES', kind='data', line=4396)
W('26,3707', 0o11045, kind='data', line=4396)

W('26,3710', 0o00001, 'ONEOCT', 'OCT', '00001', '**** NOTE -- THESE TWO CONSTANTS MUST ****', kind='data', line=4398)
W('26,3711', 0o00000, '3SECONDS', '2DEC', '300', '**** BE IN THIS ORDER BECAUSE         ****', kind='data', line=4399)
W('26,3712', 0o00454, kind='data', line=4399)

# **** ONEOCT NEEDS A LOWER ORDER       ****
# **** WORD OF ZEROES                   ****
W('26,3713', 0o01130, '6SECONDS', 'DEC', '600', kind='data', line=4403)
W('26,3714', 0o00000, '1.5SECS', '2DEC', '150', kind='data', line=4404)
W('26,3715', 0o00226, kind='data', line=4404)

S('ZERO/SP', 'equals', 0o56521, line=4406)

#   BLOCK 02
#   SETLOC FFTAG5
#   BANK
#   COUNT* $$/P20
W('6022', 0o00006, 'GOTOV56', 'EXTEND', '', 'P20 TERMINATES BY GOTOV56 INSTEAD OF', line=4412)
W('6023', 0o36026, '', 'DCA', 'VB56CADR', 'GOTOPOOH', line=4413)
W('6024', 0o15165, '', 'TCF', 'SUPDXCHZ', line=4414)
#   EBANK= WHOCARES
W('6025', 0o03024, 'VB56CADR', '2CADR', 'TRMTRACK', kind='data', line=4416)
W('6026', 0o66107, kind='data', line=4416)

# Page 594
# PROGRAM NAME: R29     (RENDEZVOUS RADAR DESIGNATE DURING POWERED FLIGHT)
# MOD NO. 2     BY H. BLAIR-SMITH       JULY 2, 1968
#
# FUNCTIONAL DESCRIPTION:
#
# DESIGNATES THE RENDEZVOUS RADAR TOWARD THE COMPUTES LOS TO THE CSM, WITH THE CHIEF OBJECTIVE OF OBTAINING RANGE
# AND RANGE RATE DATA AT 2-SECOND INTERVALS FOR TRANSMISSION TO THE GROUND.  WHEN THE RR IS WITHIN .5 DEGREE OF
# THE COMPUTED LOS, TRACKING IS ENABLED, AND DESIGNATION CONTINUES UNTIL THE DATA-GOOD DISCRETE IS RECEIVED.  AT
# THAT POINT, DESIGNATION CEASES AND A RADAR-READING ROUTINE TAKES OVER, PREPARING A CONSISTENT SET OF DATA FOR
# DOWN TELEMETRY.  THE SET INCLUDES RANGE, RANGE RATE, MARK TIME, TWO RR CDU ANGLES, THREE IMUCDU ANGLES, AND AN
# INDICATOR WHICH IS 1 WHEN THE SET IS CONSISTENT AND 0 OTHERWISE.  THE INDICATOR IS IN TRKMKCNT.
#
# CALLING SEQUENCE:  BEGUN EVERY 2 SECONDS AS AN INTEGRAL PART OF SERVICER
#
# SUBROUTINES CALLED:
#
# REMODE          RRPONLY
# UNIT            MPACVBUF
# QUICTRIG        AX*SR*T
# SPSIN           SPCOS
# SETRRECR        RROUT
# RRRDOT          RRRANGE
#
# EXIT:  TO NOR29NOW, IN SERVICER.
#
# OUTPUT:  (ALL FOR DOWNLINK)
#
# RM              RDOTM           (RAW)
# AIG             AMG
# AOG             TRKMKCNT        TRKMKCNT = 00001 IF SET IS CONSISTENT,
# TANGNB          TANGNB +1       OTHERWISE TRKMKCNT = 00000.
# MKTIME
# Page 595
#
# ERASABLE INITIALIZATION REQUIRED:
#
# NOR29FLG        READRFLG                (TO 1 AND 0 BY FRESH START) (RESET NOR29FLG TO LET SERVICER RUN R29)
# PIPTIME         RADMODES (BIT 10)       (BIT SET TO 0 BY FRESH START)
# R(CSM)          V(CSM)
# R               V                       (PIPTIME THRU V BY AVE G IN SERVICER)
#
# DEBRIS:
#
# RADMODES (BIT 10)
# LOSSM           LOSVDT/4                (= RRTARGET & LOSVEL)
# SAVECDUT        OLDESFLG                (SAVECDUT = MLOSV)
# LOSCMFLG        READRFLG
#
# ALARMS:  NONE.
#
# COMPONENT JOBS AND TASKS:
#
# INITIALIZING, IF RR IS FOUND TO BE IN MODE 1:  JOB R29REMOJ AND TASK REMODE:  ALWAYS: TASK PREPOS29.
# DESIGNATING:  TASK BEGDES29 & JOB R29DODES.
# RADAR READING:  TASK R29READ AND JOB R29RDJOB.  ALL JOBS ARE NOVAC TYPE.

#   BANK 33
#   SETLOC R29/SERV
#   BANK

#   COUNT* $$/r29

S('NR29&RDR', 'equals', 0o5014, line=4481)

# Page 596
# SERVICER COMES TO R29 FROM "R29?" IF NOR29FLG, READRFLG, RRREMODE, RRCDUZRO, RRREPOS, AND DISPLAY-INERTIAL-DATA
# ARE ALL RESET, AND THE RR IS IN LGC MODE (OFTEN CONFUSINGLY CALLED AUTO MODE).

W('33,2045', 0o40110, 'R29', 'CS', 'RADMODES', line=4487)
W('33,2046', 0o74742, '', 'MASK', 'DESIGBIT', line=4488)
W('33,2047', 0o00006, '', 'EXTEND', line=4489)
W('33,2050', 0o12123, '', 'BZF', 'R29.LOS', 'BRANCH IF DESIGNATION IS ALREADY ON.', line=4490)

W('33,2051', 0o00004, '', 'INHINT', line=4492)
W('33,2052', 0o26110, '', 'ADS', 'RADMODES', 'SHOW THAT DESIGNATION IS NOW ON.', line=4493)
W('33,2053', 0o44736, '', 'CS', 'BIT14', line=4494)
W('33,2054', 0o00006, '', 'EXTEND', line=4495)
W('33,2055', 0o03012, '', 'WAND', 'CHAN12', 'REMOVE RR TRACK ENABLE DISCRETE.', line=4496)
W('33,2056', 0o44740, '', 'CS', 'LOSCMBIT', line=4497)
W('33,2057', 0o70076, '', 'MASK', 'FLAGWRD2', line=4498)
W('33,2060', 0o54076, '', 'TS', 'FLAGWRD2', 'CLEAR LOSCMFLG TO SHOW DES. LOOP IS OFF.', line=4499)
W('33,2061', 0o44753, '', 'CS', 'OLDESBIT', line=4500)
W('33,2062', 0o70074, '', 'MASK', 'STATE', line=4501)
W('33,2063', 0o54074, '', 'TS', 'STATE', 'SHOW THAT DES. LOOP IS NOT REQUESTED.', line=4502)
W('33,2064', 0o04616, '', 'TC', 'BANKCALL', line=4503)
W('33,2065', 0o52156, '', 'CADR', 'SETRRECR', 'ENABLE RR ERROR COUNTERS.', kind='data', line=4504)
W('33,2066', 0o34740, '', 'CA', 'ANTENBIT', line=4505)
W('33,2067', 0o70110, '', 'MASK', 'RADMODES', line=4506)
W('33,2070', 0o10000, '', 'CCS', 'A', 'TEST RR MODE BIT.', line=4507)
W('33,2071', 0o12104, '', 'TCF', 'SETPRPOS', 'MODE 2.', line=4508)

W('33,2072', 0o35031, '', 'CA', 'PRIO21', 'MODE 1:  MUST REMODE.', line=4510)
W('33,2073', 0o05072, '', 'TC', 'NOVAC', line=4511)
#   EBANK= LOSCOUNT
W('33,2074', 0o02113, '', '2CADR', 'R29REM0J', 'NEEDS OWN JOB TO RADSTALL IN.', kind='data', line=4513)
W('33,2075', 0o66067, kind='data', line=4513)

W('33,2076', 0o44742, '', 'CS', 'DESIGBIT', line=4515)
W('33,2077', 0o70110, '', 'MASK', 'RADMODES', 'CLEAR DESIGNATE FLAG IN RADMODES', line=4516)
W('33,2100', 0o54110, '', 'TS', 'RADMODES', 'BEFORE CALLING REMODE', line=4517)
W('33,2101', 0o34736, '', 'CA', 'REMODBIT', line=4518)
W('33,2102', 0o26110, '', 'ADS', 'RADMODES', 'SHOW THAT REMODING IS ON.', line=4519)
W('33,2103', 0o12570, '', 'TCF', 'NOR29NOW', 'CONTINUE SERVICER FUNCTIONS.', line=4520)

W('33,2104', 0o34753, 'SETPRPOS', 'CA', 'ONE', line=4522)
W('33,2105', 0o05203, '', 'TC', 'WAITLIST', line=4523)
#   EBANK= LOSCOUNT
W('33,2106', 0o03601, '', '2CADR', 'PREPOS29', 'TASK TO SET TRUNNION ANGLE TO 180 DEG.', kind='data', line=4525)
W('33,2107', 0o52067, kind='data', line=4525)

W('33,2110', 0o34741, '', 'CA', 'REPOSBIT', line=4527)
W('33,2111', 0o26110, '', 'ADS', 'RADMODES', 'SHOW THAT REPOSITIONING IS ON.', line=4528)
W('33,2112', 0o12570, '', 'TCF', 'NOR29NOW', line=4529)

# Page 597
# FORCE RENDEZVOUS RADAR INTO MODE 2.

W('33,2113', 0o34753, 'R29REM0J', 'CA', 'ONE', line=4534)
W('33,2114', 0o05203, '', 'TC', 'WAITLIST', line=4535)
#   EBANK= LOSCOUNT
W('33,2115', 0o02171, '', '2CADR', 'REMODE', 'REMODE MUST RUN AS A TASK.', kind='data', line=4537)
W('33,2116', 0o52067, kind='data', line=4537)

W('33,2117', 0o04616, '', 'TC', 'BANKCALL', 'WAIT FOR END OF REMODING', line=4539)
W('33,2120', 0o17714, '', 'CADR', 'RADSTALL', kind='data', line=4540)

W('33,2121', 0o15155, '', 'TCF', 'ENDOFJOB', "BAD EXIT CAN'T HAPPEN.", line=4542)
W('33,2122', 0o15155, '', 'TCF', 'ENDOFJOB', line=4543)

# TASK TO PREPOSITION THE RR TRUNNION ANGLE TO -180 DEG.

#   SETLOC R29S1
#   BANK

W('25,3601', 0o34735, 'PREPOS29', 'CA', 'NEGMAX', '-180 DEG.', line=4550)
W('25,3602', 0o02241, '', 'TC', 'RRTONLY', 'DRIVE TRUNNION CDU.', line=4551)
W('25,3603', 0o44741, '', 'CS', 'REPOSBIT', 'SHOW THAT REPOSITIONING IS OFF.', line=4552)
W('25,3604', 0o70110, '', 'MASK', 'RADMODES', line=4553)
W('25,3605', 0o54110, '', 'TS', 'RADMODES', line=4554)
W('25,3606', 0o15261, '', 'TCF', 'TASKOVER', line=4555)

# COMPUTE THE LINE-OF-SIGHT AND LOS VELOCITY, AND PASS THEM TO THE R29DODES LOOP.

#   SETLOC R29
#   BANK

W('33,2123', 0o00006, 'R29.LOS', 'EXTEND', line=4562)
W('33,2124', 0o41235, '', 'DCS', 'PIPTIME', line=4563)
W('33,2125', 0o52155, '', 'DXCH', 'MPAC', line=4564)
W('33,2126', 0o00006, '', 'EXTEND', line=4565)
W('33,2127', 0o30025, '', 'DCA', 'TIME2', line=4566)
W('33,2130', 0o20155, '', 'DAS', 'MPAC', '(MPAC) = T-PIPTIME, SCALED B-28.', line=4567)
W('33,2131', 0o54163, '', 'TS', 'MODE', 'SET MODE TO DOUBLE PRECISION.', line=4568)
W('33,2132', 0o30155, '', 'CA', 'MPAC +1', line=4569)
W('33,2133', 0o00006, '', 'EXTEND', line=4570)
W('33,2134', 0o74740, '', 'MP', 'BIT12', line=4571)
W('33,2135', 0o52155, '', 'DXCH', 'MPAC', 'T-PIPTIME NOW SCALED B-17.', line=4572)
W('33,2136', 0o06037, '', 'TC', 'INTPRET', line=4573)
# Page 598
# LOSCMFLG = 0 MEANS THAT THE DESIGNATION IS READY FOR NEW DATA.  SETTING LOSCMFLG MAKES IT GO AWAY SO SETUP29D CAN
# START IT UP WHEN THE DATA IS IN PLACE.

W('33,2137', 0o52315, '', 'PDVL', 'VSU', 'PUSH DOWN T-PIPTIME', kind='interp', line=4578)
W('33,2140', 0o01726, '', '', 'V(CSM)', kind='operand', line=4579)
W('33,2141', 0o03527, '', '', 'V', 'LOSVEL = V(CSM) - V', kind='operand', line=4580)
W('33,2142', 0o74325, '', 'PDDL', 'VXSC', 'SWAP LOSVEL FOR T-PIPTIME, MULTIPLY THEM', kind='interp', line=4581)
W('33,2143', 0o52255, '', 'VAD', 'VSU', '      AND ADD THE RESULT TO R(CSM) - R TO GET', kind='interp', line=4582)
W('33,2144', 0o01720, '', '', 'R(CSM)', '      AN UP-TO-DATE LOS VECTOR IN SM AXES.', kind='operand', line=4583)
W('33,2145', 0o03521, '', '', 'R', kind='operand', line=4584)
W('33,2146', 0o77414, '', 'BOFSET', 'EXIT', '(BOFSET DOES ITS THING INHINTED.)', kind='interp', line=4585)
W('33,2147', 0o01043, '', '', 'LOSCMFLG', 'IF DESIGNATE LOOP IS OFF, CHANGE LOSCM-', kind='operand', line=4586)
W('33,2150', 0o66152, '', '', 'SETUP29D', 'FLG TO ON AND GO TO SET UP NEW DATA.', kind='operand', line=4587)
W('33,2151', 0o12570, '', 'TCF', 'NOR29NOW', 'IF DES. LOOP IS ON, LET IT USE OLD DATA.', line=4588)

W('33,2152', 0o25102, 'SETUP29D', 'STOVL', 'LOSSM', 'LINE-OF-SIGHT VECTOR, STABLE MEMBER AXES', kind='interp', line=4590)
W('33,2153', 0o00001, '', '', '0', kind='operand', line=4591)
W('33,2154', 0o77761, '', 'VXSC', kind='interp', line=4592)
W('33,2155', 0o26177, '', '', '.5SECB17', kind='operand', line=4593)
W('33,2156', 0o01761, '', 'STORE', 'LOSVDT/4', "1/2 SECOND'S WORTH OF LOS VELOCITY.", kind='interp', line=4594)
W('33,2157', 0o77414, '', 'CLEAR', 'EXIT', kind='interp', line=4595)
W('33,2160', 0o01263, '', '', 'LOSCMFLG', 'LET R29DLOOP USE NEW DATA.', kind='operand', line=4596)

W('33,2161', 0o40074, '', 'CS', 'STATE', line=4598)
W('33,2162', 0o74753, '', 'MASK', 'OLDESBIT', line=4599)
W('33,2163', 0o00006, '', 'EXTEND', line=4600)
W('33,2164', 0o12570, '', 'BZF', 'NOR29NOW', 'BRANCH IF R29 DES. LOOP IS REQUESTED.', line=4601)
W('33,2165', 0o00004, '', 'INHINT', line=4602)
W('33,2166', 0o26074, '', 'ADS', 'STATE', 'OTHERWISE REQUEST IT NOW.', line=4603)

W('33,2167', 0o11056, '', 'CCS', 'PIPCTR', 'SEE IF TASK SHOULD BE OFFSET ONE SECOND.', line=4605)
W('33,2170', 0o44776, '', 'CS', 'SUPER110', '-96D +100D = 4.', line=4606)
W('33,2171', 0o64777, '', 'AD', '1SEC', '0 +100D = 100D.', line=4607)
W('33,2172', 0o05203, '', 'TC', 'WAITLIST', line=4608)
#   EBANK= LOSCOUNT
W('33,2173', 0o03356, '', '2CADR', 'BEGDES29', 'START BEGDES29 TASK ASAP.', kind='data', line=4610)
W('33,2174', 0o50067, kind='data', line=4610)

W('33,2175', 0o12570, '', 'TCF', 'NOR29NOW', 'RELINT AND CONTINUE SERVICER FUNCTIONS.', line=4612)

W('33,2176', 0o00006, '.5SECB17', '2DEC', '50 B-17', kind='data', line=4614)
W('33,2177', 0o10000, kind='data', line=4614)

# Page 599
# R29 DESIGNATE JOB AND TASK MACHINERY.  TASK RECURS EVERY .5 SEC UNTIL DESIGNATE IS CALLED OFF; IT MAY WAIT FOR A
# CENTISECOND OR TWO IF IT COMES UP WHILE SETUP29D IS SUPPLYING NEW DATA.

#   BANK 24
#   SETLOC P20S
#   BANK

#   COUNT* $$/R29

W('24,3356', 0o35031, 'BEGDES29', 'CAF', 'PRIO21', line=4626)
W('24,3357', 0o05072, '', 'TC', 'NOVAC', line=4627)
#   EBANK= LOSVDT/4
W('24,3360', 0o02547, '', '2CADR', 'R29DODES', 'START R29DODES JOB TWICE A SECOND.', kind='data', line=4629)
W('24,3361', 0o64063, kind='data', line=4629)

W('24,3362', 0o34774, 'R29DLOOP', 'CAF', '.5SEC', line=4631)
W('24,3363', 0o05224, '', 'TC', 'VARDELAY', line=4632)

W('24,3364', 0o40110, '', 'CS', 'RADMODES', line=4634)
W('24,3365', 0o74742, '', 'MASK', 'DESIGBIT', line=4635)
W('24,3366', 0o10000, '', 'CCS', 'A', line=4636)
W('24,3367', 0o15261, '', 'TCF', 'TASKOVER', 'QUIT IF DESIGNATION IS CALLED OFF.', line=4637)

W('24,3370', 0o40076, '', 'CS', 'FLAGWRD2', line=4639)
W('24,3371', 0o74740, '', 'MASK', 'LOSCMBIT', line=4640)
W('24,3372', 0o00006, '', 'EXTEND', line=4641)
W('24,3373', 0o13376, '', 'BZF', '+3', "BRANCH IF SETUP29D'S SUPPLYING NEW DATA.", line=4642)
W('24,3374', 0o26076, '', 'ADS', 'FLAGWRD2', 'SET LOSCMFLG:  SHOW THAT DES. LOOP IS ON.', line=4643)
W('24,3375', 0o13356, '', 'TCF', 'BEGDES29', line=4644)

W('24,3376', 0o34753, '', 'CA', 'ONE', line=4646)
W('24,3377', 0o13363, '', 'TCF', 'R29DLOOP +1', 'WAIT A CENTISECOND FOR NEW DATA.', line=4647)
# Page 600
# R29DODES:  RR DESIGNATION LOOP FOR R29
#
# THIS ROUTINE DOES MUCH THE SAME THING AS DODES, BUT A GREAT DEAL FASTER.  IT TAKES THE NON-UNITIZED LOS VECTOR
# IN STABLE MEMBER COORDINATES (LOSSM) AND A DELTA-LOS IN SM AXES (LOSVDT/4) WHICH IS 1/2 SEC TIMES LOS VELOCITY,
# AND DEVELOPS THE SHAFT AND TRUNNION COMMANDS USING SINGLE PRECISION AS MUCH AS POSSIBLE, AND INTERPRETIVE NOT AT
# ALL.  THE UNIT(LOSM + LOSVEL * 1 SEC) IS COMPUTED IN DP AND TRANSFORMED TO NAV BASE COORDINATES IN DOUBLE PRE-
# CISION (USING SP SINES AND COSINES OF CDU ANGLES), AND THE REST IS DONE IN SP.
#
# THE FUNCTIONAL DIFFERENCE IS THAT R29DODES ALWAYS CLEARS LOSCMFLG WHEN IT ENDS, AND IT STARTS UP THE R29READ
# TASK WHEN LOCK-ON IS ACHIEVED.

#   BANK 32
#   SETLOC F2DPS*32
#   BANK

#   COUNT* $$/R29
#   EBANK= LOSVDT/4

W('32,2547', 0o34753, 'R29DODES', 'CA', 'ONE', line=4667)
W('32,2550', 0o55107, '', 'TS', 'TANG', 'INDICATE 1ST PASS THRU VECTOR LOOP.', line=4668)
W('32,2551', 0o34756, '', 'CA', 'FIVE', line=4669)

W('32,2552', 0o10000, 'R29DVBEG', 'CCS', 'A', "COUNT DOWN BY TWO'S IN VECTOR LOOP.", line=4671)
W('32,2553', 0o54002, '', 'TS', 'Q', line=4672)
W('32,2554', 0o11107, '', 'CCS', 'TANG', line=4673)
W('32,2555', 0o12563, '', 'TCF', 'R29DPAS1', 'DO THIS ON 1ST PASS THRU LOOP.', line=4674)

W('32,2556', 0o00006, '', 'EXTEND', '', '(A "PASS" HERE MEANS 3 TIMES AROUND).', line=4676)
W('32,2557', 0o50002, '', 'INDEX', 'Q', line=4677)
W('32,2560', 0o31761, '', 'DCA', 'LOSVDT/4', line=4678)
W('32,2561', 0o50002, '', 'INDEX', 'Q', line=4679)
W('32,2562', 0o21102, '', 'DAS', 'LOSSM', 'ADVANCE LOS VECTOR 1/2 SECOND.', line=4680)

W('32,2563', 0o00006, 'R29DPAS1', 'EXTEND', line=4682)
W('32,2564', 0o50002, '', 'INDEX', 'Q', line=4683)
W('32,2565', 0o31102, '', 'DCA', 'LOSSM', line=4684)
W('32,2566', 0o50002, '', 'INDEX', 'Q', 'MOVE CURRENT LOS (1ST PASS) OR LOS PRO-', line=4685)
W('32,2567', 0o52156, '', 'DXCH', 'MPAC +1', 'JECTED 1/2 SEC AHEAD (2ND PASS).', line=4686)
W('32,2570', 0o11107, '', 'CCS', 'TANG', line=4687)
W('32,2571', 0o12577, '', 'TCF', 'R29DVEND', 'BUG OUT HERE IN 1ST PASS.', line=4688)

W('32,2572', 0o00006, '', 'EXTEND', line=4690)
W('32,2573', 0o50002, '', 'INDEX', 'Q', line=4691)
W('32,2574', 0o31761, '', 'DCA', 'LOSVDT/4', line=4692)
W('32,2575', 0o50002, '', 'INDEX', 'Q', line=4693)
W('32,2576', 0o20156, '', 'DAS', 'MPAC +1', 'PROJECT LOS 1 SECOND AHEAD (2ND PASS).', line=4694)

W('32,2577', 0o10002, 'R29DVEND', 'CCS', 'Q', line=4696)
W('32,2600', 0o12552, '', 'TCF', 'R29DVBEG', 'BRANCH TO CONTINUE VECTOR LOOP.', line=4697)

# Page 601
# UNITIZE AND TRANSFORM TO NAV BASE AXES THE PRESENT LOS (1ST PASS) OR THE 1-SEC PROJECTED LOS (2ND PASS).

W('32,2601', 0o52156, '', 'DXCH', 'MPAC +1', line=4702)
W('32,2602', 0o52155, '', 'DXCH', 'MPAC', line=4703)
W('32,2603', 0o32774, '', 'CA', 'R29FXLOC', '= ADRES INTB15 + -34D', line=4704)
W('32,2604', 0o54120, '', 'TS', 'FIXLOC', line=4705)
W('32,2605', 0o04713, '', 'TC', 'USPRCADR', 'WITH FIXLOC ARMED FOR LENGTH AND LENGTH', line=4706)
W('32,2606', 0o01023, '', 'CADR', 'UNIT', 'SQUARED, BORROW UNITIZING ROUTINE.', kind='data', line=4707)
W('32,2607', 0o07532, '', 'TC', 'MPACVBUF', 'MOVE UNIT(LOS) TO AX*SR*T ARG AREA.', line=4708)

W('32,2610', 0o11107, '', 'CCS', 'TANG', line=4710)
W('32,2611', 0o12613, '', 'TCF', '+2', line=4711)
W('32,2612', 0o12627, '', 'TCF', 'GOTANGLS', 'GET CDU ANGLES ONLY AFTER 1ST PASS.', line=4712)
W('32,2613', 0o00004, '', 'INHINT', '', 'ENSURE CONSISTENT CDU READINGS.', line=4713)
W('32,2614', 0o00006, '', 'EXTEND', line=4714)
W('32,2615', 0o30036, '', 'DCA', 'CDUT', line=4715)
W('32,2616', 0o53767, '', 'DXCH', 'SAVECDUT', 'TRUNNION AND SHAFT ANGLES.', line=4716)
W('32,2617', 0o30033, '', 'CA', 'CDUY', line=4717)
W('32,2620', 0o54766, '', 'TS', 'CDUSPOT', line=4718)
W('32,2621', 0o30034, '', 'CA', 'CDUZ', line=4719)
W('32,2622', 0o54770, '', 'TS', 'CDUSPOT +2', line=4720)
W('32,2623', 0o30032, '', 'CA', 'CDUX', line=4721)
W('32,2624', 0o54772, '', 'TS', 'CDUSPOT +4', 'CDU ANGLES IN FUNNY ORDER FOR AX*SR*T.', line=4722)
W('32,2625', 0o04616, '', 'TC', 'BANKCALL', line=4723)
W('32,2626', 0o47615, '', 'CADR', 'QUICTRIG', 'GET SINES AND COSINES OF CDU ANGLES.', kind='data', line=4724)

W('32,2627', 0o46245, 'GOTANGLS', 'CS', 'THREE', line=4726)
W('32,2630', 0o04616, '', 'TC', 'BANKCALL', line=4727)
W('32,2631', 0o47675, '', 'CADR', 'AX*SR*T', 'TRANSFORM UNIT LOS TO NB AXES (ULOSNB).', kind='data', line=4728)

W('32,2632', 0o11107, '', 'CCS', 'TANG', line=4730)
W('32,2633', 0o12635, '', 'TCF', '+2', line=4731)
W('32,2634', 0o12702, '', 'TCF', 'R29DPAS2', 'GO TO RR COMMAND COMP. AFTER 2ND PASS.', line=4732)

# Page 602
# COMPUTE COSINE OF THE ANGLE BETWEEN THE PRESENT LOS AND THE RR BORESIGHT VECTOR, AND SET THE SELFTRACK ENABLE IF
# THE COSINE IS APPROXIMATELY COS(.5 DEG) OR GREATER (I.E., SMALLER ANGLE).

W('32,2635', 0o00004, '', 'INHINT', line=4738)
W('32,2636', 0o55107, '', 'TS', 'TANG', 'INDICATE 2ND PASS THRU VECTOR LOOP.', line=4739)
W('32,2637', 0o31766, '', 'CA', 'SAVECDUT', line=4740)
W('32,2640', 0o05032, '', 'TC', 'SPCOS', line=4741)
W('32,2641', 0o54166, '', 'TS', 'PUSHLOC', 'PUSHLOC = COS T.', line=4742)
W('32,2642', 0o41766, '', 'CS', 'SAVECDUT', line=4743)
W('32,2643', 0o05033, '', 'TC', 'SPSIN', line=4744)
W('32,2644', 0o54163, '', 'TS', 'MODE', 'MODE = -SIN T.', line=4745)
W('32,2645', 0o00006, '', 'EXTEND', line=4746)
W('32,2646', 0o70124, '', 'MP', 'VBUF +2', 'FORM - SIN T ULOSNBY.', line=4747)
W('32,2647', 0o52155, '', 'DXCH', 'MPAC', line=4748)
W('32,2650', 0o31767, '', 'CA', 'SAVECDUT +1', line=4749)
W('32,2651', 0o05033, '', 'TC', 'SPSIN', line=4750)
W('32,2652', 0o55766, '', 'TS', 'SAVECDUT', 'SAVECDUT NOW = SIN S.', line=4751)
W('32,2653', 0o00006, '', 'EXTEND', line=4752)
W('32,2654', 0o70166, '', 'MP', 'PUSHLOC', line=4753)
W('32,2655', 0o00006, '', 'EXTEND', line=4754)
W('32,2656', 0o70122, '', 'MP', 'VBUF', 'FORM SIN S COS T ULOSNBX.', line=4755)
W('32,2657', 0o20155, '', 'DAS', 'MPAC', line=4756)
W('32,2660', 0o31767, '', 'CA', 'SAVECDUT +1', line=4757)
W('32,2661', 0o05032, '', 'TC', 'SPCOS', line=4758)
W('32,2662', 0o55767, '', 'TS', 'SAVECDUT +1', 'SAVECDUT +1 NOW = COS S.', line=4759)
W('32,2663', 0o00006, '', 'EXTEND', line=4760)
W('32,2664', 0o70166, '', 'MP', 'PUSHLOC', line=4761)
W('32,2665', 0o00006, '', 'EXTEND', line=4762)
W('32,2666', 0o70126, '', 'MP', 'VBUF +4', 'FORM COS S COS T ULOSNBZ.', line=4763)
W('32,2667', 0o20155, '', 'DAS', 'MPAC', 'COS(ERROR) = ULOSNB . (SIN S COS T,', line=4764)
W('32,2670', 0o00006, '', 'EXTEND', '', '-SIN T, COS S COS T).', line=4765)
W('32,2671', 0o30155, '', 'DCA', 'MPAC', line=4766)
W('32,2672', 0o20155, 'TESTCOS', 'DAS', 'MPAC', '(ULOSNB IN VBUF WAS A HALF-UNIT VECTOR).', line=4767)
W('32,2673', 0o10000, '', 'CCS', 'A', 'TEST FOR + OVERFLOW, NONE, OR MINUS.', line=4768)
W('32,2674', 0o34736, '', 'CA', 'BIT14', line=4769)
W('32,2675', 0o12676, '', 'NOOP', line=4770)
W('32,2676', 0o00006, '', 'EXTEND', line=4771)
W('32,2677', 0o05012, '', 'WOR', 'CHAN12', 'IF PLUS OVERFLOW, SET SELFTRACK ENABLE.', line=4772)
W('32,2700', 0o00003, '', 'RELINT', line=4773)
W('32,2701', 0o12551, '', 'TCF', 'R29DVBEG -1', 'MAKE 2ND PASS THRU VECTOR LOOP.', line=4774)

# Page 603
# COMPUTE SHAFT AND TRUNNION COMMANDS TO NULL HAVE THE ERROR IN HALF A SECOND.

W('32,2702', 0o31767, 'R29DPAS2', 'CA', 'SAVECDUT +1', line=4779)
W('32,2703', 0o00006, '', 'EXTEND', line=4780)
W('32,2704', 0o70122, '', 'MP', 'VBUF', "FORM COS S ULOSNB'X.", line=4781)
W('32,2705', 0o53110, '', 'DXCH', 'TANG', line=4782)
W('32,2706', 0o41766, '', 'CS', 'SAVECDUT', line=4783)
W('32,2707', 0o00006, '', 'EXTEND', line=4784)
W('32,2710', 0o70126, '', 'MP', 'VBUF +4', "FORM - SIN S ULOSNB'Z.", line=4785)
W('32,2711', 0o21110, '', 'DAS', 'TANG', "RAW SHAFT CMD = ULOSNB' . (COS S, 0,", line=4786)
W('32,2712', 0o40163, '', 'CS', 'MODE', '- SIN S)', line=4787)
W('32,2713', 0o00006, '', 'EXTEND', line=4788)
W('32,2714', 0o71766, '', 'MP', 'SAVECDUT', line=4789)
W('32,2715', 0o00006, '', 'EXTEND', line=4790)
W('32,2716', 0o70122, '', 'MP', 'VBUF', "FORM SIN T SIN S ULOSNB'X.", line=4791)
W('32,2717', 0o52155, '', 'DXCH', 'MPAC', line=4792)
W('32,2720', 0o30166, '', 'CA', 'PUSHLOC', line=4793)
W('32,2721', 0o00006, '', 'EXTEND', line=4794)
W('32,2722', 0o70124, '', 'MP', 'VBUF +2', "FORM COS T ULOSNB'Y.", line=4795)
W('32,2723', 0o20155, '', 'DAS', 'MPAC', line=4796)
W('32,2724', 0o40163, '', 'CS', 'MODE', line=4797)
W('32,2725', 0o00006, '', 'EXTEND', line=4798)
W('32,2726', 0o71767, '', 'MP', 'SAVECDUT +1', line=4799)
W('32,2727', 0o00006, '', 'EXTEND', line=4800)
W('32,2730', 0o70126, '', 'MP', 'VBUF +4', "FORM SIN T COS S ULOSNB'Z.", line=4801)
W('32,2731', 0o20155, '', 'DAS', 'MPAC', "RAW TRUNNION CMD = ULOSNB'.", line=4802)
W('32,2732', 0o30154, '', 'CA', 'MPAC', '(SIN S SIN T, COS T, SIN S COS T).', line=4803)
W('32,2733', 0o00006, '', 'EXTEND', line=4804)
W('32,2734', 0o72775, '', 'MP', 'RR29GAIN', line=4805)
W('32,2735', 0o57107, '', 'XCH', 'TANG', 'STORE REFINED T CMD, GET RAW S CMD.', line=4806)
W('32,2736', 0o00006, '', 'EXTEND', line=4807)
W('32,2737', 0o72775, '', 'MP', 'RR29GAIN', line=4808)
W('32,2740', 0o55110, '', 'TS', 'TANG +1', 'STORE REFINED S CMD.', line=4809)

# Page 604
# WHETHER OR NOT TRACKING WAS ENABLED THIS TIME, CHECK ON RR DATA-GOOD.  IF PRESENT, STOP DESIGNATING AND START
# READING DATA FROM THE RENDEZVOUS RADAR.

W('32,2741', 0o34750, 'DGOOD?', 'CAF', 'BIT4', line=4815)
W('32,2742', 0o00006, '', 'EXTEND', line=4816)
W('32,2743', 0o02033, '', 'RAND', 'CHAN33', 'GET RR DATA-GOOD BIT.', line=4817)
W('32,2744', 0o00004, '', 'INHINT', '', '(MAINLY FOR RROUT).', line=4818)
W('32,2745', 0o00006, '', 'EXTEND', line=4819)
W('32,2746', 0o12752, '', 'BZF', 'R29LOKON', 'BRANCH IF DATA-GOOD IS PRESENT.', line=4820)

W('32,2747', 0o04616, '', 'TC', 'BANKCALL', line=4822)
W('32,2750', 0o52306, '', 'CADR', 'RROUT', 'DATA-GOOD IS ABSENT, SO SEND COMMANDS.', kind='data', line=4823)
W('32,2751', 0o12770, '', 'TCF', 'END29DOD', line=4824)

W('32,2752', 0o44742, 'R29LOKON', 'CS', 'DESIGBIT', line=4826)
W('32,2753', 0o70110, '', 'MASK', 'RADMODES', line=4827)
W('32,2754', 0o54110, '', 'TS', 'RADMODES', 'SHOW THAT DESIGNATION IS OVER.', line=4828)
W('32,2755', 0o44752, '', 'CS', 'BIT2', line=4829)
W('32,2756', 0o00006, '', 'EXTEND', line=4830)
W('32,2757', 0o03012, '', 'WAND', 'CHAN12', 'DISABLE RR ERROR COUNTERS.', line=4831)
W('32,2760', 0o34743, '', 'CA', 'READRBIT', line=4832)
W('32,2761', 0o26077, '', 'ADS', 'FLAGWRD3', 'SHOW THAT READING HAS BEEN REQUESTED.', line=4833)
W('32,2762', 0o11056, '', 'CCS', 'PIPCTR', 'SEE IF TASK SHOULD BE OFFSET 1 SEC.', line=4834)
W('32,2763', 0o44776, '', 'CS', 'SUPER110', '-96D + 100D = 4.', line=4835)
W('32,2764', 0o64777, '', 'AD', '1SEC', '0 + 100D = 100D.', line=4836)
W('32,2765', 0o05203, '', 'TC', 'WAITLIST', line=4837)
#   EBANK= LOSCOUNT
W('32,2766', 0o03400, '', '2CADR', 'R29READ', 'START READING TASK AND JOB.', kind='data', line=4839)
W('32,2767', 0o50067, kind='data', line=4839)

W('32,2770', 0o44740, 'END29DOD', 'CS', 'LOSCMBIT', line=4841)
W('32,2771', 0o70076, '', 'MASK', 'FLAGWRD2', line=4842)
W('32,2772', 0o54076, '', 'TS', 'FLAGWRD2', 'ALWAYS CLEAR LOSCMFLG.', line=4843)
W('32,2773', 0o15155, '', 'TCF', 'ENDOFJOB', line=4844)

W('32,2774', 0o00052, 'R29FXLOC', 'ADRES', 'INTB15+ -34D', kind='data', line=4846)
W('32,2775', 0o56655, 'RR29GAIN', 'DEC', '-.53624', kind='data', line=4847)
S('LOSVDT/4', 'equals', 0o1760, line=4848)
S('LOSSM', 'equals', 0o1101, line=4849)
S('SAVECDUT', 'equals', 0o1766, line=4850)

# Page 605
# RR READING IS SET UP BY R29DODES WHEN IT DETECTS RR LOCK-ON

#   BANK 24
#   SETLOC P20S
#   BANK

#   COUNT* $$/R29

#   EBANK= LOSCOUNT

W('24,3400', 0o37714, 'R29READ', 'CAF', 'PRIO26', 'CALLED BY WAITLIST', line=4863)
W('24,3401', 0o05072, '', 'TC', 'NOVAC', line=4864)
#   EBANK= LOSCOUNT
W('24,3402', 0o03413, '', '2CADR', 'R29RDJOB', 'START JOB TO READ AND DOWNLINK FOR R29.', kind='data', line=4866)
W('24,3403', 0o50067, kind='data', line=4866)

W('24,3404', 0o35000, '', 'CA', '2SECS', line=4868)
W('24,3405', 0o05224, '', 'TC', 'VARDELAY', line=4869)

W('24,3406', 0o30077, '', 'CA', 'FLAGWRD3', '2 SECONDS LATER, SEE IF READING IS STILL', line=4871)
W('24,3407', 0o74743, '', 'MASK', 'READRBIT', 'ALLOWED (NO TRACKER FAIL ETC.)', line=4872)
W('24,3410', 0o10000, '', 'CCS', 'A', line=4873)
W('24,3411', 0o13400, '', 'TCF', 'R29READ', "IT'S OK:  CALL IT AGAIN.", line=4874)
W('24,3412', 0o15261, '', 'TCF', 'TASKOVER', "IT AIN'T:  WAIT FOR REDESIGNATE.", line=4875)

W('24,3413', 0o30077, 'R29RDJOB', 'CA', 'FLAGWRD3', 'CALLED VIA NOVAC.', line=4877)
W('24,3414', 0o74741, '', 'MASK', 'NR29FBIT', line=4878)
W('24,3415', 0o10000, '', 'CCS', 'A', 'TEST "NOR29FLG".', line=4879)
W('24,3416', 0o13475, '', 'TCF', 'ENDRRD29', 'R29 IS NOW OVER, STOP AT ONCE.', line=4880)

W('24,3417', 0o30110, '', 'CA', 'RADMODES', line=4882)
W('24,3420', 0o74752, '', 'MASK', 'AUTOMBIT', line=4883)
W('24,3421', 0o10000, '', 'CCS', 'A', 'TEST RR-NOT-IN-AUTO-MODE BIT.', line=4884)
W('24,3422', 0o13475, '', 'TCF', 'ENDRRD29', 'ASTRO TOOK RR OUT OF AUTO MODE.', line=4885)

W('24,3423', 0o04616, '', 'TC', 'BANKCALL', line=4887)
W('24,3424', 0o53103, '', 'CADR', 'RRRDOT', 'INITIATE READING OF RANGE RATE.', kind='data', line=4888)
W('24,3425', 0o04616, '', 'TC', 'BANKCALL', line=4889)
W('24,3426', 0o17714, '', 'CADR', 'RADSTALL', "GOT TO SLEEP UNTIL IT'S READY.", kind='data', line=4890)
W('24,3427', 0o13475, '', 'TCF', 'ENDRRD29', 'BAD READ; REDESIGNATE.', line=4891)

# Page 606
# R29 RADAR READING CONTINUED.

W('24,3430', 0o53106, '', 'DXCH', 'TIMEHOLD', line=4896)
W('24,3431', 0o52155, '', 'DXCH', 'MPAC', 'TIME OF RR READING, FOR DOWNLINK.', line=4897)
W('24,3432', 0o00004, '', 'INHINT', '', 'BE SURE OF 5 CONSISTENT CDU ANGLES.', line=4898)
W('24,3433', 0o00006, '', 'EXTEND', line=4899)
W('24,3434', 0o30036, '', 'DCA', 'CDUT', line=4900)
W('24,3435', 0o52157, '', 'DXCH', 'MPAC +2', 'RRCDU ANGLES AT RR READ, FOR DOWNLINK.', line=4901)
W('24,3436', 0o00006, '', 'EXTEND', line=4902)
W('24,3437', 0o30034, '', 'DCA', 'CDUY', line=4903)
W('24,3440', 0o52161, '', 'DXCH', 'MPAC +4', "MPAC'S 7 WORDS ARE BUFFERED FOR COPYCYCLE.", line=4904)
W('24,3441', 0o30032, '', 'CA', 'CDUX', line=4905)
W('24,3442', 0o54162, '', 'TS', 'MPAC +6', 'IMUCDU ANGLES AT RR READ, FOR DOWNLINK.', line=4906)

W('24,3443', 0o04616, 'R29RANGE', 'TC', 'BANKCALL', line=4908)
W('24,3444', 0o53105, '', 'CADR', 'RRRANGE', 'INITIATE READING OF RR RANGE.', kind='data', line=4909)
W('24,3445', 0o04616, '', 'TC', 'BANKCALL', line=4910)
W('24,3446', 0o17714, '', 'CADR', 'RADSTALL', "GO TO SLEEP UNTIL IT'S READY.", kind='data', line=4911)
W('24,3447', 0o13466, '', 'TCF', 'R29RRR?', 'BAD READ OR SCALE CHANGE ... WHICH?', line=4912)

W('24,3450', 0o00004, '', 'INHINT', line=4914)
W('24,3451', 0o53334, '', 'DXCH', 'DNRRANGE', 'COPYCYCLE TO LAY OUT NEW R29 DOWNLINK.', line=4915)
W('24,3452', 0o53757, '', 'DXCH', 'RM', line=4916)
W('24,3453', 0o52155, '', 'DXCH', 'MPAC', line=4917)
W('24,3454', 0o53755, '', 'DXCH', 'MKTIME', line=4918)
W('24,3455', 0o52157, '', 'DXCH', 'MPAC +2', line=4919)
W('24,3456', 0o53753, '', 'DXCH', 'TANGNB', line=4920)
W('24,3457', 0o52161, '', 'DXCH', 'MPAC +4', line=4921)
W('24,3460', 0o53460, '', 'DXCH', 'AIG', line=4922)
W('24,3461', 0o30162, '', 'CA', 'MPAC +6', line=4923)
W('24,3462', 0o55461, '', 'TS', 'AOG', line=4924)
W('24,3463', 0o34753, '', 'CA', 'ONE', line=4925)
W('24,3464', 0o55462, '', 'TS', 'TRKMKCNT', 'SHOW THAT DOWNLINK DATA IS CONSISTENT.', line=4926)
W('24,3465', 0o15155, '', 'TCF', 'ENDOFJOB', line=4927)

W('24,3466', 0o40101, 'R29RRR?', 'CS', 'FLAGWRD5', line=4929)
W('24,3467', 0o74742, '', 'MASK', 'BIT10', line=4930)
W('24,3470', 0o10000, '', 'CCS', 'A', 'WAS IT A SCALE CHANGE (REAL OR PHONY)?', line=4931)
W('24,3471', 0o13475, '', 'TCF', 'ENDRRD29', 'NO, A BAD READ; REDESIGNATE.', line=4932)
W('24,3472', 0o05516, '', 'TC', 'DOWNFLAG', line=4933)
W('24,3473', 0o00120, '', 'ADRES', 'RNGSCFLG', kind='data', line=4934)
W('24,3474', 0o13443, '', 'TCF', 'R29RANGE', 'YES; CLEAR FLAG AND READ AGAIN.', line=4935)

W('24,3475', 0o34755, 'ENDRRD29', 'CA', 'ZERO', 'TROUBLE MADE US COME HERE TO LEAVE THE', line=4937)
W('24,3476', 0o55462, '', 'TS', 'TRKMKCNT', 'RR-READING MODE.  DISCREDIT DOWNTEL.', line=4938)
W('24,3477', 0o05516, '', 'TC', 'DOWNFLAG', line=4939)
W('24,3500', 0o00063, '', 'ADRES', 'READRFLG', kind='data', line=4940)
W('24,3501', 0o44736, '', 'CS', 'BIT14', line=4941)
W('24,3502', 0o00006, '', 'EXTEND', line=4942)
# Page 607
W('24,3503', 0o03012, '', 'WAND', 'CHAN12', 'REMOVE TRACK-ENABLE DISCRETE.', line=4944)
W('24,3504', 0o15155, '', 'TCF', 'ENDOFJOB', line=4945)

# Page 608
# W-MATRIX MONITOR

#   BANK 31
#   SETLOC VB67
#   BANK
#   COUNT* $$/EXTVB

#   EBANK= WWPOS

W('31,2007', 0o06037, 'V67CALL', 'TC', 'INTPRET', line=4957)
W('31,2010', 0o77624, '', 'CALL', kind='interp', line=4958)
W('31,2011', 0o62120, '', '', 'V67WW', kind='operand', line=4959)
W('31,2012', 0o77776, '', 'EXIT', kind='interp', line=4960)
W('31,2013', 0o00006, '', 'EXTEND', '', 'SAVE THE PRESENT N99 VALUES FOR', line=4961)
W('31,2014', 0o31601, '', 'DCA', 'WWPOS', 'COMPARISON AFTER THE DISPLAY', line=4962)
W('31,2015', 0o53607, '', 'DXCH', 'WWBIAS +2', line=4963)
W('31,2016', 0o00006, '', 'EXTEND', line=4964)
W('31,2017', 0o31603, '', 'DCA', 'WWVEL', line=4965)
W('31,2020', 0o53611, '', 'DXCH', 'WWBIAS +4', line=4966)
W('31,2021', 0o00006, '', 'EXTEND', line=4967)
W('31,2022', 0o31605, '', 'DCA', 'WWBIAS', line=4968)
W('31,2023', 0o53613, '', 'DXCH', 'WWBIAS +6', line=4969)
W('31,2024', 0o32143, 'V06N99DS', 'CAF', 'V06N99', line=4970)
W('31,2025', 0o04616, '', 'TC', 'BANKCALL', line=4971)
W('31,2026', 0o20334, '', 'CADR', 'GOXDSPF', kind='data', line=4972)
W('31,2027', 0o15472, '', 'TCF', 'ENDEXT', line=4973)
W('31,2030', 0o12032, '', 'TCF', 'V6N99PRO', line=4974)
W('31,2031', 0o12024, '', 'TCF', 'V06N99DS', line=4975)
W('31,2032', 0o22007, 'V6N99PRO', 'ZL', line=4976)
W('31,2033', 0o34756, '', 'CA', 'FIVE', line=4977)
W('31,2034', 0o54002, 'N99LOOP', 'TS', 'Q', line=4978)
W('31,2035', 0o50002, '', 'INDEX', 'Q', line=4979)
W('31,2036', 0o41600, '', 'CS', 'WWPOS', line=4980)
W('31,2037', 0o50002, '', 'INDEX', 'Q', line=4981)
W('31,2040', 0o61606, '', 'AD', 'WWPOS +6', line=4982)
W('31,2041', 0o26001, '', 'ADS', 'L', line=4983)
W('31,2042', 0o10002, '', 'CCS', 'Q', 'THE SUM OF ALL DIFFERENCES MUST BE ZERO.', line=4984)
W('31,2043', 0o12034, '', 'TCF', 'N99LOOP', line=4985)
W('31,2044', 0o22000, '', 'LXCH', 'A', line=4986)
W('31,2045', 0o00006, '', 'EXTEND', line=4987)
W('31,2046', 0o12051, '', 'BZF', 'V06N9933', line=4988)
W('31,2047', 0o05504, '', 'TC', 'UPFLAG', line=4989)
W('31,2050', 0o00160, '', 'ADRES', 'V67FLAG', kind='data', line=4990)

W('31,2051', 0o06037, 'V06N9933', 'TC', 'INTPRET', line=4992)
W('31,2052', 0o77414, '', 'BON', 'EXIT', kind='interp', line=4993)
W('31,2053', 0o03707, '', '', 'V67FLAG', kind='operand', line=4994)
W('31,2054', 0o62056, '', '', '+2', kind='operand', line=4995)
W('31,2055', 0o15472, '', 'TCF', 'ENDEXT', line=4996)
W('31,2056', 0o77745, '', 'DLOAD', kind='interp', line=4997)
# Page 609
W('31,2057', 0o02201, '', '', 'WWPOS', kind='operand', line=4999)
W('31,2060', 0o72412, '', 'SL4', 'SL1', kind='interp', line=5000)
W('31,2061', 0o14001, '', 'STODL', '0D', kind='interp', line=5001)
W('31,2062', 0o02203, '', '', 'WWVEL', kind='operand', line=5002)
W('31,2063', 0o14003, '', 'STODL', '2D', kind='interp', line=5003)
W('31,2064', 0o02205, '', '', 'WWBIAS', kind='operand', line=5004)
W('31,2065', 0o77661, '', 'SL', '', 'SHIFT FROM NOUN SCALING (B-5) TO', kind='interp', line=5005)
W('31,2066', 0o20213, '', '', '10D', 'INTERNAL SCALING (B+5)', kind='operand', line=5006)
W('31,2067', 0o00005, '', 'STORE', '4D', kind='interp', line=5007)
W('31,2070', 0o72014, '', 'BON', 'LXA,1', kind='interp', line=5008)
W('31,2071', 0o04307, '', '', 'SURFFLAG', kind='operand', line=5009)
W('31,2072', 0o62102, '', '', 'V67SURF', kind='operand', line=5010)
W('31,2073', 0o00000, '', '', '0D', kind='operand', line=5011)
W('31,2074', 0o72130, '', 'SXA,1', 'LXA,1', kind='interp', line=5012)
W('31,2075', 0o02000, '', '', 'WRENDPOS', kind='operand', line=5013)
W('31,2076', 0o00002, '', '', '2D', kind='operand', line=5014)
W('31,2077', 0o52130, '', 'SXA,1', 'GOTO', kind='interp', line=5015)
W('31,2100', 0o02001, '', '', 'WRENDVEL', kind='operand', line=5016)
W('31,2101', 0o62110, '', '', 'V67CLRF', kind='operand', line=5017)
W('31,2102', 0o66150, 'V67SURF', 'LXA,1', 'SXA,1', kind='interp', line=5018)
W('31,2103', 0o00000, '', '', '0D', kind='operand', line=5019)
W('31,2104', 0o02006, '', '', 'WSURFPOS', kind='operand', line=5020)
W('31,2105', 0o66150, '', 'LXA,1', 'SXA,1', kind='interp', line=5021)
W('31,2106', 0o00002, '', '', '2D', kind='operand', line=5022)
W('31,2107', 0o02007, '', '', 'WSURFVEL', kind='operand', line=5023)
W('31,2110', 0o66150, 'V67CLRF', 'LXA,1', 'SXA,1', kind='interp', line=5024)
W('31,2111', 0o00004, '', '', '4D', kind='operand', line=5025)
W('31,2112', 0o02003, '', '', 'WTRUN', kind='operand', line=5026)
W('31,2113', 0o77730, '', 'SXA,1', kind='interp', line=5027)
W('31,2114', 0o02002, '', '', 'WSHAFT', kind='operand', line=5028)
W('31,2115', 0o77414, '', 'CLEAR', 'EXIT', kind='interp', line=5029)
W('31,2116', 0o02676, '', '', 'RENDWFLG', kind='operand', line=5030)
W('31,2117', 0o15472, '', 'TCF', 'ENDEXT', line=5031)
W('31,2120', 0o40020, 'V67WW', 'STQ', 'BOV', kind='interp', line=5032)
W('31,2121', 0o00051, '', '', 'S2', kind='operand', line=5033)
W('31,2122', 0o62123, '', '', '+1', kind='operand', line=5034)
W('31,2123', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=5035)
W('31,2124', 0o03667, '', '', 'V67FLAG', kind='operand', line=5036)
W('31,2125', 0o27414, '', '', 'INTSTALL', kind='operand', line=5037)
W('31,2126', 0o71331, '', 'SSP', 'DLOAD', kind='interp', line=5038)
W('31,2127', 0o00051, '', '', 'S1', kind='operand', line=5039)
W('31,2130', 0o00006, '', 'DEC', '6', kind='data', line=5040)
W('31,2131', 0o06522, '', '', 'ZEROVECS', kind='operand', line=5041)
W('31,2132', 0o02201, '', 'STORE', 'WWPOS', kind='interp', line=5042)
W('31,2133', 0o02203, '', 'STORE', 'WWVEL', kind='interp', line=5043)
W('31,2134', 0o02205, '', 'STORE', 'WWBIAS', kind='interp', line=5044)
W('31,2135', 0o77770, '', 'AXT,1', kind='interp', line=5045)
W('31,2136', 0o00066, '', 'DEC', '54', kind='data', line=5046)
W('31,2137', 0o47573, 'NXPOSVEL', 'VLOAD*', 'VSQ', kind='interp', line=5047)
W('31,2140', 0o02467, '', '', 'W +54D,1', kind='operand', line=5048)
# Page 610
W('31,2141', 0o77650, '', 'GOTO', kind='interp', line=5050)
W('31,2142', 0o60002, '', '', 'ADDPOS', kind='operand', line=5051)
W('31,2143', 0o01543, 'V06N99', 'VN', '0699', kind='data', line=5052)

#   SETLOC VB67A
#   BANK
#   COUNT* $$/EXTVB

W('30,2002', 0o77615, 'ADDPOS', 'DAD', kind='interp', line=5058)
W('30,2003', 0o02201, '', '', 'WWPOS', kind='operand', line=5059)
W('30,2004', 0o02201, '', 'STORE', 'WWPOS', kind='interp', line=5060)
W('30,2005', 0o47573, '', 'VLOAD*', 'VSQ', kind='interp', line=5061)
W('30,2006', 0o02555, '', '', 'W +108D,1', kind='operand', line=5062)
W('30,2007', 0o77615, '', 'DAD', kind='interp', line=5063)
W('30,2010', 0o02203, '', '', 'WWVEL', kind='operand', line=5064)
W('30,2011', 0o02203, '', 'STORE', 'WWVEL', kind='interp', line=5065)
W('30,2012', 0o47573, '', 'VLOAD*', 'VSQ', kind='interp', line=5066)
W('30,2013', 0o02643, '', '', 'W +162D,1', kind='operand', line=5067)
W('30,2014', 0o77615, '', 'DAD', kind='interp', line=5068)
W('30,2015', 0o02205, '', '', 'WWBIAS', kind='operand', line=5069)
W('30,2016', 0o02205, '', 'STORE', 'WWBIAS', kind='interp', line=5070)
W('30,2017', 0o75500, '', 'TIX,1', 'SQRT', kind='interp', line=5071)
W('30,2020', 0o62137, '', '', 'NXPOSVEL', kind='operand', line=5072)
W('30,2021', 0o77661, '', 'SR', '', 'SHIFT FROM INTERNAL SCALING (B+5) TO', kind='interp', line=5073)
W('30,2022', 0o20613, '', '', '10D', 'NOUN SCALING (B-5)', kind='operand', line=5074)
W('30,2023', 0o16205, '', 'STODL', 'WWBIAS', kind='interp', line=5075)
W('30,2024', 0o02203, '', '', 'WWVEL', kind='operand', line=5076)
W('30,2025', 0o77766, '', 'SQRT', kind='interp', line=5077)
W('30,2026', 0o16203, '', 'STODL', 'WWVEL', kind='interp', line=5078)
W('30,2027', 0o02201, '', '', 'WWPOS', kind='operand', line=5079)
W('30,2030', 0o77766, '', 'SQRT', kind='interp', line=5080)
W('30,2031', 0o02201, '', 'STORE', 'WWPOS', kind='interp', line=5081)
W('30,2032', 0o52000, '', 'BOV', 'GOTO', kind='interp', line=5082)
W('30,2033', 0o60035, '', '', '+2', kind='operand', line=5083)
W('30,2034', 0o60042, '', '', 'V67XXX', kind='operand', line=5084)
W('30,2035', 0o77745, '', 'DLOAD', kind='interp', line=5085)
W('30,2036', 0o06530, '', '', 'DPPOSMAX', kind='operand', line=5086)
W('30,2037', 0o02201, '', 'STORE', 'WWPOS', kind='interp', line=5087)
W('30,2040', 0o02203, '', 'STORE', 'WWVEL', kind='interp', line=5088)
W('30,2041', 0o02205, '', 'STORE', 'WWBIAS', kind='interp', line=5089)
W('30,2042', 0o45345, 'V67XXX', 'DLOAD', 'DSU', kind='interp', line=5090)
W('30,2043', 0o02201, '', '', 'WWPOS', kind='operand', line=5091)
W('30,2044', 0o20060, '', '', 'FT99999', kind='operand', line=5092)
W('30,2045', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=5093)
W('30,2046', 0o60051, '', '', '+3', kind='operand', line=5094)
W('30,2047', 0o20060, '', '', 'FT99999', kind='operand', line=5095)
W('30,2050', 0o02201, '', 'STORE', 'WWPOS', kind='interp', line=5096)
W('30,2051', 0o66150, '', 'LXA,1', 'SXA,1', kind='interp', line=5097)
W('30,2052', 0o00051, '', '', 'S2', kind='operand', line=5098)
W('30,2053', 0o00052, '', '', 'QPRET', kind='operand', line=5099)
# Page 611
W('30,2054', 0o77776, '', 'EXIT', kind='interp', line=5101)
W('30,2055', 0o04635, '', 'TC', 'POSTJUMP', line=5102)
W('30,2056', 0o27425, '', 'CADR', 'INTWAKE', kind='data', line=5103)

W('30,2057', 0o01670, 'FT99999', '2DEC', '30479 B-19', kind='data', line=5105)
W('30,2060', 0o17000, kind='data', line=5105)

# Page 612
#   BANK 25
#   SETLOC RADARUPT
#   BANK
#   COUNT* $$/RRUPT

#   EBANK= LOSCOUNT

W('25,3607', 0o34753, 'R12LITES', 'CA', 'ONE', line=5115)
W('25,3610', 0o71303, '', 'MASK', 'IMODES33', line=5116)
W('25,3611', 0o10000, '', 'CCS', 'A', line=5117)
W('25,3612', 0o14707, '', 'TCF', 'ISWRETRN', line=5118)

W('25,3613', 0o03630, '', 'TC', 'HLIGHT', line=5120)
W('25,3614', 0o03625, '', 'TC', 'HLIGHT -3', line=5121)
W('25,3615', 0o14707, '', 'TCF', 'ISWRETRN', line=5122)

W('25,3616', 0o34753, 'RADLITES', 'CA', 'BIT1', line=5124)
W('25,3617', 0o71303, '', 'MASK', 'IMODES33', line=5125)
W('25,3620', 0o10000, '', 'CCS', 'A', line=5126)
W('25,3621', 0o00002, '', 'TC', 'Q', line=5127)

W('25,3622', 0o44747, '', 'CS', 'BIT5', line=5129)
W('25,3623', 0o60061, '', 'AD', 'ITEMP1', line=5130)
W('25,3624', 0o10000, '', 'CCS', 'A', line=5131)
W('25,3625', 0o44753, '', 'CS', 'ONE', line=5132)
W('25,3626', 0o13664, '', 'TCF', 'VLIGHT', line=5133)

W('25,3627', 0o14570, '', 'TCF', 'RRTRKF', line=5135)

W('25,3630', 0o54065, 'HLIGHT', 'TS', 'ITEMP5', 'ZERO ITEMP5 FOR H INDEX', line=5137)

W('25,3631', 0o34747, '', 'CA', 'HLITE', line=5139)
W('25,3632', 0o54001, '', 'TS', 'L', line=5140)

W('25,3633', 0o30107, '', 'CA', 'FLGWRD11', line=5142)
W('25,3634', 0o74751, '', 'MASK', 'SCABBIT', line=5143)
W('25,3635', 0o10000, '', 'CCS', 'A', line=5144)
W('25,3636', 0o13656, '', 'TCF', 'ONLITES', line=5145)
W('25,3637', 0o34747, '', 'CA', 'LRALTBIT', line=5146)
W('25,3640', 0o70110, 'BOTHLITS', 'MASK', 'RADMODES', line=5147)
W('25,3641', 0o10000, '', 'CCS', 'A', line=5148)
W('25,3642', 0o13656, '', 'TCF', 'ONLITES', line=5149)

W('25,3643', 0o30107, '', 'CA', 'FLGWRD11', line=5151)
W('25,3644', 0o50065, '', 'INDEX', 'ITEMP5', line=5152)
W('25,3645', 0o74753, '', 'MASK', 'HFLSHBIT', line=5153)
W('25,3646', 0o10000, '', 'CCS', 'A', line=5154)
W('25,3647', 0o14570, '', 'TCF', 'RRTRKF', line=5155)
# Page 613
W('25,3650', 0o00006, 'LITIT', 'EXTEND', line=5157)
W('25,3651', 0o22066, '', 'QXCH', 'ITEMP6', line=5158)
W('25,3652', 0o04602, '', 'TC', 'TRKFLON +1', line=5159)

W('25,3653', 0o00006, '', 'EXTEND', line=5161)
W('25,3654', 0o22066, '', 'QXCH', 'ITEMP6', line=5162)
W('25,3655', 0o14570, '', 'TCF', 'RRTRKF', line=5163)

W('25,3656', 0o50065, 'ONLITES', 'INDEX', 'ITEMP5', line=5166)
W('25,3657', 0o44753, '', 'CS', 'HFLSHBIT', line=5167)
W('25,3660', 0o70107, '', 'MASK', 'FLGWRD11', line=5168)
W('25,3661', 0o54107, '', 'TS', 'FLGWRD11', line=5169)

W('25,3662', 0o30001, '', 'CA', 'L', line=5171)
W('25,3663', 0o13650, '', 'TCF', 'LITIT', line=5172)
W('25,3664', 0o54065, 'VLIGHT', 'TS', 'ITEMP5', line=5173)
W('25,3665', 0o34751, '', 'CA', 'VLITE', line=5174)
W('25,3666', 0o54001, '', 'TS', 'L', line=5175)
W('25,3667', 0o34744, '', 'CA', 'BIT8', line=5176)
W('25,3670', 0o13640, '', 'TCF', 'BOTHLITS', line=5177)

S('HLITE', 'equals', 0o4747, line=5179)
S('VLITE', 'equals', 0o4751, line=5180)

# *** END OF LEMP20S .127 ***
