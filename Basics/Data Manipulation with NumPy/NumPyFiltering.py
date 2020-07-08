import numpy as np

# Filtering data
arr = np.array([[0, 2, 3],
                [1, 3, -6],
                [-3, -2, 1]])
data = arr == 3  # [[False, False, True], [False, True, False], [False, False, False]]
data = arr > 0  # [[False, True, True], [ True, True, False], [False, False, True]]
data = arr != 1  # [[ True, True, True], [False, True, True], [ True, True, False]]
data = ~(arr != 1)  # [[False, False, False], [ True, False, False], [False, False, True]]
arr2 = np.array([[0, 2, np.nan],
                [1, np.nan, -6],
                [np.nan, -2, 1]])
data = np.isnan(arr2)  # [[False, False, True], [False, True, False], [ True, False, False]]

# Filtering in NumPy
data = np.where([True, False, True])  # [0, 2]
arr3 = np.array([0, 3, 5, 3, 1])
data = np.where(arr3 == 3)  # [1, 3]
arr4 = np.array([[0, 2, 3],
                [1, 0, 0],
                [-3, 0, 0]])
x_ind, y_ind = np.where(arr4 != 0)  # x_ind = [0, 0, 1, 2] & y_ind = [1, 2, 0, 0]
data = arr4[x_ind, y_ind]  # [ 2, 3, 1, -3]
np_filter = np.array([[True, False], [False, True]])
positives = np.array([[1, 2], [3, 4]])
negatives = np.array([[-2, -5], [-1, -8]])
data = np.where(np_filter, positives, negatives)  # [[ 1, -5], [-1, 4]]
np_filter = positives > 2  # [[False False] [ True True]]
data = np.where(np_filter, positives, negatives)  # [[-2, -5], [ 3, 4]]
np_filter = negatives > 0  # [[False False] [False False]]
data = np.where(np_filter, positives, negatives)  # [[-2, -5], [-1, -8]]
# The term broadcasting describes how numpy treats arrays with different
# shapes during arithmetic operations. Subject to certain constraints,
# the smaller array is “broadcast” across the larger array so that they
# have compatible shapes
np_filter = np.array([[True, False], [False, True]])
positives = np.array([[1, 2], [3, 4]])
data = np.where(np_filter, positives, -1)  # [[1, 2], [3, 4]] & [[-1, -1], [-1, -1]] --> [[ 1, -1], [-1, 4]]

# Axis-wise filtering
arr5 = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
data = arr5 > 0  # [[False, False, False], [ True, True, False], [ True, True, True]]
data = np.any(arr5 > 0)  # True
data = np.all(arr5 > 0)  # False
arr6 = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
data = arr6 > 0  # [[False, False, False], [ True, True, False], [ True, True, True]]
data = np.any(arr > 0, axis=0)  # -2, 4, 3 --> [False, True, True]
data = np.any(arr > 0, axis=1)  # -1, 5, 9 --> [False, True, True]
data = np.all(arr > 0, axis=2)  # -3, -6, 1 --> [False, False, True]
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
has_positive = np.any(arr > 0, axis=1)  # -1, 5, 9 --> [False True True]
data = arr[np.where(has_positive)]  # [False True True] --> [[ 4, 5, -6], [ 3, 9, 1]]





