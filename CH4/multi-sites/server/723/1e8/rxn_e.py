#!/usr/bin/env python
# -*- coding: utf-8 -*-

'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o', (-, -)  # 1st C-H activation
'H_o + *_o <-> H-_o + *_o -> *_o + H_o', (0.5, 0.0)           # H transfer
'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c', (0.9, -1.0)    # 1st C-O coupling
'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o', (0.74, -0.06 - 1.26) # 2nd C-H activation & 2nd C-O coupling
'O2_g + *_c -> O2_c',  (0.0, -2.02)                             # O2 adsorption
'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o', (0.74, -0.25 + 0.25 + 0.25)  # 3nd C-H activation & reconst
'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o', (1.14, -0.2) # 4th C-H activation path 1
'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o', (0.94, 0.65) #4th C-H activation path 2
'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c', (0.49, -0.47) # O2 adsorption and dissociation
'H_a + *_a <-> H-_a + *_a -> *_a + H_a', (0.5, 0.0) # H transfer b/w O2c
'H_b + *_b <-> H-_b + *_b -> *_b + H_b', (0.92, 0.0) # H trbnsfer b/w O2c
'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a', (0.43, -0.39) -> (0.5, -0.39) # H -> O* from O2c
'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b', (0.13, -0.37) -> (0.5, -0.37)# H -> O* from O3c
'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a', (0.11, -0.2) -> (0.5, -0.2) # H -> OH* from O2c
'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b', (0.08, -0.1) -> (0.5, -0.1) # H -> OH* from O3c

