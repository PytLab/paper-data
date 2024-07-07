#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands

import numpy as np

filename = "pt-111.mkm"

species_pressures = {"O2_g": np.linspace(1e-5, 5, 20)}

species_name = "O2_g"

def dict2setup(d):
    setup = ""
    for key, value in d.iteritems():
        value = "'{}'".format(value) if type(value) is str else value
        line = "{} = {}\n".format(key, value)
        setup += line
    return setup

if "__main__" == __name__:
    setup_file = "./template/{}".format(filename)
    if os.path.exists(setup_file):
        globs, locs = {}, {}
        execfile(setup_file, globs, locs)

    job_dirs = ''
    for p in species_pressures[species_name]:
        dest = str(p)
        job_dirs += '{}\n'.format(p)
        print("Create job {}".format(p))
        os.mkdir(dest)
        commands.getstatusoutput("cp ./template/* {}".format(dest))
        locs['species_definitions'][species_name]['pressure'] = p

        # Write new setup file.
        with open("./{}/{}".format(dest, filename), "w") as f:
            content = dict2setup(locs)
            f.write(content)
        print("Ok.")
    with open('job_dirs.txt', 'w') as f:
        f.write(job_dirs)


