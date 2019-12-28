#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Creating four arrays with 20 elements each
linear = np.arange(1, 20) # 1 to 20
square = linear ** 2      # 1 to 400
log = np.log(linear)      # 1 to 3
random = np.random.randint(0, 100, 20) # 1 to 100

# Plotting all four arrays with plot
plt.plot(linear)
plt.plot(square)
plt.plot(log)
plt.plot(random)

# Cleaning the figure with clf
# plt.clf()

# The plot function also allows for two parameters to be passed X, y
# plt.plot(log, square)

# Setting title and labels
plt.title('Linear Plot')
plt.xlabel('Index')
plt.ylabel('Linear Y')

# Show displays figures in a separate window
plt.show()

# Closing the used resources
plt.close()
