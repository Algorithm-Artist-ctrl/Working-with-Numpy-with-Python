import numpy as np
import pandas as pd
temperature = np.array([30, 32, 31, 78,87,29, 35, 36, 33])
df = pd.DataFrame({
    "Temperature": temperature
})
print(df)
print("\nAverage Temperature:", np.mean(df["Temperature"]))
print("Minimum Temperature:", np.min(df["Temperature"]))