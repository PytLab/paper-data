#!/usr/bin/env python
# -*- coding: utf-8 -*-
Ga, dG = [], []

#1 CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a'
Ga.append(1.803 + 0.1)
dG.append(0.862)

#2 CH3_c + *_b -> CH3-_c + *_b -> CH3_b + *_c
Ga.append(1.4)
dG.append(-0.51)

#3 'O2_g + *_c + CH3_b -> O2_c + CH3_b
Ga.append(0.412)
dG.append(-0.12)

#4 O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b
Ga.append(1.029)
dG.append(-0.66)

#5 OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c
Ga.append(0.77)
dG.append(-0.53 - 1.55)

#6 OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c
#Ga.append(1.304)
Ga.append(1.8)
dG.append(1.079)
#dG.append(0.5)

##7 OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a
#Ga.append(0.81)
#dG.append(-0.46 + -0.91)

#7 OCH2_c + *_a <-> OCH-H_c + *_a -> CHO_c + H_a
Ga.append(1.21)
dG.append(-1.044)

#7b CHO_c + *_b <-> CHO-_c + *_b -> CHO_b + *_c
Ga.append(0.784)
dG.append(-0.96)

#8 O2_g + CHO_b + *_c -> O2_c + CHO_b
Ga.append(0.412)
#Ga.append(0.)
dG.append(-0.7)
#dG.append(-0.94)

#9 O2_c + CHO_b + O_b <-> OO-H_c + CO_b -> OOH_c + CO2_g + 2*_b
Ga.append(1.33)
dG.append(-0.57)

#10 OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v
Ga.append(0.0)
dG.append(-3.05 - 0.66)

