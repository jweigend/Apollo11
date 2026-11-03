"""ATTITUDE_MANEUVER_ROUTINE.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/ATTITUDE_MANEUVER_ROUTINE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 342-363 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('ATTITUDE_MANEUVER_ROUTINE', 'ATTITUDE_MANEUVER_ROUTINE.agc', 'Luminary099', pages='342-363')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     ATTITUDE_MANEUVER_ROUTINE.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        342-363
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

# Page 342
# BLOCK 2 LGC ATTITUDE MANEUVER ROUTINE -- KALCMANU
#
# MOD 2         DATE 5/1/67     BY DON KEENE
#
# PROGRAM DESCRIPTION
#
# KALCMANU IS A ROUTINE WHICH GENERATES COMMANDS FOR THE LM DAP TO CHANGE THE ATTITUDE OF THE SPACECRAFT
# DURING FREE FALL.  IT IS DESIGNED TO MANEUVER THE SPACECRAFT FROM ITS INITIAL ORIENTATION TO SOME DESIRED
# ORIENTATION SPECIFIED BY THE PROGRAM WHICH CALLS KALCMANU, AVOIDING GIMBAL LOCK IN THE PROCESS.  IN THE
# MOD 2 VERSION, THIS DESIRED ATTITUDE IS SPECIFIED BY A SET OF OF THREE COMMANDED CDU ANGLES STORES AS 2'S COMPLEMENT
# SINGLE PRECISION ANGLES IN THE THREE CONSECUTIVE LOCATIONS, CPHI, CTHETA, CPSI, WHERE
#
# CPHI = COMMANDED OUTER GIMBAL ANGLE
# CTHETA = COMMANDED INNER GIMBAL ANGLE
# CPSI = COMMANDED MIDDLE GIMBAL ANGLE
#
# WHEN POINTING A SPACECRAFT AXIS (I.E., X, Y, Z, THE AOT, THRUST AXIS, ETC.) THE SUBROUTINE VECPOINT MAY BE
# USED TO GENERATE THIS SET OF DESIRED CDU ANGLES (SEE DESCRIPTION IN R60).
#
# WITH THIS INFORMATION KALCMANU DETERMINES THE DIRECTION OF THE SINGLE EQUIVALENT ROTATION (COF ALSO U) AND THE
# MAGNITUDE OF THE ROTATION (AM) TO BRING THE S/C FROM ITS INITIAL ORIENTATION TO ITS FINAL ORIENTATION.
# THIS DIRECTION REMAINS FIXED BOTH IN INERTIAL COORDINATES AND IN COMMANDED S/C AXES THROUGHOUT THE
# _
# MANEUVER.  ONCE COF AND AM HAVE BEEN DETERMINED, KALCMANU THEN EXAMINES THE MANEUVER TO SEE IF IT WILL BRING
# _
# THE S/C THROUGH GIMBAL LOCK.  IF SO, COF AND AM ARE READJUSTED SO THAT THE S/C WILL JUST SKIM THE GIMBAL
# LOCK ZONE AND ALIGN THE X-AXIS.  IN GENERAL A FINAL YAW ABOUT X WILL BE NECESSARY TO COMPLETE THE MANEUVER.
# NEEDLESS TO SAY, NEITHER THE INITIAL NOR THE FINAL ORIENTATION CAN BE IN GIMBAL LOCK.
#
# FOR PROPER ATTITUDE CONTROL THE DIGITAL AUTOPILOT MUST BE GIVEN AN ATTITUDE REFERENCE WHICH IT CAN TRACK.
# KALCMANU DOES THIS BY GENERATING A REFERENCE OF DESIRED GIMBAL ANGLES (CDUXD, CDUYD, CDUZD) WHICH ARE UPDATED
# EVERY ONE SECOND DURING THE MANEUVER.  TO ACHIEVE A SMOOTHER SEQUENCE OF COMMANDS BETWEEN SUCCESSIVE UPDATES,
# THE PROGRAM ALSO GENERATES A SET OF INCREMENTAL CDU ANGLES (DELDCDU) TO BE ADDED TO CDU DESIRED BY THE DIGITAL
# AUTOPILOT.  KALCMANU ALSO CALCULATES THE COMPONENT MANEUVER RATES (OMEGAPD, OMEGAQD, OMEGARD), WHICH CAN
# _
# BE DETERMINED SIMPLY BY MULTIPLYING COF BY SOME SCALAR (ARATE) CORRESPONDING TO THE DESIRED ROTATIONAL RATE.
#
# AUTOMATIC MANEUVERS ARE TIMED WTH THE HELP OF WAITLIST SO THAT AFTER A SPECIFIED INTERVAL THE Y AND Z
# DESIRED RATES ARE SET TO ZERO AND THE DESIRED CDU ANGLES (CDUYD, CDUZD) ARE SET EQUAL TO THE FINAL DESIRED CDU
# ANGLES (CTHETA, CPSI).  IF ANY YAW REMAINS DUE TO GIMBAL LOCK AVOIDANCE, THE FINAL YAW MANEUVER IS
# CALCULATED AND THE DESIRED YAW RATE SET TO SOME FIXED VALUE (ROLLRATE = + OR - 2 DEGREES PER SEC).
# IN THIS CASE ONLY AN INCREMENTAL CDUX ANGLE (DELFROLL) IS SUPPLIED TO THE DAP.  AT THE END OF THE YAW
# MANEUVER OR IN THE EVENT THAT THERE WAS NO FINAL YAW, CDUXD IS SET EQUAL TO CPHI AND THE X-AXIS DESIRED
# RATE SET TO ZERO.  THUS, UPON COMPLETION OF THE MANEUVER THE S/C WILL FINISH UP IN A LIMIT CYCLE ABOUT THE
# DESIRED GIMBAL ANGLES.
#
# PROGRAM LOGIC FLOW
#
# KALCMANU IS CALLED AS A HIGH PRIORITY JOB WITH ENTRY POINTS AT KALCMAN3 AND VECPOINT.  IT FIRST PICKS
# UP THE CURRENT CDU ANGLES TO BE USED AS THE BASIS FOR ALL COMPUTATIONS INVOLVING THE INITIAL S/C ORIENTATION.
# Page 343
# IT THEN DETERMINES THE DIRECTION COSINE MATRICES RELATING BOTH THE INITIAL AND FINAL S/C ORIENTATION TO STABLE
# *   *                                                                               *
# MEMBER AXES (MIS,MFS).  IT ALSO COMPUTES THE MATRIX RELATING FINAL S/C AXES TO INITIAL S/C AXES (MFI).  THE
# ANGLE OF ROTATION (AM) IS THEN EXTRACTED FROM THIS MATRIX, AND TEST ARE MADE TO DETERMINE IF
#
# A)      AM LESS THAN .25 DEGREES (MINANG)
# B)      AM GREATER THAN 170 DEGREES (MAXANG)
#
# IF AM IS LESS THAN .25 DEGREES, NO COMPLICATED AUTOMATIC MANEUVERING IS NECESSARY.  THEREFORE, WE CAN SIMPLY
# SET CDU DESIRED EQUAL TO THE FINAL CDU DESIRED ANGLES AND TERMINATE THE JOB.
#
# IF AM IS GREATER THAN .25 DEGREES BUT LESS THAN 170 DEGREES THE AXES OF THE SINGLE EQUIVALENT ROTATION
# _                                                       *
# (COF) IS EXTRACTED FROM THE SKEW SYMMETRIC COMPONENTS OF MFI.
# *     *
# IF AM GREATER THAN 170 DEGREES AN ALTERNATE METHOD EMPLOYING THE SYMMETRIC PART OF MFI (MFISYM) IS USED
# _
# TO DETERMINE COF.
#
# THE PROGRAM THEN CHECKS TO SEE IF THE MANEUVER AS COMPUTED WILL BRING THE S/C THROUGH GIMBAL LOCK.  IF
# SO, A NEW MANEUVER IS CALCULATED WHICH WILL JUST SKIM THE GIMBAL LOCK ZONE AND ALIGN THE S/C X-AXIS.  THIS
# METHOD ASSURES THAT THE ADDITIONAL MANEUVERING TO AVOID GIMBAL LOCK WILL BE KEPT TO A MINIMUM.  SINCE A FINAL
# P AXIS YAW WILL BE NECESSARY, A SWITCH IS RESET (STATE SWITCH 31) TO ALLOW FOR THE COMPUTATION OF THIS FINAL
# YAW.
#
# AS STATED PREVIOUSLY, KALCMANU GENERATES A SEQUENCE OF DESIRED GIMBAL ANGLES WHICH ARE UPDATED EVERY
# _
# SECOND.  THIS IS ACCOMPLISHED BY A SMALL ROTATION OF THE DESIRED S/C FRAME ABOUT THE VECTOR COF.  THE NEW
# DESIRED REFERENCE MATRIX IS THEN,
# *               *       *
# MIS     =       MIS     DEL
# N+1             N
# *
# WHERE DEL IS THE MATRIX CORRESPONDING TO THIS SMALL ROTATION.  THE NEW CDU ANGLES CAN THEN BE EXTRACTED
# *
# FROM MIS.
#
# AT THE BEGINNING OF THE MANEUVER THE AUTOPILOT DESIRED RATES (OMEGAPD, OMEGAQD, OMEGARD) AND THE
# MANEUVER TIMINGS ARE ESTABLISHED.  ON THE FIRST PASS AND ON ALL SUBSEQUENT UPDATES THE CDU DESIRED
# ANGLES ARE LOADED WITH THE APPROPRIATE VALUES AND THE INCREMENTAL CDU ANGLES ARE COMPUTED.  THE AGC CLOCKS
# (TIME1 AND TIME2) ARE THEN CHECKED TO SEE IF THE MANEUVER WILL TERMINATE BEFORE THE NEXT UPDATE.  IF
# NOT, KALCMANU CALLS FOR ANOTHER UPDATE (RUN AS A JOB WITH PRIORITY TBD) IN ONE SECOND.  ANY DELAYS IN THIS
# CALLING SEQUENCE ARE AUTOMATICALLY COMPENSATED IN CALLING FOR THE NEXT UPDATE.
#
# IF IT IS FOUND THAT THE MANEUVER IS TO TERMINATE BEFORE THE NEXT UPDATE A ROUTINE IS CALLED (AS A WAIT-
# LIST TASK) TO STOP THE MANEUVER AT THE APPROPRIATE TIME AS EXPLAINED ABOVE.

# Page 344
# CALLING SEQUENCE
#
# IN ORDER TO PERFORM A KALCMANU SUPERVISED MANEUVER, THE COMMANDED GIMBAL ANGLES MUST BE PRECOMPUTED AND
# STORED IN LOCATIONS CPHI, CTHETA, CPSI.  THE USER'S PROGRAM MUST THEN CLEAR STATE SWITCH NO 33 TO ALLOW THE
# ATTITUDE MANEUVER ROUTINE TO PERFORM ANY FINAL P-AXIS YAW INCURRED BY AVOIDING GIMBAL LOCK.  THE MANEUVER IS
# THEN INITIATED BY ESTABLISHING THE FOLLOWING EXECUTIVE JOB
# *
# CAF     PRIO XX
# --
# INHINT
# TC      FINDVAC
# 2CADR   KALCMAN3
# RELINT
#
# THE USER'S PROGRAM MAY EITHER CONTINUE OR WAIT FOR THE TERMINATION OF THE MANEUVER.  IF THE USER WISHES TO
# WAIT, HE MAY PUT HIS JOB TO SLEEP WITH THE FOLLOWING INSTRUCTIONS:
#
# L       TC      BANKCALL
# L+1     CADR    ATTSTALL
# L+2     (BAD RETURN)
# L+3     (GOOD RETURN)
#
# UPON COMPLETION OF THE MANEUVER, THE PROGRAM WILL BE AWAKENED AT L+3 IF THE MANEUVER WAS COMPLETED
# SUCCESSFULLY, OR AT L+2 IF THE MANEUVER WAS ABORTED.  THIS ABORT WOULD OCCUR IF THE INITIAL OR FINAL ATTITUDE
# WAS IN GIMBAL LOCK.
#
# *** NOTA BENE ***  IF IT IS ASSUMED THAT THE DESIRED MANEUVERING RATE (0.5, 2, 5, 10 DEG/SEC) HAS BEEN SELECTED BY
# KEYBOARD ENTRY PRIOR TO THE EXECUTION OF KALCMANU.
#
# IT IS ALSO ASSUMED THAT THE AUTOPILOT IS IN THE AUTO MODE.  IF THE MODE SWITCH IS CHANGED DURING THE
# MANEUVER, KALCMANU WILL TERMINATE VIA GOODEND WITHIN 1 SECOND SO THAT R60 MAY REQUEST A TRIM OF THE S/C ATTITUDE
# SUBROUTINES.
#
# KALCMANU USES A NUMBER OF INTERPRETIVE SUBROUTINES WHICH MAY BE OF GENERAL INTEREST.  SINCE THESE ROUTINES
# WERE PROGRAMMED EXCLUSIVELY FOR KALCMANU, THEY ARE NOT, AS YET, GENERALLY AVAILABLE FOR USE BY OTHER PROGRAMS.
#
# MXM3
# ----
#
# THIS SUBROUTINE MULTIPLIES TWO 3X3 MATRICES AND LEAVES THE RESULT IN THE FIRST 18 LOCATIONS OF THE PUSH
# DOWN LIST, I.E.,
# [ M     M     M  ]
# [  0     1     2 ]
# *               [                ]              *               *
# M       =       [ M     M     M  ]      =       M1      X       M2
# [  3     4     5 ]
# [                ]
# [ M     M     M  ]
# [  6     7     8 ]
# Page 345
# *
# INDEX REGISTER X1 MUST BE LOADED WITH THE COMPLEMENT OF THE STARTING ADDRESS FOR M1, AND X2 MUST BE
# *
# LOADED WITH THE COMPLEMENT OF THE STARTING ADDRESS FOR M2.  THE ROUTINE USES THE FIRST 20 LOCATIONS OF THE PUSH
# DOWN LIST.  THE FIRST ELEMENT OF THE MATRIX APPEARS IN PDO.  PUSH UP FOR M .
# 8
# TRANSPOS
# --------
#
# THIS ROUTINE TRANSPOSES A 3X3 MATRIX AND LEAVES THE RESULT IN THE PUSH DOWN LIST, I.E.,
#
# *               * T
# M       =       M1
#
# INDEX REGISTER X1 MUST CONTAIN THE COMPLEMENT OF THE STARTING ADDRESS FOR M1.  PUSH UP FOR THE FIRST AND SUB-
# *
# SEQUENT COMPONENTS OF M.  THIS SUBROUTINE ALSO USES THE FIRST 20 LOCATIONS OF THE PUSH DOWN LIST.
#
# CDU TO DCM
# ----------
#
# THIS SUBROUTINE CONVERTS THREE CDU ANGLES IN T(MPAC) TO A DIRECTION COSINE MATRIX (SCALED BY 2) RELATING
# THE CORRESPONDING S/C ORIENTATIONS TO THE STABLE MEMBER FRAME.  THE FORMULAS FOR THIS CONVERSION ARE
#
# M       =       COSY COSZ
# 0
#
# M       =       -COSY SINZ COSX + SINY SINX
# 1
#
# M       =       COSY SINZ SINX + SINY COSX
# 2
#
# M       =       SINZ
# 3
#
# M       =       COSZ COSX
# 4
#
# M       =       -COSZ SINX
# 5
#
# M       =       -SINY COSZ
# 6
#
# M       =       SINY SINZ COSX + COSY SINX
# 7
# Page 346
# M       =       -SINY SINZ SINX + COSY COSX
# 8
#
# WHERE         X       =       OUTER GIMBAL ANGLE
# Y       =       INNER GIMBAL ANGLE
# Z       =       MIDDLE GIMBAL ANGLE
#
# THE INTERPRETATION OF THIS MATRIX IS AS FOLLOWS:
#
# IF A , A , A  REPRESENT THE COMPONENTS OF A VECTOR IN S/C AXES THEN THE COMPONENTS OF THE SAME VECTOR IN
# X   Y   Z
# STABLE MEMBER AXES (B , B , B ) ARE
# X   Y   Z
#
# [ B  ]                  [ A  ]
# [  X ]                  [  X ]
# [    ]                  [    ]
# [ B  ]            *     [ A  ]
# [  Y ]     =      M     [  Y ]
# [    ]                  [    ]
# [ B  ]                  [ B  ]
# [  Z ]                  [  Z ]
#
# THE SUBROUTINE WILL STORE THIS MATRIX IN SEQUENTIAL LOCATIONS OF ERASABLE MEMORY AS SPECIFIED BY THE CALLING
# *
# PROGRAM.  TO DO THIS THE CALLING PROGRAM MUST FIRST LOAD X2 WITH THE COMPLEMENT OF THE STARTING ADDRESS FOR M.
#
# INTERNALLY, THE ROUTINE USES THE FIRST 16 LOCATIONS OF THE PUSH DOWN LIST, ALSO STEP REGISTER S1 AND INDEX
# REGISTER X2.
#
# DCM TO CDU
# ----------
# *
# THIS ROUTINE EXTRACTS THE CDU ANGLES FROM A DIRECTION COSINE MATRIX (M SCALED BY 2) RELATING S/C AXIS TO
# *
# STABLE MEMBER AXES.  X1 MUST CONTAIN THE COMPLEMENT OF THE STARTING ADDRESS FOR M.  THE SUBROUTINE LEAVES THE
# CORRESPONDING GIMBAL ANGLES IN V(MPAC) AS DOUBLE PRECISION 1'S COMPLEMENT ANGLES SCALED BY 2PI.  THE FORMULAS
# FOR THIS CONVERSION ARE
#
# Z       =       ARCSIN (M  )
# 3
#
# Y       =       ARCSIN (-M /COSZ)
# 6
#
# IF M  IS NEGATIVE, Y IS REPLACED BY PI SGN Y - Y.
# 0
# Page 347
# X       =       ARCSIN (-M /COSZ)
# 5
#
# IF M  IS NEGATIVE, X IS REPLACED BY PI SGN X - X.
# 4
#
# THIS ROUTINE DOES NOT SET THE PUSH DOWN POINTER, BUT USES THE NEXT 8 LOCATIONS OF THE PUSH DOWN LIST AND
# RETURNS THE POINTER TO ITS ORIGINAL SETTING.  THIS PROCEDURE ALLOWS THE CALLER TO STORE THE MATRIX AT THE TOP OF
# THE PUSH DOWN LIST.
#
# DELCOMP
# -------
# *
# THIS ROUTINE COMPUTES THE DIRECTION COSINE MATRIX (DEL) RELATING ON
# _
# IS ROTATED WITH RESPECT TO THE FIRST BY AN ANGLE, A, ABOUT A UNIT VECTOR U.  THE FORMULA FOR THIS MATRIX IS
#
# *              *        _ _T              *
# DEL     =       I COSA + U U  (1 - COSA) + V  SINA
# X
#
# WHERE         *               [ 1    0    0 ]
# I       =       [ 0    1    0 ]
# [ 0    0    1 ]
#
# [    2                             ]
# [  U           U  U          U  U  ]
# [   X           X  Y          X  Z ]
# [                                  ]
# _ _T            [                 2                ]
# U U     =       [ U  U          U            U  U  ]
# [  Y  X          Y            Y  Z ]
# [                                  ]
# [                               2  ]
# [ U  U         U  U           U    ]
# [  Z  X         Z  Y           Z   ]
#
#
# [   0           -U               U  ]
# [                 Z               Y ]
# *               [                                   ]
# V       =       [  U             0              -U  ]
# X              [   Z                             X ]
# [                                   ]
# [ -U             U               0  ]
# [   Y             X                 ]
#
# Page 348
# _
# U       =       UNIT ROTATION VECTOR RESOLVED INTO S/C AXES.
# A       =       ROTATION ANGLE
#
# *
# THE INTERPRETATION OF DEL IS AS FOLLOWS:
#
# IF A , A , A  REPRESENT THE COMPONENTS OF A VECTOR IN THE ROTATED FRAME, THEN THE COMPONENTS OF THE SAME
# X   Y   Z
# VECTOR IN THE ORIGINAL S/C AXES (B , B , B ) ARE
# X   Y   Z
#
# [ B  ]                  [ A  ]
# [  X ]                  [  X ]
# [    ]                  [    ]
# [ B  ]            *     [ A  ]
# [  Y ]     =     DEL    [  Y ]
# [    ]                  [    ]
# [ B  ]                  [ B  ]
# [  Z ]                  [  Z ]
#
# THE ROUTINE WILL STORE THIS MATRIX (SCALED UNITY) IN SEQUENTIAL LOCATIONS OF ERASABLE MEMORY BEGINNING WITH
# _
# THE LOCATION CALLED DEL.  IN ORDER TO USE THE ROUTINE, THE CALLING PROGRAM MUST FIRST STORE U (A HALF UNIT
# DOUBLE PRECISION VECTOR) IN THE SET OF ERASABLE LOCATIONS BEGINNING WITH THE ADDRESS CALLED COF.  THE ANGLE, A,
# MUST THEN BE LOADED INTO D(MPAC).
#
# INTERNALLY, THE PROGRAM ALSO USES THE FIRST 10 LOCATIONS OF THE PUSH DOWN LIST.
#
# READCDUK
# --------
#
# THIS BASIC LANGUAGE SUBROUTINE LOADS T(MPAC) WITH THE THREE CDU ANGLES.
#
# SIGNMPAC
# --------
#
# THIS IS A BASIC LANGUAGE SUBROUTINE WHICH LIMITS THE MAGNITUDE OF D(MPAC) TO + OR - DPOSMAX ON OVERFLOW.
#
# PROGRAM STORAGE ALLOCATION
#
# 1)      FIXED MEMORY            1059 WORDS
# 2)      ERASABLE MEMORY           98
# 3)      STATE SWITCHES             3
# Page 349
# 4)      FLAGS                      1
#
# JOB PRIORITIES
#
# 1)      KALCMANU                TBD
# 2)      ONE SECOND UPDATE       TBD
#
# SUMMARY OF STATE SWITCHES AND FLAGWORDS USED BY KALCMANU.
#
# STATE           FLAGWRD 2       SETTING         MEANING
# SWITCH NO.      BIT NO.
#
# *
# 31              14              0               MANEUVER WENT THROUGH GIMBAL LOCK
# 1               MANEUVER DID NOT GO THROUGH GIMBAL LOCK
# *
# 32              13              0               CONTINUE UPDATE PROCESS
# 1               START UPDATE PROCESS
#
# 33              12              0               PERFORM FINAL P AXIS YAW IF REQUIRED
# 1               IGNORE ANY FINAL P-AXIS YAW
#
# 34              11              0               SIGNAL END OF KALCMANU
# 1               KALCMANU IN PROCESS.    USER MUST SET SWITCH BEFORE INITIATING
#
# * INTERNAL TO KALCMANU
#
# SUGGESTIONS FOR PROGRAM INTEGRATION
#
# THE FOLLOWING VARIABLES SHOULD BE ASSIGNED TO UNSWITCH ERASABLE:
#
# CPHI
# CTHETA
# CPSI
# POINTVSM +5
# SCAXIS   +5
# DELDCDU
# DELDCDU1
# DELDCDU2
# RATEINDX
#
# THE FOLLOWING SUBROUTINES MAY BE PUT IN A DIFFERENT BANK
#
# MXM3
# Page 350
# TRANSPGS
# SIGNMPAC
# READCDUK
# CDUTODCM

# Page 351
#   BANK 15
#   SETLOC KALCMON1
#   BANK

#   EBANK= BCDU

# THE THREE DESIRED CDU ANGLES MUST BE STORED AS SINGLE PRECISION TWO'S COMPLEMENT ANGLES IN THE THREE SUCCESSIVE
# LOCATIONS, CPHI, CTHETA, CPSI.

#   COUNT* $$/KALC
W('22,2004', 0o06037, 'KALCMAN3', 'TC', 'INTPRET', 'PICK UP THE CURRENT CDU ANGLES AND', line=429)
W('22,2005', 0o77634, '', 'RTB', '', '      COMPUTE THE MATRIX FROM INITIAL S/C', kind='interp', line=430)
W('22,2006', 0o44403, '', '', 'READCDUK', '      AXES TO FINAL S/C AXES.', kind='operand', line=431)
W('22,2007', 0o03277, '', 'STORE', 'BCDU', 'STORE INITIAL S/C ANGLES', kind='interp', line=432)
W('22,2010', 0o51535, '', 'SLOAD', 'ABS', 'CHECK THE MAGNITUDE OF THE DESIRED', kind='interp', line=433)
W('22,2011', 0o00324, '', '', 'CPSI', 'MIDDLE GIMBAL ANGLE', kind='operand', line=434)
W('22,2012', 0o51025, '', 'DSU', 'BPL', kind='interp', line=435)
W('22,2013', 0o04403, '', '', 'LOCKANGL', 'IF GREATER THAN 70 DEG ABORT MANEUVER', kind='operand', line=436)
W('22,2014', 0o44724, '', '', 'TOOBADF', kind='operand', line=437)
W('22,2015', 0o72364, '', 'AXC,2', 'TLOAD', kind='interp', line=438)
W('22,2016', 0o03246, '', '', 'MIS', kind='operand', line=439)
W('22,2017', 0o03277, '', '', 'BCDU', kind='operand', line=440)
W('22,2020', 0o77624, '', 'CALL', '', 'COMPUTE THE TRANSFORMATION FROM INITIAL', kind='interp', line=441)
W('22,2021', 0o44410, '', '', 'CDUTODCM', 'S/C AXES TO STABLE MEMBER AXES', kind='operand', line=442)
W('22,2022', 0o72364, '', 'AXC,2', 'TLOAD', kind='interp', line=443)
W('22,2023', 0o02230, '', '', 'MFS', 'PREPARE TO CALCULATE ARRAY MFS', kind='operand', line=444)
W('22,2024', 0o00322, '', '', 'CPHI', kind='operand', line=445)
W('22,2025', 0o77624, '', 'CALL', kind='interp', line=446)
W('22,2026', 0o44410, '', '', 'CDUTODCM', kind='operand', line=447)
W('22,2027', 0o45160, 'SECAD', 'AXC,1', 'CALL', 'MIS AND MFS ARRAYS CALCULATED         $2', kind='interp', line=448)
W('22,2030', 0o03246, '', '', 'MIS', kind='operand', line=449)
W('22,2031', 0o44326, '', '', 'TRANSPOS', kind='operand', line=450)
W('22,2032', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=451)
W('22,2033', 0o50457, '', 'STOVL', 'TMIS +12D', kind='interp', line=452)
W('22,2034', 0o77626, '', 'STADR', kind='interp', line=453)
W('22,2035', 0o50465, '', 'STOVL', 'TMIS +6', kind='interp', line=454)
W('22,2036', 0o77626, '', 'STADR', kind='interp', line=455)
W('22,2037', 0o74473, '', 'STORE', 'TMIS', 'TMIS = TRANSPOSE(MIS) SCALED BY 2', kind='interp', line=456)
W('22,2040', 0o75160, '', 'AXC,1', 'AXC,2', kind='interp', line=457)
W('22,2041', 0o03303, '', '', 'TMIS', kind='operand', line=458)
W('22,2042', 0o02230, '', '', 'MFS', kind='operand', line=459)
W('22,2043', 0o77624, '', 'CALL', kind='interp', line=460)
W('22,2044', 0o44312, '', '', 'MXM3', kind='operand', line=461)
W('22,2045', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=462)
W('22,2046', 0o51532, '', 'STOVL', 'MFI +12D', kind='interp', line=463)
W('22,2047', 0o77626, '', 'STADR', kind='interp', line=464)
W('22,2050', 0o51540, '', 'STOVL', 'MFI +6', kind='interp', line=465)
W('22,2051', 0o77626, '', 'STADR', kind='interp', line=466)
W('22,2052', 0o75546, '', 'STORE', 'MFI', 'MFI = TMIS MFS (SCALED BY 4)', kind='interp', line=467)
W('22,2053', 0o45001, '', 'SETPD', 'CALL', 'TRANSPOSE MFI IN PD LIST', kind='interp', line=468)
# Page 352
W('22,2054', 0o00023, '', '', '18D', kind='operand', line=470)
W('22,2055', 0o44335, '', '', 'TRNSPSPD', kind='operand', line=471)
W('22,2056', 0o45575, '', 'VLOAD', 'STADR', kind='interp', line=472)
W('22,2057', 0o50457, '', 'STOVL', 'TMFI +12D', kind='interp', line=473)
W('22,2060', 0o77626, '', 'STADR', kind='interp', line=474)
W('22,2061', 0o50465, '', 'STOVL', 'TMFI +6', kind='interp', line=475)
W('22,2062', 0o77626, '', 'STADR', kind='interp', line=476)
W('22,2063', 0o74473, '', 'STORE', 'TMFI', 'TMFI = TRANSPOSE (MFI) SCALED BY 4', kind='interp', line=477)

# CALCULATE COFSKEW AND MFISYM

W('22,2064', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=481)
W('22,2065', 0o03306, '', '', 'TMFI +2', kind='operand', line=482)
W('22,2066', 0o02233, '', '', 'MFI +2', kind='operand', line=483)
W('22,2067', 0o45325, '', 'PDDL', 'DSU', 'CALCULATE COF SCALED BY 2/SIN(AM)', kind='interp', line=484)
W('22,2070', 0o02235, '', '', 'MFI +4', kind='operand', line=485)
W('22,2071', 0o03310, '', '', 'TMFI +4', kind='operand', line=486)
W('22,2072', 0o45325, '', 'PDDL', 'DSU', kind='interp', line=487)
W('22,2073', 0o03316, '', '', 'TMFI +10D', kind='operand', line=488)
W('22,2074', 0o02243, '', '', 'MFI +10D', kind='operand', line=489)
W('22,2075', 0o77666, '', 'VDEF', kind='interp', line=490)
W('22,2076', 0o03326, '', 'STORE', 'COFSKEW', 'EQUALS MFISKEW', kind='interp', line=491)

# CALCULATE AM AND PROCEED ACCORDING TO ITS MAGNITUDE

W('22,2077', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=495)
W('22,2100', 0o02231, '', '', 'MFI', kind='operand', line=496)
W('22,2101', 0o02251, '', '', 'MFI +16D', kind='operand', line=497)
W('22,2102', 0o43225, '', 'DSU', 'DAD', kind='interp', line=498)
W('22,2103', 0o06512, '', '', 'DP1/4TH', kind='operand', line=499)
W('22,2104', 0o02241, '', '', 'MFI +8D', kind='operand', line=500)
W('22,2105', 0o03334, '', 'STORE', 'CAM', 'CAM = (MFI0+MFI4+MFI8-1)/2 HALF SCALE', kind='interp', line=501)
W('22,2106', 0o77726, '', 'ARCCOS', kind='interp', line=502)
W('22,2107', 0o03336, '', 'STORE', 'AM', 'AM=ARCCOS(CAM)        (AM SCALED BY 2)', kind='interp', line=503)
W('22,2110', 0o51025, '', 'DSU', 'BPL', kind='interp', line=504)
W('22,2111', 0o04363, '', '', 'MINANG', kind='operand', line=505)
W('22,2112', 0o44117, '', '', 'CHECKMAX', kind='operand', line=506)
W('22,2113', 0o77751, '', 'TLOAD', '', 'MANEUVER LESS THAN .25 DEGREES', kind='interp', line=507)
W('22,2114', 0o00322, '', '', 'CPHI', 'GO DIRECTLY INTO ATTITUDE HOLD', kind='operand', line=508)
W('22,2115', 0o37236, '', 'STCALL', 'CDUXD', 'ABOUT COMMANDED ANGLES', kind='interp', line=509)
W('22,2116', 0o44742, '', '', 'TOOBADI', 'STOP RATE AND EXIT', kind='operand', line=510)

W('22,2117', 0o45345, 'CHECKMAX', 'DLOAD', 'DSU', kind='interp', line=512)
W('22,2120', 0o03336, '', '', 'AM', kind='operand', line=513)
W('22,2121', 0o04365, '', '', 'MAXANG', kind='operand', line=514)
W('22,2122', 0o77244, '', 'BPL', 'VLOAD', kind='interp', line=515)
W('22,2123', 0o44131, '', '', 'ALTCALC', 'UNIT', kind='operand', line=516)
W('22,2124', 0o03326, '', '', 'COFSKEW', 'COFSKEW', kind='operand', line=517)
W('22,2125', 0o77656, '', 'UNIT', kind='interp', line=518)
W('22,2126', 0o03271, '', 'STORE', 'COF', 'COF IS THE MANEUVER AXIS', kind='interp', line=519)
# Page 353
W('22,2127', 0o77650, '', 'GOTO', '', 'SEE IF MANEUVER GOES THRU GIMBAL LOCK', kind='interp', line=521)
W('22,2130', 0o44744, '', '', 'LOCSKIRT', kind='operand', line=522)
W('22,2131', 0o53375, 'ALTCALC', 'VLOAD', 'VAD', 'IF AM GREATER THAN 170 DEGREES', kind='interp', line=523)
W('22,2132', 0o02231, '', '', 'MFI', kind='operand', line=524)
W('22,2133', 0o03304, '', '', 'TMFI', kind='operand', line=525)
W('22,2134', 0o77762, '', 'VSR1', kind='interp', line=526)
W('22,2135', 0o27304, '', 'STOVL', 'MFISYM', kind='interp', line=527)
W('22,2136', 0o02237, '', '', 'MFI +6', kind='operand', line=528)
W('22,2137', 0o74455, '', 'VAD', 'VSR1', kind='interp', line=529)
W('22,2140', 0o03312, '', '', 'TMFI +6', kind='operand', line=530)
W('22,2141', 0o27312, '', 'STOVL', 'MFISYM +6', kind='interp', line=531)
W('22,2142', 0o02245, '', '', 'MFI +12D', kind='operand', line=532)
W('22,2143', 0o74455, '', 'VAD', 'VSR1', kind='interp', line=533)
W('22,2144', 0o03320, '', '', 'TMFI +12D', kind='operand', line=534)
W('22,2145', 0o03320, '', 'STORE', 'MFISYM +12D', 'MFISYM=(MFI+TMFI)/2   SCALED BY 4', kind='interp', line=535)

# CALCULATE COF

W('22,2146', 0o70545, '', 'DLOAD', 'SR1', kind='interp', line=539)
W('22,2147', 0o03334, '', '', 'CAM', kind='operand', line=540)
W('22,2150', 0o45325, '', 'PDDL', 'DSU', 'PDO CAM                               $4', kind='interp', line=541)
W('22,2151', 0o06520, '', '', 'DPHALF', kind='operand', line=542)
W('22,2152', 0o03334, '', '', 'CAM', kind='operand', line=543)
W('22,2153', 0o65204, '', 'BOVB', 'PDDL', 'PS2 1 - CAM                           $2', kind='interp', line=544)
W('22,2154', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=545)
W('22,2155', 0o03324, '', '', 'MFISYM +16D', kind='operand', line=546)
W('22,2156', 0o56225, '', 'DSU', 'DDV', kind='interp', line=547)
W('22,2157', 0o00001, '', '', '0', kind='operand', line=548)
W('22,2160', 0o00003, '', '', '2', kind='operand', line=549)
W('22,2161', 0o65366, '', 'SQRT', 'PDDL', 'COFZ = SQRT(MFISYM8-CAM)/(1-CAM)', kind='interp', line=550)
W('22,2162', 0o03314, '', '', 'MFISYM +8D', '                              $ ROOT 2', kind='operand', line=551)
W('22,2163', 0o56225, '', 'DSU', 'DDV', kind='interp', line=552)
W('22,2164', 0o00001, '', '', '0', kind='operand', line=553)
W('22,2165', 0o00003, '', '', '2', kind='operand', line=554)
W('22,2166', 0o65366, '', 'SQRT', 'PDDL', 'COFY = SQRT(MFISYM4-CAM)/(1-CAM)  $ROOT2', kind='interp', line=555)
W('22,2167', 0o03304, '', '', 'MFISYM', kind='operand', line=556)
W('22,2170', 0o56225, '', 'DSU', 'DDV', kind='interp', line=557)
W('22,2171', 0o00001, '', '', '0', kind='operand', line=558)
W('22,2172', 0o00003, '', '', '2', kind='operand', line=559)
W('22,2173', 0o55566, '', 'SQRT', 'VDEF', 'COFX = SQRT(MFISYM-CAM)/(1-CAM)  $ROOT 2', kind='interp', line=560)
W('22,2174', 0o77656, '', 'UNIT', kind='interp', line=561)
W('22,2175', 0o03271, '', 'STORE', 'COF', kind='interp', line=562)

# DETERMINE LARGEST COF AND ADJUST ACCORDINGLY

W('22,2176', 0o45345, 'COFMAXGO', 'DLOAD', 'DSU', kind='interp', line=566)
W('22,2177', 0o03271, '', '', 'COF', kind='operand', line=567)
W('22,2200', 0o03273, '', '', 'COF +2', kind='operand', line=568)
W('22,2201', 0o71240, '', 'BMN', 'DLOAD', 'COFY G COFX', kind='interp', line=569)
# Page 354
W('22,2202', 0o44211, '', '', 'COMP12', kind='operand', line=571)
W('22,2203', 0o03271, '', '', 'COF', kind='operand', line=572)
W('22,2204', 0o50025, '', 'DSU', 'BMN', kind='interp', line=573)
W('22,2205', 0o03275, '', '', 'COF +4', kind='operand', line=574)
W('22,2206', 0o44266, '', '', 'METHOD3', 'COFZ G COFX OR COFY', kind='operand', line=575)
W('22,2207', 0o77650, '', 'GOTO', kind='interp', line=576)
W('22,2210', 0o44242, '', '', 'METHOD1', 'COFX G COFY OR COFZ', kind='operand', line=577)
W('22,2211', 0o45345, 'COMP12', 'DLOAD', 'DSU', kind='interp', line=578)
W('22,2212', 0o03273, '', '', 'COF +2', kind='operand', line=579)
W('22,2213', 0o03275, '', '', 'COF +4', kind='operand', line=580)
W('22,2214', 0o77640, '', 'BMN', kind='interp', line=581)
W('22,2215', 0o44266, '', '', 'METHOD3', 'COFZ G COFY OR COFX', kind='operand', line=582)

W('22,2216', 0o51145, 'METHOD2', 'DLOAD', 'BPL', 'COFY MAX', kind='interp', line=584)
W('22,2217', 0o03330, '', '', 'COFSKEW +2', 'UY', kind='operand', line=585)
W('22,2220', 0o44224, '', '', 'U2POS', kind='operand', line=586)
W('22,2221', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=587)
W('22,2222', 0o03271, '', '', 'COF', kind='operand', line=588)
W('22,2223', 0o03271, '', 'STORE', 'COF', kind='interp', line=589)
W('22,2224', 0o51145, 'U2POS', 'DLOAD', 'BPL', kind='interp', line=590)
W('22,2225', 0o03306, '', '', 'MFISYM +2', 'UX UY', kind='operand', line=591)
W('22,2226', 0o44232, '', '', 'OKU21', kind='operand', line=592)
W('22,2227', 0o57545, '', 'DLOAD', 'DCOMP', 'SIGN OF UX OPPOSITE garbled', kind='interp', line=593)
W('22,2230', 0o03271, '', '', 'COF', kind='operand', line=594)
W('22,2231', 0o03271, '', 'STORE', 'COF', kind='interp', line=595)
W('22,2232', 0o51145, 'OKU21', 'DLOAD', 'BPL', kind='interp', line=596)
W('22,2233', 0o03316, '', '', 'MFISYM +10D', 'UY UZ', kind='operand', line=597)
W('22,2234', 0o44744, '', '', 'LOCSKIRT', kind='operand', line=598)
W('22,2235', 0o57545, '', 'DLOAD', 'DCOMP', 'SIGN OF UZ OPPOSITE TO UY', kind='interp', line=599)
W('22,2236', 0o03275, '', '', 'COF +4', kind='operand', line=600)
W('22,2237', 0o03275, '', 'STORE', 'COF +4', kind='interp', line=601)
W('22,2240', 0o77650, '', 'GOTO', kind='interp', line=602)
W('22,2241', 0o44744, '', '', 'LOCSKIRT', kind='operand', line=603)
W('22,2242', 0o51145, 'METHOD1', 'DLOAD', 'BPL', 'COFX MAX', kind='interp', line=604)
W('22,2243', 0o03326, '', '', 'COFSKEW', 'UX', kind='operand', line=605)
W('22,2244', 0o44250, '', '', 'U1POS', kind='operand', line=606)
W('22,2245', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=607)
W('22,2246', 0o03271, '', '', 'COF', kind='operand', line=608)
W('22,2247', 0o03271, '', 'STORE', 'COF', kind='interp', line=609)
W('22,2250', 0o51145, 'U1POS', 'DLOAD', 'BPL', kind='interp', line=610)
W('22,2251', 0o03306, '', '', 'MFISYM +2', 'UX UY', kind='operand', line=611)
W('22,2252', 0o44256, '', '', 'OKU12', kind='operand', line=612)
W('22,2253', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=613)
W('22,2254', 0o03273, '', '', 'COF +2', 'SIGN OF UY OPPOSITE TO UX', kind='operand', line=614)
W('22,2255', 0o03273, '', 'STORE', 'COF +2', kind='interp', line=615)
W('22,2256', 0o51145, 'OKU12', 'DLOAD', 'BPL', kind='interp', line=616)
W('22,2257', 0o03310, '', '', 'MFISYM +4', 'UX UZ', kind='operand', line=617)
W('22,2260', 0o44744, '', '', 'LOCSKIRT', kind='operand', line=618)
W('22,2261', 0o57545, '', 'DLOAD', 'DCOMP', 'SIGN OF UZ OPPOSITE TO UY', kind='interp', line=619)
W('22,2262', 0o03275, '', '', 'COF +4', kind='operand', line=620)
# Page 355
W('22,2263', 0o03275, '', 'STORE', 'COF +4', kind='interp', line=622)
W('22,2264', 0o77650, '', 'GOTO', kind='interp', line=623)
W('22,2265', 0o44744, '', '', 'LOCSKIRT', kind='operand', line=624)
W('22,2266', 0o51145, 'METHOD3', 'DLOAD', 'BPL', 'COFZ MAX', kind='interp', line=625)
W('22,2267', 0o03332, '', '', 'COFSKEW +4', 'UZ', kind='operand', line=626)
W('22,2270', 0o44274, '', '', 'U3POS', kind='operand', line=627)
W('22,2271', 0o57575, '', 'VLOAD', 'VCOMP', kind='interp', line=628)
W('22,2272', 0o03271, '', '', 'COF', kind='operand', line=629)
W('22,2273', 0o03271, '', 'STORE', 'COF', kind='interp', line=630)
W('22,2274', 0o51145, 'U3POS', 'DLOAD', 'BPL', kind='interp', line=631)
W('22,2275', 0o03310, '', '', 'MFISYM +4', 'UX UZ', kind='operand', line=632)
W('22,2276', 0o44302, '', '', 'OKU31', kind='operand', line=633)
W('22,2277', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=634)
W('22,2300', 0o03271, '', '', 'COF', 'SIGN OF UX OPPOSITE TO UZ', kind='operand', line=635)
W('22,2301', 0o03271, '', 'STORE', 'COF', kind='interp', line=636)
W('22,2302', 0o51145, 'OKU31', 'DLOAD', 'BPL', kind='interp', line=637)
W('22,2303', 0o03316, '', '', 'MFISYM +10D', 'UY UZ', kind='operand', line=638)
W('22,2304', 0o44744, '', '', 'LOCSKIRT', kind='operand', line=639)
W('22,2305', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=640)
W('22,2306', 0o03273, '', '', 'COF +2', 'SIGN OF UY OPPOSITE TO UZ', kind='operand', line=641)
W('22,2307', 0o03273, '', 'STORE', 'COF +2', kind='interp', line=642)
W('22,2310', 0o77650, '', 'GOTO', kind='interp', line=643)
W('22,2311', 0o44744, '', '', 'LOCSKIRT', kind='operand', line=644)
# Page 356
# MATRIX OPERATIONS

#   BANK 13
#   SETLOC KALCMON2
#   BANK

#   EBANK= BCDU

W('22,2312', 0o76601, 'MXM3', 'SETPD', 'VLOAD*', 'MXM3 MULTIPLIES 2 3X3 MATRICES', kind='interp', line=654)
W('22,2313', 0o00001, '', '', '0', 'AND LEAVES RESULT IN PD LIST', kind='operand', line=655)
W('22,2314', 0o00001, '', '', '0,1', 'AND MPAC', kind='operand', line=656)
W('22,2315', 0o62703, '', 'VXM*', 'PDVL*', kind='interp', line=657)
W('22,2316', 0o77776, '', '', '0,2', kind='operand', line=658)
W('22,2317', 0o00007, '', '', '6,1', kind='operand', line=659)
W('22,2320', 0o62703, '', 'VXM*', 'PDVL*', kind='interp', line=660)
W('22,2321', 0o77776, '', '', '0,2', kind='operand', line=661)
W('22,2322', 0o00015, '', '', '12D,1', kind='operand', line=662)
W('22,2323', 0o41503, '', 'VXM*', 'PUSH', kind='interp', line=663)
W('22,2324', 0o77776, '', '', '0,2', kind='operand', line=664)
W('22,2325', 0o77616, '', 'RVQ', kind='interp', line=665)

# RETURN WITH MIXM2 IN PD LIST

W('22,2326', 0o76601, 'TRANSPOS', 'SETPD', 'VLOAD*', 'TRANSPOS TRANSPOSES A 3X3 MATRIX', kind='interp', line=669)
W('22,2327', 0o00001, '', '', '0', '      AND LEAVES RESULT IN PD LIST', kind='operand', line=670)
W('22,2330', 0o00001, '', '', '0,1', 'MATRIX ADDRESS IN XR1', kind='operand', line=671)
W('22,2331', 0o62713, '', 'PDVL*', 'PDVL*', kind='interp', line=672)
W('22,2332', 0o00007, '', '', '6,1', kind='operand', line=673)
W('22,2333', 0o00015, '', '', '12D,1', kind='operand', line=674)
W('22,2334', 0o77606, '', 'PUSH', '', 'MATRIX IN PD', kind='interp', line=675)
W('22,2335', 0o77776, 'TRNSPSPD', 'EXIT', '', 'ENTER WITH MATRIX AT 0 IN PD LIST', kind='interp', line=676)
W('22,2336', 0o50120, '', 'INDEX', 'FIXLOC', line=677)
W('22,2337', 0o52013, '', 'DXCH', '12', line=678)
W('22,2340', 0o50120, '', 'INDEX', 'FIXLOC', line=679)
W('22,2341', 0o52017, '', 'DXCH', '16', line=680)
W('22,2342', 0o50120, '', 'INDEX', 'FIXLOC', line=681)
W('22,2343', 0o52013, '', 'DXCH', '12', line=682)
W('22,2344', 0o50120, '', 'INDEX', 'FIXLOC', line=683)
W('22,2345', 0o52015, '', 'DXCH', '14', line=684)
W('22,2346', 0o50120, '', 'INDEX', 'FIXLOC', line=685)
W('22,2347', 0o52005, '', 'DXCH', '4', line=686)
W('22,2350', 0o50120, '', 'INDEX', 'FIXLOC', line=687)
W('22,2351', 0o52015, '', 'DXCH', '14', line=688)
W('22,2352', 0o50120, '', 'INDEX', 'FIXLOC', line=689)
W('22,2353', 0o52003, '', 'DXCH', '2', line=690)
W('22,2354', 0o50120, '', 'INDEX', 'FIXLOC', line=691)
W('22,2355', 0o52007, '', 'DXCH', '6', line=692)
W('22,2356', 0o50120, '', 'INDEX', 'FIXLOC', line=693)
W('22,2357', 0o52003, '', 'DXCH', '2', line=694)
# Page 357
W('22,2360', 0o06037, '', 'TC', 'INTPRET', line=696)
W('22,2361', 0o77616, '', 'RVQ', kind='interp', line=697)

#   BANK 15
#   SETLOC KALCMON1
#   BANK

#   EBANK= BCDU

W('22,2362', 0o00013, 'MINANG', '2DEC', '0.00069375', kind='data', line=705)
W('22,2363', 0o13563, kind='data', line=705)

W('22,2364', 0o17070, 'MAXANG', '2DEC', '0.472222222', kind='data', line=707)
W('22,2365', 0o34343, kind='data', line=707)

# GIMBAL LOCK CONSTANTS

# D = MGA CORRESPONDING TO GIMBAL LOCK = 60 DEGREES
# NGL = BUFFER ANGLE (TO AVOID DIVISIONS BY ZERO) = 2 DEGREES

W('22,2366', 0o15666, 'SD', '2DEC', '.433015', '= SIN(D)                      $2', kind='data', line=714)
W('22,2367', 0o20443, kind='data', line=714)

W('22,2370', 0o33555, 'K3S1', '2DEC', '.86603', '= SIN(D)                      $1', kind='data', line=716)
W('22,2371', 0o01106, kind='data', line=716)

W('22,2372', 0o67777, 'K4', '2DEC', '-.25', '= -COS(D)                     $2', kind='data', line=718)
W('22,2373', 0o77777, kind='data', line=718)

W('22,2374', 0o04000, 'K4SQ', '2DEC', '.125', '= COS(D)COS(D)                $2', kind='data', line=720)
W('22,2375', 0o00000, kind='data', line=720)

W('22,2376', 0o00216, 'SNGLCD', '2DEC', '.008725', '= SIN(NGL)COS(D)              $2', kind='data', line=722)
W('22,2377', 0o36323, kind='data', line=722)

W('22,2400', 0o17773, 'CNGL', '2DEC', '.499695', 'COS(NGL)                      $2', kind='data', line=724)
W('22,2401', 0o00057, kind='data', line=724)

W('22,2402', 0o14344, 'LOCKANGL', 'DEC', '.388889', '= 70 DEGREES', kind='data', line=726)

# INTERPRETIVE SUBROUTINE TO READ THE CDU ANGLES

W('22,2403', 0o30034, 'READCDUK', 'CA', 'CDUZ', 'LOAD T(MPAC) WITH CDU ANGLES', line=730)
W('22,2404', 0o54156, '', 'TS', 'MPAC +2', line=731)
W('22,2405', 0o00006, '', 'EXTEND', line=732)
W('22,2406', 0o30033, '', 'DCA', 'CDUX', 'AND CHANGE MODE TO TRIPLE PRECISION', line=733)
W('22,2407', 0o16476, '', 'TCF', 'TLOAD +6', line=734)

W('22,2410', 0o66370, 'CDUTODCM', 'AXT,1', 'SSP', kind='interp', line=736)
W('22,2411', 0o00003, '', 'OCT', '3', kind='data', line=737)
W('22,2412', 0o00051, '', '', 'S1', kind='operand', line=738)
W('22,2413', 0o00001, '', 'OCT', '1', 'SET XR1, S1, AND PD FOR LOOP', kind='data', line=739)
W('22,2414', 0o00010, '', 'STORE', '7', kind='interp', line=740)
W('22,2415', 0o77601, '', 'SETPD', kind='interp', line=741)
W('22,2416', 0o00001, '', '', '0', kind='operand', line=742)
W('22,2417', 0o47133, 'LOOPSIN', 'SLOAD*', 'RTB', kind='interp', line=743)
W('22,2420', 0o00013, '', '', '10D,1', kind='operand', line=744)
W('22,2421', 0o21576, '', '', 'CDULOGIC', kind='operand', line=745)
# Page 358
W('22,2422', 0o00013, '', 'STORE', '10D', 'LOAD PD WITH  0 SIN(PHI)', kind='interp', line=747)
W('22,2423', 0o65356, '', 'SIN', 'PDDL', '              2 COS(PHI)', kind='interp', line=748)
W('22,2424', 0o00013, '', '', '10D', '              4 SIN(THETA)', kind='operand', line=749)
W('22,2425', 0o41546, '', 'COS', 'PUSH', '              6 COS(THETA)', kind='interp', line=750)
W('22,2426', 0o71300, '', 'TIX,1', 'DLOAD', '              8 SIN(PSI)', kind='interp', line=751)
W('22,2427', 0o44417, '', '', 'LOOPSIN', '              10 COS(PSI)', kind='operand', line=752)
W('22,2430', 0o00007, '', '', '6', kind='operand', line=753)
W('22,2431', 0o72405, '', 'DMP', 'SL1', kind='interp', line=754)
W('22,2432', 0o00013, '', '', '10D', kind='operand', line=755)
W('22,2433', 0o10001, '', 'STORE', '0,2', 'C0 = COS(THETA)COS(PSI)', kind='interp', line=756)
W('22,2434', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=757)
W('22,2435', 0o00005, '', '', '4', kind='operand', line=758)
W('22,2436', 0o00001, '', '', '0', kind='operand', line=759)
W('22,2437', 0o41325, '', 'PDDL', 'DMP', '(PD6 SIN(THETA)SIN(PHI))', kind='interp', line=760)
W('22,2440', 0o00007, '', '', '6', kind='operand', line=761)
W('22,2441', 0o00011, '', '', '8D', kind='operand', line=762)
W('22,2442', 0o72405, '', 'DMP', 'SL1', kind='interp', line=763)
W('22,2443', 0o00003, '', '', '2', kind='operand', line=764)
W('22,2444', 0o72421, '', 'BDSU', 'SL1', kind='interp', line=765)
W('22,2445', 0o00015, '', '', '12D', kind='operand', line=766)
W('22,2446', 0o10003, '', 'STORE', '2,2', 'C1=-COS(THETA)SIN(PSI)COS(PHI)', kind='interp', line=767)
W('22,2447', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=768)
W('22,2450', 0o00003, '', '', '2', kind='operand', line=769)
W('22,2451', 0o00005, '', '', '4', kind='operand', line=770)
W('22,2452', 0o41325, '', 'PDDL', 'DMP', '(PD7 COS(PHI)SIN(THETA)) SCALED 4', kind='interp', line=771)
W('22,2453', 0o00007, '', '', '6', kind='operand', line=772)
W('22,2454', 0o00011, '', '', '8D', kind='operand', line=773)
W('22,2455', 0o72405, '', 'DMP', 'SL1', kind='interp', line=774)
W('22,2456', 0o00001, '', '', '0', kind='operand', line=775)
W('22,2457', 0o72415, '', 'DAD', 'SL1', kind='interp', line=776)
W('22,2460', 0o00017, '', '', '14D', kind='operand', line=777)
W('22,2461', 0o10005, '', 'STORE', '4,2', 'C2=COS(THETA)SIN(PSI)SIN(PHI)', kind='interp', line=778)
W('22,2462', 0o77745, '', 'DLOAD', kind='interp', line=779)
W('22,2463', 0o00011, '', '', '8D', kind='operand', line=780)
W('22,2464', 0o10007, '', 'STORE', '6,2', 'C3=SIN(PSI)', kind='interp', line=781)
W('22,2465', 0o77745, '', 'DLOAD', kind='interp', line=782)
W('22,2466', 0o00013, '', '', '10D', kind='operand', line=783)
W('22,2467', 0o72405, '', 'DMP', 'SL1', kind='interp', line=784)
W('22,2470', 0o00003, '', '', '2', kind='operand', line=785)
W('22,2471', 0o10011, '', 'STORE', '8D,2', 'C4=COS(PSI)COS(PHI)', kind='interp', line=786)
W('22,2472', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=787)
W('22,2473', 0o00013, '', '', '10D', kind='operand', line=788)
W('22,2474', 0o00001, '', '', '0', kind='operand', line=789)
W('22,2475', 0o72476, '', 'DCOMP', 'SL1', kind='interp', line=790)
W('22,2476', 0o10013, '', 'STORE', '10D,2', 'C5=-COS(PSI)SIN(PHI)', kind='interp', line=791)
W('22,2477', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=792)
W('22,2500', 0o00005, '', '', '4', kind='operand', line=793)
W('22,2501', 0o00013, '', '', '10D', kind='operand', line=794)
W('22,2502', 0o72476, '', 'DCOMP', 'SL1', kind='interp', line=795)
W('22,2503', 0o10015, '', 'STORE', '12D,2', 'C6=-SIN(THETA)COS(PSI)', kind='interp', line=796)
# Page 359
W('22,2504', 0o77745, '', 'DLOAD', kind='interp', line=798)
W('22,2505', 0o72405, '', 'DMP', 'SL1', '(PUSH UP 7)', kind='interp', line=799)
W('22,2506', 0o00011, '', '', '8D', kind='operand', line=800)
W('22,2507', 0o41325, '', 'PDDL', 'DMP', '(PD7 COS(PHI)SIN(THETA)SIN(PSI)) SCALE 4', kind='interp', line=801)
W('22,2510', 0o00007, '', '', '6', kind='operand', line=802)
W('22,2511', 0o00001, '', '', '0', kind='operand', line=803)
W('22,2512', 0o72415, '', 'DAD', 'SL1', '(PUSH UP 7)', kind='interp', line=804)
W('22,2513', 0o77626, '', 'STADR', '', 'C7=COS(PHI)SIN(THETA)SIN(PSI)', kind='interp', line=805)
W('22,2514', 0o67760, '', 'STORE', '14D,2', '      +COS(THETA)SIN(PHI)', kind='interp', line=806)
W('22,2515', 0o77745, '', 'DLOAD', kind='interp', line=807)
W('22,2516', 0o72405, '', 'DMP', 'SL1', '(PUSH UP 6)', kind='interp', line=808)
W('22,2517', 0o00011, '', '', '8D', kind='operand', line=809)
W('22,2520', 0o41325, '', 'PDDL', 'DMP', '(PD6 SIN(THETA)SIN(PHI)SIN(PSI)) SCALE 4', kind='interp', line=810)
W('22,2521', 0o00007, '', '', '6', kind='operand', line=811)
W('22,2522', 0o00003, '', '', '2', kind='operand', line=812)
W('22,2523', 0o72425, '', 'DSU', 'SL1', '(PUSH UP 6)', kind='interp', line=813)
W('22,2524', 0o77626, '', 'STADR', kind='interp', line=814)
W('22,2525', 0o67756, '', 'STORE', '16D,2', 'C8=-SIN(THETA)SIN(PHI)SIN(PSI)', kind='interp', line=815)
W('22,2526', 0o77616, '', 'RVQ', '', '+COS(THETA)COS(PHI)', kind='interp', line=816)

# CALCULATION OF THE MATRIX DEL......
#
# *         *           __T           *
# DEL = (IDMATRIX)COS(A)+UU (1-COS(A))+UX SIN(A)          SCALED 1
# _
# WHERE U IS A UNIT VECTOR (DP SCALED 2) ALONG THE AXIS OF ROTATION.
# A IS THE ANGLE OF ROTATION (DP SCALED 2)
# _
# UPON ENTRY, THE STARTING ADDRESS OF U IS COF, AND A IS IN MPAC

W('22,2527', 0o41401, 'DELCOMP', 'SETPD', 'PUSH', 'MPAC CONTAINS THE ANGLE A', kind='interp', line=828)
W('22,2530', 0o00001, '', '', '0', kind='operand', line=829)
W('22,2531', 0o65356, '', 'SIN', 'PDDL', 'PD0 = SIN(A)', kind='interp', line=830)
W('22,2532', 0o41546, '', 'COS', 'PUSH', 'PD2 = COS(A)', kind='interp', line=831)
W('22,2533', 0o65302, '', 'SR2', 'PDDL', 'PD2 = COS(A)                          $8', kind='interp', line=832)
W('22,2534', 0o41021, '', 'BDSU', 'BOVB', kind='interp', line=833)
W('22,2535', 0o06520, '', '', 'DPHALF', kind='operand', line=834)
W('22,2536', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=835)
W('22,2537', 0o77725, '', 'PDDL', '', 'PDA = 1-COS(A)', kind='interp', line=836)

# COMPUTE THE DIAGONAL COMPONENTS OF DEL

W('22,2540', 0o03271, '', '', 'COF', kind='operand', line=840)
W('22,2541', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=841)
W('22,2542', 0o00005, '', '', '4', kind='operand', line=842)
W('22,2543', 0o52415, '', 'DAD', 'SL3', kind='interp', line=843)
W('22,2544', 0o00003, '', '', '2', kind='operand', line=844)
W('22,2545', 0o77604, '', 'BOVB', kind='interp', line=845)
W('22,2546', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=846)
# Page 360
W('22,2547', 0o16231, '', 'STODL', 'KEL', 'UX UX(1-COS(A)) +COS(A)               $1', kind='interp', line=848)
W('22,2550', 0o03273, '', '', 'COF +2', kind='operand', line=849)
W('22,2551', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=850)
W('22,2552', 0o00005, '', '', '4', kind='operand', line=851)
W('22,2553', 0o52415, '', 'DAD', 'SL3', kind='interp', line=852)
W('22,2554', 0o00003, '', '', '2', kind='operand', line=853)
W('22,2555', 0o77604, '', 'BOVB', kind='interp', line=854)
W('22,2556', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=855)
W('22,2557', 0o16241, '', 'STODL', 'KEL +8D', 'UY UY(1-COS(A)) +COS(A)               $1', kind='interp', line=856)
W('22,2560', 0o03275, '', '', 'COF +4', kind='operand', line=857)
W('22,2561', 0o41316, '', 'DSQ', 'DMP', kind='interp', line=858)
W('22,2562', 0o00005, '', '', '4', kind='operand', line=859)
W('22,2563', 0o52415, '', 'DAD', 'SL3', kind='interp', line=860)
W('22,2564', 0o00003, '', '', '2', kind='operand', line=861)
W('22,2565', 0o77604, '', 'BOVB', kind='interp', line=862)
W('22,2566', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=863)
W('22,2567', 0o02251, '', 'STORE', 'KEL +16D', 'UZ UZ(1-COS(A)) +COS(A)               $1', kind='interp', line=864)

# COMPUTE THE OFF DIAGONAL TERMS OF DEL

W('22,2570', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=868)
W('22,2571', 0o03271, '', '', 'COF', kind='operand', line=869)
W('22,2572', 0o03273, '', '', 'COF +2', kind='operand', line=870)
W('22,2573', 0o72405, '', 'DMP', 'SL1', kind='interp', line=871)
W('22,2574', 0o00005, '', '', '4', kind='operand', line=872)
W('22,2575', 0o41325, '', 'PDDL', 'DMP', 'D6     UX UY (1-COS A)                $4', kind='interp', line=873)
W('22,2576', 0o03275, '', '', 'COF +4', kind='operand', line=874)
W('22,2577', 0o00001, '', '', '0', kind='operand', line=875)
W('22,2600', 0o43206, '', 'PUSH', 'DAD', 'D8    UZ SIN A                        $4', kind='interp', line=876)
W('22,2601', 0o00007, '', '', '6', kind='operand', line=877)
W('22,2602', 0o41112, '', 'SL2', 'BOVB', kind='interp', line=878)
W('22,2603', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=879)
W('22,2604', 0o16237, '', 'STODL', 'KEL +6', kind='interp', line=880)
W('22,2605', 0o62421, '', 'BDSU', 'SL2', kind='interp', line=881)
W('22,2606', 0o77604, '', 'BOVB', kind='interp', line=882)
W('22,2607', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=883)
W('22,2610', 0o16233, '', 'STODL', 'KEL +2', kind='interp', line=884)
W('22,2611', 0o03271, '', '', 'COF', kind='operand', line=885)
W('22,2612', 0o41205, '', 'DMP', 'DMP', kind='interp', line=886)
W('22,2613', 0o03275, '', '', 'COF +4', kind='operand', line=887)
W('22,2614', 0o00005, '', '', '4', kind='operand', line=888)
W('22,2615', 0o65352, '', 'SL1', 'PDDL', 'D6    UX UZ (1-COS A)                 $4', kind='interp', line=889)
W('22,2616', 0o03273, '', '', 'COF +2', kind='operand', line=890)
W('22,2617', 0o41405, '', 'DMP', 'PUSH', 'D8    UY SIN(A)', kind='interp', line=891)
W('22,2620', 0o00001, '', '', '0', kind='operand', line=892)
W('22,2621', 0o62415, '', 'DAD', 'SL2', kind='interp', line=893)
W('22,2622', 0o00007, '', '', '6', kind='operand', line=894)
W('22,2623', 0o77604, '', 'BOVB', kind='interp', line=895)
W('22,2624', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=896)
W('22,2625', 0o16235, '', 'STODL', 'KEL +4', 'UX UZ (1-COS(A))+UY SIN(A)', kind='interp', line=897)
# Page 361
W('22,2626', 0o62421, '', 'BDSU', 'SL2', kind='interp', line=899)
W('22,2627', 0o77604, '', 'BOVB', kind='interp', line=900)
W('22,2630', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=901)
W('22,2631', 0o16245, '', 'STODL', 'KEL +12D', 'UX UZ (1-COS(A))-UY SIN(A)', kind='interp', line=902)
W('22,2632', 0o03273, '', '', 'COF +2', kind='operand', line=903)
W('22,2633', 0o41205, '', 'DMP', 'DMP', kind='interp', line=904)
W('22,2634', 0o03275, '', '', 'COF +4', kind='operand', line=905)
W('22,2635', 0o00005, '', '', '4', kind='operand', line=906)
W('22,2636', 0o65352, '', 'SL1', 'PDDL', 'D6    UY UZ (1-COS(A))                $ 4', kind='interp', line=907)
W('22,2637', 0o03271, '', '', 'COF', kind='operand', line=908)
W('22,2640', 0o41405, '', 'DMP', 'PUSH', 'D8    UX SIN(A)', kind='interp', line=909)
W('22,2641', 0o00001, '', '', '0', kind='operand', line=910)
W('22,2642', 0o62415, '', 'DAD', 'SL2', kind='interp', line=911)
W('22,2643', 0o00007, '', '', '6', kind='operand', line=912)
W('22,2644', 0o77604, '', 'BOVB', kind='interp', line=913)
W('22,2645', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=914)
W('22,2646', 0o16247, '', 'STODL', 'KEL +14D', 'UY UZ(1-COS(A)) +UX SIN(A)', kind='interp', line=915)
W('22,2647', 0o62421, '', 'BDSU', 'SL2', kind='interp', line=916)
W('22,2650', 0o77604, '', 'BOVB', kind='interp', line=917)
W('22,2651', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=918)
W('22,2652', 0o02243, '', 'STORE', 'KEL +10D', 'UY UZ (1-COS(A)) -UX SIN(A)', kind='interp', line=919)
W('22,2653', 0o77616, '', 'RVQ', kind='interp', line=920)

# DIRECTION COSINE MATRIX TO CDU ANGLE ROUTINE
# X1 CONTAINS THE COMPLEMENT OF THE STARTING ADDRESS FOR MATRIX (SCALED 2).
# LEAVE CDU ANGLES SCALED 2PI IN V(MPAC).
# COS(MGA) WILL BE LEFT IN S1 (SCALED 1).
#
# THE DIRECTION COSINE MATRIX RELATING S/C AXES TO STABLE MEMBER AXES CAN BE WRITTEN AS:
#
# C  = COS(THETA) COS(PSI
# 0
#
# C  = -COS(THETA) SIN(PSI) COS(PHI) + SIN(THETA) SIN(PHI)
# 1
#
# C  = COS(THETA) SIN(PSI) SIN(PHI) + SIN(THETA) COS(PHI)
# 2
#
# C  = SIN(PSI)
# 3
#
# C  = COS(PSI) COS(PHI)
# 4
#
# C  = -COS(PSI) SIN(PHI)
# 5
#
# C  = -SIN(THETA) COS(PSI)
# 6
#
# C  = SIN(THETA) SIN(PSI) COS(PHI) + COS (THETA) SIN(PHI)
# 7
#
# C  = -SIN(THETA) SIN(PSI) SIN(PHI) + COS(THETA)COS(PHI)
# 8
# Page 362
#
# WHERE PHI = OGA
# THETA = IGA
# PSI = MGA

W('22,2654', 0o67543, 'DCMTOCDU', 'DLOAD*', 'ARCSIN', kind='interp', line=961)
W('22,2655', 0o00007, '', '', '6,1', kind='operand', line=962)
W('22,2656', 0o71406, '', 'PUSH', 'COS', 'PD +0         PSI', kind='interp', line=963)
W('22,2657', 0o41152, '', 'SL1', 'BOVB', kind='interp', line=964)
W('22,2660', 0o21712, '', '', 'SIGNMPAC', kind='operand', line=965)
W('22,2661', 0o00051, '', 'STORE', 'S1', kind='interp', line=966)
W('22,2662', 0o57543, '', 'DLOAD*', 'DCOMP', kind='interp', line=967)
W('22,2663', 0o00015, '', '', '12D,1', kind='operand', line=968)
W('22,2664', 0o67471, '', 'DDV', 'ARCSIN', kind='interp', line=969)
W('22,2665', 0o00051, '', '', 'S1', kind='operand', line=970)
W('22,2666', 0o51123, '', 'PDDL*', 'BPL', 'PD +2         THETA', kind='interp', line=971)
W('22,2667', 0o00001, '', '', '0,1', 'MUST CHECK THE SIGN OF COS(THETA)', kind='operand', line=972)
W('22,2670', 0o44702, '', '', 'OKTHETA', 'TO DETERMINE THE PROPER QUADRANT.', kind='operand', line=973)
W('22,2671', 0o57545, '', 'DLOAD', 'DCOMP', kind='interp', line=974)
W('22,2672', 0o43244, '', 'BPL', 'DAD', kind='interp', line=975)
W('22,2673', 0o44677, '', '', 'SUHALFA', kind='operand', line=976)
W('22,2674', 0o06520, '', '', 'DPHALF', kind='operand', line=977)
W('22,2675', 0o77650, '', 'GOTO', kind='interp', line=978)
W('22,2676', 0o44701, '', '', 'CALCPHI', kind='operand', line=979)
W('22,2677', 0o77625, 'SUHALFA', 'DSU', kind='interp', line=980)
W('22,2700', 0o06520, '', '', 'DPHALF', kind='operand', line=981)
W('22,2701', 0o77606, 'CALCPHI', 'PUSH', kind='interp', line=982)
W('22,2702', 0o57543, 'OKTHETA', 'DLOAD*', 'DCOMP', kind='interp', line=983)
W('22,2703', 0o00013, '', '', '10D,1', kind='operand', line=984)
W('22,2704', 0o67471, '', 'DDV', 'ARCSIN', kind='interp', line=985)
W('22,2705', 0o00051, '', '', 'S1', kind='operand', line=986)
W('22,2706', 0o51123, '', 'PDDL*', 'BPL', 'PUSH DOWN PHI', kind='interp', line=987)
W('22,2707', 0o00011, '', '', '8D,1', kind='operand', line=988)
W('22,2710', 0o44722, '', '', 'OKPHI', kind='operand', line=989)
W('22,2711', 0o57545, '', 'DLOAD', 'DCOMP', 'PUSH UP PHI', kind='interp', line=990)
W('22,2712', 0o43244, '', 'BPL', 'DAD', kind='interp', line=991)
W('22,2713', 0o44717, '', '', 'SUHALFAP', kind='operand', line=992)
W('22,2714', 0o06520, '', '', 'DPHALF', kind='operand', line=993)
W('22,2715', 0o77650, '', 'GOTO', kind='interp', line=994)
W('22,2716', 0o44723, '', '', 'VECOFANG', kind='operand', line=995)
W('22,2717', 0o52025, 'SUHALFAP', 'DSU', 'GOTO', kind='interp', line=996)
W('22,2720', 0o06520, '', '', 'DPHALF', kind='operand', line=997)
W('22,2721', 0o44723, '', '', 'VECOFANG', kind='operand', line=998)
W('22,2722', 0o77745, 'OKPHI', 'DLOAD', '', 'PUSH UP PHI', kind='interp', line=999)
W('22,2723', 0o43466, 'VECOFANG', 'VDEF', 'RVQ', kind='interp', line=1000)
# Page 363
# ROUTINES FOR TERMINATING THE AUTOMATIC MANEUVER AND RETURNING TO USER.

W('22,2724', 0o77776, 'TOOBADF', 'EXIT', kind='interp', line=1004)
W('22,2725', 0o05567, '', 'TC', 'ALARM', line=1005)
W('22,2726', 0o00401, '', 'OCT', '00401', kind='data', line=1006)

W('22,2727', 0o12732, '', 'TCF', 'NOGO', 'DO NOT ZERO ATTITUDE ERRORS', line=1008)

W('22,2730', 0o04616, '', 'TC', 'BANKCALL', line=1010)
W('22,2731', 0o40153, '', 'CADR', 'ZATTEROR', 'ZERO ATTITUDE ERRORS', kind='data', line=1011)

W('22,2732', 0o04616, 'NOGO', 'TC', 'BANKCALL', line=1013)
W('22,2733', 0o40165, '', 'CADR', 'STOPRATE', 'STOP RATES', kind='data', line=1014)

W('22,2734', 0o34752, '', 'CAF', 'TWO', line=1016)
W('22,2735', 0o00004, '', 'INHINT', '', 'ALL RETURNS ARE NOW MADE VIA GOODEND', line=1017)
W('22,2736', 0o05203, '', 'TC', 'WAITLIST', line=1018)
#   EBANK= BCDU
W('22,2737', 0o03234, '', '2CADR', 'GOODMANU', kind='data', line=1020)
W('22,2740', 0o44066, kind='data', line=1020)

W('22,2741', 0o15155, '', 'TCF', 'ENDOFJOB', line=1022)

W('22,2742', 0o77776, 'TOOBADI', 'EXIT', kind='interp', line=1024)
W('22,2743', 0o12732, '', 'TCF', 'NOGO', line=1025)
