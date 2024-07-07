"""
Script to run kynetix kMC simulation.
"""

from scaks.models.micro_kinetic_model import MicroKineticModel

model = MicroKineticModel(setup_file="ch4.model")
parser = model.parser
parser.parse_data("rel_energy.py")


kfs, _ = model.solver.get_rate_constants()

