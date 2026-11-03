"""KEYRUPT_UPRUPT.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/KEYRUPT_UPRUPT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1338-1340 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('KEYRUPT_UPRUPT', 'KEYRUPT_UPRUPT.agc', 'Luminary099', pages='1338-1340')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     KEYRUPT_UPRUPT.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1338-1340
# Mod history:  2009-05-27 RSB  Adapted from the corresponding
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

# Page 1338
#   BANK 14
#   SETLOC KEYRUPT
#   BANK
#   COUNT* $$/KEYUP

W('04,3274', 0o54016, 'KEYRUPT1', 'TS', 'BANKRUPT', line=35)
W('04,3275', 0o56002, '', 'XCH', 'Q', line=36)
W('04,3276', 0o54012, '', 'TS', 'QRUPT', line=37)
W('04,3277', 0o04400, '', 'TC', 'LODSAMPT', 'TIME IS SNATCHED IN RUPT FOR NOUN 65.', line=38)
W('04,3300', 0o34346, '', 'CAF', 'LOW5', line=39)
W('04,3301', 0o00006, '', 'EXTEND', line=40)
W('04,3302', 0o02015, '', 'RAND', 'MNKEYIN', 'CHECK IF KEYS 5M-1M ON', line=41)
W('04,3303', 0o54073, 'KEYCOM', 'TS', 'RUPTREG4', line=42)
W('04,3304', 0o40101, '', 'CS', 'FLAGWRD5', line=43)
W('04,3305', 0o74735, '', 'MASK', 'DSKYFBIT', line=44)
W('04,3306', 0o26101, '', 'ADS', 'FLAGWRD5', line=45)

W('04,3307', 0o34355, 'ACCEPTUP', 'CAF', 'CHRPRIO', '(NOTE: RUPTREG4 = KEYTEMP1)', line=47)
W('04,3310', 0o05072, '', 'TC', 'NOVAC', line=48)
#   EBANK= DSPCOUNT
W('04,3311', 0o02077, '', '2CADR', 'CHARIN', kind='data', line=50)
W('04,3312', 0o60101, kind='data', line=50)

W('04,3313', 0o30073, '', 'CA', 'RUPTREG4', line=52)
W('04,3314', 0o50064, '', 'INDEX', 'LOCCTR', line=53)
W('04,3315', 0o54154, '', 'TS', 'MPAC', 'LEAVE 5 BIT KEY CDE IN MPAC FOR CHARIN', line=54)
W('04,3316', 0o05270, '', 'TC', 'RESUME', line=55)

# Page 1339
# UPRUPT PROGRAM

W('04,3317', 0o54016, 'UPRUPT', 'TS', 'BANKRUPT', line=60)
W('04,3320', 0o56002, '', 'XCH', 'Q', line=61)
W('04,3321', 0o54012, '', 'TS', 'QRUPT', line=62)
W('04,3322', 0o04400, '', 'TC', 'LODSAMPT', 'TIME IS SNATCHED IN RUPT FOR NOUN 65.', line=63)
W('04,3323', 0o34755, '', 'CAF', 'ZERO', line=64)
W('04,3324', 0o56045, '', 'XCH', 'INLINK', line=65)
W('04,3325', 0o54073, '', 'TS', 'KEYTEMP1', line=66)
W('04,3326', 0o34751, '', 'CAF', 'BIT3', 'TURN ON UPACT LIGHT', line=67)
W('04,3327', 0o00006, '', 'EXTEND', '', '(BIT 3 OF CHANNEL 11)', line=68)
W('04,3330', 0o05011, '', 'WOR', 'DSALMOUT', line=69)
W('04,3331', 0o34346, 'UPRPT1', 'CAF', 'LOW5', 'TEST FOR TRIPLE CHAR REDUNDANCY', line=70)
W('04,3332', 0o70073, '', 'MASK', 'KEYTEMP1', 'LOW5 OF WORD', line=71)
W('04,3333', 0o56073, '', 'XCH', 'KEYTEMP1', 'LOW5 INTO KEYTEMP1', line=72)
W('04,3334', 0o00006, '', 'EXTEND', line=73)
W('04,3335', 0o74742, '', 'MP', 'BIT10', 'SHIFT RIGHT 5', line=74)
W('04,3336', 0o54734, '', 'TS', 'KEYTEMP2', line=75)
W('04,3337', 0o74346, '', 'MASK', 'LOW5', 'MID 5', line=76)
W('04,3340', 0o63374, '', 'AD', 'HI10', line=77)
W('04,3341', 0o03371, '', 'TC', 'UPTEST', line=78)
W('04,3342', 0o34742, '', 'CAF', 'BIT10', line=79)
W('04,3343', 0o00006, '', 'EXTEND', line=80)
W('04,3344', 0o70734, '', 'MP', 'KEYTEMP2', 'SHIFT RIGHT 5', line=81)
W('04,3345', 0o74346, '', 'MASK', 'LOW5', 'HIGH 5', line=82)
W('04,3346', 0o40000, '', 'COM', line=83)
W('04,3347', 0o03371, '', 'TC', 'UPTEST', line=84)

W('04,3350', 0o43377, 'UPCK', 'CS', 'ELRCODE', "CODE IS GOOD. IF CODE = 'ERROR RESET',", line=86)
W('04,3351', 0o60073, '', 'AD', 'KEYTEMP1', 'CLEAR UPLOCKFL(SET BIT4 OF FLAGWRD7 = 0)', line=87)
W('04,3352', 0o00006, '', 'EXTEND', '', "IF CODE DOES NOT = 'ERROR RESET', ACCEPT", line=88)
W('04,3353', 0o13361, '', 'BZF', 'CLUPLOCK', 'CODE ONLY IF UPLOCKFL IS CLEAR (=0).', line=89)

W('04,3354', 0o34750, '', 'CAF', 'UPLOCBIT', 'TEST UPLOCKFL FOR 0 OR 1', line=91)
W('04,3355', 0o70103, '', 'MASK', 'FLAGWRD7', line=92)
W('04,3356', 0o10000, '', 'CCS', 'A', line=93)
W('04,3357', 0o05270, '', 'TC', 'RESUME', 'UPLOCKFL = 1', line=94)
W('04,3360', 0o03307, '', 'TC', 'ACCEPTUP', 'UPLOCKFL = 0', line=95)

W('04,3361', 0o44750, 'CLUPLOCK', 'CS', 'UPLOCBIT', 'CLEAR UPLOCKFL (I.E.,SET BIT 4 OF )', line=97)
W('04,3362', 0o70103, '', 'MASK', 'FLAGWRD7', 'FLAGWRD7 = 0)', line=98)
W('04,3363', 0o54103, '', 'TS', 'FLAGWRD7', line=99)
W('04,3364', 0o03307, '', 'TC', 'ACCEPTUP', line=100)

# CODE IS BAD
W('04,3365', 0o40103, 'TMFAIL2', 'CS', 'FLAGWRD7', 'LOCK OUT FURTHER UPLINK ACTIVITY', line=103)
W('04,3366', 0o74750, '', 'MASK', 'UPLOCBIT', '(BY SETTING UPLOCKFL = 1) UNTIL', line=104)
W('04,3367', 0o26103, '', 'ADS', 'FLAGWRD7', "'ERROR RESET' IS SENT VIA UPLINK.", line=105)
W('04,3370', 0o05270, '', 'TC', 'RESUME', line=106)
W('04,3371', 0o60073, 'UPTEST', 'AD', 'KEYTEMP1', line=107)
# Page 1340
W('04,3372', 0o10000, '', 'CCS', 'A', line=109)
W('04,3373', 0o03365, '', 'TC', 'TMFAIL2', line=110)
W('04,3374', 0o77740, 'HI10', 'OCT', '77740', kind='data', line=111)
W('04,3375', 0o03365, '', 'TC', 'TMFAIL2', line=112)
W('04,3376', 0o00002, '', 'TC', 'Q', line=113)

W('04,3377', 0o00022, 'ELRCODE', 'OCT', '22', kind='data', line=115)

# 'UPLINK ACTIVITY LIGHT' IS TURNED OFF BY .....
# 1.     VBRELDSP
# 2.     ERROR RESET
# 3.     UPDATE PROGRAM(P27) ENTERED BY V70,V71,V72,AND V73.
#
# _
# THE RECEPTION OF A BAD CODE(I.E  CCC FAILURE) LOCKS OUT FURTHER UPLINK ACTIVITY BY SETTING BIT4 OF FLAGWRD7 = 1.
# THIS INDICATION WILL BE TRANSFERRED TO THE GROUND BY THE DOWNLINK WHICH DOWNLINKS ALL FLAGWORDS.
# WHEN UPLINK ACTIVITY IS LOCKED OUT ,IT CAN BE ALLOWED WHEN THE GROUND UPLINKS AND 'ERROR RESET' CODE.
# (IT IS RECOMMENDED THAT THE 'ERROR LIGHT RESET' CODE IS PRECEEDED BY 16 BITS THE FIRST OF WHICH IS 1 FOLLOWED
# BY 15 ZEROES. THIS WILL ELIMINATE EXTRANEOUS BITS FROM INLINK WHICH MAY HAVE BEEN LEFT OVER FROM THE ORIGINAL
# FAILURE)
# UPLINK ACTIVITY IS ALSO ALLOWED(UNLOCKED) DURING FRESH START WHEN FRESH START SETS BIT4 OF FLAGWRD7 = 0.
W('04,3400', 0o44753, '', 'CS', 'XDSPBIT', line=130)
