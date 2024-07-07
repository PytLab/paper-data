#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import log10

from auto_frequency import reaction_rates
from ch4_model import rxn_expressions

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
        y_f.append(log10(rf) + 7)
    else:
        y_f.append(0.0)

    if rr != 0.0:
        y_r.append(log10(rr) + 7)
    else:
        y_r.append(0.0)

x = []
for f, r in zip(x_f, x_r):
    x.extend([f, r])

plt.bar(x=x_f, height=y_f, bottom=-7, color='#0010FD')
plt.bar(x=x_r, height=y_r, bottom=-7, color='#FDDA00')
plt.legend(['Fwd', 'Rev'], loc=2)
plt.xticks(x, labels, rotation=90)
plt.ylim(-7, -0.5)
#plt.xlabel(labels)

plt.show()

