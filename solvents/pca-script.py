import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from sklearn.decomposition import PCA

df = pd.read_csv('solvent-pal-input.txt', sep=' ')
scaler = StandardScaler()
scaler.fit(df)
df_scaled = scaler.transform(df)

pca = PCA(n_components=2)
PC = pca.fit_transform(df_scaled)

pca_df = pd.DataFrame(data = PC, columns = ['PC1', 'PC2'])

fig, ax = plt.subplots(figsize=(14, 9))
ax.scatter(x=pca_df['PC1'], 
           y=pca_df['PC2'],
           s=100,
           cmap='cool')
 
ax.set_xlabel('PC1', 
              fontsize = 20)
ax.set_ylabel('PC2', 
              fontsize = 20)
ax.set_title('PCA: Solvent Feature Space', 
             fontsize=20)
 
plt.savefig('solvent-feature-space.png')