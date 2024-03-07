import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import seaborn as sns

sns.set_theme(context="paper", style="ticks")


dfLower = pd.read_excel('../0.Data/Modelling_Results_LOWER.xlsx', sheet_name="S8_2021")
dfMedian = pd.read_excel('../0.Data/Modelling_Results_MEDIAN.xlsx', sheet_name="S8_2021")
dfUpper = pd.read_excel('../0.Data/Modelling_Results_UPPER.xlsx', sheet_name="S8_2021")
dfReal = pd.read_excel('../0.Data/Field_Data_2021.xlsx', sheet_name="Real")

columns = ['Day', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']


dfLower.columns = columns
dfMedian.columns = columns
dfUpper.columns = columns
dfReal.columns = columns

dfLower = dfLower.subtract(dfReal)
dfLower['Day'] = np.array(range(1,366))
dfLower = dfLower[['Day', '1', '3', '8', '10', '15', '2', '4', '9', '11', '16', '5', '12', '17', '6', '13', '18', '7', '14', '19']]

dfMedian = dfMedian.subtract(dfReal)
dfMedian['Day'] = np.array(range(1,366))
dfMedian = dfMedian[['Day', '1', '3', '8', '10', '15', '2', '4', '9', '11', '16', '5', '12', '17', '6', '13', '18', '7', '14', '19']]

dfUpper = dfUpper.subtract(dfReal)
dfUpper['Day'] = np.array(range(1,366))
dfUpper = dfUpper[['Day', '1', '3', '8', '10', '15', '2', '4', '9', '11', '16', '5', '12', '17', '6', '13', '18', '7', '14', '19']]

dfLower = dfLower[['2', '4', '9', '11', '16']]
dfMedian = dfMedian[['2', '4', '9', '11', '16']]
dfUpper = dfUpper[['2', '4', '9', '11', '16']]

dfData = pd.concat([dfLower, dfMedian, dfUpper], axis=1)

dfData = dfData.transpose()

sns.set(rc = {'figure.figsize':(8, 6), 'axes.facecolor':'grey', 'grid.color': 'grey'}, font_scale=1)

yLabel = ['2', '4', '9', '11', '16', '2', '4', '9', '11', '16', '2', '4', '9', '11', '16']
xLabel = [*range(0, 366, 14)]

cmap = sns.color_palette('RdBu_r', n_colors = 16)
hmap = sns.heatmap(dfData, cmap=cmap, xticklabels=xLabel, yticklabels=yLabel, vmin=-0.2, vmax=0.2, cbar=False, cbar_kws={'label': r'$\theta_{Model}-\theta_{Field}$'}, mask=dfData.isna())

hmap.set_xticks(xLabel)
hmap.set_xticklabels(xLabel)

hmap.set(xlabel='Julian Day (2021)', ylabel="Instrumentation Points")
hmap.invert_yaxis()
hmap.tick_params(left=True, bottom=True)
hmap.hlines([5, 10], xmin=-10, xmax=370, color='white', lw=5)

plt.yticks(rotation=0)
plt.subplots_adjust(bottom=0.2)
plt.savefig('../2.Figures/F11b_Heatmap_85.png', bbox_inches='tight', dpi=600)
plt.show()