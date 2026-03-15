# how to access the element 
'''
array[index] #1d array
array[row,column] #2d array
'''

import numpy as np
arr = np.array([10,20,30,40,50])

'''print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[-1])'''


# how to slice
'''slicing
array[start:stop:step]
'''

# print(arr[1:3:1])
# print(arr[::-1])

 
'''
 fancy indexing -> selecting multiple elements at once

 print(arr[[0,2,4]]) -> it gives the 0th, 2nd and 4th index elements.

'''


# Boolean Masking or filtering

print(arr[arr>35])



