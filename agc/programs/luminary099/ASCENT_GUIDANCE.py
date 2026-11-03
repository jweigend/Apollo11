"""ASCENT_GUIDANCE.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/ASCENT_GUIDANCE.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 843-856 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('ASCENT_GUIDANCE', 'ASCENT_GUIDANCE.agc', 'Luminary099', pages='843-856')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     ASCENT_GUIDANCE.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        843-856
# Mod history:  2009-05-23 HG   Transcribed from page images.
# 2009-06-05 RSB  Fixed a couple of typos.
# 2009-06-07 RSB  Corrected a typo.
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

# Page 843
#   BANK 34
#   SETLOC ASCFILT
#   BANK

#   EBANK= DVCNTR

#   COUNT* $$/ASENT

W('34,3642', 0o05353, 'ATMAG', 'TC', 'PHASCHNG', line=38)
W('34,3643', 0o00035, '', 'OCT', '00035', kind='data', line=39)
W('34,3644', 0o06037, '', 'TC', 'INTPRET', line=40)
W('34,3645', 0o77614, '', 'BON', kind='interp', line=41)
W('34,3646', 0o04705, '', '', 'FLRCS', kind='operand', line=42)
W('34,3647', 0o60321, '', '', 'ASCENT', kind='operand', line=43)
W('34,3650', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=44)
W('34,3651', 0o03514, '', '', 'ABDVCONV', kind='operand', line=45)
W('34,3652', 0o26205, '', '', 'MINABDV', kind='operand', line=46)
W('34,3653', 0o43040, '', 'BMN', 'CLEAR', kind='interp', line=47)
W('34,3654', 0o60750, '', '', 'ASCTERM4', kind='operand', line=48)
W('34,3655', 0o04267, '', '', 'SURFFLAG', kind='operand', line=49)
W('34,3656', 0o67214, '', 'CLEAR', 'SLOAD', kind='interp', line=50)
W('34,3657', 0o02676, '', '', 'RENDWFLG', kind='operand', line=51)
W('34,3660', 0o31716, '', '', 'BIT3H', kind='operand', line=52)
W('34,3661', 0o77471, '', 'DDV', 'EXIT', kind='interp', line=53)
W('34,3662', 0o03514, '', '', 'ABDVCONV', kind='operand', line=54)
W('34,3663', 0o52155, '', 'DXCH', 'MPAC', line=55)
W('34,3664', 0o53641, '', 'DXCH', '1/DV3', line=56)
W('34,3665', 0o53637, '', 'DXCH', '1/DV2', line=57)
W('34,3666', 0o53635, '', 'DXCH', '1/DV1', line=58)
W('34,3667', 0o53571, '', 'DXCH', '1/DV0', line=59)
W('34,3670', 0o06037, '', 'TC', 'INTPRET', line=60)
W('34,3671', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=61)
W('34,3672', 0o03571, '', '', '1/DV0', kind='operand', line=62)
W('34,3673', 0o03635, '', '', '1/DV1', kind='operand', line=63)
W('34,3674', 0o43215, '', 'DAD', 'DAD', kind='interp', line=64)
W('34,3675', 0o03637, '', '', '1/DV2', kind='operand', line=65)
W('34,3676', 0o03641, '', '', '1/DV3', kind='operand', line=66)
W('34,3677', 0o41205, '', 'DMP', 'DMP', kind='interp', line=67)
W('34,3700', 0o02265, '', '', 'VE', kind='operand', line=68)
W('34,3701', 0o21032, '', '', '2SEC(9)', kind='operand', line=69)
W('34,3702', 0o65252, '', 'SL3', 'PDDL', kind='interp', line=70)
W('34,3703', 0o02271, '', '', 'TBUP', kind='operand', line=71)
W('34,3704', 0o43342, '', 'SR1', 'DAD', kind='interp', line=72)
W('34,3705', 0o77625, '', 'DSU', kind='interp', line=73)
W('34,3706', 0o21027, '', '', '6SEC(18)', kind='operand', line=74)
W('34,3707', 0o16271, '', 'STODL', 'TBUP', kind='interp', line=75)
W('34,3710', 0o02265, '', '', 'VE', kind='operand', line=76)
W('34,3711', 0o56342, '', 'SR1', 'DDV', kind='interp', line=77)
W('34,3712', 0o02271, '', '', 'TBUP', kind='operand', line=78)
W('34,3713', 0o36263, '', 'STCALL', 'AT', kind='interp', line=79)
# Page 844
W('34,3714', 0o60321, '', '', 'ASCENT', kind='operand', line=81)
W('34,3715', 0o00004, 'BIT3H', 'OCT', '4', kind='data', line=82)

# Page 845
#   BANK 30
#   SETLOC ASENT
#   BANK
#   COUNT* $$/ASENT

W('30,2321', 0o51575, 'ASCENT', 'VLOAD', 'ABVAL', kind='interp', line=90)
W('30,2322', 0o03521, '', '', 'R', kind='operand', line=91)
W('30,2323', 0o26301, '', 'STOVL', '/R/MAG', kind='interp', line=92)
W('30,2324', 0o03726, '', '', 'ZAXIS1', kind='operand', line=93)
W('30,2325', 0o72441, '', 'DOT', 'SL1', kind='interp', line=94)
W('30,2326', 0o03527, '', '', 'V', 'Z.V = ZDOT*2(-8).', kind='operand', line=95)
W('30,2327', 0o26313, '', 'STOVL', 'ZDOT', 'ZDOT*2(-7)', kind='interp', line=96)
W('30,2330', 0o03726, '', '', 'ZAXIS1', kind='operand', line=97)
W('30,2331', 0o76435, '', 'VXV', 'VSL1', kind='interp', line=98)
W('30,2332', 0o03537, '', '', 'UNIT/R/', 'Z X UR = LAXIS*2(-2)', kind='operand', line=99)
W('30,2333', 0o02303, '', 'STORE', 'LAXIS', 'LAXIS*2(-1)', kind='interp', line=100)
W('30,2334', 0o72441, '', 'DOT', 'SL1', kind='interp', line=101)
W('30,2335', 0o03527, '', '', 'V', 'L.V = YDOT*2(-8).', kind='operand', line=102)
W('30,2336', 0o36311, '', 'STCALL', 'YDOT', 'YDOT * 2(-7)', kind='interp', line=103)
W('30,2337', 0o57312, '', '', 'YCOMP', kind='operand', line=104)
W('30,2340', 0o77775, '', 'VLOAD', kind='interp', line=105)
W('30,2341', 0o03563, '', '', 'GDT1/2', 'LOAD GDT1/2*2(-7) M/CS.', kind='operand', line=106)
W('30,2342', 0o50341, '', 'V/SC', 'DOT', kind='interp', line=107)
W('30,2343', 0o27147, '', '', '2SEC(18)', kind='operand', line=108)
W('30,2344', 0o03537, '', '', 'UNIT/R/', 'G.UR*2(9) = GR*2(9).', kind='operand', line=109)
W('30,2345', 0o47315, '', 'PDVL', 'VXV', 'STORE IN PDL(0)', kind='interp', line=110)
W('30,2346', 0o03537, '', '', 'UNIT/R/', 'LOAD UNIT/R/ *2(-1)', kind='operand', line=111)
W('30,2347', 0o03527, '', '', 'V', 'UR*2(-1) X V*2(-7) = H/R*2(-8).', kind='operand', line=112)
W('30,2350', 0o56236, '', 'VSQ', 'DDV', 'H(2)/R(2)*2(-16).', kind='interp', line=113)
W('30,2351', 0o02301, '', '', '/R/MAG', 'H(2)/R(3)*2(9).', kind='operand', line=114)
W('30,2352', 0o43352, '', 'SL1', 'DAD', kind='interp', line=115)
W('30,2353', 0o77626, '', 'STADR', kind='interp', line=116)
W('30,2354', 0o61462, '', 'STODL', 'GEFF', 'GEFF*2(10)m/CS/CS.', kind='interp', line=117)
W('30,2355', 0o02277, '', '', 'ZDOTD', kind='operand', line=118)
W('30,2356', 0o77625, '', 'DSU', kind='interp', line=119)
W('30,2357', 0o02313, '', '', 'ZDOT', kind='operand', line=120)
W('30,2360', 0o02343, '', 'STORE', 'DZDOT', 'DZDOT = (ZDOTD - ZDOT) * 2(7) M/CS.', kind='interp', line=121)
W('30,2361', 0o65361, '', 'VXSC', 'PDDL', kind='interp', line=122)
W('30,2362', 0o03726, '', '', 'ZAXIS1', kind='operand', line=123)
W('30,2363', 0o02275, '', '', 'YDOTD', kind='operand', line=124)
W('30,2364', 0o77625, '', 'DSU', kind='interp', line=125)
W('30,2365', 0o02311, '', '', 'YDOT', kind='operand', line=126)
W('30,2366', 0o02341, '', 'STORE', 'DYDOT', 'DYDOT = (YDOTD - YDOT) *2(7) M/CS.', kind='interp', line=127)
W('30,2367', 0o65361, '', 'VXSC', 'PDDL', kind='interp', line=128)
W('30,2370', 0o02303, '', '', 'LAXIS', kind='operand', line=129)
W('30,2371', 0o02273, '', '', 'RDOTD', kind='operand', line=130)
# Page 846
W('30,2372', 0o77625, '', 'DSU', kind='interp', line=132)
W('30,2373', 0o03474, '', '', 'RDOT', kind='operand', line=133)
W('30,2374', 0o02337, '', 'STORE', 'DRDOT', 'DRDOT = (RDOTD - RDOT) * 2(7) M/CS.', kind='interp', line=134)
W('30,2375', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=135)
W('30,2376', 0o03537, '', '', 'UNIT/R/', kind='operand', line=136)
W('30,2377', 0o76455, '', 'VAD', 'VSL1', kind='interp', line=137)
W('30,2400', 0o77626, '', 'STADR', kind='interp', line=138)
W('30,2401', 0o74131, '', 'STORE', 'VGVECT', 'VG = (DRDOT)R + (DVDOT)L + (DZDOT)Z.', kind='interp', line=139)
W('30,2402', 0o41345, '', 'DLOAD', 'DMP', 'LOAD TGO', kind='interp', line=140)
W('30,2403', 0o03517, '', '', 'TGO', 'TGO GEFF', kind='operand', line=141)
W('30,2404', 0o02315, '', '', 'GEFF', kind='operand', line=142)
W('30,2405', 0o76561, '', 'VXSC', 'VSL1', kind='interp', line=143)
W('30,2406', 0o03537, '', '', 'UNIT/R/', 'TGO GEFF UR', kind='operand', line=144)
W('30,2407', 0o77645, '', 'BVSU', kind='interp', line=145)
W('30,2410', 0o03646, '', '', 'VGVECT', 'COMPENSATED FOR GEFF', kind='operand', line=146)
W('30,2411', 0o03646, '', 'STORE', 'VGVECT', 'STORE FOR DOWNLINK', kind='interp', line=147)
W('30,2412', 0o76521, '', 'MXV', 'VSL1', 'GET VGBODY FOR N85 DISPLAY', kind='interp', line=148)
W('30,2413', 0o02146, '', '', 'XNBPIP', kind='operand', line=149)
W('30,2414', 0o27502, '', 'STOVL', 'VGBODY', kind='interp', line=150)
W('30,2415', 0o03646, '', '', 'VGVECT', kind='operand', line=151)
W('30,2416', 0o43046, '', 'ABVAL', 'BOFF', 'MAGNITUDE OF VGVECT', kind='interp', line=152)
W('30,2417', 0o04745, '', '', 'FLRCS', 'IF FLRCS=0,D0 NORMAL GUIDANCE', kind='operand', line=153)
W('30,2420', 0o60425, '', '', 'MAINENG', kind='operand', line=154)
W('30,2421', 0o77671, '', 'DDV', '', 'USE TGO=VG/AT WITH RCS', kind='interp', line=155)
W('30,2422', 0o20001, '', '', 'AT/RCS', kind='operand', line=156)
W('30,2423', 0o37517, '', 'STCALL', 'TGO', 'THIS WILL BE USED ON NEXT CYCLE', kind='interp', line=157)
W('30,2424', 0o60746, '', '', 'ASCTERM2', kind='operand', line=158)
W('30,2425', 0o41471, 'MAINENG', 'DDV', 'PUSH', 'VG/VE IN PDL(0)               (2)', kind='interp', line=159)
W('30,2426', 0o02265, '', '', 'VE', kind='operand', line=160)
W('30,2427', 0o44205, '', 'DMP', 'BDSU', '1 - KT VG/VE', kind='interp', line=161)
W('30,2430', 0o26201, '', '', 'KT1', kind='operand', line=162)
W('30,2431', 0o17771, '', '', 'NEARONE', kind='operand', line=163)
W('30,2432', 0o41205, '', 'DMP', 'DMP', 'TBUP VG(1-KT VG/VE)/VE        (0)', kind='interp', line=164)
W('30,2433', 0o02271, '', '', 'TBUP', '      = TGO', kind='operand', line=165)
W('30,2434', 0o77625, '', 'DSU', '', 'COMPENSATE FOR TAILOFF', kind='interp', line=166)
W('30,2435', 0o02267, '', '', 'TTO', kind='operand', line=167)
W('30,2436', 0o03517, '', 'STORE', 'TGO', kind='interp', line=168)
W('30,2437', 0o57461, '', 'SR', 'DCOMP', kind='interp', line=169)
W('30,2440', 0o20614, '', '', '11D', kind='operand', line=170)
W('30,2441', 0o17454, '', 'STODL', 'TTOGO', 'TGO *2(-28) CS', kind='interp', line=171)
W('30,2442', 0o03517, '', '', 'TGO', kind='operand', line=172)
W('30,2443', 0o45214, '', 'BON', 'DSU', kind='interp', line=173)
W('30,2444', 0o03710, '', '', 'IDLEFLAG', kind='operand', line=174)
W('30,2445', 0o60451, '', '', 'T2TEST', kind='operand', line=175)
W('30,2446', 0o21021, '', '', '4SEC(17)', '( TGO - 4 )*2(-17) CS.', kind='operand', line=176)
W('30,2447', 0o77640, '', 'BMN', kind='interp', line=177)
W('30,2450', 0o30355, '', '', 'ENGOFF', kind='operand', line=178)
W('30,2451', 0o77745, 'T2TEST', 'DLOAD', kind='interp', line=179)
W('30,2452', 0o03517, '', '', 'TGO', kind='operand', line=180)
W('30,2453', 0o50025, '', 'DSU', 'BMN', 'IF TGO - T2 NEG., GO TO CMPONENT', kind='interp', line=181)
# Page 847
W('30,2454', 0o21023, '', '', 'T2A', kind='operand', line=183)
W('30,2455', 0o60612, '', '', 'CMPONENT', kind='operand', line=184)
W('30,2456', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=185)
W('30,2457', 0o02271, '', '', 'TBUP', kind='operand', line=186)
W('30,2460', 0o03517, '', '', 'TGO', kind='operand', line=187)
W('30,2461', 0o45071, '', 'DDV', 'CALL', '1- TGO/TBUP', kind='interp', line=188)
W('30,2462', 0o02271, '', '', 'TBUP', kind='operand', line=189)
W('30,2463', 0o61036, '', '', 'LOGSUB', kind='operand', line=190)
W('30,2464', 0o41461, '', 'SL', 'PUSH', '-L IN PDL(0)                  (2)', kind='interp', line=191)
W('30,2465', 0o20206, '', '', '5', kind='operand', line=192)
W('30,2466', 0o44265, '', 'BDDV', 'BDSU', '-TGO/L*2(-17)', kind='interp', line=193)
W('30,2467', 0o03517, '', '', 'TGO', kind='operand', line=194)
W('30,2470', 0o02271, '', '', 'TBUP', 'TBUP + TGO/L = D12*2(-17)', kind='operand', line=195)
W('30,2471', 0o43006, '', 'PUSH', 'BON', 'STORE IN PDL(2)               (4)', kind='interp', line=196)
W('30,2472', 0o04703, '', '', 'FLPC', 'IF FLPC = 1, GO TO CONST', kind='operand', line=197)
W('30,2473', 0o60502, '', '', 'NORATES', kind='operand', line=198)
W('30,2474', 0o45345, '', 'DLOAD', 'DSU', kind='interp', line=199)
W('30,2475', 0o03517, '', '', 'TGO', kind='operand', line=200)
W('30,2476', 0o21025, '', '', 'T3', kind='operand', line=201)
W('30,2477', 0o43044, '', 'BPL', 'SET', 'FLPC=1', kind='interp', line=202)
W('30,2500', 0o60510, '', '', 'RATES', kind='operand', line=203)
W('30,2501', 0o04463, '', '', 'FLPC', kind='operand', line=204)
W('30,2502', 0o77745, 'NORATES', 'DLOAD', kind='interp', line=205)
W('30,2503', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=206)
W('30,2504', 0o02351, '', 'STORE', 'PRATE', 'B = 0', kind='interp', line=207)
W('30,2505', 0o02353, '', 'STORE', 'YRATE', 'D = 0', kind='interp', line=208)
W('30,2506', 0o77650, '', 'GOTO', kind='interp', line=209)
W('30,2507', 0o60572, '', '', 'CONST', 'GO TO CONST', kind='operand', line=210)
W('30,2510', 0o45345, 'RATES', 'DLOAD', 'DSU', kind='interp', line=211)
W('30,2511', 0o03517, '', '', 'TGO', kind='operand', line=212)
W('30,2512', 0o00003, '', '', '02D', 'TGO - D12 = D21*2(-17)', kind='operand', line=213)
W('30,2513', 0o72406, '', 'PUSH', 'SL1', 'IN PDL(4)                     (6)', kind='interp', line=214)
W('30,2514', 0o52421, '', 'BDSU', 'SL3', '(1/2TGO - D21)*2(-13) = E * 2(-13)', kind='interp', line=215)
W('30,2515', 0o03517, '', '', 'TGO', '                              (8)', kind='operand', line=216)
W('30,2516', 0o41325, '', 'PDDL', 'DMP', 'IN PDL(6)', kind='interp', line=217)
W('30,2517', 0o03517, '', '', 'TGO', kind='operand', line=218)
W('30,2520', 0o03474, '', '', 'RDOT', 'RDOT TGO * 2(-24)', kind='operand', line=219)
W('30,2521', 0o45215, '', 'DAD', 'DSU', 'R + RDOT TGO', kind='interp', line=220)
W('30,2522', 0o02301, '', '', '/R/MAG', 'R + RDOT TGO - RCO', kind='operand', line=221)
W('30,2523', 0o03631, '', '', 'RCO', 'MPAC = -DR *2(-24).', kind='operand', line=222)
W('30,2524', 0o41325, '', 'PDDL', 'DMP', '-DR IN PDL(8)                 (10)', kind='interp', line=223)
W('30,2525', 0o02337, '', '', 'DRDOT', kind='operand', line=224)
W('30,2526', 0o00005, '', '', '04D', 'D21 DRDOT*2(-24)', kind='operand', line=225)
W('30,2527', 0o62415, '', 'DAD', 'SL2', '(D21 DRDOT-DR)*2(-22)         (8)', kind='interp', line=226)
W('30,2530', 0o56271, '', 'DDV', 'DDV', kind='interp', line=227)
W('30,2531', 0o00007, '', '', '06D', '(D21 DRDOT-DR)/E*2(-9)', kind='operand', line=228)
W('30,2532', 0o03517, '', '', 'TGO', kind='operand', line=229)
W('30,2533', 0o02351, '', 'STORE', 'PRATE', 'B * 2(8)', kind='interp', line=230)
W('30,2534', 0o71240, '', 'BMN', 'DLOAD', 'B>0 NOT PERMITTED', kind='interp', line=231)
W('30,2535', 0o60541, '', '', 'CHKBMAG', kind='operand', line=232)
# Page 848
W('30,2536', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=234)
W('30,2537', 0o36351, '', 'STCALL', 'PRATE', kind='interp', line=235)
W('30,2540', 0o60553, '', '', 'PROK', kind='operand', line=236)
W('30,2541', 0o56202, 'CHKBMAG', 'SR4', 'DDV', 'B*2(4)', kind='interp', line=237)
W('30,2542', 0o02271, '', '', 'TBUP', '(B / TAU) * 2(21)', kind='operand', line=238)
W('30,2543', 0o51025, '', 'DSU', 'BPL', kind='interp', line=239)
W('30,2544', 0o26203, '', '', 'PRLIMIT', '( B / TAU ) = 2(21) MAX.', kind='operand', line=240)
W('30,2545', 0o60553, '', '', 'PROK', kind='operand', line=241)
W('30,2546', 0o41345, '', 'DLOAD', 'DMP', kind='interp', line=242)
W('30,2547', 0o26203, '', '', 'PRLIMIT', kind='operand', line=243)
W('30,2550', 0o02271, '', '', 'TBUP', 'B MAX. * 2(4)', kind='operand', line=244)
W('30,2551', 0o77612, '', 'SL4', '', 'BMAX*2(8)', kind='interp', line=245)
W('30,2552', 0o02351, '', 'STORE', 'PRATE', kind='interp', line=246)
W('30,2553', 0o77745, 'PROK', 'DLOAD', kind='interp', line=247)
W('30,2554', 0o03517, '', '', 'TGO', kind='operand', line=248)
W('30,2555', 0o43205, '', 'DMP', 'DAD', 'YDOT TGO', kind='interp', line=249)
W('30,2556', 0o02311, '', '', 'YDOT', kind='operand', line=250)
W('30,2557', 0o02335, '', '', 'Y', 'Y + YDOT TGO', kind='operand', line=251)
W('30,2560', 0o65225, '', 'DSU', 'PDDL', 'Y + YDOT TGO - YCO', kind='interp', line=252)
W('30,2561', 0o03633, '', '', 'YCO', 'MPAC = - DY*(-24.) IN PDL(8)  (10)', kind='operand', line=253)
W('30,2562', 0o02341, '', '', 'DYDOT', kind='operand', line=254)
W('30,2563', 0o43205, '', 'DMP', 'DAD', 'D21 DYDOT - DY                (8)', kind='interp', line=255)
W('30,2564', 0o00005, '', '', '04D', kind='operand', line=256)
W('30,2565', 0o56312, '', 'SL2', 'DDV', '(D21 DYDOT - DY)/E*2(-9)', kind='interp', line=257)
W('30,2566', 0o40271, '', 'DDV', 'SETPD', '(D21 DYDOT - DY)/E TGO*2(8)', kind='interp', line=258)
W('30,2567', 0o03517, '', '', 'TGO', '      = D*2(8)', kind='operand', line=259)
W('30,2570', 0o00005, '', '', '04', kind='operand', line=260)
W('30,2571', 0o02353, '', 'STORE', 'YRATE', kind='interp', line=261)
W('30,2572', 0o41345, 'CONST', 'DLOAD', 'DMP', 'LOAD B*2(8)', kind='interp', line=262)
W('30,2573', 0o02351, '', '', 'PRATE', 'B D12*2(-9)', kind='operand', line=263)
W('30,2574', 0o00003, '', '', '02D', kind='operand', line=264)
W('30,2575', 0o56325, '', 'PDDL', 'DDV', 'D12 B IN PDL(4)       (6)', kind='interp', line=265)
W('30,2576', 0o02337, '', '', 'DRDOT', 'LOAD DRDOT*2(-7)', kind='operand', line=266)
W('30,2577', 0o00001, '', '', '00D', '-DRDOT/L*2(-7)', kind='operand', line=267)
W('30,2600', 0o45302, '', 'SR2', 'DSU', '(-DRDOT/L-D12 B)=A*2(-9)      (4)', kind='interp', line=268)
W('30,2601', 0o77626, '', 'STADR', kind='interp', line=269)
W('30,2602', 0o61432, '', 'STODL', 'PCONS', kind='interp', line=270)
W('30,2603', 0o02353, '', '', 'YRATE', 'D*2(8)', kind='operand', line=271)
W('30,2604', 0o65205, '', 'DMP', 'PDDL', 'D12 D,EXCH WITH -L IN PDL(0)  (2,2)', kind='interp', line=272)
W('30,2605', 0o60465, '', 'BDDV', 'SR2', '-DYDOT/L*2(-9)', kind='interp', line=273)
W('30,2606', 0o02341, '', '', 'DYDOT', kind='operand', line=274)
W('30,2607', 0o77625, '', 'DSU', '', '(-DYDOT/L-D12 D)=C*2(-9)', kind='interp', line=275)
W('30,2610', 0o00001, '', '', '00D', kind='operand', line=276)
W('30,2611', 0o02347, '', 'STORE', 'YCONS', kind='interp', line=277)
W('30,2612', 0o71201, 'CMPONENT', 'SETPD', 'DLOAD', kind='interp', line=278)
W('30,2613', 0o00001, '', '', '00D', kind='operand', line=279)
W('30,2614', 0o27147, '', '', '100CS', kind='operand', line=280)
W('30,2615', 0o77605, '', 'DMP', kind='interp', line=281)
W('30,2616', 0o02351, '', '', 'PRATE', 'B(T-T0)*2(-9)', kind='operand', line=282)
W('30,2617', 0o56215, '', 'DAD', 'DDV', '(A+B(T-T0))*2(-9)', kind='interp', line=283)
# Page 849
W('30,2620', 0o02345, '', '', 'PCONS', '(A+B(T-T0))/TBUP*2(8)', kind='operand', line=285)
W('30,2621', 0o02271, '', '', 'TBUP', kind='operand', line=286)
W('30,2622', 0o45352, '', 'SL1', 'DSU', kind='interp', line=287)
W('30,2623', 0o02315, '', '', 'GEFF', 'ATR*2(9)', kind='operand', line=288)
W('30,2624', 0o16357, '', 'STODL', 'ATR', kind='interp', line=289)
W('30,2625', 0o27147, '', '', '100CS', kind='operand', line=290)
W('30,2626', 0o43205, '', 'DMP', 'DAD', kind='interp', line=291)
W('30,2627', 0o02353, '', '', 'YRATE', kind='operand', line=292)
W('30,2630', 0o02347, '', '', 'YCONS', '(C+D(T-T0))*2(-9)', kind='operand', line=293)
W('30,2631', 0o72471, '', 'DDV', 'SL1', kind='interp', line=294)
W('30,2632', 0o02271, '', '', 'TBUP', kind='operand', line=295)
W('30,2633', 0o02355, '', 'STORE', 'ATY', 'ATY*2(9)', kind='interp', line=296)
W('30,2634', 0o65361, '', 'VXSC', 'PDDL', 'ATY UY*2(8)           (6)', kind='interp', line=297)
W('30,2635', 0o02303, '', '', 'LAXIS', kind='operand', line=298)
W('30,2636', 0o02357, '', '', 'ATR', kind='operand', line=299)
W('30,2637', 0o53361, '', 'VXSC', 'VAD', kind='interp', line=300)
W('30,2640', 0o03537, '', '', 'UNIT/R/', kind='operand', line=301)
W('30,2641', 0o41572, '', 'VSL1', 'PUSH', 'AH*2(9) IN PDL(0)     (6)', kind='interp', line=302)
W('30,2642', 0o65246, '', 'ABVAL', 'PDDL', 'AH(2) IN PDL(34)', kind='interp', line=303)
W('30,2643', 0o02263, '', '', 'AT', 'AHMAG IN PDL(6)       (8)', kind='operand', line=304)
W('30,2644', 0o45316, '', 'DSQ', 'DSU', '(AT(2)-AH(2))*2(18)', kind='interp', line=305)
W('30,2645', 0o00043, '', '', '34D', '=ATP2*2(18)', kind='operand', line=306)
W('30,2646', 0o41525, '', 'PDDL', 'PUSH', '                      (12)', kind='interp', line=307)
W('30,2647', 0o02263, '', '', 'AT', kind='operand', line=308)
W('30,2650', 0o45316, '', 'DSQ', 'DSU', '(AT(2)KR(2)-AH(2))*2(18)      (10)', kind='interp', line=309)
W('30,2651', 0o00043, '', '', '34D', '=ATP3*2(18)', kind='operand', line=310)
W('30,2652', 0o71240, '', 'BMN', 'DLOAD', 'IF ATP3 NEG,GO TO NO-ATP', kind='interp', line=311)
W('30,2653', 0o60657, '', '', 'NO-ATP', 'LOAD ATP2, IF ATP3 POS', kind='operand', line=312)
W('30,2654', 0o00011, '', '', '8D', kind='operand', line=313)
W('30,2655', 0o52166, '', 'SQRT', 'GOTO', 'ATP*2(9)', kind='interp', line=314)
W('30,2656', 0o60665, '', '', 'AIMER', kind='operand', line=315)
W('30,2657', 0o55345, 'NO-ATP', 'DLOAD', 'BDDV', 'KR AT/AH = KH         (8)', kind='interp', line=316)
W('30,2660', 0o00007, '', '', '6D', kind='operand', line=317)
W('30,2661', 0o77761, '', 'VXSC', '', 'KH AG*2(9)', kind='interp', line=318)
W('30,2662', 0o00001, '', '', '00D', kind='operand', line=319)
W('30,2663', 0o14001, '', 'STODL', '00D', 'STORE NEW AH IN PDL(0)', kind='interp', line=320)
W('30,2664', 0o06522, '', '', 'HI6ZEROS', kind='operand', line=321)
W('30,2665', 0o77765, 'AIMER', 'SIGN', kind='interp', line=322)
W('30,2666', 0o02343, '', '', 'DZDOT', kind='operand', line=323)
W('30,2667', 0o02361, '', 'STORE', 'ATP', kind='interp', line=324)
W('30,2670', 0o77761, '', 'VXSC', kind='interp', line=325)
W('30,2671', 0o03726, '', '', 'ZAXIS1', 'ATP ZAXIS *2(8).', kind='operand', line=326)
W('30,2672', 0o53372, '', 'VSL1', 'VAD', 'AT*2(0)', kind='interp', line=327)
W('30,2673', 0o00001, '', '', '00D', kind='operand', line=328)
W('30,2674', 0o03254, '', 'STORE', 'UNFC/2', 'WILL BE OVERWRITTEN IF IN VERT. RISE.', kind='interp', line=329)
W('30,2675', 0o43001, '', 'SETPD', 'BON', kind='interp', line=330)
W('30,2676', 0o00001, '', '', '00D', kind='operand', line=331)
W('30,2677', 0o04704, '', '', 'FLPI', kind='operand', line=332)
W('30,2700', 0o60220, '', '', 'P12RET', kind='operand', line=333)
W('30,2701', 0o77614, '', 'BON', kind='interp', line=334)
# Page 850
W('30,2702', 0o04701, '', '', 'FLVR', kind='operand', line=336)
W('30,2703', 0o60755, '', '', 'CHECKALT', kind='operand', line=337)
W('30,2704', 0o57575, 'MAINLINE', 'VLOAD', 'VCOMP', kind='interp', line=338)
W('30,2705', 0o03537, '', '', 'UNIT/R/', kind='operand', line=339)
W('30,2706', 0o17262, '', 'STODL', 'UNWC/2', kind='interp', line=340)
W('30,2707', 0o03654, '', '', 'TXO', kind='operand', line=341)
W('30,2710', 0o51025, '', 'DSU', 'BPL', kind='interp', line=342)
W('30,2711', 0o01235, '', '', 'PIPTIME', kind='operand', line=343)
W('30,2712', 0o60721, '', '', 'ASCTERM', kind='operand', line=344)
W('30,2713', 0o77614, '', 'BON', kind='interp', line=345)
W('30,2714', 0o04711, '', '', 'ROTFLAG', kind='operand', line=346)
W('30,2715', 0o57273, '', '', 'ANG1CHEK', kind='operand', line=347)
W('30,2716', 0o43014, 'CLRXFLAG', 'CLEAR', 'CLEAR', kind='interp', line=348)
W('30,2717', 0o01664, '', '', 'NOR29FLG', 'START r29 IN ASCENT PHASE.', kind='operand', line=349)
W('30,2720', 0o06666, '', '', 'XOVINFLG', 'ALLOW X-AXIS OVERRIDE', kind='operand', line=350)
W('30,2721', 0o77776, 'ASCTERM', 'EXIT', kind='interp', line=351)
W('30,2722', 0o30105, '', 'CA', 'FLAGWRD9', line=352)
W('30,2723', 0o74742, '', 'MASK', 'FLRCSBIT', line=353)
W('30,2724', 0o10000, '', 'CCS', 'A', line=354)
W('30,2725', 0o12747, '', 'TCF', 'ASCTERM3', line=355)
W('30,2726', 0o06037, '', 'TC', 'INTPRET', line=356)
W('30,2727', 0o77624, '', 'CALL', kind='interp', line=357)
W('30,2730', 0o61111, '', '', 'FINDCDUW -2', kind='operand', line=358)
W('30,2731', 0o77776, 'ASCTERM1', 'EXIT', kind='interp', line=359)
W('30,2732', 0o30105, '', 'CA', 'FLAGWRD9', 'INSURE THAT THE NOUN 63 DISPLAY IS', line=360)
W('30,2733', 0o74742, '', 'MASK', 'FLRCSBIT', 'BYPASSED IF WE ARE IN THE RCS TRIMMING', line=361)
W('30,2734', 0o10000, '', 'CCS', 'A', 'MODE OF OPERATION', line=362)
W('30,2735', 0o12747, '', 'TCF', 'ASCTERM3', line=363)
W('30,2736', 0o30104, '', 'CA', 'FLAGWRD8', 'BYPASS DISPLAYS IF ENGINE FAILURE IS', line=364)
W('30,2737', 0o74742, '', 'MASK', 'FLUNDBIT', 'INDICATED.', line=365)
W('30,2740', 0o10000, '', 'CCS', 'A', line=366)
W('30,2741', 0o12747, '', 'TCF', 'ASCTERM3', line=367)
W('30,2742', 0o33033, '', 'CAF', 'V06N63*', line=368)
W('30,2743', 0o04616, '', 'TC', 'BANKCALL', line=369)
W('30,2744', 0o20451, '', 'CADR', 'GODSPR', kind='data', line=370)
W('30,2745', 0o12747, '', 'TCF', 'ASCTERM3', line=371)
W('30,2746', 0o77776, 'ASCTERM2', 'EXIT', kind='interp', line=372)
W('30,2747', 0o15155, 'ASCTERM3', 'TCF', 'ENDOFJOB', line=373)
W('30,2750', 0o77776, 'ASCTERM4', 'EXIT', kind='interp', line=374)
W('30,2751', 0o00004, '', 'INHINT', line=375)
W('30,2752', 0o04674, '', 'TC', 'IBNKCALL', 'NO GUIDANCE THIS CYCLE -- HENCE ZERO', line=376)
W('30,2753', 0o40153, '', 'CADR', 'ZATTEROR', 'THE DAP COMMANDED ERRORS.', kind='data', line=377)
W('30,2754', 0o12732, '', 'TCF', 'ASCTERM1 +1', line=378)

W('30,2755', 0o45345, 'CHECKALT', 'DLOAD', 'DSU', kind='interp', line=380)
W('30,2756', 0o02301, '', '', '/R/MAG', kind='operand', line=381)
W('30,2757', 0o02333, '', '', '/LAND/', kind='operand', line=382)
W('30,2760', 0o50025, '', 'DSU', 'BMN', 'IF H LT 25K CHECK Z AXIS ORIENTATION', kind='interp', line=383)
W('30,2761', 0o26700, '', '', '25KFT', kind='operand', line=384)
W('30,2762', 0o16667, '', '', 'CHECKYAW', kind='operand', line=385)
# Page 851
W('30,2763', 0o43014, 'EXITVR', 'CLEAR', 'BON', kind='interp', line=387)
W('30,2764', 0o04661, '', '', 'FLVR', kind='operand', line=388)
W('30,2765', 0o04711, '', '', 'ROTFLAG', kind='operand', line=389)
W('30,2766', 0o60704, '', '', 'MAINLINE', kind='operand', line=390)
W('30,2767', 0o43345, '', 'DLOAD', 'DAD', kind='interp', line=391)
W('30,2770', 0o01235, '', '', 'PIPTIME', kind='operand', line=392)
W('30,2771', 0o25755, '', '', '10SECS', kind='operand', line=393)
W('30,2772', 0o37654, '', 'STCALL', 'TXO', kind='interp', line=394)
W('30,2773', 0o60704, '', '', 'MAINLINE', kind='operand', line=395)
W('30,2774', 0o77614, 'EXITVR1', 'CLRGO', kind='interp', line=396)
W('30,2775', 0o04631, '', '', 'ROTFLAG', kind='operand', line=397)
W('30,2776', 0o60763, '', '', 'EXITVR', kind='operand', line=398)

#   SETLOC ASENT1
#   BANK
#   COUNT* $$/ASENT

W('27,3273', 0o50375, 'ANG1CHEK', 'VLOAD', 'DOT', kind='interp', line=404)
W('27,3274', 0o03254, '', '', 'UNFC/2', kind='operand', line=405)
W('27,3275', 0o02146, '', '', 'XNBPIP', kind='operand', line=406)
W('27,3276', 0o51025, '', 'DSU', 'BPL', kind='interp', line=407)
W('27,3277', 0o02577, '', '', 'COSTHET1', kind='operand', line=408)
W('27,3300', 0o57307, '', '', 'OFFROT', kind='operand', line=409)
W('27,3301', 0o50375, '', 'VLOAD', 'DOT', kind='interp', line=410)
W('27,3302', 0o02146, '', '', 'XNBPIP', kind='operand', line=411)
W('27,3303', 0o03537, '', '', 'UNIT/R/', kind='operand', line=412)
W('27,3304', 0o50025, '', 'DSU', 'BMN', kind='interp', line=413)
W('27,3305', 0o02601, '', '', 'COSTHET2', kind='operand', line=414)
W('27,3306', 0o30351, '', '', 'KEEPVR1', kind='operand', line=415)
W('27,3307', 0o77614, 'OFFROT', 'CLRGO', kind='interp', line=416)
W('27,3310', 0o04631, '', '', 'ROTFLAG', kind='operand', line=417)
W('27,3311', 0o60716, '', '', 'CLRXFLAG', kind='operand', line=418)

#   BANK 7
#   SETLOC ASENT2
#   BANK
#   COUNT* $$/ASENT

S('SETXFLAG', 'equals', 0o26667, line=425)

W('07,2667', 0o77614, 'CHECKYAW', 'SET', kind='interp', line=427)
W('07,2670', 0o06466, '', '', 'XOVINFLG', 'PROHIBIT X-AXIS OVERRIDE', kind='operand', line=428)
W('07,2671', 0o74345, '', 'DLOAD', 'VXSC', kind='interp', line=429)
W('07,2672', 0o02355, '', '', 'ATY', kind='operand', line=430)
W('07,2673', 0o02303, '', '', 'LAXIS', kind='operand', line=431)
W('07,2674', 0o74325, '', 'PDDL', 'VXSC', kind='interp', line=432)
W('07,2675', 0o02361, '', '', 'ATP', kind='operand', line=433)
W('07,2676', 0o03726, '', '', 'ZAXIS1', kind='operand', line=434)
W('07,2677', 0o53455, '', 'VAD', 'UNIT', kind='interp', line=435)
W('07,2700', 0o50206, '', 'PUSH', 'DOT', kind='interp', line=436)
# Page 852
W('07,2701', 0o02154, '', '', 'YNBPIP', kind='operand', line=438)
W('07,2702', 0o45246, '', 'ABS', 'DSU', kind='interp', line=439)
W('07,2703', 0o13503, '', '', 'SIN5DEG', kind='operand', line=440)
W('07,2704', 0o71244, '', 'BPL', 'DLOAD', kind='interp', line=441)
W('07,2705', 0o30347, '', '', 'KEEPVR', kind='operand', line=442)
W('07,2706', 0o03474, '', '', 'RDOT', kind='operand', line=443)
W('07,2707', 0o51025, '', 'DSU', 'BPL', kind='interp', line=444)
W('07,2710', 0o13505, '', '', '40FPS', kind='operand', line=445)
W('07,2711', 0o60774, '', '', 'EXITVR1', kind='operand', line=446)
W('07,2712', 0o77650, '', 'GOTO', kind='interp', line=447)
W('07,2713', 0o30347, '', '', 'KEEPVR', kind='operand', line=448)

#   BANK 5
#   SETLOC ASENT3
#   BANK
#   COUNT* $$/ASENT

W('05,3502', 0o00545, 'SIN5DEG', '2DEC', '0.08716 B-2', kind='data', line=455)
W('05,3503', 0o00171, kind='data', line=455)
W('05,3504', 0o00017, '40FPS', '2DEC', '0.12192 B-7', kind='data', line=456)
W('05,3505', 0o23305, kind='data', line=456)

#   BANK 14
#   SETLOC ASENT4
#   BANK
#   COUNT* $$/ASENT

W('14,2347', 0o45575, 'KEEPVR', 'VLOAD', 'STADR', 'RECALL LOSVEC FROM PUSHLIST', kind='interp', line=463)
W('14,2350', 0o74515, '', 'STORE', 'UNWC/2', kind='interp', line=464)
W('14,2351', 0o77775, 'KEEPVR1', 'VLOAD', kind='interp', line=465)
W('14,2352', 0o03537, '', '', 'UNIT/R/', kind='operand', line=466)
W('14,2353', 0o37254, '', 'STCALL', 'UNFC/2', kind='interp', line=467)
W('14,2354', 0o60721, '', '', 'ASCTERM', kind='operand', line=468)

W('14,2355', 0o77634, 'ENGOFF', 'RTB', kind='interp', line=470)
W('14,2356', 0o21573, '', '', 'LOADTIME', kind='operand', line=471)
W('14,2357', 0o43225, '', 'DSU', 'DAD', kind='interp', line=472)
W('14,2360', 0o01235, '', '', 'PIPTIME', kind='operand', line=473)
W('14,2361', 0o03454, '', '', 'TTOGO', kind='operand', line=474)
W('14,2362', 0o77476, '', 'DCOMP', 'EXIT', kind='interp', line=475)
W('14,2363', 0o07257, '', 'TC', 'TPAGREE', 'FORCE SIGN AGREEMENT ON MPAC, MPAC +1.', line=476)
W('14,2364', 0o35016, '', 'CAF', 'EBANK7', line=477)
W('14,2365', 0o54003, '', 'TS', 'EBANK', line=478)
#   EBANK= TGO
W('14,2366', 0o00004, '', 'INHINT', line=480)
W('14,2367', 0o10155, '', 'CCS', 'MPAC +1', line=481)
W('14,2370', 0o12373, '', 'TCF', '+3', 'C(A) = DT - 1 BIT', line=482)
W('14,2371', 0o12373, '', 'TCF', '+2', 'C(A) = 0', line=483)
W('14,2372', 0o34755, '', 'CAF', 'ZERO', 'C(A) = 0', line=484)
W('14,2373', 0o64753, '', 'AD', 'BIT1', 'C(A) = 1 BIT OR DT.', line=485)
# Page 853
W('14,2374', 0o55644, '', 'TS', 'ENGOFFDT', line=487)
W('14,2375', 0o05173, '', 'TC', 'TWIDDLE', line=488)
W('14,2376', 0o02410, '', 'ADRES', 'ENGOFF1', kind='data', line=489)
W('14,2377', 0o05353, '', 'TC', 'PHASCHNG', line=490)
W('14,2400', 0o47014, '', 'OCT', '47014', kind='data', line=491)
W('14,2401', 0o76133, '', '-GENADR', 'ENGOFFDT', kind='data', line=492)
#   EBANK= TGO
W('14,2402', 0o02410, '', '2CADR', 'ENGOFF1', kind='data', line=494)
W('14,2403', 0o30067, kind='data', line=494)

W('14,2404', 0o06037, '', 'TC', 'INTPRET', line=496)
W('14,2405', 0o52014, '', 'SET', 'GOTO', kind='interp', line=497)
W('14,2406', 0o03470, '', '', 'IDLEFLAG', 'DISABLE DELTA-V MONITOR', kind='operand', line=498)
W('14,2407', 0o60451, '', '', 'T2TEST', kind='operand', line=499)

W('14,2410', 0o04674, 'ENGOFF1', 'TC', 'IBNKCALL', 'SHUT OFF THE ENGINE.', line=501)
W('14,2411', 0o75551, '', 'CADR', 'ENGINOF2', kind='data', line=502)

W('14,2412', 0o35027, '', 'CAF', 'PRIO17', 'SET UP A JOB FOR THE ASCENT GUIDANCE', line=504)
W('14,2413', 0o05105, '', 'TC', 'FINDVAC', 'POSTBURN LOGIC.', line=505)
#   EBANK= WHICH
W('14,2414', 0o02424, '', '2CADR', 'CUTOFF', kind='data', line=507)
W('14,2415', 0o30067, kind='data', line=507)

W('14,2416', 0o05353, '', 'TC', 'PHASCHNG', line=509)
W('14,2417', 0o07024, '', 'OCT', '07024', kind='data', line=510)
W('14,2420', 0o17000, '', 'OCT', '17000', kind='data', line=511)
#   EBANK= TGO
W('14,2421', 0o02424, '', '2CADR', 'CUTOFF', kind='data', line=513)
W('14,2422', 0o30067, kind='data', line=513)

W('14,2423', 0o15261, '', 'TCF', 'TASKOVER', line=515)

W('14,2424', 0o05504, 'CUTOFF', 'TC', 'UPFLAG', 'SET FLRCS FLAG.', line=517)
W('14,2425', 0o00214, '', 'ADRES', 'FLRCS', kind='data', line=518)

W('14,2426', 0o32445, '', 'CAF', 'V16N63', line=520)
W('14,2427', 0o04616, '', 'TC', 'BANKCALL', line=521)
W('14,2430', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=522)
W('14,2431', 0o12434, '', 'TCF', '+3', line=523)
W('14,2432', 0o12436, '', 'TCF', 'CUTOFF1', line=524)
W('14,2433', 0o12426, '', 'TCF', '-5', line=525)

W('14,2434', 0o04635, '', 'TC', 'POSTJUMP', line=527)
W('14,2435', 0o61007, '', 'CADR', 'TERMASC', kind='data', line=528)

W('14,2436', 0o00004, 'CUTOFF1', 'INHINT', line=530)
W('14,2437', 0o04674, '', 'TC', 'IBNKCALL', 'ZERO ATTITUDE ERRORS BEFORE REDUCINT DB.', line=531)
W('14,2440', 0o40153, '', 'CADR', 'ZATTEROR', kind='data', line=532)
W('14,2441', 0o04674, '', 'TC', 'IBNKCALL', line=533)
W('14,2442', 0o40140, '', 'CADR', 'SETMINDB', kind='data', line=534)
W('14,2443', 0o04635, '', 'TC', 'POSTJUMP', line=535)
W('14,2444', 0o60777, '', 'CADR', 'CUTOFF2', kind='data', line=536)
# Page 854

W('14,2445', 0o04077, 'V16N63', 'VN', '1663', kind='data', line=539)
#   BANK 30
#   SETLOC ASENT5
#   BANK
#   COUNT* $$/ASENT

W('30,2777', 0o05353, 'CUTOFF2', 'TC', 'PHASCHNG', line=545)
W('30,3000', 0o04024, '', 'OCT', '04024', kind='data', line=546)

W('30,3001', 0o33017, '', 'CAF', 'V16N85C', line=548)
W('30,3002', 0o04616, '', 'TC', 'BANKCALL', line=549)
W('30,3003', 0o20476, '', 'CADR', 'GOFLASH', kind='data', line=550)
W('30,3004', 0o13007, '', 'TCF', 'TERMASC', line=551)
W('30,3005', 0o13007, '', 'TCF', '+2', 'PROCEED', line=552)
W('30,3006', 0o12777, '', 'TCF', 'CUTOFF2', line=553)

W('30,3007', 0o05353, 'TERMASC', 'TC', 'PHASCHNG', line=555)
W('30,3010', 0o04024, '', 'OCT', '04024', kind='data', line=556)

W('30,3011', 0o00004, '', 'INHINT', '', 'RESTORE DEADBAND DESIRED BY ASTRONAUT.', line=558)
W('30,3012', 0o04674, '', 'TC', 'IBNKCALL', line=559)
W('30,3013', 0o40123, '', 'CADR', 'RESTORDB', kind='data', line=560)
W('30,3014', 0o05516, '', 'TC', 'DOWNFLAG', 'DISALLOW ABORTS AT THIS TIME.', line=561)
W('30,3015', 0o00215, '', 'ADRES', 'LETABORT', kind='data', line=562)
W('30,3016', 0o16001, '', 'TCF', 'GOTOPOOH', line=563)

W('30,3017', 0o04125, 'V16N85C', 'VN', '1685', kind='data', line=565)

#   BANK 27
#   SETLOC ASENT1
#   BANK
#   COUNT* $$/ASENT

W('27,3312', 0o50375, 'YCOMP', 'VLOAD', 'DOT', kind='interp', line=572)
W('27,3313', 0o03537, '', '', 'UNIT/R/', kind='operand', line=573)
W('27,3314', 0o03720, '', '', 'QAXIS', kind='operand', line=574)
W('27,3315', 0o41312, '', 'SL2', 'DMP', kind='interp', line=575)
W('27,3316', 0o03631, '', '', 'RCO', kind='operand', line=576)
W('27,3317', 0o02335, '', 'STORE', 'Y', kind='interp', line=577)
W('27,3320', 0o77616, '', 'RVQ', kind='interp', line=578)

#   BANK 30
#   SETLOC ASENT
#   BANK
# Page 855
S('100CS', 'equals', 0o77146, line=584)
S('T2A', 'equals', 0o71022, line=585)
W('30,3020', 0o00062, '4SEC(17)', '2DEC', '400 B-17', kind='data', line=586)
W('30,3021', 0o00000, kind='data', line=586)
W('30,3022', 0o00031, '2SEC(17)', '2DEC', '200 B-17', kind='data', line=587)
W('30,3023', 0o00000, kind='data', line=587)
W('30,3024', 0o00175, 'T3', '2DEC', '1000 B-17', kind='data', line=588)
W('30,3025', 0o00000, kind='data', line=588)
W('30,3026', 0o00045, '6SEC(18)', '2DEC', '600 B-18', kind='data', line=589)
W('30,3027', 0o20000, kind='data', line=589)
W('30,3030', 0o00010, 'BIT4H', 'OCT', '10', kind='data', line=590)
W('30,3031', 0o14400, '2SEC(9)', '2DEC', '200 B-9', kind='data', line=591)
W('30,3032', 0o00000, kind='data', line=591)
W('30,3033', 0o01477, 'V06N63*', 'VN', '0663', kind='data', line=592)
W('30,3034', 0o01514, 'V06N76', 'VN', '0676', kind='data', line=593)
W('30,3035', 0o01441, 'V06N33A', 'VN', '0633', kind='data', line=594)

#   BANK 33
#   SETLOC ASENT6
#   BANK
#   COUNT* $$/ASENT

W('33,2200', 0o20000, 'KT1', '2DEC', '0.5000', kind='data', line=601)
W('33,2201', 0o00000, kind='data', line=601)
W('33,2202', 0o75751, 'PRLIMIT', '2DEC', '-.0639', '(B/TBUP)MIN=-.1FT.SEC(-3)', kind='data', line=602)
W('33,2203', 0o41775, kind='data', line=602)
W('33,2204', 0o00022, 'MINABDV', '2DEC', '.0356 B-5', '10 PERCENT BIGGER THAN GRAVITY', kind='data', line=603)
W('33,2205', 0o07212, kind='data', line=603)
S('1/DV0', 'equals', 0o3570, line=604)

# Page 856
# THE LOGARITHM SUBROUTINE

#   BANK 24
#   SETLOC FLOGSUB
#   BANK

# INPUT ..... X IN MPAC
# OUTPUT ..... -LOG(X) IN MPAC

W('30,3036', 0o44301, 'LOGSUB', 'NORM', 'BDSU', kind='interp', line=616)
W('30,3037', 0o00163, '', '', 'MPAC +6', kind='operand', line=617)
W('30,3040', 0o17771, '', '', 'NEARONE', kind='operand', line=618)
W('30,3041', 0o77776, '', 'EXIT', kind='interp', line=619)
W('30,3042', 0o07222, '', 'TC', 'POLY', line=620)
W('30,3043', 0o00006, '', 'DEC', '6', kind='data', line=621)
W('30,3044', 0o00000, '', '2DEC', '.0000000060', kind='data', line=622)
W('30,3045', 0o00002, kind='data', line=622)
W('30,3046', 0o76777, '', '2DEC', '-.0312514377', kind='data', line=623)
W('30,3047', 0o77175, kind='data', line=623)
W('30,3050', 0o77400, '', '2DEC', '-.0155686771', kind='data', line=624)
W('30,3051', 0o75416, kind='data', line=624)
W('30,3052', 0o77507, '', '2DEC', '-.0112502068', kind='data', line=625)
W('30,3053', 0o65515, kind='data', line=625)
W('30,3054', 0o77741, '', '2DEC', '-.0018545108', kind='data', line=626)
W('30,3055', 0o63547, kind='data', line=626)
W('30,3056', 0o77052, '', '2DEC', '-.0286607906', kind='data', line=627)
W('30,3057', 0o55373, kind='data', line=627)
W('30,3060', 0o01167, '', '2DEC', '.0385598563', kind='data', line=628)
W('30,3061', 0o30361, kind='data', line=628)
W('30,3062', 0o76520, '', '2DEC', '-.0419361902', kind='data', line=629)
W('30,3063', 0o75267, kind='data', line=629)

W('30,3064', 0o34755, '', 'CAF', 'ZERO', line=631)
W('30,3065', 0o54156, '', 'TS', 'MPAC +2', line=632)
W('30,3066', 0o00006, '', 'EXTEND', line=633)
W('30,3067', 0o33103, '', 'DCA', 'CLOG2/32', line=634)
W('30,3070', 0o52155, '', 'DXCH', 'MPAC', line=635)
W('30,3071', 0o52132, '', 'DXCH', 'BUF +1', line=636)
W('30,3072', 0o30162, '', 'CA', 'MPAC +6', line=637)
W('30,3073', 0o07307, '', 'TC', 'SHORTMP', line=638)
W('30,3074', 0o52156, '', 'DXCH', 'MPAC +1', line=639)
W('30,3075', 0o52155, '', 'DXCH', 'MPAC', line=640)
W('30,3076', 0o52132, '', 'DXCH', 'BUF +1', line=641)
W('30,3077', 0o20155, '', 'DAS', 'MPAC', line=642)
W('30,3100', 0o06037, '', 'TC', 'INTPRET', line=643)
W('30,3101', 0o43476, '', 'DCOMP', 'RVQ', kind='interp', line=644)

W('30,3102', 0o00542, 'CLOG2/32', '2DEC', '.0216608494', kind='data', line=646)
W('30,3103', 0o34414, kind='data', line=646)
