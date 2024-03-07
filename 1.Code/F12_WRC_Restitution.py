import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import math

# Data
dfPsi = pd.read_excel('../0.Data/WRC_Restitution.xlsx', sheet_name="Psi")
dfPsi = dfPsi.drop(['Date'], axis=1)
dfVWC = pd.read_excel('../0.Data/WRC_Restitution.xlsx', sheet_name="Selected")
dfVWC = dfVWC.drop(['Date'], axis=1)

x = np.logspace(-4, 10, num=100, endpoint=True, base=10.0, dtype=None, axis=0)

def wrc(param):
    a, n, ksat, Qs, Qr = [param[0], param[1], param[2], param[3], param[4]]
    m = 1-(1/n)
    l = 0.5
    WRC = ((Qs - Qr) * (1 + (x * a) ** n) ** (-m) + Qr)
    return WRC

def kfct(param):
    a, n, ksat, Qs, Qr = [param[0], param[1], param[2], param[3], param[4]]
    m = 1-(1/n)
    l = 0.5
    Kfct = ksat * ((1 - ((a * x) ** (n * m)) * ((1 + ((a * x) ** n)) ** (-m))) ** 2) / ((1 + ((a * x) ** n)) ** (m * l)) / 100
    return Kfct

# soil parameters for van genuchten
compostMixUpper = [0.673, 1.292, 0.01, 0.62, 0.11] #a(1/kpa), n, Ksat(cm/s), Qs, Qr
compostMixMedian = [0.852, 1.445, 0.01, 0.62, 0.11] #a(1/kpa), n, Ksat(cm/s), Qs, Qr
compostMixLower = [1.730, 1.460, 0.01, 0.62, 0.11] #a(1/kpa), n, Ksat(cm/s), Qs, Qr

# Water Retention Curve
fig, ax1 = plt.subplots(figsize=(8, 5))

for i in ['95', '85']:
    dfPsi_new = dfPsi.reindex(columns=['L2-D%sp' % i,'L2,5-D%sp' % i, 'L3-D%sp' % i, 'L5-D%sp' % i, 'L7,5-D%sp' % i])
    dfVWC_new = dfVWC.reindex(columns=['L2-D%si' % i,'L2,5-D%si' % i, 'L3-D%si' % i, 'L5-D%si' % i, 'L7,5-D%si' % i])
    globals()['df%s' % i] = pd.DataFrame()
    X = dfPsi_new[['L2-D%sp' % i,'L2,5-D%sp' % i, 'L3-D%sp' % i, 'L5-D%sp' % i, 'L7,5-D%sp' % i]]
    Y = dfVWC_new[['L2-D%si' % i,'L2,5-D%si' % i, 'L3-D%si' % i, 'L5-D%si' % i, 'L7,5-D%si' % i]]
    globals()['df%sx' % i] = pd.concat([dfPsi_new['L2-D%sp' % i], dfPsi_new['L2,5-D%sp' % i], dfPsi_new['L3-D%sp' % i], dfPsi_new['L5-D%sp' % i], dfPsi_new['L7,5-D%sp' % i]], axis=0, ignore_index=True)
    globals()['df%sy' % i] = pd.concat([dfVWC_new['L2-D%si' % i], dfVWC_new['L2,5-D%si' % i], dfVWC_new['L3-D%si' % i], dfVWC_new['L5-D%si' % i], dfVWC_new['L7,5-D%si' % i]], axis=0, ignore_index=True)
    globals()['df%s' % i] = pd.DataFrame({'X': globals()['df%sx' % i], 'Y': globals()['df%sy' % i]})

ax1.plot(df95['X'], df95['Y'], color='#e41a1c', marker="s", markersize=4, linestyle="", label='Pos. 1, 3, 8, 10, 15')
ax1.plot(df85['X'], df85['Y'], color='#377eb8', marker=".", markersize=4, linestyle="", label='Pos. 2, 4, 9, 11, 16')

ax1.set_xlabel("Suction (kPa)", fontsize=12)
ax1.set_xticks([0.01, 0.01, 0.1, 1, 10, 100])
ax1.set_xscale("log")
ax1.set_xlim(0.01, 10000)

ax1.set_ylabel("Volumetric Water Content", fontsize=12)
ax1.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax1.set_yticks(np.arange(0, 0.71, 0.1))
ax1.set_ylim(0, 0.7)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# multiple line plots
ax1.plot(x, wrc(compostMixUpper), marker=None, color='grey', linestyle='--', linewidth=2, label='Compost Mix Upper')
ax1.plot(x, wrc(compostMixMedian), marker=None, color='black', linestyle='-', linewidth=2, label='Compost Mix Median')
ax1.plot(x, wrc(compostMixLower), marker=None, color='grey', linestyle='--', linewidth=2, label='Compost Mix Lower')

plt.annotate(r'Upper WRC',
            xy=(100, 0.26), xytext=(200, 0.31), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=-180,angleB=-90"))

plt.annotate(r'Mean WRC',
            xy=(10, 0.30), xytext=(1.1, 0.25), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

plt.annotate(r'Lower WRC',
            xy=(100, 0.16), xytext=(11, 0.11), color='k', size='10',
            arrowprops=dict(arrowstyle="fancy", color='k', connectionstyle="angle3,angleA=0,angleB=90"))

plt.annotate('Each point is a couple of VWC and Suction\nSee field instrumentation point number',
            xy=(100, 0.16), xytext=(0.011, 0.63), color='k', size='10')

plt.fill_between(x, wrc(compostMixUpper), wrc(compostMixLower), color='lightgrey')

plt.grid(which='major', color='grey', linewidth=0.8)
plt.grid(which='minor', color='lightgrey', linestyle='--')

figure = fig.add_axes([0.52, 0.63, 0.37, 0.37], anchor='SW', zorder=1) # tuple (left, bottom, width, height)
image = plt.imread('../0.Data/Figures/Restitution Loc.png')
figure.imshow(image)
figure.axis('off')

plt.savefig('../2.Figures/F12_Restitution.png', bbox_inches='tight', dpi=600)
plt.show()