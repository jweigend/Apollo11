"""P51-P53.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P51-P53.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 926-983 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P51_P53', 'P51-P53.agc', 'Luminary099', pages='926-983')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P51-P53.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        926-983
# Mod history:  2009-05-31 HG   Transcribed from page images.
# 2009-06-07 RSB  Corrected a typo.
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

# Page 926
# PROGRAM NAME -- PROG52                        DATE -- JAN 9, 1967
# MOD NO -- 0                                   LOG SECTION -- P51-P53
# MODIFICATION BY -- LONSKE                     ASSEMBLY -- SUNDANCE REV 46
#
# FUNCTIONAL DESCRIPTION --
#
# ALIGNS THE IMU TO ONE OF THREE ORIENTATIONS SELECTED BY THE ASTRONAUT.  THE PRESENT IMU ORIENTATION IS KNOWN
# AND IS STORED IN REFSMMAT.  THE THREE POSSIBLE ORIENTATIONS MAY BE:
#
# (A)     PREFERRED ORIENTATION
#
# AN OPTIMUM ORIENTATION FOR A PREVIOUSLY CALCULATED MANEUVER.  THIS ORIENTATION MUST BE CALCULATED AND
# STORED BY A PREVIOUSLY SELECTED PROGRAM.
#
# (B)     NOMINAL ORIENTATION
#
# X   = UNIT ( R )
# -SM
#
# Y   = UNIT (V X R)
# SM
#
# Z   = UNIT (X   X Y  )
# SM          SM    SM
#
# WHERE:
#
# R = THE GEOCENTRIC RADIUS VECTOR AT TIME T(ALIGN) SELECTED BY THE ASTRONAUT
# -
#
# V = THE INERTIAL VELOCITY VECTOR AT TIME T(ALIGN) SELECTED BY THE ASTRONAUT
# -
#
# (C)     RERSMMAT ORIENTATION
#
# (D)     LANDING SITE -- THIS IS NOT AVAILABLE IN SUNDANCE
#
# THIS SELECTION CORRECTS THE PRESENT IMU ORIENTATION.  THE PRESENT ORIENTATION DIFFERS FROM THAT TO WHICH IT
# WAS LAST ALIGNED ONLY DUE TO GYRO DRIFT (I.E., NEITHER GIMBAL LOCK NOR IMU POWER INTERRUPTION HAS OCCURRED
# SINCE THE LAST ALIGNMENT).
#
# AFTER A IMU ORIENTATION HAS BEEN SELECTED ROUTINE S52.2 IS OPERATED TO COMPUTE THE GIMBAL ANGLES USING THE
# NEW ORIENTATION AND THE PRESENT VEHICLE ATTITUDE.  CAL52A THEN USES THESE ANGLES, STORED IN THETAD,+1,+2, TO
# COARSE ALIGN THE IMU.  THE STARS SELECTION ROUTINE, R56, IS THEN OPERATED.  IF 2 STARS ARE NOT AVAILABLE AN ALARM
# IS FLASHED TO NOTIFY THE ASTRONAUT.  AT THIS POINT THE ASTRONAUT WILL MANEUVER THE VEHICLE AND SELECT 2 STARS
# EITHER MANUALLY OR AUTOMATICALLY.  AFTER 2 STARS HAVE BEEN SELECTED THE IMU IS FINE ALIGNED USING ROUTINE R51.  IF
# THE RENDEZVOUS NAVIGATION PROCESS IS OPERATING (INDICATED BY RNDVZFLG) P20 IS DISPLAYED.  OTHERWISE P00 IS
# REQUESTED.
#
# CALLING SEQUENCE --
#
# Page 927
# THE PROGRAM IS CALLED BY THE ASTRONAUT BY DSKY ENTRY.
#
# SUBROUTINES CALLED --
#
# 1. FLAGDOWN              7. S52.2               13. NEWMODEX
# 2. R02BOTH               8. CAL53A              14. PRIOLARM
# 3. GOPERF4               9. FLAGUP
# 4. MATMOVE              10. R56
# 5. GOFLASH              11. R51
# 6. S52.3                12. GOPERF3
#
# NORMAL EXIT MODES --
#
# EXITS TO ENDOFJOB
#
# ALARM OR ABORT EXIT MODES --
#
# NONE
#
# OUTPUT --
#
# THE FOLLOWING MAY BE FLASHED ON THE DSKY
# 1. IMU ORIENTATION CODE
# 2. ALARM CODE 215 -- PREFERRED IMU ORIENTATION NOT SPECIFIED
# 3. TIME OF NEXT IGNITION
# 4. GIMBAL ANGLES
# 5. ALARM CODE 405 -- TWO STARS NOT AVAILABLE
# 6. PLEASE PERFORM P00
# THE MODE DISPLAY MAY BE CHANGED TO 20
#
# ERASABLE INITIALIZATION REQUIRED --
#
# PFRATFLG SHOULD BE SET IF A PREFERRED ORIENTATION HAS BEEN COMPUTED.  IF IT HAS BEEN COMPUTED IT IS STORED IN
# XSMD, YSMD, ZSMD.
#
# RNDVZFLG INDICATES WHETHER THE RENDEZVOUS NAVIGATION PROCESS IS OPERATING.
#
# DEBRIS --
#
# WORK AREA

#   BANK 33
#   SETLOC P50S
#   BANK

#   EBANK= BESTI
#   COUNT* $$/P52
W('15,2050', 0o04616, 'PROG52', 'TC', 'BANKCALL', line=128)
W('15,2051', 0o11254, '', 'CADR', 'R02BOTH', 'IMU STATUS CHECK', kind='data', line=129)
W('15,2052', 0o34750, '', 'CAF', 'PFRATBIT', line=130)
W('15,2053', 0o70076, '', 'MASK', 'FLAGWRD2', 'IS PFRATFLG SET?', line=131)
W('15,2054', 0o10000, '', 'CCS', 'A', line=132)
# Page 928
W('15,2055', 0o02060, '', 'TC', 'P52A', 'YES', line=134)
W('15,2056', 0o34752, '', 'CAF', 'BIT2', 'NO', line=135)
W('15,2057', 0o02061, '', 'TC', 'P52A +1', line=136)
W('15,2060', 0o34753, 'P52A', 'CAF', 'BIT1', line=137)
W('15,2061', 0o55145, '', 'TS', 'OPTION2', line=138)
W('15,2062', 0o34753, 'P52B', 'CAF', 'BIT1', line=139)
W('15,2063', 0o04616, '', 'TC', 'BANKCALL', 'FLASH OPTION CODE AND ORIENTATION CODE', line=140)
W('15,2064', 0o20713, '', 'CADR', 'GOPERF4R', 'FLASH V04N06', kind='data', line=141)
W('15,2065', 0o06001, '', 'TC', 'GOTOPOOH', line=142)
W('15,2066', 0o12073, '', 'TCF', '+5', 'V33 -- PROCEED', line=143)
W('15,2067', 0o02062, '', 'TC', 'P52B', 'NEW CODE -- NEW ORIENTATION CODE INPUT', line=144)
W('15,2070', 0o05353, '', 'TC', 'PHASCHNG', 'DISPLAY RETURN', line=145)
W('15,2071', 0o00014, '', 'OCT', '00014', kind='data', line=146)
W('15,2072', 0o05155, '', 'TC', 'ENDOFJOB', line=147)

W('15,2073', 0o31145, '', 'CA', 'OPTION2', line=149)
W('15,2074', 0o76245, '', 'MASK', 'THREE', line=150)
W('15,2075', 0o50000, '', 'INDEX', 'A', line=151)
W('15,2076', 0o02077, '', 'TC', '+1', line=152)
W('15,2077', 0o12105, '', 'TCF', 'OPT4', 'OPTION 4 LANDING SITE', line=153)
W('15,2100', 0o12153, '', 'TCF', 'P52H', 'OPTION 1 PREFERRED', line=154)
W('15,2101', 0o12110, '', 'TCF', 'P52T', 'OPTION 2 NOMINAL', line=155)
W('15,2102', 0o06037, 'P52E', 'TC', 'INTPRET', 'OPTION 3 REFSMMAT', line=156)
W('15,2103', 0o77650, '', 'GOTO', kind='interp', line=157)
W('15,2104', 0o32164, '', '', 'P52F', 'GO DO R51', kind='operand', line=158)

W('15,2105', 0o00006, 'OPT4', 'EXTEND', line=160)
W('15,2106', 0o31401, '', 'DCA', 'TLAND', 'IF OPTION 4 DISPLAY TLAND', line=161)
W('15,2107', 0o12112, '', 'TCF', 'P52T +2', line=162)

W('15,2110', 0o00006, 'P52T', 'EXTEND', line=164)
W('15,2111', 0o34755, '', 'DCA', 'NEG0', line=165)
W('15,2112', 0o53046, '', 'DXCH', 'DSPTEM1', line=166)
W('15,2113', 0o32170, '', 'CAF', 'V06N34*', line=167)
W('15,2114', 0o04616, '', 'TC', 'BANKCALL', line=168)
W('15,2115', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=169)
W('15,2116', 0o06001, '', 'TC', 'GOTOPOOH', line=170)
W('15,2117', 0o02121, '', 'TC', '+2', line=171)
W('15,2120', 0o02113, '', 'TC', '-5', line=172)
W('15,2121', 0o53046, '', 'DXCH', 'DSPTEM1', line=173)
W('15,2122', 0o00006, '', 'EXTEND', line=174)
W('15,2123', 0o62125, '', 'BZMF', '+2', 'IF TIME ZERO OR NEG USE TIME2', line=175)
W('15,2124', 0o12127, '', 'TCF', '+3', line=176)
W('15,2125', 0o00006, '', 'EXTEND', line=177)
W('15,2126', 0o30025, '', 'DCA', 'TIME2', line=178)
W('15,2127', 0o53775, '', 'DXCH', 'TALIGN', line=179)
W('15,2130', 0o31145, 'P52V', 'CA', 'OPTION2', line=180)
W('15,2131', 0o74752, '', 'MASK', 'BIT2', line=181)
W('15,2132', 0o10000, '', 'CCS', 'A', line=182)
W('15,2133', 0o02137, '', 'TC', 'P52W', line=183)
# Page 929
W('15,2134', 0o06037, '', 'TC', 'INTPRET', 'OPTION 4 -- GET LS ORIENTATION', line=185)
W('15,2135', 0o77650, '', 'GOTO', kind='interp', line=186)
W('15,2136', 0o32220, '', '', 'P52LS', kind='operand', line=187)

# Page 930
W('15,2137', 0o06037, 'P52W', 'TC', 'INTPRET', line=190)
W('15,2140', 0o45145, '', 'DLOAD', 'CALL', 'PICK UP ALIGN TIME', kind='interp', line=191)
W('15,2141', 0o02775, '', '', 'TALIGN', 'COMPUTED NOMINAL IMU', kind='operand', line=192)
W('15,2142', 0o31650, '', '', 'S52.3', '      ORIENTATION', kind='operand', line=193)
W('15,2143', 0o77624, 'P52D', 'CALL', '', 'READ VEHICLE ATTITUDE AND', kind='interp', line=194)
W('15,2144', 0o31617, '', '', 'S52.2', '      COMPUTE GIMBAL ANGLES', kind='operand', line=195)
W('15,2145', 0o77776, '', 'EXIT', kind='interp', line=196)
W('15,2146', 0o35010, '', 'CAF', 'V06N22', line=197)
W('15,2147', 0o04616, '', 'TC', 'BANKCALL', 'DISPLAY GIMBAL ANGLES', line=198)
W('15,2150', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=199)
W('15,2151', 0o06001, '', 'TC', 'GOTOPOOH', line=200)
W('15,2152', 0o12171, '', 'TCF', 'COARSTYP', 'V33 -- PROCEED, SEE IF GYRO TORQUE COARSE', line=201)
W('15,2153', 0o06037, 'P52H', 'TC', 'INTPRET', line=202)
W('15,2154', 0o77650, '', 'GOTO', kind='interp', line=203)
W('15,2155', 0o32143, '', '', 'P52D', kind='operand', line=204)
W('15,2156', 0o06037, 'REGCOARS', 'TC', 'INTPRET', line=205)
W('15,2157', 0o77624, '', 'CALL', '', 'DO COARSE ALIGN', kind='interp', line=206)
W('15,2160', 0o31327, '', '', 'CAL53A', '      ROUTINE', kind='operand', line=207)
W('15,2161', 0o43014, 'COARSRET', 'SET', 'CLEAR', kind='interp', line=208)
W('15,2162', 0o01462, '', '', 'REFSMFLG', kind='operand', line=209)
W('15,2163', 0o01273, '', '', 'PFRATFLG', kind='operand', line=210)
W('15,2164', 0o77624, 'P52F', 'CALL', kind='interp', line=211)
W('15,2165', 0o31015, '', '', 'R51', kind='operand', line=212)
W('15,2166', 0o77776, 'P52OUT', 'EXIT', kind='interp', line=213)
W('15,2167', 0o06001, '', 'TC', 'GOTOPOOH', line=214)
S('VB05N09', 'equals', 0o5006, line=215)
W('15,2170', 0o01442, 'V06N34*', 'VN', '634', kind='data', line=216)

# Page 931
# CHECK FOR GYRO TORQUE COARSE ALIGNMENT

W('15,2171', 0o32217, 'COARSTYP', 'CAF', 'OCT13', line=221)
W('15,2172', 0o04616, '', 'TC', 'BANKCALL', 'DISPLAY V 50N25 WITH COARSE ALIGN OPTION', line=222)
W('15,2173', 0o20623, '', 'CADR', 'GOPERF1', kind='data', line=223)
W('15,2174', 0o16001, '', 'TCF', 'GOTOPOOH', 'V34 -- TERMIN&OE', line=224)
W('15,2175', 0o12156, '', 'TCF', 'REGCOARS', 'V33 -- NORMAL COARSE', line=225)
W('15,2176', 0o06037, '', 'TC', 'INTPRET', 'V32 -- GYRO TORQUE COARSE', line=226)
W('15,2177', 0o64375, '', 'VLOAD', 'MXV', kind='interp', line=227)
W('15,2200', 0o03607, '', '', 'XSMD', 'GET SM(DESIRED) WRT SM(PRESENT)', kind='operand', line=228)
W('15,2201', 0o01734, '', '', 'REFSMMAT', kind='operand', line=229)
W('15,2202', 0o77656, '', 'UNIT', kind='interp', line=230)
W('15,2203', 0o26665, '', 'STOVL', 'XDC', kind='interp', line=231)
W('15,2204', 0o03615, '', '', 'YSMD', kind='operand', line=232)
W('15,2205', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=233)
W('15,2206', 0o01734, '', '', 'REFSMMAT', kind='operand', line=234)
W('15,2207', 0o26673, '', 'STOVL', 'YDC', kind='interp', line=235)
W('15,2210', 0o03623, '', '', 'ZSMD', kind='operand', line=236)
W('15,2211', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=237)
W('15,2212', 0o01734, '', '', 'REFSMMAT', kind='operand', line=238)
W('15,2213', 0o36701, '', 'STCALL', 'ZDC', kind='interp', line=239)
W('15,2214', 0o31164, '', '', 'GYCOARS', kind='operand', line=240)
W('15,2215', 0o77650, '', 'GOTO', kind='interp', line=241)
W('15,2216', 0o32166, '', '', 'P52OUT', kind='operand', line=242)
W('15,2217', 0o00013, 'OCT13', 'OCT', '13', kind='data', line=243)

# Page 932
# COMPUTE LANDING ORIENTATION FOR OPTION 4

W('15,2220', 0o43014, 'P52LS', 'SET', 'CLEAR', 'GET LANDING SITE ORIENTATION', kind='interp', line=248)
W('15,2221', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=249)
W('15,2222', 0o00662, '', '', 'ERADFLAG', 'TO PICK UP RLS', kind='operand', line=250)
W('15,2223', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=251)
W('15,2224', 0o00001, '', '', '0', kind='operand', line=252)
W('15,2225', 0o02023, '', '', 'RLS', 'PICK UP LANDING SITE VEC IN MF', kind='operand', line=253)
W('15,2226', 0o41525, '', 'PDDL', 'PUSH', 'RLS PD 0-5', kind='interp', line=254)
W('15,2227', 0o02775, '', '', 'TALIGN', kind='operand', line=255)
W('15,2230', 0o36401, '', 'STCALL', 'TLAND', 'JAM ALIGN TIME IN TLAND FOR OPTION 4', kind='interp', line=256)
W('15,2231', 0o55716, '', '', 'RP-TO-R', 'TRANS RLS TO REF', kind='operand', line=257)
W('15,2232', 0o77742, '', 'VSR2', kind='interp', line=258)
W('15,2233', 0o16032, '', 'STODL', 'ALPHAV', 'INPUT TO LAT-LONG', kind='interp', line=259)
W('15,2234', 0o02775, '', '', 'TALIGN', kind='operand', line=260)
W('15,2235', 0o77624, '', 'CALL', kind='interp', line=261)
W('15,2236', 0o30446, '', '', 'N89DISP', kind='operand', line=262)
W('15,2237', 0o53575, '', 'VLOAD', 'UNIT', 'COMPUTE LANDING SITE ORIENT (XSMD)', kind='interp', line=263)
W('15,2240', 0o02032, '', '', 'ALPHAV', kind='operand', line=264)
W('15,2241', 0o37607, '', 'STCALL', 'XSMD', kind='interp', line=265)
W('15,2242', 0o11013, '', '', 'LSORIENT', kind='operand', line=266)
W('15,2243', 0o77650, '', 'GOTO', kind='interp', line=267)
W('15,2244', 0o32143, '', '', 'P52D', 'NOW GO COMPUTE GIMBAL ANGLES.', kind='operand', line=268)

# Page 933
# SUBROUTINE TO CALCULATE AND DISPLAY THE LUNAR LANDING SITE

#   SETLOC P50S1
#   BANK
#   EBANK= XSM

W('14,2446', 0o77620, 'N89DISP', 'STQ', kind='interp', line=277)
W('14,2447', 0o02746, '', '', 'QMAJ', kind='operand', line=278)
W('14,2450', 0o35243, '', 'STCALL', 'GDT/2 +4', 'TEMP STORE TIME', kind='interp', line=279)
W('14,2451', 0o26351, '', '', 'LAT-LONG', kind='operand', line=280)
W('14,2452', 0o70545, '', 'DLOAD', 'SR1', kind='interp', line=281)
W('14,2453', 0o01123, '', '', 'LONG', kind='operand', line=282)
W('14,2454', 0o16711, '', 'STODL', 'LANDLONG', kind='interp', line=283)
W('14,2455', 0o01125, '', '', 'ALT', kind='operand', line=284)
W('14,2456', 0o16713, '', 'STODL', 'LANDALT', kind='interp', line=285)
W('14,2457', 0o01121, '', '', 'LAT', kind='operand', line=286)
W('14,2460', 0o16707, '', 'STODL', 'LANDLAT', kind='interp', line=287)
W('14,2461', 0o77776, '', 'EXIT', kind='interp', line=288)

W('14,2462', 0o32505, 'LSDISP', 'CAF', 'V06N89*', 'DISPLAY LAT,LONG/2,ALT', line=290)
W('14,2463', 0o04616, '', 'TC', 'BANKCALL', line=291)
W('14,2464', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=292)
W('14,2465', 0o16001, '', 'TCF', 'GOTOPOOH', 'V34 -- TERMINATE -- EXIT P57', line=293)
W('14,2466', 0o12470, '', 'TCF', '+2', 'V33 -- PROCEED -- ACCEPT LS DATA', line=294)
W('14,2467', 0o12462, '', 'TCF', 'LSDISP', 'V32 OR E -- LOOK AGAIN AND/OR LOAD NEW LS', line=295)

W('14,2470', 0o06037, '', 'TC', 'INTPRET', line=297)
W('14,2471', 0o72545, '', 'DLOAD', 'SL1', kind='interp', line=298)
W('14,2472', 0o02711, '', '', 'LANDLONG', kind='operand', line=299)
W('14,2473', 0o15123, '', 'STODL', 'LONG', kind='interp', line=300)
W('14,2474', 0o02713, '', '', 'LANDALT', kind='operand', line=301)
W('14,2475', 0o15125, '', 'STODL', 'ALT', kind='interp', line=302)
W('14,2476', 0o02707, '', '', 'LANDLAT', kind='operand', line=303)
W('14,2477', 0o15121, '', 'STODL', 'LAT', kind='interp', line=304)
W('14,2500', 0o01243, '', '', 'GDT/2 +4', 'PICK UP TIME', kind='operand', line=305)
W('14,2501', 0o77624, '', 'CALL', '', 'GET RLS BACK FROM LAT,LONG,ALT', kind='interp', line=306)
W('14,2502', 0o26422, '', '', 'LALOTORV', 'RLS B-29 IN MPAC AND ALPHAV', kind='operand', line=307)
W('14,2503', 0o77650, '', 'GOTO', kind='interp', line=308)
W('14,2504', 0o02746, '', '', 'QMAJ', kind='operand', line=309)
W('14,2505', 0o01531, 'V06N89*', 'VN', '689', kind='data', line=310)

# Page 934
# NAME -- S50 ALIAS LOCSAM
# BY
# VINCENT
#
# FUNCTION -- COMPUTE INPUTS FOR PICAPAR AND PLANET
#
# DEFINE
#
# U   = UNIT( SUN WRT EARTH )
# ES
#
# U   = UNIT( MOON WRT EARTH )
# EM
#
# R   = POSITION VECTOR OF LEM
# L
#
# R   = MEAN DISTANCE (384402KM) BETWEEN EARTH AND MOON
# EM
#
# P   = RATIO R  /(DISTANCE SUN TO EARTH) > .00257125
# EM
#
# R   = EQUATORIAL RADIUS (6378.166KM) OF EARTH
# E
#
# LOCSAM COMPUTES IN EARTH INFLUENCE
#
# VSUN = U
# ES
#
# VEARTH = -UNIT( R  )
# L
#
# VMOON = UNIT(R  .U   - R  )
# EM  EM    L
#
# CSUN = COS 90
#
# CEARTH = COS(5 + ARCSIN(R /MAG(R )))
# E      L
#
# CMOON   = COS 5
#
# INPUT -- TIME IN MPAC
#
# OUTPUT -- LISTED ABOVE
#
# SUBROUTINES -- LSPOS, LEMPREC
#
# DEBRIS -- VAC AREA, TSIGHT

# Page 935
#   COUNT* $$/LOSAM

S('S50', 'equals', 0o40506, line=368)
W('14,2506', 0o77620, 'LOCSAM', 'STQ', kind='interp', line=369)
W('14,2507', 0o02745, '', '', 'QMIN', kind='operand', line=370)
W('14,2510', 0o37562, '', 'STCALL', 'TSIGHT', kind='interp', line=371)
W('14,2511', 0o33664, '', '', 'LSPOS', kind='operand', line=372)
W('14,2512', 0o77745, '', 'DLOAD', kind='interp', line=373)
W('14,2513', 0o03562, '', '', 'TSIGHT', kind='operand', line=374)
W('14,2514', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=375)
W('14,2515', 0o27057, '', '', 'LEMPREC', kind='operand', line=376)
W('14,2516', 0o61131, '', 'SSP', 'TIX,2', kind='interp', line=377)
W('14,2517', 0o00052, '', '', 'S2', kind='operand', line=378)
W('14,2520', 0o00000, '', '', '0', kind='operand', line=379)
W('14,2521', 0o30543, '', '', 'MOONCNTR', kind='operand', line=380)
W('14,2522', 0o74375, 'EARTCNTR', 'VLOAD', 'VXSC', kind='interp', line=381)
W('14,2523', 0o02723, '', '', 'VMOON', kind='operand', line=382)
W('14,2524', 0o30001, '', '', 'RSUBEM', kind='operand', line=383)
W('14,2525', 0o52372, '', 'VSL1', 'VSU', kind='interp', line=384)
W('14,2526', 0o00001, '', '', 'RATT', kind='operand', line=385)
W('14,2527', 0o77656, '', 'UNIT', kind='interp', line=386)
W('14,2530', 0o26723, '', 'STOVL', 'VMOON', kind='interp', line=387)
W('14,2531', 0o00001, '', '', 'RATT', kind='operand', line=388)
W('14,2532', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=389)
W('14,2533', 0o16707, '', 'STODL', 'VEARTH', kind='interp', line=390)
W('14,2534', 0o30005, '', '', 'RSUBE', kind='operand', line=391)
W('14,2535', 0o77624, '', 'CALL', kind='interp', line=392)
W('14,2536', 0o30575, '', '', 'OCCOS', kind='operand', line=393)
W('14,2537', 0o14017, '', 'STODL', 'CEARTH', kind='interp', line=394)
W('14,2540', 0o30604, '', '', 'CSS5', kind='operand', line=395)
W('14,2541', 0o34023, '', 'STCALL', 'CMOON', kind='interp', line=396)
W('14,2542', 0o30570, '', '', 'ENDSAM', kind='operand', line=397)
W('14,2543', 0o74375, 'MOONCNTR', 'VLOAD', 'VXSC', kind='interp', line=398)
W('14,2544', 0o02723, '', '', 'VMOON', kind='operand', line=399)
W('14,2545', 0o30007, '', '', 'ROE', kind='operand', line=400)
W('14,2546', 0o53445, '', 'BVSU', 'UNIT', kind='interp', line=401)
W('14,2547', 0o02715, '', '', 'VSUN', kind='operand', line=402)
W('14,2550', 0o26715, '', 'STOVL', 'VSUN', kind='interp', line=403)
W('14,2551', 0o02723, '', '', 'VMOON', kind='operand', line=404)
W('14,2552', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=405)
W('14,2553', 0o30001, '', '', 'RSUBEM', kind='operand', line=406)
W('14,2554', 0o00001, '', '', 'RATT', kind='operand', line=407)
W('14,2555', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=408)
W('14,2556', 0o26707, '', 'STOVL', 'VEARTH', kind='interp', line=409)
W('14,2557', 0o00001, '', '', 'RATT', kind='operand', line=410)
W('14,2560', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=411)
W('14,2561', 0o16723, '', 'STODL', 'VMOON', kind='interp', line=412)
W('14,2562', 0o30003, '', '', 'RSUBM', kind='operand', line=413)
W('14,2563', 0o77624, '', 'CALL', kind='interp', line=414)
W('14,2564', 0o30575, '', '', 'OCCOS', kind='operand', line=415)
# Page 936
W('14,2565', 0o14023, '', 'STODL', 'CMOON', kind='interp', line=417)
W('14,2566', 0o30604, '', '', 'CSS5', kind='operand', line=418)
W('14,2567', 0o00017, '', 'STORE', 'CEARTH', kind='interp', line=419)
W('14,2570', 0o77745, 'ENDSAM', 'DLOAD', kind='interp', line=420)
W('14,2571', 0o30606, '', '', 'CSSUN', kind='operand', line=421)
W('14,2572', 0o00021, '', 'STORE', 'CSUN', kind='interp', line=422)
W('14,2573', 0o77650, '', 'GOTO', kind='interp', line=423)
W('14,2574', 0o02745, '', '', 'QMIN', kind='operand', line=424)
W('14,2575', 0o70471, 'OCCOS', 'DDV', 'SR1', kind='interp', line=425)
W('14,2576', 0o00045, '', '', '36D', kind='operand', line=426)
W('14,2577', 0o43336, '', 'ASIN', 'DAD', kind='interp', line=427)
W('14,2600', 0o30610, '', '', '5DEGREES', kind='operand', line=428)
W('14,2601', 0o70546, '', 'COS', 'SR1', kind='interp', line=429)
W('14,2602', 0o77616, '', 'RVQ', kind='interp', line=430)
S('CEARTH', 'equals', 0o16, line=431)
S('CSUN', 'equals', 0o20, line=432)
S('CMOON', 'equals', 0o22, line=433)
W('14,2603', 0o07760, 'CSS5', '2DEC', '.2490475', '(COS 5)/4', kind='data', line=434)
W('14,2604', 0o14473, kind='data', line=434)
W('14,2605', 0o04000, 'CSSUN', '2DEC', '.125', '(COS 60)/4', kind='data', line=435)
W('14,2606', 0o00000, kind='data', line=435)
W('14,2607', 0o00343, '5DEGREES', '2DEC', '.013888889', 'SCALED IN REVS', kind='data', line=436)
W('14,2610', 0o21616, kind='data', line=436)

# Page 937
# PROGRAM NAME -- R56           DATE: DEC 20 66
# MOD 1                         LOG SECTION: P51-P53
# ASSEMBLY:  SUNDISK REV4D
# BY KEN VINCENT
#
# FUNCTION
# THIS PROGRAM READS THE IMU-CDUS AND COMPUTES THE VEHICLE ORIENTATION
# WITH RESPECT TO INERTIAL SPACE.  IT THEN COMPUTES THE SHAFT AXIS (SAX)
# WITH RESPECT TO REFERENCE INTERTIAL.  EACH STAR IN THE CATALOG IS TESTED
# TO DETERMIN IF IT IS OCCULTED BY EITHER EARTH, SUN OR MOON.  IF A
# STAR IS NOT OCCULTED THEN IT IS PAIRED WITH ALL STARS OF LOWER INDEX.
# THE PAIRED STAR IS TESTED FOR OCCULTATION.  PAIRS OF STARS THAT PASS
# THE OCCULTATION TESTS ARE TESTED FOR GOOD SEPARATION.  A PAIR OF STARS
# HAVE GOOD SEPARATION IF THE ANGLE BETWEEN THEM IS LESS THAN 100 DEGREES
# AND MORE THAN 50 DEGREES.  THOSE PAIRS WITH GOOD SEPARATION
# ARE THEN TESTED TO SEE IF THEY LIE IN CURRENT FIELD OF VIEW.  (WITHIN
# 50 DEGREES OF SAX).  THE PAIR WITH MAX SEPARATION IS CHOSEN FROM
# THOSE WITH GOOD SEPARATION, AND IN FIELD OF VIEW.
#
# CALLING SEQUENCE
# L       TC      BANKCALL
# L+1     CADR    R56
# L+2     ERROR RETURN -- NO STARS IN FIELD OF VIEW
# L+3     NORMAL RETURN
#
# OUTPUT
# BESTI, BESTJ -- SINGLE PREC, INTEGERS, STAR NUMBERS TIMES 6
# VFLAG -- FLAG BIT SET IMPLIES NO STARS IN FIELD OF VIEW
#
# INITIALIZATION
# 1)      A CALL TO LOCSAM MUST BE MADE
#
# DEBRIS
# WORKAREA
# X,Y,ZNB
# SINCDU, COSCDU
# STARAD -- STAR +5

S('R56', 'equals', 0o40611, line=477)
#   COUNT* $$/R56
W('14,2611', 0o04645, 'PICAPAR', 'TC', 'MAKECADR', line=479)
W('14,2612', 0o55745, '', 'TS', 'QMIN', line=480)
W('14,2613', 0o06037, '', 'TC', 'INTPRET', line=481)
W('14,2614', 0o77624, '', 'CALL', kind='interp', line=482)
W('14,2615', 0o47537, '', '', 'CDUTRIG', kind='operand', line=483)
W('14,2616', 0o77624, '', 'CALL', kind='interp', line=484)
W('14,2617', 0o20030, '', '', 'CALCSMSC', kind='operand', line=485)
W('14,2620', 0o77601, '', 'SETPD', kind='interp', line=486)
W('14,2621', 0o00001, '', '', '0', kind='operand', line=487)
W('14,2622', 0o71214, '', 'SET', 'DLOAD', 'VFLAG = 1', kind='interp', line=488)
W('14,2623', 0o01465, '', '', 'VFLAG', kind='operand', line=489)
# Page 938
W('14,2624', 0o24007, '', '', 'DPZERO', kind='operand', line=491)
W('14,2625', 0o26756, '', 'STOVL', 'BESTI', kind='interp', line=492)
W('14,2626', 0o02665, '', '', 'XNB', kind='operand', line=493)
W('14,2627', 0o63361, '', 'VXSC', 'PDVL', kind='interp', line=494)
W('14,2630', 0o24005, '', '', 'HALFDP', kind='operand', line=495)
W('14,2631', 0o02701, '', '', 'ZNB', kind='operand', line=496)
W('14,2632', 0o74370, '', 'AXT,1', 'VXSC', kind='interp', line=497)
W('14,2633', 0o00344, '', '', '228D', 'X1 = 37 X 6 + 6', kind='operand', line=498)
W('14,2634', 0o24005, '', '', 'HALFDP', kind='operand', line=499)
W('14,2635', 0o77655, '', 'VAD', kind='interp', line=500)
W('14,2636', 0o53505, '', 'VXM', 'UNIT', kind='interp', line=501)
W('14,2637', 0o01734, '', '', 'REFSMMAT', kind='operand', line=502)
W('14,2640', 0o02731, '', 'STORE', 'SAX', 'SAX = SHAFT AXIS', kind='interp', line=503)
W('14,2641', 0o66331, '', 'SSP', 'SSP', 'S1 = S2 = 6', kind='interp', line=504)
W('14,2642', 0o00051, '', '', 'S1', kind='operand', line=505)
W('14,2643', 0o00006, '', '', '6', kind='operand', line=506)
W('14,2644', 0o00052, '', '', 'S2', kind='operand', line=507)
W('14,2645', 0o00006, '', '', '6', kind='operand', line=508)
W('14,2646', 0o52100, 'PIC1', 'TIX,1', 'GOTO', 'MAJOR STAR', kind='interp', line=509)
W('14,2647', 0o30651, '', '', 'PIC2', kind='operand', line=510)
W('14,2650', 0o30766, '', '', 'PICEND', kind='operand', line=511)
W('14,2651', 0o50373, 'PIC2', 'VLOAD*', 'DOT', kind='interp', line=512)
W('14,2652', 0o30347, '', '', 'CATLOG,1', kind='operand', line=513)
W('14,2653', 0o02731, '', '', 'SAX', kind='operand', line=514)
W('14,2654', 0o50025, '', 'DSU', 'BMN', kind='interp', line=515)
W('14,2655', 0o30765, '', '', 'CSS33', kind='operand', line=516)
W('14,2656', 0o30646, '', '', 'PIC1', kind='operand', line=517)
W('14,2657', 0o77754, '', 'LXA,2', kind='interp', line=518)
W('14,2660', 0o00046, '', '', 'X1', kind='operand', line=519)
W('14,2661', 0o52104, 'PIC3', 'TIX,2', 'GOTO', kind='interp', line=520)
W('14,2662', 0o30664, '', '', 'PIC4', kind='operand', line=521)
W('14,2663', 0o30646, '', '', 'PIC1', kind='operand', line=522)
W('14,2664', 0o50373, 'PIC4', 'VLOAD*', 'DOT', kind='interp', line=523)
W('14,2665', 0o47430, '', '', 'CATLOG,2', kind='operand', line=524)
W('14,2666', 0o02731, '', '', 'SAX', kind='operand', line=525)
W('14,2667', 0o50025, '', 'DSU', 'BMN', kind='interp', line=526)
W('14,2670', 0o30765, '', '', 'CSS33', kind='operand', line=527)
W('14,2671', 0o30661, '', '', 'PIC3', kind='operand', line=528)
W('14,2672', 0o47773, '', 'VLOAD*', 'DOT*', kind='interp', line=529)
W('14,2673', 0o30347, '', '', 'CATLOG,1', kind='operand', line=530)
W('14,2674', 0o47430, '', '', 'CATLOG,2', kind='operand', line=531)
W('14,2675', 0o51025, '', 'DSU', 'BPL', kind='interp', line=532)
W('14,2676', 0o30763, '', '', 'CSS40', kind='operand', line=533)
W('14,2677', 0o30661, '', '', 'PIC3', kind='operand', line=534)
W('14,2700', 0o45173, '', 'VLOAD*', 'CALL', kind='interp', line=535)
W('14,2701', 0o30347, '', '', 'CATLOG,1', kind='operand', line=536)
W('14,2702', 0o30740, '', '', 'OCCULT', kind='operand', line=537)
W('14,2703', 0o77614, '', 'BON', kind='interp', line=538)
W('14,2704', 0o01710, '', '', 'CULTFLAG', kind='operand', line=539)
W('14,2705', 0o30646, '', '', 'PIC1', kind='operand', line=540)
# Page 939
W('14,2706', 0o45173, '', 'VLOAD*', 'CALL', kind='interp', line=542)
W('14,2707', 0o47430, '', '', 'CATLOG,2', kind='operand', line=543)
W('14,2710', 0o30740, '', '', 'OCCULT', kind='operand', line=544)
W('14,2711', 0o77614, '', 'BON', kind='interp', line=545)
W('14,2712', 0o01710, '', '', 'CULTFLAG', kind='operand', line=546)
W('14,2713', 0o30661, '', '', 'PIC3', kind='operand', line=547)
W('14,2714', 0o77614, 'STRATGY', 'BONCLR', kind='interp', line=548)
W('14,2715', 0o01605, '', '', 'VFLAG', kind='operand', line=549)
W('14,2716', 0o30733, '', '', 'NEWPAR', kind='operand', line=550)
W('14,2717', 0o65120, '', 'XCHX,1', 'XCHX,2', kind='interp', line=551)
W('14,2720', 0o02755, '', '', 'BESTI', kind='operand', line=552)
W('14,2721', 0o02756, '', '', 'BESTJ', kind='operand', line=553)
W('14,2722', 0o47773, 'STRAT', 'VLOAD*', 'DOT*', kind='interp', line=554)
W('14,2723', 0o30347, '', '', 'CATLOG,1', kind='operand', line=555)
W('14,2724', 0o47430, '', '', 'CATLOG,2', kind='operand', line=556)
W('14,2725', 0o43006, '', 'PUSH', 'BOFINV', kind='interp', line=557)
W('14,2726', 0o01545, '', '', 'VFLAG', kind='operand', line=558)
W('14,2727', 0o30717, '', '', 'STRAT -3', kind='operand', line=559)
W('14,2730', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=560)
W('14,2731', 0o77644, '', 'BPL', kind='interp', line=561)
W('14,2732', 0o30661, '', '', 'PIC3', kind='operand', line=562)
W('14,2733', 0o67130, 'NEWPAR', 'SXA,1', 'SXA,2', kind='interp', line=563)
W('14,2734', 0o02755, '', '', 'BESTI', kind='operand', line=564)
W('14,2735', 0o02756, '', '', 'BESTJ', kind='operand', line=565)
W('14,2736', 0o77650, '', 'GOTO', kind='interp', line=566)
W('14,2737', 0o30661, '', '', 'PIC3', kind='operand', line=567)
W('14,2740', 0o51321, 'OCCULT', 'MXV', 'BVSU', kind='interp', line=568)
W('14,2741', 0o02707, '', '', 'CULTRIX', kind='operand', line=569)
W('14,2742', 0o00017, '', '', 'CSS', kind='operand', line=570)
W('14,2743', 0o77654, '', 'BZE', kind='interp', line=571)
W('14,2744', 0o30757, '', '', 'CULTED', kind='operand', line=572)
W('14,2745', 0o75240, '', 'BMN', 'SIGN', kind='interp', line=573)
W('14,2746', 0o30757, '', '', 'CULTED', kind='operand', line=574)
W('14,2747', 0o00160, '', '', 'MPAC +3', kind='operand', line=575)
W('14,2750', 0o75240, '', 'BMN', 'SIGN', kind='interp', line=576)
W('14,2751', 0o30757, '', '', 'CULTED', kind='operand', line=577)
W('14,2752', 0o00162, '', '', 'MPAC +5', kind='operand', line=578)
W('14,2753', 0o43040, '', 'BMN', 'CLRGO', kind='interp', line=579)
W('14,2754', 0o30757, '', '', 'CULTED', kind='operand', line=580)
W('14,2755', 0o01630, '', '', 'CULTFLAG', kind='operand', line=581)
W('14,2756', 0o00052, '', '', 'QPRET', kind='operand', line=582)
W('14,2757', 0o77614, 'CULTED', 'SETGO', kind='interp', line=583)
W('14,2760', 0o01430, '', '', 'CULTFLAG', kind='operand', line=584)
W('14,2761', 0o00052, '', '', 'QPRET', kind='operand', line=585)
S('CSS', 'equals', 0o16, line=586)
W('14,2762', 0o05110, 'CSS40', '2DEC', '.16070', 'COS 50 / 4', kind='data', line=587)
W('14,2763', 0o35052, kind='data', line=587)
W('14,2764', 0o05110, 'CSS33', '2DEC', '.16070', 'COS 50 / 4', kind='data', line=588)
W('14,2765', 0o35052, kind='data', line=588)
W('14,2766', 0o77414, 'PICEND', 'BOFF', 'EXIT', kind='interp', line=589)

# Page 940
W('14,2767', 0o01745, '', '', 'VFLAG', kind='operand', line=592)
W('14,2770', 0o30772, '', '', 'PICGXT', kind='operand', line=593)
W('14,2771', 0o03013, '', 'TC', 'PICBXT', line=594)
W('14,2772', 0o73150, 'PICGXT', 'LXA,1', 'LXA,2', kind='interp', line=595)
W('14,2773', 0o02755, '', '', 'BESTI', kind='operand', line=596)
W('14,2774', 0o02756, '', '', 'BESTJ', kind='operand', line=597)
W('14,2775', 0o47775, '', 'VLOAD', 'DOT*', kind='interp', line=598)
W('14,2776', 0o02731, '', '', 'SAX', kind='operand', line=599)
W('14,2777', 0o30347, '', '', 'CATLOG,1', kind='operand', line=600)
W('14,3000', 0o47715, '', 'PDVL', 'DOT*', kind='interp', line=601)
W('14,3001', 0o02731, '', '', 'SAX', kind='operand', line=602)
W('14,3002', 0o47430, '', '', 'CATLOG,2', kind='operand', line=603)
W('14,3003', 0o77625, '', 'DSU', kind='interp', line=604)
W('14,3004', 0o66044, '', 'BPL', 'SXA,1', kind='interp', line=605)
W('14,3005', 0o31011, '', '', 'PICNSWP', kind='operand', line=606)
W('14,3006', 0o02756, '', '', 'BESTJ', kind='operand', line=607)
W('14,3007', 0o77734, '', 'SXA,2', kind='interp', line=608)
W('14,3010', 0o02755, '', '', 'BESTI', kind='operand', line=609)
W('14,3011', 0o77776, 'PICNSWP', 'EXIT', kind='interp', line=610)
W('14,3012', 0o25745, '', 'INCR', 'QMIN', line=611)
W('14,3013', 0o31745, 'PICBXT', 'CA', 'QMIN', line=612)
W('14,3014', 0o04622, '', 'TC', 'SWCALL', line=613)
S('VPD', 'equals', 0o0, line=614)
S('V0', 'equals', 0o6, line=615)
S('V1', 'equals', 0o14, line=616)
S('V2', 'equals', 0o22, line=617)
S('V3', 'equals', 0o30, line=618)
S('DP0', 'equals', 0o36, line=619)
S('DP1', 'equals', 0o40, line=620)

# Page 941
# NAME -- R51   FINE ALIGN
# FUNCTION -- TO ALIGN THE STABLE MEMBER TO REFSSMAT
# CALLING SEQ -- CALL R51
# INPUT -- REFSMMAT
# OUTPUT -- GYRO TORQUE PULSES
# SUBROUTINES -- LOCSAM, PICAPAR, R52, R53, R54, R55

#   COUNT* $$/R51
W('14,3015', 0o77620, 'R51', 'STQ', kind='interp', line=631)
W('14,3016', 0o02746, '', '', 'QMAJ', kind='operand', line=632)
W('14,3017', 0o77776, 'R51.1', 'EXIT', kind='interp', line=633)
W('14,3020', 0o05353, '', 'TC', 'PHASCHNG', line=634)
W('14,3021', 0o04024, '', 'OCT', '04024', kind='data', line=635)

W('14,3022', 0o34761, 'R51C', 'CAF', 'OCT15', line=637)
W('14,3023', 0o04616, '', 'TC', 'BANKCALL', line=638)
W('14,3024', 0o20623, '', 'CADR', 'GOPERF1', kind='data', line=639)
W('14,3025', 0o06001, '', 'TC', 'GOTOPOOH', line=640)
W('14,3026', 0o03030, '', 'TC', '+2', 'V33E', line=641)
W('14,3027', 0o03053, '', 'TC', 'R51E', 'ENTER', line=642)
W('14,3030', 0o06037, '', 'TC', 'INTPRET', line=643)
W('14,3031', 0o43234, '', 'RTB', 'DAD', kind='interp', line=644)
W('14,3032', 0o21573, '', '', 'LOADTIME', kind='operand', line=645)
W('14,3033', 0o31163, '', '', 'TSIGHT1', kind='operand', line=646)
W('14,3034', 0o77624, '', 'CALL', kind='interp', line=647)
W('14,3035', 0o30506, '', '', 'LOCSAM', kind='operand', line=648)
W('14,3036', 0o77776, '', 'EXIT', kind='interp', line=649)
W('14,3037', 0o04616, '', 'TC', 'BANKCALL', line=650)
W('14,3040', 0o30611, '', 'CADR', 'R56', kind='data', line=651)
W('14,3041', 0o03043, '', 'TC', 'R51I', line=652)
W('14,3042', 0o03053, 'R51F', 'TC', 'R51E', line=653)
W('14,3043', 0o05567, 'R51I', 'TC', 'ALARM', line=654)
W('14,3044', 0o00405, '', 'OCT', '405', kind='data', line=655)
W('14,3045', 0o35006, '', 'CAF', 'VB05N09', line=656)
W('14,3046', 0o04616, '', 'TC', 'BANKCALL', line=657)
W('14,3047', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=658)
W('14,3050', 0o06001, '', 'TC', 'GOTOPOOH', line=659)
W('14,3051', 0o03053, '', 'TC', 'R51E', line=660)
W('14,3052', 0o03022, '', 'TC', 'R51C', line=661)
W('14,3053', 0o34755, 'R51E', 'CAF', 'ZERO', line=662)
W('14,3054', 0o55757, '', 'TS', 'STARIND', line=663)
W('14,3055', 0o06037, 'R51.2', 'TC', 'INTPRET', line=664)
W('14,3056', 0o77776, 'R51.3', 'EXIT', kind='interp', line=665)
W('14,3057', 0o05353, '', 'TC', 'PHASCHNG', line=666)
W('14,3060', 0o04024, '', 'OCT', '04024', kind='data', line=667)

W('14,3061', 0o06037, '', 'TC', 'INTPRET', line=669)
W('14,3062', 0o77624, '', 'CALL', kind='interp', line=670)
W('14,3063', 0o31670, '', '', 'R52', 'AOP WILL MAKE CALLS TO SIGHTING', kind='operand', line=671)
W('14,3064', 0o77776, '', 'EXIT', kind='interp', line=672)
W('14,3065', 0o04616, '', 'TC', 'BANKCALL', line=673)
# Page 942
W('14,3066', 0o16000, '', 'CADR', 'AOTMARK', kind='data', line=675)
W('14,3067', 0o04616, '', 'TC', 'BANKCALL', line=676)
W('14,3070', 0o17712, '', 'CADR', 'OPTSTALL', kind='data', line=677)
W('14,3071', 0o05711, '', 'TC', 'CURTAINS', line=678)
W('14,3072', 0o11757, '', 'CCS', 'STARIND', line=679)
W('14,3073', 0o13075, '', 'TCF', '+2', line=680)
W('14,3074', 0o03145, '', 'TC', 'R51.4', line=681)
W('14,3075', 0o06037, '', 'TC', 'INTPRET', line=682)
W('14,3076', 0o77775, '', 'VLOAD', kind='interp', line=683)
W('14,3077', 0o02715, '', '', 'STARAD +6', kind='operand', line=684)
W('14,3100', 0o02767, '', 'STORE', 'STARSAV2', kind='interp', line=685)
W('14,3101', 0o77776, '', 'EXIT', kind='interp', line=686)
W('14,3102', 0o05353, '', 'TC', 'PHASCHNG', line=687)
W('14,3103', 0o04024, '', 'OCT', '04024', kind='data', line=688)

W('14,3104', 0o06037, '', 'TC', 'INTPRET', line=690)
W('14,3105', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=691)
W('14,3106', 0o03562, '', '', 'TSIGHT', kind='operand', line=692)
W('14,3107', 0o32472, '', '', 'PLANET', kind='operand', line=693)
W('14,3110', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=694)
W('14,3111', 0o01734, '', '', 'REFSMMAT', kind='operand', line=695)
W('14,3112', 0o26715, '', 'STOVL', 'STARAD +6', kind='interp', line=696)
W('14,3113', 0o03554, '', '', 'PLANVEC', kind='operand', line=697)
W('14,3114', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=698)
W('14,3115', 0o01734, '', '', 'REFSMMAT', kind='operand', line=699)
W('14,3116', 0o26707, '', 'STOVL', 'STARAD', kind='interp', line=700)
W('14,3117', 0o02761, '', '', 'STARSAV1', kind='operand', line=701)
W('14,3120', 0o24007, '', 'STOVL', '6D', kind='interp', line=702)
W('14,3121', 0o02767, '', '', 'STARSAV2', kind='operand', line=703)
W('14,3122', 0o34015, '', 'STCALL', '12D', kind='interp', line=704)
W('14,3123', 0o31256, '', '', 'R54', 'STAR DATA TEST', kind='operand', line=705)
W('14,3124', 0o45014, '', 'BOFF', 'CALL', kind='interp', line=706)
W('14,3125', 0o00354, '', '', 'FREEFLAG', kind='operand', line=707)
W('14,3126', 0o31134, '', '', 'R51K', kind='operand', line=708)
W('14,3127', 0o47441, '', '', 'AXISGEN', kind='operand', line=709)
W('14,3130', 0o77624, '', 'CALL', kind='interp', line=710)
W('14,3131', 0o31224, '', '', 'R55', 'GYRO TORQUE', kind='operand', line=711)
W('14,3132', 0o77614, '', 'CLEAR', kind='interp', line=712)
W('14,3133', 0o01273, '', '', 'PFRATFLG', kind='operand', line=713)
W('14,3134', 0o77776, 'R51K', 'EXIT', kind='interp', line=714)
W('14,3135', 0o35751, 'R51P63', 'CAF', 'OCT14', line=715)
W('14,3136', 0o04616, '', 'TC', 'BANKCALL', line=716)
W('14,3137', 0o20623, '', 'CADR', 'GOPERF1', kind='data', line=717)
W('14,3140', 0o06001, '', 'TC', 'GOTOPOOH', line=718)
W('14,3141', 0o03022, '', 'TC', 'R51C', line=719)
W('14,3142', 0o06037, '', 'TC', 'INTPRET', line=720)
W('14,3143', 0o77650, '', 'GOTO', kind='interp', line=721)
W('14,3144', 0o02746, '', '', 'QMAJ', kind='operand', line=722)
W('14,3145', 0o06037, 'R51.4', 'TC', 'INTPRET', line=723)
W('14,3146', 0o77775, '', 'VLOAD', kind='interp', line=724)
# Page 943
W('14,3147', 0o02715, '', '', 'STARAD +6', kind='operand', line=726)
W('14,3150', 0o02761, '', 'STORE', 'STARSAV1', kind='interp', line=727)
W('14,3151', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=728)
W('14,3152', 0o03562, '', '', 'TSIGHT', kind='operand', line=729)
W('14,3153', 0o32472, '', '', 'PLANET', kind='operand', line=730)
W('14,3154', 0o03554, '', 'STORE', 'PLANVEC', kind='interp', line=731)
W('14,3155', 0o77731, '', 'SSP', kind='interp', line=732)
W('14,3156', 0o02760, '', '', 'STARIND', kind='operand', line=733)
W('14,3157', 0o00001, '', '', '1', kind='operand', line=734)
W('14,3160', 0o77650, '', 'GOTO', kind='interp', line=735)
W('14,3161', 0o31056, '', '', 'R51.3', kind='operand', line=736)
W('14,3162', 0o00002, 'TSIGHT1', '2DEC', '36000', '6 MIN TO MARKING', kind='data', line=737)
W('14,3163', 0o06240, kind='data', line=737)

# Page 944
# GYRO TORQUE COARSE ALGNMENT

W('14,3164', 0o45020, 'GYCOARS', 'STQ', 'CALL', kind='interp', line=742)
W('14,3165', 0o02746, '', '', 'QMAJ', kind='operand', line=743)
W('14,3166', 0o47247, '', '', 'CALCGTA', kind='operand', line=744)
W('14,3167', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=745)
W('14,3170', 0o01260, '', '', 'DRIFTFLG', kind='operand', line=746)
W('14,3171', 0o01662, '', '', 'REFSMFLG', kind='operand', line=747)
W('14,3172', 0o77776, '', 'EXIT', kind='interp', line=748)
W('14,3173', 0o33223, '', 'CAF', 'V16N20', 'MONITOR GIMBALS', line=749)
W('14,3174', 0o04616, '', 'TC', 'BANKCALL', line=750)
W('14,3175', 0o20451, '', 'CADR', 'GODSPR', kind='data', line=751)
W('14,3176', 0o33255, '', 'CA', 'R55CDR', line=752)
W('14,3177', 0o04616, '', 'TC', 'BANKCALL', line=753)
W('14,3200', 0o17323, '', 'CADR', 'IMUPULSE', kind='data', line=754)
W('14,3201', 0o04616, '', 'TC', 'BANKCALL', line=755)
W('14,3202', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=756)
W('14,3203', 0o05711, '', 'TC', 'CURTAINS', line=757)
W('14,3204', 0o05353, '', 'TC', 'PHASCHNG', line=758)
W('14,3205', 0o04024, '', 'OCT', '04024', kind='data', line=759)

W('14,3206', 0o06037, '', 'TC', 'INTPRET', line=761)
W('14,3207', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=762)
W('14,3210', 0o03606, '', '', 'XSMD', kind='operand', line=763)
W('14,3211', 0o01733, '', '', 'REFSMMAT', kind='operand', line=764)
W('14,3212', 0o77624, '', 'CALL', '', 'STORE DESIRED REFSMMAT', kind='interp', line=765)
W('14,3213', 0o31377, '', '', 'MATMOVE', kind='operand', line=766)
W('14,3214', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=767)
W('14,3215', 0o01273, '', '', 'PFRATFLG', kind='operand', line=768)
W('14,3216', 0o01462, '', '', 'REFSMFLG', kind='operand', line=769)
W('14,3217', 0o77624, '', 'CALL', kind='interp', line=770)
W('14,3220', 0o31602, '', '', 'NCOARSE', 'SET DRIFT AND INITIALIZE 1/PIPADT', kind='operand', line=771)
W('14,3221', 0o77650, '', 'GOTO', kind='interp', line=772)
W('14,3222', 0o31134, '', '', 'R51K', kind='operand', line=773)
W('14,3223', 0o04024, 'V16N20', 'VN', '1620', kind='data', line=774)

# Page 945
# R55   GYRO TORQUE
# FUNCTION -- COMPUTE AND SEND GYRO PULSES
# CALLING SEQ -- CALL R55
# INPUT -- X,Y,ZDC -- REFSMMAT WRT PRESENT STABLE MEMBER
# OUTPUT -- GYRO PULSES
# SUBROUTINES -- CALCGTA, GOFLASH, GODSPR, IMUFINE, IMUPULSE, GOPERF1

#   COUNT* $$/R55
W('14,3224', 0o77620, 'R55', 'STQ', kind='interp', line=785)
W('14,3225', 0o02745, '', '', 'QMIN', kind='operand', line=786)
W('14,3226', 0o77624, '', 'CALL', kind='interp', line=787)
W('14,3227', 0o47247, '', '', 'CALCGTA', kind='operand', line=788)
W('14,3230', 0o77776, 'PULSEM', 'EXIT', kind='interp', line=789)
W('14,3231', 0o33254, 'R55.1', 'CAF', 'V06N93', line=790)
W('14,3232', 0o04616, '', 'TC', 'BANKCALL', line=791)
W('14,3233', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=792)
W('14,3234', 0o06001, '', 'TC', 'GOTOPOOH', line=793)
W('14,3235', 0o03237, '', 'TC', 'R55.2', line=794)
W('14,3236', 0o03251, '', 'TC', 'R55RET', line=795)
W('14,3237', 0o05353, 'R55.2', 'TC', 'PHASCHNG', line=796)
W('14,3240', 0o00214, '', 'OCT', '00214', kind='data', line=797)
W('14,3241', 0o33255, '', 'CA', 'R55CDR', line=798)
W('14,3242', 0o04616, '', 'TC', 'BANKCALL', line=799)
W('14,3243', 0o17323, '', 'CADR', 'IMUPULSE', kind='data', line=800)
W('14,3244', 0o04616, '', 'TC', 'BANKCALL', line=801)
W('14,3245', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=802)
W('14,3246', 0o05711, '', 'TC', 'CURTAINS', line=803)
W('14,3247', 0o05353, '', 'TC', 'PHASCHNG', line=804)
W('14,3250', 0o04024, '', 'OCT', '04024', kind='data', line=805)

W('14,3251', 0o06037, 'R55RET', 'TC', 'INTPRET', line=807)
W('14,3252', 0o77650, '', 'GOTO', kind='interp', line=808)
W('14,3253', 0o02745, '', '', 'QMIN', kind='operand', line=809)
W('14,3254', 0o01535, 'V06N93', 'VN', '0693', kind='data', line=810)
W('14,3255', 0o02737, 'R55CDR', 'ECADR', 'OGC', kind='data', line=811)
S('R54', 'equals', 0o41256, line=812)

# ROUTINE NAME -- CHKSDATA              DATE -- JAN 9, 1967
# MOD NO -- 0                           LOG SECTION -- P51-P53
# MODIFICATION BY -- LONSKE             ASSEMBLY --
#
# FUNCTIONAL DESCRIPTION -- CHECKS THE VALIDITY OF A PAIR OF STAR SIGHTINGS.  WHEN A PAIR OF STAR SIGHTINGS ARE MADE
# BY THE ASTRONAUT THIS ROUTINE OPERATES AND CHECKS THE OBSERVED SIGHTINGS AGAINST STORED STAR VECTORS IN THE
# COMPUTER TO INSURE A PROPER SIGHTING WAS MADE.  THE FOLLOWING COMPUTATIONS ARE PERFORMED --
# OS1     =       OBSERVED STAR 1 VECTOR
# OS2     =       OBSERVED STAR 2 VECTOR
# SS1     =       STORED STAR 1 VECTOR
# SS2     =       STORED STAR 2 VECTOR
# A1     =       ARCCOS(OS1 - OS2)
# A2     =       ARCCOS(SS1 - SS2)
# A     =       ABS(2(A1 - A2))
# Page 946
# THE ANGULAR DIFFERENCE IS DISPLAYED FOR ASTRONAUT ACCEPTANCE.
#
# EXIT MODE --  1. FREEFLAG SET IMPLIES ASTRONAUT WANTS TO PROCEED
# 2. FREEFLAG RESET IMPLIES ASTRONAUT WANTS TO RECYCLE
#
# OUTPUT --     1. VERB 6,NOUN 3 -- DISPLAYS ANGULAR DIFFERENCE BETWEEN 2 SETS OF STARS.
# 2. STAR VECTORS FROM STAR CATALOG ARE LEFT IN 6D AND 12D.
#
# ERASABLE INITIALIZATION REQUIRED --
# 1. MARK VECTORS ARE STORED IN STARAD AND STARAD +6.
# 2. CATALOG VECTORS ARE STORED IN 6D AND 12D.
#
# DEBRIS --

#   COUNT* $$/R54
W('14,3256', 0o43020, 'CHKSDATA', 'STQ', 'SET', kind='interp', line=844)
W('14,3257', 0o02745, '', '', 'QMIN', kind='operand', line=845)
W('14,3260', 0o00074, '', '', 'FREEFLAG', kind='operand', line=846)
W('14,3261', 0o77760, 'CHKSAB', 'AXC,1', '', 'SET X1 TO STORE EPHEMERIS DATA', kind='interp', line=847)
W('14,3262', 0o02706, '', '', 'STARAD', kind='operand', line=848)

W('14,3263', 0o47773, 'CHKSB', 'VLOAD*', 'DOT*', 'CAL. ANGLE THETA', kind='interp', line=850)
W('14,3264', 0o00001, '', '', '0,1', kind='operand', line=851)
W('14,3265', 0o00007, '', '', '6,1', kind='operand', line=852)
W('14,3266', 0o65552, '', 'SL1', 'ACOS', kind='interp', line=853)
W('14,3267', 0o00025, '', 'STORE', 'THETA', kind='interp', line=854)
W('14,3270', 0o43014, '', 'BOFF', 'INVERT', 'BRANCH TO CHKSD IF THIS IS 2ND PASS', kind='interp', line=855)
W('14,3271', 0o00354, '', '', 'FREEFLAG', kind='operand', line=856)
W('14,3272', 0o31302, '', '', 'CHKSD', kind='operand', line=857)
W('14,3273', 0o00174, '', '', 'FREEFLAG', 'CLEAR FREEFLAG', kind='operand', line=858)
W('14,3274', 0o71360, '', 'AXC,1', 'DLOAD', 'SET X1 TO MARK ANGLES', kind='interp', line=859)
W('14,3275', 0o00006, '', '', '6D', kind='operand', line=860)
W('14,3276', 0o00025, '', '', 'THETA', kind='operand', line=861)
W('14,3277', 0o00023, '', 'STORE', '18D', kind='interp', line=862)
W('14,3300', 0o77650, '', 'GOTO', kind='interp', line=863)
W('14,3301', 0o31263, '', '', 'CHKSB', 'RETURN TO CAL. 2ND ANGLE', kind='operand', line=864)
W('14,3302', 0o45345, 'CHKSD', 'DLOAD', 'DSU', kind='interp', line=865)
W('14,3303', 0o00025, '', '', 'THETA', kind='operand', line=866)
W('14,3304', 0o00023, '', '', '18D', kind='operand', line=867)
W('14,3305', 0o47046, '', 'ABS', 'RTB', 'COMPUTE POS DIFF', kind='interp', line=868)
W('14,3306', 0o21612, '', '', 'SGNAGREE', kind='operand', line=869)
W('14,3307', 0o01046, '', 'STORE', 'NORMTEM1', kind='interp', line=870)
W('14,3310', 0o77414, '', 'SET', 'EXIT', kind='interp', line=871)
W('14,3311', 0o00074, '', '', 'FREEFLAG', kind='operand', line=872)
W('14,3312', 0o33326, '', 'CAF', 'VB6N5', line=873)
W('14,3313', 0o04616, '', 'TC', 'BANKCALL', line=874)
W('14,3314', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=875)
W('14,3315', 0o16001, '', 'TCF', 'GOTOPOOH', line=876)
W('14,3316', 0o03323, '', 'TC', 'CHKSDA', 'PROCEED', line=877)
W('14,3317', 0o06037, '', 'TC', 'INTPRET', line=878)
W('14,3320', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=879)
W('14,3321', 0o00274, '', '', 'FREEFLAG', kind='operand', line=880)
W('14,3322', 0o02745, '', '', 'QMIN', kind='operand', line=881)
W('14,3323', 0o06037, 'CHKSDA', 'TC', 'INTPRET', line=882)
# Page 947
W('14,3324', 0o77650, '', 'GOTO', kind='interp', line=884)
W('14,3325', 0o02745, '', '', 'QMIN', kind='operand', line=885)
W('14,3326', 0o01405, 'VB6N5', 'VN', '605', kind='data', line=886)

# NAME -- CAL53A
# FUNCTION -- COMPUTE DESIRED GIMBAL ANGLES AND COARSE ALIGN IF NECESSARY
# CALLING SEQUENCE -- CALL CAL53A
# INPUT -- X,Y,ZSMD, CDUX,Y,Z
# DESIRED GIMBAL ANGLES -- THETAD,+1,+2
# OUTPUT -- THE IMU COORDINATES AT STORED IN REFSMMAT
# SUBROUTINES -- S52.2, IMUCOARSE, IMUFINE

#   COUNT* $$/R50
W('14,3327', 0o77624, 'CAL53A', 'CALL', kind='interp', line=897)
W('14,3330', 0o31617, '', '', 'S52.2', 'MAKE ONE FINAL COMP OF GIMBAL ANGLES', kind='operand', line=898)
W('14,3331', 0o66234, '', 'RTB', 'SSP', kind='interp', line=899)
W('14,3332', 0o31413, '', '', 'RDCDUS', 'READ CDUS', kind='operand', line=900)
W('14,3333', 0o00051, '', '', 'S1', kind='operand', line=901)
W('14,3334', 0o00001, '', '', '1', kind='operand', line=902)
W('14,3335', 0o40370, '', 'AXT,1', 'SETPD', kind='interp', line=903)
W('14,3336', 0o00003, '', '', '3', kind='operand', line=904)
W('14,3337', 0o00005, '', '', '4', kind='operand', line=905)
W('14,3340', 0o70543, 'CALOOP', 'DLOAD*', 'SR1', kind='interp', line=906)
W('14,3341', 0o00325, '', '', 'THETAD +3D,1', kind='operand', line=907)
W('14,3342', 0o70523, '', 'PDDL*', 'SR1', kind='interp', line=908)
W('14,3343', 0o00005, '', '', '4,1', kind='operand', line=909)
W('14,3344', 0o51425, '', 'DSU', 'ABS', kind='interp', line=910)
W('14,3345', 0o45206, '', 'PUSH', 'DSU', kind='interp', line=911)
W('14,3346', 0o31412, '', '', 'DEGREE1', kind='operand', line=912)
W('14,3347', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=913)
W('14,3350', 0o31366, '', '', 'CALOOP1', kind='operand', line=914)
W('14,3351', 0o51025, '', 'DSU', 'BPL', kind='interp', line=915)
W('14,3352', 0o31413, '', '', 'DEG359', kind='operand', line=916)
W('14,3353', 0o31366, '', '', 'CALOOP1', kind='operand', line=917)
W('14,3354', 0o77776, '', 'EXIT', kind='interp', line=918)
W('14,3355', 0o05353, '', 'TC', 'PHASCHNG', line=919)
W('14,3356', 0o04024, '', 'OCT', '04024', kind='data', line=920)

W('14,3357', 0o06037, '', 'TC', 'INTPRET', line=922)
W('14,3360', 0o77624, 'COARFINE', 'CALL', kind='interp', line=923)
W('14,3361', 0o31565, '', '', 'COARSE', kind='operand', line=924)
W('14,3362', 0o77624, '', 'CALL', kind='interp', line=925)
W('14,3363', 0o31602, '', '', 'NCOARSE', kind='operand', line=926)
W('14,3364', 0o77650, '', 'GOTO', kind='interp', line=927)
W('14,3365', 0o31370, '', '', 'FINEONLY', kind='operand', line=928)
W('14,3366', 0o77700, 'CALOOP1', 'TIX,1', kind='interp', line=929)
W('14,3367', 0o31340, '', '', 'CALOOP', kind='operand', line=930)
W('14,3370', 0o75160, 'FINEONLY', 'AXC,1', 'AXC,2', kind='interp', line=931)
W('14,3371', 0o02642, '', '', 'XSM', kind='operand', line=932)
W('14,3372', 0o01733, '', '', 'REFSMMAT', kind='operand', line=933)
W('14,3373', 0o77624, '', 'CALL', kind='interp', line=934)
W('14,3374', 0o31377, '', '', 'MATMOVE', kind='operand', line=935)
# Page 948
W('14,3375', 0o77650, '', 'GOTO', kind='interp', line=937)
W('14,3376', 0o32161, '', '', 'COARSRET', kind='operand', line=938)
W('14,3377', 0o77773, 'MATMOVE', 'VLOAD*', '', 'TRANSFER MATRIX', kind='interp', line=939)
W('14,3400', 0o00001, '', '', '0,1', kind='operand', line=940)
W('14,3401', 0o10001, '', 'STORE', '0,2', kind='interp', line=941)
W('14,3402', 0o77773, '', 'VLOAD*', kind='interp', line=942)
W('14,3403', 0o00007, '', '', '6D,1', kind='operand', line=943)
W('14,3404', 0o10007, '', 'STORE', '6D,2', kind='interp', line=944)
W('14,3405', 0o77773, '', 'VLOAD*', kind='interp', line=945)
W('14,3406', 0o00015, '', '', '12D,1', kind='operand', line=946)
W('14,3407', 0o10015, '', 'STORE', '12D,2', kind='interp', line=947)
W('14,3410', 0o77616, '', 'RVQ', kind='interp', line=948)
W('14,3411', 0o00056, 'DEGREE1', 'DEC', '46', '1 DEG SCALED CDU/2', kind='data', line=949)
W('14,3412', 0o37722, 'DEG359', 'DEC', '16338', '359 DEG SCALED CDU/2', kind='data', line=950)
W('14,3413', 0o00004, 'RDCDUS', 'INHINT', '', 'READ CDUS', line=951)
W('14,3414', 0o30032, '', 'CA', 'CDUX', line=952)
W('14,3415', 0o50120, '', 'INDEX', 'FIXLOC', line=953)
W('14,3416', 0o54001, '', 'TS', '1', line=954)
W('14,3417', 0o30033, '', 'CA', 'CDUY', line=955)
W('14,3420', 0o50120, '', 'INDEX', 'FIXLOC', line=956)
W('14,3421', 0o54002, '', 'TS', '2', line=957)
W('14,3422', 0o30034, '', 'CA', 'CDUZ', line=958)
W('14,3423', 0o50120, '', 'INDEX', 'FIXLOC', line=959)
W('14,3424', 0o54003, '', 'TS', '3', line=960)
W('14,3425', 0o00003, '', 'RELINT', line=961)
W('14,3426', 0o06061, '', 'TC', 'DANZIG', line=962)
#   COUNT* $$/INFLT

# Page 949
# NAME -- P51 -- IMU ORIENTATION DETERMINATION
# MOD. NO. 1    23 JAN 67                               LOG SECTION -- P51-P53
# MOD BY STURLAUGSON                                    ASSEMBLY SUNDANCE REV56
#
# FUNCTIONAL DESCRIPTION
# DETERMINES THE INERTIAL ORIENTATION OF THE IMU.  THE PROGRAM IS SELECTED BY DSKY ENTRY.  THE SIGHTING
# (AOTMARK) ROUTINE IS CALLED TO COLLECT AND PROCESS MARKED-STAR DATA.  AOTMARK (R53) RETURNS THE STAR NUMBER AND THE
# STAR LOS VECTOR IN STARAD +6.  TWO STARS ARE THUS SIGHTED.  THE ANGLE BETWEEN THE TWO STARS IS THEN CHECKED AT
# CHKSDATA (R54).  REFSMMAT IS THEN COMPUTED AT AXISGEN.
#
# CALLING SEQUENCE
# THE PROGRAM IS CALLED BY THE ASTRONAUT BY DSKY ENTRY.
#
# SUBROUTINES CALLED
# GOPERF3
# GOPERF1
# GODSPR
# IMUCOARS
# IMUFIN20
# AOTMARK (R53)
# CHKSDATA (R54)
# MKRELEAS
# AXISGEN
# MATMOVE
#
# ALARMS
# NONE.
#
# ERASABLE INITIALIZATION
# IMU ZERO FLAG SHOULD BE SET.
#
# OUTPUT
# REFSMMAT
# REFSMFLG
#
# DEBRIS
# WORK AREA
# STARAD
# STARIND
# BESTI
# BESTJ

#   COUNT* $$/P51
# Page 950
W('14,3427', 0o04616, 'P51', 'TC', 'BANKCALL', 'IS ISS ON - IF NOT, IMUCHK WILL SEND', line=1010)
W('14,3430', 0o33652, '', 'CADR', 'IMUCHK', 'ALARM CODE 210 AND EXIT VIA GOTOPOOH.', kind='data', line=1011)

W('14,3431', 0o34761, '', 'CAF', 'OCT15', line=1013)
W('14,3432', 0o04616, '', 'TC', 'BANKCALL', line=1014)
W('14,3433', 0o20623, '', 'CADR', 'GOPERF1', kind='data', line=1015)
W('14,3434', 0o06001, '', 'TC', 'GOTOPOOH', 'TERM.', line=1016)
W('14,3435', 0o13461, '', 'TCF', 'P51B', 'V33', line=1017)
W('14,3436', 0o05353, '', 'TC', 'PHASCHNG', line=1018)
W('14,3437', 0o04024, '', 'OCT', '04024', kind='data', line=1019)

W('14,3440', 0o34755, '', 'CAF', 'ZERO', line=1021)
W('14,3441', 0o54321, '', 'TS', 'THETAD', 'ZERO THE GIMBALS', line=1022)
W('14,3442', 0o54322, '', 'TS', 'THETAD +1', line=1023)
W('14,3443', 0o54323, '', 'TS', 'THETAD +2', line=1024)
W('14,3444', 0o35010, '', 'CAF', 'V06N22', line=1025)
W('14,3445', 0o04616, '', 'TC', 'BANKCALL', line=1026)
W('14,3446', 0o20446, '', 'CADR', 'GODSPRET', kind='data', line=1027)
W('14,3447', 0o33564, '', 'CAF', 'V41K', 'NOW DISPLAY COARSE ALIGN VERB 41', line=1028)
W('14,3450', 0o04616, '', 'TC', 'BANKCALL', line=1029)
W('14,3451', 0o20446, '', 'CADR', 'GODSPRET', kind='data', line=1030)
W('14,3452', 0o06037, '', 'TC', 'INTPRET', line=1031)
W('14,3453', 0o77624, '', 'CALL', kind='interp', line=1032)
W('14,3454', 0o31565, '', '', 'COARSE', kind='operand', line=1033)
W('14,3455', 0o77776, '', 'EXIT', kind='interp', line=1034)
W('14,3456', 0o05353, '', 'TC', 'PHASCHNG', line=1035)
W('14,3457', 0o04024, '', 'OCT', '04024', kind='data', line=1036)
W('14,3460', 0o13431, '', 'TCF', 'P51 +2', line=1037)

W('14,3461', 0o05353, 'P51B', 'TC', 'PHASCHNG', line=1039)
W('14,3462', 0o00014, '', 'OCT', '00014', kind='data', line=1040)
W('14,3463', 0o06037, '', 'TC', 'INTPRET', line=1041)
W('14,3464', 0o77624, '', 'CALL', kind='interp', line=1042)
W('14,3465', 0o31602, '', '', 'NCOARSE', kind='operand', line=1043)
W('14,3466', 0o40331, '', 'SSP', 'SETPD', kind='interp', line=1044)
W('14,3467', 0o02760, '', '', 'STARIND', 'INDEX -- STAR 1 OR 2', kind='operand', line=1045)
W('14,3470', 0o00000, '', '', '0', kind='operand', line=1046)
W('14,3471', 0o00001, '', '', '0', kind='operand', line=1047)
W('14,3472', 0o77776, 'P51C', 'EXIT', kind='interp', line=1048)
W('14,3473', 0o05353, '', 'TC', 'PHASCHNG', line=1049)
W('14,3474', 0o04024, '', 'OCT', '04024', kind='data', line=1050)

W('14,3475', 0o04616, '', 'TC', 'BANKCALL', line=1052)
W('14,3476', 0o16000, '', 'CADR', 'AOTMARK', 'R53', kind='data', line=1053)
W('14,3477', 0o04616, '', 'TC', 'BANKCALL', line=1054)
W('14,3500', 0o17712, '', 'CADR', 'AOTSTALL', kind='data', line=1055)
W('14,3501', 0o05711, '', 'TC', 'CURTAINS', line=1056)
W('14,3502', 0o11757, '', 'CCS', 'STARIND', line=1057)
W('14,3503', 0o13511, '', 'TCF', 'P51D +1', line=1058)
W('14,3504', 0o06037, '', 'TC', 'INTPRET', line=1059)
# Page 951
W('14,3505', 0o77775, '', 'VLOAD', kind='interp', line=1061)
W('14,3506', 0o02715, '', '', 'STARAD +6', kind='operand', line=1062)
W('14,3507', 0o02761, '', 'STORE', 'STARSAV1', kind='interp', line=1063)
W('14,3510', 0o77776, 'P51D', 'EXIT', kind='interp', line=1064)
W('14,3511', 0o05353, '', 'TC', 'PHASCHNG', line=1065)
W('14,3512', 0o04024, '', 'OCT', '04024', kind='data', line=1066)

W('14,3513', 0o11757, '', 'CCS', 'STARIND', line=1068)
W('14,3514', 0o13530, '', 'TCF', 'P51E', line=1069)
W('14,3515', 0o05353, '', 'TC', 'PHASCHNG', line=1070)
W('14,3516', 0o04024, '', 'OCT', '04024', kind='data', line=1071)

W('14,3517', 0o06037, '', 'TC', 'INTPRET', line=1073)
W('14,3520', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=1074)
W('14,3521', 0o03562, '', '', 'TSIGHT', kind='operand', line=1075)
W('14,3522', 0o32472, '', '', 'PLANET', kind='operand', line=1076)
W('14,3523', 0o03554, '', 'STORE', 'PLANVEC', kind='interp', line=1077)
W('14,3524', 0o77776, '', 'EXIT', kind='interp', line=1078)
W('14,3525', 0o34753, '', 'CAF', 'BIT1', line=1079)
W('14,3526', 0o55757, '', 'TS', 'STARIND', line=1080)
W('14,3527', 0o13473, '', 'TCF', 'P51C +1', 'DO SECOND STAR', line=1081)
W('14,3530', 0o05353, 'P51E', 'TC', 'PHASCHNG', line=1082)
W('14,3531', 0o04024, '', 'OCT', '04024', kind='data', line=1083)

W('14,3532', 0o06037, '', 'TC', 'INTPRET', line=1085)
W('14,3533', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=1086)
W('14,3534', 0o03562, '', '', 'TSIGHT', kind='operand', line=1087)
W('14,3535', 0o32472, '', '', 'PLANET', kind='operand', line=1088)
W('14,3536', 0o24015, '', 'STOVL', '12D', kind='interp', line=1089)
W('14,3537', 0o03554, '', '', 'PLANVEC', kind='operand', line=1090)
W('14,3540', 0o24007, '', 'STOVL', '6D', kind='interp', line=1091)
W('14,3541', 0o02761, '', '', 'STARSAV1', kind='operand', line=1092)
W('14,3542', 0o26707, '', 'STOVL', 'STARAD', kind='interp', line=1093)
W('14,3543', 0o02767, '', '', 'STARSAV2', kind='operand', line=1094)
W('14,3544', 0o36715, '', 'STCALL', 'STARAD +6', kind='interp', line=1095)
W('14,3545', 0o31256, '', '', 'CHKSDATA', 'CHECK STAR ANGLES IN STARAD AND', kind='operand', line=1096)
W('14,3546', 0o77414, '', 'BON', 'EXIT', kind='interp', line=1097)
W('14,3547', 0o00314, '', '', 'FREEFLAG', kind='operand', line=1098)
W('14,3550', 0o31552, '', '', 'P51G', kind='operand', line=1099)
W('14,3551', 0o03431, '', 'TC', 'P51 +2', line=1100)
W('14,3552', 0o77624, 'P51G', 'CALL', kind='interp', line=1101)
W('14,3553', 0o47441, '', '', 'AXISGEN', 'COME BACK WITH REFSMMAT IN XDC', kind='operand', line=1102)
W('14,3554', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=1103)
W('14,3555', 0o02664, '', '', 'XDC', kind='operand', line=1104)
W('14,3556', 0o01733, '', '', 'REFSMMAT', kind='operand', line=1105)
W('14,3557', 0o77624, '', 'CALL', kind='interp', line=1106)
W('14,3560', 0o31377, '', '', 'MATMOVE', kind='operand', line=1107)
W('14,3561', 0o77414, '', 'SET', 'EXIT', kind='interp', line=1108)
W('14,3562', 0o01462, '', '', 'REFSMFLG', kind='operand', line=1109)
W('14,3563', 0o06001, '', 'TC', 'GOTOPOOH', 'FINIS', line=1110)
# Page 952
W('14,3564', 0o12200, 'V41K', 'VN', '4100', kind='data', line=1112)
W('14,3565', 0o77776, 'COARSE', 'EXIT', kind='interp', line=1113)
W('14,3566', 0o04616, '', 'TC', 'BANKCALL', line=1114)
W('14,3567', 0o17000, '', 'CADR', 'IMUCOARS', kind='data', line=1115)
W('14,3570', 0o04616, '', 'TC', 'BANKCALL', line=1116)
W('14,3571', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=1117)
W('14,3572', 0o05711, '', 'TC', 'CURTAINS', line=1118)
W('14,3573', 0o04616, '', 'TC', 'BANKCALL', line=1119)
W('14,3574', 0o17210, '', 'CADR', 'IMUFINE', kind='data', line=1120)
W('14,3575', 0o04616, '', 'TC', 'BANKCALL', line=1121)
W('14,3576', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=1122)
W('14,3577', 0o05711, '', 'TC', 'CURTAINS', line=1123)
W('14,3600', 0o06037, '', 'TC', 'INTPRET', line=1124)
W('14,3601', 0o77616, '', 'RVQ', kind='interp', line=1125)
W('14,3602', 0o77776, 'NCOARSE', 'EXIT', kind='interp', line=1126)
W('14,3603', 0o30025, '', 'CA', 'TIME1', line=1127)
W('14,3604', 0o55075, '', 'TS', '1/PIPADT', line=1128)
W('14,3605', 0o44755, '', 'CS', 'ZERO', line=1129)
W('14,3606', 0o54037, '', 'TS', 'PIPAX', line=1130)
W('14,3607', 0o54040, '', 'TS', 'PIPAY', line=1131)
W('14,3610', 0o54041, '', 'TS', 'PIPAZ', line=1132)
W('14,3611', 0o06037, '', 'TC', 'INTPRET', line=1133)
W('14,3612', 0o77775, '', 'VLOAD', kind='interp', line=1134)
W('14,3613', 0o24007, '', '', 'ZEROVEC', kind='operand', line=1135)
W('14,3614', 0o01472, '', 'STORE', 'GCOMP', kind='interp', line=1136)
W('14,3615', 0o43414, '', 'SET', 'RVQ', kind='interp', line=1137)
W('14,3616', 0o01060, '', '', 'DRIFTFLG', kind='operand', line=1138)

# Page 953
# NAME -- S52.2
# FUNCTION -- COMPUTE GIMBAL ANGLES FOR DESIRED SM AND PRESENT VEHICLE
# CALL -- CALL S52.2
# INPUT -- X,Y,ZSMD
# OUTPUT -- OGC,IGC,MGC,THETAD,+1,+2
# SUBROUTINES -- CDUTRIG, CALCSMSC, MATMOVE, CALCGA

#   COUNT* $$/S52.1
W('14,3617', 0o45020, 'S52.2', 'STQ', 'CALL', kind='interp', line=1149)
W('14,3620', 0o02746, '', '', 'QMAJ', kind='operand', line=1150)
W('14,3621', 0o47537, '', '', 'CDUTRIG', kind='operand', line=1151)
W('14,3622', 0o77624, '', 'CALL', kind='interp', line=1152)
W('14,3623', 0o20030, '', '', 'CALCSMSC', kind='operand', line=1153)
W('14,3624', 0o66370, '', 'AXT,1', 'SSP', kind='interp', line=1154)
W('14,3625', 0o00022, '', '', '18D', kind='operand', line=1155)
W('14,3626', 0o00051, '', '', 'S1', kind='operand', line=1156)
W('14,3627', 0o00006, '', '', '6D', kind='operand', line=1157)
W('14,3630', 0o61373, 'S52.2A', 'VLOAD*', 'VXM', kind='interp', line=1158)
W('14,3631', 0o02707, '', '', 'XNB +18D,1', kind='operand', line=1159)
W('14,3632', 0o01734, '', '', 'REFSMMAT', kind='operand', line=1160)
W('14,3633', 0o77656, '', 'UNIT', kind='interp', line=1161)
W('14,3634', 0o06707, '', 'STORE', 'XNB +18D,1', kind='interp', line=1162)
W('14,3635', 0o77700, '', 'TIX,1', kind='interp', line=1163)
W('14,3636', 0o31630, '', '', 'S52.2A', kind='operand', line=1164)
W('14,3637', 0o75160, 'S52.2.1', 'AXC,1', 'AXC,2', kind='interp', line=1165)
W('14,3640', 0o03606, '', '', 'XSMD', kind='operand', line=1166)
W('14,3641', 0o02642, '', '', 'XSM', kind='operand', line=1167)
W('14,3642', 0o77624, '', 'CALL', kind='interp', line=1168)
W('14,3643', 0o31377, '', '', 'MATMOVE', kind='operand', line=1169)
W('14,3644', 0o77624, '', 'CALL', kind='interp', line=1170)
W('14,3645', 0o47353, '', '', 'CALCGA', kind='operand', line=1171)
W('14,3646', 0o77650, '', 'GOTO', kind='interp', line=1172)
W('14,3647', 0o02746, '', '', 'QMAJ', kind='operand', line=1173)

# Page 954
# NAME -- S52.3
# FUNCTION --   XSMD= UNIT R
# YSMD= UNIT(V X R)
# ZSMD= UNIT(XSMD X YSMD)
# CALL --       DLOAD   CALL
# TALIGN
# S52.3
# INPUT --      TIME OF ALIGNMENT IN MPAC
# OUTPUT --     X,Y,ZSMD
# SUBROUTINES -- CSMCONIC

#   COUNT* $$/S52.3
W('14,3650', 0o77620, 'S52.3', 'STQ', kind='interp', line=1188)
W('14,3651', 0o02746, '', '', 'QMAJ', kind='operand', line=1189)
W('14,3652', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1190)
W('14,3653', 0o27100, '', '', 'LEMCONIC', kind='operand', line=1191)
W('14,3654', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=1192)
W('14,3655', 0o00001, '', '', 'RATT', kind='operand', line=1193)
W('14,3656', 0o27607, '', 'STOVL', 'XSMD', kind='interp', line=1194)
W('14,3657', 0o00007, '', '', 'VATT', kind='operand', line=1195)
W('14,3660', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1196)
W('14,3661', 0o00001, '', '', 'RATT', kind='operand', line=1197)
W('14,3662', 0o27615, '', 'STOVL', 'YSMD', kind='interp', line=1198)
W('14,3663', 0o03607, '', '', 'XSMD', kind='operand', line=1199)
W('14,3664', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1200)
W('14,3665', 0o03615, '', '', 'YSMD', kind='operand', line=1201)
W('14,3666', 0o37623, '', 'STCALL', 'ZSMD', kind='interp', line=1202)
W('14,3667', 0o02746, '', '', 'QMAJ', kind='operand', line=1203)

# Page 955
# NAME -- R52 (AUTOMATIC OPTICS POSITIONING ROUTINE)
#
# FUNCTION -- POINT THE AOT APTICS AXIS BY MANEUVERING THE LEM TO A NAVIGATION
# STAR SELECTED BY ALIGNMENT PROGRAMS OR DSKY INPUT
#
# CALLING -- CALL R52
#
# INPUT -- BESTI AND BESTJ (STAR CODES TIMES 6)
#
# OUTPUT -- STAR CODE IN BITS 1-6, DETENT CODE IN BITS 7-9
# (NO CHECK IS MADE TO INSURE THE DETENT CODE TO BE VALID)
# POINTVSM-1/2 UNIT NAV STAR VEC IN SM
# SCAXIS-AOT OPTIC AXIS VEC IN NB X-Z PLANE
#
# SUBROUT -- R60LEM

#   COUNT* $$/R52
W('14,3670', 0o77420, 'R52', 'STQ', 'EXIT', kind='interp', line=1223)
W('14,3671', 0o03665, '', '', 'SAVQR52', kind='operand', line=1224)
W('14,3672', 0o51757, '', 'INDEX', 'STARIND', line=1225)
W('14,3673', 0o31755, '', 'CA', 'BESTI', 'PICK UP STARCODE DETERMINED BY R56', line=1226)
W('14,3674', 0o00006, '', 'EXTEND', line=1227)
W('14,3675', 0o73771, '', 'MP', '1/6TH', line=1228)
W('14,3676', 0o64744, '', 'AD', 'BIT8', 'SET DETENT POSITION 2', line=1229)
W('14,3677', 0o54735, '', 'TS', 'STARCODE', 'SCALE AND STORE IN STARCODE', line=1230)

W('14,3700', 0o33772, 'R52A', 'CAF', 'V01N70', line=1232)
W('14,3701', 0o04616, '', 'TC', 'BANKCALL', line=1233)
W('14,3702', 0o20476, '', 'CADR', 'GOFLASH', 'DISPLAY STARCODE AND WAIT FOR RESPONSE', kind='data', line=1234)
W('14,3703', 0o06001, '', 'TC', 'GOTOPOOH', 'V34 -- TERMINATE', line=1235)
W('14,3704', 0o13706, '', 'TCF', 'R52B', 'V33 -- PROCEED TO ORIENT LEM', line=1236)
W('14,3705', 0o13700, '', 'TCF', 'R52A', 'ENTER -- SELECT NEW STARCODE -- RECYCLE', line=1237)

W('14,3706', 0o05516, 'R52B', 'TC', 'DOWNFLAG', line=1239)
W('14,3707', 0o00124, '', 'ADRES', '3AXISFLG', 'BIT6 OF FLAGWRD5 ZERO TO ALLOW VECPOINT', kind='data', line=1240)
W('14,3710', 0o30735, '', 'CA', 'STARCODE', 'GRAB DETENT CODE', line=1241)
W('14,3711', 0o77744, '', 'MASK', 'HIGH9', line=1242)
W('14,3712', 0o00006, '', 'EXTEND', line=1243)
W('14,3713', 0o74743, '', 'MP', 'BIT9', line=1244)
W('14,3714', 0o54001, '', 'TS', 'L', 'TEMP STORE DETENT', line=1245)

W('14,3715', 0o00006, '', 'EXTEND', line=1247)
W('14,3716', 0o63734, '', 'BZMF', 'GETAZEL', 'CODE 0, COAS CALIBRATION', line=1248)

W('14,3717', 0o65660, '', 'AD', 'NEG7', line=1250)
W('14,3720', 0o00006, '', 'EXTEND', line=1251)
W('14,3721', 0o13734, '', 'BZF', 'GETAZEL', 'CODE 7, COAS SIGHTING', line=1252)

#   EBANK= XYMARK
W('14,3722', 0o35016, '', 'CA', 'EBANK7', line=1255)
W('14,3723', 0o54003, '', 'TS', 'EBANK', line=1256)
# Page 956
W('14,3724', 0o50001, '', 'INDEX', 'L', line=1258)
W('14,3725', 0o31403, '', 'CA', 'AOTAZ -1', 'PICK UP AZ CORRESPONDING TO DETENT', line=1259)
W('14,3726', 0o54001, '', 'TS', 'L', line=1260)
#   EBANK= XSM
W('14,3727', 0o35014, '', 'CA', 'EBANK5', "CHANGE TO EBANK5 BUT DON'T DISTURB L", line=1262)
W('14,3730', 0o54003, '', 'TS', 'EBANK', line=1263)
W('14,3731', 0o34737, '', 'CA', 'BIT13', 'SET ELV TO 45 DEG', line=1264)
W('14,3732', 0o56001, '', 'XCH', 'L', 'SET C(A)=AZ, C(L)=45 DEG', line=1265)
W('14,3733', 0o13744, '', 'TCF', 'AZEL', 'GO COMP OPTIC AXIS', line=1266)

W('14,3734', 0o33773, 'GETAZEL', 'CAF', 'V06N87', 'CODE 0 OR 7, GET AZ AND EL KEY IN', line=1268)
W('14,3735', 0o04616, '', 'TC', 'BANKCALL', line=1269)
W('14,3736', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=1270)
W('14,3737', 0o06001, '', 'TC', 'GOTOPOOH', 'V34 -- TERMINATE', line=1271)
W('14,3740', 0o13742, '', 'TCF', '+2', 'PROCEED -- CALC OPTIC AXIS', line=1272)
W('14,3741', 0o13734, '', 'TCF', 'GETAZEL', 'ENTER -- RECYCLE', line=1273)

W('14,3742', 0o00006, '', 'EXTEND', line=1275)
W('14,3743', 0o31350, '', 'DCA', 'AZ', "PICK UP AZ AND EL IN SP 2'S COMP", line=1276)
W('14,3744', 0o50120, 'AZEL', 'INDEX', 'FIXLOC', 'JAM AZ AND EL IN 8 AND 9 OF VAC', line=1277)
W('14,3745', 0o52011, '', 'DXCH', '8D', line=1278)
W('14,3746', 0o06037, '', 'TC', 'INTPRET', line=1279)
W('14,3747', 0o77624, '', 'CALL', '', 'GO COMPUTE OPTIC AXIS AND STORE IN', kind='interp', line=1280)
W('14,3750', 0o10536, '', '', 'OANB', 'SCAXIS IN NB COORDS', kind='operand', line=1281)
W('14,3751', 0o45034, '', 'RTB', 'CALL', kind='interp', line=1282)
W('14,3752', 0o21573, '', '', 'LOADTIME', kind='operand', line=1283)
W('14,3753', 0o32472, '', '', 'PLANET', kind='operand', line=1284)
W('14,3754', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=1285)
W('14,3755', 0o01734, '', '', 'REFSMMAT', kind='operand', line=1286)
W('14,3756', 0o03773, '', 'STORE', 'POINTVSM', 'STORE FOR VECPOINT', kind='interp', line=1287)

W('14,3757', 0o77776, '', 'EXIT', kind='interp', line=1289)
W('14,3760', 0o04616, '', 'TC', 'BANKCALL', line=1290)
W('14,3761', 0o54123, '', 'CADR', 'R60LEM', 'GO TORQUE LEM OPTIC AXIS TO STAR LOS', kind='data', line=1291)

W('14,3762', 0o37744, '', 'CAF', 'HIGH9', 'IF COAS CALIBRATION CODE 0.  RECYCLE', line=1293)
W('14,3763', 0o70735, '', 'MASK', 'STARCODE', line=1294)
W('14,3764', 0o00006, '', 'EXTEND', line=1295)
W('14,3765', 0o13700, '', 'BZF', 'R52A', line=1296)

W('14,3766', 0o06037, '', 'TC', 'INTPRET', 'RETURN FROM KALCMANU', line=1298)
W('14,3767', 0o77650, '', 'GOTO', kind='interp', line=1299)
W('14,3770', 0o03665, '', '', 'SAVQR52', 'RETURN TO CALLER', kind='operand', line=1300)

W('14,3771', 0o05253, '1/6TH', 'DEC', '.1666667', kind='data', line=1302)
W('14,3772', 0o00306, 'V01N70', 'VN', '0170', kind='data', line=1303)
W('14,3773', 0o01527, 'V06N87', 'VN', '687', kind='data', line=1304)

# Page 957
# LUNAR SURFACE STAR ACQUISITION

#   BANK 15
#   SETLOC P50S
#   BANK
#   COUNT* $$/R59

W('15,2245', 0o40077, 'R59', 'CS', 'FLAGWRD3', line=1314)
W('15,2246', 0o74737, '', 'MASK', 'REFSMBIT', 'IF REFSMMAT FLAG CLEAR BYPASS STAR ACQUIRE', line=1315)
W('15,2247', 0o10000, '', 'CCS', 'A', line=1316)
W('15,2250', 0o12455, '', 'TCF', 'R59OUT', 'NO REFSMMAT GO TO AOTMARK', line=1317)

W('15,2251', 0o32463, '', 'CAF', 'V01N70*', 'SELECT STAR CODE FOR ACQUISITION', line=1319)
W('15,2252', 0o04616, '', 'TC', 'BANKCALL', line=1320)
W('15,2253', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=1321)
W('15,2254', 0o06001, '', 'TC', 'GOTOPOOH', 'V34 -- TERMINATE', line=1322)
W('15,2255', 0o12257, '', 'TCF', 'R59A', 'V33 -- PROCEED', line=1323)
W('15,2256', 0o12245, '', 'TCF', 'R59', 'V32 -- RECYCLE', line=1324)

W('15,2257', 0o47744, 'R59A', 'CS', 'HIGH9', 'GRAB STARCODE FOR INDEX', line=1326)
W('15,2260', 0o70735, '', 'MASK', 'AOTCODE', line=1327)
W('15,2261', 0o00006, '', 'EXTEND', line=1328)
W('15,2262', 0o76242, '', 'MP', 'REVCNT', 'JUST 6', line=1329)
W('15,2263', 0o56001, '', 'XCH', 'L', line=1330)
W('15,2264', 0o51757, '', 'INDEX', 'STARIND', line=1331)
W('15,2265', 0o55755, '', 'TS', 'BESTI', line=1332)
W('15,2266', 0o50120, '', 'INDEX', 'FIXLOC', line=1333)
W('15,2267', 0o54046, '', 'TS', 'X1', 'CODE X 6 FOR CATLOG STAR INDEX', line=1334)
W('15,2270', 0o00006, '', 'EXTEND', line=1335)
W('15,2271', 0o12455, '', 'BZF', 'R59OUT', 'BYPASS ACQUISITION IF NOT CATLOG STAR', line=1336)
W('15,2272', 0o40000, '', 'COM', line=1337)
W('15,2273', 0o62561, '', 'AD', 'DEC227', line=1338)
W('15,2274', 0o00006, '', 'EXTEND', line=1339)
W('15,2275', 0o62455, '', 'BZMF', 'R59OUT', line=1340)

W('15,2276', 0o06037, '', 'TC', 'INTPRET', line=1342)
W('15,2277', 0o64373, '', 'VLOAD*', 'MXV', kind='interp', line=1343)
W('15,2300', 0o30347, '', '', 'CATLOG,1', 'GRAB STAR VECTOR', kind='operand', line=1344)
W('15,2301', 0o01734, '', '', 'REFSMMAT', 'TRANSFORM TO SM', kind='operand', line=1345)
W('15,2302', 0o45056, '', 'UNIT', 'CALL', kind='interp', line=1346)
W('15,2303', 0o47646, '', '', 'CDU*SMNB', kind='operand', line=1347)
W('15,2304', 0o02731, '', 'STORE', 'STAR', 'TEMP STORE STAR VEC(NB)', kind='interp', line=1348)
W('15,2305', 0o77776, '', 'EXIT', kind='interp', line=1349)

W('15,2306', 0o34753, '', 'CAF', 'BIT1', 'INITIALIZE AZ POSITION COD TO 1 (-60)', line=1351)
W('15,2307', 0o55242, '', 'TS', 'POSCODE', line=1352)

#   EBANK= XYMARK
W('15,2310', 0o35016, 'INCAZ', 'CA', 'EBANK7', line=1355)
W('15,2311', 0o54003, '', 'TS', 'EBANK', line=1356)

# Page 958
W('15,2312', 0o51242, '', 'INDEX', 'POSCODE', line=1359)
W('15,2313', 0o31403, '', 'CA', 'AOTAZ -1', 'PICK UP AZ CORRESPONDING TO POSCODE', line=1360)
W('15,2314', 0o54001, '', 'TS', 'L', line=1361)

#   EBANK= XSM
W('15,2315', 0o35014, '', 'CA', 'EBANK5', line=1364)
W('15,2316', 0o54003, '', 'TS', 'EBANK', line=1365)

W('15,2317', 0o34737, '', 'CA', 'BIT13', 'SET ELV TO 45 DEG', line=1367)
W('15,2320', 0o56001, '', 'XCH', 'L', 'SET C(A)=AZ, C(L)=45 DEG', line=1368)
W('15,2321', 0o55745, '', 'TS', 'QMIN', 'STORE QMIN=AZ FOR LATER', line=1369)
W('15,2322', 0o50120, '', 'INDEX', 'FIXLOC', line=1370)
W('15,2323', 0o52011, '', 'DXCH', '8D', 'JAM AZ IN 8D, 45 DEG IN 9D FOR OANB', line=1371)

W('15,2324', 0o06037, '', 'TC', 'INTPRET', line=1373)
W('15,2325', 0o77624, '', 'CALL', kind='interp', line=1374)
W('15,2326', 0o10536, '', '', 'OANB', 'GO CALC OPTIC AXIS WRT NB', kind='operand', line=1375)
W('15,2327', 0o50375, '', 'VLOAD', 'DOT', kind='interp', line=1376)
W('15,2330', 0o02731, '', '', 'STAR', 'DOT STAR WITH OA', kind='operand', line=1377)
W('15,2331', 0o03765, '', '', 'SCAXIS', kind='operand', line=1378)
W('15,2332', 0o65552, '', 'SL1', 'ARCCOS', kind='interp', line=1379)
W('15,2333', 0o00031, '', 'STORE', '24D', 'TEMP STORE ARCCOS(STAR.OPTAXIS)', kind='interp', line=1380)

W('15,2334', 0o51025, '', 'DSU', 'BPL', kind='interp', line=1382)
W('15,2335', 0o32466, '', '', 'DEG30', 'SEE IF STAR IN AOT FIELD-OF-VIEW', kind='operand', line=1383)
W('15,2336', 0o32420, '', '', 'NXAX', 'NOT IN FIELD -- TRY NEXT POSITION', kind='operand', line=1384)
W('15,2337', 0o45345, '', 'DLOAD', 'DSU', 'SEE IF STAR AT FIELD CENTER', kind='interp', line=1385)
W('15,2340', 0o00031, '', '', '24D', kind='operand', line=1386)
W('15,2341', 0o32470, '', '', 'DEG.5', kind='operand', line=1387)
W('15,2342', 0o71240, '', 'BMN', 'DLOAD', 'CALC SPIRAL AND CURSOR', kind='interp', line=1388)
W('15,2343', 0o32413, '', '', 'ZSPCR', 'GO ZERO CURSOR AND SPIRAL', kind='operand', line=1389)
W('15,2344', 0o00031, '', '', '24D', 'GET SPIRAL', kind='operand', line=1390)
W('15,2345', 0o42405, '', 'DMP', 'SL4', kind='interp', line=1391)
W('15,2346', 0o25764, '', '', '3/4', '12 SCALED AT 16', kind='operand', line=1392)
W('15,2347', 0o24031, '', 'STOVL', '24D', '12(ARCCOS(AO.STAR)) SCALED IN REVS', kind='interp', line=1393)

W('15,2350', 0o03765, '', '', 'SCAXIS', 'OA', kind='operand', line=1395)
W('15,2351', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1396)
W('15,2352', 0o24005, '', '', 'XUNIT', kind='operand', line=1397)
W('15,2353', 0o47206, '', 'PUSH', 'VXV', 'OA X UNITX    PD 0-5', kind='interp', line=1398)
W('15,2354', 0o03765, '', '', 'SCAXIS', kind='operand', line=1399)
W('15,2355', 0o77676, '', 'VCOMP', kind='interp', line=1400)
W('15,2356', 0o63256, '', 'UNIT', 'PDVL', 'UNIT(OA X (OA X UNITX))       PD 6-11', kind='interp', line=1401)
W('15,2357', 0o03765, '', '', 'SCAXIS', kind='operand', line=1402)
W('15,2360', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=1403)
W('15,2361', 0o02731, '', '', 'STAR', kind='operand', line=1404)
W('15,2362', 0o50206, '', 'PUSH', 'DOT', '1/2(OA X STAR)        PD 12-17', kind='interp', line=1405)
W('15,2363', 0o00001, '', '', '0', 'DOT WITH 1/2(OA X UNITX) FOR YROT', kind='operand', line=1406)
W('15,2364', 0o65552, '', 'SL1', 'ARCCOS', kind='interp', line=1407)
W('15,2365', 0o24033, '', 'STOVL', '26D', 'STORE THET SCALED IN REVS', kind='interp', line=1408)
# Page 959
W('15,2366', 0o77641, '', 'DOT', '', 'UP 12-17, UP 6-11 FOR C2', kind='interp', line=1410)
W('15,2367', 0o71244, '', 'BPL', 'DLOAD', 'IF THET NEG -- GET 360-THET', kind='interp', line=1411)
W('15,2370', 0o32375, '', '', 'R59D', kind='operand', line=1412)
W('15,2371', 0o32047, '', '', 'ABOUTONE', kind='operand', line=1413)
W('15,2372', 0o77625, '', 'DSU', kind='interp', line=1414)
W('15,2373', 0o00033, '', '', '26D', kind='operand', line=1415)
W('15,2374', 0o00033, '', 'STORE', '26D', '360-THET SCALED IN REVS', kind='interp', line=1416)

W('15,2375', 0o70535, 'R59D', 'SLOAD', 'SR1', kind='interp', line=1418)
W('15,2376', 0o02746, '', '', 'QMIN', 'RESCALE AZ(N) TO REVS', kind='operand', line=1419)
W('15,2377', 0o41415, '', 'DAD', 'PUSH', 'PUSH YROT + AZ(N) REVS', kind='interp', line=1420)
W('15,2400', 0o00033, '', '', '26D', kind='operand', line=1421)
W('15,2401', 0o77634, '', 'RTB', kind='interp', line=1422)
W('15,2402', 0o21614, '', '', '1STO2S', kind='operand', line=1423)
W('15,2403', 0o15237, '', 'STODL', 'CURSOR', 'YROT IN 1/2 REVS', kind='interp', line=1424)
W('15,2404', 0o00031, '', '', '24D', 'LOAD SROT IN REVS', kind='operand', line=1425)
W('15,2405', 0o77615, '', 'DAD', '', '12(SEP) + YROT', kind='interp', line=1426)
W('15,2406', 0o77634, '', 'RTB', kind='interp', line=1427)
W('15,2407', 0o21614, '', '', '1STO2S', kind='operand', line=1428)
W('15,2410', 0o01241, '', 'STORE', 'SPIRAL', 'SROT IN 1/2 REVS', kind='interp', line=1429)
W('15,2411', 0o77776, '', 'EXIT', kind='interp', line=1430)
W('15,2412', 0o12437, '', 'TCF', '79DISP', 'GO DISPLAY CURSOR-SPIRAL-POS CODE', line=1431)

W('15,2413', 0o77776, 'ZSPCR', 'EXIT', kind='interp', line=1433)
W('15,2414', 0o34755, '', 'CAF', 'ZERO', 'STAR ALMOST OPTIC AXIS, ZERO CURSOR', line=1434)
W('15,2415', 0o55236, '', 'TS', 'CURSOR', 'AND SPIRAL ANGLES', line=1435)
W('15,2416', 0o55240, '', 'TS', 'SPIRAL', line=1436)
W('15,2417', 0o12437, '', 'TCF', '79DISP', line=1437)

W('15,2420', 0o77776, 'NXAX', 'EXIT', kind='interp', line=1439)
W('15,2421', 0o25242, '', 'INCR', 'POSCODE', line=1440)
W('15,2422', 0o41242, '', 'CS', 'POSCODE', line=1441)
W('15,2423', 0o64757, '', 'AD', 'SEVEN', line=1442)
W('15,2424', 0o00006, '', 'EXTEND', line=1443)
W('15,2425', 0o62427, '', 'BZMF', 'R59ALM', 'THIS STAR NOT AT ANY POSITION', line=1444)
W('15,2426', 0o12310, '', 'TCF', 'INCAZ', line=1445)

W('15,2427', 0o05567, 'R59ALM', 'TC', 'ALARM', "THIS STAR CAN'T BE LOCATED IN AOT FIELD", line=1447)
W('15,2430', 0o00404, '', 'OCT', '404', kind='data', line=1448)
W('15,2431', 0o35006, '', 'CAF', 'VB05N09', 'DISPLAY ALARM', line=1449)
W('15,2432', 0o04616, '', 'TC', 'BANKCALL', line=1450)
W('15,2433', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=1451)
W('15,2434', 0o16001, '', 'TCF', 'GOTOPOOH', 'VB34 -- TERMINATE', line=1452)
W('15,2435', 0o12455, '', 'TCF', 'R59OUT', 'VB33 -- PROCEED, GO WITHOUT ACQUIRE', line=1453)
W('15,2436', 0o12245, '', 'TCF', 'R59', 'VB32 -- RECYCLE AND TRY ANOTHER STAR', line=1454)

W('15,2437', 0o32464, '79DISP', 'CAF', 'V06N79', 'DISPLAY CURSOR, SPIRAL AND POS CODE', line=1456)
W('15,2440', 0o04616, '', 'TC', 'BANKCALL', line=1457)
W('15,2441', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=1458)
W('15,2442', 0o16001, '', 'TCF', 'GOTOPOOH', 'V34 -- TERMINATE', line=1459)
# Page 960
W('15,2443', 0o12445, '', 'TCF', 'R59E', 'V33 -- PROCEED TO MARK ROUTINE', line=1461)
W('15,2444', 0o12245, '', 'TCF', 'R59', 'V32 -- RECYCLE TO TOP OF R59 AGAIN', line=1462)

W('15,2445', 0o34757, 'R59E', 'CAF', 'SEVEN', 'GET DETENT CODE CORRESPONDING TO POSCODE', line=1464)
W('15,2446', 0o71242, '', 'MASK', 'POSCODE', line=1465)
W('15,2447', 0o00006, '', 'EXTEND', line=1466)
W('15,2450', 0o74745, '', 'MP', 'BIT7', 'DETEND CODE NOW IN L', line=1467)
W('15,2451', 0o47744, '', 'CS', 'HIGH9', line=1468)
W('15,2452', 0o70735, '', 'MASK', 'AOTCODE', 'ISOLATE STAR NO BIT 1-6', line=1469)
W('15,2453', 0o60001, '', 'AD', 'L', line=1470)
W('15,2454', 0o54735, '', 'TS', 'AOTCODE', 'STORE DETENT 7-9', line=1471)

W('15,2455', 0o04616, 'R59OUT', 'TC', 'BANKCALL', 'GO TO AOTMARK FOR SIGHTING', line=1473)
W('15,2456', 0o16000, '', 'CADR', 'AOTMARK', kind='data', line=1474)
W('15,2457', 0o04616, '', 'TC', 'BANKCALL', line=1475)
W('15,2460', 0o17712, '', 'CADR', 'AOTSTALL', 'SLEEP TILL SIGHTING DONE', kind='data', line=1476)
W('15,2461', 0o05711, '', 'TC', 'CURTAINS', 'BADEND RETURN FROM AOTMARK', line=1477)
W('15,2462', 0o13054, '', 'TCF', 'R59RET', 'RETURN TO 1 STAR OR 2STAR', line=1478)

W('15,2463', 0o00306, 'V01N70*', 'VN', '170', kind='data', line=1480)
W('15,2464', 0o01517, 'V06N79', 'VN', '679', kind='data', line=1481)
W('15,2465', 0o02525, 'DEG30', '2DEC', '.083333333', '30 DEGREES', kind='data', line=1482)
W('15,2466', 0o12525, kind='data', line=1482)
W('15,2467', 0o00026, 'DEG.5', '2DEC', '.00138888', '.5 DEGREES SCALED IN REVS.', kind='data', line=1483)
W('15,2470', 0o30131, kind='data', line=1483)
W('15,2471', 0o12525, 'DEG60', 'OCT', '12525', '60 DEG CDU SCALING', kind='data', line=1484)
S('CURSOR', 'equals', 0o1236, line=1485)
S('SPIRAL', 'equals', 0o1240, line=1486)
S('POSCODE', 'equals', 0o1242, line=1487)

# Page 961
# NAME --       PLANET
# FUNCTION --   TO PROVIDE THE REFERENCE VECTOR FOR THE SIGHTED CELESTIAL
# BODY.  STARS ARE FETCHED FROM THE CATALOG, SUN, EARTH AND
# MOON ARE COMPUTED BY LOCSAM, PLANET VECTORS ARE ENTERED
# BY DSKY INPUT.
# CALL --       CALL
# PLANET
# INPUT --      TIME IN MPAC
# OUTPUT --     VECTOR IN MPAC
# SUBROUTINES -- LOCSAM
# DEBRIS --     VAC, STARAD - STARAD +17

#   SETLOC P50S
#   BANK
#   COUNT* $$/P51

W('15,2472', 0o27562, 'PLANET', 'STOVL', 'TSIGHT', kind='interp', line=1506)
W('15,2473', 0o24007, '', '', 'ZEROVEC', kind='operand', line=1507)
W('15,2474', 0o02707, '', 'STORE', 'STARAD', kind='interp', line=1508)
W('15,2475', 0o77420, '', 'STQ', 'EXIT', kind='interp', line=1509)
W('15,2476', 0o02736, '', '', 'GCTR', kind='operand', line=1510)
W('15,2477', 0o47744, '', 'CS', 'HIGH9', line=1511)
W('15,2500', 0o70735, '', 'MASK', 'AOTCODE', line=1512)
W('15,2501', 0o00006, '', 'EXTEND', line=1513)
W('15,2502', 0o76242, '', 'MP', 'REVCNT', line=1514)
W('15,2503', 0o56001, '', 'XCH', 'L', line=1515)
W('15,2504', 0o51757, '', 'INDEX', 'STARIND', line=1516)
W('15,2505', 0o55755, '', 'TS', 'BESTI', line=1517)
W('15,2506', 0o10000, '', 'CCS', 'A', line=1518)
W('15,2507', 0o12523, '', 'TCF', 'NOTPLAN', line=1519)
W('15,2510', 0o32562, '', 'CAF', 'VNPLANV', line=1520)
W('15,2511', 0o04616, '', 'TC', 'BANKCALL', line=1521)
W('15,2512', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=1522)
W('15,2513', 0o02510, '', 'TC', '-3', line=1523)
W('15,2514', 0o02516, '', 'TC', '+2', line=1524)
W('15,2515', 0o02510, '', 'TC', '-5', line=1525)
W('15,2516', 0o06037, '', 'TC', 'INTPRET', line=1526)
W('15,2517', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=1527)
W('15,2520', 0o02707, '', '', 'STARAD', kind='operand', line=1528)
W('15,2521', 0o77650, '', 'GOTO', kind='interp', line=1529)
W('15,2522', 0o02736, '', '', 'GCTR', kind='operand', line=1530)
W('15,2523', 0o40000, 'NOTPLAN', 'CS', 'A', line=1531)
W('15,2524', 0o62561, '', 'AD', 'DEC227', line=1532)
W('15,2525', 0o00006, '', 'EXTEND', line=1533)
W('15,2526', 0o62537, '', 'BZMF', 'CALSAM1', line=1534)
W('15,2527', 0o51757, '', 'INDEX', 'STARIND', line=1535)
W('15,2530', 0o31755, '', 'CA', 'BESTI', line=1536)
W('15,2531', 0o50120, '', 'INDEX', 'FIXLOC', line=1537)
W('15,2532', 0o54046, '', 'TS', 'X1', line=1538)
W('15,2533', 0o06037, '', 'TC', 'INTPRET', line=1539)
# Page 962
W('15,2534', 0o52173, '', 'VLOAD*', 'GOTO', kind='interp', line=1541)
W('15,2535', 0o30347, '', '', 'CATLOG,1', kind='operand', line=1542)
W('15,2536', 0o02736, '', '', 'GCTR', kind='operand', line=1543)
W('15,2537', 0o06037, 'CALSAM1', 'TC', 'INTPRET', line=1544)
W('15,2540', 0o45145, 'CALSAM', 'DLOAD', 'CALL', kind='interp', line=1545)
W('15,2541', 0o03562, '', '', 'TSIGHT', kind='operand', line=1546)
W('15,2542', 0o30506, '', '', 'LOCSAM', kind='operand', line=1547)
W('15,2543', 0o77340, '', 'LXC,1', 'VLOAD', kind='interp', line=1548)
W('15,2544', 0o02757, '', '', 'STARIND', kind='operand', line=1549)
W('15,2545', 0o02707, '', '', 'VEARTH', kind='operand', line=1550)
W('15,2546', 0o24001, '', 'STOVL', '0D', kind='interp', line=1551)
W('15,2547', 0o02715, '', '', 'VSUN', kind='operand', line=1552)
W('15,2550', 0o26707, '', 'STOVL', 'VEARTH', kind='interp', line=1553)
W('15,2551', 0o00001, '', '', '0D', kind='operand', line=1554)
W('15,2552', 0o02715, '', 'STORE', 'VSUN', kind='interp', line=1555)
W('15,2553', 0o70143, '', 'DLOAD*', 'LXC,1', kind='interp', line=1556)
W('15,2554', 0o02756, '', '', 'BESTI,1', kind='operand', line=1557)
W('15,2555', 0o00154, '', '', 'MPAC', kind='operand', line=1558)
W('15,2556', 0o52173, '', 'VLOAD*', 'GOTO', kind='interp', line=1559)
W('15,2557', 0o02343, '', '', 'STARAD -228D,1', kind='operand', line=1560)
W('15,2560', 0o02736, '', '', 'GCTR', kind='operand', line=1561)
W('15,2561', 0o00343, 'DEC227', 'DEC', '227', kind='data', line=1562)
W('15,2562', 0o01530, 'VNPLANV', 'VN', '0688', kind='data', line=1563)
S('PIPSRINE', 'equals', 0o107544, line=1564)  # EBANK NOT 4 SO DON'T LOAD PIPTIME1

# Page 963
# GRAVITY VECTOR DETERMINATION ROUTINE
# BY KEN VINCENT
#
# FOR DETAILED DESCRIPTION SEE 504GSOP 5.6.3.2.5.
#
# THIS PROGRAM FINDS THE DIRECTION OF THE MOON'S GRAVITY
# WHILE THE LM IS IN THE MOON'S SURFACE.  IT WILL BE USED
# FOR LUNAR SURFACE ALIGNMENT.  THE GRAVITY VECTOR IS
# DETERMINED BY READING THE PIPAS WITH THE IMU AT TWO
# PARTICULAR ORIENTATIONS.  THE TWO READINGS ARE AVERAGED
# AND UNITIZED AND TRANSFORMED TO NB COORDINATES.  THE TWO
# ORIENTATIONS WERE CHOSEN TO REDUCE BIAS ERRORS IN THE
# READINGS.
#
# CALL --
# TC      BANKCALL
# CADR    GVDETER
#
# INPUTS --
# PIPAS, CDUS
#
# OUTPUTS --
# STARSAV1 = UNIT GRAVITY
# GSAV     = DITTO
# GRAVBIT  = 1
#
# SUBROUTINES --
# PIPASR, IMUCOARS, IMUFINE, IMUSTALL, 1/PIPA, DELAYJOB, CDUTRIG,
# *NBSM*, *SNMB*, CALCGA, GOFLASH
#
# DEBRIS --
# VAC, SAC, STARAD, XSM, XNB, THETAD, DELV, COSCDU, SINCDU

W('15,2563', 0o32772, 'GVDETER', 'CAF', '42DEG', line=1600)
W('15,2564', 0o54321, '', 'TS', 'THETAD', line=1601)
W('15,2565', 0o40000, '', 'COM', line=1602)
W('15,2566', 0o54322, '', 'TS', 'THETAD +1', line=1603)
W('15,2567', 0o32773, '', 'CAF', '35DEG', line=1604)
W('15,2570', 0o54323, '', 'TS', 'THETAD +2', line=1605)
W('15,2571', 0o06037, '', 'TC', 'INTPRET', line=1606)
W('15,2572', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=1607)
W('15,2573', 0o01662, '', '', 'REFSMFLG', kind='operand', line=1608)
W('15,2574', 0o32670, '', '', 'LUNG', kind='operand', line=1609)

# FIND GIMBAL ANGLES WHICH ROTATE SM 180 DEG ABOUT G VEC
#
# DEFINE G COOR SYS
# _
# [ X ]   [    UNIT G    ]
# *   [ _ ]   [            _ ]
# M = [ Y ] = [ UNITEZSM * X ]
# [ _ ]   [       _   _  ]
# [ Z ]   [ UNIT( X * Y )]
#
# THEN ROTATED SM WRT PRESENT IS
#
# Page 964
# [ 1   0   0 ]
# *      *T [           ] *             *      *
# XSM =   M  [ 0  -1   0 ] M  =  2 (X X ) - 1/2 I
# [           ]           I J
# [ 0   0  -1 ]
#
# ALSO NB WRT PRES SM IS
#
# *      *  *
# XNB = NBSM I
#
# *    *
# GIMBAL ANGLES = CALCGA( XSM, XNB )

#   SETLOC P50S
#   BANK
#   COUNT* $$/P57
W('15,2575', 0o66370, '', 'AXT,1', 'SSP', 'X1=18', kind='interp', line=1641)
W('15,2576', 0o00022, '', '', '18D', 'S1=6', kind='operand', line=1642)
W('15,2577', 0o00051, '', '', 'S1', 'X2, -2', kind='operand', line=1643)
W('15,2600', 0o00006, '', '', '6D', kind='operand', line=1644)
W('15,2601', 0o77744, '', 'LXC,2', kind='interp', line=1645)
W('15,2602', 0o00050, '', '', 'S1', kind='operand', line=1646)
W('15,2603', 0o45173, 'GRAVEL', 'VLOAD*', 'CALL', kind='interp', line=1647)
W('15,2604', 0o54000, '', '', 'XUNIT -6,2', kind='operand', line=1648)
W('15,2605', 0o47673, '', '', '*NBSM*', 'SIN AND COS COMPUTED IN LUNG', kind='operand', line=1649)
W('15,2606', 0o06707, '', 'STORE', 'XNB +18D,1', kind='interp', line=1650)
W('15,2607', 0o77775, '', 'VLOAD', kind='interp', line=1651)
W('15,2610', 0o02731, '', '', 'STAR', kind='operand', line=1652)
W('15,2611', 0o73744, '', 'LXC,2', 'VXSC*', 'COMPLEMENT -- UNITX ARE BACKWARD --', kind='interp', line=1653)
W('15,2612', 0o00047, '', '', 'X2', kind='operand', line=1654)
W('15,2613', 0o75040, '', '', 'STAR +6,2', 'OUTER PRODUCT', kind='operand', line=1655)
W('15,2614', 0o71152, '', 'VSL2', 'LXC,2', kind='interp', line=1656)
W('15,2615', 0o00047, '', '', 'X2', kind='operand', line=1657)
W('15,2616', 0o63047, '', 'VSU*', 'INCR,2', kind='interp', line=1658)
W('15,2617', 0o54000, '', '', 'XUNIT -6,2', kind='operand', line=1659)
W('15,2620', 0o00002, '', '', '2D', kind='operand', line=1660)
W('15,2621', 0o06665, '', 'STORE', 'XSM +18D,1', kind='interp', line=1661)
W('15,2622', 0o45100, '', 'TIX,1', 'CALL', kind='interp', line=1662)
W('15,2623', 0o32603, '', '', 'GRAVEL', kind='operand', line=1663)
W('15,2624', 0o47353, '', '', 'CALCGA', kind='operand', line=1664)
W('15,2625', 0o74575, '', 'VLOAD', 'VSR1', kind='interp', line=1665)
W('15,2626', 0o02715, '', '', 'GOUT', kind='operand', line=1666)
W('15,2627', 0o36723, '', 'STCALL', 'STARAD +12D', kind='interp', line=1667)
W('15,2630', 0o32670, '', '', 'LUNG', kind='operand', line=1668)
W('15,2631', 0o74575, '', 'VLOAD', 'VSR1', kind='interp', line=1669)
W('15,2632', 0o02715, '', '', 'GOUT', kind='operand', line=1670)
W('15,2633', 0o53455, '', 'VAD', 'UNIT', kind='interp', line=1671)
W('15,2634', 0o02723, '', '', 'STARAD +12D', kind='operand', line=1672)
W('15,2635', 0o02761, '', 'STORE', 'STARSAV1', kind='interp', line=1673)
W('15,2636', 0o77641, '', 'DOT', kind='interp', line=1674)
W('15,2637', 0o02231, '', '', 'GSAV', kind='operand', line=1675)
W('15,2640', 0o65552, '', 'SL1', 'ACOS', kind='interp', line=1676)
# Page 965
W('15,2641', 0o01046, '', 'STORE', 'DSPTEM1', kind='interp', line=1678)
W('15,2642', 0o77776, '', 'EXIT', kind='interp', line=1679)
W('15,2643', 0o05516, '', 'TC', 'DOWNFLAG', 'CLAR FREEFLAG IN CASE OF RECYCLE', line=1680)
W('15,2644', 0o00014, '', 'ADRES', 'FREEFLAG', kind='data', line=1681)

W('15,2645', 0o32771, '', 'CA', 'DISGRVER', line=1683)
W('15,2646', 0o04616, '', 'TC', 'BANKCALL', line=1684)
W('15,2647', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=1685)
W('15,2650', 0o06001, '', 'TC', 'GOTOPOOH', line=1686)
W('15,2651', 0o12654, '', 'TCF', 'PROGRAV', 'VB33 -- PROCEED', line=1687)
W('15,2652', 0o05504, '', 'TC', 'UPFLAG', 'VB32 -- RECYCLE -- STORE GRAV AND DO IT AGAIN', line=1688)
W('15,2653', 0o00014, '', 'ADRES', 'FREEFLAG', 'AND SET FREEFLAG TO SHOW RECYCLE', kind='data', line=1689)

W('15,2654', 0o05353, 'PROGRAV', 'TC', 'PHASCHNG', line=1691)
W('15,2655', 0o04024, '', 'OCT', '04024', kind='data', line=1692)

W('15,2656', 0o06037, '', 'TC', 'INTPRET', line=1694)
W('15,2657', 0o77775, '', 'VLOAD', kind='interp', line=1695)
W('15,2660', 0o02761, '', '', 'STARSAV1', kind='operand', line=1696)
W('15,2661', 0o02231, '', 'STORE', 'GSAV', kind='interp', line=1697)
W('15,2662', 0o77776, '', 'EXIT', kind='interp', line=1698)
W('15,2663', 0o34751, '', 'CAF', 'FREEFBIT', 'IF FREEFLAG SET, RE-COMPUTE GRAVITY', line=1699)
W('15,2664', 0o70074, '', 'MASK', 'FLAGWRD0', line=1700)
W('15,2665', 0o10000, '', 'CCS', 'A', line=1701)
W('15,2666', 0o12563, '', 'TCF', 'GVDETER', 'SET', line=1702)
W('15,2667', 0o13553, '', 'TCF', 'ATTCHK', 'EXIT FROM GVDETER', line=1703)

W('15,2670', 0o77220, 'LUNG', 'STQ', 'VLOAD', kind='interp', line=1705)
W('15,2671', 0o02745, '', '', 'QMIN', kind='operand', line=1706)
W('15,2672', 0o24007, '', '', 'ZEROVEC', kind='operand', line=1707)
W('15,2673', 0o02707, '', 'STORE', 'GACC', kind='interp', line=1708)
W('15,2674', 0o77776, '', 'EXIT', kind='interp', line=1709)
W('15,2675', 0o05353, '', 'TC', 'PHASCHNG', line=1710)
W('15,2676', 0o04024, '', 'OCT', '04024', kind='data', line=1711)

W('15,2677', 0o04616, '', 'TC', 'BANKCALL', line=1713)
W('15,2700', 0o17000, '', 'CADR', 'IMUCOARS', kind='data', line=1714)
W('15,2701', 0o04616, '', 'TC', 'BANKCALL', line=1715)
W('15,2702', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=1716)
W('15,2703', 0o05711, '', 'TC', 'CURTAINS', line=1717)
W('15,2704', 0o04616, '', 'TC', 'BANKCALL', line=1718)
W('15,2705', 0o17210, '', 'CADR', 'IMUFINE', kind='data', line=1719)
W('15,2706', 0o04616, '', 'TC', 'BANKCALL', line=1720)
W('15,2707', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=1721)
W('15,2710', 0o05711, '', 'TC', 'CURTAINS', line=1722)
W('15,2711', 0o32770, '', 'CA', 'T/2SEC', line=1723)
W('15,2712', 0o55736, '', 'TS', 'GCTR', line=1724)
W('15,2713', 0o37716, '', 'CA', 'PRIO31', line=1725)
W('15,2714', 0o55075, '', 'TS', '1/PIPADT', line=1726)
W('15,2715', 0o04616, '', 'TC', 'BANKCALL', line=1727)
# Page 966
W('15,2716', 0o15701, '', 'CADR', 'GCOMPZER', 'INITIALIZE COMPENSATION', kind='data', line=1729)
W('15,2717', 0o05353, '', 'TC', 'PHASCHNG', line=1730)
W('15,2720', 0o04024, '', 'OCT', '04024', kind='data', line=1731)

W('15,2721', 0o04616, '', 'TC', 'BANKCALL', "DON'T NEED TO INHINT.  THIS USED TO", line=1733)
W('15,2722', 0o77544, '', 'CADR', 'PIPSRINE', "INITIALIZE PIPAS.  DON'T USE DATA", kind='data', line=1734)
W('15,2723', 0o06037, '', 'TC', 'INTPRET', line=1735)
W('15,2724', 0o77776, 'GREED', 'EXIT', '', "= MASK 7776 IN BASIC SO DON'T CARE", kind='interp', line=1736)
W('15,2725', 0o35000, '', 'CAF', '2SECS', line=1737)
W('15,2726', 0o05173, '', 'TC', 'TWIDDLE', 'SET UP 2 SEC TASK TO READ PIPAS', line=1738)
W('15,2727', 0o02731, '', 'ADRES', 'GRABGRAV', kind='data', line=1739)

W('15,2730', 0o05155, '', 'TC', 'ENDOFJOB', line=1741)

W('15,2731', 0o04674, 'GRABGRAV', 'TC', 'IBNKCALL', line=1743)
W('15,2732', 0o77544, '', 'CADR', 'PIPSRINE', kind='data', line=1744)
W('15,2733', 0o35023, '', 'CAF', 'PRIO13', 'RE-ESTABLISH MAINLINE JOB', line=1745)
W('15,2734', 0o05105, '', 'TC', 'FINDVAC', line=1746)
#   EBANK= STARAD
W('15,2735', 0o02740, '', '2CADR', 'ADDGRAV', kind='data', line=1748)
W('15,2736', 0o32065, kind='data', line=1748)

W('15,2737', 0o05261, '', 'TC', 'TASKOVER', line=1750)

W('15,2740', 0o04616, 'ADDGRAV', 'TC', 'BANKCALL', line=1752)
W('15,2741', 0o15263, '', 'CADR', '1/PIPA', kind='data', line=1753)
W('15,2742', 0o25736, '', 'INCR', 'GCTR', line=1754)
W('15,2743', 0o06037, '', 'TC', 'INTPRET', line=1755)
W('15,2744', 0o53375, '', 'VLOAD', 'VAD', kind='interp', line=1756)
W('15,2745', 0o00325, '', '', 'DELV', kind='operand', line=1757)
W('15,2746', 0o02707, '', '', 'GACC', kind='operand', line=1758)
W('15,2747', 0o02707, '', 'STORE', 'GACC', 'ACCUMULATE G VECTOR', kind='interp', line=1759)
W('15,2750', 0o50135, '', 'SLOAD', 'BMN', kind='interp', line=1760)
W('15,2751', 0o02737, '', '', 'GCTR', kind='operand', line=1761)
W('15,2752', 0o32724, '', '', 'GREED', kind='operand', line=1762)
W('15,2753', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=1763)
W('15,2754', 0o02707, '', '', 'GACC', kind='operand', line=1764)
W('15,2755', 0o36731, '', 'STCALL', 'STAR', kind='interp', line=1765)
W('15,2756', 0o47537, '', '', 'CDUTRIG', 'TRANSFORM IN NB COOR AND STORE', kind='operand', line=1766)
W('15,2757', 0o77624, '', 'CALL', '', '      IN OUTPUT', kind='interp', line=1767)
W('15,2760', 0o47671, '', '', '*SMNB*', kind='operand', line=1768)
W('15,2761', 0o02715, '', 'STORE', 'GOUT', kind='interp', line=1769)
W('15,2762', 0o77776, '', 'EXIT', kind='interp', line=1770)
W('15,2763', 0o05353, '', 'TC', 'PHASCHNG', line=1771)
W('15,2764', 0o04024, '', 'OCT', '04024', kind='data', line=1772)

W('15,2765', 0o06037, 'QMINEXIT', 'TC', 'INTPRET', line=1774)
W('15,2766', 0o77650, '', 'GOTO', kind='interp', line=1775)
W('15,2767', 0o02745, '', '', 'QMIN', kind='operand', line=1776)
W('15,2770', 0o77753, 'T/2SEC', 'DEC', '-20', kind='data', line=1777)
# Page 967
W('15,2771', 0o01404, 'DISGRVER', 'VN', '0604', kind='data', line=1779)
W('15,2772', 0o07357, '42DEG', 'OCT', '07357', kind='data', line=1780)
W('15,2773', 0o06211, '35DEG', 'OCT', '06211', kind='data', line=1781)

# Page 968
# NAME -- GYROTRIM
#
# THIS PROGRAM COMPUTES AND SENDS GYRO COMMANDS WHICH CAUSE THE CDUS
# TO ATTAIN A PRESCRIBED SET OF ANGLES.  THIS ROUTINE ASSUMES THE
# VEHICLES ATTITUDE REMAINS STATIONARY DURING ITS OPERATION.
#
# CALL          CALL
# GYROTRIM
#
# INPUT         THETAD,+1,+2 = DESIRED CDU ANGLES
# CDUX,CDUY,CDUZ
#
# OUTPUT        GYRO TORQUE PULSES
#
# SUBROUTINES   TRG*NBSM, *NBSM*, CDUTRIG, AXISGEN, CALCGTA, IMUFINE
# IMPULSE, IMUSTALL
# _______  ______  ______     *          *   ___
# DEBRIS        CDUSPOT, SINCDU, COSCDU, STARAD, VAC, XDC, OGC

#   COUNT* $$/P57
W('15,2774', 0o71220, 'GYROTRIM', 'STQ', 'DLOAD', kind='interp', line=1804)
W('15,2775', 0o02745, '', '', 'QMIN', kind='operand', line=1805)
W('15,2776', 0o00322, '', '', 'THETAD', kind='operand', line=1806)
W('15,2777', 0o65325, '', 'PDDL', 'PDDL', kind='interp', line=1807)
W('15,3000', 0o00324, '', '', 'THETAD +2', kind='operand', line=1808)
W('15,3001', 0o00323, '', '', 'THETAD +1', kind='operand', line=1809)
W('15,3002', 0o77666, '', 'VDEF', kind='interp', line=1810)
W('15,3003', 0o24767, '', 'STOVL', 'CDUSPOT', kind='interp', line=1811)
W('15,3004', 0o24005, '', '', 'XUNIT', kind='operand', line=1812)
W('15,3005', 0o77624, '', 'CALL', kind='interp', line=1813)
W('15,3006', 0o47664, '', '', 'TRG*NBSM', kind='operand', line=1814)
W('15,3007', 0o26707, '', 'STOVL', 'STARAD', kind='interp', line=1815)
W('15,3010', 0o24003, '', '', 'YUNIT', kind='operand', line=1816)
W('15,3011', 0o77624, '', 'CALL', kind='interp', line=1817)
W('15,3012', 0o47673, '', '', '*NBSM*', kind='operand', line=1818)
W('15,3013', 0o36715, '', 'STCALL', 'STARAD +6', kind='interp', line=1819)
W('15,3014', 0o47537, '', '', 'CDUTRIG', kind='operand', line=1820)
W('15,3015', 0o77624, '', 'CALL', kind='interp', line=1821)
W('15,3016', 0o20030, '', '', 'CALCSMSC', kind='operand', line=1822)
W('15,3017', 0o77775, '', 'VLOAD', kind='interp', line=1823)
W('15,3020', 0o02665, '', '', 'XNB', kind='operand', line=1824)
W('15,3021', 0o24007, '', 'STOVL', '6D', kind='interp', line=1825)
W('15,3022', 0o02673, '', '', 'YNB', kind='operand', line=1826)
W('15,3023', 0o34015, '', 'STCALL', '12D', kind='interp', line=1827)
W('15,3024', 0o47441, '', '', 'AXISGEN', kind='operand', line=1828)
W('15,3025', 0o77624, '', 'CALL', kind='interp', line=1829)
W('15,3026', 0o47247, '', '', 'CALCGTA', kind='operand', line=1830)
W('15,3027', 0o77776, 'JUSTTRIM', 'EXIT', kind='interp', line=1831)
W('15,3030', 0o04616, '', 'TC', 'BANKCALL', line=1832)
W('15,3031', 0o17210, '', 'CADR', 'IMUFINE', kind='data', line=1833)
W('15,3032', 0o04616, '', 'TC', 'BANKCALL', line=1834)
# Page 969
W('15,3033', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=1836)
W('15,3034', 0o05711, '', 'TC', 'CURTAINS', line=1837)
W('15,3035', 0o33044, '', 'CA', 'GYRCDR', line=1838)
W('15,3036', 0o04616, '', 'TC', 'BANKCALL', line=1839)
W('15,3037', 0o17323, '', 'CADR', 'IMUPULSE', kind='data', line=1840)
W('15,3040', 0o04616, '', 'TC', 'BANKCALL', line=1841)
W('15,3041', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=1842)
W('15,3042', 0o05711, '', 'TC', 'CURTAINS', line=1843)
W('15,3043', 0o12765, '', 'TCF', 'QMINEXIT', line=1844)

W('15,3044', 0o02737, 'GYRCDR', 'ECADR', 'OGC', kind='data', line=1846)

# Page 970
# PERFORM STAR ACQUISITION AND STAR SIGHTINGS

W('15,3045', 0o34755, '2STARS', 'CAF', 'ZERO', 'INITIALIZE STARIND', line=1851)
W('15,3046', 0o13050, '', 'TCF', '+2', 'ZERO FOR 1ST STAR, ONE FOR 2ND STAR', line=1852)
W('15,3047', 0o34753, '1STAR', 'CAF', 'BIT1', line=1853)
W('15,3050', 0o55757, '', 'TS', 'STARIND', line=1854)

W('15,3051', 0o05353, '', 'TC', 'PHASCHNG', line=1856)
W('15,3052', 0o04024, '', 'OCT', '04024', kind='data', line=1857)

W('15,3053', 0o12245, '', 'TCF', 'R59', 'GO DO STAR ACQUIRE AND AOTMARK', line=1859)

W('15,3054', 0o31757, 'R59RET', 'CA', 'STARIND', 'BACK FROM SURFACE MARKING', line=1861)
W('15,3055', 0o00006, '', 'EXTEND', line=1862)
W('15,3056', 0o13067, '', 'BZF', 'ASTAR', '1ST STAR MARKED', line=1863)

W('15,3057', 0o05353, '', 'TC', 'PHASCHNG', line=1865)
W('15,3060', 0o04024, '', 'OCT', '04024', kind='data', line=1866)

W('15,3061', 0o06037, '', 'TC', 'INTPRET', line=1868)
W('15,3062', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=1869)
W('15,3063', 0o03562, '', '', 'TSIGHT', 'TIME OF 2ND MARK', kind='operand', line=1870)
W('15,3064', 0o32472, '', '', 'PLANET', kind='operand', line=1871)
W('15,3065', 0o36731, '', 'STCALL', 'VEC2', 'STORE 2ND CATALOG VEC (REF)', kind='interp', line=1872)
W('15,3066', 0o33101, '', '', 'SURFLINE', kind='operand', line=1873)

W('15,3067', 0o06037, 'ASTAR', 'TC', 'INTPRET', line=1875)
W('15,3070', 0o77775, '', 'VLOAD', kind='interp', line=1876)
W('15,3071', 0o02715, '', '', 'STARAD +6', kind='operand', line=1877)
W('15,3072', 0o02761, '', 'STORE', 'STARSAV1', '1ST OBSERVED STAR (SM)', kind='interp', line=1878)
W('15,3073', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=1879)
W('15,3074', 0o03562, '', '', 'TSIGHT', 'TIME OF 1ST MARK', kind='operand', line=1880)
W('15,3075', 0o32472, '', '', 'PLANET', kind='operand', line=1881)
W('15,3076', 0o02723, '', 'STORE', 'VEC1', 'STORE 1ST CATALOG VEC (REF)', kind='interp', line=1882)
W('15,3077', 0o77776, '', 'EXIT', kind='interp', line=1883)
W('15,3100', 0o13047, '', 'TCF', '1STAR', 'GO GET 2ND STAR SIGHTING', line=1884)

# Page 971
# DO FINE OR COARSE ALIGNMENT OF IMU

W('15,3101', 0o77131, 'SURFLINE', 'SSP', 'AXT,2', kind='interp', line=1889)
W('15,3102', 0o00052, '', '', 'S2', kind='operand', line=1890)
W('15,3103', 0o00006, '', '', '6', kind='operand', line=1891)
W('15,3104', 0o00014, '', '', '12D', kind='operand', line=1892)
W('15,3105', 0o64373, 'WRTDESIR', 'VLOAD*', 'MXV', kind='interp', line=1893)
W('15,3106', 0o75040, '', '', 'VEC1 +12D,2', 'PICK UP VEC IN REF, TRANS TO DESIRED SH', kind='operand', line=1894)
W('15,3107', 0o03607, '', '', 'XSMD', kind='operand', line=1895)
W('15,3110', 0o77656, '', 'UNIT', kind='interp', line=1896)
W('15,3111', 0o12723, '', 'STORE', 'STARAD +12D,2', 'VEC IN SM', kind='interp', line=1897)
W('15,3112', 0o77773, '', 'VLOAD*', kind='interp', line=1898)
W('15,3113', 0o75002, '', '', 'STARSAV1 +12D,2', 'PICK UP VEC IN PRESENT SM', kind='operand', line=1899)
W('15,3114', 0o10023, '', 'STORE', '18D,2', kind='interp', line=1900)
W('15,3115', 0o43104, '', 'TIX,2', 'BON', kind='interp', line=1901)
W('15,3116', 0o33105, '', '', 'WRTDESIR', kind='operand', line=1902)
W('15,3117', 0o04315, '', '', 'INITALGN', 'IF INITIAL PASS (OPTION 0) BYPASS R54', kind='operand', line=1903)
W('15,3120', 0o33126, '', '', 'INITBY', kind='operand', line=1904)
W('15,3121', 0o77624, 'DOALIGN', 'CALL', kind='interp', line=1905)
W('15,3122', 0o31256, '', '', 'R54', 'DO CHKSDATA', kind='operand', line=1906)
W('15,3123', 0o77614, '', 'BOFF', kind='interp', line=1907)
W('15,3124', 0o00354, '', '', 'FREEFLAG', kind='operand', line=1908)
W('15,3125', 0o33206, '', '', 'P57POST', 'ASTRO DOES NOT LIKE DATA TEST RESULTS', kind='operand', line=1909)
W('15,3126', 0o77624, 'INITBY', 'CALL', kind='interp', line=1910)
W('15,3127', 0o47441, '', '', 'AXISGEN', 'GET DESIRED ORIENT WRT PRES. XDC,YDC,ZDC', kind='operand', line=1911)
W('15,3130', 0o77624, '', 'CALL', kind='interp', line=1912)
W('15,3131', 0o47247, '', '', 'CALCGTA', 'GET GYRO TORQ ANGLES, OGC,IGC,MGC', kind='operand', line=1913)
W('15,3132', 0o77776, '', 'EXIT', kind='interp', line=1914)
W('15,3133', 0o34752, '', 'CAF', 'INITABIT', 'IF INITIAL PASS BYPASS NOUN 93 DISPLAY', line=1915)
W('15,3134', 0o70104, '', 'MASK', 'FLAGWRD8', line=1916)
W('15,3135', 0o10000, '', 'CCS', 'A', line=1917)
W('15,3136', 0o13145, '', 'TCF', '5DEGTEST', line=1918)
W('15,3137', 0o33313, '', 'CAF', 'DISPGYRO', 'DISPLAY GYRO TORQ ANGLES V 06N93', line=1919)
W('15,3140', 0o04616, '', 'TC', 'BANKCALL', line=1920)
W('15,3141', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=1921)
W('15,3142', 0o06001, '', 'TC', 'GOTOPOOH', 'V34 -- TERMINATE', line=1922)
W('15,3143', 0o13145, '', 'TCF', '5DEGTEST', 'VB33 -- PROCEED TO COARSE OR FINE', line=1923)
W('15,3144', 0o13207, '', 'TCF', 'P57POST +1', 'VB32 -- RECYCLE, MAYBE RE-ALIGN', line=1924)

W('15,3145', 0o06037, '5DEGTEST', 'TC', 'INTPRET', 'IF ANGLES GREATER THAN 5 DEGS, DO COARSE', line=1926)
W('15,3146', 0o40175, '', 'VLOAD', 'BOV', kind='interp', line=1927)
W('15,3147', 0o02740, '', '', 'OGC', kind='operand', line=1928)
W('15,3150', 0o33151, '', '', 'SURFSUP', kind='operand', line=1929)
W('15,3151', 0o02750, 'SURFSUP', 'STORE', 'OGCT', kind='interp', line=1930)
W('15,3152', 0o40141, '', 'V/SC', 'BOV', kind='interp', line=1931)
W('15,3153', 0o30610, '', '', '5DEGREES', kind='operand', line=1932)
W('15,3154', 0o33254, '', '', 'COATRIM', kind='operand', line=1933)
W('15,3155', 0o52131, '', 'SSP', 'GOTO', kind='interp', line=1934)
W('15,3156', 0o02746, '', '', 'QMIN', kind='operand', line=1935)
W('15,3157', 0o33161, '', '', 'SURFDISP', kind='operand', line=1936)
# Page 972
W('15,3160', 0o33027, '', '', 'JUSTTRIM', 'ANGLES LESS THAN 5 DEG, DO GYRO TORQ', kind='operand', line=1938)

W('15,3161', 0o77776, 'SURFDISP', 'EXIT', kind='interp', line=1940)
W('15,3162', 0o05353, '', 'TC', 'PHASCHNG', line=1941)
W('15,3163', 0o04024, '', 'OCT', '04024', kind='data', line=1942)

W('15,3164', 0o06037, '', 'TC', 'INTPRET', line=1944)
W('15,3165', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=1945)
W('15,3166', 0o03606, '', '', 'XSMD', kind='operand', line=1946)
W('15,3167', 0o01733, '', '', 'REFSMMAT', kind='operand', line=1947)
W('15,3170', 0o45014, '', 'SET', 'CALL', kind='interp', line=1948)
W('15,3171', 0o01462, '', '', 'REFSMFLG', kind='operand', line=1949)
W('15,3172', 0o31377, '', '', 'MATMOVE', kind='operand', line=1950)
W('15,3173', 0o77776, '', 'EXIT', kind='interp', line=1951)
W('15,3174', 0o11145, '', 'CCS', 'OPTION2', 'IF OPTION ZERO DO FINISH', line=1952)
W('15,3175', 0o13177, '', 'TCF', 'B2F8', line=1953)
W('15,3176', 0o13207, '', 'TCF', 'P57POST +1', line=1954)

W('15,3177', 0o34752, 'B2F8', 'CAF', 'INITABIT', 'IF INITIAL FLAG SET, RE-CYCLE.', line=1956)
W('15,3200', 0o70104, '', 'MASK', 'FLAGWRD8', line=1957)
W('15,3201', 0o10000, '', 'CCS', 'A', line=1958)
W('15,3202', 0o13561, '', 'TCF', 'P57JUMP', "IT'S SET", line=1959)
W('15,3203', 0o06037, '', 'TC', 'INTPRET', line=1960)
W('15,3204', 0o77624, '', 'CALL', kind='interp', line=1961)
W('15,3205', 0o33506, '', '', 'REFMF', 'GO GET ATTITUDE VEC IN MF(YNBSAV,XNBSAV)', kind='operand', line=1962)
W('15,3206', 0o77776, 'P57POST', 'EXIT', kind='interp', line=1963)
W('15,3207', 0o35751, '', 'CAF', 'OCT14', 'DISPLAY V50N25 CHK CODE 14', line=1964)
W('15,3210', 0o04616, '', 'TC', 'BANKCALL', line=1965)
W('15,3211', 0o20623, '', 'CADR', 'GOPERF1', kind='data', line=1966)
W('15,3212', 0o16001, '', 'TCF', 'GOTOPOOH', 'VB34 -- TERMINATE', line=1967)
W('15,3213', 0o13561, '', 'TCF', 'P57JUMP', 'VB33 -- PROCEED TO RE-ALIGN', line=1968)
W('15,3214', 0o44752, '', 'CS', 'BIT2', 'TEST TO SEE IF ALIGNED BY OPTION 2', line=1969)
W('15,3215', 0o61145, '', 'AD', 'OPTION2', line=1970)
W('15,3216', 0o00006, '', 'EXTEND', line=1971)
W('15,3217', 0o13221, '', 'BZF', '+2', 'YES -- GO CALCULATE LANDING SITE', line=1972)
W('15,3220', 0o16001, '', 'TCF', 'GOTOPOOH', 'NO -- EXIT P57', line=1973)
W('15,3221', 0o05353, '', 'TC', 'PHASCHNG', 'RESTART PLACE', line=1974)
W('15,3222', 0o04024, '', 'OCT', '04024', kind='data', line=1975)
W('15,3223', 0o06037, '', 'TC', 'INTPRET', line=1976)
W('15,3224', 0o45175, '', 'VLOAD', 'CALL', 'USE GNB', kind='interp', line=1977)
W('15,3225', 0o02231, '', '', 'GSAV', kind='operand', line=1978)
W('15,3226', 0o47661, '', '', 'CDU*NBSM', 'GO TO SM COORDS', kind='operand', line=1979)
W('15,3227', 0o43105, '', 'VXM', 'SET', '      ON MOON SO SET LUNAFLAG', kind='interp', line=1980)
W('15,3230', 0o01734, '', '', 'REFSMMAT', '      G(REF) = (REFSMMAT)T (NBSM)GNB', kind='operand', line=1981)
W('15,3231', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=1982)
W('15,3232', 0o51515, '', 'PDVL', 'ABVAL', kind='interp', line=1983)
W('15,3233', 0o02023, '', '', 'RLS', kind='operand', line=1984)
W('15,3234', 0o45561, '', 'VXSC', 'STADR', kind='interp', line=1985)
W('15,3235', 0o75745, '', 'STORE', 'ALPHAV', 'ALPHAV = RLSMAG * G(REF)', kind='interp', line=1986)
W('15,3236', 0o47014, '', 'CLEAR', 'RTB', kind='interp', line=1987)
# Page 973
W('15,3237', 0o00662, '', '', 'ERADFLAG', kind='operand', line=1989)
W('15,3240', 0o21573, '', '', 'LOADTIME', kind='operand', line=1990)
W('15,3241', 0o77624, '', 'CALL', kind='interp', line=1991)
W('15,3242', 0o30446, '', '', 'N89DISP', 'SUBROUTINE TO CALC LS AND GIVE RLS BACK', kind='operand', line=1992)
W('15,3243', 0o01221, '', 'STORE', 'RN', 'RN=RLS B-29 = LM POSITION', kind='interp', line=1993)
W('15,3244', 0o65352, '', 'VSL2', 'PDDL', 'R-TO-RP GETS RLS B-27 AT 0-50 IN PDLIST', kind='interp', line=1994)
W('15,3245', 0o01243, '', '', 'GDT/2 +4', 'TIME TEMP STORED IN N89DISP', kind='operand', line=1995)
W('15,3246', 0o77606, '', 'PUSH', '', 'TIME AT 6-7 IN PDLIST', kind='interp', line=1996)
W('15,3247', 0o35235, '', 'STCALL', 'PIPTIME', 'PIPTIME = LM STATE TIME', kind='interp', line=1997)
W('15,3250', 0o51670, '', '', 'R-TO-RP', kind='operand', line=1998)
W('15,3251', 0o02023, '', 'STORE', 'RLS', 'RLS IN MOON-FIXED COORDS', kind='interp', line=1999)
W('15,3252', 0o77776, '', 'EXIT', kind='interp', line=2000)
W('15,3253', 0o16001, '', 'TCF', 'GOTOPOOH', 'EXIT P57', line=2001)

# Page 974
# COARSE AND FINE ALIGN IMU

W('15,3254', 0o75160, 'COATRIM', 'AXC,1', 'AXC,2', kind='interp', line=2006)
W('15,3255', 0o02664, '', '', 'XDC', kind='operand', line=2007)
W('15,3256', 0o02642, '', '', 'XSM', kind='operand', line=2008)
W('15,3257', 0o77624, '', 'CALL', kind='interp', line=2009)
W('15,3260', 0o31377, '', '', 'MATMOVE', kind='operand', line=2010)
W('15,3261', 0o77624, '', 'CALL', kind='interp', line=2011)
W('15,3262', 0o47537, '', '', 'CDUTRIG', kind='operand', line=2012)
W('15,3263', 0o77624, '', 'CALL', kind='interp', line=2013)
W('15,3264', 0o20030, '', '', 'CALCSMSC', kind='operand', line=2014)
W('15,3265', 0o77624, '', 'CALL', kind='interp', line=2015)
W('15,3266', 0o47353, '', '', 'CALCGA', kind='operand', line=2016)
W('15,3267', 0o77414, '', 'BOFF', 'EXIT', kind='interp', line=2017)
W('15,3270', 0o04355, '', '', 'INITALGN', 'IF INITIAL ALIGNMENT DISPLAY FINAL', kind='operand', line=2018)
W('15,3271', 0o33303, '', '', 'CORSIT', 'GIMBAL ANGLES IF COARSE ANGLES GREATER', kind='operand', line=2019)
W('15,3272', 0o35010, '', 'CAF', 'V06N22', 'THAN 5 DEGREES', line=2020)
W('15,3273', 0o04616, '', 'TC', 'BANKCALL', line=2021)
W('15,3274', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=2022)
W('15,3275', 0o06001, '', 'TC', 'GOTOPOOH', line=2023)
W('15,3276', 0o13300, '', 'TCF', '+2', line=2024)
W('15,3277', 0o13272, '', 'TCF', '-5', line=2025)
W('15,3300', 0o05353, '', 'TC', 'PHASCHNG', line=2026)
W('15,3301', 0o04024, '', 'OCT', '04024', kind='data', line=2027)

W('15,3302', 0o06037, '', 'TC', 'INTPRET', line=2029)
W('15,3303', 0o77624, 'CORSIT', 'CALL', kind='interp', line=2030)
W('15,3304', 0o31565, '', '', 'COARSE', kind='operand', line=2031)
W('15,3305', 0o77624, '', 'CALL', kind='interp', line=2032)
W('15,3306', 0o31602, '', '', 'NCOARSE', kind='operand', line=2033)
W('15,3307', 0o77624, '', 'CALL', kind='interp', line=2034)
W('15,3310', 0o32774, '', '', 'GYROTRIM', kind='operand', line=2035)
W('15,3311', 0o77650, '', 'GOTO', kind='interp', line=2036)
W('15,3312', 0o33161, '', '', 'SURFDISP', kind='operand', line=2037)
W('15,3313', 0o01535, 'DISPGYRO', 'VN', '0693', kind='data', line=2038)

# Page 975
# LUNAR SURFACE IMU ALIGNMENT PROGRAM

W('15,3314', 0o04616, 'P57', 'TC', 'BANKCALL', 'IS ISS ON -- IF NOT, IMUCHK WILL SEND', line=2043)
W('15,3315', 0o33652, '', 'CADR', 'IMUCHK', 'ALARM CODE 210 AND EXIT VIA GOTOPOOH', kind='data', line=2044)

W('15,3316', 0o36245, '', 'CAF', 'THREE', 'JAM REFSMMAT OPTION 3 FOR INITIAL DISP.', line=2046)
W('15,3317', 0o55145, '', 'TS', 'OPTION2', line=2047)
W('15,3320', 0o34753, 'P57OPT', 'CAF', 'BIT1', line=2048)
W('15,3321', 0o04616, '', 'TC', 'BANKCALL', line=2049)
W('15,3322', 0o20713, '', 'CADR', 'GOPERF4R', 'FLASH V04N06 FOR ALIGNMENT CODE', kind='data', line=2050)
W('15,3323', 0o06001, '', 'TC', 'GOTOPOOH', 'V34 TERMINATE', line=2051)
W('15,3324', 0o13331, '', 'TCF', 'ALIGNOPT', 'V33 PROCEED', line=2052)
W('15,3325', 0o13320, '', 'TCF', 'P57OPT', 'V32 RECYCLE', line=2053)

W('15,3326', 0o05353, '', 'TC', 'PHASCHNG', line=2055)
W('15,3327', 0o00014, '', 'OCT', '00014', kind='data', line=2056)
W('15,3330', 0o05155, '', 'TC', 'ENDOFJOB', line=2057)

W('15,3331', 0o31145, 'ALIGNOPT', 'CA', 'OPTION2', line=2059)
W('15,3332', 0o76245, '', 'MASK', 'THREE', line=2060)
W('15,3333', 0o50000, '', 'INDEX', 'A', line=2061)
W('15,3334', 0o13335, '', 'TCF', '+1', line=2062)
W('15,3335', 0o13350, '', 'TCF', 'TDISP', 'OPTION 4 LS ORIENTATION', line=2063)
W('15,3336', 0o13411, '', 'TCF', 'PACKOPTN', 'OPTION 1 PREFERRED', line=2064)
W('15,3337', 0o13320, '', 'TCF', 'P57OPT', 'OPTION 2 INVALID IN P57, RECYCLE', line=2065)
W('15,3340', 0o06037, '', 'TC', 'INTPRET', 'OPTION 3 REFSMMAT', line=2066)
W('15,3341', 0o75160, '', 'AXC,1', 'AXC,2', 'JAM REFSMMAT IN XSMD LOC', kind='interp', line=2067)
W('15,3342', 0o01733, '', '', 'REFSMMAT', kind='operand', line=2068)
W('15,3343', 0o03606, '', '', 'XSMD', kind='operand', line=2069)
W('15,3344', 0o77624, '', 'CALL', kind='interp', line=2070)
W('15,3345', 0o31377, '', '', 'MATMOVE', kind='operand', line=2071)
W('15,3346', 0o77650, '', 'GOTO', kind='interp', line=2072)
W('15,3347', 0o33410, '', '', 'PACKOPTN -1', kind='operand', line=2073)

W('15,3350', 0o06037, 'TDISP', 'TC', 'INTPRET', line=2075)
W('15,3351', 0o77745, '', 'DLOAD', kind='interp', line=2076)
W('15,3352', 0o03442, '', '', 'TIG', 'LOAD ASCENT TIME FOR DISPLAY', kind='operand', line=2077)
W('15,3353', 0o01046, 'P57A', 'STORE', 'DSPTEM1', kind='interp', line=2078)
W('15,3354', 0o77776, '', 'EXIT', kind='interp', line=2079)
W('15,3355', 0o32170, 'P57AA', 'CAF', 'V06N34*', 'DISPLAY TALIGN, TALIGN : DSPTEM1', line=2080)
W('15,3356', 0o04616, '', 'TC', 'BANKCALL', line=2081)
W('15,3357', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=2082)
W('15,3360', 0o16001, '', 'TCF', 'GOTOPOOH', 'V34 -- TERMINATE', line=2083)
W('15,3361', 0o13363, '', 'TCF', '+2', line=2084)
W('15,3362', 0o13355, '', 'TCF', 'P57AA', 'VB32 -- RECYCLE', line=2085)

W('15,3363', 0o06037, '', 'TC', 'INTPRET', line=2087)
W('15,3364', 0o65234, '', 'RTB', 'PDDL', kind='interp', line=2088)
W('15,3365', 0o21573, '', '', 'LOADTIME', 'PUSH CURRENT TIME AND PICK UP KEY IN', kind='operand', line=2089)
W('15,3366', 0o01046, '', '', 'DSPTEM1', kind='operand', line=2090)
# Page 976
W('15,3367', 0o65254, '', 'BZE', 'PDDL', kind='interp', line=2092)
W('15,3370', 0o33400, '', '', 'P57C', 'IF KEY IN TIME ZERO - TALIGN=CURRENT TIME', kind='operand', line=2093)
W('15,3371', 0o51025, '', 'DSU', 'BPL', 'NOT ZERO SO EXCHANGE PD WITH DSPTEM1', kind='interp', line=2094)
W('15,3372', 0o01046, '', '', 'DSPTEM1', kind='operand', line=2095)
W('15,3373', 0o33400, '', '', 'P57C', kind='operand', line=2096)
W('15,3374', 0o45545, '', 'DLOAD', 'STADR', 'IF KEYIN TIME GREATER THAN CURRENT TIME', kind='interp', line=2097)
W('15,3375', 0o74335, '', 'STORE', 'TIG', 'STORE IT IN TIG', kind='interp', line=2098)
W('15,3376', 0o36775, '', 'STCALL', 'TALIGN', kind='interp', line=2099)
W('15,3377', 0o33402, '', '', 'P57D', kind='operand', line=2100)
W('15,3400', 0o45545, 'P57C', 'DLOAD', 'STADR', kind='interp', line=2101)
W('15,3401', 0o75002, '', 'STORE', 'TALIGN', kind='interp', line=2102)
W('15,3402', 0o34041, 'P57D', 'STCALL', 'TDEC1', kind='interp', line=2103)
W('15,3403', 0o27057, '', '', 'LEMPREC', 'COMPUTE DESIRED IMU ORIENTATION STORE', kind='operand', line=2104)
W('15,3404', 0o53575, '', 'VLOAD', 'UNIT', 'IN X,Y,ZSMD', kind='interp', line=2105)
W('15,3405', 0o00001, '', '', 'RATT', kind='operand', line=2106)
W('15,3406', 0o37607, '', 'STCALL', 'XSMD', kind='interp', line=2107)
W('15,3407', 0o11013, '', '', 'LSORIENT', kind='operand', line=2108)
W('15,3410', 0o77776, '', 'EXIT', kind='interp', line=2109)
W('15,3411', 0o34755, 'PACKOPTN', 'CAF', 'ZERO', 'PACK FLAG BITS FOR OPTION DISPLAY', line=2110)
W('15,3412', 0o55145, '', 'TS', 'OPTION1 +1', 'JAM ZERO IN ALIGNMENT OPTION', line=2111)
W('15,3413', 0o55146, '', 'TS', 'OPTION1 +2', 'INITIALIZE FLAG BIT CONFIGURATION', line=2112)
W('15,3414', 0o34737, '', 'CAF', 'REFSMBIT', line=2113)
W('15,3415', 0o70077, '', 'MASK', 'FLAGWRD3', 'REFSMFLG', line=2114)
W('15,3416', 0o10000, '', 'CCS', 'A', line=2115)
W('15,3417', 0o34745, '', 'CAF', 'BIT7', 'SET', line=2116)
W('15,3420', 0o27146, '', 'ADS', 'OPTION1 +2', 'CLEAR -- JUST ZERO', line=2117)
W('15,3421', 0o34753, '', 'CAF', 'ATTFLBIT', line=2118)
W('15,3422', 0o70102, '', 'MASK', 'FLAGWRD6', 'ATTFLG', line=2119)
W('15,3423', 0o10000, '', 'CCS', 'A', line=2120)
W('15,3424', 0o34750, '', 'CAF', 'BIT4', 'SET', line=2121)
W('15,3425', 0o27146, '', 'ADS', 'OPTION1 +2', 'CLEAR -- ZERO IN A', line=2122)
W('15,3426', 0o34750, '', 'CAF', 'BIT4', line=2123)
W('15,3427', 0o55144, '', 'TS', 'OPTION1', 'JAM 00010 IN OPTION1 FOR CHECK LIST', line=2124)

W('15,3430', 0o33651, 'DSPOPTN', 'CAF', 'VB05N06', 'DISPLAY OPTION CODE AND FLAG BITS', line=2126)
W('15,3431', 0o04616, '', 'TC', 'BANKCALL', line=2127)
W('15,3432', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=2128)
W('15,3433', 0o16001, '', 'TCF', 'GOTOPOOH', 'VB34 -- TERMINATE', line=2129)
W('15,3434', 0o13436, '', 'TCF', '+2', 'V33 -- PROCEED', line=2130)
W('15,3435', 0o13430, '', 'TCF', 'DSPOPTN', 'V32 -- RECYCLE', line=2131)

W('15,3436', 0o34737, '', 'CAF', 'REFSMBIT', line=2133)
W('15,3437', 0o70077, '', 'MASK', 'FLAGWRD3', line=2134)
W('15,3440', 0o10000, '', 'CCS', 'A', line=2135)
W('15,3441', 0o13541, '', 'TCF', 'GETLMATT', 'SET, GO COMPUTE LM ATTITUDE', line=2136)
W('15,3442', 0o34753, '', 'CAF', 'ATTFLBIT', 'CLEAR -- CHECK ATTFLAG FOR STORED ATTITUDE.', line=2137)
W('15,3443', 0o70102, '', 'MASK', 'FLAGWRD6', line=2138)
W('15,3444', 0o10000, '', 'CCS', 'A', line=2139)
W('15,3445', 0o13545, '', 'TCF', 'BYLMATT', 'ALLFLG SET, CHK OPTION FOR GRAVITY COMP', line=2140)
W('15,3446', 0o34752, '', 'CAF', 'BIT2', 'SEE IF OPTION 2 OR 3', line=2141)
# Page 977
W('15,3447', 0o71145, '', 'MASK', 'OPTION2', line=2143)
W('15,3450', 0o10000, '', 'CCS', 'A', line=2144)
W('15,3451', 0o13545, '', 'TCF', 'BYLMATT', "OPTION 2 OR 3 BUT DON'T HAVE ATTITUDE", line=2145)
W('15,3452', 0o05567, '', 'TC', 'ALARM', 'OPTION INCONSISTENT WITH FLAGS -- ALARM 701', line=2146)
W('15,3453', 0o00701, '', 'OCT', '701', kind='data', line=2147)
W('15,3454', 0o35006, '', 'CAF', 'VB05N09', 'DISPLAY ALARM FOR ACTION', line=2148)
W('15,3455', 0o04616, '', 'TC', 'BANKCALL', line=2149)
W('15,3456', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=2150)
W('15,3457', 0o16001, '', 'TCF', 'GOTOPOOH', 'VB34 -- TERMINATE', line=2151)
W('15,3460', 0o13430, '', 'TCF', 'DSPOPTN', 'V33 -- PROCEED *********TEMPORARY', line=2152)
W('15,3461', 0o13430, '', 'TCF', 'DSPOPTN', 'VB32 -- RECYCLE TO OPTION DISPLAY V 05N06', line=2153)

# Page 978
# TRANSFORM VEC1,2 FROM MOON FIXED TO REF AND JAM BACK IN VEC1,2

W('15,3462', 0o40220, 'MFREF', 'STQ', 'SETPD', kind='interp', line=2158)
W('15,3463', 0o02746, '', '', 'QMAJ', kind='operand', line=2159)
W('15,3464', 0o00001, '', '', '0', kind='operand', line=2160)
W('15,3465', 0o77634, '', 'RTB', kind='interp', line=2161)
W('15,3466', 0o21573, '', '', 'LOADTIME', kind='operand', line=2162)
W('15,3467', 0o27562, '', 'STOVL', 'TSIGHT', kind='interp', line=2163)
W('15,3470', 0o02723, '', '', 'VEC1', kind='operand', line=2164)
W('15,3471', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=2165)
W('15,3472', 0o03562, '', '', 'TSIGHT', kind='operand', line=2166)
W('15,3473', 0o77624, '', 'CALL', kind='interp', line=2167)
W('15,3474', 0o55716, '', '', 'RP-TO-R', kind='operand', line=2168)
W('15,3475', 0o26723, '', 'STOVL', 'VEC1', kind='interp', line=2169)
W('15,3476', 0o02731, '', '', 'VEC2', kind='operand', line=2170)
W('15,3477', 0o65201, '', 'SETPD', 'PDDL', kind='interp', line=2171)
W('15,3500', 0o00001, '', '', '0', kind='operand', line=2172)
W('15,3501', 0o03562, '', '', 'TSIGHT', kind='operand', line=2173)
W('15,3502', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=2174)
W('15,3503', 0o55716, '', '', 'RP-TO-R', kind='operand', line=2175)
W('15,3504', 0o36731, '', 'STCALL', 'VEC2', kind='interp', line=2176)
W('15,3505', 0o02746, '', '', 'QMAJ', kind='operand', line=2177)

# Page 979
# COMPUTE LM ATTITUDE IN MOON FIXED COORDINATES USING REFSMMAT AND
# STORE IN YNBSAV AND ZNBSAV.

W('15,3506', 0o45020, 'REFMF', 'STQ', 'CALL', kind='interp', line=2183)
W('15,3507', 0o02746, '', '', 'QMAJ', kind='operand', line=2184)
W('15,3510', 0o47537, '', '', 'CDUTRIG', 'GET SIN AND COS OF CDUS', kind='operand', line=2185)
W('15,3511', 0o40234, '', 'RTB', 'SETPD', kind='interp', line=2186)
W('15,3512', 0o21573, '', '', 'LOADTIME', kind='operand', line=2187)
W('15,3513', 0o00001, '', '', '0', kind='operand', line=2188)
W('15,3514', 0o37562, '', 'STCALL', 'TSIGHT', kind='interp', line=2189)
W('15,3515', 0o20030, '', '', 'CALCSMSC', 'GET YNB IN SM', kind='operand', line=2190)
W('15,3516', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=2191)
W('15,3517', 0o02673, '', '', 'YNB', kind='operand', line=2192)
W('15,3520', 0o01734, '', '', 'REFSMMAT', 'YNB TO REF', kind='operand', line=2193)
W('15,3521', 0o65256, '', 'UNIT', 'PDDL', kind='interp', line=2194)
W('15,3522', 0o03562, '', '', 'TSIGHT', kind='operand', line=2195)
W('15,3523', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=2196)
W('15,3524', 0o51670, '', '', 'R-TO-RP', kind='operand', line=2197)
W('15,3525', 0o26237, '', 'STOVL', 'YNBSAV', 'YNB TO MF', kind='interp', line=2198)
W('15,3526', 0o02701, '', '', 'ZNB', kind='operand', line=2199)
W('15,3527', 0o53505, '', 'VXM', 'UNIT', kind='interp', line=2200)
W('15,3530', 0o01734, '', '', 'REFSMMAT', 'ZNB TO REF', kind='operand', line=2201)
W('15,3531', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=2202)
W('15,3532', 0o03562, '', '', 'TSIGHT', kind='operand', line=2203)
W('15,3533', 0o77624, '', 'CALL', kind='interp', line=2204)
W('15,3534', 0o51670, '', '', 'R-TO-RP', 'ZNB TO MF', kind='operand', line=2205)
W('15,3535', 0o02245, '', 'STORE', 'ZNBSAV', kind='interp', line=2206)
W('15,3536', 0o77614, '', 'SETGO', kind='interp', line=2207)
W('15,3537', 0o03036, '', '', 'ATTFLAG', kind='operand', line=2208)
W('15,3540', 0o02746, '', '', 'QMAJ', kind='operand', line=2209)

# Page 980
# BRANCH TO ALIGNMENT OPTION

W('15,3541', 0o06037, 'GETLMATT', 'TC', 'INTPRET', line=2214)
W('15,3542', 0o77624, '', 'CALL', kind='interp', line=2215)
W('15,3543', 0o33506, '', '', 'REFMF', 'GO TRANSFORM TO MF IN YNBSAV, ZNBSAV', kind='operand', line=2216)
W('15,3544', 0o77776, '', 'EXIT', kind='interp', line=2217)

W('15,3545', 0o05504, 'BYLMATT', 'TC', 'UPFLAG', 'SET INITIAL ALIGN FLAG', line=2219)
W('15,3546', 0o00205, '', 'ADRES', 'INITALGN', kind='data', line=2220)
W('15,3547', 0o34753, '', 'CAF', 'BIT1', line=2221)
W('15,3550', 0o71145, '', 'MASK', 'OPTION2', 'SEE IF OPTION 1 OR 3', line=2222)
W('15,3551', 0o10000, '', 'CCS', 'A', line=2223)
W('15,3552', 0o12563, '', 'TCF', 'GVDETER', 'OPTION 1 OR 2, GET GRAVITY', line=2224)

W('15,3553', 0o05353, 'ATTCHK', 'TC', 'PHASCHNG', line=2226)
W('15,3554', 0o04024, '', 'OCT', '04024', kind='data', line=2227)

W('15,3555', 0o34753, '', 'CAF', 'ATTFLBIT', 'NOT 1 OR 3, CHECK ATTFLAG', line=2229)
W('15,3556', 0o70102, '', 'MASK', 'FLAGWRD6', line=2230)
W('15,3557', 0o10000, '', 'CCS', 'A', line=2231)
W('15,3560', 0o13575, '', 'TCF', 'P57OPT0', 'GET ALIGNMENT VECS FOR OPTION 0', line=2232)
W('15,3561', 0o05353, 'P57JUMP', 'TC', 'PHASCHNG', line=2233)
W('15,3562', 0o04024, '', 'OCT', '04024', kind='data', line=2234)

W('15,3563', 0o05516, '', 'TC', 'DOWNFLAG', 'ATTFLG CLEAR -- RESET INTALIGN FLAG', line=2236)
W('15,3564', 0o00205, '', 'ADRES', 'INITALGN', kind='data', line=2237)
W('15,3565', 0o36245, '', 'CAF', 'THREE', line=2238)
W('15,3566', 0o71145, '', 'MASK', 'OPTION2', 'BRANCH ON OPTION CODE', line=2239)
W('15,3567', 0o50000, '', 'INDEX', 'A', line=2240)
W('15,3570', 0o13571, '', 'TCF', '+1', line=2241)
W('15,3571', 0o13575, '', 'TCF', 'P57OPT0', 'OPTION IS 0', line=2242)
W('15,3572', 0o13616, '', 'TCF', 'P57OPT1', 'OPTION IS 1', line=2243)
W('15,3573', 0o13634, '', 'TCF', 'P57OPT2', 'OPTION IS 2', line=2244)
W('15,3574', 0o13635, '', 'TCF', 'P57OPT3', 'OPTION IS 3', line=2245)

# Page 981
# OPTION 0, GET TWO ATTITUDE VECS

W('15,3575', 0o06037, 'P57OPT0', 'TC', 'INTPRET', line=2250)
W('15,3576', 0o77775, '', 'VLOAD', kind='interp', line=2251)
W('15,3577', 0o02237, '', '', 'YNBSAV', 'Y AND Z ATTITUDE WILL BE PUT IN REF', kind='operand', line=2252)
W('15,3600', 0o26723, '', 'STOVL', 'VEC1', kind='interp', line=2253)
W('15,3601', 0o02245, '', '', 'ZNBSAV', kind='operand', line=2254)
W('15,3602', 0o36731, '', 'STCALL', 'VEC2', kind='interp', line=2255)
W('15,3603', 0o47537, '', '', 'CDUTRIG', kind='operand', line=2256)
W('15,3604', 0o77624, '', 'CALL', kind='interp', line=2257)
W('15,3605', 0o20030, '', '', 'CALCSMSC', 'COMPUTE SC AXIS WRT PRESENT SM', kind='operand', line=2258)
W('15,3606', 0o77775, '', 'VLOAD', kind='interp', line=2259)
W('15,3607', 0o02673, '', '', 'YNB', kind='operand', line=2260)
W('15,3610', 0o26761, 'SAMETYP', 'STOVL', 'STARSAV1', 'Y SC AXIS WRT PRESENT SM', kind='interp', line=2261)
W('15,3611', 0o02701, '', '', 'ZNB', kind='operand', line=2262)
W('15,3612', 0o36767, '', 'STCALL', 'STARSAV2', 'Z SC AXIS WRT PRESENT SM', kind='interp', line=2263)
W('15,3613', 0o33462, '', '', 'MFREF', 'TRANSFORM VEC1,2 FROM MF TO REF', kind='operand', line=2264)
W('15,3614', 0o77650, '', 'GOTO', kind='interp', line=2265)
W('15,3615', 0o33101, '', '', 'SURFLINE', kind='operand', line=2266)

# OPTION 1, GET LANDING SITE AND Z-ATTITUDE VEC

W('15,3616', 0o06037, 'P57OPT1', 'TC', 'INTPRET', line=2270)
W('15,3617', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=2271)
W('15,3620', 0o02023, '', '', 'RLS', 'LANDING SITE VEC', kind='operand', line=2272)
W('15,3621', 0o26723, '', 'STOVL', 'VEC1', kind='interp', line=2273)
W('15,3622', 0o02245, '', '', 'ZNBSAV', 'Z ATTITUDE VEC', kind='operand', line=2274)
W('15,3623', 0o36731, '', 'STCALL', 'VEC2', kind='interp', line=2275)
W('15,3624', 0o47537, '', '', 'CDUTRIG', kind='operand', line=2276)
W('15,3625', 0o77624, '', 'CALL', kind='interp', line=2277)
W('15,3626', 0o20030, '', '', 'CALCSMSC', 'GET ZNB AXIS WRT PRES SM FOR STARSAV2', kind='operand', line=2278)
W('15,3627', 0o45175, '', 'VLOAD', 'CALL', kind='interp', line=2279)
W('15,3630', 0o02231, '', '', 'GSAV', 'TRANS GSAV FROM NB TO SM FOR STARSAV1', kind='operand', line=2280)
W('15,3631', 0o47661, '', '', 'CDU*NBSM', kind='operand', line=2281)
W('15,3632', 0o77650, '', 'GOTO', kind='interp', line=2282)
W('15,3633', 0o33610, '', '', 'SAMETYP', 'NOW DO SAME AS OPTION 0', kind='operand', line=2283)

# Page 982
# OPTION 2, GET TWO STAR SIGHTINGS

W('15,3634', 0o13045, 'P57OPT2', 'TCF', '2STARS', 'DO SIGHTING ON 2 STARS', line=2288)

# OPTION 3, GET LANDING SITE VEC AND ONE STAR SIGHTING

W('15,3635', 0o06037, 'P57OPT3', 'TC', 'INTPRET', line=2292)
W('15,3636', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=2293)
W('15,3637', 0o02023, '', '', 'RLS', 'LANDING SITE VEC', kind='operand', line=2294)
W('15,3640', 0o02723, '', 'STORE', 'VEC1', kind='interp', line=2295)
W('15,3641', 0o26731, '', 'STOVL', 'VEC2', 'DUMMY VEC2 FOR 2ND CATALOG STAR', kind='interp', line=2296)
W('15,3642', 0o02231, '', '', 'GSAV', 'GRAVITY VEC NB', kind='operand', line=2297)
W('15,3643', 0o77624, '', 'CALL', kind='interp', line=2298)
W('15,3644', 0o47661, '', '', 'CDU*NBSM', 'TRANS GSAV FROM NB TO SM FOR STARSAV1', kind='operand', line=2299)
W('15,3645', 0o36761, '', 'STCALL', 'STARSAV1', kind='interp', line=2300)
W('15,3646', 0o33462, '', '', 'MFREF', 'STARSAV2 IS STORED AS 2ND OBSERVED STAR', kind='operand', line=2301)
W('15,3647', 0o77776, '', 'EXIT', kind='interp', line=2302)
W('15,3650', 0o13047, '', 'TCF', '1STAR', '1STAR GET VEC2, STARSAV2 GOES TO SURFLINE.', line=2303)

W('15,3651', 0o01206, 'VB05N06', 'VN', '506', kind='data', line=2305)

# Page 983
# CHECK IMODES30 TO VERIFY IMU IS ON

W('15,3652', 0o41302, 'IMUCHK', 'CS', 'IMODES30', line=2310)
W('15,3653', 0o74743, '', 'MASK', 'BIT9', line=2311)
W('15,3654', 0o10000, '', 'CCS', 'A', 'IS IMU ON', line=2312)
W('15,3655', 0o13661, '', 'TCF', '+4', 'YES', line=2313)

W('15,3656', 0o05567, '', 'TC', 'ALARM', 'NO, SEND ALARM AND EXIT', line=2315)
W('15,3657', 0o00210, '', 'OCT', '210', kind='data', line=2316)
W('15,3660', 0o06001, '', 'TC', 'GOTOPOOH', line=2317)

W('15,3661', 0o05504, '', 'TC', 'UPFLAG', line=2319)
W('15,3662', 0o00007, '', 'ADRES', 'IMUSE', 'SET IMUSE FLAG', kind='data', line=2320)

W('15,3663', 0o04631, '', 'TC', 'SWRETURN', line=2322)

#   BANK 04
#   SETLOC AOTMARK2
#   BANK
#   COUNT* $$/P57

W('04,3013', 0o77220, 'LSORIENT', 'STQ', 'VLOAD', kind='interp', line=2329)
W('04,3014', 0o02746, '', '', 'QMAJ', kind='operand', line=2330)
W('04,3015', 0o01555, '', '', 'RRECTCSM', kind='operand', line=2331)
W('04,3016', 0o47235, '', 'VXV', 'VXV', kind='interp', line=2332)
W('04,3017', 0o01563, '', '', 'VRECTCSM', kind='operand', line=2333)
W('04,3020', 0o03607, '', '', 'XSMD', kind='operand', line=2334)
W('04,3021', 0o77656, '', 'UNIT', kind='interp', line=2335)
W('04,3022', 0o03623, '', 'STORE', 'ZSMD', kind='interp', line=2336)
W('04,3023', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=2337)
W('04,3024', 0o03607, '', '', 'XSMD', kind='operand', line=2338)
W('04,3025', 0o37615, '', 'STCALL', 'YSMD', kind='interp', line=2339)
W('04,3026', 0o02746, '', '', 'QMAJ', kind='operand', line=2340)
