"""R63.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/R63.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 338-341 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('R63', 'R63.agc', 'Luminary099', pages='338-341')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     R63.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        338-341
# Mod history:  2009-05-16 RSB  Adapted from the corresponding
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

# Page 338
# SUBROUTINE NAME:      V89CALL
# MOD NO:       0                       DATE:           9 JAN 1968
# MOD BY:       DIGITAL DEVEL GROUP     LOG SECTION:    R63
#
# FUNCTIONAL DESCRIPTION:
#
# CALLED BY VERB 89 ENTER DURING P00.  PRIO 10 USED.  CALCULATES AND
# DISPLAYS FINAL FDAI BALL ANGLES TO POINT LM +X OR +Z AXIS AT CSM.
#
# 1. KEY IN V 89 E ONLY IF IN PROG 00.  IF NOT IN P00, OPERATOR ERROR AND
# EXIT R63, OTHERWISE CONTINUE.
#
# 2. IF IN P00, DO IMU STATUS CHECK ROUTINE (R02BOTH).  IF IMU ON AND ITS
# ORIENTATION KNOWN TO LGC, CONTINUE.
#
# 3. FLASH DISPLAY V 04 N 06.  R2 INDICATES WHICH SPACECRAFT AXIS IS TO
# BE POINTED AT CSM.  INITIAL CHOICE IS PREFERRED (+Z) AXIS (R2=1).
# ASTRONAUT CAN CHANGE TO (+X) AXIS (R2 NOT = 1) BY V 22 E 2 E.  CONTINUE
# AFTER KEYING IN PROCEED.
#
# 4. BOTH VEHICLE STATE VECTORS UPDATED BY CONIC EQS.
#
# 5. HALF MAGNITUDE UNIT LOS VECTOR (IN STABLE MEMBER COORDINATES) AND
# HALF MAGNITUDE UNIT SPACECRAFT AXIS VECTOR (IN BODY COORDINATES)
# PREPARED FOR VECPOINT.
#
# 6. GIMBAL ANGLES FROM VECPOINT TRANSFORMED INTO FDAI BALL ANGLES BY
# BALLANGS.  FLASH DISPLAY V 06 N 18 AND AWAIT RESPONSE.
#
# 7. RECYCLE - RETURN TO STEP 4.
# TERMINATE - EXIT R63.
# PROCEED - RESET 3AXISFLG AND CALL R60LEM FOR ATTITUDE MANEUVER.
#
# CALLING SEQUENCE:     V 89 E.
#
# SUBROUTINES CALLED:   CHKPOOH, R02BOTH, GOXDSPF, CSMCONIC, LEMCONIC,
# VECPOINT, BALLANGS, R60LEM.
#
# NORMAL EXIT MODES:    TC ENDEXT
#
# ALARMS:       1. OPERATOR ERROR IF NOT IN P00.
# 2. PROGRAM ALARM IF IMU IS OFF.
# 3. PROGRAM ALARM IF IMU ORIENTATION IS UNKNOWN.
#
# OUTPUT:       NONE
#
# ERASABLE INITIALIZATION REQUIRED:  NONE
#
# DEBRIS:       OPTION1, +1, TDEC1, PDINTVSM, SCAXIS, CPHI, CTHETA, CPSI,
# Page 339
# 3AXISFLG.

#   EBANK= RONE
#   BANK 32
#   SETLOC BAWLANGS
#   BANK

#   COUNT* $$/R63
W('26,2022', 0o04616, 'V89CALL', 'TC', 'BANKCALL', 'IMU STATUS CHECK.  RETURNS IF ORIENTATION', line=88)
W('26,2023', 0o11254, '', 'CADR', 'R02BOTH', 'KNOWN.  ALARMS IF NOT.', kind='data', line=89)
W('26,2024', 0o36245, '', 'CAF', 'THREE', 'ALLOW ASTRONAUT TO SELECT DESIRED', line=90)
W('26,2025', 0o55051, '', 'TS', 'OPTIONX', 'TRACKING ATTITUDE AXIS.', line=91)
W('26,2026', 0o34753, '', 'CAF', 'ONE', line=92)
W('26,2027', 0o55052, '', 'TS', 'OPTIONX +1', line=93)
W('26,2030', 0o32117, '', 'CAF', 'VB04N12', 'V 04 N 12', line=94)
W('26,2031', 0o04616, '', 'TC', 'BANKCALL', line=95)
W('26,2032', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=96)
W('26,2033', 0o05472, '', 'TC', 'ENDEXT', 'TERMINATE', line=97)
W('26,2034', 0o02036, '', 'TC', '+2', 'PROCEED', line=98)
W('26,2035', 0o02030, '', 'TC', '-5', 'DATA IN.  OPTION1+1 = 1 FOR Z AXIS', line=99)
W('26,2036', 0o06037, 'V89RECL', 'TC', 'INTPRET', '                      = 2 FOR X AXIS', line=100)
W('26,2037', 0o43234, '', 'RTB', 'DAD', kind='interp', line=101)
W('26,2040', 0o21573, '', '', 'LOADTIME', 'READ PRESENT TIME', kind='operand', line=102)
W('26,2041', 0o14122, '', '', 'DP1MIN', kind='operand', line=103)
W('26,2042', 0o02205, '', 'STORE', 'TSTART82', 'SAVE TIME FOR LEMCONIC CALL', kind='interp', line=104)
W('26,2043', 0o34041, '', 'STCALL', 'TDEC1', 'STORE TIME FOR CSMCONIC CALL', kind='interp', line=105)
W('26,2044', 0o27066, '', '', 'CSMCONIC', 'CSM STATE VECTOR UPDATE', kind='operand', line=106)
W('26,2045', 0o77775, '', 'VLOAD', '', 'CSMCONIC LEFT R VECTOR IN RATT', kind='interp', line=107)
W('26,2046', 0o00001, '', '', 'RATT', kind='operand', line=108)
W('26,2047', 0o16207, '', 'STODL', 'RONE', 'SAVE FOR LINE OF SIGHT (LOS) COMPUTATION', kind='interp', line=109)
W('26,2050', 0o02205, '', '', 'TSTART82', kind='operand', line=110)
W('26,2051', 0o34041, '', 'STCALL', 'TDEC1', 'STORE TIME FOR LEMCONIC CALL', kind='interp', line=111)
W('26,2052', 0o27100, '', '', 'LEMCONIC', 'LEM STATE VECTOR UPDATE', kind='operand', line=112)
W('26,2053', 0o52375, '', 'VLOAD', 'VSU', 'CSM POSITION - LEM POSITION = LOS', kind='interp', line=113)
W('26,2054', 0o02207, '', '', 'RONE', 'LOS VECTOR LEFT IN MPAC', kind='operand', line=114)
W('26,2055', 0o00001, '', '', 'RATT', kind='operand', line=115)
W('26,2056', 0o47121, '', 'MXV', 'RTB', '(REFSMAT X LOS).  TRANSFORMS LOS FROM', kind='interp', line=116)
W('26,2057', 0o01734, '', '', 'REFSMMAT', 'REFERENCE COORD TO STAB MEMB COORD.', kind='operand', line=117)
W('26,2060', 0o21726, '', '', 'NORMUNIT', kind='operand', line=118)
W('26,2061', 0o03773, '', 'STORE', 'POINTVSM', 'STORE LOS FOR VECPOINT CALCULATION', kind='interp', line=119)
W('26,2062', 0o77776, '', 'EXIT', kind='interp', line=120)
W('26,2063', 0o41052, '', 'CS', 'OPTIONX +1', '1 FOR Z AXIS.  2 FOR X AXIS.', line=121)
W('26,2064', 0o64753, '', 'AD', 'ONE', line=122)
W('26,2065', 0o00006, '', 'EXTEND', line=123)
W('26,2066', 0o12113, '', 'BZF', 'ALINEZ', line=124)
W('26,2067', 0o06037, 'ALINEX', 'TC', 'INTPRET', 'X AXIS ALIGNMENT', line=125)
W('26,2070', 0o77775, '', 'VLOAD', kind='interp', line=126)
W('26,2071', 0o06520, '', '', 'UNITX', 'READ (.5, 0, 0)', kind='operand', line=127)
# Page 340
W('26,2072', 0o37765, 'V89CALL1', 'STCALL', 'SCAXIS', 'STORE SELECTED ALIGNMENT AXIS', kind='interp', line=129)
W('26,2073', 0o56040, '', '', 'VECPOINT', 'PUTS DESIRED GIM ANG (OG,IG,MG) IN TMPAC', kind='operand', line=130)
W('26,2074', 0o00322, '', 'STORE', 'CPHI', 'STORE GIMBAL ANGLES FOR BALLANGS CALL.', kind='interp', line=131)
W('26,2075', 0o77776, '', 'EXIT', kind='interp', line=132)
W('26,2076', 0o04616, '', 'TC', 'BANKCALL', line=133)
W('26,2077', 0o54266, '', 'CADR', 'BALLANGS', 'PUTS DESIRED BALL ANGLE IN FDAIX,Y,Z', kind='data', line=134)
W('26,2100', 0o32120, '', 'CAF', 'VB06N18', 'V 06 N 18', line=135)
W('26,2101', 0o04616, '', 'TC', 'BANKCALL', 'NOUN 18 REFERS TO FDAIX,Y,Z', line=136)
W('26,2102', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=137)
W('26,2103', 0o05472, '', 'TC', 'ENDEXT', 'TERMINATE', line=138)
W('26,2104', 0o02106, '', 'TC', '+2', 'PROCEED', line=139)
W('26,2105', 0o02036, '', 'TC', 'V89RECL', 'RECYCLE', line=140)
W('26,2106', 0o05516, '', 'TC', 'DOWNFLAG', 'RESET 3 AXIS FLAG', line=141)
W('26,2107', 0o00124, '', 'ADRES', '3AXISFLG', 'RESET BIT6 FLAG WORD 5', kind='data', line=142)
W('26,2110', 0o04616, '', 'TC', 'BANKCALL', 'PERFORMS LEM MANEUVER TO ALIGN SELECTED', line=143)
W('26,2111', 0o54123, '', 'CADR', 'R60LEM', 'SPACECRAFT AXIS TO CSM.', kind='data', line=144)
W('26,2112', 0o15472, '', 'TCF', 'ENDEXT', 'TERMINATE R63', line=145)

W('26,2113', 0o06037, 'ALINEZ', 'TC', 'INTPRET', 'Z AXIS ALIGNMENT', line=147)
W('26,2114', 0o52175, '', 'VLOAD', 'GOTO', kind='interp', line=148)
W('26,2115', 0o06514, '', '', 'UNITZ', 'READ (0, 0, .5)', kind='operand', line=149)
W('26,2116', 0o54072, '', '', 'V89CALL1', kind='operand', line=150)

W('26,2117', 0o01014, 'VB04N12', 'VN', '412', kind='data', line=152)
W('26,2120', 0o01422, 'VB06N18', 'VN', '0618', kind='data', line=153)
# Page 341
W('26,2121', 0o00000, 'DP1MIN', '2DEC', '6000', kind='data', line=155)
W('26,2122', 0o13560, kind='data', line=155)
