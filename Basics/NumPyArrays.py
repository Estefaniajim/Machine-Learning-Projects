import numpy as np

arr = np.array([[0, 1, 2], [3, 4, 5]], dtype=np.float32)  # array is manually cast to np.float32
arr2 = np.array([0, 0.1, 2])  # np.array upcasting
b = np.array([9, 8])
d = b.copy()
d[0] = 6  # this does not change b, only changes d
arr3 = np.array([0, 1, 2])
arr3 = arr3.astype(np.float32)  # casting
arr4 = np.array([np.nan, 1, 2])  # nan is a filler value for incomplete data, nan cannot take int data
arr5 = np.array([np.inf, 5])  # infinite positive value
arr6 = np.array([-np.inf, 5])  # negative infinite value
# infinite values cannot take int data
