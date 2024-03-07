import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dfData = pd.DataFrame({'x': [0, 0], 'y': [0, 0]})

sns.set(rc = {'figure.figsize':(8, 6)}, font_scale=1)

cmap = sns.color_palette('RdBu_r', n_colors = 16)
hmap = sns.heatmap(dfData, cmap=cmap, vmin=-0.2, vmax=0.2, cbar=True, cbar_kws={'label': r'$\theta_{Model}-\theta_{Field}$'})

plt.savefig('../2.Figures/F11_Color_Map.png', bbox_inches='tight', dpi=600)