#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt

with np.load("tofs-data.npz") as data:
    pCOs = data['pCOs']
    pO2s = data['pO2s']
    tofs = data['tofs']

tofs = np.log10(tofs + 1e-15)

# 2D interpolate.
pO2s.shape = (-1, 1)
interp_func = interp2d(pCOs, pO2s, tofs, kind="linear")

# Plot 3D contour.
#y, x = np.mgrid[0:1:100j, 0:1:100j]
ynew = np.linspace(1e-5, 5, 100)
xnew = np.linspace(1e-5, 1e-4, 100)
z = interp_func(xnew, ynew)

extent = [np.min(xnew), np.max(xnew), np.min(ynew), np.max(ynew)]

CS = plt.contourf(xnew.reshape(-1), ynew.reshape(-1),
                  z, 20, cmap=plt.cm.coolwarm)

#CS2 = plt.contour(CS, levels=CS.levels[::2],
#                  colors='#838B8B',
#                  hold='on')
#plt.clabel(CS2, colors='grey', inline=1, fontsize=12, fmt="%.2f")

# Add orthogonal lines.
# horizontal_line
#plt.plot([0.01, 1.0], [1.0, 1.0], color='#000000', linewidth=1.0)
#plt.plot([0.6, 0.6], [0.01, 2.0], color='#000000', linewidth=1.0)

plt.xlabel(r"$P_{CO(g)}/bar$", fontsize="x-large")
plt.ylabel(r"$P_{O_{2(g)}}/bar$", fontsize="x-large")

# Make a colorbar.
cbar = plt.colorbar(CS)
cbar.ax.set_ylabel(r"$TOF/s^{-1}$", fontsize="x-large")

#cbar.add_lines(CS2)

plt.show()
#plt.savefig('tofs_contour.pdf')

