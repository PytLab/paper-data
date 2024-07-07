#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = [3.35, 3.4, 3.45, 3.5]
y = np.log([1.84e-7, 1.51e-7, 1.32e-7, 8.4e-8])

f = lambda x: -4.97*x + 1.2

lx = [3.33, 3.52]
ly = [f(3.33), f(3.52)]

plt.plot(lx, ly, color="red", linewidth=2)
plt.scatter(x, y, c="blue", s=100, marker="v")
plt.xlim(3.3, 3.55)
plt.yticks([-16.6, -16.2, -15.8, -15.4, -15.0])
plt.ylim(-16.75, -15)

plt.show()

