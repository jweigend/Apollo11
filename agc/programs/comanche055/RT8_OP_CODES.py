"""RT8_OP_CODES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/RT8_OP_CODES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1508-1516 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('RT8_OP_CODES', 'RT8_OP_CODES.agc', 'Comanche055', pages='1508-1516')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     RT8_OP_CODES.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 1508-1516
# Contact:      Ron Burkey <info@sandroid.org>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-07 RSB  Adapted from Colossus249/RT8_OP_CODES.agc
# and page images.
# 2009-05-07 RSB  Oops! Left out the entire last page before.
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

# Page 1508
#   BANK 22
#   SETLOC RTBCODES
#   BANK

#   EBANK= XNB
#   COUNT* $$/RTB

# LOAD TIME2, TIME1 INTO MPAC:

W('22,3510', 0o00006, 'LOADTIME', 'EXTEND', line=42)
W('22,3511', 0o30025, '', 'DCA', 'TIME2', line=43)
W('22,3512', 0o16024, '', 'TCF', 'SLOAD2', line=44)

# CONVERT THE SINGLE PRECISION 2'S COMPLEMENT NUMBER ARRIVING IN MPAC (SCALED IN HALF-REVOLUTIONS) TO A
# DP 1'S COMPLEMENT NUMBER SCALED IN REVOLUTIONS.

W('22,3513', 0o10154, 'CDULOGIC', 'CCS', 'MPAC', line=49)
W('22,3514', 0o35021, '', 'CAF', 'ZERO', line=50)
W('22,3515', 0o13520, '', 'TCF', '+3', line=51)
W('22,3516', 0o13517, '', 'NOOP', line=52)
W('22,3517', 0o45002, '', 'CS', 'HALF', line=53)

W('22,3520', 0o54155, '', 'TS', 'MPAC +1', line=55)
W('22,3521', 0o35021, '', 'CAF', 'ZERO', line=56)
W('22,3522', 0o56154, '', 'XCH', 'MPAC', line=57)
W('22,3523', 0o00006, '', 'EXTEND', line=58)
W('22,3524', 0o75002, '', 'MP', 'HALF', line=59)
W('22,3525', 0o20155, '', 'DAS', 'MPAC', line=60)
W('22,3526', 0o16030, '', 'TCF', 'DANZIG', 'MODE IS ALREADY AT DOUBLE-PRECISION', line=61)

# READ THE PIPS INTO MPAC WITHOUT CHANGING THEM:

W('22,3527', 0o00004, 'READPIPS', 'INHINT', line=65)
W('22,3530', 0o30037, '', 'CA', 'PIPAX', line=66)
W('22,3531', 0o54154, '', 'TS', 'MPAC', line=67)
W('22,3532', 0o30040, '', 'CA', 'PIPAY', line=68)
W('22,3533', 0o54157, '', 'TS', 'MPAC +3', line=69)
W('22,3534', 0o30041, '', 'CA', 'PIPAZ', line=70)
W('22,3535', 0o00003, '', 'RELINT', line=71)
W('22,3536', 0o54161, '', 'TS', 'MPAC +5', line=72)

W('22,3537', 0o35021, '', 'CAF', 'ZERO', line=74)
W('22,3540', 0o54155, '', 'TS', 'MPAC +1', line=75)
W('22,3541', 0o54160, '', 'TS', 'MPAC +4', line=76)
W('22,3542', 0o54162, '', 'TS', 'MPAC +6', line=77)

W('22,3543', 0o16470, 'VECMODE', 'TCF', 'VMODE', line=79)

# FORCE TP SIGN AGREEMENT IN MPAC:

W('22,3544', 0o07226, 'SGNAGREE', 'TC', 'TPAGREE', line=83)

# Page 1509

W('22,3545', 0o16030, '', 'TCF', 'DANZIG', line=87)

# CONVERT THE DP 1'S COMPLEMENT ANGLE SCALED IN REVOLUTIONS TO A SINGLE PRECISION 2'S COMPLEMENT ANGLE
# SCALED IN HALF-REVOLUTIONS.

W('22,3546', 0o03576, '1STO2S', 'TC', '1TO2SUB', line=92)
W('22,3547', 0o35021, '', 'CAF', 'ZERO', line=93)
W('22,3550', 0o54155, '', 'TS', 'MPAC +1', line=94)
W('22,3551', 0o16027, '', 'TCF', 'NEWMODE', line=95)

# DO 1STO2S ON A VECTOR OF ANGLES:

W('22,3552', 0o03576, 'V1STO2S', 'TC', '1TO2SUB', 'ANSWER ARRIVES IN A AND MPAC.', line=99)

W('22,3553', 0o52162, '', 'DXCH', 'MPAC +5', line=101)
W('22,3554', 0o52155, '', 'DXCH', 'MPAC', line=102)
W('22,3555', 0o03576, '', 'TC', '1TO2SUB', line=103)
W('22,3556', 0o54156, '', 'TS', 'MPAC +2', line=104)

W('22,3557', 0o52160, '', 'DXCH', 'MPAC +3', line=106)
W('22,3560', 0o52155, '', 'DXCH', 'MPAC', line=107)
W('22,3561', 0o03576, '', 'TC', '1TO2SUB', line=108)
W('22,3562', 0o54155, '', 'TS', 'MPAC +1', line=109)

W('22,3563', 0o30161, '', 'CA', 'MPAC +5', line=111)
W('22,3564', 0o54154, '', 'TS', 'MPAC', line=112)

W('22,3565', 0o35017, 'TPMODE', 'CAF', 'ONE', 'MODE IS TP.', line=114)
W('22,3566', 0o16027, '', 'TCF', 'NEWMODE', line=115)

# V1STO2S FOR 2 COMPONENT VECTOR. USED BY RR.

W('22,3567', 0o03576, '2V1STO2S', 'TC', '1TO2SUB', line=119)
W('22,3570', 0o52160, '', 'DXCH', 'MPAC +3', line=120)
W('22,3571', 0o52155, '', 'DXCH', 'MPAC', line=121)
W('22,3572', 0o03576, '', 'TC', '1TO2SUB', line=122)
W('22,3573', 0o54001, '', 'TS', 'L', line=123)
W('22,3574', 0o30157, '', 'CA', 'MPAC +3', line=124)
W('22,3575', 0o16024, '', 'TCF', 'SLOAD2', line=125)

# SUBROUTINE TO DO DOUBLING AND 1'S TO 2'S CONVERSION:

W('22,3576', 0o52155, '1TO2SUB', 'DXCH', 'MPAC', 'FINAL MPAC +1 UNSPECIFIED.', line=129)
W('22,3577', 0o20001, '', 'DDOUBL', line=130)
W('22,3600', 0o10000, '', 'CCS', 'A', line=131)
W('22,3601', 0o65017, '', 'AD', 'ONE', line=132)
W('22,3602', 0o13604, '', 'TCF', '+2', line=133)
W('22,3603', 0o40000, '', 'COM', '', 'THIS WAS REVERSE OF MSU.', line=134)

W('22,3604', 0o54154, '', 'TS', 'MPAC', 'AND SKIP ON OVERFLOW.', line=136)
# Page 1510
W('22,3605', 0o00002, '', 'TC', 'Q', line=138)

W('22,3606', 0o50000, '', 'INDEX', 'A', 'OVERFLOW UNCORRECT AND IN MSU.', line=140)
W('22,3607', 0o35000, '', 'CAF', 'LIMITS', line=141)
W('22,3610', 0o26154, '', 'ADS', 'MPAC', line=142)
W('22,3611', 0o00002, '', 'TC', 'Q', line=143)

# Page 1511
# SUBROUTINE TO INCREMENT CDUS

W('22,3612', 0o33625, 'INCRCDUS', 'CAF', 'LOCTHETA', line=148)
W('22,3613', 0o54130, '', 'TS', 'BUF', 'PLACE ADRES(THETA) IN BUF.', line=149)
W('22,3614', 0o30154, '', 'CAE', 'MPAC', 'INCREMENT IN 1S COMPL.', line=150)
W('22,3615', 0o03626, '', 'TC', 'CDUINC', line=151)

W('22,3616', 0o24130, '', 'INCR', 'BUF', line=153)
W('22,3617', 0o30157, '', 'CAE', 'MPAC +3', line=154)
W('22,3620', 0o03626, '', 'TC', 'CDUINC', line=155)

W('22,3621', 0o24130, '', 'INCR', 'BUF', line=157)
W('22,3622', 0o30161, '', 'CAE', 'MPAC +5', line=158)
W('22,3623', 0o03626, '', 'TC', 'CDUINC', line=159)

W('22,3624', 0o13543, '', 'TCF', 'VECMODE', line=161)

W('22,3625', 0o01155, 'LOCTHETA', 'ADRES', 'THETAD', kind='data', line=163)

# THE FOLLOWING ROUTINE INCREMENTS IN 2S COMPLEMENT THE REGISTER WHOSE ADDRESS IS IN BUF BY THE 1S COMPL.
# QUANTITY FOUND IN TEM2.  THIS MAY BE USED TO INCREMENT DESIRED IMU AND OPTICS CDU ANGLES OR ANY OTHER 2S COMPL.
# (+0 UNEQUAL TO -0) QUANTITY.  MAY BE CALLED BY BANKCALL/SWCALL.

W('22,3626', 0o54142, 'CDUINC', 'TS', 'TEM2', '1S COMPL.QUANT. ARRIVES IN ACC.  STORE IT', line=169)
W('22,3627', 0o50130, '', 'INDEX', 'BUF', line=170)
W('22,3630', 0o10000, '', 'CCS', '0', 'CHANGE 2S COMPLE. ANGLE(IN BUF) INTO 1S', line=171)
W('22,3631', 0o65017, '', 'AD', 'ONE', line=172)
W('22,3632', 0o13636, '', 'TCF', '+4', line=173)
W('22,3633', 0o65017, '', 'AD', 'ONE', line=174)
W('22,3634', 0o65017, '', 'AD', 'ONE', 'OVEFLOW HERE IF 2S COMPL. IS 180 DEG.', line=175)
W('22,3635', 0o40000, '', 'COM', line=176)

W('22,3636', 0o60142, '', 'AD', 'TEM2', 'SULT MOVES FROM 2ND TO 3D QUAD.(OR BACK)', line=178)
W('22,3637', 0o10000, '', 'CCS', 'A', 'BACK TO 2S COMPL.', line=179)
W('22,3640', 0o65017, '', 'AD', 'ONE', line=180)
W('22,3641', 0o13643, '', 'TCF', '+2', line=181)
W('22,3642', 0o40000, '', 'COM', line=182)
W('22,3643', 0o54142, '', 'TS', 'TEM2', 'STORE 14BIT QUANTITY WITH PRESENT SIGN', line=183)
W('22,3644', 0o13650, '', 'TCF', '+4', line=184)
W('22,3645', 0o50000, '', 'INDEX', 'A', 'SIGN.', line=185)
W('22,3646', 0o35000, '', 'CAF', 'LIMITS', 'FIX IT,BY ADDING IN 37777 OR 40000', line=186)
W('22,3647', 0o60142, '', 'AD', 'TEM2', line=187)

W('22,3650', 0o50130, '', 'INDEX', 'BUF', line=189)
W('22,3651', 0o54000, '', 'TS', '0', 'STORE NEW ANGLE IN 2S COMPLEMENT.', line=190)
W('22,3652', 0o00002, '', 'TC', 'Q', line=191)

# Page 1512
# RTB TO TORQUE GYROS, EXCEPT FOR THE CALL TO IMUSTALL.  ECADR OF COMMANDS ARRIVES IN X1.

W('22,3653', 0o50120, 'PULSEIMU', 'INDEX', 'FIXLOC', 'ADDRESS OF GYRO COMMANDS SHOULD BE IN X1', line=196)
W('22,3654', 0o30046, '', 'CA', 'X1', line=197)
W('22,3655', 0o04662, '', 'TC', 'BANKCALL', line=198)
W('22,3656', 0o17206, '', 'CADR', 'IMUPULSE', kind='data', line=199)
W('22,3657', 0o16030, '', 'TCF', 'DANZIG', line=200)

# Page 1513
# EACH ROUTINE TAKES A 3X3 MATRIX STORED IN DOUBLE PRECISION IN A FIXED AREA OF ERASABLE MEMORY AND REPLACES IT
# WITH THE TRANSPOSE MATRIX.  TRANSP1 USES LOCATIONS XNB+0,+1 THROUGH XNB+16D, 17D AND TRANSP2 USES LOCATIONS
# XNB1+0,+1 THROUGH XNB1+16D, 17D.  EACH MATRIX IS STORED BY ROWS.

W('22,3660', 0o02713, 'XNBEB', 'ECADR', 'XNB', kind='data', line=207)
W('22,3661', 0o02554, 'XNB1EB', 'ECADR', 'XNB1', kind='data', line=208)

#   EBANK= XNB

W('22,3662', 0o33660, 'TRANSP1', 'CAF', 'XNBEB', line=212)
W('22,3663', 0o54003, '', 'TS', 'EBANK', line=213)
W('22,3664', 0o53716, '', 'DXCH', 'XNB +2', line=214)
W('22,3665', 0o53722, '', 'DXCH', 'XNB +6', line=215)
W('22,3666', 0o53716, '', 'DXCH', 'XNB +2', line=216)

W('22,3667', 0o53720, '', 'DXCH', 'XNB +4', line=218)
W('22,3670', 0o53730, '', 'DXCH', 'XNB +12D', line=219)
W('22,3671', 0o53720, '', 'DXCH', 'XNB +4', line=220)

W('22,3672', 0o53726, '', 'DXCH', 'XNB +10D', line=222)
W('22,3673', 0o53732, '', 'DXCH', 'XNB +14D', line=223)
W('22,3674', 0o53726, '', 'DXCH', 'XNB +10D', line=224)
W('22,3675', 0o16030, '', 'TCF', 'DANZIG', line=225)

#   EBANK= XNB1

W('22,3676', 0o33661, 'TRANSP2', 'CAF', 'XNB1EB', line=230)
W('22,3677', 0o54003, '', 'TS', 'EBANK', line=231)
W('22,3700', 0o53557, '', 'DXCH', 'XNB1 +2', line=232)
W('22,3701', 0o53563, '', 'DXCH', 'XNB1 +6', line=233)
W('22,3702', 0o53557, '', 'DXCH', 'XNB1 +2', line=234)

W('22,3703', 0o53561, '', 'DXCH', 'XNB1 +4', line=236)
W('22,3704', 0o53571, '', 'DXCH', 'XNB1 +12D', line=237)
W('22,3705', 0o53561, '', 'DXCH', 'XNB1 +4', line=238)

W('22,3706', 0o53567, '', 'DXCH', 'XNB1 +10D', line=240)
W('22,3707', 0o53573, '', 'DXCH', 'XNB1 +14D', line=241)
W('22,3710', 0o53567, '', 'DXCH', 'XNB1 +10D', line=242)
W('22,3711', 0o16030, '', 'TCF', 'DANZIG', line=243)

# Page 1514
# THE SUBROUTINE SIGNMPAC SETS C(MPAC, MPAC +1) TO SIGN(MPAC).
# FOR THIS, ONLY THE CONTENTS OF MPAC ARE EXAMINED.  ALSO +0 YIELDS POSMAX AND -0 YIELDS NEGMAX.
#
# ENTRY MAY BE BY EITHER OF THE FOLLOWING:
# 1.      LIMIT THE SIZE OF MPAC ON INTERPRETIVE OVERFLOW:
# ENTRY:          BOVB
# SIGNMPAC
# 2.      GENERATE IN MPAC THE SIGNUM FUNCTION OF MPAC:
# ENTRY:          RTB
# SIGNMPAC
# IN EITHER CASE, RETURN IS TO TEH NEXT INTERPRETIVE INSTRUCTION IN THE CALLING SEQUENCE.

W('22,3712', 0o00006, 'SIGNMPAC', 'EXTEND', line=258)
W('22,3713', 0o34777, '', 'DCA', 'DPOSMAX', line=259)
W('22,3714', 0o52155, '', 'DXCH', 'MPAC', line=260)
W('22,3715', 0o10000, '', 'CCS', 'A', line=261)
W('22,3716', 0o35021, 'DPMODE', 'CAF', 'ZERO', 'SETS MPAC +2 TO ZERO IN THE PROCESS', line=262)
W('22,3717', 0o16026, '', 'TCF', 'SLOAD2 +2', line=263)
W('22,3720', 0o13721, '', 'TCF', '+1', line=264)
W('22,3721', 0o00006, '', 'EXTEND', line=265)
W('22,3722', 0o44777, '', 'DCS', 'DPOSMAX', line=266)
W('22,3723', 0o16024, '', 'TCF', 'SLOAD2', line=267)

# RTB OP CODE NORMUNIT IS LIKE INTERPRETIVE INSTRUCTION UNIT, EXCEPT THAT IT CAN BE DEPENDED ON NOT TO BLOW
# UP WHEN THE VECTOR BEING UNITIZED IS VERY SMALL -- IT WILL BLOW UP WHEN ALL COMPONENT ARE ZERO.  IF NORMUNIT
# IS USED AND THE UPPER ORDER HALVES OF ALL COMPONENTS ARE ZERO, THE MAGNITUDE RETURNS IN 36D WILL BE TOO LARGE
# BY A FACTOR OF 2(13) AND THE SQUARED MAGNITUDE RETURNED AT 34D WILL BE TOO BIG BY A FACTOR OF 2(26).

W('22,3724', 0o35017, 'NORMUNX1', 'CAF', 'ONE', line=274)
W('22,3725', 0o13727, '', 'TCF', 'NORMUNIT +1', line=275)
W('22,3726', 0o35021, 'NORMUNIT', 'CAF', 'ZERO', line=276)
W('22,3727', 0o60120, '', 'AD', 'FIXLOC', line=277)
W('22,3730', 0o54156, '', 'TS', 'MPAC +2', line=278)
W('22,3731', 0o04662, '', 'TC', 'BANKCALL', 'GET SIGN AGREEMENT IN ALL COMPONENTS', line=279)
W('22,3732', 0o01010, '', 'CADR', 'VECAGREE', kind='data', line=280)
W('22,3733', 0o10154, '', 'CCS', 'MPAC', line=281)
W('22,3734', 0o13770, '', 'TCF', 'NOSHIFT', line=282)
W('22,3735', 0o13737, '', 'TCF', '+2', line=283)
W('22,3736', 0o13770, '', 'TCF', 'NOSHIFT', line=284)
W('22,3737', 0o10157, '', 'CCS', 'MPAC +3', line=285)
W('22,3740', 0o13770, '', 'TCF', 'NOSHIFT', line=286)
W('22,3741', 0o13743, '', 'TCF', '+2', line=287)
W('22,3742', 0o13770, '', 'TCF', 'NOSHIFT', line=288)
W('22,3743', 0o10161, '', 'CCS', 'MPAC +5', line=289)
W('22,3744', 0o13770, '', 'TCF', 'NOSHIFT', line=290)
W('22,3745', 0o13747, '', 'TCF', '+2', line=291)
W('22,3746', 0o13770, '', 'TCF', 'NOSHIFT', line=292)
# Page 1515
W('22,3747', 0o30155, '', 'CA', 'MPAC +1', 'SHIFT ALL COMPONENTS LEFT 13', line=294)
W('22,3750', 0o00006, '', 'EXTEND', line=295)
W('22,3751', 0o75002, '', 'MP', 'BIT14', line=296)
W('22,3752', 0o20155, '', 'DAS', 'MPAC', 'DAS GAINS A LITTLE ACCURACY', line=297)
W('22,3753', 0o30160, '', 'CA', 'MPAC +4', line=298)
W('22,3754', 0o00006, '', 'EXTEND', line=299)
W('22,3755', 0o75002, '', 'MP', 'BIT14', line=300)
W('22,3756', 0o20160, '', 'DAS', 'MPAC +3', line=301)
W('22,3757', 0o30162, '', 'CA', 'MPAC +6', line=302)
W('22,3760', 0o00006, '', 'EXTEND', line=303)
W('22,3761', 0o75002, '', 'MP', 'BIT14', line=304)
W('22,3762', 0o20162, '', 'DAS', 'MPAC +5', line=305)
W('22,3763', 0o35025, '', 'CAF', 'THIRTEEN', line=306)
W('22,3764', 0o50156, '', 'INDEX', 'MPAC +2', line=307)
W('22,3765', 0o54045, '', 'TS', '37D', line=308)
W('22,3766', 0o04701, 'OFFTUNIT', 'TC', 'POSTJUMP', line=309)
W('22,3767', 0o01024, '', 'CADR', 'UNIT +1', 'SKIP THE "TC VECAGREE" DONE AT UNIT', kind='data', line=310)

W('22,3770', 0o35021, 'NOSHIFT', 'CAF', 'ZERO', line=312)
W('22,3771', 0o13764, '', 'TCF', 'OFFTUNIT -2', line=313)

# RTB VECSGNAG ...FORCES SIGN AGREEMENT OF VECTOR IN MPAC.

W('22,3772', 0o04662, 'VECSGNAG', 'TC', 'BANKCALL', line=317)
W('22,3773', 0o01010, '', 'CADR', 'VECAGREE', kind='data', line=318)
W('22,3774', 0o06030, '', 'TC', 'DANZIG', line=319)

# Page 1516
# MODULE CHANGE FOR NEW LUNAR GRAVITY MODEL
#   SETLOC MODCHG3
#   BANK
W('13,3770', 0o71214, 'QUALITY1', 'BOF', 'DLOAD', kind='interp', line=325)
W('13,3771', 0o00343, '', '', 'MOONFLAG', kind='operand', line=326)
W('13,3772', 0o23220, '', '', 'NBRANCH', kind='operand', line=327)
W('13,3773', 0o00017, '', '', 'URPV', kind='operand', line=328)
W('13,3774', 0o52116, '', 'DSQ', 'GOTO', kind='interp', line=329)
W('13,3775', 0o25754, '', '', 'QUALITY2', kind='operand', line=330)
#   SETLOC MODCHG2
#   BANK
W('12,3754', 0o63525, 'QUALITY2', 'PDDL', 'DSQ', 'SQUARE INTO 2D, B2', kind='interp', line=333)
W('12,3755', 0o00021, '', '', 'URPV +2', 'Y COMPONENT, B1', kind='operand', line=334)
W('12,3756', 0o77625, '', 'DSU', kind='interp', line=335)
W('12,3757', 0o74205, '', 'DMP', 'VXSC', '5(Y**2-X**2)UR', kind='interp', line=336)
W('12,3760', 0o27755, '', '', '5/8', 'CONSTANT, 5B3', kind='operand', line=337)
W('12,3761', 0o00017, '', '', 'URPV', 'VECTOR, RESULT MAXIMUM IS 5, SCALING', kind='operand', line=338)
# HERE B6
W('12,3762', 0o65332, '', 'VSL3', 'PDDL', 'STORE SCALED B3 IN 2D, 4D, 6D FOR XYZ', kind='interp', line=340)
W('12,3763', 0o00017, '', '', 'URPV', 'X COMPONENT, B1', kind='operand', line=341)
W('12,3764', 0o43342, '', 'SR1', 'DAD', '2 X X COMPONENT FOR B3 SCALING', kind='interp', line=342)
W('12,3765', 0o00003, '', '', '2D', 'ADD TO VECTOR X COMPONENT OF ANSWER.', kind='operand', line=343)
# SAME AS MULTIPLYING BY UNITX.  MAX IS 7.
W('12,3766', 0o14003, '', 'STODL', '2D', kind='interp', line=345)
W('12,3767', 0o00021, '', '', 'URPV +2', 'Y COMPONENT, B1', kind='operand', line=346)
W('12,3770', 0o44342, '', 'SR1', 'BDSU', '2 X Y COMPONENT FOR B3 SCALING', kind='interp', line=347)
W('12,3771', 0o00005, '', '', '4D', 'SUBTRACT FROM VECTOR Y COMPONENT OF', kind='operand', line=348)
# ANSWER, SAME AS MULTIPLYING BY UNITY.
# MAX IS 7.
W('12,3772', 0o00005, '', 'STORE', '4D', '2D HAS VECTOR, B3.', kind='interp', line=351)
W('12,3773', 0o74335, '', 'SLOAD', 'VXSC', 'MULTIPLY COEFFICIENT TIMES VECTOR IN 2D', kind='interp', line=352)
W('12,3774', 0o01777, '', '', 'E3J22R2M', kind='operand', line=353)
W('12,3775', 0o43525, '', 'PDDL', 'RVQ', 'J22 TERM X R**4 IN 2D, SCALED B61', kind='interp', line=354)
W('12,3776', 0o00023, '', '', 'COSPHI/2', 'SAME AS URPV +4, Z COMPONENT', kind='operand', line=355)

# *** END OF CHIEFTAN.028 ***
