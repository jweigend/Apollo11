"""PINBALL_NOUN_TABLES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/PINBALL_NOUN_TABLES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 268-284 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('PINBALL_NOUN_TABLES', 'PINBALL_NOUN_TABLES.agc', 'Comanche055', pages='268-284')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     PINBALL_NOUN_TABLES.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 268-284
# Contact:      Ron Burkey <info@sandroid.org>,
# Fabrizio Bernardini <fabrizio@spacecraft.it>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-18 FB   Transcription Batch 3 Assignment.
# 2009-05-23 RSB  In NNTYPTAB, corrected former 13 SPARE.
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

# Page 268
# THE FOLLOWING REFERS TO THE NOUN TABLES

# COMPONENT CODE NUMBER         INTERPRETATION

# 00000                         1 COMPONENT
# 00001                         2 COMPONENT
# 00010                         3 COMPONENT
# X1XXX                         BIT 4 = 1. DECIMAL ONLY
# 1XXXX                         BIT 5 = 1. NO LOAD
# END OF COMPONENT CODE NUMBERS

# SF ROUTINE CODE NUMBER        INTERPRETATION

# 00000         OCTAL ONLY
# 00001         STRAIGHT FRACTIONAL
# 00010         CDU DEGREES (XXX.XX)
# 00011         ARITHMETIC SF
# 00100         ARITH DP1       OUT(MULT BY 2EXP14 AT END)      IN(STRAIGHT)
# 00101         ARITH DP2       OUT(STRAIGHT)                   IN(SL 7 AT END)
# 00110         Y OPTICS DEGREES (XX.XXX MAX 89.999)
# 00111         ARITH DP3       OUT ( SL 7 AT END)              IN ( STRAIGHT)
# 01000         WHOLE HOURS IN R1, WHOLE MINUTES (MOD 60) IN R2,
# SECONDS (MOD 60) 0XX.XX IN R3. *** ALARMS IF USED WITH OCTAL
# 01001         MINUTES (MOD 60) IN D1D2, D3 BLANK, SECONDS (MOD 60) IN D4D5
# LIMITS TO 59B59 IF MAG EXCEEDS THIS VALUE.
# ALARMS IF USED WITH OCTAL ******** IN (ALARM)
# 01010         ARITH DP4       OUT (STRAIGHT)                  IN (SL 3 AT END)
# 01011         ARITH1 SF       OUT(MULT BY 2EXP14 AT END)      IN(STRAIGHT)
# 01100         2 INTEGERS IN D1D2, D4D5, D3 BLANK.
# ALARMS IF USED WITH OCTAL ******** IN (ALARM)
# 01101 DP STRAIGHT FRACTIONAL
# END OF SF ROUTINE CODE NUMBERS

# SF CONSTANT CODE NUMBER INTERPRETATION

# 00000                   WHOLE                           USE ARITH
# 00000                   DP TIME SEC (XXX.XX SEC)        USE ARITHDP1
# 00001                   SPARE
# 00010                   CDU DEGREES                  USE CDU DEGREES
# 00010                   Y OPTICS DEGREES        USE Y OPTICS DEGREES
# 00011                   DP DEGREES (90) XX.XXX DEG      USE ARITHDP3
# 00100                   DP DEGREES (360) XXX.XX DEG     USE ARITHDP4
# 00101                   DEGREES (180) XXX.XX DEG        USE ARITH
# 00110                   WEIGHT2 (XXXXX. LBS)            USE ARITH1
# 00111                   POSITION5 (XXX.XX NAUTICAL MILES)
# USE ARITHDP3
# 01000                   POSITION4 (XXXX.X NAUTICAL MILES)
# Page 269
# USE ARITHDP3
# 01001                   VELOCITY2 (XXXXX. FT/SEC)   USE ARITHDP4
# 01010                   VELOCITY3 (XXXX.X FT/SEC)   USE ARITHDP3
# 01011                   ELEVATION DEGREES (89.999MAX) USE ARITH
# 01100                   TRIM DEGREES (XXX.XX DEG)    USE ARITH
# 01101                   INERTIA (XXXXXBB. SLUG FT FT)  USE ARITH
# 01101                   THRUST MOMENT (XXXXXBB.FT LBS) USE ARITH
# 01110                   VELOCITY/2VS (XXXXX. FT/SEC)USE ARITHDP4
# 01111                   POSITION6 (XXXX.X NAUT MI)  USE ARITHDP3
# 10000                   DRAG ACCELERATION (XXX.XX G)USE ARITHDP2
# 10001                   POSITION8 (XXXX.X NAUT MI)  USE ARITHDP3
# 10010                   POSITION9 (XXXXX. FT)       USE ARITHDP3
# 10011                   VELOCITY4 (XXXX.X FT/SEC)   USE ARITHDP2
# END OF SF CONSTANT CODE NUMBERS

# FOR GREATER THAN SINGLE PRECISION SCALES, PUT ADDRESS IN MAJOR PART INTO
# NOUN TABLES.
# OCTAL LOADS PLACE +0 INTO MAJOR PART, DATA INTO MINOR PART.
# OCTAL DISPLAYS SHOW MINOR PART ONLY.
# TO GET AT BOTH MAJOR AND MINOR PARTS(IN OCTAL), USE NOUN 01.

# A NOUN MAY BE DECLARED :DECIMAL ONLY: BY MAKING BIT4=1 OF ITS COMPONENT
# CODE NUMBER.  IF THIS NOUN IS USED WITH ANY OCTAL DISPLAY VERB, OR IF
# DATA IS LOADED IN OCTAL, IT ALARMS.

# IN LOADING AN :HOURS, MINUTES, SECONDS: NOUN, ALL 3 WORDS MUST BE
# LOADED, OR ALARM.
# ALARM IF AN ATTEMPT IS MADE TO LOAD :SPLIT MINUTES/SECONDS: (MMBSS).
# THIS IS USED FOR DISPLAY ONLY.

# Page 270
# THE FOLLOWING ROUTINES ARE FOR READING THE NOUN TABLES AND THE SF TABLES
# (WHICH ARE IN A SEPARATE BANK FROM THE REST OF PINBALL).  THESE READING
# ROUTINES ARE IN THE SAME BANK AS THE TABLES.  THEY ARE CALLED BY DXCH Z.

# LODNNTAB LOADS NNADTEM WITH THE NNADTAB ENTRY, NNTYPTEM WITH THE
# NNTYPTAB ENTRY.  IF THE NOUN IS MIXED, IDADITEM IS LOADED WITH THE FIRST
# IDADDTAB ENTRY, IDAD2TEM THE SECOND IDADDTAB ENTRY, IDAD3TEM THE THIRD
# IDADDTAB ENTRY, RUTMXTEM WITH THE RUTMXTAB ENTRY.  MIXBR IS SET FOR
# MIXED OR NORMAL NOUN.

#   BANK 06
#   SETLOC PINBALL3
#   BANK

#   COUNT 42/NOUNS

W('42,2062', 0o52152, 'LODNNTAB', 'DXCH', 'IDAD2TEM', 'SAVE RETURN INFO IN IDAD2TEM, IDAD3TEM.', line=134)
W('42,2063', 0o51002, '', 'INDEX', 'NOUNREG', line=135)
W('42,2064', 0o32133, '', 'CAF', 'NNADTAB', line=136)
W('42,2065', 0o54146, '', 'TS', 'NNADTEM', line=137)
W('42,2066', 0o51002, '', 'INDEX', 'NOUNREG', line=138)
W('42,2067', 0o32277, '', 'CAF', 'NNTYPTAB', line=139)
W('42,2070', 0o54147, '', 'TS', 'NNTYPTEM', line=140)
W('42,2071', 0o41002, '', 'CS', 'NOUNREG', line=141)
W('42,2072', 0o65033, '', 'AD', 'MIXCON', line=142)
W('42,2073', 0o00006, '', 'EXTEND', line=143)
W('42,2074', 0o62100, '', 'BZMF', 'LODMIXNN', 'NOUN NUMBER G/E FIRST MIXED NOUN', line=144)
W('42,2075', 0o35017, '', 'CAF', 'ONE', 'NOUN NUMBER L/ FIRST MIXED NOUN', line=145)
W('42,2076', 0o54140, '', 'TS', 'MIXBR', 'NORMAL.  +1 INTO MIXBR.', line=146)
W('42,2077', 0o02116, '', 'TC', 'LODNLV', line=147)
W('42,2100', 0o35016, 'LODMIXNN', 'CAF', 'TWO', 'MIXED.  +2 INTO MIXBR.', line=148)
W('42,2101', 0o54140, '', 'TS', 'MIXBR', line=149)
W('42,2102', 0o51002, '', 'INDEX', 'NOUNREG', line=150)
W('42,2103', 0o32777, '', 'CAF', 'RUTMXTAB -40D', 'FIRST MIXED NOUN = 40.', line=151)
W('42,2104', 0o54153, '', 'TS', 'RUTMXTEM', line=152)
W('42,2105', 0o35054, '', 'CAF', 'LOW10', line=153)
W('42,2106', 0o70146, '', 'MASK', 'NNADTEM', line=154)
W('42,2107', 0o54002, '', 'TS', 'Q', 'TEMP', line=155)
W('42,2110', 0o50000, '', 'INDEX', 'A', line=156)
W('42,2111', 0o32563, '', 'CAF', 'IDADDTAB', line=157)
W('42,2112', 0o54150, '', 'TS', 'IDAD1TEM', 'LOAD IDAD1TEM WITH FIRST IDADDTAB ENTRY', line=158)
W('42,2113', 0o00006, '', 'EXTEND', line=159)
W('42,2114', 0o50002, '', 'INDEX', 'Q', 'LOAD IDAD2TEM WITH 2ND IDADDTAB ENTRY', line=160)
W('42,2115', 0o32565, '', 'DCA', 'IDADDTAB +1', 'LOAD IDAD3TEM WITH 3RD IDADDTAB ENTRY.', line=161)
W('42,2116', 0o52152, 'LODNLV', 'DXCH', 'IDAD2TEM', 'PUT RETURN INFO INTO A, L.', line=162)
W('42,2117', 0o52006, '', 'DXCH', 'Z', line=163)

S('MIXCON', 'equals', 0o5033, line=165)  # FIRST MIXED NOUN =40.  (DEC 40)

# GTSFOUT LOADS SFTEMP1, SFTEMP2 WITH THE DP SFOUTAB ENTRIES.
# Page 271

W('42,2120', 0o52124, 'GTSFOUT', 'DXCH', 'SFTEMP1', '2X(SFCONUM) ARRIVES IN SFTEMP1.', line=170)
W('42,2121', 0o00006, '', 'EXTEND', line=171)
W('42,2122', 0o50000, '', 'INDEX', 'A', line=172)
W('42,2123', 0o32514, '', 'DCA', 'SFOUTAB', line=173)
W('42,2124', 0o52124, 'SFCOM', 'DXCH', 'SFTEMP1', line=174)
W('42,2125', 0o52006, '', 'DXCH', 'Z', line=175)

# GTSFIN LOADS SFTEMP1, SFTEMP2 WITH THE DP SFINTAB ENTRIES.

W('42,2126', 0o52124, 'GTSFIN', 'DXCH', 'SFTEMP1', '2X(SFCONUM) ARIVES IN SFTEMP1.', line=179)
W('42,2127', 0o00006, '', 'EXTEND', line=180)
W('42,2130', 0o50000, '', 'INDEX', 'A', line=181)
W('42,2131', 0o32444, '', 'DCA', 'SFINTAB', line=182)
W('42,2132', 0o12124, '', 'TCF', 'SFCOM', line=183)

# NN     NORMAL NOUNS
W('42,2133', 0o00000, 'NNADTAB', 'OCT', '00000', '00    NOT IN USE', kind='data', line=186)
W('42,2134', 0o40000, '', 'OCT', '40000', '01    SPECIFY MACHINE ADDRESS (FRACTIONAL)', kind='data', line=187)
W('42,2135', 0o40000, '', 'OCT', '40000', '02    SPECIFY MACHINE ADDRESS (WHOLE)', kind='data', line=188)
W('42,2136', 0o40000, '', 'OCT', '40000', '03    SPECIFY MACHINE ADDRESS (DEGREES)', kind='data', line=189)
W('42,2137', 0o00000, '', 'OCT', '0', '04    SPARE', kind='data', line=190)
W('42,2140', 0o01045, '', 'ECADR', 'DSPTEM1', '05    ANGULAR ERROR/DIFFERENCE', kind='data', line=191)
W('42,2141', 0o01131, '', 'ECADR', 'OPTION1', '06    OPTION CODE', kind='data', line=192)
W('42,2142', 0o01003, '', 'ECADR', 'XREG', '07    ECADR OF WORD TO BE MODIFIED', kind='data', line=193)
# ONES FOR BITS TO BE MODIFIED
# 1 TO SET OR 0 TO RESET SELECTED BITS
W('42,2143', 0o01363, '', 'ECADR', 'ALMCADR', '08    ALARM DATA', kind='data', line=196)
W('42,2144', 0o00375, '', 'ECADR', 'FAILREG', '09    ALARM CODES', kind='data', line=197)
W('42,2145', 0o77776, '', 'OCT', '77776', '10    CHANNEL TO BE SPECIFIED', kind='data', line=198)
W('42,2146', 0o02636, '', 'ECADR', 'TCSI', '11    TIG OF CSI (HRS,MIN,SEC)', kind='data', line=199)
W('42,2147', 0o01051, '', 'ECADR', 'OPTIONX', '12    OPTION CODE', kind='data', line=200)
# (USED BY EXTENDED VERBS ONLY)
W('42,2150', 0o02634, '', 'ECADR', 'TCDH', '13    TIG OF CDH (HRS,MIN,SEC)', kind='data', line=202)
W('42,2151', 0o00000, '', 'OCT', '0', '14    SPARE', kind='data', line=203)
W('42,2152', 0o77777, '', 'OCT', '77777', '15    INCREMENT MACHINE ADDRESS', kind='data', line=204)
W('42,2153', 0o01051, '', 'ECADR', 'DSPTEMX', '16    TIME OF EVENT (HRS,MIN,SEC)', kind='data', line=205)
W('42,2154', 0o01333, '', 'ECADR', 'CPHIX', '17    ASTRONAUT TOTAL ATTITUDE', kind='data', line=206)
W('42,2155', 0o01155, '', 'ECADR', 'THETAD', '18    AUTO MANEUVER BALL ANGLES', kind='data', line=207)
W('42,2156', 0o01155, '', 'ECADR', 'THETAD', '19    BYPASS ATTITUDE TRIM MANEUVER', kind='data', line=208)
W('42,2157', 0o00032, '', 'ECADR', 'CDUX', '20    ICDU ANGLES', kind='data', line=209)
W('42,2160', 0o00037, '', 'ECADR', 'PIPAX', '21    PIPAS', kind='data', line=210)
W('42,2161', 0o01155, '', 'ECADR', 'THETAD', '22    NEW ICDU ANGLES', kind='data', line=211)
W('42,2162', 0o00000, '', 'OCT', '00000', '23    SPARE', kind='data', line=212)
W('42,2163', 0o01051, '', 'ECADR', 'DSPTEM2 +1', '24    DELTA TIME FOR AGC CLOCK(HRS,MIN,SEC)', kind='data', line=213)
W('42,2164', 0o01045, '', 'ECADR', 'DSPTEM1', '25    CHECKLIST', kind='data', line=214)
# (USED WITH PLEASE PERFORM ONLY)
W('42,2165', 0o01045, '', 'ECADR', 'DSPTEM1', '26    PRIO/DELAY, ADRES, BBCON', kind='data', line=216)
W('42,2166', 0o01362, '', 'ECADR', 'SMODE', '27    SELF TEST ON/OFF SWITCH', kind='data', line=217)
# Page 272
W('42,2167', 0o00000, '', 'OCT', '0', '28    SPARE', kind='data', line=219)
W('42,2170', 0o01045, '', 'ECADR', 'DSPTEM1', '29    XSM LAUNCH AZIMUTH', kind='data', line=220)
W('42,2171', 0o01045, '', 'ECADR', 'DSPTEM1', '30    TARGET CODES', kind='data', line=221)
W('42,2172', 0o01045, '', 'ECADR', 'DSPTEM1', '31    TIME OF LANDING SITE (HRS,MIN,SEC)', kind='data', line=222)
W('42,2173', 0o02345, '', 'ECADR', '-TPER', '32    TIME TO PERIGEE (HRS,MIN,SEC)', kind='data', line=223)
W('42,2174', 0o03412, '', 'ECADR', 'TIG', '33    TIME OF IGNITION (HRS,MIN,SEC)', kind='data', line=224)
W('42,2175', 0o01045, '', 'ECADR', 'DSPTEM1', '34    TIME OF EVENT (HRS,MIN,SEC)', kind='data', line=225)
W('42,2176', 0o03660, '', 'ECADR', 'TTOGO', '35    TIME TO GO TO EVENT (HRS,MIN,SEC)', kind='data', line=226)
W('42,2177', 0o00024, '', 'ECADR', 'TIME2', '36    TIME OF AGC CLOCK (HRS,MIN,SEC)', kind='data', line=227)
W('42,2200', 0o03662, '', 'ECADR', 'TTPI', '37    TIG OF TPI (HRS,MIN,SEC)', kind='data', line=228)
W('42,2201', 0o01516, '', 'ECADR', 'TET', '38    TIME OF STATE VECTOR', kind='data', line=229)
W('42,2202', 0o02640, '', 'ECADR', 'T3TOT4', '39    DELTA TIME TO TRANSFER (HRS,MIN,SEC)', kind='data', line=230)
# END OF NNADTAB FOR NORMAL NOUNS

# NN     MIXED NOUNS
W('42,2203', 0o64000, '', 'OCT', '64000', '40    TIME TO IGNITION/CUTOFF', kind='data', line=234)
# VG
# DELTA V (ACCUMULATED)
W('42,2204', 0o02003, '', 'OCT', '02003', '41    TARGET  AZIMUTH', kind='data', line=237)
# ELEVATION
W('42,2205', 0o24006, '', 'OCT', '24006', '42    APOGEE', kind='data', line=239)
# PERIGEE
# DELTA V (REQUIRED)
W('42,2206', 0o24011, '', 'OCT', '24011', '43    LATITUDE', kind='data', line=242)
# LONGITUDE
# ALTITUDE
W('42,2207', 0o64014, '', 'OCT', '64014', '44    APOGEE', kind='data', line=245)
# PERIGEE
# TFF
W('42,2210', 0o64017, '', 'OCT', '64017', '45    MARKS (VHF - OPTICS)', kind='data', line=248)
# TTI OF NEXT BURN
# MGA
W('42,2211', 0o02022, '', 'OCT', '02022', '46    AUTOPILOT CONFIGURATION', kind='data', line=251)
W('42,2212', 0o22025, '', 'OCT', '22025', '47    THIS VEHICLE WEIGHT', kind='data', line=252)
# OTHER VEHICLE WEIGHT
W('42,2213', 0o22030, '', 'OCT', '22030', '48    PITCH TRIM', kind='data', line=254)
# YAW TRIM
W('42,2214', 0o24033, '', 'OCT', '24033', '49    DELTA R', kind='data', line=256)
# DELTA V
# VHF OR OPTICS CODE
W('42,2215', 0o64036, '', 'OCT', '64036', '50    SPLASH ERROR', kind='data', line=259)
# PERIGEE
# TFF
W('42,2216', 0o22041, '', 'OCT', '22041', '51    S-BAND ANTENNA  PITCH', kind='data', line=262)
# YAW
W('42,2217', 0o00044, '', 'OCT', '00044', '52    CENTRAL ANGLE OF ACTIVE VEHICLE', kind='data', line=264)
W('42,2220', 0o24047, '', 'OCT', '24047', '53    RANGE', kind='data', line=265)
# RANGE RATE
# PHI
# Page 273
W('42,2221', 0o24052, '', 'OCT', '24052', '54    RANGE', kind='data', line=269)
# RANGE RATE
# THETA
W('42,2222', 0o24055, '', 'OCT', '24055', '55    PERIGEE CODE', kind='data', line=272)
# ELEVATION ANGLE
# CENTRAL ANGLE
W('42,2223', 0o22060, '', 'OCT', '22060', '56    REENTRY ANGLE,', kind='data', line=275)
# DELTA V
W('42,2224', 0o20063, '', 'OCT', '20063', '57    DELTA R', kind='data', line=277)
W('42,2225', 0o24066, '', 'OCT', '24066', '58    PERIGEE ALT', kind='data', line=278)
# DELTA V TPI
# DELTA V TPF
W('42,2226', 0o24071, '', 'OCT', '24071', '59    DELTA VELOCITY LOS', kind='data', line=281)
W('42,2227', 0o24074, '', 'OCT', '24074', '60    GMAX', kind='data', line=282)
# VPRED
# GAMMA EI
W('42,2230', 0o24077, '', 'OCT', '24077', '61    IMPACT LATITUDE', kind='data', line=285)
# IMPACT LONGITUDE
# HEADS UP/DOWN
W('42,2231', 0o24102, '', 'OCT', '24102', '62    INERTIAL VEL MAG (V1)', kind='data', line=288)
# ALT RATE CHANGE (HDOT)
# ALT ABOVE PAD RADIUS (H)
W('42,2232', 0o64105, '', 'OCT', '64105', '63    RANGE 297,431 TO SPLASH (RTGO)', kind='data', line=291)
# PREDICTED INERT VEL (VIO)
# TIME TO GO TO 297,431 (TTE)
W('42,2233', 0o24110, '', 'OCT', '24110', '64    DRAG ACCELERATION', kind='data', line=294)
# INERTIAL VELOCITY (VI)
# RANGE TO SPLASH
W('42,2234', 0o24113, '', 'OCT', '24113', '65    SAMPLED AGC TIME (HRS,MIN,SEC)', kind='data', line=297)
# (FETCHED IN INTERRUPT)
W('42,2235', 0o24116, '', 'OCT', '24116', '66    COMMAND BANK ANGLE (BETA)', kind='data', line=299)
# CROSS RANGE ERROR
# DOWN RANGE ERROR
W('42,2236', 0o24121, '', 'OCT', '24121', '67    RANGE TO TARGET', kind='data', line=302)
# PRESENT LATITUDE
# PRESENT LONGITUDE
W('42,2237', 0o24124, '', 'OCT', '24124', '68    COMMAND BANK ANGLE (BETA)', kind='data', line=305)
# INERTIAL VELOCITY (VI)
# ALT RATE CHANGE (RDOT)
W('42,2240', 0o24127, '', 'OCT', '24127', '69    BETA', kind='data', line=308)
# DL
# VL
W('42,2241', 0o04132, '', 'OCT', '04132', '70    STAR CODE', kind='data', line=311)
# LANDMARK DATA
# HORIZON DATA
W('42,2242', 0o04135, '', 'OCT', '04135', '71    STAR CODE', kind='data', line=314)
# LANDMARK
# HORIZON
W('42,2243', 0o24140, '', 'OCT', '24140', '72    DELT ANG', kind='data', line=317)
# DELT ALT
# Page 274
# SEARCH OPTION
W('42,2244', 0o04143, '', 'OCT', '04143', '73    ALTITUDE', kind='data', line=321)
# VELOCITY
# FLIGHT PATH ANGLE
W('42,2245', 0o04146, '', 'OCT', '04146', '74    COMMAND BANK ANGLE (BETA)', kind='data', line=324)
# INERTIAL VELOCITY (VI)
# DRAG ACCELERATION
W('42,2246', 0o64151, '', 'OCT', '64151', '75    DELTA ALTITUDE CDH', kind='data', line=327)
# DELTA TIME (CDH-CSI OR TPI-CDH)
# DELTA TIME (TPI-CDH OR TPI-NOMTPI)
W('42,2247', 0o00000, '', 'OCT', '0', '76    SPARE', kind='data', line=330)
W('42,2250', 0o00000, '', 'OCT', '0', '77    SPARE', kind='data', line=331)
W('42,2251', 0o00000, '', 'OCT', '0', '78    SPARE', kind='data', line=332)
W('42,2252', 0o00000, '', 'OCT', '0', '79    SPARE', kind='data', line=333)
W('42,2253', 0o64170, '', 'OCT', '64170', '80    TIME TO IGNITION/CUTOFF', kind='data', line=334)
# VG
# DELTA V (ACCUMULATED)
W('42,2254', 0o24173, '', 'OCT', '24173', '81    DELTA V (LV)', kind='data', line=337)
W('42,2255', 0o24176, '', 'OCT', '24176', '82    DELTA V (LV)', kind='data', line=338)
W('42,2256', 0o24201, '', 'OCT', '24201', '83    DELTA V (BODY)', kind='data', line=339)
W('42,2257', 0o24204, '', 'OCT', '24204', '84    DELTA V (OTHER VEHICLE)', kind='data', line=340)
W('42,2260', 0o24207, '', 'OCT', '24207', '85    VG (BODY)', kind='data', line=341)
W('42,2261', 0o24212, '', 'OCT', '24212', '86    DELTA V (LV)', kind='data', line=342)
W('42,2262', 0o02215, '', 'OCT', '02215', '87    MARK DATA       SHAFT', kind='data', line=343)
# TRUNION
W('42,2263', 0o24220, '', 'OCT', '24220', '88    HALF UNIT SUN OR PLANET VECTOR', kind='data', line=345)
W('42,2264', 0o24223, '', 'OCT', '24223', '89    LANDMARK        LATITUDE', kind='data', line=346)
# LONGITUDE/2
# ALTITUDE
W('42,2265', 0o24226, '', 'OCT', '24226', '90    Y', kind='data', line=349)
# Y DOT
# PSI
W('42,2266', 0o02231, '', 'OCT', '02231', '91    OCDU ANGLES     SHAFT', kind='data', line=352)
# TRUNION
W('42,2267', 0o02234, '', 'OCT', '02234', '92    NEW OPTICS ANGLES SHAFT', kind='data', line=354)
# TRUNION
W('42,2270', 0o04237, '', 'OCT', '04237', '93    DELTA GYRO ANGLES', kind='data', line=356)
W('42,2271', 0o02242, '', 'OCT', '02242', '94    NEW OPTICS ANGLES SHAFT', kind='data', line=357)
# TRUNNION
W('42,2272', 0o04245, '', 'OCT', '04245', '95    PREFERRED ATTITUDE ICDU ANGLES', kind='data', line=359)
W('42,2273', 0o04250, '', 'OCT', '04250', '96    +X-AXIS ATTITUDE ICDU ANGLES', kind='data', line=360)
W('42,2274', 0o04253, '', 'OCT', '04253', '97    SYSTEM TEST INPUTS', kind='data', line=361)
W('42,2275', 0o04256, '', 'OCT', '04256', '98    SYSTEM TEST RESULTS', kind='data', line=362)
W('42,2276', 0o24261, '', 'OCT', '24261', '99    RMS IN POSITION', kind='data', line=363)
# RMS IN VELOCITY
# RMS OPTION
# END OF NNADTAB FOR MIXED NOUNS

# NN    NORMAL NOUNS
# Page 275
W('42,2277', 0o00000, 'NNTYPTAB', 'OCT', '00000', '00    NOT IN USE', kind='data', line=370)
W('42,2300', 0o04040, '', 'OCT', '04040', '01    3COMP FRACTIONAL', kind='data', line=371)
W('42,2301', 0o04140, '', 'OCT', '04140', '02    3COMP WHOLE', kind='data', line=372)
W('42,2302', 0o04102, '', 'OCT', '04102', '03    3COMP CDU DEGREES', kind='data', line=373)
W('42,2303', 0o00000, '', 'OCT', '0', '04    SPARE', kind='data', line=374)
W('42,2304', 0o00504, '', 'OCT', '00504', '05    1COMP DPDEG(360)', kind='data', line=375)
W('42,2305', 0o02000, '', 'OCT', '02000', '06    2COMP OCTAL ONLY', kind='data', line=376)
W('42,2306', 0o04000, '', 'OCT', '04000', '07    3COMP OCTAL ONLY', kind='data', line=377)
W('42,2307', 0o04000, '', 'OCT', '04000', '08    3COMP OCTAL ONLY', kind='data', line=378)
W('42,2310', 0o04000, '', 'OCT', '04000', '09    3COMP OCTAL ONLY', kind='data', line=379)
W('42,2311', 0o00000, '', 'OCT', '00000', '10    1COMP OCTAL ONLY', kind='data', line=380)
W('42,2312', 0o24400, '', 'OCT', '24400', '11    3COMP HMS (DEC ONLY)', kind='data', line=381)
W('42,2313', 0o02000, '', 'OCT', '02000', '12    2COMP OCTAL ONLY', kind='data', line=382)
W('42,2314', 0o24400, '', 'OCT', '24400', '13    3COMP HMS (DEC ONLY)', kind='data', line=383)
W('42,2315', 0o00000, '', 'OCT', '0', '14    SPARE', kind='data', line=384)
W('42,2316', 0o00000, '', 'OCT', '00000', '15    1COMP OCTAL ONLY', kind='data', line=385)
W('42,2317', 0o24400, '', 'OCT', '24400', '16    3COMP HMS (DEC ONLY)', kind='data', line=386)
W('42,2320', 0o04102, '', 'OCT', '04102', '17    3COMP CDU DEG', kind='data', line=387)
W('42,2321', 0o04102, '', 'OCT', '04102', '18    3COMP CDU DEG', kind='data', line=388)
W('42,2322', 0o04102, '', 'OCT', '04102', '19    3COMP CDU DEG', kind='data', line=389)
W('42,2323', 0o04102, '', 'OCT', '04102', '20    3COMP CDU DEGREES', kind='data', line=390)
W('42,2324', 0o04140, '', 'OCT', '04140', '21    3COMP WHOLE', kind='data', line=391)
W('42,2325', 0o04102, '', 'OCT', '04102', '22    3COMP CDU DEGREES', kind='data', line=392)
W('42,2326', 0o00000, '', 'OCT', '00000', '23    SPARE', kind='data', line=393)
W('42,2327', 0o24400, '', 'OCT', '24400', '24    3COMP HMS (DEC ONLY)', kind='data', line=394)
W('42,2330', 0o04140, '', 'OCT', '04140', '25    3COMP WHOLE', kind='data', line=395)
W('42,2331', 0o04000, '', 'OCT', '04000', '26    3COMP OCTAL ONLY', kind='data', line=396)
W('42,2332', 0o00140, '', 'OCT', '00140', '27    1COMP WHOLE', kind='data', line=397)
W('42,2333', 0o00000, '', 'OCT', '00000', '28    SPARE', kind='data', line=398)
W('42,2334', 0o20102, '', 'OCT', '20102', '29    1COMP CDU DEG (DEC ONLY)', kind='data', line=399)
W('42,2335', 0o04140, '', 'OCT', '04140', '30    3COMP WHOLE', kind='data', line=400)
W('42,2336', 0o24400, '', 'OCT', '24400', '31    3COMP HMS (DEC ONLY)', kind='data', line=401)
W('42,2337', 0o24400, '', 'OCT', '24400', '32    3COMP HMS (DEC ONLY)', kind='data', line=402)
W('42,2340', 0o24400, '', 'OCT', '24400', '33    3COMP HMS (DEC ONLY)', kind='data', line=403)
W('42,2341', 0o24400, '', 'OCT', '24400', '34    3COMP HMS (DEC ONLY)', kind='data', line=404)
W('42,2342', 0o24400, '', 'OCT', '24400', '35    3COMP HMS (DEC ONLY)', kind='data', line=405)
W('42,2343', 0o24400, '', 'OCT', '24400', '36    3COMP HMS (DEC ONLY)', kind='data', line=406)
W('42,2344', 0o24400, '', 'OCT', '24400', '37    3COMP HMS (DEC ONLY)', kind='data', line=407)
W('42,2345', 0o24400, '', 'OCT', '24400', '38    3COMP HMS (DEC ONLY)', kind='data', line=408)
W('42,2346', 0o24400, '', 'OCT', '24400', '39    3COMP HMS (DEC ONLY)', kind='data', line=409)
# END OF NNTYPTAB FOR NORMAL NOUNS

# NN    MIXED NOUNS

W('42,2347', 0o24500, '', 'OCT', '24500', '40    3COMP   MIN/SEC, VEL3, VEL3', kind='data', line=414)
# (NO LOAD, DEC ONLY)
W('42,2350', 0o00542, '', 'OCT', '00542', '41    2COMP   CDU DEG, ELEV DEG', kind='data', line=416)
W('42,2351', 0o24410, '', 'OCT', '24410', '42    3COMP   POS4, POS4, VEL3', kind='data', line=417)
# (DEC ONLY)
W('42,2352', 0o20204, '', 'OCT', '20204', '43    3COMP   DPDEG(360), DPDEG(360), POS4', kind='data', line=419)
# Page 276
# (DEC ONLY)
W('42,2353', 0o00410, '', 'OCT', '00410', '44    3COMP   POS4, POS4, MIN/SEC', kind='data', line=422)
# (NO LOAD, DEC ONLY)
W('42,2354', 0o10000, '', 'OCT', '10000', '45    3COMP   2INT, MIN/SEC, DPDEG(360)', kind='data', line=424)
# (NO LOAD, DEC ONLY)
W('42,2355', 0o00000, '', 'OCT', '00000', '46    2COMP   OCTAL ONLY FOR EACH', kind='data', line=426)
W('42,2356', 0o00306, '', 'OCT', '00306', '47    2COMP   WEIGHT2 FOR EACH', kind='data', line=427)
# (DEC ONLY)
W('42,2357', 0o00614, '', 'OCT', '00614', '48    2COMP   TRIM DEG, TRIM DEG', kind='data', line=429)
# (DEC ONLY)
W('42,2360', 0o00510, '', 'OCT', '00510', '49    3COMP   POS4, VEL3, WHOLE', kind='data', line=431)
# (DEC ONLY)
W('42,2361', 0o00417, '', 'OCT', '00417', '50    3COMP   POS6, POS4, MIN/SEC', kind='data', line=433)
# (NO LOAD, DEC ONLY)
W('42,2362', 0o00204, '', 'OCT', '00204', '51    2COMP   DPDEG(360), DPDEG(360)', kind='data', line=435)
# (DEC ONLY)
W('42,2363', 0o00004, '', 'OCT', '00004', '52    1COMP   DPDEG(360)', kind='data', line=437)
W('42,2364', 0o10507, '', 'OCT', '10507', '53    3COMP   POS5, VEL3, DPDEG(360)', kind='data', line=438)
# (DEC ONLY)
W('42,2365', 0o10507, '', 'OCT', '10507', '54    3COMP   POS5, VEL3, DPDEG(360)', kind='data', line=440)
# (DEC ONLY)
W('42,2366', 0o10200, '', 'OCT', '10200', '55    3COMP   WHOLE, DPDEG(360), DPDEG(360)', kind='data', line=442)
# (DEC ONLY)
W('42,2367', 0o00444, '', 'OCT', '00444', '56    2COMP   DPDEG(360), VEL2', kind='data', line=444)
# (DEC ONLY)
W('42,2370', 0o00010, '', 'OCT', '00010', '57    1COMP   POS4', kind='data', line=446)
# (DEC ONLY)
W('42,2371', 0o24510, '', 'OCT', '24510', '58    3COMP   POS4, VEL3, VEL3', kind='data', line=448)
# (DEC ONLY)
W('42,2372', 0o24512, '', 'OCT', '24512', '59    3COMP   VEL3 FOR EACH', kind='data', line=450)
# (DEC ONLY)
W('42,2373', 0o10440, '', 'OCT', '10440', '60    3COMP   WHOLE, VEL2, DPDEG(360)', kind='data', line=452)
# (DEC ONLY)
W('42,2374', 0o00204, '', 'OCT', '00204', '61    3COMP   DPDEG(360), DPDEG(360), WHOLE', kind='data', line=454)
# (DEC ONLY)
W('42,2375', 0o20451, '', 'OCT', '20451', '62    3COMP   VEL2, VEL2, POS4', kind='data', line=456)
# (DEC ONLY)
W('42,2376', 0o00457, '', 'OCT', '00457', '63    3COMP   POS6, VEL2, MIN/SEC', kind='data', line=458)
# (NO LOAD, DEC ONLY)
W('42,2377', 0o36460, '', 'OCT', '36460', '64    3COMP   DRAG ACCEL, VEL2, POS6', kind='data', line=460)
# (DEC ONLY)
W('42,2400', 0o00000, '', 'OCT', '00000', '65    3COMP   HMS (DEC ONLY)', kind='data', line=462)
W('42,2401', 0o37044, '', 'OCT', '37044', '66    3COMP   DPDEG(360), POS8, POS6', kind='data', line=463)
# (DEC ONLY)
W('42,2402', 0o10217, '', 'OCT', '10217', '67    3COMP   POS6, DPDEG(360), DPDEG(360)', kind='data', line=465)
# (DEC ONLY)
W('42,2403', 0o34444, '', 'OCT', '34444', '68    3COMP   DPDEG(360), VEL2, VEL/2VS', kind='data', line=467)
# (DEC ONLY)
W('42,2404', 0o35004, '', 'OCT', '35004', '69    3COMP   DPDEG(360), DRAG ACCEL,VEL/2VS', kind='data', line=469)
# (DEC ONLY)
# Page 277
W('42,2405', 0o00000, '', 'OCT', '00000', '70    3COMP   OCTAL ONLY FOR EACH', kind='data', line=472)
W('42,2406', 0o00000, '', 'OCT', '0', '71    3COMP   OCTAL ONLY FOR EACH', kind='data', line=473)
W('42,2407', 0o00404, '', 'OCT', '00404', '72    3COMP   DPDEG(360), POS4, WHOLE', kind='data', line=474)
# (DEC ONLY)
W('42,2410', 0o10450, '', 'OCT', '10450', '73    3COMP   POS4, VEL2, DPDEG(360)', kind='data', line=476)
W('42,2411', 0o40444, '', 'OCT', '40444', '74    3COMP   DPDEG(360), VEL2, DRAG ACCEL', kind='data', line=477)
W('42,2412', 0o00010, '', 'OCT', '00010', '75    3COMP   POS4, MIN/SEC, MIN/SEC', kind='data', line=478)
# #               (NO LOAD, DEC ONLY)
W('42,2413', 0o00000, '', 'OCT', '0', '76            SPARE', kind='data', line=480)
W('42,2414', 0o00000, '', 'OCT', '0', '77            SPARE', kind='data', line=481)
W('42,2415', 0o00000, '', 'OCT', '0', '78            SPARE', kind='data', line=482)
W('42,2416', 0o00000, '', 'OCT', '0', '79            SPARE', kind='data', line=483)
W('42,2417', 0o22440, '', 'OCT', '22440', '80    3COMP   MIN/SEC, VEL2, VEL2', kind='data', line=484)
# (NO LOAD, DEC ONLY)
W('42,2420', 0o24512, '', 'OCT', '24512', '81    3COMP   VEL3 FOR EACH', kind='data', line=486)
# (DEC ONLY)
W('42,2421', 0o24512, '', 'OCT', '24512', '82    3COMP   VEL3 FOR EACH', kind='data', line=488)
# (DEC ONLY)
W('42,2422', 0o24512, '', 'OCT', '24512', '83    3COMP   VEL3 FOR EACH', kind='data', line=490)
# (DEC ONLY)
W('42,2423', 0o24512, '', 'OCT', '24512', '84    3COMP   VEL3 FOR EACH', kind='data', line=492)
# (DEC ONLY)
W('42,2424', 0o24512, '', 'OCT', '24512', '85    3COMP   VEL3 FOR EACH', kind='data', line=494)
# (DEC ONLY)
W('42,2425', 0o22451, '', 'OCT', '22451', '86    3COMP   VEL2 FOR EACH', kind='data', line=496)
# (DEC ONLY)
W('42,2426', 0o00102, '', 'OCT', '00102', '87    2COMP   CDU DEG, Y OPTICS DEG', kind='data', line=498)
W('42,2427', 0o00000, '', 'OCT', '0', '88    3COMP   FRAC FOR EACH', kind='data', line=499)
# (DEC ONLY)
W('42,2430', 0o16143, '', 'OCT', '16143', '89    3COMP   DPDEG(90), DPDEG(90), POS5', kind='data', line=501)
# (DEC ONLY)
W('42,2431', 0o10507, '', 'OCT', '10507', '90    3COMP   POS5, VEL3, DEPDEG(360)', kind='data', line=503)
# (DEC ONLY)
W('42,2432', 0o00102, '', 'OCT', '00102', '91    2COMP   CDUDEG, YOPTICS DEG', kind='data', line=505)
W('42,2433', 0o00102, '', 'OCT', '00102', '92    2COMP   CDUDEG, YOPTICS DEG', kind='data', line=506)
W('42,2434', 0o06143, '', 'OCT', '06143', '93    3COMP   DPDEG(90) FOR EACH', kind='data', line=507)
W('42,2435', 0o00102, '', 'OCT', '00102', '94    2COMP   CDUDEG, YOPTICS DEG', kind='data', line=508)
W('42,2436', 0o04102, '', 'OCT', '04102', '95    3COMP   CDU DEG FOR EACH', kind='data', line=509)
W('42,2437', 0o04102, '', 'OCT', '04102', '96    3COMP   CDU DEG FOR EACH', kind='data', line=510)
W('42,2440', 0o00000, '', 'OCT', '00000', '97    3COMP   WHOLE FOR EACH', kind='data', line=511)
W('42,2441', 0o00000, '', 'OCT', '00000', '98    3COMP   WHOLE, FRAC, WHOLE', kind='data', line=512)
W('42,2442', 0o01162, '', 'OCT', '01162', '99    3COMP   POS9, VEL4, WHOLE', kind='data', line=513)
# (DEC ONLY)
# END OF NNTYPTAB FOR MIXED NOUNS

W('42,2443', 0o00006, 'SFINTAB', 'OCT', '00006', 'WHOLE, DP TIME (SEC)', kind='data', line=518)
W('42,2444', 0o03240, '', 'OCT', '03240', kind='data', line=519)
W('42,2445', 0o00000, '', 'OCT', '00000', 'SPARE', kind='data', line=520)
W('42,2446', 0o00000, '', 'OCT', '00000', kind='data', line=521)
# Page 278
W('42,2447', 0o00000, '', 'OCT', '00000', 'CDU DEGREES, Y OPTICS DEGREES', kind='data', line=523)
W('42,2450', 0o00000, '', 'OCT', '00000', '      (SFCONS IN DEGINSF, OPTDEGIN)', kind='data', line=524)
W('42,2451', 0o10707, '', 'OCT', '10707', 'DP DEGREES (90)', kind='data', line=525)
W('42,2452', 0o03435, '', 'OCT', '03435', '      UPPED BY 1', kind='data', line=526)
W('42,2453', 0o13070, '', 'OCT', '13070', 'DP DEGREES (360)(POINT BETWN BITS 11-12)', kind='data', line=527)
W('42,2454', 0o34345, '', 'OCT', '34345', '      UPPED BY 1', kind='data', line=528)
W('42,2455', 0o00005, '', 'OCT', '00005', 'DEGREES (180)', kind='data', line=529)
W('42,2456', 0o21616, '', 'OCT', '21616', kind='data', line=530)
W('42,2457', 0o26113, '', 'OCT', '26113', 'WEIGHT2', kind='data', line=531)
W('42,2460', 0o31713, '', 'OCT', '31713', kind='data', line=532)
W('42,2461', 0o00070, '', 'OCT', '00070', 'POSITION5', kind='data', line=533)
W('42,2462', 0o20460, '', 'OCT', '20460', kind='data', line=534)
W('42,2463', 0o01065, '', 'OCT', '01065', 'POSITION4', kind='data', line=535)
W('42,2464', 0o05740, '', 'OCT', '05740', kind='data', line=536)
W('42,2465', 0o11414, '', 'OCT', '11414', 'VELOCITY2     (POINT BETWN BITS 11-12)', kind='data', line=537)
W('42,2466', 0o31463, '', 'OCT', '31463', kind='data', line=538)
W('42,2467', 0o07475, '', 'OCT', '07475', 'VELOCITY3', kind='data', line=539)
W('42,2470', 0o16051, '', 'OCT', '16051', kind='data', line=540)
W('42,2471', 0o00001, '', 'OCT', '00001', 'ELEVATION DEGREES', kind='data', line=541)
W('42,2472', 0o03434, '', 'OCT', '03434', kind='data', line=542)
W('42,2473', 0o00002, '', 'OCT', '00002', 'TRIM DEGREES', kind='data', line=543)
W('42,2474', 0o22245, '', 'OCT', '22245', kind='data', line=544)
W('42,2475', 0o00014, '', 'OCT', '00014', 'INERTIA, THRUST MOMENT', kind='data', line=545)
W('42,2476', 0o35607, '', 'OCT', '35607', kind='data', line=546)
W('42,2477', 0o07606, '', 'OCT', '07606', 'VELOCITY/2VS', kind='data', line=547)
W('42,2500', 0o06300, '', 'OCT', '06300', kind='data', line=548)
W('42,2501', 0o16631, '', 'OCT', '16631', 'POSITION 6', kind='data', line=549)
W('42,2502', 0o11307, '', 'OCT', '11307', kind='data', line=550)
W('42,2503', 0o12000, '', 'OCT', '12000', 'DRAG ACCELERATION (POINT BETWN BITS 7-8)', kind='data', line=551)
W('42,2504', 0o00000, '', 'OCT', '00000', kind='data', line=552)
W('42,2505', 0o27176, '', 'OCT', '27176', 'POSITION 8', kind='data', line=553)
W('42,2506', 0o14235, '', 'OCT', '14235', kind='data', line=554)
W('42,2507', 0o01670, '', '2DEC', '30480 B-19', 'POSITION 9', kind='data', line=555)
W('42,2510', 0o20000, kind='data', line=555)

W('42,2511', 0o07475, '', '2DEC', '30.48 B-7', 'VELOCITY4', kind='data', line=557)
W('42,2512', 0o16051, kind='data', line=557)

# END OF SFINTAB

W('42,2513', 0o05174, 'SFOUTAB', 'OCT', '05174', 'WHOLE, DP TIME (SEC)', kind='data', line=562)
W('42,2514', 0o13261, '', 'OCT', '13261', kind='data', line=563)
W('42,2515', 0o00000, '', 'OCT', '00000', 'SPARE', kind='data', line=564)
W('42,2516', 0o00000, '', 'OCT', '00000', kind='data', line=565)
W('42,2517', 0o00000, '', 'OCT', '00000', 'CDU DEGREES, Y OPTICS DEGREES', kind='data', line=566)
W('42,2520', 0o00000, '', 'OCT', '00000', '      (SFCONS IN DEGOUTSF, OPTDEGOUT)', kind='data', line=567)
W('42,2521', 0o00714, '', 'OCT', '00714', 'DP DEGREES (90) (POINT BETWN BITS 7-8)', kind='data', line=568)
W('42,2522', 0o31463, '', 'OCT', '31463', kind='data', line=569)
W('42,2523', 0o13412, '', 'OCT', '13412', 'DP DEGREES (360)', kind='data', line=570)
W('42,2524', 0o07534, '', 'OCT', '07534', kind='data', line=571)
W('42,2525', 0o05605, '', 'OCT', '05605', 'DEGREES (180)', kind='data', line=572)
# Page 279
W('42,2526', 0o03656, '', 'OCT', '03656', kind='data', line=574)
W('42,2527', 0o00001, '', 'OCT', '00001', 'WEIGHT2', kind='data', line=575)
W('42,2530', 0o16170, '', 'OCT', '16170', kind='data', line=576)
W('42,2531', 0o00441, '', 'OCT', '00441', 'POSITION5', kind='data', line=577)
W('42,2532', 0o34306, '', 'OCT', '34306', kind='data', line=578)
W('42,2533', 0o07176, '', 'OCT', '07176', 'POSITION4', kind='data', line=579)
W('42,2534', 0o21603, '', 'OCT', '21603', kind='data', line=580)
W('42,2535', 0o15340, '', 'OCT', '15340', 'VELOCITY2', kind='data', line=581)
W('42,2536', 0o15340, '', 'OCT', '15340', kind='data', line=582)
W('42,2537', 0o01031, '', 'OCT', '01031', 'VELOCITY3     (POINT BETWN BITS 7-8)', kind='data', line=583)
W('42,2540', 0o21032, '', 'OCT', '21032', kind='data', line=584)
W('42,2541', 0o34631, '', 'OCT', '34631', 'ELEVATION DEGREES', kind='data', line=585)
W('42,2542', 0o23146, '', 'OCT', '23146', kind='data', line=586)
W('42,2543', 0o14340, '', 'OCT', '14340', 'TRIM DEGREES', kind='data', line=587)
W('42,2544', 0o24145, '', 'OCT', '24145', kind='data', line=588)
W('42,2545', 0o02363, '', 'OCT', '02363', 'INERTIA, THRUST MOMENT', kind='data', line=589)
W('42,2546', 0o03721, '', 'OCT', '03721', kind='data', line=590)
W('42,2547', 0o20373, '', 'OCT', '20373', 'VELOCITY/ZVS', kind='data', line=591)
W('42,2550', 0o02122, '', 'OCT', '02122', kind='data', line=592)
W('42,2551', 0o00424, '', 'OCT', '00424', 'POSITION 6    (POINT BETWN BITS 7-8)', kind='data', line=593)
W('42,2552', 0o30446, '', 'OCT', '30446', kind='data', line=594)
W('42,2553', 0o00631, '', 'OCT', '00631', 'DRAG ACCELERATION', kind='data', line=595)
W('42,2554', 0o23146, '', 'OCT', '23146', kind='data', line=596)
W('42,2555', 0o00260, '', 'OCT', '00260', 'POSITION 8', kind='data', line=597)
W('42,2556', 0o06213, '', 'OCT', '06213', kind='data', line=598)
W('42,2557', 0o04231, '', '2DEC', '17.2010499 B-7', 'POSITION 9', kind='data', line=599)
W('42,2560', 0o27400, kind='data', line=599)

W('42,2561', 0o01031, '', '2DEC', '.032808399', 'VELOCITY4', kind='data', line=601)
W('42,2562', 0o21032, kind='data', line=601)

# END OF SFOUTAB

# NN     SF CONSTANT            SF ROUTINE

W('42,2563', 0o03660, 'IDADDTAB', 'ECADR', 'TTOGO', '40    MIN/SEC                 M/S', kind='data', line=608)
W('42,2564', 0o03772, '', 'ECADR', 'VGDISP', '40    VEL3                    DP3', kind='data', line=609)
W('42,2565', 0o03425, '', 'ECADR', 'DVTOTAL', '40    VEL3                    DP3', kind='data', line=610)
W('42,2566', 0o01045, '', 'ECADR', 'DSPTEM1', '41    CDU DEG                 CDU', kind='data', line=611)
W('42,2567', 0o01046, '', 'ECADR', 'DSPTEM1 +1', '41    ELEV DEG                ARTH', kind='data', line=612)
W('42,2570', 0o00000, '', 'OCT', '0', '41    SPARE COMPONENT', kind='data', line=613)
W('42,2571', 0o02363, '', 'ECADR', 'HAPO', '42    POS4                    DP3', kind='data', line=614)
W('42,2572', 0o02365, '', 'ECADR', 'HPER', '42    POS4                    DP3', kind='data', line=615)
W('42,2573', 0o03772, '', 'ECADR', 'VGDISP', '42    VEL3                    DP3', kind='data', line=616)
W('42,2574', 0o01103, '', 'ECADR', 'LAT', '43    DPDEG(360)              DP4', kind='data', line=617)
W('42,2575', 0o01105, '', 'ECADR', 'LONG', '43    DPDEG(360)              DP4', kind='data', line=618)
W('42,2576', 0o01107, '', 'ECADR', 'ALT', '43    POS4                    DP3', kind='data', line=619)
W('42,2577', 0o02351, '', 'ECADR', 'HAPOX', '44    POS4                    DP3', kind='data', line=620)
W('42,2600', 0o02353, '', 'ECADR', 'HPERX', '44    POS4                    DP3', kind='data', line=621)
W('42,2601', 0o02343, '', 'ECADR', 'TFF', '44    MIN/SEC                 M/S', kind='data', line=622)
W('42,2602', 0o01125, '', 'ECADR', 'VHFCNT', '45    2INT                    2INT', kind='data', line=623)
# Page 280
W('42,2603', 0o03660, '', 'ECADR', 'TTOGO', '45    MIN/SEC                 M/S', kind='data', line=625)
W('42,2604', 0o03625, '', 'ECADR', '+MGA', '45    DPDEG(360)              DP4', kind='data', line=626)
W('42,2605', 0o03066, '', 'ECADR', 'DAPDATR1', '46    OCTAL ONLY              OCT', kind='data', line=627)
W('42,2606', 0o03067, '', 'ECADR', 'DAPDATR2', '46    OCATAL ONLY             OCT', kind='data', line=628)
W('42,2607', 0o00000, '', 'OCT', '0', '46    SPARE COMPONENT', kind='data', line=629)
W('42,2610', 0o03074, '', 'ECADR', 'CSMMASS', '47    WEIGHT2                 ARTH1', kind='data', line=630)
W('42,2611', 0o03073, '', 'ECADR', 'LEMMASS', '47    WEIGHT2                 ARTH1', kind='data', line=631)
W('42,2612', 0o00000, '', 'OCT', '00000', '47    SPARE COMPONENT', kind='data', line=632)
W('42,2613', 0o03023, '', 'ECADR', 'PACTOFF', '48    TRIM DEG                ARTH', kind='data', line=633)
W('42,2614', 0o03024, '', 'ECADR', 'YACTOFF', '48    TRIM DEG                ARTH', kind='data', line=634)
W('42,2615', 0o00000, '', 'OCT', '00000', '48    SPARE COMPONENT', kind='data', line=635)
W('42,2616', 0o03501, '', 'ECADR', 'N49DISP', '49    POS4                    DP3', kind='data', line=636)
W('42,2617', 0o03503, '', 'ECADR', 'N49DISP +2', '49    VEL3                    DP3', kind='data', line=637)
W('42,2620', 0o03505, '', 'ECADR', 'N49DISP +4', '49    WHOLE                   ARTH', kind='data', line=638)
W('42,2621', 0o02355, '', 'ECADR', 'RSP-RREC', '50    POS6                    DP3', kind='data', line=639)
W('42,2622', 0o02353, '', 'ECADR', 'HPERX', '50    POS4                    DP3', kind='data', line=640)
W('42,2623', 0o02343, '', 'ECADR', 'TFF', '50    MIN/SEC                 M/S', kind='data', line=641)
W('42,2624', 0o02320, '', 'ECADR', 'RHOSB', '51    DPDEG(360)', kind='data', line=642)
W('42,2625', 0o02322, '', 'ECADR', 'GAMMASB', '51    DPDEG(360)              DP4', kind='data', line=643)
W('42,2626', 0o00000, '', 'OCT', '0', '51    SPARE COMPONENT', kind='data', line=644)
W('42,2627', 0o02632, '', 'ECADR', 'ACTCENT', '52    DPDEG(360)              DP4', kind='data', line=645)
W('42,2630', 0o00000, '', 'OCT', '00000', '52    SPARE COMPONENT', kind='data', line=646)
W('42,2631', 0o00000, '', 'OCT', '00000', '52    SPARE COMPONENT', kind='data', line=647)
W('42,2632', 0o02320, '', 'ECADR', 'RANGE', '53    POS5                    DP1', kind='data', line=648)
W('42,2633', 0o02322, '', 'ECADR', 'RRATE', '53    VEL3                    DP3', kind='data', line=649)
W('42,2634', 0o02324, '', 'ECADR', 'RTHETA', '53    DPDEG(360)              DP4', kind='data', line=650)
W('42,2635', 0o02320, '', 'ECADR', 'RANGE', '54    POS5                    DP1', kind='data', line=651)
W('42,2636', 0o02322, '', 'ECADR', 'RRATE', '54    VEL3                    DP3', kind='data', line=652)
W('42,2637', 0o02324, '', 'ECADR', 'RTHETA', '54    DPDEG(360)              DP4', kind='data', line=653)
W('42,2640', 0o03765, '', 'ECADR', 'NN1', '55    WHOLE                   ARTH', kind='data', line=654)
W('42,2641', 0o03743, '', 'ECADR', 'ELEV', '55    DPDEG(360)              DP4', kind='data', line=655)
W('42,2642', 0o03753, '', 'ECADR', 'CENTANG', '55    DPDEG(360)              DP4', kind='data', line=656)
W('42,2643', 0o03633, '', 'ECADR', 'RTEGAM2D', '56    DPDEG(360)              DP4', kind='data', line=657)
W('42,2644', 0o03631, '', 'ECADR', 'RTEDVD', '56    VEL2                    DP4', kind='data', line=658)
W('42,2645', 0o00000, '', 'OCT', '0', '56    SPARE COMPONENT', kind='data', line=659)
W('42,2646', 0o02610, '', 'ECADR', 'DELTAR', '57    POS4                    DP3', kind='data', line=660)
W('42,2647', 0o00000, '', 'OCT', '0', '57    SPARE COMPONENT', kind='data', line=661)
W('42,2650', 0o00000, '', 'OCT', '0', '57    SPARE COMPONENT', kind='data', line=662)
W('42,2651', 0o02640, '', 'ECADR', 'POSTTPI', '58    POS4                    DP3', kind='data', line=663)
W('42,2652', 0o02634, '', 'ECADR', 'DELVTPI', '58    VEL3                    DP3', kind='data', line=664)
W('42,2653', 0o02636, '', 'ECADR', 'DELVTPF', '58    VEL3                    DP3', kind='data', line=665)
W('42,2654', 0o02610, '', 'ECADR', 'DVLOS', '59    VEL3                    DP3', kind='data', line=666)
W('42,2655', 0o02612, '', 'ECADR', 'DVLOS +2', '59    VEL3                    DP3', kind='data', line=667)
W('42,2656', 0o02614, '', 'ECADR', 'DVLOS +4', '59    VEL3                    DP3', kind='data', line=668)
W('42,2657', 0o03721, '', 'ECADR', 'GMAX', '60    WHOLE                   ARTH', kind='data', line=669)
W('42,2660', 0o03766, '', 'ECADR', 'VPRED', '60    VEL2                    DP4', kind='data', line=670)
W('42,2661', 0o03770, '', 'ECADR', 'GAMMAEI', '60    DPDEG(360)              DP4', kind='data', line=671)
W('42,2662', 0o03400, '', 'ECADR', 'LAT(SPL)', '61    DPDEG(360)              DP4', kind='data', line=672)
W('42,2663', 0o03402, '', 'ECADR', 'LNG(SPL)', '61    DPDEG(360)              DP4', kind='data', line=673)
W('42,2664', 0o03326, '', 'ECADR', 'HEADSUP', '61    WHOLE                   ARTH', kind='data', line=674)
# Page 281
W('42,2665', 0o03722, '', 'ECADR', 'VMAGI', '62    VEL2                    DP4', kind='data', line=676)
W('42,2666', 0o03736, '', 'ECADR', 'HDOT', '62    VEL2                    DP4', kind='data', line=677)
W('42,2667', 0o03734, '', 'ECADR', 'ALTI', '62    POS4                    DP3', kind='data', line=678)
W('42,2670', 0o03713, '', 'ECADR', 'RTGO', '63    POS6                    DP3', kind='data', line=679)
W('42,2671', 0o03724, '', 'ECADR', 'VIO', '63    VEL2                    DP4', kind='data', line=680)
W('42,2672', 0o03726, '', 'ECADR', 'TTE', '63    MIN/SEC                 M/S', kind='data', line=681)
W('42,2673', 0o03637, '', 'ECADR', 'D', '64    DRAG ACCEL              DP2', kind='data', line=682)
W('42,2674', 0o03722, '', 'ECADR', 'VMAGI', '64    VEL2                    DP4', kind='data', line=683)
W('42,2675', 0o03713, '', 'ECADR', 'RTGON64', '64    POS6                    DP3', kind='data', line=684)
W('42,2676', 0o00013, '', 'ECADR', 'SAMPTIME', '65    HMS (MIXED ONLY TO KEEP CODE 65) HMS', kind='data', line=685)
W('42,2677', 0o00013, '', 'ECADR', 'SAMPTIME', '65    HMS                     HMS', kind='data', line=686)
W('42,2700', 0o00013, '', 'ECADR', 'SAMPTIME', '65    HMS                     HMS', kind='data', line=687)
W('42,2701', 0o03315, '', 'ECADR', 'ROLLC', '66    DPDEG(360)              DP4', kind='data', line=688)
W('42,2702', 0o03675, '', 'ECADR', 'XRNGERR', '66    POS8                    DP3', kind='data', line=689)
W('42,2703', 0o03715, '', 'ECADR', 'DNRNGERR', '66    POS6                    DP3', kind='data', line=690)
W('42,2704', 0o03713, '', 'ECADR', 'RTGON67', '67    POS6                    DP3', kind='data', line=691)
W('42,2705', 0o01103, '', 'ECADR', 'LAT', '67    DPDEG(360)              DP4', kind='data', line=692)
W('42,2706', 0o01105, '', 'ECADR', 'LONG', '67    DPDEG(360)              DP4', kind='data', line=693)
W('42,2707', 0o03315, '', 'ECADR', 'ROLLC', '68    DPDEG(360)              DP4', kind='data', line=694)
W('42,2710', 0o03722, '', 'ECADR', 'VMAGI', '68    VEL2                    DP4', kind='data', line=695)
W('42,2711', 0o03677, '', 'ECADR', 'RDOT', '68    VEL/2VS                 DP4', kind='data', line=696)
W('42,2712', 0o03315, '', 'ECADR', 'ROLLC', '69    DPDEG(360)              DP4', kind='data', line=697)
W('42,2713', 0o03174, '', 'ECADR', 'Q7', '69    DRAG ACCEL              DP2', kind='data', line=698)
W('42,2714', 0o03766, '', 'ECADR', 'VL', '69    VEL/2VS                 DP4', kind='data', line=699)
W('42,2715', 0o00735, '', 'ECADR', 'STARCODE', '70    OCTAL ONLY              OCT', kind='data', line=700)
W('42,2716', 0o02751, '', 'ECADR', 'LANDMARK', '70    OCTAL ONLY              OCT', kind='data', line=701)
W('42,2717', 0o02752, '', 'ECADR', 'HORIZON', '70    OCTAL ONLY              OCT', kind='data', line=702)
W('42,2720', 0o00735, '', 'ECADR', 'STARCODE', '71    OCTAL ONLY              OCT', kind='data', line=703)
W('42,2721', 0o02751, '', 'ECADR', 'LANDMARK', '71    OCTAL ONLY              OCT', kind='data', line=704)
W('42,2722', 0o02752, '', 'ECADR', 'HORIZON', '71    OCTAL ONLY              OCT', kind='data', line=705)
W('42,2723', 0o02616, '', 'ECADR', 'THETZERO', '72    DPDEG(360)              DP4', kind='data', line=706)
W('42,2724', 0o03753, '', 'ECADR', 'DELHITE', '72    POS4                    DP3', kind='data', line=707)
W('42,2725', 0o01132, '', 'ECADR', 'OPTION2', '72    WHOLE                   ARTH', kind='data', line=708)
W('42,2726', 0o03620, '', 'ECADR', 'P21ALT', '73    POS4                    DP3', kind='data', line=709)
W('42,2727', 0o03622, '', 'ECADR', 'P21VEL', '73    VEL2                    DP4', kind='data', line=710)
W('42,2730', 0o03624, '', 'ECADR', 'P21GAM', '73    DPDEG(360)              DP4', kind='data', line=711)
W('42,2731', 0o03315, '', 'ECADR', 'ROLLC', '74    DPDEG(360)              DP4', kind='data', line=712)
W('42,2732', 0o03722, '', 'ECADR', 'VMAGI', '74    VEL2                    DP4', kind='data', line=713)
W('42,2733', 0o03637, '', 'ECADR', 'D', '74    DRAG ACCEL              DP2', kind='data', line=714)
W('42,2734', 0o02632, '', 'ECADR', 'DIFFALT', '75    POS4                    DP3', kind='data', line=715)
W('42,2735', 0o02546, '', 'ECADR', 'T1TOT2', '75    MIN/SEC                 M/S', kind='data', line=716)
W('42,2736', 0o03655, '', 'ECADR', 'T2TOT3', '75    MIN/SEC                 M/S', kind='data', line=717)
W('42,2737', 0o00000, '', 'OCT', '0', '76    SPARE', kind='data', line=718)
W('42,2740', 0o00000, '', 'OCT', '0', '76    SPARE', kind='data', line=719)
W('42,2741', 0o00000, '', 'OCT', '0', '76    SPARE', kind='data', line=720)
W('42,2742', 0o00000, '', 'OCT', '0', '77    SPARE', kind='data', line=721)
W('42,2743', 0o00000, '', 'OCT', '0', '77    SPARE', kind='data', line=722)
W('42,2744', 0o00000, '', 'OCT', '0', '77    SPARE', kind='data', line=723)
W('42,2745', 0o00000, '', 'OCT', '0', '78    SPARE', kind='data', line=724)
W('42,2746', 0o00000, '', 'OCT', '0', '78    SPARE', kind='data', line=725)
# Page 282
W('42,2747', 0o00000, '', 'OCT', '0', '78    SPARE', kind='data', line=727)
W('42,2750', 0o00000, '', 'OCT', '0', '79    SPARE', kind='data', line=728)
W('42,2751', 0o00000, '', 'OCT', '0', '79    SPARE', kind='data', line=729)
W('42,2752', 0o00000, '', 'OCT', '0', '79    SPARE', kind='data', line=730)
W('42,2753', 0o03660, '', 'ECADR', 'TTOGO', '80    MIN/SEC                 M/S', kind='data', line=731)
W('42,2754', 0o03772, '', 'ECADR', 'VGDISP', '80    VEL2                    DP4', kind='data', line=732)
W('42,2755', 0o03425, '', 'ECADR', 'DVTOTAL', '80    VEL2                    DP4', kind='data', line=733)
W('42,2756', 0o03404, '', 'ECADR', 'DELVLVC', '81    VEL3                    DP3', kind='data', line=734)
W('42,2757', 0o03406, '', 'ECADR', 'DELVLVC +2', '81    VEL3                    DP3', kind='data', line=735)
W('42,2760', 0o03410, '', 'ECADR', 'DELVLVC +4', '81    VEL3                    DP3', kind='data', line=736)
W('42,2761', 0o03404, '', 'ECADR', 'DELVLVC', '82    VEL3                    DP3', kind='data', line=737)
W('42,2762', 0o03406, '', 'ECADR', 'DELVLVC +2', '82    VEL3                    DP3', kind='data', line=738)
W('42,2763', 0o03410, '', 'ECADR', 'DELVLVC +4', '82    VEL3                    DP3', kind='data', line=739)
W('42,2764', 0o03674, '', 'ECADR', 'DELVIMU', '83    VEL3                    DP3', kind='data', line=740)
W('42,2765', 0o03676, '', 'ECADR', 'DELVIMU +2', '83    VEL3                    DP3', kind='data', line=741)
W('42,2766', 0o03700, '', 'ECADR', 'DELVIMU +4', '83    VEL3                    DP3', kind='data', line=742)
W('42,2767', 0o03537, '', 'ECADR', 'DELVOV', '84    VEL3                    DP3', kind='data', line=743)
W('42,2770', 0o03541, '', 'ECADR', 'DELVOV +2', '84    VEL3                    DP3', kind='data', line=744)
W('42,2771', 0o03543, '', 'ECADR', 'DELVOV +4', '84    VEL3                    DP3', kind='data', line=745)
W('42,2772', 0o03664, '', 'ECADR', 'VGBODY', '85    VEL3                    DP3', kind='data', line=746)
W('42,2773', 0o03666, '', 'ECADR', 'VGBODY +2', '85    VEL3                    DP3', kind='data', line=747)
W('42,2774', 0o03670, '', 'ECADR', 'VGBODY +4', '85    VEL3                    DP3', kind='data', line=748)
W('42,2775', 0o03404, '', 'ECADR', 'DELVLVC', '86    VEL2                    DP4', kind='data', line=749)
W('42,2776', 0o03406, '', 'ECADR', 'DELVLVC +2', '86    VEL2                    DP4', kind='data', line=750)
W('42,2777', 0o03410, '', 'ECADR', 'DELVLVC +4', '86    VEL2                    DP4', kind='data', line=751)
W('42,3000', 0o03730, '', 'ECADR', 'MRKBUF1 +3', '87    CDU DEG                 CDU', kind='data', line=752)
W('42,3001', 0o03732, '', 'ECADR', 'MRKBUF1 +5', '87    Y OPTICS DEG            YOPT', kind='data', line=753)
W('42,3002', 0o00000, '', 'OCT', '0', '87    SPARE COMPONENT', kind='data', line=754)
W('42,3003', 0o03704, '', 'ECADR', 'STARSAV3', '88    DPFRAC                DPFRAC', kind='data', line=755)
W('42,3004', 0o03706, '', 'ECADR', 'STARSAV3 +2', '88    DPFRAC                DPFRAC', kind='data', line=756)
W('42,3005', 0o03710, '', 'ECADR', 'STARSAV3 +4', '88    DPFRAC                DPFRAC', kind='data', line=757)
W('42,3006', 0o01103, '', 'ECADR', 'LANDLAT', '89    DPDEG(90)               DP3', kind='data', line=758)
W('42,3007', 0o02357, '', 'ECADR', 'LANDLONG', '89    DPDEG(90)               DP3', kind='data', line=759)
W('42,3010', 0o02361, '', 'ECADR', 'LANDALT', '89    POS5                    DP1', kind='data', line=760)
W('42,3011', 0o02320, '', 'ECADR', 'RANGE', '90    POS5                    DP1', kind='data', line=761)
W('42,3012', 0o02322, '', 'ECADR', 'RRATE', '90    VEL3                    DP3', kind='data', line=762)
W('42,3013', 0o02324, '', 'ECADR', 'RTHETA', '90    DPDEG(360)              DP4', kind='data', line=763)
W('42,3014', 0o00036, '', 'ECADR', 'CDUS', '91    CDU DEG                 CDU', kind='data', line=764)
W('42,3015', 0o00035, '', 'ECADR', 'CDUT', '91    Y OPTICS DEG            YOPT', kind='data', line=765)
W('42,3016', 0o00000, '', 'OCT', '0', '91    SPARE COMPONENT', kind='data', line=766)
W('42,3017', 0o02773, '', 'ECADR', 'SAC', '92    CDU DEG                 CDU', kind='data', line=767)
W('42,3020', 0o02775, '', 'ECADR', 'PAC', '92    Y OPTICS DEG            YOPT', kind='data', line=768)
W('42,3021', 0o00000, '', 'OCT', '0', '92    SPARE COMPONENT', kind='data', line=769)
W('42,3022', 0o02757, '', 'ECADR', 'OGC', '93    DPDEG(90)               DP3', kind='data', line=770)
W('42,3023', 0o02761, '', 'ECADR', 'OGC +2', '93    DPDEG(90)               DP3', kind='data', line=771)
W('42,3024', 0o02763, '', 'ECADR', 'OGC +4', '93    DPDEG(90)               DP3', kind='data', line=772)
W('42,3025', 0o03730, '', 'ECADR', 'MRKBUF1 +3', '94    CDU DEG                 CDU', kind='data', line=773)
W('42,3026', 0o03732, '', 'ECADR', 'MRKBUF1 +5', '94    Y OPTICS DEG            YOPT', kind='data', line=774)
W('42,3027', 0o00000, '', 'OCT', '00000', '94    SPARE', kind='data', line=775)
W('42,3030', 0o03722, '', 'ECADR', 'PRAXIS', '95    CDU DEG                 CDU', kind='data', line=776)
# Page 283
W('42,3031', 0o03723, '', 'ECADR', 'PRAXIS +1', '95    CDU DEG                 CDU', kind='data', line=778)
W('42,3032', 0o03724, '', 'ECADR', 'PRAXIS +2', '95    CDU DEG                 CDU', kind='data', line=779)
W('42,3033', 0o01333, '', 'ECADR', 'CPHIX', '96    CDU DEG                 CDU', kind='data', line=780)
W('42,3034', 0o01334, '', 'ECADR', 'CPHIX +1', '96    CDU DEG                 CDU', kind='data', line=781)
W('42,3035', 0o01335, '', 'ECADR', 'CPHIX +2', '96    CDU DEG                 CDU', kind='data', line=782)
W('42,3036', 0o01045, '', 'ECADR', 'DSPTEM1', '97    WHOLE                   ARTH', kind='data', line=783)
W('42,3037', 0o01046, '', 'ECADR', 'DSPTEM1 +1', '97    WHOLE                   ARTH', kind='data', line=784)
W('42,3040', 0o01047, '', 'ECADR', 'DSPTEM1 +2', '97    WHOLE                   ARTH', kind='data', line=785)
W('42,3041', 0o01050, '', 'ECADR', 'DSPTEM2', '98    WHOLE                   ARTH', kind='data', line=786)
W('42,3042', 0o01051, '', 'ECADR', 'DSPTEM2 +1', '98    FRAC                    FRAC', kind='data', line=787)
W('42,3043', 0o01052, '', 'ECADR', 'DSPTEM2 +2', '98    WHOLE                   ARTH', kind='data', line=788)
W('42,3044', 0o02320, '', 'ECADR', 'WWPOS', '99    POS9                    DP3', kind='data', line=789)
W('42,3045', 0o02322, '', 'ECADR', 'WWVEL', '99    VEL4                    DP2', kind='data', line=790)
W('42,3046', 0o02324, '', 'ECADR', 'WWOPT', '99    WHOLE                   ARTH', kind='data', line=791)
# END OF IDADDTAB

# NN    SF ROUTINES

W('42,3047', 0o16351, 'RUTMXTAB', 'OCT', '16351', '40    M/S, DP3, DP3', kind='data', line=797)
W('42,3050', 0o00142, '', 'OCT', '00142', '41    CDU, ARTH', kind='data', line=798)
W('42,3051', 0o16347, '', 'OCT', '16347', '42    DP3, DP3, DP3', kind='data', line=799)
W('42,3052', 0o16512, '', 'OCT', '16512', '43    DP4, DP4, DP3', kind='data', line=800)
W('42,3053', 0o22347, '', 'OCT', '22347', '44    DP3, DP3, M/S', kind='data', line=801)
W('42,3054', 0o24454, '', 'OCT', '24454', '45    2INT, M/S, DP4', kind='data', line=802)
W('42,3055', 0o00000, '', 'OCT', '00000', '46    OCT, OCT', kind='data', line=803)
W('42,3056', 0o00553, '', 'OCT', '00553', '47    ARITH1, ARITH1', kind='data', line=804)
W('42,3057', 0o00143, '', 'OCT', '00143', '48    ARTH, ARTH', kind='data', line=805)
W('42,3060', 0o06347, '', 'OCT', '06347', '49    DP3, DP3, ARTH', kind='data', line=806)
W('42,3061', 0o22347, '', 'OCT', '22347', '50    DP3, DP3, M/S', kind='data', line=807)
W('42,3062', 0o00512, '', 'OCT', '00512', '51    DP4, DP4', kind='data', line=808)
W('42,3063', 0o00012, '', 'OCT', '00012', '52    DP4', kind='data', line=809)
W('42,3064', 0o24344, '', 'OCT', '24344', '53    DP1, DP3, DP4', kind='data', line=810)
W('42,3065', 0o24344, '', 'OCT', '24344', '54    DP1, DP3, DP4', kind='data', line=811)
W('42,3066', 0o24503, '', 'OCT', '24503', '55    ARTH, DP4 , DP4', kind='data', line=812)
W('42,3067', 0o00512, '', 'OCT', '00512', '56    DP4, DP4', kind='data', line=813)
W('42,3070', 0o00007, '', 'OCT', '00007', '57    DP3', kind='data', line=814)
W('42,3071', 0o16347, '', 'OCT', '16347', '58    DP3, DP3, DP3', kind='data', line=815)
W('42,3072', 0o16347, '', 'OCT', '16347', '59    DP3, DP3, DP3', kind='data', line=816)
W('42,3073', 0o24503, '', 'OCT', '24503', '60    ARTH, DP4, DP4', kind='data', line=817)
W('42,3074', 0o06512, '', 'OCT', '06512', '61    DP4, DP4, ARTH', kind='data', line=818)
W('42,3075', 0o16512, '', 'OCT', '16512', '62    DP4, DP4, DP3', kind='data', line=819)
W('42,3076', 0o22507, '', 'OCT', '22507', '63    DP3, DP4, M/S', kind='data', line=820)
W('42,3077', 0o16505, '', 'OCT', '16505', '64    DP2, DP4, DP3', kind='data', line=821)
W('42,3100', 0o20410, '', 'OCT', '20410', '65    HMS, HMS, HMS', kind='data', line=822)
W('42,3101', 0o16352, '', 'OCT', '16352', '66    DP4, DP3, DP3', kind='data', line=823)
W('42,3102', 0o24507, '', 'OCT', '24507', '67    DP3, DP4, DP4', kind='data', line=824)
W('42,3103', 0o24512, '', 'OCT', '24512', '68    DP4, DP4, DP4', kind='data', line=825)
W('42,3104', 0o24252, '', 'OCT', '24252', '69    DP4, DP2, DP4', kind='data', line=826)
W('42,3105', 0o00000, '', 'OCT', '00000', '70    OCT, OCT, OCT', kind='data', line=827)
# Page 284
W('42,3106', 0o00000, '', 'OCT', '0', '71    OCT, OCT, OCT', kind='data', line=829)
W('42,3107', 0o06352, '', 'OCT', '06352', '72    DP4, DP3, ARTH', kind='data', line=830)
W('42,3110', 0o24507, '', 'OCT', '24507', '73    DPR, DP4, DP4', kind='data', line=831)
W('42,3111', 0o12512, '', 'OCT', '12512', '74    DP4, DP4, DP2', kind='data', line=832)
W('42,3112', 0o22447, '', 'OCT', '22447', '75    DP3, M/S, M/S', kind='data', line=833)
W('42,3113', 0o00000, '', 'OCT', '0', '76    SPARE', kind='data', line=834)
W('42,3114', 0o00000, '', 'OCT', '0', '77    SPARE', kind='data', line=835)
W('42,3115', 0o00000, '', 'OCT', '0', '78    SPARE', kind='data', line=836)
W('42,3116', 0o00000, '', 'OCT', '0', '79    SPARE', kind='data', line=837)
W('42,3117', 0o24511, '', 'OCT', '24511', '80    M/S, DP4, DP4', kind='data', line=838)
W('42,3120', 0o16347, '', 'OCT', '16347', '81    DP3, DP3, DP3', kind='data', line=839)
W('42,3121', 0o16347, '', 'OCT', '16347', '82    DP3, DP3, DP3', kind='data', line=840)
W('42,3122', 0o16347, '', 'OCT', '16347', '83    DP3, DP3, DP3', kind='data', line=841)
W('42,3123', 0o16347, '', 'OCT', '16347', '84    DP3, DP3, DP3', kind='data', line=842)
W('42,3124', 0o16347, '', 'OCT', '16347', '85    DP3, DP3, DP3', kind='data', line=843)
W('42,3125', 0o24512, '', 'OCT', '24512', '86    DP4, DP4, DP4', kind='data', line=844)
W('42,3126', 0o00302, '', 'OCT', '00302', '87    CDU, YOPT', kind='data', line=845)
W('42,3127', 0o32655, '', 'OCT', '32655', '88    DPFRAC FOR EACH', kind='data', line=846)
W('42,3130', 0o10347, '', 'OCT', '10347', '89    DP3, DP3, DP1', kind='data', line=847)
W('42,3131', 0o24344, '', 'OCT', '24344', '90    DP1, DP3, DP4', kind='data', line=848)
W('42,3132', 0o00302, '', 'OCT', '00302', '91    CDU, YOPT', kind='data', line=849)
W('42,3133', 0o00302, '', 'OCT', '00302', '92    CDU, YOPT', kind='data', line=850)
W('42,3134', 0o16347, '', 'OCT', '16347', '93    DP3, DP3, DP3', kind='data', line=851)
W('42,3135', 0o00302, '', 'OCT', '00302', '94    CDU, YOPT', kind='data', line=852)
W('42,3136', 0o04102, '', 'OCT', '04102', '95    CDU, CDU, CDU', kind='data', line=853)
W('42,3137', 0o04102, '', 'OCT', '04102', '96    CDU, CDU, CDU', kind='data', line=854)
W('42,3140', 0o06143, '', 'OCT', '06143', '97    ARTH, ARTH, ARTH', kind='data', line=855)
W('42,3141', 0o06043, '', 'OCT', '06043', '98    ARTH, FRAC, ARTH', kind='data', line=856)
W('42,3142', 0o06247, '', 'OCT', '06247', '99    DP3, DP2, ARTH', kind='data', line=857)
# END OF RUTMXTAB

#   SBANK= LOWSUPER
