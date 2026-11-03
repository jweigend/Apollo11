"""GROUND_TRACKING_DETERMINATION_PROGRAM.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/GROUND_TRACKING_DETERMINATION_PROGRAM.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 456-459 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('GROUND_TRACKING_DETERMINATION_PROGRAM', 'GROUND_TRACKING_DETERMINATION_PROGRAM.agc', 'Comanche055', pages='456-459')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     GROUND_TRACKING_DETERMINATION_PROGRAM.agc
# Purpose:      Part of the source code for Comanche, build 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 456-459
# Contact:      Onno Hommes <ohommes@cmu.edu>.
# Website:      www.ibiblio.org/apollo.
# Mod history:  2009-05-07 OH   Transcription Batch 1 Assignment
# 2009-05-20 RSB  Corrected a couple of DIMOFLAG to DIM0FLAG.
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
# Refer directly to the online document mentioned above for further information.
# Please report any errors to info@sandroid.org.

# Page 456
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
# ASTRONAUT REQUEST THROUGH DSKY TO TERMINATE PROGRAM V34E
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
# AX0           2DEC    4.652459653 E-5         RADIANS         "68-69 CONSTANTS"
#
# -AY0          2DEC    2.147535898 E-5         RADIANS
#
# AZ0           2DEC    .7753206164             REVOLUTIONS
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

# Page 457
# CENTRALS-A,Q,L
# OTHER-THOSE USED BY THE ABOVE LISTED SUBROUTINES
# SEE LEMPREC,LAT-LONG
#   SBANK= LOWSUPER  # FOR LOW 2CADR'S.

#   BANK 33
#   SETLOC P20S
#   BANK

#   EBANK= P21TIME
#   COUNT 24/P21

W('37,2001', 0o35017, 'PROG21', 'CAF', 'ONE', line=96)
W('37,2002', 0o55132, '', 'TS', 'OPTION2', 'ASSUMED VEHICLE IS LM , R2 = 00001', line=97)
W('37,2003', 0o35016, '', 'CAF', 'BIT2', ' OPTION 2', line=98)
W('37,2004', 0o04662, '', 'TC', 'BANKCALL', line=99)
W('37,2005', 0o21055, '', 'CADR', 'GOPERF4', kind='data', line=100)
W('37,2006', 0o04106, '', 'TC', 'GOTOPOOH', 'TERMINATE', line=101)
W('37,2007', 0o02011, '', 'TC', '+2', 'PROCEED VALUE OF ASSUMED VEHICLE OK', line=102)
W('37,2010', 0o02003, '', 'TC', '-5', 'R2 LOADED THROUGH DSKY', line=103)
W('37,2011', 0o32152, 'P21PROG1', 'CAF', 'V6N34', 'LOAD DESIRED TIME OF LAT-LONG.', line=104)
W('37,2012', 0o04662, '', 'TC', 'BANKCALL', line=105)
W('37,2013', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=106)
W('37,2014', 0o04106, '', 'TC', 'GOTOPOOH', 'TERM', line=107)
W('37,2015', 0o02017, '', 'TC', '+2', 'PROCEED VALUES OK', line=108)
W('37,2016', 0o02011, '', 'TC', '-5', 'TIME LOADED THROUGH DSKY', line=109)
W('37,2017', 0o06006, '', 'TC', 'INTPRET', line=110)
W('37,2020', 0o77745, '', 'DLOAD', kind='interp', line=111)
W('37,2021', 0o01046, '', '', 'DSPTEM1', kind='operand', line=112)
W('37,2022', 0o34041, '', 'STCALL', 'TDEC1', 'INTEG TO TIME SPECIFIED IN TDEC', kind='interp', line=113)
W('37,2023', 0o27442, '', '', 'INTSTALL', kind='operand', line=114)
W('37,2024', 0o43014, '', 'BON', 'SET', kind='interp', line=115)
W('37,2025', 0o01303, '', '', 'P21FLAG', kind='operand', line=116)
W('37,2026', 0o76044, '', '', 'P21CONT', 'ON...RECYCLE USING BASE VECTOR', kind='operand', line=117)
W('37,2027', 0o01474, '', '', 'VINTFLAG', 'OFF..1ST PASS CALC BASE VECTOR', kind='operand', line=118)
W('37,2030', 0o70535, '', 'SLOAD', 'SR1', kind='interp', line=119)
W('37,2031', 0o01133, '', '', 'OPTION2', kind='operand', line=120)
W('37,2032', 0o43030, '', 'BHIZ', 'CLEAR', kind='interp', line=121)
W('37,2033', 0o76035, '', '', '+2', 'ZERO..THIS VEHICLE (CM)', kind='operand', line=122)
W('37,2034', 0o01674, '', '', 'VINTFLAG', 'ONE...OTHER VEHICLE(LM)', kind='operand', line=123)
W('37,2035', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=124)
W('37,2036', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=125)
W('37,2037', 0o01673, '', '', 'INTYPFLG', 'PRECISION', kind='operand', line=126)
W('37,2040', 0o77624, '', 'CALL', kind='interp', line=127)
W('37,2041', 0o27162, '', '', 'INTEGRV', 'CALCULATE', kind='operand', line=128)
W('37,2042', 0o77650, '', 'GOTO', '', '.AND', kind='interp', line=129)
W('37,2043', 0o76065, '', '', 'P21VSAVE', '..SAVE BASE VECTOR', kind='operand', line=130)
W('37,2044', 0o77775, 'P21CONT', 'VLOAD', '', 'RECYCLE..INTEG FROM BASE VECTOR', kind='interp', line=131)
W('37,2045', 0o03605, '', '', 'P21BASER', kind='operand', line=132)
# Page 458
W('37,2046', 0o25535, '', 'STOVL', 'RCV', '..POS', kind='interp', line=134)
W('37,2047', 0o03613, '', '', 'P21BASEV', kind='operand', line=135)
W('37,2050', 0o15543, '', 'STODL', 'VCV', '..VEL', kind='interp', line=136)
W('37,2051', 0o02316, '', '', 'P21TIME', kind='operand', line=137)
W('37,2052', 0o01517, '', 'STORE', 'TET', '..TIME', kind='interp', line=138)
W('37,2053', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=139)
W('37,2054', 0o01676, '', '', 'DIM0FLAG', kind='operand', line=140)
W('37,2055', 0o00263, '', '', 'MOONFLAG', kind='operand', line=141)
W('37,2056', 0o53135, '', 'SLOAD', 'BZE', kind='interp', line=142)
W('37,2057', 0o03604, '', '', 'P21ORIG', kind='operand', line=143)
W('37,2060', 0o76063, '', '', '+3', 'ZERO = EARTH', kind='operand', line=144)
W('37,2061', 0o77614, '', 'SET', '', '...2 = MOON', kind='interp', line=145)
W('37,2062', 0o00063, '', '', 'MOONFLAG', kind='operand', line=146)
W('37,2063', 0o77624, '', 'CALL', kind='interp', line=147)
W('37,2064', 0o27135, '', '', 'INTEGRVS', kind='operand', line=148)
W('37,2065', 0o77745, 'P21VSAVE', 'DLOAD', '', 'SAVE CURRENT BASE VECTOR', kind='interp', line=149)
W('37,2066', 0o00015, '', '', 'TAT', kind='operand', line=150)
W('37,2067', 0o26316, '', 'STOVL', 'P21TIME', '..TIME', kind='interp', line=151)
W('37,2070', 0o00017, '', '', 'RATT1', kind='operand', line=152)
W('37,2071', 0o27605, '', 'STOVL', 'P21BASER', '..POS B-29 OR B-27', kind='interp', line=153)
W('37,2072', 0o00025, '', '', 'VATT1', kind='operand', line=154)
W('37,2073', 0o03613, '', 'STORE', 'P21BASEV', '..VEL B-7  OR B-5', kind='interp', line=155)
W('37,2074', 0o53646, '', 'ABVAL', 'SL*', kind='interp', line=156)
W('37,2075', 0o57576, '', '', '0,2', kind='operand', line=157)
W('37,2076', 0o27623, '', 'STOVL', 'P21VEL', '/VEL/ FOR N73 DSP', kind='interp', line=158)
W('37,2077', 0o00001, '', '', 'RATT', kind='operand', line=159)
W('37,2100', 0o50256, '', 'UNIT', 'DOT', kind='interp', line=160)
W('37,2101', 0o00007, '', '', 'VATT', 'U(R).(V)', kind='operand', line=161)
W('37,2102', 0o67471, '', 'DDV', 'ASIN', 'U(R).U(V)', kind='interp', line=162)
W('37,2103', 0o03623, '', '', 'P21VEL', kind='operand', line=163)
W('37,2104', 0o03625, '', 'STORE', 'P21GAM', 'SIN-1 U(R).U(V), -90 TO +90', kind='interp', line=164)
W('37,2105', 0o43134, '', 'SXA,2', 'SET', kind='interp', line=165)
W('37,2106', 0o03603, '', '', 'P21ORIG', '0 = EARTH  2 = MOON', kind='operand', line=166)
W('37,2107', 0o01063, '', '', 'P21FLAG', kind='operand', line=167)
W('37,2110', 0o67214, 'P21DSP', 'CLEAR', 'SLOAD', 'GENERATE DISPLAY DATA', kind='interp', line=168)
W('37,2111', 0o01663, '', '', 'LUNAFLAG', kind='operand', line=169)
W('37,2112', 0o00050, '', '', 'X2', kind='operand', line=170)
W('37,2113', 0o43054, '', 'BZE', 'SET', kind='interp', line=171)
W('37,2114', 0o76116, '', '', '+2', '0 = EARTH', kind='operand', line=172)
W('37,2115', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=173)
W('37,2116', 0o77775, '', 'VLOAD', kind='interp', line=174)
W('37,2117', 0o00001, '', '', 'RATT', kind='operand', line=175)
W('37,2120', 0o16152, '', 'STODL', 'ALPHAV', kind='interp', line=176)
W('37,2121', 0o00015, '', '', 'TAT', kind='operand', line=177)
W('37,2122', 0o45014, '', 'CLEAR', 'CALL', kind='interp', line=178)
W('37,2123', 0o00662, '', '', 'ERADFLAG', kind='operand', line=179)
W('37,2124', 0o26370, '', '', 'LAT-LONG', kind='operand', line=180)
W('37,2125', 0o77605, '', 'DMP', '', 'MPAC = ALT, METERS B-29', kind='interp', line=181)
W('37,2126', 0o36154, '', '', 'K.01', kind='operand', line=182)
W('37,2127', 0o03621, '', 'STORE', 'P21ALT', 'ALT/100 FOR N73 DSP', kind='interp', line=183)
# Page 459
W('37,2130', 0o77776, '', 'EXIT', kind='interp', line=185)
W('37,2131', 0o32151, '', 'CAF', 'V06N43', 'DISPLAY LAT,LONG,ALT', line=186)
W('37,2132', 0o04662, '', 'TC', 'BANKCALL', 'LAT,LONG = REVS B0 BOTH EARTH/MOON', line=187)
W('37,2133', 0o20720, '', 'CADR', 'GOFLASH', 'ALT = METERS B-29  BOTH EARTH/MOON', kind='data', line=188)
W('37,2134', 0o04106, '', 'TC', 'GOTOPOOH', 'TERM', line=189)
W('37,2135', 0o04106, '', 'TC', 'GOTOPOOH', line=190)
W('37,2136', 0o06006, '', 'TC', 'INTPRET', 'V32E RECYCLE', line=191)
W('37,2137', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=192)
W('37,2140', 0o02316, '', '', 'P21TIME', kind='operand', line=193)
W('37,2141', 0o36146, '', '', '600SEC', '600 SECONDS OR 10 MIN', kind='operand', line=194)
W('37,2142', 0o01046, '', 'STORE', 'DSPTEM1', kind='interp', line=195)
W('37,2143', 0o77634, '', 'RTB', kind='interp', line=196)
W('37,2144', 0o76011, '', '', 'P21PROG1', kind='operand', line=197)
W('37,2145', 0o00003, '600SEC', '2DEC', '60000', '10 MIN', kind='data', line=198)
W('37,2146', 0o25140, kind='data', line=198)

W('37,2147', 0o00001, 'P21ONENN', 'OCT', '00001', 'NEEDED TO DETERMINE VEHICLE', kind='data', line=200)
W('37,2150', 0o00000, '', 'OCT', '00000', 'TO BE INTEGRATED', kind='data', line=201)
W('37,2151', 0o01453, 'V06N43', 'VN', '00643', kind='data', line=202)
W('37,2152', 0o01442, 'V6N34', 'VN', '00634', kind='data', line=203)
W('37,2153', 0o00243, 'K.01', '2DEC', '.01', kind='data', line=204)
W('37,2154', 0o32703, kind='data', line=204)
