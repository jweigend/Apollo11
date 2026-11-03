"""The Apollo 11 LM erasable pad load (Luminary 99).

Source: Grumman LM Data Book, Vol. II, table LM5/4.5.1-1 "G Prelaunch Erasable
Load (LUMINARY 99)", LED-540-54 amendment 1-109/1-127 (June/July 1969), as
archived by the Virtual AGC project (Luminary99PadLoads.pdf).  The values below
are the octal words from that table; the address column of the table is
checked against the assembled symbol table when the load is applied, so an
OCR error would be caught.

Mission-time quantities (state vectors, REFSMMAT, TLAND, mass) are not part
of the pad load and are set by the simulation scenario.
"""

from __future__ import annotations

# name -> (octal address of first word, [octal words])
PADLOAD: dict[str, tuple[int, list[int]]] = {
    # --- mission tape -----------------------------------------------------
    "FLAGWRD3": (0o77, [0o02000]),
    "FLAGWRD8": (0o104, [0o00000]),
    "FLGWRD10": (0o106, [0o00000]),
    "DUMPCNT": (0o333, [0o10000]),
    "E3J22R2M": (0o1352, [0o12160]),
    "E32C31RM": (0o1353, [0o03363]),
    "RADSKAL": (0o1354, [0o00000, 0o00000]),
    "SKALSKAL": (0o1356, [0o00000]),
    "GCOMPSW": (0o1477, [0o00000]),
    "TETCSM": (0o1570, [0o37777, 0o37777]),         # inhibits P00 integration of the CSM
    "TETLEM": (0o1642, [0o37777, 0o37777]),         # replaced by the scenario's state vector
    "X789": (0o1700, [0, 0, 0, 0, 0, 0]),
    "RANGEVAR": (0o1770, [0o01351, 0o24734]),
    "RATEVAR": (0o1772, [0o02354, 0o04750]),
    "RVARMIN": (0o1774, [0o00410]),
    "VVARMIN": (0o1775, [0o00165]),
    "WRENDPOS": (0o2000, [0o05750]),
    "WRENDVEL": (0o2001, [0o00763]),
    "WSHAFT": (0o2002, [0o17270]),
    "WTRUN": (0o2003, [0o17270]),
    "RMAX": (0o2004, [0o00023]),
    "VMAX": (0o2005, [0o00001]),                    # 0.006096 m/cs at B7 (2 ft/s); OCR unreadable
    "WSURFPOS": (0o2006, [0o37200]),
    "WSURFVEL": (0o2007, [0o00754]),
    "SHAFTVAR": (0o2010, [0o00103]),
    "TRUNVAR": (0o2011, [0o00103]),
    "AGSK": (0o2020, [0o03671, 0o21200]),
    "TLAND": (0o2400, [0o04247, 0o34030]),          # 100:50:49.20 GET, nominal landing time
    "RBRFG": (0o2402, [0o00000, 0o01506, 0o00000, 0o00000, 0o77774, 0o72222]),
    "VBRFG": (0o2410, [0o77772, 0o72612, 0o00000, 0o00000, 0o77777, 0o76300]),
    "ABRFG": (0o2416, [0o00004, 0o37445, 0o00000, 0o00000, 0o77667, 0o50111]),
    "VBRFG*": (0o2424, [0o77777, 0o74261]),
    "ABRFG*": (0o2426, [0o77113, 0o60670]),
    "JBRFG*": (0o2430, [0o77472, 0o72437]),
    "GAINBRAK": (0o2432, [0o37777, 0o37777]),
    "TCGFBRAK": (0o2434, [0o00567]),
    "TCGIBRAK": (0o2435, [0o25762]),
    "RAPFG": (0o2436, [0o00000, 0o01036, 0o00000, 0o00000, 0o77777, 0o77574]),
    "VAPFG": (0o2444, [0o77777, 0o70152, 0o00000, 0o00000, 0o00000, 0o00306]),
    "AAPFG": (0o2452, [0o77775, 0o74720, 0o00000, 0o00000, 0o77773, 0o75055]),
    "VAPFG*": (0o2460, [0o00000, 0o00676]),
    "AAPFG*": (0o2462, [0o77747, 0o56422]),
    "JAPFG*": (0o2464, [0o00022, 0o35646]),
    "GAINAPPR": (0o2466, [0o00000, 0o00000]),
    "TCGFAPPR": (0o2470, [0o00567]),
    "TCGIAPPR": (0o2471, [0o04704]),
    "VIGN": (0o2472, [0o00416, 0o16071]),
    "RIGNX": (0o2474, [0o77731, 0o44630]),
    "RIGNZ": (0o2476, [0o77125, 0o62404]),
    "KIGNX/B4": (0o2500, [0o76607, 0o61356]),
    "KIGNY/B8": (0o2502, [0o72634, 0o51602]),
    "KIGNV/B4": (0o2504, [0o72775, 0o57777]),
    "LOWCRIT": (0o2506, [0o04114]),
    "HIGHCRIT": (0o2507, [0o04454]),
    "V2FG": (0o2510, [0o77777, 0o73242, 0o00000, 0o00000, 0o00000, 0o00000]),
    "TAUVERT": (0o2516, [0o01750, 0o00000]),
    "DELQFIX": (0o2520, [0o00000, 0o01717]),
    "LRALPHA": (0o2522, [0o01027]),
    "LRBETA1": (0o2523, [0o04204]),
    "LRALPHA2": (0o2524, [0o01022]),
    "LRBETA2": (0o2525, [0o00004]),
    "LRVMAX": (0o2526, [0o01414]),
    "LRVF": (0o2527, [0o00116]),
    "LRWVZ": (0o2530, [0o11463]),
    "LRWVY": (0o2531, [0o11463]),
    "LRWVX": (0o2532, [0o11463]),
    "LRWVFZ": (0o2533, [0o06315]),
    "LRWVFY": (0o2534, [0o06315]),
    "LRWVFX": (0o2535, [0o06315]),
    "LRWVFF": (0o2536, [0o03146]),
    "RODSCALE": (0o2537, [0o14370]),
    "TAUROD": (0o2540, [0o11300, 0o00000]),
    "LAG/TAU": (0o2542, [0o15164, 0o01420]),
    "MINFORCE": (0o2544, [0o00001, 0o27631]),
    "MAXFORCE": (0o2546, [0o00013, 0o06551]),
    "ABTCOF": (0o2550, [0o01311, 0o21176, 0o76401, 0o47023, 0o00132, 0o26223, 0o04231, 0o05721,
                        0o01241, 0o32430, 0o76470, 0o45634, 0o00106, 0o22276, 0o04232, 0o10573]),
    "VMIN": (0o2570, [0o04147, 0o24472]),
    "YLIM": (0o2572, [0o00016, 0o32446]),
    "ABTRDOT": (0o2574, [0o00007, 0o23346]),
    "COSTHET1": (0o2576, [0o00000, 0o00000]),
    "COSTHET2": (0o2600, [0o06733, 0o07535]),
    "ROLLTIME": (0o3001, [0o05556]),
    "PITTIME": (0o3002, [0o04431]),
    "DKTRAP": (0o3003, [0o77001]),
    "DKOMEGAN": (0o3004, [0o00012]),
    "DKKAOSN": (0o3005, [0o00074]),
    "LMTRAP": (0o3006, [0o77001]),
    "LMOMEGAN": (0o3007, [0o00000]),
    "LMKAOSN": (0o3010, [0o00074]),
    "DKDB": (0o3011, [0o00200]),
    "IGNAOSQ": (0o3012, [0o02614]),
    "IGNAOSR": (0o3013, [0o00062]),
    "DOWNTORK": (0o3113, [0, 0, 0, 0, 0, 0]),
    "ATIGINC": (0o3400, [0o00001, 0o03120]),
    "PTIGINC": (0o3402, [0o00001, 0o03120]),
    "AOTAZ": (0o3404, [0o65244, 0o77762, 0o12476, 0o25247, 0o37771, 0o52510]),
    "AOTEL": (0o3412, [0o07777, 0o10006, 0o10006, 0o10000, 0o07772, 0o07771]),
    "LRHMAX": (0o3420, [0o35610]),
    "LRWH": (0o3421, [0o13146]),
    "ZOOMTIME": (0o3422, [0o05050]),                # 26 s: throttle-up after ignition
    "TENDBRAK": (0o3423, [0o01407]),
    "TENDAPPR": (0o3424, [0o00226]),
    "DELTTFAP": (0o3425, [0o75240]),
    "LEADTIME": (0o3426, [0o77743]),
    "RPCRTIME": (0o3427, [0o01407]),
    "RPCRTQSW": (0o3430, [0o77777]),
    "TNEWA": (0o3431, [0o20000, 0o00000]),
    # --- launch tape -------------------------------------------------------
    "MASS": (0o1244, [0o07351, 0o15463]),           # 15269.7 kg at DOI; scenario overrides
    "LEMMASS": (0o1331, [0o07351]),
    "CSMMASS": (0o1332, [0o10050]),
    "PBIASX": (0o1452, [0o06604]),
    "PIPASCFX": (0o1453, [0o73446]),
    "PBIASY": (0o1454, [0o01014]),
    "PIPASCFY": (0o1455, [0o55120]),
    "PBIASZ": (0o1456, [0o02031]),
    "PIPASCFZ": (0o1457, [0o65656]),
    "NBDX": (0o1460, [0o77463]),
    "NBDY": (0o1461, [0o00744]),
    "NBDZ": (0o1462, [0o01060]),
    "ADIAX": (0o1463, [0o00404]),
    "ADIAY": (0o1464, [0o00116]),
    "ADIAZ": (0o1465, [0o77661]),
    "ADSRAX": (0o1466, [0o00234]),
    "ADSRAY": (0o1467, [0o77575]),
    "ADSRAZ": (0o1470, [0o77575]),
    "TEPHEM": (0o1706, [0o00000, 0o20017, 0o20500]),  # launch 16 July 1969 13:32 GMT
    "AZO": (0o1711, [0o30624, 0o01636]),
    "-AYO": (0o1713, [0o77777, 0o53172]),
    "AXO": (0o1715, [0o00000, 0o26056]),
    "504LM": (0o2012, [0o77775, 0o46355, 0o77766, 0o72372, 0o77777, 0o52552]),
    "RLS": (0o2022, [0o00301, 0o34760, 0o00125, 0o04627, 0o00002, 0o24342]),  # landing site, moon-fixed, m B27
    "HIASCENT": (0o3000, [0o02350]),
}

