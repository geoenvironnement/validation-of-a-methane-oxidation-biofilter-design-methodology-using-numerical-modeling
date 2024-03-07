import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from scipy.interpolate import make_interp_spline

model = 'UPPER'

for i in [2, 6, 8]:
    globals()['df_S%s' % i] = pd.read_excel('../0.Data/Modelling_Results_%s.xlsx' % model, sheet_name='S%s' % i, header=0)
    globals()['df_S%s' % i].reset_index(inplace=True, drop=True)

    globals()['df_S%s' % i]['Day'] += 17167

    headers = ['Day', 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5]
    globals()['df_S%s' % i] = globals()['df_S%s' % i].set_axis(headers, axis=1, copy=False)

    globals()['max_S%s' % i] = pd.DataFrame([])
    globals()['max_S%s' % i].insert(0, 'Day', globals()['df_S%s' % i]['Day'], True)

    globals()['df_S%s' % i][globals()['df_S%s' % i] < 0.53] = np.nan

    globals()['df_S%s' % i].drop('Day', inplace=True, axis=1)

    globals()['max_S%s' % i]['Max'] = globals()['df_S%s' % i].min(axis=1)
    globals()['max_S%s' % i]['MaxPos'] = globals()['df_S%s' % i].idxmin(axis=1)

    globals()['max_S%s' % i] = globals()['max_S%s' % i].fillna(10)

    X_Y_Spline = make_interp_spline(globals()['max_S%s' % i]['Day'], globals()['max_S%s' % i]['MaxPos'])
    globals()['X_%s' % i] = np.linspace(globals()['max_S%s' % i]['Day'].min(), globals()['max_S%s' % i]['Day'].max(), 1000)
    globals()['Y_%s' % i] = X_Y_Spline(globals()['X_%s' % i])

fig, ax = plt.subplots(figsize=(8, 5))
plt.plot(X_2, Y_2, marker='', color='#ca0020', linestyle='--', label='2% Slope')
plt.plot(X_6, Y_6, marker='', color='#0571b0', linestyle='-.', label='6% Slope')
plt.plot(X_8, Y_8, marker='', color='k', linestyle='-', label='8% Slope')

# adjust graph
myFmt = mdates.DateFormatter('%b-%y')
ax.xaxis.set_major_formatter(myFmt)
plt.ylim([0, 10])
plt.yticks(np.arange(0,11,1))

# draw horizontal Occ
plt.fill_between([0, 20000], [7.5, 7.5], 10, color='forestgreen', alpha=0.15, zorder=0)
plt.axhline(7.5, color='white', linestyle='-', lw=5, zorder=1)
plt.text(pd.Timestamp('2019-09-01'), 8, 'Bottom-most''\n''Zone''\n''2.5 m', horizontalalignment='center', color='forestgreen', weight='bold', fontsize=8)

plt.fill_between([0, 20000], [0, 0], 7.5, color='firebrick', alpha=0.15, zorder=0)
plt.text(pd.Timestamp('2019-09-01'), 4, 'Upper-most''\n''Zone''\n''\n''7.5 m''\n''Unrestricted gas\nflow zone', horizontalalignment='center', color='firebrick', weight='bold', fontsize=8)

plt.xlim(pd.Timestamp('2018-01-01'), pd.Timestamp('2021-01-01'))

# show legend
plt.legend(loc="lower right")
plt.xlabel("Date (MMM-YY)", fontsize=12)
plt.ylabel("LUGM (m)", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# show graph
plt.savefig('../2.Figures/F7_LUGM_T.png', bbox_inches='tight', dpi=600)
plt.show()