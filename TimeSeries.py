import numpy as np
import pandas as pd

rng = pd.date_range("1/1/2012", periods=100, freq="S")
# print(rng)
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
# print(ts)
# print(ts.resample("5Min"))
# print(ts.resample("5Min").sum())

rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
# print(ts)
ts_utc = ts.tz_localize("UTC")
# print(ts_utc)
# print(ts_utc.tz_convert("US/Eastern"))

rng = pd.date_range("1/1/2012", periods=5, freq="M")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts)
ps = ts.to_period()
# print(ps)
# print(ps.to_timestamp())

prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")
ts = pd.Series(np.random.randn(len(prng)), prng)
# print(ts)
ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9
print(ts.head())
