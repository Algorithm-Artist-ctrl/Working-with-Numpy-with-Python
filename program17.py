import numpy as np
import pandas as pd
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "speaker","Laptop"],
    "Sales": [50000, 2000,7000, 3000,8900,8777,6578 ,15000, 55000],
    "Quantity": [5, 20, 15, 7, 6]
}
df = pd.DataFrame(data)
print("SalesData:\n")
print(df)
total_sales = np.sum(df["Sales"])
print("\nTotal Sales:", total_sales)
avg_sales = np.mean(df["Sales"])
print("Average Sales:", avg_sales)
max_sale = np.max(df["Sales"])
print("Highest Sale:", max_sale)
summary = df.groupby("Product")["Sales"].sum()
print("\nProduct-wise Sales Summary:\n")
print(summary)