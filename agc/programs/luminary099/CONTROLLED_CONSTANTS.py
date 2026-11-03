"""CONTROLLED_CONSTANTS.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/CONTROLLED_CONSTANTS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 38-53 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('CONTROLLED_CONSTANTS', 'CONTROLLED_CONSTANTS.agc', 'Luminary099', pages='38-53')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     CONTROLLED_CONSTANTS.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
#
# Assembler:    yaYUL
# Contact:      Jim Lawton <jim.lawton@gmail.com>
# Website:      www.ibiblio.org/apollo.
# Pages:        038-053
# Mod history:  2009-05-16      JVL     Transcribed from page images.
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
# Assemble revision 001 of AGC program LMY99 by NASA 2021112-061
# 16:27 JULY 14, 1969

# Page 38
# DPS AND APS ENGINE PARAMETERS

#   SETLOC P40S
#   BANK
#   COUNT* $$/P40

# *** THE ORDER OF THE FOLLOWING SIX CONSTANTS MUST NOT BE CHANGED ***

W('36,2000', 0o01056, 'FDPS', '2DEC', '4.3670 B-7', '9817.5 LBS FORCE IN NEWTONS', kind='data', line=36)
W('36,2001', 0o37167, kind='data', line=36)
W('36,2002', 0o00457, 'MDOTDPS', '2DEC', '0.1480 B-3', '32.62 LBS/SEC IN KGS/CS', kind='data', line=37)
W('36,2003', 0o03250, kind='data', line=37)
W('36,2004', 0o77777, 'DTDECAY', '2DEC', '-38', kind='data', line=38)
W('36,2005', 0o77731, kind='data', line=38)
W('36,2006', 0o00307, 'FAPS', '2DEC', '1.5569 B-7', '3500 LBS FORCE IN NEWTONS', kind='data', line=39)
W('36,2007', 0o11040, kind='data', line=39)
W('36,2010', 0o00151, 'MDOTAPS', '2DEC', '0.05135 B-3', '11.32 LBS/SEC IN KGS/CS', kind='data', line=40)
W('36,2011', 0o05214, kind='data', line=40)
W('36,2012', 0o77777, 'ATDECAY', '2DEC', '-10', kind='data', line=41)
W('36,2013', 0o77765, kind='data', line=41)

# ********************************************************************

W('36,2014', 0o00026, 'FRCS4', '2DEC', '0.17792 B-7', '400 LBS FORCE IN NEWTONS', kind='data', line=45)
W('36,2015', 0o30605, kind='data', line=45)
W('36,2016', 0o00013, 'FRCS2', '2DEC', '0.08896 B-7', '200 LBS FORCE IN NEWTONS', kind='data', line=46)
W('36,2017', 0o14303, kind='data', line=46)

#   SETLOC P40S1
#   BANK
#   COUNT* $$/P40

# *** APS IMPULSE DATA FOR P42 ***************************************

W('27,2000', 0o00000, 'K1VAL', '2DEC', '124.55 B-23', '2800 LB-SEC', kind='data', line=54)
W('27,2001', 0o07622, kind='data', line=54)
W('27,2002', 0o00000, 'K2VAL', '2DEC', '31.138 B-24', '700 LB-SEC', kind='data', line=55)
W('27,2003', 0o00762, kind='data', line=55)
W('27,2004', 0o00030, 'K3VAL', '2DEC', '1.5569 B-10', 'FAPS (3500 LBS THRUST)', kind='data', line=56)
W('27,2005', 0o35104, kind='data', line=56)

# ********************************************************************

W('27,2006', 0o00016, 'S40.136', '2DEC', '.4671 B-9', '.4671 M NEWTONS (DPS)', kind='data', line=60)
W('27,2007', 0o36237, kind='data', line=60)
W('27,2010', 0o35711, 'S40.136_', '2DEC', '.4671 B+1', 'S40.136 SHIFTED LEFT 10.', kind='data', line=61)
W('27,2011', 0o35663, kind='data', line=61)

#   SETLOC ASENT1
#   BANK
#   COUNT* $$/P70

W('27,2012', 0o03631, '(1/DV)A', '2DEC', '15.20 B-7', '2 SECONDS WORTH OF INITIAL ASCENT', kind='data', line=67)
W('27,2013', 0o23146, kind='data', line=67)
# Page 39
# STAGE ACCELERATION -- INVERTED (M/CS)
# 1) PREDICATED ON A LIFTOFF MASS OF
# 4869.9 KG (SNA-8-D-027 7/11/68)
# 2) PREDICATED ON A CONTRIBUTION TO VEH-
# ICLE ACCELERATION FROM RCS THRUSTERS
# EQUIV. TO 1 JET ON CONTINUOUSLY.

W('27,2014', 0o33226, 'K(1/DV)', '2DEC', '436.70 B-9', 'DPS ENGINE THRUST IN NEWTONS / 100 CS.', kind='data', line=76)
W('27,2015', 0o14632, kind='data', line=76)

W('27,2016', 0o05306, '(AT)A', '2DEC', '3.2883 E-4 B9', 'INITIAL ASC. STG. ACCELERATION ** M/CS.', kind='data', line=78)
W('27,2017', 0o15503, kind='data', line=78)
# ASSUMPTIONS SAME AS FOR (1/DV)A.
W('27,2020', 0o26337, '(TBUP)A', '2DEC', '91902 B-17', 'ESTIMATED BURN-UP TIME OF THE ASCENT STG.', kind='data', line=80)
W('27,2021', 0o30000, kind='data', line=80)
# ASSUMPTIONS SAME AS FOR (1/DV)A WITH THE
# ADDITIONAL ASSUMPTION THAT NET MASS-FLOW
# RATE = 5.299 KG/SEC = 5.135 (APS) +
# .164 (1 RCS JET).
#   SETLOC ASENT
#   BANK
#   COUNT* $$/ASENT
W('30,2000', 0o02445, 'AT/RCS', '2DEC', '.0000785 B+10', '4 JETS IN A DRY LEM', kind='data', line=88)
W('30,2001', 0o00274, kind='data', line=88)

#   SETLOC SERVICES
#   BANK
#   COUNT* $$/SERV

# *** THE ORDER OF THE FOLLOWING TWO CONSTANTS MUST NOT BE CHANGED *******

W('33,2000', 0o41545, 'APSVEX', 'DEC', '-3030 E-2 B-5', '9942 FT/SEC IN M/CS.', kind='data', line=96)
W('33,2001', 0o42341, 'DPSVEX', 'DEC*', '-2.95588868 E+1 B-05*', 'VE (DPS) +2.95588868E+ 3', kind='data', line=97)

# ************************************************************************

#   SETLOC F2DPS*31
#   BANK
#   COUNT* $$/F2DPS

W('31,2000', 0o00222, 'TRIMACCL', '2DEC*', '+3.50132708 E-5 B+08*', 'A (T) +3.50132708E- 1', kind='data', line=105)
W('31,2001', 0o33316, kind='data', line=105)

# Page 40
# THROTTLING AND THRUST DETECTION PARAMETERS

#   SETLOC P40S
#   BANK
#   COUNT* $$/P40

W('36,2020', 0o00030, 'THRESH1', 'DEC', '24', kind='data', line=114)
W('36,2021', 0o00014, 'THRESH3', 'DEC', '12', kind='data', line=115)
S('HIRTHROT', 'equals', 0o4737, line=116)

#   SETLOC FFTAG5
#   BANK
#   COUNT* $$/P40

W('6000', 0o00464, 'THRESH2', 'DEC', '308', kind='data', line=122)

#   SETLOC FTHROT
#   BANK
#   COUNT* $$/THROT

W('31,2002', 0o07401, 'FMAXODD', 'DEC', '+3841', 'FSAT          +4.81454413 E+4', kind='data', line=128)
W('31,2003', 0o06613, 'FMAXPOS', 'DEC', '+3467', 'FMAX          +4.34546769 E+4', kind='data', line=129)
W('31,2004', 0o00024, 'THROTLAG', 'DEC', '+20', 'TAU (TH)      +1.99999999 E-1', kind='data', line=130)
W('31,2005', 0o00307, 'SCALEFAC', '2DEC*', '+7.97959872 E+2 B-16*', 'BITPERF       +7.97959872 E-2', kind='data', line=131)
W('31,2006', 0o17534, kind='data', line=131)

#   SETLOC F2DPS*32
#   BANK
#   COUNT* $$/F2DPS

W('32,2000', 0o00044, 'DPSTHRSH', 'DEC', '36', '(THRESH1 + THRESH3 FOR P63)', kind='data', line=137)

# Page 41
# LM HARDWARE-RELATED PARAMETERS

#   SETLOC RADARUPT
#   BANK
#   COUNT* $$/RRUPT

W('25,2000', 0o47777, 'LVELBIAS', 'DEC', '-12288', 'LANDING RADAR BIAS FOR 153.6 KC.', kind='data', line=146)
W('25,2001', 0o00001, 'RDOTBIAS', '2DEC', '17000', 'BIAS COUNT FOR RR RANGE RATE.', kind='data', line=147)
W('25,2002', 0o01150, kind='data', line=147)

#   SETLOC LRS22
#   BANK
#   COUNT* $$/LRS22

W('32,2001', 0o70123, 'RDOTCONV', '2DEC', '-.0019135344 B7', 'CONVERTS RR RDOT READING TO M/CS AT 2(7)', kind='data', line=153)
W('32,2002', 0o40702, kind='data', line=153)
W('32,2003', 0o13337, 'RANGCONV', '2DEC', '2.859024 B-3', 'CONVERTS RR RANGE READING TO M. AT 2(-29', kind='data', line=154)
W('32,2004', 0o10776, kind='data', line=154)

#   SETLOC SERVICES
#   BANK
#   COUNT* $$/SERV

W('33,2002', 0o61000, 'HBEAMANT', '2DEC', '-.4687018041', 'RANGE BEAM IN LR ANTENNA COORDINATES.', kind='data', line=160)
W('33,2003', 0o71210, kind='data', line=160)
W('33,2004', 0o00000, '', '2DEC', '0', kind='data', line=161)
W('33,2005', 0o00000, kind='data', line=161)
W('33,2006', 0o72333, '', '2DEC', '-.1741224271', kind='data', line=162)
W('33,2007', 0o45546, kind='data', line=162)

W('33,2010', 0o65363, 'HSCAL', '2DEC', '-.3288792', 'SCALES 1.079 FT/BIT TO 2(22)M.', kind='data', line=164)
W('33,2011', 0o64451, kind='data', line=164)

# ***** THE SEQUENCE OF THE FOLLOWING CONSTANTS MUST BE PRESERVED *********

W('33,2012', 0o21241, 'VZSCAL', '2DEC', '+.5410829105', 'SCALES .8668 FT/SEC/BIT TO 2(18) M/CS.', kind='data', line=168)
W('33,2013', 0o03216, kind='data', line=168)
W('33,2014', 0o30153, 'VYSCAL', '2DEC', '+.7565672446', 'SCALES 1.212 FT/SEC/BIT TO 2(18) M/CS.', kind='data', line=169)
W('33,2015', 0o23101, kind='data', line=169)
W('33,2016', 0o63105, 'VXSCAL', '2DEC', '-.4020043770', 'SCALES -.644 FT/SEC/BIT TO 2(18) M/CS.', kind='data', line=170)
W('33,2017', 0o61733, kind='data', line=170)

# *************************************************************************

W('33,2020', 0o01507, 'KPIP', 'DEC', '.0512', 'SCALES DELV TO UNITS OF 2(5) M/CS.', kind='data', line=174)
W('33,2021', 0o00321, 'KPIP1', '2DEC', '.0128', 'SCALES DELV TO UNITS OF 2(7) M/CS.', kind='data', line=175)
W('33,2022', 0o26706, kind='data', line=175)
W('33,2023', 0o00150, 'KPIP2', '2DEC', '.0064', 'SCALES DELV TO UNITS OF 2(8) M/CS.', kind='data', line=176)
W('33,2024', 0o33343, kind='data', line=176)

# Page 42
W('33,2025', 0o02630, 'ALTCONV', '2DEC', '1.399078846 B-4', 'CONVERTS M*2(-24) TO BIT UNITS *2(-28).', kind='data', line=179)
W('33,2026', 0o25010, kind='data', line=179)
W('33,2027', 0o24402, 'ARCONV1', '2DEC', '656.167979 B-10', 'CONV. ALTRATE COMP. TO BIT UNITS<', kind='data', line=180)
W('33,2030', 0o26003, kind='data', line=180)

#   SETLOC R10
#   BANK
#   COUNT* $$/R10

W('21,2000', 0o24402, 'ARCONV', 'OCT', '24402', '656.1679798B-10 CONV ALTRATE TO BIT UNIT', kind='data', line=186)
W('21,2001', 0o01551, 'ARTOA', 'DEC', '.1066098 B-1', '.25/2.345 B-1 4X/SEC CYCLE RATE.', kind='data', line=187)
W('21,2002', 0o21357, 'ARTOA2', 'DEC', '.0021322 B8', '(.5)/(2.345)(100)', kind='data', line=188)
W('21,2003', 0o22316, 'VELCONV', 'OCT', '22316', '588.914 B-10 CONV VEL. TO BIT UNITS.', kind='data', line=189)
W('21,2004', 0o01507, 'KPIP1(5)', 'DEC', '.0512', 'SCALES DELV TO M/CS*2(-5).', kind='data', line=190)
W('21,2005', 0o00547, 'MAXVBITS', 'OCT', '00547', 'MAX. DISPLAYED VELOCITY 199.9989 FT/SEC.', kind='data', line=191)

#   SETLOC DAPS3
#   BANK
#   COUNT* $$/DAPAO

W('20,2000', 0o01150, 'TORKJET1', 'DEC', '.03757', '550 / .2 SCALED AT (+16) 64 / 180', kind='data', line=197)

# Page 43
# PARAMETERS RELATING TO MASS, INERTIA, AND VEHICLE DIMENSIONS

#   SETLOC FRANDRES
#   BANK
#   COUNT* $$/START

W('05,2000', 0o02357, 'FULLAPS', 'DEC', '5050 B-16', 'NOMINAL FULL ASCENT MASS -- 2(16) KG.', kind='data', line=206)

#   SETLOC LOADDAP1
#   BANK
#   COUNT* $$/R03

W('01,2000', 0o76466, 'MINLMD', 'DEC', '-2850 B-16', 'MIN. DESCENT STAGE MASS -- 2(16) KG.', kind='data', line=212)
W('01,2001', 0o76731, 'MINMINLM', 'DEC', '-2200 B-16', 'MIN ASCENT STAGE MASS -- 2(16) KG.', kind='data', line=213)
S('MINCSM', 'equals', 0o4741, line=214)  # MIN CSM MASS (OK FOR 1/ACCS) = 9050 LB

#   SETLOC DAPS3
#   BANK
#   COUNT* $$/DAPAD

W('20,2001', 0o01046, 'LOASCENT', 'DEC', '2200 B-16', 'MIN ASCENT LEM MASS -- 2(16) KG.', kind='data', line=220)
W('20,2002', 0o07361, 'HIDESCNT', 'DEC', '15300 B-16', 'MAX DESCENT LEM MASS -- 2(16) KG.', kind='data', line=221)
W('20,2003', 0o00666, 'LODESCNT', 'DEC', '1750 B-16', 'MIN DESCENT STAGE (ALONE) -- 2(16) KG.', kind='data', line=222)

# Page 44
# PHYSICAL CONSTANTS ( TIME - INVARIANT )

#   SETLOC IMU2
#   BANK
#   COUNT* $$/P07

W('37,2000', 0o07623, 'OMEG/MS', '2DEC', '.24339048', kind='data', line=231)
W('37,2001', 0o26552, kind='data', line=231)

#   SETLOC R30LOC
#   BANK
#   COUNT* $$/R30

# *** THE ORDER OF THE FOLLOWING TWO CONSTANTS MUST BE PRESERVED ***********

W('22,2000', 0o27533, '1/RTMUM', '2DEC*', '.45162595 E-4 B14*', kind='data', line=239)
W('22,2001', 0o07571, kind='data', line=239)
W('22,2002', 0o25004, '1/RTMUE', '2DEC*', '.50087529 E-5 B17*', kind='data', line=240)
W('22,2003', 0o06702, kind='data', line=240)

# **************************************************************************

#   SETLOC P40S1
#   BANK
#   COUNT* $$/S40.9

W('27,2022', 0o55340, 'EARTHMU', '2DEC*', '-3.986032 E10 B-36*', 'M(3)/CS(2)', kind='data', line=248)
W('27,2023', 0o61710, kind='data', line=248)

#   SETLOC ASENT1
#   BANK
#   COUNT* $$/P12

W('27,2024', 0o00072, 'MUM(-37)', '2DEC*', '4.9027780 E8 B-37*', kind='data', line=254)
W('27,2025', 0o16206, kind='data', line=254)
W('27,2026', 0o00344, 'MOONRATE', '2DEC*', '.26616994890062991 E-7 B+19*', 'RAD/CS.', kind='data', line=255)
W('27,2027', 0o24331, kind='data', line=255)

#   SETLOC SERVICES
#   BANK
#   COUNT* $$/SERV

# *** THE ORDER OF THE FOLLOWING TWO CONSTANTS MUST BE PRESERVED ***********

W('33,2031', 0o61377, '-MUDT', '2DEC*', '-7.9720645 E+12 B-44*', kind='data', line=263)
W('33,2032', 0o55754, kind='data', line=263)
W('33,2033', 0o77644, '-MUDT1', '2DEC*', '-9.8055560 E+10 B-44*', kind='data', line=264)
W('33,2034', 0o65556, kind='data', line=264)

# **************************************************************************

W('33,2035', 0o64453, '-MUDTMUN', '2DEC*', '-9.8055560 E+10 B-38*', kind='data', line=268)
W('33,2036', 0o55670, kind='data', line=268)
W('33,2037', 0o00002, 'RESQ', '2DEC*', '40.6809913 E12 B-58*', kind='data', line=269)
W('33,2040', 0o11777, kind='data', line=269)

# Page 45
W('33,2041', 0o01023, '20J', '2DEC', '3.24692010 E-2', kind='data', line=272)
W('33,2042', 0o37155, kind='data', line=272)
W('33,2043', 0o00065, '2J', '2DEC', '3.24692010 E-3', kind='data', line=273)
W('33,2044', 0o06244, kind='data', line=273)

#   SETLOC P50S1
#   BANK
#   COUNT* $$/LOSAM

W('14,2000', 0o26723, 'RSUBEM', '2DEC', '384402000 B-29', kind='data', line=279)
W('14,2001', 0o00450, kind='data', line=279)
W('14,2002', 0o00065, 'RSUBM', '2DEC', '1738090 B-29', kind='data', line=280)
W('14,2003', 0o01265, kind='data', line=280)
W('14,2004', 0o00302, 'RSUBE', '2DEC', '6378166 B-29', kind='data', line=281)
W('14,2005', 0o24533, kind='data', line=281)
W('14,2006', 0o00052, 'ROE', '2DEC', '.00257125', kind='data', line=282)
W('14,2007', 0o04047, kind='data', line=282)

#   SETLOC CONICS1
#   BANK
#   COUNT* $$/LT-LG

W('04,2000', 0o00302, 'ERAD', '2DEC', '6373338 B-29', 'PAD RADIUS', kind='data', line=288)
W('04,2001', 0o17755, kind='data', line=288)
W('04,2002', 0o00065, '504RM', '2DEC', '1738090 B-29', 'METERS B-29 (EQUATORIAL MOON RADIUS)', kind='data', line=289)
W('04,2003', 0o01265, kind='data', line=289)

#   SETLOC CONICS1
#   BANK
#   COUNT* $$/CONIC

# *** THE ORDER OF THE FOLLOWING CONSTANTS MUST BE PRESERVED **************

W('04,2004', 0o22437, 'MUTABLE', '2DEC*', '3.986032 E10 B-36*', 'MUE', kind='data', line=297)
W('04,2005', 0o16067, kind='data', line=297)
W('04,2006', 0o15625, '', '2DEC*', '.25087606 E-10 B+34*', '1/MUE', kind='data', line=298)
W('04,2007', 0o21042, kind='data', line=298)
W('04,2010', 0o30276, '', '2DEC*', '1.99650495 E5 B-18*', 'SQRT(MUE)', kind='data', line=299)
W('04,2011', 0o04773, kind='data', line=299)
W('04,2012', 0o25004, '', '2DEC*', '.50087529 E-5 B+17*', '1/SQRT(MUE)', kind='data', line=300)
W('04,2013', 0o06702, kind='data', line=300)
W('04,2014', 0o16471, '', '2DEC*', '4.902778 E8 B-30*', 'MUM', kind='data', line=301)
W('04,2015', 0o01352, kind='data', line=301)
W('04,2016', 0o21412, '', '2DEC*', '.203966 E-8 B+28*', '1/MUM', kind='data', line=302)
W('04,2017', 0o20500, kind='data', line=302)
W('04,2020', 0o25477, '', '2DEC*', '2.21422176 E4 B-15*', 'SQRT(MUM)', kind='data', line=303)
W('04,2021', 0o03367, kind='data', line=303)
W('04,2022', 0o27533, '', '2DEC*', '.45162595 E-4 B+14*', '1/SQRT(MUM)', kind='data', line=304)
W('04,2023', 0o07571, kind='data', line=304)

# *************************************************************************

# Page 46
#   SETLOC INTINIT
#   BANK
#   COUNT* $$/INTIN

W('13,2000', 0o07112, 'OMEGMOON', '2DEC*', '2.66169947 E-8 B+23*', kind='data', line=313)
W('13,2001', 0o06620, kind='data', line=313)

#   SETLOC ORBITAL2
#   BANK
#   COUNT* $$/ORBIT

# *** THE ORDER OF THE FOLLOWING CONSTANTS MUST NOT BE CHANGED ************

W('13,2002', 0o27446, '', '2DEC*', '1.32715445 E16 B-54*', kind='data', line=321)
W('13,2003', 0o14620, kind='data', line=321)
W('13,2004', 0o16471, 'MUM', '2DEC*', '4.9027780 E8 B-30*', kind='data', line=322)
W('13,2005', 0o01352, kind='data', line=322)
W('13,2006', 0o22437, 'MUEARTH', '2DEC*', '3.986032 E10 B-36*', kind='data', line=323)
W('13,2007', 0o16067, kind='data', line=323)
W('13,2010', 0o00000, '', '2DEC', '0', kind='data', line=324)
W('13,2011', 0o00000, kind='data', line=324)
W('13,2012', 0o02302, 'J4REQ/J3', '2DEC*', '.4991607391 E7 B-26*', kind='data', line=325)
W('13,2013', 0o24736, kind='data', line=325)
W('13,2014', 0o77651, '', '2DEC', '-176236.02 B-25', kind='data', line=326)
W('13,2015', 0o76237, kind='data', line=326)
W('13,2016', 0o77776, '2J3RE/J2', '2DEC*', '-.1355426363 E5 B-27*', kind='data', line=327)
W('13,2017', 0o53032, kind='data', line=327)
W('13,2020', 0o10407, '', '2DEC*', '.3067493316 E18 B-60*', kind='data', line=328)
W('13,2021', 0o05344, kind='data', line=328)
W('13,2022', 0o13710, 'J2REQSQ', '2DEC*', '1.75501139 E21 B-72*', kind='data', line=329)
W('13,2023', 0o35320, kind='data', line=329)
W('13,2024', 0o12160, '3J22R2MU', '2DEC*', '9.20479048 E16 B-58*', kind='data', line=330)
W('13,2025', 0o12124, kind='data', line=330)

# *************************************************************************

#   SETLOC TOF-FF1
#   BANK
#   COUNT* $$/TFF

W('27,2030', 0o24775, '1/RTMU', '2DEC*', '.5005750271 E-5 B17*', 'MODIFIED EARTH MU', kind='data', line=338)
W('27,2031', 0o30424, kind='data', line=338)

#   SETLOC SBAND
#   BANK
#   COUNT* $$/R05

W('42,2000', 0o26723, 'REMDIST', '2DEC', '384402000 B-29', 'MEAN DISTANCE BETWEEN EARTH AND MOON.', kind='data', line=344)
W('42,2001', 0o00450, kind='data', line=344)

# Page 47
# PHYSICAL CONSTANTS (TIME - VARIANT)

#   SETLOC STARTAB
#   BANK
#   COUNT* $$/STARS

W('14,2010', 0o15262, '', '2DEC', '+.8342971408 B-1', 'STAR 37       X', kind='data', line=353)
W('14,2011', 0o21773, kind='data', line=353)
W('14,2012', 0o74130, '', '2DEC', '-.2392481515 B-1', 'STAR 37       Y', kind='data', line=354)
W('14,2013', 0o42420, kind='data', line=354)
W('14,2014', 0o70033, '', '2DEC', '-.4966976975 B-1', 'STAR 37       Z', kind='data', line=355)
W('14,2015', 0o41533, kind='data', line=355)

W('14,2016', 0o15014, '', '2DEC', '+.8139832631 B-1', 'STAR 36       X', kind='data', line=357)
W('14,2017', 0o04650, kind='data', line=357)
W('14,2020', 0o67067, '', '2DEC', '-.5557243189 B-1', 'STAR 36       Y', kind='data', line=358)
W('14,2021', 0o60150, kind='data', line=358)
W('14,2022', 0o02551, '', '2DEC', '+.1691204557 B-1', 'STAR 36       Z', kind='data', line=359)
W('14,2023', 0o15723, kind='data', line=359)

W('14,2024', 0o07210, '', '2DEC', '+.4541086270 B-1', 'STAR 35       X', kind='data', line=361)
W('14,2025', 0o01664, kind='data', line=361)
W('14,2026', 0o67276, '', '2DEC', '-.5392368197 B-1', 'STAR 35       Y', kind='data', line=362)
W('14,2027', 0o62232, kind='data', line=362)
W('14,2030', 0o13262, '', '2DEC', '+.7092312789 B-1', 'STAR 35       Z', kind='data', line=363)
W('14,2031', 0o00563, kind='data', line=363)

W('14,2032', 0o05076, '', '2DEC', '+.3201817378 B-1', 'STAR 34       X', kind='data', line=365)
W('14,2033', 0o35561, kind='data', line=365)
W('14,2034', 0o70716, '', '2DEC', '-.4436021946 B-1', 'STAR 34       Y', kind='data', line=366)
W('14,2035', 0o40260, kind='data', line=366)
W('14,2036', 0o62466, '', '2DEC', '-.8370786986 B-1', 'STAR 34       Z', kind='data', line=367)
W('14,2037', 0o64656, kind='data', line=367)

W('14,2040', 0o10652, '', '2DEC', '+.5520184464 B-1', 'STAR 33       X', kind='data', line=369)
W('14,2041', 0o04246, kind='data', line=369)
W('14,2042', 0o63235, '', '2DEC', '-.7933187400 B-1', 'STAR 33       Y', kind='data', line=370)
W('14,2043', 0o44200, kind='data', line=370)
W('14,2044', 0o73710, '', '2DEC', '-.2567508745 B-1', 'STAR 33       Z', kind='data', line=371)
W('14,2045', 0o66230, kind='data', line=371)

W('14,2046', 0o07204, '', '2DEC', '+.4537196908 B-1', 'STAR 32       X', kind='data', line=373)
W('14,2047', 0o33712, kind='data', line=373)
W('14,2050', 0o61747, '', '2DEC', '-.8779508801 B-1', 'STAR 32       Y', kind='data', line=374)
W('14,2051', 0o72343, kind='data', line=374)
W('14,2052', 0o02343, '', '2DEC', '+.1527766153 B-1', 'STAR 32       Z', kind='data', line=375)
W('14,2053', 0o21362, kind='data', line=375)

W('14,2054', 0o03237, '', '2DEC', '+.2069525789 B-1', 'STAR 31       X', kind='data', line=377)
W('14,2055', 0o13301, kind='data', line=377)
W('14,2056', 0o62030, '', '2DEC', '-.8719885748 B-1', 'STAR 31       Y', kind='data', line=378)
W('14,2057', 0o65332, kind='data', line=378)
W('14,2060', 0o70715, '', '2DEC', '-.4436288486 B-1', 'STAR 31       Z', kind='data', line=379)
W('14,2061', 0o71267, kind='data', line=379)

W('14,2062', 0o01745, '', '2DEC', '+.1217293692 B-1', 'STAR 30       X', kind='data', line=381)
W('14,2063', 0o06477, kind='data', line=381)
W('14,2064', 0o63531, '', '2DEC', '-.7702732847 B-1', 'STAR 30       Y', kind='data', line=382)
W('14,2065', 0o75365, kind='data', line=382)
# Page 48
W('14,2066', 0o12010, '', '2DEC', '+.6259880410 B-1', 'STAR 30       Z', kind='data', line=384)
W('14,2067', 0o03005, kind='data', line=384)

W('14,2070', 0o76146, '', '2DEC', '-.1124304773 B-1', 'STAR 29       X', kind='data', line=386)
W('14,2071', 0o77014, kind='data', line=386)
W('14,2072', 0o60371, '', '2DEC', '-.9694934200 B-1', 'STAR 29       Y', kind='data', line=387)
W('14,2073', 0o75073, kind='data', line=387)
W('14,2074', 0o03370, '', '2DEC', '+.2178116072 B-1', 'STAR 29       Z', kind='data', line=388)
W('14,2075', 0o12003, kind='data', line=388)

W('14,2076', 0o76125, '', '2DEC', '-.1146237858 B-1', 'STAR 28       X', kind='data', line=390)
W('14,2077', 0o40037, kind='data', line=390)
W('14,2100', 0o72436, '', '2DEC', '-.3399692557 B-1', 'STAR 28       Y', kind='data', line=391)
W('14,2101', 0o77062, kind='data', line=391)
W('14,2102', 0o61041, '', '2DEC', '-.9334250333 B-1', 'STAR 28       Z', kind='data', line=392)
W('14,2103', 0o54164, kind='data', line=392)

W('14,2104', 0o72277, '', '2DEC', '-.3516499609 B-1', 'STAR 27       X', kind='data', line=394)
W('14,2105', 0o51044, kind='data', line=394)
W('14,2106', 0o62641, '', '2DEC', '-.8240752703 B-1', 'STAR 27       Y', kind='data', line=395)
W('14,2107', 0o45471, kind='data', line=395)
W('14,2110', 0o70711, '', '2DEC', '-.4441196390 B-1', 'STAR 27       Z', kind='data', line=396)
W('14,2111', 0o70546, kind='data', line=396)

W('14,2112', 0o67364, '', '2DEC', '-.5326876930 B-1', 'STAR 26       X', kind='data', line=398)
W('14,2113', 0o47073, kind='data', line=398)
W('14,2114', 0o64425, '', '2DEC', '-.7160644554 B-1', 'STAR 26       Y', kind='data', line=399)
W('14,2115', 0o77777, kind='data', line=399)
W('14,2116', 0o07157, '', '2DEC', '+.4511047742 B-1', 'STAR 26       Z', kind='data', line=400)
W('14,2117', 0o16322, kind='data', line=400)

W('14,2120', 0o63327, '', '2DEC', '-.7861763936 B-1', 'STAR 25       X', kind='data', line=402)
W('14,2121', 0o64446, kind='data', line=402)
W('14,2122', 0o67515, '', '2DEC', '-.5217996305 B-1', 'STAR 25       Y', kind='data', line=403)
W('14,2123', 0o55266, kind='data', line=403)
W('14,2124', 0o05230, '', '2DEC', '+.3311371675 B-1', 'STAR 25       Z', kind='data', line=404)
W('14,2125', 0o25476, kind='data', line=404)

W('14,2126', 0o64754, '', '2DEC', '-.6898393233 B-1', 'STAR 24       X', kind='data', line=406)
W('14,2127', 0o72604, kind='data', line=406)
W('14,2130', 0o71235, '', '2DEC', '-.4182330640 B-1', 'STAR 24       Y', kind='data', line=407)
W('14,2131', 0o72553, kind='data', line=407)
W('14,2132', 0o66427, '', '2DEC', '-.5909338474 B-1', 'STAR 24       Z', kind='data', line=408)
W('14,2133', 0o42171, kind='data', line=408)

W('14,2134', 0o66546, '', '2DEC', '-.5812035376 B-1', 'STAR 23       X', kind='data', line=410)
W('14,2135', 0o70765, kind='data', line=410)
W('14,2136', 0o73260, '', '2DEC', '-.2909171294 B-1', 'STAR 23       Y', kind='data', line=411)
W('14,2137', 0o71643, kind='data', line=411)
W('14,2140', 0o14121, '', '2DEC', '+.7599800468 B-1', 'STAR 23       Z', kind='data', line=412)
W('14,2141', 0o30153, kind='data', line=412)

W('14,2142', 0o61247, '', '2DEC', '-.9170097662 B-1', 'STAR 22       X', kind='data', line=414)
W('14,2143', 0o73310, kind='data', line=414)
W('14,2144', 0o72313, '', '2DEC', '-.3502146628 B-1', 'STAR 22       Y', kind='data', line=415)
W('14,2145', 0o41247, kind='data', line=415)
W('14,2146', 0o74744, '', '2DEC', '-.1908999176 B-1', 'STAR 22       Z', kind='data', line=416)
W('14,2147', 0o44566, kind='data', line=416)

# Page 49
W('14,2150', 0o70606, '', '2DEC', '-.4523440203 B-1', 'STAR 21       X', kind='data', line=419)
W('14,2151', 0o54564, kind='data', line=419)
W('14,2152', 0o77153, '', '2DEC', '-.0493710140 B-1', 'STAR 21       Y', kind='data', line=420)
W('14,2153', 0o61536, kind='data', line=420)
W('14,2154', 0o61601, '', '2DEC', '-.8904759346 B-1', 'STAR 21       Z', kind='data', line=421)
W('14,2155', 0o47046, kind='data', line=421)

W('14,2156', 0o60604, '', '2DEC', '-.9525211695 B-1', 'STAR 20       X', kind='data', line=423)
W('14,2157', 0o76224, kind='data', line=423)
W('14,2160', 0o77031, '', '2DEC', '-.0593434796 B-1', 'STAR 20       Y', kind='data', line=424)
W('14,2161', 0o73354, kind='data', line=424)
W('14,2162', 0o73161, '', '2DEC', '-.2986331746 B-1', 'STAR 20       Z', kind='data', line=425)
W('14,2163', 0o63065, kind='data', line=425)

W('14,2164', 0o60431, '', '2DEC', '-.9656605484 B-1', 'STAR 19       X', kind='data', line=427)
W('14,2165', 0o51702, kind='data', line=427)
W('14,2166', 0o00656, '', '2DEC', '+.0525933156 B-1', 'STAR 19       Y', kind='data', line=428)
W('14,2167', 0o33013, kind='data', line=428)
W('14,2170', 0o04044, '', '2DEC', '+.2544280809 B-1', 'STAR 19       Z', kind='data', line=429)
W('14,2171', 0o10627, kind='data', line=429)

W('14,2172', 0o62164, '', '2DEC', '-.8608205219 B-1', 'STAR 18       X', kind='data', line=431)
W('14,2173', 0o45040, kind='data', line=431)
W('14,2174', 0o07325, '', '2DEC', '+.4636213989 B-1', 'STAR 18       Y', kind='data', line=432)
W('14,2175', 0o37443, kind='data', line=432)
W('14,2176', 0o03267, '', '2DEC', '+.2098647835 B-1', 'STAR 18       Z', kind='data', line=433)
W('14,2177', 0o06626, kind='data', line=433)

W('14,2200', 0o63471, '', '2DEC', '-.7742591356 B-1', 'STAR 17       X', kind='data', line=435)
W('14,2201', 0o50471, kind='data', line=435)
W('14,2202', 0o11660, '', '2DEC', '+.6152504197 B-1', 'STAR 17       Y', kind='data', line=436)
W('14,2203', 0o04151, kind='data', line=436)
W('14,2204', 0o75501, '', '2DEC', '-.1482892839 B-1', 'STAR 17       Z', kind='data', line=437)
W('14,2205', 0o46664, kind='data', line=437)

W('14,2206', 0o70430, '', '2DEC', '-.4657947941 B-1', 'STAR 16       X', kind='data', line=439)
W('14,2207', 0o46540, kind='data', line=439)
W('14,2210', 0o07507, '', '2DEC', '+.4774785033 B-1', 'STAR 16       Y', kind='data', line=440)
W('14,2211', 0o20100, kind='data', line=440)
W('14,2212', 0o13727, '', '2DEC', '+.7450164351 B-1', 'STAR 16       Z', kind='data', line=441)
W('14,2213', 0o05455, kind='data', line=441)

W('14,2214', 0o72160, '', '2DEC', '-.3612508532 B-1', 'STAR 15       X', kind='data', line=443)
W('14,2215', 0o64202, kind='data', line=443)
W('14,2216', 0o11144, '', '2DEC', '+.5747270840 B-1', 'STAR 15       Y', kind='data', line=444)
W('14,2217', 0o05203, kind='data', line=444)
W('14,2220', 0o64200, '', '2DEC', '-.7342932655 B-1', 'STAR 15       Z', kind='data', line=445)
W('14,2221', 0o65331, kind='data', line=445)

W('14,2222', 0o71322, '', '2DEC', '-.4118589524 B-1', 'STAR 14       X', kind='data', line=447)
W('14,2223', 0o41512, kind='data', line=447)
W('14,2224', 0o16402, '', '2DEC', '+.9065485360 B-1', 'STAR 14       Y', kind='data', line=448)
W('14,2225', 0o16205, kind='data', line=448)
W('14,2226', 0o01365, '', '2DEC', '+.0924226975 B-1', 'STAR 14       Z', kind='data', line=449)
W('14,2227', 0o04034, kind='data', line=449)

W('14,2230', 0o75054, '', '2DEC', '-.1820751783 B-1', 'STAR 13       X', kind='data', line=451)
W('14,2231', 0o56052, kind='data', line=451)
# Page 50
W('14,2232', 0o17030, '', '2DEC', '+.9404899869 B-1', 'STAR 13       Y', kind='data', line=453)
W('14,2233', 0o17635, kind='data', line=453)
W('14,2234', 0o73321, '', '2DEC', '-.2869271926 B-1', 'STAR 13       Z', kind='data', line=454)
W('14,2235', 0o57603, kind='data', line=454)

W('14,2236', 0o77010, '', '2DEC', '-.0614937230 B-1', 'STAR 12       X', kind='data', line=456)
W('14,2237', 0o47623, kind='data', line=456)
W('14,2240', 0o11515, '', '2DEC', '+.6031563286 B-1', 'STAR 12       Y', kind='data', line=457)
W('14,2241', 0o01640, kind='data', line=457)
W('14,2242', 0o63215, '', '2DEC', '-.7952489957 B-1', 'STAR 12       Z', kind='data', line=458)
W('14,2243', 0o52176, kind='data', line=458)

W('14,2244', 0o02143, '', '2DEC', '+.1371725575 B-1', 'STAR 11       X', kind='data', line=460)
W('14,2245', 0o26755, kind='data', line=460)
W('14,2246', 0o12715, '', '2DEC', '+.6813721061 B-1', 'STAR 11       Y', kind='data', line=461)
W('14,2247', 0o31470, kind='data', line=461)
W('14,2250', 0o13401, '', '2DEC', '+.7189685267 B-1', 'STAR 11       Z', kind='data', line=462)
W('14,2251', 0o31222, kind='data', line=462)

W('14,2252', 0o03157, '', '2DEC', '+.2011399589 B-1', 'STAR 10       X', kind='data', line=464)
W('14,2253', 0o27504, kind='data', line=464)
W('14,2254', 0o17402, '', '2DEC', '+.9690337941 B-1', 'STAR 10       Y', kind='data', line=465)
W('14,2255', 0o12312, kind='data', line=465)
W('14,2256', 0o75552, '', '2DEC', '-.1432348512 B-1', 'STAR 10       Z', kind='data', line=466)
W('14,2257', 0o63657, kind='data', line=466)

W('14,2260', 0o05471, '', '2DEC', '+.3507315038 B-1', 'STAR 9        X', kind='data', line=468)
W('14,2261', 0o06122, kind='data', line=468)
W('14,2262', 0o16220, '', '2DEC', '+.8926333307 B-1', 'STAR 9        Y', kind='data', line=469)
W('14,2263', 0o16362, kind='data', line=469)
W('14,2264', 0o04417, '', '2DEC', '+.2831839492 B-1', 'STAR 9        Z', kind='data', line=470)
W('14,2265', 0o32762, kind='data', line=470)

W('14,2266', 0o06443, '', '2DEC', '+.4105636020 B-1', 'STAR 8        X', kind='data', line=472)
W('14,2267', 0o12622, kind='data', line=472)
W('14,2270', 0o07766, '', '2DEC', '+.4988110001 B-1', 'STAR 8        Y', kind='data', line=473)
W('14,2271', 0o10237, kind='data', line=473)
W('14,2272', 0o14154, '', '2DEC', '+.7632988371 B-1', 'STAR 8        Z', kind='data', line=474)
W('14,2273', 0o36154, kind='data', line=474)

W('14,2274', 0o13200, '', '2DEC', '+.7032235469 B-1', 'STAR 7        X', kind='data', line=476)
W('14,2275', 0o31653, kind='data', line=476)
W('14,2276', 0o13244, '', '2DEC', '+.7075846047 B-1', 'STAR 7        Y', kind='data', line=477)
W('14,2277', 0o21036, kind='data', line=477)
W('14,2300', 0o01067, '', '2DEC', '+.0692868685 B-1', 'STAR 7        Z', kind='data', line=478)
W('14,2301', 0o23106, kind='data', line=478)

W('14,2302', 0o10560, '', '2DEC', '+.5450107404 B-1', 'STAR 6        X', kind='data', line=480)
W('14,2303', 0o27227, kind='data', line=480)
W('14,2304', 0o10402, '', '2DEC', '+.5314955466 B-1', 'STAR 6        Y', kind='data', line=481)
W('14,2305', 0o00275, kind='data', line=481)
W('14,2306', 0o65477, '', '2DEC', '-.6484410356 B-1', 'STAR 6        Z', kind='data', line=482)
W('14,2307', 0o77044, kind='data', line=482)

W('14,2310', 0o00153, '', '2DEC', '+.0130968840 B-1', 'STAR 5        X', kind='data', line=484)
W('14,2311', 0o11212, kind='data', line=484)
W('14,2312', 0o00077, '', '2DEC', '+.0078062795 B-1', 'STAR 5        Y', kind='data', line=485)
W('14,2313', 0o36275, kind='data', line=485)
# Page 51
W('14,2314', 0o17777, '', '2DEC', '+.9998837600 B-1', 'STAR 5        Z', kind='data', line=487)
W('14,2315', 0o01417, kind='data', line=487)

W('14,2316', 0o07674, '', '2DEC', '+.4917678276 B-1', 'STAR 4        X', kind='data', line=489)
W('14,2317', 0o21771, kind='data', line=489)
W('14,2320', 0o03416, '', '2DEC', '+.2204887125 B-1', 'STAR 4        Y', kind='data', line=490)
W('14,2321', 0o07626, kind='data', line=490)
W('14,2322', 0o62413, '', '2DEC', '-.8423473935 B-1', 'STAR 4        Z', kind='data', line=491)
W('14,2323', 0o57536, kind='data', line=491)

W('14,2324', 0o07510, '', '2DEC', '+.4775639450 B-1', 'STAR 3        X', kind='data', line=493)
W('14,2325', 0o06414, kind='data', line=493)
W('14,2326', 0o01673, '', '2DEC', '+.1166004340 B-1', 'STAR 3        Y', kind='data', line=494)
W('14,2327', 0o06065, kind='data', line=494)
W('14,2330', 0o15735, '', '2DEC', '+.8708254803 B-1', 'STAR 3        Z', kind='data', line=495)
W('14,2331', 0o31531, kind='data', line=495)

W('14,2332', 0o16745, '', '2DEC', '+.9342640400 B-1', 'STAR 2        X', kind='data', line=497)
W('14,2333', 0o17555, kind='data', line=497)
W('14,2334', 0o02615, '', '2DEC', '+.1735073142 B-1', 'STAR 2        Y', kind='data', line=498)
W('14,2335', 0o13716, kind='data', line=498)
W('14,2336', 0o73010, '', '2DEC', '-.3115219339 B-1', 'STAR 2        Z', kind='data', line=499)
W('14,2337', 0o40311, kind='data', line=499)

W('14,2340', 0o15776, '', '2DEC', '+.8748658918 B-1', 'STAR 1        X', kind='data', line=501)
W('14,2341', 0o34660, kind='data', line=501)
W('14,2342', 0o00325, '', '2DEC', '+.0260879174 B-1', 'STAR 1        Y', kind='data', line=502)
W('14,2343', 0o26625, kind='data', line=502)
W('14,2344', 0o07572, '', '2DEC', '+.4836621670 B-1', 'STAR 1        Z', kind='data', line=503)
W('14,2345', 0o05105, kind='data', line=503)

W('14,2346', 0o15472, 'CATLOG', 'DEC', '6970', kind='data', line=505)

# *******************************************************************************

#   SETLOC EPHEM1
#   BANK
#   COUNT* $$/EPHEM

W('05,2001', 0o20000, 'KONMAT', '2DEC', '1.0 B-1', '********************', kind='data', line=513)
W('05,2002', 0o00000, kind='data', line=513)
W('05,2003', 0o00000, '', '2DEC', '0', '                   *', kind='data', line=514)
W('05,2004', 0o00000, kind='data', line=514)
W('05,2005', 0o00000, '', '2DEC', '0', '                   *', kind='data', line=515)
W('05,2006', 0o00000, kind='data', line=515)
W('05,2007', 0o00000, '', '2DEC', '0', '                   *', kind='data', line=516)
W('05,2010', 0o00000, kind='data', line=516)
W('05,2011', 0o16533, '', '2DEC', '.91745 B-1', 'K1 COS(OBL)        *', kind='data', line=517)
W('05,2012', 0o30007, kind='data', line=517)
W('05,2013', 0o77333, '', '2DEC', '-.03571 B-1', 'K2 SIN(OBL)SIN(IM) *', kind='data', line=518)
W('05,2014', 0o56654, kind='data', line=518)
W('05,2015', 0o00000, '', '2DEC', '0', '                   *', kind='data', line=519)
W('05,2016', 0o00000, kind='data', line=519)
W('05,2017', 0o06273, '', '2DEC', '.39784 B-1', 'K3 SIN(OBL)        *', kind='data', line=520)
W('05,2020', 0o03275, kind='data', line=520)
# Page 52
W('05,2021', 0o01242, '', '2DEC', '.082354 B-1', 'K4 COS(OBL)SIN(IM) *', kind='data', line=522)
W('05,2022', 0o24467, kind='data', line=522)
W('05,2023', 0o00020, 'CSTODAY', '2DEC', '8640000 B-33', '                   * NOTE:          *', kind='data', line=523)
W('05,2024', 0o17260, kind='data', line=523)
W('05,2025', 0o00002, 'RCB-13', 'OCT', '00002', '                   * TABLES CONTAIN *', kind='data', line=524)
W('05,2026', 0o00000, '', 'OCT', '00000', '                   * CONSTANTS FOR  *', kind='data', line=525)
W('05,2027', 0o22572, 'RATESP', '2DEC', '.03660098 B+4', 'LOMR               * 1969 - 1970    *', kind='data', line=526)
W('05,2030', 0o27214, kind='data', line=526)
W('05,2031', 0o01315, '', '2DEC', '.00273779 B+4', 'LOSR', kind='data', line=527)
W('05,2032', 0o26177, kind='data', line=527)
W('05,2033', 0o77731, '', '2DEC', '-.00014719 B+4', 'LONR', kind='data', line=528)
W('05,2034', 0o55217, kind='data', line=528)
W('05,2035', 0o32055, '', '2DEC', '.815282336', 'LOMO', kind='data', line=529)
W('05,2036', 0o22576, kind='data', line=529)
W('05,2037', 0o10624, '', '2DEC', '.274674910', 'LOSO', kind='data', line=530)
W('05,2040', 0o10605, kind='data', line=530)
W('05,2041', 0o37436, '', '2DEC', '.986209499', 'LONO', kind='data', line=531)
W('05,2042', 0o01635, kind='data', line=531)
W('05,2043', 0o01065, 'VAL67', '2DEC*', '.01726666666 B+1*', 'AMOD', kind='data', line=532)
W('05,2044', 0o31323, kind='data', line=532)
W('05,2045', 0o20770, '', '2DEC', '.530784445', 'AARG', kind='data', line=533)
W('05,2046', 0o13725, kind='data', line=533)
W('05,2047', 0o02245, '', '2DEC', '.036291712 B+1', '1/27', kind='data', line=534)
W('05,2050', 0o06475, kind='data', line=534)
W('05,2051', 0o00162, '', '2DEC', '.003505277 B+1', 'BMOD', kind='data', line=535)
W('05,2052', 0o33431, kind='data', line=535)
W('05,2053', 0o22566, '', '2DEC', '.585365625', 'BARG', kind='data', line=536)
W('05,2054', 0o24130, kind='data', line=536)
W('05,2055', 0o02000, '', '2DEC', '.03125 B+1', '1/32', kind='data', line=537)
W('05,2056', 0o00000, kind='data', line=537)
W('05,2057', 0o00256, '', '2DEC', '.005325277 B+1', 'CMOD', kind='data', line=538)
W('05,2060', 0o17752, kind='data', line=538)
W('05,2061', 0o77512, '', '2DEC', '-.01106341036', 'CARG', kind='data', line=539)
W('05,2062', 0o67453, kind='data', line=539)
W('05,2063', 0o00131, '', '2DEC', '.002737925 B+1', '1/365', kind='data', line=540)
W('05,2064', 0o26730, kind='data', line=540)

# ********************************************************************************

#   SETLOC PLANTIN2
#   BANK
#   COUNT* $$/LUROT

W('26,2000', 0o17775, 'COSI', '2DEC', '.99964173 B-1', 'COS (5521.5 SEC.) B-1', kind='data', line=548)
W('26,2001', 0o02052, kind='data', line=548)
W('26,2002', 0o00333, 'SINI', '2DEC', '.02676579 B-1', 'SIN (5521.5 SEC.) B-1', kind='data', line=549)
W('26,2003', 0o10374, kind='data', line=549)
W('26,2004', 0o77665, 'NODDOT', '2DEC', '-.457335121 E-2', 'REV/CSEC B+28 = -1.07047011 E-8 RAD/SEC', kind='data', line=550)
W('26,2005', 0o42175, kind='data', line=550)
W('26,2006', 0o22211, 'FDOT', '2DEC', '.570863327', 'REV/CSEC B+27 =  2.67240410 E-6 RAD/SEC', kind='data', line=551)
W('26,2007', 0o00625, kind='data', line=551)
# Page 53
W('26,2010', 0o77777, 'BDOT', '2DEC', '-3.07500686 E-8', 'REV/CSEC B+28 = -7.19757301 E-14 RAD/SEC', kind='data', line=553)
W('26,2011', 0o77767, kind='data', line=553)
W('26,2012', 0o37436, 'NODIO', '2DEC', '.986209434', 'REVS B-D      = 6.19653663041 RAD', kind='data', line=554)
W('26,2013', 0o01613, kind='data', line=554)
W('26,2014', 0o32417, 'FSUBO', '2DEC', '.829090536', 'REVS B-D      = 5.20932947829 RAD', kind='data', line=555)
W('26,2015', 0o32160, kind='data', line=555)
W('26,2016', 0o02052, 'BSUBO', '2DEC', '.0651201393', 'REVS B-D      = 0.40916190299 RAD', kind='data', line=556)
W('26,2017', 0o35552, kind='data', line=556)
W('26,2020', 0o37116, 'WEARTH', '2DEC', '.973561595', 'REV/CSEC B+23 = 7.29211494 E-5 RAD/SEC', kind='data', line=557)
W('26,2021', 0o32523, kind='data', line=557)
