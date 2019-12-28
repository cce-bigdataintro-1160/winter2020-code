#!/usr/bin/env python3

import os

import matplotlib.pyplot as plt
import numpy as np

linear = np.arange(1, 20)
log = np.log(linear)

# The plt style describes a theme for our charts, other examples include:
# Solarize_light2, bmh,grayscale, dark_background, ggplot
# https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html
plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# When creating plots there are several parameters we can use to optimize the visualization
# https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html
# https://matplotlib.org/api/markers_api.html
axes.plot(log, label='Log', color='blue', linestyle='--', linewidth=2, alpha=0.6, marker='o')
axes.set_title('Log Plot')
axes.set_xlabel('Index')
axes.set_ylabel('Linear')
axes.legend()

os.makedirs('plots/5-matplotlib_customizing_plots', exist_ok=True)

plt.savefig('plots/5-matplotlib_customizing_plots/customized_plot.png', dpi=300)

plt.close()
