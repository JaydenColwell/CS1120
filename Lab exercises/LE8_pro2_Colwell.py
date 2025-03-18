import numpy as np

# First array prints max, min, total sum, and cumulative sums for rows.
array1 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(f'Array 1: {array1}')
print(f'Max: {np.max(array1)}')
print(f'Min: {np.min(array1)}')
print(f'Sum: {np.sum(array1)}')
print(f'cumsum: {np.cumsum(array1, axis=1)}\n')

# Second array prints flatten, ravel, and original versions.
array2 = np.array([[1,2,4],
                   [8,16,32]])
print(f'flattened: {np.ndarray.flatten(array2)}')
print(f'ravel: {np.ndarray.ravel(array2)}')
print(f'Regular: {array2}')