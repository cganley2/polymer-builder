while read solventline; do
    solvent=$solventline

    mkdir sims-$solvent
    cp /scratch4/pclancy3/users/cganley/bo/all-polymer-combos/array-skel.slurm ./sims-$solvent/array.slurm
    counter=1
    for filename in /scratch4/pclancy3/users/cganley/bo/all-polymer-combos/xyz/vacopt/*.xyz; do
        fullpath=$(realpath $filename)
        xyz=$(basename $filename)
        id=${xyz%????}
        mkdir sims-$solvent/$counter-$id
        cd sims-$solvent/$counter-$id
        cp $filename .
        cp /scratch4/pclancy3/users/cganley/bo/all-polymer-combos/orca-b97d3-skel.in ./orca-b97d3.in
        tail --lines=+3 $xyz >> orca-b97d3.in
        echo "*" >> orca-b97d3.in
        cp /scratch4/pclancy3/users/cganley/bo/all-polymer-combos/settings.ini .
        cp /scratch4/pclancy3/users/cganley/bo/all-polymer-combos/multiwfn-input-skel.inp ./multiwfn-input.inp
        sed -i "s/#filename#/$id/g" multiwfn-input.inp
        sed -i "s/#solvent#/$solvent/g" orca-b97d3.in
        touch $id.features
        echo $id >> $id.features
        counter=$((counter+1))
        cd ../..
    done

    cd sims-$solvent
    sbatch array.slurm
    cd ..

done < /scratch4/pclancy3/users/cganley/bo/all-polymer-combos/solvent-list-v2.txt