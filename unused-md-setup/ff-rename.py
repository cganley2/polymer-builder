original_species = []

with open('toluene.xyz', 'r') as f:

    n_atoms = int(f.readline())
    f.seek(0)

    xyz_lines = f.readlines()
    for index in range(2, n_atoms + 2):
        original_species.append(xyz_lines[index].split()[0])
    f.seek(0)
    
    xyz_read = f.read()
    for species in original_species:
        xyz_read = xyz_read.replace(species, species + 'Z')

    with open('toluene.ff', 'r') as g:
        ff_read = g.read()
        for species in original_species:
            ff_read = ff_read.replace(species, species + 'Z')
    g.close()

f.close()

with open('toluene.xyz', 'w') as f:
    f.write(xyz_read)
f.close()

with open('toluene.ff', 'w') as g:
    g.write(ff_read)
g.close()