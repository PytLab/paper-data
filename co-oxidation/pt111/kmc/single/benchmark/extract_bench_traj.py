#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

coverages = [[], [], []]
steps, times = [], []
location = ''

file_path = os.path.join(location, 'auto_coverages.py')
globs, locs = {}, {}
with open(file_path, 'r') as f:
    exec(f.read(), globs, locs)

step = locs['steps'][1]
time = locs['times'][1]
coverage = locs['coverages']
steps.append(step)
times.append(time)
coverages[0].append(coverage[0][1])
coverages[1].append(coverage[1][1])
coverages[2].append(coverage[2][1])

while os.path.exists('continue'):
    location = os.path.join(location, 'continue')
    file_path = os.path.join(location, 'auto_coverages.py')
    globs, locs = {}, {}
    with open(file_path, 'r') as f:
        exec(f.read(), globs, locs)
    try:
        step = locs['steps'][1]
        time = locs['times'][1]

        if time > 1e-3:
            break
        coverage = locs['coverages']
        steps.append(step)
        times.append(time)
        coverages[0].append(coverage[0][1])
        coverages[1].append(coverage[1][1])
        coverages[2].append(coverage[2][1])

        step = locs['steps'][-1]
        time = locs['times'][-1]
        coverage = locs['coverages']
        steps.append(step)
        times.append(time)
        coverages[0].append(coverage[0][-1])
        coverages[1].append(coverage[1][-1])
        coverages[2].append(coverage[2][-1])
    except IndexError:
        break

with open('bench_coverages.py', 'w') as f:
    content = 'times = {}\nsteps = {}\ncoverages = {}\n'.format(times, steps, coverages)
    content += "possible_types = ['V', 'O', 'C']\n"
    f.write(content)

