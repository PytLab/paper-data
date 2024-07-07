'''
    Module to plot ODE trajectory data in auto_ode_coverages.py
'''

import sys

import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    adsorbate_names = sys.argv[1: ]
else:
    adsorbate_names = []

globs, locs = {}, {}
exec(open('auto_ode_coverages.py', "rb").read(), globs, locs)
times, coverages = locs['times'][0::10], locs['coverages']
#times, coverages = locs['times'], locs['coverages']

# check args number
if adsorbate_names and len(adsorbate_names) != len(coverages[0]):
    print("args do not match coverges in auto_ode_coverages.py")
    sys.exit(1)

# plot
fig = plt.figure()
ax = fig.add_subplot(111)

coverages = np.array(coverages)
CO_cvgs = coverages[:, 0][0::10]
O_cvgs = coverages[:, 1][0::10]
Vac_cvgs = np.ones(len(coverages)//10) - CO_cvgs - O_cvgs

ax.set_ylim(-0.1, 1.1)
time = times[-1]
left, right = -time*0.05, time*1.05
ax.set_xlim(left, right)

label = r'$\bf{CO^{*}}$'
ax.plot(times, CO_cvgs, c='#000000', marker='o', markersize=3, label=label, lw=1.5)
label = r'$\bf{O^{*}}$'
ax.plot(times, O_cvgs, c='#FF0000', marker='o', markersize=3, label=label, lw=1.5)
label = r'$\bf{*}$'
ax.plot(times, Vac_cvgs, c='#33FF3A', marker='o', markersize=3, label=label, lw=1.5)

plt.legend(loc=0)
plt.show()

