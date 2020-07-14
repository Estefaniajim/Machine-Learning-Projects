import pandas as pd
import numpy as np

# Indicator features
df = pd.read_csv('data.csv')
#     color
# r1    red
# r2   blue
# r3  green
# r4    red
# r5    red
# r6   blue
indicator_df = df
# blue  green  red
# r1     0      0    1
# r2     1      0    0
# r3     0      1    0
# r4     0      0    1
# r5     0      0    1
# r6     1      0    0

# Converting to indicators
df = pd.read_csv("data.csv")
#           lgID teamID
# playerID
# bettsmo01   AL    BOS
# martest01   NL    PIT
# pedrodu01   AL    BOS
# polangr01   NL    PIT
converted = pd.get_dummies(df)  # ['lgID_AL', 'lgID_NL', 'teamID_BOS', 'teamID_PIT']
converted = converted[['teamID_BOS','teamID_PIT']]
#            teamID_BOS  teamID_PIT
# playerID
# bettsmo01           1           0
# martest01           0           1
# pedrodu01           1           0
# polangr01           0           1
converted = converted[['lgID_AL','lgID_NL']]
 #           lgID_AL  lgID_NL
# playerID
# bettsmo01        1        0
# martest01        0        1
# pedrodu01        1        0
#polangr01        0        1

# Converting to NumPy
df = pd.read_csv("data.csv")
#            HR  teamID_BOS  teamID_PIT
# playerID
# bettsmo01  24           1           0
# martest01   7           0           1
# pedrodu01   7           1           0
# polangr01  11           0           1
n_matrix = df.values
#[[24,  1,  0],
# [ 7,  0,  1],
# [ 7,  1,  0],
# [11,  0,  1]]