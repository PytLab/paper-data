#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy

x = [3.25, 3.3, 3.35, 3.4, 3.45, 3.5]
y = numpy.log([4.58e-7, 7.52e-7, 6.09e-7, 2.98e-7, 3.05e-7, 1.5e-7])

a, b = numpy.polyfit(x, y, 1)

print('{}x + {}'.format(a, b))

