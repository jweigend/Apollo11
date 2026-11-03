"""KALMAN_FILTER.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/KALMAN_FILTER.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1470-1471 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('KALMAN_FILTER', 'KALMAN_FILTER.agc', 'Luminary099', pages='1470-1471')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     KALMAN_FILTER.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1470-1471
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

# Page 1470
#   EBANK= NO.UJETS
#   BANK 16
#   SETLOC DAPS1
#   BANK

#   COUNT* $$/DAP

W('16,3641', 0o34752, 'RATELOOP', 'CA', 'TWO', line=37)
W('16,3642', 0o55744, '', 'TS', 'DAPTEMP6', line=38)
W('16,3643', 0o60000, '', 'DOUBLE', line=39)
W('16,3644', 0o54002, '', 'TS', 'Q', line=40)
W('16,3645', 0o51744, '', 'INDEX', 'DAPTEMP6', line=41)
W('16,3646', 0o11524, '', 'CCS', 'TJP', line=42)
W('16,3647', 0o13651, '', 'TCF', '+2', line=43)
W('16,3650', 0o13670, '', 'TCF', 'LOOPRATE', line=44)
W('16,3651', 0o63731, '', 'AD', '-100MST6', line=45)
W('16,3652', 0o00006, '', 'EXTEND', line=46)
W('16,3653', 0o63707, '', 'BZMF', 'SMALLTJU', line=47)
W('16,3654', 0o51744, '', 'INDEX', 'DAPTEMP6', line=48)
W('16,3655', 0o11524, '', 'CCS', 'TJP', line=49)
W('16,3656', 0o33731, '', 'CA', '-100MST6', line=50)
W('16,3657', 0o13661, '', 'TCF', '+2', line=51)
W('16,3660', 0o43731, '', 'CS', '-100MST6', line=52)
W('16,3661', 0o51744, '', 'INDEX', 'DAPTEMP6', line=53)
W('16,3662', 0o27524, '', 'ADS', 'TJP', line=54)
W('16,3663', 0o51744, '', 'INDEX', 'DAPTEMP6', line=55)
W('16,3664', 0o11524, '', 'CCS', 'TJP', line=56)
W('16,3665', 0o43615, '', 'CS', '-100MS', '0.1 AT 1', line=57)
W('16,3666', 0o13670, '', 'TCF', '+2', line=58)
W('16,3667', 0o33615, '', 'CA', '-100MS', line=59)
W('16,3670', 0o00006, 'LOOPRATE', 'EXTEND', line=60)
W('16,3671', 0o51744, '', 'INDEX', 'DAPTEMP6', line=61)
W('16,3672', 0o71521, '', 'MP', 'NO.PJETS', line=62)
W('16,3673', 0o30001, '', 'CA', 'L', line=63)
W('16,3674', 0o51744, '', 'INDEX', 'DAPTEMP6', line=64)
W('16,3675', 0o55737, '', 'TS', 'DAPTEMP1', 'SIGNED TORQUE AT 1 JET-SEC FOR FILTER', line=65)
W('16,3676', 0o00006, '', 'EXTEND', line=66)
W('16,3677', 0o74742, '', 'MP', 'BIT10', 'RESCALE TO 32; ONE BIT ABOUT 2 JET-MSEC', line=67)
W('16,3700', 0o00006, '', 'EXTEND', line=68)
W('16,3701', 0o63732, '', 'BZMF', 'NEGTORK', line=69)
W('16,3702', 0o50002, 'STORTORK', 'INDEX', 'Q', 'INCREMENT DOWNLIST REGISTER.', line=70)
W('16,3703', 0o27513, '', 'ADS', 'DOWNTORK', '  NOTE: NOT INITIALIZED; OVERFLOWS.', line=71)

W('16,3704', 0o11744, '', 'CCS', 'DAPTEMP6', line=73)
W('16,3705', 0o13642, '', 'TCF', 'RATELOOP +1', line=74)
W('16,3706', 0o13716, '', 'TCF', 'ROTORQUE', line=75)
W('16,3707', 0o34755, 'SMALLTJU', 'CA', 'ZERO', line=76)
W('16,3710', 0o51744, '', 'INDEX', 'DAPTEMP6', line=77)
W('16,3711', 0o57524, '', 'XCH', 'TJP', line=78)
W('16,3712', 0o00006, '', 'EXTEND', line=79)
# Page 1471
W('16,3713', 0o74760, '', 'MP', 'ELEVEN', '10.24 PLUS', line=81)
W('16,3714', 0o30001, '', 'CA', 'L', line=82)
W('16,3715', 0o13670, '', 'TCF', 'LOOPRATE', line=83)
W('16,3716', 0o31740, 'ROTORQUE', 'CA', 'DAPTEMP2', line=84)
W('16,3717', 0o61741, '', 'AD', 'DAPTEMP3', line=85)
W('16,3720', 0o00006, '', 'EXTEND', line=86)
W('16,3721', 0o71532, '', 'MP', '1JACCR', line=87)
W('16,3722', 0o55747, '', 'TS', 'JETRATER', line=88)
W('16,3723', 0o41741, '', 'CS', 'DAPTEMP3', line=89)
W('16,3724', 0o61740, '', 'AD', 'DAPTEMP2', line=90)
W('16,3725', 0o00006, '', 'EXTEND', line=91)
W('16,3726', 0o71531, '', 'MP', '1JACCQ', line=92)
W('16,3727', 0o55746, '', 'TS', 'JETRATEQ', line=93)
W('16,3730', 0o12316, '', 'TCF', 'BACKP', line=94)
W('16,3731', 0o77537, '-100MST6', 'DEC', '-160', kind='data', line=95)

W('16,3732', 0o40000, 'NEGTORK', 'COM', line=97)
W('16,3733', 0o24002, '', 'INCR', 'Q', line=98)
W('16,3734', 0o13702, '', 'TCF', 'STORTORK', line=99)
