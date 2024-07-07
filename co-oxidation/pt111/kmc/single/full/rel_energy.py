# Energy barriers.
#Ga = [0.0, 0.0, 0.0, 0.0, 0.0, 0.39]

# Reaction energies.
#dG = [-1.92, -2.09, -1.29, -2.33, -3.48, -0.46]

Ga, dG = [], []

# CO_g + *_h -> CO_h
Ga.append(0.4)
dG.append(-0.71)
#dG.append(-1.65)

# CO_g + *_f -> CO_f
Ga.append(0.4)
dG.append(-0.74)
#dG.append(-1.69)

# O2_g + 2*_f <-> O-O_2f -> 2O_f
Ga.append(0.98)
dG.append(-2.4)

# O2_g + 2*_h <-> O-O_2h -> 2O_h
Ga.append(0.45)
dG.append(-1.56)

# O_h + CO_f <-> O-CO_f + *_h -> CO2_g + *_h + *_f
Ga.append(0.87)
dG.append(-1.78)

# O_f + CO_h <-> O-CO_h + *_f -> CO2_g + *_h + *_f
Ga.append(0.82)
dG.append(-1.40)

# O_f + *_h -> O_h + *_f
Ga.append(1.41)
dG.append(0.42)

# CO_f + *_h -> CO_h + *_f
Ga.append(0.19)
dG.append(0.16)

