# KMC processes.
processes = [

    # CH4 adsorption
    {
        "reaction": 'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a',
        "coordinates_group": [
            [[0.0, 0.0, 0.0],
             [0.8, 0.5, 0.0],
             [0.4, 0.5, 0.0],
             [0.0, 0.5, 0.0]],
        ],
        "elements_before": ['*', '*_a', '*_c', '*_b'],
        "elements_after": ['*', 'H_a', 'CH3_c', '*_b'],
        "basis_sites": [0],
    },
    # CH3 transfer
    {
        "reaction": 'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'CH3_c', '*_b'],
        "elements_after": ['*', '*_c', 'CH3_b'],
        "basis_sites": [0],
    },
    # O2 adsorption
    {
        "reaction": 'O2_g + *_c + CH3_b -> O2_c + CH3_b',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', '*_c', 'CH3_b'],
        "elements_after": ['*', 'O2_c', 'CH3_b'],
        "basis_sites": [0],
    },
    # 4  
    {
        "reaction": 'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'O2_c', 'CH3_b'],
        "elements_after": ['*', 'OOH_c', 'CH2_b'],
        "basis_sites": [0],
    },
    # 5
    {
        "reaction": 'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.8, 0.5, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'H_a', 'OOH_c', 'CH2_b'],
        "elements_after": ['*', '*_a', '-OCH2_c', '-OCH2_b'],
        "basis_sites": [0],
    },
    # 6
    {
        "reaction": 'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', '-OCH2_c', '-OCH2_b'],
        "elements_after": ['*', 'OCH2_c', '*_b'],
        "basis_sites": [0],
    },
    # 7
    {
        "reaction": 'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.8, 0.5, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', '*_a', 'OCH2_c', '*_b'],
        "elements_after": ['*', 'H_a', '*_c', 'CHO_b'],
        "basis_sites": [0],
    },
    # 8
    {
        "reaction": 'O2_g + CHO_b + *_c -> O2_c + CHO_b',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', '*_c', 'CHO_b'],
        "elements_after": ['*', 'O2_c', 'CHO_b'],
        "basis_sites": [0],
    },
    # 9
    {
        "reaction": 'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'O2_c', 'CHO_b'],
        "elements_after": ['*', 'OOH_c', '*_v'],
        "basis_sites": [0],
    },
    # 10 H2O desorption
    {
        "reaction": 'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v',
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [0.8, 0.5, 0.0],
            [0.4, 0.5, 0.0],
            [0.0, 0.5, 0.0]]
        ],
        "elements_before": ['*', 'H_a', 'OOH_c', '*_v'],
        "elements_after": ['*', '*_a', '*_c', '*_b'],
        "basis_sites": [0],
    },
]
