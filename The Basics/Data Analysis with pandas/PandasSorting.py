import pandas as pd

# Sorting by feature
df = pd.read_csv('data.csv')
#    HR   playerID teamID  yearID
# 0  15  pedrodu01    BOS    2016
# 1   7  pedrodu01    BOS    2017
# 2  33  troutmi01    LAA    2017
# 3  43   cruzne02    SEA    2016
# 4  39   cruzne02    SEA    2017
# 5  29  troutmi01    LAA    2016
sort1 = df.sort_values('yearID')
#    HR   playerID teamID  yearID
# 0  15  pedrodu01    BOS    2016
# 3  43   cruzne02    SEA    2016
# 5  29  troutmi01    LAA    2016
# 1   7  pedrodu01    BOS    2017
# 2  33  troutmi01    LAA    2017
# 4  39   cruzne02    SEA    2017
sort2 = df.sort_values('playerID', ascending=False)
#    HR   playerID teamID  yearID
# 2  33  troutmi01    LAA    2017
# 5  29  troutmi01    LAA    2016
# 0  15  pedrodu01    BOS    2016
# 1   7  pedrodu01    BOS    2017
# 3  43   cruzne02    SEA    2016
# 4  39   cruzne02    SEA    2017
df = pd.read_csv('data.csv')
#    HR   playerID teamID  yearID
# 0  15  pedrodu01    BOS    2016
# 1   7  pedrodu01    BOS    2017
# 2  33  troutmi01    LAA    2017
# 3  43   cruzne02    SEA    2016
# 4  39   cruzne02    SEA    2017
# 5  29  troutmi01    LAA    2016
sort1 = df.sort_values(['yearID', 'playerID'])
#   HR   playerID teamID  yearID
# 3  43   cruzne02    SEA    2016
# 0  15  pedrodu01    BOS    2016
# 5  29  troutmi01    LAA    2016
# 4  39   cruzne02    SEA    2017
# 1   7  pedrodu01    BOS    2017
# 2  33  troutmi01    LAA    2017
sort2 = df.sort_values(['yearID', 'HR'],
                       ascending=[True, False])
#    HR   playerID teamID  yearID
# 3  43   cruzne02    SEA    2016
# 5  29  troutmi01    LAA    2016
# 0  15  pedrodu01    BOS    2016
# 4  39   cruzne02    SEA    2017
# 2  33  troutmi01    LAA    2017
# 1   7  pedrodu01    BOS    2017