"""P70-P71.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P70-P71.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 829-837 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P70_P71', 'P70-P71.agc', 'Luminary099', pages='829-837')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P70-P71.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        829-837
# Mod history:  2009-05-23 HG   Transcribed from page images.
# 2009-06-05 RSB  Fixed a typo.
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

# Page 829
#   BANK 21
#   SETLOC R11
#   BANK

#   EBANK= DVCNTR
#   COUNT* $$/R11

W('21,2006', 0o40103, 'R10,R11', 'CS', 'FLAGWRD7', 'IS SERVICER STILL RUNNING?', line=36)
W('21,2007', 0o74747, '', 'MASK', 'AVEGFBIT', line=37)
W('21,2010', 0o10000, '', 'CCS', 'A', line=38)
W('21,2011', 0o15261, '', 'TCF', 'TASKOVER', 'LET AVGEND TAKE CARE OF GROUP 2.', line=39)
W('21,2012', 0o11056, '', 'CCS', 'PIPCTR', line=40)
W('21,2013', 0o12015, '', 'TCF', '+2', line=41)
W('21,2014', 0o12130, '', 'TCF', 'LRHTASK', 'LAST PASS. CALL LRHTASK.', line=42)
W('21,2015', 0o55714, '', 'TS', 'PIPCTR1', line=43)

S('PIPCTR1', 'equals', 0o3714, line=45)
S('PIPCTR', 'equals', 0o1056, line=46)
W('21,2016', 0o36010, '', 'CAF', 'OCT31', line=47)
W('21,2017', 0o05173, '', 'TC', 'TWIDDLE', line=48)
W('21,2020', 0o02006, '', 'ADRES', 'R10,R11', kind='data', line=49)
W('21,2021', 0o41303, 'R10,R11A', 'CS', 'IMODES33', 'IF LAMP TEST, DO NOT CHANGE LR LITES.', line=50)
W('21,2022', 0o74753, '', 'MASK', 'BIT1', line=51)
W('21,2023', 0o00006, '', 'EXTEND', line=52)
W('21,2024', 0o12042, '', 'BZF', '10,11', line=53)

W('21,2025', 0o70107, 'FLASHH?', 'MASK', 'FLGWRD11', 'C(A) = 1 = HFLASH BIT', line=55)
W('21,2026', 0o00006, '', 'EXTEND', line=56)
W('21,2027', 0o12033, '', 'BZF', 'FLASHV?', 'H FLASH OFF, SO LEAVE ALONE', line=57)

W('21,2030', 0o34747, '', 'CA', 'HLITE', line=59)
W('21,2031', 0o54001, '', 'TS', 'L', line=60)
W('21,2032', 0o04606, '', 'TC', 'FLIP', 'FLIP H LITE', line=61)

W('21,2033', 0o34752, 'FLASHV?', 'CA', 'VFLSHBIT', 'VLASHBIT MUST BE BIT 2.', line=63)
W('21,2034', 0o70107, '', 'MASK', 'FLGWRD11', line=64)
W('21,2035', 0o00006, '', 'EXTEND', line=65)
W('21,2036', 0o12042, '', 'BZF', '10,11', 'V FLASH OFF', line=66)

W('21,2037', 0o34751, '', 'CA', 'VLITE', line=68)
W('21,2040', 0o54001, '', 'TS', 'L', line=69)
W('21,2041', 0o04606, '', 'TC', 'FLIP', 'FLIP V LITE', line=70)

W('21,2042', 0o30105, '10,11', 'CA', 'FLAGWRD9', 'IS THE LETABORT FLAG SET ?', line=72)
W('21,2043', 0o74743, '', 'MASK', 'LETABBIT', line=73)
W('21,2044', 0o00006, '', 'EXTEND', line=74)
W('21,2045', 0o12154, '', 'BZF', 'LANDISP', 'NO.  PROCEED TO R10.', line=75)

W('21,2046', 0o41011, 'P71NOW?', 'CS', 'MODREG', 'YES.  ARE WE IN P71 NOW?', line=77)
# Page 830
W('21,2047', 0o62107, '', 'AD', '1DEC71', line=79)
W('21,2050', 0o00006, '', 'EXTEND', line=80)
W('21,2051', 0o12154, '', 'BZF', 'LANDISP', 'YES.  PROCEED TO R10.', line=81)

W('21,2052', 0o00006, '', 'EXTEND', '', 'NO.  IS AN ABORT STAGE COMMANDED?', line=83)
W('21,2053', 0o00030, '', 'READ', 'CHAN30', line=84)
W('21,2054', 0o40000, '', 'COM', line=85)
W('21,2055', 0o54001, '', 'TS', 'L', line=86)
W('21,2056', 0o74750, '', 'MASK', 'BIT4', line=87)
W('21,2057', 0o10000, '', 'CCS', 'A', line=88)
W('21,2060', 0o12076, '', 'TCF', 'P71A', 'YES.', line=89)

W('21,2061', 0o41011, 'P70NOW?', 'CS', 'MODREG', 'NO.  ARE WE IN P70 NOW?', line=91)
W('21,2062', 0o62106, '', 'AD', '1DEC70', line=92)
W('21,2063', 0o00006, '', 'EXTEND', line=93)
W('21,2064', 0o12154, '', 'BZF', 'LANDISP', 'YES.  PROCEED TO R10.', line=94)

W('21,2065', 0o30001, '', 'CA', 'L', 'NO.  IS AN ABORT COMMANDED?', line=96)
W('21,2066', 0o74753, '', 'MASK', 'BIT1', line=97)
W('21,2067', 0o10000, '', 'CCS', 'A', line=98)
W('21,2070', 0o12073, '', 'TCF', 'P70A', 'YES.', line=99)
W('21,2071', 0o12154, '', 'TCF', 'LANDISP', 'NO.  PROCEED TO R10.', line=100)

#   COUNT* $$/P70

W('21,2072', 0o02110, 'P70', 'TC', 'LEGAL?', line=104)
W('21,2073', 0o44755, 'P70A', 'CS', 'ZERO', line=105)
W('21,2074', 0o12077, '', 'TCF', '+3', line=106)
W('21,2075', 0o02110, 'P71', 'TC', 'LEGAL?', line=107)
W('21,2076', 0o34752, 'P71A', 'CAF', 'TWO', line=108)
W('21,2077', 0o54002, '', 'TS', 'Q', line=109)
W('21,2100', 0o00004, '', 'INHINT', line=110)
W('21,2101', 0o00006, '', 'EXTEND', line=111)
W('21,2102', 0o32105, '', 'DCA', 'CNTABTAD', line=112)
W('21,2103', 0o52006, '', 'DTCB', line=113)

#   EBANK= DVCNTR
W('21,2104', 0o03402, 'CNTABTAD', '2CADR', 'CONTABRT', kind='data', line=116)
W('21,2105', 0o12067, kind='data', line=116)

W('21,2106', 0o00106, '1DEC70', 'DEC', '70', kind='data', line=118)
W('21,2107', 0o00107, '1DEC71', 'DEC', '71', kind='data', line=119)

#   BANK 05
#   SETLOC ABORTS1
#   BANK
#   COUNT* $$/P70

W('05,3402', 0o33405, 'CONTABRT', 'CAF', 'ABRTJADR', line=126)
W('05,3403', 0o54017, '', 'TS', 'BRUPT', line=127)
W('05,3404', 0o50017, '', 'RESUME', line=128)
# Page 831

W('05,3405', 0o13406, 'ABRTJADR', 'TCF', 'ABRTJASK', line=131)

W('05,3406', 0o33477, 'ABRTJASK', 'CAF', 'OCTAL27', line=133)
W('05,3407', 0o60002, '', 'AD', 'Q', line=134)
W('05,3410', 0o54001, '', 'TS', 'L', line=135)
W('05,3411', 0o40000, '', 'COM', line=136)
W('05,3412', 0o52761, '', 'DXCH', '-PHASE4', line=137)
W('05,3413', 0o50002, '', 'INDEX', 'Q', line=138)
W('05,3414', 0o33476, '', 'CAF', 'MODE70', line=139)
W('05,3415', 0o55011, '', 'TS', 'MODREG', line=140)

W('05,3416', 0o55163, '', 'TS', 'DISPDEX', 'INSURE DISPDEX IS POSITIVE.', line=142)

W('05,3417', 0o10002, '', 'CCS', 'Q', 'SET APSFLAG IF P71.', line=144)
W('05,3420', 0o40106, '', 'CS', 'FLGWRD10', 'SET APSFLAG PRIOR TO THE ENEMA.', line=145)
W('05,3421', 0o74737, '', 'MASK', 'APSFLBIT', line=146)
W('05,3422', 0o26106, '', 'ADS', 'FLGWRD10', line=147)
W('05,3423', 0o43501, '', 'CS', 'DAPBITS', 'DAPBITS = OCT 640 = BITS 6, 8, 9', line=148)
W('05,3424', 0o70111, '', 'MASK', 'DAPBOOLS', '(TURN OFF: ULLAGE, DRIFT, AND XOVINHIB )', line=149)
W('05,3425', 0o54111, '', 'TS', 'DAPBOOLS', line=150)

W('05,3426', 0o40101, '', 'CS', 'FLAGWRD5', 'SET ENGONFLG.', line=152)
W('05,3427', 0o74745, '', 'MASK', 'ENGONBIT', line=153)
W('05,3430', 0o26101, '', 'ADS', 'FLAGWRD5', line=154)

W('05,3431', 0o44355, '', 'CS', 'PRIO30', 'INSURE THAT THE ENGINE IS ON, IF ARMED.', line=156)
W('05,3432', 0o00006, '', 'EXTEND', line=157)
W('05,3433', 0o02011, '', 'RAND', 'DSALMOUT', line=158)
W('05,3434', 0o64737, '', 'AD', 'BIT13', line=159)
W('05,3435', 0o00006, '', 'EXTEND', line=160)
W('05,3436', 0o01011, '', 'WRITE', 'DSALMOUT', line=161)

W('05,3437', 0o34735, '', 'CAF', 'LRBYBIT', 'TERMINATE R12.', line=163)
W('05,3440', 0o54107, '', 'TS', 'FLGWRD11', line=164)

W('05,3441', 0o40074, '', 'CS', 'FLAGWRD0', 'SET R10FLAG TO SUPPRESS OUTPUTS TO THE', line=166)
W('05,3442', 0o74752, '', 'MASK', 'R10FLBIT', 'CROSS-POINTER DISPLAY.', line=167)
W('05,3443', 0o26074, '', 'ADS', 'FLAGWRD0', 'THE FOLLOWING ENEMA WILL REMOVE THE', line=168)
# DISPLAY INERTIAL DATA OUTBIT.

W('05,3444', 0o06011, '', 'TC', 'CLRADMOD', 'INSURE RADMODES PROPERLY SET FOR R29.', line=171)

W('05,3445', 0o00006, '', 'EXTEND', '', 'LOAD TEVENT FOR THE DOWNLINK.', line=173)
W('05,3446', 0o30025, '', 'DCA', 'TIME2', line=174)
W('05,3447', 0o53345, '', 'DXCH', 'TEVENT', line=175)

W('05,3450', 0o00006, '', 'EXTEND', line=177)
W('05,3451', 0o33475, '', 'DCA', 'SVEXITAD', line=178)
W('05,3452', 0o53253, '', 'DXCH', 'AVGEXIT', line=179)

# Page 832
W('05,3453', 0o00006, '', 'EXTEND', line=182)
W('05,3454', 0o34755, '', 'DCA', 'NEG0', line=183)
W('05,3455', 0o52753, '', 'DXCH', '-PHASE1', line=184)

W('05,3456', 0o00006, '', 'EXTEND', line=186)
W('05,3457', 0o34755, '', 'DCA', 'NEG0', line=187)
W('05,3460', 0o52757, '', 'DXCH', '-PHASE3', line=188)

W('05,3461', 0o00006, '', 'EXTEND', line=190)
W('05,3462', 0o34755, '', 'DCA', 'NEG0', line=191)
W('05,3463', 0o52765, '', 'DXCH', '-PHASE6', line=192)

W('05,3464', 0o36245, '', 'CAF', 'THREE', 'SET UP 4.3SPOT FOR GOABORT', line=194)
W('05,3465', 0o54001, '', 'TS', 'L', line=195)
W('05,3466', 0o40000, '', 'COM', line=196)
W('05,3467', 0o52761, '', 'DXCH', '-PHASE4', line=197)

W('05,3470', 0o37730, '', 'CAF', 'OCT37774', 'SET T5RUPT TO CALL DAPIDLER IN', line=199)
W('05,3471', 0o54030, '', 'TS', 'TIME5', '40 MILLISECONDS.', line=200)

W('05,3472', 0o04635, '', 'TC', 'POSTJUMP', line=202)
W('05,3473', 0o12765, '', 'CADR', 'ENEMA', kind='data', line=203)

#   EBANK= DVCNTR
W('05,3474', 0o03770, 'SVEXITAD', '2CADR', 'SERVEXIT', kind='data', line=206)
W('05,3475', 0o64067, kind='data', line=206)

W('05,3476', 0o00106, 'MODE70', 'DEC', '70', kind='data', line=208)
W('05,3477', 0o00027, 'OCTAL27', 'OCT', '27', kind='data', line=209)
W('05,3500', 0o00107, 'MODE71', 'DEC', '71', kind='data', line=210)

W('05,3501', 0o00640, 'DAPBITS', 'OCT', '00640', kind='data', line=212)

#   BANK 32
#   SETLOC ABORTS
#   BANK

#   COUNT* $$/P70

W('32,3540', 0o06037, 'GOABORT', 'TC', 'INTPRET', line=220)
W('32,3541', 0o77624, '', 'CALL', kind='interp', line=221)
W('32,3542', 0o61104, '', '', 'INITCDUW', kind='operand', line=222)
W('32,3543', 0o77776, '', 'EXIT', kind='interp', line=223)
W('32,3544', 0o34751, '', 'CAF', 'FOUR', line=224)
W('32,3545', 0o55515, '', 'TS', 'DVCNTR', line=225)

W('32,3546', 0o33764, '', 'CAF', 'WHICHADR', line=227)
W('32,3547', 0o55455, '', 'TS', 'WHICH', line=228)

W('32,3550', 0o05516, '', 'TC', 'DOWNFLAG', line=230)
W('32,3551', 0o00214, '', 'ADRES', 'FLRCS', kind='data', line=231)
# Page 833
W('32,3552', 0o05516, '', 'TC', 'DOWNFLAG', line=233)
W('32,3553', 0o00175, '', 'ADRES', 'FLUNDISP', kind='data', line=234)

W('32,3554', 0o05516, '', 'TC', 'DOWNFLAG', line=236)
W('32,3555', 0o00161, '', 'ADRES', 'IDLEFLAG', kind='data', line=237)

W('32,3556', 0o05504, '', 'TC', 'UPFLAG', 'INSURE 4-JET TRANSLATION CAPABILITY.', line=239)
W('32,3557', 0o00307, '', 'ADRES', 'ACC4-2FL', kind='data', line=240)

W('32,3560', 0o05321, '', 'TC', 'CHECKMM', line=242)
W('32,3561', 0o00106, '70DEC', 'DEC', '70', kind='data', line=243)
W('32,3562', 0o13707, '', 'TCF', 'P71RET', line=244)

W('32,3563', 0o06037, 'P70INIT', 'TC', 'INTPRET', line=246)
W('32,3564', 0o77624, '', 'CALL', kind='interp', line=247)
W('32,3565', 0o65737, '', '', 'TGOCOMP', kind='operand', line=248)
W('32,3566', 0o54345, '', 'DLOAD', 'SL', kind='interp', line=249)
W('32,3567', 0o34003, '', '', 'MDOTDPS', kind='operand', line=250)
W('32,3570', 0o20205, '', '', '4D', kind='operand', line=251)
W('32,3571', 0o77665, '', 'BDDV', kind='interp', line=252)
W('32,3572', 0o01245, '', '', 'MASS', kind='operand', line=253)
W('32,3573', 0o16271, '', 'STODL', 'TBUP', kind='interp', line=254)
W('32,3574', 0o01245, '', '', 'MASS', kind='operand', line=255)
W('32,3575', 0o70471, '', 'DDV', 'SR1', kind='interp', line=256)
W('32,3576', 0o16015, '', '', 'K(1/DV)', kind='operand', line=257)
W('32,3577', 0o03635, '', 'STORE', '1/DV1', kind='interp', line=258)
W('32,3600', 0o03637, '', 'STORE', '1/DV2', kind='interp', line=259)
W('32,3601', 0o03641, '', 'STORE', '1/DV3', kind='interp', line=260)
W('32,3602', 0o77665, '', 'BDDV', kind='interp', line=261)
W('32,3603', 0o25763, '', '', 'K(AT)', kind='operand', line=262)
W('32,3604', 0o16263, '', 'STODL', 'AT', kind='interp', line=263)
W('32,3605', 0o34005, '', '', 'DTDECAY', kind='operand', line=264)
W('32,3606', 0o54276, '', 'DCOMP', 'SL', kind='interp', line=265)
W('32,3607', 0o20214, '', '', '11D', kind='operand', line=266)
W('32,3610', 0o02267, '', 'STORE', 'TTO', kind='interp', line=267)
W('32,3611', 0o57535, '', 'SLOAD', 'DCOMP', kind='interp', line=268)
W('32,3612', 0o26002, '', '', 'DPSVEX', kind='operand', line=269)
W('32,3613', 0o77702, '', 'SR2', kind='interp', line=270)
W('32,3614', 0o02265, '', 'STORE', 'VE', 'INITIALIZE DPS EXHAUST VELOCITY', kind='interp', line=271)
W('32,3615', 0o45014, '', 'SET', 'CALL', kind='interp', line=272)
W('32,3616', 0o04467, '', '', 'FLAP', kind='operand', line=273)
W('32,3617', 0o60300, '', '', 'COMMINIT', kind='operand', line=274)
W('32,3620', 0o52160, '', 'AXC,1', 'GOTO', 'RETURN HERE IN P70, SE X1 FOR DPS COEFF.', kind='interp', line=275)
W('32,3621', 0o00000, '', '', '0D', kind='operand', line=276)
W('32,3622', 0o65625, '', '', 'BOTHPOLY', kind='operand', line=277)
W('32,3623', 0o77760, 'INJTARG', 'AXC,1', '', 'RETURN HERE IN P71, SET X1 FOR APS COEFF', kind='interp', line=278)
W('32,3624', 0o00010, '', '', '8D', kind='operand', line=279)
W('32,3625', 0o41343, 'BOTHPOLY', 'DLOAD*', 'DMP', 'TGO D', kind='interp', line=280)
W('32,3626', 0o02551, '', '', 'ABTCOF,1', kind='operand', line=281)
W('32,3627', 0o03517, '', '', 'TGO', kind='operand', line=282)
# Page 834
W('32,3630', 0o41213, '', 'DAD*', 'DMP', kind='interp', line=284)
W('32,3631', 0o02553, '', '', 'ABTCOF +2,1', 'TGO(C+TGO D)', kind='operand', line=285)
W('32,3632', 0o03517, '', '', 'TGO', kind='operand', line=286)
W('32,3633', 0o41213, '', 'DAD*', 'DMP', kind='interp', line=287)
W('32,3634', 0o02555, '', '', 'ABTCOF +4,1', 'TGO(B+TGO(C+TGO D))', kind='operand', line=288)
W('32,3635', 0o03517, '', '', 'TGO', kind='operand', line=289)
W('32,3636', 0o77613, '', 'DAD*', kind='interp', line=290)
W('32,3637', 0o02557, '', '', 'ABTCOF +6,1', 'A+TGO(B+TGO(C+TGO D))', kind='operand', line=291)
W('32,3640', 0o02277, '', 'STORE', 'ZDOTD', 'STORE TENTATIVELY IN ZDOTD', kind='interp', line=292)
W('32,3641', 0o51025, '', 'DSU', 'BPL', 'CHECK AGAINST MINIMUM', kind='interp', line=293)
W('32,3642', 0o02571, '', '', 'VMIN', kind='operand', line=294)
W('32,3643', 0o65647, '', '', 'UPRATE', 'IF BIG ENOUGH, LEAVE ZDOTD AS IS .', kind='operand', line=295)
W('32,3644', 0o77745, '', 'DLOAD', kind='interp', line=296)
W('32,3645', 0o02571, '', '', 'VMIN', kind='operand', line=297)
W('32,3646', 0o02277, '', 'STORE', 'ZDOTD', 'IF TOO SMALL, REPLACE WITH MINIMUM.', kind='interp', line=298)
W('32,3647', 0o77745, 'UPRATE', 'DLOAD', kind='interp', line=299)
W('32,3650', 0o02575, '', '', 'ABTRDOT', kind='operand', line=300)
W('32,3651', 0o36273, '', 'STCALL', 'RDOTD', 'INITIALZE RDOTD.', kind='interp', line=301)
W('32,3652', 0o57312, '', '', 'YCOMP', 'COMPUTE Y', kind='operand', line=302)
W('32,3653', 0o45246, '', 'ABS', 'DSU', kind='interp', line=303)
W('32,3654', 0o02573, '', '', 'YLIM', '/Y/-DYMAX', kind='operand', line=304)
W('32,3655', 0o75240, '', 'BMN', 'SIGN', 'IF <0, XR<.5DEG, LEAVE YCO AT 0', kind='interp', line=305)
W('32,3656', 0o65661, '', '', 'YOK', 'IF >0, FIX SIGN OF DEFICIT, THIS IS YCO.', kind='operand', line=306)
W('32,3657', 0o02335, '', '', 'Y', kind='operand', line=307)
W('32,3660', 0o03633, '', 'STORE', 'YCO', kind='interp', line=308)
W('32,3661', 0o45345, 'YOK', 'DLOAD', 'DSU', kind='interp', line=309)
W('32,3662', 0o03633, '', '', 'YCO', kind='operand', line=310)
W('32,3663', 0o02335, '', '', 'Y', 'COMPUTE XRANGE IN CASE ASTRONAUT WANTS', kind='operand', line=311)
W('32,3664', 0o77661, '', 'SR', kind='interp', line=312)
W('32,3665', 0o20606, '', '', '5D', kind='operand', line=313)
W('32,3666', 0o03643, '', 'STORE', 'XRANGE', 'TO LOOK.', kind='interp', line=314)
W('32,3667', 0o77414, 'UPTHROT', 'SET', 'EXIT', kind='interp', line=315)
W('32,3670', 0o04461, '', '', 'FLVR', kind='operand', line=316)

W('32,3671', 0o05504, '', 'TC', 'UPFLAG', 'SET ROTFLAG', line=318)
W('32,3672', 0o00220, '', 'ADRES', 'ROTFLAG', kind='data', line=319)

W('32,3673', 0o03746, '', 'TC', 'THROTUP', line=321)

W('32,3674', 0o05353, '', 'TC', 'PHASCHNG', line=323)
W('32,3675', 0o04024, '', 'OCT', '04024', kind='data', line=324)

W('32,3676', 0o04616, '', 'TC', 'BANKCALL', 'VERIFY THAT THE PANEL SWITCHES', line=326)
W('32,3677', 0o73747, '', 'CADR', 'P40AUTO', 'ARE PROPERLY SET.', kind='data', line=327)

W('32,3700', 0o03746, '', 'TC', 'THROTUP', line=329)

W('32,3701', 0o00006, 'UPTHROT1', 'EXTEND', '', 'SET SERVICER TO CALL ASCENT GUIDANCE.', line=331)
W('32,3702', 0o33766, '', 'DCA', 'ATMAGAD', line=332)
W('32,3703', 0o53253, '', 'DXCH', 'AVGEXIT', line=333)
# Page 835
W('32,3704', 0o05353, 'GRP4OFF', 'TC', 'PHASCHNG', 'TERMINATE USE OF GROUP 4.', line=335)
W('32,3705', 0o00004, '', 'OCT', '00004', kind='data', line=336)

W('32,3706', 0o15155, '', 'TCF', 'ENDOFJOB', line=338)

W('32,3707', 0o05516, 'P71RET', 'TC', 'DOWNFLAG', line=340)
W('32,3710', 0o00215, '', 'ADRES', 'LETABORT', kind='data', line=341)

W('32,3711', 0o36000, '', 'CAF', 'THRESH2', 'SET DVMON THRESHOLD TO THE ASCENT VALUE.', line=343)
W('32,3712', 0o55251, '', 'TS', 'DVTHRUSH', line=344)

W('32,3713', 0o06037, '', 'TC', 'INTPRET', line=346)
W('32,3714', 0o45014, '', 'BON', 'CALL', kind='interp', line=347)
W('32,3715', 0o04707, '', '', 'FLAP', kind='operand', line=348)
W('32,3716', 0o65724, '', '', 'OLDTIME', kind='operand', line=349)
W('32,3717', 0o65737, '', '', 'TGOCOMP', 'IF FLAP=0, TGO=T-TIG', kind='operand', line=350)
W('32,3720', 0o52131, '', 'SSP', 'GOTO', kind='interp', line=351)
W('32,3721', 0o00053, '', '', 'QPRET', kind='operand', line=352)
W('32,3722', 0o65623, '', 'CADR', 'INJTARG', kind='data', line=353)
W('32,3723', 0o60254, '', '', 'P12INIT', 'WILL EXIT P12INIT TO INJTARG', kind='operand', line=354)
W('32,3724', 0o72545, 'OLDTIME', 'DLOAD', 'SL1', 'IF FLAP=1,GTO=2 TGO', kind='interp', line=355)
W('32,3725', 0o03517, '', '', 'TGO', kind='operand', line=356)
W('32,3726', 0o37502, '', 'STCALL', 'TGO1', kind='interp', line=357)
W('32,3727', 0o60254, '', '', 'P12INIT', kind='operand', line=358)
W('32,3730', 0o77776, '', 'EXIT', kind='interp', line=359)
W('32,3731', 0o05353, '', 'TC', 'PHASCHNG', line=360)
W('32,3732', 0o04024, '', 'OCT', '04024', kind='data', line=361)

W('32,3733', 0o00006, '', 'EXTEND', line=363)
W('32,3734', 0o31502, '', 'DCA', 'TGO1', line=364)
W('32,3735', 0o53517, '', 'DXCH', 'TGO', line=365)
W('32,3736', 0o13676, '', 'TCF', 'UPTHROT1 -3', line=366)

S('TGO1', 'equals', 0o3501, line=368)
# *************************************************************************

#   BANK 21
#   SETLOC R11
#   BANK

#   COUNT* $$/P70

W('21,2110', 0o40775, 'LEGAL?', 'CS', 'MMNUMBER', 'IS THE DESIRED PGM ALREADY IN PROGRESS?', line=377)
W('21,2111', 0o61011, '', 'AD', 'MODREG', line=378)
W('21,2112', 0o00006, '', 'EXTEND', line=379)
W('21,2113', 0o12124, '', 'BZF', 'ABORTALM', line=380)

W('21,2114', 0o40105, '', 'CS', 'FLAGWRD9', 'ARE THE ABORTS ENABLED?', line=382)
W('21,2115', 0o74743, '', 'MASK', 'LETABBIT', line=383)
W('21,2116', 0o10000, '', 'CCS', 'A', line=384)
# Page 836
W('21,2117', 0o12124, '', 'TCF', 'ABORTALM', line=386)

W('21,2120', 0o30103, '', 'CA', 'FLAGWRD7', 'IS SERVICER ON THE AIR?', line=388)
W('21,2121', 0o74747, '', 'MASK', 'AVEGFBIT', line=389)
W('21,2122', 0o10000, '', 'CCS', 'A', line=390)
W('21,2123', 0o00002, '', 'TC', 'Q', 'YES.  ALL IS WELL.', line=391)
W('21,2124', 0o04364, 'ABORTALM', 'TC', 'FALTON', line=392)
W('21,2125', 0o04457, '', 'TC', 'RELDSP', line=393)
W('21,2126', 0o04635, '', 'TC', 'POSTJUMP', line=394)
W('21,2127', 0o21050, '', 'CADR', 'PINBRNCH', kind='data', line=395)

#   BANK 32
#   SETLOC ABORTS
#   BANK

#   COUNT* $$/P70

# ************************************************************************

W('32,3737', 0o45234, 'TGOCOMP', 'RTB', 'DSU', kind='interp', line=405)
W('32,3740', 0o21573, '', '', 'LOADTIME', kind='operand', line=406)
W('32,3741', 0o03442, '', '', 'TIG', kind='operand', line=407)
W('32,3742', 0o77661, '', 'SL', kind='interp', line=408)
W('32,3743', 0o20214, '', '', '11D', kind='operand', line=409)
W('32,3744', 0o03517, '', 'STORE', 'TGO', kind='interp', line=410)
W('32,3745', 0o77616, '', 'RVQ', kind='interp', line=411)

# ************************************************************************

W('32,3746', 0o34737, 'THROTUP', 'CAF', 'BIT13', line=415)
W('32,3747', 0o54055, '', 'TS', 'THRUST', line=416)
W('32,3750', 0o34750, '', 'CAF', 'BIT4', line=417)
W('32,3751', 0o00006, '', 'EXTEND', line=418)
W('32,3752', 0o05014, '', 'WOR', 'CHAN14', line=419)
W('32,3753', 0o00002, '', 'TC', 'Q', line=420)

# ************************************************************************

W('32,3754', 0o00000, '10SECS', '2DEC', '1000', kind='data', line=424)
W('32,3755', 0o01750, kind='data', line=424)

W('32,3756', 0o00021, 'HINJECT', '2DEC', '18288 B-24', '60,000 FEET EXPRESSED IN METERS.', kind='data', line=426)
W('32,3757', 0o33400, kind='data', line=426)

W('32,3760', 0o11021, '(TGO)A', '2DEC', '37000 B-17', kind='data', line=428)
W('32,3761', 0o00000, kind='data', line=428)

W('32,3762', 0o00507, 'K(AT)', '2DEC', '.02', 'SCALING CONSTANT', kind='data', line=430)
W('32,3763', 0o25605, kind='data', line=430)

W('32,3764', 0o02112, 'WHICHADR', 'REMADR', 'ABRTABLE', kind='data', line=432)

# ************************************************************************
# Page 837
#   EBANK= DVCNTR
W('32,3765', 0o03642, 'ATMAGAD', '2CADR', 'ATMAG', kind='data', line=437)
W('32,3766', 0o70067, kind='data', line=437)

W('32,3767', 0o00003, 'ORBMANAD', 'ADRES', 'ORBMANUV', kind='data', line=439)
