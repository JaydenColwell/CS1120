import numpy as np

array_a = np.array([[1,2,1],[7,5,3],[9,4,8]])
print(array_a)
array_b = array_a[[0,1,2],[0,1,2]]
print(array_b)
array_a[0,0] = 12
array_a[1,1] -= 1
array_a[2,2] -=1
print(array_a)
array_c = np.array([[[0,1,2,3],[4,5,6,7], [8,9,10,11]],[[2,13,14,15],[16,17,18,19],[20,21,22,23]]])
print(array_c)
