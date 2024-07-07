#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from auto_coverages import possible_types
from auto_sum_coverages import cvgs

possible_types = ['*(Co)', '*(O2c)', '*(O3c)', '*(vac)', 'H(O2c)', 'CH3(Co)',
                  'CH3(O3c)', 'O2(Co)', 'OOH(Co)', 'CH2(O3c)', '-OCH2(Co)',
                  '-OCH2(O3c)', 'OCH2(Co)', 'CHO(O3c)']

cvgs_1 = [cvgs[0], cvgs[1], cvgs[2], sum(cvgs[3:])]
labels_1 = possible_types[:3] + ['intermediates']

pct_2 = np.array(cvgs[3:])/sum(cvgs[3:])
labels_2 = ['{} {:.2E}'.format(l, c) for c, l in zip(cvgs[3:], possible_types[3:])]

def func(pct):
    if pct > 2:
        return '{:.2f}%'.format(pct)
    else:
        return ''

fig1, ax1 = plt.subplots(figsize=(3, 3), subplot_kw=dict(aspect="equal"))
fig2, ax2 = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
#ax1.pie(cvgs_1, autopct=func, labels=labels_1, textprops=dict(color="w"))
ax1.pie(cvgs_1)

#wedges, texts, _ = ax2.pie(pct_2, autopct=func, textprops=dict(color="w"))
wedges, texts = ax2.pie(pct_2)

ax2.legend(wedges, labels_2, title='intermediate coverages',
           loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()

