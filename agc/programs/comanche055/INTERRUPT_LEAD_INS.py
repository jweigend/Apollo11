"""INTERRUPT_LEAD_INS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/INTERRUPT_LEAD_INS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 131-132 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('INTERRUPT_LEAD_INS', 'INTERRUPT_LEAD_INS.agc', 'Comanche055', pages='131-132')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     INTERRUPT_LEAD_INS.agc
# Purpose:      Part of the source code for Comanche, build 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 131-132
# Contact:      Ron Burkey <info@sandroid.org>,
# Fabrizio Bernardini <fabrizio@spacecraft.it>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  09/05/09 FB     Transcription of Batch FB-1 Assignment.
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

# Page 131
#   SETLOC 4000

#   COUNT 02/RUPTS

W('4000', 0o00004, '', 'INHINT', '', 'GO', line=36)
W('4001', 0o34054, '', 'CAF', 'GOBB', line=37)
W('4002', 0o56006, '', 'XCH', 'BBANK', line=38)
W('4003', 0o12526, '', 'TCF', 'GOPROG', line=39)

W('4004', 0o52011, '', 'DXCH', 'ARUPT', 'T6RUPT', line=41)
W('4005', 0o00006, '', 'EXTEND', line=42)
W('4006', 0o31311, '', 'DCA', 'T6LOC', line=43)
W('4007', 0o52006, '', 'DTCB', line=44)

W('4010', 0o52011, '', 'DXCH', 'ARUPT', 'T5RUPT', line=46)
W('4011', 0o40030, '', 'CS', 'TIME5', line=47)
W('4012', 0o65036, '', 'AD', '.5SEC', line=48)
W('4013', 0o14065, '', 'TCF', 'T5RUPT', line=49)

W('4014', 0o52011, '', 'DXCH', 'ARUPT', 'T3RUPT', line=51)
W('4015', 0o34055, '', 'CAF', 'T3RPTBB', line=52)
W('4016', 0o56006, '', 'XCH', 'BBANK', line=53)
W('4017', 0o13416, '', 'TCF', 'T3RUPT', line=54)

W('4020', 0o52011, '', 'DXCH', 'ARUPT', 'T4RUPT', line=56)
W('4021', 0o34063, '', 'CAF', 'T4RPTBB', line=57)
W('4022', 0o56006, '', 'XCH', 'BBANK', line=58)
W('4023', 0o12000, '', 'TCF', 'T4RUPT', line=59)

W('4024', 0o52011, '', 'DXCH', 'ARUPT', 'KEYRUPT1', line=61)
W('4025', 0o34056, '', 'CAF', 'KEYRPTBB', line=62)
W('4026', 0o56006, '', 'XCH', 'BBANK', line=63)
W('4027', 0o13673, '', 'TCF', 'KEYRUPT1', line=64)

W('4030', 0o52011, '', 'DXCH', 'ARUPT', 'KEYRUPT2', line=66)
W('4031', 0o34057, '', 'CAF', 'MKRUPTBB', line=67)
W('4032', 0o56006, '', 'XCH', 'BBANK', line=68)
W('4033', 0o12104, '', 'TCF', 'MARKRUPT', line=69)

W('4034', 0o52011, '', 'DXCH', 'ARUPT', 'UPRUPT', line=71)
W('4035', 0o34056, '', 'CAF', 'UPRPTBB', line=72)
W('4036', 0o56006, '', 'XCH', 'BBANK', line=73)
W('4037', 0o13716, '', 'TCF', 'UPRUPT', line=74)

W('4040', 0o52011, '', 'DXCH', 'ARUPT', 'DOWNRUPT', line=76)
W('4041', 0o34060, '', 'CAF', 'DWNRPTBB', line=77)
W('4042', 0o56006, '', 'XCH', 'BBANK', line=78)
W('4043', 0o13521, '', 'TCF', 'DODOWNTM', line=79)

W('4044', 0o52011, '', 'DXCH', 'ARUPT', 'RADAR RUPT', line=81)
# Page 132
W('4045', 0o34061, '', 'CAF', 'RDRPTBB', line=83)
W('4046', 0o56006, '', 'XCH', 'BBANK', line=84)
W('4047', 0o12504, '', 'TCF', 'VHFREAD', line=85)

W('4050', 0o52011, '', 'DXCH', 'ARUPT', 'HAND CONTROL RUPT', line=87)
W('4051', 0o34062, '', 'CAF', 'HCRUPTBB', line=88)
W('4052', 0o56006, '', 'XCH', 'BBANK', line=89)
W('4053', 0o15336, '', 'TCF', 'RESUME +3', 'NOT USED', line=90)
#   EBANK= LST1  # RESTART USES E0,E3
W('4054', 0o12063, 'GOBB', 'BBCON', 'GOPROG', kind='data', line=92)

#   EBANK= LST1
W('4055', 0o02063, 'T3RPTBB', 'BBCON', 'T3RUPT', kind='data', line=95)

#   EBANK= KEYTEMP1
W('4056', 0o16060, 'KEYRPTBB', 'BBCON', 'KEYRUPT1', kind='data', line=98)

#   EBANK= MRKBUF1
W('4057', 0o16067, 'MKRUPTBB', 'BBCON', 'MARKRUPT', kind='data', line=101)

S('UPRPTBB', 'equals', 0o4056, line=103)

#   EBANK= DNTMBUFF
W('4060', 0o12060, 'DWNRPTBB', 'BBCON', 'DODOWNTM', kind='data', line=106)

#   EBANK= DATATEST
W('4061', 0o56067, 'RDRPTBB', 'BBCON', 'VHFREAD', kind='data', line=109)
#   EBANK= TIME1
W('4062', 0o04060, 'HCRUPTBB', 'BBCON', 'RESUME', 'NOT USED', kind='data', line=111)
#   EBANK= DSRUPTSW
W('4063', 0o14062, 'T4RPTBB', 'BBCON', 'T4RUPT', kind='data', line=113)
#   EBANK= TIME1
W('4064', 0o04060, 'T5RPTBB', 'BBCON', 'T5RUPT', kind='data', line=115)

W('4065', 0o00006, 'T5RUPT', 'EXTEND', line=117)
W('4066', 0o65337, '', 'BZMF', 'NOQBRSM', line=118)
W('4067', 0o00006, '', 'EXTEND', line=119)
W('4070', 0o31313, '', 'DCA', 'T5LOC', line=120)
W('4071', 0o52006, '', 'DTCB', line=121)
