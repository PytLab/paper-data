#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt

from auto_tofs import pCO, pO2
from auto_tofs import tofs as tofs_mkm

pCO_mkm = np.array(pCO)
pO2_mkm = np.array(pO2)
tofs_mkm = np.array(tofs_mkm)

with np.load("tofs-data.npz") as data:
    pCO_kmc = np.array(data['pCOs'])
    pO2_kmc = np.array(data['pO2s'])
    tofs_kmc = np.array(data['tofs'])*2 + 1e-22

# 2D interpolate.
pO2_mkm.shape = (-1, 1)
pO2_kmc.shape = (-1, 1)
interp_func_mkm = interp2d(pCO_mkm, pO2_mkm, tofs_mkm, kind="linear")
interp_func_kmc = interp2d(pCO_kmc, pO2_kmc, tofs_kmc, kind="linear")

import ipdb; ipdb.set_trace()
# Plot 3D contour.
#y, x = np.mgrid[0:1:100j, 0:1:100j]
ynew = np.linspace(1e-5, 0.5, 100)
xnew = np.linspace(1e-5, 0.5, 100)
z = interp_func_kmc(xnew, ynew) / interp_func_mkm(xnew, ynew)

extent = [np.min(xnew), np.max(xnew), np.min(ynew), np.max(ynew)]

CS = plt.contourf(xnew.reshape(-1), ynew.reshape(-1),
                  z, 20, cmap=plt.cm.jet)

#CS2 = plt.contour(CS, levels=CS.levels[::2],
#                  colors='#838B8B',
#                  hold='on')
#plt.clabel(CS2, colors='grey', inline=1, fontsize=12, fmt="%.2f")

# Add orthogonal lines.
# horizontal_line
#plt.plot([0.01, 1.0], [1.0, 1.0], color='#000000', linewidth=1.0)
#plt.plot([0.6, 0.6], [0.01, 2.0], color='#000000', linewidth=1.0)

plt.xlabel("P(CO_g)/bar")
plt.ylabel("P(O_2_g)/bar")

# Make a colorbar.
cbar = plt.colorbar(CS)
cbar.ax.set_ylabel("log(TOF)")

#cbar.add_lines(CS2)

plt.show()
