"""P61-P67.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P61-P67.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 789-818 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P61_P67', 'P61-P67.agc', 'Comanche055', pages='789-818')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P61-P67.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 789-818
# Contact:      Ron Burkey <info@sandroid.org>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-12 RSB  Adapted from Colossus249 file of the same
# name and Comanche 055 page images.
# 2009-05-20 RSB  Corrections:  V06N68 -> V06N74, added missing
# definition of V06N74, in several
# interpreter operands fixed stuff like
# N-M,1 to N -M,1
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

# Page 789
# PROGRAM:      P61
# MOD NO.:      0       MAR. 13, 1967
# MOD BY:       R. HIRSCHKOP
# MOD NO: 1     MOD BY:  RR BAIRNSFATHER        DATE: 22 JUN 67         RESTARTS
# MOD NO: 2     MOD BY:  RR BAIRNSFATHER        DATE: 17 JAN 68         COLOSSUS GSOP CHANGES
# MOD NO: 3     MOD BY:  RR BAIRNSFATHER        DATE:  8 MAY 68         DELETE CMSM MANEUVER (PCR 50)
# FUNCTION:     TO CALCULATE AND DISPLAY EMS INITIALIZATION DATA
# CALLING SEQUENCE:  BY V37
# EXIT:         TO P62
# SUBROUTINE CALLS:  S61.1, S61.3, GOFLASH, FLAGUP, R02BOTH
# ERASABLE INITIALIZATION:
# EMSALT (-29) M          .05G ALTITUDE ABOVE FISCHER ELLIPSOID   PAD LOADED.
# ALFAPAD /180            HYPERSONIC CM TRIM ANGLE OF ATTACK      PAD LOADED
# OUTPUT:       THE FOLLOWING REGISTERS ARE WRITTEN IN FOR USE BY DISPLAYS
# GMAX    100 GMAX (-14) G,S      MAXIMUM ACCELERATION
# VPRED   (-7) M/CS               PREDICTED VELOCITY AT 400K FT
# GAMMAEI (GAMMA/360              PREDICTED GAMMA    AT 400K FT
# RTGO    THETAH/360              RANGE ANGLE TO SPLASH FROM EMSALT       EMSALT IS PAD LOADED
# VIO     (-7) M/CS               INERTIAL VELOCITY AT       EMSALT       EMSALT IS PAD LOADED
# TTE     (-28) CS                TIME TO                    EMSALT       EMSALT IS PAD LOADED
# LAT(SPL) /360                   TARGET LOCATION                         LEFT BY DSKY
# LNG(SPL) /360                   TARGET LOCATION                         LEFT BY DSKY
# HEADSUP (0)                     +1 = LIFT DOWN, -1 = LIFT UP            LEFT BY DSKY
# DEBRIS:       SEE SUBROUTINES.

#   BANK 26
#   SETLOC P60S
#   BANK

#   EBANK= AOG

#   COUNT* $$/P61

W('26,2217', 0o35002, 'P61', 'CA', 'BIT14', 'EXTENDED VERB SHOULD BE FREE THIS CLOSE', line=69)
W('26,2220', 0o55044, '', 'TS', 'EXTVBACT', 'TO V37', line=70)
# LOCK OUT EXTENDED VERBS SO CAN USE TFF
# ROUTINES.  EXT VERB ERASE IS USED

W('26,2221', 0o45017, '', 'CS', 'ONE', 'REMOVE IF HEADSUP EVER ON UPLINK DATA', line=74)
W('26,2222', 0o55726, '', 'TS', 'HEADSUP', 'PRELOAD', line=75)

W('26,2223', 0o02544, '', 'TC', 'S61.1', 'CHECK STATE VECTOR AND IMU ORIENTATION', line=77)
# RV 60GENRET. DOES PHASCHNG, GROUP 4.

W('26,2224', 0o32425, '', 'CA', 'V06N61', 'LAT(SPL)      LNG(SPL)        HEADSUP', line=80)
# XXX.XX DEG    XXX.XX DEG      XXXXX.
W('26,2225', 0o04662, '', 'TC', 'BANKCALL', line=82)
W('26,2226', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=83)
W('26,2227', 0o04106, '', 'TC', 'GOTOPOOH', line=84)
# Page 790
W('26,2230', 0o02235, '', 'TC', 'P61.4', line=86)
W('26,2231', 0o02224, '', 'TC', '-5', line=87)

W('26,2232', 0o05412, 'P61.3', 'TC', 'PHASCHNG', line=89)
W('26,2233', 0o00014, '', 'OCT', '00014', kind='data', line=90)

W('26,2234', 0o05217, '', 'TC', 'ENDOFJOB', line=92)

W('26,2235', 0o22007, 'P61.4', 'ZL', line=94)
W('26,2236', 0o11726, '', 'CCS', 'HEADSUP', 'C(HEADSUP)= +1/-1', line=95)
W('26,2237', 0o35002, '', 'CA', 'BIT14', 'IF HEADSUP POS,ROLLC =180 DEG.(LIFT DWN)', line=96)
W('26,2240', 0o12241, '', 'NOOP', '', 'IF HEADSUP NEG,ROLLC =0 (LIFT UP)', line=97)
W('26,2241', 0o53716, '', 'DXCH', 'ROLLC', 'ROLLC IS USED BY S62.3: GIM ANG AT .05G', line=98)

W('26,2242', 0o06006, '', 'TC', 'INTPRET', line=100)
W('26,2243', 0o77745, 'NEWRNVN', 'DLOAD', kind='interp', line=101)
W('26,2244', 0o01205, '', '', 'PIPTIME', 'SAVE TIME OF RN,VN TO DETERMINE IF AN', kind='operand', line=102)
W('26,2245', 0o37651, '', 'STCALL', 'MM', 'UPDATE HAS OCCURRED.', kind='interp', line=103)
W('26,2246', 0o52063, '', '', 'STARTEN1', 'INITIALIZE', kind='operand', line=104)
W('26,2247', 0o77775, '', 'VLOAD', kind='interp', line=105)
W('26,2250', 0o01171, '', '', 'RN', kind='operand', line=106)
W('26,2251', 0o02327, '', 'STORE', 'RONE', kind='interp', line=107)
W('26,2252', 0o77656, '', 'UNIT', kind='interp', line=108)
W('26,2253', 0o26343, '', 'STOVL', 'URONE', kind='interp', line=109)
W('26,2254', 0o01177, '', '', 'VN', kind='operand', line=110)
W('26,2255', 0o02335, '', 'STORE', 'VONE', kind='interp', line=111)
W('26,2256', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=112)
W('26,2257', 0o02343, '', '', 'URONE', kind='operand', line=113)
W('26,2260', 0o03502, '', 'STORE', 'UNI', kind='interp', line=114)
W('26,2261', 0o45345, 'DUMPP61', 'DLOAD', 'DSU', kind='interp', line=115)
W('26,2262', 0o03651, '', '', 'MM', 'INITIAL VALUE OF PIPTIME', kind='operand', line=116)
W('26,2263', 0o01205, '', '', 'PIPTIME', kind='operand', line=117)
W('26,2264', 0o45040, '', 'BMN', 'CALRB', kind='interp', line=118)
W('26,2265', 0o54243, '', '', 'NEWRNVN', 'UPDATED... GO TRY AGAIN', kind='operand', line=119)
W('26,2266', 0o54651, '', '', 'S61.2', 'GET DISPLAY DATA FOR N60 AND N63', kind='operand', line=120)
# AND RETURN IN BASIC, BELOW.
W('26,2267', 0o05536, 'P61.1', 'TC', 'CLEARMRK', line=122)
W('26,2270', 0o32424, '', 'CA', 'V06N60', 'GMAX          VPRED           GAMMAEI', line=123)
# XXX.XX G      XXXXX. FPS      XXX.XX DEG
W('26,2271', 0o04662, '', 'TC', 'BANKCALL', line=125)
W('26,2272', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=126)

W('26,2273', 0o04106, '', 'TC', 'GOTOPOOH', line=128)
W('26,2274', 0o02276, '', 'TC', 'P61.2', 'PROCEED', line=129)
W('26,2275', 0o02270, '', 'TC', '-5', line=130)

W('26,2276', 0o06006, 'P61.2', 'TC', 'INTPRET', 'CORRECT TTE FOR TIME LAPSE DURING', line=132)
# ABOVE DISPLAY.
W('26,2277', 0o45234, '', 'RTB', 'DSU', kind='interp', line=134)
W('26,2300', 0o45510, '', '', 'LOADTIME', 'CURRENT TIME.', kind='operand', line=135)
# Page 791
W('26,2301', 0o03651, '', '', 'MM', 'PIPTIME FOR RONE & VONE.', kind='operand', line=137)
W('26,2302', 0o77615, '', 'DAD', kind='interp', line=138)
W('26,2303', 0o03733, '', '', 'TTE1', 'NEGATIVE OF FREE FALL TIME.', kind='operand', line=139)
W('26,2304', 0o03727, '', 'STORE', 'TTE', 'DECREMENTED', kind='interp', line=140)

W('26,2305', 0o77776, '', 'EXIT', kind='interp', line=142)

W('26,2306', 0o32426, '', 'CA', 'V06N63', 'RTGO          VIO             TTE', line=144)
# XXXX.X NM     XXXXX. FPS      XXBXX M,S
W('26,2307', 0o04662, '', 'TC', 'BANKCALL', line=146)
W('26,2310', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=147)
W('26,2311', 0o04106, '', 'TC', 'GOTOPOOH', line=148)
W('26,2312', 0o02314, '', 'TC', '+2', line=149)
W('26,2313', 0o02276, '', 'TC', 'P61.2', 'REDO', line=150)

# .... THEN FALL INTO P62
# Page 792

# PROGRAM:      P62
# MOD NO.:      0       MAR. 13, 1967
# MOD BY:       R. HIRSCHKOP
# MOD NO:  1    MOD BY:  RR BAIRNSFATHER        DATE: 21 MAR 67
# MOD NO:  2    MOD BY:  RR BAIRNSFATHER        DATE: 22 JUN 67         RESTARTS.
# MOD NO:  3    MOD BY:  RR BAIRNSFATHER        DATE: 17 JAN 68         COLOSSUS GSOP CHANGES.
# MOD NO:  4    MOD BY:  RR BAIRNSFATHER        DATE:  8 MAY 68         MOVE START OF DESIRED GIMBAL CALC.
# FUNCTION:     1) TO NOTIFY CREW WHEN GNC SYSTEM IS PREPARED FOR CM/SM SEPARATION.
# 2) TO ORIENT THE CM TO THE CORRECT ATTITUDE FOR ATMOSPHERIC ENTRY.
# CALLING SEQUENCE:  BY V37 OR DIRECTLY FROM P61
# EXIT:         TO P63
# ERASABLE INITIALIZATION:
# ALFAPAD                                         LEFT BY PAD LOAD
# LADPAD                                          LEFT BY PAD LOAD
# LODPAD                                          LEFT BY PAD LOAD
# LAT(SPL)        (MAY BE CHANGED BELOW)          LEFT BY DSKY, VIA P61
# LNG(SPL)        (MAY BE CHANGED BELOW)          LEFT BY DSKY, VIA P61
# HEADSUP         (MAY BE CHANGED BELOW)          LEFT BY DSKY, VIA P61
# SUBROUTINE CALLS:  NEWMODEX, S61.1, CM/DAPIC, CM/DAPON, R02BOTH, GOPERF1, GOFLASH, GODSPR.

#   COUNT* $$/P62

W('26,2314', 0o05354, '', 'TC', 'NEWMODEX', 'MODE CHANGE IF CAME FROM P61.', line=177)
W('26,2315', 0o00076, '', 'MM', '62', 'MODE CHANGE AUTOMATIC VIA V 37.', kind='data', line=178)
W('26,2316', 0o35017, '', 'CA', 'ONE', line=179)
W('26,2317', 0o54332, '', 'TS', 'DNLSTCOD', line=180)

W('26,2320', 0o02544, 'P62', 'TC', 'S61.1', 'CHECK STATE VECTOR AND IMU ORIENTATION.', line=182)

W('26,2321', 0o06006, '', 'TC', 'INTPRET', line=184)
W('26,2322', 0o47131, '', 'SSP', 'RTB', kind='interp', line=185)
W('26,2323', 0o03325, '', '', 'POSEXIT', kind='operand', line=186)
W('26,2324', 0o54401, '', '', 'P62.3', 'CALCULATE DESIRED .05G GIMBAL ANGLES.', kind='operand', line=187)
# WITHOUT DISPLAY.
W('26,2325', 0o41672, '', '', 'CM/DAPIC', 'START CM/POSE AND BODY RATE CALC', kind='operand', line=189)

# DOES 2PHSCHNG, OCT 40116, OCT 05024, OCT 13000.
# CM/DAPIC SETS EBANK = EBAOG
# AND RETURNS IN BASIC TO P62.2.
W('26,2326', 0o00006, 'P62.2', 'EXTEND', line=194)
W('26,2327', 0o32432, '', 'DCA', 'POSECADR', 'CONTINUE WITH CM/POSE AFTER AV G.', line=195)
W('26,2330', 0o53223, '', 'DXCH', 'AVEGEXIT', line=196)

W('26,2331', 0o34270, '', 'CAF', 'OCT41', 'REQUEST SEPARATION', line=198)
W('26,2332', 0o04662, '', 'TC', 'BANKCALL', line=199)
W('26,2333', 0o21125, '', 'CADR', 'GOPERF1R', kind='data', line=200)
W('26,2334', 0o04106, '', 'TC', 'GOTOPOOH', line=201)
W('26,2335', 0o02340, '', 'TC', '+3', 'PROCEED', line=202)
# Page 793
# NOTE:  NODOFLAG WILL BE SET IN CM/DAPON. ***
W('26,2336', 0o02331, '', 'TC', '-5', 'ENTER', line=205)
W('26,2337', 0o02232, '', 'TC', 'P61.3', 'FOR PHASCHNG AND ENDOFJOB', line=206)

W('26,2340', 0o04701, '', 'TC', 'POSTJUMP', line=208)
W('26,2341', 0o41612, '', 'CADR', 'CM/DAPON', 'DISABLE RCS DAP, ENABLE ENTRY DAP AND', kind='data', line=209)
# DO ATTITUDE HOLD.

# WILL IDLE UNTIL CM/POSE DOES ONE UPDATE.
# CM/DAPON DOES NO PHASCHNG.

W('26,2342', 0o32425, 'P62.1', 'CA', 'V06N61', 'LAT(SPL)      LNG(SPL)        HEADSUP', line=215)
# XXX.XX DEG    XXX.XX DEG      0000X.

# TERMINATE ATTITUDE HOLD.  SET UP COMMANDS:
# ROLLC, ALFACOM, BETACOM.  BEGIN MANEUVER TO
# ENTRY ATTITUDE.

W('26,2343', 0o04662, '', 'TC', 'BANKCALL', line=222)
W('26,2344', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=223)
W('26,2345', 0o02342, '', 'TC', '-3', line=224)
W('26,2346', 0o02350, '', 'TC', '+2', line=225)
W('26,2347', 0o02342, '', 'TC', '-5', line=226)

W('26,2350', 0o05412, '', 'TC', 'PHASCHNG', line=228)
W('26,2351', 0o04024, '', 'OCT', '04024', 'USE ENTRYVN FOR DISPLAY BELOW.', kind='data', line=229)
# EBANK WAS SET IN CM/DAPON TO EBAOG

W('26,2352', 0o11726, '', 'CCS', 'HEADSUP', 'C(HEADSUP) = +/- 1', line=232)
W('26,2353', 0o35002, '', 'CA', 'BIT14', 'IF HEADSUP POS, ROLLC=180 DEG (LIFT DWN)', line=233)
W('26,2354', 0o12355, '', 'NOOP', '', 'IF HEADSUP NEG, ROLLC=0 DEG (LIFT UP)', line=234)
W('26,2355', 0o55715, '', 'TS', 'ROLLC', line=235)
W('26,2356', 0o31411, '', 'CA', 'ALFAPAD', 'NOMINAL ALFATRIM PAD LOADED, NEG. NO.', line=236)
W('26,2357', 0o22007, '', 'ZL', line=237)
W('26,2360', 0o53604, '', 'DXCH', 'ALFACOM', 'SET ALFACOM = ALFA TRIM, BETACOM=0', line=238)

W('26,2361', 0o35017, '', 'CA', 'ONE', 'PERMITS EXDAP2 TO CHANGE FLAG TO +0', line=240)
W('26,2362', 0o55727, '', 'TS', 'P63FLAG', 'AS INDICATOR.  STARTS UP P63.', line=241)

W('26,2363', 0o35052, '', 'CA', 'V06N22', 'SET UP DISPLAY FOR CDU DESIRED VALUES', line=243)
W('26,2364', 0o55263, '', 'TS', 'ENTRYVN', 'FROM ENTRY ATTITUDE CALC, THAT IS', line=244)
# ALREADY GOING.
W('26,2365', 0o05546, '', 'TC', 'UPFLAG', 'TURN ON ENTRY DISPLAY', line=246)
W('26,2366', 0o00134, '', 'ADRES', 'ENTRYDSP', 'ENTRYDSP = 92D BIT 13 FLAG 6', kind='data', line=247)
S('SKIP', 'label', 0o64367, line=248)
# Page 794
W('26,2367', 0o41700, '', 'CS', 'CMDAPMOD', 'GO DIRECTLY TO P63 IF BODY ATTITUDE', line=250)
W('26,2370', 0o75017, '', 'MASK', 'ONE', 'IS SUCH THAT THE DELAY TASK: WAKEP62', line=251)
W('26,2371', 0o00006, '', 'EXTEND', '', 'WILL BE OMITTED.', line=252)
W('26,2372', 0o12421, '', 'BZF', 'P63.1', 'DISABLE GRP 4, GO TO ENDOFJOB.', line=253)
# (I.E., CONTINUE IF CMDAPMOD = -1, OR +0)
W('26,2373', 0o02405, '', 'TC', 'P63', line=255)

# PUT JOB TO SLEEP UNTIL VEHICLE MANEUVER HAS
# REDUCED ALFA TO +/-45 DEG. CONSIDER REMAINING
# 65 DEG (25 DEG IF ALFA NEG) TO ALFA TRIM TO
# OCCUR AT 3 DEG/SEC, AND TERMINATE P62 AT THAT
# TIME.

# TASK WAKEP62 IS CALLED FROM ENTRY DAP.
W('26,2374', 0o35065, 'WAKEP62', 'CA', 'PRIO13', line=264)
W('26,2375', 0o05134, '', 'TC', 'NOVAC', line=265)
#   EBANK= AOG
W('26,2376', 0o02405, '', '2CADR', 'P63', kind='data', line=267)
W('26,2377', 0o54066, kind='data', line=267)

W('26,2400', 0o05324, '', 'TC', 'TASKOVER', line=269)

# EACH 2 SEC, CALCULATE GIMBAL ANGLES FOR ENTRY CON-
# DITIONS THAT WILL HOLD IF REORIENTATION WERE MADE
# AT PRESENT RN, VN.  COME HERE FROM CM/POSE AND ALSO
# IN KEPLER PHASE OF ENTRY.

W('26,2401', 0o52131, 'P62.3', 'SSP', 'GOTO', 'SET RETURN ADDRESS SO THAT ROUTINE', kind='interp', line=276)
W('26,2402', 0o00053, '', '', 'QPRET', 'GOES DIRECTLY TO ENTRY GUIDANCE EXIT', kind='operand', line=277)
W('26,2403', 0o53576, '', '', 'ENDEXIT', 'THAT DOES ENTRY DISPLAY, GRP 5.', kind='operand', line=278)
W('26,2404', 0o20376, '', '', 'S62.3', "PUT DESIRED CDU VALUES IN CPHI'S FOR", kind='operand', line=279)
# N22 DISPLAY.

# Page 795
# P63
# PROGRAM:      P63
# MOD NO:       0       MAR. 13, 1967
# MOD BY:       R. HIRSCHKOP
# MOD NO: 1     MOD BY: RR BAIRNSFATHER         DATE: 22 JUN 67         RESTARTS
# MOD NO: 2     MOD BY: RR BAIRNSFATHER         DATE: 14 JUL 67         REVISED RESTARTS
# FUNCTION:     1) TO INITIALIZE THE ENTRY EQUATIONS.
# 2) TO CONTINUE TO HOLD THE CM TO THE CORRECT ATTITUDE WITH RESPECT TO THE ATMOSPHERE FOR
# THE ONSET OF ENTRY DECELERATION.  ROLL ANGLE IS LIFT UP/DOWN AS SPECIFIED BY HEADSUP.
# 3) TO SENSE .05G.
# CALLING SEQUENCE:  DIRECTLY FROM P62
# EXIT:         TO ENDOFJOB
# SUBROUTINE CALLS:  NEWMODEX, GODSPR

#   COUNT* $$/P63

W('26,2405', 0o05354, 'P63', 'TC', 'NEWMODEX', line=299)
W('26,2406', 0o00077, '', 'MM', '63', kind='data', line=300)

# ARRIVE WITH EBANK = AOG.

W('26,2407', 0o32430, '', 'CA', 'ENTCADR', 'CONTINUE AT STARTENT AFTER CM/POSE.', line=304)

# AT END OF STATEMENT, CHANGE ADDRESS IN GOTOADDR
# TO CONTINUE AT SCALEPOP THEREAFTER.

W('26,2410', 0o55724, '', 'TS', 'POSEXIT', line=309)

W('26,2411', 0o32427, '', 'CA', 'V06N64', 'G             VI              R TO SPLSH', line=311)
# XXX.XX G      XXXX. FPS       XXXX.X NM
W('26,2412', 0o55263, '', 'TS', 'ENTRYVN', 'FOR DISPLAY CALL IN OVERNOUT', line=313)

W('26,2413', 0o45017, '', 'CS', 'ONE', 'IN CASE FLAG IS LEFT AT +1 BY DAP.  THE', line=315)
W('26,2414', 0o55727, '', 'TS', 'P63FLAG', '-1 ASSURES THAT EXO-ATM DAP WILL NOT', line=316)
# CALL P63 OUT OF SEQUENCE IN P66.

W('26,2415', 0o05412, '', 'TC', 'PHASCHNG', 'THIS IS REQUIRED TO PRESERVE CLEANDSP', line=319)
W('26,2416', 0o00004, '', 'OCT', '00004', 'RETURN IN EVENT OF AN EXTENDED VERB', kind='data', line=320)

W('26,2417', 0o04662, '', 'TC', 'BANKCALL', "FLUSH 'N22' DISPLAY, IF ON, (OMIT", line=322)
W('26,2420', 0o20703, '', 'CADR', 'CLEANDSP', "DISPLAY DURING 'STARTENT' PASS.)", kind='data', line=323)

W('26,2421', 0o05412, 'P63.1', 'TC', 'PHASCHNG', line=325)
W('26,2422', 0o00004, '', 'OCT', '00004', 'DISABLE.  DISPLAY RESTARTED VIA ENTRY.', kind='data', line=326)

W('26,2423', 0o05217, '', 'TC', 'ENDOFJOB', line=328)

W('26,2424', 0o01474, 'V06N60', 'VN', '0660', kind='data', line=330)
W('26,2425', 0o01475, 'V06N61', 'VN', '0661', kind='data', line=331)
W('26,2426', 0o01477, 'V06N63', 'VN', '0663', kind='data', line=332)
# Page 796
W('26,2427', 0o01500, 'V06N64', 'VN', '0664', kind='data', line=334)
W('26,2430', 0o52000, 'ENTCADR', 'CADR', 'STARTENT', kind='data', line=335)

#   EBANK= RTINIT  # TO CARRY OVER INTO ENTRY STEERING.
W('26,2431', 0o03470, 'POSECADR', '2CADR', 'CM/POSE', kind='data', line=338)
W('26,2432', 0o76067, kind='data', line=338)

# Page 797
# PROGRAM:      P64
# MOD NO:       1       SEPT. 19, 1967
# MOD BY:       R. HIRSCHKOP
# MOD NO: 2     MOD BY: RR BAIRNSFATHER         DATE: 8 MAY 68          REVISED COMMENTS FOR COLOSSUS
# FUNCTION:     1.  TO START ENTRY GUIDANCE AT .05G SELECTING ROLL ATTITUDE, CONSTANT DRAG LEVEL, AND
# DRAG THRESHOLD, KA, WHICH ARE KEYED TO THE .05G POINT.
# 2.  SELECT FINAL PHASE P67 IF V < 27000 FPS WHEN .2G OCCURS.
# 3.  ITERATE FOR UP-CONTROL SOLUTION P65 IF V > 27000 FPS AND IF ALTITUDE RATE AND DRAG
# LEVEL CONDITIONS ARE SATISFIED.  ENTER P65 WHEN CONSTANT DRAG CONTROLLER HAS BROUGHT RANGE
# AS PREDICTED TO WITHIN 25 NM OF DESIRED RANGE.
# 4.  SELECT FINAL PHASE  P67  IF NO UP-CONTROL SOLUTION EXISTS WITH VL > 18000 FPS.
# CALLING SEQUENCE:  BY RTB FROM REENTRY CONTROL
# EXIT:         BACK TO REENTRY CONTROL.
# SUBROUTINE CALLS:  NEWMODEX

#   BANK 25
#   SETLOC P60S1
#   BANK

# THIS DISPLAY IS CALLED EACH PASS THROUGH STEERING.  RESTART PROTECTION IS VIA STEERING.

#   COUNT* $$/P64

W('26,2433', 0o05354, 'P64', 'TC', 'NEWMODEX', 'ENTER VIA RTB WHEN .05G IS EXCEEDED.', line=364)
W('26,2434', 0o00100, '', 'MM', '64', kind='data', line=365)
W('26,2435', 0o32440, '', 'CA', 'V06N74', 'ROLLC         VI              D', line=366)
# XXX.XX DEG    XXXXX. FPS      XXX.XX G
W('26,2436', 0o55263, '', 'TS', 'ENTRYVN', 'DISPLAY VIA OVERNOUT.', line=368)

W('26,2437', 0o06030, '', 'TC', 'DANZIG', '... AND CONTINUE IN INITROLL ...', line=370)

W('26,2440', 0o01512, 'V06N74', 'VN', '0674', kind='data', line=372)

# Page 798
# PROGRAM:      P65
# MOD NO:  0    MOD BY:  RR BAIRNSFATHER        DATE:  17 JAN 68        COLOSSUS GSOP ADDITION.
# FUNCTION:     TO CONTINUE ENTRY GUIDANCE, USING THE UP-CONTROL PHASE TO STEER TO A CONTROLLED EXIT
# CONDITION.  THIS PHASE TERMINATES  A) IF D < Q7 FPSS, GOTO TO P66.
# B) IF RDOT NEG, AND IF V < VL +500 FPS, GO TO P67.
# CALLING SEQUENCE:  BY RTB FROM REENTRY CONTROL
# EXIT:         BACK TO REENTRY CONTROL, OR TO ENDOFJOB.
# SUBROUTINE CALLS:  NEWMODEX

#   COUNT* $$/P65

W('26,2441', 0o05354, 'P65', 'TC', 'NEWMODEX', 'ENTER VIA RTB WHEN RANGE < 25 N M OF', line=386)
W('26,2442', 0o00101, '', 'MM', '65', 'TARGET.', kind='data', line=387)

W('26,2443', 0o35065, '', 'CA', 'PRIO13', line=389)
W('26,2444', 0o05134, '', 'TC', 'NOVAC', line=390)
#   EBANK= ENTRYVN
W('26,2445', 0o02457, '', '2CADR', 'P65.1', kind='data', line=392)
W('26,2446', 0o54062, kind='data', line=392)

W('26,2447', 0o05372, '', 'TC', '2PHSCHNG', '2 PHASE CHG REQUIRED TO PREVENT RE-', line=394)
W('26,2450', 0o00554, '', 'OCT', '00554', 'STARTING FLASHING DISPLAY TWICE.', kind='data', line=395)
W('26,2451', 0o10035, '', 'OCT', '10035', '4.55 SPOT AND SERVICER, HERE.', kind='data', line=396)
W('26,2452', 0o06006, '', 'TC', 'INTPRET', line=397)
W('26,2453', 0o47131, '', 'SSP', 'RTB', kind='interp', line=398)
W('26,2454', 0o03646, '', '', 'GOTOADDR', 'CHANGE ENTRY MODE TO UPCONTRL.', kind='operand', line=399)
W('26,2455', 0o53035, '', '', 'UPCONTRL', kind='operand', line=400)
W('26,2456', 0o52120, '', '', 'REFAZE10', 'GO HERE TO REESTABLISH ENTRY SEQUENCER.', kind='operand', line=401)
# AND CONTINUE AT UPCONTRL...

W('26,2457', 0o05560, 'P65.1', 'TC', 'DOWNFLAG', line=404)
W('26,2460', 0o00134, '', 'ADRES', 'ENTRYDSP', 'ENTRYDSP = 92D BIT 13 FLAG 6', kind='data', line=405)

W('26,2461', 0o32473, '', 'CA', 'V16N69', 'ROLLC         DL (Q7)         VL', line=407)
W('26,2462', 0o04662, '', 'TC', 'BANKCALL', 'XXX.XX DEG    XXX.XX G        XXXXX. FPS', line=408)
W('26,2463', 0o21057, '', 'CADR', 'GOFLASHR', kind='data', line=409)
W('26,2464', 0o02461, '', 'TC', '-3', 'NODOFLAG IS SET ...', line=410)
W('26,2465', 0o02470, '', 'TC', '+3', line=411)
W('26,2466', 0o02461, '', 'TC', '-5', line=412)
W('26,2467', 0o02232, '', 'TC', 'P61.3', 'EST. GRP 4 FOR DISPLAY AND DO ENDOFJOB', line=413)
# IF PROCEED, CONTINUE
W('26,2470', 0o05546, '', 'TC', 'UPFLAG', line=415)
W('26,2471', 0o00134, '', 'ADRES', 'ENTRYDSP', 'ENTRYDSP = 92D BIT 13 FLAG 6', kind='data', line=416)

W('26,2472', 0o02421, '', 'TC', 'P63.1', 'DISABLE GRP 4, START UP ENTRY DISPLAY', line=418)
# N06V68 VIA OVERNOUT, AS USED IN P64
W('26,2473', 0o04105, 'V16N69', 'VN', '1669', kind='data', line=420)

# Page 799
# PROGRAM:      P66
# MOD NO: 0     MOD BY: RR BAIRNSFATHER         DATE: 17 JAN 68         COLOSSUS GSOP ADDITIONS
# FUNCTION:     KEEP CM ATTITUDE IN TRIM TO THE RELATIVE VELOCITY VECTOR.  ENTRY GUIDANCE STOPS GENERATING
# ROLL COMMANDS UNTIL DRAG BUILDS UP TO Q7+0.5 FPSS.
# CALLING SEQUENCE:  VIA RTB FROM REENTRY CONTROL.
# EXIT:         BACK TO REENTRY CONTROL.
# SUBROUTINE CALLS:  NEWMODEX

#   COUNT* $$/P66

W('26,2474', 0o05354, 'P66', 'TC', 'NEWMODEX', 'ENTER VIA RTB WHEN D < Q7 FPSS', line=433)
W('26,2475', 0o00102, '', 'MM', '66', kind='data', line=434)

W('26,2476', 0o35052, '', 'CA', 'V06N22', 'OGA           IGA             MGA', line=436)
# XXX.XX DEG    XXX.XX DEG      XXX.XX DEG
W('26,2477', 0o02503, '', 'TC', 'P66END', 'IN CASE CAME FROM P65, GO TO DISABLE GRP 4,', line=438)
# AND SET ENTRYDSP TO DO DISPLAY VIA
# OVERNOUT.

# ... AND CONTINUE AT KEP2

# Page 800
# PROGRAM:      P67
# MOD NO:       0       MAR. 16, 1967
# MOD BY:       R. HIRSCHKOP
# FUNCTION:     TO TERMINATE STEERING WHEN THE CM VELOCITY WRT EARTH = 1000 FT/SEC
# CALLING SEQUENCE:
# EXIT:         TO POOH
# SUBROUTINE CALLS:  GOFLASH

# THIS DISPLAY IS CALLED EACH PASS THROUGH STEERING.  RESTART PROTECTION IS VIA STEERING.

#   COUNT* $$/P67

W('26,2500', 0o05354, 'P67', 'TC', 'NEWMODEX', 'ENTER VIA RTB', line=457)
W('26,2501', 0o00103, '', 'MM', '67', kind='data', line=458)
W('26,2502', 0o32511, '', 'CA', 'V06N66', 'ROLLC         XRNGERR         DNRNGERR', line=459)
# XXX.XX DEG    XXXX.X NM       XXXX.X NM
W('26,2503', 0o55263, 'P66END', 'TS', 'ENTRYVN', 'DISPLAY VIA OVERNOUT.', line=461)

W('26,2504', 0o05546, '', 'TC', 'UPFLAG', '(IN CASE CAME FROM P65.  ENTRY DISPLAY', line=463)
W('26,2505', 0o00134, '', 'ADRES', 'ENTRYDSP', 'WILL FLUSH FLASHING DISP.  IF STILL ON)', kind='data', line=464)
# BIT 13 FLAG 6
W('26,2506', 0o05412, 'KILLGRP4', 'TC', 'PHASCHNG', 'DISABLE GRP4, IN CASE CAME FROM HUNTEST.', line=466)
W('26,2507', 0o00004, '', 'OCT', '00004', '(COME TO KILLGRP4 VIA RTB, RET TO CALLER)', kind='data', line=467)

W('26,2510', 0o06030, '', 'TC', 'DANZIG', '... AND CONTINUE AT PREDICT3 ...', line=469)

W('26,2511', 0o01502, 'V06N66', 'VN', '0666', kind='data', line=471)

#   BANK 26
#   SETLOC P60S2
#   BANK

W('26,2512', 0o32543, 'P67.1', 'CA', 'V16N67', 'RTOGO         LAT             LONG', line=477)
# XXXX.X NM     XXX.XX DEG      XXX.XX DEG
W('26,2513', 0o04662, '', 'TC', 'BANKCALL', line=479)
W('26,2514', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=480)
W('26,2515', 0o02520, '', 'TC', '+3', 'EFFECTIVE GOTOPOOH', line=481)
W('26,2516', 0o02520, '', 'TC', '+2', line=482)
W('26,2517', 0o02512, '', 'TC', 'P67.1', 'REDO', line=483)

W('26,2520', 0o46214, '', 'CS', 'THREE', 'TURN OFF ENTRY DAP', line=485)
W('26,2521', 0o00004, '', 'INHINT', line=486)
W('26,2522', 0o70102, '', 'MASK', 'CM/FLAGS', 'CM/DSTBY, GAMDIFSW', line=487)
W('26,2523', 0o54102, '', 'TS', 'CM/FLAGS', line=488)
W('26,2524', 0o00003, '', 'RELINT', line=489)
W('26,2525', 0o00006, '', 'EXTEND', line=490)
W('26,2526', 0o32643, '', 'DCA', 'SERVCAD2', line=491)

# Page 801
W('26,2527', 0o53223, '', 'DXCH', 'AVEGEXIT', line=494)

W('26,2530', 0o14106, '', 'TCF', 'GOTOPOOH', line=496)

# Page 802
W('26,2531', 0o43175, 'P67.2', 'VLOAD', 'CLEAR', 'CALC PRESENT LAT, LONG, ALT.', kind='interp', line=499)
W('26,2532', 0o01171, '', '', 'RN', kind='operand', line=500)
W('26,2533', 0o00662, '', '', 'ERADFLAG', 'USE PAD RAD FOR ALT. (NOT SEEN ANYWAY)', kind='operand', line=501)
W('26,2534', 0o16152, '', 'STODL', 'ALPHAV', kind='interp', line=502)
W('26,2535', 0o01205, '', '', 'PIPTIME', 'USE TIME OF RN', kind='operand', line=503)
W('26,2536', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=504)
W('26,2537', 0o01663, '', '', 'LUNAFLAG', kind='operand', line=505)
W('26,2540', 0o26370, '', '', 'LAT-LONG', kind='operand', line=506)
W('26,2541', 0o77634, 'P67.3', 'RTB', '', 'ENTRY EXIT THAT OMITS DISPLAY.', kind='interp', line=507)
W('26,2542', 0o53611, '', '', 'SERVNOUT', kind='operand', line=508)

W('26,2543', 0o04103, 'V16N67', 'VN', '1667', kind='data', line=510)
S('OCT41', 'equals', 0o4270, line=511)
S('SERVCAD2', 'equals', 0o64642, line=512)

# Page 803
# SUBROUTINE NAME:      S61.1
# MOD NO:       0                                       DATE:           21 FEB 67
# MOD BY:       RR BAIRNSFATHER                         LOG SECTION:    P61-P67
# MOD NO:       1       MOD BY: RR BAIRNSFATHER         DATE:           22 JUN 67       RESTARTS.
# FUNCTIONAL DESCRIPTION:       CALLED BY BOTH P61 AND P62
# FIRST, TEST TO SEE IF  AVERAGEG  IS ON.  IF NOT, UPDATE THE STATE VECTOR TO PRESENT TIME + TOLERANCE
# AND TURN ON  AVERAGEG  AT THAT TIME, AND CONTINUE.  OTHERWISE CONTINUE:  SEE IF IMU Y AXIS IS
# WITHIN 30 DEG OF VAR.  IF YES, EXIT SUBROUTINE S61.1.  IF SO, SEE IF -Y AXIS OF IMU IS WITHIN
# 30 DEG OF VAR.  IF YES, DISPLAY ALARM:  01427   IMU REVERSED.
# IF NO, DISPLAY ALARM:   01426   IMU UNSATISFACTORY.
# IN EITHER OF THESE LAST 2 CASES, WAIT 10 SEC AND THEN EXIT SUBROUTINE S61.1.
#
# REMARK:       THERE WILL BE A SHORT 10 SEC DELAY IF AN ALARM EXIT IS TAKEN.  THE DELAY FOR INTEGRATION IS
# AS SHORT AS CAN BE MADE, BUT IS ARBITRARY SINCE IT DEPENDS ON THE AGE OF THE STATE VECTOR.
#
# CALLING SEQUENCE:     CALL
# S61.1
#
# C(MPAC) UNSPECIFIED
# PUSHLOC UNSPECIFIED
#
# SUBROUTINES CALLED:   LOADTIME, CSMPREC, TPAGTREE,
# WAITLIST, JOBSLEEP, JOBWAKE, PREREAD, ALARM, GODSPR, BANKCALL, DELAYJOB
#
# NORMAL EXIT MODES:    RVQ
#
# ALARMS:       01426   IMU UNSATISFACTORY
# 01427   IMU REVERSED
#
# OUTPUT:       POSSIBLE ALARMS
# POSSIBLY TDEC1, RATT, VATT, RN, VN
#
# ERASABLE INITIALIZATION REQUIRED:
# AVEGFLAG                AVERAGEG ON OR OFF                              LEFT BY SERVICER
# PIPTIME   (-28) CS      TIME OF PIPA UPDATE                             LEFT BY READACCS
# RN        (-29) M       STATE VECTOR                                    LEFT BY AVERAGEG
# VN        (-7) M/CS     STATE VECTOR                                    LEFT BY AVERAGEG
# REFSMMAT  (-1)          .5 REF TO SM MATRIX                             LEFT BY LAST IMU ALIGNMENT
#
# DEBRIS:       QPRET
# POSSIBLY PIPTIME1, RATT, VATT, TDEC1, RN1, VN1, QTEMP, X1       IF UPDATED
# PUSH LIST LOCS USED BY CSMPREC

#   EBANK= AOG  # FOR 60GENRET, S61DT
#   BANK 26
#   SETLOC P60S3
#   BANK

#   COUNT* $$/S61.1

W('26,2544', 0o00006, 'S61.1', 'EXTEND', line=565)
W('26,2545', 0o23773, '', 'QXCH', '60GENRET', 'SAVE RET ADDR IN EB 6', line=566)
W('26,2546', 0o04662, '', 'TC', 'BANKCALL', line=567)
W('26,2547', 0o17653, '', 'CADR', 'R02BOTH', kind='data', line=568)
W('26,2550', 0o06006, '', 'TC', 'INTPRET', line=569)
# Page 804
W('26,2551', 0o45014, '', 'BON', 'CALRB', kind='interp', line=571)
W('26,2552', 0o00716, '', '', 'AVEGFLAG', 'IS AVERAGEG ON', kind='operand', line=572)
W('26,2553', 0o54604, '', '', 'S61.1A', 'YES', kind='operand', line=573)
W('26,2554', 0o27543, '', '', 'MIDTOAV2', 'GET FUTURE STATE VECTOR SOON AS CAN', kind='operand', line=574)

W('26,2555', 0o30155, '', 'CA', 'MPAC +1', 'RETURN INHINTED ***', line=576)
W('26,2556', 0o55774, '', 'TS', 'S61DT', 'FOR RESTART.', line=577)
W('26,2557', 0o05245, '', 'TC', 'WAITLIST', line=578)
#   EBANK= DVCNTR
W('26,2560', 0o02565, '', '2CADR', 'S61.1C', kind='data', line=580)
W('26,2561', 0o54067, kind='data', line=580)

W('26,2562', 0o05412, '', 'TC', 'PHASCHNG', line=582)
W('26,2563', 0o40434, '', 'OCT', '40434', kind='data', line=583)
W('26,2564', 0o05217, '', 'TC', 'ENDOFJOB', line=584)

W('26,2565', 0o35065, 'S61.1C', 'CA', 'PRIO13', line=586)
W('26,2566', 0o05147, '', 'TC', 'FINDVAC', line=587)
#   EBANK= AOG
W('26,2567', 0o02603, '', '2CADR', 'S61.1A -1', kind='data', line=589)
W('26,2570', 0o54066, kind='data', line=589)

W('26,2571', 0o00006, '', 'EXTEND', line=591)
W('26,2572', 0o32643, '', 'DCA', 'SERVCAD1', 'HE WHO START AVERAGEG MUST SERVICE', line=592)
W('26,2573', 0o53223, '', 'DXCH', 'AVEGEXIT', 'THE EXIT.', line=593)

W('26,2574', 0o05372, '', 'TC', '2PHSCHNG', line=595)
W('26,2575', 0o00454, '', 'OCT', '00454', kind='data', line=596)
W('26,2576', 0o00415, '', 'OCT', '00415', kind='data', line=597)

W('26,2577', 0o35060, '', 'CA', 'EBENTRY', 'SET EB= 7 FOR PREREAD.', line=599)
W('26,2600', 0o54003, '', 'TS', 'EBANK', line=600)

W('26,2601', 0o04701, '', 'TC', 'POSTJUMP', line=602)
W('26,2602', 0o76701, '', 'CADR', 'PREREAD', 'PREREAD DOES TC TASKOVER.', kind='data', line=603)

W('26,2603', 0o06006, '', 'TC', 'INTPRET', line=605)
W('26,2604', 0o77204, 'S61.1A', 'BOVB', 'VLOAD', kind='interp', line=606)
W('26,2605', 0o57352, '', '', 'TCDANZIG', 'TURN OFF OVFIND, IF ON', kind='operand', line=607)
W('26,2606', 0o01177, '', '', 'VN', 'VN    (-7) M/CS', kind='operand', line=608)
W('26,2607', 0o64235, '', 'VXV', 'MXV', kind='interp', line=609)
W('26,2610', 0o01171, '', '', 'RN', 'RN    (-29) M', kind='operand', line=610)
W('26,2611', 0o01736, '', '', 'REFSMMAT', '.5 UNIT MATRIX', kind='operand', line=611)
W('26,2612', 0o71256, '', 'UNIT', 'DLOAD', kind='interp', line=612)
W('26,2613', 0o00160, '', '', 'MPAC +3', 'GET COS(THETA)/2', kind='operand', line=613)
W('26,2614', 0o43240, '', 'BMN', 'DAD', kind='interp', line=614)
W('26,2615', 0o54622, '', '', 'S61.1B', 'DO TEST ON -YSM', kind='operand', line=615)
W('26,2616', 0o14645, '', '', 'C(30)LIM', '= 1.0 -.5 COS(30)', kind='operand', line=616)
W('26,2617', 0o47004, '', 'BOVB', 'RTB', kind='interp', line=617)
W('26,2620', 0o54641, '', '', 'RETRN1', kind='operand', line=618)
W('26,2621', 0o54626, '', '', 'RETRN3', kind='operand', line=619)
# Page 805
W('26,2622', 0o43276, 'S61.1B', 'DCOMP', 'DAD', kind='interp', line=621)
W('26,2623', 0o14645, '', '', 'C(30)LIM', '= 1.0 - .5 COS(30)', kind='operand', line=622)
W('26,2624', 0o77404, '', 'BOVB', 'EXIT', kind='interp', line=623)
W('26,2625', 0o54631, '', '', 'RETRN2', kind='operand', line=624)

W('26,2626', 0o05650, 'RETRN3', 'TC', 'ALARM', line=626)
W('26,2627', 0o01426, '', 'OCT', '01426', 'IMU UNSATISFACTORY', kind='data', line=627)
W('26,2630', 0o02633, '', 'TC', 'RETRN2 +2', line=628)

W('26,2631', 0o05650, 'RETRN2', 'TC', 'ALARM', line=630)
W('26,2632', 0o01427, '', 'OCT', '01427', 'IMU REVERSED', kind='data', line=631)

W('26,2633', 0o35050, '', 'CAF', 'V05N09', line=633)
W('26,2634', 0o04662, '', 'TC', 'BANKCALL', line=634)
W('26,2635', 0o20676, '', 'CADR', 'GODSPR', 'DO DISPLAY', kind='data', line=635)
W('26,2636', 0o32646, '', 'CA', '10SECS', line=636)
W('26,2637', 0o04662, '', 'TC', 'BANKCALL', line=637)
W('26,2640', 0o01732, '', 'CADR', 'DELAYJOB', kind='data', line=638)

W('26,2641', 0o01773, 'RETRN1', 'TC', '60GENRET', line=640)

#   EBANK= DVCNTR
W('26,2642', 0o03227, 'SERVCAD1', '2CADR', 'SERVEXIT', kind='data', line=643)
W('26,2643', 0o76067, kind='data', line=643)

W('26,2644', 0o22111, 'C(30)LIM', '2DEC', '.566985', '= 1.0 - .5 COS(30)', kind='data', line=645)
W('26,2645', 0o17335, kind='data', line=645)

W('26,2646', 0o01750, '10SECS', 'DEC', '1000', '1000 CS', kind='data', line=647)
W('26,2647', 0o00000, '60SECDP', '2DEC', '6000 B-28', '6000 CS', kind='data', line=648)
W('26,2650', 0o13560, kind='data', line=648)

# Page 806
# PROGRAM NAME:         S61.2                   DATE:           14 FEB 67
# MOD NO:       1                               LOG SECTION:    P61-P67
# MOD BY:       NORTH / BAIRNSFATHER
# MOD NO: 2     MOD BY: NORTH/BAIRNSFATHER      DATE: 11 MAY 67         ADD 2ND ITER FOR ERAD AT 400K FT.
# MOD NO: 3     MOD BY: RR BAIRNSFATHER         DATE: 21 NOV 67         VARIABLE MU ADDED.
# MOD NO: 4     MOD BY: RR BAIRNSFATHER         DATE: 21 MAR 68         DIFFERENT EARTH/MOON SCALES IN TFF'S
#
# FUNCTIONAL DESCRIPTION:  CALLED IN P61.  PROVIDES DISPLAYS FOR NOUNS  N60  AND  N63 .
# PROGRAM CALCULATES ENTRY DISPLAY OF MAXIMUM ACCELERATION EXPECTED  (GMAX)  AND ALSO THE EXPECTED
# INERTIAL VELOCITY (VPRED) AND ENTRY ANGLE  (GAMMAEI)  THAT WILL OBTAIN AT 400K FT ABOVE THE FISCHER
# ELLIPSOID.  PROGRAM ALSO CALCULATES A SECOND DISPLAY RELATIVE TO THE  EMSALT  ABOVE FISCHER ELLIPSOID
# AND CONSISTS OF RANGE TO SPLASH FROM NOW  (RTGO) , PREDICTED INERTIAL VELOCITY  (VIO) , AND THE TIME TO
# GO FROM NOW  (TTE) .
#
# CALLING SEQUENCE:     CALL
# S61.2
# C(MPAC) UNSPECIFIED
# PUSHLOC WILL BE SET TO ZERO.
#
# SUBROUTINES CALLED:   TFFCONIC, CALCTFF, TFF/TRIG, FISHCALC, GETERAD, VGAMCALC
#
# NORMAL EXIT MODES:    RTB, P61.1
#
# ALARMS:       NONE
#
# OUTPUT:       THE FOLLOWING REGISTERS ARE WRITTEN IN FOR USE BY DISPLAYS
# GMAX    100 GMAX (-14) G,S      MAXIMUM ACCELERATION
# VPRED   (-7) M/CS               PREDICTED VELOCITY AT 400K FT
# GAMMAEI GAMMA/360               PREDICTED GAMMA    AT 400K FT
# FOR TM, DP(GAMMAEI) = (GAMMAEI, RTGO) / 360
# RTGO    THETAH/360              RANGE ANGLE TO SPLASH FROM EMSALT       EMSALT IS PAD LOADED.
# VIO     (-7) M/CS               INTERTIAL VELOCITY AT      EMSALT       EMSALT IS PAD LOADED.
# TTE     (-28) CS                TIME TO                    EMSALT       EMSALT IS PAD LOADED.
# PUSHLOC = 0
# CONIC PARAMETERS STORED IN VAC AREA (SEE TFF SUBROUTINES)
#
# ERASABLE INITIALIZATION REQUIRED:
# RONE    (-29) M                 STATE VECTOR                            LEFT BY USER
# VONE    (-7) M/CS               STATE VECTOR                            LEFT BY USER
# URONE   UR/2                                                            LEFT BY USER
# UNI     (-1)                    UNIT NORMAL V*R                         LEFT BY ENTRY / P61
# THETAH  THETAH/360              RANGE ANGLE                             LEFT BY ENTRY / P61
# UNITW   (0)                     UNIT POLAR VECTOR                       LEFT BY PAD LOAD
# EMSALT  (-29) M                 EMS INTERFACE ALTITUDE                  LEFT BY PAD LOAD
# ORBITAL REENTRY: 284843 FT., LUNAR REENTRY: 297431 FT.
#
# DEBRIS:       QPRET,
# ALL PDL LOCATIONS ABOVE 12D, INCLUDING X1,X2,S1,S2
# ALSO PDL+0 ... PDL+5, WHERE INITIAL PUSHLOC = PDL

# Page 807
# THE FOLLOWING PUSH LIST LOCATIONS HAVE BEEN RESERVED FOR TFF ROUTINES AND ARE REPEATED HERE FOR CONVENIENCE.
# OF COURSE FOR S61.2 USAGE, EARTH ORIGIN SCALING IS USED.
#
# BELOW   E:  IS USED FOR EARTH ORIGIN SCALE
# M:  IS USED FOR MOON ORIGIN SCALE
#
# RTERM   =       18D             TERMINAL RADIUS M       E:  (-29)       M:  (-27)
# NRTERM  =       16D             TERMINAL RADIUS M       E:  (-29+NR)
# M:  (-27+NR)
# RMAG1   =       12D             PRESENT RADIUS M        E:  (-29)       M:  (-27)
# NRMAG   =       32D             PRESENT RADIUS M        E:  (-29+NR)
# M:  (-27+NR)
# SDELF/2                         SIN(THETA) / 2
# CDELF/2 =       14D             COS(THETA) / 2
# TFFX    =       34D             X, ARGUMENT OF SERIES T(X)
# TFFTEM  =       36D             ARG FOR TRANSFER ANGLE CALCULATION
# TFFNP   =       28D             LC P M                  E:  (-38+2NR)   M:  (-36+2NR)
# TFF/RTMU=       30D             1/SQRT(MU)              E:  (17)        M:  (14)
# TFFVSQ  =       20D             -(VN.VN/MU)     1/M     E:  (20)        M:  (18)

# Page 808
#   BANK 34
#   SETLOC P60S2
#   BANK

#   COUNT* $$/S61.2
# PDL LEFT AT ZERO BY TARGETING

W('26,2651', 0o45345, 'S61.2', 'DLOAD', 'DSU', kind='interp', line=730)
W('26,2652', 0o02020, '', '', 'EMSALT', kind='operand', line=731)
W('26,2653', 0o15001, '', '', '290KFT', kind='operand', line=732)
W('26,2654', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=733)
W('26,2655', 0o54775, '', '', 'LUNENT', kind='operand', line=734)
W('26,2656', 0o17354, '', '', '1/RTMU', 'ESTABLISH MU FOR ORBITAL ENTRIES', kind='operand', line=735)
W('26,2657', 0o77624, 'CALLCON', 'CALL', kind='interp', line=736)
W('26,2660', 0o56757, '', '', 'TFFCONIC', 'FILL VAC AREA WITH CONIC PARAMETERS', kind='operand', line=737)

W('26,2661', 0o45145, '', 'DLOAD', 'CALL', kind='interp', line=739)
W('26,2662', 0o15021, '', '', 'RTRIAL', '1ST GUESS AT TERMINAL RADIUS  (-29)', kind='operand', line=740)
W('26,2663', 0o57067, '', '', 'CALCTFF', 'SAVES MPAC IN RTERM           (18D)', kind='operand', line=741)

W('26,2664', 0o77624, '', 'CALL', '', 'CALC SDELF/2, CDELF/2', kind='interp', line=743)
W('26,2665', 0o56631, '', '', 'TFF/TRIG', 'RETURN WITH S(THETA) IN MPAC', kind='operand', line=744)

W('26,2666', 0o77624, '', 'CALL', '', 'GET FISCHER RADIUS            (-29) M', kind='interp', line=746)
W('26,2667', 0o55030, '', '', 'FISHCALC', 'ANS IN MPAC AND IN ERADM', kind='operand', line=747)

W('26,2670', 0o45015, '', 'DAD', 'CALL', kind='interp', line=749)
W('26,2671', 0o02020, '', '', 'EMSALT', kind='operand', line=750)
W('26,2672', 0o57067, '', '', 'CALCTFF', 'SAVES MPAC IN RTERM           (18D)', kind='operand', line=751)

W('26,2673', 0o77676, '', 'DCOMP', '', 'NEGATIVE AS IN COUNTDOWN', kind='interp', line=753)
W('26,2674', 0o03733, '', 'STORE', 'TTE1', 'DECR TTE FROM BASB TTE1.  (RESTART)', kind='interp', line=754)
# DNLIST AND DSKY WILL USE TTE.
W('26,2675', 0o37727, '', 'STCALL', 'TTE', 'LET MISS CONTRL DECR BY ELAPSED TIME', kind='interp', line=756)
# TTE= TIME FROM NOW TO EMSALT +FISCHER

W('26,2676', 0o56631, '', '', 'TFF/TRIG', 'S(THETA) IN MPAC ON RETURNING', kind='operand', line=759)
# AND THETA= RANGE FROM NOW TO EMSALT

W('26,2677', 0o77624, '', 'CALL', kind='interp', line=762)
W('26,2700', 0o55030, '', '', 'FISHCALC', kind='operand', line=763)
W('26,2701', 0o77624, '', 'CALL', kind='interp', line=764)
W('26,2702', 0o56664, '', '', 'VRCALC', kind='operand', line=765)
W('26,2703', 0o77624, '', 'CALL', kind='interp', line=766)
W('26,2704', 0o56651, '', '', 'DISPTARG', kind='operand', line=767)
W('26,2705', 0o77624, '', 'CALL', kind='interp', line=768)
W('26,2706', 0o56651, '', '', 'DISPTARG', kind='operand', line=769)
W('26,2707', 0o37714, '', 'STCALL', 'RTGO', kind='interp', line=770)
# Page 809
W('26,2710', 0o55051, '', '', 'VGAMCALC', kind='operand', line=772)

W('26,2711', 0o77605, '', 'DMP', '', 'MPAC = GAMMA', kind='interp', line=774)
# PDL0 HAS VGAM.
W('26,2712', 0o43265, '', 'BDDV', 'DAD', kind='interp', line=776)
W('26,2713', 0o15027, '', '', 'VEMSCON', '-HS D 180/PI (-14)', kind='operand', line=777)
W('26,2714', 0o00001, '', '', '0', 'VGAM FROM PDL0', kind='operand', line=778)
W('26,2715', 0o17725, '', 'STODL', 'VIO', 'PREDICTED VELOCITY AT EMSALT.', kind='interp', line=779)

# GAMMA AND VGAM AT 300K FT ARE REQUIRED BY GMAX
# ALGORITHM.

W('26,2716', 0o02241, '', '', 'ERADM', 'EARTH RADIUS FROM GETERAD (-29) M', kind='operand', line=784)
# = FISCHER RADIUS (-29)

W('26,2717', 0o77615, '', 'DAD', kind='interp', line=787)
W('26,2720', 0o06462, '', '', '300KFT', 'M (-29)', kind='operand', line=788)
W('26,2721', 0o34023, '', 'STCALL', 'RTERM', 'TERMINAL RADIUS M (-29)', kind='interp', line=789)

W('26,2722', 0o55046, '', '', 'PREVGAM', 'VGAMCALC WITH NEW RTERM', kind='operand', line=791)

# VBAR = (V(FPS) - 36KF/S) / 20 F/S
# GMAX = (4/(1 + 4.8 VBARSQ))(GAM - 6.05 - 2.4 VBARSQ) - 10(L/D - .3) + 10      ASSUME L/D = 0.3, BANK =0.

# GMAXCALC
W('26,2723', 0o45325, '', 'PDDL', 'DSU', 'GAM TO PDL2', kind='interp', line=797)
W('26,2724', 0o00001, '', '', '0', 'VGAM IS IN PDL0 (-7)', kind='operand', line=798)
W('26,2725', 0o15005, '', '', '36KFT/S', '(-7) M/CS', kind='operand', line=799)
W('26,2726', 0o63471, '', 'DDV', 'DSQ', kind='interp', line=800)
W('26,2727', 0o15007, '', '', '20KFT/S', '(-6) M/CS', kind='operand', line=801)
W('26,2730', 0o00001, '', 'STORE', '0', 'VBARSQ (-2) TO PDL0', kind='interp', line=802)

W('26,2731', 0o43205, '', 'DMP', 'DAD', kind='interp', line=804)
W('26,2732', 0o15011, '', '', 'KR1', kind='operand', line=805)
# GAM, POS DOWN, FROM PDL2
W('26,2733', 0o41215, '', 'DAD', 'DMP', kind='interp', line=807)
W('26,2734', 0o15013, '', '', '-6.05DEG', kind='operand', line=808)
W('26,2735', 0o15015, '', '', 'KR2', kind='operand', line=809)
W('26,2736', 0o77725, '', 'PDDL', '', 'XCH PDL+0 FOR VBARSQ (-2)', kind='interp', line=810)
W('26,2737', 0o43271, '', 'DDV', 'DAD', kind='interp', line=811)
W('26,2740', 0o15025, '', '', 'KR4', kind='operand', line=812)
W('26,2741', 0o17366, '', '', 'DP2(-4)', kind='operand', line=813)
W('26,2742', 0o77665, '', 'BDDV', kind='interp', line=814)
# NUM FROM PDL+0
W('26,2743', 0o51015, '', 'DAD', 'BPL', kind='interp', line=816)
W('26,2744', 0o15017, '', '', 'KR3', kind='operand', line=817)
W('26,2745', 0o54750, '', '', '+3', kind='operand', line=818)
W('26,2746', 0o77745, '', 'DLOAD', kind='interp', line=819)
W('26,2747', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=820)
W('26,2750', 0o17722, '', 'STODL', 'GMAX', '100 GMAX (-14)', kind='interp', line=821)
# Page 810
# DISPLAY USES GMAX AS SP, SO LO WORD IS WRITTEN OVER BY VPRED.
W('26,2751', 0o02241, '', '', 'ERADM', '= FISCHER RADIUS (-29) M', kind='operand', line=824)
W('26,2752', 0o45015, '', 'DAD', 'CALL', '2 ND ITERATION FOR FISCHER RADIUS', kind='interp', line=825)
W('26,2753', 0o15023, '', '', '400KFT', kind='operand', line=826)
W('26,2754', 0o57067, '', '', 'CALCTFF', 'ESTABLISH TRANSFER ANGLE DATA.', kind='operand', line=827)
W('26,2755', 0o77624, '', 'CALL', kind='interp', line=828)
W('26,2756', 0o56631, '', '', 'TFF/TRIG', 'GET SIN, COS DELF', kind='operand', line=829)
W('26,2757', 0o77624, '', 'CALL', kind='interp', line=830)
W('26,2760', 0o55030, '', '', 'FISHCALC', 'GET CORRESPONDING FISCHER RADIUS.', kind='operand', line=831)

W('26,2761', 0o73015, '', 'DAD', 'LXA,2', 'SAVE HI-WORD FOR DOWNLIST.', kind='interp', line=833)
W('26,2762', 0o15023, '', '', '400KFT', 'M (-29)', kind='operand', line=834)
W('26,2763', 0o03713, '', '', 'RTGO', '(RANGE ANGLE FROM EMSALT) / 360', kind='operand', line=835)
W('26,2764', 0o34023, '', 'STCALL', 'RTERM', kind='interp', line=836)
W('26,2765', 0o55046, '', '', 'PREVGAM', 'VGAMCALC WITH NEW RTERM', kind='operand', line=837)

W('26,2766', 0o67076, '', 'DCOMP', 'SXA,2', 'HI-WORD OF EACH ON DOWNLIST.', kind='interp', line=839)
W('26,2767', 0o00155, '', '', 'MPAC +1', kind='operand', line=840)
W('26,2770', 0o17771, '', 'STODL', 'GAMMAEI', 'CONIC GAMMA/360 AT 400K FT.   (HI-WORD)', kind='interp', line=841)
# CONIC RTGO/360 FROM EMSALT   (LOW-WORD)
# FOR TM, DP(GAMMAEI) = (GAMMA, RTGO) / 360

# VGAM FROM PDL+0 (-7)
W('26,2771', 0o77626, '', 'STADR', kind='interp', line=846)
W('26,2772', 0o74010, '', 'STORE', 'VPRED', 'CONIC VELOCITY AT 400K FT', kind='interp', line=847)

W('26,2773', 0o77634, '', 'RTB', kind='interp', line=849)
W('26,2774', 0o54267, '', '', 'P61.1', kind='operand', line=850)
# PDL BACK TO ZERO.

W('26,2775', 0o52145, 'LUNENT', 'DLOAD', 'GOTO', kind='interp', line=853)
W('26,2776', 0o06456, '', '', '1/RTMUE', 'ESTABLISH MU FOR LUNAR TYPE ENTRIES', kind='operand', line=854)
W('26,2777', 0o54657, '', '', 'CALLCON', kind='operand', line=855)
W('26,3000', 0o00002, '290KFT', '2DEC', '88392.0 B-29', kind='data', line=856)
W('26,3001', 0o26244, kind='data', line=856)

W('26,3002', 0o00052, 'KTETA1', '2DEC*', '.421844723 E2 B-14*', '110 2PI/16384(163.84)', kind='data', line=858)
W('26,3003', 0o05716, kind='data', line=858)

W('26,3004', 0o33335, '36KFT/S', '2DEC', '109.728 B-7', '(-7) M/CS = 36 KFT/S (-7)', kind='data', line=860)
W('26,3005', 0o05707, kind='data', line=860)

W('26,3006', 0o36365, '20KFT/S', '2DEC', '121.92 B-7', '(-6) M/CS = 2 20KFT/S (-7)', kind='data', line=862)
W('26,3007', 0o30244, kind='data', line=862)

W('26,3010', 0o77113, 'KR1', '2DEC', '-.026666667', '= -2.4 4 / 360', kind='data', line=864)
W('26,3011', 0o42770, kind='data', line=864)

W('26,3012', 0o77354, '-6.05DEG', '2DEC', '-.016805556', '= -6.05 / 360', kind='data', line=866)
W('26,3013', 0o65030, kind='data', line=866)

W('26,3014', 0o21450, 'KR2', '2DEC', '.54931641', '= (360/4) 100 (-14) = 9000 B-14', kind='data', line=868)
W('26,3015', 0o00001, kind='data', line=868)

W('26,3016', 0o01750, 'KR3', '2DEC', '1000 B-14', '= 100 (10.0) (-14) G,S', kind='data', line=870)
W('26,3017', 0o00000, kind='data', line=870)
# Page 811
# ASSUMES L/D = 0.3, BANK =0.
W('26,3020', 0o00305, 'RTRIAL', '2DEC', '6460097.18 B-29', 'RPAD +264643 FT =21 194 545 FT', kind='data', line=873)
W('26,3021', 0o04541, kind='data', line=873)
# RPAD DEFINED AS 20 909 901.57 FT =6 373 336 M
W('26,3022', 0o00003, '400KFT', '2DEC', '121920 B-29', 'METERS', kind='data', line=875)
W('26,3023', 0o27040, kind='data', line=875)

# 300KFT        2DEC    91440 B-29      # (-29) M

# EMSALT        2DEC    86759.2 B-29    # 284643 FT (-29) M     (ORBITAL REENTRY)

# EMSALT        2DEC    90657 B-29      # 297431 FT (-29) M     (LUNAR REENTRY)

W('26,3024', 0o32525, 'KR4', '2DEC', '.833333333', kind='data', line=883)
W('26,3025', 0o12525, kind='data', line=883)

S('300KFT', 'equals', 0o56461, line=885)
W('26,3026', 0o77777, 'VEMSCON', '2DEC', '-.0389676 B-14', '= -HS D / 2 PI (-14)  M SQ / CS SQ', kind='data', line=886)
W('26,3027', 0o76601, kind='data', line=886)

# = -16369      .05G    32.2    .3048   .3048/2 PI      (-14)

# Page 812
# SUBROUTINE NAME:  FISHCALC    (USED BY S61.2)         DATE:           01.21.67
# MOD NO: 0                                             LOG SECTION:    P61-P67
# MOD BY: MORTH / BAIRNSFATHER
# MOD NO: 1     MOD BY: RR BAIRNSFATHER                 DATE:           11 MAY 67       INCLUDE GETERAD CALL
#
# FUNCTIONAL DESCRIPTION:  GIVEN THE PRESENT POSITION, UNITR, CALCULATE A NEW UNITR THAT IS ROTATED THROUGH
# TRANSFER ANGLE, THETA, ALONG THE TRAJECTORY.  THEN CALCULATE SIN(LAT) AND USE TO OBTAIN FISCHER RADIUS.
# SINCE FISHCALC USED UNI (LEFT BY ENTRY) EARTH SCALING IS ASSUMED.  (WILL IMPROVE FOR SUITABLE TENNANT)
#
# CALLING SEQUENCE:     CALL
# FISHCALC
# ENTER WITH .5 SIN(THETA) IN MPAC.
# PUSHLOC IS AT PDL+0, AN ARBITRARY BASE VALUE IF LEQ 8D
#
# SUBROUTINES CALLED:  GET ERAD
#
# NORMAL EXIT MODE:  RVQ
#
# EXIT MODES:   NONE
#
# OUTPUT:       ERADM (-29) M IN MPAC ON RETURNING
# NEW UNIT VECTOR NOT SAVED.
# SIN(LAT) NOT SAVED.
# PUSHLOC AT PDL+0
#
# ERASABLE INITIALIZATION REQUIRED:
# SDELF/2         =SIN(THETA) / 2, IN MPAC                LEFT BY TFF/TRIG
# CDELF/2         =COS(THETA) / 2, STORED IN PDL 14D      LEFT BY TFF/TRIG
# RONE            (-29) M                                 LEFT BY USER
# VONE            (-7) M/CS                               LEFT BY USER
# URONE           UR/2                                    LEFT BY USER
# UNI             .5 UNIT(V*R)                            LEFT BY ENTRY / P61
# UNITW           UNIT NORTH POLE                         LEFT BY PAD LOAD
#
# DEBRIS:       QPRET, PDL+0 ... PDL+5
# _      _          _
W('26,3030', 0o47315, 'FISHCALC', 'PDVL', 'VXV', 'URPR = UR CDELF + UHOR SDELF', kind='interp', line=927)
W('26,3031', 0o02343, '', '', 'URONE', kind='operand', line=928)
W('26,3032', 0o03502, '', '', 'UNI', kind='operand', line=929)
W('26,3033', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=930)
# SIN(THETA) / 2 FROM PDL+0
W('26,3034', 0o74315, '', 'PDVL', 'VXSC', 'TO PDL+0, +5', kind='interp', line=932)
W('26,3035', 0o02343, '', '', 'URONE', kind='operand', line=933)
W('26,3036', 0o00017, '', '', 'CDELF/2', 'COS(THETA) / 2', kind='operand', line=934)
W('26,3037', 0o45455, '', 'VAD', 'STADR', kind='interp', line=935)
W('26,3040', 0o74235, '', 'STORE', 'URH', 'FOR USE IN RTGO FROM EMS DISPLAY', kind='interp', line=936)
W('26,3041', 0o72441, '', 'DOT', 'SL1', kind='interp', line=937)
W('26,3042', 0o01714, '', '', 'UNITW', 'PULL UNIT VECTOR      UNIT NORTH', kind='operand', line=938)
W('26,3043', 0o02156, '', 'STORE', 'ALPHAV +4', '= .5 SIN(LAT)', kind='interp', line=939)
W('26,3044', 0o77650, 'DUMPFISH', 'GOTO', kind='interp', line=940)
W('26,3045', 0o26505, '', '', 'GETERAD', 'SAVES FISCHER RAD (-29) M IN ERADM AND', kind='operand', line=941)
# IN MPAC.  RETURNS TO CALLER VIO QPRET.

# Page 813
# SUBROUTINE NAME:  VGAMCALC    (USED BY S61.2)                         DATE:           01.21.67
# MOD NO: 0                                                             LOG SECTION:    P61-P67
# MOD BY: MORTH / BAIRNSFATHER
# MOD NO: 1     MOD BY: RR BAIRNSFATHER         DATE: 11 APR 67
# MOD NO: 2     MOD BY: RR BAIRNSFATHER         DATE: 21 NOV 67         VARIABLE MU ADDED.
# MOD NO: 3     MOD BY: RR BAIRNSFATHER         DATE: 21 MAR 68         ACCEPT DIFFERENT EARTH/MOON SCALE
#
# FUNCTIONAL DESCRIPTION:  EARTH CENTERED VIS VIVA CALCULATION OF TERMINAL VELOCITY AND GAMMA (REL TO
# HORIZONTAL) GIVEN THE SCALAR QUANTITIES:  PRESENT RADIUS AND VELOCITY AND THE TERMINAL RADIUS.
# THE USER MUST APPEND PROPER SIGN TO GAMMA, SINCE IT IS CALCULATED AS A POSITIVE NUMBER.
# THE EQUATIONS ARE
#
# VGAM = SQRT(VN VN/MU + 2(RN-RTERM)/(RN RTERM) ) RTMU
#
# COSGAM = H / RTERM VGAM = SQRT (LCP) / (RTERM VGAM/RTMU)
#
# VGAMCALC ASSUMES THAT THE TERMINAL RADIUS IS LESS THAN THE PRESENT RADIUS.  BOTH CALCTFF AND CALCTPER
# MAKE THIS ASSUMPTION.
#
# CALLING SEQUENCE:     CALL                    STCALL  RTERM
# VGAMCALC                PREVGAM
# PUSHLOC AT PDL+0, ARBITRARY IF LEQ 12D
# C(MPAC) UNSPECIFIED                     C(MPAC)=NEW RTERM
#
# SUBROUTINES CALLED:  NONE
#
# NORMAL EXIT MODE:  RVQ
#
# ALARMS:       NONE
#
# OUTPUT:       GAMMA / 360 IN MPAC, POSITIVE NUMBER
# VGAM    E: (-7)   M: (-5)       M/CS IN PDL+0
# PUSHLOC AT PDL+2
#
# ERASABLE INITIALIZATION REQD:
# TFF/RTMU  E: (17)   M: (14)     1/SQRT(MU)                              LEFT BY TFFCONIC
# RMAG1     E: (-29)  M: (-27)    M  PRESENT RADIUS LENGTH                LEFT BY TFFCONIC
# NRMAG     E: (-29+NR)           M  NORM LENGTH OF PRESENT POSITION      LEFT BY TFFCONIC
# M: (-27+NR)
# RTERM     E: (-29)  M: (-27)    M  TERMINAL RADIUS LENGTH               LEFT BY CALCTFF
# NRTERM    E: (-29+NR)           M  NORM LENGTH OF TERMINAL RADIUS       LEFT BY CALCTFF
# M: (-27+NR)
# TFFVSQ    E: (20)   M: (18)   1/M  -(V SQ/MU): PRESENT VELOCITY, NORM   LEFT BY TFFCONIC
# TFFNP     E: (-38+2NR)          M  LCP, SEMI-LATUS RECTUM, WEIGHT NR    LEFT BY TFFCONIC
# M: (-36+2NR)
#
# DEBRIS:       QPRET, PDL+0 ... PDL+3
# RTERM, NRTERM IF PREVGAM ENTERED.
# Page 814

W('26,3046', 0o77657, 'PREVGAM', 'SL*', '', 'ENTER WITH NEW RTERM IN MPAC', kind='interp', line=995)
# E: (-29)  M: (-27)
W('26,3047', 0o20201, '', '', '0,1', 'X1 = -NR', kind='operand', line=997)
W('26,3050', 0o00021, '', 'STORE', 'NRTERM', 'RTERM M               E: (-29+NR)     M: (-27+NR)', kind='interp', line=998)

W('26,3051', 0o41345, 'VGAMCALC', 'DLOAD', 'DMP', kind='interp', line=1000)
W('26,3052', 0o00041, '', '', 'NRMAG', 'RMAG M                E: (-29+NR)     M: (-27+NR)', kind='operand', line=1001)
W('26,3053', 0o00021, '', '', 'NRTERM', 'RTERM M               E: (-29+NR)     M: (-27+NR)', kind='operand', line=1002)
W('26,3054', 0o45325, '', 'PDDL', 'DSU', 'RMAG RTERM M          E: (-58+2NR)    M: (-54+2NR)', kind='interp', line=1003)
W('26,3055', 0o00041, '', '', 'NRMAG', 'RMAG M                E: (-29+NR)     M: (-27+NR)', kind='operand', line=1004)
W('26,3056', 0o00021, '', '', 'NRTERM', 'RTERM M               E: (-29+NR)     M: (-27+NR)', kind='operand', line=1005)
W('26,3057', 0o56257, '', 'SL*', 'DDV', '2(RN-RTERM)           E: (-30+NR)     M: (-28+NR)', kind='interp', line=1006)
W('26,3060', 0o20171, '', '', '0 -8D,1', '(-8+NR)', kind='operand', line=1007)
# PUSH UP PRODUCT.
W('26,3061', 0o77625, '', 'DSU', kind='interp', line=1009)
W('26,3062', 0o00025, '', '', 'TFFVSQ', '-(V SQ/MU)            E: (20)         M: (18)', kind='operand', line=1010)
W('26,3063', 0o41566, '', 'SQRT', 'PUSH', 'SAVE VGAM/RT(MU) FOR NOW.     E: (10) M: (9)', kind='interp', line=1011)
W('26,3064', 0o65271, '', 'DDV', 'PDDL', 'XCH PDL+0, LEAVING VGAM FOR OUTPUT.', kind='interp', line=1012)
# VGAM TO PDL M/CS      E: (-7)         M: (-2)
W('26,3065', 0o00037, '', '', 'TFF/RTMU', '                      E: (17)         M: (14)', kind='operand', line=1014)
W('26,3066', 0o65205, '', 'DMP', 'PDDL', 'RTERM VGAM/RTMU       E: (-19+NR)     M: (-18+NR)', kind='interp', line=1015)
W('26,3067', 0o00021, '', '', 'NRTERM', 'RTERM M               E: (-29+NR)     M: (-27+NR)', kind='operand', line=1016)
W('26,3070', 0o00035, '', '', 'TFFNP', 'LC P =H.H/MU M        E: (-38+2NR)    M: (-36+2NR)', kind='operand', line=1017)
W('26,3071', 0o56366, '', 'SQRT', 'DDV', '                      E: (-19+NR)     M: (-18+NR)', kind='interp', line=1018)
# PUSH UP DEN           E: (-19+NR)     M: (-18+NR)
# USE DDV OVFL AS LIMITER (|COS| <1.0)
W('26,3072', 0o65542, '', 'SR1', 'ACOS', kind='interp', line=1021)
W('26,3073', 0o77616, 'DUMPVGAM', 'RVQ', kind='interp', line=1022)
# CALLER MUST SUPPLY OWN SIGN ...
# 22W     27MS

# Page 815
# SUBROUTINE NAME:      TFF/TRIG        (USED BY S61.2)         DATE:           01.17.67
# MOD NO: 0                                                     LOG SECTION:    P61-P67
# MOD BY: RR BAIRNSFATHER
# MOD NO: 1     MOD BY: RR BAIRNSFATHER         DATE: 14 APR 67
# MOD NO: 2     MOD BY: RR BAIRNSFATHER         DATE: 21 MAR 68         ACCEPT DIFFERENT EARTH/MOON SCALE
#
# FUNCTIONAL DESCRIPTION:  USED BY ENTRY DISPLAY TO CALCULATE SIN(THETA), COS(THETA) FROM DATA LEFT IN
# PDL BY TFF SUBROUTINES.  THE EQNS ARE
#
# COS(THETA) = 1-2 ABS(ARG) / (RN RTERM (1+X) )
# 2
# SIN(THETA) = SGN(ARG) SQRT(1-COS (THETA) )
#
# WHERE THETA = TRANSFER ANGLE
# AND     ARG = P Z ABS(Z)                        IF ALFA ZZ LEQ 1
# ARG = (P / ALFA) SGN(Q1 + R 1/Z)        IF ALFA Z Z G 1
# AND  ARG  HAS BEEN AFFIXED WITH THE SIGN OF SIN(THETA)
#
# CALLING SEQUENCE:     CALL
# TFF/TRIG
# PUSHLOC AT PDL+0, ARBITRARY IF NOT EQ 14D
# C(MPAC) UNSPECIFIED
#
# SUBROUTINES CALLED:  NONE
#
# NORMAL EXIT MODES:  RVQ
#
# ALARMS:       NONE
#
# OUTPUT:       C(MPAC) = .5 SIN(THETA)
# CDELF/2 = .5 COS(THETA)         (IN PDL 14D)
# PUSHLOC AT PDL+0
#
# ERASABLE INITIALIZATION REQUIRED:
# TFFX                    X                                       LEFT BY CALCTFF OR CALCTPER
# TFFTEM  E: (-59+2NR)    ARG                                     LEFT BY CALCTFF OR CALCTPER
# M: (-55+2NR)    WHERE ARG = LCF ZZ SGN(DELF) OR ARG = LCP/ALFA SGN(DELF)
# NRTERM  E: (-29+NR)     M  NORM LENGTH OF TERMINAL RADIUS       LEFT BY CALCTFF OR CALCTPER
# M: (-27+NR)
# NRMAG   E: (-29+NR)     M  NORM LENGTH OF PRESENT POSITION      LEFT BY TFFCONIC
# M: (-27+NR)
#
# DEBRIS:       QPRET, CDELF/2

#   BANK 27
#   SETLOC P60S5
#   BANK
W('27,2631', 0o70545, 'TFF/TRIG', 'DLOAD', 'SR1', kind='interp', line=1074)
W('27,2632', 0o00043, '', '', 'TFFX', kind='operand', line=1075)
W('27,2633', 0o41215, '', 'DAD', 'DMP', kind='interp', line=1076)
W('27,2634', 0o15333, '', '', 'HIDPHALF', kind='operand', line=1077)
W('27,2635', 0o00041, '', '', 'NRMAG', 'RMAG M                E: (-29+NR)     M: (-27+NR)', kind='operand', line=1078)
W('27,2636', 0o55205, '', 'DMP', 'BDDV', kind='interp', line=1079)
W('27,2637', 0o00021, '', '', 'NRTERM', 'RTERM M               E: (-29+NR)     M: (-27+NR)', kind='operand', line=1080)
W('27,2640', 0o00045, '', '', 'TFFTEM', 'P ZSQ OR P/ALFA       E: (-59+2NR)    M: (-55+2NR)', kind='operand', line=1081)
W('27,2641', 0o44246, '', 'ABS', 'BDSU', 'THE SIGN IS FOR SDELF.', kind='interp', line=1082)
W('27,2642', 0o15333, '', '', 'HIDPHALF', kind='operand', line=1083)
W('27,2643', 0o00017, '', 'STORE', 'CDELF/2', '.5 COS(THETA)', kind='interp', line=1084)
W('27,2644', 0o57516, '', 'DSQ', 'DCOMP', 'KEEP HONEST FOR SQRT.', kind='interp', line=1085)
# Page 816
W('27,2645', 0o75415, '', 'DAD', 'SQRT', kind='interp', line=1087)
W('27,2646', 0o15325, '', '', 'HIDP1/4', kind='operand', line=1088)
W('27,2647', 0o43565, 'DUMPTRIG', 'SIGN', 'RVQ', kind='interp', line=1089)
W('27,2650', 0o00045, '', '', 'TFFTEM', 'AFFIX SIGN(DELE/2)', kind='operand', line=1090)
# RETURN WITH .5 SIN(THETA) IN MPAC

# 16W     15MS

W('27,2651', 0o77620, 'DISPTARG', 'STQ', '', 'C(MPAC = TRGO ESTIMATE', kind='interp', line=1095)
W('27,2652', 0o03373, '', '', '60GENRET', kind='operand', line=1096)
W('27,2653', 0o45205, '', 'DMP', 'DSU', kind='interp', line=1097)
W('27,2654', 0o15003, '', '', 'KTETA1', kind='operand', line=1098)
W('27,2655', 0o03733, '', '', 'TTE1', kind='operand', line=1099)
W('27,2656', 0o37606, '', 'STCALL', 'DTEAROT', kind='interp', line=1100)
W('27,2657', 0o46225, '', '', 'EARROT2', kind='operand', line=1101)
W('27,2660', 0o77624, '', 'CALL', kind='interp', line=1102)
W('27,2661', 0o56664, '', '', 'VRCALC', kind='operand', line=1103)
W('27,2662', 0o77650, '', 'GOTO', kind='interp', line=1104)
W('27,2663', 0o03373, '', '', '60GENRET', kind='operand', line=1105)
W('27,2664', 0o50375, 'VRCALC', 'VLOAD', 'DOT', kind='interp', line=1106)
W('27,2665', 0o03542, '', '', 'URH', kind='operand', line=1107)
W('27,2666', 0o03474, '', '', 'RT', kind='operand', line=1108)
W('27,2667', 0o65512, '', 'SL2', 'ACOS', kind='interp', line=1109)
W('27,2670', 0o77616, '', 'RVQ', kind='interp', line=1110)

# END OF PROGRAM S61.2

# Page 817
# PROGRAM DESCRIPTION S62.3     DATE 10JAN67
# MOD NO 1:                     LOG SECTION P60-P67
# MOD BY ZELDIN
# MOD NO: 2     MOD BY: RR BAIRNSFATHER         DATE: 15 MAY 67         CHANGED TO REF COORDS.
# MOD NO: 3     MOD BY: RR BAIRNSFATHER         DATE: 17 JAN 68         ALFAPAD CHANGES MADE.
#
# FUNCTIONAL DESCRIPTION
#
# COMPUTE DESIRED GIMBAL ANGLES FOR ENTRY ATTITUDE
# THE FOLLOWING TRAJECTORY TRIAD IS AVAILABLE IN MEMORY AND IS COMPUTED EACH 2 SECONDS BY CM/POSE IN
# REFERENCE COORDINATES (V = VELOCITY RELATIVE TO EARTH):
#
# UXA = -UNIT(V)
# UYA =  UNIT(V*R)
# UZA =  UXA*UYA
#
# GENERATE A DESIRED BODY TRIAD FOR TRIMMED FLIGHT WITH RESPECT TO THE RELATIVE VELOCITY VECTOR, USING
# ROLL COMMAND AND TRIM ANGLE OF ATTACK:
#
# UXD = UNIT(UYD*UXA) SIN(ALFATRIM) + UXA COS(ALFATRIM)
# UYD = UYA COS(ROLLC) + UZA SIN(ROLLC)
# UZD = UXD * UYD
#
# USE THE DESIRED SET (IN REFERENCE COORDS) AND REFSMMAT TO CALL  CALCGA  AND OBTAIN GIMBAL ANGLES
# IN 2S, C IN MPAC, +2 AND THETAD, +2.
#
# CALLING SEQUENCE
#
# L       CALL
# L+1             S62.3
#
# NORMAL EXIT MODE
#
# RETURN VIA QPRET DIRECTLY FROM CALCGA.
#
# SUBROUTINES CALLED
#
# CALCGA
#
# ALARM OR ABORT MODES
#
# NONE
#
# ERASABLE INITIALIZATION REQUIRED
#
# ROLLC   ROLL COMMAND            DP 1'S COMP AT 1REV
# ALFAPAD SP 1'S C / 180          LEFT BY PAD LOAD        ALFATRIM IS NEGATIVE.
# UXA/2   REF COORDS              LEFT BY CM/POSE
# UYA/2   REF COORDS              LEFT BY CM/POSE
# UZA/2   REF COORDS              LEFT BY CM/POSE
#
# OUTPUT
#
# CPHI    GIMBAL ANGLES (O,I,M) 2'S COMP TP (O,I,M)/180
#
# DEBRIS
#
# QTEMP, QPRET, PUSHLIST

#   BANK 10
#   SETLOC P60S4
#   BANK
# Page 818
#   COUNT* $$/S62.3

W('10,2376', 0o67201, 'S62.3', 'SETPD', 'SLOAD', kind='interp', line=1180)
W('10,2377', 0o00001, '', '', '0', kind='operand', line=1181)
W('10,2400', 0o03012, '', '', 'ALFAPAD', 'ALFATRIM / 180, ALFA IS NEG.', kind='operand', line=1182)
W('10,2401', 0o41542, '', 'SR1', 'PUSH', kind='interp', line=1183)
W('10,2402', 0o65346, '', 'COS', 'PDDL', 'XCH PDL, COS TO PDL0', kind='interp', line=1184)
W('10,2403', 0o65356, '', 'SIN', 'PDDL', 'SIN TO PDL2', kind='interp', line=1185)
W('10,2404', 0o03316, '', '', 'ROLLC', kind='operand', line=1186)
W('10,2405', 0o74346, '', 'COS', 'VXSC', kind='interp', line=1187)
W('10,2406', 0o03550, '', '', 'UYA/2', '                              REF COORDS', kind='operand', line=1188)
W('10,2407', 0o73525, '', 'PDDL', 'SIN', 'PUSH VECTOR INTO PDL4...9', kind='interp', line=1189)
W('10,2410', 0o03316, '', '', 'ROLLC', kind='operand', line=1190)
W('10,2411', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=1191)
W('10,2412', 0o03556, '', '', 'UZA/2', '                              REF COORDS', kind='operand', line=1192)
# VECTOR FROM PDL4...9
W('10,2413', 0o77772, '', 'VSL1', kind='interp', line=1194)
W('10,2414', 0o02722, '', 'STORE', 'YNB', '= UYD                         REF COORDS', kind='interp', line=1195)

W('10,2415', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=1197)
W('10,2416', 0o03542, '', '', 'UXA/2', '                              REF COORDS', kind='operand', line=1198)
W('10,2417', 0o65361, '', 'VXSC', 'PDDL', kind='interp', line=1199)
# SIN TRIM FROM PDL2
# XCH PDL0 FOR COS TRIM
W('10,2420', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=1202)
W('10,2421', 0o03542, '', '', 'UXA/2', '                              REF COORDS', kind='operand', line=1203)
# FROM PDL0
W('10,2422', 0o77772, '', 'VSL1', kind='interp', line=1205)
W('10,2423', 0o02714, '', 'STORE', 'XNB', 'X SC AXIS (.5 UNIT)           REF COORDS', kind='interp', line=1206)

W('10,2424', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=1208)
W('10,2425', 0o02722, '', '', 'YNB', kind='operand', line=1209)
W('10,2426', 0o26730, '', 'STOVL', 'ZNB', 'Z SC IN REF COOR. SCALED AT 2', kind='interp', line=1210)
W('10,2427', 0o01736, '', '', 'REFSMMAT', kind='operand', line=1211)
W('10,2430', 0o26672, '', 'STOVL', 'XSM', kind='interp', line=1212)
W('10,2431', 0o01744, '', '', 'REFSMMAT +6', kind='operand', line=1213)
W('10,2432', 0o26700, '', 'STOVL', 'YSM', kind='interp', line=1214)
W('10,2433', 0o01752, '', '', 'REFSMMAT +12D', kind='operand', line=1215)
W('10,2434', 0o02706, '', 'STORE', 'ZSM', kind='interp', line=1216)

W('10,2435', 0o52014, '', 'CLEAR', 'GOTO', kind='interp', line=1218)
W('10,2436', 0o00260, '', '', 'CPHIFLAG', 'CAUSE CALCGA TO STORE ANS IN TP CPHI', kind='operand', line=1219)
W('10,2437', 0o47311, '', '', 'CALCGA', kind='operand', line=1220)
# CALCGA WILL RETURN TO ORIGINAL CALLER
# VIA QPRET WITH 2'S COMP. ANGLES IN CPHI
