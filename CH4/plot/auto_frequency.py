# This file was automatically generated by scaks (https://github.com/PytLab/scaks).
# Version 0.1.0
# Date: Sun Sep 22 15:31:50 2019 
#
# Do not make changes to this file unless you know what you are doing

times = []
picked_indices = []
process_occurencies = []
process_occurencies = [
    16, 0, 17, 1, 16, 
    0, 156096, 156080, 19403, 19387, 
    2913, 2897, 1, 1, 14, 
    0, 2, 0, 47160564, 47160548, 
    1118350, 1118353, 1540891, 1540896, 282, 
    282, 1492, 1498, 0, 0, 
    0, 0, 0, 0, 0, 
    0, 
]

reaction_occurencies = {
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(->)': 19403,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(<-)': 19387,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(->)': 17,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(<-)': 1,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(->)': 16,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(<-)': 0,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(->)': 16,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(<-)': 0,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)': 2,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)': 0,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)': 1,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)': 1,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(->)': 14,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(<-)': 0,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(->)': 282,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(<-)': 282,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(->)': 1118350,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(<-)': 1118353,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(->)': 1492,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(<-)': 1498,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(->)': 1540891,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(<-)': 1540896,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 47160564,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 47160548,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(->)': 156096,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(<-)': 156080,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(->)': 2913,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)': 2897,
}

steady_reaction_occurencies = {
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(->)': 19403,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(<-)': 19387,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(->)': 17,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(<-)': 1,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(->)': 16,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(<-)': 0,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(->)': 16,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(<-)': 0,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)': 2,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)': 0,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)': 1,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)': 1,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(->)': 14,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(<-)': 0,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(->)': 282,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(<-)': 282,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(->)': 1118350,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(<-)': 1118353,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(->)': 1492,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(<-)': 1498,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(->)': 1540891,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(<-)': 1540896,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 47160564,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 47160548,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(->)': 156096,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(<-)': 156080,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(->)': 2913,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)': 2897,
}

reaction_rates = {
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(->)': 0.3057281972803352,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(<-)': 0.30547608929927633,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(->)': 0.00026786472987505534,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(<-)': 1.5756748816179724e-05,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(->)': 0.0002521079810588756,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(<-)': 0.0,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(->)': 0.0002521079810588756,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(<-)': 0.0,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)': 0.0,#3.151349763235945e-05,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)': 0.0,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)': 1.5756748816179724e-05,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)': 1.5756748816179724e-05,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(->)': 0.00022059448342651614,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(<-)': 0.0,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(->)': 0.004443403166162683,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(<-)': 0.004443403166162683,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(->)': 17.621560038574597,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(<-)': 17.621607308821044,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(->)': 0.02350906923374015,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(<-)': 0.023603609726637227,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(->)': 24.279432440111993,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(<-)': 24.279511223856073,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 743.0971609773682,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 743.0969088693871,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(->)': 2.4595654632103905,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(<-)': 2.4593133552293316,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(->)': 0.04589940930153154,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)': 0.045647301320472664,
}
