"""SYSTEM_TEST_STANDARD_LEAD_INS.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/SYSTEM_TEST_STANDARD_LEAD_INS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 370-372 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('SYSTEM_TEST_STANDARD_LEAD_INS', 'SYSTEM_TEST_STANDARD_LEAD_INS.agc', 'Luminary099', pages='370-372')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     SYSTEM_TEST_STANDARD_LEAD_INS.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        370-372
# Mod history:  2009-05-17 RSB  Adapted from the corresponding
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

# Page 370
#   EBANK= XSM

#   BANK 33
#   SETLOC E/PROG
#   BANK

#   COUNT* $$/P07

# SPECIAL PROGRAMS TO EASE THE PANGS OF ERASABLE MEMORY PROGRAMS.
#
# E/BKCALL      FOR DOING BANKCALLS FROM AND RETURNING TO ERASABLE.
#
# THIS ROUTINE IS CALLABLE FROM ERASABLE OR FIXED.  LIKE BANKCALL, HOWEVER, SWITCHING BETWEEN S3 AND S4
# IS NOT POSSIBLE.
#
# THE CALLING SEQUENCE IS:
#
# TC      BANKCALL
# CADR    E/BKCALL
# CADR    ROUTINE         # WHERE TO WANT TO GO IN FIXED.
# RETURN HERE FROM DISPLAY TERMINATE, BAD STALL OR TC Q.
# RETURN HERE FROM DISPLAY PROCEED OR GOOD RETURN FROM STALL.
# RETURN HERE FROM DISPLAY ENTER OR RECYCLE.
#
# THIS ROUTINE REQUIRES TWO ERASABLES (EBUF2, +1) IN UNSWITCHED WHICH ARE UNSHARED BY INTERRUPTS AND
# OTHER EMEMORY PROGRAMS.
#
# A + L ARE PRESERVED THROUGH BANKCALL AND E/BKCALL.

W('04,2576', 0o52134, 'E/BKCALL', 'DXCH', 'BUF2', 'SAVE A,L AND GET DP RETURN.', line=59)
W('04,2577', 0o53170, '', 'DXCH', 'EBUF2', 'SAVE DP RETURN.', line=60)
W('04,2600', 0o25167, '', 'INCR', 'EBUF2', 'RETURN +1 BECAUSE DOUBLE CADR.', line=61)
W('04,2601', 0o30006, '', 'CA', 'BBANK', line=62)
W('04,2602', 0o75012, '', 'MASK', 'LOW10', 'GET CURRENT EBANK.  (SBANK SOMEDAY)', line=63)
W('04,2603', 0o27170, '', 'ADS', 'EBUF2 +1', 'FORM BBCON.  (WAS FBANK)', line=64)
W('04,2604', 0o51167, '', 'NDX', 'EBUF2', line=65)
W('04,2605', 0o27777, '', 'CA', '0 -1', 'GET CADR OF ROUTINE.', line=66)
W('04,2606', 0o04622, '', 'TC', 'SWCALL', 'GO TO ROUTINE, SETTING Q TO SWRETURN', line=67)
# AND RESTORING A + L.
W('04,2607', 0o02613, '', 'TC', '+4', 'TX Q, V34, OR BAD STALL RETURN.', line=69)
W('04,2610', 0o02612, '', 'TC', '+2', 'PROCEED OR GOOD STALL RETURN.', line=70)
W('04,2611', 0o25167, '', 'INCR', 'EBUF2', 'ENTER OR RECYCLE RETURN.', line=71)
W('04,2612', 0o25167, '', 'INCR', 'EBUF2', line=72)
W('04,2613', 0o53170, 'E/SWITCH', 'DXCH', 'EBUF2', line=73)
W('04,2614', 0o52006, '', 'DTCB', line=74)

# Page 371
# E/CALL        FOR CALLING A FIXED MEMORY INTERPRETIVE SUBROUTINE FROM ERASABLE AND RETURNING TO ERASABLE.
#
# THE CALLING SEQUENCE IS...
#
# RTB
# E/CALL
# CADR    ROUTINE                 # THE INTERPRETIVE SUBROUTINE YOU WANT.
# # RETURNS HERE IN INTERPRETIVE.

W('04,2615', 0o22164, 'E/CALL', 'LXCH', 'LOC', 'ADRES -1 OF CADR.', line=86)
W('04,2616', 0o50001, '', 'INDEX', 'L', line=87)
W('04,2617', 0o30001, '', 'CA', 'L', 'CADR IN A.', line=88)
W('04,2620', 0o24001, '', 'INCR', 'L', line=89)
W('04,2621', 0o24001, '', 'INCR', 'L', 'RETURN ADRES IN L.', line=90)
W('04,2622', 0o53170, '', 'DXCH', 'EBUF2', 'STORE CADR AND RETURN', line=91)
W('04,2623', 0o06037, '', 'TC', 'INTPRET', line=92)
W('04,2624', 0o77624, '', 'CALL', kind='interp', line=93)
W('04,2625', 0o01167, '', '', 'EBUF2', 'INDIRECTLY EXECUTE ROUTINE.  IT MUST', kind='operand', line=94)
W('04,2626', 0o77776, '', 'EXIT', '', 'LEAVE VIA RVQ OR EQUIVALENT.', kind='interp', line=95)
W('04,2627', 0o23170, '', 'LXCH', 'EBUF2 +1', 'PICK UP RETURN.', line=96)
W('04,2630', 0o16041, '', 'TCF', 'INTPRET +2', 'SET LOC AND RETURN TO CALLER.', line=97)

# Page 372
# E/JOBWAK      FOR WAKING UP ERASABLE MEMORY JOBS.
#
# THIS ROUTINE MUST BE CALLED IN INTERRUPT OR WITH INTERRUPTS INHIBITED.
#
# THE CALLING SEQUENCE IS:
#
# INHINT
# ...
# CA      WAKEADR         # ADDRESS OF SLEEPING JOB
# TC      IBNKCALL
# CADR    E/JOBWAK
# ...                     # RETURNS HERE
# RELINT                  # IF YOU DID AND INHINT.

#   BANK 33
#   SETLOC E/PROG
#   BANK

#   COUNT* $$/P07

W('04,2631', 0o05137, 'E/JOBWAK', 'TC', 'JOBWAKE', 'ARRIVE IWTH ADRES IN A.', line=120)
W('04,2632', 0o44741, '', 'CS', 'BIT11', line=121)
W('04,2633', 0o50064, '', 'NDX', 'LOCCTR', line=122)
W('04,2634', 0o26164, '', 'ADS', 'LOC', 'KNOCK FIXED MEMORY BIT OUT OF ADRES.', line=123)
W('04,2635', 0o00072, '', 'TC', 'RUPTREG3', 'RETURN', line=124)
