import numpy as np

# checking the dimension of an array -> shape()
arr = np.array([[1,2,3],
                  [4,5,6]])
# print(arr.shape)


# checking the total number of element in an array

# print(arr.size)


# checking the dimension of an array -> ndim()
arr_1d  = np.array([1,2,3])
arr_2d  = np.array([[1,2,3],[4,5,6]])
arr_3d  = np.array([[1,2],[3,4],[5,6],[7,8]])

'''print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)'''

# checking the datatype of elements of an array

array = np.array([10,20,30.5,40])
# print(array.dtype)


# type conversion -> astype(type)

arr1 = np.array([1.2,2.5,3.8])
int_arr = arr1.astype(int)

print(int_arr)
print(int_arr.dtype)




