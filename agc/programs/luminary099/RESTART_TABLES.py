"""RESTART_TABLES.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/RESTART_TABLES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 238-243 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('RESTART_TABLES', 'RESTART_TABLES.agc', 'Luminary099', pages='238-243')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     RESTART_TABLES.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Ron Burkey <info@sandroid.org>.
# Website:      www.ibiblio.org/apollo.
# Pages:        238-243
# Mod history:  2009-05-10 SN   (Sergio Navarro).  Started adapting
# from the Luminary131/ file of the same
# name, using Luminary099 page images.
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

# Page 238
# RESTART TABLES
# ------------------
#
# THERE ARE TWO FORMS OF RESTART TABLES FOR EACH GROUP.  THEY ARE KNOWN AS THE EVEN RESTART TABLES AND THE ODD
# RESTART TABLES.  THE ODD TABLES HAVE ONLY ONE ENTRY OF THREE LOCATIONS WHILE THE EVEN TABLES HAVE TWO ENTRIES
# EACH USING THREE LOCATIONS. THE INFORMATION AS TO WHETHER IT IS A JOB, WAITLIST, OR A LONGCALL IS GIVEN BY THE
# WAY THINGS ARE PUT INTO THE TABLES.
# A JOB HAS ITS PRIORITY STORED IN PRDTTAB OF THE CORRECT PHASE SPOT - A POSITIVE PRIORITY INDICATES A
# FINDVAC JOB, A NEGATIVE PRIORITY A NOVAC.  THE 2CADR OF THE JOB IS STORED IN THE CADRTAB.
# FOR EXAMPLE,
#
# 5.7SPOT       OCT     23000
# 2CADR   SOMEJOB
#
# A RESTART OF GROUP 5 WITH PHASE SEVEN WOULD THEN CAUSE SOMEJOB TO BE RESTARTED AS A FINDVAC WITH PRIORITY 23.
#
# 5.5SPOT       OCT     -23000
# 2CADR   ANYJOB
#
# HERE A RESTART OF GROUP 5 WITH PHASE 7 WOULD CAUSE ANYJOB TO BE RESTARTED AS A NOVAC WITH PRIORITY 23.
# A LONGCALL HAS ITS GENADR OF ITS 2CADR STORED NEGATIVELY AND ITS BBCON STORED POSITIVELY.  IN ITS PRDTTAB IS
# PLACED THE LOCATION OF A DP REGISTER THAT CONTAINS THE DELTA TIME THAT LONGCALL HAD BEEN ORIGINALLY STARTED
# WITH.  EXAMPLE,
#
# 3.6SPOT       GENADR  DELTAT
# -GENADR  LONGTASK
# BBCON   LONGTASK
#
# OCT     31000
# 2CADR   JOBAGAIN
#
# THIS WOULD START UP LONGTASK AT THE APPROPRIATE TIME, OR IMMEDIATELY IF THE TIME HAD ALREADY PASSED. IT SHOULD
# BE NOTED THAT IF DELTAT IS IN A SWITCHED E BANK, THIS INFORMATOIN SHOULD BE IN THE BBCON OFTHE 2CADR OF THE
# TASK.  FROM ABOVE, WE SEE THAT THE SECOND PART OF THIS PHASE WOULD BE STARTED AS A JOB WITH A PRIORITY OF 31.
#
# WAITLIST CALLS ARE IDENTIFIED BY THE FACT THAT THEIR 2CADR IS STORED NEGATIVELY. IF PRDTTAB OF THE PHASE SPOT
# IS POSITIVE, THEN IT CONTAINS THE DELTA TIME, IF PRDTTAB IS NEGATIVE THEN IT IS THE -GENADR OF AN ERASABLE
# LOCATION CONTAINING THE DELTA TIME, THAT IS, THE TIME IS STORED INDIRECTLY.  IT SHOULD BE NOTED AS ABOVE, THAT
# IF THE TIME IS STORED INDIRECTLY, THE BBCON MUST CONTAIN THE NECESSARY E BANK INFORMATION IF APPLICABLE.  WITH
# WAITLIST WE HAVE ONE FURTHER OPTION, IF -0 IS STORED IN PRDTTAB, IT WILL CAUSE AN IMMEDIATE RESTART OF THE
# TASK.  EXAMPLES,
#
# OCT     77777           # THIS WILL CAUSE AN IMMEDIATE RESTART
# -2CADR   ATASK           # OF THE TASK :ATASK:
#
# DEC     200             # IF THE TIME OF THE 2 SECONDS SINCE DUMMY
# -2CADR   DUMMY           # WAS PUT ON THE WAITLIST IS UP, IT WILL BEGIN
# # IN 10 MS, OTHERWISE IT WILL BEGIN WHEN
# # IT NORMALLY WOULD HAVE BEGUN.
# Page 239
# -GENADR  DTIME           # WHERE DTIME CONTAINS THE DELTA TIME
# -2CADR   TASKTASK        # OTHERWISE THIS IS AS ABOVE
#
# ***** NOW THE TABLES THEMSELVES *****

#   BANK 01
#   SETLOC RESTART
#   BANK

S('PRDTTAB', 'equals', 0o12000, line=89)  # USED TO FIND THE PRIORITY OR DELTATIME
S('CADRTAB', 'equals', 0o12001, line=90)  # THIS AND THE NEXT RELATIVE LOC CONTAIN
# RESTART 2CADR

#   COUNT* $$/RSTAB  # TABLES IN BANK 1.
W('01,2002', 0o00010, 'SIZETAB', 'TC', '1.2SPOT -12006', line=94)
W('01,2003', 0o00020, '', 'TC', '1.3SPOT -12004', line=95)
W('01,2004', 0o00010, '', 'TC', '2.2SPOT -12006', line=96)
W('01,2005', 0o00023, '', 'TC', '2.3SPOT -12004', line=97)
W('01,2006', 0o00010, '', 'TC', '3.2SPOT -12006', line=98)
W('01,2007', 0o00053, '', 'TC', '3.3SPOT -12004', line=99)
W('01,2010', 0o00057, '', 'TC', '4.2SPOT -12006', line=100)
W('01,2011', 0o00067, '', 'TC', '4.3SPOT -12004', line=101)
W('01,2012', 0o00142, '', 'TC', '5.2SPOT -12006', line=102)
W('01,2013', 0o00160, '', 'TC', '5.3SPOT -12004', line=103)
W('01,2014', 0o00010, '', 'TC', '6.2SPOT -12006', line=104)
W('01,2015', 0o00171, '', 'TC', '6.3SPOT -12004', line=105)
W('01,2016', 0o21000, '1.2SPOT', 'OCT', '21000', 'A DUMMY EXAMPLE TO BE REPLACED AS SOON', kind='data', line=106)
#   EBANK= STATE
W('01,2017', 0o05155, '', '2CADR', 'ENDOFJOB', 'AS THERE IS A LEGITIMATE 1.2SPOT', kind='data', line=108)
W('01,2020', 0o04060, kind='data', line=108)

W('01,2021', 0o00144, '', 'DEC', '100', kind='data', line=110)
#   EBANK= STATE
W('01,2022', 0o05261, '', '2CADR', 'TASKOVER', kind='data', line=112)
W('01,2023', 0o04060, kind='data', line=112)

# ANY MORE GROUP 1.EVEN RESTART VALUES SHOULD GO HERE

W('01,2024', 0o76300, '1.3SPOT', '-GENADR', 'SAVET-30', kind='data', line=116)
#   EBANK= DVCNTR
W('01,2025', 0o75431, '', '-2CADR', 'ULLGTASK', kind='data', line=118)
W('01,2026', 0o03710, kind='data', line=118)

# ANY MORE GROUP 1.ODD RESTART VALUES SHOULD GO HERE

S('2.2SPOT', 'equals', 0o12016, line=122)
# ANY MORE GROUP 2.EVEN RESTART VALUES SHOULD GO HERE

W('01,2027', 0o02630, '2.3SPOT', 'GENADR', '600SECS', kind='data', line=125)
W('01,2030', 0o75173, '', '-GENADR', 'STATEINT', kind='data', line=126)
#   EBANK= RRECTCSM
W('01,2031', 0o26063, '', 'BBCON', 'STATEINT', kind='data', line=128)

# Page 240
W('01,2032', 0o05000, '2.5SPOT', 'OCT', '05000', kind='data', line=131)
#   EBANK= RRECTCSM
W('01,2033', 0o02613, '', '2CADR', 'STATINT1', kind='data', line=133)
W('01,2034', 0o26063, kind='data', line=133)

W('01,2035', 0o02734, '2.7SPOT', 'DEC', '1500', kind='data', line=135)
#   EBANK= LOSCOUNT
W('01,2036', 0o75533, '', '-2CADR', 'P20LEMC1', kind='data', line=137)
W('01,2037', 0o27710, kind='data', line=137)

W('01,2040', 0o14000, '2.11SPOT', 'OCT', '14000', kind='data', line=139)
#   EBANK= P21TIME
W('01,2041', 0o02416, '', '2CADR', 'P25LEM1', kind='data', line=141)
W('01,2042', 0o50067, kind='data', line=141)

W('01,2043', 0o10000, '2.13SPOT', 'OCT', '10000', kind='data', line=143)
#   EBANK= LOSCOUNT
W('01,2044', 0o02217, '', '2CADR', 'RELINUS', kind='data', line=145)
W('01,2045', 0o54067, kind='data', line=145)

W('01,2046', 0o26000, '2.15SPOT', 'OCT', '26000', kind='data', line=147)
#   EBANK= LOSCOUNT
W('01,2047', 0o02653, '', '2CADR', 'R22RSTRT', kind='data', line=149)
W('01,2050', 0o50067, kind='data', line=149)

W('01,2051', 0o77777, '2.17SPOT', 'OCT', '77777', kind='data', line=151)
#   EBANK= VGPREV
W('01,2052', 0o75440, '', '-2CADR', 'REDO2.17', kind='data', line=153)
W('01,2053', 0o03710, kind='data', line=153)

W('01,2054', 0o00031, '2.21SPOT', 'DEC', '25', kind='data', line=155)
#   EBANK= DVCNTR
W('01,2055', 0o75771, '', '-2CADR', 'R10,R11', kind='data', line=157)
W('01,2056', 0o35710, kind='data', line=157)

# ANY MORE GROUP 2.ODD RESTART VALUES SHOULD GO HERE.

S('3.2SPOT', 'equals', 0o12016, line=161)
# ANY MORE GROUP 3.EVEN RESTART VALUES SHOULD GO HERE

W('01,2057', 0o76355, '3.3SPOT', '-GENADR', 'ZOOMTIME', kind='data', line=164)
#   EBANK= DVCNTR
W('01,2060', 0o75755, '', '-2CADR', 'ZOOM', kind='data', line=166)
W('01,2061', 0o41710, kind='data', line=166)

W('01,2062', 0o20000, '3.5SPOT', 'OCT', '20000', kind='data', line=168)
#   EBANK= TTOGO
W('01,2063', 0o02540, '', '2CADR', 'S40.13', kind='data', line=170)
W('01,2064', 0o56067, kind='data', line=170)

# ANY MORE GROUP 3.ODD RESTART VALUES SHOULD GO HERE

W('01,2065', 0o04704, '4.2SPOT', 'DEC', '2500', kind='data', line=174)
#   EBANK= TTOGO
W('01,2066', 0o75425, '', '-2CADR', 'TIG-5', kind='data', line=176)
W('01,2067', 0o03710, kind='data', line=176)

W('01,2070', 0o77777, '', 'OCT', '77777', kind='data', line=178)
#   EBANK= TTOGO
# Page 241
W('01,2071', 0o75435, '', '-2CADR', 'REDO4.2', kind='data', line=181)
W('01,2072', 0o03710, kind='data', line=181)

# ANY MORE GROUP 4.EVEN RESTART VALUES SHOULD GO HERE

W('01,2073', 0o25000, '4.3SPOT', 'OCT', '25000', kind='data', line=185)
#   EBANK= DVCNTR
W('01,2074', 0o03540, '', '2CADR', 'GOABORT', kind='data', line=187)
W('01,2075', 0o64067, kind='data', line=187)

W('01,2076', 0o00062, '4.5SPOT', 'DEC', '50', kind='data', line=189)
#   EBANK= TTOGO
W('01,2077', 0o75215, '', '-2CADR', 'ULLAGOFF', kind='data', line=191)
W('01,2100', 0o03710, kind='data', line=191)

W('01,2101', 0o00764, '4.7SPOT', 'DEC', '500', kind='data', line=193)
#   EBANK= DVCNTR
W('01,2102', 0o75374, '', '-2CADR', 'TIG-0', kind='data', line=195)
W('01,2103', 0o03710, kind='data', line=195)

W('01,2104', 0o76260, '4.11SPOT', '-GENADR', 'TGO +1', kind='data', line=197)
#   EBANK= DVCNTR
W('01,2105', 0o74235, '', '-2CADR', 'ENGOFTSK', kind='data', line=199)
W('01,2106', 0o03710, kind='data', line=199)

W('01,2107', 0o12000, '4.13SPOT', 'OCT', '12000', kind='data', line=201)
#   EBANK= TRKMKCNT
W('01,2110', 0o03223, '', '2CADR', 'POSTBURN', kind='data', line=203)
W('01,2111', 0o74067, kind='data', line=203)

W('01,2112', 0o00764, '4.15SPOT', 'DEC', '500', kind='data', line=205)
#   EBANK= TTOGO
W('01,2113', 0o75501, '', '-2CADR', 'TIG-30', kind='data', line=207)
W('01,2114', 0o03710, kind='data', line=207)

W('01,2115', 0o77777, '4.17SPOT', 'OCT', '77777', kind='data', line=209)
#   EBANK= DVCNTR
W('01,2116', 0o75425, '', '-2CADR', 'TIG-5', kind='data', line=211)
W('01,2117', 0o03710, kind='data', line=211)

W('01,2120', 0o13000, '4.21SPOT', 'OCT', '13000', kind='data', line=213)
#   EBANK= STAR
W('01,2121', 0o03020, '', '2CADR', 'R51.1 +1', kind='data', line=215)
W('01,2122', 0o30065, kind='data', line=215)

W('01,2123', 0o77777, '4.23SPOT', 'OCT', '77777', kind='data', line=217)
#   EBANK= DVCNTR
W('01,2124', 0o75351, '', '-2CADR', 'IGNITION', kind='data', line=219)
W('01,2125', 0o03710, kind='data', line=219)

W('01,2126', 0o01477, '4.25SPOT', 'GENADR', 'SAVET-30', kind='data', line=221)
W('01,2127', 0o75537, '', '-GENADR', 'TIG-35', kind='data', line=222)
#   EBANK= SAVET-30
W('01,2130', 0o74067, '', 'BBCON', 'TIG-35', kind='data', line=224)

W('01,2131', 0o52777, '4.27SPOT', 'OCT', '52777', kind='data', line=226)
#   EBANK= DVCNTR
W('01,2132', 0o02073, '', '2CADR', 'P70A', kind='data', line=228)
W('01,2133', 0o42067, kind='data', line=228)

# Page 242
W('01,2134', 0o52777, '4.31SPOT', 'OCT', '52777', kind='data', line=231)
#   EBANK= DVCNTR
W('01,2135', 0o02076, '', '2CADR', 'P71A', kind='data', line=233)
W('01,2136', 0o42067, kind='data', line=233)

W('01,2137', 0o46777, '4.33SPOT', 'OCT', '46777', kind='data', line=235)
#   EBANK= DVCNTR
W('01,2140', 0o02024, '', '2CADR', 'GOP00FIX', kind='data', line=237)
W('01,2141', 0o10067, kind='data', line=237)

W('01,2142', 0o46777, '4.35SPOT', 'OCT', '46777', kind='data', line=239)
#   EBANK= DVCNTR
W('01,2143', 0o05665, '', '2CADR', 'GOPOODOO', kind='data', line=241)
W('01,2144', 0o04067, kind='data', line=241)

W('01,2145', 0o52777, '4.37SPOT', 'OCT', '52777', kind='data', line=243)
#   EBANK= WHICH
W('01,2146', 0o02571, '', '2CADR', 'COMFAIL', kind='data', line=245)
W('01,2147', 0o74067, kind='data', line=245)

# ANY MORE 4.ODD RESTART VALUES SHOULD GO HERE.

W('01,2150', 0o22000, '5.2SPOT', 'OCT', '22000', kind='data', line=249)
#   EBANK= DVCNTR
W('01,2151', 0o02461, '', '2CADR', 'NORMLIZE', kind='data', line=251)
W('01,2152', 0o46067, kind='data', line=251)

W('01,2153', 0o00310, '', 'DEC', '200', kind='data', line=253)
#   EBANK= DVCNTR
W('01,2154', 0o74163, '', '-2CADR', 'REREADAC', kind='data', line=255)
W('01,2155', 0o01710, kind='data', line=255)

W('01,2156', 0o00310, '5.4SPOT', 'DEC', '200', kind='data', line=257)
#   EBANK= DVCNTR
W('01,2157', 0o74163, '', '-2CADR', 'REREADAC', kind='data', line=259)
W('01,2160', 0o01710, kind='data', line=259)

W('01,2161', 0o20000, '', 'OCT', '20000', kind='data', line=261)
#   EBANK= DVCNTR
W('01,2162', 0o02206, '', '2CADR', 'SERVICER', kind='data', line=263)
W('01,2163', 0o66067, kind='data', line=263)

# ANY MORE GROUP 5.EVEN RESTART VALUES SHOULD GO HERE

W('01,2164', 0o00310, '5.3SPOT', 'DEC', '200', kind='data', line=267)
#   EBANK= DVCNTR
W('01,2165', 0o74163, '', '-2CADR', 'REREADAC', kind='data', line=269)
W('01,2166', 0o01710, kind='data', line=269)

W('01,2167', 0o77777, '5.5SPOT', 'OCT', '77777', kind='data', line=271)
#   EBANK= DVCNTR
W('01,2170', 0o74324, '', '-2CADR', 'REDO5.5', kind='data', line=273)
W('01,2171', 0o01710, kind='data', line=273)

W('01,2172', 0o77777, '5.7SPOT', 'OCT', '77777', kind='data', line=275)
#   EBANK= DVCNTR
# Page 243
W('01,2173', 0o74361, '', '-2CADR', 'BIBIBIAS', kind='data', line=278)
W('01,2174', 0o01710, kind='data', line=278)

# ANY MORE GROUP 5.ODD RESTART VALUES SHOULD GO HERE

S('6.2SPOT', 'equals', 0o12016, line=282)
W('01,2175', 0o00144, '6.3SPOT', 'DEC', '100', kind='data', line=283)
#   EBANK= TIG
W('01,2176', 0o75060, '', '-2CADR', 'CLOKTASK', kind='data', line=285)
W('01,2177', 0o03710, kind='data', line=285)

W('01,2200', 0o30000, '6.5SPOT', 'OCT', '30000', 'PROTECT INCREMENTING OF TIME2,TIME1 BY', kind='data', line=287)
#   EBANK= TEPHEM  # P27(UPDATE PROGRAM) VIA V70 OR V73.
W('01,2201', 0o03601, '', '2CADR', 'TIMEDIDR', kind='data', line=289)
W('01,2202', 0o10063, kind='data', line=289)

W('01,2203', 0o17000, '6.7SPOT', 'OCT', '17000', kind='data', line=291)
#   EBANK= VGPREV
W('01,2204', 0o03350, '', '2CADR', 'REDO6.7', kind='data', line=293)
W('01,2205', 0o74067, kind='data', line=293)
