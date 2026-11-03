"""POWERED_FLIGHT_SUBROUTINES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/POWERED_FLIGHT_SUBROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1365-1372 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('POWERED_FLIGHT_SUBROUTINES', 'POWERED_FLIGHT_SUBROUTINES.agc', 'Comanche055', pages='1365-1372')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     POWERED_FLIGHT_SUBROUTINES.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1365-1372
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Colossus249/ file of the same
# name, using Comanche055 page images.
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

# Page 1365
#   BANK 14  # SAME FBANK AS THE FINDCDUD SUB-PROGRAM
#   SETLOC POWFLITE
#   BANK

#   EBANK= DEXDEX
#   COUNT* $$/POWFL

# CDUTRIG, CDUTRIG1, CDUTRIG2, AND CD*GR*GS ALL COMPUTE THE SINES AND
# COSINES OF THREE 2'S COMPLEMENT ANGLES AND PLACE THE RESULT, DOUBLE
# PRECISION, IN THE SAME ORDER AS THE INPUTS, AT SINCDU AND COSCDU.  AN
# ADDITIONAL OUTPUT IS THE 1'S COMPLEMENT ANGLES AT CDUSPOT.  THESE
# ROUTINES GO OUT OF THEIR WAY TO LEAVE THE MPAC AREA AS THEY FIND IT,
# EXCEPT FOR THE GENERALLY UNIMPORTANT MPAC +2.  THEY DIFFER ONLY IN
# WHERE THEY GET THE ANGLES, AND IN METHOD OF CALLING.

# CDUTRIG (AND CDUTRIG1, WHICH CAN BE CALLED IN BASIC) COMPUTE THE
# SINES AND COSINES FROM THE CURRENT CONTENTS OF THE CDU REGISTERS.
# THE CONTENTS OF CDUTEMP, ETC., ARE NOT TOUCHED SO THAT THEY MAY
# CONTINUE TO FORM A CONSISTENT SET WITH THE LATEST PIPA READINGS.

# CDUTRIG1 IS LIKE CDUTRIG EXCEPT THAT IT CAN BE CALLED IN BASIC.

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

# CD*TR*G IS LIKE CD*TR*GS EXCEPT THAT IT CAN BE CALLED IN
# INTERPRETIVE.

W('23,3477', 0o77776, 'CDUTRIG', 'EXIT', kind='interp', line=69)
W('23,3500', 0o03507, '', 'TC', 'CDUTRIGS', line=70)
W('23,3501', 0o06006, '', 'TC', 'INTPRET', line=71)
W('23,3502', 0o77616, '', 'RVQ', kind='interp', line=72)

W('23,3503', 0o77776, 'CD*TR*G', 'EXIT', kind='interp', line=74)
W('23,3504', 0o03515, '', 'TC', 'CD*TR*GS', line=75)
W('23,3505', 0o06006, '', 'TC', 'INTPRET', line=76)
W('23,3506', 0o77616, '', 'RVQ', kind='interp', line=77)

W('23,3507', 0o30032, 'CDUTRIGS', 'CA', 'CDUX', line=79)
W('23,3510', 0o54772, '', 'TS', 'CDUSPOT +4', line=80)
W('23,3511', 0o30033, '', 'CA', 'CDUY', line=81)
W('23,3512', 0o54766, '', 'TS', 'CDUSPOT', line=82)
# Page 1366
W('23,3513', 0o30034, '', 'CA', 'CDUZ', line=84)
W('23,3514', 0o54770, '', 'TS', 'CDUSPOT +2', line=85)

W('23,3515', 0o00006, 'CD*TR*GS', 'EXTEND', line=87)
W('23,3516', 0o22142, '', 'QXCH', 'TEM2', line=88)
W('23,3517', 0o35015, '', 'CAF', 'FOUR', line=89)
W('23,3520', 0o76211, 'TR*GL**P', 'MASK', 'SIX', 'MAKE IT EVEN AND SMALLER', line=90)
W('23,3521', 0o54143, '', 'TS', 'TEM3', line=91)
W('23,3522', 0o50143, '', 'INDEX', 'TEM3', line=92)
W('23,3523', 0o30766, '', 'CA', 'CDUSPOT', line=93)
W('23,3524', 0o52155, '', 'DXCH', 'MPAC', "STORING 2'S COMP ANGLE, LOADING MPAC", line=94)
W('23,3525', 0o52127, '', 'DXCH', 'VBUF +4', 'STORING MPAC FOR LATER RESTORATION', line=95)
W('23,3526', 0o04757, '', 'TC', 'USPRCADR', line=96)
W('23,3527', 0o45513, '', 'CADR', 'CDULOGIC', kind='data', line=97)
W('23,3530', 0o00006, '', 'EXTEND', line=98)
W('23,3531', 0o30155, '', 'DCA', 'MPAC', line=99)
W('23,3532', 0o50143, '', 'INDEX', 'TEM3', line=100)
W('23,3533', 0o52767, '', 'DXCH', 'CDUSPOT', "STORING 1'S COMPLEMENT ANGLE", line=101)
W('23,3534', 0o04757, '', 'TC', 'USPRCADR', line=102)
W('23,3535', 0o01516, '', 'CADR', 'COSINE', kind='data', line=103)
W('23,3536', 0o52155, '', 'DXCH', 'MPAC', line=104)
W('23,3537', 0o50143, '', 'INDEX', 'TEM3', line=105)
W('23,3540', 0o52745, '', 'DXCH', 'COSCDU', 'STORING COSINE', line=106)
W('23,3541', 0o00006, '', 'EXTEND', line=107)
W('23,3542', 0o50143, '', 'INDEX', 'TEM3', line=108)
W('23,3543', 0o30767, '', 'DCA', 'CDUSPOT', "LOADING 1'S COMPLEMENT ANGLE", line=109)
W('23,3544', 0o04757, '', 'TC', 'USPRCADR', line=110)
W('23,3545', 0o01530, '', 'CADR', 'SINE +1', 'SINE +1 EXPECTS ARGUMENT IN A AND L', kind='data', line=111)
W('23,3546', 0o52127, '', 'DXCH', 'VBUF +4', 'BRINGING UP PRIOR MPAC TO BE RESTORED', line=112)
W('23,3547', 0o52155, '', 'DXCH', 'MPAC', line=113)
W('23,3550', 0o50143, '', 'INDEX', 'TEM3', line=114)
W('23,3551', 0o52737, '', 'DXCH', 'SINCDU', line=115)
W('23,3552', 0o10143, '', 'CCS', 'TEM3', line=116)
W('23,3553', 0o13520, '', 'TCF', 'TR*GL**P', line=117)
W('23,3554', 0o00142, '', 'TC', 'TEM2', line=118)
# Page 1367
# *******************************************************************************************************

# QUICTRIG, INTENDED FOR GUIDANCE CYCLE USE WHERE TIME IS CRITICAL, IS A MUCH FASTER VERSION OF CD*TR*GS.
# QUICTRIG COMPUTES AND STORES THE SINES AND COSINES OF THE 2'S COMPLEMENT ANGLES AT CDUSPOT, CDUSPOT +2,
# AND CDUSPOT +4.  UNLIKE CD*TR*GS, QUICTRIG DOES NOT LEAVE THE 1'S COMPLEMENT VERSIONS OF THE ANGLES IN
# CDUSPOT.  QUICTRIG'S EXECUTION TIME IS 4.1 MS; THIS IS 10 TIMES AS FAST AS CD*TR*GS.  QUICTRIG MAY BE
# CALLED FROM INTERPRETIVE AS AN RTB OP-CODE, OR FROM BASIC VIA BANKCALL OR IBNKCALL.

W('23,3555', 0o00004, 'QUICTRIG', 'INHINT', '', 'INHINT SINCE DAP USES THE SAME TEMPS', line=128)
W('23,3556', 0o00006, '', 'EXTEND', line=129)
W('23,3557', 0o22061, '', 'QXCH', 'ITEMP1', line=130)
W('23,3560', 0o35015, '', 'CAF', 'FOUR', line=131)
W('23,3561', 0o76211, '', 'MASK', 'SIX', line=132)
W('23,3562', 0o54062, '', 'TS', 'ITEMP2', line=133)
W('23,3563', 0o50062, '', 'INDEX', 'ITEMP2', line=134)
W('23,3564', 0o30766, '', 'CA', 'CDUSPOT', line=135)
W('23,3565', 0o05075, '', 'TC', 'SPSIN', line=136)
W('23,3566', 0o00006, '', 'EXTEND', line=137)
W('23,3567', 0o75002, '', 'MP', 'BIT14', 'SCALE DOWN TO MATCH INTERPRETER OUTPUTS', line=138)
W('23,3570', 0o50062, '', 'INDEX', 'ITEMP2', line=139)
W('23,3571', 0o52737, '', 'DXCH', 'SINCDU', line=140)
W('23,3572', 0o50062, '', 'INDEX', 'ITEMP2', line=141)
W('23,3573', 0o30766, '', 'CA', 'CDUSPOT', line=142)
W('23,3574', 0o05074, '', 'TC', 'SPCOS', line=143)
W('23,3575', 0o00006, '', 'EXTEND', line=144)
W('23,3576', 0o75002, '', 'MP', 'BIT14', line=145)
W('23,3577', 0o50062, '', 'INDEX', 'ITEMP2', line=146)
W('23,3600', 0o52745, '', 'DXCH', 'COSCDU', line=147)
W('23,3601', 0o10062, '', 'CCS', 'ITEMP2', line=148)
W('23,3602', 0o13561, '', 'TCF', 'QUICTRIG +4', line=149)
W('23,3603', 0o30061, '', 'CA', 'ITEMP1', line=150)
W('23,3604', 0o00003, '', 'RELINT', line=151)
W('23,3605', 0o00000, '', 'TC', 'A', line=152)
# Page 1368
# ****************************************************************************

# THESE INTERFACE ROUTINES MAKE IT POSSIBLE TO CALL AX*SR*T, ETC., IN
# INTERPRETIVE.  LATER, WHERE POSSIBLE, THEY WILL BE ELIMINATED.
#
# NBSM WILL BE THE FIRST TO GO.  IT SHOULD NOT BE USED.

W('23,3606', 0o77620, 'NBSM', 'STQ', kind='interp', line=162)
W('23,3607', 0o00047, '', '', 'X2', kind='operand', line=163)
W('23,3610', 0o76740, '', 'LXC,1', 'VLOAD*', kind='interp', line=164)
W('23,3611', 0o00050, '', '', 'S1', 'BASE ADDRESS OF THE CDU ANGLES IS IN S1', kind='operand', line=165)
W('23,3612', 0o00001, '', '', '0,1', kind='operand', line=166)
W('23,3613', 0o24767, '', 'STOVL', 'CDUSPOT', kind='interp', line=167)
W('23,3614', 0o00041, '', '', '32D', 'VECTOR TO BE TRANSFORMED IS IN 32D', kind='operand', line=168)
W('23,3615', 0o77624, '', 'CALL', kind='interp', line=169)
W('23,3616', 0o47637, '', '', 'TRG*NBSM', kind='operand', line=170)
W('23,3617', 0o34041, '', 'STCALL', '32D', "SINCE THERE'S NO STGOTO", kind='interp', line=171)
W('23,3620', 0o00047, '', '', 'X2', kind='operand', line=172)

# THESE INTERFACE ROUTINES ARE PERMANENT.  ALL RESTORE USER'S EBANK
# SETTING.  ALL ARE STRICT INTERPRETIVE SUBROUTINES, CALLED USING "CALL",
# RETURNING VIA QPRET.  ALL EXPECT AND RETURN THE VECTOR TO BE TRANSFOR-
# MED INTERPRETER-STYLE IN MPAC; COMPONENTS AT MPAC, MPAC +3, AND MPAC +5.

# TRG*SMNB AND TRG*NBSM BOTH EXPECT TO SEE THE 2'S COMPLEMENT ANGLES
# AT CDUSPOT (ORDER Y Z X, AT CDUSPOT, CDUSPOT +2, AND CDUSPOT +4; ODD
# LOCATIONS NEED NOT BE ZEROED).  TRG*NBSM DOES THE NB TO SM TRANSFOR-
# MATION; TRG*SMNB, VICE VERSA.

# CDU*NBSM DOES ITS TRANSFORMATION USING THE PRESENT CONTENTS OF
# THE CDL COUNTERS.  OTHERWISE IT IS LIKE TRG*NBSM.
#
# CDU*SMNB IS THE COMPLEMENT OF CDU*NBSM.

W('23,3621', 0o77776, 'CDU*SMNB', 'EXIT', kind='interp', line=189)
W('23,3622', 0o03507, '', 'TC', 'CDUTRIGS', line=190)
W('23,3623', 0o13626, '', 'TCF', 'C*MM*N1', line=191)

W('23,3624', 0o77776, 'TRG*SMNB', 'EXIT', kind='interp', line=193)
W('23,3625', 0o03515, '', 'TC', 'CD*TR*GS', line=194)
W('23,3626', 0o07501, 'C*MM*N1', 'TC', 'MPACVBUF', 'AX*SR*T EXPECTS VECTOR IN VBUF', line=195)
W('23,3627', 0o46214, '', 'CS', 'THREE', 'SIGNAL FOR SM TO NB TRANSFORMATION.', line=196)
W('23,3630', 0o03650, 'C*MM*N2', 'TC', 'AX*SR*T', line=197)
W('23,3631', 0o06006, '', 'TC', 'INTPRET', line=198)
W('23,3632', 0o43575, '', 'VLOAD', 'RVQ', kind='interp', line=199)
W('23,3633', 0o00123, '', '', 'VBUF', kind='operand', line=200)

W('23,3634', 0o77776, 'CDU*NBSM', 'EXIT', kind='interp', line=202)
W('23,3635', 0o03507, '', 'TC', 'CDUTRIGS', line=203)

# Page 1369

W('23,3636', 0o13641, '', 'TCF', 'C*MM*N3', line=207)

W('23,3637', 0o77776, 'TRG*NBSM', 'EXIT', kind='interp', line=209)
W('23,3640', 0o03515, '', 'TC', 'CD*TR*GS', line=210)
W('23,3641', 0o07501, 'C*MM*N3', 'TC', 'MPACVBUF', 'FOR AX*SR*T', line=211)
W('23,3642', 0o36214, '', 'CA', 'THREE', 'SIGNAL FOR NB TO SM TRANSFORMATION', line=212)
W('23,3643', 0o13630, '', 'TCF', 'C*MM*N2', line=213)

# *NBSM* AND *SMNB* EXPECT TO SEE THE SINES AND COSINES (AT SINCDU
# AND COSCDU) RATHER THAN THE ANGLES THEMSELVES.  OTHERWISE THEY ARE
# LIKE TRG*NBSM AND TRG*SMNB.

# NOTE THAT JUST AS CD*TR*GS NEED BE CALLED ONLY ONCE FOR EACH SERIES
# OF TRANSFORMATIONS USING THE SAME ANGLES, SO TOO ONLY ONE OF TRG*NBSM
# AND TRG*SMNB NEED BE CALLED FOR EACH SERIES.  FOR SUBSEQUENT TRANFOR-
# MATIONS USE *NBSM* AND *SMNB*.

W('23,3644', 0o77776, '*SMNB*', 'EXIT', kind='interp', line=224)
W('23,3645', 0o13626, '', 'TCF', 'C*MM*N1', line=225)

W('23,3646', 0o77776, '*NBSM*', 'EXIT', kind='interp', line=227)
W('23,3647', 0o13641, '', 'TCF', 'C*MM*N3', line=228)

# AX*SR*T COMBINES THE OLD SMNB AND NBSM.  FOR THE NB TO SM
# TRANSFORMATION, ENTER WITH +3 IN A.  FOR SM TO NB, ENTER WITH -3.
# THE VECTOR TO BE TRANSFORMED ARRIVES, AND IS RETURNED, IN VBUF.
# AX*SR*T EXPECTS TO FIND THE SINES AND COSINES OF THE ANGLES OF ROTATION
# AT SINCDU AND COSCDU, IN THE ORDER Y Z X.  A CALL TO CD*TR*GS, WITH
# THE 2'S COMPLEMENT ANGLES (ORDER Y Z X) AT CDUSPOT, WILL TAKE CARE OF
# THIS.  HERE IS A SAMPLE CALLING SEQUENCE:-

# TC      CDUTRIGS
# CS      THREE           ("CA THREE" FOR NBSM)
# TC      AX*SR*T

# THE CALL TO CD*TR*GS NEED NOT BE REPEATED, WHEN AX*SR*T IS CALLED MORE
# THAN ONCE, UNLESS THE ANGLES HAVE CHANGED.

# AX*SR*T IS GUARANTEED SAFE ONLY FOR VECTORS OF MAGNITUDE LESS THAN
# UNITY.  A LOOK AT THE CASE IN WHICH A VECTOR OF GREATER MAGNITUDE
# HAPPENS TO LIE ALONG AN AXIS OF THE SYSTEM TO WHICH IT IS TO BE TRANS-
# FORMED CONVINCES ONE THAT THIS IS A RESTRICTION WHICH MUST BE ACCEPTED.

W('23,3650', 0o54142, 'AX*SR*T', 'TS', 'DEXDEX', 'WHERE IT BECOMES THE INDEX OF INDEXES', line=250)
W('23,3651', 0o00006, '', 'EXTEND', line=251)
W('23,3652', 0o22145, '', 'QXCH', 'RTNSAVER', line=252)

W('23,3653', 0o10142, 'R*TL**P', 'CCS', 'DEXDEX', '              +3 --> 0        -3 --> 2', line=254)
W('23,3654', 0o40142, '', 'CS', 'DEXDEX', 'THUS:         +2 --> 1        -2 --> 1', line=255)
W('23,3655', 0o66214, '', 'AD', 'THREE', '              +1 --> 2        -1 --> 0', line=256)
# Page 1370
W('23,3656', 0o00006, '', 'EXTEND', line=258)
W('23,3657', 0o50000, '', 'INDEX', 'A', line=259)
W('23,3660', 0o33737, '', 'DCA', 'INDEXI', line=260)
W('23,3661', 0o52144, '', 'DXCH', 'DEXI', line=261)

W('23,3662', 0o35017, '', 'CA', 'ONE', line=263)
W('23,3663', 0o54130, '', 'TS', 'BUF', line=264)
W('23,3664', 0o00006, '', 'EXTEND', line=265)
W('23,3665', 0o50143, '', 'INDEX', 'DEX1', line=266)
W('23,3666', 0o40123, '', 'DCS', 'VBUF', line=267)
W('23,3667', 0o13671, '', 'TCF', 'LOOP1', 'REALLY BE A SUBTRACT, AND VICE VERSA', line=268)

W('23,3670', 0o52131, 'LOOP2', 'DXCH', 'BUF', 'LOADING VECTOR COMPONENT, STORING INDEX', line=270)

W('23,3671', 0o52155, 'LOOP1', 'DXCH', 'MPAC', line=272)
W('23,3672', 0o33735, '', 'CA', 'SINESLOC', line=273)
W('23,3673', 0o60143, '', 'AD', 'DEX1', line=274)
W('23,3674', 0o54116, '', 'TS', 'ADDRWD', line=275)

W('23,3675', 0o07056, '', 'TC', 'DMPSUB', 'MULTIPLY BY SIN(CDUANGLE)', line=277)
W('23,3676', 0o10142, '', 'CCS', 'DEXDEX', line=278)
W('23,3677', 0o52155, '', 'DXCH', 'MPAC', 'NBSM CASE', line=279)
W('23,3700', 0o13703, '', 'TCF', '+3', line=280)
W('23,3701', 0o00006, '', 'EXTEND', '', 'SMNB CASE', line=281)
W('23,3702', 0o40155, '', 'DCS', 'MPAC', line=282)
W('23,3703', 0o52134, '', 'DXCH', 'TERM1TMP', line=283)

W('23,3704', 0o36211, '', 'CA', 'SIX', 'SINCDU AND COSCDU (EACH 6 WORDS) MUST', line=285)
W('23,3705', 0o26116, '', 'ADS', 'ADDRWD', '      BE CONSECUTIVE AND IN THAT ORDER', line=286)

W('23,3706', 0o00006, '', 'EXTEND', line=288)
W('23,3707', 0o50130, '', 'INDEX', 'BUF', line=289)
W('23,3710', 0o50143, '', 'INDEX', 'DEX1', line=290)
W('23,3711', 0o30123, '', 'DCA', 'VBUF', line=291)
W('23,3712', 0o52155, '', 'DXCH', 'MPAC', line=292)
W('23,3713', 0o07056, '', 'TC', 'DMPSUB', 'MULTIPLY BY COS(CDUANGLE)', line=293)
W('23,3714', 0o52155, '', 'DXCH', 'MPAC', line=294)
W('23,3715', 0o20134, '', 'DAS', 'TERM1TMP', line=295)
W('23,3716', 0o52134, '', 'DXCH', 'TERM1TMP', line=296)
W('23,3717', 0o20001, '', 'DDOUBL', line=297)
W('23,3720', 0o50130, '', 'INDEX', 'BUF', line=298)
W('23,3721', 0o50143, '', 'INDEX', 'DEX1', line=299)
W('23,3722', 0o52123, '', 'DXCH', 'VBUF', line=300)
W('23,3723', 0o52131, '', 'DXCH', 'BUF', 'LOADING INDEX, STORING VECTOR COMPONENT', line=301)

W('23,3724', 0o10000, '', 'CCS', 'A', "'CAUSE THAT'S WHERE THE INDEX NOW IS", line=303)
W('23,3725', 0o13670, '', 'TCF', 'LOOP2', line=304)

W('23,3726', 0o00006, '', 'EXTEND', line=306)
W('23,3727', 0o26142, '', 'DIM', 'DEXDEX', 'DECREMENT MAGNITUDE PRESERVING SIGN', line=307)

# Page 1371
W('23,3730', 0o10142, 'TSTPOINT', 'CCS', 'DEXDEX', 'ONLY THE BRANCHING FUNCTION IS USED', line=310)
W('23,3731', 0o13653, '', 'TCF', 'R*TL**P', line=311)
W('23,3732', 0o00145, '', 'TC', 'RTNSAVER', line=312)
W('23,3733', 0o13653, '', 'TCF', 'R*TL**P', line=313)
W('23,3734', 0o00145, '', 'TC', 'RTNSAVER', line=314)

W('23,3735', 0o00736, 'SINESLOC', 'ADRES', 'SINCDU', 'FOR USE IN SETTING ADDRWD', kind='data', line=317)

W('23,3736', 0o00004, 'INDEXI', 'DEC', '4', "**********   DON'T   ***********", kind='data', line=320)
W('23,3737', 0o00002, '', 'DEC', '2', '**********   TOUCH   ***********', kind='data', line=321)
W('23,3740', 0o00000, '', 'DEC', '0', '**********   THESE   ***********', kind='data', line=322)
W('23,3741', 0o00004, '', 'DEC', '4', '********** CONSTANTS ***********', kind='data', line=323)

# ******************************************************************************
# Page 1372
# THIS SUBROUTINE COMPUTES INCREMENTAL CHANGES IN CDU(GIMBAL) ANGLES FROM INCREMENTAL CHANGES ABOUT SM AXES.  IT
# REQUIRES SM INCREMENTS AS A DP VECTOR SCALED AT ONE REVOLUTION(DTHETASM,+2,+4).  SIN,COS(CDUY,Z,X) ARE IN
# SINCDU,+2,+4 AND COSCDU,+2,+4 RESPECTIVELY,SCALED TO ONE HALF.  CDU INCREENTS ARE PLACED IN DCDU,+2,+4 SCALED TO
# ONE REVOLUTION.

# *  COS(IGA)SEC(MGA)             0               -SIN(IGA)SEC(MGA) *
# *                                                                 *
# * -COS(IGA)TAN(MGA)             1                SIN(IGA)TAN(MGA) *
# *                                                                 *
# *      SIN(IGA)                 0                    COS(IGA)     *

#   BANK 14
#   SETLOC POWFLIT1
#   BANK

W('23,3742', 0o41345, 'SMCDURES', 'DLOAD', 'DMP', kind='interp', line=342)
W('23,3743', 0o03212, '', '', 'DTHETASM', kind='operand', line=343)
W('23,3744', 0o00745, '', '', 'COSCDUY', kind='operand', line=344)

W('23,3745', 0o41325, '', 'PDDL', 'DMP', kind='interp', line=346)
W('23,3746', 0o03216, '', '', 'DTHETASM +4', kind='operand', line=347)
W('23,3747', 0o00737, '', '', 'SINCDUY', kind='operand', line=348)

W('23,3750', 0o77621, '', 'BDSU', kind='interp', line=350)
W('23,3751', 0o77671, '', 'DDV', kind='interp', line=351)
W('23,3752', 0o00747, '', '', 'COSCDUZ', kind='operand', line=352)
W('23,3753', 0o03204, '', 'STORE', 'DCDU', kind='interp', line=353)

W('23,3754', 0o72405, '', 'DMP', 'SL1', 'SCALE', kind='interp', line=355)
W('23,3755', 0o00741, '', '', 'SINCDUZ', kind='operand', line=356)
W('23,3756', 0o77621, '', 'BDSU', kind='interp', line=357)

W('23,3757', 0o03214, '', '', 'DTHETASM +2', kind='operand', line=359)
W('23,3760', 0o17206, '', 'STODL', 'DCDU +2', kind='interp', line=360)
W('23,3761', 0o03212, '', '', 'DTHETASM', kind='operand', line=361)

W('23,3762', 0o65205, '', 'DMP', 'PDDL', kind='interp', line=363)
W('23,3763', 0o00737, '', '', 'SINCDUY', kind='operand', line=364)
W('23,3764', 0o03216, '', '', 'DTHETASM +4', kind='operand', line=365)

W('23,3765', 0o43205, '', 'DMP', 'DAD', kind='interp', line=367)
W('23,3766', 0o00745, '', '', 'COSCDUY', kind='operand', line=368)
W('23,3767', 0o77752, '', 'SL1', kind='interp', line=369)
W('23,3770', 0o03210, '', 'STORE', 'DCDU +4', kind='interp', line=370)
W('23,3771', 0o77616, '', 'RVQ', kind='interp', line=371)
