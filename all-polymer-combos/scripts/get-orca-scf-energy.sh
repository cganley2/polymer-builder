for dir in /Users/connorganley/Documents/JHU/2023-2024/polymer-builder/code/input-data/all-polymer-combos/orca-vac-opts/*; do
    grep "FINAL SINGLE POINT ENERGY" "$dir"/orca-b97d3.out | tail -n 1 | awk -v d="$dir" '{print d ": " $0}'
done