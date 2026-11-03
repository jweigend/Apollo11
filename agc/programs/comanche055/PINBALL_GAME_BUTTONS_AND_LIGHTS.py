"""PINBALL_GAME_BUTTONS_AND_LIGHTS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 307-389 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('PINBALL_GAME_BUTTONS_AND_LIGHTS', 'PINBALL_GAME_BUTTONS_AND_LIGHTS.agc', 'Comanche055', pages='307-389')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     PINBALL_GAME_BUTTONS_AND_LIGHTS.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        307-389
# Mod history:  2009-05-08 RSB  Started adapting from the Colossus249/ file
# of the same name, using Comanche055 page
# images.  Finished through page 329.
# 2009-05-09 RSB  Finished first draft.
# 2009-05-20 RSB  Corrected a CHKPOOH to CHKPOOH.
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

# Page 307
# PROGRAM NAME -- KEYBOARD AND DISPLAY PROGRAM
# MOD NO -- 4           DATE -- 27 APRIL 1967           ASSEMBLY -- PINDISK REV 17
# MOD BY -- FILENE
# LOG SECTION -- PINBALL GAME BUTTONS AND LIGHTS
#
# FUNCTIONAL DESCRIPTION
#
# THE KEYBOARD AND DISPLAY SYSTEM PROGRAM OPERATES UNDER EXECUTIVE
# CONTROL AND PROCESSES INFORMATION EXCHANGED BETWEEN THE AGC AND THE
# COMPUTER OPERATOR.  THE INPUTS TO THE PROGRAM ARE FROM THE KEYBOARD,
# FROM INTERNAL PROGRAM, AND FROM THE UPLINK.
#
# THE LANGUAGE OF COMMUNICATION WITH THE PROGRAM IS A PAIR OF WORDS
# KNOWN AS VERB AND NOUN.  EACH OF THESE IS REPRESENTED BY A 2 CHARACTER
# DECIMAL NUMBER.  THE VERB CODE INDICATES WHAT ACTION IS TO BE TAKEN, THE
# NOUN CODE INDICATES TO WHAT THIS ACTION IS APPLIED.  NOUNS USUALLY
# REFER TO A GROUP OF ERASABLE REGISTERS.
#
# VERBS ARE GROUPED INTO DISPLAYS, LOADS, MONITORS (DISPLAYS THAT ARE
# UPDATED ONCE PER SECOND), SPECIAL FUNCTIONS, AND EXTENDED VERBS (THESE
# ARE OUTSIDE OF THE DOMAIN OF PINBALL AND CAN BE FOUND UNDER LOG SECTION
# `EXTENDED VERBS').
#
# A LIST OF VERBS AND NOUNS IS GIVEN IN LOG SECTION `ASSEMBLY AND
# OPERATION INFORMATION'.
#
# CALLING SEQUENCES --
#
# KEYBOARD:
# EACH DEPRESSION OF A MAIN (NAVIGATION) KEYBOARD BUTTON ACTIVATES
# INTERRUPT KEYRUPT1 (KEYRUPT2) AND PLACES THE 5 BIT KEY CODE INTO
# CHANNEL 15 (CHANNEL 16).  KEYRUPT1 (KEYRUPT2) PLACES THE KEY
# CODE INTO MPAC, ENTERS AN EXECUTIVE REQUEST FOR THE KEYBOARD AND DISPLAY
# PROGRAM (AT `CHARIN'), AND EXECUTES A RESUME.
#
# UPLINK:
# EACH WORD RECEIVED BY THE UPLINK ACTIVATES INTERRUPT UPRUPT, WHICH
# PLACES THE 5 BIT KEY CODE INTO MPAC, ENTERS AN EXECUTIVE REQUEST FOR THE
# KEYBOARD AND DISPLAY PROGRAM (AT `CHARIN') AND EXECUTES A RESUME.
#
# INTERNAL PROGRAMS:
# INTERNAL PROGRAMS CALL PINBALL AT `NVSUB' WITH THE DESIRED VERB/NOUN
# CODE IN A (LOW 7 BITS FOR NOUN, NEXT 7 BITS FOR VERB).  DETAILS
# DESCRIBED ON REMARKS CARDS JUST BEFORE `NVSUB' AND `NVSBWAIT' (SEE
# SYMBOL TABLE FOR PAGE NUMBERS).
#
# NORMAL EXIT MODES --
#
# IF PINBALL WAS CALLED BY EXTERNAL ACTION, THERE ARE FOUR EXITS:
# 1)      ALL BUT (2), (3), AND (4) EXIT DIRECTLY TO ENDOFJOB.
# Page 308
# 2)      EXTENDED VERBS TO TO THE EXTENDED VERB FAN AS PART OF THE
# PINBALL EXECUTIVE JOB WITH PRIORITY 30000.  IT IS THE
# RESPONSIBILITY OF THE EXTENDED VERB CALLED TO EVENTUALLY
# CHANGE PRIORITY (IF NECESSARY) AD DO AN ENDOFJOB.
# ALSO PINBALL IS A NOVAC JOB.  EBANK SET FOR COMMON.
# 3)      VERB 37.  CHANGE OF PROGRAM (MAJOR MODE) CALLS `V37' IN THE
# SERVICE ROUTINES AS PART OF THE PINBALL EXEC JOB WITH PRIO
# 30000.  THE NEW PROGRAM CODE (MAJOR MODE) IS LEFT IN A.
# 4)      KEY RELEASE BUTTON CALLS `PINBRNCH' IN THE DISPLAY INTERFACE
# ROUTINES AS PART OF THE PINBALL EXEC JOB WITH PRIO 30000 IF
# THE KEY RELEASE LIGHT IS OFF AND `CADRSTOR' IS NOT 40.
#
# IF PINBALL WAS CALLED BY INTERNAL PROGRAMS, EXIT FROM PINBALL IS BACK
# TO CALLING ROUTINE.  DETAILS DESCRIBED IN REMARKS CARDS JUST BEFORE
# `NVSUB' AND `NVSBWAIT' (SEE SYMBOL TABLE FOR PAGE NUMBERS).
#
# ALARM OR ABORT EXIT MODES --
#
# EXTERNAL INITIATION:
# IF SOME IMPROPER SEQUENCE OF KEY CODES IS DETECTED, THE OPERATOR
# ERROR LIGHT IS TURNED ON AND EXIT IS TO `ENDOFJOB'.
#
# INTERNAL PROGRAM INITIATION:
# IF AN ILLEGAL V/N COMBINATION IS ATTEMPTED, AN ABORT IS CAUSED
# (WITH OCTAL 01501).
# IF A SECOND ATTEMPT IS MADE TO GO TO SLEEP IN PINBALL, AN ABORT IS
# CAUSED (WITH OCTAL 01206).  THERE ARE TWO WAYS TO GO TO SLEEP IN PINBALL:
# 1)      ENDIDLE OR DATAWAIT.
# 2)      NVSBWAIT, PRENVBSY, OR NVSUBUSY.
#
# CONDITIONS LEADING TO THE ABOVE ARE DESCRIBED IN FORTHCOMING MIT/IL
# E-REPORT DESCRIBING KEYBOARD AND DISPLAY OPERATION FOR 278.
#
# OUTPUT --
#
# INFORMATION TO BE SENT TO THE DISPLAY PANEL IS LEFT IN THE `DSPTAB'
# BUFFERS REGISTERS (UNDER EXEC CONTROL).  `DSPOUT' (A PART OF T4RUPT)
# HANDLES THE PLACING OF THE `DSPTAB' INFORMATION INTO OUTPUT CHANNEL 10
# IN INTERRUPT.
#
# ERASABLE INITIALIZATION --
#
# FRESH START AND RESTART INITIALIZE THE NECESSARY E REGISTERS FOR
# PINBALL IN `STARTSUB'.  REGISTERS ARE:  DSPTAB BUFFER, CADRSTOR,
# REQRET, CLPASS, DSPLOCK, MONSAVE, MONSAVE1, VERBREG, NOUNREG, DSPLIST,
# DSPCOUNT, NOUT.
#
# Page 309
# A COMPLETE LIST OF ALL THE ERASABLES (BOTH RESERVED AND TEMPORARIES) FOR
# PINBALL IS GIVEN BELOW.
#
# THE FOLLOWING ARE OF GENERAL INTEREST --
#
# REMARKS CARDS PRECEDE THE REFERENCED SYMBOL DEFINITION.  SEE SYMBOL
# TABLE TO FIND APPROPRIATE PAGE NUMBERS.
#
# NVSUB           CALLING POINT FOR INTERNAL USE OF PINBALL.
# OF RELATED INTEREST     NVSBWAIT
# NVSUBUSY
# PRENVBSY
#
# ENDIDLE         ROUTINE FOR INTERNAL PROGRAMS WISHING TO TO SLEEP WHILE
# AWAITING OPERATOR'S RESPONSE.
#
# DSPMM           ROUTINE BY WHICH AN INTERNAL PROGRAM MAY DISPLAY A DECIMAL
# PROGRAM CODE (MAJOR MODE) IN THE PROGRAM (MAJOR MODE) LIGHT
# (DSPMM DOES NOT DISPLAY DIRECTLY BUT ENTERS EXEC REQUEST
# FOR DSPMMJB WITH PRIO 30000 AND RETURNS TO CALLER.)
#
# BLANKSUB        ROUTINE BY WHICH AN INTERNAL PROGRAM MAY BLANK ANY
# COMBINATION OF THE DISPLAY REGISTERS R1, R2, R3.
#
# JAMTERM         ROUTINE BY WHICH AN INTERNAL PROGRAM MAY PERFORM THE
# JAMPROC         TERMINATE (V 34) OR PROCEED (V33) FUNCTION.
#
# MONITOR         VERBS FOR PERIODIC (1 PER SEC) DISPLAY.
#
# PLEASE PERFORM, PLEASE MARK SITUATIONS
# REMARKS DESCRIBING HOW AN INTERNAL ROUTINE SHOULD HANDLE
# THESE SITUATIONS CAN BE FOUND JUST BEFORE `NVSUB' (SEE
# SYMBOL TABLE FOR PAGE NUMBER).
#
# THE NOUN TABLE FORMAT IS DESCRIBED ON A PAGE OF REMARKS CARDS JUST
# BEFORE `DSPABC' (SEE SYMBOL TABLE FOR PAGE NUMBER).
#
# THE NOUN TABLES THEMSELVES ARE FOUND IN LOG SECTION `PINBALL NOUN
# TABLES'.
#
# FOR FURTHER DETAILS ABOUT OPERATION OF THE KEYBOARD AND DISPLAY SYSTEM
# PROGRAM, SEE THE MISSION PLAN AND/OR MIT/IL E-2129
# DESCRIBING KEYBOARD AND DISPLAY OPERATION FOR 278.
# (Note that this doc by Green and Filene is/was available online at
# http://hrst.mit.edu/hrs/apollo/public/archive/1706.pdf --- RSB 6/2004.)
#
# THE FOLLOWING QUOTATION IS PROVIDED THROUGH THE COURTESY OF THE AUTHORS.
#
# "IT WILL BE PROVED TO THY FACE THAT THOU HAST MEN ABOUT THEE THAT
# Page 310
# USUALLY TALK OF A NOUN AND A VERB, AND SUCH ABOMINABLE WORDS AS NO
# CHRISTIAN EAR CAN ENDURE TO HEAR."
# HENRY 6, ACT 2, SCENE 4

# THE FOLLOWING ASSIGNMENTS FOR PINBALL ARE MADE ELSEWHERE

# RESERVED FOR PINBALL EXECUTIVE ACTION
#
# DSPCOUNT       ERASE                   # DISPLAY POSITION INDICATOR
# DECBRNCH       ERASE                   # +DEC, -DEC, OCT INDICATOR
# VERBREG        ERASE                   # VERB CODE
# NOUNREG        ERASE                   # NOUN CODE
# XREG           ERASE                   # R1 INPUT BUFFER
# YREG           ERASE                   # R2 INPUT BUFFER
# ZREG           ERASE                   # R3 INPUT BUFFER
# XREGLP         ERASE                   # LO PART OF XREG (FOR DEC CONV ONLY)
# YREGLP         ERASE                   # LO PART OF YREG (FOR DEC CONV ONLY)
# HITEMOUT       =       YREGLP          # TEMP FOR DISPLAY OF HRS,MIN,SEC
# # MUST = LOTEMOUT-1.
# ZREGLP         ERASE                   # LO PART OF ZREG (FOR DEC CONV ONLY)
# LOTEMOUT       =       ZREGLP          # TEMP FOR DISPLAY OF HRS,MIN,SEC
# # MUST = HITEMOUT+1
# MODREG         ERASE                   # MODE CODE
# DSPLOCK        ERASE                   # KEYBOARD/SUBROUTINE CALL INTERLOCK
# REQRET         ERASE                   # RETURN REGISTER FOR LOAD
# LOADSTAT       ERASE                   # STATUS INDICATOR FOR LOADTST
# CLPASS         ERASE                   # PASS INDICATOR FOR CLEAR
# NOUT           ERASE                   # ACTIVITY COUNTER FOR DSPTAB
# NOUNCADR       ERASE                   # MACHINE CADR FOR NOUN
# MONSAVE        ERASE                   # N/V CODE FOR MONITOR. (= MONSAVE1-1)
# MONSAVE1       ERASE                   # NOUNCADR FOR MONITOR (MATBS1) = MONSAVE+1
# MONSAVE2       ERASE                   # NVMONOPT OPTIONS
# DSPTAB         ERASE   +13D            # 0-10, DISPLAY PANEL BUFFER 11-13, C RELAYS.
# CADRSTOR       ERASE                   # ENDIDLE STORAGE
# NVQTEM         ERASE                   # NVSUB STORAGE FOR CALLING ADDRESS
# # MUST = NVBNKTEM-1.
# NVBNKTEM       ERASE                   # NVSUB STORAGE FOR CALLING BANK
# # MUST = NVQTEM+1
# VERBSAVE       ERASE                   # NEEDED FOR RECYCLE
# DSPLIST        ERASE                   # WAITING REG FOR DSP SYST INTERNAL USE
# EXTVBACT       ERASE                   # EXTENDED VERB ACTIVITY INTERLOCK
# DSPTEM1        ERASE   +2              # BUFFER STORAGE AREA 1 (MOSTLY FOR TIME)
# DSPTEM2        ERASE   +2              # BUFFER STORAGE AREA 2 (MOSTLY FOR DEG)
#
# END OF ERASABLES RESERVED FOR PINBALL EXECUTIVE ACTION.
#
# TEMPORARIES FOR PINBALL EXECUTIVE ACTION
# Page 311
# DSEXIT         =       INTB15+         # RETURN FOR DSPIN
# EXITEM         =       INTB15+         # RETURN FOR SCALE FACTOR ROUTINE SELECT
# BLANKRET       =       INTB15+         # RETURN FOR 2BLANK
# WRDRET         =       INTBIT15        # RETURN FOR 5BLANK.
# WDRET          =       INTBIT15        # RETURN FOR DSPWD
# DECRET         =       INTBIT15        # RETURN FOR PUTCOM(DEC LOAD)
# 21/22REG       =       INTBIT15        # TEMP FOR CHARIN
# UPDATRET       =       POLISH          # RETURN FOR UPDATNN, UPDATVB
# CHAR           =       POLISH          # TEMP FOR CHARIN
# ERCNT          =       POLISH          # COUNTER FOR ERROR LIGHT RESET
# DECOUNT        =       POLISH          # COUNTER FOR SCALING AND DISPLAY (DEC)
# SGNON          =       VBUF            # TEMP FOR +,- ON
# NOUNTEM        =       VBUF            # COUNTER FOR MIXNOUN FETCH
# DISTEM         =       VBUF            # COUNTER FOR OCTAL DISPLAY VERB
# DECTEM         =       VBUF            # COUNTER FOR FETCH (DEC DISPLAY VERBS)
# SGNOFF         =       VBUF +1         # TEMP FOR +,- ON
# NVTEMP         =       VBUF +1         # TEMP FOR NVSUB
# SFTEMP1        =       VBUF +1         # STORAGE FOR SF CONST HI PART (=SFTEMP2-1)
# HITEMIN        =       VBUF +1         # TEMP FOR LOAD OF HRS,MIN,SEC
# #       MUST = LOTEMIN-1.
# CODE           =       VBUF +2         # FOR DSPIN
# SFTEMP2        =       VBUF +2         # STORAGE FOR SF CONST LO PART (=SFTEMP1+1)
# LOTEMIN        =       VBUF +2         # TEMP FOR LOAD OF HRS,MIN,SEC
# #       MUST = HITEMIN+1
# MIXTEMP        =       VBUF +3         # FOR MIXNOUN DATA
# SIGNRET        =       VBUF +3         # RETURN FOR +,- ON
# ALSO MIXTEMP+1 = VBUF+4, MIXTEMP+2 = VBUF+5
# ENTRET         =       DOTINC          # EXIT FROM ENTER
# WDONT          =       DOTRET          # CHAR COUNTER FOR DSPWD
# INREL          =       DOTRET          # INPUT BUFFER SELECTOR (X,Y,Z, REG )
# DSPMMTEM       =       MATINC          # DSPCOUNT SAVE FOR DSPMM
# MIXBR          =       MATINC          # INDICATOR FOR MIXED OR NORMAL NOUN
# TEM1           ERASE                   # EXEC TEMP
# DSREL          =       TEM1            # REL ADDRESS FOR DSPIN
# TEM2           ERASE                   # EXEC TEMP
# DSMAG          =       TEM2            # MAGNITUDE STORE FOR DSPIN
# IDADDTEM       =       TEM2            # MIXNOUN INDIRECT ADDRESS STORAGE
# TEM3           ERASE                   # EXEC TEMP
# COUNT          =       TEM3            # FOR DSPIN
# Page 312
# TEM4           ERASE                   # EXEC TEMP
# LSTPTR         =       TEM4            # LIST POINTER FOR GRABUSY
# RELRET         =       TEM4            # RETURN FOR RELDSP
# FREERET        =       TEM4            # RETURN FOR FREEDSP
# DSPWDRET       =       TEM4            # RETURN FOR DSPSIGN
# SEPSCRET       =       TEM4            # RETURN FOR SEPSEC
# SEPMNRET       =       TEM4            # RETURN FOR SEPMIN
# TEM5           ERASE                   # EXEC TEMP
# NOUNADD        =       TEM5            # TEMP STORAGE FOR NOUN ADDRESS
# NNADTEM        ERASE                   # TEMP FOR NOUN ADDRESS TABLE ENTRY
# NNTYPTEM       ERASE                   # TEMP FOR NOUN TYPE TABLE ENTRY
# IDAD1TEM       ERASE                   # TEMP FOR INDIR ADDRESS TABLE ENTRY (MIXNN)
# # MUST = IDAD2TEM-1, = IDAD3TEM-2
# IDAD2TEM       ERASE                   # TEMP FOR INDIR ADDRESS TABLE ENTRY (MIXNN)
# # MUST = IDAD1TEM+1, IDAD3TEM-1.
# IDAD3TEM       ERASE                   # TEMP FOR INDIR ADDRESS TABLE ENTRY (MIXNN)
# # MUST = IDAD1TEM+2, IDAD2TEM+1.
# RUTMXTEM       ERASE                   # TEMP FOR SF ROUT TABLE ENTRY (MIXNN ONLY)
#
# END OF TEMPORARIES FOR PINBALL EXECUTIVE ACTION.
#
# ADDITIONAL TEMPORARIES FOR PINBALL EXECUTIVE ACTION
#
# MPAC, THRU MPAC +6
# BUF, +1, +2
# BUF2, +1, +2
# MPTEMP
# ADDRWD
#
# END OF ADDITIONAL TEMPS FOR PINBALL EXEC ACTION
#
# RESERVED FOR PINBALL INTERRUPT ACTION
#
# DSPCNT         ERASE                   # COUNTER FOR DSPOUT
# UPLOCK         ERASE                   # BIT1 = UPLINK INTERLOCK (ACTIVATED BY
# # RECEPTION OF A BAD MESSAGE IN UPLINK)
#
# END OF ERASABLES RESERVED FOR PINBALL INTERRUPT ACTION
#
# TEMPORARIES FOR PINBALL INTERRUPT ACTION
#
# KEYTEMP1       =       WAITEXIT        # TEMP FOR KEYRUPT, UPRUPT
# DSRUPTEM       =       WAITEXIT        # TEMP FOR DSPOUT
# KEYTEMP2       =       RUPTAGN         # TEMP FOR KEYRUPT, UPRUPT
#
# END OF TEMPORARIES FOR PINBALL INTERRUPT ACTION

# Page 313
# THE INPUT CODES ASSUMED FOR THE KEYBOARD ARE,
# 0               10000
# 1               00001
# 9               01001
# VERB            10001
# ERROR RES       10010
# KEY RLSE        11001
# +               11010
# -               11011
# ENTER           11100
# CLEAR           11110
# NOUN            11111
#
# OUTPUT FORMAT FOR DISPLAY PANEL.  SET OUT0 TO AAAABCCCCCDDDDD.
# A'S   SELECTS A RELAYWORD.  THIS DETERMINES WHICH PAIR OF CHARACTERS ARE
# ENERGIZED.
# B     FOR SPECIAL RELAYS SUCH AS SIGNS ETC.
# C'S   5 BIT RELAY CODE FOR LEFT CHAR OF PAIR SELECTED BY RELAYWORD.
# D'S   5 BIT RELAY CODE FOR RIGHT CHAR OF PAIR SELECTED BY RELAYWORD.
#
# THE PANEL APPEARS AS FOLLOWS,
# MD1             MD2 (MAJOR MODE)
# VD1             VD2 (VERB)                      ND1             ND2 (NOUN)
# R1D1            R1D2            R1D3            R1D4            R1D5 (R1)
# R2D1            R2D2            R2D3            R2D4            R2D5 (R2)
# R3D1            R3D2            R3D3            R3D4            R3D5 (R3)
#
# EACH OF THESE IS GIVEN A DSPCOUNT NUMBER FOR USE WITHIN COMPUTATION ONLY
#
# MD1     25              R2D1    11              ALL ARE OCTAL
# MD2     24              R2D2    10
# VD1     23              R2D3    7
# VD2     22              R2D4    6
# ND1     21              R2D5    5
# ND2     20              R3D1    4
# R1D1    16              R3D2    3
# R1D2    15              R3D3    2
# R1D3    14              R3D4    1
# R1D4    13              R3D5    0
# R1D5    12
#
# THERE IS AN 11-REGISTER TABLE (DSPTAB) FOR THE DISPLAY PANEL.
#
# DSPTAB          RELAYWD         BIT11           BITS 10-6       BITS 5-1
# RELADD
# 10              1011                            MD1 (25)        MD2  (24)
# 9               1010                            VD1 (23)        VD2  (22)
# 8               1001                            ND1 (21)        ND2  (20)
# 7               1000                                            R1D1 (16)
# Page 314
# 6               0111            +R1             R1D2 (15)       R1D3 (14)
# 5               0110            -R1             R1D4 (13)       R1D5 (12)
# 4               0101            +R2             R2D1 (11)       R2D2 (10)
# 3               0100            -R2             R2D3 (7)        R2D4 (6)
# 2               0011                            R2D5 (5)        R3D1 (4)
# 1               0010            +R3             R3D2 (3)        R3D3 (2)
# 0               0001            -R3             R3D4 (1)        R3D5 (0)
# 0000        NO RELAYWORD
#
# THE 5-BIT OUTOUT RELAY CODES ARE:
#
# BLANK   00000
# 0       10101
# 1       00011
# 2       11001
# 3       11011
# 4       01111
# 5       11110
# 6       11100
# 7       10011
# 8       11101
# 9       11111
#
# OUTPUT BITS USED BY PINBALL:
#
# KEY RELEASE LIGHT       --      BIT 5 OF CHANNEL 11
# VERB/NOUN FLASH         --      BIT 6 OF CHANNEL 11
# OPERATOR ERROR LIGHT    --      BIT 7 OF CHANNEL 11

# Page 315
# START OF EXECUTIVE SECTION OF PINBALL

#   BANK 40
#   SETLOC PINBALL1
#   BANK

#   COUNT 40/PIN

W('40,2000', 0o35017, 'CHARIN', 'CAF', 'ONE', 'BLOCK DISPLAY SYST', line=407)
W('40,2001', 0o57012, '', 'XCH', 'DSPLOCK', 'MAKE DSP SYST BUSY, BUT SAVE OLD', line=408)
W('40,2002', 0o54115, '', 'TS', '21/22REG', 'C(DSPLOCK) FOR ERROR LIGHT RESET.', line=409)
W('40,2003', 0o11042, '', 'CCS', 'CADRSTOR', 'ALL KEYS EXCEPT ER TURN ON KR LITE IF', line=410)
W('40,2004', 0o02006, '', 'TC', '+2', 'CADRSTOR IS FULL.  THIS REMINDS OPERATOR', line=411)
W('40,2005', 0o02013, '', 'TC', 'CHARIN2', 'TO RE-ESTABLISH A FLASHING DISPLAY', line=412)
W('40,2006', 0o42057, '', 'CS', 'ELRCODE1', 'WHICH HE HAS OBSCURED WITH DISPLAYS OF', line=413)
W('40,2007', 0o60154, '', 'AD', 'MPAC', 'HIS OWN (SEE REMARKS PRECEDING ROUTINE', line=414)
W('40,2010', 0o00006, '', 'EXTEND', '', 'VBRELDSP).', line=415)
W('40,2011', 0o12013, '', 'BZF', 'CHARIN2', line=416)
W('40,2012', 0o04410, '', 'TC', 'RELDSPON', line=417)
W('40,2013', 0o56154, 'CHARIN2', 'XCH', 'MPAC', line=418)
W('40,2014', 0o54117, '', 'TS', 'CHAR', line=419)
W('40,2015', 0o50000, '', 'INDEX', 'A', line=420)
W('40,2016', 0o02017, '', 'TC', '+1', '  INPUT CODE      FUNCTION', line=421)
W('40,2017', 0o03341, '', 'TC', 'CHARALRM', '      0', line=422)
W('40,2020', 0o02076, '', 'TC', 'NUM', '      1', line=423)
W('40,2021', 0o02076, '', 'TC', 'NUM', '      2', line=424)
W('40,2022', 0o02076, '', 'TC', 'NUM', '      3', line=425)
W('40,2023', 0o02076, '', 'TC', 'NUM', '      4', line=426)
W('40,2024', 0o02076, '', 'TC', 'NUM', '      5', line=427)
W('40,2025', 0o02076, '', 'TC', 'NUM', '      6', line=428)
W('40,2026', 0o02076, '', 'TC', 'NUM', '      7', line=429)
W('40,2027', 0o02062, '', 'TC', '89TEST', '      10              8', line=430)
W('40,2030', 0o02062, '', 'TC', '89TEST', '      11              9', line=431)
W('40,2031', 0o03341, '', 'TC', 'CHARALRM', '      12', line=432)
W('40,2032', 0o03341, '', 'TC', 'CHARALRM', '      13', line=433)
W('40,2033', 0o03341, '', 'TC', 'CHARALRM', '      14', line=434)
W('40,2034', 0o03341, '', 'TC', 'CHARALRM', '      15', line=435)
W('40,2035', 0o03341, '', 'TC', 'CHARALRM', '      16', line=436)
W('40,2036', 0o03341, '', 'TC', 'CHARALRM', '      17', line=437)
W('40,2037', 0o02074, '', 'TC', 'NUM -2', '      20              0', line=438)
W('40,2040', 0o02255, '', 'TC', 'VERB', '      21              VERB', line=439)
W('40,2041', 0o03510, '', 'TC', 'ERROR', '      22              ERROR LIGHT RESET', line=440)
W('40,2042', 0o03341, '', 'TC', 'CHARALRM', '      23', line=441)
W('40,2043', 0o03341, '', 'TC', 'CHARALRM', '      24', line=442)
W('40,2044', 0o03341, '', 'TC', 'CHARALRM', '      25', line=443)
W('40,2045', 0o03341, '', 'TC', 'CHARALRM', '      26', line=444)
W('40,2046', 0o03341, '', 'TC', 'CHARALRM', '      27', line=445)
W('40,2047', 0o03341, '', 'TC', 'CHARALRM', '      30', line=446)
W('40,2050', 0o03366, '', 'TC', 'VBRELDSP', '      31              KEY RELEASE', line=447)
# Page 316
W('40,2051', 0o02310, '', 'TC', 'POSGN', '      32              +', line=449)
W('40,2052', 0o02275, '', 'TC', 'NEGSGN', '      33              -', line=450)
W('40,2053', 0o02060, '', 'TC', 'ENTERJMP', '      34              ENTER', line=451)
W('40,2054', 0o03341, '', 'TC', 'CHARALRM', '      35', line=452)
W('40,2055', 0o02370, '', 'TC', 'CLEAR', '      36              CLEAR', line=453)
W('40,2056', 0o02271, '', 'TC', 'NOUN', '      37              NOUN', line=454)

W('40,2057', 0o00022, 'ELRCODE1', 'OCT', '22', kind='data', line=456)
W('40,2060', 0o04701, 'ENTERJMP', 'TC', 'POSTJUMP', line=457)
W('40,2061', 0o62002, '', 'CADR', 'ENTER', kind='data', line=458)

W('40,2062', 0o10777, '89TEST', 'CCS', 'DSPCOUNT', line=460)
W('40,2063', 0o02067, '', 'TC', '+4', '+', line=461)
W('40,2064', 0o02067, '', 'TC', '+3', '+0', line=462)
W('40,2065', 0o05217, '', 'TC', 'ENDOFJOB', '- BLOCK DATA IN IF DSPCOUNT IS - OR -0', line=463)
W('40,2066', 0o05217, '', 'TC', 'ENDOFJOB', '-0', line=464)
W('40,2067', 0o36214, '', 'CAF', 'THREE', line=465)
W('40,2070', 0o71000, '', 'MASK', 'DECBRNCH', line=466)
W('40,2071', 0o10000, '', 'CCS', 'A', line=467)
W('40,2072', 0o02076, '', 'TC', 'NUM', 'IF DECBRNCH IS +, 8 OR 9 OK', line=468)
W('40,2073', 0o03341, '', 'TC', 'CHARALRM', 'IF DECBRNCH IS +0, REJECT 8 OR 9', line=469)

# NUM ASSEMBLES OCTAL 3 BITS AT A TIME.  FOR DECIMAL IT CONVERTS INCOMING
# WORD AS A FRACTION, KEEPING RESULTS TO DP.
# OCTAL RESULTS ARE LEFT IN XREG, YREG, OR ZREG.  HI PART OF DEC IN XREG,
# YREG, ZREG.  THE LOW PARTS IN XREGLP, YREGLP, OR ZREGLP.
# DECBRNCH IS LEFT AT +0 FOR OCT, +1 FOR + DEC, +2 FOR - DEC.
# IF DSPCOUNT WAS LEFT -, NO MORE DATA IS ACCEPTED.

W('40,2074', 0o35021, '', 'CAF', 'ZERO', line=478)
W('40,2075', 0o54117, '', 'TS', 'CHAR', line=479)
W('40,2076', 0o10777, 'NUM', 'CCS', 'DSPCOUNT', line=480)
W('40,2077', 0o02103, '', 'TC', '+4', '+', line=481)
W('40,2100', 0o02103, '', 'TC', '+3', '+0', line=482)
W('40,2101', 0o02102, '', 'TC', '+1', '-BLOCK DATA IN IF DSPCOUNT IS -', line=483)
W('40,2102', 0o05217, '', 'TC', 'ENDOFJOB', '-0', line=484)
W('40,2103', 0o02225, '', 'TC', 'GETINREL', line=485)
W('40,2104', 0o11015, '', 'CCS', 'CLPASS', 'IF CLPASS IS + OR +0, MAKE IT +0.', line=486)
W('40,2105', 0o35021, '', 'CAF', 'ZERO', line=487)
W('40,2106', 0o55015, '', 'TS', 'CLPASS', line=488)
W('40,2107', 0o02110, '', 'TC', '+1', line=489)
W('40,2110', 0o50117, '', 'INDEX', 'CHAR', line=490)
W('40,2111', 0o34072, '', 'CAF', 'RELTAB', line=491)
W('40,2112', 0o74362, '', 'MASK', 'LOW5', line=492)
W('40,2113', 0o54124, '', 'TS', 'CODE', line=493)
W('40,2114', 0o30777, '', 'CA', 'DSPCOUNT', line=494)
W('40,2115', 0o54143, '', 'TS', 'COUNT', line=495)
W('40,2116', 0o03227, '', 'TC', 'DSPIN', line=496)
# Page 317
W('40,2117', 0o36214, '', 'CAF', 'THREE', line=498)
W('40,2120', 0o71000, '', 'MASK', 'DECBRNCH', line=499)
W('40,2121', 0o10000, '', 'CCS', 'A', '+0, OCTAL.  +1, + DEC.  +2, - DEC.', line=500)
W('40,2122', 0o02133, '', 'TC', 'DECTOBIN', '+', line=501)
W('40,2123', 0o50137, '', 'INDEX', 'INREL', '+0 OCTAL', line=502)
W('40,2124', 0o57001, '', 'XCH', 'VERBREG', line=503)
W('40,2125', 0o54022, '', 'TS', 'CYL', line=504)
W('40,2126', 0o40022, '', 'CS', 'CYL', line=505)
W('40,2127', 0o40022, '', 'CS', 'CYL', line=506)
W('40,2130', 0o56022, '', 'XCH', 'CYL', line=507)
W('40,2131', 0o60117, '', 'AD', 'CHAR', line=508)
W('40,2132', 0o02150, '', 'TC', 'ENDNMTST', line=509)
W('40,2133', 0o50137, 'DECTOBIN', 'INDEX', 'INREL', line=510)
W('40,2134', 0o57001, '', 'XCH', 'VERBREG', line=511)
W('40,2135', 0o54154, '', 'TS', 'MPAC', 'SUM X 2EXP-14 IN MPAC', line=512)
W('40,2136', 0o35021, '', 'CAF', 'ZERO', line=513)
W('40,2137', 0o54155, '', 'TS', 'MPAC +1', line=514)
W('40,2140', 0o34377, '', 'CAF', 'TEN', '10 X 2EXP-14', line=515)
W('40,2141', 0o07256, '', 'TC', 'SHORTMP', '10SUM X 2EXP-28 IN MPAC, MPAC+1', line=516)
W('40,2142', 0o56155, '', 'XCH', 'MPAC +1', line=517)
W('40,2143', 0o60117, '', 'AD', 'CHAR', line=518)
W('40,2144', 0o54155, '', 'TS', 'MPAC +1', line=519)
W('40,2145', 0o02150, '', 'TC', 'ENDNMTST', 'NO OF', line=520)
W('40,2146', 0o26154, '', 'ADS', 'MPAC', 'OF MUST BE 5TH CHAR', line=521)
W('40,2147', 0o02166, '', 'TC', 'DECEND', line=522)
W('40,2150', 0o50137, 'ENDNMTST', 'INDEX', 'INREL', line=523)
W('40,2151', 0o55001, '', 'TS', 'VERBREG', line=524)
W('40,2152', 0o40777, '', 'CS', 'DSPCOUNT', line=525)
W('40,2153', 0o50137, '', 'INDEX', 'INREL', line=526)
W('40,2154', 0o62216, '', 'AD', 'CRITCON', line=527)
W('40,2155', 0o00006, '', 'EXTEND', line=528)
W('40,2156', 0o12160, '', 'BZF', 'ENDNUM', '-0, DSPCOUNT = CRITCON', line=529)
W('40,2157', 0o02213, '', 'TC', 'MORNUM', '-, DSPCOUNT G/ CRITCON', line=530)
W('40,2160', 0o36214, 'ENDNUM', 'CAF', 'THREE', line=531)
W('40,2161', 0o71000, '', 'MASK', 'DECBRNCH', line=532)
W('40,2162', 0o10000, '', 'CCS', 'A', line=533)
W('40,2163', 0o02166, '', 'TC', 'DECEND', line=534)
W('40,2164', 0o40777, 'ENDALL', 'CS', 'DSPCOUNT', 'BLOCK NUMIN BY PLACING DSPCOUNT', line=535)
W('40,2165', 0o02214, '', 'TC', 'MORNUM +1', 'NEGATIVELY', line=536)
W('40,2166', 0o45017, 'DECEND', 'CS', 'ONE', line=537)
W('40,2167', 0o60137, '', 'AD', 'INREL', line=538)
W('40,2170', 0o00006, '', 'EXTEND', line=539)
W('40,2171', 0o62164, '', 'BZMF', 'ENDALL', 'IF INREL=0,1 (VBREG,NNREG) LEAVE WHOLE', line=540)
W('40,2172', 0o07052, '', 'TC', 'DMP', 'IF INREL=2,3,4 (R1,R2,R3), CONVERT TO FRAC', line=541)
# MULT SUM X 2EXP-28 IN MPAC, MPAC+1 BY
W('40,2173', 0o02223, '', 'ADRES', 'DECON', '2EXP14/10EXP5, GIVES (SUM/10EXP5)X2EXP-14', kind='data', line=543)
W('40,2174', 0o36214, '', 'CAF', 'THREE', 'IN MPAC, +1, +2.', line=544)
W('40,2175', 0o71000, '', 'MASK', 'DECBRNCH', line=545)
W('40,2176', 0o50000, '', 'INDEX', 'A', line=546)
W('40,2177', 0o02177, '', 'TC', '+0', line=547)
# Page 318
W('40,2200', 0o02204, '', 'TC', '+DECSGN', line=549)
W('40,2201', 0o00006, '', 'EXTEND', '', '- CASE', line=550)
W('40,2202', 0o40156, '', 'DCS', 'MPAC +1', line=551)
W('40,2203', 0o52156, '', 'DXCH', 'MPAC +1', line=552)
W('40,2204', 0o56156, '+DECSGN', 'XCH', 'MPAC +2', line=553)
W('40,2205', 0o50137, '', 'INDEX', 'INREL', line=554)
W('40,2206', 0o55004, '', 'TS', 'XREGLP -2', line=555)
W('40,2207', 0o56155, '', 'XCH', 'MPAC +1', line=556)
W('40,2210', 0o50137, '', 'INDEX', 'INREL', line=557)
W('40,2211', 0o55001, '', 'TS', 'VERBREG', line=558)
W('40,2212', 0o02164, '', 'TC', 'ENDALL', line=559)
W('40,2213', 0o10777, 'MORNUM', 'CCS', 'DSPCOUNT', 'DECREMENT DSPCOUNT', line=560)
W('40,2214', 0o54777, '', 'TS', 'DSPCOUNT', line=561)
W('40,2215', 0o05217, '', 'TC', 'ENDOFJOB', line=562)

W('40,2216', 0o00022, 'CRITCON', 'OCT', '22', '(DEC 18)', kind='data', line=564)
W('40,2217', 0o00020, '', 'OCT', '20', '(DEC 16)', kind='data', line=565)
W('40,2220', 0o00012, '', 'OCT', '12', '(DEC 10)', kind='data', line=566)
W('40,2221', 0o00005, '', 'OCT', '5', kind='data', line=567)
W('40,2222', 0o00000, '', 'OCT', '0', kind='data', line=568)

W('40,2223', 0o05174, 'DECON', '2DEC', 'E-5 B14', '2EXP14/10EXP5 = .16384 DEC', kind='data', line=570)
W('40,2224', 0o13261, kind='data', line=570)

# GETINREL GETS PROPER DATA REG REL ADDRESS FOR CURRENT C(DSPCOUNT) AND
# PUTS IN INTO INREL. +0 VERBREG, 1 NOUNREG, 2 XREG, 3 YREG, 4 ZREG.

W('40,2225', 0o50777, 'GETINREL', 'INDEX', 'DSPCOUNT', line=576)
W('40,2226', 0o32231, '', 'CAF', 'INRELTAB', line=577)
W('40,2227', 0o54137, '', 'TS', 'INREL', '(A TEMP, REG)', line=578)
W('40,2230', 0o00002, '', 'TC', 'Q', line=579)

W('40,2231', 0o00004, 'INRELTAB', 'OCT', '4', 'R3D5 (DSPCOUNT = 0)', kind='data', line=581)
W('40,2232', 0o00004, '', 'OCT', '4', 'R3D4           =(1)', kind='data', line=582)
W('40,2233', 0o00004, '', 'OCT', '4', 'R3D3           =(2)', kind='data', line=583)
W('40,2234', 0o00004, '', 'OCT', '4', 'R3D2           =(3)', kind='data', line=584)
W('40,2235', 0o00004, '', 'OCT', '4', 'R3D1           =(4)', kind='data', line=585)
W('40,2236', 0o00003, '', 'OCT', '3', 'R2D5           =(5)', kind='data', line=586)
W('40,2237', 0o00003, '', 'OCT', '3', 'R2D4           =(6)', kind='data', line=587)
W('40,2240', 0o00003, '', 'OCT', '3', 'R2D3           =(7)', kind='data', line=588)
W('40,2241', 0o00003, '', 'OCT', '3', 'R2D2           =(8D)', kind='data', line=589)
W('40,2242', 0o00003, '', 'OCT', '3', 'R2D1           =(9D)', kind='data', line=590)
W('40,2243', 0o00002, '', 'OCT', '2', 'R1D5           =(10D)', kind='data', line=591)
W('40,2244', 0o00002, '', 'OCT', '2', 'R1D4           =(11D)', kind='data', line=592)
W('40,2245', 0o00002, '', 'OCT', '2', 'R1D3           =(12D)', kind='data', line=593)
W('40,2246', 0o00002, '', 'OCT', '2', 'R1D2           =(13D)', kind='data', line=594)
W('40,2247', 0o00002, '', 'OCT', '2', 'R1D1           =(14D)', kind='data', line=595)
W('40,2250', 0o05747, '', 'TC', 'CCSHOLE', 'NO DISCOUNT NUMBER = 15D', line=596)
W('40,2251', 0o00001, '', 'OCT', '1', 'ND2            =(16D)', kind='data', line=597)
# Page 319
W('40,2252', 0o00001, '', 'OCT', '1', 'ND1            =(17D)', kind='data', line=599)
W('40,2253', 0o00000, '', 'OCT', '0', 'VD2            =(18D)', kind='data', line=600)
W('40,2254', 0o00000, '', 'OCT', '0', 'VD1            =(19D)', kind='data', line=601)

W('40,2255', 0o35021, 'VERB', 'CAF', 'ZERO', line=603)
W('40,2256', 0o55001, '', 'TS', 'VERBREG', line=604)
W('40,2257', 0o34374, '', 'CAF', 'VD1', line=605)
W('40,2260', 0o54777, 'NVCOM', 'TS', 'DSPCOUNT', line=606)
W('40,2261', 0o02502, '', 'TC', '2BLANK', line=607)
W('40,2262', 0o35017, '', 'CAF', 'ONE', line=608)
W('40,2263', 0o55000, '', 'TS', 'DECBRNCH', 'SET FOR DEC V/N CODE', line=609)
W('40,2264', 0o35021, '', 'CAF', 'ZERO', line=610)
W('40,2265', 0o55013, '', 'TS', 'REQRET', 'SET FOR ENTPAS0', line=611)
W('40,2266', 0o34233, '', 'CAF', 'ENDINST', 'IF DSPALARM OCCURS BEFORE FIRST ENTPAS0', line=612)
W('40,2267', 0o54136, '', 'TS', 'ENTRET', 'OR NVSUB, ENTRET MUST ALREADY BE SET', line=613)
# TO TC ENDOFJOB
W('40,2270', 0o05217, '', 'TC', 'ENDOFJOB', line=615)
W('40,2271', 0o35021, 'NOUN', 'CAF', 'ZERO', line=616)
W('40,2272', 0o55002, '', 'TS', 'NOUNREG', line=617)
W('40,2273', 0o34375, '', 'CAF', 'ND1', 'ND1, OCT 21 (DEC 17)', line=618)
W('40,2274', 0o02260, '', 'TC', 'NVCOM', line=619)

W('40,2275', 0o02347, 'NEGSGN', 'TC', 'SIGNTEST', line=622)
W('40,2276', 0o02334, '', 'TC', '-ON', line=623)
W('40,2277', 0o35016, '', 'CAF', 'TWO', line=624)
W('40,2300', 0o50137, 'BOTHSGN', 'INDEX', 'INREL', 'SET DEC COMP BIT TO 1 (IN DECBRNCH)', line=625)
W('40,2301', 0o65011, '', 'AD', 'BIT7', 'BIT 5 FOR R1.  BIT 4 FOR R2.', line=626)
W('40,2302', 0o27000, '', 'ADS', 'DECBRNCH', 'BIT 3 FOR R3.', line=627)
W('40,2303', 0o11015, 'FIXCLPAS', 'CCS', 'CLPASS', 'IF CLPASS IS + OR +0, MAKE IT +0.', line=628)
W('40,2304', 0o35021, '', 'CAF', 'ZERO', line=629)
W('40,2305', 0o55015, '', 'TS', 'CLPASS', line=630)
W('40,2306', 0o02307, '', 'TC', '+1', line=631)
W('40,2307', 0o05217, '', 'TC', 'ENDOFJOB', line=632)

W('40,2310', 0o02347, 'POSGN', 'TC', 'SIGNTEST', line=634)
W('40,2311', 0o02314, '', 'TC', '+ON', line=635)
W('40,2312', 0o35017, '', 'CAF', 'ONE', line=636)
W('40,2313', 0o02300, '', 'TC', 'BOTHSGN', line=637)

W('40,2314', 0o22002, '+ON', 'LXCH', 'Q', line=639)
W('40,2315', 0o02225, '', 'TC', 'GETINREL', line=640)
W('40,2316', 0o50137, '', 'INDEX', 'INREL', line=641)
W('40,2317', 0o32342, '', 'CAF', 'SGNTAB -2', line=642)
W('40,2320', 0o54123, '', 'TS', 'SGNOFF', line=643)
W('40,2321', 0o65017, '', 'AD', 'ONE', line=644)
W('40,2322', 0o54122, '', 'TS', 'SGNON', line=645)
W('40,2323', 0o35021, 'SGNCOM', 'CAF', 'ZERO', line=646)
W('40,2324', 0o54124, '', 'TS', 'CODE', line=647)
# Page 320
W('40,2325', 0o56123, '', 'XCH', 'SGNOFF', line=649)
W('40,2326', 0o03311, '', 'TC', '11DSPIN', line=650)
W('40,2327', 0o35005, '', 'CAF', 'BIT11', line=651)
W('40,2330', 0o54124, '', 'TS', 'CODE', line=652)
W('40,2331', 0o56122, '', 'XCH', 'SGNON', line=653)
W('40,2332', 0o03311, '', 'TC', '11DSPIN', line=654)
W('40,2333', 0o00001, '', 'TC', 'L', line=655)
W('40,2334', 0o22002, '-ON', 'LXCH', 'Q', line=656)
W('40,2335', 0o02225, '', 'TC', 'GETINREL', line=657)
W('40,2336', 0o50137, '', 'INDEX', 'INREL', line=658)
W('40,2337', 0o32342, '', 'CAF', 'SGNTAB -2', line=659)
W('40,2340', 0o54122, '', 'TS', 'SGNON', line=660)
W('40,2341', 0o65017, '', 'AD', 'ONE', line=661)
W('40,2342', 0o54123, '', 'TS', 'SGNOFF', line=662)
W('40,2343', 0o02323, '', 'TC', 'SGNCOM', line=663)

W('40,2344', 0o00005, 'SGNTAB', 'OCT', '5', '-R1', kind='data', line=665)
W('40,2345', 0o00003, '', 'OCT', '3', '-R2', kind='data', line=666)
W('40,2346', 0o00000, '', 'OCT', '0', '-R3', kind='data', line=667)

W('40,2347', 0o22002, 'SIGNTEST', 'LXCH', 'Q', 'ALLOWS +,- ONLY WHEN DSPCOUNT=R1D1,', line=670)
W('40,2350', 0o36214, '', 'CAF', 'THREE', 'R2D1, OR R3D1. ALLOWS ONLY FIRST OF', line=671)
W('40,2351', 0o71000, '', 'MASK', 'DECBRNCH', 'CONSECUTIVE +/- CHARACTERS.', line=672)
W('40,2352', 0o10000, '', 'CCS', 'A', 'IF LOW2 BITS OF DECBRNCH NOT 0, SIGN', line=673)
W('40,2353', 0o05217, '', 'TC', 'ENDOFJOB', 'FOR THIS WORD ALREADY IN. REJECT.', line=674)
W('40,2354', 0o44333, '', 'CS', 'R1D1', line=675)
W('40,2355', 0o02363, '', 'TC', 'SGNTST1', line=676)
W('40,2356', 0o44334, '', 'CS', 'R2D1', line=677)
W('40,2357', 0o02363, '', 'TC', 'SGNTST1', line=678)
W('40,2360', 0o44335, '', 'CS', 'R3D1', line=679)
W('40,2361', 0o02363, '', 'TC', 'SGNTST1', line=680)
W('40,2362', 0o05217, '', 'TC', 'ENDOFJOB', 'NO MATCH FOUND. SIGN ILLEGAL', line=681)
W('40,2363', 0o60777, 'SGNTST1', 'AD', 'DSPCOUNT', line=682)
W('40,2364', 0o00006, '', 'EXTEND', line=683)
W('40,2365', 0o12367, '', 'BZF', '+2', 'MATCH FOUND', line=684)
W('40,2366', 0o00002, '', 'TC', 'Q', line=685)
W('40,2367', 0o00001, '', 'TC', 'L', 'SIGN LEGAL', line=686)

# CLEAR BLANKS WHICH R1, R2, R3 IS CURRENT OR LAST TO BE DISPLAYED(PERTINE
# NT XREG,YREG,ZREG IS CLEARED). SUCCESSIVE CLEARS TAKE CARE OF EACH RX
# L/ RC UNTIL R1 IS DONE. THEN NO FURTHER ACTION
#
# THE SINGLE COMPONENT LOAD VERBS ALLOW ONLY THE SINGLE RC THAT IS
# APPROPRIATE TO BE CLEARED.
#
# CLPASS   +0  PASS0, CAN BE BACKED UP
# +NZ  HIPASS, CAN BE BACKED UP
# -NZ  PASS0, CANNOT BE BACKED UP
# Page 321
W('40,2370', 0o10777, 'CLEAR', 'CCS', 'DSPCOUNT', line=700)
W('40,2371', 0o65017, '', 'AD', 'ONE', line=701)
W('40,2372', 0o02374, '', 'TC', '+2', line=702)
W('40,2373', 0o65017, '', 'AD', 'ONE', line=703)
W('40,2374', 0o50000, '', 'INDEX', 'A', 'DO NOT CHANGE DSPCOUNT BECAUSE MAY LATER', line=704)
W('40,2375', 0o32231, '', 'CAF', 'INRELTAB', 'FAIL LEGALTST.', line=705)
W('40,2376', 0o54137, '', 'TS', 'INREL', 'MUST SET INREL, EVEN FOR HIPASS.', line=706)
W('40,2377', 0o11015, '', 'CCS', 'CLPASS', line=707)
W('40,2400', 0o02406, '', 'TC', 'CLPASHI', '+', line=708)
W('40,2401', 0o02403, '', 'TC', '+2', '+0    IF CLPASS IS +0 OR -, IT IS PASS0', line=709)
W('40,2402', 0o02403, '', 'TC', '+1', '-', line=710)
W('40,2403', 0o30137, '', 'CA', 'INREL', line=711)
W('40,2404', 0o02430, '', 'TC', 'LEGALTST', line=712)
W('40,2405', 0o02423, '', 'TC', 'CLEAR1', line=713)
W('40,2406', 0o10137, 'CLPASHI', 'CCS', 'INREL', line=714)
W('40,2407', 0o54137, '', 'TS', 'INREL', line=715)
W('40,2410', 0o02430, '', 'TC', 'LEGALTST', line=716)
W('40,2411', 0o32500, '', 'CAF', 'DOUBLK +2', '+3 TO - NUMBER. BACKS DATA REQUESTS.', line=717)
W('40,2412', 0o27013, '', 'ADS', 'REQRET', line=718)
W('40,2413', 0o30137, '', 'CA', 'INREL', line=719)
W('40,2414', 0o54125, '', 'TS', 'MIXTEMP', 'TEMP STORAGE FOR INREL', line=720)
W('40,2415', 0o00006, '', 'EXTEND', line=721)
W('40,2416', 0o27001, '', 'DIM', 'VERBREG', 'DECREMENT VERB AND RE-DISPLAY', line=722)
W('40,2417', 0o04662, '', 'TC', 'BANKCALL', line=723)
W('40,2420', 0o62340, '', 'CADR', 'UPDATVB', kind='data', line=724)
W('40,2421', 0o30125, '', 'CA', 'MIXTEMP', line=725)
W('40,2422', 0o54137, '', 'TS', 'INREL', 'RESTORE INREL', line=726)
W('40,2423', 0o02426, 'CLEAR1', 'TC', 'CLR5', line=727)
W('40,2424', 0o25015, '', 'INCR', 'CLPASS', 'ONLY IF CLPASS IS + OR +0', line=728)
W('40,2425', 0o05217, '', 'TC', 'ENDOFJOB', 'SET FOR HIGHER PASS.', line=729)
W('40,2426', 0o22002, 'CLR5', 'LXCH', 'Q', 'USED 5BLANK BUT AVOIDS ITS TC GETINREL', line=730)
W('40,2427', 0o02441, '', 'TC', '5BLANK +2', line=731)
W('40,2430', 0o67715, 'LEGALTST', 'AD', 'NEG2', line=732)
W('40,2431', 0o10000, '', 'CCS', 'A', line=733)
W('40,2432', 0o00002, '', 'TC', 'Q', 'LEGAL  INREL G/ 2', line=734)
W('40,2433', 0o05747, '', 'TC', 'CCSHOLE', line=735)
W('40,2434', 0o05217, '', 'TC', 'ENDOFJOB', 'ILLEGAL   INREL= 0,1', line=736)
W('40,2435', 0o00002, '', 'TC', 'Q', 'LEGAL    INREL = 2', line=737)

# 5BLANK BLANKS 5 CHAR DISPLAY WORD IN R1, R2, OR R3. IT ALSO ZEROES XREG,
# YREG, OR ZREG.PLACE ANY + DSPCOUNT NUMBER FOR PERTINENT RC INTO DSPCOUNT
# DSPCOUNT IS LEFT SET TO LEFT MOST DSP NUMB FOR RC JUST BLANKED.

W('40,2436', 0o54777, '', 'TS', 'DSPCOUNT', 'NEEDED FOR BLANKSUB', line=744)
W('40,2437', 0o22002, '5BLANK', 'LXCH', 'Q', line=745)
W('40,2440', 0o02225, '', 'TC', 'GETINREL', line=746)
W('40,2441', 0o35021, '', 'CAF', 'ZERO', line=747)
W('40,2442', 0o50137, '', 'INDEX', 'INREL', line=748)
W('40,2443', 0o55001, '', 'TS', 'VERBREG', 'ZERO X, Y, Z, REG.', line=749)
# Page 322
W('40,2444', 0o50137, '', 'INDEX', 'INREL', line=751)
W('40,2445', 0o55004, '', 'TS', 'XREGLP -2', line=752)
W('40,2446', 0o54124, '', 'TS', 'CODE', line=753)
W('40,2447', 0o50137, '', 'INDEX', 'INREL', 'ZERO PERTINENT DEC COMP BIT.', line=754)
W('40,2450', 0o45011, '', 'CS', 'BIT7', 'PROTECT OTHERS', line=755)
W('40,2451', 0o71000, '', 'MASK', 'DECBRNCH', line=756)
W('40,2452', 0o72501, '', 'MASK', 'BRNCHCON', 'ZERO LOW 2 BITS.', line=757)
W('40,2453', 0o55000, '', 'TS', 'DECBRNCH', line=758)
W('40,2454', 0o50137, '', 'INDEX', 'INREL', line=759)
W('40,2455', 0o32471, '', 'CAF', 'SINBLANK -2', 'BLANK ISOLATED CHAR SEPARATELY', line=760)
W('40,2456', 0o54143, '', 'TS', 'COUNT', line=761)
W('40,2457', 0o03227, '', 'TC', 'DSPIN', line=762)
W('40,2460', 0o50137, '5BLANK1', 'INDEX', 'INREL', line=763)
W('40,2461', 0o32474, '', 'CAF', 'DOUBLK -2', line=764)
W('40,2462', 0o54777, '', 'TS', 'DSPCOUNT', line=765)
W('40,2463', 0o02502, '', 'TC', '2BLANK', line=766)
W('40,2464', 0o45016, '', 'CS', 'TWO', line=767)
W('40,2465', 0o26777, '', 'ADS', 'DSPCOUNT', line=768)
W('40,2466', 0o02502, '', 'TC', '2BLANK', line=769)
W('40,2467', 0o50137, '', 'INDEX', 'INREL', line=770)
W('40,2470', 0o34331, '', 'CAF', 'R1D1 -2', line=771)
W('40,2471', 0o54777, '', 'TS', 'DSPCOUNT', 'SET DSPCOUNT TO LEFT MOST DSP NUMBER', line=772)
W('40,2472', 0o00001, '', 'TC', 'L', 'OF REG. JUST BLANKED', line=773)

W('40,2473', 0o00016, 'SINBLANK', 'OCT', '16', 'DEC 14', kind='data', line=775)
W('40,2474', 0o00005, '', 'OCT', '5', kind='data', line=776)
W('40,2475', 0o00004, '', 'OCT', '4', kind='data', line=777)
W('40,2476', 0o00015, 'DOUBLK', 'OCT', '15', 'DEC 13', kind='data', line=778)
W('40,2477', 0o00011, '', 'OCT', '11', 'DEC 9', kind='data', line=779)
W('40,2500', 0o00003, '', 'OCT', '3', kind='data', line=780)

W('40,2501', 0o77774, 'BRNCHCON', 'OCT', '77774', kind='data', line=782)

# 2BLANK BLANKS TWO CHAR. PLACE DSP NUMBER OF LEFT CHAR  OF THE PAIR INTO
# DSPCOUNT. THIS NUMBER IS LEFT IN DSPCOUNT

W('40,2502', 0o30777, '2BLANK', 'CA', 'DSPCOUNT', line=787)
W('40,2503', 0o54021, '', 'TS', 'SR', line=788)
W('40,2504', 0o42515, '', 'CS', 'BLANKCON', line=789)
W('40,2505', 0o00004, '', 'INHINT', line=790)
W('40,2506', 0o50021, '', 'INDEX', 'SR', line=791)
W('40,2507', 0o57023, '', 'XCH', 'DSPTAB', line=792)
W('40,2510', 0o00006, '', 'EXTEND', line=793)
W('40,2511', 0o62513, '', 'BZMF', '+2', 'IF OLD CONTENTS -, NOUT OK', line=794)
W('40,2512', 0o25016, '', 'INCR', 'NOUT', 'IF OLD CONTENTS +, +1 TO NOUT', line=795)
W('40,2513', 0o00003, '', 'RELINT', '', 'IF -,NOUT OK', line=796)
W('40,2514', 0o00002, '', 'TC', 'Q', line=797)
W('40,2515', 0o04000, 'BLANKCON', 'OCT', '4000', kind='data', line=798)

# Page 323
# ENTER PASS 0 IS THE EXECUTE FUNCTION. HIGHER ORDER ENTERS ARE TO LOAD
# DATA. THE SIGN OF REQRET DETERMINES THE PASS, + FOR PASS 0,- FOR HIGHER
# PASSES.
#
#
# MACHINE CADR TO BE SPECIFIED (MCTBS) NOUNS DESIRE AN ECADR TO BE LOADED
# WHEN USED WITH LOAD VERBS, MONITOR VERBS, OR DISPLAY VERBS (EXCEPT
# VERB = FIXED MEMORY DISPLAY, WHICH REQUIRES AN FCADR).

#   BANK 41
#   SETLOC PINBALL2
#   BANK

#   COUNT 41/PIN

W('41,2000', 0o03544, 'NVSUBB', 'TC', 'NVSUB1', 'STANDARD LEAD INS. DONT MOVE.', line=817)
W('41,2001', 0o02775, 'LOADLV1', 'TC', 'LOADLV', line=818)

# END OF STANDARD LEAD INS.

W('41,2002', 0o35021, 'ENTER', 'CAF', 'ZERO', line=823)
W('41,2003', 0o55015, '', 'TS', 'CLPASS', line=824)
W('41,2004', 0o34233, '', 'CAF', 'ENDINST', line=825)
W('41,2005', 0o54136, '', 'TS', 'ENTRET', line=826)
W('41,2006', 0o11013, '', 'CCS', 'REQRET', line=827)
W('41,2007', 0o02035, '', 'TC', 'ENTPAS0', 'IF +, PASS 0', line=828)
W('41,2010', 0o02035, '', 'TC', 'ENTPAS0', 'IF +, PASS 0', line=829)
W('41,2011', 0o02012, '', 'TC', '+1', 'IF -, NOT PASS 0', line=830)
W('41,2012', 0o32033, 'ENTPASHI', 'CAF', 'MMADREF', line=831)
W('41,2013', 0o61013, '', 'AD', 'REQRET', 'IF L/ 2 CHAR IN FOR MM CODE, ALARM', line=832)
W('41,2014', 0o00006, '', 'EXTEND', '', 'AND RECYCLE(DECIDE AT MMCHANG+1).', line=833)
W('41,2015', 0o12027, '', 'BZF', 'ACCEPTWD', line=834)
W('41,2016', 0o36214, '', 'CAF', 'THREE', 'IF DEC, ALARM IF L/ 5 CHAR IN FOR DATA,', line=835)
W('41,2017', 0o71000, '', 'MASK', 'DECBRNCH', 'BUT LEAVE REQRET - AND FLASH ON, SO', line=836)
W('41,2020', 0o10000, '', 'CCS', 'A', 'OPERATOR CAN SUPPLY MISSING NUMERICAL', line=837)
W('41,2021', 0o02023, '', 'TC', '+2', 'CHARACTERS AND CONTINUE.', line=838)
W('41,2022', 0o02027, '', 'TC', 'ACCEPTWD', 'OCTAL. ANY NUMBER OF CHAR OK.', line=839)
W('41,2023', 0o10777, '', 'CCS', 'DSPCOUNT', line=840)
W('41,2024', 0o02351, '', 'TC', 'GODSPALM', 'LESS THAN 5 CHAR DEC(DSPCOUNT IS +)', line=841)
W('41,2025', 0o02351, '', 'TC', 'GODSPALM', 'LESS THAN 5 CHAR DEC(DSPCOUNT IS +)', line=842)
W('41,2026', 0o02027, '', 'TC', '+1', '5 CHAR IN (DSPCOUNT IS -)', line=843)
W('41,2027', 0o41013, 'ACCEPTWD', 'CS', 'REQRET', '5 CHAR IN (DSPCOUNT IS -)', line=844)
W('41,2030', 0o55013, '', 'TS', 'REQRET', 'SET REQRET +.', line=845)
W('41,2031', 0o04447, '', 'TC', 'FLASHOFF', line=846)
W('41,2032', 0o01013, '', 'TC', 'REQRET', line=847)

S('ENTEXIT', 'equals', 0o136, line=849)

W('41,2033', 0o03431, 'MMADREF', 'ADRES', 'MMCHANG +1', 'ASSUMES TC REQMM AT MMCHANG.', kind='data', line=851)

# Page 324
W('41,2034', 0o00034, 'LOWVERB', 'DEC', '28', 'LOWER VERB THAT AVOIDS NOUN TEST.', kind='data', line=854)

W('41,2035', 0o35021, 'ENTPAS0', 'CAF', 'ZERO', ' NOUN VERB SUB ENTERS HERE', line=856)
W('41,2036', 0o55000, '', 'TS', 'DECBRNCH', line=857)
W('41,2037', 0o44374, '', 'CS', 'VD1', 'BLOCK FURTHER NUM CHAR, SO THAT STRAY', line=858)
W('41,2040', 0o54777, '', 'TS', 'DSPCOUNT', 'CHAR DO NOT GET INTO VERB OR NOUN LTS.', line=859)
W('41,2041', 0o41001, 'TESTVB', 'CS', 'VERBREG', 'IF VERB IS G/E LOWVB, SKIP NOUN TEST.', line=860)
W('41,2042', 0o55041, '', 'TS', 'VERBSAVE', 'SAVE VERB FOR POSSIBLE RECYCLE.', line=861)
W('41,2043', 0o62034, '', 'AD', 'LOWVERB', 'LOWVERB - VB', line=862)
W('41,2044', 0o00006, '', 'EXTEND', line=863)
W('41,2045', 0o62133, '', 'BZMF', 'VERBFAN', 'VERB G/E LOWVERB', line=864)
W('41,2046', 0o00006, 'TESTNN', 'EXTEND', '', 'VERB L/ LOWVERB', line=865)
W('41,2047', 0o32114, '', 'DCA', 'LODNNLOC', 'SWITCH BANKS TO NOUN TABLE READING', line=866)
W('41,2050', 0o52006, '', 'DXCH', 'Z', 'ROUTINE.', line=867)
W('41,2051', 0o50140, '', 'INDEX', 'MIXBR', line=868)
W('41,2052', 0o02052, '', 'TC', '+0', line=869)
W('41,2053', 0o02055, '', 'TC', '+2', 'NORMAL', line=870)
W('41,2054', 0o02221, '', 'TC', 'MIXNOUN', 'MIXED', line=871)
W('41,2055', 0o10146, '', 'CCS', 'NNADTEM', 'NORMAL', line=872)
W('41,2056', 0o02131, '', 'TC', 'VERBFAN -2', '     NORMAL IF +', line=873)
W('41,2057', 0o02351, '', 'TC', 'GODSPALM', 'NOT IN USE   IF +0', line=874)
W('41,2060', 0o02064, '', 'TC', 'REQADD', 'SPECIFY MACHINE CADR IF -', line=875)
W('41,2061', 0o25017, '', 'INCR', 'NOUNCADR', 'AUGMENT MACHINE CADR IF -0', line=876)
W('41,2062', 0o04325, '', 'TC', 'SETNADD', 'ECADR FROM NOUNCADR. SETS EB, NOUNADD.', line=877)
W('41,2063', 0o02120, '', 'TC', 'INTMCTBS +2', line=878)
W('41,2064', 0o35001, 'REQADD', 'CAF', 'BIT15', 'SET CLPASS FOR PASS0 ONLY', line=879)
W('41,2065', 0o55015, '', 'TS', 'CLPASS', line=880)
W('41,2066', 0o44233, '', 'CS', 'ENDINST', 'TEST IF REACHED HERE FROM INTERNAL OR', line=881)
W('41,2067', 0o60136, '', 'AD', 'ENTEXIT', '            FROM EXTERNAL', line=882)
W('41,2070', 0o00006, '', 'EXTEND', line=883)
W('41,2071', 0o12073, '', 'BZF', '+2', 'EXTERNAL MACH CADR TO BE SPECIFIED', line=884)
W('41,2072', 0o02116, '', 'TC', 'INTMCTBS', line=885)
W('41,2073', 0o02307, '', 'TC', 'REQDATZ', 'EXTERNAL MACH CADR TO BE SPECIFIED', line=886)
W('41,2074', 0o11000, '', 'CCS', 'DECBRNCH', 'ALARM AND RECYCLE IF DECIMAL USED', line=887)
W('41,2075', 0o04161, '', 'TC', 'ALMCYCLE', 'FOR MCTBS.', line=888)
W('41,2076', 0o44374, '', 'CS', 'VD1', 'OCTAL USED  OK', line=889)
W('41,2077', 0o54777, '', 'TS', 'DSPCOUNT', 'BLOCK NUM CHAR IN', line=890)
W('41,2100', 0o11042, '', 'CCS', 'CADRSTOR', line=891)
W('41,2101', 0o02104, '', 'TC', '+3', 'EXTERNAL MCTBS DISPLAY WILL LEAVE FLASH', line=892)
W('41,2102', 0o02105, '', 'TC', 'USEADD', 'ON IF ENDIDLE NOT = +0.', line=893)
W('41,2103', 0o02104, '', 'TC', '+1', line=894)
W('41,2104', 0o04443, '', 'TC', 'FLASHON', line=895)
W('41,2105', 0o57005, 'USEADD', 'XCH', 'ZREG', line=896)
W('41,2106', 0o04317, '', 'TC', 'SETNCADR', 'ECADR INTO NOUNCADR. SET EB, NOUNADD.', line=897)
W('41,2107', 0o00006, '', 'EXTEND', line=898)
W('41,2110', 0o32114, '', 'DCA', 'LODNNLOC', 'SWITCH BANKS TO NOUN TAB E READING', line=899)
W('41,2111', 0o52006, '', 'DXCH', 'Z', 'ROUTINE.', line=900)
W('41,2112', 0o02133, '', 'TC', 'VERBFAN', line=901)

#   EBANK= DSPCOUNT
# Page 325
W('41,2113', 0o02062, 'LODNNLOC', '2CADR', 'LODNNTAB', kind='data', line=905)
W('41,2114', 0o64101, kind='data', line=905)

W('41,2115', 0o77772, 'NEG5', 'OCT', '77772', kind='data', line=907)

W('41,2116', 0o30156, 'INTMCTBS', 'CA', 'MPAC +2', 'INTERNAL MACH CADR TO BE SPECIFIED.', line=909)
W('41,2117', 0o04317, '', 'TC', 'SETNCADR', 'ECADR INTO NOUNCADR. SET EB, NOUNADD.', line=910)
W('41,2120', 0o45022, '', 'CS', 'FIVE', 'NVSUB CALL LEFT CADR IN MPAC+2 FOR MACH', line=911)
W('41,2121', 0o61001, '', 'AD', 'VERBREG', 'CADR TO BE SPECIFIED.', line=912)
W('41,2122', 0o00006, '', 'EXTEND', line=913)
W('41,2123', 0o12133, '', 'BZF', 'VERBFAN', 'DONT DISPLAY CADR IF VB = 05.', line=914)
W('41,2124', 0o34335, '', 'CAF', 'R3D1', 'VB NOT = 05. DISPLAY CADR.', line=915)
W('41,2125', 0o54777, '', 'TS', 'DSPCOUNT', line=916)
W('41,2126', 0o31017, '', 'CA', 'NOUNCADR', line=917)
W('41,2127', 0o03363, '', 'TC', 'DSPOCTWO', line=918)
W('41,2130', 0o02133, '', 'TC', 'VERBFAN', line=919)

W('41,2131', 0o65017, '', 'AD', 'ONE', line=921)
W('41,2132', 0o04317, '', 'TC', 'SETNCADR', 'ECADR INTO NOUNCADR. SETS EB, NOUNADD.', line=922)
W('41,2133', 0o42145, 'VERBFAN', 'CS', 'LST2CON', line=923)
W('41,2134', 0o61001, '', 'AD', 'VERBREG', 'VERB-LST2CON', line=924)
W('41,2135', 0o10000, '', 'CCS', 'A', line=925)
W('41,2136', 0o65017, '', 'AD', 'ONE', 'VERB G/ LST2CON', line=926)
W('41,2137', 0o02141, '', 'TC', '+2', line=927)
W('41,2140', 0o02146, '', 'TC', 'VBFANDIR', 'VERB L/ LST2CON', line=928)
W('41,2141', 0o54154, '', 'TS', 'MPAC', line=929)
W('41,2142', 0o04473, '', 'TC', 'RELDSP', 'RELEASE DISPLAY SYST', line=930)
W('41,2143', 0o04701, '', 'TC', 'POSTJUMP', 'GO TO GOEXTVB WITH VB-40 IN MPAC.', line=931)
W('41,2144', 0o66000, '', 'CADR', 'GOEXTVB', kind='data', line=932)
W('41,2145', 0o00050, 'LST2CON', 'DEC', '40', 'FIRST LIST2 VERB (EXTENDED VERB)', kind='data', line=933)

W('41,2146', 0o51001, 'VBFANDIR', 'INDEX', 'VERBREG', line=935)
W('41,2147', 0o32151, '', 'CAF', 'VERBTAB', line=936)
W('41,2150', 0o04704, '', 'TC', 'BANKJUMP', line=937)

W('41,2151', 0o62351, 'VERBTAB', 'CADR', 'GODSPALM', 'VB00 ILLEGAL', kind='data', line=939)
W('41,2152', 0o62365, '', 'CADR', 'DSPA', 'VB01 DISPLAY OCT COMP 1 (R1)', kind='data', line=940)
W('41,2153', 0o62373, '', 'CADR', 'DSPB', 'VB02 DISPLAY OCT COMP 2 (R1)', kind='data', line=941)
W('41,2154', 0o62400, '', 'CADR', 'DSPC', 'VB03 DISPLAY OCT COMP 3 (R1)', kind='data', line=942)
W('41,2155', 0o62360, '', 'CADR', 'DSPAB', 'VB04 DISPLAY OCT COMP 1,2 (R1,R2)', kind='data', line=943)
W('41,2156', 0o62353, '', 'CADR', 'DSPABC', 'VB05 DISPLAY OCT COMP 1,2,3 (R1,R2,R3)', kind='data', line=944)
W('41,2157', 0o62523, '', 'CADR', 'DECDSP', 'VB06 DECIMAL DISPLAY', kind='data', line=945)
W('41,2160', 0o60677, '', 'CADR', 'DSPDPDEC', 'VB07 DP DECIMAL DISPLAY (R1,R2)', kind='data', line=946)
W('41,2161', 0o62351, '', 'CADR', 'GODSPALM', 'VB08 SPARE', kind='data', line=947)
W('41,2162', 0o62351, '', 'CADR', 'GODSPALM', 'VB09 SPARE', kind='data', line=948)
W('41,2163', 0o61325, '', 'CADR', 'DSPALARM', 'VB10 SPARE', kind='data', line=949)
W('41,2164', 0o63230, '', 'CADR', 'MONITOR', 'VB11 MONITOR OCT COMP 1 (R1)', kind='data', line=950)
W('41,2165', 0o63230, '', 'CADR', 'MONITOR', 'VB12 MONITOR OCT COMP 2 (R1)', kind='data', line=951)
W('41,2166', 0o63230, '', 'CADR', 'MONITOR', 'VB13 MONITOR OCT COMP 3 (R1)', kind='data', line=952)
W('41,2167', 0o63230, '', 'CADR', 'MONITOR', 'VB14 MONITOR OCT COMP 1,2 (R1,R2)', kind='data', line=953)
# Page 326
W('41,2170', 0o63230, '', 'CADR', 'MONITOR', 'VB15 MONITOR OCT COMP 1,2,3 (R1,R2,R3)', kind='data', line=955)
W('41,2171', 0o63230, '', 'CADR', 'MONITOR', 'VB16 MONITOR DECIMAL', kind='data', line=956)
W('41,2172', 0o63230, '', 'CADR', 'MONITOR', 'VB17 MONITOR DP DEC (R1,R2)', kind='data', line=957)
W('41,2173', 0o62351, '', 'CADR', 'GODSPALM', 'VB18 SPARE', kind='data', line=958)
W('41,2174', 0o62351, '', 'CADR', 'GODSPALM', 'VB19 SPARE', kind='data', line=959)
W('41,2175', 0o62351, '', 'CADR', 'GODSPALM', 'VB20 SPARE', kind='data', line=960)
W('41,2176', 0o62732, '', 'CADR', 'ALOAD', 'VB21 LOAD COMP 1 (R1)', kind='data', line=961)
W('41,2177', 0o62743, '', 'CADR', 'BLOAD', 'VB22 LOAD COMP 2 (R2)', kind='data', line=962)
W('41,2200', 0o62760, '', 'CADR', 'CLOAD', 'VB23 LOAD COMP 3 (R3)', kind='data', line=963)
W('41,2201', 0o62703, '', 'CADR', 'ABLOAD', 'VB24 LOAD COMP 1,2 (R1,R2)', kind='data', line=964)
W('41,2202', 0o62616, '', 'CADR', 'ABCLOAD', 'VB25 LOAD COMP 1,2,3 (R1,R2,R3)', kind='data', line=965)
W('41,2203', 0o62351, '', 'CADR', 'GODSPALM', 'VB26 SPARE', kind='data', line=966)
W('41,2204', 0o63353, '', 'CADR', 'DSPFMEM', 'VB27 FIXED MEMORY DISPLAY', kind='data', line=967)
# THE FOLLOWING VERBS MAKE NO NOUN TEST
W('41,2205', 0o62351, '', 'CADR', 'GODSPALM', 'VB28 SPARE', kind='data', line=969)
W('41,2206', 0o62351, '', 'CADR', 'GODSPALM', 'VB29 SPARE', kind='data', line=970)
W('41,2207', 0o63466, 'REQEXLQC', 'CADR', 'VBRQEXEC', 'VB30 REQUEST EXECUTIVE', kind='data', line=971)
W('41,2210', 0o63512, '', 'CADR', 'VBRQWAIT', 'VB31 REQUEST WAITLIST', kind='data', line=972)
W('41,2211', 0o61364, '', 'CADR', 'VBRESEQ', 'VB32 RESEQUENCE', kind='data', line=973)
W('41,2212', 0o61347, '', 'CADR', 'VBPROC', 'VB33 PROCEED WITHOUT DATA', kind='data', line=974)
W('41,2213', 0o61355, '', 'CADR', 'VBTERM', 'VB34 TERMINATE CURRENT TEST OR LOAD REQ', kind='data', line=975)
W('41,2214', 0o63613, '', 'CADR', 'VBTSTLTS', 'VB35 TEST LIGHTS', kind='data', line=976)
W('41,2215', 0o12342, '', 'CADR', 'SLAP1', 'VB36 FRESH START', kind='data', line=977)
W('41,2216', 0o63430, '', 'CADR', 'MMCHANG', 'VB37 CHANGE MAJOR MODE', kind='data', line=978)
W('41,2217', 0o62351, '', 'CADR', 'GODSPALM', 'VB38 SPARE', kind='data', line=979)
W('41,2220', 0o62351, '', 'CADR', 'GODSPALM', 'VB39 SPARE', kind='data', line=980)

# THE LIST2 VERBFAN IS LOCATED IN THE EXTENDED VERB BANK.
# Page 327
# NNADTAB CONTAINS A RELATIVE ADDRESS, IDADDREL(IN LOW 10 BITS), REFERRING
# TO WHERE 3 CONSECUTIVE ADDRESSES ARE STORED (IN IDADDTAB).
# MIXNOUN GETS DATA AND STORES IN MIXTEMP,+1,+2. IT SETS NOUNADD FOR
# MIXTEMP.

W('41,2221', 0o10146, 'MIXNOUN', 'CCS', 'NNADTEM', line=990)
W('41,2222', 0o02226, '', 'TC', '+4', '+  IN USE', line=991)
W('41,2223', 0o02351, '', 'TC', 'GODSPALM', '+0  NOT IN USE', line=992)
W('41,2224', 0o02226, '', 'TC', '+2', '-  IN USE', line=993)
W('41,2225', 0o02226, '', 'TC', '+1', '-0  IN USE', line=994)
W('41,2226', 0o46211, '', 'CS', 'SIX', line=995)
W('41,2227', 0o61001, '', 'AD', 'VERBREG', line=996)
W('41,2230', 0o00006, '', 'EXTEND', line=997)
W('41,2231', 0o62233, '', 'BZMF', '+2', 'VERB L/E 6', line=998)
W('41,2232', 0o02133, '', 'TC', 'VERBFAN', 'AVOID MIXNOUN SWAP IF VB NOT = DISPLAY', line=999)
W('41,2233', 0o35016, '', 'CAF', 'TWO', line=1000)
W('41,2234', 0o54117, 'MIXNN1', 'TS', 'DECOUNT', line=1001)
W('41,2235', 0o62260, '', 'AD', 'MIXAD', line=1002)
W('41,2236', 0o54145, '', 'TS', 'NOUNADD', 'SET NOUNADD TO MIXTEMP + K', line=1003)
W('41,2237', 0o50117, '', 'INDEX', 'DECOUNT', 'GET IDADDTAB ENTRY FOR COMPONENT K', line=1004)
W('41,2240', 0o30150, '', 'CA', 'IDAD1TEM', 'OF NOUN.', line=1005)
W('41,2241', 0o54122, '', 'TS', 'NOUNTEM', line=1006)
# TEST FOR DP(FOR OCT DISPLAY). IF SO, GET
# MINOR PART ONLY.
W('41,2242', 0o03034, '', 'TC', 'SFRUTMIX', 'GET SF ROUT NUMBER IN A', line=1009)
W('41,2243', 0o02261, '', 'TC', 'DPTEST', line=1010)
W('41,2244', 0o02246, '', 'TC', 'MIXNN2', 'NO DP', line=1011)
W('41,2245', 0o24122, '', 'INCR', 'NOUNTEM', 'DP  GET MINOR PART', line=1012)
W('41,2246', 0o30122, 'MIXNN2', 'CA', 'NOUNTEM', line=1013)
W('41,2247', 0o74372, '', 'MASK', 'LOW11', 'ESUBK (NO DP)  OR (ESUBK)+1    FOR DP', line=1014)
W('41,2250', 0o04327, '', 'TC', 'SETEBANK', 'SET EBANK, LEAVE EADRES IN A.', line=1015)
W('41,2251', 0o50000, '', 'INDEX', 'A', 'PICK UP C(ESUBK)  NOT DP', line=1016)
W('41,2252', 0o30000, '', 'CA', '0', 'OR C((ESUBK)+1)  FOR DP MINOR PART', line=1017)
W('41,2253', 0o50145, '', 'INDEX', 'NOUNADD', line=1018)
W('41,2254', 0o56000, '', 'XCH', '0', 'STORE IN MIXTEM + K', line=1019)
W('41,2255', 0o10117, '', 'CCS', 'DECOUNT', line=1020)
W('41,2256', 0o02234, '', 'TC', 'MIXNN1', line=1021)
W('41,2257', 0o02133, '', 'TC', 'VERBFAN', line=1022)

W('41,2260', 0o00125, 'MIXAD', 'TC', 'MIXTEMP', line=1024)

# DPTEST   ENTER WITH SF ROUT NUMBER IN A.
# RETURNS TO L+1 IF NO DP.
# RETURNS TO L+2 IF DP.

W('41,2261', 0o50000, 'DPTEST', 'INDEX', 'A', line=1031)
W('41,2262', 0o12263, '', 'TCF', '+1', line=1032)
W('41,2263', 0o00002, '', 'TC', 'Q', 'OCTAL ONLY  NO DP', line=1033)
W('41,2264', 0o00002, '', 'TC', 'Q', 'FRACT NO DP', line=1034)
# Page 328
W('41,2265', 0o00002, '', 'TC', 'Q', 'DEG  NO DP', line=1036)
W('41,2266', 0o00002, '', 'TC', 'Q', 'ARITH  NO DP', line=1037)
W('41,2267', 0o12301, '', 'TCF', 'DPTEST1', 'DP1OUT', line=1038)
W('41,2270', 0o12301, '', 'TCF', 'DPTEST1', 'DP2OUT', line=1039)
W('41,2271', 0o00002, '', 'TC', 'Q', 'OPDEG  NO DP', line=1040)
W('41,2272', 0o12301, '', 'TCF', 'DPTEST1', 'DP3OUT', line=1041)
W('41,2273', 0o00002, '', 'TC', 'Q', 'HMS   NO DP', line=1042)
W('41,2274', 0o00002, '', 'TC', 'Q', 'M/S   NO DP', line=1043)
W('41,2275', 0o12301, '', 'TCF', 'DPTEST1', 'DP4OUT', line=1044)
W('41,2276', 0o00002, '', 'TC', 'Q', 'ARITH1   NO DP', line=1045)
W('41,2277', 0o00002, '', 'TC', 'Q', '2INTOUT  NO DP TO GET HI PART IN MPAC', line=1046)
W('41,2300', 0o12301, '', 'TCF', 'DPTEST1', 'DPFRACOT', line=1047)
W('41,2301', 0o50002, 'DPTEST1', 'INDEX', 'Q', line=1048)
W('41,2302', 0o00001, '', 'TC', '1', 'RETURN TO L+2', line=1049)

W('41,2303', 0o34333, 'REQDATX', 'CAF', 'R1D1', line=1052)
W('41,2304', 0o12310, '', 'TCF', 'REQCOM', line=1053)
W('41,2305', 0o34334, 'REQDATY', 'CAF', 'R2D1', line=1054)
W('41,2306', 0o12310, '', 'TCF', 'REQCOM', line=1055)
W('41,2307', 0o34335, 'REQDATZ', 'CAF', 'R3D1', line=1056)
W('41,2310', 0o54777, 'REQCOM', 'TS', 'DSPCOUNT', line=1057)
W('41,2311', 0o40002, '', 'CS', 'Q', line=1058)
W('41,2312', 0o55013, '', 'TS', 'REQRET', line=1059)
W('41,2313', 0o04662, '', 'TC', 'BANKCALL', line=1060)
W('41,2314', 0o60437, '', 'CADR', '5BLANK', kind='data', line=1061)
W('41,2315', 0o04443, '', 'TC', 'FLASHON', line=1062)
W('41,2316', 0o00136, 'ENDRQDAT', 'TC', 'ENTEXIT', line=1063)

W('41,2317', 0o55002, '', 'TS', 'NOUNREG', line=1065)
W('41,2320', 0o56002, 'UPDATNN', 'XCH', 'Q', line=1066)
W('41,2321', 0o54117, '', 'TS', 'UPDATRET', line=1067)
W('41,2322', 0o00006, '', 'EXTEND', line=1068)
W('41,2323', 0o32114, '', 'DCA', 'LODNNLOC', 'SWITCH BANKS TO NOUN TABLE READING', line=1069)
W('41,2324', 0o52006, '', 'DXCH', 'Z', 'ROUTINE.', line=1070)
W('41,2325', 0o10146, '', 'CCS', 'NNADTEM', line=1071)
W('41,2326', 0o65017, '', 'AD', 'ONE', 'NORMAL', line=1072)
W('41,2327', 0o12332, '', 'TCF', 'PUTADD', line=1073)
W('41,2330', 0o12333, '', 'TCF', 'PUTADD +1', 'MCTBS  DONT CHANGE NOUNADD', line=1074)
W('41,2331', 0o12333, '', 'TCF', 'PUTADD +1', 'MCTBI  DONT CHANGE NOUNADD', line=1075)
W('41,2332', 0o04317, 'PUTADD', 'TC', 'SETNCADR', 'ECADR INTO NOUNCADR. SETS EB, NOUNADD.', line=1076)
W('41,2333', 0o34375, '', 'CAF', 'ND1', line=1077)
W('41,2334', 0o54777, '', 'TS', 'DSPCOUNT', line=1078)
W('41,2335', 0o31002, '', 'CA', 'NOUNREG', line=1079)
W('41,2336', 0o12345, '', 'TCF', 'UPDAT1', line=1080)

W('41,2337', 0o55001, '', 'TS', 'VERBREG', line=1082)
W('41,2340', 0o56002, 'UPDATVB', 'XCH', 'Q', line=1083)
W('41,2341', 0o54117, '', 'TS', 'UPDATRET', line=1084)
W('41,2342', 0o34374, '', 'CAF', 'VD1', line=1085)
# Page 329
W('41,2343', 0o54777, '', 'TS', 'DSPCOUNT', line=1087)
W('41,2344', 0o31001, '', 'CA', 'VERBREG', line=1088)
W('41,2345', 0o04701, 'UPDAT1', 'TC', 'POSTJUMP', 'CANT USE SWCALL TO GO TC DSPDECVN.SINCE', line=1089)
W('41,2346', 0o61224, '', 'CADR', 'GOVNUPDT', 'UPDATVB CAN ITSELF BE CALLED BY SWCALL.', kind='data', line=1090)
W('41,2347', 0o00117, '', 'TC', 'UPDATRET', line=1091)

W('41,2350', 0o04161, 'GOALMCYC', 'TC', 'ALMCYCLE', 'NEEDED BECAUSE BANKJUMP CANT HANDLE F/F.', line=1094)

W('41,2351', 0o04701, 'GODSPALM', 'TC', 'POSTJUMP', line=1097)
W('41,2352', 0o61325, '', 'CADR', 'DSPALARM', kind='data', line=1098)

# Page 330
# NOUN   TABLES
# NOUN CODE L/40, NORMAL NOUN CASE.  NOUN CODE G/E 40, MIXED NOUN CASE.
# FOR NORMAL CASE, NNADTAB CONTAINS ONE       ECADR FOR EACH NOUN.
# +0 INDICATES NOUN NOT USED.   - ENTRY INDICATES MACHINE CADR(E OR F) TO
# BE SPECIFIED. -1 INDICATES CHANNEL TO BE SPECIFIED. -0 INDICATES AUGMENT
# OF LAST MACHINE CADR SUPPLIED.
#
# FOR MIXED CASE, NNADTAB CONTAINS ONE INDIRECT ADDRESS(IDADDREL) IN LOW
# 10 BITS, AND THE COMPONENT CODE NUMBER IN THE HIGH 5 BITS.
#
# NNTYPTAB IS A PACKED TABLE OF THE FORM MMMMMNNNNNPPPPP.
#
# FOR THE NORMAL CASE,  M-S ARE THE COMPONENT CODE NUMBER.
# N-S ARE THE SF ROUTINE CODE NUMBER.
# P-S ARE THE SF CONSTANT CODE NUMBER.
#
# MIXED-CASE,M-S ARE THE SF CONSTANT3 CODE NUMBER      3 COMPONENT CASE
# N-S ARE THE SF CONSTANT2 CODE NUMBER
# P-S ARE THE SF CONSTANT1 CODE NUMBER
# N-S ARE THE SF CONSTANT2 CODE NUMBER      2 COMPONENT CASE
# P-S ARE THE SF CONSTANT1 CODE NUMBER
# P-S ARE THE SF CONSTANT1 CODE NUMBER       1 COMPONENT CASE
#
# THERE IS ALSO AN INDIRECT ADDRESS TABLE(IDADDTAB) FOR MIXED CASE ONLY
# EACH ENTRY CONTAINS ONE ECADR.    IDADDREL IS THE RELATIVE ADDRESS OF
# THE FIRST OF THESE ENTRIES.
# THERE IS ONE ENTRY IN THIS TABEL FOR EACH COMPONENT OF A MIXED NOUN
# THEY ARE LISTED IN ORDER OF ASCENDING K.
#
# THERE IS ALSO A SCALE FACTOR ROUTINE NUMBER TABLE( RUTMXTAB ) FOR MIXED
# CASE ONLY. THERE IS ONE ENTRY PER MIXED NOUN. THE FORM IS,
# QQQQQRRRRRSSSSS
# Q-S ARE THE SF ROUTINE 3 CODE NUMBER     3 COMPONENT CASE
# R-S ARE THE SF ROUTINE 2 CODE NUMBER
# S-S ARE THE SF ROUTINE 1 CODE NUMBER
# R-S ARE THE SF ROUTINE 2 CODE NUMBER     2 COMPONENT CASE
# S-S ARE THE SF ROUTINE 1 CODE NUMBER
#
#
# IN OCTAL DISPLAY AND LOAD (OCT OR DEC) VERBS, EXCLUDE USE OF VERBS WHOSE
# COMPONENT NUMBER IS GREATER THAN THE NUMBER OF COMPONENTS IN NOUN.
# (ALL MACHINE ADDRESS TO BE SPECIFIED NOUNS ARE 3 COMPONENT.)
#
#
# IN MULTI-COMPONENT LOAD VERBS, NO MIXING OF OCTAL AND DECIMAL DATA
# COMPONENT WORDS IS ALLOWED.  ALARM IF VIOLATION.
#
# IN DECIMAL LOADS OF DATA, 5 NUMERICAL CHARACTERS MUST BE KEYED IN
# BEFORE EACH ENTER. IF NOT, ALARM.

# Page 331
# DISPLAY VERBS

W('41,2353', 0o45016, 'DSPABC', 'CS', 'TWO', line=1154)
W('41,2354', 0o02424, '', 'TC', 'COMPTEST', line=1155)
W('41,2355', 0o50145, '', 'INDEX', 'NOUNADD', line=1156)
W('41,2356', 0o40002, '', 'CS', '2', line=1157)
W('41,2357', 0o56132, '', 'XCH', 'BUF +2', line=1158)
W('41,2360', 0o45017, 'DSPAB', 'CS', 'ONE', line=1159)
W('41,2361', 0o02424, '', 'TC', 'COMPTEST', line=1160)
W('41,2362', 0o50145, '', 'INDEX', 'NOUNADD', line=1161)
W('41,2363', 0o40001, '', 'CS', '1', line=1162)
W('41,2364', 0o56131, '', 'XCH', 'BUF +1', line=1163)
W('41,2365', 0o02443, 'DSPA', 'TC', 'DECTEST', line=1164)
W('41,2366', 0o02466, '', 'TC', 'TSTFORDP', line=1165)
W('41,2367', 0o50145, '', 'INDEX', 'NOUNADD', line=1166)
W('41,2370', 0o40000, '', 'CS', '0', line=1167)
W('41,2371', 0o56130, 'DSPCOM1', 'XCH', 'BUF', line=1168)
W('41,2372', 0o02405, '', 'TC', 'DSPCOM2', line=1169)
W('41,2373', 0o45017, 'DSPB', 'CS', 'ONE', line=1170)
W('41,2374', 0o02437, '', 'TC', 'DCOMPTST', line=1171)
W('41,2375', 0o50145, '', 'INDEX', 'NOUNADD', line=1172)
W('41,2376', 0o40001, '', 'CS', '1', line=1173)
W('41,2377', 0o02371, '', 'TC', 'DSPCOM1', line=1174)
W('41,2400', 0o45016, 'DSPC', 'CS', 'TWO', line=1175)
W('41,2401', 0o02437, '', 'TC', 'DCOMPTST', line=1176)
W('41,2402', 0o50145, '', 'INDEX', 'NOUNADD', line=1177)
W('41,2403', 0o40002, '', 'CS', '2', line=1178)
W('41,2404', 0o02371, '', 'TC', 'DSPCOM1', line=1179)
W('41,2405', 0o45016, 'DSPCOM2', 'CS', 'TWO', 'A  B  C  AB  ABC', line=1180)
W('41,2406', 0o61001, '', 'AD', 'VERBREG', '-1 -0 +1 +2  +3   IN A', line=1181)
W('41,2407', 0o10000, '', 'CCS', 'A', '+0 +0 +0 +1  +2    IN A AFTER CCS', line=1182)
W('41,2410', 0o02413, '', 'TC', 'DSPCOM3', line=1183)
W('41,2411', 0o00136, '', 'TC', 'ENTEXIT', line=1184)
W('41,2412', 0o02413, '', 'TC', '+1', line=1185)
W('41,2413', 0o54122, 'DSPCOM3', 'TS', 'DISTEM', '+0 +1 +2 INTO DISTEM', line=1186)
W('41,2414', 0o50000, '', 'INDEX', 'A', line=1187)
W('41,2415', 0o34333, '', 'CAF', 'R1D1', line=1188)
W('41,2416', 0o54777, '', 'TS', 'DSPCOUNT', line=1189)
W('41,2417', 0o50122, '', 'INDEX', 'DISTEM', line=1190)
W('41,2420', 0o40130, '', 'CS', 'BUF', line=1191)
W('41,2421', 0o03363, '', 'TC', 'DSPOCTWO', line=1192)
W('41,2422', 0o56122, '', 'XCH', 'DISTEM', line=1193)
W('41,2423', 0o02407, '', 'TC', 'DSPCOM2 +2', line=1194)

# COMPTEST ALARMS IF COMPONENT NUMBER OF VERB(LOAD OR OCT DISPLAY) IS
# GREATER THAN THE HIGHEST COMPONENT NUMBER OF NOUN.
W('41,2424', 0o54123, 'COMPTEST', 'TS', 'SFTEMP1', '- VERB COMP', line=1198)
W('41,2425', 0o22002, '', 'LXCH', 'Q', line=1199)
W('41,2426', 0o02515, 'COMPTST1', 'TC', 'GETCOMP', line=1200)
W('41,2427', 0o04345, '', 'TC', 'LEFT5', line=1201)
W('41,2430', 0o76214, '', 'MASK', 'THREE', 'NOUN COMP', line=1202)
# Page 332
W('41,2431', 0o60123, '', 'AD', 'SFTEMP1', 'NOUN COMP - VERB COMP', line=1204)
W('41,2432', 0o10000, '', 'CCS', 'A', line=1205)
W('41,2433', 0o00001, '', 'TC', 'L', 'NOUN COMP G/ VERB COMP', line=1206)
W('41,2434', 0o05747, '', 'TC', 'CCSHOLE', line=1207)
W('41,2435', 0o02351, '', 'TC', 'GODSPALM', 'NOUN COMP L/ VERB COMP', line=1208)
W('41,2436', 0o00001, 'NDCMPTST', 'TC', 'L', 'NOUN COMP = VERB COMP', line=1209)

# DCOMPTST ALARMS IF DECIMAL ONLY BIT (BIT4 OF COMP CODE NUMBER) = 1.
# IF NOT, IT PERFORMS REGULAR COMPTEST.
W('41,2437', 0o54123, 'DCOMPTST', 'TS', 'SFTEMP1', '- VERB COMP', line=1214)
W('41,2440', 0o22002, '', 'LXCH', 'Q', line=1215)
W('41,2441', 0o02443, '', 'TC', 'DECTEST', line=1216)
W('41,2442', 0o02426, '', 'TC', 'COMPTST1', line=1217)

W('41,2443', 0o00006, 'DECTEST', 'EXTEND', '', 'ALARMS IF DEC ONLY BIT = 1 (BIT4 OF COMP', line=1219)
W('41,2444', 0o22156, '', 'QXCH', 'MPAC +2', 'CODE NUMBER). RETURNS IF NOT.', line=1220)
W('41,2445', 0o02515, '', 'TC', 'GETCOMP', line=1221)
W('41,2446', 0o75002, '', 'MASK', 'BIT14', line=1222)
W('41,2447', 0o10000, '', 'CCS', 'A', line=1223)
W('41,2450', 0o02351, '', 'TC', 'GODSPALM', line=1224)
W('41,2451', 0o00156, '', 'TC', 'MPAC +2', line=1225)

W('41,2452', 0o22002, 'DCTSTCYC', 'LXCH', 'Q', 'ALARMS AND RECYCLES IF DEC ONLY BIT = 1', line=1228)
W('41,2453', 0o02515, '', 'TC', 'GETCOMP', '( BIT4 OF COMP CODE NUMBER). RETURNS', line=1229)
W('41,2454', 0o75002, '', 'MASK', 'BIT14', 'IF NOT.  USED BY LOAD VERBS.', line=1230)
W('41,2455', 0o10000, '', 'CCS', 'A', line=1231)
W('41,2456', 0o04161, '', 'TC', 'ALMCYCLE', line=1232)
W('41,2457', 0o00001, '', 'TC', 'L', line=1233)

# NOUNTEST ALARMS IF NO-LOAD BIT (BIT5 OF COMP CODE NUMBER) = 1.
# IF NOT, IT RETURNS.
W('41,2460', 0o22002, 'NOUNTEST', 'LXCH', 'Q', line=1238)
W('41,2461', 0o02515, '', 'TC', 'GETCOMP', line=1239)
W('41,2462', 0o10000, '', 'CCS', 'A', line=1240)
W('41,2463', 0o00001, '', 'TC', 'L', line=1241)
W('41,2464', 0o00001, '', 'TC', 'L', line=1242)
W('41,2465', 0o02351, '', 'TC', 'GODSPALM', line=1243)

W('41,2466', 0o22002, 'TSTFORDP', 'LXCH', 'Q', 'TEST FOR DP. IF SO, GET MINOR PART ONLY.', line=1245)
W('41,2467', 0o30146, '', 'CA', 'NNADTEM', line=1246)
W('41,2470', 0o65017, '', 'AD', 'ONE', 'IF NNADTEM = -1, CHANNEL TO BE SPECIFIED', line=1247)
W('41,2471', 0o00006, '', 'EXTEND', line=1248)
W('41,2472', 0o12504, '', 'BZF', 'CHANDSP', line=1249)
W('41,2473', 0o50140, '', 'INDEX', 'MIXBR', line=1250)
W('41,2474', 0o02474, '', 'TC', '+0', line=1251)
W('41,2475', 0o02477, '', 'TC', '+2', 'NORMAL', line=1252)
# Page 333
W('41,2476', 0o00001, '', 'TC', 'L', 'MIXED CASE ALREADY HANDLED IN MIXNOUN', line=1254)
W('41,2477', 0o03026, '', 'TC', 'SFRUTNOR', line=1255)
W('41,2500', 0o02261, '', 'TC', 'DPTEST', line=1256)
W('41,2501', 0o00001, '', 'TC', 'L', 'NO DP', line=1257)
W('41,2502', 0o24145, '', 'INCR', 'NOUNADD', 'DP    E+1 INTO NOUNADD FOR MINOR PART.', line=1258)
W('41,2503', 0o00001, '', 'TC', 'L', line=1259)

W('41,2504', 0o31017, 'CHANDSP', 'CA', 'NOUNCADR', line=1262)
W('41,2505', 0o75046, '', 'MASK', 'LOW9', line=1263)
W('41,2506', 0o00006, '', 'EXTEND', line=1264)
W('41,2507', 0o50000, '', 'INDEX', 'A', line=1265)
W('41,2510', 0o00000, '', 'READ', '0', line=1266)
W('41,2511', 0o40000, '', 'CS', 'A', line=1267)
W('41,2512', 0o12371, '', 'TCF', 'DSPCOM1', line=1268)

W('41,2513', 0o00147, 'COMPICK', 'ADRES', 'NNTYPTEM', kind='data', line=1271)
W('41,2514', 0o00146, '', 'ADRES', 'NNADTEM', kind='data', line=1272)

W('41,2515', 0o50140, 'GETCOMP', 'INDEX', 'MIXBR', 'NORMAL                MIXED', line=1274)
W('41,2516', 0o32512, '', 'CAF', 'COMPICK -1', 'ADRES NNTYPTEM        ADRES NNADTEM', line=1275)
W('41,2517', 0o50000, '', 'INDEX', 'A', line=1276)
W('41,2520', 0o30000, '', 'CA', '0', 'C(NNTYPTEM)           C(NNADTEM)', line=1277)
W('41,2521', 0o74364, '', 'MASK', 'HI5', 'GET HI5 OF NNTYPTAB(NORM)OF NNADTAB(MIX)', line=1278)
W('41,2522', 0o00002, '', 'TC', 'Q', line=1279)

W('41,2523', 0o02515, 'DECDSP', 'TC', 'GETCOMP', line=1282)
W('41,2524', 0o04345, '', 'TC', 'LEFT5', line=1283)
W('41,2525', 0o76214, '', 'MASK', 'THREE', line=1284)
W('41,2526', 0o54117, '', 'TS', 'DECOUNT', 'COMP NUMBER INTO DECOUNT', line=1285)
W('41,2527', 0o54122, 'DSPDCGET', 'TS', 'DECTEM', 'PICKS UP DATA', line=1286)
W('41,2530', 0o60145, '', 'AD', 'NOUNADD', 'DECTEM  1COMP +0, 2COMP +1, 3COMP +2', line=1287)
W('41,2531', 0o50000, '', 'INDEX', 'A', line=1288)
W('41,2532', 0o40000, '', 'CS', '0', line=1289)
W('41,2533', 0o50122, '', 'INDEX', 'DECTEM', line=1290)
W('41,2534', 0o57003, '', 'XCH', 'XREG', 'CANT USE BUF SINCE DMP USES IT.', line=1291)
W('41,2535', 0o10122, '', 'CCS', 'DECTEM', line=1292)
W('41,2536', 0o02527, '', 'TC', 'DSPDCGET', 'MORE TO GET', line=1293)
W('41,2537', 0o35021, 'DSPDCPUT', 'CAF', 'ZERO', 'DISPLAYS DATA', line=1294)
W('41,2540', 0o54155, '', 'TS', 'MPAC +1', 'DECOUNT 1COMP +0, 2COMP +1, 3COMP +2', line=1295)
W('41,2541', 0o54156, '', 'TS', 'MPAC +2', line=1296)
W('41,2542', 0o50117, '', 'INDEX', 'DECOUNT', line=1297)
W('41,2543', 0o34333, '', 'CAF', 'R1D1', line=1298)
W('41,2544', 0o54777, '', 'TS', 'DSPCOUNT', line=1299)
W('41,2545', 0o50117, '', 'INDEX', 'DECOUNT', line=1300)
W('41,2546', 0o41003, '', 'CS', 'XREG', line=1301)
W('41,2547', 0o54154, '', 'TS', 'MPAC', line=1302)
W('41,2550', 0o03047, '', 'TC', 'SFCONUM', '2X( SF CON NUMB ) IN A', line=1303)
# Page 334
W('41,2551', 0o54123, '', 'TS', 'SFTEMP1', line=1305)
W('41,2552', 0o00006, '', 'EXTEND', '', 'SWITCH BANKS TO SF CONSTANT TABLE', line=1306)
W('41,2553', 0o32565, '', 'DCA', 'GTSFOUTL', '   READING ROUTINE.', line=1307)
W('41,2554', 0o52006, '', 'DXCH', 'Z', 'LOADS SFTEMP1, SFTEMP2', line=1308)
W('41,2555', 0o50140, '', 'INDEX', 'MIXBR', line=1309)
W('41,2556', 0o02556, '', 'TC', '+0', line=1310)
W('41,2557', 0o02562, '', 'TC', 'DSPSFNOR', line=1311)
W('41,2560', 0o03034, '', 'TC', 'SFRUTMIX', line=1312)
W('41,2561', 0o02575, '', 'TC', 'DECDSP3', line=1313)

W('41,2562', 0o03026, 'DSPSFNOR', 'TC', 'SFRUTNOR', line=1315)
W('41,2563', 0o02575, '', 'TC', 'DECDSP3', line=1316)

#   EBANK= DSPCOUNT
W('41,2564', 0o02120, 'GTSFOUTL', '2CADR', 'GTSFOUT', kind='data', line=1319)
W('41,2565', 0o64101, kind='data', line=1319)

W('41,2566', 0o04662, 'DSPDCEND', 'TC', 'BANKCALL', 'ALL SFOUT ROUTINES END HERE', line=1322)
W('41,2567', 0o61133, '', 'CADR', 'DSPDECWD', kind='data', line=1323)
W('41,2570', 0o10117, '', 'CCS', 'DECOUNT', line=1324)
W('41,2571', 0o02573, '', 'TC', '+2', line=1325)
W('41,2572', 0o00136, '', 'TC', 'ENTEXIT', line=1326)
W('41,2573', 0o54117, '', 'TS', 'DECOUNT', line=1327)
W('41,2574', 0o02537, '', 'TC', 'DSPDCPUT', 'MORE TO DISPLAY', line=1328)

W('41,2575', 0o50000, 'DECDSP3', 'INDEX', 'A', line=1331)
W('41,2576', 0o32600, '', 'CAF', 'SFOUTABR', line=1332)
W('41,2577', 0o04704, '', 'TC', 'BANKJUMP', line=1333)

W('41,2600', 0o61323, 'SFOUTABR', 'CADR', 'PREDSPAL', 'ALARM IF DEC DISP WITH OCTAL ONLY NOUN', kind='data', line=1335)
W('41,2601', 0o62566, '', 'CADR', 'DSPDCEND', kind='data', line=1336)
W('41,2602', 0o60516, '', 'CADR', 'DEGOUTSF', kind='data', line=1337)
W('41,2603', 0o60603, '', 'CADR', 'ARTOUTSF', kind='data', line=1338)
W('41,2604', 0o60614, '', 'CADR', 'DP1OUTSF', kind='data', line=1339)
W('41,2605', 0o60621, '', 'CADR', 'DP2OUTSF', kind='data', line=1340)
W('41,2606', 0o60524, '', 'CADR', 'OPDEGOUT', kind='data', line=1341)
W('41,2607', 0o60623, '', 'CADR', 'DP3OUTSF', kind='data', line=1342)
W('41,2610', 0o65143, '', 'CADR', 'HMSOUT', kind='data', line=1343)
W('41,2611', 0o65216, '', 'CADR', 'M/SOUT', kind='data', line=1344)
W('41,2612', 0o60621, '', 'CADR', 'DP2OUTSF', kind='data', line=1345)
W('41,2613', 0o60610, '', 'CADR', 'AROUT1SF', kind='data', line=1346)
W('41,2614', 0o60636, '', 'CADR', '2INTOUT', kind='data', line=1347)
W('41,2615', 0o60653, '', 'CADR', 'DPFRACOT', kind='data', line=1348)
S('ENDRTOUT', 'equals', 0o112616, line=1349)

# THE FOLLOWING IS ATYPICAL SF ROUTINE . IT USES MPAC. LEAVES RESU
# LTS IN MPAC, MPAC+1. ENDS WITH TC DSPDCEND

# Page 335

#   SETLOC BLANKCON +1

#   COUNT 40/PIN
# DEGOUTSF SCALES BY .18 THE LOW 14 BITS OF ANGLE , ADDING .18 FOR
# NUMBERS IN THE NEGATIVE (AGC) RANGE.

W('40,2516', 0o35021, 'DEGOUTSF', 'CAF', 'ZERO', line=1362)
W('40,2517', 0o54156, '', 'TS', 'MPAC +2', 'SET INDEX FOR FULL SCALE', line=1363)
W('40,2520', 0o02555, '', 'TC', 'FIXRANGE', line=1364)
W('40,2521', 0o02523, '', 'TC', '+2', 'NO AUGMENT NEEDED (SFTEMP1 AND 2 ARE 0)', line=1365)
W('40,2522', 0o02550, '', 'TC', 'SETAUG', 'SET AUGMENTER ACCORDING TO C(MPAC +2)', line=1366)
W('40,2523', 0o02566, '', 'TC', 'DEGCOM', line=1367)

# OPDEGOUT SCALES BY .45 (THE RANGE IS 90 DEGREES) AND ADDS A 20 DEG BIAS.

W('40,2524', 0o10154, 'OPDEGOUT', 'CCS', 'MPAC', 'RANGE IS 90 DEG', line=1371)
W('40,2525', 0o56154, '', 'XCH', 'MPAC', 'IF POS OR POS 0 THEN ADD BIAS AND', line=1372)
W('40,2526', 0o02531, '', 'TC', '+3', 'CORRECT FOR POSSIBLE OVERFLOW', line=1373)
W('40,2527', 0o02540, '', 'TC', 'NEGOPT', 'IF NEG NON ZERO', line=1374)
W('40,2530', 0o67716, '', 'AD', 'NEG1', 'IF NEG ZERO SUBTRACT 1', line=1375)
W('40,2531', 0o62602, '', 'AD', '20BIAS', line=1376)
W('40,2532', 0o54154, 'BIASCOM', 'TS', 'MPAC', 'TEST FOR OVEFLOW', line=1377)
W('40,2533', 0o02536, '', 'TC', '+3', 'NO OVFLOW', line=1378)
W('40,2534', 0o35001, '', 'CAF', 'BIT15', 'IF OVFLOW', line=1379)
W('40,2535', 0o26154, '', 'ADS', 'MPAC', line=1380)
W('40,2536', 0o35016, '', 'CAF', 'TWO', 'SET MULTIPLIER TO .45', line=1381)
W('40,2537', 0o02517, '', 'TC', 'DEGOUTSF +1', line=1382)

W('40,2540', 0o56154, 'NEGOPT', 'XCH', 'MPAC', 'NEGATIVE CASE', line=1384)
W('40,2541', 0o62602, '', 'AD', '20BIAS', line=1385)
W('40,2542', 0o10000, '', 'CCS', 'A', line=1386)
W('40,2543', 0o02532, '', 'TC', 'BIASCOM', 'IF POS THEN SUBTRACT 1 BECASUE OF 2SCOM', line=1387)
W('40,2544', 0o05747, '', 'TC', 'CCSHOLE', line=1388)
W('40,2545', 0o65017, '', 'AD', 'ONE', 'IF NEG RESTORE SUM', line=1389)
W('40,2546', 0o40000, '', 'COM', '', 'IF NEG 0 LEAVE NEG 0', line=1390)
W('40,2547', 0o02532, '', 'TC', 'BIASCOM', line=1391)

W('40,2550', 0o00006, 'SETAUG', 'EXTEND', '', 'LOADS SFTEMP1 AND SFTEMP2 WITH THE', line=1393)
W('40,2551', 0o50156, '', 'INDEX', 'MPAC +2', 'DP AUGMENTER CONSTANT', line=1394)
W('40,2552', 0o32577, '', 'DCA', 'DEGTAB', line=1395)
W('40,2553', 0o52124, '', 'DXCH', 'SFTEMP1', line=1396)
W('40,2554', 0o00002, '', 'TC', 'Q', line=1397)

W('40,2555', 0o10154, 'FIXRANGE', 'CCS', 'MPAC', 'IF MPAC IS + RETURN TO L+1', line=1399)
W('40,2556', 0o00002, '', 'TC', 'Q', 'IF MPAC IS - RETURN TO L+2 AFTER', line=1400)
W('40,2557', 0o00002, '', 'TC', 'Q', 'MASKING OUT THE SIGN BIT', line=1401)
W('40,2560', 0o12561, '', 'TCF', '+1', line=1402)
W('40,2561', 0o45001, '', 'CS', 'BIT15', line=1403)
W('40,2562', 0o70154, '', 'MASK', 'MPAC', line=1404)
# Page 336
W('40,2563', 0o54154, '', 'TS', 'MPAC', line=1406)
W('40,2564', 0o50002, '', 'INDEX', 'Q', line=1407)
W('40,2565', 0o00001, '', 'TC', '1', line=1408)

W('40,2566', 0o00006, 'DEGCOM', 'EXTEND', '', 'LOADS MULTIPLIER , DOES SHORTMP, AND', line=1410)
W('40,2567', 0o50156, '', 'INDEX', 'MPAC +2', 'ADDS AUTMENTER.', line=1411)
W('40,2570', 0o32577, '', 'DCA', 'DEGTAB', line=1412)
W('40,2571', 0o52155, '', 'DXCH', 'MPAC', 'ADJUSTED ANGLE IN A', line=1413)
W('40,2572', 0o07256, '', 'TC', 'SHORTMP', line=1414)
W('40,2573', 0o52124, '', 'DXCH', 'SFTEMP1', line=1415)
W('40,2574', 0o20155, '', 'DAS', 'MPAC', line=1416)
W('40,2575', 0o02606, '', 'TC', 'SCOUTEND', line=1417)

W('40,2576', 0o05605, 'DEGTAB', 'OCT', '05605', 'HI PART OF     .18', kind='data', line=1420)
W('40,2577', 0o03656, '', 'OCT', '03656', 'LOW PART OF    .18', kind='data', line=1421)
W('40,2600', 0o16314, '', 'OCT', '16314', 'HI PART OF     .45', kind='data', line=1422)
W('40,2601', 0o31463, '', 'OCT', '31463', 'LO PART OF     .45', kind='data', line=1423)

W('40,2602', 0o16040, '20BIAS', 'OCT', '16040', '20 DEG BIAS FOR OPTICS', kind='data', line=1425)

W('40,2603', 0o52124, 'ARTOUTSF', 'DXCH', 'SFTEMP1', 'ASSUMES POINT AT LEFT OF DP SFCON', line=1427)
W('40,2604', 0o52155, '', 'DXCH', 'MPAC', line=1428)
W('40,2605', 0o04431, '', 'TC', 'PRSHRTMP', 'IF C(A) = -0, SHORTMP FAILS TO GIVE -0.', line=1429)
W('40,2606', 0o04701, 'SCOUTEND', 'TC', 'POSTJUMP', line=1430)
W('40,2607', 0o62566, '', 'CADR', 'DSPDCEND', kind='data', line=1431)

W('40,2610', 0o52124, 'AROUT1SF', 'DXCH', 'SFTEMP1', 'ASSUMES POINT BETWEEN HI AND LO PARTS OF', line=1433)
W('40,2611', 0o52155, '', 'DXCH', 'MPAC', 'DP SFCON. SHIFTS RESULTS LEFT 14, BY', line=1434)
W('40,2612', 0o04431, '', 'TC', 'PRSHRTMP', 'TAKING RESULTS FROM MPAC+1, MPAC+2.', line=1435)
W('40,2613', 0o02615, '', 'TC', 'L14/OUT', line=1436)

W('40,2614', 0o02627, 'DP1OUTSF', 'TC', 'DPOUT', 'SCALES MPAC, MPAC +1 BY DP SCALE FACTOR', line=1439)
W('40,2615', 0o56156, 'L14/OUT', 'XCH', 'MPAC +2', 'IN SFTEMP1, SFTEMP2. THEN SCALE RESULT', line=1440)
W('40,2616', 0o56155, '', 'XCH', 'MPAC +1', 'BY B14', line=1441)
W('40,2617', 0o54154, '', 'TS', 'MPAC', line=1442)
W('40,2620', 0o02606, '', 'TC', 'SCOUTEND', line=1443)

W('40,2621', 0o02627, 'DP2OUTSF', 'TC', 'DPOUT', 'SCALES MPAC , MPAC +1 BY DP SCALE FACTOR', line=1446)
W('40,2622', 0o02606, '', 'TC', 'SCOUTEND', line=1447)

W('40,2623', 0o02627, 'DP3OUTSF', 'TC', 'DPOUT', 'ASSUMES POINT BETWEEN BITS 7-8 OF HIGH', line=1450)
W('40,2624', 0o36211, '', 'CAF', 'SIX', 'LEFT BY 7, ROUNDS MPAC+2 INTO MPAC+1.', line=1451)
W('40,2625', 0o03060, '', 'TC', 'TPLEFTN', 'SHIFT LEFT 7.', line=1452)
W('40,2626', 0o02606, '', 'TC', 'SCOUTEND', line=1453)

# Page 337

S('MPAC+6', 'equals', 0o162, line=1457)  # USE MPAC +6 INSTEAD OF OVFIND

W('40,2627', 0o56002, 'DPOUT', 'XCH', 'Q', line=1459)
W('40,2630', 0o54162, '', 'TS', 'MPAC+6', line=1460)
W('40,2631', 0o02655, '', 'TC', 'READLO', 'GET FRESH DATA FOR BOTH HI AND LO.', line=1461)
W('40,2632', 0o07226, '', 'TC', 'TPAGREE', 'MAKE DP DATA AGREE', line=1462)
W('40,2633', 0o07052, '', 'TC', 'DMP', line=1463)
W('40,2634', 0o00123, '', 'ADRES', 'SFTEMP1', kind='data', line=1464)
W('40,2635', 0o00162, '', 'TC', 'MPAC+6', line=1465)
# THE FOLLOWING ROUTINE DISPLAYS TWO CONTIGUOUS SP POSITIVE INTEGERS
# AS TWO POSITIVE DECIMAL INTEGERS IN RXD1-RXD2 AND RXD4-RXD5 (RXD3 IS
# BLANKED). THE INTEGER IN THE LOWER NUMBERED ADDRESS IS DISPLAYED IN
# RXD1-RXD2.

W('40,2636', 0o02437, '2INTOUT', 'TC', '5BLANK', 'TO BLANK RXD3', line=1471)
W('40,2637', 0o02314, '', 'TC', '+ON', 'TURN ON + SIGN', line=1472)
W('40,2640', 0o30154, '', 'CA', 'MPAC', line=1473)
W('40,2641', 0o03213, '', 'TC', 'DSPDECVN', 'DISPLAY 1ST INTEGER (LIKE VERB AND NOUN)', line=1474)
W('40,2642', 0o46214, '', 'CS', 'THREE', line=1475)
W('40,2643', 0o50117, '', 'INDEX', 'DECOUNT', line=1476)
W('40,2644', 0o64333, '', 'AD', 'R1D1', 'RXD4', line=1477)
W('40,2645', 0o54777, '', 'TS', 'DSPCOUNT', line=1478)
W('40,2646', 0o02655, '', 'TC', 'READLO', 'GET 2ND INTEGER', line=1479)
W('40,2647', 0o30155, '', 'CA', 'MPAC +1', line=1480)
W('40,2650', 0o03213, '', 'TC', 'DSPDECVN', 'DISPLAY 2ND INTEGER (LIKE VERB AND NOUN)', line=1481)
W('40,2651', 0o04701, '', 'TC', 'POSTJUMP', line=1482)
W('40,2652', 0o62570, '', 'CADR', 'DSPDCEND +2', kind='data', line=1483)

W('40,2653', 0o02655, 'DPFRACOT', 'TC', 'READLO', 'DP FRACTION TO MPAC,+1', line=1486)
W('40,2654', 0o02606, '', 'TC', 'SCOUTEND', line=1487)

# READLO PICKS UP FRESH DATA FOR BOTH HI AND LO AND LEAVES IT IN
# MPAC, MPAC+1. THIS IS NEEDED FOR TIME DISPLAY. IT ZEROES MPAC+2, BUT
# DOES NOT FORCE TPAGREE.

W('40,2655', 0o56002, 'READLO', 'XCH', 'Q', line=1494)
W('40,2656', 0o54144, '', 'TS', 'TEM4', line=1495)
W('40,2657', 0o50140, '', 'INDEX', 'MIXBR', line=1496)
W('40,2660', 0o02660, '', 'TC', '+0', line=1497)
W('40,2661', 0o02675, '', 'TC', 'RDLONOR', line=1498)
W('40,2662', 0o50117, '', 'INDEX', 'DECOUNT', line=1499)
W('40,2663', 0o30150, '', 'CA', 'IDAD1TEM', 'GET IDADDTAB ENTRY FOR COMP K OF NOUN.', line=1500)
W('40,2664', 0o74372, '', 'MASK', 'LOW11', 'E SUBK', line=1501)
W('40,2665', 0o04327, '', 'TC', 'SETEBANK', 'SET EB, LEAVE EADRES IN A.', line=1502)
W('40,2666', 0o00006, 'READLO1', 'EXTEND', '', 'MIXED         NORMAL', line=1503)
W('40,2667', 0o50000, '', 'INDEX', 'A', 'C(ESUBK)      C(E)', line=1504)
W('40,2670', 0o30001, '', 'DCA', '0', 'C((E SUBK)+1)       C(E+1)', line=1505)
W('40,2671', 0o52155, '', 'DXCH', 'MPAC', line=1506)
# Page 338
W('40,2672', 0o35021, '', 'CAF', 'ZERO', line=1508)
W('40,2673', 0o54156, '', 'TS', 'MPAC +2', line=1509)
W('40,2674', 0o00144, '', 'TC', 'TEM4', line=1510)

W('40,2675', 0o30145, 'RDLONOR', 'CA', 'NOUNADD', 'E', line=1512)
W('40,2676', 0o02666, 'ENDRDLO', 'TC', 'READLO1', line=1513)

#   BANK 42
#   SETLOC PINBALL3
#   BANK

#   COUNT 42/PIN

W('42,3143', 0o04662, 'HMSOUT', 'TC', 'BANKCALL', 'READ FRESH DATA FOR HI AND LO INTO MPAC,', line=1522)
W('42,3144', 0o60655, '', 'CADR', 'READLO', 'MPAC+1.', kind='data', line=1523)
W('42,3145', 0o07226, '', 'TC', 'TPAGREE', 'MAKE DP DATA AGREE', line=1524)
W('42,3146', 0o03332, '', 'TC', 'SEPSECNR', 'LEAVE FRACT SEC/60 IN MPAC, MPAC+1.LEAVE', line=1525)
# WHOLE MIN IN BIT13 OF LOTEMOUT AND ABOVE
W('42,3147', 0o07052, '', 'TC', 'DMP', 'USE ONLY FRACT SEC/60 MOD 60', line=1527)
W('42,3150', 0o03204, '', 'ADRES', 'SECON2', 'MULT BY .06', kind='data', line=1528)
W('42,3151', 0o34335, '', 'CAF', 'R3D1', 'GIVES CENTI-SEC/10EXP5 MOD 60', line=1529)
W('42,3152', 0o54777, '', 'TS', 'DSPCOUNT', line=1530)
W('42,3153', 0o04662, '', 'TC', 'BANKCALL', 'DISPLAY SEC MOD 60', line=1531)
W('42,3154', 0o61133, '', 'CADR', 'DSPDECWD', kind='data', line=1532)
W('42,3155', 0o03350, '', 'TC', 'SEPMIN', 'REMOVE REST OF SECONDS', line=1533)
W('42,3156', 0o33206, '', 'CAF', 'MINCON2', 'LEAVE FRACT MIN/60 IN MPAC+1. LEAVE', line=1534)
W('42,3157', 0o56154, '', 'XCH', 'MPAC', 'WHOLE HOURS IN MPAC.', line=1535)
W('42,3160', 0o55007, '', 'TS', 'HITEMOUT', 'SAVE WHOLE HOURS.', line=1536)
W('42,3161', 0o33207, '', 'CAF', 'MINCON2 +1', line=1537)
W('42,3162', 0o56155, '', 'XCH', 'MPAC +1', 'USE ONLY FRACT MIN/60 MOD 60', line=1538)
W('42,3163', 0o04431, '', 'TC', 'PRSHRTMP', 'IF C(A) = -0, SHORTMP FAILS TO GIVE -0.', line=1539)
# MULT BY .0006
W('42,3164', 0o34334, '', 'CAF', 'R2D1', 'GIVES MIN/10EXP5 MOD 60', line=1541)
W('42,3165', 0o54777, '', 'TS', 'DSPCOUNT', line=1542)
W('42,3166', 0o04662, '', 'TC', 'BANKCALL', 'DISPLAY MIN MOD 60', line=1543)
W('42,3167', 0o61133, '', 'CADR', 'DSPDECWD', kind='data', line=1544)
W('42,3170', 0o00006, '', 'EXTEND', '', 'MINUTES, SECONDS HAVE BEEN REMOVED', line=1545)
W('42,3171', 0o33213, '', 'DCA', 'HRCON1', line=1546)
W('42,3172', 0o52155, '', 'DXCH', 'MPAC', line=1547)
W('42,3173', 0o31007, '', 'CA', 'HITEMOUT', 'USE WHOLE HOURS', line=1548)
W('42,3174', 0o04431, '', 'TC', 'PRSHRTMP', 'IF C(A) = -0, SHORTMP FAILS TO GIVE -0.', line=1549)
# MULT BY .16384
W('42,3175', 0o34333, '', 'CAF', 'R1D1', 'GIVES HOURS/10EXP5', line=1551)
W('42,3176', 0o54777, '', 'TS', 'DSPCOUNT', line=1552)
W('42,3177', 0o04662, '', 'TC', 'BANKCALL', 'USE REGULAR DSPDECWD, WITH ROUND OFF.', line=1553)
W('42,3200', 0o61133, '', 'CADR', 'DSPDECWD', kind='data', line=1554)
W('42,3201', 0o00136, '', 'TC', 'ENTEXIT', line=1555)

W('42,3202', 0o25660, 'SECON1', '2DEC*', '1.666666666 E-4 B12*', '2EXP12/6000', kind='data', line=1557)
W('42,3203', 0o31742, kind='data', line=1557)
# Page 339
W('42,3204', 0o01727, 'SECON2', 'OCT', '01727', '.06 FOR SECONDS DISPLAY', kind='data', line=1559)
W('42,3205', 0o01217, '', 'OCT', '01217', kind='data', line=1560)
W('42,3206', 0o00011, 'MINCON2', 'OCT', '00011', '.0006 FOR MINUTES DISLPAY', kind='data', line=1561)
W('42,3207', 0o32445, '', 'OCT', '32445', kind='data', line=1562)
W('42,3210', 0o02104, 'MINCON1', 'OCT', '02104', '.066..66 UPPED BY 2EXP-28', kind='data', line=1563)
W('42,3211', 0o10422, '', 'OCT', '10422', kind='data', line=1564)
W('42,3212', 0o05174, 'HRCON1', '2DEC', '.16384', kind='data', line=1565)
W('42,3213', 0o13261, kind='data', line=1565)

W('42,3214', 0o00000, '', 'OCT', '00000', kind='data', line=1567)
W('42,3215', 0o00062, 'RNDCON', 'OCT', '00062', '.5 SEC', kind='data', line=1568)

W('42,3216', 0o04662, 'M/SOUT', 'TC', 'BANKCALL', 'READ FRESH DATA FOR HI AND LO INTO MPAC.', line=1571)
W('42,3217', 0o60655, '', 'CADR', 'READLO', 'MPAC+1.', kind='data', line=1572)
W('42,3220', 0o07226, '', 'TC', 'TPAGREE', 'MAKE DP DATA AGREE', line=1573)
W('42,3221', 0o10154, '', 'CCS', 'MPAC', 'IF MAG OF (MPAC, MPAC+1) G/ 59 M 59 S,', line=1574)
W('42,3222', 0o03224, '', 'TC', '+2', 'DISPLAY 59B59, WITH PROPER SIGN.', line=1575)
W('42,3223', 0o03255, '', 'TC', 'M/SNORM', 'MPAC = +0. L/ 59M58.5S', line=1576)
W('42,3224', 0o63312, '', 'AD', 'M/SCON1', '- HI PART OF (59M58.5S) +1  FOR CCS', line=1577)
W('42,3225', 0o10000, '', 'CCS', 'A', 'MAG OF MPAC - HI PART OF (59M58.5S)', line=1578)
W('42,3226', 0o03241, '', 'TC', 'M/SLIMIT', 'G/ 59M58.5S', line=1579)
W('42,3227', 0o03255, '', 'TC', 'M/SNORM', 'ORIGINAL MPAC = -0. L/ 59M58.5S', line=1580)
W('42,3230', 0o03255, '', 'TC', 'M/SNORM', 'L/ 59M58.5S', line=1581)
W('42,3231', 0o10155, '', 'CCS', 'MPAC +1', 'MAG OF MPAC = HI PART OF 59M58.5S', line=1582)
W('42,3232', 0o03234, '', 'TC', '+2', line=1583)
W('42,3233', 0o03255, '', 'TC', 'M/SNORM', 'MPAC+1 = +0. L/ 59M58.5S', line=1584)
W('42,3234', 0o63313, '', 'AD', 'M/SCON2', '- LO PART OF (59M58.5S) +1  FOR CCS', line=1585)
W('42,3235', 0o10000, '', 'CCS', 'A', 'MAG OF MPAC+1 - LO PART OF (59M58.5S)', line=1586)
W('42,3236', 0o03241, '', 'TC', 'M/SLIMIT', 'G/ 59M58.5S', line=1587)
W('42,3237', 0o03255, '', 'TC', 'M/SNORM', 'ORIGINAL MPAC+1 = -0. L/ 59M58.5S', line=1588)
W('42,3240', 0o03255, '', 'TC', 'M/SNORM', 'L/ 59M58.5S', line=1589)
W('42,3241', 0o10154, 'M/SLIMIT', 'CCS', 'MPAC', '= 59M58.5S    LIMIT', line=1590)
W('42,3242', 0o33315, '', 'CAF', 'M/SCON3', 'MPAC CANNOT BE +/- 0 AT THIS POINT.', line=1591)
W('42,3243', 0o03252, '', 'TC', '+LIMIT', 'FORCE MPAC, MPAC+1 TO +/- 59M58.5S', line=1592)
W('42,3244', 0o43315, '', 'CS', 'M/SCON3', line=1593)
W('42,3245', 0o54154, '', 'TS', 'MPAC', 'WILL DISPLAY 59M59S IN DSPDECNR', line=1594)
W('42,3246', 0o43316, '', 'CS', 'M/SCON3 +1', line=1595)
W('42,3247', 0o54155, 'LIMITCOM', 'TS', 'MPAC +1', line=1596)
W('42,3250', 0o33314, '', 'CAF', 'NORMADR', 'SET RETURN TO M/SNORM+1.', line=1597)
W('42,3251', 0o03333, '', 'TC', 'SEPSECNR +1', line=1598)
W('42,3252', 0o54154, '+LIMIT', 'TS', 'MPAC', line=1599)
W('42,3253', 0o33316, '', 'CAF', 'M/SCON3 +1', line=1600)
W('42,3254', 0o03247, '', 'TC', 'LIMITCOM', line=1601)
W('42,3255', 0o03317, 'M/SNORM', 'TC', 'SEPSEC', 'LEAVE FRACT SEC/60 IN MPAC,MPAC+1. LEAVE', line=1602)
# WHOLE MIN IN BIT13 OF LOTEMOUT AND ABOVE
W('42,3256', 0o33310, '', 'CAF', 'HISECON', 'USE ONLY FRACT SEC/60 MOD 60', line=1604)
W('42,3257', 0o07256, '', 'TC', 'SHORTMP', 'MULT BY .6 + 2EXP-14', line=1605)
W('42,3260', 0o46214, '', 'CS', 'THREE', 'GIVES SEC/100 MOD 60', line=1606)
W('42,3261', 0o26777, '', 'ADS', 'DSPCOUNT', 'DSPCOUNT ALREADY SET TO RXD1', line=1607)
W('42,3262', 0o04662, '', 'TC', 'BANKCALL', 'DISPLAY SEC MOD 60 IN D4D5.', line=1608)
# Page 340
W('42,3263', 0o61173, '', 'CADR', 'DSPDC2NR', kind='data', line=1610)
W('42,3264', 0o35021, '', 'CAF', 'ZERO', line=1611)
W('42,3265', 0o54124, '', 'TS', 'CODE', line=1612)
W('42,3266', 0o45016, '', 'CS', 'TWO', line=1613)
W('42,3267', 0o50117, '', 'INDEX', 'DECOUNT', line=1614)
W('42,3270', 0o64333, '', 'AD', 'R1D1', 'RXD3', line=1615)
W('42,3271', 0o54143, '', 'TS', 'COUNT', line=1616)
W('42,3272', 0o04662, '', 'TC', 'BANKCALL', 'BLANK MIDDLE CHAR', line=1617)
W('42,3273', 0o61227, '', 'CADR', 'DSPIN', kind='data', line=1618)
W('42,3274', 0o03350, '', 'TC', 'SEPMIN', 'REMOVE REST OF SECONDS', line=1619)
W('42,3275', 0o56155, '', 'XCH', 'MPAC +1', 'LEAVE FRACT MIN/60 IN MPAC+1', line=1620)
W('42,3276', 0o00006, '', 'EXTEND', '', 'USE ONLY FRACT MIN/60 MOD 60', line=1621)
W('42,3277', 0o73311, '', 'MP', 'HIMINCON', 'MULT BY .6 + 2EXP-7', line=1622)
W('42,3300', 0o52155, '', 'DXCH', 'MPAC', 'GIVES MIN/100 MOD 60', line=1623)
W('42,3301', 0o50117, '', 'INDEX', 'DECOUNT', line=1624)
W('42,3302', 0o34333, '', 'CAF', 'R1D1', 'RXD1', line=1625)
W('42,3303', 0o54777, '', 'TS', 'DSPCOUNT', line=1626)
W('42,3304', 0o04662, '', 'TC', 'BANKCALL', 'DISPLAY MIN MOD 60 IN D1D2.', line=1627)
W('42,3305', 0o61173, '', 'CADR', 'DSPDC2NR', kind='data', line=1628)
W('42,3306', 0o04701, '', 'TC', 'POSTJUMP', line=1629)
W('42,3307', 0o62570, '', 'CADR', 'DSPDCEND +2', kind='data', line=1630)

W('42,3310', 0o23147, 'HISECON', 'OCT', '23147', '.6 + 2EXP-14', kind='data', line=1632)
W('42,3311', 0o23346, 'HIMINCON', 'OCT', '23346', '.6 + 2EXP-7', kind='data', line=1633)

W('42,3312', 0o77753, 'M/SCON1', 'OCT', '77753', '- HI PART OF (59M58.5S)', kind='data', line=1635)
W('42,3313', 0o41126, 'M/SCON2', 'OCT', '41126', '- LO PART OF (59M58.5S)', kind='data', line=1636)
W('42,3314', 0o03256, 'NORMADR', 'ADRES', 'M/SNORM +1', kind='data', line=1637)
W('42,3315', 0o00025, 'M/SCON3', 'OCT', '00025', '59M 59.5S', kind='data', line=1638)
W('42,3316', 0o37016, '', 'OCT', '37016', kind='data', line=1639)

W('42,3317', 0o10155, 'SEPSEC', 'CCS', 'MPAC +1', 'IF +, ROUND BY ADDING .5 SEC', line=1641)
W('42,3320', 0o13327, '', 'TCF', 'POSEC', 'IF -, ROUND BY SUBTRACTING .5 SEC', line=1642)
W('42,3321', 0o13327, '', 'TCF', 'POSEC', 'FINDS TIME IN MPAC, MPAC+1', line=1643)
W('42,3322', 0o13323, '', 'TCF', '+1', 'ROUNDS OFF BY +/- .5 SEC', line=1644)
W('42,3323', 0o00006, '', 'EXTEND', '', 'LEAVES WHOLE MIN IN BIT13 OF', line=1645)
W('42,3324', 0o43215, '', 'DCS', 'RNDCON -1', 'LOTEMOUT AND ABOVE.', line=1646)
W('42,3325', 0o20155, 'SEPSEC1', 'DAS', 'MPAC', 'LEAVES FRACT SEC/60 IN MPAC, MPAC+1.', line=1647)
W('42,3326', 0o13332, '', 'TCF', 'SEPSECNR', line=1648)
W('42,3327', 0o00006, 'POSEC', 'EXTEND', line=1649)
W('42,3330', 0o33215, '', 'DCA', 'RNDCON -1', line=1650)
W('42,3331', 0o13325, '', 'TCF', 'SEPSEC1', line=1651)
W('42,3332', 0o56002, 'SEPSECNR', 'XCH', 'Q', 'THIS ENTRY AVOIDS ROUNDING BY .5 SEC', line=1652)
W('42,3333', 0o54144, '', 'TS', 'SEPSCRET', line=1653)
W('42,3334', 0o07052, '', 'TC', 'DMP', 'MULT BY 2EXP12/6000', line=1654)
W('42,3335', 0o03202, '', 'ADRES', 'SECON1', 'GIVES FRACT SEC/60 IN BIT12 OF MPAC+1', kind='data', line=1655)
W('42,3336', 0o00006, '', 'EXTEND', '', 'AND BELOW.', line=1656)
W('42,3337', 0o30155, '', 'DCA', 'MPAC', 'SAVE MINUTES AND HOURS', line=1657)
W('42,3340', 0o53010, '', 'DXCH', 'HITEMOUT', line=1658)
# Page 341
W('42,3341', 0o04420, '', 'TC', 'TPSL1', line=1660)
W('42,3342', 0o04420, '', 'TC', 'TPSL1', 'GIVES FRACT SEC/60 IN MPAC+1, MPAC+2.', line=1661)
W('42,3343', 0o35021, '', 'CAF', 'ZERO', line=1662)
W('42,3344', 0o56156, '', 'XCH', 'MPAC +2', 'LEAVE FRACT SEC/60 IN MPAC, MPAC+1.', line=1663)
W('42,3345', 0o56155, '', 'XCH', 'MPAC +1', line=1664)
W('42,3346', 0o56154, '', 'XCH', 'MPAC', line=1665)
W('42,3347', 0o00144, '', 'TC', 'SEPSCRET', line=1666)

W('42,3350', 0o56002, 'SEPMIN', 'XCH', 'Q', 'FINDS WHOLE MINUTES IN BIT13', line=1669)
W('42,3351', 0o54144, '', 'TS', 'SEPMNRET', 'OF LOTEMOUT AND ABOVE.', line=1670)
W('42,3352', 0o31010, '', 'CA', 'LOTEMOUT', 'REMOVES REST OF SECONDS.', line=1671)
W('42,3353', 0o00006, '', 'EXTEND', '', 'LEAVES FRACT MIN/60 IN MPAC+1.', line=1672)
W('42,3354', 0o75015, '', 'MP', 'BIT3', 'LEAVES WHOLE HOURS IN MPAC.', line=1673)
W('42,3355', 0o00006, '', 'EXTEND', '', 'SR 12, THROW AWAY LP.', line=1674)
W('42,3356', 0o75003, '', 'MP', 'BIT13', 'SR 2, TAKE FROM LP. = SL 12.', line=1675)
W('42,3357', 0o22155, '', 'LXCH', 'MPAC +1', 'THIS FORCES BITS 12-1 TO 0 IF +.', line=1676)
# FORCES BITS 12-1 TO 1 IF -.
W('42,3360', 0o31007, '', 'CA', 'HITEMOUT', line=1678)
W('42,3361', 0o54154, '', 'TS', 'MPAC', line=1679)
W('42,3362', 0o07052, '', 'TC', 'DMP', 'MULT BY 1/15', line=1680)
W('42,3363', 0o03210, '', 'ADRES', 'MINCON1', 'GIVES FRACT MIN/60 IN MPAC+1.', kind='data', line=1681)
W('42,3364', 0o00144, 'ENDSPMIN', 'TC', 'SEPMNRET', 'GIVES WHOLE HOURS IN MPAC.', line=1682)

# THIS IS A SPECIAL PURPOSE VERB FOR DISPLAYING A DOUBLE PRECISION AGC
# WORD AS 10 DECIMAL DIGITS ON THE AGC DISPLAY PANEL.  IT CAN BE USED WITH
# ANY NOUN, EXCEPT MIXED NOUNS. IT DISPLAYS THE CONTENTS
# OF THE REGISTER NOUNADD IS POINTING TO .  IF USED WITH NOUNS WHICH ARE
# INHERENTLY NOT DP SUCH AS THE CDU COUNTERS THE DISPLAY WILL BE GARBAGE.
# DISPLAY IS IN R1 AND R2 ONLY WITH THE SIGN IN R1.

#   SETLOC ENDRDLO +1

#   COUNT 40/PIN

W('40,2677', 0o50140, 'DSPDPDEC', 'INDEX', 'MIXBR', line=1697)
W('40,2700', 0o02700, '', 'TC', '+0', line=1698)
W('40,2701', 0o02703, '', 'TC', '+2', 'NORMAL NOUN', line=1699)
W('40,2702', 0o03325, '', 'TC', 'DSPALARM', line=1700)
W('40,2703', 0o00006, '', 'EXTEND', line=1701)
W('40,2704', 0o50145, '', 'INDEX', 'NOUNADD', line=1702)
W('40,2705', 0o30001, '', 'DCA', '0', line=1703)
W('40,2706', 0o52155, '', 'DXCH', 'MPAC', line=1704)
W('40,2707', 0o34333, '', 'CAF', 'R1D1', line=1705)
W('40,2710', 0o54777, '', 'TS', 'DSPCOUNT', line=1706)
W('40,2711', 0o35021, '', 'CAF', 'ZERO', line=1707)
W('40,2712', 0o54156, '', 'TS', 'MPAC +2', line=1708)
W('40,2713', 0o07226, '', 'TC', 'TPAGREE', line=1709)
# Page 342
W('40,2714', 0o03200, '', 'TC', 'DSP2DEC', line=1711)
W('40,2715', 0o00136, 'ENDDPDEC', 'TC', 'ENTEXIT', line=1712)

# Page 343

# LOAD VERBS           IF ALARM CONDITION IS DETECTED DURING EXECUTE,
# CHECK FAIL LIGHT IS TURNED ON AND ENDOFJOB. IF ALARM CONDITION IS
# DETECTED DURING ENTER OF DATA, CHECK FAIL IS TURNED ON AND IT RECYCLES
# TO EXECUTE OF ORIGINAL LOAD VERB.  RECYCLE CAUSED BY  1) DECIMAL MACHINE
# CADR  2) MIXTURE OF OCTAL/DECIMAL DATA  3) OCTAL DATA INTO DECIMAL
# ONLY NOUN  4) DEC DATA INTO OCT ONLY NOUN  5) DATA TOO LARGE FOR SCALE
# 6) FEWER THAN 3 DATA WORDS LOADED FOR HRS, MIN, SEC NOUN.8(2)-(6) ALARM
# AND RECYCLE OCCUR AT FINAL ENTER OF SET. (1) ALARM AND RECYCLE OCCUR AT
# ENTER OF CADR.

#   SETLOC ENDRTOUT

#   COUNT 41/PIN

W('41,2616', 0o45016, 'ABCLOAD', 'CS', 'TWO', line=1731)
W('41,2617', 0o02424, '', 'TC', 'COMPTEST', line=1732)
W('41,2620', 0o02460, '', 'TC', 'NOUNTEST', 'TEST IF NOUN CAN BE LOADED.', line=1733)
W('41,2621', 0o33006, '', 'CAF', 'VBSP1LD', line=1734)
W('41,2622', 0o02337, '', 'TC', 'UPDATVB -1', line=1735)
W('41,2623', 0o02303, '', 'TC', 'REQDATX', line=1736)
W('41,2624', 0o33007, '', 'CAF', 'VBSP2LD', line=1737)
W('41,2625', 0o02337, '', 'TC', 'UPDATVB -1', line=1738)
W('41,2626', 0o02305, '', 'TC', 'REQDATY', line=1739)
W('41,2627', 0o33010, '', 'CAF', 'VBSP3LD', line=1740)
W('41,2630', 0o02337, '', 'TC', 'UPDATVB -1', line=1741)
W('41,2631', 0o02307, '', 'TC', 'REQDATZ', line=1742)

W('41,2632', 0o46211, 'PUTXYZ', 'CS', 'SIX', 'TEST THAT THE 3 DATA WORDS LOADED ARE', line=1745)
W('41,2633', 0o03011, '', 'TC', 'ALLDC/OC', 'ALL DEC OR ALL OCT.', line=1746)
W('41,2634', 0o00006, '', 'EXTEND', line=1747)
W('41,2635', 0o32114, '', 'DCA', 'LODNNLOC', 'SWITCH BANKS TO NOUN TABLE READING', line=1748)
W('41,2636', 0o52006, '', 'DXCH', 'Z', 'ROUTINE.', line=1749)
W('41,2637', 0o35021, '', 'CAF', 'ZERO', 'X COMP', line=1750)
W('41,2640', 0o03075, '', 'TC', 'PUTCOM', line=1751)
W('41,2641', 0o50145, '', 'INDEX', 'NOUNADD', line=1752)
W('41,2642', 0o54000, '', 'TS', '0', line=1753)
W('41,2643', 0o35017, '', 'CAF', 'ONE', 'Y COMP', line=1754)
W('41,2644', 0o03075, '', 'TC', 'PUTCOM', line=1755)
W('41,2645', 0o50145, '', 'INDEX', 'NOUNADD', line=1756)
W('41,2646', 0o54001, '', 'TS', '1', line=1757)
W('41,2647', 0o35016, '', 'CAF', 'TWO', 'Z COMP', line=1758)
W('41,2650', 0o03075, '', 'TC', 'PUTCOM', line=1759)
W('41,2651', 0o50145, '', 'INDEX', 'NOUNADD', line=1760)
W('41,2652', 0o54002, '', 'TS', '2', line=1761)
W('41,2653', 0o45023, '', 'CS', 'SEVEN', 'IF NOUN 7 HAS JUST BEEN LOADED, SET', line=1762)
W('41,2654', 0o61002, '', 'AD', 'NOUNREG', ' FLAG BITS AS SPECIFIED.', line=1763)
W('41,2655', 0o00006, '', 'EXTEND', line=1764)
W('41,2656', 0o12660, '', 'BZF', '+2', line=1765)
# Page 344
W('41,2657', 0o02775, '', 'TC', 'LOADLV', line=1767)
W('41,2660', 0o31003, '', 'CA', 'XREG', 'ECADR OF FLAG WORD.', line=1768)
W('41,2661', 0o04320, '', 'TC', 'SETNCADR +1', ' SET EBANK, NOUNADD.', line=1769)
W('41,2662', 0o31005, '', 'CA', 'ZREG', 'ZERO TO RESET BITS. NON-ZERO TO SET BITS', line=1770)
W('41,2663', 0o00004, '', 'INHINT', line=1771)
W('41,2664', 0o00006, '', 'EXTEND', line=1772)
W('41,2665', 0o12674, '', 'BZF', 'BITSOFF', line=1773)
W('41,2666', 0o50145, '', 'INDEX', 'NOUNADD', line=1774)
W('41,2667', 0o40000, '', 'CS', '0', line=1775)
W('41,2670', 0o71004, '', 'MASK', 'YREG', 'BITS TO BE PROCESSED.', line=1776)
W('41,2671', 0o50145, '', 'INDEX', 'NOUNADD', line=1777)
W('41,2672', 0o26000, '', 'ADS', '0', 'SET BITS.', line=1778)
W('41,2673', 0o02701, '', 'TC', 'BITSOFF1', line=1779)
W('41,2674', 0o41004, 'BITSOFF', 'CS', 'YREG', 'BITS TO BE PROCESSED.', line=1780)
W('41,2675', 0o50145, '', 'INDEX', 'NOUNADD', line=1781)
W('41,2676', 0o70000, '', 'MASK', '0', line=1782)
W('41,2677', 0o50145, '', 'INDEX', 'NOUNADD', line=1783)
W('41,2700', 0o54000, '', 'TS', '0', 'RESET BITS.', line=1784)
W('41,2701', 0o00003, 'BITSOFF1', 'RELINT', line=1785)
W('41,2702', 0o02775, '', 'TC', 'LOADLV', line=1786)

W('41,2703', 0o45017, 'ABLOAD', 'CS', 'ONE', line=1788)
W('41,2704', 0o02424, '', 'TC', 'COMPTEST', line=1789)
W('41,2705', 0o02460, '', 'TC', 'NOUNTEST', 'TEST IF NOUN CAN BE LOADED.', line=1790)
W('41,2706', 0o33006, '', 'CAF', 'VBSP1LD', line=1791)
W('41,2707', 0o02337, '', 'TC', 'UPDATVB -1', line=1792)
W('41,2710', 0o02303, '', 'TC', 'REQDATX', line=1793)
W('41,2711', 0o33007, '', 'CAF', 'VBSP2LD', line=1794)
W('41,2712', 0o02337, '', 'TC', 'UPDATVB -1', line=1795)
W('41,2713', 0o02305, '', 'TC', 'REQDATY', line=1796)
W('41,2714', 0o45022, 'PUTXY', 'CS', 'FIVE', 'TEST THAT THE 2 DATA WORDS LOADED ARE', line=1797)
W('41,2715', 0o03011, '', 'TC', 'ALLDC/OC', 'ALL DEC OR ALL OCT.', line=1798)
W('41,2716', 0o00006, '', 'EXTEND', line=1799)
W('41,2717', 0o32114, '', 'DCA', 'LODNNLOC', 'SWITCH BANKS TO NOUN TABLE READING', line=1800)
W('41,2720', 0o52006, '', 'DXCH', 'Z', 'ROUTINE.', line=1801)
W('41,2721', 0o35021, '', 'CAF', 'ZERO', 'X COMP', line=1802)
W('41,2722', 0o03075, '', 'TC', 'PUTCOM', line=1803)
W('41,2723', 0o50145, '', 'INDEX', 'NOUNADD', line=1804)
W('41,2724', 0o54000, '', 'TS', '0', line=1805)
W('41,2725', 0o35017, '', 'CAF', 'ONE', 'Y COMP', line=1806)
W('41,2726', 0o03075, '', 'TC', 'PUTCOM', line=1807)
W('41,2727', 0o50145, '', 'INDEX', 'NOUNADD', line=1808)
W('41,2730', 0o54001, '', 'TS', '1', line=1809)
W('41,2731', 0o02775, '', 'TC', 'LOADLV', line=1810)

W('41,2732', 0o02303, 'ALOAD', 'TC', 'REQDATX', line=1812)
W('41,2733', 0o00006, '', 'EXTEND', line=1813)
W('41,2734', 0o32114, '', 'DCA', 'LODNNLOC', 'SWITCH BANKS TO NOUN TABLE READING', line=1814)
W('41,2735', 0o52006, '', 'DXCH', 'Z', 'ROUTINE.', line=1815)
W('41,2736', 0o35021, '', 'CAF', 'ZERO', 'X COMP', line=1816)
# Page 345
W('41,2737', 0o03075, '', 'TC', 'PUTCOM', line=1818)
W('41,2740', 0o50145, '', 'INDEX', 'NOUNADD', line=1819)
W('41,2741', 0o54000, '', 'TS', '0', line=1820)
W('41,2742', 0o02775, '', 'TC', 'LOADLV', line=1821)

W('41,2743', 0o45017, 'BLOAD', 'CS', 'ONE', line=1823)
W('41,2744', 0o02424, '', 'TC', 'COMPTEST', line=1824)
W('41,2745', 0o35001, '', 'CAF', 'BIT15', 'SET CLPASS FOR PASS0 ONLY', line=1825)
W('41,2746', 0o55015, '', 'TS', 'CLPASS', line=1826)
W('41,2747', 0o02305, '', 'TC', 'REQDATY', line=1827)
W('41,2750', 0o00006, '', 'EXTEND', line=1828)
W('41,2751', 0o32114, '', 'DCA', 'LODNNLOC', 'SWITCH BANKS TO NOUN TABLE READING', line=1829)
W('41,2752', 0o52006, '', 'DXCH', 'Z', 'ROUTINE.', line=1830)
W('41,2753', 0o35017, '', 'CAF', 'ONE', line=1831)
W('41,2754', 0o03075, '', 'TC', 'PUTCOM', line=1832)
W('41,2755', 0o50145, '', 'INDEX', 'NOUNADD', line=1833)
W('41,2756', 0o54001, '', 'TS', '1', line=1834)
W('41,2757', 0o02775, '', 'TC', 'LOADLV', line=1835)

W('41,2760', 0o45016, 'CLOAD', 'CS', 'TWO', line=1837)
W('41,2761', 0o02424, '', 'TC', 'COMPTEST', line=1838)
W('41,2762', 0o35001, '', 'CAF', 'BIT15', 'SET CLPASS FOR PASS0 ONLY', line=1839)
W('41,2763', 0o55015, '', 'TS', 'CLPASS', line=1840)
W('41,2764', 0o02307, '', 'TC', 'REQDATZ', line=1841)
W('41,2765', 0o00006, '', 'EXTEND', line=1842)
W('41,2766', 0o32114, '', 'DCA', 'LODNNLOC', 'SWITCH BANKS TO NOUN TABLE READING', line=1843)
W('41,2767', 0o52006, '', 'DXCH', 'Z', 'ROUTINE.', line=1844)
W('41,2770', 0o35016, '', 'CAF', 'TWO', line=1845)
W('41,2771', 0o03075, '', 'TC', 'PUTCOM', line=1846)
W('41,2772', 0o50145, '', 'INDEX', 'NOUNADD', line=1847)
W('41,2773', 0o54002, '', 'TS', '2', line=1848)
W('41,2774', 0o02775, '', 'TC', 'LOADLV', line=1849)

W('41,2775', 0o35021, 'LOADLV', 'CAF', 'ZERO', line=1851)
W('41,2776', 0o55000, '', 'TS', 'DECBRNCH', line=1852)
W('41,2777', 0o45021, '', 'CS', 'ZERO', line=1853)
W('41,3000', 0o55014, '', 'TS', 'LOADSTAT', line=1854)
W('41,3001', 0o04473, '', 'TC', 'RELDSP', 'RELEASE FOR PRIORITY DISPLAY PROBLEM.', line=1855)
W('41,3002', 0o44374, '', 'CS', 'VD1', 'TO BLOCK NUMERICAL CHARACTERS AND', line=1856)
W('41,3003', 0o54777, '', 'TS', 'DSPCOUNT', 'CLEARS AFTER A COMPLETED LOAD', line=1857)
W('41,3004', 0o04701, '', 'TC', 'POSTJUMP', 'AFTER COMPLETED LOAD, GO TO RECALTST', line=1858)
W('41,3005', 0o61454, '', 'CADR', 'RECALTST', 'TO SEE IF THERE IS RECALL FROM ENDIDLE.', kind='data', line=1859)

W('41,3006', 0o00025, 'VBSP1LD', 'DEC', '21', 'VB21 = ALOAD', kind='data', line=1861)
W('41,3007', 0o00026, 'VBSP2LD', 'DEC', '22', 'VB22 = BLOAD', kind='data', line=1862)
W('41,3010', 0o00027, 'VBSP3LD', 'DEC', '23', 'VB23 = CLOAD', kind='data', line=1863)

W('41,3011', 0o54117, 'ALLDC/OC', 'TS', 'DECOUNT', 'TESTS THAT DATA WORDS LOADED ARE EITHER', line=1865)
W('41,3012', 0o41000, '', 'CS', 'DECBRNCH', 'ALL DEC OR ALL OCT. ALARMS IF NOT.', line=1866)
# Page 346
W('41,3013', 0o54021, '', 'TS', 'SR', line=1868)
W('41,3014', 0o40021, '', 'CS', 'SR', line=1869)
W('41,3015', 0o40021, '', 'CS', 'SR', 'SHIFTED RIGHT 2', line=1870)
W('41,3016', 0o10000, '', 'CCS', 'A', 'DEC COMP BITS IN LOW 3', line=1871)
W('41,3017', 0o13021, '', 'TCF', '+2', 'SOME ONES IN LOW 3', line=1872)
W('41,3020', 0o00002, '', 'TC', 'Q', 'ALL ZEROS. ALL OCTAL.  OK', line=1873)
W('41,3021', 0o60117, '', 'AD', 'DECOUNT', 'DEC COMP = 7 FOR 3COMP, =6 FOR 2COMP', line=1874)
W('41,3022', 0o00006, '', 'EXTEND', '', '(BUT IT HAS BEEN DECREMENTED BY CCS)', line=1875)
W('41,3023', 0o13025, '', 'BZF', '+2', 'MUST MATCH 6 FOR 3COMP, 5 FOR 2COMP.', line=1876)
W('41,3024', 0o04161, '', 'TC', 'ALMCYCLE', 'ALARM AND RECYCLE.', line=1877)
W('41,3025', 0o00002, 'GOQ', 'TC', 'Q', 'ALL REQUIRED ARE DEC. OK', line=1878)

W('41,3026', 0o56002, 'SFRUTNOR', 'XCH', 'Q', 'GETS SF ROUTINE NUMBER FOR NORMAL CASE', line=1881)
W('41,3027', 0o54114, '', 'TS', 'EXITEM', 'CANT USE L FOR RETURN. TSTFORDP USES L.', line=1882)
W('41,3030', 0o34363, '', 'CAF', 'MID5', line=1883)
W('41,3031', 0o70147, '', 'MASK', 'NNTYPTEM', line=1884)
W('41,3032', 0o04336, '', 'TC', 'RIGHT5', line=1885)
W('41,3033', 0o00114, '', 'TC', 'EXITEM', 'SF ROUTINE NUMBER IN A', line=1886)

W('41,3034', 0o56002, 'SFRUTMIX', 'XCH', 'Q', 'GETS SF ROUTINE NUMBER FOR MIXED CASE', line=1888)
W('41,3035', 0o54114, '', 'TS', 'EXITEM', line=1889)
W('41,3036', 0o50117, '', 'INDEX', 'DECOUNT', line=1890)
W('41,3037', 0o33066, '', 'CAF', 'DISPLACE', 'PUT TC GOQ, TC RIGHT5, OR TC LEFT5 IN L', line=1891)
W('41,3040', 0o54001, '', 'TS', 'L', line=1892)
W('41,3041', 0o50117, '', 'INDEX', 'DECOUNT', line=1893)
W('41,3042', 0o34362, '', 'CAF', 'LOW5', 'LOW5, MID5, OR HI5 IN A', line=1894)
W('41,3043', 0o70153, '', 'MASK', 'RUTMXTEM', 'GET HI5, MID5, OR LOW5 OF RUTMXTAB ENTRY', line=1895)
W('41,3044', 0o50001, '', 'INDEX', 'L', line=1896)
W('41,3045', 0o00000, '', 'TC', '0', line=1897)
# DO TC GOQ(DECOUNT=0), DO TC RIGHT5(DECOUNT=1). DO TC LEFT5(DECOUNT=2).
W('41,3046', 0o00114, 'SFRET1', 'TC', 'EXITEM', 'SF ROUTINE NUMBER IN A', line=1899)

W('41,3047', 0o56002, 'SFCONUM', 'XCH', 'Q', 'GETS 2X( SF CONSTANT NUMBER)', line=1901)
W('41,3050', 0o54114, '', 'TS', 'EXITEM', line=1902)
W('41,3051', 0o50140, '', 'INDEX', 'MIXBR', line=1903)
W('41,3052', 0o03052, '', 'TC', '+0', line=1904)
W('41,3053', 0o03071, '', 'TC', 'CONUMNOR', 'NORMAL NOUN', line=1905)
W('41,3054', 0o50117, '', 'INDEX', 'DECOUNT', 'MIXED NOUN', line=1906)
W('41,3055', 0o33066, '', 'CAF', 'DISPLACE', line=1907)
W('41,3056', 0o54001, '', 'TS', 'L', 'PUT TC GOQ, TC RIGHT5, OR TC LEFT5 IN L', line=1908)
W('41,3057', 0o50117, '', 'INDEX', 'DECOUNT', line=1909)
W('41,3060', 0o34362, '', 'CAF', 'LOW5', line=1910)
W('41,3061', 0o70147, '', 'MASK', 'NNTYPTEM', line=1911)
W('41,3062', 0o50001, '', 'INDEX', 'L', line=1912)
W('41,3063', 0o00000, '', 'TC', '0', line=1913)
# DO TC GOQ(DECOUNT=0), DO TC RIGHT5(DECOUNT=1), DO TC LEFT5(DECOUNT=2).
W('41,3064', 0o60000, 'SFRET', 'DOUBLE', '', '2X(SF CONSTANT NUMBER) IN A', line=1915)
W('41,3065', 0o00114, '', 'TC', 'EXITEM', line=1916)

# Page 347

W('41,3066', 0o03025, 'DISPLACE', 'TC', 'GOQ', line=1920)
W('41,3067', 0o04336, '', 'TC', 'RIGHT5', line=1921)
W('41,3070', 0o04345, '', 'TC', 'LEFT5', line=1922)

W('41,3071', 0o34362, 'CONUMNOR', 'CAF', 'LOW5', 'NORMAL NOUN ALWAYS GETS LOW 5 OF', line=1924)
W('41,3072', 0o70147, '', 'MASK', 'NNTYPTEM', 'NNTYPTAB FOR SF CONUM.', line=1925)
W('41,3073', 0o60000, '', 'DOUBLE', line=1926)
W('41,3074', 0o00114, '', 'TC', 'EXITEM', '2X( SF CONSTANT NUMBER) IN A', line=1927)

W('41,3075', 0o54117, 'PUTCOM', 'TS', 'DECOUNT', line=1930)
W('41,3076', 0o56002, '', 'XCH', 'Q', line=1931)
W('41,3077', 0o54115, '', 'TS', 'DECRET', line=1932)
W('41,3100', 0o35021, '', 'CAF', 'ZERO', line=1933)
W('41,3101', 0o54162, '', 'TS', 'MPAC+6', line=1934)
W('41,3102', 0o50117, '', 'INDEX', 'DECOUNT', line=1935)
W('41,3103', 0o57006, '', 'XCH', 'XREGLP', line=1936)
W('41,3104', 0o54155, '', 'TS', 'MPAC +1', line=1937)
W('41,3105', 0o50117, '', 'INDEX', 'DECOUNT', line=1938)
W('41,3106', 0o57003, '', 'XCH', 'XREG', line=1939)
W('41,3107', 0o54154, '', 'TS', 'MPAC', line=1940)
W('41,3110', 0o50140, '', 'INDEX', 'MIXBR', line=1941)
W('41,3111', 0o03111, '', 'TC', '+0', line=1942)
W('41,3112', 0o03137, '', 'TC', 'PUTNORM', 'NORMAL NOUN', line=1943)
# IF MIXNOUN, PLACE ADDRESS FOR COMPONENT K INTO NOUNADD, SET EBANK BITS.
W('41,3113', 0o50117, '', 'INDEX', 'DECOUNT', 'GET IDADDTAB ENTRY FOR COMPONENT K', line=1945)
W('41,3114', 0o30150, '', 'CA', 'IDAD1TEM', '        OF NOUN.', line=1946)
W('41,3115', 0o74372, '', 'MASK', 'LOW11', '(ECADR)SUBK FOR CURRENT COMP OF NOUN', line=1947)
W('41,3116', 0o04317, '', 'TC', 'SETNCADR', 'ECADR INTO NOUNCADR. SETS EB. NOUNADD.', line=1948)
W('41,3117', 0o00006, '', 'EXTEND', '', 'C(NOUNADD) IN A UPON RETURN', line=1949)
W('41,3120', 0o60117, '', 'SU', 'DECOUNT', 'PLACE (ESUBK)-K INTO NOUNADD', line=1950)
W('41,3121', 0o54145, '', 'TS', 'NOUNADD', line=1951)
W('41,3122', 0o11000, '', 'CCS', 'DECBRNCH', line=1952)
W('41,3123', 0o03174, '', 'TC', 'PUTDECSF', '+  DEC', line=1953)
W('41,3124', 0o02452, '', 'TC', 'DCTSTCYC', '+0 OCTAL', line=1954)
W('41,3125', 0o03034, '', 'TC', 'SFRUTMIX', 'TEST IF DEC ONLY BIT = 1. IF SO,', line=1955)
W('41,3126', 0o02261, '', 'TC', 'DPTEST', 'ALARM AND RECYCLE. IF NOT, CONTINUE.', line=1956)
W('41,3127', 0o03155, '', 'TC', 'PUTCOM2', 'NO DP', line=1957)
# TEST FOR DP SCALE FOR OCT LOAD. IF SO,
# +0 INTO MAJOR PART. SET NOUNADD FOR
# LOADING OCTAL WORD INTO MINOR PART.
W('41,3130', 0o24145, 'PUTDPCOM', 'INCR', 'NOUNADD', 'DP  (ESUBK)-K+1  OR  E+1', line=1961)
W('41,3131', 0o30145, '', 'CA', 'NOUNADD', 'NOUNADD NOW SET FOR MINOR PART', line=1962)
W('41,3132', 0o26117, '', 'ADS', 'DECOUNT', '(ESUBK)+1  OR  E+1  INTO DECOUNT', line=1963)
W('41,3133', 0o35021, '', 'CAF', 'ZERO', 'NOUNADD SET FOR MINOR PART', line=1964)
W('41,3134', 0o50117, '', 'INDEX', 'DECOUNT', line=1965)
W('41,3135', 0o53777, '', 'TS', '0 -1', 'ZERO MAJOR PART(ESUBK OR E)', line=1966)
W('41,3136', 0o03155, '', 'TC', 'PUTCOM2', line=1967)

W('41,3137', 0o04325, 'PUTNORM', 'TC', 'SETNADD', 'ECADR FROM NOUNCADR. SETS EB, NOUNADD.', line=1969)
# Page 348
W('41,3140', 0o11000, '', 'CCS', 'DECBRNCH', line=1971)
W('41,3141', 0o03174, '', 'TC', 'PUTDECSF', '+  DEC', line=1972)
W('41,3142', 0o02452, '', 'TC', 'DCTSTCYC', '+0 OCTAL', line=1973)
W('41,3143', 0o03026, '', 'TC', 'SFRUTNOR', 'TEST IF DEC ONLY BIT = 1. IF SO,', line=1974)
W('41,3144', 0o02261, '', 'TC', 'DPTEST', 'ALARM AND RECYCLE. IF NOT, CONTINUE.', line=1975)
W('41,3145', 0o03151, '', 'TC', 'PUTCOM2 -4', 'NO DP', line=1976)
W('41,3146', 0o35021, '', 'CAF', 'ZERO', 'DP', line=1977)
W('41,3147', 0o54117, '', 'TS', 'DECOUNT', line=1978)
W('41,3150', 0o03130, '', 'TC', 'PUTDPCOM', line=1979)

W('41,3151', 0o30146, '', 'CA', 'NNADTEM', line=1981)
W('41,3152', 0o65017, '', 'AD', 'ONE', 'IF NNADTEM = -1. CHANNEL TO BE SPECIFIED', line=1982)
W('41,3153', 0o00006, '', 'EXTEND', line=1983)
W('41,3154', 0o13161, '', 'BZF', 'CHANLOAD', line=1984)
W('41,3155', 0o56154, 'PUTCOM2', 'XCH', 'MPAC', line=1985)
W('41,3156', 0o00115, '', 'TC', 'DECRET', line=1986)

#   EBANK= DSPCOUNT
W('41,3157', 0o02126, 'GTSFINLC', '2CADR', 'GTSFIN', kind='data', line=1989)
W('41,3160', 0o64101, kind='data', line=1989)

W('41,3161', 0o45023, 'CHANLOAD', 'CS', 'SEVEN', 'DONT LOAD CHAN 7. (IT = SUPERBANK).', line=1992)
W('41,3162', 0o61017, '', 'AD', 'NOUNCADR', line=1993)
W('41,3163', 0o00006, '', 'EXTEND', line=1994)
W('41,3164', 0o12775, '', 'BZF', 'LOADLV', line=1995)
W('41,3165', 0o31017, '', 'CA', 'NOUNCADR', line=1996)
W('41,3166', 0o75046, '', 'MASK', 'LOW9', line=1997)
W('41,3167', 0o56154, '', 'XCH', 'MPAC', line=1998)
W('41,3170', 0o00006, '', 'EXTEND', line=1999)
W('41,3171', 0o50154, '', 'INDEX', 'MPAC', line=2000)
W('41,3172', 0o01000, '', 'WRITE', '0', line=2001)
W('41,3173', 0o02775, '', 'TC', 'LOADLV', line=2002)

# PUTDECSF FINDS MIXBR AND DECOUNT STILL SET FROM PUTCOM

W('41,3174', 0o03047, 'PUTDECSF', 'TC', 'SFCONUM', '2X(SF CON NUMB) IN A', line=2007)
W('41,3175', 0o54123, '', 'TS', 'SFTEMP1', line=2008)
W('41,3176', 0o00006, '', 'EXTEND', '', 'SWITCH BANKS TO SF CONSTANT TABLE', line=2009)
W('41,3177', 0o33160, '', 'DCA', 'GTSFINLC', 'READING ROUTINE.', line=2010)
W('41,3200', 0o52006, '', 'DXCH', 'Z', 'LOADS SFTEMP1. SFTEMP2.', line=2011)
W('41,3201', 0o50140, '', 'INDEX', 'MIXBR', line=2012)
W('41,3202', 0o03202, '', 'TC', '+0', line=2013)
W('41,3203', 0o03206, '', 'TC', 'PUTSFNOR', line=2014)
W('41,3204', 0o03034, '', 'TC', 'SFRUTMIX', line=2015)
W('41,3205', 0o03207, '', 'TC', 'PUTDCSF2', line=2016)
W('41,3206', 0o03026, 'PUTSFNOR', 'TC', 'SFRUTNOR', line=2017)

W('41,3207', 0o50000, 'PUTDCSF2', 'INDEX', 'A', line=2019)
# Page 349
W('41,3210', 0o33212, '', 'CAF', 'SFINTABR', line=2021)
W('41,3211', 0o04704, '', 'TC', 'BANKJUMP', 'SWITCH BANKS FOR EXPANSHION ROOM', line=2022)
W('41,3212', 0o62350, 'SFINTABR', 'CADR', 'GOALMCYC', 'ALARM AND RECYCLE IF DEC LOAD', kind='data', line=2023)
# WITH OCTAL ONLY NOUN.
W('41,3213', 0o60776, '', 'CADR', 'BINROUND', kind='data', line=2025)
W('41,3214', 0o60716, '', 'CADR', 'DEGINSF', kind='data', line=2026)
W('41,3215', 0o60766, '', 'CADR', 'ARTHINSF', kind='data', line=2027)
W('41,3216', 0o61021, '', 'CADR', 'DPINSF', kind='data', line=2028)
W('41,3217', 0o61046, '', 'CADR', 'DPINSF2', kind='data', line=2029)
W('41,3220', 0o61004, '', 'CADR', 'OPTDEGIN', kind='data', line=2030)
W('41,3221', 0o61021, '', 'CADR', 'DPINSF', 'SAME AS ARITHDP1', kind='data', line=2031)
W('41,3222', 0o65365, '', 'CADR', 'HMSIN', kind='data', line=2032)
W('41,3223', 0o61325, '', 'CADR', 'DSPALARM', 'MIN/SEC CANT BE LOADED.', kind='data', line=2033)
W('41,3224', 0o61053, '', 'CADR', 'DPINSF4', kind='data', line=2034)
W('41,3225', 0o61001, '', 'CADR', 'ARTIN1SF', kind='data', line=2035)
W('41,3226', 0o61325, '', 'CADR', 'DSPALARM', '2INTOUT CANT BE LOADED.', kind='data', line=2036)
W('41,3227', 0o61032, '', 'CADR', 'DPFRACIN', kind='data', line=2037)
S('ENDRUTIN', 'equals', 0o113230, line=2038)

# SCALE FACTORS FOR THOSE ROUTINES NEEDING THEM ARE AVAILABLE IN SFTEMP1.
# ALL SFIN ROUTINES USE MPAC MPAC+1. LEAVE RESULT IN A. END WITH TC DECRET.

#   SETLOC ENDDPDEC +1

#   COUNT 40/PIN

# DEGINSF APPLIES 1000/180 * 5.55555(10) = 5.43434(8)

W('40,2716', 0o07052, 'DEGINSF', 'TC', 'DMP', 'SF ROUTINE FOR DEC DEGREES', line=2051)
W('40,2717', 0o02761, '', 'ADRES', 'DEGCON1', 'MULT BY 5.5  5(10)X2EXP-3', kind='data', line=2052)
W('40,2720', 0o10155, '', 'CCS', 'MPAC +1', 'THIS ROUNDS OFF MPAC+1 BEFORE SHIFT', line=2053)
W('40,2721', 0o35005, '', 'CAF', 'BIT11', 'LEFT 3, AND CAUSES 360.00 TO OF/UF', line=2054)
W('40,2722', 0o02724, '', 'TC', '+2', 'WHEN SHIFTED LEFT AND ALARM.', line=2055)
W('40,2723', 0o45005, '', 'CS', 'BIT11', line=2056)
W('40,2724', 0o60155, '', 'AD', 'MPAC +1', line=2057)
W('40,2725', 0o03072, '', 'TC', '2ROUND +2', line=2058)
W('40,2726', 0o04420, '', 'TC', 'TPSL1', 'LEFT 1', line=2059)
W('40,2727', 0o04420, 'DEGINSF2', 'TC', 'TPSL1', 'LEFT 2', line=2060)
W('40,2730', 0o03101, '', 'TC', 'TESTOFUF', line=2061)
W('40,2731', 0o04420, '', 'TC', 'TPSL1', 'RETURNS IF NO OF/UF (LEFT3)', line=2062)
W('40,2732', 0o10154, '', 'CCS', 'MPAC', line=2063)
W('40,2733', 0o02737, '', 'TC', 'SIGNFIX', 'IF+, GO TO SIGNFIX', line=2064)
W('40,2734', 0o02737, '', 'TC', 'SIGNFIX', 'IF +0, GO TO SIGNFIX', line=2065)
W('40,2735', 0o40000, '', 'COM', '', 'IF - , USE -MAGNITUDE +1', line=2066)
W('40,2736', 0o54154, '', 'TS', 'MPAC', 'IF -0, USE +0', line=2067)
W('40,2737', 0o10162, 'SIGNFIX', 'CCS', 'MPAC+6', line=2068)
W('40,2740', 0o02755, '', 'TC', 'SGNTO1', 'IF OVERFLOW', line=2069)
W('40,2741', 0o02751, '', 'TC', 'ENDSCALE', 'NO OVERFLOW/UNDERFLOW', line=2070)
# Page 350
W('40,2742', 0o10154, '', 'CCS', 'MPAC', 'IF UF FORCE SIGN TO 0 EXCEPT -180', line=2072)
W('40,2743', 0o05747, '', 'TC', 'CCSHOLE', line=2073)
W('40,2744', 0o02753, '', 'TC', 'NEG180', line=2074)
W('40,2745', 0o02746, '', 'TC', '+1', line=2075)
W('40,2746', 0o56154, '', 'XCH', 'MPAC', line=2076)
W('40,2747', 0o74777, '', 'MASK', 'POSMAX', line=2077)
W('40,2750', 0o54154, '', 'TS', 'MPAC', line=2078)
W('40,2751', 0o04701, 'ENDSCALE', 'TC', 'POSTJUMP', line=2079)
W('40,2752', 0o63155, '', 'CADR', 'PUTCOM2', kind='data', line=2080)

W('40,2753', 0o44777, 'NEG180', 'CS', 'POSMAX', line=2082)
W('40,2754', 0o02750, '', 'TC', 'ENDSCALE -1', line=2083)

W('40,2755', 0o40154, 'SGNTO1', 'CS', 'MPAC', 'IF OF FORCE SIGN TO 1', line=2085)
W('40,2756', 0o74777, '', 'MASK', 'POSMAX', line=2086)
W('40,2757', 0o40000, '', 'CS', 'A', line=2087)
W('40,2760', 0o02750, '', 'TC', 'ENDSCALE -1', line=2088)

W('40,2761', 0o26161, 'DEGCON1', '2DEC', '5.555555555 B-3', kind='data', line=2090)
W('40,2762', 0o30707, kind='data', line=2090)

W('40,2763', 0o21616, 'DEGCON2', '2DEC', '2.222222222 B-2', kind='data', line=2092)
W('40,2764', 0o07071, kind='data', line=2092)

W('40,2765', 0o71527, 'NEG.2', 'OCT', '-06250', '= .197753906  I.E., THE BIAS SCALED', kind='data', line=2094)

W('40,2766', 0o07052, 'ARTHINSF', 'TC', 'DMP', 'SCALES MPAC, +1 BY SFTEMP1, SFTEMP2.', line=2096)
W('40,2767', 0o00123, '', 'ADRES', 'SFTEMP1', 'ASSUMES POINT BETWEEN HI AND LO PARTS', kind='data', line=2097)
W('40,2770', 0o56156, '', 'XCH', 'MPAC +2', 'OF SFCON.  SHIFTS RESULTS LEFT BY 14.', line=2098)
W('40,2771', 0o56155, '', 'XCH', 'MPAC +1', '(BY TAKING RESULTS FROM MPAC+1, MPAC+2)', line=2099)
W('40,2772', 0o56154, '', 'XCH', 'MPAC', line=2100)
W('40,2773', 0o00006, '', 'EXTEND', line=2101)
W('40,2774', 0o12776, '', 'BZF', 'BINROUND', line=2102)
W('40,2775', 0o04161, '', 'TC', 'ALMCYCLE', 'TOO LARGE A LOAD.  ALARM AND RECYCLE.', line=2103)
W('40,2776', 0o03070, 'BINROUND', 'TC', '2ROUND', line=2104)
W('40,2777', 0o03101, '', 'TC', 'TESTOFUF', line=2105)
W('40,3000', 0o02751, '', 'TC', 'ENDSCALE', 'RETURNS IF NO OF/UF', line=2106)

W('40,3001', 0o07052, 'ARTIN1SF', 'TC', 'DMP', 'SCALES MPAC, +1 BY SFTEMP1, SFTEMP2.', line=2108)
W('40,3002', 0o00123, '', 'ADRES', 'SFTEMP1', 'ROUNDS MPAC+1 INTO MPAC.', kind='data', line=2109)
W('40,3003', 0o02776, '', 'TC', 'BINROUND', line=2110)

W('40,3004', 0o10154, 'OPTDEGIN', 'CCS', 'MPAC', 'OPTICS SCALING ROUTINE', line=2112)
W('40,3005', 0o03011, '', 'TC', '+4', line=2113)
W('40,3006', 0o03011, '', 'TC', '+3', line=2114)
W('40,3007', 0o04161, '', 'TC', 'ALMCYCLE', 'REJECT -- INPUT.  ALARM AND RECYCLE.', line=2115)
W('40,3010', 0o04161, '', 'TC', 'ALMCYCLE', 'REJECT -- INPUT.  ALARM AND RECYCLE.', line=2116)
W('40,3011', 0o32765, 'OPDEGIN2', 'CAF', 'NEG.2', 'RANGE IS 90 DEG', line=2117)
W('40,3012', 0o26154, '', 'ADS', 'MPAC', 'SUBTRACT BIAS', line=2118)
# Page 351
W('40,3013', 0o07052, '', 'TC', 'DMP', 'MULT BY 100 / 45 B-2', line=2120)
W('40,3014', 0o02763, '', 'ADRES', 'DEGCON2', kind='data', line=2121)
W('40,3015', 0o35004, '', 'CAF', 'BIT12', 'ROUND AS IN DEGINSF', line=2122)
W('40,3016', 0o60155, '', 'AD', 'MPAC +1', line=2123)
W('40,3017', 0o03072, '', 'TC', '2ROUND +2', line=2124)
W('40,3020', 0o02727, '', 'TC', 'DEGINSF2', line=2125)

W('40,3021', 0o07052, 'DPINSF', 'TC', 'DMP', 'SCALES MPAC, MPAC +1 BY SFTEMP1,', line=2127)
W('40,3022', 0o00123, '', 'ADRES', 'SFTEMP1', 'SFTEMP.  STORES LOW PART OF RESULT', kind='data', line=2128)
W('40,3023', 0o56156, '', 'XCH', 'MPAC +2', 'IN (E SUBK) +1 OR E+1', line=2129)
W('40,3024', 0o60000, '', 'DOUBLE', line=2130)
W('40,3025', 0o54156, '', 'TS', 'MPAC +2', line=2131)
W('40,3026', 0o35021, '', 'CAF', 'ZERO', line=2132)
W('40,3027', 0o60155, '', 'AD', 'MPAC +1', line=2133)
W('40,3030', 0o03072, '', 'TC', '2ROUND +2', line=2134)
W('40,3031', 0o03101, '', 'TC', 'TESTOFUF', line=2135)
W('40,3032', 0o50140, 'DPFRACIN', 'INDEX', 'MIXBR', 'RETURNS IF NO OF/UF', line=2136)
W('40,3033', 0o03033, '', 'TC', '+0', line=2137)
W('40,3034', 0o03044, '', 'TC', 'DPINORM', line=2138)
W('40,3035', 0o30117, '', 'CA', 'DECOUNT', 'MIXED NOUN', line=2139)
W('40,3036', 0o60145, 'DPINCOM', 'AD', 'NOUNADD', '      MIXED           NORMAL', line=2140)
W('40,3037', 0o54002, '', 'TS', 'Q', '      E SUBK          E', line=2141)
W('40,3040', 0o56155, '', 'XCH', 'MPAC +1', line=2142)
W('40,3041', 0o50002, '', 'INDEX', 'Q', line=2143)
W('40,3042', 0o54001, '', 'TS', '1', 'PLACE LOW PART IN', line=2144)
W('40,3043', 0o02751, '', 'TC', 'ENDSCALE', '      (E SUBK) +1     MIXED', line=2145)

W('40,3044', 0o35021, 'DPINORM', 'CAF', 'ZERO', '      E +1            NORMAL', line=2147)
W('40,3045', 0o03036, '', 'TC', 'DPINCOM', line=2148)

W('40,3046', 0o07052, 'DPINSF2', 'TC', 'DMP', 'ASSUMES POINT BETWEEN BITS 7-8 OF HIGH', line=2150)
W('40,3047', 0o00123, '', 'ADRES', 'SFTEMP1', 'PART OF SF CONST.  DPINSF2 SHIFTS RESULTS', kind='data', line=2151)
W('40,3050', 0o36211, '', 'CAF', 'SIX', 'LEFT BY 7, ROUNDS MPAC+2 INTO MPAC+1', line=2152)
W('40,3051', 0o03060, '', 'TC', 'TPLEFTN', 'SHIFT LEFT 7.', line=2153)
W('40,3052', 0o03023, '', 'TC', 'DPINSF +2', line=2154)

W('40,3053', 0o07052, 'DPINSF4', 'TC', 'DMP', 'ASSUMES POINT BETWEEN BITS 11-12 OF HIGH', line=2156)
W('40,3054', 0o00123, '', 'ADRES', 'SFTEMP1', 'PART OF SF CONST.  DPINSF2 SHIFTS RESULTS', kind='data', line=2157)
W('40,3055', 0o35016, '', 'CAF', 'TWO', 'LEFT BY 3, ROUNDS MPAC+2 INTO MPAC+1.', line=2158)
W('40,3056', 0o03060, '', 'TC', 'TPLEFTN', 'SHIFT LEFT 3.', line=2159)
W('40,3057', 0o03023, '', 'TC', 'DPINSF +2', line=2160)

W('40,3060', 0o56002, 'TPLEFTN', 'XCH', 'Q', 'SHIFTS MPAC, +1, +2 LEFT N.  SETS OVFIND', line=2162)
W('40,3061', 0o54124, '', 'TS', 'SFTEMP2', 'TO +1 FOR OF, -1 FOR UF.', line=2163)
W('40,3062', 0o56002, '', 'XCH', 'Q', 'CALL WITH N-1 IN A.', line=2164)
W('40,3063', 0o54123, 'LEFTNCOM', 'TS', 'SFTEMP1', '      LOOP TIME .37 MSEC.', line=2165)
W('40,3064', 0o04420, '', 'TC', 'TPSL1', line=2166)
W('40,3065', 0o10123, '', 'CCS', 'SFTEMP1', line=2167)
# Page 352
W('40,3066', 0o03063, '', 'TC', 'LEFTNCOM', line=2169)
W('40,3067', 0o00124, '', 'TC', 'SFTEMP2', line=2170)

W('40,3070', 0o56155, '2ROUND', 'XCH', 'MPAC +1', line=2172)
W('40,3071', 0o60000, '', 'DOUBLE', line=2173)
W('40,3072', 0o54155, '', 'TS', 'MPAC +1', line=2174)
W('40,3073', 0o00002, '', 'TC', 'Q', 'IF MPAC+1 DOES NOT OF/UF', line=2175)
W('40,3074', 0o60154, '', 'AD', 'MPAC', line=2176)
W('40,3075', 0o54154, '', 'TS', 'MPAC', line=2177)
W('40,3076', 0o00002, '', 'TC', 'Q', 'IF MPAC DOES NOT OF/UF', line=2178)
W('40,3077', 0o54162, '', 'TS', 'MPAC+6', line=2179)
W('40,3100', 0o00002, '2RNDEND', 'TC', 'Q', line=2180)

W('40,3101', 0o10162, 'TESTOFUF', 'CCS', 'MPAC+6', 'RETURNS IF NO OF/UF', line=2182)
W('40,3102', 0o04161, '', 'TC', 'ALMCYCLE', 'OF    ALARM AND RECYCLE.', line=2183)
W('40,3103', 0o00002, '', 'TC', 'Q', line=2184)
W('40,3104', 0o04161, '', 'TC', 'ALMCYCLE', 'UF    ALARM AND RECYCLE.', line=2185)

#   SETLOC ENDSPMIN +1

#   COUNT 42/PIN

W('42,3365', 0o03506, 'HMSIN', 'TC', 'ALL3DEC', 'IF ALL 3 WORDS WERE NOT LOADED, ALARM.', line=2191)
W('42,3366', 0o07052, '', 'TC', 'DMP', 'XREG, XREGLP (=HOURS) WERE ALREADY PUT', line=2192)
W('42,3367', 0o03447, '', 'ADRES', 'WHOLECON', 'INTO MPAC, MPAC+1.', kind='data', line=2193)
W('42,3370', 0o03456, '', 'TC', 'RND/TST', 'ROUND OFF TO WHOLE HRS IN MPAC+1.', line=2194)
W('42,3371', 0o35021, '', 'CAF', 'ZERO', 'ALARM IF MPAC NON ZERO (G/ 16383).', line=2195)
W('42,3372', 0o54156, '', 'TS', 'MPAC +2', line=2196)
W('42,3373', 0o33451, '', 'CAF', 'HRCON', line=2197)
W('42,3374', 0o54154, '', 'TS', 'MPAC', line=2198)
W('42,3375', 0o33452, '', 'CAF', 'HRCON +1', line=2199)
W('42,3376', 0o56155, '', 'XCH', 'MPAC +1', line=2200)
W('42,3377', 0o07256, '', 'TC', 'SHORTMP', line=2201)
W('42,3400', 0o03467, '', 'TC', 'MPACTST', 'ALARM IF MPAC NON ZERO (G/ 745)', line=2202)
W('42,3401', 0o52156, '', 'DXCH', 'MPAC +1', 'STORE HOURS CONTRIBUTION', line=2203)
W('42,3402', 0o52124, '', 'DXCH', 'HITEMIN', line=2204)
W('42,3403', 0o31004, '', 'CA', 'YREG', 'PUT YREG, YREGLP INTO MPAC, +1.', line=2205)
W('42,3404', 0o23007, '', 'LXCH', 'YREGLP', line=2206)
W('42,3405', 0o52155, '', 'DXCH', 'MPAC', line=2207)
W('42,3406', 0o07052, '', 'TC', 'DMP', line=2208)
W('42,3407', 0o03447, '', 'ADRES', 'WHOLECON', kind='data', line=2209)
W('42,3410', 0o03456, '', 'TC', 'RND/TST', 'ROUND OFF TO WHOLE MIN IN MPAC+1', line=2210)
W('42,3411', 0o43454, '', 'CS', '59MIN', 'ALARM IF MPAC NON ZERO (G/16383)', line=2211)
W('42,3412', 0o03474, '', 'TC', 'SIZETST', 'ALARM IF MPAC+1 G/ 59MIN', line=2212)
W('42,3413', 0o56155, '', 'XCH', 'MPAC +1', line=2213)
W('42,3414', 0o00006, '', 'EXTEND', line=2214)
W('42,3415', 0o73453, '', 'MP', 'MINCON', 'LEAVES MINUTES CONTRIBUTION IN A,L', line=2215)
# Page 353
W('42,3416', 0o20124, '', 'DAS', 'HITEMIN', 'ADD IN MINUTES CONTRIBUTION', line=2217)
W('42,3417', 0o00006, '', 'EXTEND', '', 'IF THIS DAS OVERFLOWS, G/ 745 HR,39MIN', line=2218)
W('42,3420', 0o13422, '', 'BZF', '+2', line=2219)
W('42,3421', 0o04161, '', 'TC', 'ALMCYCLE', line=2220)
W('42,3422', 0o31005, '', 'CA', 'ZREG', 'PUT ZREG, ZREGLP INTO MPAC +1.', line=2221)
W('42,3423', 0o23010, '', 'LXCH', 'ZREGLP', line=2222)
W('42,3424', 0o52155, '', 'DXCH', 'MPAC', line=2223)
W('42,3425', 0o07052, '', 'TC', 'DMP', line=2224)
W('42,3426', 0o03447, '', 'ADRES', 'WHOLECON', kind='data', line=2225)
W('42,3427', 0o03456, '', 'TC', 'RND/TST', 'ROUND OFF TO WHOLE CENTI-SEC IN MPAC+1', line=2226)
W('42,3430', 0o43455, '', 'CS', '59.99SEC', 'ALARM IF MPAC NON ZERO (G/163.83 SEC)', line=2227)
W('42,3431', 0o03474, '', 'TC', 'SIZETST', 'ALARM IF MPAC+1 G/59.99 SEC', line=2228)
W('42,3432', 0o52124, '', 'DXCH', 'HITEMIN', 'ADD IN SECONDS CONTRIBUTION', line=2229)
W('42,3433', 0o20155, '', 'DAS', 'MPAC', 'IF THIS DAS OVERFLOWS,', line=2230)
W('42,3434', 0o00006, '', 'EXTEND', '', 'G/ 745 HR, 39 MIN, 14.59 SEC.', line=2231)
W('42,3435', 0o13437, '', 'BZF', '+2', line=2232)
W('42,3436', 0o04161, '', 'TC', 'ALMCYCLE', 'ALARM AND RECYCLE', line=2233)
W('42,3437', 0o35021, '', 'CAF', 'ZERO', line=2234)
W('42,3440', 0o54156, '', 'TS', 'MPAC +2', line=2235)
W('42,3441', 0o07226, '', 'TC', 'TPAGREE', line=2236)
W('42,3442', 0o52155, '', 'DXCH', 'MPAC', line=2237)
W('42,3443', 0o50145, '', 'INDEX', 'NOUNADD', line=2238)
W('42,3444', 0o52001, '', 'DXCH', '0', line=2239)
W('42,3445', 0o04701, '', 'TC', 'POSTJUMP', line=2240)
W('42,3446', 0o62775, '', 'CADR', 'LOADLV', kind='data', line=2241)

W('42,3447', 0o00006, 'WHOLECON', 'OCT', '00006', '(10EXP5/2EXP14)2EXP14', kind='data', line=2243)
W('42,3450', 0o03240, '', 'OCT', '03240', kind='data', line=2244)
W('42,3451', 0o00025, 'HRCON', 'OCT', '00025', '1 HOUR IN CENTI-SEC', kind='data', line=2245)
W('42,3452', 0o37100, '', 'OCT', '37100', kind='data', line=2246)
W('42,3453', 0o13560, 'MINCON', 'OCT', '13560', '1 MINUTE IN CENTI-SEC', kind='data', line=2247)
W('42,3454', 0o00073, '59MIN', 'OCT', '00073', '59 AS WHOLE', kind='data', line=2248)
W('42,3455', 0o13557, '59.99SEC', 'OCT', '13557', '5999 SENTI-SEC', kind='data', line=2249)

W('42,3456', 0o56156, 'RND/TST', 'XCH', 'MPAC +2', 'ROUNDS MPAC+2 INTO MPAC+1.', line=2251)
W('42,3457', 0o60000, '', 'DOUBLE', '', 'ALARMS IF MPAC NOT 0', line=2252)
W('42,3460', 0o54156, '', 'TS', 'MPAC +2', line=2253)
W('42,3461', 0o35021, '', 'CAF', 'ZERO', line=2254)
W('42,3462', 0o60155, '', 'AD', 'MPAC +1', line=2255)
W('42,3463', 0o54155, '', 'TS', 'MPAC +1', line=2256)
W('42,3464', 0o35021, '', 'CAF', 'ZERO', line=2257)
W('42,3465', 0o60154, '', 'AD', 'MPAC', "CAN'T OVFLOW", line=2258)
W('42,3466', 0o56154, '', 'XCH', 'MPAC', line=2259)
W('42,3467', 0o10154, 'MPACTST', 'CCS', 'MPAC', 'ALARM IF MPAC NON ZERO', line=2260)
W('42,3470', 0o04161, '', 'TC', 'ALMCYCLE', 'ALARM AND RECYCLE', line=2261)
W('42,3471', 0o00002, '', 'TC', 'Q', line=2262)
W('42,3472', 0o04161, '', 'TC', 'ALMCYCLE', 'ALARM AND RECYCLE', line=2263)
W('42,3473', 0o00002, '', 'TC', 'Q', line=2264)

# Page 354

W('42,3474', 0o54156, 'SIZETST', 'TS', 'MPAC +2', 'CALLED WITH - CON IN A', line=2268)
W('42,3475', 0o10155, '', 'CCS', 'MPAC +1', 'GET MAG OF MPAC+1', line=2269)
W('42,3476', 0o65017, '', 'AD', 'ONE', line=2270)
W('42,3477', 0o13501, '', 'TCF', '+2', line=2271)
W('42,3500', 0o65017, '', 'AD', 'ONE', line=2272)
W('42,3501', 0o60156, '', 'AD', 'MPAC +2', line=2273)
W('42,3502', 0o00006, '', 'EXTEND', '', 'MAG OF MPAC+1 - CON', line=2274)
W('42,3503', 0o63505, '', 'BZMF', '+2', line=2275)
W('42,3504', 0o04161, '', 'TC', 'ALMCYCLE', 'MAG OF MPAC+1 G/ CON.  ALARM AND RECYCLE.', line=2276)
W('42,3505', 0o00002, '', 'TC', 'Q', 'MAG OF MPAC+1 L/= CON', line=2277)

# ALL3DEC TESTS THAT ALL 3 WORDS ARE LOADED IN DEC (FOR HMSIN).
# ALARM IF NOT.  (TEST THAT BITS 3,4,5 OF DECBRNCH ARE ALL = 1).

W('42,3506', 0o43513, 'ALL3DEC', 'CS', 'OCT34BAR', 'GET BITS 3,4,5 IN A', line=2282)
W('42,3507', 0o71000, '', 'MASK', 'DECBRNCH', 'GET BITS 3,4,5 OF DECBRNCH IN A', line=2283)
W('42,3510', 0o63513, '', 'AD', 'OCT34BAR', 'BITS 3,4,5 OF DECBRNCH MUST ALL = 1', line=2284)
W('42,3511', 0o10000, '', 'CCS', 'A', line=2285)
W('42,3512', 0o03516, '', 'TC', 'FORCEV25', line=2286)
W('42,3513', 0o77743, 'OCT34BAR', 'OCT', '77743', kind='data', line=2287)
W('42,3514', 0o03516, '', 'TC', 'FORCEV25', line=2288)
W('42,3515', 0o00002, '', 'TC', 'Q', line=2289)

W('42,3516', 0o44113, 'FORCEV25', 'CS', 'OCT31', 'FORCE VERB 25 TO BE EXECUTED BY RECYCLE', line=2291)
W('42,3517', 0o55041, '', 'TS', 'VERBSAVE', 'IN CASE OPERATOR EXECUTED A LOWER LOAD', line=2292)
W('42,3520', 0o04161, '', 'TC', 'ALMCYCLE', 'VERB.  ALARM AND RECYCLE.', line=2293)
S('ENDHMSS', 'equals', 0o115521, line=2294)

# Page 355
# MONITOR ALLOWS OTHER KEYBOARD ACTIVITY.  IT IS ENDED BY VERB TERMINATE,
# VERB PROCEED WITHOUT DATA, VERB RESEQUENCE,
# ANOTHER MONITOR, OR ANY NVSUB CALL THAT PASSES THE DSPLOCK (PROVIDED
# THAT THE OPERATOR HAS SOMEHOW ALLOWED THE ENDING OF A MONITOR WHICH
# HE HAS INITIATED THROUGH THE KEYBOARD).
#
# MONITOR ACTION IS SUSPENDED, BUT NOT ENDED, BY ANY KEYBOARD ACTION.
# EXCEPT ERROR LIGHT RESET.  IT BEGINS AGAIN WHEN KEY RELEASE IS PERFORMED.
# MONITOR SAVES THE NOUN AND APPROPRIATE DISPLAY VERB IN MONSAVE.  IT SAVES
# NOUNCADR IN MONSAVE1, IF NOUN = MACHINE CADR TO BE SPECIFIED.  BIT 15 OF
# MONSAVE1 IS THE KILL MONITOR SIGNAL (KILLER BIT).  BIT 14 OF MONSAVE1
# INDICATES THE CURRENT MONITOR WAS EXTERNALLY INITIATED (EXTERNAL
# MONITOR BIT).  IT IS TURNED OFF BY RELDSP AND KILMONON.
#
# MONSAVE INDICATES IF MONITOR IS ON (+=ON, +0=OFF)
# IF MONSAVE IS +, MONITOR ENTERS NO REQUEST, BUT TURNS KILLER BIT OFF.
# IF MONSAVE IS +0, MONITOR ENTERS REQUEST AND TURNS KILLER BIT OFF.
#
# NVSUB (IF EXTERNAL MONITOR BIT IS OFF), VB=PROCEED WITHOUT DATA,
# VB=RESEQUENCE, AND VB=TERMINATE TURN KILL MONITOR BIT ON.
#
# IF KILLER BIT IS ON, MONREQ ENTERS NO FURTHER REQUESTS, ZEROS MONSAVE
# AND MONSAVE1 (TURNING OFF KILLER BIT AND EXTERNAL MONITOR BIT).
#
# MONITOR DOESN'T TEST FOR MATBS SINCE NVSUB CAN HANDLE INTERNAL MATBS NOW.

#   SETLOC ENDRUTIN

#   COUNT 41/PIN

W('41,3230', 0o43237, 'MONITOR', 'CS', 'BIT15/14', line=2327)
W('41,3231', 0o71017, '', 'MASK', 'NOUNCADR', line=2328)
W('41,3232', 0o54155, 'MONIT1', 'TS', 'MPAC +1', 'TEMP STORAGE', line=2329)
W('41,3233', 0o40136, '', 'CS', 'ENTEXIT', line=2330)
W('41,3234', 0o64233, '', 'AD', 'ENDINST', line=2331)
W('41,3235', 0o10000, '', 'CCS', 'A', line=2332)
W('41,3236', 0o03245, '', 'TC', 'MONIT2', line=2333)
W('41,3237', 0o60000, 'BIT15/14', 'OCT', '60000', kind='data', line=2334)
W('41,3240', 0o03245, '', 'TC', 'MONIT2', line=2335)
W('41,3241', 0o35002, '', 'CAF', 'BIT14', 'EXTERNALLY INITIATED MONITOR.', line=2336)
W('41,3242', 0o26155, '', 'ADS', 'MPAC +1', 'SET BIT 14 FOR MONSAVE1.', line=2337)
W('41,3243', 0o35021, '', 'CAF', 'ZERO', line=2338)
W('41,3244', 0o55022, '', 'TS', 'MONSAVE2', 'ZERO NVMONOPT OPTIONS', line=2339)
W('41,3245', 0o36043, 'MONIT2', 'CAF', 'LOW7', line=2340)
W('41,3246', 0o71001, '', 'MASK', 'VERBREG', line=2341)
W('41,3247', 0o04345, '', 'TC', 'LEFT5', line=2342)
W('41,3250', 0o54022, '', 'TS', 'CYL', line=2343)
W('41,3251', 0o40022, '', 'CS', 'CYL', line=2344)
W('41,3252', 0o56022, '', 'XCH', 'CYL', line=2345)
W('41,3253', 0o61002, '', 'AD', 'NOUNREG', line=2346)
W('41,3254', 0o54154, '', 'TS', 'MPAC', 'TEMP STORAGE', line=2347)
# Page 356
W('41,3255', 0o35021, '', 'CAF', 'ZERO', line=2349)
W('41,3256', 0o55012, '', 'TS', 'DSPLOCK', '+0 INTO DSPLOCK SO MONITOR CAN RUN.', line=2350)
W('41,3257', 0o11042, '', 'CCS', 'CADRSTOR', 'TURN OFF KR LITE IF CADRSTOR AND DSPLIST', line=2351)
W('41,3260', 0o03262, '', 'TC', '+2', 'ARE BOTH EMPTY.  (LITE COMES ON IF NEW', line=2352)
W('41,3261', 0o04516, '', 'TC', 'RELDSP1', 'MONITOR IS KEYED IN OVER OLD MONITOR.)', line=2353)
W('41,3262', 0o00004, '', 'INHINT', line=2354)
W('41,3263', 0o11020, '', 'CCS', 'MONSAVE', line=2355)
W('41,3264', 0o03271, '', 'TC', '+5', 'IF MONSAVE WAS +, NO REQUEST', line=2356)
W('41,3265', 0o35017, '', 'CAF', 'ONE', 'IF MONSAVE WAS 0, REQUEST MONREQ', line=2357)
W('41,3266', 0o05245, '', 'TC', 'WAITLIST', line=2358)
#   EBANK= DSPCOUNT
W('41,3267', 0o03275, '', '2CADR', 'MONREQ', kind='data', line=2360)
W('41,3270', 0o62101, kind='data', line=2360)

W('41,3271', 0o52155, '', 'DXCH', 'MPAC', 'PLACE MONITOR VERB AND NOUN INTO MONSAVE', line=2362)
W('41,3272', 0o53021, '', 'DXCH', 'MONSAVE', 'ZERO THE KILL MONITOR BIT', line=2363)
W('41,3273', 0o00003, '', 'RELINT', '', 'SET UP EXTERNAL MONITOR BIT', line=2364)
W('41,3274', 0o00136, '', 'TC', 'ENTRET', line=2365)

W('41,3275', 0o04414, 'MONREQ', 'TC', 'LODSAMPT', 'CALLED BY WAITLIST', line=2367)
W('41,3276', 0o11021, '', 'CCS', 'MONSAVE1', 'TIME IS SNATCHED N RUPT FOR NOUN 65', line=2368)
W('41,3277', 0o03303, '', 'TC', '+4', 'IF KILLER BIT = 0, ENTER REQUESTS', line=2369)
W('41,3300', 0o03303, '', 'TC', '+3', 'IF KILLER BIT = 0, ENTER REQUESTS', line=2370)
W('41,3301', 0o03314, '', 'TC', 'KILLMON', 'IF KILLER BIT = 1, NO REQUESTS.', line=2371)
W('41,3302', 0o03314, '', 'TC', 'KILLMON', 'IF KILLER BIT = 1, NO REQUESTS.', line=2372)
W('41,3303', 0o33320, '', 'CAF', 'MONDEL', line=2373)
W('41,3304', 0o05245, '', 'TC', 'WAITLIST', 'ENTER WAITLIST REQUEST FOR MONREQ', line=2374)
#   EBANK= DSPCOUNT
W('41,3305', 0o03275, '', '2CADR', 'MONREQ', kind='data', line=2376)
W('41,3306', 0o62101, kind='data', line=2376)

W('41,3307', 0o34371, '', 'CAF', 'CHRPRIO', line=2378)
W('41,3310', 0o05134, '', 'TC', 'NOVAC', 'ENTER EXEC REQUEST FOR MONDO', line=2379)
#   EBANK= DSPCOUNT
W('41,3311', 0o03321, '', '2CADR', 'MONDO', kind='data', line=2381)
W('41,3312', 0o62101, kind='data', line=2381)

W('41,3313', 0o05324, '', 'TC', 'TASKOVER', line=2383)

W('41,3314', 0o35021, 'KILLMON', 'CAF', 'ZERO', 'ZERO MONSAVE AND TURN KILLER BIT OFF', line=2385)
W('41,3315', 0o55020, '', 'TS', 'MONSAVE', line=2386)
W('41,3316', 0o55021, '', 'TS', 'MONSAVE1', 'TURN OFF KILL MONITOR BIT.', line=2387)
W('41,3317', 0o05324, '', 'TC', 'TASKOVER', 'TURN OFF EXTERNAL MONITOR BIT.', line=2388)
W('41,3320', 0o00144, 'MONDEL', 'OCT', '144', 'FOR 1 SEC MONITOR INTERVALS.', kind='data', line=2389)

W('41,3321', 0o11021, 'MONDO', 'CCS', 'MONSAVE1', 'CALLED BY EXEC', line=2391)
W('41,3322', 0o03326, '', 'TC', '+4', 'IF KILLER BIT = 0, CONTINUE', line=2392)
W('41,3323', 0o03326, '', 'TC', '+3', 'IF KILLER BIT = 0, CONTINUE', line=2393)
W('41,3324', 0o05217, '', 'TC', 'ENDOFJOB', 'IN CASE TERMINATE CAME SINCE LAST MONREQ', line=2394)
W('41,3325', 0o05217, '', 'TC', 'ENDOFJOB', 'IN CASE TERMINATE CAME SINCE LAST MONREQ', line=2395)
W('41,3326', 0o11012, '', 'CCS', 'DSPLOCK', line=2396)
# Page 357
W('41,3327', 0o03351, '', 'TC', 'MONBUSY', 'NVSUB IS BUSY', line=2398)
W('41,3330', 0o36043, '', 'CAF', 'LOW7', line=2399)
W('41,3331', 0o71020, '', 'MASK', 'MONSAVE', line=2400)
W('41,3332', 0o02317, '', 'TC', 'UPDATNN -1', 'PLACE NOUN INTO NOUNREG AND DISPLAY IT', line=2401)
W('41,3333', 0o34160, '', 'CAF', 'MID7', line=2402)
W('41,3334', 0o71020, '', 'MASK', 'MONSAVE', 'CHANGE MONITOR VERB TO DISPLAY VERB', line=2403)
W('41,3335', 0o63347, '', 'AD', 'MONREF', '-DEC10, STARTING IN BIT8', line=2404)
W('41,3336', 0o54023, '', 'TS', 'EDOP', 'RIGHT 7', line=2405)
W('41,3337', 0o30023, '', 'CA', 'EDOP', line=2406)
W('41,3340', 0o55001, '', 'TS', 'VERBREG', line=2407)
W('41,3341', 0o33350, '', 'CAF', 'MONBACK', 'SET RETURN TO PASTEVB AFTER DATA DISPLAY', line=2408)
W('41,3342', 0o54136, '', 'TS', 'ENTRET', line=2409)
W('41,3343', 0o43237, '', 'CS', 'BIT15/14', line=2410)
W('41,3344', 0o71021, '', 'MASK', 'MONSAVE1', 'PUT ECADR INTO MPAC +2.  INTMCTBS WILL', line=2411)
W('41,3345', 0o54156, '', 'TS', 'MPAC +2', 'DISPLAY IT AND SET NOUNCADR, NOUNADD,', line=2412)
W('41,3346', 0o02046, 'ENDMONDO', 'TC', 'TESTNN', 'EBANK.', line=2413)

#   BLOCK 2

#   SETLOC FFTAG8
#   BANK

#   COUNT 02/PIN

W('4140', 0o34160, 'PASTEVB', 'CAF', 'MID7', line=2422)
W('4141', 0o71022, '', 'MASK', 'MONSAVE2', 'NVMONOPT PASTE OPTION', line=2423)
W('4142', 0o00006, '', 'EXTEND', line=2424)
W('4143', 0o14145, '', 'BZF', '+2', line=2425)
W('4144', 0o04146, '', 'TC', 'PASTEOPT', 'PASTE PLEASE VERB FOR NVMONOPT', line=2426)
W('4145', 0o31020, '', 'CA', 'MONSAVE', 'PASTE MONITOR VERB -- PASTE OPTION IS 0', line=2427)
W('4146', 0o54023, 'PASTEOPT', 'TS', 'EDOP', 'RIGHT 7', line=2428)
W('4147', 0o30023, '', 'CA', 'EDOP', 'PLACE MONITOR VERB OR PLEASE VERB INTO', line=2429)
W('4150', 0o04662, '', 'TC', 'BANKCALL', '      VERBREG AND DISPLAY IT.', line=2430)
W('4151', 0o62337, '', 'CADR', 'UPDATVB -1', kind='data', line=2431)
W('4152', 0o35021, '', 'CAF', 'ZERO', 'ZERO REQRET SO THAT PASTED VERBS CAN', line=2432)
W('4153', 0o55013, '', 'TS', 'REQRET', '      BE EXECUTED BY OPERATOR.', line=2433)
W('4154', 0o31022, '', 'CA', 'MONSAVE2', line=2434)
W('4155', 0o04271, '', 'TC', 'BLANKSUB', 'PROCESS NVMONOPT BLANK OPTION IF ANY', line=2435)
W('4156', 0o04157, '', 'TC', '+1', line=2436)
W('4157', 0o05217, 'ENDPASTE', 'TC', 'ENDOFJOB', line=2437)

W('4160', 0o37600, 'MID7', 'OCT', '37600', kind='data', line=2439)

#   SETLOC ENDMONDO +1
#   COUNT 41/PIN

W('41,3347', 0o75377, 'MONREF', 'OCT', '75377', '-DEC10, STARTING IN BIT8', kind='data', line=2444)
W('41,3350', 0o04140, 'MONBACK', 'ADRES', 'PASTEVB', kind='data', line=2445)

# Page 358
W('41,3351', 0o04410, 'MONBUSY', 'TC', 'RELDSPON', 'TURN KEY RELEASE LIGHT', line=2448)
W('41,3352', 0o05217, '', 'TC', 'ENDOFJOB', line=2449)

# DSPFMEM IS USED TO DISPLAY (IN OCTAL) ANY FIXED REGISTER.
# IT IS USED WITH NOUN = MACHINE CADR TO BE SPECIFIED.  THE FCADR OF THE
# DESIRED LOCATION IS THEN PUNCHED IN.  IT HANDLES F/F (FCADR 4000-7777)
#
# FOR BANKS L/E 27, THIS IS ENOUGH.
#
# FOR BANKS G/E 30, THE THIRD COMPONENT OF NOUN 26 (PRIO, ADRES, BBCON)
# MUST BE PRELOADED WITH THE DESIRED SUPERBANK BITS (BITS 5,6,7).
# V23N26 SHOULD BE USED.
#
# SUMMARY
# FOR BANKS L/E 27,                             V27N01E(FCADR)E
# FOR BANKS G/E 30,     V23N26E(SUPERBITS)E     V27N01E(FCADR)E

W('41,3353', 0o34333, 'DSPFMEM', 'CAF', 'R1D1', 'IF F/F, DATACALL USES BANK 02 OR 03.', line=2465)
W('41,3354', 0o54777, '', 'TS', 'DSPCOUNT', line=2466)
W('41,3355', 0o31047, '', 'CA', 'DSPTEM1 +2', 'SUPERBANK BITS WERE PRELOADED INTO', line=2467)
W('41,3356', 0o54001, '', 'TS', 'L', '3RD COMPONENT OF NOUN 26.', line=2468)
W('41,3357', 0o31017, '', 'CA', 'NOUNCADR', 'ORIGINAL FCADR LOADED STILL IN NOUNCADR.', line=2469)
W('41,3360', 0o04715, '', 'TC', 'SUPDACAL', 'CALL WITH FCADR IN A, SUPERBITS IN L.', line=2470)
W('41,3361', 0o03363, '', 'TC', 'DSPOCTWO', line=2471)
W('41,3362', 0o05217, 'ENDSPF', 'TC', 'ENDOFJOB', line=2472)

# Page 359
# WORD DISPLAY ROUTINES
#   SETLOC TESTOFUF +4
#   COUNT 40/PIN

W('40,3105', 0o56002, 'DSPSIGN', 'XCH', 'Q', line=2479)
W('40,3106', 0o54144, '', 'TS', 'DSPWDRET', line=2480)
W('40,3107', 0o10154, '', 'CCS', 'MPAC', line=2481)
W('40,3110', 0o03120, '', 'TC', '+8D', line=2482)
W('40,3111', 0o03120, '', 'TC', '+7', line=2483)
W('40,3112', 0o65017, '', 'AD', 'ONE', line=2484)
W('40,3113', 0o54154, '', 'TS', 'MPAC', line=2485)
W('40,3114', 0o02334, '', 'TC', '-ON', line=2486)
W('40,3115', 0o40155, '', 'CS', 'MPAC +1', line=2487)
W('40,3116', 0o54155, '', 'TS', 'MPAC +1', line=2488)
W('40,3117', 0o00144, '', 'TC', 'DSPWDRET', line=2489)
W('40,3120', 0o02314, '', 'TC', '+ON', line=2490)
W('40,3121', 0o00144, '', 'TC', 'DSPWDRET', line=2491)

W('40,3122', 0o00006, 'DSPRND', 'EXTEND', '', 'ROUND BY 5 EXP-6', line=2493)
W('40,3123', 0o33166, '', 'DCA', 'DECROUND -1', line=2494)
W('40,3124', 0o20155, '', 'DAS', 'MPAC', line=2495)
W('40,3125', 0o00006, '', 'EXTEND', line=2496)
W('40,3126', 0o13132, '', 'BZF', '+4', line=2497)
W('40,3127', 0o00006, '', 'EXTEND', line=2498)
W('40,3130', 0o34777, '', 'DCA', 'DPOSMAX', line=2499)
W('40,3131', 0o52155, '', 'DXCH', 'MPAC', line=2500)
W('40,3132', 0o00002, '', 'TC', 'Q', line=2501)

# DSPDECWD CONVERTS C(MPAC,MPAC+1) INTO A SIGN AND 5 CHAR DECIMAL
# STARTING IN LOC SPECIFIED IN DSPCOUNT.  IT ROUNDS BY 5 EXP-6.

W('40,3133', 0o56002, 'DSPDECWD', 'XCH', 'Q', line=2506)
W('40,3134', 0o54115, '', 'TS', 'WDRET', line=2507)
W('40,3135', 0o03105, '', 'TC', 'DSPSIGN', line=2508)
W('40,3136', 0o03122, '', 'TC', 'DSPRND', line=2509)
W('40,3137', 0o35015, '', 'CAF', 'FOUR', line=2510)
W('40,3140', 0o54137, 'DSPDCWD1', 'TS', 'WDCNT', line=2511)
W('40,3141', 0o34377, '', 'CAF', 'BINCON', line=2512)
W('40,3142', 0o07256, '', 'TC', 'SHORTMP', line=2513)
W('40,3143', 0o50154, 'TRACE1', 'INDEX', 'MPAC', line=2514)
W('40,3144', 0o34072, '', 'CAF', 'RELTAB', line=2515)
W('40,3145', 0o74362, '', 'MASK', 'LOW5', line=2516)
W('40,3146', 0o54124, '', 'TS', 'CODE', line=2517)
W('40,3147', 0o35021, '', 'CAF', 'ZERO', line=2518)
W('40,3150', 0o56156, '', 'XCH', 'MPAC +2', line=2519)
W('40,3151', 0o56155, '', 'XCH', 'MPAC +1', line=2520)
W('40,3152', 0o54154, '', 'TS', 'MPAC', line=2521)
W('40,3153', 0o56777, '', 'XCH', 'DSPCOUNT', line=2522)
W('40,3154', 0o54143, 'TRACE1S', 'TS', 'COUNT', line=2523)
# Page 360
W('40,3155', 0o10000, '', 'CCS', 'A', 'DECREMENT DSPCOUNT EXCEPT AT +0', line=2525)
W('40,3156', 0o54777, '', 'TS', 'DSPCOUNT', line=2526)
W('40,3157', 0o03227, '', 'TC', 'DSPIN', line=2527)
W('40,3160', 0o10137, '', 'CCS', 'WDCNT', line=2528)
W('40,3161', 0o03140, '', 'TC', 'DSPDCWD1', line=2529)
W('40,3162', 0o44374, '', 'CS', 'VD1', line=2530)
W('40,3163', 0o54777, '', 'TS', 'DSPCOUNT', line=2531)
W('40,3164', 0o00115, '', 'TC', 'WDRET', line=2532)

W('40,3165', 0o00000, '', 'OCT', '00000', kind='data', line=2534)
W('40,3166', 0o02476, 'DECROUND', 'OCT', '02476', kind='data', line=2535)

# DSPDECNR CONVERTS C(MPAC,MPAC+1) INTO A SIGN AND 5 CHAR DECIMAL
# STARTING IN LOC SPECIFIED IN DSPCOUNT.  IT DOES NOT ROUND

W('40,3167', 0o56002, 'DSPDECNR', 'XCH', 'Q', line=2540)
W('40,3170', 0o54115, '', 'TS', 'WDRET', line=2541)
W('40,3171', 0o03105, '', 'TC', 'DSPSIGN', line=2542)
W('40,3172', 0o03137, '', 'TC', 'DSPDCWD1 -1', line=2543)

# DSPDC2NR CONVERTS C(MPAC,MPAC+1) INTO A SIGN AND 2 CHAR DECIMAL
# STARTING IN LOC SPECIFIED IN DSPCOUNT.  IT DOES NOT ROUND

W('40,3173', 0o56002, 'DSPDC2NR', 'XCH', 'Q', line=2548)
W('40,3174', 0o54115, '', 'TS', 'WDRET', line=2549)
W('40,3175', 0o03105, '', 'TC', 'DSPSIGN', line=2550)
W('40,3176', 0o35017, '', 'CAF', 'ONE', line=2551)
W('40,3177', 0o03140, '', 'TC', 'DSPDCWD1', line=2552)

# DSP2DEC CONVERTS C(MPAC) AND C(MPAC+1) INTO A SIGN AND 10 CHAR DECIMAL
# STARTING IN THE LOC SPECIFIED IN DSPCOUNT.

W('40,3200', 0o56002, 'DSP2DEC', 'XCH', 'Q', line=2557)
W('40,3201', 0o54115, '', 'TS', 'WDRET', line=2558)
W('40,3202', 0o35021, '', 'CAF', 'ZERO', line=2559)
W('40,3203', 0o54124, '', 'TS', 'CODE', line=2560)
W('40,3204', 0o36214, '', 'CAF', 'THREE', line=2561)
W('40,3205', 0o03311, '', 'TC', '11DSPIN', '-R2 OFF', line=2562)
W('40,3206', 0o35015, '', 'CAF', 'FOUR', line=2563)
W('40,3207', 0o03311, '', 'TC', '11DSPIN', '+R2 OFF', line=2564)
W('40,3210', 0o03105, '', 'TC', 'DSPSIGN', line=2565)
W('40,3211', 0o34334, '', 'CAF', 'R2D1', line=2566)
W('40,3212', 0o03140, 'END2DEC', 'TC', 'DSPDCWD1', line=2567)

# DSPDECVN DISPLAYS C(A) UPON ENTRY AS A 2 CHAR DECIMAL BEGINNING IN THE
# DSP LOC SPECIFIED IN DSPCOUNT.
#
# C(A) SHOULD BE IN FORM N X 2EXP-14.  THIS IS SCALED TO FORM N/100 BEFORE
# DISPLAY CONVERSION.
# Page 361

W('40,3213', 0o00006, 'DSPDECVN', 'EXTEND', line=2576)
W('40,3214', 0o73223, '', 'MP', 'VNDSPCON', 'MULT BY .01', line=2577)
W('40,3215', 0o22154, '', 'LXCH', 'MPAC', 'TAKE RESULTS FROM L. (MULT BY 2EXP14).', line=2578)
W('40,3216', 0o35021, '', 'CAF', 'ZERO', line=2579)
W('40,3217', 0o54155, '', 'TS', 'MPAC +1', line=2580)
W('40,3220', 0o56002, '', 'XCH', 'Q', line=2581)
W('40,3221', 0o54115, '', 'TS', 'WDRET', line=2582)
W('40,3222', 0o03176, '', 'TC', 'DSPDC2NR +3', 'NO SIGN, NO ROUND, 2 CHAR', line=2583)

W('40,3223', 0o00244, 'VNDSPCON', 'OCT', '00244', '.01 ROUNDED UP', kind='data', line=2585)

W('40,3224', 0o03213, 'GOVNUPDT', 'TC', 'DSPDECVN', 'THIS IS NOT FOR GENERAL USE.  REALLY PART', line=2587)
W('40,3225', 0o04701, '', 'TC', 'POSTJUMP', 'OF UPDATVB.', line=2588)
W('40,3226', 0o62347, '', 'CADR', 'UPDAT1 +2', kind='data', line=2589)

S('ENDECVN', 'equals', 0o111227, line=2591)

#   SETLOC ENDSPF +1
#   COUNT 41/PIN

# DSPOCTWD DISPLAYS C(A) UPON ENTRY AS A 5 CHAR OCT STARTING IN THE DSP
# CHAR SPECIFIED IN DSPCOUNT.  IT STOPS AFTER 5 CHAR HAVE BEEN DISPLAYED.

W('41,3363', 0o54022, 'DSPOCTWO', 'TS', 'CYL', line=2599)
W('41,3364', 0o56002, '', 'XCH', 'Q', line=2600)
W('41,3365', 0o54115, '', 'TS', 'WDRET', 'MUST USE SAME RETURN AS DSP2BIT.', line=2601)
W('41,3366', 0o35002, '', 'CAF', 'BIT14', 'TO BLANK SIGNS', line=2602)
W('41,3367', 0o26777, '', 'ADS', 'DSPCOUNT', line=2603)
W('41,3370', 0o35015, '', 'CAF', 'FOUR', line=2604)
W('41,3371', 0o54137, 'WDAGAIN', 'TS', 'WDCNT', line=2605)
W('41,3372', 0o40022, '', 'CS', 'CYL', line=2606)
W('41,3373', 0o40022, '', 'CS', 'CYL', line=2607)
W('41,3374', 0o40022, '', 'CS', 'CYL', line=2608)
W('41,3375', 0o40000, '', 'CS', 'A', line=2609)
W('41,3376', 0o75023, '', 'MASK', 'DSPMSK', line=2610)
W('41,3377', 0o50000, '', 'INDEX', 'A', line=2611)
W('41,3400', 0o34072, '', 'CAF', 'RELTAB', line=2612)
W('41,3401', 0o74362, '', 'MASK', 'LOW5', line=2613)
W('41,3402', 0o54124, '', 'TS', 'CODE', line=2614)
W('41,3403', 0o56777, '', 'XCH', 'DSPCOUNT', line=2615)
W('41,3404', 0o54143, '', 'TS', 'COUNT', line=2616)
W('41,3405', 0o10000, '', 'CCS', 'A', 'DECREMENT DSPCOUNT EXCEPT AT +0', line=2617)
W('41,3406', 0o54777, '', 'TS', 'DSPCOUNT', line=2618)
W('41,3407', 0o04701, '', 'TC', 'POSTJUMP', line=2619)
W('41,3410', 0o61317, '', 'CADR', 'DSPOCTIN', kind='data', line=2620)
W('41,3411', 0o10137, 'OCTBACK', 'CCS', 'WDCNT', line=2621)
W('41,3412', 0o03371, '', 'TC', 'WDAGAIN', '+', line=2622)
W('41,3413', 0o44374, 'DSPLV', 'CS', 'VD1', 'TO BLOCK NUMERICAL CHARACTERS, CLEARS,', line=2623)
# Page 362
W('41,3414', 0o54777, '', 'TS', 'DSPCOUNT', 'AND SIGNS AFTER A COMPLETED DISPLAY.', line=2625)
W('41,3415', 0o00115, '', 'TC', 'WDRET', line=2626)

S('DSPMSK', 'equals', 0o5023, line=2628)

# DSP2BIT DISPLAYS C(A) UPON ENTRY AS A 2 CHAR OCT BEGINNING IN THE DSP
# LOC SPECIFIED IN DSPCOUNT BY PRE CYCLING RIGHT C(A) AND USING THE LOGIC
# OF THE 5 CHAR OCTAL DISPLAY

W('41,3416', 0o54020, 'DSP2BIT', 'TS', 'CYR', line=2634)
W('41,3417', 0o56002, '', 'XCH', 'Q', line=2635)
W('41,3420', 0o54115, '', 'TS', 'WDRET', line=2636)
W('41,3421', 0o35017, '', 'CAF', 'ONE', line=2637)
W('41,3422', 0o54137, '', 'TS', 'WDCNT', line=2638)
W('41,3423', 0o40020, '', 'CS', 'CYR', line=2639)
W('41,3424', 0o40020, '', 'CS', 'CYR', line=2640)
W('41,3425', 0o56020, '', 'XCH', 'CYR', line=2641)
W('41,3426', 0o54022, '', 'TS', 'CYL', line=2642)
W('41,3427', 0o03376, '', 'TC', 'WDAGAIN +5', line=2643)

# FOR DSPIN PLACE 0/25 OCT INTO COUNT, 5 BIT RELAY CODE INTO CODE.  BOTH
# ARE DESTROYED.  IF BIT14 OF COUNT IS 1, SIGN IS BLANKED WITH LEFT CHAR.
# FOR DSPIN1 PLACE 0,1 INTO BIT11 OF CODE, 2 INTO COUNT, REL ADDRESS OF
# DSPTAB ENTRY INTO DSREL.

#   SETLOC ENDECVN

#   COUNT 40/PIN

W('40,3227', 0o56002, 'DSPIN', 'XCH', 'Q', "CAN'T USE L FOR RETURN, SINCE MANY OF THE", line=2654)
W('40,3230', 0o54114, '', 'TS', 'DSEXIT', 'ROUTINES CALLING DSPIN USE L AS RETURN.', line=2655)
W('40,3231', 0o34362, '', 'CAF', 'LOW5', line=2656)
W('40,3232', 0o70143, '', 'MASK', 'COUNT', line=2657)
W('40,3233', 0o54021, '', 'TS', 'SR', line=2658)
W('40,3234', 0o56021, '', 'XCH', 'SR', line=2659)
W('40,3235', 0o54141, '', 'TS', 'DSREL', line=2660)
W('40,3236', 0o35017, '', 'CAF', 'BIT1', line=2661)
W('40,3237', 0o70143, '', 'MASK', 'COUNT', line=2662)
W('40,3240', 0o10000, '', 'CCS', 'A', line=2663)
W('40,3241', 0o03243, '', 'TC', '+2', 'LEFT IF COUNT IS ODD', line=2664)
W('40,3242', 0o03253, '', 'TC', 'DSPIN1 -1', 'RIGHT IF COUNT IS EVEN', line=2665)
W('40,3243', 0o56124, '', 'XCH', 'CODE', line=2666)
W('40,3244', 0o04354, '', 'TC', 'SLEFT5', 'DOES NOT USE CYL', line=2667)
W('40,3245', 0o54124, '', 'TS', 'CODE', line=2668)
W('40,3246', 0o35002, '', 'CAF', 'BIT14', line=2669)
W('40,3247', 0o70143, '', 'MASK', 'COUNT', line=2670)
W('40,3250', 0o10000, '', 'CCS', 'A', line=2671)
W('40,3251', 0o35016, '', 'CAF', 'TWO', 'BIT14 = 1, BLANK SIGN', line=2672)
# Page 363
W('40,3252', 0o65017, '', 'AD', 'ONE', 'BIT14 = 0, LEAVE SIGN ALONE', line=2674)
W('40,3253', 0o54143, '', 'TS', 'COUNT', '+0 INTO COUNT FOR RIGHT', line=2675)
# +1 INTO COUNT FOR LEFT (SIGN LEFT ALONE)
# +3 INTO COUNT FOR LEFT (TO BLANK SIGN)
W('40,3254', 0o00004, 'DSPIN1', 'INHINT', line=2678)
W('40,3255', 0o50141, '', 'INDEX', 'DSREL', line=2679)
W('40,3256', 0o11023, '', 'CCS', 'DSPTAB', line=2680)
W('40,3257', 0o03261, '', 'TC', '+2', 'IF +', line=2681)
W('40,3260', 0o05747, '', 'TC', 'CCSHOLE', line=2682)
W('40,3261', 0o65017, '', 'AD', 'ONE', 'IF -', line=2683)
W('40,3262', 0o54142, '', 'TS', 'DSMAG', line=2684)
W('40,3263', 0o50143, '', 'INDEX', 'COUNT', line=2685)
W('40,3264', 0o73305, '', 'MASK', 'DSMSK', line=2686)
W('40,3265', 0o00006, '', 'EXTEND', line=2687)
W('40,3266', 0o60124, '', 'SU', 'CODE', line=2688)
W('40,3267', 0o00006, '', 'EXTEND', line=2689)
W('40,3270', 0o13303, '', 'BZF', 'DSLV', 'SAME', line=2690)
W('40,3271', 0o50143, 'DFRNT', 'INDEX', 'COUNT', line=2691)
W('40,3272', 0o43305, '', 'CS', 'DSMSK', 'MASK WITH 77740, 76037, 76777, OR 74037', line=2692)
W('40,3273', 0o70142, '', 'MASK', 'DSMAG', line=2693)
W('40,3274', 0o60124, '', 'AD', 'CODE', line=2694)
W('40,3275', 0o40000, '', 'CS', 'A', line=2695)
W('40,3276', 0o50141, '', 'INDEX', 'DSREL', line=2696)
W('40,3277', 0o57023, '', 'XCH', 'DSPTAB', line=2697)
W('40,3300', 0o00006, '', 'EXTEND', line=2698)
W('40,3301', 0o63303, '', 'BZMF', 'DSLV', 'DSPTAB ENTRY WAS -', line=2699)
W('40,3302', 0o25016, '', 'INCR', 'NOUT', 'DSPTAB ENTRY WAS +', line=2700)
W('40,3303', 0o00003, 'DSLV', 'RELINT', line=2701)
W('40,3304', 0o00114, '', 'TC', 'DSEXIT', line=2702)

W('40,3305', 0o00037, 'DSMSK', 'OCT', '37', kind='data', line=2704)
W('40,3306', 0o01740, '', 'OCT', '1740', kind='data', line=2705)
W('40,3307', 0o02000, '', 'OCT', '2000', kind='data', line=2706)
W('40,3310', 0o03740, '', 'OCT', '3740', kind='data', line=2707)

# FOR 11DSPIN, PUT REL ADDRESS OF DSPTAB ENTRY INTO A, 1 IN BIT11 OR 0 IN
# BIT11 OF CODE.

W('40,3311', 0o54141, '11DSPIN', 'TS', 'DSREL', line=2712)
W('40,3312', 0o35016, '', 'CAF', 'TWO', line=2713)
W('40,3313', 0o54143, '', 'TS', 'COUNT', line=2714)
W('40,3314', 0o56002, '', 'XCH', 'Q', 'MUST USE SAME RETURN AS DSPIN', line=2715)
W('40,3315', 0o54114, '', 'TS', 'DSEXIT', line=2716)
W('40,3316', 0o03254, '', 'TC', 'DSPIN1', line=2717)

W('40,3317', 0o03227, 'DSPOCTIN', 'TC', 'DSPIN', "SO DSPOCTWD DOESN'T USE SWCALL", line=2719)
W('40,3320', 0o33322, '', 'CAF', '+2', line=2720)
W('40,3321', 0o04704, '', 'TC', 'BANKJUMP', line=2721)
# Page 364
W('40,3322', 0o63411, 'ENDSPOCT', 'CADR', 'OCTBACK', kind='data', line=2723)

# DSPALARM FINDS TC NVSUBEND IN ENTRET FOR NVSUB INITIATED ROUTINES
# ABORT WITH 01501.
#
# DSPALARM FINDS TC ENDOFJOB IN ENTRET FOR KEYBOARD INITIATED ROUTINES.
# DC TC ENTRET.

W('40,3323', 0o44374, 'PREDSPAL', 'CS', 'VD1', line=2731)
W('40,3324', 0o54777, '', 'TS', 'DSPCOUNT', line=2732)
W('40,3325', 0o43346, 'DSPALARM', 'CS', 'NVSBENDL', line=2733)
W('40,3326', 0o60136, '', 'AD', 'ENTEXIT', line=2734)
W('40,3327', 0o00006, '', 'EXTEND', line=2735)
W('40,3330', 0o13343, '', 'BZF', 'CHARALRM +2', line=2736)
W('40,3331', 0o43345, '', 'CS', 'MONADR', 'IF THIS IS A MONITOR, KILL IT', line=2737)
W('40,3332', 0o60136, '', 'AD', 'ENTEXIT', line=2738)
W('40,3333', 0o00006, '', 'EXTEND', line=2739)
W('40,3334', 0o13336, '', 'BZF', '+2', line=2740)
W('40,3335', 0o03341, '', 'TC', 'CHARALRM', line=2741)
W('40,3336', 0o04220, '', 'TC', 'KILMONON', line=2742)
W('40,3337', 0o04400, '', 'TC', 'FALTON', line=2743)
W('40,3340', 0o04140, '', 'TC', 'PASTEVB', 'PUT MONITOR VERB BACK IN VERBREG', line=2744)
W('40,3341', 0o04400, 'CHARALRM', 'TC', 'FALTON', 'NOT NVSUB INITATED TURN ON OPR ERROR', line=2745)
W('40,3342', 0o05217, '', 'TC', 'ENDOFJOB', line=2746)
W('40,3343', 0o05721, '', 'TC', 'POODOO', line=2747)
W('40,3344', 0o01501, '', 'OCT', '01501', kind='data', line=2748)
W('40,3345', 0o04140, 'MONADR', 'GENADR', 'PASTEVB', kind='data', line=2749)
W('40,3346', 0o04216, 'NVSBENDL', 'TC', 'NVSUBEND', line=2750)

# ALMCYCLE TURNS ON CHECK FAIL LIGHT, REDISPLAYS THE ORIGINAL VERB THAT
# WAS EXECUTED, AND RECYCLES TO EXECUTE THE ORIGINAL VERB/NOUN COMBINATION
# THAT WAS LAST EXECUTED.  USED FOR BAD DATA DURING LOAD VERBS AND BY
# MCTBS.  ALSO BY MMCHANG IF 2 NUMERICAL CHARACTERS WERE NOT PUNCHED IN
# FOR MM CODE

#   SETLOC MID7 +1
#   COUNT 02/PIN

W('4161', 0o04400, 'ALMCYCLE', 'TC', 'FALTON', 'TURN ON CHECK FAIL LIGHT.', line=2761)
W('4162', 0o41041, '', 'CS', 'VERBSAVE', 'GET ORIGINAL VERB THAT WAS EXECUTED', line=2762)
W('4163', 0o55013, '', 'TS', 'REQRET', 'SET FOR ENTPAS0', line=2763)
W('4164', 0o04662, '', 'TC', 'BANKCALL', 'PUTS ORIGINAL VERB INTO VERBREG AND', line=2764)
W('4165', 0o62337, '', 'CADR', 'UPDATVB -1', 'DISPLAYS IT IN VERB LIGHTS.', kind='data', line=2765)
W('4166', 0o04701, '', 'TC', 'POSTJUMP', line=2766)
W('4167', 0o62002, 'ENDALM', 'CADR', 'ENTER', kind='data', line=2767)

# MMCHANG USES NOUN DISPLAY UNTIL ENTER.  THEN IT USES MODE DISP.
# IT GOES TO MODROUT WITH THE NEW M M CODE IN A, BUT NOT DISPLAYED IN
# Page 365
# MM LIGHTS.
#
# IT DEMANDS 2 NUMERICAL CHARACTERS BE PUNCHED IN FOR NEW MM CODE.
# IF NOT, IT RECYCLES.

#   SETLOC DSP2BIT +10D

#   COUNT 41/PIN

W('41,3430', 0o03452, 'MMCHANG', 'TC', 'REQMM', 'ENTPASHI ASSUMES THE TC REQMM AT MMCHANG', line=2781)
# IF THIS MOVES AT ALL, MUST CHANGE
# MMADREF AT ENTPASHI.
W('41,3431', 0o35013, '', 'CAF', 'BIT5', 'OCT20 = ND2.', line=2784)
W('41,3432', 0o60777, '', 'AD', 'DSPCOUNT', 'DSPCOUNT MUST = -ND2.', line=2785)
W('41,3433', 0o00006, '', 'EXTEND', '', 'DEMAND THAT 2 NUM CHAR WERE PUNCHED IN.', line=2786)
W('41,3434', 0o13436, '', 'BZF', '+2', line=2787)
W('41,3435', 0o04161, '', 'TC', 'ALMCYCLE', 'DSPCOUNT NOT= -ND2.  ALARM AND RECYCLE.', line=2788)
W('41,3436', 0o35021, '', 'CAF', 'ZERO', 'DSPCOUNT = -ND2.', line=2789)
W('41,3437', 0o57002, '', 'XCH', 'NOUNREG', line=2790)
W('41,3440', 0o54154, '', 'TS', 'MPAC', line=2791)
W('41,3441', 0o34375, '', 'CAF', 'ND1', line=2792)
W('41,3442', 0o54777, '', 'TS', 'DSPCOUNT', line=2793)
W('41,3443', 0o04662, '', 'TC', 'BANKCALL', line=2794)
W('41,3444', 0o60502, '', 'CADR', '2BLANK', kind='data', line=2795)
W('41,3445', 0o44374, '', 'CS', 'VD1', 'BLOCK NUM CHAR IN', line=2796)
W('41,3446', 0o54777, '', 'TS', 'DSPCOUNT', line=2797)
W('41,3447', 0o30154, '', 'CA', 'MPAC', line=2798)
W('41,3450', 0o04701, '', 'TC', 'POSTJUMP', line=2799)
W('41,3451', 0o10011, '', 'CADR', 'MODROUTB', 'GO THRU STANDARD LOC.', kind='data', line=2800)

S('MODROUTB', 'equals', 0o20011, line=2802)
W('41,3452', 0o40002, 'REQMM', 'CS', 'Q', line=2803)
W('41,3453', 0o55013, '', 'TS', 'REQRET', line=2804)
W('41,3454', 0o34375, '', 'CAF', 'ND1', line=2805)
W('41,3455', 0o54777, '', 'TS', 'DSPCOUNT', line=2806)
W('41,3456', 0o35021, '', 'CAF', 'ZERO', line=2807)
W('41,3457', 0o55002, '', 'TS', 'NOUNREG', line=2808)
W('41,3460', 0o04662, '', 'TC', 'BANKCALL', line=2809)
W('41,3461', 0o60502, '', 'CADR', '2BLANK', kind='data', line=2810)
W('41,3462', 0o04443, '', 'TC', 'FLASHON', line=2811)
W('41,3463', 0o35017, '', 'CAF', 'ONE', line=2812)
W('41,3464', 0o55000, '', 'TS', 'DECBRNCH', 'SET FOR DEC', line=2813)
W('41,3465', 0o00136, '', 'TC', 'ENTEXIT', line=2814)

# VBRQEXEC ENTERS REQUEST TO EXEC FOR ANY ADDRESS WITH ANY PRIORITY.
# IT DOES ENDOFJOB AFTER ENTERING REQUEST.  DISPLAY SYST IS RELEASED.
# IT ASSUMES NOUN 26 HAS BEEN PRELOADED WITH
# COMPONENT 1     PRIORITY (BITS 10-14) BIT1=0 FOR NOVAC, BIT1=1 FOR FINDVAC.
# COMPONENT 2     JOB ADRES (12 BIT)
# Page 366
# COMPONENT 3     BBCON

W('41,3466', 0o35017, 'VBRQEXEC', 'CAF', 'BIT1', line=2824)
W('41,3467', 0o71045, '', 'MASK', 'DSPTEM1', line=2825)
W('41,3470', 0o10000, '', 'CCS', 'A', line=2826)
W('41,3471', 0o03510, '', 'TC', 'SETVAC', 'IF BIT1 = 1, FINDVAC', line=2827)
W('41,3472', 0o34365, '', 'CAF', 'TCNOVAC', 'IF BIT1 = 0, NOVAC', line=2828)
W('41,3473', 0o54154, 'REQEX1', 'TS', 'MPAC', 'TC NOVAC OR TC FINDVAC INTO MPAC', line=2829)
W('41,3474', 0o45017, '', 'CS', 'BIT1', line=2830)
W('41,3475', 0o71045, '', 'MASK', 'DSPTEM1', line=2831)
W('41,3476', 0o54160, '', 'TS', 'MPAC +4', 'PRIO INTO MPAC+4 AS A TEMP', line=2832)
W('41,3477', 0o04473, 'REQUESTC', 'TC', 'RELDSP', line=2833)
W('41,3500', 0o34233, '', 'CA', 'ENDINST', line=2834)
W('41,3501', 0o54157, '', 'TS', 'MPAC +3', 'TC ENDOFJOB INTO MPAC+3', line=2835)
W('41,3502', 0o00006, '', 'EXTEND', line=2836)
W('41,3503', 0o31047, '', 'DCA', 'DSPTEM1 +1', 'JOB ADRES INTO MPAC+1', line=2837)
W('41,3504', 0o52156, '', 'DXCH', 'MPAC +1', 'BBCON INTO MPAC+2', line=2838)
W('41,3505', 0o30160, '', 'CA', 'MPAC +4', 'PRIO IN A', line=2839)
W('41,3506', 0o00004, '', 'INHINT', line=2840)
W('41,3507', 0o00154, '', 'TC', 'MPAC', line=2841)

W('41,3510', 0o34370, 'SETVAC', 'CAF', 'TCFINDVC', line=2843)
W('41,3511', 0o03473, '', 'TC', 'REQEX1', line=2844)

# VBRQWAIT ENTERS REQUEST TO WAITLIST FOR ANY ADDRESS WITH ANY DELAY.
# IT DOES ENDOFJOB AFTER ENTERING REQUEST.  DISPLAY SYST IS RELEASED.
# IT ASSUMES NOUN 26 HAS BEEN PRELOADED WITH
# COMPONENT 1     DELAY (LOW BITS)
# COMPONENT 2     TASK ADRES (12 BIT)
# COMPONENT 3     BBCON

W('41,3512', 0o34366, 'VBRQWAIT', 'CAF', 'TCWAIT', line=2853)
W('41,3513', 0o54154, '', 'TS', 'MPAC', 'TC WAITLIST INTO MPAC', line=2854)
W('41,3514', 0o31045, '', 'CA', 'DSPTEM1', 'TIME DELAY', line=2855)
W('41,3515', 0o03476, 'ENDRQWT', 'TC', 'REQUESTC -1', line=2856)

# REQUESTC WILL PUT TASK ADRES INTO MPAC+1, BBCON INTO MPAC+2,
# TC ENDOFJOB INTO MPAC+3.  IT WILL TAKE TIME DELAY OUT OF MPAC+4 AND
# LEAVE IT IN A, INHINT AND TC MPAC.

#   SETLOC NVSBENDL +1
#   COUNT 40/PIN

W('40,3347', 0o35017, 'VBPROC', 'CAF', 'ONE', 'PROCEED WITHOUT DATA', line=2865)
W('40,3350', 0o55014, '', 'TS', 'LOADSTAT', line=2866)
W('40,3351', 0o04220, '', 'TC', 'KILMONON', 'TURN ON KILL MONITOR BIT', line=2867)
W('40,3352', 0o04473, '', 'TC', 'RELDSP', line=2868)
W('40,3353', 0o04447, '', 'TC', 'FLASHOFF', line=2869)
W('40,3354', 0o03454, '', 'TC', 'RECALTST', 'SEE IF THERE IS ANY RECALL FROM ENDIDLE', line=2870)

# Page 367
W('40,3355', 0o45017, 'VBTERM', 'CS', 'ONE', line=2873)
W('40,3356', 0o03350, '', 'TC', 'VBPROC +1', 'TERM VERB SETS LOADSTAT NEG', line=2874)

# PROCKEY PERFORMS THE SAME FUNCTION AS VBPROC.  IT MUST BE CALLED UNDER
# EXECUTIVE CONTROL, WITH CHRPRIO.

W('40,3357', 0o35021, 'PROCKEY', 'CAF', 'ZERO', 'SET REQRET FOR ENTER PASS 0.', line=2879)
W('40,3360', 0o55013, '', 'TS', 'REQRET', line=2880)
W('40,3361', 0o44374, '', 'CS', 'VD1', 'BLOCK NUMERICAL CHARACTERS, SIGNS, CLEAR', line=2881)
W('40,3362', 0o54777, '', 'TS', 'DSPCOUNT', line=2882)
W('40,3363', 0o03347, '', 'TC', 'VBPROC', line=2883)

# VBRESEQ WAKES ENDIDLE AT SAME LINE AS FINAL ENTER OF LOAD (L+3).
# (MAIN USE IS INTENDED AS RESPONSE TO INTERNALLY INITIATED FLASHING
# DISPLAYS IN ENDIDLE.  SHOULD NOT BE USED WITH LOAD VERBS, PLEASE PERFORM,
# OR PLEASE MARK VERBS BECAUSE THEY ALREADY USE L+3 IN ANOTHER CONTEXT.)

W('40,3364', 0o45021, 'VBRESEQ', 'CS', 'ZERO', 'MAKE IT LOOK LIKE DATA IN.', line=2890)
W('40,3365', 0o03350, '', 'TC', 'VBPROC +1', line=2891)

# FLASH IS TURNED OFF BY PROCEED WITHOUT DATA, TERMINATE, RESEQUENCE,
# END OF LOAD.
# Page 368

# KEY RELEASE ROUTINE
#
# THIS ROUTINE ALWAYS TURNS OFF THE UPACT LIGHT AND ALWAYS CLEARS DSPLOCK.
#
# THE HIGHEST PRIORITY FUNCTION OF THE KEY RELEASE BUTTON IS THE
# UNSUSPENDING OF A SUSPENDED MONITOR WHICH WAS EXTERNALLY INITIATED.
# THIS FUNCTION IS ACCOMPLISHED BY CLEARING DSPLOCK AND TURNING OFF
# THE KEY RELEASE LIGHT IF BOTH DSPLIST AND CADRSTOR ARE EMPTY.
#
# IF NO SUCH MONITOR EXISTS, THEN RELDSP IS EXECUTED TO CLEAR DSPLOCK
# AND THE EXTERNAL MONITOR BIT (FREEING THE DISPLAY SYSTEM FOR INTERNAL
# USE), TURN OFF THE KEY RELEASE LIGHT, AND WAKE UP ANY JOB IN DSPLIST.
#
# IN ADDITION IF THERE IS A JOB IN ENDIDLE, THEN CONTROL IS TRANSFERRED
# TO PINBRNCH (IN DISPLAY INTERFACE ROUTINE) TO RE-EXECUTE THE SERIES OF
# NVSUB CALLS ETC. THAT PRECEDED THE ENDIDLE CALL STILL AWAITING RESPONSE.
# THIS FEATURE IS INTENDED FOR USE WHEN THE OPERATOR HAS BEEN REQUESTED TO
# RESPOND TO SOME INTERNAL ACTION THAT USED ENDIDLE, BUT HE HAS WRITTEN
# OVER THE INFORMATION ON THE DISPLAY PANEL BY SOME DISPLAYS OF HIS OWN
# INITIATION WHICH DO NOT SERVE AS RESPONSES.  HITTING KEYRLSE WILL
# RE-ESTABLISH THE DISPLAYS TO THE STATE THEY WERE IN BEOFRE HE OBSCURED
# THEM, SO THAT HE CAN SEE THE WAITING REQUEST.  THIS WORKS ONLY FOR
# INTERNAL PROGRAMS THAT USED ENDIDLE THROUGH MARGARET'S DISPLAY
# SUBROUTINES.

W('40,3366', 0o45015, 'VBRELDSP', 'CS', 'BIT3', line=2922)
W('40,3367', 0o00006, '', 'EXTEND', line=2923)
W('40,3370', 0o03011, '', 'WAND', 'DSALMOUT', 'TURN OF UPACT LITE', line=2924)
W('40,3371', 0o10115, '', 'CCS', '21/22REG', 'OLD DSPLOCK', line=2925)
W('40,3372', 0o35002, '', 'CAF', 'BIT14', line=2926)
W('40,3373', 0o71021, '', 'MASK', 'MONSAVE1', 'EXTERNAL MONITOR BIT (EMB)', line=2927)
W('40,3374', 0o10000, '', 'CCS', 'A', line=2928)
W('40,3375', 0o03404, '', 'TC', 'UNSUSPEN', 'OLD DSPLOCK AND EMB BOTH 1, UNSUSPEND,', line=2929)
W('40,3376', 0o04473, 'TSTLTS4', 'TC', 'RELDSP', 'NOT UNSUSPENDING EXTERNAL MONITOR', line=2930)
W('40,3377', 0o11042, '', 'CCS', 'CADRSTOR', '      RELEASE DISPLAY SYSTEM AND', line=2931)
W('40,3400', 0o03402, '', 'TC', '+2', '      DO RE-ESTABLISH IF CADRSTOR IS FULL.', line=2932)
W('40,3401', 0o05217, '', 'TC', 'ENDOFJOB', line=2933)
W('40,3402', 0o04701, '', 'TC', 'POSTJUMP', line=2934)
W('40,3403', 0o21272, '', 'CADR', 'PINBRNCH', kind='data', line=2935)
W('40,3404', 0o35021, 'UNSUSPEN', 'CAF', 'ZERO', 'EXTERNAL MONITOR IS SUSPENDED,', line=2936)
W('40,3405', 0o55012, '', 'TS', 'DSPLOCK', '      JUST UNSUSPEND IT BY CLEARING DSPLOCK.', line=2937)
W('40,3406', 0o11042, '', 'CCS', 'CADRSTOR', '      TURN KEY RELEASE LIGHT OFF IF BOTH', line=2938)
W('40,3407', 0o05217, '', 'TC', 'ENDOFJOB', '      CADRSTOR AND DSPLIST ARE EMPTY.', line=2939)
W('40,3410', 0o04516, '', 'TC', 'RELDSP1', line=2940)
W('40,3411', 0o05217, '', 'TC', 'ENDOFJOB', line=2941)

S('ENDRELDS', 'equals', 0o111412, line=2943)

# Page 369
# NVSUB IS USED FOR SUBROUTINE CALLS FROM WITHIN COMPUTER.  IT CAN BE
# USED TO CALL THE COMBINATION OF ANY DISPLAY, LOAD, OR MONITOR VERB
# TOGETHER WITH ANY NOUN AVAILABLE TO THE KEYBOARD.
# PLACE 0VVVVVVVNNNNNNN INTO A.
# V'S ARE THE 7-BIT VERB CODE.  N'S ARE THE 7-BIT NOUN CODE.
#
# IF NVSUB IS CALLED WITH THE FOLLOWING NEGATIVE NUMBERS (RATHER THAN THE
# VERB-NOUN CODE) IN A, THEN THE DISPLAY IS BLANKED AS FOLLOWS ---
# -4 FULL BLANK, -3 LEAVE MODE, -2 LEAVE MODE AND VERB, -1 BLANK R'S ONLY.
#
# NVSUB CAN BE USED WITH MACHINE CADR TO BE SPECIFIED BY PLACING THE CADR INTO
# MPAC+2 BEFORE THE STANDARD NVSUB CALL.
#
# NVSUB RETURNS TO 2+ CALLING LOC AFTER PERFORMING TASK, IF DISPLAY
# SYSTEM IS AVAILABLE.  THE NEW NOUN AND VERB CODES ARE DISPLAYED.
# IF V'S =0, THE NEW NOUN CODE IS DISPLAYED ONLY (RETURN WITH NO FURTHER
# ACTION).  IF N'S =0, THE NEW VERB CODE IS DISPLAYED ONLY (RETURN WITH NO
# FURTHER ACTION).
#
# IT RETURNS TO 1+ CALLING LOC WITHOUT PERFORMING TASK, IF DISPLAY
# SYSTEM IS BLOCKED (NOTHING IS DISPLAYED IN THIS CASE).
# IT DOES TC ABORT (WITH OCT 01501) IF IT ENCOUNTERS A DISPLAY PROGRAM
# ALARM CONDITION BEFORE RETURN TO CALLER.
#
# THE DISPLAY SYSTEM IS BLOCKED BY THE DEPRESSION OF ANY
# KEY, EXCEPT ERROR LIGHT RESET.
# IT IS RELEASED BY THE KEY RELEASE BUTTON, ALL EXTENDED VERBS,
# PROCEED WITHOUT DATA, TERMINATE, RESEQUENCE, INITIALIZE EXECUTIVE,
# RECALL PART OF RECALTST IF ENDIDLE WAS USED,
# VB = REQUEST EXECUTIVE, VB = REQUEST WAITLIST,
# MONITOR SET UP.
#
# THE DISPLAY SYSTEM IS ALSO BLOCKED BY THE EXTERNAL MONITOR BIT, WHICH
# INDICATES AND EXTERNALLY INITIATED MONITOR IS RUNNING (SEE MONITOR).
#
# A NVSUB CALL THAT PASSES DSPLOCK AND THE EXTERNAL MONITOR BIT ENDS OLD
# MONITOR.
#
# DSPLOCK IS THE INTERLOCK FOR USE OF KEYBOARD AND DISPLAY SYSTEM WHICH
# LOCKS OUT INTERNAL USE WHENEVER THERE IS EXTERNAL KEYBOARD ACTION.
#
# NVSUB SHOULD BE USED TWICE IN SUCCESSION FOR `PLEASE PERFORM' SITUATIONS
# (SIMILARLY FOR PLEASE MARK).  FIRST PLACE THE CODED NUMBER FOR WHAT
# ACTION IS DESIRED OF OPERATOR INTO THEREGISTERS REFERRED TO BY THE
# `CHECKLIST' NOUN.  GO TO NVSUB WITH A DISPLAY VERB AND THE `CHECKLIST'
# NOUN.  GO TO NVSUB AGAIN WITH THE `PLEASE PERFORM' VERB AND ZEROS IN THE
# LOW 7 BITS.  THIS `PASTES UP' THE `PLEASE PERFORM' VERB INTO THE VERB
# LIGHTS.
#
# NVMONOPT IS AN ENTRY SIMILAR TO NVSUB, BUT REQUIRING AN ADDITIONAL
# Page 370
# PARAMETER IN L.  IT SHOULD BE USED ONLY WITH A MONITOR VERB-NOUN CODE IN
# A.  AFTER EACH MONITOR DISPLAY A *PLEASE* VERB WILL BE PASTED IN THE VERB
# LIGHTS OR DATA WILL BE BLANKED (OR BOTH) ACCORDING TO THE OPTIONS
# SPECIFIED IN L.  IF BITS 8-14 OF L ARE OTHER THAN ZERO, THEN THEY WILL
# BE INTERPRETED AS A VERB CODE AND PASTED IN THE VERB LIGHTS.  (THIS VERB
# CODE SHOULD DESIGNATE ONE OF THE *PLEASE* VERBS.)  IF BITS 1-3 OF L ARE
# OTHER THAN ZERO, THEN THEY WILL BE USED BO BLANK DATA BY BEING FED TO
# BLANKSUB.  IF NVMONOPT IS USED WITH A VERB OTHER THAN A MONITOR VERB,
# THE PARAMETER IN L HAS NO EFFECT.
#
# NVSUB IN FIXED-FIXED PLACES 2+CALLING LOC INTO NVQTEM, TC NVSUBEND INTO
# ENTRET.  (THIS WILL RESTORE OLD CALLING BANK BITS)

#   SETLOC ENDALM +1

#   COUNT 02/PIN

W('4170', 0o22007, 'NVSUB', 'LXCH', '7', 'ZERO NVMONOPT OPTIONS', line=3014)
W('4171', 0o54123, 'NVMONOPT', 'TS', 'NVTEMP', line=3015)
W('4172', 0o35002, '', 'CAF', 'BIT14', line=3016)
W('4173', 0o71021, '', 'MASK', 'MONSAVE1', 'EXTERNAL MONITOR BIT', line=3017)
W('4174', 0o61012, '', 'AD', 'DSPLOCK', line=3018)
W('4175', 0o10000, '', 'CCS', 'A', line=3019)
W('4176', 0o00002, '', 'TC', 'Q', 'DSP SYST BLOCKED.  RET TO 1.  CALLING LOC', line=3020)
W('4177', 0o35017, '', 'CAF', 'ONE', 'DSP SYST AVAILABLE.', line=3021)
W('4200', 0o60002, 'NVSBCOM', 'AD', 'Q', line=3022)
W('4201', 0o55037, '', 'TS', 'NVQTEM', '2+ CALLING LOC INTO NVQTEM', line=3023)
W('4202', 0o23022, '', 'LXCH', 'MONSAVE2', 'STORE NVMONOPT OPTIONS', line=3024)
W('4203', 0o04220, '', 'TC', 'KILMONON', 'TURN ON KILL MONITOR BIT', line=3025)
W('4204', 0o34215, 'NVSUBCOM', 'CAF', 'NVSBBBNK', line=3026)

W('4205', 0o56006, '', 'XCH', 'BBANK', line=3028)
W('4206', 0o00006, '', 'EXTEND', '', 'SAVE OLD SUPERBITS', line=3029)
W('4207', 0o04007, '', 'ROR', 'SUPERBNK', line=3030)
W('4210', 0o55040, '', 'TS', 'NVBNKTEM', line=3031)
W('4211', 0o34215, '', 'CAF', 'PINSUPBT', line=3032)
W('4212', 0o00006, '', 'EXTEND', line=3033)
W('4213', 0o01007, '', 'WRITE', 'SUPERBNK', line=3034)
W('4214', 0o02000, '', 'TC', 'NVSUBB', 'GO TO NVSUB1 THRU STANDARD LOC', line=3035)
#   EBANK= DSPCOUNT
W('4215', 0o62101, 'NVSBBBNK', 'BBCON', 'NVSUB1', kind='data', line=3037)

S('PINSUPBT', 'equals', 0o4215, line=3039)  # CONTAINS THE PINBALL SUPERBIT.

W('4216', 0o53040, 'NVSUBEND', 'DXCH', 'NVQTEM', 'NVBNKTEM MUST = NVQTEM+1', line=3041)
W('4217', 0o05227, '', 'TC', 'SUPDXCHZ', 'DTCB WITH SUPERBIT SWITCHING', line=3042)

#   SETLOC ENDRQWT +1

#   COUNT 41/PIN
# Page 371

# BLANKDSP BLANKS DISPLAY ACCORDING TO OPTION NUMBER IN NVTEMP AS FOLLOWS:
# -4 FULL BLANK, -3 LEAVE MODE, -2 LEAVE MODE AND VERB, -1 BLANK R'S ONLY.

W('41,3516', 0o65023, 'BLANKDSP', 'AD', 'SEVEN', '7,8,9, OR 10 (A HAD 0,1,2,OR 3)', line=3052)
W('41,3517', 0o00004, '', 'INHINT', line=3053)
W('41,3520', 0o54124, '', 'TS', 'CODE', 'BLANK SPECIFIED DSPTABS', line=3054)
W('41,3521', 0o45004, '', 'CS', 'BIT12', line=3055)
W('41,3522', 0o50124, '', 'INDEX', 'CODE', line=3056)
W('41,3523', 0o57023, '', 'XCH', 'DSPTAB', line=3057)
W('41,3524', 0o10000, '', 'CCS', 'A', line=3058)
W('41,3525', 0o25016, '', 'INCR', 'NOUT', line=3059)
W('41,3526', 0o03527, '', 'TC', '+1', line=3060)
W('41,3527', 0o10124, '', 'CCS', 'CODE', line=3061)
W('41,3530', 0o03520, '', 'TC', 'BLANKDSP +2', line=3062)
W('41,3531', 0o00003, '', 'RELINT', line=3063)
W('41,3532', 0o50123, '', 'INDEX', 'NVTEMP', line=3064)
W('41,3533', 0o03540, '', 'TC', '+5', line=3065)
W('41,3534', 0o03535, '', 'TC', '+1', 'NVTEMP HAS    -4 (NEVER TOUCH MODREG)', line=3066)
W('41,3535', 0o55001, '', 'TS', 'VERBREG', '              -3', line=3067)
W('41,3536', 0o55002, '', 'TS', 'NOUNREG', '              -2', line=3068)
W('41,3537', 0o55015, '', 'TS', 'CLPASS', '              -1', line=3069)
W('41,3540', 0o44374, '', 'CS', 'VD1', line=3070)
W('41,3541', 0o54777, '', 'TS', 'DSPCOUNT', line=3071)
W('41,3542', 0o04447, '', 'TC', 'FLASHOFF', 'PROTECT AGAINST INVISIBLE FLASH', line=3072)
W('41,3543', 0o03566, '', 'TC', 'ENTSET -2', 'ZEROS REQRET', line=3073)

W('41,3544', 0o33570, 'NVSUB1', 'CAF', 'ENTSET', 'IN BANK', line=3075)
W('41,3545', 0o54136, '', 'TS', 'ENTRET', 'SET RETURN TO NVSUBEND', line=3076)
W('41,3546', 0o10123, '', 'CCS', 'NVTEMP', 'WHAT NOW', line=3077)
W('41,3547', 0o03553, '', 'TC', '+4', 'NORMAL NVSUB CALL (EXECUTE VN OR PASTE)', line=3078)
W('41,3550', 0o02351, '', 'TC', 'GODSPALM', line=3079)
W('41,3551', 0o03516, '', 'TC', 'BLANKDSP', 'BLANK DISPLAY AS SPECIFIED', line=3080)
W('41,3552', 0o02351, '', 'TC', 'GODSPALM', line=3081)
W('41,3553', 0o36043, '', 'CAF', 'LOW7', line=3082)
W('41,3554', 0o70123, '', 'MASK', 'NVTEMP', line=3083)
W('41,3555', 0o54157, '', 'TS', 'MPAC +3', "TEMP FOR NOUN (CAN'T USE MPAC.  DSPDECVN", line=3084)
W('41,3556', 0o30123, '', 'CA', 'NVTEMP', '               USES MPAC, +1, +2).', line=3085)
W('41,3557', 0o54023, '', 'TS', 'EDOP', 'RIGHT 7', line=3086)
W('41,3560', 0o30023, '', 'CA', 'EDOP', line=3087)
W('41,3561', 0o54160, '', 'TS', 'MPAC +4', "TEMP FOR VERB (CAN'T USE MPAC+1.  DSPDECVN", line=3088)
# USES MPAC, +1, +2)
W('41,3562', 0o10157, '', 'CCS', 'MPAC +3', 'TEST NOUN', line=3090)
W('41,3563', 0o03571, '', 'TC', 'NVSUB2', 'IF NOUN NOT +0, GO ON', line=3091)
W('41,3564', 0o30160, '', 'CA', 'MPAC +4', line=3092)
W('41,3565', 0o02337, '', 'TC', 'UPDATVB -1', 'IF NOUN = +0, DISPLAY VERB.  THEN RETURN', line=3093)
W('41,3566', 0o35021, '', 'CAF', 'ZERO', 'ZERO REQRET SO THAT PASTED VERBS CAN', line=3094)
W('41,3567', 0o55013, '', 'TS', 'REQRET', 'BE EXECUTED BY OPERATOR.', line=3095)
W('41,3570', 0o04216, 'ENTSET', 'TC', 'NVSUBEND', line=3096)
W('41,3571', 0o10160, 'NVSUB2', 'CCS', 'MPAC +4', 'TEST VERB', line=3097)
W('41,3572', 0o03576, '', 'TC', '+4', 'IF VERB NOT +0, GO ON', line=3098)
# Page 372
W('41,3573', 0o30157, '', 'CA', 'MPAC +3', line=3100)
W('41,3574', 0o02317, '', 'TC', 'UPDATNN -1', 'IF VERB = +0, DISPLAY NOUN.  THEN RETURN', line=3101)
W('41,3575', 0o04216, '', 'TC', 'NVSUBEND', line=3102)
W('41,3576', 0o30156, '', 'CA', 'MPAC +2', 'TEMP FOR MACH CADR TO BE SPEC.  (DSPDECVN', line=3103)
W('41,3577', 0o54161, '', 'TS', 'MPAC +5', '      USES MPAC, +1, +2)', line=3104)
W('41,3600', 0o30160, '', 'CA', 'MPAC +4', line=3105)
W('41,3601', 0o02337, '', 'TC', 'UPDATVB -1', 'IF BOTH NOUN AND VERB NOT +0, DISPLAY', line=3106)
W('41,3602', 0o30157, '', 'CA', 'MPAC +3', 'BOTH AND GO TO ENTPAS0.', line=3107)
W('41,3603', 0o02317, '', 'TC', 'UPDATNN -1', line=3108)
W('41,3604', 0o35021, '', 'CAF', 'ZERO', line=3109)
W('41,3605', 0o55014, '', 'TS', 'LOADSTAT', 'SET FOR WAITING FOR DATA CONDITION', line=3110)
W('41,3606', 0o55015, '', 'TS', 'CLPASS', line=3111)
W('41,3607', 0o55013, '', 'TS', 'REQRET', 'SET REQRET FOR PASS 0.', line=3112)
W('41,3610', 0o30161, '', 'CA', 'MPAC +5', 'RESTORES MACH CADR TO BE SPEC TO MPAC+2', line=3113)
W('41,3611', 0o54156, '', 'TS', 'MPAC +2', 'FOR USE IN INTMCTBS (IN ENTPAS0).', line=3114)
W('41,3612', 0o02035, 'ENDNVSB1', 'TC', 'ENTPAS0', line=3115)

# IF INTERNAL MACH CADR TO BE SPECIFIED, MPAC+2 WILL BE PLACED INTO
# NOUNCADR IN ENTPAS0 (INTMCTBS).

#   SETLOC NVSUBEND +2
#   COUNT 02/PIN
# FORCE BIT 15 OF MONSAVE1 TO .
W('4220', 0o35001, 'KILMONON', 'CAF', 'BIT15', '      THIS IS THE KILL MONITOR BIT.', line=3123)
W('4221', 0o55021, '', 'TS', 'MONSAVE1', 'TURN OFF BIT 14, THE EXTERNAL', line=3124)
# MONITOR BIT.
W('4222', 0o00002, '', 'TC', 'Q', line=3126)

# LOADSTAT      +0      INACTIVE (WAITING FOR DATA).  SET BY NVSUB
# +1      PROCEED NO DATA.  SET BY SPECIAL VERB
# -1      TERMINATE.  SET BY SPECIAL VERB.
# -0      DATA IN.        SET BY END OF LOAD ROUTINE.
# OR RESEQUENCE.  SET BY VERB 32
#
# L TO ENDIDLE (FIXED FIXED).
# ROUTINES THAT REQUEST LOADS THROUGH NVSUB SHOULD USE ENDIDLE WHILE
# WAITING FOR THE DATA TO BE LOADED.  ENDIDLE PUTS CURRENT JOB TO SLEEP.
# ENDIDLE CANNOT BE CALLED FROM ERASABLE OR F/F MEMORY,
# SINCE JOB SLEEP AND JOBWAKE CAN HANDLE ONLY FIXED BANKS.
# RECALTST TESTS LOADSTAT AND WAKES JOB UP TO,
# L+1     FOR TERMINATE
# L+2     FOR PROCEED WITHOUT DATA
# L+3     FOR DATA IN, OR RESEQUENCE
# IT DOES NOTHING IF LOADSTAT INDICATES WAITING FOR DTA.
# Page 373
#
# ENDIDLE ABORTS (WITH CODE 1206) IF A SECOND JOB ATTEMPTS TO GO TO SLEEP
# IN PINBALL.  IN PARTICULAR, IF AN ATTEMPT IS MADE TO GO TO ENDIDLE WHEN
# 1)      CADRSTOR NOT= +0.  THIS IS THE CASE WHERE THE CAPACITY OF ENDIDLE IS
# EXCEEDED.  (+-NZ INDICATES A JOB IS ALREADY ASLEEP DUE TO ENDIDDLE.)
# 2)      DSPLIST NOT= +0.  THIS INDICATES A JOB IS ALREADY ASLEEP DUE TO
# NVSUBUSY.

W('4223', 0o22002, 'ENDIDLE', 'LXCH', 'Q', 'RETURN ADDRESS INTO L.', line=3153)
W('4224', 0o04234, '', 'TC', 'ISCADR+0', 'ABORT IF CADRSTOR NOT= +0.', line=3154)
W('4225', 0o04240, '', 'TC', 'ISLIST+0', 'ABORT IF DSPLIST NOT= +0', line=3155)
W('4226', 0o30001, '', 'CA', 'L', "DON'T SET DSPLOC TO 1 SO CAN USE", line=3156)
W('4227', 0o75054, '', 'MASK', 'LOW10', 'ENDIDLE WITH NVSUB INITIATE MONITOR.', line=3157)
W('4230', 0o60004, '', 'AD', 'FBANK', 'SAME STRATEGY FOR CADR AS MAKECADR.', line=3158)
W('4231', 0o55042, '', 'TS', 'CADRSTOR', line=3159)
W('4232', 0o05175, '', 'TC', 'JOBSLEEP', line=3160)

W('4233', 0o05217, 'ENDINST', 'TC', 'ENDOFJOB', line=3162)

W('4234', 0o11042, 'ISCADR+0', 'CCS', 'CADRSTOR', 'ABORTS (CODE 01206) IF CADRSTOR NOT= +0.', line=3164)
W('4235', 0o04243, '', 'TC', 'DSPABORT', 'RETURNS IF CADRSTOR = +0.', line=3165)
W('4236', 0o00002, '', 'TC', 'Q', line=3166)
W('4237', 0o04243, '', 'TC', 'DSPABORT', line=3167)

W('4240', 0o11043, 'ISLIST+0', 'CCS', 'DSPLIST', 'ABORTS (CODE 01206) IF DSPLIST NOT= +0.', line=3169)
W('4241', 0o04243, '', 'TC', 'DSPABORT', 'RETURNS IF DSPLIST = +0.', line=3170)
W('4242', 0o00002, '', 'TC', 'Q', line=3171)
W('4243', 0o05721, 'DSPABORT', 'TC', 'POODOO', line=3172)
W('4244', 0o01206, '', 'OCT', '01206', kind='data', line=3173)

# JAMTERM ALLOWS PROGRAMS TO PERFORM THE TERMINATE FUNCTION.
# IT DOES ENDOFJOB.

W('4245', 0o34215, 'JAMTERM', 'CAF', 'PINSUPBT', line=3178)
W('4246', 0o00006, '', 'EXTEND', line=3179)
W('4247', 0o01007, '', 'WRITE', 'SUPERBNK', line=3180)
W('4250', 0o34256, '', 'CAF', '34DEC', line=3181)
W('4251', 0o55013, '', 'TS', 'REQRET', 'LEAVE ENTER SET FOR ENTPASS0.', line=3182)
W('4252', 0o44374, '', 'CS', 'VD1', line=3183)
W('4253', 0o54777, '', 'TS', 'DSPCOUNT', line=3184)
W('4254', 0o04701, '', 'TC', 'POSTJUMP', line=3185)
W('4255', 0o61355, '', 'CADR', 'VBTERM', kind='data', line=3186)

W('4256', 0o00042, '34DEC', 'DEC', '34', kind='data', line=3188)

# JAMPROC ALLOWS PROGRAMS TO PERFORM THE PROCEED/PROCEED WITHOUT DATA
# FUNCTION.  IT DOES ENDOFJOB.
# Page 374

W('4257', 0o34215, 'JAMPROC', 'CAF', 'PINSUPBT', line=3194)
W('4260', 0o00006, '', 'EXTEND', line=3195)
W('4261', 0o01007, '', 'WRITE', 'SUPERBNK', line=3196)
W('4262', 0o34270, '', 'CAF', '33DEC', line=3197)
W('4263', 0o55013, '', 'TS', 'REQRET', 'LEAVE ENTER SET FOR ENTPASS0.', line=3198)
W('4264', 0o44374, '', 'CS', 'VD1', line=3199)
W('4265', 0o54777, '', 'TS', 'DSPCOUNT', line=3200)
W('4266', 0o04701, '', 'TC', 'POSTJUMP', line=3201)
W('4267', 0o61347, '', 'CADR', 'VBPROC', kind='data', line=3202)

W('4270', 0o00041, '33DEC', 'DEC', '33', kind='data', line=3204)

# BLANKSUB BLANKS ANY COMBINATION OF R1, R2, R3.
# CALL WITH BLANKING CODE IN A.
# BIT1=1 BLANKS R1, BIT2=1 BLANKS R2, BIT3=1 BLANKS R3.
# ANY COMBINATION OF THESE BITS IS ACCEPTED.
#
# DSPCOUNT IS RESTORED TO STATE IT WAS IN BEFORE BLANKSUB WAS EXECUTED.

W('4271', 0o75023, 'BLANKSUB', 'MASK', 'SEVEN', line=3213)
W('4272', 0o54123, '', 'TS', 'NVTEMP', 'STORE BLANKING CODE IN NVTEMP.', line=3214)
W('4273', 0o35002, '', 'CAF', 'BIT14', line=3215)
W('4274', 0o71021, '', 'MASK', 'MONSAVE1', 'EXTERNAL MONITOR BIT', line=3216)
W('4275', 0o61012, '', 'AD', 'DSPLOCK', line=3217)
W('4276', 0o10000, '', 'CCS', 'A', line=3218)
W('4277', 0o00002, '', 'TC', 'Q', 'DSP SYST BLOCKED.  RET TO 1+ CALLING LOC', line=3219)
W('4300', 0o24002, '', 'INCR', 'Q', 'DSP SYST AVAILABLE', line=3220)
# SET RETURN FOR 2+ CALLING LOC
W('4301', 0o10123, '', 'CCS', 'NVTEMP', line=3222)
W('4302', 0o14304, '', 'TCF', '+2', line=3223)
W('4303', 0o00002, '', 'TC', 'Q', 'NOTHING TO BLANK.  RET TO 2+ CALLING LOC', line=3224)
W('4304', 0o22002, '', 'LXCH', 'Q', 'SET RETURN FOR 2 + CALLING LOC', line=3225)
W('4305', 0o34316, '', 'CAF', 'BLNKBBNK', line=3226)
W('4306', 0o56006, '', 'XCH', 'BBANK', line=3227)
W('4307', 0o00006, '', 'EXTEND', line=3228)
W('4310', 0o04007, '', 'ROR', 'SUPERBNK', 'SAVE OLD SUPERBITS.', line=3229)
W('4311', 0o52131, '', 'DXCH', 'BUF', line=3230)
W('4312', 0o34215, '', 'CAF', 'PINSUPBT', line=3231)
W('4313', 0o00006, '', 'EXTEND', line=3232)
W('4314', 0o01007, '', 'WRITE', 'SUPERBNK', line=3233)
W('4315', 0o03412, '', 'TC', 'BLNKSUB1', line=3234)

#   EBANK= DSPCOUNT
W('4316', 0o60101, 'BLNKBBNK', 'BBCON', 'BLNKSUB1', kind='data', line=3237)
S('ENDBLFF', 'equals', 0o4317, line=3238)

#   SETLOC ENDRELDS
#   COUNT 40/PIN

# Page 375
W('40,3412', 0o30777, 'BLNKSUB1', 'CA', 'DSPCOUNT', 'SAVE OLD DSPCOUNT FOR LATER RESTORATION', line=3244)
W('40,3413', 0o54132, '', 'TS', 'BUF +2', line=3245)
W('40,3414', 0o35017, '', 'CAF', 'BIT1', 'TEST BIT1.  SEE IF R1 TO BE BLANKED.', line=3246)
W('40,3415', 0o03434, '', 'TC', 'TESTBIT', line=3247)
W('40,3416', 0o34333, '', 'CAF', 'R1D1', line=3248)
W('40,3417', 0o02436, '', 'TC', '5BLANK -1', line=3249)
W('40,3420', 0o35016, '', 'CAF', 'BIT2', 'TEST BIT2.  SEE IF R2 TO BE BLANKED.', line=3250)
W('40,3421', 0o03434, '', 'TC', 'TESTBIT', line=3251)
W('40,3422', 0o34334, '', 'CAF', 'R2D1', line=3252)
W('40,3423', 0o02436, '', 'TC', '5BLANK -1', line=3253)
W('40,3424', 0o35015, '', 'CAF', 'BIT3', 'TEST BIT3.  SEE IF R3 TO BE BLANKED.', line=3254)
W('40,3425', 0o03434, '', 'TC', 'TESTBIT', line=3255)
W('40,3426', 0o34335, '', 'CAF', 'R3D1', line=3256)
W('40,3427', 0o02436, '', 'TC', '5BLANK -1', line=3257)
W('40,3430', 0o30132, '', 'CA', 'BUF +2', 'RESTORE DSPCOUNT TO STATE IT HAD', line=3258)
W('40,3431', 0o54777, '', 'TS', 'DSPCOUNT', '      BEFORE BLANKSUB.', line=3259)
W('40,3432', 0o52131, '', 'DXCH', 'BUF', 'CALL L+2 DIRECTORY.', line=3260)
W('40,3433', 0o05230, '', 'TC', 'SUPDXCHZ +1', 'DTCB WITH SUPERBIT SWITCHING', line=3261)

W('40,3434', 0o70123, 'TESTBIT', 'MASK', 'NVTEMP', 'NVTEMP CONTAINS BLANKING CODE', line=3263)
W('40,3435', 0o10000, '', 'CCS', 'A', line=3264)
W('40,3436', 0o00002, '', 'TC', 'Q', 'IF CURRENT BIT = 1, RETURN TO L+1.', line=3265)
W('40,3437', 0o50002, '', 'INDEX', 'Q', 'IF CURRENT BIT = 0, RETURN TO L+3.', line=3266)
W('40,3440', 0o00002, '', 'TC', '2', line=3267)

S('ENDBSUB1', 'equals', 0o111441, line=3269)

# DSPMM DOES NOT DISPLAY MODREG DIRECTLY.  IT PUTS IN EXEC REQUEST WITH
# PRIO 30000 FOR DSPMMJB AND RETURNS TO CALLER.
#
# IF MODREG CONTAINS -0, DSPMMJB BLANKS THE MODE LIGHTS.
#
# DSPMM MUST BE IN BANK 27 OR LOWER, SO IT CAN BE CALLED VIA BANKCALL.

#   BANK 7
#   SETLOC PINBALL4
#   BANK

#   COUNT 07/PIN

W('04,2566', 0o56002, 'DSPMM', 'XCH', 'Q', line=3284)
W('04,2567', 0o54154, '', 'TS', 'MPAC', line=3285)
W('04,2570', 0o00004, '', 'INHINT', line=3286)
W('04,2571', 0o34371, '', 'CAF', 'CHRPRIO', line=3287)
W('04,2572', 0o05134, '', 'TC', 'NOVAC', line=3288)
#   EBANK= DSPCOUNT
W('04,2573', 0o03441, '', '2CADR', 'DSPMMJB', kind='data', line=3290)
W('04,2574', 0o60101, kind='data', line=3290)

W('04,2575', 0o00003, '', 'RELINT', line=3292)
# Page 376
W('04,2576', 0o00154, 'ENDSPMM', 'TC', 'MPAC', line=3294)

# DSPMM PLACE MAJOR MODE CODE INTO MODREG

#   SETLOC ENDBSUB1

#   COUNT 40/PIN

W('40,3441', 0o34376, 'DSPMMJB', 'CAF', 'MD1', 'GETS HERE THRU DSPMM', line=3302)
W('40,3442', 0o56777, '', 'XCH', 'DSPCOUNT', line=3303)
W('40,3443', 0o54140, '', 'TS', 'DSPMMTEM', 'SAVE DSPCOUNT', line=3304)
W('40,3444', 0o11011, '', 'CCS', 'MODREG', line=3305)
W('40,3445', 0o65017, '', 'AD', 'ONE', line=3306)
W('40,3446', 0o03213, '', 'TC', 'DSPDECVN', 'IF MODREG IS + OR +0, DISPLAY MODREG', line=3307)
W('40,3447', 0o03451, '', 'TC', '+2', 'IF MODREG IS -NZ, DO NOTHING', line=3308)
W('40,3450', 0o02502, '', 'TC', '2BLANK', 'IF MODREG IS -0, BLANK MM', line=3309)
W('40,3451', 0o56140, '', 'XCH', 'DSPMMTEM', 'RESTORE DSPCOUNT', line=3310)
W('40,3452', 0o54777, '', 'TS', 'DSPCOUNT', line=3311)
W('40,3453', 0o05217, '', 'TC', 'ENDOFJOB', line=3312)

# RECALTST IS ENTERED DIRECTLY AFTER DATA IS LOADED (OR RESEQUENCE VERB IS
# EXECUTED), TERMINATE VERB IS EXECUTED, OR PROCEED WITHOUT DATA VERB IS
# EXECUTED.  IT WAKES UP JOB THAT DID TC ENDIDLE.
#
# IF CADRSTOR NOT= +0, IT PUTS +0 INTO DSPLOCK, AND TURNS OFF KEY RLSE
# LIGHT IF DSPLIST IS EMPTY (LEAVES KEY RLSE LIGHT ALONE IF NOT EMPTY).

W('40,3454', 0o11042, 'RECALTST', 'CCS', 'CADRSTOR', line=3321)
W('40,3455', 0o03457, '', 'TC', 'RECAL1', line=3322)
W('40,3456', 0o05217, '', 'TC', 'ENDOFJOB', 'NORMAL EXIT IF KEYBOARD INITIATED', line=3323)
W('40,3457', 0o35021, 'RECAL1', 'CAF', 'ZERO', line=3324)
W('40,3460', 0o57042, '', 'XCH', 'CADRSTOR', line=3325)
W('40,3461', 0o00004, '', 'INHINT', line=3326)
W('40,3462', 0o05201, '', 'TC', 'JOBWAKE', line=3327)
W('40,3463', 0o11014, '', 'CCS', 'LOADSTAT', line=3328)
W('40,3464', 0o03506, '', 'TC', 'DOPROC', '+ PROCEED WITHOUT DATA', line=3329)
W('40,3465', 0o05217, '', 'TC', 'ENDOFJOB', 'PATHOLOGICAL CASE EXIT', line=3330)
W('40,3466', 0o03504, '', 'TC', 'DOTERM', '-  TERMINATE', line=3331)
W('40,3467', 0o35016, '', 'CAF', 'TWO', '-0 DATA IN OR RESEQUENCE', line=3332)
W('40,3470', 0o50064, 'RECAL2', 'INDEX', 'LOCCTR', line=3333)
W('40,3471', 0o60164, '', 'AD', 'LOC', 'LOC IS + FOR BASIC JOBS', line=3334)
W('40,3472', 0o50064, '', 'INDEX', 'LOCCTR', line=3335)
W('40,3473', 0o54164, '', 'TS', 'LOC', line=3336)
W('40,3474', 0o31002, '', 'CA', 'NOUNREG', 'SAVE VERB IN MPAC, NOUN IN MPAC+1 AT', line=3337)
W('40,3475', 0o54001, '', 'TS', 'L', 'TIME OF RESPONSE TO ENDIDLE FOR', line=3338)
W('40,3476', 0o31001, '', 'CA', 'VERBREG', 'POSSIBLE LATER TESTING BY JOB THAT HAS', line=3339)
W('40,3477', 0o50064, '', 'INDEX', 'LOCCTR', 'BEEN WAKED UP.', line=3340)
W('40,3500', 0o52155, '', 'DXCH', 'MPAC', line=3341)
W('40,3501', 0o00003, '', 'RELINT', line=3342)
# Page 377
W('40,3502', 0o04473, 'RECAL3', 'TC', 'RELDSP', line=3344)
W('40,3503', 0o05217, '', 'TC', 'ENDOFJOB', line=3345)

W('40,3504', 0o35021, 'DOTERM', 'CAF', 'ZERO', line=3347)
W('40,3505', 0o03470, '', 'TC', 'RECAL2', line=3348)

W('40,3506', 0o35017, 'DOPROC', 'CAF', 'ONE', line=3350)
W('40,3507', 0o03470, '', 'TC', 'RECAL2', line=3351)

#   SBANK= LOWSUPER
# Page 378
# MISCELLANEOUS SERVICE ROUTINES IN FIXED/FIXED

#   SETLOC ENDBLFF

#   COUNT 02/PIN

# SETNCADR      E CADR ARRIVES IN A.  IT IS STORED IN NOUNCADR.  EBANK BITS
# ARE SET.  E ADRES IS DERIVED AND PUT INTO NOUNADD.

W('4317', 0o55017, 'SETNCADR', 'TS', 'NOUNCADR', 'STORE ECADR', line=3364)
W('4320', 0o54003, '', 'TS', 'EBANK', 'SET EBANK BITS', line=3365)
W('4321', 0o74373, '', 'MASK', 'LOW8', line=3366)
W('4322', 0o65051, '', 'AD', 'OCT1400', line=3367)
W('4323', 0o54145, '', 'TS', 'NOUNADD', 'PUT E ADRES INTO NOUNADD', line=3368)
W('4324', 0o00002, '', 'TC', 'Q', line=3369)

# SETNADD       GETS E CADR FROM NOUNCADR, SETS EBANK BITS, DERIVES
# E ADRES AND PUTS IT INTO NOUNADD.

W('4325', 0o31017, 'SETNADD', 'CA', 'NOUNCADR', line=3374)
W('4326', 0o14320, '', 'TCF', 'SETNCADR +1', line=3375)

# SETEBANK      E CADR ARRIVES IN A.  EBANK BITS ARE SET.  E ADRES IS
# DERIVED AND LEFT IN A.

W('4327', 0o54003, 'SETEBANK', 'TS', 'EBANK', 'SET EBANK BITS', line=3380)
W('4330', 0o74373, '', 'MASK', 'LOW8', line=3381)
W('4331', 0o65051, '', 'AD', 'OCT1400', 'E ADRES LEFT IN A', line=3382)
W('4332', 0o00002, '', 'TC', 'Q', line=3383)

W('4333', 0o00016, 'R1D1', 'OCT', '16', 'THESE 3 CONSTANTS FORM A PACKED TABLE.', kind='data', line=3385)
W('4334', 0o00011, 'R2D1', 'OCT', '11', "DON'T SEPARATE.", kind='data', line=3386)
W('4335', 0o00004, 'R3D1', 'OCT', '4', kind='data', line=3387)

W('4336', 0o54020, 'RIGHT5', 'TS', 'CYR', line=3389)
W('4337', 0o40020, '', 'CS', 'CYR', line=3390)
W('4340', 0o40020, '', 'CS', 'CYR', line=3391)
W('4341', 0o40020, '', 'CS', 'CYR', line=3392)
W('4342', 0o40020, '', 'CS', 'CYR', line=3393)
W('4343', 0o56020, '', 'XCH', 'CYR', line=3394)
W('4344', 0o00002, '', 'TC', 'Q', line=3395)

W('4345', 0o54022, 'LEFT5', 'TS', 'CYL', line=3397)
W('4346', 0o40022, '', 'CS', 'CYL', line=3398)
W('4347', 0o40022, '', 'CS', 'CYL', line=3399)
W('4350', 0o40022, '', 'CS', 'CYL', line=3400)
# Page 379
W('4351', 0o40022, '', 'CS', 'CYL', line=3402)
W('4352', 0o56022, '', 'XCH', 'CYL', line=3403)
W('4353', 0o00002, '', 'TC', 'Q', line=3404)

W('4354', 0o60000, 'SLEFT5', 'DOUBLE', line=3406)
W('4355', 0o60000, '', 'DOUBLE', line=3407)
W('4356', 0o60000, '', 'DOUBLE', line=3408)
W('4357', 0o60000, '', 'DOUBLE', line=3409)
W('4360', 0o60000, '', 'DOUBLE', line=3410)
W('4361', 0o00002, '', 'TC', 'Q', line=3411)

W('4362', 0o00037, 'LOW5', 'OCT', '37', 'THESE 3 CONSTANTS FORM A PACKED TABLE.', kind='data', line=3413)
W('4363', 0o01740, 'MID5', 'OCT', '1740', "DON'T SEPARATE.", kind='data', line=3414)
W('4364', 0o76000, 'HI5', 'OCT', '76000', 'MUST STAY HERE', kind='data', line=3415)

W('4365', 0o05134, 'TCNOVAC', 'TC', 'NOVAC', line=3417)
W('4366', 0o05245, 'TCWAIT', 'TC', 'WAITLIST', line=3418)
W('4367', 0o05324, 'TCTSKOVR', 'TC', 'TASKOVER', line=3419)
W('4370', 0o05147, 'TCFINDVC', 'TC', 'FINDVAC', line=3420)

W('4371', 0o30000, 'CHRPRIO', 'OCT', '30000', 'EXEC PRIORITY OF CHARIN', kind='data', line=3422)

W('4372', 0o03777, 'LOW11', 'OCT', '3777', kind='data', line=3424)
S('B12-1', 'equals', 0o4372, line=3425)
W('4373', 0o00377, 'LOW8', 'OCT', '377', kind='data', line=3426)

W('4374', 0o00023, 'VD1', 'OCT', '23', 'THESE 3 CONSTANTS FORM A PACKED TABLE.', kind='data', line=3428)
W('4375', 0o00021, 'ND1', 'OCT', '21', "DON'T SEPARATE.", kind='data', line=3429)
W('4376', 0o00025, 'MD1', 'OCT', '25', kind='data', line=3430)

W('4377', 0o00012, 'BINCON', 'DEC', '10', kind='data', line=3432)

W('4400', 0o35011, 'FALTON', 'CA', 'BIT7', 'TURN ON OPERATOR ERROR LIGHT.', line=3434)
W('4401', 0o00006, '', 'EXTEND', line=3435)
W('4402', 0o05011, '', 'WOR', 'DSALMOUT', 'BIT 7 OF CHANNEL 11', line=3436)
W('4403', 0o00002, '', 'TC', 'Q', line=3437)

W('4404', 0o45011, 'FALTOF', 'CS', 'BIT7', 'TURN OFF OPERATOR ERROR LIGHT', line=3439)
W('4405', 0o00006, '', 'EXTEND', line=3440)
W('4406', 0o03011, '', 'WAND', 'DSALMOUT', 'BIT 7 OF CHANNEL 11', line=3441)
W('4407', 0o00002, '', 'TC', 'Q', line=3442)

W('4410', 0o35013, 'RELDSPON', 'CAF', 'BIT5', 'TURN ON KEY RELEASE LIGHT', line=3444)
W('4411', 0o00006, '', 'EXTEND', line=3445)
W('4412', 0o05011, '', 'WOR', 'DSALMOUT', 'BIT 5 OF CHANNEL 11', line=3446)
W('4413', 0o00002, '', 'TC', 'Q', line=3447)

# Page 380
W('4414', 0o00006, 'LODSAMPT', 'EXTEND', line=3450)
W('4415', 0o30025, '', 'DCA', 'TIME2', line=3451)
W('4416', 0o52014, '', 'DXCH', 'SAMPTIME', line=3452)
W('4417', 0o00002, '', 'TC', 'Q', line=3453)

W('4420', 0o00006, 'TPSL1', 'EXTEND', '', 'SHIFTS MPAC, +1, +2 LEFT 1', line=3455)
W('4421', 0o30156, '', 'DCA', 'MPAC +1', 'LEAVES OVFIND SET TO +/- 1 FOR OF/UF', line=3456)
W('4422', 0o20156, '', 'DAS', 'MPAC +1', line=3457)
W('4423', 0o60154, '', 'AD', 'MPAC', line=3458)
W('4424', 0o26154, '', 'ADS', 'MPAC', line=3459)
W('4425', 0o54007, '', 'TS', '7', 'TS A DOES NOT CHANGE A ON OF/UF.', line=3460)
W('4426', 0o00002, '', 'TC', 'Q', 'NO NET OF/UF', line=3461)
W('4427', 0o54162, '', 'TS', 'MPAC+6', 'MPAC +6 SET TO +/- 1 FOR OF/UF', line=3462)
W('4430', 0o00002, '', 'TC', 'Q', line=3463)

# IF MPAC, +1 ARE EACH +NZ OR +0 AND C(A)=-0, SHORTMP WRONGLY GIVES +0.
# IF MPAC, +1 ARE EACH -NZ OR -0 AND C(A)=+0, SHORTMP WRONGLY GIVES +0.
# PRSHRTMP FIXES FIRST CASE ONLY, BY MERELY TESTING C(A) AND IF IT = -0,
# SETTING RESULT TO -0.
#
# (DO NOT USE PRSHRTMP UNLESS MPAC, +1 ARE EACH +NZ OR +0, AS THEY ARE
# WHEN THEY CONTAIN THE SF CONSTANTS.)

W('4431', 0o54135, 'PRSHRTMP', 'TS', 'MPTEMP', line=3473)
W('4432', 0o10000, '', 'CCS', 'A', line=3474)
W('4433', 0o30135, '', 'CA', 'MPTEMP', 'C(A) +,  DO REGULAR SHORTMP', line=3475)
W('4434', 0o17257, '', 'TCF', 'SHORTMP +1', 'C(A) +0, DO REGULAR SHORTMP', line=3476)
W('4435', 0o14433, '', 'TCF', '-2', 'C(A) -,  DO REGULAR SHORTMP', line=3477)
W('4436', 0o45021, '', 'CS', 'ZERO', 'C(A) -0, FORCE RESULT TO -0 AND RETURN.', line=3478)
W('4437', 0o54154, '', 'TS', 'MPAC', line=3479)
W('4440', 0o54155, '', 'TS', 'MPAC +1', line=3480)
W('4441', 0o54156, '', 'TS', 'MPAC +2', line=3481)
W('4442', 0o00002, '', 'TC', 'Q', line=3482)

W('4443', 0o35012, 'FLASHON', 'CAF', 'BIT6', 'TURN ON V/N FLASH', line=3484)
W('4444', 0o00006, '', 'EXTEND', '', 'BIT 6 OF CHANNEL 11', line=3485)
W('4445', 0o05011, '', 'WOR', 'DSALMOUT', line=3486)
W('4446', 0o00002, '', 'TC', 'Q', line=3487)

W('4447', 0o45012, 'FLASHOFF', 'CS', 'BIT6', 'TURN OFF V/N FLASH', line=3489)
W('4450', 0o00006, '', 'EXTEND', line=3490)
W('4451', 0o03011, '', 'WAND', 'DSALMOUT', 'BIT 6 OF CHANNEL 11', line=3491)
W('4452', 0o00002, '', 'TC', 'Q', line=3492)

# Page 381
# INTERNAL USE OF KEYBOARD AND DISPLAY PROGRAM.
#
# USER MUST SCHEDULE CALLS TO NVSUB SO THAT THERE IS NO CONFLICT OF USE OR
# CONFUSION TO OPERATOR.  THE OLD CRABLOCK (INTERNAL/INTERNAL INTERLOCK)
# HAS BEEN REMOVED AND THE INTERNAL USER NO LONGER HAS THE PROTECTION THIS
# OFFERED.
#
# THERE ARE TWO WAYS A JOB CAN BE PUT TO SLEEP BY THE KEYBOARD + DISPLAY
# PROGRAM.      1)      BY ENDIDLE
# 2)      BY NVSUBUSY
# THE BASIC CONVENTION IS THAT ONLY ONE JOB WILL BE PERITTED ASLEEP VIA
# THE KEYBOARD + DISPLAY PROGRAM AT A TIME.  IF A JOB ATTEMPTS TO GO TO
# SLEEP BY MEANS OF (1) OR (2) AND THERE IS ALREADY AJOB ASLEEP THAT WAS
# PUT TO SLEEP BY (1) OR (2), THEN AN ABORT IS CAUSED.
#
# THE CALLING SEQUENCE FOR NVSUB IS
# CAF             V/N
# L               TC              NVSUB
# L+1             RETURN HERE IF OPERATOR HAS INTERVENED
# L+2             RETURN HERE AFTER EXECUTION
#
# A ROUTINE CALLED NVSUBUSY IS PROVIDED (USE IS OPTIONAL) TO PUT
# YOUR JOB TO SLEEP UNTIL THE OPERATOR RELEASES THE KEYBOARD + DISPLAY
# SYSTEM.  NVSUBUSY ALSO TURNS ON THE KEY RELEASE LIGHT.
# NVSUBUSY CANNOT BE CALLED FROM ERASABLE OR F/F MEMORY,
# SINCE JOBSLEEP AND JOBWAKE CAN HANDLE ONLY FIXED BANKS.
#
# THE CALLING SEQUENCE IS
# CAF     WAKEFCADR
# TC      NVSUBUSY
# .
#
# NVSUBUSY IS INTENDED FOR USE WHEN AN INTERNAL PROGRAM FINDS THE OPERATOR
# IS NOT USING THE KEYBOARD + DISPLAY PROGRAM (BY HIS OWN INITIATION).  IT IS
# NOT INTENDED FOR USE WHEN ONE INTERNAL PROGRAM FINDS ANOTHER INTERNAL
# PROGRAM USING THE KEYBOARD + DISPLAY PROGRAM.
#
# NVSUBUSY ABORTS (WITH CODE 01206) IF A SECOND JOB ATTEMPTS TO GO TO
# SLEEP IN PINBALL.  IN PARTICULAR, IF AN ATTEMPT IS MAKE TO GO TO NVSUBUSY
# WHEN
#
# 1)      DSPLIST NOT= +0.  THIS IS THE CASE WHERE THE CAPACITY FO THE DSPLIST
# IS EXCEEDED.
# 2)      CADRSTOR NOT= +0.  THIS INDICATES THAT A JOB IS ALREADY USING
# Page 382
# ENDIDLE.  (+-NZ INDICATES A JOB IS ALREADY ASLEEP DUE TO ENDIDLE.)

W('4453', 0o44460, 'PRENVBSY', 'CS', '2K+3', 'SPECIAL ENTRANCE FOR ROUTINES IN FIXED', line=3542)
W('4454', 0o60002, '', 'AD', 'Q', 'BANKS ONLY DESIRING THE FCADR OF (LOC', line=3543)
W('4455', 0o60004, '', 'AD', 'FBANK', 'FROM WHICH THE TC PRENVBSY WAS DONE) -2', line=3544)
W('4456', 0o04701, 'NVSUBUSY', 'TC', 'POSTJUMP', 'TO BE ENTERED.', line=3545)
W('4457', 0o10577, '', 'CADR', 'NVSUBSY1', kind='data', line=3546)
W('4460', 0o02003, '2K+3', 'OCT', '2003', kind='data', line=3547)

# NVSUBSY1 MUST BE IN BANK 27 OR LOWER, SO IT WILL PUT CALLER TO SLEEP
# WITH HIS PROPER SUPERBITS.

#   SETLOC ENDSPMM +1
#   COUNT 07/PIN

W('04,2577', 0o54001, 'NVSUBSY1', 'TS', 'L', line=3555)
W('04,2600', 0o04234, '', 'TC', 'ISCADR+0', 'ABORT IF CADRSTOR NOT= +0.', line=3556)
W('04,2601', 0o04240, '', 'TC', 'ISLIST+0', 'ABORT IF DSPLIST NOT= +0.', line=3557)
W('04,2602', 0o04410, '', 'TC', 'RELDSPON', line=3558)
W('04,2603', 0o30001, '', 'CA', 'L', line=3559)
W('04,2604', 0o55043, '', 'TS', 'DSPLIST', line=3560)
W('04,2605', 0o05175, 'ENDNVBSY', 'TC', 'JOBSLEEP', line=3561)

# NVSBWAIT IS A SPECIAL ENTRANCE FOR ROUTINES IN FIXED BANKS ONLY. IF
# SYSTEM IS NOT BUSY, IT EXECUTES V/N AND RETURNS TO L+1 (L= LOC FROM
# WHICH THE TC NVSBWAIT WAS DONE).  IF SYSTEM IS BUSY, IT PUTS CALLING JOB
# TO SLEEP WITH L-1 GOING INTO LIST FOR EVENTUAL WAKING UP WHEN SYSTEM
# IS NOT BUSY.

#   SETLOC NVSUBUSY +3
#   COUNT 02/PIN

W('4461', 0o22007, 'NVSBWAIT', 'LXCH', '7', 'ZERO NVMONOPT OPTIONS', line=3572)
W('4462', 0o54123, '', 'TS', 'NVTEMP', line=3573)
W('4463', 0o35002, '', 'CAF', 'BIT14', line=3574)
W('4464', 0o71021, '', 'MASK', 'MONSAVE1', 'EXTERNAL MONITOR BIT', line=3575)
W('4465', 0o61012, '', 'AD', 'DSPLOCK', line=3576)
W('4466', 0o10000, '', 'CCS', 'A', line=3577)
W('4467', 0o14471, '', 'TCF', 'NVSBWT1', 'BUSY', line=3578)
W('4470', 0o14200, '', 'TCF', 'NVSBCOM', 'FREE. NVSUB WILL SAVE L+1 FOR RETURN', line=3579)
# AFTER EXECUTION.
W('4471', 0o24002, 'NVSBWT1', 'INCR', 'Q', 'L+2.  PRENVBSY WILL PUT L-1 INTO LIST AND', line=3581)
W('4472', 0o14453, '', 'TCF', 'PRENVBSY', 'GO TO SLEEP.', line=3582)

# RELDSP IS USED BY VBPROC, VBTERM, VBRQEXEC, VBRQWAIT, VBRELDSP, EXTENDED
# VERB DISPATCHER, VBRESEQ, RECALTST.
#
# RELDSP1 IS USED BY MONITOR SET UP, VBRELDSP.

W('4473', 0o56002, 'RELDSP', 'XCH', 'Q', 'SET DSPLOCK TO +0, TURN RELDSP LIGHT', line=3589)
# Page 383
W('4474', 0o54144, '', 'TS', 'RELRET', 'OFF, SEARCH DSPLIST', line=3591)
W('4475', 0o45002, '', 'CS', 'BIT14', line=3592)
W('4476', 0o00004, '', 'INHINT', line=3593)
W('4477', 0o71021, '', 'MASK', 'MONSAVE1', line=3594)
W('4500', 0o55021, '', 'TS', 'MONSAVE1', 'TURN OFF EXTERNAL MONITOR BIT', line=3595)
W('4501', 0o11043, '', 'CCS', 'DSPLIST', line=3596)
W('4502', 0o04504, '', 'TC', '+2', line=3597)
W('4503', 0o04507, '', 'TC', 'RELDSP2', 'LIST EMPTY', line=3598)
W('4504', 0o35021, '', 'CAF', 'ZERO', line=3599)
W('4505', 0o57043, '', 'XCH', 'DSPLIST', line=3600)
W('4506', 0o05201, '', 'TC', 'JOBWAKE', line=3601)
W('4507', 0o00003, 'RELDSP2', 'RELINT', line=3602)
W('4510', 0o45013, '', 'CS', 'BIT5', 'TURN OFF KEY RELEASE LIGHT', line=3603)
W('4511', 0o00006, '', 'EXTEND', '', '(BIT 5 OF CHANNEL 11)', line=3604)
W('4512', 0o03011, '', 'WAND', 'DSALMOUT', line=3605)
W('4513', 0o35021, '', 'CAF', 'ZERO', line=3606)
W('4514', 0o55012, '', 'TS', 'DSPLOCK', line=3607)
W('4515', 0o00144, '', 'TC', 'RELRET', line=3608)
W('4516', 0o56002, 'RELDSP1', 'XCH', 'Q', 'SET DSPLOCK TO +0.  NO DSPLIST SEARCH.', line=3609)
W('4517', 0o54144, '', 'TS', 'RELRET', 'TURN KEY RLSE LIGHT OFF IF DSPLIST IS', line=3610)
# EMPTY.  LEAVE KEY RLSE LIGHT ALONE IF
# DSPLIST IS NOT EMPTY.
W('4520', 0o11043, '', 'CCS', 'DSPLIST', line=3613)
W('4521', 0o04523, '', 'TC', '+2', '+     NOT EMPTY.  LEAVE KEY RLSE LIGHT ALONE.', line=3614)
W('4522', 0o04507, '', 'TC', 'RELDSP2', '+0    EMPTY.  TURN OFF KEY RLSE LIGHT', line=3615)
W('4523', 0o35021, '', 'CAF', 'ZERO', '-     NOT EMPTY.  LEAVE KEY RLSE LIGHT ALONE', line=3616)
W('4524', 0o55012, '', 'TS', 'DSPLOCK', line=3617)
W('4525', 0o00144, '', 'TC', 'RELRET', line=3618)

S('ENDPINBF', 'equals', 0o4526, line=3620)

# Page 384
# PINTEST IS NEEDED FOR AUTO CHECK OF PINBALL.

S('PINTEST', 'equals', 0o116002, line=3625)

# Page 385
# VBTSTLTS TURNS ON ALL DISPLAY PANEL LIGHTS.  AFTER 5 SEC, IT TURNS
# OFF THE CAUTION AND STATUS LIGHTS.

#   SETLOC ENDNVSB1 +1

#   COUNT 41/PIN

W('41,3613', 0o04662, 'VBTSTLTS', 'TC', 'BANKCALL', line=3635)
W('41,3614', 0o66730, '', 'CADR', 'CHKPOOH', kind='data', line=3636)

W('41,3615', 0o00004, '', 'INHINT', line=3638)
W('41,3616', 0o45017, '', 'CS', 'BIT1', "SET BIT 1 OF IMODES33 SO IMUMON WON'T", line=3639)
W('41,3617', 0o71321, '', 'MASK', 'IMODES33', 'TURN OUT ANY LAMPS.', line=3640)
W('41,3620', 0o65017, '', 'AD', 'BIT1', line=3641)
W('41,3621', 0o55321, '', 'TS', 'IMODES33', line=3642)

W('41,3622', 0o33656, '', 'CAF', 'TSTCON1', 'TURN ON UPLINK ACTIVITY, TEMP, KEY RLSE,', line=3644)
W('41,3623', 0o00006, '', 'EXTEND', '', 'V/N FLASH, OPERATOR ERROR.', line=3645)
W('41,3624', 0o05011, '', 'WOR', 'DSALMOUT', line=3646)
W('41,3625', 0o33657, '', 'CAF', 'TSTCON2', 'TURN ON NO ATT, GIMBAL LOCK, TRACKER,', line=3647)
W('41,3626', 0o55036, '', 'TS', 'DSPTAB +11D', 'PROG ALM.', line=3648)
W('41,3627', 0o35006, '', 'CAF', 'BIT10', 'TURN ON TEST ALARM OUTBIT', line=3649)
W('41,3630', 0o00006, '', 'EXTEND', line=3650)
W('41,3631', 0o05013, '', 'WOR', 'CHAN13', line=3651)
W('41,3632', 0o34377, '', 'CAF', 'TEN', line=3652)
W('41,3633', 0o54117, 'TSTLTS1', 'TS', 'ERCNT', line=3653)
W('41,3634', 0o43654, '', 'CS', 'FULLDSP', line=3654)
W('41,3635', 0o50117, '', 'INDEX', 'ERCNT', line=3655)
W('41,3636', 0o55023, '', 'TS', 'DSPTAB', line=3656)
W('41,3637', 0o10117, '', 'CCS', 'ERCNT', line=3657)
W('41,3640', 0o03633, '', 'TC', 'TSTLTS1', line=3658)
W('41,3641', 0o43655, '', 'CS', 'FULLDSP1', line=3659)
W('41,3642', 0o55024, '', 'TS', 'DSPTAB +1', 'TURN ON 3 PLUS SIGNS', line=3660)
W('41,3643', 0o55027, '', 'TS', 'DSPTAB +4', line=3661)
W('41,3644', 0o55031, '', 'TS', 'DSPTAB +6', line=3662)
W('41,3645', 0o35024, '', 'CAF', 'ELEVEN', line=3663)
W('41,3646', 0o55016, '', 'TS', 'NOUT', line=3664)
W('41,3647', 0o33661, '', 'CAF', 'SHOLTS', line=3665)
W('41,3650', 0o05245, '', 'TC', 'WAITLIST', line=3666)
#   EBANK= DSPTAB
W('41,3651', 0o03662, '', '2CADR', 'TSTLTS2', kind='data', line=3668)
W('41,3652', 0o62102, kind='data', line=3668)

W('41,3653', 0o05217, '', 'TC', 'ENDOFJOB', 'DSPLOCK IS LEFT BUSY (FROM KEYBOARD', line=3670)
# ACTION) UNTIL TSTLTS3 TO INSURE THAT
# LIGHTS TEST WILL BE SEEN.

W('41,3654', 0o05675, 'FULLDSP', 'OCT', '05675', "DISPLAY ALL 8'S", kind='data', line=3674)
W('41,3655', 0o07675, 'FULLDSP1', 'OCT', '07675', "DISPLAY ALL 8'S AND +", kind='data', line=3675)
W('41,3656', 0o00175, 'TSTCON1', 'OCT', '00175', kind='data', line=3676)
# Page 386
# UPLINK ACTIVITY, TEMP, KEY RLSE,
# V/N FLASH, OPERATOR ERROR.
W('41,3657', 0o40650, 'TSTCON2', 'OCT', '40650', 'DSPTAB+11D BITS 4,6,8,9,', kind='data', line=3680)
# NO ATT, GIMBAL LOCK, TRACKER, PROG ALM.
W('41,3660', 0o00115, 'TSTCON3', 'OCT', '00115', 'CHAN 11 BITS 1, 3, 4, 7.', kind='data', line=3682)
# UPLINK ACITIVY, TEMP, OPERATOR ERROR.
W('41,3661', 0o00764, 'SHOLTS', 'OCT', '764', '5 SEC', kind='data', line=3684)

W('41,3662', 0o34371, 'TSTLTS2', 'CAF', 'CHRPRIO', 'CALLED BY WAITLIST', line=3686)
W('41,3663', 0o05134, '', 'TC', 'NOVAC', line=3687)
#   EBANK= DSPTAB
W('41,3664', 0o03667, '', '2CADR', 'TSTLTS3', kind='data', line=3689)
W('41,3665', 0o62102, kind='data', line=3689)

W('41,3666', 0o05324, '', 'TC', 'TASKOVER', line=3691)

W('41,3667', 0o43660, 'TSTLTS3', 'CS', 'TSTCON3', 'CALLED BY EXECUTIVE', line=3693)
W('41,3670', 0o00004, '', 'INHINT', line=3694)
W('41,3671', 0o00006, '', 'EXTEND', '', 'TURN OFF UPLINK ACTIVITY, TEMP,', line=3695)
W('41,3672', 0o03011, '', 'WAND', 'DSALMOUT', 'OPERATOR ERROR.', line=3696)
W('41,3673', 0o45006, '', 'CS', 'BIT10', 'TURN OFF TEST ALARM OUTBIT', line=3697)
W('41,3674', 0o00006, '', 'EXTEND', line=3698)
W('41,3675', 0o03013, '', 'WAND', 'CHAN13', line=3699)
W('41,3676', 0o35014, '', 'CAF', 'BIT4', 'MAKE NO ATT FOLLOW BIT 4 OF CHANNEL 12', line=3700)
W('41,3677', 0o00006, '', 'EXTEND', '', '      (NO TT LIGHT ON IF IN COARSE ALIGN)', line=3701)
W('41,3700', 0o02012, '', 'RAND', 'CHAN12', line=3702)
W('41,3701', 0o65001, '', 'AD', 'BIT15', 'TURN OFF AUTO, HOLD, FREE, SPARE,', line=3703)
W('41,3702', 0o55036, '', 'TS', 'DSPTAB +11D', 'GIMBAL LOCK, SPARE, TRACKER, PROG ALM', line=3704)
W('41,3703', 0o43725, '', 'CS', '13-11,1', 'SET BITS TO INDICATE ALL LAMPS OUT. TEST', line=3705)
W('41,3704', 0o71321, '', 'MASK', 'IMODES33', 'LIGHTS COMPLETE.', line=3706)
W('41,3705', 0o65070, '', 'AD', 'PRIO16', line=3707)
W('41,3706', 0o55321, '', 'TS', 'IMODES33', line=3708)

W('41,3707', 0o43726, '', 'CS', 'OCT55000', line=3710)
W('41,3710', 0o71320, '', 'MASK', 'IMODES30', line=3711)
W('41,3711', 0o65067, '', 'AD', 'PRIO15', '15000.', line=3712)
W('41,3712', 0o55320, '', 'TS', 'IMODES30', line=3713)

W('41,3713', 0o41331, '', 'CS', 'OPTMODES', line=3715)
W('41,3714', 0o75011, '', 'MASK', 'BIT7', line=3716)
W('41,3715', 0o27331, '', 'ADS', 'OPTMODES', line=3717)
W('41,3716', 0o00003, '', 'RELINT', line=3718)

W('41,3717', 0o04662, '', 'TC', 'BANKCALL', 'REDISPLAY C(MODREG)', line=3720)
W('41,3720', 0o10566, '', 'CADR', 'DSPMM', kind='data', line=3721)
W('41,3721', 0o04220, '', 'TC', 'KILMONON', 'TURN ON KILL MONITOR BIT.', line=3722)
W('41,3722', 0o04447, '', 'TC', 'FLASHOFF', 'TURN OFF V/N FLASH.', line=3723)
W('41,3723', 0o04701, '', 'TC', 'POSTJUMP', 'DOES RELDSP AND GOES TO PINBRNCH IF', line=3724)
W('41,3724', 0o61376, '', 'CADR', 'TSTLTS4', 'ENDIDLE IS AWAITING OPERATOR RESPONSE.', kind='data', line=3725)
# Page 387
W('41,3725', 0o16001, '13-11,1', 'OCT', '16001', kind='data', line=3727)
W('41,3726', 0o55000, 'OCT55000', 'OCT', '55000', kind='data', line=3728)
S('ENDPINS2', 'equals', 0o113727, line=3729)

# Page 388
# ERROR LIGHT RESET (RSET) TURNS OFF:
# UPLINK ACTIVITY, AUTO, HOLD, FREE, OPERATOR ERROR,
# PROG ALM, TRACKER FAIL.
#
# LEAVES GIMBAL LOCK AND NO ATT ALONE.
#
# IT ALSO ZEROS THE `TEST ALARM' OUT BIT, WHICH TURNS OFF STBY, RESTART.
# IT ALSO SETS `CAUTION RESET' TO 1.
# IT ALSO FORCES BIT 12 OF ALL DSPTAB ENTRIES TO 1.

#   SETLOC DOPROC +2
#   COUNT 40/PIN

W('40,3510', 0o56115, 'ERROR', 'XCH', '21/22REG', 'RESTORE ORIGINAL C(DSPLOCK).  THUS ERROR', line=3745)
W('40,3511', 0o55012, '', 'TS', 'DSPLOCK', 'LIGHT RESET LEAVES DSPLOCK CHANGED.', line=3746)
W('40,3512', 0o00004, '', 'INHINT', line=3747)
W('40,3513', 0o35006, '', 'CAF', 'BIT10', "TURN ON `CAUTION RESET' OUTBIT", line=3748)
W('40,3514', 0o00006, '', 'EXTEND', line=3749)
W('40,3515', 0o05011, '', 'WOR', 'DSALMOUT', 'BIT10 CHAN 11', line=3750)
W('40,3516', 0o33576, '', 'CAF', 'GL+NOATT', 'LEAVE GIMBAL LOCK AND NO ATT INTACT,', line=3751)
W('40,3517', 0o71036, '', 'MASK', 'DSPTAB +11D', 'TURNING OFF AUTO, HOLD, FREE,', line=3752)
W('40,3520', 0o65001, '', 'AD', 'BIT15', 'PROG ALARM, AND TRACKER.', line=3753)
W('40,3521', 0o55036, '', 'TS', 'DSPTAB +11D', line=3754)
W('40,3522', 0o45070, '', 'CS', 'PRIO16', 'RESET FAIL BITS WHICH GENERATE PROG', line=3755)
W('40,3523', 0o71321, '', 'MASK', 'IMODES33', 'ALARM SO THAT IF THE FAILURE STILL', line=3756)
W('40,3524', 0o65070, '', 'AD', 'PRIO16', 'EXISTS, THE ALARM WILL COME BACK.', line=3757)
W('40,3525', 0o55321, '', 'TS', 'IMODES33', line=3758)
W('40,3526', 0o45006, '', 'CS', 'BIT10', line=3759)
W('40,3527', 0o71320, '', 'MASK', 'IMODES30', line=3760)
W('40,3530', 0o65006, '', 'AD', 'BIT10', line=3761)
W('40,3531', 0o55320, '', 'TS', 'IMODES30', line=3762)

W('40,3532', 0o41331, '', 'CS', 'OPTMODES', line=3764)
W('40,3533', 0o75011, '', 'MASK', 'BIT7', line=3765)
W('40,3534', 0o27331, '', 'ADS', 'OPTMODES', line=3766)
W('40,3535', 0o45006, '', 'CS', 'BIT10', "TURN OFF 'TEST ALARM' OUTBIT", line=3767)
W('40,3536', 0o00006, '', 'EXTEND', line=3768)
W('40,3537', 0o03013, '', 'WAND', 'CHAN13', line=3769)
W('40,3540', 0o43574, '', 'CS', 'ERCON', 'TURN OFF UPLINK ACTIVITY,', line=3770)
W('40,3541', 0o00006, '', 'EXTEND', '', 'OPERATOR ERROR.', line=3771)
W('40,3542', 0o03011, '', 'WAND', 'DSALMOUT', line=3772)
W('40,3543', 0o34377, 'TSTAB', 'CAF', 'BINCON', '(DEC 10)', line=3773)
W('40,3544', 0o54117, '', 'TS', 'ERCNT', 'ERCNT = COUNT', line=3774)
W('40,3545', 0o00004, '', 'INHINT', line=3775)
W('40,3546', 0o50117, '', 'INDEX', 'ERCNT', line=3776)
W('40,3547', 0o11023, '', 'CCS', 'DSPTAB', line=3777)
W('40,3550', 0o65017, '', 'AD', 'ONE', line=3778)
W('40,3551', 0o03556, '', 'TC', 'ERPLUS', line=3779)
W('40,3552', 0o65017, '', 'AD', 'ONE', line=3780)
W('40,3553', 0o40000, 'ERMINUS', 'CS', 'A', line=3781)
W('40,3554', 0o73577, '', 'MASK', 'NOTBIT12', line=3782)
W('40,3555', 0o03561, '', 'TC', 'ERCOM', line=3783)
# Page 389
W('40,3556', 0o40000, 'ERPLUS', 'CS', 'A', line=3785)
W('40,3557', 0o73577, '', 'MASK', 'NOTBIT12', line=3786)
W('40,3560', 0o40000, '', 'CS', 'A', 'MIGHT WANT TO RESET CLPASS, DECBRNCH,', line=3787)
W('40,3561', 0o50117, 'ERCOM', 'INDEX', 'ERCNT', 'ETC.', line=3788)
W('40,3562', 0o55023, '', 'TS', 'DSPTAB', line=3789)
W('40,3563', 0o00003, '', 'RELINT', line=3790)
W('40,3564', 0o10117, '', 'CCS', 'ERCNT', line=3791)
W('40,3565', 0o03544, '', 'TC', 'TSTAB +1', line=3792)
W('40,3566', 0o35021, '', 'CAF', 'ZERO', line=3793)
W('40,3567', 0o54375, '', 'TS', 'FAILREG', line=3794)
W('40,3570', 0o54376, '', 'TS', 'FAILREG +1', line=3795)
W('40,3571', 0o54377, '', 'TS', 'FAILREG +2', line=3796)
W('40,3572', 0o55357, '', 'TS', 'SFAIL', line=3797)
W('40,3573', 0o05217, '', 'TC', 'ENDOFJOB', line=3798)

W('40,3574', 0o00104, 'ERCON', 'OCT', '104', 'CHAN 11 BITS 3,7.', kind='data', line=3800)
# UPLINK ACTIVITY, AND OPERATOR ERROR.
W('40,3575', 0o00240, 'BITS6,8', 'OCT', '240', kind='data', line=3802)
W('40,3576', 0o00050, 'GL+NOATT', 'OCT', '00050', 'NO ATT AND GIMBAL LOCK LAMPS', kind='data', line=3803)
W('40,3577', 0o73777, 'NOTBIT12', 'OCT', '73777', kind='data', line=3804)

S('ENDPINS1', 'equals', 0o111600, line=3806)

#   SBANK= LOWSUPER
