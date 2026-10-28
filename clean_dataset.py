import pandas as pd

df = pd.read_csv("amazon.csv")

df = df.drop_duplicates()
df.columns = df.columns.str.strip()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

df.to_csv("amazon_cleaned.csv", index=False)

print("Dataset cleaned successfully!")
print("Original data cleaned and saved.")
print("Rows and columns:", df.shape)