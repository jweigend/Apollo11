"""T6-RUPT_PROGRAMS.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/T6-RUPT_PROGRAMS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1403-1405 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('T6_RUPT_PROGRAMS', 'T6-RUPT_PROGRAMS.agc', 'Luminary099', pages='1403-1405')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     T6-RUPT_PROGRAMS.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1403-1405
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

# Page 1403
# PROGRAM NAMES:        (1) T6JOBCHK    MOD. NO. 5      OCTOBER 2, 1967
# (2) DOT6RUPT
# MODIFICATION BY:      LOWELL G. HULL (A.C.ELECTRONICS)
#
# THESE PROGRAMS ENABLE THE LM DAP TO CONTROL THE THRUST TIMES OF THE REACTION CONTROL SYSTEM JETS BY USING TIME6.
# SINCE THE LM DAP MAINTAINS EXCLUSIVE CONTROL OVER TIME6 AND ITS INTERRUPTS, THE FOLLOWING CONVENTIONS HAVE BEEN
# ESTABLISHED AND MUST NOT BE TAMPERED WITH:
# 1.      NO NUMBER IS EVER PLACED INTO TIME6 EXCEPT BY LM DAP.
# 2.      NO PROGRAM OTHER THAN LM DAP ENABLES THE TIME6 COUNTER.
# 3.      TO USE TIME6, THE FOLLOWING SEQUENCE IS ALWAYS EMPLOYED:
# A.      A POSITIVE (NON-ZERO) NUMBER IS STORED IN TIME6.
# B.      THE TIME6 CLOCK IS ENABLED.
# C.      TIME6 IS INTERROGATED AND IS:
# I.      NEVER FOUND NEGATIVE (NON-ZERO) OR +0.
# II.     SOMETIMES FOUND POSITIVE (BETWEEN 1 AND 240D) INDICATING THAT IT IS ACTIVE.
# III.    SOMETIMES FOUND POSMAX INDICATING THAT IT IS INACTIVE AND NOT ENABLED.
# IV.     SOMETIMES FOUND NEGATIVE ZERO INDICATING THAT:
# A.      A T6RUPT IS ABOUT TO OCCUR AT THE NEXT DINC, OR
# B.      A T6RUPT IS WAITING IN THE PRIORITY CHAIN, OR
# C.      A T6RUPT IS IN PROCESS NOW.
# 4.      ALL PROGRAMS WHICH OPERATE IN EITHER INTERRUPT MODE OR WITH INTERRUPT INHIBITED MUST CALL T6JOBCHK
# EVERY 5 MILLISECONDS TO PROCESS A POSSIBLE WAITING T6RUPT BEFORE IT CAN BE HONORED BY THE HARDWARE.
# (5.      PROGRAM JTLST, IN Q,R-AXES, HANDLES THE INPUT LIST.)
#
# T6JOBCHK CALLING SEQUENCE:
# L       TC      T6JOBCHK
# L+1     (RETURN)
#
# DOT6RUPT CALLING SEQUENCE:
# DXCH    ARUPT           # T6RUPT LEAD IN AT LOCATION 4004.
# EXTEND
# DCA     T6ADR
# DTCB
#
# SUBROUTINES CALLED:   DOT6RUPT CALLS T6JOBCHK.
#
# NORMAL EXIT MODES:    T6JOBCHK RETURNS TO L +1.
# DOT6RUPT TRANSFERS CONTROL TO RESUME.
#
# ALARM/ABORT MODES:    NONE.
#
# INPUT:        TIME6           NXT6ADR         OUTPUT:         TIME6           NXT6ADR         CHANNEL 5
# T6NEXT          T6NEXT +1                       T6NEXT          T6NEXT +1       CHANNEL 6
# T6FURTHA        T6FURTHA +1                     T6FURTHA        T6FURTHA +1     BIT15/CH13
#
# DEBRIS:       T6JOBCHK CLOBBERS A.  DOT6RUPT CLOBBERS NOTHING.

#   BLOCK 02
# Page 1404
#   BANK 17
#   SETLOC DAPS2
#   BANK
#   EBANK= T6NEXT
#   COUNT* $$/DAPT6

W('17,2027', 0o10031, 'T6JOBCHK', 'CCS', 'TIME6', 'CHECK TIME6 FOR WAITING T6RUPT:', line=85)
W('17,2030', 0o00002, '', 'TC', 'Q', 'NONE: CLOCK COUNTING DOWN.', line=86)
W('17,2031', 0o05705, '', 'TC', 'CCSHOLE', line=87)
W('17,2032', 0o02032, '', 'TC', 'T6JOBCHK +3', line=88)

# CONTROL PASSES TO T6JOB ONLY WHEN C(TIME6) = -0 (I.E., WHEN A T6RUPT MUST BE PROCESSED).

W('17,2033', 0o34733, 'T6JOB', 'CAF', 'POSMAX', 'DISABLE CLOCK: NEEDED SINCE RUPT OCCURS', line=92)
W('17,2034', 0o00006, '', 'EXTEND', '', '1 DINC AFTER T6 = 77777. FOR 625 MUSECS', line=93)
W('17,2035', 0o03013, '', 'WAND', 'CHAN13', 'MUST NOT HAVE T6 = +0 WITH ENABLE SET', line=94)

W('17,2036', 0o34733, '', 'CA', 'POSMAX', line=96)
W('17,2037', 0o22007, '', 'ZL', line=97)
W('17,2040', 0o53471, '', 'DXCH', 'T6FURTHA', line=98)
W('17,2041', 0o53467, '', 'DXCH', 'T6NEXT', line=99)
W('17,2042', 0o23465, '', 'LXCH', 'NXT6ADR', line=100)
W('17,2043', 0o54031, '', 'TS', 'TIME6', line=101)

W('17,2044', 0o67725, '', 'AD', 'PRIO37', line=103)
W('17,2045', 0o54000, '', 'TS', 'A', line=104)
W('17,2046', 0o12052, '', 'TCF', 'ENABLET6', line=105)
W('17,2047', 0o34733, '', 'CA', 'POSMAX', line=106)
W('17,2050', 0o54031, '', 'TS', 'TIME6', line=107)
W('17,2051', 0o12063, '', 'TCF', 'GOCH56', line=108)
W('17,2052', 0o34735, 'ENABLET6', 'CA', 'BIT15', line=109)
W('17,2053', 0o00006, '', 'EXTEND', line=110)
W('17,2054', 0o05013, '', 'WOR', 'CHAN13', line=111)
W('17,2055', 0o31466, '', 'CA', 'T6NEXT', line=112)
W('17,2056', 0o67725, '', 'AD', 'PRIO37', line=113)
W('17,2057', 0o54000, '', 'TS', 'A', line=114)
W('17,2060', 0o12063, '', 'TCF', 'GOCH56', line=115)
W('17,2061', 0o34733, '', 'CA', 'POSMAX', line=116)
W('17,2062', 0o55466, '', 'TS', 'T6NEXT', line=117)
W('17,2063', 0o50001, 'GOCH56', 'INDEX', 'L', line=118)
W('17,2064', 0o15753, '', 'TCF', 'WRITEP -1', line=119)

#   BLOCK 02
#   SETLOC FFTAG9
#   BANK
#   EBANK= CDUXD
#   COUNT* $$/DAPT6

W('5753', 0o31472, '', 'CA', 'NEXTP', line=127)
W('5754', 0o00006, 'WRITEP', 'EXTEND', line=128)
W('5755', 0o01006, '', 'WRITE', 'CHAN6', line=129)
# Page 1405
W('5756', 0o00002, '', 'TC', 'Q', line=131)

W('5757', 0o31473, '', 'CA', 'NEXTU', line=133)
W('5760', 0o54001, 'WRITEU', 'TS', 'L', line=134)
W('5761', 0o45774, '', 'CS', '00314OCT', line=135)
W('5762', 0o00006, '', 'EXTEND', line=136)
W('5763', 0o02005, '', 'RAND', 'CHAN5', line=137)
W('5764', 0o60001, '', 'AD', 'L', line=138)
W('5765', 0o00006, '', 'EXTEND', line=139)
W('5766', 0o01005, '', 'WRITE', 'CHAN5', line=140)
W('5767', 0o00002, '', 'TC', 'Q', line=141)

W('5770', 0o31474, '', 'CA', 'NEXTV', line=143)
W('5771', 0o54001, 'WRITEV', 'TS', 'L', line=144)
W('5772', 0o35774, '', 'CA', '00314OCT', line=145)
W('5773', 0o15762, '', 'TCF', '-9D', line=146)
W('5774', 0o00314, '00314OCT', 'OCT', '00314', kind='data', line=147)

#   BANK 17
#   SETLOC DAPS2
#   BANK

#   EBANK= T6NEXT
#   COUNT* $$/DAPT6

W('17,2065', 0o22016, 'DOT6RUPT', 'LXCH', 'BANKRUPT', '(INTERRUPT LEAD INS CONTINUED)', line=156)
W('17,2066', 0o00006, '', 'EXTEND', line=157)
W('17,2067', 0o22012, '', 'QXCH', 'QRUPT', line=158)

W('17,2070', 0o02027, '', 'TC', 'T6JOBCHK', 'CALL T6JOBCHK.', line=160)

W('17,2071', 0o15270, '', 'TCF', 'RESUME', 'END TIME6 INTERRUPT PROCESSOR.', line=162)
