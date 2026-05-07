import pandas as pd

# 1. Load the data
df = pd.read_csv('ApexSales.csv')

# 2. Create the calculated column
df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']

# 3. Aggregations (Business Insights)

# Revenue by Category
category_revenue = df.groupby('Category')['TotalRevenue'].sum()
print("Revenue by Category:\n", category_revenue)

# Transactions by Region
region_counts = df['Region'].value_counts()
print("\nTransactions by Region:\n", region_counts)

# Top Spender (Customer who spent the most)
top_spender = df.groupby('CustomerID')['TotalRevenue'].sum().idxmax()
print(f"\nTop CustomerID: {top_spender}")

import pandas as pd

# Load the data
df = pd.read_csv('Apex_Global_Retail_Sales.csv')

# Grouping by Category AND Region
analysis = df.groupby(['Category', 'Region']).agg({
    'Quantity': 'sum',      # Total items sold
    'UnitPrice': 'mean'     # Average price point
})

print(analysis)
