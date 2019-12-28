#!/usr/bin/env python3

import os

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/wine.data',
                 sep=',',
                 header=None)

df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids',
              'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
              'proline']

os.makedirs('plots/8-matplotlib_multiple_plot_axes', exist_ok=True)

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# This time we plot multiple plots on the same axes, to get some perspective on their comparisons
# The size parameter can be either a fixed value or another columns as in here
axes.scatter(df['alcohol'], df['malic_acid'], s=(df['color_intensity']) ** 2.5,
             label=f'Alcohol to Malic Acid', color='orange', marker='o', edgecolors='w', alpha=0.7)

axes.set_xlabel(f'Alcohol')
axes.set_ylabel(f'Malic Acid')
axes.set_title(f'Alcohol, Malic Acid and Color Intensity (Size)')

axes.legend()
plt.savefig(f'plots/8-matplotlib_multiple_plot_axes/multiplot_scatter_with_size.png', dpi=300)
plt.close()
