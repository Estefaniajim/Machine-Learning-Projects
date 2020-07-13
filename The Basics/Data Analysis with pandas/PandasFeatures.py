import pandas as pd

# Quantitative features
df = pd.DataFrame({
  'T1': [10, 15, 8],
  'T2': [25, 27, 25],
  'T3': [16, 15, 10]})
#    T1  T2  T3
# 0  10  25  16
# 1  15  27  15
# 2   8  25  10
sumDf = df.sum()
# T1    33
# T2    77
# T3    41
sumDf = df.sum(axis=1)
# 0    51
# 1    57
# 2    43
meanDf = df.mean()
# T1    11.000000
# T2    25.666667
# T3    13.666667
meanDf = df.mean(axis=1)
# 0    17.000000
# 1    19.000000
# 2    14.333333

# Weighted features
df = pd.DataFrame({
  'T1': [0.1, 150.],
  'T2': [0.25, 240.],
  'T3': [0.16, 100.]})
#       T1      T2      T3
# 0    0.1    0.25    0.16
# 1  150.0  240.00  100.00
mulDf = df.multiply(2)
#       T1     T2      T3
# 0    0.2    0.5    0.32
# 1  300.0  480.0  200.00
df_ms = df.multiply([1000, 1], axis=0)
#       T1     T2     T3
# 0  100.0  250.0  160.0
# 1  150.0  240.0  100.0
df_w = df_ms.multiply([1,0.5,1])
#       T1     T2     T3
# 0  100.0  125.0  160.0
# 1  150.0  120.0  100.0
df_ms_sum = df_w.sum(axis=1)
# 0    385.0
# 1    370.0

# Examples
# Utility function to calculate the sum of multiple columns across a DataFrame.
def col_list_sum(df, col_list, weights=None):
    col_df = df[col_list]
    if weights is not None:
        col_df = col_df.multiply(weights)
    return col_df.sum(axis=1)