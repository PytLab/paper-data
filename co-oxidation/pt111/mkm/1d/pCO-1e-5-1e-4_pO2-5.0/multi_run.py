#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

import numpy as np

from kynetix.models.micro_kinetic_model import MicroKineticModel
from kynetix.compatutil import subprocess

setup_dict = dict(
    rxn_expressions = [
        'CO_g + *_s <-> C-O_s -> CO_s',
        'O2_g + 2*_s -> 2O_s',
        'CO_s + O_s <-> CO-O_2s -> CO2_g + 2*_s',
    ],

    species_definitions = {
        'CO_g': {'pressure': 0.10},
        'O2_g': {'pressure': 5.0},
        'CO2_g': {'pressure': 0.0},
        '*_s': {'site_name': 'top', 'type': 'site', 'total': 1.0},
    },

    temperature = 500,

    unitcell_area = 9.0e-20,
    active_ratio = 4./9.,

    parser = "RelativeEnergyParser",
    solver = "SteadyStateSolver",
    corrector = "ThermodynamicCorrector",
    plotter = "EnergyProfilePlotter",

    rate_algo = "TST",
    rootfinding = "MDNewton",
    tolerance = 1e-15,
    max_rootfinding_iterations = 100,
)

pCOs = np.linspace(1e-5, 1e-4, 20)

if "__main__" == __name__:
    # Clean up current dir.
    subprocess.getstatusoutput("rm -rf out.log auto_*")

    ss_cvgs = []
    tofs = []
    for i, pCO in enumerate(pCOs):
        # Construct setup dict.
        setup_dict['species_definitions']['CO_g']['pressure'] = pCO

        # Construct model.
        model = MicroKineticModel(setup_dict=setup_dict, console_handler_level=logging.WARNING)

        # Read data.
        model.parser.parse_data()
        model.solver.get_data()

        # Initial coverage guess.
#        if i == 0:
#            trajectory = model.solver.solve_ode(time_span=0.0001,
#                                                time_end=10,
#                                                traj_output=False)
#            init_guess = trajectory[-1]
#        else:
#            init_guess = ss_cvgs[-1]

        trajectory = model.solver.solve_ode(time_span=0.0001,
                                            time_end=10,
                                            traj_output=False)
        init_guess = trajectory[-1]

        # Run.
        print("Running pressure CO_g: {}".format(pCO))
        model.run(init_cvgs=init_guess,
                  XRC=False,
                  product_name="CO2_g")
        model.clear_handlers()

        # Collect TOF.
        tof_idx = model.gas_names.index("CO2_g")
        tofs.append(float(model.TOFs[tof_idx]))

        # Collect steady state coverages.
        cvgs = [float(cvg) for cvg in model.steady_state_coverages]
        ss_cvgs.append(cvgs)

    # Write tofs to file.
    tof_str = "tofs = {}\n".format(tofs)
    p_str = "pCO = {}\n".format(pCOs.tolist())
    with open("auto_tofs.py", "w") as f:
        f.write(tof_str + p_str)

    cvgs_str = "cvgs = {}\n".format(ss_cvgs)
    adsorbates_str = "adsorbates = {}\n".format(model.adsorbate_names)
    with open("auto_cvgs.py", "w") as f:
        f.write(cvgs_str + adsorbates_str + p_str)

