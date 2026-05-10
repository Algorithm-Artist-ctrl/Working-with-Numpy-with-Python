import numpy as np
import pandas as pd
sales = np.random.randint(1000, 5000, size=7)
df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Sales": sales
})
print(df)
print("\nTotal Sales:", np.sum(df["Sales"]))