import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.close("All")
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
# print(ts)
# ts.plot()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"])
df = df.cumsum()
# print(df)
# plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()
