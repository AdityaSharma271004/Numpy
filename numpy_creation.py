# importing numpy
import numpy as np
arr = np.array([1,2,3])
#print(arr)

#with default values
zeros_array = np.zeros(3)
# print(zeros_array)

#one shape
ones_array = np.ones((2,3))
# print(ones_array)

# full(shape,value)
filled_array = np.full((2,2),7)
# print(filled_array)

# creating sequences of numbers in numpy
# arange()
# arange(start,stop,step)

array = np.arange(1,10,2)
# print(array)

# creating idetity matrix
# eye(size)

identity_matrix = np.eye(3)
print(identity_matrix)


