import numpy as np
import pandas as pd
data = {
    "Math": [80, 70, 89,98,90],
    "Science": [75, 85,90,90, 95]
}
df = pd.DataFrame(data)
df["Total"] = np.sum(df[["Math", "Science"]], axis=1)
df["Percentage"] = df["Total"] / 2
print(df)