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
        Cpdata = ([1.10, 0.76, 0.50, 0.31, 0.05, -0.05, -0.12],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.55,'cal/(mol*K)'),
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
        Cpdata = ([1.15, 1.03, 0.87, 0.75, 0.53, 0.41, 0.23],'cal/(mol*K)'),
        H298 = (1.59,'kcal/mol'),
        S298 = (-1.06,'cal/(mol*K)'),
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
        Cpdata = ([0.62, 0.76, 1.00, 1.20, 1.15, 0.86, 0.14],'cal/(mol*K)'),
        H298 = (5.69,'kcal/mol'),
        S298 = (-1.24,'cal/(mol*K)'),
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
        Cpdata = ([0.86, 0.76, 0.75, 0.75, 0.60, 0.41, 0.01],'cal/(mol*K)'),
        H298 = (3.81,'kcal/mol'),
        S298 = (-0.90,'cal/(mol*K)'),
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
        Cpdata = ([1.67, 1.72, 1.67, 1.60, 1.27, 0.93, 0.31],'cal/(mol*K)'),
        H298 = (3.94,'kcal/mol'),
        S298 = (-1.98,'cal/(mol*K)'),
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
        Cpdata = ([0.91, 1.03, 1.12, 1.20, 1.08, 0.86, 0.36],'cal/(mol*K)'),
        H298 = (3.47,'kcal/mol'),
        S298 = (-1.41,'cal/(mol*K)'),
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
        Cpdata = ([1.91, 1.72, 1.42, 1.16, 0.72, 0.48, 0.18],'cal/(mol*K)'),
        H298 = (2.07,'kcal/mol'),
        S298 = (-1.64,'cal/(mol*K)'),
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
        Cpdata = ([2.72, 2.68, 2.34, 2.01, 1.39, 1.00, 0.48],'cal/(mol*K)'),
        H298 = (2.20,'kcal/mol'),
        S298 = (-2.72,'cal/(mol*K)'),
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
        Cpdata = ([1.96, 1.98, 1.79, 1.60, 1.20, 0.93, 0.53],'cal/(mol*K)'),
        H298 = (1.72,'kcal/mol'),
        S298 = (-2.15,'cal/(mol*K)'),
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
        Cpdata = ([0.31, 0.38, 0.50, 0.60, 0.57, 0.43, 0.07],'cal/(mol*K)'),
        H298 = (2.84,'kcal/mol'),
        S298 = (-0.62,'cal/(mol*K)'),
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
        Cpdata = ([0.55, 0.38, 0.25, 0.16, 0.02, -0.02, -0.06],'cal/(mol*K)'),
        H298 = (0.97,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
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
        Cpdata = ([1.36, 1.34, 1.17, 1.00, 0.69, 0.50, 0.24],'cal/(mol*K)'),
        H298 = (1.10,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
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
        Cpdata = ([0.60, 0.65, 0.62, 0.60, 0.50, 0.43, 0.29],'cal/(mol*K)'),
        H298 = (0.62,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
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
        Cpdata = ([1.91, 1.43, 0.96, 0.53, 0.00, -0.29, -0.43],'cal/(mol*K)'),
        H298 = (3.87,'kcal/mol'),
        S298 = (-1.15,'cal/(mol*K)'),
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
        Cpdata = ([1.35, 1.06, 0.79, 0.56, 0.27, 0.10, -0.04],'cal/(mol*K)'),
        H298 = (2.44,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
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
        Cpdata = ([0.79, 0.69, 0.62, 0.60, 0.55, 0.48, 0.36],'cal/(mol*K)'),
        H298 = (1.00,'kcal/mol'),
        S298 = (-1.58,'cal/(mol*K)'),
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
        Cpdata = ([0.96, 0.72, 0.48, 0.26, 0.00, -0.14, -0.22],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.57,'cal/(mol*K)'),
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
        Cpdata = ([0.39, 0.35, 0.31, 0.30, 0.27, 0.24, 0.18],'cal/(mol*K)'),
        H298 = (0.50,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
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
        Cpdata = ([-5.35, -4.54, -3.61, -2.82, -1.41, -0.38, 1.22],'cal/(mol*K)'),
        H298 = (-14.20,'kcal/mol'),
        S298 = (-10.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "1_OH_oop_2_formyl_3_formyl_4_methoxy",
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
10   O u0 {4,S} {18,S}
11   R u0 {5,S}
12   C u0 {6,S} {16,D} {17,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   O u0 {12,D}
17   H u0 {12,S}
18   C u0 {10,S} {19,S} {20,S} {21,S}
19   H u0 {18,S}
20   H u0 {18,S}
21   H u0 {18,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.57, -4.21, -3.73, -3.27, -2.17, -1.22, 0.45],'cal/(mol*K)'),
        H298 = (-11.35,'kcal/mol'),
        S298 = (-9.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "1_OH_oop_2_formyl_3_formyl_4_OH",
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
10   O u0 {4,S} {18,S}
11   R u0 {5,S}
12   C u0 {6,S} {16,D} {17,S}
13   H u0 {7,S}
14   O u0 {8,D}
15   H u0 {8,S}
16   O u0 {12,D}
17   H u0 {12,S}
18   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.77, -4.25, -3.63, -3.07, -1.90, -0.94, 0.66],'cal/(mol*K)'),
        H298 = (-12.23,'kcal/mol'),
        S298 = (-9.70,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "1_OH_oop_2_formyl_3_methoxy_4_formyl",
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
16   C u0 {12,S} {19,S} {20,S} {21,S}
17   O u0 {10,D}
18   H u0 {10,S}
19   H u0 {16,S}
20   H u0 {16,S}
21   H u0 {16,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.51, -2.75, -1.79, -0.91, 0.41, 1.10, 1.67],'cal/(mol*K)'),
        H298 = (-8.37,'kcal/mol'),
        S298 = (-6.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "1_OH_oop_2_formyl_3_OH_4_formyl",
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
16   H u0 {12,S}
17   O u0 {10,D}
18   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.19, -2.57, -1.82, -1.15, -0.10, 0.53, 1.23],'cal/(mol*K)'),
        H298 = (-8.01,'kcal/mol'),
        S298 = (-5.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "1_OH_oop_2_formyl_3_OH_4_OH",
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
16   H u0 {12,S}
17   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.61, -2.28, -1.84, -1.40, -0.59, -0.04, 0.67],'cal/(mol*K)'),
        H298 = (-6.03,'kcal/mol'),
        S298 = (-5.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "1_OH_oop_2_formyl_3_OH_4_methoxy",
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
16   H u0 {12,S}
17   C u0 {10,S} {18,S} {19,S} {20,S}
18   H u0 {17,S}
19   H u0 {17,S}
20   H u0 {17,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.40, -2.23, -1.94, -1.60, -0.86, -0.31, 0.47],'cal/(mol*K)'),
        H298 = (-5.16,'kcal/mol'),
        S298 = (-4.80,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "1_OH_oop_2_formyl_3_methoxy_4_OH",
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
16   C u0 {12,S} {18,S} {19,S} {20,S}
17   H u0 {10,S}
18   H u0 {16,S}
19   H u0 {16,S}
20   H u0 {16,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.93, -2.46, -1.82, -1.16, -0.08, 0.54, 1.11],'cal/(mol*K)'),
        H298 = (-6.39,'kcal/mol'),
        S298 = (-5.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "1_OH_oop_2_formyl_3_methoxy_4_methoxy",
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
16   C u0 {12,S} {18,S} {19,S} {20,S}
17   C u0 {10,S} {21,S} {22,S} {23,S}
18   H u0 {16,S}
19   H u0 {16,S}
20   H u0 {16,S}
21   H u0 {17,S}
22   H u0 {17,S}
23   H u0 {17,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.72, -2.41, -1.91, -1.36, -0.36, 0.26, 0.91],'cal/(mol*K)'),
        H298 = (-5.52,'kcal/mol'),
        S298 = (-5.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "1_OH_oop_2_OH_3_OH_4_formyl",
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
14   H u0 {8,S}
15   H u0 {12,S}
16   O u0 {10,D}
17   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03, -0.60, -0.02, 0.53, 1.22, 1.43, 1.24],'cal/(mol*K)'),
        H298 = (-1.82,'kcal/mol'),
        S298 = (-1.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "1_OH_oop_2_OH_3_methoxy_4_formyl",
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
14   H u0 {8,S}
15   C u0 {12,S} {18,S} {19,S} {20,S}
16   O u0 {10,D}
17   H u0 {10,S}
18   H u0 {15,S}
19   H u0 {15,S}
20   H u0 {15,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35, -0.78, 0.00, 0.76, 1.72, 2.01, 1.68],'cal/(mol*K)'),
        H298 = (-2.17,'kcal/mol'),
        S298 = (-2.20,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "1_OH_oop_2_methoxy_3_methoxy_4_formyl",
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
14   C u0 {8,S} {18,S} {19,S} {20,S}
15   C u0 {12,S} {21,S} {22,S} {23,S}
16   O u0 {10,D}
17   H u0 {10,S}
18   H u0 {14,S}
19   H u0 {14,S}
20   H u0 {14,S}
21   H u0 {15,S}
22   H u0 {15,S}
23   H u0 {15,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.67, -0.96, 0.02, 1.00, 2.22, 2.58, 2.13],'cal/(mol*K)'),
        H298 = (-2.53,'kcal/mol'),
        S298 = (-2.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "1_OH_oop_2_OH_3_OH_4_OH",
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
14   H u0 {8,S}
15   H u0 {12,S}
16   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.44, -0.31, -0.05, 0.27, 0.73, 0.87, 0.68],'cal/(mol*K)'),
        H298 = (0.16,'kcal/mol'),
        S298 = (-0.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "1_OH_oop_2_OH_3_OH_4_methoxy",
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
14   H u0 {8,S}
15   H u0 {12,S}
16   C u0 {10,S} {17,S} {18,S} {19,S}
17   H u0 {16,S}
18   H u0 {16,S}
19   H u0 {16,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.24, -0.26, -0.14, 0.07, 0.45, 0.60, 0.48],'cal/(mol*K)'),
        H298 = (1.03,'kcal/mol'),
        S298 = (-0.38,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "1_OH_oop_2_OH_3_methoxy_4_OH",
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
14   H u0 {8,S}
15   C u0 {12,S} {17,S} {18,S} {19,S}
16   H u0 {10,S}
17   H u0 {15,S}
18   H u0 {15,S}
19   H u0 {15,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.76, -0.49, -0.02, 0.51, 1.23, 1.45, 1.12],'cal/(mol*K)'),
        H298 = (-0.20,'kcal/mol'),
        S298 = (-1.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "1_OH_oop_2_OH_3_methoxy_4_methoxy",
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
14   H u0 {8,S}
15   C u0 {12,S} {17,S} {18,S} {19,S}
16   C u0 {10,S} {20,S} {21,S} {22,S}
17   H u0 {15,S}
18   H u0 {15,S}
19   H u0 {15,S}
20   H u0 {16,S}
21   H u0 {16,S}
22   H u0 {16,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.56, -0.44, -0.12, 0.31, 0.96, 1.17, 0.92],'cal/(mol*K)'),
        H298 = (0.67,'kcal/mol'),
        S298 = (-1.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "1_OH_oop_2_methoxy_3_methoxy_4_OH",
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
14   C u0 {8,S} {20,S} {21,S} {22,S}
15   C u0 {12,S} {17,S} {18,S} {19,S}
16   H u0 {10,S}
17   H u0 {15,S}
18   H u0 {15,S}
19   H u0 {15,S}
20   H u0 {14,S}
21   H u0 {14,S}
22   H u0 {14,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09, -0.67, 0.00, 0.75, 1.73, 2.02, 1.57],'cal/(mol*K)'),
        H298 = (-0.56,'kcal/mol'),
        S298 = (-2.20,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "1_OH_oop_2_methoxy_3_methoxy_4_methoxy",
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
14   C u0 {8,S} {20,S} {21,S} {22,S}
15   C u0 {12,S} {17,S} {18,S} {19,S}
16   C u0 {10,S} {23,S} {24,S} {25,S}
17   H u0 {15,S}
18   H u0 {15,S}
19   H u0 {15,S}
20   H u0 {14,S}
21   H u0 {14,S}
22   H u0 {14,S}
23   H u0 {16,S}
24   H u0 {16,S}
25   H u0 {16,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.88, -0.62, -0.10, 0.55, 1.46, 1.74, 1.36],'cal/(mol*K)'),
        H298 = (0.31,'kcal/mol'),
        S298 = (-1.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "1_OH_oo_2_OH_3_OH",
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
14   H u0 {8,S}
15   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65, -0.36, 0.05, 0.48, 1.00, 1.15, 0.88],'cal/(mol*K)'),
        H298 = (-0.72,'kcal/mol'),
        S298 = (-1.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "1_OH_oo_2_OH_3_methoxy",
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
14   H u0 {8,S}
15   C u0 {12,S} {16,S} {17,S} {18,S}
16   H u0 {15,S}
17   H u0 {15,S}
18   H u0 {15,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.97, -0.54, 0.07, 0.72, 1.51, 1.72, 1.33],'cal/(mol*K)'),
        H298 = (-1.08,'kcal/mol'),
        S298 = (-2.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "1_OH_oo_2_methoxy_3_methoxy",
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
14   C u0 {8,S} {19,S} {20,S} {21,S}
15   C u0 {12,S} {16,S} {17,S} {18,S}
16   H u0 {15,S}
17   H u0 {15,S}
18   H u0 {15,S}
19   H u0 {14,S}
20   H u0 {14,S}
21   H u0 {14,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.29, -0.72, 0.10, 0.96, 2.01, 2.29, 1.77],'cal/(mol*K)'),
        H298 = (-1.43,'kcal/mol'),
        S298 = (-2.68,'cal/(mol*K)'),
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
        Cpdata = ([-4.97, -4.30, -3.54, -2.87, -1.63, -0.67, 0.86],'cal/(mol*K)'),
        H298 = (-13.10,'kcal/mol'),
        S298 = (-10.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "1_OH_oo_2_formyl_3_OH",
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
16   H u0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.81, -2.33, -1.74, -1.20, -0.31, 0.24, 0.87],'cal/(mol*K)'),
        H298 = (-6.91,'kcal/mol'),
        S298 = (-5.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "1_OH_oo_2_formyl_3_methoxy",
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
16   C u0 {12,S} {17,S} {18,S} {19,S}
17   H u0 {16,S}
18   H u0 {16,S}
19   H u0 {16,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.13, -2.51, -1.72, -0.96, 0.19, 0.81, 1.31],'cal/(mol*K)'),
        H298 = (-7.27,'kcal/mol'),
        S298 = (-6.43,'cal/(mol*K)'),
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
        Cpdata = ([-2.87, -2.39, -1.84, -1.39, -0.60, -0.05, 0.79],'cal/(mol*K)'),
        H298 = (-7.65,'kcal/mol'),
        S298 = (-5.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "1_OH_op_2_formyl_3_OH",
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
16   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.28, -2.10, -1.86, -1.64, -1.09, -0.61, 0.23],'cal/(mol*K)'),
        H298 = (-5.68,'kcal/mol'),
        S298 = (-4.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "1_OH_op_2_formyl_3_methoxy",
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
16   C u0 {10,S} {17,S} {18,S} {19,S}
17   H u0 {16,S}
18   H u0 {16,S}
19   H u0 {16,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.08, -2.06, -1.96, -1.84, -1.36, -0.88, 0.02],'cal/(mol*K)'),
        H298 = (-4.80,'kcal/mol'),
        S298 = (-4.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "1_OH_op_2_OH_3_formyl",
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
14   H u0 {8,S}
15   O u0 {10,D}
16   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.71, -0.42, -0.05, 0.29, 0.72, 0.86, 0.80],'cal/(mol*K)'),
        H298 = (-1.46,'kcal/mol'),
        S298 = (-0.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "1_OH_op_2_methoxy_3_formyl",
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
14   C u0 {8,S} {17,S} {18,S} {19,S}
15   O u0 {10,D}
16   H u0 {10,S}
17   H u0 {14,S}
18   H u0 {14,S}
19   H u0 {14,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03, -0.60, -0.02, 0.53, 1.22, 1.43, 1.24],'cal/(mol*K)'),
        H298 = (-1.82,'kcal/mol'),
        S298 = (-1.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "1_OH_op_2_OH_3_OH",
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
14   H u0 {8,S}
15   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.12, -0.13, -0.07, 0.04, 0.23, 0.30, 0.24],'cal/(mol*K)'),
        H298 = (0.51,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "1_OH_op_2_OH_3_methoxy",
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
14   H u0 {8,S}
15   C u0 {10,S} {16,S} {17,S} {18,S}
16   H u0 {15,S}
17   H u0 {15,S}
18   H u0 {15,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.08, -0.08, -0.17, -0.17, -0.05, 0.02, 0.04],'cal/(mol*K)'),
        H298 = (1.39,'kcal/mol'),
        S298 = (0.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "1_OH_op_2_methoxy_3_OH",
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
14   C u0 {8,S} {16,S} {17,S} {18,S}
15   H u0 {10,S}
16   H u0 {14,S}
17   H u0 {14,S}
18   H u0 {14,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.44, -0.31, -0.05, 0.27, 0.73, 0.87, 0.68],'cal/(mol*K)'),
        H298 = (0.16,'kcal/mol'),
        S298 = (-0.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "1_OH_op_2_methoxy_3_methoxy",
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
14   C u0 {8,S} {16,S} {17,S} {18,S}
15   C u0 {10,S} {19,S} {20,S} {21,S}
16   H u0 {14,S}
17   H u0 {14,S}
18   H u0 {14,S}
19   H u0 {15,S}
20   H u0 {15,S}
21   H u0 {15,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.24, -0.26, -0.14, 0.07, 0.45, 0.60, 0.48],'cal/(mol*K)'),
        H298 = (1.03,'kcal/mol'),
        S298 = (-0.38,'cal/(mol*K)'),
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
        Cpdata = ([-2.49, -2.15, -1.77, -1.43, -0.81, -0.33, 0.43],'cal/(mol*K)'),
        H298 = (-6.55,'kcal/mol'),
        S298 = (-5.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "1_OH_o_2_OH",
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
14   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32, -0.18, 0.02, 0.24, 0.50, 0.57, 0.44],'cal/(mol*K)'),
        H298 = (-0.36,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "1_OH_o_2_methoxy",
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
14   C u0 {8,S} {15,S} {16,S} {17,S}
15   H u0 {14,S}
16   H u0 {14,S}
17   H u0 {14,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65, -0.36, 0.05, 0.48, 1.00, 1.15, 0.88],'cal/(mol*K)'),
        H298 = (-0.72,'kcal/mol'),
        S298 = (-1.34,'cal/(mol*K)'),
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
        Cpdata = ([-0.38, -0.24, -0.07, 0.05, 0.22, 0.29, 0.36],'cal/(mol*K)'),
        H298 = (-1.10,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "1_OH_p_2_OH",
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
14   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.05, -0.10, -0.20, -0.27, -0.27, -0.20],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NNI from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "1_OH_p_2_methoxy",
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
14   C u0 {10,S} {15,S} {16,S} {17,S}
15   H u0 {14,S}
16   H u0 {14,S}
17   H u0 {14,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.41, 0.10, -0.19, -0.41, -0.55, -0.55, -0.41],'cal/(mol*K)'),
        H298 = (1.74,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
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
        Cpdata = ([0.20, -0.76, -1.22, -1.40, -1.33, -1.16, -0.73],'cal/(mol*K)'),
        H298 = (4.39,'kcal/mol'),
        S298 = (2.34,'cal/(mol*K)'),
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
        Cpdata = ([-0.38, -1.05, -1.20, -1.15, -0.84, -0.60, -0.17],'cal/(mol*K)'),
        H298 = (2.41,'kcal/mol'),
        S298 = (1.67,'cal/(mol*K)'),
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
        Cpdata = ([-0.42, -0.29, -0.04, 0.13, 0.18, 0.07, -0.16],'cal/(mol*K)'),
        H298 = (4.52,'kcal/mol'),
        S298 = (1.00,'cal/(mol*K)'),
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
        Cpdata = ([-1.00, -0.57, -0.01, 0.38, 0.67, 0.63, 0.41],'cal/(mol*K)'),
        H298 = (2.55,'kcal/mol'),
        S298 = (0.33,'cal/(mol*K)'),
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
        Cpdata = ([-1.04, 0.19, 1.15, 1.66, 1.68, 1.30, 0.42],'cal/(mol*K)'),
        H298 = (4.65,'kcal/mol'),
        S298 = (-0.33,'cal/(mol*K)'),
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
        Cpdata = ([-1.63, -0.10, 1.17, 1.91, 2.17, 1.86, 0.98],'cal/(mol*K)'),
        H298 = (2.68,'kcal/mol'),
        S298 = (-1.00,'cal/(mol*K)'),
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
        Cpdata = ([0.00, -0.81, -1.12, -1.20, -1.05, -0.88, -0.53],'cal/(mol*K)'),
        H298 = (3.51,'kcal/mol'),
        S298 = (1.86,'cal/(mol*K)'),
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
        Cpdata = ([-0.62, -0.33, 0.06, 0.33, 0.45, 0.35, 0.05],'cal/(mol*K)'),
        H298 = (3.64,'kcal/mol'),
        S298 = (0.53,'cal/(mol*K)'),
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
        Cpdata = ([-1.24, 0.14, 1.24, 1.86, 1.96, 1.58, 0.62],'cal/(mol*K)'),
        H298 = (3.78,'kcal/mol'),
        S298 = (-0.81,'cal/(mol*K)'),
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
        Cpdata = ([0.20, -0.36, -0.66, -0.80, -0.80, -0.72, -0.47],'cal/(mol*K)'),
        H298 = (2.63,'kcal/mol'),
        S298 = (1.41,'cal/(mol*K)'),
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
        Cpdata = ([-0.38, -0.65, -0.63, -0.55, -0.31, -0.16, 0.10],'cal/(mol*K)'),
        H298 = (0.66,'kcal/mol'),
        S298 = (0.74,'cal/(mol*K)'),
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
        Cpdata = ([-0.42, 0.12, 0.53, 0.73, 0.71, 0.51, 0.11],'cal/(mol*K)'),
        H298 = (2.76,'kcal/mol'),
        S298 = (0.07,'cal/(mol*K)'),
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
        Cpdata = ([-1.00, -0.17, 0.55, 0.98, 1.20, 1.08, 0.67],'cal/(mol*K)'),
        H298 = (0.79,'kcal/mol'),
        S298 = (-0.60,'cal/(mol*K)'),
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
        Cpdata = ([0.00, -0.41, -0.56, -0.60, -0.53, -0.44, -0.26],'cal/(mol*K)'),
        H298 = (1.76,'kcal/mol'),
        S298 = (0.93,'cal/(mol*K)'),
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
        Cpdata = ([-0.62, 0.07, 0.62, 0.93, 0.98, 0.79, 0.31],'cal/(mol*K)'),
        H298 = (1.89,'kcal/mol'),
        S298 = (-0.41,'cal/(mol*K)'),
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
        Cpdata = ([0.20, 0.05, -0.10, -0.20, -0.27, -0.27, -0.20],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
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
        Cpdata = ([-0.38, -0.24, -0.07, 0.05, 0.22, 0.29, 0.36],'cal/(mol*K)'),
        H298 = (-1.10,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
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
        Cpdata = ([1.03, 0.81, 0.62, 0.44, 0.01, -0.39, -0.90],'cal/(mol*K)'),
        H298 = (7.37,'kcal/mol'),
        S298 = (1.46,'cal/(mol*K)'),
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
        Cpdata = ([0.81, 0.65, 0.50, 0.36, 0.00, -0.36, -0.79],'cal/(mol*K)'),
        H298 = (6.19,'kcal/mol'),
        S298 = (1.55,'cal/(mol*K)'),
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
        Cpdata = ([0.82, 0.69, 0.56, 0.43, 0.06, -0.31, -0.80],'cal/(mol*K)'),
        H298 = (6.80,'kcal/mol'),
        S298 = (1.45,'cal/(mol*K)'),
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
        Cpdata = ([0.82, 0.61, 0.43, 0.27, -0.04, -0.30, -0.60],'cal/(mol*K)'),
        H298 = (4.85,'kcal/mol'),
        S298 = (0.69,'cal/(mol*K)'),
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
        Cpdata = ([0.61, 0.53, 0.44, 0.35, 0.05, -0.27, -0.69],'cal/(mol*K)'),
        H298 = (5.62,'kcal/mol'),
        S298 = (1.54,'cal/(mol*K)'),
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
        Cpdata = ([0.62, 0.57, 0.50, 0.42, 0.11, -0.23, -0.71],'cal/(mol*K)'),
        H298 = (6.23,'kcal/mol'),
        S298 = (1.43,'cal/(mol*K)'),
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
        Cpdata = ([0.61, 0.44, 0.31, 0.19, -0.05, -0.26, -0.49],'cal/(mol*K)'),
        H298 = (3.67,'kcal/mol'),
        S298 = (0.79,'cal/(mol*K)'),
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
        Cpdata = ([0.62, 0.49, 0.37, 0.26, 0.01, -0.22, -0.50],'cal/(mol*K)'),
        H298 = (4.28,'kcal/mol'),
        S298 = (0.68,'cal/(mol*K)'),
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
        Cpdata = ([0.62, 0.49, 0.37, 0.26, 0.01, -0.22, -0.50],'cal/(mol*K)'),
        H298 = (4.28,'kcal/mol'),
        S298 = (0.68,'cal/(mol*K)'),
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
        Cpdata = ([0.62, 0.41, 0.24, 0.11, -0.08, -0.20, -0.30],'cal/(mol*K)'),
        H298 = (2.33,'kcal/mol'),
        S298 = (-0.07,'cal/(mol*K)'),
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
        Cpdata = ([0.41, 0.41, 0.38, 0.33, 0.10, -0.19, -0.60],'cal/(mol*K)'),
        H298 = (5.04,'kcal/mol'),
        S298 = (1.53,'cal/(mol*K)'),
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
        Cpdata = ([0.41, 0.32, 0.25, 0.18, 0.00, -0.18, -0.39],'cal/(mol*K)'),
        H298 = (3.10,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
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
        Cpdata = ([0.41, 0.32, 0.25, 0.18, 0.00, -0.18, -0.39],'cal/(mol*K)'),
        H298 = (3.10,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
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
        Cpdata = ([0.42, 0.37, 0.31, 0.25, 0.06, -0.13, -0.41],'cal/(mol*K)'),
        H298 = (3.70,'kcal/mol'),
        S298 = (0.67,'cal/(mol*K)'),
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
        Cpdata = ([0.41, 0.24, 0.12, 0.02, -0.10, -0.17, -0.19],'cal/(mol*K)'),
        H298 = (1.15,'kcal/mol'),
        S298 = (0.02,'cal/(mol*K)'),
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
        Cpdata = ([0.42, 0.29, 0.18, 0.10, -0.04, -0.12, -0.20],'cal/(mol*K)'),
        H298 = (1.76,'kcal/mol'),
        S298 = (-0.08,'cal/(mol*K)'),
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
        Cpdata = ([0.20, 0.20, 0.19, 0.17, 0.05, -0.10, -0.30],'cal/(mol*K)'),
        H298 = (2.52,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
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
        Cpdata = ([0.20, 0.12, 0.06, 0.01, -0.05, -0.08, -0.10],'cal/(mol*K)'),
        H298 = (0.57,'kcal/mol'),
        S298 = (0.01,'cal/(mol*K)'),
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
        Cpdata = ([0.22, 0.17, 0.12, 0.08, 0.01, -0.04, -0.11],'cal/(mol*K)'),
        H298 = (1.18,'kcal/mol'),
        S298 = (-0.10,'cal/(mol*K)'),
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
            L4: 1_OH_oop_2_formyl_3_formyl_4_methoxy
            L4: 1_OH_oop_2_formyl_3_formyl_4_OH
            L4: 1_OH_oop_2_formyl_3_methoxy_4_formyl
            L4: 1_OH_oop_2_formyl_3_OH_4_formyl
            L4: 1_OH_oop_2_formyl_3_methoxy_4_methoxy
            L4: 1_OH_oop_2_formyl_3_methoxy_4_OH
            L4: 1_OH_oop_2_formyl_3_OH_4_methoxy
            L4: 1_OH_oop_2_formyl_3_OH_4_OH
            L4: 1_OH_oop_2_OH_3_OH_4_formyl
            L4: 1_OH_oop_2_OH_3_methoxy_4_formyl
            L4: 1_OH_oop_2_methoxy_3_methoxy_4_formyl
            L4: 1_OH_oop_2_OH_3_OH_4_OH
            L4: 1_OH_oop_2_OH_3_OH_4_methoxy
            L4: 1_OH_oop_2_OH_3_methoxy_4_OH
            L4: 1_OH_oop_2_OH_3_methoxy_4_methoxy
            L4: 1_OH_oop_2_methoxy_3_methoxy_4_OH
            L4: 1_OH_oop_2_methoxy_3_methoxy_4_methoxy
            L4: 1_OH_oo_2_formyl_3_formyl
            L4: 1_OH_oo_2_formyl_3_OH
            L4: 1_OH_oo_2_formyl_3_methoxy
            L4: 1_OH_oo_2_OH_3_OH
            L4: 1_OH_oo_2_OH_3_methoxy
            L4: 1_OH_oo_2_methoxy_3_methoxy
            L4: 1_OH_op_2_formyl_3_formyl
            L4: 1_OH_op_2_formyl_3_OH
            L4: 1_OH_op_2_formyl_3_methoxy
            L4: 1_OH_op_2_OH_3_formyl
            L4: 1_OH_op_2_methoxy_3_formyl
            L4: 1_OH_op_2_OH_3_OH
            L4: 1_OH_op_2_OH_3_methoxy
            L4: 1_OH_op_2_methoxy_3_OH
            L4: 1_OH_op_2_methoxy_3_methoxy
            L4: 1_OH_o_2_formyl
            L4: 1_OH_o_2_OH
            L4: 1_OH_o_2_methoxy
            L4: 1_OH_p_2_formyl
            L4: 1_OH_p_2_OH
            L4: 1_OH_p_2_methoxy
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

