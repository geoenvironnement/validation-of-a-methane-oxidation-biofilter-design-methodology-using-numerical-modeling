import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator
import numpy as np
import pandas as pd

# Data
data = pd.read_excel('../0.Data/Kair_CompostMix.xlsx')
dataTh = data['Theta']
dataKa = data['ka']

fig, ax = plt.subplots(figsize=(7, 5))

# multiple line plots
ax.plot(dataTh, dataKa, marker='x', color='black', linestyle='none', label='Compost')

# trend
ax.plot([26, 54, 58, 65], [1.e-5, 1.e-5, 6.e-6, 3.e-7], color='gray',  linestyle='-')
ax.plot([26, 51, 55, 61], [7.3e-6, 7.e-6, 4.e-6, 3.e-7], color='black',  linestyle='-.')
ax.plot([26, 49, 52, 57], [5.e-6, 5.e-6, 3.3e-6, 3.e-7], color='gray',  linestyle='-')

ax.fill_between([26, 49, 52, 54, 57, 58, 65], [5.e-6, 5.e-6, 3.3e-6, 1.2e-6, 3.e-7, 3.e-7, 3.e-7], [1.e-5, 1.e-5, 1.e-5, 1.e-5, 7.e-6, 6.e-6, 3.e-7],  color='lightgrey', alpha=0.7)

# draw vertical line Occ
ax.plot([51.5, 51.5], [0, 1e-5], color='grey', linestyle='--', lw=2)
ax.plot([54.5, 54.5], [0, 1e-5], color='grey', linestyle='--', lw=2)

# show legend
ax.set_xlabel("Volumetric water content", fontsize=12)
ax.set_ylabel("Air permeability coefficient (m/s)", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# adjust graph
ax.set_yscale("log")
ax.set_xlim([25, 65])
ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=100, decimals=0))

ax.set_xticks(np.arange(25, 66, 5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.set_ylim([1.e-7, 1.e-4])

ax.annotate(r'Occlusion''\n'
            r'$\theta_{w-occ}$ = 54-55%''\n'
            r'$\theta_{a-occ}$ = 8-7%',
            xy=(54.5, 1e-5), xytext=(55, 2.5e-5), color='black', size='12',
            arrowprops=dict(arrowstyle="fancy", color='black', connectionstyle="angle3,angleA=-90,angleB=180"))

ax.annotate(r'Pre-Occlusion''\n'
            r'$\theta_{w-preocc}$ = 51-52%''\n'
            r'$\theta_{a-preocc}$ = 11-10%',
            xy=(51.5, 1e-5), xytext=(41, 2.5e-5), color='black', size='12',
            arrowprops=dict(arrowstyle="fancy", color='black', connectionstyle="angle3,angleA=-90,angleB=0"))

ax.grid(which='major', color='lightgrey', linewidth=0.8)
ax.grid(axis='y', which='minor', color='lightgrey', linestyle='--')

figure = fig.add_axes([0.20, 0.15, 0.4, 0.4], anchor='SW', zorder=1) # tuple (left, bottom, width, height)
image = plt.imread('../0.Data/Figures/Kair 8in cell.png')
figure.imshow(image)
figure.axis('off')

# show graph
plt.savefig('../2.Figures/F2d_Kair.png', bbox_inches='tight', dpi=600)
plt.show()