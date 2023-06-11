import numpy as np
import pandas as pd

# df = pd.DataFrame(np.random.randn(10, 4))
# print(df)
# print(df[:3])
# print(df[3:7])
# print(df[7:])
# pieces = [df[:3], df[3:7], df[7:]]
# print(pieces)
# print(pd.concat(pieces))

# left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
# right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
# print(pd.merge(left, right, on="key"))
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
print(pd.merge(left, right, on="key"))
