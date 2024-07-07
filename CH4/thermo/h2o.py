#!/usr/bin/env python
# -*- coding: utf-8 -*-
A = 30.09200
B = 6.832514
C = 6.793435
D = -2.534480
E = 0.082139
F = -250.8810
G = 223.3967
H = -241.8264

T = 723.15

param = (A, B, C, D, E, F, G, H)

H0 = -241.826

from shomate import H, S

print('H = {}, S = {}'.format(H(T, param), S(T, param)))
print('TS = {}'.format(T*S(T, param)))
print(H0 + H(T, param) - T*S(T, param))

