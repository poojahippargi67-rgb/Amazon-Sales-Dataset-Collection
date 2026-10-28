
import pandas as pd
import matplotlib.pyplot as plt

# Load the transformed dataset
df = pd.read_csv("amazon_transformed.csv")

# 1. Top 10 product categories
top_categories = df["category"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_categories.plot(kind="bar")
plt.title("Top 10 Amazon Product Categories")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_categories.png")
plt.show()

# 2. Product rating distribution
ratings = pd.to_numeric(df["rating"], errors="coerce").dropna()

plt.figure(figsize=(8, 5))
ratings.plot(kind="hist", bins=10, edgecolor="black")
plt.title("Amazon Product Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

# 3. Average savings by top 10 categories
df["savings"] = pd.to_numeric(df["savings"], errors="coerce")
category_savings = (
    df.groupby("category")["savings"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
category_savings.plot(kind="bar")
plt.title("Top 10 Categories by Average Savings")
plt.xlabel("Category")
plt.ylabel("Average Savings")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("average_savings.png")
plt.show()

print("Charts created successfully!")
print("Saved: top_categories.png")
print("Saved: rating_distribution.png")
print("Saved: average_savings.png")