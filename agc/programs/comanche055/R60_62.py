"""R60_62.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/R60_62.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 390-398 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('R60_62', 'R60_62.agc', 'Comanche055', pages='390-398')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     R60_62.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        390-398
# Mod history:  2009-05-09 RSB  Adapted from the Colossus249/ file
# of the same name, using Comanche055 page
# images.
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

# Page 390
#   BANK 34
#   SETLOC MANUVER
#   BANK

#   EBANK= TEMPR60

#   COUNT 27/R60

# CONFORMS TO GSOP CHAPTER FOUR REVISION LOGIC 09 JAN 18,1968

W('27,2000', 0o04711, 'R60CSM', 'TC', 'MAKECADR', line=42)
W('27,2001', 0o55146, '', 'TS', 'TEMPR60', line=43)

# INSERT PRIODSP CHECK WITH R22 (V06N49) WITH JENNINGS BRODEUR

W('27,2002', 0o35012, 'REDOMANN', 'CAF', 'BIT6', line=47)
W('27,2003', 0o70101, '', 'MASK', 'FLAGWRD5', 'IS 3-AXIS FLAG SET', line=48)
W('27,2004', 0o10000, '', 'CCS', 'A', line=49)
W('27,2005', 0o12013, '', 'TCF', 'TOBALL', 'YES', line=50)
W('27,2006', 0o06006, '', 'TC', 'INTPRET', line=51)
W('27,2007', 0o77624, '', 'CALL', kind='interp', line=52)
W('27,2010', 0o56126, '', '', 'VECPOINT', 'TO COMPUTE FINAL ANGLES', kind='operand', line=53)
W('27,2011', 0o01156, '', 'STORE', 'CPHI', 'STORE FINAL ANGLES - CPHI,CTHETA,CPSI', kind='interp', line=54)
W('27,2012', 0o77776, '', 'EXIT', kind='interp', line=55)

W('27,2013', 0o32125, 'TOBALL', 'CAF', 'V06N18', line=57)
W('27,2014', 0o04662, '', 'TC', 'BANKCALL', line=58)
W('27,2015', 0o21132, '', 'CADR', 'GOPERF2R', 'DISPLAY PLEASE PERFORM AUTO MANEUVER', kind='data', line=59)
W('27,2016', 0o02114, '', 'TC', 'R61TEST', line=60)
W('27,2017', 0o02023, '', 'TC', 'REDOMANC', 'PROCEED', line=61)
W('27,2020', 0o12052, '', 'TCF', 'ENDMANU1', 'ENTER I.E. FINISHED WITH R60', line=62)

W('27,2021', 0o02056, '', 'TC', 'CHKLINUS', 'TO CHECK FOR PRIORITY DISPLAYS', line=64)
W('27,2022', 0o05217, '', 'TC', 'ENDOFJOB', line=65)

W('27,2023', 0o35012, 'REDOMANC', 'CAF', 'BIT6', line=67)
W('27,2024', 0o70101, '', 'MASK', 'FLAGWRD5', 'IS 3-AXIS FLAG SET', line=68)
W('27,2025', 0o10000, '', 'CCS', 'A', line=69)
W('27,2026', 0o12034, '', 'TCF', 'TOBALLC', 'YES', line=70)
W('27,2027', 0o06006, '', 'TC', 'INTPRET', line=71)
W('27,2030', 0o77624, '', 'CALL', kind='interp', line=72)
W('27,2031', 0o56126, '', '', 'VECPOINT', 'TO COMPUTE FINAL ANGLES', kind='operand', line=73)
W('27,2032', 0o01156, '', 'STORE', 'CPHI', 'STORE ANGLES', kind='interp', line=74)
W('27,2033', 0o77776, '', 'EXIT', kind='interp', line=75)

W('27,2034', 0o34371, 'TOBALLC', 'CAF', 'PRIO30', 'IS MODE AUTO AND CTL GNC', line=77)
# Page 391
W('27,2035', 0o00006, '', 'EXTEND', line=79)
W('27,2036', 0o06031, '', 'RXOR', 'CHAN31', line=80)
W('27,2037', 0o77707, '', 'MASK', '13,14,15', line=81)
W('27,2040', 0o00006, '', 'EXTEND', line=82)
W('27,2041', 0o12043, '', 'BZF', '+2', 'AUTO, NON-FLASH N18', line=83)
W('27,2042', 0o12013, '', 'TCF', 'TOBALL', 'NOT AUTO', line=84)

W('27,2043', 0o32125, '', 'CAF', 'V06N18', 'SET UP NON-FLASHING V06 N18', line=86)
W('27,2044', 0o04662, '', 'TC', 'BANKCALL', line=87)
W('27,2045', 0o20676, '', 'CADR', 'GODSPR', kind='data', line=88)
W('27,2046', 0o02056, '', 'TC', 'CHKLINUS', line=89)

W('27,2047', 0o04662, 'STARTMNV', 'TC', 'BANKCALL', line=91)
W('27,2050', 0o17627, '', 'CADR', 'GOMANUR', kind='data', line=92)
W('27,2051', 0o12013, 'ENDMANUV', 'TCF', 'TOBALL', 'FINISHED MANEUVER', line=93)

W('27,2052', 0o05560, 'ENDMANU1', 'TC', 'DOWNFLAG', 'RESET 3-AXIS FLAG', line=95)
W('27,2053', 0o00124, '', 'ADRES', '3AXISFLG', 'BIT 6 FLAG 5', kind='data', line=96)
W('27,2054', 0o31146, '', 'CAE', 'TEMPR60', line=97)
W('27,2055', 0o04704, '', 'TC', 'BANKJUMP', line=98)

W('27,2056', 0o40100, 'CHKLINUS', 'CS', 'FLAGWRD4', line=100)
W('27,2057', 0o75004, '', 'MASK', 'BIT12', 'IS PRIORITY DISPLAY FLAG SET', line=101)
W('27,2060', 0o10000, '', 'CCS', 'A', line=102)
W('27,2061', 0o00002, '', 'TC', 'Q', 'NO - EXIT', line=103)
W('27,2062', 0o30002, '', 'CA', 'Q', line=104)
W('27,2063', 0o54156, '', 'TS', 'MPAC +2', 'SAVE RETURN', line=105)
W('27,2064', 0o46214, '', 'CS', 'THREE', 'OBTAIN LOCATION FOR RESTART.', line=106)
W('27,2065', 0o60133, '', 'AD', 'BUF2', 'HOLDS Q OF LAST DISPLAY', line=107)
W('27,2066', 0o55053, '', 'TS', 'TBASE1', line=108)

W('27,2067', 0o05412, '', 'TC', 'PHASCHNG', line=110)
W('27,2070', 0o00071, '', 'OCT', '71', '1.7SPOT FOR RELINUS', kind='data', line=111)

W('27,2071', 0o35011, '', 'CAF', 'BIT7', line=113)
W('27,2072', 0o05526, '', 'TC', 'LINUS', 'GO SET BITS FOR PRIORITY DISPLAY', line=114)
W('27,2073', 0o00156, '', 'TC', 'MPAC +2', line=115)

W('27,2074', 0o35013, 'RELINUS', 'CAF', 'BIT5', 'IS TRACK FLAG ON', line=117)
W('27,2075', 0o70075, '', 'MASK', 'FLAGWRD1', line=118)
W('27,2076', 0o00006, '', 'EXTEND', line=119)
W('27,2077', 0o12111, '', 'BZF', 'GOREDO20', 'NO', line=120)

W('27,2100', 0o05546, '', 'TC', 'UPFLAG', line=122)
W('27,2101', 0o00077, '', 'ADRES', 'PDSPFLAG', 'R60 PRIODSP FLAG', kind='data', line=123)

W('27,2102', 0o05546, '', 'TC', 'UPFLAG', line=125)
W('27,2103', 0o00024, '', 'ADRES', 'TARG1FLG', 'FOR R52', kind='data', line=126)

W('27,2104', 0o35021, '', 'CAF', 'ZERO', 'RESET TO ZERO, SINCE', line=128)
# Page 392
W('27,2105', 0o55303, '', 'TS', 'OPTIND', 'OPTIND WAS SET TO -1 BY V379', line=130)

W('27,2106', 0o35066, '', 'CAF', 'PRIO14', 'RESTORE ORIGINAL PRIORITY', line=132)
W('27,2107', 0o05210, '', 'TC', 'PRIOCHNG', line=133)

W('27,2110', 0o01053, '', 'TC', 'TBASE1', line=135)

W('27,2111', 0o05412, 'GOREDO20', 'TC', 'PHASCHNG', line=137)
W('27,2112', 0o00111, '', 'OCT', '111', '1.11 FOR PIKUP20', kind='data', line=138)

W('27,2113', 0o05217, '', 'TC', 'ENDOFJOB', line=140)

W('27,2114', 0o31011, 'R61TEST', 'CA', 'MODREG', 'ARE WE IN P00.  IF YES THIS MUST BE', line=142)
W('27,2115', 0o00006, '', 'EXTEND', '', '      VERB49 OR VERB89 SO DO ENDEXT.', line=143)
W('27,2116', 0o12052, '', 'BZF', 'ENDMANU1', 'RESET 3-AXIS & RUTURN.  USER DOES ENDEXT', line=144)
W('27,2117', 0o30100, '', 'CA', 'FLAGWRD4', 'ARE WE IN R61 (P20)', line=145)
W('27,2120', 0o75004, '', 'MASK', 'BIT12', line=146)
W('27,2121', 0o00006, '', 'EXTEND', line=147)
W('27,2122', 0o14106, '', 'BZF', 'GOTOPOOH', 'NO', line=148)
W('27,2123', 0o04622, '', 'TC', 'GOTOV56', 'YES', line=149)

W('27,2124', 0o20100, 'BIT14+7', 'OCT', '20100', kind='data', line=151)
W('27,2125', 0o01422, 'V06N18', 'VN', '0618', kind='data', line=152)

# Page 393
# PROGRAM DESCRIPTION - VECPOINT

# THIS INTERPRETIVE SUBROUTINE MAY BE USED TO POINT A SPACECRAFT AXIS IN A DESIRED DIRECTION.  THE AXIS
# TO BE POINTED MUST APPEAR AS A HALF UNIT DOUBLE PRECISION VECTOR IN SUCCESSIVE LOCATIONS OF ERASABLE MEMORY
# BEGINNING WITH THE LOCATION CALLED SCAXIS.  THE COMPONENTS OF THIS VECTOR ARE GIVEN IN SPACECRAFT COORDINATES.
# THE DIRECTION IN WHICH THIS AXIS IS TO BE POINTED MUST APPEAR AS A HALF UNIT DOUBLE PRECISION VECTOR IN
# SUCCESSIVE LOCATIONS OF ERASABLE MEMORY BEGINNING WITH THE ADDRESS CALLED POINTVSM.  THE COMPONENTS OF THIS
# VECTOR ARE GIVEN IN STABLE MEMBER COORDINATES.  WITH THIS INFORMATION VECPOINT COMPUTES A SET OF THREE GIMBAL
# ANGLES (2S COMPLEMENT) CORRESPONDING TO THE CROSS-PRODUCT ROTATION BETWEEN SCAXIS AND POINTVSM AND STORES THEM
# IN T(MPAC) BEFORE RETURNING TO THE CALLER.
# THIS ROTATION, HOWEVER, MAY BRING THE S/C INTO GIMBAL LOCK.  WHEN POINTING A VECTOR IN THE Y-Z PLANE,
# THE TRANSPONDER AXIS, OR THE AOT FOR THE LEM, THE PROGRAM WILL CORRECT THIS PROBLEM BY ROTATING THE CROSS-
# PRODUCT ATTITUDE ABOUT POINTVSM BY A FIXED AMOUNT SUFFICIENT TO ROTATE THE DESIRED S/C ATTITUDE OUT OF GIMBAL
# LOCK.  IF THE AXIS TO BE POINTED IS MORE THAN 40.6 DEGREES BUT LESS THAN 60.5 DEG FROM THE +X (OR-X) AXIS,
# THE ADDITIONAL ROTATION TO AVOID GIMBAL LOCK IS 35 DEGREES.  IF THE AXIS IS MORE THAN 60.5 DEGREES FROM +X (OR -X)
# THE ADDITIONAL ROTATION IS 35 DEGREES.  THE GIMBAL ANGLES CORRESPONDING TO THIS ATTITUDE ARE THEN COMPUTED AND
# STORED AS 2S COMPLIMENT ANGLES IN T(MPAC) BEFORE RETURNING TO THE CALLER.
# WHEN POINTING THE X-AXIS, OR THE THRUST VECTOR, OR ANY VECTOR WITHIN 40.6 DEG OF THE X-AXIS, VECPOINT
# CANNOT CORRECT FOR A CROSS-PRODUCT ROTATION INTO GIMBAL LOCK.  IN THIS CASE A PLATFORM REALIGNMENT WOULD BE
# REQUIRED TO POINT THE VECTOR IN THE DESIRED DIRECTION.  AT PRESENT NO INDICATION IS GIVEN FOR THIS SITUATION
# EXCEPT THAT THE FINAL MIDDLE GIMBAL ANGLE IN MPAC +2 IS GREATER THAN 59 DEGREES.

# CALLING SEQUENCE -
# 1) LOAD SCAXIS, POINTVSM
# 2) CALL
# VECPOINT

# RETURNS WITH

# 1) DESIRED OUTER GIMBAL ANGLE IN MPAC
# 2) DESIRED INNER GIMBAL ANGLE IN MPAC +1
# 3) DESIRED MIDDLE GIMBAL ANGLE IN MPAC +2

# ERASABLES USED -

# 1) SCAXIS               6
# 2) POINTVSM             6
# 3) MIS                  18
# 4) DEL                  18
# 5) COF                  6
# 6) VECQTEMP             1
# 7) ALL OF VAC AREA      43

# TOTAL   99

#   SETLOC VECPT
#   BANK
# Page 394
#   EBANK= BCDU

#   COUNT 27/VECPT

W('27,2126', 0o40020, 'VECPOINT', 'STQ', 'BOV', 'SAVE RETURN ADDRESS', kind='interp', line=209)
W('27,2127', 0o03310, '', '', 'VECQTEMP', kind='operand', line=210)
W('27,2130', 0o56131, '', '', 'VECLEAR', 'AND CLEAR OVFIND', kind='operand', line=211)
W('27,2131', 0o47164, 'VECLEAR', 'AXC,2', 'RTB', kind='interp', line=212)
W('27,2132', 0o03320, '', '', 'MIS', 'READ THE PRESENT CDU ANGLES AND', kind='operand', line=213)
W('27,2133', 0o44376, '', '', 'READCDUK', 'STORE THEM IN PD25, 26, 27', kind='operand', line=214)
W('27,2134', 0o34032, '', 'STCALL', '25D', kind='interp', line=215)
W('27,2135', 0o44405, '', '', 'CDUTODCM', 'S/C AXES TO STABLE MEMBER AXES (MIS)', kind='operand', line=216)
W('27,2136', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=217)
W('27,2137', 0o03357, '', '', 'POINTVSM', 'RESOLVE THE POINTING DIRECTION VF INTO', kind='operand', line=218)
W('27,2140', 0o03321, '', '', 'MIS', 'INITIAL S/C AXES ( VF = POINTVSM)', kind='operand', line=219)
W('27,2141', 0o77656, '', 'UNIT', kind='interp', line=220)
W('27,2142', 0o00035, '', 'STORE', '28D', kind='interp', line=221)
# PD 28 29 30 31 32 33
W('27,2143', 0o53435, '', 'VXV', 'UNIT', 'TAKE THE CROSS PRODUCT VF X VI', kind='interp', line=223)
W('27,2144', 0o03351, '', '', 'SCAXIS', 'WHERE VI = SCAXIS', kind='operand', line=224)
W('27,2145', 0o57400, '', 'BOV', 'VCOMP', kind='interp', line=225)
W('27,2146', 0o56256, '', '', 'PICKAXIS', kind='operand', line=226)
W('27,2147', 0o17343, '', 'STODL', 'COF', 'CHECK MAGNITUDE', kind='interp', line=227)
W('27,2150', 0o00045, '', '', '36D', 'OF CROSS PRODUCT', kind='operand', line=228)
W('27,2151', 0o50025, '', 'DSU', 'BMN', 'VECTOR, IF LESS', kind='interp', line=229)
W('27,2152', 0o16327, '', '', 'DPB-14', 'THAN B-14 ASSUME', kind='operand', line=230)
W('27,2153', 0o56256, '', '', 'PICKAXIS', 'UNIT OPERATION', kind='operand', line=231)
W('27,2154', 0o50375, '', 'VLOAD', 'DOT', '      INVALID.', kind='interp', line=232)
W('27,2155', 0o03351, '', '', 'SCAXIS', kind='operand', line=233)
W('27,2156', 0o00035, '', '', '28D', kind='operand', line=234)
W('27,2157', 0o65552, '', 'SL1', 'ARCCOS', kind='interp', line=235)
W('27,2160', 0o77624, 'COMPMATX', 'CALL', '', 'NOW COMPUTE THE TRANSFORMATION FROM', kind='interp', line=236)
W('27,2161', 0o44530, '', '', 'DELCOMP', 'FINAL S/C AXES TO INITIAL S/C AXES MFI', kind='operand', line=237)
W('27,2162', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=238)
W('27,2163', 0o03320, '', '', 'MIS', 'COMPUTE THE TRANSFORMATION FROM FINAL', kind='operand', line=239)
W('27,2164', 0o03425, '', '', 'DEL', 'S/C AXES TO STABLE MEMBER AXES', kind='operand', line=240)
W('27,2165', 0o77624, '', 'CALL', '', 'MFS = MIS MFI', kind='interp', line=241)
W('27,2166', 0o44304, '', '', 'MXM3', '(IN PD LIST)', kind='operand', line=242)

W('27,2167', 0o51545, '', 'DLOAD', 'ABS', kind='interp', line=244)
W('27,2170', 0o00007, '', '', '6', 'MFS6 = SIN(CPSI)                      $2', kind='operand', line=245)
W('27,2171', 0o50025, '', 'DSU', 'BMN', kind='interp', line=246)
W('27,2172', 0o16314, '', '', 'SINGIMLC', '= SIN(59 DEGS)                        $2', kind='operand', line=247)
W('27,2173', 0o56246, '', '', 'FINDGIMB', '/CPSI/ LESS THAN 59 DEGS', kind='operand', line=248)
# I.E. DESIRED ATTITUDE NOT IN GIMBAL LOCK

W('27,2174', 0o51545, '', 'DLOAD', 'ABS', 'CHECK TO SEE IF WE ARE POINTING', kind='interp', line=251)
W('27,2175', 0o03351, '', '', 'SCAXIS', 'THE THRUST AXIS', kind='operand', line=252)
W('27,2176', 0o51025, '', 'DSU', 'BPL', kind='interp', line=253)
W('27,2177', 0o16316, '', '', 'SINVEC1', 'SIN 49.4 DEGS                         $2', kind='operand', line=254)
# Page 395
W('27,2200', 0o56246, '', '', 'FINDGIMB', 'IF SO, WE ARE TRYING TO POINT IT INTO', kind='operand', line=256)
W('27,2201', 0o77775, '', 'VLOAD', '', 'GIMBAL LOCK, ABORT COULD GO HERE', kind='interp', line=257)
W('27,2202', 0o77626, '', 'STADR', kind='interp', line=258)
W('27,2203', 0o50442, '', 'STOVL', 'MIS +12D', kind='interp', line=259)
W('27,2204', 0o77626, '', 'STADR', '', 'STORE MFS (IN PD LIST) IN MIS', kind='interp', line=260)
W('27,2205', 0o50450, '', 'STOVL', 'MIS +6', kind='interp', line=261)
W('27,2206', 0o77626, '', 'STADR', kind='interp', line=262)
W('27,2207', 0o50456, '', 'STOVL', 'MIS', kind='interp', line=263)
W('27,2210', 0o03327, '', '', 'MIS +6', 'INNER GIMBAL AXIS IN FINAL S/C AXES', kind='operand', line=264)
W('27,2211', 0o57444, '', 'BPL', 'VCOMP', 'LOCATE THE IG AXIS DIRECTION CLOSEST TO', kind='interp', line=265)
W('27,2212', 0o56213, '', '', 'IGSAMEX', 'FINAL X S/C AXIS', kind='operand', line=266)

W('27,2213', 0o50035, 'IGSAMEX', 'VXV', 'BMN', 'FIND THE SHORTEST WAY OF ROTATING THE', kind='interp', line=268)
W('27,2214', 0o03351, '', '', 'SCAXIS', 'S/C OUT OF GIMBAL LOCK BY A ROTATION', kind='operand', line=269)
W('27,2215', 0o56222, '', '', 'U=SCAXIS', 'ABOUT +- SCAXIS, I.E. IF (IG (SGN MFS3)', kind='operand', line=270)
# X SCAXIS . XF) LESS THAN 0, U = SCAXIS
# OTHERWISE U = -SCAXIS.

W('27,2216', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=274)
W('27,2217', 0o03351, '', '', 'SCAXIS', kind='operand', line=275)
W('27,2220', 0o37343, '', 'STCALL', 'COF', 'ROTATE ABOUT -SCAXIS', kind='interp', line=276)
W('27,2221', 0o56225, '', '', 'CHEKAXIS', kind='operand', line=277)
W('27,2222', 0o77775, 'U=SCAXIS', 'VLOAD', kind='interp', line=278)
W('27,2223', 0o03351, '', '', 'SCAXIS', kind='operand', line=279)
W('27,2224', 0o03343, '', 'STORE', 'COF', 'ROTATE ABOUT + SCAXIS', kind='interp', line=280)
W('27,2225', 0o51545, 'CHEKAXIS', 'DLOAD', 'ABS', kind='interp', line=281)
W('27,2226', 0o03351, '', '', 'SCAXIS', 'SEE IF WE ARE POINTING THE AOT', kind='operand', line=282)
W('27,2227', 0o51025, '', 'DSU', 'BPL', kind='interp', line=283)
W('27,2230', 0o16320, '', '', 'SINVEC2', 'SIN 29.5 DEGS                         $2', kind='operand', line=284)
W('27,2231', 0o56235, '', '', 'PICKANG1', 'IF SO, ROTATE 50 DEGS ABOUT +- SCAXIS', kind='operand', line=285)
W('27,2232', 0o52145, '', 'DLOAD', 'GOTO', 'IF NOT, MUST BE POINTING THE TRANSPONDER', kind='interp', line=286)
W('27,2233', 0o16324, '', '', 'VECANG2', 'OR SOME VECTOR IN THE Y, OR Z PLANE', kind='operand', line=287)
W('27,2234', 0o56237, '', '', 'COMPMFSN', 'IN THIS CASE ROTATE 35 DEGS TO GET OUT', kind='operand', line=288)
# OF GIMBAL LOCK (VECANG2 $360)
W('27,2235', 0o77745, 'PICKANG1', 'DLOAD', kind='interp', line=290)
W('27,2236', 0o16322, '', '', 'VECANG1', '= 50 DEGS                           $360', kind='operand', line=291)
W('27,2237', 0o77624, 'COMPMFSN', 'CALL', kind='interp', line=292)
W('27,2240', 0o44530, '', '', 'DELCOMP', 'COMPUTE THE ROTATION ABOUT SCAXIS TO', kind='operand', line=293)
W('27,2241', 0o75160, '', 'AXC,1', 'AXC,2', 'BRING MFS OUT OF GIMBAL LOCK', kind='interp', line=294)
W('27,2242', 0o03320, '', '', 'MIS', kind='operand', line=295)
W('27,2243', 0o03425, '', '', 'DEL', kind='operand', line=296)
W('27,2244', 0o77624, '', 'CALL', '', 'COMPUTE THE NEW TRANSFORMATION FROM', kind='interp', line=297)
W('27,2245', 0o44304, '', '', 'MXM3', 'DESIRED S/C AXES TO STABLE MEMBER AXES', kind='operand', line=298)
# WHICH WILL ALIGN VI WITH VF AND AVOID
# GIMBAL LOCK
W('27,2246', 0o45160, 'FINDGIMB', 'AXC,1', 'CALL', kind='interp', line=301)
W('27,2247', 0o00000, '', '', '0', 'EXTRACT THE COMMANDED CDU ANGLES FROM', kind='operand', line=302)
W('27,2250', 0o44655, '', '', 'DCMTOCDU', 'THIS MATRIX', kind='operand', line=303)
W('27,2251', 0o40234, '', 'RTB', 'SETPD', kind='interp', line=304)
W('27,2252', 0o45552, '', '', 'V1STO2S', 'CONVERT TO 2:S COMPLEMENT', kind='operand', line=305)
# Page 396
W('27,2253', 0o00001, '', '', '0', kind='operand', line=307)
W('27,2254', 0o77650, '', 'GOTO', kind='interp', line=308)
W('27,2255', 0o03310, '', '', 'VECQTEMP', 'RETURN TO CALLER', kind='operand', line=309)

W('27,2256', 0o50375, 'PICKAXIS', 'VLOAD', 'DOT', 'IF VF X VI = 0, FIND VF . VI', kind='interp', line=311)
W('27,2257', 0o00035, '', '', '28D', kind='operand', line=312)
W('27,2260', 0o03351, '', '', 'SCAXIS', kind='operand', line=313)
W('27,2261', 0o72240, '', 'BMN', 'TLOAD', kind='interp', line=314)
W('27,2262', 0o56266, '', '', 'ROT180', kind='operand', line=315)
W('27,2263', 0o00032, '', '', '25D', kind='operand', line=316)
W('27,2264', 0o77650, '', 'GOTO', '', 'IF VF = VI, CDU DESIRED = PRESENT CDU', kind='interp', line=317)
W('27,2265', 0o03310, '', '', 'VECQTEMP', 'PRESENT CDU ANGLES', kind='operand', line=318)

W('27,2266', 0o47375, 'ROT180', 'VLOAD', 'VXV', 'IF VF, VI ANTI-PARALLEL, 180 DEG ROTATION', kind='interp', line=320)
W('27,2267', 0o03327, '', '', 'MIS +6', 'IS REQUIRED.  Y STABLE MEMBER AXIS IN', kind='operand', line=321)
W('27,2270', 0o15333, '', '', 'HIUNITX', 'INITIAL S/C AXIS.', kind='operand', line=322)
W('27,2271', 0o47256, '', 'UNIT', 'VXV', 'FIND Y(SM) X X(I)', kind='interp', line=323)
W('27,2272', 0o03351, '', '', 'SCAXIS', 'FIND UNIT(VI X UNIT(Y(SM) X X(I)))', kind='operand', line=324)
W('27,2273', 0o40056, '', 'UNIT', 'BOV', 'I.E. PICK A VECTOR IN THE PLANE OF X(I),', kind='interp', line=325)
W('27,2274', 0o56310, '', '', 'PICKX', 'Y(SM) PERPENDICULAR TO VI', kind='operand', line=326)
W('27,2275', 0o17343, '', 'STODL', 'COF', kind='interp', line=327)
W('27,2276', 0o00045, '', '', '36D', 'CHECK MAGNITUDE', kind='operand', line=328)
W('27,2277', 0o50025, '', 'DSU', 'BMN', 'OF THIS VECTOR.', kind='interp', line=329)
W('27,2300', 0o16327, '', '', 'DPB-14', 'IF LESS THAN B-14,', kind='operand', line=330)
W('27,2301', 0o56310, '', '', 'PICKX', 'PICK X-AXIS.', kind='operand', line=331)
W('27,2302', 0o77775, '', 'VLOAD', kind='interp', line=332)
W('27,2303', 0o03343, '', '', 'COF', kind='operand', line=333)
W('27,2304', 0o17343, 'XROT', 'STODL', 'COF', kind='interp', line=334)
W('27,2305', 0o15333, '', '', 'HIDPHALF', kind='operand', line=335)
W('27,2306', 0o77650, '', 'GOTO', kind='interp', line=336)
W('27,2307', 0o56160, '', '', 'COMPMATX', kind='operand', line=337)
W('27,2310', 0o52175, 'PICKX', 'VLOAD', 'GOTO', 'PICK THE XAXIS IN THIS CASE', kind='interp', line=338)
W('27,2311', 0o15333, '', '', 'HIUNITX', kind='operand', line=339)
W('27,2312', 0o56304, '', '', 'XROT', kind='operand', line=340)
#   BANK 35
#   SETLOC MANUVER1
#   BANK

W('27,2313', 0o15555, 'SINGIMLC', '2DEC', '.4285836003', '=SIN(59)                      $2', kind='data', line=345)
W('27,2314', 0o35172, kind='data', line=345)

W('27,2315', 0o14113, 'SINVEC1', '2DEC', '.3796356537', '=SIN(49.4)                    $2', kind='data', line=347)
W('27,2316', 0o36326, kind='data', line=347)

W('27,2317', 0o07701, 'SINVEC2', '2DEC', '.2462117800', '=SIN(29.5)                    $2', kind='data', line=349)
W('27,2320', 0o35703, kind='data', line=349)

W('27,2321', 0o04343, 'VECANG1', '2DEC', '.1388888889', '= 50 DEGREES                        $360', kind='data', line=351)
W('27,2322', 0o21616, kind='data', line=351)

W('27,2323', 0o03070, 'VECANG2', '2DEC', '.09722222222', '= 35 DEGREES                        $360', kind='data', line=353)
W('27,2324', 0o34344, kind='data', line=353)

W('27,2325', 0o00000, '1BITDP', 'OCT', '0', 'KEEP THIS BEFORE DPB(-14)       *********', kind='data', line=356)
W('27,2326', 0o00001, 'DPB-14', 'OCT', '00001', kind='data', line=357)
# Page 397
W('27,2327', 0o00000, '', 'OCT', '00000', kind='data', line=359)
#   BANK 34
#   SETLOC MANUVER
#   BANK

# Page 398
# ROUTINE FOR INITIATING AUTOMATIC MANEUVER VIA KEYBOARD (V49)

#   EBANK= CPHI

#   COUNT 27/R62

W('27,2330', 0o35052, 'R62DISP', 'CAF', 'V06N22', 'DISPLAY COMMAND ICDUS CPHI, CTHETA, CPHI', line=371)
W('27,2331', 0o04662, '', 'TC', 'BANKCALL', line=372)
W('27,2332', 0o20720, '', 'CADR', 'GOFLASH', kind='data', line=373)
W('27,2333', 0o15534, '', 'TCF', 'ENDEXT', line=374)
W('27,2334', 0o12336, '', 'TCF', 'GOMOVE', 'PROCEED', line=375)
W('27,2335', 0o12330, '', 'TCF', 'R62DISP', 'ENTER', line=376)

# ASTRONAUT MAY LOAD NEW ICDUS AT THIS
# POINT
W('27,2336', 0o05546, 'GOMOVE', 'TC', 'UPFLAG', 'SET 3-AXIS FLAG', line=380)
W('27,2337', 0o00124, '', 'ADRES', '3AXISFLG', 'BIT 6 FLAG 5', kind='data', line=381)

W('27,2340', 0o04662, '', 'TC', 'BANKCALL', line=383)
W('27,2341', 0o56000, '', 'CADR', 'R60CSM', kind='data', line=384)
W('27,2342', 0o15534, '', 'TCF', 'ENDEXT', line=385)
