import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Aman', 'Riya', 'Sohan'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)