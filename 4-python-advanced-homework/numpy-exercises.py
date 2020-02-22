import numpy as np

# 1 - Create your first array with the elements [1,22.4,5,35,4,6.7,3,8,40] and print it. Experiment what the
# following functions do: ndim, shape, size and dtype.
my_array = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])
print(my_array)
print(f'my_array.ndim is {my_array.ndim}')
print(f'my_array.shape is {my_array.shape}')
print(f'my_array.size is {my_array.size}')
print(f'my_array.dtype is {my_array.dtype}')

# 2 - Create your first matrix with the elements [['a', 'b'],['c', 'd'],[3, 3]] and print it. Experiment what the
# following functions do: ndim, shape, size and dtype
my_matrix = np.array([['a', 'b'], ['c', 'd'], [3, 3]])
print(my_matrix)
print(f'my_matrix.ndim is {my_matrix.ndim}')
print(f'my_matrix.shape is {my_matrix.shape}')
print(f'my_matrix.size is {my_matrix.size}')
print(f'my_matrix.dtype is {my_matrix.dtype}')

# 3 - Create numpy 1 dimension array using each of the functions arange and rand
range_array = np.arange(0, 10)
print(f'range_array is {range_array}')

random_array = np.random.rand(10)
print(f'random_array is {random_array}')

# 4 - Create numpy 2 dimensions matrix using each of the functions zeros and rand
zeros_matrix = np.zeros((5, 5))
print(f'range_array is {zeros_matrix}')

random_matrix = np.random.rand(4, 4)
print(f'random_array is {random_matrix}')

# 5 - Create an array containing 20 times the value 7. Reshape it to a 4 x 5 Matrix
result_array = np.ones(20) * 7
reshaped_array = result_array.reshape(4,5)
print(reshaped_array)

# 6 - Create a 6 x 6 matrix with all numbers up to 36, then print:
matrix_to_slice = np.arange(1, 37).reshape(6, 6)
print(matrix_to_slice)
print(f'only the first element on it: {matrix_to_slice[0,0]}')
print(f'only the last 2 rows for it: {matrix_to_slice[4:6,:]}')
print(f'only the two mid columns and 2 mid rows for it: {matrix_to_slice[2:4,2:4]}')
print(f'the sum of values for each column: {matrix_to_slice.sum(axis=0)}')
