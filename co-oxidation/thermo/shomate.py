#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def H(T, params):
    A, B, C, D, E, F, G, H = params
    t = T/1000.0
    H = A*t + (B/2.0)*t**2 + (C/3.0)*t**3 + (D/4.0)*t**4 - E/t + F - H
    #kJ/mol
    return H

def S(T, params):
    A, B, C, D, E, F, G, H = params
    t = T/1000.0
    S = A*np.log(t) + B*t + (C/2.0)*t**2 + (D/3.0)*t**3 - E/(2.0*t**2) + G  # J/mol*K
    return S/1000