# A perfect simulated IMU has no bias, scale-factor or drift errors.  With the
# real compensation values the AGC would "correct" errors that do not exist.
PERFECT_IMU_ZEROES = ["PBIASX", "PIPASCFX", "PBIASY", "PIPASCFY", "PBIASZ", "PIPASCFZ",
                      "NBDX", "NBDY", "NBDZ", "ADIAX", "ADIAY", "ADIAZ", "ADSRAX", "ADSRAY", "ADSRAZ"]


def apply_padload(cpu, prog, perfect_imu: bool = True, skip: tuple[str, ...] = ()) -> list[str]:
    """Write the pad load into erasable memory.  Returns a list of warnings."""
    warnings = []
    for name, (address, words) in PADLOAD.items():
        if name in skip:
            continue
        sym = prog.symbol(name)
        if sym is None or sym.erasable_address() is None:
            warnings.append(f"{name}: symbol not found in program, using documented address {address:04o}")
            ea = address
        else:
            ea = sym.erasable_address()
            if ea != address:
                warnings.append(f"{name}: assembled at {ea:04o} but pad load table says {address:04o}; using {ea:04o}")
        if perfect_imu and name in PERFECT_IMU_ZEROES:
            words = [0] * len(words)
        for i, w in enumerate(words):
            cpu.e[ea + i] = w & 0o77777
    return warnings
