import numpy as np
import pandas as pd

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD")) # Data Frame

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
# print(pd.isna(df1))
# print(df1.fillna(value=5))
# print(df1.dropna(how="any"))
# print(df1)
df1 = df1.dropna(how="any")
print(df1)
