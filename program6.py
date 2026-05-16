import numpy as np
import pandas as pd
salary = np.array([25000, 30000, 28000, 35000, 40000])
df = pd.DataFrame({
    "Salary": salary
})
print("Mean Salary:", np.mean(df["Salary"]))
print("Standard Deviation:", np.std(df["Salary"]))