import numpy as np
import pandas as pd
num = 5
table = np.arange(1, 11) * num
df = pd.DataFrame({
    "Multiplication Table of 5": table
})
print(df)