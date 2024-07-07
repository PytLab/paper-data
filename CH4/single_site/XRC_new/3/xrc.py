#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scaks.models.micro_kinetic_model import MicroKineticModel
from kfs import kfs

#k = 0.12596991277617356
r = 7.14158769093562e-06
r_prime = 6.718109385730481e-06

def XRC(model, idx):
    kfs_prime, _ = model.solver.get_rate_constants()
    k_prime = kfs_prime[idx]
    k = kfs[idx]
    dr = r_prime - r
    dk = float(k_prime - k)
    print('k_prime: {}'.format(k_prime))

    return k/r*(dr/dk)

model = MicroKineticModel(setup_file="ch4.model")
parser = model.parser
parser.parse_data("rel_energy.py")

xrc = XRC(model, 2)
print("xrc: {}".format(xrc))

