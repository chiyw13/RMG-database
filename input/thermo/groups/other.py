#!/usr/bin/env python
# encoding: utf-8

name = "Other Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "R",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""dummy root""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "ketene",
    group = 
"""
1 * C u0 {2,D} {3,S} {4,S}
2   C u0 {1,D} {5,D}
3   R u0 {1,S}
4   R u0 {1,S}
5   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""All the corrections from this family are from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "ketene_2C-C",
    group = 
"""
1 * C       u0 {2,D} {3,S} {4,S}
2   C       u0 {1,D} {5,D}
3   [Cs,Cd] u0 {1,S} {6,S}
4   [Cs,Cd] u0 {1,S} {7,S}
5   O       u0 {2,D}
6   C       u0 {3,S}
7   C       u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NN2 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "ketene_1C-C_1C-H",
    group = 
"""
1 * C       u0 {2,D} {3,S} {4,S}
2   C       u0 {1,D} {5,D}
3   [Cs,Cd] u0 {1,S} {6,S}
4   C       u0 {1,S} {7,S} {8,S} {9,S}
5   O       u0 {2,D}
6   C       u0 {3,S}
7   H       u0 {4,S}
8   H       u0 {4,S}
9   H       u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NN1 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "biketene",
    group = 
"""
1    C   u0 {2,S} {3,S} {4,S} {5,S}
2    C   u0 {1,S} {6,D}
3  * C   u0 {1,S} {7,D} {10,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
6    C   u0 {2,D} {8,D}
7    C   u0 {3,D} {9,D}
8    O   u0 {6,D}
9    O   u0 {7,D}
10   R   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-0.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NN3 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "ketene_2C-H",
    group = 
"""
1  * C u0 {2,D} {3,S} {4,S}
2    C u0 {1,D} {5,D}
3    C u0 {1,S} {6,S} {7,S} {8,S}
4    C u0 {1,S} {9,S} {10,S} {11,S}
5    O u0 {2,D}
6    H u0 {3,S}
7    H u0 {3,S}
8    H u0 {3,S}
9    H u0 {4,S}
10   H u0 {4,S}
11   H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NN0 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "monocyclicaromatics",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    [Cs,Cd,CO,Os] u0 {1,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "1_vinyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "1_vinyl_oo_2_vinyl_3_vinyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {20,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   Cd u0 {6,S} {21,D} {24,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
17   Cd u0 {8,D} {18,S} {19,S}
18   H  u0 {17,S}
19   H  u0 {17,S}
20   H  u0 {8,S}
21   Cd u0 {12,D} {22,S} {23,S}
22   H  u0 {21,S}
23   H  u0 {21,S}
24   H  u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "1_vinyl_oo_2_vinyl_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {20,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   Os u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
17   Cd u0 {8,D} {18,S} {19,S}
18   H  u0 {17,S}
19   H  u0 {17,S}
20   H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "1_vinyl_oo_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   C u0 {6,S} {19,D} {20,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
17   O  u0 {8,D}
18   H  u0 {8,S}
19   O  u0 {12,D}
20   H  u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "1_vinyl_oo_2_formyl_3_vinyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   Cd u0 {6,S} {19,D} {20,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
17   O  u0 {8,D}
18   H  u0 {8,S}
19   Cd u0 {12,D} {21,S} {22,S}
20   H  u0 {12,S}
21   H  u0 {19,S}
22   H  u0 {19,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "1_vinyl_oo_2_formyl_3_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   Cs u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
17   O  u0 {8,D}
18   H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "1_vinyl_oo_2_formyl_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   Os u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
17   O  u0 {8,D}
18   H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "1_vinyl_oo_2_vinyl_3_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {20,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   Cs u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
17   Cd u0 {8,D} {18,S} {19,S}
18   H  u0 {17,S}
19   H  u0 {17,S}
20   H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "1_vinyl_oo_2_Cs_3_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cs u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   Cs u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "1_vinyl_oo_2_Cs_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cs u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   Os u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "1_vinyl_o_2_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
17   O  u0 {8,D}
18   H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "1_vinyl_o_2_vinyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {20,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
17   Cd u0 {8,D} {18,S} {19,S}
18   H  u0 {17,S}
19   H  u0 {17,S}
20   H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "1_vinyl_o_2_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cs u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "1_vinyl_o_2_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Os u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   Cd u0 {7,D} {14,S} {15,S}
14   H  u0 {13,S}
15   H  u0 {13,S}
16   H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "1_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   H u0 {7,S}
15   [H,Cs] u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "1_Cs_oo_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    C u0 {2,S} {16,D} {17,S}
9    R  u0 {3,S}
10   R  u0 {4,S}
11   R  u0 {5,S}
12   C u0 {6,S} {18,D} {19,S}
13   H u0 {7,S}
14   H u0 {7,S}
15   [H,Cs] u0 {7,S}
16   O u0 {8,D}
17   H u0 {8,S}
18   O u0 {12,D}
19   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "1_Cs_oo_2_formyl_3_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    C u0 {2,S} {16,D} {17,S}
9    R  u0 {3,S}
10   R  u0 {4,S}
11   R  u0 {5,S}
12   Cs u0 {6,S} {18,S} {19,S} {20,S}
13   H u0 {7,S}
14   H u0 {7,S}
15   [H,Cs] u0 {7,S}
16   O u0 {8,D}
17   H u0 {8,S}
18   H u0 {12,S}
19   H u0 {12,S}
20   [H,Cs] u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "1_Cs_oo_2_Cs_3_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    Cs u0 {2,S} {16,S} {17,S} {18,S}
9    R  u0 {3,S}
10   R  u0 {4,S}
11   R  u0 {5,S}
12   Cs u0 {6,S} {19,S} {20,S} {21,S}
13   H u0 {7,S}
14   H u0 {7,S}
15   [H,Cs] u0 {7,S}
16   H u0 {8,S}
17   H u0 {8,S}
18   [H,Cs] u0 {8,S}
19   H u0 {12,S}
20   H u0 {12,S}
21   [H,Cs] u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "1_Cs_o_2_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    C u0 {2,S} {16,D} {17,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   H u0 {7,S}
15   [H,Cs] u0 {7,S}
16   O u0 {8,D}
17   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "1_Cs_o_2_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    Cs u0 {2,S} {16,S} {17,S} {18,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   H u0 {7,S}
15   [H,Cs] u0 {7,S}
16   H u0 {8,S}
17   H u0 {8,S}
18   [H,Cs] u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "1_OH",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "1_OH_oop_2_formyl_3_formyl_4_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   C u0 {4,S} {18,D} {19,S}
11   R u0 {5,S}
12   C u0 {6,S} {16,D} {17,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   O u0 {12,D}
17   H u0 {12,S}
18   O u0 {10,D}
19   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "1_OH_oop_2_formyl_3_formyl_4_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   Os u0 {4,S} {18,S}
11   R u0 {5,S}
12   C u0 {6,S} {16,D} {17,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   O u0 {12,D}
17   H u0 {12,S}
18   [H,Cs] u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "1_OH_oop_2_formyl_3_Os_4_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   C u0 {4,S} {17,D} {18,S}
11   R u0 {5,S}
12   O u0 {6,S} {16,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   [H,Cs] u0 {12,S}
17   O u0 {10,D}
18   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "1_OH_oop_2_formyl_3_Os_4_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   O u0 {4,S} {17,S}
11   R u0 {5,S}
12   O u0 {6,S} {16,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   [H,Cs] u0 {12,S}
17   [H,Cs] u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "1_OH_oop_2_Os_3_Os_4_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {14,S}
9    R u0 {3,S}
10   C u0 {4,S} {16,D} {17,S}
11   R u0 {5,S}
12   O u0 {6,S} {15,S}
13   H u0 {7,S}
14   [H,Cs] u0 {8,S}
15   [H,Cs] u0 {12,S}
16   O u0 {10,D}
17   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "1_OH_oop_2_Os_3_Os_4_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {14,S}
9    R u0 {3,S}
10   O u0 {4,S} {16,S}
11   R u0 {5,S}
12   O u0 {6,S} {15,S}
13   H u0 {7,S}
14   [H,Cs] u0 {8,S}
15   [H,Cs] u0 {12,S}
16   [H,Cs] u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "1_OH_oo_2_Os_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {14,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   O u0 {6,S} {15,S}
13   H u0 {7,S}
14   [H,Cs] u0 {8,S}
15   [H,Cs] u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "1_OH_oo_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   C u0 {6,S} {16,D} {17,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   O u0 {12,D}
17   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "1_OH_oo_2_formyl_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   O u0 {6,S} {16,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   [H,Cs] u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "1_OH_op_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   C u0 {4,S} {16,D} {17,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   O u0 {10,D}
17   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "1_OH_op_2_formyl_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   O u0 {4,S} {16,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   [H,Cs] u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "1_OH_op_2_Os_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {14,S}
9    R u0 {3,S}
10   C u0 {4,S} {15,D} {16,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   [H,Cs] u0 {8,S}
15   O u0 {10,D}
16   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "1_OH_op_2_Os_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {14,S}
9    R u0 {3,S}
10   O u0 {4,S} {15,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   [H,Cs] u0 {8,S}
15   [H,Cs] u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "1_OH_o_2_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O  u0 {1,S} {13,S}
8    C u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "1_OH_o_2_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O  u0 {1,S} {13,S}
8    O u0 {2,S} {14,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   [H,Cs] u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "1_OH_p_2_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   C u0 {4,S} {14,D} {15,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   O u0 {10,D}
15   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "1_OH_p_2_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   O u0 {4,S} {14,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   H u0 {7,S}
14   [H,Cs] u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "1_methoxy",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "1_methoxy_oop_2_methoxy_3_methoxy_4_methoxy",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {17,S}
9    R u0 {3,S}
10   O u0 {4,S} {25,S}
11   R u0 {5,S}
12   O u0 {6,S} {21,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {8,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
21   C u0 {12,S} {22,S} {23,S} {24,S}
22   H u0 {21,S}
23   H u0 {21,S}
24   H u0 {21,S}
25   C u0 {10,S} {26,S} {27,S} {28,S}
26   H u0 {25,S}
27   H u0 {25,S}
28   H u0 {25,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "1_methoxy_oop_2_methoxy_3_methoxy_4_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {17,S}
9    R u0 {3,S}
10   C u0 {4,S} {25,D} {26,S}
11   R u0 {5,S}
12   O u0 {6,S} {21,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {8,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
21   C u0 {12,S} {22,S} {23,S} {24,S}
22   H u0 {21,S}
23   H u0 {21,S}
24   H u0 {21,S}
25   O u0 {10,D}
26   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "1_methoxy_oop_2_methoxy_3_formyl_4_methoxy",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {17,S}
9    R u0 {3,S}
10   O u0 {4,S} {23,S}
11   R u0 {5,S}
12   C u0 {6,S} {21,D} {22,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {8,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
21   O u0 {12,D}
22   H u0 {12,S}
23   C u0 {10,S} {24,S} {25,S} {26,S}
24   H u0 {23,S}
25   H u0 {23,S}
26   H u0 {23,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "1_methoxy_oop_2_methoxy_3_formyl_4_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {17,S}
9    R u0 {3,S}
10   C u0 {4,S} {23,D} {24,S}
11   R u0 {5,S}
12   C u0 {6,S} {21,D} {22,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {8,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
21   O u0 {12,D}
22   H u0 {12,S}
23   O u0 {10,D}
24   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "1_methoxy_oop_2_formyl_3_formyl_4_methoxy",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   O u0 {4,S} {21,S}
11   R u0 {5,S}
12   C u0 {6,S} {19,D} {20,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   O u0 {8,D}
18   H u0 {8,S}
19   O u0 {12,D}
20   H u0 {12,S}
21   C u0 {10,S} {22,S} {23,S} {24,S}
22   H u0 {21,S}
23   H u0 {21,S}
24   H u0 {21,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "1_methoxy_oop_2_formyl_3_formyl_4_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   C u0 {4,S} {21,D} {22,S}
11   R u0 {5,S}
12   C u0 {6,S} {19,D} {20,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   O u0 {8,D}
18   H u0 {8,S}
19   O u0 {12,D}
20   H u0 {12,S}
21   O u0 {10,D}
22   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "1_methoxy_oo_2_methoxy_3_methoxy",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {17,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   O u0 {6,S} {21,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {8,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
21   C u0 {12,S} {22,S} {23,S} {24,S}
22   H u0 {21,S}
23   H u0 {21,S}
24   H u0 {21,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "1_methoxy_oo_2_methoxy_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {17,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   C u0 {6,S} {21,D} {22,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {8,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
21   O u0 {12,D}
22   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "1_methoxy_oo_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   C u0 {6,S} {19,D} {20,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   O u0 {8,D}
18   H u0 {8,S}
19   O u0 {12,D}
20   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "1_methoxy_op_2_methoxy_3_methoxy",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {17,S}
9    R u0 {3,S}
10   O u0 {4,S} {21,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {8,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
21   C u0 {10,S} {22,S} {23,S} {24,S}
22   H u0 {21,S}
23   H u0 {21,S}
24   H u0 {21,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "1_methoxy_op_2_methoxy_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {17,S}
9    R u0 {3,S}
10   C u0 {4,S} {21,D} {22,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {8,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
21   O u0 {10,D}
22   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "1_methoxy_op_2_formyl_3_methoxy",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {21,D} {22,S}
9    R u0 {3,S}
10   O u0 {4,S} {17,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {10,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
21   O u0 {8,D}
22   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "1_methoxy_op_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   C u0 {4,S} {19,D} {20,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   O u0 {8,D}
18   H u0 {8,S}
19   O u0 {10,D}
20   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "1_methoxy_o_2_methoxy",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    O u0 {2,S} {17,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {8,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "1_methoxy_o_2_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    C u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   O u0 {8,D}
18   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "1_methoxy_p_2_methoxy",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   O u0 {4,S} {17,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   C u0 {10,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "1_methoxy_p_2_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   C u0 {4,S} {17,D} {18,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   C u0 {7,S} {14,S} {15,S} {16,S}
14   H u0 {13,S}
15   H u0 {13,S}
16   H u0 {13,S}
17   O u0 {10,D}
18   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "1_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "1_formyl_oommp",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    C u0 {3,S} {17,D} {18,S}
10   C u0 {4,S} {19,D} {20,S}
11   C u0 {5,S} {21,D} {22,S}
12   C u0 {6,S} {23,D} {24,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {9,D}
18   H u0 {9,S}
19   O u0 {10,D}
20   H u0 {10,S}
21   O u0 {11,D}
22   H u0 {11,S}
23   O u0 {12,D}
24   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "1_formyl_oomm",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    C u0 {3,S} {17,D} {18,S}
10   R u0 {4,S}
11   C u0 {5,S} {21,D} {22,S}
12   C u0 {6,S} {19,D} {20,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {9,D}
18   H u0 {9,S}
19   O u0 {12,D}
20   H u0 {12,S}
21   O u0 {11,D}
22   H u0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "1_formyl_oomp",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    C u0 {3,S} {17,D} {18,S}
10   C u0 {4,S} {19,D} {20,S}
11   R u0 {5,S} 
12   C u0 {6,S} {21,D} {22,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {9,D}
18   H u0 {9,S}
19   O u0 {10,D}
20   H u0 {10,S}
21   O u0 {12,D}
22   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "1_formyl_ommp",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    C u0 {3,S} {17,D} {18,S}
10   C u0 {4,S} {19,D} {20,S}
11   C u0 {5,S} {21,D} {22,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {9,D}
18   H u0 {9,S}
19   O u0 {10,D}
20   H u0 {10,S}
21   O u0 {11,D}
22   H u0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "1_formyl_oom",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    C u0 {3,S} {17,D} {18,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   C u0 {6,S} {19,D} {20,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {9,D}
18   H u0 {9,S}
19   O u0 {12,D}
20   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "1_formyl_oop",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    R u0 {3,S}
10   C u0 {4,S} {17,D} {18,S}
11   R u0 {5,S}
12   C u0 {6,S} {19,D} {20,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {10,D}
18   H u0 {10,S}
19   O u0 {12,D}
20   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "1_formyl_omm",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    C u0 {3,S} {17,D} {18,S}
10   R u0 {4,S}
11   C u0 {5,S} {19,D} {20,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {9,D}
18   H u0 {9,S}
19   O u0 {11,D}
20   H u0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "1_formyl_omp_o",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    C u0 {3,S} {17,D} {18,S}
10   C u0 {4,S} {19,D} {20,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {9,D}
18   H u0 {9,S}
19   O u0 {10,D}
20   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "1_formyl_omp_p",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    R u0 {3,S}
10   C u0 {4,S} {19,D} {20,S}
11   C u0 {5,S} {17,D} {18,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {11,D}
18   H u0 {11,S}
19   O u0 {10,D}
20   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "1_formyl_mmp",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    R u0 {2,S}
9    C u0 {3,S} {15,D} {16,S}
10   C u0 {4,S} {19,D} {20,S}
11   C u0 {5,S} {17,D} {18,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {9,D}
16   H u0 {9,S}
17   O u0 {11,D}
18   H u0 {11,S}
19   O u0 {10,D}
20   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "1_formyl_oo",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   C u0 {6,S} {17,D} {18,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {12,D}
18   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "1_formyl_om_o",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    C u0 {3,S} {17,D} {18,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {9,D}
18   H u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "1_formyl_om_p",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   C u0 {5,S} {17,D} {18,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {11,D}
18   H u0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "1_formyl_op",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    R u0 {3,S}
10   C u0 {4,S} {17,D} {18,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
17   O u0 {10,D}
18   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "1_formyl_mm",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    R u0 {2,S}
9    C u0 {3,S} {15,D} {16,S}
10   R u0 {4,S}
11   C u0 {5,S} {17,D} {18,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {9,D}
16   H u0 {9,S}
17   O u0 {11,D}
18   H u0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "1_formyl_mp",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    R u0 {2,S}
9    C u0 {3,S} {15,D} {16,S}
10   C u0 {4,S} {17,D} {18,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {9,D}
16   H u0 {9,S}
17   O u0 {10,D}
18   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "1_formyl_o",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    C u0 {2,S} {15,D} {16,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {8,D}
16   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "1_formyl_m",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    R u0 {2,S}
9    C u0 {3,S} {15,D} {16,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {9,D}
16   H u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "1_formyl_p",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    C u0 {1,S} {13,D} {14,S}
8    R u0 {2,S}
9    R u0 {3,S}
10   C u0 {4,S} {15,D} {16,S}
11   R u0 {5,S}
12   R u0 {6,S}
13   O u0 {7,D}
14   H u0 {7,S}
15   O u0 {10,D}
16   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: R
    L2: ketene
        L3: ketene_2C-C
        L3: ketene_1C-C_1C-H
        L3: biketene
        L3: ketene_2C-H
    L2: monocyclicaromatics
        L3: 1_vinyl
            L4: 1_vinyl_oo_2_formyl_3_formyl
            L4: 1_vinyl_oo_2_formyl_3_vinyl
            L4: 1_vinyl_oo_2_formyl_3_Cs
            L4: 1_vinyl_oo_2_formyl_3_Os
            L4: 1_vinyl_oo_2_vinyl_3_vinyl
            L4: 1_vinyl_oo_2_vinyl_3_Cs
            L4: 1_vinyl_oo_2_vinyl_3_Os
            L4: 1_vinyl_oo_2_Cs_3_Cs
            L4: 1_vinyl_oo_2_Cs_3_Os
            L4: 1_vinyl_o_2_formyl
            L4: 1_vinyl_o_2_vinyl
            L4: 1_vinyl_o_2_Cs
            L4: 1_vinyl_o_2_Os
        L3: 1_Cs
            L4: 1_Cs_oo_2_formyl_3_formyl
            L4: 1_Cs_oo_2_formyl_3_Cs
            L4: 1_Cs_oo_2_Cs_3_Cs
            L4: 1_Cs_o_2_formyl
            L4: 1_Cs_o_2_Cs
        L3: 1_OH
            L4: 1_OH_oop_2_formyl_3_formyl_4_formyl
            L4: 1_OH_oop_2_formyl_3_formyl_4_Os
            L4: 1_OH_oop_2_formyl_3_Os_4_formyl
            L4: 1_OH_oop_2_formyl_3_Os_4_Os
            L4: 1_OH_oop_2_Os_3_Os_4_formyl
            L4: 1_OH_oop_2_Os_3_Os_4_Os
            L4: 1_OH_oo_2_formyl_3_formyl
            L4: 1_OH_oo_2_formyl_3_Os
            L4: 1_OH_oo_2_Os_3_Os
            L4: 1_OH_op_2_formyl_3_formyl
            L4: 1_OH_op_2_formyl_3_Os
            L4: 1_OH_op_2_Os_3_formyl
            L4: 1_OH_op_2_Os_3_Os
            L4: 1_OH_o_2_formyl
            L4: 1_OH_o_2_Os
            L4: 1_OH_p_2_formyl
            L4: 1_OH_p_2_Os
        L3: 1_methoxy
            L4: 1_methoxy_oop_2_methoxy_3_methoxy_4_methoxy
            L4: 1_methoxy_oop_2_methoxy_3_methoxy_4_formyl
            L4: 1_methoxy_oop_2_methoxy_3_formyl_4_methoxy
            L4: 1_methoxy_oop_2_methoxy_3_formyl_4_formyl
            L4: 1_methoxy_oop_2_formyl_3_formyl_4_methoxy
            L4: 1_methoxy_oop_2_formyl_3_formyl_4_formyl
            L4: 1_methoxy_oo_2_methoxy_3_methoxy
            L4: 1_methoxy_oo_2_methoxy_3_formyl
            L4: 1_methoxy_oo_2_formyl_3_formyl
            L4: 1_methoxy_op_2_methoxy_3_methoxy
            L4: 1_methoxy_op_2_methoxy_3_formyl
            L4: 1_methoxy_op_2_formyl_3_methoxy
            L4: 1_methoxy_op_2_formyl_3_formyl
            L4: 1_methoxy_o_2_methoxy
            L4: 1_methoxy_o_2_formyl
            L4: 1_methoxy_p_2_methoxy
            L4: 1_methoxy_p_2_formyl
        L3: 1_formyl
            L4: 1_formyl_oommp
            L4: 1_formyl_oomm
            L4: 1_formyl_oomp
            L4: 1_formyl_ommp
            L4: 1_formyl_oom
            L4: 1_formyl_oop
            L4: 1_formyl_omm
            L4: 1_formyl_omp_o
            L4: 1_formyl_omp_p
            L4: 1_formyl_mmp
            L4: 1_formyl_oo
            L4: 1_formyl_om_o
            L4: 1_formyl_om_p
            L4: 1_formyl_op
            L4: 1_formyl_mm
            L4: 1_formyl_mp
            L4: 1_formyl_o
            L4: 1_formyl_m
            L4: 1_formyl_p
"""
)

