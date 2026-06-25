import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("===== SALES DATA =====")
print(df.head())

# Dataset information
print("\n===== DATASET INFORMATION =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Calculate metrics
total_revenue = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()

# Best-selling product
best_product = df.groupby("Product")["Quantity"].sum().idxmax()

# Final report
print("\n===== SALES ANALYSIS REPORT =====")
print(f"Total Revenue: ₹{total_revenue}")
print(f"Average Sales: ₹{average_sales:.2f}")
print(f"Highest Sale: ₹{highest_sale}")
print(f"Best Selling Product: {best_product}")
