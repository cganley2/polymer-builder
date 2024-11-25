for directory in ./*-DPP-*/; do
    cd $directory
    name=$(basename $directory)
    awk '/ORBITAL ENERGIES/{found=1; next} found && $2==0{print prev; print; exit} $2==2{prev=$0}' orca-b97d3.out > $name.homolumo
    cd ..
done