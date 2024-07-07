#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scaks.models.micro_kinetic_model import MicroKineticModel
from kfs import kfs

#k = 0.12596991277617356
r = 0.004785821801951488
r_prime = 0.0045670329327908024
r_by = 0.0007875402965236626
r_prime_by = 0.0005298767491083252

def XRC(model, idx):
    kfs_prime, _ = model.solver.get_rate_constants()
    k_prime = kfs_prime[idx]
    k = kfs[idx]
    dr = r_prime - r
    dk = float(k_prime - k)
    print('k_prime: {}'.format(k_prime))

    return k/r*(dr/dk)

def XRC_by(model, idx):
    kfs_prime, _ = model.solver.get_rate_constants()
    k_prime = kfs_prime[idx]
    k = kfs[idx]
    dr = r_prime_by - r_by
    dk = float(k_prime - k)
    print('k_prime: {}'.format(k_prime))

    return k/r*(dr/dk)

model = MicroKineticModel(setup_file="ch4.model")
parser = model.parser
parser.parse_data("rel_energy.py")

xrc = XRC(model, 9)
print("xrc: {}".format(xrc))

xrc_by = XRC_by(model, 9)
print("xrc_by: {}".format(xrc_by))

tot_xrc = xrc*(r/(r+r_by)) + xrc_by*(r_by/(r+r_by))
print("xrc_total: {}".format(tot_xrc))

