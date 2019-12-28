#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Creating four arrays with 20 elements each
linear = np.arange(1, 20)
square = linear ** 2
log = np.log(linear)
random = np.random.randint(0, 100, 20)


## Method 1 - Creating figure and axes using subplots
fig, axes = plt.subplots(2, 2, figsize=(8,8))

axes[0][0].plot(linear)
axes[0][1].plot(square)
axes[1][0].plot(log)
axes[1][1].plot(random)
# print(axes)

## Method 2 - Creating figure using figure(), and then adding subplots on demand
# figure = plt.figure(figsize=(5,5))
#
# subplot1 = figure.add_subplot(2,2,1)
# subplot2 = figure.add_subplot(2,2,2)
# subplot3 = figure.add_subplot(2,2,3)
# subplot4 = figure.add_subplot(2,2,4)
#
# subplot1.plot(linear)
# subplot2.plot(square)
# subplot3.plot(log)
# subplot4.plot(random)

# Tight layout automatically tries to arrange axes within a figure
# plt.tight_layout()

plt.show()

plt.close()
