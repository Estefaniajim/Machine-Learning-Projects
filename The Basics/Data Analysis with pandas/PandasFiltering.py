import pandas as pd

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
