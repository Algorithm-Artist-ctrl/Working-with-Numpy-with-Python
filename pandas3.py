import pandas as pd

df = pd.read_csv("data.csv")
df['Age'] = df['Age'].fillna(df['Age'].mean())
df_clean = df.dropna()