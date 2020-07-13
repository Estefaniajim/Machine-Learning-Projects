import numpy as np

# Analysis
arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
min = arr.min()  # -60
max = arr.max()  # 72
arrMin = arr.min(axis=0)  # [ -3,  -2, -60]
arrMax = arr.max(axis=-1)  # [72,  3,  4]
arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
mean = np.mean(arr)  # 2.0
variance = np.var(arr)  # 977.3333333333334
median = np.median(arr)  # 1.0
medianArray = np.median(arr, axis=-1)  # [ 3.,  1., -2.]

# Examples
# The function returns the overall minimum and maximum element in data
# Input = [[19 20 -5  0  1] [ 9  2 -3 -2  0] [-9 19 11  2  2] [ 1 -1 -4 -3  4]]
def get_min_max(data):
  overall_min = data.min() # -9
  overall_max = data.max() # 20
  return overall_min,overall_max

# The function returns the minimums across each column of data.
# Input = [[19 20 -5  0  1] [ 9  2 -3 -2  0] [-9 19 11  2  2] [ 1 -1 -4 -3  4]]
def col_min(data):
  min0 = data.min(axis=0)
  return min0
# Output = [-9 -1 -5 -3  0]

# The function returns the mean, median, and variance of data.
# Input = [[19 20 -5  0  1] [ 9  2 -3 -2  0] [-9 19 11  2  2] [ 1 -1 -4 -3  4]]
def basic_stats(data):
  mean = np.mean(data)  # 3.15
  median = np.median(data)  # 1.0
  var = np.var(data)  # 65.02750000000002
  return mean,median,var