"""STAR_TABLES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/STAR_TABLES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1389-1393 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('STAR_TABLES', 'STAR_TABLES.agc', 'Comanche055', pages='1389-1393')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     STAR_TABLES.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1389-1393
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

# Page 1389
#   BANK 32
#   SETLOC STARTAB
#   BANK

#   COUNT 14/STARS

W('14,3422', 0o15262, '', '2DEC', '+.8342971408 B-1', 'STAR 37       X', kind='data', line=38)
W('14,3423', 0o21773, kind='data', line=38)
W('14,3424', 0o74130, '', '2DEC', '-.2392481515 B-1', 'STAR 37       Y', kind='data', line=39)
W('14,3425', 0o42420, kind='data', line=39)
W('14,3426', 0o70033, '', '2DEC', '-.4966976975 B-1', 'STAR 37       Z', kind='data', line=40)
W('14,3427', 0o41533, kind='data', line=40)

W('14,3430', 0o15014, '', '2DEC', '+.8139832631 B-1', 'STAR 36       X', kind='data', line=42)
W('14,3431', 0o04650, kind='data', line=42)
W('14,3432', 0o67067, '', '2DEC', '-.5557243189 B-1', 'STAR 36       Y', kind='data', line=43)
W('14,3433', 0o60150, kind='data', line=43)
W('14,3434', 0o02551, '', '2DEC', '+.1691204557 B-1', 'STAR 36       Z', kind='data', line=44)
W('14,3435', 0o15723, kind='data', line=44)

W('14,3436', 0o07210, '', '2DEC', '+.4541086270 B-1', 'STAR 35       X', kind='data', line=46)
W('14,3437', 0o01664, kind='data', line=46)
W('14,3440', 0o67276, '', '2DEC', '-.5392368197 B-1', 'STAR 35       Y', kind='data', line=47)
W('14,3441', 0o62232, kind='data', line=47)
W('14,3442', 0o13262, '', '2DEC', '+.7092312789 B-1', 'STAR 35       Z', kind='data', line=48)
W('14,3443', 0o00563, kind='data', line=48)

W('14,3444', 0o05076, '', '2DEC', '+.3201817378 B-1', 'STAR 34       X', kind='data', line=50)
W('14,3445', 0o35561, kind='data', line=50)
W('14,3446', 0o70716, '', '2DEC', '-.4436021946 B-1', 'STAR 34       Y', kind='data', line=51)
W('14,3447', 0o40260, kind='data', line=51)
W('14,3450', 0o62466, '', '2DEC', '-.8370786986 B-1', 'STAR 34       Z', kind='data', line=52)
W('14,3451', 0o64656, kind='data', line=52)

W('14,3452', 0o10652, '', '2DEC', '+.5520184464 B-1', 'STAR 33       X', kind='data', line=54)
W('14,3453', 0o04246, kind='data', line=54)
W('14,3454', 0o63235, '', '2DEC', '-.7933187400 B-1', 'STAR 33       Y', kind='data', line=55)
W('14,3455', 0o44200, kind='data', line=55)
W('14,3456', 0o73710, '', '2DEC', '-.2567508745 B-1', 'STAR 33       Z', kind='data', line=56)
W('14,3457', 0o66230, kind='data', line=56)

W('14,3460', 0o07204, '', '2DEC', '+.4537196908 B-1', 'STAR 32       X', kind='data', line=58)
W('14,3461', 0o33712, kind='data', line=58)
W('14,3462', 0o61747, '', '2DEC', '-.8779508801 B-1', 'STAR 32       Y', kind='data', line=59)
W('14,3463', 0o72343, kind='data', line=59)
W('14,3464', 0o02343, '', '2DEC', '+.1527766153 B-1', 'STAR 32       Z', kind='data', line=60)
W('14,3465', 0o21362, kind='data', line=60)

W('14,3466', 0o03237, '', '2DEC', '+.2069525789 B-1', 'STAR 31       X', kind='data', line=62)
W('14,3467', 0o13301, kind='data', line=62)
W('14,3470', 0o62030, '', '2DEC', '-.8719885748 B-1', 'STAR 31       Y', kind='data', line=63)
W('14,3471', 0o65332, kind='data', line=63)
W('14,3472', 0o70715, '', '2DEC', '-.4436288486 B-1', 'STAR 31       Z', kind='data', line=64)
W('14,3473', 0o71267, kind='data', line=64)

W('14,3474', 0o01745, '', '2DEC', '+.1217293692 B-1', 'STAR 30       X', kind='data', line=66)
W('14,3475', 0o06477, kind='data', line=66)
# Page 1390
W('14,3476', 0o63531, '', '2DEC', '-.7702732847 B-1', 'STAR 30       Y', kind='data', line=68)
W('14,3477', 0o75365, kind='data', line=68)
W('14,3500', 0o12010, '', '2DEC', '+.6259880410 B-1', 'STAR 30       Z', kind='data', line=69)
W('14,3501', 0o03005, kind='data', line=69)

W('14,3502', 0o76146, '', '2DEC', '-.1124304773 B-1', 'STAR 29       X', kind='data', line=71)
W('14,3503', 0o77014, kind='data', line=71)
W('14,3504', 0o60371, '', '2DEC', '-.9694934200 B-1', 'STAR 29       Y', kind='data', line=72)
W('14,3505', 0o75073, kind='data', line=72)
W('14,3506', 0o03370, '', '2DEC', '+.2178116072 B-1', 'STAR 29       Z', kind='data', line=73)
W('14,3507', 0o12003, kind='data', line=73)

W('14,3510', 0o76125, '', '2DEC', '-.1146237858 B-1', 'STAR 28       X', kind='data', line=75)
W('14,3511', 0o40037, kind='data', line=75)
W('14,3512', 0o72436, '', '2DEC', '-.3399692557 B-1', 'STAR 28       Y', kind='data', line=76)
W('14,3513', 0o77062, kind='data', line=76)
W('14,3514', 0o61041, '', '2DEC', '-.9334250333 B-1', 'STAR 28       Z', kind='data', line=77)
W('14,3515', 0o54164, kind='data', line=77)

W('14,3516', 0o72277, '', '2DEC', '-.3516499609 B-1', 'STAR 27       X', kind='data', line=79)
W('14,3517', 0o51044, kind='data', line=79)
W('14,3520', 0o62641, '', '2DEC', '-.8240752703 B-1', 'STAR 27       Y', kind='data', line=80)
W('14,3521', 0o45471, kind='data', line=80)
W('14,3522', 0o70711, '', '2DEC', '-.4441196390 B-1', 'STAR 27       Z', kind='data', line=81)
W('14,3523', 0o70546, kind='data', line=81)

W('14,3524', 0o67364, '', '2DEC', '-.5326876930 B-1', 'STAR 26       X', kind='data', line=83)
W('14,3525', 0o47073, kind='data', line=83)
W('14,3526', 0o64425, '', '2DEC', '-.7160644554 B-1', 'STAR 26       Y', kind='data', line=84)
W('14,3527', 0o77777, kind='data', line=84)
W('14,3530', 0o07157, '', '2DEC', '+.4511047742 B-1', 'STAR 26       Z', kind='data', line=85)
W('14,3531', 0o16322, kind='data', line=85)

W('14,3532', 0o63327, '', '2DEC', '-.7861763936 B-1', 'STAR 25       X', kind='data', line=87)
W('14,3533', 0o64446, kind='data', line=87)
W('14,3534', 0o67515, '', '2DEC', '-.5217996305 B-1', 'STAR 25       Y', kind='data', line=88)
W('14,3535', 0o55266, kind='data', line=88)
W('14,3536', 0o05230, '', '2DEC', '+.3311371675 B-1', 'STAR 25       Z', kind='data', line=89)
W('14,3537', 0o25476, kind='data', line=89)

W('14,3540', 0o64754, '', '2DEC', '-.6898393233 B-1', 'STAR 24       X', kind='data', line=91)
W('14,3541', 0o72604, kind='data', line=91)
W('14,3542', 0o71235, '', '2DEC', '-.4182330640 B-1', 'STAR 24       Y', kind='data', line=92)
W('14,3543', 0o72553, kind='data', line=92)
W('14,3544', 0o66427, '', '2DEC', '-.5909338474 B-1', 'STAR 24       Z', kind='data', line=93)
W('14,3545', 0o42171, kind='data', line=93)

W('14,3546', 0o66546, '', '2DEC', '-.5812035376 B-1', 'STAR 23       X', kind='data', line=95)
W('14,3547', 0o70765, kind='data', line=95)
W('14,3550', 0o73260, '', '2DEC', '-.2909171294 B-1', 'STAR 23       Y', kind='data', line=96)
W('14,3551', 0o71643, kind='data', line=96)
W('14,3552', 0o14121, '', '2DEC', '+.7599800468 B-1', 'STAR 23       Z', kind='data', line=97)
W('14,3553', 0o30153, kind='data', line=97)

W('14,3554', 0o61247, '', '2DEC', '-.9170097662 B-1', 'STAR 22       X', kind='data', line=99)
W('14,3555', 0o73310, kind='data', line=99)
W('14,3556', 0o72313, '', '2DEC', '-.3502146628 B-1', 'STAR 22       Y', kind='data', line=100)
W('14,3557', 0o41247, kind='data', line=100)
# Page 1391
W('14,3560', 0o74744, '', '2DEC', '-.1908999176 B-1', 'STAR 22       Z', kind='data', line=102)
W('14,3561', 0o44566, kind='data', line=102)

W('14,3562', 0o70606, '', '2DEC', '-.4523440203 B-1', 'STAR 21       X', kind='data', line=104)
W('14,3563', 0o54564, kind='data', line=104)
W('14,3564', 0o77153, '', '2DEC', '-.0493710140 B-1', 'STAR 21       Y', kind='data', line=105)
W('14,3565', 0o61536, kind='data', line=105)
W('14,3566', 0o61601, '', '2DEC', '-.8904759346 B-1', 'STAR 21       Z', kind='data', line=106)
W('14,3567', 0o47046, kind='data', line=106)

W('14,3570', 0o60604, '', '2DEC', '-.9525211695 B-1', 'STAR 20       X', kind='data', line=108)
W('14,3571', 0o76224, kind='data', line=108)
W('14,3572', 0o77031, '', '2DEC', '-.0593434796 B-1', 'STAR 20       Y', kind='data', line=109)
W('14,3573', 0o73354, kind='data', line=109)
W('14,3574', 0o73161, '', '2DEC', '-.2986331746 B-1', 'STAR 20       Z', kind='data', line=110)
W('14,3575', 0o63065, kind='data', line=110)

W('14,3576', 0o60431, '', '2DEC', '-.9656605484 B-1', 'STAR 19       X', kind='data', line=112)
W('14,3577', 0o51702, kind='data', line=112)
W('14,3600', 0o00656, '', '2DEC', '+.0525933156 B-1', 'STAR 19       Y', kind='data', line=113)
W('14,3601', 0o33013, kind='data', line=113)
W('14,3602', 0o04044, '', '2DEC', '+.2544280809 B-1', 'STAR 19       Z', kind='data', line=114)
W('14,3603', 0o10627, kind='data', line=114)

W('14,3604', 0o62164, '', '2DEC', '-.8608205219 B-1', 'STAR 18       X', kind='data', line=116)
W('14,3605', 0o45040, kind='data', line=116)
W('14,3606', 0o07325, '', '2DEC', '+.4636213989 B-1', 'STAR 18       Y', kind='data', line=117)
W('14,3607', 0o37443, kind='data', line=117)
W('14,3610', 0o03267, '', '2DEC', '+.2098647835 B-1', 'STAR 18       Z', kind='data', line=118)
W('14,3611', 0o06626, kind='data', line=118)

W('14,3612', 0o63471, '', '2DEC', '-.7742591356 B-1', 'STAR 17       X', kind='data', line=120)
W('14,3613', 0o50471, kind='data', line=120)
W('14,3614', 0o11660, '', '2DEC', '+.6152504197 B-1', 'STAR 17       Y', kind='data', line=121)
W('14,3615', 0o04151, kind='data', line=121)
W('14,3616', 0o75501, '', '2DEC', '-.1482892839 B-1', 'STAR 17       Z', kind='data', line=122)
W('14,3617', 0o46664, kind='data', line=122)

W('14,3620', 0o70430, '', '2DEC', '-.4657947941 B-1', 'STAR 16       X', kind='data', line=124)
W('14,3621', 0o46540, kind='data', line=124)
W('14,3622', 0o07507, '', '2DEC', '+.4774785033 B-1', 'STAR 16       Y', kind='data', line=125)
W('14,3623', 0o20100, kind='data', line=125)
W('14,3624', 0o13727, '', '2DEC', '+.7450164351 B-1', 'STAR 16       Z', kind='data', line=126)
W('14,3625', 0o05455, kind='data', line=126)

W('14,3626', 0o72160, '', '2DEC', '-.3612508532 B-1', 'STAR 15       X', kind='data', line=128)
W('14,3627', 0o64202, kind='data', line=128)
W('14,3630', 0o11144, '', '2DEC', '+.5747270840 B-1', 'STAR 15       Y', kind='data', line=129)
W('14,3631', 0o05203, kind='data', line=129)
W('14,3632', 0o64200, '', '2DEC', '-.7342932655 B-1', 'STAR 15       Z', kind='data', line=130)
W('14,3633', 0o65331, kind='data', line=130)

W('14,3634', 0o71322, '', '2DEC', '-.4118589524 B-1', 'STAR 14       X', kind='data', line=132)
W('14,3635', 0o41512, kind='data', line=132)
W('14,3636', 0o16402, '', '2DEC', '+.9065485360 B-1', 'STAR 14       Y', kind='data', line=133)
W('14,3637', 0o16205, kind='data', line=133)
W('14,3640', 0o01365, '', '2DEC', '+.0924226975 B-1', 'STAR 14       Z', kind='data', line=134)
W('14,3641', 0o04034, kind='data', line=134)

# Page 1392
W('14,3642', 0o75054, '', '2DEC', '-.1820751783 B-1', 'STAR 13       X', kind='data', line=137)
W('14,3643', 0o56052, kind='data', line=137)
W('14,3644', 0o17030, '', '2DEC', '+.9404899869 B-1', 'STAR 13       Y', kind='data', line=138)
W('14,3645', 0o17635, kind='data', line=138)
W('14,3646', 0o73321, '', '2DEC', '-.2869271926 B-1', 'STAR 13       Z', kind='data', line=139)
W('14,3647', 0o57603, kind='data', line=139)

W('14,3650', 0o77010, '', '2DEC', '-.0614937230 B-1', 'STAR 12       X', kind='data', line=141)
W('14,3651', 0o47623, kind='data', line=141)
W('14,3652', 0o11515, '', '2DEC', '+.6031563286 B-1', 'STAR 12       Y', kind='data', line=142)
W('14,3653', 0o01640, kind='data', line=142)
W('14,3654', 0o63215, '', '2DEC', '-.7952489957 B-1', 'STAR 12       Z', kind='data', line=143)
W('14,3655', 0o52176, kind='data', line=143)

W('14,3656', 0o02143, '', '2DEC', '+.1371725575 B-1', 'STAR 11       X', kind='data', line=145)
W('14,3657', 0o26755, kind='data', line=145)
W('14,3660', 0o12715, '', '2DEC', '+.6813721061 B-1', 'STAR 11       Y', kind='data', line=146)
W('14,3661', 0o31470, kind='data', line=146)
W('14,3662', 0o13401, '', '2DEC', '+.7189685267 B-1', 'STAR 11       Z', kind='data', line=147)
W('14,3663', 0o31222, kind='data', line=147)

W('14,3664', 0o03157, '', '2DEC', '+.2011399589 B-1', 'STAR 10       X', kind='data', line=149)
W('14,3665', 0o27504, kind='data', line=149)
W('14,3666', 0o17402, '', '2DEC', '+.9690337941 B-1', 'STAR 10       Y', kind='data', line=150)
W('14,3667', 0o12312, kind='data', line=150)
W('14,3670', 0o75552, '', '2DEC', '-.1432348512 B-1', 'STAR 10       Z', kind='data', line=151)
W('14,3671', 0o63657, kind='data', line=151)

W('14,3672', 0o05471, '', '2DEC', '+.3507315038 B-1', 'STAR 9        X', kind='data', line=153)
W('14,3673', 0o06122, kind='data', line=153)
W('14,3674', 0o16220, '', '2DEC', '+.8926333307 B-1', 'STAR 9        Y', kind='data', line=154)
W('14,3675', 0o16362, kind='data', line=154)
W('14,3676', 0o04417, '', '2DEC', '+.2831839492 B-1', 'STAR 9        Z', kind='data', line=155)
W('14,3677', 0o32762, kind='data', line=155)

W('14,3700', 0o06443, '', '2DEC', '+.4105636020 B-1', 'STAR 8        X', kind='data', line=157)
W('14,3701', 0o12622, kind='data', line=157)
W('14,3702', 0o07766, '', '2DEC', '+.4988110001 B-1', 'STAR 8        Y', kind='data', line=158)
W('14,3703', 0o10237, kind='data', line=158)
W('14,3704', 0o14154, '', '2DEC', '+.7632988371 B-1', 'STAR 8        Z', kind='data', line=159)
W('14,3705', 0o36154, kind='data', line=159)

W('14,3706', 0o13200, '', '2DEC', '+.7032235469 B-1', 'STAR 7        X', kind='data', line=161)
W('14,3707', 0o31653, kind='data', line=161)
W('14,3710', 0o13244, '', '2DEC', '+.7075846047 B-1', 'STAR 7        Y', kind='data', line=162)
W('14,3711', 0o21036, kind='data', line=162)
W('14,3712', 0o01067, '', '2DEC', '+.0692868685 B-1', 'STAR 7        Z', kind='data', line=163)
W('14,3713', 0o23106, kind='data', line=163)

W('14,3714', 0o10560, '', '2DEC', '+.5450107404 B-1', 'STAR 6        X', kind='data', line=165)
W('14,3715', 0o27227, kind='data', line=165)
W('14,3716', 0o10402, '', '2DEC', '+.5314955466 B-1', 'STAR 6        Y', kind='data', line=166)
W('14,3717', 0o00275, kind='data', line=166)
W('14,3720', 0o65477, '', '2DEC', '-.6484410356 B-1', 'STAR 6        Z', kind='data', line=167)
W('14,3721', 0o77044, kind='data', line=167)

W('14,3722', 0o00153, '', '2DEC', '+.0130968840 B-1', 'STAR 5        X', kind='data', line=169)
W('14,3723', 0o11212, kind='data', line=169)
# Page 1393
W('14,3724', 0o00077, '', '2DEC', '+.0078062795 B-1', 'STAR 5        Y', kind='data', line=171)
W('14,3725', 0o36275, kind='data', line=171)
W('14,3726', 0o17777, '', '2DEC', '+.9998837600 B-1', 'STAR 5        Z', kind='data', line=172)
W('14,3727', 0o01417, kind='data', line=172)

W('14,3730', 0o07674, '', '2DEC', '+.4917678276 B-1', 'STAR 4        X', kind='data', line=174)
W('14,3731', 0o21771, kind='data', line=174)
W('14,3732', 0o03416, '', '2DEC', '+.2204887125 B-1', 'STAR 4        Y', kind='data', line=175)
W('14,3733', 0o07626, kind='data', line=175)
W('14,3734', 0o62413, '', '2DEC', '-.8423473935 B-1', 'STAR 4        Z', kind='data', line=176)
W('14,3735', 0o57536, kind='data', line=176)

W('14,3736', 0o07510, '', '2DEC', '+.4775639450 B-1', 'STAR 3        X', kind='data', line=178)
W('14,3737', 0o06414, kind='data', line=178)
W('14,3740', 0o01673, '', '2DEC', '+.1166004340 B-1', 'STAR 3        Y', kind='data', line=179)
W('14,3741', 0o06065, kind='data', line=179)
W('14,3742', 0o15735, '', '2DEC', '+.8708254803 B-1', 'STAR 3        Z', kind='data', line=180)
W('14,3743', 0o31531, kind='data', line=180)

W('14,3744', 0o16745, '', '2DEC', '+.9342640400 B-1', 'STAR 2        X', kind='data', line=182)
W('14,3745', 0o17555, kind='data', line=182)
W('14,3746', 0o02615, '', '2DEC', '+.1735073142 B-1', 'STAR 2        Y', kind='data', line=183)
W('14,3747', 0o13716, kind='data', line=183)
W('14,3750', 0o73010, '', '2DEC', '-.3115219339 B-1', 'STAR 2        Z', kind='data', line=184)
W('14,3751', 0o40311, kind='data', line=184)

W('14,3752', 0o15776, '', '2DEC', '+.8748658918 B-1', 'STAR 1        X', kind='data', line=186)
W('14,3753', 0o34660, kind='data', line=186)
W('14,3754', 0o00325, '', '2DEC', '+.0260879174 B-1', 'STAR 1        Y', kind='data', line=187)
W('14,3755', 0o26625, kind='data', line=187)
W('14,3756', 0o07572, '', '2DEC', '+.4836621670 B-1', 'STAR 1        Z', kind='data', line=188)
W('14,3757', 0o05105, kind='data', line=188)

W('14,3760', 0o15472, 'CATLOG', 'DEC', '6970', kind='data', line=190)
