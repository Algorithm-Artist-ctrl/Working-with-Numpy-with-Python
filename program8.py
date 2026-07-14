import numpy as np
import pandas as pd
arr = np.random.randint(1,67,78,90, 89,89,88,100,908,90, 10)
df = pd.DataFrame({
    "Numbers": arr
})
sorted_df = df.sort_values(by="Numbers")
print(sorted_df)