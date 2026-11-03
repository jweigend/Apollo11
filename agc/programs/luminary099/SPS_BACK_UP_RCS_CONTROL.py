"""SPS_BACK-UP_RCS_CONTROL.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/SPS_BACK-UP_RCS_CONTROL.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1507-1510 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('SPS_BACK_UP_RCS_CONTROL', 'SPS_BACK-UP_RCS_CONTROL.agc', 'Luminary099', pages='1507-1510')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     SPS_BACK-UP_RCS_CONTROL.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1507-1510
# Mod history:  2009-05-27 RSB  Adapted from the corresponding
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

# Page 1507
# PROGRAM NAME:         SPSRCS
# AUTHOR:               EDGAR M. OSHIKA (AC ELECTRONICS)
# MODIFIED:             TO RETURN TO ALL AXES VIA Q BY P. S. WEISSMAN, OCT 7, 1968
# MODIFIED TO IMPROVE BENDING STABILITY BY G. KALAN, FEB. 14, 1969
#
# FUNCTIONAL DESCRIPTION:
# THE PROGRAM CONTROLS THE FIRING OF ALL RCS JETS IN THE DOCKED CONFIGURATION ACCORDING TO THE FOLLOWING PHASE
# PLANE LOGIC.
#
# 1. JET SENSE TEST (SPSRCS)
# IF JETS ARE FIRING NEGATIVELY, SET OLDSENSE NEGATIVE AND CONTINUE
# IF JETS ARE FIRING POSITIVELY, SET OLDSENSE POSITIVE AND CONTINUE
# IF JETS ARE NOT FIRING, SET OLDSENSE TO ZERO AND GO TO OUTER RATE LIMIT TEST
#
# 2. RATE DEAD BAND TEST
# IF JETS ARE FIRING NEGATIVELY AND RATE IS GREATER THAN TARGET RATE, LEAVE
# JETS ON AND GO TO INHIBITION LOGIC.  OTHERWISE, CONTINUE.
# IF JETS ARE FIRING POSITIVELY AND RATE IS   LESS  THAN TARGET RATE, LEAVE
# JETS ON AND GO TO INHIBITION LOGIC.  OTHERWISE, CONTINUE.
#
# 3. OUTER RATE LIMIT TEST (SPSSTART)
# IF MAGNITUDE OF EDOT IS GREATER THAN 1.73 DEG/SEC SET JET FIRING TIME
# TO REDUCE RATE AND GO TO INHIBITION LOGIC.  OTHERWISE, CONTINUE.
#
# 4. COAST ZONE TEST
# IF STATE (E,EDOT) IS BELOW LINE E + 4 X EDOT > -1.4 DEG AND EDOT IS LESS THAN 1.30 DEG/SEC SET JET TIME
# POSITIVE AND CONTINUE.  OTHERWISE, SET JET FIRING TIME TO ZERO AND CONTINUE.
# IF STATE IS ABOVE LINE E + 4 X EDOT > +1.4 DEG AND EDOT IS GREATER THAN -1.30 DEG/SEC, SET JET TIME NEGATIVE
# AND CONTINUE.  OTHERWISE, SET JET FIRING TIME TO ZERO AND CONTINUE.
#
# 5. INHIBITION LOGIC
# IF OLDSENSE IS NON-ZERO:
# A) RETURN IF JET TIME AS THE SAME SIGN AS OLDSENSE
# B) SET INHIBITION COUNTER* AND RETURN IF JET TIME IS ZERO
# C) SET INHIBITION COUNTER,* SET JET TIME TO ZERO AND RETURN IF SIGN
# OF JET TIME IS OPPOSITE TO THAT OF OLDSENSE
# IF OLDSENSE IS ZERO:
# A) RETURN IF INHIBITION COUNTER IS NOT POSITIVE
# B) SET JET TIME TO ZERO AND RETURN IF INHIBITION COUNTER IS POSITIVE
# *NOTE: INHIBITION COUNTERS CAN BE SET TO 4 OR 10 FOR THE P AND UV AXES,
# RESPECTIVELY, IN SPSRCS.  THEY ARE DECREMENTED BY ONE AT THE BEGINNING OF
# Page 1508
# EACH DAP PASS.
#
# THE MINIMUM PULSE WIDTH OF THIS CONTROLLER IS DETERMINED BY THE REPETITION RATE AT WHICH THIS ROUTINE IS CALLED
# AND IS NOMINALLY 100 MS FOR ALL AXES IN DRIFTING FLIGHT.  DURING POWERED FLIGHT THE MINIMUM IS 100 MS FOR THE
# P AXIS AND 200 MS FOR THE CONTROL OF THE U AND V AXES.
#
# CALLING SEQUENCE:
# INHINT
# TC      IBNKCALL
# CADR    SPSRCE
#
# EXIT:
# TC      Q
#
# ALARM/ABORT MODE:     NONE
#
# SUBROUTINES CALLED:   NONE
#
# INPUT:                E, EDOT
# TJP, TJV, TJU           TJ MUST NOT BE NEGATIVE ZERO
#
# OUTPUT:               TJP, TJV, TJU

#   BANK 21
#   SETLOC DAPS4
#   BANK

#   COUNT* $$/DAPBU

#   EBANK= TJU
W('21,3646', 0o00632, 'RATELIM2', 'OCT', '00632', '1.125 DEG/SEC', kind='data', line=102)
W('21,3647', 0o34736, 'POSTHRST', 'CA', 'HALF', line=103)

W('21,3650', 0o51505, '', 'NDX', 'AXISCTR', line=105)
W('21,3651', 0o55525, '', 'TS', 'TJU', line=106)
W('21,3652', 0o11745, '', 'CCS', 'OLDSENSE', line=107)
W('21,3653', 0o13673, '', 'TCF', 'POSCHECK', 'JETS FIRING POSITIVELY', line=108)
W('21,3654', 0o13676, '', 'TCF', 'CTRCHECK', 'JETS OFF.  CHECK INHIBITION CTR', line=109)
W('21,3655', 0o51505, 'NEGCHECK', 'INDEX', 'AXISCTR', 'JETS FIRING NEGATIVELY', line=110)
W('21,3656', 0o41525, '', 'CS', 'TJU', line=111)
W('21,3657', 0o10000, '', 'CCS', 'A', line=112)
W('21,3660', 0o00002, '', 'TC', 'Q', 'RETURN', line=113)
W('21,3661', 0o13663, '', 'TCF', '+2', line=114)
W('21,3662', 0o13663, '', 'TCF', '+1', 'JETS COMMANDED OFF.  SET CTR AND RETURN', line=115)
W('21,3663', 0o51505, 'SETCTR', 'INDEX', 'AXISCTR', 'JET FIRING REVERSAL COMMANDED.  SET CTR,', line=116)
W('21,3664', 0o33705, '', 'CA', 'UTIME', 'SET JET TIME TO ZERO, AND RETURN', line=117)
# Page 1509
W('21,3665', 0o51505, '', 'INDEX', 'AXISCTR', line=119)
W('21,3666', 0o55770, '', 'TS', 'UJETCTR', line=120)
W('21,3667', 0o34755, 'ZAPTJ', 'CA', 'ZERO', line=121)
W('21,3670', 0o51505, '', 'INDEX', 'AXISCTR', line=122)
W('21,3671', 0o55525, '', 'TS', 'TJU', line=123)
W('21,3672', 0o00002, '', 'TC', 'Q', line=124)
W('21,3673', 0o51505, 'POSCHECK', 'INDEX', 'AXISCTR', line=125)
W('21,3674', 0o31525, '', 'CA', 'TJU', line=126)
W('21,3675', 0o13657, '', 'TCF', 'NEGCHECK +2', line=127)
W('21,3676', 0o51505, 'CTRCHECK', 'INDEX', 'AXISCTR', 'CHECK JET INHIBITION COUNTER', line=128)
W('21,3677', 0o11770, '', 'CCS', 'UJETCTR', line=129)
W('21,3700', 0o13702, '', 'TCF', '+2', line=130)
W('21,3701', 0o00002, '', 'TC', 'Q', 'CTR IS NOT POSITIVE.  RETURN', line=131)
W('21,3702', 0o13667, '', 'TCF', 'ZAPTJ', 'CTR IS POSITIVE.  INHIBIT FIRINGS', line=132)
W('21,3703', 0o00002, '', 'TC', 'Q', 'CTR IS NOT POSITIVE.  RETURN', line=133)
W('21,3704', 0o00004, '', 'OCT', '00004', kind='data', line=134)
W('21,3705', 0o00012, 'UTIME', 'OCT', '00012', kind='data', line=135)
W('21,3706', 0o00012, '', 'OCT', '00012', kind='data', line=136)
S('OLDSENSE', 'equals', 0o3345, line=137)
W('21,3707', 0o44753, 'NEGFIRE', 'CS', 'ONE', 'JETS FIRING NEGATIVELY', line=138)
W('21,3710', 0o55745, '', 'TS', 'OLDSENSE', line=139)
W('21,3711', 0o31427, '', 'CA', 'EDOT', line=140)
W('21,3712', 0o13716, '', 'TCF', '+4', line=141)
W('21,3713', 0o34753, 'PLUSFIRE', 'CA', 'ONE', line=142)
W('21,3714', 0o55745, '', 'TS', 'OLDSENSE', line=143)
W('21,3715', 0o41427, '', 'CS', 'EDOT', 'RATE DEAD BAND TEST', line=144)
W('21,3716', 0o22000, '', 'LXCH', 'A', line=145)
W('21,3717', 0o40111, '', 'CS', 'DAPBOOLS', 'IF DRIFTBIT = 1, USE ZERO TARGET RATE', line=146)
W('21,3720', 0o74744, '', 'MASK', 'DRIFTBIT', 'IF DRIFTBIT = 0, USE 0.10 RATE TARGET', line=147)
W('21,3721', 0o10000, '', 'CCS', 'A', line=148)
W('21,3722', 0o34767, '', 'CA', 'RATEDB1', line=149)
W('21,3723', 0o60001, '', 'AD', 'L', line=150)
W('21,3724', 0o00006, '', 'EXTEND', line=151)
W('21,3725', 0o63735, '', 'BZMF', 'SPSSTART', line=152)
W('21,3726', 0o13652, '', 'TCF', 'POSTHRST +3', line=153)

W('21,3727', 0o51505, 'SPSRCS', 'INDEX', 'AXISCTR', 'JET SENSE TEST', line=155)
W('21,3730', 0o11525, '', 'CCS', 'TJU', line=156)
W('21,3731', 0o13713, '', 'TCF', 'PLUSFIRE', 'JETS FIRING POSITIVELY', line=157)
W('21,3732', 0o13734, '', 'TCF', '+2', line=158)
W('21,3733', 0o13707, '', 'TCF', 'NEGFIRE', 'JETS FIRING NEGATIVELY', line=159)
W('21,3734', 0o55745, '', 'TS', 'OLDSENSE', 'JETS OFF', line=160)
W('21,3735', 0o31427, 'SPSSTART', 'CA', 'EDOT', 'OUTER RATE LIMIT TEST', line=161)
W('21,3736', 0o00006, '', 'EXTEND', line=162)
W('21,3737', 0o74766, '', 'MP', 'RATELIM1', line=163)
W('21,3740', 0o10000, '', 'CCS', 'A', line=164)
W('21,3741', 0o13760, '', 'TCF', 'NEGTHRST', 'OUTER RATE LIMIT EXCEEDED', line=165)
W('21,3742', 0o13744, '', 'TCF', '+2', line=166)
W('21,3743', 0o13647, '', 'TCF', 'POSTHRST', 'OUTER RATE LIMIT EXCEEDED', line=167)
W('21,3744', 0o31427, '', 'CA', 'EDOT', 'COAST ZONE TEST', line=168)
# Page 1510
W('21,3745', 0o61752, '', 'AD', 'E', line=170)
W('21,3746', 0o00006, '', 'EXTEND', line=171)
W('21,3747', 0o71411, '', 'MP', 'DKDB', 'PAD LOADED DEADBAND.  FRESHSTART: 1.4 DEG', line=172)
W('21,3750', 0o00006, '', 'EXTEND', line=173)
W('21,3751', 0o13766, '', 'BZF', 'TJZERO', line=174)

W('21,3752', 0o00006, '', 'EXTEND', line=176)
W('21,3753', 0o63762, '', 'BZMF', '+7', line=177)
W('21,3754', 0o31427, '', 'CA', 'EDOT', line=178)
W('21,3755', 0o63646, '', 'AD', 'RATELIM2', line=179)
W('21,3756', 0o00006, '', 'EXTEND', line=180)
W('21,3757', 0o63766, '', 'BZMF', 'TJZERO', line=181)
W('21,3760', 0o44736, 'NEGTHRST', 'CS', 'HALF', line=182)
W('21,3761', 0o13650, '', 'TCF', 'POSTHRST +1', line=183)
W('21,3762', 0o43646, '', 'CS', 'RATELIM2', line=184)
W('21,3763', 0o61427, '', 'AD', 'EDOT', line=185)
W('21,3764', 0o00006, '', 'EXTEND', line=186)
W('21,3765', 0o63647, '', 'BZMF', 'POSTHRST', line=187)
W('21,3766', 0o34755, 'TJZERO', 'CA', 'ZERO', line=188)
W('21,3767', 0o13650, '', 'TCF', 'POSTHRST +1', line=189)

S('RATELIM1', 'equals', 0o4766, line=191)  # = 00032, CORRESPONDING TO 1.73 DEG/SEC
S('RATEDB1', 'equals', 0o4767, line=192)  # = 00045, CORRESPONDS TO 0.101 DEG/SEC

# *** END OF LMDAP  .015 ***
