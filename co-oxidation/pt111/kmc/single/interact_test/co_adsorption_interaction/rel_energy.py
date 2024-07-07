# Energy barriers.
#Ga = [0.0, 0.0, 0.0, 0.0, 0.0, 0.39]

# Reaction energies.
#dG = [-1.92, -2.09, -1.29, -2.33, -3.48, -0.46]

Ga, dG = [], []

# CO_g + *_f -> CO_f
Ga.append(0.3005)
dG.append(-0.89)
#dG.append(-1.69)

# O2_g + 2*_f <-> O-O_2f -> 2O_f
Ga.append(0.9)
dG.append(-1.27)

# O_f + CO_h <-> O-CO_h + *_f -> CO2_g + *_h + *_f
Ga.append(0.87)
dG.append(-1.16)

# O_f + *_h -> O_h + *_f
#Ga.append(1.41)
Ga.append(14.1)
dG.append(0.0)

# CO_f + *_h -> CO_h + *_f
#Ga.append(0.19)
Ga.append(19)
dG.append(0.0)

