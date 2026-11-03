"""EXTENDED_VERBS.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/EXTENDED_VERBS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 262-300 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('EXTENDED_VERBS', 'EXTENDED_VERBS.agc', 'Luminary099', pages='262-300')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     EXTENDED_VERBS.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        262-300
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Luminary131/ file of the same
# name, using Luminary099 page images.
# 2009-06-05 RSB  Corrected 5 typos.
# 2009-06-06 RSB  Eliminated an extraneous 3-instruction block
# and added a missing instruction.
# 2009-06-07 RSB  Added a couple of "SBANK=" for compatibility
# with yaYUL. Corrected a typo.
# 2010-12-31 JL   Fixed page number comments.
# 2011-01-06 JL   Added missing comment characters.
# 2011-05-08 JL   Flagged SBANK= workarounds for future removal.

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

# Page 262
#   BANK 7
#   SETLOC EXTVERBS
#   BANK

#   EBANK= OGC

#   COUNT* $$/EXTVB

# FAN-OUT

W('43,2000', 0o50154, 'GOEXTVB', 'INDEX', 'MPAC', 'VERB-40 IS IN MPAC', line=48)
W('43,2001', 0o02002, '', 'TC', 'LST2FAN', 'FAN AS BEFORE.', line=49)

W('43,2002', 0o02130, 'LST2FAN', 'TC', 'VBZERO', 'VB40 ZERO (USED WITH NOUN 20 OR 72 ONLY)', line=51)
W('43,2003', 0o02171, '', 'TC', 'VBCOARK', 'VB41 COARSE ALIGN (USED WITH NOUN 20 OR', line=52)
# 72 ONLY)
W('43,2004', 0o02330, '', 'TC', 'IMUFINEK', 'VB42 FINE ALIGN IMU', line=54)
W('43,2005', 0o02707, '', 'TC', 'IMUATTCK', 'VB43 LOAD IMU ATTITUDE ERROR METERS.', line=55)
W('43,2006', 0o02302, '', 'TC', 'RRDESEND', 'VB44 TERMINATE CONTINUOUS DESIGNATE', line=56)
W('43,2007', 0o02120, '', 'TC', 'ALM/END', 'VB45 SPARE', line=57)
W('43,2010', 0o02120, '', 'TC', 'ALM/END', 'VB46 SPARE', line=58)
W('43,2011', 0o02367, '', 'TC', 'V47TXACT', 'VB47 AGS INITIALIZATION', line=59)
W('43,2012', 0o03135, '', 'TC', 'DAPDISP', 'VB48 LOAD A/P DATA', line=60)
W('43,2013', 0o13015, '', 'TCF', 'CREWMANU', 'VB49 START AUTOMATIC ATTITUDE MANEUVER', line=61)
W('43,2014', 0o02361, '', 'TC', 'GOLOADLV', 'VB50 PLEASE PERFORM', line=62)
W('43,2015', 0o02120, '', 'TC', 'ALM/END', 'VB51 SPARE', line=63)
W('43,2016', 0o02361, '', 'TC', 'GOLOADLV', 'VB52 PLEASE MARK X -- RETICLE.', line=64)
W('43,2017', 0o02361, '', 'TC', 'GOLOADLV', 'VB53 PLEASE MARK Y -- RETICLE.', line=65)
W('43,2020', 0o02361, '', 'TC', 'GOLOADLV', 'VB54 PLEASE MARK X OR Y RETICLE', line=66)
W('43,2021', 0o02401, '', 'TC', 'ALINTIME', 'VB55 ALIGN TIME', line=67)
W('43,2022', 0o03024, '', 'TC', 'TRMTRACK', 'VB56 TERMINATE TRACKING -- P20 + P25', line=68)
W('43,2023', 0o02322, '', 'TC', 'LRON', 'VB57 PERMIT LANDING RADAR UPDATES', line=69)
W('43,2024', 0o02325, '', 'TC', 'LROFF', 'VB58 INHIBIT LANDING RADAR UPDATES', line=70)
W('43,2025', 0o02120, '', 'TC', 'ALM/END', 'VB59 SPARE', line=71)
W('43,2026', 0o02151, '', 'TC', 'LRPOS2K', 'VB60 COMMAND LR TO POSITION 2.', line=72)
W('43,2027', 0o02163, '', 'TC', 'DAPATTER', 'VB61 DISPLAY DAP ATTITUDE ERROR', line=73)
W('43,2030', 0o02166, '', 'TC', 'TOTATTER', 'VB62 DISPLAY TOTAL ATTITUDE ERROR', line=74)
W('43,2031', 0o02414, '', 'TC', 'R04', 'VB63 SAMPLE RADAR ONCE PER SECOND', line=75)
W('43,2032', 0o02700, '', 'TC', 'VB64', 'VB64 CALCULATE, DISPLAY S-BAND ANT ANGLES', line=76)
W('43,2033', 0o03221, '', 'TC', 'SNUFFOUT', 'VB65 DISABLE U,V JETS DURING DPS BURNS.', line=77)
W('43,2034', 0o03142, '', 'TC', 'ATTACHED', 'VB66 ATTACHED   MOVE THIS TO OTHER STATE', line=78)
W('43,2035', 0o03213, '', 'TC', 'V67', 'VB67 W MATRIX MONITOR', line=79)
W('43,2036', 0o02120, '', 'TC', 'ALM/END', 'VB68 SPARE', line=80)
W('43,2037', 0o02037, 'VERB69', 'TC', 'VERB69', 'VB69 FORCE A HARDWARE RESTART', line=81)
W('43,2040', 0o03724, '', 'TC', 'V70UPDAT', 'VB70 UPDATE LIFTOFF TIME.', line=82)
W('43,2041', 0o03726, '', 'TC', 'V71UPDAT', 'VB71 UNIVERSAL UPDATE -- BLOCK ADDRESS.', line=83)
W('43,2042', 0o03730, '', 'TC', 'V72UPDAT', 'VB72 UNIVERSAL UPDATE -- SINGLE ADDRESS.', line=84)
W('43,2043', 0o03732, '', 'TC', 'V73UPDAT', 'VB73 UPDATE AGC TIME (OCTAL).', line=85)
W('43,2044', 0o03045, '', 'TC', 'DNEDUMP', 'VB74 INITIALIZE DOWN-TELEMETRY PROGRAM', line=86)
# FOR ERASABLE DUMP.
W('43,2045', 0o03224, '', 'TC', 'OUTSNUFF', 'VB75 ENABLE U,V JETS DURING DPS BURNS.', line=88)
# Page 263
W('43,2046', 0o03001, '', 'TC', 'MINIMP', 'VB76 MINIMUM IMPULSE MODE', line=90)
W('43,2047', 0o03006, '', 'TC', 'NOMINIMP', 'VB77 RATE COMMAND MODE', line=91)
W('43,2050', 0o02404, '', 'TC', 'R77', 'VB78 START LR SPURIOUS RETURN TEST', line=92)
W('43,2051', 0o02617, '', 'TC', 'R77END', 'VB79 TERMINATE LR SPURIOUS RETURN TEST', line=93)
W('43,2052', 0o03051, '', 'TC', 'LEMVEC', 'VB80 UPDATE LEM STATE VECTOR', line=94)
W('43,2053', 0o03054, '', 'TC', 'CSMVEC', 'VB81 UPDATE CSM STATE VECTOR', line=95)
W('43,2054', 0o02746, '', 'TC', 'V82PERF', 'VB82 REQUEST ORBIT PARAM DISPLAY (R30)', line=96)
W('43,2055', 0o02756, '', 'TC', 'V83PERF', 'VB83 REQUEST REND PARAM DISPLAY (R31)', line=97)
W('43,2056', 0o02120, '', 'TC', 'ALM/END', 'VB84 SPARE', line=98)
W('43,2057', 0o03227, '', 'TC', 'VERB85', 'VB85 DISPLAY RR LOS AZ AND ELEV', line=99)
W('43,2060', 0o02120, '', 'TC', 'ALM/END', 'VB86 SPARE', line=100)
W('43,2061', 0o02120, '', 'TC', 'ALM/END', 'VB87 SPARE', line=101)
W('43,2062', 0o02120, '', 'TC', 'ALM/END', 'VB88 SPARE', line=102)
W('43,2063', 0o02764, '', 'TC', 'V89PERF', 'VB89 ALIGN XORZ LEM AXIS ALONG LOS (R63)', line=103)
W('43,2064', 0o02773, '', 'TC', 'V90PERF', 'VB90 OUT OF PLANE RENDEZVOUS DISPLAY', line=104)
W('43,2065', 0o03100, '', 'TC', 'GOSHOSUM', 'VB91 DISPLAY BANK SUM.', line=105)
W('43,2066', 0o03064, '', 'TC', 'SYSTEST', 'VB92 OPERAT IMU PERFORMANCE TEST.', line=106)
W('43,2067', 0o03073, '', 'TC', 'WMATRXNG', 'VB93 CLEAR RENDWFLG', line=107)
W('43,2070', 0o02120, '', 'TC', 'ALM/END', 'VB94 SPARE', line=108)
W('43,2071', 0o03061, '', 'TC', 'UPDATOFF', 'VB95 NO STATE VECTOR UPDATE ALLOWED', line=109)
W('43,2072', 0o03206, '', 'TC', 'VERB96', 'VB96 INTERRUPT INTEGRATION AND GO TO P00', line=110)
W('43,2073', 0o02361, '', 'TC', 'GOLOADLV', 'VB97 PLEASE VERIFY ENGINE FAILURE', line=111)
W('43,2074', 0o02120, '', 'TC', 'ALM/END', 'VB98 SPARE', line=112)
W('43,2075', 0o02361, '', 'TC', 'GOLOADLV', 'VB99 PLEASE ENABLE ENGINE', line=113)

# END OF EXTENDED VERB FAN

W('43,2076', 0o11044, 'TESTXACT', 'CCS', 'EXTVBACT', 'ARE EXTENDED VERBS BUSY', line=117)
W('43,2077', 0o02120, '', 'TC', 'ALM/END', 'YES, TURN ON OPERATOR LIGHT', line=118)
W('43,2100', 0o30100, '', 'CA', 'FLAGWRD4', 'ARE PRIORITY DISPLAYS USING DSKY', line=119)
W('43,2101', 0o72127, '', 'MASK', 'OC24100', line=120)
W('43,2102', 0o10000, '', 'CCS', 'A', line=121)
W('43,2103', 0o02120, '', 'TC', 'ALM/END', 'YES', line=122)
W('43,2104', 0o36007, '', 'CAF', 'OCT24', 'SET BITS 3 AND 5', line=123)
W('43,2105', 0o55044, 'SETXTACT', 'TS', 'EXTVBACT', 'NO.  SET FLAG TO SHOW EXT VERB DISPLAY', line=124)
# SYSTEM BUSY

W('43,2106', 0o30002, '', 'CA', 'Q', line=127)
W('43,2107', 0o54155, '', 'TS', 'MPAC +1', line=128)

W('43,2110', 0o44752, '', 'CS', 'TWO', 'BLANK EVERYTHING EXCEPT MM AND VERB', line=130)
W('43,2111', 0o04154, '', 'TC', 'NVSUB', line=131)
W('43,2112', 0o02113, '', 'TC', '+1', line=132)
W('43,2113', 0o00155, '', 'TC', 'MPAC +1', line=133)

W('43,2114', 0o04364, 'XACTALM', 'TC', 'FALTON', 'TURN ON OPERATOR ERROR LIGHT.', line=135)
W('43,2115', 0o05472, '', 'TC', 'ENDEXT', 'RELEASE MARK AND EXT. VERB DISPLAY SYS.', line=136)

S('TERMEXTV', 'equals', 0o5472, line=138)
# Page 264
S('ENDEXTVB', 'equals', 0o5472, line=140)

W('43,2116', 0o34755, 'XACT0', 'CAF', 'ZERO', 'RELEASE MARK AND EXT. VERB DISPLAY SYS.', line=142)
W('43,2117', 0o02105, '', 'TC', 'SETXTACT', line=143)

W('43,2120', 0o04364, 'ALM/END', 'TC', 'FALTON', 'TURN ON OPERATOR ERROR LIGHT', line=145)
W('43,2121', 0o04635, 'GOPIN', 'TC', 'POSTJUMP', line=146)
W('43,2122', 0o21050, '', 'CADR', 'PINBRNCH', kind='data', line=147)

W('43,2123', 0o31011, 'CHKPOOH', 'CA', 'MODREG', 'CHECK FOR P00 OR P00-.', line=149)
W('43,2124', 0o00006, '', 'EXTEND', line=150)
W('43,2125', 0o16742, '', 'BZF', 'TCQ', line=151)
W('43,2126', 0o02120, '', 'TC', 'ALM/END', line=152)

W('43,2127', 0o24100, 'OC24100', 'OCT', '24100', kind='data', line=154)

# Page 265
# VBZERO        VERB 40         DESCRIPTION
#
# 1.      REQUIRE NOUN 20 (ICDU ANGLES) OR NOUN 72 (RCDU ANGLES).
# 2.      FOR N20, CHECK IMUCADR IN AN EFFORT TO AVOID A 1210 RESTART.
# FOR N72, CHECK IF EITHER RADAR IS IN USE.
# 3.      EXECUTE THE CDU ZERO.
# 4.      STALL UNTILL THE ZERO IS DONE.
# 5.      DON'T DIFFERENTIATE BETWEEN A BAD OR GOOD RETURN.
# 6.      EXIT, RE-ESTABLISHING THE INTERRUPTED DISPLAY (IF ANY).

W('43,2130', 0o02174, 'VBZERO', 'TC', 'OP/INERT', line=167)
W('43,2131', 0o02133, '', 'TC', 'IMUZEROK', 'RETURN HERE IF NOUN = ICDU(20)', line=168)
W('43,2132', 0o02142, '', 'TC', 'RRZEROK', 'RETURN HERE IF NOUN = RCDU(72)', line=169)
W('43,2133', 0o02375, 'IMUZEROK', 'TC', 'CKMODCAD', line=170)
W('43,2134', 0o04616, '', 'TC', 'BANKCALL', 'KEYBOARD REQ FOR ISS CDUZERO', line=171)
W('43,2135', 0o16714, '', 'CADR', 'IMUZERO', kind='data', line=172)

W('43,2136', 0o04616, '', 'TC', 'BANKCALL', 'STALL', line=174)
W('43,2137', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=175)
W('43,2140', 0o02141, '', 'TC', '+1', line=176)

W('43,2141', 0o02121, '', 'TC', 'GOPIN', 'IMUZERO', line=178)

W('43,2142', 0o02642, 'RRZEROK', 'TC', 'RDRUSECK', line=180)
W('43,2143', 0o04616, '', 'TC', 'BANKCALL', line=181)
W('43,2144', 0o52343, '', 'CADR', 'RRZERO', kind='data', line=182)

W('43,2145', 0o04616, 'RWAITK', 'TC', 'BANKCALL', line=184)
W('43,2146', 0o17714, '', 'CADR', 'RADSTALL', kind='data', line=185)
W('43,2147', 0o12150, '', 'TCF', '+1', line=186)
W('43,2150', 0o02121, '', 'TC', 'GOPIN', 'RRZERO', line=187)

# LRPOS2K       VERB 60                 DESCRIPTION
# COMMAND LANDING RADAR TO POSITION 2
#
# 1.      EXIT WITH OP ERROR IF SOMEONE IS USING EITHER RADAR.
# 2.      ALARM WITH CODE 523 IF POS 2 IS NOT INDICATED WITHIN
# THE PRESCRIBED TIME.
# 3.      RE-ESTABLISH THE DISPLAYS.

W('43,2151', 0o02642, 'LRPOS2K', 'TC', 'RDRUSECK', line=197)
W('43,2152', 0o04616, '', 'TC', 'BANKCALL', 'COMMAND LR TO POSITION 2', line=198)
W('43,2153', 0o53471, '', 'CADR', 'LRPOS2', kind='data', line=199)
W('43,2154', 0o04616, '', 'TC', 'BANKCALL', line=200)
W('43,2155', 0o17714, '', 'CADR', 'RADSTALL', kind='data', line=201)
W('43,2156', 0o02160, '', 'TC', 'LRP2ALM', line=202)
W('43,2157', 0o02121, '', 'TC', 'GOPIN', line=203)

W('43,2160', 0o05567, 'LRP2ALM', 'TC', 'ALARM', line=205)
W('43,2161', 0o00523, '', 'OCT', '523', kind='data', line=206)
W('43,2162', 0o02121, '', 'TC', 'GOPIN', line=207)
# Page 266

# V61   VERB 61, DISPLAY DAP ATTITUDE ERRORS ON FDAI ATTITUDE ERROR NEEDLES.

W('43,2163', 0o05516, 'DAPATTER', 'TC', 'DOWNFLAG', line=212)
W('43,2164', 0o00013, '', 'ADRES', 'NEEDLFLG', kind='data', line=213)
W('43,2165', 0o02121, '', 'TC', 'GOPIN', line=214)

# V62   VERB 62, DISPLAY TOTAL ATTITUDE ERRORS ON FDAI ATTITUDE ERROR NEEDLES.

W('43,2166', 0o05504, 'TOTATTER', 'TC', 'UPFLAG', line=218)
W('43,2167', 0o00013, '', 'ADRES', 'NEEDLFLG', kind='data', line=219)
W('43,2170', 0o02121, '', 'TC', 'GOPIN', line=220)

# Page 267
# VBCOARK       VERB 41         DESCRIPTION
# COARSE ALIGN IMU OR RADAR
#
# 1.      REQUIRE NOUN 20 OR NOUN 72 OR TURN ON OPERATOR ERROR.
# 2.      REQUIRE EXT VERB DISPLAY SYS AVAILABLE OR TURN ON OPERATOR ERROR LIGHT AND GO TO PINBRNCH.
# CASE 1, NOUN 20 (ICDU ANGLES)
# 3.      SET EXT VERB DISPLAY ACTIVE FLAG.
# 4.      DISPLAY FLASHING V25,N22 (LOAD NEW ICDU ANGLES).
# RESPONSES
# A.      TERMINATE
# 1.      RELEASE EXT VERB DISPLAY SYSTEM
# B.      PROCEED
# 1.      COARSE ALIGN TO THE EXISTING THETAD'S (ICORK2).
# C.      ENTER
# 1.      COARSE ALIGN TO THE LOADED THETAD'S (ICORK2).
# ICORK2
# 1.      RE-DISPLAY VERB 41.
# 2.      EXECUTE IMUCCARS (IMU COARSE ALIGN).
# 3.      EXECUTE IMUSTALL (ALLOW TIME FOR DATA TRANSFER).
# 4.      RELEASE EXT VERB DISPLAY SYSTEM.
# CASE 2 NOUN 72 (RCDU ANGLES)
# EXIT WITH OP ERROR IF SOMEONE IS USING EITHER RADAD.
# 5.      DISPLAY FLASHING V24,N73 (LOAD NEW RR TRUNION ANGLE AND NEW SHAFT ANGLE).
# RESPONSES
# A.      TERMINATE
# 1.      RELEASE EXT VERB DISPLAY SYS.
# B.      PROCEED OR ENTER
# 1.      EXECUTE AURLOKON (ASK OPERATOR FOR LOCK-ON REQUIREMENTS).
# 2.      RE-DISPLAY VERB 41.
# 3.      SCHEDULE RRDESK2 WITH PRIORITY 20.
# 4.      RELEASE EXT VERB DISPLAY SYS.
# AURLOKON
# 1.      FLASH V04 N12 R1 = 00006 R2 = 00002
# RESPONSES
# A.      TERMINATE
# B.      PROCEED
# 1.      RESET LOCK-ON SWITCH
# 2.      SET CONTINUOUS DESIGNATE FLAG
# 3.      DISABLE R25
# C.      V22 E 1 E, R1 = 00001, PROCEED
# 1.      SET LOCK-ON SWITCH

W('43,2171', 0o02174, 'VBCOARK', 'TC', 'OP/INERT', line=265)
W('43,2172', 0o02205, '', 'TC', 'IMUCOARK', 'RETURN HERE IF NOUN = ICDU (20)', line=266)
W('43,2173', 0o02227, '', 'TC', 'RRDESNBK', 'RETURN HERE IF NOUN = RCDU (72)', line=267)

# RETURNS TO L+1 IF IMU OR L+2 IF RR.

W('43,2174', 0o46007, 'OP/INERT', 'CS', 'OCT24', line=271)
W('43,2175', 0o61002, '', 'AD', 'NOUNREG', line=272)
W('43,2176', 0o00006, '', 'EXTEND', line=273)
# Page 268
W('43,2177', 0o16742, '', 'BZF', 'TCQ', 'IF = 20.', line=275)

W('43,2200', 0o62204, '', 'AD', 'RRIMUDIF', '-52', line=277)
W('43,2201', 0o00006, '', 'EXTEND', line=278)
W('43,2202', 0o16737, '', 'BZF', 'Q+1', line=279)

W('43,2203', 0o02120, '', 'TC', 'ALM/END', 'ILLEGAL.', line=281)

W('43,2204', 0o77713, 'RRIMUDIF', 'DEC', '-52', 'THE IMU', kind='data', line=283)
W('43,2205', 0o02375, 'IMUCOARK', 'TC', 'CKMODCAD', line=284)
W('43,2206', 0o02076, '', 'TC', 'TESTXACT', 'COARSE ALIGN FROM KEYBOARD.', line=285)
W('43,2207', 0o32225, '', 'CAF', 'VNLODCDU', 'CALL FOR THETAD LOAD', line=286)
W('43,2210', 0o04616, '', 'TC', 'BANKCALL', line=287)
W('43,2211', 0o20334, '', 'CADR', 'GOXDSPF', kind='data', line=288)
W('43,2212', 0o05472, '', 'TC', 'TERMEXTV', line=289)
W('43,2213', 0o12214, '', 'TCF', '+1', line=290)

W('43,2214', 0o32226, 'ICORK2', 'CAF', 'IMUCOARV', 'RE-DISPLAY COARSE ALIGN VERB.', line=292)
W('43,2215', 0o04616, '', 'TC', 'BANKCALL', line=293)
W('43,2216', 0o20620, '', 'CADR', 'EXDSPRET', kind='data', line=294)

W('43,2217', 0o04616, '', 'TC', 'BANKCALL', 'CALL MODE SWITCHING PROG', line=296)
W('43,2220', 0o17000, '', 'CADR', 'IMUCOARS', kind='data', line=297)

W('43,2221', 0o04616, '', 'TC', 'BANKCALL', 'STALL', line=299)
W('43,2222', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=300)
W('43,2223', 0o05472, '', 'TC', 'ENDEXTVB', line=301)
W('43,2224', 0o05472, '', 'TC', 'ENDEXTVB', line=302)

W('43,2225', 0o06226, 'VNLODCDU', 'VN', '2522', kind='data', line=304)
W('43,2226', 0o12200, 'IMUCOARV', 'VN', '4100', kind='data', line=305)

# Page 269
# DESIGNATE TO DESIRED GIMBAL ANGLES.

W('43,2227', 0o02642, 'RRDESNBK', 'TC', 'RDRUSECK', line=310)
W('43,2230', 0o02076, '', 'TC', 'TESTXACT', line=311)
W('43,2231', 0o34745, '', 'CA', 'RNDVZBIT', 'IS P20 RUNNING?', line=312)
W('43,2232', 0o70074, '', 'MASK', 'FLAGWRD0', line=313)
W('43,2233', 0o10000, '', 'CCS', 'A', line=314)
W('43,2234', 0o12114, '', 'TCF', 'XACTALM', 'OPERADOR ERROR IF IN P20', line=315)
W('43,2235', 0o42321, '', 'CS', 'OCT41000', 'TERMINATE PRESENT DESIGNATION', line=316)
W('43,2236', 0o00004, '', 'INHINT', '', 'RELINT DONE IN GOXDSPF', line=317)
W('43,2237', 0o70110, '', 'MASK', 'RADMODES', line=318)
W('43,2240', 0o54110, '', 'TS', 'RADMODES', line=319)

W('43,2241', 0o32260, '', 'CAF', 'VNLDRCDU', 'ASK FOR GIMBAL ANGLES.', line=321)
W('43,2242', 0o04616, '', 'TC', 'BANKCALL', line=322)
W('43,2243', 0o20334, '', 'CADR', 'GOXDSPF', kind='data', line=323)
W('43,2244', 0o05472, '', 'TC', 'TERMEXTV', line=324)
W('43,2245', 0o12241, '', 'TCF', '-4', 'V33', line=325)

W('43,2246', 0o04616, '', 'TC', 'BANKCALL', 'ASK OP FOR LOCK ON REQUIREMENTS.', line=327)
W('43,2247', 0o46000, '', 'CADR', 'AURLOKON', kind='data', line=328)

W('43,2250', 0o32226, '', 'CAF', 'OPTCOARV', 'RE-DISPLAY OUR OWN VERB', line=330)
W('43,2251', 0o04616, '', 'TC', 'BANKCALL', line=331)
W('43,2252', 0o20620, '', 'CADR', 'EXDSPRET', kind='data', line=332)

W('43,2253', 0o34736, '', 'CAF', 'PRIO20', line=334)
W('43,2254', 0o05105, '', 'TC', 'FINDVAC', line=335)
#   EBANK= LOSCOUNT
W('43,2255', 0o02261, '', '2CADR', 'RRDESK2', kind='data', line=337)
W('43,2256', 0o66107, kind='data', line=337)

W('43,2257', 0o15472, '', 'TCF', 'TERMEXTV', 'FREES DISPLAY', line=339)

W('43,2260', 0o06111, 'VNLDRCDU', 'VN', '2473', kind='data', line=341)
S('OPTCOARV', 'equals', 0o116226, line=342)  # DIFFERENT NOUNS.

W('43,2261', 0o04616, 'RRDESK2', 'TC', 'BANKCALL', line=344)
W('43,2262', 0o52475, '', 'CADR', 'RRDESNB', kind='data', line=345)

W('43,2263', 0o02264, '', 'TC', '+1', 'DUMMY NEEDED SINCE DESRETRN DOES INCR', line=347)
W('43,2264', 0o30167, '', 'CA', 'PRIORITY', line=348)
W('43,2265', 0o75004, '', 'MASK', 'LOW9', line=349)
W('43,2266', 0o10000, '', 'CCS', 'A', line=350)
W('43,2267', 0o50000, '', 'INDEX', 'A', line=351)
W('43,2270', 0o54000, '', 'TS', 'A', 'RELEASE THIS JOBS VAC AREA.', line=352)
W('43,2271', 0o40000, '', 'COM', '', 'INSURE ENDOFJOB DOES A NOVAC END (BZMF).', line=353)
W('43,2272', 0o26167, '', 'ADS', 'PRIORITY', line=354)
W('43,2273', 0o04616, '', 'TC', 'BANKCALL', 'WAIT FOR COMPLETION OF DESIGNATE', line=355)
W('43,2274', 0o17714, '', 'CADR', 'RADSTALL', kind='data', line=356)
# Page 270
W('43,2275', 0o02277, '', 'TC', '+2', 'BADEND-NO LOCKON OR OUT OF LIMITS', line=358)
W('43,2276', 0o05155, '', 'TC', 'ENDOFJOB', 'GOODEND-LOCKON ACHIEVED', line=359)
W('43,2277', 0o05567, '', 'TC', 'ALARM', line=360)
W('43,2300', 0o00503, '', 'OCT', '503', 'TURN ON ALARM LIGHT -503 DESIGNATE FAIL', kind='data', line=361)

W('43,2301', 0o05155, '', 'TC', 'ENDOFJOB', line=363)

W('43,2302', 0o10110, 'RRDESEND', 'CCS', 'RADMODES', 'TERMINATE CONTINOUS DESIGNATE ONLY', line=365)
W('43,2303', 0o12121, '', 'TCF', 'GOPIN', line=366)
W('43,2304', 0o12121, '', 'TCF', 'GOPIN', line=367)
W('43,2305', 0o12306, '', 'TCF', '+1', line=368)
W('43,2306', 0o42321, '', 'CS', 'OCT41000', 'BEGDES GOES TO ENDRADAR', line=369)
W('43,2307', 0o00004, '', 'INHINT', '', 'RELINT DONE IN DOWNFLAG', line=370)
W('43,2310', 0o70110, '', 'MASK', 'RADMODES', line=371)
W('43,2311', 0o54110, '', 'TS', 'RADMODES', line=372)
W('43,2312', 0o06011, '', 'TC', 'CLRADMOD', line=373)
W('43,2313', 0o34777, '', 'CAF', '1SEC', line=374)
W('43,2314', 0o04616, '', 'TC', 'BANKCALL', line=375)
W('43,2315', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=376)
W('43,2316', 0o05516, '', 'TC', 'DOWNFLAG', 'ENABLE R25 GIMBAL MONITOR', line=377)
W('43,2317', 0o00126, '', 'ADRES', 'NORRMON', kind='data', line=378)
W('43,2320', 0o12121, '', 'TCF', 'GOPIN', line=379)
W('43,2321', 0o41000, 'OCT41000', 'OCT', '41000', 'CONTINUOUS DESIGNATE - DESIGNATE', kind='data', line=380)

# Page 271
#   BANK 23
#   SETLOC EXTVB1
#   BANK
#   COUNT* $$/EXTVB

W('23,2000', 0o04645, 'AURLOKON', 'TC', 'MAKECADR', line=388)
W('23,2001', 0o55113, '', 'TS', 'DESRET', line=389)
W('23,2002', 0o34752, '', 'CAF', 'TWO', line=390)
W('23,2003', 0o55052, '', 'TS', 'OPTIONX +1', line=391)
W('23,2004', 0o36242, '', 'CAF', 'SIX', 'OPTION CODE FOR V04N12', line=392)
W('23,2005', 0o55051, '', 'TS', 'OPTIONX', line=393)

W('23,2006', 0o32037, '', 'CAF', 'V04N1272', line=395)
W('23,2007', 0o04616, '', 'TC', 'BANKCALL', 'R2    00001   LOCK-ON', line=396)
W('23,2010', 0o20353, '', 'CADR', 'GOMARKFR', kind='data', line=397)
W('23,2011', 0o15472, '', 'TCF', 'ENDEXT', 'V34', line=398)
W('23,2012', 0o12017, '', 'TCF', '+5', 'V33', line=399)
W('23,2013', 0o12006, '', 'TCF', '-5', 'V32', line=400)
W('23,2014', 0o34751, '', 'CAF', 'BIT3', line=401)
W('23,2015', 0o05464, '', 'TC', 'BLANKET', line=402)
W('23,2016', 0o05155, '', 'TC', 'ENDOFJOB', line=403)

W('23,2017', 0o31052, '', 'CA', 'OPTIONX +1', line=405)
W('23,2020', 0o74752, '', 'MASK', 'BIT2', line=406)
W('23,2021', 0o10000, '', 'CCS', 'A', line=407)
W('23,2022', 0o12026, '', 'TCF', 'NOLOKON', line=408)
W('23,2023', 0o05504, '', 'TC', 'UPFLAG', line=409)
W('23,2024', 0o00012, '', 'ADRES', 'LOKONSW', kind='data', line=410)
W('23,2025', 0o12034, '', 'TCF', 'AURLKON1', line=411)

W('23,2026', 0o05516, 'NOLOKON', 'TC', 'DOWNFLAG', 'IF NO LOCK-ON, SET BIT15 OF RADMADES TO', line=413)
W('23,2027', 0o00012, '', 'ADRES', 'LOKONSW', 'INDICATE THAT CONTINUOUS DESIGNATION IS', kind='data', line=414)
W('23,2030', 0o05504, '', 'TC', 'UPFLAG', 'WANTED (TO BE TERMINATED BY V44.)', line=415)
W('23,2031', 0o00264, '', 'ADRES', 'CDESFLAG', kind='data', line=416)
W('23,2032', 0o05504, '', 'TC', 'UPFLAG', 'SET NO RR ANGLE MONITOR FLAG.', line=417)
W('23,2033', 0o00126, '', 'ADRES', 'NORRMON', 'DISABLE R25 RR GIMBAL MONITOR IN T4RUPT', kind='data', line=418)
W('23,2034', 0o00003, 'AURLKON1', 'RELINT', line=419)
W('23,2035', 0o31113, '', 'CA', 'DESRET', line=420)
W('23,2036', 0o14640, '', 'TCF', 'BANKJUMP', line=421)

W('23,2037', 0o01014, 'V04N1272', 'VN', '412', kind='data', line=423)
W('23,2040', 0o77757, '-LOKONFG', 'OCT', '-20', kind='data', line=424)

#   BANK 43
#   SETLOC EXTVERBS
#   BANK
#   COUNT* $$/EXTVB

W('43,2322', 0o05504, 'LRON', 'TC', 'UPFLAG', 'PERMIT INCORPORATION OF LR DATA      V57', line=431)

# Page 272
W('43,2323', 0o00254, '', 'ADRES', 'LRINH', kind='data', line=434)
W('43,2324', 0o12121, '', 'TCF', 'GOPIN', line=435)

W('43,2325', 0o05516, 'LROFF', 'TC', 'DOWNFLAG', 'INHIBIT INCORPORATION OF LR DATA      V58', line=437)
W('43,2326', 0o00254, '', 'ADRES', 'LRINH', kind='data', line=438)
W('43,2327', 0o12121, '', 'TCF', 'GOPIN', line=439)

#   EBANK= OGC

# Page 273

# IMUFINEK      VERB 42         DESCRIPTION
# FINE ALIGN IMU
#
# 1.      REQUIRE EXT VERB DISPLAY AVAILABLE AND SET BUSY FLAG OR TURN ON OPER ERROR AND GO TO PINBRNCH.
# 2.      DISPLAY FLASHING V25,N93....LOAD DELTA GYRO ANGLES....
# RESPONSES
# A.      TERMINATE
# 1.      RELEASE EXT VERB DISPLAY SYSTEM.
# B.      PROCEED OR ENTER
# 1.      RE-DISPLAY VERB 42
# 2.      EXECUTE IMUFINE (IMU FIVE ALIGN MODE SWITCHING).
# 3.      EXECUTE IMUSTALL (ALLOW FOR DATA TRANSFER)
# A.      FAILED
# 1.      RELEASE EXT VERB DISPLAY SYSTEM.
# B.      GOOD
# 1.      EXECUTE IMUPULSE (TORQUE IRIGS).
# 2.      EXECUTE IMUSTALL AND RELEASE EXT VERB DISPLAY SYSTEM.

W('43,2330', 0o02375, 'IMUFINEK', 'TC', 'CKMODCAD', line=463)
W('43,2331', 0o02076, '', 'TC', 'TESTXACT', 'FINE ALIGN WITH GYRO TORQUING.', line=464)
W('43,2332', 0o32357, '', 'CAF', 'VNLODGYR', 'CALL FOR LOAD OF GYRO COMMANDS', line=465)
W('43,2333', 0o04616, '', 'TC', 'BANKCALL', line=466)
W('43,2334', 0o20334, '', 'CADR', 'GOXDSPF', kind='data', line=467)
W('43,2335', 0o05472, '', 'TC', 'TERMEXTV', line=468)
W('43,2336', 0o02337, '', 'TC', '+1', 'PROCEED WITHOUT A LOAD', line=469)

W('43,2337', 0o32360, '', 'CAF', 'IMUFINEV', 'RE-DISPLAY OUR OWN VERB', line=471)
W('43,2340', 0o04616, '', 'TC', 'BANKCALL', line=472)
W('43,2341', 0o20620, '', 'CADR', 'EXDSPRET', kind='data', line=473)

W('43,2342', 0o04616, '', 'TC', 'BANKCALL', 'CALL MODE SWITCH PROG', line=475)
W('43,2343', 0o17210, '', 'CADR', 'IMUFINE', kind='data', line=476)

W('43,2344', 0o04616, '', 'TC', 'BANKCALL', 'HIBERNATION', line=478)
W('43,2345', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=479)
W('43,2346', 0o05472, '', 'TC', 'ENDEXTVB', line=480)

W('43,2347', 0o32356, 'FINEK2', 'CAF', 'LGYROBIN', 'PINBALL LEFT COMMANDS IN OGC REGISTERS', line=482)
W('43,2350', 0o04616, '', 'TC', 'BANKCALL', line=483)
W('43,2351', 0o17323, '', 'CADR', 'IMUPULSE', kind='data', line=484)

W('43,2352', 0o04616, '', 'TC', 'BANKCALL', 'WAIT FOR PULSES TO GET OUT.', line=486)
W('43,2353', 0o17716, '', 'CADR', 'IMUSTALL', kind='data', line=487)
W('43,2354', 0o05472, '', 'TC', 'ENDEXTVB', line=488)
W('43,2355', 0o05472, '', 'TC', 'ENDEXTVB', line=489)

W('43,2356', 0o02737, 'LGYROBIN', 'ECADR', 'OGC', kind='data', line=491)
W('43,2357', 0o06335, 'VNLODGYR', 'VN', '2593', kind='data', line=492)
W('43,2360', 0o12400, 'IMUFINEV', 'VN', '4200', kind='data', line=493)

# GOLOADLV      VERB 50         DESCRIPTION
# AND OTHER PLEASE
# Page 274
# DO SOMETHING VERBS
#
# PLEASE PERFORM, MARK, CALIBRATE, ETC.
#
# 1.      PRESSING ENTER ON DSKY INDICATES REQUESTED ACTION HAS BEEN PERFORMED, AND THE PROGRAM DOES THE
# SAME RECALL AS A COMPLETED LOAD.
# 2.      THE EXECUTION OF A VERB 33 (PROCEED WITHOUT DATA) INDICATES THE REQUESTED ACTION IS NOT DESIRED.

#   SBANK= PINSUPER  # FOR LOADLV1 AND SHOWSUM CADR'S

W('43,2361', 0o04433, 'GOLOADLV', 'TC', 'FLASHOFF', line=508)

W('43,2362', 0o34201, '', 'CAF', 'PINSUPBT', line=510)
W('43,2363', 0o00006, '', 'EXTEND', line=511)
W('43,2364', 0o01007, '', 'WRITE', 'SUPERBNK', line=512)
W('43,2365', 0o04635, '', 'TC', 'POSTJUMP', line=513)
W('43,2366', 0o62001, '', 'CADR', 'LOADLV1', kind='data', line=514)

# VERB 47 -- AGS INITIALIZATION -- R47.
#
# SEE LOG SECTION AGS INITIALIZATION FOR OTHER PERTINENT REMARKS.

W('43,2367', 0o02076, 'V47TXACT', 'TC', 'TESTXACT', 'NO OTHER EXTVERB.', line=520)
W('43,2370', 0o34740, '', 'CAF', 'PRIO4', line=521)
W('43,2371', 0o05105, '', 'TC', 'FINDVAC', line=522)
# [WORKAROUND] RSB 2009
#   SBANK= LOWSUPER
# [WORKAROUND]
#   EBANK= AGSBUFF
W('43,2372', 0o02005, '', '2CADR', 'AGSINIT', kind='data', line=527)
W('43,2373', 0o64064, kind='data', line=527)

W('43,2374', 0o05155, '', 'TC', 'ENDOFJOB', line=529)

W('43,2375', 0o31304, 'CKMODCAD', 'CA', 'MODECADR', line=531)
W('43,2376', 0o00006, '', 'EXTEND', line=532)
W('43,2377', 0o16742, '', 'BZF', 'TCQ', line=533)
W('43,2400', 0o02120, '', 'TC', 'ALM/END', 'SOMEBODY IS USING MODECADR SO EXIT', line=534)

# Page 275
# ALINTIME      VERB 55         DESCRIPTION
# REQUIRE P00 OR P00-.
#
# 1.      SET EXT VERB DISPLAY BUSY FLAG.
# 2.      DISPLAY FLASHING V25,N24 (LOAD DELTA TIME FOR AGC CLOCK.
# 3.      REQUIRE EXECUTION OF VERB 23.
# 4.      ADD DELTA TIME, RECEIVED FROM INPUT REGISTER, TO THE COMPUTER TIME.
# 5.      RELEASE EXT VERB DISPLAY SYSTEM

W('43,2401', 0o02076, 'ALINTIME', 'TC', 'TESTXACT', line=546)
W('43,2402', 0o04635, '', 'TC', 'POSTJUMP', 'NO ROOM IN 43', line=547)
W('43,2403', 0o64002, '', 'CADR', 'R33', kind='data', line=548)

#   BANK 42
#   SETLOC SBAND
#   BANK
#   COUNT* $$/R33

W('42,2002', 0o35021, 'R33', 'CAF', 'PRIO7', line=555)
W('42,2003', 0o05146, '', 'TC', 'PRIOCHNG', line=556)
W('42,2004', 0o32034, '', 'CAF', 'VNLODDT', line=557)
W('42,2005', 0o04616, '', 'TC', 'BANKCALL', line=558)
W('42,2006', 0o20334, '', 'CADR', 'GOXDSPF', kind='data', line=559)
W('42,2007', 0o05472, '', 'TC', 'ENDEXT', 'TERMINATE', line=560)
W('42,2010', 0o05472, '', 'TC', 'ENDEXT', 'PROCEED', line=561)
W('42,2011', 0o42033, '', 'CS', 'DEC23', 'DATA IN OR RESEQUENCE (UNLIKELY)', line=562)
W('42,2012', 0o60154, '', 'AD', 'MPAC', 'RECALL LEFT VERB IN MPAC', line=563)
W('42,2013', 0o00006, '', 'EXTEND', line=564)
W('42,2014', 0o12016, '', 'BZF', 'UPDATIME', 'GO AHEAD WITH UPDATE ONLY IF RECALL', line=565)
W('42,2015', 0o05472, '', 'TC', 'ENDEXT', '      WITH V23 (DATA IN).', line=566)

W('42,2016', 0o00004, 'UPDATIME', 'INHINT', '', 'DELTA TIME IS IN DSPTEM1, +1.', line=568)
W('42,2017', 0o34755, '', 'CAF', 'ZERO', line=569)
W('42,2020', 0o54156, '', 'TS', 'MPAC +2', 'NEEDED FOR TP AGREE', line=570)
W('42,2021', 0o54001, '', 'TS', 'L', 'ZERO T1 + 2 WHILE ALIGNING.', line=571)
W('42,2022', 0o52025, '', 'DXCH', 'TIME2', line=572)
W('42,2023', 0o52155, '', 'DXCH', 'MPAC', line=573)
W('42,2024', 0o53052, '', 'DXCH', 'DSPTEM2 +1', 'INCREMENT', line=574)
W('42,2025', 0o20155, '', 'DAS', 'MPAC', line=575)

W('42,2026', 0o07257, '', 'TC', 'TPAGREE', 'FORCE SIGN AGREEMENT.', line=577)
W('42,2027', 0o52155, '', 'DXCH', 'MPAC', 'NEW CLOCK.', line=578)
W('42,2030', 0o20025, '', 'DAS', 'TIME2', line=579)
W('42,2031', 0o00003, '', 'RELINT', line=580)
W('42,2032', 0o05472, 'UPDTMEND', 'TC', 'ENDEXT', line=581)

W('42,2033', 0o00027, 'DEC23', 'DEC', '23', 'V 23', kind='data', line=583)

W('42,2034', 0o06230, 'VNLODDT', 'VN', '2524', 'V25N24 FOR LOAD DELTA TIME', kind='data', line=585)

# Page 276
# SET UP FOR RADAR SAMPLING.

#   BANK 42
#   SETLOC EXTVERBS
#   BANK

#   EBANK= RSTACK

#   COUNT* $$/R0477

W('43,2404', 0o02642, 'R77', 'TC', 'RDRUSECK', 'TRY TO AVOID THE 1210.', line=598)
W('43,2405', 0o30077, '', 'CA', 'FLAGWRD3', 'IS R04 RUNNING?', line=599)
W('43,2406', 0o74743, '', 'MASK', 'R04FLBIT', line=600)
W('43,2407', 0o10000, '', 'CCS', 'A', line=601)
W('43,2410', 0o02120, '', 'TC', 'ALM/END', 'YES.', line=602)
W('43,2411', 0o05504, '', 'TC', 'UPFLAG', line=603)
W('43,2412', 0o00117, '', 'ADRES', 'R77FLAG', kind='data', line=604)
W('43,2413', 0o12420, '', 'TCF', 'R04Z', line=605)

W('43,2414', 0o02642, 'R04', 'TC', 'RDRUSECK', 'TRY TO AVOID THE 1210.', line=607)
W('43,2415', 0o02076, '', 'TC', 'TESTXACT', line=608)
W('43,2416', 0o05504, '', 'TC', 'UPFLAG', line=609)
W('43,2417', 0o00063, '', 'ADRES', 'R04FLAG', 'SET R04FLAG FOR ALARMS', kind='data', line=610)

W('43,2420', 0o34741, 'R04Z', 'CAF', 'EBANK4', line=612)
W('43,2421', 0o54003, '', 'TS', 'EBANK', line=613)
W('43,2422', 0o32640, '', 'CAF', '1SEC+1', 'SAMPLE ONCE PER SECOND', line=614)
W('43,2423', 0o55755, '', 'TS', 'RSAMPDT', line=615)
W('43,2424', 0o34755, '', 'CAF', 'ZERO', line=616)
W('43,2425', 0o55754, '', 'TS', 'RTSTLOC', line=617)
W('43,2426', 0o55756, '', 'TS', 'RFAILCNT', 'ZERO BAD SAMPLE COUNTER', line=618)

W('43,2427', 0o00004, '', 'INHINT', line=620)
W('43,2430', 0o42641, '', 'CS', 'LRPOSCAL', 'INITIALIZE', line=621)
W('43,2431', 0o70110, '', 'MASK', 'RADMODES', '      BIT 9   LR RANGE LOW SCALE =0', line=622)
W('43,2432', 0o54110, '', 'TS', 'RADMODES', '      BIT 6   LR POS 1 =0', line=623)
W('43,2433', 0o32641, '', 'CAF', 'LRPOSCAL', '      BIT 3   RR RANGE LOW SCALE =0', line=624)
W('43,2434', 0o00006, '', 'EXTEND', line=625)
W('43,2435', 0o02033, '', 'RAND', 'CHAN33', line=626)
W('43,2436', 0o26110, '', 'ADS', 'RADMODES', line=627)
W('43,2437', 0o00003, '', 'RELINT', line=628)

W('43,2440', 0o40077, '', 'CS', 'FLAGWRD3', 'CHECK R04FLAG         R04 =1          R77 =0', line=630)
W('43,2441', 0o74743, '', 'MASK', 'R04FLBIT', line=631)
W('43,2442', 0o10000, '', 'CCS', 'A', line=632)
W('43,2443', 0o12575, '', 'TCF', 'R04K', line=633)

W('43,2444', 0o34753, '', 'CAF', 'ONE', 'INDICATES RENDEZVOUS DESIRED', line=635)
W('43,2445', 0o55052, '', 'TS', 'OPTIONX +1', line=636)
W('43,2446', 0o34751, 'R04A', 'CAF', 'BIT3', 'OPTION CODE FOR V04N12', line=637)

# Page 277
W('43,2447', 0o55051, '', 'TS', 'OPTIONX', line=640)
W('43,2450', 0o32635, '', 'CAF', 'V04N12X', line=641)
W('43,2451', 0o04616, '', 'TC', 'BANKCALL', '      R2      00001   RENDEZVOUS RADAR', line=642)
W('43,2452', 0o20353, '', 'CADR', 'GOMARKFR', '              00002   LANDING RADAR', kind='data', line=643)
W('43,2453', 0o12603, '', 'TCF', 'R04END', 'V34', line=644)
W('43,2454', 0o12461, '', 'TCF', '+5', 'V33', line=645)
W('43,2455', 0o12450, '', 'TCF', 'R04A +2', 'R2', line=646)
W('43,2456', 0o34751, '', 'CAF', 'BIT3', line=647)
W('43,2457', 0o05464, '', 'TC', 'BLANKET', line=648)
W('43,2460', 0o05155, '', 'TC', 'ENDOFJOB', line=649)

W('43,2461', 0o31052, '', 'CA', 'OPTIONX +1', 'SAVE DESIRED OPTION   RR =1   LR =2', line=651)
W('43,2462', 0o55751, '', 'TS', 'RTSTDEX', line=652)

W('43,2463', 0o36242, 'R04X', 'CAF', 'SIX', 'RR OR LR DESIRED', line=654)
W('43,2464', 0o71751, '', 'MASK', 'RTSTDEX', line=655)
W('43,2465', 0o10000, '', 'CCS', 'A', line=656)
W('43,2466', 0o12577, '', 'TCF', 'R04L', 'LANDING RADAR', line=657)
W('43,2467', 0o55753, '', 'TS', 'RTSTBASE', 'FOR RR        BASE =0, MAX =1', line=658)

W('43,2470', 0o34752, 'R04B', 'CAF', 'BIT2', 'IS RR AUTO MODE DISCRETE PRESENT', line=660)
W('43,2471', 0o00006, '', 'EXTEND', line=661)
W('43,2472', 0o02033, '', 'RAND', 'CHAN33', line=662)
W('43,2473', 0o00006, '', 'EXTEND', line=663)
W('43,2474', 0o12505, '', 'BZF', 'R04C', 'YES', line=664)

W('43,2475', 0o32637, '', 'CAF', '201R04', 'REQUEST SELECTION OF RR AUTO MODE', line=666)
W('43,2476', 0o55045, '', 'TS', 'DSPTEM1', line=667)
W('43,2477', 0o32636, '', 'CAF', 'V50N25X', line=668)
W('43,2500', 0o04616, '', 'TC', 'BANKCALL', line=669)
W('43,2501', 0o20345, '', 'CADR', 'GOMARK4', kind='data', line=670)
W('43,2502', 0o12603, '', 'TCF', 'R04END', 'V34', line=671)
W('43,2503', 0o12470, '', 'TCF', 'R04B', 'V33', line=672)
W('43,2504', 0o12475, '', 'TCF', '-7', 'E', line=673)

W('43,2505', 0o34736, 'R04C', 'CAF', 'BIT14', 'ENABLE RR AUTO TRACKER', line=675)
W('43,2506', 0o00006, '', 'EXTEND', line=676)
W('43,2507', 0o05012, '', 'WOR', 'CHAN12', line=677)

W('43,2510', 0o34752, '', 'CAF', 'TWO', line=679)
W('43,2511', 0o55752, '', 'TS', 'RTSTMAX', 'FOR SEQUENTIAL STORAGE', line=680)

W('43,2512', 0o05203, '', 'TC', 'WAITLIST', line=682)
# [WORKAROUND] RSB 2009
#   SBANK= PINSUPER
# [WORKAROUND]
#   EBANK= RSTACK
W('43,2513', 0o02003, '', '2CADR', 'RADSAMP', kind='data', line=687)
W('43,2514', 0o52104, kind='data', line=687)

W('43,2515', 0o00003, '', 'RELINT', line=689)

W('43,2516', 0o40077, '', 'CS', 'FLAGWRD3', 'CHECK R04FLAG         R04 =1          R77 =0', line=691)
W('43,2517', 0o74743, '', 'MASK', 'R04FLBIT', line=692)
# Page 278
W('43,2520', 0o10000, '', 'CCS', 'A', line=694)
W('43,2521', 0o12121, '', 'TCF', 'GOPIN', 'R77', line=695)

W('43,2522', 0o36242, '', 'CAF', 'SIX', 'RR OR LR', line=697)
W('43,2523', 0o71751, '', 'MASK', 'RTSTDEX', line=698)
W('43,2524', 0o10000, '', 'CCS', 'A', line=699)
W('43,2525', 0o12542, '', 'TCF', 'R04LR', 'LR', line=700)

W('43,2526', 0o32631, 'R04RR', 'CAF', 'V16N72', 'DISPLAY RR CDU ANGLES (1/SEC)', line=702)
W('43,2527', 0o04616, '', 'TC', 'BANKCALL', '      R1 + XXX.XX DEG         TRUNNION', line=703)
W('43,2530', 0o20334, '', 'CADR', 'GOMARKF', '      R2 + XXX.XX DEG         SHAFT', kind='data', line=704)
W('43,2531', 0o12603, '', 'TCF', 'R04END', 'V34   R3   BLANK', line=705)
W('43,2532', 0o12534, '', 'TCF', '+2', 'V33', line=706)
W('43,2533', 0o12526, '', 'TCF', 'R04RR', 'V32', line=707)

W('43,2534', 0o32632, '', 'CAF', 'V16N78', 'DISPLAY RR RANGE AND RANGE RATE (1/SEC)', line=709)
W('43,2535', 0o04616, '', 'TC', 'BANKCALL', '      R1 +- XXX.XX NM         RANGE', line=710)
W('43,2536', 0o20334, '', 'CADR', 'GOMARKF', '      R2 +- XXXXX. FPS        RANGE RATE', kind='data', line=711)
W('43,2537', 0o12603, '', 'TCF', 'R04END', 'V34   R3    BLANK', line=712)
W('43,2540', 0o12556, '', 'TCF', 'R04Y', 'V33', line=713)
W('43,2541', 0o12526, '', 'TCF', 'R04RR', 'V32', line=714)

W('43,2542', 0o32633, 'R04LR', 'CAF', 'V16N66', 'DISPLAY LR RANGE AND POSITON (1/SEC)', line=716)
W('43,2543', 0o04616, '', 'TC', 'BANKCALL', '      R1 +- XXXXX, FT         LR RANGE', line=717)
W('43,2544', 0o20334, '', 'CADR', 'GOMARKF', '      R2 +  0000X.            POS. NO.', kind='data', line=718)
W('43,2545', 0o12603, '', 'TCF', 'R04END', 'V34   R3    BLANK', line=719)
W('43,2546', 0o12550, '', 'TCF', '+2', 'V33', line=720)
W('43,2547', 0o12542, '', 'TCF', 'R04LR', 'V32', line=721)

W('43,2550', 0o32634, '', 'CAF', 'V16N67', 'DISPLAY LR VELX, VELY, VELZ (1/SEC)', line=723)
W('43,2551', 0o04616, '', 'TC', 'BANKCALL', '      R1 +- XXXXX. FPS        LR V(X)', line=724)
W('43,2552', 0o20334, '', 'CADR', 'GOMARKF', '      R2 +- XXXXX. FPS        LR V(Y)', kind='data', line=725)
W('43,2553', 0o12603, '', 'TCF', 'R04END', 'V34   R3 +- XXXXX. FPS        LR V(Z)', line=726)
W('43,2554', 0o12556, '', 'TCF', 'R04Y', 'V33', line=727)
W('43,2555', 0o12542, '', 'TCF', 'R04LR', 'V32', line=728)

W('43,2556', 0o34755, 'R04Y', 'CAF', 'ZERO', 'TO TERMINATE SAMPLING.', line=730)
W('43,2557', 0o55755, '', 'TS', 'RSAMPDT', line=731)
W('43,2560', 0o35000, '', 'CAF', '2SECS', 'WAIT FOR LAST RADARUP', line=732)
W('43,2561', 0o04616, '', 'TC', 'BANKCALL', line=733)
W('43,2562', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=734)
W('43,2563', 0o32640, '', 'CAF', '1SEC+1', 'SAMPLE ONCE PER SECOND', line=735)
W('43,2564', 0o55755, '', 'TS', 'RSAMPDT', line=736)
W('43,2565', 0o34755, '', 'CAF', 'ZERO', 'FOR STORING RESULTS', line=737)
W('43,2566', 0o55754, '', 'TS', 'RTSTLOC', line=738)
W('43,2567', 0o36242, '', 'CAF', 'SIX', line=739)
W('43,2570', 0o71751, '', 'MASK', 'RTSTDEX', line=740)
W('43,2571', 0o10000, '', 'CCS', 'A', line=741)
W('43,2572', 0o44753, '', 'CS', 'ONE', 'WAS LR', line=742)
W('43,2573', 0o64752, '', 'AD', 'TWO', 'WAS RR', line=743)
# Page 279

W('43,2574', 0o12462, '', 'TCF', 'R04X -1', line=746)

W('43,2575', 0o34766, 'R04K', 'CAF', '250MS+1', 'SAMPLE 4 LR COMPONENTS PER SECOND.', line=748)
W('43,2576', 0o55755, '', 'TS', 'RSAMPDT', line=749)

W('43,2577', 0o34752, 'R04L', 'CAF', 'TWO', line=751)
W('43,2600', 0o55753, '', 'TS', 'RTSTBASE', 'FOR LR        BASE =2, MAX =3', line=752)
W('43,2601', 0o36242, '', 'CAF', 'SIX', line=753)
W('43,2602', 0o12511, '', 'TCF', 'R04C +4', line=754)
W('43,2603', 0o34755, 'R04END', 'CAF', 'ZERO', 'ZERO RSAMPDT', line=755)
W('43,2604', 0o55755, '', 'TS', 'RSAMPDT', 'TO TERMINATE SAMPLING', line=756)
W('43,2605', 0o34744, '', 'CAF', 'BIT8', 'WAIT 1.28 SECONDS FOR POSSIBLE', line=757)
W('43,2606', 0o04616, '', 'TC', 'BANKCALL', 'PENDING RUPT.', line=758)
W('43,2607', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=759)

W('43,2610', 0o00004, '', 'INHINT', line=761)
W('43,2611', 0o44736, '', 'CS', 'BIT14', 'DISABLE RR AUTO TRACKER.', line=762)
W('43,2612', 0o00006, '', 'EXTEND', line=763)
W('43,2613', 0o03012, '', 'WAND', 'CHAN12', line=764)

W('43,2614', 0o05516, '', 'TC', 'DOWNFLAG', line=766)
W('43,2615', 0o00063, '', 'ADRES', 'R04FLAG', 'SIGNAL END OF R04.', kind='data', line=767)

W('43,2616', 0o05472, '', 'TC', 'ENDEXT', line=769)

W('43,2617', 0o34741, 'R77END', 'CAF', 'EBANK4', 'TO TERMINATE SAMPLING', line=771)
W('43,2620', 0o54003, '', 'TS', 'EBANK', line=772)
W('43,2621', 0o34755, '', 'CAF', 'ZERO', line=773)
W('43,2622', 0o55755, '', 'TS', 'RSAMPDT', line=774)
W('43,2623', 0o34746, '', 'CAF', 'BIT6', 'WAIT 320 MS FOR POSSIBLE', line=775)
W('43,2624', 0o04616, '', 'TC', 'BANKCALL', 'PENDING RUPT.', line=776)
W('43,2625', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=777)

W('43,2626', 0o05516, '', 'TC', 'DOWNFLAG', line=779)
W('43,2627', 0o00117, '', 'ADRES', 'R77FLAG', kind='data', line=780)
W('43,2630', 0o12121, '', 'TCF', 'GOPIN', line=781)

W('43,2631', 0o04110, 'V16N72', 'VN', '1672', kind='data', line=783)
W('43,2632', 0o04116, 'V16N78', 'VN', '1678', kind='data', line=784)
W('43,2633', 0o04102, 'V16N66', 'VN', '1666', kind='data', line=785)
W('43,2634', 0o04103, 'V16N67', 'VN', '1667', kind='data', line=786)
W('43,2635', 0o01014, 'V04N12X', 'VN', '412', kind='data', line=787)
W('43,2636', 0o14431, 'V50N25X', 'VN', '5025', kind='data', line=788)
W('43,2637', 0o00201, '201R04', 'OCT', '00201', kind='data', line=789)
W('43,2640', 0o00145, '1SEC+1', 'DEC', '101', kind='data', line=790)
S('250MS+1', 'equals', 0o4766, line=791)
W('43,2641', 0o00444, 'LRPOSCAL', 'OCT', '444', kind='data', line=792)

# Page 280
W('43,2642', 0o40077, 'RDRUSECK', 'CS', 'FLAGWRD3', 'IS R29 ON?', line=795)
W('43,2643', 0o74741, '', 'MASK', 'NR29FBIT', line=796)
W('43,2644', 0o10000, '', 'CCS', 'A', line=797)
W('43,2645', 0o02120, '', 'TC', 'ALM/END', 'YES', line=798)
W('43,2646', 0o30101, '', 'CA', 'FLAGWRD5', 'IS R77 RUNNING?', line=799)
W('43,2647', 0o74741, '', 'MASK', 'R77FLBIT', line=800)
W('43,2650', 0o10000, '', 'CCS', 'A', line=801)
W('43,2651', 0o02120, '', 'TC', 'ALM/END', 'YES.', line=802)
W('43,2652', 0o40103, '', 'CS', 'FLAGWRD7', 'IS SERVICER RUNNING AND HENCE POSSIBLY', line=803)
W('43,2653', 0o74746, '', 'MASK', 'V37FLBIT', 'R12 USING THE LR?', line=804)
W('43,2654', 0o10000, '', 'CCS', 'A', line=805)
W('43,2655', 0o12662, '', 'TCF', 'CHECKRR', 'NO', line=806)
W('43,2656', 0o40107, '', 'CS', 'FLGWRD11', 'YES, IS R12 ON?', line=807)
W('43,2657', 0o74735, '', 'MASK', 'LRBYBIT', line=808)
W('43,2660', 0o10000, '', 'CCS', 'A', line=809)
W('43,2661', 0o02120, '', 'TC', 'ALM/END', 'YES', line=810)
W('43,2662', 0o40075, 'CHECKRR', 'CS', 'FLAGWRD1', 'IS THE TRACK FLAG SET AND HENCE POSSIBLY', line=811)
W('43,2663', 0o74747, '', 'MASK', 'TRACKBIT', 'P20 USING THE RR?', line=812)
W('43,2664', 0o10000, '', 'CCS', 'A', line=813)
W('43,2665', 0o12672, '', 'TCF', 'CHECKP22', 'NO, CHECK FOR P22.', line=814)

W('43,2666', 0o30074, 'CKRNDBIT', 'CA', 'FLAGWRD0', 'YES, BUT IS IT P25?', line=816)
W('43,2667', 0o74745, '', 'MASK', 'RNDVZBIT', line=817)
W('43,2670', 0o10000, '', 'CCS', 'A', line=818)
W('43,2671', 0o02120, '', 'TC', 'ALM/END', line=819)
W('43,2672', 0o41011, 'CHECKP22', 'CS', 'MODREG', line=820)
W('43,2673', 0o62677, '', 'AD', 'DEC22', line=821)
W('43,2674', 0o00006, '', 'EXTEND', line=822)
W('43,2675', 0o12120, '', 'BZF', 'ALM/END', line=823)
W('43,2676', 0o00002, '', 'TC', 'Q', line=824)

W('43,2677', 0o00026, 'DEC22', 'DEC', '22', kind='data', line=826)

#   COUNT* $$/EXTVB

W('43,2700', 0o02123, 'VB64', 'TC', 'CHKPOOH', 'DEMAND PROGRAM 00.', line=830)
W('43,2701', 0o02076, '', 'TC', 'TESTXACT', 'IF DISPLAY SYS. NOT BUSY MAKE IT BUSY.', line=831)
W('43,2702', 0o34740, '', 'CAF', 'PRIO4', line=832)
W('43,2703', 0o05105, '', 'TC', 'FINDVAC', line=833)
#   EBANK= ALPHASB
W('43,2704', 0o03606, '', '2CADR', 'SBANDANT', 'CALC., DISPLAY S-BAND ANTENNA ANGLES.', kind='data', line=835)
W('43,2705', 0o64104, kind='data', line=835)

W('43,2706', 0o05155, '', 'TC', 'ENDOFJOB', line=837)

# Page 281
# IMUATTCK      VERB 43         DESCRIPTION
# LOAD IMU ATTITUDE ERROR METERS
#
# 1.      REQUIRE P00 OR FRESH START.
# 2.      REQUIRE COARSE ALIGN ENABLE AND ZERO ICDU BITS OFF.
# 3.      REQUIRE THAT NEEDLES BE OFF.
# 4.      REQUEST LOAD OF N22 (VALUES TO BE DISPLAYED).
# 5.      ON PROCEED OR ENTER RE-DISPLAY V43 AND SEND PULSES.

W('43,2707', 0o02123, 'IMUATTCK', 'TC', 'CHKPOOH', 'VB 76 -- LOAD IMU ATT. ERROR METERS', line=849)

W('43,2710', 0o34763, '', 'CAF', 'BITS4&5', 'SEE IF COARSE ALIGN ENABLE AND ZERO IMU', line=851)
W('43,2711', 0o00006, '', 'EXTEND', '', 'CDUS BITS ARE ON', line=852)
W('43,2712', 0o02012, '', 'RAND', 'CHAN12', line=853)
W('43,2713', 0o10000, '', 'CCS', 'A', line=854)
W('43,2714', 0o12120, '', 'TCF', 'ALM/END', 'NOT ALLOWED IF IMU COARSE OR IMU ZERO ON', line=855)

W('43,2715', 0o34355, '', 'CAF', 'BIT13-14', 'BOTH BITS 13 AND 14 MUST BE 1', line=857)
W('43,2716', 0o00006, '', 'EXTEND', '', 'INDICATING THE MODE SELECTED IS OFF.', line=858)
W('43,2717', 0o06031, '', 'RXOR', 'CHAN31', line=859)
W('43,2720', 0o74355, '', 'MASK', 'BIT13-14', line=860)
W('43,2721', 0o00006, '', 'EXTEND', line=861)
W('43,2722', 0o12724, '', 'BZF', '+2', 'NEEDLES IS OFF.', line=862)
W('43,2723', 0o12120, '', 'TCF', 'ALM/END', 'EXIT.  NEEDLES IS ON.', line=863)

W('43,2724', 0o02076, '', 'TC', 'TESTXACT', line=865)

W('43,2725', 0o32225, '', 'CAF', 'VNLODCDU', line=867)
W('43,2726', 0o04616, '', 'TC', 'BANKCALL', line=868)
W('43,2727', 0o20334, '', 'CADR', 'GOXDSPF', kind='data', line=869)
W('43,2730', 0o05472, '', 'TC', 'ENDEXT', 'V34', line=870)
W('43,2731', 0o02732, '', 'TC', '+1', line=871)
W('43,2732', 0o32745, '', 'CAF', 'V43K', 'REDISPLAY OUR VERB.', line=872)
W('43,2733', 0o04616, '', 'TC', 'BANKCALL', line=873)
W('43,2734', 0o20620, '', 'CADR', 'EXDSPRET', kind='data', line=874)
W('43,2735', 0o34746, '', 'CAF', 'BIT6', line=875)
W('43,2736', 0o00006, '', 'EXTEND', line=876)
W('43,2737', 0o05012, '', 'WOR', 'CHAN12', 'ENABLE ERROR COUNTERS.', line=877)
W('43,2740', 0o34752, '', 'CAF', 'TWO', line=878)
W('43,2741', 0o05203, '', 'TC', 'WAITLIST', 'PUT OUT COMMANDS IN .32 SECONDS.', line=879)
#   EBANK= THETAD
W('43,2742', 0o02035, '', '2CADR', 'ATTCK2', kind='data', line=881)
W('43,2743', 0o64100, kind='data', line=881)

W('43,2744', 0o15472, '', 'TCF', 'ENDEXT', line=883)

#   BANK 42
#   SETLOC PINBALL3  # SOMETHING IN B42.
#   BANK

#   COUNT* $$/EXTVB
# Page 282
W('42,2035', 0o34752, 'ATTCK2', 'CAF', 'TWO', 'PUT OUT COMMANDS.', line=891)
W('42,2036', 0o54002, '', 'TS', 'Q', 'CDU WILL LIMIT EXCESS DATA.', line=892)
W('42,2037', 0o50000, '', 'INDEX', 'A', line=893)
W('42,2040', 0o30321, '', 'CA', 'THETAD', line=894)
W('42,2041', 0o00006, '', 'EXTEND', line=895)
W('42,2042', 0o72053, '', 'MP', 'ATTSCALE', line=896)
W('42,2043', 0o50002, '', 'INDEX', 'Q', line=897)
W('42,2044', 0o56050, '', 'XCH', 'CDUXCMD', line=898)
W('42,2045', 0o10002, '', 'CCS', 'Q', line=899)
W('42,2046', 0o12036, '', 'TCF', 'ATTCK2 +1', line=900)

W('42,2047', 0o37740, '', 'CAF', '13,14,15', line=902)
W('42,2050', 0o00006, '', 'EXTEND', line=903)
W('42,2051', 0o05014, '', 'WOR', 'CHAN14', line=904)
W('42,2052', 0o15261, '', 'TCF', 'TASKOVER', 'LEAVE ERROR COUNTERS ENABLED.', line=905)

W('42,2053', 0o03146, 'ATTSCALE', 'DEC', '0.1', kind='data', line=907)

#   BANK 7
#   SETLOC EXTVERBS
#   BANK

#   COUNT* $$/EXTVB

W('43,2745', 0o12600, 'V43K', 'VN', '4300', kind='data', line=915)

# V82PERF       VERB82          DESCRIPTION
# REQUEST ORBIT PARAMETERS DISPLAY (R30)
#
# 1.      IF AVERAGE G IS OFF:
# FLASH DISPLAY V04N06.  R2 INDICATES WHICH SHIP'S STATE VECTOR IS
# TO BE UPDATED.  INITIAL CHOICE IS THIS SHIP (R2=1).  ASTRONAUT
# CAN CHANGE TO OTHER SHIP BY V22EXE, WHERE X NOT EQ I.
# SELECTED STATE VECTOR UPDATED BY THISPREC (OTHPREC).
# CALLS SR30.1 (WHICH CALLS TFFCONMU + TFFRP/RA) TO CALCULATE
# RPER (PERIGEE RADIUS), RAP0 (APOGEE RADIUS), HPER (PERIGEE
# HEIGHT ABOVE LAUNCH PAD OR LUNAR LANDING SITE), HAPO (APOGEE
# HEIGHT AS ABOVE), TPER (TIME TO PERIGEE), TFF (TIME TO
# INTERSECT 300 KFT ABOVE PAD OR 35KFT ABOVE LANDING SITE).
# FLASH MONITOR V16N44 (HAPO, HPER, TFF).  TFF IS -59M59S IF IT WAS
# NOT COMPUTABLE, OTHERWISE IT INCREMENTS ONCE PER SECOND.
# ASTRONAUT HAS OPTION TO MONITOR TPER BY KEYING IN N 32 E.
# DISPLAY IS IN HMS, IS NEGATIVE (AS WAS TFF), AND INCREMENTS
# ONCE PER SECOND ONLY IF TFF DISPLAY WAS -59M59S.
#
# 2.      IF AVERAGE G IS ON:
# CALLS SR30.1 APPROX EVERY TWO SECS.  STATE VECTOR IS ALWAYS
# FOR THIS VEHICLE.  V82 DOES NOT DISTURB STATE VECTOR.  RESULTS
# OF SR30.1 ARE RAPO, RPER, HAPO, HPER, TPER, TFF.
# FLASH MONITOR V16N44 (HAPO, HPER, TFF).
# IF MODE IS P11, THEN CALL DELRSPL SO ASTRONAUT CAN MONITOR
# RESULTS BY N50E.  SPLASH COMPUTATION DONE ONCE PER TWO SECS.

# Page 283
W('43,2746', 0o02076, 'V82PERF', 'TC', 'TESTXACT', line=945)

W('43,2747', 0o35021, '', 'CAF', 'PRIO7', 'LESS THAN LAMBERT.  R30,V82', line=947)
W('43,2750', 0o05146, '', 'TC', 'PRIOCHNG', line=948)
W('43,2751', 0o00006, '', 'EXTEND', line=949)
W('43,2752', 0o32755, '', 'DCA', 'V82CON', line=950)
W('43,2753', 0o05165, '', 'TC', 'SUPDXCHZ', 'V82CALL IN DIFF SUPERBANK FROM V82PERF', line=951)

#   EBANK= HAPO
W('43,2754', 0o03242, 'V82CON', '2CADR', 'V82CALL', kind='data', line=954)
W('43,2755', 0o44104, kind='data', line=954)

# VB83PERF      VERB 83         DESCRIPTION
# REQUEST RENDEZVOUS PARAMETER DISPLAY (R31)
#
# 1.      SET EXT VERB DISPLAY BUSY FLAG.
# 2.      SCHEDULE R31CALL WITH PRIORITY 5.
# A.      DISPLAY
# R1      RANGE
# R2      RANGE RATE
# R3      THETA

W('43,2756', 0o02076, 'V83PERF', 'TC', 'TESTXACT', line=966)

W('43,2757', 0o34752, '', 'CAF', 'BIT2', line=968)
W('43,2760', 0o05203, '', 'TC', 'WAITLIST', line=969)
#   EBANK= TSTRT
W('43,2761', 0o03674, '', '2CADR', 'R31CALL', kind='data', line=971)
W('43,2762', 0o60107, kind='data', line=971)

W('43,2763', 0o05155, '', 'TC', 'ENDOFJOB', line=973)

# VERB 89       DESCRIPTION     RENDEZVOUS FINAL ATTITUDE ROUTINE (R63)
#
# CALLED BY VERB 89 ENTER DURING P00.  PRIO 10 IS USED.  CALCULATES AND
# DISPLAYS FINAL FDAI BALL ANGLES TO POINT LM +X OR +Z AXIS AT CSM.
#
# 1. KEY IN V 89 E ONLY IF IN PROG 00.  IF NOT IN P00, OPERATOR ERROR AND
# EXIT R63, OTHERWISE CONTINUE.
#
# 2. IF IN P00, DO IMU STATUS CHECK ROUTINE (R02BOTH).  IF IMU ON AND ITS
# ORIENTATION KNOWN TO LGC,CONTINUE.
#
# 3. FLASH DISPLAY V 04 N 06.  R2 INDICATES WHICH SPACECRAFT AXIS IS TO
# BE POINTED AT CSM.  INITIAL CHOICE IS PREFERRED (+Z) AXIS (R2=1).
# ASTRONAUT CAN CHANGE TO (+X) AXIS (R2 NOT = 1) BY V 22 E 2 E.  CONTINUE
# AFTER KEYING IN PROCEED.
#
# 4. BOTH VEHICLE STATE VECTORS UPDATED BY CONIC EQS.
#
# 5. HALF MAGNITUDE UNIT LOS VECTOR (IN STABLE MEMBER COORDINATES) AND
# Page 284
# HALF MAGNITUDE UNIT SPACECRAFT AXIS VECTOR (IN BODY COORDINATES)
# PREPARED FOR VECPOINT.
#
# 6. GIMBAL ANGLES FROM VECPOINT TRANSFORMED INTO FDAI BALL ANGLES BY
# BALLANGS.  FLASH DISPLAY V 06 N 18 AND AWAIT RESPONSE.
#
# 7.    RECYCLE -- RETURN TO STEP 4.
# TERMINATE -- EXIT R63.
# PROCEED -- RESET 3AXISFLG AND CALL R60LEM FOR ATTITUDE MANEUVER.

W('43,2764', 0o02123, 'V89PERF', 'TC', 'CHKPOOH', line=1005)
W('43,2765', 0o02076, '', 'TC', 'TESTXACT', line=1006)
W('43,2766', 0o34737, '', 'CAF', 'PRIO10', line=1007)
W('43,2767', 0o05105, '', 'TC', 'FINDVAC', line=1008)
#   EBANK= RONE
W('43,2770', 0o02022, '', '2CADR', 'V89CALL', kind='data', line=1010)
W('43,2771', 0o54104, kind='data', line=1010)

W('43,2772', 0o05155, '', 'TC', 'ENDOFJOB', line=1012)

# V90PERF       VERB 90         DESCRIPTION
# REQUEST RENDEZVOUS OUT-OF-PLANE DISPLAY (R36)
#
# 1.      SET EXT VERB DISPLAY BUSY FLAG.
# 2.      SCHEDULE R36 CALL WITH PRIORITY 10
# A.      DISPLAY
# TIME OF EVENT -- HOURS, MINUTES, SECONDS
# Y       OUT-OF-PLANE POSITION -- NAUTICAL MILES
# YDOT    OUT-OF-PLANE VELOCITY -- FEET/SECOND
# PSI     ANGLE BTW LINE OF SIGHT AND FORWARD
# DIRECTION VECTOR IN HORIZONTAL PLANE -- DEGREES

W('43,2773', 0o02076, 'V90PERF', 'TC', 'TESTXACT', line=1026)
W('43,2774', 0o35021, '', 'CAF', 'PRIO7', 'R36,V90', line=1027)
W('43,2775', 0o05105, '', 'TC', 'FINDVAC', line=1028)
#   EBANK= RPASS36
W('43,2776', 0o02656, '', '2CADR', 'R36', kind='data', line=1030)
W('43,2777', 0o10104, kind='data', line=1030)

W('43,3000', 0o15155, '', 'TCF', 'ENDOFJOB', line=1032)

# MINIMP        VERB 76         DESCRIPTION
# MINIMUM IMPULSE MODE
#
# 1.      SET MINIMUM IMPULSE RHO MODE FLAG TO 1.

W('43,3001', 0o00004, 'MINIMP', 'INHINT', line=1039)
W('43,3002', 0o40111, '', 'CS', 'DAPBOOLS', line=1040)
W('43,3003', 0o74735, '', 'MASK', 'PULSES', 'PULSES = 1 INDICATES MIN IMP MODE', line=1041)
W('43,3004', 0o26111, '', 'ADS', 'DAPBOOLS', line=1042)
W('43,3005', 0o12121, '', 'TCF', 'GOPIN', 'RETURN VIA PINBRNCH', line=1043)

# NOMINIMP      VERB 77         DESCRIPTION
# RATE COMMAND MODE

# Page 285

#
# 1.      SET MINIMUM IMPULSE RHO MODE FLAG TO 0.  (ZERO INDICATES NOT MINIMUM IMPULSE MODE.).
# 2.      MOVE CDUX, CDUY, CDUZ INTO CDUXD, CDUYD, CDUZD.

W('43,3006', 0o00004, 'NOMINIMP', 'INHINT', line=1055)
W('43,3007', 0o44735, '', 'CS', 'PULSES', line=1056)
W('43,3010', 0o70111, '', 'MASK', 'DAPBOOLS', line=1057)
W('43,3011', 0o54111, '', 'TS', 'DAPBOOLS', 'PULSES = NOT IN MINIMUM UMPULSE MODE', line=1058)
W('43,3012', 0o04674, '', 'TC', 'IBNKCALL', line=1059)
W('43,3013', 0o40153, '', 'CADR', 'ZATTEROR', kind='data', line=1060)
W('43,3014', 0o02121, '', 'TC', 'GOPIN', line=1061)

# Page 286
# CREMANU       VERB 49         DESCRIPTION
# START AUTOMATIC ATTITUDE MANEUVER
#
# 1.      REQUIRE PROGRAM 00 ACTIVE.
# 2.      SET EXT VERB DISPLAY BUSY FLAG.
# 3.      SCHEDULE R62DISP WITH PRIORITY 10.
# 4.      RELEASE EXT VERB DISPLAY.
#
# R62DISP
# 1.      DISPLAY FLASHING V06,N22.
# RESPONSES
# A.      TERMINATE
# 1.      GOTOPOOH
# B.      PROCEED
# 1.      SET 3AXISFLG TO INDICATE MANEUVER IS SPECIFIED BY 3 AXIS.
# 2.      EXECUTE R60LEM (ATTITUDE MANEUVER).
# C.      ENTER
# 1.      REPEAT FLASHING V06,N22.

W('43,3015', 0o02123, 'CREWMANU', 'TC', 'CHKPOOH', 'DEMAND P00', line=1083)

W('43,3016', 0o02076, '', 'TC', 'TESTXACT', line=1085)

W('43,3017', 0o34737, '', 'CAF', 'PRIO10', line=1087)
W('43,3020', 0o05105, '', 'TC', 'FINDVAC', line=1088)
#   EBANK= BCDU
W('43,3021', 0o02103, '', '2CADR', 'R62DISP', kind='data', line=1090)
W('43,3022', 0o46106, kind='data', line=1090)

W('43,3023', 0o05155, '', 'TC', 'ENDOFJOB', line=1092)

# Page 287
# TRMTRACK      VERB 56         DESCRIPTION
# TERMINATE TRACKING (P20 AND P25).
#
# 1.      KNOCK DOWN RENDEZVOUS, TRACK, AND UPDATE FLAGS.
# 2.      REQUIRE P20 OR P25 NOT RUNNING ALONE OR GO TO GOGOPOOH (REQUEST PROGRAM 00).
# 3.      SCHEDULE V56TOVAC WITH PRIORITY 30.
#
# V56TOVAC
# 1.      EXECUTE INTSTALL (IF INTEGRATION IS RUNNING, STALL UNTIL IT IS FINISHED.).
# 2.      ZERO GROUP 2 TO HALT P20.
# 3.      TRANSFER CONTROL TO GOPROG2 (SOFTWARE RESTART).

W('43,3024', 0o33044, 'TRMTRACK', 'CA', 'BITS9+7', 'IS REND OR P25 FLAG ON', line=1107)
W('43,3025', 0o70074, '', 'MASK', 'FLAGWRD0', line=1108)
W('43,3026', 0o00006, '', 'EXTEND', line=1109)
W('43,3027', 0o12121, '', 'BZF', 'GOPIN', 'NO', line=1110)

W('43,3030', 0o05516, '', 'TC', 'DOWNFLAG', line=1112)
W('43,3031', 0o00010, '', 'ADRES', 'RNDVZFLG', kind='data', line=1113)

W('43,3032', 0o05516, '', 'TC', 'DOWNFLAG', line=1115)
W('43,3033', 0o00006, '', 'ADRES', 'P25FLAG', kind='data', line=1116)

W('43,3034', 0o05516, '', 'TC', 'DOWNFLAG', 'ENSURE SEARCH FLAG IS OFF', line=1118)
W('43,3035', 0o00037, '', 'ADRES', 'SRCHOPTN', kind='data', line=1119)

W('43,3036', 0o34747, '', 'CA', 'TRACKBIT', 'IS TRACK FLAG ON?', line=1121)
W('43,3037', 0o70075, '', 'MASK', 'FLAGWRD1', line=1122)
W('43,3040', 0o00006, '', 'EXTEND', line=1123)
W('43,3041', 0o12121, '', 'BZF', 'GOPIN', line=1124)

W('43,3042', 0o04635, '', 'TC', 'POSTJUMP', line=1126)
W('43,3043', 0o64054, '', 'CADR', 'TRMTRAK1', kind='data', line=1127)

W('43,3044', 0o00500, 'BITS9+7', 'OCT', '500', kind='data', line=1129)

#   SETLOC SBAND  # BANK 42
#   BANK

#   COUNT* $$/EXTVB

W('42,2054', 0o05516, 'TRMTRAK1', 'TC', 'DOWNFLAG', line=1136)
W('42,2055', 0o00027, '', 'ADRES', 'UPDATFLG', 'UPDATE FLAG DOWN', kind='data', line=1137)
W('42,2056', 0o05516, '', 'TC', 'DOWNFLAG', line=1138)
W('42,2057', 0o00031, '', 'ADRES', 'TRACKFLG', 'TRACK FLAG DOWN', kind='data', line=1139)
W('42,2060', 0o05516, '', 'TC', 'DOWNFLAG', line=1140)
W('42,2061', 0o00007, '', 'ADRES', 'IMUSE', kind='data', line=1141)

W('42,2062', 0o06037, '', 'TC', 'INTPRET', line=1143)
W('42,2063', 0o77624, '', 'CALL', kind='interp', line=1144)
W('42,2064', 0o27414, '', '', 'INTSTALL', "DON'T INTERRUPT INTEGRATION", kind='operand', line=1145)
# Page 288
W('42,2065', 0o77776, '', 'EXIT', kind='interp', line=1147)

W('42,2066', 0o05353, '', 'TC', 'PHASCHNG', line=1149)
W('42,2067', 0o00002, '', 'OCT', '2', 'KILL GROUP 2 TO HALT P20 ACTIVITY', kind='data', line=1150)

W('42,2070', 0o00004, '', 'INHINT', line=1152)
W('42,2071', 0o04674, '', 'TC', 'IBNKCALL', 'ZERO THE COMMANDED RATES TO STOP', line=1153)
W('42,2072', 0o40165, '', 'CADR', 'STOPRATE', 'MANEUVER', kind='data', line=1154)

W('42,2073', 0o04674, '', 'TC', 'IBNKCALL', line=1156)
W('42,2074', 0o40123, '', 'CADR', 'RESTORDB', kind='data', line=1157)

W('42,2075', 0o06011, '', 'TC', 'CLRADMOD', 'CLEAR BITS 10 + 15 OF RADMODES.', line=1159)

W('42,2076', 0o44736, '', 'CS', 'BIT14', 'DISABLE LOCKON', line=1161)
W('42,2077', 0o00006, '', 'EXTEND', line=1162)
W('42,2100', 0o03012, '', 'WAND', 'CHAN12', line=1163)
W('42,2101', 0o04635, '', 'TC', 'POSTJUMP', line=1164)
W('42,2102', 0o12770, '', 'CADR', 'GOPROG2', 'CAUSE RESTART.', kind='data', line=1165)

# DNEDUMP       VERB 74         DESCRIPTION
# INITIALZE DOWN-TELEMETRY PROGRAM FOR ERASABLE MEMORY DUMP.
#
# 1.      SET EXT VERB DISPLAY BUSY FLAG.
# 2.      REPLACE CURRENT DOWNLIST WITH ERASABLE MEMORY.
# 3.      RELEASE EXT VERB DISPLAY.

#   SETLOC EXTVERBS
#   BANK

#   COUNT* $$/EXTVB

#   EBANK= 400
W('43,3045', 0o33050, 'DNEDUMP', 'CAF', 'LDNDUMPI', line=1180)
W('43,3046', 0o54335, '', 'TS', 'DNTMGOTO', line=1181)
W('43,3047', 0o02121, '', 'TC', 'GOPIN', line=1182)

S('V74', 'equals', 0o117045, line=1184)
W('43,3050', 0o03707, 'LDNDUMPI', 'REMADR', 'DNDUMPI', kind='data', line=1185)

# LEMVEC        VERB 80         DESCRIPTION
# UPDATE LEM STATE VECTOR
# RESET VHUPFLG TC 0

W('43,3051', 0o05516, 'LEMVEC', 'TC', 'DOWNFLAG', line=1191)
W('43,3052', 0o00026, '', 'ADRES', 'VEHUPFLG', 'VB 80 -- VEHUPFLG DOWN INDICATES LEM', kind='data', line=1192)

W('43,3053', 0o03056, '', 'TC', 'NOUPDOWN', line=1194)

# CSMVEC        VERB 81         DESCRIPTION
# UPDATE CSM STATE VECTOR
# Page 289
# SET VEHUPFLG TO 1

W('43,3054', 0o05504, 'CSMVEC', 'TC', 'UPFLAG', line=1201)
W('43,3055', 0o00026, '', 'ADRES', 'VEHUPFLG', 'VB 81 -- VEHUPFLG UP INDICATES CSM', kind='data', line=1202)

W('43,3056', 0o05516, 'NOUPDOWN', 'TC', 'DOWNFLAG', line=1204)
W('43,3057', 0o00030, '', 'ADRES', 'NOUPFLAG', kind='data', line=1205)

W('43,3060', 0o12121, '', 'TCF', 'GOPIN', line=1207)

# UPDATOFF      VERB 95         DESCRIPTION
# INHIBIT STATE VECTOR UPDATES BY INCORP
# SET NOUPFLAG TO 1

W('43,3061', 0o05504, 'UPDATOFF', 'TC', 'UPFLAG', 'VB 95 SET NOUPFLAG', line=1213)
W('43,3062', 0o00030, '', 'ADRES', 'NOUPFLAG', kind='data', line=1214)

W('43,3063', 0o02121, '', 'TC', 'GOPIN', line=1216)
# Page 290
# SYSTEST       VERB 92         DESCRIPTION
# OPERATE IMU PERFORMANCE TEST.
#
# 1.      REQUIRE PROGRAM 00 OR TURN ON OPERATOR ERROR.
# 2.      SET EXT VERB BUSY FLAG.

#   EBANK= QPLACE

W('43,3064', 0o02123, 'SYSTEST', 'TC', 'CHKPOOH', 'DEMAND P00', line=1226)

W('43,3065', 0o02076, '', 'TC', 'TESTXACT', line=1228)

W('43,3066', 0o37710, '', 'CAF', 'PRIO22', line=1230)
W('43,3067', 0o05105, '', 'TC', 'FINDVAC', line=1231)
#   EBANK= QPLACE
#   SBANK= IMUSUPER
W('43,3070', 0o02002, '', '2CADR', 'REDO', kind='data', line=1234)
W('43,3071', 0o76065, kind='data', line=1234)

W('43,3072', 0o05155, '', 'TC', 'ENDOFJOB', line=1236)

# VERB 93       CLEAR RENDWFLG, CAUSES W-MATRIX TO BE RE-INITIALIZED.

W('43,3073', 0o00004, 'WMATRXNG', 'INHINT', line=1240)
W('43,3074', 0o44753, '', 'CS', 'RENDWBIT', line=1241)
W('43,3075', 0o70101, '', 'MASK', 'FLAGWRD5', line=1242)
W('43,3076', 0o54101, '', 'TS', 'FLAGWRD5', line=1243)

W('43,3077', 0o02121, '', 'TC', 'GOPIN', line=1245)

S('GOSHOSUM', 'equals', 0o117100, line=1247)

W('43,3100', 0o02123, 'SHOWSUM', 'TC', 'CHKPOOH', '*', line=1249)
W('43,3101', 0o02076, '', 'TC', 'TESTXACT', '*', line=1250)
W('43,3102', 0o35021, '', 'CAF', 'PRIO7', '* ALLOW OTHER CHARINS.', line=1251)
W('43,3103', 0o05146, '', 'TC', 'PRIOCHNG', '*', line=1252)
W('43,3104', 0o34753, '', 'CAF', 'S+1', '*', line=1253)
W('43,3105', 0o55376, '', 'TS', 'SKEEP6', '* SHOWSUM OPTION', line=1254)
W('43,3106', 0o34755, '', 'CAF', 'S+ZERO', '*', line=1255)
W('43,3107', 0o55362, '', 'TS', 'SMODE', '* TURN OFF SELF-CHECK', line=1256)
W('43,3110', 0o33245, '', 'CA', 'SELFADRS', '*', line=1257)
W('43,3111', 0o55361, '', 'TS', 'SELFRET', '*', line=1258)
W('43,3112', 0o03522, '', 'TC', 'STSHOSUM', '* ENTER ROPECHK', line=1259)

W('43,3113', 0o23372, 'SDISPLAY', 'LXCH', 'SKEEP2', '* BANK # FOR DISPLAY', line=1261)
W('43,3114', 0o23373, '', 'LXCH', 'SKEEP3', '* BUGGER WORD FOR DISPLAY', line=1262)
W('43,3115', 0o33244, 'NOKILL', 'CA', 'ADRS1', '*', line=1263)
W('43,3116', 0o54156, '', 'TS', 'MPAC +2', '*', line=1264)
W('43,3117', 0o33130, '', 'CA', 'VNCON', '* 0501', line=1265)
W('43,3120', 0o04616, '', 'TC', 'BANKCALL', '*', line=1266)
W('43,3121', 0o20334, '', 'CADR', 'GOXDSPF', '*', kind='data', line=1267)
W('43,3122', 0o03125, '', 'TC', '+3', '*', line=1268)
W('43,3123', 0o03633, '', 'TC', 'NXTBNK', '*', line=1269)
# Page 291
W('43,3124', 0o03115, '', 'TC', 'NOKILL', '*', line=1271)
W('43,3125', 0o33245, '', 'CA', 'SELFADRS', line=1272)
W('43,3126', 0o55371, '', 'TS', 'SKEEP1', line=1273)

W('43,3127', 0o05472, '', 'TC', 'ENDEXT', '*', line=1275)
W('43,3130', 0o01201, 'VNCON', 'VN', '501', '*', kind='data', line=1276)
W('43,3131', 0o31376, 'ENDSUMS', 'CA', 'SKEEP6', '*', line=1277)
W('43,3132', 0o00006, '', 'EXTEND', '', '*', line=1278)
W('43,3133', 0o13336, '', 'BZF', 'SELFCHK', '* ROPECHK, START SELFCHK AGAIN.', line=1279)
W('43,3134', 0o03522, '', 'TC', 'STSHOSUM', '* START SHOWSUM AGAIN.', line=1280)

# Page 292
# DAPDISP       VERB 48         DESCRIPTION
# LOAD AUTO PILOT DATA
#
# 1.      REQUIRE EXT VERB DISPLAY AVAILABLE AND SET BUSY FLAG.
# 2.      EXECUTE DAPDATA1, DAPDATA2, AND DAPDATA3.
# 3.      RELEASE EXT VERB DISPLAY SYSTEM.

W('43,3135', 0o02076, 'DAPDISP', 'TC', 'TESTXACT', line=1290)
W('43,3136', 0o35021, '', 'CAF', 'PRIO7', 'R03', line=1291)
W('43,3137', 0o05146, '', 'TC', 'PRIOCHNG', line=1292)
W('43,3140', 0o04635, '', 'TC', 'POSTJUMP', line=1293)
W('43,3141', 0o40004, '', 'CADR', 'DAPDATA1', kind='data', line=1294)

#   BANK 34
#   SETLOC LOADDAP
#   BANK

#   COUNT* $$/R03

#   SBANK= LOWSUPER  # FOR SUBSEQUENT LOW 2CADR'S

W('20,2004', 0o32114, 'DAPDATA1', 'CAF', 'BOOLSMSK', 'SET DISPLAY ACCORDING TO DAPBOOLS BITS.', line=1304)
W('20,2005', 0o70111, '', 'MASK', 'DAPBOOLS', 'LM', line=1305)
W('20,2006', 0o55343, '', 'TS', 'DAPDATR1', 'LM', line=1306)
W('20,2007', 0o40106, '', 'CS', 'FLGWRD10', 'SET BIT 14 TO BE COMPLEMENT OF APSFLAG.', line=1307)
W('20,2010', 0o74737, '', 'MASK', 'APSFLBIT', line=1308)
W('20,2011', 0o10000, '', 'CCS', 'A', line=1309)
W('20,2012', 0o34736, '', 'CAF', 'BIT14', line=1310)
W('20,2013', 0o27343, '', 'ADS', 'DAPDATR1', line=1311)
W('20,2014', 0o31343, 'CHKDATA1', 'CAE', 'DAPDATR1', 'IF BITS 13 AND 14 ARE BOTH ZERO, FORCE', line=1312)
W('20,2015', 0o74355, '', 'MASK', 'BIT13-14', '      A ONE INTO BIT 13.', line=1313)
W('20,2016', 0o00006, '', 'EXTEND', line=1314)
W('20,2017', 0o12034, '', 'BZF', 'FORCEONE', line=1315)
W('20,2020', 0o31343, '', 'CAE', 'DAPDATR1', 'ENSURE THAT NO ILLEGAL BITS SET BY CREW.', line=1316)
W('20,2021', 0o72113, 'MSKDATR1', 'MASK', 'DSPLYMSK', line=1317)
W('20,2022', 0o55343, '', 'TS', 'DAPDATR1', line=1318)
W('20,2023', 0o32112, '', 'CAF', 'V01N46', 'LM', line=1319)
W('20,2024', 0o04616, '', 'TC', 'BANKCALL', line=1320)
W('20,2025', 0o20353, '', 'CADR', 'GOXDSPFR', kind='data', line=1321)
W('20,2026', 0o15472, '', 'TCF', 'ENDEXT', 'V34E TERMINATE', line=1322)
W('20,2027', 0o12037, '', 'TCF', 'DPDAT1', 'V33E PROCEED', line=1323)
W('20,2030', 0o12014, '', 'TCF', 'CHKDATA1', 'E     NEW DATA        CHECK AND REDISPLAY', line=1324)
W('20,2031', 0o36242, '', 'CAF', 'REVCNT', 'BITS 2 & 3:  BLANKS R2 & R3.', line=1325)
W('20,2032', 0o05464, '', 'TC', 'BLANKET', line=1326)
W('20,2033', 0o15155, '', 'TCF', 'ENDOFJOB', line=1327)
W('20,2034', 0o34737, 'FORCEONE', 'CAF', 'BIT13', line=1328)
W('20,2035', 0o27343, '', 'ADS', 'DAPDATR1', line=1329)
W('20,2036', 0o12021, '', 'TCF', 'MSKDATR1', line=1330)

W('20,2037', 0o00004, 'DPDAT1', 'INHINT', '', 'INHINT FOR SETTING OF FLAG BITS AND MASS', line=1332)
W('20,2040', 0o44737, '', 'CS', 'APSFLBIT', '      ON BASIS OF DISPLAYED DAPDATR1.', line=1333)
W('20,2041', 0o70106, '', 'MASK', 'FLGWRD10', line=1334)
W('20,2042', 0o54001, '', 'TS', 'L', 'SET APSFLAG TO BE COMPLEMENT OF BIT 14.', line=1335)
# Page 293
W('20,2043', 0o41343, '', 'CS', 'DAPDATR1', line=1337)
W('20,2044', 0o74736, '', 'MASK', 'BIT14', line=1338)
W('20,2045', 0o10000, '', 'CCS', 'A', line=1339)
W('20,2046', 0o34737, '', 'CAF', 'APSFLBIT', line=1340)
W('20,2047', 0o60001, '', 'AD', 'L', line=1341)
W('20,2050', 0o54106, '', 'TS', 'FLGWRD10', line=1342)
W('20,2051', 0o41343, '', 'CS', 'DAPDATR1', 'SET BITS OF DAPBOOLS ON BASIS OF DISPLAY', line=1343)
W('20,2052', 0o74355, '', 'MASK', 'BIT13-14', '      MASK OUT CSMDOCKD (BIT 13) UNLESS BOTH', line=1344)
W('20,2053', 0o10000, '', 'CCS', 'A', '      13 AND 14 ARE SET.', line=1345)
W('20,2054', 0o44737, '', 'CS', 'CSMDOCKD', line=1346)
W('20,2055', 0o62114, '', 'AD', 'BOOLSMSK', line=1347)
W('20,2056', 0o71343, '', 'MASK', 'DAPDATR1', line=1348)
W('20,2057', 0o54001, '', 'TS', 'L', line=1349)
W('20,2060', 0o42114, '', 'CS', 'BOOLSMSK', line=1350)
W('20,2061', 0o70111, '', 'MASK', 'DAPBOOLS', line=1351)
W('20,2062', 0o60001, '', 'AD', 'L', line=1352)
W('20,2063', 0o54111, '', 'TS', 'DAPBOOLS', line=1353)
W('20,2064', 0o74737, '', 'MASK', 'CSMDOCKD', 'LOAD MASS IN ACCORDANCE WITH CSMDOCKD.', line=1354)
W('20,2065', 0o10000, '', 'CCS', 'A', '      MASS IS USUALLY OKAY, SO DO', line=1355)
W('20,2066', 0o31332, '', 'CAE', 'CSMMASS', '      NOT TOUCH ITS LOW-ORDER PART.', line=1356)
W('20,2067', 0o61331, '', 'AD', 'LEMMASS', line=1357)
W('20,2070', 0o55244, '', 'TS', 'MASS', line=1358)
W('20,2071', 0o30111, '', 'CAE', 'DAPBOOLS', line=1359)
W('20,2072', 0o74741, '', 'MASK', 'ACC4OR2X', '2 OR 4 JET X-TRANSLATION', line=1360)
W('20,2073', 0o00006, '', 'EXTEND', '', '(BIT ACC4OR2X = 1 FOR 4 JETS)', line=1361)
W('20,2074', 0o12101, '', 'BZF', '+5', line=1362)
W('20,2075', 0o44735, '', 'CS', 'BIT15', line=1363)
W('20,2076', 0o70075, '', 'MASK', 'FLAGWRD1', 'CLEAR NJTSFLAG TO 0 FOR 4 JETS', line=1364)
W('20,2077', 0o54075, '', 'TS', 'FLAGWRD1', line=1365)
W('20,2100', 0o12104, '', 'TCF', '+4', line=1366)
W('20,2101', 0o40075, '', 'CS', 'FLAGWRD1', 'SET NJTSFLAG TO 1 FOR 2 JETS', line=1367)
W('20,2102', 0o74735, '', 'MASK', 'BIT15', line=1368)
W('20,2103', 0o26075, '', 'ADS', 'FLAGWRD1', line=1369)
W('20,2104', 0o30111, '', 'CA', 'DAPBOOLS', 'SELECT DESIRED KALCMANU AUTOMATIC', line=1370)
W('20,2105', 0o76245, '', 'MASK', 'THREE', 'MANEUVER RATE', line=1371)
W('20,2106', 0o60000, '', 'DOUBLE', '', 'RATEINDX HAS TO BE 0,2,4,6 SINCE RATES', line=1372)
W('20,2107', 0o55325, '', 'TS', 'RATEINDX', 'ARE DP', line=1373)
W('20,2110', 0o04635, '', 'TC', 'POSTJUMP', line=1374)
W('20,2111', 0o02206, '', 'CADR', 'STIKLOAD', kind='data', line=1375)

W('20,2112', 0o00256, 'V01N46', 'VN', '0146', kind='data', line=1377)
W('20,2113', 0o33113, 'DSPLYMSK', 'OCT', '33113', kind='data', line=1378)
W('20,2114', 0o13113, 'BOOLSMSK', 'OCT', '13113', kind='data', line=1379)

#   BANK 01
#   SETLOC LOADDAP1
#   BANK

#   COUNT* $$/R03

W('01,2206', 0o35015, 'STIKLOAD', 'CAF', 'EBANK6', line=1387)
# Page 294
W('01,2207', 0o54003, '', 'TS', 'EBANK', line=1389)
#   EBANK= STIKSENS
W('01,2210', 0o34745, '', 'CA', 'RHCSCALE', 'SET STICK SENSITIVITY TO CORRESPOND TO A', line=1391)
W('01,2211', 0o70111, '', 'MASK', 'DAPBOOLS', 'MAXIMUM COMMANDED RATE (AT 42 COUNTS) OF', line=1392)
W('01,2212', 0o10000, '', 'CCS', 'A', '20 D/S (NORMAL) OR 4 D/S (FINE), SCALED', line=1393)
W('01,2213', 0o32337, '', 'CA', 'NORMAL', 'AT 45 D/S.', line=1394)
W('01,2214', 0o62340, '', 'AD', 'FINE', line=1395)
W('01,2215', 0o55444, '', 'TS', 'STIKSENS', line=1396)
W('01,2216', 0o32342, '', 'CA', '-0.6D/S', line=1397)
W('01,2217', 0o55476, '', 'TS', '-RATEDB', 'LM-ONLY BREAKOUT LEVEL IS .6 D/S.', line=1398)
W('01,2220', 0o34737, '', 'CA', 'CSMDOCKD', 'IF CSM-DOCKED, DIVIDE STICK SENSITIVITY', line=1399)
W('01,2221', 0o70111, '', 'MASK', 'DAPBOOLS', 'BY 10.  NORMAL SCALING IS THEN 2 D/S AND', line=1400)
W('01,2222', 0o00006, '', 'EXTEND', '', 'FINE SCALING IS 0.4 D/S', line=1401)
W('01,2223', 0o12232, '', 'BZF', '+7', 'BRANCH IF CSM IS NOT DOCKED.', line=1402)
W('01,2224', 0o31444, '', 'CA', 'STIKSENS', line=1403)
W('01,2225', 0o00006, '', 'EXTEND', line=1404)
W('01,2226', 0o72341, '', 'MP', '1/10', line=1405)
W('01,2227', 0o55444, '', 'TS', 'STIKSENS', line=1406)
W('01,2230', 0o32343, '', 'CA', '-0.3D/S', 'CSM-DOCKED BREAKOUT LEVEL IS .3 D/S.', line=1407)
W('01,2231', 0o55476, '', 'TS', '-RATEDB', line=1408)
W('01,2232', 0o00003, '', 'RELINT', '', 'PROCEED TO NOUN 47, MASS LOAD.', line=1409)

W('01,2233', 0o32334, 'DAPDATA2', 'CAF', 'V0647', line=1411)
W('01,2234', 0o04616, '', 'TC', 'BANKCALL', line=1412)
W('01,2235', 0o20353, '', 'CADR', 'GOXDSPFR', kind='data', line=1413)
W('01,2236', 0o12244, '', 'TCF', 'ENDR03', 'V34E  TERMINATE. FIRST SET DB.  DO 1/ACCS', line=1414)
W('01,2237', 0o12250, '', 'TCF', 'DAPDAT2', 'V33E  PROCEED', line=1415)
W('01,2240', 0o12233, '', 'TCF', 'DAPDATA2', '      LOAD NEW DATA AND RECYCLE', line=1416)
W('01,2241', 0o34751, '', 'CAF', 'BIT3', 'BLANKS R3', line=1417)
W('01,2242', 0o05464, '', 'TC', 'BLANKET', '              LM', line=1418)
W('01,2243', 0o15155, '', 'TCF', 'ENDOFJOB', line=1419)
W('01,2244', 0o00004, 'ENDR03', 'INHINT', line=1420)
W('01,2245', 0o04674, '', 'TC', 'IBNKCALL', line=1421)
W('01,2246', 0o40123, '', 'CADR', 'RESTORDB', kind='data', line=1422)
W('01,2247', 0o15472, '', 'TCF', 'ENDEXT', 'DOES RELINT', line=1423)

W('01,2250', 0o40106, 'DAPDAT2', 'CS', 'FLGWRD10', 'DETERMINE STAGE FROM APSFLAG', line=1425)
W('01,2251', 0o74737, '', 'MASK', 'APSFLBIT', line=1426)
W('01,2252', 0o10000, '', 'CCS', 'A', line=1427)
W('01,2253', 0o32000, '', 'CA', 'MINLMD', line=1428)
W('01,2254', 0o62001, '', 'AD', 'MINMINLM', line=1429)
W('01,2255', 0o61331, '', 'AD', 'LEMMASS', 'LEMMASS MUST BE GREATER THAN EMPTY LEM', line=1430)
W('01,2256', 0o00006, '', 'EXTEND', line=1431)
W('01,2257', 0o62233, '', 'BZMF', 'DAPDATA2', 'ASK FOR NEW MASSES', line=1432)
W('01,2260', 0o30111, '', 'CAE', 'DAPBOOLS', line=1433)
W('01,2261', 0o74737, '', 'MASK', 'CSMDOCKD', line=1434)
W('01,2262', 0o00006, '', 'EXTEND', line=1435)
W('01,2263', 0o12271, '', 'BZF', 'LEMALONE', 'SKIP TEST ON CSMMASS IF NOT DOCKED.', line=1436)
W('01,2264', 0o44741, '', 'CS', 'MINCSM', 'TEST CSM MASS', line=1437)
W('01,2265', 0o61332, '', 'AD', 'CSMMASS', 'CSMMASS MUST BE GREATER THAN EMPTY CSM', line=1438)
# Page 295
W('01,2266', 0o00006, '', 'EXTEND', line=1440)
W('01,2267', 0o62233, '', 'BZMF', 'DAPDATA2', 'ASK FOR NEW MASSES', line=1441)
W('01,2270', 0o31332, '', 'CAE', 'CSMMASS', 'DOCKED:  MASS = CSMMASS + LEMMASS', line=1442)
W('01,2271', 0o61331, 'LEMALONE', 'AD', 'LEMMASS', 'LEM ALONE:  MASS = LEMMASS', line=1443)
W('01,2272', 0o22007, '', 'ZL', line=1444)
W('01,2273', 0o53245, '', 'DXCH', 'MASS', line=1445)
W('01,2274', 0o00004, '', 'INHINT', line=1446)
W('01,2275', 0o04674, '', 'TC', 'IBNKCALL', 'SET DEADBANK AND COMPUTE MOMENTS OF', line=1447)
W('01,2276', 0o40123, '', 'CADR', 'RESTORDB', '      INERTIA.', kind='data', line=1448)
W('01,2277', 0o00003, '', 'RELINT', '', 'PROCEED TO NOUN 48 (OR END).', line=1449)

W('01,2300', 0o40106, 'DAPDATA3', 'CS', 'FLGWRD10', line=1451)
W('01,2301', 0o74737, '', 'MASK', 'APSFLBIT', line=1452)
W('01,2302', 0o00006, '', 'EXTEND', '', 'END ROUTINE IF LEM HAS STAGED.', line=1453)
W('01,2303', 0o15472, '', 'BZF', 'ENDEXT', line=1454)
W('01,2304', 0o32335, '', 'CAF', 'V06N48', 'DISPLAY TRIM ANGLES AND REQUEST RESPONSE', line=1455)
W('01,2305', 0o04616, '', 'TC', 'BANKCALL', line=1456)
W('01,2306', 0o20353, '', 'CADR', 'GOXDSPFR', kind='data', line=1457)
W('01,2307', 0o05472, '', 'TC', 'ENDEXT', line=1458)
W('01,2310', 0o12315, '', 'TCF', 'DPDAT3', 'V33E GO DO TRIM (WAITLIST TO TRIMGIMB)', line=1459)
W('01,2311', 0o12304, '', 'TCF', '-5', 'LOAD NEW DATA AND RECYCLE', line=1460)
W('01,2312', 0o34751, '', 'CAF', 'BIT3', line=1461)
W('01,2313', 0o05464, '', 'TC', 'BLANKET', 'BLANK R3', line=1462)
W('01,2314', 0o15155, '', 'TCF', 'ENDOFJOB', line=1463)
W('01,2315', 0o34753, 'DPDAT3', 'CAF', 'BIT1', 'GO TO TRIMGIMB VIA WAITLIST SO IT', line=1464)
W('01,2316', 0o00004, '', 'INHINT', '', 'CAN USE FIXDELAY AND VARDELAY', line=1465)
W('01,2317', 0o05203, '', 'TC', 'WAITLIST', line=1466)
#   EBANK= ROLLTIME
W('01,2320', 0o03217, '', '2CADR', 'TRIMGIMB', kind='data', line=1468)
W('01,2321', 0o56066, kind='data', line=1468)

W('01,2322', 0o15155, '', 'TCF', 'ENDOFJOB', 'DOES A RELINT', line=1470)
W('01,2323', 0o32336, 'TRIMDONE', 'CAF', 'V50N48', line=1471)
W('01,2324', 0o04616, '', 'TC', 'BANKCALL', 'TRIM IS FINISHED; PLEASE TERMINATE R03', line=1472)
W('01,2325', 0o20361, '', 'CADR', 'GOMARK3R', kind='data', line=1473)
W('01,2326', 0o05472, '', 'TC', 'ENDEXT', 'V34E TERMINATE', line=1474)
W('01,2327', 0o05472, '', 'TC', 'ENDEXT', line=1475)
W('01,2330', 0o05472, '', 'TC', 'ENDEXT', line=1476)
W('01,2331', 0o36007, '', 'CAF', 'OCT24', 'BIT5 TO CHANGE TO PERFORM, 3 TO BLANK 43', line=1477)
W('01,2332', 0o05464, '', 'TC', 'BLANKET', line=1478)
W('01,2333', 0o15155, '', 'TCF', 'ENDOFJOB', line=1479)

W('01,2334', 0o01457, 'V0647', 'VN', '0647', kind='data', line=1481)
W('01,2335', 0o01460, 'V06N48', 'VN', '0648', kind='data', line=1482)

W('01,2336', 0o14460, 'V50N48', 'VN', '5048', kind='data', line=1484)
W('01,2337', 0o25101, 'NORMAL', 'DEC', '.660214', kind='data', line=1485)
# NORMAL SCALING IS 20 D/S
W('01,2340', 0o05220, 'FINE', 'DEC', '.165054', 'FINE STICK SCALING (4 D/S).', kind='data', line=1487)
W('01,2341', 0o03146, '1/10', 'DEC', '.1', 'FACTOR FOR CSM-DOCKED SCALING', kind='data', line=1488)
W('01,2342', 0o77445, '-0.6D/S', 'DEC', '-218', kind='data', line=1489)

# Page 296

W('01,2343', 0o77622, '-0.3D/S', 'DEC', '-109', kind='data', line=1493)

# Page 297
# VERB 66       VEHICLES ARE ATTACHED. MOVE THIS VEHICLE STATE VECTOR TO
# OTHER VEHICLE STATE VECTOR.
#
# USE SUBROUTINE GENTRAN.

#   BANK 7
#   SETLOC EXTVERBS
#   BANK

#   COUNT* $$/EXTVB

#   EBANK= RRECTHIS

W('43,3142', 0o34737, 'ATTACHED', 'CAF', 'PRIO10', line=1509)
W('43,3143', 0o05105, '', 'TC', 'FINDVAC', line=1510)
#   EBANK= RRECTHIS

W('43,3144', 0o03147, '', '2CADR', 'ATTACHIT', kind='data', line=1513)
W('43,3145', 0o66103, kind='data', line=1513)

W('43,3146', 0o05155, '', 'TC', 'ENDOFJOB', line=1515)

W('43,3147', 0o06037, 'ATTACHIT', 'TC', 'INTPRET', line=1517)
W('43,3150', 0o77624, '', 'CALL', kind='interp', line=1518)
W('43,3151', 0o27414, '', '', 'INTSTALL', kind='operand', line=1519)
W('43,3152', 0o43014, '', 'SET', 'BON', kind='interp', line=1520)
W('43,3153', 0o04063, '', '', 'MOONOTH', kind='operand', line=1521)
W('43,3154', 0o04304, '', '', 'MOONTHIS', kind='operand', line=1522)
W('43,3155', 0o67160, '', '', '+3', kind='operand', line=1523)
W('43,3156', 0o77614, '', 'CLEAR', kind='interp', line=1524)
W('43,3157', 0o04263, '', '', 'MOONOTH', kind='operand', line=1525)
W('43,3160', 0o77776, '', 'EXIT', kind='interp', line=1526)
W('43,3161', 0o33204, '', 'CAF', 'OCT51', line=1527)
W('43,3162', 0o05544, '', 'TC', 'GENTRAN', line=1528)
W('43,3163', 0o01626, '', 'ADRES', 'RRECTHIS', 'OUR STATE VECTOR INTO OTHER VIA GENTRAN', kind='data', line=1529)
W('43,3164', 0o01554, '', 'ADRES', 'RRECTOTH', kind='data', line=1530)

W('43,3165', 0o00003, '', 'RELINT', line=1532)
W('43,3166', 0o06037, '', 'TC', 'INTPRET', line=1533)
W('43,3167', 0o77624, '', 'CALL', '', 'UPDATE R-OTHER, V-OTHER', kind='interp', line=1534)
W('43,3170', 0o26760, '', '', 'PTOALEM', kind='operand', line=1535)
W('43,3171', 0o45154, '', 'LXA,2', 'CALL', kind='interp', line=1536)
W('43,3172', 0o02030, '', '', 'PBODY', kind='operand', line=1537)
W('43,3173', 0o26114, '', '', 'SVDWN1', kind='operand', line=1538)
W('43,3174', 0o77776, '', 'EXIT', kind='interp', line=1539)

W('43,3175', 0o33205, '', 'CAF', 'TCPINAD', line=1541)
W('43,3176', 0o50120, '', 'INDEX', 'FIXLOC', line=1542)
W('43,3177', 0o54052, '', 'TS', 'QPRET', line=1543)
W('43,3200', 0o04635, '', 'TC', 'POSTJUMP', line=1544)
W('43,3201', 0o27425, '', 'CADR', 'INTWAKE', 'FREE INTEGRATION AND EXIT.', kind='data', line=1545)

# Page 298

W('43,3202', 0o77634, 'TCPIN', 'RTB', kind='interp', line=1549)
W('43,3203', 0o21050, '', '', 'PINBRNCH', kind='operand', line=1550)

W('43,3204', 0o00051, 'OCT51', 'OCT', '51', kind='data', line=1552)
W('43,3205', 0o67202, 'TCPINAD', 'CADR', 'TCPIN', kind='data', line=1553)

# VERB 96       SET QUITFLAT TO STOP INTEGRATION.
#
# GO TO V37 WITH ZERO TO CAUSE P00.
# STATEINT WILL CHECK QUITFLAG AND SKIP 1ST PASS,
# THUS ALLOWING A 10 MINUT PERIOD WITHOUT INTEGRATION.

W('43,3206', 0o05504, 'VERB96', 'TC', 'UPFLAG', 'QUITFLAG WILL CAUSE INTEGRATION TO EXIT', line=1561)
W('43,3207', 0o00221, '', 'ADRES', 'QUITFLAG', '      AT NEXT TIMESTEP', kind='data', line=1562)

W('43,3210', 0o34755, '', 'CAF', 'ZERO', line=1564)
W('43,3211', 0o04635, '', 'TC', 'POSTJUMP', line=1565)
W('43,3212', 0o10040, '', 'CADR', 'V37', 'GO TO P00', kind='data', line=1566)

# VERB 67:      DISPLAY OF W MATRIX

W('43,3213', 0o02076, 'V67', 'TC', 'TESTXACT', line=1570)
W('43,3214', 0o35017, '', 'CAF', 'PRIO5', line=1571)
W('43,3215', 0o05105, '', 'TC', 'FINDVAC', line=1572)
#   EBANK= WWPOS
W('43,3216', 0o02007, '', '2CADR', 'V67CALL', kind='data', line=1574)
W('43,3217', 0o62064, kind='data', line=1574)

W('43,3220', 0o05155, '', 'TC', 'ENDOFJOB', line=1576)

# VERB 65       DISABLE U,V JETS DURING DPS BURNS

W('43,3221', 0o05504, 'SNUFFOUT', 'TC', 'UPFLAG', line=1580)
W('43,3222', 0o00115, '', 'ADRES', 'SNUFFER', kind='data', line=1581)
W('43,3223', 0o02121, '', 'TC', 'GOPIN', line=1582)

# VERB 75       ENABLE U,V JETS DURING DPS BURNS

W('43,3224', 0o05516, 'OUTSNUFF', 'TC', 'DOWNFLAG', line=1586)
W('43,3225', 0o00115, '', 'ADRES', 'SNUFFER', kind='data', line=1587)
W('43,3226', 0o02121, '', 'TC', 'GOPIN', line=1588)

# VERB 85       DISPLAY RR LOS AZIMUTH AND ELEVATION.
#
# AZIMUTH IS THE ANGLE BETWEEN THE LOS AND THE X-Z NB PLANE, 0-90 DEG IN THE +Y HEMISPHERE,
# 360-270 DEG IN THE -Y HEMISPHERE.
#
# ELEVATION IS THE ANGLE BETWEEN +ZNB AND THE PROJECTION OF THE LOS INTO THE X-Z PLANE, 0-360 ABOUT +Y.

#   EBANK= RR-AZ
W('43,3227', 0o02076, 'VERB85', 'TC', 'TESTXACT', line=1598)

# Page 299

W('43,3230', 0o04635, '', 'TC', 'POSTJUMP', line=1602)
W('43,3231', 0o60000, '', 'CADR', 'DSPRRLOS', kind='data', line=1603)

#   SETLOC PINBALL1
#   BANK

#   COUNT* $$/EXTVB

W('40,2000', 0o35017, 'DSPRRLOS', 'CAF', 'PRIO5', line=1610)
W('40,2001', 0o05105, '', 'TC', 'FINDVAC', line=1611)
#   EBANK= RR-AZ
W('40,2002', 0o02017, '', '2CADR', 'RRLOSDSP', kind='data', line=1613)
W('40,2003', 0o60104, kind='data', line=1613)

W('40,2004', 0o34740, '', 'CAF', 'PRIO4', line=1615)
W('40,2005', 0o05146, '', 'TC', 'PRIOCHNG', line=1616)
W('40,2006', 0o32076, '', 'CAF', 'V16N56', line=1617)
W('40,2007', 0o04616, '', 'TC', 'BANKCALL', line=1618)
W('40,2010', 0o20353, '', 'CADR', 'GOMARKFR', kind='data', line=1619)
W('40,2011', 0o05563, '', 'TC', 'B5OFF', line=1620)
W('40,2012', 0o05563, '', 'TC', 'B5OFF', line=1621)
W('40,2013', 0o05563, '', 'TC', 'B5OFF', line=1622)

W('40,2014', 0o34751, '', 'CAF', 'BIT3', line=1624)
W('40,2015', 0o05464, '', 'TC', 'BLANKET', line=1625)
W('40,2016', 0o05155, '', 'TC', 'ENDOFJOB', line=1626)

W('40,2017', 0o00006, 'RRLOSDSP', 'EXTEND', line=1628)
W('40,2020', 0o30036, '', 'DCA', 'CDUT', line=1629)
W('40,2021', 0o52155, '', 'DXCH', 'MPAC', line=1630)
W('40,2022', 0o06037, '', 'TC', 'INTPRET', line=1631)
W('40,2023', 0o77624, '', 'CALL', kind='interp', line=1632)
W('40,2024', 0o46065, '', '', 'RRNBMPAC', 'GET RR LOS IN BODY AXIS.', kind='operand', line=1633)
W('40,2025', 0o00001, '', 'STORE', '0D', 'UNIT LOS', kind='interp', line=1634)
W('40,2026', 0o14007, '', 'STODL', '6D', kind='interp', line=1635)
W('40,2027', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=1636)
W('40,2030', 0o24011, '', 'STOVL', '8D', kind='interp', line=1637)
W('40,2031', 0o00007, '', '', '6D', kind='operand', line=1638)
W('40,2032', 0o77656, '', 'UNIT', kind='interp', line=1639)
W('40,2033', 0o00007, '', 'STORE', '6D', 'UNIT OF LOS PROJ IN X-Z PLANE', kind='interp', line=1640)
W('40,2034', 0o77641, '', 'DOT', kind='interp', line=1641)
W('40,2035', 0o06514, '', '', 'UNITZ', kind='operand', line=1642)
W('40,2036', 0o24021, '', 'STOVL', 'COSTH', '16D', kind='interp', line=1643)
W('40,2037', 0o06520, '', '', 'UNITX', kind='operand', line=1644)
W('40,2040', 0o77641, '', 'DOT', kind='interp', line=1645)
W('40,2041', 0o00007, '', '', '6D', kind='operand', line=1646)
W('40,2042', 0o34023, '', 'STCALL', 'SINTH', '18D', kind='interp', line=1647)
W('40,2043', 0o47320, '', '', 'ARCTRIG', kind='operand', line=1648)
W('40,2044', 0o43244, '', 'BPL', 'DAD', 'INSURE DISPLAY OF 0-360 DEG.', kind='interp', line=1649)
W('40,2045', 0o60047, '', '', '+2', kind='operand', line=1650)
W('40,2046', 0o06530, '', '', 'DPPOSMAX', 'INTRODUCES AND ERROR OF B-28 REVS.', kind='operand', line=1651)

# Page 300

W('40,2047', 0o26203, '', 'STOVL', 'RR-ELEV', kind='interp', line=1655)
W('40,2050', 0o00001, '', '', '0D', kind='operand', line=1656)
W('40,2051', 0o77641, '', 'DOT', kind='interp', line=1657)
W('40,2052', 0o06516, '', '', 'UNITY', kind='operand', line=1658)
W('40,2053', 0o24023, '', 'STOVL', 'SINTH', kind='interp', line=1659)
W('40,2054', 0o00001, '', '', '0D', kind='operand', line=1660)
W('40,2055', 0o77641, '', 'DOT', kind='interp', line=1661)
W('40,2056', 0o00007, '', '', '6D', kind='operand', line=1662)
W('40,2057', 0o34021, '', 'STCALL', 'COSTH', kind='interp', line=1663)
W('40,2060', 0o47320, '', '', 'ARCTRIG', kind='operand', line=1664)
W('40,2061', 0o43244, '', 'BPL', 'DAD', 'INSURE DISPLAY OF 0-360 DEG.', kind='interp', line=1665)
W('40,2062', 0o60064, '', '', '+2', kind='operand', line=1666)
W('40,2063', 0o06530, '', '', 'DPPOSMAX', 'INTRODUCES AN ERROR OF B-28 REVS.', kind='operand', line=1667)
W('40,2064', 0o02201, '', 'STORE', 'RR-AZ', kind='interp', line=1668)
W('40,2065', 0o77776, '', 'EXIT', kind='interp', line=1669)
W('40,2066', 0o34777, '', 'CA', '1SEC', line=1670)
W('40,2067', 0o04616, '', 'TC', 'BANKCALL', line=1671)
W('40,2070', 0o01735, '', 'CADR', 'DELAYJOB', kind='data', line=1672)

W('40,2071', 0o34747, '', 'CA', 'BIT5', line=1674)
W('40,2072', 0o71044, '', 'MASK', 'EXTVBACT', line=1675)
W('40,2073', 0o10000, '', 'CCS', 'A', line=1676)
W('40,2074', 0o02017, '', 'TC', 'RRLOSDSP', line=1677)
W('40,2075', 0o05472, '', 'TC', 'ENDEXT', line=1678)

W('40,2076', 0o04070, 'V16N56', 'VN', '1656', kind='data', line=1680)
