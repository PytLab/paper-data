#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

possible_types = ['*_c', '*_o', 'H_o', 'CH3_c', 'CH3_o', '-CH2_o',
                  'O2_c', 'OH_c', 'CHO_o', 'OOH_c', '*_v', 'O_c']

color_dict = {
    '*_c': '#3913CA',
    '*_o': '#FB0101',
    'H_o': '#08DA20',
    'CH3_c': '#5E5F5E',
    'CH3_o': '#5E5F5E',
    '-CH2_o': '#FECA00',
    'O2_c': '#970000',
    'OH_c': '#D500FE',
    'CHO_o': '#009CDF',
    'OOH_c': '#79E214',
    '*_v': '#FFFFFF',
    'O_c': '#FB0101',
}

type_dict = {
    '*_c': '*(Co)',
    '*_o': '*(O)',
    'H_o': 'H(O)',
    'CH3_c': 'CH3(Co)',
    'CH3_o': 'CH3(O)',
    '-CH2_o': 'CH2(O)',
    'O2_c': 'O2(Co)',
    'OH_c': 'OH(Co)',
    'CHO_o': 'CHO(O)',
    'OOH_c': 'OOH(Co)',
    '*_v': '*(Vac)',
    'O_c': 'O(Co)',
}

for t in possible_types:
    if t == '*_v':
        edgecolor = '#000000'
    else:
        edgecolor = color_dict[t]
    plt.scatter([0.0], [0.0], color=color_dict[t],
                edgecolor=edgecolor,
                label=type_dict[t],
                marker='o')

plt.legend()
plt.show()

