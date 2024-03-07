import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import math

x = np.logspace(-4, 10, num=100)

def wrc(param):
    a, n, ksat, Qs, Qr = [param[0], param[1], param[2], param[3], param[4]]
    m = 1-(1/n)
    l = 0.5
    WRC = ((Qs - Qr) * (1 + (x * a) ** n) ** (-m) + Qr) * 100 #for results in %
    return WRC

def kfct(param):
    a, n, ksat, Qs, Qr = [param[0], param[1], param[2], param[3], param[4]]
    m = 1-(1/n)
    l = 0.5
    Kfct = ksat * ((1 - ((a * x) ** (n * m)) * ((1 + ((a * x) ** n)) ** (-m))) ** 2) / ((1 + ((a * x) ** n)) ** (m * l)) / 100
    return Kfct

# soil parameters for van genuchten
filterSand = [0.368, 3.961, 0.009, 0.35, 0.02] #a(1/kpa), n, Ksat(cm/s), Qs, Qr
compostMixUpper = [0.673, 1.292, 0.01, 0.62, 0.11] #a(1/kpa), n, Ksat(cm/s), Qs, Qr
compostMixMedian = [0.852, 1.445, 0.01, 0.62, 0.11] #a(1/kpa), n, Ksat(cm/s), Qs, Qr
compostMixLower = [1.730, 1.460, 0.01, 0.62, 0.11] #a(1/kpa), n, Ksat(cm/s), Qs, Qr

fig, axs = plt.subplots(2, 1, sharex=True, figsize=(6, 8))

# Water Retention Curve
# multiple line plots
axs[0].plot(x, wrc(filterSand), marker=None, color='maroon', linestyle='dotted', linewidth=2, label='Filter Sand')
axs[0].plot(x, wrc(compostMixUpper), marker=None, color='grey', linestyle='--', linewidth=2, label='Upper WRC')
axs[0].plot(x, wrc(compostMixMedian), marker=None, color='black', linestyle='-', linewidth=2, label='Mean WRC')
axs[0].plot(x, wrc(compostMixLower), marker=None, color='grey', linestyle='--', linewidth=2, label='Lower WRC')

axs[0].fill_between(x, wrc(compostMixUpper), wrc(compostMixLower), color='lightgrey', alpha=0.7)

# show legend
axs[0].set_ylabel("Volumetric water content\n", fontsize=12)
axs[0].yaxis.set_label_coords(-0.1,0.5)

# adjust graph
axs[0].set_xscale("log")
axs[0].set_xlim([1.e-2, 1.e4])
axs[0].set_ylim([0, 70])
axs[0].yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100))

axs[0].grid(which='major', color='grey', linewidth=0.8)
axs[0].grid(which='minor', color='lightgrey', linestyle='--')

axs[0].annotate(r'Upper WRC',
            xy=(3, 49), xytext=(10, 55), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=-180,angleB=-90"))

axs[0].annotate(r'Mean WRC',
            xy=(4, 39), xytext=(11, 45), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

axs[0].annotate(r'Lower WRC',
            xy=(0.7, 50), xytext=(0.03, 41), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

axs[0].annotate(r'Filter Sand',
            xy=(3, 18), xytext=(0.1, 15), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

# Hydraulic conductivity function
# multiple line plots
axs[1].plot(x, kfct(filterSand), marker=None, color='maroon', linestyle='dotted', linewidth=2, label='Filter Sand')
axs[1].plot(x, kfct(compostMixUpper), marker=None, color='grey', linestyle='--', linewidth=2, label='Upper WRC')
axs[1].plot(x, kfct(compostMixMedian), marker=None, color='black', linestyle='-', linewidth=2, label='Mean WRC')
axs[1].plot(x, kfct(compostMixLower), marker=None, color='grey', linestyle='--', linewidth=2, label='Lower WRC')

axs[1].fill_between(x, kfct(compostMixUpper), kfct(compostMixLower), color='lightgrey', alpha=0.7)

# show legend
axs[1].set_xlabel("Suction (kPa)", fontsize=12)
axs[1].xaxis.set_label_coords(0.5,-0.075)
axs[1].set_ylabel("Hydraulic conductivity (m/s)\n", fontsize=12)
axs[1].yaxis.set_label_coords(-0.1,0.5)

# adjust graph
axs[1].set_xscale("log")
axs[1].set_yscale("log")
axs[1].set_xlim([1.e-2, 1.e4])
axs[1].set_ylim([1.e-13, 1.e-3])
axs[1].set_yticks(np.logspace(-13, -3, num=11))

axs[1].grid(which='major', color='grey', linewidth=0.8)
axs[1].grid(which='minor', color='lightgrey', linestyle='--')

axs[1].tick_params(axis='x', labelsize=12)
axs[1].tick_params(axis='y', labelsize=12)
axs[0].tick_params(axis='y', labelsize=12)

axs[1].annotate(r'Upper WRC',
            xy=(60, 2e-10), xytext=(150, 6e-10), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=-180,angleB=-90"))

axs[1].annotate(r'Mean WRC',
            xy=(100, 1e-11), xytext=(250, 3e-11), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

axs[1].annotate(r'Lower WRC',
            xy=(20, 1e-10), xytext=(0.7, 2e-11), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

axs[1].annotate(r'Filter Sand',
            xy=(3, 1e-5), xytext=(9, 4e-5), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))


# show graph
fig.tight_layout()
fig.subplots_adjust(hspace=0.07)
plt.savefig('../2.Figures/F2ab_WRCKfct.png', bbox_inches='tight', dpi=600)
plt.show()