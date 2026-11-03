"""FIXED_FIXED_CONSTANT_POOL.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/FIXED_FIXED_CONSTANT_POOL.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1095-1099 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('FIXED_FIXED_CONSTANT_POOL', 'FIXED_FIXED_CONSTANT_POOL.agc', 'Luminary099', pages='1095-1099')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     FIXED_FIXED_CONSTANT_POOL.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1095-1099
# Mod history:  2009-05-25 RSB  Adapted from the corresponding
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

# Page 1095
#   BLOCK 02

#   COUNT* $$/FCONS
# THE FOLLOWING TABLE OF 18 VALUES IS INDEXED. DO NOT INSERT OR REMOVE ANY QUANTITIES

W('4732', 0o37777, 'DPOSMAX', 'OCT', '37777', 'MUST PRECEDE POSMAX', kind='data', line=35)
W('4733', 0o37777, 'POSMAX', 'OCT', '37777', kind='data', line=36)

S('LIMITS', 'equals', 0o4734, line=38)

W('4734', 0o57777, 'NEG1/2', 'OCT', '-20000', 'USED BY SIN ROUTINE (MUST BE TWO', kind='data', line=40)
# LOCATIONS IN FRONT OF BIT14)

# BIT TABLE

W('4735', 0o40000, 'BIT15', 'OCT', '40000', kind='data', line=45)
W('4736', 0o20000, 'BIT14', 'OCT', '20000', kind='data', line=46)
W('4737', 0o10000, 'BIT13', 'OCT', '10000', kind='data', line=47)
W('4740', 0o04000, 'BIT12', 'OCT', '04000', kind='data', line=48)
W('4741', 0o02000, 'BIT11', 'OCT', '02000', kind='data', line=49)
W('4742', 0o01000, 'BIT10', 'OCT', '01000', kind='data', line=50)
W('4743', 0o00400, 'BIT9', 'OCT', '00400', kind='data', line=51)
W('4744', 0o00200, 'BIT8', 'OCT', '00200', kind='data', line=52)
W('4745', 0o00100, 'BIT7', 'OCT', '00100', kind='data', line=53)
W('4746', 0o00040, 'BIT6', 'OCT', '00040', kind='data', line=54)
W('4747', 0o00020, 'BIT5', 'OCT', '00020', kind='data', line=55)
W('4750', 0o00010, 'BIT4', 'OCT', '00010', kind='data', line=56)
W('4751', 0o00004, 'BIT3', 'OCT', '00004', kind='data', line=57)
W('4752', 0o00002, 'BIT2', 'OCT', '00002', kind='data', line=58)
W('4753', 0o00001, 'BIT1', 'OCT', '00001', kind='data', line=59)

# DO NOT DESTROY THIS COMBINATION, SINCE IT IS USED IN DOUBLE PRECISION INSTRUCTIONS.
W('4754', 0o77777, 'NEG0', 'OCT', '-0', 'MUST PRECEDE ZERO', kind='data', line=62)
W('4755', 0o00000, 'ZERO', 'OCT', '0', 'MUST FOLLOW NEG0', kind='data', line=63)
# BIT1          OCT     00001
# NO.WDS        OCT     2               # INTERPRETER
# OCTAL3        OCT     3               # INTERPRETER
# R3D1          OCT     4               # PINBALL
W('4756', 0o00005, 'FIVE', 'OCT', '5', kind='data', line=68)
# REVCNT        OCT     6               # INTERPRETER
W('4757', 0o00007, 'SEVEN', 'OCT', '7', kind='data', line=70)
# BIT4          OCT     00010
# R2D1          OCT     11              # PINBALL
S('OCT11', 'equals', 0o4320, line=73)  # P20S
# BINCON        DEC     10              # PINBALL            (OCTAL 12)
W('4760', 0o00013, 'ELEVEN', 'DEC', '11', kind='data', line=75)
# OCT14         OCT     14              # ALARM AND ABORT (FILLER)
W('4761', 0o00015, 'OCT15', 'OCT', '15', kind='data', line=77)
# R1D1          OCT     16              # PINBALL
W('4762', 0o00017, 'LOW4', 'OCT', '17', kind='data', line=79)
# Page 1096
# BIT5          OCT     00020
# ND1           OCT     21              # PINBALL
# VD1           OCT     23              # PINBALL
# OCT24         OCT     24              # SERVICE ROUTINES
# MD1           OCT     25              # PINBALL
W('4763', 0o00030, 'BITS4&5', 'OCT', '30', kind='data', line=86)
# OCT31         OCT     31              # SERVICE ROUTINES
W('4764', 0o00033, 'OCT33', 'OCT', '33', kind='data', line=88)
S('DEC27', 'equals', 0o4764, line=89)
W('4765', 0o00035, 'OCT35', 'OCT', '35', kind='data', line=90)
S('DEC29', 'equals', 0o4765, line=91)
W('4766', 0o00032, 'CALLCODE', 'OCT', '00032', kind='data', line=92)
# LOW5          OCT     37              # PINBALL
# 33DEC         DEC     33              # PINBALL            (OCTAL 41)
# 34DEC         DEC     34              # PINBALL            (OCTAL 42)
W('4767', 0o00045, 'TBUILDFX', 'DEC', '37', 'BUILDUP FOR CONVIENCE IN DAPTESTING', kind='data', line=96)
W('4770', 0o00046, 'TDECAYFX', 'DEC', '38', 'CONVENIENCE FOR DAPTESTING', kind='data', line=97)
# BIT6          OCT     00040
W('4771', 0o00050, 'OCT50', 'OCT', '50', kind='data', line=99)
W('4772', 0o00055, 'DEC45', 'DEC', '45', kind='data', line=100)
W('4773', 0o00060, 'SUPER011', 'OCT', '60', 'BITS FOR SUPERBNK SETTING 011.', kind='data', line=101)
W('4774', 0o00062, '.5SEC', 'DEC', '50', kind='data', line=102)
# BIT7          OCT     00100

S('SUPER100', 'equals', 0o4745, line=105)  # BITS FOR SUPERBNK SETTING 100
# (LAST 4K OF ROPE)
W('4775', 0o00120, 'SUPER101', 'OCT', '120', 'BITS FOR SUPERBNK SETTING 101', kind='data', line=107)
# OCT121        OCT     121             # SERVICE ROUTINES
# (FIRST 8K OF ACM)
W('4776', 0o00140, 'SUPER110', 'OCT', '140', 'BITS FOR SUPERBNK SETTING 110.', kind='data', line=110)
# (LAST 8K OF ACM)
W('4777', 0o00144, '1SEC', 'DEC', '100', kind='data', line=112)
# LOW7          OCT     177             # INTERPRETER
# BIT8          OCT     00200
# OT215         OCT     215             # ALARM AND ABORT
# 8,5           OCT     00220           # P20-P25 SUNDANCE
W('5000', 0o00310, '2SECS', 'DEC', '200', kind='data', line=117)
# LOW8          OCT     377             # PINBALL
# BIT9          OCT     00400
W('5001', 0o00401, 'GN/CCODE', 'OCT', '00401', 'SET S/C CONTROL SWITCH TO G/N', kind='data', line=120)
W('5002', 0o00454, '3SECS', 'DEC', '300', kind='data', line=121)
W('5003', 0o00620, '4SECS', 'DEC', '400', kind='data', line=122)
W('5004', 0o00777, 'LOW9', 'OCT', '777', kind='data', line=123)
# BIT10         OCT     01000
# 5.5DEGS       DEC     .03056          # P20-P25 SUNDANCE   (OCTAL 00765)
# OCT1103       OCT     1103            # ALARM AND ABORT
W('5005', 0o01124, 'C5/2', 'DEC', '.0363551', '                   (OCTAL 01124)', kind='data', line=127)
W('5006', 0o01211, 'V05N09', 'VN', '0509', '(SAME AS OCTAL 1211)', kind='data', line=128)
W('5007', 0o01400, 'OCT1400', 'OCT', '01400', kind='data', line=129)
W('5010', 0o01426, 'V06N22', 'VN', '0622', kind='data', line=130)
# Page 1097
# MID5          OCT     1740            # PINBALL
W('5011', 0o01776, 'BITS2-10', 'OCT', '1776', kind='data', line=133)
W('5012', 0o01777, 'LOW10', 'OCT', '1777', kind='data', line=134)
# BIT11         OCT     02000
# 2K+3          OCT     2003            # PINBALL
W('5013', 0o02177, 'LOW7+2K', 'OCT', '2177', 'OP CODE MASK + BANK 1 FBANK SETTING.', kind='data', line=137)
W('5014', 0o02400, 'EBANK5', 'OCT', '02400', kind='data', line=138)
W('5015', 0o03000, 'PRIO3', 'OCT', '03000', kind='data', line=139)
W('5016', 0o03400, 'EBANK7', 'OCT', '03400', kind='data', line=140)
# LOW11         OCT     3777            # PINBALL
# BIT12         OCT     04000
# RELTAB        OCT     04025           # T4RUPT
W('5017', 0o05000, 'PRIO5', 'OCT', '05000', kind='data', line=144)
W('5020', 0o06000, 'PRIO6', 'OCT', '06000', kind='data', line=145)
W('5021', 0o07000, 'PRIO7', 'OCT', '07000', kind='data', line=146)

# BIT13         OCT     10000
# OCT     10003           # T4RUPT     RELTAB +1D
# 13,7,2        OCT     10102           # P20-P25 SUNDANCE
W('5022', 0o11000, 'PRIO11', 'OCT', '11000', kind='data', line=151)
# PRIO12        OCT     12000           # BANKCALL
W('5023', 0o13000, 'PRIO13', 'OCT', '13000', kind='data', line=153)
W('5024', 0o14000, 'PRIO14', 'OCT', '14000', kind='data', line=154)
# OCT     14031           # T4RUPT     RELTAB +2D
W('5025', 0o15000, 'PRIO15', 'OCT', '15000', kind='data', line=156)
W('5026', 0o16000, 'PRIO16', 'OCT', '16000', kind='data', line=157)
# 85DEGS        DEC     .45556          # P20-P25 SUNDANCE   (OCTAL 16450)
W('5027', 0o17000, 'PRIO17', 'OCT', '17000', kind='data', line=159)
W('5030', 0o17770, 'OCT17770', 'OCT', '17770', kind='data', line=160)
# BIT14         OCT     20000
# OCT     20033           # T4RUPT     RELTAB +3D
W('5031', 0o21000, 'PRIO21', 'OCT', '21000', kind='data', line=163)
#   BLOCK 03
#   COUNT* $$/FCONS
W('7710', 0o22000, 'PRIO22', 'OCT', '22000', 'SERVICE ROUTINES', kind='data', line=166)
W('7711', 0o23000, 'PRIO23', 'OCT', '23000', kind='data', line=167)
W('7712', 0o24000, 'PRIO24', 'OCT', '24000', kind='data', line=168)
# 5/8+1         OCT     24001           # SINGLE PRECISION SUBROUTINES
# OCT     24017           # T4RUPT     RELTAB +4D
W('7713', 0o25000, 'PRIO25', 'OCT', '25000', kind='data', line=171)
W('7714', 0o26000, 'PRIO26', 'OCT', '26000', kind='data', line=172)
W('7715', 0o27000, 'PRIO27', 'OCT', '27000', kind='data', line=173)
# CHRPRIO       OCT     30000           # PINBALL
# OCT     30036           # T4RUPT     RELTAB +5D
W('7716', 0o31000, 'PRIO31', 'OCT', '31000', kind='data', line=176)
W('7717', 0o31103, 'C1/2', 'DEC', '.7853134', '                   (OCTAL 31103)', kind='data', line=177)
W('7720', 0o32000, 'PRIO32', 'OCT', '32000', kind='data', line=178)
W('7721', 0o33000, 'PRIO33', 'OCT', '33000', kind='data', line=179)
W('7722', 0o34000, 'PRIO34', 'OCT', '34000', kind='data', line=180)
# OCT     34034           # T4RUPT     RELTAB +6D
# Page 1098
W('7723', 0o35000, 'PRIO35', 'OCT', '35000', kind='data', line=183)
W('7724', 0o36000, 'PRIO36', 'OCT', '36000', kind='data', line=184)
W('7725', 0o37000, 'PRIO37', 'OCT', '37000', kind='data', line=185)
W('7726', 0o37401, '63/64+1', 'OCT', '37401', kind='data', line=186)
# MID7          OCT     37600           # PINBALL
W('7727', 0o37766, 'OCT37766', 'OCT', '37766', kind='data', line=188)
W('7730', 0o37774, 'OCT37774', 'OCT', '37774', kind='data', line=189)
W('7731', 0o37776, 'OCT37776', 'OCT', '37776', kind='data', line=190)
# DPOSMAX       OCT     37777
# BIT15         OCT     40000
# OCT40001      OCT     40001           # INTERPRETER  ( CS   1   INSTRUCTION)
W('7732', 0o40014, 'DLOADCOD', 'OCT', '40014', kind='data', line=194)
W('7733', 0o40015, 'DLOAD*', 'OCT', '40015', kind='data', line=195)
# OCT     40023           # T4RUPT     RELTAB +7D
W('7734', 0o40040, 'BIT15+6', 'OCT', '40040', kind='data', line=197)
W('7735', 0o40200, 'OCT40200', 'OCT', '40200', kind='data', line=198)
# OCT     44035           # T4RUPT    RELTAB +8D
# OCT     50037           # T4RUPT     RELTAB +9D
# OCT     54000           # T4RUPT     RELTAB +10D
W('7736', 0o57777, '-BIT14', 'OCT', '57777', kind='data', line=202)
# RELTAB11      OCT     60000           # T4RUPT
W('7737', 0o65552, 'C3/2', 'DEC', '-.3216147', '                   (OCTAL 65552)', kind='data', line=204)
W('7740', 0o70000, '13,14,15', 'OCT', '70000', kind='data', line=205)
W('7741', 0o73777, '-1/8', 'OCT', '73777', kind='data', line=206)
W('7742', 0o74000, 'HIGH4', 'OCT', '74000', kind='data', line=207)
W('7743', 0o74056, '-ENDERAS', 'DEC', '-2001', '                   (OCTAL 74056)', kind='data', line=208)
# HI5           OCT     76000           # PINBALL
W('7744', 0o77700, 'HIGH9', 'OCT', '77700', kind='data', line=210)
# -ENDVAC       DEC     -45             # INTERPRETER        (OCTAL 77722)
# -OCT10        OCT     -10             #                     (OCT 77767)
# NEG4          DEC     -4              #                    (OCTAL 77773)
W('7745', 0o77774, 'NEG3', 'DEC', '-3', kind='data', line=214)
W('7746', 0o77775, 'NEG2', 'OCT', '77775', kind='data', line=215)
W('7747', 0o77776, 'NEGONE', 'DEC', '-1', kind='data', line=216)

# Page 1099

# DEFINED BY EQUALS

# IT WOULD BE TO THE USERS ADVANTAGE TO OCCASIONALLY CHECK ANY OF THESE SYMBOLS IN ORDER TO PREVENT ANY
# ACCIDENTAL DEFINITION CHANGES.

S('MINUS1', 'equals', 0o7747, line=225)
S('NEG1', 'equals', 0o7747, line=226)
S('ONE', 'equals', 0o4753, line=227)
S('TWO', 'equals', 0o4752, line=228)
S('THREE', 'equals', 0o6245, line=229)
S('LOW2', 'equals', 0o6245, line=230)
S('FOUR', 'equals', 0o4751, line=231)
S('SIX', 'equals', 0o6242, line=232)
S('LOW3', 'equals', 0o4757, line=233)
S('EIGHT', 'equals', 0o4750, line=234)
S('NINE', 'equals', 0o4320, line=235)
S('TEN', 'equals', 0o4363, line=236)
S('NOUTCON', 'equals', 0o4760, line=237)
S('OCT23', 'equals', 0o4360, line=238)
S('OCT25', 'equals', 0o4362, line=239)
S('PRIO1', 'equals', 0o4742, line=240)
S('EBANK3', 'equals', 0o5007, line=241)
S('PRIO2', 'equals', 0o4741, line=242)
S('OCT120', 'equals', 0o4775, line=243)
S('OCT140', 'equals', 0o4776, line=244)
S('2K', 'equals', 0o4741, line=245)
S('EBANK4', 'equals', 0o4741, line=246)
S('PRIO4', 'equals', 0o4740, line=247)
S('EBANK6', 'equals', 0o5015, line=248)
S('QUARTER', 'equals', 0o4737, line=249)
S('PRIO10', 'equals', 0o4737, line=250)
S('OCT10001', 'equals', 0o7663, line=251)
S('POS1/2', 'equals', 0o4736, line=252)
S('PRIO20', 'equals', 0o4736, line=253)
S('HALF', 'equals', 0o4736, line=254)
S('PRIO30', 'equals', 0o4355, line=255)
S('BIT13-14', 'equals', 0o4355, line=256)  # INTERPRETER USES IN PROCESSING STORECODE
S('OCT30002', 'equals', 0o6471, line=257)
S('B12T14', 'equals', 0o7722, line=258)
S('NEGMAX', 'equals', 0o4735, line=259)
S('VLOADCOD', 'equals', 0o4735, line=260)
S('VLOAD*', 'equals', 0o6107, line=261)
S('OCT60000', 'equals', 0o4101, line=262)
S('BANKMASK', 'equals', 0o4350, line=263)
