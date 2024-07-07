"""
Script to run kynetix kMC simulation.
"""

import logging
import time

from scaks.mpicommons import mpi
from scaks.compatutil import subprocess
from scaks.models.micro_kinetic_model import MicroKineticModel
from scaks.utilities.format_utilities import convert_time

if "__main__" == __name__:
    # Remove old log file.
    subprocess.getstatusoutput("rm -rm out.log auto_*")

    # Set logger.
    logger = logging.getLogger("model.KMCModelRun")

    # Construct KMC model.
    model = MicroKineticModel(setup_file="ch4.model")
    parser = model.parser
    parser.parse_data()

#    start = time.time()
#    try:
#        model.run()
#    except Exception as e:
#        # Log exception info.
#        if mpi.is_master:
#            msg = "{} exception is catched.".format(type(e).__name__)
#            logger.exception(msg)
#        raise e
#
#    end = time.time()
#    t = end - start
#    h, m, s = convert_time(t)
#
#    if mpi.is_master:
#        logger.info("Time used: {:d} h {:d} min {:f} sec".format(h, m, s))

