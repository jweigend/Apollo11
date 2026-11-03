"""KEYRUPT_UPRUPT.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/KEYRUPT_UPRUPT.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1449-1451 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('KEYRUPT_UPRUPT', 'KEYRUPT_UPRUPT.agc', 'Comanche055', pages='1449-1451')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     KEYRUPT_UPRUPT.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 1449-1451
# Contact:      Ron Burkey <info@sandroid.org>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-07 RSB  Adapted from Colossus249 file of the same
# name, and page images. Corrected various
# typos in the transcription of program
# comments, and these should be back-ported
# to Colossus249.
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

# Page 1449
#   BANK 14
#   SETLOC KEYRUPT
#   BANK
#   COUNT* $$/KEYUP

W('07,3673', 0o54016, 'KEYRUPT1', 'TS', 'BANKRUPT', line=40)
W('07,3674', 0o56002, '', 'XCH', 'Q', line=41)
W('07,3675', 0o54012, '', 'TS', 'QRUPT', line=42)
W('07,3676', 0o04414, '', 'TC', 'LODSAMPT', 'TIME IS SNATCHED IN RUPT FOR NOUN 65.', line=43)
W('07,3677', 0o34362, '', 'CAF', 'LOW5', line=44)
W('07,3700', 0o00006, '', 'EXTEND', line=45)
W('07,3701', 0o02015, '', 'RAND', 'MNKEYIN', 'CHECK IF KEYS 5M-1M ON', line=46)
W('07,3702', 0o54073, 'KEYCOM', 'TS', 'RUPTREG4', line=47)
W('07,3703', 0o40101, '', 'CS', 'FLAGWRD5', line=48)
W('07,3704', 0o75001, '', 'MASK', 'BIT15', line=49)
W('07,3705', 0o26101, '', 'ADS', 'FLAGWRD5', line=50)

W('07,3706', 0o34371, 'ACCEPTUP', 'CAF', 'CHRPRIO', '(NOTE: RUPTREG4 = KEYTEMP1)', line=52)
W('07,3707', 0o05134, '', 'TC', 'NOVAC', line=53)
#   EBANK= DSPCOUNT
W('07,3710', 0o02000, '', '2CADR', 'CHARIN', kind='data', line=55)
W('07,3711', 0o60101, kind='data', line=55)

W('07,3712', 0o30073, '', 'CA', 'RUPTREG4', line=57)
W('07,3713', 0o50064, '', 'INDEX', 'LOCCTR', line=58)
W('07,3714', 0o54154, '', 'TS', 'MPAC', 'LEAVE 5 BIT KEY CDE IN MPAC FOR CHARIN', line=59)
W('07,3715', 0o05333, '', 'TC', 'RESUME', line=60)

# Page 1450
# UPRUPT PROGRAM

W('07,3716', 0o54016, 'UPRUPT', 'TS', 'BANKRUPT', line=65)
W('07,3717', 0o56002, '', 'XCH', 'Q', line=66)
W('07,3720', 0o54012, '', 'TS', 'QRUPT', line=67)
W('07,3721', 0o04414, '', 'TC', 'LODSAMPT', 'TIME IS SNATCHED IN RUPT FOR NOUN 65.', line=68)
W('07,3722', 0o35021, '', 'CAF', 'ZERO', line=69)
W('07,3723', 0o56045, '', 'XCH', 'INLINK', line=70)
W('07,3724', 0o54073, '', 'TS', 'KEYTEMP1', line=71)
W('07,3725', 0o35015, '', 'CAF', 'BIT3', 'TURN ON UPACT LIGHT', line=72)
W('07,3726', 0o00006, '', 'EXTEND', '', '(BIT 3 OF CHANNEL 11)', line=73)
W('07,3727', 0o05011, '', 'WOR', 'DSALMOUT', line=74)
W('07,3730', 0o34362, 'UPRPT1', 'CAF', 'LOW5', 'TEST FOR TRIPLE CHAR REDUNDANCY', line=75)
W('07,3731', 0o70073, '', 'MASK', 'KEYTEMP1', 'LOW5 OF WORD', line=76)
W('07,3732', 0o56073, '', 'XCH', 'KEYTEMP1', 'LOW5 INTO KEYTEMP1', line=77)
W('07,3733', 0o00006, '', 'EXTEND', line=78)
W('07,3734', 0o75006, '', 'MP', 'BIT10', 'SHIFT RIGHT 5', line=79)
W('07,3735', 0o54734, '', 'TS', 'KEYTEMP2', line=80)
W('07,3736', 0o74362, '', 'MASK', 'LOW5', 'MID 5', line=81)
W('07,3737', 0o63773, '', 'AD', 'HI10', line=82)
W('07,3740', 0o03770, '', 'TC', 'UPTEST', line=83)
W('07,3741', 0o35006, '', 'CAF', 'BIT10', line=84)
W('07,3742', 0o00006, '', 'EXTEND', line=85)
W('07,3743', 0o70734, '', 'MP', 'KEYTEMP2', 'SHIFT RIGHT 5', line=86)
W('07,3744', 0o74362, '', 'MASK', 'LOW5', 'HIGH 5', line=87)
W('07,3745', 0o40000, '', 'COM', line=88)
W('07,3746', 0o03770, '', 'TC', 'UPTEST', line=89)

W('07,3747', 0o43776, 'UPOK', 'CS', 'ELRCODE', "CODE IS GOOD. IF CODE = 'ERROR RESET',", line=91)
W('07,3750', 0o60073, '', 'AD', 'KEYTEMP1', 'CLEAR UPLOCKFL(SET BIT4 OF FLAGWRD7 = 0)', line=92)
W('07,3751', 0o00006, '', 'EXTEND', '', "IF CODE DOES NOT = 'ERROR RESET', ACCEPT", line=93)
W('07,3752', 0o13760, '', 'BZF', 'CLUPLOCK', 'CODE ONLY IF UPLOCKFL IS CLEAR (=0).', line=94)

W('07,3753', 0o35014, '', 'CAF', 'BIT4', 'TEST UPLOCKFL FOR 0 OR 1.', line=96)
W('07,3754', 0o70103, '', 'MASK', 'FLAGWRD7', line=97)
W('07,3755', 0o10000, '', 'CCS', 'A', line=98)
W('07,3756', 0o05333, '', 'TC', 'RESUME', 'UPLOCKFL = 1', line=99)
W('07,3757', 0o03706, '', 'TC', 'ACCEPTUP', 'UPLOCKFL = 0', line=100)

W('07,3760', 0o45014, 'CLUPLOCK', 'CS', 'BIT4', 'CLEAR UPLOCKFL (I.E., SET BIT 4 OF', line=102)
W('07,3761', 0o70103, '', 'MASK', 'FLAGWRD7', 'FLAGWRD7 = 0)', line=103)
W('07,3762', 0o54103, '', 'TS', 'FLAGWRD7', line=104)
W('07,3763', 0o03706, '', 'TC', 'ACCEPTUP', line=105)

# CODE IS BAD
W('07,3764', 0o40103, 'TMFAIL2', 'CS', 'FLAGWRD7', 'LOCK OUT FURTHER UPLINK ACTIVITY', line=108)
W('07,3765', 0o75014, '', 'MASK', 'BIT4', '(BY SETTING UPLOCKFL = 1) UNTIL', line=109)
W('07,3766', 0o26103, '', 'ADS', 'FLAGWRD7', "'ERROR RESET' IS SENT VIA UPLINK.", line=110)
W('07,3767', 0o05333, '', 'TC', 'RESUME', line=111)
W('07,3770', 0o60073, 'UPTEST', 'AD', 'KEYTEMP1', line=112)
# Page 1451
W('07,3771', 0o10000, '', 'CCS', 'A', line=114)
W('07,3772', 0o03764, '', 'TC', 'TMFAIL2', line=115)
W('07,3773', 0o77740, 'HI10', 'OCT', '77740', kind='data', line=116)
W('07,3774', 0o03764, '', 'TC', 'TMFAIL2', line=117)
W('07,3775', 0o00002, '', 'TC', 'Q', line=118)

W('07,3776', 0o00022, 'ELRCODE', 'OCT', '22', kind='data', line=120)

# 'UPLINK ACTIVITY LIGHT' IS TURNED OFF BY .....
# 1.      VBRELDSP
# 2.      ERROR RESET
# 3.      UPDATE PROGRAM(P27) ENTERED BY V70,V71,V72,AND V73.
#
#
# -
# THE RECEPTION OF A BAD CODE(I.E. CCC FAILURE) LOCKS OUT FURTHER UPLINK ACTIVITY BY SETTING BIT4 OF FLAGWRD7 = 1.
# THIS INDICATION WILL BE TRANSFERRED TO THE GROUND BY THE DOWNLINK WHICH DOWNLINKS ALL FLAGWORDS.
# WHEN UPLINK ACTIVITY IS LOCKED OUT ,IT CAN BE ALLOWED WHEN THE GROUND UPLINKS AND 'ERROR RESET' CODE.
# (IT IS RECOMMENDED THAT THE 'ERROR LIGHT RESET' CODE IS PRECEEDED BY 16 BITS THE FIRST OF WHICH IS 1 FOLLOWED
# BY 15 ZEROS. THIS WILL ELIMINATE EXTRANEOUS BITS FROM INLINK WHICH MAY HAVE BEEN LEFT OVER FROM THE ORIGINAL
# FAILURE).
# UPLINK ACTIVITY IS ALSO ALLOWED(UNLOCKED) DURING FRESH START WHEN FRESH START SETS BIT4 OF FLAGWRD7 = 0.
