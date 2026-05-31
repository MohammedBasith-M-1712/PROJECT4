import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Retail_Sales_Analysis_Dataset.csv")

# Display Dataset
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Total Sales and Profit
total_sales = df["Sales_Amount"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

# Sales by Product Category
category_sales = df.groupby("Product_Category")["Sales_Amount"].sum()

print("\nSales by Category:")
print(category_sales)

# Visualization - Sales by Category
category_sales.plot(kind='bar')

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.show()

# Profit Trend
plt.plot(df["Order_Date"], df["Profit"])

plt.title("Profit Trend")
plt.xlabel("Order Date")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.show()

# Region-wise Sales
region_sales = df.groupby("Region")["Sales_Amount"].sum()

region_sales.plot(kind='pie', autopct='%1.1f%%')

plt.title("Region-wise Sales Distribution")
plt.ylabel("")
plt.show()

# Correlation Matrix
correlation = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(correlation)