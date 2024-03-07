import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import make_interp_spline

dfReal = pd.read_excel('../0.Data/Field_Data_2021.xlsx', sheet_name="Real")
dfClimate = pd.read_excel('../0.Data/KITCHENERWATERLOO_2017-2021.xlsx')

i = 'R'

dfReal = dfReal.drop(['%s2' % i, '%s4' % i, '%s5' % i, '%s6' % i, '%s7' % i, '%s9' % i, '%s11' % i, '%s12' % i, '%s13' % i, '%s14' % i, '%s16' % i, '%s17' % i, '%s18' % i, '%s19' % i], axis=1)
dfReal = dfReal.rename(columns={'%s1' % i: 8, '%s3' % i: 7.5, '%s8' % i: 7, '%s10' % i: 5, '%s15' % i: 2.5})

fig, axs = plt.subplots(2, 1, sharex=True, figsize=(8, 5))


for i, j, color, line, marker, occ in zip([0.52, 0.54], [1, 0], ['black', 'black'], [':', ':'], ['x', 'x'], ['52', '54']):
    dfMax = pd.DataFrame([])
    dfMax.insert(0, 'Day', dfReal['Day'], True)

    dfReal[dfReal < i] = np.nan

    dfValues = dfReal.drop('Day', axis=1)

    dfMax['Max'] = dfValues.min(axis=1)
    dfMax['MaxPos'] = dfValues.idxmin(axis=1)
    dfMax['Day'] += 18627

    axs[j].plot(dfMax['Day'], dfMax['MaxPos'], marker=marker, color=color, linestyle=line, markersize=4, label='LUGM') # $\theta_w > \theta_{w-occ}$

    # adjust graph
    myFmt = mdates.DateFormatter('%b-%y')
    axs[j].xaxis.set_major_formatter(myFmt)

    axs[j].set_ylim([0, 10])
    axs[j].set_yticks(np.arange(0,11,2))

    axs[j].yaxis.set_minor_locator(MultipleLocator(1))

    # draw horizontal Occ
    axs[j].axhline(7.5, color='red', linestyle='--', lw=2, zorder=0)

    # text and fill
    axs[j].fill_between([15000, 20000], [8, 8], 10, color='firebrick', alpha=0.15, zorder=0)
    axs[j].axhline(8, color = 'white', linestyle='-', lw=5, zorder=1)
    axs[j].fill_between([15000, 20000], [2.5, 2.5], 8, color='forestgreen', alpha=0.15, zorder=0)
    axs[j].axhline(2.5, color = 'white', linestyle='-', lw=5, zorder=1)   
    axs[j].fill_between([15000, 20000], [0, 0], 2.5, color='firebrick', alpha=0.15, zorder=0)

    if j==0:
        axs[j].text(pd.Timestamp('2021-03-15'), 8.5, 'Uninstrumented\n(8 to 10 m)', color='dimgrey', fontsize=9, weight='bold', horizontalalignment='left')
        axs[j].text(pd.Timestamp('2021-01-15'), 0.75, 'Uninstrumented\n(Upmost 2,5 m)', color='dimgrey', fontsize=9, weight='bold', horizontalalignment='left')
        axs[j].text(pd.Timestamp('2021-10-15'), 6.8, 'Target LUGM', color='firebrick', weight='bold', fontsize=10)
    
        axs[j].text(pd.Timestamp('2021-10-01'), 8.75, r'Trigger: $\theta_{w-occ}$ = %s' %occ + ' %', color='k', fontsize=14, horizontalalignment='center')

    if j==1:
        axs[j].text(pd.Timestamp('2021-10-01'), 8.75, r'Trigger: $\theta_{w-preocc}$ = %s' %occ + ' %', color='k', fontsize=14, horizontalalignment='center')

    axs[j].set_xlim(pd.Timestamp('2021-01-01'), pd.Timestamp('2022-01-01'))    

    axs[j].tick_params(axis='x', labelsize=12)
    axs[j].tick_params(axis='y', labelsize=12)


    # right axis
    ax_rain = axs[j].twinx()
    rainfall = dfClimate['Rain_mm'].to_list()
    ax_rain.bar(dfClimate['Date'], rainfall, width=1.5)
    ax_rain.set_ylim([0, 100])
    ax_rain.tick_params(axis='y', labelsize=12)
    ax_rain.yaxis.set_minor_locator(MultipleLocator(10))
    
    if j==1:
        ax_rain.set_ylabel("                            Equivalent Rainfall (mm)", fontsize=12)

# arrows
axs[0].annotate(r'',
            xy=(pd.Timestamp('2021-05-01'), 8.5), xytext=(pd.Timestamp('2021-04-25'), 5.5), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='dimgrey', connectionstyle="angle3,angleA=45,angleB=135"))

axs[0].annotate(r'',
            xy=(pd.Timestamp('2021-01-25'), 2), xytext=(pd.Timestamp('2021-01-28'), 4.5), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='dimgrey', connectionstyle="angle3,angleA=-135,angleB=-45"))

# titles
fig.supxlabel("Date (MMM-YY)", fontsize=12)
fig.supylabel("            LUGM (m)", fontsize=12)

# figure
im = plt.imread('../0.Data/Figures/LUGM Real Nodes.png')
axs[0].imshow(im, extent=[18642, 18754, 3, 7], aspect='auto')

axs[1].legend(loc=(0.01, 0.275), markerscale=1.5, fontsize=12)

# show graph
fig.tight_layout()
fig.subplots_adjust(hspace=0.1)

plt.savefig('../2.Figures/F10_LUGM_T_Real.png', bbox_inches='tight', dpi=1000)
plt.show()