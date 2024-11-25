for file in /Users/connorganley/Documents/JHU/2023-2024/polymer-builder/code/input-data/all-polymer-combos/unopt-xyz/*.xyz; do
    # Read the first line of the file and double the number
    read -r line < $file
    new_count=$(( $(echo "$line" | awk '{print $1}') * 2))

    # Output the new count to a temporary file
    echo "$new_count" > temp.xyz

    # Copy the species and coordinates and paste them below the existing coordinates
    awk 'NR>2{print} NR==2{print}' $file >> temp.xyz

    # Add 5 to the z values of only the new coordinates
    awk -v OFS="\t" 'NR>2{print $1, $2, $3, $4+5}' $file >> temp.xyz

    # Rename the temporary file to the original filename
    filename=$(basename "$file" .xyz)
    mv temp.xyz ../2x-interactions/2x-$filename-unopt.xyz
done