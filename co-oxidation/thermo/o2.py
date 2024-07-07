#!/usr/bin/env python
# -*- coding: utf-8 -*-
A = 31.32234
B = -20.23531
C = 57.86644
D = -36.50624
E = -0.007374
F = -8.903471
G = 246.7945
H = 0

T = 500

param = (A, B, C, D, E, F, G, H)

H0 = 0

from shomate import H, S

print('H = {}, S = {}'.format(H(T, param), S(T, param)))
print('TS = {}'.format(T*S(T, param)))
print(H0 + H(T, param) - T*S(T, param))

