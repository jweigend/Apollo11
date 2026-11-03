"""DOWNLINK_LISTS.agc -- Luminary 1A (build 099), Apollo 11 Lunar Module guidance computer

Converted from external/Apollo-11/Luminary099/DOWNLINK_LISTS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 193-205 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('DOWNLINK_LISTS', 'DOWNLINK_LISTS.agc', 'Luminary099', pages='193-205')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     DOWNLINK_LISTS.agc
# Purpose:      Part of the source code for Luminary 1A build 099.
# It is part of the source code for the Lunar Module's (LM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Hartmuth Gutsche <hgutsche@xplornet.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        193-205
# Mod history:  2009-05-19 HG   Transcribed from page images.
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

# Page 193
#   BANK 22
#   SETLOC DOWNTELM
#   BANK

#   EBANK= DNTMBUFF

# SPECIAL DOWNLINK OP CODES
# OP CODE         ADDRESS (EXAMPLE)       SENDS...                BIT 15          BITS 14-12      BITS 11-0
# -------         -----------------       --------                ------          ----------      ---------
# 1DNADR          TIME2                   (2 AGC WDS)             0               0               ECADR
# 2DNADR          TEPHEM                  (4 AGC WDS)             0               1               ECADR
# 3DNADR          VGBODY                  (6 AGC WDS)             0               2               ECADR
# 4DNADR          STATE                   (8 AGC WDS)             0               3               ECADR
# 5DNADR          UPBUFF                  (10 AGC WDS)            0               4               ECADR
# 6DNADR          DSPTAB                  (12 AGC WDS)            0               5               ECADR
# DNCHAN          30                      CHANNELS                0               7               CHANNEL
# ADDRESS
# DNPTR           NEXTLIST                POINTS TO NEXT          0               6               ADRES
# LIST
#
# DOWNLIST FORMAT DEFINITIONS AND RULES --
# 1. END OF A LIST = -XDNADR (X = 1 TO 6), -DNPTR, OR -DNCHAN.
# 2. SNAPSHOT SUBLIST = LIST WHICH STARTS WITH A -1DNADR.
# 3. SNAPSHOT SUBLIST CAN ONLY CONTAIN 1DNADRS.
# 4. TIME2 1DNADR MUST BE LOCATED IN THE CONTROL LIST OF A DOWNLIST.
# 5. ERASABLE DOWN TELEMETRY WORDS SHOULD BE GROUPED IN SEQUENTIAL
# LOCATIONS AS MUCH AS POSSIBLE TO SAVE STORAGE USED BY DOWNLINK LISTS.

#   COUNT* $$/DLIST
S('ERASZERO', 'equals', 0o7, line=57)
S('UNKNOWN', 'equals', 0o7, line=58)
S('SPARE', 'equals', 0o7, line=59)  # USE SPARE TO INDICATE AVAILABLE SPACE
W('05,2065', 0o77340, 'LOWIDCOD', 'OCT', '77340', 'LOW ID CODE', kind='data', line=60)

S('NOMDNLST', 'equals', 0o22172, line=62)  # FRESH START AND POST P27 DOWNLIST

S('AGSLIST', 'equals', 0o22407, line=64)

S('UPDNLIST', 'equals', 0o22407, line=66)  # UPDATE PROGRAM (P27) DOWNLIST

# Page 194
# LM ORBITAL MANEUVERS LIST
#
# --------------------- CONTROL LIST -------------------------

S('LMORBMDL', 'equals', 0o22066, line=73)  # SEND ID BY SPECIAL CODING
W('05,2066', 0o32127, '', 'DNPTR', 'LMORBM01', 'COLLECT SNAPSHOT', kind='data', line=74)
W('05,2067', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=75)
W('05,2070', 0o03451, '', '1DNADR', 'DELLT4', 'DELLT4,+1', kind='data', line=76)
W('05,2071', 0o13443, '', '3DNADR', 'RTARG', 'RTARG,+1...+5', kind='data', line=77)
W('05,2072', 0o02256, '', '1DNADR', 'ELEV', 'ELEV,+1', kind='data', line=78)
W('05,2073', 0o01344, '', '1DNADR', 'TEVENT', 'TEVENT,+1', kind='data', line=79)
W('05,2074', 0o25733, '', '6DNADR', 'REFSMMAT', 'REFSMMAT +0...+11D', kind='data', line=80)
W('05,2075', 0o03633, '', '1DNADR', 'TCSI', 'TCSI,+1', kind='data', line=81)
W('05,2076', 0o12266, '', '3DNADR', 'DELVEET1', 'DELVEET1 +0...+5', kind='data', line=82)
W('05,2077', 0o13700, '', '3DNADR', 'VGTIG', 'VGTIG +0...+5', kind='data', line=83)
W('05,2100', 0o01340, '', '1DNADR', 'DNLRVELZ', 'DNLRVELZ,DNLRALT', kind='data', line=84)
W('05,2101', 0o03630, '', '1DNADR', 'TPASS4', 'TPASS4,+1', kind='data', line=85)
W('05,2102', 0o32136, '', 'DNPTR', 'LMORBM02', 'COMMON DATA', kind='data', line=86)
W('05,2103', 0o00024, '', '1DNADR', 'TIME2', 'TIME2/1', kind='data', line=87)
W('05,2104', 0o32145, '', 'DNPTR', 'LMORBM03', 'COLLECT SNAPSHOT', kind='data', line=88)
W('05,2105', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=89)
W('05,2106', 0o32154, '', 'DNPTR', 'LMORBM04', 'COMMON DATA', kind='data', line=90)
W('05,2107', 0o07115, '', '2DNADR', 'POSTORKU', 'POSTORKU,NEGTORKU,POSTORKV,NEGTORKV', kind='data', line=91)
W('05,2110', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=92)
W('05,2111', 0o01776, '', '1DNADR', 'TCDH', 'TCDH,+1', kind='data', line=93)
W('05,2112', 0o12274, '', '3DNADR', 'DELVEET2', 'DELVEET2 +0...+5', kind='data', line=94)
W('05,2113', 0o03635, '', '1DNADR', 'TTPI', 'TTPI,+1', kind='data', line=95)
W('05,2114', 0o12365, '', '3DNADR', 'DELVEET3', 'DELVEET3 +0...+5', kind='data', line=96)
W('05,2115', 0o01333, '', '1DNADR', 'DNRRANGE', 'DNRRANGE,DNRRDOT', kind='data', line=97)
W('05,2116', 0o05336, '', '2DNADR', 'DNLRVELX', 'DNLRVELX,DNLRVELY,DNLRVELZ,DNLRALT', kind='data', line=98)
W('05,2117', 0o03577, '', '1DNADR', 'DIFFALT', 'DIFFALT,+1', kind='data', line=99)
W('05,2120', 0o01331, '', '1DNADR', 'LEMMASS', 'LEMMASS,CSMMASS', kind='data', line=100)
W('05,2121', 0o01302, '', '1DNADR', 'IMODES30', 'IMODES30,IMODES33', kind='data', line=101)
W('05,2122', 0o03441, '', '1DNADR', 'TIG', 'TIG,+1', kind='data', line=102)
W('05,2123', 0o32157, '', 'DNPTR', 'LMORBM05', 'COMMON DATA', kind='data', line=103)
W('05,2124', 0o32170, '', 'DNPTR', 'LMORBM06', 'COMMON DATA', kind='data', line=104)
W('05,2125', 0o00007, '', '1DNADR', 'SPARE', 'FORMERLY PIF', kind='data', line=105)
W('05,2126', 0o74261, '', '-1DNADR', 'TGO', 'TGO,+1', kind='data', line=106)

# --------------------- SUB-LISTS ---------------------------

W('05,2127', 0o76056, 'LMORBM01', '-1DNADR', 'R-OTHER +2', 'R-OTHER +2,+3         SNAPSHOT', kind='data', line=110)
W('05,2130', 0o01723, '', '1DNADR', 'R-OTHER +4', 'R-OTHER +4,+5', kind='data', line=111)
W('05,2131', 0o01725, '', '1DNADR', 'V-OTHER', 'V-OTHER,+1', kind='data', line=112)
W('05,2132', 0o01727, '', '1DNADR', 'V-OTHER +2', 'V-OTHER +2,+3', kind='data', line=113)
W('05,2133', 0o01731, '', '1DNADR', 'V-OTHER +4', 'V-OTHER +4,+5', kind='data', line=114)
W('05,2134', 0o01570, '', '1DNADR', 'T-OTHER', 'T-OTHER,+1', kind='data', line=115)
W('05,2135', 0o76060, '', '-1DNADR', 'R-OTHER', 'R-OTHER +0,+1', kind='data', line=116)

W('05,2136', 0o04320, 'LMORBM02', '2DNADR', 'REDOCTR', 'REDOCTR,THETAD,+1,+2  COMMON DATA', kind='data', line=118)
# Page 195
W('05,2137', 0o01432, '', '1DNADR', 'RSBBQ', 'RSBBQ,+1', kind='data', line=120)
W('05,2140', 0o07021, '', '2DNADR', 'OMEGAP', 'OMEGAP,OMEGAQ,OMEGAR,GARBAGE', kind='data', line=121)
W('05,2141', 0o07235, '', '2DNADR', 'CDUXD', 'CDUXD,CDUYD,CDUZD,GARBAGE', kind='data', line=122)
W('05,2142', 0o04032, '', '2DNADR', 'CDUX', 'CDUX,CDUY,CDUZ,CDUT', kind='data', line=123)
W('05,2143', 0o24074, '', '6DNADR', 'STATE', 'STATE +0...+11D (FLAGWORDS)', kind='data', line=124)
W('05,2144', 0o52754, '', '-6DNADR', 'DSPTAB', 'DSPTAB TABLES', kind='data', line=125)

W('05,2145', 0o76555, 'LMORBM03', '-1DNADR', 'RN +2', 'RN +2,+3              SNAPSHOT', kind='data', line=127)
W('05,2146', 0o01224, '', '1DNADR', 'RN +4', 'RN +4,+5', kind='data', line=128)
W('05,2147', 0o01226, '', '1DNADR', 'VN', 'VN,+1', kind='data', line=129)
W('05,2150', 0o01230, '', '1DNADR', 'VN +2', 'VN +2,+3', kind='data', line=130)
W('05,2151', 0o01232, '', '1DNADR', 'VN +4', 'VN +4,+5', kind='data', line=131)
W('05,2152', 0o01234, '', '1DNADR', 'PIPTIME', 'PIPTIME,+1', kind='data', line=132)
W('05,2153', 0o76557, '', '-1DNADR', 'RN', 'RN,+1', kind='data', line=133)

W('05,2154', 0o07243, 'LMORBM04', '2DNADR', 'OMEGAPD', 'OMEGAPD,OMEGAQD,OMEGARD,GARBAGE', kind='data', line=135)
W('05,2155', 0o10372, '', '3DNADR', 'CADRFLSH', 'CADRFLSH,+1,+2,FAILREG,+1,+2', kind='data', line=136)
W('05,2156', 0o77667, '', '-1DNADR', 'RADMODES', 'RADMODES,DAPBOOLS     COMMON DATA', kind='data', line=137)

W('05,2157', 0o07021, 'LMORBM05', '2DNADR', 'OMEGAP', 'OMEGAP,OMEGAQ,OMEGAR,GARBAGE', kind='data', line=139)
W('05,2160', 0o07235, '', '2DNADR', 'CDUXD', 'CDUXD,CDUYD,CDUZD,GARBAGE', kind='data', line=140)
W('05,2161', 0o04032, '', '2DNADR', 'CDUX', 'CDUX,CDUY,CDUZ,CDUT', kind='data', line=141)
W('05,2162', 0o03024, '', '1DNADR', 'ALPHAQ', 'ALPHAQ,ALPHAR         COMMON DATA', kind='data', line=142)
W('05,2163', 0o03113, '', '1DNADR', 'POSTORKP', 'POSTORKP,NEGTORKP', kind='data', line=143)
W('05,2164', 0o34011, '', 'DNCHAN', '11', 'CHANNELS 11,12', kind='data', line=144)
W('05,2165', 0o34013, '', 'DNCHAN', '13', 'CHANNELS 13,14', kind='data', line=145)
W('05,2166', 0o34030, '', 'DNCHAN', '30', 'CHANNELS 30,31', kind='data', line=146)
W('05,2167', 0o43745, '', '-DNCHAN', '32', 'CHANNELS 32,33', kind='data', line=147)

W('05,2170', 0o03560, 'LMORBM06', '1DNADR', 'PIPTIME1', 'PIPTIME,+1            COMMON DATA', kind='data', line=149)
W('05,2171', 0o67453, '', '-3DNADR', 'DELV', 'DELV +0...+5', kind='data', line=150)

# --------------------------------------------------------------------

# Page 196
# LM COAST AND ALIGNMENT DOWNLIST
#
# ---------------------- CONTROL LIST --------------------------------

S('LMCSTADL', 'equals', 0o22172, line=159)  # SEND ID BY SPECIAL CODING
W('05,2172', 0o32127, '', 'DNPTR', 'LMCSTA01', 'COLLECT SNAPSHOT', kind='data', line=160)
W('05,2173', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=161)
W('05,2174', 0o02020, '', '1DNADR', 'AGSK', 'AGSK,+1', kind='data', line=162)
W('05,2175', 0o02774, '', '1DNADR', 'TALIGN', 'TALIGN,+1', kind='data', line=163)
W('05,2176', 0o07115, '', '2DNADR', 'POSTORKU', 'POSTORKU,NEGTORKU,POSTORKV,NEGTORKV', kind='data', line=164)
W('05,2177', 0o01333, '', '1DNADR', 'DNRRANGE', 'DNRRANGE,DNRRDOT', kind='data', line=165)
W('05,2200', 0o01344, '', '1DNADR', 'TEVENT', 'TEVENT,+1', kind='data', line=166)
W('05,2201', 0o25733, '', '6DNADR', 'REFSMMAT', 'REFSMMAT +0...+11D', kind='data', line=167)
W('05,2202', 0o00735, '', '1DNADR', 'AOTCODE', 'AOTCODE,GARBAGE', kind='data', line=168)
W('05,2203', 0o12022, '', '3DNADR', 'RLS', 'RLS +0...+5', kind='data', line=169)
W('05,2204', 0o05336, '', '2DNADR', 'DNLRVELX', 'DNLRVELX,DNLRVELY,DNLRVELZ,DNLRALT', kind='data', line=170)
W('05,2205', 0o32224, '', 'DNPTR', 'LMCSTA06', 'COMMON DATA', kind='data', line=171)
W('05,2206', 0o32136, '', 'DNPTR', 'LMCSTA02', 'COMMON DATA', kind='data', line=172)
W('05,2207', 0o00024, '', '1DNADR', 'TIME2', 'TIME2/1', kind='data', line=173)
W('05,2210', 0o32145, '', 'DNPTR', 'LMCSTA03', 'COLLECT SNAPSHOT', kind='data', line=174)
W('05,2211', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=175)
W('05,2212', 0o32154, '', 'DNPTR', 'LMCSTA04', 'COMMON DATA', kind='data', line=176)
W('05,2213', 0o32226, '', 'DNPTR', 'LMCSTA07', 'COMMON DATA', kind='data', line=177)
W('05,2214', 0o05336, '', '2DNADR', 'DNLRVELX', 'DNLRVELX,DNLRVELY,DNLRVELZ,DNLRALT', kind='data', line=178)
W('05,2215', 0o04036, '', '2DNADR', 'CDUS', 'CDUS,PIPAX,PIPAY,PIPAZ', kind='data', line=179)
W('05,2216', 0o00112, '', '1DNADR', 'LASTYCMD', 'LASTYCMD,LASTXCMD', kind='data', line=180)
W('05,2217', 0o01331, '', '1DNADR', 'LEMMASS', 'LEMMASS,CSMMASS', kind='data', line=181)
W('05,2220', 0o01302, '', '1DNADR', 'IMODES30', 'IMODES30,IMODES33', kind='data', line=182)
W('05,2221', 0o03441, '', '1DNADR', 'TIG', 'TIG,+1', kind='data', line=183)
W('05,2222', 0o32157, '', 'DNPTR', 'LMCSTA05', 'COMMON DATA', kind='data', line=184)
W('05,2223', 0o52754, '', '-6DNADR', 'DSPTAB', 'DSPTAB +0...+11D TABLE', kind='data', line=185)

# ---------------------- SUB-LISTS --------------------------

S('LMCSTA01', 'equals', 0o22127, line=189)  # COMMON DOWNLIST DATA
S('LMCSTA02', 'equals', 0o22136, line=190)  # COMMON DOWNLIST DATA
S('LMCSTA03', 'equals', 0o22145, line=191)  # COMMON DOWNLIST DATA
S('LMCSTA04', 'equals', 0o22154, line=192)  # COMMON DOWNLIST DATA
S('LMCSTA05', 'equals', 0o22157, line=193)  # COMMON DOWNLIST DATA

W('05,2224', 0o05700, 'LMCSTA06', '2DNADR', 'X789', 'X789 +0...+3          COMMON DATA', kind='data', line=195)
W('05,2225', 0o77665, '', '-1DNADR', 'LASTYCMD', 'LASTYCMD,LASTXCMD', kind='data', line=196)
W('05,2226', 0o12737, 'LMCSTA07', '3DNADR', 'OGC', 'OGC,+1,IGC,+1,MGC,+1  COMMON DATA', kind='data', line=197)
W('05,2227', 0o02755, '', '1DNADR', 'BESTI', 'BESTI,BESTJ', kind='data', line=198)
W('05,2230', 0o12760, '', '3DNADR', 'STARSAV1', 'STARSAV1 +0...+5', kind='data', line=199)
W('05,2231', 0o65011, '', '-3DNADR', 'STARSAV2', 'STARSAV2 +0...+5', kind='data', line=200)
# Page 197
# -----------------------------------------------------------

# Page 198
# LM RENDEZVOUS AND PRE-THRUST DOWNLIST
#
# --------------------- CONTROL LIST ------------------------

S('LMRENDDL', 'equals', 0o22232, line=209)  # SEND ID BY SPECIAL CODING
W('05,2232', 0o32127, '', 'DNPTR', 'LMREND01', 'COLLECT SNAPSHOT', kind='data', line=210)
W('05,2233', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=211)
W('05,2234', 0o32276, '', 'DNPTR', 'LMREND07', 'COLLECT SNAPSHOT', kind='data', line=212)
W('05,2235', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=213)
W('05,2236', 0o03451, '', '1DNADR', 'DELLT4', 'DELLT4,+1', kind='data', line=214)
W('05,2237', 0o13443, '', '3DNADR', 'RTARG', 'RTARG +0...+5', kind='data', line=215)
W('05,2240', 0o13433, '', '3DNADR', 'DELVSLV', 'DELVSLV +0...+5', kind='data', line=216)
W('05,2241', 0o03633, '', '1DNADR', 'TCSI', 'TCSI,+1', kind='data', line=217)
W('05,2242', 0o12266, '', '3DNADR', 'DELVEET1', 'DELVEET +0...+5', kind='data', line=218)
W('05,2243', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=219)
W('05,2244', 0o03630, '', '1DNADR', 'TPASS4', 'TPASS4,+1', kind='data', line=220)
W('05,2245', 0o32224, '', 'DNPTR', 'LMREND06', 'COMMON DATA', kind='data', line=221)
W('05,2246', 0o32136, '', 'DNPTR', 'LMREND02', 'COMMON DATA', kind='data', line=222)
W('05,2247', 0o00024, '', '1DNADR', 'TIME2', 'TIME2/1', kind='data', line=223)
W('05,2250', 0o32145, '', 'DNPTR', 'LMREND03', 'COLLECT SNAPSHOT', kind='data', line=224)
W('05,2251', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=225)
W('05,2252', 0o32154, '', 'DNPTR', 'LMREND04', 'COMMON DATA', kind='data', line=226)
W('05,2253', 0o07115, '', '2DNADR', 'POSTORKU', 'POSTORKU,NEGTORKU,POSTORKV,NEGTORKV', kind='data', line=227)
W('05,2254', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=228)
W('05,2255', 0o01776, '', '1DNADR', 'TCDH', 'TCDH,+1', kind='data', line=229)
W('05,2256', 0o12274, '', '3DNADR', 'DELVEET2', 'DELVEET2 +0...+5', kind='data', line=230)
W('05,2257', 0o03635, '', '1DNADR', 'TTPI', 'TTPI,+1', kind='data', line=231)
W('05,2260', 0o12365, '', '3DNADR', 'DELVEET3', 'DELVEET3 +0...+5', kind='data', line=232)
W('05,2261', 0o02256, '', '1DNADR', 'ELEV', 'ELEV,+1', kind='data', line=233)
W('05,2262', 0o04036, '', '2DNADR', 'CDUS', 'CDUS,PIPAX,PIPAY,PIPAZ', kind='data', line=234)
W('05,2263', 0o00112, '', '1DNADR', 'LASTYCMD', 'LASTYCMD,LASTXCMD', kind='data', line=235)
W('05,2264', 0o01331, '', '1DNADR', 'LEMMASS', 'LEMMASS,CSMMASS', kind='data', line=236)
W('05,2265', 0o01302, '', '1DNADR', 'IMODES30', 'IMODES30,IMODES33', kind='data', line=237)
W('05,2266', 0o03441, '', '1DNADR', 'TIG', 'TIG,+1', kind='data', line=238)
W('05,2267', 0o32157, '', 'DNPTR', 'LMREND05', 'COMMON DATA', kind='data', line=239)
W('05,2270', 0o02302, '', '1DNADR', 'DELTAR', 'DELTAR,+1', kind='data', line=240)
W('05,2271', 0o03620, '', '1DNADR', 'CENTANG', 'CENTANG,+1', kind='data', line=241)
W('05,2272', 0o03466, '', '1DNADR', 'NN', 'NN,+1', kind='data', line=242)
W('05,2273', 0o03577, '', '1DNADR', 'DIFFALT', 'DIFFALT,+1', kind='data', line=243)
W('05,2274', 0o02347, '', '1DNADR', 'DELVTPF', 'DELVTPF,+1', kind='data', line=244)
W('05,2275', 0o77770, '', '-1DNADR', 'SPARE', kind='data', line=245)

# --------------------- SUB-LISTS --------------------------

S('LMREND01', 'equals', 0o22127, line=249)  # COMMON DOWNLIST DATA
S('LMREND02', 'equals', 0o22136, line=250)  # COMMON DOWNLIST DATA
S('LMREND03', 'equals', 0o22145, line=251)  # COMMON DOWNLIST DATA
# Page 199
S('LMREND04', 'equals', 0o22154, line=253)  # COMMON DOWNLIST DATA
S('LMREND05', 'equals', 0o22157, line=254)  # COMMON DOWNLIST DATA
S('LMREND06', 'equals', 0o22224, line=255)  # COMMON DOWNLIST DATA

W('05,2276', 0o74320, 'LMREND07', '-1DNADR', 'AIG', 'AIG,AMG               SNAPSHOT', kind='data', line=257)
W('05,2277', 0o03461, '', '1DNADR', 'AOG', 'AOG,TRKMKCNT', kind='data', line=258)
W('05,2300', 0o03752, '', '1DNADR', 'TANGNB', 'TANGNB,+1', kind='data', line=259)
W('05,2301', 0o03754, '', '1DNADR', 'MKTIME', 'MKTIME,+1', kind='data', line=260)
W('05,2302', 0o74017, '', '-1DNADR', 'RANGRDOT', 'DNRRANGE,DNRRDOT', kind='data', line=261)

# -----------------------------------------------------------

# Page 200
# LM DESCENT AND ASCENT DOWNLIST

# ---------------------- CONTROL LIST ------------------------

S('LMDSASDL', 'equals', 0o22303, line=270)  # SEND ID BY SPECIAL CODING
W('05,2303', 0o32341, '', 'DNPTR', 'LMDSAS07', 'COLLECT SNAPSHOT', kind='data', line=271)
W('05,2304', 0o32355, '', 'DNPTR', 'LMDSAS08', 'SEND SNAPSHOT', kind='data', line=272)
W('05,2305', 0o01344, '', '1DNADR', 'TEVENT', 'TEVENT,+1', kind='data', line=273)
W('05,2306', 0o13253, '', '3DNADR', 'UNFC/2', 'UNFC/2 +0...+5', kind='data', line=274)
W('05,2307', 0o13645, '', '3DNADR', 'VGVECT', 'VGVECT +0...+5', kind='data', line=275)
W('05,2310', 0o03642, '', '1DNADR', 'TTF/8', 'TTF/8,+1', kind='data', line=276)
W('05,2311', 0o03664, '', '1DNADR', 'DELTAH', 'DELTAH,+1', kind='data', line=277)
W('05,2312', 0o12022, '', '3DNADR', 'RLS', 'RLS +0...+5', kind='data', line=278)
W('05,2313', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=279)
W('05,2314', 0o32224, '', 'DNPTR', 'LMDSAS09', 'COMMON DATA', kind='data', line=280)
W('05,2315', 0o32136, '', 'DNPTR', 'LMDSAS02', 'COMMON DATA', kind='data', line=281)
W('05,2316', 0o00024, '', '1DNADR', 'TIME2', 'TIME2/1', kind='data', line=282)
W('05,2317', 0o32145, '', 'DNPTR', 'LMDSAS03', 'COLLECT SNAPSHOT', kind='data', line=283)
W('05,2320', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=284)
W('05,2321', 0o32154, '', 'DNPTR', 'LMDSAS04', 'COMMON DATA', kind='data', line=285)
W('05,2322', 0o07115, '', '2DNADR', 'POSTORKU', 'POSTORKU,NEGTORKU,POSTORKV,NEGTORKV', kind='data', line=286)
W('05,2323', 0o12636, '', '3DNADR', 'RGU', 'RGU +0...+5', kind='data', line=287)
W('05,2324', 0o13626, '', '3DNADR', 'VGU', 'VGU +0...+5', kind='data', line=288)
W('05,2325', 0o13634, '', '3DNADR', 'LAND', 'LAND +0...+5', kind='data', line=289)
W('05,2326', 0o02262, '', '1DNADR', 'AT', 'AT,+1', kind='data', line=290)
W('05,2327', 0o02400, '', '1DNADR', 'TLAND', 'TLAND,+1', kind='data', line=291)
W('05,2330', 0o03615, '', '1DNADR', 'FC', 'FC,GARBAGE', kind='data', line=292)
W('05,2331', 0o00112, '', '1DNADR', 'LASTYCMD', 'LASTYCMD,LASTXCMD', kind='data', line=293)
W('05,2332', 0o01331, '', '1DNADR', 'LEMMASS', 'LEMMASS,CSMMASS', kind='data', line=294)
W('05,2333', 0o01302, '', '1DNADR', 'IMODES30', 'IMODES30,IMODES33', kind='data', line=295)
W('05,2334', 0o03441, '', '1DNADR', 'TIG', 'TIG,+1', kind='data', line=296)
W('05,2335', 0o32157, '', 'DNPTR', 'LMDSAS05', 'COMMON DATA', kind='data', line=297)
W('05,2336', 0o32170, '', 'DNPTR', 'LMDSAS06', 'COMMON DATA', kind='data', line=298)
W('05,2337', 0o03614, '', '1DNADR', 'PSEUDO55', 'PSEUDO55,GARBAGE', kind='data', line=299)
W('05,2340', 0o74324, '', '-1DNADR', 'TTOGO', 'TTOGO,+1', kind='data', line=300)

# ---------------------- SUB-LISTS ------------------------

S('LMDSAS02', 'equals', 0o22136, line=304)  # COMMON DOWNLIST DATA
S('LMDSAS03', 'equals', 0o22145, line=305)  # COMMON DOWNLIST DATA
S('LMDSAS04', 'equals', 0o22154, line=306)  # COMMON DOWNLIST DATA
S('LMDSAS05', 'equals', 0o22157, line=307)  # COMMON DOWNLIST DATA
S('LMDSAS06', 'equals', 0o22170, line=308)  # COMMON DOWNLIST DATA

W('05,2341', 0o75441, 'LMDSAS07', '-1DNADR', 'LRZCDUDL', 'LRZCDUDL,GARBAGE              SNAPSHOT', kind='data', line=310)
W('05,2342', 0o03651, '', '1DNADR', 'VSELECT', 'VSELECT,GARBAGE', kind='data', line=311)
W('05,2343', 0o02337, '', '1DNADR', 'LRVTIMDL', 'LRVTIMDL,+1', kind='data', line=312)
# Page 201
W('05,2344', 0o03652, '', '1DNADR', 'VMEAS', 'VMEAS,+1', kind='data', line=314)
W('05,2345', 0o03754, '', '1DNADR', 'MKTIME', 'MKTIME,+1', kind='data', line=315)
W('05,2346', 0o03654, '', '1DNADR', 'HMEAS', 'HMEAS,+1', kind='data', line=316)
W('05,2347', 0o03756, '', '1DNADR', 'RM', 'RM,+1', kind='data', line=317)
W('05,2350', 0o03457, '', '1DNADR', 'AIG', 'AIG,AMG', kind='data', line=318)
W('05,2351', 0o03461, '', '1DNADR', 'AOG', 'AOG,TRKMKCNT', kind='data', line=319)
W('05,2352', 0o03752, '', '1DNADR', 'TANGNB', 'TANGNB,+1', kind='data', line=320)
W('05,2353', 0o03754, '', '1DNADR', 'MKTIME', 'MKTIME,+1', kind='data', line=321)
W('05,2354', 0o75443, '', '-1DNADR', 'LRXCDUDL', 'LRXCDUDL,LRYCDUDL', kind='data', line=322)

W('05,2355', 0o24340, 'LMDSAS08', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=324)
W('05,2356', 0o57423, '', '-5DNADR', 'DNTMBUFF +12D', kind='data', line=325)

S('LMDSAS09', 'equals', 0o22224, line=327)  # COMMON DOWNLIST DATA

# ---------------------------------------------------------

# Page 202
# LM LUNAR SURFACE ALIGN DOWNLIST

# ---------------------- CONTROL LIST ---------------------

S('LMLSALDL', 'equals', 0o22357, line=336)  # SEND ID BY SPECIAL CODING
W('05,2357', 0o32127, '', 'DNPTR', 'LMLSAL01', 'COLLECT SNAPSHOT', kind='data', line=337)
W('05,2360', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=338)
W('05,2361', 0o32276, '', 'DNPTR', 'LMLSAL07', 'COLLECT SNAPSHOT', kind='data', line=339)
W('05,2362', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SHAPSHOT', kind='data', line=340)
W('05,2363', 0o02774, '', '1DNADR', 'TALIGN', 'TALIGN,+1', kind='data', line=341)
W('05,2364', 0o25733, '', '6DNADR', 'REFSMMAT', 'REFSMMAT +0...+11D', kind='data', line=342)
W('05,2365', 0o26236, '', '6DNADR', 'YNBSAV', 'YNBSAV +0...+5,SNBSAV +0...+5', kind='data', line=343)
W('05,2366', 0o32224, '', 'DNPTR', 'LMLSAL08', 'COMMON DATA', kind='data', line=344)
W('05,2367', 0o32136, '', 'DNPTR', 'LMLSAL02', 'COMMON DATA', kind='data', line=345)
W('05,2370', 0o00024, '', '1DNADR', 'TIME2', 'TIME2/1', kind='data', line=346)
W('05,2371', 0o32145, '', 'DNPTR', 'LMLSAL03', 'COLLECT SNAPSHOT', kind='data', line=347)
W('05,2372', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SHAPSHOT', kind='data', line=348)
W('05,2373', 0o32154, '', 'DNPTR', 'LMLSAL04', 'COMMON DATA', kind='data', line=349)
W('05,2374', 0o32226, '', 'DNPTR', 'LMLSAL09', 'COMMON DATA', kind='data', line=350)
W('05,2375', 0o12230, '', '3DNADR', 'GSAV', 'GSAV +0...+5', kind='data', line=351)
W('05,2376', 0o02020, '', '1DNADR', 'AGSK', 'AGSK,+1', kind='data', line=352)
W('05,2377', 0o00112, '', '1DNADR', 'LASTYCMD', 'LASTYCMD,LASTXCMD', kind='data', line=353)
W('05,2400', 0o01331, '', '1DNADR', 'LEMMASS', 'LEMMASS,CSMMASS', kind='data', line=354)
W('05,2401', 0o01302, '', '1DNADR', 'IMODES30', 'IMODES30,IMODES33', kind='data', line=355)
W('05,2402', 0o03441, '', '1DNADR', 'TIG', 'TIG,+1', kind='data', line=356)
W('05,2403', 0o32157, '', 'DNPTR', 'LMLSAL05', 'COMMON DATA', kind='data', line=357)
W('05,2404', 0o32170, '', 'DNPTR', 'LMLSAL06', 'COMMON DATA', kind='data', line=358)
W('05,2405', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=359)
W('05,2406', 0o77770, '', '-1DNADR', 'SPARE', kind='data', line=360)

# ---------------------- SUB-LISTS ----------------------

S('LMLSAL01', 'equals', 0o22127, line=364)  # COMMON DOWNLIST DATA
S('LMLSAL02', 'equals', 0o22136, line=365)  # COMMON DOWNLIST DATA
S('LMLSAL03', 'equals', 0o22145, line=366)  # COMMON DOWNLIST DATA
S('LMLSAL04', 'equals', 0o22154, line=367)  # COMMON DOWNLIST DATA
S('LMLSAL05', 'equals', 0o22157, line=368)  # COMMON DOWNLIST DATA
S('LMLSAL06', 'equals', 0o22170, line=369)  # COMMON DOWNLIST DATA
S('LMLSAL07', 'equals', 0o22276, line=370)  # COMMON DOWNLIST DATA
S('LMLSAL08', 'equals', 0o22224, line=371)  # COMMON DOWNLIST DATA
S('LMLSAL09', 'equals', 0o22226, line=372)  # COMMON DOWNLIST DATA

# Page 203
# --------------------------------------------------------

# Page 204
# LM AGS INITIALIZATION AND UPDATE DOWNLIST

# ---------------------- CONTROL LIST --------------------

S('LMAGSIDL', 'equals', 0o22407, line=382)  # SEND IO BY SPECIAL CODING
W('05,2407', 0o12200, '', '3DNADR', 'AGSBUFF +0', 'AGSBUFF +0...+5', kind='data', line=383)
W('05,2410', 0o02214, '', '1DNADR', 'AGSBUFF +12D', 'AGSBUFF +12D,GARBAGE', kind='data', line=384)
W('05,2411', 0o12201, '', '3DNADR', 'AGSBUFF +1', 'AGSBUFF +1...+6', kind='data', line=385)
W('05,2412', 0o02215, '', '1DNADR', 'AGSBUFF +13D', 'AGSBUFF +13D, GARBAGE', kind='data', line=386)
W('05,2413', 0o12206, '', '3DNADR', 'AGSBUFF +6', 'AGSBUFF +6...+11', kind='data', line=387)
W('05,2414', 0o02214, '', '1DNADR', 'AGSBUFF +12D', 'AGSBUFF +12D,GARBAGE', kind='data', line=388)
W('05,2415', 0o12207, '', '3DNADR', 'AGSBUFF +7', 'AGSBUFF +7...+12D', kind='data', line=389)
W('05,2416', 0o02215, '', '1DNADR', 'AGSBUFF +13D', 'AGSBUFF +13D,GARBAGE', kind='data', line=390)
W('05,2417', 0o25170, '', '6DNADR', 'COMPNUMB', 'COMPNUMB,UPOLDMOD,UPVERB,UPCOUNT,', kind='data', line=391)
# UPBUFF +0...+7
W('05,2420', 0o25204, '', '6DNADR', 'UPBUFF +8D', 'UPBUFF +8D...+19D', kind='data', line=393)
W('05,2421', 0o32136, '', 'DNPTR', 'LMAGSI02', 'COMMON DATA', kind='data', line=394)
W('05,2422', 0o00024, '', '1DNADR', 'TIME2', 'TIME2/1', kind='data', line=395)
W('05,2423', 0o32145, '', 'DNPTR', 'LMAGSI03', 'COLLECT SNAPSHOT', kind='data', line=396)
W('05,2424', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=397)
W('05,2425', 0o32154, '', 'DNPTR', 'LMAGSI04', 'COMMON DATA', kind='data', line=398)
W('05,2426', 0o07115, '', '2DNADR', 'POSTORKU', 'POSTORKU,NEGTORKU,POSTORKV,NEGTORKV', kind='data', line=399)
W('05,2427', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=400)
W('05,2430', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=401)
W('05,2431', 0o02020, '', '1DNADR', 'AGSK', 'AGSK,+1', kind='data', line=402)
W('05,2432', 0o25174, '', '6DNADR', 'UPBUFF', 'UPBUFF +0...+11D', kind='data', line=403)
W('05,2433', 0o15210, '', '4DNADR', 'UPBUFF +12D', 'UPBUFF +12D...+19D', kind='data', line=404)
W('05,2434', 0o01331, '', '1DNADR', 'LEMMASS', 'LEMMASS,CSMMASS', kind='data', line=405)
W('05,2435', 0o01302, '', '1DNADR', 'IMODES30', 'IMODES30,IMODES33', kind='data', line=406)
W('05,2436', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=407)
W('05,2437', 0o32157, '', 'DNPTR', 'LMAGSI05', 'COMMON DATA', kind='data', line=408)
W('05,2440', 0o52754, '', '-6DNADR', 'DSPTAB', 'DSPTAB +0...+11D', kind='data', line=409)

# ---------------------- SUB-LISTS ---------------------

S('LMAGSI02', 'equals', 0o22136, line=413)  # COMMON DOWNLIST DATA
S('LMAGSI03', 'equals', 0o22145, line=414)  # COMMON DOWNLIST DATA
S('LMAGSI04', 'equals', 0o22154, line=415)  # COMMON DOWNLIST DATA
S('LMAGSI05', 'equals', 0o22157, line=416)  # COMMON DOWNLIST DATA

# ------------------------------------------------------

W('05,2441', 0o02172, 'DNTABLE', 'GENADR', 'LMCSTADL', 'LM COAST AND ALIGN DOWNLIST', kind='data', line=420)
W('05,2442', 0o02407, '', 'GENADR', 'LMAGSIDL', 'LM AGS INITIALIZATION/UPDATE DOWNLIST', kind='data', line=421)
W('05,2443', 0o02232, '', 'GENADR', 'LMRENDDL', 'LM RENDEZVOUS AND PRE-THRUST DOWNLIST', kind='data', line=422)
W('05,2444', 0o02066, '', 'GENADR', 'LMORBMDL', 'LM ORBITAL MANEUVERS DOWNLIST', kind='data', line=423)
W('05,2445', 0o02303, '', 'GENADR', 'LMDSASDL', 'LM DESCENT AND ASCENT DOWNLIST', kind='data', line=424)
# Page 205
W('05,2446', 0o02357, '', 'GENADR', 'LMLSALDL', 'LM LUNAR SURFACE ALIGN DOWNLIST', kind='data', line=426)

# ------------------------------------------------------
