import pandas as pd
import numpy as np

# For .read_csv, always use header = 0 when you know row 0 is the header row
df = pd.read_csv('train.csv', header = 0)
# print df.head(3) # list first 3 rows
# print df.tail(3) # list last 3 row
# print type(df)

"""pandas is able to infer numerical types when it can detect them"""
"""while csv package can only interpreted as a string"""
# print df.dtypes1

# print df.info()
# print df.describe()

df['Age'][0:10]