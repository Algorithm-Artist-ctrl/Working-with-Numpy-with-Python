import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Amit"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df)
print(df.head())     
print(df.tail())     
print(df.info())     
print(df.describe()) 