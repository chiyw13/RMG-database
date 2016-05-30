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
7    [Cs,Cd,Os] u0 {1,S}
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
    index = 15,
    label = "1_vinyl_doubleortho",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    [Cs,Cd,Os] u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   [Cs,Cd,Os] u0 {6,S}
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
    index = 16,
    label = "1_vinyl_singleortho",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    [Cs,Cd,Os] u0 {2,S}
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
    index = 17,
    label = "1_vinyl_2_vinyl_3CsCdOs",
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
12   [Cs,Cd,Os] u0 {6,S}
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
    index = 18,
    label = "1_vinyl_2_vinyl_3_vinyl",
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
    label = "1_vinyl_2_vinyl_3_Os",
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
    index = 20,
    label = "1_vinyl_2_formyl_3CsCdOs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {18,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   [Cs,Cd,Os] u0 {6,S}
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
    index = 21,
    label = "1_vinyl_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {18,S}
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
    label = "1_vinyl_2_formyl_3_vinyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {18,S}
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
    label = "1_vinyl_2_formyl_3_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {18,S}
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
    label = "1_vinyl_2_formyl_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {18,S}
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
    label = "1_vinyl_2_vinyl_3_Cs",
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
    index = 26,
    label = "1_vinyl_2_Cs_3CsOs",
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
12   [Cs,Os] u0 {6,S}
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
    index = 27,
    label = "1_vinyl_2_Cs_3_Cs",
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
    label = "1_vinyl_2_Cs_3_Os",
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
    label = "1_vinyl_2_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cd u0 {1,S} {13,D} {16,S}
