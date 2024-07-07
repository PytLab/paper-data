#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from cvgs import t, cvgs

#cvgs = np.array(cvgs)/6.92e-16/1e14

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim(-0.5*6.92e-2, 11*6.92e-2)
ax.plot(t, cvgs, c='#000000', marker='o', markersize=3, lw=1.5)

ax2 = ax.twinx()
ax2.set_ylim(-0.5, 11)

plt.show()

