# KMC processes.
processes = [

    # CO adsorbed on hcp site.
    {
        "reaction": "CO_g + *_h -> CO_h",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0., 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0., 0.5, 0.0],
            [-1/3., 2/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "basis_sites": [0],
    },

    # CO adsorbed on fcc site.
    {
        "reaction": "CO_g + *_f -> CO_f",
        "coordinates_group": [[
            [0., 0., 0.],
            [-1/3., 2/3., 0.0],
            [0., 1.0, 0.],
            [2/3., 2/3., 0.0],
            [1.0, 0., 0.],
            [2/3., -1/3., 0.0],
            [0., 0.5, 0.0],
            [0.5, 0.5, 0.0],
            [0.5, 0., 0.0],
            [1/3., 1/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "basis_sites": [0],
    },

    # 'O2_g + 2*_f <-> O-O_2f -> 2O_f'
    {
        "reaction": "O2_g + 2*_f <-> O-O_2f -> 2O_f",
        "coordinates_group": [[
            [0., 0., 0.],
            [-1/3., 2/3., 0.0],
            [0., 1.0, 0.0],
            [2/3., 2/3., 0.0],
            [1.0, 0., 0.0],
            [2/3., -1/3., 0.0],
            [0., 0.5, 0.0],
            [0.5, 0.5, 0.0],
            [0.5, 0., 0.],
            [1/3., 1/3., 0.0],
            [1.0, 1.0, 0.0],
            [5/3., 2/3., 0.0],
            [2.0, 0.0, 0.0],
            [5/3., -1/3., 0.0],
            [1.0, 0.5, 0.0],
            [1.5, 0.5, 0.0],
            [1.5, 0.0, 0.0],
            [4/3., 1/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "basis_sites": [0],
    },
    {
        "reaction": "O2_g + 2*_f <-> O-O_2f -> 2O_f",
        "coordinates_group": [[
            [0., 0., 0.],
            [-1/3., 2/3., 0.0],
            [0., 1.0, 0.],
            [2/3., 2/3., 0.0],
            [1.0, 0., 0.],
            [2/3., -1/3., 0.0],
            [0., 0.5, 0.],
            [0.5, 0.5, 0.0],
            [0.5, 0., 0.],
            [1/3., 1/3., 0.0],
            [-1/3., 5/3., 0.0],
            [0.0, 2.0, 0.0],
            [2/3., 5/3., 0.0],
            [1.0, 1.0, 0.0],
            [0.0, 1.5, 0.0],
            [0.5, 1.5, 0.0],
            [0.5, 1.0, 0.0],
            [1/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "basis_sites": [0],
    },
    {
        "reaction": "O2_g + 2*_f <-> O-O_2f -> 2O_f",
        "coordinates_group": [[
             [0.0, 0.0, 0.0],
             [-1/3., 2/3., 0.0],
             [0.0, 1.0, 0.0],
             [2/3., 2/3., 0.0],
             [1.0, 0.0, 0.0],
             [2/3., -1/3., 0.0],
             [0.0, 0.5, 0.0],
             [0.5, 0.5, 0.0],
             [0.5, 0.0, 0.0],
             [1/3., 1/3., 0.0],
             [-1.0, 1.0, 0.0],
             [-4/3., 5/3., 0.0],
             [-1.0, 2.0, 0.0],
             [-1/3., 5/3., 0.0],
             [-1.0, 1.5, 0.0],
             [-0.5, 1.5, 0.0],
             [-0.5, 1.0, 0.0],
             [-2/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "basis_sites": [0],
    },

    # O2_g + 2*_h <-> O-O_2h -> 2O_h
    {
        "reaction": "O2_g + 2*_h <-> O-O_2h -> 2O_h",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [1.0, 0.0, 0.0],
            [1/3., 4/3., 0.0],
            [1.0, 1.0, 0.0],
            [4/3., 1/3., 0.0],
            [0.5, 0.5, 0.0],
            [0.5, 1.0, 0.0],
            [1.0, 0.5, 0.0],
            [2/3., 2/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "basis_sites": [0],
    },
    {
        "reaction": "O2_g + 2*_h <-> O-O_2h -> 2O_h",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [-1.0, 2.0, 0.0],
            [-2/3., 7/3., 0.0],
            [0.0, 2.0, 0.0],
            [1/3., 4/3., 0.0],
            [-0.5, 1.5, 0.0],
            [-0.5, 2.0, 0.0],
            [0.0, 1.5, 0.0],
            [-1/3., 5/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "basis_sites": [0],
    },
    {
        "reaction": "O2_g + 2*_h <-> O-O_2h -> 2O_h",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [-5/3., 4/3., 0.0],
            [-2.0, 2.0, 0.0],
            [-5/3., 7/3., 0.0],
            [-1.0, 2.0, 0.0],
            [-1.5, 1.5, 0.0],
            [-1.5, 2.0, 0.0],
            [-1.0, 1.5, 0.0],
            [-4/3., 5/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "basis_sites": [0],
    },

    # O_h + CO_f <-> O-CO_f + *_h -> CO2_g + *_h + *_f
    {
        "reaction": "O_h + CO_f <-> O-CO_f + *_h -> CO2_g + *_h + *_f",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [-1/3., 5/3., 0.0],
            [0.0, 2.0, 0.0],
            [2/3., 5/3., 0.0],
            [1.0, 1.0, 0.0],
            [2/3., 2/3., 0.0],
            [0.0, 1.5, 0.0],
            [0.5, 1.5, 0.0],
            [0.5, 1.0, 0.0],
            [1/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
    },
    {
        "reaction": "O_h + CO_f <-> O-CO_f + *_h -> CO2_g + *_h + *_f",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [0.0, -1.0, 0.0],
            [-1/3., -1/3., 0.0],
            [2/3., -1/3., 0.0],
            [1.0, -1.0, 0.0],
            [2/3., -4/3., 0.0],
            [0.0, -0.5, 0.0],
            [0.5, -0.5, 0.0],
            [0.5, -1.0, 0.0],
            [1/3., -2/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
    },
    {
        "reaction": "O_h + CO_f <-> O-CO_f + *_h -> CO2_g + *_h + *_f",
        "coordinates_group": [[
             [0.0, 0.0, 0.0],
             [-2/3., 1/3., 0.0],
             [-1.0, 1.0, 0.0],
             [-2/3., 4/3., 0.0],
             [0.0, 1.0, 0.0],
             [1/3., 1/3., 0.0],
             [-0.5, 0.5, 0.0],
             [-0.5, 1.0, 0.0],
             [0.0, 0.5, 0.0],
             [-1/3., 2/3., 0.0],
             [-2.0, 1.0, 0.0],
             [-7/3., 5/3., 0.0],
             [-2.0, 2.0, 0.0],
             [-4/3., 5/3., 0.0],
             [-4/3., 2/3., 0.0],
             [-2.0, 1.5, 0.0],
             [-1.5, 1.5, 0.0],
             [-1.5, 1.0, 0.0],
             [-5/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
    },

    # O_f + CO_h <-> O-CO_h + *_f -> CO2_g + *_h + *_f
    {
        "reaction": "O_f + CO_h <-> O-CO_h + *_f -> CO2_g + *_h + *_f",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [-1/3., 5/3., 0.0],
            [0.0, 2.0, 0.0],
            [2/3., 5/3., 0.0],
            [1.0, 1.0, 0.0],
            [2/3., 2/3., 0.0],
            [0.0, 1.5, 0.0],
            [0.5, 1.5, 0.0],
            [0.5, 1.0, 0.0],
            [1/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
    },
    {
        "reaction": "O_f + CO_h <-> O-CO_h + *_f -> CO2_g + *_h + *_f",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [0.0, -1.0, 0.0],
            [-1/3., -1/3., 0.0],
            [2/3., -1/3., 0.0],
            [1.0, -1.0, 0.0],
            [2/3., -4/3., 0.0],
            [0.0, -0.5, 0.0],
            [0.5, -0.5, 0.0],
            [0.5, -1.0, 0.0],
            [1/3., -2/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
    },
    {
        "reaction": "O_f + CO_h <-> O-CO_h + *_f -> CO2_g + *_h + *_f",
        "coordinates_group": [[
             [0.0, 0.0, 0.0],
             [-2/3., 1/3., 0.0],
             [-1.0, 1.0, 0.0],
             [-2/3., 4/3., 0.0],
             [0.0, 1.0, 0.0],
             [1/3., 1/3., 0.0],
             [-0.5, 0.5, 0.0],
             [-0.5, 1.0, 0.0],
             [0.0, 0.5, 0.0],
             [-1/3., 2/3., 0.0],
             [-2.0, 1.0, 0.0],
             [-7/3., 5/3., 0.0],
             [-2.0, 2.0, 0.0],
             [-4/3., 5/3., 0.0],
             [-4/3., 2/3., 0.0],
             [-2.0, 1.5, 0.0],
             [-1.5, 1.5, 0.0],
             [-1.5, 1.0, 0.0],
             [-5/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
    },

    # O_f + *_h -> O_h + *_f
    {
        "reaction": "O_f + *_h -> O_h + *_f",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [-1/3., 5/3., 0.0],
            [0.0, 2.0, 0.0],
            [2/3., 5/3., 0.0],
            [1.0, 1.0, 0.0],
            [2/3., 2/3., 0.0],
            [0.0, 1.5, 0.0],
            [0.5, 1.5, 0.0],
            [0.5, 1.0, 0.0],
            [1/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
    },
    {
        "reaction": "O_f + *_h -> O_h + *_f",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [0.0, -1.0, 0.0],
            [-1/3., -1/3., 0.0],
            [2/3., -1/3., 0.0],
            [1.0, -1.0, 0.0],
            [2/3., -4/3., 0.0],
            [0.0, -0.5, 0.0],
            [0.5, -0.5, 0.0],
            [0.5, -1.0, 0.0],
            [1/3., -2/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
    },
    {
        "reaction": "O_f + *_h -> O_h + *_f",
        "coordinates_group": [[
             [0.0, 0.0, 0.0],
             [-2/3., 1/3., 0.0],
             [-1.0, 1.0, 0.0],
             [-2/3., 4/3., 0.0],
             [0.0, 1.0, 0.0],
             [1/3., 1/3., 0.0],
             [-0.5, 0.5, 0.0],
             [-0.5, 1.0, 0.0],
             [0.0, 0.5, 0.0],
             [-1/3., 2/3., 0.0],
             [-2.0, 1.0, 0.0],
             [-7/3., 5/3., 0.0],
             [-2.0, 2.0, 0.0],
             [-4/3., 5/3., 0.0],
             [-4/3., 2/3., 0.0],
             [-2.0, 1.5, 0.0],
             [-1.5, 1.5, 0.0],
             [-1.5, 1.0, 0.0],
             [-5/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'O', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
    },

    # CO_f + *_h -> CO_h + *_f
    {
        "reaction": "CO_f + *_h -> CO_h + *_f",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [-1/3., 5/3., 0.0],
            [0.0, 2.0, 0.0],
            [2/3., 5/3., 0.0],
            [1.0, 1.0, 0.0],
            [2/3., 2/3., 0.0],
            [0.0, 1.5, 0.0],
            [0.5, 1.5, 0.0],
            [0.5, 1.0, 0.0],
            [1/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
        "fast": True,
    },
    {
        "reaction": "CO_f + *_h -> CO_h + *_f",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0.0, 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0.0, 0.5, 0.0],
            [-1/3., 2/3., 0.0],
            [0.0, -1.0, 0.0],
            [-1/3., -1/3., 0.0],
            [2/3., -1/3., 0.0],
            [1.0, -1.0, 0.0],
            [2/3., -4/3., 0.0],
            [0.0, -0.5, 0.0],
            [0.5, -0.5, 0.0],
            [0.5, -1.0, 0.0],
            [1/3., -2/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
        "fast": True,
    },
    {
        "reaction": "CO_f + *_h -> CO_h + *_f",
        "coordinates_group": [[
             [0.0, 0.0, 0.0],
             [-2/3., 1/3., 0.0],
             [-1.0, 1.0, 0.0],
             [-2/3., 4/3., 0.0],
             [0.0, 1.0, 0.0],
             [1/3., 1/3., 0.0],
             [-0.5, 0.5, 0.0],
             [-0.5, 1.0, 0.0],
             [0.0, 0.5, 0.0],
             [-1/3., 2/3., 0.0],
             [-2.0, 1.0, 0.0],
             [-7/3., 5/3., 0.0],
             [-2.0, 2.0, 0.0],
             [-4/3., 5/3., 0.0],
             [-4/3., 2/3., 0.0],
             [-2.0, 1.5, 0.0],
             [-1.5, 1.5, 0.0],
             [-1.5, 1.0, 0.0],
             [-5/3., 4/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "basis_sites": [0],
        "fast": True,
    },

    # Redist
    {
        "reaction": "CO_g + *_h -> CO_h",
        "coordinates_group": [[
            [0.0, 0.0, 0.0],
            [-2/3., 1/3., 0.0],
            [-1.0, 1.0, 0.0],
            [-2/3., 4/3., 0.0],
            [0., 1.0, 0.0],
            [1/3., 1/3., 0.0],
            [-0.5, 0.5, 0.0],
            [-0.5, 1.0, 0.0],
            [0., 0.5, 0.0],
            [-1/3., 2/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "basis_sites": [0],
        "fast": True,
        "redist": True,
        "redist_species": "C"
    },

    # CO adsorbed on fcc site.
    {
        "reaction": "CO_g + *_f -> CO_f",
        "coordinates_group": [[
            [0., 0., 0.],
            [-1/3., 2/3., 0.0],
            [0., 1.0, 0.],
            [2/3., 2/3., 0.0],
            [1.0, 0., 0.],
            [2/3., -1/3., 0.0],
            [0., 0.5, 0.0],
            [0.5, 0.5, 0.0],
            [0.5, 0., 0.0],
            [1/3., 1/3., 0.0]
        ]],
        "elements_before": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
        "elements_after": ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'C'],
        "basis_sites": [0],
        "fast": True,
        "redist": True,
        "redist_species": "C"
    },
]