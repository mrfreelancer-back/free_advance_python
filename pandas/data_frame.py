import pandas as pnds
import numpy as nmp

data_frame = pnds.DataFrame(
    {
        "Name": ["ali", "alex", "jack"],
        "Age": [17, 88, 99],
        "Sex": ["M", "F", "M"]
    }
)

print(data_frame)
print(data_frame["Name"])
print(data_frame["Age"])

ages = pnds.Series([17, 88, 99], name="Age")
print(ages)
print(ages.max(), data_frame["Age"].max())

df_desc = data_frame.describe()
print(df_desc)

s = pnds.Series(nmp.random.randn(1000))
print(s)