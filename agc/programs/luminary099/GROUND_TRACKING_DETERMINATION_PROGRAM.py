"""GROUND_TRACKING_DETERMINATION_PROGRAM.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/GROUND_TRACKING_DETERMINATION_PROGRAM.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 654-657 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('GROUND_TRACKING_DETERMINATION_PROGRAM', 'GROUND_TRACKING_DETERMINATION_PROGRAM.agc', 'Luminary099', pages='654-657')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     GROUND_TRACKING_DETERMINATION_PROGRAM.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        654-657
# Mod history:  2009-05-18 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
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

# Page 654
# GROUND TRACKING DETERMINATION PROGRAM P21
# PROGRAM DESCRIPTION
# MOD NO - 1
# MOD BY - N.M.NEVILLE
# FUNCTIONAL DECRIPTION-
#
# TO PROVIDE THE ASTRONAUT DETAILS OF THE LM OR CSM GROUND TRACK WITHOUT
# THE NEED FOR GROUND COMMUNICATION (REQUESTED BY DSKY).
# CALLING SEQUENCE -
#
# ASTRONAUT REQUEST THROUGH DSKY V37E21E
# SUBROUTINES CALLED-
#
# GOPERF4
# GOFLASH
# THISPREC
# OTHPREC
# LAT-LONG
# NORMAL EXIT MODES-
#
# ASTRONAUT REQUEST TROUGH DSKY TO TERMINATE PROGRAM V34E
# ALARM OR ABORT EXIT MODES-
#
# NONE
# OUTPUT -
#
# OCTAL DISPLAY OF OPTION CODE AND VEHICLE WHOSE GROUND TRACK IS TO BE
# COMPUTED
# OPTION CODE     00002
# THIS            00001
# OTHER           00002
# DECIMAL DISPLAY OF TIME TO BE INTEGRATED TO HOURS , MINUTES , SECONDS
# DECIMAL DISPLAY OF LAT,LONG,ALT
# ERASABLE INITIALIZATION REQUIRED
#
# AXO           2DEC    4.652459653 E-5         RADIANS         %68-69 CONSTANTS"
#
# -AYO          2DEC    2.147535898 E-5         RADIANS
#
# AZO           2DEC    .7753206164             REVOLUTIONS
# FOR LUNAR ORBITS 504LM VECTOR IS NEEDED
#
# 504LM         2DEC    -2.700340600 E-5        RADIANS
#
# 504LM _2      2DEC    -7.514128400 E-4        RADIANS
#
# 504LM _4      2DEC    _2.553198641 E-4        RADIANS
#
# NONE
# DEBRIS
#
# Page 655
# CENTRALS-A,Q,L
# OTHER-THOSE USED BY THE ABOVE LISTED SUBROUTINES
# SEE LEMPREC,LAT-LONG
#   SBANK= LOWSUPER  # FOR LOW 2CADR'S.

#   BANK 33
#   SETLOC P20S
#   BANK

#   EBANK= P21TIME
#   COUNT* $$/P21
W('24,3505', 0o34753, 'PROG21', 'CAF', 'ONE', line=93)
W('24,3506', 0o55145, '', 'TS', 'OPTION2', 'ASSUMED VEHICLE IS LM , R2 = 00001', line=94)
W('24,3507', 0o34752, '', 'CAF', 'BIT2', ' OPTION 2', line=95)
W('24,3510', 0o04616, '', 'TC', 'BANKCALL', line=96)
W('24,3511', 0o20633, '', 'CADR', 'GOPERF4', kind='data', line=97)
W('24,3512', 0o06001, '', 'TC', 'GOTOPOOH', 'TERMINATE', line=98)
W('24,3513', 0o03515, '', 'TC', '+2', 'PROCEED VALUE OF ASSUMED VEHICLE OK', line=99)
W('24,3514', 0o03507, '', 'TC', '-5', 'R2 LOADED THROUGH DSKY', line=100)
W('24,3515', 0o33665, 'P21PROG1', 'CAF', 'V6N34', 'LOAD DESIRED TIME OF LAT-LONG.', line=101)
W('24,3516', 0o04616, '', 'TC', 'BANKCALL', line=102)
W('24,3517', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=103)
W('24,3520', 0o06001, '', 'TC', 'GOTOPOOH', 'TERM', line=104)
W('24,3521', 0o03523, '', 'TC', '+2', 'PROCEED VALUES OK', line=105)
W('24,3522', 0o03515, '', 'TC', '-5', 'TIME LOADED THROUGH DSKY', line=106)
W('24,3523', 0o06037, '', 'TC', 'INTPRET', line=107)
W('24,3524', 0o77745, '', 'DLOAD', kind='interp', line=108)
W('24,3525', 0o01046, '', '', 'DSPTEM1', kind='operand', line=109)
W('24,3526', 0o34041, '', 'STCALL', 'TDEC1', 'INTEGRATE TO TIME SPECIFIED IN TDEC', kind='interp', line=110)
W('24,3527', 0o27414, '', '', 'INTSTALL', kind='operand', line=111)
W('24,3530', 0o43014, '', 'BON', 'CLEAR', kind='interp', line=112)
W('24,3531', 0o00304, '', '', 'P21FLAG', kind='operand', line=113)
W('24,3532', 0o51550, '', '', 'P21CONT', 'ON---RECYCLE USING BASE VECTOR', kind='operand', line=114)
W('24,3533', 0o01674, '', '', 'VINTFLAG', 'OFF--IST PASS CALL BASE VECTOR', kind='operand', line=115)
W('24,3534', 0o70535, '', 'SLOAD', 'SR1', kind='interp', line=116)
W('24,3535', 0o01146, '', '', 'OPTION2', kind='operand', line=117)
W('24,3536', 0o43030, '', 'BHIZ', 'SET', kind='interp', line=118)
W('24,3537', 0o51541, '', '', '+2', 'ZERO--THIS VEHICLE(LM)', kind='operand', line=119)
W('24,3540', 0o01474, '', '', 'VINTFLAG', 'ONE--OTHER VEHICLE(CM)', kind='operand', line=120)
W('24,3541', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=121)
W('24,3542', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=122)
W('24,3543', 0o01673, '', '', 'INTYPFLG', 'PRECISION', kind='operand', line=123)
W('24,3544', 0o77624, '', 'CALL', kind='interp', line=124)
W('24,3545', 0o27134, '', '', 'INTEGRV', 'CALCULATE', kind='operand', line=125)
W('24,3546', 0o77650, '', 'GOTO', '', '-AND', kind='interp', line=126)
W('24,3547', 0o51571, '', '', 'P21VSAVE', '-SAVE BASE VECTOR', kind='operand', line=127)
W('24,3550', 0o77775, 'P21CONT', 'VLOAD', kind='interp', line=128)
W('24,3551', 0o03676, '', '', 'P21BASER', 'RECYCLE--INTEG FROM BASE VECTOR', kind='operand', line=129)
W('24,3552', 0o25535, '', 'STOVL', 'RCV', '--POS', kind='interp', line=130)
# Page 656
W('24,3553', 0o03704, '', '', 'P21BASEV', kind='operand', line=132)
W('24,3554', 0o15543, '', 'STODL', 'VCV', '--VEL', kind='interp', line=133)
W('24,3555', 0o03763, '', '', 'P21TIME', kind='operand', line=134)
W('24,3556', 0o01517, '', 'STORE', 'TET', '--TIME', kind='interp', line=135)
W('24,3557', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=136)
W('24,3560', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=137)
W('24,3561', 0o00263, '', '', 'MOONFLAG', kind='operand', line=138)
W('24,3562', 0o53135, '', 'SLOAD', 'BZE', kind='interp', line=139)
W('24,3563', 0o01164, '', '', 'P21ORIG', kind='operand', line=140)
W('24,3564', 0o51567, '', '', '+3', 'ZERO=EARTH', kind='operand', line=141)
W('24,3565', 0o77614, '', 'SET', '', '---2=MOON', kind='interp', line=142)
W('24,3566', 0o00063, '', '', 'MOONFLAG', kind='operand', line=143)
W('24,3567', 0o77624, '', 'CALL', kind='interp', line=144)
W('24,3570', 0o27107, '', '', 'INTEGRVS', kind='operand', line=145)
W('24,3571', 0o77745, 'P21VSAVE', 'DLOAD', '', 'SAVE CURRENT BASEVECTOR', kind='interp', line=146)
W('24,3572', 0o00015, '', '', 'TAT', kind='operand', line=147)
W('24,3573', 0o27763, '', 'STOVL', 'P21TIME', '--TIME', kind='interp', line=148)
W('24,3574', 0o00017, '', '', 'RATT1', kind='operand', line=149)
W('24,3575', 0o27676, '', 'STOVL', 'P21BASER', '--POS B-29 OR B-27', kind='interp', line=150)
W('24,3576', 0o00025, '', '', 'VATT1', kind='operand', line=151)
W('24,3577', 0o03704, '', 'STORE', 'P21BASEV', '--VEL B-07 OR B-05', kind='interp', line=152)
W('24,3600', 0o53646, '', 'ABVAL', 'SL*', kind='interp', line=153)
W('24,3601', 0o57576, '', '', '0,2', kind='operand', line=154)
W('24,3602', 0o27712, '', 'STOVL', 'P21VEL', 'VEL/ FOR N91 DISP', kind='interp', line=155)
W('24,3603', 0o00001, '', '', 'RATT', kind='operand', line=156)
W('24,3604', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=157)
W('24,3605', 0o00007, '', '', 'VATT', ' U(R).V', kind='operand', line=158)
W('24,3606', 0o67471, '', 'DDV', 'ASIN', 'U(R).U(V)', kind='interp', line=159)
W('24,3607', 0o03712, '', '', 'P21VEL', kind='operand', line=160)
W('24,3610', 0o03714, '', 'STORE', 'P21GAM', 'SIN-1 U(R).U(V) , -90 TO &90', kind='interp', line=161)
W('24,3611', 0o67334, '', 'SXA,2', 'SLOAD', kind='interp', line=162)
W('24,3612', 0o01163, '', '', 'P21ORIG', '0=EARTH', kind='operand', line=163)
W('24,3613', 0o01146, '', '', 'OPTION2', kind='operand', line=164)
W('24,3614', 0o46142, '', 'SR1', 'BHIZ', kind='interp', line=165)
W('24,3615', 0o51620, '', '', '+3', kind='operand', line=166)
W('24,3616', 0o77650, '', 'GOTO', kind='interp', line=167)
W('24,3617', 0o51623, '', '', '+4', kind='operand', line=168)
W('24,3620', 0o77614, '', 'BON', kind='interp', line=169)
W('24,3621', 0o04307, '', '', 'SURFFLAG', kind='operand', line=170)
W('24,3622', 0o51625, '', '', 'P21DSP', kind='operand', line=171)
W('24,3623', 0o77614, '', 'SET', kind='interp', line=172)
W('24,3624', 0o00064, '', '', 'P21FLAG', kind='operand', line=173)
W('24,3625', 0o67214, 'P21DSP', 'CLEAR', 'SLOAD', 'GENERATE DISPLAY DATA', kind='interp', line=174)
W('24,3626', 0o01663, '', '', 'LUNAFLAG', kind='operand', line=175)
W('24,3627', 0o00050, '', '', 'X2', kind='operand', line=176)
W('24,3630', 0o43054, '', 'BZE', 'SET', kind='interp', line=177)
W('24,3631', 0o51633, '', '', '+2', '0 = EARTH', kind='operand', line=178)
W('24,3632', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=179)
W('24,3633', 0o77775, '', 'VLOAD', kind='interp', line=180)
W('24,3634', 0o00001, '', '', 'RATT', kind='operand', line=181)
# Page 657
W('24,3635', 0o16032, '', 'STODL', 'ALPHAV', kind='interp', line=183)
W('24,3636', 0o00015, '', '', 'TAT', kind='operand', line=184)
W('24,3637', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=185)
W('24,3640', 0o00662, '', '', 'ERADFLAG', kind='operand', line=186)
W('24,3641', 0o26351, '', '', 'LAT-LONG', kind='operand', line=187)
W('24,3642', 0o77605, '', 'DMP', '', 'MPAC = ALT, METERS B-29', kind='interp', line=188)
W('24,3643', 0o11667, '', '', 'K.01', kind='operand', line=189)
W('24,3644', 0o03716, '', 'STORE', 'P21ALT', 'ALT/100 FOR N91 DISP', kind='interp', line=190)
W('24,3645', 0o77776, '', 'EXIT', kind='interp', line=191)
W('24,3646', 0o33664, '', 'CAF', 'V06N43', 'DISPLAY LAT, LONG, ALT', line=192)
W('24,3647', 0o04616, '', 'TC', 'BANKCALL', 'LAT, LONG = 1/2 REVS B0', line=193)
W('24,3650', 0o20476, '', 'CADR', 'GOFLASH', 'ALT = KM B14', kind='data', line=194)
W('24,3651', 0o06001, '', 'TC', 'GOTOPOOH', 'TERM', line=195)
W('24,3652', 0o06001, '', 'TC', 'GOTOPOOH', line=196)
W('24,3653', 0o06037, '', 'TC', 'INTPRET', 'V32E RECYCLE', line=197)
W('24,3654', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=198)
W('24,3655', 0o03763, '', '', 'P21TIME', kind='operand', line=199)
W('24,3656', 0o11663, '', '', '600SEC', '600 SECONDS OR 10 MIN', kind='operand', line=200)
W('24,3657', 0o01046, '', 'STORE', 'DSPTEM1', kind='interp', line=201)
W('24,3660', 0o77634, '', 'RTB', kind='interp', line=202)
W('24,3661', 0o51515, '', '', 'P21PROG1', kind='operand', line=203)
W('24,3662', 0o00003, '600SEC', '2DEC', '60000', '10 MIN', kind='data', line=204)
W('24,3663', 0o25140, kind='data', line=204)

W('24,3664', 0o01453, 'V06N43', 'VN', '00643', kind='data', line=206)
W('24,3665', 0o01442, 'V6N34', 'VN', '00634', kind='data', line=207)
W('24,3666', 0o00243, 'K.01', '2DEC', '.01', kind='data', line=208)
W('24,3667', 0o32703, kind='data', line=208)
