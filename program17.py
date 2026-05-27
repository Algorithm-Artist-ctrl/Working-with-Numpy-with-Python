import numpy as np
import pandas as pd

employees = ["Aman", "Riya", "Kunal", "Priya"]
salary = np.array([45000, 52000, 48000, 60000])

df = pd.DataFrame({
    "Employee": employees,
    "Salary": salary
})

df["Bonus"] = df["Salary"] * 0.10
df["Total"] = df["Salary"] + df["Bonus"]

print(df)