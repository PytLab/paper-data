#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#from fit import x, y
x = [3.25, 3.3, 3.35, 3.4, 3.45]#, 3.5]
y = np.log([2.58e-6, 1.69e-6, 1.02e-6, 9.17e-7, 6.56e-7])#, 2.13e-7])

a, b = np.polyfit(x, y, 1)
print('{}x + {}'.format(a, b))
print('Ea = {}'.format(a*-1.987))

f = lambda x: a*x + b

lx = [3.23, 3.47]
ly = [f(3.23), f(3.47)]

plt.plot(lx, ly, color="red", linewidth=2)
plt.scatter(x, y, c="blue", s=100, marker="v")
plt.xlim(3.2, 3.5)
plt.yticks([-14.5, -14.0, -13.5, -13.0, -12.5])
plt.ylim(-14.75, -12.25)

plt.show()

