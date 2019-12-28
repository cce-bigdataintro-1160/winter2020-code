import numpy as np

# 2 Create your first array with the elements [1,22.4,5,35,4,6.7,3,8,40] and print it. Experiment what the following
# functions do: ndim, shape, size and dtype
myarray = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])
print(myarray)
print(myarray.ndim)
print(myarray.shape)
print(myarray.size)
print(myarray.dtype)

# 3 Create your first matrix with the elements [['a', 'b'],['c', 'd'],[3, 3]] and print it. Experiment what the
# following functions do: ndim, shape, size and dtype
mymatrix = np.array([['a', 'b'], ['c', 'd'], [3, 3]])
print(mymatrix)
print(mymatrix.ndim)
print(mymatrix.shape)
print(mymatrix.size)
print(mymatrix.dtype)

# 4 Create numpy 1 dimension array using each of the functions arange and rand
range_array = np.arange(50)
rand_array = np.random.rand(50)

# 5 Create numpy 2 dimensions matrix using each of the functions zeros and rand
zero_matrix = np.zeros(50)
rand_matrix = np.random.rand(50, 50)

# 6 Create an array containing 20 times the value 7. Reshape it to a 4 x 5 Matrix
sevens_array = np.ones(20) * 7
sevens_matrix = sevens_array.reshape(4, 5)

# 7 Create a 6 x 6 matrix with all numbers up to 36, then print
range_array_2 = np.arange(36).reshape(6, 6)
print(range_array_2[0, 0])
print(range_array_2[0:2, :])
print(range_array_2[4:6, :])
print(range_array_2[2:4, :])
print(range_array_2[:, -1])
print(range_array_2[2:4, 2:4])
print(range_array_2[:, 0].mean())
