for dir in ./*/; # /scratch4/pclancy3/users/cganley/bo/all-polymer-combos/sims/*;
do
    # echo filename="${dir##*/}"
    # echo ${dir##*/}-vacopt.xyz
    cd $dir
    filename=$(basename -- "$dir")
    cp orca-b97d3.xyz $filename-vacopt.xyz
    cp $filename-vacopt.xyz ../opt-xyz-for-dragon.xyz/
    cd ..
done