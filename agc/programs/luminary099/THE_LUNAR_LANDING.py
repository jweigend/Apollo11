"""THE_LUNAR_LANDING.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/THE_LUNAR_LANDING.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 785-792 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('THE_LUNAR_LANDING', 'THE_LUNAR_LANDING.agc', 'Luminary099', pages='785-792')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     THE_LUNAR_LANDING.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche<hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        785-792
# Mod history:  2009-05-20 HG   Transcribed from page images.
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

# Page 785
#   BANK 32
#   SETLOC F2DPS*32
#   BANK

#   EBANK= E2DPS

# *************************************
# P63: THE LUNAR LANDING, BRAKING PHASE
# *************************************

#   COUNT* $$/P63

W('32,2776', 0o05353, 'P63LM', 'TC', 'PHASCHNG', line=40)
W('32,2777', 0o04024, '', 'OCT', '04024', kind='data', line=41)

W('32,3000', 0o04616, '', 'TC', 'BANKCALL', 'DO IMU STATUS CHECK ROUTINE R02', line=43)
W('32,3001', 0o11254, '', 'CADR', 'R02BOTH', kind='data', line=44)

W('32,3002', 0o33253, '', 'CAF', 'P63ADRES', 'INITIALIZE WHICH FOR BURNBABY', line=46)
W('32,3003', 0o55455, '', 'TS', 'WHICH', line=47)

W('32,3004', 0o32000, '', 'CAF', 'DPSTHRSH', 'INITIALIZE DVMON', line=49)
W('32,3005', 0o55251, '', 'TS', 'DVTHRUSH', line=50)
W('32,3006', 0o34751, '', 'CAF', 'FOUR', line=51)
W('32,3007', 0o55515, '', 'TS', 'DVCNTR', line=52)

W('32,3010', 0o44753, '', 'CS', 'ONE', 'INITIALIZE WCHPHASE AND FLPASS0', line=54)
W('32,3011', 0o55351, '', 'TS', 'WCHPHASE', line=55)

W('32,3012', 0o34755, '', 'CA', 'ZERO', line=57)
W('32,3013', 0o55623, '', 'TS', 'FLPASS0', line=58)

W('32,3014', 0o44736, '', 'CS', 'BIT14', line=60)
W('32,3015', 0o00006, '', 'EXTEND', line=61)
W('32,3016', 0o03012, '', 'WAND', 'CHAN12', 'REMOVE TRACK-ENABLE DISCRETE.', line=62)

W('32,3017', 0o06037, 'FLAGORGY', 'TC', 'INTPRET', 'DIONYSIAN FLAG WAVING', line=64)
W('32,3020', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=65)
W('32,3021', 0o02663, '', '', 'NOTHROTL', kind='operand', line=66)
W('32,3022', 0o03271, '', '', 'REDFLAG', kind='operand', line=67)
W('32,3023', 0o43014, '', 'CLEAR', 'SET', kind='interp', line=68)
W('32,3024', 0o05660, '', '', 'LRBYPASS', kind='operand', line=69)
W('32,3025', 0o03067, '', '', 'MUNFLAG', kind='operand', line=70)
W('32,3026', 0o43014, '', 'CLEAR', 'CLEAR', kind='interp', line=71)
W('32,3027', 0o00266, '', '', 'P25FLAG', 'TERMINATE P25 IF IT IS RUNNING.', kind='operand', line=72)
W('32,3030', 0o00270, '', '', 'RNDVZFLG', 'TERMINATE P20 IF IT IS RUNNING', kind='operand', line=73)

# ********************************

W('32,3031', 0o77201, 'IGNALG', 'SETPD', 'VLOAD', 'FIRST SET UP INPUTS FOR RP-TO-R:-', kind='interp', line=77)
# Page 786
W('32,3032', 0o00001, '', '', '0', '  AT 0D LANDING SITE IN MOON FIXED FRAME', kind='operand', line=79)
W('32,3033', 0o02023, '', '', 'RLS', '  AT 6D ESTIMATED TIME OF LANDING', kind='operand', line=80)
W('32,3034', 0o41525, '', 'PDDL', 'PUSH', '  MPAC NON-ZERO TO INDICATE LUNAR CASE', kind='interp', line=81)
W('32,3035', 0o02401, '', '', 'TLAND', kind='operand', line=82)
W('32,3036', 0o37625, '', 'STCALL', 'TPIP', 'ALSO SET TPIP FOR FIRST GUIDANCE PASS', kind='interp', line=83)
W('32,3037', 0o55716, '', '', 'RP-TO-R', kind='operand', line=84)
W('32,3040', 0o64312, '', 'VSL4', 'MXV', kind='interp', line=85)
W('32,3041', 0o01734, '', '', 'REFSMMAT', kind='operand', line=86)
W('32,3042', 0o37635, '', 'STCALL', 'LAND', kind='interp', line=87)
W('32,3043', 0o46432, '', '', 'GUIDINIT', 'GUIDINIT INITIALIZES WM AND /LAND/', kind='operand', line=88)
W('32,3044', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=89)
W('32,3045', 0o02401, '', '', 'TLAND', kind='operand', line=90)
W('32,3046', 0o25260, '', '', 'GUIDDURN', kind='operand', line=91)
W('32,3047', 0o34041, '', 'STCALL', 'TDEC1', 'INTEGRATE STATE FORWARD TO THAT TIME', kind='interp', line=92)
W('32,3050', 0o27057, '', '', 'LEMPREC', kind='operand', line=93)
W('32,3051', 0o77331, '', 'SSP', 'VLOAD', kind='interp', line=94)
W('32,3052', 0o03647, '', '', 'NIGNLOOP', kind='operand', line=95)
W('32,3053', 0o00050, '', '', '40D', kind='operand', line=96)
W('32,3054', 0o06520, '', '', 'UNITX', kind='operand', line=97)
W('32,3055', 0o26603, '', 'STOVL', 'CG', kind='interp', line=98)
W('32,3056', 0o06516, '', '', 'UNITY', kind='operand', line=99)
W('32,3057', 0o26611, '', 'STOVL', 'CG +6', kind='interp', line=100)
W('32,3060', 0o06514, '', '', 'UNITZ', kind='operand', line=101)
W('32,3061', 0o16617, '', 'STODL', 'CG +14', kind='interp', line=102)
W('32,3062', 0o25256, '', '', '99999CON', kind='operand', line=103)
W('32,3063', 0o27665, '', 'STOVL', 'DELTAH', 'INITIALIZE DELTAH FOR V16N68 DISPLAY', kind='interp', line=104)
W('32,3064', 0o06522, '', '', 'ZEROVECS', kind='operand', line=105)
W('32,3065', 0o17254, '', 'STODL', 'UNFC/2', 'INITIALIZE TRIM VELOCITY CORRECTION TERM', kind='interp', line=106)
W('32,3066', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=107)
W('32,3067', 0o03643, '', 'STORE', 'TTF/8', kind='interp', line=108)

W('32,3070', 0o77745, 'IGNALOOP', 'DLOAD', kind='interp', line=110)
W('32,3071', 0o00015, '', '', 'TAT', kind='operand', line=111)
W('32,3072', 0o27561, '', 'STOVL', 'PIPTIME1', kind='interp', line=112)
W('32,3073', 0o00017, '', '', 'RATT1', kind='operand', line=113)
W('32,3074', 0o64312, '', 'VSL4', 'MXV', kind='interp', line=114)
W('32,3075', 0o01734, '', '', 'REFSMMAT', kind='operand', line=115)
W('32,3076', 0o37521, '', 'STCALL', 'R', kind='interp', line=116)
W('32,3077', 0o67130, '', '', 'MUNGRAV', kind='operand', line=117)
W('32,3100', 0o35237, '', 'STCALL', 'GDT/2', kind='interp', line=118)
W('32,3101', 0o62454, '', '', '?GUIDSUB', 'WHICH DELIVERS N PASSES OF GUIDANCE', kind='operand', line=119)

# DDUMCALC IS PROGRAMMED AS FOLLOWS:-
# 2                                           ___
# (RIGNZ - RGU )/16 + 16(RGU  )KIGNY/B8 + (RGU - RIGNX)KIGNX/B4 + (ABVAL(VGU) - VIGN)KIGNV/B4
# 2             1                 0
# DDUM = -------------------------------------------------------------------------------------------
# 10
# 2   (VGU - 16 VGU KIGNX/B4)
# 2        0
# Page 787 new page is actually one line earlier but this would put the indices on a separate line
# disconnected from their respective variables
# THE NUMERATOR IS SCALED IN METERS AT 2(28).  THE DENOMINATOR IS A VELOCITY IN UNITS OF 2(10) M/CS.
# THE QUOTIENT IS THUS A TIME IN UNITS OF 2(18) CENTISECONDS.  THE FINAL SHIFT RESCALES TO UNITS OF 2(28) CS.
# THERE IS NO DAMPING FACTOR.  THE CONSTANTS KIGNX/B4, KIGNY/B8 AND KIGNV/B4 ARE ALL NEGATIVE IN SIGN.

W('32,3102', 0o55646, 'DDUMCALC', 'TS', 'NIGNLOOP', line=135)
W('32,3103', 0o06037, '', 'TC', 'INTPRET', line=136)
W('32,3104', 0o57345, '', 'DLOAD', 'DMPR', 'FORM DENOMINATOR FIRST', kind='interp', line=137)
W('32,3105', 0o03627, '', '', 'VGU', kind='operand', line=138)
W('32,3106', 0o02501, '', '', 'KIGNX/B4', kind='operand', line=139)
W('32,3107', 0o44232, '', 'SL4R', 'BDSU', kind='interp', line=140)
W('32,3110', 0o03633, '', '', 'VGU +4', kind='operand', line=141)
W('32,3111', 0o45325, '', 'PDDL', 'DSU', kind='interp', line=142)
W('32,3112', 0o02477, '', '', 'RIGNZ', kind='operand', line=143)
W('32,3113', 0o02643, '', '', 'RGU +4', kind='operand', line=144)
W('32,3114', 0o65222, '', 'SR4R', 'PDDL', kind='interp', line=145)
W('32,3115', 0o02641, '', '', 'RGU +2', kind='operand', line=146)
W('32,3116', 0o57316, '', 'DSQ', 'DMPR', kind='interp', line=147)
W('32,3117', 0o02503, '', '', 'KIGNY/B8', kind='operand', line=148)
W('32,3120', 0o65232, '', 'SL4R', 'PDDL', kind='interp', line=149)
W('32,3121', 0o02637, '', '', 'RGU', kind='operand', line=150)
W('32,3122', 0o57225, '', 'DSU', 'DMPR', kind='interp', line=151)
W('32,3123', 0o02475, '', '', 'RIGNX', kind='operand', line=152)
W('32,3124', 0o02501, '', '', 'KIGNX/B4', kind='operand', line=153)
W('32,3125', 0o51515, '', 'PDVL', 'ABVAL', kind='interp', line=154)
W('32,3126', 0o03627, '', '', 'VGU', kind='operand', line=155)
W('32,3127', 0o57225, '', 'DSU', 'DMPR', kind='interp', line=156)
W('32,3130', 0o02473, '', '', 'VIGN', kind='operand', line=157)
W('32,3131', 0o02505, '', '', 'KIGNV/B4', kind='operand', line=158)
W('32,3132', 0o43215, '', 'DAD', 'DAD', kind='interp', line=159)
W('32,3133', 0o56215, '', 'DAD', 'DDV', kind='interp', line=160)
W('32,3134', 0o77661, '', 'SRR', kind='interp', line=161)
W('32,3135', 0o21613, '', '', '10D', kind='operand', line=162)

W('32,3136', 0o43206, '', 'PUSH', 'DAD', kind='interp', line=164)
W('32,3137', 0o03561, '', '', 'PIPTIME1', kind='operand', line=165)
W('32,3140', 0o14041, '', 'STODL', 'TDEC1', 'STORE NEW GUESS FOR NEXT INTEGRATION', kind='interp', line=166)
W('32,3141', 0o45246, '', 'ABS', 'DSU', kind='interp', line=167)
W('32,3142', 0o25262, '', '', 'DDUMCRIT', kind='operand', line=168)
W('32,3143', 0o45040, '', 'BMN', 'CALL', kind='interp', line=169)
W('32,3144', 0o65163, '', '', 'DDUMGOOD', kind='operand', line=170)
W('32,3145', 0o27414, '', '', 'INTSTALL', kind='operand', line=171)
W('32,3146', 0o43014, '', 'SET', 'SET', kind='interp', line=172)
W('32,3147', 0o01473, '', '', 'INTYPFLG', kind='operand', line=173)
W('32,3150', 0o00063, '', '', 'MOONFLAG', kind='operand', line=174)
W('32,3151', 0o77745, '', 'DLOAD', kind='interp', line=175)
W('32,3152', 0o03561, '', '', 'PIPTIME1', kind='operand', line=176)
W('32,3153', 0o25517, '', 'STOVL', 'TET', 'HOPEFULLY ?GUIDSUB DID NOT', kind='interp', line=177)
W('32,3154', 0o00017, '', '', 'RATT1', '  CLOBBER RATT1 AND VATT1', kind='operand', line=178)
# Page 788
W('32,3155', 0o25535, '', 'STOVL', 'RCV', kind='interp', line=180)
W('32,3156', 0o00025, '', '', 'VATT1', kind='operand', line=181)
W('32,3157', 0o35543, '', 'STCALL', 'VCV', kind='interp', line=182)
W('32,3160', 0o27107, '', '', 'INTEGRVS', kind='operand', line=183)
W('32,3161', 0o77650, '', 'GOTO', kind='interp', line=184)
W('32,3162', 0o65070, '', '', 'IGNALOOP', kind='operand', line=185)

W('32,3163', 0o54335, 'DDUMGOOD', 'SLOAD', 'SR', kind='interp', line=187)
W('32,3164', 0o03423, '', '', 'ZOOMTIME', kind='operand', line=188)
W('32,3165', 0o20617, '', '', '14D', kind='operand', line=189)
W('32,3166', 0o77621, '', 'BDSU', kind='interp', line=190)
W('32,3167', 0o00041, '', '', 'TDEC1', kind='operand', line=191)
W('32,3170', 0o27442, '', 'STOVL', 'TIG', 'COMPUTE DISTANCE LANDING SITE WILL BE', kind='interp', line=192)
W('32,3171', 0o03527, '', '', 'V', "  OUT OF LM'S ORBITAL PLANE AT IGNITION:", kind='operand', line=193)
W('32,3172', 0o53435, '', 'VXV', 'UNIT', '  SIGN IS + IF LANDING SITE IS TO THE', kind='interp', line=194)
W('32,3173', 0o03521, '', '', 'R', '  RIGHT, NORTH; - IF TO THE LEFT, SOUTH.', kind='operand', line=195)
W('32,3174', 0o72441, '', 'DOT', 'SL1', kind='interp', line=196)
W('32,3175', 0o03635, '', '', 'LAND', kind='operand', line=197)
W('32,3176', 0o26627, 'R60INIT', 'STOVL', 'OUTOFPLN', 'INITIALIZATION FOR CALCMANU', kind='interp', line=198)
W('32,3177', 0o03254, '', '', 'UNFC/2', kind='operand', line=199)
W('32,3200', 0o02631, '', 'STORE', 'R60VSAVE', 'STORE UNFC/2 TEMPORARILY IN R60SAVE', kind='interp', line=200)
W('32,3201', 0o77776, '', 'EXIT', kind='interp', line=201)
# *******************************************

W('32,3202', 0o05353, 'IGNALGRT', 'TC', 'PHASCHNG', 'PREVENT REPEATING IGNALG', line=204)
W('32,3203', 0o04024, '', 'OCT', '04024', kind='data', line=205)

W('32,3204', 0o44362, 'ASTNCLOK', 'CS', 'ASTNDEX', line=207)
W('32,3205', 0o04616, '', 'TC', 'BANKCALL', line=208)
W('32,3206', 0o74664, '', 'CADR', 'STCLOK2', kind='data', line=209)
W('32,3207', 0o15155, '', 'TCF', 'ENDOFJOB', 'RETURN IN NEW JOB AND IN EBANK FIVE', line=210)

W('32,3210', 0o06037, 'ASTNRET', 'TC', 'INTPRET', line=212)
W('32,3211', 0o47131, '', 'SSP', 'RTB', 'GO PICK UP DISPLAY AT END OF R51:', kind='interp', line=213)
W('32,3212', 0o02747, '', '', 'QMAJ', '  "PROCEED" WILL DO A FINE ALIGNMENT', kind='operand', line=214)
W('32,3213', 0o65215, '', 'FCADR', 'P63SPOT2', '  " ENTER " WILL RETURN TO P63SPOT2', kind='data', line=215)
W('32,3214', 0o31135, '', '', 'R51P63', kind='operand', line=216)
W('32,3215', 0o53575, 'P63SPOT2', 'VLOAD', 'UNIT', 'INITIALIZE KALCMANU FOR BURN ATTITUDE', kind='interp', line=217)
W('32,3216', 0o02631, '', '', 'R60VSAVE', kind='operand', line=218)
W('32,3217', 0o27773, '', 'STOVL', 'POINTVSM', kind='interp', line=219)
W('32,3220', 0o06520, '', '', 'UNITX', kind='operand', line=220)
W('32,3221', 0o03765, '', 'STORE', 'SCAXIS', kind='interp', line=221)
W('32,3222', 0o77776, '', 'EXIT', kind='interp', line=222)

W('32,3223', 0o35016, '', 'CAF', 'EBANK7', line=224)
W('32,3224', 0o54003, '', 'TS', 'EBANK', line=225)

W('32,3225', 0o00004, '', 'INHINT', line=227)
W('32,3226', 0o04674, '', 'TC', 'IBNKCALL', line=228)
W('32,3227', 0o40142, '', 'CADR', 'PFLITEDB', kind='data', line=229)
# Page 789
W('32,3230', 0o00003, '', 'RELINT', line=231)

W('32,3231', 0o04616, '', 'TC', 'BANKCALL', line=233)
W('32,3232', 0o54123, '', 'CADR', 'R60LEM', kind='data', line=234)

W('32,3233', 0o05353, '', 'TC', 'PHASCHNG', 'PREVENT RECALLING R60', line=236)
W('32,3234', 0o04024, '', 'OCT', '04024', kind='data', line=237)

W('32,3235', 0o34746, 'P63SPOT3', 'CA', 'BIT6', 'IS THE LR ANTENNA IN POSITION 1 YET', line=239)
W('32,3236', 0o00006, '', 'EXTEND', line=240)
W('32,3237', 0o02033, '', 'RAND', 'CHAN33', line=241)
W('32,3240', 0o00006, '', 'EXTEND', line=242)
W('32,3241', 0o13247, '', 'BZF', 'P63SPOT4', 'BRANCH IF ANTENNA ALREADY IN POSITION 1', line=243)

W('32,3242', 0o33254, '', 'CAF', 'CODE500', 'ASTRONAUT:    PLEASE CRANK THE', line=245)
W('32,3243', 0o04616, '', 'TC', 'BANKCALL', '              SILLY THING AROUND', line=246)
W('32,3244', 0o20623, '', 'CADR', 'GOPERF1', kind='data', line=247)
W('32,3245', 0o16001, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=248)
W('32,3246', 0o13235, '', 'TCF', 'P63SPOT3', "PROCEED       SEE IF HE'S LYING", line=249)

W('32,3247', 0o04616, 'P63SPOT4', 'TC', 'BANKCALL', 'ENTER         INITIALIZE LANDING RADAR', line=251)
W('32,3250', 0o67721, '', 'CADR', 'SETPOS1', kind='data', line=252)

W('32,3251', 0o04635, '', 'TC', 'POSTJUMP', 'OFF TO SEE THE WIZARD...', line=254)
W('32,3252', 0o74126, '', 'CADR', 'BURNBABY', kind='data', line=255)

# ---------------------------------

# CONSTANTS FOR P63LM AND IGNALG

W('32,3253', 0o02076, 'P63ADRES', 'GENADR', 'P63TABLE', kind='data', line=261)

S('ASTNDEX', 'equals', 0o4362, line=263)  # OCT 25:  INDEX FOR CLOKTASK

W('32,3254', 0o00500, 'CODE500', 'OCT', '00500', kind='data', line=265)

W('32,3255', 0o00035, '99999CON', '2DEC', '30479.7 B-24', kind='data', line=267)
W('32,3256', 0o30373, kind='data', line=267)

W('32,3257', 0o00004, 'GUIDDURN', '2DEC', '+66440', 'GUIDDURN      +6.64400314 E+2', kind='data', line=269)
W('32,3260', 0o01610, kind='data', line=269)
W('32,3261', 0o00000, 'DDUMCRIT', '2DEC', '+8 B-28', 'CRITERION FOR IGNALG CONVERGENCE', kind='data', line=270)
W('32,3262', 0o00010, kind='data', line=270)

# Page 790
# --------------------------------

# Page 791
# *************************
# P68: LANDING CONFIRMATION
# *************************

#   BANK 31
#   SETLOC F2DPS*31
#   BANK

#   COUNT* $$/P6567

W('31,2144', 0o05353, 'LANDJUNK', 'TC', 'PHASCHNG', line=286)
W('31,2145', 0o04024, '', 'OCT', '04024', kind='data', line=287)

W('31,2146', 0o00004, '', 'INHINT', line=289)
W('31,2147', 0o04616, '', 'TC', 'BANKCALL', 'ZERO ATTITUDE ERROR', line=290)
W('31,2150', 0o40153, '', 'CADR', 'ZATTEROR', kind='data', line=291)

W('31,2151', 0o04616, '', 'TC', 'BANKCALL', 'SET 5 DEGREE DEADBAND', line=293)
W('31,2152', 0o40127, '', 'CADR', 'SETMAXDB', kind='data', line=294)

W('31,2153', 0o06037, '', 'TC', 'INTPRET', 'TO INTERPRETIVE AS TIME IS NOT CRITICAL', line=296)
W('31,2154', 0o43014, '', 'SET', 'CLEAR', kind='interp', line=297)
W('31,2155', 0o04067, '', '', 'SURFFLAG', kind='operand', line=298)
W('31,2156', 0o04666, '', '', 'LETABORT', kind='operand', line=299)
W('31,2157', 0o77214, '', 'SET', 'VLOAD', kind='interp', line=300)
W('31,2160', 0o05062, '', '', 'APSFLAG', kind='operand', line=301)
W('31,2161', 0o01221, '', '', 'RN', kind='operand', line=302)
W('31,2162', 0o16032, '', 'STODL', 'ALPHAV', kind='interp', line=303)
W('31,2163', 0o01235, '', '', 'PIPTIME', kind='operand', line=304)
W('31,2164', 0o45014, '', 'SET', 'CALL', kind='interp', line=305)
W('31,2165', 0o01463, '', '', 'LUNAFLAG', kind='operand', line=306)
W('31,2166', 0o26351, '', '', 'LAT-LONG', kind='operand', line=307)
W('31,2167', 0o77201, '', 'SETPD', 'VLOAD', 'COMPUTE RLS AND STORE IT AWAY', kind='interp', line=308)
W('31,2170', 0o00001, '', '', '0', kind='operand', line=309)
W('31,2171', 0o01221, '', '', 'RN', kind='operand', line=310)
W('31,2172', 0o65352, '', 'VSL2', 'PDDL', kind='interp', line=311)
W('31,2173', 0o01235, '', '', 'PIPTIME', kind='operand', line=312)
W('31,2174', 0o45006, '', 'PUSH', 'CALL', kind='interp', line=313)
W('31,2175', 0o51670, '', '', 'R-TO-RP', kind='operand', line=314)
W('31,2176', 0o02023, '', 'STORE', 'RLS', kind='interp', line=315)
W('31,2177', 0o77776, '', 'EXIT', kind='interp', line=316)
W('31,2200', 0o32215, '', 'CAF', 'V06N43*', 'ASTRONAUT:  NOW LOOK WHERE YOU ENDED UP', line=317)
W('31,2201', 0o04616, '', 'TC', 'BANKCALL', line=318)
W('31,2202', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=319)
W('31,2203', 0o16001, '', 'TCF', 'GOTOPOOH', 'TERMINATE', line=320)
W('31,2204', 0o12206, '', 'TCF', '+2', 'PROCEED', line=321)
W('31,2205', 0o12200, '', 'TCF', '-5', 'RECYCLE', line=322)

W('31,2206', 0o06037, '', 'TC', 'INTPRET', line=324)
# Page 792
W('31,2207', 0o77775, '', 'VLOAD', '', 'INITIALIZE GSAV AND (USING REFMF)', kind='interp', line=326)
W('31,2210', 0o06520, '', '', 'UNITX', '  YNBSAV, ZNBSAV AND ATTFLAG FOR P57', kind='operand', line=327)
W('31,2211', 0o36231, '', 'STCALL', 'GSAV', kind='interp', line=328)
W('31,2212', 0o33506, '', '', 'REFMF', kind='operand', line=329)
W('31,2213', 0o77776, '', 'EXIT', kind='interp', line=330)

W('31,2214', 0o16001, '', 'TCF', 'GOTOPOOH', 'ASTRONAUT:  PLEASE SELECT P57', line=332)

W('31,2215', 0o01453, 'V06N43*', 'VN', '0643', kind='data', line=334)
