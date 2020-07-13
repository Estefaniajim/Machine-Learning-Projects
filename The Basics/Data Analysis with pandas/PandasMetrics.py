import pandas as pd

#  Numeric metrics
df = df = pd.read_csv('data.csv')
#    HR  RBI   playerID teamID  yearID
# 0  39  119   cruzne02    SEA    2017
# 1   7   62  pedrodu01    BOS    2017
# 2  43  105   cruzne02    SEA    2016
# 3  12   42  pedrodu01    BOS    2015
# 4  33   72  troutmi01    LAA    2017
# 5  15   74  pedrodu01    BOS    2016
metrics1 = df.describe()
#               HR         RBI       yearID
# count   6.000000    6.000000     6.000000
# mean   24.833333   79.000000  2016.333333
# std    15.341664   28.312541     0.816497
# min     7.000000   42.000000  2015.000000
# 25%    12.750000   64.500000  2016.000000
# 50%    24.000000   73.000000  2016.500000
# 75%    37.500000   97.250000  2017.000000
# max    43.000000  119.000000  2017.000000
hr_rbi = df[['HR','RBI']]
metrics2 = hr_rbi.describe()
#               HR         RBI
# count   6.000000    6.000000
# mean   24.833333   79.000000
# std    15.341664   28.312541
# min     7.000000   42.000000
# 25%    12.750000   64.500000
# 50%    24.000000   73.000000
# 75%    37.500000   97.250000
# max    43.000000  119.000000
metrics1 = hr_rbi.describe(percentiles=[.5])
#               HR         RBI
# count   6.000000    6.000000
# mean   24.833333   79.000000
# std    15.341664   28.312541
# min     7.000000   42.000000
# 50%    24.000000   73.000000
# max    43.000000  119.000000
metrics2 = hr_rbi.describe(percentiles=[.1])
#               HR         RBI
# count   6.000000    6.000000
# mean   24.833333   79.000000
# std    15.341664   28.312541
# min     7.000000   42.000000
# 10%     9.500000   52.000000
# 50%    24.000000   73.000000
# max    43.000000  119.000000
metrics3 = hr_rbi.describe(percentiles=[.2,.8])
#               HR         RBI
# count   6.000000    6.000000
# mean   24.833333   79.000000
# std    15.341664   28.312541
# min     7.000000   42.000000
# 20%    12.000000   62.000000
# 50%    24.000000   73.000000
# 80%    39.000000  105.000000
# max    43.000000  119.000000

#  Categorical features
p_ids = df['playerID']
count = p_ids.value_counts()
# pedrodu01    3
# cruzne02     2
# troutmi01    1
count = p_ids.value_counts(normalize=True)
# pedrodu01    0.500000
# cruzne02     0.333333
# troutmi01    0.166667
count = p_ids.value_counts(ascending=True)
# troutmi01    1
# cruzne02     2
# pedrodu01    3
unique_players = df['playerID'].unique()  # ['cruzne02', 'pedrodu01', 'troutmi01']
unique_teams = df['teamID'].unique()  # ['SEA', 'BOS', 'LAA']
y_ids = df['yearID']
# 0    2017
# 1    2017
# 2    2016
# 3    2015
# 4    2017
# 5    2016
y_ids.unique()  # [2017, 2016, 2015]
y_ids.value_counts()
# 2017    3
# 2016    2
# 2015    1