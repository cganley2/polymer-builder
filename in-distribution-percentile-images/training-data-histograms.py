import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# THE DATA IS SORTED BY TARGET VALUE IN THE EXCEL FILE

xls = pd.ExcelFile('pal-input.xlsx')
df = pd.read_excel(xls, 'ALL_RESULTS_DATA')

# ------------------------------------------------------------------------------

df.set_index('Polymer Labels', inplace=True)
a = df.loc['TT-DPP-TT-EDOT-EDOT']
b = df.loc['EDOT-DPP-EDOT-EDOT-EDOT']
c = df.loc['TT-DPP-TT-MEET-MEET']
d = df.loc['EDOT-DPP-EDOT-MEET-MEET']

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=5, ncols=1, sharex=True)
ax1.hist(df['Target'])
ax1.set_ylabel('All',rotation=0.01, labelpad=30)
ax1.set_yticks([])
ax2.hist(a['Target'])
ax2.set_ylabel('a',rotation=0.01, labelpad=30)
ax2.set_yticks([])
ax3.hist(b['Target'])
ax3.set_ylabel('b',rotation=0.01, labelpad=30)
ax3.set_yticks([])
ax4.hist(c['Target'])
ax4.set_ylabel('c',rotation=0.01, labelpad=30)
ax4.set_yticks([])
ax5.hist(d['Target'])
ax5.set_ylabel('d',rotation=0.01, labelpad=30)
ax5.set_yticks([])
fig.suptitle('Target Values of Published Polymers')
fig.tight_layout()
# plt.show()
plt.savefig('target-values-published-polymers.png')

# ------------------------------------------------------------------------------

# solv_iso_quad = df['Solvent-orca-isotropic-quadrupole']
# solv_iso_pol = df['Solvent-orca-isotropic-polarizability']
# solv_esp_min = df['Solvent-multiwfn-ESP-min']
# solv_esp_max = df['Solvent-multiwfn-ESP-max']
# solv_pol_ind = df['Solvent-multiwfn-polarity-index']
# solv_psa = df['Solvent-multiwfn-%polar-surface-area']

# poly_iso_quad = df['Polymer-orca-isotropic-quadrupole']
# poly_iso_pol = df['Polymer-orca-isotropic-polarizability']
# poly_esp_min = df['Polymer-multiwfn-ESP-min']
# poly_esp_max = df['Polymer-multiwfn-ESP-max']
# poly_pol_ind = df['Polymer-multiwfn-polarity-index']
# poly_psa = df['Polymer-multiwfn-%polar-surface-area']

# features = [solv_iso_quad,
#             solv_iso_pol,
#             solv_esp_min,
#             solv_esp_max,
#             solv_pol_ind,
#             solv_psa,
#             poly_iso_quad,
#             poly_iso_pol,
#             poly_esp_min,
#             poly_esp_max,
#             poly_pol_ind,
#             poly_psa
#             ]

# titles = ['Solvent: Isotropic Quadrupole',
#           'Solvent: Isotropic Polarizability',
#           'Solvent: ESP Min',
#           'Solvent: ESP Max',
#           'Solvent: Polarity Index',
#           'Solvent: % Polar Surface Area',
#           'Polymer: Isotropic Quadrupole',
#           'Polymer: Isotropic Polarizability',
#           'Polymer: ESP Min',
#           'Polymer: ESP Max',
#           'Polymer: Polarity Index',
#           'Polymer: % Polar Surface Area'
#           ]

# for index, feature in enumerate(features):
#     fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=5, ncols=1, sharex=True)
#     ax1.hist(feature,range=(feature.min(), feature.max()))
#     ax1.set_ylabel('All',rotation=0.01, labelpad=30)
#     ax1.set_yticks([])
#     ax2.hist(feature.iloc[0:int(0.01*feature.shape[0])])
#     ax2.set_ylabel('Top 1%',rotation=0.01, labelpad=30)
#     ax2.set_yticks([])
#     ax3.hist(feature.iloc[0:int(0.05*feature.shape[0])])
#     ax3.set_ylabel('Top 5%',rotation=0.01, labelpad=30)
#     ax3.set_yticks([])
#     ax4.hist(feature.iloc[0:int(0.1*feature.shape[0])])
#     ax4.set_ylabel('Top 10%',rotation=0.01, labelpad=30)
#     ax4.set_yticks([])
#     ax5.hist(feature.iloc[0:int(0.2*feature.shape[0])])
#     ax5.set_ylabel('Top 20%',rotation=0.01, labelpad=30)
#     ax5.set_yticks([])
#     fig.suptitle(titles[index])
#     fig.tight_layout()
#     plt.savefig(titles[index] + '.png')
