import pandas as pd
import numpy as np

# Filter conditions
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
  'yearID': [2016, 2016, 2016, 2016, 2017],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
  'HR': [31, 39, 43, 38, 39]})
#    HR   playerID teamID  yearID
# 0  31  bettsmo01    BOS    2016
# 1  39   canoro01    SEA    2016
# 2  43   cruzne02    SEA    2016
# 3  38  ortizda01    BOS    2016
# 4  39   cruzne02    SEA    2017
cruzne02 = df['playerID'] == 'cruzne02'
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
hr40 = df['HR'] > 40
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
notbos = df['teamID'] != 'BOS'
# 0    False
# 1     True
# 2     True
# 3    False
# 4     True

# Filters from functions
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
  'yearID': [2016, 2016, 2016, 2016, 2017],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
  'HR': [31, 39, 43, 38, 39]})
#    HR   playerID teamID  yearID
# 0  31  bettsmo01    BOS    2016
# 1  39   canoro01    SEA    2016
# 2  43   cruzne02    SEA    2016
# 3  38  ortizda01    BOS    2016
# 4  39   cruzne02    SEA    2017
str_f1 = df['playerID'].str.startswith('c')
# 0    False
# 1     True
# 2     True
# 3    False
# 4     True
str_f2 = df['teamID'].str.endswith('S')
# 0     True
# 1    False
# 2    False
# 3     True
# 4    False
str_f3 = ~df['playerID'].str.contains('o')
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
  'yearID': [2016, 2016, 2016, 2016, 2017],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
  'HR': [31, 39, 43, 38, 39]})
#    HR   playerID teamID  yearID
# 0  31  bettsmo01    BOS    2016
# 1  39   canoro01    SEA    2016
# 2  43   cruzne02    SEA    2016
# 3  38  ortizda01    BOS    2016
# 4  39   cruzne02    SEA    2017
isin_f1 = df['playerID'].isin(['cruzne02',
                               'ortizda01'])
# 0    False
# 1    False
# 2     True
# 3     True
# 4     True
isin_f2 = df['yearID'].isin([2015, 2017])
# 0    False
# 1    False
# 2    False
# 3    False
# 4     True
df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'doejo01'],
    'yearID': [2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', np.nan],
    'HR': [31, 39, 99]})
#    HR   playerID teamID  yearID
# 0  31  bettsmo01    BOS    2016
# 1  39   canoro01    SEA    2016
# 2  99    doejo01    NaN    2017
isna = df['teamID'].isna()
# 0    False
# 1    False
# 2     True
notna = df['teamID'].notna()
# 0     True
# 1     True
# 2    False

# Feature filtering
df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'bettsmo01'],
    'yearID': [2016, 2016, 2016, 2016, 2015],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'BOS'],
    'HR': [31, 39, 43, 38, 18]})
#    HR   playerID teamID  yearID
# 0  31  bettsmo01    BOS    2016
# 1  39   canoro01    SEA    2016
# 2  43   cruzne02    SEA    2016
# 3  38  ortizda01    BOS    2016
# 4  18  bettsmo01    BOS    2015
hr40_df = df[df['HR'] > 40]
#    HR  playerID teamID  yearID
# 2  43  cruzne02    SEA    2016
not_hr30_df = df[~(df['HR'] > 30)]
#    HR  playerID teamID  yearID
# 2  43  cruzne02    SEA    2016
str_df = df[df['teamID'].str.startswith('B')]
#    HR   playerID teamID  yearID
# 0  31  bettsmo01    BOS    2016
# 3  38  ortizda01    BOS    2016
# 4  18  bettsmo01    BOS    2015