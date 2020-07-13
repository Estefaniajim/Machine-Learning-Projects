import pandas as pd

# Reading data
#csv
df = pd.read_csv('data.csv')
#    HR       name pos
# 0  17  joe smith  2B
# 1  28  alan west   C
# 2  19   john doe   P
df = pd.read_csv('data.csv', index_col=0)
#          name pos
# HR
# 17  joe smith  2B
# 28  alan west   C
# 19   john doe   P
df = pd.read_csv('data.csv', index_col=1)
#            HR pos
# name
# joe smith  17  2B
# alan west  28   C
# john doe   19   P
# excel sheet
df = pd.read_excel('data.xlsx')
#    HR       name pos
# 0   1   jack lee  SS
# 1  52     mo sam  1B
# 2  37  lex jones  RF
df = pd.read_excel('data.xlsx', sheet_name=1)
#   HR        name pos
# 0  32    abe hass  LF
# 1  17    jim buck   C
# 2  58  aaron dean  LF
df = pd.read_excel('data.xlsx', sheet_name='MIL')
#    HR         name pos
# 0  15      jj west  LF
# 1  44  will thomas  CF
# 2  12   alex stein  3B
df_dict = pd.read_excel('data.xlsx', sheet_name=[0, 1])  # sheets 0 and 1
#    HR        name pos
# 0  32    abe hass  LF
# 1  17    jim buck   C
# 2  58  aaron dean  LF
df_dict = pd.read_excel('data.xlsx', sheet_name=None)  # all sheets in the document
# json
df1 = pd.read_json('data.json')
#     jack doe tom june
# HR         4       31
# pos       1B        P
df2 = pd.read_json('data.json', orient='index')
#           HR pos
# jack doe   4  1B
# tom june  31   P

# Writing to files
# csv
df.to_csv('data.csv')  # Index is not kept when writing
#   HR       name pos
# 0  17  joe smith  2B
# 1  28  alan west   C
# 2  19   john doe   P
df = pd.read_csv('data.csv')
#    Unnamed: 0  HR       name pos
# 0           0  17  joe smith  2B
# 1           1  28  alan west   C
# 2           2  19   john doe   P
df.to_csv('data.csv', index=False)
df = pd.read_csv('data.csv')  # Index is not kept when writing
# excel sheet
with pd.ExcelWriter('data.xlsx') as writer:
  df1.to_excel(writer, index=False, sheet_name='NYY')
  df2.to_excel(writer, index=False, sheet_name='BOS')
df_dict = pd.read_excel('data.xlsx', sheet_name=None)
# odict_keys(['NYY', 'BOS'])
#    HR        name pos
# 0  32    abe hass  LF
# 1  17    jim buck   C
# 2  58  aaron dean  LF
# json
df.to_json('data.json')
#    HR       name pos
# 0   1   jack lee  SS
# 1  52     mo sam  1B
# 2  37  lex jones  RF
df2 = pd.read_json('data.json')
#    HR       name pos
# 0   1   jack lee  SS
# 1  52     mo sam  1B
# 2  37  lex jones  RF
df.to_json('data.json', orient='index')
df2 = pd.read_json('data.json')
#              0       1          2
# HR           1      52         37
# name  jack lee  mo sam  lex jones
# pos         SS      1B         RF
df2 = pd.read_json('data.json', orient='index')
#    HR       name pos
# 0   1   jack lee  SS
# 1  52     mo sam  1B
# 2  37  lex jones  RF