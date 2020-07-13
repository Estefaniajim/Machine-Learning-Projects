import numpy as np

# Array accessing
arr = np.array([1, 2, 3, 4, 5])
num = arr[0]  # 1
arr = np.array([[6, 3], [0, 2]])
num = arr[0]  # [6, 3]

# Slicing
arr = np.array([1, 2, 3, 4, 5])
num = arr[:]  # [1, 2, 3, 4, 5]
num = arr[1:]  # [2, 3, 4, 5]
num = arr[2:4]  # [3, 4]
num = arr[:-1]  # [1, 2, 3, 4]
num = arr[-2:]  # [4, 5]
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
num = arr[:]  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
num = arr[1:]  # [[4, 5, 6], [7, 8, 9]]
num = arr[:, -1]  # [3, 6, 9]
num = arr[:, 1:]  # [[2, 3], [5, 6], [8, 9]]
num = arr[0:1, 1:]  # [[2, 3]]
num = arr[0, 1:]  # [2, 3]

# Argmin and argmax
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])
pos = np.argmin(arr[0])  # [-2, -1, -3] --> -3 --> 2
pos = np.argmax(arr[2])  # [-3, 9, 1] --> 9 --> 1
pos = np.argmin(arr)  # --> -6 --> 5
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])
pos = np.argmin(arr, axis=0)  # -3,-2,1 --> [2, 0, 1]
pos = np.argmin(arr, axis=1)  # -3,-6,-3 --> [2, 2, 0]
pos = np.argmax(arr, axis=-1)  # -1,5,9 --> [1, 1, 1]