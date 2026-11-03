"""EXECUTIVE.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/EXECUTIVE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1208-1220 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('EXECUTIVE', 'EXECUTIVE.agc', 'Comanche055', pages='1208-1220')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     EXECUTIVE.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1208-1220
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

# Page 1208
#   BLOCK 02

# TO ENTER A JOB REQUEST REQUIRING NO VAC AREA:

#   COUNT 02/EXEC

W('5134', 0o00004, 'NOVAC', 'INHINT', line=37)
W('5135', 0o65226, '', 'AD', 'FAKEPRET', 'LOC(MPAC +6) - LOC(QPRET)', line=38)
W('5136', 0o54063, '', 'TS', 'NEWPRIO', 'PRIORITY OF NEW JOB + NOVAC C(FIXLOC)', line=39)

W('5137', 0o00006, '', 'EXTEND', line=41)
W('5140', 0o50002, '', 'INDEX', 'Q', 'Q WILL BE UNDISTURBED THROUGHOUT.', line=42)
W('5141', 0o30001, '', 'DCA', '0', '2CADR OF JOB ENTERED.', line=43)
W('5142', 0o52066, '', 'DXCH', 'NEWLOC', line=44)
W('5143', 0o35225, '', 'CAF', 'EXECBANK', line=45)
W('5144', 0o56004, '', 'XCH', 'FBANK', line=46)
W('5145', 0o54061, '', 'TS', 'EXECTEM1', line=47)
W('5146', 0o12650, '', 'TCF', 'NOVAC2', 'ENTER EXECUTIVE BANK.', line=48)

# TO ENTER A JOB REQUEST REQUIRING A VAC AREA - E.G., ALL (PARTIALLY) INTERPRETIVE JOBS.

W('5147', 0o00004, 'FINDVAC', 'INHINT', line=52)
W('5150', 0o54063, '', 'TS', 'NEWPRIO', line=53)
W('5151', 0o00006, '', 'EXTEND', line=54)
W('5152', 0o50002, '', 'INDEX', 'Q', line=55)
W('5153', 0o30001, '', 'DCA', '0', line=56)
W('5154', 0o52066, 'SPVACIN', 'DXCH', 'NEWLOC', line=57)
W('5155', 0o35225, '', 'CAF', 'EXECBANK', line=58)
W('5156', 0o56004, '', 'XCH', 'FBANK', line=59)
W('5157', 0o12626, '', 'TCF', 'FINDVAC2', 'OFF TO EXECUTIVE SWITCHED-BANK.', line=60)

# TO ENTER A FINDVAC WITH THE PRIORITY IN NEWPRIO TO THE 2CADR ARRIVING IN A AND L:
# USERS OF SPVAC MUST INHINT BEFORE STORING IN NEWPRIO.

W('5160', 0o56002, 'SPVAC', 'XCH', 'Q', line=65)
W('5161', 0o67715, '', 'AD', 'NEG2', line=66)
W('5162', 0o56002, '', 'XCH', 'Q', line=67)
W('5163', 0o15154, '', 'TCF', 'SPVACIN', line=68)

# TO SUSPEND A BASIC JOB SO A HIGHER PRIORITY JOB MAY BE SERVICED:

W('5164', 0o22002, 'CHANG1', 'LXCH', 'Q', line=72)
W('5165', 0o35225, '', 'CAF', 'EXECBANK', line=73)
W('5166', 0o56006, '', 'XCH', 'BBANK', line=74)
W('5167', 0o12727, '', 'TCF', 'CHANJOB', line=75)

# TO SUSPEND AN INTERPRETIVE JOB:

W('5170', 0o40164, 'CHANG2', 'CS', 'LOC', 'NEGATIVE LOC SHOWS JOB = INTERPRETIVE.', line=79)
# ITRACE (4) REFERS TO "CHANG2".
# Page 1209
W('5171', 0o54001, '', 'TS', 'L', line=82)
W('5172', 0o35225, '', 'CAF', 'EXECBANK', line=83)
W('5173', 0o54006, '', 'TS', 'BBANK', line=84)
W('5174', 0o12726, '', 'TCF', 'CHANJOB -1', line=85)

# Page 1210
# TO VOLUNTARILY SUSPEND A JOB UNTIL THE COMPLETION OF SOME ANTICIPATED EVENT (I/O EVENT ETC.):

W('5175', 0o54164, 'JOBSLEEP', 'TS', 'LOC', line=90)
W('5176', 0o35225, '', 'CAF', 'EXECBANK', line=91)
W('5177', 0o54004, '', 'TS', 'FBANK', line=92)
W('5200', 0o13017, '', 'TCF', 'JOBSLP1', line=93)

# TO AWAKEN A JOB PUT TO SLEEP IN THE ABOVE FASHION:

W('5201', 0o00004, 'JOBWAKE', 'INHINT', line=97)
W('5202', 0o54065, '', 'TS', 'NEWLOC', line=98)
W('5203', 0o45016, '', 'CS', 'TWO', 'EXIT IS VIA FINDVAC/NOVAC PROCEDURES.', line=99)
W('5204', 0o26002, '', 'ADS', 'Q', line=100)
W('5205', 0o35225, '', 'CAF', 'EXECBANK', line=101)
W('5206', 0o56004, '', 'XCH', 'FBANK', line=102)
W('5207', 0o13044, '', 'TCF', 'JOBWAKE2', line=103)

# TO CHANGE THE PRIORITY OF A JOB CURRENTLY UNDER EXECUTION:

W('5210', 0o00004, 'PRIOCHNG', 'INHINT', '', 'NEW PRIORITY ARRIVES IN A. RETURNS TO', line=107)
W('5211', 0o54063, '', 'TS', 'NEWPRIO', 'CALLER AS SOON AS NEW JOB PRIORITY IS', line=108)
W('5212', 0o35225, '', 'CAF', 'EXECBANK', 'HIGHEST. PREPARE FOR POSSIBLE BASIC-', line=109)
W('5213', 0o56006, '', 'XCH', 'BBANK', 'STYLE CHANGE-JOB.', line=110)
W('5214', 0o54165, '', 'TS', 'BANKSET', line=111)
W('5215', 0o30002, '', 'CA', 'Q', line=112)
W('5216', 0o13113, '', 'TCF', 'PRIOCH2', line=113)

# TO REMOVE A JOB FROM EXECUTIVE CONSIDERATIONS:

W('5217', 0o35225, 'ENDOFJOB', 'CAF', 'EXECBANK', line=117)
W('5220', 0o54004, '', 'TS', 'FBANK', line=118)
W('5221', 0o13124, '', 'TCF', 'ENDJOB1', line=119)

W('5222', 0o30061, 'ENDFIND', 'CA', 'EXECTEM1', 'RETURN TO CALLER AFTER JOB ENTRY', line=121)
W('5223', 0o54004, '', 'TS', 'FBANK', 'COMPLETE.', line=122)
W('5224', 0o16710, '', 'TCF', 'Q+2', line=123)
W('5225', 0o02626, 'EXECBANK', 'CADR', 'FINDVAC2', kind='data', line=124)

W('5226', 0o00110, 'FAKEPRET', 'ADRES', 'MPAC -36D', 'LOC(MPAC +6) - LOC(QPRET)', kind='data', line=126)

# Page 1211
# LOCATE AN AVAILABLE VAC AREA.

#   BANK 01
#   COUNT 01/EXEC

W('01,2626', 0o54061, 'FINDVAC2', 'TS', 'EXECTEM1', "(SAVE CALLER'S BANK FIRST.)", line=134)
W('01,2627', 0o10400, '', 'CCS', 'VAC1USE', line=135)
W('01,2630', 0o12643, '', 'TCF', 'VACFOUND', line=136)
W('01,2631', 0o10454, '', 'CCS', 'VAC2USE', line=137)
W('01,2632', 0o12643, '', 'TCF', 'VACFOUND', line=138)
W('01,2633', 0o10530, '', 'CCS', 'VAC3USE', line=139)
W('01,2634', 0o12643, '', 'TCF', 'VACFOUND', line=140)
W('01,2635', 0o10604, '', 'CCS', 'VAC4USE', line=141)
W('01,2636', 0o12643, '', 'TCF', 'VACFOUND', line=142)
W('01,2637', 0o10660, '', 'CCS', 'VAC5USE', line=143)
W('01,2640', 0o12643, '', 'TCF', 'VACFOUND', line=144)
W('01,2641', 0o07755, '', 'TC', 'BAILOUT', line=145)
W('01,2642', 0o01201, '', 'OCT', '1201', 'NO VAC AREAS.', kind='data', line=146)

W('01,2643', 0o65016, 'VACFOUND', 'AD', 'TWO', 'RESERVE THIS VAC AREA BY STORING A ZERO', line=148)
W('01,2644', 0o22007, '', 'ZL', '', 'IN ITS VAC USE REGISTER AND STORE THE', line=149)
W('01,2645', 0o50000, '', 'INDEX', 'A', 'ADDRESS OF THE FIRST WORD OF IT IN THE', line=150)
W('01,2646', 0o21777, '', 'LXCH', '0 -1', 'LOW NINE BITS OF THE PRIORITY WORD.', line=151)
W('01,2647', 0o26063, '', 'ADS', 'NEWPRIO', line=152)

W('01,2650', 0o35021, 'NOVAC2', 'CAF', 'ZERO', 'NOVAC ENTERS HERE. FIND A CORE SET.', line=154)
W('01,2651', 0o54064, '', 'TS', 'LOCCTR', line=155)
W('01,2652', 0o32657, '', 'CAF', 'NO.CORES', 'SEVEN SETS OF ELEVEN REGISTERS EACH.', line=156)
W('01,2653', 0o54062, 'NOVAC3', 'TS', 'EXECTEM2', line=157)
W('01,2654', 0o50064, '', 'INDEX', 'LOCCTR', line=158)
W('01,2655', 0o10167, '', 'CCS', 'PRIORITY', 'EACH PRIORITY REGISTER CONTAINS -0 IF', line=159)
W('01,2656', 0o12717, '', 'TCF', 'NEXTCORE', 'THE CORRESPONDING CORE SET IS AVAILABLE.', line=160)
W('01,2657', 0o00006, 'NO.CORES', 'DEC', '6', kind='data', line=161)
W('01,2660', 0o12717, '', 'TCF', 'NEXTCORE', 'AN ACTIVE JOB HAS A POSITIVE PRIORITY', line=162)
# BUT A DORMANT JOB'S PRIORITY IS NEGATIVE

# Page 1212
W('01,2661', 0o30063, 'CORFOUND', 'CA', 'NEWPRIO', 'SET THE PRIORITY OF THIS JOB IN THE CORE', line=166)
W('01,2662', 0o50064, '', 'INDEX', 'LOCCTR', "SET'S PRIORITY REGISTER AND SET THE", line=167)
W('01,2663', 0o54167, '', 'TS', 'PRIORITY', "JOB'S PUSH-DOWN POINTER AT THE BEGINNING", line=168)
W('01,2664', 0o75046, '', 'MASK', 'LOW9', 'OF THE WORK AREA AND OVERFLOW INDICATOR', line=169)
W('01,2665', 0o50064, '', 'INDEX', 'LOCCTR', line=170)
W('01,2666', 0o54166, '', 'TS', 'PUSHLOC', 'OFF TO PREPARE FOR INTERPRETIVE PROGRAMS', line=171)

W('01,2667', 0o10064, '', 'CCS', 'LOCCTR', 'IF CORE SET ZERO IS BEING LOADED, SET UP', line=173)
W('01,2670', 0o12704, '', 'TCF', 'SETLOC', 'OVFIND AND FIXLOC IMMEDIATELY.', line=174)
W('01,2671', 0o54121, '', 'TS', 'OVFIND', line=175)
W('01,2672', 0o30166, '', 'CA', 'PUSHLOC', line=176)
W('01,2673', 0o54120, '', 'TS', 'FIXLOC', line=177)

W('01,2674', 0o10067, 'SPECTEST', 'CCS', 'NEWJOB', 'SEE IF ANY ACTIVE JOBS WAITING (RARE).', line=179)
W('01,2675', 0o12704, '', 'TCF', 'SETLOC', 'MUST BE AWAKENED BUT UNCHANGED JOB.', line=180)
W('01,2676', 0o05747, '', 'TC', 'CCSHOLE', line=181)
W('01,2677', 0o05747, '', 'TC', 'CCSHOLE', line=182)
W('01,2700', 0o54067, '', 'TS', 'NEWJOB', '+0 SHOWS ACTIVE JOB ALREADY SET.', line=183)
W('01,2701', 0o52066, '', 'DXCH', 'NEWLOC', line=184)
W('01,2702', 0o52165, '', 'DXCH', 'LOC', line=185)
W('01,2703', 0o15222, '', 'TCF', 'ENDFIND', line=186)

W('01,2704', 0o52066, 'SETLOC', 'DXCH', 'NEWLOC', 'SET UP THE LOCATION REGISTERS FOR THIS', line=188)
W('01,2705', 0o50064, '', 'INDEX', 'LOCCTR', line=189)
W('01,2706', 0o52165, '', 'DXCH', 'LOC', line=190)
W('01,2707', 0o50067, '', 'INDEX', 'NEWJOB', 'THIS INDEX INSTRUCTION INSURES THAT THE', line=191)
W('01,2710', 0o40167, '', 'CS', 'PRIORITY', 'HIGHEST ACTIVE PRIORITY WILL BE COMPARED', line=192)
W('01,2711', 0o60063, '', 'AD', 'NEWPRIO', 'WITH THE NEW PRIORITY TO SEE IF NEWJOB', line=193)
W('01,2712', 0o00006, '', 'EXTEND', '', 'SHOULD BE SET TO SIGNAL A SWITCH.', line=194)
W('01,2713', 0o65222, '', 'BZMF', 'ENDFIND', line=195)
W('01,2714', 0o30064, '', 'CA', 'LOCCTR', 'LOCCTR IS LEFT SET AT THIS CORE SET IF', line=196)
W('01,2715', 0o54067, '', 'TS', 'NEWJOB', 'THE CALLER WANTS TO LOAD ANY MPAC', line=197)
W('01,2716', 0o15222, '', 'TCF', 'ENDFIND', 'REGISTERS, ETC.', line=198)

W('01,2717', 0o33054, 'NEXTCORE', 'CAF', 'COREINC', line=200)
W('01,2720', 0o26064, '', 'ADS', 'LOCCTR', line=201)
W('01,2721', 0o10062, '', 'CCS', 'EXECTEM2', line=202)
W('01,2722', 0o12653, '', 'TCF', 'NOVAC3', line=203)
W('01,2723', 0o07755, '', 'TC', 'BAILOUT', 'NO CORE SETS.', line=204)
W('01,2724', 0o01202, '', 'OCT', '1202', kind='data', line=205)
# Page 1213
# THE FOLLOWING ROUTINE SWAPS CORE SET 0 WITH THAT WHOSE RELATIVE ADDRESS IS IN NEWJOB.

W('01,2725', 0o22164, '', 'LXCH', 'LOC', line=209)
W('01,2726', 0o30165, '', 'CAE', 'BANKSET', 'BANKSET, NOT BBANK, HAS RIGHT CONTENTS.', line=210)
W('01,2727', 0o00004, 'CHANJOB', 'INHINT', line=211)
W('01,2730', 0o00006, '', 'EXTEND', line=212)
W('01,2731', 0o04007, '', 'ROR', 'SUPERBNK', 'PICK UP CURRENT SBANK FOR BBCON', line=213)
W('01,2732', 0o56001, '', 'XCH', 'L', 'LOC IN A AND BBCON IN L.', line=214)
W('01,2733', 0o50067, '', 'INDEX', 'NEWJOB', 'SWAP LOC AND BANKSET.', line=215)
W('01,2734', 0o52165, '', 'DXCH', 'LOC', line=216)
W('01,2735', 0o52165, '', 'DXCH', 'LOC', line=217)

W('01,2736', 0o30165, '', 'CAE', 'BANKSET', line=219)
W('01,2737', 0o00006, '', 'EXTEND', line=220)
W('01,2740', 0o01007, '', 'WRITE', 'SUPERBNK', 'SET SBANK FOR NEW JOB.', line=221)
W('01,2741', 0o52155, '', 'DXCH', 'MPAC', 'SWAP MULTI-PURPOSE ACCUMULATOR AREAS.', line=222)
W('01,2742', 0o50067, '', 'INDEX', 'NEWJOB', line=223)
W('01,2743', 0o52155, '', 'DXCH', 'MPAC', line=224)
W('01,2744', 0o52155, '', 'DXCH', 'MPAC', line=225)
W('01,2745', 0o52157, '', 'DXCH', 'MPAC +2', line=226)
W('01,2746', 0o50067, '', 'INDEX', 'NEWJOB', line=227)
W('01,2747', 0o52157, '', 'DXCH', 'MPAC +2', line=228)
W('01,2750', 0o52157, '', 'DXCH', 'MPAC +2', line=229)
W('01,2751', 0o52161, '', 'DXCH', 'MPAC +4', line=230)
W('01,2752', 0o50067, '', 'INDEX', 'NEWJOB', line=231)
W('01,2753', 0o52161, '', 'DXCH', 'MPAC +4', line=232)
W('01,2754', 0o52161, '', 'DXCH', 'MPAC +4', line=233)
W('01,2755', 0o52163, '', 'DXCH', 'MPAC +6', line=234)
W('01,2756', 0o50067, '', 'INDEX', 'NEWJOB', line=235)
W('01,2757', 0o52163, '', 'DXCH', 'MPAC +6', line=236)
W('01,2760', 0o52163, '', 'DXCH', 'MPAC +6', line=237)

W('01,2761', 0o35021, '', 'CAF', 'ZERO', line=239)
W('01,2762', 0o56121, '', 'XCH', 'OVFIND', 'MAKE PUSHLOC NEGATIVE IF OVFIND NZ.', line=240)
W('01,2763', 0o00006, '', 'EXTEND', line=241)
W('01,2764', 0o12767, '', 'BZF', '+3', line=242)
W('01,2765', 0o40166, '', 'CS', 'PUSHLOC', line=243)
W('01,2766', 0o54166, '', 'TS', 'PUSHLOC', line=244)

W('01,2767', 0o52167, '', 'DXCH', 'PUSHLOC', line=246)
W('01,2770', 0o50067, '', 'INDEX', 'NEWJOB', line=247)
W('01,2771', 0o52167, '', 'DXCH', 'PUSHLOC', line=248)
W('01,2772', 0o52167, '', 'DXCH', 'PUSHLOC', 'SWAPS PUSHLOC AND PRIORITY.', line=249)
W('01,2773', 0o35046, '', 'CAF', 'LOW9', 'SET FIXLOC TO BASE OF VAC AREA.', line=250)
W('01,2774', 0o70167, '', 'MASK', 'PRIORITY', line=251)
W('01,2775', 0o54120, '', 'TS', 'FIXLOC', line=252)

W('01,2776', 0o10166, '', 'CCS', 'PUSHLOC', 'SET OVERFLOW INDICATOR ACCORDING TO', line=254)
W('01,2777', 0o35021, '', 'CAF', 'ZERO', line=255)
W('01,3000', 0o13005, '', 'TCF', 'ENDPRCHG -1', line=256)

# Page 1214
W('01,3001', 0o40166, '', 'CS', 'PUSHLOC', line=259)
W('01,3002', 0o54166, '', 'TS', 'PUSHLOC', line=260)
W('01,3003', 0o35017, '', 'CAF', 'ONE', line=261)
W('01,3004', 0o56121, '', 'XCH', 'OVFIND', line=262)
W('01,3005', 0o54067, '', 'TS', 'NEWJOB', line=263)

W('01,3006', 0o00003, 'ENDPRCHG', 'RELINT', line=265)
W('01,3007', 0o52165, '', 'DXCH', 'LOC', 'BASIC JOBS HAVE POSITIVE ADDRESSES, SO', line=266)
W('01,3010', 0o00006, '', 'EXTEND', '', 'DISPATCH WITH A DTCB.', line=267)
W('01,3011', 0o63013, '', 'BZMF', '+2', 'IF INTERPRETIVE, SET UP EBANK, ETC.', line=268)
W('01,3012', 0o52006, '', 'DTCB', line=269)
# Page 1215
W('01,3013', 0o40000, '', 'COM', '', 'EPILOGUE TO JOB CHANGE FOR INTERPRETIVE', line=271)
W('01,3014', 0o65017, '', 'AD', 'ONE', line=272)
W('01,3015', 0o54164, '', 'TS', 'LOC', 'RESUME.', line=273)
W('01,3016', 0o16017, '', 'TCF', 'INTRSM', line=274)

# COMPLETE JOBSLEEP PREPARATIONS.

W('01,3017', 0o00004, 'JOBSLP1', 'INHINT', line=278)
W('01,3020', 0o40167, '', 'CS', 'PRIORITY', 'NNZ PRIORITY SHOWS JOB ASLEEP.', line=279)
W('01,3021', 0o54167, '', 'TS', 'PRIORITY', line=280)
W('01,3022', 0o36043, '', 'CAF', 'LOW7', line=281)
W('01,3023', 0o70006, '', 'MASK', 'BBANK', line=282)
W('01,3024', 0o00006, '', 'EXTEND', line=283)
W('01,3025', 0o04007, '', 'ROR', 'SUPERBNK', 'SAVE OLD SUPERBANK VALUE.', line=284)
W('01,3026', 0o54165, '', 'TS', 'BANKSET', line=285)
W('01,3027', 0o45021, '', 'CS', 'ZERO', line=286)
W('01,3030', 0o54131, 'JOBSLP2', 'TS', 'BUF +1', 'HOLDS - HIGHEST PRIORITY.', line=287)
W('01,3031', 0o13141, '', 'TCF', 'EJSCAN', 'SCAN FOR HIGHEST PRIORITY ALA ENDOFJOB.', line=288)

W('01,3032', 0o00004, 'NUCHANG2', 'INHINT', '', 'QUICK... DONT LET NEWJOB CHANGE TO +0 .', line=290)
W('01,3033', 0o10067, '', 'CCS', 'NEWJOB', line=291)
W('01,3034', 0o13037, '', 'TCF', '+3', 'NEWJOB STILL PNZ', line=292)
W('01,3035', 0o00003, '', 'RELINT', '', 'NEWJOB HAS CHANGED TO +0. WAKE UP JOB', line=293)
W('01,3036', 0o13233, '', 'TCF', 'ADVAN +2', 'VIA NUDIRECT.  (VERY RARE CASE.)', line=294)

W('01,3037', 0o35016, '', 'CAF', 'TWO', line=296)
W('01,3040', 0o00006, '', 'EXTEND', line=297)
W('01,3041', 0o05011, '', 'WOR', 'DSALMOUT', 'TURN ON ACTIVITY LIGHT', line=298)
W('01,3042', 0o52165, '', 'DXCH', 'LOC', 'AND SAVE ADDRESS INFO FOR BENEFIT OF', line=299)
W('01,3043', 0o12733, '', 'TCF', 'CHANJOB + 4', ' POSSIBLE SLEEPING JOB.', line=300)

# Page 1216
# TO WAKE UP A JOB, EACH CORE SET IS FOUND TO LOCATE ALL JOBS WHICH ARE ASLEEP.  IF THE FCADR IN THE
# LOC REGISTER OF ANY SUCH JOB MATCHES THAT SUPPLIED BY THE CALLER, THAT JOB IS AWAKENED.  IF NO JOB IS FOUND,
# LOCCTR IS SET TO -1 AND NO FURTHER ACTION TAKES PLACE.

W('01,3044', 0o54061, 'JOBWAKE2', 'TS', 'EXECTEM1', line=307)
W('01,3045', 0o35021, '', 'CAF', 'ZERO', 'BEGIN CORE SET SCAN.', line=308)
W('01,3046', 0o54064, '', 'TS', 'LOCCTR', line=309)
W('01,3047', 0o32657, '', 'CAF', 'NO.CORES', line=310)
W('01,3050', 0o54062, 'JOBWAKE4', 'TS', 'EXECTEM2', line=311)
W('01,3051', 0o50064, '', 'INDEX', 'LOCCTR', line=312)
W('01,3052', 0o10167, '', 'CCS', 'PRIORITY', line=313)
W('01,3053', 0o13056, '', 'TCF', 'JOBWAKE3', 'ACTIVE JOB - CHECK NEXT CORE SET.', line=314)
W('01,3054', 0o00014, 'COREINC', 'DEC', '12', '12 REGISTERS PER CORE SET.', kind='data', line=315)
W('01,3055', 0o13065, '', 'TCF', 'WAKETEST', 'SLEEPING JOB - SEE IF CADR MATCHES.', line=316)

W('01,3056', 0o33054, 'JOBWAKE3', 'CAF', 'COREINC', line=318)
W('01,3057', 0o26064, '', 'ADS', 'LOCCTR', line=319)
W('01,3060', 0o10062, '', 'CCS', 'EXECTEM2', line=320)
W('01,3061', 0o13050, '', 'TCF', 'JOBWAKE4', line=321)
W('01,3062', 0o45017, '', 'CS', 'ONE', 'EXIT IF SLEEPING JOB NOT FOUND.', line=322)
W('01,3063', 0o54064, '', 'TS', 'LOCCTR', line=323)
W('01,3064', 0o15222, '', 'TCF', 'ENDFIND', line=324)

W('01,3065', 0o40065, 'WAKETEST', 'CS', 'NEWLOC', line=326)
W('01,3066', 0o50064, '', 'INDEX', 'LOCCTR', line=327)
W('01,3067', 0o60164, '', 'AD', 'LOC', line=328)
W('01,3070', 0o00006, '', 'EXTEND', line=329)
W('01,3071', 0o13073, '', 'BZF', '+2', 'IF MATCH.', line=330)
W('01,3072', 0o13056, '', 'TCF', 'JOBWAKE3', 'EXAMINE NEXT CORE SET IF NO MATCH.', line=331)

W('01,3073', 0o50064, '', 'INDEX', 'LOCCTR', 'RE-COMPLEMENT PRIORITY TO SHOW JOB AWAKE', line=333)
W('01,3074', 0o40167, '', 'CS', 'PRIORITY', line=334)
W('01,3075', 0o54063, '', 'TS', 'NEWPRIO', line=335)
W('01,3076', 0o50064, '', 'INDEX', 'LOCCTR', line=336)
W('01,3077', 0o54167, '', 'TS', 'PRIORITY', line=337)

W('01,3100', 0o44364, '', 'CS', 'FBANKMSK', 'MAKE UP THE 2CADR OF THE WAKE ADDRESS', line=339)
W('01,3101', 0o70065, '', 'MASK', 'NEWLOC', 'USING THE CADR IN NEWLOC AND THE EBANK', line=340)
W('01,3102', 0o65005, '', 'AD', '2K', 'HALF OF BBANK SAVED IN BANKSET.', line=341)
W('01,3103', 0o56065, '', 'XCH', 'NEWLOC', line=342)
W('01,3104', 0o74364, '', 'MASK', 'FBANKMSK', line=343)
W('01,3105', 0o50064, '', 'INDEX', 'LOCCTR', line=344)
W('01,3106', 0o60165, '', 'AD', 'BANKSET', line=345)
W('01,3107', 0o54066, '', 'TS', 'NEWLOC +1', line=346)

W('01,3110', 0o10064, '', 'CCS', 'LOCCTR', 'SPECIAL TREATMENT IF THIS JOB WAS', line=348)
W('01,3111', 0o12704, '', 'TCF', 'SETLOC', 'ALREADY IN THE RUN (0) POSITION.', line=349)
W('01,3112', 0o12674, '', 'TCF', 'SPECTEST', line=350)

# Page 1217
# PRIORITY CHANGE. CHANGE THE CONTENTS OF PRIORITY AND SCAN FOR THE JOB OF HIGHEST PRIORITY.

W('01,3113', 0o54164, 'PRIOCH2', 'TS', 'LOC', line=355)
W('01,3114', 0o35021, '', 'CAF', 'ZERO', 'SET FLAG TO TELL ENDJOB SCANNER IF THIS', line=356)
W('01,3115', 0o54130, '', 'TS', 'BUF', 'JOB IS STILL HIGHEST PRIORITY.', line=357)
W('01,3116', 0o35046, '', 'CAF', 'LOW9', line=358)
W('01,3117', 0o70167, '', 'MASK', 'PRIORITY', line=359)
W('01,3120', 0o60063, '', 'AD', 'NEWPRIO', line=360)
W('01,3121', 0o54167, '', 'TS', 'PRIORITY', line=361)
W('01,3122', 0o40000, '', 'COM', line=362)
W('01,3123', 0o13030, '', 'TCF', 'JOBSLP2', 'AND TO EJSCAN.', line=363)

# Page 1218
# RELEASE THIS CORE SET AND VAC AREA AND SCAN FOR THE JOB OF HIGHEST ACTIVE PRIORITY.

W('01,3124', 0o00004, 'ENDJOB1', 'INHINT', line=368)
W('01,3125', 0o45021, '', 'CS', 'ZERO', line=369)
W('01,3126', 0o54131, '', 'TS', 'BUF +1', line=370)
W('01,3127', 0o56167, '', 'XCH', 'PRIORITY', line=371)
W('01,3130', 0o75046, '', 'MASK', 'LOW9', line=372)
W('01,3131', 0o54001, '', 'TS', 'L', line=373)

W('01,3132', 0o45226, '', 'CS', 'FAKEPRET', line=375)
W('01,3133', 0o60001, '', 'AD', 'L', line=376)

W('01,3134', 0o00006, '', 'EXTEND', line=378)
W('01,3135', 0o63141, '', 'BZMF', 'EJSCAN', 'NOVAC ENDOFJOB', line=379)

W('01,3136', 0o10001, '', 'CCS', 'L', line=381)
W('01,3137', 0o50000, '', 'INDEX', 'A', line=382)
W('01,3140', 0o54000, '', 'TS', '0', line=383)

W('01,3141', 0o10203, 'EJSCAN', 'CCS', 'PRIORITY +12D', line=385)
W('01,3142', 0o03206, '', 'TC', 'EJ1', line=386)
W('01,3143', 0o05747, '', 'TC', 'CCSHOLE', line=387)
W('01,3144', 0o13145, '', 'TCF', '+1', line=388)

W('01,3145', 0o10217, '', 'CCS', 'PRIORITY +24D', 'EXAMINE EACH PRIORITY REGISTER TO FIND', line=390)
W('01,3146', 0o03206, '', 'TC', 'EJ1', 'THE JOB OF HIGHEST ACTIVE PRIORITY.', line=391)
W('01,3147', 0o05747, '', 'TC', 'CCSHOLE', line=392)
W('01,3150', 0o13151, '', 'TCF', '+1', line=393)

W('01,3151', 0o10233, '', 'CCS', 'PRIORITY +36D', line=395)
W('01,3152', 0o03206, '', 'TC', 'EJ1', line=396)
W('01,3153', 0o67610, '-CCSPR', '-CCS', 'PRIORITY', line=397)
W('01,3154', 0o13155, '', 'TCF', '+1', line=398)

W('01,3155', 0o10247, '', 'CCS', 'PRIORITY +48D', line=400)
W('01,3156', 0o03206, '', 'TC', 'EJ1', line=401)
W('01,3157', 0o05747, '', 'TC', 'CCSHOLE', line=402)
W('01,3160', 0o13161, '', 'TCF', '+1', line=403)

W('01,3161', 0o10263, '', 'CCS', 'PRIORITY +60D', line=405)
W('01,3162', 0o03206, '', 'TC', 'EJ1', line=406)
W('01,3163', 0o05747, '', 'TC', 'CCSHOLE', line=407)
W('01,3164', 0o13165, '', 'TCF', '+1', line=408)

W('01,3165', 0o10277, '', 'CCS', 'PRIORITY +72D', line=410)
W('01,3166', 0o03206, '', 'TC', 'EJ1', line=411)
W('01,3167', 0o05747, '', 'TC', 'CCSHOLE', line=412)
W('01,3170', 0o13171, '', 'TCF', '+1', line=413)

# Page 1219
# EVALUATE THE RESULTS OF THE SCAN.

W('01,3171', 0o10131, '', 'CCS', 'BUF +1', 'SEE IF THERE ARE ANY ACTIVE JOBS WAITING', line=418)
W('01,3172', 0o05747, '', 'TC', 'CCSHOLE', line=419)
W('01,3173', 0o05747, '', 'TC', 'CCSHOLE', line=420)

W('01,3174', 0o13176, '', 'TCF', '+2', line=422)
W('01,3175', 0o13223, '', 'TCF', 'DUMMYJOB', line=423)
W('01,3176', 0o10130, '', 'CCS', 'BUF', 'BUF IS ZERO IF THIS IS A PRIOCHNG AND', line=424)
W('01,3177', 0o13201, '', 'TCF', '+2', 'CHANGED PRIORITY IS STILL HIGHEST.', line=425)
W('01,3200', 0o13005, '', 'TCF', 'ENDPRCHG -1', line=426)

W('01,3201', 0o50000, '', 'INDEX', 'A', 'OTHERWISE, SET NEWJOB TO THE RELATIVE', line=428)
W('01,3202', 0o27777, '', 'CAF', '0 -1', "ADDRESS OF THE NEW JOB'S CORE SET.", line=429)
W('01,3203', 0o63153, '', 'AD', '-CCSPR', line=430)
W('01,3204', 0o54067, '', 'TS', 'NEWJOB', line=431)
W('01,3205', 0o12725, '', 'TCF', 'CHANJOB -2', line=432)

W('01,3206', 0o54132, 'EJ1', 'TS', 'BUF +2', line=434)
W('01,3207', 0o60131, '', 'AD', 'BUF +1', '- OLD HIGH PRIORITY.', line=435)
W('01,3210', 0o10000, '', 'CCS', 'A', line=436)
W('01,3211', 0o40132, '', 'CS', 'BUF +2', line=437)
W('01,3212', 0o13216, '', 'TCF', 'EJ2', 'NEW HIGH PRIORITY.', line=438)
W('01,3213', 0o13214, '', 'NOOP', line=439)
W('01,3214', 0o50002, '', 'INDEX', 'Q', line=440)
W('01,3215', 0o00002, '', 'TC', '2', 'PROCEED WITH SEARCH.', line=441)

W('01,3216', 0o54131, 'EJ2', 'TS', 'BUF +1', line=443)
W('01,3217', 0o00006, '', 'EXTEND', line=444)
W('01,3220', 0o22130, '', 'QXCH', 'BUF', 'FOR LOCATING CCS PRIORITY + X INSTR.', line=445)
W('01,3221', 0o50130, '', 'INDEX', 'BUF', line=446)
W('01,3222', 0o00002, '', 'TC', '2', line=447)

# Page 1220
# IDLING AND COMPUTER ACTIVITY (GREEN) LIGHT MAINTENANCE. THE IDLING ROUTINE IS NOT A JOB IN ITSELF,
# BUT RATHER A SUBROUTINE OF THE EXECUTIVE.

#   EBANK= SELFRET  # SELF-CHECK STORAGE IN EBANK.

W('01,3223', 0o45021, 'DUMMYJOB', 'CS', 'ZERO', 'SET NEWJOB TO -0 FOR IDLING.', line=455)
W('01,3224', 0o54067, '', 'TS', 'NEWJOB', line=456)
W('01,3225', 0o00003, '', 'RELINT', line=457)
W('01,3226', 0o45016, '', 'CS', 'TWO', 'TURN OFF THE ACTIVITY LIGHT.', line=458)
W('01,3227', 0o00006, '', 'EXTEND', line=459)
W('01,3230', 0o03011, '', 'WAND', 'DSALMOUT', line=460)
W('01,3231', 0o10067, 'ADVAN', 'CCS', 'NEWJOB', 'IS A NEWJOB ACTIVE ?', line=461)
W('01,3232', 0o13032, '', 'TCF', 'NUCHANG2', 'YES... ONE REQUIRING A CHANGE JOB.', line=462)
W('01,3233', 0o35016, '', 'CAF', 'TWO', 'NEW JOB ALREADY IN POSITION FOR', line=463)
W('01,3234', 0o13242, '', 'TCF', 'NUDIRECT', 'EXECUTION.', line=464)

W('01,3235', 0o31361, '', 'CA', 'SELFRET', line=466)
W('01,3236', 0o54001, '', 'TS', 'L', 'PUT RETURN ADDRESS IN L.', line=467)
W('01,3237', 0o33241, '', 'CAF', 'SELFBANK', line=468)
W('01,3240', 0o15230, '', 'TCF', 'SUPDXCHZ + 1', 'AND DISPATCH JOB.', line=469)

#   EBANK= SELFRET
W('01,3241', 0o66102, 'SELFBANK', 'BBCON', 'SELFCHK', kind='data', line=472)

W('01,3242', 0o00006, 'NUDIRECT', 'EXTEND', '', 'TURN THE GREEN LIGHT BACK ON.', line=474)
W('01,3243', 0o05011, '', 'WOR', 'DSALMOUT', line=475)
W('01,3244', 0o52165, '', 'DXCH', 'LOC', 'JOBS STARTED IN THIS FASHION MUST BE', line=476)
W('01,3245', 0o15227, '', 'TCF', 'SUPDXCHZ', line=477)

#   BLOCK 2  # IN FIXED-FIXED SO OTHERS MAY USE.

#   COUNT 02/EXEC

# SUPDXCHZ - ROUTINE TO TRANSFER TO SUPERBANK.
# CALLING SEQUENCE
# TCF     SUPDXCHZ        # WITH 2CADR OF DESIRED LOCATION IN A + L.

W('5227', 0o56001, 'SUPDXCHZ', 'XCH', 'L', 'BASIC.', line=487)
W('5230', 0o00006, '', 'EXTEND', line=488)
W('5231', 0o01007, '', 'WRITE', 'SUPERBNK', line=489)
W('5232', 0o54006, '', 'TS', 'BBANK', line=490)
W('5233', 0o00001, '', 'TC', 'L', line=491)

W('5234', 0o77677, 'NEG100', 'OCT', '77677', kind='data', line=493)
