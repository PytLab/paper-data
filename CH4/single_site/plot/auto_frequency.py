# This file was automatically generated by scaks (https://github.com/PytLab/scaks).
# Version 0.1.0
# Date: Fri Oct  4 22:37:34 2019 
#
# Do not make changes to this file unless you know what you are doing

times = []
picked_indices = []
process_occurencies = []
process_occurencies = [
    509, 442, 67, 0, 463144, 
    463078, 66, 0, 66, 0, 
    66, 0, 66, 0, 36215, 
    36149, 66, 0, 66, 0, 
]

reaction_occurencies = {
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(->)': 67,
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(<-)': 0,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(->)': 509,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(<-)': 442,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(->)': 66,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(<-)': 0,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(->)': 66,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(<-)': 0,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(->)': 463144,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(<-)': 463078,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(->)': 36215,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(<-)': 36149,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(->)': 66,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(<-)': 0,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(->)': 66,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(<-)': 0,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(->)': 66,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(<-)': 0,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(->)': 66,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(<-)': 0,
}

steady_reaction_occurencies = {
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(->)': 67,
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(<-)': 0,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(->)': 509,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(<-)': 442,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(->)': 66,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(<-)': 0,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(->)': 66,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(<-)': 0,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(->)': 463144,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(<-)': 463078,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(->)': 36215,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(<-)': 36149,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(->)': 66,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(<-)': 0,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(->)': 66,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(<-)': 0,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(->)': 66,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(<-)': 0,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(->)': 66,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(<-)': 0,
}

reaction_rates = {
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(->)': 3.044098857235174e-06,
    'CH3_c + *_b <-> CH3-_c + *_b -> CH3_b + *_c(<-)': 0.0,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(->)': 2.3126064452726917e-05,
    'CH4_g + *_a + *_c <-> CH3-H_c + *_a -> CH3_c + H_a(<-)': 2.0081965595491744e-05,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(->)': 2.998664545933156e-06,
    'O2_c + CH3_b <-> OO-H_c + CH2_b -> OOH_c + CH2_b(<-)': 0.0,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(->)': 2.998664545933156e-06,
    'O2_c + CHO_b + O_v <-> OO-H_c + CO_b + O_v -> OOH_c + CO2_g + *_b + *_v(<-)': 0.0,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(->)': 0.021042628673661603,
    'O2_g + *_c + CH3_b -> O2_c + CH3_b(<-)': 0.021039630009115667,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(->)': 0.0016454035838025644,
    'O2_g + CHO_b + *_c -> O2_c + CHO_b(<-)': 0.0016424049192566312,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(->)': 2.998664545933156e-06,
    'OCH2_b + *_c <-> OCH2-_b + *_c -> *_b + OCH2_c(<-)': 0.0,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(->)': 2.998664545933156e-06,
    'OCH2_c + *_a + *_b <-> OCH-H_c + *_a + *_b -> CHO_b + *_c + H_a(<-)': 0.0,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(->)': 2.998664545933156e-06,
    'OOH_c + H_a + *_v -> H2O_g + *_c + *_a + O_v(<-)': 0.0,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(->)': 2.998664545933156e-06,
    'OOH_c + H_a + CH2_b <-> OOH-H_c + *_a + CH2_b -> H2O_g + OCH2_b + *_a + *_c(<-)': 0.0,
}
