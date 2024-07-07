#!/usr/bin/env bash

for i in $(cat job_dirs.txt)
do
    echo "submit job in $i ..."
    cd $i && qsub kynetix.script
    cd -
    echo "done"
done
