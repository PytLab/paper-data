# This file was automatically generated by scaks (https://github.com/PytLab/scaks).
# Version 0.1.0
# Date: Fri Oct 18 21:09:09 2019 
#
# Do not make changes to this file unless you know what you are doing

times = []
picked_indices = []
process_occurencies = []
process_occurencies = [
    78699, 78641, 58, 0, 388264, 
    388207, 57, 0, 57, 0, 
    57, 0, 57, 0, 32923, 
    32866, 57, 0, 57, 0, 
]

reaction_occurencies = {
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(->)': 58,
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(<-)': 0,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(->)': 78699,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(<-)': 78641,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(->)': 57,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(<-)': 0,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(->)': 57,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(<-)': 0,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(->)': 388264,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(<-)': 388207,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(->)': 32923,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(<-)': 32866,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(->)': 57,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(<-)': 0,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(->)': 57,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(<-)': 0,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(->)': 57,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(<-)': 0,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(->)': 57,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(<-)': 0,
}

steady_reaction_occurencies = {
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(->)': 58,
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(<-)': 0,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(->)': 78699,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(<-)': 78641,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(->)': 57,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(<-)': 0,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(->)': 57,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(<-)': 0,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(->)': 388264,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(<-)': 388207,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(->)': 32923,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(<-)': 32866,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(->)': 57,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(<-)': 0,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(->)': 57,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(<-)': 0,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(->)': 57,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(<-)': 0,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(->)': 57,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(<-)': 0,
}

reaction_rates = {
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(->)': 7.266878703057298e-06,
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(<-)': 0.0,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(->)': 0.009860277362963901,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(<-)': 0.009853010484260844,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(->)': 7.14158769093562e-06,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(<-)': 0.0,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(->)': 7.14158769093562e-06,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(<-)': 0.0,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(->)': 0.048645989530411014,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(<-)': 0.048638847942720075,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(->)': 0.00412495599208199,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(<-)': 0.0041178144043910545,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(->)': 7.14158769093562e-06,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(<-)': 0.0,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(->)': 7.14158769093562e-06,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(<-)': 0.0,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(->)': 7.14158769093562e-06,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(<-)': 0.0,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(->)': 7.14158769093562e-06,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(<-)': 0.0,
}

