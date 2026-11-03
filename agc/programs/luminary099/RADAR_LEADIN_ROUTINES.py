"""RADAR_LEADIN_ROUTINES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/RADAR_LEADIN_ROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 490-491 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('RADAR_LEADIN_ROUTINES', 'RADAR_LEADIN_ROUTINES.agc', 'Luminary099', pages='490-491')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     RADAR_LEADIN_ROUTINES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        490-491
# Mod history:  2009-05-17 RSB  Adapted from the corresponding
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

# Page 490
#   BANK 25
#   SETLOC RRLEADIN
#   BANK

#   EBANK= RSTACK

# RADAR SAMPLING LOOP.

#   COUNT* $$/RLEAD
W('25,2003', 0o11755, 'RADSAMP', 'CCS', 'RSAMPDT', 'TIMES NORMAL ONCE-PER-SECOND SAMPLING.', line=39)
W('25,2004', 0o12006, '', 'TCF', '+2', line=40)
W('25,2005', 0o15261, '', 'TCF', 'TASKOVER', '+0 INSERTED MANUALLY TERMINATES TEST.', line=41)

W('25,2006', 0o05203, '', 'TC', 'WAITLIST', line=43)
#   EBANK= RSTACK
W('25,2007', 0o02003, '', '2CADR', 'RADSAMP', kind='data', line=45)
W('25,2010', 0o52064, kind='data', line=45)

W('25,2011', 0o37713, '', 'CAF', 'PRIO25', line=47)
W('25,2012', 0o05072, '', 'TC', 'NOVAC', line=48)
#   EBANK= RSTACK
W('25,2013', 0o02023, '', '2CADR', 'DORSAMP', kind='data', line=50)
W('25,2014', 0o52064, kind='data', line=50)

W('25,2015', 0o34736, '', 'CAF', 'BIT14', 'FOR CYCLIC SAMPLING, RTSTDEX =', line=52)
W('25,2016', 0o00006, '', 'EXTEND', '', 'RTSTLOC/2 + RTSTBASE', line=53)
W('25,2017', 0o71754, '', 'MP', 'RTSTLOC', line=54)
W('25,2020', 0o61753, '', 'AD', 'RTSTBASE', '0 FOR RR, 2 FOR LR.', line=55)
W('25,2021', 0o55751, '', 'TS', 'RTSTDEX', line=56)
W('25,2022', 0o15261, '', 'TCF', 'TASKOVER', line=57)

# DO THE ACTUAL RADAR SAMPLE.

W('25,2023', 0o02047, 'DORSAMP', 'TC', 'VARADAR', 'SELECTS VARIABLE RADAR CHANNEL.', line=61)
W('25,2024', 0o04616, '', 'TC', 'BANKCALL', line=62)
W('25,2025', 0o17714, '', 'CADR', 'RADSTALL', kind='data', line=63)

W('25,2026', 0o25756, '', 'INCR', 'RFAILCNT', 'ADVANCE FAIL COUNTER BUT ACCEPT BAD DATA', line=65)

W('25,2027', 0o00004, 'DORSAMP2', 'INHINT', line=67)
W('25,2030', 0o30101, '', 'CA', 'FLAGWRD5', "DON'T UPDATE RSTACK IF IN R77.", line=68)
W('25,2031', 0o74741, '', 'MASK', 'R77FLBIT', line=69)
W('25,2032', 0o10000, '', 'CCS', 'A', line=70)
W('25,2033', 0o12037, '', 'TCF', '+4', line=71)

W('25,2034', 0o53102, '', 'DXCH', 'SAMPLSUM', line=73)
W('25,2035', 0o51754, '', 'INDEX', 'RTSTLOC', line=74)
W('25,2036', 0o53601, '', 'DXCH', 'RSTACK', line=75)

W('25,2037', 0o41754, '', 'CS', 'RTSTLOC', 'CYCLE RTSTLOC.', line=77)
W('25,2040', 0o61752, '', 'AD', 'RTSTMAX', line=78)
W('25,2041', 0o00006, '', 'EXTEND', line=79)

# Page 491
W('25,2042', 0o12045, '', 'BZF', '+3', line=82)
W('25,2043', 0o31754, '', 'CA', 'RTSTLOC', line=83)
W('25,2044', 0o64752, '', 'AD', 'TWO', 'STORAGE IS DP', line=84)
W('25,2045', 0o55754, '', 'TS', 'RTSTLOC', line=85)
W('25,2046', 0o15155, '', 'TCF', 'ENDOFJOB', 'CONTINUOUS SAMPLING AND 2N TRIES - GONE.', line=86)

# VARIABLE RADAR DATA CALLER FOR ONE MEASUREMENT ONLY.

W('25,2047', 0o34753, 'VARADAR', 'CAF', 'ONE', 'WILL BE SENT TO RADAR ROUTINE IN A BY', line=90)
W('25,2050', 0o54133, '', 'TS', 'BUF2', 'SWCALL.', line=91)
W('25,2051', 0o51751, '', 'INDEX', 'RTSTDEX', line=92)
W('25,2052', 0o32054, '', 'CAF', 'RDRLOCS', line=93)
W('25,2053', 0o14622, '', 'TCF', 'SWCALL', 'NOT TOUCHING Q.', line=94)

W('25,2054', 0o53105, 'RDRLOCS', 'CADR', 'RRRANGE', '=0', kind='data', line=96)
W('25,2055', 0o53103, '', 'CADR', 'RRRDOT', '=1', kind='data', line=97)
W('25,2056', 0o53101, '', 'CADR', 'LRVELX', '=2', kind='data', line=98)
W('25,2057', 0o53077, '', 'CADR', 'LRVELY', '=3', kind='data', line=99)
W('25,2060', 0o53075, '', 'CADR', 'LRVELZ', '=4', kind='data', line=100)
W('25,2061', 0o53073, '', 'CADR', 'LRALT', '=5', kind='data', line=101)
