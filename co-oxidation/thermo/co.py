#!/usr/bin/env python
# -*- coding: utf-8 -*-
A = 25.56759
B = 6.096130
C = 4.054656
D = -2.671301
E = 0.131021
F = -118.0089
G = 227.3665
H = -110.5271

T = 500

param = (A, B, C, D, E, F, G, H)

H0 = -110.53

from shomate import H, S

print('H = {}, S = {}'.format(H(T, param), S(T, param)))
print('TS = {}'.format(T*S(T, param)))
print(H0 + H(T, param) - T*S(T, param))

