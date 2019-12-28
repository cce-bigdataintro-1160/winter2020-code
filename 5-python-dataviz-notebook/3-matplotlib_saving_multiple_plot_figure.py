#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

# Creating four arrays with 20 elements each
linear = np.arange(1, 20)
square = linear ** 2
log = np.log(linear)
random = np.random.randint(0, 100, 20)

# The figsize parameter allows us to configure the figure size in inches
fig, axes = plt.subplots(2, 3, figsize=(10, 5))

# Selectively plotting the axes
axes[0][0].plot(linear)
axes[0][1].plot(square)
axes[0][2].plot(log)
axes[1][0].plot(random)
axes[1][1].plot(log)
axes[1][2].plot(random)

plt.tight_layout()

# It's a good practice to organize your saved plots in directories
os.makedirs('plots/3-matplotlib_saving_multiple_plot_figure', exist_ok=True)

# We can save figures using savefig
plt.savefig('plots/3-matplotlib_saving_multiple_plot_figure/plot.png', dpi=300)
plt.savefig('plots/3-matplotlib_saving_multiple_plot_figure/plot.svg', dpi=300)
plt.savefig('plots/3-matplotlib_saving_multiple_plot_figure/plot.pdf', dpi=300)

plt.close()
