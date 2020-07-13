import pandas as pd

# Grouping by column
df = pd.read_csv('data.csv')
#    yearID teamID     H    R
# 0    2017    CLE  1449  818
# 1    2015    CLE  1395  669
# 2    2016    BOS  1598  878
# 3    2015    DET  1515  689
# 4    2016    DET  1476  750
# 5    2016    CLE  1435  777
# 6    2015    BOS  1495  748
# 7    2017    BOS  1461  785
# 8    2017    DET  1435  735
groups = df.groupby('yearID')
for name, group in groups:
    print('Year: {}'.format(name))
    print('{}\n'.format(group))
# Year: 2015
#    yearID teamID     H    R
# 1    2015    CLE  1395  669
# 3    2015    DET  1515  689
# 6    2015    BOS  1495  748

# Year: 2016
#    yearID teamID     H    R
# 2    2016    BOS  1598  878
# 4    2016    DET  1476  750
# 5    2016    CLE  1435  777

# Year: 2017
#    yearID teamID     H    R
# 0    2017    CLE  1449  818
# 7    2017    BOS  1461  785
# 8    2017    DET  1435  735
group = groups.get_group(2016)
#    yearID teamID     H    R
# 2    2016    BOS  1598  878
# 4    2016    DET  1476  750
# 5    2016    CLE  1435  777
group = groups.sum()
#           H     R
# yearID
# 2015    4405  2106
# 2016    4509  2405
# 2017    4345  2338
group = groups.mean()
#                 H           R
# yearID
# 2015    1468.333333  702.000000
# 2016    1503.000000  801.666667
# 2017    1448.333333  779.333333
no2015 = groups.filter(lambda x: x.name > 2015)
#   yearID teamID     H    R
# 0    2017    CLE  1449  818
# 2    2016    BOS  1598  878
# 4    2016    DET  1476  750
# 5    2016    CLE  1435  777
# 7    2017    BOS  1461  785
# 8    2017    DET  1435  735

# Multiple columns
player_df = pd.read_csv('data.csv')
groups = player_df.groupby(['yearID', 'teamID'])
for name, group in groups:
  print('Year, Team: {}'.format(name))
  print('{}\n'.format(group))
# Year, Team: (2016, 'BOS')
#    yearID   playerID teamID    H
# 1    2016  bettsmo01    BOS  214
# 2    2016  bogaexa01    BOS  192
# 4    2016  pedrodu01    BOS  201

# Year, Team: (2016, 'HOU')
#    yearID   playerID teamID    H
# 0    2016  altuvjo01    HOU  216
# 3    2016  correca01    HOU  158

# Year, Team: (2017, 'BOS')
#    yearID   playerID teamID    H
# 6    2017  bettsmo01    BOS  166
# 7    2017  bogaexa01    BOS  156
# 9    2017  pedrodu01    BOS  119

# Year, Team: (2017, 'HOU')
#    yearID   playerID teamID    H
# 5    2017  altuvjo01    HOU  204
# 8    2017  correca01    HOU  133
sum_playes = groups.sum()
#                 H
# yearID teamID
# 2016   BOS     607
#        HOU     374
# 2017   BOS     441
#        HOU     337