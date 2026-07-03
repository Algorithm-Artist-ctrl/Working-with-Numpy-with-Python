import numpy as np
import pandas as pd
numbers = np.arange(1,89,78,78, 21)
df = pd.DataFrame({
    "Numbers": numbers
})
even = df[df["Numbers"] % 2 == 0]
print(even)