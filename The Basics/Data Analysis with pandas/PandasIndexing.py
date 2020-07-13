import pandas as pd

# Direct indexing
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])
col1 = df['c1']
# r1    1
# r2    2
col1_df = df[['c1']]
#     c1
# r1   1
# r2   2
col23 = df[['c2', 'c3']]
#     c2  c3
# r1   3   5
# r2   4   6
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
#     c1  c2  c3
# r1   1   4   7
# r2   2   5   8
# r3   3   6   9
first_two_rows = df[0:2]
#     c1  c2  c3
# r1   1   4   7
# r2   2   5   8
last_two_rows = df['r2':'r3']
#     c1  c2  c3
# r2   2   5   8
# r3   3   6   9

# Other Indexing
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
#     c1  c2  c3
# r1   1   4   7
# r2   2   5   8
# r3   3   6   9
index = df.iloc[1]
# c1    2
# c2    5
# c3    8
index = df.iloc[[0, 2]]
#     c1  c2  c3
# r1   1   4   7
# r3   3   6   9
bool_list = [False, True, True]
index = df.iloc[bool_list]
#     c1  c2  c3
# r2   2   5   8
# r3   3   6   9
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
#     c1  c2  c3
# r1   1   4   7
# r2   2   5   8
# r3   3   6   9
index = df.loc['r2']
# c1    2
# c2    5
# c3    8
bool_list = [False, True, True]
index = df.loc[bool_list]
#     c1  c2  c3
# r2   2   5   8
# r3   3   6   9
single_val = df.loc['r1', 'c2']
#   c1  c2  c3
# r2   2   5   8
# r3   3   6   9
index = df.loc[['r1', 'r3'], 'c2']
# r1    4
# r3    6
df.loc[['r1', 'r3'], 'c2'] = 0
#     c1  c2  c3
# r1   1   0   7
# r2   2   5   8
# r3   3   0   9