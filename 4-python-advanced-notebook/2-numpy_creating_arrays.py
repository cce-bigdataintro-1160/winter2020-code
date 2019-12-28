#!/usr/bin/env python3

import numpy as np


# Define a function to pretty print the results
def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Creating an array and a matrix with arbitrary values
pretty_print('simple_array', np.array([1, 2]))
pretty_print('matrix', np.array([[1, 2], [1, 4], [1, 3]]))

# Creating pre-defined arrays and matrixes
pretty_print('range_array', np.arange(1, 15))
pretty_print('zeros_array', np.zeros(10))
pretty_print('zeros_matrix', np.zeros((5, 5)))
pretty_print('ones_matrix', np.ones((5, 5)))
pretty_print('sevens_matrix', np.ones((5, 5)) * 7)

# Creating random arrays and matrixes
pretty_print('random_array', np.random.rand(5))
pretty_print('random_int_array', np.random.randint(1, 100, 20))

pretty_print('random_matrix', np.random.rand(4, 4))
