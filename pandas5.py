import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Aman', 'Riya', 'Sohan'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 78]
}
df = pd.DataFrame(data)
print("\nFirst rows:")
print(df.head())
'''print("\nNames:")
print(df['Name'])
print("\nStudents with marks > 80:")
print(df[df['Marks'] > 80])
df['Result'] = ['Pass', 'Pass', 'Pass']

print("\nAfter adding new column:")
print(df)'''