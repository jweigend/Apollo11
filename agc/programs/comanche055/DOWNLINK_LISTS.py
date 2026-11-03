"""DOWNLINK_LISTS.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/DOWNLINK_LISTS.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 170-180 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('DOWNLINK_LISTS', 'DOWNLINK_LISTS.agc', 'Comanche055', pages='170-180')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     DOWNLINK_LISTS.agc
# Purpose:      Part of the source code for Comanche, build 055. It
# is part of the source code for the Command Module's
# (CM) Apollo Guidance Computer (AGC), Apollo 11.
# Assembler:    yaYUL
# Reference:    pp. 170-180
# Contact:      Ron Burkey <info@sandroid.org>,
# Fabrizio Bernardini <fabrizio@spacecraft.it>
# Website:      http://www.ibiblio.org/apollo.
# Mod history:  10/05/09 FB     Transcription of Batch FB-1 Assignment.
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

# Page 170
#   BANK 22
#   SETLOC DOWNTELM
#   BANK

#   EBANK= DNTMBUFF

# SPECIAL DOWNLINK OP CODES
# OP CODE         ADDRESS(EXAMPLE)        SENDS...                BIT 15          BITS 14-12      BITS 11-0
# -------         ----------------        ----------              ------          ----------      ---------
# 1DNADR          TIME2                   (2 AGC WDS)             0               0               ECADR
# 2DNADR          TEPHEM                  (4 AGC WDS)             0               1               ECADR
# 3DNADR          VGBODY                  (6 AGC WDS)             0               2               ECADR
# 4DNADR          STATE                   (8 AGC WDS)             0               3               ECADR
# 5DNADR          UPBUFF                  (10AGC WDS)             0               4               ECADR
# 6DNADR          DSPTAB                  (12AGC WDS)             0               5               ECADR
# DNCHAN          30                      CHANNELS                0               7               CHANNEL ADDRESS
# DNPTR           NEXTLIST                POINTS TO NEXT LIST.    0               6               ADRES
#
# DOWNLIST FORMAT DEFINITIONS AND RULES -
# 1. END OF A LIST = -XDNADR (X = 1 TO 6), -DNPTR, OR -DNCHAN.
# 2. SNAPSHOT SUBLIST = LIST WHICH STARTS WITH A -1DNADR.
# 3. SNAPSHOT SUBLIST CAN ONLY CONTAIN 1DNADRS.
# 4. TIME2 1DNADR MUST BE LOCATED IN THE CONTROL LIST OF A DOWNLIST.
# 5. ERASABLE DOWN TELEMETRY WORDS SHOULD BE GROUPED IN SEQUENTIAL
# LOCATIONS AS MUCH AS POSSIBLE TO SAVE STORAGE USED BY DOWNLINK LISTS.
# 6. THE DOWNLINK LISTS (INCLUDING SUBLISTS) ARE ORGANIZED SUCH THAT THE ITEMS LISTED FIRST (IN FRONT OF FBANK) ARE
# SENT FIRST.  EXCEPTION--- SNAPSHOT SUBLISTS.  IN THE SNAPSHOT SUBLISTS THE DATA REPRESENTED BY THE FIRST
# 11 1DNADRS IS PRESERVED (IN ORDER) IN DNTMBUFF AND SENT BY THE NEXT 11 DOWNRUPTS. THE DATA REPRESENTED BY THE
# LIST IS SENT IMMEDIATELY.

#   COUNT 05/DLIST
S('ERASZERO', 'equals', 0o7, line=63)
S('SPARE', 'equals', 0o7, line=64)  # USE SPARE TO INDICATE AVAILABLE SPACE
W('05,2000', 0o77340, 'LOWIDCOD', 'OCT', '77340', 'LOW ID CODE', kind='data', line=65)

S('NOMDNLST', 'equals', 0o22107, line=67)  # FRESH START AND POST P27 DOWNLIST
S('UPDNLIST', 'equals', 0o22207, line=68)  # UPDATE PROGRAM (P27) DOWNLIST

# Page 171
# CSM POWERED FLIGHT DOWNLIST
#
# --------------------- CONTROL LIST -------------------------

S('CMPOWEDL', 'equals', 0o22001, line=75)
W('05,2001', 0o32043, '', 'DNPTR', 'CMPOWE01', 'COLLECT SNAPSHOT', kind='data', line=76)
W('05,2002', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=77)
W('05,2003', 0o32052, '', 'DNPTR', 'CMPOWE02', 'COLLECT SECOND SNAPSHOT', kind='data', line=78)
W('05,2004', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=79)
W('05,2005', 0o32057, '', 'DNPTR', 'CMPOWE03', 'COMMON DATA', kind='data', line=80)
W('05,2006', 0o03412, '', '1DNADR', 'TIG', 'TIG,+1', kind='data', line=81)
W('05,2007', 0o03422, '', '1DNADR', 'DELLT4', 'DELLT4,+1', kind='data', line=82)
W('05,2010', 0o13414, '', '3DNADR', 'RTARG', 'RTARG,+1,+2,...+5', kind='data', line=83)
W('05,2011', 0o03427, '', '1DNADR', 'TGO', 'TGO,+1', kind='data', line=84)
W('05,2012', 0o01245, '', '1DNADR', 'PIPTIME1', 'PIPTIME1,+1', kind='data', line=85)
W('05,2013', 0o11162, '', '3DNADR', 'DELV', 'DELV,+1,...+4,+5', kind='data', line=86)
W('05,2014', 0o03023, '', '1DNADR', 'PACTOFF', 'PACTOFF,YACTOFF', kind='data', line=87)
W('05,2015', 0o03223, '', '1DNADR', 'PCMD', 'PCMD,YCMD', kind='data', line=88)
W('05,2016', 0o03702, '', '1DNADR', 'CSTEER', 'CSTEER,+1', kind='data', line=89)
W('05,2017', 0o12444, '', '3DNADR', 'DELVEET1', 'CSI DELTA VELOCITY COMPONENTS   (31-33)', kind='data', line=90)
W('05,2020', 0o25735, '', '6DNADR', 'REFSMMAT', 'REFSMMAT,+1,...+10,+11', kind='data', line=91)
W('05,2021', 0o32061, '', 'DNPTR', 'CMPOWE04', 'COMMON DATA', kind='data', line=92)
W('05,2022', 0o00024, '', '1DNADR', 'TIME2', 'TIME2,TIME1', kind='data', line=93)
W('05,2023', 0o32063, '', 'DNPTR', 'CMPOWE05', 'COLLECT SNAPSHOT', kind='data', line=94)
W('05,2024', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=95)
W('05,2025', 0o32052, '', 'DNPTR', 'CMPOWE02', 'COLLECT SNAPSHOT', kind='data', line=96)
W('05,2026', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=97)
W('05,2027', 0o32057, '', 'DNPTR', 'CMPOWE03', kind='data', line=98)
W('05,2030', 0o32072, '', 'DNPTR', 'CMPOWE06', 'COMMON DATA', kind='data', line=99)
W('05,2031', 0o03743, '', '1DNADR', 'ELEV', 'ELEV,+1', kind='data', line=100)
W('05,2032', 0o03753, '', '1DNADR', 'CENTANG', 'CENTANG,+1', kind='data', line=101)
W('05,2033', 0o02610, '', '1DNADR', 'DELTAR', 'DELTAR,+1', kind='data', line=102)
W('05,2034', 0o00106, '', '1DNADR', 'STATE +10D', 'FLAGWRDS 10 AND 11', kind='data', line=103)
W('05,2035', 0o01336, '', '1DNADR', 'TEVENT', 'TEVENT,+1', kind='data', line=104)
W('05,2036', 0o03223, '', '1DNADR', 'PCMD', 'PCMD,YCMD', kind='data', line=105)
W('05,2037', 0o01331, '', '1DNADR', 'OPTMODES', 'OPTMODES,HOLDFLAG', kind='data', line=106)
W('05,2040', 0o32075, '', 'DNPTR', 'CMPOWE07', 'COMMON DATA', kind='data', line=107)
W('05,2041', 0o13720, '', '3DNADR', 'VGTIG', 'VGTIG,+1,...+4,+5', kind='data', line=108)
W('05,2042', 0o64111, '', '-3DNADR', 'DELVEET2', 'CDH DELTA VELOCITY COMPONENTS   (98-100)', kind='data', line=109)
# --------------------- SUB LISTS ---------------------------

W('05,2043', 0o76605, 'CMPOWE01', '-1DNADR', 'RN +2', 'RN+2,+3                       SNAPSHOT DATA', kind='data', line=112)
W('05,2044', 0o01174, '', '1DNADR', 'RN +4', 'RN+4,+5', kind='data', line=113)
W('05,2045', 0o01176, '', '1DNADR', 'VN', 'VN,+1', kind='data', line=114)
W('05,2046', 0o01200, '', '1DNADR', 'VN +2', 'VN+2,+3', kind='data', line=115)
W('05,2047', 0o01202, '', '1DNADR', 'VN +4', 'VN+4,+5', kind='data', line=116)
W('05,2050', 0o01204, '', '1DNADR', 'PIPTIME', 'PIPTIME,+1', kind='data', line=117)
W('05,2051', 0o76607, '', '-1DNADR', 'RN', 'RN,+1', kind='data', line=118)

W('05,2052', 0o77743, 'CMPOWE02', '-1DNADR', 'CDUZ', 'CDUZ,CDUT                     SNAPSHOT DATA', kind='data', line=120)
# Page 172
W('05,2053', 0o03133, '', '1DNADR', 'ADOT', 'ADOT,+1/OGARATE,+1', kind='data', line=122)
W('05,2054', 0o03135, '', '1DNADR', 'ADOT +2', 'ADOT+2,+3/OMEGAB+2,+3', kind='data', line=123)
W('05,2055', 0o03137, '', '1DNADR', 'ADOT +4', 'ADOT+4,+5/OMEGAB+4,+5', kind='data', line=124)
W('05,2056', 0o77745, '', '-1DNADR', 'CDUX', 'CDUX,CDUY', kind='data', line=125)

W('05,2057', 0o07076, 'CMPOWE03', '2DNADR', 'AK', 'AK,AK1,AK2,RCSFLAGS           COMMON DATA', kind='data', line=127)
W('05,2060', 0o70605, '', '-2DNADR', 'THETADX', 'THETADX,THETADY,THETADZ,GARBAGE', kind='data', line=128)

W('05,2061', 0o20074, 'CMPOWE04', '5DNADR', 'STATE', 'FLAGWRD0 THRU FLAGWRD9        COMMON DATA', kind='data', line=130)
W('05,2062', 0o52754, '', '-6DNADR', 'DSPTAB', 'DISPLAY TABLES', kind='data', line=131)

W('05,2063', 0o76054, 'CMPOWE05', '-1DNADR', 'R-OTHER +2', 'R-OTHER+2,+3                  SNAPSHOT DATA', kind='data', line=133)
W('05,2064', 0o01725, '', '1DNADR', 'R-OTHER +4', 'R-OTHER+4,+5', kind='data', line=134)
W('05,2065', 0o01727, '', '1DNADR', 'V-OTHER', 'V-OTHER,+1', kind='data', line=135)
W('05,2066', 0o01731, '', '1DNADR', 'V-OTHER +2', 'V-OTHER+2,+3', kind='data', line=136)
W('05,2067', 0o01733, '', '1DNADR', 'V-OTHER +4', 'V-OTHER+4,+5', kind='data', line=137)
W('05,2070', 0o01642, '', '1DNADR', 'T-OTHER', 'T-OTHER,+1', kind='data', line=138)
W('05,2071', 0o76056, '', '-1DNADR', 'R-OTHER', 'R-OTHER,+1', kind='data', line=139)

W('05,2072', 0o01432, 'CMPOWE06', '1DNADR', 'RSBBQ', 'RSBBQ,+1                      COMMON DATA', kind='data', line=141)
W('05,2073', 0o10372, '', '3DNADR', 'CADRFLSH', 'CADRFLSH,+1,+2,FAILREG,+1,+2', kind='data', line=142)
W('05,2074', 0o73741, '', '-2DNADR', 'CDUS', 'CDUS,PIPAX,PIPAY,PIPAZ', kind='data', line=143)

W('05,2075', 0o03073, 'CMPOWE07', '1DNADR', 'LEMMASS', 'LEMMASS,CSMMASS               COMMON DATA', kind='data', line=145)
W('05,2076', 0o03066, '', '1DNADR', 'DAPDATR1', 'DAPDATR1,DAPDATR2', kind='data', line=146)
W('05,2077', 0o07167, '', '2DNADR', 'ERRORX', 'ERRORX,ERRORY,ERRORZ,GARBAGE', kind='data', line=147)
W('05,2100', 0o13125, '', '3DNADR', 'WBODY', 'WBODY,...+5/OMEGAC,...+5', kind='data', line=148)
W('05,2101', 0o05154, '', '2DNADR', 'REDOCTR', 'REDOCTR,THETAD,+1,+2', kind='data', line=149)
W('05,2102', 0o01320, '', '1DNADR', 'IMODES30', 'IMODES30,IMODES33', kind='data', line=150)
W('05,2103', 0o34011, '', 'DNCHAN', '11', 'CHANNELS 11,12', kind='data', line=151)
W('05,2104', 0o34013, '', 'DNCHAN', '13', 'CHANNELS 13,14', kind='data', line=152)
W('05,2105', 0o34030, '', 'DNCHAN', '30', 'CHANNELS 30,31', kind='data', line=153)
W('05,2106', 0o43745, '', '-DNCHAN', '32', 'CHANNELS 32,33', kind='data', line=154)

# -----------------------------------------------------------

# Page 173
# CSM COAST AND ALIGNMENT DOWNLIST

# --------------------- CONTROL LIST ------------------------

S('CMCSTADL', 'equals', 0o22107, line=163)  # SEND ID BY SPECIAL CODING
W('05,2107', 0o32043, '', 'DNPTR', 'CMCSTA01', 'COLLECT SNAPSHOT', kind='data', line=164)
W('05,2110', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=165)
W('05,2111', 0o32052, '', 'DNPTR', 'CMCSTA02', 'COLLECT SECOND SNAPSHOT', kind='data', line=166)
W('05,2112', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=167)
W('05,2113', 0o32057, '', 'DNPTR', 'CMCSTA03', 'COMMON DATA', kind='data', line=168)
W('05,2114', 0o03412, '', '1DNADR', 'TIG', 'TIG,+1', kind='data', line=169)
W('05,2115', 0o00302, '', '1DNADR', 'BESTI', 'BESTI,BESTJ', kind='data', line=170)
W('05,2116', 0o17674, '', '4DNADR', 'MARKDOWN', 'MARKDOWN,+1,...+5,+6,GARBAGE', kind='data', line=171)
W('05,2117', 0o17502, '', '4DNADR', 'MARK2DWN', 'MARK2DWN,+1,...+5,+6', kind='data', line=172)
W('05,2120', 0o06351, '', '2DNADR', 'HAPOX', 'APOGEE AND PERIGEE FROM R30   (28-29)', kind='data', line=173)
W('05,2121', 0o03023, '', '1DNADR', 'PACTOFF', 'PACTOFF, YACTOFF                 (30)', kind='data', line=174)
W('05,2122', 0o13720, '', '3DNADR', 'VGTIG', 'VGTIG,...+5', kind='data', line=175)
W('05,2123', 0o25735, '', '6DNADR', 'REFSMMAT', 'REFSMMAT,+1,...+10,+11', kind='data', line=176)
W('05,2124', 0o32061, '', 'DNPTR', 'CMCSTA04', 'COMMON DATA', kind='data', line=177)
W('05,2125', 0o00024, '', '1DNADR', 'TIME2', 'TIME2,TIME1', kind='data', line=178)
W('05,2126', 0o32063, '', 'DNPTR', 'CMCSTA05', 'COLLECT SNAPSHOT', kind='data', line=179)
W('05,2127', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=180)
W('05,2130', 0o32052, '', 'DNPTR', 'CMCSTA02', 'COLLECT SNAPSHOT', kind='data', line=181)
W('05,2131', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=182)
W('05,2132', 0o32057, '', 'DNPTR', 'CMCSTA03', 'COMMON DATA', kind='data', line=183)
W('05,2133', 0o32072, '', 'DNPTR', 'CMCSTA06', 'COMMON DATA', kind='data', line=184)
W('05,2134', 0o12757, '', '3DNADR', 'OGC', 'OGC,+1,IGC,+1,MGC,+1', kind='data', line=185)
W('05,2135', 0o00106, '', '1DNADR', 'STATE +10D', 'FLAGWRDS 10 AND 11', kind='data', line=186)
W('05,2136', 0o01336, '', '1DNADR', 'TEVENT', 'TEVENT,+1', kind='data', line=187)
W('05,2137', 0o02633, '', '1DNADR', 'LAUNCHAZ', 'LAUNCHAZ,+1', kind='data', line=188)
W('05,2140', 0o01331, '', '1DNADR', 'OPTMODES', 'OPTMODES,HOLDFLAG', kind='data', line=189)
W('05,2141', 0o32075, '', 'DNPTR', 'CMCSTA07', 'COMMON DATA', kind='data', line=190)
W('05,2142', 0o52754, '', '-6DNADR', 'DSPTAB', 'DISPLAY TABLES', kind='data', line=191)

# --------------------- SUB LISTS ---------------------------

S('CMCSTA01', 'equals', 0o22043, line=195)  # COMMON DOWNLIST DATA

S('CMCSTA02', 'equals', 0o22052, line=197)  # COMMON DOWNLIST DATA

S('CMCSTA03', 'equals', 0o22057, line=199)  # COMMON DOWNLIST DATA

S('CMCSTA04', 'equals', 0o22061, line=201)  # COMMON DOWNLIST DATA

S('CMCSTA05', 'equals', 0o22063, line=203)  # COMMON DOWNLIST DATA

S('CMCSTA06', 'equals', 0o22072, line=205)  # COMMON DOWNLIST DATA

S('CMCSTA07', 'equals', 0o22075, line=207)  # COMMON DOWNLIST DATA
# Page 174
# -----------------------------------------------------------

# Page 175
# CSM RENDEZVOUS AND PRETHRUST LIST

# --------------------- CONTROL LIST ------------------------

S('CMRENDDL', 'equals', 0o22143, line=216)  # SEND ID BY SPECIAL CODING
W('05,2143', 0o32043, '', 'DNPTR', 'CMREND01', 'COLLECT SNAPSHOT', kind='data', line=217)
W('05,2144', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=218)
W('05,2145', 0o32052, '', 'DNPTR', 'CMREND02', 'COLLECT SECOND SNAPSHOT', kind='data', line=219)
W('05,2146', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=220)
W('05,2147', 0o32057, '', 'DNPTR', 'CMREND03', 'COMMON DATA', kind='data', line=221)
W('05,2150', 0o03412, '', '1DNADR', 'TIG', 'TIG,+1', kind='data', line=222)
W('05,2151', 0o03422, '', '1DNADR', 'DELLT4', 'DELLT4,+1', kind='data', line=223)
W('05,2152', 0o13414, '', '3DNADR', 'RTARG', 'RTARG,+1,...+4,+5', kind='data', line=224)
W('05,2153', 0o01151, '', '1DNADR', 'VHFTIME', 'VHFTIME,+1', kind='data', line=225)
W('05,2154', 0o17674, '', '4DNADR', 'MARKDOWN', 'MARKTIME(DP),YCDU,SCDU,ZCDU,TCDU,XCDU,RM', kind='data', line=226)
W('05,2155', 0o01125, '', '1DNADR', 'VHFCNT', 'VHFCNT,+1', kind='data', line=227)
W('05,2156', 0o03662, '', '1DNADR', 'TTPI', 'TTPI,+1', kind='data', line=228)
W('05,2157', 0o03424, '', '1DNADR', 'ECSTEER', 'ECSTEER,+1', kind='data', line=229)
W('05,2160', 0o02636, '', '1DNADR', 'DELVTPF', 'DELVTPF,+1', kind='data', line=230)
W('05,2161', 0o06634, '', '2DNADR', 'TCDH', 'CDH AND CSI TIME                      (32-33)', kind='data', line=231)
W('05,2162', 0o03655, '', '1DNADR', 'TPASS4', 'TPASS4,+1', kind='data', line=232)
W('05,2163', 0o13404, '', '3DNADR', 'DELVSLV', 'DELVSLV,+1...+4,+5', kind='data', line=233)
W('05,2164', 0o06320, '', '2DNADR', 'RANGE', 'RANGE,+1,RRATE,+1', kind='data', line=234)
W('05,2165', 0o32061, '', 'DNPTR', 'CMREND04', 'COMMON DATA', kind='data', line=235)
W('05,2166', 0o00024, '', '1DNADR', 'TIME2', 'TIME2,TIME1', kind='data', line=236)
W('05,2167', 0o32063, '', 'DNPTR', 'CMREND05', 'COLLECT SNAPSHOT', kind='data', line=237)
W('05,2170', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=238)
W('05,2171', 0o32052, '', 'DNPTR', 'CMREND02', 'COLLECT SNAPSHOT', kind='data', line=239)
W('05,2172', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=240)
W('05,2173', 0o32057, '', 'DNPTR', 'CMREND03', 'COMMON DATA', kind='data', line=241)
W('05,2174', 0o32072, '', 'DNPTR', 'CMREND06', 'COMMON DATA', kind='data', line=242)
W('05,2175', 0o02632, '', '1DNADR', 'DIFFALT', 'CDH DELTA ALTITUDE', kind='data', line=243)
W('05,2176', 0o03753, '', '1DNADR', 'CENTANG', 'CENTANG,+1', kind='data', line=244)
W('05,2177', 0o02610, '', '1DNADR', 'DELTAR', 'DELTAR,+1', kind='data', line=245)
W('05,2200', 0o13645, '', '3DNADR', 'DELVEET3', 'DELVEET3,+1,...+4,+5', kind='data', line=246)
W('05,2201', 0o01331, '', '1DNADR', 'OPTMODES', 'OPTMODES,HOLDFLAG', kind='data', line=247)
W('05,2202', 0o32075, '', 'DNPTR', 'CMREND07', 'COMMON DATA', kind='data', line=248)
W('05,2203', 0o02324, '', '1DNADR', 'RTHETA', 'RTHETA,+1', kind='data', line=249)
W('05,2204', 0o07400, '', '2DNADR', 'LAT(SPL)', 'LAT(SPL),LNG(SPL),+1', kind='data', line=250)
W('05,2205', 0o07766, '', '2DNADR', 'VPRED', 'VPRED,+1,GAMMAEI,+1', kind='data', line=251)
W('05,2206', 0o77671, '', '-1DNADR', 'STATE +10D', 'FLAGWRDS 10 AND 11', kind='data', line=252)

# --------------------- SUB LISTS ----------------------------

S('CMREND01', 'equals', 0o22043, line=256)  # COMMON DOWNLIST DATA

S('CMREND02', 'equals', 0o22052, line=258)  # COMMON DOWNLIST DATA

S('CMREND03', 'equals', 0o22057, line=260)  # COMMON DOWNLIST DATA

S('CMREND04', 'equals', 0o22061, line=262)  # COMMON DOWNLIST DATA
# Page 176
S('CMREND05', 'equals', 0o22063, line=264)  # COMMON DOWNLIST DATA

S('CMREND06', 'equals', 0o22072, line=266)  # COMMON DOWNLIST DATA

S('CMREND07', 'equals', 0o22075, line=268)  # COMMON DOWNLIST DATA

# ------------------------------------------------------------

# Page 177
# CSM ENTRY AND UPDATE DOWNLIST
#
# --------------------- CONTROL LIST -------------------------

S('CMENTRDL', 'equals', 0o22207, line=277)  # SEND ID BY SPECIAL CODING
W('05,2207', 0o32043, '', 'DNPTR', 'CMENTR01', 'COLLECT SNAPSHOT', kind='data', line=278)
W('05,2210', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=279)
W('05,2211', 0o32052, '', 'DNPTR', 'CMENTR02', 'COLLECT SECOND SNAPSHOT', kind='data', line=280)
W('05,2212', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=281)
W('05,2213', 0o32057, '', 'DNPTR', 'CMENTR03', 'COMMON DATA', kind='data', line=282)
W('05,2214', 0o07300, '', '2DNADR', 'CMDAPMOD', 'CMDAPMOD,PREL,QREL,RREL', kind='data', line=283)
W('05,2215', 0o03635, '', '1DNADR', 'L/D1', 'L/D1,+1', kind='data', line=284)
W('05,2216', 0o24304, '', '6DNADR', 'UPBUFF', 'UPBUFF,+1,...+10,+11', kind='data', line=285)
W('05,2217', 0o14320, '', '4DNADR', 'UPBUFF +12D', 'UPBUFF+12,13,...+18,+19D', kind='data', line=286)
W('05,2220', 0o04300, '', '2DNADR', 'COMPNUMB', 'COMPNUMB,UPOLDMOD,UPVERB,UPCOUNT', kind='data', line=287)
W('05,2221', 0o03313, '', '1DNADR', 'PAXERR1', 'PAXERR1,ROLLTM', kind='data', line=288)
W('05,2222', 0o13675, '', '3DNADR', 'LATANG', 'LATANG,+1,RDOT,+1,THETAH,+1', kind='data', line=289)
W('05,2223', 0o07400, '', '2DNADR', 'LAT(SPL)', 'LAT(SPL),+1,LNG(SPL),+1', kind='data', line=290)
W('05,2224', 0o03265, '', '1DNADR', 'ALFA/180', 'ALFA/180,BETA/180', kind='data', line=291)
W('05,2225', 0o32061, '', 'DNPTR', 'CMENTR04', 'COMMON DATA', kind='data', line=292)
W('05,2226', 0o00024, '', '1DNADR', 'TIME2', 'TIME2,TIME1', kind='data', line=293)
W('05,2227', 0o32257, '', 'DNPTR', 'CMENTR05', 'COLLECT SNAPSHOT', kind='data', line=294)
W('05,2230', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=295)
W('05,2231', 0o32052, '', 'DNPTR', 'CMENTR02', 'COLLECT SNAPSHOT', kind='data', line=296)
W('05,2232', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=297)
W('05,2233', 0o07076, '', '2DNADR', 'AK', 'AK,AK1,AK2,RCSFLAGS', kind='data', line=298)
W('05,2234', 0o13167, '', '3DNADR', 'ERRORX', 'ERRORX/Y/Z,THETADX/Y/Z', kind='data', line=299)
W('05,2235', 0o07300, '', '2DNADR', 'CMDAPMOD', 'CMDAPMOD,PREL,QREL,RREL', kind='data', line=300)
W('05,2236', 0o24304, '', '6DNADR', 'UPBUFF', 'UPBUFF+0,+1,...+10,+11D', kind='data', line=301)
W('05,2237', 0o14320, '', '4DNADR', 'UPBUFF +12D', 'UPBUFF+12,+13,...+18,+19D', kind='data', line=302)
W('05,2240', 0o03073, '', '1DNADR', 'LEMMASS', 'LEMMASS,CSMMASS', kind='data', line=303)
W('05,2241', 0o03066, '', '1DNADR', 'DAPDATR1', 'DAPDATR1,DAPDATR2', kind='data', line=304)
W('05,2242', 0o03314, '', '1DNADR', 'ROLLTM', 'ROLLTM,ROLLC', kind='data', line=305)
W('05,2243', 0o01331, '', '1DNADR', 'OPTMODES', 'OPTMODES,HOLDFLAG', kind='data', line=306)
W('05,2244', 0o13125, '', '3DNADR', 'WBODY', 'WBODY,...+5/OMEGAC,...+5', kind='data', line=307)
W('05,2245', 0o05154, '', '2DNADR', 'REDOCTR', 'REDOCTR,THETAD+0,+1,+2', kind='data', line=308)
W('05,2246', 0o01320, '', '1DNADR', 'IMODES30', 'IMODES30,IMODES33', kind='data', line=309)
W('05,2247', 0o34011, '', 'DNCHAN', '11', 'CHANNELS 11,12', kind='data', line=310)
W('05,2250', 0o34013, '', 'DNCHAN', '13', 'CHANNELS 13,14', kind='data', line=311)
W('05,2251', 0o34030, '', 'DNCHAN', '30', 'CHANNELS 30,31', kind='data', line=312)
W('05,2252', 0o34032, '', 'DNCHAN', '32', 'CHANNELS 32,33', kind='data', line=313)
W('05,2253', 0o01432, '', '1DNADR', 'RSBBQ', 'RSBBQ,+1', kind='data', line=314)
W('05,2254', 0o10372, '', '3DNADR', 'CADRFLSH', 'CADRFLSH,+1,+2,FAILREG,+1,+2', kind='data', line=315)
W('05,2255', 0o00106, '', '1DNADR', 'STATE +10D', 'FLAGWRDS 10 AND 11', kind='data', line=316)
W('05,2256', 0o74007, '', '-1DNADR', 'GAMMAEI', 'GAMMAEI,+1', kind='data', line=317)

# --------------------- SUB LISTS ----------------------------

S('CMENTR01', 'equals', 0o22043, line=321)  # COMMON DOWNLIST DATA
# Page 178
S('CMENTR02', 'equals', 0o22052, line=323)  # COMMON DOWNLIST DATA

S('CMENTR03', 'equals', 0o22057, line=325)  # COMMON DOWNLIST DATA

S('CMENTR04', 'equals', 0o22061, line=327)  # COMMON DOWNLIST DATA

W('05,2257', 0o76615, 'CMENTR05', '-1DNADR', 'DELV', 'DELV,+1               SNAPSHOT DATA', kind='data', line=329)
W('05,2260', 0o01164, '', '1DNADR', 'DELV +2', 'DELV+2,+3', kind='data', line=330)
W('05,2261', 0o01166, '', '1DNADR', 'DELV +4', 'DELV+4,+5', kind='data', line=331)
W('05,2262', 0o03726, '', '1DNADR', 'TTE', 'TTE,+1', kind='data', line=332)
W('05,2263', 0o03724, '', '1DNADR', 'VIO', 'VIO,+1', kind='data', line=333)
W('05,2264', 0o03766, '', '1DNADR', 'VPRED', 'VPRED,+1', kind='data', line=334)
W('05,2265', 0o76532, '', '-1DNADR', 'PIPTIME1', 'PIPTIME1,+1', kind='data', line=335)

S('CMENTR07', 'equals', 0o22075, line=337)  # COMMON DOWNLIST DATA

# -------------------------------------------------------------

# Page 179
# P22 DOWNLISTS
#
# --------------------- CONTROL LIST --------------------------

S('CMPG22DL', 'equals', 0o22266, line=346)  # SEND ID BY SPECIAL CODING
W('05,2266', 0o32043, '', 'DNPTR', 'CMPG2201', 'COLLECT SNAPSHOT', kind='data', line=347)
W('05,2267', 0o24340, '', '6DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=348)
W('05,2270', 0o32052, '', 'DNPTR', 'CMPG2202', 'COLLECT SNAPSHOT', kind='data', line=349)
W('05,2271', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=350)
W('05,2272', 0o32057, '', 'DNPTR', 'CMPG2203', 'COMMON DATA', kind='data', line=351)
W('05,2273', 0o27537, '', '6DNADR', 'SVMRKDAT', 'LANDING SITE MARK DATA', kind='data', line=352)
W('05,2274', 0o27553, '', '6DNADR', 'SVMRKDAT +12D', 'SVMRKDAT+0...+34', kind='data', line=353)
W('05,2275', 0o27567, '', '6DNADR', 'SVMRKDAT +24D', 'LANDING SITE MARK DATA', kind='data', line=354)
W('05,2276', 0o02751, '', '1DNADR', 'LANDMARK', 'LANDMARK,GARBAGE', kind='data', line=355)
W('05,2277', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=356)
W('05,2300', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=357)
W('05,2301', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=358)
W('05,2302', 0o32061, '', 'DNPTR', 'CMPG2204', 'COMMON DATA', kind='data', line=359)
W('05,2303', 0o00024, '', '1DNADR', 'TIME2', 'TIME2,TIME1', kind='data', line=360)
W('05,2304', 0o32332, '', 'DNPTR', 'CMPG2205', 'COLLECT SNAPSHOT', kind='data', line=361)
W('05,2305', 0o04340, '', '2DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=362)
W('05,2306', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=363)
W('05,2307', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=364)
W('05,2310', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=365)
W('05,2311', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=366)
W('05,2312', 0o32052, '', 'DNPTR', 'CMPG2202', 'COLLECT SNAPSHOT', kind='data', line=367)
W('05,2313', 0o14340, '', '4DNADR', 'DNTMBUFF', 'SEND SNAPSHOT', kind='data', line=368)
W('05,2314', 0o32057, '', 'DNPTR', 'CMPG2203', 'COMMON DATA', kind='data', line=369)
W('05,2315', 0o32072, '', 'DNPTR', 'CMPG2206', 'COMMON DATA', kind='data', line=370)
W('05,2316', 0o02747, '', '1DNADR', '8NN', '8NN,GARBAGE', kind='data', line=371)
W('05,2317', 0o00106, '', '1DNADR', 'STATE +10D', 'FLAGWRDS 10 AND 11', kind='data', line=372)
W('05,2320', 0o12025, '', '3DNADR', 'RLS', 'RLS,+1,...+4,+5', kind='data', line=373)
W('05,2321', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=374)
W('05,2322', 0o01331, '', '1DNADR', 'OPTMODES', 'OPTMODES,HOLDFLAG', kind='data', line=375)
W('05,2323', 0o32075, '', 'DNPTR', 'CMPG2207', 'COMMON DATA', kind='data', line=376)
W('05,2324', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=377)
W('05,2325', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=378)
W('05,2326', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=379)
W('05,2327', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=380)
W('05,2330', 0o00007, '', '1DNADR', 'SPARE', kind='data', line=381)
W('05,2331', 0o77770, '', '-1DNADR', 'SPARE', kind='data', line=382)

# --------------------- SUB LISTS --------------------------

S('CMPG2201', 'equals', 0o22043, line=386)  # COMMON DOWNLIST DATA

S('CMPG2202', 'equals', 0o22052, line=388)  # COMMON DOWNLIST DATA

S('CMPG2203', 'equals', 0o22057, line=390)  # COMMON DOWNLIST DATA
# Page 180
S('CMPG2204', 'equals', 0o22061, line=392)  # COMMON DOWNLIST DATA

W('05,2332', 0o76672, 'CMPG2205', '-1DNADR', 'LONG', 'LONG,+1                       SNAPSHOT DATA', kind='data', line=394)
W('05,2333', 0o01107, '', '1DNADR', 'ALT', 'ALT,+1', kind='data', line=395)
W('05,2334', 0o76674, '', '-1DNADR', 'LAT', 'LAT,+1', kind='data', line=396)

S('CMPG2206', 'equals', 0o22072, line=398)  # COMMON DOWNLIST DATA

S('CMPG2207', 'equals', 0o22075, line=400)  # COMMON DOWNLIST DATA

# -----------------------------------------------------------

W('05,2335', 0o02107, 'DNTABLE', 'GENADR', 'CMCSTADL', kind='data', line=404)
W('05,2336', 0o02207, '', 'GENADR', 'CMENTRDL', kind='data', line=405)
W('05,2337', 0o02143, '', 'GENADR', 'CMRENDDL', kind='data', line=406)
W('05,2340', 0o02001, '', 'GENADR', 'CMPOWEDL', kind='data', line=407)
W('05,2341', 0o02266, '', 'GENADR', 'CMPG22DL', kind='data', line=408)

# -----------------------------------------------------------
