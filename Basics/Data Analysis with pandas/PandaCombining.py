import pandas as pd

# Concatenate
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

# Merging
mlb_df1 = pd.DataFrame({'name': ['john doe', 'al smith', 'sam black', 'john doe'],
                        'pos': ['1B', 'C', 'P', '2B'],
                        'year': [2000, 2004, 2008, 2003]})
#       name    pos  year
#0 --> john doe  1B  2000
#1 --> al smith   C  2004
#2 --> sam black  P  2008
#3 --> john doe  2B  2003
mlb_df2 = pd.DataFrame({'name': ['john doe', 'al smith', 'jack lee'],
                        'year': [2000, 2004, 2012],
                        'rbi': [80, 100, 12]})
#        name   pos  year
#0 --> john doe  1B  2000
#1 --> al smith   C  2004
#2 --> sam black  P  2008
#3 --> john doe  2B  2003
mlb_merged = pd.merge(mlb_df1, mlb_df2)
#       name pos  year  rbi
#0  john doe  1B  2000   80
#1  al smith   C  2004  100