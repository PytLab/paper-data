# Energy barriers.
#Ga = [0.0, 0.0, 0.0, 0.0, 0.0, 0.39]

# Reaction energies.
#dG = [-1.92, -2.09, -1.29, -2.33, -3.48, -0.46]

Ga, dG = [], []

# CO_g + *_b -> CO_b
Ga.append(0.0)
dG.append(-2.09)

# O2_g + 2*_b -> 2O_b
Ga.append(0.07)
dG.append(-2.48)

# CO_b + O_b <-> CO-O_2b -> CO2_g + 2*_b
Ga.append(0.39)
dG.append(0.33)

# CO_b + *_t <-> CO_t + *_b -> CO_b + *_t
Ga.append(0.17)
dG.append(0.0)

# O_b + *_t <-> O_t + *_b -> O_b + *_t
Ga.append(1.15)
dG.append(0.0)

