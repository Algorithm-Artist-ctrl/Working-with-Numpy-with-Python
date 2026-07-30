import numpy as np
import pandas as pd
data = {
    "Marks": [97,76, np.nan, 86, np.nan, 95]
}
df = pd.DataFrame(data)
average = np.nanmean(df["Marks"])
df["Marks"].fillna(average, inplace=True)
print(df)