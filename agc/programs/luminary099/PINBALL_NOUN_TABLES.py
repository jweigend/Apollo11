"""PINBALL_NOUN_TABLES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/PINBALL_NOUN_TABLES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 301-319 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('PINBALL_NOUN_TABLES', 'PINBALL_NOUN_TABLES.agc', 'Luminary099', pages='301-319')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     PINBALL_NOUN_TABLES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        301-319
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Luminary131/ file of the same
# name, using Luminary099 page images.
# 2009-06-07 RSB  Corrected two typos.
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

# Page 301
# THE FOLLOWING REFERS TO THE NOUN TABLES
#
# COMPONENT CODE NUMBER         INTERPRETATION
#
# 00000                   1 COMPONENT
# 00001                   2 COMPONENT
# 00010                   3 COMPONENT
# X1XXX                   BIT 4 = 1.  DECIMAL ONLY
# 1XXXX                   BIT 5 = 1.  NO LOAD
# END OF COMPONENT CODE NUMBER
#
# SF ROUTINE CODE NUMBER        INTERPRETATION
#
# 00000                   OCTAL ONLY
# 00001                   STRAIGHT FRACTIONAL
# 00010                   CDU DEGREES (XXX.XX)
# 00011                   ARITHMETIC SF
# 00100                   ARITH DP1       OUT (MULT BY 2EXP14 AT END)     IN (STRAIGHT)
# 00101                   ARITH DP2       OUT (STRAIGHT)                  IN (SL 7 AT END)
# 00110                   LANDING RADAR POSITION (+0000X)
# 00111                   ARITH DP3       OUT (SL 7 AT END)               IN (STRAIGHT)
# 01000                   WHOLE HOURS IN R1, WHOLE MINUES (MOD 60) IN R2,
# SECONDS (MOD 60) 0XX.XX IN R3.  *** ALARMS IF USED WITH OCTAL
# 01001                   MINUTES (MOD 60) IN D1D2, D3 BLANK, SECONDS (MOD 60) IN D4D5
# LIMITS TO 59B59 IF MAG EXCEEDS THIS VALUE.
# ALARMS IF USED WITH OCTAL ******** IN (ALARM)
# 01010                   ARITH DP4       OUT (STRAIGHT)                  IN (SL 3 AT END)
# 01011                   ARITH1 SF       OUT (MULT BY 2EXP14 AT END)     IN (STRAIGHT)
# 01100                   2 INTEGERS IN D1D2, D4D5, D3 BLANK.
# ALARMS IF USED WITH OCTAL ******** IN (ALARM)
# 01101                   360-CDU DEGREES (XXX.XX)
#
# END OF SF ROUTINE CODE NUMBERS

# SF CONSTANT CODE NUMBER       INTERPRETATION
#
# 00000                   WHOLE                           USE ARITH
# 00000                   DP TIME SEC (XXX.XX SEC)        USE ARITHDP1
# 00000                   LR POSITION (+0000X)            USE LR POSITION
# 00001                   SPARE
# 00010                   CDU DEGREES                     USE CDU DEGREES
# 00010                   360-CDU DEGREES                 USE 360-CDU DEGREES
# 00011                   DP DEGREES (90 XX.XXX DEG       USE ARITHDP3
# 00100                   DP DEGREES (360) XXX.XX DEG     USE ARITHDP4
# 00101                   DEGREES (180) XXX.XX DEG        USE ARITH
# 00101                   OPTICAL TRACKER AZIMUTH ANGLE (XXX.XXDEG)
# USE ARITHDP1
# 00110                   WEIGHT2 (XXXXX. LBS)            USE ARITH1
# Page 302
# 00111                   POSITION5 (XXX.XX NAUTICAL MILES)
# USE ARITHDP3
# 01000                   POSITION4 (XXXX.X NAUTICAL MILES)
# USE ARITHDP3
# 01001                   VELOCITY2 (XXXXX. FT/SEC)       USE ARITHDP4
# 01010                   VELOCITY3 (XXXX.X FT/SEC)       USE ARITHDP3
# 01011                   ELEVATION DEGREES (89.999 MAX)  USE ARITH
# 01100                   RENDEZVOUS RADAR RANGE (XXX.XX NAUT MI)
# USE ARITHDP1
# 01101                   RENDEZVOUS RADAR RANGE RATE (XXXXX.FT/SEC)
# USE ARITHDP1
# 01110                   LANDING RADAR ALTITUDE (XXXXX.FEET)
# USE ARITHDP1
# 01111                   INITIAL/FINAL ALTITUDE (XXXXX. FEET)
# USE ARITHDP1
# 10000                   ALTITUDE RATE (XXXXX.FT/SEC)    USE ARITH
# 10001                   FORWARD/LATERAL VELOCITY (XXXXX.FEET/SEC)
# USE ARITH
# 10010                   ROTATIONAL HAND CONTROLLER ANGLE RATES
# XXXXX.DEG/SEC           USE ARITH
# 10011                   LANDING RADAR VELX (XXXXX.FEET/SEC)
# USE ARITHDP1
# 10100                   LANDING RADAR VELY (XXXXX.FEET/SEC)
# USE ARITHDP1
# 10101                   LANDING RADAR VELZ (XXXXX.FEET/SEC)
# USE ARITHDP1
# 10110                   POSITION7 (XXXX.X NAUT MI)      USE ARITHDP4
# 10111                   TRIM DEGREES2 (XXX.XX DEG)      USE ARITH
# 11000                   COMPUTED ALTITUDE (XXXXX. FEET)
# USE ARITHDP1
# 11001                   DP DEGREES (XXXX.X DEG)         USE ARITHDP3
# 11010                   POSITION9 (XXXX.X FT)           USE ARITHDP3
# 11011                   VELOCITY4 (XXXX.X FT/SEC)       USE ARITHDP2
# 11100                   RADIANS (XXX.XXX RADIANS)       USE ARITHDP4
#
# END OF SF CONSTANT CODE NUMBERS

# FOR GREATER THAN SINGLE PRECISION SCALES, PUT ADDRESS OF MAJOR PART INTO
# NOUN TABLES.

# OCTAL LOADS PLACE +0 INTO MAJOR PART, DATA INTO MINOR PART.

# OCTAL DISPLAYS SHOW MINOR PART ONLY.

# TO GET AT BOTH MAJOR AND MINOR PARTS (IN OCTAL), USE NOUN 01.

# A NOUN MAY BE DECLARED :DECIMAL ONLY: BY MAKING BIT4=1 OF ITS COMPONENT
# CODE NUMBER.  IF THIS NOUN IS USED WITH ANY OCTAL DISPLAY VERB, OR IF
# DATA IS LOADED IN OCTAL, IT ALARMS.

# IN LOADING AN :HOURS, MINUTES, SECONDS: NOUN, ALL 3 WORDS MUST BE
# LOADED, OR ALARM.

# Page 303

# ALARM IF AN ATTEMPT IS MADE TO LOAD :SPLIT MINUTES/SECONDS: (MMBSS).
# THIS IS USED FOR DISPLAY ONLY.

# Page 304
# THE FOLLOWING ROUTINES ARE FOR READING THE NOUN TABLES AND THE SF TABLES
# (WHICH ARE IN A SEPARATE BANK FROM THE REST OF PINBALL).  THESE READING
# ROUTINES ARE IN THE SAME BANK AS THE TABLES.  THEY ARE CALLED BY DXCH Z.

# LODNNTAB LOADS NNADTEM WITH THE NNADTAB ENTRY, NNTYPTEM WITH THE
# NNTYPTAB ENTRY.  IF THE NOUN IS MIXED, IDADITEM IS LOADED WITH THE FIRST
# IDADDTAB ENTRY, IDAD2TEM THE SECOND IDADDTAB ENTRY, IDAD3TEM THE THIRD
# IDADDTAB ENTRY, RUTMXTEM WITH THE RUTMXTAB ENTRY.  MIXBR IS SET FOR
# MIXED OR NORMAL NOUN.

#   BANK 6
#   SETLOC PINBALL3
#   BANK
#   COUNT* $$/NOUNS
W('42,2103', 0o52152, 'LODNNTAB', 'DXCH', 'IDAD2TEM', 'SAVE RETURN INFO IN IDAD2TEM, IDAD3TEM.', line=154)
W('42,2104', 0o51002, '', 'INDEX', 'NOUNREG', line=155)
W('42,2105', 0o32154, '', 'CAF', 'NNADTAB', line=156)
W('42,2106', 0o54146, '', 'TS', 'NNADTEM', line=157)
W('42,2107', 0o51002, '', 'INDEX', 'NOUNREG', line=158)
W('42,2110', 0o32320, '', 'CAF', 'NNTYPTAB', line=159)
W('42,2111', 0o54147, '', 'TS', 'NNTYPTEM', line=160)
W('42,2112', 0o41002, '', 'CS', 'NOUNREG', line=161)
W('42,2113', 0o64771, '', 'AD', 'MIXCON', line=162)
W('42,2114', 0o00006, '', 'EXTEND', line=163)
W('42,2115', 0o62121, '', 'BZMF', 'LODMIXNN', 'NOUN NUMBER G/E FIRST MIXED NOUN', line=164)
W('42,2116', 0o34753, '', 'CAF', 'ONE', 'NOUN NUMBER L/ FIRST MIXED NOUN', line=165)
W('42,2117', 0o54140, '', 'TS', 'MIXBR', 'NORMAL.  +1 INTO MIXBR', line=166)
W('42,2120', 0o02137, '', 'TC', 'LODNLV', line=167)
W('42,2121', 0o34752, 'LODMIXNN', 'CAF', 'TWO', 'MIXED.  +2 INTO MIXBR.', line=168)
W('42,2122', 0o54140, '', 'TS', 'MIXBR', line=169)
W('42,2123', 0o51002, '', 'INDEX', 'NOUNREG', line=170)
W('42,2124', 0o33064, '', 'CAF', 'RUTMXTAB -40D', 'FIRST MIXED NOUN = 40.', line=171)
W('42,2125', 0o54153, '', 'TS', 'RUTMXTEM', line=172)
W('42,2126', 0o35012, '', 'CAF', 'LOW10', line=173)
W('42,2127', 0o70146, '', 'MASK', 'NNADTEM', line=174)
W('42,2130', 0o54002, '', 'TS', 'Q', 'TEMP', line=175)
W('42,2131', 0o50000, '', 'INDEX', 'A', line=176)
W('42,2132', 0o32650, '', 'CAF', 'IDADDTAB', line=177)
W('42,2133', 0o54150, '', 'TS', 'IDAD1TEM', 'LOAD IDAD1TEM WITH FIRST IDADDTAB ENTRY', line=178)
W('42,2134', 0o00006, '', 'EXTEND', line=179)
W('42,2135', 0o50002, '', 'INDEX', 'Q', 'LOAD IDAD2TEM WITH 2ND IDADDTAB ENTRY', line=180)
W('42,2136', 0o32652, '', 'DCA', 'IDADDTAB +1', 'LOAD IDAD3TEM WITH 3RD IDADDTAB ENTRY.', line=181)
W('42,2137', 0o52152, 'LODNLV', 'DXCH', 'IDAD2TEM', 'PUT RETURN INFO INTO A, L.', line=182)
W('42,2140', 0o52006, '', 'DXCH', 'Z', line=183)

S('MIXCON', 'equals', 0o4771, line=185)  # (DEC 40)

# GTSFOUT LOADS SFTEMP1, SFTEMP2 WTIH THE DP SFOUTAB ENTRIES.

W('42,2141', 0o52124, 'GTSFOUT', 'DXCH', 'SFTEMP1', '2X(SFCONUM) ARRIVES IN SFTEMP1.', line=189)
# Page 305
W('42,2142', 0o00006, '', 'EXTEND', line=191)
W('42,2143', 0o50000, '', 'INDEX', 'A', line=192)
W('42,2144', 0o32557, '', 'DCA', 'SFOUTAB', line=193)
W('42,2145', 0o52124, 'SFCOM', 'DXCH', 'SFTEMP1', line=194)
W('42,2146', 0o52006, '', 'DXCH', 'Z', line=195)

# GTSFIN LOADS SFTEMP1, SFTEMP2 WITH THE DP SFINTAB INTRIES.

W('42,2147', 0o52124, 'GTSFIN', 'DXCH', 'SFTEMP1', '2X(SFCONUM) ARIVES IN SFTEMP1.', line=199)
W('42,2150', 0o00006, '', 'EXTEND', line=200)
W('42,2151', 0o50000, '', 'INDEX', 'A', line=201)
W('42,2152', 0o32465, '', 'DCA', 'SFINTAB', line=202)
W('42,2153', 0o12145, '', 'TCF', 'SFCOM', line=203)

# NN    NORMAL NOUNS
W('42,2154', 0o00000, 'NNADTAB', 'OCT', '00000', '00    NOT IN USE', kind='data', line=206)
W('42,2155', 0o40000, '', 'OCT', '40000', '01    SPECIFY MACHINE ADDRESS (FRACTIONAL)', kind='data', line=207)
W('42,2156', 0o40000, '', 'OCT', '40000', '02    SPECIFY MACHINE ADDRESS (WHOLE)', kind='data', line=208)
W('42,2157', 0o40000, '', 'OCT', '40000', '03    SPECIFY MACHINE ADDRESS (DEGREES)', kind='data', line=209)
W('42,2160', 0o01045, '', 'ECADR', 'DSPTEM1', '04    ANGULAR ERROR/DIFFERENCE', kind='data', line=210)
W('42,2161', 0o01045, '', 'ECADR', 'DSPTEM1', '05    ANGULAR ERROR/DIFFERENCE', kind='data', line=211)
W('42,2162', 0o01144, '', 'ECADR', 'OPTION1', '06    OPTION CODE', kind='data', line=212)
W('42,2163', 0o01003, '', 'ECADR', 'XREG', '07    ECADR OF WORD TO BE MODIFIED', kind='data', line=213)
# ONES FOR BITS TO BE MODIFIED
# 1 TO SET OR 0 TO RESET SELECTED BITS
W('42,2164', 0o01363, '', 'ECADR', 'ALMCADR', '08    ALARM DATA', kind='data', line=216)
W('42,2165', 0o00375, '', 'ECADR', 'FAILREG', '09    ALARM CODES', kind='data', line=217)
W('42,2166', 0o77776, '', 'OCT', '77776', '10    CHANNEL TO BE SPECIFIED', kind='data', line=218)
W('42,2167', 0o03633, '', 'ECADR', 'TCSI', '11    TIG OF CSI (HRS,MIN,SEC)', kind='data', line=219)
W('42,2170', 0o01051, '', 'ECADR', 'OPTIONX', '12    OPTION CODE', kind='data', line=220)
# (USED BY EXTENDED VERBS ONLY)
W('42,2171', 0o01776, '', 'ECADR', 'TCDH', '13    TIG OF CDH (HRS,MIN,SEC)', kind='data', line=222)
W('42,2172', 0o01051, '', 'ECADR', 'DSPTEMX', '14    CHECKLIST', kind='data', line=223)
# (USED BY EXTENDED VERBS ONLY)
W('42,2173', 0o77777, '', 'OCT', '77777', '15    INCREMENT MACHINE ADDRESS', kind='data', line=225)
W('42,2174', 0o01051, '', 'ECADR', 'DSPTEMX', '16    TIME OF EVENT (HRS,MIN,SEC)', kind='data', line=226)
W('42,2175', 0o00000, '', 'OCT', '00000', '17    SPARE', kind='data', line=227)
W('42,2176', 0o02344, '', 'ECADR', 'FDAIX', '18    AUTO MANEUVER BALL ANGLES', kind='data', line=228)
W('42,2177', 0o00000, '', 'OCT', '00000', '19    SPARE', kind='data', line=229)
W('42,2200', 0o00032, '', 'ECADR', 'CDUX', '20    ICDU ANGLES', kind='data', line=230)
W('42,2201', 0o00037, '', 'ECADR', 'PIPAX', '21    PIPAS', kind='data', line=231)
W('42,2202', 0o00321, '', 'ECADR', 'THETAD', '22    NEW ICDU ANGLES', kind='data', line=232)
W('42,2203', 0o00000, '', 'OCT', '00000', '23    SPARE', kind='data', line=233)
W('42,2204', 0o01051, '', 'ECADR', 'DSPTEM2 +1', '24    DELTA TIME FOR AGC CLOCK (HRS,MIN,SEC)', kind='data', line=234)
W('42,2205', 0o01045, '', 'ECADR', 'DSPTEM1', '25    CHECKLIST', kind='data', line=235)
# (USED WTIH PLEASE PERFORM ONLY)
W('42,2206', 0o01045, '', 'ECADR', 'DSPTEM1', '26    PRIO/DELAY, ADRES, BBCON', kind='data', line=237)
W('42,2207', 0o01362, '', 'ECADR', 'SMODE', '27    SELF TEST ON/OFF SWITCH', kind='data', line=238)
# Page 306
W('42,2210', 0o00000, '', 'OCT', '00000', '28    SPARE', kind='data', line=240)
W('42,2211', 0o00000, '', 'OCT', '00000', '29    SPARE', kind='data', line=241)
W('42,2212', 0o00000, '', 'OCT', '0', '30    SPARE', kind='data', line=242)
W('42,2213', 0o00000, '', 'OCT', '0', '31    SPARE', kind='data', line=243)
W('42,2214', 0o02142, '', 'ECADR', '-TPER', '32    TIME TO PERIGEE (HRS,MIN,SEC)', kind='data', line=244)
W('42,2215', 0o03441, '', 'ECADR', 'TIG', '33    TIME OF IGNITION (HRS,MIN,SEC)', kind='data', line=245)
W('42,2216', 0o01045, '', 'ECADR', 'DSPTEM1', '34    TIME OF EVENT (HRS,MIN,SEC)', kind='data', line=246)
W('42,2217', 0o03453, '', 'ECADR', 'TTOGO', '35    TIME TO GO TO EVENT (HRS,MIN,SEC)', kind='data', line=247)
W('42,2220', 0o00024, '', 'ECADR', 'TIME2', '36    TIME OF AGC CLOCK (HRS,MIN,SEC)', kind='data', line=248)
W('42,2221', 0o03635, '', 'ECADR', 'TTPI', '37    TIG OF TPI (HRS,MIN,SEC)', kind='data', line=249)
W('42,2222', 0o01516, '', 'ECADR', 'TET', '38    TIME OF STATE BEING INTEGRATED', kind='data', line=250)
W('42,2223', 0o00000, '', 'OCT', '00000', '39    SPARE', kind='data', line=251)

# END OF NNADTAB FOR NORMAL NOUNS

# NN    MIXED NOUNS
W('42,2224', 0o64000, '', 'OCT', '64000', '40    TIME TO IGNITION/CUTOFF', kind='data', line=256)
# VG
# DELTA V (ACCUMULATED)
W('42,2225', 0o02003, '', 'OCT', '02003', '41    TARGET  AZIMUTH', kind='data', line=259)
# ELEVATION
W('42,2226', 0o24006, '', 'OCT', '24006', '42    APOGEE', kind='data', line=261)
# PERIGEE
# DELTA V (REQUIRED)
W('42,2227', 0o24011, '', 'OCT', '24011', '43    LATITUDE', kind='data', line=264)
# LONGITUDE
# ALTITUDE
W('42,2230', 0o64014, '', 'OCT', '64014', '44    APOGEE', kind='data', line=267)
# PERIGEE
# TFF
W('42,2231', 0o64017, '', 'OCT', '64017', '45    MARKS', kind='data', line=270)
# TTI OF NEXT BURN
# MGA
W('42,2232', 0o00022, '', 'OCT', '00022', '46    AUTOPILOT CONFIGURATION', kind='data', line=273)
W('42,2233', 0o22025, '', 'OCT', '22025', '47    LEM WEIGHT', kind='data', line=274)
# CSM WEIGHT
W('42,2234', 0o22030, '', 'OCT', '22030', '48    GIMBAL PITCH TRIM', kind='data', line=276)
# GIMBAL ROLL TRIM
W('42,2235', 0o24033, '', 'OCT', '24033', '49    DELTA R', kind='data', line=278)
# DELTA V
# RADAR DATA SOURCE CODE
W('42,2236', 0o00000, '', 'OCT', '0', '50    SPARE', kind='data', line=281)
W('42,2237', 0o22041, '', 'OCT', '22041', '51    S-BAND ANTENNA  PITCH', kind='data', line=282)
# YAW
W('42,2240', 0o00044, '', 'OCT', '00044', '52    CENTRAL ANGLE OF ACTIVE VEHICLE', kind='data', line=284)
W('42,2241', 0o00000, '', 'OCT', '00000', '53    SPARE', kind='data', line=285)
W('42,2242', 0o24052, '', 'OCT', '24052', '54    RANGE', kind='data', line=286)
# RANGE RATE
# THETA
W('42,2243', 0o24055, '', 'OCT', '24055', '55    NO. OF APSIDAL CROSSINGS', kind='data', line=289)
# Page 307
# ELEVATION ANGLE
# CENTRAL ANGLE
W('42,2244', 0o02060, '', 'OCT', '02060', '56    RR LOS  AZIMUTH', kind='data', line=293)
# ELEVATION
W('42,2245', 0o20063, '', 'OCT', '20063', '57    DELTA R', kind='data', line=295)
W('42,2246', 0o24066, '', 'OCT', '24066', '58    PERIGEE ALT', kind='data', line=296)
# DELTA V TPI
# DELTA V TPF
W('42,2247', 0o24071, '', 'OCT', '24071', '59    DELTA VELOCITY LOS', kind='data', line=299)
W('42,2250', 0o24074, '', 'OCT', '24074', '60    HORIZONTAL VELOCITY', kind='data', line=300)
# ALTITUDE RATE
# COMPUTED ALTITUDE
W('42,2251', 0o64077, '', 'OCT', '64077', '61    TIME TO GO IN BRAKING PHASE', kind='data', line=303)
# TIME TO IGNITION
# CROSS RANGE DISTANCE
W('42,2252', 0o64102, '', 'OCT', '64102', '62    ABSOLUTE VALUE OF VELOCITY', kind='data', line=306)
# TIME TO IGNITION
# DELTA V (ACCUMULATED)
W('42,2253', 0o24105, '', 'OCT', '24105', '63    ABSOLUTE VALUE OF VELOCITY', kind='data', line=309)
# ALTITUDE RATE
# COMPUTED ALTITUDE
W('42,2254', 0o64110, '', 'OCT', '64110', '64    TIME LEFT FOR REDESIGNATION -- LPD ANGLE', kind='data', line=312)
# ALTITUDE RATE
# COMPUTED ALTITUDE
W('42,2255', 0o24113, '', 'OCT', '24113', '65    SAMPLED AGC TIME (HRS,MIN,SEC)', kind='data', line=315)
# (FETCHED IN INTERRUPT)
W('42,2256', 0o62116, '', 'OCT', '62116', '66    LR      RANGE', kind='data', line=317)
# POSITION
W('42,2257', 0o04121, '', 'OCT', '04121', '67    LRVX', kind='data', line=319)
# LRVY
# LRVZ
W('42,2260', 0o64124, '', 'OCT', '64124', '68    SLANT RANGE TO LANDING SIGHT', kind='data', line=322)
# TIME TO GO IN BRAKING PHASE
# LR ALTITUDE -- COMPUTED ALTITUDE
W('42,2261', 0o00000, '', 'OCT', '00000', '69    SPARE', kind='data', line=325)
W('42,2262', 0o04132, '', 'OCT', '04132', '70    AOT DETENT CODE/STAR CODE', kind='data', line=326)
W('42,2263', 0o04135, '', 'OCT', '04135', '71    AOT DETENT CODE/STAR CODE', kind='data', line=327)
W('42,2264', 0o02140, '', 'OCT', '02140', '72    RR      360 -- TRUNNION ANGLE', kind='data', line=328)
# SHAFT ANGLE
W('42,2265', 0o02143, '', 'OCT', '02143', '73    NEW RR  360 -- TRUNNION ANGLE', kind='data', line=330)
# SHAFT ANGLE
W('42,2266', 0o64146, '', 'OCT', '64146', '74    TIME TO IGNITION', kind='data', line=332)
# YAWAFTER VEHICLE RISE
# PITCH AFTER VEHICLE RISE
W('42,2267', 0o64151, '', 'OCT', '64151', '75    DELTA ALTITUDE CDH', kind='data', line=335)
# DELTA TIME (CDH-CSI OR TPI-CDH)
# DELTA TIME (TPI-CDH OR TPI-NOMTPI)
W('42,2270', 0o24154, '', 'OCT', '24154', '76    DESIRED HORIZONTAL VELOCITY', kind='data', line=338)
# DESIRED RADIAL VELOCITY
# CROSS-RANGE DISTANCE
# Page 308
W('42,2271', 0o62157, '', 'OCT', '62157', '77    TIME TO ENGINE CUTOFF', kind='data', line=342)
# VELOCITY NORMAL TO CSM PLANE
W('42,2272', 0o02162, '', 'OCT', '02162', '78    RR      RANGE', kind='data', line=344)
# RANGE RATE
W('42,2273', 0o24165, '', 'OCT', '24165', '79    CURSOR ANGLE', kind='data', line=346)
# SPIRAL ANGLE
# POSITION CODE
W('42,2274', 0o02170, '', 'OCT', '02170', '80    DATA INDICATOR', kind='data', line=349)
# OMEGA
W('42,2275', 0o24173, '', 'OCT', '24173', '81    DELTA V (LV)', kind='data', line=351)
W('42,2276', 0o24176, '', 'OCT', '24176', '82    DELTA V (LV)', kind='data', line=352)
W('42,2277', 0o24201, '', 'OCT', '24201', '83    DELTA V (BODY)', kind='data', line=353)
W('42,2300', 0o24204, '', 'OCT', '24204', '84    DELTA V (OTHER VEHICLE)', kind='data', line=354)
W('42,2301', 0o24207, '', 'OCT', '24207', '85    VG (BODY)', kind='data', line=355)
W('42,2302', 0o24212, '', 'OCT', '24212', '86    VG (LV)', kind='data', line=356)
W('42,2303', 0o02215, '', 'OCT', '02215', '87    BACKUP OPTICS LOS       AZIMUTH', kind='data', line=357)
# ELEVATION
W('42,2304', 0o24220, '', 'OCT', '24220', '88    HALF UNIT SUN OR PLANET VECTOR', kind='data', line=359)
W('42,2305', 0o24223, '', 'OCT', '24223', '89    LANDMARK        LATITUDE', kind='data', line=360)
# LONGITUDE/2
# ALTITUDE
W('42,2306', 0o24226, '', 'OCT', '24226', '90    Y', kind='data', line=363)
# Y DOT
# PSI
W('42,2307', 0o04231, '', 'OCT', '04231', '91    ALTITUDE', kind='data', line=366)
# VELOCITY
# FLIGHT PATH ANGLE
W('42,2310', 0o00000, '', 'OCT', '00000', '92    SPARE', kind='data', line=369)
W('42,2311', 0o04237, '', 'OCT', '04237', '93    DELTA GYRO ANGLES', kind='data', line=370)
W('42,2312', 0o00000, '', 'OCT', '00000', '94    SPARE', kind='data', line=371)
W('42,2313', 0o00000, '', 'OCT', '0', '95    SPARE', kind='data', line=372)
W('42,2314', 0o00000, '', 'OCT', '0', '96    SPARE', kind='data', line=373)
W('42,2315', 0o04253, '', 'OCT', '04253', '97    SYSTEM TEST INPUTS', kind='data', line=374)
W('42,2316', 0o04256, '', 'OCT', '04256', '98    SYSTEM TEST RESULTS', kind='data', line=375)
W('42,2317', 0o24261, '', 'OCT', '24261', '99    RMS IN POSITION', kind='data', line=376)
# RMS IN VELOCITY
# RMS IN BIAS

# END OF NNADTAB FOR MIXED NOUNS

# NN    NORMAL NOUNS
W('42,2320', 0o00000, 'NNTYPTAB', 'OCT', '00000', '00    NOT IN USE', kind='data', line=383)
W('42,2321', 0o04040, '', 'OCT', '04040', '01    3COMP FRACTIONAL', kind='data', line=384)
W('42,2322', 0o04140, '', 'OCT', '04140', '02    3COMP WHOLE', kind='data', line=385)
W('42,2323', 0o04102, '', 'OCT', '04102', '03    3COMP CDU DEGREES', kind='data', line=386)
W('42,2324', 0o00504, '', 'OCT', '00504', '04    1COMP DPDEG(360)', kind='data', line=387)
W('42,2325', 0o00504, '', 'OCT', '00504', '05    1COMP DPDEG(360)', kind='data', line=388)
W('42,2326', 0o04000, '', 'OCT', '04000', '06    3COMP OCTAL ONLY', kind='data', line=389)
W('42,2327', 0o04000, '', 'OCT', '04000', '07    3COMP OCTAL ONLY', kind='data', line=390)
W('42,2330', 0o04000, '', 'OCT', '04000', '08    3COMP OCTAL ONLY', kind='data', line=391)
# Page 309
W('42,2331', 0o04000, '', 'OCT', '04000', '09    3COMP OCTAL ONLY', kind='data', line=393)
W('42,2332', 0o00000, '', 'OCT', '00000', '10    1COMP OCTAL ONLY', kind='data', line=394)
W('42,2333', 0o24400, '', 'OCT', '24400', '11    3COMP HMS (DEC ONLY)', kind='data', line=395)
W('42,2334', 0o02000, '', 'OCT', '02000', '12    2COMP OCTAL ONLY', kind='data', line=396)
W('42,2335', 0o24400, '', 'OCT', '24400', '13    3COMP HMS (DEC ONLY)', kind='data', line=397)
W('42,2336', 0o04140, '', 'OCT', '04140', '14    3COMP WHOLE', kind='data', line=398)
W('42,2337', 0o00000, '', 'OCT', '00000', '15    1COMP OCTAL ONLY', kind='data', line=399)
W('42,2340', 0o24400, '', 'OCT', '24400', '16    3COMP HMS (DEC ONLY)', kind='data', line=400)
W('42,2341', 0o00000, '', 'OCT', '0', '17    SPARE', kind='data', line=401)
W('42,2342', 0o04102, '', 'OCT', '04102', '18    3COMP CDU DEG', kind='data', line=402)
W('42,2343', 0o00000, '', 'OCT', '00000', '19    SPARE', kind='data', line=403)
W('42,2344', 0o04102, '', 'OCT', '04102', '20    3COMP CDU DEGREES', kind='data', line=404)
W('42,2345', 0o04140, '', 'OCT', '04140', '21    3COMP WHOLE', kind='data', line=405)
W('42,2346', 0o04102, '', 'OCT', '04102', '22    3COMP CDU DEGREES', kind='data', line=406)
W('42,2347', 0o00000, '', 'OCT', '00000', '23    SPARE', kind='data', line=407)
W('42,2350', 0o24400, '', 'OCT', '24400', '24    3COMP HMS (DEC ONLY)', kind='data', line=408)
W('42,2351', 0o04140, '', 'OCT', '04140', '25    3COMP WHOLE', kind='data', line=409)
W('42,2352', 0o04000, '', 'OCT', '04000', '26    3COMP OCTAL ONLY', kind='data', line=410)
W('42,2353', 0o00140, '', 'OCT', '00140', '27    1COMP WHILE', kind='data', line=411)
W('42,2354', 0o00000, '', 'OCT', '00000', '28    SPARE', kind='data', line=412)
W('42,2355', 0o00000, '', 'OCT', '00000', '29    SPARE', kind='data', line=413)
W('42,2356', 0o00000, '', 'OCT', '0', '30    SPARE', kind='data', line=414)
W('42,2357', 0o00000, '', 'OCT', '0', '31    SPARE', kind='data', line=415)
W('42,2360', 0o24400, '', 'OCT', '24400', '32    3COMP HMS (DEC ONLY)', kind='data', line=416)
W('42,2361', 0o24400, '', 'OCT', '24400', '33    3COMP HMS (DEC ONLY)', kind='data', line=417)
W('42,2362', 0o24400, '', 'OCT', '24400', '34    3COMP HMS (DEC ONLY)', kind='data', line=418)
W('42,2363', 0o24400, '', 'OCT', '24400', '35    3COMP HMS (DEC ONLY)', kind='data', line=419)
W('42,2364', 0o24400, '', 'OCT', '24400', '36    3COMP HMS (DEC ONLY)', kind='data', line=420)
W('42,2365', 0o24400, '', 'OCT', '24400', '37    3COMP HMS (DEC ONLY)', kind='data', line=421)
W('42,2366', 0o24400, '', 'OCT', '24400', '38    3COMP HMS (DEC ONLY)', kind='data', line=422)
W('42,2367', 0o00000, '', 'OCT', '00000', '39    SPARE', kind='data', line=423)

# END OF NNTYPTAB FOR NORMAL NOUNS

# NN    MIXED NOUNS
W('42,2370', 0o24500, '', 'OCT', '24500', '40    3COMP   MIN/SEC, VEL3, VEL3', kind='data', line=428)
# (NO LOAD, DEC ONLY)
W('42,2371', 0o00542, '', 'OCT', '00542', '41    2COMP   CDU DEG, ELEV DEG', kind='data', line=430)
W('42,2372', 0o24410, '', 'OCT', '24410', '42    3COMP   POS4, POS4, VEL3', kind='data', line=431)
# (DEC ONLY)
W('42,2373', 0o20204, '', 'OCT', '20204', '43    3COMP   DPDEG(360), DPDEG(360) POS4', kind='data', line=433)
# (DEC ONLY)
W('42,2374', 0o00410, '', 'OCT', '00410', '44    3COMP   POS4, POS4, MIN/SEC', kind='data', line=435)
# (NO LOAD, DEC ONLY)
W('42,2375', 0o10000, '', 'OCT', '10000', '45    3COMP   WHOLE, MIN/SEC, DPDEG(360)', kind='data', line=437)
# (NO LOAD, DEC ONLY)
W('42,2376', 0o00000, '', 'OCT', '00000', '46    1COMP   OCTAL ONLY', kind='data', line=439)
W('42,2377', 0o00306, '', 'OCT', '00306', '47    2COMP   WEIGHT2 FOR EACH', kind='data', line=440)
# (DEC ONLY)
W('42,2400', 0o01367, '', 'OCT', '01367', '48    2COMP   TRIM DEG2 FOR EACH', kind='data', line=442)
# Page 310
# (DEC ONLY)
W('42,2401', 0o00510, '', 'OCT', '00510', '49    3COMP   POS4, VEL3, WHOLE', kind='data', line=445)
# (DEC ONLY)
W('42,2402', 0o00000, '', 'OCT', '0', '50    SPARE', kind='data', line=447)
W('42,2403', 0o00204, '', 'OCT', '00204', '51    2COMP   DPDEG(360), DPDEG(360)', kind='data', line=448)
# (DEC ONLY)
W('42,2404', 0o00004, '', 'OCT', '00004', '52    1COMP   DPDEG(360)', kind='data', line=450)
W('42,2405', 0o00000, '', 'OCT', '00000', '53    SPARE', kind='data', line=451)
W('42,2406', 0o10507, '', 'OCT', '10507', '54    3COMP   POS5, VEL3, DPDEG(360)', kind='data', line=452)
# (DEC ONLY)
W('42,2407', 0o10200, '', 'OCT', '10200', '55    3COMP   WHOLE, DPDEG(360), DPDEG(360)', kind='data', line=454)
# (DEC ONLY)
W('42,2410', 0o00204, '', 'OCT', '00204', '56    2COMP   DPDEG(360), DPDEG(360)', kind='data', line=456)
W('42,2411', 0o00010, '', 'OCT', '00010', '57    1COMP   POS4', kind='data', line=457)
# (DEC ONLY)
W('42,2412', 0o24510, '', 'OCT', '24510', '58    3COMP   POS4, VEL3, VEL3', kind='data', line=459)
# (DEC ONLY)
W('42,2413', 0o24512, '', 'OCT', '24512', '59    3COMP   VEL3 FOR EACH', kind='data', line=461)
# (DEC ONLY)
W('42,2414', 0o60512, '', 'OCT', '60512', '60    3COMP   VEL3, VEL3, COMP ALT', kind='data', line=463)
# (DEC ONLY)
W('42,2415', 0o54000, '', 'OCT', '54000', '61    3COMP   MIN/SEC, MIN/SEC, POS7', kind='data', line=465)
# (NO LOAD, DEC ONLY)
W('42,2416', 0o24012, '', 'OCT', '24012', '62    3COMP   VEL3, MIN/SEC, VEL3', kind='data', line=467)
# (NO LOAD, DEC ONLY)
W('42,2417', 0o60512, '', 'OCT', '60512', '63    3COMP   VEL3, VEL3, COMP ALT', kind='data', line=469)
# (DEC ONLY)
W('42,2420', 0o60500, '', 'OCT', '60500', '64    3COMP   2INT, VEL3, COMP ALT', kind='data', line=471)
# (NO LOAD, DEC ONLY)
W('42,2421', 0o00000, '', 'OCT', '00000', '65    3COMP   HMS (DEC ONLY)', kind='data', line=473)
W('42,2422', 0o00016, '', 'OCT', '00016', '66    2COMP   LANDING RADAR ALT, POSITION', kind='data', line=474)
# (NO LOAD, DEC ONLY)
W('42,2423', 0o53223, '', 'OCT', '53223', '67    3COMP   LANDING RADAR VELX, Y, Z', kind='data', line=476)
W('42,2424', 0o60026, '', 'OCT', '60026', '68    3COMP   POS7, MIN/SEC, COMP ALT', kind='data', line=477)
# (NO LOAD, DEC ONLY)
W('42,2425', 0o00000, '', 'OCT', '00000', '69    SPARE', kind='data', line=479)
W('42,2426', 0o00000, '', 'OCT', '0', '70    3COMP   OCTAL ONLY FOR EACH', kind='data', line=480)
W('42,2427', 0o00000, '', 'OCT', '0', '71    3COMP   OCTAL ONLY FOR EACH', kind='data', line=481)
W('42,2430', 0o00102, '', 'OCT', '00102', '72    2COMP   360-CDU DEG, CDU DEG', kind='data', line=482)
W('42,2431', 0o00102, '', 'OCT', '00102', '73    2COMP   360-CDU DEG, CDU DEG', kind='data', line=483)
W('42,2432', 0o10200, '', 'OCT', '10200', '74    3COMP   MIN/SEC, DPDEG(360), DPDEG(360)', kind='data', line=484)
# (NO LOAD, DEC ONLY)
W('42,2433', 0o00010, '', 'OCT', '00010', '75    3COMP   POS4, MIN/SEC, MIN/SEC', kind='data', line=486)
# (NO LOAD, DEC ONLY)

W('42,2434', 0o20512, '', 'OCT', '20512', '76    3COMP   VEL3, VEL3, POS4', kind='data', line=489)
# (DEC ONLY)
W('42,2435', 0o00500, '', 'OCT', '00500', '77    2COMP   MIN/SEC, VEL3', kind='data', line=491)
# (NO LOAD, DEC ONLY)
W('42,2436', 0o00654, '', 'OCT', '00654', '78    2 COMP  RR RANGE, RR RANGE RATE', kind='data', line=493)
W('42,2437', 0o00102, '', 'OCT', '00102', '79    3COMP   CDU DEG, CDU DEG, WHOLE', kind='data', line=494)
# Page 311
# (DEC ONLY)
W('42,2440', 0o00200, '', 'OCT', '00200', '80    2COMP   WHOLE, DPDEG(360)', kind='data', line=497)
W('42,2441', 0o24512, '', 'OCT', '24512', '81    3COMP   VEL3 FOR EACH', kind='data', line=498)
# (DEC ONLY)
W('42,2442', 0o24512, '', 'OCT', '24512', '82    3COMP   VEL3 FOR EACH', kind='data', line=500)
# (DEC ONLY)
W('42,2443', 0o24512, '', 'OCT', '24512', '83    3COMP   VEL3 FOR EACH', kind='data', line=502)
# (DEC ONLY)
W('42,2444', 0o24512, '', 'OCT', '24512', '84    3COMP   VEL3 FOR EACH', kind='data', line=504)
# (DEC ONLY)
W('42,2445', 0o24512, '', 'OCT', '24512', '85    3COMP   VEL3 FOR EACH', kind='data', line=506)
# (DEC ONLY)
W('42,2446', 0o24512, '', 'OCT', '24512', '86    3COMP   VEL3 FOR EACH', kind='data', line=508)
# (DEC ONLY)
W('42,2447', 0o00102, '', 'OCT', '00102', '87    2COMP   CDU DEG FOR EACH', kind='data', line=510)
W('42,2450', 0o00000, '', 'OCT', '0', '88    3COMP   FRAC FOR EACH', kind='data', line=511)
# (DEC ONLY)
W('42,2451', 0o16143, '', 'OCT', '16143', '89    3COMP   DPDEG(90), DPDEG(90), POS5', kind='data', line=513)
# (DEC ONLY)
W('42,2452', 0o10507, '', 'OCT', '10507', '90    3COMP   POS5, VEL3, DEPDEG(360)', kind='data', line=515)
# (DEC ONLY)
W('42,2453', 0o10450, '', 'OCT', '10450', '91    3COMP   POS4, VEL2, DPDEG(360)', kind='data', line=517)
W('42,2454', 0o00000, '', 'OCT', '00000', '92    SPARE', kind='data', line=518)
W('42,2455', 0o06143, '', 'OCT', '06143', '93    3COMP   DPDEG(90) FOR EACH', kind='data', line=519)
W('42,2456', 0o00000, '', 'OCT', '00000', '94    SPARE', kind='data', line=520)
W('42,2457', 0o00000, '', 'OCT', '0', '95    SPARE', kind='data', line=521)
W('42,2460', 0o00000, '', 'OCT', '0', '96    SPARE', kind='data', line=522)
W('42,2461', 0o00000, '', 'OCT', '00000', '97    3COMP   WHOLE FOR EACH', kind='data', line=523)
W('42,2462', 0o00000, '', 'OCT', '00000', '98    3COMP   WHOLE, FRAC, WHOLE', kind='data', line=524)
W('42,2463', 0o71572, '', 'OCT', '71572', '99    3COMP   POS9, VEL4, RADIANS', kind='data', line=525)
# (DEC ONLY)

# END OF NNTYPTAB FOR MIXED NOUNS

W('42,2464', 0o00006, 'SFINTAB', 'OCT', '00006', 'WHOLE, DP TIME (SEC)', kind='data', line=530)
W('42,2465', 0o03240, '', 'OCT', '03240', kind='data', line=531)
W('42,2466', 0o00000, '', 'OCT', '00000', 'SPARE', kind='data', line=532)
W('42,2467', 0o00000, '', 'OCT', '00000', kind='data', line=533)
W('42,2470', 0o00000, '', 'OCT', '00000', 'CDU DEGREES, 360-CDU DEGREES', kind='data', line=534)
W('42,2471', 0o00000, '', 'OCT', '00000', '      (SFCONS IN DEGINSF)', kind='data', line=535)
W('42,2472', 0o10707, '', 'OCT', '10707', 'DP DEGREES (90)', kind='data', line=536)
W('42,2473', 0o03435, '', 'OCT', '03435', '      UPPED BY 1', kind='data', line=537)
W('42,2474', 0o13070, '', 'OCT', '13070', 'DP DEGREES (360) (POINT BETWN BITS 11-12)', kind='data', line=538)
W('42,2475', 0o34345, '', 'OCT', '34345', '      UPPED BY 1', kind='data', line=539)
W('42,2476', 0o00005, '', 'OCT', '00005', 'DEGREES (180)', kind='data', line=540)
W('42,2477', 0o21616, '', 'OCT', '21616', kind='data', line=541)
W('42,2500', 0o26113, '', 'OCT', '26113', 'WEIGHT2', kind='data', line=542)
W('42,2501', 0o31713, '', 'OCT', '31713', kind='data', line=543)
W('42,2502', 0o00070, '', 'OCT', '00070', 'POSITION5', kind='data', line=544)
W('42,2503', 0o20460, '', 'OCT', '20460', kind='data', line=545)
# Page 312
W('42,2504', 0o01065, '', 'OCT', '01065', 'POSITION4', kind='data', line=547)
W('42,2505', 0o05740, '', 'OCT', '05740', kind='data', line=548)
W('42,2506', 0o11414, '', 'OCT', '11414', 'VELOCITY2     (POINT BETWN BITS 11-12)', kind='data', line=549)
W('42,2507', 0o31463, '', 'OCT', '31463', kind='data', line=550)
W('42,2510', 0o07475, '', 'OCT', '07475', 'VELOCITY3', kind='data', line=551)
W('42,2511', 0o16051, '', 'OCT', '16051', kind='data', line=552)
W('42,2512', 0o00001, '', 'OCT', '00001', 'ELEVATION DEGREES', kind='data', line=553)
W('42,2513', 0o03434, '', 'OCT', '03434', kind='data', line=554)
W('42,2514', 0o00047, '', 'OCT', '00047', 'RENDEZVOUS RADAR RANGE', kind='data', line=555)
W('42,2515', 0o21135, '', 'OCT', '21135', kind='data', line=556)
W('42,2516', 0o77766, '', 'OCT', '77766', 'RENDESVOUS RADAR RANGE RATE', kind='data', line=557)
W('42,2517', 0o50711, '', 'OCT', '50711', kind='data', line=558)
W('42,2520', 0o00005, '', '2DEC*', '.9267840599 E5 B-28*', 'LANDING RADAR ALTITUDE', kind='data', line=559)
W('42,2521', 0o25006, kind='data', line=559)

W('42,2522', 0o00002, '', 'OCT', '00002', 'INITIAL/FINAL ALTITUDE', kind='data', line=561)
W('42,2523', 0o23224, '', 'OCT', '23224', kind='data', line=562)
W('42,2524', 0o00014, '', 'OCT', '00014', 'ALTITUDE RATE', kind='data', line=563)
W('42,2525', 0o06500, '', 'OCT', '06500', kind='data', line=564)
W('42,2526', 0o00012, '', 'OCT', '00012', 'FORWARD/LATERAL VELOCITY', kind='data', line=565)
W('42,2527', 0o36455, '', 'OCT', '36455', kind='data', line=566)
W('42,2530', 0o04256, '', 'OCT', '04256', 'ROT HAND CONT ANGLE RATE', kind='data', line=567)
W('42,2531', 0o07071, '', 'OCT', '07071', kind='data', line=568)
W('42,2532', 0o77766, '', '2DEC*', '-1.552795030 E5 B-28*', 'LANDING RADAR VELX', kind='data', line=569)
W('42,2533', 0o60557, kind='data', line=569)

W('42,2534', 0o00005, '', '2DEC*', '.8250825087 E5 B-28*', 'LANDING RADAR VELY', kind='data', line=571)
W('42,2535', 0o01114, kind='data', line=571)

W('42,2536', 0o00007, '', '2DEC*', '1.153668673 E5 B-28*', 'LANDING RADAR VELZ', kind='data', line=573)
W('42,2537', 0o01247, kind='data', line=573)

W('42,2540', 0o04324, '', 'OCT', '04324', 'POSITION7', kind='data', line=575)
W('42,2541', 0o27600, '', 'OCT', '27600', kind='data', line=576)
W('42,2542', 0o00036, '', 'OCT', '00036', 'TRIM DEGREES2', kind='data', line=577)
W('42,2543', 0o20440, '', 'OCT', '20440', kind='data', line=578)
W('42,2544', 0o00035, '', 'OCT', '00035', 'COMPUTED ALTITUDE', kind='data', line=579)
W('42,2545', 0o30400, '', 'OCT', '30400', kind='data', line=580)
W('42,2546', 0o23420, '', 'OCT', '23420', 'DP DEGREES', kind='data', line=581)
W('42,2547', 0o00000, '', 'OCT', '00000', kind='data', line=582)
W('42,2550', 0o01670, '', '2DEC', '30480 B-19', 'POSITION 9', kind='data', line=583)
W('42,2551', 0o20000, kind='data', line=583)

W('42,2552', 0o07475, '', '2DEC', '30.48 B-7', 'VELOCITY4', kind='data', line=585)
W('42,2553', 0o16051, kind='data', line=585)

W('42,2554', 0o14400, '', '2DEC', '100 B-8', 'RADIANS', kind='data', line=587)
W('42,2555', 0o00000, kind='data', line=587)

# END OF SFINTAB

W('42,2556', 0o05174, 'SFOUTAB', 'OCT', '05174', 'WHOLE, DP TIME (SEC)', kind='data', line=591)
W('42,2557', 0o13261, '', 'OCT', '13261', kind='data', line=592)
W('42,2560', 0o00000, '', 'OCT', '00000', 'SPARE', kind='data', line=593)
W('42,2561', 0o00000, '', 'OCT', '00000', kind='data', line=594)
W('42,2562', 0o00000, '', 'OCT', '00000', 'CDU DEGREES, 360-CDU DEGREES', kind='data', line=595)
# Page 313
W('42,2563', 0o00000, '', 'OCT', '00000', '      (SFCONS IN DEGOUTSF, 360 CDUO)', kind='data', line=597)
W('42,2564', 0o00714, '', 'OCT', '00714', 'DP DEGREES (90) (POINT BETWN BITS 7-8)', kind='data', line=598)
W('42,2565', 0o31463, '', 'OCT', '31463', kind='data', line=599)
W('42,2566', 0o13412, '', 'OCT', '13412', 'DP DEGREES (360)', kind='data', line=600)
W('42,2567', 0o07534, '', 'OCT', '07534', kind='data', line=601)
W('42,2570', 0o05605, '', 'OCT', '05605', 'DEGREES (180)', kind='data', line=602)
W('42,2571', 0o03656, '', 'OCT', '03656', kind='data', line=603)
W('42,2572', 0o00001, '', 'OCT', '00001', 'WEIGHT2', kind='data', line=604)
W('42,2573', 0o16170, '', 'OCT', '16170', kind='data', line=605)
W('42,2574', 0o00441, '', 'OCT', '00441', 'POSITION5', kind='data', line=606)
W('42,2575', 0o34306, '', 'OCT', '34306', kind='data', line=607)
W('42,2576', 0o07176, '', 'OCT', '07176', 'POSITION4     (POINT BETWN BITS 7-8)', kind='data', line=608)
W('42,2577', 0o21603, '', 'OCT', '21603', kind='data', line=609)
W('42,2600', 0o15340, '', 'OCT', '15340', 'VELOCITY2', kind='data', line=610)
W('42,2601', 0o15340, '', 'OCT', '15340', kind='data', line=611)
W('42,2602', 0o01031, '', 'OCT', '01031', 'VELOCITY3     (POINT BETWN BITS 7-8)', kind='data', line=612)
W('42,2603', 0o21032, '', 'OCT', '21032', kind='data', line=613)
W('42,2604', 0o34631, '', 'OCT', '34631', 'ELEVATION DETREES', kind='data', line=614)
W('42,2605', 0o23146, '', 'OCT', '23146', kind='data', line=615)
W('42,2606', 0o00636, '', 'OCT', '00636', 'RENDEZVOUS RADAR RANGE', kind='data', line=616)
W('42,2607', 0o14552, '', 'OCT', '14552', kind='data', line=617)
W('42,2610', 0o74552, '', 'OCT', '74552', 'RENDEZVOUS RADAR RANGE RATE', kind='data', line=618)
W('42,2611', 0o70307, '', 'OCT', '70307', kind='data', line=619)
W('42,2612', 0o05520, '', '2DEC', '1.079 E-5 B14', 'LANDING RADAR ALTITUDE', kind='data', line=620)
W('42,2613', 0o15312, kind='data', line=620)

W('42,2614', 0o14226, '', 'OCT', '14226', 'INITIAL/FINAL ALTITUDE', kind='data', line=622)
W('42,2615', 0o31757, '', 'OCT', '31757', kind='data', line=623)
W('42,2616', 0o02476, '', 'OCT', '02476', 'ALTITUDE RATE', kind='data', line=624)
W('42,2617', 0o05531, '', 'OCT', '05531', kind='data', line=625)
W('42,2620', 0o02727, '', 'OCT', '02727', 'FORWARD/LATERAL VELOCTY', kind='data', line=626)
W('42,2621', 0o16415, '', 'OCT', '16415', kind='data', line=627)
W('42,2622', 0o00007, '', 'OCT', '00007', 'ROT HAND CONT ANGLE RATE', kind='data', line=628)
W('42,2623', 0o13734, '', 'OCT', '13734', kind='data', line=629)
W('42,2624', 0o74477, '', '2DEC', '-.6440 E-5 B14', 'LANDING RADAR VELX', kind='data', line=630)
W('42,2625', 0o50643, kind='data', line=630)

W('42,2626', 0o06265, '', '2DEC', '1.212 E-5 B14', 'LANDING RADAR VELY', kind='data', line=632)
W('42,2627', 0o16004, kind='data', line=632)

W('42,2630', 0o04426, '', '2DEC', '.8668 E-5 B14', 'LANDING RADAR VELZ', kind='data', line=634)
W('42,2631', 0o31433, kind='data', line=634)

W('42,2632', 0o34772, '', 'OCT', '34772', 'POSITION7', kind='data', line=636)
W('42,2633', 0o07016, '', 'OCT', '07016', kind='data', line=637)
W('42,2634', 0o01030, '', 'OCT', '01030', 'TRIM DEGREES2', kind='data', line=638)
W('42,2635', 0o33675, '', 'OCT', '33675', kind='data', line=639)
W('42,2636', 0o01046, '', 'OCT', '01046', 'COMPUTED ALTITUDE', kind='data', line=640)
W('42,2637', 0o15700, '', 'OCT', '15700', kind='data', line=641)
W('42,2640', 0o00321, '', 'OCT', '00321', 'DP DEGREES', kind='data', line=642)
W('42,2641', 0o26706, '', 'OCT', '26706', kind='data', line=643)
W('42,2642', 0o04231, '', '2DEC', '17.2010499 B-7', 'POSITION 9', kind='data', line=644)
W('42,2643', 0o27400, kind='data', line=644)

W('42,2644', 0o01031, '', '2DEC', '.032808399', 'VELOCITY4', kind='data', line=646)
W('42,2645', 0o21032, kind='data', line=646)
# Page 314
W('42,2646', 0o12172, '', '2DEC', '.32', 'RADIANS', kind='data', line=648)
W('42,2647', 0o34122, kind='data', line=648)

# END OF SFOUTAB

# NN    SF CONSTANT             SF ROUTINE
W('42,2650', 0o03453, 'IDADDTAB', 'ECADR', 'TTOGO', '40    MIN/SEC                 M/S', kind='data', line=653)
W('42,2651', 0o03663, '', 'ECADR', 'VGDISP', '40    VEL3                    DP3', kind='data', line=654)
W('42,2652', 0o03507, '', 'ECADR', 'DVTOTAL', '40    VEL3                    DP3', kind='data', line=655)
W('42,2653', 0o01045, '', 'ECADR', 'DSPTEM1', '41    CDU DEG                 CDU', kind='data', line=656)
W('42,2654', 0o01046, '', 'ECADR', 'DSPTEM1 +1', '41    ELEV DEG                ARTH', kind='data', line=657)
W('42,2655', 0o00000, '', 'OCT', '0', '41    SPARE COMPONENT', kind='data', line=658)
W('42,2656', 0o02316, '', 'ECADR', 'HAPO', '42    POS4                    DP3', kind='data', line=659)
W('42,2657', 0o02320, '', 'ECADR', 'HPER', '42    POS4                    DP3', kind='data', line=660)
W('42,2660', 0o03663, '', 'ECADR', 'VGDISP', '42    VEL3                    DP3', kind='data', line=661)
W('42,2661', 0o01120, '', 'ECADR', 'LAT', '43    DPDEG(360)              DP4', kind='data', line=662)
W('42,2662', 0o01122, '', 'ECADR', 'LONG', '43    DPDEG(360               DP4', kind='data', line=663)
W('42,2663', 0o01124, '', 'ECADR', 'ALT', '43    POS4                    DP3', kind='data', line=664)
W('42,2664', 0o02117, '', 'ECADR', 'HAPOX', '44    POS4                    DP3', kind='data', line=665)
W('42,2665', 0o02121, '', 'ECADR', 'HPERX', '44    POS4                    DP3', kind='data', line=666)
W('42,2666', 0o02140, '', 'ECADR', 'TFF', '44    MIN/SEC                 M/S', kind='data', line=667)
W('42,2667', 0o03462, '', 'ECADR', 'TRKMKCNT', '45    WHOLE                   ARTH', kind='data', line=668)
W('42,2670', 0o03453, '', 'ECADR', 'TTOGO', '45    MIN/SEC                 M/S', kind='data', line=669)
W('42,2671', 0o02252, '', 'ECADR', '+MGA', '45    DPDEG(360)              DP4', kind='data', line=670)
W('42,2672', 0o01343, '', 'ECADR', 'DAPDATR1', '46    OCTAL ONLY              OCT', kind='data', line=671)
W('42,2673', 0o00000, '', 'OCT', '0', '46    SPARE COMPONENT', kind='data', line=672)
W('42,2674', 0o00000, '', 'OCT', '0', '46    SPARE COMPONENT', kind='data', line=673)
W('42,2675', 0o01331, '', 'ECADR', 'LEMMASS', '47    WEIGHT2                 ARTH1', kind='data', line=674)
W('42,2676', 0o01332, '', 'ECADR', 'CSMMASS', '47    WEIGHT2                 ARTH1', kind='data', line=675)
W('42,2677', 0o00000, '', 'OCT', '0', '47    SPARE COMPONENT', kind='data', line=676)
W('42,2700', 0o03002, '', 'ECADR', 'PITTIME', '48    TRIM DEG2               ARTH', kind='data', line=677)
W('42,2701', 0o03001, '', 'ECADR', 'ROLLTIME', '48    TRIM DEG2               ARTH', kind='data', line=678)
W('42,2702', 0o00000, '', 'OCT', '0', '48    SPARE COMPONENT', kind='data', line=679)
W('42,2703', 0o00314, '', 'ECADR', 'R22DISP', '49    POS4                    DP3', kind='data', line=680)
W('42,2704', 0o00316, '', 'ECADR', 'R22DISP +2', '49    VEL3                    DP3', kind='data', line=681)
W('42,2705', 0o03745, '', 'ECADR', 'WHCHREAD', '49    WHOLE                   ARTH', kind='data', line=682)
W('42,2706', 0o00000, '', 'OCT', '0', '50    SPARE', kind='data', line=683)
W('42,2707', 0o00000, '', 'OCT', '0', '50    SPARE', kind='data', line=684)
W('42,2710', 0o00000, '', 'OCT', '0', '50    SPARE', kind='data', line=685)
W('42,2711', 0o02200, '', 'ECADR', 'ALPHASB', '51    DPDEG(360)              DP4', kind='data', line=686)
W('42,2712', 0o02202, '', 'ECADR', 'BETASB', '51    DPDEG(360)              DP4', kind='data', line=687)
W('42,2713', 0o00000, '', 'OCT', '0', '51    SPARE COMPONENT', kind='data', line=688)
W('42,2714', 0o01755, '', 'ECADR', 'ACTCENT', '52    DPDEG(360)              DP4', kind='data', line=689)
W('42,2715', 0o00000, '', 'OCT', '00000', '52    SPARE COMPONENT', kind='data', line=690)
W('42,2716', 0o00000, '', 'OCT', '00000', '52    SPARE COMPONENT', kind='data', line=691)
W('42,2717', 0o00000, '', 'OCT', '00000', '53    SPARE', kind='data', line=692)
W('42,2720', 0o00000, '', 'OCT', '00000', '53', kind='data', line=693)
W('42,2721', 0o00000, '', 'OCT', '00000', '53', kind='data', line=694)
W('42,2722', 0o02200, '', 'ECADR', 'RANGE', '54    POS5                    DP1', kind='data', line=695)
# Page 315
W('42,2723', 0o02202, '', 'ECADR', 'RRATE', '54    VEL3                    DP3', kind='data', line=697)
W('42,2724', 0o02204, '', 'ECADR', 'RTHETA', '54    DPDEG(360)              DP4', kind='data', line=698)
W('42,2725', 0o03466, '', 'ECADR', 'NN', '55    WHOLE                   ARTH', kind='data', line=699)
W('42,2726', 0o02256, '', 'ECADR', 'ELEV', '55    DPDEG(360)              DP4', kind='data', line=700)
W('42,2727', 0o03620, '', 'ECADR', 'CENTANG', '55    DPDEG(360)              DP4', kind='data', line=701)
W('42,2730', 0o02200, '', 'ECADR', 'RR-AZ', '56    DPDEG(360)              DP4', kind='data', line=702)
W('42,2731', 0o02202, '', 'ECADR', 'RR-ELEV', '56    DPDEG(360)              DP4', kind='data', line=703)
W('42,2732', 0o00000, '', 'OCT', '0', '56    SPARE COMPONENT', kind='data', line=704)
W('42,2733', 0o02302, '', 'ECADR', 'DELTAR', '57    POS4                    DP3', kind='data', line=705)
W('42,2734', 0o00000, '', 'OCT', '0', '57    SPARE COMPONENT', kind='data', line=706)
W('42,2735', 0o00000, '', 'OCT', '0', '57    SPARE COMPONENT', kind='data', line=707)
W('42,2736', 0o03605, '', 'ECADR', 'POSTTPI', '58    POS4                    DP3', kind='data', line=708)
W('42,2737', 0o03575, '', 'ECADR', 'DELVTPI', '58    VEL3                    DP3', kind='data', line=709)
W('42,2740', 0o02347, '', 'ECADR', 'DELVTPF', '58    VEL3                    DP3', kind='data', line=710)
W('42,2741', 0o02302, '', 'ECADR', 'DVLOS', '59    VEL3                    DP3', kind='data', line=711)
W('42,2742', 0o02304, '', 'ECADR', 'DVLOS +2', '59    VEL3                    DP3', kind='data', line=712)
W('42,2743', 0o02306, '', 'ECADR', 'DVLOS +4', '59    VEL3                    DP3', kind='data', line=713)
W('42,2744', 0o02262, '', 'ECADR', 'VHORIZ', '60    VEL3                    DP3', kind='data', line=714)
W('42,2745', 0o03473, '', 'ECADR', 'HDOTDISP', '60    VEL3                    DP3', kind='data', line=715)
W('42,2746', 0o03534, '', 'ECADR', 'HCALC', '60    COMP ALT                DP1', kind='data', line=716)
W('42,2747', 0o03475, '', 'ECADR', 'TTFDISP', '61    MIN/SEC                 M/S', kind='data', line=717)
W('42,2750', 0o03453, '', 'ECADR', 'TTOGO', '61    MIN/SEC                 M/S', kind='data', line=718)
W('42,2751', 0o02626, '', 'ECADR', 'OUTOFPLN', '61    POS7                    DP4', kind='data', line=719)
W('42,2752', 0o03471, '', 'ECADR', 'ABVEL', '62    VEL3                    DP3', kind='data', line=720)
W('42,2753', 0o03453, '', 'ECADR', 'TTOGO', '62    MIN/SEC                 M/S', kind='data', line=721)
W('42,2754', 0o03507, '', 'ECADR', 'DVTOTAL', '62    VEL3                    DP3', kind='data', line=722)
W('42,2755', 0o03471, '', 'ECADR', 'ABVEL', '63    VEL3                    DP3', kind='data', line=723)
W('42,2756', 0o03473, '', 'ECADR', 'HDOTDISP', '63    VEL3                    DP3', kind='data', line=724)
W('42,2757', 0o03774, '', 'ECADR', 'HCALC1', '63    COMP ALT                DP1', kind='data', line=725)
W('42,2760', 0o03666, '', 'ECADR', 'FUNNYDSP', '64    2INT                    2INT', kind='data', line=726)
W('42,2761', 0o03473, '', 'ECADR', 'HDOTDISP', '64    VEL3                    DP3', kind='data', line=727)
W('42,2762', 0o03534, '', 'ECADR', 'HCALC', '64    COMP ALT                DP1', kind='data', line=728)
W('42,2763', 0o00013, '', 'ECADR', 'SAMPTIME', '65    HMS (MIXED ONLY TO KEEP CODE 65) HMS', kind='data', line=729)
W('42,2764', 0o00013, '', 'ECADR', 'SAMPTIME', '65    HMS                     HMS', kind='data', line=730)
W('42,2765', 0o00013, '', 'ECADR', 'SAMPTIME', '65    HMS                     HMS', kind='data', line=731)
W('42,2766', 0o02206, '', 'ECADR', 'RSTACK +6', '66    LANDING RADAR ALT       DP1', kind='data', line=732)
W('42,2767', 0o00000, '', 'OCT', '0', '66    LR POSITION             LRPOS', kind='data', line=733)
W('42,2770', 0o00000, '', 'OCT', '0', '66    SPARE COMPONENT', kind='data', line=734)
W('42,2771', 0o02200, '', 'ECADR', 'RSTACK', '67    LANDING RADAR VELX      DP1', kind='data', line=735)
W('42,2772', 0o02202, '', 'ECADR', 'RSTACK +2', '67    LANDING RADAR VELY      DP1', kind='data', line=736)
W('42,2773', 0o02204, '', 'ECADR', 'RSTACK +4', '67    LANDING RADAR VELZ      DP1', kind='data', line=737)
W('42,2774', 0o02624, '', 'ECADR', 'RANGEDSP', '68    POS7                    DP4', kind='data', line=738)
W('42,2775', 0o03475, '', 'ECADR', 'TTFDISP', '68    MIN/SEC                 M/S', kind='data', line=739)
W('42,2776', 0o03664, '', 'ECADR', 'DELTAH', '68    COMP ALT                DP1', kind='data', line=740)
W('42,2777', 0o00000, '', 'OCT', '00000', '69    SPARE', kind='data', line=741)
W('42,3000', 0o00000, '', 'OCT', '00000', '69', kind='data', line=742)
W('42,3001', 0o00000, '', 'OCT', '00000', '69', kind='data', line=743)
W('42,3002', 0o00735, '', 'ECADR', 'AOTCODE', '70    OCTAL ONLY              OCT', kind='data', line=744)
W('42,3003', 0o00736, '', 'ECADR', 'AOTCODE +1', '70    OCTAL ONLY              OCT', kind='data', line=745)
W('42,3004', 0o00737, '', 'ECADR', 'AOTCODE +2', '70    OCTAL ONLY              OCT', kind='data', line=746)
# Page 316
W('42,3005', 0o00735, '', 'ECADR', 'AOTCODE', '71    OCTAL ONLY              OCT', kind='data', line=748)
W('42,3006', 0o00736, '', 'ECADR', 'AOTCODE +1', '71    OCTAL ONLY              OCT', kind='data', line=749)
W('42,3007', 0o00737, '', 'ECADR', 'AOTCODE +2', '71    OCTAL ONLY              OCT', kind='data', line=750)
W('42,3010', 0o00035, '', 'ECADR', 'CDUT', '72    360-CDU DEG             360-CDU', kind='data', line=751)
W('42,3011', 0o00036, '', 'ECADR', 'CDUS', '72    CDU DEG                 CDU', kind='data', line=752)
W('42,3012', 0o00000, '', 'OCT', '0', '72    SPARE COMPONENT', kind='data', line=753)
W('42,3013', 0o01107, '', 'ECADR', 'TANG', '73    360-CDU DEG             360-CDU', kind='data', line=754)
W('42,3014', 0o01110, '', 'ECADR', 'TANG +1', '73    CDU DEG                 CDU', kind='data', line=755)
W('42,3015', 0o00000, '', 'OCT', '0', '73    SPARE COMPONENT', kind='data', line=756)
W('42,3016', 0o03453, '', 'ECADR', 'TTOGO', '74    MIN/SEC                 M/S', kind='data', line=757)
W('42,3017', 0o02362, '', 'ECADR', 'YAW', '74    DPDEG(360)              DP4', kind='data', line=758)
W('42,3020', 0o02364, '', 'ECADR', 'PITCH', '74    DPDEG(360)              DP4', kind='data', line=759)
W('42,3021', 0o03577, '', 'ECADR', 'DIFFALT', '75    POS4                    DP3', kind='data', line=760)
W('42,3022', 0o02252, '', 'ECADR', 'T1TOT2', '75    MIN/SEC', kind='data', line=761)
W('42,3023', 0o02254, '', 'ECADR', 'T2TOT3', '75    MIN/SEC                 M/S', kind='data', line=762)
W('42,3024', 0o02276, '', 'ECADR', 'ZDOTD', '76    VEL3                    DP3', kind='data', line=763)
W('42,3025', 0o02272, '', 'ECADR', 'RDOTD', '76    VEL3                    DP3', kind='data', line=764)
W('42,3026', 0o03642, '', 'ECADR', 'XRANGE', '76    POS4                    DP3', kind='data', line=765)
W('42,3027', 0o03453, '', 'ECADR', 'TTOGO', '77    MIN/SEC                 M/S', kind='data', line=766)
W('42,3030', 0o02310, '', 'ECADR', 'YDOT', '77    VEL3                    DP3', kind='data', line=767)
W('42,3031', 0o00000, '', 'OCT', '0', '77    SPARE COMPONENT', kind='data', line=768)
W('42,3032', 0o02200, '', 'ECADR', 'RSTACK', '78    RR RANGE                DP1', kind='data', line=769)
W('42,3033', 0o02202, '', 'ECADR', 'RSTACK +2', '78    RR RANGE RATE           DP1', kind='data', line=770)
W('42,3034', 0o00000, '', 'OCT', '00000', '78    SPARE COMPONENT', kind='data', line=771)
W('42,3035', 0o01236, '', 'ECADR', 'CURSOR', '79    CDU DEG                 CDU', kind='data', line=772)
W('42,3036', 0o01240, '', 'ECADR', 'SPIRAL', '79    CDU DEG                 CDU', kind='data', line=773)
W('42,3037', 0o01242, '', 'ECADR', 'POSCODE', '79    WHOLE                   ARTH', kind='data', line=774)
W('42,3040', 0o03733, '', 'ECADR', 'DATAGOOD', '80    WHOLE                   ARTH', kind='data', line=775)
W('42,3041', 0o03734, '', 'ECADR', 'OMEGAD', '80    DPDEG(360)              DP4', kind='data', line=776)
W('42,3042', 0o00000, '', 'OCT', '0', '80    SPARE COMPONENT', kind='data', line=777)
W('42,3043', 0o03433, '', 'ECADR', 'DELVLVC', '81    VEL3                    DP3', kind='data', line=778)
W('42,3044', 0o03435, '', 'ECADR', 'DELVLVC +2', '81    VEL3                    DP3', kind='data', line=779)
W('42,3045', 0o03437, '', 'ECADR', 'DELVLVC +4', '81    VEL3                    DP3', kind='data', line=780)
W('42,3046', 0o03433, '', 'ECADR', 'DELVLVC', '82    VEL3                    DP3', kind='data', line=781)
W('42,3047', 0o03435, '', 'ECADR', 'DELVLVC +2', '82    VEL3                    DP3', kind='data', line=782)
W('42,3050', 0o03437, '', 'ECADR', 'DELVLVC +4', '82    VEL3                    DP3', kind='data', line=783)
W('42,3051', 0o03622, '', 'ECADR', 'DELVIMU', '83    VEL3                    DP3', kind='data', line=784)
W('42,3052', 0o03624, '', 'ECADR', 'DELVIMU +2', '83    VEL3                    DP3', kind='data', line=785)
W('42,3053', 0o03626, '', 'ECADR', 'DELVIMU +4', '83    VEL3                    DP3', kind='data', line=786)
W('42,3054', 0o02222, '', 'ECADR', 'DELVOV', '84    VEL3                    DP3', kind='data', line=787)
W('42,3055', 0o02224, '', 'ECADR', 'DELVOV +2', '84    VEL3                    DP3', kind='data', line=788)
W('42,3056', 0o02226, '', 'ECADR', 'DELVOV +4', '84    VEL3                    DP3', kind='data', line=789)
W('42,3057', 0o03501, '', 'ECADR', 'VGBODY', '85    VEL3                    DP3', kind='data', line=790)
W('42,3060', 0o03503, '', 'ECADR', 'VGBODY +2', '85    VEL3                    DP3', kind='data', line=791)
W('42,3061', 0o03505, '', 'ECADR', 'VGBODY +4', '85    VEL3                    DP3', kind='data', line=792)
W('42,3062', 0o03433, '', 'ECADR', 'DELVLVC', '86    VEL3                    DP3', kind='data', line=793)
W('42,3063', 0o03435, '', 'ECADR', 'DELVLVC +2', '86    VEL3                    DP3', kind='data', line=794)
W('42,3064', 0o03437, '', 'ECADR', 'DELVLVC +4', '86    VEL3                    DP3', kind='data', line=795)
W('42,3065', 0o01347, '', 'ECADR', 'AZ', '87    CDU DEG                 CDU', kind='data', line=796)
W('42,3066', 0o01350, '', 'ECADR', 'EL', '87    CDU DEG                 CDU', kind='data', line=797)
# Page 317
W('42,3067', 0o00000, '', 'OCT', '0', '87    SPARE COMPONENT', kind='data', line=799)
W('42,3070', 0o02706, '', 'ECADR', 'STARAD', '88    FRAC                    FRAC', kind='data', line=800)
W('42,3071', 0o02710, '', 'ECADR', 'STARAD +2', '88    FRAC                    FRAC', kind='data', line=801)
W('42,3072', 0o02712, '', 'ECADR', 'STARAD +4', '88    FRAC                    FRAC', kind='data', line=802)
W('42,3073', 0o02706, '', 'ECADR', 'LANDLAT', '89    DPDEG(90)               DP3', kind='data', line=803)
W('42,3074', 0o02710, '', 'ECADR', 'LANDLONG', '89    DPDEG(90)               DP3', kind='data', line=804)
W('42,3075', 0o02712, '', 'ECADR', 'LANDALT', '89    POS5                    DP1', kind='data', line=805)
W('42,3076', 0o02200, '', 'ECADR', 'RANGE', '90    POS5                    DP1', kind='data', line=806)
W('42,3077', 0o02202, '', 'ECADR', 'RRATE', '90    VEL3                    DP3', kind='data', line=807)
W('42,3100', 0o02204, '', 'ECADR', 'RTHETA', '90    DPDEG(360)              DP4', kind='data', line=808)
W('42,3101', 0o03715, '', 'ECADR', 'P21ALT', '91    POS4                    DP3', kind='data', line=809)
W('42,3102', 0o03711, '', 'ECADR', 'P21VEL', '91    VEL2                    DP4', kind='data', line=810)
W('42,3103', 0o03713, '', 'ECADR', 'P21GAM', '91    DPDEG(360)              DP4', kind='data', line=811)
W('42,3104', 0o00000, '', 'OCT', '00000', '92    SPARE', kind='data', line=812)
W('42,3105', 0o00000, '', 'OCT', '00000', '92', kind='data', line=813)
W('42,3106', 0o00000, '', 'OCT', '00000', '92', kind='data', line=814)
W('42,3107', 0o02737, '', 'ECADR', 'OGC', '93    DPDEG(90)               DP3', kind='data', line=815)
W('42,3110', 0o02741, '', 'ECADR', 'OGC +2', '93    DPDEG(90)               DP3', kind='data', line=816)
W('42,3111', 0o02743, '', 'ECADR', 'OGC +4', '93    DPDEG(90)               DP3', kind='data', line=817)
W('42,3112', 0o00000, '', 'OCT', '00000', '94    SPARE', kind='data', line=818)
W('42,3113', 0o00000, '', 'OCT', '00000', '94', kind='data', line=819)
W('42,3114', 0o00000, '', 'OCT', '00000', '94', kind='data', line=820)
W('42,3115', 0o00000, '', 'OCT', '0', '95    SPARE', kind='data', line=821)
W('42,3116', 0o00000, '', 'OCT', '0', '95    SPARE', kind='data', line=822)
W('42,3117', 0o00000, '', 'OCT', '0', '95    SPARE', kind='data', line=823)
W('42,3120', 0o00000, '', 'OCT', '0', '96    SPARE', kind='data', line=824)
W('42,3121', 0o00000, '', 'OCT', '0', '96    SPARE', kind='data', line=825)
W('42,3122', 0o00000, '', 'OCT', '0', '96    SPARE', kind='data', line=826)
W('42,3123', 0o01045, '', 'ECADR', 'DSPTEM1', '97    WHOLE                   ARTH', kind='data', line=827)
W('42,3124', 0o01046, '', 'ECADR', 'DSPTEM1 +1', '97    WHOLE                   ARTH', kind='data', line=828)
W('42,3125', 0o01047, '', 'ECADR', 'DSPTEM1 +2', '97    WHOLE                   ARTH', kind='data', line=829)
W('42,3126', 0o01050, '', 'ECADR', 'DSPTEM2', '98    WHOLE                   ARTH', kind='data', line=830)
W('42,3127', 0o01051, '', 'ECADR', 'DSPTEM2 +1', '98    FRAC                    FRAC', kind='data', line=831)
W('42,3130', 0o01052, '', 'ECADR', 'DSPTEM2 +2', '98    WHOLE                   ARTH', kind='data', line=832)
W('42,3131', 0o02200, '', 'ECADR', 'WWPOS', '99    POS9                    DP3', kind='data', line=833)
W('42,3132', 0o02202, '', 'ECADR', 'WWVEL', '99    VEL4                    DP2', kind='data', line=834)
W('42,3133', 0o02204, '', 'ECADR', 'WWBIAS', '99    RADIANS                 DP4', kind='data', line=835)

# END OF IDADDTAB

# NN    SF ROUTINES
W('42,3134', 0o16351, 'RUTMXTAB', 'OCT', '16351', '40    M/S, DP3, DP3', kind='data', line=840)
W('42,3135', 0o00142, '', 'OCT', '00142', '41    CDU, ARTH', kind='data', line=841)
W('42,3136', 0o16347, '', 'OCT', '16347', '42    DP3, DP3, DP3', kind='data', line=842)
W('42,3137', 0o16512, '', 'OCT', '16512', '43    DP4, DP4, DP3', kind='data', line=843)
W('42,3140', 0o22347, '', 'OCT', '22347', '44    DP3, DP3, M/S', kind='data', line=844)
W('42,3141', 0o24443, '', 'OCT', '24443', '45    ARTH, M/S, DP4', kind='data', line=845)
W('42,3142', 0o00000, '', 'OCT', '00000', '46    OCT', kind='data', line=846)
W('42,3143', 0o00553, '', 'OCT', '00553', '47    ARITH1, ARITH1', kind='data', line=847)
# Page 318
W('42,3144', 0o00143, '', 'OCT', '00143', '48    ARTH, ARTH', kind='data', line=849)
W('42,3145', 0o06347, '', 'OCT', '06347', '49    DP3, DP3, ARTH', kind='data', line=850)
W('42,3146', 0o00000, '', 'OCT', '0', '50    SPARE', kind='data', line=851)
W('42,3147', 0o00512, '', 'OCT', '00512', '51    DP4, DP4', kind='data', line=852)
W('42,3150', 0o00012, '', 'OCT', '00012', '52    DP4', kind='data', line=853)
W('42,3151', 0o00000, '', 'OCT', '00000', '53    SPARE', kind='data', line=854)
W('42,3152', 0o24344, '', 'OCT', '24344', '54    DP1, DP3, DP4', kind='data', line=855)
W('42,3153', 0o24503, '', 'OCT', '24503', '55    ARTH, DP4, DP4', kind='data', line=856)
W('42,3154', 0o00512, '', 'OCT', '00512', '56    DP4, DP4', kind='data', line=857)
W('42,3155', 0o00007, '', 'OCT', '00007', '57    DP3', kind='data', line=858)
W('42,3156', 0o16347, '', 'OCT', '16347', '58    DP3, DP3, DP3', kind='data', line=859)
W('42,3157', 0o16347, '', 'OCT', '16347', '59    DP3, DP3, DP3', kind='data', line=860)
W('42,3160', 0o10347, '', 'OCT', '10347', '60    DP3, DP3, DP1', kind='data', line=861)
W('42,3161', 0o24451, '', 'OCT', '24451', '61    M/S, M/S, DP4', kind='data', line=862)
W('42,3162', 0o16447, '', 'OCT', '16447', '62    DP3, M/S, DP3', kind='data', line=863)
W('42,3163', 0o10347, '', 'OCT', '10347', '63    DP3, DP3, DP1', kind='data', line=864)
W('42,3164', 0o10354, '', 'OCT', '10354', '64    2INT, DP3, DP1', kind='data', line=865)
W('42,3165', 0o20410, '', 'OCT', '20410', '65    HMS, HMS, HMS', kind='data', line=866)
W('42,3166', 0o00304, '', 'OCT', '00304', '66    DP1, LRPOS', kind='data', line=867)
W('42,3167', 0o10204, '', 'OCT', '10204', '67    DP1, DP1, DP1', kind='data', line=868)
W('42,3170', 0o10452, '', 'OCT', '10452', '68    DP4, M/S, DP1', kind='data', line=869)
W('42,3171', 0o00000, '', 'OCT', '00000', '69    SPARE', kind='data', line=870)
W('42,3172', 0o00000, '', 'OCT', '0', '70    OCT, OCT, OCT', kind='data', line=871)
W('42,3173', 0o00000, '', 'OCT', '0', '71    OCT, OCT, OCT', kind='data', line=872)
W('42,3174', 0o00115, '', 'OCT', '00115', '72    360-CDU, CDU', kind='data', line=873)
W('42,3175', 0o00115, '', 'OCT', '00115', '73    360-CDU, CDU', kind='data', line=874)
W('42,3176', 0o24511, '', 'OCT', '24511', '74    M/S, DP4, DP4', kind='data', line=875)
W('42,3177', 0o22447, '', 'OCT', '22447', '75    DP3, M/S, M/S', kind='data', line=876)
W('42,3200', 0o16347, '', 'OCT', '16347', '76    DP3, DP3, DP3', kind='data', line=877)
W('42,3201', 0o00351, '', 'OCT', '00351', '77    M/S, DP3', kind='data', line=878)
W('42,3202', 0o00204, '', 'OCT', '00204', '78    DP1, DP1', kind='data', line=879)
W('42,3203', 0o06102, '', 'OCT', '06102', '79    CDU, CDU, ARTH', kind='data', line=880)
W('42,3204', 0o00503, '', 'OCT', '00503', '80    ARTH, DP4', kind='data', line=881)
W('42,3205', 0o16347, '', 'OCT', '16347', '81    DP3, DP3, DP3', kind='data', line=882)
W('42,3206', 0o16347, '', 'OCT', '16347', '82    DP3, DP3, DP3', kind='data', line=883)
W('42,3207', 0o16347, '', 'OCT', '16347', '83    DP3, DP3, DP3', kind='data', line=884)
W('42,3210', 0o16347, '', 'OCT', '16347', '84    DP3, DP3, DP3', kind='data', line=885)
W('42,3211', 0o16347, '', 'OCT', '16347', '85    DP3, DP3, DP3', kind='data', line=886)
W('42,3212', 0o16347, '', 'OCT', '16347', '86    DP3, DP3, DP3', kind='data', line=887)
W('42,3213', 0o00102, '', 'OCT', '00102', '87    CDU, CDU', kind='data', line=888)
W('42,3214', 0o02041, '', 'OCT', '02041', '88    FRAC FOR EACH', kind='data', line=889)
W('42,3215', 0o10347, '', 'OCT', '10347', '89    DP3, DP3, DP1', kind='data', line=890)
W('42,3216', 0o24344, '', 'OCT', '24344', '90    DP1, DP3, DP4', kind='data', line=891)
W('42,3217', 0o24507, '', 'OCT', '24507', '91    DP3, DP4, DP4', kind='data', line=892)
W('42,3220', 0o00000, '', 'OCT', '00000', '92    SPARE', kind='data', line=893)
W('42,3221', 0o16347, '', 'OCT', '16347', '93    DP3, DP3, DP3', kind='data', line=894)
W('42,3222', 0o00000, '', 'OCT', '00000', '94    SPARE', kind='data', line=895)
W('42,3223', 0o00000, '', 'OCT', '0', '95    SPARE', kind='data', line=896)
W('42,3224', 0o00000, '', 'OCT', '0', '96    SPARE', kind='data', line=897)
W('42,3225', 0o06143, '', 'OCT', '06143', '97    ARTH, ARTH, ARTH', kind='data', line=898)
# Page 319
W('42,3226', 0o06043, '', 'OCT', '06043', '98    ARTH, FRAC, ARTH', kind='data', line=900)
W('42,3227', 0o24247, '', 'OCT', '24247', '99    DP3, DP2, DP4', kind='data', line=901)

# END OF RUTMXTAB

#   SBANK= LOWSUPER
