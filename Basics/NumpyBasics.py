import numpy as np

# Ranged data
arr = np.arange(5)  # [0, 1, 2, 3, 4] ,n --> [0,n)
arr2 = np.arange(5.1)  # [0., 1., 2., 3., 4., 5.]
arr3 = np.arange(-1, 4)  # [-1, 0, 1, 2, 3], m,n --> [m,n)
arr4 = np.arange(-1.5, 4, 2)  # [-1.5, 0.5, 2.5] m,s,n --> [m,n) using step size of s
# np.arange can perform upcasting with dtype
arr5 = np.linspace(5, 11, num=4)  # [ 5., 7., 9., 11.]
arr6 = np.linspace(5, 11, num=4, endpoint=False)  # [5. , 6.5, 8. , 9.5]
arr7 = np.linspace(5, 11, num=4, dtype=np.int32)  # [ 5, 7, 9, 11], dtype=int32
# The end of the range is inclusive for np.linspace, unless the keyword argument endpoint is set to False

# Reshaping data
arr8 = np.arange(8)  # [0 1 2 3 4 5 6 7]
reshaped_arr = np.reshape(arr8, (2, 4))  # (2, 4) --> [[0, 1, 2, 3], [4, 5, 6, 7]]
reshaped_arr2 = np.reshape(arr, (-1, 2, 2))  # (2, 2, 2) --> [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
flattened = reshaped_arr.flatten()  # (2, 4) --> (8,), [0, 1, 2, 3, 4, 5, 6, 7]

# Transposing
arr9 = np.reshape(arr8, (4, 2))  # [[0, 1], [2, 3], [4, 5], [6, 7]]
transposed = np.transpose(arr9)  # (4, 2) --> (2, 4), [[0, 2, 4, 6], [1, 3, 5, 7]]
arr10 = np.arange(24)  # [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
arr10 = np.reshape(arr10, (3, 4, 2))  # [[[ 0 1] [ 2 3] [ 4 5] [ 6 7]]
transposed2 = np.transpose(arr10, axes=(1, 2, 0))
# (3, 4, 2) --> (4, 2, 3) [[[ 0 8 16] [ 1 9 17]]
#                         [[ 2 10 18] [ 3 11 19]]
#                         [[ 4 12 20] [ 5 13 21]]
#                         [[ 6 14 22] [ 7 15 23]]]

# Zeros and ones
arr11 = np.zeros(4)  # [0., 0., 0., 0.]
arr12 = np.ones((2, 3))  # [[1., 1., 1.], [1., 1., 1.]]
arr13 = np.ones((2, 3), dtype=np.int32)  # [[1, 1, 1], [1, 1, 1]]
arr14 = np.array([[1, 2], [3, 4]])  # [[1 2] [3 4]]
arr14 = np.zeros_like(arr14) # [[0, 0], [0, 0]]
arr15 = np.array([[0., 1.], [1.2, 4.]])  # [[0. 1. ] [1.2 4. ]]
arr15 = np.ones_like(arr15)  # [[1., 1.], [1., 1.]]
arr15 = np.ones_like(arr15, dtype=np.int32)  # [[1, 1], [1, 1]]


