#!/usr/bin/env python3

import numpy as np


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Let's first create a sample array to check its functions
int_array = np.arange(0,40)

pretty_print('int_array', int_array)

# We can use mean, min, max and std to immediately extract stats on our datasets
pretty_print('int_array.mean()', int_array.mean())
pretty_print('int_array.min()', int_array.min())
pretty_print('int_array.max())', int_array.max())
pretty_print('int_array.std()', int_array.std())

# Let's reshape this array into a matrix
reshaped_int_matrix = int_array.reshape(5, 8)

# We can apply the very same operations on a numpy matrix
pretty_print('reshaped_int_matrix.mean()', reshaped_int_matrix.mean())
pretty_print('reshaped_int_matrix.min()', reshaped_int_matrix.min())
pretty_print('reshaped_int_matrix.max()', reshaped_int_matrix.max())
pretty_print('reshaped_int_matrix.std()', reshaped_int_matrix.std())

# We then can for example apply the same method to a row only
pretty_print('reshaped_int_matrix[1].mean()', reshaped_int_matrix[1].mean())
