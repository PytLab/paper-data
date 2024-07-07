#!/usr/bin/env python
# -*- coding: utf-8 -*-
A = -0.703029
B = 108.4773
C = -42.52157
D = 5.862788
E = 0.678565
F = -76.84376
G = 158.7163
H = -74.87310

T = 723.15

param = (A, B, C, D, E, F, G, H)

H0 = -74.87

from shomate import H, S

print('H = {}, S = {}'.format(H(T, param), S(T, param)))
print('TS = {}'.format(T*S(T, param)))
print(H0 + H(T, param) - T*S(T, param))

