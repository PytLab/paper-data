#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

import numpy as np

from kynetix.models.micro_kinetic_model import MicroKineticModel
from kynetix.compatutil import subprocess

setup_dict = dict(
    rxn_expressions = [
        'CO_g + *_t -> CO_t',
        'O2_g + 2*_t -> 2O_t',
        'CO_t + O_t <-> CO-O_2t -> CO2_g + 2*_t',
    ],

    # Gas pressure.
    species_definitions = {
        'CO_g': {'pressure': 0.1},
        'O2_g': {'pressure': 0.5},
        'CO2_g': {'pressure': 1.32*10**-7},
        '*_t': {'site_name': 'top', 'type': 'site', 'total': 1.0},
    },

    # Site info.

    # Temperature.
    temperature = 500,  # K

    unitcell_area = 9.0e-20,
    active_ratio = 4./9.,

    parser = "RelativeEnergyParser",
    solver = "SteadyStateSolver",
    corrector = "ThermodynamicCorrector",
    plotter = "EnergyProfilePlotter",

    rate_algo = "CT",
    rootfinding = "MDNewton",
    tolerance = 1e-50,
    max_rootfinding_iterations = 100,
)

pO2s = np.linspace(1e-7, 0.5, 20)

if "__main__" == __name__:
    # Clean up current dir.
    subprocess.getstatusoutput("rm -rf out.log auto_*")

    ss_cvgs = []
    tofs = []
    for i, pO2 in enumerate(pO2s):
        # Construct setup dict.
        setup_dict['species_definitions']['O2_g']['pressure'] = pO2

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
        print("Running pressure O2_g: {}".format(pO2))
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
    p_str = "pO2 = {}\n".format(pO2s.tolist())
    with open("auto_tofs.py", "w") as f:
        f.write(tof_str + p_str)

    cvgs_str = "cvgs = {}\n".format(ss_cvgs)
    adsorbates_str = "adsorbates = {}\n".format(model.adsorbate_names)
    with open("auto_cvgs.py", "w") as f:
        f.write(cvgs_str + adsorbates_str + p_str)

