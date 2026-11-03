"""CM_BODY_ATTITUDE.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/CM_BODY_ATTITUDE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 883-889 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('CM_BODY_ATTITUDE', 'CM_BODY_ATTITUDE.agc', 'Comanche055', pages='883-889')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     CM_BODY_ATTITUDE.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 883-889
# Contact:      Ron Burkey <info@sandroid.org>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-12 RSB  Adapted from Colossus249 file of the same
# name and Comanche 055 page images.
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

# Page 883
#   BANK 35

#   SETLOC BODYATT
#   BANK

#   COUNT 37/CMBAT

# PDL 12D - 15D SAFE.

# VALUES OF GIMBAL AND BODY ANGLES VALID AT PIP TIME ARE SAVED DURING   READACCS.

#   EBANK= RTINIT  # LET INTERPRETER SET EB

W('37,3470', 0o06006, 'CM/POSE', 'TC', 'INTPRET', 'COME HERE VIA AVEGEXIT.', line=45)

W('37,3471', 0o77201, '', 'SETPD', 'VLOAD', kind='interp', line=47)
W('37,3472', 0o00001, '', '', '0', kind='operand', line=48)
W('37,3473', 0o01177, '', '', 'VN', 'KVSCALE = (12800/ .3048) /2VS', kind='operand', line=49)
W('37,3474', 0o63361, '', 'VXSC', 'PDVL', kind='interp', line=50)
W('37,3475', 0o37767, '', '', '-KVSCALE', 'KVSCALE = .81491944', kind='operand', line=51)
W('37,3476', 0o01714, '', '', 'UNITW', 'FULL UNIT VECTOR', kind='operand', line=52)
W('37,3477', 0o74235, '', 'VXV', 'VXSC', 'VREL = V - WE*R', kind='interp', line=53)
W('37,3500', 0o01760, '', '', 'UNITR', kind='operand', line=54)
W('37,3501', 0o15245, '', '', 'KWE', kind='operand', line=55)
W('37,3502', 0o45455, '', 'VAD', 'STADR', kind='interp', line=56)
W('37,3503', 0o74251, '', 'STORE', '-VREL', 'SAVE FOR ENTRY GUIDANCE.      REF COORDS', kind='interp', line=57)

W('37,3504', 0o72056, '', 'UNIT', 'LXA,1', kind='interp', line=59)
W('37,3505', 0o00044, '', '', '36D', 'ABVAL( -VREL) TO X1', kind='operand', line=60)
W('37,3506', 0o03542, '', 'STORE', 'UXA/2', '-UVREL                        REF COORDS', kind='interp', line=61)

W('37,3507', 0o57435, '', 'VXV', 'VCOMP', kind='interp', line=63)
W('37,3510', 0o01760, '', '', 'UNITR', '.5 UNIT                       REF COORDS', kind='operand', line=64)
W('37,3511', 0o66256, '', 'UNIT', 'SSP', 'THE FOLLOWING IS TO PROVIDE A STABLE', kind='interp', line=65)
W('37,3512', 0o00051, '', '', 'S1', 'UN FOR THE END OF THE TERMINAL PHASE.', kind='operand', line=66)
W('37,3513', 0o00476, 'SPVQUIT', 'DEC', '.019405', '1000/ 2 VS', kind='data', line=67)
W('37,3514', 0o77300, '', 'TIX,1', 'VLOAD', 'IF V-VQUIT POS, BRANCH.', kind='interp', line=68)
W('37,3515', 0o77517, '', '', 'CM/POSE2', 'SAVE UYA IN OLDUYA', kind='operand', line=69)
W('37,3516', 0o03534, '', '', 'OLDUYA', 'OTHERWISE CONTINUE TO USE OLDUYA.', kind='operand', line=70)
W('37,3517', 0o03550, 'CM/POSE2', 'STORE', 'UYA/2', '                              REF COORDS', kind='interp', line=71)

W('37,3520', 0o03534, '', 'STORE', 'OLDUYA', 'RESTORE, OR SAVE AS CASE MAY BE.', kind='interp', line=73)

W('37,3521', 0o57435, '', 'VXV', 'VCOMP', kind='interp', line=75)
W('37,3522', 0o03542, '', '', 'UXA/2', 'FINISH OBTAINING TRAJECTORY TRIAD.', kind='operand', line=76)
W('37,3523', 0o77772, '', 'VSL1', kind='interp', line=77)
W('37,3524', 0o03556, '', 'STORE', 'UZA/2', '                              REF COORDS', kind='interp', line=78)
# Page 884
W('37,3525', 0o77751, '', 'TLOAD', '', 'PICK UP CDUX, CDUY, CDUZ CORRESPONDING', kind='interp', line=80)
W('37,3526', 0o03270, '', '', 'AOG/PIP', 'TO PIPUP TIME IN 2S.C AND SAVE.', kind='operand', line=81)
W('37,3527', 0o14031, 'CM/TRIO', 'STODL', '24D', kind='interp', line=82)
W('37,3530', 0o00032, '', '', '25D', 'AIG/PIP', kind='operand', line=83)

W('37,3531', 0o41434, '', 'RTB', 'PUSH', 'TO PDL0', kind='interp', line=85)
W('37,3532', 0o45513, '', '', 'CDULOGIC', kind='operand', line=86)
W('37,3533', 0o77746, '', 'COS', kind='interp', line=87)
W('37,3534', 0o17564, '', 'STODL', 'UBX/2', 'CI /2', kind='interp', line=88)
# AIG/PIP FROM PDL 0
W('37,3535', 0o57556, '', 'SIN', 'DCOMP', kind='interp', line=90)
W('37,3536', 0o17570, '', 'STODL', 'UBX/2 +4', '-SI /2', kind='interp', line=91)
W('37,3537', 0o00033, '', '', '26D', 'AMG/PIP', kind='operand', line=92)
W('37,3540', 0o41434, '', 'RTB', 'PUSH', 'TO PDL 0', kind='interp', line=93)
W('37,3541', 0o45513, '', '', 'CDULOGIC', kind='operand', line=94)
W('37,3542', 0o65356, '', 'SIN', 'PDDL', 'XCH PDL 0.  SAVE SM /2', kind='interp', line=95)
W('37,3543', 0o65346, '', 'COS', 'PDDL', 'CM /2 TO PDL 2', kind='interp', line=96)
W('37,3544', 0o00001, '', '', '0', 'SM /2', kind='operand', line=97)
W('37,3545', 0o74276, '', 'DCOMP', 'VXSC', kind='interp', line=98)
W('37,3546', 0o03564, '', '', 'UBX/2', kind='operand', line=99)
W('37,3547', 0o77772, '', 'VSL1', '', 'NOISE WONT OVFL.', kind='interp', line=100)
W('37,3550', 0o17572, '', 'STODL', 'UBY/2', '=(-SMCI, NOISE, SMSI)/2', kind='interp', line=101)
W('37,3551', 0o00003, '', '', '2', 'CM /2 REPLACES NOISE', kind='operand', line=102)
W('37,3552', 0o17574, '', 'STODL', 'UBY/2 +2', 'UBY/2=(-SMCI, CM, SMSI)/2', kind='interp', line=103)
W('37,3553', 0o00031, '', '', '24D', 'AOG/PIP', kind='operand', line=104)
W('37,3554', 0o41434, '', 'RTB', 'PUSH', 'TO PDL 4', kind='interp', line=105)
W('37,3555', 0o45513, '', '', 'CDULOGIC', kind='operand', line=106)
W('37,3556', 0o65356, '', 'SIN', 'PDDL', 'XCH PDL 4.  SAVE SO /2', kind='interp', line=107)
W('37,3557', 0o74346, '', 'COS', 'VXSC', 'CO /2', kind='interp', line=108)
W('37,3560', 0o03572, '', '', 'UBY/2', kind='operand', line=109)
W('37,3561', 0o17572, '', 'STODL', 'UBY/2', 'UBY/2=(-COSMCI, COCM, COSMSI)/4', kind='interp', line=110)
W('37,3562', 0o00005, '', '', '4D', 'SO /2', kind='operand', line=111)
W('37,3563', 0o57405, '', 'DMP', 'DCOMP', kind='interp', line=112)
W('37,3564', 0o03570, '', '', 'UBX/2 +4', '-SI /2', kind='operand', line=113)
W('37,3565', 0o77615, '', 'DAD', kind='interp', line=114)
W('37,3566', 0o03572, '', '', 'UBY/2', 'INCREMENT BY (SOSI /4)', kind='operand', line=115)
W('37,3567', 0o17572, '', 'STODL', 'UBY/2', kind='interp', line=116)
# SO /2 FROM PDL 4
W('37,3570', 0o43205, '', 'DMP', 'DAD', kind='interp', line=118)
W('37,3571', 0o03564, '', '', 'UBX/2', 'CI /2', kind='operand', line=119)
W('37,3572', 0o03576, '', '', 'UBY/2 +4', kind='operand', line=120)
W('37,3573', 0o27576, '', 'STOVL', 'UBY/2 +4', 'YB/4                          PLATFORM COORDS', kind='interp', line=121)

# YB = (-COSMCI + SOSI , COCM , COSMSI + SOCI )

W('37,3574', 0o03572, '', '', 'UBY/2', kind='operand', line=125)
W('37,3575', 0o72505, '', 'VXM', 'VSL2', kind='interp', line=126)
W('37,3576', 0o01736, '', '', 'REFSMMAT', '.5 UNIT', kind='operand', line=127)
W('37,3577', 0o17572, '', 'STODL', 'UBY/2', 'YB/2 DONE                     REF COORDS', kind='interp', line=128)
# Page 885
# CM /2 FROM PDL 2
W('37,3600', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=131)
W('37,3601', 0o03564, '', '', 'UBX/2', kind='operand', line=132)
W('37,3602', 0o17564, '', 'STODL', 'UBX/2', '=( CMCI, NOISE, -CMSI)/2', kind='interp', line=133)
W('37,3603', 0o77626, '', 'STADR', '', 'SM /2 FROM PDL 0', kind='interp', line=134)
W('37,3604', 0o50211, '', 'STOVL', 'UBX/2 +2', 'SM /2 REPLACES NOISE', kind='interp', line=135)
W('37,3605', 0o03564, '', '', 'UBX/2', 'XB/2                          PLATFORM COORDS', kind='operand', line=136)

# XB = ( CMCI , SM , -CMSI )

W('37,3606', 0o76505, '', 'VXM', 'VSL1', kind='interp', line=140)
W('37,3607', 0o01736, '', '', 'REFSMMAT', '.5 UNIT', kind='operand', line=141)
W('37,3610', 0o03564, '', 'STORE', 'UBX/2', 'XB/2 DONE                     REF COORDS', kind='interp', line=142)

W('37,3611', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=144)
W('37,3612', 0o03572, '', '', 'UBY/2', kind='operand', line=145)
W('37,3613', 0o27600, '', 'STOVL', 'UBZ/2', 'ZB/2 DONE                     REF COORDS', kind='interp', line=146)

# EQUIVALENT TO
# ZB = ( SOSMCI + COSI , -SOCM , -SOSMSI + COCI)

W('37,3614', 0o03542, '', '', 'UXA/2', '-UVREL/2 = -UVA/2', kind='operand', line=151)
W('37,3615', 0o53435, '', 'VXV', 'UNIT', 'GET UNIT(-UVREL*UBY)/2 = UL/2', kind='interp', line=152)
W('37,3616', 0o03572, '', '', 'UBY/2', 'YB/2', kind='operand', line=153)
W('37,3617', 0o50206, '', 'PUSH', 'DOT', 'UL/2 TO PDL 0,5', kind='interp', line=154)
W('37,3620', 0o03556, '', '', 'UZA/2', 'UNA/2', kind='operand', line=155)
W('37,3621', 0o24021, '', 'STOVL', 'COSTH', 'COS(ROLL)/4', kind='interp', line=156)
W('37,3622', 0o00001, '', '', '0', 'UL/2', kind='operand', line=157)

W('37,3623', 0o77641, '', 'DOT', kind='interp', line=159)
W('37,3624', 0o03550, '', '', 'UYA/2', kind='operand', line=160)
W('37,3625', 0o34023, '', 'STCALL', 'SINTH', '-SIN(ROLL)/4', kind='interp', line=161)
W('37,3626', 0o47256, '', '', 'ARCTRIG', kind='operand', line=162)
W('37,3627', 0o24007, '', 'STOVL', '6D', '-(ROLL/180) /2', kind='interp', line=163)
W('37,3630', 0o03572, '', '', 'UBY/2', kind='operand', line=164)
W('37,3631', 0o72441, '', 'DOT', 'SL1', '-UVA.UBY = -SIN(BETA)', kind='interp', line=165)
W('37,3632', 0o03542, '', '', 'UXA/2', '-UVREL/2', kind='operand', line=166)
W('37,3633', 0o77736, '', 'ARCSIN', kind='interp', line=167)
W('37,3634', 0o24010, '', 'STOVL', '7D', '-(BETA/180) /2', kind='interp', line=168)
W('37,3635', 0o03564, '', '', 'UBX/2', 'XB/2', kind='operand', line=169)
W('37,3636', 0o77641, '', 'DOT', '', 'UL.UBX = -SIN(ALFA)', kind='interp', line=170)
W('37,3637', 0o00001, '', '', '0', 'UL/2', kind='operand', line=171)
W('37,3640', 0o24023, '', 'STOVL', 'SINTH', '-SIN(ALFA)/4', kind='interp', line=172)
W('37,3641', 0o77641, '', 'DOT', '', 'UL/2 FROM PDL 0', kind='interp', line=173)
W('37,3642', 0o03600, '', '', 'UBZ/2', kind='operand', line=174)
W('37,3643', 0o34021, '', 'STCALL', 'COSTH', 'COS(ALFA)/2', kind='interp', line=175)
W('37,3644', 0o47256, '', '', 'ARCTRIG', kind='operand', line=176)
W('37,3645', 0o24011, '', 'STOVL', '8D', '-(ALFA/180) /2', kind='interp', line=177)
W('37,3646', 0o01760, '', '', 'UNITR', 'UR/2                          REF COORDS', kind='operand', line=178)
W('37,3647', 0o72441, '', 'DOT', 'SL1', kind='interp', line=179)
# Page 886
W('37,3650', 0o03556, '', '', 'UZA/2', 'MORE ACCURATE AT LARGE ARG.', kind='operand', line=181)
W('37,3651', 0o77726, '', 'ARCCOS', kind='interp', line=182)
W('37,3652', 0o00013, '', 'STORE', '10D', '(-GAMA/180)/2', kind='interp', line=183)

W('37,3653', 0o77551, '', 'TLOAD', 'EXIT', 'ANGLES IN MPAC IN THE ORDER', kind='interp', line=185)
# -( (ROLL, BETA, ALFA) /180)/2
W('37,3654', 0o00007, '', '', '6D', 'THESE VALUES CORRECT AT PIPUP TIME.', kind='operand', line=187)

# Page 887
# BASIC SUBROUTINE TO UPDATE ATTITUDE ANGLES

#   EBANK= AOG

W('37,3655', 0o35057, 'CM/ATUP', 'CA', 'EBAOG', line=194)
W('37,3656', 0o54003, '', 'TS', 'EBANK', line=195)
W('37,3657', 0o50120, 'CMTR1', 'INDEX', 'FIXLOC', line=196)
W('37,3660', 0o40012, '', 'CS', '10D', '(GAMA/180)/2', line=197)
W('37,3661', 0o57722, '', 'XCH', 'GAMA', line=198)
W('37,3662', 0o54001, '', 'TS', 'L', line=199)

W('37,3663', 0o00004, '', 'INHINT', line=201)
# MUST REMAIN INHINTED UNTIL UPDATE OF BODY
# ANGLES, SO THAT GAMDIFSW IS VALID FIRST PASS
# INDICATOR.

W('37,3664', 0o40102, '', 'CS', 'CM/FLAGS', line=206)
W('37,3665', 0o75005, '', 'MASK', 'BIT11', 'GAMDIFSW=94D BIT11    INITLY=0', line=207)
W('37,3666', 0o00006, '', 'EXTEND', '', 'DONT CALC GAMA DOT UNTIL HAVE FORMD', line=208)
# ONE DIFFERENCE.
W('37,3667', 0o13672, '', 'BZF', 'DOGAMDOT', 'IS OK, GO ON.', line=210)
W('37,3670', 0o26102, '', 'ADS', 'CM/FLAGS', 'KNOW BIT IS 0', line=211)
W('37,3671', 0o03705, '', 'TC', 'NOGAMDOT', 'SET GAMDOT = 0', line=212)

W('37,3672', 0o40001, 'DOGAMDOT', 'CS', 'L', line=214)
W('37,3673', 0o61722, '', 'AD', 'GAMA', 'DEL GAMA/360= T GAMDOT/360', line=215)
W('37,3674', 0o00006, '', 'EXTEND', line=216)
W('37,3675', 0o73770, '', 'MP', 'TCDU', 'TCDU = .1 SEC, T = 2 SEC.', line=217)
W('37,3676', 0o55723, '', 'TS', 'GAMDOT', 'GAMA DOT TCDU / 180', line=218)

W('37,3677', 0o00006, '', 'EXTEND', '', 'IGNORE GAMDOT IF LEQ .5 DEG/SEC', line=220)
W('37,3700', 0o63702, '', 'BZMF', '+2', line=221)
W('37,3701', 0o40000, '', 'COM', line=222)
W('37,3702', 0o65022, '', 'AD', 'FIVE', line=223)
W('37,3703', 0o00006, '', 'EXTEND', line=224)
W('37,3704', 0o63707, '', 'BZMF', '+3', 'SET GAMDOT=+0 AS TAG IF TOO SMALL.', line=225)

W('37,3705', 0o35021, 'NOGAMDOT', 'CA', 'ZERO', 'COME HERE INHINTED.', line=227)
W('37,3706', 0o55723, '', 'TS', 'GAMDOT', line=228)
# FOR NOW LEAVE IN 2S.C
# UPDATE ANGLES BY CORRECTING EUILER ANG
# FOR ACCRUED INCREMENT SINCE PIPUP
# R = R EUIL + R(NOW) -R(PIPUP)
W('37,3707', 0o40154, '', 'CS', 'MPAC', 'GET (R EUL/180) /2', line=233)
W('37,3710', 0o60000, '', 'DOUBLE', '', 'POSSIBLE OVERFLOW', line=234)
W('37,3711', 0o03760, '', 'TC', 'CORANGOV', 'CORRECT FOR OVFL IF ANY', line=235)
W('37,3712', 0o00006, '', 'EXTEND', line=236)
W('37,3713', 0o61672, '', 'SU', 'ROLL/PIP', 'GET INCR SINCE PIPUP', line=237)
W('37,3714', 0o61664, '', 'AD', 'ROLL/180', 'ONLY SINGLE OVFL POSSIBLE.', line=238)
W('37,3715', 0o03760, '', 'TC', 'CORANGOV', 'CORRECT FOR OVFL IF ANY', line=239)
# Page 888
W('37,3716', 0o55770, '', 'TS', 'TEMPROLL', line=241)

W('37,3717', 0o40156, '', 'CS', 'MPAC +2', 'GET (ALFA EUL/180) /2', line=243)
W('37,3720', 0o60000, '', 'DOUBLE', '', 'SAME AS FOR ROLL.  NEEDED FOR EXT ATM DAP', line=244)
W('37,3721', 0o03760, '', 'TC', 'CORANGOV', 'CORRECT FOR OVFL IF ANY', line=245)
W('37,3722', 0o00006, '', 'EXTEND', line=246)
W('37,3723', 0o61673, '', 'SU', 'ALFA/PIP', line=247)
W('37,3724', 0o61665, '', 'AD', 'ALFA/180', line=248)
W('37,3725', 0o03760, '', 'TC', 'CORANGOV', 'CORRECT FOR OVFL IF ANY', line=249)
W('37,3726', 0o55771, '', 'TS', 'TEMPALFA', line=250)

W('37,3727', 0o40155, '', 'CS', 'MPAC +1', 'GET (BETA EUL/180) /2', line=252)
W('37,3730', 0o60000, 'CMTR2', 'DOUBLE', line=253)
W('37,3731', 0o00006, '', 'EXTEND', line=254)
W('37,3732', 0o61674, '', 'SU', 'BETA/PIP', line=255)
W('37,3733', 0o61666, '', 'AD', 'BETA/180', line=256)
W('37,3734', 0o57772, '', 'XCH', 'TEMPBETA', 'OVFL NOT EXPECTED.', line=257)

W('37,3735', 0o35051, '', 'CA', 'EBANK3', line=259)
W('37,3736', 0o54003, '', 'TS', 'EBANK', line=260)

#   EBANK= PHSNAME5
W('37,3737', 0o00006, '', 'EXTEND', line=263)
W('37,3740', 0o33772, '', 'DCA', 'REPOSADR', 'THIS ASSUMES THAT THE         TC  PHASCHNG', line=264)
W('37,3741', 0o53447, '', 'DXCH', 'PHSNAME5', 'IS NOT CHANGED IN             OCT 10035', line=265)
# SERVICER.

W('37,3742', 0o35057, '', 'CA', 'EBAOG', line=268)
W('37,3743', 0o54003, '', 'TS', 'EBANK', line=269)

#   EBANK= AOG
W('37,3744', 0o00006, 'REDOPOSE', 'EXTEND', '', 'RE-STARTS COME HERE', line=272)
W('37,3745', 0o31771, '', 'DCA', 'TEMPROLL', line=273)
W('37,3746', 0o53665, '', 'DXCH', 'ROLL/180', line=274)
W('37,3747', 0o31772, '', 'CA', 'TEMPBETA', line=275)
W('37,3750', 0o55666, '', 'TS', 'BETA/180', line=276)

W('37,3751', 0o00003, '', 'RELINT', line=278)

W('37,3752', 0o06006, '', 'TC', 'INTPRET', 'CANT TC DANZIG AFTER PHASCHNG.', line=280)
W('37,3753', 0o51575, 'CM/POSE3', 'VLOAD', 'ABVAL', 'RETURN FROM CM/ATUP.  (RESTART)', kind='interp', line=281)
W('37,3754', 0o01177, '', '', 'VN', '2(-7) M/CS', kind='operand', line=282)
W('37,3755', 0o03723, '', 'STORE', 'VMAGI', 'FOR DISPLAY ON CALL.', kind='interp', line=283)

W('37,3756', 0o77650, '', 'GOTO', kind='interp', line=285)
W('37,3757', 0o03324, '', '', 'POSEXIT', 'ENDEXIT, STARTENT, OR SCALEPOP.', kind='operand', line=286)

W('37,3760', 0o54001, 'CORANGOV', 'TS', 'L', line=288)
W('37,3761', 0o00002, '', 'TC', 'Q', line=289)
W('37,3762', 0o50000, '', 'INDEX', 'A', line=290)
# Page 889
W('37,3763', 0o35000, '', 'CA', 'LIMITS', line=292)
W('37,3764', 0o26001, '', 'ADS', 'L', line=293)
W('37,3765', 0o00002, '', 'TC', 'Q', 'COSTS 2 MCT TO USE.  SEE ANGOVCOR.', line=294)

W('37,3766', 0o45730, '-KVSCALE', '2DEC', '-.81491944', '-12800/(2 VS .3048)', kind='data', line=296)
W('37,3767', 0o53410, kind='data', line=296)

W('37,3770', 0o03146, 'TCDU', 'DEC', '.1', 'TCDU = .1 SEC.', kind='data', line=298)

#   EBANK= AOG
W('37,3771', 0o03744, 'REPOSADR', '2CADR', 'REDOPOSE', kind='data', line=301)
W('37,3772', 0o76066, kind='data', line=301)
