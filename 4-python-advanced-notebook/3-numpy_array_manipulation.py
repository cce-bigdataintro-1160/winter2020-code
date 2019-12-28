#!/usr/bin/env python3

import numpy as np


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Let's first create a sample array to do some manipulation
int_array = np.arange(0, 40)

# Extracting arrays shape and information
pretty_print('array shape', int_array.shape)
pretty_print('array type', int_array.dtype)

# Slicing arrays - selecting subsets of the arrays
pretty_print('int_array', int_array)
pretty_print('slice_array1', int_array[4:14])
pretty_print('slice_array2', int_array[:])
pretty_print('slice_array3', int_array[5:-5])

# Reshaping Arrays - the reshape function allows us to transform arrays into matrices
reshaped_int_matrix = int_array.reshape(5, 8)

pretty_print('matrix shape', reshaped_int_matrix.shape)
pretty_print('matrix type', reshaped_int_matrix.dtype)

pretty_print('reshaped_random_int_matrix', reshaped_int_matrix)
pretty_print('slice_matrix1', reshaped_int_matrix[1:3, 3:5])
pretty_print('slice_matrix2', reshaped_int_matrix[0:3, :])
pretty_print('slice_matrix3', reshaped_int_matrix[:, 2:3])

# Filtering arrays by a condition
pretty_print('filtered_matrix', reshaped_int_matrix[reshaped_int_matrix > 10])

# Multiplying arrays
pretty_print('multiplied_matrix', reshaped_int_matrix * 2)
