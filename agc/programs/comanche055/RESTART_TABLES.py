"""RESTART_TABLES.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/RESTART_TABLES.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 211-221 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('RESTART_TABLES', 'RESTART_TABLES.agc', 'Comanche055', pages='211-221')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     RESTART_TABLES.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 211-221
# Contact:      Ron Burkey <info@sandroid.org>,
# Fabrizio Bernardini <fabrizio@spacecraft.it>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  2009-05-16 FB   Transcription Batch 2 Assignment.
# 2009-05-20 RSB  Added a missing comment mark.  Corrected mismarked
# Page 217 -> 220.
# 2009-05-21 RSB  Fixed value of 5.21SPOT.
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
# Refer directly to the online document mentioned above for further
# information.  Please report any errors to info@sandroid.org.

# Page 211
# RESTART TABLES
# --------------
#
# THERE ARE TWO FORMS OF RESTART TABLES FOR EACH GROUP.  THEY ARE KNOWN AS THE EVEN RESTART TABLES AND THE ODD
# RESTART TABLES.  THE ODD TABLES HAVE ONLY ONE ENTRY OF THREE LOCATIONS WHILE THE EVEN TABLES HAVE TWO ENTRIES
# EACH USING THREE LOCATIONS. THE INFORMATION AS TO WHETHER IT IS A JOB, WAITLIST, OR A LONGCALL IS GIVEN BY THE
# WAY THINGS ARE PUT INTO THE TABLES.
#
# A JOB HAS ITS PRIORITY STORED IN PRDTTAB OF THE CORRECT PHASE SPOT - A POSITIVE PRIORITY INDICATES A
# FINDVAC JOB, A NEGATIVE PRIORITY A NOVAC.  THE 2CADR OF THE JOB IS STORED IN THE CADRTAB.
# FOR EXAMPLE,
#
# 5.7SPOT         OCT     23000
# 2CADR   SOMEJOB
#
# A RESTART OF GROUP 5 WITH PHASE SEVEN WOULD THEN CAUSE SOMEJOB TO BE RESTARTED AS A FINDVAC WITH PRIORITY 23.
#
# 5.5SPOT         OCT     -23000
# 2CADR   ANYJOB
#
# HERE A RESTART OF GROUP 5 WITH PHASE 7 WOULD CAUSE ANYJOB TO BE RESTARTED AS A NOVAC WITH PRIORITY 23.
# A LONGCALL HAS ITS GENADR OF ITS 2CADR STORED NEGATIVELY AND ITS BBCON STORED POSITIVELY.  IN ITS PRDTTAB IS
# PLACED THE LOCATION OF A DP REGISTER THAT CONTAINS THE DELTA TIME THAT LONGCALL HAD BEEN ORIGINALLY STARTED
# WITH.  EXAMPLE,
#
# 3.6SPOT         GENADR  DELTAT
# -GENADR LONGTASK
# BBCON   LONGTASK

# OCT     31000
# 2CADR   JOBAGAIN
#
# THIS WOULD START UP LONGTASK AT THE APPROPRIATE TIME, OR IMMEDIATELY IF THE TIME HAD ALREADY PASSED. IT SHOULD
# BE NOTED THAT IF DELTAT IS IN A SWITCHED E BANK, THIS INFORMATION SHOULD BE IN THE BBCON OF THE 2CADR OF THE
# TASK.  FROM ABOVE, WE SEE THAT THE SECOND PART OF THIS PHASE WOULD BE STARTED AS A JOB WITH A PRIORITY OF 31.
#
# WAITLIST CALLS ARE IDENTIFIED BY THE FACT THAT THEIR 2CADR IS STORED NEGATIVELY.  IF PRDTTAB OF THE PHASE SPOT
# IS POSITIVE, THEN IT CONTAINS THE DELTA TIME, IF PRDTTAB IS NEGATIVE THEN IT IS THE -GENADR OF AN ERASABLE
# LOCATION CONTAINING THE DELTA TIME, THAT IS, THE TIME IS STORED INDIRECTLY.  IT SHOULD BE NOTED AS ABOVE, THAT
# IF THE TIME IS STORED INDIRECTLY, THE BBCON MUST CONTAIN THE NECESSARY E BANK INFORMATION IF APPLICABLE.  WITH
# WAITLIST WE HAVE ONE FURTHER OPTION, IF -0 IS STORED IN PRDTTAB, IT WILL CAUSE AN IMMEDIATE RESTART OF THE
# TASK.  EXAMPLES,
#
# OCT     77777           # THIS WILL CAUSE AN IMMEDIATE RESTART
# -2CADR  ATASK           # OF THE TASK :ATASK:
#
# DEC     200             # IF THE TIME OF THE 2 SECONDS SINCE DUMMY
# -2CADR  DUMMY           # WAS PUT ON THE WAITLIST IS UP, IT WILL BEGIN
# # IN 10 MS, OTHERWISE IT WILL BEGIN WHEN
# # IT NORMALLY WOULD HAVE BEGUN.
# Page 212
# -GENADR DTIME           # WHERE DTIME CONTAINS THE DELTA TIME
# -2CADR  TASKTASK        # OTHERWISE THIS IS AS ABOVE
#
# ***** NOW THE TABLES THEMSELVES *****

#   BANK 01
#   SETLOC RESTART
#   BANK

#   COUNT 01/RSTAB

S('PRDTTAB', 'equals', 0o12000, line=97)  # USED TO FIND THE PRIORITY OR DELTATIME
S('CADRTAB', 'equals', 0o12001, line=98)  # THIS AND THE NEXT RELATIVE LOC CONTAIN
# RESTART 2CADR

W('01,2000', 0o00063, 'SIZETAB', 'TC', '1.2SPOT -12006', line=101)
W('01,2001', 0o00010, '', 'TC', '1.3SPOT -12004', line=102)
W('01,2002', 0o00063, '', 'TC', '2.2SPOT -12006', line=103)
W('01,2003', 0o00024, '', 'TC', '2.3SPOT -12004', line=104)
W('01,2004', 0o00063, '', 'TC', '3.2SPOT -12006', line=105)
W('01,2005', 0o00043, '', 'TC', '3.3SPOT -12004', line=106)
W('01,2006', 0o00063, '', 'TC', '4.2SPOT -12006', line=107)
W('01,2007', 0o00107, '', 'TC', '4.3SPOT -12004', line=108)
W('01,2010', 0o00242, '', 'TC', '5.2SPOT -12006', line=109)
W('01,2011', 0o00260, '', 'TC', '5.3SPOT -12004', line=110)
W('01,2012', 0o00336, '', 'TC', '6.2SPOT -12006', line=111)
W('01,2013', 0o00346, '', 'TC', '6.3SPOT -12004', line=112)
S('1.2SPOT', 'equals', 0o12071, line=113)

# ANY MORE GROUP 1.EVEN RESTART VALUES SHOULD GO HERE

W('01,2014', 0o00170, '1.3SPOT', 'DEC', '120', 'THIS NUMBER MUST BE EQUAL C(JTAGTIME)', kind='data', line=117)
#   EBANK= AOG
W('01,2015', 0o74570, '', '-2CADR', 'SETJTAG', kind='data', line=119)
W('01,2016', 0o45711, kind='data', line=119)

W('01,2017', 0o10000, '1.5SPOT', 'OCT', '10000', kind='data', line=121)
#   EBANK= DAPDATR1
W('01,2020', 0o02405, '', '2CADR', 'REDO40.9', kind='data', line=123)
W('01,2021', 0o34066, kind='data', line=123)

W('01,2022', 0o10000, '1.7SPOT', 'OCT', '10000', kind='data', line=125)
#   EBANK= ESTROKER
W('01,2023', 0o02074, '', '2CADR', 'RELINUS', kind='data', line=127)
W('01,2024', 0o56066, kind='data', line=127)

W('01,2025', 0o10000, '1.11SPOT', 'OCT', '10000', kind='data', line=129)
#   EBANK= ESTROKER
W('01,2026', 0o02345, '', '2CADR', 'PIKUP20', kind='data', line=131)
W('01,2027', 0o76066, kind='data', line=131)

# ANY MORE GROUP 1.ODD RESTART VALUES SHOULD GO HERE

S('2.2SPOT', 'equals', 0o12071, line=135)

# ANY MORE GROUP 2.EVEN RESTART VALUES SHOULD GO HERE
# Page 213

W('01,2030', 0o02654, '2.3SPOT', 'GENADR', '600SECS', kind='data', line=140)
W('01,2031', 0o75150, '', '-GENADR', 'STATEINT', kind='data', line=141)
#   EBANK= RRECTCSM
W('01,2032', 0o26063, '', 'BBCON', 'STATEINT', kind='data', line=143)

W('01,2033', 0o05000, '2.5SPOT', 'OCT', '05000', kind='data', line=145)
#   EBANK= RRECTCSM
W('01,2034', 0o02636, '', '2CADR', 'STATINT1', kind='data', line=147)
W('01,2035', 0o26063, kind='data', line=147)

W('01,2036', 0o10000, '2.7SPOT', 'OCT', '10000', kind='data', line=149)
#   EBANK= MRKBUF2
W('01,2037', 0o02630, '', '2CADR', 'R22', kind='data', line=151)
W('01,2040', 0o70067, kind='data', line=151)

W('01,2041', 0o14000, '2.11SPOT', 'OCT', '14000', kind='data', line=153)
#   EBANK= LANDMARK
W('01,2042', 0o02576, '', '2CADR', 'V94ENTER', kind='data', line=155)
W('01,2043', 0o62065, kind='data', line=155)

W('01,2044', 0o10000, '2.13SPOT', 'OCT', '10000', kind='data', line=157)
#   EBANK= MRKBUF2
W('01,2045', 0o02377, '', '2CADR', 'REDOR22', kind='data', line=159)
W('01,2046', 0o56067, kind='data', line=159)

# ANY MORE GROUP 2.ODD RESTART VALUES SHOULD GO HERE

S('3.2SPOT', 'equals', 0o12071, line=163)

# ANY MORE GROUP 3.EVEN RESTART VALUES SHOULD GO HERE

W('01,2047', 0o20000, '3.3SPOT', 'OCT', '20000', kind='data', line=167)
#   EBANK= TGO
W('01,2050', 0o02427, '', '2CADR', 'S40.13', kind='data', line=169)
W('01,2051', 0o34067, kind='data', line=169)

W('01,2052', 0o00000, '3.5SPOT', 'DEC', '0', kind='data', line=171)
W('01,2053', 0o00000, '', 'DEC', '0', kind='data', line=172)
W('01,2054', 0o00000, '', 'DEC', '0', kind='data', line=173)
W('01,2055', 0o22000, '3.7SPOT', 'OCT', '22000', kind='data', line=174)
#   EBANK= TEPHEM
W('01,2056', 0o02117, '', '2CADR', 'MATRXJOB', kind='data', line=176)
W('01,2057', 0o70063, kind='data', line=176)

W('01,2060', 0o22000, '3.11SPOT', 'OCT', '22000', kind='data', line=178)
#   EBANK= TEPHEM
W('01,2061', 0o02253, '', '2CADR', 'REP11', kind='data', line=180)
W('01,2062', 0o70063, kind='data', line=180)

W('01,2063', 0o22000, '3.13SPOT', 'OCT', '22000', kind='data', line=182)
#   EBANK= TEPHEM
W('01,2064', 0o02026, '', '2CADR', 'REP11A', kind='data', line=184)
W('01,2065', 0o70063, kind='data', line=184)

W('01,2066', 0o76347, '3.15SPOT', '-GENADR', 'TGO +1', kind='data', line=186)
#   EBANK= TGO
W('01,2067', 0o75011, '', '-2CADR', 'ENGINOFF', kind='data', line=188)
W('01,2070', 0o27710, kind='data', line=188)

# Page 214
# ANY MORE GROUP 3.ODD RESTART VALUES SHOULD GO HERE

W('01,2071', 0o77777, '4.2SPOT', 'OCT', '77777', kind='data', line=193)
#   EBANK= TIG
W('01,2072', 0o75207, '', '-2CADR', 'PRECHECK', kind='data', line=195)
W('01,2073', 0o27710, kind='data', line=195)

W('01,2074', 0o30000, '', 'OCT', '30000', kind='data', line=197)
#   EBANK= DELVIMU
W('01,2075', 0o02534, '', '2CADR', 'P47BODY', kind='data', line=199)
W('01,2076', 0o50067, kind='data', line=199)

W('01,2077', 0o77777, '4.4SPOT', 'OCT', '77777', kind='data', line=201)
#   EBANK= TIG
W('01,2100', 0o75207, '', '-2CADR', 'PRECHECK', kind='data', line=203)
W('01,2101', 0o27710, kind='data', line=203)

W('01,2102', 0o05664, '', 'DEC', '2996', kind='data', line=205)
#   EBANK= DAPDATR1
W('01,2103', 0o75443, '', '-2CADR', 'TTG/0', kind='data', line=207)
W('01,2104', 0o27711, kind='data', line=207)

W('01,2105', 0o77777, '4.6SPOT', 'OCT', '77777', kind='data', line=209)
#   EBANK= TIG
W('01,2106', 0o75207, '', '-2CADR', 'PRECHECK', kind='data', line=211)
W('01,2107', 0o27710, kind='data', line=211)

W('01,2110', 0o04700, '', 'DEC', '2496', kind='data', line=213)
#   EBANK= TIG
W('01,2111', 0o75203, '', '-2CADR', 'TIG-5', kind='data', line=215)
W('01,2112', 0o27710, kind='data', line=215)

# ANY MORE GROUP 4.EVEN RESTART VALUES SHOULD GO HERE

W('01,2113', 0o00050, '4.3SPOT', 'DEC', '40', kind='data', line=219)
#   EBANK= PACTOFF
W('01,2114', 0o75115, '', '-2CADR', 'DOTVCON', kind='data', line=221)
W('01,2115', 0o27711, kind='data', line=221)

W('01,2116', 0o00240, '4.5SPOT', 'DEC', '160', kind='data', line=223)
#   EBANK= PACTOFF
W('01,2117', 0o75064, '', '-2CADR', 'DOSTRULL', kind='data', line=225)
W('01,2120', 0o27711, kind='data', line=225)

W('01,2121', 0o00764, '4.7SPOT', 'DEC', '500', kind='data', line=227)
#   EBANK= PACTOFF
W('01,2122', 0o75165, '', '-2CADR', 'TIG-0', kind='data', line=229)
W('01,2123', 0o27711, kind='data', line=229)

W('01,2124', 0o00372, '4.11SPOT', 'DEC', '250', kind='data', line=231)
#   EBANK= DAPDATR1
W('01,2125', 0o74235, '', '-2CADR', 'V97E40.6', kind='data', line=233)
W('01,2126', 0o27711, kind='data', line=233)

W('01,2127', 0o00310, '4.13SPOT', 'DEC', '200', kind='data', line=235)
#   EBANK= WHOCARES
W('01,2130', 0o74270, '', '-2CADR', 'R40ENABL', kind='data', line=237)
W('01,2131', 0o27710, kind='data', line=237)

W('01,2132', 0o16000, '4.15SPOT', 'OCT', '16000', 'PRELAUNCH OPTICAL VERIFICATION', kind='data', line=239)
#   EBANK= OGC
# Page 215
W('01,2133', 0o02000, '', '2CADR', 'COMPVER', 'CALLS FOR OPTICS DATA AGAIN (STD LEADIN)', kind='data', line=242)
W('01,2134', 0o66065, kind='data', line=242)

W('01,2135', 0o16000, '4.17SPOT', 'OCT', '16000', ' PRELAUNCH AZIMUTH CHANGE', kind='data', line=244)
#   EBANK= XSM
W('01,2136', 0o03742, '', '2CADR', 'AZMTHCG1', kind='data', line=246)
W('01,2137', 0o66065, kind='data', line=246)

W('01,2140', 0o01672, '4.21SPOT', 'GENADR', 'P40TMP', 'DELTA TIME USED IN SETTING UP', kind='data', line=248)
W('01,2141', 0o75340, '', '-GENADR', 'TIGBLNK', 'LONG CALL OF TIGBLNK  BY P40,P41', kind='data', line=249)
#   EBANK= P40TMP
W('01,2142', 0o50067, '', 'BBCON', 'TIGBLNK', kind='data', line=251)
W('01,2143', 0o12000, '4.23SPOT', 'OCT', '12000', 'PROTECT  P40S/SV BY P40 P41', kind='data', line=252)
#   EBANK= TIG
W('01,2144', 0o02204, '', '2CADR', 'P40S/SV', kind='data', line=254)
W('01,2145', 0o50067, kind='data', line=254)

W('01,2146', 0o24000, '4.25SPOT', 'OCT', '24000', kind='data', line=256)
#   EBANK= BESTI
W('01,2147', 0o02000, '', '2CADR', 'PROG52', kind='data', line=258)
W('01,2150', 0o32060, kind='data', line=258)

W('01,2151', 0o00372, '4.27SPOT', 'DEC', '250', kind='data', line=260)
#   EBANK= PACTOFF
W('01,2152', 0o74775, '', '-2CADR', 'DOTVCRCS', kind='data', line=262)
W('01,2153', 0o27711, kind='data', line=262)

W('01,2154', 0o13000, '4.31SPOT', 'OCT', '13000', kind='data', line=264)
#   EBANK= STAR
W('01,2155', 0o02533, '', '2CADR', 'R51 +1', kind='data', line=266)
W('01,2156', 0o30065, kind='data', line=266)

W('01,2157', 0o04064, '4.33SPOT', 'DEC', '2100', 'PROTECT CONTINUING JOB TO START P63', kind='data', line=268)
#   EBANK= AOG
W('01,2160', 0o75403, '', '-2CADR', 'WAKEP62', kind='data', line=270)
W('01,2161', 0o23711, kind='data', line=270)

W('01,2162', 0o12000, '4.35SPOT', 'OCT', '12000', kind='data', line=272)
#   EBANK= DAPDATR1
W('01,2163', 0o02246, '', '2CADR', 'POSTBURN', kind='data', line=274)
W('01,2164', 0o50066, kind='data', line=274)

W('01,2165', 0o00764, '4.37SPOT', 'DEC', '500', kind='data', line=276)
#   EBANK= TIG
W('01,2166', 0o75222, '', '-2CADR', 'TIGAVEG', kind='data', line=278)
W('01,2167', 0o27710, kind='data', line=278)

W('01,2170', 0o17000, '4.41SPOT', 'OCT', '17000', 'PROTECT DISPLAY JOB IN P67', kind='data', line=280)
#   EBANK= AOG
W('01,2171', 0o02512, '', '2CADR', 'P67.1', kind='data', line=282)
W('01,2172', 0o54066, kind='data', line=282)

W('01,2173', 0o76003, '4.43SPOT', '-GENADR', 'S61DT', 'PROTECT TASK TO START PREREAD,ENTRY', kind='data', line=284)
#   EBANK= S61DT  # S61.1C WILL CHANGE EBANK=EB7 FOR PREREAD
W('01,2174', 0o75212, '', '-2CADR', 'S61.1C', kind='data', line=286)
W('01,2175', 0o23711, kind='data', line=286)

W('01,2176', 0o13000, '4.45SPOT', 'OCT', '13000', 'PROTECT CONTINUING JOB S61.1', kind='data', line=288)
#   EBANK= AOG  # (ENTRY IMU ALIGNMENT)
# Page 216
W('01,2177', 0o02603, '', '2CADR', 'S61.1A -1', kind='data', line=291)
W('01,2200', 0o54066, kind='data', line=291)

W('01,2201', 0o17000, '4.47SPOT', 'OCT', '17000', 'PROTECT HUNTEST ITERATION.', kind='data', line=293)
#   EBANK= AOG
W('01,2202', 0o03014, '', '2CADR', 'PRE-HUNT', kind='data', line=295)
W('01,2203', 0o52066, kind='data', line=295)

W('01,2204', 0o77777, '4.51SPOT', 'OCT', '77777', 'PROTECT FDAI ATTITUDE', kind='data', line=297)
#   EBANK= BODY3  # ERROR DISPLAY IN P11
W('01,2205', 0o75457, '', '-2CADR', 'ATERTASK', kind='data', line=299)
W('01,2206', 0o07711, kind='data', line=299)

W('01,2207', 0o77777, '4.53SPOT', 'DEC', '-0', kind='data', line=301)
#   EBANK= END-E7  # EBANK7 FOR TIG
W('01,2210', 0o74254, '', '-2CADR', 'V97ETASK', kind='data', line=303)
W('01,2211', 0o27710, kind='data', line=303)

W('01,2212', 0o13000, '4.55SPOT', 'OCT', '13000', 'PROTECT  P65 RESPONSIVE DISPLAY.', kind='data', line=305)
#   EBANK= RTINIT
W('01,2213', 0o02457, '', '2CADR', 'P65.1', kind='data', line=307)
W('01,2214', 0o54067, kind='data', line=307)

W('01,2215', 0o76105, '4.57SPOT', '-GENADR', 'P40TMP', kind='data', line=309)
#   EBANK= P40TMP
W('01,2216', 0o75277, '', '-2CADR', 'TIGON', kind='data', line=311)
W('01,2217', 0o27710, kind='data', line=311)

W('01,2220', 0o77777, '4.61SPOT', 'OCT', '77777', kind='data', line=313)
#   EBANK= PACTOFF
W('01,2221', 0o75152, '', '-2CADR', 'IGNITION', kind='data', line=315)
W('01,2222', 0o27711, kind='data', line=315)

W('01,2223', 0o77777, '4.63SPOT', 'OCT', '77777', kind='data', line=317)
#   EBANK= PACTOFF
W('01,2224', 0o75003, '', '-2CADR', 'DOSPSOFF', kind='data', line=319)
W('01,2225', 0o27711, kind='data', line=319)

W('01,2226', 0o00012, '4.65SPOT', 'DEC', '10', kind='data', line=321)
#   EBANK= TIG
W('01,2227', 0o75203, '', '-2CADR', 'TIG-5', kind='data', line=323)
W('01,2230', 0o27710, kind='data', line=323)

W('01,2231', 0o77777, '4.67SPOT', 'DEC', '-0', kind='data', line=325)
#   EBANK= CSMMASS
W('01,2232', 0o74336, '', '-2CADR', 'V97TTASK', kind='data', line=327)
W('01,2233', 0o27711, kind='data', line=327)

W('01,2234', 0o00372, '4.71SPOT', 'DEC', '250', kind='data', line=329)
#   EBANK= DAPDATR1  # (FOR RCSDAPON)
W('01,2235', 0o74321, '', '-2CADR', 'V97TRCS', kind='data', line=331)
W('01,2236', 0o27711, kind='data', line=331)

W('01,2237', 0o77777, '4.73SPOT', 'DEC', '-0', kind='data', line=333)
#   EBANK= V97VCNTR
W('01,2240', 0o74304, '', '-2CADR', 'V97PTASK', kind='data', line=335)
W('01,2241', 0o27711, kind='data', line=335)

W('01,2242', 0o77777, '4.75SPOT', 'DEC', '-0', kind='data', line=337)
#   EBANK= DAPDATR1
W('01,2243', 0o74242, '', '-2CADR', 'SPSOFF97', kind='data', line=339)
W('01,2244', 0o27711, kind='data', line=339)

# Page 217
W('01,2245', 0o77777, '4.77SPOT', 'DEC', '-0', kind='data', line=342)
#   EBANK= PACTOFF
W('01,2246', 0o75165, '', '-2CADR', 'TIG-0', kind='data', line=344)
W('01,2247', 0o27711, kind='data', line=344)

# ANY MORE GROUP 4.ODD RESTART VALUES SHOULD GO HERE

W('01,2250', 0o32000, '5.2SPOT', 'OCT', '32000', kind='data', line=348)
#   EBANK= DVCNTR
W('01,2251', 0o03236, '', '2CADR', 'NORMLIZE', kind='data', line=350)
W('01,2252', 0o76067, kind='data', line=350)

W('01,2253', 0o00310, '', 'DEC', '200', kind='data', line=352)
#   EBANK= AOG
W('01,2254', 0o74472, '', '-2CADR', 'REREADAC', kind='data', line=354)
W('01,2255', 0o01711, kind='data', line=354)

W('01,2256', 0o20000, '5.4SPOT', 'OCT', '20000', kind='data', line=356)
#   EBANK= DVCNTR
W('01,2257', 0o03104, '', '2CADR', 'SERVICER', kind='data', line=358)
W('01,2260', 0o76067, kind='data', line=358)

W('01,2261', 0o00310, '', 'DEC', '200', kind='data', line=360)
#   EBANK= AOG
W('01,2262', 0o74472, '', '-2CADR', 'REREADAC', kind='data', line=362)
W('01,2263', 0o01711, kind='data', line=362)

# ANY MORE GROUP 5.EVEN RESTART VALUES SHOULD GO HERE

W('01,2264', 0o00310, '5.3SPOT', 'DEC', '200', kind='data', line=366)
#   EBANK= AOG
W('01,2265', 0o74472, '', '-2CADR', 'REREADAC', kind='data', line=368)
W('01,2266', 0o01711, kind='data', line=368)

W('01,2267', 0o77777, '5.5SPOT', 'OCT', '77777', kind='data', line=370)
#   EBANK= AOG
W('01,2270', 0o75026, '', '-2CADR', 'REDO5.5', kind='data', line=372)
W('01,2271', 0o01711, kind='data', line=372)

W('01,2272', 0o20000, '5.7SPOT', 'OCT', '20000', 'USED BY PRELAUNCH', kind='data', line=374)
#   EBANK= XSM
W('01,2273', 0o02456, '', '2CADR', 'RSTGTS1', kind='data', line=376)
W('01,2274', 0o66065, kind='data', line=376)

W('01,2275', 0o77777, '5.11SPOT', 'OCT', '77777', kind='data', line=378)
#   EBANK= XSM
W('01,2276', 0o75175, '', '-2CADR', 'ALLOOP1', kind='data', line=380)
W('01,2277', 0o11712, kind='data', line=380)

W('01,2300', 0o20000, '5.13SPOT', 'OCT', '20000', kind='data', line=382)
#   EBANK= XSM
W('01,2301', 0o02527, '', '2CADR', 'WTLISTNT', kind='data', line=384)
W('01,2302', 0o66065, kind='data', line=384)

W('01,2303', 0o20000, '5.15SPOT', 'OCT', '20000', kind='data', line=386)
#   EBANK= XSM
W('01,2304', 0o03324, '', '2CADR', 'RESTEST1', kind='data', line=388)
W('01,2305', 0o66065, kind='data', line=388)

W('01,2306', 0o20000, '5.17SPOT', 'OCT', '20000', kind='data', line=390)
#   EBANK= XSM
# Page 218
W('01,2307', 0o05217, '', '2CADR', 'GEOSTRT4', kind='data', line=393)
W('01,2310', 0o04065, kind='data', line=393)

W('01,2311', 0o22000, '5.21SPOT', 'OCT', '22000', kind='data', line=395)
#   EBANK= XSM
W('01,2312', 0o02636, '', '2CADR', 'ALFLT1', kind='data', line=397)
W('01,2313', 0o66065, kind='data', line=397)

W('01,2314', 0o77777, '5.23SPOT', 'OCT', '77777', kind='data', line=399)
#   EBANK= XSM
W('01,2315', 0o75152, '', '-2CADR', 'SPECSTS', kind='data', line=401)
W('01,2316', 0o11712, kind='data', line=401)

W('01,2317', 0o20000, '5.25SPOT', 'OCT', '20000', kind='data', line=403)
#   EBANK= XSM
W('01,2320', 0o03335, '', '2CADR', 'RESTEST3', kind='data', line=405)
W('01,2321', 0o66065, kind='data', line=405)

W('01,2322', 0o20000, '5.27SPOT', 'OCT', '20000', kind='data', line=407)
#   EBANK= XSM
W('01,2323', 0o03303, '', '2CADR', 'RESTAIER', kind='data', line=409)
W('01,2324', 0o66065, kind='data', line=409)

W('01,2325', 0o00000, '5.31SPOT', 'DEC', '0', kind='data', line=411)
W('01,2326', 0o00000, '', 'DEC', '0', kind='data', line=412)
W('01,2327', 0o00000, '', 'DEC', '0', kind='data', line=413)
W('01,2330', 0o20000, '5.33SPOT', 'OCT', '20000', kind='data', line=414)
#   EBANK= XSM
W('01,2331', 0o03360, '', '2CADR', 'RESCHNG', kind='data', line=416)
W('01,2332', 0o66065, kind='data', line=416)

W('01,2333', 0o00000, '5.35SPOT', 'DEC', '0', kind='data', line=418)
W('01,2334', 0o00000, '', '2DEC', '0', kind='data', line=419)
W('01,2335', 0o00000, kind='data', line=419)

W('01,2336', 0o77777, '5.37SPOT', 'OCT', '77777', kind='data', line=421)
#   EBANK= AOG
W('01,2337', 0o74744, '', '-2CADR', 'CHEKAVEG', kind='data', line=423)
W('01,2340', 0o01711, kind='data', line=423)

W('01,2341', 0o77777, '5.41SPOT', 'OCT', '77777', 'TO PROTECT PREREAD AT TIG-30A', kind='data', line=425)
#   EBANK= DVCNTR  #    TIG-15 T+60
W('01,2342', 0o75076, '', '-2CADR', 'PREREAD', kind='data', line=427)
W('01,2343', 0o01710, kind='data', line=427)

# ANY MORE GROUP 5.ODD RESTART VALUES SHOULD GO HERE

W('01,2344', 0o77777, '6.2SPOT', 'OCT', '77777', "USED BY P40 AFTER GIMB DR TST TO REPOS'N", kind='data', line=431)
#   EBANK= AK  # ENGINE UNTIL TVCDAPON
W('01,2345', 0o75536, '', '-2CADR', 'PRE40.6', kind='data', line=433)
W('01,2346', 0o37711, kind='data', line=433)

W('01,2347', 0o00144, '', 'DEC', '100', kind='data', line=435)
#   EBANK= TTOGO
W('01,2350', 0o74517, '', '-2CADR', 'CLOKTASK', kind='data', line=437)
W('01,2351', 0o27710, kind='data', line=437)

# ANY MORE 6.ODD RESTART VALUES SHOULD GO HERE
# Page 219

W('01,2352', 0o00144, '6.3SPOT', 'DEC', '100', kind='data', line=442)
#   EBANK= TIG
W('01,2353', 0o74517, '', '-2CADR', 'CLOKTASK', kind='data', line=444)
W('01,2354', 0o27710, kind='data', line=444)

W('01,2355', 0o30000, '6.5SPOT', 'OCT', '30000', 'PROTECT INCREMENTING OF TIME2,TIME1 BY', kind='data', line=446)
#   EBANK= TEPHEM  # P27(UPDATE PROGRAM)
W('01,2356', 0o03573, '', '2CADR', 'TIMEDIDR', kind='data', line=448)
W('01,2357', 0o56063, kind='data', line=448)

W('01,2360', 0o00000, '6.7SPOT', 'OCT', '0', kind='data', line=450)
W('01,2361', 0o00000, '', 'OCT', '0', kind='data', line=451)
W('01,2362', 0o00000, '', 'OCT', '0', kind='data', line=452)

W('01,2363', 0o76052, '6.11SPOT', '-GENADR', 'CM/GYMDT', 'PROTECT TASK TO READ CDUS.', kind='data', line=454)
#   EBANK= CM/GYMDT  # FOR ENTRY DAP
W('01,2364', 0o75343, '', '-2CADR', 'READGYMB', kind='data', line=456)
W('01,2365', 0o45711, kind='data', line=456)

W('01,2366', 0o00000, '6.13SPOT', 'DEC', '0', kind='data', line=458)
W('01,2367', 0o00000, '', 'DEC', '0', kind='data', line=459)
W('01,2370', 0o00000, '', 'DEC', '0', kind='data', line=460)

# Page 220
# PROGRAM DESCRIPTION: NEWPHASE                                         DATE:  11 NOV 1966
# MOD: 1                                                                ASSEMBLY:  SUNBURST REV
# MOD BY: COPPS                                                         LOG SECTION: PHASE TABLE MAINTENANCE
# FUNCTIONAL DESCRIPTION:
#
# NEWPHASE IS THE QUICK WAY TO MAKE A NON VARIABLE PHASE CHANGE. IT INCLUDES THE OPTION OF SETTING
# TBASE OF THE GROUP.  IF TBASE IS TO BE SET, -C(TIME1) IS STORED IN THE TBASE TABLE AS FOLLOWS:
#
# (L-1)   TBASE0
# (L)     TBASE1  (IF GROUP=1)
# (L+1)
# (L+2)   TBASE2  (IF GROUP=2)
# -----
# (L+6)   TBASE4  (IF GROUP=4)
# (L+7)
# (L+8)   TBASE5  (IF GROUP=5)
#
# IN ANY CASE, THE NEGATIVE OF THE PHASE, FOLLOWED (IN THE NEXT REGISTER) BY THE PHASE, IS STORED IN THE
# PHASE TABLE AS FOLLOWS:
#
# (L)     -PHASE1 (IF GROUP=1)
# (L+1)   PHASE1
# (L+2)   -PHASE2 (IF GROUP=2)
# (L+3)   PHASE2
# -----
# (L+7)   PHASE4
# (L+8)   -PHASE5 (IF GROUP=5)
# (L+9)   PHASE5
#
# CALLING SEQUENCE:
# EXAMPLE IS FOR PLACING A PHASE OF FIVE INTO GROUP THREE:
#
# 1) IF TBASE IS NOT TO BE SET:
# L-1     CA      FIVE
# L       TC      NEWPHASE
# L+1     OCT     00003
#
# 2) IF TBASE IS TO BE SET:
# L-1     CS      FIVE
# L       TC      NEWPHASE
# L+1     OCT     00003
#
# SUBROUTINES CALLED: NONE
#
# NORMAL EXIT MODE: AT L+2 OF CALLING SEQUENCE
#
# ALARM OR ABORT EXITS: NONE
#
# OUTPUT: PHASE TABLE AND TBASE TABLE UPDATED
#
# ERASABLE INITIALIZATION REQ'D: NONE
# Page 221
# DEBRIS:  A,L,TEMPG

# ***WARNING*** THIS PROGRAM IS TO BE PLACED IN FIXED-FIXED AND UNSWITCHED ERASABLE.

#   BLOCK 02
#   SETLOC FFTAG1
#   BANK

#   COUNT* $$/PHASE

W('4114', 0o00004, 'NEWPHASE', 'INHINT', line=525)

W('4115', 0o54001, '', 'TS', 'L', 'SAVE FOR FURTHER USE', line=527)
W('4116', 0o50002, '', 'NDX', 'Q', 'OBTAIN THE GROUP NUMBER', line=528)
W('4117', 0o30000, '', 'CA', '0', line=529)
W('4120', 0o24002, '', 'INCR', 'Q', 'OBTAIN THE RETURN ADDRESS', line=530)
W('4121', 0o60000, '', 'DOUBLE', '', 'SAVE THE GROUP IN A FORM USED FOR', line=531)
W('4122', 0o54061, '', 'TS', 'TEMPG', 'INDEXING', line=532)

W('4123', 0o10001, '', 'CCS', 'L', 'SEE IF WE ARE TO SET TBASE', line=534)
W('4124', 0o14133, '', 'TCF', '+7', 'NO, THE DELTA T WAS POSITIVE', line=535)
W('4125', 0o14133, '', 'TCF', '+6', line=536)

W('4126', 0o24000, 'NUFAZ+10', 'INCR', 'A', 'SET TBASE AND STORE PHASE CORRECTLY', line=538)
W('4127', 0o54001, '', 'TS', 'L', line=539)
W('4130', 0o40025, '', 'CS', 'TIME1', 'SET TBASE', line=540)
W('4131', 0o50061, '', 'NDX', 'TEMPG', line=541)
W('4132', 0o55051, '', 'TS', 'TBASE1 -2', line=542)
W('4133', 0o40001, '', 'CS', 'L', 'NOW PUT THE PHASE IN THE RIGHT TABLE LOC', line=543)
W('4134', 0o50061, '', 'NDX', 'TEMPG', line=544)
W('4135', 0o52751, '', 'DXCH', '-PHASE1 -2', line=545)
W('4136', 0o00003, '', 'RELINT', line=546)
W('4137', 0o00002, '', 'TC', 'Q', 'NOW RETURN TO CALLER', line=547)
