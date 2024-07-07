#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from cvgs import t, cvgs

plt.ylim(-0.05, 1.15)
plt.plot(t, cvgs, c='#000000', marker='o', markersize=3, lw=1.5)
plt.show()


