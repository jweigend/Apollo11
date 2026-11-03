"""PLANETARY_INERTIAL_ORIENTATION.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/PLANETARY_INERTIAL_ORIENTATION.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1243-1251 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('PLANETARY_INERTIAL_ORIENTATION', 'PLANETARY_INERTIAL_ORIENTATION.agc', 'Comanche055', pages='1243-1251')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     PLANETARY_INERTIAL_ORIENTATION.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1243-1251
# Mod history:  2009-05-14 RSB  Adapted from the Colossus249/ file of the
# same name, using Comanche055 page images.
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

# Page 1243
# PLANETARY INERTIAL ORIENTATION

# ..... RP-TO-R SUBROUTINE .....
# SUBROUTINE TO CONVERT RP (VECTOR IN PLANETARY COORDINATE SYSTEM,EITHER
# EARTH-FIXED OR MOON-FIXED) TO R (SAME VECTOR IN BASIC REF. SYSTEM)

# R=MT(T)*(RP+LPXRP)      MT= M MATRIX TRANSPOSE

# CALLING SEQUENCE
# L       CALL
# L+1             RP-TO-R

# SUBROUTINES USED
# EARTHMX,MOONMX,EARTHL

# ITEMS AVAILABLE FROM LAUNCH DATA
# 504LM= THE LIBRATION VECTOR L OF THE MOON AT TIME TIMSUBL,EXPRESSED
# IN THE MOON-FIXED COORD. SYSTEM         RADIANS B0
# ITEMS NECESSARY FOR SUBR. USED (SEE DESCRIPTION OF SUBR.)

# INPUT
# MPAC= 0 FOR EARTH,NON-ZERO FOR MOON
# 0-5D= RP VECTOR
# 6-7D= TIME

# OUTPUT
# MPAC= R VECTOR METERS B-29 FOR EARTH, B-27 FOR MOON

#   SETLOC PLANTIN
#   BANK

#   COUNT* $$/LUROT

W('26,3344', 0o46020, 'RP-TO-R', 'STQ', 'BHIZ', kind='interp', line=64)
W('26,3345', 0o00050, '', '', 'RPREXIT', kind='operand', line=65)
W('26,3346', 0o55361, '', '', 'RPTORA', kind='operand', line=66)
W('26,3347', 0o77624, '', 'CALL', '', 'COMPUTE M MATRIX FOR MOON', kind='interp', line=67)
W('26,3350', 0o55421, '', '', 'MOONMX', 'LP=LM FOR MOON        RADIANS B0', kind='operand', line=68)
W('26,3351', 0o77775, '', 'VLOAD', kind='interp', line=69)
W('26,3352', 0o02012, '', '', '504LM', kind='operand', line=70)
W('26,3353', 0o53235, 'RPTORB', 'VXV', 'VAD', kind='interp', line=71)
W('26,3354', 0o00001, '', '', '504RPR', kind='operand', line=72)
W('26,3355', 0o00001, '', '', '504RPR', kind='operand', line=73)
W('26,3356', 0o52105, '', 'VXM', 'GOTO', kind='interp', line=74)
W('26,3357', 0o00025, '', '', 'MMATRIX', 'MPAC=R=MT(T)*(RP+LPXRP)', kind='operand', line=75)
W('26,3360', 0o55407, '', '', 'RPRPXXXX', 'RESET PUSHLOC TO 0 BEFORE EXITING', kind='operand', line=76)
W('26,3361', 0o77624, 'RPTORA', 'CALL', '', 'EARTH COMPUTATIONS', kind='interp', line=77)
W('26,3362', 0o55573, '', '', 'EARTHMX', 'M MATRIX B-1', kind='operand', line=78)
W('26,3363', 0o77624, '', 'CALL', kind='interp', line=79)
W('26,3364', 0o55625, '', '', 'EARTHL', 'L VECTOR RADIANS B0', kind='operand', line=80)
W('26,3365', 0o76521, '', 'MXV', 'VSL1', 'LP=M(T)*L     RAD B-0', kind='interp', line=81)
W('26,3366', 0o00025, '', '', 'MMATRIX', kind='operand', line=82)
# Page 1244
W('26,3367', 0o77650, '', 'GOTO', kind='interp', line=84)
W('26,3370', 0o55353, '', '', 'RPTORB', kind='operand', line=85)

# Page 1245
# ..... R-TO-RP SUBROUTINE .....
# SUBROUTINE TO CONVERT R (VECTOR IN REFERENCE COORD. SYSTEM) TO RP
# (VECTOR IN PLANETARY COORD SYSTEM) EITHER EARTH-FIXED OR MOON-FIXED

# RP = M(T) * (R - L X R)

# CALLING SEQUENCE
# L       CALL
# L+1             R-TO-RP

# SUBROUTINES USED
# EARTHMX,MOONMX,EARTHL

# INPUT
# MPAC= 0 FOR EARTH,NON-ZERO FOR MOON
# 0-5D= R VECTOR
# 6-7D= TIME

# ITEMS AVAILABLE FROM LAUNCH DATA
# 504LM= THE LIBRATION VECTOR L OF THE MOON AT TIME TIMSUBL,EXPRESSED
# IN THE MOON-FIXED COORD. SYSTEM         RADIANS B0
# ITEMS NECESSARY FOR SUBROUTINES USED (SEE DESCRIPTION OF SUBR.)

# OUTPUT
# MPAC=RP VECTOR METERS B-29 FOR EARTH, B-27 FOR MOON

W('26,3371', 0o46020, 'R-TO-RP', 'STQ', 'BHIZ', kind='interp', line=114)
W('26,3372', 0o00050, '', '', 'RPREXIT', kind='operand', line=115)
W('26,3373', 0o55413, '', '', 'RTORPA', kind='operand', line=116)
W('26,3374', 0o77624, '', 'CALL', kind='interp', line=117)
W('26,3375', 0o55421, '', '', 'MOONMX', kind='operand', line=118)
W('26,3376', 0o61375, '', 'VLOAD', 'VXM', kind='interp', line=119)
W('26,3377', 0o02012, '', '', '504LM', 'LP=LM', kind='operand', line=120)
W('26,3400', 0o00025, '', '', 'MMATRIX', kind='operand', line=121)
W('26,3401', 0o77772, '', 'VSL1', '', 'L=MT(T)*LP    RADIANS B0', kind='interp', line=122)
W('26,3402', 0o51235, 'RTORPB', 'VXV', 'BVSU', kind='interp', line=123)
W('26,3403', 0o00001, '', '', '504RPR', kind='operand', line=124)
W('26,3404', 0o00001, '', '', '504RPR', kind='operand', line=125)
W('26,3405', 0o77721, '', 'MXV', '', 'M(T)*(R-LXR)  B-2', kind='interp', line=126)
W('26,3406', 0o00025, '', '', 'MMATRIX', kind='operand', line=127)
W('26,3407', 0o40372, 'RPRPXXXX', 'VSL1', 'SETPD', kind='interp', line=128)
W('26,3410', 0o00001, '', '', '0D', kind='operand', line=129)
W('26,3411', 0o77650, '', 'GOTO', kind='interp', line=130)
W('26,3412', 0o00050, '', '', 'RPREXIT', kind='operand', line=131)
W('26,3413', 0o77624, 'RTORPA', 'CALL', '', 'EARTH COMPUTATIONS', kind='interp', line=132)
W('26,3414', 0o55573, '', '', 'EARTHMX', kind='operand', line=133)
W('26,3415', 0o77624, '', 'CALL', kind='interp', line=134)
W('26,3416', 0o55625, '', '', 'EARTHL', kind='operand', line=135)
W('26,3417', 0o77650, '', 'GOTO', '', 'MPAC=L=(-AX,-AY,0) RAD B-0', kind='interp', line=136)
W('26,3420', 0o55402, '', '', 'RTORPB', kind='operand', line=137)

# Page 1246
# ..... MOONMX SUBROUTINE .....
# SUBROUTINE TO COMPUTE THE TRANSFORMATION MATRIX M FOR THE MOON

# CALLING SEQUENCE
# L       CALL
# L+1             MOONMX

# SUBROUTINES USED
# NEWANGLE

# INPUT
# 6-7D= TIME
# ITEMS AVAILABLE FROM LAUNCH DATA
# BSUBO,BDOT
# TIMSUBO,NODIO,NODDOT,FSUBO,FDOT
# COSI= COS(I)    B-1
# SINI= SIN(I)    B-1
# I IS THE ANGLE BETWEEN THE MEAN LUNAR EQUATORIAL PLANE AND THE
# PLANE OF THE ECLIPTIC (1 DEGREE 32.1 MINUTES)

# OUTPUT
# MMATRIX= 3X3 M MATRIX B-1       (STORED IN VAC AREA)

W('26,3421', 0o40220, 'MOONMX', 'STQ', 'SETPD', kind='interp', line=163)
W('26,3422', 0o00051, '', '', 'EARTHMXX', kind='operand', line=164)
W('26,3423', 0o00011, '', '', '8D', kind='operand', line=165)
W('26,3424', 0o77770, '', 'AXT,1', '', 'B REQUIRES SL 0, SL 5 IN NEWANGLE', kind='interp', line=166)
W('26,3425', 0o00005, '', '', '5', kind='operand', line=167)
W('26,3426', 0o65345, '', 'DLOAD', 'PDDL', 'PD 10D        8-9D=BSUBO', kind='interp', line=168)
W('26,3427', 0o15655, '', '', 'BSUBO', '              10-11D= BDOT', kind='operand', line=169)
W('26,3430', 0o15647, '', '', 'BDOT', kind='operand', line=170)
W('26,3431', 0o45006, '', 'PUSH', 'CALL', 'PD 12D', kind='interp', line=171)
W('26,3432', 0o55546, '', '', 'NEWANGLE', 'EXIT WITH PD 8D AND MPAC= B   REVS B0', kind='operand', line=172)
W('26,3433', 0o71406, '', 'PUSH', 'COS', 'PD 10D', kind='interp', line=173)
W('26,3434', 0o14041, '', 'STODL', 'COB', 'PD 8D         COS(B) B-1', kind='interp', line=174)
W('26,3435', 0o77756, '', 'SIN', '', '              SIN(B) B-1', kind='interp', line=175)
W('26,3436', 0o14043, '', 'STODL', 'SOB', '              SETUP INPUT FOR NEWANGLE', kind='interp', line=176)
W('26,3437', 0o15653, '', '', 'FSUBO', '                      8-9D=FSUBO', kind='operand', line=177)
W('26,3440', 0o41525, '', 'PDDL', 'PUSH', 'PD 10D THEN 12D     10-11D=FDOT', kind='interp', line=178)
W('26,3441', 0o15645, '', '', 'FDOT', kind='operand', line=179)
W('26,3442', 0o45170, '', 'AXT,1', 'CALL', 'F REQUIRES SL 1, SL 6 IN NEWANGLE', kind='interp', line=180)
W('26,3443', 0o00004, '', '', '4', kind='operand', line=181)
W('26,3444', 0o55546, '', '', 'NEWANGLE', 'EXIT WITH PD 8D AND MPAC= F REVS B0', kind='operand', line=182)
W('26,3445', 0o14027, '', 'STODL', 'AVECTR +2', 'SAVE F TEMP', kind='interp', line=183)
W('26,3446', 0o15651, '', '', 'NODIO', '                      8-9D=NODIO', kind='operand', line=184)
W('26,3447', 0o41525, '', 'PDDL', 'PUSH', 'PD 10D THEN 12D     10-11D=NODDOT', kind='interp', line=185)
W('26,3450', 0o15643, '', '', 'NODDOT', '                      MPAC=T', kind='operand', line=186)
W('26,3451', 0o45170, '', 'AXT,1', 'CALL', 'NODE REQUIRES SL 0, SL 5 IN NEWANGLE', kind='interp', line=187)
W('26,3452', 0o00005, '', '', '5', kind='operand', line=188)
W('26,3453', 0o55546, '', '', 'NEWANGLE', 'EXIT WITH PD 8D AND MPAC= NODI REVS B0', kind='operand', line=189)
# Page 1247
W('26,3454', 0o71406, '', 'PUSH', 'COS', 'PD 10D        8-9D= NODI REVS B0', kind='interp', line=191)
W('26,3455', 0o77606, '', 'PUSH', '', 'PD 12D      10-11D= COS(NODI) B-1', kind='interp', line=192)
W('26,3456', 0o00025, '', 'STORE', 'AVECTR', kind='interp', line=193)
W('26,3457', 0o76405, '', 'DMP', 'SL1R', kind='interp', line=194)
W('26,3460', 0o00041, '', '', 'COB', '                      COS(NODI) B-1', kind='operand', line=195)
W('26,3461', 0o14035, '', 'STODL', 'BVECTR +2', 'PD 10D  20-25D=AVECTR=COB*SIN(NODI)', kind='interp', line=196)
W('26,3462', 0o76405, '', 'DMP', 'SL1R', '                      SOB*SIN(NODI)', kind='interp', line=197)
W('26,3463', 0o00043, '', '', 'SOB', kind='operand', line=198)
W('26,3464', 0o14037, '', 'STODL', 'BVECTR +4', 'PD 8D', kind='interp', line=199)
W('26,3465', 0o41556, '', 'SIN', 'PUSH', 'PD 10D                -SIN(NODI) B-1', kind='interp', line=200)
W('26,3466', 0o77676, '', 'DCOMP', '', '        26-31D=BVECTR= COB*COS(NODI)', kind='interp', line=201)
W('26,3467', 0o14033, '', 'STODL', 'BVECTR', 'PD 8D                  SOB*COS(NODI)', kind='interp', line=202)
W('26,3470', 0o00027, '', '', 'AVECTR +2', 'MOVE F FROM TEMP LOC. TO 504F', kind='operand', line=203)
W('26,3471', 0o14007, '', 'STODL', '504F', kind='interp', line=204)
W('26,3472', 0o76405, '', 'DMP', 'SL1R', kind='interp', line=205)
W('26,3473', 0o00041, '', '', 'COB', kind='operand', line=206)
W('26,3474', 0o14027, '', 'STODL', 'AVECTR +2', kind='interp', line=207)
W('26,3475', 0o00011, '', '', 'SINNODI', '8-9D=SIN(NODI) B-1', kind='operand', line=208)
W('26,3476', 0o76405, '', 'DMP', 'SL1R', kind='interp', line=209)
W('26,3477', 0o00043, '', '', 'SOB', kind='operand', line=210)
W('26,3500', 0o14031, '', 'STODL', 'AVECTR +4', '                       0', kind='interp', line=211)
W('26,3501', 0o15335, '', '', 'HI6ZEROS', '      8-13D= CVECTR= -SOB B-1', kind='operand', line=212)
W('26,3502', 0o57525, '', 'PDDL', 'DCOMP', 'PD 10D                COB', kind='interp', line=213)
W('26,3503', 0o00043, '', '', 'SOB', kind='operand', line=214)
W('26,3504', 0o63325, '', 'PDDL', 'PDVL', 'PD 12D THEN PD 14D', kind='interp', line=215)
W('26,3505', 0o00041, '', '', 'COB', kind='operand', line=216)
W('26,3506', 0o00033, '', '', 'BVECTR', kind='operand', line=217)
W('26,3507', 0o63361, '', 'VXSC', 'PDVL', 'PD 20D        BVECTR*SINI B-2', kind='interp', line=218)
W('26,3510', 0o15641, '', '', 'SINI', kind='operand', line=219)
W('26,3511', 0o00011, '', '', 'CVECTR', kind='operand', line=220)
W('26,3512', 0o53361, '', 'VXSC', 'VAD', 'PD 14D        CVECTR*COSI B-2', kind='interp', line=221)
W('26,3513', 0o15637, '', '', 'COSI', kind='operand', line=222)
W('26,3514', 0o77772, '', 'VSL1', kind='interp', line=223)
W('26,3515', 0o24041, '', 'STOVL', 'MMATRIX +12D', 'PD 8D  M2=BVECTR*SINI+CVECTR*COSI B-1', kind='interp', line=224)
W('26,3516', 0o63361, '', 'VXSC', 'PDVL', 'PD 14D', kind='interp', line=225)
W('26,3517', 0o15641, '', '', 'SINI', '              CVECTR*SINI B-2', kind='operand', line=226)
W('26,3520', 0o00033, '', '', 'BVECTR', kind='operand', line=227)
W('26,3521', 0o52361, '', 'VXSC', 'VSU', 'PD 8D         BVECTR*COSI B-2', kind='interp', line=228)
W('26,3522', 0o15637, '', '', 'COSI', kind='operand', line=229)
W('26,3523', 0o65372, '', 'VSL1', 'PDDL', 'PD 14D', kind='interp', line=230)
W('26,3524', 0o00007, '', '', '504F', '8-13D=DVECTR=BVECTR*COSI-CVECTR*SINI B-1', kind='operand', line=231)
W('26,3525', 0o74346, '', 'COS', 'VXSC', kind='interp', line=232)
W('26,3526', 0o00011, '', '', 'DVECTR', kind='operand', line=233)
W('26,3527', 0o73525, '', 'PDDL', 'SIN', 'PD 20D  14-19D= DVECTR*COSF B-2', kind='interp', line=234)
W('26,3530', 0o00007, '', '', '504F', kind='operand', line=235)
W('26,3531', 0o52361, '', 'VXSC', 'VSU', 'PD 14D          AVECTR*SINF B-2', kind='interp', line=236)
W('26,3532', 0o00025, '', '', 'AVECTR', kind='operand', line=237)
W('26,3533', 0o77772, '', 'VSL1', kind='interp', line=238)
W('26,3534', 0o14033, '', 'STODL', 'MMATRIX +6', 'M1= AVECTR*SINF-DVECTR*COSF B-1', kind='interp', line=239)
W('26,3535', 0o00007, '', '', '504F', kind='operand', line=240)
# Page 1248
W('26,3536', 0o74356, '', 'SIN', 'VXSC', 'PD 8D', kind='interp', line=242)
W('26,3537', 0o71525, '', 'PDDL', 'COS', 'PD 14D  8-13D=DVECTR*SINF B-2', kind='interp', line=243)
W('26,3540', 0o00007, '', '', '504F', kind='operand', line=244)
W('26,3541', 0o53361, '', 'VXSC', 'VAD', 'PD 8D         AVECTR*COSF B-2', kind='interp', line=245)
W('26,3542', 0o00025, '', '', 'AVECTR', kind='operand', line=246)
W('26,3543', 0o57572, '', 'VSL1', 'VCOMP', kind='interp', line=247)
W('26,3544', 0o34025, '', 'STCALL', 'MMATRIX', 'M0= -(AVECTR*COSF+DVECTR*SINF) B-1', kind='interp', line=248)
W('26,3545', 0o00051, '', '', 'EARTHMXX', kind='operand', line=249)
# COMPUTE X=X0+(XDOT)(T+T0)
# 8-9D= X0 (REVS B-0),PUSHLOC SET AT 12D
# 10-11D=XDOT (REVS/CSEC) SCALED B+23 FOR WEARTH,B+28 FOR NODDOT AND BDOT
# AND B+27 FOR FDOT
# X1=DIFFERENCE IN 23 AND SCALING OF XDOT,=0 FOR WEARTH,5 FOR NDDOT AND
# BDOT AND 4 FOR FDOT
# 6-7D=T (CSEC B-28), TIMSUBO= (CSEC B-42 TRIPLE PREC.)

W('26,3546', 0o54345, 'NEWANGLE', 'DLOAD', 'SR', 'ENTER PD 12D', kind='interp', line=258)
W('26,3547', 0o00007, '', '', '6D', kind='operand', line=259)
W('26,3550', 0o20617, '', '', '14D', kind='operand', line=260)
W('26,3551', 0o72371, '', 'TAD', 'TLOAD', 'CHANGE MODE TO TP', kind='interp', line=261)
W('26,3552', 0o01707, '', '', 'TIMSUBO', kind='operand', line=262)
W('26,3553', 0o00155, '', '', 'MPAC', kind='operand', line=263)
W('26,3554', 0o14017, '', 'STODL', 'TIMSUBM', 'T+T0 CSEC B-42', kind='interp', line=264)
W('26,3555', 0o00020, '', '', 'TIMSUBM +1', kind='operand', line=265)
W('26,3556', 0o77605, '', 'DMP', '', 'PD 10D        MULT BY XDOT IN 10-11D', kind='interp', line=266)
W('26,3557', 0o43257, '', 'SL*', 'DAD', 'PD 8D         ADD X0 IN 8-9D AFTER SHIFTING', kind='interp', line=267)
W('26,3560', 0o20206, '', '', '5,1', '              SUCH THAT SCALING IS B-0', kind='operand', line=268)
W('26,3561', 0o67206, '', 'PUSH', 'SLOAD', 'PD 10D  SAVE PARTIAL (X0+XDOT*T) IN 8-9D', kind='interp', line=269)
W('26,3562', 0o00017, '', '', 'TIMSUBM', kind='operand', line=270)
W('26,3563', 0o41261, '', 'SL', 'DMP', kind='interp', line=271)
W('26,3564', 0o20212, '', '', '9D', kind='operand', line=272)
W('26,3565', 0o00013, '', '', '10D', 'XDOT', kind='operand', line=273)
W('26,3566', 0o43257, '', 'SL*', 'DAD', 'PD 8D         SHIFT SUCH THAT THIS PART OF X', kind='interp', line=274)
W('26,3567', 0o20213, '', '', '10D,1', '              IS SCALED REVS/CSEC B-0', kind='operand', line=275)
W('26,3570', 0o77600, '', 'BOV', '', 'TURN OFF OVERFLOW IF SET BY SHIFT', kind='interp', line=276)
W('26,3571', 0o55572, '', '', '+1', 'INSTRUCTION BEFORE EXITING', kind='operand', line=277)
W('26,3572', 0o77616, '', 'RVQ', '', 'MPAC=X= X0+(XDOT)(T+T0)       REVS B0', kind='interp', line=278)

# Page 1249
# ..... EARTHMX SUBROUTINE .....
# SUBROUTINE TO COMPUTE THE TRANSFORMATION MATRIX M FOR THE EARTH

# CALLING SEQUENCE
# L       CALL
# L+1             EARTHMX

# SUBROUTINE USED
# NEWANGLE

# INPUT
# INPUT AVAILABLE FROM LAUNCH DATA        AZO REVS B-0
# TEPHEM CSEC B-42
# 6-7D= TIME CSEC B-28

# OUTPUT
# MMATRIX= 3X3 M MATRIX B-1 (STORED IN VAC AREA)

W('26,3573', 0o40220, 'EARTHMX', 'STQ', 'SETPD', 'SET 8-9D=AZO', kind='interp', line=299)
W('26,3574', 0o00051, '', '', 'EARTHMXX', kind='operand', line=300)
W('26,3575', 0o00011, '', '', '8D', '10-11D=WEARTH', kind='operand', line=301)
W('26,3576', 0o77770, '', 'AXT,1', '', 'FOR SL 5, AND SL 10 IN NEWANGLE', kind='interp', line=302)
W('26,3577', 0o00000, '', '', '0', kind='operand', line=303)
W('26,3600', 0o65345, '', 'DLOAD', 'PDDL', 'LEAVING PD SET AT 12D FOR NEWANGLE', kind='interp', line=304)
W('26,3601', 0o01712, '', '', 'AZO', kind='operand', line=305)
W('26,3602', 0o15657, '', '', 'WEARTH', kind='operand', line=306)
W('26,3603', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=307)
W('26,3604', 0o55546, '', '', 'NEWANGLE', kind='operand', line=308)
W('26,3605', 0o41401, '', 'SETPD', 'PUSH', '18-19D=504AZ', kind='interp', line=309)
W('26,3606', 0o00023, '', '', '18D', '                       COS(AZ) SIN(AZ) 0', kind='operand', line=310)
W('26,3607', 0o65346, '', 'COS', 'PDDL', '20-37D=  MMATRIX=     -SIN(AZ) COS(AZ) 0 B-1', kind='interp', line=311)
W('26,3610', 0o00023, '', '', '504AZ', '                        0       0      1', kind='operand', line=312)
W('26,3611', 0o65356, '', 'SIN', 'PDDL', kind='interp', line=313)
W('26,3612', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=314)
W('26,3613', 0o73525, '', 'PDDL', 'SIN', kind='interp', line=315)
W('26,3614', 0o00023, '', '', '504AZ', kind='operand', line=316)
W('26,3615', 0o65276, '', 'DCOMP', 'PDDL', kind='interp', line=317)
W('26,3616', 0o00023, '', '', '504AZ', kind='operand', line=318)
W('26,3617', 0o63346, '', 'COS', 'PDVL', kind='interp', line=319)
W('26,3620', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=320)
W('26,3621', 0o41525, '', 'PDDL', 'PUSH', kind='interp', line=321)
W('26,3622', 0o15333, '', '', 'HIDPHALF', kind='operand', line=322)
W('26,3623', 0o77650, '', 'GOTO', kind='interp', line=323)
W('26,3624', 0o00051, '', '', 'EARTHMXX', kind='operand', line=324)

# Page 1250
# ..... EARTHL SUBROUTINE .....
# SUBROUTINE TO COMPUTE L VECTOR FOR EARTH

# CALLING SEQUENCE
# L       CALL
# L+1             EARTHL

# INPUT
# AXO,AYO SET AT LAUNCH TIME WITH AYO IMMEDIATELY FOLLOWING AXO IN CORE

# OUTPUT
# -AX
# MPAC=   -AY     RADIANS B-0
# 0

W('26,3625', 0o57545, 'EARTHL', 'DLOAD', 'DCOMP', kind='interp', line=342)
W('26,3626', 0o01716, '', '', 'AXO', kind='operand', line=343)
W('26,3627', 0o14017, '', 'STODL', '504LPL', kind='interp', line=344)
W('26,3630', 0o01714, '', '', '-AYO', kind='operand', line=345)
W('26,3631', 0o14021, '', 'STODL', '504LPL +2', kind='interp', line=346)
W('26,3632', 0o15335, '', '', 'HI6ZEROS', kind='operand', line=347)
W('26,3633', 0o24023, '', 'STOVL', '504LPL +4', kind='interp', line=348)
W('26,3634', 0o00017, '', '', '504LPL', kind='operand', line=349)
W('26,3635', 0o77616, '', 'RVQ', kind='interp', line=350)

# Page 1251
# CONSTANTS AND ERASABLE ASSIGNMENTS
S('1B1', 'equals', 0o21563, line=354)  # 1 SCALED B-1
W('26,3636', 0o17775, 'COSI', '2DEC', '.99964173 B-1', 'COS(5521.5 SEC) B-1', kind='data', line=355)
W('26,3637', 0o02052, kind='data', line=355)

W('26,3640', 0o00333, 'SINI', '2DEC', '.02676579 B-1', 'SIN(5521.5 SEC) B-1', kind='data', line=357)
W('26,3641', 0o10374, kind='data', line=357)

S('RPREXIT', 'equals', 0o50, line=359)  # R-TO-RP AND RP-TO-R SUBR EXIT
S('EARTHMXX', 'equals', 0o51, line=360)  # EARTHMX,MOONMX SUBR. EXITS
S('504RPR', 'equals', 0o0, line=361)  # 6 REGS        R OR RP VECTOR
S('SINNODI', 'equals', 0o10, line=362)  # 2             SIN(NODI)
S('DVECTR', 'equals', 0o10, line=363)  # 6             D VECTOR MOON
S('CVECTR', 'equals', 0o10, line=364)  # 6             C VECTR MOON
S('504AZ', 'equals', 0o22, line=365)  # 2            AZ
S('TIMSUBM', 'equals', 0o16, line=366)  # 3             TIME SUB M (MOON) T+10 IN GETAZ
S('504LPL', 'equals', 0o16, line=367)  # 6             L OR LP VECTOR
S('AVECTR', 'equals', 0o24, line=368)  # 6             A VECTOR (MOON)
S('BVECTR', 'equals', 0o32, line=369)  # 6             B VECTOR (MOON)
S('MMATRIX', 'equals', 0o24, line=370)  # 18            M MATRIX
S('COB', 'equals', 0o40, line=371)  # 2             COS(B) B-1
S('SOB', 'equals', 0o42, line=372)  # 2             SIN(B) B-1
S('504F', 'equals', 0o6, line=373)  # 2             F(MOON)
W('26,3642', 0o77665, 'NODDOT', '2DEC', '-.457335121 E-2', 'REVS/CSEC B+28=-1.07047011 E-8  RAD/SEC', kind='data', line=374)
W('26,3643', 0o42175, kind='data', line=374)

W('26,3644', 0o22211, 'FDOT', '2DEC', '.570863327', 'REVS/CSEC B+27= 2.67240410 E-6  RAD/SEC', kind='data', line=376)
W('26,3645', 0o00625, kind='data', line=376)

W('26,3646', 0o77777, 'BDOT', '2DEC', '-3.07500686 E-8', 'REVS/CSEC B+28=-7.19757301 E-14 RAD/SEC', kind='data', line=378)
W('26,3647', 0o77767, kind='data', line=378)

W('26,3650', 0o37436, 'NODIO', '2DEC', '.986209434', 'REVS B-0      = 6.19653663041   RAD', kind='data', line=380)
W('26,3651', 0o01613, kind='data', line=380)

W('26,3652', 0o32417, 'FSUBO', '2DEC', '.829090536', 'REVS B-0      = 5.20932947829   RAD', kind='data', line=382)
W('26,3653', 0o32160, kind='data', line=382)

W('26,3654', 0o02052, 'BSUBO', '2DEC', '.0651201393', 'REVS B=0      = 0.40916190299   RAD', kind='data', line=384)
W('26,3655', 0o35552, kind='data', line=384)

W('26,3656', 0o37116, 'WEARTH', '2DEC', '.973561595', 'REVS/CSEC B+23= 7.29211494 E-5  RAD/SEC', kind='data', line=386)
W('26,3657', 0o32523, kind='data', line=386)
