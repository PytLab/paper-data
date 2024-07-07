#!/usr/bin/env python
# -*- coding: utf-8 -*-
Ga, dG = [], []

#1 'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o', (-, -)  # 1st C-H activation
Ga.append(1.804)
dG.append(0.767)

#3 'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c', (0.9, -1.0)    # 1st C-O coupling
Ga.append(0.82 + 0.1)
dG.append(-1.0)

#4 'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o', (0.74, -0.06 - 1.26) # 2nd C-H activation & 2nd C-O coupling
Ga.append(0.74)
dG.append(-0.06 - 1.26)

#5 'O2_g + CH2_2o + *_c -> O2_c + CH2_2o',  (0.0, -2.02)                             # O2 adsorption
Ga.append(0.0)
dG.append(-2.02 + 1.41)

#6 'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o', (0.74, -0.25 + 0.25 + 0.25)  # 3nd C-H activation & reconst
Ga.append(0.74)
dG.append(-0.25 + 0.25 + 0.25)

# 'O2_g + CHO_o + *_c -> O2_c + CHO_o'
Ga.append(0.0)
dG.append(-2.02 + 1.41)

#7 'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o', (1.14, -0.2) # 4th C-H activation path 1
Ga.append(1.14)
dG.append(-0.2)

#8 'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o', (0.94, 0.65) #4th C-H activation path 2
Ga.append(0.94)
dG.append(0.65 - 1.17 - 1.57)

#9 CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o #4TH C-H activation path 3
Ga.append(1.1)
dG.append(0.33 - 1.57)

#10 'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c', (0.49, -0.47) # O2 adsorption and dissociation
Ga.append(0.0)
dG.append(-0.61 - 0.47)

#11 'H_a + *_a <-> H-_a + *_a -> *_a + H_a', (0.5, 0.0) # H transfer b/w O2c
Ga.append(0.5)
dG.append(0.0)

#12 'H_b + *_b <-> H-_b + *_b -> *_b + H_b', (0.92, 0.0) # H trbnsfer b/w O2c
Ga.append(0.92)
dG.append(0.0)

#13 'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a', (0.43, -0.39) -> (0.5, -0.39) # H -> O* from O2c
Ga.append(0.5)
dG.append(-0.39)

#14 'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b', (0.13, -0.37) -> (0.5, -0.37)# H -> O* from O3c
Ga.append(0.5)
dG.append(-0.37)

#15 'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a', (0.11, -0.2) -> (0.5, -0.2) # H -> OH* from O2c
Ga.append(0.5)
dG.append(-0.2 - 1.17)

#16 'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b', (0.08, -0.1) -> (0.5, -0.1) # H -> OH* from O3c
Ga.append(0.5)
dG.append(-0.1 - 1.17)

