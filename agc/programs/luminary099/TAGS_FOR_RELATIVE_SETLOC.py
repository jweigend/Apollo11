"""TAGS_FOR_RELATIVE_SETLOC.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/TAGS_FOR_RELATIVE_SETLOC.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 28-37 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TAGS_FOR_RELATIVE_SETLOC', 'TAGS_FOR_RELATIVE_SETLOC.agc', 'Luminary099', pages='28-37')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TAGS_FOR_RELATIVE_SETLOC.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
#
# Assembler:    yaYUL
# Contact:      Jim Lawton <jim.lawton@gmail.com>
# Website:      www.ibiblio.org/apollo.
# Pages:        028-037
# Mod history:  2009-05-16      JVL     Transcribed from page images.
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
# Assemble revision 001 of AGC program LMY99 by NASA 2021112-061
# 16:27 JULY 14, 1969

# Page 28
# TAGS FOR RELATIVE SETLOC AND BLANK BANK CARDS

# COUNT   BANKSUM

# MODULE 1 CONTAINS BANKS 0 THROUGH 5

#   BLOCK 02
S('RADARFF', 'equals', 0o4000, line=35)
S('FFTAG1', 'equals', 0o4000, line=36)
S('FFTAG2', 'equals', 0o4000, line=37)
S('FFTAG3', 'equals', 0o4000, line=38)
S('FFTAG4', 'equals', 0o4000, line=39)
S('FFTAG7', 'equals', 0o4000, line=40)
S('FFTAG8', 'equals', 0o4000, line=41)
S('FFTAG9', 'equals', 0o4000, line=42)
S('FFTAG10', 'equals', 0o4000, line=43)
S('FFTAG11', 'equals', 0o4000, line=44)
S('FFTAG12', 'equals', 0o4000, line=45)
S('FFTAG13', 'equals', 0o4000, line=46)
#   BNKSUM 02

#   BLOCK 03
S('FFTAG5', 'equals', 0o6000, line=50)
S('FFTAG6', 'equals', 0o6000, line=51)
#   BNKSUM 03

#   BANK 00
S('DLAYJOB', 'equals', 0o10000, line=55)
#   BNKSUM 00

#   BANK 01
S('RESTART', 'equals', 0o12000, line=59)
S('LOADDAP1', 'equals', 0o12000, line=60)
#   BNKSUM 01

#   BANK 04
S('R02', 'equals', 0o20000, line=64)
S('VERB37', 'equals', 0o20000, line=65)
S('PINBALL4', 'equals', 0o20000, line=66)
S('CONICS1', 'equals', 0o20000, line=67)
S('KEYRUPT', 'equals', 0o20000, line=68)
S('R36LM', 'equals', 0o20000, line=69)
S('UPDATE2', 'equals', 0o20000, line=70)
S('E/PROG', 'equals', 0o20000, line=71)
S('AOTMARK2', 'equals', 0o20000, line=72)
#   BNKSUM 04

# Page 29
#   BANK 05
S('FRANDRES', 'equals', 0o22000, line=77)
S('DOWNTELM', 'equals', 0o22000, line=78)
S('ABORTS1', 'equals', 0o22000, line=79)
S('EPHEM1', 'equals', 0o22000, line=80)
S('ASENT3', 'equals', 0o22000, line=81)
#   BNKSUM 05

# MODULE 2 CONTAINS BANKS 6 THROUGH 13

#   BANK 06
S('IMUCOMP', 'equals', 0o24000, line=87)
S('T4RUP', 'equals', 0o24000, line=88)
S('RCSMONT', 'equals', 0o24000, line=89)
S('MIDDGIM', 'equals', 0o24000, line=90)
S('EARTHLOC', 'equals', 0o24000, line=91)
#   BNKSUM 06

#   BANK 07
S('AOTMARK1', 'equals', 0o26000, line=95)
S('MODESW', 'equals', 0o26000, line=96)
S('ASENT2', 'equals', 0o26000, line=97)
#   BNKSUM 07

#   BANK 10
S('RTBCODES', 'equals', 0o30000, line=101)
S('DISPLAYS', 'equals', 0o30000, line=102)
S('PHASETAB', 'equals', 0o30000, line=103)
S('FLESHLOC', 'equals', 0o30000, line=104)
S('SLCTMU', 'equals', 0o30000, line=105)
#   BNKSUM 10

#   BANK 11
S('ORBITAL', 'equals', 0o32000, line=109)
S('F2DPS*11', 'equals', 0o32000, line=110)
S('INTVEL', 'equals', 0o32000, line=111)
#   BNKSUM 11

#   BANK 12
S('CONICS', 'equals', 0o34000, line=115)
S('ORBITAL1', 'equals', 0o34000, line=116)
# Page 30
S('INTPRET2', 'equals', 0o34000, line=118)
#   BNKSUM 12

#   BANK 13
S('LATLONG', 'equals', 0o36000, line=122)
S('INTINIT', 'equals', 0o36000, line=123)
S('LEMGEOM', 'equals', 0o36000, line=124)
S('P76LOC', 'equals', 0o36000, line=125)
S('ORBITAL2', 'equals', 0o36000, line=126)
S('ABTFLGS', 'equals', 0o36000, line=127)
#   BNKSUM 13

# Page 31
# MODULE 3 CONTAINS BANKS 14 THROUGH 21

#   BANK 14
S('P50S1', 'equals', 0o40000, line=134)
S('STARTAB', 'equals', 0o40000, line=135)
S('ASENT4', 'equals', 0o40000, line=136)
#   BNKSUM 14

#   BANK 15
S('P50S', 'equals', 0o42000, line=140)
S('EPHEM', 'equals', 0o42000, line=141)
#   BNKSUM 15

#   BANK 16
S('DAPS1', 'equals', 0o44000, line=145)
#   BNKSUM 16

#   BANK 17
S('DAPS2', 'equals', 0o46000, line=149)
S('P40S3', 'equals', 0o46000, line=150)
#   BNKSUM 17

#   BANK 20
S('DAPS3', 'equals', 0o50000, line=154)
S('LOADDAP', 'equals', 0o50000, line=155)
S('RODTRAP', 'equals', 0o50000, line=156)
#   BNKSUM 20

#   BANK 21
S('DAPS4', 'equals', 0o52000, line=160)
S('R10', 'equals', 0o52000, line=161)
S('R11', 'equals', 0o52000, line=162)
#   BNKSUM 21
# Page 32

# MODULE 4 CONTAINS BANKS 22 THROUGH 27

#   BANK 22
S('KALCMON1', 'equals', 0o54000, line=169)
S('KALCMON2', 'equals', 0o54000, line=170)
S('R30LOC', 'equals', 0o54000, line=171)
S('RENDEZ', 'equals', 0o54000, line=172)
S('SERV2', 'equals', 0o54000, line=173)
S('LANDCNST', 'equals', 0o54000, line=174)
#   BNKSUM 22

#   BANK 23
S('POWFLITE', 'equals', 0o56000, line=178)
S('POWFLIT1', 'equals', 0o56000, line=179)
S('INFLIGHT', 'equals', 0o56000, line=180)
S('APOPERI', 'equals', 0o56000, line=181)
S('R61', 'equals', 0o56000, line=182)
S('R62', 'equals', 0o56000, line=183)
S('INTPRET1', 'equals', 0o56000, line=184)
S('MEASINC', 'equals', 0o56000, line=185)
S('MEASINC1', 'equals', 0o56000, line=186)
S('EXTVB1', 'equals', 0o56000, line=187)
S('P12A', 'equals', 0o56000, line=188)
S('NORMLIZ', 'equals', 0o56000, line=189)
S('ASENT7', 'equals', 0o56000, line=190)
#   BNKSUM 23

#   BANK 24
S('PLANTIN', 'equals', 0o60000, line=194)
S('P20S', 'equals', 0o60000, line=195)
#   BNKSUM 24

#   BANK 25
S('P20S1', 'equals', 0o62000, line=199)
S('P20S2', 'equals', 0o62000, line=200)
S('RADARUPT', 'equals', 0o62000, line=201)
S('RRLEADIN', 'equals', 0o62000, line=202)
S('R29S1', 'equals', 0o62000, line=203)
S('PLANTIN3', 'equals', 0o62000, line=204)
#   BNKSUM 25

#   BANK 26
# Page 33
S('P20S3', 'equals', 0o64000, line=209)
S('BAWLANGS', 'equals', 0o64000, line=210)
S('MANUVER', 'equals', 0o64000, line=211)
S('MANUVER1', 'equals', 0o64000, line=212)
S('PLANTIN1', 'equals', 0o64000, line=213)
S('PLANTIN2', 'equals', 0o64000, line=214)
#   BNKSUM 26

#   BANK 27
S('TOF-FF', 'equals', 0o66000, line=218)
S('TOF-FF1', 'equals', 0o66000, line=219)
S('P40S1', 'equals', 0o66000, line=220)
S('VECPT', 'equals', 0o66000, line=221)
S('ASENT1', 'equals', 0o66000, line=222)
S('SERV3', 'equals', 0o66000, line=223)
#   BNKSUM 27

# Page 34
# MODULE 5 CONTAINS BANKS 30 THROUGH 35

#   BANK 30
S('LOWSUPER', 'equals', 0o70000, line=230)
S('P12', 'equals', 0o70000, line=231)
S('ASENT', 'equals', 0o70000, line=232)
S('FCDUW', 'equals', 0o70000, line=233)
S('FLOGSUB', 'equals', 0o70000, line=234)
S('VB67A', 'equals', 0o70000, line=235)
S('ASENT5', 'equals', 0o70000, line=236)
#   BNKSUM 30

#   BANK 31
S('FTHROT', 'equals', 0o72000, line=240)
S('F2DPS*31', 'equals', 0o72000, line=241)
S('VB67', 'equals', 0o72000, line=242)
#   BNKSUM 31

#   BANK 32
S('P20S4', 'equals', 0o74000, line=246)
S('F2DPS*32', 'equals', 0o74000, line=247)
S('ABORTS', 'equals', 0o74000, line=248)
S('LRS22', 'equals', 0o74000, line=249)
S('P66LOC', 'equals', 0o74000, line=250)
S('R47', 'equals', 0o74000, line=251)
S('SERV', 'equals', 0o74000, line=252)
#   BNKSUM 32

#   BANK 33
S('SERVICES', 'equals', 0o76000, line=256)
S('R29/SERV', 'equals', 0o76000, line=257)
S('ASENT6', 'equals', 0o76000, line=258)
#   BNKSUM 33

#   BANK 34
S('STBLEORB', 'equals', 0o100000, line=262)
S('P30S1', 'equals', 0o100000, line=263)
S('CSI/CDH1', 'equals', 0o100000, line=264)
S('ASCFILT', 'equals', 0o100000, line=265)
S('R12STUFF', 'equals', 0o100000, line=266)
S('SERV4', 'equals', 0o100000, line=267)
#   BNKSUM 34

# Page 35
#   BANK 35
S('CSI/CDH', 'equals', 0o102000, line=272)
S('P30S', 'equals', 0o102000, line=273)
S('GLM', 'equals', 0o102000, line=274)
S('P40S2', 'equals', 0o102000, line=275)
#   BNKSUM 35

# Page 36
# MODULE 6 CONTAINS BANKS 36 THROUGH 43

#   BANK 36
S('P40S', 'equals', 0o104000, line=282)
#   BNKSUM 36

#   BANK 37
S('P05P06', 'equals', 0o106000, line=286)
S('IMU2', 'equals', 0o106000, line=287)
S('IMU4', 'equals', 0o106000, line=288)
S('R31', 'equals', 0o106000, line=289)
S('IMUSUPER', 'equals', 0o106000, line=290)
S('SERV1', 'equals', 0o106000, line=291)
#   BNKSUM 37

#   BANK 40
S('PINBALL1', 'equals', 0o110000, line=295)
S('SELFSUPR', 'equals', 0o110000, line=296)
S('PINSUPER', 'equals', 0o110000, line=297)
S('R31LOC', 'equals', 0o110000, line=298)
#   BNKSUM 40

#   BANK 41
S('PINBALL2', 'equals', 0o112000, line=302)
#   BNKSUM 41

#   BANK 42
S('SBAND', 'equals', 0o114000, line=306)
S('PINBALL3', 'equals', 0o114000, line=307)
#   BNKSUM 42

#   BANK 43
S('EXTVERBS', 'equals', 0o116000, line=311)
S('SELFCHEC', 'equals', 0o116000, line=312)
#   BNKSUM 43

# Page 37

S('HI6ZEROS', 'equals', 0o56521, line=317)  # ZERO VECTOR ALWAYS IN HIGH MEMORY
S('LO6ZEROS', 'equals', 0o34006, line=318)  # ZERO VECTOR ALWAYS IN LOW MEMORY
S('HIDPHALF', 'equals', 0o56517, line=319)
S('LODPHALF', 'equals', 0o34004, line=320)
S('HIDP1/4', 'equals', 0o56511, line=321)
S('LODP1/4', 'equals', 0o21036, line=322)  # 2DEC .25
S('HIUNITX', 'equals', 0o56517, line=323)
S('HIUNITY', 'equals', 0o56515, line=324)
S('HIUNITZ', 'equals', 0o56513, line=325)
S('LOUNITX', 'equals', 0o34004, line=326)  # 2DEC .5
S('LOUNITY', 'equals', 0o34002, line=327)  # 2DEC 0
S('LOUNITZ', 'equals', 0o34000, line=328)  # 2DEC 0

S('DELRSPL', 'equals', 0o55541, line=330)  # COL PGM, ALSO CALLED BY R30 IN LUMINARY.

# ROPE-SPECIFIC ASSIGNS OBVIATING NEED TO CHECK COMPUTER FLAG IN DETERMINING INTEGRATION AREA ENTRIES.

S('ATOPTHIS', 'equals', 0o36734, line=334)
S('ATOPOTH', 'equals', 0o36661, line=335)
S('OTHPREC', 'equals', 0o37043, line=336)
S('MOONTHIS', 'equals', 0o174, line=337)
S('MOONOTH', 'equals', 0o173, line=338)
S('MOVATHIS', 'equals', 0o36747, line=339)
S('RMM', 'equals', 0o34017, line=340)
S('RME', 'equals', 0o34021, line=341)
S('THISPREC', 'equals', 0o37057, line=342)
S('THISAXIS', 'equals', 0o56513, line=343)
S('NB1NB2', 'equals', 0o56513, line=344)  # FOR R31
S('ERASID', 'equals', 0o5011, line=345)  # DOWNLINK ERASABLE DUMP ID
S('DELAYNUM', 'equals', 0o4752, line=346)
