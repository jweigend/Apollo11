"""P76.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/P76.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 709-711 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('P76', 'P76.agc', 'Luminary099', pages='709-711')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     P76.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        709-711
# Mod history:  2009-05-19 RSB  Adapted from the corresponding
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

# Page 709
# 1) PROGRAM NAME - TARGET DELTA V PROGRAM (P76).
# 2) FUNCTIONAL DESCRIPTION - UPON ENTRY BY ASTRONAUT ACTION, P76 FLASHES DSKY REQUESTS TO THE ASTRONAUT
# TO PROVIDE VIA DSKY (1) THE DELTA V TO BE APPLIED TO THE OTHER VEHICLE STATE VECTOR AND (2) THE
# TIME (TIG) AT WHICH THE OTHER VEHICLE VELOCITY WAS CHANGED BY EXECUTION OF A THRUSTING MANEUVER. THE
# OTHER VEHICLE STATE VECTOR IS INTEGRATED TO TIG AND UPDATED BY THE ADDITION OF DELTA V (DELTA V HAVING
# BEEN TRANSFORMED FROM LV TO REF COSYS).  USING INTEGRVS, THE PROGRAM THEN INTEGRATES THE OTHER
# VEHICLE STATE VECTOR TO THE STATE VECTOR OF THIS VEHICLE, THUS INSURING THAT THE W-MATRIX AND BOTH VEHICLE
# STATES CORRESPOND TO THE SAME TIME.
# 3) ERASABLE INIITIALIZATION REQUIRED - NONE.
# 4) CALLING SEQUENCES AND EXIT MODES - CALLED BY ASTRONAUT REQUEST THRU DSKY V 37 E 76 E.
# EXITS BY TCF ENDOFJOB.
# 5) OUTPUT -- OTHER VEHICLE STATE VECTOR INTEGRATED TO TIG AND INCREMENTED BY DELTA V IN REF COSYS.
# THE PUSHLIST CONTAINS THE MATRIX BY WHICH THE INPUT DELTA V MUST BE POST-MULTIPLIED TO CONVERT FROM LV
# TO REF COSYS.
# 6) DEBRIS - OTHER VEHICLE STATE VECTOR.
# 7) SUBROUTINES CALLED - BANKCALL, GOXDSPF, CSMPREC (OR LEMPREC), ATOPCSM (OR ATOPLEM), INTSTALL, INTWAKE, PHASCHNG
# INTPRET, INTEGRVS, AND MINIRECT.
# 8) FLAG USE - MOONFLAG, CMOONFLG, INTYPFLG, RASFLAG, AND MARKCTR.

#   BANK 30
#   SETLOC P76LOC
#   BANK

#   COUNT* $$/P76

#   EBANK= TIG

W('13,2207', 0o05504, 'P76', 'TC', 'UPFLAG', line=57)
W('13,2210', 0o00031, '', 'ADRES', 'TRACKFLG', kind='data', line=58)

W('13,2211', 0o06037, '', 'TC', 'INTPRET', line=60)
W('13,2212', 0o77775, '', 'VLOAD', kind='interp', line=61)
W('13,2213', 0o03434, '', '', 'DELVLVC', kind='operand', line=62)
W('13,2214', 0o02223, '', 'STORE', 'DELVOV', kind='interp', line=63)
W('13,2215', 0o77776, '', 'EXIT', kind='interp', line=64)

W('13,2216', 0o32336, '', 'CAF', 'V06N84', 'FLASH LAST DELTA V,', line=66)
W('13,2217', 0o04616, '', 'TC', 'BANKCALL', 'AND WAIT FOR KEYBOARD ACTION.', line=67)
W('13,2220', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=68)
W('13,2221', 0o12333, '', 'TCF', 'ENDP76', line=69)
W('13,2222', 0o02224, '', 'TC', '+2', 'PROCEED', line=70)
W('13,2223', 0o02216, '', 'TC', '-5', 'STORE DATA AND REPEAT FLASHING', line=71)
W('13,2224', 0o32337, '', 'CAF', 'V06N84 +1', 'FLASH VERB 06 NOUN 33, DISPLAY LAST TIG,', line=72)
W('13,2225', 0o04616, '', 'TC', 'BANKCALL', 'AND WAIT FOR KEYBOARD ACTION.', line=73)
W('13,2226', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=74)
W('13,2227', 0o12333, '', 'TCF', 'ENDP76', line=75)
W('13,2230', 0o02232, '', 'TC', '+2', line=76)
W('13,2231', 0o02224, '', 'TC', '-5', line=77)
W('13,2232', 0o06037, '', 'TC', 'INTPRET', 'RETURN TO INTERPRETIVE CODE', line=78)
# Page 710
W('13,2233', 0o77745, '', 'DLOAD', '', 'SET D(MPAC)=TIG IN CSEC B28', kind='interp', line=80)
W('13,2234', 0o03442, '', '', 'TIG', kind='operand', line=81)
W('13,2235', 0o34041, '', 'STCALL', 'TDEC1', 'SET TDEC1=TIG FOR ORBITAL INTEGRATION', kind='interp', line=82)
W('13,2236', 0o27043, '', '', 'OTHPREC', kind='operand', line=83)
W('13,2237', 0o53575, 'COMPMAT', 'VLOAD', 'UNIT', kind='interp', line=84)
W('13,2240', 0o00001, '', '', 'RATT', kind='operand', line=85)
W('13,2241', 0o77676, '', 'VCOMP', '', 'U(-R)', kind='interp', line=86)
W('13,2242', 0o00031, '', 'STORE', '24D', 'U(-R) TO 24D', kind='interp', line=87)
W('13,2243', 0o53435, '', 'VXV', 'UNIT', 'U(-R) XV = U(VXR)', kind='interp', line=88)
W('13,2244', 0o00007, '', '', 'VATT', kind='operand', line=89)
W('13,2245', 0o00023, '', 'STORE', '18D', kind='interp', line=90)
W('13,2246', 0o53435, '', 'VXV', 'UNIT', 'U(VXR)XU(-R) = U((RXV)XR)', kind='interp', line=91)
W('13,2247', 0o00031, '', '', '24D', kind='operand', line=92)
W('13,2250', 0o24015, '', 'STOVL', '12D', kind='interp', line=93)
W('13,2251', 0o02223, '', '', 'DELVOV', kind='operand', line=94)
W('13,2252', 0o76505, '', 'VXM', 'VSL1', 'V(MPAC)=DELTA V IN REFCOSYS', kind='interp', line=95)
W('13,2253', 0o00015, '', '', '12D', kind='operand', line=96)
W('13,2254', 0o77655, '', 'VAD', kind='interp', line=97)
W('13,2255', 0o00007, '', '', 'VATT', kind='operand', line=98)
W('13,2256', 0o00007, '', 'STORE', '6', 'V(PD6)=VATT + DELTA V', kind='interp', line=99)
W('13,2257', 0o77624, '', 'CALL', '', 'PRESENT WOULD-BE USER OF ORBITAL', kind='interp', line=100)
W('13,2260', 0o27414, '', '', 'INTSTALL', 'INTEG FROM INTERFERING WITH UPDATING', kind='operand', line=101)
W('13,2261', 0o77624, '', 'CALL', kind='interp', line=102)
W('13,2262', 0o26340, '', '', 'P76SUB1', kind='operand', line=103)
W('13,2263', 0o53775, '', 'VLOAD', 'VSR*', kind='interp', line=104)
W('13,2264', 0o00007, '', '', '6', kind='operand', line=105)
W('13,2265', 0o57176, '', '', '0,2', kind='operand', line=106)
W('13,2266', 0o25543, '', 'STOVL', 'VCV', kind='interp', line=107)
W('13,2267', 0o00001, '', '', 'RATT', kind='operand', line=108)
W('13,2270', 0o77657, '', 'VSR*', kind='interp', line=109)
W('13,2271', 0o57176, '', '', '0,2', kind='operand', line=110)
W('13,2272', 0o15535, '', 'STODL', 'RCV', kind='interp', line=111)
W('13,2273', 0o03442, '', '', 'TIG', kind='operand', line=112)
W('13,2274', 0o01517, '', 'STORE', 'TET', kind='interp', line=113)
W('13,2275', 0o71214, '', 'CLEAR', 'DLOAD', kind='interp', line=114)
W('13,2276', 0o01673, '', '', 'INTYPFLG', kind='operand', line=115)
W('13,2277', 0o01643, '', '', 'TETTHIS', kind='operand', line=116)
W('13,2300', 0o34041, 'INTOTHIS', 'STCALL', 'TDEC1', kind='interp', line=117)
W('13,2301', 0o27107, '', '', 'INTEGRVS', kind='operand', line=118)
W('13,2302', 0o77624, '', 'CALL', kind='interp', line=119)
W('13,2303', 0o27414, '', '', 'INTSTALL', kind='operand', line=120)
W('13,2304', 0o77775, '', 'VLOAD', kind='interp', line=121)
W('13,2305', 0o00017, '', '', 'RATT1', kind='operand', line=122)
W('13,2306', 0o01503, '', 'STORE', 'RRECT', kind='interp', line=123)
W('13,2307', 0o15535, '', 'STODL', 'RCV', kind='interp', line=124)
W('13,2310', 0o00015, '', '', 'TAT', kind='operand', line=125)
W('13,2311', 0o25517, '', 'STOVL', 'TET', kind='interp', line=126)
W('13,2312', 0o00025, '', '', 'VATT1', kind='operand', line=127)
W('13,2313', 0o77624, '', 'CALL', kind='interp', line=128)
W('13,2314', 0o23455, '', '', 'MINIRECT', kind='operand', line=129)
# Page 711
W('13,2315', 0o77776, '', 'EXIT', kind='interp', line=131)
W('13,2316', 0o05353, '', 'TC', 'PHASCHNG', line=132)
W('13,2317', 0o04024, '', 'OCT', '04024', kind='data', line=133)

W('13,2320', 0o05504, '', 'TC', 'UPFLAG', line=135)
W('13,2321', 0o00236, '', 'ADRES', 'REINTFLG', kind='data', line=136)

W('13,2322', 0o06037, '', 'TC', 'INTPRET', line=138)
W('13,2323', 0o77624, '', 'CALL', kind='interp', line=139)
W('13,2324', 0o26661, '', '', 'ATOPOTH', kind='operand', line=140)
W('13,2325', 0o77531, '', 'SSP', 'EXIT', kind='interp', line=141)
W('13,2326', 0o00053, '', '', 'QPRET', kind='operand', line=142)
W('13,2327', 0o26332, '', '', 'OUT', kind='operand', line=143)
W('13,2330', 0o04616, '', 'TC', 'BANKCALL', 'PERMIT USE OF ORBITAL INTEGRATION', line=144)
W('13,2331', 0o27445, '', 'CADR', 'INTWAKE1', kind='data', line=145)
W('13,2332', 0o77776, 'OUT', 'EXIT', kind='interp', line=146)
W('13,2333', 0o34755, 'ENDP76', 'CAF', 'ZERO', line=147)
W('13,2334', 0o55462, '', 'TS', 'MARKCTR', 'CLEAR RR TRACKING MARK COUNTER', line=148)
W('13,2335', 0o16001, '', 'TCF', 'GOTOPOOH', line=149)

W('13,2336', 0o01524, 'V06N84', 'NV', '0684', kind='data', line=151)
W('13,2337', 0o01441, '', 'NV', '0633', kind='data', line=152)
W('13,2340', 0o43174, 'P76SUB1', 'AXT,2', 'SET', kind='interp', line=153)
W('13,2341', 0o00002, '', '', '2', kind='operand', line=154)
W('13,2342', 0o00063, '', '', 'MOONFLAG', 'SET MEANS MOON IS SPHERE OF INFLUENCE.', kind='operand', line=155)
W('13,2343', 0o77014, '', 'BON', 'AXT,2', kind='interp', line=156)
W('13,2344', 0o04303, '', '', 'CMOONFLG', 'SET MEANS PERM CM STATE IN LUNAR SPHERE.', kind='operand', line=157)
W('13,2345', 0o00052, '', '', 'QPRET', kind='operand', line=158)
W('13,2346', 0o00000, '', '', '0', kind='operand', line=159)
W('13,2347', 0o43414, '', 'CLEAR', 'RVQ', kind='interp', line=160)
W('13,2350', 0o00263, '', '', 'MOONFLAG', kind='operand', line=161)
