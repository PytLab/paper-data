#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#from fit import x, y
x = 1000/np.array([500, 550, 600, 650, 700, 750, 800])#, 3.5
y = np.log([7.89e-11, 7.89e-9, 3.93e-7, 5.14e-6, 7.62e-5, 5.99e-4, 5.59e-3])

a, b = np.polyfit(x, y, 1)
print('{}x + {}'.format(a, b))
print('Ea = {}'.format(a*-1.987))

f = lambda x: a*x + b

lx = [1.2, 2.0]
ly = [f(1.2), f(2.0)]

plt.plot(lx, ly, color="red", linewidth=2)
plt.scatter(x, y, c="blue", s=100, marker="v")
#plt.xlim(3.2, 3.5)
#plt.yticks([-14.5, -14.0, -13.5, -13.0, -12.5])
#plt.ylim(-14.75, -12.25)

plt.show()

