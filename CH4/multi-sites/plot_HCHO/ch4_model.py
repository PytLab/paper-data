#!/usr/bin/env python
rxn_expressions = [
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o',  # 1st C-H activation
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c',      # 1st C-O coupling
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o',     # 2nd C-H activation & 2nd C-O coupling
    'CH3_o + *_o <-> CH2-H_o + *_o -> CH2_o + H_o',
    'CH2O_o -> CH2O_g + *_o',
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o',                                  # O2 adsorption besides CH2_2o
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o', #CH_2o + OOH_c',  # 3nd C-H activation & reconst
    'O2_g + CHO_o + *_c -> O2_c + CHO_o', # O2 adsorption besides CHO_o
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o', # 4th C-H activation path 1
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o', #4th C-H activation path 2
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o', # 4th C-H activation path 3
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c', # O2 adsorption and dissociation
#    'H_a + *_a <-> H-_a + *_a -> *_a + H_a',   # H transfer b/w O2c
#    'H_b + *_b <-> H-_b + *_b -> *_b + H_b',   # H transfer b/w O3c
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a', # H -> O* from O2c
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b', # H -> O* from O3c
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a', # H -> OH* from O2c
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b', # H -> OH* from O3c
]

# Gas pressure.
species_definitions = {}
species_definitions['CH4_g'] = {'pressure': 0.01}
species_definitions['O2_g'] = {'pressure': 0.2}
species_definitions['CO2_g'] = {'pressure': 0.01}
species_definitions['H2O_g'] = {'pressure': 0.02}

# Site info.
species_definitions['f'] = {'site_name': 'fcc', 'type': 'site'}
species_definitions['h'] = {'site_name': 'hcp', 'type': 'site'}

# Temperature.
temperature = 723.15  # K

# Lattice information.
surface_name = 'Co3O4-110'

# Unitcell.
cell_vectors = [[1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]]

basis_sites = [[0.0, 0.0, 0.0], # O_l
               [0.4, 0.0, 0.0], # Co
               [0.8, 0.0, 0.0], # O_l
               [0.0, 0.5, 0.0], # O_l
               [0.4, 0.5, 0.0], # Co
               [0.8, 0.5, 0.0]] # O_l

# Supercell.
repetitions = (30, 30, 1)   # (x, y, z)
periodic = (True, True, False)           # periodic boundary condition
possible_element_types = ['*_c', '*_o', 'H_o', 'CH3_c', 'CH3_o', '-CH2_o',
                          'O2_c', 'OH_c', 'CHO_o', 'OOH_c', '*_v', 'O_c']
empty_type = "*_o"
possible_site_types = ["P"]


# KMC model attributes.
# specify tools for model to use
parser = 'KMCParser'  # default
solver = 'KMCSolver'
corrector = "ThermodynamicCorrector"
rate_algo = 'TST'

# KMC loop control parameters.
nstep = 10**7                           # number of KMC loop step
#time_limit = 1e2
seed = 13996                         # seed for random number generator
random_generator = 'MT'              # 'MT' | 'MINSTD' | 'RANLUX24' | 'RANLUX48'
analysis = ['FrequencyAnalysis', "TOFAnalysis", "CoveragesAnalysis"]     # ['CoveragesAnalysis', 'FrequencyAnalysis']
analysis_interval = [1, 1, nstep//1000]
coverage_ratios = [1/6.]*6
trajectory_dump_interval = nstep//200

# Redistribution
do_redistribution = True
redistribution_interval = 300
distributor_type = 'ProcessRandomDistributor'

