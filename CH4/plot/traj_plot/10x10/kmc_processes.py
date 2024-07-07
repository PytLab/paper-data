# KMC processes.
processes = [

    # CH4 adsorption
    {
        "reaction": 'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o',
        "coordinates_group": [
            [[0.0, 0.0, 0.0],
             [0.4, 0.5, 0.0]]
        ],
        "elements_before": ['*_o', '*_c'],
        "elements_after": ['H_o', 'CH3_c'],
        "basis_sites": [0],
    },
    # 1st C-O coupling
    {
        "reaction": 'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.8, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'CH3_c', '*_o'],
        "elements_after": ['*', '*_c', 'CH3_o'],
        "basis_sites": [0],
    },
    # 2nd C-H activation & 2nd C-O coupling
    {
        "reaction": 'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.8, 0.5, 0.0],
            [0.0, 1.0, 0.0]]
        ],
        "elements_before": ['*_o', 'CH3_o', '*_o'],
        "elements_after": ['H_o', '-CH2_o', '-CH2_o'],
        "basis_sites": [0],
    },
    # O2 adsorption
    {
        "reaction": 'O2_g + CH2_2o + *_c -> O2_c + CH2_2o',
        "coordinates_group": [
            [[0.0, 0.0, 0.0],
             [0.4, 0.5, 0.0],
             [0.8, 0.5, 0.0],
             [0.0, 1.0, 0.0]],
        ],
        "elements_before": ['*', '*_c', '-CH2_o', '-CH2_o'],
        "elements_after": ['*', 'O2_c', '-CH2_o', '-CH2_o'],
        "basis_sites": [0],
    },
    # 3nd C-H activation & reconstruction
    {
        "reaction": 'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.8, 0.5, 0.0],
            [0.0, 1.0, 0.0]]
        ],
        "elements_before": ['*', 'O2_c', '-CH2_o', '-CH2_o'],
        "elements_after": ['*', 'OH_c', '*_o', 'CHO_o'],
        "basis_sites": [0],
    },
    # O2 adsorption besides CHO_o
    {
        "reaction": 'O2_g + CHO_o + *_c -> O2_c + CHO_o',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.4, 1.0, 0.0]]
        ],
        "elements_before": ['*', 'CHO_o', '*_c'],
        "elements_after": ['*', 'CHO_o', 'O2_c'],
        "basis_sites": [0],
    },
    # 4th C-H activation path 1
    {
        "reaction": 'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.4, 1.0, 0.0]]
        ],
        "elements_before": ['*', 'CHO_o', 'O2_c'],
        "elements_after": ['*', '*_v', 'OOH_c'],
        "basis_sites": [0],
    },
    # 4th C-H activation path 2
    {
        "reaction": 'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.4, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'CHO_o', 'OH_c'],
        "elements_after": ['*', '*_v', '*_c'],
        "basis_sites": [0],
    },
    # 4th C-H activation path 3
    {
        "reaction": 'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.8, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'CHO_o', '*_o'],
        "elements_after": ['*', '*_v', 'H_o'],
        "basis_sites": [0],
    },
    # O2 adsorption & dissociation
    {
        "reaction": 'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 1.0, 0.0]]
        ],
        "elements_before": ['*', '*_c', '*_v'],
        "elements_after": ['*', 'O_c', '*_o'],
        "basis_sites": [0],
    },
    # H transfer b/w O2c
    {
        "reaction": 'H_a + *_a <-> H-_a + *_a -> *_a + H_a',
        "coordinates_group": [
           [[0.0, 0.0, 0.0],
            [0.8, 0.5, 0.0]],
           [[0.0, 0.0, 0.0],
            [0.8, -0.5, 0.0]],
        ],
        "elements_before": ['H_o', '*_o'],
        "elements_after": ['*_o', 'H_o'],
        "basis_sites": [0],
        "fast": True
    },
    # H transfer b/w O3c
    {
        "reaction": 'H_b + *_b <-> H-_b + *_b -> *_b + H_b',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.0, 0.5, 0.0],
            [0.0, 1.5, 0.0]]
        ],
        "elements_before": ['*', 'H_o', '*_o'],
        "elements_after": ['*', '*_o', 'H_o'],
        "basis_sites": [0],
        "fast": True
    },
    # H -> O* from O2c
    {
        "reaction": 'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.8, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'O_c', 'H_o'],
        "elements_after": ['*', 'OH_c', '*_o'],
        "basis_sites": [0],
    },
    # H -> O* from O3c
    {
        "reaction": 'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'O_c', 'H_o'],
        "elements_after": ['*', 'OH_c', '*_o'],
        "basis_sites": [0],
    },
    # H -> OH* from O2c
    {
        "reaction": 'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.8, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'OH_c', 'H_o'],
        "elements_after": ['*', '*_c', '*_o'],
        "basis_sites": [0],
    },
    # H -> OH* from O3c
    {
        "reaction": 'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'OH_c', 'H_o'],
        "elements_after": ['*', '*_c', '*_o'],
        "basis_sites": [0],
    },

    # Redist
    # H -> O2c
    {
        "reaction": 'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o',
        "coordinates_group": [
           [[0.0, 0.0, 0.0]],
           [[0.8, 0.5, 0.0]]
        ],
        "elements_before": ['*_o'],
        "elements_after": ['H_o'],
        "basis_sites": [0],
        "fast": True,
        "redist": True,
        "redist_species": "H_o"
    },
]

