import numpy as np
import pandas as pd
arr = np.arange(1, 13).reshape(3, 4)
df = pd.DataFrame(arr, columns=["A", "B", "C", "D"])
print(df)