#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_ExoTetcyclic/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 800,
    label = "R1_rad_R2_R3;multiplebond_intra;radadd_intra",
    group1 = "OR{R4, R5, R6, R7}",
    group2 = 
"""
1 *2 {C,O} 0 {2,S}
2 *3 {C,O} 0 {1,S}
""",
    group3 = 
"""
1 *1 R!H 1
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""
The kinetics for head nodes of this family have been copied from "Cyclic_Ether_Formation" family,
"Cyclic_Ether_Formation" is a special case of "Intra_R_Add_ExoTetcyclic" family, to make this reaction family possible.
Seems even kinetics of "Cyclic_Ether_Formation" are just an initial guess.
More accurate rate parameters should be estimated for both reaction families. 
""",
)

