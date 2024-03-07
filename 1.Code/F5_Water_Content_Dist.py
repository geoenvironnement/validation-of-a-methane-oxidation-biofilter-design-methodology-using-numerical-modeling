import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

nbPts = 19

sns.set_theme(context="paper", style="ticks", palette=sns.color_palette("cividis", nbPts))
colors = sns.color_palette("cividis", nbPts)

df0 = pd.read_excel('../0.Data/Modelling_Results_UPPER.xlsx', sheet_name="S0")
df2 = pd.read_excel('../0.Data/Modelling_Results_UPPER.xlsx', sheet_name="S2")
df4 = pd.read_excel('../0.Data/Modelling_Results_UPPER.xlsx', sheet_name="S4")
df6 = pd.read_excel('../0.Data/Modelling_Results_UPPER.xlsx', sheet_name="S6")
df8 = pd.read_excel('../0.Data/Modelling_Results_UPPER.xlsx', sheet_name="S8")

dfCurve = [df0, df2, df4, df6, df8]
slope = ['0% Slope', '2% Slope', '4% Slope', '6% Slope', '8% Slope']

fig, axs = plt.subplots(5, sharex=True, figsize=(8, 7))

for df, j, title, col in zip(dfCurve, [0, 1, 2, 3, 4], slope, colors):

    axs[j].axvline(0.52, color='white', linestyle='-', lw=5, zorder=1)
    axs[j].fill_between([0.52, 0.54], [0, 0], [60, 60], color='darkblue', alpha=0.15, zorder=0)
    axs[j].fill_between([0.54, 0.6], [0, 0], [60, 60], color='firebrick', alpha=0.15, zorder=0)
    axs[j].fill_between([0, 0.52], [0, 0], [60, 60], color='forestgreen', alpha=0.15, zorder=0)
    axs[j].axvline(0.54, color='white', linestyle='-', lw=5, zorder=1)

    for i in range(1, nbPts + 1, 1): 
        if i == 1 or i == 5 or i == 19:
            sns.kdeplot(ax=axs[j], data=df['P%s' % str(i)].squeeze(), fill=True, label='Pos. %s' % str(i), multiple='layer', color=colors[i-1], linestyle='--', lw=3)            
        else:
            sns.kdeplot(ax=axs[j], data=df['P%s' % str(i)].squeeze(), fill=True, label='Pos. %s' % str(i), multiple='layer', color=colors[i-1])

    axs[j].set(xlabel='', ylabel='')#, title=title)
    axs[j].set_title(title, y=1.0, pad=-10, fontsize=10)
    #axs[j].legend(loc="upper left", prop={'size': 8.5})
    axs[j].set_xticks([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6])
    axs[j].xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
    axs[j].set_yticks([0, 10, 20, 30])
    axs[j].xaxis.set_tick_params(labelsize=12)
    axs[j].yaxis.set_tick_params(labelsize=12)
    axs[j].set_xlim([0.35, 0.6])
    axs[j].set_ylim([0, 30])
    axs[j].tick_params(left = False, labelleft = False)
    axs[4].tick_params(left = True, labelleft = True)

axs[0].text(0.53, 20, "Pre-Occ.\nRange", color='darkblue', weight='bold', fontsize=10, rotation=0, horizontalalignment='center')
axs[0].text(0.57, 20, " MOB Occluded", color='firebrick', weight='bold', fontsize=10, rotation=0, horizontalalignment='center')
axs[0].text(0.475, 20, "Unoccluded Zone", color='forestgreen', weight='bold', fontsize=10, rotation=0, horizontalalignment='center')

axs[4].text(0.5375, 25, "1", color='firebrick', weight='bold', fontsize=10, rotation=0, horizontalalignment='center')
axs[4].text(0.495, 25, "5", color='firebrick', weight='bold', fontsize=10, rotation=0, horizontalalignment='center')
axs[4].text(0.4525, 25, "19", color='firebrick', weight='bold', fontsize=10, rotation=0, horizontalalignment='center')

figure = fig.add_axes([0.13, 0.67, 0.3, 0.3], zorder=1)
image = plt.imread('../0.Data/Figures/Nodes Design.png')
figure.imshow(image)
figure.axis('off')

fig.supxlabel('Volumetric Water Content', fontsize=12)
fig.supylabel('\n''\n''Occurrence Frequency (4 years)', fontsize=12)

plt.savefig('../2.Figures/F5_ModelResults.png', bbox_inches='tight', dpi=600)
plt.show()