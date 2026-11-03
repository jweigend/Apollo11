"""RTB_OP_CODES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/RTB_OP_CODES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1397-1402 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('RTB_OP_CODES', 'RTB_OP_CODES.agc', 'Luminary099', pages='1397-1402')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     RTB_OP_CODES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1397-1401
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Luminary131/ file of the same
# name, using Luminary099 page images.
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

# Page 1397
#   BANK 22
#   SETLOC RTBCODES
#   BANK

#   EBANK= XNB
#   COUNT* $$/RTB

# LOAD TIME2, TIME1 INTO MPAC:

W('10,3573', 0o00006, 'LOADTIME', 'EXTEND', line=39)
W('10,3574', 0o30025, '', 'DCA', 'TIME2', line=40)
W('10,3575', 0o16055, '', 'TCF', 'SLOAD2', line=41)

# CONVERT THE SINGLE PRECISION 2'S COMPLEMENT NUMBER ARRIVING IN MPAC (SCALED IN HALF-REVOLUTIONS) TO A
# DP 1'S COMPLEMENT NUMBER SCALED IN REVOLUTIONS.

W('10,3576', 0o10154, 'CDULOGIC', 'CCS', 'MPAC', line=46)
W('10,3577', 0o34755, '', 'CAF', 'ZERO', line=47)
W('10,3600', 0o13603, '', 'TCF', '+3', line=48)
W('10,3601', 0o13602, '', 'NOOP', line=49)
W('10,3602', 0o44736, '', 'CS', 'HALF', line=50)

W('10,3603', 0o54155, '', 'TS', 'MPAC +1', line=52)
W('10,3604', 0o34755, '', 'CAF', 'ZERO', line=53)
W('10,3605', 0o56154, '', 'XCH', 'MPAC', line=54)
W('10,3606', 0o00006, '', 'EXTEND', line=55)
W('10,3607', 0o74736, '', 'MP', 'HALF', line=56)
W('10,3610', 0o20155, '', 'DAS', 'MPAC', line=57)
W('10,3611', 0o16061, '', 'TCF', 'DANZIG', 'MODE IS ALREADY AT DOUBLE-PRECISION', line=58)

# FORCE TP SIGN AGREEMENT IN MPAC:

W('10,3612', 0o07257, 'SGNAGREE', 'TC', 'TPAGREE', line=62)
W('10,3613', 0o16061, '', 'TCF', 'DANZIG', line=63)

# CONVERT THE DP 1'S COMPLEMENT ANGLE SCALED IN REVOLUTIONS TO A SINGLE PRECISION 2'S COMPLEMENT ANGLE
# SCALED IN HALF-REVOLUTIONS.

W('10,3614', 0o03644, '1STO2S', 'TC', '1TO2SUB', line=68)
W('10,3615', 0o34755, '', 'CAF', 'ZERO', line=69)
W('10,3616', 0o54155, '', 'TS', 'MPAC +1', line=70)
W('10,3617', 0o16060, '', 'TCF', 'NEWMODE', line=71)

# DO 1STO2S ON A VECTOR OF ANGLES:

W('10,3620', 0o03644, 'V1STO2S', 'TC', '1TO2SUB', 'ANSWER ARRIVES IN A AND MPAC.', line=75)

W('10,3621', 0o52162, '', 'DXCH', 'MPAC +5', line=77)
W('10,3622', 0o52155, '', 'DXCH', 'MPAC', line=78)
W('10,3623', 0o03644, '', 'TC', '1TO2SUB', line=79)
# Page 1398
W('10,3624', 0o54156, '', 'TS', 'MPAC +2', line=81)

W('10,3625', 0o52160, '', 'DXCH', 'MPAC +3', line=83)
W('10,3626', 0o52155, '', 'DXCH', 'MPAC', line=84)
W('10,3627', 0o03644, '', 'TC', '1TO2SUB', line=85)
W('10,3630', 0o54155, '', 'TS', 'MPAC +1', line=86)

W('10,3631', 0o30161, '', 'CA', 'MPAC +5', line=88)
W('10,3632', 0o54154, '', 'TS', 'MPAC', line=89)

W('10,3633', 0o34753, 'TPMODE', 'CAF', 'ONE', 'MODE IS TP.', line=91)
W('10,3634', 0o16060, '', 'TCF', 'NEWMODE', line=92)

# V1STO2S FOR 2 COMPONENT VECTOR. USED BY RR.

W('10,3635', 0o03644, '2V1STO2S', 'TC', '1TO2SUB', line=96)
W('10,3636', 0o52160, '', 'DXCH', 'MPAC +3', line=97)
W('10,3637', 0o52155, '', 'DXCH', 'MPAC', line=98)
W('10,3640', 0o03644, '', 'TC', '1TO2SUB', line=99)
W('10,3641', 0o54001, '', 'TS', 'L', line=100)
W('10,3642', 0o30157, '', 'CA', 'MPAC +3', line=101)
W('10,3643', 0o16055, '', 'TCF', 'SLOAD2', line=102)

# SUBROUTINE TO DO DOUBLING AND 1'S TO 2'S CONVERSION:

W('10,3644', 0o52155, '1TO2SUB', 'DXCH', 'MPAC', 'FINAL MPAC +1 UNSPECIFIED.', line=106)
W('10,3645', 0o20001, '', 'DDOUBL', line=107)
W('10,3646', 0o10000, '', 'CCS', 'A', line=108)
W('10,3647', 0o64753, '', 'AD', 'ONE', line=109)
W('10,3650', 0o13652, '', 'TCF', '+2', line=110)
W('10,3651', 0o40000, '', 'COM', '', 'THIS WAS REVERSE OF MSU.', line=111)

W('10,3652', 0o54154, '', 'TS', 'MPAC', 'AND SKIP ON OVERFLOW.', line=113)
W('10,3653', 0o00002, '', 'TC', 'Q', line=114)

W('10,3654', 0o50000, '', 'INDEX', 'A', 'OVERFLOW UNCORRECT AND IN MSU.', line=116)
W('10,3655', 0o34734, '', 'CAF', 'LIMITS', line=117)
W('10,3656', 0o26154, '', 'ADS', 'MPAC', line=118)
W('10,3657', 0o00002, '', 'TC', 'Q', line=119)

# THE FOLLOWING ROUTINE INCREMENTS IN 2S COMPLEMENT THE REGISTER WHOSE ADDRESS IS IN BUF BY THE 1S COMPL.
# QUANTITY FOUND IN TEM2. THIS MAY BE USED TO INCREMENT DESIRED IMU AND OPTICS CDU ANGLES OR ANY OTHER 2S COMPL.
# (+0 UNEQUAL TO -0) QUANTITY. MAY BE CALLED BY BANKCALL/SWCALL.

W('10,3660', 0o54142, 'CDUINC', 'TS', 'TEM2', '1S COMPL.QUANT. ARRIVES IN ACC. STORE IT', line=125)
W('10,3661', 0o50130, '', 'INDEX', 'BUF', line=126)
W('10,3662', 0o10000, '', 'CCS', '0', 'CHANGE 2S COMPL. ANGLE(IN BUF)INTO 1S', line=127)
W('10,3663', 0o64753, '', 'AD', 'ONE', line=128)
W('10,3664', 0o13670, '', 'TCF', '+4', line=129)
W('10,3665', 0o64753, '', 'AD', 'ONE', line=130)
# Page 1399
W('10,3666', 0o64753, '', 'AD', 'ONE', 'OVERFLOW HERE IF 2S COMPL. IS 180 DEG.', line=132)
W('10,3667', 0o40000, '', 'COM', line=133)

W('10,3670', 0o60142, '', 'AD', 'TEM2', 'SULT MOVES FROM 2ND TO 3D QUAD.(OR BACK)', line=135)
W('10,3671', 0o10000, '', 'CCS', 'A', 'BACK TO 2S COMPL.', line=136)
W('10,3672', 0o64753, '', 'AD', 'ONE', line=137)
W('10,3673', 0o13675, '', 'TCF', '+2', line=138)
W('10,3674', 0o40000, '', 'COM', line=139)
W('10,3675', 0o54142, '', 'TS', 'TEM2', 'STORE 14BIT QUANTITY WITH PRESENT SIGN', line=140)
W('10,3676', 0o13702, '', 'TCF', '+4', line=141)
W('10,3677', 0o50000, '', 'INDEX', 'A', ' SIGN.', line=142)
W('10,3700', 0o34734, '', 'CAF', 'LIMITS', 'FIX IT,BY ADDING IN 37777 OR 40000', line=143)
W('10,3701', 0o60142, '', 'AD', 'TEM2', line=144)

W('10,3702', 0o50130, '', 'INDEX', 'BUF', line=146)
W('10,3703', 0o54000, '', 'TS', '0', 'STORE NEW ANGLE IN 2S COMPLEMENT.', line=147)
W('10,3704', 0o00002, '', 'TC', 'Q', line=148)

# Page 1400
# RTB TO TORQUE GYROS, EXCEPT FOR THE CALL TO IMUSTALL. ECADR OF COMMANDS ARRIVES IN X1.

W('10,3705', 0o50120, 'PULSEIMU', 'INDEX', 'FIXLOC', 'ADDRESS OF GYRO COMMANDS SHOULD BE IN X1', line=153)
W('10,3706', 0o30046, '', 'CA', 'X1', line=154)
W('10,3707', 0o04616, '', 'TC', 'BANKCALL', line=155)
W('10,3710', 0o17323, '', 'CADR', 'IMUPULSE', kind='data', line=156)
W('10,3711', 0o16061, '', 'TCF', 'DANZIG', line=157)

# Page 1401
# THE SUBROUTINE SIGNMPAC  SETS C(MPAC, MPAC +1) TO SIGN(MPAC).
# FOR THIS, ONLY THE CONTENTS OF MPAC ARE EXAMINED.   ALSO +0 YIELDS POSMAX AND -0 YIELDS NEGMAX.
#
# ENTRY MAY BE BY EITHER OF THE FOLLOWING:
# 1.       LIMIT THE SIZE OF MPAC ON INTERPRETIVE OVERFLOW:
# ENTRY:          BOVB
# SIGNMPAC
# 2.       GENERATE IN MPAC THE SIGNUM FUNCTION OF MPAC:
# ENTRY:          RTB
# SIGNMPAC
# IN EITHER CASE, RETURN IS TO  THE NEXT INTERPRETIVE INSTRUCTION IN THE CALLING SEQUENCE.

W('10,3712', 0o00006, 'SIGNMPAC', 'EXTEND', line=172)
W('10,3713', 0o34733, '', 'DCA', 'DPOSMAX', line=173)
W('10,3714', 0o52155, '', 'DXCH', 'MPAC', line=174)
W('10,3715', 0o10000, '', 'CCS', 'A', line=175)
W('10,3716', 0o34755, 'DPMODE', 'CAF', 'ZERO', 'SETS MPAC +2 TO ZERO IN THE PROCESS', line=176)
W('10,3717', 0o16057, '', 'TCF', 'SLOAD2 +2', line=177)
W('10,3720', 0o13721, '', 'TCF', '+1', line=178)
W('10,3721', 0o00006, '', 'EXTEND', line=179)
W('10,3722', 0o44733, '', 'DCS', 'DPOSMAX', line=180)
W('10,3723', 0o16055, '', 'TCF', 'SLOAD2', line=181)

# RTB OP CODE NORMUNIT IS LIKE INTERPRETIVE INSTRUCTION UNIT, EXCEPT THAT IT CAN BE DEPENDED ON NOT TO BLOW
# UP WHEN THE VECTOR BEING UNITIZED IS VERY SMALL -- IT WILL BLOW UP WHEN ALL COMPONENTS ARE ZERO.   IF NORMUNIT
# IS USED AND THE UPPER ORDER HALVES OF ALL COMPONENTS ARE ZERO, THE MAGNITUDE RETURNED IN 36D WILL BE TOO LARGE
# BY A FACTOR OF 2(13) AND THE SQUARED MAGNITUDE RETURNED AT 34D WILL BE TOO BIG BY A FACTOR OF 2(26).

W('10,3724', 0o34753, 'NORMUNX1', 'CAF', 'ONE', line=188)
W('10,3725', 0o13727, '', 'TCF', 'NORMUNIT +1', line=189)
W('10,3726', 0o34755, 'NORMUNIT', 'CAF', 'ZERO', line=190)
W('10,3727', 0o60120, '', 'AD', 'FIXLOC', line=191)
W('10,3730', 0o54156, '', 'TS', 'MPAC +2', line=192)
W('10,3731', 0o04616, '', 'TC', 'BANKCALL', 'GET SIGN AGREEMENT IN ALL COMPONENTS', line=193)
W('10,3732', 0o01010, '', 'CADR', 'VECAGREE', kind='data', line=194)
W('10,3733', 0o10154, '', 'CCS', 'MPAC', line=195)
W('10,3734', 0o13770, '', 'TCF', 'NOSHIFT', line=196)
W('10,3735', 0o13737, '', 'TCF', '+2', line=197)
W('10,3736', 0o13770, '', 'TCF', 'NOSHIFT', line=198)
W('10,3737', 0o10157, '', 'CCS', 'MPAC +3', line=199)
W('10,3740', 0o13770, '', 'TCF', 'NOSHIFT', line=200)
W('10,3741', 0o13743, '', 'TCF', '+2', line=201)
W('10,3742', 0o13770, '', 'TCF', 'NOSHIFT', line=202)
W('10,3743', 0o10161, '', 'CCS', 'MPAC +5', line=203)
W('10,3744', 0o13770, '', 'TCF', 'NOSHIFT', line=204)
W('10,3745', 0o13747, '', 'TCF', '+2', line=205)
W('10,3746', 0o13770, '', 'TCF', 'NOSHIFT', line=206)
# Page 1402
W('10,3747', 0o30155, '', 'CA', 'MPAC +1', 'SHIFT ALL COMPONENTS LEFT 13', line=208)
W('10,3750', 0o00006, '', 'EXTEND', line=209)
W('10,3751', 0o74736, '', 'MP', 'BIT14', line=210)
W('10,3752', 0o20155, '', 'DAS', 'MPAC', 'DAS GAINS A LITTLE ACCURACY', line=211)
W('10,3753', 0o30160, '', 'CA', 'MPAC +4', line=212)
W('10,3754', 0o00006, '', 'EXTEND', line=213)
W('10,3755', 0o74736, '', 'MP', 'BIT14', line=214)
W('10,3756', 0o20160, '', 'DAS', 'MPAC +3', line=215)
W('10,3757', 0o30162, '', 'CA', 'MPAC +6', line=216)
W('10,3760', 0o00006, '', 'EXTEND', line=217)
W('10,3761', 0o74736, '', 'MP', 'BIT14', line=218)
W('10,3762', 0o20162, '', 'DAS', 'MPAC +5', line=219)
W('10,3763', 0o34761, '', 'CAF', 'THIRTEEN', line=220)
W('10,3764', 0o50156, '', 'INDEX', 'MPAC +2', line=221)
W('10,3765', 0o54045, '', 'TS', '37D', line=222)
W('10,3766', 0o04635, 'OFFTUNIT', 'TC', 'POSTJUMP', line=223)
W('10,3767', 0o01024, '', 'CADR', 'UNIT +1', 'SKIP THE "TC VECAGREE" DONE AT UNIT', kind='data', line=224)

W('10,3770', 0o34755, 'NOSHIFT', 'CAF', 'ZERO', line=226)
W('10,3771', 0o13764, '', 'TCF', 'OFFTUNIT -2', line=227)

# RTB VECSGNAG   ...FORCES SIGN AGREEMENT OF VECTOR IN MPAC.

W('10,3772', 0o04616, 'VECSGNAG', 'TC', 'BANKCALL', line=231)
W('10,3773', 0o01010, '', 'CADR', 'VECAGREE', kind='data', line=232)
W('10,3774', 0o06061, '', 'TC', 'DANZIG', line=233)

# *** END OF SKIPPER .087 ***
