"""TVCINITIALIZE.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/TVCINITIALIZE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 937-944 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TVCINITIALIZE', 'TVCINITIALIZE.agc', 'Comanche055', pages='937-944')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TVCINITIALIZE.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Jim Lawton <jim.lawton@gmail.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        936-944
# Mod history:  2009-05-11 JVL  Adapted from the Colossus249/ file
# of the same name, using Comanche055 page
# images.
# 2009-05-20 RSB  Corrections:  +80 -> +8D, added 4 missing
# lines in TVCINIT1, changed the capitalization
# of a couple of the "Page N" comments,
# corrected a couple of lines in LOADCOEFF.
# 2009-05-22 RSB  In LOADCOEF, DXCH N10 +14D corrected to
# TS N10 +14D.  Also, various comment-marks
# were added to comments following this
# change.
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

# Page 937
# NAME          TVCDAPON (TVC DAP INITIALIZATION AND STARTUP CALL)
# LOG SECTION...TVCINITIALIZE                   SUBROUTINE...DAPCSM
# MODIFIED BY SCHLUNDT                          21 OCTOBER 1968
# FUNCTIONAL DESCRIPTION
# PERFORMS TVCDAP INITIALIZATION (GAINS, TIMING PARAMETERS, FILTER VARIABLES, ETC.)
# COMPUTES STEERING (S40.8) GAIN KPRIMEDT, AND ZEROES PASTDELV,+1 VARIABLE
# MAKES INITIALIZATION CALL TO "NEEDLER" FOR TVC DAP NEEDLES-SETUP
# PERFORMS INITIALIZATION FOR ROLL DAP
# CALLS TVCEXECUTIVE AT TVCEXEC, VIA WAITLIST
# CALLS TVCDAP CDU-RATE INITIALIZATION PKG AT DAPINIT  VIA T5
# PROVIDES FOR LOADING OF LOW-BANDWIDTH COEFFS AND GAINS AT SWICHOVR
# CALLING SEQUENCE - T5LOC=2CADR(TVCDAPON,EBANK=BZERO), T5=.6SECT5
# IN PARTICULAR, CALLED BY "DOTVCON" IN P40
# MRCLEAN AND TVCINIT4 ARE POSSIBLE TVC-RESTART ENTRY POINTS
# NORMAL EXIT MODE
# TCF RESUME
# SUBROUTINES CALLED
# NEEDLER, MASSPROP
# ALARM OR ABORT EXIT MODES
# NONE
# ERASABLE INITIALIZATION REQUIRED
# CSMMASS, LEMMASS, DAPDATR1 (FOR MASSPROP SUBROUTINE)
# TVC PAD LOADS (SEE EBANK6 IN ERASABLE ASSIGNMENTS)
# PACTOFF, YACTOFF, CDUX
# TVCPHASE AND THE T5 BITS OF FLAGWRD6 (SET AT DOTVCON IN P40)
# OUTPUT
# ALL TVC AND ROLL DAP ERASABLES, FLAGWRD6 (BITS 13,14), T5, WAITLIST
# DEBRIS
# NONE

#   COUNT* $$/INIT
#   BANK 17
#   SETLOC DAPS7
#   BANK

#   EBANK= BZERO

W('17,2147', 0o22016, 'TVCDAPON', 'LXCH', 'BANKRUPT', 'T5 RUPT ARRIVAL (CALL BY DOTVCON - P40)', line=77)
W('17,2150', 0o00006, '', 'EXTEND', '', 'SAVE Q REQUIRED IN RESTARTS (MRCLEAN AND', line=78)
W('17,2151', 0o22012, '', 'QXCH', 'QRUPT', '      TVCINIT4 ARE ENTRIES)', line=79)
W('17,2152', 0o32534, 'MRCLEAN', 'CAF', 'NZERO', 'NUMBER TO ZERO, LESS ONE  (MUST BE ODD)', line=80)
# TVC RESTARTS ENTER HERE  (NEW BANK)
W('17,2153', 0o10000, '', 'CCS', 'A', line=82)
W('17,2154', 0o55447, '', 'TS', 'CNTR', line=83)
W('17,2155', 0o35021, '', 'CAF', 'ZERO', line=84)
W('17,2156', 0o54001, '', 'TS', 'L', line=85)
W('17,2157', 0o51447, '', 'INDEX', 'CNTR', line=86)
W('17,2160', 0o53530, '', 'DXCH', 'OMEGAYC', 'FIRST (LAST) TWO LOCATIONS', line=87)
W('17,2161', 0o11447, '', 'CCS', 'CNTR', line=88)
W('17,2162', 0o12153, '', 'TCF', 'MRCLEAN +1', line=89)
# Page 938
W('17,2163', 0o00006, '', 'EXTEND', '', 'SET UP ANOTHER T5 RUPT TO CONTINUE', line=91)
W('17,2164', 0o32551, '', 'DCA', 'INITLOC2', '      INITIALIZATION AT TVCINIT1', line=92)
W('17,2165', 0o53313, '', 'DXCH', 'T5LOC', 'THE PHSCHK2 ENTRY  (REDOTVC) AT TVCDAPON', line=93)
W('17,2166', 0o34777, '', 'CAF', 'POSMAX', '      +3 IS IN ANOTHER BANK. MUST RESET', line=94)
W('17,2167', 0o54030, '', 'TS', 'TIME5', '      BBCON TOO (FULL 2CADR), FOR THAT', line=95)
W('17,2170', 0o15333, 'ENDMRC', 'TCF', 'RESUME', '      ENTRY.', line=96)

W('17,2171', 0o22016, 'TVCINIT1', 'LXCH', 'BANKRUPT', line=98)
W('17,2172', 0o00006, '', 'EXTEND', line=99)
W('17,2173', 0o22012, '', 'QXCH', 'QRUPT', line=100)

W('17,2174', 0o04740, '', 'TC', 'IBNKCALL', 'UPDATE IXX, IAVG/TLX FOR DAP GAINS (R03', line=102)
W('17,2175', 0o13366, '', 'CADR', 'MASSPROP', '      OR NOUNS 46 AND 47 MUST BE CORRECT)', kind='data', line=103)

W('17,2176', 0o30110, '', 'CAE', 'EMDOT', 'SPS FLOW RATE, SCALED B+3 KG/CS', line=105)
W('17,2177', 0o00006, '', 'EXTEND', line=106)
W('17,2200', 0o72545, '', 'MP', 'ONETHOU', line=107)
W('17,2201', 0o55637, '', 'TS', 'TENMDOT', '10-SEC MASS LOSS B+16 KG', line=108)
W('17,2202', 0o40000, '', 'COM', line=109)
W('17,2203', 0o61474, '', 'AD', 'CSMMASS', line=110)
W('17,2204', 0o55652, '', 'TS', 'MASSTMP', 'DECREMENT FOR FIRST 10 SEC OF BURN', line=111)

W('17,2205', 0o31466, '', 'CAE', 'DAPDATR1', 'CHECK LEM-ON/OFF', line=113)
W('17,2206', 0o75002, '', 'MASK', 'BIT14', line=114)
W('17,2207', 0o10000, '', 'CCS', 'A', line=115)
W('17,2210', 0o35017, '', 'CAF', 'BIT1', 'LEM-ON (BIT1)', line=116)
W('17,2211', 0o55447, '', 'TS', 'CNTR', 'LEM-OFF (ZERO)', line=117)

W('17,2212', 0o51447, '', 'INDEX', 'CNTR', 'LOAD THE FILTER COEFFICIENTS', line=119)
W('17,2213', 0o32531, '', 'CAF', 'CSMCFADR', line=120)
W('17,2214', 0o55722, '', 'TS', 'COEFFADR', line=121)
W('17,2215', 0o02422, '', 'TC', 'LOADCOEF', line=122)

W('17,2216', 0o51447, '', 'INDEX', 'CNTR', 'PICK UP LM-OFF,-ON KTLX/I', line=124)
W('17,2217', 0o31416, '', 'CAE', 'EKTLX/I', 'SCALED AT 1/(8 ASCREV) OF ACTUAL VALUE', line=125)
W('17,2220', 0o55636, '', 'TS', 'KTLX/I', line=126)

W('17,2221', 0o02462, '', 'TCR', 'S40.15', 'COMPUTE 1/CONACC , VARK', line=128)

W('17,2222', 0o41447, 'TVCINIT2', 'CS', 'CNTR', 'PICK LM-OFF,-ON VALUE FOR FILTER PERIOD', line=130)
W('17,2223', 0o50000, '', 'INDEX', 'A', 'DETERMINATION:', line=131)
W('17,2224', 0o35016, '', 'CAF', 'BIT2', '      BIT2 FOR CSM ONLY 40MS FILTER', line=132)
W('17,2225', 0o55634, '', 'TS', 'KPRIMEDT', '      BIT3 FOR CSM/LM 80MS FILTER', line=133)

W('17,2226', 0o40000, '', 'COM', '', 'PREPARE T5TVCDT', line=135)
W('17,2227', 0o64777, '', 'AD', 'POSMAX', line=136)
W('17,2230', 0o65017, '', 'AD', 'BIT1', line=137)
W('17,2231', 0o55625, '', 'TS', 'T5TVCDT', line=138)

W('17,2232', 0o45001, '', 'CS', 'BIT15', 'RESET SWTOVER FLAG', line=140)
# Page 939
W('17,2233', 0o70105, '', 'MASK', 'FLAGWRD9', line=142)
W('17,2234', 0o54105, '', 'TS', 'FLAGWRD9', line=143)

W('17,2235', 0o51447, '', 'INDEX', 'CNTR', 'PICK UP LEM-OFF,-ON KPRIME', line=145)
W('17,2236', 0o31414, '', 'CAE', 'EKPRIME', '      SCALED (100 PI)/16', line=146)
W('17,2237', 0o00006, '', 'EXTEND', line=147)
W('17,2240', 0o71634, '', 'MP', 'KPRIMEDT', '(TVCDT/2, SC.AT B+14CS)', line=148)
W('17,2241', 0o22000, '', 'LXCH', 'A', '      SC.AT PI/8      (DIMENSIONLESS)', line=149)
W('17,2242', 0o53635, '', 'DXCH', 'KPRIMEDT', line=150)

W('17,2243', 0o51447, '', 'INDEX', 'CNTR', 'PICK UP LEM-OFF,-ON REPFRAC', line=152)
W('17,2244', 0o31421, '', 'CAE', 'EREPFRAC', line=153)
W('17,2245', 0o55642, '', 'TS', 'REPFRAC', line=154)

W('17,2246', 0o51447, '', 'INDEX', 'CNTR', 'PICK UP ONE-SHOT CORRECTION TIME', line=156)
W('17,2247', 0o32540, '', 'CAF', 'TCORR', line=157)
W('17,2250', 0o55447, '', 'TS', 'CNTR', line=158)

W('17,2251', 0o37716, '', 'CAF', 'NEGONE', 'PREVENT STROKE TEST UNTIL CALLED', line=160)
W('17,2252', 0o55654, '', 'TS', 'STRKTIME', line=161)

W('17,2253', 0o34374, '', 'CAF', 'NINETEEN', 'SET VCNTR FOR VARIABLE-GAIN UPDATES IN', line=163)
W('17,2254', 0o55643, '', 'TS', 'VCNTR', '      10 SECONDS (TVCEXEC 1/2 SEC RATE)', line=164)
W('17,2255', 0o55444, '', 'TS', 'V97VCNTR', 'FOR ENGFAIL (R41) LOGIC', line=165)

W('17,2256', 0o31423, 'TVCINIT3', 'CAE', 'PACTOFF', 'TRIM VALUES TO TRIM-TRACKERS, OUTPUT', line=167)
W('17,2257', 0o55605, '', 'TS', 'PDELOFF', '      TRACKERS, OFFSET-UPDATES, AND', line=168)
W('17,2260', 0o55623, '', 'TS', 'PCMD', '      OFFSET-TRACKER FILTERS', line=169)
W('17,2261', 0o55601, '', 'TS', 'DELPBAR', '      NOTE, LO-ORDER DELOFF,DELBAR ZEROED', line=170)

W('17,2262', 0o31424, '', 'CAE', 'YACTOFF', line=172)
W('17,2263', 0o55607, '', 'TS', 'YDELOFF', line=173)
W('17,2264', 0o55624, '', 'TS', 'YCMD', line=174)
W('17,2265', 0o55603, '', 'TS', 'DELYBAR', line=175)

W('17,2266', 0o31466, 'ATTINIT', 'CAE', 'DAPDATR1', 'ATTITUDE-ERROR INITIALIZATION LOGIC', line=177)
W('17,2267', 0o75003, '', 'MASK', 'BIT13', '      TEST FOR CSM OR CSM/LM', line=178)
W('17,2270', 0o00006, '', 'EXTEND', line=179)
W('17,2271', 0o12317, '', 'BZF', 'NEEDLEIN', '      BYPASS INITIALIZATION FOR CSM/LM', line=180)

W('17,2272', 0o35017, '', 'CAF', 'BIT1', '      SET UP TEMPORARY COUNTER', line=182)
W('17,2273', 0o55611, '', 'TS', 'TTMP1', line=183)

W('17,2274', 0o51611, '', 'INDEX', 'TTMP1', line=185)
W('17,2275', 0o31702, '', 'CA', 'ERRBTMP', 'ERRBTMP CONTAINS RCS ATTITUDE ERRORS', line=186)
W('17,2276', 0o00006, '', 'EXTEND', '', '      ERRORY & ERRORZ (P40 AT DOTVCON)', line=187)
W('17,2277', 0o72537, '', 'MP', '1/ATTLIM', '.007325(ERROR) = 0 IF ERROR < 1.5 DEG', line=188)
W('17,2300', 0o00006, '', 'EXTEND', line=189)
W('17,2301', 0o12311, '', 'BZF', '+8D', '      |ERROR| LESS THAN 1.5 DEG', line=190)
W('17,2302', 0o00006, '', 'EXTEND', line=191)
# Page 940
W('17,2303', 0o62306, '', 'BZMF', '+3', '      |ERROR| > 1.5 DEG, AND NEG', line=193)
W('17,2304', 0o32536, '', 'CA', 'ATTLIM', '      |ERROR| > 1.5 DEG, AND POS', line=194)
W('17,2305', 0o12307, '', 'TCF', '+2', line=195)
W('17,2306', 0o42536, '', 'CS', 'ATTLIM', line=196)
W('17,2307', 0o51611, '', 'INDEX', 'TTMP1', line=197)
W('17,2310', 0o55702, '', 'TS', 'ERRBTMP', line=198)
W('17,2311', 0o11611, '', 'CCS', 'TTMP1', '      TEST TEMPORARY COUNTER', line=199)
W('17,2312', 0o12273, '', 'TCF', 'ATTINIT +5', '      BACK TO REPEAT FOR PITCH ERROR', line=200)

W('17,2313', 0o31702, '', 'CA', 'ERRBTMP', 'ERRORS ESTABLISHED AND LIMITED', line=202)
W('17,2314', 0o55575, '', 'TS', 'PERRB', line=203)
W('17,2315', 0o31703, '', 'CA', 'ERRBTMP +1', line=204)
W('17,2316', 0o55577, '', 'TS', 'YERRB', line=205)

W('17,2317', 0o41501, 'NEEDLEIN', 'CS', 'RCSFLAGS', 'SET BIT 3 FOR INITIALIZATION PASS AND GO', line=207)
W('17,2320', 0o75015, '', 'MASK', 'BIT3', '      TO NEEDLER.  WILL CLEAR FOR TVC DAP', line=208)
W('17,2321', 0o27501, '', 'ADS', 'RCSFLAGS', '      (RETURNS AFTER CADR)', line=209)
W('17,2322', 0o04740, '', 'TC', 'IBNKCALL', line=210)
W('17,2323', 0o42420, '', 'CADR', 'NEEDLER', kind='data', line=211)

W('17,2324', 0o35021, 'TVCINIT4', 'CAF', 'ZERO', 'SET TVCPHASE TO INDICATE TVCDAPON-THRU-', line=213)
W('17,2325', 0o55644, '', 'TS', 'TVCPHASE', '      NEEDLEIN INITIALIZATION FINISHED.', line=214)
# (POSSIBLE TVC-RESTART ENTRY)

W('17,2326', 0o30032, '', 'CAE', 'CDUX', 'PREPARE ROLL DAP', line=217)
W('17,2327', 0o55662, '', 'TS', 'OGANOW', line=218)

W('17,2330', 0o35003, '', 'CAF', 'BIT13', 'IF ENGINE IS ALREADY OFF, ENGINOFF HAS', line=220)
W('17,2331', 0o00006, '', 'EXTEND', '', '      ALREADY ESTABLISHED THE POST-BURN', line=221)
W('17,2332', 0o02011, '', 'RAND', 'DSALMOUT', '      CSMMASS (MASSBACK DOES IT). DONT', line=222)
W('17,2333', 0o00006, '', 'EXTEND', '', '      TOUCH CSMMASS.  IF ENGINE IS ON,', line=223)
W('17,2334', 0o12337, '', 'BZF', '+3', '      THEN ITS OK TO DO THE COPYCYCLE', line=224)
# EVEN BURNS LESS THAN 0.4 SEC ARE AOK

W('17,2335', 0o31652, '', 'CAE', 'MASSTMP', 'COPYCYCLE', line=227)
W('17,2336', 0o55474, '', 'TS', 'CSMMASS', line=228)

W('17,2337', 0o35036, '', 'CAF', '.5SEC', 'CALL TVCEXECUTIVE (ROLLDAP CALL, ETC)', line=230)
W('17,2340', 0o05245, '', 'TC', 'WAITLIST', line=231)
#   EBANK= BZERO
W('17,2341', 0o02720, '', '2CADR', 'TVCEXEC', kind='data', line=233)
W('17,2342', 0o34066, kind='data', line=233)

W('17,2343', 0o00006, '', 'EXTEND', '', 'CALL FOR DAPINIT', line=235)
W('17,2344', 0o32547, '', 'DCA', 'DAPINIT5', line=236)
W('17,2345', 0o53313, '', 'DXCH', 'T5LOC', line=237)
W('17,2346', 0o31625, '', 'CAE', 'T5TVCDT', '(ALLOW TIME FOR RESTART COMPUTATIONS)', line=238)
W('17,2347', 0o54030, '', 'TS', 'TIME5', line=239)
# Page 941
W('17,2350', 0o15333, 'ENDTVCIN', 'TCF', 'RESUME', line=241)

W('17,2351', 0o02354, 'PRESWTCH', 'TCR', 'SWICHOVR', 'ENTRY FROM V46', line=243)

W('17,2352', 0o04701, '', 'TC', 'POSTJUMP', 'THIS PROVIDES AN EXIT FROM SWITCH-OVER', line=245)
W('17,2353', 0o21272, '', 'CADR', 'PINBRNCH', '      (PINBRNCH DOES A RELINT)', kind='data', line=246)

W('17,2354', 0o00004, 'SWICHOVR', 'INHINT', line=248)
W('17,2355', 0o31644, '', 'CA', 'TVCPHASE', 'SAVE TVCPHASE', line=249)
W('17,2356', 0o55611, '', 'TS', 'PHASETMP', line=250)
W('17,2357', 0o45016, '', 'CS', 'BIT2', 'SET TVCPHASE = -2 (INDICATES SWITCH-OVER', line=251)
W('17,2360', 0o55644, '', 'TS', 'TVCPHASE', '      TO RESTART LOGIC)', line=252)

W('17,2361', 0o00006, '', 'EXTEND', '', 'SAVE Q FOR RETURN (RESTART ENTRY POINT,', line=254)
W('17,2362', 0o23613, '', 'QXCH', 'RTRNLOC', '      TVCPHASE AND PHASETMP ALREADY SET)', line=255)

W('17,2363', 0o32535, '', 'CAF', 'NZEROJR', 'ZEROING LOOP FOR FILTER STORAGE LOCS', line=257)
W('17,2364', 0o55676, '', 'TS', 'CNTRTMP', line=258)

W('17,2365', 0o35021, 'MCLEANJR', 'CA', 'ZERO', line=260)
W('17,2366', 0o54001, '', 'TS', 'L', line=261)
W('17,2367', 0o51676, '', 'INDEX', 'CNTRTMP', line=262)
W('17,2370', 0o53541, '', 'DXCH', 'PTMP1 -1', line=263)
W('17,2371', 0o11676, '', 'CCS', 'CNTRTMP', line=264)
W('17,2372', 0o10000, '', 'CCS', 'A', line=265)
W('17,2373', 0o12364, '', 'TCF', 'SWICHOVR +8D', line=266)

W('17,2374', 0o40105, '', 'CS', 'FLAGWRD9', 'SET SWITCHOVER FLAG FOR DOWNLINK', line=268)
W('17,2375', 0o75001, '', 'MASK', 'BIT15', line=269)
W('17,2376', 0o26105, '', 'ADS', 'FLAGWRD9', line=270)

W('17,2377', 0o31420, '', 'CAE', 'EKTLX/I +2', 'LOW BANDWIDTH GAINS   - DAP', line=272)
W('17,2400', 0o55636, '', 'TS', 'KTLX/I', line=273)
W('17,2401', 0o02471, '', 'TCR', 'S40.15 +7', line=274)

W('17,2402', 0o32542, '', 'CAF', 'FKPRIMDT', '                      - STEERING', line=276)
W('17,2403', 0o55634, '', 'TS', 'KPRIMEDT', line=277)

W('17,2404', 0o32543, '', 'CAF', 'FREPFRAC', '                      - TMC LOOP', line=279)
W('17,2405', 0o55642, '', 'TS', 'REPFRAC', line=280)

W('17,2406', 0o00006, '', 'EXTEND', '', 'UPDATE TRIM ESTIMATES', line=282)
W('17,2407', 0o31602, '', 'DCA', 'DELPBAR', line=283)
W('17,2410', 0o53606, '', 'DXCH', 'PDELOFF', line=284)
W('17,2411', 0o00006, '', 'EXTEND', line=285)
W('17,2412', 0o31604, '', 'DCA', 'DELYBAR', line=286)
W('17,2413', 0o53610, '', 'DXCH', 'YDELOFF', line=287)

W('17,2414', 0o32533, '', 'CA', 'LBCFADR', line=289)
# Page 942
W('17,2415', 0o55722, '', 'TS', 'COEFFADR', line=291)
W('17,2416', 0o02422, '', 'TC', 'LOADCOEF', line=292)

W('17,2417', 0o31611, '', 'CAE', 'PHASETMP', 'RESTORE TVCPHASE', line=294)
W('17,2420', 0o55644, '', 'TS', 'TVCPHASE', line=295)

W('17,2421', 0o01613, '', 'TC', 'RTRNLOC', 'BACK TO PRESWTCH OR TVCRESTARTS', line=297)

W('17,2422', 0o00006, 'LOADCOEF', 'EXTEND', '', 'LOAD DAP FILTER COEFFICIENTS', line=299)
W('17,2423', 0o51722, '', 'INDEX', 'COEFFADR', '  FROM: ERASABLE FOR CSM/LM HB', line=300)
W('17,2424', 0o30001, '', 'DCA', '0', '        FIXED    FOR CSM/LM LB', line=301)
W('17,2425', 0o53724, '', 'DXCH', 'N10', '        FIXED    FOR CSM', line=302)

W('17,2426', 0o00006, '', 'EXTEND', '', 'NOTE: FOR CSM/LM, NORMAL COEFFICIENT', line=304)
W('17,2427', 0o51722, '', 'INDEX', 'COEFFADR', 'LOAD WILL BE HIGH BANDWIDTH PAD LOAD', line=305)
W('17,2430', 0o30003, '', 'DCA', '2', 'ERASABLES. DURING CSM/LM SWITCHOVER,', line=306)
W('17,2431', 0o53726, '', 'DXCH', 'N10 +2', 'THIS LOGIC IS USED TO LOAD LOW BANDWIDTH', line=307)
# COEFFICIENTS FROM FIXED MEMORY.

W('17,2432', 0o00006, '', 'EXTEND', line=310)
W('17,2433', 0o51722, '', 'INDEX', 'COEFFADR', line=311)
W('17,2434', 0o30005, '', 'DCA', '4', line=312)
W('17,2435', 0o53730, '', 'DXCH', 'N10 +4', line=313)

W('17,2436', 0o00006, '', 'EXTEND', line=315)
W('17,2437', 0o51722, '', 'INDEX', 'COEFFADR', line=316)
W('17,2440', 0o30007, '', 'DCA', '6', line=317)
W('17,2441', 0o53732, '', 'DXCH', 'N10 +6', line=318)

W('17,2442', 0o00006, '', 'EXTEND', line=320)
W('17,2443', 0o51722, '', 'INDEX', 'COEFFADR', line=321)
W('17,2444', 0o30011, '', 'DCA', '8D', line=322)
W('17,2445', 0o53734, '', 'DXCH', 'N10 +8D', line=323)

W('17,2446', 0o00006, '', 'EXTEND', line=325)
W('17,2447', 0o51722, '', 'INDEX', 'COEFFADR', line=326)
W('17,2450', 0o30013, '', 'DCA', '10D', line=327)
W('17,2451', 0o53736, '', 'DXCH', 'N10 +10D', line=328)

W('17,2452', 0o00006, '', 'EXTEND', line=330)
W('17,2453', 0o51722, '', 'INDEX', 'COEFFADR', line=331)
W('17,2454', 0o30015, '', 'DCA', '12D', line=332)
W('17,2455', 0o53740, '', 'DXCH', 'N10 +12D', line=333)

W('17,2456', 0o51722, '', 'INDEX', 'COEFFADR', line=335)
W('17,2457', 0o30016, '', 'CA', '14D', line=336)
W('17,2460', 0o55741, '', 'TS', 'N10 +14D', line=337)

W('17,2461', 0o00002, '', 'TC', 'Q', line=339)
# Page 943
W('17,2462', 0o31470, 'S40.15', 'CAE', 'IXX', 'GAIN COMPUTATIONS (1/CONACC, VARK)', line=341)
W('17,2463', 0o00006, '', 'EXTEND', '', 'ENTERED FROM TVCINITIALIZE AND TVCEXEC', line=342)
W('17,2464', 0o72544, '', 'MP', '2PI/M', '      2PI/M SCALED 1/(B+8 N M)', line=343)
W('17,2465', 0o20001, '', 'DDOUBL', '', '      IXX   SCALED B+20 KG-MSQ', line=344)
W('17,2466', 0o20001, '', 'DDOUBL', line=345)
W('17,2467', 0o20001, '', 'DDOUBL', line=346)
W('17,2470', 0o55640, '', 'TS', '1/CONACC', '           SCALED B+9 SEC-SQ/REV', line=347)

W('17,2471', 0o31636, '', 'CAE', 'KTLX/I', 'ENTRY FROM CSM/LM V46 SWITCH-OVER', line=349)
W('17,2472', 0o00006, '', 'EXTEND', '', '           SCALED (B+3 ASCREV)  1/SECSQ', line=350)
W('17,2473', 0o71472, '', 'MP', 'IAVG/TLX', '           SCALED B+2 SECSQ', line=351)
W('17,2474', 0o20001, '', 'DDOUBL', line=352)
W('17,2475', 0o20001, '', 'DDOUBL', line=353)
W('17,2476', 0o55641, '', 'TS', 'VARK', '           SCALED (B+3 ASCREV)', line=354)
W('17,2477', 0o00002, '', 'TC', 'Q', line=355)

W('17,2500', 0o37777, 'CSMN10', 'DEC', '.99999', 'N10   CSM ONLY FILTER COEFFICIENTS', kind='data', line=357)
W('17,2501', 0o67657, '', 'DEC', '-.2549', 'N11/2', kind='data', line=358)
W('17,2502', 0o01703, '', 'DEC', '.0588', 'N12', kind='data', line=359)
W('17,2503', 0o47472, '', 'DEC', '-.7620', 'D11/2', kind='data', line=360)
W('17,2504', 0o27656, '', 'DEC', '.7450', 'D12', kind='data', line=361)

W('17,2505', 0o37777, '', 'DEC', '.99999', 'N20', kind='data', line=363)
W('17,2506', 0o60361, '', 'DEC', '-.4852', 'N21/2', kind='data', line=364)
W('17,2507', 0o00000, '', 'DEC', '0', 'N22', kind='data', line=365)
W('17,2510', 0o67304, '', 'DEC', '-.2692', 'D22/2', kind='data', line=366)
W('17,2511', 0o00000, '', 'DEC', '0', 'D22', kind='data', line=367)

W('17,2512', 0o37777, 'LBN10', 'DEC', '+.99999', 'N10   LOW BANDWIDTH FILTER COEFFICIENTS', kind='data', line=369)
W('17,2513', 0o65371, '', 'DEC', '-.3285', 'N11/2', kind='data', line=370)
W('17,2514', 0o65337, '', 'DEC', '-.3301', 'N12', kind='data', line=371)
W('17,2515', 0o42700, '', 'DEC', '-.9101', 'D11/2', kind='data', line=372)
W('17,2516', 0o33045, '', 'DEC', '+.8460', 'D12', kind='data', line=373)

W('17,2517', 0o01000, '', 'DEC', '+.03125', 'N20', kind='data', line=375)
W('17,2520', 0o00000, '', 'DEC', '0', 'N21/2', kind='data', line=376)
W('17,2521', 0o00000, '', 'DEC', '0', 'N22', kind='data', line=377)
W('17,2522', 0o42700, '', 'DEC', '-.9101', 'D21/2', kind='data', line=378)
W('17,2523', 0o33045, '', 'DEC', '+.8460', 'D22', kind='data', line=379)

W('17,2524', 0o20000, '', 'DEC', '+.5000', 'N30', kind='data', line=381)
W('17,2525', 0o60730, '', 'DEC', '-.47115', 'N31/2', kind='data', line=382)
W('17,2526', 0o17145, '', 'DEC', '+.4749', 'N32', kind='data', line=383)
W('17,2527', 0o41323, '', 'DEC', '-.9558', 'D31/2', kind='data', line=384)
W('17,2530', 0o35773, '', 'DEC', '+.9372', 'D32', kind='data', line=385)

W('17,2531', 0o02500, 'CSMCFADR', 'GENADR', 'CSMN10', 'CSM ONLY COEFFICIENTS ADDRESS', kind='data', line=387)
W('17,2532', 0o01425, 'HBCFADR', 'GENADR', 'HBN10', 'HIGH BANDWIDTH COEFFICIENTS ADDRESS', kind='data', line=388)
# Page 944
W('17,2533', 0o02512, 'LBCFADR', 'GENADR', 'LBN10', 'LOW BANDWIDTH COEFFICIENTS ADDRESS', kind='data', line=390)

W('17,2534', 0o00063, 'NZERO', 'DEC', '51', 'MUST BE ODD FOR MRCLEAN', kind='data', line=392)
W('17,2535', 0o00027, 'NZEROJR', 'DEC', '23', 'MUST BE ODD FOR MCLEANJR', kind='data', line=393)

W('17,2536', 0o00210, 'ATTLIM', 'DEC', '0.00833', 'INITIAL ATTITUDE ERROR LIMIT (1.5 DEG)', kind='data', line=395)
W('17,2537', 0o00170, '1/ATTLIM', 'DEC', '0.007325', '.007325(ERROR) = 0 IF ERROR < 1.5 DEG', kind='data', line=396)

W('17,2540', 0o00005, 'TCORR', 'OCT', '00005', 'CSM', kind='data', line=398)
W('17,2541', 0o00000, '', 'OCT', '00000', 'CSM/LM (HB,LB)', kind='data', line=399)

W('17,2542', 0o00247, 'FKPRIMDT', 'DEC', '.0102', 'CSM/LM (LB), (.05 X .08) SCALED AT PI/8', kind='data', line=401)
W('17,2543', 0o00232, 'FREPFRAC', 'DEC', '.0375 B-2', 'CSM/LM (LB), 0.0375 SCALED AT B+2', kind='data', line=402)

S('NINETEEN', 'equals', 0o4374, line=404)
W('17,2544', 0o33074, '2PI/M', 'DEC', '.00331017 B+8', '2PI/M, SCALED AT 1/(B+8 N-M)', kind='data', line=405)

W('17,2545', 0o03720, 'ONETHOU', 'DEC', '1000 B-13', 'KG/CS B3 TO KG/10SEC B16 CONVERSION', kind='data', line=407)

#   EBANK= BZERO
W('17,2546', 0o03107, 'DAPINIT5', '2CADR', 'DAPINIT', kind='data', line=410)
W('17,2547', 0o40066, kind='data', line=410)

#   EBANK= BZERO
W('17,2550', 0o02171, 'INITLOC2', '2CADR', 'TVCINIT1', kind='data', line=413)
W('17,2551', 0o36066, kind='data', line=413)
