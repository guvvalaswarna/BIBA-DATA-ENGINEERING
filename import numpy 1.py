import numpy as np
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)
sliced_arr = arr[:2, ::2]
print ("Array :\n", sliced_arr)
Index_arr = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices :\n", Index_arr)