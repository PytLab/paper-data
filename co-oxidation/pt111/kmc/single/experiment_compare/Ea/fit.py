#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy

x = [3.35, 3.4, 3.45, 3.5]
y = numpy.log([1.84e-7, 1.51e-7, 1.32e-7, 8.4e-8])

a, b = numpy.polyfit(x, y, 1)

print('{}x + {}'.format(a, b))

