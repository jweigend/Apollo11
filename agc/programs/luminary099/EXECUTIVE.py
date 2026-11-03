"""EXECUTIVE.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/EXECUTIVE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 1103-1116 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('EXECUTIVE', 'EXECUTIVE.agc', 'Luminary099', pages='1103-1116')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     EXECUTIVE.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        1103-1114
# Mod history:  2009-05-25 RSB  Adapted from the corresponding
# Luminary131 file, using page
# images from Luminary 1A.
# 2011-01-06 JL   Fixed pseudo-label indentation.
# 2011-05-08 JL   Removed workaround.

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

# Page 1103
#   BLOCK 02

# TO ENTER A JOB REQUEST REQUIRING NO VAC AREA:

#   COUNT* $$/EXEC
W('5072', 0o00004, 'NOVAC', 'INHINT', line=37)
W('5073', 0o65164, '', 'AD', 'FAKEPRET', 'LOC(MPAC +6) - LOC(QPRET)', line=38)
W('5074', 0o54063, '', 'TS', 'NEWPRIO', 'PRIORITY OF NEW JOB + NOVAC C(FIXLOC)', line=39)

W('5075', 0o00006, '', 'EXTEND', line=41)
W('5076', 0o50002, '', 'INDEX', 'Q', 'Q WILL BE UNDISTURBED THROUGHOUT.', line=42)
W('5077', 0o30001, '', 'DCA', '0', '2CADR OF JOB ENTERED.', line=43)
W('5100', 0o52066, '', 'DXCH', 'NEWLOC', line=44)
W('5101', 0o35163, '', 'CAF', 'EXECBANK', line=45)
W('5102', 0o56004, '', 'XCH', 'FBANK', line=46)
W('5103', 0o54061, '', 'TS', 'EXECTEM1', line=47)
W('5104', 0o12625, '', 'TCF', 'NOVAC2', 'ENTER EXECUTIVE BANK.', line=48)

# TO ENTER A JOB REQUEST REQUIREING A VAC AREA -- E.G., ALL (PARTIALLY) INTERPRETIVE JOBS.

W('5105', 0o00004, 'FINDVAC', 'INHINT', line=52)
W('5106', 0o54063, '', 'TS', 'NEWPRIO', line=53)
W('5107', 0o00006, '', 'EXTEND', line=54)
W('5110', 0o50002, '', 'INDEX', 'Q', line=55)
W('5111', 0o30001, '', 'DCA', '0', line=56)
W('5112', 0o52066, 'SPVACIN', 'DXCH', 'NEWLOC', line=57)
W('5113', 0o35163, '', 'CAF', 'EXECBANK', line=58)
W('5114', 0o56004, '', 'XCH', 'FBANK', line=59)
W('5115', 0o12601, '', 'TCF', 'FINDVAC2', 'OFF TO EXECUTIVE SWITCHED-BANK.', line=60)

# TO ENTER A FINDVAC WITH THE PRIORITY IN NEWPRIO TO THE 2CADR ARRIVING IN A AND L:
# USERS OF SPVAC MUST INHINT BEFORE STORING IN NEWPRIO.

W('5116', 0o56002, 'SPVAC', 'XCH', 'Q', line=65)
W('5117', 0o67746, '', 'AD', 'NEG2', line=66)
W('5120', 0o56002, '', 'XCH', 'Q', line=67)
W('5121', 0o15112, '', 'TCF', 'SPVACIN', line=68)

# TO SUSPEND A BASIC JOB SO A HIGHER PRIORITY JOB MAY BE SERVICED:

W('5122', 0o22002, 'CHANG1', 'LXCH', 'Q', line=72)
W('5123', 0o35163, '', 'CAF', 'EXECBANK', line=73)
W('5124', 0o56006, '', 'XCH', 'BBANK', line=74)
W('5125', 0o12706, '', 'TCF', 'CHANJOB', line=75)

# TO SUSPEND AN INTERPRETIVE JOB:

W('5126', 0o40164, 'CHANG2', 'CS', 'LOC', 'NEGATIVE LOC SHOWS JOB = INTERPRETIVE.', line=79)
# ITRACE (4) REFERS TO "CHANG2"
W('5127', 0o54001, '', 'TS', 'L', line=81)
# Page 1104
W('5130', 0o35163, '', 'CAF', 'EXECBANK', line=83)
W('5131', 0o54006, '', 'TS', 'BBANK', line=84)
W('5132', 0o12705, '', 'TCF', 'CHANJOB -1', line=85)

# Page 1105
# TO VOLUNTARILY SUSPEND A JOB UNTIL THE COMPLETION OF SOME ANTICIPATED EVENT (I/O EVENT ETC.):

W('5133', 0o54164, 'JOBSLEEP', 'TS', 'LOC', line=90)
W('5134', 0o35163, '', 'CAF', 'EXECBANK', line=91)
W('5135', 0o54004, '', 'TS', 'FBANK', line=92)
W('5136', 0o12776, '', 'TCF', 'JOBSLP1', line=93)

# TO AWAKEN A JOB PUT TO SLEEP IN THE ABOVE FASHION:

W('5137', 0o00004, 'JOBWAKE', 'INHINT', line=97)
W('5140', 0o54065, '', 'TS', 'NEWLOC', line=98)
W('5141', 0o44752, '', 'CS', 'TWO', 'EXIT IS VIA FINDVAC/NOVAC PROCEDURES.', line=99)
W('5142', 0o26002, '', 'ADS', 'Q', line=100)
W('5143', 0o35163, '', 'CAF', 'EXECBANK', line=101)
W('5144', 0o56004, '', 'XCH', 'FBANK', line=102)
W('5145', 0o13023, '', 'TCF', 'JOBWAKE2', line=103)

# TO CHANGE THE PRIORITY OF A JOB CURRENTLY UNDER EXECUTION:

W('5146', 0o00004, 'PRIOCHNG', 'INHINT', '', 'NEW PRIORITY ARRIVES IN A.  RETURNS TO', line=107)
W('5147', 0o54063, '', 'TS', 'NEWPRIO', 'CALLER AS SOON AS NEW JOB PRIORITY IS', line=108)
W('5150', 0o35163, '', 'CAF', 'EXECBANK', 'HIGHEST.  PREPARE FOR POSSIBLE BASIC-', line=109)
W('5151', 0o56006, '', 'XCH', 'BBANK', 'STYLE CHANGE-JOB.', line=110)
W('5152', 0o54165, '', 'TS', 'BANKSET', line=111)
W('5153', 0o30002, '', 'CA', 'Q', line=112)
W('5154', 0o13072, '', 'TCF', 'PRIOCH2', line=113)

# TO REMOVE A JOB FROM EXECUTIVE CONSIDERATIONS:

W('5155', 0o35163, 'ENDOFJOB', 'CAF', 'EXECBANK', line=117)
W('5156', 0o54004, '', 'TS', 'FBANK', line=118)
W('5157', 0o13103, '', 'TCF', 'ENDJOB1', line=119)

W('5160', 0o30061, 'ENDFIND', 'CA', 'EXECTEM1', 'RETURN TO CALLER AFTER JOB ENTRY', line=121)
W('5161', 0o54004, '', 'TS', 'FBANK', 'COMPLETE.', line=122)
W('5162', 0o16741, '', 'TCF', 'Q+2', line=123)
W('5163', 0o02601, 'EXECBANK', 'CADR', 'FINDVAC2', kind='data', line=124)

W('5164', 0o00110, 'FAKEPRET', 'ADRES', 'MPAC -36D', 'LOC(MPAC +6) - LOC(QPRET)', kind='data', line=126)

# Page 1106
# LOCATE AN AVAILABLE VAC AREA

#   BANK 01
#   COUNT* $$/EXEC
W('01,2601', 0o54061, 'FINDVAC2', 'TS', 'EXECTEM1', "(SAVE CALLER'S BANK FIRST.)", line=133)
W('01,2602', 0o10400, '', 'CCS', 'VAC1USE', line=134)
W('01,2603', 0o12620, '', 'TCF', 'VACFOUND', line=135)
W('01,2604', 0o10454, '', 'CCS', 'VAC2USE', line=136)
W('01,2605', 0o12620, '', 'TCF', 'VACFOUND', line=137)
W('01,2606', 0o10530, '', 'CCS', 'VAC3USE', line=138)
W('01,2607', 0o12620, '', 'TCF', 'VACFOUND', line=139)
W('01,2610', 0o10604, '', 'CCS', 'VAC4USE', line=140)
W('01,2611', 0o12620, '', 'TCF', 'VACFOUND', line=141)
W('01,2612', 0o10660, '', 'CCS', 'VAC5USE', line=142)
W('01,2613', 0o12620, '', 'TCF', 'VACFOUND', line=143)
W('01,2614', 0o22061, '', 'LXCH', 'EXECTEM1', line=144)
W('01,2615', 0o30002, '', 'CA', 'Q', line=145)
W('01,2616', 0o05716, '', 'TC', 'BAILOUT1', line=146)
W('01,2617', 0o01201, '', 'OCT', '1201', 'NO VAC AREAS.', kind='data', line=147)

W('01,2620', 0o64752, 'VACFOUND', 'AD', 'TWO', 'RESERVE THIS VAC AREA BY STORING A ZERO', line=149)
W('01,2621', 0o22007, '', 'ZL', '', 'IN ITS VAC USE REGISTER AND STORE THE', line=150)
W('01,2622', 0o50000, '', 'INDEX', 'A', 'ADDRESS OF THE FIRST WORD OF IT IN THE', line=151)
W('01,2623', 0o21777, '', 'LXCH', '0 -1', 'LOW NINE BITS OF THE PRIORITY WORD.', line=152)
W('01,2624', 0o26063, '', 'ADS', 'NEWPRIO', line=153)

W('01,2625', 0o34755, 'NOVAC2', 'CAF', 'ZERO', 'NOVAC ENTERS HERE.  FIND A CORE SET.', line=155)
W('01,2626', 0o54064, '', 'TS', 'LOCCTR', line=156)
W('01,2627', 0o32634, '', 'CAF', 'NO.CORES', 'SEVEN SETS OF ELEVEN REGISTERS EACH.', line=157)
W('01,2630', 0o54062, 'NOVAC3', 'TS', 'EXECTEM2', line=158)
W('01,2631', 0o50064, '', 'INDEX', 'LOCCTR', line=159)
W('01,2632', 0o10167, '', 'CCS', 'PRIORITY', 'EACH PRIORITY REGISTER CONTAINS -0 IF', line=160)
W('01,2633', 0o12674, '', 'TCF', 'NEXTCORE', 'THE CORESPONDING CORE SET IS AVAILABLE.', line=161)
W('01,2634', 0o00007, 'NO.CORES', 'DEC', '7', kind='data', line=162)
W('01,2635', 0o12674, '', 'TCF', 'NEXTCORE', 'AN ACTIVE JOB HAS A POSITIVE PRIORITY', line=163)
# BUT A DORMANT JOB'S PRIORITY IS NEGATIVE

# Page 1107
W('01,2636', 0o30063, 'CORFOUND', 'CA', 'NEWPRIO', 'SET THE PRIORITY OF THIS JOB IN THE CORE', line=167)
W('01,2637', 0o50064, '', 'INDEX', 'LOCCTR', "SET'S PRIORITY REGISTER AND SET THE", line=168)
W('01,2640', 0o54167, '', 'TS', 'PRIORITY', "JOB'S PUSH-DOWN POINTER AT THE BEGINNING", line=169)
W('01,2641', 0o75004, '', 'MASK', 'LOW9', 'OF THE WORK AREA AND OVERFLOW INDICATOR.', line=170)
W('01,2642', 0o50064, '', 'INDEX', 'LOCCTR', line=171)
W('01,2643', 0o54166, '', 'TS', 'PUSHLOC', 'OFF TO PREPARE FOR INTERPRETIVE PROGRAMS.', line=172)

W('01,2644', 0o10064, '', 'CCS', 'LOCCTR', 'IF CORE SET ZERO IS BEING LOADED, SET UP', line=174)
W('01,2645', 0o12661, '', 'TCF', 'SETLOC', 'OVFIND AND FIXLOC IMMEDIATELY.', line=175)
W('01,2646', 0o54121, '', 'TS', 'OVFIND', line=176)
W('01,2647', 0o30166, '', 'CA', 'PUSHLOC', line=177)
W('01,2650', 0o54120, '', 'TS', 'FIXLOC', line=178)

W('01,2651', 0o10067, 'SPECTEST', 'CCS', 'NEWJOB', 'SEE IF ANY ACTIVE JOBS WAITING (RARE).', line=180)
W('01,2652', 0o12661, '', 'TCF', 'SETLOC', 'MUST BE AWAKENED OUT UNCHANGED JOB.', line=181)
W('01,2653', 0o05705, '', 'TC', 'CCSHOLE', line=182)
W('01,2654', 0o05705, '', 'TC', 'CCSHOLE', line=183)
W('01,2655', 0o54067, '', 'TS', 'NEWJOB', '+0 SHOWS ACTIVE JOB ALREADY SET.', line=184)
W('01,2656', 0o52066, '', 'DXCH', 'NEWLOC', line=185)
W('01,2657', 0o52165, '', 'DXCH', 'LOC', line=186)
W('01,2660', 0o15160, '', 'TCF', 'ENDFIND', line=187)

W('01,2661', 0o52066, 'SETLOC', 'DXCH', 'NEWLOC', 'SET UP THE LOCATION REGISTERS FOR THIS', line=189)
W('01,2662', 0o50064, '', 'INDEX', 'LOCCTR', line=190)
W('01,2663', 0o52165, '', 'DXCH', 'LOC', line=191)
W('01,2664', 0o50067, '', 'INDEX', 'NEWJOB', 'THIS INDEX INSTRUCTION INSURES THAT THE', line=192)
W('01,2665', 0o40167, '', 'CS', 'PRIORITY', 'HIGHEST ACTIVE PRIORITY WILL BE COMPARED', line=193)
W('01,2666', 0o60063, '', 'AD', 'NEWPRIO', 'WITH THE NEW PRIORITY TO SEE IF NEWJOB', line=194)
W('01,2667', 0o00006, '', 'EXTEND', '', 'SHOULD BE SET TO SIGNAL A SWITCH.', line=195)
W('01,2670', 0o65160, '', 'BZMF', 'ENDFIND', line=196)
W('01,2671', 0o30064, '', 'CA', 'LOCCTR', 'LOCCTR IS LEFT SET AT THIS CORE SET IF', line=197)
W('01,2672', 0o54067, '', 'TS', 'NEWJOB', 'THE CALLER WANTS TO LOAD ANY MPAC', line=198)
W('01,2673', 0o15160, '', 'TCF', 'ENDFIND', 'REGISTERS, ETC.', line=199)

W('01,2674', 0o33033, 'NEXTCORE', 'CAF', 'COREINC', line=201)
W('01,2675', 0o26064, '', 'ADS', 'LOCCTR', line=202)
W('01,2676', 0o10062, '', 'CCS', 'EXECTEM2', line=203)
W('01,2677', 0o12630, '', 'TCF', 'NOVAC3', line=204)
W('01,2700', 0o22061, '', 'LXCH', 'EXECTEM1', line=205)
W('01,2701', 0o30002, '', 'CA', 'Q', line=206)
W('01,2702', 0o05716, '', 'TC', 'BAILOUT1', 'NO CORE SETS AVAILABLE.', line=207)
W('01,2703', 0o01202, '', 'OCT', '1202', kind='data', line=208)
# Page 1108
# THE FOLLOWING ROUTINE SWAPS CORE SET 0 WITH THAT WHOSE RELATIVE ADDRESS IS IN NEWJOB.

W('01,2704', 0o22164, '', 'LXCH', 'LOC', line=212)
W('01,2705', 0o30165, '', 'CAE', 'BANKSET', 'BANKSET, NOT BBANK, HAS RIGHT CONTENTS.', line=213)
W('01,2706', 0o00004, 'CHANJOB', 'INHINT', line=214)
W('01,2707', 0o00006, '', 'EXTEND', line=215)
W('01,2710', 0o04007, '', 'ROR', 'SUPERBNK', 'PICK UP CURRENT SBANK FOR BBCON', line=216)
W('01,2711', 0o56001, '', 'XCH', 'L', 'LOC IN A AND BBCON IN L.', line=217)
W('01,2712', 0o50067, '', 'INDEX', 'NEWJOB', 'SWAP LOC AND BANKSET.', line=218)
W('01,2713', 0o52165, '', 'DXCH', 'LOC', line=219)
W('01,2714', 0o52165, '', 'DXCH', 'LOC', line=220)

W('01,2715', 0o30165, '', 'CAE', 'BANKSET', line=222)
W('01,2716', 0o00006, '', 'EXTEND', line=223)
W('01,2717', 0o01007, '', 'WRITE', 'SUPERBNK', 'SET SBANK FOR NEW JOB.', line=224)
W('01,2720', 0o52155, '', 'DXCH', 'MPAC', 'SWAP MULTI-PURPOSE ACCUMULATOR AREAS.', line=225)
W('01,2721', 0o50067, '', 'INDEX', 'NEWJOB', line=226)
W('01,2722', 0o52155, '', 'DXCH', 'MPAC', line=227)
W('01,2723', 0o52155, '', 'DXCH', 'MPAC', line=228)
W('01,2724', 0o52157, '', 'DXCH', 'MPAC +2', line=229)
W('01,2725', 0o50067, '', 'INDEX', 'NEWJOB', line=230)
W('01,2726', 0o52157, '', 'DXCH', 'MPAC +2', line=231)
W('01,2727', 0o52157, '', 'DXCH', 'MPAC +2', line=232)
W('01,2730', 0o52161, '', 'DXCH', 'MPAC +4', line=233)
W('01,2731', 0o50067, '', 'INDEX', 'NEWJOB', line=234)
W('01,2732', 0o52161, '', 'DXCH', 'MPAC +4', line=235)
W('01,2733', 0o52161, '', 'DXCH', 'MPAC +4', line=236)
W('01,2734', 0o52163, '', 'DXCH', 'MPAC +6', line=237)
W('01,2735', 0o50067, '', 'INDEX', 'NEWJOB', line=238)
W('01,2736', 0o52163, '', 'DXCH', 'MPAC +6', line=239)
W('01,2737', 0o52163, '', 'DXCH', 'MPAC +6', line=240)

W('01,2740', 0o34755, '', 'CAF', 'ZERO', line=242)
W('01,2741', 0o56121, '', 'XCH', 'OVFIND', 'MAKE PUSHLOC NEGATIVE IF OVFIND NZ.', line=243)
W('01,2742', 0o00006, '', 'EXTEND', line=244)
W('01,2743', 0o12746, '', 'BZF', '+3', line=245)
W('01,2744', 0o40166, '', 'CS', 'PUSHLOC', line=246)
W('01,2745', 0o54166, '', 'TS', 'PUSHLOC', line=247)

W('01,2746', 0o52167, '', 'DXCH', 'PUSHLOC', line=249)
W('01,2747', 0o50067, '', 'INDEX', 'NEWJOB', line=250)
W('01,2750', 0o52167, '', 'DXCH', 'PUSHLOC', line=251)
W('01,2751', 0o52167, '', 'DXCH', 'PUSHLOC', 'SWAPS PUSHLOC AND PRIORITY.', line=252)
W('01,2752', 0o35004, '', 'CAF', 'LOW9', 'SET FIXLOC TO BASE OF VAC AREA.', line=253)
W('01,2753', 0o70167, '', 'MASK', 'PRIORITY', line=254)
W('01,2754', 0o54120, '', 'TS', 'FIXLOC', line=255)

W('01,2755', 0o10166, '', 'CCS', 'PUSHLOC', 'SET OVERFLOW INDICATOR ACCORDING TO', line=257)
W('01,2756', 0o34755, '', 'CAF', 'ZERO', line=258)
W('01,2757', 0o12764, '', 'TCF', 'ENDPRCHG -1', line=259)

# Page 1109
W('01,2760', 0o40166, '', 'CS', 'PUSHLOC', line=262)
W('01,2761', 0o54166, '', 'TS', 'PUSHLOC', line=263)
W('01,2762', 0o34753, '', 'CAF', 'ONE', line=264)
W('01,2763', 0o56121, '', 'XCH', 'OVFIND', line=265)
W('01,2764', 0o54067, '', 'TS', 'NEWJOB', line=266)

W('01,2765', 0o00003, 'ENDPRCHG', 'RELINT', line=268)
W('01,2766', 0o52165, '', 'DXCH', 'LOC', 'BASIC JOBS HAVE POSITIVE ADDRESSES, SO', line=269)
W('01,2767', 0o00006, '', 'EXTEND', '', 'DISPATCH WITH A DTCB.', line=270)
W('01,2770', 0o62772, '', 'BZMF', '+2', 'IF INTERPRETIVE, SET UP EBANK, ETC.', line=271)
W('01,2771', 0o52006, '', 'DTCB', line=272)
# Page 1110
W('01,2772', 0o40000, '', 'COM', '', 'EPILOGUE TO JOB CHANGE FOR INTERPRETIVE', line=274)
W('01,2773', 0o64753, '', 'AD', 'ONE', line=275)
W('01,2774', 0o54164, '', 'TS', 'LOC', 'RESUME', line=276)
W('01,2775', 0o16050, '', 'TCF', 'INTRSM', line=277)

# COMPLETE JOBSLEEP PREPARATIONS.

W('01,2776', 0o00004, 'JOBSLP1', 'INHINT', line=281)
W('01,2777', 0o40167, '', 'CS', 'PRIORITY', 'NNZ PRIORITY SHOWS JOB ASLEEP.', line=282)
W('01,3000', 0o54167, '', 'TS', 'PRIORITY', line=283)
W('01,3001', 0o36074, '', 'CAF', 'LOW7', line=284)
W('01,3002', 0o70006, '', 'MASK', 'BBANK', line=285)
W('01,3003', 0o00006, '', 'EXTEND', line=286)
W('01,3004', 0o04007, '', 'ROR', 'SUPERBNK', 'SAVE OLD SUPERBANK VALUE.', line=287)
W('01,3005', 0o54165, '', 'TS', 'BANKSET', line=288)
W('01,3006', 0o44755, '', 'CS', 'ZERO', line=289)
W('01,3007', 0o54131, 'JOBSLP2', 'TS', 'BUF +1', 'HOLDS -- HIGHEST PRIORITY.', line=290)
W('01,3010', 0o13120, '', 'TCF', 'EJSCAN', 'SCAN FOR HIGHEST PRIORITY ALA ENDOFJOB.', line=291)

W('01,3011', 0o00004, 'NUCHANG2', 'INHINT', '', "QUICK... DON'T LET NEWJOB CHANGE TO +0.", line=293)
W('01,3012', 0o10067, '', 'CCS', 'NEWJOB', line=294)
W('01,3013', 0o13016, '', 'TCF', '+3', 'NEWJOB STILL PNZ', line=295)
W('01,3014', 0o00003, '', 'RELINT', '', 'NEW JOB HAS CHANGED TO +0.  WAKE UP JOB', line=296)
W('01,3015', 0o13216, '', 'TCF', 'ADVAN +2', 'VIA NUDIRECT.  (VERY RARE CASE.)', line=297)

W('01,3016', 0o34752, '', 'CAF', 'TWO', line=299)
W('01,3017', 0o00006, '', 'EXTEND', line=300)
W('01,3020', 0o05011, '', 'WOR', 'DSALMOUT', 'TURN ON ACTIVITY LIGHT', line=301)
W('01,3021', 0o52165, '', 'DXCH', 'LOC', 'AND SAVE ADDRESS INFO FOR BENEFIT OF', line=302)
W('01,3022', 0o12712, '', 'TCF', 'CHANJOB +4', '      POSSIBLE SLEEPINT JOB.', line=303)

# Page 1111
# TO WAKE UP A JOB, EACH CORE SET IS FOUND TO LOCATE ALL JOBS WHICH ARE ASLEEP.  IF THE FCADR IN THE
# LOC REGISTER OF ANY SUCH JOB MATCHES THAT SUPPLIED BY THE CALLER, THAT JOB IS AWAKENED.  IF NO JOB IS FOUND,
# LOCCTR IS SET TO -1 AND NO FURTHER ACTION TAKES PLACE.

W('01,3023', 0o54061, 'JOBWAKE2', 'TS', 'EXECTEM1', line=310)
W('01,3024', 0o34755, '', 'CAF', 'ZERO', 'BEGIN CORE SET SCAN', line=311)
W('01,3025', 0o54064, '', 'TS', 'LOCCTR', line=312)
W('01,3026', 0o32634, '', 'CAF', 'NO.CORES', line=313)
W('01,3027', 0o54062, 'JOBWAKE4', 'TS', 'EXECTEM2', line=314)
W('01,3030', 0o50064, '', 'INDEX', 'LOCCTR', line=315)
W('01,3031', 0o10167, '', 'CCS', 'PRIORITY', line=316)
W('01,3032', 0o13035, '', 'TCF', 'JOBWAKE3', 'ACTIVE JOB -- CHECK NEXT CORE SET.', line=317)
W('01,3033', 0o00014, 'COREINC', 'DEC', '12', '12 REGISTERS PER CORE SET.', kind='data', line=318)
W('01,3034', 0o13044, '', 'TCF', 'WAKETEST', 'SLEEPING JOB -- SEE IF CADR MATCHES.', line=319)

W('01,3035', 0o33033, 'JOBWAKE3', 'CAF', 'COREINC', line=321)
W('01,3036', 0o26064, '', 'ADS', 'LOCCTR', line=322)
W('01,3037', 0o10062, '', 'CCS', 'EXECTEM2', line=323)
W('01,3040', 0o13027, '', 'TCF', 'JOBWAKE4', line=324)
W('01,3041', 0o44753, '', 'CS', 'ONE', 'EXIT IF SLEEPIN JOB NOT FOUND.', line=325)
W('01,3042', 0o54064, '', 'TS', 'LOCCTR', line=326)
W('01,3043', 0o15160, '', 'TCF', 'ENDFIND', line=327)

W('01,3044', 0o40065, 'WAKETEST', 'CS', 'NEWLOC', line=329)
W('01,3045', 0o50064, '', 'INDEX', 'LOCCTR', line=330)
W('01,3046', 0o60164, '', 'AD', 'LOC', line=331)
W('01,3047', 0o00006, '', 'EXTEND', line=332)
W('01,3050', 0o13052, '', 'BZF', '+2', 'IF MATCH.', line=333)
W('01,3051', 0o13035, '', 'TCF', 'JOBWAKE3', 'EXAMINE NEXT CORE SET IF NO MATCH.', line=334)

W('01,3052', 0o50064, '', 'INDEX', 'LOCCTR', 'RE-COMPLEMENT PRIORITY TO SHOW JOB AWAKE', line=336)
W('01,3053', 0o40167, '', 'CS', 'PRIORITY', line=337)
W('01,3054', 0o54063, '', 'TS', 'NEWPRIO', line=338)
W('01,3055', 0o50064, '', 'INDEX', 'LOCCTR', line=339)
W('01,3056', 0o54167, '', 'TS', 'PRIORITY', line=340)

W('01,3057', 0o44350, '', 'CS', 'FBANKMSK', 'MAKE UP THE 2CADR OF THE WAKE ADDRESS', line=342)
W('01,3060', 0o70065, '', 'MASK', 'NEWLOC', 'USING THE CADR IN NEWLOC AND THE EBANK', line=343)
W('01,3061', 0o64741, '', 'AD', '2K', 'HALF OF BBANK SAVED IN BANKSET.', line=344)
W('01,3062', 0o56065, '', 'XCH', 'NEWLOC', line=345)
W('01,3063', 0o74350, '', 'MASK', 'FBANKMSK', line=346)
W('01,3064', 0o50064, '', 'INDEX', 'LOCCTR', line=347)
W('01,3065', 0o60165, '', 'AD', 'BANKSET', line=348)
W('01,3066', 0o54066, '', 'TS', 'NEWLOC +1', line=349)

W('01,3067', 0o10064, '', 'CCS', 'LOCCTR', 'SPECIAL TREATMENT IF THIS JOB WAS', line=351)
W('01,3070', 0o12661, '', 'TCF', 'SETLOC', 'ALREADY IN THE RUN (0) POSITION.', line=352)
W('01,3071', 0o12651, '', 'TCF', 'SPECTEST', line=353)

# Page 1112
# PRIORITY CHANGE.  CHANGE THE CONTENTS OF PRIORITY AND SCAN FOR THE JOB OF HIGHEST PRIORITY.

W('01,3072', 0o54164, 'PRIOCH2', 'TS', 'LOC', line=358)
W('01,3073', 0o34755, '', 'CAF', 'ZERO', 'SET FLAG TO TELL ENDJOB SCANNER IF THIS', line=359)
W('01,3074', 0o54130, '', 'TS', 'BUF', 'JOB IS STILL HIGHEST PRIORITY.', line=360)
W('01,3075', 0o35004, '', 'CAF', 'LOW9', line=361)
W('01,3076', 0o70167, '', 'MASK', 'PRIORITY', line=362)
W('01,3077', 0o60063, '', 'AD', 'NEWPRIO', line=363)
W('01,3100', 0o54167, '', 'TS', 'PRIORITY', line=364)
W('01,3101', 0o40000, '', 'COM', line=365)
W('01,3102', 0o13007, '', 'TCF', 'JOBSLP2', 'AND TO EJSCAN.', line=366)

# Page 1113
# RELEASE THIS CORE SET AND VAC AREA AND SCAN FOR THE JOB OF HIGHEST ACTIVE PRIORITY.

W('01,3103', 0o00004, 'ENDJOB1', 'INHINT', line=371)
W('01,3104', 0o44755, '', 'CS', 'ZERO', line=372)
W('01,3105', 0o54131, '', 'TS', 'BUF +1', line=373)
W('01,3106', 0o56167, '', 'XCH', 'PRIORITY', line=374)
W('01,3107', 0o75004, '', 'MASK', 'LOW9', line=375)
W('01,3110', 0o54001, '', 'TS', 'L', line=376)

W('01,3111', 0o45164, '', 'CS', 'FAKEPRET', line=378)
W('01,3112', 0o60001, '', 'AD', 'L', line=379)

W('01,3113', 0o00006, '', 'EXTEND', line=381)
W('01,3114', 0o63120, '', 'BZMF', 'EJSCAN', 'NOVAC ENDOFJOB', line=382)

W('01,3115', 0o10001, '', 'CCS', 'L', line=384)
W('01,3116', 0o50000, '', 'INDEX', 'A', line=385)
W('01,3117', 0o54000, '', 'TS', '0', line=386)

W('01,3120', 0o10203, 'EJSCAN', 'CCS', 'PRIORITY +12D', line=388)
W('01,3121', 0o03171, '', 'TC', 'EJ1', line=389)
W('01,3122', 0o05705, '', 'TC', 'CCSHOLE', line=390)
W('01,3123', 0o13124, '', 'TCF', '+1', line=391)

W('01,3124', 0o10217, '', 'CCS', 'PRIORITY +24D', 'EXAMINE EACH PRIORITY REGISTER TO FIND', line=393)
W('01,3125', 0o03171, '', 'TC', 'EJ1', 'THE JOB OF HIGHEST ACTIVE PRIORITY.', line=394)
W('01,3126', 0o05705, '', 'TC', 'CCSHOLE', line=395)
W('01,3127', 0o13130, '', 'TCF', '+1', line=396)

W('01,3130', 0o10233, '', 'CCS', 'PRIORITY +36D', line=398)
W('01,3131', 0o03171, '', 'TC', 'EJ1', line=399)
W('01,3132', 0o67610, '-CCSPR', '-CCS', 'PRIORITY', line=400)
W('01,3133', 0o13134, '', 'TCF', '+1', line=401)

W('01,3134', 0o10247, '', 'CCS', 'PRIORITY +48D', line=403)
W('01,3135', 0o03171, '', 'TC', 'EJ1', line=404)
W('01,3136', 0o05705, '', 'TC', 'CCSHOLE', line=405)
W('01,3137', 0o13140, '', 'TCF', '+1', line=406)

W('01,3140', 0o10263, '', 'CCS', 'PRIORITY +60D', line=408)
W('01,3141', 0o03171, '', 'TC', 'EJ1', line=409)
W('01,3142', 0o05705, '', 'TC', 'CCSHOLE', line=410)
W('01,3143', 0o13144, '', 'TCF', '+1', line=411)

W('01,3144', 0o10277, '', 'CCS', 'PRIORITY +72D', line=413)
W('01,3145', 0o03171, '', 'TC', 'EJ1', line=414)
W('01,3146', 0o05705, '', 'TC', 'CCSHOLE', line=415)
W('01,3147', 0o13150, '', 'TCF', '+1', line=416)

W('01,3150', 0o10313, '', 'CCS', 'PRIORITY +84D', line=418)
# Page 1114
W('01,3151', 0o03171, '', 'TC', 'EJ1', line=420)
W('01,3152', 0o05705, '', 'TC', 'CCSHOLE', line=421)
W('01,3153', 0o13154, '', 'TCF', '+1', line=422)

# Page 1115
# EVALUATE THE RESULTS OF THE SCAN.

W('01,3154', 0o10131, '', 'CCS', 'BUF +1', 'SEE IF THERE ARE ANY ACTIVE JOBS WAITING', line=427)
W('01,3155', 0o05705, '', 'TC', 'CCSHOLE', line=428)
W('01,3156', 0o05705, '', 'TC', 'CCSHOLE', line=429)

W('01,3157', 0o13161, '', 'TCF', '+2', line=431)
W('01,3160', 0o13206, '', 'TCF', 'DUMMYJOB', line=432)
W('01,3161', 0o10130, '', 'CCS', 'BUF', 'BUF IS ZERO IS THIS IS A PRIOCHNG AND', line=433)
W('01,3162', 0o13164, '', 'TCF', '+2', 'CHANGED PRIORITY IS STILL HIGHEST.', line=434)
W('01,3163', 0o12764, '', 'TCF', 'ENDPRCHG -1', line=435)

W('01,3164', 0o50000, '', 'INDEX', 'A', 'OTHERWISE, SET NEWJOB TO THE RELATIVE', line=437)
W('01,3165', 0o27777, '', 'CAF', '0 -1', "ADDRESS OF THE NEW JOB'S CORE SET.", line=438)
W('01,3166', 0o63132, '', 'AD', '-CCSPR', line=439)
W('01,3167', 0o54067, '', 'TS', 'NEWJOB', line=440)
W('01,3170', 0o12704, '', 'TCF', 'CHANJOB -2', line=441)

W('01,3171', 0o54132, 'EJ1', 'TS', 'BUF +2', line=443)
W('01,3172', 0o60131, '', 'AD', 'BUF +1', '- OLD HIGH PRIORITY.', line=444)
W('01,3173', 0o10000, '', 'CCS', 'A', line=445)
W('01,3174', 0o40132, '', 'CS', 'BUF +2', line=446)
W('01,3175', 0o13201, '', 'TCF', 'EJ2', 'NEW HIGH PRIORITY.', line=447)
W('01,3176', 0o13177, '', 'NOOP', line=448)
W('01,3177', 0o50002, '', 'INDEX', 'Q', line=449)
W('01,3200', 0o00002, '', 'TC', '2', 'PROCEED WITH SEARCH.', line=450)

W('01,3201', 0o54131, 'EJ2', 'TS', 'BUF +1', line=452)
W('01,3202', 0o00006, '', 'EXTEND', line=453)
W('01,3203', 0o22130, '', 'QXCH', 'BUF', 'FOR LOCATING CCS PRIORITY + X INSTR.', line=454)
W('01,3204', 0o50130, '', 'INDEX', 'BUF', line=455)
W('01,3205', 0o00002, '', 'TC', '2', line=456)

# Page 1116
# IDLING AND COMPUTER ACTIVITY (GREEN) LIGHT MAINTENANCE. THE IDLING ROUTINE IS NOT A JOB IN ITSELF,
# BUT RATHER A SUBROUTINE OF THE EXECUTIVE.

#   EBANK= SELFRET  # SELF-CHECK STORAGE IN EBANK.

W('01,3206', 0o44755, 'DUMMYJOB', 'CS', 'ZERO', 'SET NEWJOB TO -0 FOR IDLING.', line=464)
W('01,3207', 0o54067, '', 'TS', 'NEWJOB', line=465)
W('01,3210', 0o00003, '', 'RELINT', line=466)
W('01,3211', 0o44752, '', 'CS', 'TWO', 'TURN OFF THE ACTIVITY LIGHT.', line=467)
W('01,3212', 0o00006, '', 'EXTEND', line=468)
W('01,3213', 0o03011, '', 'WAND', 'DSALMOUT', line=469)
W('01,3214', 0o10067, 'ADVAN', 'CCS', 'NEWJOB', 'IS THE NEWJOB ACTIVE?', line=470)
W('01,3215', 0o13011, '', 'TCF', 'NUCHANG2', 'YES... ONE REQUIRING A CHANGE JOB.', line=471)
W('01,3216', 0o34752, '', 'CAF', 'TWO', 'NEW JOB ALREADY IN POSITION FOR', line=472)
W('01,3217', 0o13225, '', 'TCF', 'NUDIRECT', 'EXECUTION', line=473)

W('01,3220', 0o31361, '', 'CA', 'SELFRET', line=475)
W('01,3221', 0o54001, '', 'TS', 'L', 'PUT RETURN ADDRESS IN L.', line=476)
W('01,3222', 0o33224, '', 'CAF', 'SELFBANK', line=477)
W('01,3223', 0o15166, '', 'TCF', 'SUPDXCHZ +1', 'AND DISPATCH JOB.', line=478)

#   EBANK= SELFRET
W('01,3224', 0o66102, 'SELFBANK', 'BBCON', 'SELFCHK', kind='data', line=481)

W('01,3225', 0o00006, 'NUDIRECT', 'EXTEND', '', 'TURN THE GREEN LIGHT BACK ON.', line=483)
W('01,3226', 0o05011, '', 'WOR', 'DSALMOUT', line=484)
W('01,3227', 0o52165, '', 'DXCH', 'LOC', 'JOBS STARTED IN THIS FASHION MUST BE', line=485)
W('01,3230', 0o15165, '', 'TCF', 'SUPDXCHZ', line=486)

#   BLOCK 2  # IN FIXED-FIXED SO OTHERS MAY USE.

#   COUNT* $$/EXEC

# SUPDXCHZ -- ROUTINE TO TRANSFER TO SUPEBANK.
# CALLING SEQUENCE:
# TCF     SUPDXCHZ        # WITH 2CADR OF DESIRED LOCATION IN A + L.

W('5165', 0o56001, 'SUPDXCHZ', 'XCH', 'L', 'BASIC.', line=496)
W('5166', 0o00006, '', 'EXTEND', line=497)
W('5167', 0o01007, '', 'WRITE', 'SUPERBNK', line=498)
W('5170', 0o54006, '', 'TS', 'BBANK', line=499)
W('5171', 0o00001, '', 'TC', 'L', line=500)

W('5172', 0o77677, 'NEG100', 'OCT', '77677', kind='data', line=502)
