#!/usr/bin/env bash

declare -a arr=("1" "auto_kmc_model.py" "kmc_*" "out.log" "*.mkm" "*.o*" "rel_energy.py" "auto_lattice_*" "kynetix.script")

for i in "${arr[@]}"
do
    echo "Remove all ${i}"
    find . -iname "$i" | xargs rm
done

