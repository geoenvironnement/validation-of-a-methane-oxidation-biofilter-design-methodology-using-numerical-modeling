import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

# Data
dfReal = pd.read_excel('../0.Data/Field_Data_2021.xlsx', sheet_name="Real")

max_S8_100 = []
max_S8_95 = []
max_S8_90 = []
for j in [1, 3, 8, 10, 15]:
    max_S8_100.append(dfReal['R%i' % j].quantile(1))
    max_S8_95.append(dfReal['R%i' % j].quantile(0.95))
    max_S8_90.append(dfReal['R%i' % j].quantile(0.9))

fig, ax = plt.subplots(figsize=(8, 5))

# multiple line plots
dfx = [8, 7.5, 7, 5, 2.5]

plt.plot(dfx, max_S8_100, marker='x', markersize=5, color='#1b9e77', linestyle='--', label='Field $100^{th}$ percentile')
plt.plot(dfx, max_S8_95, marker='o', markersize=5, color='#d95f02', linestyle='-.', label='Field $95^{th}$ percentile')
plt.plot(dfx, max_S8_90, marker='^', markersize=5, color='#7570b3', linestyle=':', label='Field $90^{th}$ percentile')

plt.annotate(r'$100^{th}$ percentile',
            xy=(5, 0.551), xytext=(2.5, 0.57), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=-40,angleB=0"))

plt.annotate(r'$95^{th}$ percentile',
            xy=(8, 0.55), xytext=(7.75, 0.58), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=-90,angleB=180"))

plt.annotate(r'$90^{th}$ percentile',
            xy=(7, 0.519), xytext=(4.5, 0.49), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

# draw horizontal Occ
plt.fill_between([0, 10], [0, 0], 0.52, color='forestgreen', alpha=0.15, zorder=0)
plt.axhline(0.54, color='white', linestyle='-', lw=5, zorder=1)
plt.fill_between([0, 10], [0.52, 0.52], 0.54, color='darkblue', alpha=0.15, zorder=0)
plt.axhline(0.52, color='white', linestyle='-', lw=5, zorder=1)
plt.fill_between([0, 10], [0.54, 0.54], 0.7, color='firebrick', alpha=0.15, zorder=0)

# draw vertical 7.5m line
plt.axvline(7.5, color='red', linestyle='--', lw=3)
plt.annotate(r'Target LUGM', weight='bold',
            xy=(7.25, 0.44), xytext=(7.25, 0.44), color='k', size='10', rotation=90)

# show legend
#plt.legend(loc="lower left")
plt.xlabel("Length Along the Interface (m)", fontsize=12)
plt.ylabel("Field Maiximum Volumetric Water Content", fontsize=12)

plt.annotate(r'MOB Occluded', weight='bold',
            xy=(0.1, 0.57), xytext=(0.1, 0.57), color='firebrick', size='10')

plt.annotate(r'Pre-Occ. Range', weight='bold',
            xy=(0.1, 0.5275), xytext=(0.1, 0.5275), color='darkblue', size='10')

plt.annotate(r'Unoccluded Zone', weight='bold',
            xy=(0.1, 0.46), xytext=(0.1, 0.46), color='forestgreen', size='10')

# adjust graph
plt.xlim([0, 10])
plt.xticks(np.arange(0,11,1))
plt.ylim([0.4, 0.6])
plt.yticks(np.arange(0.4,0.61,0.05))

ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# show graph
plt.savefig('../2.Figures/F9_LUGM_Real.png', bbox_inches='tight', dpi=600)
plt.show()