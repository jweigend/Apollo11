"""DAP_INTERFACE_SUBROUTINES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/DAP_INTERFACE_SUBROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1406-1409 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('DAP_INTERFACE_SUBROUTINES', 'DAP_INTERFACE_SUBROUTINES.agc', 'Luminary099', pages='1406-1409')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     DAP_INTERFACE_SUBROUTINES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1406-1409
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Luminary131/ file of the same
# name, using Luminary099 page images.
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

# Page 1406
#   BANK 20
#   SETLOC DAPS3
#   BANK

#   EBANK= CDUXD
#   COUNT* $$/DAPIF

# MOD 0         DATE    11/15/66        BY GEORGE W. CHERRY
# MOD 1                  1/23/67        MODIFICATION BY PETER ADLER
#
# FUNCTIONAL DESCRIPTION
# HEREIN ARE A COLLECTION OF SUBROUTINES WHICH ALLOW MISSION CONTROL PROGRAMS TO CONTROL THE MODE
# AND INTERFACE WITH THE DAP.
#
# CALLING SEQUENCES
# IN INTERRUPT OR WITH INTERRUPT INHIBITED
# TC      IBNKCALL
# FCADR   ROUTINE
# IN A JOB WITHOUT INTERRUPT INHIBITED
# INHINT
# TC      IBNKCALL
# FCADR   ROUTINE
# RELINT
#
# OUTPUT
# SEE INDIVIDUAL ROUTINES BELOW
#
# DEBRIS
# A, L, AND SOMETIMES MDUETEMP                    ODE     NOT IN PULSES MODE

# Page 1407
# SUBROUTINE NAMES:
# SETMAXDB, SETMINDB, RESTORDB, PFLITEDB
# MODIFIED:     30 JANUARY 1968 BY P S WEISSMAN TO CREATE RESTORDB.
# MODIFIED:     1 MARCH 1968 BY P S WEISSMAN TO SAVE EBANK AND CREATE PFLITEDB
#
# FUNCTIONAL DESCRIPTION:
# SETMAXDB -- SET DEADBAND TO 5.0 DEGREES
# SETMINDB -- SET DEADBAND TO 0.3 DEGREE
# RESTORDB -- SET DEADBAND TO MAX OR MIN ACCORDING TO SETTINGS OF DBSELECT BIT OF DAPBOOLS
# PFLITEDB -- SET DEADBAND TO 1.0 DEGREE AND ZERO THE COMMANDED ATTITUDE CHANGE AND COMMANDED RATE
#
# ALL ENTRIES SET UP A NOVAC JOB TO DO 1/ACCS SO THAT THE TJETLAW SWITCH CURVES ARE POSITIONED TO
# REFLECT THE NEW DEADBAND.  IT SHOULD BE NOTED THAT THE DEADBAND REFERS TO THE ATTITUDE IN THE P-, U-, AND V-AXES.
#
# SUBROUTINE CALLED:    NOVAC
#
# CALLING SEQUENCE:     SAME AS ABOVE
# OR      TC RESTORDB +1    FROM ALLCOAST
#
# DEBRIS:               A, L, Q, RUPTREG1, (ITEMPS IN NOVAC)

W('20,2123', 0o30111, 'RESTORDB', 'CAE', 'DAPBOOLS', 'DETERMINE CREW-SELECTED DEADBAND.', line=82)
W('20,2124', 0o74750, '', 'MASK', 'DBSELECT', line=83)
W('20,2125', 0o00006, '', 'EXTEND', line=84)
W('20,2126', 0o12140, '', 'BZF', 'SETMINDB', line=85)

W('20,2127', 0o32151, 'SETMAXDB', 'CAF', 'WIDEDB', 'SET 5 DEGREE DEADBAND.', line=87)
W('20,2130', 0o55346, '', 'TS', 'DB', line=88)

W('20,2131', 0o00006, '', 'EXTEND', '', 'SET UP JOB TO RE-POSITION SWITCH CURVES.', line=90)
W('20,2132', 0o22070, '', 'QXCH', 'RUPTREG1', line=91)
W('20,2133', 0o37715, 'CALLACCS', 'CAF', 'PRIO27', line=92)
W('20,2134', 0o05072, '', 'TC', 'NOVAC', line=93)
#   EBANK= AOSQ
W('20,2135', 0o02454, '', '2CADR', '1/ACCJOB', kind='data', line=95)
W('20,2136', 0o40106, kind='data', line=95)

W('20,2137', 0o00070, '', 'TC', 'RUPTREG1', 'RETURN TO CALLER.', line=97)

W('20,2140', 0o32150, 'SETMINDB', 'CAF', 'NARROWDB', 'SET 0.3 DEGREE DEADBAND.', line=99)
W('20,2141', 0o12130, '', 'TCF', 'SETMAXDB +1', line=100)

W('20,2142', 0o00006, 'PFLITEDB', 'EXTEND', '', 'THE RETURN FROM CALLACCS IS TO RUPTREG1.', line=102)
W('20,2143', 0o22070, '', 'QXCH', 'RUPTREG1', line=103)
W('20,2144', 0o02153, '', 'TC', 'ZATTEROR', 'ZERO THE ERRORS AND COMMANDED RATES.', line=104)
W('20,2145', 0o32152, '', 'CAF', 'POWERDB', 'SET DB TO 1.0 DEG.', line=105)
W('20,2146', 0o55346, '', 'TS', 'DB', line=106)
W('20,2147', 0o12133, '', 'TCF', 'CALLACCS', 'SET UP 1/ACCS AND RETURN TO CALLER.', line=107)
W('20,2150', 0o00155, 'NARROWDB', 'OCTAL', '00155', '0.3 DEGREE SCALED AT 45.', kind='data', line=108)
# Page 1408
W('20,2151', 0o03434, 'WIDEDB', 'OCTAL', '03434', '5.0 DEGREES SCALED AT 45.', kind='data', line=110)
W('20,2152', 0o00554, 'POWERDB', 'DEC', '.02222', '1.0 DEGREE SCALED AT 45.', kind='data', line=111)

W('20,2153', 0o35015, 'ZATTEROR', 'CAF', 'EBANK6', line=113)
W('20,2154', 0o56003, '', 'XCH', 'EBANK', line=114)
W('20,2155', 0o54001, '', 'TS', 'L', 'SAVE CALLERS EBANK IN L.', line=115)
W('20,2156', 0o30032, '', 'CAE', 'CDUX', line=116)
W('20,2157', 0o55635, '', 'TS', 'CDUXD', line=117)
W('20,2160', 0o30033, '', 'CAE', 'CDUY', line=118)
W('20,2161', 0o55636, '', 'TS', 'CDUYD', line=119)
W('20,2162', 0o30034, '', 'CAE', 'CDUZ', line=120)
W('20,2163', 0o55637, '', 'TS', 'CDUZD', line=121)
W('20,2164', 0o12170, '', 'TCF', 'STOPRATE +3', line=122)

W('20,2165', 0o35015, 'STOPRATE', 'CAF', 'EBANK6', line=124)
W('20,2166', 0o56003, '', 'XCH', 'EBANK', line=125)
W('20,2167', 0o54001, '', 'TS', 'L', 'SAVE CALLERS EBANK IN L.', line=126)
W('20,2170', 0o34755, '', 'CAF', 'ZERO', line=127)
W('20,2171', 0o55643, '', 'TS', 'OMEGAPD', line=128)
W('20,2172', 0o55644, '', 'TS', 'OMEGAQD', line=129)
W('20,2173', 0o55645, '', 'TS', 'OMEGARD', line=130)
W('20,2174', 0o55640, '', 'TS', 'DELCDUX', line=131)
W('20,2175', 0o55641, '', 'TS', 'DELCDUY', line=132)
W('20,2176', 0o55642, '', 'TS', 'DELCDUZ', line=133)
W('20,2177', 0o55277, '', 'TS', 'DELPEROR', line=134)
W('20,2200', 0o55300, '', 'TS', 'DELQEROR', line=135)
W('20,2201', 0o55301, '', 'TS', 'DELREROR', line=136)
W('20,2202', 0o22003, '', 'LXCH', 'EBANK', 'RESTORE CALLERS EBANK.', line=137)
W('20,2203', 0o00002, '', 'TC', 'Q', line=138)

# SUBROUTINE NAME:      ALLCOAST
# WILL BE CALLED BY FRESH STARTS AND ENGINE OFF ROUTINES.
#
# CALLING SEQUENCE:     (SAME AS ABOVE)
#
# EXIT:                 RETURN TO Q.
#
# SUBROUTINES CALLED:   STOPRATE, RESTORDB, NOVAC
#
# ZERO:                 (FOR ALL AXES) AOS, ALPHA, AOSTERM, OMEGAD, DELCDU, DELEROR
#
# OUTPUT:               DRIFTBIT/DAPBOOLS, OE, JOB TO DO 1/ACCS
#
# DEBRIS:               A, L, Q, RUPTREG1, RUPTREG2, (ITEMPS IN NOVAC)

W('20,2204', 0o00006, 'ALLCOAST', 'EXTEND', '', 'SAVE Q FOR RETURN', line=155)
W('20,2205', 0o22071, '', 'QXCH', 'RUPTREG2', line=156)
# Page 1409
W('20,2206', 0o02165, '', 'TC', 'STOPRATE', 'CLEAR RATE INTERFACE.  RETURN WITH A=0', line=158)
W('20,2207', 0o22003, '', 'LXCH', 'EBANK', "  AND L=EBANK6.  SAVE CALLER'S EBANK.", line=159)
W('20,2210', 0o55537, '', 'TS', 'AOSQ', line=160)
W('20,2211', 0o55540, '', 'TS', 'AOSQ +1', line=161)
W('20,2212', 0o55541, '', 'TS', 'AOSR', line=162)
W('20,2213', 0o55542, '', 'TS', 'AOSR +1', line=163)
W('20,2214', 0o55424, '', 'TS', 'ALPHAQ', 'FOR DOWNLIST.', line=164)
W('20,2215', 0o55425, '', 'TS', 'ALPHAR', line=165)
W('20,2216', 0o55545, '', 'TS', 'AOSQTERM', line=166)
W('20,2217', 0o55546, '', 'TS', 'AOSRTERM', line=167)
W('20,2220', 0o22003, '', 'LXCH', 'EBANK', 'RESTORE EBANK (EBANK6 NO LONGER NEEDED)', line=168)

W('20,2221', 0o40111, '', 'CS', 'DAPBOOLS', 'SET UP DRIFTBIT', line=170)
W('20,2222', 0o74744, '', 'MASK', 'DRIFTBIT', line=171)
W('20,2223', 0o26111, '', 'ADS', 'DAPBOOLS', line=172)
W('20,2224', 0o02124, '', 'TC', 'RESTORDB +1', 'RESTORE DEADBANK TO CREW-SELECTED VALUE.', line=173)

W('20,2225', 0o00071, '', 'TC', 'RUPTREG2', 'RETURN.', line=175)
