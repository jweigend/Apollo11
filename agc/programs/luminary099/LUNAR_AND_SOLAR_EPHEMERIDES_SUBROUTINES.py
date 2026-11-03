"""LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 984-987 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES', 'LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES.agc', 'Luminary099', pages='984-987')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        984-987
# Mod history:  2009-05-24 HG   Transcribed from page images.
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

# Page 984
# NAME - LSPOS  - LOCATE SUN AND MOON                   DATE - 25 OCT 67
# MOD NO.1
# MOD BY NEVILLE                                        ASSEMBLY SUNDANCE
#
# FUNCTIONAL DESCRIPTION
#
# COMPUTES UNIT POSITION VECTOR OF THE SUN AND MOON IN THE BASIC REFERENCE SYSTEM. THE SUN VECTOR S IS
# LOCATED VIA TWO ANGLES. THE FIRST ANGLE(OBLIQUITY) IS THE ANGLE BETWEEN THE EARTH EQUATOR AND THE ECLIPTIC. THE
# SECOND ANGLE IS THE LONGITUDE OF THE SUN MEASURED IN THE ECLIPTIC.
# THE POSITION VECTOR OF THE SUN IS
# -
# S=(COS(LOS), COS(OBL)*SIN(LOS), SIN(OBL)*SIN(LOS)), WHERE
#
# LOS=LOS +LOS *T-(C *SIN(2PI*T)/365.24 +C *COS(2PI*T)/365.24)
# 0    R     0                     1
# LOS  (RAD) IS THE LONGITUDE OF THE SUN FOR MIGNIGHT JUNE 30TH OF THE PARTICULAR YEAR.
# 0
# LOS  (RAD/DAY) IS THE MEAN RATE FOR THE PARTICULAR YEAR.
# R
# LOS  AND LOS  ARE STORED AS LOSO AND LOSR IN RATESP.
# 0        R
# COS(OBL) AND SIN(OBL) ARE STORED IN THE MATRIX KONMAT.
# T, TIME MEASURED IN DAYS(24 HOURS), IS STORED IN TIMEP.
# C  AND C  ARE FUDGE FACTORS TO MINIMIZE THE DEVIATION. THEY ARE STORED AS ONE CONSTANT(CMOD), SINCE
# 0      1                               2  2 1/2
# C *SIN(X)+C *COS(X) CAN BE WRITTEN AS (C +C )   *SIN(X+PHI), WHERE PHI=ARCTAN(C /C ).
# 0         1                            0  1                                   1  0
#
# THE MOON IS LOCATED VIA FOUR ANGLES. THE FIRST IS THE OBLIQUITY. THE SECOND IS THE MEAN LONGITUDE OF THE MOON,
# MEASURED IN THE ECLIPTIC FROM THE MEAN EQUINOX TO THE MEAN ASCENDING NODE OF THE LUNAR ORBIT, AND THEN ALONG THE
# ORBIT. THE THIRD ANGLE IS THE ANGLE BETWEEN THE ECLIPTIC AND THE LUNAR ORBIT. THE FOURTH ANGLE IS THE LONGITUDE
# OF THE NODE OF THE MOON, MEASURED IN THE LUNAR ORBIT. LET THESE ANGLES BE OBL,LOM,IM, AND LON RESPECTIVELY.
#
# THE SIMPLIFIED POSITION VECTOR OF THE MOON IS
# -
# M=(COS(LOM), COS(OBL)*SIN(LOM)-SIN(OBL)*SIN(IM)*SIN(LOM-LON), SIN(OBL)*SIN(LOM)+COS(OBL)*SIN(IM)*SIN(LOM-LON))
#
# WHERE
# LOM=LOM +LOM *T-(A *SIN(2PI*T/27.5545)+A *COS(2PI*T/27.5545)+B *SIN(2PI*T/32)+B *COS(2PI*T/32)), AND
# 0    R     0                     1                     0                1
# LON=LON +LON
# 0    R
# A , A , B  AND B  ARE STORED AS AMOD AND BMOD (SEE DESCRIPTION OF CMOD, ABOVE).  COS(OBL), SIN(OBL)*SIN(IM),
# 0   1   0      1
# SIN(OBL), AND COS(OBL)*SIN(IM) ARE STORED IN KONMAT AS K1, K2, K3 AND K4, RESPECTIVELY. LOM , LOM , LON , LON
# ARE STORED AS LOMO, LOMR, LONO, AND LONR IN RATESP.                                        0     R     0     R
# THE THREE PHIS ARE STORED AS AARG, BARG, AND CARG(SUN).  ALL CONSTANTS ARE UPDATED BY YEAR.
#
# CALLING SEQUENCE
# Page 985
# CALL LSPOS.  RETURN IS VIA QPRET.
# ALARMS OR ABORTS
# NONE
# ERASABLE INITIALIZATION REQUIRED
# TEPHEM - TIME FROM MIGNIGHT 1 JULY PRECEDING THE LAUNCH TO THE TIME OF THE LAUNCH (WHEN THE AGC CLOCK WENT
# TO ZERO). TEPHEM IS TP WITH UNITS OF CENTI-SECONDS.
# TIME2 AND TIME1 ARE IN MPAC AND MPAC +1 WHEN PROGRAM IS CALLED.
# OUTPUT
# UNIT POSITIONAL VECTOR OF SUN IN VSUN.   (SCALED B-1)
# UNIT POSITIONAL VECTOR OF MOON IN VMOON. (SCALED B-1)
# SUBROUTINES USED
# NONE
# DEBRIS
# CURRENT CORE SET,WORK AREA AND FREEFLAG
#   BANK 04
#   SETLOC EPHEM
#   BANK
#   EBANK= VSUN
#   COUNT* $$/EPHEM
S('LUNPOS', 'equals', 0o43664, line=97)
W('15,3664', 0o54201, 'LSPOS', 'SETPD', 'SR', kind='interp', line=98)
W('15,3665', 0o00001, '', '', '0', kind='operand', line=99)
W('15,3666', 0o20617, '', '', '14D', 'TP', kind='operand', line=100)
W('15,3667', 0o56371, '', 'TAD', 'DDV', kind='interp', line=101)
# Comments in [...] are hand-written notations in original listing
W('15,3670', 0o01707, '', '', 'TEPHEM', 'TIME OF LAUNCH [in centisec B 42]', kind='operand', line=103)
W('15,3671', 0o12024, '', '', 'CSTODAY', '24 HOURS-8640000 CENTI-SECS/DAY B-33', kind='operand', line=104)
W('15,3672', 0o00031, '', 'STORE', 'TIMEP', 'T IN DAYS [@ B 9 = 512 days]', kind='interp', line=105)
W('15,3673', 0o77170, '', 'AXT,1', 'AXT,2', '          [∴ granularity ≈ 0.164 sec]', kind='interp', line=106)
W('15,3674', 0o00000, '', '', '0', kind='operand', line=107)
W('15,3675', 0o00000, '', '', '0', kind='operand', line=108)
W('15,3676', 0o77614, '', 'CLEAR', kind='interp', line=109)
W('15,3677', 0o00274, '', '', 'FREEFLAG', 'SWITCH BIT', kind='operand', line=110)
W('15,3700', 0o77745, 'POSITA', 'DLOAD', kind='interp', line=111)
W('15,3701', 0o12004, '', '', 'KONMAT +2', 'ZERO$', kind='operand', line=112)
W('15,3702', 0o00027, '', 'STORE', 'GTMP', kind='interp', line=113)
W('15,3703', 0o40745, 'POSITB', 'DLOAD', 'DMP*', kind='interp', line=114)
W('15,3704', 0o00031, '', '', 'TIMEP', 'T', kind='operand', line=115)
W('15,3705', 0o12050, '', '', 'VAL67 +4,1', '1/27 OR 1/32 OR 1/365', kind='operand', line=116)
# Page 986
W('15,3706', 0o42661, '', 'SL', 'DAD*', kind='interp', line=118)
W('15,3707', 0o20211, '', '', '8D', kind='operand', line=119)
W('15,3710', 0o12046, '', '', 'VAL67 +2,1', 'AARG', kind='operand', line=120)
W('15,3711', 0o40756, '', 'SIN', 'DMP*', 'SIN(T/27+PHI) OR T/32 OR T/365', kind='interp', line=121)
W('15,3712', 0o12044, '', '', 'VAL67,1', '(A0**2+A1**2)**1/2SIN(X+PHIA)', kind='operand', line=122)
W('15,3713', 0o62015, '', 'DAD', 'INCR,1', 'PLUS', kind='interp', line=123)
W('15,3714', 0o00027, '', '', 'GTMP', '(B0**2+B1**2)**1/2SIN(X+PHIB)', kind='operand', line=124)
W('15,3715', 0o77771, '', 'DEC', '-6', kind='data', line=125)
W('15,3716', 0o00027, '', 'STORE', 'GTMP', 'OR (C0**2+C1**2)**1/2SIN(X+PHIC)', kind='interp', line=126)
W('15,3717', 0o77614, '', 'BOFSET', kind='interp', line=127)
W('15,3720', 0o00054, '', '', 'FREEFLAG', kind='operand', line=128)
W('15,3721', 0o33703, '', '', 'POSITB', kind='operand', line=129)
W('15,3722', 0o40745, 'POSITD', 'DLOAD', 'DMP*', kind='interp', line=130)
W('15,3723', 0o00031, '', '', 'TIMEP', 'T', kind='operand', line=131)
W('15,3724', 0o65747, '', '', 'RATESP,2', 'LOMR,LOSR,LONR', kind='operand', line=132)
W('15,3725', 0o42661, '', 'SL', 'DAD*', kind='interp', line=133)
W('15,3726', 0o20206, '', '', '5D', kind='operand', line=134)
W('15,3727', 0o65741, '', '', 'RATESP +6,2', 'LOMO,LOSO,LONO', kind='operand', line=135)
W('15,3730', 0o77625, '', 'DSU', kind='interp', line=136)
W('15,3731', 0o00027, '', '', 'GTMP', kind='operand', line=137)
W('15,3732', 0o10021, '', 'STORE', 'STMP,2', 'LOM,LOS,LON', kind='interp', line=138)
W('15,3733', 0o63135, '', 'SLOAD', 'INCR,2', kind='interp', line=139)
W('15,3734', 0o00050, '', '', 'X2', kind='operand', line=140)
W('15,3735', 0o77775, '', 'DEC', '-2', kind='data', line=141)
W('15,3736', 0o53015, '', 'DAD', 'BZE', kind='interp', line=142)
W('15,3737', 0o12026, '', '', 'RCB-13', 'PLUS 2', kind='operand', line=143)
W('15,3740', 0o33770, '', '', 'POSITE', '2ND', kind='operand', line=144)
W('15,3741', 0o77644, '', 'BPL', kind='interp', line=145)
W('15,3742', 0o33700, '', '', 'POSITA', '1ST', kind='operand', line=146)
W('15,3743', 0o45345, 'POSITF', 'DLOAD', 'DSU', '3RD', kind='interp', line=147)
W('15,3744', 0o00021, '', '', 'STMP', 'LOM', kind='operand', line=148)
W('15,3745', 0o00025, '', '', 'STMP +4', 'LON', kind='operand', line=149)
W('15,3746', 0o65356, '', 'SIN', 'PDDL', 'SIN(LOM-LON)', kind='interp', line=150)
W('15,3747', 0o00021, '', '', 'STMP', kind='operand', line=151)
W('15,3750', 0o65356, '', 'SIN', 'PDDL', 'SIN LOM', kind='interp', line=152)
W('15,3751', 0o00021, '', '', 'STMP', kind='operand', line=153)
W('15,3752', 0o55546, '', 'COS', 'VDEF', 'COS LOM', kind='interp', line=154)
W('15,3753', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=155)
W('15,3754', 0o12002, '', '', 'KONMAT', 'K1,K2,K3,K4,', kind='operand', line=156)
W('15,3755', 0o02723, '', 'STORE', 'VMOON', kind='interp', line=157)
W('15,3756', 0o65345, '', 'DLOAD', 'PDDL', kind='interp', line=158)
W('15,3757', 0o12004, '', '', 'KONMAT +2', 'ZERO', kind='operand', line=159)
W('15,3760', 0o00023, '', '', 'STMP +2', kind='operand', line=160)
W('15,3761', 0o65356, '', 'SIN', 'PDDL', 'SIN LOS', kind='interp', line=161)
W('15,3762', 0o00023, '', '', 'STMP +2', kind='operand', line=162)
W('15,3763', 0o55546, '', 'COS', 'VDEF', 'COS LOS', kind='interp', line=163)
W('15,3764', 0o53521, '', 'MXV', 'UNIT', kind='interp', line=164)
W('15,3765', 0o12002, '', '', 'KONMAT', kind='operand', line=165)
W('15,3766', 0o02715, '', 'STORE', 'VSUN', kind='interp', line=166)
W('15,3767', 0o77616, '', 'RVQ', kind='interp', line=167)
# Page 987
W('15,3770', 0o77745, 'POSITE', 'DLOAD', kind='interp', line=169)
W('15,3771', 0o12004, '', '', 'KONMAT +2', 'ZEROS', kind='operand', line=170)
W('15,3772', 0o00027, '', 'STORE', 'GTMP', kind='interp', line=171)
W('15,3773', 0o77650, '', 'GOTO', kind='interp', line=172)
W('15,3774', 0o33722, '', '', 'POSITD', kind='operand', line=173)
W('15,3775', 0o77616, 'LUNVEL', 'RVQ', '', '        TO FOOL INTEGRATION', kind='interp', line=174)
#   SETLOC EPHEM1
#   BANK

#   COUNT* $$/EPHEM
S('STMP', 'equals', 0o20, line=179)
S('GTMP', 'equals', 0o26, line=180)
S('TIMEP', 'equals', 0o30, line=181)

# *** END OF LEMP50S .115 ***
