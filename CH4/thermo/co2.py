#!/usr/bin/env python
# -*- coding: utf-8 -*-
A = 24.99735
B = 55.18696
C = -33.69137
D = 7.948387
E = -0.136638
F = -403.6075
G = 228.2431
H = -393.5224

T = 723.15

param = (A, B, C, D, E, F, G, H)

H0 = -393.52

from shomate import H, S

print('H = {}, S = {}'.format(H(T, param), S(T, param)))
print('TS = {}'.format(T*S(T, param)))
print(H0 + H(T, param) - T*S(T, param))

