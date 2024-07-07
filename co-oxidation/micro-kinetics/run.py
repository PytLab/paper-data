"""
Script for running Micro-kinetic Model simulation.
"""

import logging
import sys
import time

from kynetix.compatutil import subprocess
from kynetix.mpicommons import mpi
from kynetix.models.micro_kinetic_model import MicroKineticModel
from kynetix.utilities.format_utilities import convert_time

# Custom parameters.
OdeInterval = 0.002          # ODE integration time interval.
OdeEnd = 0.1          # ODE integration time limit.
OdeOutput = True           # Output ODE integration data or not.
CalcXRC = False             # Calculate Degree of Rate Control(XRC) or not.
ProductionName = "CO2_g"  # Production name of your model.
OdeOnly = False             # Do ODE integration only.

if "__main__" == __name__:
    # Clean up current dir.
    subprocess.getstatusoutput("rm -rf out.log auto_*")

    # Set script logger.
    logger = logging.getLogger("model.MkmRunScript")

    # Get setup file.
    status, output= subprocess.getstatusoutput("ls *.mkm | tail -1")
    if status:
        if mpi.is_master:
            logger.error(output)
            logger.info("Exiting...")
        sys.exit(1)

    start = time.time()
    try:
        # Build micor-kinetic model.
        model = MicroKineticModel(setup_file=output)

        # Read data.
        parser = model.parser
        solver = model.solver
        parser.parse_data()
        solver.get_data()

        # Initial coverages guess.
        trajectory = solver.solve_ode(initial_cvgs=(0.0, 0.0),
                                      time_span=OdeInterval,
                                      time_end=OdeEnd,
                                      traj_output=OdeOutput)
        init_guess = trajectory[-1]

        # Run.
        model.run(init_cvgs=init_guess,
                  solve_ode=OdeOnly,
                  coarse_guess=False,
                  XRC=CalcXRC,
                  product_name=ProductionName)
    except Exception as e:
        if mpi.is_master:
            msg = "{} exception is catched.".format(type(e).__name__)
            logger.exception(msg)
        raise e

    # Time used.
    end = time.time()
    t = end - start
    h, m, s = convert_time(t)

    if mpi.is_master:
        logger.info("Time used: {:d} h {:d} min {:f} sec".format(h, m, s))

