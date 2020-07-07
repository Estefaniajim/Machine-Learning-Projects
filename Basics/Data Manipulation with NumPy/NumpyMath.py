import numpy as np

# Arithmetic
arr = np.array([[1, 2], [3, 4]])
arr = arr + 1  # Add 1 to element values --> [[2, 3], [4, 5]]
arr = arr - 1.2  # Subtract element values by 1.2 --> [[-0.2, 0.8], [ 1.8, 2.8]]
arr = arr * 2  # Halve element values --> [[2, 4], [6, 8]]
arr = arr / 2  # Integer division (half) --> [[0.5, 1. ], [1.5, 2. ]]
arr = arr // 2  # Square element values --> [[0, 1], [1, 2]]
arr = arr ** 2  # Square element values --> [[ 1, 4], [ 9, 16]]
arr = arr ** 0.5  # Square root element values --> [[1. , 1.41421356], [1.73205081, 2. ]]
# performing arithmetic on NumPy arrays does not change the original array

# Non-linear functions
arr2 = np.array([[1, 2], [3, 4]])
arr2 = np.exp(arr2)  # Raised to power of e --> [[ 2.71828183, 7.3890561 ], [20.08553692, 54.59815003]]
arr2 = np.exp2(arr2)  # Raised to power of 2 --> [[ 2., 4.], [ 8., 16.]]
arr2 = np.log(arr2)  # Natural logarithm --> [[0. , 0.69314718], [1.09861229, 1.38629436]]
arr2 = np.log2(arr2)  # Base 2 logarithm --> [[0. 1. ] [1.5849625 2. ]]
arr2 = np.log10(arr2)  # Base 10 logarithm --> [[0. , 0.30103 ], [0.47712125, 0.60205999]]
arr3 = np.array([[1, 2], [3, 4]])
arr3 = np.power(3, arr3)  # Raise 3 to power of each number in arr --> [[ 3, 9], [27, 81]]
arr4 = np.array([[10.2, 4], [3, 5]])
arr4 = np.power(arr4, arr3)  # Raise arr2 to power of each number in arr --> [[ 10.2, 16. ], [ 27. , 625.

# Matrix multiplication
arr5 = np.array([1, 2, 3])
arr6 = np.array([-3, 0, 10])
dot = np.matmul(arr5, arr6)  #  When both inputs are 1-D, the output is the dot product --> 27
arr7 = np.array([[1, 2], [3, 4], [5, 6]])
arr8 = np.array([[-1, 0, 1], [3, 2, -4]])
matMul = np.matmul(arr7, arr8)  # [[ 5, 4, -7], [ 9, 8, -13], [ 13, 12, -19]]
matMul2 = np.matmul(arr4, arr3)  # [[ 4, 4], [-11, -10]]
# The dimensions of the two input matrices must be valid for a matrix multiplication



