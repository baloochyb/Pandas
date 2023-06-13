import numpy as np
import pandas as pd

tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
# print(tuples)
# print(index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
# print(df)
stacked = df.stack()
# print(stacked)
# print(stacked.unstack())
# print(df.unstack())
# print(stacked.unstack(1))
# print(stacked.unstack(0))
del df

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
print(df)
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))
