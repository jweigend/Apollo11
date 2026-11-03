"""P30_P37.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P30_P37.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 614-617 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P30_P37', 'P30_P37.agc', 'Luminary099', pages='614-617')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P30_P37.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        614-617
# Mod history:  2009-05-17 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2009-06-05 RSB  Removed 4 lines of code that shouldn't
# have survived from Luminary 131.
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

# Page 614
# PROGRAM DESCRIPTION P30       DATE 3-6-67
#
# MOD.1 BY RAMA AIYAWAR
# FUNCTIONAL DESCRIPTION
# ACCEPT ASTRONAUT INPUTS OF TIG.DELV(LV)
# CALL IMU STATUS CHECK ROUTINE (R02)
# DISPLAY TIME TO GO, APOGEE, PERIGEE, DELV(MAG), MGA AT IGN
# REQUEST BURN PROGRAM
#
# CALLING SEQUENCE VIA JOB FROM V37
#
# EXIT VIA V37 CALL OR TO GOTOPOOH (V34E)
#
# SUBROUTINE CALLS-FLAGUP, PHASCHNG, BANKCALL, ENDOFJOB, GOFLASH, GOFLASHR
# GOPERF3R, INTPRET, BLANKET, GOTOPOOH, R02BOTH, S30.1,
# TIG/N35, MIDGIM, DISPMGA
#
# ERASABLE INITIALIZATION- STATE VECTOR
#
# OUTPUT-RINIT, VINIT, +MGA, VTIG, RTIG, DELVSIN, DELVSAB, DELVSLV, HAPO,
# HPER, TTOGO
#
# DEBRIS- A,L, MPAC, PUSHLIST

#   BANK 32
#   SETLOC P30S
#   BANK
#   EBANK= +MGA
#   COUNT* $$/P30
W('35,2000', 0o05504, 'P30', 'TC', 'UPFLAG', 'SET UPDATE FLAG', line=61)
W('35,2001', 0o00027, '', 'ADRES', 'UPDATFLG', kind='data', line=62)
W('35,2002', 0o05504, '', 'TC', 'UPFLAG', 'SET TRACK FLAG', line=63)
W('35,2003', 0o00031, '', 'ADRES', 'TRACKFLG', kind='data', line=64)

W('35,2004', 0o32025, 'P30N33', 'CAF', 'V06N33', 'T OF IGN', line=66)
W('35,2005', 0o03712, '', 'TC', 'VNPOOH', 'RETURNS ON PROCEED, POOH ON TERMINATE', line=67)

W('35,2006', 0o33727, '', 'CAF', 'V06N81', 'DISPLAY DELTA V (LV)', line=69)
W('35,2007', 0o03712, '', 'TC', 'VNPOOH', '    REDISPLAY ON RECYCLE', line=70)

W('35,2010', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET UPDATE FLAG', line=72)
W('35,2011', 0o00027, '', 'ADRES', 'UPDATFLG', kind='data', line=73)
W('35,2012', 0o06037, '', 'TC', 'INTPRET', line=74)
W('35,2013', 0o77624, '', 'CALL', kind='interp', line=75)
W('35,2014', 0o70000, '', '', 'S30.1', kind='operand', line=76)
W('35,2015', 0o77414, '', 'SET', 'EXIT', kind='interp', line=77)
W('35,2016', 0o00470, '', '', 'UPDATFLG', kind='operand', line=78)
W('35,2017', 0o32026, 'PARAM30', 'CAF', 'V06N42', 'DISPLAY APOGEE,PERIGEE ,DELTA V', line=79)
W('35,2020', 0o03712, '', 'TC', 'VNPOOH', line=80)
# Page 615

W('35,2021', 0o06037, '', 'TC', 'INTPRET', line=83)
W('35,2022', 0o77614, '', 'SETGO', kind='interp', line=84)
W('35,2023', 0o01027, '', '', 'XDELVFLG', "FOR P40'S: EXTERNAL DELTA-V GUIDANCE.", kind='operand', line=85)
W('35,2024', 0o72540, '', '', 'REVN1645', 'TRKMKCNT, T60, +MGA  DISPLAY', kind='operand', line=86)

W('35,2025', 0o01441, 'V06N33', 'VN', '0633', kind='data', line=88)
W('35,2026', 0o01452, 'V06N42', 'VN', '0642', kind='data', line=89)

# Page 616
# PROGRAM DESCRIPTION S30.1     DATE 9NOV66
# MOD NO 1                      LOG SECTION P30,P37
# MOD BY RAMA AIYAWAR **
# FUNCTIONAL DESCRIPTION
# BASED ON STORED TARGET PARAMETERS(R OF IGNITION(RTIG),V OF
# IGNITION(VTIG),TIME OF IGNITION (TIG)),COMPUTE PERIGEE ALTITUDE
# APOGEE ALTITUDE AND DELTAV REQUIRED(DELVSIN).
# CALLING SEQUENCE
# L       CALL
# L+1             s30.1
# NORMAL EXIT MODE
# AT L+2 OR CALLING SEQUENCE (GOTO L+2)
# SUBROUTINES CALLED
# LEMPREC
# PERIAPO
# ALARM OR ABORT EXIT MODES
# NONE
# ERASABLE INITIALIZATION REQUIRED
# TIG             TIME OF IGNITION        DP B28CS
# DELVSLV         SPECIFIED DELTA-V IN LOCAL VERT.
# COORDS. OF ACTIVE VEHICLE AT
# TIME OF IGNITION        VECTOR  B+7 METERS/CS
#
# OUTPUT
# RTIG            POSITION AT TIG         VECTOR  B+29 METERS
# VTIG            VELOCITY AT TIG         VECTOR  B+29 METERS/CS
# PDL 4D          APOGEE ALTITUDE         DP      B+29 M ,  B+27 METERS.
# HAPO            APOGEE ALTITUDE         DP      B+29 METERS
# PDL 8D          PERIGEE ALTITUDE        DP      B+29 M ,  B+27 METERS.
# HPER            PERIGEE ALTITUDE        DP      B+29 METERS
# DELVSIN         SPECIFIED DELTA-V IN INTERTIAL
# COORD. OF ACTIVE VEHICLE AT
# TIME OF IGNITION        VECTOR  B+7 METERS/CS
# DELVSAB         MAG. OF DELVSIN         VECTOR  B+7 METERS/CS
#
# DEBRIS        QTEMP   TEMP. ERASABLE
# QPRET,MPAC
# PUSHLIST

#   SETLOC P30S1
#   BANK

#   COUNT* $$/S30S

W('34,2000', 0o71220, 'S30.1', 'STQ', 'DLOAD', kind='interp', line=136)
W('34,2001', 0o03632, '', '', 'QTEMP', kind='operand', line=137)
W('34,2002', 0o03442, '', '', 'TIG', 'TIME IGNITION SCALED AT 2(+28)CS', kind='operand', line=138)
W('34,2003', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=139)
W('34,2004', 0o27057, '', '', 'LEMPREC', 'ENCKE ROUTINE FOR LEM', kind='operand', line=140)

W('34,2005', 0o67175, '', 'VLOAD', 'SXA,2', kind='interp', line=142)
# Page 617
W('34,2006', 0o00001, '', '', 'RATT', kind='operand', line=144)
W('34,2007', 0o02777, '', '', 'RTX2', kind='operand', line=145)
W('34,2010', 0o03642, '', 'STORE', 'RTIG', 'RADIUS VECTOR AT IGNITION TIME', kind='interp', line=146)
W('34,2011', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=147)
W('34,2012', 0o27656, '', 'STOVL', 'DELVSIN', 'ZRF/LV IN DELVSIN SCALED AT 2', kind='interp', line=148)
W('34,2013', 0o00007, '', '', 'VATT', 'VELOCITY VECTOR AT TIG, SCALED 2(7) M/CS', kind='operand', line=149)
W('34,2014', 0o03650, '', 'STORE', 'VTIG', kind='interp', line=150)
W('34,2015', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=151)
W('34,2016', 0o03642, '', '', 'RTIG', kind='operand', line=152)
W('34,2017', 0o66001, '', 'SETPD', 'SXA,1', kind='interp', line=153)
W('34,2020', 0o00001, '', '', '0', kind='operand', line=154)
W('34,2021', 0o02776, '', '', 'RTX1', kind='operand', line=155)
W('34,2022', 0o47206, '', 'PUSH', 'VXV', 'YRF/LV PDL 0  SCALED AT 2', kind='interp', line=156)
W('34,2023', 0o03656, '', '', 'DELVSIN', kind='operand', line=157)
W('34,2024', 0o63372, '', 'VSL1', 'PDVL', kind='interp', line=158)
W('34,2025', 0o63315, '', 'PDVL', 'PDVL', 'YRF/LV PDL 6 SCALED AT 2', kind='interp', line=159)
W('34,2026', 0o03656, '', '', 'DELVSIN', 'ZRF/LV PDL 12D SCALED AT 2', kind='operand', line=160)
W('34,2027', 0o03434, '', '', 'DELVSLV', kind='operand', line=161)
W('34,2030', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=162)
W('34,2031', 0o00001, '', '', '0', kind='operand', line=163)
W('34,2032', 0o03656, '', 'STORE', 'DELVSIN', 'DELTAV IN INERT. COOR. SCALED TO B+7M/CS', kind='interp', line=164)
W('34,2033', 0o77646, '', 'ABVAL', kind='interp', line=165)
W('34,2034', 0o27664, '', 'STOVL', 'DELVSAB', 'DELTA V MAG.', kind='interp', line=166)
W('34,2035', 0o03642, '', '', 'RTIG', '(FOR PERIAPO)', kind='operand', line=167)
W('34,2036', 0o53315, '', 'PDVL', 'VAD', 'VREQUIRED = VTIG + DELVSIN (FOR PERIAPO)', kind='interp', line=168)
W('34,2037', 0o03650, '', '', 'VTIG', kind='operand', line=169)
W('34,2040', 0o03656, '', '', 'DELVSIN', kind='operand', line=170)
W('34,2041', 0o77624, '', 'CALL', kind='interp', line=171)
W('34,2042', 0o46316, '', '', 'PERIAPO1', kind='operand', line=172)
W('34,2043', 0o77624, '', 'CALL', kind='interp', line=173)
W('34,2044', 0o46426, '', '', 'SHIFTR1', 'RESCALE IF NEEDED', kind='operand', line=174)
W('34,2045', 0o77624, '', 'CALL', '', 'LIMIT DISPLAY TO 9999.9 N. MI.', kind='interp', line=175)
W('34,2046', 0o45636, '', '', 'MAXCHK', kind='operand', line=176)
W('34,2047', 0o16321, '', 'STODL', 'HPER', 'PERIGEE ALT 2(29) METERS, FOR DISPLAY', kind='interp', line=177)
W('34,2050', 0o00005, '', '', '4D', kind='operand', line=178)
W('34,2051', 0o77624, '', 'CALL', kind='interp', line=179)
W('34,2052', 0o46426, '', '', 'SHIFTR1', 'RESCALE IF NEEDED', kind='operand', line=180)
W('34,2053', 0o77624, '', 'CALL', '', 'LIMIT DISPLAY TO 9999.9 N. MI.', kind='interp', line=181)
W('34,2054', 0o45636, '', '', 'MAXCHK', kind='operand', line=182)
W('34,2055', 0o36317, '', 'STCALL', 'HAPO', 'APOGEE  ALT 2(29) METERS, FOR DISPLAY', kind='interp', line=183)
W('34,2056', 0o03632, '', '', 'QTEMP', kind='operand', line=184)
