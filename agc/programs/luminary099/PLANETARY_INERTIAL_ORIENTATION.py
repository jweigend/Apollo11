"""PLANETARY_INERTIAL_ORIENTATION.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/PLANETARY_INERTIAL_ORIENTATION.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1140-1148 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('PLANETARY_INERTIAL_ORIENTATION', 'PLANETARY_INERTIAL_ORIENTATION.agc', 'Luminary099', pages='1140-1148')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     PLANETARY_INERTIAL_ORIENTATION.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
#
# Assembler:    yaYUL
# Contact:      Jim Lawton <jim.lawton@gmail.com>
# Website:      www.ibiblio.org/apollo.
# Pages:        1140-1148
# Mod history:  2009-05-28      JVL     Updated from page images.
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
# Assemble revision 001 of AGC program LMY99 by NASA 2021112-061
# 16:27 JULY 14, 1969

# Page 1140
# ..... RP-TO-R SUBROUTINE .....
# SUBROUTINE TO CONVERT RP (VECTOR IN PLANETARY COORDINATE SYSTEM,EITHER
# EARTH-FIXED OR MOON-FIXED) TO R (SAME VECTOR IN THE BASIC REF. SYSTEM)
#
# R=MT(T)*(RP+LPXRP)    MT= M MATRIX TRANSPOSE
#
# CALLING SEQUENCE
# L       CALL
# L+1            RP-TO-R
#
# SUBROUTINES USED
# EARTHMX,MOONMX,EARTHL
#
# ITEMS AVAILABLE FROM LAUNCH DATA
# 504LM= THE LIBRATION VECTOR L OF THE MOON AT TIME TIMSUBL,EXPRESSED
# IN THE MOON-FIXED COORD. SYSTEM   RADIANS  B0
# ITEMS NECESSARY FOR SUBR. USED (SEE DESCRIPTION OF SUBR.)
#
# INPUT
# MPAC= 0 FOR EARTH,NON-ZERO FOR MOON
# 0-5D= RP VECTOR
# 6-7D= TIME
#
# OUTPUT
# MPAC= R VECTOR METERS B-29 FOR EARTH, B-27 FOR MOON

#   SETLOC PLANTIN1
#   BANK

#   COUNT* $$/LUROT

W('26,3716', 0o46020, 'RP-TO-R', 'STQ', 'BHIZ', kind='interp', line=59)
W('26,3717', 0o00050, '', '', 'RPREXIT', kind='operand', line=60)
W('26,3720', 0o55733, '', '', 'RPTORA', kind='operand', line=61)
W('26,3721', 0o77624, '', 'CALL', '', 'COMPUTE M MATRIX FOR MOON', kind='interp', line=62)
W('26,3722', 0o51720, '', '', 'MOONMX', 'LP=LM FOR MOON  RADIANS B0', kind='operand', line=63)
W('26,3723', 0o77775, '', 'VLOAD', kind='interp', line=64)
W('26,3724', 0o02013, '', '', '504LM', kind='operand', line=65)
W('26,3725', 0o53235, 'RPTORB', 'VXV', 'VAD', kind='interp', line=66)
W('26,3726', 0o00001, '', '', '504RPR', kind='operand', line=67)
W('26,3727', 0o00001, '', '', '504RPR', kind='operand', line=68)
W('26,3730', 0o52105, '', 'VXM', 'GOTO', kind='interp', line=69)
W('26,3731', 0o00025, '', '', 'MMATRIX', 'MPAC=R=MT(T)*(RP+LPXRP)', kind='operand', line=70)
W('26,3732', 0o51706, '', '', 'RPRPXXXX', 'RESET PUSHLOC TO 0 BEFORE EXITING', kind='operand', line=71)
W('26,3733', 0o77624, 'RPTORA', 'CALL', '', 'EARTH COMPUTATIONS', kind='interp', line=72)
W('26,3734', 0o55743, '', '', 'EARTHMX', 'M MATRIX B-1', kind='operand', line=73)
W('26,3735', 0o77624, '', 'CALL', kind='interp', line=74)
W('26,3736', 0o15753, '', '', 'EARTHL', 'L VECTOR RADIANS B0', kind='operand', line=75)
W('26,3737', 0o76521, '', 'MXV', 'VSL1', 'LP=M(T)*L  RAD B-0', kind='interp', line=76)
W('26,3740', 0o00025, '', '', 'MMATRIX', kind='operand', line=77)
# Page 1141
W('26,3741', 0o77650, '', 'GOTO', kind='interp', line=79)
W('26,3742', 0o55725, '', '', 'RPTORB', kind='operand', line=80)
#   SETLOC PLANTIN
#   BANK
#   COUNT* $$/LUROT

# Page 1142
# ..... R-TO-RP SUBROUTINE .....
# SUBROUTINE TO CONVERT R (VECTOR IN REFERENCE COORD. SYSTEM) TO RP
# (VECTOR IN PLANETARY COORD SYSTEM) EITHER EARTH-FIXED OR MOON-FIXED
#
# RP=M(T)*(R-LXR)
#
# CALLING SEQUENCE
# L       CALL
# L+1            R-TO-RP
#
# SUBROUTINES USED
# EARTHMX,MOONMX,EARTHL
#
# INPUT
# MPAC= 0 FOR EARTH, NON-ZERO FOR MOON
# 0-5D= R VECTOR
# 6-7D= TIME
#
# ITEMS AVAILABLE FROM LAUNCH DATA
# 504LM= THE LIBRATION VECTOR L OF THE MOON AT TIME TIMSUBL,EXPRESSED
# IN THE MOON-FIXED COORD. SYSTEM   RADIANS B0
# ITEMS NECESSARY FOR SUBROUTINES USED (SEE DESCRIPTION OF SUBR.)
#
# OUTPUT
# MPAC=RP VECTOR METERS B-29 FOR EARTH, B-27 FOR MOON

W('24,3670', 0o46020, 'R-TO-RP', 'STQ', 'BHIZ', kind='interp', line=112)
W('24,3671', 0o00050, '', '', 'RPREXIT', kind='operand', line=113)
W('24,3672', 0o51712, '', '', 'RTORPA', kind='operand', line=114)
W('24,3673', 0o77624, '', 'CALL', kind='interp', line=115)
W('24,3674', 0o51720, '', '', 'MOONMX', kind='operand', line=116)
W('24,3675', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=117)
W('24,3676', 0o02013, '', '', '504LM', 'LP=LM', kind='operand', line=118)
W('24,3677', 0o00025, '', '', 'MMATRIX', kind='operand', line=119)
W('24,3700', 0o77772, '', 'VSL1', '', ' L=MT(T)*LP  RADIANS B0', kind='interp', line=120)
W('24,3701', 0o51235, 'RTORPB', 'VXV', 'BVSU', kind='interp', line=121)
W('24,3702', 0o00001, '', '', '504RPR', kind='operand', line=122)
W('24,3703', 0o00001, '', '', '504RPR', kind='operand', line=123)
W('24,3704', 0o77721, '', 'MXV', '', 'M(T)*(R-LXR) B-2', kind='interp', line=124)
W('24,3705', 0o00025, '', '', 'MMATRIX', kind='operand', line=125)
W('24,3706', 0o40372, 'RPRPXXXX', 'VSL1', 'SETPD', kind='interp', line=126)
W('24,3707', 0o00001, '', '', '0D', kind='operand', line=127)
W('24,3710', 0o77650, '', 'GOTO', kind='interp', line=128)
W('24,3711', 0o00050, '', '', 'RPREXIT', kind='operand', line=129)
W('24,3712', 0o77624, 'RTORPA', 'CALL', '', 'EARTH COMPUTATIONS', kind='interp', line=130)
W('24,3713', 0o55743, '', '', 'EARTHMX', kind='operand', line=131)
W('24,3714', 0o77624, '', 'CALL', kind='interp', line=132)
W('24,3715', 0o15753, '', '', 'EARTHL', kind='operand', line=133)
W('24,3716', 0o77650, '', 'GOTO', '', 'MPAC=L=(-AX,-AY,0) RAD B-0', kind='interp', line=134)
W('24,3717', 0o51701, '', '', 'RTORPB', kind='operand', line=135)

# Page 1143
# ..... MOONMX SUBROUTINE .....
# SUBROUTINE TO COMPUTE THE TRANSFORMATION MATRIX M FOR THE MOON
#
# CALLING SEQUENCE
# L       CALL
# L+1            MOONMX
#
# SUBROUTINES USED
# NEWANGLE
#
# INPUT
# 6-7D= TIME
# ITEMS AVAILABLE FROM LAUNCH DATA
# BSUBO,BDOT
# TIMSUBO,NODIO,NODDOT,FSUBO,FDOT
# COSI= COS(I) B-1
# SINI= SIN(I) B-1
# I  IS THE ANGLE BETWEEN THE MEAN LUNAR EQUATORIAL PLANE AND THE
# PLANE OF THE ECLIPTIC  (1 DEGREE  32.1 MINUTES)
#
# OUTPUT
# MMATRIX= 3X3 M MATRIX B-1   (STORED IN VAC AREA)

W('24,3720', 0o40220, 'MOONMX', 'STQ', 'SETPD', kind='interp', line=161)
W('24,3721', 0o00051, '', '', 'EARTHMXX', kind='operand', line=162)
W('24,3722', 0o00011, '', '', '8D', kind='operand', line=163)
W('24,3723', 0o77770, '', 'AXT,1', '', 'B REQUIRES SL 0, SL 5 IN NEWANGLE', kind='interp', line=164)
W('24,3724', 0o00005, '', '', '5', kind='operand', line=165)
W('24,3725', 0o65345, '', 'DLOAD', 'PDDL', 'PD 10D            8-9D=BSUBO', kind='interp', line=166)
W('24,3726', 0o14017, '', '', 'BSUBO', '                  10-11D= BDOT', kind='operand', line=167)
W('24,3727', 0o14011, '', '', 'BDOT', kind='operand', line=168)
W('24,3730', 0o45006, '', 'PUSH', 'CALL', 'PD 12D', kind='interp', line=169)
W('24,3731', 0o53743, '', '', 'NEWANGLE', 'EXIT WITH PD 8D AND MPAC= B  REVS B0', kind='operand', line=170)
W('24,3732', 0o71406, '', 'PUSH', 'COS', 'PD 10D', kind='interp', line=171)
W('24,3733', 0o14041, '', 'STODL', 'COB', 'PD 8D    COS(B) B-1', kind='interp', line=172)
W('24,3734', 0o77756, '', 'SIN', '', '         SIN(B) B-1', kind='interp', line=173)
W('24,3735', 0o14043, '', 'STODL', 'SOB', '          SETUP INPUT FOR NEWANGLE', kind='interp', line=174)
W('24,3736', 0o14015, '', '', 'FSUBO', '                    8-9D=FSUBO', kind='operand', line=175)
W('24,3737', 0o41525, '', 'PDDL', 'PUSH', 'PD 10D THEN 12D   10-11D=FDOT', kind='interp', line=176)
W('24,3740', 0o14007, '', '', 'FDOT', kind='operand', line=177)
W('24,3741', 0o45170, '', 'AXT,1', 'CALL', 'F REQUIRES SL 1, SL 6 IN NEWANGLE', kind='interp', line=178)
W('24,3742', 0o00004, '', '', '4', kind='operand', line=179)
W('24,3743', 0o53743, '', '', 'NEWANGLE', 'EXIT WITH PD 8D AND MPAC= F REVS B0', kind='operand', line=180)
W('24,3744', 0o14027, '', 'STODL', 'AVECTR +2', 'SAVE F TEMP', kind='interp', line=181)
W('24,3745', 0o14013, '', '', 'NODIO', '                      8-9D=NODIO', kind='operand', line=182)
W('24,3746', 0o41525, '', 'PDDL', 'PUSH', 'PD 10D THEN 12D     10-11D=NODDOT', kind='interp', line=183)
W('24,3747', 0o14005, '', '', 'NODDOT', '                      MPAC=T', kind='operand', line=184)
W('24,3750', 0o45170, '', 'AXT,1', 'CALL', 'NODE REQUIRES SL 0, SL 5 IN NEWANGLE', kind='interp', line=185)
W('24,3751', 0o00005, '', '', '5', kind='operand', line=186)
W('24,3752', 0o53743, '', '', 'NEWANGLE', 'EXIT WITH PD 8D AND MPAC= NODI REVS B0', kind='operand', line=187)
# Page 1144
W('24,3753', 0o71406, '', 'PUSH', 'COS', 'PD 10D   8-9D= NODI  REVS  B0', kind='interp', line=189)
W('24,3754', 0o77606, '', 'PUSH', '', 'PD 12D 10-11D= COS(NODI)  B-1', kind='interp', line=190)
W('24,3755', 0o00025, '', 'STORE', 'AVECTR', kind='interp', line=191)
W('24,3756', 0o76405, '', 'DMP', 'SL1R', kind='interp', line=192)
W('24,3757', 0o00041, '', '', 'COB', '                        COS(NODI)    B-1', kind='operand', line=193)
W('24,3760', 0o14035, '', 'STODL', 'BVECTR +2', 'PD 10D   20-25D=AVECTR= COB*SIN(NODI)', kind='interp', line=194)
W('24,3761', 0o76405, '', 'DMP', 'SL1R', '                        SOB*SIN(NODI)', kind='interp', line=195)
W('24,3762', 0o00043, '', '', 'SOB', kind='operand', line=196)
W('24,3763', 0o14037, '', 'STODL', 'BVECTR +4', 'PD 8D', kind='interp', line=197)
W('24,3764', 0o41556, '', 'SIN', 'PUSH', 'PD 10D                 -SIN(NODI)   B-1', kind='interp', line=198)
W('24,3765', 0o77676, '', 'DCOMP', '', '         26-31D=BVECTR= COB*COS(NODI)', kind='interp', line=199)
W('24,3766', 0o14033, '', 'STODL', 'BVECTR', 'PD 8D                   SOB*COS(NODI)', kind='interp', line=200)
W('24,3767', 0o00027, '', '', 'AVECTR +2', 'MOVE F FROM TEMP LOC. TO 504F', kind='operand', line=201)
W('24,3770', 0o14007, '', 'STODL', '504F', kind='interp', line=202)
W('24,3771', 0o76405, '', 'DMP', 'SL1R', kind='interp', line=203)
W('24,3772', 0o00041, '', '', 'COB', kind='operand', line=204)
W('24,3773', 0o77650, '', 'GOTO', kind='interp', line=205)
W('24,3774', 0o53671, '', '', 'MOONMXA', kind='operand', line=206)

#   BANK 25
#   SETLOC PLANTIN3
#   BANK
#   COUNT* $$/LUROT

W('25,3671', 0o14027, 'MOONMXA', 'STODL', 'AVECTR +2', kind='interp', line=213)
W('25,3672', 0o00011, '', '', 'SINNODI', '8-9D=SIN(NODI)  B-1', kind='operand', line=214)
W('25,3673', 0o76405, '', 'DMP', 'SL1R', kind='interp', line=215)
W('25,3674', 0o00043, '', '', 'SOB', kind='operand', line=216)
W('25,3675', 0o14031, '', 'STODL', 'AVECTR +4', '                         0', kind='interp', line=217)
W('25,3676', 0o06522, '', '', 'HI6ZEROS', '        8-13D= CVECTR= -SOB  B-1', kind='operand', line=218)
W('25,3677', 0o57525, '', 'PDDL', 'DCOMP', 'PD 10D                  COB', kind='interp', line=219)
W('25,3700', 0o00043, '', '', 'SOB', kind='operand', line=220)
W('25,3701', 0o63325, '', 'PDDL', 'PDVL', 'PD 12D THEN PD 14D', kind='interp', line=221)
W('25,3702', 0o00041, '', '', 'COB', kind='operand', line=222)
W('25,3703', 0o00033, '', '', 'BVECTR', kind='operand', line=223)
W('25,3704', 0o63361, '', 'VXSC', 'PDVL', 'PD 20D         BVECTR*SINI  B-2', kind='interp', line=224)
W('25,3705', 0o14003, '', '', 'SINI', kind='operand', line=225)
W('25,3706', 0o00011, '', '', 'CVECTR', kind='operand', line=226)
W('25,3707', 0o53361, '', 'VXSC', 'VAD', 'PD 14D         CVECTR*COSI  B-2', kind='interp', line=227)
W('25,3710', 0o14001, '', '', 'COSI', kind='operand', line=228)
W('25,3711', 0o77772, '', 'VSL1', kind='interp', line=229)
W('25,3712', 0o24041, '', 'STOVL', 'MMATRIX +12D', 'PD 8D  M2=BVECTR*SINI+CVECTR*COSI  B-1', kind='interp', line=230)
W('25,3713', 0o63361, '', 'VXSC', 'PDVL', 'PD 14D', kind='interp', line=231)
W('25,3714', 0o14003, '', '', 'SINI', '               CVECTR*SINI  B-2', kind='operand', line=232)
W('25,3715', 0o00033, '', '', 'BVECTR', kind='operand', line=233)
W('25,3716', 0o52361, '', 'VXSC', 'VSU', 'PD 8D          BVECTR*COSI  B-2', kind='interp', line=234)
W('25,3717', 0o14001, '', '', 'COSI', kind='operand', line=235)
W('25,3720', 0o65372, '', 'VSL1', 'PDDL', 'PD 14D', kind='interp', line=236)
W('25,3721', 0o00007, '', '', '504F', '8-13D=DVECTR=BVECTR*COSI-CVECTR*SINI B-1', kind='operand', line=237)
W('25,3722', 0o74346, '', 'COS', 'VXSC', kind='interp', line=238)
# Page 1145
W('25,3723', 0o00011, '', '', 'DVECTR', kind='operand', line=240)
W('25,3724', 0o73525, '', 'PDDL', 'SIN', 'PD 20D  14-19D= DVECTR*COSF  B-2', kind='interp', line=241)
W('25,3725', 0o00007, '', '', '504F', kind='operand', line=242)
W('25,3726', 0o52361, '', 'VXSC', 'VSU', 'PD 14D          AVECTR*SINF  B-2', kind='interp', line=243)
W('25,3727', 0o00025, '', '', 'AVECTR', kind='operand', line=244)
W('25,3730', 0o77772, '', 'VSL1', kind='interp', line=245)
W('25,3731', 0o14033, '', 'STODL', 'MMATRIX +6', 'M1= AVECTR*SINF-DVECTR*COSF  B-1', kind='interp', line=246)
W('25,3732', 0o00007, '', '', '504F', kind='operand', line=247)
W('25,3733', 0o74356, '', 'SIN', 'VXSC', 'PD 8D', kind='interp', line=248)
W('25,3734', 0o71525, '', 'PDDL', 'COS', 'PD 14D  8-13D=DVECTR*SINF B-2', kind='interp', line=249)
W('25,3735', 0o00007, '', '', '504F', kind='operand', line=250)
W('25,3736', 0o53361, '', 'VXSC', 'VAD', 'PD 8D         AVECTR*COSF B-2', kind='interp', line=251)
W('25,3737', 0o00025, '', '', 'AVECTR', kind='operand', line=252)
W('25,3740', 0o57572, '', 'VSL1', 'VCOMP', kind='interp', line=253)
W('25,3741', 0o34025, '', 'STCALL', 'MMATRIX', 'M0= -(AVECTR*COSF+DVECTR*SINF)  B-1', kind='interp', line=254)
W('25,3742', 0o00051, '', '', 'EARTHMXX', kind='operand', line=255)
# COMPUTE X=X0+(XDOT)(T+T0)
# 8-9D= X0 (REVS B-0),PUSHLOC SET AT 12D
# 10-11D=XDOT (REVS/CSEC) SCALED B+23 FOR WEARTH,B+28 FOR NODDOT AND BDOT
# AND B+27 FOR FDOT
# X1=DIFFERENCE IN 23 AND SCALING OF XDOT,=0 FOR WEARTH,5 FOR NODDOT AND
# BDOT AND 4 FOR FDOT
# 6-7D=T (CSEC B-28), TIMSUBO= (CSEC B-42 TRIPLE PREC.)

W('25,3743', 0o54345, 'NEWANGLE', 'DLOAD', 'SR', 'ENTER PD 12D', kind='interp', line=264)
W('25,3744', 0o00007, '', '', '6D', kind='operand', line=265)
W('25,3745', 0o20617, '', '', '14D', kind='operand', line=266)
W('25,3746', 0o72371, '', 'TAD', 'TLOAD', 'CHANGE MODE TO TP', kind='interp', line=267)
W('25,3747', 0o01707, '', '', 'TIMSUBO', kind='operand', line=268)
W('25,3750', 0o00155, '', '', 'MPAC', kind='operand', line=269)
W('25,3751', 0o14017, '', 'STODL', 'TIMSUBM', 'T+T0 CSEC B-42', kind='interp', line=270)
W('25,3752', 0o00020, '', '', 'TIMSUBM +1', kind='operand', line=271)
W('25,3753', 0o77605, '', 'DMP', '', 'PD 10D  MULT BY XDOT IN 10-11D', kind='interp', line=272)
W('25,3754', 0o43257, '', 'SL*', 'DAD', 'PD 8D   ADD X0 IN 8-9D AFTER SHIFTING', kind='interp', line=273)
W('25,3755', 0o20206, '', '', '5,1', '        SUCH THAT SCALING IS B-0', kind='operand', line=274)
W('25,3756', 0o67206, '', 'PUSH', 'SLOAD', 'PD 10D SAVE PARTIAL (X0+XDOT*T) IN 8-9D', kind='interp', line=275)
W('25,3757', 0o00017, '', '', 'TIMSUBM', kind='operand', line=276)
W('25,3760', 0o41261, '', 'SL', 'DMP', kind='interp', line=277)
W('25,3761', 0o20212, '', '', '9D', kind='operand', line=278)
W('25,3762', 0o00013, '', '', '10D', 'XDOT', kind='operand', line=279)
W('25,3763', 0o43257, '', 'SL*', 'DAD', 'PD 8D   SHIFT SUCH THAT THIS PART OF X', kind='interp', line=280)
W('25,3764', 0o20213, '', '', '10D,1', '        IS SCALED REVS/CSEC B-0', kind='operand', line=281)
W('25,3765', 0o77600, '', 'BOV', '', 'TURN OFF OVERFLOW IF SET BY SHIFT', kind='interp', line=282)
W('25,3766', 0o53767, '', '', '+1', 'INSTRUCTION BEFORE EXITING', kind='operand', line=283)
W('25,3767', 0o77616, '', 'RVQ', '', 'MPAC=X= X0+(XDOT)(T+T0)  REVS B0', kind='interp', line=284)

# Page 1146
# ..... EARTHMX SUBROUTINE .....
# SUBROUTINE TO COMPUTE THE TRANSFORMATION MATRIX M FOR THE EARTH
#
# CALLING SEQUENCE
# L       CALL
# L+1            EARTHMX
#
# SUBROUTINE USED
# NEWANGLE
#
# INPUT
# INPUT AVAILABLE FROM LAUNCH DATA     AZO  REVS B-0
# TEPHEM  CSEC B-42
# 6-7D= TIME CSEC B-28
#
# OUTPUT
# MMATRIX= 3X3 M MATRIX B-1   (STORED IN VAC AREA)

#   BANK 26
#   SETLOC PLANTIN1
#   BANK
#   COUNT* $$/LUROT

W('26,3743', 0o40220, 'EARTHMX', 'STQ', 'SETPD', 'SET   8-9D=AZO', kind='interp', line=310)
W('26,3744', 0o00051, '', '', 'EARTHMXX', kind='operand', line=311)
W('26,3745', 0o00011, '', '', '8D', '10-11D=WEARTH', kind='operand', line=312)
W('26,3746', 0o77770, '', 'AXT,1', '', 'FOR SL 5, AND SL 10  IN NEWANGLE', kind='interp', line=313)
W('26,3747', 0o00000, '', '', '0', kind='operand', line=314)
W('26,3750', 0o65345, '', 'DLOAD', 'PDDL', '  LEAVING PD SET AT 12D FOR NEWANGLE', kind='interp', line=315)
W('26,3751', 0o01712, '', '', 'AZO', kind='operand', line=316)
W('26,3752', 0o14021, '', '', 'WEARTH', kind='operand', line=317)
W('26,3753', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=318)
W('26,3754', 0o53743, '', '', 'NEWANGLE', kind='operand', line=319)
W('26,3755', 0o41401, '', 'SETPD', 'PUSH', '18-19D=504AZ', kind='interp', line=320)
W('26,3756', 0o00023, '', '', '18D', '                   COS(AZ) SIN(AZ) 0', kind='operand', line=321)
W('26,3757', 0o65346, '', 'COS', 'PDDL', '20-37D=  MMATRIX= -SIN(AZ) COS(AZ) 0 B-1', kind='interp', line=322)
W('26,3760', 0o00023, '', '', '504AZ', '                    0       0      1', kind='operand', line=323)
W('26,3761', 0o65356, '', 'SIN', 'PDDL', kind='interp', line=324)
W('26,3762', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=325)
W('26,3763', 0o73525, '', 'PDDL', 'SIN', kind='interp', line=326)
W('26,3764', 0o00023, '', '', '504AZ', kind='operand', line=327)
W('26,3765', 0o65276, '', 'DCOMP', 'PDDL', kind='interp', line=328)
W('26,3766', 0o00023, '', '', '504AZ', kind='operand', line=329)
W('26,3767', 0o63346, '', 'COS', 'PDVL', kind='interp', line=330)
W('26,3770', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=331)
W('26,3771', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=332)
W('26,3772', 0o06520, '', '', 'HIDPHALF', kind='operand', line=333)
W('26,3773', 0o77650, '', 'GOTO', kind='interp', line=334)
W('26,3774', 0o00051, '', '', 'EARTHMXX', kind='operand', line=335)

# Page 1147
# ..... EARTHL SUBROUTINE .....
# SUBROUTINE TO COMPUTE L VECTOR FOR EARTH
#
# CALLING SEQUENCE
# L       CALL
# L+1            EARTHL
#
# INPUT
# AXO,AYO SET AT LAUNCH TIME WITH AYO IMMEDIATELY FOLLOWING AXO IN CORE
#
# OUTPUT
# -AX
# MPAC=   -AY    RADIANS B-0
# 0

#   BANK 06
#   SETLOC EARTHLOC
#   BANK
#   COUNT* $$/LUROT

W('06,3753', 0o57545, 'EARTHL', 'DLOAD', 'DCOMP', kind='interp', line=358)
W('06,3754', 0o01716, '', '', 'AXO', kind='operand', line=359)
W('06,3755', 0o14017, '', 'STODL', '504LPL', kind='interp', line=360)
W('06,3756', 0o01714, '', '', '-AYO', kind='operand', line=361)
W('06,3757', 0o14021, '', 'STODL', '504LPL +2', kind='interp', line=362)
W('06,3760', 0o24007, '', '', 'LO6ZEROS', kind='operand', line=363)
W('06,3761', 0o24023, '', 'STOVL', '504LPL +4', kind='interp', line=364)
W('06,3762', 0o00017, '', '', '504LPL', kind='operand', line=365)
W('06,3763', 0o77616, '', 'RVQ', kind='interp', line=366)

# Page 1148
# CONSTANTS AND ERASABLE ASSIGNMENTS
S('1B1', 'equals', 0o34004, line=370)  # 1  SCALED B-1
S('RPREXIT', 'equals', 0o50, line=371)  # R-TO-RP AND RP-TO-R SUBR EXIT
S('EARTHMXX', 'equals', 0o51, line=372)  # EARTHMX,MOONMX SUBR. EXITS
S('504RPR', 'equals', 0o0, line=373)  # 6 REGS  R OR RP VECTOR
S('SINNODI', 'equals', 0o10, line=374)  # 2       SIN(NODI)
S('DVECTR', 'equals', 0o10, line=375)  # 6       D VECTOR MOON
S('CVECTR', 'equals', 0o10, line=376)  # 6       C VECTR MOON
S('504AZ', 'equals', 0o22, line=377)  # 2      AZ
S('TIMSUBM', 'equals', 0o16, line=378)  # 3       TIME SUB M (MOON) T+T0 IN GETAZ
S('504LPL', 'equals', 0o16, line=379)  # 6       L OR LP VECTOR
S('AVECTR', 'equals', 0o24, line=380)  # 6       A VECTOR (MOON)
S('BVECTR', 'equals', 0o32, line=381)  # 6       B VECTOR (MOON)
S('MMATRIX', 'equals', 0o24, line=382)  # 18      M MATRIX
S('COB', 'equals', 0o40, line=383)  # 2       COS(B) B-1
S('SOB', 'equals', 0o42, line=384)  # 2       SIN(B) B-1
S('504F', 'equals', 0o6, line=385)  # 2       F (MOON)
