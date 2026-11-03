"""P11.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P11.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 533-550 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P11', 'P11.agc', 'Comanche055', pages='533-550')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P11.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        533-550
# Mod history:  2009-05-13 HG   Started adapting from the Colossus249/ file
# of the same name, using Comanche055 page
# images 0533.jpg - 0550.jpg.
# 2009-05-20 RSB  Corrections: ERTHALT -> EARTHALT,
# STATSW -> SATSW.
# 2009-05-23 RSB  At end of RESCALES, corrected TC 0 to TC Q.
# Added an SBANK= prior to a 2CADR.
# 2010-08-24 JL   Fixed page numbers. Added missing comment character on p537.
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
# Page 533
# EARTH ORBIT INSERTION MONITOR PROGRAM
# *************************************

# PROGRAM DESCRIPTION -P11-

# MOD NO. 1
# MOD BY ELIASSEN

# FUNCTIONAL DESCRIPTION

# P11 IS INITIATED BY

# A) GYROCOMPASS PRG P02 WHEN LIFTOFF DISCRETE IS RECEIVED OR
# B) BACKUP THRU VERB 75 ENTER

# PROGRAM WILL
# 1. ZERO CMC CLOCK AT LIFTOFF (OR UPON RECEIPT OF BACKUP)
# 2. UPDATE TEPHEM TO TIME CMC CLOCK WAS ZEROED
# 3. INITIATE SERVICER AT PREREAD1
# 4. CHANGE MAJOR MODE TO 11
# 5. CLEAR DSKY IN CASE OF V 75
# 6. STORE LIFTOFF IMU-CDU ANGLES FOR ATT. ERROR DISPLAY
# 7. TERMINATE GYROCOMPASSING     -  -
# 8. COMPUTE INITIAL VECTORS      RN, VN            -  -  -
# 9. COMPUTE REFSMMAT FOR PRELAUNCH ALIGNMENT WHERE U ,U ,U ARE
# -         -                                X  Y  Z
# U =(UNIT(-R) LOCAL VERTICAL AT TIME OF LIFTOFF
# Z
# -       -   -
# U =UNIT(A), A=HOR VECTOR AT LAUNCH AZIMUTH
# X
# -  -   -
# U =U * U
# U  Z   X

# 10. SET REFSMMAT KNOWN FLAG
# 11. SET AVGEXIT IN SERVICER TO VHHDOT TO
# COMPUTE AND DISPLAY NOUN 62 EVERY 2 SECONDS

# R1  V1  - INERTIAL VELOCITY MAGNITUDE IN FPS
# R2  HDOT - RATE OF CHANGE OF VEHICLE VEL IN FPS
# R3  H    - VEHICLE ALTITUDE ABOVE PAD IN NM

# 12. DISPLAY BODY AXES ATT. ERRORS ON FDAI NEEDLES
#
# A) FROM L.O. TO RPSTART (APPROX. 0 TO +10SECS AFTER L.O.)
# DESIRED ATTITUDE IS AS STORED AT L.O.
# B) FROM RPSTART TO POLYSTOP(APPROX.+10 TO +133SECS AFTER LO)
# DESIRED ATTITUDE IS SPECIFIED BY CMC PITCH AND ROLL
# POLYNOMIALS DURING SATURN ROLLOUT AND PITCHOVER
# Page 534
# THE DISPLAY IS RUN AS LOW PRIORITY JOB APPROX.
# EVERY 1/2 SEC OR LESS AND IS DISABLED UPON OVFLO OF TIME1

# SUBROUTINES CALLED

# 2PHSCHNG        BANKCALL        CALCGRA         CDUTRIG         CLEANDSP        DANZIG
# DELAYJOB        EARTHR          ENDOFJOB        FINDVAC         IBNKCALL
# INTPRET         LALOTORV        NEEDLER         NEWMODEX        PHASCHNG
# POSTJUMP        POWRSERS        PREREAD1        REGODSPR        S11.1
# SERVEXIT        TASKOVER        TCDANZIG        V1STO2S         WAITLIST

# ASTRONAUT REQUESTS (IF ALTITUDE ABOVE 300,000 FT)
#
# DSKY -
# MONITOR DISPLAY OF TIME TO PERIGEE R1 HOURS
# R2 MINUTES

# DSKY -
# MONITOR DISPLAY OF R1 APOGEE ALTITUDE IN NAUTICAL MILES
# R2 PERIGEE ALTITUDE IN NAUTICAL MILES
# R3 TFF IN MINUTES/SECS

# IF ASTRONAUT HAS REQUESTED ANY OF THESE DISPLAYS HE MUST
# HIT PROCEED TO RETURN TO NORMAL NOUN 62 DISPLAY.
# NORMAL EXIT MODE

# ASTRONAUT       VERB 37 ENTER 00 ENTER

# ALARM MODES - NONE

# ABORT EXIT MODES -

# OUTPUT

# TLIFTOFF (DP)   TEPHEM (TP)
# REFSMMAT
# DSKY DISPLAY
# FDAI DISPLAY

# ERASABLE INITIALIZATION

# AZO, AXO, -AYO
# LATITUDE
# PADLONG
# TEPHEM
# PGNCSALT
# POLYNUM THRU POLYNUM +14D)
# RPSTART
# POLYSTOP
# FLAGS SET OR RESET
# Page 535
# SET REFSMFLG
# SET DVMON IDLE FLAG
# CLEAR ERADFLAG

# DEBRIS

# LIFTTEMP
# POLYNUM THRU POLYNUM +7
# SPOLYARG
# BODY1, BODY2, BODY3
# VMAG2, ALTI, HDOT
# CENTRALS, CORE SET AND VAC AREAS
#   COUNT 34/P11

S('BITS5-6', 'equals', 0o5035, line=152)
#   BANK 42
#   SETLOC P11ONE
#   BANK

#   EBANK= TEPHEM
W('34,2002', 0o35051, 'P11', 'CA', 'EBANK3', line=158)
W('34,2003', 0o54003, '', 'TS', 'EBANK', line=159)

W('34,2004', 0o00006, '', 'EXTEND', line=161)
W('34,2005', 0o32277, '', 'DCA', 'REP11S', 'DIRECT RESTARTS TO REP11', line=162)
W('34,2006', 0o52757, '', 'DXCH', '-PHASE3', line=163)
W('34,2007', 0o45021, '', 'CS', 'ZERO', line=164)
W('34,2010', 0o22007, '', 'ZL', line=165)
W('34,2011', 0o55265, '', 'TS', 'LIFTTEMP', line=166)
W('34,2012', 0o52763, '', 'DXCH', '-PHASE5', 'INACTIVE GROUP 5, PRELAUNCH PROTECTION', line=167)
W('34,2013', 0o00006, 'P11+7', 'EXTEND', line=168)
W('34,2014', 0o32301, '', 'DCA', 'REP11SA', line=169)
W('34,2015', 0o53337, '', 'DXCH', 'TLIFTOFF', line=170)

W('34,2016', 0o00006, '', 'EXTEND', line=172)
W('34,2017', 0o30025, '', 'DCA', 'TIME2', line=173)
W('34,2020', 0o53266, '', 'DXCH', 'LIFTTEMP', 'FOR RESTARTS', line=174)

W('34,2021', 0o35021, '', 'CA', 'ZERO', line=176)
W('34,2022', 0o22007, '', 'ZL', line=177)
W('34,2023', 0o52025, '', 'DXCH', 'TIME2', line=178)
W('34,2024', 0o53337, 'REP11A-2', 'DXCH', 'TLIFTOFF', line=179)
W('34,2025', 0o52757, 'REP11A-1', 'DXCH', '-PHASE3', 'RESET PHASE', line=180)

W('34,2026', 0o00004, 'REP11A', 'INHINT', line=183)
W('34,2027', 0o00006, '', 'EXTEND', line=184)
W('34,2030', 0o31710, '', 'DCA', 'TEPHEM +1', line=185)
W('34,2031', 0o53271, '', 'DXCH', 'TEPHEM1 +1', line=186)
W('34,2032', 0o31706, '', 'CA', 'TEPHEM', line=187)
# Page 536
W('34,2033', 0o57267, '', 'XCH', 'TEPHEM1', line=189)

W('34,2034', 0o00006, '', 'EXTEND', line=191)
W('34,2035', 0o31337, '', 'DCA', 'TLIFTOFF', line=192)
W('34,2036', 0o21271, '', 'DAS', 'TEPHEM1 +1', line=193)
W('34,2037', 0o27267, '', 'ADS', 'TEPHEM1', 'CORRECTFOR OVERFLOW', line=194)

W('34,2040', 0o05412, '', 'TC', 'PHASCHNG', line=196)
W('34,2041', 0o05023, '', 'OCT', '05023', kind='data', line=197)
W('34,2042', 0o22000, '', 'OCT', '22000', kind='data', line=198)

W('34,2043', 0o00004, '', 'INHINT', line=200)
W('34,2044', 0o00006, '', 'EXTEND', line=201)
W('34,2045', 0o31270, '', 'DCA', 'TEPHEM1', line=202)
W('34,2046', 0o53707, '', 'DXCH', 'TEPHEM', line=203)
W('34,2047', 0o31271, '', 'CA', 'TEPHEM1 +2', line=204)
W('34,2050', 0o57710, '', 'XCH', 'TEPHEM +2', line=205)

W('34,2051', 0o32000, '', 'CAF', 'EBDVCNT', line=207)
W('34,2052', 0o54003, '', 'TS', 'EBANK', line=208)
#   EBANK= DVCNTR
W('34,2053', 0o04740, '', 'TC', 'IBNKCALL', line=210)
W('34,2054', 0o76722, '', 'CADR', 'PREREAD1', 'ZERO PIPS AND INITIALIZE AVERAGEG', kind='data', line=211)

W('34,2055', 0o05412, '', 'TC', 'PHASCHNG', line=213)
W('34,2056', 0o05023, '', 'OCT', '05023', 'CONTINUE HERE ON RESTART', kind='data', line=214)
W('34,2057', 0o22000, '', 'OCT', '22000', kind='data', line=215)

W('34,2060', 0o35036, '', 'CAF', '.5SEC', 'START ATT ERROR DISPLAY', line=217)
W('34,2061', 0o05245, '', 'TC', 'WAITLIST', 'IN .5 SEC', line=218)
#   EBANK= BODY3
W('34,2062', 0o02320, '', '2CADR', 'ATERTASK', kind='data', line=220)
W('34,2063', 0o70066, kind='data', line=220)

W('34,2064', 0o05354, '', 'TC', 'NEWMODEX', 'DISPLAY MM 11', line=222)
W('34,2065', 0o00013, '', 'MM', '11', kind='data', line=223)

W('34,2066', 0o05546, '', 'TC', 'UPFLAG', line=225)
W('34,2067', 0o00022, '', 'ADRES', 'NODOP01', kind='data', line=226)

W('34,2070', 0o36214, '', 'CA', 'POWDNCOD', 'SWITCH TO POWERED FLIGHT DOWNLIST', line=228)
W('34,2071', 0o54332, '', 'TS', 'DNLSTCOD', line=229)

W('34,2072', 0o04662, '', 'TC', 'BANKCALL', line=231)
W('34,2073', 0o20703, '', 'CADR', 'CLEANDSP', 'CLEAR DSKY IN CASE OF V75', kind='data', line=232)

W('34,2074', 0o05372, '', 'TC', '2PHSCHNG', line=234)
W('34,2075', 0o40514, '', 'OCT', '40514', 'PROTECT ATERTASK', kind='data', line=235)
W('34,2076', 0o00073, '', 'OCT', '00073', kind='data', line=236)
W('34,2077', 0o32001, '', 'CAF', 'EBQPLACE', line=237)
# Page 537
W('34,2100', 0o54003, '', 'TS', 'EBANK', line=239)

#   EBANK= QPLACES
W('34,2101', 0o32302, '', 'CA', 'P11XIT', 'SET EXIT FROM PROUT IN EARTHR', line=242)
W('34,2102', 0o55426, '', 'TS', 'QPLACES', line=243)
W('34,2103', 0o06006, '', 'TC', 'INTPRET', line=244)
W('34,2104', 0o64375, '', 'VLOAD', 'MXV', kind='interp', line=245)
W('34,2105', 0o02467, '', '', 'THETAN', kind='operand', line=246)
W('34,2106', 0o02672, '', '', 'XSM', kind='operand', line=247)
W('34,2107', 0o53372, '', 'VSL1', 'VAD', kind='interp', line=248)
W('34,2110', 0o02650, '', '', 'ERCOMP', kind='operand', line=249)
W('34,2111', 0o16650, '', 'STODL', 'ERCOMP', kind='interp', line=250)
W('34,2112', 0o01337, '', '', 'TLIFTOFF', kind='operand', line=251)
W('34,2113', 0o52131, '', 'SSP', 'GOTO', kind='interp', line=252)
W('34,2114', 0o00052, '', '', 'S2', kind='operand', line=253)
W('34,2115', 0o66424, '', 'CADR', 'PROUT', 'RETURN FROM EARTHR', kind='data', line=254)
W('34,2116', 0o66373, '', '', 'EARTHR +3', kind='operand', line=255)
W('34,2117', 0o22007, 'MATRXJOB', 'ZL', '', 'STORE DP GIMBAL ANGLES FOR ATTITUDE', line=256)
W('34,2120', 0o30032, '', 'CA', 'CDUX', '      ERROR DISPLAY AFTER LIFTOFF', line=257)
W('34,2121', 0o53760, '', 'DXCH', 'OGC', line=258)
W('34,2122', 0o22007, '', 'ZL', line=259)
W('34,2123', 0o30033, '', 'CA', 'CDUY', line=260)
W('34,2124', 0o53762, '', 'DXCH', 'IGC', line=261)
W('34,2125', 0o22007, '', 'ZL', line=262)
W('34,2126', 0o30034, '', 'CA', 'CDUZ', line=263)
W('34,2127', 0o53764, '', 'DXCH', 'MGC', line=264)
W('34,2130', 0o06006, '', 'TC', 'INTPRET', '      -', line=265)
W('34,2131', 0o74575, '', 'VLOAD', 'VSR1', 'SCALE OGC B-1', kind='interp', line=266)
W('34,2132', 0o02760, '', '', 'OGC', kind='operand', line=267)
W('34,2133', 0o02760, '', 'STORE', 'OGC', kind='interp', line=268)
W('34,2134', 0o77731, '', 'SSP', '', 'ZERO RTX2', kind='interp', line=269)
W('34,2135', 0o03747, '', '', 'RTX2', 'FOR', kind='operand', line=270)
W('34,2136', 0o00000, '', '', '0', 'EARTH', kind='operand', line=271)
W('34,2137', 0o65345, '', 'DLOAD', 'PDDL', kind='interp', line=272)
W('34,2140', 0o01273, '', '', 'PGNCSALT', 'ALTITUDE OF PGNCS', kind='operand', line=273)
W('34,2141', 0o01264, '', '', 'PADLONG', 'LONGITUDE', kind='operand', line=274)
W('34,2142', 0o55525, '', 'PDDL', 'VDEF', kind='interp', line=275)
W('34,2143', 0o02403, '', '', 'LATITUDE', 'GEODETIC LATITUDE', kind='operand', line=276)
W('34,2144', 0o15104, '', 'STODL', 'LAT', 'LAT,LONG,ALT ARE CONSECUTIVE', kind='interp', line=277)
W('34,2145', 0o15335, '', '', 'HI6ZEROS', 'TIME = 0', kind='operand', line=278)
W('34,2146', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=279)
W('34,2147', 0o00662, '', '', 'ERADFLAG', kind='operand', line=280)
W('34,2150', 0o26441, '', '', 'LALOTORV', 'CONVERT TO POSITION VECTOR IN REF.COORDS', kind='operand', line=281)

W('34,2151', 0o35232, '', 'STCALL', 'RN1', '             -', kind='interp', line=283)
W('34,2152', 0o70334, '', '', 'GETDOWN', 'RETURN WITH VECTOR FOR DOWN DIRECTION', kind='operand', line=284)
W('34,2153', 0o53476, '', 'VCOMP', 'UNIT', kind='interp', line=285)
W('34,2154', 0o25752, '', 'STOVL', 'REFSMMAT +12D', 'UNITZ = UNIT(GRAV)', kind='interp', line=286)
W('34,2155', 0o01232, '', '', 'RN1', kind='operand', line=287)
W('34,2156', 0o74235, '', 'VXV', 'VXSC', kind='interp', line=288)
# Page 538
W('34,2157', 0o01714, '', '', 'UNITW', 'SCALED AT 1', kind='operand', line=290)
W('34,2160', 0o30304, '', '', '-ERTHRAT', 'V = EARTHRATE X R', kind='operand', line=291)
W('34,2161', 0o77712, '', 'VSL4', '', 'SCALE TO 2(7) M/CS', kind='interp', line=292)
W('34,2162', 0o25240, '', 'STOVL', 'VN1', kind='interp', line=293)
W('34,2163', 0o01752, '', '', 'REFSMMAT +12D', kind='operand', line=294)
W('34,2164', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=295)
W('34,2165', 0o01714, '', '', 'UNITW', '(REF3 X UNITW) = EAST', kind='operand', line=296)
W('34,2166', 0o47206, '', 'PUSH', 'VXV', kind='interp', line=297)
W('34,2167', 0o01752, '', '', 'REFSMMAT +12D', '(EAST X REF3) = -SOUTH', kind='operand', line=298)
W('34,2170', 0o65256, '', 'UNIT', 'PDDL', kind='interp', line=299)
W('34,2171', 0o02634, '', '', 'LAUNCHAZ', 'COS(AZ)*SOUTH', kind='operand', line=300)
W('34,2172', 0o74346, '', 'COS', 'VXSC', kind='interp', line=301)
W('34,2173', 0o77626, '', 'STADR', kind='interp', line=302)
W('34,2174', 0o62041, '', 'STODL', 'REFSMMAT', 'TEMPORARY STORAGE', kind='interp', line=303)
W('34,2175', 0o02634, '', '', 'LAUNCHAZ', kind='operand', line=304)
W('34,2176', 0o74356, '', 'SIN', 'VXSC', 'SIN(AZ)*EAST', kind='interp', line=305)
W('34,2177', 0o53455, '', 'VAD', 'UNIT', 'SIN(AZ)*EAST - COS(AZ)*SOUTH = REF1', kind='interp', line=306)
W('34,2200', 0o01736, '', '', 'REFSMMAT', kind='operand', line=307)
W('34,2201', 0o01736, '', 'STORE', 'REFSMMAT', kind='interp', line=308)

W('34,2202', 0o53435, '', 'VXV', 'UNIT', '(REF1 X REF3) = -REF3', kind='interp', line=310)
W('34,2203', 0o01752, '', '', 'REFSMMAT +12D', kind='operand', line=311)
W('34,2204', 0o77676, '', 'VCOMP', kind='interp', line=312)
W('34,2205', 0o01744, '', 'STORE', 'REFSMMAT +6', kind='interp', line=313)
W('34,2206', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=314)
W('34,2207', 0o15333, '', '', 'DPHALF', '1/2 REV', kind='operand', line=315)
W('34,2210', 0o02634, '', '', 'LAUNCHAZ', kind='operand', line=316)
W('34,2211', 0o65215, '', 'DAD', 'PDDL', kind='interp', line=317)
W('34,2212', 0o02401, '', '', 'AZIMUTH', kind='operand', line=318)
W('34,2213', 0o03301, '', '', 'SATRLRT', 'SET   SATRLRT = -SATRLRT IF', kind='operand', line=319)
W('34,2214', 0o45565, '', 'SIGN', 'STADR', '(1/2REV -LAVNCHAZ +AZIMUTH) IS NEGATIVE', kind='interp', line=320)
W('34,2215', 0o74476, '', 'STORE', 'SATRLRT', 'FOR ROLL CALC IN FDAI ATT. ERROR DISPLAY', kind='interp', line=321)
W('34,2216', 0o77414, '', 'SET', 'EXIT', kind='interp', line=322)
W('34,2217', 0o01462, '', '', 'REFSMFLG', 'SET REFSMMAT KNOWN FLAG', kind='operand', line=323)

W('34,2220', 0o05412, '', 'TC', 'PHASCHNG', line=325)
W('34,2221', 0o04023, '', 'OCT', '04023', kind='data', line=326)

W('34,2222', 0o00006, '', 'EXTEND', line=328)
W('34,2223', 0o32306, '', 'DCA', 'P11SCADR', line=329)
W('34,2224', 0o53223, '', 'DXCH', 'AVGEXIT', 'SET AVGEXIT', line=330)

W('34,2225', 0o37665, '', 'CA', 'PRIO31', '2 SECONDS AT 2(+8)', line=332)
W('34,2226', 0o55074, '', 'TS', '1/PIPADT', line=333)

#   EBANK= RCSFLAGS
W('34,2227', 0o35057, '', 'CA', 'EBANK6', line=336)
W('34,2230', 0o54003, '', 'TS', 'EBANK', line=337)

W('34,2231', 0o00004, '', 'INHINT', line=339)
# Page 539
W('34,2232', 0o45021, '', 'CS', 'ZERO', line=341)
W('34,2233', 0o55063, '', 'TS', 'TBASE5', 'RESTART READACCS 2 SECONDS AFTER LIFTOFF', line=342)

W('34,2234', 0o40025, '', 'CS', 'TIME1', line=344)
W('34,2235', 0o65042, '', 'AD', '2SECS', 'DO READACCS 2 SECONDS AFTER LIFTOFF', line=345)

W('34,2236', 0o10000, '', 'CCS', 'A', 'CHECK TO INSURE DT IS POSITIVE', line=347)
W('34,2237', 0o12242, '', 'TCF', '+3', 'TIME POSITIVE', line=348)
W('34,2240', 0o12242, '', 'TCF', '+2', 'CANNOT GET HERE', line=349)
W('34,2241', 0o35021, '', 'CA', 'ZERO', 'TIME NEGATIVE - SET TO 1', line=350)
W('34,2242', 0o65017, '', 'AD', 'ONE', 'RESTORE TIME  -  OR MAKE POSITIVE', line=351)

W('34,2243', 0o05245, '', 'TC', 'WAITLIST', line=353)
#   EBANK= AOG
W('34,2244', 0o02744, '', '2CADR', 'READACCS', kind='data', line=355)
W('34,2245', 0o76066, kind='data', line=355)

W('34,2246', 0o05372, '', 'TC', '2PHSCHNG', line=357)
W('34,2247', 0o00003, '', 'OCT', '00003', 'TURN OFF GROUP 3', kind='data', line=358)
W('34,2250', 0o00025, '', 'OCT', '00025', 'PROTECT NORMLIZE AND READACCS', kind='data', line=359)

W('34,2251', 0o04701, '', 'TC', 'POSTJUMP', line=361)
W('34,2252', 0o77236, '', 'CADR', 'NORMLIZE', 'DO NORMLIZE AND ENDOFJOB', kind='data', line=362)

#   EBANK= TEPHEM
W('34,2253', 0o00004, 'REP11', 'INHINT', line=366)
W('34,2254', 0o10763, '', 'CCS', 'PHASE5', line=367)
W('34,2255', 0o05217, '', 'TC', 'ENDOFJOB', line=368)

W('34,2256', 0o11265, '', 'CCS', 'LIFTTEMP', line=370)
W('34,2257', 0o12263, '', 'TCF', '+4', line=371)
W('34,2260', 0o12263, '', 'TCF', '+3', line=372)
W('34,2261', 0o12263, '', 'TCF', '+2', line=373)
W('34,2262', 0o12013, '', 'TCF', 'P11+7', line=374)

W('34,2263', 0o41336, '', 'CS', 'TLIFTOFF', line=376)
W('34,2264', 0o00006, '', 'EXTEND', line=377)
W('34,2265', 0o62273, '', 'BZMF', 'ENDREP11', line=378)

W('34,2266', 0o10024, '', 'CCS', 'TIME2', '**TIME2 MUST BE NON-ZERO AT LIFTOFF**', line=380)
W('34,2267', 0o12021, '', 'TCF', 'REP11A -5', 'T2,T1 NOT YET ZEROED, GO AND DO IT', line=381)

W('34,2270', 0o00006, '', 'EXTEND', '', 'T2,T1 ZEROED, SET TLIFTOFF', line=383)
W('34,2271', 0o31266, '', 'DCA', 'LIFTTEMP', line=384)
W('34,2272', 0o12024, '', 'TCF', 'REP11A-2', line=385)

W('34,2273', 0o00006, 'ENDREP11', 'EXTEND', line=387)
W('34,2274', 0o32301, '', 'DCA', 'REP11SA', line=388)
W('34,2275', 0o12025, '', 'TCF', 'REP11A-1', line=389)
# Page 540
W('34,2276', 0o77766, 'REP11S', '2OCT', '7776600011', kind='data', line=391)
W('34,2277', 0o00011, kind='data', line=391)

W('34,2300', 0o77764, 'REP11SA', '2OCT', '7776400013', kind='data', line=393)
W('34,2301', 0o00013, kind='data', line=393)

W('34,2302', 0o02451, 'P11XIT', 'GENADR', 'P11OUT', kind='data', line=395)
W('34,2303', 0o71704, '-ERTHRAT', '2DEC*', '-7.292115138 E-7 B18*', '- EARTH RATE AT 2(18)', kind='data', line=396)
W('34,2304', 0o41735, kind='data', line=396)

#   EBANK= BODY3
W('34,2305', 0o02307, 'P11SCADR', '2CADR', 'VHHDOT', kind='data', line=399)
W('34,2306', 0o70066, kind='data', line=399)

S('POWDNCOD', 'equals', 0o6214, line=401)

#   EBANK= BODY3
# VHHDOT IS EXECUTED EVERY 2 SECONDS TO DISPLAY ON DSKY
# VI INERTIAL VELOCITY MAGNITUDE
# HDOT  RATE OF CHANGE OF ALT ABOVE L PAD RADIUS
# H  ALTITUDE ABOVE L PAD RADIUS

W('34,2307', 0o06006, 'VHHDOT', 'TC', 'INTPRET', line=409)
W('34,2310', 0o77624, '', 'CALL', '', 'LOAD VMAGI, ALTI,', kind='interp', line=410)
W('34,2311', 0o70542, '', '', 'S11.1', 'HDOT FOR DISPLAY', kind='operand', line=411)
W('34,2312', 0o77776, '', 'EXIT', kind='interp', line=412)
W('34,2313', 0o05412, '', 'TC', 'PHASCHNG', line=413)
W('34,2314', 0o00035, '', 'OCT', '00035', kind='data', line=414)

W('34,2315', 0o32622, '', 'CAF', 'V06N62', 'DISPLAY IN R1 R2      R3', line=416)
W('34,2316', 0o04662, '', 'TC', 'BANKCALL', '           VI HDOT    H', line=417)
W('34,2317', 0o20707, '', 'CADR', 'REGODSP', kind='data', line=418)

W('34,2320', 0o35006, 'ATERTASK', 'CAF', 'PRIO1', 'ESTABLISH JOB TO DISPLAY ATT ERRORS', line=420)
W('34,2321', 0o05147, '', 'TC', 'FINDVAC', 'COMES HERE AT L.O. + .33 SEC', line=421)
#   EBANK= BODY3
W('34,2322', 0o02345, '', '2CADR', 'ATERJOB', kind='data', line=423)
W('34,2323', 0o70066, kind='data', line=423)

W('34,2324', 0o41501, '', 'CS', 'RCSFLAGS', 'SET BIT3 FOR', line=425)
W('34,2325', 0o75015, '', 'MASK', 'BIT3', 'NEEDLER', line=426)
W('34,2326', 0o27501, '', 'ADS', 'RCSFLAGS', 'INITIALIZATION PASS', line=427)
W('34,2327', 0o04740, '', 'TC', 'IBNKCALL', 'AND GO', line=428)
W('34,2330', 0o42420, '', 'CADR', 'NEEDLER', 'DO IT', kind='data', line=429)
W('34,2331', 0o35017, '', 'CA', 'BIT1', 'SET SW', line=430)
W('34,2332', 0o55725, '', 'TS', 'SATSW', 'FOR DISPLAY', line=431)
W('34,2333', 0o05324, '', 'TC', 'TASKOVER', line=432)
W('34,2334', 0o40220, 'GETDOWN', 'STQ', 'SETPD', kind='interp', line=433)
W('34,2335', 0o02242, '', '', 'INCORPEX', kind='operand', line=434)
W('34,2336', 0o00001, '', '', '0D', kind='operand', line=435)
W('34,2337', 0o77745, '', 'DLOAD', kind='interp', line=436)
W('34,2340', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=437)
# Page 541
W('34,2341', 0o14007, '', 'STODL', '6D', kind='interp', line=439)
W('34,2342', 0o15333, '', '', 'DPHALF', kind='operand', line=440)
W('34,2343', 0o34011, '', 'STCALL', '8D', kind='interp', line=441)
W('34,2344', 0o26446, '', '', 'LALOTORV +5', kind='operand', line=442)
# THIS SECTION PROVIDES ATTITUDE ERROR DISPLAYS TO THE FDAI DURING SONE BOOST

# COMPUTE DESIRED PITCH W.R.T. PAD LOCAL VERTICAL AT LIFTOFF
# 2    3    4    5    6
# PITCH = A0+A1T+A2T +A3T +A4T +A5T +A6T
# SCALED TO 32 REVS.                                   -14
# IF TL = TIME IN SECS FROM L.O., THEN    T = 100(TL-RPSTART)2
# WHERE   TL GE RPSTART
# TL LE (-POLYSTOP + RPSTART)
# COMPUTE DESIRED ROLL WHERE ROLL EQUALS ANGLE FROM
# LAUNCHAZ TO -Z(S/C) AS SEEN FROM X(S/C).
# ROLL = LAUNCHAZ-AZIMUTH-.5 +SATRLRT*T   IN REV
# SATRLRT = RATE OF ROLL IN REV/CENTI-SEC
# T,IN CENTI-SEC,IS DEFINED AS ABOVE,INCLUSIVE OF TIME RESTRICTIONS

# FOR SIMPLICITY, LET     P = 2*PI*PITCH
# R = 2*PI*ROLL

# CONSTRUCT THE TRANSFORMATION MATRIX, TSMV, GIVING DESIRED S/C AXES IN
# TERMS OF SM COORDINATES.  LET THE RESULTING ROWS EQUAL THE VECTORS XDC,
# YDC,AND ZDC.

# *     (    SIN(P)                 0               -COS(P)    )   (XDC)
# TSMV = (-SIN(R)*COS(P)          -COS(R)         -SIN(R)*SIN(P)) = (YDC)
# (-COS(R)*COS(P)           SIN(R)         -COS(R)*SIN(P))   (ZDC)

# XDC,YDC,ZDC ARE USED AS INPUT TO CALCGTA FOR THE EXTRACTION OF THE
# EULER SET OF ANGLES WHICH WILL BRING THE SM INTO THE DESIRED
# ORIENTATION.  THIS EULER SET, OGC, IGC, AND MGC, MAY BE IDENTIFIED
# AS THE DESIRED CDU ANGLES.

# (XDC)                   (OGC)
# (YDC) ---) CALCGTA ---) (IGC)
# (ZDC)                   (MGC)

# -
# DEFINE THE VECTOR DELTACDU.

# -         (OGC)   (CDUX)
# DELTACDU = (IGC) - (CDUY)
# (MGC)   (CDUZ)

# -              -    *    -
# COMPUTE ATTITUDE ERRORS, A, WHERE       A = TGSC*DELTACDU
#
# *     (1             SIN(CDUZ)             0    )   THE GIMBAL ANGLES
# Page 542
# TGSC = (0       COS(CDUX)*COS(CDUZ)     SIN(CDUX)) = TO SPACECRAFT AXES
# (0      -SIN(CDUX)*COS(CDUZ)     COS(CDUX))   CONVERSION MATRIX

# -
# THE ATTITUDE ERRORS, A, ARE STORED ONE HALF SINGLE PRECISION IN
# THE REGISTERS AK, AK1, AK2 AS INPUT TO NEEDLER, THE FDAI ATTITUDE
# ERROR DISPLAY ROUTINE.

W('34,2345', 0o30102, 'ATERJOB', 'CAE', 'FLAGWRD6', 'CHECK FLAGWRD6', line=498)
W('34,2346', 0o74105, '', 'MASK', 'OCT60000', 'BITS 14, 15', line=499)
W('34,2347', 0o00006, '', 'EXTEND', line=500)
W('34,2350', 0o12352, '', 'BZF', '+2', 'OK - CONTINUE', line=501)
W('34,2351', 0o05217, '', 'TC', 'ENDOFJOB', 'SATURN STICK ON - KILL JOB', line=502)
W('34,2352', 0o35006, '', 'CAF', 'BIT10', 'CHECK IF S/C CONTROL', line=503)
W('34,2353', 0o00006, '', 'EXTEND', '', 'OF SATURN PANEL', line=504)
W('34,2354', 0o02030, '', 'RAND', 'CHAN30', 'SWITCH IS ON', line=505)
W('34,2355', 0o00006, '', 'EXTEND', line=506)
W('34,2356', 0o12510, '', 'BZF', 'STRSAT', 'IT IS - GO STEER', line=507)
W('34,2357', 0o11725, '', 'CCS', 'SATSW', 'IT IS NOT - WAS IT ON LAST CYCLE', line=508)
W('34,2360', 0o02363, '', 'TC', 'ATTDISP', 'NO - CONTINUE', line=509)
W('34,2361', 0o02513, '', 'TC', 'ATRESET', 'YES - REINITIALIZE NEEDLER', line=510)
W('34,2362', 0o02513, '', 'TC', 'ATRESET', 'YES - REINITIALIZE NEEDLER', line=511)
W('34,2363', 0o41702, 'ATTDISP', 'CS', 'RPSTART', 'PITCH/ROLL START TIME', line=512)
W('34,2364', 0o60025, '', 'AD', 'TIME1', line=513)
W('34,2365', 0o00006, '', 'EXTEND', line=514)
W('34,2366', 0o62615, '', 'BZMF', 'NOPOLY', 'IF MINUS THEN ATTITUDE HOLD', line=515)
W('34,2367', 0o54154, '', 'TS', 'MPAC', 'MPAC=TIME1-RPSTART', line=516)
W('34,2370', 0o55707, '', 'TS', 'SPOLYARG', 'SAVE FOR USE IN ROLL CALCULATION', line=517)
W('34,2371', 0o61703, '', 'AD', 'POLYSTOP', 'NEG PITCHOVER TIME IN CSECS', line=518)
W('34,2372', 0o00006, '', 'EXTEND', line=519)
W('34,2373', 0o62375, '', 'BZMF', '+2', line=520)
W('34,2374', 0o02615, '', 'TC', 'NOPOLY', 'GO TO ATTITUDE HOLD', line=521)
W('34,2375', 0o30024, '', 'CA', 'TIME2', line=522)
W('34,2376', 0o00006, '', 'EXTEND', line=523)
W('34,2377', 0o62401, '', 'BZMF', '+2', line=524)
W('34,2400', 0o02615, '', 'TC', 'NOPOLY', 'GO TO ATTITUDE HOLD', line=525)
W('34,2401', 0o31661, '', 'CAE', 'POLYNUM', line=526)
W('34,2402', 0o54001, '', 'TS', 'L', line=527)
W('34,2403', 0o32621, '', 'CAF', 'COEFPOLY', 'EVALUATE PITCH POLYNOMIAL', line=528)
W('34,2404', 0o07164, '', 'TC', 'POWRSERS', 'SCALED TO 32 REVOLUTIONS', line=529)

W('34,2405', 0o35021, '', 'CA', 'ZERO', 'RETURN WITH PITCH(32REV)', line=531)
W('34,2406', 0o54163, '', 'TS', 'MODE', 'STORED MPAC, MPAC +1', line=532)
W('34,2407', 0o06006, '', 'TC', 'INTPRET', line=533)
W('34,2410', 0o54201, '', 'SETPD', 'SL', '32(PITCH(32REV))=PITCH(REV)', kind='interp', line=534)
W('34,2411', 0o00001, '', '', '0', kind='operand', line=535)
W('34,2412', 0o20206, '', '', '5', kind='operand', line=536)
W('34,2413', 0o77606, '', 'PUSH', '', 'LET P(RAD)=2*PI*PITCH(REV)', kind='interp', line=537)
W('34,2414', 0o77650, '', 'GOTO', kind='interp', line=538)
W('34,2415', 0o76155, '', '', 'ATTDISP1', 'AROUND SETLOC', kind='operand', line=539)
# Page 543
# *
# CONSTRUCT SM TO S/C MATRIX, TSMV

#   SETLOC P11TWO
#   BANK  # 36 IN COL., 34 IN DISK

#   COUNT 36/P11

W('37,2155', 0o57546, 'ATTDISP1', 'COS', 'DCOMP', kind='interp', line=549)
W('37,2156', 0o14017, '', 'STODL', '14D', '-.5*COS(P)', kind='interp', line=550)
W('37,2157', 0o77756, '', 'SIN', kind='interp', line=551)
W('37,2160', 0o14013, '', 'STODL', '10D', '.5*SIN(P)', kind='interp', line=552)
W('37,2161', 0o15335, '', '', 'ZEROVECS', kind='operand', line=553)
W('37,2162', 0o00015, '', 'STORE', '12D', '0', kind='interp', line=554)

# EVALUATE ROLL = LAUNCHAZ-AZIMUTH-.5+SATRLRT*T
W('37,2163', 0o41335, '', 'SLOAD', 'DMP', kind='interp', line=557)
W('37,2164', 0o03310, '', '', 'SPOLYARG', 'TIME1 - RSPSTART ,CSECS B-14.', kind='operand', line=558)
W('37,2165', 0o03301, '', '', 'SATRLRT', kind='operand', line=559)
W('37,2166', 0o45261, '', 'SL', 'DSU', kind='interp', line=560)
W('37,2167', 0o20217, '', '', '14D', kind='operand', line=561)
W('37,2170', 0o15333, '', '', 'DPHALF', kind='operand', line=562)
W('37,2171', 0o45215, '', 'DAD', 'DSU', 'ASSUMING X(SM) ALONG LAUNCH AZIMUTH,', kind='interp', line=563)
W('37,2172', 0o02634, '', '', 'LAUNCHAZ', 'LAUNCHAZ = ANGLE FROM NORTH TO X(SM).', kind='operand', line=564)
W('37,2173', 0o02401, '', '', 'AZIMUTH', 'AZIMUTH = -ANGLE FROM NORTH TO Z(S/C)', kind='operand', line=565)
W('37,2174', 0o77634, '', 'RTB', '', 'DETERMINE IF ROLLOUT', kind='interp', line=566)
W('37,2175', 0o70604, '', '', 'RLTST', 'IS COMPLETED', kind='operand', line=567)
W('37,2176', 0o71406, 'ATTDISPR', 'PUSH', 'COS', 'CONTINUE COMPUTING TSMV', kind='interp', line=568)
W('37,2177', 0o77606, '', 'PUSH', '', 'LET   R(RAD) = 2*PI*ROLL(REV)', kind='interp', line=569)
W('37,2200', 0o72405, '', 'DMP', 'SL1', kind='interp', line=570)
W('37,2201', 0o00017, '', '', '14D', kind='operand', line=571)
W('37,2202', 0o14027, '', 'STODL', '22D', '-.5*COS(R)*COS(P)', kind='interp', line=572)
W('37,2203', 0o77676, '', 'DCOMP', kind='interp', line=573)
W('37,2204', 0o00023, '', 'STORE', '18D', '-.5*COS(R)', kind='interp', line=574)
W('37,2205', 0o72405, '', 'DMP', 'SL1', kind='interp', line=575)
W('37,2206', 0o00013, '', '', '10D', kind='operand', line=576)
W('37,2207', 0o14033, '', 'STODL', '26D', '-.5*COS(R)*SIN(P)', kind='interp', line=577)
W('37,2210', 0o41556, '', 'SIN', 'PUSH', kind='interp', line=578)
W('37,2211', 0o00031, '', 'STORE', '24D', '.5*SIN(R)', kind='interp', line=579)
W('37,2212', 0o72405, '', 'DMP', 'SL1', kind='interp', line=580)
W('37,2213', 0o00017, '', '', '14D', kind='operand', line=581)
W('37,2214', 0o14021, '', 'STODL', '16D', '-.5*SIN(R)*COS(P)', kind='interp', line=582)
W('37,2215', 0o77676, '', 'DCOMP', kind='interp', line=583)
W('37,2216', 0o72405, '', 'DMP', 'SL1', kind='interp', line=584)
W('37,2217', 0o00013, '', '', '10D', kind='operand', line=585)
W('37,2220', 0o24025, '', 'STOVL', '20D', '-.5*SIN(R)*SIN(P)', kind='interp', line=586)
W('37,2221', 0o00013, '', '', '10D', kind='operand', line=587)

# FROM TSMV FIND THE HALF UNIT VECTORS XDC,YDC,ZDC = INPUT TO CALCGTA
# Page 544
W('37,2222', 0o77656, '', 'UNIT', kind='interp', line=591)
W('37,2223', 0o26714, '', 'STOVL', 'XDC', 'XDC = .5*UNIT(SIN(P),0,-COS(P))', kind='interp', line=592)
W('37,2224', 0o00021, '', '', '16D', kind='operand', line=593)
W('37,2225', 0o77656, '', 'UNIT', kind='interp', line=594)
W('37,2226', 0o26722, '', 'STOVL', 'YDC', 'YDC = .5*UNIT(-SIN(R)*COS(P),-COS(R),', kind='interp', line=595)
W('37,2227', 0o00027, '', '', '22D', '                      -SIN(R)*SIN(P))', kind='operand', line=596)
W('37,2230', 0o77656, '', 'UNIT', kind='interp', line=597)
W('37,2231', 0o36730, '', 'STCALL', 'ZDC', 'ZDC = .5*UNIT(-COS(R)*COS(P),SIN(R),', kind='interp', line=598)
W('37,2232', 0o47205, '', '', 'CALCGTA', '                      -COS(R)*SIN(P))', kind='operand', line=599)

# CALL CALCGTA TO COMPUTE DESIRED SM ORIENTATION  OGC,IGC,AND MGC
# -          -   -
# FIND DIFFERENCE VECTOR  DELTACDU = OGC-CDUX

# ENTER HERE IF ATTITUDE HOLD

W('37,2233', 0o41575, 'NOPOLYM', 'VLOAD', 'PUSH', '       OGC      IGC', kind='interp', line=607)
W('37,2234', 0o02760, '', '', 'OGC', 'CHANGE IGC  TO  MGC FOR COMPATIBILITY', kind='operand', line=608)
W('37,2235', 0o45006, '', 'PUSH', 'CALL', '       MGC      OGC', kind='interp', line=609)
W('37,2236', 0o47477, '', '', 'CDUTRIG', 'WITH Y,Z,X ORDER OF CDUSPOT', kind='operand', line=610)
W('37,2237', 0o47175, '', 'VLOAD', 'RTB', ' -         DPHI     OGC-CDUX ,PD4', kind='interp', line=611)
W('37,2240', 0o00003, '', '', '2', 'DELTACDU = DTHETA = IGC-CDUY ,   0', kind='operand', line=612)
W('37,2241', 0o45552, '', '', 'V1STO2S', '           DPSI     MGC-CDUZ ,   2', kind='operand', line=613)
W('37,2242', 0o27317, '', 'STOVL', 'BOOSTEMP', kind='interp', line=614)
W('37,2243', 0o15335, '', '', 'ZEROVECS', kind='operand', line=615)
W('37,2244', 0o24001, '', 'STOVL', '0', kind='interp', line=616)
W('37,2245', 0o00767, '', '', 'CDUSPOT', kind='operand', line=617)
W('37,2246', 0o47034, '', 'RTB', 'RTB', kind='interp', line=618)
W('37,2247', 0o45552, '', '', 'V1STO2S', kind='operand', line=619)
W('37,2250', 0o70564, '', '', 'DELSTOR', kind='operand', line=620)
W('37,2251', 0o14013, '', 'STODL', '10D', kind='interp', line=621)
W('37,2252', 0o00741, '', '', 'SINCDUZ', kind='operand', line=622)
W('37,2253', 0o72405, '', 'DMP', 'SL1', kind='interp', line=623)
W('37,2254', 0o00001, '', '', '0', kind='operand', line=624)
W('37,2255', 0o60415, '', 'DAD', 'SR2', 'CHANGE SCALE OF AK TO 2REVS', kind='interp', line=625)
W('37,2256', 0o00005, '', '', '4', kind='operand', line=626)
W('37,2257', 0o77650, '', 'GOTO', kind='interp', line=627)
W('37,2260', 0o70416, '', '', 'ATTDISP2', kind='operand', line=628)

#   SETLOC P11ONE
#   BANK
#   COUNT 34/P11

W('34,2416', 0o14021, 'ATTDISP2', 'STODL', '16D', '16D, .5(DPHI + DTHETA*SIN(CDUZ))', kind='interp', line=634)
W('34,2417', 0o00747, '', '', 'COSCDUZ', kind='operand', line=635)
W('34,2420', 0o41405, '', 'DMP', 'PUSH', kind='interp', line=636)
W('34,2421', 0o00001, '', '', '0', kind='operand', line=637)
W('34,2422', 0o72405, '', 'DMP', 'SL1', kind='interp', line=638)
W('34,2423', 0o00751, '', '', 'COSCDUX', kind='operand', line=639)
W('34,2424', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=640)
# Page 545
W('34,2425', 0o00743, '', '', 'SINCDUX', kind='operand', line=642)
W('34,2426', 0o00003, '', '', '2', kind='operand', line=643)
W('34,2427', 0o72415, '', 'DAD', 'SL1', kind='interp', line=644)
W('34,2430', 0o77626, '', 'STADR', kind='interp', line=645)
W('34,2431', 0o63755, '', 'STODL', '17D', '17D,  .5(DTHETA*COS(CDUX)*COS(CDUZ)', kind='interp', line=646)
W('34,2432', 0o72405, '', 'DMP', 'SL1', '                      +DPSI*SIN(CDUX))', kind='interp', line=647)
W('34,2433', 0o00743, '', '', 'SINCDUX', kind='operand', line=648)
W('34,2434', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=649)
W('34,2435', 0o00751, '', '', 'COSCDUX', kind='operand', line=650)
W('34,2436', 0o00003, '', '', '2', kind='operand', line=651)
W('34,2437', 0o72425, '', 'DSU', 'SL1', kind='interp', line=652)
W('34,2440', 0o77626, '', 'STADR', kind='interp', line=653)
W('34,2441', 0o77754, '', 'STORE', '18D', '18D,  .5(-DTHETA*SIN(CDUX)*COS(CDUZ)', kind='interp', line=654)
W('34,2442', 0o77751, '', 'TLOAD', '', '                      +DPSI*COS(CDUX))', kind='interp', line=655)
W('34,2443', 0o00021, '', '', '16D', kind='operand', line=656)
W('34,2444', 0o03077, '', 'STORE', 'AK', 'STORE ATTITUDE ERRORS IN AK,AK1,AK2', kind='interp', line=657)
W('34,2445', 0o77776, '', 'EXIT', kind='interp', line=658)

W('34,2446', 0o31725, '', 'CA', 'SATSW', line=660)
W('34,2447', 0o10000, '', 'CCS', 'A', 'CHK TAKEOVER STATUS', line=661)
W('34,2450', 0o02471, '', 'TC', 'SATOUT', 'POS - DISPLAY ONLY', line=662)
W('34,2451', 0o02477, '', 'TC', 'AKLOAD', '0     STORE BIAS', line=663)
W('34,2452', 0o06006, 'STEERSAT', 'TC', 'INTPRET', 'NEG   STEER L/V', line=664)
W('34,2453', 0o76351, '', 'TLOAD', 'TAD', kind='interp', line=665)
W('34,2454', 0o03327, '', '', 'BIASAK', kind='operand', line=666)
W('34,2455', 0o03077, '', '', 'AK', kind='operand', line=667)
W('34,2456', 0o03077, '', 'STORE', 'AK', 'AKS = AKS - STORED BIAS', kind='interp', line=668)
W('34,2457', 0o77776, '', 'EXIT', kind='interp', line=669)
W('34,2460', 0o31476, '', 'CA', 'AK', line=670)
W('34,2461', 0o02623, '', 'TC', 'RESCALES', line=671)
W('34,2462', 0o55476, '', 'TS', 'AK', line=672)
W('34,2463', 0o31477, '', 'CA', 'AK1', line=673)
W('34,2464', 0o02623, '', 'TC', 'RESCALES', line=674)
W('34,2465', 0o55477, '', 'TS', 'AK1', line=675)
W('34,2466', 0o31500, '', 'CA', 'AK2', line=676)
W('34,2467', 0o02623, '', 'TC', 'RESCALES', line=677)
W('34,2470', 0o55500, '', 'TS', 'AK2', line=678)
# DISPLAY ATTITUDE ERRORS ON FDAI VIA NEEDLER

W('34,2471', 0o04662, 'SATOUT', 'TC', 'BANKCALL', line=681)
W('34,2472', 0o42420, '', 'CADR', 'NEEDLER', kind='data', line=682)
W('34,2473', 0o34113, 'ATERSET', 'CAF', 'OCT31', 'DELAY .25 SEC', line=683)
W('34,2474', 0o04662, '', 'TC', 'BANKCALL', 'EXECUTION + DELAY =.56SEC APPROX', line=684)
W('34,2475', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=685)
W('34,2476', 0o02345, '', 'TC', 'ATERJOB', 'END OF ATT ERROR DISPLAY CYCLE', line=686)

W('34,2477', 0o41476, 'AKLOAD', 'CS', 'AK', 'STORE AKS', line=688)
W('34,2500', 0o55726, '', 'TS', 'BIASAK', 'INTO BIAS', line=689)
W('34,2501', 0o41477, '', 'CS', 'AK1', 'COMPLEMENTED', line=690)
W('34,2502', 0o55727, '', 'TS', 'BIASAK +1', line=691)
# Page 546
W('34,2503', 0o41500, '', 'CS', 'AK2', line=693)
W('34,2504', 0o55730, '', 'TS', 'BIASAK +2', line=694)
W('34,2505', 0o45017, '', 'CS', 'BIT1', 'SET SW', line=695)
W('34,2506', 0o55725, '', 'TS', 'SATSW', 'TO STEER', line=696)
W('34,2507', 0o02452, '', 'TC', 'STEERSAT', 'GO STEER', line=697)
W('34,2510', 0o31725, 'STRSAT', 'CA', 'SATSW', 'CHECK IF NEEDLER', line=698)
W('34,2511', 0o00006, '', 'EXTEND', '', 'HAS BEEN INITIALIZED', line=699)
W('34,2512', 0o62363, '', 'BZMF', 'ATTDISP', 'YES - CONTINUE', line=700)
W('34,2513', 0o41501, 'ATRESET', 'CS', 'RCSFLAGS', 'NO - SET', line=701)
W('34,2514', 0o75015, '', 'MASK', 'BIT3', 'INITIALIZATION SW', line=702)
W('34,2515', 0o27501, '', 'ADS', 'RCSFLAGS', 'FOR NEEDLER', line=703)
W('34,2516', 0o04662, '', 'TC', 'BANKCALL', 'AND GO', line=704)
W('34,2517', 0o42420, '', 'CADR', 'NEEDLER', 'DO IT', kind='data', line=705)
W('34,2520', 0o36211, '', 'CAF', 'REVCNT', 'OCT 6', line=706)
W('34,2521', 0o04662, '', 'TC', 'BANKCALL', 'DELAY JOB', line=707)
W('34,2522', 0o01732, '', 'CADR', 'DELAYJOB', '60 MS -WAIT TILL IMUERRCNTR ZEROED', kind='data', line=708)
W('34,2523', 0o11725, '', 'CCS', 'SATSW', 'CHECK SW STATUS', line=709)
W('34,2524', 0o02534, '', 'TC', 'TAKEON', 'POS   STEER INIT.', line=710)
W('34,2525', 0o02526, '', 'TC', '+1', '0     RETURN TO DISPLAY', line=711)
W('34,2526', 0o35017, '', 'CA', 'BIT1', 'NEG   RETURN TO DISPLAY', line=712)
W('34,2527', 0o55725, '', 'TS', 'SATSW', 'SW = DISPLAY ON', line=713)
W('34,2530', 0o45007, '', 'CS', 'BIT9', 'DISABLE', line=714)
W('34,2531', 0o00006, '', 'EXTEND', '', 'SIVB', line=715)
W('34,2532', 0o03012, '', 'WAND', 'CHAN12', 'TAKEOVER', line=716)
W('34,2533', 0o02471, '', 'TC', 'SATOUT', 'DISPLAY', line=717)
W('34,2534', 0o35007, 'TAKEON', 'CAF', 'BIT9', 'ENABLE', line=718)
W('34,2535', 0o00006, '', 'EXTEND', '', 'SIVB', line=719)
W('34,2536', 0o05012, '', 'WOR', 'CHAN12', 'TAKEOVER', line=720)
W('34,2537', 0o35021, '', 'CA', 'ZERO', 'INDICATE NEEDLER', line=721)
W('34,2540', 0o55725, '', 'TS', 'SATSW', 'WAS INITIALIZED', line=722)
W('34,2541', 0o02471, '', 'TC', 'SATOUT', line=723)
W('34,2542', 0o51575, 'S11.1', 'VLOAD', 'ABVAL', kind='interp', line=724)
W('34,2543', 0o01177, '', '', 'VN', kind='operand', line=725)
W('34,2544', 0o27723, '', 'STOVL', 'VMAGI', 'VI    SCALED 2(7) IN METERS/CSEC', kind='interp', line=726)
W('34,2545', 0o01171, '', '', 'RN', kind='operand', line=727)
W('34,2546', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=728)
W('34,2547', 0o01177, '', '', 'VN', kind='operand', line=729)
W('34,2550', 0o77752, '', 'SL1', kind='interp', line=730)
W('34,2551', 0o17737, '', 'STODL', 'HDOT', kind='interp', line=731)
W('34,2552', 0o05152, '', '', 'RPAD', kind='operand', line=732)
W('34,2553', 0o77214, '', 'BOF', 'VLOAD', kind='interp', line=733)
W('34,2554', 0o00355, '', '', 'AMOONFLG', kind='operand', line=734)
W('34,2555', 0o70560, '', '', 'EARTHALT', kind='operand', line=735)
W('34,2556', 0o02026, '', '', 'RLS', kind='operand', line=736)
W('34,2557', 0o60446, '', 'ABVAL', 'SR2', kind='interp', line=737)
W('34,2560', 0o77621, 'EARTHALT', 'BDSU', kind='interp', line=738)
W('34,2561', 0o00045, '', '', '36D', kind='operand', line=739)
W('34,2562', 0o03735, '', 'STORE', 'ALTI', kind='interp', line=740)
W('34,2563', 0o77616, '', 'RVQ', kind='interp', line=741)
W('34,2564', 0o31716, 'DELSTOR', 'CA', 'BOOSTEMP', line=742)
# Page 547
W('34,2565', 0o00006, '', 'EXTEND', '', 'STORE DELTACDU INTO PDL 0,2,4', line=744)
W('34,2566', 0o20154, '', 'MSU', 'MPAC', line=745)
W('34,2567', 0o50120, '', 'INDEX', 'FIXLOC', line=746)
W('34,2570', 0o54000, '', 'TS', '0', line=747)
W('34,2571', 0o31717, '', 'CA', 'BOOSTEMP +1', line=748)
W('34,2572', 0o00006, '', 'EXTEND', line=749)
W('34,2573', 0o20155, '', 'MSU', 'MPAC +1', line=750)
W('34,2574', 0o50120, '', 'INDEX', 'FIXLOC', line=751)
W('34,2575', 0o54002, '', 'TS', '2', line=752)
W('34,2576', 0o31720, '', 'CA', 'BOOSTEMP +2', line=753)
W('34,2577', 0o00006, '', 'EXTEND', line=754)
W('34,2600', 0o20156, '', 'MSU', 'MPAC +2', line=755)
W('34,2601', 0o50120, '', 'INDEX', 'FIXLOC', line=756)
W('34,2602', 0o54004, '', 'TS', '4', line=757)
W('34,2603', 0o16030, '', 'TCF', 'DANZIG', line=758)
W('34,2604', 0o30154, 'RLTST', 'CA', 'MPAC', 'DETERMINE IF ROLLOUT', line=759)
W('34,2605', 0o00006, '', 'EXTEND', '', 'IS COMPLETED', line=760)
W('34,2606', 0o71701, '', 'MP', 'SATRLRT +1', line=761)
W('34,2607', 0o00006, '', 'EXTEND', line=762)
W('34,2610', 0o66030, '', 'BZMF', 'DANZIG', 'UNLIKE SIGNS STILL ROLLING', line=763)
W('34,2611', 0o00006, '', 'EXTEND', '', 'ROLLOUT COMPLETED', line=764)
W('34,2612', 0o33672, '', 'DCA', 'MBDYTCTL +2', 'ZERO OUT ROLL CONTRIBUTION', line=765)
W('34,2613', 0o52155, '', 'DXCH', 'MPAC', line=766)
W('34,2614', 0o06030, '', 'TC', 'DANZIG', line=767)
W('34,2615', 0o06006, 'NOPOLY', 'TC', 'INTPRET', 'COMES HERE IF', line=768)
W('34,2616', 0o52001, '', 'SETPD', 'GOTO', 'ATTITUDE HOLD', kind='interp', line=769)
W('34,2617', 0o00001, '', '', '0', kind='operand', line=770)
W('34,2620', 0o76233, '', '', 'NOPOLYM', kind='operand', line=771)
W('34,2621', 0o01673, 'COEFPOLY', 'ADRES', 'POLYLOC', kind='data', line=772)
W('34,2622', 0o01476, 'V06N62', 'VN', '0662', kind='data', line=773)
W('34,2623', 0o00006, 'RESCALES', 'EXTEND', '', 'RESCALE AK S FOR', line=774)
W('34,2624', 0o71731, '', 'MP', 'SATSCALE', 'NEW HARDWARE', line=775)
W('34,2625', 0o20001, '', 'DDOUBL', '', 'SCALING FOR', line=776)
W('34,2626', 0o20001, '', 'DDOUBL', '', 'STEERING', line=777)
W('34,2627', 0o00002, '', 'TC', 'Q', 'SATURN', line=778)
# SATURN TAKEOVER FUNCTION
# ************************

# PROGRAM DESCRIPTION

# MOD NUMBER 1
# MOD BY ELIASSEN

# FUNCTIONAL DESCRIPTION

# DURING THE COASTING PHASE OF SIVB ATTACHED, THE
# ASTRONAUT MAY REQUEST SATURN TAKEOVER THROUGH
# EXTENDED VERB 46 (BITS 13,14 OF DAPDATR1 SET ).
# THE CMC REGARDS RHC COMMANDS AS BODY-AXES RATE
# COMMANDS AND IT TRANSMITS THESE TO SATURN AS DC
# Page 548
# VOLTAGES.  THE VALUE OF THE CONSTANT RATE COMMAND
# IS 0.5 DEG/SEC.  AN ABSENCE OF RHC ACTIVITY RE-
# SULTS IN A ZERO RATE COMMAND.

# THE FDAI ERROR NEEDLES WILL INDICATE THE VALUE
# OF THE RATE COMMAND.

# CALLING SEQUENCE
#
# DAPFIG +9D      TC      POSTJUMP
# CADR    SATSTKON

# SUBROUTINES CALLED

# ENDEXT
# IBNKCALL
# STICKCHK
# NEEDLER
# T5RUPT
# RESUME

# ASTRONAUT REQUESTS

# ENTRY   - VERB 46 ENTER
# (CONDITION - BITS 13, 14 OF DAPDATR1 SET)
#
# EXIT    - VERB 48 ENTER (FLASH V06N46)
# VERB 21 ENTER AXXXX ENTER WHERE A=0 OR 1
# VERB 34 ENTER
# VERB 46 ENTER

# NORMAL EXIT MODE

# VERB 46 ENTER   (SEE ASTRONAUT ABOVE)

# ALARM OR ABORT EXIT MODES

# NONE

# OUTPUT

# SATURN RATES IN CDUXCMD, CDUYCMD, CDUZCMD

# ERASABLE INITIALIZATION

# DAPDATR1        (BITS 13,14 MUST BE SET)

# DEBRIS

# CENTRALS
# Page 549
# CDUXCMD, CDUYCMD, CDUZCMD

#   BANK 43
#   SETLOC EXTVERBS
#   BANK

#   COUNT 23/STTKE
W('43,3215', 0o00006, 'SATSTKON', 'EXTEND', line=853)
W('43,3216', 0o33233, '', 'DCA', '2REDOSAT', line=854)
W('43,3217', 0o00004, '', 'INHINT', line=855)
W('43,3220', 0o53313, '', 'DXCH', 'T5LOC', line=856)
W('43,3221', 0o34777, '', 'CAF', 'POSMAX', line=857)
W('43,3222', 0o54030, '', 'TS', 'TIME5', line=858)
W('43,3223', 0o40102, '', 'CS', 'FLAGWRD6', 'TURN ON BITS 15,14 OF', line=859)
W('43,3224', 0o74105, '', 'MASK', 'RELTAB11', 'FLAGWRD6', line=860)
W('43,3225', 0o26102, '', 'ADS', 'FLAGWRD6', '      SATSTICK CONTROL OF T5', line=861)
W('43,3226', 0o04740, '', 'TC', 'IBNKCALL', 'ZERO JET CHANNELS IN 14 MS AND THEN', line=862)
W('43,3227', 0o42632, '', 'CADR', 'ZEROJET', 'LEAVE THE T6 CLOCK DISABLED', kind='data', line=863)
W('43,3230', 0o00003, '', 'RELINT', line=864)
W('43,3231', 0o02121, '', 'TC', 'GOPIN', 'EXIT THUS BECAUSE WE CAME VIA V46', line=865)

#   EBANK= BODY3
W('43,3232', 0o02765, '2REDOSAT', '2CADR', 'REDOSAT', kind='data', line=868)
W('43,3233', 0o46106, kind='data', line=868)

#   SBANK= LOWSUPER
#   BANK 32
#   SETLOC P11FOUR
#   BANK

W('23,2765', 0o22016, 'REDOSAT', 'LXCH', 'BANKRUPT', 'ALSO COMES HERE FOR RESTARTS', line=876)
W('23,2766', 0o00006, '', 'EXTEND', line=877)
W('23,2767', 0o22012, '', 'QXCH', 'QRUPT', line=878)
W('23,2770', 0o41501, '', 'CS', 'RCSFLAGS', 'TURN ON BIT3 OF RCSFLAGX', line=879)
W('23,2771', 0o75015, '', 'MASK', 'BIT3', 'FOR', line=880)
W('23,2772', 0o27501, '', 'ADS', 'RCSFLAGS', 'NEEDLER INITIALIZATION', line=881)
W('23,2773', 0o04740, '', 'TC', 'IBNKCALL', line=882)
W('23,2774', 0o42420, '', 'CADR', 'NEEDLER', 'DISABLE IMU ERR COUNTERS ETC.', kind='data', line=883)
W('23,2775', 0o35007, '', 'CAF', 'BIT9', 'SIVB', line=884)
W('23,2776', 0o00006, '', 'EXTEND', '', 'TAKEOVER', line=885)
W('23,2777', 0o05012, '', 'WOR', 'CHAN12', 'ENABLE', line=886)
W('23,3000', 0o00006, '', 'EXTEND', '', 'SET UP T5 CYCLE', line=887)
W('23,3001', 0o33042, '', 'DCA', '2SATSTCK', line=888)
W('23,3002', 0o53313, '', 'DXCH', 'T5LOC', line=889)
W('23,3003', 0o33040, '', 'CAF', '100MST5', 'IN 100 MSECS', line=890)
W('23,3004', 0o54030, '', 'TS', 'TIME5', line=891)
W('23,3005', 0o15333, '', 'TCF', 'RESUME', 'END OF SATURN STICK INITIALIZATION', line=892)

# THIS SECTION IS EXECUTED EVERY 100 MSECS
# Page 550
W('23,3006', 0o22016, 'SATSTICK', 'LXCH', 'BANKRUPT', line=896)
W('23,3007', 0o00006, '', 'EXTEND', line=897)
W('23,3010', 0o22012, '', 'QXCH', 'QRUPT', line=898)

W('23,3011', 0o33041, '', 'CAF', '2SATSTCK', 'SET UP RUPT', line=900)
W('23,3012', 0o55312, '', 'TS', 'T5LOC', 'LO ORDER LOC SET', line=901)
W('23,3013', 0o33040, '', 'CAF', '100MST5', '100 MSECS', line=902)
W('23,3014', 0o54030, '', 'TS', 'TIME5', line=903)
W('23,3015', 0o33037, '', 'CAF', 'STIKBITS', line=904)
W('23,3016', 0o00006, '', 'EXTEND', line=905)
W('23,3017', 0o06031, '', 'RXOR', 'CHAN31', 'CHECK IF MAN ROT BITS SAME', line=906)
W('23,3020', 0o73037, '', 'MASK', 'STIKBITS', line=907)
W('23,3021', 0o04740, '', 'TC', 'IBNKCALL', 'SET RATE INDICES', line=908)
W('23,3022', 0o43130, '', 'CADR', 'STICKCHK', 'FOR PITCH YAW AND ROLL', kind='data', line=909)

W('23,3023', 0o51656, '', 'INDEX', 'RMANNDX', 'SET SATURN RATES', line=911)
W('23,3024', 0o31721, '', 'CA', 'SATRATE', line=912)
W('23,3025', 0o55476, '', 'TS', 'AK', '              ROLL', line=913)
W('23,3026', 0o51657, '', 'INDEX', 'PMANNDX', line=914)
W('23,3027', 0o31721, '', 'CA', 'SATRATE', line=915)
W('23,3030', 0o55477, '', 'TS', 'AK1', '              PITCH', line=916)
W('23,3031', 0o51660, '', 'INDEX', 'YMANNDX', line=917)
W('23,3032', 0o31721, '', 'CA', 'SATRATE', line=918)
W('23,3033', 0o55500, '', 'TS', 'AK2', '              YAW', line=919)

W('23,3034', 0o04740, '', 'TC', 'IBNKCALL', 'FOR SATURN INTERFACE AND FDAI DISPLAY', line=921)
W('23,3035', 0o42420, '', 'CADR', 'NEEDLER', kind='data', line=922)
W('23,3036', 0o15333, '', 'TCF', 'RESUME', 'END OF SATURN STICK CONTROL', line=923)

W('23,3037', 0o00077, 'STIKBITS', 'OCT', '00077', kind='data', line=925)
W('23,3040', 0o37766, '100MST5', 'DEC', '16374', kind='data', line=926)
#   EBANK= BODY3
W('23,3041', 0o03006, '2SATSTCK', '2CADR', 'SATSTICK', kind='data', line=928)
W('23,3042', 0o46066, kind='data', line=928)
