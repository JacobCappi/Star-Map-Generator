class Constellation:
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars

constellation_list = []

# Creating Andromeda constellation
andromeda = Constellation("Andromeda", {
    2183: [3816, 2050, 2138, 495],
    3816: [6724, 3092],
    2050: [3816, 84573],
    84541: [84683],
    84683: [84573],
    84573: [82539],
    3092: [2704],
    2704: [3804],
    3804: [5315],
    2138: [2574],
    2574: [3113]
})
constellation_list.append(andromeda)

# Creating Aquarius constellation
aquarius = Constellation("Aquarius", {
    74474: [74803],
    74803: [77257],
    77257: [79284, 79334],
    79284: [79976, 80250, 80445],
    80445: [80644],
    79976: [82014],
    82014: [81843],
    81843: [82126],
    80250: [80644],
    80644: [80999, 80250]
})
constellation_list.append(aquarius)

# Creating Aries constellation
aries = Constellation("Aries", {
    9257: [6888],
    6888: [6195],
    6195: [6147]
})
constellation_list.append(aries)

# Creating Taurus constellation
taurus = Constellation("Taurus", {
    18796: [15108],
    15108: [14714],
    14714: [14183],
    14183: [14373, 13110],
    14373: [14710],
    14710: [18021],
    13110: [11284]
})
constellation_list.append(taurus)

# Creating Gemini constellation
gemini = Constellation("Gemini", {
    27698: [27015],
    27015: [25932, 27636, 25267],
    25932: [24803, 25784],
    24803: [22916],
    25784: [23453],
    27636: [27015],
    25267: [23969, 23358, 26923],
    23358: [21860, 22291],
    21860: [21289]
})
constellation_list.append(gemini)

# Creating Cancer constellation
cancer = Constellation("Cancer", {
    31816: [31577],
    31577: [31661],
    31661: [32566, 29788]
})
constellation_list.append(cancer)

# Creating Leo constellation
leo = Constellation("Leo", {
    35524: [35934],
    35934: [37309],
    37309: [37506],
    37506: [36763, 40626],
    36763: [36830],
    36830: [40631],
    40631: [42525]
})
constellation_list.append(leo)


Virgo = Constellation("Virgo", {
                52290: [49844],
                49844: [48306],
                48306: [47773, 46201],
                47773: [50455, 46929],
                50455: [50649],
                50649: [52116],
                40631: [42525],
                42525: [40626],
                46201: [46533],
                46929: [45451],
                45451: [46201],
            })
constellationList.append(Virgo)

Libra = Constellation("Libra", {
                53308: [52562],
                52562: [54037, 55074],
                55074: [54037, 55172],
                55172: [55262],
            })
constellationList.append(Libra)

Scorpio = Constellation("Scorpio", {
                61677: [61845],
                61845: [62385],
                62385: [62676],
                62676: [62069],
                62069: [60538],
                60538: [59500],
                59500: [59345],
                59345: [59254],
                59254: [58437],
                58437: [58094],
                58094: [57640],
                57640: [56460],
                56460: [56747, 56365],
                56747: [57143],
                56365: [56260],
            })
constellationList.append(Scorpio)

Sagittarius = Constellation("Sagittarius", {
                67811: [67014],
                67014: [66393],
                66393: [67523, 65228],
                67523: [67811, 64997],
                65228: [64804],
                64804: [64997, 63828],
                63828: [64997],
            })
constellationList.append(Sagittarius)

Capricornus = Constellation("Capricornus", {
                72769: [74379, 75605],
                74379: [74748],
                74748: [76950],
                76950: [77585],
                77585: [78188],
                78188: [77773],
                77773: [76670],
                76670: [75605],
            })
constellationList.append(Capricornus)


Pisces = Constellation("Pisces",
    { 3909: [4313, 4011],
      4313: [4011],
      4011: [4959],
      4959: [5731],
      5731: [6605],
      6605: [5510],
      5510: [4892],
      4892: [3437],
      3437: [2640],
      2640: [85716],
      85716: [84662],
      84662: [84008, 84769],
      84008: [83413],
      83413: [83938],
      83938: [84769]
    })
constellationList.append(Pisces)

UrsaMinor = Constellation("Ursa Minor",
    { 8222: [61768],
      61768: [59031],
      59031: [55573],
      55573: [52554, 57447],
      52554: [54251],
      54251: [57447]
    })
constellationList.append(UrsaMinor)

UrsaMajor = Constellation("Ursa Major",
    { 49038: [47710],
      47710: [46117],
      46117: [43967],
      43967: [42763, 40027],
      42763: [39924],
      39924: [40027]
    })
constellationList.append(UrsaMajor)

Draco = Constellation("Draco",
    { 41542: [45013],
      45013: [50004],
      50004: [54497],
      54497: [56548],
      56548: [57797],
      57797: [60353],
      60353: [62344],
      62344: [64810],
      64810: [68391],
      68391: [70523],
      70523: [68192],
      68192: [63065],
      63065: [61773, 63252],
      61773: [61657],
      61657: [63252]
    })
