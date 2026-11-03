"""SYSTEM_TEST_STANDARD_LEAD_INS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/SYSTEM_TEST_STANDARD_LEAD_INS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 420-422 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('SYSTEM_TEST_STANDARD_LEAD_INS', 'SYSTEM_TEST_STANDARD_LEAD_INS.agc', 'Comanche055', pages='420-422')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     SYSTEM_TEST_STANDARD_LEAD_INS.agc
# Purpose:      Part of the source code for Comanche, build 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 420-422
# Contact:      Onno Hommes <ohommes@cmu.edu>.
# Website:      www.ibiblio.org/apollo.
# Mod history:  05/07/09 OH     Transcription Batch 1 Assignment
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
# Refer directly to the online document mentioned above for further information.
# Please report any errors to info@sandroid.org.

# Page 420
#   EBANK= XSM

#   BANK 33
#   SETLOC E/PROG1
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
# CADR    ROUTINE         # WHERE YOU WANT TO GO IN FIXED.
# RETURN HERE FROM DISPLAY TERMINATE, BAD STALL OR TC Q.
# RETURN HERE FROM DISPLAY PROCEED OR GOOD RETURN FROM STALL.
# RETURN HERE FROM DISPLAY ENTER OR RECYCLE.
#
# THIS ROUTINE REQUIRES TWO ERASABLES (EBUF2, +1) IN UNSWITCHED WHICH ARE UNSHARED BY INTERRUPTS AND
# OTHER EMEMORY PROGRAMS.
#
# A + L ARE PRESERVED THROUGH BANKCALL AND E/BKCALL.

W('13,2036', 0o52134, 'E/BKCALL', 'DXCH', 'BUF2', 'SAVE A,L AND GET DP RETURN.', line=61)
W('13,2037', 0o52365, '', 'DXCH', 'EBUF2', 'SAVE DP RETURN.', line=62)
W('13,2040', 0o24364, '', 'INCR', 'EBUF2', 'RETURN +1 BECAUSE DOUBLE CADR.', line=63)
W('13,2041', 0o30006, '', 'CA', 'BBANK', line=64)
W('13,2042', 0o75054, '', 'MASK', 'LOW10', 'GET CURRENT EBANK.  (SBANK SOMEDAY)', line=65)
W('13,2043', 0o26365, '', 'ADS', 'EBUF2 +1', 'FORM BBCON.  (WAS FBANK)', line=66)
W('13,2044', 0o50364, '', 'NDX', 'EBUF2', line=67)
W('13,2045', 0o27777, '', 'CA', '0 -1', 'GET CADR OF ROUTINE.', line=68)
W('13,2046', 0o04666, '', 'TC', 'SWCALL', 'GO TO ROUTINE, SETTING Q TO SWRETURN', line=69)
# AND RESTORING A + L.
W('13,2047', 0o02053, '', 'TC', '+4', 'TX Q, V34, OR BAD STALL RETURN.', line=71)
W('13,2050', 0o02052, '', 'TC', '+2', 'PROCEED OR GOOD STALL RETURN.', line=72)
W('13,2051', 0o24364, '', 'INCR', 'EBUF2', 'ENTER OR RECYCLE RETURN.', line=73)
W('13,2052', 0o24364, '', 'INCR', 'EBUF2', line=74)
W('13,2053', 0o52365, 'E/SWITCH', 'DXCH', 'EBUF2', line=75)
W('13,2054', 0o52006, '', 'DTCB', line=76)

# Page 421
# E/CALL        FOR CALLING A FIXED MEMORY INTERPRETIVE SUBROUTINE FROM ERASABLE AND RETURNING TO ERASABLE.
#
# THE CALLING SEQUENCE IS...
#
# RTB
# E/CALL
# CADR    ROUTINE                 # THE INTERPRETIVE SUBROUTINE YOU WANT.
# # RETURNS HERE IN INTERPRETIVE.

W('13,2055', 0o22164, 'E/CALL', 'LXCH', 'LOC', 'ADRES -1 OF CADR.', line=88)
W('13,2056', 0o50001, '', 'INDEX', 'L', line=89)
W('13,2057', 0o30001, '', 'CA', 'L', 'CADR IN A.', line=90)
W('13,2060', 0o24001, '', 'INCR', 'L', line=91)
W('13,2061', 0o24001, '', 'INCR', 'L', 'RETURN ADRES IN L.', line=92)
W('13,2062', 0o52365, '', 'DXCH', 'EBUF2', 'STORE CADR AND RETURN.', line=93)
W('13,2063', 0o06006, '', 'TC', 'INTPRET', line=94)
W('13,2064', 0o77624, '', 'CALL', kind='interp', line=95)
W('13,2065', 0o00364, '', '', 'EBUF2', 'INDIRECTLY EXECUTE ROUTING.  IT MUST', kind='operand', line=96)
W('13,2066', 0o77776, '', 'EXIT', '', 'LEAVE VIA RVQ OR EQUIVALENT.', kind='interp', line=97)
W('13,2067', 0o22365, '', 'LXCH', 'EBUF2 +1', 'PICK UP RETURN.', line=98)
W('13,2070', 0o16010, '', 'TCF', 'INTPRET +2', 'SET LOC AND RETURB TO CALLER', line=99)

# Page 422
# E/JOBWAK      FOR WAKING UP ERASABLE MEMORY JOBS.
#
# THIS ROUTINE MUST BE CALLED IN INTERRUPT OR WITH INTERRUPTS INHIBITED.
#
# THE CALLING SEQUENCE IS:
#
# INHINT
# .
# .
# CA      WAKEADR         # ADDRESS OF SLEEPING JOB
# TC      IBNKCALL
# CADR    E/JOBWAK
# .                     # RETURNS HERE
# .
# .
# RELINT                  # IF YOU DID AN INHINT.

#   BANK 33
#   SETLOC E/PROG
#   BANK

#   COUNT* $$/P07

W('04,2606', 0o05201, 'E/JOBWAK', 'TC', 'JOBWAKE', 'ARRIVE IWTH ADRES IN A.', line=125)
W('04,2607', 0o45005, '', 'CS', 'BIT11', line=126)
W('04,2610', 0o50064, '', 'NDX', 'LOCCTR', line=127)
W('04,2611', 0o26164, '', 'ADS', 'LOC', 'KNOCK FIXED MEMORY BIT OUT OF ADRES.', line=128)
W('04,2612', 0o00072, '', 'TC', 'RUPTREG3', 'RETURN', line=129)

# THESE PROGRAMS ARE PROVIDED TO ALLOW OVERLAY OF BANKS 30 THRU 33 OF THE 205 VERSIONS OF SYSTEM TESTS AND
# PRELAUNCH ALIGN.  THE INTENT IS TO ALLOW THE STG AND HYBRID LABS TO RUN ALL THE TESTS WITH COLOSSUS.

#   BANK 33
#   SETLOC TESTLEAD
#   BANK

#   COUNT 33/COMST

#   EBANK= QPLACE

W('33,2000', 0o03436, 'COMPVER', 'TC', 'GCOMPVER', 'MUST BE 33,2000.', line=144)

W('33,2001', 0o03131, 'GTSCPSS1', 'TC', 'GTSCPSS', 'MUST BE AT 33,2001', line=146)

W('33,2002', 0o05354, 'REDO', 'TC', 'NEWMODEX', 'DISPLAY MM 07.', line=148)
W('33,2003', 0o00007, '', 'MM', '07', 'FALL INTO IMUTEST', kind='data', line=149)
