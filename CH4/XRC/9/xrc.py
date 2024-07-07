#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scaks.models.micro_kinetic_model import MicroKineticModel

k = 0.12596991277617356
r = 0.00022059448342651614
r_prime = 0.0001242531914480282

def XRC(model, idx):
    kfs, _ = model.solver.get_rate_constants()
    k_prime = float(kfs[idx])
    dr = r_prime - r
    dk = k_prime - k
    print('k_prime: {}'.format(k_prime))

    return k/r*(dr/dk)

model = MicroKineticModel(setup_file="ch4.model")
parser = model.parser
parser.parse_data("rel_energy.py")

xrc = XRC(model, 7)
print("xrc: {}".format(xrc))

