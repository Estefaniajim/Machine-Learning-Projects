import pandas as pd
import numpy as np

# 1-D data
series = pd.Series()
series = pd.Series(5)  # 0 --> 5
series = pd.Series([1, 2, 3])  # 0 --> 1, 1 --> 2, 2 --> 3
series = pd.Series([1, 2.2])  # upcasting, 0 --> 1.0, 1 --> 2.2
arr = np.array([1, 2])
series = pd.Series(arr, dtype=np.float32)  # 0 --> 1.0, 1 --> 2.0
series = pd.Series([[1, 2], [3, 4]])  # 0 --> [1, 2], 1 --> [3, 4]

# Index
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # a --> 1, b --> 2, c --> 3
series = pd.Series([1, 2, 3], index=['a', 8, 0.3])  # a --> 1, 8 --> 2, 0.3 --> 3

# Dictionary input
series = pd.Series({'a':1, 'b':2, 'c':3})  # a --> 1, b --> 2, c --> 3
series = pd.Series({'b':2, 'a':1, 'c':3})  # a --> 1, b --> 2, c --> 3
series = pd.Series({"a":1, "b":3, "c":8, "d":np.nan})  # a --> 1.0, b --> 3.0, c --> 8.0, d --> NaN