import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

fig, ax = plt.subplots(figsize=(8, 5))

for model, line, color, name in zip(['UPPER', 'MEDIAN', 'LOWER'], ['-', '--', '-.'], ['#1b9e77', '#d95f02', '#7570b3'], ['Upper WRC', 'Mean WRC', 'Lower WRC']):
    for i in [0, 2, 4, 6, 8]:
        globals()['df_S%s' % i] = pd.read_excel('../0.Data/Modelling_Results_%s.xlsx' % model, sheet_name='S%s' % i, header=0)
        globals()['df_S%s' % i] = globals()['df_S%s' % i][globals()['df_S%s' % i]['Day'] > 365]
        globals()['df_S%s' % i] = globals()['df_S%s' % i].drop('Day', axis=1)
        globals()['max_S%s' % i] = globals()['df_S%s' % i].quantile(1) # max value, could be interesting to evaluate sensitivity by using 99th quantile

    # multiple line plots
    dfx = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5]

    plt.plot(0, 0, marker='', linestyle='', label=name) # for column titles
    plt.plot(dfx, max_S0, marker='x', color=color, linestyle=line, label='0% Slope')
    #plt.plot(dfx, max_S2, marker='^', color=color, linestyle=line, label='2% Slope')
    plt.plot(dfx, max_S4, marker='s', color=color, linestyle=line, label='4% Slope')
    plt.plot(dfx, max_S6, marker='D', color=color, linestyle=line, label='6% Slope')
    plt.plot(dfx, max_S8, marker='o', color=color, linestyle=line, label='8% Slope')

# draw horizontal Occ
plt.fill_between([0, 10], [0, 0], 0.52, color='forestgreen', alpha=0.15, zorder=0)
plt.axhline(0.54, color='white', linestyle='-', lw=5, zorder=1)
plt.fill_between([0, 10], [0.52, 0.52], 0.54, color='darkblue', alpha=0.15, zorder=0)
plt.axhline(0.52, color='white', linestyle='-', lw=5, zorder=1)
plt.fill_between([0, 10], [0.54, 0.54], 0.7, color='firebrick', alpha=0.15, zorder=0)

# show legend
plt.legend(loc="lower right", ncol=3, prop={'size': 8})
plt.xlabel("Length Along the Interface (m)", fontsize=12)
plt.ylabel("Maximum Volumetric Water Content", fontsize=12)

plt.annotate(r'MOB Occluded', weight='bold',
            xy=(0.1, 0.57), xytext=(0.1, 0.57), color='firebrick', size='10')

plt.annotate(r'Pre-Occ. Range', weight='bold',
            xy=(0.1, 0.5275), xytext=(0.1, 0.5275), color='darkblue', size='10')

plt.annotate(r'Unoccluded Zone', weight='bold',
            xy=(0.1, 0.38), xytext=(0.1, 0.38), color='forestgreen', size='10')

plt.annotate(r'Upper WRC',
            xy=(9.5, 0.555), xytext=(8.5, 0.585), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=-90"))

plt.annotate(r'Mean WRC',
            xy=(9.5, 0.50), xytext=(8.5, 0.45), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

plt.annotate(r'Lower WRC',
            xy=(9.5, 0.42), xytext=(8.5, 0.37), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

# adjust graph
plt.xlim([0, 10])
plt.xticks(np.arange(0,11,1))
plt.ylim([0.3, 0.6])
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# show graph
plt.savefig('../2.Figures/F6_LUGM.png', bbox_inches='tight', dpi=600)
plt.show()