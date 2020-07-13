import pandas as pd
import matplotlib.pyplot as plt

# Basics
# predefined df
df = df = pd.read_csv('data.csv')
#   HR  yearID
# 0  49    2000
# 1  73    2001
# 2  46    2002
# 3  45    2003
# 4  45    2004
# 5   5    2005
# 6  26    2006
# 7  28    2007
df.plot()
plt.title('HR vs. Year')  # title
plt.xlabel('Year')  # x label
plt.ylabel('HR Count')  # y label
plt.show()
plt.savefig('df.png')  # save to PNG file

# Multiple features
df.plot()  # line plot
df.plot(kind='box')  # boxplot
plt.show()