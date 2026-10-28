
import pandas as pd

# Load transformed dataset
df = pd.read_csv("amazon_transformed.csv")

print("DATA ANALYSIS REPORT")
print("--------------------")

# Dataset information
print("\nDataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Average rating
if "rating" in df.columns:
    print("\nAverage Rating:")
    print(df["rating"].mean())

# Top 10 product categories
if "category" in df.columns:
    print("\nTop 10 Categories:")
    print(df["category"].value_counts().head(10))

# Highest savings products
if "savings" in df.columns:
    print("\nTop 10 Products by Savings:")
    cols = ["product_name", "savings"]
    cols = [c for c in cols if c in df.columns]
    print(df[cols].sort_values(
        "savings", ascending=False
    ).head(10))

# Save analysis results
df.describe(include="all").to_csv("analysis_report.csv")

print("\nAnalysis completed successfully!")
print("Report saved as analysis_report.csv")