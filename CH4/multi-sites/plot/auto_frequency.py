# This file was automatically generated by scaks (https://github.com/PytLab/scaks).
# Version 0.1.0
# Date: Sun Oct 20 19:57:49 2019 
#
# Do not make changes to this file unless you know what you are doing

times = []
picked_indices = []
process_occurencies = []
process_occurencies = [
    96, 4, 123, 31, 92, 
    0, 840221, 840129, 104701, 104609, 
    32493, 32401, 9, 9, 79, 
    0, 13, 0, 48376558, 48376477, 
    271185, 271184, 374377, 374389, 72, 
    69, 339, 340, 0, 0, 
    0, 0, 0, 0, 0, 
    0, 
]

reaction_occurencies = {
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(->)': 104701,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(<-)': 104609,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(->)': 123,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(<-)': 31,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(->)': 92,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(<-)': 0,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(->)': 96,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(<-)': 4,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)': 13,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)': 0,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)': 9,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)': 9,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(->)': 79,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(<-)': 0,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(->)': 72,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(<-)': 69,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(->)': 271185,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(<-)': 271184,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(->)': 339,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(<-)': 340,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(->)': 374377,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(<-)': 374389,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 48376558,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 48376477,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(->)': 840221,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(<-)': 840129,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(->)': 32493,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)': 32401,
}

steady_reaction_occurencies = {
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(->)': 104701,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(<-)': 104609,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(->)': 123,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(<-)': 31,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(->)': 92,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(<-)': 0,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(->)': 96,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(<-)': 4,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)': 13,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)': 0,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)': 9,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)': 9,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(->)': 79,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(<-)': 0,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(->)': 72,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(<-)': 69,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(->)': 271185,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(<-)': 271184,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(->)': 339,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(<-)': 340,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(->)': 374377,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(<-)': 374389,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 48376558,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 48376477,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(->)': 840221,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(<-)': 840129,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(->)': 32493,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)': 32401,
}

reaction_rates = {
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(->)': 6.342788968178769,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(<-)': 6.337215606080294,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(->)': 0.007451342805570038,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(<-)': 0.0018779807070948876,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(->)': 0.005573362098475151,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(<-)': 0.0,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(->)': 0.005815682189713201,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(<-)': 0.00024232009123805002,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)': 0.0007875402965236626,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)': 0.0,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)': 0.0005452202052856125,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)': 0.0005452202052856125,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(->)': 0.004785821801951488,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(<-)': 0.0,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(->)': 0.0043617616422849,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(<-)': 0.0041800215738563625,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(->)': 16.42839348559765,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(<-)': 16.42833290557484,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(->)': 0.02053662773242474,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(<-)': 0.020597207755234253,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(->)': 22.679767199356863,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(<-)': 22.680494159630577,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 2930.652987085705,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 2930.648080103857,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(->)': 50.90060734503141,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(<-)': 50.89503398293293,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(->)': 1.96842668114949,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)': 1.9628533190510147,
}
