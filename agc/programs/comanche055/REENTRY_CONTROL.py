"""REENTRY_CONTROL.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/REENTRY_CONTROL.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 844-881 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('REENTRY_CONTROL', 'REENTRY_CONTROL.agc', 'Comanche055', pages='844-881')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     REENTRY_CONTROL.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        844-882
# Mod history:  2009-05-08 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
# 2009-05-23 RSB  In a couple of 2OCT statements, removed the
# space between the first and second octal words.
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

# Page 844
# ENTRY INITIALIZATION ROUTINE
# ----------------------------

#   BANK 25
#   SETLOC REENTRY
#   BANK

#   COUNT* $$/ENTRY
#   EBANK= RTINIT

S('EBENTRY', 'equals', 0o5060, line=43)
S('EBAOG', 'equals', 0o5057, line=44)
S('NTRYPRIO', 'equals', 0o5002, line=45)  # (SERVICER)
S('CM/FLAGS', 'equals', 0o102, line=46)

W('25,2000', 0o77776, 'STARTENT', 'EXIT', '', 'MM = 63', kind='interp', line=48)

# COME HERE FROM CM/POSE.  RESTARTED IN CM/POSE.
W('25,2001', 0o42113, '', 'CS', 'ENTMASK', 'INITIALIZE ALL SWITCHES TO ZERO', line=51)
# EXCEPT LATSW, ENTRYDSP, AND GONEPAST.
# GONEBY 112D BIT8 FLAG7, SELF-INITIALIZING.
W('25,2002', 0o00004, '', 'INHINT', line=54)
W('25,2003', 0o70102, '', 'MASK', 'CM/FLAGS', line=55)
# ENTRYDSP = 92D B13
# GONEPAST=95D B10.     RELVELSW=96D B9
# EGSW = 97D B8         NOSWITCH = 98D B7
# HIND=99D B6           INRLSW=100D B5
# LATSW=101D B4         .05GSW=102D B3

W('25,2004', 0o62114, '', 'AD', 'ENTRYSW', 'SET ENTRYDSP, LATSW, GONEPAST.', line=62)
W('25,2005', 0o54102, '', 'TS', 'CM/FLAGS', line=63)

W('25,2006', 0o00003, '', 'RELINT', line=65)

W('25,2007', 0o06006, '', 'TC', 'INTPRET', line=67)

W('25,2010', 0o77735, '', 'SLOAD', kind='interp', line=69)
W('25,2011', 0o03011, '', '', 'LODPAD', kind='operand', line=70)
W('25,2012', 0o03626, '', 'STORE', 'LOD', kind='interp', line=71)

W('25,2013', 0o77735, '', 'SLOAD', kind='interp', line=73)
W('25,2014', 0o03010, '', '', 'LADPAD', kind='operand', line=74)
W('25,2015', 0o03624, '', 'STORE', 'LAD', kind='interp', line=75)

W('25,2016', 0o77605, '', 'DMP', '', 'L/DCMINR = LAD COS(15)', kind='interp', line=77)
W('25,2017', 0o15323, '', '', 'COS15', kind='operand', line=78)
W('25,2020', 0o17630, '', 'STODL', 'L/DCMINR', kind='interp', line=79)
W('25,2021', 0o15146, '', '', 'LATSLOPE', kind='operand', line=80)
W('25,2022', 0o70405, '', 'DMP', 'SR1', 'KLAT = LAD/24', kind='interp', line=81)
W('25,2023', 0o03624, '', '', 'LAD', kind='operand', line=82)
# Page 845
W('25,2024', 0o17632, '', 'STODL', 'KLAT', kind='interp', line=84)
W('25,2025', 0o15177, '', '', 'Q7F', kind='operand', line=85)
W('25,2026', 0o17175, '', 'STODL', 'Q7', 'Q7 = Q7F', kind='interp', line=86)
W('25,2027', 0o17372, '', '', 'NEARONE', '1.0 -1BIT', kind='operand', line=87)
W('25,2030', 0o17614, '', 'STODL', 'FACTOR', kind='interp', line=88)
W('25,2031', 0o03624, '', '', 'LAD', kind='operand', line=89)
W('25,2032', 0o57565, '', 'SIGN', 'DCOMP', kind='interp', line=90)
W('25,2033', 0o03327, '', '', 'HEADSUP', 'MAY BE NOISE FOR DISPLAY P61', kind='operand', line=91)
W('25,2034', 0o37634, '', 'STCALL', 'L/D', 'L/D = - LAD SGN(HEADSUP)', kind='interp', line=92)

W('25,2035', 0o52063, '', '', 'STARTEN1', 'RETURN VIA GOTOADDR', kind='operand', line=94)
W('25,2036', 0o47375, '', 'VLOAD', 'VXV', kind='interp', line=95)
W('25,2037', 0o01177, '', '', 'VN', '(-7) M/CS', kind='operand', line=96)
W('25,2040', 0o01760, '', '', 'UNITR', '.5 UNIT               REF COORDS', kind='operand', line=97)
W('25,2041', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=98)
W('25,2042', 0o03474, '', '', 'RT', 'RT/2 TARGET VECTOR    REF COORDS', kind='operand', line=99)
W('25,2043', 0o03676, '', 'STORE', 'LATANG', 'LATANG = UNI.RT /4', kind='interp', line=100)
W('25,2044', 0o47076, '', 'DCOMP', 'RTB', kind='interp', line=101)
W('25,2045', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=102)
W('25,2046', 0o17644, '', 'STODL', 'K2ROLL', 'K2ROLL = -SGN(LATANG)', kind='interp', line=103)

W('25,2047', 0o03624, '', '', 'LAD', kind='operand', line=105)
W('25,2050', 0o43205, '', 'DMP', 'DAD', kind='interp', line=106)
W('25,2051', 0o15201, '', '', 'Q21', kind='operand', line=107)
W('25,2052', 0o15203, '', '', 'Q22', kind='operand', line=108)
W('25,2053', 0o03712, '', 'STORE', 'Q2', 'Q2 = -1152 + 500 LAD', kind='interp', line=109)

W('25,2054', 0o66331, '', 'SSP', 'SSP', kind='interp', line=111)
W('25,2055', 0o03646, '', '', 'GOTOADDR', 'SET SELECTOR FOR INITIAL PASS', kind='operand', line=112)
W('25,2056', 0o52260, '', '', 'INITROLL', kind='operand', line=113)
W('25,2057', 0o03325, '', '', 'POSEXIT', kind='operand', line=114)
W('25,2060', 0o52115, '', '', 'SCALEPOP', 'SET CM/POSE TO CONTINUE AT SCALEPOP', kind='operand', line=115)

W('25,2061', 0o77634, '', 'RTB', kind='interp', line=117)
W('25,2062', 0o53611, '', '', 'SERVNOUT', 'OMIT INITIAL DISPLAY, SINCE 1ST GUESSBAD', kind='operand', line=118)

# CALCULATE THE INITIAL TARGET VECTOR: RTINIT, ALSO RTEAST, RTNORM AND RT.  ALL ARE .5 UNIT AND IN
# REFERENCE COORDINATES.

W('25,2063', 0o77220, 'STARTEN1', 'STQ', 'VLOAD', kind='interp', line=123)
W('25,2064', 0o03645, '', '', 'GOTOADDR', kind='operand', line=124)
W('25,2065', 0o03401, '', '', 'LAT(SPL)', 'TARGET COORDINATES', kind='operand', line=125)
W('25,2066', 0o43014, '', 'CLEAR', 'CLEAR', 'DO CALL USING PAD RADIUS.  WILL UNIT IT.', kind='interp', line=126)
W('25,2067', 0o00662, '', '', 'ERADFLAG', 'ANYWAY.', kind='operand', line=127)
W('25,2070', 0o01663, '', '', 'LUNAFLAG', kind='operand', line=128)
W('25,2071', 0o15104, '', 'STODL', 'LAT', kind='interp', line=129)
W('25,2072', 0o15335, '', '', '3ZEROS', kind='operand', line=130)

W('25,2073', 0o15110, '', 'STODL', 'LAT +4', 'SET ALT=0.', kind='interp', line=132)
W('25,2074', 0o01205, '', '', 'PIPTIME', 'ESTABLISH RTINIT AT TIME OF PRESENT', kind='operand', line=133)
# Page 846
# RN AND VN.
W('25,2075', 0o37524, '', 'STCALL', 'TIME/RTO', 'SAVE TIME BASE OF RTINIT.', kind='interp', line=136)
W('25,2076', 0o26441, '', '', 'LALOTORV', 'C(MPAC) =TIME  (PIPTIME)', kind='operand', line=137)
W('25,2077', 0o77656, '', 'UNIT', '', 'ANSWER IN ALPHAV ALSO', kind='interp', line=138)
W('25,2100', 0o17452, '', 'STODL', 'RTINIT', '.5 UNIT TARGET                REF COORDS', kind='interp', line=139)
W('25,2101', 0o12112, '', '', '500SEC', 'NOMINAL ENTRY TIME FOR P63', kind='operand', line=140)
# TIME/RTO = PIPTIME, STILL.
W('25,2102', 0o37606, '', 'STCALL', 'DTEAROT', 'INITIALIZE EARROT', kind='interp', line=142)
W('25,2103', 0o46215, '', '', 'EARROT1', 'GET RT', kind='operand', line=143)
W('25,2104', 0o72441, '', 'DOT', 'SL1', kind='interp', line=144)
W('25,2105', 0o01760, '', '', 'UNITR', 'RT/2 IN MPAC', kind='operand', line=145)
W('25,2106', 0o77726, '', 'ACOS', kind='interp', line=146)
W('25,2107', 0o37702, '', 'STCALL', 'THETAH', 'RANGE ANGLE /360', kind='interp', line=147)
W('25,2110', 0o03645, '', '', 'GOTOADDR', 'RETURN TO CALLER', kind='operand', line=148)

W('25,2111', 0o00003, '500SEC', '2DEC', '50000 B-28', 'CS', kind='data', line=150)
W('25,2112', 0o01520, kind='data', line=150)

W('25,2113', 0o11774, 'ENTMASK', 'OCT', '11774', kind='data', line=152)
W('25,2114', 0o11010, 'ENTRYSW', 'OCT', '11010', 'ENTRYDSP B13, GONEPAST B10, LATSW B4', kind='data', line=153)
# Page 847

W('25,2115', 0o77624, 'SCALEPOP', 'CALL', kind='interp', line=156)
W('25,2116', 0o52125, '', '', 'TARGETNG', kind='operand', line=157)

W('25,2117', 0o77776, '', 'EXIT', kind='interp', line=159)

W('25,2120', 0o05412, 'REFAZE10', 'TC', 'PHASCHNG', line=161)
W('25,2121', 0o10035, '', 'OCT', '10035', 'SERVICER 5.3 RESTART AT REFAZE10', kind='data', line=162)

W('25,2122', 0o06006, '', 'TC', 'INTPRET', line=164)

# JUMP TO PARTICULAR RE-ENTRY PHASE:
# SEQUENCE
W('25,2123', 0o77650, '', 'GOTO', kind='interp', line=168)
W('25,2124', 0o03645, '', '', 'GOTOADDR', kind='operand', line=169)

# GOTOADDR CONTAINS THE ADDRESS OF THE ROLL COMMAND EQUATIONS TO THE CURRENT PHASE OF
# RE-ENTRY.  SEQUENCING IS AS FOLLOWS:
#
# INITROLL      ADDRESS IS SET HERE INITIALLY.  HOLDS INITIAL ROLL ATTITUDE UNTIL  KAT  IS EXCEEDED.  THEN HOLDS NEW ROLL
# ATTITUDE UNTIL  VRTHRESH  IS EXCEEDED.  THEN BRANCHES TO
#
# HUNTEST       THIS SECTION CHECKS TO SEE IF THE PREDICTED RANGE AT NOMINAL   L/D FROM PRESENT CONDITIONS IS LESS
# THAN THE DESIRED RANGE.
# IF NOT --- A ROLL COMMAND IS GENERATED BY THE CONSTANT DRAG CONTROLLER.
# IF SO  --- CONTROL AND GOTOADDR ARE SET TO UPCONTRL.
# USUALLY NO ITERATION IS INVOLVED EXCEPT IF THE RANGE DESIRED IS TOO LONG ON THE FIRST PASS THROUGH
# HUNTEST.
#
# UPCONTRL      CONTROLS ROLL DURING THE SUPER-CIRCULAR PHASE.  UPCONTRL IS TERMINATED EITHER
# (A) WHEN THE DRAG (AS MEASURED BY THE PIPAS) FALLS BELOW Q7, OR
# (B) IF RDOT IS NEGATIVE AND REFERENCE VL EXCEEDS V.
# IN CASE (A),  GOTOADDR  IS SET TO  KEP2  AND IN CASE (B), TO  PREDICT3  SKIPPING THE KEPLER PHASE OF
# ENTRY.
#
# KEP2          GOTOADDR IS SET HERE DURING THE KEPLER PHASE TO MONITOR DRAG.  THE SPACECRAFT IS INSTANTANEOUSLY
# TRIMMED IN PITCH AND YAW TO THE COMPUTED RELATIVE VELOCITY.  THE LAST COMPUTED ROLL ANGLE IS MAINTAINED.
# WHEN THE MEASURED DRAG EXCEEDS Q7 +0.5,  GOTOADDR  IS SET TO
#
# PREDICT3      THIS CONTROLS THE FINAL SUB-ORBITAL PHASE. ROLL COMMANDS CEASE
# WHEN  V  IS LESS THAN  VQUIT .  AN EXIT IS MADE TO
#
# P67.1         THE LAST COMPUTED ROLL ANGLE IS MAINTAINED.  RATE DAMPING IS DONE IN PITCH AND YAW.  PRESENT LATITUDE
# AND LONGITUDE ARE COMPUTED FOR DISPLAY.
# ENTRY IS TERMINATED WHEN DISKY RESPONSE IS MADE TO TO THIS FINAL FLASHING DISPLAY.

# Page 848
# PROCESS AVERAGE G OUTPUT...SCALE IT AND GET INPUT DATA

# * START  TARGETING ...

#   EBANK= RTINIT

# TARGETNG IS CALLED BY P61, FROM GROUP 4.
# TARGETNG IS CALLED BY ENTRY, FROM GROUP 5.

# ALL MM COME HERE.
W('25,2125', 0o77214, 'TARGETNG', 'BOFF', 'VLOAD', 'ENTER WITH PROPER EB FROM CM/POSE(TEST)', kind='interp', line=212)
W('25,2126', 0o03346, '', '', 'RELVELSW', 'RELVELSW = 96D BIT9', kind='operand', line=213)
W('25,2127', 0o52133, '', '', 'GETVEL', 'WANT INERTIAL VEL.  GO GET IT.', kind='operand', line=214)
W('25,2130', 0o03526, '', '', '-VREL', 'NEW V IS RELATIVE, CONTINUE', kind='operand', line=215)

W('25,2131', 0o52076, '', 'VCOMP', 'GOTO', '(VREL) = (V) + KWE UNITR*UNITW', kind='interp', line=217)
W('25,2132', 0o52136, '', '', 'GETUNITV -1', '- VREL WAS LEFT BY CM/POSE', kind='operand', line=218)

W('25,2133', 0o74375, 'GETVEL', 'VLOAD', 'VXSC', 'INERTIAL V WANTED', kind='interp', line=220)
W('25,2134', 0o01177, '', '', 'VN', 'KVSCALE = (12800 / .3048) / 2VS', kind='operand', line=221)
W('25,2135', 0o15231, '', '', 'KVSCALE', 'KVSCALE = .81491944', kind='operand', line=222)
W('25,2136', 0o03516, '', 'STORE', 'VEL', 'V/2 VS', kind='interp', line=223)

W('25,2137', 0o44056, 'GETUNITV', 'UNIT', 'STQ', kind='interp', line=225)
W('25,2140', 0o03373, '', '', '60GENRET', kind='operand', line=226)
W('25,2141', 0o17510, '', 'STODL', 'UNITV', kind='interp', line=227)
W('25,2142', 0o00043, '', '', '34D', kind='operand', line=228)
W('25,2143', 0o03622, '', 'STORE', 'VSQUARE', 'VSQ/4', kind='interp', line=229)

W('25,2144', 0o77625, '', 'DSU', '', 'LEQ = VSQUARE - 1', kind='interp', line=231)
W('25,2145', 0o15325, '', '', 'FOURTH', '4 G-S FULL SCALE', kind='operand', line=232)
W('25,2146', 0o17654, '', 'STODL', 'LEQ', 'LEQ/4', kind='interp', line=233)

W('25,2147', 0o00045, '', '', '36D', kind='operand', line=235)
W('25,2150', 0o27674, '', 'STOVL', 'V', 'V/2 VS = VEL/2 VS', kind='interp', line=236)

W('25,2151', 0o03516, '', '', 'VEL', kind='operand', line=238)
W('25,2152', 0o72441, '', 'DOT', 'SL1', 'RDOT= V.UNITR', kind='interp', line=239)
W('25,2153', 0o01760, '', '', 'UNITR', kind='operand', line=240)
W('25,2154', 0o27700, '', 'STOVL', 'RDOT', 'RDOT /2 VS', kind='interp', line=241)

W('25,2155', 0o01163, '', '', 'DELV', 'PIPA COUNTS IN PLATFORM COORDS.', kind='operand', line=243)
W('25,2156', 0o41246, '', 'ABVAL', 'DMP', kind='interp', line=244)
W('25,2157', 0o15233, '', '', 'KASCALE', kind='operand', line=245)
W('25,2160', 0o53152, '', 'SL1', 'BZE', kind='interp', line=246)
W('25,2161', 0o55133, '', '', 'SETMIND', kind='operand', line=247)
W('25,2162', 0o27640, 'DSTORE', 'STOVL', 'D', 'ACCELERATION USED TO APPROX DRAG', kind='interp', line=248)
W('25,2163', 0o03516, '', '', 'VEL', kind='operand', line=249)
W('25,2164', 0o53435, '', 'VXV', 'UNIT', 'UNI = UNIT(V*R)', kind='interp', line=250)
# Page 849
W('25,2165', 0o01760, '', '', 'UNITR', kind='operand', line=252)
W('25,2166', 0o03502, '', 'STORE', 'UNI', '.5 UNI                REF COORDS.', kind='interp', line=253)

W('25,2167', 0o71214, '', 'BOFF', 'DLOAD', kind='interp', line=255)
W('25,2170', 0o03346, '', '', 'RELVELSW', kind='operand', line=256)
W('25,2171', 0o55074, '', '', 'GETETA', kind='operand', line=257)
W('25,2172', 0o15335, '', '', '3ZEROS', kind='operand', line=258)
W('25,2173', 0o43225, 'UPDATERT', 'DSU', 'DAD', 'PIPTIME-TIME/RTO =ELAPSED TIME SINCE', kind='interp', line=259)
# RTINIT WAS ESTABLISHED.
W('25,2174', 0o03524, '', '', 'TIME/RTO', kind='operand', line=261)
W('25,2175', 0o01205, '', '', 'PIPTIME', kind='operand', line=262)
W('25,2176', 0o37606, '', 'STCALL', 'DTEAROT', 'GET PREDICTED TARGET VECTOR RT', kind='interp', line=263)

W('25,2177', 0o46225, '', '', 'EARROT2', kind='operand', line=265)
W('25,2200', 0o40241, '', 'DOT', 'SETPD', 'SINCE (RT) UNIT VECT, THIS IS 1/4 MAX', kind='interp', line=266)
W('25,2201', 0o03502, '', '', 'UNI', 'LATANG = RT.UNI', kind='operand', line=267)
W('25,2202', 0o00001, '', '', '0', kind='operand', line=268)
W('25,2203', 0o27676, '', 'STOVL', 'LATANG', 'LATANG = MAC LATANG / 4', kind='interp', line=269)

W('25,2204', 0o03474, '', '', 'RT', kind='operand', line=271)
W('25,2205', 0o77614, '', 'CLEAR', kind='interp', line=272)
W('25,2206', 0o03667, '', '', 'GONEBY', 'SHOW HAVE NOT GONE PAST TARGET.', kind='operand', line=273)
W('25,2207', 0o50235, '', 'VXV', 'DOT', 'IF RT*UNITR.UNI NEG, GONEBY=1', kind='interp', line=274)
W('25,2210', 0o01760, '', '', 'UNITR', 'GONEPAST IS CONDITIONAL SW SET IN', kind='operand', line=275)
W('25,2211', 0o03502, '', '', 'UNI', 'FINAL PHASE.', kind='operand', line=276)
W('25,2212', 0o43044, '', 'BPL', 'SET', kind='interp', line=277)
W('25,2213', 0o52215, '', '', '+2', kind='operand', line=278)
W('25,2214', 0o03467, '', '', 'GONEBY', 'SHOW HAVE GONE PAST TARGET.', kind='operand', line=279)

W('25,2215', 0o77775, '', 'VLOAD', kind='interp', line=281)
W('25,2216', 0o03474, '', '', 'RT', kind='operand', line=282)
W('25,2217', 0o45241, 'GETANGLE', 'DOT', 'DSU', 'THETA = ARCCOS(RT.UNITR)', kind='interp', line=283)
W('25,2220', 0o01760, '', '', 'UNITR', kind='operand', line=284)
W('25,2221', 0o15163, '', '', 'NEAR1/4', 'TO IMPROVE ACCURACY, CALC RANGE BY', kind='operand', line=285)
W('25,2222', 0o43244, '', 'BPL', 'DAD', 'TINYTHET IF HIGH ORDER PART OF', kind='interp', line=286)
W('25,2223', 0o55136, '', '', 'TINYTHET', 'ARCCOS ARGUMENT IS ZERO', kind='operand', line=287)
W('25,2224', 0o15163, '', '', 'NEAR1/4', kind='operand', line=288)
W('25,2225', 0o65552, '', 'SL1', 'ACOS', kind='interp', line=289)
W('25,2226', 0o03702, 'THETDONE', 'STORE', 'THETAH', 'THETAH/360', kind='interp', line=290)
# HI WORD, LO BIT =1.32 NM=360 60/16384

W('25,2227', 0o57414, '', 'BON', 'DCOMP', kind='interp', line=293)
W('25,2230', 0o03707, '', '', 'GONEBY', '=1 IF HAVE GONE PAST TARGET.', kind='operand', line=294)
# (SIGN MAY BECOME ERRATIC VERY NEAR
# TARGET DUE TO LOSS OF PRECISION.)
W('25,2231', 0o52232, '', '', '+1', kind='operand', line=297)
W('25,2232', 0o17714, '', 'STODL', 'RTGON67', 'RANGE ERROR:  NEG IF WILL FALL SHORT.', kind='interp', line=298)

W('25,2233', 0o03640, '', '', 'D', kind='operand', line=300)
W('25,2234', 0o50025, '', 'DSU', 'BMN', kind='interp', line=301)
# Page 850
W('25,2235', 0o15241, '', '', '.05G', kind='operand', line=303)
W('25,2236', 0o52255, '', '', 'NO.05G', kind='operand', line=304)
W('25,2237', 0o77214, '', 'SET', 'VLOAD', kind='interp', line=305)
W('25,2240', 0o03074, '', '', '.05GSW', kind='operand', line=306)
W('25,2241', 0o03433, '', '', 'DELVREF', kind='operand', line=307)
W('25,2242', 0o50206, '', 'PUSH', 'DOT', kind='interp', line=308)
W('25,2243', 0o03542, '', '', 'UXA/2', kind='operand', line=309)
W('25,2244', 0o63552, '', 'SL1', 'DSQ', kind='interp', line=310)
W('25,2245', 0o47515, '', 'PDVL', 'VSQ', 'EXCHANGE WITH PDL.', kind='interp', line=311)
W('25,2246', 0o56225, '', 'DSU', 'DDV', kind='interp', line=312)
W('25,2247', 0o00001, '', '', '0', kind='operand', line=313)
W('25,2250', 0o75400, '', 'BOV', 'SQRT', kind='interp', line=314)
W('25,2251', 0o52253, '', '', 'NOLDCALC', 'OVFL LAST CLEARED IN EARROT2 ABOVE.', kind='operand', line=315)
W('25,2252', 0o03727, '', 'STORE', 'L/DCALC', kind='interp', line=316)

W('25,2253', 0o77650, 'NOLDCALC', 'GOTO', kind='interp', line=318)
W('25,2254', 0o03373, '', '', '60GENRET', kind='operand', line=319)

W('25,2255', 0o52014, 'NO.05G', 'CLEAR', 'GOTO', 'THIS WAY FOR DAP. (MAY INTERRUPT)', kind='interp', line=321)
W('25,2256', 0o03274, '', '', '.05GSW', '.05GSW = 102D B3', kind='operand', line=322)
W('25,2257', 0o52253, '', '', 'NOLDCALC', 'KEEP SINGLE EXIT FOR TARGETNG', kind='operand', line=323)

# Page 851
# SUBROUTINES CALLED BY SCALEPOP (TARGETING):

#   BANK 26
#   SETLOC REENTRY1
#   BANK

#   COUNT* $$/ENTRY

W('26,3074', 0o56345, 'GETETA', 'DLOAD', 'DDV', 'D = D +D(-RDOT/HS -2D/V)  DT/2', kind='interp', line=334)
# DT/2 = 2/2 =1
W('26,3075', 0o03700, '', '', 'RDOT', kind='operand', line=336)
W('26,3076', 0o15317, '', '', '-HSCALED', kind='operand', line=337)
W('26,3077', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=338)
W('26,3100', 0o03640, '', '', 'D', kind='operand', line=339)
W('26,3101', 0o15321, '', '', '-KSCALE', kind='operand', line=340)
W('26,3102', 0o43271, '', 'DDV', 'DAD', kind='interp', line=341)
W('26,3103', 0o03674, '', '', 'V', kind='operand', line=342)
# -RDOT/HS FROM PDL.
W('26,3104', 0o43205, '', 'DMP', 'DAD', kind='interp', line=344)
W('26,3105', 0o03640, '', '', 'D', kind='operand', line=345)
W('26,3106', 0o03640, '', '', 'D', kind='operand', line=346)
W('26,3107', 0o03640, '', 'STORE', 'D', kind='interp', line=347)

W('26,3110', 0o71214, '', 'BON', 'DLOAD', 'EGSW INDICATES FINAL PHASE.', kind='interp', line=349)
W('26,3111', 0o03307, '', '', 'EGSW', kind='operand', line=350)
W('26,3112', 0o55117, '', '', 'SUBETA', kind='operand', line=351)
W('26,3113', 0o03702, '', '', 'THETAH', kind='operand', line=352)
W('26,3114', 0o52005, '', 'DMP', 'GOTO', kind='interp', line=353)
W('26,3115', 0o15235, '', '', 'KTETA', '= 1000X2PI/(2)E14 163.84', kind='operand', line=354)
W('26,3116', 0o52173, '', '', 'UPDATERT', kind='operand', line=355)

W('26,3117', 0o45345, 'SUBETA', 'DLOAD', 'DSU', 'SWITCH FROM INERTIAL TO RELATIVE VEL.', kind='interp', line=357)
W('26,3120', 0o03674, '', '', 'V', kind='operand', line=358)
W('26,3121', 0o15325, '', '', 'VMIN', kind='operand', line=359)
W('26,3122', 0o43044, '', 'BPL', 'SET', kind='interp', line=360)
W('26,3123', 0o55125, '', '', 'SUBETA2', kind='operand', line=361)
W('26,3124', 0o03066, '', '', 'RELVELSW', kind='operand', line=362)

W('26,3125', 0o41345, 'SUBETA2', 'DLOAD', 'DMP', kind='interp', line=364)

W('26,3126', 0o03702, '', '', 'THETAH', kind='operand', line=366)
W('26,3127', 0o15237, '', '', 'KT1', 'KT1 = KT', kind='operand', line=367)
W('26,3130', 0o52071, '', 'DDV', 'GOTO', kind='interp', line=368)
W('26,3131', 0o03674, '', '', 'V', 'KT = RE(2 PI)/2 VS 16384 163.84/ 2 VSAT', kind='operand', line=369)
W('26,3132', 0o52173, '', '', 'UPDATERT', kind='operand', line=370)

W('26,3133', 0o52145, 'SETMIND', 'DLOAD', 'GOTO', kind='interp', line=372)
W('26,3134', 0o16326, '', '', '1BITDP', kind='operand', line=373)
W('26,3135', 0o52162, '', '', 'DSTORE', kind='operand', line=374)

# Page 852
W('26,3136', 0o51425, 'TINYTHET', 'DSU', 'ABS', 'ENTER WITH X-.249', kind='interp', line=377)
W('26,3137', 0o16327, '', '', '1BITDP +1', 'GET 1/4 - MPAC', kind='operand', line=378)
W('26,3140', 0o75461, '', 'SL', 'SQRT', 'SCALE UP BEFORE SQRT', kind='interp', line=379)
W('26,3141', 0o20216, '', '', '13D', 'HAS FACTOR FOR UP SCALING', kind='operand', line=380)
W('26,3142', 0o52005, '', 'DMP', 'GOTO', kind='interp', line=381)
W('26,3143', 0o15247, '', '', 'KACOS', kind='operand', line=382)
W('26,3144', 0o52226, '', '', 'THETDONE', kind='operand', line=383)

# Page 853
# * START       INITIAL ROLL ...

#   BANK 25
#   SETLOC REENTRY
#   BANK

#   COUNT* $$/ENTRY

# MM = 63 , 64 ..
W('25,2260', 0o43014, 'INITROLL', 'BON', 'BOFF', 'IF D- .05G NEG, GO TO LIMITL/D', kind='interp', line=395)
W('25,2261', 0o03312, '', '', 'INRLSW', kind='operand', line=396)
W('25,2262', 0o52362, '', '', 'INITRL1', kind='operand', line=397)
W('25,2263', 0o03354, '', '', '.05GSW', kind='operand', line=398)
W('25,2264', 0o53526, '', '', 'LIMITL/D', kind='operand', line=399)

# MM = 64, NOW
# 3
# KA = KA1 LEQ  + KA2
W('25,2265', 0o63545, '', 'DLOAD', 'DSQ', kind='interp', line=404)
W('25,2266', 0o03654, '', '', 'LEQ', kind='operand', line=405)
W('25,2267', 0o56205, '', 'DMP', 'DDV', kind='interp', line=406)
W('25,2270', 0o03654, '', '', 'LEQ', kind='operand', line=407)
W('25,2271', 0o15305, '', '', '1/KA1', '= 25 /(64  1.8)', kind='operand', line=408)
W('25,2272', 0o47015, '', 'DAD', 'RTB', kind='interp', line=409)
W('25,2273', 0o15307, '', '', 'KA2', '= .2', kind='operand', line=410)
W('25,2274', 0o54433, '', '', 'P64', 'ROLLC         VI              RDOT', kind='operand', line=411)
# XXX.XX DEG    XXXXX. FPS      XXXXX. FPS
W('25,2275', 0o03720, '', 'STORE', 'KAT', kind='interp', line=413)

W('25,2276', 0o50025, '', 'DSU', 'BMN', kind='interp', line=415)
W('25,2277', 0o15315, '', '', 'KALIM', kind='operand', line=416)
W('25,2300', 0o52304, '', '', '+4', kind='operand', line=417)
W('25,2301', 0o77745, '', 'DLOAD', kind='interp', line=418)
W('25,2302', 0o15315, '', '', 'KALIM', kind='operand', line=419)
W('25,2303', 0o03720, '', 'STORE', 'KAT', kind='interp', line=420)
W('25,2304', 0o45345, '', 'DLOAD', 'DSU', 'IF V-VFINAL1 NEG, GO TO FINAL PHASE.', kind='interp', line=421)
W('25,2305', 0o03674, '', '', 'V', kind='operand', line=422)
W('25,2306', 0o15303, '', '', 'VFINAL1', kind='operand', line=423)
W('25,2307', 0o51014, '', 'CLEAR', 'BPL', "(CAN'T CLEAR INRLSW AFTER HERE: RESTARTS)", kind='interp', line=424)
W('25,2310', 0o03265, '', '', 'GONEPAST', 'GONEPAST WAS INITIALLY SET=1 TO FORCE', kind='operand', line=425)
# ROLLC TO REMAIN AS DEFINED BY HEADSUP
# UNTIL START OF P64.  (UNTIL D > .05G)
W('25,2311', 0o52316, '', '', 'D0EQ', kind='operand', line=428)
W('25,2312', 0o52131, '', 'SSP', 'GOTO', kind='interp', line=429)
W('25,2313', 0o03646, '', '', 'GOTOADDR', kind='operand', line=430)
W('25,2314', 0o53317, '', '', 'KEP2', 'AND IDLE UNTIL D > 0.2 G.  (NO P66 HERE)', kind='operand', line=431)
W('25,2315', 0o52351, '', '', 'INROLOUT', 'GO TO LIMITL/D AFTER SETTING INRLSW.', kind='operand', line=432)

W('25,2316', 0o41345, 'D0EQ', 'DLOAD', 'DMP', 'D0 = KA3 LEQ + KA4', kind='interp', line=434)
# Page 854
W('25,2317', 0o03654, '', '', 'LEQ', kind='operand', line=436)
W('25,2320', 0o15311, '', '', 'KA3', kind='operand', line=437)
W('25,2321', 0o77615, '', 'DAD', kind='interp', line=438)
W('25,2322', 0o15313, '', '', 'KA4', kind='operand', line=439)
W('25,2323', 0o03710, '', 'STORE', 'D0', 'D0/805', kind='interp', line=440)
W('25,2324', 0o40065, '', 'BDDV', 'BOV', kind='interp', line=441)
W('25,2325', 0o15267, '', '', 'C001', '(-4/25 G) B-8', kind='operand', line=442)
W('25,2326', 0o52327, '', '', '+1', 'CLEAR OVFIND, IF ON.', kind='operand', line=443)
W('25,2327', 0o17706, '', 'STODL', 'C/D0', '(-4/D0) B-8', kind='interp', line=444)
W('25,2330', 0o03624, '', '', 'LAD', 'IF V-VFINAL +K(RDOT/V)CUBED POS,L/D=-LAD', kind='operand', line=445)
W('25,2331', 0o17634, '', 'STODL', 'L/D', kind='interp', line=446)
W('25,2332', 0o03700, '', '', 'RDOT', kind='operand', line=447)
W('25,2333', 0o41471, '', 'DDV', 'PUSH', kind='interp', line=448)
W('25,2334', 0o03674, '', '', 'V', kind='operand', line=449)
W('25,2335', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=450)
W('25,2336', 0o45271, '', 'DDV', 'DSU', kind='interp', line=451)
W('25,2337', 0o15277, '', '', '1/K44', kind='operand', line=452)
W('25,2340', 0o15301, '', '', 'VFINAL', kind='operand', line=453)
# 3
# V-VFINAL +(RDOT/V)  / K44     OVFL $

W('25,2341', 0o40015, '', 'DAD', 'BOV', kind='interp', line=457)
W('25,2342', 0o03674, '', '', 'V', kind='operand', line=458)
W('25,2343', 0o52351, '', '', 'INROLOUT', 'GO TO LIMITL/D AFTER SETTING INRLSW.', kind='operand', line=459)
W('25,2344', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=460)
W('25,2345', 0o52351, '', '', 'INROLOUT', 'GO TO LIMITL/D AFTER SETTING INRLSW.', kind='operand', line=461)
W('25,2346', 0o03624, '', '', 'LAD', kind='operand', line=462)
W('25,2347', 0o77676, '', 'DCOMP', kind='interp', line=463)
W('25,2350', 0o03634, '', 'STORE', 'L/D', kind='interp', line=464)

# SET INRLSW AT END FOR RESTART PROTECTION
W('25,2351', 0o77614, 'INROLOUT', 'BOFSET', '', 'END OF PRE .05G PATH OF INITROLL.', kind='interp', line=467)
W('25,2352', 0o03052, '', '', 'INRLSW', 'SWITCH IS ZERO INITIALLY.', kind='operand', line=468)
W('25,2353', 0o53526, '', '', 'LIMITL/D', '(GO TO)', kind='operand', line=469)

W('25,2354', 0o45345, 'KATEST', 'DLOAD', 'DSU', 'IF KAT - D POS, GO TO CONSTD', kind='interp', line=471)
W('25,2355', 0o03720, '', '', 'KAT', kind='operand', line=472)
W('25,2356', 0o03640, '', '', 'D', 'IF POS, OUT WITH COMMAND VIA LIMITL/D', kind='operand', line=473)
W('25,2357', 0o52044, '', 'BPL', 'GOTO', kind='interp', line=474)
W('25,2360', 0o53526, '', '', 'LIMITL/D', kind='operand', line=475)
W('25,2361', 0o53232, '', '', 'CONSTD', kind='operand', line=476)

W('25,2362', 0o43345, 'INITRL1', 'DLOAD', 'DAD', 'IF RDOT + VRCONT POS, GO TO HUNTEST', kind='interp', line=478)
W('25,2363', 0o03700, '', '', 'RDOT', kind='operand', line=479)
W('25,2364', 0o15261, '', '', 'VRCONT', kind='operand', line=480)
W('25,2365', 0o45040, '', 'BMN', 'CALL', 'IF POSITIVE, FALL INTO HUNTEST.', kind='interp', line=481)
W('25,2366', 0o52354, '', '', 'KATEST', kind='operand', line=482)

W('25,2367', 0o53022, '', '', 'FOREHUNT', 'INITIALIZE HUNTEST.', kind='operand', line=484)

# Page 855
# * START       HUNT TEST ..
# MM = 64
W('25,2370', 0o77731, '', 'SSP', '', 'INITIALIZE HUNTEST ON FIRST PASS', kind='interp', line=489)
W('25,2371', 0o03646, '', '', 'GOTOADDR', kind='operand', line=490)
W('25,2372', 0o52373, '', '', 'HUNTEST', 'MUST GO AFTER FOREHUNT FOR RESTARTS.', kind='operand', line=491)

W('25,2373', 0o77745, 'HUNTEST', 'DLOAD', kind='interp', line=493)
W('25,2374', 0o03640, '', '', 'D', kind='operand', line=494)
W('25,2375', 0o17664, '', 'STODL', 'A1', 'A1/805 = A1/25G', kind='interp', line=495)

W('25,2376', 0o03624, '', '', 'LAD', kind='operand', line=497)
W('25,2377', 0o17647, '', 'STODL', 'TEM1B', kind='interp', line=498)
W('25,2400', 0o03700, '', '', 'RDOT', kind='operand', line=499)
W('25,2401', 0o71240, '', 'BMN', 'DLOAD', 'IF RDOT NEG,TEM1B=LAD, OTHERWISE = LEWD', kind='interp', line=500)
W('25,2402', 0o52406, '', '', 'A0CALC', kind='operand', line=501)
W('25,2403', 0o03725, '', '', 'LEWD', kind='operand', line=502)
W('25,2404', 0o17647, '', 'STODL', 'TEM1B', kind='interp', line=503)

W('25,2405', 0o03700, '', '', 'RDOT', kind='operand', line=505)
W('25,2406', 0o43271, 'A0CALC', 'DDV', 'DAD', 'V1 = V + RDOT/TEM1B', kind='interp', line=506)
W('25,2407', 0o03647, '', '', 'TEM1B', kind='operand', line=507)
W('25,2410', 0o03674, '', '', 'V', kind='operand', line=508)
W('25,2411', 0o14326, '', 'STODL', 'V1', 'V1/2 VS', kind='interp', line=509)

W('25,2412', 0o03700, '', '', 'RDOT', kind='operand', line=511)
W('25,2413', 0o56316, '', 'DSQ', 'DDV', 'A0=(V1/V)SQ(D+RDOT SQ/(TEM1B 2 C1 HS)', kind='interp', line=512)
W('25,2414', 0o03647, '', '', 'TEM1B', kind='operand', line=513)
W('25,2415', 0o43271, '', 'DDV', 'DAD', kind='interp', line=514)
W('25,2416', 0o15273, '', '', '2C1HS', kind='operand', line=515)
W('25,2417', 0o03640, '', '', 'D', kind='operand', line=516)
W('25,2420', 0o41205, '', 'DMP', 'DMP', kind='interp', line=517)
W('25,2421', 0o00326, '', '', 'V1', kind='operand', line=518)
W('25,2422', 0o00326, '', '', 'V1', kind='operand', line=519)
W('25,2423', 0o77671, '', 'DDV', kind='interp', line=520)
W('25,2424', 0o03622, '', '', 'VSQUARE', kind='operand', line=521)
W('25,2425', 0o14330, '', 'STODL', 'A0', 'A0/805 = A0/25G', kind='interp', line=522)

W('25,2426', 0o03700, '', '', 'RDOT', kind='operand', line=524)
W('25,2427', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=525)
W('25,2430', 0o52433, '', '', 'V1LEAD', kind='operand', line=526)
W('25,2431', 0o00330, '', '', 'A0', kind='operand', line=527)
W('25,2432', 0o03664, '', 'STORE', 'A1', 'A1/25G', kind='interp', line=528)

W('25,2433', 0o51145, 'V1LEAD', 'DLOAD', 'BPL', 'IF L/D NEG, V1=V1 - 1000', kind='interp', line=530)
W('25,2434', 0o03634, '', '', 'L/D', kind='operand', line=531)
W('25,2435', 0o52442, '', '', 'HUNTEST1', kind='operand', line=532)

W('25,2436', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=534)
W('25,2437', 0o00326, '', '', 'V1', kind='operand', line=535)
# Page 856
W('25,2440', 0o15215, '', '', 'VQUIT', kind='operand', line=537)
W('25,2441', 0o00326, '', 'STORE', 'V1', kind='interp', line=538)

W('25,2442', 0o41345, 'HUNTEST1', 'DLOAD', 'DMP', 'ALP = 2 C1 HS A0/LEWD V1 V1', kind='interp', line=540)
W('25,2443', 0o00330, '', '', 'A0', kind='operand', line=541)
W('25,2444', 0o15273, '', '', '2C1HS', kind='operand', line=542)
W('25,2445', 0o40271, '', 'DDV', 'SETPD', kind='interp', line=543)
W('25,2446', 0o00326, '', '', 'V1', kind='operand', line=544)
W('25,2447', 0o00001, '', '', '0', kind='operand', line=545)
W('25,2450', 0o56271, '', 'DDV', 'DDV', kind='interp', line=546)
W('25,2451', 0o00326, '', '', 'V1', kind='operand', line=547)
W('25,2452', 0o03725, '', '', 'LEWD', kind='operand', line=548)
W('25,2453', 0o03704, '', 'STORE', 'ALP', kind='interp', line=549)

W('25,2454', 0o55221, '', 'BDSU', 'BDDV', 'FACT1 = V1 / (1 - ALP)', kind='interp', line=551)
W('25,2455', 0o17372, '', '', 'BARELY1', kind='operand', line=552)
W('25,2456', 0o00326, '', '', 'V1', kind='operand', line=553)
W('25,2457', 0o17616, '', 'STODL', 'FACT1', 'FACT1 / 2VS', kind='interp', line=554)

W('25,2460', 0o03704, '', '', 'ALP', kind='operand', line=556)
W('25,2461', 0o41225, '', 'DSU', 'DMP', 'FACT2 = ALP(ALP - 1) / A0', kind='interp', line=557)
W('25,2462', 0o17372, '', '', 'BARELY1', kind='operand', line=558)
W('25,2463', 0o03704, '', '', 'ALP', kind='operand', line=559)
W('25,2464', 0o77671, '', 'DDV', kind='interp', line=560)
W('25,2465', 0o00330, '', '', 'A0', kind='operand', line=561)
W('25,2466', 0o03620, '', 'STORE', 'FACT2', 'FACT2 (25G)', kind='interp', line=562)

W('25,2467', 0o43205, '', 'DMP', 'DAD', kind='interp', line=564)
W('25,2470', 0o03175, '', '', 'Q7', 'Q7 / 805 = Q7 / 25G', kind='operand', line=565)
W('25,2471', 0o03704, '', '', 'ALP', 'VL=FACT1 (1-SQRT(Q7 FACT2 +ALP) )', kind='operand', line=566)
W('25,2472', 0o44366, '', 'SQRT', 'BDSU', kind='interp', line=567)
W('25,2473', 0o17372, '', '', 'BARELY1', kind='operand', line=568)
W('25,2474', 0o77605, '', 'DMP', kind='interp', line=569)
W('25,2475', 0o03616, '', '', 'FACT1', kind='operand', line=570)
W('25,2476', 0o03767, '', 'STORE', 'VL', 'VL / 2 VS', kind='interp', line=571)

W('25,2477', 0o41221, '', 'BDSU', 'DMP', 'GAMMAL1 = LEWD (V1-VL)/VL', kind='interp', line=573)
W('25,2500', 0o00326, '', '', 'V1', kind='operand', line=574)
W('25,2501', 0o03725, '', '', 'LEWD', kind='operand', line=575)
W('25,2502', 0o77671, '', 'DDV', kind='interp', line=576)
W('25,2503', 0o03767, '', '', 'VL', kind='operand', line=577)
W('25,2504', 0o14027, '', 'STODL', 'GAMMAL1', 'GAMMAL1 USED IN UPCONTROL', kind='interp', line=578)

# GAMMAL1 = PDL 22D.
W('25,2505', 0o03767, '', '', 'VL', kind='operand', line=581)
W('25,2506', 0o50025, '', 'DSU', 'BMN', 'IF VL-VLMIN NEG, GO TO PREFINAL', kind='interp', line=582)
W('25,2507', 0o15205, '', '', 'VLMIN', kind='operand', line=583)
W('25,2510', 0o53333, '', '', 'PREFINAL', kind='operand', line=584)

W('25,2511', 0o63545, '', 'DLOAD', 'DSQ', kind='interp', line=586)
# Page 857
W('25,2512', 0o03767, '', '', 'VL', kind='operand', line=588)
W('25,2513', 0o17666, '', 'STODL', 'VBARS', 'VBARS / 4 VS VS', kind='interp', line=589)

W('25,2514', 0o15333, '', '', 'HALVE', 'IF VSAT-VL NEG, GO TO CONSTD', kind='operand', line=591)
W('25,2515', 0o50025, '', 'DSU', 'BMN', kind='interp', line=592)
W('25,2516', 0o03767, '', '', 'VL', kind='operand', line=593)
W('25,2517', 0o53226, '', '', 'BECONSTD', 'SET MODE=HUNTEST, CONTINUE IN CONSTD', kind='operand', line=594)
W('25,2520', 0o17662, '', 'STODL', 'DVL', 'DVL / 2VS', kind='interp', line=595)

W('25,2521', 0o15333, '', '', 'HALVE', kind='operand', line=597)
W('25,2522', 0o03672, '', 'STORE', 'VS1', 'VS1 = VSAT', kind='interp', line=598)

W('25,2523', 0o50025, '', 'DSU', 'BMN', 'IF V1 GREATER THAN VSAT, GO ON', kind='interp', line=600)
W('25,2524', 0o00326, '', '', 'V1', kind='operand', line=601)
W('25,2525', 0o52533, '', '', 'GETDHOOK', kind='operand', line=602)
W('25,2526', 0o77621, '', 'BDSU', kind='interp', line=603)
W('25,2527', 0o03662, '', '', 'DVL', kind='operand', line=604)
W('25,2530', 0o17662, '', 'STODL', 'DVL', 'DVL = DVL - (VSAT-V1) = V1 - VL', kind='interp', line=605)
W('25,2531', 0o00326, '', '', 'V1', kind='operand', line=606)
W('25,2532', 0o03672, '', 'STORE', 'VS1', 'VS1 = V1, IN THIS CASE', kind='interp', line=607)

W('25,2533', 0o45145, 'GETDHOOK', 'DLOAD', 'CALL', 'DHOOK=((1-VS1/FACT1) SQ -ALP)/FACT2', kind='interp', line=609)
W('25,2534', 0o03672, '', '', 'VS1', 'VS1 / 2 VS', kind='operand', line=610)
W('25,2535', 0o53004, '', '', 'DHOOKYQ7', 'GO CALC DHOOK', kind='operand', line=611)
W('25,2536', 0o03656, '', 'STORE', 'DHOOK', 'DHOOK / 25G', kind='interp', line=612)

W('25,2537', 0o56261, '', 'SR', 'DDV', kind='interp', line=614)
W('25,2540', 0o20607, '', '', '6', 'CHOOK', kind='operand', line=615)
W('25,2541', 0o03175, '', '', 'Q7', kind='operand', line=616)
W('25,2542', 0o77625, '', 'DSU', kind='interp', line=617)
W('25,2543', 0o15251, '', '', 'CHOOK', '= .25/16 = (-6)', kind='operand', line=618)
W('25,2544', 0o03660, '', 'STORE', 'AHOOKDV', kind='interp', line=619)

W('25,2545', 0o41215, '', 'DAD', 'DMP', 'GAMMAL= GAMMAL1-CH1 DVL SQ(1+AHOOK DVL)', kind='interp', line=621)
W('25,2546', 0o17366, '', '', '1/16TH', kind='operand', line=622)
W('25,2547', 0o15255, '', '', 'CH1', kind='operand', line=623)
W('25,2550', 0o41205, '', 'DMP', 'DMP', kind='interp', line=624)
W('25,2551', 0o03662, '', '', 'DVL', kind='operand', line=625)
W('25,2552', 0o03662, '', '', 'DVL', kind='operand', line=626)
W('25,2553', 0o56271, '', 'DDV', 'DDV', kind='interp', line=627)
W('25,2554', 0o03656, '', '', 'DHOOK', kind='operand', line=628)
W('25,2555', 0o03666, '', '', 'VBARS', kind='operand', line=629)
W('25,2556', 0o50021, '', 'BDSU', 'BMN', kind='interp', line=630)
W('25,2557', 0o00027, '', '', 'GAMMAL1', kind='operand', line=631)
W('25,2560', 0o52751, '', '', 'NEGAMA', kind='operand', line=632)
W('25,2561', 0o03771, 'HUNTEST3', 'STORE', 'GAMMAL', kind='interp', line=633)

W('25,2562', 0o77625, '', 'DSU', '', 'GAMMAL1=GAMMAL1 +Q19 (GAMMAL-GAMMAL1)', kind='interp', line=635)
W('25,2563', 0o00027, '', '', 'GAMMAL1', kind='operand', line=636)
W('25,2564', 0o43205, '', 'DMP', 'DAD', kind='interp', line=637)
# Page 858
W('25,2565', 0o15333, '', '', 'Q19', kind='operand', line=639)
W('25,2566', 0o00027, '', '', 'GAMMAL1', kind='operand', line=640)
W('25,2567', 0o14027, '', 'STODL', 'GAMMAL1', kind='interp', line=641)
W('25,2570', 0o03771, '', '', 'GAMMAL', kind='operand', line=642)

# Page 859
# *START        RANGE PREDICTION ...
# C(MPAC) = GAMMAL
W('25,2571', 0o60516, 'RANGER', 'DSQ', 'SR2', 'COSG = 1-GAMMAL SQ/2, TRUNCATED SERIES', kind='interp', line=647)
W('25,2572', 0o77621, '', 'BDSU', kind='interp', line=648)
W('25,2573', 0o15333, '', '', 'HALVE', kind='operand', line=649)
W('25,2574', 0o17670, '', 'STODL', 'COSG/2', kind='interp', line=650)
W('25,2575', 0o03666, '', '', 'VBARS', 'E=SQRT(1+VBARS........', kind='operand', line=651)

W('25,2576', 0o41225, '', 'DSU', 'DMP', kind='interp', line=653)
W('25,2577', 0o15333, '', '', 'HALVE', kind='operand', line=654)
W('25,2600', 0o03666, '', '', 'VBARS', kind='operand', line=655)
W('25,2601', 0o41205, '', 'DMP', 'DMP', kind='interp', line=656)
W('25,2602', 0o03670, '', '', 'COSG/2', kind='operand', line=657)
W('25,2603', 0o03670, '', '', 'COSG/2', kind='operand', line=658)
W('25,2604', 0o43312, '', 'SL2', 'DAD', kind='interp', line=659)
W('25,2605', 0o17366, '', '', 'C1/16', 'C1/16 = 1/16', kind='operand', line=660)
W('25,2606', 0o65366, '', 'SQRT', 'PDDL', 'E/4 INTO PDL', kind='interp', line=661)

W('25,2607', 0o03666, '', '', 'VBARS', kind='operand', line=663)
W('25,2610', 0o41205, '', 'DMP', 'DMP', 'ASKEP/2 = ARCSIN(VBARS COSG SING/E)', kind='interp', line=664)
W('25,2611', 0o03670, '', '', 'COSG/2', kind='operand', line=665)
W('25,2612', 0o03771, '', '', 'GAMMAL', kind='operand', line=666)
W('25,2613', 0o67471, '', 'DDV', 'ASIN', kind='interp', line=667)
W('25,2614', 0o41552, '', 'SL1', 'PUSH', 'ASKEP TO PDL 0.', kind='interp', line=668)
W('25,2615', 0o17731, '', 'STODL', 'ASKEP', 'BALLISTIC RANGE       ASKEP/2PI', kind='interp', line=669)

# FOR TM, STORE RANGE COMPONENTS OVERLAPPING (SP)
W('25,2616', 0o03767, '', '', 'VL', kind='operand', line=672)
W('25,2617', 0o43205, '', 'DMP', 'DAD', 'ASP1 = Q2 + Q3 VL', kind='interp', line=673)
W('25,2620', 0o15171, '', '', 'Q3', kind='operand', line=674)
W('25,2621', 0o03712, '', '', 'Q2', kind='operand', line=675)
W('25,2622', 0o03732, '', 'STORE', 'ASP1', 'FINAL PHASE RANGE     ASP1/2 PI', kind='interp', line=676)

W('25,2623', 0o63525, '', 'PDDL', 'DSQ', 'ASP1 TO PDL 2.', kind='interp', line=678)
W('25,2624', 0o00326, '', '', 'V1', kind='operand', line=679)
# 2
# ASPUP= -C12 LOG(V1 Q7/VBARS A0)/GAMMAL1
W('25,2625', 0o56205, '', 'DMP', 'DDV', kind='interp', line=682)
W('25,2626', 0o03175, '', '', 'Q7', kind='operand', line=683)
W('25,2627', 0o03666, '', '', 'VBARS', kind='operand', line=684)
W('25,2630', 0o45071, '', 'DDV', 'CALL', kind='interp', line=685)
W('25,2631', 0o00330, '', '', 'A0', kind='operand', line=686)
W('25,2632', 0o46155, '', '', 'LOG', 'RETURN WITH -LOG IN MPAC', kind='operand', line=687)

W('25,2633', 0o56205, '', 'DMP', 'DDV', kind='interp', line=689)
W('25,2634', 0o15207, '', '', 'C12', kind='operand', line=690)
W('25,2635', 0o00027, '', '', 'GAMMAL1', kind='operand', line=691)
W('25,2636', 0o03733, '', 'STORE', 'ASPUP', 'UP PHASE RANGE        ASPUP / 2 PI', kind='interp', line=692)
# Page 860
W('25,2637', 0o41325, '', 'PDDL', 'DMP', 'ASPUP TO PDL 4.', kind='interp', line=694)
W('25,2640', 0o15257, '', '', 'KC3', 'KC3 = -4 VS VS / 2 PI 805 RE', kind='operand', line=695)
# ASPDWN = KC3 RDOT V / A0
W('25,2641', 0o03700, '', '', 'RDOT', kind='operand', line=697)
W('25,2642', 0o56205, '', 'DMP', 'DDV', kind='interp', line=698)
W('25,2643', 0o03674, '', '', 'V', kind='operand', line=699)
W('25,2644', 0o00330, '', '', 'A0', kind='operand', line=700)
W('25,2645', 0o41471, '', 'DDV', 'PUSH', 'ASPDWN TO PDL 6.', kind='interp', line=701)
W('25,2646', 0o03624, '', '', 'LAD', kind='operand', line=702)
W('25,2647', 0o17734, '', 'STODL', 'ASPDWN', 'RANGE TO PULL OUT     ASPDWN /2 PI', kind='interp', line=703)

W('25,2650', 0o15175, '', '', 'Q6', kind='operand', line=705)
W('25,2651', 0o41225, '', 'DSU', 'DMP', 'ASP3 = Q5(Q6-GAMMAL)', kind='interp', line=706)
W('25,2652', 0o03771, '', '', 'GAMMAL', kind='operand', line=707)
W('25,2653', 0o15173, '', '', 'Q5', kind='operand', line=708)
W('25,2654', 0o27735, '', 'STOVL', 'ASP3', 'GAMMA CORRECTION      ASP3/2PI', kind='interp', line=709)

W('25,2655', 0o03731, '', '', 'ASKEP', 'GET HI-WD AND', kind='operand', line=711)
W('25,2656', 0o17126, '', 'STODL', 'ASPS(TM)', "SAVE HI-WORD OF ASP'S FOR TM.", kind='interp', line=712)

W('25,2657', 0o03735, '', '', 'ASP3', kind='operand', line=714)
W('25,2660', 0o43215, '', 'DAD', 'DAD', kind='interp', line=715)
# ASPDWN FROM PDL 6.
# ASPUP FROM PDL 4.
W('25,2661', 0o43215, '', 'DAD', 'DAD', kind='interp', line=718)
# ASP1 FROM PDL 2.
# ASKEP FROM PDL 0.
W('25,2662', 0o41025, '', 'DSU', 'BOVB', 'CLEAR OVFIND.', kind='interp', line=721)
W('25,2663', 0o03702, '', '', 'THETAH', kind='operand', line=722)
W('25,2664', 0o57352, '', '', 'TCDANZIG', kind='operand', line=723)
W('25,2665', 0o03610, '', 'STORE', 'DIFF', 'DIFF = (ASP-THETAH) / 2 PI', kind='interp', line=724)
# ASP=ASKEP+ASP1+ASPUP+ASP3+ASPDWN = TOTAL RANGE

W('25,2666', 0o45246, '', 'ABS', 'DSU', 'IF ABS(THETAH-ASP) -25NM NEG, GO TO UPSY', kind='interp', line=727)
W('25,2667', 0o15223, '', '', '25NM', kind='operand', line=728)
W('25,2670', 0o43040, '', 'BMN', 'BON', kind='interp', line=729)
W('25,2671', 0o53033, '', '', 'GOTOUPSY', kind='operand', line=730)
W('25,2672', 0o03311, '', '', 'HIND', kind='operand', line=731)
W('25,2673', 0o52677, '', '', 'GETDLEWD', kind='operand', line=732)

W('25,2674', 0o51145, '', 'DLOAD', 'BPL', kind='interp', line=734)
W('25,2675', 0o03610, '', '', 'DIFF', kind='operand', line=735)
W('25,2676', 0o53221, '', '', 'DCONSTD', 'EVENTUALLY SETS MODE = HUNTEST.', kind='operand', line=736)
W('25,2677', 0o41345, 'GETDLEWD', 'DLOAD', 'DMP', kind='interp', line=737)
# DLEWD = DLEWD (DIFF/(DIFFOLD-DIFF))
W('25,2700', 0o03642, '', '', 'DLEWD', kind='operand', line=739)
W('25,2701', 0o03610, '', '', 'DIFF', kind='operand', line=740)
W('25,2702', 0o45325, '', 'PDDL', 'DSU', kind='interp', line=741)
W('25,2703', 0o03612, '', '', 'DIFFOLD', kind='operand', line=742)
W('25,2704', 0o03610, '', '', 'DIFF', kind='operand', line=743)
# Page 861
W('25,2705', 0o77665, '', 'BDDV', kind='interp', line=745)
W('25,2706', 0o77626, 'LWDSTORE', 'STADR', kind='interp', line=746)
W('25,2707', 0o74135, '', 'STORE', 'DLEWD', kind='interp', line=747)
W('25,2710', 0o50015, '', 'DAD', 'BMN', 'IF LEWD+DLEWD NEG, DLEWD=-LEWD/2', kind='interp', line=748)
W('25,2711', 0o03725, '', '', 'LEWD', kind='operand', line=749)
W('25,2712', 0o52745, '', '', 'LEWDPTR', kind='operand', line=750)
W('25,2713', 0o77600, '', 'BOV', kind='interp', line=751)
W('25,2714', 0o52741, '', '', 'LEWDOVFL', kind='operand', line=752)
W('25,2715', 0o03725, '', 'STORE', 'LEWD', kind='interp', line=753)

W('25,2716', 0o77776, 'SIDETRAK', 'EXIT', kind='interp', line=755)

W('25,2717', 0o35060, '', 'CA', 'EBENTRY', line=757)
W('25,2720', 0o54003, '', 'TS', 'EBANK', line=758)

W('25,2721', 0o35070, '', 'CA', 'PRIO16', 'DROP GRP 5 RESTART PRIO TO 1 LESS THAN', line=760)
W('25,2722', 0o55064, '', 'TS', 'PHSPRDT5', 'GRP 4.', line=761)

W('25,2723', 0o05412, '', 'TC', 'PHASCHNG', line=763)
W('25,2724', 0o00474, '', 'OCT', '00474', 'RESTART GRP 4 AT PRE-HUNT.', kind='data', line=764)
# FORCE RESTART TO PICK UP IN GRP 4:
# USE PRIO 17 FOR GRP 4 (< SERVICER PRIO)
W('25,2725', 0o35070, '', 'CA', 'PRIO16', 'CONTINUE GRP 5 AT LOWER PRIO THAN EITHER', line=767)
# GRP 4 OR SERVICER.
W('25,2726', 0o05210, '', 'TC', 'PRIOCHNG', line=769)

W('25,2727', 0o33032, '', 'CAF', 'ADENDEXT', 'SIDETRACK NEXT PASS UNTIL THIS ONE DONE.', line=771)
W('25,2730', 0o55645, '', 'TS', 'GOTOADDR', 'ONLY AFTER RESTART IS LEFT AFTER DETOUR.', line=772)

W('25,2731', 0o06006, '', 'TC', 'INTPRET', line=774)

W('25,2732', 0o43145, '', 'DLOAD', 'SET', kind='interp', line=776)
W('25,2733', 0o03610, '', '', 'DIFF', kind='operand', line=777)
W('25,2734', 0o03071, '', '', 'HIND', kind='operand', line=778)
W('25,2735', 0o17612, '', 'STODL', 'DIFFOLD', 'DIFFOLD / 2 PI', kind='interp', line=779)

W('25,2736', 0o15177, '', '', 'Q7F', kind='operand', line=781)
W('25,2737', 0o37175, '', 'STCALL', 'Q7', 'Q7 / 805 FPSS', kind='interp', line=782)
W('25,2740', 0o52373, '', '', 'HUNTEST', '(GO TO)', kind='operand', line=783)

W('25,2741', 0o77745, 'LEWDOVFL', 'DLOAD', kind='interp', line=785)
W('25,2742', 0o17372, '', '', 'NEARONE', kind='operand', line=786)
W('25,2743', 0o37725, '', 'STCALL', 'LEWD', kind='interp', line=787)
W('25,2744', 0o53221, '', '', 'DCONSTD', '(GO TO)  ALSO WILL SET MODE = HUNTEST', kind='operand', line=788)

W('25,2745', 0o70545, 'LEWDPTR', 'DLOAD', 'SR1', kind='interp', line=790)
W('25,2746', 0o03725, '', '', 'LEWD', kind='operand', line=791)
W('25,2747', 0o52076, '', 'DCOMP', 'GOTO', kind='interp', line=792)
W('25,2750', 0o52706, '', '', 'LWDSTORE', kind='operand', line=793)

# Page 862
# NEGAMA IS PART OF HUNTEST ...
W('25,2751', 0o41205, 'NEGAMA', 'DMP', 'DMP', 'ENTER WITH GAMMAL IN MPAC', kind='interp', line=797)
W('25,2752', 0o03767, '', '', 'VL', kind='operand', line=798)
W('25,2753', 0o15147, '', '', '1/3RD', kind='operand', line=799)
W('25,2754', 0o41325, '', 'PDDL', 'DMP', 'PUSH GAMMAL VL/3', kind='interp', line=800)
W('25,2755', 0o03725, '', '', 'LEWD', kind='operand', line=801)
W('25,2756', 0o15147, '', '', '1/3RD', kind='operand', line=802)
W('25,2757', 0o43325, '', 'PDDL', 'DAD', 'PUSH LEWD/3', kind='interp', line=803)
W('25,2760', 0o03660, '', '', 'AHOOKDV', kind='operand', line=804)
W('25,2761', 0o15253, '', '', '1/24TH', kind='operand', line=805)
W('25,2762', 0o41205, '', 'DMP', 'DMP', 'DEL VL = (GAMMAL VL/3)/(LEWD/3-DVL', kind='interp', line=806)
W('25,2763', 0o03662, '', '', 'DVL', '(2/3 + AHOOKDV)(CH1 GS/DHOOK VL))', kind='operand', line=807)
W('25,2764', 0o15255, '', '', 'CH1', kind='operand', line=808)
W('25,2765', 0o56271, '', 'DDV', 'DDV', kind='interp', line=809)
W('25,2766', 0o03656, '', '', 'DHOOK', kind='operand', line=810)
W('25,2767', 0o03767, '', '', 'VL', kind='operand', line=811)
W('25,2770', 0o55221, '', 'BDSU', 'BDDV', kind='interp', line=812)
# LEWD/3
# GAMMAL VL /3
W('25,2771', 0o77615, '', 'DAD', kind='interp', line=815)
W('25,2772', 0o03767, '', '', 'VL', kind='operand', line=816)
W('25,2773', 0o37767, '', 'STCALL', 'VL', 'VL/2 VS', kind='interp', line=817)

W('25,2774', 0o53004, '', '', 'DHOOKYQ7', 'GO CALC Q7', kind='operand', line=819)
# Q7=((1-VL/FACT1)SQ - ALP)/FACT2
W('25,2775', 0o17175, '', 'STODL', 'Q7', 'Q7 / 25G', kind='interp', line=821)

W('25,2776', 0o03767, '', '', 'VL', kind='operand', line=823)
W('25,2777', 0o77716, '', 'DSQ', kind='interp', line=824)
W('25,3000', 0o17666, '', 'STODL', 'VBARS', 'VBARS / 4 VS VS', kind='interp', line=825)

W('25,3001', 0o15335, '', '', '3ZEROS', kind='operand', line=827)
W('25,3002', 0o77650, '', 'GOTO', '', 'SET GAMMAL = 0', kind='interp', line=828)
W('25,3003', 0o52561, '', '', 'HUNTEST3', kind='operand', line=829)

W('25,3004', 0o56342, 'DHOOKYQ7', 'SR1', 'DDV', 'SUBROUTINE TO CALC DHOOK OR Q7)', kind='interp', line=831)
W('25,3005', 0o03616, '', '', 'FACT1', kind='operand', line=832)
W('25,3006', 0o72421, '', 'BDSU', 'SL1', kind='interp', line=833)
W('25,3007', 0o15333, '', '', 'HALVE', kind='operand', line=834)
W('25,3010', 0o45316, '', 'DSQ', 'DSU', kind='interp', line=835)
W('25,3011', 0o03704, '', '', 'ALP', kind='operand', line=836)
W('25,3012', 0o43471, '', 'DDV', 'RVQ', kind='interp', line=837)
W('25,3013', 0o03620, '', '', 'FACT2', kind='operand', line=838)

# Page 863
# COME TO PRE-HUNT WHEN RESTART OCCURS AFTER
# HUNTEST IS SIDE-TRACKED AT SIDETRAK.
# PICK UP IN GROUP 4.

W('25,3014', 0o06006, 'PRE-HUNT', 'TC', 'INTPRET', line=845)
W('25,3015', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=846)
W('25,3016', 0o03271, '', '', 'HIND', 'HIND  99D BIT 6 FLAG 6', kind='operand', line=847)
W('25,3017', 0o53022, '', '', 'FOREHUNT', 'RE-INITIALIZE HUNTEST AFTER RE-START.', kind='operand', line=848)
W('25,3020', 0o77650, '', 'GOTO', kind='interp', line=849)
W('25,3021', 0o52373, '', '', 'HUNTEST', kind='operand', line=850)

W('25,3022', 0o77745, 'FOREHUNT', 'DLOAD', '', 'INITIALIZE HUNTEST.', kind='interp', line=852)
W('25,3023', 0o15335, '', '', '3ZEROS', kind='operand', line=853)
W('25,3024', 0o17612, '', 'STODL', 'DIFFOLD', kind='interp', line=854)
W('25,3025', 0o15157, '', '', 'DLEWD0', kind='operand', line=855)
W('25,3026', 0o17642, '', 'STODL', 'DLEWD', kind='interp', line=856)
W('25,3027', 0o15151, '', '', 'LEWD1', kind='operand', line=857)
W('25,3030', 0o03725, '', 'STORE', 'LEWD', kind='interp', line=858)
W('25,3031', 0o77616, '', 'RVQ', kind='interp', line=859)

W('25,3032', 0o53576, 'ADENDEXT', 'CADR', 'ENDEXIT', kind='data', line=861)

# Page 864
# * START       UP CONTROL ...
# MM = 65
W('25,3033', 0o77634, 'GOTOUPSY', 'RTB', '', 'END OF HUNTEST', kind='interp', line=866)
W('25,3034', 0o54441, '', '', 'P65', 'HUNTEST USE OF GRP4 IS DISABLED BY P65', kind='operand', line=867)
# USE FOR DISPLAY.
# SET MODE = UPCONTRL.
# RETURN FROM P65 DIRECTLY TO UPCONTRL
# VIA THE GOTOADDR AT REFAZE10.

W('25,3035', 0o45345, 'UPCONTRL', 'DLOAD', 'DSU', 'IF D-140 POS, NOSWITCH =1', kind='interp', line=873)
W('25,3036', 0o03640, '', '', 'D', '(SUPPRESS LATERAL SWITCH)', kind='operand', line=874)
W('25,3037', 0o15221, '', '', 'C21', kind='operand', line=875)
W('25,3040', 0o43040, '', 'BMN', 'SET', kind='interp', line=876)
W('25,3041', 0o53043, '', '', '+2', kind='operand', line=877)
W('25,3042', 0o03070, '', '', 'NOSWITCH', kind='operand', line=878)

W('25,3043', 0o45345, '', 'DLOAD', 'DSU', 'IF V-V1 POS, GO TO DOWN CONTROL.', kind='interp', line=880)
W('25,3044', 0o03674, '', '', 'V', kind='operand', line=881)
W('25,3045', 0o00326, '', '', 'V1', kind='operand', line=882)
W('25,3046', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=883)
W('25,3047', 0o53260, '', '', 'DOWNCNTL', kind='operand', line=884)
W('25,3050', 0o03640, '', '', 'D', kind='operand', line=885)
W('25,3051', 0o50025, '', 'DSU', 'BMN', 'IF D- Q7 NEG, GO TO KEP', kind='interp', line=886)
W('25,3052', 0o03175, '', '', 'Q7', kind='operand', line=887)
W('25,3053', 0o53313, '', '', 'KEP', kind='operand', line=888)
W('25,3054', 0o51145, '', 'DLOAD', 'BPL', 'IF RDOT NEG, DO VLTEST', kind='interp', line=889)
W('25,3055', 0o03700, '', '', 'RDOT', kind='operand', line=890)
W('25,3056', 0o53065, '', '', 'CONT1', kind='operand', line=891)

W('25,3057', 0o45345, 'VLTEST', 'DLOAD', 'DSU', 'IF V-VL-C18 NEG,EGSW=1,MODE=PREDICT3', kind='interp', line=893)
W('25,3060', 0o03674, '', '', 'V', kind='operand', line=894)
W('25,3061', 0o03767, '', '', 'VL', kind='operand', line=895)
W('25,3062', 0o50025, '', 'DSU', 'BMN', kind='interp', line=896)
W('25,3063', 0o15165, '', '', 'C18', kind='operand', line=897)
W('25,3064', 0o53333, '', '', 'PREFINAL', kind='operand', line=898)

W('25,3065', 0o77745, 'CONT1', 'DLOAD', '', 'IF D-A0 POS, L/D = LAD, GO TO LIMITL/D', kind='interp', line=900)
W('25,3066', 0o03640, '', '', 'D', kind='operand', line=901)
W('25,3067', 0o50025, '', 'DSU', 'BMN', kind='interp', line=902)
W('25,3070', 0o00330, '', '', 'A0', kind='operand', line=903)
W('25,3071', 0o53075, '', '', 'CONT3', kind='operand', line=904)
W('25,3072', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=905)
W('25,3073', 0o03624, '', '', 'LAD', kind='operand', line=906)
W('25,3074', 0o53525, '', '', 'STOREL/D', kind='operand', line=907)

W('25,3075', 0o41345, 'CONT3', 'DLOAD', 'DMP', 'VREF=FACT1(1-SQRT(FACT2 D + ALP))', kind='interp', line=909)
W('25,3076', 0o03640, '', '', 'D', kind='operand', line=910)
W('25,3077', 0o03620, '', '', 'FACT2', kind='operand', line=911)
# Page 865
W('25,3100', 0o75415, '', 'DAD', 'SQRT', kind='interp', line=913)
W('25,3101', 0o03704, '', '', 'ALP', kind='operand', line=914)
W('25,3102', 0o41221, '', 'BDSU', 'DMP', kind='interp', line=915)
W('25,3103', 0o17372, '', '', 'BARELY1', kind='operand', line=916)
W('25,3104', 0o03616, '', '', 'FACT1', kind='operand', line=917)
W('25,3105', 0o01160, '', 'STORE', 'VREF', 'VREF / 2VS', kind='interp', line=918)

W('25,3106', 0o41221, '', 'BDSU', 'DMP', 'RDOTREF = LEWD(V1-VREF)', kind='interp', line=920)
W('25,3107', 0o00326, '', '', 'V1', kind='operand', line=921)
W('25,3110', 0o03725, '', '', 'LEWD', kind='operand', line=922)
W('25,3111', 0o15156, '', 'STODL', 'RDOTREF', 'RDOTREF / 2VS', kind='interp', line=923)

W('25,3112', 0o03672, '', '', 'VS1', kind='operand', line=925)
W('25,3113', 0o50025, '', 'DSU', 'BMN', 'IF VSAT-VREF NEG, GO TO CONTINU2', kind='interp', line=926)
W('25,3114', 0o01160, '', '', 'VREF', kind='operand', line=927)
W('25,3115', 0o53134, '', '', 'CONTINU2', kind='operand', line=928)

W('25,3116', 0o41406, '', 'PUSH', 'PUSH', 'VS1-VREF  TO PDL TWICE', kind='interp', line=930)
W('25,3117', 0o56205, '', 'DMP', 'DDV', 'RDHOOK=CHI(1+DV AHOOKDV/DVL) DV DV', kind='interp', line=931)
W('25,3120', 0o03660, '', '', 'AHOOKDV', '      /DHOOK VREF', kind='operand', line=932)
W('25,3121', 0o03662, '', '', 'DVL', 'WHERE  DV = (VS1-VREF)', kind='operand', line=933)
W('25,3122', 0o41215, '', 'DAD', 'DMP', kind='interp', line=934)
W('25,3123', 0o17366, '', '', '1/16TH', kind='operand', line=935)
W('25,3124', 0o15255, '', '', 'CH1', kind='operand', line=936)
W('25,3125', 0o41205, '', 'DMP', 'DMP', kind='interp', line=937)
# VS1-VREF  FROM PDL TWICE.
W('25,3126', 0o77671, '', 'DDV', kind='interp', line=939)
W('25,3127', 0o03656, '', '', 'DHOOK', kind='operand', line=940)
W('25,3130', 0o44271, '', 'DDV', 'BDSU', kind='interp', line=941)
W('25,3131', 0o01160, '', '', 'VREF', kind='operand', line=942)
W('25,3132', 0o01156, '', '', 'RDOTREF', 'C(RDOTREF)= LEWD (V1-VREF)', kind='operand', line=943)
W('25,3133', 0o01156, '', 'STORE', 'RDOTREF', 'RDOTREF = RDOTREF - RDHOOK', kind='interp', line=944)

W('25,3134', 0o45345, 'CONTINU2', 'DLOAD', 'DSU', kind='interp', line=946)
W('25,3135', 0o03640, '', '', 'D', kind='operand', line=947)
W('25,3136', 0o15313, '', '', 'Q7MIN', kind='operand', line=948)
W('25,3137', 0o50004, '', 'BOVB', 'BMN', kind='interp', line=949)
W('25,3140', 0o57352, '', '', 'TCDANZIG', 'CLEAR OVFL IND, IF ON.', kind='operand', line=950)
W('25,3141', 0o53152, '', '', 'UPCNTRL3', kind='operand', line=951)
W('25,3142', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=952)
W('25,3143', 0o03664, '', '', 'A1', kind='operand', line=953)
W('25,3144', 0o03175, '', '', 'Q7', kind='operand', line=954)
W('25,3145', 0o45325, '', 'PDDL', 'DSU', kind='interp', line=955)
W('25,3146', 0o03640, '', '', 'D', kind='operand', line=956)
W('25,3147', 0o03175, '', '', 'Q7', kind='operand', line=957)
W('25,3150', 0o45471, '', 'DDV', 'STADR', kind='interp', line=958)
W('25,3151', 0o74163, '', 'STORE', 'FACTOR', 'FACTOR / 25G', kind='interp', line=959)

# Page 866
# SKIPPER
# DELTA L/D=-((RDOT-RDOTREF)F1 KB1+V-VREF)F1 KB2
# WHERE F1 = FACTOR

W('25,3152', 0o77745, 'UPCNTRL3', 'DLOAD', kind='interp', line=966)
W('25,3153', 0o03700, '', '', 'RDOT', kind='operand', line=967)
W('25,3154', 0o41225, '', 'DSU', 'DMP', 'L/D = LEWD', kind='interp', line=968)
W('25,3155', 0o01156, '', '', 'RDOTREF', '-((RDOT-RDOTREF)F1/KB1+V-VREF)F1/KB2', kind='operand', line=969)
W('25,3156', 0o03614, '', '', 'FACTOR', kind='operand', line=970)
W('25,3157', 0o43271, '', 'DDV', 'DAD', kind='interp', line=971)
W('25,3160', 0o15211, '', '', '1/KB1', kind='operand', line=972)
W('25,3161', 0o03674, '', '', 'V', kind='operand', line=973)
W('25,3162', 0o41225, '', 'DSU', 'DMP', kind='interp', line=974)
W('25,3163', 0o01160, '', '', 'VREF', kind='operand', line=975)
W('25,3164', 0o03614, '', '', 'FACTOR', kind='operand', line=976)
W('25,3165', 0o41471, '', 'DDV', 'PUSH', kind='interp', line=977)

W('25,3166', 0o15213, '', '', '-1/KB2', 'DELTA L/D INTO PDL', kind='operand', line=979)
W('25,3167', 0o51400, '', 'BOV', 'ABS', 'NONLINEAR CIRCUIT FOR REDUCING HIGH GAIN', kind='interp', line=980)
W('25,3170', 0o53472, '', '', 'GOMAXL/D', kind='operand', line=981)
W('25,3171', 0o50025, '', 'DSU', 'BMN', kind='interp', line=982)
W('25,3172', 0o15275, '', '', 'PT1/16', kind='operand', line=983)
W('25,3173', 0o53200, '', '', 'NEXT1', kind='operand', line=984)
W('25,3174', 0o43205, '', 'DMP', 'DAD', kind='interp', line=985)
W('25,3175', 0o15153, '', '', 'POINT1', kind='operand', line=986)
W('25,3176', 0o15275, '', '', 'PT1/16', kind='operand', line=987)
W('25,3177', 0o41565, '', 'SIGN', 'PUSH', 'ATTACH SIGN OF PUSH TO MPAC THEN PUSH', kind='interp', line=988)

W('25,3200', 0o42545, 'NEXT1', 'DLOAD', 'SL4', kind='interp', line=990)
# DELTA L/D FROM PDL.

W('25,3201', 0o77615, '', 'DAD', kind='interp', line=993)
W('25,3202', 0o03725, '', '', 'LEWD', kind='operand', line=994)
W('25,3203', 0o41400, 'NEGTESTS', 'BOV', 'PUSH', 'L/D TO PDL FOR USE IN NEGTESTS.', kind='interp', line=995)
W('25,3204', 0o53472, '', '', 'GOMAXL/D', kind='operand', line=996)
W('25,3205', 0o17634, '', 'STODL', 'L/D', kind='interp', line=997)
# IF D-C20 POS, LATSW =0
# AND IF L/D NEG, L/D = 0.
W('25,3206', 0o03640, '', '', 'D', kind='operand', line=1000)
W('25,3207', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1001)
W('25,3210', 0o15217, '', '', 'C20', kind='operand', line=1002)
W('25,3211', 0o53526, '', '', 'LIMITL/D', kind='operand', line=1003)
W('25,3212', 0o71214, '', 'CLEAR', 'DLOAD', kind='interp', line=1004)
W('25,3213', 0o03273, '', '', 'LATSW', '=21D.  ROLL OVER TOP, REGARDLESS.', kind='operand', line=1005)
# L/D FROM PDL.
W('25,3214', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=1007)
W('25,3215', 0o53526, '', '', 'LIMITL/D', kind='operand', line=1008)
W('25,3216', 0o15335, '', '', '3ZEROS', kind='operand', line=1009)
W('25,3217', 0o37634, '', 'STCALL', 'L/D', kind='interp', line=1010)
W('25,3220', 0o53526, '', '', 'LIMITL/D', '(GO TO)', kind='operand', line=1011)

# Page 867
W('25,3221', 0o77745, 'DCONSTD', 'DLOAD', '', 'TWO RANGER ENTRIES TO CONSTD HERE', kind='interp', line=1014)
W('25,3222', 0o03610, '', '', 'DIFF', kind='operand', line=1015)
# SAVE OLD VALUE OF DIFF FOR NEXT PASS.
W('25,3223', 0o17612, '', 'STODL', 'DIFFOLD', 'DIFFOLD / 2 PI', kind='interp', line=1017)

W('25,3224', 0o15177, '', '', 'Q7F', kind='operand', line=1019)
W('25,3225', 0o03175, '', 'STORE', 'Q7', kind='interp', line=1020)

W('25,3226', 0o47131, 'BECONSTD', 'SSP', 'RTB', 'A HUNTEST ENTRY INTO CONSTD.', kind='interp', line=1022)
W('25,3227', 0o03646, '', '', 'GOTOADDR', 'RESET MODE TO HUNTEST', kind='operand', line=1023)
W('25,3230', 0o52373, '', '', 'HUNTEST', kind='operand', line=1024)
W('25,3231', 0o54506, '', '', 'KILLGRP4', 'DEACTIVATE GRP4 FROM HUNTEST.', kind='operand', line=1025)

W('25,3232', 0o77604, 'CONSTD', 'BOVB', kind='interp', line=1027)
W('25,3233', 0o57352, '', '', 'TCDANZIG', 'CLEAR OVF IND IF ON.', kind='operand', line=1028)

W('25,3234', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=1030)
W('25,3235', 0o03654, '', '', 'LEQ', kind='operand', line=1031)
W('25,3236', 0o03706, '', '', 'C/D0', 'C/D0 = -4/D0 B-8', kind='operand', line=1032)
W('25,3237', 0o41325, '', 'PDDL', 'DMP', 'LEQ C/D0 INTO PDL', kind='interp', line=1033)
W('25,3240', 0o15263, '', '', '2HS', '2HS / 4 VS VS', kind='operand', line=1034)
W('25,3241', 0o03710, '', '', 'D0', kind='operand', line=1035)
W('25,3242', 0o43271, '', 'DDV', 'DAD', 'RDOTREF = -2 HS D0/V', kind='interp', line=1036)
W('25,3243', 0o03674, '', '', 'V', kind='operand', line=1037)
W('25,3244', 0o03700, '', '', 'RDOT', kind='operand', line=1038)
W('25,3245', 0o43205, '', 'DMP', 'DAD', kind='interp', line=1039)
W('25,3246', 0o15227, '', '', 'K2D', 'C/D0 LEQ + K2D(RDOT-RDOTREF) INTO PD', kind='operand', line=1040)
W('25,3247', 0o77725, '', 'PDDL', kind='interp', line=1041)
W('25,3250', 0o03710, '', '', 'D0', 'D0 /805', kind='operand', line=1042)

W('25,3251', 0o77621, 'CONSTD1', 'BDSU', '', 'ENTER WITH DREF IN MPAC', kind='interp', line=1044)
W('25,3252', 0o03640, '', '', 'D', kind='operand', line=1045)
W('25,3253', 0o43205, '', 'DMP', 'DAD', kind='interp', line=1046)
W('25,3254', 0o15225, '', '', 'K1D', 'K2D TERM FROM PUSH', kind='operand', line=1047)
W('25,3255', 0o52061, '', 'SL', 'GOTO', kind='interp', line=1048)
W('25,3256', 0o20211, '', '', '8D', kind='operand', line=1049)
W('25,3257', 0o53203, '', '', 'NEGTESTS', '(GO TO)', kind='operand', line=1050)

W('25,3260', 0o77604, 'DOWNCNTL', 'BOVB', '', 'INITIAL PART OF UPCONTROL.', kind='interp', line=1052)
W('25,3261', 0o57352, '', '', 'TCDANZIG', 'CLEAR OVFIND, IF ON.', kind='operand', line=1053)

W('25,3262', 0o54345, '', 'DLOAD', 'SR', kind='interp', line=1055)
W('25,3263', 0o03624, '', '', 'LAD', kind='operand', line=1056)
W('25,3264', 0o20611, '', '', '8D', kind='operand', line=1057)
W('25,3265', 0o45325, '', 'PDDL', 'DSU', 'RDTR = LAD(V1-V)', kind='interp', line=1058)
W('25,3266', 0o03674, '', '', 'V', kind='operand', line=1059)
W('25,3267', 0o00326, '', '', 'V1', kind='operand', line=1060)
W('25,3270', 0o43205, '', 'DMP', 'DAD', kind='interp', line=1061)
W('25,3271', 0o03624, '', '', 'LAD', kind='operand', line=1062)
# Page 868
W('25,3272', 0o03700, '', '', 'RDOT', kind='operand', line=1064)
W('25,3273', 0o43205, '', 'DMP', 'DAD', kind='interp', line=1065)
W('25,3274', 0o15227, '', '', 'K2D', kind='operand', line=1066)
# PUSH UP LAD.
W('25,3275', 0o45325, '', 'PDDL', 'DSU', 'LAD + K2D(RDOT-RDTR) INTO PD', kind='interp', line=1068)
W('25,3276', 0o00326, '', '', 'V1', kind='operand', line=1069)
W('25,3277', 0o03674, '', '', 'V', kind='operand', line=1070)
W('25,3300', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=1071)
W('25,3301', 0o03624, '', '', 'LAD', kind='operand', line=1072)
W('25,3302', 0o65271, '', 'DDV', 'PDDL', '(V1-V)SQ LAD/(2 C1 HS) INTO PD', kind='interp', line=1073)
W('25,3303', 0o15273, '', '', '2C1HS', kind='operand', line=1074)
W('25,3304', 0o00326, '', '', 'V1', kind='operand', line=1075)
W('25,3305', 0o56316, '', 'DSQ', 'DDV', kind='interp', line=1076)
W('25,3306', 0o03622, '', '', 'VSQUARE', kind='operand', line=1077)
W('25,3307', 0o45265, '', 'BDDV', 'DSU', 'DREF = (V/V1)SQ A0 - PD', kind='interp', line=1078)
W('25,3310', 0o00330, '', '', 'A0', kind='operand', line=1079)
# PUSH UP HERE
W('25,3311', 0o77650, '', 'GOTO', '', 'C(MPAC) = DREF', kind='interp', line=1081)
W('25,3312', 0o53251, '', '', 'CONSTD1', kind='operand', line=1082)

# 2           2
# DREF = (V/V1)  A0 -(V-V1)  LAD/2 C1 HS
# Page 869
# * START       BALLISTIC PHASE ...
# MM = 66       UPCONTRL ENTRY INTO KEP2.
W('25,3313', 0o66234, 'KEP', 'RTB', 'SSP', kind='interp', line=1089)
W('25,3314', 0o54474, '', '', 'P66', 'DISPLAY TRIM GIMBAL ANGLE VALUES.', kind='operand', line=1090)
W('25,3315', 0o03646, '', '', 'GOTOADDR', 'SET GOTOADDR TO KEPLER PHASE.', kind='operand', line=1091)
W('25,3316', 0o53317, '', '', 'KEP2', kind='operand', line=1092)

# KEP2 CAN ALSO BE STARTED UP DIRECTLY FROM INITROLL
# IN P64.  PROGRAM WILL IDLE IN P64 UNTIL D EXCEEDS
# .2 G BEFORE GOING ON TO P67.

W('25,3317', 0o45345, 'KEP2', 'DLOAD', 'DSU', 'IF Q7F+KDMIN -D NEG, GO TO FINAL PHASE.', kind='interp', line=1098)
W('25,3320', 0o15167, '', '', 'Q7FKDMIN', '(Q7F + KDMIN)/805', kind='operand', line=1099)
W('25,3321', 0o03640, '', '', 'D', kind='operand', line=1100)
W('25,3322', 0o72240, '', 'BMN', 'TLOAD', kind='interp', line=1101)
W('25,3323', 0o53333, '', '', 'PREFINAL', kind='operand', line=1102)
# SET ROLLHOLD = ROLLC, IN CASE CMDAPMOD
W('25,3324', 0o03316, '', '', 'ROLLC', '= +1 EVER ENTERED.', kind='operand', line=1104)
W('25,3325', 0o72214, '', 'BON', 'TLOAD', 'IF D > .05G, KEEP PRESENT ROLL COMMAND.', kind='interp', line=1105)
W('25,3326', 0o03314, '', '', '.05GSW', 'IF D < .05G, SET ROLL COMMAND = 0.', kind='operand', line=1106)
W('25,3327', 0o53331, '', '', '+2', kind='operand', line=1107)
W('25,3330', 0o15335, '', '', '3ZEROS', 'SET ROLLC & ROLLHOLD =0.', kind='operand', line=1108)
W('25,3331', 0o37316, '', 'STCALL', 'ROLLC', '(SP ROLLHOLD FOLLOWS DP ROLLC)', kind='interp', line=1109)
W('25,3332', 0o54401, '', '', 'P62.3', 'CALC DESIRED GIMBAL ANGLES AT PRESENT', kind='operand', line=1110)
# RN, VN TO YIELD TRIM ATTITUDE.
# AVAILABLE IN CPHI'S FOR N22.
# Page 870
# START FINAL PHASE ...
# MM = 67
W('25,3333', 0o47131, 'PREFINAL', 'SSP', 'RTB', kind='interp', line=1116)
W('25,3334', 0o03646, '', '', 'GOTOADDR', 'RESTART PROTECT: RESET GOTOADDR IF CAME', kind='operand', line=1117)
W('25,3335', 0o53333, '', '', 'PREFINAL', 'FROM HUNTEST.', kind='operand', line=1118)
W('25,3336', 0o54500, '', '', 'P67', 'DISABLES GRP4.  FINE IF FROM HUNTEST.BUT', kind='operand', line=1119)
# MAY ALSO REMOVE RESTART PROTECTION OF
# N69 (P65).
# ROLLC         XRNGERR         DNRNGERR
# XXX.XX DEG    XXXX.X NM       XXXX.X NM

W('25,3337', 0o66214, '', 'SET', 'SSP', kind='interp', line=1125)
W('25,3340', 0o03067, '', '', 'EGSW', kind='operand', line=1126)
W('25,3341', 0o03646, '', '', 'GOTOADDR', kind='operand', line=1127)
W('25,3342', 0o53343, '', '', 'PREDICT3', kind='operand', line=1128)

W('25,3343', 0o45345, 'PREDICT3', 'DLOAD', 'DSU', 'IF V-VQUIT NEG, STOP STEERING', kind='interp', line=1130)
W('25,3344', 0o03674, '', '', 'V', kind='operand', line=1131)
W('25,3345', 0o15215, '', '', 'VQUIT', kind='operand', line=1132)
W('25,3346', 0o77440, '', 'BMN', 'EXIT', kind='interp', line=1133)
W('25,3347', 0o53613, '', '', 'STEEROFF', kind='operand', line=1134)

W('25,3350', 0o35060, '', 'CA', 'EBENTRY', 'PRECAUTIONARY.', line=1136)
W('25,3351', 0o54003, '', 'TS', 'EBANK', line=1137)

W('25,3352', 0o35771, '', 'CA', 'TWELVE', line=1139)
W('25,3353', 0o55771, 'BACK', 'TS', 'JJ', line=1140)

W('25,3354', 0o41673, '', 'CS', 'V', line=1142)
W('25,3355', 0o51771, '', 'INDEX', 'JJ', line=1143)
W('25,3356', 0o63637, '', 'AD', 'VREFER', 'VREF - V, HIGHEST VREF AT END OF TABLE.', line=1144)
W('25,3357', 0o10000, '', 'CCS', 'A', 'IF VREF-V POS LOOP BACK', line=1145)
W('25,3360', 0o11771, '', 'CCS', 'JJ', 'DECREMENT JJ, JJ CANNOT BE ZERO', line=1146)
W('25,3361', 0o13353, '', 'TCF', 'BACK', line=1147)
W('25,3362', 0o65017, '', 'AD', 'ONE', line=1148)
W('25,3363', 0o55646, '', 'TS', 'TEM1B', 'V-VREF IN TEM1B (MUST BE POSITIVE NUM)', line=1149)

W('25,3364', 0o51771, '', 'INDEX', 'JJ', line=1151)
W('25,3365', 0o43637, '', 'CS', 'VREFER', line=1152)
W('25,3366', 0o51771, '', 'INDEX', 'JJ', line=1153)
W('25,3367', 0o63640, '', 'AD', 'VREFER +1', 'V(K+1) - V(K)                 (POS NUM)', line=1154)
W('25,3370', 0o57646, '', 'XCH', 'TEM1B', line=1155)
W('25,3371', 0o22007, '', 'ZL', line=1156)
W('25,3372', 0o00006, '', 'EXTEND', line=1157)
W('25,3373', 0o11646, '', 'DV', 'TEM1B', line=1158)
W('25,3374', 0o55651, '', 'TS', 'GRAD', 'GRAD = (V-VREF)/(VK+1 - VK)   (POS NUM', line=1159)

W('25,3375', 0o35022, '', 'CAF', 'FIVE', line=1161)

# Page 871
W('25,3376', 0o55650, 'BACK2', 'TS', 'MM', line=1164)
W('25,3377', 0o35025, '', 'CAF', 'THIRTEEN', line=1165)
W('25,3400', 0o27771, '', 'ADS', 'JJ', line=1166)
W('25,3401', 0o50000, '', 'INDEX', 'A', line=1167)
W('25,3402', 0o43637, '', 'CS', 'VREFER', line=1168)
W('25,3403', 0o51771, '', 'INDEX', 'JJ', line=1169)
W('25,3404', 0o63640, '', 'AD', 'VREFER +1', 'X(K+1) - X(K)', line=1170)
W('25,3405', 0o00006, '', 'EXTEND', line=1171)
W('25,3406', 0o71651, '', 'MP', 'GRAD', line=1172)
W('25,3407', 0o51771, '', 'INDEX', 'JJ', line=1173)
W('25,3410', 0o63637, '', 'AD', 'VREFER', line=1174)
W('25,3411', 0o51650, '', 'INDEX', 'MM', line=1175)
W('25,3412', 0o55652, '', 'TS', 'FX', 'FX = AK + GRAD (AK+1 - AK)', line=1176)
W('25,3413', 0o11650, '', 'CCS', 'MM', line=1177)
W('25,3414', 0o13376, '', 'TCF', 'BACK2', line=1178)
W('25,3415', 0o57653, '', 'XCH', 'FX +1', 'ZERO FX +1 AND GET DREFR', line=1179)
W('25,3416', 0o61637, '', 'AD', 'D', line=1180)
W('25,3417', 0o00006, '', 'EXTEND', line=1181)
W('25,3420', 0o71657, '', 'MP', 'FX +5', 'F1', line=1182)
W('25,3421', 0o52155, '', 'DXCH', 'MPAC', 'MPAC = F1(D-DREF)', line=1183)

W('25,3422', 0o00006, '', 'EXTEND', line=1185)
W('25,3423', 0o41700, '', 'DCS', 'RDOT', 'FORM RDOTREF - RDOT', line=1186)
W('25,3424', 0o20001, '', 'DDOUBL', line=1187)
W('25,3425', 0o20001, '', 'DDOUBL', line=1188)
W('25,3426', 0o20001, '', 'DDOUBL', '', 'SCALE UP BY 8 FOR THIS PHASE.', line=1189)
W('25,3427', 0o61655, '', 'AD', 'FX +3', 'RDOTREF', line=1190)
W('25,3430', 0o00006, '', 'EXTEND', line=1191)
W('25,3431', 0o71656, '', 'MP', 'FX +4', 'F2', line=1192)
W('25,3432', 0o61654, '', 'AD', 'FX +2', 'RTOGO', line=1193)
W('25,3433', 0o20155, '', 'DAS', 'MPAC', 'ADD F2(DADV1-DADVR)', line=1194)
W('25,3434', 0o30154, '', 'CA', 'MPAC', line=1195)
W('25,3435', 0o55770, '', 'TS', 'PREDANG', line=1196)
# L/D = LOD + (THETA- PREDANG)/ Y
W('25,3436', 0o06006, '', 'TC', 'INTPRET', line=1198)

W('25,3437', 0o45242, '', 'SR3', 'DSU', kind='interp', line=1200)
W('25,3440', 0o03702, '', '', 'THETAH', kind='operand', line=1201)
W('25,3441', 0o43014, '', 'BON', 'BOFF', kind='interp', line=1202)
W('25,3442', 0o03305, '', '', 'GONEPAST', kind='operand', line=1203)
W('25,3443', 0o53470, '', '', 'GONEGLAD', kind='operand', line=1204)
W('25,3444', 0o03747, '', '', 'GONEBY', kind='operand', line=1205)
W('25,3445', 0o53453, '', '', 'HAVDNRNG', kind='operand', line=1206)
W('25,3446', 0o43145, '', 'DLOAD', 'SET', 'SET GONEPAST IF GONEBY SET & LATCH IN-PLACE', kind='interp', line=1207)
W('25,3447', 0o13773, '', '', 'MAXRNG', 'DISPLAY = 9999.9 IF GONEBY', kind='operand', line=1208)
W('25,3450', 0o03065, '', '', 'GONEPAST', kind='operand', line=1209)
W('25,3451', 0o37716, '', 'STCALL', 'DNRNGERR', kind='interp', line=1210)
W('25,3452', 0o53470, '', '', 'GONEGLAD', kind='operand', line=1211)

W('25,3453', 0o03716, 'HAVDNRNG', 'STORE', 'DNRNGERR', '= (PREDANG - THETA) /360', kind='interp', line=1213)
# Page 872
W('25,3454', 0o77676, '', 'DCOMP', '', 'FALL SHORT IF NEG, OVERSHOOT IF POS', kind='interp', line=1215)
W('25,3455', 0o56204, '', 'BOVB', 'DDV', kind='interp', line=1216)
W('25,3456', 0o57352, '', '', 'TCDANZIG', 'CLEAR OVFIND IF ON.', kind='operand', line=1217)
W('25,3457', 0o03653, '', '', 'FX', 'FX= DRANGE/D L/D = Y', kind='operand', line=1218)
W('25,3460', 0o40061, '', 'SL', 'BOV', kind='interp', line=1219)
W('25,3461', 0o20206, '', '', '5', kind='operand', line=1220)
W('25,3462', 0o53472, '', '', 'GOMAXL/D', kind='operand', line=1221)
W('25,3463', 0o40015, '', 'DAD', 'BOV', kind='interp', line=1222)
W('25,3464', 0o03626, '', '', 'LOD', kind='operand', line=1223)
W('25,3465', 0o53472, '', '', 'GOMAXL/D', kind='operand', line=1224)
W('25,3466', 0o37634, '', 'STCALL', 'L/D', kind='interp', line=1225)
W('25,3467', 0o53476, '', '', 'GLIMITER', '(GO TO)', kind='operand', line=1226)

# GONEGLAD AND GOPOSMAX ENTRY POINTS FOR GLIMITER ...

W('25,3470', 0o77745, 'GONEGLAD', 'DLOAD', '', 'SET L/D = -LAD', kind='interp', line=1230)
W('25,3471', 0o13471, '', '', 'GONEGLAD', '(ANY NEGATIVE NUMBER WILL DO)', kind='operand', line=1231)

W('25,3472', 0o41234, 'GOMAXL/D', 'RTB', 'DMP', 'L/D = LAD SIGN(MPAC)', kind='interp', line=1233)
W('25,3473', 0o45712, '', '', 'SIGNMPAC', kind='operand', line=1234)
W('25,3474', 0o03624, '', '', 'LAD', kind='operand', line=1235)
W('25,3475', 0o03634, '', 'STORE', 'L/D', 'AND FALL INTO GLIMITER SECTION', kind='interp', line=1236)

W('25,3476', 0o45345, 'GLIMITER', 'DLOAD', 'DSU', 'IF GMAX/2-D POS, GO TO LIMITL/D', kind='interp', line=1238)
W('25,3477', 0o15161, '', '', 'GMAX/2', kind='operand', line=1239)
W('25,3500', 0o03640, '', '', 'D', kind='operand', line=1240)
W('25,3501', 0o43244, '', 'BPL', 'DAD', 'IF GMAX  -D NEG, GO TO GOPOSLAD', kind='interp', line=1241)
W('25,3502', 0o53526, '', '', 'LIMITL/D', kind='operand', line=1242)
W('25,3503', 0o15161, '', '', 'GMAX/2', kind='operand', line=1243)
W('25,3504', 0o41240, '', 'BMN', 'DMP', kind='interp', line=1244)
W('25,3505', 0o53523, '', '', 'GOPOSLAD', kind='operand', line=1245)
W('25,3506', 0o15263, '', '', '2HS', kind='operand', line=1246)
W('25,3507', 0o41325, '', 'PDDL', 'DMP', '2HS(GMAX-D) INTO PD', kind='interp', line=1247)
W('25,3510', 0o03654, '', '', 'LEQ', kind='operand', line=1248)
W('25,3511', 0o15333, '', '', '1/GMAX', kind='operand', line=1249)
W('25,3512', 0o41215, '', 'DAD', 'DMP', kind='interp', line=1250)
W('25,3513', 0o03624, '', '', 'LAD', kind='operand', line=1251)
W('25,3514', 0o56325, '', 'PDDL', 'DDV', '2HS(GMAX-D) (LEQ/GMAX+LAD) INTO PD', kind='interp', line=1252)
W('25,3515', 0o15265, '', '', '2HSGMXSQ', kind='operand', line=1253)
W('25,3516', 0o03622, '', '', 'VSQUARE', kind='operand', line=1254)
W('25,3517', 0o75415, '', 'DAD', 'SQRT', 'XLIM = SQRT(PD+(2HSGMAX/V)SQ)', kind='interp', line=1255)
W('25,3520', 0o51015, '', 'DAD', 'BPL', 'IF RDOT+XLIM POS, GO TO LIMITL/D', kind='interp', line=1256)
W('25,3521', 0o03700, '', '', 'RDOT', kind='operand', line=1257)
W('25,3522', 0o53526, '', '', 'LIMITL/D', kind='operand', line=1258)

W('25,3523', 0o77745, 'GOPOSLAD', 'DLOAD', kind='interp', line=1260)
W('25,3524', 0o03624, '', '', 'LAD', kind='operand', line=1261)
W('25,3525', 0o03634, 'STOREL/D', 'STORE', 'L/D', kind='interp', line=1262)

# Page 873
W('25,3526', 0o77745, 'LIMITL/D', 'DLOAD', kind='interp', line=1265)
W('25,3527', 0o03634, '', '', 'L/D', kind='operand', line=1266)
W('25,3530', 0o17636, '', 'STODL', 'L/D1', kind='interp', line=1267)
W('25,3531', 0o03622, '', '', 'VSQUARE', kind='operand', line=1268)

W('25,3532', 0o77614, '', 'BON', '', 'NO LATERAL CONTROL IF PAST TARGET', kind='interp', line=1270)
W('25,3533', 0o03305, '', '', 'GONEPAST', kind='operand', line=1271)
W('25,3534', 0o53566, '', '', 'L355', kind='operand', line=1272)
W('25,3535', 0o43205, '', 'DMP', 'DAD', 'Y= KLAT VSQUARE + LATBIAS', kind='interp', line=1273)
W('25,3536', 0o03632, '', '', 'KLAT', kind='operand', line=1274)
W('25,3537', 0o15243, '', '', 'LATBIAS', 'Y INTO PD', kind='operand', line=1275)
W('25,3540', 0o51525, 'L350', 'PDDL', 'ABS', 'IF ABS(L/D)-L/DCMINR NEG, GO TO L353', kind='interp', line=1276)
W('25,3541', 0o03634, '', '', 'L/D', kind='operand', line=1277)
W('25,3542', 0o50025, '', 'DSU', 'BMN', kind='interp', line=1278)
W('25,3543', 0o03630, '', '', 'L/DCMINR', kind='operand', line=1279)
W('25,3544', 0o53553, '', '', 'L353', kind='operand', line=1280)
W('25,3545', 0o75345, '', 'DLOAD', 'SIGN', 'IF K2ROLL LATANG NEG, GO TO L357', kind='interp', line=1281)
W('25,3546', 0o03676, '', '', 'LATANG', kind='operand', line=1282)
W('25,3547', 0o03644, '', '', 'K2ROLL', kind='operand', line=1283)
W('25,3550', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=1284)
W('25,3551', 0o53632, '', '', 'L357', kind='operand', line=1285)
W('25,3552', 0o41542, '', 'SR1', 'PUSH', 'Y = Y/2', kind='interp', line=1286)
W('25,3553', 0o75345, 'L353', 'DLOAD', 'SIGN', 'IF LATANG SIGN(K2ROLL)-Y POS, SWITCH', kind='interp', line=1287)
W('25,3554', 0o03676, '', '', 'LATANG', kind='operand', line=1288)
W('25,3555', 0o03644, '', '', 'K2ROLL', kind='operand', line=1289)
W('25,3556', 0o77625, '', 'DSU', kind='interp', line=1290)
W('25,3557', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=1291)
W('25,3560', 0o53566, '', '', 'L355', kind='operand', line=1292)
W('25,3561', 0o03644, '', '', 'K2ROLL', kind='operand', line=1293)
W('25,3562', 0o57414, '', 'BONCLR', 'DCOMP', 'IF NOSWITCH =1, K2ROLL= K2ROLL', kind='interp', line=1294)
W('25,3563', 0o03210, '', '', 'NOSWITCH', kind='operand', line=1295)
W('25,3564', 0o53566, '', '', 'L355', kind='operand', line=1296)
W('25,3565', 0o03644, '', 'STORE', 'K2ROLL', 'K2ROLL = -K2ROLL', kind='interp', line=1297)

W('25,3566', 0o56345, 'L355', 'DLOAD', 'DDV', 'ROLLC = ACOS( (L/D1) / LAD)', kind='interp', line=1299)
W('25,3567', 0o03636, '', '', 'L/D1', kind='operand', line=1300)
W('25,3570', 0o03624, '', '', 'LAD', 'MPAC SET TO +-1 IF OVERFLOW***', kind='operand', line=1301)
W('25,3571', 0o65542, '', 'SR1', 'ACOS', kind='interp', line=1302)
W('25,3572', 0o43165, '', 'SIGN', 'CLEAR', kind='interp', line=1303)
W('25,3573', 0o03644, '', '', 'K2ROLL', kind='operand', line=1304)
W('25,3574', 0o03270, '', '', 'NOSWITCH', kind='operand', line=1305)
W('25,3575', 0o03316, '', 'STORE', 'ROLLC', kind='interp', line=1306)

W('25,3576', 0o77776, 'ENDEXIT', 'EXIT', kind='interp', line=1308)

W('25,3577', 0o35003, 'OVERNOUT', 'CA', 'BIT13', 'ENTRYDSP =92D B13', line=1310)
W('25,3600', 0o70102, '', 'MASK', 'CM/FLAGS', line=1311)
W('25,3601', 0o00006, '', 'EXTEND', line=1312)
W('25,3602', 0o13606, '', 'BZF', 'NODISKY', 'OMIT DISPLAY.', line=1313)
# Page 874
W('25,3603', 0o31263, '', 'CA', 'ENTRYVN', 'ALL ENTRY DISPLAYS ARE DONE HERE.', line=1315)
W('25,3604', 0o04662, '', 'TC', 'BANKCALL', line=1316)
W('25,3605', 0o20712, '', 'CADR', 'REGODSPR', 'NO ABORT IF DISKY IN USE', kind='data', line=1317)

W('25,3606', 0o00004, 'NODISKY', 'INHINT', line=1319)
W('25,3607', 0o10067, '', 'CCS', 'NEWJOB', 'PROTECT READACCS GRP 5, IF SIDETRACKED.', line=1320)
W('25,3610', 0o05164, '', 'TC', 'CHANG1', line=1321)
W('25,3611', 0o04701, 'SERVNOUT', 'TC', 'POSTJUMP', '( COME HERE FROM P67.3 )', line=1322)
W('25,3612', 0o77227, '', 'CADR', 'SERVEXIT', 'AND END AVERAGEG JOB VIA  ENDOFJOB.', kind='data', line=1323)

# Page 875
# DISPLAY WHEN V IS LESS THAN VQUIT.

W('25,3613', 0o77776, 'STEEROFF', 'EXIT', kind='interp', line=1328)
W('25,3614', 0o35060, '', 'CA', 'EBENTRY', 'PRECAUTIONARY.', line=1329)
W('25,3615', 0o54003, '', 'TS', 'EBANK', line=1330)

W('25,3616', 0o35070, '', 'CA', 'PRIO16', '2 LESS THAN NTRYPRIO.', line=1332)
W('25,3617', 0o05134, '', 'TC', 'NOVAC', line=1333)
#   EBANK= AOG  # ANY EB HERE
W('25,3620', 0o02512, '', '2CADR', 'P67.1', 'START UP REMAINDER OF P67', kind='data', line=1335)
W('25,3621', 0o54066, kind='data', line=1335)

# RTOGO         LAT             LONG
# XXXX.X NM     XXX.XX DEG      XXX.XX DEG

W('25,3622', 0o05372, '', 'TC', '2PHSCHNG', 'INHINT/RELINT DONE.', line=1340)
W('25,3623', 0o00414, '', 'OCT', '00414', '4.41 RESTART FOR P67.1 DISPLAY JOB.', kind='data', line=1341)
W('25,3624', 0o10035, '', 'OCT', '10035', 'SERVICER 5.3 RESTART.', kind='data', line=1342)

W('25,3625', 0o33631, '', 'CA', 'P67.2CAD', 'HEREAFTER, DO LAT, LONG.', line=1344)
W('25,3626', 0o55645, '', 'TS', 'GOTOADDR', line=1345)

W('25,3627', 0o06006, '', 'TC', 'INTPRET', line=1347)
W('25,3630', 0o77650, '', 'GOTO', kind='interp', line=1348)
W('25,3631', 0o54531, 'P67.2CAD', '', 'P67.2', 'CONTINUE FOR LAT, LONG THIS TIME.', kind='operand', line=1349)

W('25,3632', 0o75345, 'L357', 'DLOAD', 'SIGN', 'L/D = L/DCMINR SIGN(L/D)', kind='interp', line=1351)
W('25,3633', 0o03630, '', '', 'L/DCMINR', kind='operand', line=1352)
W('25,3634', 0o03634, '', '', 'L/D', kind='operand', line=1353)
W('25,3635', 0o37636, '', 'STCALL', 'L/D1', kind='interp', line=1354)
W('25,3636', 0o53566, '', '', 'L355', '(GO TO)', kind='operand', line=1355)

# Page 876
# TABLE USED FOR SUB-ORBITAL REFERENCE TRAJECTORY CONTROL.

W('25,3637', 0o00474, 'VREFER', 'DEC', '.019288', 'REFERENCE VELOCITY SCALED V/51532.3946', kind='data', line=1360)
W('25,3640', 0o01235, '', 'DEC', '.040809', '13 POINTS ARE STORED AS THE INDEPENDENT', kind='data', line=1361)
W('25,3641', 0o02337, '', 'DEC', '.076107', 'VARIABLE AND THEN SIX 13 POINT FUNCTIONS', kind='data', line=1362)
W('25,3642', 0o03721, '', 'DEC', '.122156', 'OF V ARE STORED CONSECUTIVELY', kind='data', line=1363)
W('25,3643', 0o05230, '', 'DEC', '.165546', kind='data', line=1364)
W('25,3644', 0o06213, '', 'DEC', '.196012', kind='data', line=1365)
W('25,3645', 0o10550, '', 'DEC', '.271945', kind='data', line=1366)
W('25,3646', 0o11717, '', 'DEC', '.309533', kind='data', line=1367)
W('25,3647', 0o13314, '', 'DEC', '.356222', kind='data', line=1368)
W('25,3650', 0o14736, '', 'DEC', '.404192', kind='data', line=1369)
W('25,3651', 0o16255, '', 'DEC', '.448067', kind='data', line=1370)
W('25,3652', 0o16457, '', 'DEC', '.456023', kind='data', line=1371)
W('25,3653', 0o25570, '', 'DEC', '.67918', 'HIGHVELOCITY FOR SAFETY.', kind='data', line=1372)

W('25,3654', 0o77526, '', 'DEC', '-.010337', 'DRANGE/DA     SCALED DRDA/(2700/805)', kind='data', line=1374)
W('25,3655', 0o77360, '', 'DEC', '-.016550', kind='data', line=1375)
W('25,3656', 0o77106, '', 'DEC', '-.026935', kind='data', line=1376)
W('25,3657', 0o76516, '', 'DEC', '-.042039', kind='data', line=1377)
W('25,3660', 0o76071, '', 'DEC', '-.058974', kind='data', line=1378)
W('25,3661', 0o75570, '', 'DEC', '-.070721', kind='data', line=1379)
W('25,3662', 0o74661, '', 'DEC', '-.098538', kind='data', line=1380)
W('25,3663', 0o74436, '', 'DEC', '-.107482', kind='data', line=1381)
W('25,3664', 0o73212, '', 'DEC', '-.147762', kind='data', line=1382)
W('25,3665', 0o71640, '', 'DEC', '-.193289', kind='data', line=1383)
W('25,3666', 0o54557, '', 'DEC', '-.602557', kind='data', line=1384)
W('25,3667', 0o40000, '', 'DEC', '-.99999', kind='data', line=1385)
W('25,3670', 0o40000, '', 'DEC', '-.99999', kind='data', line=1386)

W('25,3671', 0o77635, '', 'DEC', '-.0478599 B-3', '-DRANGE/DRDOT', kind='data', line=1388)
W('25,3672', 0o77563, '', 'DEC', '-.0683663 B-3', 'SCALED ((2VS/8 2700) DR/DRDOT)', kind='data', line=1389)
W('25,3673', 0o77354, '', 'DEC', '-.1343468 B-3', kind='data', line=1390)
W('25,3674', 0o76712, '', 'DEC', '-.2759846 B-3', kind='data', line=1391)
W('25,3675', 0o76066, '', 'DEC', '-.4731437 B-3', kind='data', line=1392)
W('25,3676', 0o75322, '', 'DEC', '-.6472087 B-3', kind='data', line=1393)
W('25,3677', 0o73237, '', 'DEC', '-1.171693 B-3', kind='data', line=1394)
W('25,3700', 0o72104, '', 'DEC', '-1.466382 B-3', kind='data', line=1395)
W('25,3701', 0o70301, '', 'DEC', '-1.905171 B-3', kind='data', line=1396)
W('25,3702', 0o65635, '', 'DEC', '-2.547990 B-3', kind='data', line=1397)
W('25,3703', 0o57311, '', 'DEC', '-4.151220 B-3', kind='data', line=1398)
W('25,3704', 0o50575, '', 'DEC', '-5.813617 B-3', kind='data', line=1399)
W('25,3705', 0o50575, '', 'DEC', '-5.813617 B-3', kind='data', line=1400)

# Page 877
W('25,3706', 0o74443, '', 'DEC', '-.0134001 B3', 'RDOTREF       SCALED (8 RDT/2VS)', kind='data', line=1403)
W('25,3707', 0o74333, '', 'DEC', '-.013947 B3', kind='data', line=1404)
W('25,3710', 0o74433, '', 'DEC', '-.013462 B3', kind='data', line=1405)
W('25,3711', 0o74763, '', 'DEC', '-.011813 B3', kind='data', line=1406)
W('25,3712', 0o75432, '', 'DEC', '-.0095631 B3', kind='data', line=1407)
W('25,3713', 0o75735, '', 'DEC', '-.00806946 B3', kind='data', line=1408)
W('25,3714', 0o76200, '', 'DEC', '-.006828 B3', kind='data', line=1409)
W('25,3715', 0o75735, '', 'DEC', '-.00806946 B3', kind='data', line=1410)
W('25,3716', 0o75140, '', 'DEC', '-.0109791 B3', kind='data', line=1411)
W('25,3717', 0o74075, '', 'DEC', '-.0151498 B3', kind='data', line=1412)
W('25,3720', 0o73312, '', 'DEC', '-.0179817 B3', kind='data', line=1413)
W('25,3721', 0o73732, '', 'DEC', '-.0159061 B3', kind='data', line=1414)
W('25,3722', 0o73732, '', 'DEC', '-.0159061 B3', kind='data', line=1415)

W('25,3723', 0o00015, '', 'DEC', '.0008067', 'RANGE TO GO SCALED RTOGO/2700', kind='data', line=1417)
W('25,3724', 0o00066, '', 'DEC', '.0032963', '      8.9', kind='data', line=1418)
W('25,3725', 0o00206, '', 'DEC', '.0081852', '      22.1', kind='data', line=1419)
W('25,3726', 0o00431, '', 'DEC', '.017148', kind='data', line=1420)
W('25,3727', 0o00712, '', 'DEC', '.027926', kind='data', line=1421)
W('25,3730', 0o01136, '', 'DEC', '.037', kind='data', line=1422)
W('25,3731', 0o02015, '', 'DEC', '.063296', kind='data', line=1423)
W('25,3732', 0o02374, '', 'DEC', '.077889', kind='data', line=1424)
W('25,3733', 0o03123, '', 'DEC', '.098815', kind='data', line=1425)
W('25,3734', 0o04051, '', 'DEC', '.127519', kind='data', line=1426)
W('25,3735', 0o05767, '', 'DEC', '.186963', kind='data', line=1427)
W('25,3736', 0o07476, '', 'DEC', '.238148', kind='data', line=1428)
W('25,3737', 0o11324, '', 'DEC', '.294185185', kind='data', line=1429)

W('25,3740', 0o76272, '', 'DEC', '-.051099', '-AREF/805', kind='data', line=1431)
W('25,3741', 0o75472, '', 'DEC', '-.074534', kind='data', line=1432)
W('25,3742', 0o74604, '', 'DEC', '-.101242', kind='data', line=1433)
W('25,3743', 0o74210, '', 'DEC', '-.116646', kind='data', line=1434)
W('25,3744', 0o74052, '', 'DEC', '-.122360', kind='data', line=1435)
W('25,3745', 0o73735, '', 'DEC', '-.127081', kind='data', line=1436)
W('25,3746', 0o73217, '', 'DEC', '-.147453', kind='data', line=1437)
W('25,3747', 0o73013, '', 'DEC', '-.155528', kind='data', line=1438)
W('25,3750', 0o73155, '', 'DEC', '-.149565', kind='data', line=1439)
W('25,3751', 0o74151, '', 'DEC', '-.118509', kind='data', line=1440)
W('25,3752', 0o76703, '', 'DEC', '-.034907', kind='data', line=1441)
W('25,3753', 0o77575, '', 'DEC', '-.007950', kind='data', line=1442)
W('25,3754', 0o77575, '', 'DEC', '-.007950', kind='data', line=1443)

# Page 878
W('25,3755', 0o00112, '', 'DEC', '.004491', 'DRANGE/D L/D SCALED Y/2700', kind='data', line=1446)
W('25,3756', 0o00204, '', 'DEC', '.008081', kind='data', line=1447)
W('25,3757', 0o00407, '', 'DEC', '.016030', kind='data', line=1448)
W('25,3760', 0o01113, '', 'DEC', '.035815', kind='data', line=1449)
W('25,3761', 0o02161, '', 'DEC', '.069422', kind='data', line=1450)
W('25,3762', 0o03260, '', 'DEC', '.104519', kind='data', line=1451)
W('25,3763', 0o03717, '', 'DEC', '.122', kind='data', line=1452)
W('25,3764', 0o05411, '', 'DEC', '.172407', kind='data', line=1453)
W('25,3765', 0o10057, '', 'DEC', '.252852', kind='data', line=1454)
W('25,3766', 0o13476, '', 'DEC', '.363148', kind='data', line=1455)
W('25,3767', 0o20324, '', 'DEC', '.512963', kind='data', line=1456)
W('25,3770', 0o21677, '', 'DEC', '.558519', kind='data', line=1457)
W('25,3771', 0o21677, '', 'DEC', '.558519', 'END OF STORED REFERENCE', kind='data', line=1458)

# Page 879
# REENTRY CONSTANTS.

# DEFINED BY EQUALS

S('DEC15', 'equals', 0o5026, line=1465)
# GAMMAL1        =       22D

W('25,3772', 0o16631, 'MAXRNG', '2OCT', '1663106755', 'DNRNGERR = 9999.9 IF GONEPAST=1', kind='data', line=1468)
W('25,3773', 0o06755, kind='data', line=1468)

#   BANK 26
#   SETLOC REENTRY1
#   BANK

#   COUNT* $$/ENTRY

S('BARELY1', 'equals', 0o67371, line=1476)  # COMMON TO BOTH DISK,DANCE.DEFND IN TFF
# 1BITDP                                 # COMMON TO BOTH DISK AND DANCE. DEFND IN VECPOINT.

W('26,3145', 0o02525, '1/12TH', 'DEC', '.083333', 'DP 1/12 USES HI WORD IN 1/3 BELOW', kind='data', line=1479)
W('26,3146', 0o12525, '1/3RD', '2DEC', '.3333333333', 'DP 1/3', kind='data', line=1480)
W('26,3147', 0o12525, kind='data', line=1480)

S('1/16TH', 'equals', 0o67365, line=1482)

# BELOW:  VS = VSAT = 25766.1973 FT/SEC

# RE = 21,202,900 FEET

W('26,3150', 0o04631, 'LEWD1', '2DEC', '.15', kind='data', line=1488)
W('26,3151', 0o23146, kind='data', line=1488)

W('26,3152', 0o03146, 'POINT1', '2DEC', '.1', kind='data', line=1490)
W('26,3153', 0o14632, kind='data', line=1490)

W('26,3154', 0o06314, 'POINT2', '2DEC', '.2', '.2', kind='data', line=1492)
W('26,3155', 0o31463, kind='data', line=1492)

W('26,3156', 0o76314, 'DLEWD0', '2DEC', '-.05', '-.05', kind='data', line=1494)
W('26,3157', 0o71462, kind='data', line=1494)

W('26,3160', 0o05075, 'GMAX/2', '2DEC', '.16', '8 GS / 2', kind='data', line=1496)
W('26,3161', 0o16051, kind='data', line=1496)

S('3ZEROS', 'equals', 0o65334, line=1498)
W('26,3162', 0o07777, 'NEAR1/4', '2OCT', '0777700000', '1/4 LESS 1 BIT IN UPPER PART.', kind='data', line=1499)
W('26,3163', 0o00000, kind='data', line=1499)

W('26,3164', 0o00236, 'C18', '2DEC', '.0097026346', '500/2VS', kind='data', line=1501)
W('26,3165', 0o36763, kind='data', line=1501)

W('26,3166', 0o00204, 'Q7FKDMIN', '2DEC', '.0080745342', '6.5/805  (Q7F +KDMIN) = 6 + .5)', kind='data', line=1503)
W('26,3167', 0o11303, kind='data', line=1503)

S('C1/16', 'equals', 0o67365, line=1505)

W('26,3170', 0o05260, 'Q3', '2DEC', '.167003132', '.07 2VS/21600', kind='data', line=1507)
W('26,3171', 0o05572, kind='data', line=1507)
# Page 880
W('26,3172', 0o12343, 'Q5', '2DEC', '.326388889', '.3 23500/21600', kind='data', line=1509)
W('26,3173', 0o21616, kind='data', line=1509)

W('26,3174', 0o01073, 'Q6', '2DEC', '.0349', '2 DEG. APPROX 820/23500', kind='data', line=1511)
W('26,3175', 0o31515, kind='data', line=1511)

W('26,3176', 0o00172, 'Q7F', '2DEC', '.0074534161', '6/805  (VALUE OF Q7 IN FIXED MEM.)', kind='data', line=1513)
W('26,3177', 0o03571, kind='data', line=1513)

S('Q19', 'equals', 0o65332, line=1515)  # Q19 = .5

W('26,3200', 0o00573, 'Q21', '2DEC', '.0231481481', '500/21600', kind='data', line=1517)
W('26,3201', 0o10230, kind='data', line=1517)

W('26,3202', 0o76226, 'Q22', '2DEC', '-.053333333', '-1152/21600', kind='data', line=1519)
W('26,3203', 0o45761, kind='data', line=1519)

W('26,3204', 0o13132, 'VLMIN', '2DEC', '.34929485', '18000/2 VS', kind='data', line=1521)
W('26,3205', 0o33062, kind='data', line=1521)

S('VMIN', 'equals', 0o65324, line=1523)  # (VS/2) / 2VS
W('26,3206', 0o00160, 'C12', '2DEC', '.00684572901', '32 28500/(21202900 2 PI)', kind='data', line=1524)
W('26,3207', 0o05104, kind='data', line=1524)

W('26,3210', 0o11322, '1/KB1', '2DEC', '.29411765', '1 / 3.4', kind='data', line=1526)
W('26,3211', 0o32265, kind='data', line=1526)

W('26,3212', 0o75047, '-1/KB2', '2DEC', '-.0057074322 B4', '= -1/(.0034 2 VS) EXP +4', kind='data', line=1528)
W('26,3213', 0o72454, kind='data', line=1528)

W('26,3214', 0o00475, 'VQUIT', '2DEC', '.019405269', '1000 /2VS', kind='data', line=1530)
W('26,3215', 0o35746, kind='data', line=1530)

W('26,3216', 0o06751, 'C20', '2DEC', '.21739130', '(175 FPSS) LIFT UP IF ABOVE C20', kind='data', line=1532)
W('26,3217', 0o27515, kind='data', line=1532)

W('26,3220', 0o05441, 'C21', '2DEC', '.17391304', '140/805', kind='data', line=1534)
W('26,3221', 0o14412, kind='data', line=1534)

W('26,3222', 0o00022, '25NM', '2DEC', '.0011574074', '25/21600      (25 NAUT MILES)', kind='data', line=1536)
W('26,3223', 0o36641, kind='data', line=1536)

W('26,3224', 0o01003, 'K1D', '2DEC', '.0314453125', '=C16 805/256 = .01 805/256', kind='data', line=1538)
W('26,3225', 0o06315, kind='data', line=1538)

W('26,3226', 0o71435, 'K2D', '2DEC', '-.201298418', '-C17 2VS/256 = -.001 2VS/256', kind='data', line=1540)
W('26,3227', 0o75516, kind='data', line=1540)

W('26,3230', 0o32047, 'KVSCALE', '2DEC', '.81491944', '12800/(2 VS .3048)', kind='data', line=1542)
W('26,3231', 0o24367, kind='data', line=1542)

W('26,3232', 0o37200, 'KASCALE', '2DEC', '.97657358', '5.85 16384/(4 .3048 100 805)', kind='data', line=1544)
W('26,3233', 0o05636, kind='data', line=1544)

W('26,3234', 0o00046, 'KTETA', '2DEC*', '.383495203 E2 B-14*', '1000 2PI/16384(163.84)', kind='data', line=1546)
W('26,3235', 0o13137, kind='data', line=1546)

W('26,3236', 0o00017, 'KT1', '2DEC*', '.157788327 E 2', 'RE(2PI)/2 VS(16384) 163.84', kind='data', line=1548)
W('26,3237', 0o30730, kind='data', line=1548)

W('26,3240', 0o00040, '.05G', '2DEC', '.002', '.05/25', kind='data', line=1550)
W('26,3241', 0o30447, kind='data', line=1550)

W('26,3242', 0o00000, 'LATBIAS', '2DEC', '.00003', 'APPRX .5 NM/ 4(21600/2 PI)', kind='data', line=1552)
W('26,3243', 0o17565, kind='data', line=1552)

W('26,3244', 0o01727, 'KWE', '2DEC', '.120056652 B-1', kind='data', line=1554)
W('26,3245', 0o20103, kind='data', line=1554)

W('26,3246', 0o00121, 'KACOS', '2DEC', '.004973592', '1/32(2PI)', kind='data', line=1556)
W('26,3247', 0o17460, kind='data', line=1556)

W('26,3250', 0o00400, 'CHOOK', '2DEC', '1 B-6', '.25/16', kind='data', line=1558)
W('26,3251', 0o00000, kind='data', line=1558)
# Page 881
W('26,3252', 0o01252, '1/24TH', '2DEC', '.0833333333 B-1', kind='data', line=1560)
W('26,3253', 0o25253, kind='data', line=1560)

W('26,3254', 0o24365, 'CH1', '2DEC', '.32 B1', '16 CH1/25 = 16 (1) /25', kind='data', line=1562)
W('26,3255', 0o30244, kind='data', line=1562)

W('26,3256', 0o77152, 'KC3', '2DEC', '-.0247622232', '-(4 VS VS/ 2 PI 805 RE)', kind='data', line=1564)
W('26,3257', 0o51354, kind='data', line=1564)

W('26,3260', 0o00336, 'VRCONT', '2DEC', '.0135836886', '700/2 VSAT', kind='data', line=1566)
W('26,3261', 0o21610, kind='data', line=1566)

S('HALVE', 'equals', 0o65332, line=1568)
S('FOURTH', 'equals', 0o65324, line=1569)

S('1/GMAX', 'equals', 0o65332, line=1571)  # 4/GMAX = 4 / 8
W('26,3262', 0o00433, '2HS', '2DEC', '.0172786611', '2 28500 25 32.2/(4 VS VS)', kind='data', line=1572)
W('26,3263', 0o02775, kind='data', line=1572)

W('26,3264', 0o00000, '2HSGMXSQ', '2DEC', '.0000305717', '(2 28500 8 32.2/ 4 VS VS)SQ', kind='data', line=1574)
W('26,3265', 0o20017, kind='data', line=1574)

W('26,3266', 0o77765, 'C001', '2DEC', '-.000625', '-(4/25)/256   LEQ/D0 CONST', kind='data', line=1576)
W('26,3267', 0o70243, kind='data', line=1576)

W('26,3270', 0o31463, 'POINT8', '2DEC', '.8', kind='data', line=1578)
W('26,3271', 0o06315, kind='data', line=1578)

W('26,3272', 0o00541, '2C1HS', '2DEC', '.0215983264', '2 1.25 28500 805/(2 VS)SQ', kind='data', line=1580)
W('26,3273', 0o33575, kind='data', line=1580)

W('26,3274', 0o00146, 'PT1/16', '2DEC', '.1 B-4', kind='data', line=1582)
W('26,3275', 0o14632, kind='data', line=1582)

W('26,3276', 0o00052, '1/K44', '2DEC', '.00260929464', '2 VS/19749550', kind='data', line=1584)
W('26,3277', 0o30013, kind='data', line=1584)

W('26,3300', 0o20411, 'VFINAL', '2DEC', '.51618016', '26600/2 VS', kind='data', line=1586)
W('26,3301', 0o03041, kind='data', line=1586)

W('26,3302', 0o20610, 'VFINAL1', '2DEC', '.523942273', '= 27000 / 2 VS', kind='data', line=1588)
W('26,3303', 0o10513, kind='data', line=1588)

W('26,3304', 0o11473, '1/KA1', '2DEC', '.30048077', '25/(1.3 64)', kind='data', line=1590)
W('26,3305', 0o02355, kind='data', line=1590)

W('26,3306', 0o00203, 'KA2', '2DEC', '.008', '.2/25', kind='data', line=1592)
W('26,3307', 0o02234, kind='data', line=1592)

W('26,3310', 0o16237, 'KA3', '2DEC', '.44720497', '= 90 4/805', kind='data', line=1594)
W('26,3311', 0o00146, kind='data', line=1594)

W('26,3312', 0o01456, 'KA4', '2DEC', '.049689441', '40/805', kind='data', line=1596)
W('26,3313', 0o03450, kind='data', line=1596)

W('26,3314', 0o01727, 'KALIM', '2DEC', '.06', '1.5/25', kind='data', line=1598)
W('26,3315', 0o01217, kind='data', line=1598)

S('Q7MIN', 'equals', 0o65312, line=1600)  # = 40/805 = .049689441
W('26,3316', 0o56232, '-HSCALED', '2DEC', '-.55305018', '-28500/2 VS', kind='data', line=1601)
W('26,3317', 0o72332, kind='data', line=1601)

W('26,3320', 0o77000, '-KSCALE', '2DEC', '-.0312424837', '-805/VS', kind='data', line=1603)
W('26,3321', 0o43741, kind='data', line=1603)

W('26,3322', 0o36702, 'COS15', '2DEC', '.965', kind='data', line=1605)
W('26,3323', 0o21727, kind='data', line=1605)

S('LATSLOPE', 'equals', 0o65145, line=1607)
# ... END OF RE-ENTRY CONSTANTS ...
