import numpy as np
import pandas as pd
marks = np.array([78, 85, 90, 66,78,89, 88])
df = pd.DataFrame({
    "Marks": marks
})
print("Average:", np.mean(df["Marks"]))
print("Highest:", np.max(df["Marks"]))
print("Lowest:", np.min(df["Marks"]))