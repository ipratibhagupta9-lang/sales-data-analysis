# Step 1: pandas import karo
import pandas as pd

# Step 2: CSV file load karo
df = pd.read_csv("sales_data.csv")

# Step 3: First 5 rows dikhao
print("First 5 rows:")
print(df.head())

# Step 4: Missing values check karo
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Missing values fill karo
df.fillna(0, inplace=True)

# Step 6: Total Sales calculate karo
total_sales = df["Total_Sales"].sum()

# Step 7: Average sale
average_sales = df["Total_Sales"].mean()

# Step 8: Highest sale
highest_sale = df["Total_Sales"].max()

# Step 9: Best selling product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

# Step 10: Final Report print karo
print("\n------ SALES REPORT ------")
print("Total Sales:", total_sales)
print("Average Sale:", average_sales)
print("Highest Sale:", highest_sale)
print("Best Product:", best_product)
print("--------------------------")
