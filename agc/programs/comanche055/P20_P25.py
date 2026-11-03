"""P20-P25.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P20-P25.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 562-634 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P20_P25', 'P20-P25.agc', 'Comanche055', pages='562-634')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P20-P25.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        562-534
# Mod history:  2009-05-10 RSB  Adapted from the Colossus249/ file
# of the same name, using Comanche055 page
# images.
# 2009-05-20 RSB  Corrections:  P2OS -> P20S, STO -> STQ,
# GOTOPOOH -> GOTOPOOH, a duplicated EXTEND
# was fixed, P23.10 -> R23.10,
# S22B0X44 -> S22BOX44, S22SUBSCL -> 22SUBSCL,
# S22DPP -> S22DSPP, changed some instructions in
# P23.152.
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

# Page 562
# RENDEZVOUS NAVIGATION PROGRAM 20
#
# PROGRAM DESCRIPTION
#
# MOD NO -- 1
# MOD BY -- N. BRODEUR
#
# FUNCTIONAL DESCRIPTION
#
# TO CONTROL THE CSM ATTITUDE AND OPTICS TO ACQUIRE THE LEM IN THE S+T
# FIELD AND TO POINT THE CSM TRANSPONDER AT THE LEM.  TO UPDATE EITHER THE
# LEM OR CSM STATE VECTOR (AS SPECIFIED BY THE ASTRONAUT BY THE DSKY
# ENTRY) ON THE BASIS OF OPTICAL TRACKING DATA (REQUESTED BY DSKY)
#
# CALLING SEQUENCE --
#
# ASTRONAUT REQUEST THROUGH DSKY V37E20E
#
# SUBROUTINES CALLED
#
# R02BOTH (IMU STATUS CHECK)                              BANKCALL
# FLAGUP                          2PHCHNG                 LOADTIME
# R61CSM (PREFERRED TRACKING ATTITUDE)                    FLAGDOWN
# R52 (AUTO OPTICS POSITIONING ROUT)                      SETINTG
# R22 (REND TRACK DATA PROC ROUT)                         PRIOCHNG
# ENDOFJOB                        INTEGRV                 GRP2PC
# INTPRET                         MKRLEES                 FINDVAC
#
# NORMAL EXIT MODES --
#
# P20 MAY BE TERMINATED IN TWO WAYS -- ASTRONAUT SELECTION OF IDLING
# PROGRAM (P00) BY KEYING V37E00E OR BY KEYING IN V56E
#
# ALARM OR ABORT EXIT MODES --
#
# NONE DIRECTLY FROM P20
#
# OUTPUT
#
# TRKMKCNT = NO OF RENDEZVOUS TRACKING MARKS TAKEN (COUNTER)
# VHFCNT = NO OF VHF RANGING MARKS INCORPORATED (COUNTER)
#
# FLAGS SET + RESET
#
# RNDVZFLG,VEHUPFLG,UPDATFLG,TRACKFLG,TARG1FLG
# HOLDFLAG,WBODY,WBODY1,WBODY2,DELCDUX,DELCDUY,DELCDUZ
# STIKFLAG,PRFTRKAT,VINTFLAG,DIM0FLAG,R60FLAG,R61CNTR

#   BANK 33
#   SETLOC P20S
#   BANK

#   EBANK= ESTROKER
#   COUNT* $$/P20

W('37,2261', 0o04662, 'PROG20', 'TC', 'BANKCALL', line=93)
W('37,2262', 0o17653, '', 'CADR', 'R02BOTH', 'IMU STATUS CHECK', kind='data', line=94)
# BLOCKING OF UPLINK IS DONE BY UPLINK PRG
W('37,2263', 0o35021, '', 'CAF', 'ZERO', line=96)
W('37,2264', 0o55126, '', 'TS', 'TRKMKCNT', 'ZERO REND TRACKING MARK COUNTER', line=97)
W('37,2265', 0o55125, '', 'TS', 'VHFCNT', 'ZERO REND VHF RNG MRK COUNTER', line=98)
W('37,2266', 0o05546, '', 'TC', 'UPFLAG', 'SET PREF TRACK ATT FLAG', line=99)
W('37,2267', 0o00120, '', 'ADRES', 'PRFTRKAT', 'BIT 10 FLAG 5', kind='data', line=100)
W('37,2270', 0o05560, '', 'TC', 'DOWNFLAG', 'LEM TO BE UPDATED.  VEHUPFLG RESET.', line=101)
W('37,2271', 0o00026, '', 'ADRES', 'VEHUPFLG', 'BIT 8 FLAG 1', kind='data', line=102)
# Page 563
W('37,2272', 0o05546, '', 'TC', 'UPFLAG', 'SET TRACKFLAG', line=104)
W('37,2273', 0o00031, '', 'ADRES', 'TRACKFLG', 'BIT 5 FLAG 1', kind='data', line=105)
W('37,2274', 0o05546, '', 'TC', 'UPFLAG', 'SET UPDATFLG', line=106)
W('37,2275', 0o00027, '', 'ADRES', 'UPDATFLG', 'BIT 7 FLAG 1', kind='data', line=107)
W('37,2276', 0o05546, '', 'TC', 'UPFLAG', 'SET RNDVZFLG', line=108)
W('37,2277', 0o00010, '', 'ADRES', 'RNDVZFLG', 'BIT 7 FLAG 0', kind='data', line=109)
W('37,2300', 0o05372, '', 'TC', '2PHSCHNG', line=110)
W('37,2301', 0o00004, '', 'OCT', '4', kind='data', line=111)
W('37,2302', 0o05022, '', 'OCT', '05022', kind='data', line=112)
W('37,2303', 0o26000, '', 'OCT', '26000', kind='data', line=113)
W('37,2304', 0o06006, '', 'TC', 'INTPRET', line=114)
W('37,2305', 0o77634, '', 'RTB', kind='interp', line=115)
W('37,2306', 0o45510, '', '', 'LOADTIME', kind='operand', line=116)
W('37,2307', 0o35225, '', 'STCALL', 'MARKTIME', kind='interp', line=117)
W('37,2310', 0o56343, '', '', 'SETINTG', 'SET INTEGRATION FLAGS', kind='operand', line=118)
W('37,2311', 0o43014, '', 'BOFF', 'SET', kind='interp', line=119)
W('37,2312', 0o02756, '', '', 'RENDWFLG', kind='operand', line=120)
W('37,2313', 0o76315, '', '', 'P20.1', kind='operand', line=121)
W('37,2314', 0o01476, '', '', 'DIM0FLAG', 'SET TO INTEGRATE THE W MATRIX', kind='operand', line=122)
W('37,2315', 0o43014, 'P20.1', 'BON', 'CLEAR', kind='interp', line=123)
W('37,2316', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=124)
W('37,2317', 0o76321, '', '', 'P20.2', kind='operand', line=125)
W('37,2320', 0o01674, '', '', 'VINTFLAG', 'SET FOR LM INTEGRATION', kind='operand', line=126)
W('37,2321', 0o77624, 'P20.2', 'CALL', kind='interp', line=127)
W('37,2322', 0o27162, '', '', 'INTEGRV', kind='operand', line=128)
W('37,2323', 0o77624, '', 'CALL', kind='interp', line=129)
W('37,2324', 0o56750, '', '', 'GRP2PC', 'GROUP 2 PHASE CHANGE', kind='operand', line=130)
W('37,2325', 0o77624, '', 'CALL', kind='interp', line=131)
W('37,2326', 0o56343, '', '', 'SETINTG', 'SET INTEGRATION FLAGS', kind='operand', line=132)
W('37,2327', 0o43014, '', 'BOFF', 'CLEAR', kind='interp', line=133)
W('37,2330', 0o00747, '', '', 'VEHUPFLG', kind='operand', line=134)
W('37,2331', 0o76333, '', '', 'P20.3', kind='operand', line=135)
W('37,2332', 0o01674, '', '', 'VINTFLAG', 'SET FOR LM INTEGRATION', kind='operand', line=136)
W('37,2333', 0o77624, 'P20.3', 'CALL', kind='interp', line=137)
W('37,2334', 0o27162, '', '', 'INTEGRV', kind='operand', line=138)
W('37,2335', 0o77776, '', 'EXIT', kind='interp', line=139)
W('37,2336', 0o37663, '', 'CAF', 'PRIO26', line=140)
W('37,2337', 0o05147, '', 'TC', 'FINDVAC', line=141)
#   EBANK= MRKBUF2
W('37,2340', 0o02630, '', '2CADR', 'R22', kind='data', line=143)
W('37,2341', 0o70067, kind='data', line=143)

W('37,2342', 0o05372, '', 'TC', '2PHSCHNG', line=145)
W('37,2343', 0o00072, '', 'OCT', '00072', kind='data', line=146)
W('37,2344', 0o00111, '', 'OCT', '00111', kind='data', line=147)
W('37,2345', 0o35066, 'PIKUP20', 'CAF', 'PRIO14', 'ALLOW HIGHER PRIO THAN LAMBERT', line=148)
W('37,2346', 0o05210, '', 'TC', 'PRIOCHNG', line=149)
W('37,2347', 0o35013, '', 'CAF', 'BIT5', 'IS TRACK FLAG SET', line=150)
W('37,2350', 0o70075, '', 'MASK', 'STATE +1', line=151)
W('37,2351', 0o00006, '', 'EXTEND', line=152)
W('37,2352', 0o15217, '', 'BZF', 'ENDOFJOB', 'NO', line=153)
# Page 564
W('37,2353', 0o35003, '', 'CAF', 'BIT13', line=155)
W('37,2354', 0o70077, '', 'MASK', 'STATE +3', 'IS REFSMFLG SET', line=156)
W('37,2355', 0o00006, '', 'EXTEND', line=157)
W('37,2356', 0o15217, '', 'BZF', 'ENDOFJOB', line=158)
W('37,2357', 0o35021, '', 'CAF', 'ZERO', line=159)
W('37,2360', 0o55775, '', 'TS', 'R61CNTR', 'INITIALIZE R61 COUNTER', line=160)
W('37,2361', 0o04662, '', 'TC', 'BANKCALL', line=161)
W('37,2362', 0o76557, '', 'CADR', 'R61CSM', kind='data', line=162)
#   EBANK= QMIN
W('37,2363', 0o35056, '', 'CAF', 'EBANK5', line=164)
W('37,2364', 0o54003, '', 'TS', 'EBANK', line=165)
W('37,2365', 0o05546, '', 'TC', 'UPFLAG', 'SET TARGET FLAG TO LEM', line=166)
W('37,2366', 0o00024, '', 'ADRES', 'TARG1FLG', 'BIT 10 FLAG 1', kind='data', line=167)
W('37,2367', 0o06006, 'P20R52JB', 'TC', 'INTPRET', line=168)
W('37,2370', 0o77624, '', 'CALL', kind='interp', line=169)
W('37,2371', 0o30011, '', '', 'R52', 'SET UP AUTO OPTICS JOB', kind='operand', line=170)
W('37,2372', 0o77776, '', 'EXIT', kind='interp', line=171)
W('37,2373', 0o04662, '', 'TC', 'BANKCALL', line=172)
W('37,2374', 0o16071, '', 'CADR', 'MKRLEES', kind='data', line=173)
W('37,2375', 0o35017, '', 'CAF', 'ONE', 'HOLD PRESENT ATTITUDE', line=174)
W('37,2376', 0o55332, '', 'TS', 'HOLDFLAG', line=175)
W('37,2377', 0o05217, '', 'TC', 'ENDOFJOB', line=176)
W('37,2400', 0o00203, 'OCT203', 'OCT', '00203', kind='data', line=177)
S('FIRST3', 'equals', 0o7707, line=178)

# Page 565
# ORBITAL NAVIGATION PROGRAM 22

#   BANK 31
#   SETLOC P20S1
#   BANK

#   EBANK= LANDMARK
#   COUNT* $$/P22

W('30,2000', 0o05560, 'PROG22', 'TC', 'DOWNFLAG', 'RESET RNDVZFLG BIT 7 FLAG 0', line=190)
W('30,2001', 0o00010, '', 'ADRES', 'RNDVZFLG', kind='data', line=191)
W('30,2002', 0o04662, '', 'TC', 'BANKCALL', line=192)
W('30,2003', 0o17653, '', 'CADR', 'R02BOTH', 'IMU STATUS CHECK', kind='data', line=193)
W('30,2004', 0o06006, '', 'TC', 'INTPRET', 'COMPUTE ANGLE BETWEEN Y AND VXR SM', line=194)
W('30,2005', 0o77634, '', 'RTB', kind='interp', line=195)
W('30,2006', 0o45510, '', '', 'LOADTIME', kind='operand', line=196)
W('30,2007', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=197)
W('30,2010', 0o27114, '', '', 'CSMCONIC', 'INTEGRATE TO PRESENT TIME', kind='operand', line=198)
W('30,2011', 0o47375, '', 'VLOAD', 'VXV', 'CROSS PRODUCT BETWEEN V AND R', kind='interp', line=199)
W('30,2012', 0o00007, '', '', 'VATT', kind='operand', line=200)
W('30,2013', 0o00001, '', '', 'RATT', kind='operand', line=201)
W('30,2014', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=202)
W('30,2015', 0o01744, '', '', 'REFSMMAT +6', kind='operand', line=203)
W('30,2016', 0o77646, '', 'ABS', kind='interp', line=204)
W('30,2017', 0o65552, '', 'SL1', 'ARCCOS', kind='interp', line=205)
W('30,2020', 0o03626, '', 'STORE', '+MGA', kind='interp', line=206)
W('30,2021', 0o77414, '', 'CLEAR', 'EXIT', kind='interp', line=207)
W('30,2022', 0o02676, '', '', 'RENDWFLG', kind='operand', line=208)
W('30,2023', 0o32114, '', 'CAF', 'V06N45B', line=209)
W('30,2024', 0o04662, '', 'TC', 'BANKCALL', line=210)
W('30,2025', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=211)
W('30,2026', 0o04106, '', 'TC', 'GOTOPOOH', 'TERM P22', line=212)
W('30,2027', 0o02034, '', 'TC', 'PROG22A', 'PROC', line=213)
W('30,2030', 0o02023, '', 'TC', '-5', 'ENTER', line=214)
W('30,2031', 0o36214, '', 'CAF', 'THREE', line=215)
W('30,2032', 0o05526, '', 'TC', 'BLANKET', 'BLANK OUT R1 + R2', line=216)
W('30,2033', 0o05217, '', 'TC', 'ENDOFJOB', line=217)
W('30,2034', 0o45063, 'PROG22A', 'CS', 'PRIO7', 'RESULT=70777  SET OFFSET NO.=0', line=218)
W('30,2035', 0o71751, '', 'MASK', 'LANDMARK', line=219)
W('30,2036', 0o55751, '', 'TS', 'LANDMARK', line=220)
W('30,2037', 0o06006, '', 'TC', 'INTPRET', line=221)
W('30,2040', 0o77614, '', 'CLEAR', kind='interp', line=222)
W('30,2041', 0o01664, '', '', 'P22MKFLG', kind='operand', line=223)
W('30,2042', 0o43014, '', 'SET', 'BOFF', kind='interp', line=224)
W('30,2043', 0o00462, '', '', 'ERADFLAG', kind='operand', line=225)
W('30,2044', 0o04343, '', '', 'CMOONFLG', kind='operand', line=226)
W('30,2045', 0o60055, '', '', 'PROG22B', 'EARTH', kind='operand', line=227)
W('30,2046', 0o77614, '', 'SET', '', 'MOON', kind='interp', line=228)
W('30,2047', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=229)
W('30,2050', 0o45145, '', 'DLOAD', 'CALL', 'MPAC=V05N70,MPAC+1=NONZERO FOR N70', kind='interp', line=230)
W('30,2051', 0o20116, '', '', 'V05N7022', kind='operand', line=231)
# Page 566
W('30,2052', 0o60175, '', '', 'S22N7071', kind='operand', line=233)
W('30,2053', 0o77650, '', 'GOTO', kind='interp', line=234)
W('30,2054', 0o60062, '', '', 'CALLR52', kind='operand', line=235)
W('30,2055', 0o43014, 'PROG22B', 'CLEAR', 'SET', 'EARTH ORBIT', kind='interp', line=236)
W('30,2056', 0o01663, '', '', 'LUNAFLAG', kind='operand', line=237)
W('30,2057', 0o03067, '', '', 'KNOWNFLG', kind='operand', line=238)
W('30,2060', 0o77624, '', 'CALL', '', 'GET LAT/LONG/ALT FROM ASTRO', kind='interp', line=239)
W('30,2061', 0o60143, '', '', 'P22SUBRB', kind='operand', line=240)
W('30,2062', 0o77776, 'CALLR52', 'EXIT', kind='interp', line=241)
W('30,2063', 0o05372, '', 'TC', '2PHSCHNG', line=242)
W('30,2064', 0o00004, '', 'OCT', '00004', kind='data', line=243)
W('30,2065', 0o05022, '', 'OCT', '05022', kind='data', line=244)
W('30,2066', 0o13000, '', 'OCT', '13000', kind='data', line=245)
W('30,2067', 0o35022, '', 'CAF', 'FIVE', line=246)
W('30,2070', 0o54301, '', 'TS', 'MARKINDX', 'SET MARK INDEX=5 FOR R52', line=247)
W('30,2071', 0o05546, '', 'TC', 'UPFLAG', line=248)
W('30,2072', 0o00025, '', 'ADRES', 'TARG2FLG', 'SET FOR SIGHTING LMK', kind='data', line=249)
W('30,2073', 0o05560, '', 'TC', 'DOWNFLAG', line=250)
W('30,2074', 0o00024, '', 'ADRES', 'TARG1FLG', 'CLEAR FOR NON-LEM', kind='data', line=251)
W('30,2075', 0o06006, '', 'TC', 'INTPRET', line=252)
W('30,2076', 0o77624, '', 'CALL', kind='interp', line=253)
W('30,2077', 0o30011, '', '', 'R52', kind='operand', line=254)
W('30,2100', 0o45135, 'DOV5N71', 'SLOAD', 'CALL', 'MPAC=V05N71,MPAC+1=0 FOR N71', kind='interp', line=255)
W('30,2101', 0o20117, '', '', 'V05N7122', kind='operand', line=256)
W('30,2102', 0o60175, '', '', 'S22N7071', kind='operand', line=257)
W('30,2103', 0o66744, 'PROG22C', 'LXC,2', 'SLOAD*', kind='interp', line=258)
W('30,2104', 0o01330, '', '', 'MARKSTAT', kind='operand', line=259)
W('30,2105', 0o77724, '', '', 'QPRET,2', kind='operand', line=260)
W('30,2106', 0o36750, '', 'STCALL', '8NN', kind='interp', line=261)
W('30,2107', 0o60312, '', '', 'S22.1', 'ESTABLISH LANDMARK -- COMPUTE ORBITAL', kind='operand', line=262)
W('30,2110', 0o77776, 'P22OVER', 'EXIT', kind='interp', line=263)
W('30,2111', 0o05412, '', 'TC', 'PHASCHNG', line=264)
W('30,2112', 0o04022, '', 'OCT', '04022', kind='data', line=265)
W('30,2113', 0o02034, '', 'TC', 'PROG22A', 'POINT A ON GSOP', line=266)
W('30,2114', 0o01455, 'V06N45B', 'VN', '0645', kind='data', line=267)
W('30,2115', 0o01306, 'V05N7022', 'VN', '00570', kind='data', line=268)
W('30,2116', 0o01307, 'V05N7122', 'VN', '00571', kind='data', line=269)
#   SETLOC P20S
#   BANK

#   SETLOC P20S1
#   BANK

W('30,2117', 0o77634, 'S22LSITE', 'RTB', '', 'CONVERT RLS FROM MOON-FIXED TO BASIC REF', kind='interp', line=276)
W('30,2120', 0o45510, '', '', 'LOADTIME', kind='operand', line=277)
W('30,2121', 0o24007, '', 'STOVL', '6D', '6-7D= TIME', kind='interp', line=278)
W('30,2122', 0o02026, '', '', 'RLS', kind='operand', line=279)
W('30,2123', 0o14001, '', 'STODL', '0D', '0-5D= LANDING SITE VECTOR', kind='interp', line=280)
W('30,2124', 0o15333, '', '', 'HIDPHALF', 'MPAC= ANY NON-ZERO FOR MOON', kind='operand', line=281)
W('30,2125', 0o77624, '', 'CALL', kind='interp', line=282)
# Page 567
W('30,2126', 0o55344, '', '', 'RP-TO-R', 'RLS IN BASIC REF B-27 IN MPAC', kind='operand', line=284)
W('30,2127', 0o77742, '', 'VSR2', '', 'LUNAFLAG AND ERADFLAG SET ABOVE', kind='interp', line=285)
W('30,2130', 0o02152, '', 'STORE', 'ALPHAV', 'SCALE RLS B-29 FOR LAT-LONG', kind='interp', line=286)
W('30,2131', 0o77634, '', 'RTB', kind='interp', line=287)
W('30,2132', 0o45510, '', '', 'LOADTIME', 'SET PRESENT TIME IN MPAC FOR LAT-LONG', kind='operand', line=288)
W('30,2133', 0o77624, '', 'CALL', kind='interp', line=289)
W('30,2134', 0o26370, '', '', 'LAT-LONG', kind='operand', line=290)
W('30,2135', 0o77650, '', 'GOTO', kind='interp', line=291)
W('30,2136', 0o03667, '', '', 'S22TOFF', 'EXIT', kind='operand', line=292)
W('30,2137', 0o77624, 'OBTAINLL', 'CALL', '', 'GET LAT/LONG/ALT FROM ASTRO', kind='interp', line=293)
W('30,2140', 0o60143, '', '', 'P22SUBRB', kind='operand', line=294)
W('30,2141', 0o77650, '', 'GOTO', kind='interp', line=295)
W('30,2142', 0o03667, '', '', 'S22TOFF', 'EXIT', kind='operand', line=296)
W('30,2143', 0o77420, 'P22SUBRB', 'STQ', 'EXIT', 'GET LAT/LONG/ALT FROM ASTRO', kind='interp', line=297)
W('30,2144', 0o03670, '', '', 'S22TOFF +1', kind='operand', line=298)
W('30,2145', 0o33644, '', 'CAF', 'V06N89B', line=299)
W('30,2146', 0o04662, '', 'TC', 'BANKCALL', line=300)
W('30,2147', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=301)
W('30,2150', 0o04106, '', 'TC', 'GOTOPOOH', 'TERMINATE', line=302)
W('30,2151', 0o02153, '', 'TC', '+2', 'PROCEED', line=303)
W('30,2152', 0o02145, '', 'TC', '-5', 'ENTER OR RECYCLE', line=304)
W('30,2153', 0o06006, '', 'TC', 'INTPRET', line=305)
W('30,2154', 0o51545, '', 'DLOAD', 'ABS', 'TEST LAT/LONG GREATER THAN 90', kind='interp', line=306)
W('30,2155', 0o01104, '', '', 'LANDLAT', kind='operand', line=307)
W('30,2156', 0o50021, '', 'BDSU', 'BMN', '1/4 REV - LAT', kind='interp', line=308)
W('30,2157', 0o15325, '', '', 'DP1/4TH', kind='operand', line=309)
W('30,2160', 0o60166, '', '', 'N89ERRX', kind='operand', line=310)
W('30,2161', 0o51545, '', 'DLOAD', 'ABS', kind='interp', line=311)
W('30,2162', 0o02360, '', '', 'LANDLONG', kind='operand', line=312)
W('30,2163', 0o51021, '', 'BDSU', 'BPL', kind='interp', line=313)
W('30,2164', 0o15325, '', '', 'DP1/4TH', kind='operand', line=314)
W('30,2165', 0o60171, '', '', '+4', kind='operand', line=315)

W('30,2166', 0o77776, 'N89ERRX', 'EXIT', kind='interp', line=317)
W('30,2167', 0o04400, '', 'TC', 'FALTON', line=318)
W('30,2170', 0o02145, '', 'TC', 'P22SUBRB +2', 'LONG GR. THAN 90  REDISPLAY', line=319)
W('30,2171', 0o77624, '', 'CALL', kind='interp', line=320)
W('30,2172', 0o62374, '', '', 'LLASRDA', kind='operand', line=321)
W('30,2173', 0o77650, '', 'GOTO', kind='interp', line=322)
W('30,2174', 0o03670, '', '', 'S22TOFF +1', 'EXIT', kind='operand', line=323)
W('30,2175', 0o02747, 'S22N7071', 'STORE', '8KK', '8KK=V05N71,V05N70 8KK+1=0 N71, NOT 0 N70', kind='interp', line=324)
W('30,2176', 0o77420, '', 'STQ', 'EXIT', kind='interp', line=325)
W('30,2177', 0o03667, '', '', 'S22TOFF', kind='operand', line=326)
W('30,2200', 0o31746, 'S22DSPPA', 'CA', '8KK', 'V05N70 OR V05N71', line=327)
W('30,2201', 0o04662, '', 'TC', 'BANKCALL', line=328)
W('30,2202', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=329)
W('30,2203', 0o04106, '', 'TC', 'GOTOPOOH', 'V34E TERMINATE', line=330)
W('30,2204', 0o02211, '', 'TC', '+5', 'V33E PROCEED', line=331)
W('30,2205', 0o02200, '', 'TC', '-5', 'V32E RECYCLE', line=332)
W('30,2206', 0o35022, '', 'CAF', 'FIVE', 'IMMEDIATE RETURN BLANK OUT R1,R3', line=333)
W('30,2207', 0o05526, '', 'TC', 'BLANKET', line=334)
# Page 568
W('30,2210', 0o05217, '', 'TC', 'ENDOFJOB', line=336)
W('30,2211', 0o31751, '', 'CA', 'LANDMARK', line=337)
W('30,2212', 0o75063, '', 'MASK', 'PRIO7', '07000', line=338)
W('30,2213', 0o55745, '', 'TS', 'CXOFF', '08000 = OFFSET INDICATOR', line=339)
W('30,2214', 0o45061, '', 'CS', 'PRIO5', '5 8-5', line=340)
W('30,2215', 0o61745, '', 'AD', 'CXOFF', line=341)
W('30,2216', 0o00006, '', 'EXTEND', line=342)
W('30,2217', 0o62221, '', 'BZMF', '+2', 'OFF=0 THRU 5 OK', line=343)
W('30,2220', 0o02233, '', 'TC', 'S22DSPP', 'OFF=6.7 ILLEGAL REDISPLAY', line=344)
W('30,2221', 0o05560, '', 'TC', 'DOWNFLAG', line=345)
W('30,2222', 0o00141, '', 'ADRES', 'KNOWNFLG', 'CLEAR KNOWNFLG', kind='data', line=346)
W('30,2223', 0o31751, '', 'CA', 'LANDMARK', 'MASK A FROM ABCDE', line=347)
W('30,2224', 0o77707, '', 'MASK', '13,14,15', line=348)
W('30,2225', 0o00006, '', 'EXTEND', line=349)
W('30,2226', 0o62233, '', 'BZMF', 'S22DSPP', 'A=0,4,5,6,7  ILLEGAL REDISPLAY', line=350)
W('30,2227', 0o55744, '', 'TS', '22SUBSCL', 'TEMP', line=351)
W('30,2230', 0o45002, '', 'CS', 'BIT14', line=352)
W('30,2231', 0o61744, '', 'AD', '22SUBSCL', line=353)
W('30,2232', 0o10000, '', 'CCS', 'A', line=354)
W('30,2233', 0o04400, 'S22DSPP', 'TC', 'FALTON', '+ A=3 ILLEGAL REDISPLAY', line=355)
W('30,2234', 0o02200, '', 'TC', 'S22DSPPA', 'COMMON ERROR EXIT BACK TO DISPLAY', line=356)
W('30,2235', 0o02237, '', 'TC', '+2', '- A=1 KNOWN LMK  CHECK DE', line=357)
W('30,2236', 0o02263, '', 'TC', 'S22ABDE', '-0 A=2 UNKNOWN LMK, DE MEANINGLESS', line=358)
W('30,2237', 0o05546, '', 'TC', 'UPFLAG', line=359)
W('30,2240', 0o00141, '', 'ADRES', 'KNOWNFLG', 'SET KNOWNFLG', kind='data', line=360)
W('30,2241', 0o47713, '', 'CS', 'HIGH9', 'RESULT= 00077', line=361)
W('30,2242', 0o71751, '', 'MASK', 'LANDMARK', line=362)
W('30,2243', 0o55744, '', 'TS', '22SUBSCL', '000DE', line=363)
W('30,2244', 0o45017, '', 'CS', 'BIT1', line=364)
W('30,2245', 0o61744, '', 'AD', '22SUBSCL', line=365)
W('30,2246', 0o00006, '', 'EXTEND', line=366)
W('30,2247', 0o62263, '', 'BZMF', 'S22ABDE', 'DE=0,1 OK FOR BOTH N70,N71', line=367)
W('30,2250', 0o31747, '', 'CA', '8KK +1', '=0 FOR N71, NOT =0 FOR N70', line=368)
W('30,2251', 0o00006, '', 'EXTEND', line=369)
W('30,2252', 0o12233, '', 'BZF', 'S22DSPP', 'N71 REDISPLAY  DE MUST= 0 OR 1', line=370)
W('30,2253', 0o35013, '', 'CA', 'BIT5', 'N70 TEST DE= 50-57 OCTAL FOR ADV. ORBIT', line=371)
W('30,2254', 0o65033, '', 'AD', 'OCT50', 'SUM=00070', line=372)
W('30,2255', 0o71744, '', 'MASK', '22SUBSCL', '00D0', line=373)
W('30,2256', 0o40000, '', 'CS', 'A', line=374)
W('30,2257', 0o65033, '', 'AD', 'OCT50', line=375)
W('30,2260', 0o00006, '', 'EXTEND', line=376)
W('30,2261', 0o12273, '', 'BZF', 'DE-GR-50', 'D=5 OR DE=50-57, OK FOR N70', line=377)
W('30,2262', 0o02233, '', 'TC', 'S22DSPP', 'DE NOT 50-57  ILLEGAL, REDISPLAY', line=378)
W('30,2263', 0o06006, 'S22ABDE', 'TC', 'INTPRET', line=379)
W('30,2264', 0o67214, '', 'BOFF', 'SLOAD', kind='interp', line=380)
W('30,2265', 0o03347, '', '', 'KNOWNFLG', 'UNKNOWN LMK, DE MEANINGLESS', kind='operand', line=381)
W('30,2266', 0o03667, '', '', 'S22TOFF', kind='operand', line=382)
W('30,2267', 0o02745, '', '', '22SUBSCL', '=0 GET LLA FROM ASTRO, NOT=0 USE RLS', kind='operand', line=383)
W('30,2270', 0o52030, '', 'BHIZ', 'GOTO', kind='interp', line=384)
W('30,2271', 0o60137, '', '', 'OBTAINLL', 'GET LAT/LONG/ALT FROM ASTRO  N89', kind='operand', line=385)
# Page 569
W('30,2272', 0o60117, '', '', 'S22LSITE', 'GET LAT/LONG/ALT FROM RLS', kind='operand', line=387)
W('30,2273', 0o05372, 'DE-GR-50', 'TC', '2PHSCHNG', line=388)
W('30,2274', 0o00004, '', 'OCT', '00004', kind='data', line=389)
W('30,2275', 0o05022, '', 'OCT', '05022', kind='data', line=390)
W('30,2276', 0o13000, '', 'OCT', '13000', kind='data', line=391)
W('30,2277', 0o35022, '', 'CA', 'FIVE', line=392)
W('30,2300', 0o54301, '', 'TS', 'MARKINDX', line=393)
W('30,2301', 0o05546, '', 'TC', 'UPFLAG', line=394)
W('30,2302', 0o00025, '', 'ADRES', 'TARG2FLG', kind='data', line=395)
W('30,2303', 0o05560, '', 'TC', 'DOWNFLAG', line=396)
W('30,2304', 0o00024, '', 'ADRES', 'TARG1FLG', kind='data', line=397)
W('30,2305', 0o06006, '', 'TC', 'INTPRET', line=398)
W('30,2306', 0o77624, '', 'CALL', kind='interp', line=399)
W('30,2307', 0o30215, '', '', 'ADVORB', kind='operand', line=400)
W('30,2310', 0o77650, '', 'GOTO', kind='interp', line=401)
W('30,2311', 0o60100, '', '', 'DOV5N71', kind='operand', line=402)

# Page 570
# PROGRAM NAME:  OPTICS CALIBRATION ROUTINE
# MOD NO:  1
# MOD BY:  TOM KNATT
#
# FUNCTIONAL DESCRIPTION:  TO MEASURE THE EFFECT OF SOLAR RADIATION ON
# THE SXT TRUNNON ANGLE AND STORE THE MEASURED TRUNNION BIAS FOR P23
#
# CALLING SEQUENCE:     CALL
# R57
#
# SUBROUTINES CALLED:  DISPLAY ROUTINES
#
# NORMAL EXIT MODES:  VIA EGRESS
#
# ALARMS:  NONE
#
# ABORT MODES:  P23 ABORT IF MARKING SYSTEM OR EXTENDED VERB ACTIVE
#
# INPUT:  NONE REQUIRED, NORMALLY CALLED BY P23
#
# OUTPUT:  TRUNNION BIAS ANGLE: ANGLE DETERMINED WHEN SHAFT LINE OF SIGHT
# (SLOS) AND LANDMARK LINE OF SIGHT (LLOS) ARE SUPERIMPOSED.  THIS ANGLE
# MAY NOT BE EXACTLY ZERO BECAUSE OF UNEVEN HEATING OF THE OPTICS, FOR
# EXAMPLE.
#
# ERASABLE INITIALIZATION REQUIRED:  MRKBUF1, EXTVBACT
#
# DEBRIS:  RUPTREGS USED BY MARKRUPT AND ERASABLES USED BY DISPLAYS.

#   BANK 33
#   SETLOC P20S
#   BANK
#   COUNT* $$/R57
#   EBANK= MRKBUF1
W('37,2401', 0o77420, 'R57', 'STQ', 'EXIT', kind='interp', line=439)
W('37,2402', 0o02317, '', '', 'EGRESS', kind='operand', line=440)
W('37,2403', 0o35060, '', 'CAF', 'EBANK7', line=441)
W('37,2404', 0o54003, '', 'TS', 'EBANK', line=442)
W('37,2405', 0o36211, '', 'CAF', 'SIX', 'BIT2 = MARKING SYSTEM IN USE', line=443)
W('37,2406', 0o71044, '', 'MASK', 'EXTVBACT', 'BIT3 = EXTENDED VERB IN PROGRESS', line=444)
W('37,2407', 0o10000, '', 'CCS', 'A', line=445)
W('37,2410', 0o02460, '', 'TC', 'P23ABRT', 'SET, THEREFORE ABORT', line=446)
W('37,2411', 0o35016, '', 'CAF', 'BIT2', 'NOT SET', line=447)
W('37,2412', 0o27044, '', 'ADS', 'EXTVBACT', 'SET IT', line=448)
W('37,2413', 0o05546, 'R57A', 'TC', 'UPFLAG', 'SET V59FLAG (BIT 12 FLAG 5 TO INDICATE', line=449)
W('37,2414', 0o00116, '', 'ADRES', 'V59FLAG', 'CALIBRATION MARK', kind='data', line=450)
W('37,2415', 0o32463, '', 'CAF', 'V59NB', line=451)
W('37,2416', 0o04662, '', 'TC', 'BANKCALL', line=452)
W('37,2417', 0o20600, '', 'CADR', 'GOMARKFR', kind='data', line=453)
W('37,2420', 0o04106, '', 'TC', 'GOTOPOOH', 'TERMINATE', line=454)
W('37,2421', 0o02445, '', 'TC', 'ENDR57', line=455)
W('37,2422', 0o02445, '', 'TC', 'ENDR57', line=456)
W('37,2423', 0o35023, '', 'CAF', 'SEVEN', line=457)
# Page 571
W('37,2424', 0o05526, '', 'TC', 'BLANKET', 'BLANK OUT R1,R2,R3', line=459)
W('37,2425', 0o05217, '', 'TC', 'ENDOFJOB', line=460)
# STORE TRUNNION ANGLE (OCDU)
W('37,2426', 0o32462, 'MARKDISP', 'CAF', 'V06N87NB', line=462)
W('37,2427', 0o04662, '', 'TC', 'BANKCALL', line=463)
W('37,2430', 0o20600, '', 'CADR', 'GOMARKFR', kind='data', line=464)
W('37,2431', 0o04106, '', 'TC', 'GOTOPOOH', 'TERMINATE', line=465)
W('37,2432', 0o02437, '', 'TC', 'R57B', 'PROCEED', line=466)
W('37,2433', 0o02413, '', 'TC', 'R57A', 'ENTER (RECYCLE)', line=467)
W('37,2434', 0o35022, '', 'CAF', 'FIVE', line=468)
W('37,2435', 0o05526, '', 'TC', 'BLANKET', 'BLANK OUT R1,R3', line=469)
W('37,2436', 0o05217, '', 'TC', 'ENDOFJOB', line=470)
W('37,2437', 0o32465, 'R57B', 'CA', '19.77DEG', 'PUT FIXED INTO ERASABLE FOR MSU', line=471)
W('37,2440', 0o54001, '', 'TS', 'L', 'INSTRUCTION COMING UP', line=472)
W('37,2441', 0o31732, '', 'CA', 'MRKBUF1 +5', 'CONTAINS TRUNNION', line=473)
W('37,2442', 0o00006, '', 'EXTEND', line=474)
W('37,2443', 0o20001, '', 'MSU', 'L', "CONNECTS TRUNBIAS FROM 2'S TO 1'S", line=475)
W('37,2444', 0o55342, '', 'TS', 'TRUNBIAS', line=476)
W('37,2445', 0o05560, 'ENDR57', 'TC', 'DOWNFLAG', 'RESET V59FLAG', line=477)
W('37,2446', 0o00116, '', 'ADRES', 'V59FLAG', 'BIT 12 FLAG 5', kind='data', line=478)
W('37,2447', 0o35056, '', 'CAF', 'EBANK5', line=479)
W('37,2450', 0o54003, '', 'TS', 'EBANK', line=480)
W('37,2451', 0o35066, '', 'CAF', 'PRIO14', line=481)
W('37,2452', 0o05134, '', 'TC', 'NOVAC', 'THIS JOB CLEARS BIT IN', line=482)
#   EBANK= MARKSTAT
W('37,2453', 0o05534, '', '2CADR', 'ENDMARK', 'MARKING IN R57 SO R53 CAN TAKE OVER', kind='data', line=484)
W('37,2454', 0o04062, kind='data', line=484)

W('37,2455', 0o06006, '', 'TC', 'INTPRET', line=486)
W('37,2456', 0o77650, '', 'GOTO', kind='interp', line=487)
W('37,2457', 0o02317, '', '', 'EGRESS', kind='operand', line=488)
W('37,2460', 0o07755, 'P23ABRT', 'TC', 'BAILOUT', line=489)
W('37,2461', 0o01211, '', 'OCT', '01211', kind='data', line=490)
W('37,2462', 0o01527, 'V06N87NB', 'VN', '0687', kind='data', line=491)
W('37,2463', 0o16600, 'V59NB', 'VN', '5900', kind='data', line=492)
W('37,2464', 0o14600, 'V51NB', 'VN', '5100', kind='data', line=493)
W('37,2465', 0o61740, '19.77DEG', 'OCT', '61740', kind='data', line=494)

# Page 572
# PROGRAM DESCRIPTION
# MOD NO:  1
# MOD BY:  N. BRODEUR
#
# FUNCTIONAL DESCRIPTION
#
# TO PERFORM SIGHTING MARKS IN CONJUNCTION WITH THE RENDEZVOUS NAVIG-
# ATION PROGRAM.  CALLED BY ASTRONAUT VIA EXTENDED VERB.
#
# CALLING SEQUENCE:
#
# R21 VIA V57
# R23 VIA V 54
#
# SUBROUTINES CALLED:
#
# FLAGUP          FLAGDOWN        BANKCALL
# ENDOFJOB        GOMARK2         GOMARKF
# INTPRET         GENTRAN         KLEENEX
# ENDMARK
#
# NORMAL EXIT MODES:
#
# MARKRUPT USED BY SXTMARK HAS BEEN MODIFIED TO STORE MARK IN MRKBUF2
# FOR USE BY R22.  WHEN ASTRONAUT IS FINISHED TAKING MARKS, HE HITS AN
# PROCEED, R21 IS TERMINATED THUS CAUSING THE FINAL MARK TO BE TRANSFRD
# TO MRKBUF2 FOR PROCESSING BY R22
#
# ALARM OR ABORT EXIT MODES:
#
# NONE
#
# OUTPUT:
#
# 7 REGISTER MRKBUF2 CONTAINING TIME2,TIME1,CDUY,OPTICS X,CDUZ, OPTICS Y,
# CDUX.
#
# ERASABLE INITIALIZATION REQUIRED
#
# FLAGS SET AND RESET
# R21MARK         (COMMUNICATION TO MARKRUPT TO STORE MARKS IN MRKBUF1 +2)
# R23FLG          INDICATES COAS MARKING
#
# DEBRIS

#   EBANK= MRKBUF1
#   SETLOC RENDEZ
#   BANK

#   COUNT* $$/R21

W('37,2466', 0o05546, 'R21CSM', 'TC', 'UPFLAG', 'SET R21MARK', line=548)
W('37,2467', 0o00037, '', 'ADRES', 'R21MARK', 'BIT 14 FLAG 2', kind='data', line=549)
W('37,2470', 0o37716, 'R23CSM', 'CA', 'NEGONE', line=550)
W('37,2471', 0o55725, '', 'TS', 'MRKBUF1', line=551)
W('37,2472', 0o55734, '', 'TS', 'MRKBUF2', line=552)
W('37,2473', 0o30075, '', 'CA', 'FLAGWRD1', line=553)
W('37,2474', 0o75007, '', 'MASK', 'R23BIT', 'TEST R23FLG', line=554)
W('37,2475', 0o00006, '', 'EXTEND', line=555)
W('37,2476', 0o12531, '', 'BZF', 'R21C1', 'NOT SET REGULAR R21 MARKING', line=556)
W('37,2477', 0o32556, '', 'CAF', 'V0694', 'R23 BACKUP MARKING', line=557)
W('37,2500', 0o04662, '', 'TC', 'BANKCALL', 'DISPLAY SHAFT + TRUNNION', line=558)
W('37,2501', 0o20561, '', 'CADR', 'GOMARKF', kind='data', line=559)
W('37,2502', 0o02550, '', 'TC', 'R21END', 'TERM', line=560)
W('37,2503', 0o02505, '', 'TC', '+2', 'PROC', line=561)
# Page 573
W('37,2504', 0o02477, '', 'TC', '-5', 'ENTER', line=563)
W('37,2505', 0o32555, 'R23CSM1', 'CAF', 'V53', 'PERFORM ALT LOST SIGHT MARK', line=564)
W('37,2506', 0o04662, '', 'TC', 'BANKCALL', line=565)
W('37,2507', 0o20564, '', 'CADR', 'GOMARK2', kind='data', line=566)
W('37,2510', 0o02550, '', 'TC', 'R21END', 'V34: TERMINATE R23', line=567)
W('37,2511', 0o12537, '', 'TCF', 'R21CSMA', 'PROCEED: END BACK UP MARKING (R23)', line=568)
W('37,2512', 0o36211, '', 'CAF', 'SIX', 'TRANSFER MRKBUF1 TO MRKBUF2', line=569)
W('37,2513', 0o05606, '', 'TC', 'GENTRAN', line=570)
W('37,2514', 0o01725, '', 'ADRES', 'MRKBUF1', kind='data', line=571)
W('37,2515', 0o01734, '', 'ADRES', 'MRKBUF2', kind='data', line=572)
W('37,2516', 0o00006, '', 'EXTEND', line=573)
W('37,2517', 0o30025, '', 'DCA', 'TIME2', line=574)
W('37,2520', 0o53726, '', 'DXCH', 'MRKBUF1', 'READ TIME', line=575)
W('37,2521', 0o30033, '', 'CA', 'CDUY', 'READ CDU ANGLES', line=576)
W('37,2522', 0o55727, '', 'TS', 'MRKBUF1 +2', line=577)
W('37,2523', 0o30034, '', 'CA', 'CDUZ', line=578)
W('37,2524', 0o55731, '', 'TS', 'MRKBUF1 +4', line=579)
W('37,2525', 0o30032, '', 'CA', 'CDUX', line=580)
W('37,2526', 0o55733, '', 'TS', 'MRKBUF1 +6', line=581)
W('37,2527', 0o00003, '', 'RELINT', line=582)
W('37,2530', 0o02505, '', 'TC', 'R23CSM1', line=583)
W('37,2531', 0o32464, 'R21C1', 'CAF', 'V51NB', line=584)
W('37,2532', 0o04662, '', 'TC', 'BANKCALL', line=585)
W('37,2533', 0o20564, '', 'CADR', 'GOMARK2', kind='data', line=586)
W('37,2534', 0o02550, '', 'TC', 'R21END', 'V34: TERMINATE R21', line=587)
W('37,2535', 0o12537, '', 'TCF', 'R21CSMA', 'PROCEED: END R21', line=588)
W('37,2536', 0o12531, '', 'TCF', 'R21C1', 'RECYCLE', line=589)

W('37,2537', 0o31725, 'R21CSMA', 'CA', 'MRKBUF1', 'IF -1 NO MARK', line=591)
W('37,2540', 0o65017, '', 'AD', 'ONE', line=592)
W('37,2541', 0o00006, '', 'EXTEND', line=593)
W('37,2542', 0o12550, '', 'BZF', 'R21END', 'ZERO = NO MARK', line=594)
W('37,2543', 0o36211, '', 'CAF', 'SIX', 'MARK THEREFORE TRANSFER IT TO MRKBUF2', line=595)
W('37,2544', 0o05606, 'R21CSM1', 'TC', 'GENTRAN', 'TRANSFER MRKBUF1 TO MRKBUF2', line=596)
W('37,2545', 0o01725, '', 'ADRES', 'MRKBUF1', kind='data', line=597)
W('37,2546', 0o01734, '', 'ADRES', 'MRKBUF2', kind='data', line=598)
W('37,2547', 0o00003, '', 'RELINT', line=599)
W('37,2550', 0o04662, 'R21END', 'TC', 'BANKCALL', line=600)
W('37,2551', 0o20560, '', 'CADR', 'KLEENEX', kind='data', line=601)
W('37,2552', 0o05560, '', 'TC', 'DOWNFLAG', 'RESET R21MARK', line=602)
W('37,2553', 0o00037, '', 'ADRES', 'R21MARK', 'BIT 14 FLAG 2', kind='data', line=603)
W('37,2554', 0o05534, '', 'TC', 'ENDMARK', 'END MARKING AND ENDJOB', line=604)
W('37,2555', 0o15200, 'V53', 'VN', '5300', kind='data', line=605)
W('37,2556', 0o01536, 'V0694', 'VN', '0694', kind='data', line=606)

# Page 574
# PREFERRED TRACKING ATTITUDE ROUTINE R61CSM
#
# PROGRAM DESCRIPTION
# MOD NO:  2
# MOD BY:  N. BRODEUR
#
# FUNCTIONAL DESCRIPTION:
#
# TO COMPUTE THE PREFERRED TRACKING ATTITUDE OF THE CSM TO ENABLE OPTICS
# TRACKING OF THE LM AND TO PERFORM THE MANEUVER TO THE PREFERRED
# OR X-AXIS TRACKING ATTITUDE.
#
# CALLING SEQUENCE:
#
# TC      BANKCALL
# CADR    R61CSM
#
# SUBROUTINE CALLED
#
# MAKECADR        BANKCALL
# INTPRET         FLAGUP          FLAGDOWN
# BANKJUMP        CRS61.1         R60CSM
# PHASCHNG
#
# NORMAL EXIT MODES:
#
# NORMAL RETURN TO CALLER + 1
#
# OUTPUT:
#
# SEE OUTPUT FOR CRS61.1 & ATTITUDE MANEUVER ROUTINE (R60CSM)
#
# ERASABLE INITIALIZATION REQUIRED
#
# GENRET USED TO SAVE Q FOR RETURN
# R61CNTR MUST BE PRESET TO ZERO
#
# FLAGS SET + RESET
#
# 3-AXIS FLAG
#
# DEBRIS
#
# SEE SUBROUTINES

#   EBANK= GENRET
#   COUNT* $$/R61  # ROUTINES -- NAVIGATION -- PREF. TR. 9TT=

W('37,2557', 0o35057, 'R61CSM', 'CAF', 'EBANK6', 'SWITCH TO EBANK 6', line=657)
W('37,2560', 0o56003, '', 'XCH', 'EBANK', line=658)
W('37,2561', 0o55771, '', 'TS', 'SAVBNK', 'SAVE EBANK', line=659)
W('37,2562', 0o04711, '', 'TC', 'MAKECADR', line=660)
W('37,2563', 0o55770, '', 'TS', 'GENRET', line=661)
W('37,2564', 0o11775, '', 'CCS', 'R61CNTR', 'TEST R61DNTR', line=662)
W('37,2565', 0o02616, '', 'TC', 'DECRM61', 'NOT READY TO DO R61', line=663)
W('37,2566', 0o02570, '', 'TC', '+2', 'DO R61', line=664)
W('37,2567', 0o02617, '', 'TC', 'DECRM61 +1', line=665)
W('37,2570', 0o06006, '', 'TC', 'INTPRET', line=666)
W('37,2571', 0o77624, '', 'CALL', kind='interp', line=667)
W('37,2572', 0o71343, '', '', 'CRS61.1', 'LOS DETERMINATION + VEH ATTITUDE', kind='operand', line=668)
W('37,2573', 0o77776, '', 'EXIT', kind='interp', line=669)
W('37,2574', 0o50154, '', 'INDEX', 'MPAC', line=670)
W('37,2575', 0o02576, '', 'TC', '+1', line=671)
W('37,2576', 0o02615, '', 'TC', 'R61END', 'SUBROUTINE DRIVING DAP        (EXIT R61)', line=672)
# OR AUTO MODE NOT SET          (EXIT R61)
# OR SKIKFLAG SET               (EXIT R61)
W('37,2577', 0o05560, 'R61C1', 'TC', 'DOWNFLAG', 'RESET 3-AXIS FLAG', line=675)
W('37,2600', 0o00124, '', 'ADRES', '3AXISFLG', 'BIT 6 FLAG 5', kind='data', line=676)
# Page 575
W('37,2601', 0o45017, '', 'CS', 'ONE', 'SET R61CNTR NEG. TO INDICATE KALCMANU', line=678)
W('37,2602', 0o55775, '', 'TS', 'R61CNTR', line=679)

W('37,2603', 0o05546, '', 'TC', 'UPFLAG', 'SET FLAG FOR PRIORITY DISPLAYS FOR R60', line=681)
W('37,2604', 0o00077, '', 'ADRES', 'PDSPFLAG', 'BIT 12 FLAG 4', kind='data', line=682)
W('37,2605', 0o04662, '', 'TC', 'BANKCALL', line=683)
W('37,2606', 0o56000, '', 'CADR', 'R60CSM', kind='data', line=684)
W('37,2607', 0o05560, '', 'TC', 'DOWNFLAG', 'RESET FLAG FOR PRIORITY DISPLAYS IN R60', line=685)
W('37,2610', 0o00077, '', 'ADRES', 'PDSPFLAG', 'BIT 12 FLAG 4', kind='data', line=686)
W('37,2611', 0o05412, '', 'TC', 'PHASCHNG', line=687)
W('37,2612', 0o00111, '', 'OCT', '00111', kind='data', line=688)
W('37,2613', 0o35021, '', 'CAF', 'ZERO', line=689)
W('37,2614', 0o02616, '', 'TC', 'DECRM61', line=690)
W('37,2615', 0o36214, 'R61END', 'CAF', 'THREE', line=691)

W('37,2616', 0o55775, 'DECRM61', 'TS', 'R61CNTR', line=693)

W('37,2617', 0o31770, '', 'CAE', 'GENRET', line=695)
W('37,2620', 0o22000, '', 'LXCH', 'A', 'RETURN IS IN L', line=696)
W('37,2621', 0o31771, '', 'CA', 'SAVBNK', 'RESTORE EBANK', line=697)
W('37,2622', 0o56003, '', 'XCH', 'EBANK', line=698)
W('37,2623', 0o22000, '', 'LXCH', 'A', 'RETURN IS NOW BACK IN A', line=699)
W('37,2624', 0o04704, '', 'TC', 'BANKJUMP', 'EXIT R61', line=700)
#   BANK 13
#   SETLOC P20S2
#   BANK

#   EBANK= MRKBUF1
# Page 576
# BVECTOR PERFORMS COMPUTATIONS FOR
#
# DELTAQ, THE MEASURED DEVIATION BASED ON THE DIFFERENCE BETWEEN THE CSM-LEM
# STATE VECTOR ESTIMATES AND THE ACTUAL TRACKING MEASUREMENT.
#
# US, THE MODIFIED FICTITIOUS STAR DIRECTION VECTOR
# GEOMETRY VECTORY B ASSOCIATED WITH EACH TRACKING MEASUREMENT.
#
# INPUT
#
# UM,1/2 UNIT VECTOR ALONG THE CSM-LM LINE-OF-SIGHT (BASIC REF. SYSTEM)
#
# USTAR,FICTITIOUS STAR DIRECTION (1/2 UNIT VECTOR)
#
# RCLP,RELATIVE CSM TO LM POSITION VECTOR
#
# OUTPUT
#
# USTAR,MODIFIED FICTITIOUS STAR DIRECTION (1/2 UNIT VECTOR)
#
# BVECTOR = 9 DIMENSIONAL BVECTOR (1/2 UNIT VEC.)
#
# DELTAQ = MEASURED DEVIATION
#
# CALLING SEQUENCE
#
# L       CALL BVECTORS
#
# NORMAL EXIT
#
# L+1 OF CALLING SEQUENCE

#   COUNT 23/20SUB

W('23,3043', 0o77620, 'BVECTORS', 'STQ', kind='interp', line=741)
W('23,3044', 0o02317, '', '', 'EGRESS', kind='operand', line=742)
W('23,3045', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=743)
W('23,3046', 0o03531, '', '', 'RCLP', 'RELATIVE POSITION VECTOR', kind='operand', line=744)
W('23,3047', 0o14033, '', 'STODL', '26D', 'RCLP UNIT VEC', kind='interp', line=745)
W('23,3050', 0o00045, '', '', '36D', 'RCLP ABS VALUE', kind='operand', line=746)
W('23,3051', 0o25301, '', 'STOVL', 'TEMPOR1', 'MOVE TO SAFE LOCATION', kind='interp', line=747)
W('23,3052', 0o01245, '', '', 'USTAR', kind='operand', line=748)
W('23,3053', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=749)
W('23,3054', 0o00033, '', '', '26D', 'USTAR = UNIT(US X UCL)', kind='operand', line=750)
W('23,3055', 0o37502, '', 'STCALL', 'BVECTOR', kind='interp', line=751)
W('23,3056', 0o56750, '', '', 'GRP2PC', 'PHASE CHANGE', kind='operand', line=752)
W('23,3057', 0o77775, '', 'VLOAD', kind='interp', line=753)
W('23,3060', 0o03502, '', '', 'BVECTOR', kind='operand', line=754)
W('23,3061', 0o01245, '', 'STORE', 'USTAR', kind='interp', line=755)
W('23,3062', 0o72441, '', 'DOT', 'SL1', kind='interp', line=756)
W('23,3063', 0o01235, '', '', 'UM', 'USTAR DOT UM', kind='operand', line=757)
W('23,3064', 0o45326, '', 'ACOS', 'DSU', kind='interp', line=758)
W('23,3065', 0o15325, '', '', 'DP1/4TH', kind='operand', line=759)
W('23,3066', 0o41301, '', 'NORM', 'DMP', kind='interp', line=760)
W('23,3067', 0o00047, '', '', 'X1', kind='operand', line=761)
W('23,3070', 0o07103, '', '', 'PI/4.0', kind='operand', line=762)
W('23,3071', 0o53605, '', 'DMP', 'SRR*', kind='interp', line=763)
W('23,3072', 0o01301, '', '', 'TEMPOR1', 'RCLP ABS VALUE', kind='operand', line=764)
W('23,3073', 0o21576, '', '', '0 -3,1', 'ADJUST SCALING', kind='operand', line=765)
W('23,3074', 0o27524, '', 'STOVL', 'DELTAQ', kind='interp', line=766)
W('23,3075', 0o15335, '', '', 'ZEROVECS', kind='operand', line=767)
W('23,3076', 0o03510, '', 'STORE', 'BVECTOR +6', kind='interp', line=768)
W('23,3077', 0o03516, '', 'STORE', 'BVECTOR +12D', kind='interp', line=769)
W('23,3100', 0o77650, '', 'GOTO', kind='interp', line=770)
# Page 577
W('23,3101', 0o02317, '', '', 'EGRESS', kind='operand', line=772)
W('23,3102', 0o31103, 'PI/4.0', '2DEC', '.785398164', kind='data', line=773)
W('23,3103', 0o36652, kind='data', line=773)

# Page 578
# GETUM:  DETERMINES THE LINE OF SIGHT UNIT VECTOR UM IN THE BASIC REFERENCE
# COORDINATE SYSTEM FROM THE OPTICS SHAFT AND TRUNNION ANGLES AND THE IMU
# GIMBAL ANGLES.
#
# INPUT
#
# MARKDATA, BASE ADDRESS OF MARK DATA
# REFSMMAT, ROTATION MATRIX FROM STABLE MEMBER TO BASIC REF. COORD. SYSTEM
#
# SUBROUTINES CALLED-
#
# SXTNB -- SEXT. ANGULAR READINGS TO NAV. BASE COOR.
# NBSM -- TRANSFORM FROM NAV. BASE TO STABLE MEMBER
#
# OUTPUT
#
# MPAC = LINE OF SIGHT 1/2 UNIT VECTOR IN BASIC REFERENCE SYSTEM
#
# CALLING SEQUENCE
#
# L       CALL GETUM
#
# NORMAL EXIT
#
# L+1 OF CALLING SEQUENCE

W('23,3104', 0o40220, 'GETUM', 'STQ', 'SETPD', kind='interp', line=802)
W('23,3105', 0o02317, '', '', 'EGRESS', kind='operand', line=803)
W('23,3106', 0o00001, '', '', '0', kind='operand', line=804)
W('23,3107', 0o76740, '', 'LXC,1', 'VLOAD*', kind='interp', line=805)
W('23,3110', 0o01242, '', '', 'MARKDATA', 'CONTAINS ADDRESS OF MARK DATA', kind='operand', line=806)
W('23,3111', 0o00002, '', '', '1,1', kind='operand', line=807)
W('23,3112', 0o23676, '', 'STODL*', 'MARKDOWN +1', 'TRANSFER DATA FROM WORKING STORAGE', kind='interp', line=808)
W('23,3113', 0o00001, '', '', '0,1', 'TO MARKDOWN ARRAY FOR DOWNLINK', kind='operand', line=809)
W('23,3114', 0o03675, '', 'STORE', 'MARKDOWN', kind='interp', line=810)
W('23,3115', 0o77774, '', 'AXT,2', kind='interp', line=811)
W('23,3116', 0o00002, '', '', '2', kind='operand', line=812)
W('23,3117', 0o67064, '', 'XSU,2', 'SXA,2', kind='interp', line=813)
W('23,3120', 0o00046, '', '', 'X1', 'X1 = MARKDATA', kind='operand', line=814)
W('23,3121', 0o00050, '', '', 'S1', 'S1 = MARKDATA(ADR) +2', kind='operand', line=815)
W('23,3122', 0o77624, '', 'CALL', kind='interp', line=816)
W('23,3123', 0o46000, '', '', 'SXTNB', 'SEXT. ANGULAR READINGS TO NAV. BASE COOR.', kind='operand', line=817)
W('23,3124', 0o77624, '', 'CALL', kind='interp', line=818)
W('23,3125', 0o47606, '', '', 'NBSM', 'TRANSFORM FROM NAV. BASE TO STABLE MEM.', kind='operand', line=819)
W('23,3126', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=820)
W('23,3127', 0o01736, '', '', 'REFSMMAT', kind='operand', line=821)
W('23,3130', 0o77650, '', 'GOTO', '', 'MPAC = (UM) LINE OF SIGHT VECTOR', kind='interp', line=822)
W('23,3131', 0o02317, '', '', 'EGRESS', 'EXIT', kind='operand', line=823)

# Page 579
# RENDEZVOUS TRACKING DATA PROCESSING ROUTINE (R22)
#
# PURPOSE       (1) TO PROCESS RENDEZVOUS SIGHTING MARK DATA TO UPDATE THE STATE VECTOR OF EITHER THE CSM OR LM AS
# DEFINED BY THE RENDEZVOUS NAVIGATION PROGRAM (P20).
#
# ASSUMPTIONS   (1) THIS ROUTINE IS MANUALLY SELECTED BY THE ASTRONAUT BY V55E WHENEVER RENDEZVOUS SIGHTING MARKS
# ARE DESIRED.  ITS SELECTION, HOWEVER, IS LIMITED TO PERIODS WHEN THE CMC IS HOLDING FOR A V/N FLASHING
# DATA DISPLAY.  THIS ROUTINE RETURNS TO THE ORIGINAL PROGRAM AT THE INTERRUPTED DISPLAY.

#   BANK 34
#   SETLOC P20S3
#   BANK

#   COUNT 34/R22

W('34,2630', 0o37663, 'R22', 'CAF', 'PRIO26', line=841)
W('34,2631', 0o55056, '', 'TS', 'PHSPRDT2', line=842)
W('34,2632', 0o05210, '', 'TC', 'PRIOCHNG', line=843)
W('34,2633', 0o37714, '', 'CA', 'NEG3', line=844)
W('34,2634', 0o55734, '', 'TS', 'MRKBUF2', line=845)
W('34,2635', 0o06006, '', 'TC', 'INTPRET', line=846)
W('34,2636', 0o77634, '', 'RTB', kind='interp', line=847)
W('34,2637', 0o45510, '', '', 'LOADTIME', kind='operand', line=848)
W('34,2640', 0o01152, '', 'STORE', 'VHFTIME', 'PRESENT TIME', kind='interp', line=849)
W('34,2641', 0o77624, 'REND1', 'CALL', kind='interp', line=850)
W('34,2642', 0o56750, '', '', 'GRP2PC', kind='operand', line=851)
W('34,2643', 0o77624, '', 'CALL', kind='interp', line=852)
W('34,2644', 0o56404, '', '', 'WAITONE', kind='operand', line=853)
W('34,2645', 0o77776, 'REND1A', 'EXIT', kind='interp', line=854)
W('34,2646', 0o31734, '', 'CA', 'MRKBUF2', line=855)
W('34,2647', 0o00006, '', 'EXTEND', line=856)
W('34,2650', 0o12653, '', 'BZF', 'REND2', line=857)
W('34,2651', 0o00006, '', 'EXTEND', line=858)
W('34,2652', 0o62672, '', 'BZMF', 'REND3A', line=859)
W('34,2653', 0o36211, 'REND2', 'CAF', 'SIX', line=860)
W('34,2654', 0o05606, '', 'TC', 'GENTRAN', line=861)
W('34,2655', 0o01734, '', 'ADRES', 'MRKBUF2', kind='data', line=862)
W('34,2656', 0o01224, '', 'ADRES', 'MARKTIME', 'MARKTIME MUST BE CONTIGUOUS WITH VTEMP', kind='data', line=863)
W('34,2657', 0o37714, '', 'CAF', 'NEG3', 'NEG VALUE TO INDICATE VALUES USED', line=864)
W('34,2660', 0o55734, '', 'TS', 'MRKBUF2', line=865)
W('34,2661', 0o00003, '', 'RELINT', line=866)
W('34,2662', 0o06006, '', 'TC', 'INTPRET', line=867)
W('34,2663', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=868)
W('34,2664', 0o04667, '', '', 'SOURCFLG', '0 = OPTICS DATA', kind='operand', line=869)
W('34,2665', 0o56750, '', '', 'GRP2PC', kind='operand', line=870)
W('34,2666', 0o52131, '', 'SSP', 'GOTO', kind='interp', line=871)
W('34,2667', 0o01243, '', '', 'MARKDATA', kind='operand', line=872)
W('34,2670', 0o01224, '', 'ECADR', 'VTEMP -2', kind='data', line=873)
W('34,2671', 0o70715, '', '', 'REND4', kind='operand', line=874)
W('34,2672', 0o06006, 'REND3A', 'TC', 'INTPRET', line=875)
W('34,2673', 0o77624, 'REND3', 'CALL', kind='interp', line=876)
# Page 580
W('34,2674', 0o56750, '', '', 'GRP2PC', kind='operand', line=878)
W('34,2675', 0o77624, '', 'CALL', kind='interp', line=879)
W('34,2676', 0o56404, '', '', 'WAITONE', kind='operand', line=880)
W('34,2677', 0o77614, '', 'BOFF', kind='interp', line=881)
W('34,2700', 0o04746, '', '', 'VHFRFLAG', kind='operand', line=882)
W('34,2701', 0o70645, '', '', 'REND1A', kind='operand', line=883)
W('34,2702', 0o77634, '', 'RTB', kind='interp', line=884)
W('34,2703', 0o45510, '', '', 'LOADTIME', 'PRESENT TIME', kind='operand', line=885)
W('34,2704', 0o45225, '', 'DSU', 'DSU', kind='interp', line=886)
W('34,2705', 0o14650, '', '', '60SECDP', '1 MIN', kind='operand', line=887)
W('34,2706', 0o01152, '', '', 'VHFTIME', 'LAST READING OF RADAR', kind='operand', line=888)
W('34,2707', 0o45040, '', 'BMN', 'CALL', kind='interp', line=889)
W('34,2710', 0o70645, '', '', 'REND1A', kind='operand', line=890)
W('34,2711', 0o56415, '', '', 'RANGERD', 'READ RADAR RANGE', kind='operand', line=891)
W('34,2712', 0o77745, '', 'DLOAD', kind='interp', line=892)
W('34,2713', 0o01225, '', '', 'MARKTIME', kind='operand', line=893)
W('34,2714', 0o01152, '', 'STORE', 'VHFTIME', 'FOR DOWNLINK', kind='interp', line=894)
W('34,2715', 0o77624, 'REND4', 'CALL', kind='interp', line=895)
W('34,2716', 0o56343, '', '', 'SETINTG', 'SET INTEGRV FLAGS', kind='operand', line=896)
W('34,2717', 0o45014, '', 'BON', 'CALL', kind='interp', line=897)
W('34,2720', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=898)
W('34,2721', 0o71152, '', '', 'CSMUPP', 'BRANCH IF CSM UPDATE', kind='operand', line=899)
W('34,2722', 0o27162, '', '', 'INTEGRV', kind='operand', line=900)
W('34,2723', 0o77624, '', 'CALL', kind='interp', line=901)
W('34,2724', 0o56750, '', '', 'GRP2PC', 'PHASE CHANGE', kind='operand', line=902)
W('34,2725', 0o77624, '', 'CALL', kind='interp', line=903)
W('34,2726', 0o56343, '', '', 'SETINTG', 'SET INTEGRV FLAGS', kind='operand', line=904)
W('34,2727', 0o77614, '', 'CLEAR', kind='interp', line=905)
W('34,2730', 0o01674, '', '', 'VINTFLAG', 'SET INTEGRATION VEHICLE TO LM', kind='operand', line=906)
W('34,2731', 0o43014, 'REND5', 'BOFF', 'SET', kind='interp', line=907)
W('34,2732', 0o02756, '', '', 'RENDWFLG', kind='operand', line=908)
W('34,2733', 0o70735, '', '', 'REND5A', 'DO NOT INTEGRATE W IF FLAG = 0', kind='operand', line=909)
W('34,2734', 0o01476, '', '', 'DIM0FLAG', kind='operand', line=910)
W('34,2735', 0o77624, 'REND5A', 'CALL', kind='interp', line=911)
W('34,2736', 0o27162, '', '', 'INTEGRV', kind='operand', line=912)
W('34,2737', 0o77624, '', 'CALL', kind='interp', line=913)
W('34,2740', 0o56547, '', '', 'SHIFTNDX', 'SET EARTH MOON SCALING INDEX', kind='operand', line=914)
W('34,2741', 0o77624, '', 'CALL', kind='interp', line=915)
W('34,2742', 0o71241, '', '', 'CMPOS', 'SET CSM POSITION', kind='operand', line=916)
W('34,2743', 0o45014, '', 'SET', 'CALL', kind='interp', line=917)
W('34,2744', 0o02464, '', '', 'INCORFLG', 'SET FOR 1ST PASS', kind='operand', line=918)
W('34,2745', 0o71250, '', '', 'LMPOS', 'SET LM POSITION', kind='operand', line=919)
W('34,2746', 0o43014, '', 'CLEAR', 'BON', kind='interp', line=920)
W('34,2747', 0o01671, '', '', 'ORBWFLAG', 'CLEAR FOR ORBITAL AND CISLUNAR', kind='operand', line=921)
W('34,2750', 0o02716, '', '', 'RENDWFLG', kind='operand', line=922)
W('34,2751', 0o70761, '', '', 'REND6', kind='operand', line=923)
W('34,2752', 0o77745, '', 'DLOAD', kind='interp', line=924)
W('34,2753', 0o02001, '', '', 'WRENDPOS', kind='operand', line=925)
W('34,2754', 0o34001, '', 'STCALL', '0', '0 = WRENDPOS  1 = WRENDVEL', kind='interp', line=926)
W('34,2755', 0o56565, '', '', 'INITIALW', 'INTIIALIZE W MATRIX', kind='operand', line=927)
# Page 581
W('34,2756', 0o77745, '', 'DLOAD', kind='interp', line=929)
W('34,2757', 0o15335, '', '', 'ZEROVECS', kind='operand', line=930)
W('34,2760', 0o01126, '', 'STORE', 'VHFCNT', 'ZERO OUT VHFCNT AND TRKMKCNT', kind='interp', line=931)
W('34,2761', 0o77614, 'REND6', 'SET', kind='interp', line=932)
W('34,2762', 0o02476, '', '', 'RENDWFLG', kind='operand', line=933)
W('34,2763', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=934)
W('34,2764', 0o01215, '', '', 'LEMPOS', kind='operand', line=935)
W('34,2765', 0o01207, '', '', 'CSMPOS', kind='operand', line=936)
W('34,2766', 0o03531, '', 'STORE', 'RCLP', 'LM - CSM', kind='interp', line=937)
W('34,2767', 0o43056, 'REND7', 'UNIT', 'BON', kind='interp', line=938)
W('34,2770', 0o04707, '', '', 'SOURCFLG', kind='operand', line=939)
W('34,2771', 0o71163, '', '', 'REND14', 'BRANCH IF DATA IS RADAR', kind='operand', line=940)
W('34,2772', 0o01273, '', 'STORE', 'UCL', kind='interp', line=941)
W('34,2773', 0o45014, '', 'BOFF', 'CALL', kind='interp', line=942)
W('34,2774', 0o02744, '', '', 'INCORFLG', kind='operand', line=943)
W('34,2775', 0o71007, '', '', 'REND9', kind='operand', line=944)
W('34,2776', 0o47104, '', '', 'GETUM', 'CALCULATE UM LINE OF SIGHT', kind='operand', line=945)
W('34,2777', 0o25235, '', 'STOVL', 'UM', kind='interp', line=946)
W('34,3000', 0o01273, '', '', 'UCL', kind='operand', line=947)
W('34,3001', 0o40035, '', 'VXV', 'BOV', kind='interp', line=948)
W('34,3002', 0o01235, '', '', 'UM', 'UCL X UM', kind='operand', line=949)
W('34,3003', 0o71004, '', '', 'REND8', kind='operand', line=950)
W('34,3004', 0o40056, 'REND8', 'UNIT', 'BOV', kind='interp', line=951)
W('34,3005', 0o70673, '', '', 'REND3', 'BRANCH IF OVERFLOW IGNORE MARK', kind='operand', line=952)
W('34,3006', 0o01245, '', 'STORE', 'USTAR', kind='interp', line=953)
W('34,3007', 0o77624, 'REND9', 'CALL', kind='interp', line=954)
W('34,3010', 0o47043, '', '', 'BVECTORS', kind='operand', line=955)
W('34,3011', 0o77214, '', 'BON', 'VLOAD', kind='interp', line=956)
W('34,3012', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=957)
W('34,3013', 0o71017, '', '', 'REND9A', kind='operand', line=958)
W('34,3014', 0o03502, '', '', 'BVECTOR', kind='operand', line=959)
W('34,3015', 0o77676, '', 'VCOMP', kind='interp', line=960)
W('34,3016', 0o03502, '', 'STORE', 'BVECTOR', kind='interp', line=961)
W('34,3017', 0o77624, 'REND9A', 'CALL', kind='interp', line=962)
W('34,3020', 0o56750, '', '', 'GRP2PC', kind='operand', line=963)
W('34,3021', 0o77614, '', 'BON', kind='interp', line=964)
W('34,3022', 0o00706, '', '', 'R23FLG', kind='operand', line=965)
W('34,3023', 0o71214, '', '', 'REND15', 'BRANCH IF BACKUP OPTICS (R23 WORKING)', kind='operand', line=966)
W('34,3024', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=967)
W('34,3025', 0o31336, '', '', 'SXTVAR', kind='operand', line=968)
W('34,3026', 0o31340, '', '', 'IMUVAR', kind='operand', line=969)
W('34,3027', 0o27526, 'REND10', 'STOVL', 'VARIANCE', 'TEMP STORAGE FOR VARIANCE CALC.', kind='interp', line=970)
W('34,3030', 0o03531, '', '', 'RCLP', kind='operand', line=971)
W('34,3031', 0o60246, '', 'ABVAL', 'NORM', kind='interp', line=972)
W('34,3032', 0o00047, '', '', 'X1', kind='operand', line=973)
W('34,3033', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=974)
W('34,3034', 0o03526, '', '', 'VARIANCE', kind='operand', line=975)
W('34,3035', 0o45070, '', 'XAD,1', 'CALL', kind='interp', line=976)
W('34,3036', 0o00046, '', '', 'X1', kind='operand', line=977)
W('34,3037', 0o56547, '', '', 'SHIFTNDX', 'GET EARTH MOON SCALING INDEX', kind='operand', line=978)
# Page 582
W('34,3040', 0o56070, '', 'XAD,1', 'XAD,1', kind='interp', line=980)
W('34,3041', 0o00047, '', '', 'X2', kind='operand', line=981)
W('34,3042', 0o00047, '', '', 'X2', kind='operand', line=982)
W('34,3043', 0o72257, '', 'SR*', 'TLOAD', kind='interp', line=983)
W('34,3044', 0o20577, '', '', '0 -2,1', 'ADJUST SCALING TO B-40', kind='operand', line=984)
W('34,3045', 0o00155, '', '', 'MPAC', kind='operand', line=985)
W('34,3046', 0o03526, '', 'STORE', 'VARIANCE', kind='interp', line=986)
W('34,3047', 0o54335, '', 'SLOAD', 'SR', kind='interp', line=987)
W('34,3050', 0o02400, '', '', 'INTVAR', 'INTEGRATION VARIANCE SCALED B-15', kind='operand', line=988)
W('34,3051', 0o20632, '', '', '25D', 'SCALE IT B-40', kind='operand', line=989)
W('34,3052', 0o47171, '', 'TAD', 'RTB', kind='interp', line=990)
W('34,3053', 0o03526, '', '', 'VARIANCE', kind='operand', line=991)
W('34,3054', 0o45565, '', '', 'TPMODE', kind='operand', line=992)
W('34,3055', 0o03526, '', 'STORE', 'VARIANCE', kind='interp', line=993)
W('34,3056', 0o76214, '', 'BOFF', 'TAD', kind='interp', line=994)
W('34,3057', 0o04747, '', '', 'SOURCFLG', 'BRANCH IF NOT VHF RADAR', kind='operand', line=995)
W('34,3060', 0o71067, '', '', 'REND10A', kind='operand', line=996)
W('34,3061', 0o03005, '', '', 'RVARMIN', 'VHF RADAR MIN. VARIANCE', kind='operand', line=997)
W('34,3062', 0o72244, '', 'BPL', 'TLOAD', kind='interp', line=998)
W('34,3063', 0o71067, '', '', 'REND10A', kind='operand', line=999)
W('34,3064', 0o03005, '', '', 'RVARMIN', kind='operand', line=1000)
W('34,3065', 0o77646, '', 'ABS', '', 'MIN. VALUE WAS STORED AS NEG.', kind='interp', line=1001)
W('34,3066', 0o03526, '', 'STORE', 'VARIANCE', 'STORE MIN. VALUE', kind='interp', line=1002)
W('34,3067', 0o45014, 'REND10A', 'CLEAR', 'CALL', kind='interp', line=1003)
W('34,3070', 0o02666, '', '', 'DMENFLG', 'CLEAR FOR 6 X 6 W MATRIX', kind='operand', line=1004)
W('34,3071', 0o75254, '', '', 'INCORP1', 'CALCULATE UPDATE', kind='operand', line=1005)
W('34,3072', 0o77624, '', 'CALL', kind='interp', line=1006)
W('34,3073', 0o56750, '', '', 'GRP2PC', kind='operand', line=1007)
W('34,3074', 0o45014, '', 'BOFF', 'CALL', kind='interp', line=1008)
W('34,3075', 0o02744, '', '', 'INCORFLG', kind='operand', line=1009)
W('34,3076', 0o71124, '', '', 'REND12', kind='operand', line=1010)
W('34,3077', 0o56547, '', '', 'SHIFTNDX', 'GET EARTH MOON SCALING INDEX', kind='operand', line=1011)
W('34,3100', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=1012)
W('34,3101', 0o01265, '', '', 'DELTAX +6', kind='operand', line=1013)
W('34,3102', 0o77657, '', 'SR*', kind='interp', line=1014)
W('34,3103', 0o57176, '', '', '0,2', kind='operand', line=1015)
W('34,3104', 0o27504, '', 'STOVL', 'N49DISP +2', kind='interp', line=1016)
W('34,3105', 0o01257, '', '', 'DELTAX', kind='operand', line=1017)
W('34,3106', 0o53646, '', 'ABVAL', 'SR*', kind='interp', line=1018)
W('34,3107', 0o57176, '', '', '0,2', kind='operand', line=1019)
W('34,3110', 0o03502, '', 'STORE', 'N49DISP', kind='interp', line=1020)
W('34,3111', 0o77735, '', 'SLOAD', kind='interp', line=1021)
W('34,3112', 0o02003, '', '', 'RMAX', kind='operand', line=1022)
W('34,3113', 0o45261, '', 'SR', 'DSU', kind='interp', line=1023)
W('34,3114', 0o20613, '', '', '10D', kind='operand', line=1024)
W('34,3115', 0o03502, '', '', 'N49DISP', kind='operand', line=1025)
W('34,3116', 0o67240, '', 'BMN', 'SLOAD', kind='interp', line=1026)
W('34,3117', 0o71257, '', '', 'RENDISP', 'BRANCH IF POS UP. GREATER THAN MAX.', kind='operand', line=1027)
W('34,3120', 0o02004, '', '', 'VMAX', kind='operand', line=1028)
W('34,3121', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1029)
# Page 583
W('34,3122', 0o03504, '', '', 'N49DISP +2', kind='operand', line=1031)
W('34,3123', 0o71257, '', '', 'RENDISP', 'BRANCH IF VEL. UPDATE GREATER THAN MAX.', kind='operand', line=1032)
W('34,3124', 0o77624, 'REND12', 'CALL', kind='interp', line=1033)
W('34,3125', 0o75466, '', '', 'INCORP2', 'INCORPORATE UPDATE VALUES INTO STATE VEC', kind='operand', line=1034)
W('34,3126', 0o43014, '', 'BON', 'BOFF', kind='interp', line=1035)
W('34,3127', 0o04707, '', '', 'SOURCFLG', kind='operand', line=1036)
W('34,3130', 0o71221, '', '', 'REND16', 'BRANCH IF DATA IS RADAR', kind='operand', line=1037)
W('34,3131', 0o02744, '', '', 'INCORFLG', kind='operand', line=1038)
W('34,3132', 0o71227, '', '', 'REND17', kind='operand', line=1039)
W('34,3133', 0o77624, '', 'CALL', kind='interp', line=1040)
W('34,3134', 0o56547, '', '', 'SHIFTNDX', 'GET EARTH MOON SCALING INDEX', kind='operand', line=1041)
W('34,3135', 0o45014, '', 'BON', 'CALL', kind='interp', line=1042)
W('34,3136', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=1043)
W('34,3137', 0o71235, '', '', 'REND18', 'BRANCH IF CSM UPDATE', kind='operand', line=1044)
W('34,3140', 0o71250, '', '', 'LMPOS', 'GET LM POSITION', kind='operand', line=1045)
W('34,3141', 0o77624, 'REND13', 'CALL', kind='interp', line=1046)
W('34,3142', 0o56750, '', '', 'GRP2PC', 'PHASE CHANGE', kind='operand', line=1047)
W('34,3143', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=1048)
W('34,3144', 0o01215, '', '', 'LEMPOS', kind='operand', line=1049)
W('34,3145', 0o01207, '', '', 'CSMPOS', kind='operand', line=1050)
W('34,3146', 0o03531, '', 'STORE', 'RCLP', 'LM - CSM', kind='interp', line=1051)
W('34,3147', 0o77614, '', 'CLRGO', kind='interp', line=1052)
W('34,3150', 0o02624, '', '', 'INCORFLG', kind='operand', line=1053)
W('34,3151', 0o70767, '', '', 'REND7', 'BRANCH FOR 2ND PASS THIS OPTICS MARK', kind='operand', line=1054)
W('34,3152', 0o45014, 'CSMUPP', 'CLEAR', 'CALL', kind='interp', line=1055)
W('34,3153', 0o01674, '', '', 'VINTFLAG', 'SET INTEGRATION VEHICLE EQ LM', kind='operand', line=1056)
W('34,3154', 0o27162, '', '', 'INTEGRV', kind='operand', line=1057)
W('34,3155', 0o77624, '', 'CALL', kind='interp', line=1058)
W('34,3156', 0o56750, '', '', 'GRP2PC', 'PHASE CHANGE', kind='operand', line=1059)
W('34,3157', 0o77624, '', 'CALL', kind='interp', line=1060)
W('34,3160', 0o56343, '', '', 'SETINTG', 'SET FLAGS FOR INTEGRATION', kind='operand', line=1061)
W('34,3161', 0o77650, '', 'GOTO', kind='interp', line=1062)
W('34,3162', 0o70731, '', '', 'REND5', kind='operand', line=1063)
W('34,3163', 0o27502, 'REND14', 'STOVL', 'BVECTOR', 'VHF RADAR BVECTOR', kind='interp', line=1064)
W('34,3164', 0o15335, '', '', 'ZEROVECS', kind='operand', line=1065)
W('34,3165', 0o03510, '', 'STORE', 'BVECTOR +6', kind='interp', line=1066)
W('34,3166', 0o27516, '', 'STOVL', 'BVECTOR +12D', kind='interp', line=1067)
W('34,3167', 0o03531, '', '', 'RCLP', kind='operand', line=1068)
W('34,3170', 0o71256, '', 'UNIT', 'DLOAD', kind='interp', line=1069)
W('34,3171', 0o01257, '', '', 'VHFRANGE', 'VHFRANGE SCALED B-27', kind='operand', line=1070)
W('34,3172', 0o60414, '', 'BON', 'SR2', kind='interp', line=1071)
W('34,3173', 0o04303, '', '', 'MOONTHIS', kind='operand', line=1072)
W('34,3174', 0o71175, '', '', '+1', kind='operand', line=1073)
W('34,3175', 0o43025, '', 'DSU', 'SET', kind='interp', line=1074)
W('34,3176', 0o00045, '', '', '36D', 'ABVAL (RCLP)', kind='operand', line=1075)
W('34,3177', 0o02464, '', '', 'INCORFLG', kind='operand', line=1076)
W('34,3200', 0o03524, '', 'STORE', 'DELTAQ', kind='interp', line=1077)
W('34,3201', 0o77214, '', 'BOFF', 'VLOAD', kind='interp', line=1078)
W('34,3202', 0o00747, '', '', 'VEHUPFLG', kind='operand', line=1079)
W('34,3203', 0o71207, '', '', 'REND14A', kind='operand', line=1080)
# Page 584
W('34,3204', 0o03502, '', '', 'BVECTOR', kind='operand', line=1082)
W('34,3205', 0o77676, '', 'VCOMP', kind='interp', line=1083)
W('34,3206', 0o03502, '', 'STORE', 'BVECTOR', kind='interp', line=1084)
W('34,3207', 0o77624, 'REND14A', 'CALL', kind='interp', line=1085)
W('34,3210', 0o56750, '', '', 'GRP2PC', kind='operand', line=1086)
W('34,3211', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=1087)
W('34,3212', 0o03003, '', '', 'RVAR', kind='operand', line=1088)
W('34,3213', 0o71027, '', '', 'REND10', kind='operand', line=1089)
W('34,3214', 0o43335, 'REND15', 'SLOAD', 'DAD', 'GET ALT LOS VARIANCE', kind='interp', line=1090)
W('34,3215', 0o01357, '', '', 'ALTVAR', 'BACKUP OPTICS', kind='operand', line=1091)
W('34,3216', 0o31340, '', '', 'IMUVAR', 'IMU VARIANCE', kind='operand', line=1092)
W('34,3217', 0o77650, '', 'GOTO', kind='interp', line=1093)
W('34,3220', 0o71027, '', '', 'REND10', kind='operand', line=1094)
W('34,3221', 0o62150, 'REND16', 'LXA,1', 'INCR,1', kind='interp', line=1095)
W('34,3222', 0o01125, '', '', 'VHFCNT', 'VHF RADAR UPDATE COUNT', kind='operand', line=1096)
W('34,3223', 0o00001, '', 'DEC', '1', kind='data', line=1097)
W('34,3224', 0o52130, '', 'SXA,1', 'GOTO', kind='interp', line=1098)
W('34,3225', 0o01125, '', '', 'VHFCNT', 'UPDATE COUNT', kind='operand', line=1099)
W('34,3226', 0o70641, '', '', 'REND1', kind='operand', line=1100)
W('34,3227', 0o62150, 'REND17', 'LXA,1', 'INCR,1', kind='interp', line=1101)
W('34,3230', 0o01126, '', '', 'TRKMKCNT', 'OPTICS MARK COUNT', kind='operand', line=1102)
W('34,3231', 0o00001, '', 'DEC', '1', kind='data', line=1103)
W('34,3232', 0o52130, '', 'SXA,1', 'GOTO', kind='interp', line=1104)
W('34,3233', 0o01126, '', '', 'TRKMKCNT', 'UPDATE COUNT', kind='operand', line=1105)
W('34,3234', 0o70673, '', '', 'REND3', kind='operand', line=1106)
W('34,3235', 0o77624, 'REND18', 'CALL', kind='interp', line=1107)
W('34,3236', 0o71241, '', '', 'CMPOS', 'GET CSM POSITION', kind='operand', line=1108)
W('34,3237', 0o77650, '', 'GOTO', kind='interp', line=1109)
W('34,3240', 0o71141, '', '', 'REND13', kind='operand', line=1110)
W('34,3241', 0o53775, 'CMPOS', 'VLOAD', 'VSR*', kind='interp', line=1111)
W('34,3242', 0o01573, '', '', 'DELTACSM', kind='operand', line=1112)
W('34,3243', 0o57167, '', '', '7,2', kind='operand', line=1113)
W('34,3244', 0o77655, '', 'VAD', kind='interp', line=1114)
W('34,3245', 0o01607, '', '', 'RCVCSM', kind='operand', line=1115)
W('34,3246', 0o01207, '', 'STORE', 'CSMPOS', 'CSM POSITION SCALED B-27 OR B-29', kind='interp', line=1116)
W('34,3247', 0o77616, '', 'RVQ', kind='interp', line=1117)
W('34,3250', 0o53775, 'LMPOS', 'VLOAD', 'VSR*', kind='interp', line=1118)
W('34,3251', 0o01645, '', '', 'DELTALEM', kind='operand', line=1119)
W('34,3252', 0o57167, '', '', '7,2', kind='operand', line=1120)
W('34,3253', 0o77655, '', 'VAD', kind='interp', line=1121)
W('34,3254', 0o01661, '', '', 'RCVLEM', kind='operand', line=1122)
W('34,3255', 0o01215, '', 'STORE', 'LEMPOS', 'LM POSITION SCALED B-27 OR B-29', kind='interp', line=1123)
W('34,3256', 0o77616, '', 'RVQ', kind='interp', line=1124)
W('34,3257', 0o77776, 'RENDISP', 'EXIT', kind='interp', line=1125)
W('34,3260', 0o30105, '', 'CA', 'FLAGWRD9', line=1126)
W('34,3261', 0o75010, '', 'MASK', 'SOURCBIT', line=1127)
W('34,3262', 0o00006, '', 'EXTEND', line=1128)
W('34,3263', 0o13266, '', 'BZF', '+3', line=1129)
W('34,3264', 0o35016, '', 'CA', 'BIT2', line=1130)
W('34,3265', 0o03267, '', 'TC', '+2', line=1131)
# Page 585
W('34,3266', 0o35017, '', 'CA', 'BIT1', line=1133)
W('34,3267', 0o55505, '', 'TS', 'N49DISP +4', line=1134)
W('34,3270', 0o35021, '', 'CAF', 'ZERO', 'SET TEMPOR1 > ZERO TO INDICATE', line=1135)
W('34,3271', 0o55300, '', 'TS', 'TEMPOR1', "V06 N49 DISPLAY HASN'T BEEN ANSWERED", line=1136)
W('34,3272', 0o05412, '', 'TC', 'PHASCHNG', line=1137)
W('34,3273', 0o04022, '', 'OCT', '04022', kind='data', line=1138)
W('34,3274', 0o37664, '', 'CAF', 'PRIO27', 'SET UP DISPLAY JOB WITH HIGHER PRIORITY', line=1139)
W('34,3275', 0o05134, '', 'TC', 'NOVAC', line=1140)
#   EBANK= MRKBUF1  # THAN PRESENT JOB
W('34,3276', 0o03310, '', '2CADR', 'RENDISP2', kind='data', line=1142)
W('34,3277', 0o70067, kind='data', line=1142)

W('34,3300', 0o06006, 'RENDISP7', 'TC', 'INTPRET', line=1144)
W('34,3301', 0o00155, '', 'STORE', 'MPAC', kind='interp', line=1145)
W('34,3302', 0o53135, '', 'SLOAD', 'BZE', kind='interp', line=1146)
W('34,3303', 0o01301, '', '', 'TEMPOR1', kind='operand', line=1147)
W('34,3304', 0o71301, '', '', 'RENDISP7 +1', 'DISPLAY HAS NOT BEEN ANSWERED YET', kind='operand', line=1148)
W('34,3305', 0o52040, '', 'BMN', 'GOTO', kind='interp', line=1149)
W('34,3306', 0o71124, '', '', 'REND12', 'NEG INDICATES PROCEED', kind='operand', line=1150)
W('34,3307', 0o71317, '', '', 'RENDISP3', 'POS INDICATES RECYCLE', kind='operand', line=1151)
W('34,3310', 0o33341, 'RENDISP2', 'CAF', 'V06N49', line=1152)
W('34,3311', 0o04662, '', 'TC', 'BANKCALL', line=1153)
W('34,3312', 0o20731, '', 'CADR', 'PRIODSP', kind='data', line=1154)
W('34,3313', 0o04622, '', 'TC', 'GOTOV56', 'TERM EXIT P20 VIA V56', line=1155)
W('34,3314', 0o45017, '', 'CS', 'ONE', 'NEG INDICATES PROCEED RENDISP7 JOB', line=1156)
W('34,3315', 0o55300, '', 'TS', 'TEMPOR1', 'POS INDICATES RECYCLE RENDISP7 JOB', line=1157)
W('34,3316', 0o05217, '', 'TC', 'ENDOFJOB', 'GO COMPLETE ABOVE JOB', line=1158)
W('34,3317', 0o77614, 'RENDISP3', 'BON', kind='interp', line=1159)
W('34,3320', 0o04707, '', '', 'SOURCFLG', kind='operand', line=1160)
W('34,3321', 0o70641, '', '', 'REND1', 'DATA WAS RADAR GO LOOK FOR OPTICS NEXT', kind='operand', line=1161)
W('34,3322', 0o77776, '', 'EXIT', kind='interp', line=1162)
#   EBANK= MRKBUF1
W('34,3323', 0o00004, '', 'INHINT', line=1164)
W('34,3324', 0o33342, '', 'CAF', 'BUFBANK', line=1165)
W('34,3325', 0o54006, '', 'TS', 'BBANK', line=1166)
W('34,3326', 0o37716, '', 'CA', 'NEGONE', line=1167)
W('34,3327', 0o55725, '', 'TS', 'MRKBUF1', 'ERASE MARK ONE BUFFER', line=1168)
W('34,3330', 0o55734, '', 'TS', 'MRKBUF2', 'ERASE MARK TWO BUFFER', line=1169)
W('34,3331', 0o00003, '', 'RELINT', line=1170)
W('34,3332', 0o06006, 'RENDISP4', 'TC', 'INTPRET', line=1171)
W('34,3333', 0o77650, '', 'GOTO', kind='interp', line=1172)
W('34,3334', 0o70673, '', '', 'REND3', kind='operand', line=1173)
W('34,3335', 0o00052, 'SXTVAR', '2DEC', '0.04 E-6 B+16', 'SXT ERROR VARIANCE = .04 (MR)SQ', kind='data', line=1174)
W('34,3336', 0o36307, kind='data', line=1174)

W('34,3337', 0o00052, 'IMUVAR', '2DEC', '0.04 E-6 B+16', 'IMU ERROR VARIANCE = .04 (MR)SQ', kind='data', line=1176)
W('34,3340', 0o36307, kind='data', line=1176)

W('34,3341', 0o01461, 'V06N49', 'VN', '0649', kind='data', line=1178)
#   EBANK= MRKBUF1
W('34,3342', 0o70067, 'BUFBANK', 'BBCON', 'RENDISP3', kind='data', line=1180)
#   BANK 31
#   SETLOC R22S1
# Page 586
#   BANK
W('27,2343', 0o45020, 'SETINTG', 'STQ', 'CALL', kind='interp', line=1185)
W('27,2344', 0o02317, '', '', 'EGRESS', kind='operand', line=1186)
W('27,2345', 0o27442, '', '', 'INTSTALL', 'RESERVE INTEGRATION', kind='operand', line=1187)
W('27,2346', 0o43145, '', 'DLOAD', 'SET', kind='interp', line=1188)
W('27,2347', 0o01225, '', '', 'MARKTIME', kind='operand', line=1189)
W('27,2350', 0o01472, '', '', 'STATEFLG', kind='operand', line=1190)
W('27,2351', 0o00041, '', 'STORE', 'TDEC1', 'MARKTIME', kind='interp', line=1191)
W('27,2352', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=1192)
W('27,2353', 0o01673, '', '', 'INTYPFLG', 'PRECISION INTEGRATION', kind='operand', line=1193)
W('27,2354', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=1194)
W('27,2355', 0o43014, '', 'SET', 'CLRGO', kind='interp', line=1195)
W('27,2356', 0o01474, '', '', 'VINTFLAG', 'SET VEHICLE EQ. CSM', kind='operand', line=1196)
W('27,2357', 0o01635, '', '', 'D6OR9FLG', 'SET W MATRIX DIM. EQ 6', kind='operand', line=1197)
W('27,2360', 0o02317, '', '', 'EGRESS', 'EXIT', kind='operand', line=1198)
W('27,2361', 0o77620, 'CNTCHK', 'STQ', kind='interp', line=1199)
W('27,2362', 0o01150, '', '', 'POINTEX', kind='operand', line=1200)
W('27,2363', 0o77614, 'CONTCHK', 'BOFF', kind='interp', line=1201)
W('27,2364', 0o01742, '', '', 'REFSMFLG', 'BRANCH TO END OF JOB IF REFSMMAT NO GOOD', kind='operand', line=1202)
W('27,2365', 0o30156, '', '', 'ENDPLAC', kind='operand', line=1203)
W('27,2366', 0o50135, '', 'SLOAD', 'BMN', kind='interp', line=1204)
W('27,2367', 0o03376, '', '', 'R61CNTR', kind='operand', line=1205)
W('27,2370', 0o56406, '', '', 'WAITONE1', kind='operand', line=1206)
W('27,2371', 0o43014, '', 'BON', 'BOFF', 'IS TRACK FLAG SET', kind='interp', line=1207)
W('27,2372', 0o00710, '', '', 'UPDATFLG', kind='operand', line=1208)
W('27,2373', 0o01150, '', '', 'POINTEX', kind='operand', line=1209)
W('27,2374', 0o00752, '', '', 'TRACKFLG', kind='operand', line=1210)
W('27,2375', 0o30156, '', '', 'ENDPLAC', kind='operand', line=1211)
W('27,2376', 0o77776, '', 'EXIT', kind='interp', line=1212)
W('27,2377', 0o05412, 'REDOR22', 'TC', 'PHASCHNG', line=1213)
W('27,2400', 0o00132, '', 'OCT', '00132', kind='data', line=1214)
W('27,2401', 0o37663, '', 'CAF', 'PRIO26', line=1215)
W('27,2402', 0o05210, '', 'TC', 'PRIOCHNG', line=1216)
W('27,2403', 0o02407, '', 'TC', 'WAITONE +3', line=1217)
W('27,2404', 0o77620, 'WAITONE', 'STQ', kind='interp', line=1218)
W('27,2405', 0o01150, '', '', 'POINTEX', kind='operand', line=1219)
W('27,2406', 0o77776, 'WAITONE1', 'EXIT', kind='interp', line=1220)
W('27,2407', 0o35045, '', 'CAF', '4SECS', 'WAIT 4 SECS.', line=1221)
W('27,2410', 0o04662, '', 'TC', 'BANKCALL', line=1222)
W('27,2411', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=1223)
W('27,2412', 0o06006, '', 'TC', 'INTPRET', line=1224)
W('27,2413', 0o77650, '', 'GOTO', kind='interp', line=1225)
W('27,2414', 0o56363, '', '', 'CONTCHK', 'CHECK AGAIN NOW', kind='operand', line=1226)
W('27,2415', 0o77776, 'RANGERD', 'EXIT', kind='interp', line=1227)
W('27,2416', 0o00004, '', 'INHINT', line=1228)
W('27,2417', 0o42500, '', 'CS', 'OCT17', line=1229)
W('27,2420', 0o00006, '', 'EXTEND', line=1230)
W('27,2421', 0o03013, '', 'WAND', 'CHAN13', 'ZERO OUT BITS 1-4 OF CHANNEL 13', line=1231)
W('27,2422', 0o34334, '', 'CAF', 'OCT11', line=1232)
W('27,2423', 0o00006, '', 'EXTEND', line=1233)
# Page 587
W('27,2424', 0o05013, '', 'WOR', 'CHAN13', 'GENERAGE SHIFT PULSES TO RADR, SET R. BIT', line=1235)
W('27,2425', 0o00003, '', 'RELINT', line=1236)
W('27,2426', 0o00006, '', 'EXTEND', line=1237)
W('27,2427', 0o30025, '', 'DCA', 'TIME2', line=1238)
W('27,2430', 0o53225, '', 'DXCH', 'MARKTIME', 'READ PRESENT TIME', line=1239)
W('27,2431', 0o05560, '', 'TC', 'DOWNFLAG', line=1240)
W('27,2432', 0o00043, '', 'ADRES', 'SKIPVHF', kind='data', line=1241)
W('27,2433', 0o04662, '', 'TC', 'BANKCALL', line=1242)
W('27,2434', 0o17575, '', 'CADR', 'RADSTALL', 'WAIT FOR RANGE COMPLETE', kind='data', line=1243)
W('27,2435', 0o02464, '', 'TC', 'LIGHTON', 'BAD DATA GOOD BIT', line=1244)
W('27,2436', 0o05631, '', 'TC', 'TRFAILOF', 'TURN TRACKER LIGHT OFF', line=1245)
W('27,2437', 0o11703, 'RANGERD1', 'CCS', 'RM', '15 BIT UNSIGNED RANGE', line=1246)
W('27,2440', 0o02444, '', 'TC', 'RANGERD4', 'GR + 0', line=1247)
W('27,2441', 0o02470, '', 'TC', 'LIGHTON +4', '= + 0', line=1248)
W('27,2442', 0o02453, '', 'TC', 'RANGERD3', 'L - 0', line=1249)
W('27,2443', 0o02453, '', 'TC', 'RANGERD3', '= - 0', line=1250)
W('27,2444', 0o06006, 'RANGERD4', 'TC', 'INTPRET', line=1251)
W('27,2445', 0o41335, '', 'SLOAD', 'DMP', kind='interp', line=1252)
W('27,2446', 0o03704, '', '', 'RM', kind='operand', line=1253)
W('27,2447', 0o16503, '', '', 'CONVRNGE', 'CONVERT RANGE TO METERS B-27', kind='operand', line=1254)
W('27,2450', 0o01257, 'RANGERD2', 'STORE', 'VHFRANGE', kind='interp', line=1255)
W('27,2451', 0o43414, '', 'SET', 'RVQ', kind='interp', line=1256)
W('27,2452', 0o04467, '', '', 'SOURCFLG', 'SOURCE OF DATA TO VHF RADAR', kind='operand', line=1257)
W('27,2453', 0o31703, 'RANGERD3', 'CA', 'RM', line=1258)
W('27,2454', 0o74777, '', 'MASK', 'POSMAX', line=1259)
W('27,2455', 0o54154, '', 'TS', 'MPAC', 'MASK OUT NEG. SIGN BIT', line=1260)
W('27,2456', 0o06006, '', 'TC', 'INTPRET', line=1261)
W('27,2457', 0o77605, '', 'DMP', kind='interp', line=1262)
W('27,2460', 0o16503, '', '', 'CONVRNGE', 'CONVERT FROM NM TO METERS AND SCALE B-27', kind='operand', line=1263)
W('27,2461', 0o52015, '', 'DAD', 'GOTO', kind='interp', line=1264)
W('27,2462', 0o16477, '', '', 'RANGEB14', 'VALUE IN METERS OF SIGN BIT SCALED B-27', kind='operand', line=1265)
W('27,2463', 0o56450, '', '', 'RANGERD2', kind='operand', line=1266)
W('27,2464', 0o31256, 'LIGHTON', 'CA', 'VHFRANGE', line=1267)
W('27,2465', 0o00006, '', 'EXTEND', line=1268)
W('27,2466', 0o12470, '', 'BZF', '+2', line=1269)
W('27,2467', 0o05643, '', 'TC', 'TRFAILON', line=1270)
W('27,2470', 0o06006, '', 'TC', 'INTPRET', line=1271)
W('27,2471', 0o77745, '', 'DLOAD', kind='interp', line=1272)
W('27,2472', 0o01225, '', '', 'MARKTIME', kind='operand', line=1273)
W('27,2473', 0o01152, '', 'STORE', 'VHFTIME', kind='interp', line=1274)
W('27,2474', 0o77650, '', 'GOTO', kind='interp', line=1275)
W('27,2475', 0o70641, '', '', 'REND1', kind='operand', line=1276)
W('27,2476', 0o00045, 'RANGEB14', '2DEC', '303431.7 B-27', '16384 X 18.52 SCALED B-27', kind='data', line=1277)
W('27,2477', 0o01217, kind='data', line=1277)

W('27,2500', 0o00017, 'OCT17', 'OCT', '00017', kind='data', line=1279)
W('27,2501', 0o40200, 'OC40200', 'OCT', '40200', kind='data', line=1280)
W('27,2502', 0o00045, 'CONVRNGE', '2DEC', '18.52 B-13', 'VHF INPUT RANGE CONV. FROM .01 NM TO M', kind='data', line=1281)
W('27,2503', 0o01217, kind='data', line=1281)

W('27,2504', 0o00006, 'VHFREAD', 'EXTEND', line=1283)
W('27,2505', 0o04007, '', 'ROR', 'SUPERBNK', 'MUST SAVE SBANK BECAUSE OF RUPT', line=1284)
# Page 588
W('27,2506', 0o54016, '', 'TS', 'BANKRUPT', 'EXITS VIA TASKOVER BADEND OR GOODEND', line=1286)
W('27,2507', 0o45021, '', 'CS', 'ZERO', line=1287)
W('27,2510', 0o54734, '', 'TS', 'RUPTAGN', line=1288)
W('27,2511', 0o00006, '', 'EXTEND', line=1289)
W('27,2512', 0o22012, '', 'QXCH', 'QRUPT', line=1290)
W('27,2513', 0o40076, '', 'CS', 'STATE +2', line=1291)
W('27,2514', 0o75006, '', 'MASK', 'SKIPVBIT', 'SKIPVHF FLAG', line=1292)
W('27,2515', 0o00006, '', 'EXTEND', line=1293)
W('27,2516', 0o15324, '', 'BZF', 'TASKOVER', 'BRANCH IF VHF RESTART BIT SET', line=1294)
W('27,2517', 0o35011, '', 'CAF', 'UPDATBIT', line=1295)
W('27,2520', 0o70075, '', 'MASK', 'STATE +1', 'UPDATEFLG', line=1296)
W('27,2521', 0o00006, '', 'EXTEND', line=1297)
W('27,2522', 0o12542, '', 'BZF', 'BYPASS1', line=1298)
W('27,2523', 0o40100, '', 'CS', 'STATE +4', line=1299)
W('27,2524', 0o75004, '', 'MASK', 'PDSPFBIT', 'PDSPFLAG', line=1300)
W('27,2525', 0o00006, '', 'EXTEND', line=1301)
W('27,2526', 0o12542, '', 'BZF', 'BYPASS1', line=1302)
W('27,2527', 0o30046, '', 'CA', 'RNRAD', line=1303)
W('27,2530', 0o55703, '', 'TS', 'RM', 'SAVE RANGE', line=1304)
W('27,2531', 0o35016, '', 'CAF', 'BIT2', line=1305)
W('27,2532', 0o00006, '', 'EXTEND', line=1306)
W('27,2533', 0o02033, '', 'RAND', 'CHAN33', 'READ DATA GOOD BIT', line=1307)
W('27,2534', 0o00006, '', 'EXTEND', line=1308)
W('27,2535', 0o12544, '', 'BZF', 'VHFGOOD', 'BRANCH IF DATA GOOD BIT EQUALS GOOD', line=1309)
W('27,2536', 0o55256, 'BYPASS', 'TS', 'VHFRANGE', 'STORE NON ZERO VALUE', line=1310)
W('27,2537', 0o35016, '', 'CAF', 'TWO', line=1311)
W('27,2540', 0o04701, '', 'TC', 'POSTJUMP', line=1312)
W('27,2541', 0o17545, '', 'CADR', 'BADEND', kind='data', line=1313)
W('27,2542', 0o35021, 'BYPASS1', 'CAF', 'ZERO', line=1314)
W('27,2543', 0o02536, '', 'TC', 'BYPASS', line=1315)
W('27,2544', 0o35016, 'VHFGOOD', 'CAF', 'TWO', line=1316)
W('27,2545', 0o04701, '', 'TC', 'POSTJUMP', line=1317)
W('27,2546', 0o17550, '', 'CADR', 'GOODEND', kind='data', line=1318)
W('27,2547', 0o43174, 'SHIFTNDX', 'AXT,2', 'BON', kind='interp', line=1319)
W('27,2550', 0o00000, '', '', '0', kind='operand', line=1320)
W('27,2551', 0o00707, '', '', 'VEHUPFLG', kind='operand', line=1321)
W('27,2552', 0o56560, '', '', 'SHIFTA', 'VEHICLE IS CSM', kind='operand', line=1322)
W('27,2553', 0o43414, '', 'BON', 'RVQ', kind='interp', line=1323)
W('27,2554', 0o04304, '', '', 'LMOONFLG', kind='operand', line=1324)
W('27,2555', 0o56556, '', '', '+1', kind='operand', line=1325)
W('27,2556', 0o43514, '', 'INCR,2', 'RVQ', kind='interp', line=1326)
W('27,2557', 0o77775, '', 'DEC', '-2', kind='data', line=1327)
W('27,2560', 0o43414, 'SHIFTA', 'BON', 'RVQ', kind='interp', line=1328)
W('27,2561', 0o04303, '', '', 'CMOONFLG', kind='operand', line=1329)
W('27,2562', 0o56563, '', '', '+1', 'MOON ORB.', kind='operand', line=1330)
W('27,2563', 0o43514, '', 'INCR,2', 'RVQ', kind='interp', line=1331)
W('27,2564', 0o77775, '', 'DEC', '-2', kind='data', line=1332)
W('27,2565', 0o66370, 'INITIALW', 'AXT,1', 'SSP', kind='interp', line=1333)
W('27,2566', 0o00044, '', '', '36D', kind='operand', line=1334)
W('27,2567', 0o00051, '', '', 'S1', kind='operand', line=1335)
# Page 589
W('27,2570', 0o00006, '', '', '6', kind='operand', line=1337)
W('27,2571', 0o77775, '', 'VLOAD', kind='interp', line=1338)
W('27,2572', 0o15335, '', '', 'ZEROVECS', kind='operand', line=1339)
W('27,2573', 0o06445, 'INITA', 'STORE', 'W +36D,1', 'CLEAR 0 - 35', kind='interp', line=1340)
W('27,2574', 0o76100, '', 'TIX,1', 'AXT,1', kind='interp', line=1341)
W('27,2575', 0o56573, '', '', 'INITA', kind='operand', line=1342)
W('27,2576', 0o00044, '', '', '36D', kind='operand', line=1343)
W('27,2577', 0o06533, 'INITB', 'STORE', 'W +90D,1', 'CLEAR 54 - 89', kind='interp', line=1344)
W('27,2600', 0o67300, '', 'TIX,1', 'SLOAD', kind='interp', line=1345)
W('27,2601', 0o56577, '', '', 'INITB', kind='operand', line=1346)
W('27,2602', 0o00001, '', '', '0', 'POSITION VALUE', kind='operand', line=1347)
W('27,2603', 0o02401, '', 'STORE', 'W', 'INITIALIZE DIAGONAL W POSITION', kind='interp', line=1348)
W('27,2604', 0o02411, '', 'STORE', 'W +8D', kind='interp', line=1349)
W('27,2605', 0o02421, '', 'STORE', 'W +16D', kind='interp', line=1350)
W('27,2606', 0o77735, '', 'SLOAD', kind='interp', line=1351)
W('27,2607', 0o00002, '', '', '1', 'VELOCITY VALUE', kind='operand', line=1352)
W('27,2610', 0o02511, '', 'STORE', 'W +72D', 'INITIALIZE DIAGONAL W VELOCITY', kind='interp', line=1353)
W('27,2611', 0o02521, '', 'STORE', 'W +80D', kind='interp', line=1354)
W('27,2612', 0o02531, '', 'STORE', 'W +88D', kind='interp', line=1355)
W('27,2613', 0o77616, '', 'RVQ', kind='interp', line=1356)
# Page 590
# CRS61.1       R/10/68
#
# TO COMPUTE THE PREFERRED TRACKING ATTITUDE OF THE CSM WHICH ENABLES
# OPTICS TRACKING OF THE LEM AND LM TRACKING OF THE CSM RADAR TRANSPONDER
# AND TO COMPUTE THE X-AXIS TRACKING ATTITUDE OF THE CSM WHICH ENABLES
# COAS TRACKING OF THE LM.
#
# TO PERFORM THE MANEUVER TO THE SELECTED TRACKING ATTITUDE IF THE
# MANEUVER IS LESS THAN 10 DEGREES BUT TO CALL R60 IF THE MANEUVER IS
# GREATER THAN 10 DEGREES BUT TO CALL R60 IF THE MANEUVER IS
# GREATER THAN 10 DEGREES OR IF THE R60 FLAG IS SET.
#
# (1)     EXTRAPOLATE LM AND CSM STATE VECTORS TO PRESENT TIME USING
# CONIC EQUATIONS.
#
# (2)     CALCULATE LOS FROM CSM TO LM = RL - RC.
#
# (3)     THE PRERFERRED TRACKING ATTITUDE IS DEFINED AS FOLLOWS:
# THE TRACK AXIS (I) IS ALIGNED ALONG THE LOS TO THE LM.  THE
# TRACK AXIS (I) IS DEFINED AS:
#
# UNIT(I)=UNIT(Z  )COS55  &  UNIT(X  )SIN55
# -       -SC                -SC
#
# (4)     COMPUTE DESIRED CDU ANGLES, USING VECPOINT.
#
# (Sorry, I don't know where (5) and (6) are. --- RSB 2009.)
# (7)     FORM DIFFERENCE BETWEEN DESIRED AND ACTUAL CDUS.
# IF ANY OF THE THREE ANGLE DIFFERENCES EXCEEDS 10 DEGREES,
# GROSS MANEUVER IS REQUIRED.  SIGNAL R61 (SET MPAC=1) TO
# OPERATE KALCMANU AND EXIT CRS61.1.
# IF ALL DIFFERENCES ARE LESS THAN 10 DEGREES, CONTINUE.
#
# (8)     CALCULATE ORTHOGONAL LOS RATE IN REF COORDS AS
#
# OMEGATH = (UNITLOS(B1) X UNITDV(B1))(ABSDV(B7)/ABSLOS(B29))
#
# CONVERSION FACTOR OF 100/2PI (B4) REV CSEC PER RAD SEC IS
# APPLIED TO YIELD UNITS OF REVS/SEC.  SCALE IS CARRIED AS
# B+1+1+7-29+4+1 PLUS RESULTS OF NORMALIZING ABSDV, ABSLOS.
# THE EXTRA B+1 RESULTS FROM RESCALING ABSDV B8 AFTER NORM
# TO AVOID OVFLOW ON DIVIDE.
#
# UNITLOS = UNIT( RL - RC ) B1.
# UNITDY  = UNIT( VL - VC ) B1.
# ABSLOS  = LENGTH OF LOS, METERS B29.
# ABSDV   = LENGTH OF DV, METERS/CSEC B7.
#
# (9)     OBTAIN RATE IN SM COORDS.
#
# OMETATHSM = (REFSMMAT)(OMEGATH).
#
# (10)    OBTAIN GIMBAL ANGLE INCREMENTS FOR 0.1 SECOND.
#
# DTHETASM = (0.1)(OMEGATHSM)
#
# (11)    OBTAIN DELCDUX,Y,Z USING SUBR SMCDURES.
# Page 591
# INPUT CONSISTS OF
#
# (A)     VECTOR OF ANGULAR INCREMENTS, DTHETASM, STORED
# IN V(DTHETASM).
# (B)     SIN,COS CDUX,Y,Z FROM SUBR CDUTRIG.
#
# TRANSFER OUTPUT OF SMCDURES FROM V(DCDU) TO VAC14D.
#
# (12)    CALCULATE ANG LOS RATE IN BODY(NB) COORDS USING SUBR SMNB.
#
# OMEGANB = (SMNB)(OMETATHSM)
#
# SUBR SMNB REQUIRES OMEGATHSM IN V(VAC32D) AND ACTUAL CDUS
# (Y,X,Z ORDER) IN V(VAC20D) WITH S1 OF VAC = BASE ADDRESS
# OF CDUS (FIXLOC + 20D).
#
# (13)    CALCULATE ANG LOS RATE IN CONTROL COORDS AS FOLLOWS
#
# WBODY = (MBDYTCTL)(OMEGANB)     UNITS=REVS/SEC(B0) (?).
#
# ( 0.5       0              0      )   BODY TO
# MBDYTCTL(B1) = (  0   COS(7.25)B1   -SIN(7.25)B1 ) = CONTROL
# (  0   SIN(7.25)B1    COS(7.25)B1 )   AXES
# CONVERSION
# MATRIX
#
# (14)    RESCALE WBODY TO UNITS OF 460 DEG/SEC BY APPLYING FACTOR
# OF 0.8 TO REVS/SEC.
#
# (15)    ADDRESS LIVE AUTOPILOT REGISTERS IN BASIC (UNDER INHINT).
#
# TRANSFER DESIRED CDUS, SCALED 180 DEGREES, FROM T(SAVEDCDU)
# TO V(CDUXD).
#
# TRANSFER DELCDUS, SCALED 180 DEG, FROM V(VAC14D)
# TO V(DELCDUX).
#
# TRANSFER OMEGA CONTROL, SCALED 450 DEG/SEC, FROM V(MPAC)
# TO V(WBODY).
#
# RELINT, SET MPAC=0, EXIT CRS61.1.
#
# CALL:         L       CALL    CRS61.1
#
# RETURNS:      ALL TO L+1.
#
# (1)     S(MPAC)=0.  NORMAL EXIT.  3 SETS OF INPUTS FED TO DAP.
# (2)     S(MPAC)=1.  CALCULATED DESIRED CDUS,SP, SET IN T(CPHI)
# FOR KALCMANU.  ABS(ACDU - DCDU) EXCEEDS 10 DEGREES.
# (3)     S(MPAC)=2.  GNCS AUTO MODE NOT SELECTED (BIT10=1).
# (4)     S(MPAC)=3.  DAP HOLD FLAG (HOLDFLAG) NOT EQUAL -1.
# Page 592
#
# INPUT:        (1)     TIME2,TIME1.  COMPUTER CLOCK TIME,DP, CENTISEC B28.
# (2)     CDUX,Y,Z.  PRESENT CDU ANGLES,SP,2S COMPL HALF-REVS B0.
# (3)     M(REFSMMAT), STABLE MEMBER COORDS B1.
#
# OUTPUT:       NORMAL.  EXIT WITH S(MPAC) = 0.
#
# (1)     CDUXD,CDUYD,CDUZD, DESIRED OUTER, INNER, MIDDLE CDU ANGLES,
# DP, IS COMPL, SCALED 180 DEGREES (HALF-REVS B0).
# (2)     DELCDUX,DELCDUY,DELCDUZ.  0.1 SEC DCU ANGULAR INCREMENTS,
# DP, IS COMPL, SCALED 180 DEG.
# (3)     WBODY,WBODY1,WBODY2.  LOS ANGULAR RATE IN CONTROL COORDS,
# DP, IS COMPL, SCALED 450 DEG/SEC.
#
# SPECIAL.  EXIT WITH S(MPAC) = 1.
#
# (1)     CPHI,CTHETA,CPSI.  DESIRED OUTER, INNER, MIDDLE CDU ANGLES,
# SP, 2'S COMPL, SCALED 180 DEGREES.
#
# EXTERNAL SUBROUTINES USED     (B)=BASIC
#
# (1) CALCGA              (5) LOADTIME(B)         (9) SMNB
# (2) CDUTRIG             (6) MATMOVE
# (3) CSMCONIC            (7) RCDUS(B)
# (4) LEMCONIC            (8) SMCDURES
#
# ERASABLE
#
# (1) S(Q611),EBANK7      CRS61.1 EXIT.
# (2) S(Q6111),EBANK7     CALCDCDU EXIT.
# (3) T(SAVEDCDU),E6      SP VECTOR OF CDUDS.
# (4) V(SAVEPOS),E7       CSM POS VEC AND D(SAVEPOS)= LENGTH OF LOS.
# (5) V(SAVEVEL),E7       CSM VEL VEC.
#
# FLAGWDS:      HOLDFLAG.  USED, NOT SET.
#
# MISC: (1) ERASABLE ITEMP1 USED TO TEMP STORE EBANK UNDER INHINT.
# (2) ERASABLE P21TIME USED AS TEMP STORE DURING CRS61.1
# (3) ERAS DTHETASM USED AS TEMP STORE DURING EARLY CRS61.1
#
# DEBRIS -- CURRENT VAC AREA, CRS61.1 ERASABLES, ITEMP1, P21TIME

#   BANK 24
#   SETLOC P20S4
#   BANK

#   EBANK= CDUXD
#   COUNT* $/CRS61

W('34,3343', 0o40220, 'CRS61.1', 'STQ', 'SETPD', kind='interp', line=1517)
W('34,3344', 0o03704, '', '', 'Q611', kind='operand', line=1518)
W('34,3345', 0o00001, '', '', '0', kind='operand', line=1519)
W('34,3346', 0o77634, '', 'RTB', kind='interp', line=1520)
# Page 593
W('34,3347', 0o45510, '', '', 'LOADTIME', 'LOAD CLOCK TIME2,1 INTO MPAC.', kind='operand', line=1522)

W('34,3350', 0o36316, 'STORT', 'STCALL', 'P21TIME', 'STORE CLOCK TIME FOR SUBR R63', kind='interp', line=1524)
W('34,3351', 0o71572, '', '', 'R63', 'SUBR TO CALC DCDU (T=PRESENT,PASS1)', kind='operand', line=1525)
W('34,3352', 0o77751, '', 'TLOAD', kind='interp', line=1526)
W('34,3353', 0o01156, '', '', 'THETAD', 'SAVE DCDU(T) FROM CALCDCDU FOR STEP4.', kind='operand', line=1527)
W('34,3354', 0o03373, '', 'STORE', 'SAVEDCDU', kind='interp', line=1528)

W('34,3355', 0o77776, '', 'EXIT', kind='interp', line=1530)
W('34,3356', 0o03377, '', 'TC', 'STEP2CK', line=1531)
W('34,3357', 0o34371, 'AUTOCK', 'CAF', 'PRIO30', line=1532)
W('34,3360', 0o00006, '', 'EXTEND', line=1533)
W('34,3361', 0o06031, '', 'RXOR', 'CHAN31', line=1534)
W('34,3362', 0o77707, '', 'MASK', 'FURST3', line=1535)
W('34,3363', 0o00006, '', 'EXTEND', '', 'AUTO MODE SELECTED (BITS 15-13=011)', line=1536)
W('34,3364', 0o13366, '', 'BZF', 'DAPCK', '      YES -- CONTINUE.', line=1537)
W('34,3365', 0o03372, '', 'TC', 'ASET', line=1538)

W('34,3366', 0o40075, 'DAPCK', 'CS', 'FLAGWRD1', 'IS STIKFLAG SET (I.E., IS SOMEONE ON RHC)', line=1540)
W('34,3367', 0o75002, '', 'MASK', 'STIKBIT', line=1541)
W('34,3370', 0o10000, '', 'CCS', 'A', line=1542)
W('34,3371', 0o03432, '', 'TC', 'STEP3CK', line=1543)
W('34,3372', 0o35021, 'ASET', 'CAF', 'ZERO', line=1544)
W('34,3373', 0o54154, '', 'TS', 'MPAC', line=1545)
W('34,3374', 0o06006, '', 'TC', 'INTPRET', 'EXIT CRS61.1', line=1546)
W('34,3375', 0o77650, '', 'GOTO', kind='interp', line=1547)
W('34,3376', 0o03704, '', '', 'Q611', kind='operand', line=1548)

W('34,3377', 0o04662, 'STEP2CK', 'TC', 'BANKCALL', line=1550)
W('34,3400', 0o57757, '', 'CADR', 'UPACTOFF', kind='data', line=1551)

W('34,3401', 0o35016, '', 'CAF', 'TWO', 'SET TEMPORARY INDEX DTHETASM = 2', line=1553)
W('34,3402', 0o55611, 'CDULOOP', 'TS', 'DTHETASM', line=1554)
W('34,3403', 0o51611, '', 'INDEX', 'DTHETASM', line=1555)
W('34,3404', 0o30032, '', 'CA', 'CDUX', 'SET A = ACTUAL CDU (ACDU).', line=1556)
W('34,3405', 0o00006, '', 'EXTEND', line=1557)
W('34,3406', 0o51611, '', 'INDEX', 'DTHETASM', 'SET INDEX TO ACCESS DESIRED CDU (DCDU).', line=1558)
W('34,3407', 0o21155, '', 'MSU', 'THETAD', 'A = DIFF = ACDU - DCDU.', line=1559)
W('34,3410', 0o54154, '', 'TS', 'MPAC', 'RETURN TO INTERPRETER FOR 10 DEGREE CK.', line=1560)
W('34,3411', 0o06006, '', 'TC', 'INTPRET', '(DP APPROX SP OK FOR ROUGH CHECK)', line=1561)
W('34,3412', 0o45246, '', 'ABS', 'DSU', kind='interp', line=1562)
W('34,3413', 0o31661, '', '', 'DEGREE10', 'IS (ACDU - DCDU) MORE THAN 10 DEGREES.', kind='operand', line=1563)
W('34,3414', 0o77444, '', 'BPL', 'EXIT', 'NO -- OK, CONTINUE CHECKING OTHER ANGLES.', kind='interp', line=1564)
W('34,3415', 0o71421, '', '', 'STKTEST', 'TEST STICK FLAG', kind='operand', line=1565)
W('34,3416', 0o11611, '', 'CCS', 'DTHETASM', 'HAVE ALL 3 ANGLE DIFFS BEEN CHECKED.', line=1566)
W('34,3417', 0o03402, '', 'TC', 'CDULOOP', 'NO -- DIM COUNT, CHECK NEXT ANGLE DIFF.', line=1567)
W('34,3420', 0o03357, '', 'TC', 'AUTOCK', line=1568)
W('34,3421', 0o77776, 'STKTEST', 'EXIT', kind='interp', line=1569)
W('34,3422', 0o40075, '', 'CS', 'FLAGWRD1', line=1570)
W('34,3423', 0o75002, '', 'MASK', 'STIKBIT', line=1571)
# Page 594
W('34,3424', 0o10000, '', 'CCS', 'A', line=1573)
W('34,3425', 0o03563, '', 'TC', 'MANUEXIS', 'STIKFLAG IS NOT SET (DO R63)', line=1574)
W('34,3426', 0o35015, '', 'CAF', 'BIT3', line=1575)
W('34,3427', 0o00006, '', 'EXTEND', '', 'STIKFLG IS SET', line=1576)
W('34,3430', 0o05011, '', 'WOR', 'DSALMOUT', 'TURN ON UPACTY LIGHT', line=1577)

W('34,3431', 0o03372, '', 'TC', 'ASET', 'EXIT AND SET R61CNTR', line=1579)
W('34,3432', 0o06006, 'STEP3CK', 'TC', 'INTPRET', line=1580)
W('34,3433', 0o77601, '', 'SETPD', kind='interp', line=1581)
W('34,3434', 0o00001, '', '', '0', '*', kind='operand', line=1582)
# NOW HAVE DCDUS STORED IN T(SAVEDCDU).
# GO CALC OTHER DAP INPUTS (DELCDU,WBODY)
W('34,3435', 0o52375, 'CRS61.2', 'VLOAD', 'VSU', kind='interp', line=1585)
W('34,3436', 0o03204, '', '', 'DCDU', kind='operand', line=1586)
W('34,3437', 0o03715, '', '', 'SAVEVEL', 'DV = VL - VC', kind='operand', line=1587)
W('34,3440', 0o57456, '', 'UNIT', 'VCOMP', 'V(MPAC)=-UNITDV. VAC36D=ABSDV.', kind='interp', line=1588)
W('34,3441', 0o74235, '', 'VXV', 'VXSC', '(-UNITDV)CROSS(UNITLOS).', kind='interp', line=1589)
W('34,3442', 0o03707, '', '', 'SAVEPOS', kind='operand', line=1590)
W('34,3443', 0o31662, '', '', 'RVCS/RDS', '(UNITLOS B1)(UNITDV B1)(CONST B4)=CROSS.', kind='operand', line=1591)
W('34,3444', 0o77606, '', 'PUSH', '', 'HOLD CROSS IN PUSHLIST0.  SCALED B6.', kind='interp', line=1592)
W('34,3445', 0o60345, '', 'DLOAD', 'NORM', 'OBTAIN ABS VALUE OF LOS.', kind='interp', line=1593)
W('34,3446', 0o02316, '', '', 'P21TIME', 'P21TIME IS TEMP STORE FOR ABSLOS.', kind='operand', line=1594)
W('34,3447', 0o00047, '', '', 'X1', kind='operand', line=1595)
W('34,3450', 0o77606, '', 'PUSH', '', 'NORM ABSLOS(DENOM) AND HOLD IN PUSH1.', kind='interp', line=1596)

W('34,3451', 0o60345, '', 'DLOAD', 'NORM', kind='interp', line=1598)
W('34,3452', 0o00045, '', '', '36D', 'NORM ABS VALUE OF DV(NUM).', kind='operand', line=1599)
W('34,3453', 0o00051, '', '', 'S1', kind='operand', line=1600)

W('34,3454', 0o70460, '', 'XSU,1', 'SR1', 'X1 = X1(N DENOM)-S1(N NUM).', kind='interp', line=1602)
W('34,3455', 0o00050, '', '', 'S1', 'SR1 TO AVOID OFLOW ON DOV.', kind='operand', line=1603)
W('34,3456', 0o74271, '', 'DDV', 'VXSC', 'ABSDV(MPAC)/ABSLOS(PUSH1) = QUOT.', kind='interp', line=1604)
W('34,3457', 0o77730, '', 'SXA,1', '', 'QUOT(MPAC) X CROSS(PUSH0)', kind='interp', line=1605)
W('34,3460', 0o03705, '', '', 'Q6111', 'SAVE SCALE OF RESULT (R-15,1X).', kind='operand', line=1606)
# X1= NORM OF QUOT. QTUOT SCALE B7-B29=B-22
# CROSS IS SCALED B6.  NEED SL1 TO RECOVER
# SR1 SO THAT -22+6+1=-15.  MPAC NOW HOLDS
# ORTHO LOS RATE (OMEGA TH, B-15,X1).
W('34,3461', 0o76521, '', 'MXV', 'VSL1', 'OBTAIN RATE IN SM COORDS (OMEGTHSM) AND', kind='interp', line=1611)
W('34,3462', 0o01736, '', '', 'REFSMMAT', 'ADJUST FOR REFSMMAT SCALE OF B1.', kind='operand', line=1612)
W('34,3463', 0o00025, '', 'STORE', '20D', 'OMEGTHSM = VAC20D', kind='interp', line=1613)
# DELTA THETA SM = OMEGTHSM * .1B-3.
W('34,3464', 0o77761, '', 'VXSC', kind='interp', line=1615)
W('34,3465', 0o31664, '', '', 'TENTH', kind='operand', line=1616)
W('34,3466', 0o03212, '', 'STORE', 'DTHETASM', 'STORE SM INCREM ANGLES FOR SMCDURES.', kind='interp', line=1617)
W('34,3467', 0o77624, '', 'CALL', kind='interp', line=1618)
W('34,3470', 0o47477, '', '', 'CDUTRIG', 'OBTAIN SIN,COSCDUS FOR SMCDURES.', kind='operand', line=1619)
W('34,3471', 0o45001, '', 'SETPD', 'CALL', 'SMCDURES USES PUSH', kind='interp', line=1620)
W('34,3472', 0o00001, '', '', '0', kind='operand', line=1621)
W('34,3473', 0o47742, '', '', 'SMCDURES', 'OBTAIN DELCDU IN V(DCDU).', kind='operand', line=1622)
# Page 595
W('34,3474', 0o77750, '', 'LXA,1', '', 'RELOAD X1', kind='interp', line=1624)
W('34,3475', 0o03705, '', '', 'Q6111', kind='operand', line=1625)
W('34,3476', 0o53775, '', 'VLOAD', 'VSL*', 'RECOVER SCALE.', kind='interp', line=1626)
W('34,3477', 0o03204, '', '', 'DCDU', '(B-15,X1) + TENTH(B-3) + HALFREVS(B1)', kind='operand', line=1627)
W('34,3500', 0o20160, '', '', '0 -17D,1', 'EQUALS B-17D,1 TO OBTAIN HALFREVS B0.', kind='operand', line=1628)
W('34,3501', 0o00017, '', 'STORE', '14D', 'HOLD DELS IN V(VAC14D) FOR AUTOPILOT.', kind='interp', line=1629)

W('34,3502', 0o77624, '', 'CALL', '', 'COMPUTES SINES AND COSINES FOR *SMNB*', kind='interp', line=1631)
W('34,3503', 0o47477, '', '', 'CDUTRIG', kind='operand', line=1632)
W('34,3504', 0o45175, '', 'VLOAD', 'CALL', 'LOAD VECTOR AND CALL TRANSFORMATION', kind='interp', line=1633)
W('34,3505', 0o00025, '', '', '20D', 'VECTOR FOR TRG*SMNB INTO MPAC', kind='operand', line=1634)
W('34,3506', 0o47644, '', '', '*SMNB*', 'OBTAIN ANG. RATE REFERRED TO NB (BODY)', kind='operand', line=1635)
W('34,3507', 0o77721, '', 'MXV', kind='interp', line=1636)
W('34,3510', 0o31670, '', '', 'MBDYTCTL', 'CONVERT RATE(OMEGA) TO CONTROL COORDS.', kind='operand', line=1637)
W('34,3511', 0o77761, '', 'VXSC', '', 'MULT. BY 0.8 TO RESCALE REVS TO 450 DEG.', kind='interp', line=1638)
W('34,3512', 0o15271, '', '', 'POINT8', 'RECOVER SCALE.', kind='operand', line=1639)
W('34,3513', 0o53750, '', 'LXA,1', 'VSL*', 'RELOAD X1 TO RECOVER NORMALIZ.', kind='interp', line=1640)
W('34,3514', 0o03705, '', '', 'Q6111', '(B-15,X1) + MBDYTCTL(B1) = B-14D,1 TO', kind='operand', line=1641)
W('34,3515', 0o20163, '', '', '0 -14D,1', 'OBTAIN REVS SCALED AT 450 DEGREES.', kind='operand', line=1642)

W('34,3516', 0o77776, 'CRS61.2A', 'EXIT', kind='interp', line=1644)
W('34,3517', 0o00004, '', 'INHINT', line=1645)
W('34,3520', 0o35021, '', 'CAF', 'ZERO', 'TRANSFER DESIRED GIMBAL ANGLES', line=1646)
W('34,3521', 0o55647, '', 'TS', 'CDUXD +1', 'FROM T(SAVEDCDU) TO V(CDUXD).', line=1647)
W('34,3522', 0o55651, '', 'TS', 'CDUYD +1', line=1648)
W('34,3523', 0o55653, '', 'TS', 'CDUZD +1', line=1649)
W('34,3524', 0o31772, '', 'CA', 'SAVEDCDU', line=1650)
W('34,3525', 0o55646, '', 'TS', 'CDUXD', line=1651)
W('34,3526', 0o31773, '', 'CA', 'SAVEDCDU +1', line=1652)
W('34,3527', 0o55650, '', 'TS', 'CDUYD', line=1653)
W('34,3530', 0o31774, '', 'CA', 'SAVEDCDU +2', line=1654)
W('34,3531', 0o55652, '', 'TS', 'CDUZD', line=1655)

W('34,3532', 0o00006, '', 'EXTEND', '', 'TRANSFER OMEGA CONTROL (ANG. LOS RATE)', line=1657)
W('34,3533', 0o30155, '', 'DCA', 'MPAC', 'FROM V(MPAC) TO V(WBODY)', line=1658)
W('34,3534', 0o53526, '', 'DXCH', 'WBODY', line=1659)
W('34,3535', 0o00006, '', 'EXTEND', line=1660)
W('34,3536', 0o30160, '', 'DCA', 'MPAC +3', line=1661)
W('34,3537', 0o53530, '', 'DXCH', 'WBODY1', line=1662)
W('34,3540', 0o00006, '', 'EXTEND', line=1663)
W('34,3541', 0o30162, '', 'DCA', 'MPAC +5', line=1664)
W('34,3542', 0o53532, '', 'DXCH', 'WBODY2', line=1665)

W('34,3543', 0o00006, '', 'EXTEND', '', 'TRANSFER CDU INCREMENTS', line=1667)
W('34,3544', 0o50120, '', 'INDEX', 'FIXLOC', 'FROM V(VAC14D) TO V(DELCDUX)', line=1668)
W('34,3545', 0o30017, '', 'DCA', '14D', line=1669)
W('34,3546', 0o53576, '', 'DXCH', 'DELCDUX', line=1670)
W('34,3547', 0o00006, '', 'EXTEND', line=1671)
W('34,3550', 0o50120, '', 'INDEX', 'FIXLOC', line=1672)
W('34,3551', 0o30021, '', 'DCA', '16D', line=1673)
# Page 596
W('34,3552', 0o53600, '', 'DXCH', 'DELCDUY', line=1675)
W('34,3553', 0o00006, '', 'EXTEND', line=1676)
W('34,3554', 0o50120, '', 'INDEX', 'FIXLOC', line=1677)
W('34,3555', 0o30023, '', 'DCA', '18D', line=1678)
W('34,3556', 0o53602, '', 'DXCH', 'DELCDUZ', line=1679)
W('34,3557', 0o45017, '', 'CS', 'ONE', 'NOW DAP VARIABLES LOADED.  SET HOLDFLAG.', line=1680)
W('34,3560', 0o55332, '', 'TS', 'HOLDFLAG', 'TO -1.', line=1681)
W('34,3561', 0o00003, '', 'RELINT', line=1682)
W('34,3562', 0o03372, '', 'TC', 'ASET', line=1683)
W('34,3563', 0o06006, 'MANUEXIS', 'TC', 'INTPRET', line=1684)
W('34,3564', 0o77751, 'MANUEXIT', 'TLOAD', '', 'ENTER FROM STEP2.  ACDU-DCDU EXCEEDS', kind='interp', line=1685)
W('34,3565', 0o03373, '', '', 'SAVEDCDU', '10 DEG. STORE DCDU(T) IN CPHI,CTHETA,', kind='operand', line=1686)
W('34,3566', 0o01156, '', 'STORE', 'CPHI', 'CPSI FOR KALCMANU.', kind='interp', line=1687)
W('34,3567', 0o52135, '', 'SLOAD', 'GOTO', 'SPECIAL RETURN (MPAC+0 = 1)', kind='interp', line=1688)
W('34,3570', 0o31712, '', '', 'LOONE', 'OCTAL 00001', kind='operand', line=1689)
W('34,3571', 0o03704, '', '', 'Q611', kind='operand', line=1690)

W('34,3572', 0o71220, 'R63', 'STQ', 'DLOAD', 'SUBR TO CALC DCDUS(T)', kind='interp', line=1692)
W('34,3573', 0o03705, '', '', 'Q6111', kind='operand', line=1693)
W('34,3574', 0o02316, '', '', 'P21TIME', kind='operand', line=1694)
W('34,3575', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1695)
W('34,3576', 0o27114, '', '', 'CSMCONIC', kind='operand', line=1696)
W('34,3577', 0o77775, 'HOLDATT', 'VLOAD', '', 'HOLD EXTRAPOLATED CSM POSITION AND', kind='interp', line=1697)
W('34,3600', 0o00001, '', '', 'RATT', 'VELOCITY', kind='operand', line=1698)
W('34,3601', 0o27707, '', 'STOVL', 'SAVEPOS', kind='interp', line=1699)
W('34,3602', 0o00007, '', '', 'VATT', kind='operand', line=1700)
W('34,3603', 0o03715, '', 'STORE', 'SAVEVEL', kind='interp', line=1701)
W('34,3604', 0o77745, 'CALCLEM', 'DLOAD', '', 'EXTRAPOLATE LEM STATE VECTOR TO SAVE', kind='interp', line=1702)
W('34,3605', 0o02316, '', '', 'P21TIME', 'TIME AS CSM USING LEMCONIC', kind='operand', line=1703)
W('34,3606', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1704)
W('34,3607', 0o27126, '', '', 'LEMCONIC', kind='operand', line=1705)
W('34,3610', 0o77775, '', 'VLOAD', kind='interp', line=1706)
W('34,3611', 0o00007, '', '', 'VATT', kind='operand', line=1707)
W('34,3612', 0o27204, '', 'STOVL', 'DCDU', 'STORE VATT IN DCDU TEMPORARILY', kind='interp', line=1708)
W('34,3613', 0o00001, '', '', 'RATT', 'LOS = RL RC', kind='operand', line=1709)
W('34,3614', 0o53451, '', 'VSU', 'UNIT', kind='interp', line=1710)
W('34,3615', 0o03707, '', '', 'SAVEPOS', kind='operand', line=1711)
W('34,3616', 0o03707, '', 'STORE', 'SAVEPOS', 'SAVE UNITLOS FOR CRS61.2 RATE CALC.', kind='interp', line=1712)
W('34,3617', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=1713)
W('34,3620', 0o01736, '', '', 'REFSMMAT', 'CONVERT TO STABLE MEMBER', kind='operand', line=1714)
W('34,3621', 0o17357, '', 'STODL', 'POINTVSM', kind='interp', line=1715)
W('34,3622', 0o00045, '', '', '36D', 'HOLD ABS VAL OF LOS (VAC 36D)', kind='operand', line=1716)
W('34,3623', 0o02316, '', 'STORE', 'P21TIME', 'IN D(P21TIME) FOR CRS61.2 RATE CALC.', kind='interp', line=1717)
W('34,3624', 0o77775, '', 'VLOAD', kind='interp', line=1718)
W('34,3625', 0o15333, '', '', 'UNITX', kind='operand', line=1719)
W('34,3626', 0o37351, '', 'STCALL', 'SCAXIS', 'TRACK AXIS UNIT VECTOR', kind='interp', line=1720)
W('34,3627', 0o56126, '', '', 'VECPOINT', 'FOR +X-AXIS TRACKING ATTITUDE', kind='operand', line=1721)
W('34,3630', 0o01334, '', 'STORE', 'CPHIX', 'STORE ANGLES FOR N96 DISPLAY', kind='interp', line=1722)
W('34,3631', 0o77775, '', 'VLOAD', kind='interp', line=1723)
W('34,3632', 0o31653, '', '', 'PRFUNIT', kind='operand', line=1724)
# Page 597
W('34,3633', 0o37351, '', 'STCALL', 'SCAXIS', kind='interp', line=1726)
W('34,3634', 0o56126, '', '', 'VECPOINT', kind='operand', line=1727)
W('34,3635', 0o03723, '', 'STORE', 'PRAXIS', 'STORE ANGLES FOR N95 DISPLAY', kind='interp', line=1728)
W('34,3636', 0o77614, '', 'BOFF', kind='interp', line=1729)
W('34,3637', 0o02745, '', '', 'PRFTRKAT', kind='operand', line=1730)
W('34,3640', 0o71644, '', '', 'CRSTOR1', kind='operand', line=1731)
W('34,3641', 0o01156, 'CRSTOR', 'STORE', 'THETAD', 'STORE ANGLES FOR N18 DISPLAY', kind='interp', line=1732)
W('34,3642', 0o77650, '', 'GOTO', kind='interp', line=1733)
W('34,3643', 0o03705, '', '', 'Q6111', kind='operand', line=1734)
W('34,3644', 0o77775, 'CRSTOR1', 'VLOAD', kind='interp', line=1735)
W('34,3645', 0o15333, '', '', 'UNITX', kind='operand', line=1736)
W('34,3646', 0o03351, '', 'STORE', 'SCAXIS', kind='interp', line=1737)
W('34,3647', 0o52151, '', 'TLOAD', 'GOTO', kind='interp', line=1738)
W('34,3650', 0o01334, '', '', 'CPHIX', kind='operand', line=1739)
W('34,3651', 0o71641, '', '', 'CRSTOR', kind='operand', line=1740)
W('34,3652', 0o15066, 'PRFUNIT', '2DEC', '.40957602', '55 DEG TRACK AXIS UNIT VECTOR', kind='data', line=1741)
W('34,3653', 0o17626, kind='data', line=1741)

W('34,3654', 0o00000, '', '2DEC', '0.0', 'FOR USE WITH VECPOINT', kind='data', line=1743)
W('34,3655', 0o00000, kind='data', line=1743)

W('34,3656', 0o11132, '', '2DEC', '.28678822', kind='data', line=1745)
W('34,3657', 0o27477, kind='data', line=1745)

W('34,3660', 0o01616, 'DEGREE10', 'DEC', '.05556', '10 DEG IN REVS                STEP2', kind='data', line=1747)
W('34,3661', 0o37651, 'RVCS/RDS', '2DEC', '15.915494 B-4', '100/2PI REV-CSEC/RAD-SEC.', kind='data', line=1748)
W('34,3662', 0o16721, kind='data', line=1748)

W('34,3663', 0o31463, 'TENTH', '2DEC', '.1 B+3', '.1 B-3 (TO SCALE ANG. RATE TO .1 INREMS)', kind='data', line=1750)
W('34,3664', 0o06315, kind='data', line=1750)

W('34,3665', 0o20000, 'MAT1B1', '2DEC', '1.0 B-1', kind='data', line=1752)
W('34,3666', 0o00000, kind='data', line=1752)

W('34,3667', 0o20000, 'MBDYTCTL', '2DEC', '.5', '              7.25 DEG NEGATIVE', kind='data', line=1754)
W('34,3670', 0o00000, kind='data', line=1754)

W('34,3671', 0o00000, '', '2DEC', '0', '              X-AXIS ROTATION MATRIX', kind='data', line=1756)
W('34,3672', 0o00000, kind='data', line=1756)

W('34,3673', 0o00000, '', '2DEC', '0', '              CONVERTS BODY TO CTL', kind='data', line=1758)
W('34,3674', 0o00000, kind='data', line=1758)

W('34,3675', 0o00000, '', '2DEC', '0', '              AXES.  CAME AS QUADROT', kind='data', line=1760)
W('34,3676', 0o00000, kind='data', line=1760)

W('34,3677', 0o17676, '', '2DEC', '.99200495 B-1', 'COS7.25 B1    BUT SCALED B', kind='data', line=1762)
W('34,3700', 0o20113, kind='data', line=1762)

W('34,3701', 0o75766, '', '2DEC', '-.12619897 B-1', '-SIN7.25 B1', kind='data', line=1764)
W('34,3702', 0o45544, kind='data', line=1764)

W('34,3703', 0o00000, '', '2DEC', '0', kind='data', line=1766)
W('34,3704', 0o00000, kind='data', line=1766)

W('34,3705', 0o02011, '', '2DEC', '.12619897 B-1', 'SIN7.25 B1', kind='data', line=1768)
W('34,3706', 0o32233, kind='data', line=1768)

W('34,3707', 0o17676, '', '2DEC', '.99200495 B-1', 'COS7.25 B1', kind='data', line=1770)
W('34,3710', 0o20113, kind='data', line=1770)

W('34,3711', 0o00001, 'LOONE', 'OCT', '00001', 'TO SET MPAC = 00001 FOR SPECIAL EXIT.', kind='data', line=1772)
S('FURST3', 'equals', 0o7707, line=1773)  # CONSTANT FOR AUTOCK (OCT 70000).

# Page 598
# ..... S22.1 ORBITAL NAVIGATION ROUTINE
# MOD 1
#
# FUNCTIONAL DESCRIPTION
# 1.  UPDATE CSM STATE VECTOR
# 2.  UPDATE LANDMARK POSITION
# 3.  CONVERT W MATRIX FROM 9 TO 6 DIMENSIONS
#
# SUBROUTINES CALLED
# INTSTALL,INTEGRV,GETNUM,SETRE,R-TO-TP,RP-TO-R,BVECTORS,INCORP1,INCORP2
# LALOTORV,S22F2410,LAT-LONG,ROWDOT
#
# ERASABLE INITIALIZATION
# W=9X9 MATRIX
# ORBWFLAG=0 FOR INVALID W MATRIX, =1 FOR VALID W MATRIX
# ASTRONAUT ENTRY OF KNOWN,L,OFF
# 8NN= NUMBER OF MARKS, DECIMAL INTEGER B-14
# REFSMMAT= TRANSFORMATION MATRIX
# MARKSTAT= ADDRESS OF START OF MARK DATA (MARK DATA OF EACH MARK IS
# STORED AS FOLLOWS: TIME,AIG,SA,AMG,PA,AOG) TIME IS IN DOUBLE
# PRECISION, ALL OTHERS ARE IN SINGLE PRECISION
# CSM STATE VECTOR
#
# OUTPUT
# UPDATED CSM STATE VECTOR
# UPDATED LANDMARK POSITION
# NEW 6 DIMENSIONAL W MATRIX
#
# DEBRIS
# PUSH LIST,CSMPOS,ALPHAV,ERADM,UM,RCLP,USTAR,VARIANCE,X789,BVECTOR,8KK,
# S22LOC,SVMRKDAT TABLE,22SUBSCL,LANDMARK,CXOFF,S22C,LAT,LOG,ALT,
# TEMPOR1,S22TOFF,S221OFF,DSPTEM1,S22EORM,S22TPRIM

#   BANK 13

#   SETLOC P20S6
#   BANK

#   EBANK= LANDMARK
#   COUNT 35/LUORB

W('30,2312', 0o66220, 'S22.1', 'STQ', 'SSP', kind='interp', line=1817)
W('30,2313', 0o03703, '', '', 'S22RTNEX', kind='operand', line=1818)
W('30,2314', 0o00051, '', '', 'S1', kind='operand', line=1819)
W('30,2315', 0o00006, '', 'DEC', '6', kind='data', line=1820)
W('30,2316', 0o66331, '', 'SSP', 'SSP', 'SET I=1       ITEM 8KK IS I', kind='interp', line=1821)
W('30,2317', 0o02747, '', '', '8KK', kind='operand', line=1822)
W('30,2320', 0o00001, '', 'DEC', '1', kind='data', line=1823)
W('30,2321', 0o02751, '', '', 'S22LOC', kind='operand', line=1824)
W('30,2322', 0o03537, '', 'ECADR', 'SVMRKDAT', 'SET MARK DATA ADDRESS INTO S22LOC', kind='data', line=1825)
# Page 599
W('30,2323', 0o76144, '', 'LXC,2', 'AXT,1', kind='interp', line=1827)
W('30,2324', 0o01330, '', '', 'MARKSTAT', kind='operand', line=1828)
W('30,2325', 0o00044, '', 'DEC', '36', kind='data', line=1829)
W('30,2326', 0o77773, 'S22.111', 'VLOAD*', '', 'MOVE MARK DATA (5 SETS FROM ADDR. IN', kind='interp', line=1830)
W('30,2327', 0o77776, '', '', '0,2', 'MARKSTAT TO SVMRKDAT TABLE TO AVOID LOSS', kind='operand', line=1831)
W('30,2330', 0o07604, '', 'STORE', 'SVMRKDAT +36D,1', 'IF RESTART OCCURS', kind='interp', line=1832)
W('30,2331', 0o60114, '', 'INCR,2', 'TIX,1', kind='interp', line=1833)
W('30,2332', 0o77771, '', 'DEC', '-6', kind='data', line=1834)
W('30,2333', 0o60326, '', '', 'S22.111', kind='operand', line=1835)
W('30,2334', 0o77414, '', 'SET', 'EXIT', kind='interp', line=1836)
W('30,2335', 0o01464, '', '', 'P22MKFLG', 'DOWNLINKED SVMRKDAT HOLDS PRESENT MARKS', kind='operand', line=1837)
W('30,2336', 0o04662, '', 'TC', 'BANKCALL', 'RELEASE VAC AREA WHERE MARK DATA WAS', line=1838)
W('30,2337', 0o16063, '', 'CADR', 'MKRELEAS', kind='data', line=1839)
W('30,2340', 0o05372, '', 'TC', '2PHSCHNG', line=1840)
W('30,2341', 0o00004, '', 'OCT', '00004', kind='data', line=1841)
W('30,2342', 0o05022, '', 'OCT', '05022', kind='data', line=1842)
W('30,2343', 0o13000, '', 'OCT', '13000', kind='data', line=1843)
W('30,2344', 0o06006, '', 'TC', 'INTPRET', line=1844)
W('30,2345', 0o43170, '', 'AXT,1', 'BOFF', kind='interp', line=1845)
W('30,2346', 0o00000, '', '', '0D', kind='operand', line=1846)
W('30,2347', 0o04343, '', '', 'CMOONFLG', '=0 EARTH, =1 MOON', kind='operand', line=1847)
W('30,2350', 0o60353, '', '', 'S22SHIFT', kind='operand', line=1848)
W('30,2351', 0o77710, '', 'INCR,1', kind='interp', line=1849)
W('30,2352', 0o77775, '', 'DEC', '-2', kind='data', line=1850)
W('30,2353', 0o40330, 'S22SHIFT', 'SXA,1', 'SETPD', kind='interp', line=1851)
W('30,2354', 0o03673, '', '', 'S22EORM', 'SET =0 EARTH, =-2 MOON FOR SHIFTING', kind='operand', line=1852)
W('30,2355', 0o00001, '', '', '0D', kind='operand', line=1853)
W('30,2356', 0o77624, 'FIG2EXIT', 'CALL', kind='interp', line=1854)
W('30,2357', 0o27442, '', '', 'INTSTALL', kind='operand', line=1855)
W('30,2360', 0o77624, '', 'CALL', kind='interp', line=1856)
W('30,2361', 0o62355, '', '', 'S22FLGS', kind='operand', line=1857)
# FLOWCHART D=0   THEN DIM0FLAG=0, D6O9FLG NOT TESTED
# FLOWCHART D=6   THEN DIM0FLAG=1, D60R9FLG=0
# FLOWCHART D=9   THEN DIM0FLAG=1, D6OR9FLG=1

W('30,2362', 0o43014, '', 'BOFF', 'CLRGO', kind='interp', line=1862)
W('30,2363', 0o01751, '', '', 'ORBWFLAG', kind='operand', line=1863)
W('30,2364', 0o60367, '', '', 'SETWW5D', 'BRANCH TO SET W0-W5,ORBWFLAG,D', kind='operand', line=1864)
W('30,2365', 0o01635, '', '', 'D6OR9FLG', 'FLOWCHART D=6 PATH', kind='operand', line=1865)
W('30,2366', 0o60414, '', '', 'SETVANDI', kind='operand', line=1866)
W('30,2367', 0o77614, 'SETWW5D', 'CLEAR', kind='interp', line=1867)
W('30,2370', 0o01676, '', '', 'DIM0FLAG', 'FLOWCHART D=0 PATH', kind='operand', line=1868)
W('30,2371', 0o66370, '', 'AXT,1', 'SSP', kind='interp', line=1869)
W('30,2372', 0o00154, '', 'DEC', '108', kind='data', line=1870)
W('30,2373', 0o00051, '', '', 'S1', kind='operand', line=1871)
W('30,2374', 0o00006, '', 'DEC', '6', kind='data', line=1872)
W('30,2375', 0o77214, '', 'CLEAR', 'VLOAD', kind='interp', line=1873)
W('30,2376', 0o02676, '', '', 'RENDWFLG', 'GSOP CHANGE 8/18/67', kind='operand', line=1874)
W('30,2377', 0o15335, '', '', 'ZEROVECS', kind='operand', line=1875)
W('30,2400', 0o06555, 'CLEARWW5', 'STORE', 'W +108D,1', kind='interp', line=1876)
# Page 600
W('30,2401', 0o67300, '', 'TIX,1', 'SLOAD', kind='interp', line=1878)
W('30,2402', 0o60400, '', '', 'CLEARWW5', kind='operand', line=1879)
W('30,2403', 0o02005, '', '', 'WORBPOS', kind='operand', line=1880)
W('30,2404', 0o02401, '', 'STORE', 'W', 'SET DIAGONALS OF W0', kind='interp', line=1881)
W('30,2405', 0o02411, '', 'STORE', 'W +8D', kind='interp', line=1882)
W('30,2406', 0o02421, '', 'STORE', 'W +16D', kind='interp', line=1883)
W('30,2407', 0o77735, '', 'SLOAD', kind='interp', line=1884)
W('30,2410', 0o02006, '', '', 'WORBVEL', kind='operand', line=1885)
W('30,2411', 0o02511, '', 'STORE', 'W +72D', 'SET DIAGONALS OF W4', kind='interp', line=1886)
W('30,2412', 0o02521, '', 'STORE', 'W +80D', kind='interp', line=1887)
W('30,2413', 0o02531, '', 'STORE', 'W +88D', kind='interp', line=1888)
W('30,2414', 0o77614, 'SETVANDI', 'CLEAR', kind='interp', line=1889)
W('30,2415', 0o02666, '', '', 'DMENFLG', '0=6X6W, 1=9X9W', kind='operand', line=1890)
W('30,2416', 0o77624, 'S22NXTIN', 'CALL', kind='interp', line=1891)
W('30,2417', 0o62351, '', '', 'GETTF', kind='operand', line=1892)
W('30,2420', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1893)
W('30,2421', 0o27162, '', '', 'INTEGRV', kind='operand', line=1894)
W('30,2422', 0o77624, '', 'CALL', kind='interp', line=1895)
W('30,2423', 0o61332, '', '', 'S22CALRC', 'CALC. RC B-29 OR B-27 (CSMPOS)', kind='operand', line=1896)
W('30,2424', 0o66150, '', 'LXA,1', 'SXA,1', kind='interp', line=1897)
W('30,2425', 0o02750, '', '', 'S22LOC', 'SETUP ADDR. OF MARK DATA FOR GETUM SUBR.', kind='operand', line=1898)
W('30,2426', 0o01242, '', '', 'MARKDATA', kind='operand', line=1899)
W('30,2427', 0o77624, '', 'CALL', '', 'COMPUTE UM', kind='interp', line=1900)
W('30,2430', 0o47104, 'S2GETUM', '', 'GETUM', kind='operand', line=1901)
W('30,2431', 0o01235, '', 'STORE', 'UM', kind='interp', line=1902)
W('30,2432', 0o41535, 'DMPINTEG', 'SLOAD', 'PUSH', 'TEST OFF=I', kind='interp', line=1903)
W('30,2433', 0o02747, '', '', '8KK', kind='operand', line=1904)
W('30,2434', 0o50535, '', 'SLOAD', 'SR3', 'CXOFF SCALED B-5, MUST MOVE TO B-14', kind='interp', line=1905)
W('30,2435', 0o02746, '', '', 'CXOFF', 'BEFORE SUBT.', kind='operand', line=1906)
W('30,2436', 0o50442, '', 'SR3', 'SR3', kind='interp', line=1907)
W('30,2437', 0o77625, '', 'DSU', kind='interp', line=1908)
W('30,2440', 0o43030, '', 'BHIZ', 'BON', kind='interp', line=1909)
W('30,2441', 0o60755, '', '', 'S22OFF=I', 'BRANCH HERE IF OFF=I', kind='operand', line=1910)
W('30,2442', 0o02706, '', '', 'DMENFLG', '0=6X6W, 1=9X9W', kind='operand', line=1911)
W('30,2443', 0o60763, '', '', 'S22D=9', kind='operand', line=1912)
W('30,2444', 0o77624, '', 'CALL', kind='interp', line=1913)
W('30,2445', 0o56750, '', '', 'GRP2PC', kind='operand', line=1914)
W('30,2446', 0o77614, '', 'SET', kind='interp', line=1915)
W('30,2447', 0o01471, '', '', 'ORBWFLAG', kind='operand', line=1916)
W('30,2450', 0o43014, '', 'SET', 'SET', kind='interp', line=1917)
W('30,2451', 0o02466, '', '', 'DMENFLG', '=0 ON FIRST PASS THRU HERE FOR D=0, OR 6', kind='operand', line=1918)
W('30,2452', 0o01062, '', '', '22DSPFLG', '=1 TO DISPLAY DR,DV ON FIRST PASS', kind='operand', line=1919)
W('30,2453', 0o43014, '', 'SET', 'BON', kind='interp', line=1920)
W('30,2454', 0o00462, '', '', 'ERADFLAG', '=1 TO COMPUTE FISCHER RADIUS', kind='operand', line=1921)
W('30,2455', 0o03307, '', '', 'KNOWNFLG', kind='operand', line=1922)
W('30,2456', 0o61123, '', '', 'S22BOX22', kind='operand', line=1923)
W('30,2457', 0o53575, '', 'VLOAD', 'UNIT', 'UNIT ALSO PUTS ABVAL(RC) IN 36D', kind='interp', line=1924)
W('30,2460', 0o01207, '', '', 'CSMPOS', kind='operand', line=1925)
W('30,2461', 0o02152, '', 'STORE', 'ALPHAV', 'ALPHAV +4=SINL FOR SETRE', kind='interp', line=1926)
W('30,2462', 0o43014, '', 'CLEAR', 'BOFF', kind='interp', line=1927)
# Page 601
W('30,2463', 0o01663, '', '', 'LUNAFLAG', kind='operand', line=1929)
W('30,2464', 0o04343, '', '', 'CMOONFLG', kind='operand', line=1930)
W('30,2465', 0o60470, '', '', 'S22C=I', kind='operand', line=1931)
W('30,2466', 0o77614, '', 'SET', kind='interp', line=1932)
W('30,2467', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=1933)
W('30,2470', 0o77624, 'S22C=I', 'CALL', '', 'ERADM= R0 METERS B-29 BOTH EARTH/MOON', kind='interp', line=1934)
W('30,2471', 0o26601, '', '', 'SETRE', kind='operand', line=1935)
W('30,2472', 0o77624, '', 'CALL', '', 'COMPUTE RL FROM EQUATION 2.4.10', kind='interp', line=1936)
W('30,2473', 0o61277, '', '', 'S22F2410', 'STORED IN X789,MPAC B-27,B-29', kind='operand', line=1937)
W('30,2474', 0o70414, '', 'BOFF', 'VSR2', 'SCALE RL B-29 FOR BOTH EARTH/MOON', kind='interp', line=1938)
W('30,2475', 0o04343, '', '', 'CMOONFLG', kind='operand', line=1939)
W('30,2476', 0o60477, '', '', '+1', kind='operand', line=1940)
W('30,2477', 0o02635, '', 'STORE', 'S22RL', kind='interp', line=1941)
W('30,2500', 0o72441, '', 'DOT', 'SL1', kind='interp', line=1942)
W('30,2501', 0o01235, '', '', 'UM', kind='operand', line=1943)
W('30,2502', 0o24037, '', 'STOVL', 'S22D', 'D=UM RL B-29', kind='interp', line=1944)
W('30,2503', 0o15335, '', '', 'ZEROVECS', kind='operand', line=1945)
W('30,2504', 0o41401, '', 'SETPD', 'PUSH', kind='interp', line=1946)
W('30,2505', 0o00001, '', '', '0D', kind='operand', line=1947)
W('30,2506', 0o65206, '', 'PUSH', 'PDDL', 'SET 0-18D = I BACKWARDS', kind='interp', line=1948)
W('30,2507', 0o15333, '', '', 'HIDPHALF', 'PD 18', kind='operand', line=1949)
W('30,2510', 0o77702, '', 'SR2', '', 'B-3', kind='interp', line=1950)
W('30,2511', 0o00005, '', 'STORE', '4D', kind='interp', line=1951)
W('30,2512', 0o00011, '', 'STORE', '8D', kind='interp', line=1952)
W('30,2513', 0o24015, '', 'STOVL', '12D', kind='interp', line=1953)
W('30,2514', 0o01235, '', '', 'UM', 'B-1', kind='operand', line=1954)
W('30,2515', 0o24023, '', 'STOVL', 'S223X1', kind='interp', line=1955)
W('30,2516', 0o02635, '', '', 'S22RL', 'B-29', kind='operand', line=1956)
W('30,2517', 0o77624, '', 'CALL', '', '(UM)(RL T) B-30 STORED IN S22UMRL THRU', kind='interp', line=1957)
W('30,2520', 0o62332, '', '', 'S2231X13', 'S22UMRL +17D', kind='operand', line=1958)
W('30,2521', 0o66370, '', 'AXT,1', 'SSP', kind='interp', line=1959)
W('30,2522', 0o00022, '', 'DEC', '18', kind='data', line=1960)
W('30,2523', 0o00051, '', '', 'S1', kind='operand', line=1961)
W('30,2524', 0o00006, '', 'DEC', '6', kind='data', line=1962)
W('30,2525', 0o70573, 'S22NXTU', 'VLOAD*', 'VSR2', '(UM)(RL T) B-32', kind='interp', line=1963)
W('30,2526', 0o03524, '', '', 'S22UMRL +18D,1', kind='operand', line=1964)
W('30,2527', 0o77741, '', 'V/SC', kind='interp', line=1965)
W('30,2530', 0o00037, '', '', 'S22D', 'D B-29', kind='operand', line=1966)
W('30,2531', 0o45445, '', 'BVSU', 'STADR', 'SUBTRACT FROM I B-3', kind='interp', line=1967)
W('30,2532', 0o70253, '', 'STORE', 'S22UMRL +18D,1', 'U MATRIX B-3', kind='interp', line=1968)
W('30,2533', 0o76100, '', 'TIX,1', 'AXT,1', 'PD 0 AFTER TIX', kind='interp', line=1969)
W('30,2534', 0o60525, '', '', 'S22NXTU', kind='operand', line=1970)
W('30,2535', 0o00044, '', 'DEC', '36', 'S1 STILL 6 FROM ABOVE', kind='data', line=1971)
W('30,2536', 0o64373, 'S22NXTWI', 'VLOAD*', 'MXV', kind='interp', line=1972)
W('30,2537', 0o02445, '', '', 'W +36D,1', 'B-19', kind='operand', line=1973)
W('30,2540', 0o03502, '', '', 'S22UMRL', 'B-3', kind='operand', line=1974)
W('30,2541', 0o77732, '', 'VSL3', kind='interp', line=1975)
W('30,2542', 0o06621, '', 'STORE', 'W +144D,1', 'W(I+18)= UW(I) B-19', kind='interp', line=1976)
W('30,2543', 0o71300, '', 'TIX,1', 'DLOAD', kind='interp', line=1977)
W('30,2544', 0o60536, '', '', 'S22NXTWI', kind='operand', line=1978)
# Page 602
W('30,2545', 0o00041, '', '', 'S22RHO', 'B-28,B-30', kind='operand', line=1980)
W('30,2546', 0o60414, '', 'BOFF', 'SR2', 'MAKE RHO B-30', kind='interp', line=1981)
W('30,2547', 0o04343, '', '', 'CMOONFLG', kind='operand', line=1982)
W('30,2550', 0o60551, '', '', '+1', kind='operand', line=1983)
W('30,2551', 0o57101, '', 'NORM', 'XAD,2', kind='interp', line=1984)
W('30,2552', 0o00050, '', '', 'X2', kind='operand', line=1985)
W('30,2553', 0o00047, '', '', 'X2', kind='operand', line=1986)
W('30,2554', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=1987)
W('30,2555', 0o21636, '', '', 'SCTVAR', 'B+16', kind='operand', line=1988)
W('30,2556', 0o77742, '', 'SR1', '', 'ACCOUNTS FOR 1/2 IN NEXT FORMULA', kind='interp', line=1989)
W('30,2557', 0o00041, '', 'STORE', 'S22RHO', '1/2(RHO SQ)(VARSCT)', kind='interp', line=1990)
W('30,2560', 0o77770, '', 'AXT,1', kind='interp', line=1991)
W('30,2561', 0o00022, '', 'DEC', '18', 'S1 STILL 6 FROM ABOVE', kind='data', line=1992)
W('30,2562', 0o64373, 'S22NXXA', 'VLOAD*', 'MXV', kind='interp', line=1993)
W('30,2563', 0o03524, '', '', 'S22UMRL +18D,1', 'B-3', kind='operand', line=1994)
W('30,2564', 0o03502, '', '', 'S22UMRL', 'B-3', kind='operand', line=1995)
W('30,2565', 0o53761, '', 'VXSC', 'VSR*', kind='interp', line=1996)
W('30,2566', 0o00041, '', '', 'S22RHO', kind='operand', line=1997)
W('30,2567', 0o57212, '', '', '0 -12D,2', 'WITH VARRP SCALED B-28', kind='operand', line=1998)
W('30,2570', 0o05301, '', 'STORE', 'S22UUT +18D,1', '1/2(RHO SQ)(VARSCT)(U)(U T)', kind='interp', line=1999)
W('30,2571', 0o77300, '', 'TIX,1', 'VLOAD', kind='interp', line=2000)
W('30,2572', 0o60562, '', '', 'S22NXXA', kind='operand', line=2001)
W('30,2573', 0o01235, '', '', 'UM', kind='operand', line=2002)
W('30,2574', 0o34023, '', 'STCALL', 'S223X1', 'UM ALSO IN MPAC FOR S2231X13 SUBR.', kind='interp', line=2003)
W('30,2575', 0o62332, '', '', 'S2231X13', '(UM)(UM T) B-2 IN S22UMRL,P17D', kind='operand', line=2004)
W('30,2576', 0o50545, '', 'DLOAD', 'SR3', kind='interp', line=2005)
W('30,2577', 0o02241, '', '', 'ERADM', 'B0 B-29', kind='operand', line=2006)
W('30,2600', 0o63471, '', 'DDV', 'DSQ', kind='interp', line=2007)
W('30,2601', 0o00037, '', '', 'S22D', 'B-29', kind='operand', line=2008)
W('30,2602', 0o77605, '', 'DMP', kind='interp', line=2009)
W('30,2603', 0o02010, '', '', 'RPVAR', '***** METERS SQ', kind='operand', line=2010)
W('30,2604', 0o00041, '', 'STORE', 'S22RHO', 'TEMP (VARRP)(R0/D)', kind='interp', line=2011)
W('30,2605', 0o77770, '', 'AXT,1', kind='interp', line=2012)
W('30,2606', 0o00022, '', 'DEC', '18', 'S1 STILL 6 FROM ABOVE', kind='data', line=2013)
W('30,2607', 0o74373, 'S22NXXB', 'VLOAD*', 'VXSC', kind='interp', line=2014)
W('30,2610', 0o03524, '', '', 'S22UMRL +18D,1', '(UM)(UM T) B-2', kind='operand', line=2015)
W('30,2611', 0o00041, '', '', 'S22RHO', kind='operand', line=2016)
W('30,2612', 0o77653, '', 'VAD*', kind='interp', line=2017)
W('30,2613', 0o01301, '', '', 'S22UUT +18D,1', kind='operand', line=2018)
W('30,2614', 0o05301, '', 'STORE', 'S22UUT +18D,1', 'SMALL E MATRIX', kind='interp', line=2019)
W('30,2615', 0o77775, '', 'VLOAD', kind='interp', line=2020)
W('30,2616', 0o15335, '', '', 'ZEROVECS', kind='operand', line=2021)
W('30,2617', 0o06643, '', 'STORE', 'W +162D,1', 'CLEAR W8', kind='interp', line=2022)
W('30,2620', 0o40100, '', 'TIX,1', 'BOV', kind='interp', line=2023)
W('30,2621', 0o60607, '', '', 'S22NXXB', kind='operand', line=2024)
W('30,2622', 0o60623, '', '', '+1', kind='operand', line=2025)
W('30,2623', 0o50145, '', 'DLOAD', 'BMN', kind='interp', line=2026)
W('30,2624', 0o01277, '', '', 'S22UUT +16D', 'E5', kind='operand', line=2027)
W('30,2625', 0o60644, '', '', 'S22W76X', kind='operand', line=2028)
W('30,2626', 0o53166, '', 'SQRT', 'BZE', kind='interp', line=2029)
# Page 603
W('30,2627', 0o60644, '', '', 'S22W76X', kind='operand', line=2031)
W('30,2630', 0o16625, '', 'STODL', 'W +148D', 'W74= SQ ROOT E5', kind='interp', line=2032)
W('30,2631', 0o01275, '', '', 'S22UUT +14D', 'E4', kind='operand', line=2033)
W('30,2632', 0o40071, '', 'DDV', 'BOV', kind='interp', line=2034)
W('30,2633', 0o02625, '', '', 'W +148D', kind='operand', line=2035)
W('30,2634', 0o60636, '', '', 'S22W72X', kind='operand', line=2036)
W('30,2635', 0o02623, '', 'STORE', 'W +146D', 'W73= E4/W74', kind='interp', line=2037)
W('30,2636', 0o56345, 'S22W72X', 'DLOAD', 'DDV', kind='interp', line=2038)
W('30,2637', 0o01273, '', '', 'S22UUT +12D', 'E3', kind='operand', line=2039)
W('30,2640', 0o02625, '', '', 'W +148D', kind='operand', line=2040)
W('30,2641', 0o77600, '', 'BOV', kind='interp', line=2041)
W('30,2642', 0o60644, '', '', 'S22W76X', kind='operand', line=2042)
W('30,2643', 0o02621, '', 'STORE', 'W +144D', 'W72= E4/W74', kind='interp', line=2043)
W('30,2644', 0o63545, 'S22W76X', 'DLOAD', 'DSQ', kind='interp', line=2044)
W('30,2645', 0o02623, '', '', 'W +146D', 'W73', kind='operand', line=2045)
W('30,2646', 0o50021, '', 'BDSU', 'BMN', kind='interp', line=2046)
W('30,2647', 0o01267, '', '', 'S22UUT +8D', 'E2', kind='operand', line=2047)
W('30,2650', 0o60664, '', '', 'S22W78X', kind='operand', line=2048)
W('30,2651', 0o53166, '', 'SQRT', 'BZE', kind='interp', line=2049)
W('30,2652', 0o60664, '', '', 'S22W78X', kind='operand', line=2050)
W('30,2653', 0o16631, '', 'STODL', 'W +152D', 'W76= SQ ROOT (E2-W73 SQ)', kind='interp', line=2051)
W('30,2654', 0o02621, '', '', 'W +144D', 'W72', kind='operand', line=2052)
W('30,2655', 0o44205, '', 'DMP', 'BDSU', kind='interp', line=2053)
W('30,2656', 0o02623, '', '', 'W +146D', 'W73', kind='operand', line=2054)
W('30,2657', 0o01265, '', '', 'S22UUT +6D', 'E1', kind='operand', line=2055)
W('30,2660', 0o40071, '', 'DDV', 'BOV', kind='interp', line=2056)
W('30,2661', 0o02631, '', '', 'W +152D', 'W76', kind='operand', line=2057)
W('30,2662', 0o60664, '', '', 'S22W78X', kind='operand', line=2058)
W('30,2663', 0o02627, '', 'STORE', 'W +150D', 'W75= (E1-W72W73)/W76', kind='interp', line=2059)
W('30,2664', 0o63545, 'S22W78X', 'DLOAD', 'DSQ', kind='interp', line=2060)
W('30,2665', 0o02627, '', '', 'W +150D', kind='operand', line=2061)
W('30,2666', 0o63525, '', 'PDDL', 'DSQ', kind='interp', line=2062)
W('30,2667', 0o02621, '', '', 'W +144D', 'W72', kind='operand', line=2063)
W('30,2670', 0o77615, '', 'DAD', kind='interp', line=2064)
W('30,2671', 0o50021, '', 'BDSU', 'BMN', kind='interp', line=2065)
W('30,2672', 0o01257, '', '', 'S22UUT', 'E0', kind='operand', line=2066)
W('30,2673', 0o60676, '', '', 'S22SCLW', kind='operand', line=2067)
W('30,2674', 0o77766, '', 'SQRT', kind='interp', line=2068)
W('30,2675', 0o02635, '', 'STORE', 'W +156D', 'W78= SQ RT(E0-W72 SQ-W75 SQ)', kind='interp', line=2069)
W('30,2676', 0o74575, 'S22SCLW', 'VLOAD', 'VSR1', 'SCALE W6 METERS B-19', kind='interp', line=2070)
W('30,2677', 0o02621, '', '', 'W +144D', kind='operand', line=2071)
W('30,2700', 0o26621, '', 'STOVL', 'W +144D', kind='interp', line=2072)
W('30,2701', 0o02627, '', '', 'W +150D', kind='operand', line=2073)
W('30,2702', 0o77762, '', 'VSR1', kind='interp', line=2074)
W('30,2703', 0o26627, '', 'STOVL', 'W +150D', kind='interp', line=2075)
W('30,2704', 0o02635, '', '', 'W +156D', kind='operand', line=2076)
W('30,2705', 0o77762, '', 'VSR1', kind='interp', line=2077)
W('30,2706', 0o02635, '', 'STORE', 'W +156D', kind='interp', line=2078)
W('30,2707', 0o77624, 'S22SAVET', 'CALL', kind='interp', line=2079)
W('30,2710', 0o62351, '', '', 'GETTF', kind='operand', line=2080)
# Page 604
W('30,2711', 0o03672, '', 'STORE', 'S22TPRIM', 'SAVE PRESENT TIME FOR PIOS', kind='interp', line=2082)
W('30,2712', 0o77776, 'S22I=N', 'EXIT', '', 'TEST I=N', kind='interp', line=2083)
W('30,2713', 0o05412, '', 'TC', 'PHASCHNG', line=2084)
W('30,2714', 0o04022, '', 'OCT', '04022', kind='data', line=2085)
W('30,2715', 0o41746, '', 'CS', '8KK', line=2086)
W('30,2716', 0o61747, '', 'AD', '8NN', line=2087)
W('30,2717', 0o00006, '', 'EXTEND', line=2088)
W('30,2720', 0o63161, '', 'BZMF', 'S22F244X', 'EXIT TO FIGURE 2.4-4', line=2089)
W('30,2721', 0o31746, '', 'CA', '8KK', 'I=I+1', line=2090)
W('30,2722', 0o65017, '', 'AD', 'ONE', line=2091)
W('30,2723', 0o55300, '', 'TS', 'TEMPOR1', line=2092)
W('30,2724', 0o31750, '', 'CA', 'S22LOC', 'ADD 7 TO LOC TO GET ADDR. OF NEXT MARK', line=2093)
W('30,2725', 0o65023, '', 'AD', 'SEVEN', line=2094)
W('30,2726', 0o55301, '', 'TS', 'TEMPOR1 +1', line=2095)
W('30,2727', 0o05412, '', 'TC', 'PHASCHNG', line=2096)
W('30,2730', 0o04022, '', 'OCT', '04022', kind='data', line=2097)
W('30,2731', 0o31300, '', 'CA', 'TEMPOR1', line=2098)
W('30,2732', 0o55746, '', 'TS', '8KK', line=2099)
W('30,2733', 0o31301, '', 'CA', 'TEMPOR1 +1', line=2100)
W('30,2734', 0o55750, '', 'TS', 'S22LOC', line=2101)
W('30,2735', 0o06006, '', 'TC', 'INTPRET', line=2102)
W('30,2736', 0o77624, '', 'CALL', '', 'FOR ALL INTEGRATIONS OTHER THAN FIRST', kind='interp', line=2103)
W('30,2737', 0o27442, 'S2INTS1', '', 'INTSTALL', kind='operand', line=2104)
W('30,2740', 0o77624, '', 'CALL', kind='interp', line=2105)
W('30,2741', 0o62355, '', '', 'S22FLGS', kind='operand', line=2106)
W('30,2742', 0o43014, '', 'BON', 'CLEAR', kind='interp', line=2107)
W('30,2743', 0o02706, '', '', 'DMENFLG', kind='operand', line=2108)
W('30,2744', 0o60416, '', '', 'S22NXTIN', 'RETURN ALWAYS EXCEPT OFFSET POINT MARK 1', kind='operand', line=2109)
W('30,2745', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=2110)
W('30,2746', 0o43014, '', 'BOFF', 'SET', kind='interp', line=2111)
W('30,2747', 0o01751, '', '', 'ORBWFLAG', kind='operand', line=2112)
W('30,2750', 0o60416, '', '', 'S22NXTIN', 'OFFSET POINT MARK 1, NO W INTEGRATION', kind='operand', line=2113)
W('30,2751', 0o01476, '', '', 'DIM0FLAG', kind='operand', line=2114)
W('30,2752', 0o77614, '', 'CLRGO', kind='interp', line=2115)
W('30,2753', 0o01635, '', '', 'D6OR9FLG', kind='operand', line=2116)
W('30,2754', 0o60416, '', '', 'S22NXTIN', 'OFFSET POINT MARK 1, INTEGRATE W 6X6', kind='operand', line=2117)
W('30,2755', 0o77624, 'S22OFF=I', 'CALL', kind='interp', line=2118)
W('30,2756', 0o62351, '', '', 'GETTF', kind='operand', line=2119)
W('30,2757', 0o27670, '', 'STOVL', 'S22TOFF', 'TIME SUB OFF', kind='interp', line=2120)
W('30,2760', 0o01235, '', '', 'UM', kind='operand', line=2121)
W('30,2761', 0o35215, '', 'STCALL', 'S22UOFF', 'U SUB OFF', kind='interp', line=2122)
W('30,2762', 0o60712, '', '', 'S22I=N', 'TEST I=N', kind='operand', line=2123)
W('30,2763', 0o77775, 'S22D=9', 'VLOAD', '', 'D=9 PATH', kind='interp', line=2124)
W('30,2764', 0o01701, '', '', 'X789', kind='operand', line=2125)
W('30,2765', 0o14001, '', 'STODL', '0D', 'CALL PIOS TWICE TO TRANSFORM RL TO TIME', kind='interp', line=2126)
W('30,2766', 0o03672, '', '', 'S22TPRIM', 'T(SUB F) FROM TIME T PRIME', kind='operand', line=2127)
W('30,2767', 0o00007, '', 'STORE', '6D', kind='interp', line=2128)
W('30,2770', 0o45135, '', 'SLOAD', 'CALL', kind='interp', line=2129)
W('30,2771', 0o03674, '', '', 'S22EORM', '0=EARTH, NON-ZERO=MOON', kind='operand', line=2130)
W('30,2772', 0o55371, 'S2RTRP', '', 'R-TO-RP', kind='operand', line=2131)
# Page 605
W('30,2773', 0o45006, '', 'PUSH', 'CALL', 'R-TO-RP LEAVES PUSHLOC AT 0', kind='interp', line=2133)
W('30,2774', 0o62351, '', '', 'GETTF', kind='operand', line=2134)
W('30,2775', 0o00007, '', 'STORE', '6D', kind='interp', line=2135)
W('30,2776', 0o45135, '', 'SLOAD', 'CALL', kind='interp', line=2136)
W('30,2777', 0o03674, '', '', 'S22EORM', kind='operand', line=2137)
W('30,3000', 0o55344, 'S2RPTR', '', 'RP-TO-R', kind='operand', line=2138)
W('30,3001', 0o01701, 'S22BOX32', 'STORE', 'X789', kind='interp', line=2139)
W('30,3002', 0o40014, '', 'SET', 'BOV', kind='interp', line=2140)
W('30,3003', 0o02464, '', '', 'INCORFLG', 'FLAG=1', kind='operand', line=2141)
W('30,3004', 0o61005, '', '', '+1', 'CLEAR OVERFLOW', kind='operand', line=2142)
W('30,3005', 0o77651, '', 'VSU', kind='interp', line=2143)
W('30,3006', 0o01207, '', '', 'CSMPOS', kind='operand', line=2144)
W('30,3007', 0o03531, '', 'STORE', 'RCLP', 'RCL=RL-RC', kind='interp', line=2145)
W('30,3010', 0o47256, '', 'UNIT', 'VXV', 'USTAR=UNIT(UNIT(RCL)XUM)', kind='interp', line=2146)
W('30,3011', 0o01235, '', '', 'UM', kind='operand', line=2147)
W('30,3012', 0o40056, '', 'UNIT', 'BOV', kind='interp', line=2148)
W('30,3013', 0o60707, '', '', 'S22SAVET', 'COMPUTATION OVERFLOW, SAVE TF', kind='operand', line=2149)
W('30,3014', 0o01245, '', 'STORE', 'USTAR', kind='interp', line=2150)
W('30,3015', 0o43014, 'S22BOX12', 'SET', 'SET', kind='interp', line=2151)
W('30,3016', 0o02466, '', '', 'DMENFLG', '=1 FOR 9X9 W', kind='operand', line=2152)
W('30,3017', 0o00467, '', '', 'VEHUPFLG', '=1 FOR CSM', kind='operand', line=2153)
W('30,3020', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=2154)
W('30,3021', 0o21636, '', '', 'SCTVAR', 'B+18', kind='operand', line=2155)
W('30,3022', 0o21640, '', '', 'IMUVARR', 'B+18', kind='operand', line=2156)
W('30,3023', 0o27526, '', 'STOVL', 'VARIANCE', kind='interp', line=2157)
W('30,3024', 0o03531, '', '', 'RCLP', 'B-29 OR B-27', kind='operand', line=2158)
W('30,3025', 0o60246, '', 'ABVAL', 'NORM', kind='interp', line=2159)
W('30,3026', 0o00047, '', '', 'X1', kind='operand', line=2160)
W('30,3027', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=2161)
W('30,3030', 0o03526, '', '', 'VARIANCE', kind='operand', line=2162)
W('30,3031', 0o56070, '', 'XAD,1', 'XAD,1', kind='interp', line=2163)
W('30,3032', 0o00046, '', '', 'X1', 'DOUBLE NORM SHIFT SINCE RCLP WAS SQUARED', kind='operand', line=2164)
W('30,3033', 0o03673, '', '', 'S22EORM', 'DOUBLE EARTH OR MOON SHIFT, SAME REASON', kind='operand', line=2165)
W('30,3034', 0o53670, '', 'XAD,1', 'SR*', kind='interp', line=2166)
W('30,3035', 0o03673, '', '', 'S22EORM', kind='operand', line=2167)
W('30,3036', 0o20601, '', '', '0,1', 'SCALE VARIANCE B-40 FOR BOTH EARTH, MOON', kind='operand', line=2168)
W('30,3037', 0o77751, '', 'TLOAD', '', 'CHANGE MODE TO TRIPLE', kind='interp', line=2169)
W('30,3040', 0o00155, '', '', 'MPAC', kind='operand', line=2170)
W('30,3041', 0o37526, '', 'STCALL', 'VARIANCE', 'CALC B0,B1,DELTAQ, NEW USTAR', kind='interp', line=2171)
W('30,3042', 0o47043, 'S2BVTRS', '', 'BVECTORS', kind='operand', line=2172)
W('30,3043', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=2173)
W('30,3044', 0o03502, '', '', 'BVECTOR', kind='operand', line=2174)
W('30,3045', 0o37516, '', 'STCALL', 'BVECTOR +12D', 'B2=-B0', kind='interp', line=2175)
W('30,3046', 0o75254, 'S2INCP1', '', 'INCORP1', kind='operand', line=2176)
W('30,3047', 0o77624, '', 'CALL', kind='interp', line=2177)
W('30,3050', 0o56750, '', '', 'GRP2PC', kind='operand', line=2178)
W('30,3051', 0o43014, '', 'BOFF', 'CLEAR', kind='interp', line=2179)
W('30,3052', 0o01342, '', '', '22DSPFLG', '=1 DISPLAY DELTA R,V    =0 DO NOT', kind='operand', line=2180)
W('30,3053', 0o61104, '', '', 'S22BOX42', kind='operand', line=2181)
W('30,3054', 0o01262, '', '', '22DSPFLG', kind='operand', line=2182)
# Page 606
W('30,3055', 0o77624, '', 'CALL', kind='interp', line=2184)
W('30,3056', 0o56750, '', '', 'GRP2PC', kind='operand', line=2185)
W('30,3057', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=2186)
W('30,3060', 0o01257, '', '', 'DELTAX', 'DELTA R', kind='operand', line=2187)
W('30,3061', 0o53750, '', 'LXA,1', 'SR*', kind='interp', line=2188)
W('30,3062', 0o03673, '', '', 'S22EORM', 'SCALE DELTA R ALWAYS METERS B-29', kind='operand', line=2189)
W('30,3063', 0o20601, '', '', '0,1', kind='operand', line=2190)
W('30,3064', 0o27502, '', 'STOVL', 'N49DISP', kind='interp', line=2191)
W('30,3065', 0o01265, '', '', 'DELTAX +6', 'DELTA V', kind='operand', line=2192)
W('30,3066', 0o53646, '', 'ABVAL', 'SR*', 'DELTA V=METERS/CSEC B-7 ALWAYS', kind='interp', line=2193)
W('30,3067', 0o20601, '', '', '0,1', kind='operand', line=2194)
W('30,3070', 0o03504, '', 'STORE', 'N49DISP +2', kind='interp', line=2195)
W('30,3071', 0o77776, '', 'EXIT', kind='interp', line=2196)
W('30,3072', 0o33643, '', 'CAF', 'V06N49EE', line=2197)
W('30,3073', 0o04662, '', 'TC', 'BANKCALL', line=2198)
W('30,3074', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=2199)
W('30,3075', 0o04106, '', 'TC', 'GOTOPOOH', 'V34E TERMINATE', line=2200)
W('30,3076', 0o03103, '', 'TC', '+5', 'INCORPORATE CHANGES', line=2201)
W('30,3077', 0o03267, '', 'TC', 'S22EXEX', 'V32E RECYCLE', line=2202)
W('30,3100', 0o35015, '', 'CAF', 'BIT3', line=2203)
W('30,3101', 0o05526, '', 'TC', 'BLANKET', line=2204)
W('30,3102', 0o05217, '', 'TC', 'ENDOFJOB', line=2205)
W('30,3103', 0o06006, '', 'TC', 'INTPRET', line=2206)
W('30,3104', 0o77624, 'S22BOX42', 'CALL', kind='interp', line=2207)
W('30,3105', 0o75466, '', '', 'INCORP2', kind='operand', line=2208)
W('30,3106', 0o77624, '', 'CALL', '', 'CSMPOS=RC B-29 OR B-27', kind='interp', line=2209)
W('30,3107', 0o61332, '', '', 'S22CALRC', kind='operand', line=2210)
W('30,3110', 0o45014, 'DMPINCP2', 'BOFF', 'CALL', kind='interp', line=2211)
W('30,3111', 0o02744, '', '', 'INCORFLG', kind='operand', line=2212)
W('30,3112', 0o60707, '', '', 'S22SAVET', 'SAVE TF AND TEST I=N', kind='operand', line=2213)
W('30,3113', 0o56750, '', '', 'GRP2PC', kind='operand', line=2214)
W('30,3114', 0o77214, '', 'CLEAR', 'VLOAD', kind='interp', line=2215)
W('30,3115', 0o02664, '', '', 'INCORFLG', 'FLAG=0', kind='operand', line=2216)
W('30,3116', 0o01701, '', '', 'X789', kind='operand', line=2217)
W('30,3117', 0o77651, '', 'VSU', kind='interp', line=2218)
W('30,3120', 0o01207, '', '', 'CSMPOS', kind='operand', line=2219)
W('30,3121', 0o37531, '', 'STCALL', 'RCLP', 'RCL=RL-RC', kind='interp', line=2220)
W('30,3122', 0o61015, '', '', 'S22BOX12', kind='operand', line=2221)
W('30,3123', 0o66370, 'S22BOX22', 'AXT,1', 'SSP', 'CLEAR W6,W7,W8.  (27 ELEMENTS 54 REGS)', kind='interp', line=2222)
W('30,3124', 0o00066, '', 'DEC', '54', kind='data', line=2223)
W('30,3125', 0o00051, '', '', 'S1', kind='operand', line=2224)
W('30,3126', 0o00006, '', 'DEC', '6', kind='data', line=2225)
W('30,3127', 0o77775, '', 'VLOAD', kind='interp', line=2226)
W('30,3130', 0o15335, '', '', 'ZEROVECS', kind='operand', line=2227)
W('30,3131', 0o06643, 'CLRW678', 'STORE', 'W +162D,1', kind='interp', line=2228)
W('30,3132', 0o67300, '', 'TIX,1', 'SLOAD', kind='interp', line=2229)
W('30,3133', 0o61131, '', '', 'CLRW678', kind='operand', line=2230)
W('30,3134', 0o02007, '', '', 'S22WSUBL', kind='operand', line=2231)
W('30,3135', 0o02621, '', 'STORE', 'W +144D', kind='interp', line=2232)
W('30,3136', 0o02631, '', 'STORE', 'W +152D', kind='interp', line=2233)
# Page 607
W('30,3137', 0o02641, '', 'STORE', 'W +160D', kind='interp', line=2235)
W('30,3140', 0o43014, '', 'CLEAR', 'BOFF', 'SET LUNAFLAG, TIME FOR LALOTORV', kind='interp', line=2236)
W('30,3141', 0o01663, '', '', 'LUNAFLAG', 'ERADFLAG,LAT,LONG,ALT SET PREVIOUSLY', kind='operand', line=2237)
W('30,3142', 0o04343, '', '', 'CMOONFLG', 'CHECK SCALING OF ITEMS,ALT INPUT AND', kind='operand', line=2238)
W('30,3143', 0o61146, '', '', 'S22BX22A', 'RL OUTPUT IN ALPHAV BOTH B-29', kind='operand', line=2239)
W('30,3144', 0o77614, '', 'SET', kind='interp', line=2240)
W('30,3145', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=2241)
W('30,3146', 0o77624, 'S22BX22A', 'CALL', kind='interp', line=2242)
W('30,3147', 0o62351, '', '', 'GETTF', kind='operand', line=2243)
W('30,3150', 0o77624, '', 'CALL', '', 'COMPUTE RL', kind='interp', line=2244)
W('30,3151', 0o26441, '', '', 'LALOTORV', kind='operand', line=2245)
W('30,3152', 0o43175, '', 'VLOAD', 'BOFF', kind='interp', line=2246)
W('30,3153', 0o02152, '', '', 'ALPHAV', 'RL B-29', kind='operand', line=2247)
W('30,3154', 0o04343, '', '', 'CMOONFLG', kind='operand', line=2248)
W('30,3155', 0o61157, '', '', 'S22BX22B', kind='operand', line=2249)
W('30,3156', 0o77752, '', 'VSL2', '', 'SCALE RL B-27 FOR MOON', kind='interp', line=2250)
W('30,3157', 0o77650, 'S22BX22B', 'GOTO', kind='interp', line=2251)
W('30,3160', 0o61001, '', '', 'S22BOX32', kind='operand', line=2252)
W('30,3161', 0o06006, 'S22F244X', 'TC', 'INTPRET', line=2253)
W('30,3162', 0o46135, 'S22F244', 'SLOAD', 'BHIZ', 'FIG 2.4-4     TEST OFF=0', kind='interp', line=2254)
W('30,3163', 0o02746, '', '', 'CXOFF', kind='operand', line=2255)
W('30,3164', 0o61220, '', '', 'S22BOX44', kind='operand', line=2256)
W('30,3165', 0o77661, '', 'SR', '', 'SCALE OFFSET B-14 THEN GET GR. 8NN', kind='interp', line=2257)
W('30,3166', 0o20612, '', '', '9D', kind='operand', line=2258)
W('30,3167', 0o02152, '', 'STORE', 'ALPHAV', 'TEMP', kind='interp', line=2259)
W('30,3170', 0o45335, '', 'SLOAD', 'DSU', kind='interp', line=2260)
W('30,3171', 0o02750, '', '', '8NN', kind='operand', line=2261)
W('30,3172', 0o02152, '', '', 'ALPHAV', kind='operand', line=2262)
W('30,3173', 0o45040, '', 'BMN', 'CALL', 'OFFSET GR. NO. MARKS.  FORGET IT', kind='interp', line=2263)
W('30,3174', 0o61220, '', '', 'S22BOX44', kind='operand', line=2264)
W('30,3175', 0o56750, '', '', 'GRP2PC', 'GROUP 2 PHASE CHANGE', kind='operand', line=2265)
W('30,3176', 0o77745, '', 'DLOAD', kind='interp', line=2266)
W('30,3177', 0o03670, '', '', 'S22TOFF', kind='operand', line=2267)
W('30,3200', 0o34041, '', 'STCALL', 'TDEC1', 'CALC RC AT OFFSET TIME', kind='interp', line=2268)
W('30,3201', 0o27071, '', '', 'CSMPREC', kind='operand', line=2269)
W('30,3202', 0o77775, '', 'VLOAD', kind='interp', line=2270)
W('30,3203', 0o00017, '', '', 'RATT1', 'RC METERS B-29 OR B-27', kind='operand', line=2271)
W('30,3204', 0o25207, '', 'STOVL', 'CSMPOS', kind='interp', line=2272)
W('30,3205', 0o01215, '', '', 'S22UOFF', kind='operand', line=2273)
W('30,3206', 0o25235, '', 'STOVL', 'UM', 'U=UOFF', kind='interp', line=2274)
W('30,3207', 0o01701, '', '', 'X789', kind='operand', line=2275)
W('30,3210', 0o43046, '', 'ABVAL', 'BOFF', kind='interp', line=2276)
W('30,3211', 0o04343, '', '', 'CMOONFLG', kind='operand', line=2277)
W('30,3212', 0o61214, '', '', '+2', kind='operand', line=2278)
W('30,3213', 0o77702, '', 'SR2', '', 'SCALE MOON R0 B-29 FOR S22F2410 SUBR', kind='interp', line=2279)
W('30,3214', 0o36241, '', 'STCALL', 'ERADM', kind='interp', line=2280)
W('30,3215', 0o61277, '', '', 'S22F2410', kind='operand', line=2281)
W('30,3216', 0o77650, '', 'GOTO', kind='interp', line=2282)
W('30,3217', 0o61223, '', '', 'S22BX44A', kind='operand', line=2283)
W('30,3220', 0o77624, 'S22BOX44', 'CALL', kind='interp', line=2284)
# Page 608
W('30,3221', 0o62351, '', '', 'GETTF', kind='operand', line=2286)
W('30,3222', 0o03670, '', 'STORE', 'S22TOFF', 'PRESENT TIME FOR LAT-LONG SETUP', kind='interp', line=2287)
W('30,3223', 0o77214, 'S22BX44A', 'CLEAR', 'VLOAD', kind='interp', line=2288)
W('30,3224', 0o01663, '', '', 'LUNAFLAG', kind='operand', line=2289)
W('30,3225', 0o01701, '', '', 'X789', kind='operand', line=2290)
W('30,3226', 0o43014, '', 'BOFF', 'SET', kind='interp', line=2291)
W('30,3227', 0o04343, '', '', 'CMOONFLG', kind='operand', line=2292)
W('30,3230', 0o61233, '', '', 'S22BX44B', kind='operand', line=2293)
W('30,3231', 0o01463, '', '', 'LUNAFLAG', 'SET = 1 FOR LAT-LONG', kind='operand', line=2294)
W('30,3232', 0o77742, '', 'VSR2', '', 'SCALE RL MOON B-29 FOR LAT-LONG', kind='interp', line=2295)
W('30,3233', 0o16152, 'S22BX44B', 'STODL', 'ALPHAV', 'RL SCALED B-29 FOR LAT-LONG', kind='interp', line=2296)
W('30,3234', 0o03670, '', '', 'S22TOFF', 'EITHER PRESENT OR OFFSET TIME', kind='operand', line=2297)
W('30,3235', 0o77624, '', 'CALL', kind='interp', line=2298)
W('30,3236', 0o26370, '', '', 'LAT-LONG', '**** ALT OUTPUT ALWAYS B-29', kind='operand', line=2299)
W('30,3237', 0o77624, '', 'CALL', '', 'DISPLAY LAT/LONG/ALT', kind='interp', line=2300)
W('30,3240', 0o62365, '', '', 'LLASRD', kind='operand', line=2301)
W('30,3241', 0o77776, '', 'EXIT', kind='interp', line=2302)
W('30,3242', 0o33644, '', 'CAF', 'V06N89B', line=2303)
W('30,3243', 0o04662, '', 'TC', 'BANKCALL', line=2304)
W('30,3244', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=2305)
W('30,3245', 0o03272, '', 'TC', 'S22GTP', 'V34E TERMINATE', line=2306)
W('30,3246', 0o03250, '', 'TC', '+2', 'PROCEED       SAVE LANDING SITE COORD', line=2307)
W('30,3247', 0o03263, '', 'TC', 'S22.981X', 'RECYCLE       POINT A IN GSOP', line=2308)
W('30,3250', 0o06006, '', 'TC', 'INTPRET', line=2309)
W('30,3251', 0o77745, '', 'DLOAD', kind='interp', line=2310)
W('30,3252', 0o03670, '', '', 'S22TOFF', 'EITHER PRESENT OR OFFSET TIME', kind='operand', line=2311)
W('30,3253', 0o24007, '', 'STOVL', '6D', '6-7D= LANDING SITE TIME FOR R-TO-RP', kind='interp', line=2312)
W('30,3254', 0o01701, '', '', 'X789', kind='operand', line=2313)
W('30,3255', 0o00001, '', 'STORE', '0D', '0-5D= LANDING SITE VEC FOR R-TO-RP', kind='interp', line=2314)
W('30,3256', 0o45135, '', 'SLOAD', 'CALL', kind='interp', line=2315)
W('30,3257', 0o15333, '', '', 'HIDPHALF', 'ANY NON-ZERO FOR MOON', kind='operand', line=2316)
W('30,3260', 0o55371, '', '', 'R-TO-RP', 'CONVERT RLS TO MOON-FIXED COORD', kind='operand', line=2317)
W('30,3261', 0o02026, '', 'STORE', 'RLS', 'LANDING SITE VECTOR', kind='interp', line=2318)
W('30,3262', 0o77776, '', 'EXIT', kind='interp', line=2319)
W('30,3263', 0o06006, 'S22.981X', 'TC', 'INTPRET', line=2320)
W('30,3264', 0o77624, '', 'CALL', kind='interp', line=2321)
W('30,3265', 0o61342, '', '', '9DWTO6DW', kind='operand', line=2322)
W('30,3266', 0o77776, '', 'EXIT', '', 'GO TO POINT A IN CHAPTER 5', kind='interp', line=2323)
W('30,3267', 0o06006, 'S22EXEX', 'TC', 'INTPRET', 'WITHOUT CONVERTING W', line=2324)
W('30,3270', 0o77650, '', 'GOTO', kind='interp', line=2325)
W('30,3271', 0o03703, '', '', 'S22RTNEX', kind='operand', line=2326)

W('30,3272', 0o06006, 'S22GTP', 'TC', 'INTPRET', 'CONVERT W BEFORE TC GOTOPOOH', line=2328)
W('30,3273', 0o77624, '', 'CALL', kind='interp', line=2329)
W('30,3274', 0o61342, '', '', '9DWTO6DW', kind='operand', line=2330)
W('30,3275', 0o77776, '', 'EXIT', kind='interp', line=2331)
W('30,3276', 0o04106, '', 'TC', 'GOTOPOOH', line=2332)
W('30,3277', 0o77201, 'S22F2410', 'SETPD', 'VLOAD', 'COMPUTE FORMULA 2.4.10', kind='interp', line=2333)
W('30,3300', 0o00001, '', '', '0D', kind='operand', line=2334)
W('30,3301', 0o01207, '', '', 'CSMPOS', 'RC B-29 EARTH, B-27 MOON', kind='operand', line=2335)
# Page 609
W('30,3302', 0o50256, '', 'UNIT', 'DOT', 'UNIT ALSO SETS 36D=ABVAL(RC) USED BELOW', kind='interp', line=2337)
W('30,3303', 0o01235, '', '', 'UM', kind='operand', line=2338)
W('30,3304', 0o57552, '', 'SL1', 'DCOMP', 'GSOP CHANGE 8/18/67', kind='interp', line=2339)
W('30,3305', 0o77606, '', 'PUSH', '', 'PD 2D 8D=COSA=-(UM.RC)/ABVAL(RC)      B-1', kind='interp', line=2340)
W('30,3306', 0o44316, '', 'DSQ', 'BDSU', kind='interp', line=2341)
W('30,3307', 0o21642, '', '', 'DEC1B2', kind='operand', line=2342)
W('30,3310', 0o43125, '', 'PDDL', 'BOFF', 'PD 4D 2D=1-COSA SQ=SINA SQ            B-2', kind='interp', line=2343)
W('30,3311', 0o02241, '', '', 'ERADM', 'R0 ALWAYS B-29 FROM SETRE', kind='operand', line=2344)
W('30,3312', 0o04343, '', '', 'CMOONFLG', kind='operand', line=2345)
W('30,3313', 0o61315, '', '', '+2', kind='operand', line=2346)
W('30,3314', 0o77712, '', 'SL2', '', 'SCALE R0 B-27 FOR MOON', kind='interp', line=2347)
W('30,3315', 0o56362, '', 'SR1R', 'DDV', '(R0/RC)       B-1', kind='interp', line=2348)
W('30,3316', 0o00045, '', '', '36D', kind='operand', line=2349)
W('30,3317', 0o45316, '', 'DSQ', 'DSU', 'PD 2D (RP/RC) SQ - SINA SQ            B-2', kind='interp', line=2350)
W('30,3320', 0o44366, '', 'SQRT', 'BDSU', 'PD 0D COSA-SQRT((R0/RC)SQ-SINA SQ)    B-1', kind='interp', line=2351)
W('30,3321', 0o77605, '', 'DMP', '', 'DMP RESULT B-28 MOON, B-30 EARTH', kind='interp', line=2352)
W('30,3322', 0o00045, '', '', '36D', 'VXSC RESULT B-29 MOON, B-31 EARTH', kind='operand', line=2353)
W('30,3323', 0o00041, '', 'STORE', 'S22RHO', 'RHO FOR W INIT. OF UNKNOWN LMK B-28,B-30', kind='interp', line=2354)
W('30,3324', 0o77761, '', 'VXSC', kind='interp', line=2355)
W('30,3325', 0o01235, '', '', 'UM', kind='operand', line=2356)
W('30,3326', 0o53352, '', 'VSL2', 'VAD', 'SCALE B-27 MOON, B-29 EARTH AND ADD RC', kind='interp', line=2357)
W('30,3327', 0o01207, '', '', 'CSMPOS', kind='operand', line=2358)
W('30,3330', 0o01701, '', 'STORE', 'X789', kind='interp', line=2359)
W('30,3331', 0o77616, '', 'RVQ', '', 'B-27 FOR EARTH OR B-29 FOR MOON', kind='interp', line=2360)
W('30,3332', 0o77350, 'S22CALRC', 'LXA,1', 'VLOAD', 'COMPUTE RC B-29 OR B-27', kind='interp', line=2361)
W('30,3333', 0o03673, '', '', 'S22EORM', '=0 FOR EARTH, -2 FOR MOON', kind='operand', line=2362)
W('30,3334', 0o01573, '', '', 'DELTACSM', kind='operand', line=2363)
W('30,3335', 0o53257, '', 'VSR*', 'VAD', kind='interp', line=2364)
W('30,3336', 0o20610, '', '', '7,1', kind='operand', line=2365)
W('30,3337', 0o01607, '', '', 'RCVCSM', kind='operand', line=2366)
W('30,3340', 0o01207, '', 'STORE', 'CSMPOS', kind='interp', line=2367)
W('30,3341', 0o77616, '', 'RVQ', kind='interp', line=2368)
#   SETLOC P22S
#   BANK

W('31,2332', 0o00031, 'S2231X13', 'STORE', 'S221X3', 'MULT 3X1 BY 1X3, STORE RESULTING 3X3 IN', kind='interp', line=2372)
W('31,2333', 0o77131, '', 'SSP', 'AXT,2', 'S22UMRL - S22UMRL+17D', kind='interp', line=2373)
W('31,2334', 0o00052, '', '', 'S2', kind='operand', line=2374)
W('31,2335', 0o00002, '', 'DEC', '2', kind='data', line=2375)
W('31,2336', 0o00006, '', 'DEC', '6', kind='data', line=2376)
W('31,2337', 0o77770, '', 'AXT,1', kind='interp', line=2377)
W('31,2340', 0o00022, '', 'DEC', '18', kind='data', line=2378)
W('31,2341', 0o73775, 'S2231NXT', 'VLOAD', 'VXSC*', kind='interp', line=2379)
W('31,2342', 0o00031, '', '', 'S221X3', kind='operand', line=2380)
W('31,2343', 0o77746, '', '', 'S223X1 +6,2', kind='operand', line=2381)
W('31,2344', 0o07524, '', 'STORE', 'S22UMRL +18D,1', kind='interp', line=2382)
W('31,2345', 0o61110, '', 'INCR,1', 'TIX,2', kind='interp', line=2383)
W('31,2346', 0o77771, '', 'DEC', '-6', kind='data', line=2384)
W('31,2347', 0o62341, '', '', 'S2231NXT', kind='operand', line=2385)
W('31,2350', 0o77616, '', 'RVQ', kind='interp', line=2386)
# Page 610
W('31,2351', 0o70740, 'GETTF', 'LXC,1', 'DLOAD*', 'SET MPAC= TF', kind='interp', line=2388)
W('31,2352', 0o02750, '', '', 'S22LOC', kind='operand', line=2389)
W('31,2353', 0o00001, '', '', '0,1', kind='operand', line=2390)
W('31,2354', 0o77616, '', 'RVQ', kind='interp', line=2391)
W('31,2355', 0o43014, 'S22FLGS', 'SET', 'SET', 'INTEGRATION FLAGS', kind='interp', line=2392)
W('31,2356', 0o01476, '', '', 'DIM0FLAG', kind='operand', line=2393)
W('31,2357', 0o01475, '', '', 'D6OR9FLG', kind='operand', line=2394)
W('31,2360', 0o43014, '', 'SET', 'SET', kind='interp', line=2395)
W('31,2361', 0o01474, '', '', 'VINTFLAG', kind='operand', line=2396)
W('31,2362', 0o01472, '', '', 'STATEFLG', kind='operand', line=2397)
W('31,2363', 0o43414, '', 'CLEAR', 'RVQ', kind='interp', line=2398)
W('31,2364', 0o01673, '', '', 'INTYPFLG', kind='operand', line=2399)

# SUBROUTINE TO MODIFY ALT AND STORE LAT TO LAT+5 IN LANDLAT TO LANDLAT+5
# PRIOR TO DISPLAY.

W('31,2365', 0o77745, 'LLASRD', 'DLOAD', '', 'ALT, LANDALT METERS B-29', kind='interp', line=2404)
W('31,2366', 0o01110, '', '', 'ALT', kind='operand', line=2405)
W('31,2367', 0o16362, '', 'STODL', 'LANDALT', kind='interp', line=2406)
W('31,2370', 0o01106, '', '', 'LONG', kind='operand', line=2407)
W('31,2371', 0o77742, '', 'SR1', kind='interp', line=2408)
W('31,2372', 0o02360, '', 'STORE', 'LANDLONG', kind='interp', line=2409)
W('31,2373', 0o77616, '', 'RVQ', kind='interp', line=2410)

# SUBROUTINE TO MODIFY LANDALT AND STORE LANDALT TO LANDALT+5 IN LAT TO
# LAT+5 AFTER LMK DATA LOADED BY ASTRONAUT.

W('31,2374', 0o77745, 'LLASRDA', 'DLOAD', '', 'ALT, LANDALT METERS B-29', kind='interp', line=2415)
W('31,2375', 0o02362, '', '', 'LANDALT', kind='operand', line=2416)
W('31,2376', 0o15110, '', 'STODL', 'ALT', kind='interp', line=2417)
W('31,2377', 0o02360, '', '', 'LANDLONG', kind='operand', line=2418)
W('31,2400', 0o77752, '', 'SL1', kind='interp', line=2419)
W('31,2401', 0o01106, '', 'STORE', 'LONG', kind='interp', line=2420)
W('31,2402', 0o77616, '', 'RVQ', kind='interp', line=2421)
#   SETLOC P20S6
#   BANK

W('30,3342', 0o40220, '9DWTO6DW', 'STQ', 'SETPD', kind='interp', line=2425)
W('30,3343', 0o01214, '', '', '9DWXX', kind='operand', line=2426)
W('30,3344', 0o00001, '', '', '0D', kind='operand', line=2427)
W('30,3345', 0o41575, '', 'VLOAD', 'PUSH', 'CLEAR WORKING AREA OF PUSHLIST', kind='interp', line=2428)
W('30,3346', 0o15335, '', '', 'HI6ZEROS', 'INCLUDING P', kind='operand', line=2429)
W('30,3347', 0o41406, '', 'PUSH', 'PUSH', 'PD 18D', kind='interp', line=2430)
W('30,3350', 0o77731, '', 'SSP', kind='interp', line=2431)
W('30,3351', 0o00017, '', '', '9DWJ', 'J=29  USE 2*29 FOR DP WORDS', kind='operand', line=2432)
W('30,3352', 0o00072, '', 'DEC', '58', kind='data', line=2433)
W('30,3353', 0o66150, '9DWI=J', 'LXA,1', 'SXA,1', 'SET I=J', kind='interp', line=2434)
W('30,3354', 0o00016, '', '', '9DWJ', kind='operand', line=2435)
W('30,3355', 0o00012, '', '', '9DWI', kind='operand', line=2436)
W('30,3356', 0o77624, '9DWEPCAL', 'CALL', kind='interp', line=2437)
# Page 611
W('30,3357', 0o61574, '', '', 'ROWDOT', kind='operand', line=2439)
W('30,3360', 0o77750, '', 'LXA,1', '', 'P VARIES 0-20 INSTEAD OF 20-0', kind='interp', line=2440)
W('30,3361', 0o00010, '', '', '9DWP', kind='operand', line=2441)
W('30,3362', 0o06641, '', 'STORE', 'EMATRIX +40D,1', kind='interp', line=2442)
W('30,3363', 0o66110, '', 'INCR,1', 'SXA,1', kind='interp', line=2443)
W('30,3364', 0o00002, '', 'DEC', '2', kind='data', line=2444)
W('30,3365', 0o00010, '', '', '9DWP', kind='operand', line=2445)
W('30,3366', 0o46135, '', 'SLOAD', 'BHIZ', 'TEST I=0', kind='interp', line=2446)
W('30,3367', 0o00013, '', '', '9DWI', kind='operand', line=2447)
W('30,3370', 0o61405, '', '', '9DWTESTJ', kind='operand', line=2448)
W('30,3371', 0o77625, '', 'DSU', '', 'I=I-1', kind='interp', line=2449)
W('30,3372', 0o21634, '', '', '9DWID', kind='operand', line=2450)
W('30,3373', 0o00013, '', 'STORE', '9DWI', kind='interp', line=2451)
W('30,3374', 0o46025, '', 'DSU', 'BHIZ', 'TEST I=26', kind='interp', line=2452)
W('30,3375', 0o21632, '', '', '9DW26D', kind='operand', line=2453)
W('30,3376', 0o61401, '', '', '9DWSETI2', kind='operand', line=2454)
W('30,3377', 0o77650, '', 'GOTO', '', 'NEXT E SUB P', kind='interp', line=2455)
W('30,3400', 0o61356, '', '', '9DWEPCAL', kind='operand', line=2456)
W('30,3401', 0o52131, '9DWSETI2', 'SSP', 'GOTO', 'I=2', kind='interp', line=2457)
W('30,3402', 0o00013, '', '', '9DWI', kind='operand', line=2458)
W('30,3403', 0o00004, '', 'DEC', '4', kind='data', line=2459)
W('30,3404', 0o61356, '', '', '9DWEPCAL', kind='operand', line=2460)
W('30,3405', 0o46135, '9DWTESTJ', 'SLOAD', 'BHIZ', 'TEST J=0', kind='interp', line=2461)
W('30,3406', 0o00017, '', '', '9DWJ', kind='operand', line=2462)
W('30,3407', 0o61424, '', '', '9DWFIG6', kind='operand', line=2463)
W('30,3410', 0o77625, '', 'DSU', kind='interp', line=2464)
W('30,3411', 0o21634, '', '', '9DWID', kind='operand', line=2465)
W('30,3412', 0o00017, '', 'STORE', '9DWJ', 'J=J-1', kind='interp', line=2466)
W('30,3413', 0o46025, '', 'DSU', 'BHIZ', 'TEST J=26', kind='interp', line=2467)
W('30,3414', 0o21632, '', '', '9DW26D', kind='operand', line=2468)
W('30,3415', 0o61420, '', '', '9DWSETJ2', kind='operand', line=2469)
W('30,3416', 0o77650, '', 'GOTO', kind='interp', line=2470)
W('30,3417', 0o61353, '', '', '9DWI=J', kind='operand', line=2471)
W('30,3420', 0o52131, '9DWSETJ2', 'SSP', 'GOTO', 'SET J=2', kind='interp', line=2472)
W('30,3421', 0o00017, '', '', '9DWJ', kind='operand', line=2473)
W('30,3422', 0o00004, '', 'DEC', '4', kind='data', line=2474)
W('30,3423', 0o61353, '', '', '9DWI=J', kind='operand', line=2475)
W('30,3424', 0o77624, '9DWFIG6', 'CALL', kind='interp', line=2476)
W('30,3425', 0o56750, '', '', 'GRP2PC', kind='operand', line=2477)
W('30,3426', 0o77331, '', 'SSP', 'VLOAD', 'START OF FIGURE 2.4-6', kind='interp', line=2478)
W('30,3427', 0o00017, '', '', '9DWJ', 'J=29', kind='operand', line=2479)
W('30,3430', 0o00072, '', 'DEC', '58', kind='data', line=2480)
W('30,3431', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=2481)
W('30,3432', 0o00011, '', 'STORE', '9DWP', 'P,N,I=0', kind='interp', line=2482)
W('30,3433', 0o66370, '', 'AXT,1', 'SSP', kind='interp', line=2483)
W('30,3434', 0o00154, '', 'DEC', '108', 'CLEAR W0 TO W54', kind='data', line=2484)
W('30,3435', 0o00051, '', '', 'S1', kind='operand', line=2485)
W('30,3436', 0o00006, '', '', '6', kind='operand', line=2486)
W('30,3437', 0o06555, 'CLEARW54', 'STORE', 'W +108D,1', kind='interp', line=2487)
W('30,3440', 0o77700, '', 'TIX,1', kind='interp', line=2488)
# Page 612
W('30,3441', 0o61437, '', '', 'CLEARW54', kind='operand', line=2490)
W('30,3442', 0o66150, '9DWI=JA', 'LXA,1', 'SXA,1', 'I=J', kind='interp', line=2491)
W('30,3443', 0o00016, '', '', '9DWJ', kind='operand', line=2492)
W('30,3444', 0o00012, '', '', '9DWI', kind='operand', line=2493)
W('30,3445', 0o77624, '', 'CALL', kind='interp', line=2494)
W('30,3446', 0o61574, '', '', 'ROWDOT', kind='operand', line=2495)
W('30,3447', 0o43750, '', 'LXA,1', 'BDSU*', kind='interp', line=2496)
W('30,3450', 0o00010, '', '', '9DWP', kind='operand', line=2497)
W('30,3451', 0o02641, '', '', 'EMATRIX +40D,1', kind='operand', line=2498)
W('30,3452', 0o66110, '', 'INCR,1', 'SXA,1', '-(P+1)', kind='interp', line=2499)
W('30,3453', 0o00002, '', '', '2', kind='operand', line=2500)
W('30,3454', 0o00010, '', '', '9DWP', kind='operand', line=2501)
W('30,3455', 0o54140, '', 'LXC,1', 'XSU,1', '-(I+N)', kind='interp', line=2502)
W('30,3456', 0o00012, '', '', '9DWI', kind='operand', line=2503)
W('30,3457', 0o00014, '', '', '9DWN', kind='operand', line=2504)
W('30,3460', 0o71244, '', 'BPL', 'DLOAD', 'TEST WSQ LTE 0', kind='interp', line=2505)
W('30,3461', 0o61465, '', '', '9DWAAA', kind='operand', line=2506)
W('30,3462', 0o15335, '', '', 'HI6ZEROS', 'W=0', kind='operand', line=2507)
W('30,3463', 0o77650, '', 'GOTO', kind='interp', line=2508)
W('30,3464', 0o61466, '', '', '9DWAAB', kind='operand', line=2509)
W('30,3465', 0o77766, '9DWAAA', 'SQRT', '', 'W= SQRT(WSQ)', kind='interp', line=2510)
W('30,3466', 0o06401, '9DWAAB', 'STORE', 'W,1', kind='interp', line=2511)
W('30,3467', 0o14001, '', 'STODL', 'WORKW', kind='interp', line=2512)
W('30,3470', 0o00017, '', '', '9DWJ', 'TEST J=0', kind='operand', line=2513)
W('30,3471', 0o77630, '', 'BHIZ', kind='interp', line=2514)
W('30,3472', 0o61560, '', '', '9DWEXITX', 'EXIT', kind='operand', line=2515)
W('30,3473', 0o46135, 'TST2I=0', 'SLOAD', 'BHIZ', 'TEST I=0', kind='interp', line=2516)
W('30,3474', 0o00013, '', '', '9DWI', kind='operand', line=2517)
W('30,3475', 0o61536, '', '', '9DWN=N+3', kind='operand', line=2518)
W('30,3476', 0o77625, '', 'DSU', kind='interp', line=2519)
W('30,3477', 0o21634, '', '', '9DWID', kind='operand', line=2520)
W('30,3500', 0o00013, '', 'STORE', '9DWI', 'I=I-1', kind='interp', line=2521)
W('30,3501', 0o46025, '', 'DSU', 'BHIZ', 'TEST I=26', kind='interp', line=2522)
W('30,3502', 0o21632, '', '', '9DW26D', kind='operand', line=2523)
W('30,3503', 0o61506, '', '', '9DWAAC', kind='operand', line=2524)
W('30,3504', 0o77650, '', 'GOTO', kind='interp', line=2525)
W('30,3505', 0o61511, '', '', '9DWNEXEP', kind='operand', line=2526)
W('30,3506', 0o77731, '9DWAAC', 'SSP', '', 'I=2', kind='interp', line=2527)
W('30,3507', 0o00013, '', '', '9DWI', kind='operand', line=2528)
W('30,3510', 0o00004, '', '', '4', kind='operand', line=2529)
W('30,3511', 0o77624, '9DWNEXEP', 'CALL', kind='interp', line=2530)
W('30,3512', 0o61574, '', '', 'ROWDOT', kind='operand', line=2531)
W('30,3513', 0o43750, '', 'LXA,1', 'BDSU*', '(EP-ROWI*ROWJ)/W', kind='interp', line=2532)
W('30,3514', 0o00010, '', '', '9DWP', kind='operand', line=2533)
W('30,3515', 0o02641, '', '', 'EMATRIX +40D,1', kind='operand', line=2534)
W('30,3516', 0o62071, '', 'DDV', 'INCR,1', 'P=P+1', kind='interp', line=2535)
W('30,3517', 0o00001, '', '', 'WORKW', kind='operand', line=2536)
W('30,3520', 0o00002, '', '', '2', kind='operand', line=2537)
W('30,3521', 0o70130, '', 'SXA,1', 'LXC,1', kind='interp', line=2538)
W('30,3522', 0o00010, '', '', '9DWP', kind='operand', line=2539)
# Page 613
W('30,3523', 0o00012, '', '', '9DWI', kind='operand', line=2541)
W('30,3524', 0o40060, '', 'XSU,1', 'BOV', '-(I+N)', kind='interp', line=2542)
W('30,3525', 0o00014, '', '', '9DWN', kind='operand', line=2543)
W('30,3526', 0o61531, '', '', 'SETWIN=0', kind='operand', line=2544)
W('30,3527', 0o77650, '', 'GOTO', kind='interp', line=2545)
W('30,3530', 0o61533, '', '', '9DWSETWX', kind='operand', line=2546)
W('30,3531', 0o77745, 'SETWIN=0', 'DLOAD', '', 'W(I+N)=0', kind='interp', line=2547)
W('30,3532', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=2548)
W('30,3533', 0o06401, '9DWSETWX', 'STORE', 'W,1', kind='interp', line=2549)
W('30,3534', 0o77650, '', 'GOTO', kind='interp', line=2550)
W('30,3535', 0o61473, '', '', 'TST2I=0', kind='operand', line=2551)
W('30,3536', 0o62150, '9DWN=N+3', 'LXA,1', 'INCR,1', 'N=N+3', kind='interp', line=2552)
W('30,3537', 0o00014, '', '', '9DWN', kind='operand', line=2553)
W('30,3540', 0o00006, '', '', '6', kind='operand', line=2554)
W('30,3541', 0o67330, '', 'SXA,1', 'SLOAD', 'J=J-1', kind='interp', line=2555)
W('30,3542', 0o00014, '', '', '9DWN', kind='operand', line=2556)
W('30,3543', 0o00017, '', '', '9DWJ', kind='operand', line=2557)
W('30,3544', 0o77625, '', 'DSU', kind='interp', line=2558)
W('30,3545', 0o21634, '', '', '9DWID', kind='operand', line=2559)
W('30,3546', 0o00017, '', 'STORE', '9DWJ', kind='interp', line=2560)
W('30,3547', 0o46025, '', 'DSU', 'BHIZ', 'TEST J=26', kind='interp', line=2561)
W('30,3550', 0o21632, '', '', '9DW26D', kind='operand', line=2562)
W('30,3551', 0o61554, '', '', 'SETJ=2A', kind='operand', line=2563)
W('30,3552', 0o77650, '', 'GOTO', kind='interp', line=2564)
W('30,3553', 0o61442, '', '', '9DWI=JA', kind='operand', line=2565)
W('30,3554', 0o52131, 'SETJ=2A', 'SSP', 'GOTO', 'J=2', kind='interp', line=2566)
W('30,3555', 0o00017, '', '', '9DWJ', kind='operand', line=2567)
W('30,3556', 0o00004, '', '', '4', kind='operand', line=2568)
W('30,3557', 0o61442, '', '', '9DWI=JA', kind='operand', line=2569)
W('30,3560', 0o77624, '9DWEXITX', 'CALL', kind='interp', line=2570)
W('30,3561', 0o56750, '', '', 'GRP2PC', kind='operand', line=2571)
W('30,3562', 0o66370, '', 'AXT,1', 'SSP', 'CLEAR W6,W7,W8 USED TEMP FOR EMATRIX', kind='interp', line=2572)
W('30,3563', 0o00066, '', 'DEC', '54', kind='data', line=2573)
W('30,3564', 0o00051, '', '', 'S1', kind='operand', line=2574)
W('30,3565', 0o00006, '', '', '6', kind='operand', line=2575)
W('30,3566', 0o77775, '', 'VLOAD', kind='interp', line=2576)
W('30,3567', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=2577)
W('30,3570', 0o06643, '9DWEXXXA', 'STORE', 'W +162D,1', kind='interp', line=2578)
W('30,3571', 0o52100, '', 'TIX,1', 'GOTO', kind='interp', line=2579)
W('30,3572', 0o61570, '', '', '9DWEXXXA', kind='operand', line=2580)
W('30,3573', 0o01214, '', '', '9DWXX', kind='operand', line=2581)
W('30,3574', 0o40131, 'ROWDOT', 'SSP', 'BOV', kind='interp', line=2582)
W('30,3575', 0o00007, '', '', 'XTMP1', kind='operand', line=2583)
W('30,3576', 0o00377, '', 'OCT', '377', kind='data', line=2584)
W('30,3577', 0o61600, '', '', '+1', kind='operand', line=2585)
W('30,3600', 0o71140, '', 'LXC,1', 'LXC,2', kind='interp', line=2586)
W('30,3601', 0o00012, '', '', '9DWI', kind='operand', line=2587)
W('30,3602', 0o00016, '', '', '9DWJ', kind='operand', line=2588)
W('30,3603', 0o41545, '', 'DLOAD', 'PUSH', kind='interp', line=2589)
W('30,3604', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=2590)
# Page 614
W('30,3605', 0o56743, 'ROWDOT1', 'DLOAD*', 'DMPR*', kind='interp', line=2592)
W('30,3606', 0o02401, '', '', 'W,1', kind='operand', line=2593)
W('30,3607', 0o75376, '', '', 'W,2', kind='operand', line=2594)
W('30,3610', 0o41415, '', 'DAD', 'PUSH', kind='interp', line=2595)
W('30,3611', 0o62000, '', 'BOV', 'INCR,1', kind='interp', line=2596)
W('30,3612', 0o61626, '', '', 'ROWDOT3', kind='operand', line=2597)
W('30,3613', 0o77771, '', 'DEC', '-6', kind='data', line=2598)
W('30,3614', 0o67314, '', 'INCR,2', 'SLOAD', kind='interp', line=2599)
W('30,3615', 0o77771, '', 'DEC', '-6', kind='data', line=2600)
W('30,3616', 0o00007, '', '', 'XTMP1', kind='operand', line=2601)
W('30,3617', 0o70430, '', 'BHIZ', 'SR1', kind='interp', line=2602)
W('30,3620', 0o61624, '', '', 'ROWDOT2', kind='operand', line=2603)
W('30,3621', 0o00007, '', 'STORE', 'XTMP1', kind='interp', line=2604)
W('30,3622', 0o77650, '', 'GOTO', kind='interp', line=2605)
W('30,3623', 0o61605, '', '', 'ROWDOT1', kind='operand', line=2606)
W('30,3624', 0o77745, 'ROWDOT2', 'DLOAD', kind='interp', line=2607)
W('30,3625', 0o77616, '', 'RVQ', kind='interp', line=2608)
W('30,3626', 0o77614, 'ROWDOT3', 'CLRGO', kind='interp', line=2609)
W('30,3627', 0o01631, '', '', 'ORBWFLAG', kind='operand', line=2610)
W('30,3630', 0o61624, '', '', 'ROWDOT2', kind='operand', line=2611)
S('WORKW', 'equals', 0o0, line=2612)
S('XTMP1', 'equals', 0o6, line=2613)
S('9DWP', 'equals', 0o10, line=2614)  # P
S('9DWI', 'equals', 0o12, line=2615)  # I
S('9DWN', 'equals', 0o14, line=2616)  # N
S('9DWJ', 'equals', 0o16, line=2617)  # J
S('9DWXX', 'equals', 0o1214, line=2618)
S('S22UMRL', 'equals', 0o3501, line=2619)  # 18
S('S22UUT', 'equals', 0o1256, line=2620)  # 18
S('S223X1', 'equals', 0o22, line=2621)  # 6
S('S221X3', 'equals', 0o30, line=2622)  # 6
S('S22D', 'equals', 0o36, line=2623)  # 2
S('S22RHO', 'equals', 0o40, line=2624)  # 2
S('S22RL', 'equals', 0o2634, line=2625)  # 6
W('30,3631', 0o00064, '9DW26D', '2DEC', '52 B-14', kind='data', line=2626)
W('30,3632', 0o00000, kind='data', line=2626)

W('30,3633', 0o00002, '9DWID', '2DEC', '2 B-14', kind='data', line=2628)
W('30,3634', 0o00000, kind='data', line=2628)

W('30,3635', 0o10306, 'SCTVAR', '2DEC', '1.0 E-6 B+18', kind='data', line=2630)
W('30,3636', 0o36750, kind='data', line=2630)

W('30,3637', 0o00253, 'IMUVARR', '2DEC', '0.04 E-6 B+18', kind='data', line=2632)
W('30,3640', 0o31436, kind='data', line=2632)

W('30,3641', 0o10000, 'DEC1B2', '2DEC', '1 B-2', kind='data', line=2634)
W('30,3642', 0o00000, kind='data', line=2634)

W('30,3643', 0o01461, 'V06N49EE', 'VN', '00649', kind='data', line=2636)
W('30,3644', 0o01531, 'V06N89B', 'VN', '00689', kind='data', line=2637)
S('S22UOFF', 'equals', 0o1214, line=2638)  # 6     U SUB OFF
#   SETLOC P20S2
#   BANK
# Page 615
# Nothing on this page. --- RSB 2009.

# Page 616
# SUBROUTINE NAME:  V89CALL
# MOD NO:  0                                    DATE: 8 FEB 1968
# MOD BY:  DIGITAL DEVEL GROUP                  LOG SECTION:  P20-P25
#
# FUNCTIONAL DESCRIPTION:
#
# CALLED BY VERB 89 ENTER DURING P00.  PRIO 10 USED.  CALCULATES AND
# DISPLAYS FINAL GIMBAL ANGLES TO POINT CSM +X AXIS OR PREFERRED AXIS
# (UNIT(Z)COS55 DEG + UNIT(X)SIN55 DEG) AT LM.
#
# 1. KEY IN V89 E ONLY IF IN PROG 00. IF NOT IN P00, OPERATOR ERROR AND
# EXIT R63, OTHERWISE CONTINUE.
#
# 2. IF IN P00, DO IMU STATUS CHECK (R02BOTH).  IF IMU ON AND ITS
# ORIENTATION KNOWN TO CGC, CONTINUE.
#
# 3. FLASH DISPLAY V 04 N 06.  R2 INDICATES WHICH SPACECRAFT AXIS IS TO
# BE POINTED AT LM.  INITIAL CHOICE IS PREFERRED AXIS.  (R2=1).
# ASTRONAUT CAN CHANGE TO (+X) AXIS (R2 NOT= 1) BY V22 E 2 E.  CONTINUE
# AFTER KEYING IN PROCEED.
#
# 4. SET PREFERRED ATTITUDE FLAG ACCORDING TO OPTION DESIRED.  SET FLAG
# FOR PREFERRED AXIS.  RESET FLAG FOR X AXIS.
#
# 5. CURRENT TIME IS STORED AND R63COMP IS CALLED
#
# R63COMP JOB:
#
# UPDATE CSM AND LM STATE VECTORS USING CONIC EQUATIONS
#
# CALCULATES BOTH PREFERRED AND X AXIS TRACKING ATT FROM CSM TO LM.
#
# DESIRED GIMBAL ANGLES AS INDICATED BY PREFERRED ATTITUDE FLAG
# ARE STORED FOR LATER R60CSM CALL.
#
# 6. FLASH DISPLAY V 06 N18 AND AWAIT RESPONSE.
#
# 7. RECYCLE: RETURN TO STEP 5.
# TERMINATE: EXIT R63 ROUTINE
# PROCEED:  RESET 3AXISFLG AND CALL R60CSM FOR ATTITUDE MANEUVER.
#
# CALLING SEQUENCE:     V 89 E
#
# SUBROUTINES CALLED:  CHKPOOH, R02BOTH, GOXDSPF, R63COMP, R60CSM
#
# ALARMS        1.  OPERATOR ERROR IF NOT IN P00
# 2.  PROGRAM ALARM IF IMU IS OFF
# 3.  PROGRAM ALARM IF IMU ORIENTATION IS UNKNOWN
# Page 617
#
# ERASABLE INITIALIZATION REQUIRED:  NONE
#
# DEBRIS:  OPTION1, OPTION1+1, PRFTEXAT(PREF ATT FLAG), P21TIME, 3AXISFLG

W('23,3132', 0o00000, 'DP1MIN', '2DEC', '6000', kind='data', line=2699)
W('23,3133', 0o13560, kind='data', line=2699)

#   EBANK= P21TIME
#   BANK 34
#   SETLOC P20S4
#   BANK
#   COUNT* $$/R63

W('34,3712', 0o04662, 'V89CALL', 'TC', 'BANKCALL', 'IMU STATUS CHECK. RETURNS IF ORIENTATION', line=2707)
W('34,3713', 0o17653, '', 'CADR', 'R02BOTH', 'KNOWN.  ALARMS IF NOT.', kind='data', line=2708)
W('34,3714', 0o36214, '', 'CAF', 'THREE', 'ALLOW ASTRONAUT TO SELECT DESIRED', line=2709)
W('34,3715', 0o55131, '', 'TS', 'OPTION1', 'TRACKING ATTITUDE AXIS.', line=2710)
W('34,3716', 0o35017, '', 'CAF', 'ONE', line=2711)
W('34,3717', 0o55132, '', 'TS', 'OPTION1 +1', line=2712)
W('34,3720', 0o33761, '', 'CAF', 'VB04N06', 'V 04 N 06', line=2713)
W('34,3721', 0o04662, '', 'TC', 'BANKCALL', line=2714)
W('34,3722', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=2715)
W('34,3723', 0o05534, '', 'TC', 'ENDEXT', 'TERMINATE', line=2716)
W('34,3724', 0o03726, '', 'TC', '+2', 'PROCEED', line=2717)
W('34,3725', 0o03720, '', 'TC', '-5', 'DATA IN.  OPTION1 +1 = 1 FOR PREF AXIS', line=2718)
# = 2 FOR X AXIS
W('34,3726', 0o41132, '', 'CS', 'OPTION1 +1', '1 FOR PREF AXIS.  2 FOR X AXIS.', line=2720)
W('34,3727', 0o65017, '', 'AD', 'ONE', line=2721)
W('34,3730', 0o00006, '', 'EXTEND', line=2722)
W('34,3731', 0o13756, '', 'BZF', 'SETPAF', line=2723)
W('34,3732', 0o05560, 'RSTPAF', 'TC', 'DOWNFLAG', 'RESET PREF ATT FLAG FOR R63COMP', line=2724)
W('34,3733', 0o00120, '', 'ADRES', 'RNGSCFLG', 'TO DO X AXIS.  RESET BIT 10 FLAG 5', kind='data', line=2725)
W('34,3734', 0o06006, 'V89RECL', 'TC', 'INTPRET', line=2726)
W('34,3735', 0o43234, '', 'RTB', 'DAD', kind='interp', line=2727)
W('34,3736', 0o45510, '', '', 'LOADTIME', 'READ PRESENT TIME', kind='operand', line=2728)
W('34,3737', 0o07133, '', '', 'DP1MIN', 'INTEGRATE TO 1 MIN FROM NOW', kind='operand', line=2729)
W('34,3740', 0o36316, '', 'STCALL', 'P21TIME', 'STORE TIME FOR CALL TO R63COMP.  R63COMP', kind='interp', line=2730)
W('34,3741', 0o71572, '', '', 'R63COMP', 'LEAVES DESIRED GIM ANGS IN THETAD, LOS IN', kind='operand', line=2731)
W('34,3742', 0o77776, '', 'EXIT', '', 'POINTVSM, AND SELECTED AXIS IN SCAXIS.', kind='interp', line=2732)
W('34,3743', 0o33762, '', 'CAF', 'VB06N18', 'V 06 N 18', line=2733)
W('34,3744', 0o04662, '', 'TC', 'BANKCALL', 'NOUN 18 REFERS TO THE DESIRED GIMBAL', line=2734)
W('34,3745', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=2735)
W('34,3746', 0o05534, '', 'TC', 'ENDEXT', 'TERMINATE', line=2736)
W('34,3747', 0o03751, '', 'TC', '+2', 'PROCEED', line=2737)
W('34,3750', 0o03734, '', 'TC', 'V89RECL', 'RECYCLE', line=2738)
W('34,3751', 0o05560, '', 'TC', 'DOWNFLAG', 'RESET 3 AXIS FLAG', line=2739)
W('34,3752', 0o00124, '', 'ADRES', '3AXISFLG', 'RESET BIT 6 FLAG 5', kind='data', line=2740)
# Page 618
W('34,3753', 0o04662, '', 'TC', 'BANKCALL', 'PERFORMS CSM MANEUVER TO ALIGN SELECTED', line=2742)
W('34,3754', 0o56000, '', 'CADR', 'R60CSM', 'SPACECRAFT AXIS TO LOS.', kind='data', line=2743)
W('34,3755', 0o15534, '', 'TCF', 'ENDEXT', line=2744)

W('34,3756', 0o05546, 'SETPAF', 'TC', 'UPFLAG', 'SET PREFERRED ATT FLAG FOR R63COMP', line=2746)
W('34,3757', 0o00120, '', 'ADRES', 'RNGSCFLG', 'TO DO PREF AXIS.  SET BIT 10 FLAG 5.', kind='data', line=2747)
W('34,3760', 0o03734, '', 'TC', 'V89RECL', line=2748)

W('34,3761', 0o01006, 'VB04N06', 'VN', '0406', kind='data', line=2750)
W('34,3762', 0o01422, 'VB06N18', 'VN', '0618', kind='data', line=2751)

S('R63COMP', 'equals', 0o101572, line=2753)

# Page 619
# PROGRAM NAME:  P23 CISLUNAR MIDCOURSE NAVIGATION
# MOD NO:
# MOD BY:  TOM KNATT
#
# FUNCTIONAL DESCRIPTION:  DO MIDCOURSE NAVIGATION BY INCORPORATION OF
# STAR/EARTH AND STAR/MOON OPTICAL MEASUREMENTS.
#
# CALLING SEQUENCE:  ASTRONAUT OPERATED
#
# SUBROUTINES CALLED:  R52,R53,R57,R60,ORBITAL INTEGRATION (INTEGRV)
# INCORP1,INCORP2,LALOTORV,LUNLMKLD, AND DISPLAY INTERFACE ROuTINES.
#
# N0RMAL EXIT MODES:  VIA R00
#
# ALARMS:  NONE
#
# ABORT MODES:  NONE
#
# ERASABLE INITIALIZATION REQUIRED:  PAD-LOADED ERASABLES, ORBWFLAG RESET,
# REFSMFLG=0 IF IMU OFF AND REFSMFLG=1 IF IMU ONE
#
# INPUTS BY USER REQUIRED:  STAR NUMBER, LANDMARK LAT, LONG/2, ALT OR ID NUMB.
# IF LANDMARK IS USED, NEAR OR FAR HORIzON IF HORIZON IS USED, AND
# BODY TO BE MARKED ON (EARTH OR MOON).  SEE GSOP CHAPT 4.
#
# OUTPUT:  UPDATED CMC STATE VECTOR.  VECTOR FROM S/C TO HORIZON OR LANDMARK
# IN POINTAXS.  POINTAXS CAN BE USED TO GENERATE THIS VECTOR APART FROM
# P23 IF DESIRED.
#
# DEBRIS:  NO USABLE DEBRIS IS GENERATED.  RENDWFLG IS RESET FOR P20 UPON
# COMPLETION OF P23.  RUPTREGS AND ERASABLES USED BY DISPLAYS ARE DEBRIS.

#   BANK 31
#   SETLOC RT23
#   BANK
#   COUNT 31/S23
#   EBANK= W
W('31,2403', 0o05560, 'P23', 'TC', 'DOWNFLAG', line=2793)
W('31,2404', 0o00010, '', 'ADRES', 'RNDVZFLG', kind='data', line=2794)

W('31,2405', 0o05372, '', 'TC', '2PHSCHNG', line=2796)
W('31,2406', 0o00004, '', 'OCT', '00004', 'LEAVE GROUP 4', kind='data', line=2797)
W('31,2407', 0o00012, '', 'OCT', '00012', 'ENTER GROUP 2', kind='data', line=2798)
W('31,2410', 0o35065, '', 'CAF', 'PRIO13', line=2799)
W('31,2411', 0o55056, '', 'TS', 'PHSPRDT2', line=2800)
W('31,2412', 0o06006, '', 'TC', 'INTPRET', line=2801)
W('31,2413', 0o43131, '', 'SSP', 'CLEAR', kind='interp', line=2802)
W('31,2414', 0o00302, '', '', 'MARKINDX', kind='operand', line=2803)
W('31,2415', 0o00001, '', '', '1', kind='operand', line=2804)
W('31,2416', 0o00666, '', '', 'TARG2FLG', 'TARGET FLAG USED R52 AND R53', kind='operand', line=2805)
W('31,2417', 0o66214, '', 'CLEAR', 'SSP', kind='interp', line=2806)
W('31,2420', 0o00665, '', '', 'TARG1FLG', kind='operand', line=2807)
W('31,2421', 0o00305, '', '', 'STARIND', kind='operand', line=2808)
W('31,2422', 0o00000, '', '', '0', kind='operand', line=2809)
W('31,2423', 0o43131, '', 'SSP', 'CLEAR', kind='interp', line=2810)
W('31,2424', 0o00303, '', '', 'BESTI', kind='operand', line=2811)
W('31,2425', 0o00000, '', '', '0', kind='operand', line=2812)
W('31,2426', 0o03267, '', '', 'R57FLAG', 'SET = DO NOT REPERFORM R57', kind='operand', line=2813)
W('31,2427', 0o77414, '', 'CLEAR', 'EXIT', kind='interp', line=2814)
W('31,2430', 0o04664, '', '', 'V94FLAG', 'SET = ALLOW V94', kind='operand', line=2815)
W('31,2431', 0o06006, 'P23.00', 'TC', 'INTPRET', line=2816)
# Page 620
W('31,2432', 0o45014, '', 'BON', 'CALL', kind='interp', line=2818)
W('31,2433', 0o01702, '', '', 'REFSMFLG', 'SET NOW AS INPUT, NORMALLY EXTERNAL CONT', kind='operand', line=2819)
W('31,2434', 0o62442, '', '', 'P23.05', 'WHEN ALIGNED, PERFORM MEASUREMENT', kind='operand', line=2820)
W('31,2435', 0o76401, '', '', 'R57', 'DO OPTICS CALIBRATION IF IMU NOT ALIGNED.', kind='operand', line=2821)
W('31,2436', 0o77624, '', 'CALL', kind='interp', line=2822)
W('31,2437', 0o31300, '', '', 'R53', kind='operand', line=2823)
W('31,2440', 0o77650, '', 'GOTO', kind='interp', line=2824)
W('31,2441', 0o62641, '', '', 'P23.60', kind='operand', line=2825)
W('31,2442', 0o77414, 'P23.05', 'CLEAR', 'EXIT', kind='interp', line=2826)
W('31,2443', 0o04665, '', '', 'SAVECFLG', 'USED TO SAVE SPACE IN P23.65', kind='operand', line=2827)
W('31,2444', 0o33456, 'P23.06', 'CAF', 'V05N70', line=2828)
W('31,2445', 0o04662, '', 'TC', 'BANKCALL', 'IDENTIFICATION:  STAR, HOR  IDENT.', line=2829)
W('31,2446', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=2830)
W('31,2447', 0o04106, '', 'TC', 'GOTOPOOH', 'TERMINATE', line=2831)
W('31,2450', 0o02452, '', 'TC', 'P23.15', line=2832)
W('31,2451', 0o02444, '', 'TC', '-5', 'REDISPLAY', line=2833)
W('31,2452', 0o31751, 'P23.15', 'CA', 'LANDMARK', 'IF C=2, LUNAFLAG=1.  IF C=1, LUNAFLAG=0', line=2834)
W('31,2453', 0o00006, '', 'EXTEND', line=2835)
W('31,2454', 0o12463, '', 'BZF', 'P23.151', line=2836)
W('31,2455', 0o31752, '', 'CA', 'HORIZON', line=2837)
W('31,2456', 0o00006, '', 'EXTEND', line=2838)
W('31,2457', 0o12461, '', 'BZF', '+2', line=2839)
W('31,2460', 0o03134, '', 'TC', 'R23.10', 'OPERATOR DSKY ERROR', line=2840)
W('31,2461', 0o31751, '', 'CA', 'LANDMARK', line=2841)
W('31,2462', 0o02466, '', 'TC', 'P23.152', line=2842)
W('31,2463', 0o31752, 'P23.151', 'CA', 'HORIZON', line=2843)
W('31,2464', 0o00006, '', 'EXTEND', line=2844)
W('31,2465', 0o13134, '', 'BZF', 'R23.10', line=2845)
W('31,2466', 0o73473, 'P23.152', 'MASK', 'BITS7-9', 'IS C EQUAL TO 1 OR 2', line=2846)
W('31,2467', 0o65234, '', 'AD', 'NEG100', line=2847)
W('31,2470', 0o00006, '', 'EXTEND', line=2848)
W('31,2471', 0o12501, '', 'BZF', 'P23.16', line=2849)
W('31,2472', 0o65234, '', 'AD', 'NEG100', line=2850)
W('31,2473', 0o00006, '', 'EXTEND', line=2851)
W('31,2474', 0o12476, '', 'BZF', '+2', line=2852)
W('31,2475', 0o03134, '', 'TC', 'R23.10', line=2853)
W('31,2476', 0o05546, '', 'TC', 'UPFLAG', line=2854)
W('31,2477', 0o00060, '', 'ADRES', 'LUNAFLAG', kind='data', line=2855)
W('31,2500', 0o12503, '', 'TCF', '+3', line=2856)
W('31,2501', 0o05560, 'P23.16', 'TC', 'DOWNFLAG', line=2857)
W('31,2502', 0o00060, '', 'ADRES', 'LUNAFLAG', kind='data', line=2858)
W('31,2503', 0o30735, '', 'CA', 'STARCODE', 'IS STARCODE GREATER THAN OR', line=2859)
W('31,2504', 0o00006, '', 'EXTEND', '', 'EQUAL TO 0 AND LESS THAN 37', line=2860)
W('31,2505', 0o12532, '', 'BZF', 'P23.176', line=2861)
W('31,2506', 0o00006, '', 'EXTEND', line=2862)
W('31,2507', 0o63134, '', 'BZMF', 'R23.10', line=2863)
W('31,2510', 0o63472, '', 'AD', 'NEG37', line=2864)
W('31,2511', 0o00006, '', 'EXTEND', line=2865)
W('31,2512', 0o62514, '', 'BZMF', '+2', line=2866)
W('31,2513', 0o03134, '', 'TC', 'R23.10', line=2867)
# Page 621

W('31,2514', 0o06006, '', 'TC', 'INTPRET', line=2870)
W('31,2515', 0o53135, 'P23.17', 'SLOAD', 'BZE', kind='interp', line=2871)
W('31,2516', 0o00736, '', '', 'STARCODE', kind='operand', line=2872)
W('31,2517', 0o62531, '', '', 'P23.175', kind='operand', line=2873)
W('31,2520', 0o77606, '', 'PUSH', kind='interp', line=2874)
W('31,2521', 0o41335, '', 'SLOAD', 'DMP', kind='interp', line=2875)
W('31,2522', 0o23463, '', '', 'SPSIX', kind='operand', line=2876)
W('31,2523', 0o66150, '', 'LXA,1', 'SXA,1', kind='interp', line=2877)
W('31,2524', 0o00155, '', '', 'MPAC +1', kind='operand', line=2878)
W('31,2525', 0o00302, '', '', 'BESTI', 'BESTI = 6 X STAR NUMBER', kind='operand', line=2879)
W('31,2526', 0o77624, '', 'CALL', kind='interp', line=2880)
W('31,2527', 0o30000, '', '', 'LOWMEMRY', 'NEEDED TO RETRIEVE STAR VECTOR FROM LOW', kind='operand', line=2881)
W('31,2530', 0o02617, '', 'STORE', 'STARSAV2', 'STORE FOR R53,P23.  US(IN P23)=STARSAV2', kind='interp', line=2882)
W('31,2531', 0o77776, 'P23.175', 'EXIT', kind='interp', line=2883)
W('31,2532', 0o31752, 'P23.176', 'CA', 'HORIZON', line=2884)
W('31,2533', 0o00006, '', 'EXTEND', line=2885)
W('31,2534', 0o12553, '', 'BZF', 'P23.20', line=2886)
W('31,2535', 0o73474, '', 'MASK', 'BITS4-6', line=2887)
W('31,2536', 0o66171, '', 'AD', '-OCT10', line=2888)
W('31,2537', 0o00006, '', 'EXTEND', line=2889)
W('31,2540', 0o12550, '', 'BZF', 'P23.18', line=2890)
W('31,2541', 0o66171, '', 'AD', '-OCT10', line=2891)
W('31,2542', 0o00006, '', 'EXTEND', line=2892)
W('31,2543', 0o12545, '', 'BZF', '+2', line=2893)
W('31,2544', 0o03134, '', 'TC', 'R23.10', line=2894)
W('31,2545', 0o05546, '', 'TC', 'UPFLAG', line=2895)
W('31,2546', 0o00004, '', 'ADRES', 'NORFHOR', kind='data', line=2896)
W('31,2547', 0o02557, '', 'TC', 'P23.30', line=2897)
W('31,2550', 0o05560, 'P23.18', 'TC', 'DOWNFLAG', line=2898)
W('31,2551', 0o00004, '', 'ADRES', 'NORFHOR', kind='data', line=2899)
W('31,2552', 0o02557, '', 'TC', 'P23.30', line=2900)
W('31,2553', 0o06006, 'P23.20', 'TC', 'INTPRET', line=2901)
W('31,2554', 0o77624, '', 'CALL', kind='interp', line=2902)
W('31,2555', 0o60143, '', '', 'P22SUBRB', kind='operand', line=2903)
W('31,2556', 0o77776, '', 'EXIT', kind='interp', line=2904)
W('31,2557', 0o06006, 'P23.30', 'TC', 'INTPRET', line=2905)
W('31,2560', 0o53135, '', 'SLOAD', 'BZE', kind='interp', line=2906)
W('31,2561', 0o00736, '', '', 'STARCODE', kind='operand', line=2907)
W('31,2562', 0o34000, '', '', 'LDPLANET', kind='operand', line=2908)
W('31,2563', 0o77414, 'P23.31', 'BON', 'EXIT', kind='interp', line=2909)
W('31,2564', 0o04705, '', '', 'SAVECFLG', kind='operand', line=2910)
W('31,2565', 0o62700, '', '', 'P23.85', kind='operand', line=2911)
W('31,2566', 0o33461, '', 'CAF', 'V50N25P', line=2912)
W('31,2567', 0o04662, '', 'TC', 'BANKCALL', line=2913)
W('31,2570', 0o21045, '', 'CADR', 'GOPERF1', 'GOPERF1 BLANKS OUT R2 AND R3', kind='data', line=2914)
W('31,2571', 0o04106, '', 'TC', 'GOTOPOOH', line=2915)
W('31,2572', 0o02576, '', 'TC', 'V94ENTER', 'PROCEED.  AUTOCONTROL CMC', line=2916)
W('31,2573', 0o06006, 'P23.55', 'TC', 'INTPRET', line=2917)
W('31,2574', 0o77650, '', 'GOTO', kind='interp', line=2918)
W('31,2575', 0o62627, '', '', 'P23.56', kind='operand', line=2919)
# Page 622

# VERB 94 BEGINS HERE
W('31,2576', 0o06006, 'V94ENTER', 'TC', 'INTPRET', line=2923)
W('31,2577', 0o77634, '', 'RTB', kind='interp', line=2924)
W('31,2600', 0o45510, '', '', 'LOADTIME', 'READ CLOCK', kind='operand', line=2925)
W('31,2601', 0o35225, '', 'STCALL', 'MARKTIME', kind='interp', line=2926)
W('31,2602', 0o62705, '', '', 'POINTAXS', 'RETURN LOS IN RCLL AND MPAC', kind='operand', line=2927)
W('31,2603', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=2928)
W('31,2604', 0o01736, '', '', 'REFSMMAT', kind='operand', line=2929)
W('31,2605', 0o27357, '', 'STOVL', 'POINTVSM', kind='interp', line=2930)
W('31,2606', 0o23464, '', '', 'JCAXIS', kind='operand', line=2931)
W('31,2607', 0o03351, '', 'STORE', 'SCAXIS', kind='interp', line=2932)
W('31,2610', 0o77776, '', 'EXIT', kind='interp', line=2933)
W('31,2611', 0o05560, '', 'TC', 'DOWNFLAG', 'CLEAR AND GO TO VECPOINT IN R60', line=2934)
W('31,2612', 0o00124, '', 'ADRES', '3AXISFLG', 'BIT 6 FLAG 5', kind='data', line=2935)
W('31,2613', 0o33471, '', 'CAF', 'R60ADRS', line=2936)
W('31,2614', 0o54374, '', 'TS', 'TEMPFLSH', line=2937)
W('31,2615', 0o05412, '', 'TC', 'PHASCHNG', line=2938)
W('31,2616', 0o00012, '', 'OCT', '00012', kind='data', line=2939)
W('31,2617', 0o04662, 'R60CALL', 'TC', 'BANKCALL', line=2940)
W('31,2620', 0o56000, '', 'CADR', 'R60CSM', kind='data', line=2941)
W('31,2621', 0o05412, '', 'TC', 'PHASCHNG', line=2942)
W('31,2622', 0o04022, '', 'OCT', '04022', kind='data', line=2943)
W('31,2623', 0o06006, '', 'TC', 'INTPRET', line=2944)
W('31,2624', 0o77614, '', 'BON', kind='interp', line=2945)
W('31,2625', 0o03307, '', '', 'R57FLAG', kind='operand', line=2946)
W('31,2626', 0o62631, '', '', 'P23.57', 'DO NOT REPERFORM R57', kind='operand', line=2947)
W('31,2627', 0o77624, 'P23.56', 'CALL', kind='interp', line=2948)
W('31,2630', 0o76401, '', '', 'R57', kind='operand', line=2949)
W('31,2631', 0o43014, 'P23.57', 'SET', 'SET', kind='interp', line=2950)
W('31,2632', 0o04464, '', '', 'V94FLAG', kind='operand', line=2951)
W('31,2633', 0o03067, '', '', 'R57FLAG', kind='operand', line=2952)
W('31,2634', 0o77624, '', 'CALL', kind='interp', line=2953)
W('31,2635', 0o30011, '', '', 'R52', kind='operand', line=2954)
W('31,2636', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=2955)
W('31,2637', 0o04664, '', '', 'V94FLAG', kind='operand', line=2956)
W('31,2640', 0o03267, '', '', 'R57FLAG', kind='operand', line=2957)
W('31,2641', 0o77776, 'P23.60', 'EXIT', kind='interp', line=2958)
W('31,2642', 0o00004, '', 'INHINT', line=2959)
W('31,2643', 0o31330, '', 'CA', 'MARKSTAT', line=2960)
W('31,2644', 0o75054, '', 'MASK', 'LOW10', line=2961)
W('31,2645', 0o55242, '', 'TS', 'MARKDATA', line=2962)
W('31,2646', 0o00006, '', 'EXTEND', line=2963)
W('31,2647', 0o51242, '', 'INDEX', 'MARKDATA', line=2964)
W('31,2650', 0o30001, '', 'DCA', '0', line=2965)
W('31,2651', 0o53225, '', 'DXCH', 'MARKTIME', line=2966)
W('31,2652', 0o51242, '', 'INDEX', 'MARKDATA', line=2967)
W('31,2653', 0o30005, '', 'CA', '5', line=2968)
W('31,2654', 0o57754, '', 'XCH', 'TRUNION', line=2969)
W('31,2655', 0o00003, '', 'RELINT', line=2970)
W('31,2656', 0o06006, '', 'TC', 'INTPRET', line=2971)
# Page 623
W('31,2657', 0o76740, '', 'LXC,1', 'VLOAD*', kind='interp', line=2973)
W('31,2660', 0o01242, '', '', 'MARKDATA', kind='operand', line=2974)
W('31,2661', 0o00002, '', '', '1,1', kind='operand', line=2975)
W('31,2662', 0o23676, '', 'STODL*', 'MARKDOWN +1', kind='interp', line=2976)
W('31,2663', 0o00001, '', '', '0,1', kind='operand', line=2977)
W('31,2664', 0o03675, '', 'STORE', 'MARKDOWN', kind='interp', line=2978)
W('31,2665', 0o77776, '', 'EXIT', kind='interp', line=2979)
W('31,2666', 0o33457, '', 'CAF', 'V05N71', line=2980)
W('31,2667', 0o04662, '', 'TC', 'BANKCALL', line=2981)
W('31,2670', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=2982)
W('31,2671', 0o04106, '', 'TC', 'GOTOPOOH', 'TERMINATE', line=2983)
W('31,2672', 0o02674, '', 'TC', 'P23.65', 'STORE DATA', line=2984)
W('31,2673', 0o02666, '', 'TC', '-5', 'REDISPLAY', line=2985)
W('31,2674', 0o06006, 'P23.65', 'TC', 'INTPRET', line=2986)
W('31,2675', 0o77414, '', 'SET', 'EXIT', kind='interp', line=2987)
W('31,2676', 0o04465, '', '', 'SAVECFLG', kind='operand', line=2988)
W('31,2677', 0o02452, '', 'TC', 'P23.15', line=2989)
W('31,2700', 0o45014, 'P23.85', 'CLEAR', 'CALL', kind='interp', line=2990)
W('31,2701', 0o02676, '', '', 'RENDWFLG', kind='operand', line=2991)
W('31,2702', 0o62705, '', '', 'POINTAXS', kind='operand', line=2992)
W('31,2703', 0o77650, '', 'GOTO', kind='interp', line=2993)
W('31,2704', 0o62771, '', '', 'R23.55', kind='operand', line=2994)

# WE BEGIN CALCULATIONS HERE
# POINTAXIS SUBROUTINE

W('31,2705', 0o77620, 'POINTAXS', 'STQ', kind='interp', line=2999)
W('31,2706', 0o01150, '', '', 'POINTEX', kind='operand', line=3000)
W('31,2707', 0o71214, 'R23.05', 'BON', 'DLOAD', kind='interp', line=3001)
W('31,2710', 0o01711, '', '', 'ORBWFLAG', kind='operand', line=3002)
W('31,2711', 0o62715, '', '', 'R23.1', kind='operand', line=3003)
W('31,2712', 0o03001, '', '', 'WMIDPOS', kind='operand', line=3004)
W('31,2713', 0o34001, '', 'STCALL', '0', kind='interp', line=3005)
W('31,2714', 0o56565, '', '', 'INITIALW', 'INITIALIZE W-MATRIX FIRST PASS IN P23', kind='operand', line=3006)
W('31,2715', 0o77624, 'R23.1', 'CALL', kind='interp', line=3007)
W('31,2716', 0o56343, '', '', 'SETINTG', 'SETUP FOR CSM INTEGRATION', kind='operand', line=3008)
W('31,2717', 0o43014, '', 'BOF', 'SET', kind='interp', line=3009)
W('31,2720', 0o01751, '', '', 'ORBWFLAG', kind='operand', line=3010)
W('31,2721', 0o62723, '', '', 'R23.2', kind='operand', line=3011)
W('31,2722', 0o01476, '', '', 'DIM0FLAG', kind='operand', line=3012)
W('31,2723', 0o45014, 'R23.2', 'SET', 'CALL', kind='interp', line=3013)
W('31,2724', 0o01471, '', '', 'ORBWFLAG', kind='operand', line=3014)
W('31,2725', 0o27162, '', '', 'INTEGRV', 'INTEGRATE CSM STATE VEC. TO MARKTIME', kind='operand', line=3015)
W('31,2726', 0o77776, '', 'EXIT', kind='interp', line=3016)
W('31,2727', 0o05412, '', 'TC', 'PHASCHNG', line=3017)
W('31,2730', 0o04022, '', 'OCT', '04022', kind='data', line=3018)
W('31,2731', 0o06006, '', 'TC', 'INTPRET', line=3019)
W('31,2732', 0o77624, '', 'CALL', kind='interp', line=3020)
W('31,2733', 0o63376, '', '', 'RECT.1', 'PICKUP CSM STATE VECTOR FROM PERM', kind='operand', line=3021)
W('31,2734', 0o77614, '', 'BOFF', kind='interp', line=3022)
W('31,2735', 0o00345, '', '', 'ZMEASURE', 'IN SPHERE OF INFLUENCE OF PRIMARY BODY', kind='operand', line=3023)
W('31,2736', 0o62750, '', '', 'R23.3', kind='operand', line=3024)
# Page 624
W('31,2737', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=3026)
W('31,2740', 0o01225, '', '', 'MARKTIME', kind='operand', line=3027)
W('31,2741', 0o54115, '', '', 'LUNPOS', kind='operand', line=3028)
W('31,2742', 0o57414, '', 'BON', 'VCOMP', kind='interp', line=3029)
W('31,2743', 0o04303, '', '', 'CMOONFLG', kind='operand', line=3030)
W('31,2744', 0o62745, '', '', '+1', kind='operand', line=3031)
W('31,2745', 0o77655, '', 'VAD', kind='interp', line=3032)
W('31,2746', 0o03627, '', '', 'RZC', kind='operand', line=3033)
W('31,2747', 0o03627, '', 'STORE', 'RZC', kind='interp', line=3034)
W('31,2750', 0o46135, 'R23.3', 'SLOAD', 'BHIZ', kind='interp', line=3035)
W('31,2751', 0o02752, '', '', 'LANDMARK', 'IF LANDMARK = 0, USE HORIZ SUBR', kind='operand', line=3036)
W('31,2752', 0o62762, '', '', 'R23.4', kind='operand', line=3037)
W('31,2753', 0o77614, '', 'SET', kind='interp', line=3038)
W('31,2754', 0o00462, '', '', 'ERADFLAG', kind='operand', line=3039)
W('31,2755', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=3040)
W('31,2756', 0o01225, '', '', 'MARKTIME', kind='operand', line=3041)
W('31,2757', 0o26441, '', '', 'LALOTORV', kind='operand', line=3042)
W('31,2760', 0o77650, '', 'GOTO', kind='interp', line=3043)
W('31,2761', 0o62764, '', '', 'R23.5', kind='operand', line=3044)
W('31,2762', 0o77624, 'R23.4', 'CALL', kind='interp', line=3045)
W('31,2763', 0o63136, '', '', 'HORIZ', kind='operand', line=3046)
W('31,2764', 0o40251, 'R23.5', 'VSU', 'SETPD', kind='interp', line=3047)
W('31,2765', 0o03627, '', '', 'RZC', kind='operand', line=3048)
W('31,2766', 0o00001, '', '', '0', kind='operand', line=3049)
W('31,2767', 0o77650, '', 'GOTO', kind='interp', line=3050)
W('31,2770', 0o01150, '', '', 'POINTEX', kind='operand', line=3051)
# Page 625
W('31,2771', 0o41456, 'R23.55', 'UNIT', 'PUSH', 'RCLL IS IN MPAC', kind='interp', line=3053)
W('31,2772', 0o77775, '', 'VLOAD', kind='interp', line=3054)
W('31,2773', 0o00043, '', '', '34D', 'RCLL * RCLL', kind='operand', line=3055)
W('31,2774', 0o24037, '', 'STOVL', '30D', 'PUSH 30-31 =RCLL*RCLL 32-33=ABVAL RCLL', kind='interp', line=3056)
W('31,2775', 0o03635, '', '', 'VZC', kind='operand', line=3057)
W('31,2776', 0o54361, '', 'VXSC', 'VSR', kind='interp', line=3058)
W('31,2777', 0o23437, '', '', 'ONE/C', kind='operand', line=3059)
W('31,3000', 0o20620, '', '', '15D', kind='operand', line=3060)
W('31,3001', 0o77655, '', 'VAD', '', 'PUSH UP RCLL(UNIT)', kind='interp', line=3061)
W('31,3002', 0o77656, '', 'UNIT', kind='interp', line=3062)
W('31,3003', 0o27643, '', 'STOVL', 'UCLSTAR', kind='interp', line=3063)
W('31,3004', 0o03635, '', '', 'VZC', kind='operand', line=3064)
W('31,3005', 0o52342, '', 'VSR2', 'VSU', kind='interp', line=3065)
W('31,3006', 0o02141, '', '', 'VESO', kind='operand', line=3066)
W('31,3007', 0o54361, '', 'VXSC', 'VSR', kind='interp', line=3067)
W('31,3010', 0o23437, '', '', 'ONE/C', kind='operand', line=3068)
W('31,3011', 0o20616, '', '', '13D', kind='operand', line=3069)
W('31,3012', 0o53455, '', 'VAD', 'UNIT', kind='interp', line=3070)
W('31,3013', 0o02617, '', '', 'US', kind='operand', line=3071)
W('31,3014', 0o03651, '', 'STORE', 'USSTAR', kind='interp', line=3072)
W('31,3015', 0o72441, '', 'DOT', 'SL1', kind='interp', line=3073)
W('31,3016', 0o03643, '', '', 'UCLSTAR', kind='operand', line=3074)
W('31,3017', 0o77206, '', 'PUSH', 'VLOAD', 'PD 0,1 = USSTAR(DOT)UCLSTAR', kind='interp', line=3075)
W('31,3020', 0o03643, '', '', 'UCLSTAR', kind='operand', line=3076)
W('31,3021', 0o57561, '', 'VXSC', 'VCOMP', kind='interp', line=3077)
W('31,3022', 0o53372, '', 'VSL1', 'VAD', kind='interp', line=3078)
W('31,3023', 0o03651, '', '', 'USSTAR', kind='operand', line=3079)
W('31,3024', 0o77656, '', 'UNIT', kind='interp', line=3080)
W('31,3025', 0o27502, '', 'STOVL', 'BVECTOR', 'USSTAR - COSQ(UCLSTAR)', kind='interp', line=3081)
W('31,3026', 0o15335, '', '', 'ZEROVECS', kind='operand', line=3082)
W('31,3027', 0o03510, '', 'STORE', 'BVECTOR +6', kind='interp', line=3083)
W('31,3030', 0o17516, '', 'STODL', 'BVECTOR +12D', kind='interp', line=3084)
W('31,3031', 0o00001, '', '', '0', kind='operand', line=3085)
W('31,3032', 0o57526, '', 'ACOS', 'DCOMP', kind='interp', line=3086)
W('31,3033', 0o71206, '', 'PUSH', 'DLOAD', kind='interp', line=3087)
W('31,3034', 0o15335, '', '', 'ZEROVECS', kind='operand', line=3088)
W('31,3035', 0o77776, '', 'EXIT', kind='interp', line=3089)
W('31,3036', 0o33450, '', 'CA', 'VARSUBL', 'PUT FIXED INTO ERASABLE FOR MSU', line=3090)
W('31,3037', 0o54001, '', 'TS', 'L', 'INSTRUCTION COMING UP', line=3091)
W('31,3040', 0o31754, '', 'CA', 'TRUNION', "REQUIRED TO CHANGE 2'S COMPLEMENT", line=3092)
W('31,3041', 0o00006, '', 'EXTEND', '', "TRUNION TO 1'S COMPLEMENT", line=3093)
W('31,3042', 0o20001, '', 'MSU', 'L', "TRUNION (2'S)-00000 CONVERTS TRUNION TO", line=3094)
W('31,3043', 0o54154, '', 'TS', 'MPAC', "1'S.  VARSUBL=00000.", line=3095)
W('31,3044', 0o06006, '', 'TC', 'INTPRET', line=3096)
W('31,3045', 0o67206, '', 'PUSH', 'SLOAD', 'PUSH IS DP.  WHEN BDSU IS EXECUTED, 2ND', kind='interp', line=3097)
W('31,3046', 0o01343, '', '', 'TRUNBIAS', 'HALF OF PUSHLIST IS GUARANTEED ZERO FROM', kind='operand', line=3098)
W('31,3047', 0o77621, '', 'BDSU', '', 'DLOAD ZEROVECS ABOVE', kind='interp', line=3099)
W('31,3050', 0o43242, '', 'SR3', 'DAD', kind='interp', line=3100)
W('31,3051', 0o41215, '', 'DAD', 'DMP', kind='interp', line=3101)
# Page 626
W('31,3052', 0o23445, '', '', 'TRUN19', kind='operand', line=3103)
W('31,3053', 0o00041, '', '', '32D', kind='operand', line=3104)
W('31,3054', 0o52405, '', 'DMP', 'SL3', kind='interp', line=3105)
W('31,3055', 0o07103, '', '', 'PI/4.0', kind='operand', line=3106)
W('31,3056', 0o62414, '', 'BOFF', 'SL2', kind='interp', line=3107)
W('31,3057', 0o04343, '', '', 'CMOONFLG', kind='operand', line=3108)
W('31,3060', 0o63061, '', '', 'R23.51', kind='operand', line=3109)
W('31,3061', 0o17524, 'R23.51', 'STODL', 'DELTAQ', kind='interp', line=3110)
W('31,3062', 0o00037, '', '', '30D', 'RCLL * RCLL', kind='operand', line=3111)
W('31,3063', 0o47005, '', 'DMP', 'RTB', kind='interp', line=3112)
W('31,3064', 0o23454, '', '', 'TRUNVAR', kind='operand', line=3113)
W('31,3065', 0o45565, '', '', 'TPMODE', kind='operand', line=3114)
W('31,3066', 0o77771, '', 'TAD', kind='interp', line=3115)
W('31,3067', 0o23451, '', '', 'VARSUBL', kind='operand', line=3116)
W('31,3070', 0o03526, '', 'STORE', 'VARIANCE', kind='interp', line=3117)
W('31,3071', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=3118)
W('31,3072', 0o02666, '', '', 'DMENFLG', kind='operand', line=3119)
W('31,3073', 0o75254, '', '', 'INCORP1', kind='operand', line=3120)
W('31,3074', 0o77624, '', 'CALL', kind='interp', line=3121)
W('31,3075', 0o56750, '', '', 'GRP2PC', kind='operand', line=3122)
W('31,3076', 0o51575, '', 'VLOAD', 'ABVAL', kind='interp', line=3123)
W('31,3077', 0o01265, '', '', 'DELTAX +6', kind='operand', line=3124)
W('31,3100', 0o60414, '', 'BOF', 'SR2', 'DISPLAY IS 2-27 IF IN LUNAR SPHERE.', kind='interp', line=3125)
W('31,3101', 0o04343, '', '', 'CMOONFLG', kind='operand', line=3126)
W('31,3102', 0o63103, '', '', 'R23.52', kind='operand', line=3127)
W('31,3103', 0o27504, 'R23.52', 'STOVL', 'N49DISP +2', kind='interp', line=3128)
W('31,3104', 0o01257, '', '', 'DELTAX', kind='operand', line=3129)
W('31,3105', 0o77646, '', 'ABVAL', kind='interp', line=3130)
W('31,3106', 0o60414, '', 'BOF', 'SR2', kind='interp', line=3131)
W('31,3107', 0o04343, '', '', 'CMOONFLG', kind='operand', line=3132)
W('31,3110', 0o63111, '', '', 'R23.53', kind='operand', line=3133)
W('31,3111', 0o03502, 'R23.53', 'STORE', 'N49DISP', kind='interp', line=3134)
W('31,3112', 0o77776, '', 'EXIT', kind='interp', line=3135)
W('31,3113', 0o33455, 'R23.6', 'CAF', 'V6N49', line=3136)
W('31,3114', 0o04662, '', 'TC', 'BANKCALL', line=3137)
W('31,3115', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=3138)
W('31,3116', 0o04106, '', 'TC', 'GOTOPOOH', line=3139)
W('31,3117', 0o03126, '', 'TC', 'R23.7', 'INCORPORATE DATA', line=3140)
W('31,3120', 0o04106, '', 'TC', 'GOTOPOOH', line=3141)
W('31,3121', 0o35015, '', 'CAF', 'BIT3', 'BLAN OUT R3', line=3142)
W('31,3122', 0o05526, '', 'TC', 'BLANKET', line=3143)
W('31,3123', 0o05412, '', 'TC', 'PHASCHNG', line=3144)
W('31,3124', 0o00012, '', 'OCT', '00012', kind='data', line=3145)
W('31,3125', 0o05217, '', 'TC', 'ENDOFJOB', line=3146)
W('31,3126', 0o06006, 'R23.7', 'TC', 'INTPRET', line=3147)
W('31,3127', 0o45014, 'R23.8', 'SET', 'CALL', kind='interp', line=3148)
W('31,3130', 0o00467, '', '', 'VEHUPFLG', kind='operand', line=3149)
W('31,3131', 0o75466, '', '', 'INCORP2', kind='operand', line=3150)
W('31,3132', 0o77776, '', 'EXIT', kind='interp', line=3151)
W('31,3133', 0o04106, 'R23.END', 'TC', 'GOTOPOOH', line=3152)

# Page 627
W('31,3134', 0o04400, 'R23.10', 'TC', 'FALTON', line=3155)
W('31,3135', 0o02444, '', 'TC', 'P23.06', line=3156)
W('31,3136', 0o40220, 'HORIZ', 'STQ', 'SETPD', kind='interp', line=3157)
W('31,3137', 0o03656, '', '', 'SRRETURN', kind='operand', line=3158)
W('31,3140', 0o00001, '', '', '0', kind='operand', line=3159)
W('31,3141', 0o65345, '', 'DLOAD', 'PDDL', 'PUSH 0-1 = -AYO SCALED B0', kind='interp', line=3160)
W('31,3142', 0o01714, '', '', '-AYO', kind='operand', line=3161)
W('31,3143', 0o01716, '', '', 'AXO', kind='operand', line=3162)
W('31,3144', 0o63325, '', 'PDDL', 'PDVL', 'PUSH 2-3 = +AX SCALED B0', kind='interp', line=3163)
W('31,3145', 0o15343, '', '', 'DPPOSMAX', kind='operand', line=3164)
W('31,3146', 0o02617, '', '', 'US', kind='operand', line=3165)
W('31,3147', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=3166)
W('31,3150', 0o03627, '', '', 'RZC', kind='operand', line=3167)
W('31,3151', 0o27621, '', 'STOVL', 'UBAR2', kind='interp', line=3168)
W('31,3152', 0o53435, '', 'VXV', 'UNIT', 'PUSH UP', kind='interp', line=3169)
W('31,3153', 0o03621, '', '', 'UBAR2', kind='operand', line=3170)
W('31,3154', 0o27605, '', 'STOVL', 'UBAR0', kind='interp', line=3171)
W('31,3155', 0o03621, '', '', 'UBAR2', kind='operand', line=3172)
W('31,3156', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=3173)
W('31,3157', 0o03605, '', '', 'UBAR0', kind='operand', line=3174)
W('31,3160', 0o03613, '', 'STORE', 'UBAR1', kind='interp', line=3175)
W('31,3161', 0o50214, '', 'BON', 'DOT', kind='interp', line=3176)
W('31,3162', 0o01703, '', '', 'LUNAFLAG', kind='operand', line=3177)
W('31,3163', 0o63361, '', '', 'HORIZ.6', kind='operand', line=3178)
W('31,3164', 0o00001, '', '', '0', 'UBAR1 DOT UZ', kind='operand', line=3179)
W('31,3165', 0o36156, '', 'STCALL', 'ALPHAV +4', kind='interp', line=3180)
W('31,3166', 0o26505, '', '', 'GETERAD', kind='operand', line=3181)
W('31,3167', 0o65215, '', 'DAD', 'PDDL', 'MPAC HAS RADIUS OF FISCHER ELLIPSOID', kind='interp', line=3182)
W('31,3170', 0o01355, '', '', 'HORIZALT', 'PUSH 0-1 = BH SCALED B29', kind='operand', line=3183)
W('31,3171', 0o23441, '', '', 'AEARTH', kind='operand', line=3184)
W('31,3172', 0o41415, '', 'DAD', 'PUSH', 'PUSH 2-3 = AH B29', kind='interp', line=3185)
W('31,3173', 0o01355, '', '', 'HORIZALT', kind='operand', line=3186)
W('31,3174', 0o64375, 'HORIZ.1', 'VLOAD', 'MXV', kind='interp', line=3187)
W('31,3175', 0o03627, '', '', 'RZC', 'B29', kind='operand', line=3188)
W('31,3176', 0o03605, '', '', 'UBAR0', 'B1', kind='operand', line=3189)
W('31,3177', 0o63372, '', 'VSL1', 'PDVL', 'PUSH 4-9 = RH(XH,YH,ZH) B29', kind='interp', line=3190)
W('31,3200', 0o02617, '', '', 'US', kind='operand', line=3191)
W('31,3201', 0o76521, '', 'MXV', 'VSL1', kind='interp', line=3192)
W('31,3202', 0o03605, '', '', 'UBAR0', kind='operand', line=3193)
W('31,3203', 0o77725, '', 'PDDL', '', 'PUSH 10-15 = USH B1', kind='interp', line=3194)
W('31,3204', 0o00003, '', '', '2', 'AH', kind='operand', line=3195)
W('31,3205', 0o14043, '', 'STODL', '34D', kind='interp', line=3196)
W('31,3206', 0o00005, '', '', '4', 'XH', kind='operand', line=3197)
W('31,3207', 0o77624, '', 'CALL', kind='interp', line=3198)
W('31,3210', 0o63365, '', '', 'DIVIDE', kind='operand', line=3199)
W('31,3211', 0o41257, '', 'SR*', 'DMP', kind='interp', line=3200)
W('31,3212', 0o20611, '', '', '8D,1', 'NOW SCALED B9', kind='operand', line=3201)
W('31,3213', 0o00155, '', '', 'MPAC', kind='operand', line=3202)
W('31,3214', 0o14037, '', 'STODL', '30D', kind='interp', line=3203)
W('31,3215', 0o00001, '', '', '0', kind='operand', line=3204)
# Page 628
W('31,3216', 0o14043, '', 'STODL', '34D', kind='interp', line=3206)
W('31,3217', 0o00007, '', '', '6', 'YH', kind='operand', line=3207)
W('31,3220', 0o77624, '', 'CALL', kind='interp', line=3208)
W('31,3221', 0o63365, '', '', 'DIVIDE', kind='operand', line=3209)
W('31,3222', 0o41257, '', 'SR*', 'DMP', kind='interp', line=3210)
W('31,3223', 0o20611, '', '', '8D,1', 'B9', kind='operand', line=3211)
W('31,3224', 0o00155, '', '', 'MPAC', 'B18', kind='operand', line=3212)
W('31,3225', 0o41415, '', 'DAD', 'PUSH', 'PUSH 16-17 =A SCALED B18', kind='interp', line=3213)
W('31,3226', 0o00037, '', '', '30D', kind='operand', line=3214)
W('31,3227', 0o75425, '', 'DSU', 'SQRT', kind='interp', line=3215)
W('31,3230', 0o23447, '', '', '1.0B18', kind='operand', line=3216)
W('31,3231', 0o77725, '', 'PDDL', '', 'PUSH 18-19 SQRT(A-1) B9', kind='interp', line=3217)
W('31,3232', 0o00021, '', '', '16D', kind='operand', line=3218)
W('31,3233', 0o14043, '', 'STODL', '34D', kind='interp', line=3219)
W('31,3234', 0o00005, '', '', '4', 'XH', kind='operand', line=3220)
W('31,3235', 0o77624, '', 'CALL', kind='interp', line=3221)
W('31,3236', 0o63365, '', '', 'DIVIDE', kind='operand', line=3222)
W('31,3237', 0o65257, '', 'SR*', 'PDDL', kind='interp', line=3223)
W('31,3240', 0o20622, '', '', '17D,1', 'PUSH 20-21 = XH/A B29', kind='operand', line=3224)
W('31,3241', 0o00007, '', '', '6', 'YH', kind='operand', line=3225)
W('31,3242', 0o77624, '', 'CALL', kind='interp', line=3226)
W('31,3243', 0o63365, '', '', 'DIVIDE', kind='operand', line=3227)
W('31,3244', 0o65257, '', 'SR*', 'PDDL', kind='interp', line=3228)
W('31,3245', 0o20622, '', '', '17D,1', 'PUSH 22-23 = YH/A B29', kind='operand', line=3229)
W('31,3246', 0o00021, '', '', '16D', 'A', kind='operand', line=3230)
W('31,3247', 0o14043, '', 'STODL', '34D', kind='interp', line=3231)
W('31,3250', 0o00023, '', '', '18D', 'SQRT(A-1)', kind='operand', line=3232)
W('31,3251', 0o77624, '', 'CALL', kind='interp', line=3233)
W('31,3252', 0o63365, '', '', 'DIVIDE', kind='operand', line=3234)
W('31,3253', 0o77657, '', 'SR*', kind='interp', line=3235)
W('31,3254', 0o20611, '', '', '8D,1', kind='operand', line=3236)
W('31,3255', 0o14035, '', 'STODL', '28D', kind='interp', line=3237)
W('31,3256', 0o00001, '', '', '0', 'BH', kind='operand', line=3238)
W('31,3257', 0o14043, '', 'STODL', '34D', kind='interp', line=3239)
W('31,3260', 0o00003, '', '', '2', 'AH', kind='operand', line=3240)
W('31,3261', 0o77624, '', 'CALL', kind='interp', line=3241)
W('31,3262', 0o63365, '', '', 'DIVIDE', kind='operand', line=3242)
W('31,3263', 0o41257, '', 'SR*', 'DMP', 'AH/BH SCALED B1', kind='interp', line=3243)
W('31,3264', 0o20601, '', '', '0,1', kind='operand', line=3244)
W('31,3265', 0o00035, '', '', '28D', 'SQRT(A-1)/A', kind='operand', line=3245)
W('31,3266', 0o72405, '', 'DMP', 'SL1', kind='interp', line=3246)
W('31,3267', 0o00007, '', '', '6', 'YH', kind='operand', line=3247)
W('31,3270', 0o77725, '', 'PDDL', kind='interp', line=3248)
W('31,3271', 0o00003, '', '', '2', 'AH', kind='operand', line=3249)
W('31,3272', 0o14043, '', 'STODL', '34D', kind='interp', line=3250)
W('31,3273', 0o00001, '', '', '0', kind='operand', line=3251)
W('31,3274', 0o77624, '', 'CALL', kind='interp', line=3252)
W('31,3275', 0o63365, '', '', 'DIVIDE', kind='operand', line=3253)
W('31,3276', 0o41257, '', 'SR*', 'DMP', 'BH/AH SCALED B1', kind='interp', line=3254)
W('31,3277', 0o20601, '', '', '0,1', kind='operand', line=3255)
# Page 629
W('31,3300', 0o00035, '', '', '28D', 'SQRT (A-1)/A', kind='operand', line=3257)
W('31,3301', 0o72405, '', 'DMP', 'SL1', kind='interp', line=3258)
W('31,3302', 0o00005, '', '', '4', 'XH', kind='operand', line=3259)
W('31,3303', 0o43325, '', 'PDDL', 'DAD', kind='interp', line=3260)
W('31,3304', 0o00025, '', '', '20D', 'XH/A', kind='operand', line=3261)
W('31,3305', 0o00031, '', '', '24D', 'ALPHA', kind='operand', line=3262)
W('31,3306', 0o45325, '', 'PDDL', 'DSU', kind='interp', line=3263)
W('31,3307', 0o00027, '', '', '22D', 'YH/A', kind='operand', line=3264)
W('31,3310', 0o00033, '', '', '26D', 'BETA', kind='operand', line=3265)
W('31,3311', 0o40206, '', 'PUSH', 'SETPD', kind='interp', line=3266)
W('31,3312', 0o00021, '', '', '16D', kind='operand', line=3267)
W('31,3313', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=3268)
W('31,3314', 0o00025, '', '', '20D', 'XH/A', kind='operand', line=3269)
W('31,3315', 0o00031, '', '', '24D', 'ALPHA', kind='operand', line=3270)
W('31,3316', 0o43325, '', 'PDDL', 'DAD', kind='interp', line=3271)
W('31,3317', 0o00027, '', '', '22D', 'YH/A', kind='operand', line=3272)
W('31,3320', 0o00033, '', '', '26D', 'BETA', kind='operand', line=3273)
W('31,3321', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=3274)
W('31,3322', 0o15335, '', '', 'ZEROVECS', kind='operand', line=3275)
W('31,3323', 0o24041, '', 'STOVL', '32D', 'ZERO THIRD COMP. OF T-0 VECTOR', kind='interp', line=3276)
W('31,3324', 0o00035, '', '', '28D', kind='operand', line=3277)
W('31,3325', 0o53451, '', 'VSU', 'UNIT', kind='interp', line=3278)
W('31,3326', 0o00005, '', '', '4', 'RH VECTOR', kind='operand', line=3279)
W('31,3327', 0o63241, '', 'DOT', 'PDVL', 'PUSH 22-23 A-SUB-ZERO', kind='interp', line=3280)
W('31,3330', 0o00013, '', '', '10D', 'USH VECTOR', kind='operand', line=3281)
W('31,3331', 0o00021, '', '', '16D', 'T1 VECTOR', kind='operand', line=3282)
W('31,3332', 0o53451, '', 'VSU', 'UNIT', kind='interp', line=3283)
W('31,3333', 0o00005, '', '', '4', 'RH VECTOR', kind='operand', line=3284)
W('31,3334', 0o41441, '', 'DOT', 'PUSH', 'PUSH 24-25 A-SUB-ONE', kind='interp', line=3285)
W('31,3335', 0o00013, '', '', '10D', kind='operand', line=3286)
W('31,3336', 0o50021, '', 'BDSU', 'BMN', kind='interp', line=3287)
W('31,3337', 0o00027, '', '', '22D', 'A-SUB-ZERO', kind='operand', line=3288)
W('31,3340', 0o63347, '', '', 'HORIZ.3', kind='operand', line=3289)
W('31,3341', 0o77614, '', 'BON', kind='interp', line=3290)
W('31,3342', 0o00304, '', '', 'NORFHOR', kind='operand', line=3291)
W('31,3343', 0o63353, '', '', 'HORIZ.4', kind='operand', line=3292)
W('31,3344', 0o52175, 'HORIZ.2', 'VLOAD', 'GOTO', kind='interp', line=3293)
W('31,3345', 0o00035, '', '', '28D', 'T-0 VECTOR', kind='operand', line=3294)
W('31,3346', 0o63355, '', '', 'HORIZ.5', kind='operand', line=3295)
W('31,3347', 0o52014, 'HORIZ.3', 'BON', 'GOTO', kind='interp', line=3296)
W('31,3350', 0o00304, '', '', 'NORFHOR', kind='operand', line=3297)
W('31,3351', 0o63344, '', '', 'HORIZ.2', kind='operand', line=3298)
W('31,3352', 0o63353, '', '', 'HORIZ.4', kind='operand', line=3299)
W('31,3353', 0o77775, 'HORIZ.4', 'VLOAD', kind='interp', line=3300)
W('31,3354', 0o00021, '', '', '16D', 'T1 VECTOR', kind='operand', line=3301)
W('31,3355', 0o76505, 'HORIZ.5', 'VXM', 'VSL1', kind='interp', line=3302)
W('31,3356', 0o03605, '', '', 'UBAR0', kind='operand', line=3303)
W('31,3357', 0o77650, '', 'GOTO', kind='interp', line=3304)
W('31,3360', 0o03656, '', '', 'SRRETURN', kind='operand', line=3305)
W('31,3361', 0o41545, 'HORIZ.6', 'DLOAD', 'PUSH', kind='interp', line=3306)
# Page 630
W('31,3362', 0o23443, '', '', 'RADMOON', kind='operand', line=3308)
W('31,3363', 0o52006, '', 'PUSH', 'GOTO', kind='interp', line=3309)
W('31,3364', 0o63174, '', '', 'HORIZ.1', kind='operand', line=3310)
W('31,3365', 0o70501, 'DIVIDE', 'NORM', 'SR1', kind='interp', line=3311)
W('31,3366', 0o00047, '', '', 'X1', kind='operand', line=3312)
W('31,3367', 0o14045, '', 'STODL', '36D', kind='interp', line=3313)
W('31,3370', 0o00043, '', '', '34D', kind='operand', line=3314)
W('31,3371', 0o55301, '', 'NORM', 'BDDV', kind='interp', line=3315)
W('31,3372', 0o00051, '', '', 'S1', kind='operand', line=3316)
W('31,3373', 0o00045, '', '', '36D', kind='operand', line=3317)
W('31,3374', 0o43460, '', 'XSU,1', 'RVQ', kind='interp', line=3318)
W('31,3375', 0o00050, '', '', 'S1', kind='operand', line=3319)
W('31,3376', 0o77014, 'RECT.1', 'BOFF', 'AXT,2', 'SR TO SET ZMEASURE = 0 IF MEASUREMENT', kind='interp', line=3320)
W('31,3377', 0o04343, '', '', 'CMOONFLG', '  PLANET AND PRIMARY PLANET ARE THE SAME.', kind='operand', line=3321)
W('31,3400', 0o63410, '', '', 'RECT.3', '    OTHERWISE = 1', kind='operand', line=3322)
W('31,3401', 0o77775, '', 'DEC', '-2', kind='data', line=3323)
W('31,3402', 0o77614, '', 'BOFF', '', '      VEC. AND SCALE B29 AND B7', kind='interp', line=3324)
W('31,3403', 0o01743, '', '', 'LUNAFLAG', kind='operand', line=3325)
W('31,3404', 0o63414, '', '', 'RECT.4', kind='operand', line=3326)
W('31,3405', 0o52014, 'RECT.2', 'CLEAR', 'GOTO', kind='interp', line=3327)
W('31,3406', 0o00265, '', '', 'ZMEASURE', kind='operand', line=3328)
W('31,3407', 0o63416, '', '', 'RECT.5', kind='operand', line=3329)
W('31,3410', 0o43174, 'RECT.3', 'AXT,2', 'BOFF', kind='interp', line=3330)
W('31,3411', 0o00000, '', '', '0', kind='operand', line=3331)
W('31,3412', 0o01743, '', '', 'LUNAFLAG', kind='operand', line=3332)
W('31,3413', 0o63405, '', '', 'RECT.2', kind='operand', line=3333)
W('31,3414', 0o77614, 'RECT.4', 'SET', kind='interp', line=3334)
W('31,3415', 0o00065, '', '', 'ZMEASURE', kind='operand', line=3335)
W('31,3416', 0o44575, 'RECT.5', 'VLOAD', 'VSR7', kind='interp', line=3336)
W('31,3417', 0o01573, '', '', 'DELTACSM', 'SCALED B22 OR B18', kind='operand', line=3337)
W('31,3420', 0o53257, '', 'VSR*', 'VAD', kind='interp', line=3338)
W('31,3421', 0o57176, '', '', '0,2', kind='operand', line=3339)
W('31,3422', 0o01607, '', '', 'RCVCSM', 'SCALED B29 OR B27', kind='operand', line=3340)
W('31,3423', 0o77657, '', 'VSR*', kind='interp', line=3341)
W('31,3424', 0o57176, '', '', '0,2', kind='operand', line=3342)
W('31,3425', 0o27627, '', 'STOVL', 'RZC', 'NOW SCALED B29', kind='interp', line=3343)
W('31,3426', 0o01601, '', '', 'NUVCSM', 'SCALED B3 OR B-1', kind='operand', line=3344)
W('31,3427', 0o53702, '', 'VSR4', 'VSR*', kind='interp', line=3345)
W('31,3430', 0o57176, '', '', '0,2', kind='operand', line=3346)
W('31,3431', 0o53655, '', 'VAD', 'VSR*', kind='interp', line=3347)
W('31,3432', 0o01615, '', '', 'VCVCSM', 'SCALED B7 OR B5', kind='operand', line=3348)
W('31,3433', 0o57176, '', '', '0,2', kind='operand', line=3349)
W('31,3434', 0o03635, '', 'STORE', 'VZC', 'NOW SCALED B7', kind='interp', line=3350)
W('31,3435', 0o77616, '', 'RVQ', kind='interp', line=3351)
W('31,3436', 0o26305, 'ONE/C', '2DEC*', '.333564049 E-6 B+21*', kind='data', line=3352)
W('31,3437', 0o05432, kind='data', line=3352)

W('31,3440', 0o00302, 'AEARTH', '2DEC', '6378166 B-29', 'A AXIS OF EARTH (METERS B-29)', kind='data', line=3354)
W('31,3441', 0o24533, kind='data', line=3354)

W('31,3442', 0o00065, 'RADMOON', '2DEC', '1738090 B-29', 'RADIUS MOON IN METERS', kind='data', line=3356)
W('31,3443', 0o01265, kind='data', line=3356)

# Page 631

W('31,3444', 0o01604, 'TRUN19', 'OCT', '01604', kind='data', line=3360)
W('31,3445', 0o00000, 'TRUN19A', 'OCT', '00000', kind='data', line=3361)
W('31,3446', 0o00000, '1.0B18', '2DEC', '1.0 B-18', kind='data', line=3362)
W('31,3447', 0o02000, kind='data', line=3362)

W('31,3450', 0o00000, 'VARSUBL', 'DEC', '0', kind='data', line=3364)
W('31,3451', 0o01505, 'VARSUBL3', '2DEC*', '3.4299040 E+6 B-26*', kind='data', line=3365)
W('31,3452', 0o14100, kind='data', line=3365)

W('31,3453', 0o00012, 'TRUNVAR', '2DEC', '2.5 E-9 B+18', kind='data', line=3367)
W('31,3454', 0o27462, kind='data', line=3367)

W('31,3455', 0o01461, 'V6N49', 'VN', '0649', kind='data', line=3369)
W('31,3456', 0o01306, 'V05N70', 'VN', '0570', kind='data', line=3370)
W('31,3457', 0o01307, 'V05N71', 'VN', '0571', kind='data', line=3371)
W('31,3460', 0o00077, 'OCT00077', 'OCT', '00077', kind='data', line=3372)
W('31,3461', 0o00202, 'V50N25P', 'OCT', '00202', kind='data', line=3373)
W('31,3462', 0o00006, 'SPSIX', 'OCT', '00006', kind='data', line=3374)
W('31,3463', 0o10464, 'JCAXIS', '2DEC', '.2688190620', '1/2(SIN 32.523 DEG)  TRACK AXIS', kind='data', line=3375)
W('31,3464', 0o12467, kind='data', line=3375)

W('31,3465', 0o00000, '', '2DEC', '0', kind='data', line=3377)
W('31,3466', 0o00000, kind='data', line=3377)

W('31,3467', 0o15373, '', '2DEC', '.4215878460', '1/2(COS 32.523 DEG)', kind='data', line=3379)
W('31,3470', 0o11346, kind='data', line=3379)

W('31,3471', 0o62622, 'R60ADRS', 'CADR', 'R60CALL +3', kind='data', line=3381)
W('31,3472', 0o77732, 'NEG37', 'DEC', '-37', kind='data', line=3382)
W('31,3473', 0o00700, 'BITS7-9', 'OCT', '700', kind='data', line=3383)
W('31,3474', 0o00070, 'BITS4-6', 'OCT', '70', kind='data', line=3384)
#   SETLOC RT53
#   BANK
W('14,2000', 0o43573, 'LOWMEMRY', 'VLOAD*', 'RVQ', kind='interp', line=3387)
W('14,2001', 0o31761, '', '', 'CATLOG,1', kind='operand', line=3388)
#   BANK 37
#   SETLOC P23S1
#   BANK
W('16,2000', 0o77776, 'LDPLANET', 'EXIT', '', 'KEEP THIS OPEN SUBROUTINE IN EBANK=5', kind='interp', line=3392)
W('16,2001', 0o32017, '', 'CAF', 'VNPLAN23', 'BECAUSE STAR IS EBANK=5', line=3393)
W('16,2002', 0o04662, '', 'TC', 'BANKCALL', 'LDPLANET ALLOWS VECTOR TO PLANET TO BE', line=3394)
W('16,2003', 0o20720, '', 'CADR', 'GOFLASH', 'STORED IN STARSAV2 IF STORED STARS ARE', kind='data', line=3395)
W('16,2004', 0o04106, '', 'TC', 'GOTOPOOH', 'NOT VISIBLE', line=3396)
W('16,2005', 0o02007, '', 'TC', '+2', line=3397)
W('16,2006', 0o02001, '', 'TC', '-5', line=3398)
W('16,2007', 0o06006, '', 'TC', 'INTPRET', line=3399)
W('16,2010', 0o77775, '', 'VLOAD', kind='interp', line=3400)
W('16,2011', 0o03705, '', '', 'STARSAV3', kind='operand', line=3401)
W('16,2012', 0o53561, '', 'VXSC', 'UNIT', kind='interp', line=3402)
W('16,2013', 0o32433, '', '', '1/SQR3', kind='operand', line=3403)
W('16,2014', 0o02617, '', 'STORE', 'STARSAV2', kind='interp', line=3404)
W('16,2015', 0o77650, '', 'GOTO', kind='interp', line=3405)
W('16,2016', 0o62563, '', '', 'P23.31', kind='operand', line=3406)
W('16,2017', 0o01530, 'VNPLAN23', 'VN', '0688', kind='data', line=3407)
#   BLOCK 02
W('4622', 0o00006, 'GOTOV56', 'EXTEND', '', 'P20 TERMINATES BY GOTOV56 INSTEAD OF', line=3409)
# Page 632
W('4623', 0o34626, '', 'DCA', 'VB56CADR', '      GOTOPOOH', line=3411)
W('4624', 0o15227, '', 'TCF', 'SUPDXCHZ', line=3412)
#   EBANK= WHOCARES
W('4625', 0o02653, 'VB56CADR', '2CADR', 'TRACKTRM', kind='data', line=3414)
W('4626', 0o66107, kind='data', line=3414)

#   SETLOC FFTAG2
#   BANK
#   COUNT* $$/P20
#   BANK 40
#   SETLOC ENDPINS1
#   BANK
#   COUNT* $$/EXTVB
W('40,3624', 0o06006, 'V67CALL', 'TC', 'INTPRET', line=3423)
W('40,3625', 0o77624, '', 'CALL', kind='interp', line=3424)
W('40,3626', 0o61701, '', '', 'V67WW', kind='operand', line=3425)
W('40,3627', 0o77776, '', 'EXIT', kind='interp', line=3426)
W('40,3630', 0o33763, 'V06N99DS', 'CAF', 'V06N99A', line=3427)
W('40,3631', 0o04662, '', 'TC', 'BANKCALL', line=3428)
W('40,3632', 0o20561, '', 'CADR', 'GOXDSPF', kind='data', line=3429)
W('40,3633', 0o15534, '', 'TCF', 'ENDEXT', line=3430)
W('40,3634', 0o03636, '', 'TC', 'V06N9933', line=3431)
W('40,3635', 0o03630, '', 'TC', 'V06N99DS', line=3432)
W('40,3636', 0o06006, 'V06N9933', 'TC', 'INTPRET', line=3433)
W('40,3637', 0o46135, '', 'SLOAD', 'BHIZ', 'IF R3 OF V67 = 0 EXIT', kind='interp', line=3434)
W('40,3640', 0o02325, '', '', 'WWOPT', kind='operand', line=3435)
W('40,3641', 0o61644, '', '', '+3', kind='operand', line=3436)
W('40,3642', 0o77650, '', 'GOTO', kind='interp', line=3437)
W('40,3643', 0o61646, '', '', 'V6N99INP', kind='operand', line=3438)
W('40,3644', 0o77776, '', 'EXIT', kind='interp', line=3439)
W('40,3645', 0o15534, '', 'TCF', 'ENDEXT', line=3440)
W('40,3646', 0o73150, 'V6N99INP', 'LXA,1', 'LXA,2', kind='interp', line=3441)
W('40,3647', 0o02320, '', '', 'WWPOS', kind='operand', line=3442)
W('40,3650', 0o02322, '', '', 'WWVEL', kind='operand', line=3443)
W('40,3651', 0o45335, '', 'SLOAD', 'DSU', kind='interp', line=3444)
W('40,3652', 0o02325, '', '', 'WWOPT', kind='operand', line=3445)
W('40,3653', 0o21767, '', '', 'V67DEC2', kind='operand', line=3446)
W('40,3654', 0o51030, '', 'BHIZ', 'BPL', kind='interp', line=3447)
W('40,3655', 0o61664, '', '', 'V67WORB', kind='operand', line=3448)
W('40,3656', 0o61671, '', '', 'V67WMID', kind='operand', line=3449)
W('40,3657', 0o67130, '', 'SXA,1', 'SXA,2', kind='interp', line=3450)
W('40,3660', 0o02000, '', '', 'WRENDPOS', kind='operand', line=3451)
W('40,3661', 0o02001, '', '', 'WRENDVEL', kind='operand', line=3452)
W('40,3662', 0o77650, '', 'GOTO', kind='interp', line=3453)
W('40,3663', 0o61674, '', '', 'V67EXITX', kind='operand', line=3454)
W('40,3664', 0o67130, 'V67WORB', 'SXA,1', 'SXA,2', kind='interp', line=3455)
W('40,3665', 0o02004, '', '', 'WORBPOS', kind='operand', line=3456)
W('40,3666', 0o02005, '', '', 'WORBVEL', kind='operand', line=3457)
W('40,3667', 0o77650, '', 'GOTO', kind='interp', line=3458)
W('40,3670', 0o61674, '', '', 'V67EXITX', kind='operand', line=3459)
W('40,3671', 0o67130, 'V67WMID', 'SXA,1', 'SXA,2', kind='interp', line=3460)
# Page 633
W('40,3672', 0o03000, '', '', 'WMIDPOS', kind='operand', line=3462)
W('40,3673', 0o03001, '', '', 'WMIDVEL', kind='operand', line=3463)
W('40,3674', 0o43014, 'V67EXITX', 'CLEAR', 'CLEAR', kind='interp', line=3464)
W('40,3675', 0o01671, '', '', 'ORBWFLAG', kind='operand', line=3465)
W('40,3676', 0o02676, '', '', 'RENDWFLG', kind='operand', line=3466)
W('40,3677', 0o77776, '', 'EXIT', kind='interp', line=3467)
W('40,3700', 0o15534, '', 'TCF', 'ENDEXT', line=3468)
W('40,3701', 0o40020, 'V67WW', 'STQ', 'BOV', kind='interp', line=3469)
W('40,3702', 0o00051, '', '', 'S2', kind='operand', line=3470)
W('40,3703', 0o61704, '', '', '+1', kind='operand', line=3471)
W('40,3704', 0o77624, '', 'CALL', kind='interp', line=3472)
W('40,3705', 0o27442, '', '', 'INTSTALL', kind='operand', line=3473)
W('40,3706', 0o71331, '', 'SSP', 'DLOAD', kind='interp', line=3474)
W('40,3707', 0o00051, '', '', 'S1', kind='operand', line=3475)
W('40,3710', 0o00006, '', 'DEC', '6', kind='data', line=3476)
W('40,3711', 0o15335, '', '', 'ZEROVECS', kind='operand', line=3477)
W('40,3712', 0o02321, '', 'STORE', 'WWPOS', kind='interp', line=3478)
W('40,3713', 0o02323, '', 'STORE', 'WWVEL', kind='interp', line=3479)
W('40,3714', 0o02325, '', 'STORE', 'WWOPT', kind='interp', line=3480)
W('40,3715', 0o77770, '', 'AXT,1', kind='interp', line=3481)
W('40,3716', 0o00044, '', 'DEC', '36', kind='data', line=3482)
W('40,3717', 0o47573, 'NXPOSVEL', 'VLOAD*', 'VSQ', kind='interp', line=3483)
W('40,3720', 0o02445, '', '', 'W +36D,1', kind='operand', line=3484)
W('40,3721', 0o77615, '', 'DAD', kind='interp', line=3485)
W('40,3722', 0o02321, '', '', 'WWPOS', kind='operand', line=3486)
W('40,3723', 0o02321, '', 'STORE', 'WWPOS', kind='interp', line=3487)
W('40,3724', 0o47573, '', 'VLOAD*', 'VSQ', kind='interp', line=3488)
W('40,3725', 0o02533, '', '', 'W +90D,1', kind='operand', line=3489)
W('40,3726', 0o77615, '', 'DAD', kind='interp', line=3490)
W('40,3727', 0o02323, '', '', 'WWVEL', kind='operand', line=3491)
W('40,3730', 0o02323, '', 'STORE', 'WWVEL', kind='interp', line=3492)
W('40,3731', 0o75500, '', 'TIX,1', 'SQRT', kind='interp', line=3493)
W('40,3732', 0o61717, '', '', 'NXPOSVEL', kind='operand', line=3494)
W('40,3733', 0o16323, '', 'STODL', 'WWVEL', kind='interp', line=3495)
W('40,3734', 0o02321, '', '', 'WWPOS', kind='operand', line=3496)
W('40,3735', 0o77766, '', 'SQRT', kind='interp', line=3497)
W('40,3736', 0o02321, '', 'STORE', 'WWPOS', kind='interp', line=3498)
W('40,3737', 0o52000, '', 'BOV', 'GOTO', kind='interp', line=3499)
W('40,3740', 0o61742, '', '', '+2', kind='operand', line=3500)
W('40,3741', 0o61746, '', '', 'V67XXX', kind='operand', line=3501)
W('40,3742', 0o77745, '', 'DLOAD', kind='interp', line=3502)
W('40,3743', 0o15343, '', '', 'DPPOSMAX', kind='operand', line=3503)
W('40,3744', 0o02321, '', 'STORE', 'WWPOS', kind='interp', line=3504)
W('40,3745', 0o02323, '', 'STORE', 'WWVEL', kind='interp', line=3505)
W('40,3746', 0o45345, 'V67XXX', 'DLOAD', 'DSU', kind='interp', line=3506)
W('40,3747', 0o02321, '', '', 'WWPOS', kind='operand', line=3507)
W('40,3750', 0o21765, '', '', 'FT99999', kind='operand', line=3508)
W('40,3751', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=3509)
W('40,3752', 0o61755, '', '', '+3', kind='operand', line=3510)
W('40,3753', 0o21765, '', '', 'FT99999', kind='operand', line=3511)
# Page 634
W('40,3754', 0o02321, '', 'STORE', 'WWPOS', kind='interp', line=3513)
W('40,3755', 0o66150, '', 'LXA,1', 'SXA,1', kind='interp', line=3514)
W('40,3756', 0o00051, '', '', 'S2', kind='operand', line=3515)
W('40,3757', 0o00052, '', '', 'QPRET', kind='operand', line=3516)
W('40,3760', 0o77776, '', 'EXIT', kind='interp', line=3517)
W('40,3761', 0o04701, '', 'TC', 'POSTJUMP', line=3518)
W('40,3762', 0o27457, '', 'CADR', 'INTWAKE', kind='data', line=3519)
S('WWPOS', 'equals', 0o2320, line=3520)
S('WWVEL', 'equals', 0o2322, line=3521)
S('WWOPT', 'equals', 0o2324, line=3522)
W('40,3763', 0o01543, 'V06N99A', 'VN', '0699', kind='data', line=3523)
W('40,3764', 0o01670, 'FT99999', '2DEC', '30479 B-19', kind='data', line=3524)
W('40,3765', 0o17000, kind='data', line=3524)

W('40,3766', 0o00002, 'V67DEC2', '2DEC', '2 B-14', kind='data', line=3526)
W('40,3767', 0o00000, kind='data', line=3526)

#   SBANK= LOWSUPER
