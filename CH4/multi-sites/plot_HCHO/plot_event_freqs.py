#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import log10

from auto_frequency import reaction_rates
from ch4_model import rxn_expressions

reaction_rates.pop('CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)')
reaction_rates.pop('CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)')
reaction_rates.pop('CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)')
reaction_rates.pop('CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)')
reaction_rates.pop('O2_g + CHO_o + *_c -> O2_c + CHO_o(->)')
reaction_rates.pop('O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)')

skipped = [7, 8, 10]
rxn_expressions = [r for i, r in enumerate(rxn_expressions) if i not in skipped]

n_rxns = len(reaction_rates)//2
indices = list(range(1, 3*n_rxns+1, 3))
x_f, x_r = [], []
for i in indices:
    x_f.append(i)
    x_r.append(i+1)

y_f, y_r = [], []
labels = []
#for i, (k, v) in enumerate(sorted(reaction_rates.items())):
for rxn in rxn_expressions:
    rf = reaction_rates[rxn+'(->)']
    rr = reaction_rates[rxn+'(<-)']
    if rf != 0.0:
        y_f.append(log10(rf) + 5)
    else:
        y_f.append(0.0)

    if rr != 0.0:
        y_r.append(log10(rr) + 5)
    else:
        y_r.append(0.0)

x = []
for f, r in zip(x_f, x_r):
    x.extend([f, r])

plt.bar(x=x_f, height=y_f, bottom=-5, color='#0010FD')
plt.bar(x=x_r, height=y_r, bottom=-5, color='#FDDA00')
plt.legend(['Fwd', 'Rev'], loc=2)
plt.xticks(x, labels, rotation=90)
plt.yticks([-5, -4, -3, -2, -1, 0, 1, 2, 3 ,4], labels, rotation=90)
plt.ylim(-5, 4.5)
#plt.xlabel(labels)

plt.show()

