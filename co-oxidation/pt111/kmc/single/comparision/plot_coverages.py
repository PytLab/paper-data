'''
    Module to plot auto_converages.py
'''

import sys
import numpy as np

import matplotlib.pyplot as plt

globs_1, locs_1 = {}, {}
exec(open('auto_coverages_std.py', "rb").read(), globs_1, locs_1)
std_times, std_steps = locs_1['times'][::10], locs_1['steps'][::10]

globs_2, locs_2 = {}, {}
exec(open('auto_coverages_redist.py', "rb").read(), globs_2, locs_2)
redist_times, redist_steps = locs_2['times'][::10], locs_2['steps'][::10]

# coverage vs time
plt.subplot(111)
plt.plot(std_steps, std_times, marker='o', markersize=10, c='#33FF3A', label='VSSM', linewidth=1.5)
plt.plot(redist_steps, redist_times, c='#FF0000', label='FDSR', linewidth=1.5, marker='^', markersize=10)

plt.xlabel(r'$\bf{kMC step}$', fontsize=16)
plt.ylabel(r'$\bf{Time (s)}$', fontsize=16)
plt.legend()

plt.show()

