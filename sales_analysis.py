import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

print("Total Sales:", df["Sales"].sum())
print("\nSales by Product:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False))

print("\nSales by City:")
print(df.groupby("City")["Sales"].sum().sort_values(ascending=False))

print("\nMonthly Sales:")
print(df.groupby("Month")["Sales"].sum())

# Product chart
df.groupby("Product")["Sales"].sum().sort_values().plot(kind="barh")
plt.title("Sales by Product")
plt.xlabel("Sales (₹)")
plt.tight_layout()
plt.show()

# City chart
df.groupby("City")["Sales"].sum().sort_values().plot(kind="bar")
plt.title("Sales by City")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.show()

# Monthly trend
df.groupby("Month")["Sales"].sum().plot(marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