8    Cd u0 {2,S} {17,D} {18,S}
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
    label = "1_vinyl_2_vinyl",
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
    label = "1_vinyl_2_Cs",
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
    label = "1_vinyl_2_Os",
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
    index = 34,
    label = "1_Cs_doubleortho",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    [Cs,CO] u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   [Cs,CO] u0 {6,S}
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
    index = 35,
    label = "1_Cs_2_formyl_3CsCO",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    Cd u0 {2,S} {16,D} {17,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   [Cs,CO] u0 {6,S}
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
    index = 36,
    label = "1_Cs_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    Cd u0 {2,S} {16,D} {17,S}
9    R  u0 {3,S}
10   R  u0 {4,S}
11   R  u0 {5,S}
12   Cd u0 {6,S} {18,D} {19,S}
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
    label = "1_Cs_2_formyl_3_Cs",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    Cd u0 {2,S} {16,D} {17,S}
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
    label = "1_Cs_2_Cs_3_Cs",
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
    index = 39,
    label = "1_Cs_singleortho",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    [Cs,CO] u0 {2,S}
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
    index = 40,
    label = "1_Cs_2_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    Cs u0 {1,S} {13,S} {14,S} {15,S}
8    Cd u0 {2,S} {16,D} {17,S}
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
    label = "1_Cs_2_Cs",
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
    index = 43,
    label = "1_OH_triplesub_oop",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    [CO,Os] u0 {2,S}
9    R u0 {3,S}
10   [CO,Os] u0 {4,S}
11   R u0 {5,S}
12   [CO,Os] u0 {6,S}
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
    index = 44,
    label = "1_OH_2_formyl_3_formyl_4p",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   [CO,Os] u0 {4,S}
11   R u0 {5,S}
12   Cd u0 {6,S} {16,D} {17,S}
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
    index = 45,
    label = "1_OH_2_formyl_3_formyl_4_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   Cd u0 {4,S} {18,D} {19,S}
11   R u0 {5,S}
12   Cd u0 {6,S} {16,D} {17,S}
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
    label = "1_OH_2_formyl_3_formyl_4_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   Os u0 {4,S} {18,S}
11   R u0 {5,S}
12   Cd u0 {6,S} {16,D} {17,S}
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
    index = 47,
    label = "1_OH_2_formyl_3_Os_4p",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   [CO,Os] u0 {4,S}
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
    index = 48,
    label = "1_OH_2_formyl_3_Os_4_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   Cd u0 {4,S} {17,D} {18,S}
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
    label = "1_OH_2_formyl_3_Os_4_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
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
    index = 50,
    label = "1_OH_2_Os_3_Os_4p",
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
10   [CO,Os] u0 {4,S}
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
    index = 51,
    label = "1_OH_2_Os_3_Os_4_formyl",
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
10   Cd u0 {4,S} {16,D} {17,S}
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
    label = "1_OH_2_Os_3_Os_4_Os",
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
    index = 53,
    label = "1_OH_doublesub_oo",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    [CO,Os] u0 {2,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   [CO,Os] u0 {6,S}
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
    index = 54,
    label = "1_OH_23oo_2_Os_3_Os",
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
    label = "1_OH_23oo_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   R u0 {4,S}
11   R u0 {5,S}
12   Cd u0 {6,S} {16,D} {17,S}
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
    label = "1_OH_23oo_2_formyl_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
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
    index = 57,
    label = "1_OH_doublesub_op",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    [CO,Os] u0 {2,S}
9    R u0 {3,S}
10   [CO,Os] u0 {4,S}
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
    index = 58,
    label = "1_OH_23op_2_formyl_3p",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   [CO,Os] u0 {4,S}
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
    index = 59,
    label = "1_OH_23op_2_formyl_3_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
9    R u0 {3,S}
10   Cd u0 {4,S} {16,D} {17,S}
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
    label = "1_OH_23op_2_formyl_3_Os",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
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
    index = 61,
    label = "1_OH_23op_2_Os_3p",
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
10   [CO,Os] u0 {4,S}
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
    index = 62,
    label = "1_OH_23op_2_Os_3_formyl",
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
10   Cd u0 {4,S} {15,D} {16,S}
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
    label = "1_OH_23op_2_Os_3_Os",
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
    index = 64,
    label = "1_OH_singlesub_ortho",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O u0 {1,S} {13,S}
8    [CO,Os] u0 {2,S}
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
    index = 65,
    label = "1_OH_2_ortho_formyl",
    group = 
"""
1  * Cb u0 {2,B} {6,B} {7,S}
2    Cb u0 {1,B} {3,B} {8,S}
3    Cb u0 {2,B} {4,B} {9,S}
4    Cb u0 {3,B} {5,B} {10,S}
5    Cb u0 {4,B} {6,B} {11,S}
6    Cb u0 {5,B} {1,B} {12,S}
7    O  u0 {1,S} {13,S}
8    Cd u0 {2,S} {14,D} {15,S}
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
    label = "1_OH_2_ortho_Os",
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
    index = 67,
    label = "1_OH_singlesub_para",
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
10   [CO,Os] u0 {4,S}
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
    index = 68,
    label = "1_OH_2_para_formyl",
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
10   Cd u0 {4,S} {14,D} {15,S}
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
    label = "1_OH_2_para_Os",
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
            L4: 1_vinyl_doubleortho
                L5: 1_vinyl_2_formyl_3CsCdOs
                    L6: 1_vinyl_2_formyl_3_formyl
                    L6: 1_vinyl_2_formyl_3_vinyl
                    L6: 1_vinyl_2_formyl_3_Cs
                    L6: 1_vinyl_2_formyl_3_Os
                L5: 1_vinyl_2_vinyl_3CsCdOs
                    L6: 1_vinyl_2_vinyl_3_vinyl
                    L6: 1_vinyl_2_vinyl_3_Cs
                    L6: 1_vinyl_2_vinyl_3_Os
                L5: 1_vinyl_2_Cs_3CsOs
                    L6: 1_vinyl_2_Cs_3_Cs
                    L6: 1_vinyl_2_Cs_3_Os
            L4: 1_vinyl_singleortho
                L5: 1_vinyl_2_formyl
                L5: 1_vinyl_2_vinyl
                L5: 1_vinyl_2_Cs
                L5: 1_vinyl_2_Os
        L3: 1_Cs
            L4: 1_Cs_doubleortho
                L5: 1_Cs_2_formyl_3CsCO
                    L6: 1_Cs_2_formyl_3_formyl
                    L6: 1_Cs_2_formyl_3_Cs
                L5: 1_Cs_2_Cs_3_Cs
            L4: 1_Cs_singleortho
                L5: 1_Cs_2_formyl
                L5: 1_Cs_2_Cs
        L3: 1_OH
            L4: 1_OH_triplesub_oop
                L5: 1_OH_2_formyl_3_formyl_4p
                    L6: 1_OH_2_formyl_3_formyl_4_formyl
                    L6: 1_OH_2_formyl_3_formyl_4_Os
                L5: 1_OH_2_formyl_3_Os_4p
                    L6: 1_OH_2_formyl_3_Os_4_formyl
                    L6: 1_OH_2_formyl_3_Os_4_Os
                L5: 1_OH_2_Os_3_Os_4p
                    L6: 1_OH_2_Os_3_Os_4_formyl
                    L6: 1_OH_2_Os_3_Os_4_Os
            L4: 1_OH_doublesub_oo
                L5: 1_OH_23oo_2_formyl_3_formyl
                L5: 1_OH_23oo_2_formyl_3_Os
                L5: 1_OH_23oo_2_Os_3_Os
            L4: 1_OH_doublesub_op
                L5: 1_OH_23op_2_formyl_3p
                    L6: 1_OH_23op_2_formyl_3_formyl
                    L6: 1_OH_23op_2_formyl_3_Os
                L5: 1_OH_23op_2_Os_3p
                    L6: 1_OH_23op_2_Os_3_formyl
                    L6: 1_OH_23op_2_Os_3_Os
            L4: 1_OH_singlesub_ortho
                L5: 1_OH_2_ortho_formyl
                L5: 1_OH_2_ortho_Os
            L4: 1_OH_singlesub_para
                L5: 1_OH_2_para_formyl
                L5: 1_OH_2_para_Os
"""
)