constellationList.append(Draco)

Cepheus = Constellation("Cepheus",
    { 76423: [77064, 77981, 74331],
      74331: [73336],
      77064: [84631, 81849],
      84631: [81849],
      81849: [80665],
      80665: [79646],
      79646: [79864],
      79864: [77981]
    })
constellationList.append(Cepheus)

Cassiopeia = Constellation("Cassiopeia",
    { 544: [2243],
      2243: [3084],
      3084: [4667],
      4667: [6182]
    })
constellationList.append(Cassiopeia)


Auriga = Constellation("Auriga", {
    18021: [20267, 16265],
    20267: [20254],
    20254: [17425],
    17425: [16550],
    16550: [16813],
    16813: [16265]
})
constellationList.append(Auriga)

Bootes = Constellation("Bootes", {
    49140: [49019],
    49019: [49456],
    49456: [50628],
    50628: [51524, 52212, 52000],
    51524: [51541],
    51541: [53203, 50672],
    53203: [53953],
    53953: [52212],
    50672: [50491, 51152],
    50491: [51152]
})
constellationList.append(Bootes)

Centaurus = Constellation("Centaurus", {
    51926: [49969],
    49969: [48596],
    48596: [49509, 45444],
    49509: [49150, 45444],
    49150: [49143],
    49143: [51714, 50118, 48088],
    51714: [53060],
    48088: [47527],
    45444: [44708],
    44708: [43573],
    43573: [43743],
    43743: [41017]
})
constellationList.append(Centaurus)

Cygnus = Constellation("Cygnus", {
    74084: [72847],
    72847: [71041, 74382, 70319],
    71041: [69376]
})
constellationList.append(Cygnus)

Orion = Constellation("Orion", {
    17947: [19984],
    19984: [19013],
    19013: [18686, 19506],
    18686: [18386],
    18386: [17301],
    17013: [18686]
})
constellationList.append(Orion)

Hercules = Constellation("Hercules", {
    57888: [57682],
    # 57682: [58128],
    58128: [60677, 58736, 57682],
    60677: [60696],
    60696: [61675, 59842],
    61675: [62610],
    62610: [63335],
    63335: [63949],
    59842: [58736, 60697],
    60697: [61241, 58841],
    61241: [63232],
    63232: [62201],
    58841: [58736, 58344],
    58344: [57559]
})
constellationList.append(Hercules)




Aquila = Constellation("Aquila",
    {
        67320: [67718, ],
        67718: [69041, ],
        69041: [67763, 70803, 70401],
        67763: [69783, ],
        69783: [72099, ],
        72099: [70803, ],
        70401: [70683, ],
        70683: [70987, ],
    })
constellationList.append(Aquila)

CanisMajor = Constellation("Canis Major",
    {
        26214: [25082, ],
        25082: [24404, 24711, ],
        24404: [24072, ],
        24072: [22848, ],
        22848: [21842, ],
        21842: [23440, ],
        23440: [24711, 24225, ],
        24225: [24766, 24079, ],
        24766: [24079, ],
    })
constellationList.append(CanisMajor)

CanisMinor = Constellation("Canis Minor",
    {
        27267: [26419, ],
    })
constellationList.append(CanisMinor)

Crux = Constellation("Crux",
    {
        45767: [43947, ],
        44632: [44890, ],
    })
constellationList.append(Crux)

Hydra = Constellation("Hydra",
    {
        50094: [47425, ],
        47425: [42717, ],
        42717: [41635, ],
        41635: [39238, ],
        39238: [37870, ],
        37870: [36946, ],
        36946: [35865, ],
        35865: [34371, ],
        34371: [35170, ],
        35170: [33540, ],
        33540: [32366, ],
        32366: [31822, ],
        31822: [31185, ],
        31185: [66304, ],
        66304: [31571, ],
        31571: [31914, ],
    })
constellationList.append(Hydra)

Lyra = Constellation("Lyra",
    {
        65795: [66302, 66340, ],
        66302: [66340, ],
        66340: [66965, 66674, ],
        66965: [67277, ],
        66674: [67277, ],
    })
constellationList.append(Lyra)



Pegasus = Constellation("Pegasus", {
                79533: [81457],
                81457: [82663],
                82663: [81865, 82712, 495],
                81865: [81652],
                81652: [79360],
                79360: [78049],
                82712: [81657, 782],
                81657: [81364],
                81364: [79545],
                79545: [78021],
                782: [495],
            })
constellationList.append(Pegasus)

Perseus = Constellation("Perseus", {
                50098: [12791],
                12791: [13038],
                13038: [12986],
                12986: [10217, 12151],
                10217: [10058, 10288],
                10288: [10260],
                10260: [9483, 11142, 8956],
                9483: [9298, 10038],
                10038: [9298, 11142],
                11142: [12151],
                12151: [13888],
            })
constellationList.append(Perseus)

# Return the list of constellations
return constellationList
