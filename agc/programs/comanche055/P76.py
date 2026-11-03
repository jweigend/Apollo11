"""P76.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/P76.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 511-513 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P76', 'P76.agc', 'Comanche055', pages='511-513')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P76.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        pp  511-513
# Mod history:  2009-05-08 HG    Adapting from the Luminary131/ file
# of the same name, using Comanche055 page
# images 0511.jpg - 0513.jpg.
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

# Page 511
# 1)    PROGRAM NAME - TARGET DELTA V PROGRAM (P76).
# 2)    FUNCTIONAL DESCRIPTION - UPON ENTRY BY ASTRONAUT ACTION, P76 FLASHES DSKY REQUESTS TO THE ASTRONAUT
# TO PROVIDE VIA DSKY (1) THE DELTA V TO BE APPLIED TO THE OTHER VEHICLE STATE VECTOR AND (2) THE
# TIME (TIG) AT WHICH THE OTHER VEHICLE VELOCITY WAS CHANGED BY EXECUTION OF A THRUSTING MANEUVER. THE
# OTHER VEHICLE STATE VECTOR IS INTEGRATED TO TIG AND UPDATED BY THE ADDITION OF DELTA V (DELTA V HAVING
# BEEN TRANSFORMED FROM LV TO REF COSYS).  USING INTEGRVS, THE PROGRAM THEN INTEGRATES THE OTHER
# VEHICLE STATE VECTOR TO THE STATE VECTOR OF THIS VEHICLE, THUS INSURING THAT THE W-MATRIX AND BOTH VEHICLE
# STATES CORRESPOND TO THE SAME TIME.
# 3)    ERASABLE INITIALIZATION REQUIRED - NONE.
# 4)    CALLING SEQUENCES AND EXIT MODES - CALLED BY ASTRONAUT REQUEST THRU DSKY V 37 E 76 E.
# EXITS BY TCF ENDOFJOB.
# 5)    OUTPUT - OTHER VEHICLE STATE VECTOR INTEGRATED TO TIG AND INCREMENTED BY DELTA V IN REF COSYS.
# THE PUSHLIST CONTAINS THE MATRIX BY WHICH THE INPUT DELTA V MUST BE POST-MULTIPLIED TO CONVERT FROM LV
# TO REF COSYS.
# 6)    DEBRIS - OTHER VEHICLE STATE VECTOR.
# 7)    SUBROUTINES CALLED - BANKCALL,GOXDSPF,CSMPREC (OR LEMPREC),ATOPCSM (OR ATOPLEM),INTSTALL,INTWAKE, PHASCHNG
# INTPRET, INTEGRVS, AND MINIRECT.
# 8)    FLAG USE - MOONFLAG,CMOONFLG,INTYPFLG,RASFLAG, AND MARKCTR.

#   BANK 30
#   SETLOC P76LOC
#   BANK

#   COUNT* $$/P76

#   EBANK= TIG

W('13,2071', 0o05546, 'P76', 'TC', 'UPFLAG', line=59)
W('13,2072', 0o00031, '', 'ADRES', 'TRACKFLG', kind='data', line=60)

W('13,2073', 0o32220, '', 'CAF', 'V06N84', 'FLASH LAST DELTA V.', line=62)
W('13,2074', 0o04662, '', 'TC', 'BANKCALL', 'AND WAIT FOR KEYBOARD ACTION.', line=63)
W('13,2075', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=64)
W('13,2076', 0o12212, '', 'TCF', 'ENDP76', line=65)
W('13,2077', 0o02101, '', 'TC', '+2', 'PROCEED', line=66)
W('13,2100', 0o02073, '', 'TC', '-5', 'STORE DATA AND REPEAT FLASHING', line=67)
W('13,2101', 0o32221, '', 'CAF', 'V06N84 +1', 'FLASH VERB 06 NOUN 33, DISPLAY LAST TIG,', line=68)
W('13,2102', 0o04662, '', 'TC', 'BANKCALL', 'AND WAIT FOR KEYBOARD ACTION.', line=69)
W('13,2103', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=70)
W('13,2104', 0o12212, '', 'TCF', 'ENDP76', line=71)
W('13,2105', 0o02107, '', 'TC', '+2', line=72)
W('13,2106', 0o02101, '', 'TC', '-5', line=73)
W('13,2107', 0o06006, '', 'TC', 'INTPRET', 'RETURN TO INTERPRETIVE CODE', line=74)
W('13,2110', 0o77745, '', 'DLOAD', '', 'SET D(MPAC)=TIG IN CSEC B28', kind='interp', line=75)
W('13,2111', 0o03413, '', '', 'TIG', kind='operand', line=76)
W('13,2112', 0o34041, '', 'STCALL', 'TDEC1', 'SET TDEC1=TIG FOR ORBITAL INTEGRATION', kind='interp', line=77)
W('13,2113', 0o27105, '', '', 'OTHPREC', kind='operand', line=78)
W('13,2114', 0o53575, 'COMPMAT', 'VLOAD', 'UNIT', kind='interp', line=79)
W('13,2115', 0o00001, '', '', 'RATT', kind='operand', line=80)
# Page 512
W('13,2116', 0o77676, '', 'VCOMP', '', 'U(-R)', kind='interp', line=82)
W('13,2117', 0o00031, '', 'STORE', '24D', 'U(-R) TO 24D', kind='interp', line=83)
W('13,2120', 0o53435, '', 'VXV', 'UNIT', 'U(-R) X V = U(V X R)', kind='interp', line=84)
W('13,2121', 0o00007, '', '', 'VATT', kind='operand', line=85)
W('13,2122', 0o00023, '', 'STORE', '18D', kind='interp', line=86)
W('13,2123', 0o53435, '', 'VXV', 'UNIT', 'U(V X R) X U(-R) = U((R X V) X R)', kind='interp', line=87)
W('13,2124', 0o00031, '', '', '24D', kind='operand', line=88)
W('13,2125', 0o24015, '', 'STOVL', '12D', kind='interp', line=89)
W('13,2126', 0o03540, '', '', 'DELVOV', kind='operand', line=90)
W('13,2127', 0o76505, '', 'VXM', 'VSL1', 'V(MPAC)=DELTA V IN REFCOSYS', kind='interp', line=91)
W('13,2130', 0o00015, '', '', '12D', kind='operand', line=92)
W('13,2131', 0o77655, '', 'VAD', kind='interp', line=93)
W('13,2132', 0o00007, '', '', 'VATT', kind='operand', line=94)
W('13,2133', 0o00007, '', 'STORE', '6', 'V(PD6)=VATT + DELTA V', kind='interp', line=95)
W('13,2134', 0o77624, '', 'CALL', '', 'PREVENT WOULD-BE USER OF ORBITAL', kind='interp', line=96)
W('13,2135', 0o27442, '', '', 'INTSTALL', 'INTEG FROM INTERFERING WITH UPDATING', kind='operand', line=97)
W('13,2136', 0o77624, '', 'CALL', kind='interp', line=98)
W('13,2137', 0o26222, '', '', 'P76SUB1', kind='operand', line=99)
W('13,2140', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=100)
W('13,2141', 0o00007, '', '', '6', kind='operand', line=101)
W('13,2142', 0o57176, '', '', '0,2', kind='operand', line=102)
W('13,2143', 0o25543, '', 'STOVL', 'VCV', kind='interp', line=103)
W('13,2144', 0o00001, '', '', 'RATT', kind='operand', line=104)
W('13,2145', 0o77657, '', 'VSR*', kind='interp', line=105)
W('13,2146', 0o57176, '', '', '0,2', kind='operand', line=106)
W('13,2147', 0o15535, '', 'STODL', 'RCV', kind='interp', line=107)
W('13,2150', 0o03413, '', '', 'TIG', kind='operand', line=108)
W('13,2151', 0o01517, '', 'STORE', 'TET', kind='interp', line=109)
W('13,2152', 0o71214, '', 'CLEAR', 'DLOAD', kind='interp', line=110)
W('13,2153', 0o01673, '', '', 'INTYPFLG', kind='operand', line=111)
W('13,2154', 0o01571, '', '', 'TETTHIS', kind='operand', line=112)
W('13,2155', 0o34041, 'INTOTHIS', 'STCALL', 'TDEC1', kind='interp', line=113)
W('13,2156', 0o27135, '', '', 'INTEGRVS', kind='operand', line=114)
W('13,2157', 0o77624, '', 'CALL', kind='interp', line=115)
W('13,2160', 0o27442, '', '', 'INTSTALL', kind='operand', line=116)
W('13,2161', 0o77624, '', 'CALL', kind='interp', line=117)
W('13,2162', 0o26222, '', '', 'P76SUB1', 'SET/CLEAR MOONFLAG', kind='operand', line=118)
W('13,2163', 0o77775, '', 'VLOAD', kind='interp', line=119)
W('13,2164', 0o00017, '', '', 'RATT1', kind='operand', line=120)
W('13,2165', 0o01503, '', 'STORE', 'RRECT', kind='interp', line=121)
W('13,2166', 0o15535, '', 'STODL', 'RCV', kind='interp', line=122)
W('13,2167', 0o00015, '', '', 'TAT', kind='operand', line=123)
W('13,2170', 0o25517, '', 'STOVL', 'TET', kind='interp', line=124)
W('13,2171', 0o00025, '', '', 'VATT1', kind='operand', line=125)
W('13,2172', 0o77624, '', 'CALL', kind='interp', line=126)
W('13,2173', 0o23435, '', '', 'MINIRECT', kind='operand', line=127)
W('13,2174', 0o77776, '', 'EXIT', kind='interp', line=128)
W('13,2175', 0o05412, '', 'TC', 'PHASCHNG', line=129)
W('13,2176', 0o04024, '', 'OCT', '04024', kind='data', line=130)
# Page 513
W('13,2177', 0o05546, '', 'TC', 'UPFLAG', line=132)
W('13,2200', 0o00236, '', 'ADRES', 'REINTFLG', kind='data', line=133)

W('13,2201', 0o06006, '', 'TC', 'INTPRET', line=135)
W('13,2202', 0o77624, '', 'CALL', kind='interp', line=136)
W('13,2203', 0o26760, '', '', 'ATOPOTH', kind='operand', line=137)
W('13,2204', 0o77531, '', 'SSP', 'EXIT', kind='interp', line=138)
W('13,2205', 0o00053, '', '', 'QPRET', kind='operand', line=139)
W('13,2206', 0o26211, '', '', 'OUT', kind='operand', line=140)
W('13,2207', 0o04662, '', 'TC', 'BANKCALL', 'PERMIT USE OF ORBITAL INTEGRATION', line=141)
W('13,2210', 0o27477, '', 'CADR', 'INTWAKE1', kind='data', line=142)
W('13,2211', 0o77776, 'OUT', 'EXIT', kind='interp', line=143)
W('13,2212', 0o35021, 'ENDP76', 'CAF', 'ZERO', line=144)
W('13,2213', 0o55126, '', 'TS', 'MARKCTR', 'CLEAR RR TRACKING MARK COUNTER', line=145)
W('13,2214', 0o55125, '', 'TS', 'VHFCNT', line=146)

W('13,2215', 0o37716, '', 'CAF', 'NEGONE', line=148)
W('13,2216', 0o55734, '', 'TS', 'MRKBUF2', 'INVALIDATE MARK BUFFER', line=149)

W('13,2217', 0o14106, '', 'TCF', 'GOTOPOOH', line=151)

W('13,2220', 0o01524, 'V06N84', 'NV', '0684', kind='data', line=153)
W('13,2221', 0o01441, '', 'NV', '0633', kind='data', line=154)
W('13,2222', 0o67214, 'P76SUB1', 'CLEAR', 'SLOAD', kind='interp', line=155)
W('13,2223', 0o00263, '', '', 'MOONFLAG', kind='operand', line=156)
W('13,2224', 0o00050, '', '', 'X2', kind='operand', line=157)
W('13,2225', 0o43030, '', 'BHIZ', 'SET', 'X2=0...CLEAR MOONFLAG', kind='interp', line=158)
W('13,2226', 0o26230, '', '', '+2', '  =2.....SET MOONFLAG', kind='operand', line=159)
W('13,2227', 0o00063, '', '', 'MOONFLAG', kind='operand', line=160)
W('13,2230', 0o77616, '', 'RVQ', kind='interp', line=161)
