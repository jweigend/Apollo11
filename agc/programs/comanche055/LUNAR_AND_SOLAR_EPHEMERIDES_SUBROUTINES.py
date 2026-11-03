"""LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 785-788 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES', 'LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES.agc', 'Comanche055', pages='785-788')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 785-788
# Contact:      Ron Burkey <info@sandroid.org>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-12 RSB  Adapted from Colossus249 file of the same
# name and Comanche 055 page images.
# 2009-07-26 RSB  Added annotations related to computation
# of the ephemeral(?) polynomials.
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

# Page 785
# LUNAR AND SOLAR EPHEMERIDES SUBROUTINES
#
# FUNCTIONAL DESCRIPTION
#
# THESE SUBROUTINES ARE USED TO DETERMINE THE POSITION AND VELOCITY
# VECTORS OF THE SUN AND THE MOON RELATIVE TO THE EARTH AT THE
# SPECIFIED GROUND ELAPSED TIME INPUT BY THE USER.
#
# THE POSITION OF THE MOON IS STORED IN THE COMPUTER IN THE FORM OF
# A NINTH DEGREE POLYNOMIAL APPROXIMATION WHICH IS VALID OVER A 15
# DAY INTERVAL BEGINNING SHORTLY BEFORE LAUNCH.  THEREFORE THE TIME
# INPUT BY THE USER SHOULD FALL WITHIN THIS 15 DAY INTERVAL.
#
# LSPOS COMPUTES THE POSITION VECTORS OF THE SUN AND THE MOON.
#
# LUNPOS COMPUTES THE POSITION VECTOR OF THE MOON.
#
# LUNVEL COMPUTES THE VELOCITY VECTOR OF THE MOON.
#
# SOLPOS COMPUTES THE POSITION VECTOR OF THE SUN.
#
# CALLING SEQUENCE
#
# DLOAD   CALL
# TIME            GROUND ELAPSED TIME
# SUBROUTINE      LSPOS OR LUNPOS OR LUNVEL OR SOLPOS
#
# INPUT
#
# 1) SPECIFIED GROUND ELAPSED TIME IN CS x B-28 LOADED IN MPAC.
#
# 2) TIMEMO - TIME AT THE CENTER OF THE RANGE OVER WHICH THE LUNAR
# POSITION POLYNOMIAL IS VALID IN CS x B-42.
#
# 3) VECOEM - VECTOR COEFFICIENTS OF THE LUNAR POSITION POLYNOMIAL
# LOADED IN DESCENDING SEQUENCE IN METERS/CS**N x B-2
#
# 4) RESO - POSITION VECTOR OF THE SUN RELATIVE TO THE EARTH AT
# TIMEMO IN METERS x B-38.
#
# 5) VESO - VELOCITY VECTOR OF THE SUN RELATIVE TO THE EARTH AT
# TIMEMO IN METERS/CS x B-9.
#
# 6) OMEGAES - ANGULAR VELOCITY OF THE VECTOR RESO AT TIMEMO IN
# REV/CS x B+26.
#
# ALL EXCEPT THE FIRST INPUT ARE INCLUDED IN THE PRE-LAUNCH
# ERASABLE DATA LOAD.
#
# OUTPUT - LSPOS
# Page 786
# 1) 2D OF VAC AREA CONTAINS THE POSITION VECTOR OF THE SUN RELATIVE
# TO THE EARTH AT TIME INPUT BY THE USER IN METERS x B-38.
#
# 2) MPAC CONTAINS THE POSITION VECTOR OF THE MOON RELATIVE TO THE
# EARTH AT TIME INPUT BY THE USER IN METERS x B-29.
#
# OUTPUT - LUNPOS
#
# MPAC CONTAINS THE POSITION VECTOR OF THE MOON RELATIVE TO THE
# EARTH AT THE TIME INPUT BY USER IN METERS x B-29.
#
# OUTPUT - LUNVEL
#
# MPAC CONTAINS THE VELOCITY VECTOR OF THE MOON RELATIVE TO THE
# EARTH AT THE TIME INPUT BY THE USER IN METERS/CS x B-7.
#
# OUTPUT - SOLPOS
#
# MPAC CONTAINS THE POSITION VECTOR OF THE SUN RELATIVE TO THE EARTH
# AT TIME INPUT BY THE USER IN METERS x B-38.
#
# SUBROUTINES USED
#
# NONE
#
# REMARKS
#
# THE VAC AREA IS USED FOR STORAGE OF INTERMEDIATE AND FINAL RESULTS
# OF COMPUTATIONS.
#
# S1, X1 AND X2 ARE USED BY THESE SUBROUTINES.
# PRELAUNCH ERASABLE DATA LOAD ARE ONLY ERASABLE STORAGE USED BY
# THESE SUBROUTINES.
# RESTARTS DURING OPERATION OF THESE SUBROUTINES MUST BE HANDLED BY
# THE USER.

#   BANK 36
#   SETLOC EPHEM
#   BANK

#   COUNT* $$/EPHEM
#   EBANK= END-E7
W('26,2110', 0o77774, 'LSPOS', 'AXT,2', '', 'COMPUTES POSITION VECTORS OF BOTH THE', kind='interp', line=127)
W('26,2111', 0o54161, '', '', 'RESA', 'SUN AND THE MOON.  THE POSITION VECTOR', kind='operand', line=128)
W('26,2112', 0o52170, '', 'AXT,1', 'GOTO', 'OF THE SUN IS STORED IN 2D OF THE VAC', kind='interp', line=129)
W('26,2113', 0o54143, '', '', 'RES', 'AREA.  THE POSITION VECTOR OF THE MOON', kind='operand', line=130)
W('26,2114', 0o54126, '', '', 'LSTIME', 'IS STORED IN MPAC.', kind='operand', line=131)
W('26,2115', 0o52170, 'LUNPOS', 'AXT,1', 'GOTO', 'COMPUTES THE POSITION VECTOR OF THE MOON', kind='interp', line=132)
W('26,2116', 0o54162, '', '', 'REM', 'AND STORES IT IN MPAC.', kind='operand', line=133)
W('26,2117', 0o54126, '', '', 'LSTIME', kind='operand', line=134)
# Page 787
W('26,2120', 0o52170, 'LUNVEL', 'AXT,1', 'GOTO', 'COMPUTES THE VELOCITY VECTOR OF THE MOON', kind='interp', line=136)
W('26,2121', 0o54173, '', '', 'VEM', 'AND STORES IT IN MPAC.', kind='operand', line=137)
W('26,2122', 0o54126, '', '', 'LSTIME', kind='operand', line=138)
W('26,2123', 0o76020, 'SOLPOS', 'STQ', 'AXT,1', 'COMPUTES THE POSITION VECTOR OF THE SUN', kind='interp', line=139)
W('26,2124', 0o00047, '', '', 'X2', 'AND STORES IT IN MPAC.', kind='operand', line=140)
W('26,2125', 0o54143, '', '', 'RES', kind='operand', line=141)
W('26,2126', 0o54201, 'LSTIME', 'SETPD', 'SR', kind='interp', line=142)
W('26,2127', 0o00001, '', '', '0D', kind='operand', line=143)
W('26,2130', 0o20617, '', '', '14D', kind='operand', line=144)
W('26,2131', 0o57571, '', 'TAD', 'DCOMP', kind='interp', line=145)
W('26,2132', 0o01707, '', '', 'TEPHEM', kind='operand', line=146)
W('26,2133', 0o57571, '', 'TAD', 'DCOMP', kind='interp', line=147)
W('26,2134', 0o02034, '', '', 'TIMEMO', kind='operand', line=148)
W('26,2135', 0o66261, '', 'SL', 'SSP', kind='interp', line=149)
W('26,2136', 0o20221, '', '', '16D', kind='operand', line=150)
W('26,2137', 0o00051, '', '', 'S1', kind='operand', line=151)
W('26,2140', 0o00006, '', '', '6D', kind='operand', line=152)
W('26,2141', 0o77650, '', 'GOTO', kind='interp', line=153)
W('26,2142', 0o00046, '', '', 'X1', kind='operand', line=154)
W('26,2143', 0o41206, 'RES', 'PUSH', 'DMP', '                                      PD- 2', kind='interp', line=155)
W('26,2144', 0o02147, '', '', 'OMEGAES', kind='operand', line=156)
W('26,2145', 0o71406, '', 'PUSH', 'COS', '                                      PD- 4', kind='interp', line=157)
W('26,2146', 0o65361, '', 'VXSC', 'PDDL', '                                      PD- 8', kind='interp', line=158)
W('26,2147', 0o02133, '', '', 'RESO', kind='operand', line=159)
W('26,2150', 0o63356, '', 'SIN', 'PDVL', '                                      PD-10', kind='interp', line=160)
W('26,2151', 0o02133, '', '', 'RESO', kind='operand', line=161)
W('26,2152', 0o53406, '', 'PUSH', 'UNIT', '                                      PD-16', kind='interp', line=162)
W('26,2153', 0o53435, '', 'VXV', 'UNIT', kind='interp', line=163)
W('26,2154', 0o02141, '', '', 'VESO', kind='operand', line=164)
W('26,2155', 0o76435, '', 'VXV', 'VSL1', '                                      PD-10', kind='interp', line=165)
W('26,2156', 0o53361, '', 'VXSC', 'VAD', '                                      PD-02', kind='interp', line=166)
W('26,2157', 0o52172, '', 'VSL1', 'GOTO', 'RES IN METERS x B-38 IN MPAC.', kind='interp', line=167)
W('26,2160', 0o00047, '', '', 'X2', kind='operand', line=168)
W('26,2161', 0o14003, 'RESA', 'STODL', '2D', 'RES IN METERS x B-38 IN 2D OF VAC.    PD- 0', kind='interp', line=169)
W('26,2162', 0o63370, 'REM', 'AXT,1', 'PDVL', '                                      PD- 2', kind='interp', line=170)
W('26,2163', 0o00066, '', '', '54D', kind='operand', line=171)
W('26,2164', 0o02037, '', '', 'VECOEM', kind='operand', line=172)
W('26,2165', 0o52761, 'REMA', 'VXSC', 'VAD*', kind='interp', line=173)
W('26,2166', 0o00001, '', '', '0D', kind='operand', line=174)
W('26,2167', 0o02133, '', '', 'VECOEM +60D,1', kind='operand', line=175)
W('26,2170', 0o72500, '', 'TIX,1', 'VSL2', 'REM IN METERS x B-29 IN MPAC.', kind='interp', line=176)
W('26,2171', 0o54165, '', '', 'REMA', kind='operand', line=177)
W('26,2172', 0o77616, '', 'RVQ', kind='interp', line=178)
W('26,2173', 0o65370, 'VEM', 'AXT,1', 'PDDL', '                                      PD- 2', kind='interp', line=179)
W('26,2174', 0o00060, '', '', '48D', kind='operand', line=180)
W('26,2175', 0o14214, '', '', 'NINEB4', kind='operand', line=181)
W('26,2176', 0o74206, '', 'PUSH', 'VXSC', '                                      PD- 4', kind='interp', line=182)
W('26,2177', 0o02037, '', '', 'VECOEM', kind='operand', line=183)
W('26,2200', 0o77761, 'VEMA', 'VXSC', kind='interp', line=184)
W('26,2201', 0o00001, '', '', '0D', kind='operand', line=185)
# Page 788
W('26,2202', 0o14005, '', 'STODL', '4D', '                                      PD- 2', kind='interp', line=187)
W('26,2203', 0o41425, '', 'DSU', 'PUSH', '                                      PD- 4', kind='interp', line=188)
W('26,2204', 0o14216, '', '', 'ONEB4', kind='operand', line=189)
W('26,2205', 0o53357, '', 'VXSC*', 'VAD', kind='interp', line=190)
W('26,2206', 0o02125, '', '', 'VECOEM +54D,1', kind='operand', line=191)
W('26,2207', 0o00005, '', '', '4D', kind='operand', line=192)
W('26,2210', 0o72500, '', 'TIX,1', 'VSL2', 'VEM IN METERS/CS x B-7 IN MPAC.', kind='interp', line=193)
W('26,2211', 0o54200, '', '', 'VEMA', kind='operand', line=194)
W('26,2212', 0o77616, '', 'RVQ', kind='interp', line=195)
W('26,2213', 0o22000, 'NINEB4', '2DEC', '9.0 B-4', kind='data', line=196)
W('26,2214', 0o00000, kind='data', line=196)

W('26,2215', 0o02000, 'ONEB4', '2DEC', '1.0 B-4', kind='data', line=198)
W('26,2216', 0o00000, kind='data', line=198)
