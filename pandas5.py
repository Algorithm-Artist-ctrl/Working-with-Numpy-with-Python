import pandas as pd
data = {
    'Name': ['Aman', 'Riya', 'Sohan'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 78]
}
df = pd.DataFrame(data)
print("\nFirst rows:")
print(df.head())
