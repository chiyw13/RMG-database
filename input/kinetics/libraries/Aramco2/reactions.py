#!/usr/bin/env python
# encoding: utf-8

name = "Aramco2"
shortDesc = u"Aramco 2.0"
longDesc = u"""
Developed by NUI Galway. 
Released date: February 2016
http://www.nuigalway.ie/c3/aramco2/frontmatter.html

Reference paper:
Y. Li, C-W. Zhou, K.P. Somers, K. Zhang, H.J. Curran 
The Oxidation of 2-Butene: A High Pressure Ignition Delay, Kinetic Modeling Study and Reactivity Comparison with Isobutene and 1-Butene
Proc. Combust. Inst. (2017) submitted
C-W. Zhou, Y. Li, E. O'Connor, K.P. Somers, S. Thion et al.
A Comprehensive experimental and modeling study of isobutene oxidation
Combust. Flame (2016) accepted
U. Burke, W.K. Metcalfe, S.M. Burke, K.A. Heufer, P. Dagaut, H.J. Curran
A Detailed Chemical Kinetic Modeling, Ignition Delay time and Jet-Stirred Reactor Study of Methanol Oxidation
Combust. Flame (2016) 165 125–136
S.M. Burke, U. Burke, O. Mathieu, I. Osorio et al.
An experimental and modeling study of propene oxidation. Part 2: Ignition delay time and flame speed measurements
Combust. Flame (2015) 162(2) 296–314
S.M. Burke, W.K. Metcalfe, O. Herbinet et al.
An experimental and modeling study of propene oxidation. Part 1: Speciation measurements in jet-stirred and flow reactors
Combust. Flame (2014) 161(11) 2765–2784
W.K. Metcalfe, S.M. Burke, S.S. Ahmed, H.J. Curran
A hierarchical and comparative kinetic modeling study of C1–C2 hydrocarbon and oxygenated fuels
Int. J. Chem. Kinet. (2013) 45(10) 638–675
A. Kéromnès, W.K. Metcalfe, K.A. Heufer et al.
An Experimental and Detailed Chemical Kinetic Modelling Study of Hydrogen and Syngas Mixtures at Elevated Pressures
Combustion and Flame (2013) 160 995–1011

The species in excited state, together with corresponding reactions have been deleted.
The reactions with 4 or more products have also been deleted.
Peng Zhang
Date: Mar. 20, 2016
"""
entry(
    index = 1,
    label = "H2 <=> H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.83, '[C]=O': 1.9},
    ),
)

entry(
    index = 2,
    label = "H2 + O <=> H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(50800, 'cm^3/(mol*s)'), n=2.67, Ea=(6292, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "H2 + OH <=> H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.38e+13, 'cm^3/(mol*s)'), n=0, Ea=(6990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.165e+15, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.83, '[C]=O': 1.9, '[Ar]': 0.83},
    ),
)

entry(
    index = 5,
    label = "O2 + H <=> O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+14, 'cm^3/(mol*s)'), n=0, Ea=(15286, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 0.73, 'O': 3.65, '[Ar]': 0.38},
    ),
)

entry(
    index = 7,
    label = "O + H2O <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+07, 'cm^3/(mol*s)'),
        n = 1.704,
        Ea = (14986.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "O + H <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.75, '[C]=O': 1.5, '[Ar]': 0.75},
    ),
)

entry(
    index = 9,
    label = "H2O2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48749, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.49e+24, 'cm^3/(mol*s)'),
            n = -2.3,
            Ea = (48749, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.43,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'OO': 7.7, 'O=C=O': 1.6, 'O': 7.65, '[H][H]': 3.7, '[He]': 0.65, '[O][O]': 1.2, 'N#N': 1.5, '[C]=O': 2.8},
    ),
)

entry(
    index = 10,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "H2O2 + H <=> H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+10, 'cm^3/(mol*s)'), n=1, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "H2O2 + O <=> OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "H2O2 + OH <=> H2O + HO2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(318, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.59e+13, 'cm^3/(mol*s)'), n=0, Ea=(7269, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 14,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.079e+13, 'cm^3/(mol*s)'), n=0, Ea=(295, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "HO2 + H <=> H2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1402e+10, 'cm^3/(mol*s)'),
        n = 1.0827,
        Ea = (553.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 16,
    label = "HO2 + O <=> OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "OH + HO2 <=> H2O + O2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1092.96, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.5e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (10929.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 18,
    label = "HO2 + HO2 <=> H2O2 + O2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(11040.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.9e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1408.92, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 19,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.65e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.737e+19, 'cm^6/(mol^2*s)'),
            n = -1.23,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.67,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 10, '[H][H]': 1.3, '[He]': 0.64, '[C]=O': 1.9, '[Ar]': 0.5},
    ),
)

entry(
    index = 20,
    label = "CO + O <=> CO2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.362e+10, 'cm^3/(mol*s)'), n=0, Ea=(2384, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.173e+24, 'cm^6/(mol^2*s)'),
            n = -2.79,
            Ea = (4191, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.6, 'O': 12, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 21,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (70150, 'cm^3/(mol*s)'),
                n = 2.053,
                Ea = (-355.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.757e+12, 'cm^3/(mol*s)'),
                n = -0.664,
                Ea = (331.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 22,
    label = "CO + HO2 <=> CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 23,
    label = "CO + O2 <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.119e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "H + CO2 <=> OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "HOCO <=> CO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.003, 0.0296, 0.0987, 0.2961, 0.9869, 2.9607, 9.869, 29.607, 98.69, 296.07, 986.9], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.55e-08, 's^-1'), n=2.93, Ea=(8768, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1770, 's^-1'), n=0.34, Ea=(18076, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.02e+13, 's^-1'), n=-1.87, Ea=(22755, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.68e+18, 's^-1'), n=-3.05, Ea=(24323, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.5e+24, 's^-1'), n=-4.63, Ea=(27067, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.54e+26, 's^-1'), n=-5.12, Ea=(27572, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.12e+28, 's^-1'), n=-5.6, Ea=(28535, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.48e+29, 's^-1'), n=-5.7, Ea=(28899, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.89e+31, 's^-1'), n=-6.19, Ea=(30518, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.74e+33, 's^-1'), n=-6.53, Ea=(32068, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.61e+33, 's^-1'), n=-6.29, Ea=(32231, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.3e+32, 's^-1'), n=-5.96, Ea=(32470, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 26,
    label = "HOCO <=> CO2 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.003, 0.0099, 0.0296, 0.0987, 0.2961, 0.9869, 2.9607, 9.869, 29.607, 98.69, 296.07, 986.9], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.758e+18, 's^-1'), n=-3.817, Ea=(17676, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.225e+20, 's^-1'), n=-4.149, Ea=(19037, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.564e+21, 's^-1'), n=-4.434, Ea=(20325, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.107e+24, 's^-1'), n=-5.189, Ea=(22419, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.144e+29, 's^-1'), n=-6.376, Ea=(25233, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.15e+32, 's^-1'), n=-7.037, Ea=(26662, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.069e+36, 's^-1'), n=-8.107, Ea=(29064, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.438e+36, 's^-1'), n=-8.153, Ea=(29336, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.663e+35, 's^-1'), n=-7.919, Ea=(29217, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.723e+38, 's^-1'), n=-8.506, Ea=(31273, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.007e+41, 's^-1'), n=-9.29, Ea=(33966, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.767e+36, 's^-1'), n=-7.832, Ea=(31613, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.897e+38, 's^-1'), n=-8.047, Ea=(34240, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 27,
    label = "CH3 + H <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.27e+16, 'cm^3/(mol*s)'),
            n = -0.63,
            Ea = (383, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.477e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (2440, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 28,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(614000, 'cm^3/(mol*s)'), n=2.5, Ea=(9587, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 30,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(58300, 'cm^3/(mol*s)'), n=2.6, Ea=(2190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11.3, 'cm^3/(mol*s)'), n=3.74, Ea=(21010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "CH4 + CH3O2 <=> CH3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.96, 'cm^3/(mol*s)'), n=3.77, Ea=(17810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "CH3 + HO2 <=> CH4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (116000, 'cm^3/(mol*s)'),
        n = 2.23,
        Ea = (-3022, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 34,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(8270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "CH2(S) + N2 <=> CH2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "CH2(S) + AR <=> CH2 + AR",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "CH2(S) + H2O <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "CH2(S) + CO <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "CH2(S) + CO2 <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "CH2(S) + O2 => H + OH + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "CH2(S) + O2 <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "CH2(S) + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "CH2(S) + O <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "CH2(S) + H2 <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 45,
    label = "CH2(S) + H <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "CH2(S) + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "CH2(S) + CO2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "CH2 + H <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.2e+27, 'cm^6/(mol^2*s)'),
            n = -3.14,
            Ea = (1230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.68,
        T3 = (78, 'K'),
        T1 = (1995, 'K'),
        T2 = (5590, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 49,
    label = "CH2 + O2 <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+13, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "CH2 + O2 => CO2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "CH2 + O => CO + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "CH2 + H <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "CH2 + OH <=> CH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "CH + O2 <=> HCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "CH + O <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "CH + H <=> C + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "CH + OH <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "CH + H2O <=> H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.774e+16, 'cm^3/(mol*s)'),
        n = -1.22,
        Ea = (23.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 59,
    label = "CH + CO2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(685, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "C + OH <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "C + O2 <=> CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 62,
    label = "CH3 + O2 <=> CH3O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.812e+09, 'cm^3/(mol*s)'), n=0.9, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(6.85e+24, 'cm^6/(mol^2*s)'), n=-3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.6,
        T3 = (1000, 'K'),
        T1 = (70, 'K'),
        T2 = (1700, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 63,
    label = "CH3 + O2 <=> CH3O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.546e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28320, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 64,
    label = "CH3 + O2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.641, 'cm^3/(mol*s)'), n=3.283, Ea=(8105, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 65,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.54e+13, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (-136, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 66,
    label = "CH3 + OH <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.936e+14, 'cm^3/(mol*s)'),
                n = -0.669,
                Ea = (-445.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.207e+15, 'cm^3/(mol*s)'),
                n = -0.778,
                Ea = (-175.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.282e+17, 'cm^3/(mol*s)'),
                n = -1.518,
                Ea = (1772, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.788e+23, 'cm^3/(mol*s)'),
                n = -3.155,
                Ea = (7003, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.433e+19, 'cm^3/(mol*s)'),
                n = -1.962,
                Ea = (8244, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 67,
    label = "CH3 + OH <=> CH2O + H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (350200, 'cm^3/(mol*s)'),
                n = 1.441,
                Ea = (-3244, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (885400, 'cm^3/(mol*s)'),
                n = 1.327,
                Ea = (-2975, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.65e+07, 'cm^3/(mol*s)'),
                n = 0.973,
                Ea = (-2010, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.374e+09, 'cm^3/(mol*s)'),
                n = 0.287,
                Ea = (280, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.494e+18, 'cm^3/(mol*s)'),
                n = -2.199,
                Ea = (9769, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 68,
    label = "CH3 + OH <=> CH2OH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.621e+10, 'cm^3/(mol*s)'),
                n = 0.965,
                Ea = (3214, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.807e+10, 'cm^3/(mol*s)'),
                n = 0.95,
                Ea = (3247, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.686e+10, 'cm^3/(mol*s)'),
                n = 0.833,
                Ea = (3566, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.525e+13, 'cm^3/(mol*s)'),
                n = 0.134,
                Ea = (5641, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.59e+14, 'cm^3/(mol*s)'),
                n = -0.186,
                Ea = (8601, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 69,
    label = "CH3 + OH <=> H + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.186e+09, 'cm^3/(mol*s)'),
                n = 1.016,
                Ea = (11940, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.188e+09, 'cm^3/(mol*s)'),
                n = 1.016,
                Ea = (11940, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.23e+09, 'cm^3/(mol*s)'),
                n = 1.011,
                Ea = (11950, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.798e+09, 'cm^3/(mol*s)'),
                n = 0.965,
                Ea = (12060, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.242e+10, 'cm^3/(mol*s)'),
                n = 0.551,
                Ea = (13070, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 70,
    label = "CH3 + OH <=> HCOH + H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.674e+08, 'cm^3/(mol*s)'),
                n = 0.787,
                Ea = (-3046, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.115e+09, 'cm^3/(mol*s)'),
                n = 0.63,
                Ea = (-2669, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.557e+11, 'cm^3/(mol*s)'),
                n = 0.156,
                Ea = (-1368, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.704e+21, 'cm^3/(mol*s)'),
                n = -2.641,
                Ea = (6412, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.25e+20, 'cm^3/(mol*s)'),
                n = -2.402,
                Ea = (9639, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 71,
    label = "CH3 + OH <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42930, 'cm^3/(mol*s)'),
        n = 2.568,
        Ea = (3997.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 72,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0.269,
        Ea = (-687.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 73,
    label = "CH3O2 + O <=> CH3O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 74,
    label = "CH3O2 + H <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 76,
    label = "CH3O2 + HO2 <=> CH3O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.47e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1570, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 77,
    label = "CH3O2 + H2O2 <=> CH3O2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(9936, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 78,
    label = "CH3O2 + CH3 <=> CH3O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.08e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 79,
    label = "CH3O2 + CH3O2 => CH2O + CH3OH + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.11e+14, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (-1051, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 80,
    label = "CH3O2 + CH3O2 => O2 + CH3O + CH3O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 81,
    label = "H2 + CH3O2 <=> H + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 82,
    label = "CH3O2H <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+14, 's^-1'), n=0, Ea=(42300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "CH2O2H <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+14, 's^-1'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 84,
    label = "CH3OH <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.084e+18, 's^-1'), n=-0.615, Ea=(92540.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.5e+43, 'cm^3/(mol*s)'),
            n = -6.995,
            Ea = (97992.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.4748,
        T3 = (35580, 'K'),
        T1 = (1116, 'K'),
        T2 = (9023, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 85,
    label = "CH3OH <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.121e+18, 's^-1'), n=-1.017, Ea=(91712, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.43e+47, 'cm^3/(mol*s)'),
            n = -8.227,
            Ea = (99417.1, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 2.545,
        T3 = (3290, 'K'),
        T1 = (47320, 'K'),
        T2 = (47110, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 86,
    label = "CH3OH <=> CH2OH + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(0.007896, 's^-1'), n=5.038, Ea=(84467.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.39e+42, 'cm^3/(mol*s)'),
            n = -7.244,
            Ea = (105230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -73.91,
        T3 = (37050, 'K'),
        T1 = (41500, 'K'),
        T2 = (5220, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 87,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (199000, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (10300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 88,
    label = "CH3OH + H <=> CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(307000, 'cm^3/(mol*s)'), n=2.55, Ea=(5440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "CH3OH + O <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(38800, 'cm^3/(mol*s)'), n=2.5, Ea=(3080, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(388000, 'cm^3/(mol*s)'), n=2.5, Ea=(3080, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=3.03, Ea=(-763, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "CH3OH + OH <=> CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30800, 'cm^3/(mol*s)'),
        n = 2.65,
        Ea = (-806.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 93,
    label = "CH3OH + O2 <=> CH3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (35800, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (42764.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 94,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (358000, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (42764.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 95,
    label = "CH3OH + HO2 <=> CH3O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.22e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20070.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 96,
    label = "CH3OH + HO2 <=> CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.26e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18782.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 97,
    label = "CH3OH + CH3 <=> CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.213, 'cm^3/(mol*s)'),
        n = 3.953,
        Ea = (7055.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 98,
    label = "CH3OH + CH3 <=> CH3O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3220, 'cm^3/(mol*s)'),
        n = 2.425,
        Ea = (8579.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 99,
    label = "CH3OH + HCO <=> CH2OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9630, 'cm^3/(mol*s)'), n=2.9, Ea=(13110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 100,
    label = "CH3OH + CH3O <=> CH2OH + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(4074, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "CH3OH + CH3O2 <=> CH2OH + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(13710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
    label = "CH2OH + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.51e+15, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.41e+14, 'cm^3/(mol*s)'), n=0, Ea=(5017, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 103,
    label = "CH2OH + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 104,
    label = "CH2OH + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "CH2OH + HCO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "CH2OH + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "CH2OH + CH3O <=> CH2O + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
    label = "CH2OH + OH <=> H2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 109,
    label = "CH2OH + O <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "CH2OH + CH2OH <=> CH2O + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "CH2OH + HO2 <=> HOCH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 112,
    label = "CH3O + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.38e-19, 'cm^3/(mol*s)'),
        n = 9.5,
        Ea = (-5501, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 113,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 114,
    label = "CH3O + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 115,
    label = "CH3O + CH3 <=> CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "CH3O + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 117,
    label = "HCOH + O2 => CO2 + H + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "HCOH + O2 <=> CO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "HCOH + O => CO2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 120,
    label = "HCOH + O => CO + OH + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 121,
    label = "HCOH + H <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 122,
    label = "HCOH + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "HCO + H <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.09e+12, 'cm^3/(mol*s)'),
            n = 0.48,
            Ea = (-260, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.35e+24, 'cm^6/(mol^2*s)'),
            n = -2.57,
            Ea = (1425, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7824,
        T3 = (271, 'K'),
        T1 = (2755, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 124,
    label = "CO + H2 <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.3e+07, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (79600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.07e+27, 'cm^6/(mol^2*s)'),
            n = -3.42,
            Ea = (84348, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 125,
    label = "CH2O + O2 <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.07e+15, 'cm^3/(mol*s)'), n=0, Ea=(53420, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 126,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.26e+09, 'cm^3/(mol*s)'),
        n = 1.15,
        Ea = (2260, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 127,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2740, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 128,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.82e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1055, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 129,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18800, 'cm^3/(mol*s)'), n=2.7, Ea=(11520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 130,
    label = "CH2O + CH3 <=> HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(38.3, 'cm^3/(mol*s)'), n=3.36, Ea=(4312, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 131,
    label = "CH2O + O2CHO <=> HCO + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 132,
    label = "CH2O + OCHO <=> HCO + HOCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 133,
    label = "CH2O + CH3O <=> HCO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(2294, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 134,
    label = "CH2O + CH3O2 <=> HCO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 135,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.7e+11, 'cm^3/(mol*s)'),
            n = 0.66,
            Ea = (14870, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 136,
    label = "HCO + O2 <=> CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(410, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 137,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 138,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 139,
    label = "HCO + OH <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.011e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 140,
    label = "HCO + CH3 <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.65e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 141,
    label = "HCO + HCO <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 143,
    label = "HCO + HO2 => CO2 + H + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "HCO + HCO => H2 + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "CH2O + H <=> CH2OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (3600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.27e+32, 'cm^6/(mol^2*s)'),
            n = -4.82,
            Ea = (6530, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7187,
        T3 = (103, 'K'),
        T1 = (1291, 'K'),
        T2 = (4160, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 146,
    label = "CH3O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.8e+13, 's^-1'), n=0, Ea=(26170, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.867e+25, 'cm^3/(mol*s)'),
            n = -3,
            Ea = (24307, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9,
        T3 = (2500, 'K'),
        T1 = (1300, 'K'),
        T2 = (1e+99, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 147,
    label = "CH2O + OH <=> HOCH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+15, 'cm^3/(mol*s)'), n=-1.1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "HOCH2O <=> HOCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 149,
    label = "CH2O + HO2 <=> OCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 150,
    label = "OCH2O2H <=> HOCH2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 151,
    label = "HOCH2O2 + HO2 <=> HOCH2O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 152,
    label = "HOCH2O + OH <=> HOCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 153,
    label = "HCO + O2 <=> O2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 154,
    label = "HOCHO <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.45e+12, 's^-1'), n=0, Ea=(60470, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 155,
    label = "HOCHO <=> CO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.95e+09, 's^-1'), n=0, Ea=(48520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 156,
    label = "OCHO + HO2 <=> HOCHO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 157,
    label = "OCHO + H2O2 <=> HOCHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 158,
    label = "HOCHO + H => H2 + CO2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.24e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4868, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 159,
    label = "HOCHO + H => H2 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.03e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (2988, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 160,
    label = "HOCHO + O => CO + OH + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.77e+18, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (2975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 161,
    label = "HOCHO + OH => H2O + CO2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.62e+06, 'cm^3/(mol*s)'),
        n = 2.06,
        Ea = (916, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 162,
    label = "HOCHO + OH => H2O + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.85e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 163,
    label = "HOCHO + CH3 => CH4 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.9e-07, 'cm^3/(mol*s)'), n=5.8, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 164,
    label = "HOCHO + HO2 => H2O2 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 165,
    label = "OCHO + OH <=> HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 166,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.277e+15, 'cm^3/(mol*s)'),
            n = -0.69,
            Ea = (174.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (8.054e+31, 'cm^6/(mol^2*s)'),
            n = -3.75,
            Ea = (981.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        T3 = (570, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 167,
    label = "C2H5 + H <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.842,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 168,
    label = "C2H6 + O2 <=> C2H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(51870, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 169,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.55e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5830, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 170,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 171,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.48e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 172,
    label = "C2H6 + HO2 <=> C2H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34.6, 'cm^3/(mol*s)'), n=3.61, Ea=(16920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 173,
    label = "C2H6 + CH <=> C2H5 + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(-260, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 174,
    label = "C2H6 + CH2(S) <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000555, 'cm^3/(mol*s)'),
        n = 4.72,
        Ea = (3231, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 176,
    label = "C2H6 + CH3O <=> C2H5 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+11, 'cm^3/(mol*s)'), n=0, Ea=(7090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 177,
    label = "C2H6 + CH3O2 <=> C2H5 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.4, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 178,
    label = "C2H6 + C2H5O2 <=> C2H5 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 179,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (9.569e+08, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1355, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.419e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.569,
        T3 = (299, 'K'),
        T1 = (-9147, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 180,
    label = "C2H5 + H <=> C2H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 181,
    label = "C2H4 + C2H4 <=> C2H5 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+14, 'cm^3/(mol*s)'), n=0, Ea=(71530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 182,
    label = "C2H5 + CH3 <=> CH4 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11800, 'cm^3/(mol*s)'), n=2.45, Ea=(-2921, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 183,
    label = "C2H5 + O <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 184,
    label = "C2H5 + HO2 <=> C2H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 185,
    label = "C2H5 + CH3O2 <=> C2H5O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 186,
    label = "CH3 + CH3 <=> H + C2H5",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.74e+12, 'cm^3/(mol*s)'),
                n = 0.105,
                Ea = (10664.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.57e+13, 'cm^3/(mol*s)'),
                n = -0.096,
                Ea = (11406.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.1e+14, 'cm^3/(mol*s)'),
                n = -0.362,
                Ea = (13372.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.15e+10, 'cm^3/(mol*s)'),
                n = 0.885,
                Ea = (13532.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (103.2, 'cm^3/(mol*s)'),
                n = 3.23,
                Ea = (11236.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 187,
    label = "C2H5 + O2 <=> C2H5O2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.398e+53, 'cm^3/(mol*s)'),
                n = -13.9,
                Ea = (9279, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.362e+59, 'cm^3/(mol*s)'),
                n = -15.28,
                Ea = (14240, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.262e+60, 'cm^3/(mol*s)'),
                n = -14.91,
                Ea = (16240, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 188,
    label = "C2H5 + O2 <=> C2H4O2H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.103e+34, 'cm^3/(mol*s)'),
                n = -9.01,
                Ea = (5444, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.884e+33, 'cm^3/(mol*s)'),
                n = -8.31,
                Ea = (7710, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.705e+45, 'cm^3/(mol*s)'),
                n = -11.49,
                Ea = (14590, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 189,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.094e+09, 'cm^3/(mol*s)'),
                n = 0.49,
                Ea = (-391.4, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.843e+07, 'cm^3/(mol*s)'),
                n = 1.13,
                Ea = (-720.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.561e+14, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (4749, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 190,
    label = "C2H5 + O2 <=> C2H4O1-2 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1303, 'cm^3/(mol*s)'), n=1.93, Ea=(-502.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(243.8, 'cm^3/(mol*s)'), n=2.18, Ea=(-62.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.621e+09, 'cm^3/(mol*s)'),
                n = 0.15,
                Ea = (5409, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 191,
    label = "C2H5 + O2 <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.908e-06, 'cm^3/(mol*s)'),
                n = 4.76,
                Ea = (254.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.06803, 'cm^3/(mol*s)'),
                n = 3.57,
                Ea = (2643, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(826.5, 'cm^3/(mol*s)'), n=2.41, Ea=(5285, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 192,
    label = "C2H4O2H <=> C2H5O2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.653e-16, 's^-1'), n=6.96, Ea=(2396, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.064e+41, 's^-1'), n=-10.1, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.203e+36, 's^-1'), n=-8.13, Ea=(27020, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 193,
    label = "C2H5O2 <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.237e+35, 's^-1'), n=-9.42, Ea=(36360, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.687e+36, 's^-1'), n=-9.22, Ea=(38700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.52e+41, 's^-1'), n=-10.2, Ea=(43710, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 194,
    label = "C2H5O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.782e+32, 's^-1'), n=-7.1, Ea=(32840, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.701e+37, 's^-1'), n=-8.47, Ea=(35840, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.98e+38, 's^-1'), n=-8.46, Ea=(37900, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 195,
    label = "C2H5O2 <=> C2H4O1-2 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.778e+45, 's^-1'), n=-11.9, Ea=(4112, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.916e+43, 's^-1'), n=-10.75, Ea=(42400, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.965e+43, 's^-1'), n=-10.46, Ea=(45580, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 196,
    label = "C2H4O2H <=> C2H4O1-2 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.959e+38, 's^-1'), n=-9.4, Ea=(20660, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.224e+37, 's^-1'), n=-8.32, Ea=(21460, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.848e+30, 's^-1'), n=-6.08, Ea=(20660, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 197,
    label = "C2H4O2H <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.918e+40, 's^-1'), n=-10.2, Ea=(22250, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.825e+40, 's^-1'), n=-9.61, Ea=(23840, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.98e+34, 's^-1'), n=-7.25, Ea=(23250, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 198,
    label = "C2H4O2H <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.819e+26, 's^-1'), n=-7.97, Ea=(20860, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.52e+34, 's^-1'), n=-9.88, Ea=(26230, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.188e+34, 's^-1'), n=-9.02, Ea=(29210, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 199,
    label = "H2 + C2H5O2 <=> H + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "C2H5O2 + HO2 <=> C2H5O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 201,
    label = "C2H5O2 + CH2O <=> C2H5O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 202,
    label = "C2H5O2 + CH4 <=> C2H5O2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "C2H5O2 + CH3OH <=> C2H5O2H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(13710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 204,
    label = "C2H5O2H <=> C2H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+14, 's^-1'), n=0, Ea=(42300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 205,
    label = "C2H4O1-2 <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.63e+13, 's^-1'), n=0, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 206,
    label = "C2H4O1-2 <=> CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.407e+12, 's^-1'), n=0, Ea=(53800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 207,
    label = "C2H4O1-2 + H <=> C2H3O1-2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(9680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 208,
    label = "C2H4O1-2 + OH <=> C2H3O1-2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+13, 'cm^3/(mol*s)'), n=0, Ea=(3610, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 209,
    label = "C2H4O1-2 + HO2 <=> C2H3O1-2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 210,
    label = "C2H4O1-2 + CH3 <=> C2H3O1-2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07e+12, 'cm^3/(mol*s)'), n=0, Ea=(11830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 211,
    label = "C2H4O1-2 + CH3O <=> C2H3O1-2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 212,
    label = "C2H4O1-2 + CH3O2 <=> C2H3O1-2 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 213,
    label = "C2H4O1-2 + C2H5O2 <=> C2H3O1-2 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 214,
    label = "C2H3O1-2 <=> CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+14, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 215,
    label = "C2H3O1-2 <=> CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 216,
    label = "C2H3 + H <=> C2H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.08e+12, 'cm^3/(mol*s)'),
            n = 0.27,
            Ea = (280, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3320, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (207.5, 'K'),
        T1 = (2663, 'K'),
        T2 = (6095, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 217,
    label = "C2H4 <=> H2 + H2CC",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(88770, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7e+50, 'cm^3/(mol*s)'),
            n = -9.31,
            Ea = (99860, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7345,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 218,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (57623.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 219,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.07e+07, 'cm^3/(mol*s)'),
        n = 1.93,
        Ea = (12950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 220,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22300, 'cm^3/(mol*s)'),
        n = 2.745,
        Ea = (2215.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 221,
    label = "C2H4 + CH3O <=> C2H3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 222,
    label = "C2H4 + CH3O2 <=> C2H3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 223,
    label = "C2H4 + C2H5O2 <=> C2H3 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 224,
    label = "C2H4 + CH3CO3 <=> C2H3 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 225,
    label = "C2H4 + CH3 <=> C2H3 + CH4",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(976, 'cm^3/(mol*s)'), n=2.947, Ea=(15148, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (8.13e-05, 'cm^3/(mol*s)'),
                n = 4.417,
                Ea = (8835.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 226,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.453e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 227,
    label = "C2H4 + O <=> CH2CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.098e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 228,
    label = "CH + CH4 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 229,
    label = "CH2(S) + CH3 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 230,
    label = "C2H4 + OH <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.35, 'cm^3/(mol*s)'),
                n = 2.92,
                Ea = (-1732.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (31.9, 'cm^3/(mol*s)'),
                n = 2.71,
                Ea = (-1172.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(555, 'cm^3/(mol*s)'), n=2.36, Ea=(-180.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (178000, 'cm^3/(mol*s)'),
                n = 1.68,
                Ea = (2060.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.37e+09, 'cm^3/(mol*s)'),
                n = 0.56,
                Ea = (6006.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.76e+13, 'cm^3/(mol*s)'),
                n = -0.5,
                Ea = (11455.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 231,
    label = "C2H4 + OH <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.37e-07, 'cm^3/(mol*s)'),
                n = 5.3,
                Ea = (-2050.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.73e-05, 'cm^3/(mol*s)'),
                n = 4.57,
                Ea = (-618, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.403, 'cm^3/(mol*s)'),
                n = 3.54,
                Ea = (1881.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.0238, 'cm^3/(mol*s)'),
                n = 3.91,
                Ea = (1722.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.25e+08, 'cm^3/(mol*s)'),
                n = 1.01,
                Ea = (10507.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.8e+09, 'cm^3/(mol*s)'),
                n = 0.81,
                Ea = (13867.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 232,
    label = "C2H4 + OH <=> C2H3OH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(10400, 'cm^3/(mol*s)'), n=2.6, Ea=(4121, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(10700, 'cm^3/(mol*s)'), n=2.6, Ea=(4129, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (15200, 'cm^3/(mol*s)'),
                n = 2.56,
                Ea = (4238.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (319000, 'cm^3/(mol*s)'),
                n = 2.19,
                Ea = (5255.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.94e+08, 'cm^3/(mol*s)'),
                n = 1.43,
                Ea = (7828.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.55e+10, 'cm^3/(mol*s)'),
                n = 0.75,
                Ea = (11490.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 233,
    label = "C2H4 + OH <=> PC2H4OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.74e+43, 'cm^3/(mol*s)'),
                n = -10.461,
                Ea = (7698.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.25e+37, 'cm^3/(mol*s)'),
                n = -8.629,
                Ea = (5214.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.84e+35, 'cm^3/(mol*s)'),
                n = -7.75,
                Ea = (4908.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.56e+36, 'cm^3/(mol*s)'),
                n = -7.752,
                Ea = (6946.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.7e+33, 'cm^3/(mol*s)'),
                n = -6.573,
                Ea = (7605.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.12e+26, 'cm^3/(mol*s)'),
                n = -4.101,
                Ea = (5757, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 234,
    label = "C2H4 + HO2 <=> C2H4O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.345e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17190, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 235,
    label = "C2H4 + CH3O2 <=> C2H4O1-2 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(17110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 236,
    label = "C2H4 + C2H5O2 <=> C2H4O1-2 + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(17110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 237,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.71e+10, 'cm^3/(mol*s)'),
            n = 1.266,
            Ea = (2709, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.346e+31, 'cm^6/(mol^2*s)'),
            n = -4.664,
            Ea = (3780, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.788,
        T3 = (-10200, 'K'),
        T1 = (1e-30, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 238,
    label = "C2H3 + O2 <=> C2H3OO",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.55e+24, 'cm^3/(mol*s)'),
                        n = -5.45,
                        Ea = (9662, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.48e+56, 'cm^3/(mol*s)'),
                        n = -15.01,
                        Ea = (19160, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.25e+64, 'cm^3/(mol*s)'),
                        n = -16.97,
                        Ea = (21290, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.34e+61, 'cm^3/(mol*s)'),
                        n = -15.79,
                        Ea = (20150, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.34e+53, 'cm^3/(mol*s)'),
                        n = -13.11,
                        Ea = (17300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.16e+48, 'cm^3/(mol*s)'),
                        n = -11.21,
                        Ea = (16000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.33e+43, 'cm^3/(mol*s)'),
                        n = -9.38,
                        Ea = (14810, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.41e+39, 'cm^3/(mol*s)'),
                        n = -8.04,
                        Ea = (14360, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.78e-09, 'cm^3/(mol*s)'),
                        n = 4.15,
                        Ea = (-4707, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.36e+22, 'cm^3/(mol*s)'),
                        n = -4.52,
                        Ea = (2839, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(2e+26, 'cm^3/(mol*s)'), n=-5.43, Ea=(2725, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (6.13e+28, 'cm^3/(mol*s)'),
                        n = -5.89,
                        Ea = (3154, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.14e+29, 'cm^3/(mol*s)'),
                        n = -5.8,
                        Ea = (3520, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.48e+28, 'cm^3/(mol*s)'),
                        n = -5.37,
                        Ea = (3636, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.32e+27, 'cm^3/(mol*s)'),
                        n = -4.95,
                        Ea = (3610, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.03e+27, 'cm^3/(mol*s)'),
                        n = -4.72,
                        Ea = (3680, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 239,
    label = "C2H3 + O2 <=> CHCHO + OH",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (3.91e+11, 'cm^3/(mol*s)'),
                        n = -0.11,
                        Ea = (2131, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1.13e+09, 'cm^3/(mol*s)'), n=0.55, Ea=(46, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (8.46e+08, 'cm^3/(mol*s)'),
                        n = 0.56,
                        Ea = (0.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.75e+14, 'cm^3/(mol*s)'),
                        n = -1.83,
                        Ea = (4.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.58e+20, 'cm^3/(mol*s)'),
                        n = -2.84,
                        Ea = (7530, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.18e+14, 'cm^3/(mol*s)'),
                        n = -2.26,
                        Ea = (-0.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.11e+25, 'cm^3/(mol*s)'),
                        n = -4.21,
                        Ea = (13050, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.65e+30, 'cm^3/(mol*s)'),
                        n = -5.35,
                        Ea = (18430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (9.91e+11, 'cm^3/(mol*s)'),
                        n = -0.66,
                        Ea = (-0.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.94e+14, 'cm^3/(mol*s)'),
                        n = -1.16,
                        Ea = (4542, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.79e+13, 'cm^3/(mol*s)'),
                        n = -0.72,
                        Ea = (3479, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.99e+11, 'cm^3/(mol*s)'),
                        n = -0.14,
                        Ea = (1995, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.35e+10, 'cm^3/(mol*s)'),
                        n = 0.23,
                        Ea = (1573, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.7e+14, 'cm^3/(mol*s)'),
                        n = -0.82,
                        Ea = (4450, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.42e+11, 'cm^3/(mol*s)'),
                        n = 0.05,
                        Ea = (3774, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.17e+11, 'cm^3/(mol*s)'),
                        n = -0.02,
                        Ea = (5338, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 240,
    label = "C2H3 + O2 <=> CH2CHO + O",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (7.88e+20, 'cm^3/(mol*s)'),
                        n = -2.67,
                        Ea = (6742, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.72e+20, 'cm^3/(mol*s)'),
                        n = -2.67,
                        Ea = (6713, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.87e+20, 'cm^3/(mol*s)'),
                        n = -2.7,
                        Ea = (6724, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.1e+20, 'cm^3/(mol*s)'),
                        n = -2.65,
                        Ea = (6489, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.5e+20, 'cm^3/(mol*s)'),
                        n = -2.53,
                        Ea = (6406, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.76e+23, 'cm^3/(mol*s)'),
                        n = -3.22,
                        Ea = (8697, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.14e+25, 'cm^3/(mol*s)'),
                        n = -3.77,
                        Ea = (11530, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.02e+26, 'cm^3/(mol*s)'),
                        n = -3.8,
                        Ea = (13910, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.36e+10, 'cm^3/(mol*s)'),
                        n = 0.62,
                        Ea = (-277.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.42e+10, 'cm^3/(mol*s)'),
                        n = 0.62,
                        Ea = (-247.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.66e+10, 'cm^3/(mol*s)'),
                        n = 0.6,
                        Ea = (-162.5, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.02e+10, 'cm^3/(mol*s)'),
                        n = 0.58,
                        Ea = (38.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.75e+09, 'cm^3/(mol*s)'),
                        n = 0.67,
                        Ea = (248, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.34e+09, 'cm^3/(mol*s)'),
                        n = 0.72,
                        Ea = (778.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.57e+09, 'cm^3/(mol*s)'),
                        n = 0.92,
                        Ea = (1219, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.85e+07, 'cm^3/(mol*s)'),
                        n = 1.28,
                        Ea = (1401, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 241,
    label = "C2H3 + O2 <=> C2H2 + HO2",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.08e+07, 'cm^3/(mol*s)'),
                        n = 1.28,
                        Ea = (3322, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.75e+06, 'cm^3/(mol*s)'),
                        n = 1.33,
                        Ea = (3216, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.21e+07, 'cm^3/(mol*s)'),
                        n = 1.27,
                        Ea = (3311, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.15e+07, 'cm^3/(mol*s)'),
                        n = 1.19,
                        Ea = (3367, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1.13e+08, 'cm^3/(mol*s)'), n=1, Ea=(3695, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (1.31e+11, 'cm^3/(mol*s)'),
                        n = 0.12,
                        Ea = (5872, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.19e+09, 'cm^3/(mol*s)'),
                        n = 0.82,
                        Ea = (5617, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+17, 'cm^3/(mol*s)'),
                        n = -1.45,
                        Ea = (12230, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(47.6, 'cm^3/(mol*s)'), n=2.75, Ea=(-796.4, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(51.6, 'cm^3/(mol*s)'), n=2.73, Ea=(-768.3, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(55.5, 'cm^3/(mol*s)'), n=2.73, Ea=(-658.5, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(46, 'cm^3/(mol*s)'), n=2.76, Ea=(-492.8, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.75, 'cm^3/(mol*s)'), n=3.07, Ea=(-601, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.48, 'cm^3/(mol*s)'), n=3.07, Ea=(85.7, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.47e+08, 'cm^3/(mol*s)'), n=0, Ea=(955, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(20.2, 'cm^3/(mol*s)'), n=2.94, Ea=(1847, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 242,
    label = "C2H3 + O2 <=> CHOCHO + H",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.79e+14, 'cm^3/(mol*s)'),
                        n = -1.03,
                        Ea = (912, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.03e+14, 'cm^3/(mol*s)'),
                        n = -1.04,
                        Ea = (922.5, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.43e+14, 'cm^3/(mol*s)'),
                        n = -1.07,
                        Ea = (982.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.73e+15, 'cm^3/(mol*s)'),
                        n = -1.29,
                        Ea = (1441, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.44e+18, 'cm^3/(mol*s)'),
                        n = -2.13,
                        Ea = (3234, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.3e+15, 'cm^3/(mol*s)'),
                        n = -1.09,
                        Ea = (2393, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.57e+33, 'cm^3/(mol*s)'),
                        n = -6.5,
                        Ea = (14910, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.28e+31, 'cm^3/(mol*s)'),
                        n = -5.76,
                        Ea = (16250, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (0.00028, 'cm^3/(mol*s)'),
                        n = 4.04,
                        Ea = (-7019, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (0.000345, 'cm^3/(mol*s)'),
                        n = 4.01,
                        Ea = (-6978, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (0.000973, 'cm^3/(mol*s)'),
                        n = 3.89,
                        Ea = (-6768, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(0.498, 'cm^3/(mol*s)'), n=3.15, Ea=(-5496, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (134000, 'cm^3/(mol*s)'),
                        n = 1.67,
                        Ea = (-2931, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.5e+15, 'cm^3/(mol*s)'),
                        n = -3.08,
                        Ea = (-4836, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.84e+10, 'cm^3/(mol*s)'),
                        n = 0.22,
                        Ea = (941.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.75e+08, 'cm^3/(mol*s)'),
                        n = 0.83,
                        Ea = (857.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 243,
    label = "C2H3 + O2 <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(866, 'cm^3/(mol*s)'), n=2.41, Ea=(6061, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(891, 'cm^3/(mol*s)'), n=2.41, Ea=(6078, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(943, 'cm^3/(mol*s)'), n=2.4, Ea=(6112, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1060, 'cm^3/(mol*s)'), n=2.39, Ea=(6180, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1090, 'cm^3/(mol*s)'), n=2.38, Ea=(6179, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1390, 'cm^3/(mol*s)'), n=2.36, Ea=(6074, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (2.49e+06, 'cm^3/(mol*s)'),
                        n = 1.42,
                        Ea = (8480, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.66e+10, 'cm^3/(mol*s)'),
                        n = 0.36,
                        Ea = (12010, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(0.182, 'cm^3/(mol*s)'), n=3.12, Ea=(1331, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0.207, 'cm^3/(mol*s)'), n=3.11, Ea=(1383, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0.271, 'cm^3/(mol*s)'), n=3.08, Ea=(1496, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0.526, 'cm^3/(mol*s)'), n=3.01, Ea=(1777, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.37, 'cm^3/(mol*s)'), n=2.9, Ea=(2225, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0.419, 'cm^3/(mol*s)'), n=2.93, Ea=(2052, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (0.000119, 'cm^3/(mol*s)'),
                        n = 4.21,
                        Ea = (2043, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(0.0013, 'cm^3/(mol*s)'), n=3.97, Ea=(3414, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 244,
    label = "C2H3 + O2 <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.49e+36, 'cm^3/(mol*s)'),
                        n = -7.6,
                        Ea = (12640, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.43e+36, 'cm^3/(mol*s)'),
                        n = -7.6,
                        Ea = (12610, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.95e+36, 'cm^3/(mol*s)'),
                        n = -7.57,
                        Ea = (12490, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.73e+35, 'cm^3/(mol*s)'),
                        n = -7.32,
                        Ea = (11820, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.43e+36, 'cm^3/(mol*s)'),
                        n = -7.47,
                        Ea = (12460, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.18e+35, 'cm^3/(mol*s)'),
                        n = -7.2,
                        Ea = (13430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.19e+20, 'cm^3/(mol*s)'),
                        n = -2.57,
                        Ea = (5578, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.73e+33, 'cm^3/(mol*s)'),
                        n = -6.28,
                        Ea = (16000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.54e+15, 'cm^3/(mol*s)'),
                        n = -1.28,
                        Ea = (515.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.59e+15, 'cm^3/(mol*s)'),
                        n = -1.28,
                        Ea = (513, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.81e+15, 'cm^3/(mol*s)'),
                        n = -1.29,
                        Ea = (520.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.08e+15, 'cm^3/(mol*s)'),
                        n = -1.31,
                        Ea = (645.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.45e+15, 'cm^3/(mol*s)'),
                        n = -1.36,
                        Ea = (1066, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.56e+15, 'cm^3/(mol*s)'),
                        n = -1.18,
                        Ea = (1429, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.03e+69, 'cm^3/(mol*s)'),
                        n = -19.23,
                        Ea = (14760, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.21e+10, 'cm^3/(mol*s)'),
                        n = 0.19,
                        Ea = (830.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 245,
    label = "C2H3 + O2 <=> CH2O + H + CO",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (5.82e+36, 'cm^3/(mol*s)'),
                        n = -7.6,
                        Ea = (12640, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.66e+36, 'cm^3/(mol*s)'),
                        n = -7.6,
                        Ea = (12610, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.55e+36, 'cm^3/(mol*s)'),
                        n = -7.57,
                        Ea = (12490, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.36e+35, 'cm^3/(mol*s)'),
                        n = -7.32,
                        Ea = (11820, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.35e+36, 'cm^3/(mol*s)'),
                        n = -7.47,
                        Ea = (12460, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.21e+36, 'cm^3/(mol*s)'),
                        n = -7.2,
                        Ea = (13430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.43e+20, 'cm^3/(mol*s)'),
                        n = -2.57,
                        Ea = (5578, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.36e+33, 'cm^3/(mol*s)'),
                        n = -6.28,
                        Ea = (16000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.06e+16, 'cm^3/(mol*s)'),
                        n = -1.28,
                        Ea = (515.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.07e+16, 'cm^3/(mol*s)'),
                        n = -1.28,
                        Ea = (513, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.13e+16, 'cm^3/(mol*s)'),
                        n = -1.29,
                        Ea = (520.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.42e+16, 'cm^3/(mol*s)'),
                        n = -1.31,
                        Ea = (645.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.2e+16, 'cm^3/(mol*s)'),
                        n = -1.36,
                        Ea = (1066, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.98e+15, 'cm^3/(mol*s)'),
                        n = -1.18,
                        Ea = (1429, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.39e+69, 'cm^3/(mol*s)'),
                        n = -19.23,
                        Ea = (14760, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.81e+10, 'cm^3/(mol*s)'),
                        n = 0.19,
                        Ea = (830.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 246,
    label = "C2H3 + O2 <=> CO + CH3O",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.19e+18, 'cm^3/(mol*s)'),
                        n = -2.66,
                        Ea = (3201, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.06e+14, 'cm^3/(mol*s)'),
                        n = -1.32,
                        Ea = (885.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.34e+14, 'cm^3/(mol*s)'),
                        n = -1.33,
                        Ea = (900.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.03e+11, 'cm^3/(mol*s)'),
                        n = -0.33,
                        Ea = (-747.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.89e+12, 'cm^3/(mol*s)'),
                        n = -3,
                        Ea = (-8995, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.93e+24, 'cm^3/(mol*s)'),
                        n = -5.63,
                        Ea = (1.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.1e+18, 'cm^3/(mol*s)'),
                        n = -2.22,
                        Ea = (5178, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.79e+32, 'cm^3/(mol*s)'),
                        n = -6.45,
                        Ea = (16810, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.29e+09, 'cm^3/(mol*s)'),
                        n = 0.18,
                        Ea = (-1717, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.99e+11, 'cm^3/(mol*s)'),
                        n = -2.93,
                        Ea = (-9564, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.91e+11, 'cm^3/(mol*s)'),
                        n = -2.93,
                        Ea = (-10120, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.77e+21, 'cm^3/(mol*s)'),
                        n = -3.54,
                        Ea = (4772, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.99e+15, 'cm^3/(mol*s)'),
                        n = -1.62,
                        Ea = (1849, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.33e+16, 'cm^3/(mol*s)'),
                        n = -1.96,
                        Ea = (3324, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.02e+72, 'cm^3/(mol*s)'),
                        n = -20.69,
                        Ea = (15860, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.1e+09, 'cm^3/(mol*s)'),
                        n = 0.31,
                        Ea = (1024, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 247,
    label = "C2H3 + O2 <=> CO2 + CH3",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.37e+35, 'cm^3/(mol*s)'),
                        n = -7.76,
                        Ea = (12630, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.73e+35, 'cm^3/(mol*s)'),
                        n = -7.72,
                        Ea = (12520, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.47e+34, 'cm^3/(mol*s)'),
                        n = -7.55,
                        Ea = (12140, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.25e+31, 'cm^3/(mol*s)'),
                        n = -6.7,
                        Ea = (10440, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.63e+35, 'cm^3/(mol*s)'),
                        n = -7.75,
                        Ea = (12830, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.09e+35, 'cm^3/(mol*s)'),
                        n = -7.53,
                        Ea = (14050, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.84e+18, 'cm^3/(mol*s)'),
                        n = -2.44,
                        Ea = (5408, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.21e+32, 'cm^3/(mol*s)'),
                        n = -6.32,
                        Ea = (16190, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (6.27e+13, 'cm^3/(mol*s)'),
                        n = -1.16,
                        Ea = (406.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.24e+13, 'cm^3/(mol*s)'),
                        n = -1.16,
                        Ea = (401.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.12e+13, 'cm^3/(mol*s)'),
                        n = -1.16,
                        Ea = (397, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.32e+13, 'cm^3/(mol*s)'),
                        n = -1.14,
                        Ea = (446.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.45e+14, 'cm^3/(mol*s)'),
                        n = -1.26,
                        Ea = (987.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.02e+13, 'cm^3/(mol*s)'),
                        n = -1.11,
                        Ea = (1409, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.4e+70, 'cm^3/(mol*s)'),
                        n = -20.11,
                        Ea = (15430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.21e+08, 'cm^3/(mol*s)'),
                        n = 0.25,
                        Ea = (855.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 248,
    label = "C2H3OO <=> CHCHO + OH",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(3.64e+49, 's^-1'), n=-12.13, Ea=(67420, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.44e+36, 's^-1'), n=-9.92, Ea=(41220, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.18e+40, 's^-1'), n=-10.53, Ea=(43670, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.79e+46, 's^-1'), n=-10.72, Ea=(51900, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.6e+49, 's^-1'), n=-11.24, Ea=(54150, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.38e+51, 's^-1'), n=-11.64, Ea=(56980, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2e+54, 's^-1'), n=-12.22, Ea=(61840, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.54e+195, 's^-1'), n=-52.27, Ea=(163500, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.17e+56, 's^-1'), n=-14.81, Ea=(60700, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.32e+40, 's^-1'), n=-9.39, Ea=(50420, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.61e+43, 's^-1'), n=-9.99, Ea=(50290, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.33e+124, 's^-1'), n=-36.77, Ea=(70100, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.88e+103, 's^-1'), n=-29.49, Ea=(65410, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.96e+86, 's^-1'), n=-23.81, Ea=(62170, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.51e+57, 's^-1'), n=-13.94, Ea=(55390, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.79e+34, 's^-1'), n=-6.4, Ea=(50000, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 249,
    label = "C2H3OO <=> CH2CHO + O",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(2.7e+180, 's^-1'), n=-48.19, Ea=(169300, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.9e+38, 's^-1'), n=-8.69, Ea=(42770, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.57e+47, 's^-1'), n=-11.21, Ea=(47050, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.62e+81, 's^-1'), n=-21.28, Ea=(65080, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.86e+68, 's^-1'), n=-16.83, Ea=(60680, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.02e+55, 's^-1'), n=-12.69, Ea=(55840, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.11e+53, 's^-1'), n=-11.79, Ea=(56690, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.3e+48, 's^-1'), n=-10.31, Ea=(56090, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.47e+30, 's^-1'), n=-6.64, Ea=(41110, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.65e-12, 's^-1'), n=5.96, Ea=(22890, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.95e+22, 's^-1'), n=-3.71, Ea=(36270, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.39e+33, 's^-1'), n=-6.62, Ea=(41280, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.37e+31, 's^-1'), n=-5.96, Ea=(41260, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.13e+29, 's^-1'), n=-5.1, Ea=(40710, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.66e+27, 's^-1'), n=-4.5, Ea=(40530, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.99e+25, 's^-1'), n=-3.85, Ea=(40120, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 250,
    label = "C2H3OO <=> CHOCHO + H",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(6.41e+80, 's^-1'), n=-22.2, Ea=(51750, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.31e+65, 's^-1'), n=-17.01, Ea=(48090, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.98e+51, 's^-1'), n=-12.62, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.48e+44, 's^-1'), n=-10.12, Ea=(40790, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.26e+59, 's^-1'), n=-14.33, Ea=(51390, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.93e+26, 's^-1'), n=-4.67, Ea=(34320, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.06e+33, 's^-1'), n=-6.38, Ea=(39520, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.3e+32, 's^-1'), n=-5.92, Ea=(40660, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.19e+28, 's^-1'), n=-6.01, Ea=(28740, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.4e+25, 's^-1'), n=-4.8, Ea=(28940, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.91e+20, 's^-1'), n=-3.29, Ea=(27550, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.58e+19, 's^-1'), n=-2.82, Ea=(27620, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.93e+22, 's^-1'), n=-3.54, Ea=(29980, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.51e+29, 's^-1'), n=-5.75, Ea=(34490, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.14e+61, 's^-1'), n=-16.16, Ea=(43280, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.14e+19, 's^-1'), n=-2.56, Ea=(29670, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 251,
    label = "C2H3OO <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.15e+47, 's^-1'), n=-12.28, Ea=(75330, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.43e+09, 's^-1'), n=-2.06, Ea=(33720, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(60600, 's^-1'), n=0.17, Ea=(34220, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.51e+19, 's^-1'), n=-3.61, Ea=(43060, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.13e+33, 's^-1'), n=-7.39, Ea=(51610, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.44e+36, 's^-1'), n=-7.99, Ea=(54680, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.19e+37, 's^-1'), n=-7.8, Ea=(56460, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.08e+35, 's^-1'), n=-7.21, Ea=(57550, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(231, 's^-1'), n=-0.73, Ea=(25710, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.83e-23, 's^-1'), n=7.84, Ea=(20190, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.82e+63, 's^-1'), n=-20.44, Ea=(43420, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.18e+27, 's^-1'), n=-7.76, Ea=(37230, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.32e-05, 's^-1'), n=3.47, Ea=(31560, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0.106, 's^-1'), n=2.64, Ea=(34160, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(562, 's^-1'), n=1.7, Ea=(36450, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.11e+07, 's^-1'), n=0.52, Ea=(38670, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 252,
    label = "C2H3OO <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.66e+174, 's^-1'), n=-55.52, Ea=(60320, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.03e+66, 's^-1'), n=-17.25, Ea=(48120, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.82e+43, 's^-1'), n=-9.87, Ea=(37960, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.64e+33, 's^-1'), n=-6.88, Ea=(34370, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.29e+171, 's^-1'), n=-43.53, Ea=(191900, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.03e+32, 's^-1'), n=-6.06, Ea=(35500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.85e+34, 's^-1'), n=-6.57, Ea=(38510, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.7e+29, 's^-1'), n=-5.19, Ea=(36800, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(2.27e+35, 's^-1'), n=-7.97, Ea=(31280, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.08e+26, 's^-1'), n=-4.96, Ea=(28780, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.45e+20, 's^-1'), n=-3.08, Ea=(26630, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.06e+130, 's^-1'), n=-39.38, Ea=(54700, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.35e+34, 's^-1'), n=-6.87, Ea=(35700, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.18e+175, 's^-1'), n=-53.78, Ea=(68500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.07e+185, 's^-1'), n=-54.22, Ea=(88990, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(468, 's^-1'), n=1.81, Ea=(18100, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 253,
    label = "C2H3OO <=> CH2O + H + CO",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(3.88e+174, 's^-1'), n=-55.52, Ea=(60320, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.11e+67, 's^-1'), n=-17.25, Ea=(48120, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.26e+43, 's^-1'), n=-9.87, Ea=(37960, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.02e+34, 's^-1'), n=-6.88, Ea=(34370, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.7e+172, 's^-1'), n=-43.53, Ea=(191900, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.4e+32, 's^-1'), n=-6.06, Ea=(35500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.32e+34, 's^-1'), n=-6.57, Ea=(38510, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.33e+30, 's^-1'), n=-5.19, Ea=(36800, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(5.29e+35, 's^-1'), n=-7.97, Ea=(31280, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.85e+26, 's^-1'), n=-4.96, Ea=(28780, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.37e+20, 's^-1'), n=-3.08, Ea=(26630, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.46e+130, 's^-1'), n=-39.38, Ea=(54700, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.49e+34, 's^-1'), n=-6.87, Ea=(35700, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.09e+175, 's^-1'), n=-53.78, Ea=(68500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.49e+185, 's^-1'), n=-54.22, Ea=(88990, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1090, 's^-1'), n=1.81, Ea=(18100, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 254,
    label = "C2H3OO <=> CO + CH3O",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(5.2e+33, 's^-1'), n=-7.92, Ea=(31320, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.26e+98, 's^-1'), n=-27.09, Ea=(64060, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.8e+33, 's^-1'), n=-7.27, Ea=(33760, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.83e+33, 's^-1'), n=-7.2, Ea=(35100, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.28e+79, 's^-1'), n=-19.61, Ea=(74870, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.07e+32, 's^-1'), n=-6.62, Ea=(37210, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.86e+44, 's^-1'), n=-10.04, Ea=(47030, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(2.31e+129, 's^-1'), n=-41.86, Ea=(45850, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.42e+28, 's^-1'), n=-5.99, Ea=(30540, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.69e-50, 's^-1'), n=16.63, Ea=(-3900, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.19e-39, 's^-1'), n=13.61, Ea=(-1317, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.8e+86, 's^-1'), n=-23.08, Ea=(61010, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1270, 's^-1'), n=1.44, Ea=(18660, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.97e+17, 's^-1'), n=-2.23, Ea=(28590, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(32500, 's^-1'), n=1.694, Ea=(23327.6, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 255,
    label = "CHOCHO + OH => HCO + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (61329.9, 'cm^3/(mol*s)'),
        n = 2.65,
        Ea = (-4586.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 256,
    label = "C2H3 + H <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 257,
    label = "C2H3 + H <=> H2CC + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "C2H3 + OH <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.011e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 259,
    label = "C2H3 + CH3 <=> CH4 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.92e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 260,
    label = "C2H3 + C2H3 <=> C2H2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 261,
    label = "C2H + H <=> C2H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.646,
        T3 = (132, 'K'),
        T1 = (1315, 'K'),
        T2 = (5566, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 262,
    label = "C2H2 <=> H2CC",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(8e+14, 's^-1'), n=-0.52, Ea=(50750, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.45e+15, 'cm^3/(mol*s)'),
            n = -0.64,
            Ea = (49700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, 'C=C': 2.5, 'C#C': 2.5},
    ),
)

entry(
    index = 263,
    label = "C2H2 + O <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.395e+08, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (2472, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 264,
    label = "C2H2 + O <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.958e+09, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (2472, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 265,
    label = "C2H2 + HO2 <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+09, 'cm^3/(mol*s)'), n=0, Ea=(7949, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 266,
    label = "C2H2 + HCO <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 267,
    label = "C2H2 + CH2 <=> C3H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6620, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 268,
    label = "C2H2 + CH2(S) <=> C3H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 269,
    label = "C2H2 + HCCO <=> C3H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 270,
    label = "H2CC + H <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 271,
    label = "H2CC + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 272,
    label = "H2CC + O2 <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 273,
    label = "C2H2 + OH <=> C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.632e+06, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (17060, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 274,
    label = "C2H2 + OH <=> HCCOH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (280000, 'cm^3/(mol*s)'),
                n = 2.28,
                Ea = (12420, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (746700, 'cm^3/(mol*s)'),
                n = 2.16,
                Ea = (12550, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.776e+06, 'cm^3/(mol*s)'),
                n = 2.04,
                Ea = (12670, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.415e+06, 'cm^3/(mol*s)'),
                n = 2,
                Ea = (12710, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.21e+06, 'cm^3/(mol*s)'),
                n = 1.97,
                Ea = (12810, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.347e+06, 'cm^3/(mol*s)'),
                n = 1.89,
                Ea = (13600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 275,
    label = "C2H2 + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1578, 'cm^3/(mol*s)'), n=2.56, Ea=(-844.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (15180, 'cm^3/(mol*s)'),
                n = 2.28,
                Ea = (-292.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (301700, 'cm^3/(mol*s)'),
                n = 1.92,
                Ea = (598.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.528e+06, 'cm^3/(mol*s)'),
                n = 1.55,
                Ea = (2106, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.101e+06, 'cm^3/(mol*s)'),
                n = 1.65,
                Ea = (3400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(14570, 'cm^3/(mol*s)'), n=2.45, Ea=(4477, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 276,
    label = "C2H2 + OH <=> CH3 + CO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (475700, 'cm^3/(mol*s)'),
                n = 1.68,
                Ea = (-329.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.372e+06, 'cm^3/(mol*s)'),
                n = 1.4,
                Ea = (226.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.648e+07, 'cm^3/(mol*s)'),
                n = 1.05,
                Ea = (1115, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.277e+09, 'cm^3/(mol*s)'),
                n = 0.73,
                Ea = (2579, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.312e+08, 'cm^3/(mol*s)'),
                n = 0.92,
                Ea = (3736, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(825000, 'cm^3/(mol*s)'), n=1.77, Ea=(4697, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 277,
    label = "C2H2 + OH <=> C2H2OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.913e+32, 'cm^3/(mol*s)'),
                n = -7.126,
                Ea = (5824, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.067e+32, 'cm^3/(mol*s)'),
                n = -6.847,
                Ea = (5508, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.646e+32, 'cm^3/(mol*s)'),
                n = -6.717,
                Ea = (5822, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.387e+31, 'cm^3/(mol*s)'),
                n = -6.087,
                Ea = (6348, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.892e+29, 'cm^3/(mol*s)'),
                n = -5.288,
                Ea = (7055, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.367e+25, 'cm^3/(mol*s)'),
                n = -3.754,
                Ea = (6543, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 278,
    label = "H + HCCOH <=> H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 279,
    label = "C2H + O2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 280,
    label = "C2H + O <=> CO + CH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 281,
    label = "C2H + H2 <=> H + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(490000, 'cm^3/(mol*s)'), n=2.5, Ea=(560, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 282,
    label = "C2H + OH <=> H + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 283,
    label = "CH3CHO <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.45e+22, 's^-1'), n=-1.74, Ea=(86355, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.03e+59, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95912.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.00249,
        T3 = (718.1, 'K'),
        T1 = (6.089, 'K'),
        T2 = (3780, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 284,
    label = "CH3CHO <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.72e+21, 's^-1'), n=-1.74, Ea=(86355, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.144e+58, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95912.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.00249,
        T3 = (718.1, 'K'),
        T1 = (6.089, 'K'),
        T2 = (3780, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 285,
    label = "CH3CHO + O2 <=> CH3CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(39150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 286,
    label = "CH3CHO + O <=> CH3CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 287,
    label = "CH3CHO + H <=> CH3CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(131000, 'cm^3/(mol*s)'), n=2.58, Ea=(1220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 288,
    label = "CH3CHO + OH <=> CH3CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+12, 'cm^3/(mol*s)'), n=0, Ea=(-619, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 289,
    label = "CH3CHO + HO2 <=> CH3CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 290,
    label = "CH3CHO + CH3 <=> CH3CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000708, 'cm^3/(mol*s)'),
        n = 4.58,
        Ea = (1966, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 291,
    label = "CH3CHO + CH3O2 <=> CH3CO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 292,
    label = "CH3CHO + CH3CO3 <=> CH3CO + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 293,
    label = "CH3CHO + H <=> CH2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2720, 'cm^3/(mol*s)'), n=3.1, Ea=(5210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 294,
    label = "CH3CHO + OH <=> CH2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(172000, 'cm^3/(mol*s)'), n=2.4, Ea=(815, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 295,
    label = "CH3CHO + OH <=> CH3 + HOCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+15, 'cm^3/(mol*s)'), n=-1.076, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 296,
    label = "CH3CO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.07e+12, 's^-1'), n=0.63, Ea=(16900, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.65e+18, 'cm^3/(mol*s)'),
            n = -0.97,
            Ea = (14600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.629,
        T3 = (8.73e+09, 'K'),
        T1 = (5.52, 'K'),
        T2 = (7.6e+07, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 297,
    label = "CH3CO <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.413e+07, 's^-1'), n=1.917, Ea=(44987.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.516e+51, 'cm^3/(mol*s)'),
            n = -10.27,
            Ea = (55390, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6009,
        T3 = (8.103e+09, 'K'),
        T1 = (667.7, 'K'),
        T2 = (5e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 298,
    label = "CH3CO + H <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 299,
    label = "CH3CO + O <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 300,
    label = "CH3CO + CH3 <=> CH2CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 301,
    label = "CH3CO + O2 <=> CH3CO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 302,
    label = "CH3CO3 + HO2 <=> CH3CO3H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 303,
    label = "H2O2 + CH3CO3 <=> HO2 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(9936, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 304,
    label = "CH4 + CH3CO3 <=> CH3 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 305,
    label = "C2H3OH <=> CH3CHO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.42e+46, 's^-1'), n=-10.56, Ea=(67420, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.42e+42, 's^-1'), n=-9.09, Ea=(67069.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.9e+27, 's^-1'), n=-4.35, Ea=(61612.9, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 306,
    label = "C2H3OH + O2 <=> CH2CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.31e+11, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (39830, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 307,
    label = "C2H3OH + O <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.875e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 308,
    label = "C2H3OH + H <=> CH2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1480, 'cm^3/(mol*s)'), n=3.077, Ea=(7220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 309,
    label = "C2H3OH + OH <=> CH2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.33e+09, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (540.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 310,
    label = "C2H3OH + CH3 <=> CH2CHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.03e-08, 'cm^3/(mol*s)'),
        n = 5.9,
        Ea = (1052, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 311,
    label = "C2H3OH + CH3O2 <=> CH2CHO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3400, 'cm^3/(mol*s)'), n=2.5, Ea=(8922, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 312,
    label = "C2H3OH + H <=> C2H2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47e+07, 'cm^3/(mol*s)'),
        n = 2.03,
        Ea = (15200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 313,
    label = "C2H3OH + H <=> PC2H4OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+08, 'cm^3/(mol*s)'),
        n = 1.577,
        Ea = (3670, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 314,
    label = "C2H3OH + HO2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 315,
    label = "CH2CHO <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.43e+15, 's^-1'), n=-0.15, Ea=(45600, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6e+29, 'cm^3/(mol*s)'),
            n = -3.8,
            Ea = (43423.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.985,
        T3 = (393, 'K'),
        T1 = (9.8e+09, 'K'),
        T2 = (5e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 316,
    label = "CH2CHO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.93e+12, 's^-1'), n=0.29, Ea=(40300, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.52e+33, 'cm^3/(mol*s)'),
            n = -5.07,
            Ea = (41300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 7.13e-17,
        T3 = (1150, 'K'),
        T1 = (4.99e+09, 'K'),
        T2 = (1.79e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 317,
    label = "CH3CO3H <=> CH3CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+14, 's^-1'), n=0, Ea=(40150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 318,
    label = "CH3CO3 + CH2O <=> CH3CO3H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 319,
    label = "CH3CO3 + C2H6 <=> CH3CO3H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 320,
    label = "CH3CO2 <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.4e+15, 'cm^3/(mol*s)'), n=0, Ea=(10500, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 321,
    label = "CH2CHO + O2 <=> O2CH2CHO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.58e+77, 'cm^3/(mol*s)'),
                n = -21.9,
                Ea = (19350, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.88e+69, 'cm^3/(mol*s)'),
                n = -18.84,
                Ea = (19240, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.8e+59, 'cm^3/(mol*s)'),
                n = -15.4,
                Ea = (17650, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.05e+50, 'cm^3/(mol*s)'),
                n = -12.2,
                Ea = (15630, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 322,
    label = "CH2CHO + O2 <=> CH2CO + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (188000, 'cm^3/(mol*s)'),
                n = 2.37,
                Ea = (23730, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (188000, 'cm^3/(mol*s)'),
                n = 2.37,
                Ea = (27370, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (251000, 'cm^3/(mol*s)'),
                n = 2.33,
                Ea = (23800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.05e+07, 'cm^3/(mol*s)'),
                n = 1.63,
                Ea = (25290, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 323,
    label = "CH2CHO + O2 => CH2O + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.68e+17, 'cm^3/(mol*s)'),
                n = -1.84,
                Ea = (6530, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.52e+20, 'cm^3/(mol*s)'),
                n = -2.58,
                Ea = (8980, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.65e+19, 'cm^3/(mol*s)'),
                n = -2.22,
                Ea = (10340, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.953e+13, 'cm^3/(mol*s)'),
                n = -0.6,
                Ea = (10120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 324,
    label = "CH2CHO + O2 <=> HO2CH2CO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.64e+65, 'cm^3/(mol*s)'),
                n = -21.87,
                Ea = (19020, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.64e+58, 'cm^3/(mol*s)'),
                n = -19,
                Ea = (19090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.65e+48, 'cm^3/(mol*s)'),
                n = -15.55,
                Ea = (17460, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.8e+38, 'cm^3/(mol*s)'),
                n = -12.14,
                Ea = (14960, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 325,
    label = "O2CH2CHO <=> HO2CH2CO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.27e+30, 's^-1'), n=-6.65, Ea=(24500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.73e+26, 's^-1'), n=-4.99, Ea=(23760, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.03e+19, 's^-1'), n=-2.92, Ea=(22170, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.43e+16, 's^-1'), n=-1.67, Ea=(21210, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 326,
    label = "O2CH2CHO <=> CH2CO + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.05e+40, 's^-1'), n=-13.31, Ea=(52150, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.72e+45, 's^-1'), n=-14, Ea=(52200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.16e+55, 's^-1'), n=-15.76, Ea=(55080, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.12e+61, 's^-1'), n=-16.04, Ea=(60010, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 327,
    label = "HO2CH2CO => CO + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.36e+17, 's^-1'), n=-2.95, Ea=(8100, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.38e+18, 's^-1'), n=-2.95, Ea=(8100, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.51e+19, 's^-1'), n=-2.95, Ea=(8110, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.16e+20, 's^-1'), n=-3.02, Ea=(8240, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 328,
    label = "HO2CH2CO <=> CH2CO + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.12e+07, 's^-1'), n=-3.76, Ea=(21680, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e+08, 's^-1'), n=-3.76, Ea=(21680, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.2e+08, 's^-1'), n=-3.73, Ea=(21630, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.09e+09, 's^-1'), n=-3.55, Ea=(21220, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 329,
    label = "CH2 + CO <=> CH2CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7095, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5907,
        T3 = (275, 'K'),
        T1 = (1226, 'K'),
        T2 = (5185, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 330,
    label = "CH2CO + H <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.401e+15, 'cm^3/(mol*s)'),
        n = -0.171,
        Ea = (8783.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 331,
    label = "CH2CO + O <=> HCCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 332,
    label = "CH2CO + OH <=> HCCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 333,
    label = "CH2CO + H <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.704e+13, 'cm^3/(mol*s)'),
        n = -0.171,
        Ea = (4183.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 334,
    label = "CH + CH2O <=> H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.46e+13, 'cm^3/(mol*s)'), n=0, Ea=(-515, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 335,
    label = "CH2CO + O <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+12, 'cm^3/(mol*s)'), n=0, Ea=(1350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 336,
    label = "CH2CO + OH <=> CH2OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 337,
    label = "CH2CO + CH2(S) <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 338,
    label = "CH2CO + CH3 <=> C2H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47690, 'cm^3/(mol*s)'), n=2.312, Ea=(9468, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 339,
    label = "HCCO + OH => H2 + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 340,
    label = "HCCO + O => H + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 341,
    label = "CH + CO <=> HCCO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (7.57e+22, 'cm^6/(mol^2*s)'),
            n = -1.9,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 342,
    label = "HCCO + H <=> CH2(S) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 343,
    label = "HCCO + O2 => OH + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.91e+11, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (1020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 344,
    label = "HCCO + O2 => CO2 + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.78e+12, 'cm^3/(mol*s)'),
        n = -0.142,
        Ea = (1150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 345,
    label = "CH + HCCO <=> CO + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 346,
    label = "C2H5OH <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.41e+59, 's^-1'), n=-14.2, Ea=(83672.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.62e+57, 's^-1'), n=-13.3, Ea=(85262.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.65e+52, 's^-1'), n=-11.5, Ea=(84745.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.23e+43, 's^-1'), n=-8.9, Ea=(81506.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.59e+32, 's^-1'), n=-5.6, Ea=(76062.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.84e+20, 's^-1'), n=-2.06, Ea=(69465.5, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 347,
    label = "C2H5OH <=> CH3 + CH2OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.2e+54, 's^-1'), n=-12.9, Ea=(100006, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.18e+59, 's^-1'), n=-14, Ea=(99906.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.62e+66, 's^-1'), n=-15.3, Ea=(105390, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.55e+64, 's^-1'), n=-14.5, Ea=(106183, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.55e+58, 's^-1'), n=-12.3, Ea=(105768, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.78e+47, 's^-1'), n=-8.96, Ea=(101059, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 348,
    label = "C2H5OH <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.1e+46, 's^-1'), n=-11.3, Ea=(111053, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.86e+56, 's^-1'), n=-13.5, Ea=(107238, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.65e+63, 's^-1'), n=-15, Ea=(109623, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.46e+65, 's^-1'), n=-14.9, Ea=(112345, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.79e+61, 's^-1'), n=-13.4, Ea=(113080, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.17e+51, 's^-1'), n=-10.3, Ea=(109941, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 349,
    label = "C2H5OH + O <=> C2H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00146, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 350,
    label = "C2H5OH + OH <=> C2H5O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00581, 'cm^3/(mol*s)'),
        n = 4.28,
        Ea = (-3560, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 351,
    label = "C2H5OH + H <=> C2H5O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 352,
    label = "C2H5OH + HO2 <=> C2H5O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (10533.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 353,
    label = "C2H5OH + CH3 <=> C2H5O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.035, 'cm^3/(mol*s)'), n=3.57, Ea=(7721, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 354,
    label = "C2H5OH + CH3O2 <=> C2H5O + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.236e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (10533.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 355,
    label = "C2H5OH + C2H5 <=> PC2H4OH + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 356,
    label = "C2H5OH + O2 <=> SC2H4OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(50150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 357,
    label = "C2H5OH + O <=> SC2H4OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(145000, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 358,
    label = "C2H5OH + H <=> SC2H4OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(87900, 'cm^3/(mol*s)'), n=2.68, Ea=(2910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 359,
    label = "C2H5OH + OH <=> SC2H4OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (75200, 'cm^3/(mol*s)'),
        n = 2.49,
        Ea = (-1474.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 360,
    label = "C2H5OH + HO2 <=> SC2H4OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.45e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (7475.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 361,
    label = "C2H5OH + CH3 <=> SC2H4OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.93, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 362,
    label = "C2H5OH + CH3O2 <=> SC2H4OH + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.225e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (7475.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 363,
    label = "C2H5OH + C2H5 <=> SC2H4OH + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 364,
    label = "C2H5OH + O2 <=> PC2H4OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(52800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 365,
    label = "C2H5OH + O <=> PC2H4OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(969, 'cm^3/(mol*s)'), n=3.23, Ea=(4658, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 366,
    label = "C2H5OH + H <=> PC2H4OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(53100, 'cm^3/(mol*s)'), n=2.81, Ea=(7490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 367,
    label = "C2H5OH + OH <=> PC2H4OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3760, 'cm^3/(mol*s)'),
        n = 2.78,
        Ea = (-1810.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 368,
    label = "C2H5OH + HO2 <=> PC2H4OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.03986, 'cm^3/(mol*s)'),
        n = 4.3,
        Ea = (15333, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 369,
    label = "C2H5OH + CH3 <=> PC2H4OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(330, 'cm^3/(mol*s)'), n=3.3, Ea=(12290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 370,
    label = "C2H5OH + CH3O2 <=> PC2H4OH + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01995, 'cm^3/(mol*s)'),
        n = 4.3,
        Ea = (15333, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 371,
    label = "SC2H4OH <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.69e+52, 's^-1'), n=-13.38, Ea=(45049, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.29e+56, 's^-1'), n=-14.12, Ea=(48129, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.58e+57, 's^-1'), n=-14.16, Ea=(50743, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.36e+55, 's^-1'), n=-13.15, Ea=(51886, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.66e+48, 's^-1'), n=-10.64, Ea=(50297, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.26e+44, 's^-1'), n=-9.59, Ea=(49218, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.01e+40, 's^-1'), n=-8.06, Ea=(47439, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e+36, 's^-1'), n=-6.84, Ea=(45899, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 372,
    label = "SC2H4OH <=> C2H3OH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.4e+46, 's^-1'), n=-11.63, Ea=(44323, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.21e+51, 's^-1'), n=-12.55, Ea=(47240, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.87e+54, 's^-1'), n=-13.15, Ea=(50702, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.79e+53, 's^-1'), n=-12.51, Ea=(52560, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.33e+46, 's^-1'), n=-10.2, Ea=(51441, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.87e+43, 's^-1'), n=-9.17, Ea=(50440, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.08e+38, 's^-1'), n=-7.65, Ea=(48713, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.12e+34, 's^-1'), n=-6.41, Ea=(47182, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 373,
    label = "SC2H4OH <=> C2H5O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.48e+45, 's^-1'), n=-11.63, Ea=(44328, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.54e+49, 's^-1'), n=-12.37, Ea=(46445, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.65e+54, 's^-1'), n=-13.4, Ea=(50330, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.81e+55, 's^-1'), n=-13.31, Ea=(53132, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.58e+49, 's^-1'), n=-11.32, Ea=(52714, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.11e+46, 's^-1'), n=-10.33, Ea=(51834, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.68e+41, 's^-1'), n=-8.83, Ea=(50202, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.54e+37, 's^-1'), n=-7.58, Ea=(48697, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 374,
    label = "SC2H4OH <=> PC2H4OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.65e+36, 's^-1'), n=-8.86, Ea=(51019, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.56e+37, 's^-1'), n=-8.89, Ea=(51114, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.14e+39, 's^-1'), n=-9.19, Ea=(51912, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.82e+44, 's^-1'), n=-10.34, Ea=(55296, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.26e+48, 's^-1'), n=-11.06, Ea=(59458, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.84e+47, 's^-1'), n=-10.74, Ea=(59901, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.23e+45, 's^-1'), n=-9.84, Ea=(59604, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.7e+42, 's^-1'), n=-8.83, Ea=(58737, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 375,
    label = "CH3 + CH2O <=> C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(6336, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 376,
    label = "CH3CHO + H <=> C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.61e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (7090, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 377,
    label = "C2H5O + O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.28e+10, 'cm^3/(mol*s)'), n=0, Ea=(1097, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 378,
    label = "O2C2H4OH <=> PC2H4OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+16, 's^-1'), n=-1, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 379,
    label = "O2C2H4OH => OH + CH2O + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.25e+11, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 380,
    label = "SC2H4OH + O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 381,
    label = "SC2H4OH + O2 <=> C2H3OH + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(512, 'cm^3/(mol*s)'), n=2.496, Ea=(-414, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(533, 'cm^3/(mol*s)'), n=2.49, Ea=(-402, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(762, 'cm^3/(mol*s)'), n=2.446, Ea=(-296, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8920, 'cm^3/(mol*s)'), n=2.146, Ea=(470, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (438000, 'cm^3/(mol*s)'),
                n = 1.699,
                Ea = (2330, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 382,
    label = "CH3OCH3 <=> CH3 + CH3O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.33e+19, 's^-1'), n=-0.661, Ea=(84139, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.72e+59, 'cm^3/(mol*s)'),
            n = -11.4,
            Ea = (93295.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1e-30, 'K'),
        T1 = (880, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 3, 'CC': 4.5, '[H][H]': 3, 'O': 9, 'COC': 5, 'N#N': 1.5, '[C]=O': 2.25},
    ),
)

entry(
    index = 383,
    label = "CH3OCH3 + OH <=> CH3OCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (935000, 'cm^3/(mol*s)'),
        n = 2.29,
        Ea = (-780.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 384,
    label = "CH3OCH3 + H <=> CH3OCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.721e+06, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (3384, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 385,
    label = "CH3OCH3 + O <=> CH3OCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.75e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (2250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 386,
    label = "CH3OCH3 + HO2 <=> CH3OCH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00317, 'cm^3/(mol*s)'),
        n = 4.64,
        Ea = (10556, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 387,
    label = "CH3OCH3 + CH3O2 <=> CH3OCH2 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001268, 'cm^3/(mol*s)'),
        n = 4.64,
        Ea = (10556, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 388,
    label = "CH3OCH3 + CH3 <=> CH3OCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.02, 'cm^3/(mol*s)'), n=3.78, Ea=(9687.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 389,
    label = "CH3OCH3 + O2 <=> CH3OCH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(44910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 390,
    label = "CH3OCH3 + CH3O <=> CH3OCH2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(4074, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 391,
    label = "CH3OCH3 + CH3OCH2O2 <=> CH3OCH2 + CH3OCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 392,
    label = "CH3OCH3 + O2CHO <=> CH3OCH2 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44250, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 393,
    label = "CH3OCH3 + OCHO <=> CH3OCH2 + HOCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 394,
    label = "CH3OCH2 + CH3O <=> CH3OCH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 395,
    label = "CH3OCH2 + CH2O <=> CH3OCH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5490, 'cm^3/(mol*s)'), n=2.8, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 396,
    label = "CH3OCH2 + CH3CHO <=> CH3OCH3 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(8499, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 397,
    label = "CH3OCH2 <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (7.494e+23, 's^-1'),
                n = -4.5152,
                Ea = (25236.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.921e+28, 's^-1'),
                n = -5.7271,
                Ea = (27494.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.229e+29, 's^-1'),
                n = -5.6103,
                Ea = (28898.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.608e+27, 's^-1'),
                n = -4.7073,
                Ea = (29735.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.659e+29, 's^-1'),
                n = -4.9358,
                Ea = (31785.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 398,
    label = "CH3OCH2 + O2 <=> CH3OCH2O2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.12e+18, 'cm^3/(mol*s)'),
                n = -3.37,
                Ea = (-4294, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.33e+21, 'cm^3/(mol*s)'),
                n = -3.95,
                Ea = (-2615, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.13e+28, 'cm^3/(mol*s)'),
                n = -5.24,
                Ea = (4088, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(3.91e+27, 'cm^3/(mol*s)'), n=-5, Ea=(4512, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (2.75e+24, 'cm^3/(mol*s)'),
                n = -3.87,
                Ea = (4290, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.97e+22, 'cm^3/(mol*s)'),
                n = -3.23,
                Ea = (3781, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.19e+19, 'cm^3/(mol*s)'),
                n = -2.35,
                Ea = (2908, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.43e+17, 'cm^3/(mol*s)'),
                n = -1.73,
                Ea = (2210, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 399,
    label = "CH3OCH2 + O2 <=> CH2OCH2O2H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.08e+20, 'cm^3/(mol*s)'),
                n = -4.39,
                Ea = (469, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.47e+23, 'cm^3/(mol*s)'),
                n = -4.96,
                Ea = (2183, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.81e+28, 'cm^3/(mol*s)'),
                n = -5.63,
                Ea = (7848, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.19e+27, 'cm^3/(mol*s)'),
                n = -5.33,
                Ea = (8144, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.67e+24, 'cm^3/(mol*s)'),
                n = -4.36,
                Ea = (8417, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.08e+23, 'cm^3/(mol*s)'),
                n = -3.9,
                Ea = (8494, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.08e+21, 'cm^3/(mol*s)'),
                n = -3.28,
                Ea = (8585, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.62e+20, 'cm^3/(mol*s)'),
                n = -2.81,
                Ea = (8619, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 400,
    label = "CH3OCH2 + O2 => CH2O + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.01e+21, 'cm^3/(mol*s)'),
                n = -3.18,
                Ea = (3067, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.73e+23, 'cm^3/(mol*s)'),
                n = -3.55,
                Ea = (4050, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.04e+31, 'cm^3/(mol*s)'),
                n = -5.76,
                Ea = (11594, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.99e+31, 'cm^3/(mol*s)'),
                n = -5.87,
                Ea = (12710, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.39e+30, 'cm^3/(mol*s)'),
                n = -5.59,
                Ea = (14517, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.09e+30, 'cm^3/(mol*s)'),
                n = -5.3,
                Ea = (15051, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.58e+28, 'cm^3/(mol*s)'),
                n = -4.88,
                Ea = (15664, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.41e+27, 'cm^3/(mol*s)'),
                n = -4.55,
                Ea = (16107, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 401,
    label = "CH3OCH2O2 <=> CH2OCH2O2H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.94e+29, 's^-1'), n=-6.99, Ea=(22446, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.07e+27, 's^-1'), n=-6.16, Ea=(21619, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.52e+25, 's^-1'), n=-4.76, Ea=(22691, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.97e+24, 's^-1'), n=-4.48, Ea=(22868, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.44e+21, 's^-1'), n=-3.38, Ea=(22386, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.52e+19, 's^-1'), n=-2.74, Ea=(21803, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.72e+16, 's^-1'), n=-1.82, Ea=(20829, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.7e+14, 's^-1'), n=-1.13, Ea=(20034, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 402,
    label = "CH3OCH2O2 => CH2O + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.06e+36, 's^-1'), n=-8.32, Ea=(33415, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.07e+39, 's^-1'), n=-8.86, Ea=(35842, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.12e+40, 's^-1'), n=-8.42, Ea=(39835, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.72e+38, 's^-1'), n=-8.04, Ea=(39923, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.28e+35, 's^-1'), n=-6.97, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.6e+34, 's^-1'), n=-6.46, Ea=(39850, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.32e+31, 's^-1'), n=-5.75, Ea=(39719, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.22e+30, 's^-1'), n=-5.2, Ea=(39549, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 403,
    label = "CH2OCH2O2H => CH2O + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.66e+23, 's^-1'), n=-4.53, Ea=(22243, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.3e+25, 's^-1'), n=-4.93, Ea=(24158, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.81e+22, 's^-1'), n=-3.5, Ea=(23156, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.98e+22, 's^-1'), n=-3.35, Ea=(23062, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.46e+22, 's^-1'), n=-3.22, Ea=(23559, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.09e+22, 's^-1'), n=-3.14, Ea=(23899, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.59e+22, 's^-1'), n=-2.94, Ea=(24262, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.4e+22, 's^-1'), n=-2.72, Ea=(24407, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 404,
    label = "CH2OCH2O2H + O2 <=> O2CH2OCH2O2H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (9.42e+12, 'cm^3/(mol*s)'),
                n = -1.68,
                Ea = (-4998, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.16e+16, 'cm^3/(mol*s)'),
                n = -2.5,
                Ea = (-2753, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.06e+22, 'cm^3/(mol*s)'),
                n = -3.3,
                Ea = (3389, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.48e+20, 'cm^3/(mol*s)'),
                n = -2.79,
                Ea = (3131, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.86e+16, 'cm^3/(mol*s)'),
                n = -1.48,
                Ea = (1873, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.55e+14, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (1312, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.68e+13, 'cm^3/(mol*s)'),
                n = -0.54,
                Ea = (727, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.87e+12, 'cm^3/(mol*s)'),
                n = -0.32,
                Ea = (428, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 405,
    label = "CH2OCH2O2H + O2 <=> HO2CH2OCHO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.9e+20, 'cm^3/(mol*s)'),
                n = -2.88,
                Ea = (3234, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.06e+23, 'cm^3/(mol*s)'),
                n = -3.59,
                Ea = (5116, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.45e+29, 'cm^3/(mol*s)'),
                n = -5.29,
                Ea = (12791, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.44e+28, 'cm^3/(mol*s)'),
                n = -4.92,
                Ea = (12891, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.42e+23, 'cm^3/(mol*s)'),
                n = -3.68,
                Ea = (12049, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.04e+22, 'cm^3/(mol*s)'),
                n = -3.16,
                Ea = (11505, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.95e+19, 'cm^3/(mol*s)'),
                n = -2.6,
                Ea = (10861, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.96e+18, 'cm^3/(mol*s)'),
                n = -2.31,
                Ea = (10500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 406,
    label = "O2CH2OCH2O2H <=> HO2CH2OCHO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.05e+23, 's^-1'), n=-4.88, Ea=(18805, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.84e+26, 's^-1'), n=-5.32, Ea=(22533, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.07e+16, 's^-1'), n=-1.81, Ea=(21175, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.66e+14, 's^-1'), n=-1.11, Ea=(20310, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.69e+10, 's^-1'), n=0.18, Ea=(18604, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.11e+09, 's^-1'), n=0.54, Ea=(18100, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.07e+08, 's^-1'), n=0.84, Ea=(17661, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.86e+07, 's^-1'), n=0.98, Ea=(17467, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 407,
    label = "CH3OCH2O2 + CH3OCH2O2 => O2 + CH3OCH2O + CH3OCH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.547e+23, 'cm^3/(mol*s)'), n=-4.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 408,
    label = "CH3OCH2O2 + CH2O <=> CH3OCH2O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 409,
    label = "CH3OCH2O2 + CH3CHO <=> CH3OCH2O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 410,
    label = "CH3OCH2O + OH <=> CH3OCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 411,
    label = "HO2CH2OCHO <=> OCH2OCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 412,
    label = "CH2O + OCHO <=> OCH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 413,
    label = "OCH2OCHO <=> HOCH2OCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 414,
    label = "HOCH2OCO <=> CH2OH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.117e+17, 's^-1'), n=-1.526, Ea=(20771.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 415,
    label = "HOCH2OCO <=> HOCH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.92e+18, 's^-1'), n=-1.965, Ea=(19619, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 416,
    label = "CH3O + CH2O <=> CH3OCH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 417,
    label = "CH3OCH2O + O2 <=> CH3OCHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.38e-19, 'cm^3/(mol*s)'),
        n = 9.5,
        Ea = (-5501, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 418,
    label = "CH3OCH2O <=> CH3OCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 's^-1'), n=0.004, Ea=(26136.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 419,
    label = "CH3O + HCO <=> CH3OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 420,
    label = "CH3O + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 421,
    label = "CH3 + OCHO <=> CH3OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 422,
    label = "CH2OCHO + H <=> CH3OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 423,
    label = "CH3OCO + H <=> CH3OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 424,
    label = "CH3OCHO + O2 <=> CH3OCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(49700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 425,
    label = "CH3OCHO + O2 <=> CH2OCHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(52000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 426,
    label = "CH3OCHO + OH <=> CH3OCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(934, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 427,
    label = "CH3OCHO + OH <=> CH2OCHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 428,
    label = "CH3OCHO + HO2 <=> CH3OCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 429,
    label = "CH3OCHO + HO2 <=> CH2OCHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 430,
    label = "CH3OCHO + O <=> CH3OCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(275500, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 431,
    label = "CH3OCHO + O <=> CH2OCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 432,
    label = "CH3OCHO + H <=> CH3OCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(650000, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 433,
    label = "CH3OCHO + H <=> CH2OCHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 434,
    label = "CH3OCHO + CH3 <=> CH3OCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.755, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 435,
    label = "CH3OCHO + CH3 <=> CH2OCHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.452, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 436,
    label = "CH3OCHO + CH3O <=> CH3OCO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.48e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 437,
    label = "CH3OCHO + CH3O <=> CH2OCHO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 438,
    label = "CH3OCHO + CH3O2 <=> CH3OCO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 439,
    label = "CH3OCHO + CH3O2 <=> CH2OCHO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 440,
    label = "CH3OCHO + HCO <=> CH3OCO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 441,
    label = "CH3OCHO + HCO <=> CH2OCHO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(102500, 'cm^3/(mol*s)'), n=2.5, Ea=(18430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 442,
    label = "CH3OCO <=> CH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.629e+12, 's^-1'), n=-0.18, Ea=(40670, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 443,
    label = "CH3OCO <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.05, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.72e+12, 's^-1'), n=-1.31, Ea=(9416.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.25e+16, 's^-1'), n=-1.83, Ea=(11340.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.04e+18, 's^-1'), n=-2.1, Ea=(12826.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.69e+17, 's^-1'), n=-1.81, Ea=(13656.7, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 444,
    label = "CH3OCO <=> CH3O + CO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.05, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1030, 's^-1'), n=1.29, Ea=(25401, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(409000, 's^-1'), n=0.81, Ea=(21969.1, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.02e+14, 's^-1'), n=-1.72, Ea=(21767.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.825e+22, 's^-1'), n=-3.44, Ea=(23592.4, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 445,
    label = "CH2O + HCO <=> CH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 446,
    label = "C3H8 <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.29e+37, 's^-1'), n=-5.84, Ea=(97380, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.64e+74, 'cm^3/(mol*s)'),
            n = -15.74,
            Ea = (98714, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.31,
        T3 = (50, 'K'),
        T1 = (3000, 'K'),
        T2 = (9000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 447,
    label = "NC3H7 + H <=> C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 448,
    label = "IC3H7 + H <=> C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 449,
    label = "C3H8 + IC3H7 <=> NC3H7 + C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(12900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 450,
    label = "C3H8 + O2 <=> IC3H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 451,
    label = "C3H8 + H <=> IC3H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 452,
    label = "C3H8 + O <=> IC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(549000, 'cm^3/(mol*s)'), n=2.5, Ea=(3140, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 453,
    label = "C3H8 + OH <=> IC3H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 454,
    label = "C3H8 + HO2 <=> IC3H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(63.2, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 455,
    label = "C3H8 + CH3 <=> IC3H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(64000, 'cm^3/(mol*s)'), n=2.17, Ea=(7520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 456,
    label = "C3H8 + C2H3 <=> IC3H7 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 457,
    label = "C3H8 + C2H5 <=> IC3H7 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 458,
    label = "C3H8 + C3H5-A <=> IC3H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(16200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 459,
    label = "C3H8 + CH3O <=> IC3H7 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 460,
    label = "C3H8 + CH3O2 <=> IC3H7 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10.19, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 461,
    label = "C3H8 + C2H5O2 <=> IC3H7 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10.19, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 462,
    label = "C3H8 + NC3H7O2 <=> IC3H7 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 463,
    label = "C3H8 + CH3CO3 <=> IC3H7 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 464,
    label = "C3H8 + O2CHO <=> IC3H7 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14750, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 465,
    label = "C3H8 + IC3H7O2 <=> IC3H7 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 466,
    label = "C3H8 + O2 <=> NC3H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 467,
    label = "C3H8 + H <=> NC3H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(349000, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 468,
    label = "C3H8 + O <=> NC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.71e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5505, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 469,
    label = "C3H8 + OH <=> NC3H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.054e+10, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 470,
    label = "C3H8 + HO2 <=> NC3H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 471,
    label = "C3H8 + CH3 <=> NC3H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 472,
    label = "C3H8 + C2H3 <=> NC3H7 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 473,
    label = "C3H8 + C2H5 <=> NC3H7 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 474,
    label = "C3H8 + C3H5-A <=> NC3H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 475,
    label = "C3H8 + CH3O <=> NC3H7 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 476,
    label = "C3H8 + CH3O2 <=> NC3H7 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 477,
    label = "C3H8 + C2H5O2 <=> NC3H7 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 478,
    label = "C3H8 + NC3H7O2 <=> NC3H7 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 479,
    label = "C3H8 + IC3H7O2 <=> NC3H7 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 480,
    label = "C3H8 + CH3CO3 <=> NC3H7 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 481,
    label = "C3H8 + O2CHO <=> NC3H7 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(55200, 'cm^3/(mol*s)'), n=2.55, Ea=(16480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 482,
    label = "IC3H7 + H <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 483,
    label = "IC3H7 + OH <=> C3H6 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 484,
    label = "IC3H7 + O <=> CH3COCH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.818e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 485,
    label = "IC3H7 + O <=> CH3CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.818e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 486,
    label = "NC3H7 + HO2 <=> NC3H7O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 487,
    label = "NC3H7 + CH3O2 <=> NC3H7O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 488,
    label = "IC3H7 + HO2 <=> IC3H7O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 489,
    label = "IC3H7 + CH3O2 <=> IC3H7O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 490,
    label = "C2H5 + CH2O <=> NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3496, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 491,
    label = "C2H5CHO + H <=> NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(6260, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 492,
    label = "CH3 + CH3CHO <=> IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9256, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 493,
    label = "CH3COCH3 + H <=> IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 494,
    label = "IC3H7O + O2 <=> CH3COCH3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.09e+09, 'cm^3/(mol*s)'), n=0, Ea=(390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 495,
    label = "NC3H7 + O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e-19, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 496,
    label = "NC3H7 + O2 <=> NC3H7O2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (9.2e+08, 'cm^3/(mol*s)'),
                n = 0.405,
                Ea = (-4398.65, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.45e+14, 'cm^3/(mol*s)'),
                n = -0.984,
                Ea = (-1710.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.09e+13, 'cm^3/(mol*s)'),
                n = -0.499,
                Ea = (-938.423, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.15e+20, 'cm^3/(mol*s)'),
                n = -2.42,
                Ea = (2451.26, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.07e+16, 'cm^3/(mol*s)'),
                n = -1.3,
                Ea = (803.419, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 497,
    label = "IC3H7 + O2 <=> IC3H7O2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (733000, 'cm^3/(mol*s)'),
                n = 1.33,
                Ea = (-6345.64, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.24e+11, 'cm^3/(mol*s)'),
                n = -0.105,
                Ea = (-3697.87, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -2.02,
                Ea = (-498.567, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.74e+27, 'cm^3/(mol*s)'),
                n = -4.85,
                Ea = (3779.82, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.67e+29, 'cm^3/(mol*s)'),
                n = -5.15,
                Ea = (5036.45, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 498,
    label = "IC3H7O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.224e+09, 's^-1'), n=1.28, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 499,
    label = "NC3H7O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.24e+08, 's^-1'), n=1.25, Ea=(29600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 500,
    label = "NC3H7O2 <=> C3H6OOH1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.09e+08, 's^-1'), n=1.1, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 501,
    label = "NC3H7O2 <=> C3H6OOH1-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.566e+06, 's^-1'), n=1.6, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 502,
    label = "IC3H7O2 <=> C3H6OOH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.917e+09, 's^-1'), n=1.1, Ea=(33500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 503,
    label = "C3H6OOH1-2 <=> C3H6O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+09, 's^-1'), n=1.05, Ea=(11300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 504,
    label = "C3H6OOH1-3 <=> C3H6O1-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.64e+09, 's^-1'), n=0.71, Ea=(18500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 505,
    label = "C3H6OOH1-2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.34e+10, 's^-1'), n=0.77, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 506,
    label = "C3H6OOH1-3 => OH + CH2O + C2H4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.89e+09, 's^-1'), n=1.3, Ea=(26700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 507,
    label = "C3H6OOH2-1 <=> C2H3OOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.56e+10, 's^-1'), n=0.85, Ea=(30700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 508,
    label = "C3H6OOH1-2 => C2H4 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.31e+33, 's^-1'), n=-7.01, Ea=(48120, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 509,
    label = "C3H6OOH1-2 + O2 <=> C3H6OOH1-2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.744e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 510,
    label = "C3H6OOH1-3 + O2 <=> C3H6OOH1-3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 511,
    label = "C3H6OOH2-1 + O2 <=> C3H6OOH2-1O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 512,
    label = "C3H6OOH1-2O2 <=> C3H51-2,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.917e+09, 's^-1'), n=1.1, Ea=(33500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 513,
    label = "C3H6OOH1-3O2 <=> C3H52-1,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.009e+08, 's^-1'), n=1.1, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 514,
    label = "C3H6OOH2-1O2 <=> C3H51-2,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.566e+06, 's^-1'), n=1.6, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 515,
    label = "C3H51-2,3OOH <=> AC3H5OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.56e+13, 's^-1'), n=-0.49, Ea=(17770, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 516,
    label = "C3H52-1,3OOH <=> AC3H5OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+14, 's^-1'), n=-0.63, Ea=(17250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 517,
    label = "C3H51-2,3OOH <=> C3H5O1-2OOH-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.45e+09, 's^-1'), n=0.86, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 518,
    label = "C3H51-2,3OOH <=> C3H5O1-3OOH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.64e+09, 's^-1'), n=0.71, Ea=(18500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 519,
    label = "C3H52-1,3OOH <=> C3H5O1-2OOH-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+09, 's^-1'), n=1.05, Ea=(11300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 520,
    label = "C3H5O1-2OOH-3 => CH2CHO + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 521,
    label = "C3H5O1-3OOH-2 => CH2CHO + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 522,
    label = "C3H6OOH1-2O2 <=> C3KET12 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 523,
    label = "C3H6OOH1-3O2 <=> C3KET13 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 524,
    label = "C3H6OOH2-1O2 <=> C3KET21 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(23850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 525,
    label = "C3KET12 => CH3CHO + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.5e+15, 's^-1'), n=0, Ea=(42540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 526,
    label = "C3KET13 => CH2O + CH2CHO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 527,
    label = "C3KET21 => CH2O + CH3CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 529,
    label = "C2H3OOH <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+14, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 530,
    label = "C2H3OOH => CH2CO + H + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.59e+20, 's^-1'), n=-1.5, Ea=(42879.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 531,
    label = "C3KET21 <=> CH3COCH2O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.49e+58, 's^-1'), n=-13.9, Ea=(54266.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+54, 's^-1'), n=-12.4, Ea=(54193.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.36e+46, 's^-1'), n=-9.81, Ea=(52468.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.39e+36, 's^-1'), n=-6.54, Ea=(49429, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.28e+27, 's^-1'), n=-3.61, Ea=(46333.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 532,
    label = "NC3H7O2H <=> NC3H7O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 533,
    label = "NC3H7O2 + H2 <=> NC3H7O2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 534,
    label = "NC3H7O2 + HO2 <=> NC3H7O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 535,
    label = "NC3H7O2 + CH2O <=> NC3H7O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 536,
    label = "NC3H7O2 + CH4 <=> NC3H7O2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 537,
    label = "NC3H7O2 + CH3OH <=> NC3H7O2H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 538,
    label = "NC3H7O2 + CH3CHO <=> NC3H7O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 539,
    label = "NC3H7O2 + C2H4 <=> NC3H7O2H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 540,
    label = "NC3H7O2 + C2H6 <=> NC3H7O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 541,
    label = "NC3H7O2 + C2H3CHO <=> NC3H7O2H + C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 542,
    label = "NC3H7O2 + C2H5CHO <=> NC3H7O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 543,
    label = "NC3H7O2 + NC3H7O2 => NC3H7O + NC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 544,
    label = "NC3H7O2 + CH3CO3 => NC3H7O + CH3CO2 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 545,
    label = "NC3H7O2 + C2H5O2 => NC3H7O + C2H5O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 546,
    label = "NC3H7O2 + CH3 <=> NC3H7O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 547,
    label = "NC3H7O2 + C2H5 <=> NC3H7O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 548,
    label = "NC3H7O2 + IC3H7 <=> NC3H7O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 549,
    label = "NC3H7O2 + NC3H7 <=> NC3H7O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 550,
    label = "NC3H7O2 + C3H5-A <=> NC3H7O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 551,
    label = "NC3H7O2 + CH3O2 => NC3H7O + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 552,
    label = "IC3H7O + OH <=> IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+15, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 553,
    label = "IC3H7O2 + H2 <=> IC3H7O2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 554,
    label = "IC3H7O2 + HO2 <=> IC3H7O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 555,
    label = "IC3H7O2 + CH2O <=> IC3H7O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 556,
    label = "IC3H7O2 + CH4 <=> IC3H7O2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 557,
    label = "IC3H7O2 + CH3CHO <=> IC3H7O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 558,
    label = "IC3H7O2 + C2H4 <=> IC3H7O2H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 559,
    label = "IC3H7O2 + CH3OH <=> IC3H7O2H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 560,
    label = "IC3H7O2 + C2H6 <=> IC3H7O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 561,
    label = "IC3H7O2 + C2H3CHO <=> IC3H7O2H + C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 562,
    label = "IC3H7O2 + C2H5CHO <=> IC3H7O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 563,
    label = "IC3H7O2 + CH3O2 => IC3H7O + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 564,
    label = "IC3H7O2 + CH3CO3 => IC3H7O + CH3CO2 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 565,
    label = "IC3H7O2 + C2H5O2 => IC3H7O + C2H5O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 566,
    label = "IC3H7O2 + IC3H7O2 => O2 + IC3H7O + IC3H7O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 567,
    label = "IC3H7O2 + NC3H7O2 => IC3H7O + NC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 568,
    label = "IC3H7O2 + CH3 <=> IC3H7O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 569,
    label = "IC3H7O2 + C2H5 <=> IC3H7O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 570,
    label = "IC3H7O2 + IC3H7 <=> IC3H7O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 571,
    label = "IC3H7O2 + NC3H7 <=> IC3H7O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 572,
    label = "IC3H7O2 + C3H5-A <=> IC3H7O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 573,
    label = "C3H6O1-2 <=> C2H4 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 574,
    label = "C3H6O1-2 + OH => CH2O + C2H3 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 575,
    label = "C3H6O1-2 + H => CH2O + C2H3 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.63e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 576,
    label = "C3H6O1-2 + O => CH2O + C2H3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 577,
    label = "C3H6O1-2 + HO2 => CH2O + C2H3 + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 578,
    label = "C3H6O1-2 + CH3O2 => CH2O + C2H3 + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 579,
    label = "C3H6O1-2 + CH3 => CH2O + C2H3 + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 580,
    label = "C3H6O1-3 <=> C2H4 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 581,
    label = "C3H6O1-3 + OH => CH2O + C2H3 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 582,
    label = "C3H6O1-3 + O => CH2O + C2H3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 583,
    label = "C3H6O1-3 + H => CH2O + C2H3 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.63e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 584,
    label = "C3H6O1-3 + CH3O2 => CH2O + C2H3 + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 585,
    label = "C3H6O1-3 + HO2 => CH2O + C2H3 + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 586,
    label = "C3H6O1-3 + CH3 => CH2O + C2H3 + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 587,
    label = "C2H3 + CH3 <=> C3H6",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.27e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9769.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1341, 'K'),
        T1 = (60000, 'K'),
        T2 = (10140, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 588,
    label = "CH2(S) + C2H4 <=> CC3H6",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.44e+51, 'cm^3/(mol*s)'),
                        n = -13.1,
                        Ea = (14200, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.38e+54, 'cm^3/(mol*s)'),
                        n = -13.6,
                        Ea = (16500, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.35e+54, 'cm^3/(mol*s)'),
                        n = -13,
                        Ea = (18900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.73e+47, 'cm^3/(mol*s)'),
                        n = -10.8,
                        Ea = (14200, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.71e+50, 'cm^3/(mol*s)'),
                        n = -11.2,
                        Ea = (16700, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (6.16e+40, 'cm^3/(mol*s)'),
                        n = -10.5,
                        Ea = (5428.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.93e+41, 'cm^3/(mol*s)'),
                        n = -10.3,
                        Ea = (6188.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.81e+37, 'cm^3/(mol*s)'),
                        n = -8.55,
                        Ea = (5521, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.26e+37, 'cm^3/(mol*s)'),
                        n = -8.32,
                        Ea = (4770.2, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.68e+35, 'cm^3/(mol*s)'),
                        n = -7.37,
                        Ea = (4689.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 589,
    label = "CH2(S) + C2H4 <=> C3H6",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.82e+57, 'cm^3/(mol*s)'),
                        n = -14.3,
                        Ea = (17100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.84e+59, 'cm^3/(mol*s)'),
                        n = -14.4,
                        Ea = (18400, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.13e+58, 'cm^3/(mol*s)'),
                        n = -13.5,
                        Ea = (20400, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.48e+52, 'cm^3/(mol*s)'),
                        n = -11.6,
                        Ea = (20700, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.07e+47, 'cm^3/(mol*s)'),
                        n = -9.85,
                        Ea = (22100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.15e+45, 'cm^3/(mol*s)'),
                        n = -11.1,
                        Ea = (6145.2, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.83e+45, 'cm^3/(mol*s)'),
                        n = -10.7,
                        Ea = (6638.5, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.3e+40, 'cm^3/(mol*s)'),
                        n = -8.77,
                        Ea = (5863.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.27e+32, 'cm^3/(mol*s)'),
                        n = -6.14,
                        Ea = (4317.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.28e+24, 'cm^3/(mol*s)'),
                        n = -3.49,
                        Ea = (2529.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 590,
    label = "CH2(S) + C2H4 <=> C3H5-A + H",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.2e+19, 'cm^3/(mol*s)'),
                        n = -2.06,
                        Ea = (1150, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.27e+21, 'cm^3/(mol*s)'),
                        n = -2.44,
                        Ea = (2650, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.44e+35, 'cm^3/(mol*s)'),
                        n = -6.55,
                        Ea = (13900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.18e+28, 'cm^3/(mol*s)'),
                        n = -4.09,
                        Ea = (14000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.51e+26, 'cm^3/(mol*s)'),
                        n = -3.58,
                        Ea = (18900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.08e+07, 'cm^3/(mol*s)'),
                        n = 1.62,
                        Ea = (-3174.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (137000, 'cm^3/(mol*s)'),
                        n = 2.15,
                        Ea = (-3799.2, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.89e+14, 'cm^3/(mol*s)'),
                        n = -0.42,
                        Ea = (1237.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.45e+10, 'cm^3/(mol*s)'),
                        n = 0.67,
                        Ea = (750.93, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(181, 'cm^3/(mol*s)'), n=2.97, Ea=(-746.03, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 591,
    label = "CH2(S) + C2H4 <=> C2H3 + CH3",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.77e+19, 'cm^3/(mol*s)'),
                        n = -1.94,
                        Ea = (6790, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.68e+19, 'cm^3/(mol*s)'),
                        n = -1.8,
                        Ea = (4310, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.16e+24, 'cm^3/(mol*s)'),
                        n = -3.19,
                        Ea = (9760, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.89e+24, 'cm^3/(mol*s)'),
                        n = -3.07,
                        Ea = (13900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.36e+29, 'cm^3/(mol*s)'),
                        n = -4.28,
                        Ea = (23800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.3e+12, 'cm^3/(mol*s)'),
                        n = 0.19,
                        Ea = (-110.41, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.26e+11, 'cm^3/(mol*s)'),
                        n = 0.54,
                        Ea = (47.81, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.92e+09, 'cm^3/(mol*s)'),
                        n = 1.02,
                        Ea = (599.77, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.47e+08, 'cm^3/(mol*s)'),
                        n = 1.33,
                        Ea = (1228.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.11e+10, 'cm^3/(mol*s)'),
                        n = 0.55,
                        Ea = (5506.5, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 592,
    label = "C2H3 + CH3 <=> C3H5-A + H",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.12e+29, 'cm^3/(mol*s)'),
                        n = -4.95,
                        Ea = (8000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.86e+30, 'cm^3/(mol*s)'),
                        n = -5.03,
                        Ea = (11300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.3e+29, 'cm^3/(mol*s)'),
                        n = -4.57,
                        Ea = (14400, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.32e+30, 'cm^3/(mol*s)'),
                        n = -4.54,
                        Ea = (19300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.16e+28, 'cm^3/(mol*s)'),
                        n = -4.03,
                        Ea = (23800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (5.73e+15, 'cm^3/(mol*s)'),
                        n = -0.77,
                        Ea = (1195.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.06e+13, 'cm^3/(mol*s)'),
                        n = -0.074,
                        Ea = (1428.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.48e+10, 'cm^3/(mol*s)'),
                        n = 0.6,
                        Ea = (1421.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.1e+06, 'cm^3/(mol*s)'),
                        n = 1.71,
                        Ea = (1056.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (0.137, 'cm^3/(mol*s)'),
                        n = 3.91,
                        Ea = (-353.55, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 593,
    label = "C3H6 <=> C2H3 + CH3",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.88e+78, 's^-1'), n=-18.7, Ea=(130000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.73e+76, 's^-1'), n=-17.9, Ea=(132000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.8e+75, 's^-1'), n=-17.2, Ea=(134000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.12e+71, 's^-1'), n=-15.8, Ea=(136000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.15e+64, 's^-1'), n=-13.4, Ea=(135000, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.69e+59, 's^-1'), n=-13.6, Ea=(113290, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2e+60, 's^-1'), n=-13.7, Ea=(114890, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.7e+54, 's^-1'), n=-11.8, Ea=(113840, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.06e+47, 's^-1'), n=-9.27, Ea=(111510, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.29e+38, 's^-1'), n=-6.7, Ea=(108740, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 594,
    label = "C3H6 <=> C3H5-A + H",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(9.16e+74, 's^-1'), n=-17.6, Ea=(120000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.73e+70, 's^-1'), n=-16, Ea=(120000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.08e+71, 's^-1'), n=-15.9, Ea=(124860, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.4e+65, 's^-1'), n=-14.2, Ea=(125000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.05e+56, 's^-1'), n=-11.5, Ea=(122000, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(2.98e+54, 's^-1'), n=-12.3, Ea=(101200, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.37e+43, 's^-1'), n=-8.87, Ea=(96365, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.28e+42, 's^-1'), n=-8.51, Ea=(98004, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.73e+35, 's^-1'), n=-6.26, Ea=(95644, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.34e+28, 's^-1'), n=-4.06, Ea=(93114, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 595,
    label = "C3H6 <=> CC3H6",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.26e+64, 's^-1'), n=-15.6, Ea=(95000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.94e+67, 's^-1'), n=-16.2, Ea=(101000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.14e+68, 's^-1'), n=-16.2, Ea=(106000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.7e+66, 's^-1'), n=-15.3, Ea=(109000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.45e+62, 's^-1'), n=-13.6, Ea=(110000, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(4.84e+41, 's^-1'), n=-9.62, Ea=(79528, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.07e+44, 's^-1'), n=-10.2, Ea=(82671, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.15e+47, 's^-1'), n=-10.6, Ea=(85502, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.33e+39, 's^-1'), n=-7.98, Ea=(83303, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.97e+31, 's^-1'), n=-5.6, Ea=(80987, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 596,
    label = "CC3H6 <=> C3H5-A + H",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(2.33e+63, 's^-1'), n=-14.6, Ea=(103000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.03e+63, 's^-1'), n=-14.4, Ea=(107000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.07e+64, 's^-1'), n=-14.3, Ea=(112000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.92e+61, 's^-1'), n=-13.2, Ea=(115000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.82e+57, 's^-1'), n=-11.7, Ea=(118000, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.12e+40, 's^-1'), n=-8.37, Ea=(85836, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.06e+41, 's^-1'), n=-8.33, Ea=(88499, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.23e+43, 's^-1'), n=-8.88, Ea=(92907, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.27e+39, 's^-1'), n=-7.33, Ea=(93401, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.45e+28, 's^-1'), n=-4.02, Ea=(90995, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 597,
    label = "CC3H6 <=> C2H3 + CH3",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(8.31e+64, 's^-1'), n=-15.1, Ea=(111000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.29e+64, 's^-1'), n=-14.7, Ea=(114000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e+70, 's^-1'), n=-15.7, Ea=(122000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.66e+67, 's^-1'), n=-14.6, Ea=(124000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.87e+62, 's^-1'), n=-13.1, Ea=(127000, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.51e+49, 's^-1'), n=-11, Ea=(99748, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.05e+45, 's^-1'), n=-9.46, Ea=(99275, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.39e+50, 's^-1'), n=-10.6, Ea=(104220, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.76e+47, 's^-1'), n=-9.43, Ea=(104930, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.88e+39, 's^-1'), n=-6.93, Ea=(103980, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 598,
    label = "C3H5-T + H <=> C3H6",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.96e+60, 'cm^3/(mol*s)'),
                        n = -15.2,
                        Ea = (18000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.2e+62, 'cm^3/(mol*s)'),
                        n = -15.1,
                        Ea = (20100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.31e+60, 'cm^3/(mol*s)'),
                        n = -14,
                        Ea = (21900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.69e+54, 'cm^3/(mol*s)'),
                        n = -12,
                        Ea = (22100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.15e+50, 'cm^3/(mol*s)'),
                        n = -10.4,
                        Ea = (23300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.49e+48, 'cm^3/(mol*s)'),
                        n = -12,
                        Ea = (7203.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.76e+46, 'cm^3/(mol*s)'),
                        n = -11.1,
                        Ea = (7629.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.09e+40, 'cm^3/(mol*s)'),
                        n = -8.66,
                        Ea = (6447.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.38e+31, 'cm^3/(mol*s)'),
                        n = -5.73,
                        Ea = (4506, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.69e+25, 'cm^3/(mol*s)'),
                        n = -3.83,
                        Ea = (3250.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 599,
    label = "C3H5-T + H <=> C3H5-A + H",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.11e+17, 'cm^3/(mol*s)'),
                        n = -1.08,
                        Ea = (1290, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.05e+29, 'cm^3/(mol*s)'),
                        n = -4.91,
                        Ea = (8540, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.98e+30, 'cm^3/(mol*s)'),
                        n = -4.79,
                        Ea = (12000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.22e+28, 'cm^3/(mol*s)'),
                        n = -4.14,
                        Ea = (15400, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.28e+29, 'cm^3/(mol*s)'),
                        n = -4.12,
                        Ea = (20900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (6410, 'cm^3/(mol*s)'),
                        n = 2.61,
                        Ea = (-3778.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.19e+14, 'cm^3/(mol*s)'),
                        n = -0.3,
                        Ea = (1090.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.17e+11, 'cm^3/(mol*s)'),
                        n = 0.49,
                        Ea = (1184.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.79e+09, 'cm^3/(mol*s)'),
                        n = 1.09,
                        Ea = (1187.5, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(6750, 'cm^3/(mol*s)'), n=2.7, Ea=(373.8, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 600,
    label = "C3H5-T + H <=> C2H3 + CH3",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (3.31e+16, 'cm^3/(mol*s)'),
                        n = -0.69,
                        Ea = (5200, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.04e+16, 'cm^3/(mol*s)'),
                        n = -0.81,
                        Ea = (4800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.01e+24, 'cm^3/(mol*s)'),
                        n = -2.86,
                        Ea = (10900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.75e+26, 'cm^3/(mol*s)'),
                        n = -3.31,
                        Ea = (15800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.15e+32, 'cm^3/(mol*s)'),
                        n = -4.83,
                        Ea = (26000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.04e+13, 'cm^3/(mol*s)'),
                        n = -0.14,
                        Ea = (1150, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.17e+10, 'cm^3/(mol*s)'),
                        n = 0.67,
                        Ea = (673.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.97e+08, 'cm^3/(mol*s)'),
                        n = 1.36,
                        Ea = (1596.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.41e+07, 'cm^3/(mol*s)'),
                        n = 1.57,
                        Ea = (2108.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.7e+12, 'cm^3/(mol*s)'),
                        n = 0.32,
                        Ea = (6791.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 601,
    label = "C3H6 <=> C3H5-S + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.71e+69, 's^-1'), n=-16.09, Ea=(140000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 602,
    label = "C3H6 + H <=> C3H5-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (364400, 'cm^3/(mol*s)'),
        n = 2.455,
        Ea = (4361.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 603,
    label = "C3H6 + O2 <=> C3H5-A + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.96e+19, 'cm^3/(mol*s)'),
        n = -1.67,
        Ea = (46192.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 604,
    label = "C3H6 + O <=> C3H5-A + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 605,
    label = "C3H6 + OH <=> C3H5-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.46e+06, 'cm^3/(mol*s)'),
        n = 2.072,
        Ea = (1050.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 606,
    label = "C3H6 + HO2 <=> C3H5-A + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0307, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 607,
    label = "C3H6 + CH3 <=> C3H5-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 608,
    label = "C3H6 + CH3O <=> C3H5-A + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 609,
    label = "C3H6 + CH3O2 <=> C3H5-A + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0768, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 610,
    label = "C3H6 + C2H5 <=> C3H5-A + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 611,
    label = "C3H6 + C2H5O2 <=> C3H5-A + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0768, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 612,
    label = "C3H6 + CH3CO3 <=> C3H5-A + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0768, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 613,
    label = "C3H6 + NC3H7O2 <=> C3H5-A + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0768, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 614,
    label = "C3H6 + IC3H7O2 <=> C3H5-A + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0768, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 615,
    label = "C3H6 + H <=> C3H5-T + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (149.8, 'cm^3/(mol*s)'),
        n = 3.381,
        Ea = (8909.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 616,
    label = "C3H6 + O <=> C3H5-T + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7632, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 617,
    label = "C3H6 + OH <=> C3H5-T + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.979,
        Ea = (2235.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 618,
    label = "C3H6 + HO2 <=> C3H5-T + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15600, 'cm^3/(mol*s)'),
        n = 2.82,
        Ea = (24427.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 619,
    label = "C3H6 + O2 <=> C3H5-T + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(58770, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 620,
    label = "C3H6 + CH3 <=> C3H5-T + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 621,
    label = "C3H6 + H <=> C3H5-S + H2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (510.1, 'cm^3/(mol*s)'),
                n = 3.234,
                Ea = (12357, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (396.9, 'cm^3/(mol*s)'),
                n = 3.252,
                Ea = (12007, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 622,
    label = "C3H6 + O2 <=> C3H5-S + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(62270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 623,
    label = "C3H6 + O <=> C3H5-S + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8959.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 624,
    label = "C3H6 + OH <=> C3H5-S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (186000, 'cm^3/(mol*s)'),
        n = 2.369,
        Ea = (2502, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 625,
    label = "C3H6 + HO2 <=> C3H5-S + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (957, 'cm^3/(mol*s)'),
        n = 3.059,
        Ea = (20798.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 626,
    label = "C3H6 + CH3 <=> C3H5-S + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.348, 'cm^3/(mol*s)'), n=3.5, Ea=(12850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 627,
    label = "C3H6 + O <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.45e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 628,
    label = "C3H6 + O => CH2CO + CH3 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.05e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 629,
    label = "C3H6 + O => CH3CHCO + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.05e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 630,
    label = "C3H6 + H <=> NC3H7",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (7.99e+81, 'cm^3/(mol*s)'),
                        n = -23.161,
                        Ea = (22239, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.24e+68, 'cm^3/(mol*s)'),
                        n = -18.427,
                        Ea = (19665, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.04e+49, 'cm^3/(mol*s)'),
                        n = -11.5,
                        Ea = (15359, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.2e+41, 'cm^3/(mol*s)'),
                        n = -8.892,
                        Ea = (14637, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.85e+26, 'cm^3/(mol*s)'),
                        n = -5.83,
                        Ea = (3865.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.82e+30, 'cm^3/(mol*s)'),
                        n = -6.49,
                        Ea = (5470.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.78e+28, 'cm^3/(mol*s)'),
                        n = -5.57,
                        Ea = (5625.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.46e+25, 'cm^3/(mol*s)'),
                        n = -4.28,
                        Ea = (5247.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.22e+27, 'cm^3/(mol*s)'),
                        n = -4.39,
                        Ea = (9345.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 631,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.54e+09, 'cm^3/(mol*s)'),
                        n = 1.35,
                        Ea = (2542, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.88e+10, 'cm^3/(mol*s)'),
                        n = 0.87,
                        Ea = (3599.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.67e+12, 'cm^3/(mol*s)'),
                        n = 0.47,
                        Ea = (5431.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.25e+22, 'cm^3/(mol*s)'),
                        n = -2.6,
                        Ea = (12898, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.32e+23, 'cm^3/(mol*s)'),
                        n = -2.42,
                        Ea = (16500, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (124000, 'cm^3/(mol*s)'),
                        n = 2.52,
                        Ea = (3679.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(2510, 'cm^3/(mol*s)'), n=2.91, Ea=(3980.9, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 632,
    label = "C3H6 + H <=> IC3H7",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.35e+44, 'cm^3/(mol*s)'),
                        n = -10.68,
                        Ea = (8196.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.11e+57, 'cm^3/(mol*s)'),
                        n = -14.23,
                        Ea = (15147, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.26e+61, 'cm^3/(mol*s)'),
                        n = -14.94,
                        Ea = (20161, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.3e+56, 'cm^3/(mol*s)'),
                        n = -13.12,
                        Ea = (20667, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.11e+50, 'cm^3/(mol*s)'),
                        n = -10.8,
                        Ea = (20202, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.17e+130, 'cm^3/(mol*s)'),
                        n = -32.58,
                        Ea = (136140, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.25e+29, 'cm^3/(mol*s)'),
                        n = -5.84,
                        Ea = (4241.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+30, 'cm^3/(mol*s)'),
                        n = -5.63,
                        Ea = (5613.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.11e+26, 'cm^3/(mol*s)'),
                        n = -4.44,
                        Ea = (5182.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.73e+23, 'cm^3/(mol*s)'),
                        n = -3.26,
                        Ea = (4597, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 633,
    label = "C2H4 + CH3 <=> NC3H7",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.67e+48, 'cm^3/(mol*s)'),
                        n = -12.54,
                        Ea = (18206, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+49, 'cm^3/(mol*s)'),
                        n = -12.04,
                        Ea = (20001, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.67e+47, 'cm^3/(mol*s)'),
                        n = -11.17,
                        Ea = (22366, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.81e+45, 'cm^3/(mol*s)'),
                        n = -10.03,
                        Ea = (23769, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.04e+40, 'cm^3/(mol*s)'),
                        n = -8.25,
                        Ea = (24214, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.12e+43, 'cm^3/(mol*s)'),
                        n = -11.3,
                        Ea = (13080, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.28e+39, 'cm^3/(mol*s)'),
                        n = -9.88,
                        Ea = (13164, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.6e+33, 'cm^3/(mol*s)'),
                        n = -7.46,
                        Ea = (12416, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.85e+27, 'cm^3/(mol*s)'),
                        n = -5.38,
                        Ea = (11455, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.66e+21, 'cm^3/(mol*s)'),
                        n = -3.17,
                        Ea = (10241, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 634,
    label = "C3H6 + HO2 <=> C3H6OOH2-1",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.9869, 9.87, 98.69], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.31e+13, 'cm^3/(mol*s)'),
                n = -1.84,
                Ea = (8561, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.93e+17, 'cm^3/(mol*s)'),
                n = -2.61,
                Ea = (11533, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.34e+24, 'cm^3/(mol*s)'),
                n = -4.4,
                Ea = (16440, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.75e+23, 'cm^3/(mol*s)'),
                n = -3.68,
                Ea = (17965, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 635,
    label = "C3H6 + HO2 <=> C3H6O1-2 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.9869, 9.87, 98.69], 'atm'),
        arrhenius = [
            Arrhenius(A=(3730, 'cm^3/(mol*s)'), n=2.64, Ea=(11173, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.78e+12, 'cm^3/(mol*s)'),
                n = 0.11,
                Ea = (16137, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.9e+17, 'cm^3/(mol*s)'),
                n = -1.4,
                Ea = (20077, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.13e+19, 'cm^3/(mol*s)'),
                n = -1.68,
                Ea = (23587, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 636,
    label = "C3H6 + HO2 <=> IC3H7 + O2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.9869, 9.87, 98.69], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.02e+07, 'cm^3/(mol*s)'),
                n = 1.16,
                Ea = (10273, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.31e+20, 'cm^3/(mol*s)'),
                n = -2.58,
                Ea = (19078, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.14e+28, 'cm^3/(mol*s)'),
                n = -4.92,
                Ea = (26212, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.87e+22, 'cm^3/(mol*s)'),
                n = -3.09,
                Ea = (26586, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 637,
    label = "C3H6OOH2-1 <=> C3H6O1-2 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.9869, 9.87, 98.69], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.66e+35, 's^-1'), n=-8.36, Ea=(18056, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.96e+35, 's^-1'), n=-7.66, Ea=(20595, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.24e+33, 's^-1'), n=-6.75, Ea=(21619, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.48e+26, 's^-1'), n=-4.58, Ea=(20278, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 638,
    label = "C3H5-A + H <=> C3H4-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1232, 'cm^3/(mol*s)'), n=3.035, Ea=(2582, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 639,
    label = "C3H5-A + OH <=> C3H4-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 640,
    label = "C3H5-A + CH3 <=> C3H4-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=-0.32, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 641,
    label = "C3H5-A + C2H5 <=> C3H4-A + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 642,
    label = "C3H5-A + C2H3 <=> C3H4-A + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 643,
    label = "C3H4-A + C3H4-A <=> C3H5-A + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+14, 'cm^3/(mol*s)'), n=0, Ea=(64746.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 644,
    label = "C3H5-S + H <=> C3H4-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.333e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 645,
    label = "C3H5-S + CH3 <=> C3H4-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 646,
    label = "C3H5-S + H <=> C3H4-P + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 647,
    label = "C3H5-S + CH3 <=> C3H4-P + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 648,
    label = "C3H5-T + H <=> C3H4-P + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 649,
    label = "C3H5-T + CH3 <=> C3H4-P + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 650,
    label = "C3H5-A + C3H5-A <=> C3H4-A + C3H6",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 4, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.77e+40, 'cm^3/(mol*s)'),
                n = -9.3,
                Ea = (12470, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.97e+32, 'cm^3/(mol*s)'),
                n = -6.8,
                Ea = (9180, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.46e+28, 'cm^3/(mol*s)'),
                n = -5.5,
                Ea = (7410, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 651,
    label = "C3H5-A + C2H5 <=> C2H4 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 652,
    label = "C3H5-A + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 653,
    label = "C3H5-S + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 654,
    label = "C3H5-T + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 655,
    label = "C3H5-S + O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 656,
    label = "C3H5-S + OH => C2H4 + HCO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 657,
    label = "C3H5-S + HO2 => C2H4 + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 658,
    label = "C3H5-T + O <=> CH3 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 659,
    label = "C3H5-T + OH => CH3 + CH2CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 660,
    label = "C3H5-T + HO2 => CH3 + CH2CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 661,
    label = "C3H5-A + O <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 662,
    label = "C3H5-A + OH => C2H3CHO + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.3e+37, 'cm^3/(mol*s)'),
                n = -6.71,
                Ea = (29306, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.2e+32, 'cm^3/(mol*s)'),
                n = -5.16,
                Ea = (30126, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6e+20, 'cm^3/(mol*s)'),
                n = -1.56,
                Ea = (26330, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 663,
    label = "C3H5-A + O2 <=> C3H4-A + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.99e+15, 'cm^3/(mol*s)'),
                n = -1.4,
                Ea = (22428, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.18e+21, 'cm^3/(mol*s)'),
                n = -2.85,
                Ea = (30755, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 664,
    label = "C3H5-A + O2 <=> CH3CO + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.19e+15, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (20128, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.14e+15, 'cm^3/(mol*s)'),
                n = -1.21,
                Ea = (21046, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 665,
    label = "C3H5-A + O2 <=> C2H3CHO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.82e+13, 'cm^3/(mol*s)'),
                n = -0.41,
                Ea = (22859, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+13, 'cm^3/(mol*s)'),
                n = -0.45,
                Ea = (23017, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 666,
    label = "C3H5-S + O2 <=> CH3CHO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+31, 'cm^3/(mol*s)'),
        n = -5.944,
        Ea = (5748.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 667,
    label = "C3H5-S + O2 <=> CH3CHCHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.38e+18, 'cm^3/(mol*s)'),
        n = -2.14,
        Ea = (5142.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 668,
    label = "C3H5-S + O2 <=> C2H3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+19, 'cm^3/(mol*s)'),
        n = -2.14,
        Ea = (5142.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 669,
    label = "C3H5-T + O2 <=> CH3COCH2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.86e+25, 'cm^3/(mol*s)'),
        n = -3.751,
        Ea = (11255.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 670,
    label = "C3H5-T + O2 <=> CH3CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.55e+20, 'cm^3/(mol*s)'),
        n = -2.608,
        Ea = (1565.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 671,
    label = "C3H5-T + O2 <=> C3H4-A + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.59e+10, 'cm^3/(mol*s)'),
        n = -0.27,
        Ea = (-413.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 672,
    label = "C3H5-A + HO2 <=> C3H5O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.02e+13, 'cm^3/(mol*s)'),
                n = -0.158,
                Ea = (-1417, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.98e+14, 'cm^3/(mol*s)'),
                n = -0.642,
                Ea = (-349.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.77e+17, 'cm^3/(mol*s)'),
                n = -1.52,
                Ea = (2379.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.93e+15, 'cm^3/(mol*s)'),
                n = -0.684,
                Ea = (3615.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (16400, 'cm^3/(mol*s)'),
                n = 2.74,
                Ea = (1144.4, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 673,
    label = "C3H5-A + HO2 <=> AC3H5OOH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.91e+31, 'cm^3/(mol*s)'),
                n = -7.23,
                Ea = (1336.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.31e+42, 'cm^3/(mol*s)'),
                n = -10.3,
                Ea = (5568.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.03e+45, 'cm^3/(mol*s)'),
                n = -10.6,
                Ea = (7851.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.79e+37, 'cm^3/(mol*s)'),
                n = -7.92,
                Ea = (6497.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.44e+32, 'cm^3/(mol*s)'),
                n = -6.01,
                Ea = (6053.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 674,
    label = "C3H5-A + HO2 <=> C2H3CHO + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.09, 'cm^3/(mol*s)'),
                n = 3.01,
                Ea = (-3421.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(63.5, 'cm^3/(mol*s)'), n=2.5, Ea=(-2341.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (605000, 'cm^3/(mol*s)'),
                n = 1.39,
                Ea = (595.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (310000, 'cm^3/(mol*s)'),
                n = 1.59,
                Ea = (2677.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.07e-05, 'cm^3/(mol*s)'),
                n = 4.59,
                Ea = (927.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 675,
    label = "AC3H5OOH <=> C2H3CHO + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.99e+50, 's^-1'), n=-12.7, Ea=(53531.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.72e+47, 's^-1'), n=-11.5, Ea=(54360.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+40, 's^-1'), n=-8.84, Ea=(53179.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.54e+28, 's^-1'), n=-5, Ea=(49919.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.48e+16, 's^-1'), n=-1.12, Ea=(45949.3, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 676,
    label = "AC3H5OOH <=> C3H5O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.49e+58, 's^-1'), n=-13.9, Ea=(54266.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+54, 's^-1'), n=-12.4, Ea=(54193.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.36e+46, 's^-1'), n=-9.81, Ea=(52468.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.39e+36, 's^-1'), n=-6.54, Ea=(49429, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.28e+27, 's^-1'), n=-3.61, Ea=(46333.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 677,
    label = "C3H5O <=> C2H3 + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.26e+06, 's^-1'), n=0.182, Ea=(17815.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.97e+16, 's^-1'), n=-2.5, Ea=(20878.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.64e+23, 's^-1'), n=-4.23, Ea=(23565, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.07e+26, 's^-1'), n=-4.56, Ea=(24622.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.5e+29, 's^-1'), n=-5.37, Ea=(26645, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.63e+31, 's^-1'), n=-5.59, Ea=(28915.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.52e+25, 's^-1'), n=-3.61, Ea=(27863.4, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 678,
    label = "C3H5O <=> CH2CHOCH2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.17e+20, 's^-1'), n=-4.15, Ea=(12121.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.79e+24, 's^-1'), n=-5.03, Ea=(14606.1, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.9e+26, 's^-1'), n=-5.16, Ea=(16124.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.51e+28, 's^-1'), n=-5.4, Ea=(18165.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.42e+28, 's^-1'), n=-5.17, Ea=(19691.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.57e+24, 's^-1'), n=-3.86, Ea=(19395.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.35e+18, 's^-1'), n=-1.73, Ea=(17386.5, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 679,
    label = "C3H5O <=> CH2CH2CHO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.25e-49, 's^-1'), n=15.5, Ea=(-15639.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.46e-88, 's^-1'), n=27.6, Ea=(-35995, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.44e-22, 's^-1'), n=8.38, Ea=(-3819, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.23e+12, 's^-1'), n=-1.44, Ea=(10829.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.48e+42, 's^-1'), n=-9.91, Ea=(25297.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.88e+38, 's^-1'), n=-8.16, Ea=(25974.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.67e+21, 's^-1'), n=-2.74, Ea=(20337.7, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 680,
    label = "C3H5O <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(3e+15, 's^-1'), n=-2.31, Ea=(14667.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+22, 's^-1'), n=-3.96, Ea=(18283, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.95e+23, 's^-1'), n=-3.99, Ea=(19143.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.15e+25, 's^-1'), n=-4.24, Ea=(20311.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.76e+28, 's^-1'), n=-4.89, Ea=(22765.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.41e+27, 's^-1'), n=-4.28, Ea=(23770.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.57e+20, 's^-1'), n=-2.06, Ea=(22040.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 681,
    label = "C3H5O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.62e+16, 's^-1'), n=-2.84, Ea=(13197, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.26e+20, 's^-1'), n=-3.53, Ea=(15469.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.13e+21, 's^-1'), n=-3.64, Ea=(16584.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.07e+24, 's^-1'), n=-4.16, Ea=(18985, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.42e+25, 's^-1'), n=-4.4, Ea=(22382.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.86e+21, 's^-1'), n=-2.73, Ea=(23658.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.75e+08, 's^-1'), n=1.14, Ea=(20922.5, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 682,
    label = "CH2CHOCH2 <=> C2H3 + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.3e+09, 's^-1'), n=-0.638, Ea=(19747.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.36e+21, 's^-1'), n=-3.9, Ea=(23945.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.91e+29, 's^-1'), n=-5.9, Ea=(27249.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.83e+34, 's^-1'), n=-6.94, Ea=(30690.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.72e+33, 's^-1'), n=-6.5, Ea=(33002.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.68e+27, 's^-1'), n=-4.26, Ea=(33305.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.81e+14, 's^-1'), n=-0.326, Ea=(31553.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 683,
    label = "CH2CHOCH2 <=> CH2CH2CHO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.01e-92, 's^-1'), n=27.8, Ea=(-37321.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.78e-11, 's^-1'), n=3.7, Ea=(-2766.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.11e+15, 's^-1'), n=-2.76, Ea=(15937.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.48e+25, 's^-1'), n=-5.2, Ea=(21532.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.97e+34, 's^-1'), n=-7.41, Ea=(28116.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.62e+22, 's^-1'), n=-3.56, Ea=(25806.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.51e+20, 's^-1'), n=-2.63, Ea=(29288.4, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 684,
    label = "CH2CHOCH2 <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.93e+24, 's^-1'), n=-5.05, Ea=(20108.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.14e+28, 's^-1'), n=-5.8, Ea=(22219.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.93e+32, 's^-1'), n=-6.64, Ea=(25108.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.6e+34, 's^-1'), n=-7.11, Ea=(28209.1, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.17e+34, 's^-1'), n=-6.64, Ea=(30647.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.17e+28, 's^-1'), n=-4.71, Ea=(31231.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.98e+18, 's^-1'), n=-1.62, Ea=(30129.8, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 685,
    label = "CH2CHOCH2 <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.23e+26, 's^-1'), n=-5.84, Ea=(19356.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.32e+29, 's^-1'), n=-6.21, Ea=(21293.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.47e+32, 's^-1'), n=-6.96, Ea=(24197.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.44e+36, 's^-1'), n=-7.76, Ea=(28007.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.72e+37, 's^-1'), n=-8.02, Ea=(32394.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.43e+31, 's^-1'), n=-5.81, Ea=(34295.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.73e+14, 's^-1'), n=-0.726, Ea=(32008.3, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 686,
    label = "CH2CH2CHO <=> C2H3 + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.89e-69, 's^-1'), n=21.5, Ea=(2638, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.34e-33, 's^-1'), n=11.1, Ea=(16749.1, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.11e+26, 's^-1'), n=-6.01, Ea=(44116.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.04e+35, 's^-1'), n=-8.31, Ea=(46919.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.52e+40, 's^-1'), n=-9.19, Ea=(50508.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.85e+35, 's^-1'), n=-7.18, Ea=(52038.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.93e+19, 's^-1'), n=-1.94, Ea=(48440, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 687,
    label = "CH2CH2CHO <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.61e+10, 's^-1'), n=-1.24, Ea=(32371.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.84e+15, 's^-1'), n=-2.61, Ea=(32878.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.64e+23, 's^-1'), n=-4.6, Ea=(34275.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.58e+31, 's^-1'), n=-6.63, Ea=(37895.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.86e+32, 's^-1'), n=-6.3, Ea=(39990.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.57e+23, 's^-1'), n=-3.14, Ea=(38011.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.52e+12, 's^-1'), n=0.214, Ea=(34570.5, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 688,
    label = "CH2CH2CHO <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.9e+32, 's^-1'), n=-7.24, Ea=(25687.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.3e+33, 's^-1'), n=-7.28, Ea=(27100.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+35, 's^-1'), n=-7.41, Ea=(29027.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.01e+34, 's^-1'), n=-6.7, Ea=(30018.1, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.76e+27, 's^-1'), n=-4.63, Ea=(28923.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.11e+19, 's^-1'), n=-1.85, Ea=(26239.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.59e+13, 's^-1'), n=0.063, Ea=(24086.3, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 689,
    label = "C2H3 + CH2O <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (26000, 'cm^3/(mol*s)'),
                n = 2.26,
                Ea = (1510.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (51300, 'cm^3/(mol*s)'),
                n = 2.17,
                Ea = (1675.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (399000, 'cm^3/(mol*s)'),
                n = 1.91,
                Ea = (2218.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.75e+07, 'cm^3/(mol*s)'),
                n = 1.45,
                Ea = (3428, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.35e+09, 'cm^3/(mol*s)'),
                n = 0.933,
                Ea = (5173, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.24e+11, 'cm^3/(mol*s)'),
                n = 0.357,
                Ea = (8001.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (601000, 'cm^3/(mol*s)'),
                n = 2.09,
                Ea = (7895.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 690,
    label = "C2H3 + CH2O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.11e+07, 'cm^3/(mol*s)'),
                n = 1.09,
                Ea = (1807.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+07, 'cm^3/(mol*s)'),
                n = 0.993,
                Ea = (1994.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+08, 'cm^3/(mol*s)'),
                n = 0.704,
                Ea = (2596.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.42e+10, 'cm^3/(mol*s)'),
                n = 0.209,
                Ea = (3934.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.45e+13, 'cm^3/(mol*s)'),
                n = -0.726,
                Ea = (6944.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.31e+14, 'cm^3/(mol*s)'),
                n = -0.866,
                Ea = (10965.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(16.5, 'cm^3/(mol*s)'), n=3.17, Ea=(9399.8, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 691,
    label = "C3H5-A + CH3O2 <=> C3H5O + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.33e+12, 'cm^3/(mol*s)'),
                n = -0.158,
                Ea = (-1417, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.66e+14, 'cm^3/(mol*s)'),
                n = -0.642,
                Ea = (-349.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.595e+17, 'cm^3/(mol*s)'),
                n = -1.52,
                Ea = (2379.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.78e+14, 'cm^3/(mol*s)'),
                n = -0.684,
                Ea = (3615.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(5470, 'cm^3/(mol*s)'), n=2.74, Ea=(1144.4, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 692,
    label = "C3H5-A + CH3O2 <=> AC4H7OOH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.91e+31, 'cm^3/(mol*s)'),
                n = -7.23,
                Ea = (1336.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.31e+42, 'cm^3/(mol*s)'),
                n = -10.3,
                Ea = (5568.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.03e+45, 'cm^3/(mol*s)'),
                n = -10.6,
                Ea = (7851.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.79e+37, 'cm^3/(mol*s)'),
                n = -7.92,
                Ea = (6497.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.4e+29, 'cm^3/(mol*s)'),
                n = -5.28,
                Ea = (4539.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 693,
    label = "AC4H7OOH <=> C3H5O + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.49e+58, 's^-1'), n=-13.9, Ea=(54266.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+54, 's^-1'), n=-12.4, Ea=(54193.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.36e+46, 's^-1'), n=-9.81, Ea=(52468.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.39e+36, 's^-1'), n=-6.54, Ea=(49429, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.56e+27, 's^-1'), n=-3.61, Ea=(46333.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 694,
    label = "C3H6 + OH <=> C3H5OH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.67e+13, 'cm^3/(mol*s)'),
                n = 0.05,
                Ea = (10611, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.75e+13, 'cm^3/(mol*s)'),
                n = 0.05,
                Ea = (10623, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.87e+13, 'cm^3/(mol*s)'),
                n = 0.04,
                Ea = (10634, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.59e+14, 'cm^3/(mol*s)'),
                n = -0.16,
                Ea = (11125, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.1e+14, 'cm^3/(mol*s)'),
                n = -0.22,
                Ea = (11407, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+14, 'cm^3/(mol*s)'),
                n = -0.24,
                Ea = (11458, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.15e+07, 'cm^3/(mol*s)'),
                n = 1.42,
                Ea = (10087, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (366000, 'cm^3/(mol*s)'),
                n = 2.14,
                Ea = (10410, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(819, 'cm^3/(mol*s)'), n=2.84, Ea=(10481, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 695,
    label = "C3H6 + OH <=> C2H3OH + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.29e+06, 'cm^3/(mol*s)'),
                n = 1.65,
                Ea = (1233, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(18200, 'cm^3/(mol*s)'), n=2.1, Ea=(1162, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2040, 'cm^3/(mol*s)'), n=2.48, Ea=(1128, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(288, 'cm^3/(mol*s)'), n=2.8, Ea=(1152, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(14, 'cm^3/(mol*s)'), n=3.21, Ea=(1208, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.71, 'cm^3/(mol*s)'), n=3.29, Ea=(1216, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(11300, 'cm^3/(mol*s)'), n=2.5, Ea=(3238, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (2.41e+19, 'cm^3/(mol*s)'),
                n = -1.74,
                Ea = (13107, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(0.33, 'cm^3/(mol*s)'), n=3.7, Ea=(3665, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 696,
    label = "C3H6 + OH <=> IC3H5OH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.87, 'cm^3/(mol*s)'), n=2.92, Ea=(625, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.484, 'cm^3/(mol*s)'), n=2.98, Ea=(704, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.313, 'cm^3/(mol*s)'), n=3.04, Ea=(721, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.00933, 'cm^3/(mol*s)'), n=3.62, Ea=(677, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.64e-05, 'cm^3/(mol*s)'),
                n = 4.48,
                Ea = (687, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.71e-05, 'cm^3/(mol*s)'),
                n = 4.56,
                Ea = (707, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.65e-07, 'cm^3/(mol*s)'),
                n = 5.05,
                Ea = (874, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.64e+15, 'cm^3/(mol*s)'),
                n = -0.8,
                Ea = (12728, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.000487, 'cm^3/(mol*s)'),
                n = 4.32,
                Ea = (4020, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 697,
    label = "C3H6 + OH <=> SC3H5OH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.47e+06, 'cm^3/(mol*s)'),
                n = 1.53,
                Ea = (4288, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.08e+07, 'cm^3/(mol*s)'),
                n = 1.34,
                Ea = (4576, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.76e+06, 'cm^3/(mol*s)'),
                n = 1.33,
                Ea = (4589, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.14e+06, 'cm^3/(mol*s)'),
                n = 1.36,
                Ea = (4594, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(313000, 'cm^3/(mol*s)'), n=1.69, Ea=(4603, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(139000, 'cm^3/(mol*s)'), n=1.8, Ea=(4603, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(103, 'cm^3/(mol*s)'), n=2.83, Ea=(4530, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.034, 'cm^3/(mol*s)'), n=3.89, Ea=(4390, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.46e-06, 'cm^3/(mol*s)'),
                n = 5.03,
                Ea = (4132, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 698,
    label = "C3H6 + OH <=> CH3CHO + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(693000, 'cm^3/(mol*s)'), n=1.49, Ea=(-536, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5940, 'cm^3/(mol*s)'), n=2.01, Ea=(-560, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1100, 'cm^3/(mol*s)'), n=2.22, Ea=(-680, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(107, 'cm^3/(mol*s)'), n=2.5, Ea=(-759, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.783, 'cm^3/(mol*s)'), n=3.1, Ea=(-919, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.307, 'cm^3/(mol*s)'), n=3.22, Ea=(-946, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (0.000316, 'cm^3/(mol*s)'),
                n = 4.05,
                Ea = (-1144, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.59e-06, 'cm^3/(mol*s)'),
                n = 4.49,
                Ea = (-680, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.45e-05, 'cm^3/(mol*s)'),
                n = 4.22,
                Ea = (1141, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 699,
    label = "C3H6 + OH <=> C3H6OH1-2",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.3e+78, 'cm^3/(mol*s)'),
                        n = -20.7,
                        Ea = (32402, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.74e+77, 'cm^3/(mol*s)'),
                        n = -20,
                        Ea = (33874, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.07e+76, 'cm^3/(mol*s)'),
                        n = -19.58,
                        Ea = (32874, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.68e+73, 'cm^3/(mol*s)'),
                        n = -18.79,
                        Ea = (31361, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.04e+68, 'cm^3/(mol*s)'),
                        n = -17.01,
                        Ea = (27909, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.23e+66, 'cm^3/(mol*s)'),
                        n = -16.64,
                        Ea = (27162, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.95e+59, 'cm^3/(mol*s)'),
                        n = -14.17,
                        Ea = (23079, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.58e+53, 'cm^3/(mol*s)'),
                        n = -12.23,
                        Ea = (22976, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.43e+48, 'cm^3/(mol*s)'),
                        n = -10.23,
                        Ea = (23772, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (6.41e+59, 'cm^3/(mol*s)'),
                        n = -15.84,
                        Ea = (11594, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.28e+59, 'cm^3/(mol*s)'),
                        n = -15.51,
                        Ea = (12898, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.79e+59, 'cm^3/(mol*s)'),
                        n = -15.34,
                        Ea = (12913, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.65e+58, 'cm^3/(mol*s)'),
                        n = -14.93,
                        Ea = (12936, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.35e+56, 'cm^3/(mol*s)'),
                        n = -14.04,
                        Ea = (12945, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.98e+55, 'cm^3/(mol*s)'),
                        n = -13.85,
                        Ea = (12887, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.55e+50, 'cm^3/(mol*s)'),
                        n = -12.04,
                        Ea = (11493, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.41e+41, 'cm^3/(mol*s)'),
                        n = -9.35,
                        Ea = (8921, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.3e+32, 'cm^3/(mol*s)'),
                        n = -6.31,
                        Ea = (6088, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 700,
    label = "C3H6 + OH <=> C3H6OH2-1",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.14e+59, 'cm^3/(mol*s)'),
                        n = -15.84,
                        Ea = (11594, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.43e+59, 'cm^3/(mol*s)'),
                        n = -15.51,
                        Ea = (12898, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.3e+58, 'cm^3/(mol*s)'),
                        n = -15.34,
                        Ea = (12913, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.83e+57, 'cm^3/(mol*s)'),
                        n = -14.93,
                        Ea = (12936, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.5e+55, 'cm^3/(mol*s)'),
                        n = -14.04,
                        Ea = (12945, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.33e+55, 'cm^3/(mol*s)'),
                        n = -13.85,
                        Ea = (12887, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.18e+49, 'cm^3/(mol*s)'),
                        n = -12.04,
                        Ea = (11493, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.14e+41, 'cm^3/(mol*s)'),
                        n = -9.35,
                        Ea = (8921, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.65e+31, 'cm^3/(mol*s)'),
                        n = -6.31,
                        Ea = (6088, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (7.68e+77, 'cm^3/(mol*s)'),
                        n = -20.7,
                        Ea = (32402, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.13e+76, 'cm^3/(mol*s)'),
                        n = -20,
                        Ea = (33874, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.55e+75, 'cm^3/(mol*s)'),
                        n = -19.58,
                        Ea = (32874, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.23e+73, 'cm^3/(mol*s)'),
                        n = -18.79,
                        Ea = (31361, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.45e+67, 'cm^3/(mol*s)'),
                        n = -17.01,
                        Ea = (27909, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.41e+66, 'cm^3/(mol*s)'),
                        n = -16.64,
                        Ea = (27162, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.5e+58, 'cm^3/(mol*s)'),
                        n = -14.17,
                        Ea = (23079, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.53e+53, 'cm^3/(mol*s)'),
                        n = -12.23,
                        Ea = (22976, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.78e+47, 'cm^3/(mol*s)'),
                        n = -10.23,
                        Ea = (23772, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 701,
    label = "CH2CCH2OH + H <=> C3H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 702,
    label = "C3H5OH + H <=> CH2CCH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(390000, 'cm^3/(mol*s)'), n=2.5, Ea=(5821, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 703,
    label = "C3H5OH + O2 <=> CH2CCH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(60690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 704,
    label = "C3H5OH + OH <=> CH2CCH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.06e+12, 'cm^3/(mol*s)'), n=0, Ea=(5960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 705,
    label = "C3H5OH + CH3 <=> CH2CCH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(8030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 706,
    label = "CH2CCH2OH + H2O2 <=> C3H5OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+09, 'cm^3/(mol*s)'), n=0, Ea=(2583, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 707,
    label = "CH2CCH2OH <=> C2H2 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.163e+40, 's^-1'), n=-8.31, Ea=(45110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 708,
    label = "CH2CCH2OH <=> CH2O + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.24e+10, 's^-1'), n=0.87, Ea=(30460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 709,
    label = "CH2CCH2OH <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11e+11, 's^-1'), n=0.48, Ea=(36770, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 710,
    label = "CH2CCH2OH <=> HCO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.24e+10, 's^-1'), n=0.87, Ea=(30460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 711,
    label = "CH2CCH2OH + O2 => CH2OH + CO + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4.335e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 712,
    label = "C3H5O + O2 <=> C2H3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 713,
    label = "CH3COCH3 + H <=> C3H6OH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 714,
    label = "IC3H5OH + H <=> C3H6OH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.25e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (4020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 715,
    label = "C2H5CHO + H <=> C3H6OH1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 716,
    label = "C3H5-T + OH <=> IC3H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 717,
    label = "C3H6OH2-1 + O2 <=> CH3COCH3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 718,
    label = "C3H6OH1-2 + O2 <=> C2H5CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 719,
    label = "C3H6OH1-2 + O2 <=> HOC3H6O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 720,
    label = "C3H6OH2-1 + O2 <=> HOC3H6O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 721,
    label = "HOC3H6O2 => CH3CHO + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 722,
    label = "SC3H5OH <=> C2H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 723,
    label = "SC3H5OH + O2 => C2H3CHO + H + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(39100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 724,
    label = "SC3H5OH + OH => C2H3CHO + H + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 725,
    label = "SC3H5OH + H => C2H3CHO + H + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 726,
    label = "SC3H5OH + O => C2H3CHO + H + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.75e+12, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 727,
    label = "SC3H5OH + HO2 => C2H3CHO + H + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9600, 'cm^3/(mol*s)'), n=2.6, Ea=(13900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 728,
    label = "SC3H5OH + CH3 => C2H3CHO + H + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 729,
    label = "SC3H5OH + CH3O2 => C2H3CHO + H + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9600, 'cm^3/(mol*s)'), n=2.6, Ea=(13900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 730,
    label = "SC3H5OH + CH3O => C2H3CHO + H + CH3OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 731,
    label = "SC3H5OH + HO2 <=> C2H5CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 732,
    label = "SC3H5OH + HOCHO <=> C2H5CHO + HOCHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4509, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 733,
    label = "C3H5-A + C2H3 => C5H6 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.6e+35, 'cm^3/(mol*s)'),
        n = -14,
        Ea = (61137.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 734,
    label = "C2H + CH3 <=> C3H4-P",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 735,
    label = "C3H4-A <=> C3H4-P",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.762e+39, 's^-1'), n=-7.8, Ea=(78446, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.786e+48, 's^-1'), n=-10, Ea=(88685, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 736,
    label = "CC3H4 <=> C3H4-P",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.512e+50, 's^-1'), n=-11.82, Ea=(50914, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.23e+37, 's^-1'), n=-7.51, Ea=(45551, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.66e+37, 's^-1'), n=-7.24, Ea=(48013, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 737,
    label = "CC3H4 <=> C3H4-A",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.772e+43, 's^-1'), n=-9.97, Ea=(56007, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.512e+26, 's^-1'), n=-4.56, Ea=(43922, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.012e+35, 's^-1'), n=-6.87, Ea=(51298, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 738,
    label = "C3H4-P <=> C3H3 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.48e+30, 's^-1'), n=-4.655, Ea=(93925.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.21e+25, 's^-1'), n=-2.787, Ea=(92376.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 739,
    label = "C3H4-A <=> C3H3 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.32e+31, 's^-1'), n=-4.749, Ea=(92079.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.65e+25, 's^-1'), n=-2.95, Ea=(90624.9, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 740,
    label = "C3H3 + H <=> CC3H4",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.913e+112, 'cm^3/(mol*s)'),
                n = -28.26,
                Ea = (83611, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.072e+21, 'cm^3/(mol*s)'),
                n = -2.95,
                Ea = (2687, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.236e+18, 'cm^3/(mol*s)'),
                n = -2.05,
                Ea = (2053, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 741,
    label = "C3H4-P + C3H3 <=> C3H4-A + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+06, 'cm^3/(mol*s)'),
        n = 1.74,
        Ea = (10450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 742,
    label = "C3H4-P + O2 <=> C3H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(42630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 743,
    label = "C3H4-P + O <=> C3H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.65e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 744,
    label = "C3H4-P + H <=> C3H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(35720, 'cm^3/(mol*s)'), n=2.825, Ea=(4821, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 745,
    label = "C3H4-P + OH <=> C3H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.94e+06, 'cm^3/(mol*s)'),
        n = 2.027,
        Ea = (1059.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 746,
    label = "C3H4-P + HO2 <=> C3H3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0955, 'cm^3/(mol*s)'),
        n = 4.17,
        Ea = (9632.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 747,
    label = "C3H4-P + CH3 <=> C3H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 748,
    label = "C3H4-P + CH3O2 <=> C3H3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0955, 'cm^3/(mol*s)'),
        n = 4.17,
        Ea = (9632.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 749,
    label = "C3H4-P + C2H <=> C2H2 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 750,
    label = "C3H4-P + C2H3 <=> C3H3 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 751,
    label = "C3H4-P + C3H5-A <=> C3H3 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 752,
    label = "C3H4-A + H <=> C3H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6625, 'cm^3/(mol*s)'), n=3.095, Ea=(5522, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 753,
    label = "C3H4-A + O2 <=> C3H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(41320, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 754,
    label = "C3H4-A + OH <=> C3H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (148200, 'cm^3/(mol*s)'),
        n = 2.492,
        Ea = (1807.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 755,
    label = "C3H4-A + CH3 <=> C3H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 756,
    label = "C3H4-A + HO2 <=> C3H3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0358, 'cm^3/(mol*s)'),
        n = 4.17,
        Ea = (9632.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 757,
    label = "C3H4-A + CH3O2 <=> C3H3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.07161, 'cm^3/(mol*s)'),
        n = 4.17,
        Ea = (9632.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 758,
    label = "C3H4-A + C3H5-A <=> C3H3 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 759,
    label = "C3H4-A + H <=> C3H4-P + H",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.49e+10, 'cm^3/(mol*s)'),
                        n = 0.89,
                        Ea = (2503, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.48e+13, 'cm^3/(mol*s)'),
                        n = 0.26,
                        Ea = (4103, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.48e+15, 'cm^3/(mol*s)'),
                        n = -0.33,
                        Ea = (6436, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.35e+25, 'cm^3/(mol*s)'),
                        n = -3.23,
                        Ea = (13165, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.02e+24, 'cm^3/(mol*s)'),
                        n = -2.67,
                        Ea = (15552, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (1.79e+07, 'cm^3/(mol*s)'),
                        n = 1.98,
                        Ea = (4521, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(46300, 'cm^3/(mol*s)'), n=2.62, Ea=(4466, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 760,
    label = "C3H4-A + H <=> C3H5-A",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.21e+61, 'cm^3/(mol*s)'),
                        n = -15.25,
                        Ea = (20076, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.24e+52, 'cm^3/(mol*s)'),
                        n = -12.02,
                        Ea = (17839, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.67e+51, 'cm^3/(mol*s)'),
                        n = -11.45,
                        Ea = (21340, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.75e+48, 'cm^3/(mol*s)'),
                        n = -10.27,
                        Ea = (22511, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.23e+43, 'cm^3/(mol*s)'),
                        n = -8.61,
                        Ea = (22522, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.8e+38, 'cm^3/(mol*s)'),
                        n = -8.67,
                        Ea = (8035, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.33e+36, 'cm^3/(mol*s)'),
                        n = -8.19,
                        Ea = (7462, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.32e+30, 'cm^3/(mol*s)'),
                        n = -5.78,
                        Ea = (6913, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.29e+26, 'cm^3/(mol*s)'),
                        n = -4.32,
                        Ea = (6163, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.38e+21, 'cm^3/(mol*s)'),
                        n = -2.71,
                        Ea = (5187, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 761,
    label = "C3H4-A + H <=> C3H5-S",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+30, 'cm^3/(mol*s)'),
                n = -6.52,
                Ea = (15200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.4e+29, 'cm^3/(mol*s)'),
                n = -6.09,
                Ea = (16300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.6e+31, 'cm^3/(mol*s)'),
                n = -6.23,
                Ea = (18700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.2e+31, 'cm^3/(mol*s)'),
                n = -5.88,
                Ea = (21500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 762,
    label = "C3H4-A + H <=> C3H5-T",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (6.44e+102, 'cm^3/(mol*s)'),
                        n = -27.51,
                        Ea = (51768, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.55e+53, 'cm^3/(mol*s)'),
                        n = -13.1,
                        Ea = (14472, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.9e+53, 'cm^3/(mol*s)'),
                        n = -12.59,
                        Ea = (16726, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.95e+51, 'cm^3/(mol*s)'),
                        n = -11.82,
                        Ea = (18286, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.21e+52, 'cm^3/(mol*s)'),
                        n = -11.64,
                        Ea = (22262, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.1e+54, 'cm^3/(mol*s)'),
                        n = -14.29,
                        Ea = (10809, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.88e+44, 'cm^3/(mol*s)'),
                        n = -11.21,
                        Ea = (8212, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.81e+40, 'cm^3/(mol*s)'),
                        n = -9.42,
                        Ea = (7850, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.6e+35, 'cm^3/(mol*s)'),
                        n = -7.57,
                        Ea = (7147, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.88e+29, 'cm^3/(mol*s)'),
                        n = -5.53,
                        Ea = (6581, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 763,
    label = "C3H4-A + H <=> CH3 + C2H2",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.23e+08, 'cm^3/(mol*s)'),
                        n = 1.53,
                        Ea = (4737, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.72e+09, 'cm^3/(mol*s)'),
                        n = 1.2,
                        Ea = (6834, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.26e+20, 'cm^3/(mol*s)'),
                        n = -1.83,
                        Ea = (15003, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.68e+16, 'cm^3/(mol*s)'),
                        n = -0.6,
                        Ea = (14754, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.37e+17, 'cm^3/(mol*s)'),
                        n = -0.79,
                        Ea = (17603, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(12300, 'cm^3/(mol*s)'), n=2.68, Ea=(6335, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.31e+08, 'cm^3/(mol*s)'),
                        n = 1.14,
                        Ea = (8886, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.28e+06, 'cm^3/(mol*s)'),
                        n = 1.71,
                        Ea = (9774, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 764,
    label = "C3H4-P + H <=> C3H5-T",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.85e+51, 'cm^3/(mol*s)'),
                        n = -13.04,
                        Ea = (12325, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.17e+52, 'cm^3/(mol*s)'),
                        n = -12.69,
                        Ea = (14226, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.87e+53, 'cm^3/(mol*s)'),
                        n = -12.51,
                        Ea = (16853, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.51e+51, 'cm^3/(mol*s)'),
                        n = -11.74,
                        Ea = (18331, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.51e+52, 'cm^3/(mol*s)'),
                        n = -11.58,
                        Ea = (22207, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.97e+46, 'cm^3/(mol*s)'),
                        n = -11.91,
                        Ea = (7456, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.59e+45, 'cm^3/(mol*s)'),
                        n = -11.23,
                        Ea = (8046, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.93e+39, 'cm^3/(mol*s)'),
                        n = -9.11,
                        Ea = (7458, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.8e+34, 'cm^3/(mol*s)'),
                        n = -7.29,
                        Ea = (6722, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.65e+29, 'cm^3/(mol*s)'),
                        n = -5.39,
                        Ea = (6150, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 765,
    label = "C3H4-P + H <=> C3H5-S",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.38e+49, 'cm^3/(mol*s)'),
                        n = -12.75,
                        Ea = (14072, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.37e+51, 'cm^3/(mol*s)'),
                        n = -12.55,
                        Ea = (15428, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.88e+50, 'cm^3/(mol*s)'),
                        n = -11.9,
                        Ea = (16915, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.17e+49, 'cm^3/(mol*s)'),
                        n = -11.1,
                        Ea = (18746, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.49e+38, 'cm^3/(mol*s)'),
                        n = -10.11,
                        Ea = (7458, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.98e+43, 'cm^3/(mol*s)'),
                        n = -11.43,
                        Ea = (8736, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.75e+39, 'cm^3/(mol*s)'),
                        n = -9.51,
                        Ea = (8772, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.33e+40, 'cm^3/(mol*s)'),
                        n = -9.6,
                        Ea = (9401, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.44e+34, 'cm^3/(mol*s)'),
                        n = -7.36,
                        Ea = (8558, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 766,
    label = "C3H4-P + H <=> CH3 + C2H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.44e+10, 'cm^3/(mol*s)'),
                n = 1.04,
                Ea = (3980, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.89e+10, 'cm^3/(mol*s)'),
                n = 0.989,
                Ea = (4114, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.46e+12, 'cm^3/(mol*s)'),
                n = 0.442,
                Ea = (5463, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.72e+14, 'cm^3/(mol*s)'),
                n = -0.01,
                Ea = (7134, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.9e+15, 'cm^3/(mol*s)'),
                n = -0.29,
                Ea = (8306, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 767,
    label = "C3H4-P + H <=> C3H5-A",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+60, 'cm^3/(mol*s)'),
                n = -14.56,
                Ea = (28100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.91e+60, 'cm^3/(mol*s)'),
                n = -14.37,
                Ea = (31644, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.04e+60, 'cm^3/(mol*s)'),
                n = -14.19,
                Ea = (32642, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.02e+59, 'cm^3/(mol*s)'),
                n = -13.89,
                Ea = (33953, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.2e+59, 'cm^3/(mol*s)'),
                n = -13.61,
                Ea = (34900, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6e+55, 'cm^3/(mol*s)'),
                n = -12.07,
                Ea = (37500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 768,
    label = "C3H5-A <=> C3H5-T",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.9e+59, 's^-1'), n=-15.42, Ea=(75400, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.06e+56, 's^-1'), n=-14.08, Ea=(75868, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.8e+55, 's^-1'), n=-13.59, Ea=(75949, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.86e+53, 's^-1'), n=-12.81, Ea=(75883, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.4e+51, 's^-1'), n=-12.12, Ea=(75700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+43, 's^-1'), n=-9.27, Ea=(74000, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 769,
    label = "C3H5-A <=> C3H5-S",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.3e+55, 's^-1'), n=-14.53, Ea=(73800, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5e+51, 's^-1'), n=-13.02, Ea=(73300, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.7e+48, 's^-1'), n=-11.73, Ea=(73700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.86e+44, 's^-1'), n=-9.84, Ea=(73400, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 770,
    label = "C2H2 + CH3 <=> C3H5-T",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.8e+20, 'cm^3/(mol*s)'),
                n = -4.16,
                Ea = (18000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.99e+22, 'cm^3/(mol*s)'),
                n = -4.39,
                Ea = (18850, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(6e+23, 'cm^3/(mol*s)'), n=-4.6, Ea=(19571, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (7.31e+25, 'cm^3/(mol*s)'),
                n = -5.06,
                Ea = (21150, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.3e+27, 'cm^3/(mol*s)'),
                n = -5.55,
                Ea = (22900, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.8e+36, 'cm^3/(mol*s)'),
                n = -7.58,
                Ea = (31300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 771,
    label = "C3H5-T <=> C3H5-S",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.6e+44, 's^-1'), n=-12.16, Ea=(52200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+48, 's^-1'), n=-12.71, Ea=(53900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.1e+52, 's^-1'), n=-13.37, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.8e+51, 's^-1'), n=-12.43, Ea=(59200, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 772,
    label = "C2H2 + CH3 <=> C3H5-A",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.2e+53, 'cm^3/(mol*s)'),
                n = -13.32,
                Ea = (33200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.68e+53, 'cm^3/(mol*s)'),
                n = -12.82,
                Ea = (35730, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.64e+52, 'cm^3/(mol*s)'),
                n = -12.46,
                Ea = (36127, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.04e+51, 'cm^3/(mol*s)'),
                n = -11.89,
                Ea = (36476, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.4e+49, 'cm^3/(mol*s)'),
                n = -11.4,
                Ea = (36700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.8e+44, 'cm^3/(mol*s)'),
                n = -9.63,
                Ea = (37600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 773,
    label = "CH3 + C2H2 <=> C3H5-S",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.78e+42, 'cm^3/(mol*s)'),
                        n = -10.4,
                        Ea = (13647, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.52e+44, 'cm^3/(mol*s)'),
                        n = -10.73,
                        Ea = (15256, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.19e+44, 'cm^3/(mol*s)'),
                        n = -10.19,
                        Ea = (18728, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.02e+43, 'cm^3/(mol*s)'),
                        n = -9.74,
                        Ea = (20561, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.42e+42, 'cm^3/(mol*s)'),
                        n = -8.91,
                        Ea = (22235, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (8.49e+35, 'cm^3/(mol*s)'),
                        n = -8.43,
                        Ea = (12356, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.04e+32, 'cm^3/(mol*s)'),
                        n = -7.01,
                        Ea = (12357, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.69e+27, 'cm^3/(mol*s)'),
                        n = -5.07,
                        Ea = (11690, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 774,
    label = "C3H4-P + O <=> HCCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 775,
    label = "C3H4-P + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 776,
    label = "C3H4-P + O <=> C2H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(2010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 777,
    label = "C3H4-A + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 778,
    label = "C3H4-A + O <=> C2H2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.003, 'cm^3/(mol*s)'), n=4.61, Ea=(-4243, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 779,
    label = "C3H4-A + OH <=> CH2CCH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11e+12, 'cm^3/(mol*s)'), n=0, Ea=(-304, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 780,
    label = "C3H4-A + OH <=> SC3H4OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+12, 'cm^3/(mol*s)'), n=0, Ea=(-304, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 781,
    label = "SC3H4OH <=> CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.24e+10, 's^-1'), n=0.87, Ea=(30460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 782,
    label = "C3H4-P + OH <=> PC3H4OH-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 783,
    label = "C3H4-P + OH <=> SC3H4OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.36e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 784,
    label = "PC3H4OH-2 <=> CH3CHCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.56e+10, 's^-1'), n=0.88, Ea=(23238, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 785,
    label = "CH3CHCHO <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2.5, 5, 10, 25, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.74e+50, 's^-1'), n=-11.73, Ea=(52870, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.13e+47, 's^-1'), n=-10.57, Ea=(50479, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.94e+43, 's^-1'), n=-9.29, Ea=(48810, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.16e+42, 's^-1'), n=-8.78, Ea=(48382, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.48e+40, 's^-1'), n=-8.4, Ea=(48095, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.19e+39, 's^-1'), n=-8.01, Ea=(47818, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.13e+38, 's^-1'), n=-7.49, Ea=(47438, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.42e+37, 's^-1'), n=-7.09, Ea=(47128, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 786,
    label = "CH3CHCHO <=> CH3CHCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.328e+12, 's^-1'), n=-0.02, Ea=(32410, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 787,
    label = "CH3CHCHO + H2 <=> C2H5CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (216000, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (18990, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 788,
    label = "C3H4-P + HO2 => C2H4 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 789,
    label = "C3H4-A + HO2 => C2H4 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 790,
    label = "C3H4-A + HO2 => CH2CO + CH2 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 791,
    label = "C3H4-A + C2H <=> C2H2 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 792,
    label = "C3H3 + O <=> CH2O + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 793,
    label = "C3H3 + HO2 => OH + CO + C2H3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 794,
    label = "C3H3 + HCO <=> C3H4-A + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 795,
    label = "C3H3 + HCO <=> C3H4-P + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 796,
    label = "C2H5 + C2H <=> C3H3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 797,
    label = "C3H3 + O2 <=> CH2CO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=1.7, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 798,
    label = "C3H3 + CH <=> C4H3-N + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 799,
    label = "C3H3 + HO2 <=> C3H3O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.02e+13, 'cm^3/(mol*s)'),
                n = -0.158,
                Ea = (-1417, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.98e+14, 'cm^3/(mol*s)'),
                n = -0.642,
                Ea = (-349.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.77e+17, 'cm^3/(mol*s)'),
                n = -1.52,
                Ea = (2379.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.93e+15, 'cm^3/(mol*s)'),
                n = -0.684,
                Ea = (3615.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (16400, 'cm^3/(mol*s)'),
                n = 2.74,
                Ea = (1144.4, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 800,
    label = "C3H3 + HO2 <=> C3H3O2H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.91e+31, 'cm^3/(mol*s)'),
                n = -7.23,
                Ea = (1336.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.31e+42, 'cm^3/(mol*s)'),
                n = -10.3,
                Ea = (5568.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.03e+45, 'cm^3/(mol*s)'),
                n = -10.6,
                Ea = (7851.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.79e+37, 'cm^3/(mol*s)'),
                n = -7.92,
                Ea = (6497.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.73e+25, 'cm^3/(mol*s)'),
                n = -4.13,
                Ea = (2923.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 801,
    label = "C3H3 + HO2 <=> C2HCHO + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.09, 'cm^3/(mol*s)'),
                n = 3.01,
                Ea = (-3421.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(63.5, 'cm^3/(mol*s)'), n=2.5, Ea=(-2341.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (605000, 'cm^3/(mol*s)'),
                n = 1.39,
                Ea = (595.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (310000, 'cm^3/(mol*s)'),
                n = 1.59,
                Ea = (2677.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.07e-05, 'cm^3/(mol*s)'),
                n = 4.59,
                Ea = (927.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 802,
    label = "C3H3O2H <=> C2HCHO + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.99e+50, 's^-1'), n=-12.7, Ea=(53531.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.72e+47, 's^-1'), n=-11.5, Ea=(54360.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+40, 's^-1'), n=-8.84, Ea=(53179.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.54e+28, 's^-1'), n=-5, Ea=(49919.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.48e+16, 's^-1'), n=-1.12, Ea=(45949.3, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 803,
    label = "C2H + CH2O <=> C3H3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (0.0005925, 'cm^3/(mol*s)'),
                n = 2.609,
                Ea = (-4297.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.688e+06, 'cm^3/(mol*s)'),
                n = -0.073,
                Ea = (-1234.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.39e+13, 'cm^3/(mol*s)'),
                n = -1.803,
                Ea = (1452.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.733e+15, 'cm^3/(mol*s)'),
                n = -2.074,
                Ea = (2510.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.305e+19, 'cm^3/(mol*s)'),
                n = -2.943,
                Ea = (4532.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.779e+21, 'cm^3/(mol*s)'),
                n = -3.163,
                Ea = (6802.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 804,
    label = "C2HCHO <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.51e+14, 's^-1'), n=0, Ea=(68000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 805,
    label = "C2H + HCO <=> C2HCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 806,
    label = "C3H3 + H <=> C3H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(214000, 'cm^3/(mol*s)'), n=2.52, Ea=(7453, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 807,
    label = "C3H3 + H <=> C3H2(S) + H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1, 10], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.951e+09, 'cm^3/(mol*s)'),
                        n = 1.28,
                        Ea = (13474, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.692e+09, 'cm^3/(mol*s)'),
                        n = 1.05,
                        Ea = (5371, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.097e+10, 'cm^3/(mol*s)'),
                        n = 1.13,
                        Ea = (13929, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.884e+13, 'cm^3/(mol*s)'),
                        n = -0.03,
                        Ea = (9448, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.311e+13, 'cm^3/(mol*s)'),
                        n = 0.195,
                        Ea = (17579, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1e+18, 'cm^3/(mol*s)'),
                        n = -1.23,
                        Ea = (15111, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 808,
    label = "C3H3 + H <=> C3H2C + H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.072e+07, 'cm^3/(mol*s)'),
                n = 1.37,
                Ea = (15557, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.349e+07, 'cm^3/(mol*s)'),
                n = 1.34,
                Ea = (15560, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.244e+09, 'cm^3/(mol*s)'),
                n = 0.606,
                Ea = (18356, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 809,
    label = "C3H2C + O2 <=> C2H2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 810,
    label = "C3H3 + OH <=> C3H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 811,
    label = "C3H3 + OH <=> CH2O + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 812,
    label = "C3H3 + OH <=> C2H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 813,
    label = "C3H3 + OH <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 814,
    label = "C3H3 + OH <=> C3H2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 815,
    label = "C3H2(S) <=> C3H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 816,
    label = "C3H3 + C3H3 <=> C6H5 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.0467e+54, 'cm^3/(mol*s)'),
                n = -11.88,
                Ea = (28757, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6975e+48, 'cm^3/(mol*s)'),
                n = -9.977,
                Ea = (36755, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.6712e+26, 'cm^3/(mol*s)'),
                n = -3.879,
                Ea = (28963, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 817,
    label = "C3H3 + C3H3 <=> C6H6",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.64e+66, 'cm^3/(mol*s)'),
                n = -15.902,
                Ea = (27529, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.1609e+55, 'cm^3/(mol*s)'),
                n = -12.55,
                Ea = (22264, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.8888e+50, 'cm^3/(mol*s)'),
                n = -11.01,
                Ea = (20320, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 818,
    label = "C3H3 + C3H3 <=> FULVENE",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (7.25e+65, 'cm^3/(mol*s)'),
                n = -16.015,
                Ea = (25035, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.3798e+66, 'cm^3/(mol*s)'),
                n = -15.66,
                Ea = (28260, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.2584e+56, 'cm^3/(mol*s)'),
                n = -12.61,
                Ea = (23515, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 819,
    label = "C3H3 + C3H5-A => FULVENE + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.26e+29, 'cm^3/(mol*s)'),
        n = -5.397,
        Ea = (3390, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 820,
    label = "C3H3 + C3H4-A <=> C6H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(9990.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 821,
    label = "CH3CHCO + OH <=> C2H5 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 822,
    label = "CH3CHCO + OH <=> SC2H4OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 823,
    label = "CH3CHCO + H <=> C2H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1459, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 824,
    label = "CH3CHCO + O <=> CH3CHO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 825,
    label = "CH3COCH3 <=> CH3CO + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.05e+58, 's^-1'), n=-12.796, Ea=(100030, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.3e+51, 's^-1'), n=-10.574, Ea=(98221.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.31e+42, 's^-1'), n=-7.657, Ea=(94660.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.16e+33, 's^-1'), n=-4.989, Ea=(90916.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.4e+28, 's^-1'), n=-3.669, Ea=(89022.8, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 826,
    label = "CH3COCH2 + H <=> CH3COCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 827,
    label = "CH3COCH3 + OH <=> CH3COCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(125000, 'cm^3/(mol*s)'), n=2.483, Ea=(445, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 828,
    label = "CH3COCH3 + H <=> CH3COCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(5160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 829,
    label = "CH3COCH3 + O <=> CH3COCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.13e+11, 'cm^3/(mol*s)'),
        n = 0.211,
        Ea = (4890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 830,
    label = "CH3COCH3 + CH3 <=> CH3COCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.96e+11, 'cm^3/(mol*s)'), n=0, Ea=(9784, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 831,
    label = "CH3COCH3 + CH3O <=> CH3COCH2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.34e+11, 'cm^3/(mol*s)'), n=0, Ea=(6460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 832,
    label = "CH3COCH3 + O2 <=> CH3COCH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(48500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 833,
    label = "CH3COCH3 + HO2 <=> CH3COCH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 834,
    label = "CH3COCH3 + CH3O2 <=> CH3COCH2 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 835,
    label = "CH3COCH3 + CH3COCH2O2 <=> CH3COCH2 + C3KET21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 836,
    label = "CH3COCH2 + HO2 <=> CH3COCH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 837,
    label = "CH3COCH2 + CH3O2 <=> CH3COCH2O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.205e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 838,
    label = "CH3COCH2O <=> CH3CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.872e+20, 's^-1'),
        n = -2.4218,
        Ea = (10535.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 839,
    label = "CH3COCH2 + O2 <=> CH3COCH2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 840,
    label = "CH2CO + CH3 <=> CH3COCH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 841,
    label = "CH2O + CH3COCH2O2 <=> HCO + C3KET21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.288e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 842,
    label = "HO2 + CH3COCH2O2 <=> C3KET21 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 843,
    label = "C2H3 + HCO <=> C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 844,
    label = "C2H3CHO + H <=> C2H3CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 845,
    label = "C2H3CHO + O <=> C2H3CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 846,
    label = "C2H3CHO + OH <=> C2H3CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.24e+06, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 847,
    label = "C2H3CHO + O2 <=> C2H3CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 848,
    label = "C2H3CHO + HO2 <=> C2H3CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 849,
    label = "C2H3CHO + CH3 <=> C2H3CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.608e+06, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (5911, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 850,
    label = "C2H3CHO + C2H3 <=> C2H3CO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 851,
    label = "C2H3CHO + CH3O <=> C2H3CO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 852,
    label = "C2H3CHO + CH3O2 <=> C2H3CO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 853,
    label = "C2H3 + CO <=> C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 854,
    label = "C2H5 + HCO <=> C2H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 855,
    label = "C2H5CHO + H <=> C2H5CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 856,
    label = "C2H5CHO + O <=> C2H5CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 857,
    label = "C2H5CHO + OH <=> C2H5CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 858,
    label = "C2H5CHO + CH3 <=> C2H5CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.608e+06, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (5911, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 859,
    label = "C2H5CHO + HO2 <=> C2H5CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 860,
    label = "C2H5CHO + CH3O <=> C2H5CO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 861,
    label = "C2H5CHO + CH3O2 <=> C2H5CO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 862,
    label = "C2H5CHO + C2H5 <=> C2H5CO + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 863,
    label = "C2H5CHO + C2H5O <=> C2H5CO + C2H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.026e+11, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 864,
    label = "C2H5CHO + C2H5O2 <=> C2H5CO + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 865,
    label = "C2H5CHO + O2 <=> C2H5CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 866,
    label = "C2H5CHO + CH3CO3 <=> C2H5CO + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 867,
    label = "C2H5CHO + C2H3 <=> C2H5CO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 868,
    label = "C2H5CHO + NC3H7 <=> C2H5CO + C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 869,
    label = "C2H5CHO + IC3H7 <=> C2H5CO + C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 870,
    label = "C2H5CHO + C3H5-A <=> C2H5CO + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 871,
    label = "C2H5 + CO <=> C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 872,
    label = "C4H10 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.355e+37, 's^-1'), n=-6.036, Ea=(92929, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.72e+18, 'cm^3/(mol*s)'), n=0, Ea=(49578, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.07998,
        T3 = (1e-20, 'K'),
        T1 = (32430, 'K'),
        T2 = (4858, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 873,
    label = "C4H10 <=> NC3H7 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.6e+52, 's^-1'), n=-10.626, Ea=(100330, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(5.34e+17, 'cm^3/(mol*s)'), n=0, Ea=(42959, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.09502,
        T3 = (1e-20, 'K'),
        T1 = (5348, 'K'),
        T2 = (4326, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 874,
    label = "C4H10 <=> PC4H9 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.45e+90, 's^-1'), n=-21.91, Ea=(140564, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.63e+76, 's^-1'), n=-17.64, Ea=(134669, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.94e+58, 's^-1'), n=-12.32, Ea=(125435, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.8e+40, 's^-1'), n=-7.06, Ea=(115302, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.49e+27, 's^-1'), n=-3.15, Ea=(107323, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 875,
    label = "C4H10 <=> SC4H9 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.1e+88, 's^-1'), n=-21.24, Ea=(136355, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.34e+73, 's^-1'), n=-16.76, Ea=(129590, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.39e+55, 's^-1'), n=-11.52, Ea=(120199, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.52e+38, 's^-1'), n=-6.58, Ea=(110556, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.4e+26, 's^-1'), n=-3.05, Ea=(103313, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 876,
    label = "C4H10 + H <=> PC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(349000, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 877,
    label = "C4H10 + O2 <=> PC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 878,
    label = "C4H10 + O <=> PC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+14, 'cm^3/(mol*s)'), n=0, Ea=(7850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 879,
    label = "C4H10 + OH <=> PC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.054e+10, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 880,
    label = "C4H10 + HO2 <=> PC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 881,
    label = "C4H10 + CH3 <=> PC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 882,
    label = "C4H10 + CH3O <=> PC4H9 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 883,
    label = "C4H10 + CH3O2 <=> PC4H9 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 884,
    label = "C4H10 + O2CHO <=> PC4H9 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.68e+13, 'cm^3/(mol*s)'), n=0, Ea=(20440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 885,
    label = "C4H10 + C2H5 <=> PC4H9 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+11, 'cm^3/(mol*s)'), n=0, Ea=(12300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 886,
    label = "C4H10 + C2H3 <=> PC4H9 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 887,
    label = "C4H10 + C2H5O <=> PC4H9 + C2H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 888,
    label = "C4H10 + C2H5O2 <=> PC4H9 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 889,
    label = "C4H10 + CH3CO3 <=> PC4H9 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 890,
    label = "C4H10 + C3H5-A <=> PC4H9 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 891,
    label = "C4H10 + NC3H7O2 <=> PC4H9 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 892,
    label = "C4H10 + IC3H7O2 <=> PC4H9 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 893,
    label = "C4H10 + PC4H9 <=> SC4H9 + C4H10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 894,
    label = "C4H10 + PC4H9O2 <=> PC4H9 + PC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 895,
    label = "C4H10 + SC4H9O2 <=> PC4H9 + SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 896,
    label = "C4H10 + IC4H9O2 <=> PC4H9 + IC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 897,
    label = "C4H10 + TC4H9O2 <=> PC4H9 + TC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 898,
    label = "C4H10 + H <=> SC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 899,
    label = "C4H10 + O2 <=> SC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 900,
    label = "C4H10 + O <=> SC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 901,
    label = "C4H10 + OH <=> SC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.34e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 902,
    label = "C4H10 + HO2 <=> SC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(126.4, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 903,
    label = "C4H10 + CH3 <=> SC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 904,
    label = "C4H10 + CH3O <=> SC4H9 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 905,
    label = "C4H10 + CH3O2 <=> SC4H9 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20.37, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 906,
    label = "C4H10 + O2CHO <=> SC4H9 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 907,
    label = "C4H10 + C2H5 <=> SC4H9 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 908,
    label = "C4H10 + C2H3 <=> SC4H9 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(16800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 909,
    label = "C4H10 + C2H5O <=> SC4H9 + C2H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 910,
    label = "C4H10 + C2H5O2 <=> SC4H9 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(126.4, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 911,
    label = "C4H10 + CH3CO3 <=> SC4H9 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 912,
    label = "C4H10 + C3H5-A <=> SC4H9 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.16e+11, 'cm^3/(mol*s)'), n=0, Ea=(16400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 913,
    label = "C4H10 + NC3H7O2 <=> SC4H9 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 914,
    label = "C4H10 + IC3H7O2 <=> SC4H9 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 915,
    label = "C4H10 + PC4H9O2 <=> SC4H9 + PC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 916,
    label = "C4H10 + SC4H9O2 <=> SC4H9 + SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 917,
    label = "C4H10 + IC4H9O2 <=> SC4H9 + IC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 918,
    label = "C4H10 + TC4H9O2 <=> SC4H9 + TC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 919,
    label = "PC4H9 + HO2 <=> PC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 920,
    label = "CH3O2 + PC4H9 <=> CH3O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 921,
    label = "SC4H9 + HO2 <=> SC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 922,
    label = "SC4H9 + CH3O2 <=> CH3O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 923,
    label = "C2H5 + CH3CHO <=> SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.33e+10, 'cm^3/(mol*s)'), n=0, Ea=(6397, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 924,
    label = "PC4H9 + O2 <=> C4H8-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.837, 'cm^3/(mol*s)'), n=3.59, Ea=(11960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 925,
    label = "PC4H9 + O2 <=> PC4H9O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.865e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 926,
    label = "SC4H9 + O2 <=> C4H8-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.535, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 927,
    label = "SC4H9 + O2 <=> C4H8-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 928,
    label = "SC4H9 + O2 <=> SC4H9O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.487e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 929,
    label = "PC4H9O2 + H2 <=> PC4H9O2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 930,
    label = "PC4H9O2 + HO2 <=> PC4H9O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 931,
    label = "PC4H9O2 + H2O2 <=> PC4H9O2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 932,
    label = "PC4H9O2 + CH4 <=> PC4H9O2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 933,
    label = "PC4H9O2 + CH3OH <=> PC4H9O2H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 934,
    label = "PC4H9O2 + CH2O <=> PC4H9O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 935,
    label = "PC4H9O2 + C2H6 <=> PC4H9O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 936,
    label = "PC4H9O2 + CH3CHO <=> PC4H9O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 937,
    label = "PC4H9O2 + C2H4 <=> PC4H9O2H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 938,
    label = "PC4H9O2 + C3H6 <=> PC4H9O2H + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0535, 'cm^3/(mol*s)'),
        n = 4.207,
        Ea = (13288.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 939,
    label = "PC4H9O2 + C2H5CHO <=> PC4H9O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 940,
    label = "PC4H9O2 + C2H3CHO <=> PC4H9O2H + C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 941,
    label = "PC4H9O2 + C3H8 <=> PC4H9O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 942,
    label = "PC4H9O2 + C3H8 <=> PC4H9O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 943,
    label = "PC4H9O2 + CH3 <=> PC4H9O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 944,
    label = "PC4H9O2 + C2H5 <=> PC4H9O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 945,
    label = "PC4H9O2 + IC3H7 <=> PC4H9O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 946,
    label = "PC4H9O2 + NC3H7 <=> PC4H9O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 947,
    label = "PC4H9O2 + C3H5-A <=> PC4H9O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 948,
    label = "PC4H9O2 + PC4H9 <=> PC4H9O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 949,
    label = "PC4H9O2 + SC4H9 <=> PC4H9O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 950,
    label = "PC4H9O2 + C4H71-3 <=> PC4H9O + C4H71-O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 951,
    label = "PC4H9O2H <=> PC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 952,
    label = "PC4H9O2 + CH3O2 => PC4H9O + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 953,
    label = "PC4H9O2 + CH3CO3 => PC4H9O + CH3CO2 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 954,
    label = "PC4H9O2 + C2H5O2 => PC4H9O + C2H5O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 955,
    label = "PC4H9O2 + NC3H7O2 => PC4H9O + NC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 956,
    label = "PC4H9O2 + IC3H7O2 => PC4H9O + IC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 957,
    label = "PC4H9O2 + PC4H9O2 => PC4H9O + PC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 958,
    label = "PC4H9O2 + SC4H9O2 => PC4H9O + SC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 959,
    label = "PC4H9O2 <=> C4H8OOH1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.009e+08, 's^-1'), n=1.1, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 960,
    label = "PC4H9O2 <=> C4H8OOH1-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+07, 's^-1'), n=1.3, Ea=(18200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 961,
    label = "PC4H9O2 <=> C4H8OOH1-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.233e+06, 's^-1'), n=1.5, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 962,
    label = "PC4H9O2 <=> C4H8-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.258e+08, 's^-1'), n=1.38, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 963,
    label = "IC3H7O2 + PC4H9 <=> IC3H7O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 964,
    label = "NC3H7O2 + PC4H9 <=> NC3H7O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 965,
    label = "SC4H9O2 + PC4H9 <=> SC4H9O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 966,
    label = "IC3H7O2 + SC4H9 <=> IC3H7O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 967,
    label = "NC3H7O2 + SC4H9 <=> NC3H7O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 968,
    label = "SC4H9O2 + H2 <=> SC4H9O2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 969,
    label = "SC4H9O2 + HO2 <=> SC4H9O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 970,
    label = "SC4H9O2 + CH2O <=> SC4H9O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 971,
    label = "SC4H9O2 + CH3CHO <=> SC4H9O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 972,
    label = "SC4H9O2 + C2H6 <=> SC4H9O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 973,
    label = "SC4H9O2 + C2H5CHO <=> SC4H9O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 974,
    label = "SC4H9O2 + C3H6 <=> SC4H9O2H + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0535, 'cm^3/(mol*s)'),
        n = 4.207,
        Ea = (13288.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 975,
    label = "SC4H9O2 + C2H4 <=> SC4H9O2H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 976,
    label = "SC4H9O2 + CH3OH <=> SC4H9O2H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 977,
    label = "SC4H9O2 + C2H3CHO <=> SC4H9O2H + C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 978,
    label = "SC4H9O2 + CH4 <=> SC4H9O2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 979,
    label = "SC4H9O2 + H2O2 <=> SC4H9O2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 980,
    label = "SC4H9O2 + C3H8 <=> SC4H9O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 981,
    label = "SC4H9O2 + C3H8 <=> SC4H9O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 982,
    label = "SC4H9O2 + CH3O2 => SC4H9O + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 983,
    label = "SC4H9O2 + CH3CO3 => SC4H9O + CH3CO2 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 984,
    label = "SC4H9O2 + NC3H7O2 => SC4H9O + NC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 985,
    label = "SC4H9O2 + IC3H7O2 => SC4H9O + IC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 986,
    label = "SC4H9O2 + SC4H9O2 => SC4H9O + SC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 987,
    label = "SC4H9O2 + C2H5O2 => SC4H9O + C2H5O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 988,
    label = "SC4H9O2 + CH3 <=> SC4H9O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 989,
    label = "SC4H9O2 + C2H5 <=> SC4H9O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 990,
    label = "SC4H9O2 + IC3H7 <=> SC4H9O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 991,
    label = "SC4H9O2 + NC3H7 <=> SC4H9O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 992,
    label = "SC4H9O2 + SC4H9 <=> SC4H9O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 993,
    label = "SC4H9O2 + C3H5-A <=> SC4H9O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 994,
    label = "SC4H9O2 + C4H71-3 <=> SC4H9O + C4H71-O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 995,
    label = "SC4H9O + OH <=> SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+15, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 996,
    label = "SC4H9O2 <=> C4H8OOH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.458e+09, 's^-1'), n=1.1, Ea=(33500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 997,
    label = "SC4H9O2 <=> C4H8OOH2-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.716e+09, 's^-1'), n=0.9, Ea=(29500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 998,
    label = "SC4H9O2 <=> C4H8OOH2-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.439e+07, 's^-1'), n=1.4, Ea=(20800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 999,
    label = "SC4H9O2 <=> C4H8-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.13e+09, 's^-1'), n=1, Ea=(30400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1000,
    label = "C4H8OOH1-2 <=> C4H8O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+09, 's^-1'), n=1.06, Ea=(10900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1001,
    label = "C4H8OOH1-3 <=> C4H8O1-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+09, 's^-1'), n=0.69, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1002,
    label = "C4H8OOH1-4 <=> C4H8O1-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+08, 's^-1'), n=0.76, Ea=(11100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1003,
    label = "C4H8OOH2-4 <=> C4H8O1-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+09, 's^-1'), n=0.78, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1004,
    label = "C4H8O1-2 + H => CH2O + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1005,
    label = "C4H8O1-2 + O => CH2O + C3H5-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1006,
    label = "C4H8O1-2 + OH => CH2O + C3H5-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1007,
    label = "C4H8O1-2 + HO2 => CH2O + C3H5-A + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1008,
    label = "C4H8O1-2 + CH3 => CH2O + C3H5-A + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1009,
    label = "C4H8O1-2 + CH3O2 => CH2O + C3H5-A + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1010,
    label = "C4H8O1-3 + H => CH2O + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1011,
    label = "C4H8O1-3 + O => CH2O + C3H5-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1012,
    label = "C4H8O1-3 + OH => CH2O + C3H5-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1013,
    label = "C4H8O1-3 + HO2 => CH2O + C3H5-A + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1014,
    label = "C4H8O1-3 + CH3 => CH2O + C3H5-A + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1015,
    label = "C4H8O1-3 + CH3O2 => CH2O + C3H5-A + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1016,
    label = "C4H8O1-4 + H => CH2O + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1017,
    label = "C4H8O1-4 + O => CH2O + C3H5-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1018,
    label = "C4H8O1-4 + OH => CH2O + C3H5-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1019,
    label = "C4H8O1-4 + HO2 => CH2O + C3H5-A + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1020,
    label = "C4H8O1-4 + CH3 => CH2O + C3H5-A + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1021,
    label = "C4H8O1-4 + CH3O2 => CH2O + C3H5-A + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1022,
    label = "C4H8O2-3 + H => CH2O + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1023,
    label = "C4H8O2-3 + OH => CH2O + C3H5-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1024,
    label = "C4H8O2-3 + O => CH2O + C3H5-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1025,
    label = "C4H8O2-3 + HO2 => CH2O + C3H5-A + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1026,
    label = "C4H8O2-3 + CH3O2 => CH2O + C3H5-A + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1027,
    label = "C4H8O2-3 + CH3 => CH2O + C3H5-A + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1028,
    label = "C4H8OOH1-3 => OH + CH2O + C3H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.23e+09, 's^-1'), n=1.3, Ea=(24900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1029,
    label = "C4H8OOH2-4 => OH + CH3CHO + C2H4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.08e+08, 's^-1'), n=1.5, Ea=(23500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1030,
    label = "C4H8OOH1-2 + O2 <=> C4H8OOH1-2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.744e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1031,
    label = "C4H8OOH1-3 + O2 <=> C4H8OOH1-3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.744e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1032,
    label = "C4H8OOH1-4 + O2 <=> C4H8OOH1-4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1033,
    label = "C4H8OOH2-1 + O2 <=> C4H8OOH2-1O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1034,
    label = "C4H8OOH2-3 + O2 <=> C4H8OOH2-3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.744e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1035,
    label = "C4H8OOH2-4 + O2 <=> C4H8OOH2-4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1036,
    label = "C4H8OOH1-2O2 <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.54e+10, 's^-1'), n=0.804, Ea=(30098.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1037,
    label = "C4H8OOH1-3O2 <=> C4H71-4OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.13e+09, 's^-1'), n=1, Ea=(30400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1038,
    label = "C4H8OOH1-3O2 <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.54e+10, 's^-1'), n=0.804, Ea=(30098.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1039,
    label = "C4H8OOH1-4O2 <=> C4H71-4OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44e+07, 's^-1'), n=1.38, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1040,
    label = "C4H8OOH2-3O2 <=> C4H71-3OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.13e+09, 's^-1'), n=1, Ea=(30400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1041,
    label = "C4H8OOH2-4O2 <=> C4H71-3OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44e+07, 's^-1'), n=1.38, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1042,
    label = "C4H8OOH1-2O2 <=> C4H71-3,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44e+07, 's^-1'), n=1.4, Ea=(20800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1043,
    label = "C4H8OOH1-2O2 <=> C4H72-3,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.9, Ea=(29500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1044,
    label = "C4H8OOH1-2O2 <=> NC4KET12 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+07, 's^-1'), n=1.6, Ea=(27900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1045,
    label = "C4H8OOH1-3O2 <=> C4H71-2,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.46e+09, 's^-1'), n=1.1, Ea=(33500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1046,
    label = "C4H8OOH1-3O2 <=> C4H72-1,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.9, Ea=(29500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1047,
    label = "C4H8OOH1-3O2 <=> NC4KET13 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10900, 's^-1'), n=2.4, Ea=(19900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1048,
    label = "C4H8OOH1-4O2 <=> C4H72-1,4OOH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.36e+07, 's^-1'), n=1.3, Ea=(18200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.01e+08, 's^-1'), n=1.1, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1049,
    label = "C4H8OOH1-4O2 <=> NC4KET14 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4800, 's^-1'), n=1.7, Ea=(16600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1050,
    label = "C4H8OOH2-1O2 <=> C4H72-3,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.9, Ea=(29500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1051,
    label = "C4H8OOH2-1O2 <=> C4H71-3,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+06, 's^-1'), n=1.5, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1052,
    label = "C4H8OOH2-1O2 <=> NC4KET21 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.76e+08, 's^-1'), n=1.2, Ea=(25700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1053,
    label = "C4H8OOH2-3O2 <=> C4H71-2,3OOH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.46e+09, 's^-1'), n=1.1, Ea=(33500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.44e+07, 's^-1'), n=1.4, Ea=(20800, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1054,
    label = "C4H8OOH2-3O2 <=> NC4KET23 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+06, 's^-1'), n=1.7, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1055,
    label = "C4H8OOH2-4O2 <=> C4H71-2,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+06, 's^-1'), n=1.5, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1056,
    label = "C4H8OOH2-4O2 <=> C4H72-1,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.01e+08, 's^-1'), n=1.1, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1057,
    label = "C4H8OOH2-4O2 <=> NC4KET24 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(57.9, 's^-1'), n=2.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1058,
    label = "C4H71-3,4OOH <=> C4H7O1-3OOH-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+09, 's^-1'), n=0.78, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1059,
    label = "C4H71-3,4OOH <=> C4H7O1-4OOH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.76, Ea=(11100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1060,
    label = "C4H72-3,4OOH <=> C4H7O2-3OOH-1 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.99e+09, 's^-1'), n=0.815, Ea=(9788.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1061,
    label = "C4H72-3,4OOH <=> C4H7O1-3OOH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+09, 's^-1'), n=0.69, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1062,
    label = "C4H71-2,4OOH <=> C4H7O1-2OOH-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+10, 's^-1'), n=0.68, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1063,
    label = "C4H71-2,4OOH <=> C4H7O1-4OOH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.76, Ea=(11100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1064,
    label = "C4H72-1,3OOH <=> C4H7O1-2OOH-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+09, 's^-1'), n=1.06, Ea=(10900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1065,
    label = "C4H72-1,3OOH <=> C4H7O2-3OOH-1 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.99e+09, 's^-1'), n=0.815, Ea=(9788.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1066,
    label = "C4H72-1,4OOH <=> C4H7O1-2OOH-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+09, 's^-1'), n=1.06, Ea=(10900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1067,
    label = "C4H72-1,4OOH <=> C4H7O1-3OOH-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+09, 's^-1'), n=0.69, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1068,
    label = "C4H71-2,3OOH <=> C4H7O1-2OOH-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+10, 's^-1'), n=0.68, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1069,
    label = "C4H71-2,3OOH <=> C4H7O1-3OOH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+09, 's^-1'), n=0.78, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1070,
    label = "C4H71-3,4OOH => C2H4 + OH + HO2CH2CHO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.23e+09, 's^-1'), n=1.3, Ea=(24900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1071,
    label = "C4H72-3,4OOH <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.568e+11, 's^-1'), n=0.538, Ea=(15324.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1072,
    label = "C4H71-2,4OOH <=> C4H71-4OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.67e+11, 's^-1'), n=0.5, Ea=(15800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1073,
    label = "C4H72-1,3OOH <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.568e+11, 's^-1'), n=0.538, Ea=(15324.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1074,
    label = "C4H72-1,3OOH <=> C4H71-3OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+09, 's^-1'), n=0.95, Ea=(15200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1075,
    label = "C4H72-1,4OOH <=> C4H71-4OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.568e+11, 's^-1'), n=0.538, Ea=(15324.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1076,
    label = "C4H71-2,3OOH <=> C4H71-3OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+09, 's^-1'), n=0.95, Ea=(15200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1077,
    label = "C4H72-1,4OOH <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.67e+11, 's^-1'), n=0.5, Ea=(15800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1078,
    label = "C4H72-1OOH => CH2O + C3H5-S + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1079,
    label = "C4H71-3OOH => C2H3CHO + CH3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1080,
    label = "C4H71-3OOH => CH3CHO + C2H3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1081,
    label = "NC4KET12 => C2H5CHO + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1082,
    label = "NC4KET13 => CH3CHO + CH2CHO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1083,
    label = "NC4KET14 => CH2CH2CHO + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1084,
    label = "NC4KET21 => CH2O + C2H5CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1085,
    label = "NC4KET23 => CH3CHO + CH3CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1086,
    label = "NC4KET24 => CH2O + CH3COCH2 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1087,
    label = "HO2CH2CHO => CH2O + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1088,
    label = "IC4H10 <=> CH3 + IC3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.52e+31, 's^-1'), n=-4.102, Ea=(91495, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.41e+19, 'cm^3/(mol*s)'), n=0, Ea=(52576, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.3662,
        T3 = (815.3, 'K'),
        T1 = (60.79, 'K'),
        T2 = (1e+20, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1089,
    label = "IC4H10 <=> TC4H9 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.51e+98, 's^-1'), n=-23.81, Ea=(145300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1090,
    label = "IC4H10 <=> IC4H9 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.85e+95, 's^-1'), n=-23.11, Ea=(147600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1091,
    label = "IC4H10 + CH3 <=> IC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1092,
    label = "IC4H10 + H <=> IC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1093,
    label = "IC4H10 + OH <=> IC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66540, 'cm^3/(mol*s)'),
        n = 2.665,
        Ea = (-168.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1094,
    label = "IC4H10 + C2H5 <=> IC4H9 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+12, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1095,
    label = "IC4H10 + HO2 <=> IC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(61.2, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1096,
    label = "IC4H10 + O <=> IC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.046e+07, 'cm^3/(mol*s)'),
        n = 2.034,
        Ea = (5136, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1097,
    label = "IC4H10 + CH3O <=> IC4H9 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1098,
    label = "IC4H10 + O2 <=> IC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1099,
    label = "IC4H10 + CH3O2 <=> IC4H9 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.079, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1100,
    label = "IC4H10 + C2H5O2 <=> IC4H9 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1101,
    label = "IC4H10 + CH3CO3 <=> IC4H9 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1102,
    label = "IC4H10 + NC3H7O2 <=> IC4H9 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1103,
    label = "IC4H10 + IC3H7O2 <=> IC4H9 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1104,
    label = "IC4H10 + IC4H9O2 <=> IC4H9 + IC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1105,
    label = "IC4H10 + TC4H9O2 <=> IC4H9 + TC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1106,
    label = "IC4H10 + O2CHO <=> IC4H9 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52e+13, 'cm^3/(mol*s)'), n=0, Ea=(20440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1107,
    label = "IC4H10 + SC4H9O2 <=> IC4H9 + SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1108,
    label = "IC4H10 + SC4H9O2 <=> TC4H9 + SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1109,
    label = "IC4H10 + PC4H9O2 <=> IC4H9 + PC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1110,
    label = "IC4H10 + H <=> TC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(602000, 'cm^3/(mol*s)'), n=2.4, Ea=(2583, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1111,
    label = "IC4H10 + CH3 <=> TC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.46, Ea=(4598, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1112,
    label = "IC4H10 + OH <=> TC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29250, 'cm^3/(mol*s)'),
        n = 2.531,
        Ea = (-1659, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1113,
    label = "IC4H10 + C2H5 <=> TC4H9 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1114,
    label = "IC4H10 + HO2 <=> TC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(433.2, 'cm^3/(mol*s)'), n=3.01, Ea=(12090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1115,
    label = "IC4H10 + O <=> TC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (196800, 'cm^3/(mol*s)'),
        n = 2.402,
        Ea = (1150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1116,
    label = "IC4H10 + CH3O <=> TC4H9 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+10, 'cm^3/(mol*s)'), n=0, Ea=(2800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1117,
    label = "IC4H10 + O2 <=> TC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(48200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1118,
    label = "IC4H10 + O2CHO <=> TC4H9 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1119,
    label = "IC4H10 + PC4H9O2 <=> TC4H9 + PC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1120,
    label = "IC4H10 + CH3O2 <=> TC4H9 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(136.6, 'cm^3/(mol*s)'), n=3.12, Ea=(13190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1121,
    label = "IC4H10 + C2H5O2 <=> TC4H9 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1122,
    label = "IC4H10 + CH3CO3 <=> TC4H9 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1123,
    label = "IC4H10 + NC3H7O2 <=> TC4H9 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1124,
    label = "IC4H10 + IC3H7O2 <=> TC4H9 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1125,
    label = "IC4H10 + IC4H9O2 <=> TC4H9 + IC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1126,
    label = "IC4H10 + TC4H9O2 <=> TC4H9 + TC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1127,
    label = "IC4H10 + IC4H9 <=> TC4H9 + IC4H10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1128,
    label = "IC4H9 <=> TC4H9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.56e+10, 's^-1'), n=0.88, Ea=(34600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1129,
    label = "IC4H9 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.15e+41, 's^-1'), n=-9.5, Ea=(33486, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.75e+44, 's^-1'), n=-10.07, Ea=(37209, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.79e+44, 's^-1'), n=-9.7, Ea=(39751, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.61e+39, 's^-1'), n=-7.78, Ea=(39583, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1130,
    label = "TC4H9 + HO2 <=> TC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1131,
    label = "TC4H9 + CH3O2 <=> TC4H9O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1132,
    label = "TC4H9 + NC3H7O2 <=> TC4H9O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1133,
    label = "TC4H9 + SC4H9O2 <=> TC4H9O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1134,
    label = "TC4H9 + PC4H9O2 <=> TC4H9O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1135,
    label = "TC4H9 + IC3H7O2 <=> TC4H9O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1136,
    label = "IC4H9 + HO2 <=> IC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1137,
    label = "IC4H9 + CH3O2 <=> IC4H9O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1138,
    label = "IC4H9 + NC3H7O2 <=> IC4H9O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1139,
    label = "IC4H9 + SC4H9O2 <=> IC4H9O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1140,
    label = "IC4H9 + PC4H9O2 <=> IC4H9O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1141,
    label = "IC4H9 + IC3H7O2 <=> IC4H9O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1142,
    label = "CH3COCH3 + CH3 <=> TC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1143,
    label = "TC4H9O + O2 <=> IC4H8O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(4700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1144,
    label = "IC4H9O + H <=> IC3H7CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1145,
    label = "IC4H9O + O2 <=> IC3H7CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(1660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1146,
    label = "IC4H9O + O <=> IC3H7CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1147,
    label = "IC4H9O + OH <=> IC3H7CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1148,
    label = "IC4H9O + HO2 <=> IC3H7CHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1149,
    label = "IC4H9O + CH3 <=> IC3H7CHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1150,
    label = "IC3H7CHO + H <=> IC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1151,
    label = "CH2O + IC3H7 <=> IC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(2330, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1152,
    label = "TC3H6CHO + H <=> IC3H7CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1153,
    label = "SC4H7OH-I <=> IC3H7CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1154,
    label = "IC3H7 + HCO <=> IC3H7CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1155,
    label = "IC4H8O <=> IC3H7CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.18e+13, 's^-1'), n=0, Ea=(52720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1156,
    label = "IC3H7CHO + HO2 <=> IC3H7CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1157,
    label = "IC3H7CHO + CH3 <=> IC3H7CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(8700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1158,
    label = "IC3H7CHO + O <=> IC3H7CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+12, 'cm^3/(mol*s)'), n=0, Ea=(1389, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1159,
    label = "IC3H7CHO + O2 <=> IC3H7CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(37600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1160,
    label = "IC3H7CHO + OH <=> IC3H7CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1161,
    label = "IC3H7CHO + H <=> IC3H7CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1162,
    label = "IC3H7CHO + OH <=> IC3H6CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1163,
    label = "IC3H7CHO + HO2 <=> IC3H6CHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27400, 'cm^3/(mol*s)'), n=2.55, Ea=(15500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1164,
    label = "IC3H7CHO + CH3O2 <=> IC3H6CHO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47600, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1165,
    label = "TC3H6CHO + H2 <=> IC3H7CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (216000, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (18990, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1166,
    label = "IC3H7CHO + HO2 <=> TC3H6CHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+10, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1167,
    label = "IC3H7CHO + OH <=> TC3H6CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.684e+12, 'cm^3/(mol*s)'), n=0, Ea=(-781, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1168,
    label = "IC4H8O + OH <=> IC3H6CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (75200, 'cm^3/(mol*s)'),
        n = 2.49,
        Ea = (-1474.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1169,
    label = "IC4H8O + H <=> IC3H6CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(87900, 'cm^3/(mol*s)'), n=2.68, Ea=(2910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1170,
    label = "IC4H8O + HO2 <=> IC3H6CHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.45e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (7475.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1171,
    label = "IC4H8O + CH3O2 <=> IC3H6CHO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.225e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (7475.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1172,
    label = "IC4H8O + CH3 <=> IC3H6CHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.93, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1173,
    label = "IC4H8O + O <=> IC3H6CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(145000, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1174,
    label = "IC4H8O + O2 <=> IC3H6CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(50150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1175,
    label = "IC3H5CHO + H <=> TC3H6CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1176,
    label = "IC3H6CO + H <=> TC3H6CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1177,
    label = "IC3H6CO + OH <=> IC3H7 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1178,
    label = "IC3H6CO + OH <=> C3H6OH2-1 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1179,
    label = "TC3H6CHO + HO2 <=> IC3H7CHO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.675e+12, 'cm^3/(mol*s)'), n=0, Ea=(1310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1180,
    label = "TC3H6CHO + CH3 <=> IC3H5CHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-131, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1181,
    label = "TC3H6CHO + CH2O <=> IC3H7CHO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (18190, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1182,
    label = "TC3H6CHO + IC4H8 <=> IC3H7CHO + IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(470, 'cm^3/(mol*s)'), n=3.3, Ea=(19840, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1183,
    label = "TC3H6CHO + O2 <=> TC3H6O2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+17, 'cm^3/(mol*s)'), n=-2.1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1184,
    label = "TC3H6O2CHO <=> IC3H5O2HCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(29880, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1185,
    label = "TC3H6O2CHO <=> TC3H6O2HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1186,
    label = "IC3H5CHO + HO2 <=> IC3H5O2HCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1187,
    label = "TC3H6OCHO + OH <=> TC3H6CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.018e+17, 'cm^3/(mol*s)'),
        n = -1.2,
        Ea = (21010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1188,
    label = "TC3H6OCHO <=> CH3COCH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+13, 's^-1'), n=0, Ea=(9700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1189,
    label = "TC3H6CHO + OH <=> IC3H6OHCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1190,
    label = "C3H6OH2-1 + HCO <=> IC3H6OHCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1191,
    label = "IC3H5CHO + H <=> IC3H5CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (714740, 'cm^3/(mol*s)'),
        n = 2.35674,
        Ea = (1577.16, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1192,
    label = "IC3H5CHO + O2 <=> IC3H5CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(40700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1193,
    label = "IC3H5CHO + O <=> IC3H5CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+12, 'cm^3/(mol*s)'), n=0, Ea=(1389, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1194,
    label = "IC3H5CHO + OH <=> IC3H5CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (61329.9, 'cm^3/(mol*s)'),
        n = 2.65,
        Ea = (-4586.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1195,
    label = "IC3H5CHO + HO2 <=> IC3H5CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00011773, 'cm^3/(mol*s)'),
        n = 4.91966,
        Ea = (3684.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1196,
    label = "IC3H5CHO + CH3 <=> IC3H5CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.24879, 'cm^3/(mol*s)'),
        n = 3.63386,
        Ea = (4328.93, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1197,
    label = "IC3H5CHO + H <=> IC3H4CHO-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (364000, 'cm^3/(mol*s)'),
        n = 2.455,
        Ea = (4361.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1198,
    label = "IC3H5CHO + O2 <=> IC3H4CHO-A + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.96e+19, 'cm^3/(mol*s)'),
        n = -1.67,
        Ea = (46192.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1199,
    label = "IC3H5CHO + OH <=> IC3H4CHO-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.46e+06, 'cm^3/(mol*s)'),
        n = 2.072,
        Ea = (1050.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1200,
    label = "IC3H5CHO + O <=> IC3H4CHO-A + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1201,
    label = "IC3H5CHO + HO2 <=> IC3H4CHO-A + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0307, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1202,
    label = "IC3H5CHO + CH3 <=> IC3H4CHO-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1203,
    label = "IC3H5CO <=> C3H5-T + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.278e+20, 's^-1'), n=-1.89, Ea=(34460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1204,
    label = "C3H4-A + HCO <=> IC3H4CHO-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40209.7, 'cm^3/(mol*s)'),
        n = 2.51815,
        Ea = (8847.54, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1205,
    label = "IC3H7 + CO <=> IC3H7CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1206,
    label = "C2H3CHO + CH3 <=> IC3H6CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1207,
    label = "SC4H7OH-I + HO2 <=> IC3H7CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1208,
    label = "SC4H7OH-I + HOCHO <=> IC3H7CHO + HOCHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4509, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1209,
    label = "SC4H7OH-I + H <=> IC4H6OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (729000, 'cm^3/(mol*s)'),
        n = 2.455,
        Ea = (4361.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1210,
    label = "SC4H7OH-I + O <=> IC4H6OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+12, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1211,
    label = "SC4H7OH-I + OH <=> IC4H6OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43950.2, 'cm^3/(mol*s)'),
        n = 2.67841,
        Ea = (-827.103, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1212,
    label = "SC4H7OH-I + HO2 <=> IC4H6OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.292, 'cm^3/(mol*s)'), n=4.12, Ea=(12802, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1213,
    label = "SC4H7OH-I + CH3 <=> IC4H6OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.42, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1214,
    label = "SC4H7OH-I + CH3O <=> IC4H6OH + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.68e+11, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1215,
    label = "SC4H7OH-I + CH3O2 <=> IC4H6OH + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1216,
    label = "IC4H6OH + H => CH3 + C3H4-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (40209.7, 'cm^3/(mol*s)'),
        n = 2.51815,
        Ea = (8847.54, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1217,
    label = "TC4H9 + O2 <=> IC4H8 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.837, 'cm^3/(mol*s)'), n=3.59, Ea=(11960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1218,
    label = "IC4H9 + O2 <=> IC4H8 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1219,
    label = "IC4H9 + O2 <=> IC4H9O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6946e+13, 'cm^3/(mol*s)'),
        n = -0.3,
        Ea = (-187.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1220,
    label = "TC4H9 + O2 <=> TC4H9O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6946e+13, 'cm^3/(mol*s)'),
        n = -0.3,
        Ea = (-187.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1221,
    label = "IC4H9O2 <=> IC4H8 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.94e+08, 's^-1'), n=1.27, Ea=(29600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1222,
    label = "IC4H9O2 <=> IC4H8O2H-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.82e+07, 's^-1'), n=1.3, Ea=(21500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1223,
    label = "IC4H9O2 <=> IC4H8O2H-T",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.31e+09, 's^-1'), n=0.8, Ea=(27100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1224,
    label = "TC4H9O2 <=> TC4H8O2H-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.521e+09, 's^-1'), n=1.2, Ea=(33500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1225,
    label = "IC4H8O2H-I <=> CC4H8O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+11, 's^-1'), n=0, Ea=(21900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1226,
    label = "IC4H8O2H-I => OH + CH2O + C3H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.451e+15, 's^-1'), n=-0.68, Ea=(29170, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1227,
    label = "CC4H8O + OH => CH2O + C3H5-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1228,
    label = "CC4H8O + H => CH2O + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.51e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1229,
    label = "CC4H8O + O => CH2O + C3H5-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.124e+14, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1230,
    label = "CC4H8O + HO2 => CH2O + C3H5-A + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1231,
    label = "CC4H8O + CH3O2 => CH2O + C3H5-A + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1232,
    label = "CC4H8O + CH3 => CH2O + C3H5-A + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1233,
    label = "IC4H8O2H-I + O2 <=> IC4H8OOH-IO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.35316e+11, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (-1010.88, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1234,
    label = "IC4H8O2H-T + O2 <=> IC4H8OOH-TO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.04482e+12, 'cm^3/(mol*s)'),
        n = -0.1,
        Ea = (-655.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1235,
    label = "TC4H8O2H-I + O2 <=> TC4H8OOH-IO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.28443e+10, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-786.24, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1236,
    label = "IC4H8OOH-IO2 <=> IC4KETII + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1237,
    label = "IC4H8OOH-TO2 <=> IC4KETIT + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 's^-1'), n=0, Ea=(31500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1238,
    label = "IC4H8OOH-TO2 <=> TIC4H7Q2-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(34500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1239,
    label = "IC4H8OOH-IO2 <=> IIC4H7Q2-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1240,
    label = "IC4H8OOH-IO2 <=> IIC4H7Q2-T",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(29200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1241,
    label = "TC4H8OOH-IO2 <=> TIC4H7Q2-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.82e+07, 's^-1'), n=1.3, Ea=(21500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1242,
    label = "IC4H8O2H-T <=> IC4H8O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+12, 's^-1'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1243,
    label = "AC3H5OOH + CH2O2H <=> IIC4H7Q2-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1244,
    label = "IC4H7OOH + HO2 <=> IIC4H7Q2-T",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1245,
    label = "TIC4H7Q2-I <=> IC4H7OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+12, 's^-1'), n=0.23, Ea=(15200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1246,
    label = "IC4KETII => CH2O + C2H5CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1247,
    label = "IC4H9O2 + CH3O2 => IC4H9O + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1248,
    label = "IC4H9O2 + C2H5O2 => IC4H9O + C2H5O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1249,
    label = "IC4H9O2 + CH3CO3 => IC4H9O + CH3CO2 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1250,
    label = "IC4H9O2 + IC4H9O2 => O2 + IC4H9O + IC4H9O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1251,
    label = "IC4H9O2 + TC4H9O2 => IC4H9O + TC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1252,
    label = "IC4H9O2 + PC4H9O2 => IC4H9O + PC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1253,
    label = "IC4H9O2 + SC4H9O2 => IC4H9O + SC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1254,
    label = "IC4H9O2 + NC3H7O2 => IC4H9O + NC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1255,
    label = "IC4H9O2 + IC3H7O2 => IC4H9O + IC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1256,
    label = "IC4H9O2 + HO2 => IC4H9O + OH + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1257,
    label = "TC4H9O2 + CH3O2 => TC4H9O + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1258,
    label = "TC4H9O2 + C2H5O2 => TC4H9O + C2H5O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1259,
    label = "TC4H9O2 + CH3CO3 => TC4H9O + CH3CO2 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1260,
    label = "TC4H9O2 + TC4H9O2 => O2 + TC4H9O + TC4H9O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1261,
    label = "TC4H9O2 + PC4H9O2 => TC4H9O + PC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1262,
    label = "TC4H9O2 + SC4H9O2 => TC4H9O + SC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1263,
    label = "TC4H9O2 + NC3H7O2 => TC4H9O + NC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1264,
    label = "TC4H9O2 + IC3H7O2 => TC4H9O + IC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1265,
    label = "TC4H9O2 + HO2 => TC4H9O + OH + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1266,
    label = "IC4H9O2 + CH3 <=> IC4H9O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1267,
    label = "IC4H9O2 + C2H5 <=> IC4H9O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1268,
    label = "IC4H9O2 + IC3H7 <=> IC4H9O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1269,
    label = "IC4H9O2 + NC3H7 <=> IC4H9O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1270,
    label = "IC4H9O2 + PC4H9 <=> IC4H9O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1271,
    label = "IC4H9O2 + SC4H9 <=> IC4H9O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1272,
    label = "IC4H9O2 + IC4H9 <=> IC4H9O + IC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1273,
    label = "IC4H9O2 + TC4H9 <=> IC4H9O + TC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1274,
    label = "IC4H9O2 + C3H5-A <=> IC4H9O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1275,
    label = "IC4H9O2 + C4H71-3 <=> IC4H9O + C4H71-O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1276,
    label = "IC4H9O2 + IC4H7 <=> IC4H9O + IC4H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1277,
    label = "TC4H9O2 + CH3 <=> TC4H9O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1278,
    label = "TC4H9O2 + C2H5 <=> TC4H9O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1279,
    label = "TC4H9O2 + IC3H7 <=> TC4H9O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1280,
    label = "TC4H9O2 + NC3H7 <=> TC4H9O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1281,
    label = "TC4H9O2 + PC4H9 <=> TC4H9O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1282,
    label = "TC4H9O2 + SC4H9 <=> TC4H9O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1283,
    label = "TC4H9O2 + IC4H9 <=> TC4H9O + IC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1284,
    label = "TC4H9O2 + TC4H9 <=> TC4H9O + TC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1285,
    label = "TC4H9O2 + C3H5-A <=> TC4H9O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1286,
    label = "TC4H9O2 + C4H71-3 <=> TC4H9O + C4H71-O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1287,
    label = "IC4H9O2H <=> IC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1288,
    label = "IC4H9O2 + HO2 <=> IC4H9O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1289,
    label = "IC4H9O2 + H2O2 <=> IC4H9O2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1290,
    label = "IC4H9O2 + H2 <=> IC4H9O2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1291,
    label = "IC4H9O2 + CH4 <=> IC4H9O2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1292,
    label = "IC4H9O2 + CH3OH <=> IC4H9O2H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1293,
    label = "IC4H9O2 + CH2O <=> IC4H9O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1294,
    label = "IC4H9O2 + C2H6 <=> IC4H9O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1295,
    label = "IC4H9O2 + C2H4 <=> IC4H9O2H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1296,
    label = "IC4H9O2 + C2H5OH <=> IC4H9O2H + PC2H4OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1297,
    label = "IC4H9O2 + C2H5OH <=> IC4H9O2H + SC2H4OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1298,
    label = "IC4H9O2 + CH3CHO <=> IC4H9O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1299,
    label = "IC4H9O2 + C3H8 <=> IC4H9O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1300,
    label = "IC4H9O2 + C3H8 <=> IC4H9O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1301,
    label = "IC4H9O2 + C2H3CHO <=> IC4H9O2H + C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1302,
    label = "IC4H9O2 + C2H5CHO <=> IC4H9O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1303,
    label = "IC4H9O2 + C3H6 <=> IC4H9O2H + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0535, 'cm^3/(mol*s)'),
        n = 4.207,
        Ea = (13288.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1304,
    label = "TC4H9O2H <=> TC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.95e+15, 's^-1'), n=0, Ea=(42540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1305,
    label = "TC4H9O2 + CH4 <=> TC4H9O2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1306,
    label = "TC4H9O2 + C2H6 <=> TC4H9O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1307,
    label = "TC4H9O2 + C3H8 <=> TC4H9O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1308,
    label = "TC4H9O2 + C3H8 <=> TC4H9O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1309,
    label = "TC4H9O2 + CH3OH <=> TC4H9O2H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1310,
    label = "TC4H9O2 + C2H5OH <=> TC4H9O2H + PC2H4OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1311,
    label = "TC4H9O2 + C2H5OH <=> TC4H9O2H + SC2H4OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1312,
    label = "TC4H9O2 + CH3CHO <=> TC4H9O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1313,
    label = "TC4H9O2 + C2H3CHO <=> TC4H9O2H + C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1314,
    label = "TC4H9O2 + C2H5CHO <=> TC4H9O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1315,
    label = "TC4H9O2 + HO2 <=> TC4H9O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1316,
    label = "TC4H9O2 + H2O2 <=> TC4H9O2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1317,
    label = "TC4H9O2 + CH2O <=> TC4H9O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1318,
    label = "TC4H9O2 + C2H4 <=> TC4H9O2H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1319,
    label = "TC4H9O2 + H2 <=> TC4H9O2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1320,
    label = "TC4H9O2 + C3H6 <=> TC4H9O2H + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0535, 'cm^3/(mol*s)'),
        n = 4.207,
        Ea = (13288.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1321,
    label = "IC4H8 <=> IC4H7-I1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.71e+69, 's^-1'), n=-16.09, Ea=(140000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1322,
    label = "IC4H8 <=> C3H5-T + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 3.5, 10, 35, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.26e+94, 's^-1'), n=-22.99, Ea=(134024, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.76e+93, 's^-1'), n=-22.51, Ea=(137933, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.14e+90, 's^-1'), n=-21.37, Ea=(137866, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.2e+85, 's^-1'), n=-19.94, Ea=(136498, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.05e+78, 's^-1'), n=-17.76, Ea=(133437, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.87e+71, 's^-1'), n=-15.65, Ea=(129919, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1323,
    label = "IC4H8 <=> IC4H7 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 3.5, 10, 35, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.51e+95, 's^-1'), n=-23.38, Ea=(129214, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.59e+88, 's^-1'), n=-20.99, Ea=(127813, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.96e+82, 's^-1'), n=-19.12, Ea=(125456, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.13e+76, 's^-1'), n=-17.27, Ea=(122629, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.13e+68, 's^-1'), n=-14.82, Ea=(118416, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.73e+60, 's^-1'), n=-12.66, Ea=(114404, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1324,
    label = "IC4H8 + OH <=> IC4H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43950.2, 'cm^3/(mol*s)'),
        n = 2.67841,
        Ea = (-827.103, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1325,
    label = "IC4H8 + OH <=> IC4H7-I1 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10930.1, 'cm^3/(mol*s)'),
        n = 2.81477,
        Ea = (1114.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1326,
    label = "IC4H8 + O2 <=> IC4H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(37450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1327,
    label = "IC4H8 + O2 <=> IC4H7-I1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(62270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1328,
    label = "IC4H8 + H <=> IC4H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (729000, 'cm^3/(mol*s)'),
        n = 2.455,
        Ea = (4361.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1329,
    label = "IC4H8 + H <=> IC4H7-I1 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(862.1, 'cm^3/(mol*s)'), n=3.25, Ea=(12167, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1330,
    label = "IC4H8 + O <=> IC4H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+12, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1331,
    label = "IC4H8 + O <=> IC4H7-I1 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8959.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1332,
    label = "IC4H8 + HO2 <=> IC4H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.292, 'cm^3/(mol*s)'), n=4.12, Ea=(12802, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1333,
    label = "IC4H8 + HO2 <=> IC4H7-I1 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (97038.9, 'cm^3/(mol*s)'),
        n = 2.54892,
        Ea = (24733.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1334,
    label = "IC4H8 + CH3 <=> IC4H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1335,
    label = "IC4H8 + CH3 <=> IC4H7-I1 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1336,
    label = "IC4H8 + CH3O <=> IC4H7 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.68e+11, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1337,
    label = "IC4H8 + C3H5-A <=> IC4H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1338,
    label = "IC4H8 + C3H5-S <=> IC4H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1339,
    label = "IC4H8 + C3H5-T <=> IC4H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1340,
    label = "IC4H8 + CH3O2 <=> IC4H7 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.154, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1341,
    label = "IC4H8 + CH3CO3 <=> IC4H7 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.154, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1342,
    label = "IC4H8 + O2CHO <=> IC4H7 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1343,
    label = "IC4H9O2 + IC4H8 <=> IC4H9O2H + IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1344,
    label = "TC4H9O2 + IC4H8 <=> TC4H9O2H + IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1345,
    label = "PC4H9O2 + IC4H8 <=> PC4H9O2H + IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1346,
    label = "SC4H9O2 + IC4H8 <=> SC4H9O2H + IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1347,
    label = "IC3H7O2 + IC4H8 <=> IC3H7O2H + IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1348,
    label = "NC3H7O2 + IC4H8 <=> NC3H7O2H + IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1349,
    label = "IC4H7O + IC4H8 <=> IC4H7OH + IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1350,
    label = "IC4H8 + CH2CCH2OH <=> IC4H7 + C3H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1351,
    label = "IC4H7 <=> IC4H7-I1",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.3e+55, 's^-1'), n=-14.53, Ea=(73800, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5e+51, 's^-1'), n=-13.02, Ea=(73300, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.7e+48, 's^-1'), n=-11.73, Ea=(73700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.86e+44, 's^-1'), n=-9.84, Ea=(73400, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1352,
    label = "C3H4-A + CH3 <=> IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40209.7, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (8847.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1353,
    label = "IC4H7 + HO2 <=> IC4H7O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.02e+13, 'cm^3/(mol*s)'),
                n = -0.158,
                Ea = (-1417, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.98e+14, 'cm^3/(mol*s)'),
                n = -0.642,
                Ea = (-349.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.77e+17, 'cm^3/(mol*s)'),
                n = -1.52,
                Ea = (2379.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.93e+15, 'cm^3/(mol*s)'),
                n = -0.684,
                Ea = (3615.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (16400, 'cm^3/(mol*s)'),
                n = 2.74,
                Ea = (1144.4, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1354,
    label = "IC4H7 + HO2 <=> IC4H7OOH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.91e+31, 'cm^3/(mol*s)'),
                n = -7.23,
                Ea = (1336.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.31e+42, 'cm^3/(mol*s)'),
                n = -10.3,
                Ea = (5568.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.03e+45, 'cm^3/(mol*s)'),
                n = -10.6,
                Ea = (7851.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.79e+37, 'cm^3/(mol*s)'),
                n = -7.92,
                Ea = (6497.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.44e+32, 'cm^3/(mol*s)'),
                n = -6.01,
                Ea = (6053.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1355,
    label = "IC4H7 + HO2 <=> IC3H5CHO + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.09, 'cm^3/(mol*s)'),
                n = 3.01,
                Ea = (-3421.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(63.5, 'cm^3/(mol*s)'), n=2.5, Ea=(-2341.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (605000, 'cm^3/(mol*s)'),
                n = 1.39,
                Ea = (595.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (310000, 'cm^3/(mol*s)'),
                n = 1.59,
                Ea = (2677.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.07e-05, 'cm^3/(mol*s)'),
                n = 4.59,
                Ea = (927.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1356,
    label = "IC4H7OOH <=> IC3H5CHO + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.99e+50, 's^-1'), n=-12.7, Ea=(53531.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.72e+47, 's^-1'), n=-11.5, Ea=(54360.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+40, 's^-1'), n=-8.84, Ea=(53179.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.54e+28, 's^-1'), n=-5, Ea=(49919.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.48e+16, 's^-1'), n=-1.12, Ea=(45949.3, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1357,
    label = "IC4H7OOH <=> IC4H7O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.49e+58, 's^-1'), n=-13.9, Ea=(54266.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+54, 's^-1'), n=-12.4, Ea=(54193.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.36e+46, 's^-1'), n=-9.81, Ea=(52468.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.39e+36, 's^-1'), n=-6.54, Ea=(49429, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.28e+27, 's^-1'), n=-3.61, Ea=(46333.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1358,
    label = "IC4H7O <=> C3H5-T + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.26e+06, 's^-1'), n=0.182, Ea=(17815.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.97e+16, 's^-1'), n=-2.5, Ea=(20878.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.64e+23, 's^-1'), n=-4.23, Ea=(23565, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.07e+26, 's^-1'), n=-4.56, Ea=(24622.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.5e+29, 's^-1'), n=-5.37, Ea=(26645, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.63e+31, 's^-1'), n=-5.59, Ea=(28915.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.52e+25, 's^-1'), n=-3.61, Ea=(27863.4, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1359,
    label = "IC4H7O <=> IC3H5OCH2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.17e+20, 's^-1'), n=-4.15, Ea=(12121.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.79e+24, 's^-1'), n=-5.03, Ea=(14606.1, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.9e+26, 's^-1'), n=-5.16, Ea=(16124.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.51e+28, 's^-1'), n=-5.4, Ea=(18165.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.42e+28, 's^-1'), n=-5.17, Ea=(19691.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.57e+24, 's^-1'), n=-3.86, Ea=(19395.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.35e+18, 's^-1'), n=-1.73, Ea=(17386.5, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1360,
    label = "IC4H7O <=> IC3H6CHO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.25e-49, 's^-1'), n=15.5, Ea=(-15639.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.46e-88, 's^-1'), n=27.6, Ea=(-35995, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.44e-22, 's^-1'), n=8.38, Ea=(-3819, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.23e+12, 's^-1'), n=-1.44, Ea=(10829.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.48e+42, 's^-1'), n=-9.91, Ea=(25297.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.88e+38, 's^-1'), n=-8.16, Ea=(25974.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.67e+21, 's^-1'), n=-2.74, Ea=(20337.7, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1361,
    label = "IC4H7O <=> IC3H5CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(3e+15, 's^-1'), n=-2.31, Ea=(14667.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+22, 's^-1'), n=-3.96, Ea=(18283, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.95e+23, 's^-1'), n=-3.99, Ea=(19143.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.15e+25, 's^-1'), n=-4.24, Ea=(20311.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.76e+28, 's^-1'), n=-4.89, Ea=(22765.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.41e+27, 's^-1'), n=-4.28, Ea=(23770.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.57e+20, 's^-1'), n=-2.06, Ea=(22040.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1362,
    label = "IC4H7O <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.62e+16, 's^-1'), n=-2.84, Ea=(13197, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.26e+20, 's^-1'), n=-3.53, Ea=(15469.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.13e+21, 's^-1'), n=-3.64, Ea=(16584.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.07e+24, 's^-1'), n=-4.16, Ea=(18985, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.42e+25, 's^-1'), n=-4.4, Ea=(22382.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.86e+21, 's^-1'), n=-2.73, Ea=(23658.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.75e+08, 's^-1'), n=1.14, Ea=(20922.5, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1363,
    label = "IC3H5OCH2 <=> C3H5-T + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.3e+09, 's^-1'), n=-0.638, Ea=(19747.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.36e+21, 's^-1'), n=-3.9, Ea=(23945.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.91e+29, 's^-1'), n=-5.9, Ea=(27249.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.83e+34, 's^-1'), n=-6.94, Ea=(30690.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.72e+33, 's^-1'), n=-6.5, Ea=(33002.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.68e+27, 's^-1'), n=-4.26, Ea=(33305.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.81e+14, 's^-1'), n=-0.326, Ea=(31553.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1364,
    label = "IC3H5OCH2 <=> IC3H6CHO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.01e-92, 's^-1'), n=27.8, Ea=(-37321.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.78e-11, 's^-1'), n=3.7, Ea=(-2766.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.11e+15, 's^-1'), n=-2.76, Ea=(15937.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.48e+25, 's^-1'), n=-5.2, Ea=(21532.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.97e+34, 's^-1'), n=-7.41, Ea=(28116.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.62e+22, 's^-1'), n=-3.56, Ea=(25806.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.51e+20, 's^-1'), n=-2.63, Ea=(29288.4, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1365,
    label = "IC3H5OCH2 <=> IC3H5CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.93e+24, 's^-1'), n=-5.05, Ea=(20108.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.14e+28, 's^-1'), n=-5.8, Ea=(22219.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.93e+32, 's^-1'), n=-6.64, Ea=(25108.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.6e+34, 's^-1'), n=-7.11, Ea=(28209.1, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.17e+34, 's^-1'), n=-6.64, Ea=(30647.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.17e+28, 's^-1'), n=-4.71, Ea=(31231.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.98e+18, 's^-1'), n=-1.62, Ea=(30129.8, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1366,
    label = "IC3H5OCH2 <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.23e+26, 's^-1'), n=-5.84, Ea=(19356.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.32e+29, 's^-1'), n=-6.21, Ea=(21293.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.47e+32, 's^-1'), n=-6.96, Ea=(24197.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.44e+36, 's^-1'), n=-7.76, Ea=(28007.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.72e+37, 's^-1'), n=-8.02, Ea=(32394.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.43e+31, 's^-1'), n=-5.81, Ea=(34295.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.73e+14, 's^-1'), n=-0.726, Ea=(32008.3, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1367,
    label = "IC3H6CHO <=> C3H5-T + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.89e-69, 's^-1'), n=21.5, Ea=(2638, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.34e-33, 's^-1'), n=11.1, Ea=(16749.1, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.11e+26, 's^-1'), n=-6.01, Ea=(44116.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.04e+35, 's^-1'), n=-8.31, Ea=(46919.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.52e+40, 's^-1'), n=-9.19, Ea=(50508.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.85e+35, 's^-1'), n=-7.18, Ea=(52038.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.93e+19, 's^-1'), n=-1.94, Ea=(48440, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1368,
    label = "IC3H6CHO <=> IC3H5CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.61e+10, 's^-1'), n=-1.24, Ea=(32371.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.84e+15, 's^-1'), n=-2.61, Ea=(32878.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.64e+23, 's^-1'), n=-4.6, Ea=(34275.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.58e+31, 's^-1'), n=-6.63, Ea=(37895.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.86e+32, 's^-1'), n=-6.3, Ea=(39990.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.57e+23, 's^-1'), n=-3.14, Ea=(38011.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.52e+12, 's^-1'), n=0.214, Ea=(34570.5, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1369,
    label = "IC3H6CHO <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.9e+32, 's^-1'), n=-7.24, Ea=(25687.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.3e+33, 's^-1'), n=-7.28, Ea=(27100.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+35, 's^-1'), n=-7.41, Ea=(29027.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.01e+34, 's^-1'), n=-6.7, Ea=(30018.1, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.76e+27, 's^-1'), n=-4.63, Ea=(28923.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.11e+19, 's^-1'), n=-1.85, Ea=(26239.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.59e+13, 's^-1'), n=0.063, Ea=(24086.3, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1370,
    label = "C3H5-T + CH2O <=> IC3H5CHO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (26000, 'cm^3/(mol*s)'),
                n = 2.26,
                Ea = (1510.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (51300, 'cm^3/(mol*s)'),
                n = 2.17,
                Ea = (1675.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (399000, 'cm^3/(mol*s)'),
                n = 1.91,
                Ea = (2218.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.75e+07, 'cm^3/(mol*s)'),
                n = 1.45,
                Ea = (3428, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.35e+09, 'cm^3/(mol*s)'),
                n = 0.933,
                Ea = (5173, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.24e+11, 'cm^3/(mol*s)'),
                n = 0.357,
                Ea = (8001.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (601000, 'cm^3/(mol*s)'),
                n = 2.09,
                Ea = (7895.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1371,
    label = "C3H5-T + CH2O <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.11e+07, 'cm^3/(mol*s)'),
                n = 1.09,
                Ea = (1807.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+07, 'cm^3/(mol*s)'),
                n = 0.993,
                Ea = (1994.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+08, 'cm^3/(mol*s)'),
                n = 0.704,
                Ea = (2596.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.42e+10, 'cm^3/(mol*s)'),
                n = 0.209,
                Ea = (3934.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.45e+13, 'cm^3/(mol*s)'),
                n = -0.726,
                Ea = (6944.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.31e+14, 'cm^3/(mol*s)'),
                n = -0.866,
                Ea = (10965.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(16.5, 'cm^3/(mol*s)'), n=3.17, Ea=(9399.8, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1372,
    label = "IC4H7 + CH3O2 <=> IC4H7O + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.33e+12, 'cm^3/(mol*s)'),
                n = -0.158,
                Ea = (-1417, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.66e+14, 'cm^3/(mol*s)'),
                n = -0.642,
                Ea = (-349.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.595e+17, 'cm^3/(mol*s)'),
                n = -1.52,
                Ea = (2379.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.78e+14, 'cm^3/(mol*s)'),
                n = -0.684,
                Ea = (3615.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(5470, 'cm^3/(mol*s)'), n=2.74, Ea=(1144.4, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1373,
    label = "IC4H7 + CH3O2 <=> IC4H7OOCH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.91e+31, 'cm^3/(mol*s)'),
                n = -7.23,
                Ea = (1336.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.31e+42, 'cm^3/(mol*s)'),
                n = -10.3,
                Ea = (5568.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.03e+45, 'cm^3/(mol*s)'),
                n = -10.6,
                Ea = (7851.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.79e+37, 'cm^3/(mol*s)'),
                n = -7.92,
                Ea = (6497.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.4e+29, 'cm^3/(mol*s)'),
                n = -5.28,
                Ea = (4539.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1374,
    label = "IC4H7OOCH3 <=> IC4H7O + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.49e+58, 's^-1'), n=-13.9, Ea=(54266.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+54, 's^-1'), n=-12.4, Ea=(54193.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.36e+46, 's^-1'), n=-9.81, Ea=(52468.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.39e+36, 's^-1'), n=-6.54, Ea=(49429, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.56e+27, 's^-1'), n=-3.61, Ea=(46333.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1375,
    label = "IC4H7O2 + IC4H7 <=> IC4H7O + IC4H7O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.55e+12, 'cm^3/(mol*s)'),
                n = -0.158,
                Ea = (-1417, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.25e+14, 'cm^3/(mol*s)'),
                n = -0.642,
                Ea = (-349.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.94e+17, 'cm^3/(mol*s)'),
                n = -1.52,
                Ea = (2379.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.33e+14, 'cm^3/(mol*s)'),
                n = -0.684,
                Ea = (3615.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=2.74, Ea=(1144.4, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1376,
    label = "IC4H7O2 + IC4H7 <=> IC4H7OOIC4H7",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.78e+30, 'cm^3/(mol*s)'),
                n = -7.23,
                Ea = (1336.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.58e+42, 'cm^3/(mol*s)'),
                n = -10.3,
                Ea = (5568.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.58e+44, 'cm^3/(mol*s)'),
                n = -10.6,
                Ea = (7851.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.98e+36, 'cm^3/(mol*s)'),
                n = -7.92,
                Ea = (6497.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.6e+31, 'cm^3/(mol*s)'),
                n = -6.01,
                Ea = (6053.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1377,
    label = "IC4H7OOIC4H7 <=> IC4H7O + IC4H7O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.73e+57, 's^-1'), n=-13.9, Ea=(54266.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.5e+53, 's^-1'), n=-12.4, Ea=(54193.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.4e+45, 's^-1'), n=-9.81, Ea=(52468.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.98e+35, 's^-1'), n=-6.54, Ea=(49429, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.2e+26, 's^-1'), n=-3.61, Ea=(46333.1, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1378,
    label = "IC4H7 + NC3H7O2 <=> IC4H7O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1379,
    label = "IC4H7 + PC4H9O2 <=> IC4H7O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1380,
    label = "IC4H7 + SC4H9O2 <=> IC4H7O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1381,
    label = "IC4H7 + IC3H7O2 <=> IC4H7O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1382,
    label = "IC4H7 + TC4H9O2 <=> IC4H7O + TC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1383,
    label = "IC4H7 + IC4H7 <=> C3H4-A + AC5H10",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 4, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.1e+40, 'cm^3/(mol*s)'),
                n = -9.3,
                Ea = (12470, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.41e+32, 'cm^3/(mol*s)'),
                n = -6.8,
                Ea = (9180, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.26e+28, 'cm^3/(mol*s)'),
                n = -5.5,
                Ea = (7410, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1384,
    label = "IC4H7 + IC4H7 <=> H15DE25DM",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.039, 0.078, 0.156], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.27e+64, 'cm^3/(mol*s)'),
                n = -15.935,
                Ea = (20230, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.5e+59, 'cm^3/(mol*s)'),
                n = -14.49,
                Ea = (18600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.14e+55, 'cm^3/(mol*s)'),
                n = -12.995,
                Ea = (16700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1385,
    label = "H15DE25DM + H <=> H15DE25DM-S + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+06, 'cm^3/(mol*s)'),
        n = 2.31517,
        Ea = (2075.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1386,
    label = "H15DE25DM + O2 <=> H15DE25DM-S + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(38890, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1387,
    label = "H15DE25DM + O <=> H15DE25DM-S + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.59243e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (13, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1388,
    label = "H15DE25DM + OH <=> H15DE25DM-S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(89500, 'cm^3/(mol*s)'), n=2.63697, Ea=(-6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1389,
    label = "H15DE25DM + HO2 <=> H15DE25DM-S + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1, 'cm^3/(mol*s)'),
        n = 3.88737,
        Ea = (9386.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1390,
    label = "H15DE25DM + CH3 <=> H15DE25DM-S + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1, 'cm^3/(mol*s)'),
        n = 3.64902,
        Ea = (3374.05, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1391,
    label = "H15DE25DM + H <=> H15DE25DM-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (729000, 'cm^3/(mol*s)'),
        n = 2.455,
        Ea = (4361.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1392,
    label = "H15DE25DM + O2 <=> H15DE25DM-A + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.86e+09, 'cm^3/(mol*s)'),
        n = 1.301,
        Ea = (40939, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1393,
    label = "H15DE25DM + O <=> H15DE25DM-A + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+12, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1394,
    label = "H15DE25DM + OH <=> H15DE25DM-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (253000, 'cm^3/(mol*s)'),
        n = 2.46,
        Ea = (729.44, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1395,
    label = "H15DE25DM + HO2 <=> H15DE25DM-A + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.292, 'cm^3/(mol*s)'), n=4.12, Ea=(12802, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1396,
    label = "H15DE25DM + CH3 <=> H15DE25DM-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.42, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1397,
    label = "C3H5-T + B13DE2M <=> H15DE25DM-S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7070, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1398,
    label = "C3H4-A + AC5H9-D <=> H15DE25DM-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(28400, 'cm^3/(mol*s)'), n=2.5, Ea=(8847.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1399,
    label = "H15DE25DM-S + HO2 <=> H15DE25DM-SO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1400,
    label = "IC3H5CHO + IC4H7 <=> H15DE25DM-SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6329.74, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1401,
    label = "C3H5-T + IC4H7CHO <=> H15DE25DM-SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15526.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1402,
    label = "IC4H7CHO + OH => CH2CHO + C3H4-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.064e+07, 'cm^3/(mol*s)'),
        n = 2.46,
        Ea = (729.44, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1403,
    label = "H15DE25DM-A + HO2 <=> H15DE25DM-AO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1404,
    label = "H15DE2M-T + CH2O <=> H15DE25DM-AO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4786.58, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1405,
    label = "IC4H7 + C3H4-A <=> H15DE2M-T",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1406,
    label = "IC4H7-I1 + H <=> C3H4-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.333e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1407,
    label = "IC4H7-I1 + H <=> C3H4-P + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1408,
    label = "IC4H7-I1 + O <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1409,
    label = "IC4H7-I1 + OH => C3H6 + HCO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1410,
    label = "IC4H7-I1 + HO2 => C3H6 + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1411,
    label = "IC4H7-I1 + HCO <=> IC4H8 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1412,
    label = "IC4H7-I1 + CH3 <=> C3H4-P + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1413,
    label = "IC4H7-I1 + O2 <=> CH3COCH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+31, 'cm^3/(mol*s)'),
        n = -5.944,
        Ea = (5748.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1414,
    label = "IC4H7-I1 + O2 <=> TC3H6CHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.38e+18, 'cm^3/(mol*s)'),
        n = -2.14,
        Ea = (5142.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1415,
    label = "IC4H7-I1 + O2 <=> IC3H5CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+19, 'cm^3/(mol*s)'),
        n = -2.14,
        Ea = (5142.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1416,
    label = "IC4H7 + O2 <=> IC4H7O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.09e+10, 'cm^3/(mol*s)'),
        n = 0.56725,
        Ea = (2290, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1417,
    label = "IC4H7 + O <=> IC3H5CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1418,
    label = "IC4H7O2 <=> IC4H6OOH-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(141000, 's^-1'), n=1.83586, Ea=(19820, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1419,
    label = "IC4H7O2 <=> CCYCCOOC-T1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.19e+08, 's^-1'), n=0.80412, Ea=(28020, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1420,
    label = "IC4H7O2 <=> C2CYCOOC-I1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07e+08, 's^-1'), n=0.89161, Ea=(29720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1421,
    label = "IC4H7O2 <=> IC4H7O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.82e+14, 's^-1'), n=0, Ea=(60620, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1422,
    label = "IC4H7O2 <=> IC3H5CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.52e+09, 's^-1'), n=1.02524, Ea=(39460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1423,
    label = "IC4H6OOH-I <=> C3H4-A + CH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+12, 's^-1'), n=0.91203, Ea=(51390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1424,
    label = "IC4H6OOH-I <=> IC3H5CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+09, 's^-1'), n=0.8739, Ea=(54090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1425,
    label = "CCYCCOOC-T1 <=> CCYC2OCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+11, 's^-1'), n=0.92729, Ea=(17470, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1426,
    label = "CCYCCOOC-T1 <=> CCYCCOOC-I2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.56e+13, 's^-1'), n=0, Ea=(38820, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1427,
    label = "CCYCCOOC-I2 <=> CHOIC3H6O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.19e+14, 's^-1'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1428,
    label = "C2CYCOOC-I1 <=> IC3H5OOCH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.41e+13, 's^-1'), n=-0.22618, Ea=(18500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1429,
    label = "IC3H5OOCH2 <=> CH3COCH2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+10, 's^-1'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1430,
    label = "CHOIC3H6O <=> CH3CHCHO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+12, 's^-1'), n=0, Ea=(9780, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1431,
    label = "CCYC2OCO <=> CCYCCO-T1 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74e+13, 's^-1'), n=0, Ea=(18150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1432,
    label = "C2CYCOOC-I1 <=> CCYC2OCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 's^-1'), n=0.1018, Ea=(20320, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1433,
    label = "IC4H7O2 + IC4H7O2 => IC4H7O + IC4H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1434,
    label = "IC4H7O2 + IC4H8 <=> IC4H7 + IC4H7OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.146, 'cm^3/(mol*s)'), n=4.12, Ea=(12802, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1435,
    label = "IC4H8 + H <=> IC4H9",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (7.99e+81, 'cm^3/(mol*s)'),
                        n = -23.161,
                        Ea = (22239, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.24e+68, 'cm^3/(mol*s)'),
                        n = -18.427,
                        Ea = (19665, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.04e+49, 'cm^3/(mol*s)'),
                        n = -11.5,
                        Ea = (15359, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.2e+41, 'cm^3/(mol*s)'),
                        n = -8.892,
                        Ea = (14637, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.85e+26, 'cm^3/(mol*s)'),
                        n = -5.83,
                        Ea = (3865.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.82e+30, 'cm^3/(mol*s)'),
                        n = -6.49,
                        Ea = (5470.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.78e+28, 'cm^3/(mol*s)'),
                        n = -5.57,
                        Ea = (5625.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.46e+25, 'cm^3/(mol*s)'),
                        n = -4.28,
                        Ea = (5247.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.22e+27, 'cm^3/(mol*s)'),
                        n = -4.39,
                        Ea = (9345.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1436,
    label = "IC4H8 + H <=> TC4H9",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.35e+44, 'cm^3/(mol*s)'),
                        n = -10.68,
                        Ea = (8196.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.11e+57, 'cm^3/(mol*s)'),
                        n = -14.23,
                        Ea = (15147, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.26e+61, 'cm^3/(mol*s)'),
                        n = -14.94,
                        Ea = (20161, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.3e+56, 'cm^3/(mol*s)'),
                        n = -13.12,
                        Ea = (20667, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.11e+50, 'cm^3/(mol*s)'),
                        n = -10.8,
                        Ea = (20202, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.17e+130, 'cm^3/(mol*s)'),
                        n = -32.58,
                        Ea = (136140, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.25e+29, 'cm^3/(mol*s)'),
                        n = -5.84,
                        Ea = (4241.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+30, 'cm^3/(mol*s)'),
                        n = -5.63,
                        Ea = (5613.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.11e+26, 'cm^3/(mol*s)'),
                        n = -4.44,
                        Ea = (5182.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.73e+23, 'cm^3/(mol*s)'),
                        n = -3.26,
                        Ea = (4597, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1437,
    label = "IC4H8 + H <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (5.13e+08, 'cm^3/(mol*s)'),
                        n = 1.35,
                        Ea = (2542, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.63e+10, 'cm^3/(mol*s)'),
                        n = 0.87,
                        Ea = (3599.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.9e+11, 'cm^3/(mol*s)'),
                        n = 0.47,
                        Ea = (5431.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.08e+22, 'cm^3/(mol*s)'),
                        n = -2.6,
                        Ea = (12898, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.4e+22, 'cm^3/(mol*s)'),
                        n = -2.42,
                        Ea = (16500, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(770, 'cm^3/(mol*s)'), n=1.35, Ea=(2542, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (39400, 'cm^3/(mol*s)'),
                        n = 0.87,
                        Ea = (3599.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.34e+06, 'cm^3/(mol*s)'),
                        n = 0.47,
                        Ea = (5431.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (41300, 'cm^3/(mol*s)'),
                        n = 2.52,
                        Ea = (3679.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(837, 'cm^3/(mol*s)'), n=2.91, Ea=(3980.9, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 1438,
    label = "IC4H8 + HO2 <=> TC4H9O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.104, 'cm^3/(mol*s)'), n=3.45, Ea=(4338, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1439,
    label = "IC4H8 + HO2 <=> IC4H8O2H-T",
    degeneracy = 1,
    kinetics = Arrhenius(A=(16400, 'cm^3/(mol*s)'), n=2.43, Ea=(8300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1440,
    label = "IC4H8 + HO2 <=> TC4H8O2H-I",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.67e+14, 'cm^3/(mol*s)'),
                n = -2.14,
                Ea = (14188, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.25e+06, 'cm^3/(mol*s)'),
                n = 0.64,
                Ea = (9073, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.96e+06, 'cm^3/(mol*s)'),
                n = 0.82,
                Ea = (8771, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.05e+13, 'cm^3/(mol*s)'),
                n = -0.82,
                Ea = (12919, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1441,
    label = "IC4H8 + HO2 <=> IC4H8O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
            Arrhenius(A=(11800, 'cm^3/(mol*s)'), n=2.29, Ea=(11321, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(53000, 'cm^3/(mol*s)'), n=2.1, Ea=(11797, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.47e+09, 'cm^3/(mol*s)'),
                n = 0.83,
                Ea = (14808, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.96e+17, 'cm^3/(mol*s)'),
                n = -1.45,
                Ea = (21195, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1442,
    label = "TC4H8O2H-I <=> IC4H8O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.23e+17, 's^-1'), n=-2.97, Ea=(8215, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.39e+22, 's^-1'), n=-3.9, Ea=(11424, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4e+25, 's^-1'), n=-4.5, Ea=(13952, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.21e+27, 's^-1'), n=-4.66, Ea=(16324, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1443,
    label = "IC4H8 + O <=> IC3H7 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.45e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1444,
    label = "IC4H8 + O => CH2CO + CH3 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.05e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1445,
    label = "IC4H8 + O => IC3H6CO + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.05e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1446,
    label = "IC4H8 + OH <=> IC4H7OH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.67e+13, 'cm^3/(mol*s)'),
                n = 0.05,
                Ea = (10611, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.75e+13, 'cm^3/(mol*s)'),
                n = 0.05,
                Ea = (10623, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.87e+13, 'cm^3/(mol*s)'),
                n = 0.04,
                Ea = (10634, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.59e+14, 'cm^3/(mol*s)'),
                n = -0.16,
                Ea = (11125, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.1e+14, 'cm^3/(mol*s)'),
                n = -0.22,
                Ea = (11407, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+14, 'cm^3/(mol*s)'),
                n = -0.24,
                Ea = (11458, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.15e+07, 'cm^3/(mol*s)'),
                n = 1.42,
                Ea = (10087, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (366000, 'cm^3/(mol*s)'),
                n = 2.14,
                Ea = (10410, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(819, 'cm^3/(mol*s)'), n=2.84, Ea=(10481, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1447,
    label = "IC4H8 + OH <=> SC3H5OH + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(516000, 'cm^3/(mol*s)'), n=1.65, Ea=(1233, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7280, 'cm^3/(mol*s)'), n=2.1, Ea=(1162, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(816, 'cm^3/(mol*s)'), n=2.48, Ea=(1128, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(115, 'cm^3/(mol*s)'), n=2.8, Ea=(1152, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.6, 'cm^3/(mol*s)'), n=3.21, Ea=(1208, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.08, 'cm^3/(mol*s)'), n=3.29, Ea=(1216, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4520, 'cm^3/(mol*s)'), n=2.5, Ea=(3238, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (9.64e+18, 'cm^3/(mol*s)'),
                n = -1.74,
                Ea = (13107, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(0.132, 'cm^3/(mol*s)'), n=3.7, Ea=(3665, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1448,
    label = "IC4H8 + OH <=> IC3H5OH + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.06e+06, 'cm^3/(mol*s)'),
                n = 1.65,
                Ea = (1233, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(29100, 'cm^3/(mol*s)'), n=2.1, Ea=(1162, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3260, 'cm^3/(mol*s)'), n=2.48, Ea=(1128, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(461, 'cm^3/(mol*s)'), n=2.8, Ea=(1152, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(22.4, 'cm^3/(mol*s)'), n=3.21, Ea=(1208, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(12.3, 'cm^3/(mol*s)'), n=3.29, Ea=(1216, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(18100, 'cm^3/(mol*s)'), n=2.5, Ea=(3238, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (3.86e+19, 'cm^3/(mol*s)'),
                n = -1.74,
                Ea = (13107, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(0.528, 'cm^3/(mol*s)'), n=3.7, Ea=(3665, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1449,
    label = "IC4H8 + OH <=> SC4H7OH-I + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.87, 'cm^3/(mol*s)'), n=2.92, Ea=(625, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.484, 'cm^3/(mol*s)'), n=2.98, Ea=(704, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.313, 'cm^3/(mol*s)'), n=3.04, Ea=(721, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.00933, 'cm^3/(mol*s)'), n=3.62, Ea=(677, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.64e-05, 'cm^3/(mol*s)'),
                n = 4.48,
                Ea = (687, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.71e-05, 'cm^3/(mol*s)'),
                n = 4.56,
                Ea = (707, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.65e-07, 'cm^3/(mol*s)'),
                n = 5.05,
                Ea = (874, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.64e+15, 'cm^3/(mol*s)'),
                n = -0.8,
                Ea = (12728, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.000487, 'cm^3/(mol*s)'),
                n = 4.32,
                Ea = (4020, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1450,
    label = "IC4H8 + OH <=> CH3COCH3 + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(693000, 'cm^3/(mol*s)'), n=1.49, Ea=(-536, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5940, 'cm^3/(mol*s)'), n=2.01, Ea=(-560, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1100, 'cm^3/(mol*s)'), n=2.22, Ea=(-680, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(107, 'cm^3/(mol*s)'), n=2.5, Ea=(-759, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.783, 'cm^3/(mol*s)'), n=3.1, Ea=(-919, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.307, 'cm^3/(mol*s)'), n=3.22, Ea=(-946, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (0.000316, 'cm^3/(mol*s)'),
                n = 4.05,
                Ea = (-1144, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.59e-06, 'cm^3/(mol*s)'),
                n = 4.49,
                Ea = (-680, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.45e-05, 'cm^3/(mol*s)'),
                n = 4.22,
                Ea = (1141, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1451,
    label = "IC4H8 + OH <=> IC4H8OH-IT",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.3e+78, 'cm^3/(mol*s)'),
                        n = -20.7,
                        Ea = (32402, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.74e+77, 'cm^3/(mol*s)'),
                        n = -20,
                        Ea = (33874, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.07e+76, 'cm^3/(mol*s)'),
                        n = -19.58,
                        Ea = (32874, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.68e+73, 'cm^3/(mol*s)'),
                        n = -18.79,
                        Ea = (31361, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.04e+68, 'cm^3/(mol*s)'),
                        n = -17.01,
                        Ea = (27909, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.23e+66, 'cm^3/(mol*s)'),
                        n = -16.64,
                        Ea = (27162, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.95e+59, 'cm^3/(mol*s)'),
                        n = -14.17,
                        Ea = (23079, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.58e+53, 'cm^3/(mol*s)'),
                        n = -12.23,
                        Ea = (22976, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.43e+48, 'cm^3/(mol*s)'),
                        n = -10.23,
                        Ea = (23772, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (6.41e+59, 'cm^3/(mol*s)'),
                        n = -15.84,
                        Ea = (11594, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.28e+59, 'cm^3/(mol*s)'),
                        n = -15.51,
                        Ea = (12898, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.79e+59, 'cm^3/(mol*s)'),
                        n = -15.34,
                        Ea = (12913, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.65e+58, 'cm^3/(mol*s)'),
                        n = -14.93,
                        Ea = (12936, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.35e+56, 'cm^3/(mol*s)'),
                        n = -14.04,
                        Ea = (12945, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.98e+55, 'cm^3/(mol*s)'),
                        n = -13.85,
                        Ea = (12887, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.55e+50, 'cm^3/(mol*s)'),
                        n = -12.04,
                        Ea = (11493, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.41e+41, 'cm^3/(mol*s)'),
                        n = -9.35,
                        Ea = (8921, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.3e+32, 'cm^3/(mol*s)'),
                        n = -6.31,
                        Ea = (6088, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1452,
    label = "IC4H8 + OH <=> IC4H8OH-TI",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.14e+59, 'cm^3/(mol*s)'),
                        n = -15.84,
                        Ea = (11594, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.43e+59, 'cm^3/(mol*s)'),
                        n = -15.51,
                        Ea = (12898, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.3e+58, 'cm^3/(mol*s)'),
                        n = -15.34,
                        Ea = (12913, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.83e+57, 'cm^3/(mol*s)'),
                        n = -14.93,
                        Ea = (12936, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.5e+55, 'cm^3/(mol*s)'),
                        n = -14.04,
                        Ea = (12945, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.33e+55, 'cm^3/(mol*s)'),
                        n = -13.85,
                        Ea = (12887, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.18e+49, 'cm^3/(mol*s)'),
                        n = -12.04,
                        Ea = (11493, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.14e+41, 'cm^3/(mol*s)'),
                        n = -9.35,
                        Ea = (8921, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.65e+31, 'cm^3/(mol*s)'),
                        n = -6.31,
                        Ea = (6088, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.1315, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (7.68e+77, 'cm^3/(mol*s)'),
                        n = -20.7,
                        Ea = (32402, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.13e+76, 'cm^3/(mol*s)'),
                        n = -20,
                        Ea = (33874, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.55e+75, 'cm^3/(mol*s)'),
                        n = -19.58,
                        Ea = (32874, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.23e+73, 'cm^3/(mol*s)'),
                        n = -18.79,
                        Ea = (31361, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.45e+67, 'cm^3/(mol*s)'),
                        n = -17.01,
                        Ea = (27909, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.41e+66, 'cm^3/(mol*s)'),
                        n = -16.64,
                        Ea = (27162, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.5e+58, 'cm^3/(mol*s)'),
                        n = -14.17,
                        Ea = (23079, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.53e+53, 'cm^3/(mol*s)'),
                        n = -12.23,
                        Ea = (22976, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.78e+47, 'cm^3/(mol*s)'),
                        n = -10.23,
                        Ea = (23772, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1453,
    label = "IC4H8OH-IT + O2 <=> TQJC4H8OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.05e+114, 'cm^3/(mol*s)'),
                n = -33.81,
                Ea = (24741, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.13e+114, 'cm^3/(mol*s)'),
                n = -33.44,
                Ea = (26448, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.62e+110, 'cm^3/(mol*s)'),
                n = -31.75,
                Ea = (26612, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6e+101, 'cm^3/(mol*s)'),
                n = -28.79,
                Ea = (25197, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.36e+89, 'cm^3/(mol*s)'),
                n = -24.76,
                Ea = (22402, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.55e+81, 'cm^3/(mol*s)'),
                n = -21.95,
                Ea = (20197, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.51e+75, 'cm^3/(mol*s)'),
                n = -20,
                Ea = (18578, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.16e+70, 'cm^3/(mol*s)'),
                n = -18.48,
                Ea = (17287, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1454,
    label = "IC4H8OH-IT + O2 <=> IC4H7OH + HO2",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.21e+26, 'cm^3/(mol*s)'),
                        n = -5.09,
                        Ea = (5755, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.41e+31, 'cm^3/(mol*s)'),
                        n = -6.55,
                        Ea = (8781, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.08e+34, 'cm^3/(mol*s)'),
                        n = -7.53,
                        Ea = (11702, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.67e+34, 'cm^3/(mol*s)'),
                        n = -7.27,
                        Ea = (13418, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.82e+28, 'cm^3/(mol*s)'),
                        n = -5.41,
                        Ea = (13318, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.5e+22, 'cm^3/(mol*s)'),
                        n = -3.52,
                        Ea = (12314, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.82e+17, 'cm^3/(mol*s)'),
                        n = -1.99,
                        Ea = (11286, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.93e+13, 'cm^3/(mol*s)'),
                        n = -0.71,
                        Ea = (10340, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.45e+21, 'cm^3/(mol*s)'),
                        n = -4.19,
                        Ea = (6837, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.4e+30, 'cm^3/(mol*s)'),
                        n = -6.75,
                        Ea = (11554, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.11e+39, 'cm^3/(mol*s)'),
                        n = -9.56,
                        Ea = (17834, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.16e+42, 'cm^3/(mol*s)'),
                        n = -10.17,
                        Ea = (22412, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.07e+32, 'cm^3/(mol*s)'),
                        n = -6.94,
                        Ea = (22738, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.88e+20, 'cm^3/(mol*s)'),
                        n = -3.14,
                        Ea = (20677, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.32e+10, 'cm^3/(mol*s)'),
                        n = -0.03,
                        Ea = (18552, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(122, 'cm^3/(mol*s)'), n=2.57, Ea=(16623, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 1455,
    label = "IC4H8OH-IT + O2 <=> SC4H7OH-I + HO2",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.26e+25, 'cm^3/(mol*s)'),
                        n = -4.69,
                        Ea = (5755, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.44e+30, 'cm^3/(mol*s)'),
                        n = -6.15,
                        Ea = (8785, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.78e+33, 'cm^3/(mol*s)'),
                        n = -7.11,
                        Ea = (11695, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.4e+33, 'cm^3/(mol*s)'),
                        n = -6.84,
                        Ea = (13395, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.12e+27, 'cm^3/(mol*s)'),
                        n = -4.96,
                        Ea = (13277, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.78e+21, 'cm^3/(mol*s)'),
                        n = -3.07,
                        Ea = (12265, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.97e+16, 'cm^3/(mol*s)'),
                        n = -1.53,
                        Ea = (11234, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.32e+12, 'cm^3/(mol*s)'),
                        n = -0.25,
                        Ea = (10285, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (3.22e+23, 'cm^3/(mol*s)'),
                        n = -4.69,
                        Ea = (5341, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.8e+28, 'cm^3/(mol*s)'),
                        n = -6.18,
                        Ea = (8461, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.71e+32, 'cm^3/(mol*s)'),
                        n = -7.16,
                        Ea = (11410, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.53e+32, 'cm^3/(mol*s)'),
                        n = -7.02,
                        Ea = (13378, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.55e+29, 'cm^3/(mol*s)'),
                        n = -6.14,
                        Ea = (15100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.72e+26, 'cm^3/(mol*s)'),
                        n = -4.97,
                        Ea = (15849, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.46e+21, 'cm^3/(mol*s)'),
                        n = -3.51,
                        Ea = (15644, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.06e+16, 'cm^3/(mol*s)'),
                        n = -1.96,
                        Ea = (14979, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1456,
    label = "IC4H8OH-IT + O2 <=> TQC4H8OI",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.36e+104, 'cm^3/(mol*s)'),
                n = -33.74,
                Ea = (22390, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.96e+103, 'cm^3/(mol*s)'),
                n = -33.01,
                Ea = (22966, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.99e+96, 'cm^3/(mol*s)'),
                n = -30.48,
                Ea = (20584, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.04e+88, 'cm^3/(mol*s)'),
                n = -27.47,
                Ea = (16629, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.13e+96, 'cm^3/(mol*s)'),
                n = -29.62,
                Ea = (20346, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.79e+105, 'cm^3/(mol*s)'),
                n = -32.04,
                Ea = (24971, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.64e+109, 'cm^3/(mol*s)'),
                n = -33.12,
                Ea = (27657, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.06e+111, 'cm^3/(mol*s)'),
                n = -33.48,
                Ea = (29197, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1457,
    label = "IC4H8OH-IT + O2 => CH3COCH3 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.03e+37, 'cm^3/(mol*s)'),
                n = -8.35,
                Ea = (6940, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.07e+42, 'cm^3/(mol*s)'),
                n = -9.64,
                Ea = (9965, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.22e+43, 'cm^3/(mol*s)'),
                n = -10.12,
                Ea = (12427, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.14e+42, 'cm^3/(mol*s)'),
                n = -9.42,
                Ea = (13806, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.8e+38, 'cm^3/(mol*s)'),
                n = -8.13,
                Ea = (15131, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.61e+34, 'cm^3/(mol*s)'),
                n = -6.8,
                Ea = (15691, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7e+29, 'cm^3/(mol*s)'),
                n = -5.41,
                Ea = (15552, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.74e+25, 'cm^3/(mol*s)'),
                n = -4.06,
                Ea = (15118, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1458,
    label = "IC4H8OH-IT + O2 <=> QC4H7OHP",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.18e+118, 'cm^3/(mol*s)'),
                n = -37.6,
                Ea = (26229, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.91e+131, 'cm^3/(mol*s)'),
                n = -40.73,
                Ea = (34079, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.81e+138, 'cm^3/(mol*s)'),
                n = -42.17,
                Ea = (40750, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.05e+134, 'cm^3/(mol*s)'),
                n = -40.19,
                Ea = (43580, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.07e+117, 'cm^3/(mol*s)'),
                n = -34.26,
                Ea = (41516, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.71e+101, 'cm^3/(mol*s)'),
                n = -29.04,
                Ea = (38094, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.25e+89, 'cm^3/(mol*s)'),
                n = -25.15,
                Ea = (35203, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.98e+79, 'cm^3/(mol*s)'),
                n = -22.09,
                Ea = (32802, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1459,
    label = "IC4H8OH-IT + O2 <=> CCY(CCO)COH + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.11e+18, 'cm^3/(mol*s)'),
                n = -2.87,
                Ea = (6870, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.02e+27, 'cm^3/(mol*s)'),
                n = -5.54,
                Ea = (11842, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.36e+37, 'cm^3/(mol*s)'),
                n = -8.29,
                Ea = (18165, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.21e+39, 'cm^3/(mol*s)'),
                n = -8.66,
                Ea = (22517, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.53e+28, 'cm^3/(mol*s)'),
                n = -5.13,
                Ea = (22530, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.72e+15, 'cm^3/(mol*s)'),
                n = -1.16,
                Ea = (20283, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (106000, 'cm^3/(mol*s)'),
                n = 2.06,
                Ea = (18044, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.00023, 'cm^3/(mol*s)'),
                n = 4.73,
                Ea = (16037, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1460,
    label = "IC4H8OH-IT + O2 <=> TQC4H7OHI",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.76e+53, 'cm^3/(mol*s)'),
                n = -19.87,
                Ea = (9019, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.68e+67, 'cm^3/(mol*s)'),
                n = -23.92,
                Ea = (11892, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.07e+91, 'cm^3/(mol*s)'),
                n = -30.58,
                Ea = (17347, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.84e+100, 'cm^3/(mol*s)'),
                n = -32.4,
                Ea = (20041, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.16e+115, 'cm^3/(mol*s)'),
                n = -35.81,
                Ea = (27656, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.87e+123, 'cm^3/(mol*s)'),
                n = -37.83,
                Ea = (33314, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.95e+124, 'cm^3/(mol*s)'),
                n = -37.82,
                Ea = (35683, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.58e+122, 'cm^3/(mol*s)'),
                n = -36.86,
                Ea = (36374, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1461,
    label = "IC4H8OH-IT + O2 <=> C2CY(COC)OH + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.42e+32, 'cm^3/(mol*s)'),
                n = -6.95,
                Ea = (6210, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.19e+36, 'cm^3/(mol*s)'),
                n = -8.24,
                Ea = (9233, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.77e+38, 'cm^3/(mol*s)'),
                n = -8.76,
                Ea = (11715, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.86e+36, 'cm^3/(mol*s)'),
                n = -7.95,
                Ea = (12823, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.37e+32, 'cm^3/(mol*s)'),
                n = -6.51,
                Ea = (13646, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.15e+29, 'cm^3/(mol*s)'),
                n = -5.56,
                Ea = (14541, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.2e+26, 'cm^3/(mol*s)'),
                n = -4.51,
                Ea = (14778, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.31e+22, 'cm^3/(mol*s)'),
                n = -3.37,
                Ea = (14606, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1462,
    label = "TQJC4H8OH <=> IC4H7OH + HO2",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
                arrhenius = [
                    Arrhenius(A=(9.73e+65, 's^-1'), n=-18.5, Ea=(42975, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.04e+64, 's^-1'), n=-17.25, Ea=(44419, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.9e+59, 's^-1'), n=-15.59, Ea=(44504, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.35e+53, 's^-1'), n=-13.49, Ea=(43566, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.13e+44, 's^-1'), n=-10.39, Ea=(41279, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.57e+38, 's^-1'), n=-8.49, Ea=(39745, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.32e+34, 's^-1'), n=-7.23, Ea=(38675, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.46e+31, 's^-1'), n=-6.28, Ea=(37849, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
                arrhenius = [
                    Arrhenius(A=(5.27e+64, 's^-1'), n=-18, Ea=(42872, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.82e+62, 's^-1'), n=-16.74, Ea=(44284, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.42e+58, 's^-1'), n=-15.07, Ea=(44348, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.05e+52, 's^-1'), n=-12.97, Ea=(43402, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.93e+43, 's^-1'), n=-9.88, Ea=(41120, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.28e+37, 's^-1'), n=-7.99, Ea=(39593, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.35e+33, 's^-1'), n=-6.74, Ea=(38527, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.13e+30, 's^-1'), n=-5.79, Ea=(37706, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 1463,
    label = "TQJC4H8OH <=> TQC4H8OI",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.78e+50, 's^-1'), n=-12.91, Ea=(31539, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.42e+45, 's^-1'), n=-10.94, Ea=(30864, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+40, 's^-1'), n=-9.21, Ea=(29932, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.12e+35, 's^-1'), n=-7.64, Ea=(28864, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.73e+29, 's^-1'), n=-5.67, Ea=(27243, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.88e+25, 's^-1'), n=-4.54, Ea=(26272, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.6e+23, 's^-1'), n=-3.8, Ea=(25622, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.08e+21, 's^-1'), n=-3.25, Ea=(25131, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1464,
    label = "TQJC4H8OH <=> QC4H7OHP",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.16e+62, 's^-1'), n=-18.02, Ea=(45297, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.56e+62, 's^-1'), n=-17.1, Ea=(47393, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.25e+59, 's^-1'), n=-15.61, Ea=(47984, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.97e+53, 's^-1'), n=-13.49, Ea=(47281, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.91e+43, 's^-1'), n=-10.15, Ea=(44926, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.68e+36, 's^-1'), n=-8.05, Ea=(43267, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.49e+32, 's^-1'), n=-6.64, Ea=(42089, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.77e+29, 's^-1'), n=-5.57, Ea=(41173, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1465,
    label = "TQJC4H8OH <=> TQC4H7OHI",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.57e+58, 's^-1'), n=-15.99, Ea=(38293, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.27e+54, 's^-1'), n=-14.25, Ea=(38593, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.3e+49, 's^-1'), n=-12.44, Ea=(38031, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.9e+44, 's^-1'), n=-10.51, Ea=(36905, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.18e+36, 's^-1'), n=-7.9, Ea=(34865, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.1e+31, 's^-1'), n=-6.36, Ea=(33581, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3e+28, 's^-1'), n=-5.35, Ea=(32704, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.34e+26, 's^-1'), n=-4.59, Ea=(32035, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1466,
    label = "TQC4H8OI => CH3COCH3 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.09e+38, 's^-1'), n=-9.91, Ea=(19096, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.09e+39, 's^-1'), n=-9.93, Ea=(19135, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.89e+41, 's^-1'), n=-10.02, Ea=(19407, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.47e+23, 's^-1'), n=-4.1, Ea=(14658, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.95e+33, 's^-1'), n=-6.75, Ea=(18685, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.24e+36, 's^-1'), n=-7.56, Ea=(20307, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.83e+36, 's^-1'), n=-7.54, Ea=(20747, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.63e+35, 's^-1'), n=-7.17, Ea=(20641, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1467,
    label = "QC4H7OHP <=> IC4H7OH + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.29e+57, 's^-1'), n=-15.64, Ea=(28576, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.65e+58, 's^-1'), n=-15.75, Ea=(29927, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.19e+50, 's^-1'), n=-12.66, Ea=(28547, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.67e+49, 's^-1'), n=-12.05, Ea=(29204, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.08e+40, 's^-1'), n=-9.26, Ea=(27188, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.32e+30, 's^-1'), n=-5.82, Ea=(24071, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.15e+30, 's^-1'), n=-5.8, Ea=(24053, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.12e+30, 's^-1'), n=-5.8, Ea=(24050, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1468,
    label = "QC4H7OHP <=> CCY(CCO)COH + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.11e+51, 's^-1'), n=-12.97, Ea=(28497, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.58e+51, 's^-1'), n=-12.87, Ea=(29529, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.03e+44, 's^-1'), n=-10.28, Ea=(28326, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.42e+44, 's^-1'), n=-9.98, Ea=(28986, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.69e+37, 's^-1'), n=-7.93, Ea=(27491, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.9e+29, 's^-1'), n=-5.3, Ea=(25095, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.27e+29, 's^-1'), n=-5.29, Ea=(25081, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.15e+29, 's^-1'), n=-5.28, Ea=(25078, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1469,
    label = "TQC4H7OHI <=> C2CY(COC)OH + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.1e+31, 's^-1'), n=-7.21, Ea=(14640, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.37e+32, 's^-1'), n=-7.24, Ea=(14716, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.34e+33, 's^-1'), n=-7.35, Ea=(15127, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.86e+23, 's^-1'), n=-3.68, Ea=(12864, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.88e+31, 's^-1'), n=-6.23, Ea=(16040, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.25e+34, 's^-1'), n=-6.78, Ea=(17056, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.73e+33, 's^-1'), n=-6.67, Ea=(17176, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.13e+33, 's^-1'), n=-6.45, Ea=(17170, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1470,
    label = "TQC4H7OHI <=> SC4H7OH-I + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.01e+27, 's^-1'), n=-7.27, Ea=(14658, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.78e+28, 's^-1'), n=-7.3, Ea=(14733, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.27e+30, 's^-1'), n=-7.48, Ea=(15191, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.81e+17, 's^-1'), n=-2.82, Ea=(12336, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.92e+26, 's^-1'), n=-5.22, Ea=(16146, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.61e+27, 's^-1'), n=-5.49, Ea=(17483, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.91e+26, 's^-1'), n=-4.86, Ea=(17429, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.94e+24, 's^-1'), n=-4.18, Ea=(17285, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1471,
    label = "IC4H8OH-TI + O2 <=> IQJC4H8OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.34e+111, 'cm^3/(mol*s)'),
                n = -32.67,
                Ea = (25143, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.84e+107, 'cm^3/(mol*s)'),
                n = -31.05,
                Ea = (25460, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.41e+100, 'cm^3/(mol*s)'),
                n = -28.42,
                Ea = (24474, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.55e+89, 'cm^3/(mol*s)'),
                n = -24.78,
                Ea = (22176, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.14e+76, 'cm^3/(mol*s)'),
                n = -20.31,
                Ea = (18721, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.25e+66, 'cm^3/(mol*s)'),
                n = -17.35,
                Ea = (16238, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.2e+60, 'cm^3/(mol*s)'),
                n = -15.36,
                Ea = (14499, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.3e+56, 'cm^3/(mol*s)'),
                n = -13.86,
                Ea = (13159, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1472,
    label = "IC4H8OH-TI + O2 <=> IC3H6OHCHO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.59e+15, 'cm^3/(mol*s)'),
                n = -1.63,
                Ea = (8947, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.07e+20, 'cm^3/(mol*s)'),
                n = -3.24,
                Ea = (11938, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5e+25, 'cm^3/(mol*s)'),
                n = -4.66,
                Ea = (15251, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.18e+26, 'cm^3/(mol*s)'),
                n = -4.79,
                Ea = (17388, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6e+20, 'cm^3/(mol*s)'),
                n = -2.95,
                Ea = (17297, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.7e+14, 'cm^3/(mol*s)'),
                n = -0.91,
                Ea = (16099, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.91e+08, 'cm^3/(mol*s)'),
                n = 0.73,
                Ea = (14913, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(30300, 'cm^3/(mol*s)'), n=2.08, Ea=(13854, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1473,
    label = "IC4H8OH-TI + O2 <=> IQC4H8OT",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.12e+102, 'cm^3/(mol*s)'),
                n = -32.4,
                Ea = (23496, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.23e+95, 'cm^3/(mol*s)'),
                n = -30.04,
                Ea = (22067, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.45e+83, 'cm^3/(mol*s)'),
                n = -26.08,
                Ea = (17114, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.16e+82, 'cm^3/(mol*s)'),
                n = -25.61,
                Ea = (16198, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.04e+97, 'cm^3/(mol*s)'),
                n = -29.54,
                Ea = (22648, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.25e+103, 'cm^3/(mol*s)'),
                n = -31.42,
                Ea = (26487, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.48e+106, 'cm^3/(mol*s)'),
                n = -32.06,
                Ea = (28397, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.39e+107, 'cm^3/(mol*s)'),
                n = -32.2,
                Ea = (29446, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1474,
    label = "IC4H8OH-TI + O2 => CH3COCH3 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.39e+48, 'cm^3/(mol*s)'),
                n = -11.88,
                Ea = (11603, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.82e+50, 'cm^3/(mol*s)'),
                n = -12.49,
                Ea = (14143, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.43e+49, 'cm^3/(mol*s)'),
                n = -11.94,
                Ea = (15561, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.43e+45, 'cm^3/(mol*s)'),
                n = -10.56,
                Ea = (16415, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.98e+39, 'cm^3/(mol*s)'),
                n = -8.68,
                Ea = (17473, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.99e+33, 'cm^3/(mol*s)'),
                n = -6.83,
                Ea = (17502, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.02e+29, 'cm^3/(mol*s)'),
                n = -5.28,
                Ea = (17165, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.18e+24, 'cm^3/(mol*s)'),
                n = -3.99,
                Ea = (16747, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1475,
    label = "IC4H8OH-TI + O2 <=> CH3 + C3KET21",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.91e+40, 'cm^3/(mol*s)'),
                n = -9.23,
                Ea = (10830, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.66e+43, 'cm^3/(mol*s)'),
                n = -10.2,
                Ea = (13698, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.34e+44, 'cm^3/(mol*s)'),
                n = -10.13,
                Ea = (15661, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.57e+41, 'cm^3/(mol*s)'),
                n = -9.18,
                Ea = (17047, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.82e+36, 'cm^3/(mol*s)'),
                n = -7.46,
                Ea = (18330, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.82e+29, 'cm^3/(mol*s)'),
                n = -5.44,
                Ea = (18205, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.74e+24, 'cm^3/(mol*s)'),
                n = -3.65,
                Ea = (17600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.16e+19, 'cm^3/(mol*s)'),
                n = -2.12,
                Ea = (16925, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1476,
    label = "IC4H8OH-TI + O2 <=> IQC4H7OHT",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.03e+115, 'cm^3/(mol*s)'),
                n = -35.13,
                Ea = (25407, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+129, 'cm^3/(mol*s)'),
                n = -38.89,
                Ea = (32891, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.15e+135, 'cm^3/(mol*s)'),
                n = -40.38,
                Ea = (38573, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.27e+129, 'cm^3/(mol*s)'),
                n = -38.13,
                Ea = (39933, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.5e+112, 'cm^3/(mol*s)'),
                n = -32.49,
                Ea = (37045, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.72e+97, 'cm^3/(mol*s)'),
                n = -27.79,
                Ea = (33612, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.17e+86, 'cm^3/(mol*s)'),
                n = -24.26,
                Ea = (30799, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.7e+77, 'cm^3/(mol*s)'),
                n = -21.41,
                Ea = (28440, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1477,
    label = "IC4H8OH-TI + O2 => IC3H5OH + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.1e+24, 'cm^3/(mol*s)'),
                n = -4.31,
                Ea = (13009, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.91e+33, 'cm^3/(mol*s)'),
                n = -6.97,
                Ea = (17935, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.74e+41, 'cm^3/(mol*s)'),
                n = -9.03,
                Ea = (23613, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.26e+36, 'cm^3/(mol*s)'),
                n = -7.32,
                Ea = (25633, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.15e+17, 'cm^3/(mol*s)'),
                n = -1.4,
                Ea = (22782, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(9.35, 'cm^3/(mol*s)'), n=3.71, Ea=(19114, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (5.59e-12, 'cm^3/(mol*s)'),
                n = 7.46,
                Ea = (16156, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.27e-21, 'cm^3/(mol*s)'),
                n = 10.41,
                Ea = (13733, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1478,
    label = "IC4H8OH-TI + O2 <=> CCY(CCOC)OH + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.06e+33, 'cm^3/(mol*s)'),
                n = -7.24,
                Ea = (11476, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.56e+42, 'cm^3/(mol*s)'),
                n = -9.92,
                Ea = (17197, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.24e+46, 'cm^3/(mol*s)'),
                n = -10.95,
                Ea = (22090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.48e+38, 'cm^3/(mol*s)'),
                n = -8.22,
                Ea = (23019, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.01e+18, 'cm^3/(mol*s)'),
                n = -1.77,
                Ea = (19496, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(11.6, 'cm^3/(mol*s)'), n=3.44, Ea=(15637, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.85e-12, 'cm^3/(mol*s)'),
                n = 7.23,
                Ea = (12599, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.64e-22, 'cm^3/(mol*s)'),
                n = 10.21,
                Ea = (10126, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1479,
    label = "IQJC4H8OH <=> IC3H6OHCHO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.58e+71, 's^-1'), n=-20.62, Ea=(52656, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.67e+71, 's^-1'), n=-20.08, Ea=(54935, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.39e+67, 's^-1'), n=-18.18, Ea=(55330, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.26e+58, 's^-1'), n=-15.09, Ea=(54016, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.57e+46, 's^-1'), n=-11.01, Ea=(51172, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.31e+38, 's^-1'), n=-8.38, Ea=(49054, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.12e+33, 's^-1'), n=-6.66, Ea=(47587, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.72e+29, 's^-1'), n=-5.41, Ea=(46486, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1480,
    label = "IQJC4H8OH <=> IQC4H8OT",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.04e+45, 's^-1'), n=-11.2, Ea=(31755, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.9e+40, 's^-1'), n=-9.62, Ea=(30945, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.85e+35, 's^-1'), n=-8.01, Ea=(29850, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.62e+30, 's^-1'), n=-6.28, Ea=(28498, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.37e+24, 's^-1'), n=-4.37, Ea=(26873, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.75e+20, 's^-1'), n=-3.23, Ea=(25861, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.61e+18, 's^-1'), n=-2.52, Ea=(25208, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.44e+17, 's^-1'), n=-2.01, Ea=(24740, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1481,
    label = "IQJC4H8OH <=> IQC4H7OHT",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.36e+50, 's^-1'), n=-12.93, Ea=(36743, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.36e+45, 's^-1'), n=-11.27, Ea=(36143, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.13e+40, 's^-1'), n=-9.41, Ea=(34990, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.93e+33, 's^-1'), n=-7.33, Ea=(33438, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.24e+26, 's^-1'), n=-5, Ea=(31502, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.97e+22, 's^-1'), n=-3.61, Ea=(30275, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.43e+19, 's^-1'), n=-2.72, Ea=(29477, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.69e+17, 's^-1'), n=-2.09, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1482,
    label = "IQC4H7OHT => IC3H5OH + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.25e+16, 's^-1'), n=-3.66, Ea=(19364, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.98e+33, 's^-1'), n=-8.01, Ea=(27106, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.46e+38, 's^-1'), n=-8.83, Ea=(31412, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.07e+28, 's^-1'), n=-5.46, Ea=(29633, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.01e+13, 's^-1'), n=-0.43, Ea=(25278, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.43e+13, 's^-1'), n=-0.38, Ea=(25238, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.38e+13, 's^-1'), n=-0.38, Ea=(25234, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.37e+13, 's^-1'), n=-0.37, Ea=(25233, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1483,
    label = "IQC4H7OHT <=> CCY(CCOC)OH + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.12e+25, 's^-1'), n=-5.59, Ea=(19349, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.2e+32, 's^-1'), n=-7.6, Ea=(23093, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.22e+34, 's^-1'), n=-7.65, Ea=(25130, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.4e+27, 's^-1'), n=-5.28, Ea=(23663, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.24e+17, 's^-1'), n=-2.04, Ea=(20810, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.82e+17, 's^-1'), n=-2.01, Ea=(20786, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.78e+17, 's^-1'), n=-2.01, Ea=(20783, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.77e+17, 's^-1'), n=-2.01, Ea=(20782, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1484,
    label = "IQC4H7OHT <=> IC4H7OOH + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 40, 100, 200], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.07e+13, 's^-1'), n=-4.21, Ea=(22478, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.74e+39, 's^-1'), n=-10.89, Ea=(33616, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.18e+49, 's^-1'), n=-12.65, Ea=(40359, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.32e+37, 's^-1'), n=-8.42, Ea=(38539, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.34e+16, 's^-1'), n=-1.56, Ea=(32712, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.44e+16, 's^-1'), n=-1.49, Ea=(32656, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.38e+16, 's^-1'), n=-1.48, Ea=(32651, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.37e+16, 's^-1'), n=-1.48, Ea=(32649, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1485,
    label = "IQC4H8OT => CH3COCH3 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.64e+09, 's^-1'), n=1.3, Ea=(23700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1486,
    label = "IQC4H8OT <=> CH3 + C3KET21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.95e+10, 's^-1'), n=0.83, Ea=(27900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1487,
    label = "IQC4H7OHT <=> CH2COHCH2OOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.95e+10, 's^-1'), n=0.83, Ea=(27900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1488,
    label = "TQC4H7OHIO2 <=> TQC4H7OHIQ-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.56e+12, 's^-1'), n=-0.13, Ea=(34360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1489,
    label = "TQC4H7OHIQ-I => HO2CHO + CH3COCH3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(581900, 's^-1'), n=2.4, Ea=(22790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1490,
    label = "TQC4H7OHIQ-I <=> IC4KETIT + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.829e+10, 's^-1'), n=0.79, Ea=(15100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1491,
    label = "IC4KETIT => CH3COCH3 + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.5e+15, 's^-1'), n=0, Ea=(42540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1492,
    label = "IC4KETIT + OH <=> TC3H6O2HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (61329.9, 'cm^3/(mol*s)'),
        n = 2.65419,
        Ea = (-4586.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1493,
    label = "IC4KETIT + HO2 <=> TC3H6O2HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00011773, 'cm^3/(mol*s)'),
        n = 4.91966,
        Ea = (3684.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1494,
    label = "TC3H6O2HCO => CH3COCH3 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.278e+20, 's^-1'), n=-1.89, Ea=(34460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1495,
    label = "TQC4H7OHIO2 <=> TQC4H7OHIQ-P",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.69e+08, 's^-1'), n=0.78, Ea=(21850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1496,
    label = "TQC4H7OHIQ-P <=> IC3H5COHQ + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.83e+10, 's^-1'), n=0.79, Ea=(15100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1497,
    label = "TQC4H7OHIQ-P <=> CH2CQCOHQ + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.38e+11, 's^-1'), n=0.07, Ea=(24800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1498,
    label = "TQC4H7OHIQ-P => IC3H5Q + HOCHO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5.38e+11, 's^-1'), n=0.07, Ea=(24800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1499,
    label = "TQC4H7OHIQ-P <=> COHQCYC(COC) + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.28e+08, 's^-1'), n=1.29, Ea=(9890, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1500,
    label = "TQC4H7OHIQ-P <=> QCYC(CCOC)OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+15, 's^-1'), n=-1.08, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1501,
    label = "IC3H5COHQ => HOCHO + C3H5-T + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.59e+20, 's^-1'), n=-1.5, Ea=(42879.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1504,
    label = "IC3H5Q => CH2CO + CH3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.59e+20, 's^-1'), n=-1.5, Ea=(42879.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1507,
    label = "TQC4H7OHIO2 <=> TQC4H7OHTO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.956e+09, 's^-1'), n=0.04, Ea=(16350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1508,
    label = "TQC4H7OHTO2 <=> HOCOCQ(CH3)2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+08, 's^-1'), n=1.7, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1510,
    label = "IQC4H7OHTO2 <=> IQC4H7OHTQ-P",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.063e+07, 's^-1'), n=1, Ea=(21070, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1511,
    label = "IQC4H7OHTQ-P => OH + CH2O + CH2COHCH2OOH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.2e+10, 's^-1'), n=0.35, Ea=(15700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1513,
    label = "IQC4H7OHTQ-P <=> OH + IC4H6Q2-II",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.53e+40, 's^-1'), n=-9.91, Ea=(32631.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.54e+37, 's^-1'), n=-8.72, Ea=(32909.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.12e+31, 's^-1'), n=-6.53, Ea=(31806.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.98e+21, 's^-1'), n=-3.34, Ea=(29137.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.95e+10, 's^-1'), n=0.154, Ea=(25612, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1515,
    label = "IQC4H7OHTO2 <=> IQC4H8OTQ-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.13e+07, 's^-1'), n=1, Ea=(21070, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1516,
    label = "IQC4H8OTQ-I => OH + CH2O + C3KET21",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.2e+10, 's^-1'), n=0.35, Ea=(15700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1517,
    label = "IQC4H8OTQ-I <=> CH3 + CO(CH2OOH)2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.74e+13, 's^-1'), n=0.24, Ea=(29830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1519,
    label = "IQC4H7OHTO2 <=> CHOC(CH3)OHCH2Q + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+10, 's^-1'), n=0.35, Ea=(15700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1522,
    label = "TQC4H7OHI + O2 <=> TQC4H7OHIO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.49e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.49, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1523,
    label = "IQC4H7OHT + O2 <=> IQC4H7OHTO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1524,
    label = "C2CY(COC)OH + OH => IC3H6CO + OH + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2260, 'cm^3/(mol*s)'), n=2.73, Ea=(-4688, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1525,
    label = "C2CY(COC)OH + HO2 => IC3H6CO + OH + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.46, Ea=(9732.33, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1526,
    label = "CCY(CCO)COH + OH => IC3H5CHO + OH + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(566, 'cm^3/(mol*s)'), n=2.93, Ea=(-4039.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1527,
    label = "CCY(CCO)COH + HO2 => IC3H5CHO + OH + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (0.181, 'cm^3/(mol*s)'),
        n = 3.98,
        Ea = (9056.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1528,
    label = "CCY(CCO)COH + OH => PC3H4OH-2 + CH2O + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1260, 'cm^3/(mol*s)'),
        n = 2.97,
        Ea = (-2660.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1529,
    label = "CCY(CCO)COH + HO2 => PC3H4OH-2 + CH2O + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (8267.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1530,
    label = "CCY(CCOC)OH + OH => CH2O + SC3H4OH + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(566, 'cm^3/(mol*s)'), n=2.93, Ea=(-4039.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1531,
    label = "CCY(CCOC)OH + HO2 => CH2O + SC3H4OH + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (0.181, 'cm^3/(mol*s)'),
        n = 3.98,
        Ea = (9056.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1532,
    label = "IC4H7 + OH <=> IC4H7OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1533,
    label = "IC4H7O + H <=> IC4H7OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1534,
    label = "IC4H6OH + H <=> IC4H7OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1535,
    label = "CH2CCH2OH + CH3 <=> IC4H7OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1536,
    label = "IC4H7OH + O2 <=> IC4H6OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1537,
    label = "IC4H7OH + OH <=> IC4H6OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1260, 'cm^3/(mol*s)'),
        n = 2.97,
        Ea = (-2660.59, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1538,
    label = "IC4H7OH + HO2 <=> IC4H6OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (8267.91, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1539,
    label = "IC4H6OH + H2 <=> IC4H7OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(21600, 'cm^3/(mol*s)'), n=2.38, Ea=(18990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1540,
    label = "IC4H6OH + CH2O <=> IC4H7OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (18190, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1541,
    label = "IC4H6OH + IC4H8 <=> IC4H7OH + IC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(470, 'cm^3/(mol*s)'), n=3.3, Ea=(19840, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1542,
    label = "IC4H7O + H2 <=> IC4H7OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.05e+06, 'cm^3/(mol*s)'), n=2, Ea=(17830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1543,
    label = "IC4H7OH + HCO <=> IC4H7O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(18160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1544,
    label = "C3H4-A + CH2OH <=> IC4H6OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1545,
    label = "IC4H7O <=> IC4H6OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.391e+11, 's^-1'), n=0, Ea=(15600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1546,
    label = "IC4H6OH + HO2 => CH2CCH2OH + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.446e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1547,
    label = "IC4H7OH + H <=> IC4H8OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1548,
    label = "IC4H7O + O2 <=> IC3H5CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(1649, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1549,
    label = "IC4H7O + HO2 <=> IC3H5CHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1550,
    label = "IC4H7O + CH3 <=> IC3H5CHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1551,
    label = "IC4H7O + O <=> IC3H5CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1552,
    label = "IC4H7O + OH <=> IC3H5CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1553,
    label = "IC4H7O + H <=> IC3H5CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1554,
    label = "IC3H6OHCHO + OH => TC3H6OH + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (61329.9, 'cm^3/(mol*s)'),
        n = 2.65,
        Ea = (-4586.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1555,
    label = "IC3H6OHCHO + H => TC3H6OH + CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(866000, 'cm^3/(mol*s)'), n=2.3, Ea=(1426, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1556,
    label = "IC3H6OHCHO + HO2 => TC3H6OH + CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(0.000101, 'cm^3/(mol*s)'), n=5, Ea=(3429, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1557,
    label = "IC3H6OHCHO + CH3 => TC3H6OH + CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.94, 'cm^3/(mol*s)'), n=3.6, Ea=(4223, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1558,
    label = "TC3H6OH <=> CH3COCH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.981e+11, 's^-1'), n=0.271, Ea=(32990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1559,
    label = "TC3H6OH <=> IC3H5OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.211e+10, 's^-1'), n=1.005, Ea=(40900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1560,
    label = "TC3H6OH + O2 <=> CH3COCH3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1561,
    label = "C3H5-A + CH3 <=> C4H8-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1e+14, 'cm^3/(mol*s)'),
            n = -0.32,
            Ea = (-262.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.91e+60, 'cm^6/(mol^2*s)'),
            n = -12.81,
            Ea = (6250, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.104,
        T3 = (1606, 'K'),
        T1 = (60000, 'K'),
        T2 = (6118.4, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 1562,
    label = "C2H5 + C2H3 <=> C4H8-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.55e+56, 'cm^6/(mol^2*s)'),
            n = -11.79,
            Ea = (8984.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.198,
        T3 = (2277.9, 'K'),
        T1 = (60000, 'K'),
        T2 = (5723.2, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 1563,
    label = "C4H71-4 + H <=> C4H8-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 1564,
    label = "C4H71-3 + H <=> C4H8-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1565,
    label = "C3H5-S + CH3 <=> C4H8-2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.54e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9769.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000, 'K'),
        T2 = (10139.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, 'C=C': 3, 'C#C': 3, '[Ar]': 0.7},
    ),
)

entry(
    index = 1566,
    label = "C4H8-2 <=> C3H5-A + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+65, 's^-1'), n=-15.6, Ea=(97300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1567,
    label = "C4H8-2 <=> H + C4H71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+84, 's^-1'), n=-20.03, Ea=(132787, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1568,
    label = "C4H8-1 + OH <=> C4H71-3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (776900, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-437.18, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1569,
    label = "C4H8-1 + OH <=> C4H71-4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.6e+06, 'cm^3/(mol*s)'),
        n = 2.03,
        Ea = (2623.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1570,
    label = "C4H8-1 + OH <=> C4H71-2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+06, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (2847.66, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1571,
    label = "C4H8-1 + OH <=> C4H71-1 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.93e+06, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (4962.04, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1572,
    label = "C4H8-2 + OH <=> C4H71-3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.46e+06, 'cm^3/(mol*s)'),
        n = 2.072,
        Ea = (1050.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1573,
    label = "C4H8-2 + OH <=> C4H72-2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+06, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (2845.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1574,
    label = "C4H8-1 + HO2 <=> C4H71-3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.782, 'cm^3/(mol*s)'), n=3.97, Ea=(11702, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1575,
    label = "C4H8-2 + HO2 <=> C4H71-3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.69, 'cm^3/(mol*s)'), n=4, Ea=(12103, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1576,
    label = "C4H8-1 + HO2 <=> C4H71-4 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1577,
    label = "C4H8-1 + HO2 <=> C4H71-1 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (957, 'cm^3/(mol*s)'),
        n = 3.059,
        Ea = (20798.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1578,
    label = "C4H8-1 + HO2 <=> C4H71-2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15600, 'cm^3/(mol*s)'),
        n = 2.82,
        Ea = (24427.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1579,
    label = "C4H8-2 + HO2 <=> C4H72-2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31200, 'cm^3/(mol*s)'),
        n = 2.82,
        Ea = (24427.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1580,
    label = "C4H8-1 + H <=> C4H71-4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(38400, 'cm^3/(mol*s)'), n=2.87, Ea=(6611, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1581,
    label = "C4H8-1 + H <=> C4H71-3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2420, 'cm^3/(mol*s)'), n=3.05, Ea=(1995, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1582,
    label = "C4H8-1 + H <=> C4H71-2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23700, 'cm^3/(mol*s)'), n=2.85, Ea=(8917, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1583,
    label = "C4H8-1 + H <=> C4H71-1 + H2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2.83, Ea=(12050, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(22300, 'cm^3/(mol*s)'), n=2.85, Ea=(11710, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1584,
    label = "C4H8-2 + H <=> C4H71-3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(562, 'cm^3/(mol*s)'), n=3.5, Ea=(1627, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1585,
    label = "C4H8-2 + H <=> C4H72-2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(84700, 'cm^3/(mol*s)'), n=2.76, Ea=(9304, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1586,
    label = "C4H8-1 + O <=> C4H71-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1587,
    label = "C4H8-2 + O <=> C4H71-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.19e+11, 'cm^3/(mol*s)'),
        n = 0.81,
        Ea = (7550, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1588,
    label = "C4H8-1 + O <=> C4H71-1 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8959.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1589,
    label = "C4H8-1 + O <=> C4H71-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7632, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1590,
    label = "C4H8-2 + O <=> C4H72-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7632, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1591,
    label = "C4H8-1 + O <=> C4H71-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+14, 'cm^3/(mol*s)'), n=0, Ea=(7850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1592,
    label = "C4H8-1 + O2 <=> C4H71-3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1593,
    label = "C4H8-2 + O2 <=> C4H71-3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(39390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1594,
    label = "C4H8-1 + O2 <=> C4H71-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(62270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1595,
    label = "C4H8-1 + O2 <=> C4H71-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(58770, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1596,
    label = "C4H8-2 + O2 <=> C4H72-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(58770, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1597,
    label = "C4H8-1 + O2 <=> C4H71-4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1598,
    label = "C4H8-1 + CH3 <=> C4H71-3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1599,
    label = "C4H8-1 + CH3 <=> C4H71-4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.452, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1600,
    label = "C4H8-2 + CH3 <=> C4H71-3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.14, 'cm^3/(mol*s)'), n=3.57, Ea=(7642, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1601,
    label = "C4H8-1 + CH3 <=> C4H71-1 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.348, 'cm^3/(mol*s)'), n=3.5, Ea=(12850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1602,
    label = "C4H8-1 + CH3 <=> C4H71-2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1603,
    label = "C4H8-2 + CH3 <=> C4H72-2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.68, 'cm^3/(mol*s)'), n=3.5, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1604,
    label = "C4H8-1 + CH3O2 <=> C4H71-3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=0.7, Ea=(5884, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1605,
    label = "C4H8-1 + CH3O2 <=> C4H71-4 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2380, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1606,
    label = "C4H8-1 + CH3O <=> C4H71-3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1607,
    label = "C4H8-1 + CH3O <=> C4H71-4 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1608,
    label = "C4H8-2 + CH3O <=> C4H71-3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18, 'cm^3/(mol*s)'), n=2.95, Ea=(11990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1609,
    label = "C4H8-1 + CH3CO3 <=> C4H71-3 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1610,
    label = "C4H8-1 + C3H5-A <=> C4H71-3 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.9e+10, 'cm^3/(mol*s)'), n=0, Ea=(12400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1611,
    label = "C4H8-1 + C2H5O2 <=> C4H71-3 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1612,
    label = "C4H8-1 + NC3H7O2 <=> C4H71-3 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1613,
    label = "C4H8-1 + IC3H7O2 <=> C4H71-3 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1614,
    label = "C4H8-1 + PC4H9O2 <=> C4H71-3 + PC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1615,
    label = "C4H8-1 + SC4H9O2 <=> C4H71-3 + SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1616,
    label = "C4H8-2 + NC3H7O2 <=> C4H71-3 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1617,
    label = "C4H8-2 + IC3H7O2 <=> C4H71-3 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1618,
    label = "C4H8-2 + PC4H9O2 <=> C4H71-3 + PC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1619,
    label = "C4H8-2 + SC4H9O2 <=> C4H71-3 + SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1620,
    label = "C4H71-3 + C2H5 <=> C4H8-1 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+12, 'cm^3/(mol*s)'), n=0, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1621,
    label = "C4H71-3 + CH3O <=> C4H8-1 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1622,
    label = "IC4H9O2 + C4H8-1 <=> IC4H9O2H + C4H71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1623,
    label = "TC4H9O2 + C4H8-1 <=> TC4H9O2H + C4H71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1624,
    label = "IC4H9O2 + C4H8-2 <=> IC4H9O2H + C4H71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1625,
    label = "TC4H9O2 + C4H8-2 <=> TC4H9O2H + C4H71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1626,
    label = "C4H71-1 <=> C4H6-1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.95e+08, 's^-1'), n=1.14, Ea=(35636.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1627,
    label = "C4H71-1 <=> C2H5 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.85e+12, 's^-1'), n=0.68, Ea=(33178.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1628,
    label = "C4H71-2 <=> C4H6-1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.79e+08, 's^-1'), n=1.2, Ea=(38080.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1629,
    label = "C4H71-2 <=> C4H612 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+08, 's^-1'), n=1.56, Ea=(37683.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1630,
    label = "C4H71-2 <=> C3H4-A + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+10, 's^-1'), n=1.19, Ea=(32916, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1631,
    label = "C4H71-3 <=> C4H612 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.95e+11, 's^-1'), n=0.93, Ea=(61611.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1632,
    label = "C4H71-3 <=> C4H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.53e+07, 's^-1'), n=1.95, Ea=(47490.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1633,
    label = "C4H71-4 <=> C2H4 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.84e+10, 's^-1'), n=0.99, Ea=(38998.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1634,
    label = "C4H71-4 <=> C4H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(132000, 's^-1'), n=2.28, Ea=(33245.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1635,
    label = "C4H72-2 <=> C4H6-2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.87e+09, 's^-1'), n=1.16, Ea=(36173, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1636,
    label = "C4H72-2 <=> C4H612 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.54e+07, 's^-1'), n=1.81, Ea=(38992.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1637,
    label = "C4H72-2 <=> C3H4-P + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+11, 's^-1'), n=0.93, Ea=(34754.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1638,
    label = "C4H71-3 <=> C4H71-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e-12, 's^-1'), n=7.19, Ea=(36200.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1639,
    label = "C4H71-3 <=> C4H72-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.76e-23, 's^-1'), n=10.21, Ea=(41574.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1640,
    label = "C4H71-3 + HO2 <=> C4H71-3OOH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(20.5, 'cm^3/(mol*s)'), n=1.24, Ea=(-22589, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (3.69e+06, 'cm^3/(mol*s)'),
                n = 0.08,
                Ea = (-18331, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.02e+13, 'cm^3/(mol*s)'),
                n = -1.45,
                Ea = (-11709, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.49e+15, 'cm^3/(mol*s)'),
                n = -1.87,
                Ea = (-9604, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.85e+17, 'cm^3/(mol*s)'),
                n = -2.31,
                Ea = (-6991, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.88e+18, 'cm^3/(mol*s)'),
                n = -2.55,
                Ea = (-5260, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.45e+19, 'cm^3/(mol*s)'),
                n = -2.71,
                Ea = (-3140, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.33e+19, 'cm^3/(mol*s)'),
                n = -2.7,
                Ea = (-2438, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1641,
    label = "C4H71-3 + HO2 <=> C4H71-O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.9e+20, 'cm^3/(mol*s)'),
                n = -2.68,
                Ea = (229, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.5e+22, 'cm^3/(mol*s)'),
                n = -3.18,
                Ea = (1760, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.61e+27, 'cm^3/(mol*s)'),
                n = -4.63,
                Ea = (6415, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.92e+30, 'cm^3/(mol*s)'),
                n = -5.28,
                Ea = (8578, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.46e+33, 'cm^3/(mol*s)'),
                n = -6.22,
                Ea = (11879, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.98e+36, 'cm^3/(mol*s)'),
                n = -6.97,
                Ea = (14600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.58e+40, 'cm^3/(mol*s)'),
                n = -8.14,
                Ea = (19040, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.44e+42, 'cm^3/(mol*s)'),
                n = -8.67,
                Ea = (21071, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1642,
    label = "C4H71-3 + HO2 <=> C2H3COCH3 + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.16e+14, 'cm^3/(mol*s)'),
                n = -1.74,
                Ea = (1910, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.62e+16, 'cm^3/(mol*s)'),
                n = -2.16,
                Ea = (3167, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.73e+20, 'cm^3/(mol*s)'),
                n = -3.47,
                Ea = (7339, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.7e+23, 'cm^3/(mol*s)'),
                n = -4.09,
                Ea = (9378, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.33e+26, 'cm^3/(mol*s)'),
                n = -5.02,
                Ea = (12574, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.59e+29, 'cm^3/(mol*s)'),
                n = -5.78,
                Ea = (15275, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.85e+33, 'cm^3/(mol*s)'),
                n = -7.01,
                Ea = (19801, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.84e+35, 'cm^3/(mol*s)'),
                n = -7.58,
                Ea = (21918, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1643,
    label = "C4H71-3OOH <=> C4H71-O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.41e+35, 's^-1'), n=-7.37, Ea=(39745, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.64e+37, 's^-1'), n=-7.6, Ea=(44224, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.09e+37, 's^-1'), n=-7.24, Ea=(47692, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.92e+37, 's^-1'), n=-6.97, Ea=(48350, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.2e+36, 's^-1'), n=-6.51, Ea=(48849, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.17e+34, 's^-1'), n=-6.08, Ea=(48933, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.69e+32, 's^-1'), n=-5.32, Ea=(48614, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.04e+31, 's^-1'), n=-4.97, Ea=(48341, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1644,
    label = "C4H71-3OOH <=> C2H3COCH3 + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.58e+23, 's^-1'), n=-4.64, Ea=(38121, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.85e+27, 's^-1'), n=-5.36, Ea=(43407, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.63e+29, 's^-1'), n=-5.53, Ea=(48042, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.83e+29, 's^-1'), n=-5.43, Ea=(49101, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.04e+29, 's^-1'), n=-5.18, Ea=(50137, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.12e+28, 's^-1'), n=-4.89, Ea=(50610, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.39e+26, 's^-1'), n=-4.33, Ea=(50818, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.76e+25, 's^-1'), n=-4.04, Ea=(50737, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1645,
    label = "C4H71-O <=> C2H3 + CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.52e+25, 's^-1'), n=-3.61, Ea=(27863.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1646,
    label = "C4H71-O <=> AC3H5OCH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.35e+18, 's^-1'), n=-1.73, Ea=(17386.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1647,
    label = "C4H71-O <=> CH2CH2COCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+21, 's^-1'), n=-2.74, Ea=(20337.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1648,
    label = "C4H71-O <=> C2H3COCH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.57e+20, 's^-1'), n=-2.06, Ea=(22040.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1649,
    label = "C4H71-O <=> C2H4 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.75e+08, 's^-1'), n=1.14, Ea=(20922.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1650,
    label = "AC3H5OCH2 <=> C3H5-A + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.81e+14, 's^-1'), n=-0.326, Ea=(31553.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1651,
    label = "AC3H5OCH2 <=> CH2CH2COCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.51e+20, 's^-1'), n=-2.63, Ea=(29288.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1652,
    label = "AC3H5OCH2 <=> C2H3COCH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+18, 's^-1'), n=-1.62, Ea=(30129.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1653,
    label = "AC3H5OCH2 <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.73e+14, 's^-1'), n=-0.726, Ea=(32008.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1654,
    label = "CH2CH2COCH3 <=> C2H3 + CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.93e+19, 's^-1'), n=-1.94, Ea=(48440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1655,
    label = "CH2CH2COCH3 <=> C2H3COCH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 's^-1'), n=0.214, Ea=(34570.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1656,
    label = "CH2CH2COCH3 <=> C2H4 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.59e+13, 's^-1'), n=0.063, Ea=(24086.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1657,
    label = "C2H3 + CH3CHO <=> C2H4 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(16.5, 'cm^3/(mol*s)'), n=3.17, Ea=(9399.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1658,
    label = "C4H71-3 + HO2 <=> C4H72-1OOH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1e+07, 'cm^3/(mol*s)'),
                n = -0.33,
                Ea = (-17896, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.15e+11, 'cm^3/(mol*s)'),
                n = -1.16,
                Ea = (-14831, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.95e+16, 'cm^3/(mol*s)'),
                n = -2.33,
                Ea = (-9451, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.68e+17, 'cm^3/(mol*s)'),
                n = -2.62,
                Ea = (-7705, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.21e+19, 'cm^3/(mol*s)'),
                n = -2.89,
                Ea = (-5556, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.14e+20, 'cm^3/(mol*s)'),
                n = -2.99,
                Ea = (-4159, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.8e+20, 'cm^3/(mol*s)'),
                n = -2.96,
                Ea = (-2503, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.4e+20, 'cm^3/(mol*s)'),
                n = -2.88,
                Ea = (-1971, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1659,
    label = "C4H71-3 + HO2 <=> C4H7O2-1 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.81e+20, 'cm^3/(mol*s)'),
                n = -2.68,
                Ea = (217, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.25e+22, 'cm^3/(mol*s)'),
                n = -3.1,
                Ea = (1516, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.75e+27, 'cm^3/(mol*s)'),
                n = -4.49,
                Ea = (6067, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.27e+29, 'cm^3/(mol*s)'),
                n = -5.14,
                Ea = (8273, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.96e+33, 'cm^3/(mol*s)'),
                n = -6.09,
                Ea = (11661, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.16e+36, 'cm^3/(mol*s)'),
                n = -6.85,
                Ea = (14456, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.51e+40, 'cm^3/(mol*s)'),
                n = -8.04,
                Ea = (19009, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.18e+42, 'cm^3/(mol*s)'),
                n = -8.58,
                Ea = (21090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1660,
    label = "C4H71-3 + HO2 <=> SC3H5CHO + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.62e+14, 'cm^3/(mol*s)'),
                n = -1.6,
                Ea = (1519, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.19e+15, 'cm^3/(mol*s)'),
                n = -1.96,
                Ea = (2620, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.69e+20, 'cm^3/(mol*s)'),
                n = -3.26,
                Ea = (6800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.39e+22, 'cm^3/(mol*s)'),
                n = -3.89,
                Ea = (8918, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.09e+26, 'cm^3/(mol*s)'),
                n = -4.85,
                Ea = (12249, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.81e+28, 'cm^3/(mol*s)'),
                n = -5.63,
                Ea = (15058, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.14e+33, 'cm^3/(mol*s)'),
                n = -6.89,
                Ea = (19743, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.07e+35, 'cm^3/(mol*s)'),
                n = -7.48,
                Ea = (21927, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1661,
    label = "C4H72-1OOH <=> C4H7O2-1 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.07e+35, 's^-1'), n=-7.39, Ea=(39733, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.69e+37, 's^-1'), n=-7.63, Ea=(43994, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.76e+37, 's^-1'), n=-7.14, Ea=(47024, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.32e+36, 's^-1'), n=-6.81, Ea=(47507, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.21e+35, 's^-1'), n=-6.24, Ea=(47760, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.92e+33, 's^-1'), n=-5.74, Ea=(47658, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.62e+30, 's^-1'), n=-4.88, Ea=(47084, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.29e+29, 's^-1'), n=-4.5, Ea=(46721, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1662,
    label = "C4H72-1OOH <=> SC3H5CHO + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.15e+24, 's^-1'), n=-4.78, Ea=(38584, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.65e+27, 's^-1'), n=-5.51, Ea=(43561, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.33e+29, 's^-1'), n=-5.53, Ea=(47626, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.29e+29, 's^-1'), n=-5.35, Ea=(48469, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.81e+28, 's^-1'), n=-4.98, Ea=(49208, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.76e+27, 's^-1'), n=-4.61, Ea=(49458, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.59e+25, 's^-1'), n=-3.91, Ea=(49357, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.58e+24, 's^-1'), n=-3.58, Ea=(49164, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1663,
    label = "C4H7O2-1 <=> C3H5-S + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.52e+25, 's^-1'), n=-3.61, Ea=(27863.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1664,
    label = "C4H7O2-1 <=> SC3H5OCH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.35e+18, 's^-1'), n=-1.73, Ea=(17386.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1665,
    label = "C4H7O2-1 <=> C3H6CHO-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+21, 's^-1'), n=-2.74, Ea=(20337.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1666,
    label = "C4H7O2-1 <=> SC3H5CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.57e+20, 's^-1'), n=-2.06, Ea=(22040.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1667,
    label = "C4H7O2-1 <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.75e+08, 's^-1'), n=1.14, Ea=(20922.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1668,
    label = "SC3H5OCH2-1 <=> C3H5-S + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.81e+14, 's^-1'), n=-0.326, Ea=(31553.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1669,
    label = "SC3H5OCH2-1 <=> C3H6CHO-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.51e+20, 's^-1'), n=-2.63, Ea=(29288.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1670,
    label = "SC3H5OCH2-1 <=> SC3H5CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+18, 's^-1'), n=-1.62, Ea=(30129.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1671,
    label = "SC3H5OCH2-1 <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.73e+14, 's^-1'), n=-0.726, Ea=(32008.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1672,
    label = "C3H6CHO-2 <=> C3H5-S + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.93e+19, 's^-1'), n=-1.94, Ea=(48440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1673,
    label = "C3H6CHO-2 <=> SC3H5CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 's^-1'), n=0.214, Ea=(34570.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1674,
    label = "C3H6CHO-2 <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.59e+13, 's^-1'), n=0.063, Ea=(24086.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1675,
    label = "C3H5-S + CH2O <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(16.5, 'cm^3/(mol*s)'), n=3.17, Ea=(9399.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1676,
    label = "C4H71-3 + CH3O2 <=> C4H71-3OOCH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(10.3, 'cm^3/(mol*s)'), n=1.24, Ea=(-22589, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.85e+06, 'cm^3/(mol*s)'),
                n = 0.08,
                Ea = (-18331, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.01e+13, 'cm^3/(mol*s)'),
                n = -1.45,
                Ea = (-11709, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.45e+14, 'cm^3/(mol*s)'),
                n = -1.87,
                Ea = (-9604, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.25e+16, 'cm^3/(mol*s)'),
                n = -2.31,
                Ea = (-6991, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.44e+18, 'cm^3/(mol*s)'),
                n = -2.55,
                Ea = (-5260, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.73e+19, 'cm^3/(mol*s)'),
                n = -2.71,
                Ea = (-3140, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.67e+19, 'cm^3/(mol*s)'),
                n = -2.7,
                Ea = (-2438, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1677,
    label = "C4H71-3 + CH3O2 <=> C4H71-O + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.45e+20, 'cm^3/(mol*s)'),
                n = -2.68,
                Ea = (229, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.25e+22, 'cm^3/(mol*s)'),
                n = -3.18,
                Ea = (1760, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.31e+27, 'cm^3/(mol*s)'),
                n = -4.63,
                Ea = (6415, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.6e+29, 'cm^3/(mol*s)'),
                n = -5.28,
                Ea = (8578, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.73e+33, 'cm^3/(mol*s)'),
                n = -6.22,
                Ea = (11879, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.49e+36, 'cm^3/(mol*s)'),
                n = -6.97,
                Ea = (14600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.79e+40, 'cm^3/(mol*s)'),
                n = -8.14,
                Ea = (19040, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.22e+42, 'cm^3/(mol*s)'),
                n = -8.67,
                Ea = (21071, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1678,
    label = "C4H71-3OOCH3 <=> C4H71-O + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.21e+35, 's^-1'), n=-7.37, Ea=(39745, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.32e+37, 's^-1'), n=-7.6, Ea=(44224, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.55e+37, 's^-1'), n=-7.24, Ea=(47692, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.6e+36, 's^-1'), n=-6.97, Ea=(48350, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6e+35, 's^-1'), n=-6.51, Ea=(48849, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.59e+34, 's^-1'), n=-6.08, Ea=(48933, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.85e+32, 's^-1'), n=-5.32, Ea=(48614, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.52e+31, 's^-1'), n=-4.97, Ea=(48341, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1679,
    label = "C4H71-3 + CH3O2 <=> C4H72-1OOCH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5e+06, 'cm^3/(mol*s)'),
                n = -0.33,
                Ea = (-17896, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.75e+10, 'cm^3/(mol*s)'),
                n = -1.16,
                Ea = (-14831, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.48e+16, 'cm^3/(mol*s)'),
                n = -2.33,
                Ea = (-9451, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.84e+17, 'cm^3/(mol*s)'),
                n = -2.62,
                Ea = (-7705, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.11e+19, 'cm^3/(mol*s)'),
                n = -2.89,
                Ea = (-5556, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.7e+19, 'cm^3/(mol*s)'),
                n = -2.99,
                Ea = (-4159, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.4e+20, 'cm^3/(mol*s)'),
                n = -2.96,
                Ea = (-2503, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.2e+20, 'cm^3/(mol*s)'),
                n = -2.88,
                Ea = (-1971, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1680,
    label = "C4H71-3 + CH3O2 <=> C4H7O2-1 + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.41e+20, 'cm^3/(mol*s)'),
                n = -2.68,
                Ea = (217, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.13e+22, 'cm^3/(mol*s)'),
                n = -3.1,
                Ea = (1516, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.38e+27, 'cm^3/(mol*s)'),
                n = -4.49,
                Ea = (6067, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.14e+29, 'cm^3/(mol*s)'),
                n = -5.14,
                Ea = (8273, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.8e+32, 'cm^3/(mol*s)'),
                n = -6.09,
                Ea = (11661, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.8e+35, 'cm^3/(mol*s)'),
                n = -6.85,
                Ea = (14456, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.26e+40, 'cm^3/(mol*s)'),
                n = -8.04,
                Ea = (19009, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.09e+42, 'cm^3/(mol*s)'),
                n = -8.58,
                Ea = (21090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1681,
    label = "C4H72-1OOCH3 <=> C4H7O2-1 + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.54e+35, 's^-1'), n=-7.39, Ea=(39733, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.85e+37, 's^-1'), n=-7.63, Ea=(43994, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.38e+37, 's^-1'), n=-7.14, Ea=(47024, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.16e+36, 's^-1'), n=-6.81, Ea=(47507, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.05e+34, 's^-1'), n=-6.24, Ea=(47760, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.96e+33, 's^-1'), n=-5.74, Ea=(47658, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.31e+30, 's^-1'), n=-4.88, Ea=(47084, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.65e+29, 's^-1'), n=-4.5, Ea=(46721, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1682,
    label = "C4H71-3 + C2H5O2 <=> C4H71-O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1683,
    label = "IC3H7O2 + C4H71-3 <=> IC3H7O + C4H71-O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1684,
    label = "NC3H7O2 + C4H71-3 <=> NC3H7O + C4H71-O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1685,
    label = "C4H71-O <=> C2H3CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+14, 's^-1'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1686,
    label = "C4H71-3 + O <=> C2H3CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1687,
    label = "C4H71-3 + O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1688,
    label = "H + C4H71-3 <=> C4H6 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.16e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1689,
    label = "C2H5 + C4H71-3 <=> C4H6 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1690,
    label = "C2H3 + C4H71-3 <=> C2H4 + C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1691,
    label = "C3H5-A + C4H71-3 <=> C3H6 + C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1692,
    label = "C4H71-3 + C4H71-3 <=> C8H141-5,3-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.11e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (1560.62, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1693,
    label = "C4H71-3 + C4H71-3 <=> C8H141-5,3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.11e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (1560.62, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1694,
    label = "C4H71-3 + C4H71-3 <=> C8H142-6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.11e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (1560.62, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1695,
    label = "C8H141-5,3-4 + OH <=> C8H131-5,3-4,TA + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-2629.06, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1696,
    label = "C8H141-5,3 + OH <=> C8H131-5,3,TA + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-2629.06, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1697,
    label = "C8H141-5,3 + OH <=> C8H131-5,3,SA + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1434.03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1698,
    label = "C8H141-5,3 + OH <=> C8H131-5,3,PA + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+06, 'cm^3/(mol*s)'), n=2, Ea=(-239.01, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1699,
    label = "C8H142-6 + OH <=> C8H132-6,SA + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1434.03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1700,
    label = "C8H142-6 + OH <=> C8H132-6,PA + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+06, 'cm^3/(mol*s)'), n=2, Ea=(-239.01, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1701,
    label = "C8H141-5,3-4 + HO2 <=> C8H131-5,3-4,TA + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (10755.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1702,
    label = "C8H141-5,3 + HO2 <=> C8H131-5,3,TA + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (10755.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1703,
    label = "C8H141-5,3 + HO2 <=> C8H131-5,3,SA + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6300, 'cm^3/(mol*s)'), n=2.6, Ea=(12428.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1704,
    label = "C8H141-5,3 + HO2 <=> C8H131-5,3,PA + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9500, 'cm^3/(mol*s)'), n=2.6, Ea=(13862.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1705,
    label = "C8H142-6 + HO2 <=> C8H132-6,SA + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (12428.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1706,
    label = "C8H142-6 + HO2 <=> C8H132-6,PA + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13862.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1707,
    label = "C8H141-5,3-4 + H <=> C8H131-5,3-4,TA + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (-2868.07, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1708,
    label = "C8H141-5,3 + H <=> C8H131-5,3,TA + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (-2868.07, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1709,
    label = "C8H141-5,3 + H <=> C8H131-5,3,SA + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (-1673.04, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1710,
    label = "C8H141-5,3 + H <=> C8H131-5,3,PA + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (190000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2390.06, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1711,
    label = "C8H142-6 + H <=> C8H132-6,SA + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (-1673.04, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1712,
    label = "C8H142-6 + H <=> C8H132-6,PA + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (380000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2390.06, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1713,
    label = "C8H141-5,3-4 + O <=> C8H131-5,3-4,TA + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (1195.03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1714,
    label = "C8H141-5,3 + O <=> C8H131-5,3,TA + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (1195.03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1715,
    label = "C8H141-5,3 + O <=> C8H131-5,3,SA + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (3107.07, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1716,
    label = "C8H141-5,3 + O <=> C8H131-5,3,PA + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5975.14, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1717,
    label = "C8H142-6 + O <=> C8H132-6,SA + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (3107.07, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1718,
    label = "C8H142-6 + O <=> C8H132-6,PA + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5975.14, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1719,
    label = "C8H141-5,3-4 + CH3 <=> C8H131-5,3-4,TA + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5258.13, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1720,
    label = "C8H141-5,3 + CH3 <=> C8H131-5,3,TA + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5258.13, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1721,
    label = "C8H141-5,3 + CH3 <=> C8H131-5,3,SA + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6931.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1722,
    label = "C8H141-5,3 + CH3 <=> C8H131-5,3,PA + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.15, 'cm^3/(mol*s)'), n=3.5, Ea=(5736.14, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1723,
    label = "C8H142-6 + CH3 <=> C8H132-6,SA + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6931.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1724,
    label = "C8H142-6 + CH3 <=> C8H132-6,PA + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.3, 'cm^3/(mol*s)'), n=3.5, Ea=(5736.14, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1725,
    label = "C8H141-5,3-4 + O2 <=> C8H131-5,3-4,TA + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(35420, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1726,
    label = "C8H141-5,3 + O2 <=> C8H131-5,3,TA + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(35420, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1727,
    label = "C8H141-5,3 + O2 <=> C8H131-5,3,SA + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1728,
    label = "C8H141-5,3 + O2 <=> C8H131-5,3,PA + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(39390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1729,
    label = "C8H142-6 + O2 <=> C8H132-6,SA + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1730,
    label = "C8H142-6 + O2 <=> C8H132-6,PA + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(39390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1731,
    label = "C6H101-3,3 + C2H3 <=> C8H131-5,3-4,TA",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44000, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1732,
    label = "B13DE2M + C3H5-S <=> C8H131-5,3,TA",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44000, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1733,
    label = "C6H10D24 + C2H3 <=> C8H131-5,3,SA",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1734,
    label = "C4H6 + C4H71-3 <=> C8H131-5,3,PA",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1300, 'cm^3/(mol*s)'), n=2.48, Ea=(8520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1735,
    label = "C5H81-3 + C3H5-S <=> C8H132-6,SA",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1736,
    label = "C4H6 + C4H71-3 <=> C8H132-6,PA",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1300, 'cm^3/(mol*s)'), n=2.48, Ea=(8520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1737,
    label = "C6H101-3,3 <=> C2H3 + C4H72-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+15, 's^-1'), n=0, Ea=(99500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1738,
    label = "C6H10D24 <=> C3H5-S + C3H5-S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+15, 's^-1'), n=0, Ea=(99500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1739,
    label = "C8H131-5,3-4,TA + HO2 <=> C8H131-5,3-4,TAO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (1144.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1740,
    label = "C8H131-5,3,TA + HO2 <=> C8H131-5,3,TAO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (1144.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1741,
    label = "C8H131-5,3,SA + HO2 <=> C8H131-5,3,SAO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (1144.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1742,
    label = "C8H131-5,3,PA + HO2 <=> C8H131-5,3,PAO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (1144.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1743,
    label = "C8H132-6,SA + HO2 <=> C8H132-6,SAO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (1144.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1744,
    label = "C8H132-6,PA + HO2 <=> C8H132-6,PAO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (1144.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1745,
    label = "C4H71-3 + C2H3COCH3 <=> C8H131-5,3-4,TAO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1746,
    label = "C4H71-3 + C2H3COCH3 <=> C8H131-5,3,TAO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1747,
    label = "C4H71-3 + SC3H5CHO <=> C8H131-5,3,SAO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.33e+10, 'cm^3/(mol*s)'), n=0, Ea=(6397, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1748,
    label = "C7H111-5,3,6P + CH2O <=> C8H131-5,3,PAO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3496, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1749,
    label = "C4H71-3 + SC3H5CHO <=> C8H132-6,SAO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.33e+10, 'cm^3/(mol*s)'), n=0, Ea=(6397, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1750,
    label = "C7H111-5,1P + CH2O <=> C8H132-6,PAO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3496, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1751,
    label = "CC5H9-A + C2H2 <=> C7H111-5,3,6P",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13200, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1752,
    label = "C5H92-5 + C2H2 <=> C7H111-5,1P",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13200, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1753,
    label = "C4H71-4 + O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1754,
    label = "C4H71-4 + O2 <=> C4H71-4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.865e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1755,
    label = "C4H71-4 + HO2 <=> C4H7O1-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1756,
    label = "CH3O2 + C4H71-4 <=> CH3O + C4H7O1-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1757,
    label = "C4H71-4O2 + H2 <=> C4H71-4OOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1758,
    label = "C4H71-4O2 + HO2 <=> C4H71-4OOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1759,
    label = "C4H71-4O2 + H2O2 <=> C4H71-4OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1760,
    label = "C4H71-4O2 + CH4 <=> C4H71-4OOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1761,
    label = "C4H71-4O2 + CH3OH <=> C4H71-4OOH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1762,
    label = "C4H71-4O2 + CH2O <=> C4H71-4OOH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1763,
    label = "C4H71-4O2 + C2H6 <=> C4H71-4OOH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1764,
    label = "C4H71-4O2 + CH3CHO <=> C4H71-4OOH + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1765,
    label = "C4H71-4O2 + C2H4 <=> C4H71-4OOH + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1766,
    label = "C4H71-4O2 + C3H6 <=> C4H71-4OOH + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0535, 'cm^3/(mol*s)'),
        n = 4.207,
        Ea = (13288.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1767,
    label = "C4H71-4O2 + C2H5CHO <=> C4H71-4OOH + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1768,
    label = "C4H71-4O2 + C2H3CHO <=> C4H71-4OOH + C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1769,
    label = "C4H71-4O2 + C3H8 <=> C4H71-4OOH + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1770,
    label = "C4H71-4O2 + C3H8 <=> C4H71-4OOH + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1771,
    label = "C4H71-4O2 + CH3 <=> C4H7O1-4 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1772,
    label = "C4H71-4O2 + C2H5 <=> C4H7O1-4 + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1773,
    label = "C4H71-4O2 + IC3H7 <=> C4H7O1-4 + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1774,
    label = "C4H71-4O2 + NC3H7 <=> C4H7O1-4 + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1775,
    label = "C4H71-4O2 + C3H5-A <=> C4H7O1-4 + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1776,
    label = "C4H71-4O2 + PC4H9 <=> C4H7O1-4 + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1777,
    label = "C4H71-4O2 + SC4H9 <=> C4H7O1-4 + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1778,
    label = "C4H71-4O2 + C4H71-3 <=> C4H7O1-4 + C4H71-O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1779,
    label = "C4H71-4OOH <=> C4H7O1-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1780,
    label = "C4H71-4O2 + CH3O2 => C4H7O1-4 + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1781,
    label = "C4H71-4O2 + CH3CO3 => C4H7O1-4 + CH3CO2 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1782,
    label = "C4H71-4O2 + C2H5O2 => C4H7O1-4 + C2H5O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1783,
    label = "C4H71-4O2 + NC3H7O2 => C4H7O1-4 + NC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1784,
    label = "C4H71-4O2 + IC3H7O2 => C4H7O1-4 + IC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1785,
    label = "C4H71-4O2 + C4H71-4O2 => C4H7O1-4 + C4H7O1-4 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1786,
    label = "C4H71-4O2 + SC4H9O2 => C4H7O1-4 + SC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1787,
    label = "C4H71-4O2 <=> C4H61-3OOH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.009e+08, 's^-1'), n=1.1, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1788,
    label = "C4H61-3OOH4 <=> C2H3CHOCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+09, 's^-1'), n=1.06, Ea=(10900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1789,
    label = "C4H61-3OOH4 <=> C4H6O25 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+08, 's^-1'), n=0.76, Ea=(11100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1790,
    label = "C2H3CHOCH2 + H => C2H3 + CH2CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1791,
    label = "C2H3CHOCH2 + O => C2H3 + CH2CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1792,
    label = "C2H3CHOCH2 + OH => C2H3 + CH2CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1793,
    label = "C2H3CHOCH2 + HO2 => C2H3 + CH2CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1794,
    label = "C2H3CHOCH2 + CH3 => C2H3 + CH2CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1795,
    label = "C2H3CHOCH2 + CH3O2 => C2H3 + CH2CO + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1796,
    label = "C4H6O25 + H <=> CH2CHCHCHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1797,
    label = "C4H6O25 + O <=> CH2CHCHCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1798,
    label = "C4H6O25 + OH <=> CH2CHCHCHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1799,
    label = "C4H6O25 + HO2 <=> CH2CHCHCHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1800,
    label = "C4H6O25 + CH3 <=> CH2CHCHCHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1801,
    label = "C4H6O25 + CH3O2 <=> CH2CHCHCHO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1802,
    label = "C4H61-3OOH4 + HO2 <=> C4H6O1-3OOH4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=2.74, Ea=(1144.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1803,
    label = "C4H61-3OOH4 + HO2 <=> C4H6O2-1OOH4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=2.74, Ea=(1144.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1804,
    label = "C4H6O1-3OOH4 <=> C2H3CHO + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.7e+39, 's^-1'), n=-8.38, Ea=(22782, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1805,
    label = "C4H6O1-3OOH4 <=> C2H3 + HO2CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.67e+34, 's^-1'), n=-6.63, Ea=(22672, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1806,
    label = "C4H71-1 + O2 <=> C4H71-1O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.07e+27, 'cm^3/(mol*s)'),
        n = -4.67,
        Ea = (5222, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1807,
    label = "C4H71-1O2 <=> C3H6CHO-3 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.22e+29, 's^-1'), n=-4.71, Ea=(42340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1808,
    label = "C4H71-1O2 <=> C2H5CHCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+24, 's^-1'), n=-3.87, Ea=(49850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1809,
    label = "C4H71-2 + O2 <=> C4H71-2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.07e+27, 'cm^3/(mol*s)'),
        n = -4.67,
        Ea = (5222, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1810,
    label = "C4H71-2O2 <=> C2H5COCH2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.22e+29, 's^-1'), n=-4.71, Ea=(42340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1811,
    label = "C4H72-2 + O2 <=> C4H72-2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.07e+27, 'cm^3/(mol*s)'),
        n = -4.67,
        Ea = (5222, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1812,
    label = "C4H72-2O2 <=> CH3CHCOCH3 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.22e+29, 's^-1'), n=-4.71, Ea=(42340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1813,
    label = "C4H8-1 + H <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.55e+06, 'cm^3/(mol*s)'),
                        n = 1.93,
                        Ea = (5564, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.56e+06, 'cm^3/(mol*s)'),
                        n = 1.83,
                        Ea = (5802, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.21e+09, 'cm^3/(mol*s)'),
                        n = 1.18,
                        Ea = (7472, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.47e+16, 'cm^3/(mol*s)'),
                        n = -1.03,
                        Ea = (13413, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.5e+28, 'cm^3/(mol*s)'),
                        n = -4.24,
                        Ea = (23618, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.02e+32, 'cm^3/(mol*s)'),
                        n = -5.22,
                        Ea = (31754, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (3.45e+07, 'cm^3/(mol*s)'),
                        n = 1.81,
                        Ea = (2263, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.06e+07, 'cm^3/(mol*s)'),
                        n = 1.71,
                        Ea = (2522, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.18e+10, 'cm^3/(mol*s)'),
                        n = 1.1,
                        Ea = (4077, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.02e+15, 'cm^3/(mol*s)'),
                        n = -0.49,
                        Ea = (8452, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.58e+21, 'cm^3/(mol*s)'),
                        n = -2.14,
                        Ea = (14245, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.29e+21, 'cm^3/(mol*s)'),
                        n = -1.87,
                        Ea = (17243, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1814,
    label = "C4H8-1 + H <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (7.83e+09, 'cm^3/(mol*s)'),
                        n = 1.17,
                        Ea = (1442, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(3.39e+10, 'cm^3/(mol*s)'), n=1, Ea=(1895, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.7e+13, 'cm^3/(mol*s)'),
                        n = 0.14,
                        Ea = (4127, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.57e+19, 'cm^3/(mol*s)'),
                        n = -1.54,
                        Ea = (9061, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.57e+23, 'cm^3/(mol*s)'),
                        n = -2.66,
                        Ea = (14140, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.32e+20, 'cm^3/(mol*s)'),
                        n = -1.46,
                        Ea = (15383, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.8e+06, 'cm^3/(mol*s)'),
                        n = 1.76,
                        Ea = (5900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.46e+06, 'cm^3/(mol*s)'),
                        n = 1.68,
                        Ea = (6100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.02e+08, 'cm^3/(mol*s)'),
                        n = 1.1,
                        Ea = (7574, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.21e+16, 'cm^3/(mol*s)'),
                        n = -0.99,
                        Ea = (13175, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.14e+27, 'cm^3/(mol*s)'),
                        n = -4.23,
                        Ea = (23319, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1e+33, 'cm^3/(mol*s)'),
                        n = -5.49,
                        Ea = (31922, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1815,
    label = "C4H8-1 + H <=> PC4H9",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.35e+15, 'cm^3/(mol*s)'),
                        n = -2.81,
                        Ea = (1570, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.2e+16, 'cm^3/(mol*s)'),
                        n = -2.97,
                        Ea = (1992, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.91e+21, 'cm^3/(mol*s)'),
                        n = -3.97,
                        Ea = (4636, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.9e+31, 'cm^3/(mol*s)'),
                        n = -6.46,
                        Ea = (11968, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.1e+40, 'cm^3/(mol*s)'),
                        n = -8.6,
                        Ea = (21058, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.44e+37, 'cm^3/(mol*s)'),
                        n = -7.21,
                        Ea = (24896, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.33e+20, 'cm^3/(mol*s)'),
                        n = -4.16,
                        Ea = (-263, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.78e+22, 'cm^3/(mol*s)'),
                        n = -4.33,
                        Ea = (186, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.98e+26, 'cm^3/(mol*s)'),
                        n = -5.18,
                        Ea = (2518, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.78e+32, 'cm^3/(mol*s)'),
                        n = -6.63,
                        Ea = (7265, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.79e+34, 'cm^3/(mol*s)'),
                        n = -6.91,
                        Ea = (10952, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.8e+28, 'cm^3/(mol*s)'),
                        n = -4.79,
                        Ea = (10355, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1816,
    label = "C4H8-1 + H <=> SC4H9",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.07e+22, 'cm^3/(mol*s)'),
                        n = -4.51,
                        Ea = (-771, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.9e+24, 'cm^3/(mol*s)'),
                        n = -4.78,
                        Ea = (-34, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.03e+29, 'cm^3/(mol*s)'),
                        n = -5.81,
                        Ea = (2970, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.53e+34, 'cm^3/(mol*s)'),
                        n = -6.95,
                        Ea = (7525, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.19e+34, 'cm^3/(mol*s)'),
                        n = -6.42,
                        Ea = (9810, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.37e+26, 'cm^3/(mol*s)'),
                        n = -3.79,
                        Ea = (8012, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (3.52e+12, 'cm^3/(mol*s)'),
                        n = -2.15,
                        Ea = (1466, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.02e+14, 'cm^3/(mol*s)'),
                        n = -2.28,
                        Ea = (1799, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.16e+18, 'cm^3/(mol*s)'),
                        n = -3.13,
                        Ea = (4049, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.22e+27, 'cm^3/(mol*s)'),
                        n = -5.53,
                        Ea = (10963, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.33e+37, 'cm^3/(mol*s)'),
                        n = -7.92,
                        Ea = (20354, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.22e+36, 'cm^3/(mol*s)'),
                        n = -7.06,
                        Ea = (25203, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1817,
    label = "C4H8-2 + H <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.96e+06, 'cm^3/(mol*s)'),
                n = 1.86,
                Ea = (6209, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.92e+07, 'cm^3/(mol*s)'),
                n = 1.77,
                Ea = (6443, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.97e+09, 'cm^3/(mol*s)'),
                n = 1.11,
                Ea = (8097, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.01e+17, 'cm^3/(mol*s)'),
                n = -1.09,
                Ea = (14023, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.88e+29, 'cm^3/(mol*s)'),
                n = -4.33,
                Ea = (24297, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.15e+33, 'cm^3/(mol*s)'),
                n = -5.39,
                Ea = (32601, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1818,
    label = "C4H8-2 + H <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.39e+09, 'cm^3/(mol*s)'),
                n = 1.29,
                Ea = (1834, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.6e+10, 'cm^3/(mol*s)'),
                n = 1.12,
                Ea = (2267, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.48e+13, 'cm^3/(mol*s)'),
                n = 0.29,
                Ea = (4456, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.91e+19, 'cm^3/(mol*s)'),
                n = -1.39,
                Ea = (9365, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.13e+23, 'cm^3/(mol*s)'),
                n = -2.53,
                Ea = (14463, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.23e+20, 'cm^3/(mol*s)'),
                n = -1.35,
                Ea = (15762, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1819,
    label = "C4H8-2 + H <=> PC4H9",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.9e+14, 'cm^3/(mol*s)'),
                n = -2.55,
                Ea = (1729, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.41e+16, 'cm^3/(mol*s)'),
                n = -2.71,
                Ea = (2133, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.31e+20, 'cm^3/(mol*s)'),
                n = -3.69,
                Ea = (4719, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.03e+30, 'cm^3/(mol*s)'),
                n = -6.17,
                Ea = (12020, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.19e+39, 'cm^3/(mol*s)'),
                n = -8.33,
                Ea = (21137, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.17e+36, 'cm^3/(mol*s)'),
                n = -6.98,
                Ea = (25063, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1820,
    label = "C4H8-2 + H <=> SC4H9",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.34e+21, 'cm^3/(mol*s)'),
                n = -4.21,
                Ea = (-602, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.79e+23, 'cm^3/(mol*s)'),
                n = -4.46,
                Ea = (82, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.85e+28, 'cm^3/(mol*s)'),
                n = -5.47,
                Ea = (3003, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.45e+33, 'cm^3/(mol*s)'),
                n = -6.61,
                Ea = (7559, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.33e+33, 'cm^3/(mol*s)'),
                n = -6.11,
                Ea = (9893, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.27e+25, 'cm^3/(mol*s)'),
                n = -3.51,
                Ea = (8145, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1821,
    label = "C4H8-1 + H <=> C4H8-2 + H",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.98e+07, 'cm^3/(mol*s)'),
                        n = 1.86,
                        Ea = (3575, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.11e+07, 'cm^3/(mol*s)'),
                        n = 1.77,
                        Ea = (3794, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.78e+09, 'cm^3/(mol*s)'),
                        n = 1.24,
                        Ea = (5152, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.02e+15, 'cm^3/(mol*s)'),
                        n = -0.25,
                        Ea = (9233, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.51e+20, 'cm^3/(mol*s)'),
                        n = -1.82,
                        Ea = (14806, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.44e+19, 'cm^3/(mol*s)'),
                        n = -1.37,
                        Ea = (17409, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(15500, 'cm^3/(mol*s)'), n=2.32, Ea=(7049, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(23600, 'cm^3/(mol*s)'), n=2.27, Ea=(7177, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(660000, 'cm^3/(mol*s)'), n=1.86, Ea=(8201, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (1.15e+12, 'cm^3/(mol*s)'),
                        n = 0.11,
                        Ea = (12789, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.8e+23, 'cm^3/(mol*s)'),
                        n = -3.17,
                        Ea = (22546, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.72e+31, 'cm^3/(mol*s)'),
                        n = -5.16,
                        Ea = (32234, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 1822,
    label = "SC4H9 <=> PC4H9",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.6e+37, 's^-1'), n=-11.04, Ea=(38840, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.05e+40, 's^-1'), n=-11.26, Ea=(39461, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.64e+47, 's^-1'), n=-12.49, Ea=(43112, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.53e+55, 's^-1'), n=-14.27, Ea=(50351, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.13e+56, 's^-1'), n=-13.71, Ea=(54866, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.02e+45, 's^-1'), n=-10.07, Ea=(53399, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1823,
    label = "PC4H9 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.44e+34, 's^-1'), n=-8.1, Ea=(28397, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.11e+39, 's^-1'), n=-9.05, Ea=(31891, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.74e+42, 's^-1'), n=-9.78, Ea=(35771, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.47e+43, 's^-1'), n=-9.67, Ea=(38722, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.06e+39, 's^-1'), n=-7.97, Ea=(38955, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.48e+29, 's^-1'), n=-4.71, Ea=(35950, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1824,
    label = "PC4H9 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.71e+25, 's^-1'), n=-5.81, Ea=(34965, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.85e+27, 's^-1'), n=-6.01, Ea=(35481, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.46e+32, 's^-1'), n=-7.16, Ea=(38637, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.05e+42, 's^-1'), n=-9.61, Ea=(46415, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.98e+48, 's^-1'), n=-10.97, Ea=(54456, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.23e+42, 's^-1'), n=-8.68, Ea=(56601, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1825,
    label = "SC4H9 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.3e+25, 's^-1'), n=-5.75, Ea=(39343, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.12e+27, 's^-1'), n=-5.94, Ea=(39859, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.57e+32, 's^-1'), n=-7.1, Ea=(43029, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.54e+42, 's^-1'), n=-9.54, Ea=(50839, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.06e+49, 's^-1'), n=-10.9, Ea=(58899, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.94e+42, 's^-1'), n=-8.7, Ea=(61203, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1826,
    label = "SC4H9 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.89e+40, 's^-1'), n=-9.76, Ea=(33601, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+44, 's^-1'), n=-10.5, Ea=(37007, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.51e+46, 's^-1'), n=-10.73, Ea=(40237, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.74e+44, 's^-1'), n=-9.85, Ea=(41841, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.79e+37, 's^-1'), n=-7.44, Ea=(40604, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.79e+26, 's^-1'), n=-4.01, Ea=(36898, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1827,
    label = "C4H71-1OH + H <=> PC4H8OH-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.26795e+12, 'cm^3/(mol*s)'),
        n = 0.492751,
        Ea = (4444.58, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1828,
    label = "NC3H7CHO + H <=> PC4H8OH-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.8e+10, 'cm^3/(mol*s)'),
        n = 1.19206,
        Ea = (8785.57, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1829,
    label = "C2H3OH + C2H5 <=> PC4H8OH-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+06, 'cm^3/(mol*s)'),
        n = 1.83442,
        Ea = (7337.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1830,
    label = "C4H8-1 + OH <=> PC4H8OH-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+06, 'cm^3/(mol*s)'),
        n = 1.80584,
        Ea = (-3292.33, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1831,
    label = "C4H71-1OH + H <=> PC4H8OH-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+10, 'cm^3/(mol*s)'),
        n = 1.11403,
        Ea = (4389.24, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1832,
    label = "C4H72-1OH + H <=> PC4H8OH-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+11, 'cm^3/(mol*s)'),
        n = -0.134332,
        Ea = (1584.66, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1833,
    label = "C3H6 + CH2OH <=> PC4H8OH-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000, 'cm^3/(mol*s)'),
        n = 2.42681,
        Ea = (7063.51, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1834,
    label = "C4H71-4OH + H <=> PC4H8OH-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11, 'cm^3/(mol*s)'),
        n = 0.882812,
        Ea = (2750.63, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1835,
    label = "SC4H8OH-1 <=> PC4H8OH-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+08, 's^-1'), n=1.37714, Ea=(37866, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1836,
    label = "C3H6 + CH2OH <=> PC4H8OH-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000, 'cm^3/(mol*s)'),
        n = 2.42681,
        Ea = (7063.51, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1837,
    label = "C4H71-4OH + H <=> PC4H8OH-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11, 'cm^3/(mol*s)'),
        n = 0.882812,
        Ea = (2750.63, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1838,
    label = "SC4H8OH-1 <=> PC4H8OH-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+08, 's^-1'), n=1.37714, Ea=(37866, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1839,
    label = "NC3H7CHO + H <=> PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.7e+09, 'cm^3/(mol*s)'),
        n = 1.43469,
        Ea = (4357.89, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1840,
    label = "NC3H7 + CH2O <=> PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000, 'cm^3/(mol*s)'),
        n = 2.42516,
        Ea = (3238.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1841,
    label = "C4H71-2OH + H <=> SC4H8OH-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+08, 'cm^3/(mol*s)'),
        n = 1.5155,
        Ea = (218.841, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1842,
    label = "C2H5COCH3 + H <=> SC4H8OH-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+07, 'cm^3/(mol*s)'),
        n = 1.80134,
        Ea = (13223.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1843,
    label = "C4H8-1 + OH <=> SC4H8OH-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700000, 'cm^3/(mol*s)'),
        n = 1.80188,
        Ea = (-3290.24, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1844,
    label = "C2H3OH + C2H5 <=> SC4H8OH-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.4e+06, 'cm^3/(mol*s)'),
        n = 1.6709,
        Ea = (10270.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1845,
    label = "C4H8-2 + OH <=> SC4H8OH-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+06, 'cm^3/(mol*s)'),
        n = 1.80188,
        Ea = (-3290.24, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1846,
    label = "SC3H5OH + CH3 <=> SC4H8OH-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.4e+06, 'cm^3/(mol*s)'),
        n = 1.6709,
        Ea = (10270.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1847,
    label = "C2H5COCH3 + H <=> SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+07, 'cm^3/(mol*s)'),
        n = 1.75633,
        Ea = (6206.15, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1848,
    label = "C2H5CHO + CH3 <=> SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000, 'cm^3/(mol*s)'),
        n = 2.28383,
        Ea = (7978.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1849,
    label = "C4H71-4OH + OH <=> C4H64,2-1OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.02e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-437.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1850,
    label = "C4H71-4OH + HO2 <=> C4H64,2-1OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.391, 'cm^3/(mol*s)'), n=3.97, Ea=(11702, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1851,
    label = "PC4H8OH-2 + O2 <=> PC4H8OH-2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1852,
    label = "PC4H8OH-2O2 <=> SQC4H8OP",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.91e+12, 's^-1'), n=-0.226, Ea=(22300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1853,
    label = "PC4H8OH-2O2 <=> C4H72-1OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.64e+14, 's^-1'), n=-0.711, Ea=(32710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1854,
    label = "PC4H8OH-2O2 <=> C4H71-1OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+13, 's^-1'), n=-0.253, Ea=(32590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1855,
    label = "SQC4H8OP => C2H5CHO + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5.36e+12, 's^-1'), n=-0.08, Ea=(10790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1856,
    label = "PC4H8OH-2O2 <=> NC4KET21OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=0.109, Ea=(41390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1857,
    label = "C4H72-1OH + OH <=> C4H64,2-1OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.02e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-436.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1858,
    label = "C4H72-1OH + OH <=> C4H63,1-1OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-436.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1859,
    label = "C4H72-1OH + HO2 <=> C4H64,2-1OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.1725, 'cm^3/(mol*s)'), n=4, Ea=(12103, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1860,
    label = "C4H72-1OH + HO2 <=> C4H63,1-1OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.23, 'cm^3/(mol*s)'), n=4, Ea=(12103, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1861,
    label = "C4H71-1OH + OH <=> C4H63,1-1OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.02e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-437.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1862,
    label = "C4H71-1OH + HO2 <=> C4H63,1-1OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.391, 'cm^3/(mol*s)'), n=3.97, Ea=(11702, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1863,
    label = "C4H64,2-1OH <=> C4H6 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.035e+16, 's^-1'), n=-1.012, Ea=(36070, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1864,
    label = "C4H63,1-1OH <=> C4H5OH-13 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.722e+12, 's^-1'), n=0.488, Ea=(43940, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1865,
    label = "C4H5OH-13 <=> C4H5-N + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.61e+21, 's^-1'), n=-1.612, Ea=(106000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1866,
    label = "C4H5OH-13 <=> C2H3 + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.816e+24, 's^-1'), n=-2.381, Ea=(90130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1867,
    label = "NC4KET21OH + OH <=> C2H4COCH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(-228, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1868,
    label = "NC4KET21OH + HO2 <=> C2H4COCH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(8698, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1869,
    label = "NC4KET21OH + O <=> C2H4COCH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.07e+13, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1870,
    label = "NC4KET21OH + H <=> C2H4COCH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(3200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1871,
    label = "NC4KET21OH + O2 <=> C2H4COCH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(41970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1872,
    label = "NC4KET21OH + CH3 <=> C2H4COCH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74, 'cm^3/(mol*s)'), n=3.46, Ea=(3680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1873,
    label = "NC4KET21OH + CH3O <=> C2H4COCH2OH + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(2771, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1874,
    label = "NC4KET21OH + CH3O2 <=> C2H4COCH2OH + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1875,
    label = "NC4KET21OH + C2H3 <=> C2H4COCH2OH + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1876,
    label = "NC4KET21OH + C2H5 <=> C2H4COCH2OH + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1877,
    label = "C2H4COCH2OH <=> CH3CHCO + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.44e+29, 's^-1'), n=-4.93, Ea=(38330, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1878,
    label = "PC4H8OH-2O2 <=> SQC4H7OHP-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.439e+07, 's^-1'), n=1.4, Ea=(20800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1879,
    label = "SQC4H7OHP-4 <=> CY(CCCO)COH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+09, 's^-1'), n=0.78, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1880,
    label = "SQC4H7OHP-4 => OH + HOCH2CHO + C2H4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.08e+08, 's^-1'), n=1.5, Ea=(23500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1881,
    label = "CY(CCCO)COH + H => C2H4 + HOCH2CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1882,
    label = "CY(CCCO)COH + O => C2H4 + HOCH2CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1883,
    label = "CY(CCCO)COH + OH => C2H4 + HOCH2CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1884,
    label = "CY(CCCO)COH + HO2 => C2H4 + HOCH2CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1885,
    label = "CY(CCCO)COH + CH3 => C2H4 + HOCH2CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1886,
    label = "CY(CCCO)COH + CH3O2 => C2H4 + HOCH2CO + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1887,
    label = "CY(CCCO)COH + H => CH2O + CH2CCH2OH + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1888,
    label = "CY(CCCO)COH + O => CH2O + CH2CCH2OH + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1889,
    label = "CY(CCCO)COH + OH => CH2O + CH2CCH2OH + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1890,
    label = "CY(CCCO)COH + HO2 => CH2O + CH2CCH2OH + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1891,
    label = "CY(CCCO)COH + CH3 => CH2O + CH2CCH2OH + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1892,
    label = "CY(CCCO)COH + CH3O2 => CH2O + CH2CCH2OH + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1893,
    label = "HOCH2CO <=> CH2OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07e+12, 's^-1'), n=0.63, Ea=(16900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1894,
    label = "SQC4H7OHP-4 + O2 <=> SQC4H7OHP-4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1895,
    label = "SQC4H7OHP-4O2 <=> C4H6OHOOH1-4-3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44e+07, 's^-1'), n=1.38, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1896,
    label = "SQC4H7OHP-4O2 <=> NC4KET24OH-1 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(57.9, 's^-1'), n=2.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1897,
    label = "C4H6OHOOH1-4-3 => C2H3CHO + CH2OH + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1898,
    label = "C4H6OHOOH1-4-3 => HOCH2CHO + C2H3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1899,
    label = "NC4KET24OH-1 => CH2O + HOCH2COCH2 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1900,
    label = "HOCH2CHO + O2 <=> HOCH2CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(39150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1901,
    label = "HOCH2CHO + O <=> HOCH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1902,
    label = "HOCH2CHO + H <=> HOCH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(131000, 'cm^3/(mol*s)'), n=2.58, Ea=(1220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1903,
    label = "HOCH2CHO + OH <=> HOCH2CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+12, 'cm^3/(mol*s)'), n=0, Ea=(-619, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1904,
    label = "HOCH2CHO + HO2 <=> HOCH2CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1905,
    label = "HOCH2CHO + CH3 <=> HOCH2CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000708, 'cm^3/(mol*s)'),
        n = 4.58,
        Ea = (1966, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1906,
    label = "HOCH2CHO + CH3O2 <=> HOCH2CO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1907,
    label = "HOCH2CHO + CH3CO3 <=> HOCH2CO + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1908,
    label = "SC4H8OH-1 + O2 <=> SC4H8OH-1O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1909,
    label = "SC4H8OH-1O2 <=> PQC4H8OS",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.3e+10, 's^-1'), n=-0.036, Ea=(22890, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1910,
    label = "SC4H8OH-1O2 <=> NC4KET12OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=0.109, Ea=(41390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1911,
    label = "PQC4H8OS => C2H5CHO + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.7e+39, 's^-1'), n=-8.38, Ea=(22782, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1912,
    label = "PQC4H8OS => C2H5 + HO2CH2CHO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.67e+34, 's^-1'), n=-6.63, Ea=(22672, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1913,
    label = "SC4H8OH-1O2 <=> C4H71-2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+13, 's^-1'), n=-0.253, Ea=(32590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1914,
    label = "SC4H8OH-1O2 <=> PQC4H7OHS-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+07, 's^-1'), n=1.3, Ea=(18200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1915,
    label = "PQC4H7OHS-3 <=> CCY(COCC)OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+09, 's^-1'), n=0.69, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1916,
    label = "PQC4H7OHS-3 => OH + CH2O + SC3H5OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.23e+09, 's^-1'), n=1.3, Ea=(24900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1917,
    label = "C4H71-2OH + OH <=> C4H63,1-2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.02e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-437.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1918,
    label = "C4H71-2OH + HO2 <=> C4H63,1-2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.391, 'cm^3/(mol*s)'), n=3.97, Ea=(11702, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1919,
    label = "C4H63,1-2OH <=> C4H612 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.035e+16, 's^-1'), n=-1.012, Ea=(36070, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1920,
    label = "NC4KET12OH + H <=> C2H5CHOHCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=2.58, Ea=(1220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1921,
    label = "NC4KET12OH + OH <=> C2H5CHOHCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-619, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1922,
    label = "NC4KET12OH + O <=> C2H5CHOHCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1923,
    label = "NC4KET12OH + HO2 <=> C2H5CHOHCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9500, 'cm^3/(mol*s)'), n=2.7, Ea=(11520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1924,
    label = "NC4KET12OH + CH3 <=> C2H5CHOHCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00142, 'cm^3/(mol*s)'),
        n = 4.58,
        Ea = (1966, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1925,
    label = "NC4KET12OH + C2H5 <=> C2H5CHOHCO + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(73600, 'cm^3/(mol*s)'), n=2, Ea=(5917.09, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1926,
    label = "NC4KET12OH + CH3O <=> C2H5CHOHCO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1927,
    label = "NC4KET12OH + CH3O2 <=> C2H5CHOHCO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1928,
    label = "NC4KET12OH + O2 <=> C2H5CHOHCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(43320, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1929,
    label = "NC4KET12OH + C2H3 <=> C2H5CHOHCO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(325600, 'cm^3/(mol*s)'), n=2, Ea=(3965.69, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1930,
    label = "NC4KET12OH + C2H5O <=> C2H5CHOHCO + C2H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+11, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1931,
    label = "C2H5CHOHCO <=> C3H6OH1-1 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.78e+14, 's^-1'), n=0, Ea=(16843.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1932,
    label = "C3H6OH1-1 <=> C2H5CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.981e+11, 's^-1'), n=0.271, Ea=(32990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1933,
    label = "C2H3OH + CH3 <=> C3H6OH1-1",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.04e+40, 'cm^3/(mol*s)'),
                n = -8.25,
                Ea = (24214, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.66e+21, 'cm^3/(mol*s)'),
                n = -3.17,
                Ea = (10241, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1934,
    label = "CCY(COCC)OH + H => OH + C2H3COCH3 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1935,
    label = "CCY(COCC)OH + O => OH + C2H3COCH3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1936,
    label = "CCY(COCC)OH + OH => OH + C2H3COCH3 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1937,
    label = "CCY(COCC)OH + HO2 => OH + C2H3COCH3 + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1938,
    label = "CCY(COCC)OH + CH3 => OH + C2H3COCH3 + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1939,
    label = "CCY(COCC)OH + CH3O2 => OH + C2H3COCH3 + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1940,
    label = "CCY(COCC)OH + H => OH + SC3H5CHO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1941,
    label = "CCY(COCC)OH + O => OH + SC3H5CHO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1942,
    label = "CCY(COCC)OH + OH => OH + SC3H5CHO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1943,
    label = "CCY(COCC)OH + HO2 => OH + SC3H5CHO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1944,
    label = "CCY(COCC)OH + CH3 => OH + SC3H5CHO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1945,
    label = "CCY(COCC)OH + CH3O2 => OH + SC3H5CHO + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1946,
    label = "CCY(COCC)OH + H => C2H3OH + CH3CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1947,
    label = "CCY(COCC)OH + O => C2H3OH + CH3CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1948,
    label = "CCY(COCC)OH + OH => C2H3OH + CH3CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1949,
    label = "CCY(COCC)OH + HO2 => C2H3OH + CH3CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1950,
    label = "CCY(COCC)OH + CH3 => C2H3OH + CH3CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1951,
    label = "CCY(COCC)OH + CH3O2 => C2H3OH + CH3CO + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1952,
    label = "CCY(COCC)OH + H => HCO + SC3H5OH + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1953,
    label = "CCY(COCC)OH + O => HCO + SC3H5OH + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1954,
    label = "CCY(COCC)OH + OH => HCO + SC3H5OH + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1955,
    label = "CCY(COCC)OH + HO2 => HCO + SC3H5OH + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1956,
    label = "CCY(COCC)OH + CH3 => HCO + SC3H5OH + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1957,
    label = "CCY(COCC)OH + CH3O2 => HCO + SC3H5OH + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1958,
    label = "PQC4H7OHS-3 + O2 <=> PQC4H7OHS-3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.744e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1959,
    label = "PQC4H7OHS-3O2 <=> NC4KET13OH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10900, 's^-1'), n=2.4, Ea=(19900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1960,
    label = "NC4KET13OH-2 => CH3CHO + HOCHCHO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1961,
    label = "PQC4H7OHS-3O2 <=> C4H7O2-1,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.91e+12, 's^-1'), n=-0.226, Ea=(22300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1962,
    label = "PQC4H7OHS-3O2 <=> C4H6OHOOH1-3-4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.64e+14, 's^-1'), n=-0.711, Ea=(32710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1963,
    label = "PQC4H7OHS-3O2 <=> C4H6OHOOH2-2-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+13, 's^-1'), n=-0.253, Ea=(32590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1964,
    label = "C4H7O2-1,3OOH => C3KET12 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5.36e+12, 's^-1'), n=-0.08, Ea=(10790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1965,
    label = "C4H7O2-1,3OOH => HO2CH2CHO + CH3CHO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.7e+39, 's^-1'), n=-8.38, Ea=(22782, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1966,
    label = "PQC4H7OHS-3O2 <=> NC4KET24OH-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=0.109, Ea=(41390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1967,
    label = "HOCHCHO + O <=> CHOCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00146, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1968,
    label = "HOCHCHO + OH <=> CHOCHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00581, 'cm^3/(mol*s)'),
        n = 4.28,
        Ea = (-3560, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1969,
    label = "HOCHCHO + H <=> CHOCHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1970,
    label = "HOCHCHO + HO2 <=> CHOCHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (10533.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1971,
    label = "HOCHCHO + CH3 <=> CHOCHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.035, 'cm^3/(mol*s)'), n=3.57, Ea=(7721, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1972,
    label = "HOCHCHO + CH3O2 <=> CHOCHO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.236e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (10533.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1973,
    label = "C4H6OHOOH1-3-4 => CH2O + PC3H4OH-3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1974,
    label = "C4H6OHOOH2-2-1 => CH2O + PC3H4OH-1 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1975,
    label = "NC4KET24OH-3 => CH2O + CH3COCHOH + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1976,
    label = "PC3H4OH-3 <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.69e+52, 's^-1'), n=-13.38, Ea=(45049, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1977,
    label = "PC3H4OH-3 <=> C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.48e+45, 's^-1'), n=-11.63, Ea=(44328, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1978,
    label = "PC3H4OH-3 <=> CH2CCH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.65e+36, 's^-1'), n=-8.86, Ea=(51019, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1979,
    label = "PC3H4OH-3 + O2 <=> C2H3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.26e+17, 'cm^3/(mol*s)'),
        n = -1.638,
        Ea = (869, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1980,
    label = "PC3H4OH-1 <=> CH3CHCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.69e+52, 's^-1'), n=-13.38, Ea=(45049, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1981,
    label = "PC3H4OH-1 <=> PC3H4OH-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.65e+36, 's^-1'), n=-8.86, Ea=(51019, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1982,
    label = "PC3H4OH-1 + O2 <=> CH3CHCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.26e+17, 'cm^3/(mol*s)'),
        n = -1.638,
        Ea = (869, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1983,
    label = "CH3COCHOH <=> CH3COCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.69e+52, 's^-1'), n=-13.38, Ea=(45049, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1984,
    label = "CH3COCHOH <=> CH3COCH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.48e+45, 's^-1'), n=-11.63, Ea=(44328, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1985,
    label = "CH3COCHOH + O2 <=> CH3COCHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.26e+17, 'cm^3/(mol*s)'),
        n = -1.638,
        Ea = (869, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1986,
    label = "SC4H8OH-3 + O2 <=> SC4H8OH-3O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1987,
    label = "SC4H8OH-3O2 <=> SQC4H8OS",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.91e+12, 's^-1'), n=-0.226, Ea=(22300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1988,
    label = "SC4H8OH-3O2 <=> C4H71-3OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.64e+14, 's^-1'), n=-0.711, Ea=(32710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1989,
    label = "SC4H8OH-3O2 <=> C4H72-2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+13, 's^-1'), n=-0.253, Ea=(32590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1990,
    label = "SQC4H8OS => CH3CHO + CH3CHO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.68e+13, 's^-1'), n=-0.08, Ea=(10790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1991,
    label = "SC4H8OH-3O2 <=> NC4KET23OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=0.109, Ea=(41390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1992,
    label = "SC4H8OH-3O2 <=> SQC4H7OHS-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.439e+07, 's^-1'), n=1.4, Ea=(20800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1993,
    label = "SQC4H7OHS-4 <=> CCY(COCC)OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+09, 's^-1'), n=0.78, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1994,
    label = "SQC4H7OHS-4 => OH + CH3CHO + C2H3OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.08e+08, 's^-1'), n=1.5, Ea=(23500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1995,
    label = "C4H71-3OH + OH <=> C4H63,1-3OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.02e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-437.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1996,
    label = "C4H71-3OH + HO2 <=> C4H63,1-3OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.391, 'cm^3/(mol*s)'), n=3.97, Ea=(11702, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1997,
    label = "C4H72-2OH + OH <=> C4H63,1-3OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.02e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-437.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1998,
    label = "C4H72-2OH + HO2 <=> C4H63,1-3OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.391, 'cm^3/(mol*s)'), n=3.97, Ea=(11702, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1999,
    label = "C4H63,1-3OH <=> C4H6 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.035e+16, 's^-1'), n=-1.012, Ea=(36070, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2000,
    label = "NC4KET23OH + OH <=> CH3COCOHCH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(-228, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2001,
    label = "NC4KET23OH + HO2 <=> CH3COCOHCH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(8698, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2002,
    label = "NC4KET23OH + O <=> CH3COCOHCH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.07e+13, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2003,
    label = "NC4KET23OH + H <=> CH3COCOHCH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(3200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2004,
    label = "NC4KET23OH + O2 <=> CH3COCOHCH3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(41970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2005,
    label = "NC4KET23OH + CH3 <=> CH3COCOHCH3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74, 'cm^3/(mol*s)'), n=3.46, Ea=(3680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2006,
    label = "NC4KET23OH + CH3O <=> CH3COCOHCH3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(2771, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2007,
    label = "NC4KET23OH + CH3O2 <=> CH3COCOHCH3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2008,
    label = "NC4KET23OH + C2H3 <=> CH3COCOHCH3 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2009,
    label = "NC4KET23OH + C2H5 <=> CH3COCOHCH3 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2010,
    label = "CH3COHCO + CH3 <=> CH3COCOHCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2011,
    label = "CH3COHCO + OH <=> SC2H4OH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2012,
    label = "CH3COHCO + H <=> SC2H4OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1459, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2013,
    label = "SQC4H7OHS-4 + O2 <=> SQC4H7OHS-4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2014,
    label = "SQC4H7OHS-4O2 <=> NC4KET24OH-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(57.9, 's^-1'), n=2.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2015,
    label = "SQC4H7OHS-4O2 <=> C4H7O2-1,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.3e+10, 's^-1'), n=-0.036, Ea=(22890, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2016,
    label = "SQC4H7OHS-4O2 <=> C4H6OHOOH1-2-3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+13, 's^-1'), n=-0.253, Ea=(32590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2017,
    label = "SQC4H7OHS-4O2 <=> NC4KET13OH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=0.109, Ea=(41390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2018,
    label = "C4H6OHOOH1-2-3 => CH2COHCHO + CH3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2019,
    label = "C4H6OHOOH1-2-3 => CH3CHO + SC2H2OH + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2020,
    label = "SC2H2OH + HCO <=> CH2COHCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2021,
    label = "CH2COHCHO + H <=> CH2COHCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2022,
    label = "CH2COHCHO + O <=> CH2COHCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2023,
    label = "CH2COHCHO + OH <=> CH2COHCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.24e+06, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2024,
    label = "CH2COHCHO + O2 <=> CH2COHCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2025,
    label = "CH2COHCHO + HO2 <=> CH2COHCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2026,
    label = "CH2COHCHO + CH3 <=> CH2COHCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.608e+06, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (5911, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2027,
    label = "CH2COHCHO + C2H3 <=> CH2COHCO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2028,
    label = "CH2COHCHO + CH3O <=> CH2COHCO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2029,
    label = "CH2COHCHO + CH3O2 <=> CH2COHCO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2030,
    label = "SC2H2OH + CO <=> CH2COHCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2031,
    label = "SC2H2OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.69e+52, 's^-1'), n=-13.38, Ea=(45049, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2032,
    label = "SC2H2OH <=> HCCOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+46, 's^-1'), n=-11.63, Ea=(44323, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2033,
    label = "SC2H2OH <=> C2H2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.65e+36, 's^-1'), n=-8.86, Ea=(51019, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2034,
    label = "SC2H2OH + O2 <=> CH2CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.26e+17, 'cm^3/(mol*s)'),
        n = -1.638,
        Ea = (869, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2035,
    label = "SC2H2OH + O2 <=> HCCOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5512, 'cm^3/(mol*s)'), n=2.495, Ea=(-414, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2036,
    label = "C4H8-1 + O <=> NC3H7 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.45e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2037,
    label = "C4H8-1 + O => CH2CO + C2H5 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.05e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2038,
    label = "C4H8-1 + O => C2H5CHCO + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.05e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2039,
    label = "C4H8-2 + O <=> CH3 + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.45e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2040,
    label = "C4H8-2 + O => CH2CO + C2H5 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.05e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2041,
    label = "C4H8-2 + O => C2H5CHCO + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.05e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2042,
    label = "SC4H9O2 <=> C4H8-2 + HO2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(7.25e+09, 's^-1'), n=0.8, Ea=(29900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.7e+10, 's^-1'), n=0.67, Ea=(30700, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2043,
    label = "C4H8OOH1-2 <=> C4H8-1 + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 30, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.09e+13, 's^-1'), n=-1.38, Ea=(9113, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.93e+18, 's^-1'), n=-2.6, Ea=(13142, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.8e+24, 's^-1'), n=-4.05, Ea=(18999, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.76e+26, 's^-1'), n=-4.32, Ea=(20657, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.86e+26, 's^-1'), n=-4.35, Ea=(22246, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.73e+26, 's^-1'), n=-4.06, Ea=(22736, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.39e+23, 's^-1'), n=-3.04, Ea=(22032, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.45e+21, 's^-1'), n=-2.43, Ea=(21227, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2044,
    label = "C4H8-1 + HO2 <=> C4H8OOH2-1",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0133, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(974000, 'cm^3/(mol*s)'), n=0.41, Ea=(7570, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (8.43e+14, 'cm^3/(mol*s)'),
                n = -1.76,
                Ea = (12124, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.82e+20, 'cm^3/(mol*s)'),
                n = -3.03,
                Ea = (16135, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.79e+17, 'cm^3/(mol*s)'),
                n = -2.04,
                Ea = (17111, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2045,
    label = "C4H8-1 + HO2 <=> C4H8O1-2 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0133, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2960, 'cm^3/(mol*s)'), n=2.45, Ea=(12199, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.69e+10, 'cm^3/(mol*s)'),
                n = 0.51,
                Ea = (16606, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.19e+17, 'cm^3/(mol*s)'),
                n = -1.48,
                Ea = (22209, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.73e+21, 'cm^3/(mol*s)'),
                n = -2.51,
                Ea = (27857, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2046,
    label = "C4H8OOH2-1 <=> C4H8O1-2 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0133, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.75e+22, 's^-1'), n=-4.39, Ea=(12349, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.44e+29, 's^-1'), n=-5.9, Ea=(17573, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.52e+30, 's^-1'), n=-5.84, Ea=(19702, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.93e+20, 's^-1'), n=-2.66, Ea=(16454, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2047,
    label = "C4H8-2 + HO2 <=> C4H8OOH2-3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0133, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.53e+12, 'cm^3/(mol*s)'),
                n = -1.27,
                Ea = (10098, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.34e+11, 'cm^3/(mol*s)'),
                n = -0.48,
                Ea = (8480, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.93e+17, 'cm^3/(mol*s)'),
                n = -2.04,
                Ea = (12122, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.45e+19, 'cm^3/(mol*s)'),
                n = -2.45,
                Ea = (14812, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2048,
    label = "C4H8-2 + HO2 <=> C4H8O2-3 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0133, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (765000, 'cm^3/(mol*s)'),
                n = 1.92622,
                Ea = (10745, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.79e+08, 'cm^3/(mol*s)'),
                n = 1.25089,
                Ea = (12370, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.75e+15, 'cm^3/(mol*s)'),
                n = -0.74,
                Ea = (17220, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.37e+20, 'cm^3/(mol*s)'),
                n = -2.28314,
                Ea = (22838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2049,
    label = "C4H8OOH2-3 <=> C4H8O2-3 + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0133, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.02e+19, 's^-1'), n=-3.51, Ea=(9746, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.37e+24, 's^-1'), n=-4.55, Ea=(13480, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.39e+28, 's^-1'), n=-5.25, Ea=(16470, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.54e+27, 's^-1'), n=-4.69, Ea=(17832, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2050,
    label = "C4H8-1 + CH3O2 <=> C4H8O1-2 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(14340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2051,
    label = "C4H8-2 + CH3O2 <=> C4H8O2-3 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(12310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2052,
    label = "C4H6 <=> C4H5-I + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+36, 's^-1'), n=-6.27, Ea=(112353, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2053,
    label = "C4H6 <=> C4H5-N + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+44, 's^-1'), n=-8.62, Ea=(123608, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2054,
    label = "C4H6 <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+15, 's^-1'), n=0, Ea=(94700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2055,
    label = "H2CC + C2H4 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2056,
    label = "C4H6 + H <=> C4H5-N + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12240, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2057,
    label = "C4H5-N + HO2 <=> C4H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2058,
    label = "C4H6 + O <=> C4H5-N + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+06, 'cm^3/(mol*s)'), n=1.9, Ea=(3740, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2059,
    label = "C4H6 + OH <=> C4H5-N + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(3430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2060,
    label = "C4H5-N + H2O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+10, 'cm^3/(mol*s)'), n=0, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2061,
    label = "C4H6 + CH3 <=> C4H5-N + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(22800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2062,
    label = "C4H6 + C2H3 <=> C4H5-N + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(22800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2063,
    label = "C4H6 + C3H3 <=> C4H5-N + C3H4-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(22500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2064,
    label = "C4H6 + C3H5-A <=> C4H5-N + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(22500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2065,
    label = "C4H6 + H <=> C4H5-I + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665000, 'cm^3/(mol*s)'), n=2.53, Ea=(9240, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2066,
    label = "C4H5-I + HO2 <=> C4H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2067,
    label = "C4H6 + O <=> C4H5-I + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+06, 'cm^3/(mol*s)'), n=1.9, Ea=(3740, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2068,
    label = "C4H6 + OH <=> C4H5-I + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2069,
    label = "C4H5-I + H2O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+10, 'cm^3/(mol*s)'), n=0, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2070,
    label = "C4H6 + CH3 <=> C4H5-I + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(19800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2071,
    label = "C4H6 + C2H3 <=> C4H5-I + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(19800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2072,
    label = "C4H6 + C3H3 <=> C4H5-I + C3H4-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2073,
    label = "C4H6 + C3H5-A <=> C4H5-I + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2074,
    label = "C4H6 + H <=> C2H4 + C2H3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.46e+30, 'cm^3/(mol*s)'),
                n = -4.34,
                Ea = (21647, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.45e+30, 'cm^3/(mol*s)'),
                n = -4.51,
                Ea = (21877, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2075,
    label = "C4H6 + H <=> C3H4-P + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2076,
    label = "C4H6 + H <=> C3H4-A + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2077,
    label = "C4H6 + O <=> C2H2 + C2H4O1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+08, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2078,
    label = "C4H6 + O <=> SC3H5CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+07, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2079,
    label = "C4H6 + O <=> CH2CHCHCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2080,
    label = "C4H6 + OH <=> C2H3CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.37e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1040, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2081,
    label = "C4H6 + OH <=> C3H5-A + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.37e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1040, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2082,
    label = "C4H6 + HO2 <=> C4H6O25 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2083,
    label = "C4H6 + HO2 <=> C2H3CHOCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2084,
    label = "C4H6O25 <=> C4H4O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+12, 's^-1'), n=0, Ea=(48500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2085,
    label = "C2H3CHOCH2 <=> C4H6O23",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 's^-1'), n=0, Ea=(50600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2086,
    label = "C4H6O23 <=> SC3H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.95e+13, 's^-1'), n=0, Ea=(49400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2087,
    label = "C4H6O23 <=> C2H4 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.75e+15, 's^-1'), n=0, Ea=(69300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2088,
    label = "C4H6O23 <=> C2H2 + C2H4O1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(75800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2089,
    label = "C4H4O <=> CO + C3H4-P",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+15, 's^-1'), n=0, Ea=(77500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2090,
    label = "C4H4O <=> C2H2 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+14, 's^-1'), n=0, Ea=(77500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2091,
    label = "C2H3 + C2H2 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (7.2e+13, 'cm^3/(mol*s)'),
                n = -0.48,
                Ea = (6100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(5e+14, 'cm^3/(mol*s)'), n=-0.71, Ea=(6700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.6e+16, 'cm^3/(mol*s)'),
                n = -1.25,
                Ea = (8400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2e+18, 'cm^3/(mol*s)'),
                n = -1.68,
                Ea = (10600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.9e+16, 'cm^3/(mol*s)'),
                n = -1.13,
                Ea = (11800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2092,
    label = "C2H3 + C2H2 <=> C4H5-N",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+31, 'cm^3/(mol*s)'),
                n = -7.14,
                Ea = (5600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+32, 'cm^3/(mol*s)'),
                n = -7.33,
                Ea = (6200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.4e+31, 'cm^3/(mol*s)'),
                n = -6.95,
                Ea = (5600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.3e+38, 'cm^3/(mol*s)'),
                n = -8.76,
                Ea = (12000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.1e+37, 'cm^3/(mol*s)'),
                n = -8.09,
                Ea = (13400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2093,
    label = "C2H3 + C2H2 <=> C4H5-I",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(5e+34, 'cm^3/(mol*s)'), n=-8.42, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (2.1e+36, 'cm^3/(mol*s)'),
                n = -8.78,
                Ea = (9100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1e+37, 'cm^3/(mol*s)'), n=-8.77, Ea=(9800, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.6e+46, 'cm^3/(mol*s)'),
                n = -10.98,
                Ea = (18600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.1e+53, 'cm^3/(mol*s)'),
                n = -12.64,
                Ea = (28800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2094,
    label = "C2H3 + C2H3 <=> C4H6",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0263, 0.12, 1], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (7e+57, 'cm^3/(mol*s)'),
                n = -13.82,
                Ea = (17629, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.5e+52, 'cm^3/(mol*s)'),
                n = -11.97,
                Ea = (16056, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.5e+42, 'cm^3/(mol*s)'),
                n = -8.84,
                Ea = (12483, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2095,
    label = "C2H3 + C2H3 <=> C4H5-I + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0263, 0.12, 1], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.5e+30, 'cm^3/(mol*s)'),
                n = -4.95,
                Ea = (12958, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.2e+28, 'cm^3/(mol*s)'),
                n = -4.49,
                Ea = (14273, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.2e+22, 'cm^3/(mol*s)'),
                n = -2.44,
                Ea = (13654, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2096,
    label = "C2H3 + C2H3 <=> C4H5-N + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0263, 0.12, 1], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+24, 'cm^3/(mol*s)'),
                n = -3.28,
                Ea = (12395, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.6e+24, 'cm^3/(mol*s)'),
                n = -3.38,
                Ea = (14650, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.4e+20, 'cm^3/(mol*s)'),
                n = -2.04,
                Ea = (15361, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2097,
    label = "C4H5-N <=> C4H5-I",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.4e+60, 's^-1'), n=-16.08, Ea=(47500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+62, 's^-1'), n=-16.38, Ea=(49600, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.9e+66, 's^-1'), n=-17.26, Ea=(55400, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+67, 's^-1'), n=-16.89, Ea=(59100, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+60, 's^-1'), n=-14.46, Ea=(58600, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2098,
    label = "C4H4 + H <=> C4H5-N",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.2e+51, 'cm^3/(mol*s)'),
                n = -12.57,
                Ea = (12300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.2e+50, 'cm^3/(mol*s)'),
                n = -12.34,
                Ea = (12500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+50, 'cm^3/(mol*s)'),
                n = -11.94,
                Ea = (13400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.3e+51, 'cm^3/(mol*s)'),
                n = -11.92,
                Ea = (16500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.2e+45, 'cm^3/(mol*s)'),
                n = -10.08,
                Ea = (15800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2099,
    label = "C4H4 + H <=> C4H5-I",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.1e+53, 'cm^3/(mol*s)'),
                n = -13.19,
                Ea = (14200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.6e+52, 'cm^3/(mol*s)'),
                n = -12.85,
                Ea = (14300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.1e+52, 'cm^3/(mol*s)'),
                n = -12.44,
                Ea = (15500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.9e+51, 'cm^3/(mol*s)'),
                n = -11.92,
                Ea = (17700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.5e+48, 'cm^3/(mol*s)'),
                n = -10.58,
                Ea = (18800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2100,
    label = "C4H5-N + H <=> C4H5-I + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+26, 'cm^3/(mol*s)'),
        n = -3.35,
        Ea = (17423, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2101,
    label = "C4H5-N + H <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2102,
    label = "C4H5-N + OH <=> C4H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2103,
    label = "C4H5-N + HCO <=> C4H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2104,
    label = "C4H5-N + HO2 => C2H3 + CH2CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2105,
    label = "C4H5-N + O2 <=> CH2CHCHCHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0.29, Ea=(11, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2106,
    label = "C4H5-N + O2 <=> HCO + C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.2e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2107,
    label = "C4H5-N + O2 => H + CO + C2H3CHO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.19e+15, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3312.62, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2108,
    label = "C4H5-I + H <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2109,
    label = "C4H5-I + H <=> C3H3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2110,
    label = "C4H5-I + OH <=> C4H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2111,
    label = "C4H5-I + HCO <=> C4H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2112,
    label = "C4H5-I + HO2 => C2H3 + CH2CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2113,
    label = "C4H5-I + O2 <=> CH2CO + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+10, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2114,
    label = "C4H5-2 <=> C4H5-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+67, 's^-1'), n=-16.89, Ea=(59100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2115,
    label = "C4H5-2 + H <=> C4H5-I + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+26, 'cm^3/(mol*s)'),
        n = -3.35,
        Ea = (17423, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2116,
    label = "C4H5-2 + HO2 => OH + C2H2 + CH3CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2117,
    label = "C4H5-2 + O2 <=> CH3CO + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+10, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2118,
    label = "C4H5-2 + OH <=> CH2OH + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2119,
    label = "C4H5-2 + O <=> CH2O + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2120,
    label = "C4H6 + C2H3 => C6H6 + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(3240, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2121,
    label = "C4H5-I + C2H2 <=> FULVENE + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.738e+26, 'cm^3/(mol*s)'),
        n = -3.76,
        Ea = (21329, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2122,
    label = "C4H5-N + C2H2 <=> FULVENE + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+19, 'cm^3/(mol*s)'),
        n = -1.86,
        Ea = (12384, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2123,
    label = "C4H5-N + C2H2 <=> C6H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (5400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2124,
    label = "C4H5-N + C2H3 <=> C6H6 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e-13, 'cm^3/(mol*s)'),
        n = 7.07,
        Ea = (-3611, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2125,
    label = "C4H5-2 + C2H <=> C3H3 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2126,
    label = "C4H5-2 + C2H2 <=> C6H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+14, 'cm^3/(mol*s)'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2127,
    label = "C4H5-2 + C2H4 <=> C5H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+14, 'cm^3/(mol*s)'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2128,
    label = "C4H612 <=> C4H5-I + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+15, 's^-1'), n=0, Ea=(92600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2129,
    label = "C4H612 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(65000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2130,
    label = "C3H3 + CH3 <=> C4H612",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.6e+57, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9770, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1341, 'K'),
        T1 = (60000, 'K'),
        T2 = (9770, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 2131,
    label = "C4H612 + H <=> C4H5-I + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2132,
    label = "C4H612 + CH3 <=> C4H5-I + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(18500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2133,
    label = "C4H612 + O <=> C4H5-I + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(5880, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2134,
    label = "C4H612 + OH <=> C4H5-I + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2135,
    label = "C4H612 + H <=> C4H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2136,
    label = "C4H612 + H <=> C3H4-A + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2137,
    label = "C4H612 + H <=> C3H4-P + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2138,
    label = "C4H612 + O <=> CH2CO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+08, 'cm^3/(mol*s)'), n=1.65, Ea=(327, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2139,
    label = "C4H6-2 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(65000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2140,
    label = "C4H6-2 <=> C4H612",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(67000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2141,
    label = "C4H6-2 + H <=> C4H612 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2142,
    label = "C4H6-2 + H <=> C4H5-2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(340000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2143,
    label = "C4H6-2 + H <=> CH3 + C3H4-P",
    degeneracy = 1,
    kinetics = Arrhenius(A=(260000, 'cm^3/(mol*s)'), n=2.5, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2144,
    label = "C4H6-2 <=> H + C4H5-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+15, 's^-1'), n=0, Ea=(87300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2145,
    label = "C4H6-2 + CH3 <=> C4H5-2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(18500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2146,
    label = "C4H3-I + H <=> C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+43, 'cm^3/(mol*s)'),
        n = -9.01,
        Ea = (12120, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2147,
    label = "C4H4 + H <=> C4H3-N + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665000, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12240, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2148,
    label = "C4H4 + OH <=> C4H3-N + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+07, 'cm^3/(mol*s)'), n=2, Ea=(3430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2149,
    label = "C4H4 + H <=> C4H3-I + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(333000, 'cm^3/(mol*s)'), n=2.53, Ea=(9240, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2150,
    label = "C4H4 + OH <=> C4H3-I + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+07, 'cm^3/(mol*s)'), n=2, Ea=(430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2151,
    label = "C4H4 + CH3 <=> C4H3-I + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(19800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2152,
    label = "C4H4 + CH3 <=> C4H3-N + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(22800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2153,
    label = "C3H3 + CH2 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2154,
    label = "C4H4 + O <=> C3H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+08, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2155,
    label = "C4H4 + OH <=> CH2O + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2156,
    label = "C2H2 + C2H <=> C4H3-N",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.3e+10, 'cm^3/(mol*s)'),
            n = 0.899,
            Ea = (-363, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.24e+31, 'cm^6/(mol^2*s)'),
            n = -4.718,
            Ea = (1871, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (100, 'K'),
        T1 = (5613, 'K'),
        T2 = (13390, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, 'C=C': 2.5, 'C#C': 2.5},
    ),
)

entry(
    index = 2157,
    label = "C2H2 + C2H <=> C4H3-I",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.3e+10, 'cm^3/(mol*s)'),
            n = 0.899,
            Ea = (-363, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.24e+31, 'cm^6/(mol^2*s)'),
            n = -4.718,
            Ea = (1871, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (100, 'K'),
        T1 = (5613, 'K'),
        T2 = (13390, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, 'C=C': 2.5, 'C#C': 2.5},
    ),
)

entry(
    index = 2158,
    label = "C4H2 + H <=> C4H3-N",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+42, 'cm^3/(mol*s)'),
        n = -8.72,
        Ea = (15300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2159,
    label = "C4H2 + H <=> C4H3-I",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+30, 'cm^3/(mol*s)'),
        n = -4.92,
        Ea = (10800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2160,
    label = "C4H3-N <=> C4H3-I",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.1e+43, 's^-1'), n=-9.49, Ea=(53000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2161,
    label = "C4H3-N + H <=> C4H3-I + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+20, 'cm^3/(mol*s)'),
        n = -1.67,
        Ea = (10800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2162,
    label = "C4H3-N + H <=> C2H2 + H2CC",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+25, 'cm^3/(mol*s)'),
        n = -3.34,
        Ea = (10014, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2163,
    label = "C4H3-N + H <=> C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+47, 'cm^3/(mol*s)'),
        n = -10.26,
        Ea = (13070, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2164,
    label = "C4H3-N + H <=> C4H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2165,
    label = "C4H3-N + OH <=> C4H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2166,
    label = "C4H3-N + C2H3 <=> C3H3 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2167,
    label = "C3H3 + CH <=> C4H3-I + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2168,
    label = "C4H3-I + H <=> C2H2 + H2CC",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+23, 'cm^3/(mol*s)'),
        n = -2.55,
        Ea = (10780, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2169,
    label = "C4H3-I + H <=> C4H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2170,
    label = "C4H3-I + OH <=> C4H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2171,
    label = "C4H3-I + O2 <=> HCCO + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.86e+16, 'cm^3/(mol*s)'), n=-1.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2172,
    label = "C4H3-I + CH2 <=> C3H4-A + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2173,
    label = "C4H4 + C2H <=> L-C6H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2174,
    label = "C4H3-N + C2H2 <=> L-C6H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = -0.56,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2175,
    label = "C4H3-N + C2H2 <=> C-C6H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+46, 'cm^3/(mol*s)'),
        n = -10.01,
        Ea = (30100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2176,
    label = "C4H3-N + C2H2 <=> C6H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+70, 'cm^3/(mol*s)'),
        n = -17.77,
        Ea = (31300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2177,
    label = "C4H3-I + CH3 <=> C5H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2178,
    label = "C3H3 + HCCO <=> C4H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2179,
    label = "H2CC + C2H2 <=> C4H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (350000, 'cm^3/(mol*s)'),
            n = 2.055,
            Ea = (-2400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+60, 'cm^6/(mol^2*s)'),
            n = -12.599,
            Ea = (7417, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.98,
        T3 = (56, 'K'),
        T1 = (580, 'K'),
        T2 = (4164, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, 'C=C': 3, 'C#C': 3},
    ),
)

entry(
    index = 2180,
    label = "C2H2 + C2H <=> C4H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2181,
    label = "C4H2 + OH <=> H2C4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(-410, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2182,
    label = "C4H2 + OH <=> CO + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.58e+19, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (3034, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2183,
    label = "H2C4O + H <=> C2H2 + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2184,
    label = "H2C4O + OH <=> CH2CO + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2185,
    label = "C4H2 + C2H <=> C6H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2186,
    label = "C4H2 + C2H <=> C6H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+37, 'cm^3/(mol*s)'),
        n = -7.68,
        Ea = (7100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2187,
    label = "NC3H7CHO + O2 <=> NC3H7CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(39150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2188,
    label = "NC3H7CHO + O <=> NC3H7CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2189,
    label = "NC3H7CHO + H <=> NC3H7CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(131000, 'cm^3/(mol*s)'), n=2.58, Ea=(1220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2190,
    label = "NC3H7CHO + OH <=> NC3H7CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+12, 'cm^3/(mol*s)'), n=0, Ea=(-619, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2191,
    label = "NC3H7CHO + HO2 <=> NC3H7CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2192,
    label = "NC3H7CHO + CH3 <=> NC3H7CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000708, 'cm^3/(mol*s)'),
        n = 4.58,
        Ea = (1966, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2193,
    label = "NC3H7CHO + CH3O2 <=> NC3H7CO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2194,
    label = "NC3H7CHO + OH <=> C3H6CHO-3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(552, 'cm^3/(mol*s)'), n=3.12, Ea=(-1176, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2195,
    label = "NC3H7CHO + HO2 <=> C3H6CHO-3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.44e+12, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (17880, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2196,
    label = "NC3H7CHO + CH3O2 <=> C3H6CHO-3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.44e+12, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (17880, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2197,
    label = "NC3H7CHO + OH <=> C3H6CHO-2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.68e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2198,
    label = "NC3H7CHO + HO2 <=> C3H6CHO-2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2199,
    label = "NC3H7CHO + CH3O2 <=> C3H6CHO-2 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2200,
    label = "NC3H7CHO + OH <=> C3H6CHO-1 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.28e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2201,
    label = "NC3H7CHO + HO2 <=> C3H6CHO-1 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23790, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2202,
    label = "NC3H7CHO + CH3O2 <=> C3H6CHO-1 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23790, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2203,
    label = "NC3H7CO <=> NC3H7 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(9600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2204,
    label = "C2H5CHCO + H <=> C3H6CHO-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2205,
    label = "C2H3CHO + CH3 <=> C3H6CHO-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2206,
    label = "C3H6CHO-1 <=> C2H4 + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.4e+11, 's^-1'), n=0, Ea=(21970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2207,
    label = "C2H5CHCO + OH <=> NC3H7 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2208,
    label = "C2H5CHCO + H <=> NC3H7 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1459, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2209,
    label = "C2H5CHCO + O <=> C3H6 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2210,
    label = "SC3H5CHO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+14, 's^-1'), n=0, Ea=(69000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2211,
    label = "SC3H5CO + H <=> SC3H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2212,
    label = "CH2CHCHCHO + H <=> SC3H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2213,
    label = "SC3H5CHO + OH <=> SC3H5CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+12, 'cm^3/(mol*s)'), n=0, Ea=(-619, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2214,
    label = "SC3H5CHO + HO2 <=> SC3H5CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2215,
    label = "SC3H5CHO + CH3 <=> SC3H5CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(8700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2216,
    label = "SC3H5CHO + O <=> SC3H5CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+12, 'cm^3/(mol*s)'), n=0, Ea=(1389, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2217,
    label = "SC3H5CHO + O2 <=> SC3H5CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(37600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2218,
    label = "SC3H5CHO + H <=> SC3H5CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2219,
    label = "SC3H5CHO + C2H3 <=> SC3H5CO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11, 'cm^3/(mol*s)'), n=3.5, Ea=(4682, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2220,
    label = "SC3H5CHO + H <=> CH2CHCHCHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2221,
    label = "SC3H5CHO + O <=> CH2CHCHCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2222,
    label = "SC3H5CHO + OH <=> CH2CHCHCHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.46e+06, 'cm^3/(mol*s)'),
        n = 2.072,
        Ea = (1051, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2223,
    label = "SC3H5CHO + CH3 <=> CH2CHCHCHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2224,
    label = "SC3H5CHO + C2H3 <=> CH2CHCHCHO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(4682, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2225,
    label = "SC3H5CHO + H <=> CH3 + C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2226,
    label = "SC3H5CHO + H <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2227,
    label = "C3H5-S + CO <=> SC3H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2228,
    label = "CH2CHCHCHO <=> C3H5-A + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(610000, 's^-1'), n=0.92, Ea=(-1120, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2229,
    label = "CH2CHCHCHO + O2 <=> C2H3CHO + HOCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+36, 'cm^3/(mol*s)'),
        n = -7.25,
        Ea = (33600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2230,
    label = "C2H3COCH3 + OH <=> CH3CHO + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2231,
    label = "C2H3COCH3 + OH => CH2CO + C2H3 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2232,
    label = "C2H3COCH3 + HO2 => CH2CHO + CH3CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.03e+09, 'cm^3/(mol*s)'), n=0, Ea=(7949, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2233,
    label = "C2H3COCH3 + HO2 => CH2CO + C2H3 + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2234,
    label = "C2H3COCH3 + CH3O2 => CH2CHO + CH3CO + CH3O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.97e+11, 'cm^3/(mol*s)'), n=0, Ea=(17050, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2235,
    label = "C2H3COCH3 + CH3O2 => CH2CO + C2H3 + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(17580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2236,
    label = "C2H5COCH3 + OH <=> CH2CH2COCH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.55e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2237,
    label = "C2H5COCH3 + HO2 <=> CH2CH2COCH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2238,
    label = "C2H5COCH3 + O <=> CH2CH2COCH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2239,
    label = "C2H5COCH3 + H <=> CH2CH2COCH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.16e+06, 'cm^3/(mol*s)'), n=2, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2240,
    label = "C2H5COCH3 + O2 <=> CH2CH2COCH3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(51310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2241,
    label = "C2H5COCH3 + CH3 <=> CH2CH2COCH3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(31.9, 'cm^3/(mol*s)'), n=3.17, Ea=(7172, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2242,
    label = "C2H5COCH3 + CH3O <=> CH2CH2COCH3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2243,
    label = "C2H5COCH3 + CH3O2 <=> CH2CH2COCH3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(19380, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2244,
    label = "C2H5COCH3 + C2H3 <=> CH2CH2COCH3 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2245,
    label = "C2H5COCH3 + C2H5 <=> CH2CH2COCH3 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2246,
    label = "C2H5COCH3 + OH <=> CH3CHCOCH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(-228, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2247,
    label = "C2H5COCH3 + HO2 <=> CH3CHCOCH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(8698, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2248,
    label = "C2H5COCH3 + O <=> CH3CHCOCH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.07e+13, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2249,
    label = "C2H5COCH3 + H <=> CH3CHCOCH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(3200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2250,
    label = "C2H5COCH3 + O2 <=> CH3CHCOCH3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(41970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2251,
    label = "C2H5COCH3 + CH3 <=> CH3CHCOCH3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74, 'cm^3/(mol*s)'), n=3.46, Ea=(3680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2252,
    label = "C2H5COCH3 + CH3O <=> CH3CHCOCH3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(2771, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2253,
    label = "C2H5COCH3 + CH3O2 <=> CH3CHCOCH3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2254,
    label = "C2H5COCH3 + C2H3 <=> CH3CHCOCH3 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2255,
    label = "C2H5COCH3 + C2H5 <=> CH3CHCOCH3 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2256,
    label = "C2H5COCH3 + OH <=> C2H5COCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2257,
    label = "C2H5COCH3 + HO2 <=> C2H5COCH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(14690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2258,
    label = "C2H5COCH3 + O <=> C2H5COCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(5962, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2259,
    label = "C2H5COCH3 + H <=> C2H5COCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(6357, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2260,
    label = "C2H5COCH3 + O2 <=> C2H5COCH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(49150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2261,
    label = "C2H5COCH3 + CH3 <=> C2H5COCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(9630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2262,
    label = "C2H5COCH3 + CH3O <=> C2H5COCH2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(4660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2263,
    label = "C2H5COCH3 + CH3O2 <=> C2H5COCH2 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(17580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2264,
    label = "C2H5COCH3 + C2H3 <=> C2H5COCH2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.15e+10, 'cm^3/(mol*s)'), n=0, Ea=(4278, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2265,
    label = "C2H5COCH3 + C2H5 <=> C2H5COCH2 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(11600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2266,
    label = "C2H3COCH3 + H <=> CH3CHCOCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2267,
    label = "CH3CHCO + CH3 <=> CH3CHCOCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2268,
    label = "C2H5COCH2 <=> CH2CO + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(35000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2269,
    label = "CH3CHCOCH3 + O2 <=> CH3CHOOCOCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2270,
    label = "CH3CHOOCOCH3 <=> CH2CHOOHCOCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.9e+12, 's^-1'), n=0, Ea=(29700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2271,
    label = "C2H3COCH3 + HO2 <=> CH2CHOOHCOCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+10, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2272,
    label = "C5H81-3 + OH <=> CH2O + C4H71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2273,
    label = "C5H81-3 + OH <=> C2H3CHO + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2274,
    label = "C5H81-3 + OH <=> CH3CHO + C3H5-S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2275,
    label = "C4H7O1-4 <=> CH2O + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.326e+21, 's^-1'), n=-2.349, Ea=(25084, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2276,
    label = "C5H10-1 <=> C2H5 + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.864e+21, 's^-1'), n=-2.086, Ea=(75060, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2277,
    label = "C4H71-3 + CH3 <=> C5H10-2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1e+14, 'cm^3/(mol*s)'),
            n = -0.32,
            Ea = (-262.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.91e+60, 'cm^6/(mol^2*s)'),
            n = -12.81,
            Ea = (6250, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.104,
        T3 = (1606, 'K'),
        T1 = (60000, 'K'),
        T2 = (6118, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 2278,
    label = "C5H10-1 + O2 <=> C5H91-5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2279,
    label = "C5H10-1 + O <=> C5H91-5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2280,
    label = "C5H10-1 + H <=> C5H91-5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2281,
    label = "C5H10-1 + OH <=> C5H91-5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2282,
    label = "C5H10-1 + HO2 <=> C5H91-5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2283,
    label = "C5H10-1 + CH3 <=> C5H91-5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.4521, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2284,
    label = "C5H10-1 + CH3O <=> C5H91-5 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2285,
    label = "C5H10-1 + CH3O2 <=> C5H91-5 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2286,
    label = "C5H10-2 + O2 <=> C5H92-5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2287,
    label = "C5H10-2 + O <=> C5H92-5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2288,
    label = "C5H10-2 + H <=> C5H92-5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665100, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2289,
    label = "C5H10-2 + OH <=> C5H92-5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2290,
    label = "C5H10-2 + HO2 <=> C5H92-5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2291,
    label = "C5H10-2 + CH3 <=> C5H92-5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.4521, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2292,
    label = "C5H10-2 + CH3O <=> C5H92-5 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2293,
    label = "C5H10-2 + CH3O2 <=> C5H92-5 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2294,
    label = "C5H10-1 + O2 <=> C5H91-4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2295,
    label = "C5H10-1 + O <=> C5H91-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(551000, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2296,
    label = "C5H10-1 + H <=> C5H91-4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2297,
    label = "C5H10-1 + OH <=> C5H91-4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2298,
    label = "C5H10-1 + HO2 <=> C5H91-4 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2299,
    label = "C5H10-1 + CH3 <=> C5H91-4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2300,
    label = "C5H10-1 + CH3O <=> C5H91-4 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(4571, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2301,
    label = "C5H10-1 + CH3O2 <=> C5H91-4 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2302,
    label = "C5H10-2 + O2 <=> C5H91-3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2303,
    label = "C5H10-2 + O <=> C5H91-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(441000, 'cm^3/(mol*s)'), n=2.42, Ea=(3150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2304,
    label = "C5H10-2 + H <=> C5H91-3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2305,
    label = "C5H10-2 + OH <=> C5H91-3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2306,
    label = "C5H10-2 + HO2 <=> C5H91-3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9639, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2307,
    label = "C5H10-2 + CH3 <=> C5H91-3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2308,
    label = "C5H10-2 + CH3O <=> C5H91-3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(90, 'cm^3/(mol*s)'), n=2.95, Ea=(11990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2309,
    label = "C5H10-2 + CH3O2 <=> C5H91-3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9639, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2310,
    label = "C5H10-1 + O2 <=> C5H91-3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(37220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2311,
    label = "C5H10-1 + O <=> C5H91-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(660000, 'cm^3/(mol*s)'), n=2.43, Ea=(1210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2312,
    label = "C5H10-1 + H <=> C5H91-3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2313,
    label = "C5H10-1 + OH <=> C5H91-3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2314,
    label = "C5H10-1 + HO2 <=> C5H91-3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2315,
    label = "C5H10-1 + CH3 <=> C5H91-3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2316,
    label = "C5H10-1 + CH3O <=> C5H91-3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2317,
    label = "C5H10-1 + CH3O2 <=> C5H91-3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2318,
    label = "C5H10-2 + O2 <=> C5H92-4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(37220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2319,
    label = "C5H10-2 + O <=> C5H92-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(990000, 'cm^3/(mol*s)'), n=2.43, Ea=(1210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2320,
    label = "C5H10-2 + H <=> C5H92-4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2321,
    label = "C5H10-2 + OH <=> C5H92-4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2322,
    label = "C5H10-2 + HO2 <=> C5H92-4 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2323,
    label = "C5H10-2 + CH3 <=> C5H92-4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2324,
    label = "C5H10-2 + CH3O <=> C5H92-4 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2325,
    label = "C5H10-2 + CH3O2 <=> C5H92-4 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2326,
    label = "C4H6 + CH3 <=> C5H91-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2327,
    label = "C5H81-3 + H <=> C5H91-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2328,
    label = "C3H6 + C2H3 <=> C5H91-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2329,
    label = "C2H4 + C3H5-A <=> C5H91-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2330,
    label = "C5H81-3 + H <=> C5H92-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2331,
    label = "C2H4 + C3H5-S <=> C5H92-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2332,
    label = "C5H9O1-3 + OH <=> C5H91-3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.088e+15, 'cm^3/(mol*s)'),
        n = -1.07,
        Ea = (15720, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2333,
    label = "C5H9O1-3 + CH3O <=> C5H91-3 + CH3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.946e+17, 'cm^3/(mol*s)'),
        n = -1.65,
        Ea = (20480, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2334,
    label = "C5H9O1-3 + C2H5O <=> C5H91-3 + C2H5O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.893e+14, 'cm^3/(mol*s)'),
        n = -0.72,
        Ea = (18330, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2335,
    label = "C5H9O2-4 + OH <=> C5H92-4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.027e+15, 'cm^3/(mol*s)'),
        n = -1.24,
        Ea = (15890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2336,
    label = "C5H9O2-4 + CH3O <=> C5H92-4 + CH3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.863e+17, 'cm^3/(mol*s)'),
        n = -1.82,
        Ea = (20650, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2337,
    label = "C5H9O2-4 + C2H5O <=> C5H92-4 + C2H5O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.493e+14, 'cm^3/(mol*s)'),
        n = -0.89,
        Ea = (18490, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2338,
    label = "C5H9O1-3 <=> C2H3CHO + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.131e+19, 's^-1'), n=-1.85, Ea=(10670, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2339,
    label = "C5H9O1-3 <=> C2H5CHO + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.417e+18, 's^-1'), n=-1.56, Ea=(23340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2340,
    label = "C5H9O2-4 <=> SC3H5CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.983e+15, 's^-1'), n=-1.13, Ea=(9941, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2341,
    label = "C5H9O2-4 <=> CH3CHO + C3H5-S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.073e+22, 's^-1'), n=-2.66, Ea=(29650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2342,
    label = "BC5H10 <=> C4H72-2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.217e+23, 's^-1'), n=-1.926, Ea=(101400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2343,
    label = "BC5H10 <=> IC4H7 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.61e+19, 's^-1'), n=-1.017, Ea=(79020, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2344,
    label = "C4H71-3 + CH3 <=> CC5H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1e+14, 'cm^3/(mol*s)'),
            n = -0.32,
            Ea = (-262.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.91e+60, 'cm^6/(mol^2*s)'),
            n = -12.81,
            Ea = (6250, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.104,
        T3 = (1606, 'K'),
        T1 = (60000, 'K'),
        T2 = (6118, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 2345,
    label = "CC5H10 + H <=> CC5H9-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2346,
    label = "CC5H10 + OH <=> CC5H9-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+08, 'cm^3/(mol*s)'), n=1.61, Ea=(-35, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2347,
    label = "CC5H10 + HO2 <=> CC5H9-A + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(28920, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2348,
    label = "CC5H10 + CH3 <=> CC5H9-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.53, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2349,
    label = "CC5H10 + CH3O <=> CC5H9-A + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.35e+11, 'cm^3/(mol*s)'), n=0, Ea=(4571, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2350,
    label = "CC5H10 + CH3O2 <=> CC5H9-A + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(28920, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2351,
    label = "BC5H10 + H <=> AC5H9-C + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(346000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2352,
    label = "BC5H10 + H <=> CC5H9-B + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2353,
    label = "BC5H10 + OH <=> AC5H9-C + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.24e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2354,
    label = "BC5H10 + OH <=> CC5H9-B + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2355,
    label = "BC5H10 + HO2 <=> AC5H9-C + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2356,
    label = "BC5H10 + HO2 <=> CC5H9-B + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9639, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2357,
    label = "BC5H10 + CH3 <=> AC5H9-C + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.42, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2358,
    label = "BC5H10 + CH3 <=> CC5H9-B + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2359,
    label = "BC5H10 + CH3O <=> AC5H9-C + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(180, 'cm^3/(mol*s)'), n=2.95, Ea=(11990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2360,
    label = "BC5H10 + CH3O <=> CC5H9-B + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(90, 'cm^3/(mol*s)'), n=2.95, Ea=(11990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2361,
    label = "BC5H10 + CH3O2 <=> AC5H9-C + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2362,
    label = "BC5H10 + CH3O2 <=> CC5H9-B + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9639, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2363,
    label = "CC5H10 + H <=> CC5H9-B + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.65e+06, 'cm^3/(mol*s)'), n=2.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2364,
    label = "CC5H10 + OH <=> CC5H9-B + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(614, 'cm^3/(mol*s)'), n=3.2, Ea=(-3500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2365,
    label = "CC5H10 + HO2 <=> CC5H9-B + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1810, 'cm^3/(mol*s)'), n=2.5, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2366,
    label = "CC5H10 + CH3 <=> CC5H9-B + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.613, 'cm^3/(mol*s)'), n=3.1, Ea=(2330, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2367,
    label = "CC5H10 + CH3O <=> CC5H9-B + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10, 'cm^3/(mol*s)'), n=2.85, Ea=(5231, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2368,
    label = "CC5H10 + CH3O2 <=> CC5H9-B + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1810, 'cm^3/(mol*s)'), n=2.5, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2369,
    label = "BC5H10 + OH <=> IC3H7 + CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+10, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2370,
    label = "CC5H10 + OH <=> IC4H9 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+10, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2371,
    label = "CC5H9-B + HO2 <=> CC5H9O-B + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2372,
    label = "CC5H9-B + CH3O2 <=> CC5H9O-B + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2373,
    label = "CC5H9-B + C2H5O2 <=> CC5H9O-B + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2374,
    label = "AC5H9-D <=> AC5H9-A2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.113e+12, 's^-1'), n=0, Ea=(31700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2375,
    label = "AC5H10 <=> C3H5-T + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.922e+24, 's^-1'), n=-2.409, Ea=(100500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2376,
    label = "IC4H7 + CH3 <=> AC5H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.5e+14, 'cm^3/(mol*s)'),
            n = -0.32,
            Ea = (-262.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.865e+60, 'cm^6/(mol^2*s)'),
            n = -12.81,
            Ea = (6250, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.104,
        T3 = (1606, 'K'),
        T1 = (60000, 'K'),
        T2 = (6118, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 2377,
    label = "AC5H10 + H <=> AC5H9-A2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2378,
    label = "AC5H10 + O <=> AC5H9-A2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (370000, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (-1130, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2379,
    label = "AC5H10 + OH <=> AC5H9-A2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2380,
    label = "AC5H10 + HO2 <=> AC5H9-A2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9639, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2381,
    label = "AC5H10 + CH3 <=> AC5H9-A2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2382,
    label = "AC5H10 + CH3O2 <=> AC5H9-A2 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9639, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2383,
    label = "AC5H10 + CH3O <=> AC5H9-A2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(90, 'cm^3/(mol*s)'), n=2.95, Ea=(11990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2384,
    label = "AC5H10 + H <=> AC5H9-C + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2385,
    label = "AC5H10 + OH <=> AC5H9-C + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2386,
    label = "AC5H10 + HO2 <=> AC5H9-C + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2387,
    label = "AC5H10 + CH3 <=> AC5H9-C + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2388,
    label = "AC5H10 + CH3O2 <=> AC5H9-C + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2389,
    label = "AC5H10 + CH3O <=> AC5H9-C + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2390,
    label = "AC5H10 + H <=> AC5H9-D + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.95e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2391,
    label = "AC5H10 + OH <=> AC5H9-D + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.01e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2392,
    label = "AC5H10 + CH3 <=> AC5H9-D + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.27, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2393,
    label = "AC5H10 + HO2 <=> AC5H9-D + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14500, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2394,
    label = "AC5H10 + CH3O <=> AC5H9-D + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.18e+11, 'cm^3/(mol*s)'), n=0, Ea=(4571, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2395,
    label = "AC5H10 + CH3O2 <=> AC5H9-D + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14500, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2396,
    label = "AC5H9-A2 <=> C3H4-A + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.983e+20, 's^-1'), n=-1.63, Ea=(59240, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2397,
    label = "B13DE2M + H <=> AC5H9-C",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(1300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2398,
    label = "C4H612 + CH3 <=> AC5H9-C",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2399,
    label = "B13DE2M + H <=> AC5H9-D",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2400,
    label = "AC5H9-D <=> C3H5-T + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.22e+12, 's^-1'), n=0.64, Ea=(29370, 'cal/mol'), T0=(1, 'K')),
)


entry(
    index = 2401,
    label = "AC5H10 + OH <=> SC4H9 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+10, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2402,
    label = "AC5H10 + O <=> SC4H9 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (723000, 'cm^3/(mol*s)'),
        n = 2.34,
        Ea = (-1050, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2403,
    label = "AC5H10 + O <=> IC3H7 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (723000, 'cm^3/(mol*s)'),
        n = 2.34,
        Ea = (-1050, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2404,
    label = "AC5H10 + O <=> IC4H9 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (723000, 'cm^3/(mol*s)'),
        n = 2.34,
        Ea = (-1050, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2405,
    label = "AC5H9-C + HO2 <=> AC5H9O-C + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2406,
    label = "AC5H9-C + CH3O2 <=> AC5H9O-C + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2407,
    label = "AC5H9-C + C2H5O2 <=> AC5H9O-C + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2408,
    label = "CH3CHO + C3H5-T <=> AC5H9O-C",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2409,
    label = "AC5H9-C + HO2 <=> B2E2M1OJ + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2410,
    label = "AC5H9-C + CH3O2 <=> B2E2M1OJ + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2411,
    label = "CH2O + C4H72-2 <=> B2E2M1OJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2412,
    label = "C2H3 + C3H5-T <=> B13DE2M",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2413,
    label = "H + B13DE2MJ <=> B13DE2M",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2414,
    label = "B13DE2M + H <=> B13DE2MJ + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (364400, 'cm^3/(mol*s)'),
        n = 2.455,
        Ea = (4361.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2415,
    label = "B13DE2M + O2 <=> B13DE2MJ + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.96e+19, 'cm^3/(mol*s)'),
        n = -1.67,
        Ea = (46192.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2416,
    label = "B13DE2M + OH <=> B13DE2MJ + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.46e+06, 'cm^3/(mol*s)'),
        n = 2.072,
        Ea = (1050.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2417,
    label = "B13DE2M + HO2 <=> B13DE2MJ + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0307, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2418,
    label = "B13DE2M + CH3 <=> B13DE2MJ + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2419,
    label = "B13DE2M + CH3O2 <=> B13DE2MJ + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0768, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2420,
    label = "C2H3 + C3H4-A <=> B13DE2MJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2421,
    label = "B13DE2M + H <=> CC5H9-B",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2422,
    label = "B13DE2M + H <=> CC5H9-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2423,
    label = "B12DE3M + H <=> CC5H9-B",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2424,
    label = "C2H3 + C3H6 <=> CC5H9-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2425,
    label = "C2H3 + CH3COCH3 <=> CC5H9O-B",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2426,
    label = "CC5H9-B + HO2 <=> B2E3M1OJ + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2427,
    label = "CC5H9-B + CH3O2 <=> B2E3M1OJ + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2428,
    label = "CH2O + IC4H7-I1 <=> B2E3M1OJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2429,
    label = "TC4H8CHO <=> IC3H5CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(26290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2430,
    label = "TC4H8CHO <=> IC4H8 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.52e+12, 's^-1'), n=0, Ea=(20090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2431,
    label = "TC4H8CHO + O2 <=> O2C4H8CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2432,
    label = "O2C4H8CHO <=> O2HC4H8CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+11, 's^-1'), n=0, Ea=(15360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2433,
    label = "IC4H8O2H-T + CO <=> O2HC4H8CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4809, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2434,
    label = "C6H101-5 <=> C3H5-A + C3H5-A",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 4, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.07e+47, 's^-1'), n=-9.7, Ea=(72680, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.22e+39, 's^-1'), n=-7.3, Ea=(69390, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.12e+35, 's^-1'), n=-6, Ea=(67620, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2435,
    label = "C6H101-5 + H <=> C6H9-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(675200, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2436,
    label = "C6H101-5 + O2 <=> C6H9-A + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(38890, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2437,
    label = "C6H101-5 + O <=> C6H9-A + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+06, 'cm^3/(mol*s)'),
        n = 2.43,
        Ea = (1210, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2438,
    label = "C6H101-5 + OH <=> C6H9-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(55280, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2439,
    label = "C6H101-5 + CH3 <=> C6H9-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.38, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2440,
    label = "C4H6 + C2H3 <=> C6H9-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(880000, 'cm^3/(mol*s)'), n=2.5, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2441,
    label = "C6H101-5 + H => C3H4-A + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2442,
    label = "C6H101-5 + H <=> C3H5-A + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2443,
    label = "L-C6H4 + H <=> C-C6H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+54, 'cm^3/(mol*s)'),
        n = -11.7,
        Ea = (34500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2444,
    label = "C-C6H4 + H <=> C6H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+60, 'cm^3/(mol*s)'),
        n = -13.66,
        Ea = (29500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2445,
    label = "L-C6H4 + H <=> C6H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+78, 'cm^3/(mol*s)'),
        n = -19.72,
        Ea = (31400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2446,
    label = "C6H3 + H <=> L-C6H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+43, 'cm^3/(mol*s)'),
        n = -9.01,
        Ea = (12120, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2447,
    label = "L-C6H4 + H <=> C6H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (9240, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2448,
    label = "L-C6H4 + OH <=> C6H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2449,
    label = "C6H2 + H <=> C6H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+30, 'cm^3/(mol*s)'),
        n = -4.92,
        Ea = (10800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2450,
    label = "C6H3 + H <=> C6H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2451,
    label = "C6H3 + OH <=> C6H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2452,
    label = "C6H3 + H <=> C4H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+23, 'cm^3/(mol*s)'),
        n = -2.55,
        Ea = (10780, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2453,
    label = "C6H5 + H <=> C6H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.6e+75, 'cm^6/(mol^2*s)'),
            n = -16.3,
            Ea = (7000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (0.1, 'K'),
        T1 = (584.9, 'K'),
        T2 = (6113, 'K'),
        efficiencies = {'[H][H]': 2, 'C': 2, '[C]=O': 1.5, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 2454,
    label = "FULVENE <=> C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.95e+31, 's^-1'), n=-4.97, Ea=(88470, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2455,
    label = "FULVENE <=> C6H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.511e+24, 's^-1'), n=-2.505, Ea=(113330, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2456,
    label = "C6H6 + H <=> FULVENE + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+32, 'cm^3/(mol*s)'),
        n = -4.95,
        Ea = (51244, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2457,
    label = "C6H6 + H <=> C6H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2458,
    label = "C6H6 + O2 <=> C6H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2459,
    label = "C6H6 + O <=> C6H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(14700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2460,
    label = "C6H6 + OH <=> C6H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2, 'cm^3/(mol*s)'), n=4.1, Ea=(-301, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2461,
    label = "C6H6 + HO2 <=> C6H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2462,
    label = "C6H6 + CH3 <=> C6H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.32e+12, 'cm^3/(mol*s)'), n=0, Ea=(18920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2463,
    label = "C6H5 + CH2O <=> C6H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(85500, 'cm^3/(mol*s)'), n=2.19, Ea=(38, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2464,
    label = "C6H5 + HCO <=> C6H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(85500, 'cm^3/(mol*s)'), n=2.19, Ea=(38, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2465,
    label = "C6H5 => H + C4H2 + C2H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4.3e+12, 's^-1'), n=0.62, Ea=(77294, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2466,
    label = "C6H6 + O <=> C6H5O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(4530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2467,
    label = "C6H6 + OH <=> C6H5OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(132, 'cm^3/(mol*s)'), n=3.25, Ea=(5590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2468,
    label = "C6H5 + HO2 <=> C6H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2469,
    label = "C6H5 + O2 <=> C6H5O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(6120, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2470,
    label = "C6H5 + O2 <=> O-C6H4O2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(8980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2471,
    label = "C6H5 + O2 <=> C6H5OO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.86e+13, 'cm^3/(mol*s)'),
        n = -0.22,
        Ea = (-711, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2472,
    label = "C6H5OO <=> C6H5O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.27e+15, 's^-1'), n=-0.246, Ea=(38536, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2473,
    label = "C6H5O + OH <=> C6H5OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2474,
    label = "C6H5O + H <=> C6H5OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e+94, 'cm^6/(mol^2*s)'),
            n = -21.84,
            Ea = (13880, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.043,
        T3 = (304.2, 'K'),
        T1 = (60000, 'K'),
        T2 = (5896, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 2475,
    label = "C6H4OH + H <=> C6H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2476,
    label = "C6H5OH <=> C5H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.31e+15, 's^-1'), n=-0.61, Ea=(74115, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2477,
    label = "C6H5OH + H <=> C6H5O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(12400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2478,
    label = "C6H5OH + O2 <=> C6H5O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(38800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2479,
    label = "C6H5OH + O <=> C6H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2480,
    label = "C6H5OH + OH <=> C6H5O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+08, 'cm^3/(mol*s)'), n=1.4, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2481,
    label = "C6H5OH + HO2 <=> C6H5O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2482,
    label = "C6H5OH + CH3 <=> C6H5O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2483,
    label = "C6H5OH + C3H5-A <=> C6H5O + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(9400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2484,
    label = "C6H5OH + C4H5-I <=> C6H5O + C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(9400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2485,
    label = "C6H5OH + C6H5 <=> C6H5O + C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(4400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2486,
    label = "C6H5OH + C6H5OO <=> C6H5O + C6H5OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.33e+11, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2487,
    label = "C6H5OH + H <=> C6H4OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+14, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2488,
    label = "C6H5OH + O <=> C6H4OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(14700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2489,
    label = "C6H5OH + OH <=> C6H4OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2490,
    label = "C6H5OH + HO2 <=> C6H4OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2491,
    label = "C6H5OH + CH3 <=> C6H4OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2492,
    label = "C6H5OH + O <=> OC6H4OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2493,
    label = "C6H5O <=> CO + C5H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(43900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2494,
    label = "C6H5O + H <=> CO + C5H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2495,
    label = "C6H5O + O <=> C5H5 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2496,
    label = "C6H5O + O <=> OC6H4OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+10, 'cm^3/(mol*s)'), n=0.47, Ea=(800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2497,
    label = "C6H4OH + O2 <=> OC6H4OH + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(6100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2498,
    label = "OC6H4OH <=> C5H4OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.4e+11, 's^-1'), n=0, Ea=(43800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2499,
    label = "C6H5O + O <=> P-C6H4O2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2500,
    label = "C6H5O + O <=> O-C6H4O2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2501,
    label = "C6H5O + HO2 <=> O-OC6H5OJ + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2502,
    label = "P-C6H4O2 + H <=> P-OC6H5OJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(9740, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2503,
    label = "O-C6H4O2 + H <=> O-OC6H5OJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(6960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2504,
    label = "O-C6H4O2 <=> C5H4O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 's^-1'), n=0, Ea=(40000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2505,
    label = "P-C6H4O2 <=> C5H4O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+11, 's^-1'), n=0, Ea=(59000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2506,
    label = "P-C6H3O2 + H <=> P-C6H4O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2507,
    label = "P-C6H4O2 + H <=> P-C6H3O2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(8100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2508,
    label = "P-C6H4O2 + O <=> P-C6H3O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(14700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2509,
    label = "P-C6H4O2 + OH <=> P-C6H3O2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2510,
    label = "P-C6H4O2 + H <=> C5H5O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(4700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2514,
    label = "C5H6 + C2H3 <=> C6H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+67, 'cm^3/(mol*s)'),
        n = -16.08,
        Ea = (42460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2515,
    label = "C5H5 + H <=> C5H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.4e+80, 'cm^6/(mol^2*s)'),
            n = -18.28,
            Ea = (12994, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.068,
        T3 = (400.7, 'K'),
        T1 = (4136, 'K'),
        T2 = (5502, 'K'),
        efficiencies = {'[H][H]': 2, 'C': 2, '[C]=O': 1.5, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 2516,
    label = "C5H6 <=> C3H4-A + C2H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.8e+17, 's^-1'), n=0, Ea=(104000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e+98, 'cm^3/(mol*s)'),
            n = -22.25,
            Ea = (126322, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1441,
        T3 = (5.358, 'K'),
        T1 = (3284, 'K'),
        T2 = (6.71e+09, 'K'),
        efficiencies = {'[H][H]': 2, 'C': 2, '[C]=O': 1.5, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 2517,
    label = "C5H6 + H <=> C5H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(3500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2518,
    label = "C5H6 + O2 <=> C5H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(37150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2519,
    label = "C5H6 + O <=> C5H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(48000, 'cm^3/(mol*s)'), n=2.71, Ea=(1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2520,
    label = "C5H6 + OH <=> C5H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.08e+06, 'cm^3/(mol*s)'), n=2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2521,
    label = "C5H6 + HO2 <=> C5H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11000, 'cm^3/(mol*s)'), n=2.6, Ea=(12900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2522,
    label = "C5H6 + CH3 <=> C5H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.18, 'cm^3/(mol*s)'), n=4, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2523,
    label = "C5H6 + HCO <=> C5H5 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (16000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2524,
    label = "C5H6 + C2H3 <=> C5H5 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.12, 'cm^3/(mol*s)'), n=4, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2525,
    label = "C5H6 + C3H5-A <=> C5H5 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(5505, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2526,
    label = "C5H6 + C4H5-I <=> C5H5 + C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2527,
    label = "C5H6 + C4H5-N <=> C5H5 + C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2528,
    label = "C5H6 + C6H5 <=> C5H5 + C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.1, 'cm^3/(mol*s)'), n=4, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2529,
    label = "C5H6 + C6H5O <=> C5H5 + C6H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.16e+11, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2530,
    label = "C5H6 + C5H5 <=> C6H6 + C4H5-N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2531,
    label = "C5H6 + H <=> C2H2 + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.548e+37, 'cm^3/(mol*s)'),
        n = -6.18,
        Ea = (32890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2532,
    label = "C5H6 + H <=> C5H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+73, 'cm^3/(mol*s)'),
        n = -17.85,
        Ea = (31500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2533,
    label = "C5H6 + O <=> C5H5O + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (8.9e+12, 'cm^3/(mol*s)'),
                n = -0.15,
                Ea = (590, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.6e+12, 'cm^3/(mol*s)'),
                n = -0.06,
                Ea = (200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2534,
    label = "C5H81-3 + H <=> C4H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+71, 'cm^3/(mol*s)'),
        n = -16.38,
        Ea = (51000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2535,
    label = "C5H7 + O2 <=> OC5H7O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.9e+24, 'cm^3/(mol*s)'),
        n = -3.8,
        Ea = (20000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2536,
    label = "OC5H7O + O2 <=> OC4H6O + HOCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (630000, 'cm^3/(mol*s)'),
        n = -7.25,
        Ea = (33600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2537,
    label = "OC4H6O + H <=> OC4H5O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+10, 'cm^3/(mol*s)'),
        n = 1.05,
        Ea = (3279, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2538,
    label = "OC4H6O + OH <=> OC4H5O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-447, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2539,
    label = "OC4H5O + O2 <=> O2CCHOOJ + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+45, 'cm^3/(mol*s)'),
        n = -9.92,
        Ea = (20670, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2540,
    label = "O2CCHOOJ <=> HOCO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2541,
    label = "C5H7 + H <=> C5H6 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2542,
    label = "C5H7 + O <=> C5H6 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2543,
    label = "C5H7 + OH <=> C5H6 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2544,
    label = "C5H6 + HO2 <=> C5H7 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+15, 'cm^3/(mol*s)'),
        n = -1.07,
        Ea = (9530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2545,
    label = "C5H5 <=> C3H3 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.98e+68, 's^-1'), n=-15, Ea=(124900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2546,
    label = "C5H5 + HO2 <=> C5H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+29, 'cm^3/(mol*s)'),
        n = -4.69,
        Ea = (11650, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2547,
    label = "C5H5 + O2 <=> C4H4O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+18, 'cm^3/(mol*s)'),
        n = -2.48,
        Ea = (10970, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2548,
    label = "C5H5 + O <=> C4H5-N + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13, 'cm^3/(mol*s)'),
        n = -0.17,
        Ea = (440, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2549,
    label = "C5H5 + O <=> C5H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.8e+13, 'cm^3/(mol*s)'), n=-0.02, Ea=(20, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2550,
    label = "C5H5 + OH <=> C5H5OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (6.5e+14, 'cm^3/(mol*s)'),
                n = -0.85,
                Ea = (-2730, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+43, 'cm^3/(mol*s)'),
                n = -8.76,
                Ea = (18730, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+59, 'cm^3/(mol*s)'),
                n = -13.08,
                Ea = (33450, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2551,
    label = "C5H5 + OH <=> C5H4OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+57, 'cm^3/(mol*s)'),
        n = -12.18,
        Ea = (48350, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2552,
    label = "C5H5 + OH <=> C4H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2553,
    label = "C5H4OH + H <=> C5H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2554,
    label = "C5H5OH + H <=> C5H5O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(6094, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2555,
    label = "C5H5OH + O <=> C5H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(4683, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2556,
    label = "C5H5OH + OH <=> C5H5O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(1697, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2557,
    label = "C5H5OH + HO2 <=> C5H5O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2558,
    label = "C5H5OH + H <=> C5H4OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2559,
    label = "C5H5OH + O <=> C5H4OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2560,
    label = "C5H5OH + OH <=> C5H4OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1731, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2561,
    label = "C5H5OH + HO2 <=> C5H4OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3600, 'cm^3/(mol*s)'), n=2.55, Ea=(10531, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2562,
    label = "C5H5O <=> C5H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+32, 's^-1'), n=-6.5, Ea=(21220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2563,
    label = "C5H5O <=> C4H5-N + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+79, 's^-1'), n=-19.62, Ea=(66250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2564,
    label = "C5H5O + O2 <=> C5H4O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+10, 'cm^3/(mol*s)'), n=0, Ea=(1600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2565,
    label = "C5H4OH + H <=> C5H4O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(54000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2566,
    label = "C5H4OH + O2 <=> C5H4O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2567,
    label = "C5H4O <=> CO + C2H2 + C2H2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(5.7e+32, 's^-1'), n=-6.76, Ea=(68500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.2e+41, 's^-1'), n=-7.87, Ea=(98700, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2568,
    label = "C5H3O + H <=> C5H4O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2569,
    label = "C5H4O + H <=> C5H3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(8100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2570,
    label = "C5H4O + O <=> C5H3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(1470, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2571,
    label = "C5H4O + OH <=> C5H3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+08, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (1450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2572,
    label = "C5H3O => C2H2 + CO + C2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 's^-1'), n=0, Ea=(51000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2573,
    label = "C5H3O + O2 => CO2 + C2H2 + HCCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (9.7e+58, 'cm^3/(mol*s)'),
        n = -13.47,
        Ea = (38180, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2574,
    label = "C5H4O + H <=> C4H5-N + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+61, 'cm^3/(mol*s)'),
        n = -13.27,
        Ea = (40810, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2575,
    label = "C5H4O + O <=> C4H4 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2576,
    label = "C4H4O + H <=> C3H5-A + CO",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (6.6e+13, 'cm^3/(mol*s)'),
                n = -0.02,
                Ea = (2740, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(5.9e+06, 'cm^3/(mol*s)'), n=2, Ea=(1300, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2577,
    label = "C4H4O + O <=> CH2CHO + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+08, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2578,
    label = "C4H4O + OH <=> C3H5-A + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2579,
    label = "C4H4O + OH => C2H2 + HCCO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(5933, 'cal/mol'), T0=(1, 'K')),
)

