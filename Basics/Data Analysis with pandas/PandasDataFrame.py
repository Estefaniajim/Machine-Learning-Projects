import pandas as pd

# DataFrame
df = pd.DataFrame()  # Columns: [] Index: []
df = pd.DataFrame([5, 6])  # 0, 0 --> 5, 1 --> 6
df = pd.DataFrame([[5,6]])  # 0  1, 0 --> 5,6
df = pd.DataFrame([[5, 6], [1, 3]],
                  index=['r1', 'r2'],
                  columns=['c1', 'c2'])  #  c1  c2, r1 --> 5,6, r2 --> 1,3
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4]},
                   index=['r1', 'r2'])   # c1  c2, r1 --> 1,3, r2 --> 2,4

# Upcasting
upcast = pd.DataFrame([[5, 6], [1.2, 3]])  # 0 --> float64  1 --> int64, 0 --> 5.0,6, 1 --> 1.2,3

# Appending rows
df = pd.DataFrame([[5, 6], [1.2, 3]])
ser = pd.Series([0, 0], name='r3')
df_app = df.append(ser)  # 0  1, 0 --> 5.0,6, 1 --> 1.2,3, r3 --> 0.0,0
df_app = df.append(ser, ignore_index=True)  # 0  1, 0 --> 5.0,6, 1 --> 1.2,3, 2 --> 0.0,0
df2 = pd.DataFrame([[0,0],[9,9]])
df_app = df.append(df2)  # 0  1, 0 --> 5.0,6, 1 --> 1.2,3, 0 --> 0.0,0, 1 --> 9.0,9

# Dropping data
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]},
                  index=['r1', 'r2'])
df_drop = df.drop(labels='r1')  #  c1  c2  c3, r2 --> 2,4,6
df_drop = df.drop(labels=['c1', 'c3'], axis=1)  # c2, r1 --> 3, r2 --> 4
df_drop = df.drop(index='r2')  # c1  c2  c3, r1 --> 1   3   5
df_drop = df.drop(columns='c2')  # c1  c3, r1 --> 1   5, r2 --> 2   6
df.drop(index='r2', columns='c2')  # c1  c3, r1 --> 1   5, r2 --> 2   6