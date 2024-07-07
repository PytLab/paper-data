#!/usr/bin/env python
rxn_expressions = [
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a',
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c',
    'O2_g + *_c + CH3_b -> O2_c + CH3_b',
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b',
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c',
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c',
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a',
    'O2_g + CHO_b + *_c -> O2_c + CHO_b',
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v',
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v',
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
temperature = 732.15  # K

# Lattice information.
surface_name = 'Co3O4-110'

# Unitcell.
cell_vectors = [[1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]]

basis_sites = [[0.0, 0.0, 0.0], # O_l
               [0.4, 0.0, 0.0], # Co
               [0.8, 0.0, 0.0],
               [0.0, 0.5, 0.0], # O3c
               [0.4, 0.5, 0.0], # Co
               [0.8, 0.5, 0.0]] # O2c

# Supercell.
repetitions = (30, 30, 1)   # (x, y, z)
periodic = (True, True, False)           # periodic boundary condition
possible_element_types = ['*_c', '*_a', '*_b', '*_v', 'H_a', 'CH3_c', 'CH3_b',
                          'O2_c', 'OOH_c', 'CH2_b', '-OCH2_c', '-OCH2_b', 'OCH2_c',
                          'CHO_b']
empty_type = "*_a"
possible_site_types = ["P"]


# KMC model attributes.
# specify tools for model to use
parser = 'KMCParser'  # default
solver = 'KMCSolver'
corrector = "ThermodynamicCorrector"
rate_algo = 'TST'

# KMC loop control parameters.
nstep = 10**6                           # number of KMC loop step
seed = 13996                         # seed for random number generator
random_generator = 'MT'              # 'MT' | 'MINSTD' | 'RANLUX24' | 'RANLUX48'
analysis = ['TOFAnalysis', 'FrequencyAnalysis', 'CoveragesAnalysis']     # ['CoveragesAnalysis', 'FrequencyAnalysis']
analysis_interval = [1, 1, nstep//1000]
coverage_ratios = [1/6.]*6
trajectory_dump_interval = nstep//200

