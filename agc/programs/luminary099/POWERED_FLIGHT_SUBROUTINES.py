"""POWERED_FLIGHT_SUBROUTINES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1259-1267 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('POWERED_FLIGHT_SUBROUTINES', 'POWERED_FLIGHT_SUBROUTINES.agc', 'Luminary099', pages='1259-1267')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     POWERED_FLIGHT_SUBROUTINES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1259-1267
# Mod history:  2009-05-26 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2011-01-06 JL   Fixed pseudo-label indentation.
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

# Page 1259
#   BANK 14  # SAME FBANK AS THE FINDCDUD SUB-PROGRAM
#   SETLOC POWFLITE
#   BANK

#   EBANK= DEXDEX
#   COUNT* $$/POWFL

# CDUTRIG, CDUTRIG1, CDUTRIG2, AND CD*TR*GS ALL COMPUTE THE SINES AND
# COSINES OF THREE 2'S COMPLEMENT ANGLES AND PLACE THE RESULT, DOUBLE
# PRECISION, IN THE SAME ORDER AS THE INPUTS, AT SINCDU AND COSCDU.  AN
# ADDITIONAL OUTPUT IS THE 1'S COMPLEMENT ANGLES AT CDUSPOT.  THESE
# ROUTINES GO OUT OF THEIR WAY TO LEAVE THE MPAC AREA AS THEY FIND IT.
# EXCEPT FOR THE GENERALLY UNIMPORTANT MPAC +2.  THEY DIFFER ONLY IN
# WHERE THEY GET THE ANGLES, AND IN METHOD OF CALLING.
#
# CDUTRIG (AND CDUTRIG1, WHICH CAN BE CALLED IN BASIC) COMPUTE THE
# SINES AND COSINES FROM THE CURRENT CONTENTS OF THE CDU REGISTERS.
# THE CONTENTS OF CDUTEMP, ETC., ARE NOT TOUCHED SO THAT THEY MAY
# CONTINUE TO FORM A CONSISTENT SET WITH THE LATEST PIPA READINGS.
#
# CDUTRIG1 IS LIKE CDUTRIG EXCEPT THAT IT CAN BE CALLED IN BASIC.
#
# CD*TR*GS FINDS CDU VALUES IN CDUSPOT RATHER THAN IN CDUTEMP.  THIS
# ALLOWS USERS TO MAKE TRANSFORMATIONS USING ARBITRARY ANGLES, OR REAL
# ANGLES IN AN ORDER OTHER THAN X Y Z.  A CALL TO THIS ROUTINE IS
# NECESSARY IN PREPARATION FOR A CALL TO AX*SR*T IN EITHER OF ITS TWO
# MODES (SMNB OR NBSM).  SINCE AX*SR*T EXPECTS TO FIND THE SINES AND
# COSINES IN THE ORDER Y Z X THE ANGLES MUST HAVE BEEN PLACED IN CDUSPOT
# IN THIS ORDER.  CD*TR*GS NEED NOT BE REPEATED WHEN AX*SR*T IS CALLED
# MORE THAN ONCE, PROVIDED THE ANGLES HAVE NOT CHANGED.  NOTE THAT SINCE
# IT CLOBBERS BUF2 (IN THE SINE AND COSINE ROUTINES) CD*TR*GS CANNOT BE
# CALLED USING BANKCALL.  SORRY.
#
# CD*TR*G IS LIKE CD*TR*GS EXCEPT THAT IT CAN BE CALLED IN
# INTERPRETIVE.

W('23,3537', 0o77776, 'CDUTRIG', 'EXIT', kind='interp', line=67)
W('23,3540', 0o03547, '', 'TC', 'CDUTRIGS', line=68)
W('23,3541', 0o06037, '', 'TC', 'INTPRET', line=69)
W('23,3542', 0o77616, '', 'RVQ', kind='interp', line=70)

W('23,3543', 0o77776, 'CD*TR*G', 'EXIT', kind='interp', line=72)
W('23,3544', 0o03555, '', 'TC', 'CD*TR*GS', line=73)
W('23,3545', 0o06037, '', 'TC', 'INTPRET', line=74)
W('23,3546', 0o77616, '', 'RVQ', kind='interp', line=75)

W('23,3547', 0o30032, 'CDUTRIGS', 'CA', 'CDUX', line=77)
W('23,3550', 0o54772, '', 'TS', 'CDUSPOT +4', line=78)
W('23,3551', 0o30033, '', 'CA', 'CDUY', line=79)
W('23,3552', 0o54766, '', 'TS', 'CDUSPOT', line=80)
# Page 1260
W('23,3553', 0o30034, '', 'CA', 'CDUZ', line=82)
W('23,3554', 0o54770, '', 'TS', 'CDUSPOT +2', line=83)

W('23,3555', 0o00006, 'CD*TR*GS', 'EXTEND', line=85)
W('23,3556', 0o22142, '', 'QXCH', 'TEM2', line=86)
W('23,3557', 0o34751, '', 'CAF', 'FOUR', line=87)
W('23,3560', 0o76242, 'TR*GL**P', 'MASK', 'SIX', 'MAKE IT EVEN AND SMALLER', line=88)
W('23,3561', 0o54143, '', 'TS', 'TEM3', line=89)
W('23,3562', 0o50143, '', 'INDEX', 'TEM3', line=90)
W('23,3563', 0o30766, '', 'CA', 'CDUSPOT', line=91)
W('23,3564', 0o52155, '', 'DXCH', 'MPAC', "STORING 2'S COMP ANGLE, LOADING MPAC", line=92)
W('23,3565', 0o52127, '', 'DXCH', 'VBUF +4', 'STORING MPAC FOR LATER RESTORATION', line=93)
W('23,3566', 0o04713, '', 'TC', 'USPRCADR', line=94)
W('23,3567', 0o21576, '', 'CADR', 'CDULOGIC', kind='data', line=95)
W('23,3570', 0o00006, '', 'EXTEND', line=96)
W('23,3571', 0o30155, '', 'DCA', 'MPAC', line=97)
W('23,3572', 0o50143, '', 'INDEX', 'TEM3', line=98)
W('23,3573', 0o52767, '', 'DXCH', 'CDUSPOT', "STORING 1'S COMPLEMENT ANGLE", line=99)
W('23,3574', 0o04713, '', 'TC', 'USPRCADR', line=100)
W('23,3575', 0o01517, '', 'CADR', 'COSINE', kind='data', line=101)
W('23,3576', 0o52155, '', 'DXCH', 'MPAC', line=102)
W('23,3577', 0o50143, '', 'INDEX', 'TEM3', line=103)
W('23,3600', 0o52745, '', 'DXCH', 'COSCDU', 'STORING COSINE', line=104)
W('23,3601', 0o00006, '', 'EXTEND', line=105)
W('23,3602', 0o50143, '', 'INDEX', 'TEM3', line=106)
W('23,3603', 0o30767, '', 'DCA', 'CDUSPOT', "LOADING 1'S COMPLEMENT ANGLE", line=107)
W('23,3604', 0o04713, '', 'TC', 'USPRCADR', line=108)
W('23,3605', 0o01531, '', 'CADR', 'SINE +1', 'SINE +1 EXPECTS ARGUMENT IN A AND L', kind='data', line=109)
W('23,3606', 0o52127, '', 'DXCH', 'VBUF +4', 'BRINGING UP PRIOR MPAC TO BE RESTORED', line=110)
W('23,3607', 0o52155, '', 'DXCH', 'MPAC', line=111)
W('23,3610', 0o50143, '', 'INDEX', 'TEM3', line=112)
W('23,3611', 0o52737, '', 'DXCH', 'SINCDU', line=113)
W('23,3612', 0o10143, '', 'CCS', 'TEM3', line=114)
W('23,3613', 0o13560, '', 'TCF', 'TR*GL**P', line=115)
W('23,3614', 0o00142, '', 'TC', 'TEM2', line=116)
# Page 1261
# *******************************************************************************************************
# QUICTRIG, INTENDED FOR QUIDANCE CYCLE USE WHERE TIME IS CRITICAL, IS A MUCH FASTER VERSION OF CD*TR*GS.
# QUICTRIG COMPUTES AND STORES THE SINES AND COSINES OF THE 2'S COMPLEMENT ANGLES AT CDUSPOT, CDUSPOT +2,
# AND CDUSPOT +4.  UNLIKE CD*TR*GS, QUICTRIG DOES NOT LEAVE THE 1'S COMPLEMENT VERSIONS OF THE ANGLES IN
# CDUSPOT.  QUICTRIG'S EXECUTION TIME IS 4.1 MS;  THIS IS 10 TIMES AS FAST AS CD*TR*GS.  QUICTRIG MAY BE
# CALLED FROM INTERPRETIVE AS AN RTB OP-CODE, OR FROM BASIC VIA BANKCALL OR IBNKCALL.

W('23,3615', 0o00004, 'QUICTRIG', 'INHINT', '', 'INHINT SINCE DAP USES THE SAME TEMPS', line=125)
W('23,3616', 0o00006, '', 'EXTEND', line=126)
W('23,3617', 0o22061, '', 'QXCH', 'ITEMP1', line=127)
W('23,3620', 0o34751, '', 'CAF', 'FOUR', line=128)
W('23,3621', 0o76242, '', 'MASK', 'SIX', line=129)
W('23,3622', 0o54062, '', 'TS', 'ITEMP2', line=130)
W('23,3623', 0o50062, '', 'INDEX', 'ITEMP2', line=131)
W('23,3624', 0o30766, '', 'CA', 'CDUSPOT', line=132)
W('23,3625', 0o05033, '', 'TC', 'SPSIN', line=133)
W('23,3626', 0o00006, '', 'EXTEND', line=134)
W('23,3627', 0o74736, '', 'MP', 'BIT14', 'SCALE DOWN TO MATCH INTERPRETER OUTPUTS', line=135)
W('23,3630', 0o50062, '', 'INDEX', 'ITEMP2', line=136)
W('23,3631', 0o52737, '', 'DXCH', 'SINCDU', line=137)
W('23,3632', 0o50062, '', 'INDEX', 'ITEMP2', line=138)
W('23,3633', 0o30766, '', 'CA', 'CDUSPOT', line=139)
W('23,3634', 0o05032, '', 'TC', 'SPCOS', line=140)
W('23,3635', 0o00006, '', 'EXTEND', line=141)
W('23,3636', 0o74736, '', 'MP', 'BIT14', line=142)
W('23,3637', 0o50062, '', 'INDEX', 'ITEMP2', line=143)
W('23,3640', 0o52745, '', 'DXCH', 'COSCDU', line=144)
W('23,3641', 0o10062, '', 'CCS', 'ITEMP2', line=145)
W('23,3642', 0o13621, '', 'TCF', 'QUICTRIG +4', line=146)
W('23,3643', 0o30061, '', 'CA', 'ITEMP1', line=147)
W('23,3644', 0o00003, '', 'RELINT', line=148)
W('23,3645', 0o00000, '', 'TC', 'A', line=149)

# Page 1262
# ****************************************************************************
# THESE INTERFACE ROUTINES MAKE IT POSSIBLE TO CALL AX*SR*T, ETC., IN
# INTERPRETIVE.  LATER, WHERE POSSIBLE, THEY WILL BE ELIMINATED.
#
# THESE INTERFACE ROUTINES ARE PERMANENT.  ALL RESTORE USER'S EBANK
# SETTING. ALL ARE STRICT INTERPRETIVE SUBROUTINES, CALLED USING "CALL",
# RETURNING VIA QPRET.  ALL EXPECT AND RETURN THE VECTOR TO BE TRANSFORMED
# INTERPRETER-STYLE IN MPAC; COMPONENTS AT MPAC, MPAC +3, AND MPAC +5.
#
# TRG*SMNB AND TRG*NBSM BOTH EXPECT TO SEE THE 2'S COMPLEMENT ANGLES
# AT CDUSPOT (ORDER Y Z X, AT CDUSPOT, CDUSPOT +2, AND CDUSPOT +4; ODD
# LOCATIONS NEED NOT BE ZEROED).  TRG*NBSM DOES THE NB TO SM TRANSFORMATION;
# TRG*SMNB, VICE VERSA.
#
# CDU*NBSM DOES ITS TRANSFORMATION USING THE PRESENT CONTENTS OF
# THE CDL COUNTERS.  OTHERWISE IT IS LIKE TRG*NBSM.
#
# CDU*SMNB IS THE COMPLEMENT OF CDU*NBSM.

W('23,3646', 0o77776, 'CDU*SMNB', 'EXIT', kind='interp', line=171)
W('23,3647', 0o03547, '', 'TC', 'CDUTRIGS', line=172)
W('23,3650', 0o13653, '', 'TCF', 'C*MM*N1', line=173)

W('23,3651', 0o77776, 'TRG*SMNB', 'EXIT', kind='interp', line=175)
W('23,3652', 0o03555, '', 'TC', 'CD*TR*GS', line=176)
W('23,3653', 0o07532, 'C*MM*N1', 'TC', 'MPACVBUF', 'AX*SR*T EXPECTS VECTOR IN VBUF', line=177)
W('23,3654', 0o46245, '', 'CS', 'THREE', 'SIGNAL FOR SM TO NB TRANSFORMATION.', line=178)
W('23,3655', 0o03675, 'C*MM*N2', 'TC', 'AX*SR*T', line=179)
W('23,3656', 0o06037, '', 'TC', 'INTPRET', line=180)
W('23,3657', 0o43575, '', 'VLOAD', 'RVQ', kind='interp', line=181)
W('23,3660', 0o00123, '', '', 'VBUF', kind='operand', line=182)

W('23,3661', 0o77776, 'CDU*NBSM', 'EXIT', kind='interp', line=184)
W('23,3662', 0o03547, '', 'TC', 'CDUTRIGS', line=185)
W('23,3663', 0o13666, '', 'TCF', 'C*MM*N3', line=186)

W('23,3664', 0o77776, 'TRG*NBSM', 'EXIT', kind='interp', line=188)
W('23,3665', 0o03555, '', 'TC', 'CD*TR*GS', line=189)
W('23,3666', 0o07532, 'C*MM*N3', 'TC', 'MPACVBUF', 'FOR AX*SR*T', line=190)
W('23,3667', 0o36245, '', 'CA', 'THREE', 'SIGNAL FOR NB TO SM TRANSFORMATION', line=191)
W('23,3670', 0o13655, '', 'TCF', 'C*MM*N2', line=192)

# *NBSM* AND *SMNB* EXPECT TO SEE THE SINES AND COSINES (AT SINCDU
# AND COSCDU) RATHER THAN THE ANGLES THEMSELVES.  OTHERWISE THEY ARE
# LIKE TRG*NBSM AND TRG*SMNB.
#
# NOTE THAT JUST AS CD*TR*GS NEED BE CALLED ONLY ONCE FOR EACH SERIES
# OF TRANSFORMATIONS USING THE SAME ANGLES, SO TOO ONLY ONE OF TRG*NBSM
# Page 1263
# AND TRG*SMNB NEED BE CALLED FOR EACH SERIES.  FOR SUBSEQUENT TRANFOR-
# MATIONS USE *NBSM* AND *SMNB*.

W('23,3671', 0o77776, '*SMNB*', 'EXIT', kind='interp', line=204)
W('23,3672', 0o13653, '', 'TCF', 'C*MM*N1', line=205)

W('23,3673', 0o77776, '*NBSM*', 'EXIT', kind='interp', line=207)
W('23,3674', 0o13666, '', 'TCF', 'C*MM*N3', line=208)

# AX*SR*T COMBINES THE OLD SMNB AND NBSM.  FOR THE NB TO SM
# TRANSFORMATION, ENTER WITH +3 IN A.  FOR SM TO NB, ENTER WITH -3.
# THE VECTOR TO BE TRANSFORMED ARRIVES, AND IS RETURNED, IN VBUF.
# AX*SR*T EXPECTS TO FIND THE SINES AND COSINES OF THE ANGLES OF ROTATION
# AT SINCDU AND COSCDU, IN THE ORDER Y Z X.  A CALL TO CD*TR*GS, WITH
# THE 2'S COMPLEMENT ANGLES (ORDER Y Z X) AT CDUSPOT, WILL TAKE CARE OF
# THIS.  HERE IS A SAMPLE CALLING SEQUENCE:--
# TC      CDUTRIGS
# CS      THREE           # ("CA THREE" FOR NBSM)
# TC      AX*SR*T
# THE CALL TO CD*TR*GS NEED NOT BE REPEATED, WHEN AX*SR*T IS CALLED MORE
# THAN ONCE, UNLESS THE ANGLES HAVE CHANGED.
#
# AX*SR*T IS GUARANTEED SAFE ONLY FOR VECTORS OF MAGNITUDE LESS THAN
# UNITY.  A LOOK AT THE CASE IN WHICH A VECTOR OF GREATER MAGNITUDE
# HAPPENS TO LIE ALONG AN AXIS OF THE SYSTEM TO WHICH IT IS TO BE TRANS-
# FORMED CONVINCES ONE THAT THIS IS A RESTRICTION WHICH MUST BE ACCEPTED.

W('23,3675', 0o54142, 'AX*SR*T', 'TS', 'DEXDEX', 'WHERE IT BECOMES THE INDEX OF INDEXES.', line=228)
W('23,3676', 0o00006, '', 'EXTEND', line=229)
W('23,3677', 0o22145, '', 'QXCH', 'RTNSAVER', line=230)

W('23,3700', 0o10142, 'R*TL**P', 'CCS', 'DEXDEX', '              +3 --> 0        -3 --> 2', line=232)
W('23,3701', 0o40142, '', 'CS', 'DEXDEX', 'THUS:         +2 --> 1        -2 --> 1', line=233)
W('23,3702', 0o66245, '', 'AD', 'THREE', '              +1 --> 2        -1 --> 0', line=234)
W('23,3703', 0o00006, '', 'EXTEND', line=235)
W('23,3704', 0o50000, '', 'INDEX', 'A', line=236)
W('23,3705', 0o33764, '', 'DCA', 'INDEXI', line=237)
W('23,3706', 0o52144, '', 'DXCH', 'DEXI', line=238)

W('23,3707', 0o34753, '', 'CA', 'ONE', line=240)
W('23,3710', 0o54130, '', 'TS', 'BUF', line=241)
W('23,3711', 0o00006, '', 'EXTEND', line=242)
W('23,3712', 0o50143, '', 'INDEX', 'DEX1', line=243)
W('23,3713', 0o40123, '', 'DCS', 'VBUF', line=244)
W('23,3714', 0o13716, '', 'TCF', 'LOOP1', 'REALLY BE A SUBTRACT, AND VICE VERSA', line=245)

W('23,3715', 0o52131, 'LOOP2', 'DXCH', 'BUF', 'LOADING VECTOR COMPONENT, STORING INDEX', line=247)
# Page 1264
W('23,3716', 0o52155, 'LOOP1', 'DXCH', 'MPAC', line=249)
W('23,3717', 0o33762, '', 'CA', 'SINSLOC', line=250)
W('23,3720', 0o60143, '', 'AD', 'DEX1', line=251)
W('23,3721', 0o54116, '', 'TS', 'ADDRWD', line=252)

W('23,3722', 0o07107, '', 'TC', 'DMPSUB', 'MULTIPLY AT SIN(CDUANGLE)', line=254)
W('23,3723', 0o10142, '', 'CCS', 'DEXDEX', line=255)
W('23,3724', 0o52155, '', 'DXCH', 'MPAC', 'NBSM CASE', line=256)
W('23,3725', 0o13730, '', 'TCF', '+3', line=257)
W('23,3726', 0o00006, '', 'EXTEND', '', 'SMNB CASE', line=258)
W('23,3727', 0o40155, '', 'DCS', 'MPAC', line=259)
W('23,3730', 0o52160, '', 'DXCH', 'TERM1TMP', line=260)

W('23,3731', 0o36242, '', 'CA', 'SIX', 'SINCDU AND COSCDU (EACH 6 WORDS) MUST', line=262)
W('23,3732', 0o26116, '', 'ADS', 'ADDRWD', '      BE CONSECUTIVE AND IN THAT ORDER', line=263)

W('23,3733', 0o00006, '', 'EXTEND', line=265)
W('23,3734', 0o50130, '', 'INDEX', 'BUF', line=266)
W('23,3735', 0o50143, '', 'INDEX', 'DEX1', line=267)
W('23,3736', 0o30123, '', 'DCA', 'VBUF', line=268)
W('23,3737', 0o52155, '', 'DXCH', 'MPAC', line=269)
W('23,3740', 0o07107, '', 'TC', 'DMPSUB', 'MULTIPLY BY COS(CDUANGLE)', line=270)
W('23,3741', 0o52155, '', 'DXCH', 'MPAC', line=271)
W('23,3742', 0o20160, '', 'DAS', 'TERM1TMP', line=272)
W('23,3743', 0o52160, '', 'DXCH', 'TERM1TMP', line=273)
W('23,3744', 0o20001, '', 'DDOUBL', line=274)
W('23,3745', 0o50130, '', 'INDEX', 'BUF', line=275)
W('23,3746', 0o50143, '', 'INDEX', 'DEX1', line=276)
W('23,3747', 0o52123, '', 'DXCH', 'VBUF', line=277)
W('23,3750', 0o52131, '', 'DXCH', 'BUF', 'LOADING INDEX, STORING VECTOR COMPONENT', line=278)

W('23,3751', 0o10000, '', 'CCS', 'A', "'CAUSE THAT'S WHERE THE INDEX NOW IS", line=280)
W('23,3752', 0o13715, '', 'TCF', 'LOOP2', line=281)

W('23,3753', 0o00006, '', 'EXTEND', line=283)
W('23,3754', 0o26142, '', 'DIM', 'DEXDEX', 'DECREMENT MAGNITUDE PRESERVING SIGN', line=284)

W('23,3755', 0o10142, 'TSTPOINT', 'CCS', 'DEXDEX', 'ONLY THE BRANCHING FUNCTION IS USED', line=286)
W('23,3756', 0o13700, '', 'TCF', 'R*TL**P', line=287)
W('23,3757', 0o00145, '', 'TC', 'RTNSAVER', line=288)
W('23,3760', 0o13700, '', 'TCF', 'R*TL**P', line=289)
W('23,3761', 0o00145, '', 'TC', 'RTNSAVER', line=290)

W('23,3762', 0o00736, 'SINSLOC', 'ADRES', 'SINCDU', 'FOR USE IN SETTING ADDRWD', kind='data', line=292)

W('23,3763', 0o00004, 'INDEXI', 'DEC', '4', "**********   DON'T   ***********", kind='data', line=294)
W('23,3764', 0o00002, '', 'DEC', '2', '**********   TOUCH   ***********', kind='data', line=295)
W('23,3765', 0o00000, '', 'DEC', '0', '**********   THESE   ***********', kind='data', line=296)
# Page 1265
W('23,3766', 0o00004, '', 'DEC', '4', '********** CONSTANTS ***********', kind='data', line=298)

# ******************************************************************************

#   BANK 10
#   SETLOC FLESHLOC
#   BANK
#   COUNT* $$/POWFL

# ROUTINE FLESHPOT COMPUTES THE BODY-STABLE MEMBER TRANSFORMATION MATRIX (COMMONLY CALLED XNB) AND STORES
# IT IN THE LOCATIONS SPECIFIED BY THE ECADR ENTERING IN A.

W('10,2030', 0o77776, 'CALCSMSC', 'EXIT', kind='interp', line=310)
W('10,2031', 0o04616, '', 'TC', 'BANKCALL', line=311)
W('10,2032', 0o20036, '', 'CADR', 'FLESHPOT -1', kind='data', line=312)
W('10,2033', 0o06037, '', 'TC', 'INTPRET', line=313)
W('10,2034', 0o77616, '', 'RVQ', kind='interp', line=314)

W('10,2035', 0o02664, 'XNBECADR', 'ECADR', 'XNB', kind='data', line=316)

W('10,2036', 0o32035, '', 'CAF', 'XNBECADR', line=318)

W('10,2037', 0o54142, 'FLESHPOT', 'TS', 'TEM2', line=320)
W('10,2040', 0o56003, '', 'XCH', 'EBANK', line=321)
W('10,2041', 0o56142, '', 'XCH', 'TEM2', line=322)
W('10,2042', 0o74357, '', 'MASK', 'LOW8', line=323)
W('10,2043', 0o65007, '', 'AD', 'OCT1400', line=324)
W('10,2044', 0o54141, '', 'TS', 'TEM1', line=325)

W('10,2045', 0o00006, '', 'EXTEND', line=327)
W('10,2046', 0o30745, '', 'DCA', 'COSCDUY', line=328)
W('10,2047', 0o52155, '', 'DXCH', 'MPAC', line=329)
W('10,2050', 0o07103, '', 'TC', 'DMP', line=330)
W('10,2051', 0o00746, '', 'ADRES', 'COSCDUZ', kind='data', line=331)
W('10,2052', 0o52155, '', 'DXCH', 'MPAC', line=332)
W('10,2053', 0o20001, '', 'DDOUBL', line=333)
W('10,2054', 0o50141, '', 'INDEX', 'TEM1', line=334)
W('10,2055', 0o52001, '', 'DXCH', '0', '= COSY COSZ', line=335)

W('10,2056', 0o00006, '', 'EXTEND', line=337)
W('10,2057', 0o30741, '', 'DCA', 'SINCDUZ', line=338)
W('10,2060', 0o50141, '', 'INDEX', 'TEM1', line=339)
W('10,2061', 0o52003, '', 'DXCH', '2', '= SINZ', line=340)

W('10,2062', 0o00006, '', 'EXTEND', line=342)
W('10,2063', 0o40737, '', 'DCS', 'SINCDUY', line=343)
W('10,2064', 0o52155, '', 'DXCH', 'MPAC', line=344)
W('10,2065', 0o07107, '', 'TC', 'DMPSUB', 'ADDRWD SET TO COSCDUZ', line=345)
# Page 1266
W('10,2066', 0o52155, '', 'DXCH', 'MPAC', line=347)
W('10,2067', 0o20001, '', 'DDOUBL', line=348)
W('10,2070', 0o50141, '', 'INDEX', 'TEM1', line=349)
W('10,2071', 0o52005, '', 'DXCH', '4', '= - SINY COSZ', line=350)

W('10,2072', 0o00006, '', 'EXTEND', line=352)
W('10,2073', 0o40743, '', 'DCS', 'SINCDUX', line=353)
W('10,2074', 0o52155, '', 'DXCH', 'MPAC', line=354)
W('10,2075', 0o07107, '', 'TC', 'DMPSUB', 'ADDRWD SET TO COSCDUZ STILL', line=355)
W('10,2076', 0o52155, '', 'DXCH', 'MPAC', line=356)
W('10,2077', 0o20001, '', 'DDOUBL', line=357)
W('10,2100', 0o52160, '', 'DXCH', 'MPAC +3', line=358)

W('10,2101', 0o00006, '', 'EXTEND', line=360)
W('10,2102', 0o40743, '', 'DCS', 'SINCDUX', line=361)
W('10,2103', 0o52155, '', 'DXCH', 'MPAC', line=362)
W('10,2104', 0o07103, '', 'TC', 'DMP', line=363)
W('10,2105', 0o00740, '', 'ADRES', 'SINCDUZ', kind='data', line=364)
W('10,2106', 0o00006, '', 'EXTEND', line=365)
W('10,2107', 0o40155, '', 'DCS', 'MPAC', line=366)
W('10,2110', 0o52162, '', 'DXCH', 'MPAC +5', line=367)
W('10,2111', 0o07103, '', 'TC', 'DMP', line=368)
W('10,2112', 0o00736, '', 'ADRES', 'SINCDUY', kind='data', line=369)
W('10,2113', 0o52155, '', 'DXCH', 'MPAC', line=370)
W('10,2114', 0o20001, '', 'DDOUBL', line=371)
W('10,2115', 0o20001, '', 'DDOUBL', line=372)
W('10,2116', 0o52162, '', 'DXCH', 'MPAC +5', line=373)

W('10,2117', 0o52155, '', 'DXCH', 'MPAC', line=375)
W('10,2120', 0o07103, '', 'TC', 'DMP', line=376)
W('10,2121', 0o00744, '', 'ADRES', 'COSCDUY', kind='data', line=377)
W('10,2122', 0o52155, '', 'DXCH', 'MPAC', line=378)
W('10,2123', 0o20001, '', 'DDOUBL', line=379)
W('10,2124', 0o20001, '', 'DDOUBL', line=380)
W('10,2125', 0o52131, '', 'DXCH', 'BUF', line=381)

W('10,2126', 0o00006, '', 'EXTEND', line=383)
W('10,2127', 0o30745, '', 'DCA', 'COSCDUY', line=384)
W('10,2130', 0o52155, '', 'DXCH', 'MPAC', line=385)
W('10,2131', 0o07103, '', 'TC', 'DMP', line=386)
W('10,2132', 0o00750, '', 'ADRES', 'COSCDUX', kind='data', line=387)
W('10,2133', 0o52155, '', 'DXCH', 'MPAC', line=388)
W('10,2134', 0o20001, '', 'DDOUBL', line=389)
W('10,2135', 0o20162, '', 'DAS', 'MPAC +5', line=390)

W('10,2136', 0o00006, '', 'EXTEND', line=392)
W('10,2137', 0o30737, '', 'DCA', 'SINCDUY', line=393)
W('10,2140', 0o52155, '', 'DXCH', 'MPAC', line=394)
W('10,2141', 0o07107, '', 'TC', 'DMPSUB', 'ADDRWD SET TO COSCDUX', line=395)
W('10,2142', 0o52155, '', 'DXCH', 'MPAC', line=396)

# Page 1267
W('10,2143', 0o20001, '', 'DDOUBL', line=399)
W('10,2144', 0o20131, '', 'DAS', 'BUF', line=400)

W('10,2145', 0o52131, '', 'DXCH', 'BUF', line=402)
W('10,2146', 0o52155, '', 'DXCH', 'MPAC', line=403)

W('10,2147', 0o00006, '', 'EXTEND', line=405)
W('10,2150', 0o30155, '', 'DCA', 'MPAC', line=406)
W('10,2151', 0o50141, '', 'INDEX', 'TEM1', line=407)
W('10,2152', 0o52015, '', 'DXCH', '14', '= - SINY COSX + SINX SINZ COSY', line=408)

W('10,2153', 0o00006, '', 'EXTEND', line=410)
W('10,2154', 0o30160, '', 'DCA', 'MPAC +3', line=411)
W('10,2155', 0o50141, '', 'INDEX', 'TEM1', line=412)
W('10,2156', 0o52017, '', 'DXCH', '16', '= - SINX COSZ', line=413)

W('10,2157', 0o00006, '', 'EXTEND', line=415)
W('10,2160', 0o30162, '', 'DCA', 'MPAC +5', line=416)
W('10,2161', 0o50141, '', 'INDEX', 'TEM1', line=417)
W('10,2162', 0o52021, '', 'DXCH', '20', '= COSX COSY - SINX SINY SINZ', line=418)

W('10,2163', 0o30141, '', 'CA', 'TEM1', line=420)
W('10,2164', 0o54116, '', 'TS', 'ADDRWD', line=421)
W('10,2165', 0o00006, '', 'EXTEND', line=422)
W('10,2166', 0o30006, '', 'DCA', 'Z', line=423)
W('10,2167', 0o64751, '', 'AD', 'FOUR', line=424)
W('10,2170', 0o52165, '', 'DXCH', 'LOC', line=425)
W('10,2171', 0o34744, '', 'CAF', 'BIT8', line=426)
W('10,2172', 0o54023, '', 'TS', 'EDOP', line=427)
W('10,2173', 0o17460, '', 'TCF', 'VXV', line=428)
W('10,2174', 0o52155, '', 'DXCH', 'MPAC', line=429)
W('10,2175', 0o20001, '', 'DDOUBL', line=430)
W('10,2176', 0o50141, '', 'INDEX', 'TEM1', line=431)
W('10,2177', 0o52007, '', 'DXCH', '6', line=432)

W('10,2200', 0o52160, '', 'DXCH', 'MPAC +3', line=434)
W('10,2201', 0o20001, '', 'DDOUBL', line=435)
W('10,2202', 0o50141, '', 'INDEX', 'TEM1', line=436)
W('10,2203', 0o52011, '', 'DXCH', '10', line=437)

W('10,2204', 0o52162, '', 'DXCH', 'MPAC +5', line=439)
W('10,2205', 0o20001, '', 'DDOUBL', line=440)
W('10,2206', 0o50141, '', 'INDEX', 'TEM1', line=441)
W('10,2207', 0o52013, '', 'DXCH', '12', line=442)

W('10,2210', 0o30142, '', 'CA', 'TEM2', line=444)
W('10,2211', 0o54003, '', 'TS', 'EBANK', line=445)
W('10,2212', 0o14631, '', 'TCF', 'SWRETURN', line=446)
