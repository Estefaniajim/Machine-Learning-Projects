import numpy as np

# Summation
arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
sum = np.sum(arr)  # 18
sum = np.sum(arr, axis=0)  # [ -2,  73, -53]
sum = np.sum(arr, axis=1)  # [ 75, -56,  -1]
arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
sum = np.cumsum(arr)  # [ 0, 72, 75, 76, 79, 19, 16, 14, 18]
sum = np.cumsum(arr, axis=0)  # 0+1+-3,72+3+-2,3-60+4 --> [[  0,  72,   3], [  1,  75, -57],[ -2,  73, -53]]
sum = np.cumsum(arr, axis=1)  # [[  0,  72,  75], [  1,   4, -56], [ -3,  -5,  -1]]

# Concatenation
arr1 = np.array([[0, 72, 3],
                 [1, 3, -60],
                 [-3, -2, 4]])
arr2 = np.array([[-15, 6, 1],
                 [8, 9, -4],
                 [5, -21, 18]])
conc = np.concatenate([arr1, arr2])  # [[  0,  72,   3],
#                                       [  1,   3, -60],
#                                       [ -3,  -2,   4],
#                                       [-15,   6,   1],
#                                       [  8,   9,  -4],
#                                       [  5, -21,  18]]
conc = np.concatenate([arr1, arr2], axis=1)  # [[  0,  72,   3, -15,   6,   1],
#                                               [  1,   3, -60,   8,   9,  -4],
#                                               [ -3,  -2,   4,   5, -21,  18]]
conc = np.concatenate([arr2, arr1], axis=1)  # [[-15,   6,   1,   0,  72,   3],
#                                               [  8,   9,  -4,   1,   3, -60],
#                                               [  5, -21,  18,  -3,  -2,   4]]

# Examples
# The function returns the overall sum and column sums of data.
# Input = [[19 20 -5  0  1]
#          [ 9  2 -3 -2  0]
#          [-9 19 11  2  2]
#          [ 1 -1 -4 -3  4]]
def get_sums(data):
  total_sum = np.sum(data)  # 63
  col_sum = np.sum(data,axis=0)  # [20 40 -1 -3  7]
  return total_sum,col_sum

# The function returns the cumulative sums for each row of data.
# Input = [[19 20 -5  0  1]
#          [ 9  2 -3 -2  0]
#          [-9 19 11  2  2]
#          [ 1 -1 -4 -3  4]]
def get_cumsum(data):
  row_cumsum = np.cumsum(data,axis=1)
  return row_cumsum
# Output = [[19 39 34 34 35]
#           [ 9 11  8  6  6]
#           [-9 10 21 23 25]
#           [ 1  0 -4 -7 -3]]

# The function returns the column-wise and row-wise concatenations of the input arrays.
# Input = [[19 20 -5  0  1]
#          [ 9  2 -3 -2  0]
#          [-9 19 11  2  2]
#          [ 1 -1 -4 -3  4]]
#         [[  1  -2  15 -10   0]
#          [ 91  18  32 -12  10]
#          [-91  17   1  23   0]
#          [  0  -1  -5  16  81]]
def concat_arrays(data1, data2):
  col_concat = np.concatenate([data1,data2])  # [[ 19  20  -5   0   1]
 #                                               [  9   2  -3  -2   0]
 #                                               [ -9  19  11   2   2]
 #                                               [  1  -1  -4  -3   4]
 #                                               [  1  -2  15 -10   0]
 #                                               [ 91  18  32 -12  10]
 #                                               [-91  17   1  23   0]
 #                                               [  0  -1  -5  16  81]]
  row_concat = np.concatenate([data1,data2], axis = 1)  # [[ 19  20  -5   0   1   1  -2  15 -10   0]
 #                                                         [  9   2  -3  -2   0  91  18  32 -12  10]
 #                                                         [ -9  19  11   2   2 -91  17   1  23   0]
 #                                                         [  1  -1  -4  -3   4   0  -1  -5  16  81]]
  return col_concat,row_concat