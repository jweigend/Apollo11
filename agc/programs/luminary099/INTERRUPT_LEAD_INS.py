"""INTERRUPT_LEAD_INS.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/INTERRUPT_LEAD_INS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 153-154 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INTERRUPT_LEAD_INS', 'INTERRUPT_LEAD_INS.agc', 'Luminary099', pages='153-154')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INTERRUT_LEAD_INS.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Onno Hommes <ohommes@cmu.edu>.
# Website:      www.ibiblio.org/apollo.
# Pages:        0153-0154
# Mod history:  2009-05-14 OH   Transcribed from page images.
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

# Page 153
#   SETLOC 4000

#   COUNT* $$/RUPTS  # FIX-FIX LEAD INS
W('4000', 0o00004, '', 'INHINT', '', 'GO', line=32)
W('4001', 0o34054, '', 'CAF', 'GOBB', line=33)
W('4002', 0o56006, '', 'XCH', 'BBANK', line=34)
W('4003', 0o12667, '', 'TCF', 'GOPROG', line=35)

W('4004', 0o52011, '', 'DXCH', 'ARUPT', 'T6RUPT', line=37)
W('4005', 0o00006, '', 'EXTEND', line=38)
W('4006', 0o34056, '', 'DCA', 'T6ADR', line=39)
W('4007', 0o52006, '', 'DTCB', line=40)

W('4010', 0o52011, '', 'DXCH', 'ARUPT', 'T5RUPT - AUTOPILOT', line=42)
W('4011', 0o00006, '', 'EXTEND', line=43)
W('4012', 0o31275, '', 'DCA', 'T5ADR', line=44)
W('4013', 0o52006, '', 'DTCB', line=45)

W('4014', 0o52011, '', 'DXCH', 'ARUPT', 'T3RUPT', line=47)
W('4015', 0o34057, '', 'CAF', 'T3RPTBB', line=48)
W('4016', 0o56006, '', 'XCH', 'BBANK', line=49)
W('4017', 0o13407, '', 'TCF', 'T3RUPT', line=50)

W('4020', 0o52011, '', 'DXCH', 'ARUPT', 'T4RUPT', line=52)
W('4021', 0o34064, '', 'CAF', 'T4RPTBB', line=53)
W('4022', 0o56006, '', 'XCH', 'BBANK', line=54)
W('4023', 0o12000, '', 'TCF', 'T4RUPT', line=55)

W('4024', 0o52011, '', 'DXCH', 'ARUPT', 'KEYRUPT1', line=57)
W('4025', 0o34060, '', 'CAF', 'KEYRPTBB', line=58)
W('4026', 0o56006, '', 'XCH', 'BBANK', line=59)
W('4027', 0o13274, '', 'TCF', 'KEYRUPT1', line=60)

W('4030', 0o52011, '', 'DXCH', 'ARUPT', 'KEYRUPT2', line=62)
W('4031', 0o34061, '', 'CAF', 'MKRUPTBB', line=63)
W('4032', 0o56006, '', 'XCH', 'BBANK', line=64)
W('4033', 0o12332, '', 'TCF', 'MARKRUPT', line=65)

W('4034', 0o52011, '', 'DXCH', 'ARUPT', 'UPRUPT', line=67)
W('4035', 0o34060, '', 'CAF', 'UPRPTBB', line=68)
W('4036', 0o56006, '', 'XCH', 'BBANK', line=69)
W('4037', 0o13317, '', 'TCF', 'UPRUPT', line=70)

W('4040', 0o52011, '', 'DXCH', 'ARUPT', 'DOWNRUPT', line=72)
W('4041', 0o34062, '', 'CAF', 'DWNRPTBB', line=73)
W('4042', 0o56006, '', 'XCH', 'BBANK', line=74)
W('4043', 0o13506, '', 'TCF', 'DODOWNTM', line=75)

W('4044', 0o52011, '', 'DXCH', 'ARUPT', 'RADAR RUPT', line=77)
W('4045', 0o34063, '', 'CAF', 'RDRPTBB', line=78)
# Page 154
W('4046', 0o56006, '', 'XCH', 'BBANK', line=80)
W('4047', 0o13150, '', 'TCF', 'RADAREAD', line=81)

W('4050', 0o52011, '', 'DXCH', 'ARUPT', 'RUPT10 IS USED ONLY BY LANDING GUIDANCE', line=83)
W('4051', 0o34065, '', 'CA', 'RUPT10BB', line=84)
W('4052', 0o56006, '', 'XCH', 'BBANK', line=85)
W('4053', 0o12275, '', 'TCF', 'PITFALL', line=86)

#   EBANK= LST1  # RESTART USES E0, E3
W('4054', 0o12103, 'GOBB', 'BBCON', 'GOPROG', kind='data', line=90)

#   EBANK= PERROR
W('4055', 0o02065, 'T6ADR', '2CADR', 'DOT6RUPT', kind='data', line=93)
W('4056', 0o36106, kind='data', line=93)

#   EBANK= LST1
W('4057', 0o02103, 'T3RPTBB', 'BBCON', 'T3RUPT', kind='data', line=96)

#   EBANK= KEYTEMP1
W('4060', 0o10100, 'KEYRPTBB', 'BBCON', 'KEYRUPT1', kind='data', line=99)

#   EBANK= AOTAZ
W('4061', 0o16107, 'MKRUPTBB', 'BBCON', 'MARKRUPT', kind='data', line=102)

S('UPRPTBB', 'equals', 0o4060, line=104)

#   EBANK= DNTMBUFF
W('4062', 0o12100, 'DWNRPTBB', 'BBCON', 'DODOWNTM', kind='data', line=107)

#   EBANK= RADMODES
W('4063', 0o52100, 'RDRPTBB', 'BBCON', 'RADAREAD', kind='data', line=110)

#   EBANK= M11
W('4064', 0o14106, 'T4RPTBB', 'BBCON', 'T4RUPT', kind='data', line=113)

#   EBANK= ELVIRA
W('4065', 0o22102, 'RUPT10BB', 'BBCON', 'PITFALL', kind='data', line=116)
