'''
    Module to plot auto_converages.py
'''

import sys

import numpy as np
import matplotlib.pyplot as plt

if "__main__" == __name__:
    globs, locs = {}, {}
    exec(open('bench_coverages.py', "rb").read(), globs, locs)

    times, steps, coverages = locs['times'], locs['steps'], locs['coverages']
    possible_types = locs['possible_types']

    times = np.array(times)*5

    # coverage vs steps
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    CO_cvgs, O_cvgs, Vac_cvgs = np.zeros(len(steps)), np.zeros(len(steps)), np.zeros(len(steps))
    for sp, cvgs in zip(possible_types, coverages):
        if sp.startswith("O"):
            O_cvgs += np.array(cvgs)
        elif sp.startswith("C"):
            CO_cvgs += np.array(cvgs)
        elif sp.startswith("V"):
            Vac_cvgs += np.array(cvgs)

    # Plot lines.
    # CO
    label = r'$\bf{CO^{*}}$'
    ax1.plot(steps, CO_cvgs, c="#000000", marker='o', markersize=3, label=label, lw=1.5)
    # O
    label = r'$\bf{O^{*}}$'
    ax1.plot(steps, O_cvgs, c="#FF0000", marker='o', markersize=3, label=label, lw=1.5)
    # Vac
    label = r'$\bf{*}$'
    ax1.plot(steps, Vac_cvgs, c="#33FF3A", marker='o', markersize=3, label=label, lw=1.5)

    ax1.set_ylim(-0.1, 1.1)
    step = steps[-1]
    left, right = -step*0.05, step*1.05
    ax1.set_xlim(left, right)
    ax1.legend(loc=0)

    # coverage vs time
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    # Plot lines.
    # CO
    label = r'$\bf{CO^{*}}$'
    ax2.plot(times, CO_cvgs, c="#000000", marker='o', markersize=3, label=label, lw=1.5)
    # O
    label = r'$\bf{O^{*}}$'
    ax2.plot(times, O_cvgs, c="#FF0000", marker='o', markersize=3, label=label, lw=1.5)
    # Vac
    label = r'$\bf{*}$'
    ax2.plot(times, Vac_cvgs, c="#33FF3A", marker='o', markersize=3, label=label, lw=1.5)
    ax2.legend(loc=0)

    ax2.set_ylim(-0.1, 1.1)
    time = times[-1]
    left, right = -time*0.05, time*1.05
    ax2.set_xlim(left, right)

    plt.show()

