# This file was automatically generated by scaks (https://github.com/PytLab/scaks).
# Version 0.1.0
# Date: Fri Oct 25 20:54:03 2019 
#
# Do not make changes to this file unless you know what you are doing

times = []
picked_indices = []
process_occurencies = []
process_occurencies = [
    39, 1, 69, 31, 34, 
    0, 336728, 336694, 41983, 41949, 
    11775, 11741, 3, 3, 27, 
    0, 7, 0, 4608469, 4608440, 
    299, 299, 430, 435, 22, 
    20, 123, 123, 128, 124, 
    4, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 
]

reaction_occurencies = {
    'CH2O_o -> CH2O_g + *_o(->)': 4,
    'CH2O_o -> CH2O_g + *_o(<-)': 0,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(->)': 41983,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(<-)': 41949,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(->)': 69,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(<-)': 31,
    'CH3_o + *_o <-> CH2-H_o + *_o -> CH2_o + H_o(->)': 128,
    'CH3_o + *_o <-> CH2-H_o + *_o -> CH2_o + H_o(<-)': 124,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(->)': 34,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(<-)': 0,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(->)': 39,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(<-)': 1,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)': 7,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)': 0,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)': 3,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)': 3,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(->)': 27,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(<-)': 0,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(->)': 22,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(<-)': 20,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(->)': 299,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(<-)': 299,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(->)': 123,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(<-)': 123,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(->)': 430,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(<-)': 435,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 4608469,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 4608440,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(->)': 336728,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(<-)': 336694,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(->)': 11775,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)': 11741,
}

steady_reaction_occurencies = {
    'CH2O_o -> CH2O_g + *_o(->)': 4,
    'CH2O_o -> CH2O_g + *_o(<-)': 0,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(->)': 41983,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(<-)': 41949,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(->)': 69,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(<-)': 31,
    'CH3_o + *_o <-> CH2-H_o + *_o -> CH2_o + H_o(->)': 128,
    'CH3_o + *_o <-> CH2-H_o + *_o -> CH2_o + H_o(<-)': 124,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(->)': 34,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(<-)': 0,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(->)': 39,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(<-)': 1,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)': 7,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)': 0,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)': 3,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)': 3,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(->)': 27,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(<-)': 0,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(->)': 22,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(<-)': 20,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(->)': 299,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(<-)': 299,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(->)': 123,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(<-)': 123,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(->)': 430,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(<-)': 435,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 4608469,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 4608440,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(->)': 336728,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(<-)': 336694,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(->)': 11775,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)': 11741,
}

reaction_rates = {
    'CH2O_o -> CH2O_g + *_o(->)': 0.0007182687634485281,
    'CH2O_o -> CH2O_g + *_o(<-)': 0.0,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(->)': 7.5387693739648896,
    'CH2_2o + O2_c <-> OO-HCH_2o + *_c -> CHO_o + OH_c + *_o(<-)': 7.532664089475577,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(->)': 0.012390136169487111,
    'CH3_c + *_o <-> CH3-_c + *_o -> CH3_o + *_c(<-)': 0.005566582916726093,
    'CH3_o + *_o <-> CH2-H_o + *_o -> CH2_o + H_o(->)': 0.0229846004303529,
    'CH3_o + *_o <-> CH2-H_o + *_o -> CH2_o + H_o(<-)': 0.022266331666904372,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(->)': 0.00610528448931249,
    'CH3_o + 2*_o <-> CH2-H_o + 2*_o -> CH2_2o + H_o(<-)': 0.0,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(->)': 0.007003120443623149,
    'CH4_g + *_c + *_o <-> CH3-H_c + *_o -> CH3_c + H_o(<-)': 0.00017956719086213203,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(->)': 0.0012569703360349243,
    'CHO_o + O_o + *_o <-> COO-H_2o + *_o -> CO2_g + H_o + 2*_o(<-)': 0.0,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(->)': 0.0005387015725863961,
    'CHO_o + O_o + O2_c <-> COO-H_2o + O2_c -> CO2_g + OOH_c + 2*_o(<-)': 0.0005387015725863961,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(->)': 0.004848314153277565,
    'CHO_o + O_o + OH_c <-> CO-H_o + O_o + OH_c -> CO2_g + H2O_g + *_c + 2*_o(<-)': 0.0,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(->)': 0.003950478198966905,
    'H_a + OH_c <-> H-OH_c + *_a -> H2O_g + *_c + *_a(<-)': 0.003591343817242641,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(->)': 0.05369059006777748,
    'H_a + O_c <-> H-O_c + *_a -> OH_c + *_a(<-)': 0.05369059006777748,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(->)': 0.022086764476042242,
    'H_b + OH_c <-> H-OH_c + *_b -> H2O_g + *_c + *_b(<-)': 0.022086764476042242,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(->)': 0.07721389207071677,
    'H_b + O_c <-> H-O_c + *_b -> OH_c + *_b(<-)': 0.07811172802502744,
#    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 827.5298325052188,
#    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 827.5246250566838,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(->)': 60.465301044624,
    'O2_g + *_v + *_c <-> O-O_v + *_c -> O_v + O_c(<-)': 60.45919576013468,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(->)': 827.5298325052188,
    'O2_g + CH2_2o + *_c -> O2_c + CH2_2o(<-)': 827.5246250566838,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(->)': 2.114403672401605,
    'O2_g + CHO_o + *_c -> O2_c + CHO_o(<-)': 2.1082983879122925,
}
