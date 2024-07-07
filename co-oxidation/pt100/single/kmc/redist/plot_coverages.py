'''
    Module to plot auto_converages.py
'''

import sys

import matplotlib.pyplot as plt

if "__main__" == __name__:
    globs, locs = {}, {}
    exec(open('auto_coverages.py', "rb").read(), globs, locs)

    times, steps, coverages = locs['times'], locs['steps'], locs['coverages'][-3:]
    possible_types = locs['possible_types'][-3:]
    colors = ['#33FF3A', '#FF0000', '#000000']

    # coverage vs steps
#    plt.subplot(111)
#    for sp, cvgs, color in zip(possible_types, coverages, colors):
#        sp = r'$\bf{*}$' if sp == 'Vac' else r'$\bf{' + sp + r'^{*}}$'
#        plt.plot(steps, cvgs, c=color, label=sp, linewidth=1.5)
#        plt.scatter(steps, cvgs, c=color, s=10)
#
#    plt.ylabel(r'$\bf{Coverages}$', fontsize=16)
#    plt.xlabel(r'$\bf{kMC step}$', fontsize=16)
#    plt.ylim(-0.1, 1.1)
#    plt.legend()

    # coverage vs time
    plt.subplot(111)
    for sp, cvgs, color in zip(possible_types, coverages, colors):
        sp = r'$\bf{*}$' if sp == 'Vac' else r'$\bf{' + sp + r'^{*}}$'
        plt.plot(times, cvgs, c=color, label=sp, linewidth=1.5)
        plt.scatter(times, cvgs, c=color, s=10)

    plt.ylabel(r'$\bf{Coverages}$', fontsize=16)
    plt.xlabel(r'$\bf{Time (s)}$', fontsize=16)
    plt.ylim(-0.1, 1.1)
    plt.legend()

    if "-s" in sys.argv:
        plt.savefig("coverages.png")
    else:
        plt.show()

