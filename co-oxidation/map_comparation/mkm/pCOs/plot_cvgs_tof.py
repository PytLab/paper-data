import os

import numpy as np
import matplotlib.pyplot as plt


if "__main__" == __name__:
    # Plot TOFs.
    globs, locs = {}, {}
    exec(open("auto_tofs.py", "rb").read(), globs, locs)
    pressures = locs['pCO']
    TONs = locs['tofs']

    fig = plt.figure()

    # Plot cvgs.
    globs, locs = {}, {}
    exec(open("auto_cvgs.py", "rb").read(), globs, locs)
    coverages = locs['cvgs']
    adsorbates = locs['adsorbates']


    ax1 = fig.add_subplot(111)
    pressure_range = max(pressures) - min(pressures)
    ax1.set_ylim(-0.1, 1.1)
    ax1.set_xlim(min(pressures)-pressure_range*0.1, max(pressures)+pressure_range*0.1)
    ax1.set_xlabel(r"$P(CO_{(g)})/bar$")
    ax1.set_ylabel(r"$Coverages$")


    coverages = list(zip(*coverages))
    CO_cvgs = np.array(coverages[0])
    O_cvgs = np.array(coverages[1])

    # plot CO
    ax1.plot(pressures, CO_cvgs, color="#0F0F0F",
                                 linewidth=2.0,
                                 marker='o',
                                 markerfacecolor="#0F0F0F",
                                 markeredgecolor="#0F0F0F",
                                 markersize=7.0,
                                 alpha=0.7,
                                 label=r"$\theta_{CO^{*}}$")

    # plot O
    ax1.plot(pressures, O_cvgs, color="#CD6889",
                                linewidth=2.0,
                                marker='o',
                                markerfacecolor="#CD6889",
                                markeredgecolor="#CD6889",
                                markersize=7.0,
                                alpha=0.7,
                                label=r"$\theta_{O^{*}}$")

    # Plot TOF.
    ax2 = ax1.twinx()
    pressure_range = max(pressures) - min(pressures)
    TON_range = max(TONs) - min(TONs)
    ax2.set_ylim(min(TONs)-TON_range*0.1, max(TONs)+TON_range*0.1)
    ax2.set_ylabel(r"$TOF/s^{-1}$")
    ax2.plot(pressures, TONs, color="#7D9EC0",
                              linewidth=2.0,
                              marker='s',
                              markerfacecolor="#7D9EC0",
                              markeredgecolor="#7D9EC0",
                              markersize=7.0,
                              alpha=0.7,
                              label='$TOF$')

    # Trick for labels.
    ax1.plot(0, 0, color="#7D9EC0",
                   linewidth=2.0,
                   marker='s',
                   markerfacecolor="#7D9EC0",
                   markeredgecolor="#7D9EC0",
                   markersize=7.0,
                   alpha=0.7,
                   label=r'$TOF$')
#    ax1.grid(True)
    ax1.legend(loc=0)

    plt.show()

