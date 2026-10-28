
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("amazon_cleaned.csv")

# Convert price columns to numbers
for col in ["actual_price", "discounted_price"]:
    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col].astype(str)
            .str.replace("₹", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip(),
            errors="coerce"
        )

# Convert rating to numbers
if "rating" in df.columns:
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# Create savings column
if "actual_price" in df.columns and "discounted_price" in df.columns:
    df["savings"] = df["actual_price"] - df["discounted_price"]

# Create rating category
if "rating" in df.columns:
    df["rating_category"] = df["rating"].apply(
        lambda x: "High" if pd.notna(x) and x >= 4
        else "Low" if pd.notna(x) else "Unknown"
    )

# Save transformed dataset
df.to_csv("amazon_transformed.csv", index=False)

print("Data transformation completed successfully!")
print("Rows and columns:", df.shape)
print("Saved as amazon_transformed.csv")