"""P51-P53.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P51-P53.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 737-784 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P51_P53', 'P51-P53.agc', 'Comanche055', pages='737-784')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P51-P53.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 737-784
# Contact:      Ron Burkey <info@sandroid.org>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-12 RSB  Adapted from Colossus249 file of the same
# name, and Comanche 055 page images.
# 2009-05-20 RSB  Corrections: SETI/PDT -> SET1/PDT,
# GOTOPOOH -> GOTOPOOH, R33EXIT -> R53EXIT,
# V853 -> VB53, R56A -> R56A1 (some places
# only), added missing R56A1 label, added a
# missing CAF in COARSTYP, corrected a SETLOC
# from P50S to P50S3.
# 2009-05-21 RSB  In COARFINE, a TC BANKCALL was corrected to
# TC PHASCHNG.  In R53C, a CADR GOFLASHR was
# corrected to CADR GOFLASH.
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

# Page 737
# PROGRAM NAME -- PROG52                        DATE -- NOV 30, 1966
# MOD NO -- 2                                   LOG SECTION -- P51-P53
# MODIFICATION BY -- LONSKE                     ASSEMBLY -- SUNDISK REV 30
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
# X   = UNIT ( Y   x Z   )
# -SM          -SM   -SM
#
# Y   = UNIT (V X R)
# -SM         -   -
#
# Z   = UNIT ( -R )
# -SM           -
#
# WHERE:
#
# R = THE GEOMETRIC RADIUS VECTOR AT TIME T(ALIGN) SELECTED BY THE ASTRONAUT
# -
#
# V = THE INERTIAL VELOCITY VECTOR AT TIME T(ALIGN) SELECTED BY THE ASTRONAUT
# -
#
# (C)     RERSMMAT ORIENTATION
#
# THIS SELECTION CORRECTS THE PRESENT IMU ORIENTATION.  THE PRESENT ORIENTATION DIFFERS FROM THAT TO WHICH IT
# WAS LAST ALIGNED ONLY DUE TO GYRO DRIVE (I.E., NEITHER GIMBAL LOCK NOR IMU POWER INTERRUPT HAS OCCURRED
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
# THE PROGRAM IS CALLED BY THE ASTRONAUT BY DSKY ENTRY.
# Page 738
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

S('P54', 'equals', 0o42000, line=132)
#   BANK 33
#   SETLOC P50S
#   BANK

#   SBANK= LOWSUPER
#   EBANK= SAC
#   COUNT 15/P52

W('15,2000', 0o05412, 'PROG52', 'TC', 'PHASCHNG', line=141)
W('15,2001', 0o00254, '', 'OCT', '00254', kind='data', line=142)
W('15,2002', 0o05560, '', 'TC', 'DOWNFLAG', line=143)
W('15,2003', 0o00027, '', 'ADRES', 'UPDATFLG', 'BIT 7 FLAG 1', kind='data', line=144)
# Page 739
W('15,2004', 0o05560, '', 'TC', 'DOWNFLAG', line=146)
W('15,2005', 0o00031, '', 'ADRES', 'TRACKFLG', 'BIT 5 FLAG 1', kind='data', line=147)
W('15,2006', 0o04662, '', 'TC', 'BANKCALL', line=148)
W('15,2007', 0o17653, '', 'CADR', 'R02BOTH', 'IMU STATUS CHECK', kind='data', line=149)
W('15,2010', 0o35014, '', 'CAF', 'BIT4', line=150)
W('15,2011', 0o70076, '', 'MASK', 'STATE +2', 'IS PFRATFLG SET?', line=151)
W('15,2012', 0o10000, '', 'CCS', 'A', line=152)
W('15,2013', 0o02016, '', 'TC', 'P52A', 'YES', line=153)
W('15,2014', 0o35016, '', 'CAF', 'BIT2', 'NO', line=154)
W('15,2015', 0o02017, '', 'TC', 'P52A +1', line=155)
W('15,2016', 0o35017, 'P52A', 'CAF', 'BIT1', line=156)
W('15,2017', 0o55132, '', 'TS', 'OPTION2', line=157)
W('15,2020', 0o35017, 'P52B', 'CAF', 'BIT1', line=158)
W('15,2021', 0o04662, '', 'TC', 'BANKCALL', 'FLASH OPTION CODE AND ORIENTATION CODE', line=159)
W('15,2022', 0o21135, '', 'CADR', 'GOPERF4R', kind='data', line=160)
W('15,2023', 0o04106, '', 'TC', 'GOTOPOOH', line=161)
W('15,2024', 0o02031, '', 'TC', '+5', line=162)
W('15,2025', 0o02020, '', 'TC', 'P52B', 'NEW CODE -- NEW ORIENTATION CODE INPUT', line=163)
W('15,2026', 0o05412, '', 'TC', 'PHASCHNG', line=164)
W('15,2027', 0o00014, '', 'OCT', '00014', kind='data', line=165)
W('15,2030', 0o05217, '', 'TC', 'ENDOFJOB', line=166)
W('15,2031', 0o31132, '', 'CA', 'OPTION2', line=167)
W('15,2032', 0o76214, '', 'MASK', 'THREE', line=168)
W('15,2033', 0o50000, '', 'INDEX', 'A', line=169)
W('15,2034', 0o02035, '', 'TC', '+1', line=170)
W('15,2035', 0o02041, '', 'TC', 'P52T', 'L.S.', line=171)
W('15,2036', 0o02110, '', 'TC', 'P52J', 'PREF', line=172)
W('15,2037', 0o02041, '', 'TC', 'P52T', 'NORM', line=173)
W('15,2040', 0o12120, '', 'TCF', 'P52C', 'REF', line=174)
W('15,2041', 0o00006, 'P52T', 'EXTEND', line=175)
W('15,2042', 0o35021, '', 'DCA', 'NEG0', line=176)
W('15,2043', 0o53046, '', 'DXCH', 'DSPTEM1', line=177)
W('15,2044', 0o32157, '', 'CAF', 'V06N34', line=178)
W('15,2045', 0o04662, '', 'TC', 'BANKCALL', line=179)
W('15,2046', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=180)
W('15,2047', 0o04106, '', 'TC', 'GOTOPOOH', line=181)
W('15,2050', 0o02052, '', 'TC', '+2', line=182)
W('15,2051', 0o02044, '', 'TC', '-5', line=183)
W('15,2052', 0o00006, '', 'EXTEND', line=184)
W('15,2053', 0o31046, '', 'DCA', 'DSPTEM1', line=185)
W('15,2054', 0o00006, '', 'EXTEND', line=186)
W('15,2055', 0o12057, '', 'BZF', '+2', line=187)
W('15,2056', 0o12062, '', 'TCF', '+4', line=188)

W('15,2057', 0o00006, '', 'EXTEND', line=190)
W('15,2060', 0o30025, '', 'DCA', 'TIME2', line=191)
W('15,2061', 0o53046, '', 'DXCH', 'DSPTEM1', line=192)
W('15,2062', 0o31132, '', 'CA', 'OPTION2', line=193)
W('15,2063', 0o75016, '', 'MASK', 'BIT2', line=194)
W('15,2064', 0o10000, '', 'CCS', 'A', line=195)
# Page 740
W('15,2065', 0o12073, '', 'TCF', '+6', 'NOM', line=197)
W('15,2066', 0o06006, '', 'TC', 'INTPRET', 'LS', line=198)
W('15,2067', 0o77624, '', 'CALL', kind='interp', line=199)
W('15,2070', 0o34531, '', '', 'P52LS', kind='operand', line=200)
W('15,2071', 0o77650, '', 'GOTO', kind='interp', line=201)
W('15,2072', 0o32100, '', '', 'P52D', kind='operand', line=202)
W('15,2073', 0o06006, '', 'TC', 'INTPRET', line=203)
W('15,2074', 0o77745, '', 'DLOAD', kind='interp', line=204)
W('15,2075', 0o01046, '', '', 'DSPTEM1', kind='operand', line=205)
W('15,2076', 0o77624, '', 'CALL', '', 'COMPUTE NOMINAL IMU', kind='interp', line=206)
W('15,2077', 0o34661, '', '', 'S52.3', '      ORIENTATION', kind='operand', line=207)
W('15,2100', 0o77624, 'P52D', 'CALL', '', 'READ VEHICLE ATTITUDE AND', kind='interp', line=208)
W('15,2101', 0o22331, '', '', 'S52.2', '      COMPUTE GIMBAL ANGLES', kind='operand', line=209)
W('15,2102', 0o77776, '', 'EXIT', kind='interp', line=210)
W('15,2103', 0o32160, '', 'CAF', 'VB06N22', line=211)
W('15,2104', 0o04662, '', 'TC', 'BANKCALL', 'DISPLAY GIMBAL ANGLES', line=212)
W('15,2105', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=213)
W('15,2106', 0o04106, '', 'TC', 'GOTOPOOH', line=214)
W('15,2107', 0o02161, '', 'TC', 'COARSTYP', line=215)
W('15,2110', 0o06006, 'P52J', 'TC', 'INTPRET', 'RECYCLE: VEHICLE HAS BEEN MANEUVERED', line=216)
W('15,2111', 0o77650, '', 'GOTO', kind='interp', line=217)
W('15,2112', 0o32100, '', '', 'P52D', kind='operand', line=218)
W('15,2113', 0o06006, '', 'TC', 'INTPRET', line=219)
W('15,2114', 0o77624, '', 'CALL', '', 'DO COARSE ALIGN', kind='interp', line=220)
W('15,2115', 0o30770, '', '', 'CAL53A', '      ROUTINE', kind='operand', line=221)
W('15,2116', 0o77414, 'CAL53RET', 'SET', 'EXIT', kind='interp', line=222)
W('15,2117', 0o01462, '', '', 'REFSMFLG', kind='operand', line=223)
W('15,2120', 0o05412, 'P52C', 'TC', 'PHASCHNG', line=224)
W('15,2121', 0o04024, '', 'OCT', '04024', kind='data', line=225)
W('15,2122', 0o35025, '', 'CAF', 'ALRM15', line=226)
W('15,2123', 0o04662, '', 'TC', 'BANKCALL', line=227)
W('15,2124', 0o21045, '', 'CADR', 'GOPERF1', kind='data', line=228)
W('15,2125', 0o04106, '', 'TC', 'GOTOPOOH', line=229)
W('15,2126', 0o02130, '', 'TC', '+2', 'V33', line=230)
W('15,2127', 0o02142, '', 'TC', 'P52F', 'E', line=231)
W('15,2130', 0o06006, '', 'TC', 'INTPRET', line=232)
W('15,2131', 0o43234, '', 'RTB', 'DAD', kind='interp', line=233)
W('15,2132', 0o45510, '', '', 'LOADTIME', kind='operand', line=234)
W('15,2133', 0o32264, '', '', 'TSIGHT1', kind='operand', line=235)
W('15,2134', 0o77624, '', 'CALL', kind='interp', line=236)
W('15,2135', 0o30225, '', '', 'LOCSAM', kind='operand', line=237)
W('15,2136', 0o77776, '', 'EXIT', kind='interp', line=238)
W('15,2137', 0o04662, 'P52E', 'TC', 'BANKCALL', 'DO STAR SELECTION', line=239)
W('15,2140', 0o30333, '', 'CADR', 'PICAPAR', kind='data', line=240)
W('15,2141', 0o02147, '', 'TC', 'P52I', '2 STARS NOT AVAILABLE', line=241)
W('15,2142', 0o06006, 'P52F', 'TC', 'INTPRET', '2 STARS AVAILABLE', line=242)
W('15,2143', 0o77624, '', 'CALL', kind='interp', line=243)
W('15,2144', 0o30532, '', '', 'R51', kind='operand', line=244)
W('15,2145', 0o77776, 'ENDP50S', 'EXIT', kind='interp', line=245)
W('15,2146', 0o04106, '', 'TC', 'GOTOPOOH', line=246)
# Page 741
W('15,2147', 0o05650, 'P52I', 'TC', 'ALARM', line=248)
W('15,2150', 0o00405, '', 'OCT', '405', kind='data', line=249)
W('15,2151', 0o35050, '', 'CAF', 'V05N09', line=250)
W('15,2152', 0o04662, '', 'TC', 'BANKCALL', line=251)
W('15,2153', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=252)
W('15,2154', 0o04106, '', 'TC', 'GOTOPOOH', line=253)
W('15,2155', 0o02142, '', 'TC', 'P52F', 'PROCEED:  DO FINE ALIGN-R51', line=254)
W('15,2156', 0o02120, '', 'TC', 'P52C', 'RECYCLE:  VEHICLE HAS BEEN MANEUVERED', line=255)
W('15,2157', 0o01442, 'V06N34', 'VN', '0634', kind='data', line=256)
W('15,2160', 0o01426, 'VB06N22', 'VN', '00622', kind='data', line=257)
W('15,2161', 0o35024, 'COARSTYP', 'CAF', 'OCT13', line=258)
W('15,2162', 0o04662, '', 'TC', 'BANKCALL', line=259)
W('15,2163', 0o21045, '', 'CADR', 'GOPERF1', kind='data', line=260)
W('15,2164', 0o14106, '', 'TCF', 'GOTOPOOH', 'V34', line=261)
W('15,2165', 0o12113, '', 'TCF', 'P52J +3', '      NORMAL', line=262)
W('15,2166', 0o06006, '', 'TC', 'INTPRET', 'GYRO COARSE', line=263)
W('15,2167', 0o64375, 'GYCRS', 'VLOAD', 'MXV', kind='interp', line=264)
W('15,2170', 0o00307, '', '', 'XSMD', kind='operand', line=265)
W('15,2171', 0o01736, '', '', 'REFSMMAT', kind='operand', line=266)
W('15,2172', 0o77656, '', 'UNIT', kind='interp', line=267)
W('15,2173', 0o26714, '', 'STOVL', 'XDC', kind='interp', line=268)
W('15,2174', 0o00315, '', '', 'YSMD', kind='operand', line=269)
W('15,2175', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=270)
W('15,2176', 0o01736, '', '', 'REFSMMAT', kind='operand', line=271)
W('15,2177', 0o26722, '', 'STOVL', 'YDC', kind='interp', line=272)
W('15,2200', 0o00323, '', '', 'ZSMD', kind='operand', line=273)
W('15,2201', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=274)
W('15,2202', 0o01736, '', '', 'REFSMMAT', kind='operand', line=275)
W('15,2203', 0o36730, '', 'STCALL', 'ZDC', kind='interp', line=276)
W('15,2204', 0o47205, '', '', 'CALCGTA', kind='operand', line=277)
W('15,2205', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=278)
W('15,2206', 0o01260, '', '', 'DRIFTFLG', kind='operand', line=279)
W('15,2207', 0o01662, '', '', 'REFSMFLG', kind='operand', line=280)
W('15,2210', 0o77776, '', 'EXIT', kind='interp', line=281)
W('15,2211', 0o32244, '', 'CAF', 'V16N20', line=282)
W('15,2212', 0o04662, '', 'TC', 'BANKCALL', line=283)
W('15,2213', 0o20676, '', 'CADR', 'GODSPR', kind='data', line=284)
W('15,2214', 0o32323, '', 'CA', 'R55CDR', line=285)
W('15,2215', 0o04662, '', 'TC', 'BANKCALL', line=286)
W('15,2216', 0o17206, '', 'CADR', 'IMUPULSE', kind='data', line=287)
W('15,2217', 0o04662, '', 'TC', 'BANKCALL', line=288)
W('15,2220', 0o17577, '', 'CADR', 'IMUSTALL', kind='data', line=289)
W('15,2221', 0o05757, '', 'TC', 'CURTAINS', line=290)
W('15,2222', 0o05412, '', 'TC', 'PHASCHNG', line=291)
W('15,2223', 0o04024, '', 'OCT', '04024', kind='data', line=292)
W('15,2224', 0o06006, '', 'TC', 'INTPRET', line=293)
W('15,2225', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=294)
W('15,2226', 0o00306, '', '', 'XSMD', kind='operand', line=295)
W('15,2227', 0o01735, '', '', 'REFSMMAT', kind='operand', line=296)
W('15,2230', 0o77624, '', 'CALL', kind='interp', line=297)
# Page 742
W('15,2231', 0o31053, '', '', 'MATMOVE', kind='operand', line=299)
W('15,2232', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=300)
W('15,2233', 0o01273, '', '', 'PFRATFLG', kind='operand', line=301)
W('15,2234', 0o01462, '', '', 'REFSMFLG', kind='operand', line=302)
W('15,2235', 0o77234, '', 'RTB', 'VLOAD', kind='interp', line=303)
W('15,2236', 0o31275, '', '', 'SET1/PDT', kind='operand', line=304)
W('15,2237', 0o11566, '', '', 'ZEROVEC', kind='operand', line=305)
W('15,2240', 0o01472, '', 'STORE', 'GCOMP', kind='interp', line=306)
W('15,2241', 0o52014, '', 'SET', 'GOTO', kind='interp', line=307)
W('15,2242', 0o01060, '', '', 'DRIFTFLG', kind='operand', line=308)
W('15,2243', 0o30655, '', '', 'R51K', kind='operand', line=309)
W('15,2244', 0o04024, 'V16N20', 'VN', '1620', kind='data', line=310)
S('ALRM15', 'equals', 0o5025, line=311)
#   SETLOC P50S2
#   BANK
W('16,2530', 0o01531, 'V06N89*', 'VN', '0689', kind='data', line=314)

# NAME -- P52LS
#
# FUNCTION -- TO DISPLAY THE LANDING SITE LATITUDE,
# LONGITUDE AND ALTITUDE.  TO ACCEPT NEW DATA VIA
# THE KEYBOARD.  TO COMPUTE THE LANDING SITE
# ORIENTATION FOR P52 OR P54
#
# LET:
# RLS  = LANDING SITE VECTOR IN REF COORDINATES
# R    = CSM POSITION VECTOR IN REF COORDINATES
# V    = CSM VELOCITY VECTOR IN REF COORDINATES
# THEN THE LANDING SITE ORIENTATION IS:
# XSMD = UNIT(RLS)
# YSMD = UNIT(ZSMD*XSMD)
# ZSMD = UNIT((R*V)*RLS)
#
# CALL:         CALL
# P52LS
#
# INPUTS:       DSPTEM1 = TIME OF ALIGNMENT
# RLS = LANDING SITE VECTOR IN MOON FIXED COORDINATES
#
# OUTPUTS:      XSMD, YSMD, ZSMD
#
# SUBROUTINES:  RP-TO-R, LAT-LONG, LLASRD, LLASRDA, CSMPREC
#
# DEBRIS:       VAC, SEE SUBROUTINES

W('16,2531', 0o43020, 'P52LS', 'STQ', 'SET', kind='interp', line=344)
W('16,2532', 0o00300, '', '', 'QMAJ', kind='operand', line=345)
W('16,2533', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=346)
W('16,2534', 0o77745, '', 'DLOAD', kind='interp', line=347)
W('16,2535', 0o01046, '', '', 'DSPTEM1', kind='operand', line=348)
W('16,2536', 0o02607, '', 'STORE', 'TSIGHT', kind='interp', line=349)
W('16,2537', 0o43175, '', 'VLOAD', 'SET', kind='interp', line=350)
W('16,2540', 0o02026, '', '', 'RLS', kind='operand', line=351)
W('16,2541', 0o00462, '', '', 'ERADFLAG', kind='operand', line=352)
W('16,2542', 0o14001, '', 'STODL', '0D', kind='interp', line=353)
W('16,2543', 0o02607, '', '', 'TSIGHT', kind='operand', line=354)
W('16,2544', 0o34007, '', 'STCALL', '6D', kind='interp', line=355)
# Page 743
W('16,2545', 0o55344, '', '', 'RP-TO-R', kind='operand', line=357)
W('16,2546', 0o77742, '', 'VSR2', kind='interp', line=358)
W('16,2547', 0o16152, '', 'STODL', 'ALPHAV', kind='interp', line=359)
W('16,2550', 0o02607, '', '', 'TSIGHT', kind='operand', line=360)
W('16,2551', 0o77624, '', 'CALL', kind='interp', line=361)
W('16,2552', 0o26370, '', '', 'LAT-LONG', kind='operand', line=362)
W('16,2553', 0o77624, '', 'CALL', kind='interp', line=363)
W('16,2554', 0o62365, '', '', 'LLASRD', kind='operand', line=364)
W('16,2555', 0o77776, '', 'EXIT', kind='interp', line=365)
W('16,2556', 0o32530, 'LSDISP', 'CAF', 'V06N89*', line=366)
W('16,2557', 0o04662, '', 'TC', 'BANKCALL', line=367)
W('16,2560', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=368)
W('16,2561', 0o04106, '', 'TC', 'GOTOPOOH', line=369)
W('16,2562', 0o02564, '', 'TC', '+2', line=370)
W('16,2563', 0o02556, '', 'TC', 'LSDISP', line=371)
W('16,2564', 0o06006, '', 'TC', 'INTPRET', line=372)
W('16,2565', 0o77624, '', 'CALL', kind='interp', line=373)
W('16,2566', 0o62374, '', '', 'LLASRDA', kind='operand', line=374)
W('16,2567', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=375)
W('16,2570', 0o02607, '', '', 'TSIGHT', kind='operand', line=376)
W('16,2571', 0o26441, '', '', 'LALOTORV', kind='operand', line=377)
W('16,2572', 0o53575, '', 'VLOAD', 'UNIT', kind='interp', line=378)
W('16,2573', 0o02152, '', '', 'ALPHAV', kind='operand', line=379)
W('16,2574', 0o14307, '', 'STODL', 'XSMD', kind='interp', line=380)
W('16,2575', 0o02607, '', '', 'TSIGHT', kind='operand', line=381)
W('16,2576', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=382)
W('16,2577', 0o27071, '', '', 'CSMPREC', kind='operand', line=383)
W('16,2600', 0o47375, '', 'VLOAD', 'VXV', kind='interp', line=384)
W('16,2601', 0o00001, '', '', 'RATT', kind='operand', line=385)
W('16,2602', 0o00007, '', '', 'VATT', kind='operand', line=386)
W('16,2603', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=387)
W('16,2604', 0o00307, '', '', 'XSMD', kind='operand', line=388)
W('16,2605', 0o00323, '', 'STORE', 'ZSMD', kind='interp', line=389)
W('16,2606', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=390)
W('16,2607', 0o00307, '', '', 'XSMD', kind='operand', line=391)
W('16,2610', 0o34315, '', 'STCALL', 'YSMD', kind='interp', line=392)
W('16,2611', 0o00300, '', '', 'QMAJ', kind='operand', line=393)
#   SETLOC P50S1
#   BANK

# NAME:         AUTOMATIC OPTICS POSITIONING ROUTINE
#
# FUNCTION:     (1) TO POINT THE STAR LOS OF THE OPTICS AT A STAR OR LANDMARK DEFINED BY THE PROGRAM OR BY DSKY INPUT.
# (2) TO POINT THE STAR LOS OF THE OPTICS AT THE LEM DURING RENDEZVOUS TRACKING OPERATIONS.
#
# CALLING:      CALL R52
#
# INPUT:        1.  TARG1FLG AND TARG2FLG:  PRESET BY CALLER
# 2.  RNDVZFLG AND TRACKFLG:  PRESET BY CALLER
# 3.  STAR CODE:  PRESET BY CALLER.  ALSO INPUT THROUGH DSKY
# 4.  LAT, LONG, AND ALT OF LANDMARK:  INPUT THROUGH DSKY
# Page 744
# 5.  NO. OF MARKS (MARKINDX):  PRESET BY CALLER
#
# OUTPUT:       DRIVE SHAFT AND TRUNNION CDUS.
#
# SUBROUTINES:  1.  FIXDELAY            7.  CLEANDSP
# 2.  GOPERF1             8.  GODSPR
# 3.  GOFLASH             9.  REFLASHR
# 4.  R53                 10. R52.2
# 5.  ALARM               11. R52.3
# 6.  SR52.1

#   COUNT 15/R52

W('14,2011', 0o43020, 'R52', 'STQ', 'CLEAR', kind='interp', line=422)
W('14,2012', 0o02576, '', '', 'SAVQR52', kind='operand', line=423)
W('14,2013', 0o04265, '', '', 'ADVTRK', kind='operand', line=424)
W('14,2014', 0o77776, 'R52VRB', 'EXIT', kind='interp', line=425)
W('14,2015', 0o00006, '', 'EXTEND', line=426)
W('14,2016', 0o30036, '', 'DCA', 'CDUT', line=427)
W('14,2017', 0o53161, '', 'DXCH', 'DESOPTT', line=428)
W('14,2020', 0o06006, '', 'TC', 'INTPRET', line=429)
W('14,2021', 0o43131, '', 'SSP', 'CLEAR', kind='interp', line=430)
W('14,2022', 0o01304, '', '', 'OPTIND', kind='operand', line=431)
W('14,2023', 0o00000, '', '', '0', kind='operand', line=432)
W('14,2024', 0o00271, '', '', 'R53FLAG', kind='operand', line=433)
W('14,2025', 0o77776, '', 'EXIT', kind='interp', line=434)
W('14,2026', 0o06006, 'R52A', 'TC', 'INTPRET', line=435)
W('14,2027', 0o43014, '', 'SET', 'BON', kind='interp', line=436)
W('14,2030', 0o00073, '', '', 'TRUNFLAG', kind='operand', line=437)
W('14,2031', 0o00705, '', '', 'TARG1FLG', kind='operand', line=438)
W('14,2032', 0o30112, '', '', 'R52H', kind='operand', line=439)
W('14,2033', 0o77414, '', 'CLEAR', 'EXIT', kind='interp', line=440)
W('14,2034', 0o03660, '', '', 'TERMIFLG', kind='operand', line=441)
W('14,2035', 0o31314, 'R52C', 'CA', 'SWSAMPLE', 'IS OPTICS MODE IN AGC', line=442)
W('14,2036', 0o00006, '', 'EXTEND', line=443)
W('14,2037', 0o62140, '', 'BZMF', 'R52M', 'MANUAL', line=444)
W('14,2040', 0o04662, 'R52D', 'TC', 'BANKCALL', 'AGC', line=445)
W('14,2041', 0o26244, '', 'CADR', 'SR52.1', kind='data', line=446)
W('14,2042', 0o12170, '', 'TCF', 'R52L', 'GR 90 DEGREES', line=447)
W('14,2043', 0o12133, '', 'TCF', 'R52J', 'GR 50 DEGREES', line=448)
W('14,2044', 0o05546, '', 'TC', 'UPFLAG', 'LS 50 DEGREES', line=449)
W('14,2045', 0o00013, '', 'ADRES', 'TRUNFLAG', 'SET TRUNFLAG BIT 4 FLAG 0', kind='data', line=450)
W('14,2046', 0o35006, 'R52JA', 'CAF', 'BIT10', 'IS THIS A LEM', line=451)
W('14,2047', 0o70075, '', 'MASK', 'STATE +1', line=452)
W('14,2050', 0o10000, '', 'CCS', 'A', line=453)
W('14,2051', 0o02061, '', 'TC', 'R52E', 'YES', line=454)
W('14,2052', 0o35012, '', 'CAF', 'BIT6', 'NO, IS R53FLAG SET', line=455)
W('14,2053', 0o70074, '', 'MASK', 'STATE', line=456)
W('14,2054', 0o10000, '', 'CCS', 'A', line=457)
W('14,2055', 0o12061, '', 'TCF', 'R52E', 'YES', line=458)
# Page 745
W('14,2056', 0o32160, '', 'CAF', 'V06N92', 'NO', line=460)
W('14,2057', 0o04662, '', 'TC', 'BANKCALL', line=461)
W('14,2060', 0o20676, '', 'CADR', 'GODSPR', kind='data', line=462)
W('14,2061', 0o31314, 'R52E', 'CA', 'SWSAMPLE', 'IS OSS IN CMC MODE', line=463)
W('14,2062', 0o00006, '', 'EXTEND', line=464)
W('14,2063', 0o62074, '', 'BZMF', 'R52F', 'NO', line=465)
W('14,2064', 0o40074, '', 'CS', 'STATE', 'YES: IS TRUNFLAG SET', line=466)
W('14,2065', 0o75014, '', 'MASK', 'BIT4', line=467)
W('14,2066', 0o10000, '', 'CCS', 'A', line=468)
W('14,2067', 0o02072, '', 'TC', '+3', 'NO', line=469)
W('14,2070', 0o31775, '', 'CA', 'PAC', 'YES', line=470)
W('14,2071', 0o55160, '', 'TS', 'DESOPTT', line=471)
W('14,2072', 0o31773, '', 'CA', 'SAC', line=472)
W('14,2073', 0o55161, '', 'TS', 'DESOPTS', line=473)
W('14,2074', 0o35036, 'R52F', 'CAF', '.5SEC', 'WAIT 1/2 SEC', line=474)
W('14,2075', 0o04662, '', 'TC', 'BANKCALL', line=475)
W('14,2076', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=476)
W('14,2077', 0o35006, '', 'CAF', 'BIT10', line=477)
W('14,2100', 0o70075, '', 'MASK', 'STATE +1', line=478)
W('14,2101', 0o10000, '', 'CCS', 'A', line=479)
W('14,2102', 0o12113, '', 'TCF', 'R52HA', 'YES, LEM', line=480)
W('14,2103', 0o35001, '', 'CAF', 'BIT15', 'NO', line=481)
W('14,2104', 0o70103, '', 'MASK', 'STATE +7', 'IS TERMIFLG SET', line=482)
W('14,2105', 0o00006, '', 'EXTEND', line=483)
W('14,2106', 0o12035, '', 'BZF', 'R52C', 'NO', line=484)
W('14,2107', 0o06006, 'R52Q', 'TC', 'INTPRET', 'YES', line=485)
W('14,2110', 0o77650, '', 'GOTO', kind='interp', line=486)
W('14,2111', 0o02576, '', '', 'SAVQR52', kind='operand', line=487)
W('14,2112', 0o77776, 'R52H', 'EXIT', '', 'LEM', kind='interp', line=488)
W('14,2113', 0o04662, 'R52HA', 'TC', 'BANKCALL', line=489)
W('14,2114', 0o76557, '', 'CADR', 'R61CSM', kind='data', line=490)
W('14,2115', 0o30075, '', 'CA', 'STATE +1', line=491)
W('14,2116', 0o75013, '', 'MASK', 'BIT5', line=492)
W('14,2117', 0o00006, '', 'EXTEND', '', 'TRACKFLG', line=493)
W('14,2120', 0o12107, '', 'BZF', 'R52Q', line=494)

W('14,2121', 0o40075, '', 'CS', 'STATE +1', line=496)
W('14,2122', 0o75011, '', 'MASK', 'BIT7', 'UPDATFLG', line=497)
W('14,2123', 0o10000, '', 'CCS', 'A', line=498)
W('14,2124', 0o12131, '', 'TCF', 'R52SYNC', line=499)

W('14,2125', 0o30101, 'R52I', 'CA', 'STATE +5', line=501)
W('14,2126', 0o75006, '', 'MASK', 'BIT10', line=502)
W('14,2127', 0o10000, '', 'CCS', 'A', line=503)
W('14,2130', 0o02040, '', 'TC', 'R52D', 'PRFTRKAT = 1', line=504)
W('14,2131', 0o32204, 'R52SYNC', 'CAF', '1.8SEC', 'MAKE UP FOR LOST TIME', line=505)
W('14,2132', 0o12075, '', 'TCF', 'R52F +1', line=506)

W('14,2133', 0o05560, 'R52J', 'TC', 'DOWNFLAG', 'CLEAR TRUNFLAG', line=508)
W('14,2134', 0o00013, '', 'ADRES', 'TRUNFLAG', 'BIT 4 FLAG 0', kind='data', line=509)
# Page 746
W('14,2135', 0o05650, '', 'TC', 'ALARM', 'SET 407 ALARM', line=511)
W('14,2136', 0o00407, '', 'OCT', '407', kind='data', line=512)
W('14,2137', 0o02046, '', 'TC', 'R52JA', line=513)
W('14,2140', 0o35012, 'R52M', 'CAF', 'BIT6', 'IS R53FLAG SET', line=514)
W('14,2141', 0o70074, '', 'MASK', 'STATE', line=515)
W('14,2142', 0o10000, '', 'CCS', 'A', line=516)
W('14,2143', 0o02074, '', 'TC', 'R52F', 'YES', line=517)
W('14,2144', 0o00004, '', 'INHINT', '', 'NO', line=518)
W('14,2145', 0o37661, '', 'CAF', 'PRIO24', line=519)
W('14,2146', 0o05147, '', 'TC', 'FINDVAC', line=520)
#   EBANK= SAC
W('14,2147', 0o02153, '', '2CADR', 'R53JOB', kind='data', line=522)
W('14,2150', 0o30065, kind='data', line=522)

W('14,2151', 0o00003, '', 'RELINT', line=524)
W('14,2152', 0o12074, '', 'TCF', 'R52F', line=525)
W('14,2153', 0o06006, 'R53JOB', 'TC', 'INTPRET', line=526)
W('14,2154', 0o77624, '', 'CALL', kind='interp', line=527)
W('14,2155', 0o31300, '', '', 'R53', kind='operand', line=528)
W('14,2156', 0o77776, 'ENDPLAC', 'EXIT', '', 'INTERPRETER RETURN TO ENDOFJOB (R22 USES)', kind='interp', line=529)
W('14,2157', 0o05217, '', 'TC', 'ENDOFJOB', line=530)
W('14,2160', 0o01534, 'V06N92', 'VN', '00692', kind='data', line=531)
W('14,2161', 0o01531, 'V06N89A', 'VN', '0689', kind='data', line=532)
W('14,2162', 0o10464, 'SHAXIS', '2DEC', '.5376381241 B-1', kind='data', line=533)
W('14,2163', 0o12470, kind='data', line=533)

W('14,2164', 0o00000, '', '2DEC', '0', kind='data', line=535)
W('14,2165', 0o00000, kind='data', line=535)

W('14,2166', 0o15373, '', '2DEC', '.8431766920 B-1', kind='data', line=537)
W('14,2167', 0o11554, kind='data', line=537)

W('14,2170', 0o35006, 'R52L', 'CAF', 'BIT10', 'IS THIS A LEM', line=539)
W('14,2171', 0o70075, '', 'MASK', 'STATE +1', line=540)
W('14,2172', 0o10000, '', 'CCS', 'A', line=541)
W('14,2173', 0o02133, '', 'TC', 'R52J', 'YES', line=542)
W('14,2174', 0o32203, '', 'CAF', 'OCT404', line=543)
W('14,2175', 0o04662, '', 'TC', 'BANKCALL', line=544)
W('14,2176', 0o21766, '', 'CADR', 'PRIOLARM', kind='data', line=545)
W('14,2177', 0o12205, '', 'TCF', 'TERM52', 'TERMINATE', line=546)
W('14,2200', 0o12074, '', 'TCF', 'R52F', 'PROCEED', line=547)
W('14,2201', 0o12074, '', 'TCF', 'R52F', 'NO PROVISION FOR NEW DATA', line=548)
W('14,2202', 0o15217, '', 'TCF', 'ENDOFJOB', line=549)

W('14,2203', 0o00404, 'OCT404', 'OCT', '404', kind='data', line=551)
W('14,2204', 0o00264, '1.8SEC', 'DEC', '180', kind='data', line=552)

W('14,2205', 0o05536, 'TERM52', 'TC', 'CLEARMRK', line=554)

W('14,2206', 0o04662, '', 'TC', 'BANKCALL', 'KILL MARK SYSTEM', line=556)
W('14,2207', 0o16063, '', 'CADR', 'MKRELEAS', kind='data', line=557)

# Page 747

W('14,2210', 0o35021, '', 'CAF', 'ZERO', line=561)
W('14,2211', 0o55323, '', 'TS', 'OPTCADR', line=562)

W('14,2212', 0o04662, '', 'TC', 'BANKCALL', 'CLEAR OUT EXTENDED VERBS', line=564)
W('14,2213', 0o20560, '', 'CADR', 'KLEENEX', kind='data', line=565)

W('14,2214', 0o04106, '', 'TC', 'GOTOPOOH', 'NO GO TO P00', line=567)

W('14,2215', 0o43020, 'ADVORB', 'STQ', 'SET', 'SETS UP ADVANCED ORBIT TRACKING', kind='interp', line=569)
W('14,2216', 0o02576, '', '', 'SAVQR52', kind='operand', line=570)
W('14,2217', 0o04065, '', '', 'ADVTRK', kind='operand', line=571)
W('14,2220', 0o43014, '', 'SET', 'SET', kind='interp', line=572)
W('14,2221', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=573)
W('14,2222', 0o00462, '', '', 'ERADFLAG', kind='operand', line=574)
W('14,2223', 0o77650, '', 'GOTO', kind='interp', line=575)
W('14,2224', 0o30014, '', '', 'R52VRB', kind='operand', line=576)

# Page 748
# NAME -- S50 ALIAS LOCSAM
# NAME: LOCSAM
#
# FUNCTION -- TO COMPUTE QUATITIGS LISTED BELOW, USED IN THE
# IMU ALIGNMENT PROGRAMS.
#
# DEFINE:
#
# RATT = POSITION VECTOR OF CM WRT PRIMARY BODY
#
# VATT = VELOCITY VECTOR OF CM WRT PRIMARY BODY
#
# RE = RADIUS OF EARTH
#
# RM = RADIUS OF MOON
#
# ECLIPOL = POLE OF ECLIPTIC SCALED BY TANGENTIAL VELOCITY OF EARTH
# WRT TO SUN OVER THE VELOCITY OF LIGHT
#
# REM = POSITION OF MOON WRT EARTH
#
# RES = POSITION OF SUN WRT EARTH
#
# C = VELOCITY OF LIGHT
#
# EARTH IS PRIMARY                        MOON IS PRIMARY
# _                                       _
# VEARTH=-1(RATT)                         VEARTH=-1(REM+RATT)
# _                                       _
# VMOON = 1(REM-RATT)                     VMOON =-1(RATT)
# _                                       _
# VSUN  = 1(RES)                          VSUN  = 1(RES-REM)
# -1
# CEARTH=COS(SIN  (RE/RATT)+5)            CEARTH=COS 5
# -1
# CMOON =COS 5                            CMOON =COS(SIN  CRM/RATT)+5)
#
# CSUN  =COS 15                           CSUN  =COS 15
#
# VEL/C = VSUN x ECLIPOL + VATT/C
#
# CALL:         DLOAD   CALL
# DESIRED TIME
# LOCSAM
#
# INPUTS:       MPAC = TIME
#
# OUTPUTS:      VEARTH, VMOON, VSUN, CEARTH, CMOON, CSUN, VEL/C
#
# SUBROUTINES:  LSPOS, CSMCONIC
#
# DEBRIS:       VAC AREA, SEE SUBROUTINES.

# Page 749
#   SETLOC P50S1
#   BANK

#   COUNT* $$/S50

S('LOCSAM', 'equals', 0o40225, line=638)
W('14,2225', 0o77620, 'S50', 'STQ', kind='interp', line=639)
W('14,2226', 0o00300, '', '', 'QMAJ', kind='operand', line=640)
W('14,2227', 0o36607, '', 'STCALL', 'TSIGHT', kind='interp', line=641)
W('14,2230', 0o54110, '', '', 'LSPOS', kind='operand', line=642)
W('14,2231', 0o26752, '', 'STOVL', 'VMOON', kind='interp', line=643)
W('14,2232', 0o00003, '', '', '2D', kind='operand', line=644)
W('14,2233', 0o16744, '', 'STODL', 'VSUN', kind='interp', line=645)
W('14,2234', 0o02607, '', '', 'TSIGHT', kind='operand', line=646)
W('14,2235', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=647)
W('14,2236', 0o27114, '', '', 'CSMCONIC', kind='operand', line=648)
W('14,2237', 0o61131, '', 'SSP', 'TIX,2', kind='interp', line=649)
W('14,2240', 0o00052, '', '', 'S2', kind='operand', line=650)
W('14,2241', 0o00000, '', '', '0', kind='operand', line=651)
W('14,2242', 0o30265, '', '', 'MOONCNTR', kind='operand', line=652)
W('14,2243', 0o52375, 'EARTCNTR', 'VLOAD', 'VSU', kind='interp', line=653)
W('14,2244', 0o02752, '', '', 'VMOON', kind='operand', line=654)
W('14,2245', 0o00001, '', '', 'RATT', kind='operand', line=655)
W('14,2246', 0o77656, '', 'UNIT', kind='interp', line=656)
W('14,2247', 0o26752, '', 'STOVL', 'VMOON', kind='interp', line=657)
W('14,2250', 0o00001, '', '', 'RATT', kind='operand', line=658)
W('14,2251', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=659)
W('14,2252', 0o16736, '', 'STODL', 'VEARTH', kind='interp', line=660)
W('14,2253', 0o32250, '', '', 'RSUBE', kind='operand', line=661)
W('14,2254', 0o77624, '', 'CALL', kind='interp', line=662)
W('14,2255', 0o30325, '', '', 'OCCOS', kind='operand', line=663)
W('14,2256', 0o14017, '', 'STODL', 'CEARTH', kind='interp', line=664)
W('14,2257', 0o32266, '', '', 'CSS5', kind='operand', line=665)
W('14,2260', 0o24023, '', 'STOVL', 'CMOON', kind='interp', line=666)
W('14,2261', 0o02744, '', '', 'VSUN', kind='operand', line=667)
W('14,2262', 0o77656, '', 'UNIT', kind='interp', line=668)
W('14,2263', 0o36744, '', 'STCALL', 'VSUN', kind='interp', line=669)
W('14,2264', 0o30312, '', '', 'ENDSAM', kind='operand', line=670)
W('14,2265', 0o40575, 'MOONCNTR', 'VLOAD', 'VSR8', kind='interp', line=671)
W('14,2266', 0o02752, '', '', 'VMOON', kind='operand', line=672)
W('14,2267', 0o51362, '', 'VSR1', 'BVSU', kind='interp', line=673)
W('14,2270', 0o02744, '', '', 'VSUN', kind='operand', line=674)
W('14,2271', 0o77656, '', 'UNIT', kind='interp', line=675)
W('14,2272', 0o26744, '', 'STOVL', 'VSUN', kind='interp', line=676)
W('14,2273', 0o02752, '', '', 'VMOON', kind='operand', line=677)
W('14,2274', 0o53455, '', 'VAD', 'UNIT', kind='interp', line=678)
W('14,2275', 0o00001, '', '', 'RATT', kind='operand', line=679)
W('14,2276', 0o77676, '', 'VCOMP', kind='interp', line=680)
W('14,2277', 0o26736, '', 'STOVL', 'VEARTH', kind='interp', line=681)
# Page 750

W('14,2300', 0o00001, '', '', 'RATT', kind='operand', line=684)
W('14,2301', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=685)
W('14,2302', 0o16752, '', 'STODL', 'VMOON', kind='interp', line=686)
W('14,2303', 0o32246, '', '', 'RSUBM', kind='operand', line=687)
W('14,2304', 0o77624, '', 'CALL', kind='interp', line=688)
W('14,2305', 0o30325, '', '', 'OCCOS', kind='operand', line=689)
W('14,2306', 0o14023, '', 'STODL', 'CMOON', kind='interp', line=690)
W('14,2307', 0o32266, '', '', 'CSS5', kind='operand', line=691)
W('14,2310', 0o24017, '', 'STOVL', 'CEARTH', kind='interp', line=692)
W('14,2311', 0o02744, '', '', 'VSUN', kind='operand', line=693)
W('14,2312', 0o77635, 'ENDSAM', 'VXV', kind='interp', line=694)
W('14,2313', 0o32256, '', '', 'ECLIPOL', kind='operand', line=695)
W('14,2314', 0o27474, '', 'STOVL', 'VEL/C', kind='interp', line=696)
W('14,2315', 0o00007, '', '', 'VATT', kind='operand', line=697)
W('14,2316', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=698)
W('14,2317', 0o32254, '', '', '1/C', kind='operand', line=699)
W('14,2320', 0o03474, '', '', 'VEL/C', kind='operand', line=700)
W('14,2321', 0o17474, '', 'STODL', 'VEL/C', kind='interp', line=701)
W('14,2322', 0o32270, '', '', 'CSSUN', kind='operand', line=702)
W('14,2323', 0o34021, '', 'STCALL', 'CSUN', kind='interp', line=703)
W('14,2324', 0o00300, '', '', 'QMAJ', kind='operand', line=704)
W('14,2325', 0o70471, 'OCCOS', 'DDV', 'SR1', kind='interp', line=705)
W('14,2326', 0o00045, '', '', '36D', kind='operand', line=706)
W('14,2327', 0o43336, '', 'ASIN', 'DAD', kind='interp', line=707)
W('14,2330', 0o32252, '', '', '5DEGREES', kind='operand', line=708)
W('14,2331', 0o70546, '', 'COS', 'SR1', kind='interp', line=709)
W('14,2332', 0o77616, '', 'RVQ', kind='interp', line=710)
#   SETLOC P50S
#   BANK
W('15,2245', 0o00065, 'RSUBM', '2DEC', '1738090 B-29', 'MOON RADIUS IN METERS', kind='data', line=713)
W('15,2246', 0o01265, kind='data', line=713)

W('15,2247', 0o00302, 'RSUBE', '2DEC', '6378166 B-29', kind='data', line=715)
W('15,2250', 0o24533, kind='data', line=715)

W('15,2251', 0o00343, '5DEGREES', '2DEC', '.013888889', 'SCALED IN REVS', kind='data', line=717)
W('15,2252', 0o21616, kind='data', line=717)

W('15,2253', 0o00000, '1/C', '2DEC', '.000042699 B-1', '*', kind='data', line=719)
W('15,2254', 0o13143, kind='data', line=719)

W('15,2255', 0o00000, 'ECLIPOL', '2DEC', '0', '*', kind='data', line=721)
W('15,2256', 0o00000, kind='data', line=721)

W('15,2257', 0o77777, '', '2DEC', '-.00007896 B-1', '*', kind='data', line=723)
W('15,2260', 0o53231, kind='data', line=723)

W('15,2261', 0o00001, '', '2DEC', '.00018209 B-1', '*             * FOR USE BY CSM ONLY', kind='data', line=725)
W('15,2262', 0o17570, kind='data', line=725)

W('15,2263', 0o00001, 'TSIGHT1', '2DEC', '24000', kind='data', line=727)
W('15,2264', 0o16700, kind='data', line=727)

S('CEARTH', 'equals', 0o16, line=729)
S('CSUN', 'equals', 0o20, line=730)
S('CMOON', 'equals', 0o22, line=731)
W('15,2265', 0o07760, 'CSS5', '2DEC', '.2490475', '(COS 5)/4', kind='data', line=732)
W('15,2266', 0o14473, kind='data', line=732)
# Page 751
W('15,2267', 0o07564, 'CSSUN', '2DEC', '.24148', '(COS 15)/4', kind='data', line=734)
W('15,2270', 0o15042, kind='data', line=734)

# Page 752
# PROGRAM NAME -- PICAPAR       DATE: DEC 20 66
# MOD 1                         LOG SECTION: P51-P53
# ASSEMBLY:  SUNDISK REV40
# BY KEN VINCENT
#
# FUNCTION
# THIS PROGRAM READS THE IMU-CDUS AND COMPUTES THE VEHICLE ORIENTATION
# WITH RESPECT TO INERTIAL SPACE.  IT THEN COMPUTES THE SHAFT AXIS (SAX)
# WITH RESPECT TO REFERENCE INERTIAL.  EACH STAR IN THE CATALOG IS TESTED
# TO DETERMINE IF IT IS OCCULTED BY EITHER EARTH, SUN OR MOON.  IF A
# STAR IS NOT OCCULTED THEN IT IS PAIRED WITH ALL STARS OF LOWER INDEX.
# THE PAIRED STAR IS TESTED FOR OCCULTATION.  PAIRS OF STARS THAT PASS
# THE OCCULTATION TESTS ARE TESTED FOR GOOD SEPARATION.  A PAIR OF STARS
# HAVE GOOD SEPARATION IF THE ANGLE BETWEEN THEM IS LESS THAN 66 DEGREES
# AND MORE THAN 40 DEGREES.  THOSE PAIRS WITH GOOD SEPARATION
# ARE THEN TESTED TO SEE IF THEY LIE IN CURRENT FIELD OF VIEW.  (WITHIN
# 33 DEGREES OF SAX).  THE PAIR WITH MAX SEPARATION IS CHOSEN FROM
# THOSE WITH GOOD SEPARATION, AND IN FIELD OF VIEW.
#
# CALLING SEQUENCE
# L       TC      BANKCALL
# L+1     CADR    PICAPAR
# L+2     ERROR RETURN -- NO STARS IN FIELD OF VIEW
# L+3     NORMAL RETURN
#
# OUTPUT
# BESTI, BESTJ -- SINGLE PREC, INTEGERS, STAR NUMBERS TIMES 6
# VFLAG -- FLAG BIT SET IMPLIES NO STARS IN FIELD OF VIEW
#
# INITIALIZATION
# 1)      A CALL TO LOCSAM MUST BE MADE
# 2)      VEARTH = -UNIT(R) WHERE R HAS BEEN UPDATED TO APPROXIMATE TIME OF
# SIGHTINGS.
#
# DEBRIS
# WORK AREA
# X,Y,ZNB
# SINCDU, COSCDU
# STARAD -- STAR +5

#   COUNT 14/PICAP

#   SETLOC P50S1
#   BANK
W('14,2333', 0o04711, 'PICAPAR', 'TC', 'MAKECADR', line=781)
W('14,2334', 0o55777, '', 'TS', 'QMIN', line=782)
W('14,2335', 0o06006, '', 'TC', 'INTPRET', line=783)
W('14,2336', 0o77624, '', 'CALL', kind='interp', line=784)
W('14,2337', 0o47477, '', '', 'CDUTRIG', kind='operand', line=785)
W('14,2340', 0o77624, '', 'CALL', kind='interp', line=786)
W('14,2341', 0o34612, '', '', 'CALCSMSC', kind='operand', line=787)
# Page 753
W('14,2342', 0o77601, '', 'SETPD', kind='interp', line=789)
W('14,2343', 0o00001, '', '', '0', kind='operand', line=790)
W('14,2344', 0o71214, '', 'SET', 'DLOAD', 'VFLAG = 1', kind='interp', line=791)
W('14,2345', 0o01465, '', '', 'VFLAG', kind='operand', line=792)
W('14,2346', 0o11566, '', '', 'DPZERO', kind='operand', line=793)
W('14,2347', 0o24303, '', 'STOVL', 'BESTI', kind='interp', line=794)
W('14,2350', 0o02714, '', '', 'XNB', kind='operand', line=795)
W('14,2351', 0o63361, '', 'VXSC', 'PDVL', kind='interp', line=796)
W('14,2352', 0o30511, '', '', 'SIN33', kind='operand', line=797)
W('14,2353', 0o02730, '', '', 'ZNB', kind='operand', line=798)
W('14,2354', 0o74370, '', 'AXT,1', 'VXSC', kind='interp', line=799)
W('14,2355', 0o00344, '', '', '228D', 'X1 = 37 X 6 + 6', kind='operand', line=800)
W('14,2356', 0o30513, '', '', 'COS33', kind='operand', line=801)
W('14,2357', 0o77655, '', 'VAD', kind='interp', line=802)
W('14,2360', 0o53505, '', 'VXM', 'UNIT', kind='interp', line=803)
W('14,2361', 0o01736, '', '', 'REFSMMAT', kind='operand', line=804)
W('14,2362', 0o02760, '', 'STORE', 'SAX', 'SAX = SHAFT AXIS', kind='interp', line=805)
W('14,2363', 0o66331, '', 'SSP', 'SSP', 'S1 = S2 = 6', kind='interp', line=806)
W('14,2364', 0o00051, '', '', 'S1', kind='operand', line=807)
W('14,2365', 0o00006, '', '', '6', kind='operand', line=808)
W('14,2366', 0o00052, '', '', 'S2', kind='operand', line=809)
W('14,2367', 0o00006, '', '', '6', kind='operand', line=810)
W('14,2370', 0o52100, 'PIC1', 'TIX,1', 'GOTO', 'MAJOR STAR', kind='interp', line=811)
W('14,2371', 0o30373, '', '', 'PIC2', kind='operand', line=812)
W('14,2372', 0o30522, '', '', 'PICEND', kind='operand', line=813)
W('14,2373', 0o45173, 'PIC2', 'VLOAD*', 'CALL', kind='interp', line=814)
W('14,2374', 0o31761, '', '', 'CATLOG,1', kind='operand', line=815)
W('14,2375', 0o30466, '', '', 'OCCULT', kind='operand', line=816)
W('14,2376', 0o73014, '', 'BON', 'LXA,2', kind='interp', line=817)
W('14,2377', 0o01710, '', '', 'CULTFLAG', kind='operand', line=818)
W('14,2400', 0o30370, '', '', 'PIC1', kind='operand', line=819)
W('14,2401', 0o00046, '', '', 'X1', kind='operand', line=820)
W('14,2402', 0o52104, 'PIC3', 'TIX,2', 'GOTO', kind='interp', line=821)
W('14,2403', 0o30405, '', '', 'PIC4', kind='operand', line=822)
W('14,2404', 0o30370, '', '', 'PIC1', kind='operand', line=823)
W('14,2405', 0o45173, 'PIC4', 'VLOAD*', 'CALL', kind='interp', line=824)
W('14,2406', 0o46016, '', '', 'CATLOG,2', kind='operand', line=825)
W('14,2407', 0o30466, '', '', 'OCCULT', kind='operand', line=826)
W('14,2410', 0o76614, '', 'BON', 'VLOAD*', kind='interp', line=827)
W('14,2411', 0o01710, '', '', 'CULTFLAG', kind='operand', line=828)
W('14,2412', 0o30402, '', '', 'PIC3', kind='operand', line=829)
W('14,2413', 0o31761, '', '', 'CATLOG,1', kind='operand', line=830)
W('14,2414', 0o45237, '', 'DOT*', 'DSU', kind='interp', line=831)
W('14,2415', 0o46016, '', '', 'CATLOG,2', kind='operand', line=832)
W('14,2416', 0o30515, '', '', 'CSS66', 'SEPARATION LESS THAN 66 DEG.', kind='operand', line=833)
W('14,2417', 0o43240, '', 'BMN', 'DAD', kind='interp', line=834)
W('14,2420', 0o30402, '', '', 'PIC3', kind='operand', line=835)
W('14,2421', 0o30517, '', '', 'CSS6640', 'SEPARATION MORE THAN 40 DEG.', kind='operand', line=836)
W('14,2422', 0o77644, '', 'BPL', kind='interp', line=837)
W('14,2423', 0o30402, '', '', 'PIC3', kind='operand', line=838)
# Page 754
W('14,2424', 0o50373, '', 'VLOAD*', 'DOT', kind='interp', line=840)
W('14,2425', 0o31761, '', '', 'CATLOG,1', kind='operand', line=841)
W('14,2426', 0o02760, '', '', 'SAX', kind='operand', line=842)
W('14,2427', 0o50025, '', 'DSU', 'BMN', 'MAJOR STAR IN CONE', kind='interp', line=843)
W('14,2430', 0o30521, '', '', 'CSS33', kind='operand', line=844)
W('14,2431', 0o30370, '', '', 'PIC1', kind='operand', line=845)
W('14,2432', 0o50373, '', 'VLOAD*', 'DOT', kind='interp', line=846)
W('14,2433', 0o46016, '', '', 'CATLOG,2', kind='operand', line=847)
W('14,2434', 0o02760, '', '', 'SAX', kind='operand', line=848)
W('14,2435', 0o51025, '', 'DSU', 'BPL', kind='interp', line=849)
W('14,2436', 0o30521, '', '', 'CSS33', kind='operand', line=850)
W('14,2437', 0o30442, '', '', 'STRATGY', kind='operand', line=851)
W('14,2440', 0o77650, '', 'GOTO', kind='interp', line=852)
W('14,2441', 0o30402, '', '', 'PIC3', kind='operand', line=853)
W('14,2442', 0o77614, 'STRATGY', 'BONCLR', kind='interp', line=854)
W('14,2443', 0o01605, '', '', 'VFLAG', kind='operand', line=855)
W('14,2444', 0o30461, '', '', 'NEWPAR', kind='operand', line=856)
W('14,2445', 0o65120, '', 'XCHX,1', 'XCHX,2', kind='interp', line=857)
W('14,2446', 0o00302, '', '', 'BESTI', kind='operand', line=858)
W('14,2447', 0o00303, '', '', 'BESTJ', kind='operand', line=859)
W('14,2450', 0o47773, 'STRAT', 'VLOAD*', 'DOT*', kind='interp', line=860)
W('14,2451', 0o31761, '', '', 'CATLOG,1', kind='operand', line=861)
W('14,2452', 0o46016, '', '', 'CATLOG,2', kind='operand', line=862)
W('14,2453', 0o43006, '', 'PUSH', 'BOFINV', kind='interp', line=863)
W('14,2454', 0o01545, '', '', 'VFLAG', kind='operand', line=864)
W('14,2455', 0o30445, '', '', 'STRAT -3', kind='operand', line=865)
W('14,2456', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=866)
W('14,2457', 0o77644, '', 'BPL', kind='interp', line=867)
W('14,2460', 0o30402, '', '', 'PIC3', kind='operand', line=868)
W('14,2461', 0o67130, 'NEWPAR', 'SXA,1', 'SXA,2', kind='interp', line=869)
W('14,2462', 0o00302, '', '', 'BESTI', kind='operand', line=870)
W('14,2463', 0o00303, '', '', 'BESTJ', kind='operand', line=871)
W('14,2464', 0o77650, '', 'GOTO', kind='interp', line=872)
W('14,2465', 0o30402, '', '', 'PIC3', kind='operand', line=873)
W('14,2466', 0o51321, 'OCCULT', 'MXV', 'BVSU', kind='interp', line=874)
W('14,2467', 0o02736, '', '', 'CULTRIX', kind='operand', line=875)
W('14,2470', 0o00017, '', '', 'CSS', kind='operand', line=876)
W('14,2471', 0o77654, '', 'BZE', kind='interp', line=877)
W('14,2472', 0o30505, '', '', 'CULTED', kind='operand', line=878)
W('14,2473', 0o75240, '', 'BMN', 'SIGN', kind='interp', line=879)
W('14,2474', 0o30505, '', '', 'CULTED', kind='operand', line=880)
W('14,2475', 0o00160, '', '', 'MPAC +3', kind='operand', line=881)
W('14,2476', 0o75240, '', 'BMN', 'SIGN', kind='interp', line=882)
W('14,2477', 0o30505, '', '', 'CULTED', kind='operand', line=883)
W('14,2500', 0o00162, '', '', 'MPAC +5', kind='operand', line=884)
W('14,2501', 0o43040, '', 'BMN', 'CLRGO', kind='interp', line=885)
W('14,2502', 0o30505, '', '', 'CULTED', kind='operand', line=886)
W('14,2503', 0o01630, '', '', 'CULTFLAG', kind='operand', line=887)
W('14,2504', 0o00052, '', '', 'QPRET', kind='operand', line=888)
W('14,2505', 0o77614, 'CULTED', 'SETGO', kind='interp', line=889)
# Page 755
W('14,2506', 0o01430, '', '', 'CULTFLAG', kind='operand', line=891)
W('14,2507', 0o00052, '', '', 'QPRET', kind='operand', line=892)
S('CSS', 'equals', 0o16, line=893)
W('14,2510', 0o21150, 'SIN33', '2DEC', '.5376381241', kind='data', line=894)
W('14,2511', 0o25157, kind='data', line=894)

W('14,2512', 0o32766, 'COS33', '2DEC', '.8431756920', kind='data', line=896)
W('14,2513', 0o22713, kind='data', line=896)

W('14,2514', 0o01736, 'CSS66', '2DEC', '.060480472', '(COS76)/4', kind='data', line=898)
W('14,2515', 0o35137, kind='data', line=898)

W('14,2516', 0o73003, 'CSS6640', '2DEC', '-.15602587', '(COS76 - COS30)/4', kind='data', line=900)
W('14,2517', 0o65403, kind='data', line=900)

W('14,2520', 0o06233, 'CSS33', '2DEC', '.197002688', '(COS(1/2(76))/4', kind='data', line=902)
W('14,2521', 0o26112, kind='data', line=902)

W('14,2522', 0o77414, 'PICEND', 'BOFF', 'EXIT', kind='interp', line=904)
W('14,2523', 0o01745, '', '', 'VFLAG', kind='operand', line=905)
W('14,2524', 0o30526, '', '', 'PICGXT', kind='operand', line=906)
W('14,2525', 0o02530, '', 'TC', 'PICBXT', line=907)
W('14,2526', 0o77776, 'PICGXT', 'EXIT', kind='interp', line=908)
W('14,2527', 0o25777, '', 'INCR', 'QMIN', line=909)
W('14,2530', 0o31777, 'PICBXT', 'CA', 'QMIN', line=910)
W('14,2531', 0o04666, '', 'TC', 'SWCALL', line=911)
# V1             =       12D

# Page 756
# NAME -- R51   FINE ALIGN
# FUNCTION -- TO ALIGN THE STABLE MEMBER TO REFSSMAT
# CALLING SEQ -- CALL R51
# INPUT -- BESTI, BESTJ (PAIR OF STAR NO)
# OUTPUT -- GYRO TORQUE PULSES
# SUBROUTINES -- R52, R54, R55 (SXTNB, NBSM, AXISGEN)

#   COUNT 14/R51

W('14,2532', 0o77776, 'R51', 'EXIT', kind='interp', line=924)
W('14,2533', 0o35017, '', 'CAF', 'BIT1', line=925)
W('14,2534', 0o54304, '', 'TS', 'STARIND', line=926)
W('14,2535', 0o54301, '', 'TS', 'MARKINDX', line=927)
W('14,2536', 0o06006, 'R51.2', 'TC', 'INTPRET', line=928)
W('14,2537', 0o43014, 'R51.3', 'CLEAR', 'CLEAR', kind='interp', line=929)
W('14,2540', 0o00666, '', '', 'TARG2FLG', kind='operand', line=930)
W('14,2541', 0o00665, '', '', 'TARG1FLG', kind='operand', line=931)
W('14,2542', 0o77776, '', 'EXIT', kind='interp', line=932)
W('14,2543', 0o05412, '', 'TC', 'PHASCHNG', line=933)
W('14,2544', 0o05024, '', 'OCT', '05024', 'RESTART GR 4 FOR R52-R53', kind='data', line=934)
W('14,2545', 0o13000, '', 'OCT', '13000', kind='data', line=935)
W('14,2546', 0o50304, '', 'INDEX', 'STARIND', line=936)
W('14,2547', 0o30302, '', 'CA', 'BESTI', line=937)
W('14,2550', 0o00006, '', 'EXTEND', line=938)
W('14,2551', 0o72713, '', 'MP', '1/6TH', line=939)
W('14,2552', 0o54735, '', 'TS', 'STARCODE', line=940)
W('14,2553', 0o32712, 'R51DSP', 'CAF', 'V01N70', line=941)
W('14,2554', 0o04662, '', 'TC', 'BANKCALL', line=942)
W('14,2555', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=943)
W('14,2556', 0o04106, '', 'TC', 'GOTOPOOH', line=944)
W('14,2557', 0o02564, '', 'TC', '+5', line=945)
W('14,2560', 0o02553, '', 'TC', '-5', line=946)
W('14,2561', 0o36211, '', 'CAF', 'SIX', line=947)
W('14,2562', 0o05526, '', 'TC', 'BLANKET', line=948)
W('14,2563', 0o15217, '', 'TCF', 'ENDOFJOB', line=949)
W('14,2564', 0o03366, '', 'TC', 'CHKSCODE', line=950)
W('14,2565', 0o04400, '', 'TC', 'FALTON', line=951)
W('14,2566', 0o02553, '', 'TC', 'R51DSP', line=952)
W('14,2567', 0o06006, '', 'TC', 'INTPRET', line=953)
W('14,2570', 0o45034, '', 'RTB', 'CALL', kind='interp', line=954)
W('14,2571', 0o45510, '', '', 'LOADTIME', kind='operand', line=955)
W('14,2572', 0o32340, '', '', 'PLANET', kind='operand', line=956)
W('14,2573', 0o72131, '', 'SSP', 'LXA,1', kind='interp', line=957)
W('14,2574', 0o00051, '', '', 'S1', kind='operand', line=958)
W('14,2575', 0o00000, '', '', '0', kind='operand', line=959)
W('14,2576', 0o00304, '', '', 'STARIND', kind='operand', line=960)
W('14,2577', 0o77700, '', 'TIX,1', kind='interp', line=961)
W('14,2600', 0o30603, '', '', 'R51ST', kind='operand', line=962)
W('14,2601', 0o36617, '', 'STCALL', 'STARSAV2', '2ND STAR', kind='interp', line=963)
W('14,2602', 0o30604, '', '', 'R51ST +1', kind='operand', line=964)
W('14,2603', 0o02611, 'R51ST', 'STORE', 'STARSAV1', '1ST STAR', kind='interp', line=965)
# Page 757
W('14,2604', 0o77776, '', 'EXIT', kind='interp', line=967)
W('14,2605', 0o41011, '', 'CS', 'MODREG', 'IS THIS P54', line=968)
W('14,2606', 0o62711, '', 'AD', 'OCT66', line=969)
W('14,2607', 0o00006, '', 'EXTEND', line=970)
W('14,2610', 0o12704, '', 'BZF', 'R51B', 'YES', line=971)
W('14,2611', 0o06006, '', 'TC', 'INTPRET', line=972)
W('14,2612', 0o77624, '', 'CALL', kind='interp', line=973)
W('14,2613', 0o30011, '', '', 'R52', 'AOP WILL MAKE CALLS TO SIGHTING', kind='operand', line=974)
W('14,2614', 0o77624, 'R51A', 'CALL', '', 'COMPUTE LOS IN SM FROM MARK DATA', kind='interp', line=975)
W('14,2615', 0o36022, '', '', 'SXTSM', kind='operand', line=976)
W('14,2616', 0o02617, '', 'STORE', 'STARSAV2', kind='interp', line=977)
W('14,2617', 0o77776, '', 'EXIT', kind='interp', line=978)
W('14,2620', 0o04662, '', 'TC', 'BANKCALL', line=979)
W('14,2621', 0o16063, '', 'CADR', 'MKRELEAS', kind='data', line=980)
W('14,2622', 0o06006, '', 'TC', 'INTPRET', line=981)
W('14,2623', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=982)
W('14,2624', 0o02607, '', '', 'TSIGHT', kind='operand', line=983)
W('14,2625', 0o32340, '', '', 'PLANET', kind='operand', line=984)
W('14,2626', 0o77776, '', 'EXIT', kind='interp', line=985)
W('14,2627', 0o10304, '', 'CCS', 'STARIND', line=986)
W('14,2630', 0o02671, '', 'TC', 'R51.4', line=987)
W('14,2631', 0o06006, '', 'TC', 'INTPRET', line=988)
W('14,2632', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=989)
W('14,2633', 0o01736, '', '', 'REFSMMAT', kind='operand', line=990)
W('14,2634', 0o02736, '', 'STORE', 'STARAD', kind='interp', line=991)
W('14,2635', 0o77775, '', 'VLOAD', kind='interp', line=992)
W('14,2636', 0o02617, '', '', 'STARSAV2', kind='operand', line=993)
W('14,2637', 0o24007, '', 'STOVL', '6D', kind='interp', line=994)
W('14,2640', 0o02611, '', '', 'STARSAV1', kind='operand', line=995)
W('14,2641', 0o24015, '', 'STOVL', '12D', kind='interp', line=996)
W('14,2642', 0o02601, '', '', 'PLANVEC', kind='operand', line=997)
W('14,2643', 0o36744, '', 'STCALL', 'STARAD +6', kind='interp', line=998)
W('14,2644', 0o30714, '', '', 'R54', 'STAR DATA TEST', kind='operand', line=999)
W('14,2645', 0o45014, '', 'BOFF', 'CALL', kind='interp', line=1000)
W('14,2646', 0o00354, '', '', 'FREEFLAG', kind='operand', line=1001)
W('14,2647', 0o30655, '', '', 'R51K', kind='operand', line=1002)
W('14,2650', 0o47401, '', '', 'AXISGEN', kind='operand', line=1003)
W('14,2651', 0o77624, '', 'CALL', kind='interp', line=1004)
W('14,2652', 0o32271, '', '', 'R55', 'GYRO TORQUE', kind='operand', line=1005)
W('14,2653', 0o77614, '', 'CLEAR', kind='interp', line=1006)
W('14,2654', 0o01273, '', '', 'PFRATFLG', kind='operand', line=1007)
W('14,2655', 0o77776, 'R51K', 'EXIT', kind='interp', line=1008)
W('14,2656', 0o35771, '', 'CAF', 'OCT14', line=1009)
W('14,2657', 0o04662, '', 'TC', 'BANKCALL', line=1010)
W('14,2660', 0o21045, '', 'CADR', 'GOPERF1', kind='data', line=1011)
W('14,2661', 0o04106, '', 'TC', 'GOTOPOOH', line=1012)
W('14,2662', 0o02664, '', 'TC', '+2', 'V33', line=1013)
W('14,2663', 0o02666, '', 'TC', '+3', line=1014)
W('14,2664', 0o04662, '', 'TC', 'BANKCALL', line=1015)
W('14,2665', 0o32120, '', 'CADR', 'P52C', kind='data', line=1016)
# Page 758
W('14,2666', 0o06006, '', 'TC', 'INTPRET', line=1018)
W('14,2667', 0o77650, '', 'GOTO', kind='interp', line=1019)
W('14,2670', 0o32145, '', '', 'ENDP50S', kind='operand', line=1020)
W('14,2671', 0o06006, 'R51.4', 'TC', 'INTPRET', line=1021)
W('14,2672', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=1022)
W('14,2673', 0o01736, '', '', 'REFSMMAT', kind='operand', line=1023)
W('14,2674', 0o26601, '', 'STOVL', 'PLANVEC', kind='interp', line=1024)
W('14,2675', 0o02617, '', '', 'STARSAV2', kind='operand', line=1025)
W('14,2676', 0o02611, '', 'STORE', 'STARSAV1', kind='interp', line=1026)
W('14,2677', 0o77731, '', 'SSP', kind='interp', line=1027)
W('14,2700', 0o00305, '', '', 'STARIND', kind='operand', line=1028)
W('14,2701', 0o00000, '', '', '0', kind='operand', line=1029)
W('14,2702', 0o77650, '', 'GOTO', kind='interp', line=1030)
W('14,2703', 0o30537, '', '', 'R51.3', kind='operand', line=1031)
W('14,2704', 0o06006, 'R51B', 'TC', 'INTPRET', line=1032)
W('14,2705', 0o77624, '', 'CALL', kind='interp', line=1033)
W('14,2706', 0o36056, '', '', 'R56', kind='operand', line=1034)
W('14,2707', 0o77650, '', 'GOTO', kind='interp', line=1035)
W('14,2710', 0o30614, '', '', 'R51A', kind='operand', line=1036)
W('14,2711', 0o00066, 'OCT66', 'OCT', '00066', kind='data', line=1037)
W('14,2712', 0o00306, 'V01N70', 'VN', '0170', kind='data', line=1038)
W('14,2713', 0o05253, '1/6TH', 'DEC', '.1666667', kind='data', line=1039)

# Page 759
# NAME:         R55     GYRO TORQUE
# FUNCTION -- COMPUTE AND SEND GYRO PULSES
# CALLING SEQ -- CALL R55
# INPUT -- X,Y,ZDC -- REFSMMAT WRT PRESENT STABLE MEMBER
# OUTPUT -- GYRO PULSES
# SUBROUTINES -- CALCGTA, GOFLASH, GODSPR, IMUFINE, IMUPULSE, GOPERF1

#   SETLOC P50S
#   BANK
#   COUNT* $$/R55
W('15,2271', 0o77620, 'R55', 'STQ', kind='interp', line=1052)
W('15,2272', 0o02777, '', '', 'QMIN', kind='operand', line=1053)
W('15,2273', 0o77624, '', 'CALL', kind='interp', line=1054)
W('15,2274', 0o47205, '', '', 'CALCGTA', kind='operand', line=1055)
W('15,2275', 0o77776, 'PULSEM', 'EXIT', kind='interp', line=1056)
W('15,2276', 0o32322, 'R55.1', 'CAF', 'V06N93', line=1057)
W('15,2277', 0o04662, '', 'TC', 'BANKCALL', line=1058)
W('15,2300', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=1059)
W('15,2301', 0o04106, '', 'TC', 'GOTOPOOH', line=1060)
W('15,2302', 0o02304, '', 'TC', 'R55.2', line=1061)
W('15,2303', 0o02317, '', 'TC', 'R55RET', line=1062)
W('15,2304', 0o05412, 'R55.2', 'TC', 'PHASCHNG', line=1063)
W('15,2305', 0o00314, '', 'OCT', '00314', kind='data', line=1064)
W('15,2306', 0o32323, '', 'CA', 'R55CDR', line=1065)
W('15,2307', 0o04662, '', 'TC', 'BANKCALL', line=1066)
W('15,2310', 0o17206, '', 'CADR', 'IMUPULSE', kind='data', line=1067)
W('15,2311', 0o04662, '', 'TC', 'BANKCALL', line=1068)
W('15,2312', 0o17577, '', 'CADR', 'IMUSTALL', kind='data', line=1069)
W('15,2313', 0o05757, '', 'TC', 'CURTAINS', line=1070)
W('15,2314', 0o05412, '', 'TC', 'PHASCHNG', line=1071)
W('15,2315', 0o05024, '', 'OCT', '05024', kind='data', line=1072)
W('15,2316', 0o13000, '', 'OCT', '13000', kind='data', line=1073)
W('15,2317', 0o06006, 'R55RET', 'TC', 'INTPRET', line=1074)
W('15,2320', 0o77650, '', 'GOTO', kind='interp', line=1075)
W('15,2321', 0o02777, '', '', 'QMIN', kind='operand', line=1076)
W('15,2322', 0o01535, 'V06N93', 'VN', '0693', kind='data', line=1077)
W('15,2323', 0o02757, 'R55CDR', 'ECADR', 'OGC', kind='data', line=1078)
S('R54', 'equals', 0o40714, line=1079)

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
# Page 760
# A2     =       ARCCOS(SS1 - SS2)
# A     =       ABS(2(A1 - A2))

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

#   SETLOC P50S1
#   BANK
#   COUNT* $$/R50
W('14,2714', 0o43020, 'CHKSDATA', 'STQ', 'SET', kind='interp', line=1114)
W('14,2715', 0o02777, '', '', 'QMIN', kind='operand', line=1115)
W('14,2716', 0o00074, '', '', 'FREEFLAG', kind='operand', line=1116)
W('14,2717', 0o77760, 'CHKSAB', 'AXC,1', '', 'SET X1 TO STORE EPHEMERIS DATA', kind='interp', line=1117)
W('14,2720', 0o02735, '', '', 'STARAD', kind='operand', line=1118)

W('14,2721', 0o47773, 'CHKSB', 'VLOAD*', 'DOT*', 'CAL. ANGLE THETA', kind='interp', line=1120)
W('14,2722', 0o00001, '', '', '0,1', kind='operand', line=1121)
W('14,2723', 0o00007, '', '', '6,1', kind='operand', line=1122)
W('14,2724', 0o65552, '', 'SL1', 'ACOS', kind='interp', line=1123)
W('14,2725', 0o00025, '', 'STORE', 'THETA', kind='interp', line=1124)
W('14,2726', 0o43014, '', 'BOFF', 'INVERT', 'BRANCH TO CHKSD IF THIS IS 2ND PASS', kind='interp', line=1125)
W('14,2727', 0o00354, '', '', 'FREEFLAG', kind='operand', line=1126)
W('14,2730', 0o30740, '', '', 'CHKSD', kind='operand', line=1127)
W('14,2731', 0o00174, '', '', 'FREEFLAG', 'CLEAR FREEFLAG', kind='operand', line=1128)
W('14,2732', 0o71360, '', 'AXC,1', 'DLOAD', 'SET X1 TO MARK ANGLES', kind='interp', line=1129)
W('14,2733', 0o00006, '', '', '6D', kind='operand', line=1130)
W('14,2734', 0o00025, '', '', 'THETA', kind='operand', line=1131)
W('14,2735', 0o00023, '', 'STORE', '18D', kind='interp', line=1132)
W('14,2736', 0o77650, '', 'GOTO', kind='interp', line=1133)
W('14,2737', 0o30721, '', '', 'CHKSB', 'RETURN TO CAL. 2ND ANGLE', kind='operand', line=1134)
W('14,2740', 0o45345, 'CHKSD', 'DLOAD', 'DSU', kind='interp', line=1135)
W('14,2741', 0o00025, '', '', 'THETA', 'COMPUTE POS DIFF', kind='operand', line=1136)
W('14,2742', 0o00023, '', '', '18D', kind='operand', line=1137)
W('14,2743', 0o47046, '', 'ABS', 'RTB', kind='interp', line=1138)
W('14,2744', 0o45544, '', '', 'SGNAGREE', kind='operand', line=1139)
W('14,2745', 0o01046, '', 'STORE', 'NORMTEM1', kind='interp', line=1140)
W('14,2746', 0o77414, '', 'SET', 'EXIT', kind='interp', line=1141)
W('14,2747', 0o00074, '', '', 'FREEFLAG', kind='operand', line=1142)
W('14,2750', 0o35021, '', 'CAF', 'ZERO', line=1143)
W('14,2751', 0o04662, '', 'TC', 'BANKCALL', line=1144)
W('14,2752', 0o20703, '', 'CADR', 'CLEANDSP', kind='data', line=1145)

W('14,2753', 0o32767, '', 'CAF', 'VB6N5', line=1147)
# Page 761
W('14,2754', 0o04662, '', 'TC', 'BANKCALL', line=1149)
W('14,2755', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=1150)
W('14,2756', 0o14106, '', 'TCF', 'GOTOPOOH', line=1151)
W('14,2757', 0o02764, '', 'TC', 'CHKSDA', 'PROCEED', line=1152)
W('14,2760', 0o06006, '', 'TC', 'INTPRET', line=1153)
W('14,2761', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=1154)
W('14,2762', 0o00274, '', '', 'FREEFLAG', kind='operand', line=1155)
W('14,2763', 0o02777, '', '', 'QMIN', kind='operand', line=1156)
W('14,2764', 0o06006, 'CHKSDA', 'TC', 'INTPRET', line=1157)
W('14,2765', 0o77650, '', 'GOTO', kind='interp', line=1158)
W('14,2766', 0o02777, '', '', 'QMIN', kind='operand', line=1159)
W('14,2767', 0o01405, 'VB6N5', 'VN', '605', kind='data', line=1160)

# NAME -- CAL53A
# FUNCTION -- COARSE ALIGN THE IMU, IF NECESSARY
# CALLING SEQUENCE -- CALL CAL53A
# INPUT -- PRESENT GIMBAL ANGLES -- CDUX, CDUY, CDUZ
# DESIRED GIMBAL ANGLES -- THETAD,+1,+2
# OUTPUT -- THE IMU COORDINATES AT STORED IN REFSMMAT
# SUBROUTINES -- 1.IMUCOARS, 2.IMUSTALL, 3CURTAINS

#   COUNT 14/R50

W('14,2770', 0o77624, 'CAL53A', 'CALL', kind='interp', line=1172)
W('14,2771', 0o22331, '', '', 'S52.2', 'MAKE FINAL COMP OF GIMBAL ANGLES', kind='operand', line=1173)
W('14,2772', 0o66234, '', 'RTB', 'SSP', kind='interp', line=1174)
W('14,2773', 0o32324, '', '', 'RDCDUS', 'READ CDUS', kind='operand', line=1175)
W('14,2774', 0o00051, '', '', 'S1', kind='operand', line=1176)
W('14,2775', 0o00001, '', '', '1', kind='operand', line=1177)
W('14,2776', 0o40370, '', 'AXT,1', 'SETPD', kind='interp', line=1178)
W('14,2777', 0o00003, '', '', '3', kind='operand', line=1179)
W('14,3000', 0o00005, '', '', '4', kind='operand', line=1180)
W('14,3001', 0o70543, 'CALOOP', 'DLOAD*', 'SR1', kind='interp', line=1181)
W('14,3002', 0o01161, '', '', 'THETAD +3D,1', kind='operand', line=1182)
W('14,3003', 0o70523, '', 'PDDL*', 'SR1', kind='interp', line=1183)
W('14,3004', 0o00005, '', '', '4,1', kind='operand', line=1184)
W('14,3005', 0o51425, '', 'DSU', 'ABS', kind='interp', line=1185)
W('14,3006', 0o45206, '', 'PUSH', 'DSU', kind='interp', line=1186)
W('14,3007', 0o31066, '', '', 'DEGREE1', kind='operand', line=1187)
W('14,3010', 0o71240, '', 'BMN', 'DLOAD', kind='interp', line=1188)
W('14,3011', 0o31042, '', '', 'CALOOP1', kind='operand', line=1189)
W('14,3012', 0o51025, '', 'DSU', 'BPL', kind='interp', line=1190)
W('14,3013', 0o31067, '', '', 'DEG359', kind='operand', line=1191)
W('14,3014', 0o31042, '', '', 'CALOOP1', kind='operand', line=1192)
W('14,3015', 0o77776, 'COARFINE', 'EXIT', kind='interp', line=1193)
W('14,3016', 0o05412, '', 'TC', 'PHASCHNG', line=1194)
W('14,3017', 0o04024, '', 'OCT', '04024', kind='data', line=1195)
W('14,3020', 0o04662, '', 'TC', 'BANKCALL', line=1196)
W('14,3021', 0o16663, '', 'CADR', 'IMUCOARS', 'PERFORM COARSE ALIGNMENT', kind='data', line=1197)
W('14,3022', 0o04662, '', 'TC', 'BANKCALL', line=1198)
W('14,3023', 0o17577, '', 'CADR', 'IMUSTALL', 'REQUEST MODE SWITCH', kind='data', line=1199)
# Page 762
W('14,3024', 0o05757, '', 'TC', 'CURTAINS', line=1201)
W('14,3025', 0o04662, '', 'TC', 'BANKCALL', line=1202)
W('14,3026', 0o17073, '', 'CADR', 'IMUFIN20', kind='data', line=1203)
W('14,3027', 0o04662, '', 'TC', 'BANKCALL', line=1204)
W('14,3030', 0o17577, '', 'CADR', 'IMUSTALL', kind='data', line=1205)
W('14,3031', 0o05757, '', 'TC', 'CURTAINS', 'TEST FOR MALFUNCTION', line=1206)
W('14,3032', 0o06006, '', 'TC', 'INTPRET', line=1207)
W('14,3033', 0o77234, '', 'RTB', 'VLOAD', kind='interp', line=1208)
W('14,3034', 0o31275, '', '', 'SET1/PDT', kind='operand', line=1209)
W('14,3035', 0o11566, '', '', 'ZEROVEC', kind='operand', line=1210)
W('14,3036', 0o01472, '', 'STORE', 'GCOMP', kind='interp', line=1211)
W('14,3037', 0o52014, '', 'SET', 'GOTO', kind='interp', line=1212)
W('14,3040', 0o01060, '', '', 'DRIFTFLG', kind='operand', line=1213)
W('14,3041', 0o31044, '', '', 'FINEONLY', kind='operand', line=1214)
W('14,3042', 0o77700, 'CALOOP1', 'TIX,1', kind='interp', line=1215)
W('14,3043', 0o31001, '', '', 'CALOOP', kind='operand', line=1216)
W('14,3044', 0o75160, 'FINEONLY', 'AXC,1', 'AXC,2', kind='interp', line=1217)
W('14,3045', 0o02671, '', '', 'XSM', kind='operand', line=1218)
W('14,3046', 0o01735, '', '', 'REFSMMAT', kind='operand', line=1219)
W('14,3047', 0o77624, '', 'CALL', kind='interp', line=1220)
W('14,3050', 0o31053, '', '', 'MATMOVE', kind='operand', line=1221)
W('14,3051', 0o77650, '', 'GOTO', kind='interp', line=1222)
W('14,3052', 0o32116, '', '', 'CAL53RET', kind='operand', line=1223)
W('14,3053', 0o77773, 'MATMOVE', 'VLOAD*', '', 'TRANSFER MATRIX', kind='interp', line=1224)
W('14,3054', 0o00001, '', '', '0,1', kind='operand', line=1225)
W('14,3055', 0o10001, '', 'STORE', '0,2', kind='interp', line=1226)
W('14,3056', 0o77773, '', 'VLOAD*', kind='interp', line=1227)
W('14,3057', 0o00007, '', '', '6D,1', kind='operand', line=1228)
W('14,3060', 0o10007, '', 'STORE', '6D,2', kind='interp', line=1229)
W('14,3061', 0o77773, '', 'VLOAD*', kind='interp', line=1230)
W('14,3062', 0o00015, '', '', '12D,1', kind='operand', line=1231)
W('14,3063', 0o10015, '', 'STORE', '12D,2', kind='interp', line=1232)
W('14,3064', 0o77616, '', 'RVQ', kind='interp', line=1233)
W('14,3065', 0o00056, 'DEGREE1', 'DEC', '46', kind='data', line=1234)
W('14,3066', 0o37722, 'DEG359', 'DEC', '16338', kind='data', line=1235)
#   SETLOC P50S
#   BANK
W('15,2324', 0o00004, 'RDCDUS', 'INHINT', '', 'READ CDUS', line=1238)
W('15,2325', 0o30032, '', 'CA', 'CDUX', line=1239)
W('15,2326', 0o50120, '', 'INDEX', 'FIXLOC', line=1240)
W('15,2327', 0o54001, '', 'TS', '1', line=1241)
W('15,2330', 0o30033, '', 'CA', 'CDUY', line=1242)
W('15,2331', 0o50120, '', 'INDEX', 'FIXLOC', line=1243)
W('15,2332', 0o54002, '', 'TS', '2', line=1244)
W('15,2333', 0o30034, '', 'CA', 'CDUZ', line=1245)
W('15,2334', 0o50120, '', 'INDEX', 'FIXLOC', line=1246)
W('15,2335', 0o54003, '', 'TS', '3', line=1247)
W('15,2336', 0o00003, '', 'RELINT', line=1248)
W('15,2337', 0o06030, '', 'TC', 'DANZIG', line=1249)

# Page 763
# NAME:         GIMB
#
# FUNCTION:     DETERMINE AND COMPUTE THE DESIRED GIMBAL ANGLES TO BE USED FOR COARSE ALIGNMENT.
#
# CALLING SEQUENCE:  CALL GIMB
#
# INPUT:        DESIRED IMU INERTIAL ORIENTATION VECTORS:  XSMD, YSMD, ZSMD
#
# OUTPUT:       GIMBAL ANGLES LEFT IN THETAD, +1, +2
#
# SUBROUTINES USED:  1.CDUTRIG 2.CALCSMSC 3.CALCGA

#   SETLOC P50S2
#   BANK
#   COUNT 14/INFLT

W('16,2612', 0o41345, 'CALCSMSC', 'DLOAD', 'DMP', kind='interp', line=1268)
W('16,2613', 0o00737, '', '', 'SINCDUY', kind='operand', line=1269)
W('16,2614', 0o00747, '', '', 'COSCDUZ', kind='operand', line=1270)
W('16,2615', 0o77676, '', 'DCOMP', kind='interp', line=1271)
W('16,2616', 0o70525, '', 'PDDL', 'SR1', kind='interp', line=1272)
W('16,2617', 0o00741, '', '', 'SINCDUZ', kind='operand', line=1273)
W('16,2620', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=1274)
W('16,2621', 0o00745, '', '', 'COSCDUY', kind='operand', line=1275)
W('16,2622', 0o00747, '', '', 'COSCDUZ', kind='operand', line=1276)
W('16,2623', 0o76466, '', 'VDEF', 'VSL1', kind='interp', line=1277)
W('16,2624', 0o02714, '', 'STORE', 'XNB', kind='interp', line=1278)
W('16,2625', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=1279)
W('16,2626', 0o00743, '', '', 'SINCDUX', kind='operand', line=1280)
W('16,2627', 0o00741, '', '', 'SINCDUZ', kind='operand', line=1281)
W('16,2630', 0o77752, '', 'SL1', kind='interp', line=1282)
W('16,2631', 0o00033, '', 'STORE', '26D', kind='interp', line=1283)
W('16,2632', 0o77605, '', 'DMP', kind='interp', line=1284)
W('16,2633', 0o00737, '', '', 'SINCDUY', kind='operand', line=1285)
W('16,2634', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=1286)
W('16,2635', 0o00751, '', '', 'COSCDUX', kind='operand', line=1287)
W('16,2636', 0o00745, '', '', 'COSCDUY', kind='operand', line=1288)
W('16,2637', 0o77625, '', 'DSU', kind='interp', line=1289)
W('16,2640', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=1290)
W('16,2641', 0o00743, '', '', 'SINCDUX', kind='operand', line=1291)
W('16,2642', 0o00747, '', '', 'COSCDUZ', kind='operand', line=1292)
W('16,2643', 0o77676, '', 'DCOMP', kind='interp', line=1293)
W('16,2644', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=1294)
W('16,2645', 0o00751, '', '', 'COSCDUX', kind='operand', line=1295)
W('16,2646', 0o00737, '', '', 'SINCDUY', kind='operand', line=1296)
W('16,2647', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=1297)
W('16,2650', 0o00745, '', '', 'COSCDUY', kind='operand', line=1298)
W('16,2651', 0o00033, '', '', '26D', kind='operand', line=1299)
W('16,2652', 0o55415, '', 'DAD', 'VDEF', kind='interp', line=1300)
W('16,2653', 0o77772, '', 'VSL1', kind='interp', line=1301)
W('16,2654', 0o02730, '', 'STORE', 'ZNB', kind='interp', line=1302)
W('16,2655', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=1303)
W('16,2656', 0o02714, '', '', 'XNB', kind='operand', line=1304)
W('16,2657', 0o02722, '', 'STORE', 'YNB', kind='interp', line=1305)
W('16,2660', 0o77616, '', 'RVQ', kind='interp', line=1306)

# NAME -- P51 -- IMU ORIENTATION DETERMINATION
# MOD. NO. 2    21 DEC 66                               LOG SECTION -- P51-P53
# Page 764
# MOD BY STURLAUGSON                                    ASSEMBLY SUNDISK REV15
#
# FUNCTIONAL DESCRIPTION
# DETERMINES THE INERTIAL ORIENTATION OF THE IMU.  THE PROGRAM IS SELECTED BY DSKY ENTRY.  THE SIGHTING
# ROUTINE IS CALLED TO COLLECT THE CDU COUNTERS AND SHAFT AND TRUNNION ANGLES FOR A SIGHTED STAR.  THE DATA IS
# THEN PROCESSED AS FOLLOWS.
#
# 1.  SEXTANT ANGLES ARE COMPUTED IN TERMS OF NAVIGATIONAL BASE COORDINATES.  LET SA AND TA BE THE SHAFT AND
# TRUNNION ANGLES, RESPECTIVELY.  THEN,
# _
# V  = (SIN(TA)*COS(SA), SIN(TA)*SIN(SA), COS(TA))        (A COLUMN VECTOR)
# NB
# THE OUTPUT IS A HALF-UNIT VECTOR STORED IN STARM.
#
# 2.  THIS VECTOR IN NAV. BASE COORDS. IS THEN TRANSFORMED TO ONE IN STABLE MEMBER COORDINATES.
# _    T  T  T _
# V = Q *Q *Q *V  ,       WHERE
# 1  2  3  NB
#
# ( COS(IG)   0    -SIN(IG) )
# (                         )                                        THE GIMBAL ANGLES ARE COMPUTED FROM
# Q  = (   0       1       0     ), IG= INNER GIMBAL ANGLE                THE CDU COUNTERS AT NBSM (USING AXIS-
# 1   (                         )                                        ROT AND CDULOGIC)
# ( SIN(IG)   0     COS(IG) )
#
# ( COS(MG) SIN(MG)   0     )
# (                         )
# Q  = (-SIN(MG) COS(MG)   0     ), MG= MIDDLE GIMBAL ANGLE
# 2   (                         )
# (   0       0       1     )
#
# (   1       0       0     )
# (                         )
# Q  = (   0     COS(OG) SIN(OG) ), OG= OUTER GIMBAL ANGLE
# 3   (                         )
# (   0    -SIN(OG) COS(OG) )
#
# 3.  THE STAR NUMBER IS SAVED AND THE SECOND STAR IS THEN SIMILARLY PROCESSED.
#
# 4.  THE ANGLE BETWEEN THE TWO STARS IS THEN CHECKED AT CKSDATA.
#
# 5.  REFSMMAT IS THEN COMPUTED AT AXISGEN AS FOLLOWS.
# _      _
# LET S  AND S  BE TWO STAR VECTORS EXPRESSED IN TWO COORDINATE SYSTEMS, A AND B (BASIC AND STABLE MEMBER).
# 1      2
# Page 765
# DEFINE,
# _    _
# U  = S
# A    A1
# _         _    _
# V  = UNIT(S  x S  )
# A         A1   A2
# _    _   _
# W  = U x V
# A    A   A
#
# AND,
# _    _
# U  = S
# B    B1
# _         _    _
# V  = UNIT(S  x S  )
# B         B1   B2
# _    _   _
# W  = U x V
# B    B   B
#
# THEN
# _        _       _       _
# X  = U  *U + V  *V + W  *W
# B1  A   B1  A   B1  A
# _        _       _       _
# Y  = U  *U + V  *V + W  *W              (REFSMMAT)
# B2  A   B2  A   B2  A
# _        _       _       _
# Z  = U  *U + V  *V + W  *W
# B3  A   B3  A   B3  A
#
# THE INPUTS CONSIST OF THE FOUR HALF-UNIT VECTORS STORED AS FOLLOWS
# _
# S   IN 6-11 OF THE VAC AREA
# A1
# _
# S   IN 12-17 OF THE VAC AREA
# A2
# _
# S   IN STARAD
# B1
# Page 766      _
# S   IN STARAD +6
# B2
#
# CALLING SEQUENCE:
#
# THE PROGRAM IS CALLED BY THE ASTRONAUT BY DSKY ENTRY.
#
# SUBROUTINES CALLED:
#
# GOPERF3
# GOPERF1R
# GODSPR
# IMUCOARS
# IMUFIN20
# R53
# SXTNB
# NBSM
# MKRELEAS
# CHKSDATA
# MATMOVE
#
# ALARMS
#
# NONE
#
# ERASABLE INITIALIZATION:
#
# IMU ZERO FLAG SHOULD BE SET.
#
# OUTPUT
#
# REFSMMAT
# REFSMFLG
#
# DEBRIS
#
# WORK AREA
# STARAD
# STARIND
# BESTI
# BESTJ

#   SETLOC P50S1
#   BANK
#   COUNT 14/P5153

S('P53', 'equals', 0o41067, line=1447)
W('14,3067', 0o41320, 'P51', 'CS', 'IMODES30', line=1448)
W('14,3070', 0o75007, '', 'MASK', 'BIT9', line=1449)
W('14,3071', 0o10000, '', 'CCS', 'A', line=1450)
# Page 767
W('14,3072', 0o03076, '', 'TC', 'P51A', line=1452)
W('14,3073', 0o05650, '', 'TC', 'ALARM', line=1453)
W('14,3074', 0o00210, '', 'OCT', '210', kind='data', line=1454)
W('14,3075', 0o04106, '', 'TC', 'GOTOPOOH', line=1455)
W('14,3076', 0o04662, 'P51A', 'TC', 'BANKCALL', line=1456)
W('14,3077', 0o17667, '', 'CADR', 'R02ZERO', kind='data', line=1457)

W('14,3100', 0o35025, 'P51AA', 'CAF', 'PRFMSTAQ', line=1459)
W('14,3101', 0o04662, '', 'TC', 'BANKCALL', line=1460)
W('14,3102', 0o21045, '', 'CADR', 'GOPERF1', kind='data', line=1461)
W('14,3103', 0o04106, '', 'TC', 'GOTOPOOH', 'TERM.', line=1462)
W('14,3104', 0o03140, '', 'TC', 'P51B', 'V33', line=1463)
W('14,3105', 0o05412, '', 'TC', 'PHASCHNG', line=1464)
W('14,3106', 0o05024, '', 'OCT', '05024', kind='data', line=1465)
W('14,3107', 0o13000, '', 'OCT', '13000', kind='data', line=1466)
W('14,3110', 0o35021, '', 'CAF', 'P51ZERO', line=1467)
W('14,3111', 0o55155, '', 'TS', 'THETAD', 'ZERO THE GIMBALS', line=1468)
W('14,3112', 0o55156, '', 'TS', 'THETAD +1', line=1469)
W('14,3113', 0o55157, '', 'TS', 'THETAD +2', line=1470)
W('14,3114', 0o33273, '', 'CAF', 'V6N22', line=1471)
W('14,3115', 0o04662, '', 'TC', 'BANKCALL', line=1472)
W('14,3116', 0o20673, '', 'CADR', 'GODSPRET', kind='data', line=1473)
W('14,3117', 0o33274, '', 'CAF', 'V41K', 'NOW DISPLAY COARSE ALIGN VERB 41', line=1474)
W('14,3120', 0o04662, '', 'TC', 'BANKCALL', line=1475)
W('14,3121', 0o20673, '', 'CADR', 'GODSPRET', kind='data', line=1476)
W('14,3122', 0o04662, '', 'TC', 'BANKCALL', line=1477)
W('14,3123', 0o16663, '', 'CADR', 'IMUCOARS', kind='data', line=1478)
W('14,3124', 0o04662, '', 'TC', 'BANKCALL', line=1479)
W('14,3125', 0o17577, '', 'CADR', 'IMUSTALL', kind='data', line=1480)
W('14,3126', 0o05757, '', 'TC', 'CURTAINS', 'CAGING OR BAD END', line=1481)
W('14,3127', 0o04662, '', 'TC', 'BANKCALL', 'SCHEDULE IFAILOK AND IMUFINED TASKS, IN 5', line=1482)
W('14,3130', 0o17073, '', 'CADR', 'IMUFIN20', 'AND 20 SECS. DIRECT RETURN AND NO STALL,', kind='data', line=1483)
W('14,3131', 0o04662, '', 'TC', 'BANKCALL', 'IF CAGING, BUT T4 WILL ZERO C/A ENABLE.', line=1484)
W('14,3132', 0o17577, '', 'CADR', 'IMUSTALL', 'IF PUT TO SLEEP, IMUFINED WILL WAKE US', kind='data', line=1485)
W('14,3133', 0o05757, '', 'TC', 'CURTAINS', 'UP.', line=1486)
W('14,3134', 0o05412, '', 'TC', 'PHASCHNG', line=1487)
W('14,3135', 0o05024, '', 'OCT', '05024', kind='data', line=1488)
W('14,3136', 0o13000, '', 'OCT', '13000', kind='data', line=1489)
W('14,3137', 0o13100, '', 'TCF', 'P51AA', 'COARSE ALIGN DONE:  RECYCLE FOR FINE', line=1490)

# Page 768
# DO STAR SIGHTING AND COMPUTE NEW REFSMMAT
W('14,3140', 0o05412, 'P51B', 'TC', 'PHASCHNG', line=1494)
W('14,3141', 0o00014, '', 'OCT', '00014', kind='data', line=1495)
W('14,3142', 0o06006, '', 'TC', 'INTPRET', line=1496)
W('14,3143', 0o40331, '', 'SSP', 'SETPD', kind='interp', line=1497)
W('14,3144', 0o00305, '', '', 'STARIND', 'INDEX -- STAR 1 OR 2', kind='operand', line=1498)
W('14,3145', 0o00000, '', '', '0', kind='operand', line=1499)
W('14,3146', 0o00001, '', '', '0', kind='operand', line=1500)
W('14,3147', 0o77234, '', 'RTB', 'VLOAD', kind='interp', line=1501)
W('14,3150', 0o31275, '', '', 'SET1/PDT', kind='operand', line=1502)
W('14,3151', 0o11566, '', '', 'ZEROVEC', kind='operand', line=1503)
W('14,3152', 0o01472, '', 'STORE', 'GCOMP', kind='interp', line=1504)
W('14,3153', 0o43014, '', 'SET', 'CLEAR', kind='interp', line=1505)
W('14,3154', 0o01060, '', '', 'DRIFTFLG', 'ENABLE T4 COMPENSATION', kind='operand', line=1506)
W('14,3155', 0o00666, '', '', 'TARG2FLG', 'SHOW MARK IS STAR --- NOT LANDMARK', kind='operand', line=1507)
W('14,3156', 0o77776, '', 'EXIT', kind='interp', line=1508)
W('14,3157', 0o35017, '', 'CAF', 'BIT1', line=1509)
W('14,3160', 0o54301, '', 'TS', 'MARKINDX', 'INITIALIZE FOR ONE MARK', line=1510)

W('14,3161', 0o05412, 'P51C', 'TC', 'PHASCHNG', line=1512)
W('14,3162', 0o05024, '', 'OCT', '05024', kind='data', line=1513)
W('14,3163', 0o13000, '', 'OCT', '13000', kind='data', line=1514)
W('14,3164', 0o05364, '', 'TC', 'CHECKMM', line=1515)
W('14,3165', 0o00065, '', 'MM', '53', 'BACKUP PROGRAM', kind='data', line=1516)
W('14,3166', 0o13174, '', 'TCF', 'P51C.1', 'NOT P53', line=1517)
W('14,3167', 0o06006, '', 'TC', 'INTPRET', line=1518)
W('14,3170', 0o77624, '', 'CALL', kind='interp', line=1519)
W('14,3171', 0o36056, '', '', 'R56', kind='operand', line=1520)
W('14,3172', 0o77650, '', 'GOTO', kind='interp', line=1521)
W('14,3173', 0o31177, '', '', 'P51C.2', kind='operand', line=1522)
W('14,3174', 0o06006, 'P51C.1', 'TC', 'INTPRET', line=1523)
W('14,3175', 0o77624, '', 'CALL', kind='interp', line=1524)
W('14,3176', 0o31300, '', '', 'R53', 'SIGHTING ROUTINE', kind='operand', line=1525)
W('14,3177', 0o77624, 'P51C.2', 'CALL', '', 'COMPUTE LOS IN SM FROM MARK DATA', kind='interp', line=1526)
W('14,3200', 0o36022, '', '', 'SXTSM', kind='operand', line=1527)
W('14,3201', 0o77606, '', 'PUSH', kind='interp', line=1528)
W('14,3202', 0o53135, '', 'SLOAD', 'BZE', kind='interp', line=1529)
W('14,3203', 0o00305, '', '', 'STARIND', kind='operand', line=1530)
W('14,3204', 0o31211, '', '', 'P51D', kind='operand', line=1531)
W('14,3205', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=1532)
W('14,3206', 0o75160, '', 'STORE', 'STARSAV2', 'DOWNLINK', kind='interp', line=1533)
W('14,3207', 0o77650, '', 'GOTO', kind='interp', line=1534)
W('14,3210', 0o31217, '', '', 'P51E', kind='operand', line=1535)
W('14,3211', 0o45575, 'P51D', 'VLOAD', 'STADR', kind='interp', line=1536)
W('14,3212', 0o61166, '', 'STODL', 'STARSAV1', kind='interp', line=1537)
W('14,3213', 0o02607, '', '', 'TSIGHT', kind='operand', line=1538)
W('14,3214', 0o77624, '', 'CALL', kind='interp', line=1539)
W('14,3215', 0o32340, '', '', 'PLANET', kind='operand', line=1540)
W('14,3216', 0o02601, '', 'STORE', 'PLANVEC', kind='interp', line=1541)
# Page 769
W('14,3217', 0o77776, 'P51E', 'EXIT', kind='interp', line=1543)
W('14,3220', 0o05412, '', 'TC', 'PHASCHNG', line=1544)
W('14,3221', 0o05024, '', 'OCT', '05024', kind='data', line=1545)
W('14,3222', 0o13000, '', 'OCT', '13000', kind='data', line=1546)
W('14,3223', 0o04662, '', 'TC', 'BANKCALL', line=1547)
W('14,3224', 0o16063, '', 'CADR', 'MKRELEAS', 'ZERO MARKSTAT', kind='data', line=1548)
W('14,3225', 0o10304, '', 'CCS', 'STARIND', line=1549)
W('14,3226', 0o13235, '', 'TCF', 'P51F', 'STAR 2', line=1550)
W('14,3227', 0o05412, '', 'TC', 'PHASCHNG', line=1551)
W('14,3230', 0o05024, '', 'OCT', '05024', kind='data', line=1552)
W('14,3231', 0o13000, '', 'OCT', '13000', kind='data', line=1553)
W('14,3232', 0o35017, '', 'CAF', 'BIT1', line=1554)
W('14,3233', 0o54304, '', 'TS', 'STARIND', line=1555)
W('14,3234', 0o13161, '', 'TCF', 'P51C', 'GO DO SECOND STAR', line=1556)
W('14,3235', 0o05412, 'P51F', 'TC', 'PHASCHNG', line=1557)
W('14,3236', 0o05024, '', 'OCT', '05024', kind='data', line=1558)
W('14,3237', 0o13000, '', 'OCT', '13000', kind='data', line=1559)
W('14,3240', 0o06006, '', 'TC', 'INTPRET', line=1560)
W('14,3241', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=1561)
W('14,3242', 0o02607, '', '', 'TSIGHT', kind='operand', line=1562)
W('14,3243', 0o32340, '', '', 'PLANET', kind='operand', line=1563)
W('14,3244', 0o24015, '', 'STOVL', '12D', kind='interp', line=1564)
W('14,3245', 0o02601, '', '', 'PLANVEC', kind='operand', line=1565)
W('14,3246', 0o24007, '', 'STOVL', '6D', kind='interp', line=1566)
W('14,3247', 0o02611, '', '', 'STARSAV1', kind='operand', line=1567)
W('14,3250', 0o26736, '', 'STOVL', 'STARAD', kind='interp', line=1568)
W('14,3251', 0o02617, '', '', 'STARSAV2', kind='operand', line=1569)
W('14,3252', 0o36744, '', 'STCALL', 'STARAD +6', kind='interp', line=1570)
W('14,3253', 0o30714, '', '', 'CHKSDATA', 'CHECK STAR ANGLES IN STARAD AND', kind='operand', line=1571)
W('14,3254', 0o77414, '', 'BON', 'EXIT', kind='interp', line=1572)
W('14,3255', 0o00314, '', '', 'FREEFLAG', kind='operand', line=1573)
W('14,3256', 0o31260, '', '', 'P51G', kind='operand', line=1574)
W('14,3257', 0o03100, '', 'TC', 'P51AA', line=1575)
W('14,3260', 0o77624, 'P51G', 'CALL', kind='interp', line=1576)
W('14,3261', 0o47401, '', '', 'AXISGEN', 'COME BACK WITH REFSMMAT IN XDC', kind='operand', line=1577)
W('14,3262', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=1578)
W('14,3263', 0o02713, '', '', 'XDC', kind='operand', line=1579)
W('14,3264', 0o01735, '', '', 'REFSMMAT', kind='operand', line=1580)
W('14,3265', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=1581)
W('14,3266', 0o01662, '', '', 'REFSMFLG', kind='operand', line=1582)
W('14,3267', 0o31053, '', '', 'MATMOVE', kind='operand', line=1583)
W('14,3270', 0o52014, '', 'SET', 'GOTO', kind='interp', line=1584)
W('14,3271', 0o01462, '', '', 'REFSMFLG', kind='operand', line=1585)
W('14,3272', 0o32145, '', '', 'ENDP50S', kind='operand', line=1586)
S('PRFMSTAQ', 'equals', 0o5025, line=1587)
S('P51ZERO', 'equals', 0o5021, line=1588)
S('P51FIVE', 'equals', 0o5022, line=1589)
W('14,3273', 0o01426, 'V6N22', 'VN', '0622', kind='data', line=1590)
W('14,3274', 0o12200, 'V41K', 'VN', '4100', kind='data', line=1591)
W('14,3275', 0o30025, 'SET1/PDT', 'CA', 'TIME1', line=1592)
# Page 770
W('14,3276', 0o55074, '', 'TS', '1/PIPADT', line=1594)
W('14,3277', 0o16030, '', 'TCF', 'DANZIG', line=1595)

# Page 771
# SXTSM COMPUTES AN LOS VECTOR IN SM COORD FROM OCDU AND ICDU MARK DATA

#   SETLOC P50S3
#   BANK
W('17,2022', 0o77620, 'SXTSM', 'STQ', kind='interp', line=1602)
W('17,2023', 0o00300, '', '', 'QMAJ', kind='operand', line=1603)
W('17,2024', 0o70740, '', 'LXC,1', 'DLOAD*', kind='interp', line=1604)
W('17,2025', 0o01330, '', '', 'MARKSTAT', kind='operand', line=1605)
W('17,2026', 0o00001, '', '', '0D,1', kind='operand', line=1606)
W('17,2027', 0o02607, '', 'STORE', 'TSIGHT', kind='interp', line=1607)
W('17,2030', 0o66744, '', 'LXC,2', 'SLOAD*', kind='interp', line=1608)
W('17,2031', 0o00304, '', '', 'STARIND', kind='operand', line=1609)
W('17,2032', 0o41722, '', '', 'MKDNCDR,2', kind='operand', line=1610)
W('17,2033', 0o76744, '', 'LXC,2', 'VLOAD*', kind='interp', line=1611)
W('17,2034', 0o00154, '', '', 'MPAC', kind='operand', line=1612)
W('17,2035', 0o00001, '', '', '0,1', kind='operand', line=1613)
W('17,2036', 0o10001, '', 'STORE', '0,2', kind='interp', line=1614)
W('17,2037', 0o77743, '', 'DLOAD*', kind='interp', line=1615)
W('17,2040', 0o00006, '', '', '5,1', kind='operand', line=1616)
W('17,2041', 0o10006, '', 'STORE', '5,2', kind='interp', line=1617)
W('17,2042', 0o77624, '', 'CALL', kind='interp', line=1618)
W('17,2043', 0o46000, '', '', 'SXTNB', 'COMPUTE LOS VECTOR FROM OCDU IN MKVAC', kind='operand', line=1619)
W('17,2044', 0o62150, '', 'LXA,1', 'INCR,1', kind='interp', line=1620)
W('17,2045', 0o01330, '', '', 'MARKSTAT', kind='operand', line=1621)
W('17,2046', 0o00002, '', '', '2', 'INCREMENT TO BASE ADR OF ICDU', kind='operand', line=1622)
W('17,2047', 0o45130, '', 'SXA,1', 'CALL', kind='interp', line=1623)
W('17,2050', 0o00050, '', '', 'S1', kind='operand', line=1624)
W('17,2051', 0o47606, '', '', 'NBSM', 'TRANSFORM LOS TO SM', kind='operand', line=1625)
W('17,2052', 0o77650, '', 'GOTO', kind='interp', line=1626)
W('17,2053', 0o00300, '', '', 'QMAJ', kind='operand', line=1627)
W('17,2054', 0o03674, 'MKDNCDR', 'ECADR', 'MARKDOWN', kind='data', line=1628)
W('17,2055', 0o03502, '', 'ECADR', 'MARK2DWN', kind='data', line=1629)

# Page 772
# PROGRAM DESCRIPTION:  R53 -- SIGHTING MARK ROUTINE
# MOD. NO. 2                                            21 DEC 66
# MOD. BY STURLAUGSON
#
# FUNCTIONAL DESCRIPTION:
#
# TO PERFORM A SATISFACTORY NUMBER OF SIGHTING MARKS FOR THE REQUESTING PROGRAM (OR ROUTINE).  SIGHTINGS
# CAN BE MADE ON A STAR OR LANDMARK.  WHEN THE CMC ACCEPTS A MARK IT RECORDS AND STORES 5 ANGLES (3 ICDUS AND 2
# OCDUS) AND THE TIME OF THE MARK.
#
# CALLING SEQUENCE:
#
# R53 IS CALLED AND RETURNS IN INTERPRETIVE CODE.  RETURN IS VIA QPRET.
# THERE IS NO ERROR EXIT IN THIS ROUTINE ITSELF.
#
# SUBROUTINES CALLED
#
# SXTMARK
# OPTSTALL
# GOFLASH
#
# ERASABLE INITIALIZATION:
#
# TARGET FLAG -- STAR OR LANDMARK
# MARKINDX -- NUMBER OF MARKS WANTED
# STARIND -- INDEX TO BESTI OR BESTJ (STAR NUMBER)
#
# OUTPUT
#
# MARKSTAT CONTAINS INDEX TO VACANT AREA WEHRE MARK DATA IS STORED
# BESTI (INDEXED BY STARIND) CONTAINS STAR NUMBER SIGHTED.
#
# DEBRIS
#
# MARKINDX CONTAINS NUMBER OF MARKS DESIRED

#   SETLOC RT53
#   BANK

#   COUNT 14/R53

W('14,3300', 0o43020, 'R53', 'STQ', 'SET', 'SET SIGHTING MARK FLAG', kind='interp', line=1673)
W('14,3301', 0o03501, '', '', 'R53EXIT', kind='operand', line=1674)
W('14,3302', 0o00071, '', '', 'R53FLAG', kind='operand', line=1675)
W('14,3303', 0o77776, '', 'EXIT', kind='interp', line=1676)
W('14,3304', 0o30301, 'R53A', 'CA', 'MARKINDX', 'NUMBER OF MARKS', line=1677)
W('14,3305', 0o75023, '', 'MASK', 'LOW3', line=1678)
W('14,3306', 0o04662, '', 'TC', 'BANKCALL', line=1679)
W('14,3307', 0o16002, '', 'CADR', 'SXTMARK', kind='data', line=1680)
W('14,3310', 0o04662, '', 'TC', 'BANKCALL', line=1681)
W('14,3311', 0o17573, '', 'CADR', 'OPTSTALL', kind='data', line=1682)
W('14,3312', 0o05757, '', 'TC', 'CURTAINS', line=1683)
W('14,3313', 0o51330, '', 'INDEX', 'MARKSTAT', line=1684)
W('14,3314', 0o10052, '', 'CCS', 'QPRET', 'NUMBER OF MARKS ACTUALLY DONE', line=1685)
W('14,3315', 0o13326, '', 'TCF', 'R53B', line=1686)
W('14,3316', 0o13320, '', 'TCF', '+2', 'ZERO', line=1687)
W('14,3317', 0o13320, '', 'TCF', '+1', 'CCS HOLE', line=1688)
W('14,3320', 0o35021, '', 'CAF', 'ZERO', 'HOUSEKEEP VAC AREA SAVE', line=1689)
W('14,3321', 0o57330, '', 'XCH', 'MARKSTAT', '      AND MARKSTAT', line=1690)
# Page 773
W('14,3322', 0o10000, '', 'CCS', 'A', line=1692)
W('14,3323', 0o50000, '', 'INDEX', 'A', line=1693)
W('14,3324', 0o54000, '', 'TS', '0', line=1694)
W('14,3325', 0o13304, '', 'TCF', 'R53A', line=1695)
W('14,3326', 0o05364, 'R53B', 'TC', 'CHECKMM', line=1696)
W('14,3327', 0o00026, '', 'MM', '22', kind='data', line=1697)
W('14,3330', 0o13332, '', 'TCF', '+2', line=1698)
W('14,3331', 0o13361, '', 'TCF', 'R53D', line=1699)
W('14,3332', 0o05364, '', 'TC', 'CHECKMM', line=1700)
W('14,3333', 0o00027, '', 'MM', '23', kind='data', line=1701)
W('14,3334', 0o13336, '', 'TCF', 'R53C1', line=1702)
W('14,3335', 0o13361, '', 'TCF', 'R53D', line=1703)
W('14,3336', 0o35021, 'R53C1', 'CAF', 'ZERO', line=1704)
W('14,3337', 0o04662, '', 'TC', 'BANKCALL', line=1705)
W('14,3340', 0o20703, '', 'CADR', 'CLEANDSP', kind='data', line=1706)
W('14,3341', 0o33365, 'R53C', 'CAF', 'V01N71', line=1707)
W('14,3342', 0o04662, '', 'TC', 'BANKCALL', line=1708)
W('14,3343', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=1709)
W('14,3344', 0o04106, '', 'TC', 'GOTOPOOH', 'TERM.', line=1710)
W('14,3345', 0o13347, '', 'TCF', 'R53Z', line=1711)
W('14,3346', 0o03341, '', 'TC', 'R53C', 'RECYCLE', line=1712)
W('14,3347', 0o03366, 'R53Z', 'TC', 'CHKSCODE', line=1713)
W('14,3350', 0o04400, '', 'TC', 'FALTON', line=1714)
W('14,3351', 0o03341, '', 'TC', 'R53C', line=1715)
W('14,3352', 0o47713, '', 'CS', 'HIGH9', line=1716)
W('14,3353', 0o70735, '', 'MASK', 'STARCODE', line=1717)
W('14,3354', 0o00006, '', 'EXTEND', line=1718)
W('14,3355', 0o76211, '', 'MP', 'SIGHTSIX', line=1719)
W('14,3356', 0o56001, '', 'XCH', 'L', line=1720)
W('14,3357', 0o50304, '', 'INDEX', 'STARIND', line=1721)
W('14,3360', 0o54302, '', 'TS', 'BESTI', line=1722)
W('14,3361', 0o06006, 'R53D', 'TC', 'INTPRET', line=1723)
W('14,3362', 0o77614, 'R53OUT', 'SETGO', kind='interp', line=1724)
W('14,3363', 0o03420, '', '', 'TERMIFLG', 'SET TERMINATE FOR R52', kind='operand', line=1725)
W('14,3364', 0o03501, '', '', 'R53EXIT', kind='operand', line=1726)
S('SIGHTSIX', 'equals', 0o6211, line=1727)
W('14,3365', 0o00307, 'V01N71', 'VN', '0171', kind='data', line=1728)

# ****** KEEP IN SAME BANK AS R51 AND R53 ********
W('14,3366', 0o10735, 'CHKSCODE', 'CCS', 'STARCODE', line=1731)
W('14,3367', 0o63376, '', 'AD', 'NEG47', line=1732)
W('14,3370', 0o10000, '', 'CCS', 'A', line=1733)
W('14,3371', 0o00002, '', 'TC', 'Q', 'SC < 0 OR SC > 50', line=1734)
W('14,3372', 0o13374, '', 'TCF', '+2', 'SC = + OR - 0', line=1735)
W('14,3373', 0o13374, '', 'TCF', '+1', '0 <= SC< 50', line=1736)
W('14,3374', 0o50002, '', 'INDEX', 'Q', 'SC = 50', line=1737)
W('14,3375', 0o00002, '', 'TC', '00002', line=1738)
W('14,3376', 0o77730, 'NEG47', 'OCT', '77730', kind='data', line=1739)

# Page 774
# NAME -- S52.2
# FUNCTION -- COMPUTE GIMBAL ANGLES FOR DESIRED SM AND PRESENT VEHICLE
# CALL -- CALL S52.2
# INPUT -- X,Y,ZSMD
# OUTPUT -- OGC,IGC,MGC,THETAD,+1,+2
# SUBROUTINES -- CDUTRIG, CALCSMSC, MATMOVE, CALCGA

#   SETLOC S52/2
#   BANK

#   COUNT 13/S52.2
W('11,2331', 0o77620, 'S52.2', 'STQ', kind='interp', line=1753)
W('11,2332', 0o00300, '', '', 'QMAJ', kind='operand', line=1754)
W('11,2333', 0o77624, '', 'CALL', kind='interp', line=1755)
W('11,2334', 0o47477, '', '', 'CDUTRIG', kind='operand', line=1756)
W('11,2335', 0o77624, '', 'CALL', kind='interp', line=1757)
W('11,2336', 0o34612, '', '', 'CALCSMSC', kind='operand', line=1758)
W('11,2337', 0o66370, '', 'AXT,1', 'SSP', kind='interp', line=1759)
W('11,2340', 0o00022, '', '', '18D', kind='operand', line=1760)
W('11,2341', 0o00051, '', '', 'S1', kind='operand', line=1761)
W('11,2342', 0o00006, '', '', '6D', kind='operand', line=1762)
W('11,2343', 0o61373, 'S52.2A', 'VLOAD*', 'VXM', kind='interp', line=1763)
W('11,2344', 0o02736, '', '', 'XNB +18D,1', kind='operand', line=1764)
W('11,2345', 0o01736, '', '', 'REFSMMAT', kind='operand', line=1765)
W('11,2346', 0o77656, '', 'UNIT', kind='interp', line=1766)
W('11,2347', 0o06736, '', 'STORE', 'XNB +18D,1', kind='interp', line=1767)
W('11,2350', 0o77700, '', 'TIX,1', kind='interp', line=1768)
W('11,2351', 0o22343, '', '', 'S52.2A', kind='operand', line=1769)
W('11,2352', 0o75160, 'S52.2.1', 'AXC,1', 'AXC,2', kind='interp', line=1770)
W('11,2353', 0o00306, '', '', 'XSMD', kind='operand', line=1771)
W('11,2354', 0o02671, '', '', 'XSM', kind='operand', line=1772)
W('11,2355', 0o77624, '', 'CALL', kind='interp', line=1773)
W('11,2356', 0o31053, '', '', 'MATMOVE', kind='operand', line=1774)
W('11,2357', 0o77624, '', 'CALL', kind='interp', line=1775)
W('11,2360', 0o47311, '', '', 'CALCGA', kind='operand', line=1776)
W('11,2361', 0o77650, '', 'GOTO', kind='interp', line=1777)
W('11,2362', 0o00300, '', '', 'QMAJ', kind='operand', line=1778)

# Page 775
# PROGRAM NAME:  SR52.1                         DATE:  DEC 20 1968
# MOD 1                                         LOG SEC:  P51-P53
# BY KEN VINCENT                                ASSEMBLY:  SUNDISK REV 40
#
# FUNCTION
#
# TARG1 AND TARG2 FLAGS ARE LOOKED AT TO DETERMINE IF THE TARGET IS THE
# LEM, STAR, OR LANDMARK.  IN CASE OF LEM OR LMK, THE PRESENT TIME PLUS
# 2 SECONDS IS SAVED IN AOPTIME (ALIAS STARAD, +1).  IF THE LEM IS
# THE TARGET THEN CONIC UPDATES OF THE CSM AND LEM ARE MADE TO
# THE TIME IN AOPTIME.  THE UNIT OF THE DIFFERENCE OF LEM AND CSM
# POSITION VECTORS BECOMES THE REFERENCE SIGHTING VECTOR USED IN THE
# COMMON PART OF THE THIS PROGRAM.
#
# IN THE CASE OF LANDMARK, THE CSM IS UPDATED CONICALLY.  THE RADIUS
# VECTOR FOR THE LANDMARK IS OBTAINED FROM LALOTORV.  BOTH OF THESE ARE
# FOUND FOR THE TIME IN AOPTIME.  THE UNIT OF THE DIFFERENCE BETWEEN
# THE LANDMARK AND CSM RADIUS VECTORS BECOMES THE REFERENCE SIGHTING
# VECTOR FOR THE COMMON PART OF THIS ROUTINE.
#
# IF A STAR IS THE TARGET, THE PROPER STAR IS OBTAINED FROM THE CATALOG
# AND THIS VECTOR BECOMES THE REFERENCE SIGHTING VECTOR.
#
# THE COMMON PART OF THIS PROGRAM TRANSFORMS THE REFERENCE SIGHTING
# VECTOR INTO STABLE MEMBER COORDINATES.  IT READS THE IMU-CDUS AND USES
# THIS DATA IN A CALL TO CALCSXA.  ON RETURN FROM CALCSXA A TEST IS
# MADE TO SEE IF THE TRUNNION ANGLE IS GREATER THAN  90DEG OR 38DEG.
# MADE TO SEE IF THE TRUNNION ANGLE IS GREATER THAN 90DEG. OR 50DEG.
#
# CALLING SEQUENCE
#
# L+4     RETURN WHEN SHAFT OR TRUNION NOT WITHIN 5 DEG OF DESIRED
# L       TC      BANKCALL
# L+1     CADR    SR52.1
# L+2     ERROR RETURN    TRUNNION GREATER THAN 90 DEG.
# L+3     ERROR RETURN    TRUNNION GREATER THAN 50 DEG
# L+4     NORMAL RETURN
#
# OUTPUT
#
# SAC:    SINGLE PREC, 2'S COMP, SCALED AT HALF REVS -- SHAFT ANGLE DESIRED.
# PAC:    SINGLE PREC, 2'S COMP, SCALED AT EIGHTH REVS -- TRUNNION ANGLE DESIRED.
#
# INITIALIZATION
#
# IF TARG1FLG =1 THEN TARGET IS LEM -- NO OTHER INPUT REQUIRED.
#
# IF TARG1FLG =0 AND TARG2FLG =0 THE TARGET IS STAR, STARIND SHOULD
# 0 OR 1 DENOTING BESTI OR BESTJ RESPECTIVELY AS STAR CODE.  STAR CODES
# ARE 6 TIMES STAR NUMBER.
#
# IF TARG1FLG =0 AND TARG2FLG =1 THEN TARGET IS LANDMARK.  SETT ROUTINE
# LALOTORV FOR INPUT REQUIREMENTS.  HERE FIXERAD=1 FOR CONSTANT EARTH
# RADIUS
#
# DEBRIS
#
# WORK AREA
# STARAD -- STAR+5 (STAR IS DESIRED LOS IN STABLE MEMBER COORDINATES)

#   COUNT* $$/SR521
# Page 776
#   SETLOC SR52/1
#   BANK

W('13,2244', 0o04711, 'SR52.1', 'TC', 'MAKECADR', line=1846)
W('13,2245', 0o55777, '', 'TS', 'QMIN', line=1847)
W('13,2246', 0o06006, '', 'TC', 'INTPRET', line=1848)
W('13,2247', 0o43234, '', 'RTB', 'DAD', kind='interp', line=1849)
W('13,2250', 0o45510, '', '', 'LOADTIME', kind='operand', line=1850)
W('13,2251', 0o26365, '', '', '1.3SECDP', kind='operand', line=1851)
W('13,2252', 0o02356, '', 'STORE', 'AOPTIME', kind='interp', line=1852)
W('13,2253', 0o43014, '', 'BON', 'BON', kind='interp', line=1853)
W('13,2254', 0o00705, '', '', 'TARG1FLG', kind='operand', line=1854)
W('13,2255', 0o26262, '', '', 'LEM52', kind='operand', line=1855)
W('13,2256', 0o00706, '', '', 'TARG2FLG', kind='operand', line=1856)
W('13,2257', 0o26272, '', '', 'LMK52', kind='operand', line=1857)
W('13,2260', 0o77650, '', 'GOTO', kind='interp', line=1858)
W('13,2261', 0o26313, '', '', 'STAR52', kind='operand', line=1859)
W('13,2262', 0o77745, 'LEM52', 'DLOAD', kind='interp', line=1860)
W('13,2263', 0o02356, '', '', 'AOPTIME', kind='operand', line=1861)
W('13,2264', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1862)
W('13,2265', 0o27126, '', '', 'LEMCONIC', kind='operand', line=1863)
W('13,2266', 0o77775, '', 'VLOAD', kind='interp', line=1864)
W('13,2267', 0o00001, '', '', 'RATT', kind='operand', line=1865)
W('13,2270', 0o77650, '', 'GOTO', kind='interp', line=1866)
W('13,2271', 0o26302, '', '', 'LMKLMCOM', kind='operand', line=1867)
W('13,2272', 0o71214, 'LMK52', 'BON', 'DLOAD', kind='interp', line=1868)
W('13,2273', 0o04305, '', '', 'ADVTRK', kind='operand', line=1869)
W('13,2274', 0o54000, '', '', 'ADVTRACK', kind='operand', line=1870)
W('13,2275', 0o02356, '', '', 'AOPTIME', kind='operand', line=1871)
W('13,2276', 0o77624, '', 'CALL', kind='interp', line=1872)
W('13,2277', 0o26441, '', '', 'LALOTORV', kind='operand', line=1873)
W('13,2300', 0o77775, '', 'VLOAD', kind='interp', line=1874)
W('13,2301', 0o02152, '', '', 'ALPHAV', kind='operand', line=1875)
W('13,2302', 0o16766, 'LMKLMCOM', 'STODL', 'STAR', kind='interp', line=1876)
W('13,2303', 0o02356, '', '', 'AOPTIME', kind='operand', line=1877)
W('13,2304', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=1878)
W('13,2305', 0o27114, '', '', 'CSMCONIC', kind='operand', line=1879)
W('13,2306', 0o52375, '', 'VLOAD', 'VSU', kind='interp', line=1880)
W('13,2307', 0o02766, '', '', 'STAR', kind='operand', line=1881)
W('13,2310', 0o00001, '', '', 'RATT', kind='operand', line=1882)
W('13,2311', 0o52056, '', 'UNIT', 'GOTO', kind='interp', line=1883)
W('13,2312', 0o26326, '', '', 'COM52', kind='operand', line=1884)
W('13,2313', 0o72131, 'STAR52', 'SSP', 'LXA,1', kind='interp', line=1885)
W('13,2314', 0o00051, '', '', 'S1', kind='operand', line=1886)
W('13,2315', 0o00000, '', '', '0', kind='operand', line=1887)
W('13,2316', 0o00304, '', '', 'STARIND', kind='operand', line=1888)
W('13,2317', 0o77700, '', 'TIX,1', kind='interp', line=1889)
W('13,2320', 0o26324, '', '', 'ST52ST', kind='operand', line=1890)
W('13,2321', 0o52175, '', 'VLOAD', 'GOTO', kind='interp', line=1891)
W('13,2322', 0o02617, '', '', 'STARSAV2', kind='operand', line=1892)
# Page 777
W('13,2323', 0o26326, '', '', 'COM52', kind='operand', line=1894)
W('13,2324', 0o77775, 'ST52ST', 'VLOAD', kind='interp', line=1895)
W('13,2325', 0o02611, '', '', 'STARSAV1', kind='operand', line=1896)
W('13,2326', 0o53521, 'COM52', 'MXV', 'UNIT', kind='interp', line=1897)
W('13,2327', 0o01736, '', '', 'REFSMMAT', kind='operand', line=1898)
W('13,2330', 0o02766, '', 'STORE', 'STAR', kind='interp', line=1899)
W('13,2331', 0o45001, '', 'SETPD', 'CALL', kind='interp', line=1900)
W('13,2332', 0o00001, '', '', '0', kind='operand', line=1901)
W('13,2333', 0o47477, '', '', 'CDUTRIG', 'COMPUTES SINES AND COSINES FOR CALCSXA', kind='operand', line=1902)
W('13,2334', 0o77624, '', 'CALL', '', '      NOW EXPECT TO SEE THE CDU ANGLES.', kind='interp', line=1903)
W('13,2335', 0o46034, '', '', 'CALCSXA', kind='operand', line=1904)
W('13,2336', 0o77414, '', 'BOFF', 'EXIT', kind='interp', line=1905)
W('13,2337', 0o01750, '', '', 'CULTFLAG', kind='operand', line=1906)
W('13,2340', 0o26342, '', '', 'TRUN38', kind='operand', line=1907)
W('13,2341', 0o02360, '', 'TC', 'SR52E1', line=1908)
W('13,2342', 0o45345, 'TRUN38', 'DLOAD', 'DSU', kind='interp', line=1909)
W('13,2343', 0o02776, '', '', 'PAC', kind='operand', line=1910)
W('13,2344', 0o26363, '', '', '38TRDEG', kind='operand', line=1911)
W('13,2345', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=1912)
W('13,2346', 0o26353, '', '', 'SR52E22', kind='operand', line=1913)
W('13,2347', 0o02776, '', '', 'PAC', kind='operand', line=1914)
W('13,2350', 0o51025, '', 'DSU', 'BPL', kind='interp', line=1915)
W('13,2351', 0o26367, '', '', '20DEGSMN', kind='operand', line=1916)
W('13,2352', 0o26355, '', '', 'SR52E3', kind='operand', line=1917)
W('13,2353', 0o77776, 'SR52E22', 'EXIT', kind='interp', line=1918)
W('13,2354', 0o02357, '', 'TC', 'SR52E2', line=1919)
W('13,2355', 0o77776, 'SR52E3', 'EXIT', kind='interp', line=1920)
W('13,2356', 0o25777, '', 'INCR', 'QMIN', line=1921)
W('13,2357', 0o25777, 'SR52E2', 'INCR', 'QMIN', line=1922)
W('13,2360', 0o31777, 'SR52E1', 'CA', 'QMIN', line=1923)
W('13,2361', 0o04666, '', 'TC', 'SWCALL', line=1924)
W('13,2362', 0o25252, '38TRDEG', '2DEC', '.66666667', 'CORRESPONDS TO 50 DEGS IN TRUNION', kind='data', line=1925)
W('13,2363', 0o25254, kind='data', line=1925)

W('13,2364', 0o00000, '1.3SECDP', '2DEC', '130', kind='data', line=1927)
W('13,2365', 0o00202, kind='data', line=1927)

W('13,2366', 0o61740, '20DEGSMN', 'DEC', '-07199', kind='data', line=1929)
W('13,2367', 0o77777, '', 'DEC', '-0', kind='data', line=1930)

# Page 778
# THE ADVTRACK ROUTINE IS USED TO COMPUTE AN OPTICS LOS VECTOR TO
# A POINT ON THE GROUND TRACK 60 DEGREES FORWARD OF THE LOCAL VERTICAL
# OF AN ADVANCED ORBIT A SPECIFIED NUMBER OF REVOLUTIONS FROM NOW.

#   SETLOC 26P50S
#   BANK
W('26,2000', 0o77601, 'ADVTRACK', 'SETPD', kind='interp', line=1939)
W('26,2001', 0o00001, '', '', '0', kind='operand', line=1940)
W('26,2002', 0o41575, '', 'VLOAD', 'PUSH', 'INITIALIZE FOR RP-TO-R', kind='interp', line=1941)
W('26,2003', 0o15327, '', '', 'UNITZ', 'UZ VEC IN PD 0-5', kind='operand', line=1942)
W('26,2004', 0o41434, '', 'RTB', 'PUSH', 'TIME IN PD 6-7', kind='interp', line=1943)
W('26,2005', 0o45510, '', '', 'LOADTIME', kind='operand', line=1944)
W('26,2006', 0o36356, '', 'STCALL', 'AOPTIME', 'TIME ALSO IN AOPTIME FOR CSMCONIC', kind='interp', line=1945)
W('26,2007', 0o55344, '', '', 'RP-TO-R', 'GET MOON ROTATION VEC IN REF', kind='operand', line=1946)
W('26,2010', 0o16766, '', 'STODL', 'STAR', kind='interp', line=1947)
W('26,2011', 0o02356, '', '', 'AOPTIME', 'PICK UP TIME', kind='operand', line=1948)
W('26,2012', 0o34041, '', 'STCALL', 'TDEC1', 'UPDATE STATE TO TIME', kind='interp', line=1949)
W('26,2013', 0o27114, '', '', 'CSMCONIC', kind='operand', line=1950)
W('26,2014', 0o47375, '', 'VLOAD', 'VXV', kind='interp', line=1951)
W('26,2015', 0o00007, '', '', 'VATT', kind='operand', line=1952)
W('26,2016', 0o00001, '', '', 'RATT', kind='operand', line=1953)
W('26,2017', 0o77656, '', 'UNIT', kind='interp', line=1954)
W('26,2020', 0o24031, '', 'STOVL', '24D', 'SAVE -UNIT(VxR) FOR 2ND ROTATION', kind='interp', line=1955)
W('26,2021', 0o00001, '', '', 'RATT', kind='operand', line=1956)
W('26,2022', 0o57456, '', 'UNIT', 'VCOMP', kind='interp', line=1957)
W('26,2023', 0o41401, '', 'SETPD', 'PUSH', 'PUSH LOS=-UNIT(RVEC) PD 0-5', kind='interp', line=1958)
W('26,2024', 0o00001, '', '', '0', kind='operand', line=1959)
W('26,2025', 0o77776, '', 'EXIT', kind='interp', line=1960)
W('26,2026', 0o31751, '', 'CA', 'LANDMARK', line=1961)
W('26,2027', 0o75023, '', 'MASK', 'SEVEN', 'GET NUMBER OF ADVANCE PERIODS', line=1962)
W('26,2030', 0o00006, '', 'EXTEND', line=1963)
W('26,2031', 0o75005, '', 'MP', 'BIT11', 'GET N/16', line=1964)
W('26,2032', 0o56001, '', 'XCH', 'L', line=1965)
W('26,2033', 0o50120, '', 'INDEX', 'FIXLOC', line=1966)
W('26,2034', 0o54036, '', 'TS', '30D', 'TEMP STORE N/16', line=1967)
W('26,2035', 0o06006, '', 'TC', 'INTPRET', line=1968)
W('26,2036', 0o41335, '', 'SLOAD', 'DMP', kind='interp', line=1969)
W('26,2037', 0o00037, '', '', '30D', kind='operand', line=1970)
W('26,2040', 0o14107, '', '', 'MPERIOD', kind='operand', line=1971)
W('26,2041', 0o36356, '', 'STCALL', 'AOPTIME', 'ROTATE ANG ABOUT UR', kind='interp', line=1972)
W('26,2042', 0o54057, '', '', 'ROTA', kind='operand', line=1973)
W('26,2043', 0o77775, '', 'VLOAD', kind='interp', line=1974)
W('26,2044', 0o00031, '', '', '24D', 'PICK UP 2ND ROTATION AXIS', kind='operand', line=1975)
W('26,2045', 0o16766, '', 'STODL', 'STAR', kind='interp', line=1976)
W('26,2046', 0o14105, '', '', 'DP1/6', kind='operand', line=1977)
W('26,2047', 0o77625, '', 'DSU', kind='interp', line=1978)
W('26,2050', 0o02356, '', '', 'AOPTIME', '2ND RAT ANGLE = 60 - A', kind='operand', line=1979)
W('26,2051', 0o36356, '', 'STCALL', 'AOPTIME', kind='interp', line=1980)
W('26,2052', 0o54057, '', '', 'ROTA', 'GO ROTATE 2ND TIME', kind='operand', line=1981)
W('26,2053', 0o77775, '', 'VLOAD', kind='interp', line=1982)
# Page 779
W('26,2054', 0o00001, '', '', '0', kind='operand', line=1984)
W('26,2055', 0o36766, '', 'STCALL', 'STAR', 'STORE FINAL LOS IN STAR', kind='interp', line=1985)
W('26,2056', 0o26326, '', '', 'COM52', 'RETURN TO SR52.1', kind='operand', line=1986)

W('26,2057', 0o73545, 'ROTA', 'DLOAD', 'SIN', kind='interp', line=1988)
W('26,2060', 0o02356, '', '', 'AOPTIME', kind='operand', line=1989)
W('26,2061', 0o47315, '', 'PDVL', 'VXV', 'PUSH 1/2SIN(A) PD 6-7', kind='interp', line=1990)
W('26,2062', 0o02766, '', '', 'STAR', '      UR VEC', kind='operand', line=1991)
W('26,2063', 0o00001, '', '', '0', '      LOS', kind='operand', line=1992)
W('26,2064', 0o72561, '', 'VXSC', 'VSL2', '1/2SIN(A)(URXLOS) PD 6-11', kind='interp', line=1993)
W('26,2065', 0o50315, '', 'PDVL', 'DOT', kind='interp', line=1994)
W('26,2066', 0o02766, '', '', 'STAR', kind='operand', line=1995)
W('26,2067', 0o00001, '', '', '0', kind='operand', line=1996)
W('26,2070', 0o72561, '', 'VXSC', 'VSL2', kind='interp', line=1997)
W('26,2071', 0o02766, '', '', 'STAR', kind='operand', line=1998)
W('26,2072', 0o71525, '', 'PDDL', 'COS', '1/2(UR . LOS)UR 12-17', kind='interp', line=1999)
W('26,2073', 0o02356, '', '', 'AOPTIME', kind='operand', line=2000)
W('26,2074', 0o51315, '', 'PDVL', 'BVSU', 'PUSH 1/2COS(A) 18-19', kind='interp', line=2001)
W('26,2075', 0o00015, '', '', '12D', kind='operand', line=2002)
W('26,2076', 0o00001, '', '', '0', kind='operand', line=2003)
W('26,2077', 0o76561, '', 'VXSC', 'VSL1', 'UP 18-19', kind='interp', line=2004)
W('26,2100', 0o53255, '', 'VAD', 'VAD', 'UP 12-17 UP 6011', kind='interp', line=2005)
W('26,2101', 0o40256, '', 'UNIT', 'SETPD', kind='interp', line=2006)
W('26,2102', 0o00001, '', '', '0', kind='operand', line=2007)
W('26,2103', 0o43406, '', 'PUSH', 'RVQ', kind='interp', line=2008)

W('26,2104', 0o05252, 'DP1/6', '2DEC', '.16666666', kind='data', line=2010)
W('26,2105', 0o25251, kind='data', line=2010)

W('26,2106', 0o01414, 'MPERIOD', '2DEC', '.047619', 'APPROX LUNAR ROT ANG IN 2HRS x 16', kind='data', line=2012)
W('26,2107', 0o06044, kind='data', line=2012)

# Page 780
# NAME -- S52.3
# FUNCTION --   XSMD= UNIT(YSMD x ZSMD)
# YSMD= UNIT(V X R)
# ZSMD= UNIT(-R)
# CALL --       DLOAD   CALL
# TALIGN
# S52.3
# INPUT --      TIME OF ALIGNMENT IN MPAC
# OUTPUT --     X,Y,ZSMD
# SUBROUTINES -- CSMCONIC

#   SETLOC P50S2
#   BANK

#   COUNT 15/S52.3
W('16,2661', 0o77620, 'S52.3', 'STQ', kind='interp', line=2030)
W('16,2662', 0o00300, '', '', 'QMAJ', kind='operand', line=2031)
W('16,2663', 0o34041, '', 'STCALL', 'TDEC1', kind='interp', line=2032)
W('16,2664', 0o27071, '', '', 'CSMPREC', kind='operand', line=2033)
W('16,2665', 0o77601, '', 'SETPD', kind='interp', line=2034)
W('16,2666', 0o00001, '', '', '0', kind='operand', line=2035)
W('16,2667', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=2036)
W('16,2670', 0o00001, '', '', 'RATT', kind='operand', line=2037)
W('16,2671', 0o77656, '', 'UNIT', kind='interp', line=2038)
W('16,2672', 0o24323, '', 'STOVL', 'ZSMD', kind='interp', line=2039)
W('16,2673', 0o00007, '', '', 'VATT', kind='operand', line=2040)
W('16,2674', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=2041)
W('16,2675', 0o00001, '', '', 'RATT', kind='operand', line=2042)
W('16,2676', 0o00315, '', 'STORE', 'YSMD', kind='interp', line=2043)
W('16,2677', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=2044)
W('16,2700', 0o00323, '', '', 'ZSMD', kind='operand', line=2045)
W('16,2701', 0o34307, '', 'STCALL', 'XSMD', kind='interp', line=2046)
W('16,2702', 0o00300, '', '', 'QMAJ', kind='operand', line=2047)

# Page 781
# PROGRAM DESCRIPTION:  R56 -- ALTERNATE LOS SIGHTING MARK ROUTINE
#
# FUNCTIONAL DESCRIPTION
#
# TO PERFORM SIGHTING MARKS FOR THE BACK-UP ALIGNMENT PROGRAMS (P53,P54).  THE ASTRONAUT KNOWS THE
# COORDINATES (OPTICS) OF THE ALTERNATE LINE OF SIGHT HE MUST USE FOR THIS ROUTINE.  WHEN THE ASTRONAUT KEYS IN
# ENTER IN RESPONSE TO THE FLASHING V50 N25 R1-XXXXX THE CMC STORES THE THREE ICDU ANGLES AND TWO ANGLES DISPLAYED
# IN N92.
#
# CALLING SEQUENCE
#
# CALL
# R56
#
# SUBROUTINES CALLED
#
# A PORTION OF SXTMARK (VAC.AREA SEARCH)
# GOFLASH
# GOPERF1
#
# ERASABLE INITIALIZATION
#
# STARIND:  INDEX TO STAR NUMBER
#
# OUTPUT
#
# MARKSTAT:  INDEX TO VAC.AREA WHERE OUTPUT IS STORED.
# BESTI (INDEXED BY STARIND) CONTAINS STAR NUMBER.
# ICDU AND OCDU ANGLES IN VAC. AREA AS FOLLOWS:
# VAC +2  CDUY
# VAC +3  CDUS
# VAC +4  CDUZ
# VAC +5  CDUT
# VAC +6  CDUX

#   COUNT* $$/R56
#   SETLOC P50S3
#   BANK
W('17,2056', 0o77420, 'R56', 'STQ', 'EXIT', kind='interp', line=2088)
W('17,2057', 0o03501, '', '', 'R53EXIT', kind='operand', line=2089)
W('17,2060', 0o32146, '', 'CAF', 'V06N94B', line=2090)
W('17,2061', 0o04662, '', 'TC', 'BANKCALL', line=2091)
W('17,2062', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=2092)
W('17,2063', 0o04106, '', 'TC', 'GOTOPOOH', 'TERM.', line=2093)
W('17,2064', 0o02066, '', 'TC', 'R56A', 'PROCEED:  ANGLES OK', line=2094)
W('17,2065', 0o02060, '', 'TC', '-5', 'ENTER:  NEW ANGLES', line=2095)
W('17,2066', 0o04662, 'R56A', 'TC', 'BANKCALL', line=2096)
W('17,2067', 0o16004, '', 'CADR', 'SXTMARK +2', 'INHIBIR EXT VB ACT AND FIND VAC AREA', kind='data', line=2097)

W('17,2070', 0o35021, '', 'CAF', 'ZERO', line=2099)
W('17,2071', 0o04662, '', 'TC', 'BANKCALL', line=2100)
W('17,2072', 0o20703, '', 'CADR', 'CLEANDSP', kind='data', line=2101)

W('17,2073', 0o32145, 'R56A1', 'CAF', 'VB53', 'DISPLAY V53 REQUESTING ALTERNATE MARK', line=2103)
W('17,2074', 0o04662, '', 'TC', 'BANKCALL', line=2104)
# Page 782
W('17,2075', 0o20564, '', 'CADR', 'GOMARK2', kind='data', line=2106)
W('17,2076', 0o14106, '', 'TCF', 'GOTOPOOH', 'V34:  TERMINATE', line=2107)
W('17,2077', 0o12073, '', 'TCF', 'R56A1', "V33:  DON'T PROCEED -- JUST ENTER TO MARK", line=2108)
W('17,2100', 0o06006, '', 'TC', 'INTPRET', line=2109)
W('17,2101', 0o77745, '', 'DLOAD', kind='interp', line=2110)
W('17,2102', 0o03731, '', '', 'MRKBUF1 +3', kind='operand', line=2111)
W('17,2103', 0o16774, '', 'STODL', 'SAC', kind='interp', line=2112)
W('17,2104', 0o03733, '', '', 'MRKBUF1 +5', kind='operand', line=2113)
W('17,2105', 0o02776, '', 'STORE', 'PAC', kind='interp', line=2114)
W('17,2106', 0o77776, '', 'EXIT', kind='interp', line=2115)
W('17,2107', 0o00004, '', 'INHINT', line=2116)
W('17,2110', 0o00006, '', 'EXTEND', line=2117)
W('17,2111', 0o30025, '', 'DCA', 'TIME2', line=2118)
W('17,2112', 0o51330, '', 'INDEX', 'MARKSTAT', line=2119)
W('17,2113', 0o52001, '', 'DXCH', '0', line=2120)
W('17,2114', 0o30033, '', 'CA', 'CDUY', 'ENTER:  THIS IS A BACKUP SYSTEM MARK', line=2121)
W('17,2115', 0o51330, '', 'INDEX', 'MARKSTAT', line=2122)
W('17,2116', 0o54002, '', 'TS', '2', line=2123)
W('17,2117', 0o31773, '', 'CA', 'SAC', line=2124)
W('17,2120', 0o51330, '', 'INDEX', 'MARKSTAT', line=2125)
W('17,2121', 0o54003, '', 'TS', '3', line=2126)
W('17,2122', 0o30034, '', 'CA', 'CDUZ', line=2127)
W('17,2123', 0o51330, '', 'INDEX', 'MARKSTAT', line=2128)
W('17,2124', 0o54004, '', 'TS', '4', line=2129)
W('17,2125', 0o31775, '', 'CA', 'PAC', line=2130)
W('17,2126', 0o51330, '', 'INDEX', 'MARKSTAT', line=2131)
W('17,2127', 0o54005, '', 'TS', '5', line=2132)
W('17,2130', 0o30032, '', 'CA', 'CDUX', line=2133)
W('17,2131', 0o51330, '', 'INDEX', 'MARKSTAT', line=2134)
W('17,2132', 0o54006, '', 'TS', '6', line=2135)
W('17,2133', 0o00003, '', 'RELINT', line=2136)
W('17,2134', 0o05536, '', 'TC', 'CLEARMRK', 'ENABLE EXTENDED VERBS', line=2137)
W('17,2135', 0o34333, '', 'CAF', 'OCT16', line=2138)
W('17,2136', 0o04662, '', 'TC', 'BANKCALL', line=2139)
W('17,2137', 0o21045, '', 'CADR', 'GOPERF1', kind='data', line=2140)
W('17,2140', 0o04106, '', 'TC', 'GOTOPOOH', 'TERM.', line=2141)
W('17,2141', 0o12143, '', 'TCF', 'R56B', 'PROCEED:  MARK COMPLETED', line=2142)
W('17,2142', 0o12070, '', 'TCF', 'R56A +2', 'RECYCLE:  DO ANOTHER MARK -- LIKE REJECT.', line=2143)
W('17,2143', 0o04662, 'R56B', 'TC', 'BANKCALL', line=2144)
W('17,2144', 0o31336, '', 'CADR', 'R53C1', kind='data', line=2145)
W('17,2145', 0o15200, 'VB53', 'VN', '05300', 'ALTERNATE MARK VERB', kind='data', line=2146)
W('17,2146', 0o01536, 'V06N94B', 'VN', '00694', kind='data', line=2147)
#   SETLOC P50S
#   BANK

W('15,2340', 0o02607, 'PLANET', 'STORE', 'TSIGHT', kind='interp', line=2151)
W('15,2341', 0o45020, '', 'STQ', 'CALL', kind='interp', line=2152)
W('15,2342', 0o02777, '', '', 'QMIN', kind='operand', line=2153)
W('15,2343', 0o30225, '', '', 'LOCSAM', kind='operand', line=2154)
W('15,2344', 0o77775, '', 'VLOAD', kind='interp', line=2155)
# Page 783
W('15,2345', 0o02736, '', '', 'VEARTH', kind='operand', line=2157)
W('15,2346', 0o24001, '', 'STOVL', '0D', kind='interp', line=2158)
W('15,2347', 0o02744, '', '', 'VSUN', kind='operand', line=2159)
W('15,2350', 0o26736, '', 'STOVL', 'VEARTH', kind='interp', line=2160)
W('15,2351', 0o00001, '', '', '0D', kind='operand', line=2161)
W('15,2352', 0o02744, '', 'STORE', 'VSUN', kind='interp', line=2162)
W('15,2353', 0o77776, 'NOSAM', 'EXIT', kind='interp', line=2163)
W('15,2354', 0o47713, '', 'CS', 'HIGH9', line=2164)
W('15,2355', 0o70735, '', 'MASK', 'STARCODE', line=2165)
W('15,2356', 0o00006, '', 'EXTEND', line=2166)
W('15,2357', 0o76211, '', 'MP', 'SIGHTSIX', line=2167)
W('15,2360', 0o56001, '', 'XCH', 'L', line=2168)
W('15,2361', 0o50304, '', 'INDEX', 'STARIND', line=2169)
W('15,2362', 0o54302, '', 'TS', 'BESTI', line=2170)
W('15,2363', 0o10000, '', 'CCS', 'A', line=2171)
W('15,2364', 0o12401, '', 'TCF', 'NOTPLAN', line=2172)
W('15,2365', 0o32431, '', 'CAF', 'VNPLANV', line=2173)
W('15,2366', 0o04662, '', 'TC', 'BANKCALL', line=2174)
W('15,2367', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=2175)
W('15,2370', 0o04106, '', 'TC', 'GOTOPOOH', line=2176)
W('15,2371', 0o02373, '', 'TC', '+2', line=2177)
W('15,2372', 0o02365, '', 'TC', '-5', line=2178)
W('15,2373', 0o06006, '', 'TC', 'INTPRET', line=2179)
W('15,2374', 0o74375, '', 'VLOAD', 'VXSC', kind='interp', line=2180)
W('15,2375', 0o03705, '', '', 'STARSAV3', kind='operand', line=2181)
W('15,2376', 0o32433, '', '', '1/SQR3', kind='operand', line=2182)
W('15,2377', 0o52056, '', 'UNIT', 'GOTO', kind='interp', line=2183)
W('15,2400', 0o32424, '', '', 'CORPLAN', kind='operand', line=2184)
W('15,2401', 0o40000, 'NOTPLAN', 'CS', 'A', line=2185)
W('15,2402', 0o62430, '', 'AD', 'DEC227', line=2186)
W('15,2403', 0o00006, '', 'EXTEND', line=2187)
W('15,2404', 0o62415, '', 'BZMF', 'CALSAM1', line=2188)
W('15,2405', 0o50304, '', 'INDEX', 'STARIND', line=2189)
W('15,2406', 0o30302, '', 'CA', 'BESTI', line=2190)
W('15,2407', 0o50120, '', 'INDEX', 'FIXLOC', line=2191)
W('15,2410', 0o54046, '', 'TS', 'X1', line=2192)
W('15,2411', 0o06006, '', 'TC', 'INTPRET', line=2193)
W('15,2412', 0o52173, '', 'VLOAD*', 'GOTO', kind='interp', line=2194)
W('15,2413', 0o31761, '', '', 'CATLOG,1', kind='operand', line=2195)
W('15,2414', 0o32424, '', '', 'CORPLAN', kind='operand', line=2196)
W('15,2415', 0o06006, 'CALSAM1', 'TC', 'INTPRET', line=2197)
W('15,2416', 0o70740, '', 'LXC,1', 'DLOAD*', kind='interp', line=2198)
W('15,2417', 0o00304, '', '', 'STARIND', kind='operand', line=2199)
W('15,2420', 0o00303, '', '', 'BESTI,1', kind='operand', line=2200)
W('15,2421', 0o76740, '', 'LXC,1', 'VLOAD*', kind='interp', line=2201)
W('15,2422', 0o00154, '', '', 'MPAC', kind='operand', line=2202)
W('15,2423', 0o02372, '', '', 'STARAD -228D,1', kind='operand', line=2203)
W('15,2424', 0o53455, 'CORPLAN', 'VAD', 'UNIT', kind='interp', line=2204)
W('15,2425', 0o03474, '', '', 'VEL/C', kind='operand', line=2205)
W('15,2426', 0o77650, '', 'GOTO', kind='interp', line=2206)
# Page 784
W('15,2427', 0o02777, '', '', 'QMIN', kind='operand', line=2208)
W('15,2430', 0o00343, 'DEC227', 'DEC', '227', kind='data', line=2209)
W('15,2431', 0o01530, 'VNPLANV', 'VN', '0688', kind='data', line=2210)
W('15,2432', 0o22363, '1/SQR3', '2DEC', '.57735021', kind='data', line=2211)
W('15,2433', 0o11623, kind='data', line=2211)
