import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

dfClimate = pd.read_excel('../0.Data/KITCHENERWATERLOO_2017-2021.xlsx')

fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()

ax1.bar(dfClimate['Date'], dfClimate['Rain_mm'], width=5, label="Precipitation", color="steelblue")

# adjust graph
myFmt = mdates.DateFormatter('%Y-%m')
ax1.xaxis.set_major_formatter(myFmt)

ax1.set_ylim([0, 70])
ax1.set_yticks(np.arange(0, 71, 10))

ax1.set_xlabel("Date (YYYY-MM)", fontsize=12)
ax1.set_ylabel("Equivalent Rainfall (mm)", fontsize=12)

group = dfClimate.groupby('Year')[['Rain_mm', 'ET_mm']].sum().astype(int)

ax1.text(pd.Timestamp('2017-07-01'), 67, r'$\Sigma$=' + str(group.iloc[0][1]) + ' mm', color = "firebrick", fontsize=10, horizontalalignment='center', weight='bold')
ax1.text(pd.Timestamp('2017-07-01'), 32.5, r'$\Sigma$=' + str(group.iloc[0][0]) + ' mm', color = "steelblue", fontsize=10, horizontalalignment='center', weight='bold')
#ax1.axvline(pd.Timestamp('2018-01-01'), color='grey', linestyle='--')

ax1.text(pd.Timestamp('2018-07-01'), 67, r'$\Sigma$=' + str(group.iloc[1][1]) + ' mm', color = "firebrick", fontsize=10, horizontalalignment='center', weight='bold')
ax1.text(pd.Timestamp('2018-07-01'), 32.5, r'$\Sigma$=' + str(group.iloc[1][0]) + ' mm', color = "steelblue", fontsize=10, horizontalalignment='center', weight='bold')
#ax1.axvline(pd.Timestamp('2019-01-01'), color='grey', linestyle='--')

ax1.text(pd.Timestamp('2019-07-01'), 67, r'$\Sigma$=' + str(group.iloc[2][1]) + ' mm', color = "firebrick", fontsize=10, horizontalalignment='center', weight='bold')
ax1.text(pd.Timestamp('2019-07-01'), 32.5, r'$\Sigma$=' + str(group.iloc[2][0]) + ' mm', color = "steelblue", fontsize=10, horizontalalignment='center', weight='bold')
#ax1.axvline(pd.Timestamp('2020-01-01'), color='grey', linestyle='--')

ax1.text(pd.Timestamp('2020-07-01'), 67, r'$\Sigma$=' + str(group.iloc[3][1]) + ' mm', color = "firebrick", fontsize=10, horizontalalignment='center', weight='bold')
ax1.text(pd.Timestamp('2020-07-01'), 32.5, r'$\Sigma$=' + str(group.iloc[3][0]) + ' mm', color = "steelblue", fontsize=10, horizontalalignment='center', weight='bold')
ax1.axvline(pd.Timestamp('2021-01-01'), color='grey', linestyle='--')

ax1.text(pd.Timestamp('2021-07-01'), 67, r'$\Sigma$=' + str(group.iloc[4][1]) + ' mm', color = "firebrick", fontsize=10, horizontalalignment='center', weight='bold')
ax1.text(pd.Timestamp('2021-07-01'), 32.5, r'$\Sigma$=' + str(group.iloc[4][0]) + ' mm', color = "steelblue", fontsize=10, horizontalalignment='center', weight='bold')

ax1.annotate('', xy=(pd.Timestamp('2018-07-01'), 45), xytext=(pd.Timestamp('2020-12-15'), 45), color='grey', arrowprops=dict(arrowstyle="-|>", color='grey'))
ax1.text(pd.Timestamp('2019-12-15'), 39, "Env. & Climate Change\nCanada (ECCC) Data", color = "grey", fontsize=10, horizontalalignment='right')
ax1.annotate('', xy=(pd.Timestamp('2021-01-15'), 45), xytext=(pd.Timestamp('2021-07-01'), 45), color='grey', arrowprops=dict(arrowstyle="<|-", color='grey'))
ax1.text(pd.Timestamp('2021-02-01'), 39, "Field\nData", color = "grey", fontsize=10)

ax2.annotate('', xy=(pd.Timestamp('2021-12-25'), 3.7), xytext=(pd.Timestamp('2021-08-15'), 3), color='firebrick', size='30', arrowprops=dict(arrowstyle="fancy", color='firebrick', connectionstyle="angle3,angleA=-90,angleB=180"))
ax1.annotate('', xy=(pd.Timestamp('2017-01-05'), 30), xytext=(pd.Timestamp('2017-05-01'), 25), color='steelblue', size='30', arrowprops=dict(arrowstyle="fancy", color='steelblue', connectionstyle="angle3,angleA=-90,angleB=180"))

ax1.set_xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2022-01-01'))

ax2.plot(dfClimate['Date'], dfClimate['ET_mm'], marker='', color='firebrick', linestyle='-', label='Evapotranspiration')

ax2.set_ylim([10, 0])
ax2.set_yticks(np.arange(10, -1, -1))
ax2.set_ylabel("Evapotranspiration (mm)", fontsize=12)

ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)
ax2.tick_params(axis='y', labelsize=12)

# show legend
#fig.legend(loc='upper left', bbox_to_anchor=(0.125, 0.93), ncol=2, frameon=False)

# show graph
plt.savefig('../2.Figures/F4_Climate.png', bbox_inches='tight', dpi=600)
plt.show()