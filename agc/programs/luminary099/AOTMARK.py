"""AOTMARK.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/AOTMARK.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 244-261 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('AOTMARK', 'AOTMARK.agc', 'Luminary099', pages='244-261')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     AOTMARK.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        244-261
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Luminary131/ file of the same
# name, using Luminary099 page images.
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

# Page 244
#   BANK 12
#   SETLOC AOTMARK1
#   BANK

#   EBANK= XYMARK
#   COUNT* $$/MARK

W('07,2000', 0o00004, 'AOTMARK', 'INHINT', line=37)
W('07,2001', 0o11312, '', 'CCS', 'MARKSTAT', 'SEE IF AOTMARK BUSY', line=38)
W('07,2002', 0o02004, '', 'TC', '+2', 'MARK SYSTEM BUSY -- DO ALARM', line=39)
W('07,2003', 0o02006, '', 'TC', 'EXTVBCHK', line=40)
W('07,2004', 0o05652, '', 'TC', 'POODOO', line=41)
W('07,2005', 0o00105, '', 'OCT', '00105', kind='data', line=42)

W('07,2006', 0o36242, 'EXTVBCHK', 'CAF', 'SIX', 'SEE IF EXT. VERB WORKING', line=44)
W('07,2007', 0o71044, '', 'MASK', 'EXTVBACT', line=45)
W('07,2010', 0o10000, '', 'CCS', 'A', line=46)
W('07,2011', 0o12044, '', 'TCF', 'MKABORT', 'YES -- ABORT', line=47)

W('07,2012', 0o34752, '', 'CAF', 'BIT2', 'NO -- DISALLOW SOME EXTENDED VERB ACTION', line=49)
W('07,2013', 0o27044, '', 'ADS', 'EXTVBACT', 'BIT2 RESET IN ENDMARK', line=50)
W('07,2014', 0o10400, 'MKVAC', 'CCS', 'VAC1USE', 'LOOK FOR A VAC AREAD -- DO ABORT IF', line=51)
W('07,2015', 0o12031, '', 'TCF', 'MKVACFND', 'NONE AVAILABLE', line=52)
W('07,2016', 0o10454, '', 'CCS', 'VAC2USE', line=53)
W('07,2017', 0o12031, '', 'TCF', 'MKVACFND', line=54)
W('07,2020', 0o10530, '', 'CCS', 'VAC3USE', line=55)
W('07,2021', 0o12031, '', 'TCF', 'MKVACFND', line=56)
W('07,2022', 0o10604, '', 'CCS', 'VAC4USE', line=57)
W('07,2023', 0o12031, '', 'TCF', 'MKVACFND', line=58)
W('07,2024', 0o10660, '', 'CCS', 'VAC5USE', line=59)
W('07,2025', 0o12031, '', 'TCF', 'MKVACFND', line=60)
W('07,2026', 0o52134, '', 'DXCH', 'BUF2', line=61)
W('07,2027', 0o05716, '', 'TC', 'BAILOUT1', 'ALL VAC AREAS OCCUPIED -- ABORT.', line=62)
W('07,2030', 0o01207, '', 'OCT', '01207', kind='data', line=63)

W('07,2031', 0o64752, 'MKVACFND', 'AD', 'TWO', line=65)
W('07,2032', 0o55312, '', 'TS', 'MARKSTAT', 'STORE VAC ADR IN LOW 9 OF MARKSTAT', line=66)

W('07,2033', 0o34755, '', 'CAF', 'ZERO', line=68)
W('07,2034', 0o51312, '', 'INDEX', 'MARKSTAT', line=69)
W('07,2035', 0o53777, '', 'TS', '0 -1', 'ZERO IN VACUSE REG TO SHOW VAC OCCUPIED', line=70)

W('07,2036', 0o35025, '', 'CAF', 'PRIO15', line=72)
W('07,2037', 0o05105, '', 'TC', 'FINDVAC', 'SET UP JOB FOR GETDAT', line=73)
#   EBANK= XYMARK
W('07,2040', 0o02063, '', '2CADR', 'GETDAT', kind='data', line=75)
W('07,2041', 0o16067, kind='data', line=75)

W('07,2042', 0o00003, '', 'RELINT', line=77)
W('07,2043', 0o14631, '', 'TCF', 'SWRETURN', line=78)
# Page 245
W('07,2044', 0o52134, 'MKABORT', 'DXCH', 'BUF2', line=80)
W('07,2045', 0o05716, '', 'TC', 'BAILOUT1', 'CONFLICT WITH EXTENDED VERB', line=81)
W('07,2046', 0o01211, '', 'OCT', '01211', kind='data', line=82)

W('07,2047', 0o34755, 'MKRELEAS', 'CAF', 'ZERO', line=84)
W('07,2050', 0o57312, '', 'XCH', 'MARKSTAT', 'SET MARKSTAT TO ZERO', line=85)
W('07,2051', 0o75004, '', 'MASK', 'LOW9', 'PICK UP VAC AREA AOR', line=86)
W('07,2052', 0o10000, '', 'CCS', 'A', line=87)
W('07,2053', 0o50000, '', 'INDEX', 'A', line=88)
W('07,2054', 0o54000, '', 'TS', '0', 'SHOW MKVAC AREA AVAILABLE', line=89)
W('07,2055', 0o34753, '', 'CAF', 'ONE', line=90)
W('07,2056', 0o04674, '', 'TC', 'IBNKCALL', line=91)
W('07,2057', 0o17665, '', 'CADR', 'GOODEND', 'GO WAKE UP CALLING JOB', kind='data', line=92)

# Page 246
W('07,2060', 0o34755, 'KILLAOT', 'CAF', 'ZERO', line=95)
W('07,2061', 0o55044, '', 'TS', 'EXTVBACT', 'TERMINATE AOTMARK -- ALLOW EXT VERB', line=96)
W('07,2062', 0o06001, '', 'TC', 'GOTOPOOH', line=97)
W('07,2063', 0o41312, 'GETDAT', 'CS', 'MARKSTAT', 'SET BIT12 TO DISCOURAGE MARKRUPT', line=98)
W('07,2064', 0o74740, '', 'MASK', 'BIT12', '      BIT12 RESET AT GETMARK', line=99)
W('07,2065', 0o27312, '', 'ADS', 'MARKSTAT', line=100)

W('07,2066', 0o32330, '', 'CAF', 'V01N71', 'DISPLAY DETENT AND STAR CODE', line=102)
W('07,2067', 0o04616, '', 'TC', 'BANKCALL', line=103)
W('07,2070', 0o20334, '', 'CADR', 'GOMARKF', kind='data', line=104)

W('07,2071', 0o12060, '', 'TCF', 'KILLAOT', 'V34 -- DOES GOTOPOOH', line=106)
W('07,2072', 0o12074, '', 'TCF', 'DODAT', 'V33 -- PROCEED -- USE THIS STAR FOR MARKS', line=107)
W('07,2073', 0o12063, 'ENTERDAT', 'TCF', 'GETDAT', 'ENTER -- REDISPLAY STAR CODE', line=108)

W('07,2074', 0o37744, 'DODAT', 'CAF', 'HIGH9', 'PICK DETENT CODE FROM BITS7-9 OF AOTCODE', line=110)
W('07,2075', 0o70735, '', 'MASK', 'AOTCODE', 'AND SEE IF CODE 1 TO 6', line=111)
W('07,2076', 0o00006, '', 'EXTEND', line=112)
W('07,2077', 0o74743, '', 'MP', 'BIT9', line=113)
W('07,2100', 0o55551, '', 'TS', 'XYMARK', 'STORE DETENT', line=114)

W('07,2101', 0o00006, '', 'EXTEND', line=116)
W('07,2102', 0o62063, '', 'BZMF', 'GETDAT', 'COAS CALIBRATION CODE - NO GOOD HERE', line=117)

W('07,2103', 0o65660, '', 'AD', 'NEG7', 'SEE IF DETENT 7 FOR COAS', line=119)
W('07,2104', 0o00006, '', 'EXTEND', line=120)
W('07,2105', 0o12107, '', 'BZF', 'CODE7', line=121)

W('07,2106', 0o12123, '', 'TCF', 'CODE1TO6', line=123)

W('07,2107', 0o32331, 'CODE7', 'CAF', 'V06N87*', 'CODE 7, COAS SIGHTING, GET OPTIC AXIS', line=125)
W('07,2110', 0o04616, '', 'TC', 'BANKCALL', 'AZ AND EL OF SIGHTING DEVICE FROM ASTRO', line=126)
W('07,2111', 0o20334, '', 'CADR', 'GOMARKF', kind='data', line=127)

W('07,2112', 0o12060, '', 'TCF', 'KILLAOT', 'V34 -- DOES GOTOPOOH', line=129)
W('07,2113', 0o12115, '', 'TCF', '+2', 'PROCEED', line=130)
W('07,2114', 0o12107, '', 'TCF', 'CODE7', 'ON ENTER, RECYCLE', line=131)
W('07,2115', 0o00006, '', 'EXTEND', line=132)
W('07,2116', 0o31350, '', 'DCA', 'AZ', 'PICK UP AZ AND EL IN SP 25 COMP', line=133)
W('07,2117', 0o50120, '', 'INDEX', 'FIXLOC', line=134)
W('07,2120', 0o52011, '', 'DXCH', '8D', 'STORE IN 8D AND 9D OF LOCAL VAC', line=135)
W('07,2121', 0o34755, '', 'CAF', 'ZERO', 'BACKUP SYSTEM TO BE USED', line=136)
W('07,2122', 0o12137, '', 'TCF', 'COASCODE', 'ZERO APPARENT ROTATION', line=137)

W('07,2123', 0o51551, 'CODE1TO6', 'INDEX', 'XYMARK', 'INDEX AOT POSITION BY DET CODE', line=139)
W('07,2124', 0o31411, '', 'CA', 'AOTEL -1', line=140)
W('07,2125', 0o50120, '', 'INDEX', 'FIXLOC', line=141)
W('07,2126', 0o54011, '', 'TS', '9D', 'STORE ELEVATION IN VAC+9D', line=142)

W('07,2127', 0o51551, '', 'INDEX', 'XYMARK', 'INDEX DET CODE 1,2 OR 3', line=144)
# Page 247
W('07,2130', 0o31403, '', 'CA', 'AOTAZ -1', line=146)
W('07,2131', 0o50120, '', 'INDEX', 'FIXLOC', line=147)
W('07,2132', 0o54010, '', 'TS', '8D', 'STORE AZIMUTH IN VAC +8D', line=148)

W('07,2133', 0o31405, '', 'CA', 'AOTAZ +1', 'COMPENSATION FOR APPARENT ROTATION OF', line=150)
W('07,2134', 0o00006, '', 'EXTEND', '', 'AOT FIELD OF VIEW IN LEFT AND RIGHT', line=151)
W('07,2135', 0o50120, '', 'INDEX', 'FIXLOC', 'DETENTS IS STORED IN VAC +10D IN SP', line=152)
W('07,2136', 0o20010, '', 'MSU', '8D', "PRECISION ONE'S COMPLEMENT", line=153)
W('07,2137', 0o50120, 'COASCODE', 'INDEX', 'FIXLOC', line=154)
W('07,2140', 0o54012, '', 'TS', '10D', 'ROT ANGLE', line=155)

W('07,2141', 0o06037, '', 'TC', 'INTPRET', 'COMPUTE X AND Y PLANE VECTORS', line=157)

# Page 248
# THE OPTAXIS SUBROUTINE COMPUTES THE X AND Y MARK PLANE VECS AND
# ROTATES THEM THRU THE APPARENT FIELD OF VIEW ROTATION UNIQUE TO AOT
# OPTAXIS USES OANB TO COMPUTE THE OPTIC AXIS
#
# INPUT --        AZIMUTH ANGLE IN SINGLE PREC AT CDU SCALE IN 8D OF JOB VAC
# ELEVATION ANGLE IN SINGLE PREC AT CDU SCALE IN 9D OF JOB VAC
# ROTATION ANGLE IN SINGLE PREC IS COMP SCALED BY PI IN 10D OF VAC
#
# OUTPUT --       OPTIC AXIS VEC IN NG COORDS IN SCAXIS
# X-MARK PLANE 1/4VEC IN NB COORDS AT 18D OF JOB VAC
# Y-MARK PLANE 1/4VEC IN NB COORDS AT 12D OF JOB VAC

W('07,2142', 0o77624, 'OPTAXIS', 'CALL', '', 'GO COMPUTE OA AN X AND Y PLANE VECS', kind='interp', line=172)
W('07,2143', 0o10536, '', '', 'OANB', kind='operand', line=173)
W('07,2144', 0o70535, '', 'SLOAD', 'SR1', 'LOAD APP ROTATION IN ONES COMP', kind='interp', line=174)
W('07,2145', 0o00013, '', '', '10D', 'RESCALE BY 2PI', kind='operand', line=175)
W('07,2146', 0o73406, '', 'PUSH', 'SIN', '1/2SIN(ROT) 0-1', kind='interp', line=176)
W('07,2147', 0o71525, '', 'PDDL', 'COS', kind='interp', line=177)
W('07,2150', 0o74206, '', 'PUSH', 'VXSC', '1/2COS(ROT) 2-3', kind='interp', line=178)
W('07,2151', 0o00023, '', '', '18D', kind='operand', line=179)
W('07,2152', 0o74325, '', 'PDDL', 'VXSC', '1/4COS(ROT)UYP 4-9', kind='interp', line=180)
W('07,2153', 0o00001, '', '', '0', kind='operand', line=181)
W('07,2154', 0o00031, '', '', '24D', '1/4SIN(ROT)UXP', kind='operand', line=182)
W('07,2155', 0o45445, '', 'BVSU', 'STADR', 'UP 4-9', kind='interp', line=183)
W('07,2156', 0o63762, '', 'STODL', '12D', 'YPNB=1/4(COS(ROT)UYP-SIN(ROT)UXP)', kind='interp', line=184)
W('07,2157', 0o65361, '', 'VXSC', 'PDDL', 'UP 2-3 UP 0-1 FOR EXCHANGE', kind='interp', line=185)
W('07,2160', 0o00031, '', '', '24D', '1/4COS(ROT)UXP        PUSH 0-5', kind='operand', line=186)
W('07,2161', 0o53361, '', 'VXSC', 'VAD', '1/4SIN(ROT)UYP', kind='interp', line=187)
W('07,2162', 0o00023, '', '', '18D', 'UP 0-5', kind='operand', line=188)
W('07,2163', 0o77626, '', 'STADR', kind='interp', line=189)
W('07,2164', 0o53754, '', 'STOVL', '18D', 'XPNB=1/4(COS(ROT)UXP+SIN(ROT)UYP)', kind='interp', line=190)
W('07,2165', 0o24007, '', '', 'LO6ZEROS', 'INITIALIZE AVE STAR VEC ACCUMULATOR', kind='operand', line=191)
W('07,2166', 0o02715, '', 'STORE', 'STARAD +6', kind='interp', line=192)
W('07,2167', 0o77776, '', 'EXIT', kind='interp', line=193)
W('07,2170', 0o12202, '', 'TCF', 'GETMKS', line=194)

# Page 249
# THE OANB SUBROUTINE COMPUTES THE OPTIC AXIS OF THE SIGHTING INSTRUMENT
# FROM AZIMUTH AND ELEVATION INPUT FROM THE ASTRONAUT.
#
# INPUT --        AZIMUTH ANGLE IN SINGLE PREC 2'S COMP IN 8D OF JOB VAC
# ELEVATION ANGLE IN SINGLE PREC 2'S COMP IN 9D OF VAC
#
# OUTPUT --       OPTIC AXIS IN NB COORDS. IN SCAXIS
# X-PLANE 1/2VEC IN NB COORDS AT 24D OF VAC
# Y-PLANE 1/2VEC IN NB COORDS AT 18D OF VAC

#   BANK 05
#   SETLOC AOTMARK2
#   BANK

#   COUNT* $$/MARK

W('04,2536', 0o44001, 'OANB', 'SETPD', 'STQ', kind='interp', line=213)
W('04,2537', 0o00001, '', '', '0', kind='operand', line=214)
W('04,2540', 0o02736, '', '', 'GCTR', 'STORE RETURN', kind='operand', line=215)
W('04,2541', 0o47135, '', 'SLOAD', 'RTB', kind='interp', line=216)
W('04,2542', 0o00012, '', '', '9D', 'PICK UP SP ELV', kind='operand', line=217)
W('04,2543', 0o21576, '', '', 'CDULOGIC', kind='operand', line=218)
W('04,2544', 0o71406, '', 'PUSH', 'COS', kind='interp', line=219)
W('04,2545', 0o73525, '', 'PDDL', 'SIN', '1/2COS(ELV)   PD 0-1', kind='interp', line=220)
W('04,2546', 0o77626, '', 'STADR', kind='interp', line=221)
W('04,2547', 0o60012, '', 'STODL', 'SCAXIS', 'OAX=1/2SIN(ELV)', kind='interp', line=222)
W('04,2550', 0o00011, '', '', '8D', kind='operand', line=223)
W('04,2551', 0o77634, '', 'RTB', kind='interp', line=224)
W('04,2552', 0o21576, '', '', 'CDULOGIC', kind='operand', line=225)
W('04,2553', 0o71406, '', 'PUSH', 'COS', kind='interp', line=226)
W('04,2554', 0o00025, '', 'STORE', '20D', 'STORE UYP(Y)  20-21', kind='interp', line=227)
W('04,2555', 0o73525, '', 'PDDL', 'SIN', '1/2COS(AZ)    PD 2-3', kind='interp', line=228)
W('04,2556', 0o57406, '', 'PUSH', 'DCOMP', 'PUSH 1/2S IN (AZ)     4-5', kind='interp', line=229)
W('04,2557', 0o14027, '', 'STODL', '22D', 'STORE UYP(Z)  22-23', kind='interp', line=230)
W('04,2560', 0o24007, '', '', 'LO6ZEROS', kind='operand', line=231)
W('04,2561', 0o14023, '', 'STODL', '18D', 'STORE UYP(X)  18-19', kind='interp', line=232)
W('04,2562', 0o72405, '', 'DMP', 'SL1', kind='interp', line=233)
W('04,2563', 0o00001, '', '', '0', kind='operand', line=234)
W('04,2564', 0o17767, '', 'STODL', 'SCAXIS +2', 'OAY=1/2COS(ELV)SIN(AZ)', kind='interp', line=235)
W('04,2565', 0o72405, '', 'DMP', 'SL1', 'UP    2-3', kind='interp', line=236)
W('04,2566', 0o77626, '', 'STADR', '', 'UP    0-1', kind='interp', line=237)
W('04,2567', 0o50006, '', 'STOVL', 'SCAXIS +4', 'OAZ=1/2COS(ELV)COS(AZ)', kind='interp', line=238)
W('04,2570', 0o00023, '', '', '18D', 'LOAD UYP VEC', kind='operand', line=239)
W('04,2571', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=240)
W('04,2572', 0o03765, '', '', 'SCAXIS', 'UXP VEC=UYP X OA', kind='operand', line=241)
W('04,2573', 0o00031, '', 'STORE', '24D', 'STORE UXP', kind='interp', line=242)
W('04,2574', 0o77650, '', 'GOTO', kind='interp', line=243)
W('04,2575', 0o02736, '', '', 'GCTR', kind='operand', line=244)
# Page 250
# SURFSTAR COMPUTES A STAR VECTOR IN SM COORDINATES FOR LUNAR
# SURFACE ALIGNMENT AND EXITS TO AVEIT TO AVERAGE STAR VECTORS.
#
# GIVEN   X-MARK PLANE 1/4 VEC IN NB AT 18D OF LOCAL VAC
# Y-MARK PLANE 1/4 VEC IN NB AT 12D OF LOCAL VAC
# CURSOR SP 2COMP AT POSITION 1 OF INDEXED MARKVAC
# SPIRAL SP 2COMP AT POSITION 3 OF INDEXED MARKVAC
# CDUY,Z,X AT POSITIONS 0,2,4 OF INDEXED MARKVAC

#   BANK 15
#   SETLOC P50S
#   BANK
#   COUNT* $$/R59

W('15,2000', 0o77773, 'SURFSTAR', 'VLOAD*', kind='interp', line=260)
W('15,2001', 0o00001, '', '', '0,1', 'PUT X-MARK CDUS IN CDUSPOT FOR TRG*NBSM', kind='operand', line=261)
W('15,2002', 0o00767, '', 'STORE', 'CDUSPOT', kind='interp', line=262)
W('15,2003', 0o47133, '', 'SLOAD*', 'RTB', kind='interp', line=263)
W('15,2004', 0o00002, '', '', '1,1', 'PICK UP YROT', kind='operand', line=264)
W('15,2005', 0o21576, '', '', 'CDULOGIC', kind='operand', line=265)
W('15,2006', 0o00031, '', 'STORE', '24D', 'STORE CURSOR FOR SPIRAL COMP (REVS)', kind='interp', line=266)
W('15,2007', 0o77654, '', 'BZE', kind='interp', line=267)
W('15,2010', 0o16171, '', '', 'YZCHK', 'IF YROT ZERO -- SEE IF SROT ZERO', kind='operand', line=268)
W('15,2011', 0o71406, 'JUSTZY', 'PUSH', 'COS', kind='interp', line=269)
W('15,2012', 0o73525, '', 'PDDL', 'SIN', '1/2COS(YROT)  0-1', kind='interp', line=270)
W('15,2013', 0o65361, '', 'VXSC', 'PDDL', 'UP 0-1        1/8SIN(YROT)UXP 0-5', kind='interp', line=271)
W('15,2014', 0o00023, '', '', '18D', kind='operand', line=272)
W('15,2015', 0o52361, '', 'VXSC', 'VSU', 'UP    0-5', kind='interp', line=273)
W('15,2016', 0o00015, '', '', '12D', 'UYP', kind='operand', line=274)
W('15,2017', 0o47256, '', 'UNIT', 'VXV', kind='interp', line=275)
W('15,2020', 0o03765, '', '', 'SCAXIS', kind='operand', line=276)
W('15,2021', 0o41456, '', 'UNIT', 'PUSH', kind='interp', line=277)
W('15,2022', 0o47133, '', 'SLOAD*', 'RTB', kind='interp', line=278)
W('15,2023', 0o00004, '', '', '3,1', 'PICK UP SPIRAL', kind='operand', line=279)
W('15,2024', 0o21576, '', '', 'CDULOGIC', kind='operand', line=280)
W('15,2025', 0o00033, '', 'STORE', '26D', 'STORE SPIRAL (REVS)', kind='interp', line=281)
W('15,2026', 0o43225, '', 'DSU', 'DAD', kind='interp', line=282)
W('15,2027', 0o00031, '', '', '24D', kind='operand', line=283)
W('15,2030', 0o32047, '', '', 'ABOUTONE', kind='operand', line=284)
W('15,2031', 0o77605, '', 'DMP', kind='interp', line=285)
W('15,2032', 0o32466, '', '', 'DP1/12', kind='operand', line=286)
W('15,2033', 0o00033, '', 'STORE', '26D', 'SEP=(360 + SPIRAL -CURSOR)/12', kind='interp', line=287)
W('15,2034', 0o74356, '', 'SIN', 'VXSC', 'UP    0-5', kind='interp', line=288)
W('15,2035', 0o65372, '', 'VSL1', 'PDDL', '1/2SIN(SEP)(UPP X OA) 0-5', kind='interp', line=289)
W('15,2036', 0o00033, '', '', '26D', kind='operand', line=290)
W('15,2037', 0o74346, '', 'COS', 'VXSC', kind='interp', line=291)
W('15,2040', 0o03765, '', '', 'SCAXIS', kind='operand', line=292)
W('15,2041', 0o53372, '', 'VSL1', 'VAD', 'UP    0-5', kind='interp', line=293)
W('15,2042', 0o45056, 'JUSTOA', 'UNIT', 'CALL', kind='interp', line=294)
W('15,2043', 0o47664, '', '', 'TRG*NBSM', kind='operand', line=295)
W('15,2044', 0o34031, '', 'STCALL', '24D', 'STAR VEC IN SM', kind='interp', line=296)
W('15,2045', 0o16276, '', '', 'AVEIT', 'GO AVERAGE', kind='operand', line=297)
# Page 251
W('15,2046', 0o37777, 'ABOUTONE', '2DEC', '.99999999', kind='data', line=299)
W('15,2047', 0o37775, kind='data', line=299)

S('DP1/12', 'equals', 0o42465, line=301)  # .08333333
#   BANK 7
#   SETLOC AOTMARK1
#   BANK
#   COUNT* $$/MARK
W('07,2171', 0o53133, 'YZCHK', 'SLOAD*', 'BZE', 'YROT ZERO AND IF SROT ZERO FORCE STAR', kind='interp', line=306)
W('07,2172', 0o00004, '', '', '3,1', 'ALONG OPTIC AXIS', kind='operand', line=307)
W('07,2173', 0o16177, '', '', 'YSZERO', kind='operand', line=308)
W('07,2174', 0o52145, '', 'DLOAD', 'GOTO', kind='interp', line=309)
W('07,2175', 0o00031, '', '', '24D', kind='operand', line=310)
W('07,2176', 0o32011, '', '', 'JUSTZY', 'SROT NOT ZERO -- CONTINUE NORMALLY', kind='operand', line=311)
W('07,2177', 0o52175, 'YSZERO', 'VLOAD', 'GOTO', kind='interp', line=312)
W('07,2200', 0o03765, '', '', 'SCAXIS', kind='operand', line=313)
W('07,2201', 0o32042, '', '', 'JUSTOA', kind='operand', line=314)

# Page 252
# THE GETMKS ROUTINE INITIALIZES THE SIGHTING MARK PROCEDURE

W('07,2202', 0o34755, 'GETMKS', 'CAF', 'ZERO', 'INITIALIZE MARK ID REGISTER AND MARK CNT', line=319)
W('07,2203', 0o55551, '', 'TS', 'XYMARK', line=320)
W('07,2204', 0o55550, '', 'TS', 'MARKCNTR', line=321)
W('07,2205', 0o35004, '', 'CAF', 'LOW9', 'ZERO BITS10 TO 15 RETAINING MKVAC ADR', line=322)
W('07,2206', 0o71312, '', 'MASK', 'MARKSTAT', line=323)
W('07,2207', 0o55312, '', 'TS', 'MARKSTAT', line=324)
W('07,2210', 0o32621, '', 'CAF', 'MKVB54*', 'DISPLAY VB54 INITIALLY', line=325)
W('07,2211', 0o04616, 'PASTIT', 'TC', 'BANKCALL', line=326)
W('07,2212', 0o20345, '', 'CADR', 'GOMARK4', kind='data', line=327)

W('07,2213', 0o12060, '', 'TCF', 'KILLAOT', 'V34 -- DOES GOTOPOOH', line=329)
W('07,2214', 0o12216, '', 'TCF', 'MARKCHEX', 'VB33 -- PROCEED, GOT MARKS, COMPUTE LOS', line=330)
W('07,2215', 0o12063, '', 'TCF', 'GETDAT', 'ENTER -- RECYCLE TO V01N71', line=331)

W('07,2216', 0o41312, 'MARKCHEX', 'CS', 'MARKSTAT', 'SET BIT12 TO DISCOURAGE MARKRUPT', line=333)
W('07,2217', 0o74740, '', 'MASK', 'BIT12', line=334)
W('07,2220', 0o27312, '', 'ADS', 'MARKSTAT', line=335)
W('07,2221', 0o75004, '', 'MASK', 'LOW9', line=336)
W('07,2222', 0o55551, '', 'TS', 'XYMARK', 'JAM MARK VAC ADR IN XYMARK FOR AVESTAR', line=337)
W('07,2223', 0o34755, '', 'CAF', 'ZERO', line=338)
W('07,2224', 0o55552, '', 'TS', 'MKDEX', 'SET MKDEX ZERO FOR LOS VEC CNTR', line=339)
W('07,2225', 0o31312, '', 'CA', 'MARKSTAT', line=340)
W('07,2226', 0o75015, '', 'MASK', 'PRIO3', 'SEE IF LAST MK PART COMPLETE', line=341)
W('07,2227', 0o54001, '', 'TS', 'L', line=342)
W('07,2230', 0o35015, '', 'CAF', 'PRIO3', 'BITS10 AND 11', line=343)
W('07,2231', 0o00006, '', 'EXTEND', line=344)
W('07,2232', 0o06001, '', 'RXOR', 'LCHAN', line=345)
W('07,2233', 0o00006, '', 'EXTEND', line=346)
W('07,2234', 0o12241, '', 'BZF', 'AVESTAR', 'LAST PAIR COMPLETE -- TO COMPUTE LOS', line=347)
W('07,2235', 0o11550, 'CNTCHK', 'CCS', 'MARKCNTR', 'NO PAIR SHOWING -- SEE IF PAIR IN HOLD', line=348)
W('07,2236', 0o12240, '', 'TCF', '+2', 'PAIR BURIED -- DECREMENT COUNTER', line=349)
W('07,2237', 0o12325, '', 'TCF', 'MKALARM', 'NO PAIR -- ALARM', line=350)
W('07,2240', 0o55550, '', 'TS', 'MARKCNTR', 'STORE DECREMENTED COUNTER', line=351)

W('07,2241', 0o34740, 'AVESTAR', 'CAF', 'BIT12', 'INITIALIZE MKDEX FOR STAR LOS COUNTER', line=353)
W('07,2242', 0o27552, '', 'ADS', 'MKDEX', 'MKDEX WAS INITIALIZED ZERO IN MARKCHEX', line=354)
W('07,2243', 0o41550, '', 'CS', 'MARKCNTR', line=355)
W('07,2244', 0o00006, '', 'EXTEND', line=356)
W('07,2245', 0o76242, '', 'MP', 'SIX', 'GET C(L) = -6 MARKCNTR', line=357)
W('07,2246', 0o41551, '', 'CS', 'XYMARK', line=358)
W('07,2247', 0o60001, '', 'AD', 'L', 'ADD -- MARK VAC ADR SET IN MARKCHEX', line=359)
W('07,2250', 0o50120, '', 'INDEX', 'FIXLOC', line=360)
W('07,2251', 0o54046, '', 'TS', 'X1', 'JAM -- CDU ADR OF X-MARK IN X1', line=361)

W('07,2252', 0o30120, '', 'CA', 'FIXLOC', 'SET PD POINTER TO ZERO', line=363)
W('07,2253', 0o54166, '', 'TS', 'PUSHLOC', line=364)

W('07,2254', 0o06037, '', 'TC', 'INTPRET', line=366)
# Page 253
W('07,2255', 0o76614, '', 'BON', 'VLOAD*', kind='interp', line=368)
W('07,2256', 0o04307, '', '', 'SURFFLAG', 'IF ON SURFACE COMPUTE VEC AT SURFSTAR', kind='operand', line=369)
W('07,2257', 0o32000, '', '', 'SURFSTAR', kind='operand', line=370)
W('07,2260', 0o00002, '', '', '1,1', 'PUT Y-MARK CDUS IN CDUSPOT FOR TRG*NBSM', kind='operand', line=371)
W('07,2261', 0o24767, '', 'STOVL', 'CDUSPOT', kind='interp', line=372)
W('07,2262', 0o00015, '', '', '12D', 'LOAD Y-PLANE VECTOR IN NG', kind='operand', line=373)
W('07,2263', 0o77624, '', 'CALL', kind='interp', line=374)
W('07,2264', 0o47664, '', '', 'TRG*NBSM', 'CONVERT IT TO STABLE MEMBER', kind='operand', line=375)
W('07,2265', 0o76606, '', 'PUSH', 'VLOAD*', kind='interp', line=376)
W('07,2266', 0o00001, '', '', '0,1', 'PUT X-MARK CDUS IN CDUSPOT FOR TRG*NBSM', kind='operand', line=377)
W('07,2267', 0o24767, '', 'STOVL', 'CDUSPOT', kind='interp', line=378)
W('07,2270', 0o00023, '', '', '18D', 'LOAD X-PLANE VECTOR IN NB', kind='operand', line=379)
W('07,2271', 0o77624, '', 'CALL', kind='interp', line=380)
W('07,2272', 0o47664, '', '', 'TRG*NBSM', 'CONVERT IT TO STABLE-MEMBER', kind='operand', line=381)
W('07,2273', 0o53435, '', 'VXV', 'UNIT', 'UNIT(XPSM * YPSM)', kind='interp', line=382)
W('07,2274', 0o77626, '', 'STADR', kind='interp', line=383)
W('07,2275', 0o77746, '', 'STORE', '24D', kind='interp', line=384)

W('07,2276', 0o63335, 'AVEIT', 'SLOAD', 'PDVL', 'N(NUMBER OF VECS) IN 0-1', kind='interp', line=386)
W('07,2277', 0o03553, '', '', 'MKDEX', kind='operand', line=387)
W('07,2300', 0o00031, '', '', '24D', 'LOAD CURRENT VECTOR', kind='operand', line=388)
W('07,2301', 0o70322, '', 'VSR3', 'V/SC', kind='interp', line=389)
W('07,2302', 0o00001, '', '', '0', kind='operand', line=390)
W('07,2303', 0o14031, '', 'STODL', '24D', 'VEC/N', kind='interp', line=391)
W('07,2304', 0o00001, '', '', '0', kind='operand', line=392)
W('07,2305', 0o56225, '', 'DSU', 'DDV', kind='interp', line=393)
W('07,2306', 0o16623, '', '', 'DP1/8', '(N-1)/N', kind='operand', line=394)
W('07,2307', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=395)
W('07,2310', 0o02715, '', '', 'STARAD +6', 'ADD VEC TO PREVIOUSLY AVERAGED VECTOR', kind='operand', line=396)
W('07,2311', 0o00031, '', '', '24D', '(N-1)/N AVESTVEC + VEC/N', kind='operand', line=397)
W('07,2312', 0o02715, '', 'STORE', 'STARAD +6', 'AVERAGE STAR VECTOR', kind='interp', line=398)
W('07,2313', 0o02767, '', 'STORE', 'STARSAV2', kind='interp', line=399)
W('07,2314', 0o77776, '', 'EXIT', kind='interp', line=400)
W('07,2315', 0o11550, '', 'CCS', 'MARKCNTR', 'SEE IF ANOTHER MARK PAIR IN MKVAC', line=401)
W('07,2316', 0o12240, '', 'TCF', 'AVESTAR -1', 'THERE IS -- GO GET IT -- DECREMENT COUNTER', line=402)
W('07,2317', 0o34756, 'ENDMARKS', 'CAF', 'FIVE', 'NO MORE MARKS -- TERMINATE AOTMARK', line=403)
W('07,2320', 0o00004, '', 'INHINT', line=404)
W('07,2321', 0o05203, '', 'TC', 'WAITLIST', line=405)
#   EBANK= XYMARK
W('07,2322', 0o02047, '', '2CADR', 'MKRELEAS', kind='data', line=407)
W('07,2323', 0o16067, kind='data', line=407)

W('07,2324', 0o05472, '', 'TC', 'ENDMARK', line=409)

W('07,2325', 0o05567, 'MKALARM', 'TC', 'ALARM', 'NOT A PAIR TO PROCESS -- DO GETMKS', line=411)
W('07,2326', 0o00111, '', 'OCT', '111', kind='data', line=412)
W('07,2327', 0o12202, '', 'TCF', 'GETMKS', line=413)

W('07,2330', 0o00307, 'V01N71', 'VN', '171', kind='data', line=415)
W('07,2331', 0o01527, 'V06N87*', 'VN', '687', kind='data', line=416)

# Page 254
# MARKRUPT IS ENTERED FROM INTERRUPT LEAD-INS AND PROCESSES CHANNEL 16
# CAUSED BY X,Y MARK OR MARK REJECT OR BY THE RATE OF DESCENT SWITCH

W('07,2332', 0o54016, 'MARKRUPT', 'TS', 'BANKRUPT', line=422)
W('07,2333', 0o30033, '', 'CA', 'CDUY', 'STORE CDUS AND TIME NOW -- THEN SEE IF', line=423)
W('07,2334', 0o54063, '', 'TS', 'ITEMP3', 'WE NEED THEM', line=424)
W('07,2335', 0o30034, '', 'CA', 'CDUZ', line=425)
W('07,2336', 0o54064, '', 'TS', 'ITEMP4', line=426)
W('07,2337', 0o30032, '', 'CA', 'CDUX', line=427)
W('07,2340', 0o54065, '', 'TS', 'ITEMP5', line=428)
W('07,2341', 0o00006, '', 'EXTEND', line=429)
W('07,2342', 0o30025, '', 'DCA', 'TIME2', line=430)
W('07,2343', 0o52062, '', 'DXCH', 'ITEMP1', line=431)
W('07,2344', 0o56002, '', 'XCH', 'Q', line=432)
W('07,2345', 0o54012, '', 'TS', 'QRUPT', line=433)

W('07,2346', 0o32624, '', 'CAF', 'OCT34', 'SEE IF X OR Y MARK OR MKREJECT', line=435)
W('07,2347', 0o00006, '', 'EXTEND', line=436)
W('07,2350', 0o02016, '', 'RAND', 'NAVKEYIN', line=437)
W('07,2351', 0o10000, '', 'CCS', 'A', line=438)
W('07,2352', 0o12354, '', 'TCF', '+2', 'ITS A LIVE ONE -- SEE IF ITS WANTED', line=439)
W('07,2353', 0o12404, '', 'TCF', 'SOMEKEY', 'ITS SOME OTHER KEY', line=440)

W('07,2354', 0o34740, '', 'CAF', 'BIT12', 'ARE WE ASKING FOR A MARK', line=442)
W('07,2355', 0o71312, '', 'MASK', 'MARKSTAT', line=443)
W('07,2356', 0o10000, '', 'CCS', 'A', line=444)
W('07,2357', 0o05270, '', 'TC', 'RESUME', "DON'T WANT MARK OR MKREJECT -- DO NOTHING", line=445)

W('07,2360', 0o11312, '', 'CCS', 'MARKSTAT', 'ARE MARKS BEING ACCEPTED', line=447)
W('07,2361', 0o12365, '', 'TCF', 'FINDKEY', 'THEY ARE -- WHICH ONE IS IT', line=448)
W('07,2362', 0o05567, '', 'TC', 'ALARM', 'MARKS NOT BEING ACCEPTED -- DO ALARM', line=449)
W('07,2363', 0o00112, '', 'OCT', '112', kind='data', line=450)
W('07,2364', 0o05270, '', 'TC', 'RESUME', line=451)

W('07,2365', 0o34747, 'FINDKEY', 'CAF', 'BIT5', 'SEE IF MARK REJECT.', line=453)
W('07,2366', 0o00006, '', 'EXTEND', line=454)
W('07,2367', 0o02016, '', 'RAND', 'NAVKEYIN', line=455)
W('07,2370', 0o10000, '', 'CCS', 'A', line=456)
W('07,2371', 0o12461, '', 'TCF', 'MKREJ', "IT'S A MARK REJECT", line=457)

W('07,2372', 0o34750, '', 'CAF', 'BIT4', 'SEE IF Y MARK', line=459)
W('07,2373', 0o00006, '', 'EXTEND', line=460)
W('07,2374', 0o02016, '', 'RAND', 'NAVKEYIN', line=461)
W('07,2375', 0o10000, '', 'CCS', 'A', line=462)

W('07,2376', 0o12422, '', 'TCF', 'YMKRUPT', "IT'S A Y MARK", line=464)

W('07,2377', 0o34751, '', 'CAF', 'BIT3', 'SEE IF X MARK', line=466)
W('07,2400', 0o00006, '', 'EXTEND', line=467)
W('07,2401', 0o02016, '', 'RAND', 'NAVKEYIN', line=468)

# Page 255
W('07,2402', 0o10000, '', 'CCS', 'A', line=471)
W('07,2403', 0o12416, '', 'TCF', 'XMKRUPT', "IT'S A X MARK", line=472)

W('07,2404', 0o34776, 'SOMEKEY', 'CAF', 'OCT140', 'NOT MARK OR MKREJECT -- SEE IF DESCENT BITS', line=474)
W('07,2405', 0o00006, '', 'EXTEND', line=475)
W('07,2406', 0o02016, '', 'RAND', 'NAVKEYIN', line=476)
W('07,2407', 0o00006, '', 'EXTEND', line=477)
W('07,2410', 0o12413, '', 'BZF', '+3', 'IF NO BITS', line=478)

W('07,2411', 0o04635, '', 'TC', 'POSTJUMP', 'IF DESCENT BITS', line=480)
W('07,2412', 0o40115, '', 'CADR', 'DESCBITS', kind='data', line=481)

W('07,2413', 0o05567, '', 'TC', 'ALARM', 'NO INBITS IN CHANNEL 16.', line=483)
W('07,2414', 0o00113, '', 'OCT', '113', kind='data', line=484)

W('07,2415', 0o05270, '', 'TC', 'RESUME', line=486)

W('07,2416', 0o34755, 'XMKRUPT', 'CAF', 'ZERO', line=488)
W('07,2417', 0o54070, '', 'TS', 'RUPTREG1', 'SET X MARK STORE INDEX TO ZERO', line=489)
W('07,2420', 0o34742, '', 'CAF', 'BIT10', line=490)
W('07,2421', 0o12425, '', 'TCF', '+4', line=491)
W('07,2422', 0o34753, 'YMKRUPT', 'CAF', 'ONE', line=492)
W('07,2423', 0o54070, '', 'TS', 'RUPTREG1', 'SET Y MARK STORE INDEX TO ONE', line=493)
W('07,2424', 0o34741, '', 'CAF', 'BIT11', line=494)
W('07,2425', 0o55551, '', 'TS', 'XYMARK', 'SET MARK IDENTIFICATION', line=495)

W('07,2426', 0o02514, '', 'TC', 'MARKTYPE', 'SEE IF SURFACE MARK', line=497)
W('07,2427', 0o12521, '', 'TCF', 'SURFSTOR', 'SURFACE MARK -- JUST STORE CDUS', line=498)

W('07,2430', 0o34736, '', 'CAF', 'BIT14', 'GOT A MARK -- SEE IF MARK PARI MADE', line=500)
W('07,2431', 0o71312, '', 'MASK', 'MARKSTAT', line=501)
W('07,2432', 0o00006, '', 'EXTEND', line=502)
W('07,2433', 0o12444, '', 'BZF', 'VERIFYMK', 'NOT A PAIR, NORMAL PROCEDURE', line=503)
W('07,2434', 0o41550, '', 'CS', 'MARKCNTR', 'GO A PAIR, SEE IF ANOTHER CAN BE MADE', line=504)
W('07,2435', 0o64751, '', 'AD', 'FOUR', 'IF SO, INCREMENT POINTER, CLEAR BITS 10,11', line=505)
W('07,2436', 0o00006, '', 'EXTEND', line=506)
W('07,2437', 0o62454, '', 'BZMF', '5MKALARM', "HAVE FIVE MARK PAIRS -- DON'T ALLOW MARK", line=507)
W('07,2440', 0o25550, '', 'INCR', 'MARKCNTR', 'OK FOR ANOTHER PAIR, INCR POINTER', line=508)
W('07,2441', 0o47711, '', 'CS', 'PRIO23', 'CLEAR BITS 10,11,14 FOR NEXT PAIR', line=509)
W('07,2442', 0o71312, '', 'MASK', 'MARKSTAT', line=510)
W('07,2443', 0o55312, '', 'TS', 'MARKSTAT', line=511)

W('07,2444', 0o31551, 'VERIFYMK', 'CA', 'XYMARK', line=513)
W('07,2445', 0o71312, '', 'MASK', 'MARKSTAT', line=514)
W('07,2446', 0o10000, '', 'CCS', 'A', line=515)
W('07,2447', 0o12451, '', 'TCF', '+2', 'THIS MARK NOT DESIRED', line=516)
W('07,2450', 0o12526, '', 'TCF', 'VACSTOR', 'MARK DESIRED -- STORE CDUS', line=517)
W('07,2451', 0o05567, '', 'TC', 'ALARM', line=518)
W('07,2452', 0o00114, '', 'OCT', '114', kind='data', line=519)
W('07,2453', 0o05270, '', 'TC', 'RESUME', 'RESUME -- DISPLAY UNCHANGED -- WAIT FOR ACTION', line=520)

# Page 256
W('07,2454', 0o05567, '5MKALARM', 'TC', 'ALARM', 'ATTEMPTING TO MAKE MORE THAN 5 MK PAIRS', line=523)
W('07,2455', 0o00107, '', 'OCT', '107', kind='data', line=524)
W('07,2456', 0o02514, '', 'TC', 'MARKTYPE', 'SEE IF SURFACE MARK', line=525)
W('07,2457', 0o12627, '', 'TCF', 'DSPV6N79', 'IT IS', line=526)
W('07,2460', 0o05270, '', 'TC', 'RESUME', "DON'T CHANGE DISPLAY -- DO NOTHING", line=527)

# Page 257
W('07,2461', 0o02514, 'MKREJ', 'TC', 'MARKTYPE', 'SEE IF SURFACE', line=530)
W('07,2462', 0o12507, '', 'TCF', 'SURFREJ', 'SURFACE -- JUST CHECK MARK COUNTER', line=531)

W('07,2463', 0o35015, '', 'CAF', 'PRIO3', 'INFLIGHT -- SEE IF MARKS MADE', line=533)
W('07,2464', 0o71312, '', 'MASK', 'MARKSTAT', line=534)
W('07,2465', 0o10000, '', 'CCS', 'A', line=535)
W('07,2466', 0o12472, '', 'TCF', 'REJECT', 'MARKS MADE -- REJECT ONE', line=536)
W('07,2467', 0o05567, 'REJALM', 'TC', 'ALARM', 'NO MARK TO REJECT -- BAD PROCEDURE -- ALARM', line=537)
W('07,2470', 0o00115, '', 'OCT', '115', kind='data', line=538)
W('07,2471', 0o05270, '', 'TC', 'RESUME', 'DESIRED ACTION DISPLAYED', line=539)

W('07,2472', 0o44355, 'REJECT', 'CS', 'PRIO30', 'ZERO BIT14, SHOW REJ., SEE IF MARK SINCE', line=541)
W('07,2473', 0o71312, '', 'MASK', 'MARKSTAT', 'LAST REJECT', line=542)
W('07,2474', 0o64737, '', 'AD', 'BIT13', line=543)
W('07,2475', 0o57312, '', 'XCH', 'MARKSTAT', line=544)
W('07,2476', 0o74737, '', 'MASK', 'BIT13', line=545)
W('07,2477', 0o10000, '', 'CCS', 'A', line=546)
W('07,2500', 0o12505, '', 'TCF', 'REJECT2', 'ANOTHER REJECT SET BIT 10+11 TO ZERO', line=547)

W('07,2501', 0o41551, '', 'CS', 'XYMARK', 'MARK MADE SINCE REJECT -- REJECT MARK IN 1D', line=549)
W('07,2502', 0o71312, 'RENEWMK', 'MASK', 'MARKSTAT', line=550)
W('07,2503', 0o55312, '', 'TS', 'MARKSTAT', line=551)
W('07,2504', 0o12577, '', 'TCF', 'REMARK', 'GO REQUEST NEW MARK ACTION', line=552)

W('07,2505', 0o45015, 'REJECT2', 'CS', 'PRIO3', 'ON SECOND REJECT -- DISPLAY VB53 AGAIN', line=554)
W('07,2506', 0o12502, '', 'TCF', 'RENEWMK', line=555)

W('07,2507', 0o11550, 'SURFREJ', 'CCS', 'MARKCNTR', 'IF MARK DECREMENT COUNTER', line=557)
W('07,2510', 0o12512, '', 'TCF', '+2', line=558)
W('07,2511', 0o12467, '', 'TCF', 'REJALM', 'NO MARKS TO REJECT -- ALARM', line=559)
W('07,2512', 0o55550, '', 'TS', 'MARKCNTR', line=560)
W('07,2513', 0o05270, '', 'TC', 'RESUME', line=561)

# Page 258
# MARKTYPE TESTS TO SEE IF LEM ON LUNAR SURFACE.  IF IT IS RETURN TO LOC+1

W('07,2514', 0o40104, 'MARKTYPE', 'CS', 'FLAGWRD8', 'SURFFLAG ******** TEMPORARY ******', line=566)
W('07,2515', 0o74744, '', 'MASK', 'BIT8', line=567)
W('07,2516', 0o10000, '', 'CCS', 'A', line=568)
W('07,2517', 0o24002, '', 'INCR', 'Q', 'IF SURFACE MARK RETURN TO LOC +1', line=569)
W('07,2520', 0o00002, '', 'TC', 'Q', 'IF INFLIGHT MARK RETURN TO LOC +2', line=570)

W('07,2521', 0o34755, 'SURFSTOR', 'CAF', 'ZERO', 'FOR SURFACE MARK ZERO MARK KIND INDEX', line=572)
W('07,2522', 0o54070, '', 'TS', 'RUPTREG1', line=573)

W('07,2523', 0o41312, '', 'CS', 'MARKSTAT', 'SET BITS10,11 TO SHOW SURFACE MARK', line=575)
W('07,2524', 0o75015, '', 'MASK', 'PRIO3', 'FOR MARKCHEX', line=576)
W('07,2525', 0o27312, '', 'ADS', 'MARKSTAT', line=577)

W('07,2526', 0o35004, 'VACSTOR', 'CAF', 'LOW9', line=579)
W('07,2527', 0o71312, '', 'MASK', 'MARKSTAT', 'STORE MARK VAC ADR IN RUPTREG2', line=580)
W('07,2530', 0o54071, '', 'TS', 'RUPTREG2', line=581)
W('07,2531', 0o00006, '', 'EXTEND', line=582)
W('07,2532', 0o30062, '', 'DCA', 'ITEMP1', 'PICK UP MARKTIME', line=583)
W('07,2533', 0o53562, '', 'DXCH', 'TSIGHT', 'STORE LAST MARK TIME', line=584)
W('07,2534', 0o31550, '', 'CA', 'MARKCNTR', '6 X MARKCNTR FOR STORE INDEX', line=585)
W('07,2535', 0o00006, '', 'EXTEND', line=586)
W('07,2536', 0o76242, '', 'MP', 'SIX', line=587)
W('07,2537', 0o56001, '', 'XCH', 'L', 'GET INDEX FROM LOW ORDER PART', line=588)
W('07,2540', 0o60071, '', 'AD', 'RUPTREG2', 'SET CDU STORE INDEX TO MARKVAC', line=589)
W('07,2541', 0o26070, '', 'ADS', 'RUPTREG1', 'INCREMENT VAC PICKUP BY MARK FOR FLIGHT', line=590)
W('07,2542', 0o55552, '', 'TS', 'MKDEX', 'STORE HERE IN CASE OF SURFACE MARK', line=591)
W('07,2543', 0o30063, '', 'CA', 'ITEMP3', line=592)
W('07,2544', 0o50070, '', 'INDEX', 'RUPTREG1', line=593)
W('07,2545', 0o54000, '', 'TS', '0', 'STORE CDUY', line=594)
W('07,2546', 0o30064, '', 'CA', 'ITEMP4', line=595)
W('07,2547', 0o50070, '', 'INDEX', 'RUPTREG1', line=596)
W('07,2550', 0o54002, '', 'TS', '2', 'STORE CDUZ', line=597)
W('07,2551', 0o30065, '', 'CA', 'ITEMP5', line=598)
W('07,2552', 0o50070, '', 'INDEX', 'RUPTREG1', line=599)
W('07,2553', 0o54004, '', 'TS', '4', 'STORE CDUX', line=600)
W('07,2554', 0o02514, '', 'TC', 'MARKTYPE', 'IF SURFACE MARK -- JUST DO SURFJOB', line=601)
W('07,2555', 0o12604, '', 'TCF', 'SURFJOB', line=602)

W('07,2556', 0o34737, '', 'CAF', 'BIT13', 'CLEAR BIT13 TO SHOW MARK MADE', line=604)
W('07,2557', 0o61551, '', 'AD', 'XYMARK', 'SET MARK ID IN MARKSTAT', line=605)
W('07,2560', 0o40000, '', 'COM', line=606)
W('07,2561', 0o71312, '', 'MASK', 'MARKSTAT', line=607)
W('07,2562', 0o61551, '', 'AD', 'XYMARK', line=608)
W('07,2563', 0o55312, '', 'TS', 'MARKSTAT', line=609)
W('07,2564', 0o75015, '', 'MASK', 'PRIO3', 'SEE IF X, Y MARK MADE', line=610)
W('07,2565', 0o54001, '', 'TS', 'L', line=611)

# Page 259
W('07,2566', 0o35015, '', 'CA', 'PRIO3', line=614)
W('07,2567', 0o00006, '', 'EXTEND', line=615)
W('07,2570', 0o06001, '', 'RXOR', 'LCHAN', line=616)
W('07,2571', 0o10000, '', 'CCS', 'A', line=617)
W('07,2572', 0o12577, '', 'TCF', 'REMARK', 'NOT PAIR YET, DISPLAY MARK ACTION', line=618)
W('07,2573', 0o41312, '', 'CS', 'MARKSTAT', 'MARK PAIR COMPLETE -- SET BIT14', line=619)
W('07,2574', 0o74736, '', 'MASK', 'BIT14', line=620)
W('07,2575', 0o27312, '', 'ADS', 'MARKSTAT', line=621)
W('07,2576', 0o12577, '', 'TCF', 'REMARK', 'GO DISPLAY V54', line=622)

# Page 260
W('07,2577', 0o35015, 'REMARK', 'CAF', 'PRIO3', 'BITS 10 AND 11', line=625)
W('07,2600', 0o71312, '', 'MASK', 'MARKSTAT', line=626)
W('07,2601', 0o00006, '', 'EXTEND', line=627)
W('07,2602', 0o74746, '', 'MP', 'BIT6', 'SHIFT MARK IDS TO BE 0 TO 3 FOR INDEX', line=628)
W('07,2603', 0o55552, '', 'TS', 'MKDEX', 'STORE VERB INDEX', line=629)
W('07,2604', 0o35025, 'SURFJOB', 'CAF', 'PRIO15', line=630)
W('07,2605', 0o05072, '', 'TC', 'NOVAC', 'ENTER JOB TO CHANGE DISPLAY TO', line=631)
#   EBANK= XYMARK  # REQUEST NEXT ACTION
W('07,2606', 0o02611, '', '2CADR', 'CHANGEVB', kind='data', line=633)
W('07,2607', 0o16067, kind='data', line=633)

W('07,2610', 0o05270, '', 'TC', 'RESUME', line=635)

W('07,2611', 0o02514, 'CHANGEVB', 'TC', 'MARKTYPE', line=637)
W('07,2612', 0o12627, '', 'TCF', 'DSPV6N79', 'SURFACE -- DISPLAY V 06 N 79', line=638)
W('07,2613', 0o51552, '', 'INDEX', 'MKDEX', 'INFLIGHT -- PICK UP MARK VB INDEX', line=639)
W('07,2614', 0o32616, '', 'CAF', 'MKVB54', line=640)
W('07,2615', 0o02211, '', 'TC', 'PASTIT', 'PASTE UP NEXT MK VERB DISPLAY', line=641)

# THE FOUR MKVBS ARE INDEXED -- THEIR ORDER CANNOT BE CHANGED

W('07,2616', 0o15507, 'MKVB54', 'VN', '5471', 'MAKE X OR Y MARK', kind='data', line=645)
W('07,2617', 0o15307, 'MKVB53', 'VN', '5371', 'MAKE Y MARK', kind='data', line=646)
W('07,2620', 0o15107, 'MKVB52', 'VN', '5271', 'MAKE X MARK', kind='data', line=647)
W('07,2621', 0o15507, 'MKVB54*', 'VN', '5471', 'MAKE X OR Y MARK', kind='data', line=648)
W('07,2622', 0o04000, 'DP1/8', '2DEC', '.125', kind='data', line=649)
W('07,2623', 0o00000, kind='data', line=649)

W('07,2624', 0o00034, 'OCT34', 'OCT', '34', kind='data', line=651)
W('07,2625', 0o01507, 'V06N71', 'VN', '671', kind='data', line=652)
W('07,2626', 0o01517, 'V06N79*', 'VN', '679', kind='data', line=653)

# Page 261
# ROUTINE TO REQUEST CURSOR AND SPIRAL MEASUREMENTS
#   COUNT* $$/R59

W('07,2627', 0o32626, 'DSPV6N79', 'CAF', 'V06N79*', 'CURSOR -- SPIRAL DISPLAY', line=659)
W('07,2630', 0o04616, '', 'TC', 'BANKCALL', line=660)
W('07,2631', 0o20334, '', 'CADR', 'GOMARKF', kind='data', line=661)

W('07,2632', 0o12060, '', 'TCF', 'KILLAOT', 'V34 -- DOES GOTOPOOH', line=663)
W('07,2633', 0o12641, '', 'TCF', 'SURFEND', 'V33 -- PROCEED, END MARKING', line=664)
W('07,2634', 0o34746, '', 'CAF', 'BIT6', 'IF V32(OCT40) IN MPAC DO RECYCLE', line=665)
W('07,2635', 0o70154, '', 'MASK', 'MPAC', 'OTHERWISE IT IS LOAD VB ENTER SO', line=666)
W('07,2636', 0o10000, '', 'CCS', 'A', 'RE-DISPLAY V06N79', line=667)
W('07,2637', 0o12645, '', 'TCF', 'SURFAGAN', 'VB32 -- RECYCLE', line=668)
W('07,2640', 0o12627, '', 'TCF', 'DSPV6N79', 'ENTER', line=669)

W('07,2641', 0o44736, 'SURFEND', 'CS', 'BIT14', 'SET BIT14 TO SHOW MARK END', line=671)
W('07,2642', 0o71312, '', 'MASK', 'MARKSTAT', line=672)
W('07,2643', 0o64736, '', 'AD', 'BIT14', line=673)
W('07,2644', 0o55312, '', 'TS', 'MARKSTAT', line=674)

W('07,2645', 0o31236, 'SURFAGAN', 'CA', 'CURSOR', line=676)
W('07,2646', 0o51552, '', 'INDEX', 'MKDEX', 'HOLDS VAC AREA POINTER FOR SURF MARKING', line=677)
W('07,2647', 0o54001, '', 'TS', '1', 'STORE CURSOR SP 2COMP', line=678)
W('07,2650', 0o31240, '', 'CA', 'SPIRAL', line=679)
W('07,2651', 0o51552, '', 'INDEX', 'MKDEX', line=680)
W('07,2652', 0o54003, '', 'TS', '3', 'STORE SPIRAL', line=681)

W('07,2653', 0o41312, '', 'CS', 'MARKSTAT', 'IF BIT 14 SET -- END MARKING', line=683)
W('07,2654', 0o74736, '', 'MASK', 'BIT14', line=684)
W('07,2655', 0o00006, '', 'EXTEND', line=685)
W('07,2656', 0o12216, '', 'BZF', 'MARKCHEX', line=686)
W('07,2657', 0o31550, '', 'CA', 'MARKCNTR', 'THIS IS RECYCLE -- SEE IF 5 MARKS ALREADY', line=687)
W('07,2660', 0o64753, '', 'AD', 'ONE', line=688)
W('07,2661', 0o40000, '', 'COM', line=689)
W('07,2662', 0o64756, '', 'AD', 'FIVE', line=690)
W('07,2663', 0o00006, '', 'EXTEND', line=691)
W('07,2664', 0o62454, '', 'BZMF', '5MKALARM', "CAN'T RECYCLE -- TOO MANY MARKS -- ALARM", line=692)
W('07,2665', 0o25550, '', 'INCR', 'MARKCNTR', 'OF FOR RECYCLE -- INCR COUNTER', line=693)
W('07,2666', 0o12205, '', 'TCF', 'GETMKS +3', 'GO DISPLAY MARK VB', line=694)
