import pandas as pd

# Combining
df1 = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4]},
                   index=['r1', 'r2'])
df2 = pd.DataFrame({'c1': [5, 6], 'c2': [7, 8]},
                   index=['r1', 'r2'])
df3 = pd.DataFrame({'c1': [5, 6], 'c2': [7, 8]})
concat = pd.concat([df1, df2], axis=1)
#         c1  c2  c1  c2,
# r1 -->  1   3   5    7
# r2 -->  2   4   6    8
concat = pd.concat([df2, df1, df3])
#        c1  c2
# r1 --> 5   7
# r2 --> 6   8
# r1 --> 1   3
# r2 --> 2   4
# 0 -->  5   7
# 1 -->  6   8
concat = pd.concat([df1, df3], axis=1)
#       c1   c2   c1   c2
#r1 --> 1.0  3.0  NaN  NaN
#r2 --> 2.0  4.0  NaN  NaN
#0  --> NaN  NaN  5.0  7.0
#1  --> NaN  NaN  6.0  8.0