"""KALCMANU_STEERING.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/KALCMANU_STEERING.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 414-419 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('KALCMANU_STEERING', 'KALCMANU_STEERING.agc', 'Comanche055', pages='414-419')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     KALCMANU_STEERING.agc
# Purpose:      Part of the source code for Comanche, build 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 414-419
# Contact:      Onno Hommes <ohommes@cmu.edu>.
# Website:      www.ibiblio.org/apollo.
# Mod history:  05/07/09 OH     Transcription Batch 1 Assignment
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
# Refer directly to the online document mentioned above for further information.
# Please report any errors to info@sandroid.org.

# Page 414
# GENERATION OF STEERING COMMANDS FOR DIGITAL AUTOPILOT FREE FALL MANEUVERS
#
# NEW COMMANDS WILL BE GENERATED EVERY ONE SECOND DURING THE MANEUVER

#   BANK 15

#   SETLOC KALCMON1
#   BANK

#   EBANK= BCDU

#   COUNT 22/KALC

W('22,3026', 0o41332, 'NEWDELHI', 'CS', 'HOLDFLAG', 'SEE IF MANEUVER HAS BEEN INTERRUPTED', line=44)
W('22,3027', 0o00006, '', 'EXTEND', '', 'BY ASTRONAUT', line=45)
W('22,3030', 0o62726, '', 'BZMF', 'NOGO -2', 'IF SO, TERMINATE KALCMANU', line=46)
W('22,3031', 0o06006, 'NEWANGL', 'TC', 'INTPRET', line=47)
W('22,3032', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=48)
W('22,3033', 0o03320, '', '', 'MIS', 'COMPUTE THE NEW MATRIX FROM S/C TO', kind='operand', line=49)
W('22,3034', 0o03425, '', '', 'DEL', 'STABLE MEMBER AXES', kind='operand', line=50)
W('22,3035', 0o77624, '', 'CALL', kind='interp', line=51)
W('22,3036', 0o44304, '', '', 'MXM3', kind='operand', line=52)
W('22,3037', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=53)
W('22,3040', 0o50442, '', 'STOVL', 'MIS +12D', 'CALCULATE NEW DESIRED CDU ANGLES', kind='interp', line=54)
W('22,3041', 0o77626, '', 'STADR', kind='interp', line=55)
W('22,3042', 0o50450, '', 'STOVL', 'MIS +6D', kind='interp', line=56)
W('22,3043', 0o77626, '', 'STADR', kind='interp', line=57)
W('22,3044', 0o74456, '', 'STORE', 'MIS', kind='interp', line=58)
W('22,3045', 0o45160, '', 'AXC,1', 'CALL', kind='interp', line=59)
W('22,3046', 0o03320, '', '', 'MIS', kind='operand', line=60)
W('22,3047', 0o44655, '', '', 'DCMTOCDU', 'PICK UP THE NEW CDU ANGLES FROM MATRIX', kind='operand', line=61)
W('22,3050', 0o77634, '', 'RTB', kind='interp', line=62)
W('22,3051', 0o45552, '', '', 'V1STO2S', kind='operand', line=63)
W('22,3052', 0o03267, '', 'STORE', 'NCDU', 'NEW CDU ANGLES', kind='interp', line=64)
W('22,3053', 0o77414, '', 'BONCLR', 'EXIT', kind='interp', line=65)
W('22,3054', 0o01215, '', '', 'CALCMAN2', kind='operand', line=66)
W('22,3055', 0o40065, '', '', 'MANUSTAT', 'TO START MANEUVER', kind='operand', line=67)
W('22,3056', 0o35016, '', 'CAF', 'TWO', '         +0 OTHERWISE', line=68)
W('22,3057', 0o55664, 'INCRDCDU', 'TS', 'KSPNDX', line=69)
W('22,3060', 0o60000, '', 'DOUBLE', line=70)
W('22,3061', 0o55665, '', 'TS', 'KDPNDX', line=71)
W('22,3062', 0o51664, '', 'INDEX', 'KSPNDX', line=72)
W('22,3063', 0o31666, '', 'CA', 'NCDU', 'NEW DESIRED CDU ANGLES', line=73)
W('22,3064', 0o00006, '', 'EXTEND', line=74)
W('22,3065', 0o51664, '', 'INDEX', 'KSPNDX', line=75)
W('22,3066', 0o21661, '', 'MSU', 'BCDU', 'INITIAL S/C ANGLE OR PREVIOUS DESIRED', line=76)
W('22,3067', 0o00006, '', 'EXTEND', '', 'CDU ANGLES', line=77)
W('22,3070', 0o73002, '', 'MP', 'QUADROT', line=78)
W('22,3071', 0o51665, '', 'INDEX', 'KDPNDX', line=79)
W('22,3072', 0o53576, '', 'DXCH', 'DELCDUX', 'ANGEL INCREMENTS TO BE ADDED TO', line=80)
# Page 415
W('22,3073', 0o51664, '', 'INDEX', 'KSPNDX', 'DCDU EVERY TENTH SEC', line=82)
W('22,3074', 0o31666, '', 'CA', 'NCDU', 'BY LEM DAP', line=83)
W('22,3075', 0o51664, '', 'INDEX', 'KSPNDX', line=84)
W('22,3076', 0o57661, '', 'XCH', 'BCDU', line=85)
W('22,3077', 0o51665, '', 'INDEX', 'KDPNDX', line=86)
W('22,3100', 0o55646, '', 'TS', 'CDUXD', line=87)
W('22,3101', 0o11664, '', 'CCS', 'KSPNDX', line=88)
W('22,3102', 0o13057, '', 'TCF', 'INCRDCDU', 'LOOP FOR THREE AXES', line=89)

W('22,3103', 0o00003, '', 'RELINT', line=91)
# COMPARE PRESENT TIME WITH TIME TO TERMINATE MANEUVER

W('22,3104', 0o03115, 'TMANUCHK', 'TC', 'TIMECHK', line=94)
W('22,3105', 0o04701, '', 'TC', 'POSTJUMP', line=95)
W('22,3106', 0o40131, '', 'CADR', 'CONTMANU', kind='data', line=96)

W('22,3107', 0o35017, '', 'CAF', 'ONE', line=98)
W('22,3110', 0o05245, 'MANUSTAL', 'TC', 'WAITLIST', line=99)
#   EBANK= BCDU
W('22,3111', 0o02000, '', '2CADR', 'MANUSTOP', kind='data', line=101)
W('22,3112', 0o42066, kind='data', line=101)

W('22,3113', 0o00003, '', 'RELINT', line=103)
W('22,3114', 0o15217, '', 'TCF', 'ENDOFJOB', line=104)

W('22,3115', 0o00006, 'TIMECHK', 'EXTEND', line=107)
W('22,3116', 0o40025, '', 'DCS', 'TIME2', line=108)
W('22,3117', 0o53673, '', 'DXCH', 'TTEMP', line=109)
W('22,3120', 0o00006, '', 'EXTEND', line=110)
W('22,3121', 0o31717, '', 'DCA', 'TM', line=111)
W('22,3122', 0o21673, '', 'DAS', 'TTEMP', line=112)
W('22,3123', 0o11672, '', 'CCS', 'TTEMP', line=113)
W('22,3124', 0o00002, '', 'TC', 'Q', line=114)
W('22,3125', 0o13127, '', 'TCF', '+2', line=115)
W('22,3126', 0o13137, '', 'TCF', '2NDRETRN', line=116)
W('22,3127', 0o11673, '', 'CCS', 'TTEMP +1', line=117)
W('22,3130', 0o00002, '', 'TC', 'Q', line=118)
W('22,3131', 0o13133, '', 'TCF', 'MANUOFF', line=119)
W('22,3132', 0o40000, '', 'COM', line=120)
W('22,3133', 0o65041, 'MANUOFF', 'AD', '1SEC', line=121)
W('22,3134', 0o00006, '', 'EXTEND', line=122)
W('22,3135', 0o63137, '', 'BZMF', '2NDRETRN', line=123)
W('22,3136', 0o24002, '', 'INCR', 'Q', line=124)
W('22,3137', 0o24002, '2NDRETRN', 'INCR', 'Q', line=125)
W('22,3140', 0o24002, '', 'INCR', 'Q', line=126)
W('22,3141', 0o00002, '', 'TC', 'Q', line=127)

#   SETLOC MANUSTUF
#   BANK
# Page 416
W('20,2065', 0o77776, 'MANUSTAT', 'EXIT', '', 'INITIALIZATION ROUTINE', kind='interp', line=132)
W('20,2066', 0o00006, '', 'EXTEND', '', 'FOR AUTOMATIC MANEUVERS', line=133)
W('20,2067', 0o30025, '', 'DCA', 'TIME2', line=134)
W('20,2070', 0o21717, '', 'DAS', 'TM', 'TM+T0    MANEUVER COMPLETION TIME', line=135)
W('20,2071', 0o45041, '', 'CS', '1SEC', line=136)
W('20,2072', 0o54001, '', 'TS', 'L', line=137)
W('20,2073', 0o45021, '', 'CS', 'ZERO', line=138)
W('20,2074', 0o21717, '', 'DAS', 'TM', '(TM+T0)-1', line=139)
W('20,2075', 0o00004, '', 'INHINT', line=140)
W('20,2076', 0o45017, '', 'CS', 'ONE', 'ENABLE AUTOPILOT TO PERFORM', line=141)
W('20,2077', 0o55332, '', 'TS', 'HOLDFLAG', 'AUTOMATIC MANEUVERS', line=142)
W('20,2100', 0o41130, '', 'CS', 'RATEINDX', 'SEE IF MANEUVERING AT HIGH RATE', line=143)
W('20,2101', 0o66211, '', 'AD', 'SIX', line=144)
W('20,2102', 0o00006, '', 'EXTEND', line=145)
W('20,2103', 0o62105, '', 'BZMF', 'HIGHGAIN', line=146)
W('20,2104', 0o12110, '', 'TCF', '+4', line=147)
W('20,2105', 0o41501, 'HIGHGAIN', 'CS', 'RCSFLAGS', 'IF SO, SET HIGH RATE FLAG (BIT 15 OF', line=148)
W('20,2106', 0o75001, '', 'MASK', 'BIT15', 'RCSFLAGS)', line=149)
W('20,2107', 0o27501, '', 'ADS', 'RCSFLAGS', line=150)
W('20,2110', 0o53711, '', 'DXCH', 'BRATE', 'X-AXIS MANEUVER RATE', line=151)
W('20,2111', 0o53526, '', 'DXCH', 'WBODY', line=152)
W('20,2112', 0o53713, '', 'DXCH', 'BRATE +2', 'Y-AXIS MANEUVER RATE', line=153)
W('20,2113', 0o53530, '', 'DXCH', 'WBODY1', line=154)
W('20,2114', 0o53715, '', 'DXCH', 'BRATE +4', 'Z-AXIS MANEUVER RATE', line=155)
W('20,2115', 0o53532, '', 'DXCH', 'WBODY2', line=156)
W('20,2116', 0o31675, '', 'CA', 'BIASTEMP +1', 'INSERT ATTITUDE ERROR BIASES', line=157)
W('20,2117', 0o55564, '', 'TS', 'BIAS', 'INTO AUTOPILOT', line=158)
W('20,2120', 0o31677, '', 'CA', 'BIASTEMP +3', line=159)
W('20,2121', 0o55565, '', 'TS', 'BIAS1', line=160)
W('20,2122', 0o31701, '', 'CA', 'BIASTEMP +5', line=161)
W('20,2123', 0o55566, '', 'TS', 'BIAS2', line=162)
W('20,2124', 0o30025, '', 'CA', 'TIME1', line=163)
W('20,2125', 0o65041, '', 'AD', '1SEC', line=164)
W('20,2126', 0o57671, '', 'XCH', 'NEXTIME', line=165)
W('20,2127', 0o04701, '', 'TC', 'POSTJUMP', line=166)
W('20,2130', 0o45056, '', 'CADR', 'INCRDCDU -1', kind='data', line=167)

W('20,2131', 0o00004, 'CONTMANU', 'INHINT', '', 'CONTINUE WITH UPDATE PROCESS', line=169)
W('20,2132', 0o40025, '', 'CS', 'TIME1', line=170)
W('20,2133', 0o61671, '', 'AD', 'NEXTIME', line=171)
W('20,2134', 0o10000, '', 'CCS', 'A', line=172)
W('20,2135', 0o65017, '', 'AD', 'ONE', line=173)
W('20,2136', 0o12141, '', 'TCF', 'MANUCALL', line=174)
W('20,2137', 0o65001, '', 'AD', 'NEGMAX', line=175)
W('20,2140', 0o40000, '', 'COM', line=176)
W('20,2141', 0o05245, 'MANUCALL', 'TC', 'WAITLIST', line=177)
#   EBANK= BCDU
W('20,2142', 0o02150, '', '2CADR', 'UPDTCALL', kind='data', line=179)
W('20,2143', 0o40066, kind='data', line=179)

W('20,2144', 0o00003, '', 'RELINT', line=181)
# Page 417
W('20,2145', 0o35041, '', 'CAF', '1SEC', 'INCREMENT TIME FOR NEXT UPDATE', line=183)
W('20,2146', 0o27671, '', 'ADS', 'NEXTIME', line=184)
W('20,2147', 0o15217, '', 'TCF', 'ENDOFJOB', line=185)

W('20,2150', 0o37663, 'UPDTCALL', 'CAF', 'PRIO26', 'CALL FOR UPDATE', line=188)
W('20,2151', 0o05147, '', 'TC', 'FINDVAC', 'OF STEERING COMMANDS', line=189)
#   EBANK= BCDU
W('20,2152', 0o03026, '', '2CADR', 'NEWDELHI', kind='data', line=191)
W('20,2153', 0o44066, kind='data', line=191)

W('20,2154', 0o05324, '', 'TC', 'TASKOVER', line=193)

# Page 418
# ROUTINE FOR TERMINATING AUTOMATIC MANEUVERS

#   SETLOC KALCMON3
#   BANK

W('21,2000', 0o04537, 'MANUSTOP', 'TC', 'STOPYZ', line=201)
W('21,2001', 0o04740, '', 'TC', 'IBNKCALL', line=202)
W('21,2002', 0o45144, '', 'CADR', 'LOADYZ', kind='data', line=203)

W('21,2003', 0o31155, 'ENDROLL', 'CA', 'CPHI', line=205)
W('21,2004', 0o55646, '', 'TS', 'CDUXD', 'SET CDUXD TO THE COMMANDED OUTER GIMBAL', line=206)
W('21,2005', 0o04526, '', 'TC', 'STOPRATE', line=207)
W('21,2006', 0o31327, 'ENDMANU', 'CA', 'ATTPRIO', 'RESTORE USERS PRIORITY', line=208)
W('21,2007', 0o54063, '', 'TS', 'NEWPRIO', line=209)

W('21,2010', 0o35021, '', 'CA', 'ZERO', 'ZERO ATTCADR', line=211)
W('21,2011', 0o53326, '', 'DXCH', 'ATTCADR', line=212)

W('21,2012', 0o05160, '', 'TC', 'SPVAC', 'RETURN TO USER OF GOMANUR', line=214)

W('21,2013', 0o05324, '', 'TC', 'TASKOVER', line=216)

#   SETLOC STOPRAT
#   BANK
W('4526', 0o35021, 'STOPRATE', 'CAF', 'ZERO', line=220)
W('4527', 0o55575, '', 'TS', 'DELCDUX', line=221)
W('4530', 0o55576, '', 'TS', 'DELCDUX +1', 'ZERO ROLL INCREMENTAL ANGLES', line=222)
W('4531', 0o55525, '', 'TS', 'WBODY', 'RATE', line=223)
W('4532', 0o55526, '', 'TS', 'WBODY +1', line=224)
W('4533', 0o55564, '', 'TS', 'BIAS', 'BIAS', line=225)

W('4534', 0o45001, '', 'CS', 'BIT15', 'MAKE SURE HIGH RATE FLAG (BIT 15 OF', line=227)
W('4535', 0o71501, '', 'MASK', 'RCSFLAGS', 'RCSFLAGS) IS RESET.', line=228)
W('4536', 0o55501, '', 'TS', 'RCSFLAGS', line=229)

W('4537', 0o35021, 'STOPYZ', 'CAF', 'ZERO', line=231)
W('4540', 0o55577, '', 'TS', 'DELCDUY', 'ZERO PITCH, YAW', line=232)
W('4541', 0o55600, '', 'TS', 'DELCDUY +1', 'INCREMENTAL ANGLES', line=233)
W('4542', 0o55601, '', 'TS', 'DELCDUZ', line=234)
W('4543', 0o55602, '', 'TS', 'DELCDUZ +1', line=235)
W('4544', 0o55527, '', 'TS', 'WBODY1', 'RATES', line=236)
W('4545', 0o55530, '', 'TS', 'WBODY1 +1', line=237)
W('4546', 0o55531, '', 'TS', 'WBODY2', line=238)
W('4547', 0o55532, '', 'TS', 'WBODY2 +1', line=239)
W('4550', 0o55565, '', 'TS', 'BIAS1', 'BIASES', line=240)
W('4551', 0o55566, '', 'TS', 'BIAS2', line=241)
W('4552', 0o00002, '', 'TC', 'Q', line=242)

#   SETLOC MANUSTUF
#   BANK

# Page 419
W('20,2155', 0o30032, 'ZEROEROR', 'CA', 'CDUX', 'PICK UP CDU ANGLES AND STORE IN', line=248)
W('20,2156', 0o55646, '', 'TS', 'CDUXD', 'CDU DESIRED', line=249)
W('20,2157', 0o30033, '', 'CA', 'CDUY', line=250)
W('20,2160', 0o55650, '', 'TS', 'CDUYD', line=251)
W('20,2161', 0o30034, '', 'CA', 'CDUZ', line=252)
W('20,2162', 0o55652, '', 'TS', 'CDUZD', line=253)
W('20,2163', 0o00002, '', 'TC', 'Q', line=254)

#   SETLOC KALCMON1
#   BANK

W('22,3142', 0o31155, 'LOADCDUD', 'CA', 'CPHI', 'STORE TERMINAL ANGLES INTO', line=259)
W('22,3143', 0o55646, '', 'TS', 'CDUXD', 'COMMAND ANGLES', line=260)
W('22,3144', 0o31156, 'LOADYZ', 'CA', 'CTHETA', line=261)
W('22,3145', 0o55650, '', 'TS', 'CDUYD', line=262)
W('22,3146', 0o31157, '', 'CA', 'CPSI', line=263)
W('22,3147', 0o55652, '', 'TS', 'CDUZD', line=264)
W('22,3150', 0o00002, '', 'TC', 'Q', line=265)
