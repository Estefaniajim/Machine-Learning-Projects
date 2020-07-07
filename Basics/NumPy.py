import numpy as np
#Arrays
arr = np.array([[0, 1, 2], [3, 4, 5]],dtype=np.float32)#array is manually cast to np.float32
arr2 = np.array([0, 0.1, 2])#np.array upcasting
b = np.array([9, 8])
d = b.copy()
d[0] = 6 #this does not change b, only changes d
arr3 = np.array([0, 1, 2])
arr = arr.astype(np.float32) #casting




