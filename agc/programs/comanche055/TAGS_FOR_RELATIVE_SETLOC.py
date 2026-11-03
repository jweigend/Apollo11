"""TAGS_FOR_RELATIVE_SETLOC.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/TAGS_FOR_RELATIVE_SETLOC.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 27-36 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('TAGS_FOR_RELATIVE_SETLOC', 'TAGS_FOR_RELATIVE_SETLOC.agc', 'Comanche055', pages='27-36')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     TAGS_FOR_RELATIVE_SETLOC.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Mod history:  2009-05-05 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
# 2009-05-20 RSB  Corrected R32 -> R31.
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

# Page 27
# TAGS FOR RELATIVE SETLOC AND BLANK BANK CARDS

#   FIXED MEMORY 120000 - 167777
#   COUNT BANKSUM

# MODULE 1 CONTAINS BANKS 0 THROUGH 5

#   BLOCK 02
S('FFTAG1', 'equals', 0o4000, line=39)
S('FFTAG2', 'equals', 0o4000, line=40)
S('FFTAG3', 'equals', 0o4000, line=41)
S('FFTAG4', 'equals', 0o4000, line=42)
S('FFTAG7', 'equals', 0o4000, line=43)
S('FFTAG8', 'equals', 0o4000, line=44)
S('FFTAG9', 'equals', 0o4000, line=45)
S('FFTAG10', 'equals', 0o4000, line=46)
S('FFTAG12', 'equals', 0o4000, line=47)
S('P30SUBS', 'equals', 0o4000, line=48)
S('STOPRAT', 'equals', 0o4000, line=49)
S('P23S', 'equals', 0o4000, line=50)
#   BNKSUM 02

#   BLOCK 03
S('FFTAG5', 'equals', 0o6000, line=54)
S('FFTAG6', 'equals', 0o6000, line=55)
S('DAPS9', 'equals', 0o6000, line=56)
S('FFTAG13', 'equals', 0o6000, line=57)
#   BNKSUM 03

#   BANK 00
S('DLAYJOB', 'equals', 0o10000, line=61)
#   BNKSUM 00

#   BANK 01
S('RESTART', 'equals', 0o12000, line=65)
#   BNKSUM 01

#   BANK 4
S('VERB37', 'equals', 0o20000, line=69)
S('CONICS1', 'equals', 0o20000, line=70)
S('PINBALL4', 'equals', 0o20000, line=71)
S('CSI/CDH1', 'equals', 0o20000, line=72)
S('INTPRET2', 'equals', 0o20000, line=73)
S('IMUCAL1', 'equals', 0o20000, line=74)

# Page 28

S('STBLEORB', 'equals', 0o20000, line=78)
S('E/PROG', 'equals', 0o20000, line=79)
S('MIDDGIM', 'equals', 0o20000, line=80)
#   BNKSUM 04

#   BANK 5
S('FRANDRES', 'equals', 0o22000, line=84)
S('DOWNTELM', 'equals', 0o22000, line=85)
S('DAPMASS', 'equals', 0o22000, line=86)
S('CDHTAG', 'equals', 0o22000, line=87)
#   BNKSUM 05

# MODULE 2 CONTAINS BANKS 6 THROUGH 13

#   BANK 6
S('IMUCOMP', 'equals', 0o24000, line=93)
S('T4RUP', 'equals', 0o24000, line=94)
S('IMUCAL2', 'equals', 0o24000, line=95)
S('CSIPROG', 'equals', 0o24000, line=96)
#   BNKSUM 06

#   BANK 7
S('SXTMARKE', 'equals', 0o26000, line=100)
S('R02', 'equals', 0o26000, line=101)
S('MODESW', 'equals', 0o26000, line=102)
S('XANG', 'equals', 0o26000, line=103)
S('KEYRUPT', 'equals', 0o26000, line=104)
S('CSIPROG6', 'equals', 0o26000, line=105)
#   BNKSUM 07

#   BANK 10
S('DISPLAYS', 'equals', 0o30000, line=109)
S('PHASETAB', 'equals', 0o30000, line=110)
S('COMGEOM2', 'equals', 0o30000, line=111)
S('SXTMARK1', 'equals', 0o30000, line=112)
S('P60S4', 'equals', 0o30000, line=113)
S('OPTDRV', 'equals', 0o30000, line=114)
S('CSIPROG8', 'equals', 0o30000, line=115)
#   BNKSUM 10

#   BANK 11
S('ORBITAL', 'equals', 0o32000, line=119)
S('ORBITAL1', 'equals', 0o32000, line=120)  # CONSTANTS

# Page 29

S('INTVEL', 'equals', 0o32000, line=124)
S('S52/2', 'equals', 0o32000, line=125)
S('CSIPROG5', 'equals', 0o32000, line=126)
S('INTINIT1', 'equals', 0o32000, line=127)
#   BNKSUM 11

#   BANK 12
S('CONICS', 'equals', 0o34000, line=131)
S('CSIPROG2', 'equals', 0o34000, line=132)
S('CSI/CDH2', 'equals', 0o34000, line=133)
S('MODCHG2', 'equals', 0o34000, line=134)
#   BNKSUM 12

#   BANK 13
S('P76LOC', 'equals', 0o36000, line=138)
S('LATLONG', 'equals', 0o36000, line=139)
S('INTINIT', 'equals', 0o36000, line=140)
S('SR52/1', 'equals', 0o36000, line=141)
S('ORBITAL2', 'equals', 0o36000, line=142)
S('CDHTAGS', 'equals', 0o36000, line=143)
S('E/PROG1', 'equals', 0o36000, line=144)
S('MODCHG3', 'equals', 0o36000, line=145)
#   BNKSUM 13

# SPACER

# MODULE 3 CONTAINS BANKS 14 THROUGH 21

#   BANK 14
S('STARTAB', 'equals', 0o40000, line=153)
S('RT53', 'equals', 0o40000, line=154)
S('P50S1', 'equals', 0o40000, line=155)
S('MEASINC2', 'equals', 0o40000, line=156)
S('CSI/CDH3', 'equals', 0o40000, line=157)
#   BNKSUM 14

#   BANK 15
S('P50S', 'equals', 0o42000, line=161)
S('ETRYDAP', 'equals', 0o42000, line=162)
S('S52/3', 'equals', 0o42000, line=163)
#   BNKSUM 15

#   BANK 16
S('P40S1', 'equals', 0o44000, line=167)

# Page 30

S('DAPROLL', 'equals', 0o44000, line=171)
S('P50S2', 'equals', 0o44000, line=172)
S('P23S1', 'equals', 0o44000, line=173)
S('RTE2', 'equals', 0o44000, line=174)
#   BNKSUM 16

#   BANK 17
S('DAPS4', 'equals', 0o46000, line=178)
S('DAPS5', 'equals', 0o46000, line=179)
S('DAPS7', 'equals', 0o46000, line=180)
S('P50S3', 'equals', 0o46000, line=181)
#   BNKSUM 17

#   BANK 20
S('DAPS6', 'equals', 0o50000, line=185)
S('DAPS1', 'equals', 0o50000, line=186)
S('DAPS2', 'equals', 0o50000, line=187)
S('MANUSTUF', 'equals', 0o50000, line=188)
S('R36CM', 'equals', 0o50000, line=189)
S('VAC5LOC', 'equals', 0o50000, line=190)
#   BNKSUM 20

#   BANK 21
S('DAPS3', 'equals', 0o52000, line=194)
S('MYSUBS', 'equals', 0o52000, line=195)
S('KALCMON3', 'equals', 0o52000, line=196)
#   BNKSUM 21

# MODULE 4 CONTAINS BANKS 22 THROUGH 27

#   BANK 22
S('RTBCODES', 'equals', 0o54000, line=202)
S('RTBCODE1', 'equals', 0o54000, line=203)
S('DAPS8', 'equals', 0o54000, line=204)
S('APOPERI', 'equals', 0o54000, line=205)
S('P40S5', 'equals', 0o54000, line=206)
S('KALCMON2', 'equals', 0o54000, line=207)
S('KALCMON1', 'equals', 0o54000, line=208)
S('CSIPROG3', 'equals', 0o54000, line=209)
#   BNKSUM 22

# Page 31

#   BANK 23
S('P20S2', 'equals', 0o56000, line=215)
S('INFLIGHT', 'equals', 0o56000, line=216)
S('COMGEOM1', 'equals', 0o56000, line=217)
S('POWFLITE', 'equals', 0o56000, line=218)
S('POWFLIT1', 'equals', 0o56000, line=219)
S('RENDGUID', 'equals', 0o56000, line=220)
S('POWFLIT2', 'equals', 0o56000, line=221)
S('R30LOC', 'equals', 0o56000, line=222)
S('P11FOUR', 'equals', 0o56000, line=223)
S('CSIPROG4', 'equals', 0o56000, line=224)
#   BNKSUM 23

#   BANK 24
S('LOADDAP', 'equals', 0o60000, line=228)
S('P40S', 'equals', 0o60000, line=229)
S('CSIPROG7', 'equals', 0o60000, line=230)
#   BNKSUM 24

#   BANK 25
S('REENTRY', 'equals', 0o62000, line=234)
S('CDHTAG1', 'equals', 0o62000, line=235)
#   BNKSUM 25

#   BANK 26
S('INTPRET1', 'equals', 0o64000, line=239)
S('REENTRY1', 'equals', 0o64000, line=240)
S('P60S', 'equals', 0o64000, line=241)
S('P60S1', 'equals', 0o64000, line=242)
S('P60S2', 'equals', 0o64000, line=243)
S('P60S3', 'equals', 0o64000, line=244)
S('PLANTIN', 'equals', 0o64000, line=245)  # LUNAR ROT
S('EPHEM', 'equals', 0o64000, line=246)
S('P05P06', 'equals', 0o64000, line=247)
S('26P50S', 'equals', 0o64000, line=248)
#   BNKSUM 26

#   BANK 27
S('TOF-FF', 'equals', 0o66000, line=252)
S('TOF-FF1', 'equals', 0o66000, line=253)
S('MANUVER', 'equals', 0o66000, line=254)
S('MANUVER1', 'equals', 0o66000, line=255)

# Page 32

S('VECPT', 'equals', 0o66000, line=259)
S('UPDATE1', 'equals', 0o66000, line=260)
S('UPDATE2', 'equals', 0o66000, line=261)
S('R22S1', 'equals', 0o66000, line=262)
S('P60S5', 'equals', 0o66000, line=263)
S('P40S2', 'equals', 0o66000, line=264)
#   BNKSUM 27

# MODULE 5 CONTAINS BANKS 30 THROUGH 35

#   BANK 30
S('IMUSUPER', 'equals', 0o70000, line=270)
S('LOWSUPER', 'equals', 0o70000, line=271)
S('FCSTART', 'equals', 0o70000, line=272)  # STANDARD LOCATION FOR THIS. (FOR EXTV8)
S('LOPC', 'equals', 0o70000, line=273)
S('P20S1', 'equals', 0o70000, line=274)
S('P20S6', 'equals', 0o70000, line=275)
S('P40S3', 'equals', 0o70000, line=276)
S('R35A', 'equals', 0o70000, line=277)
#   BNKSUM 30

#   BANK 31
S('R35', 'equals', 0o72000, line=281)
S('RT23', 'equals', 0o72000, line=282)
S('P30S1A', 'equals', 0o72000, line=283)
S('R34', 'equals', 0o72000, line=284)
S('CDHTAG2', 'equals', 0o72000, line=285)
S('CSIPROG9', 'equals', 0o72000, line=286)
S('R31', 'equals', 0o72000, line=287)
S('P22S', 'equals', 0o72000, line=288)
S('RTE3', 'equals', 0o72000, line=289)
#   BNKSUM 31

#   BANK 32
S('MSGSCAN1', 'equals', 0o74000, line=293)
S('RTE', 'equals', 0o74000, line=294)
S('DELRSPL1', 'equals', 0o74000, line=295)
S('IMUCAL3', 'equals', 0o74000, line=296)
#   BNKSUM 32

#   BANK 33
S('TESTLEAD', 'equals', 0o76000, line=300)

# Page 33

S('IMUCAL', 'equals', 0o76000, line=304)
#   BNKSUM 33

#   BANK 34
S('P11ONE', 'equals', 0o100000, line=308)
S('P20S3', 'equals', 0o100000, line=309)
S('P20S4', 'equals', 0o100000, line=310)
S('RTECON', 'equals', 0o100000, line=311)
#   BNKSUM 34

#   BANK 35
S('RTECON1', 'equals', 0o102000, line=315)
S('CSI/CDH', 'equals', 0o102000, line=316)
S('P30S1', 'equals', 0o102000, line=317)
S('P30S', 'equals', 0o102000, line=318)
S('P17S1', 'equals', 0o102000, line=319)
S('MEASINC3', 'equals', 0o102000, line=320)
S('INTINIT2', 'equals', 0o102000, line=321)
#   BNKSUM 35

# MODULE 6 CONTAINS BANKS 36 THROUGH 43

#   BANK 36
S('MEASINC', 'equals', 0o104000, line=327)
S('MEASINC1', 'equals', 0o104000, line=328)
S('P17S', 'equals', 0o104000, line=329)
S('RTE1', 'equals', 0o104000, line=330)
S('S3435LOC', 'equals', 0o104000, line=331)
#   BNKSUM 36

#   BANK 37
S('P20S', 'equals', 0o106000, line=335)
S('BODYATT', 'equals', 0o106000, line=336)
S('RENDEZ', 'equals', 0o106000, line=337)
S('SERVICES', 'equals', 0o106000, line=338)
S('P11TWO', 'equals', 0o106000, line=339)
S('CDHTAG3', 'equals', 0o106000, line=340)
#   BNKSUM 37

#   BANK 40
S('PINSUPER', 'equals', 0o110000, line=344)

# Page 34

S('SELFSUPR', 'equals', 0o110000, line=348)
S('PINBALL1', 'equals', 0o110000, line=349)
S('R36CM1', 'equals', 0o110000, line=350)
#   BNKSUM 40

#   BANK 41
S('PINBALL2', 'equals', 0o112000, line=354)
S('R36LM', 'equals', 0o112000, line=355)
#   BNKSUM 41

#   BANK 42
S('SBAND', 'equals', 0o114000, line=359)
S('PINBALL3', 'equals', 0o114000, line=360)
S('EXTVBS', 'equals', 0o114000, line=361)
S('R36LM1', 'equals', 0o114000, line=362)
#   BNKSUM 42

#   BANK 43
S('SELFCHEC', 'equals', 0o116000, line=366)
S('EXTVERBS', 'equals', 0o116000, line=367)
#   BNKSUM 43

S('HI6ZEROS', 'equals', 0o65334, line=370)  # ZERO VECTOR ALWAYS IN HIGH MEMORY
S('LO6ZEROS', 'equals', 0o21565, line=371)  # ZERO VECTOR ALWAYS IN LOW MEMORY
S('HIDPHALF', 'equals', 0o65332, line=372)
S('LODPHALF', 'equals', 0o21563, line=373)
S('HIDP1/4', 'equals', 0o65324, line=374)
S('LODP1/4', 'equals', 0o21611, line=375)  # 2DEC .25
S('HIUNITX', 'equals', 0o65332, line=376)
S('HIUNITY', 'equals', 0o65330, line=377)
S('HIUNITZ', 'equals', 0o65326, line=378)
S('LOUNITX', 'equals', 0o21563, line=379)  # 2DEC .5
S('LOUNITY', 'equals', 0o21561, line=380)  # 2DEC 0
S('LOUNITZ', 'equals', 0o21557, line=381)  # 2DEC 0
S('3/4LOWDP', 'equals', 0o33763, line=382)  # 2DEC 3.0 B-2
#   SBANK= LOWSUPER

# ROPE SPECIFIC ASSIGNS OBVIATING NEED TO CHECK COMPUTER FLAG IN DETVRUZVING INTEGRATION AREA ENTRIES

S('OTHPREC', 'equals', 0o37105, line=387)
S('ATOPOTH', 'equals', 0o36760, line=388)
S('ATOPTHIS', 'equals', 0o36705, line=389)
S('MOONTHIS', 'equals', 0o173, line=390)

# Page 35

S('MOONOTH', 'equals', 0o174, line=394)
S('MOVATHIS', 'equals', 0o36720, line=395)
S('STATEST', 'equals', 0o72032, line=396)  # * TEMPORARY
S('THISPREC', 'equals', 0o37071, line=397)
S('THISAXIS', 'equals', 0o65332, line=398)
S('ERASID', 'equals', 0o5054, line=399)  # DOWNLINK ERASABLE DUMP ID
S('DELAYNUM', 'equals', 0o6214, line=400)

# ***************************************************************************************************************

# THE FOLLOWING ECADRS ARE DEFINED TO FACILITATE EBANK SWITCHING.  THEY ALSO MAKE IT EASIER FOR
# ERASABLE CONTROL TO REARRANGE ERASABLE MEMORY WITHOUT DISRUPTING THE PROGRAMS WHICH SET EBANKS.
# PRIOR TO ROPE RELEASE FIXED MEMORY CAN BE SAVED BY SETTING EACH EBXXXX =EBANKX (X=4,5,6,7).EBANKX OF COURSE
# WILL BE THE BANK WHERE THE ERASABLES REFERENCED IN EBXXXX WILL BE STORED.

#   BANK 7
#   EBANK= MARKDOWN
W('07,2000', 0o03674, 'EBMARKDO', 'ECADR', 'MARKDOWN', kind='data', line=411)
#   EBANK= MRKBUF1
W('07,2001', 0o03725, 'EBMRKBUF', 'ECADR', 'MRKBUF1', kind='data', line=413)

#   BANK 24
#   EBANK= DVCNTR
W('24,2000', 0o03431, 'EBDVCNTR', 'ECADR', 'DVCNTR', kind='data', line=417)
#   EBANK= P40TMP
W('24,2001', 0o03672, 'EBP40TMP', 'ECADR', 'P40TMP', kind='data', line=419)

#   BANK 34
#   EBANK= DVCNTR
W('34,2000', 0o03431, 'EBDVCNT', 'ECADR', 'DVCNTR', kind='data', line=423)
#   EBANK= QPLACES
W('34,2001', 0o02426, 'EBQPLACE', 'ECADR', 'QPLACES', kind='data', line=425)

#   BANK 37
#   EBANK= RN1
W('37,2000', 0o01231, 'EBRN1', 'ECADR', 'RN1', kind='data', line=429)

# ***************************************************************************************************************

# Page 36

# *** END OF MAIN PROGRAM ***
