# Apex-Global-Retail-Analysis
A Python and Excel-based analysis of weekly retail sales to identify revenue drivers and regional performance.
Project Title: Apex Global Retail – Weekly Sales Performance Analysis
1. Project Overview
This project involves analyzing a transactional dataset for a retail company to identify revenue drivers, regional performance, and customer purchasing behavior. I utilized both Python (Pandas) for automated data processing and Excel/Pivot Tables for rapid business intelligence.

2. The Dataset
The analysis is based on 10 transactions from the first week of May 2026.

Fields: OrderID, Date, CustomerID, Category, Region, Quantity, UnitPrice, PaymentMethod.

Key Derived Metric: TotalRevenue (Quantity × UnitPrice).

3. Technical Problems Solved (The "How")
In a portfolio, showing how you fixed errors is just as important as the final chart.

Environment Setup: Successfully configured a Python 3.12 environment and resolved ModuleNotFoundError by managing packages via pip.

Debugging File Paths: Resolved a FileNotFoundError by aligning script directories and handling file extensions (.csv) correctly in the code.

Multi-Tool Workflow: Established a workflow that leverages Excel for stakeholder reporting and Python for repeatable data aggregation.
4. Core Analysis Tasks
I completed the following data tasks to extract value from the raw CSV:
Objective,Task Description
Data Cleaning,"Checked for null values and ensured data types (e.g., Dates) were correct for analysis."
Revenue Analysis,"Calculated total revenue ($1,856.00) and Average Order Value ($185.60)."
Categorical Insights,Identified Electronics as the top-performing category (69% of total revenue).
Regional Performance,Determined that North and West regions lead in transaction volume.
Behavioral Analysis,Isolated the top-spending customer and identified Credit Card as the primary payment method.
5. Code Snippet (Python Integration)
The following script was developed to automate the multi-dimensional analysis:
import pandas as pd

# Load and process data
df = pd.read_csv('Apex_Global_Retail_Sales.csv')
df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']

# Grouping by Category and Region to find Average Price and Total Sales
analysis = df.groupby(['Category', 'Region']).agg({
    'Quantity': 'sum',
    'UnitPrice': 'mean',
    'TotalRevenue': 'sum'
})
print(analysis)

<img width="1320" height="708" alt="Apex-Sales by region" src="https://github.com/user-attachments/assets/b386821f-7504-40e8-8fe0-175c7c0b3ca7" />

Using Excel
Pivot Table
Total revenue by region is the image:
![Sales Charts](<img width="823" height="678" alt="Apex-Sales Total Revenue by region" src="https://github.com/user-attachments/assets/1b0d1048-51b2-4cb2-a455-4f9810f31a85" />)


6. Business Recommendations
Based on the data, I proposed the following actions to the management:

High-Value Targeting: Since Electronics drives the most revenue but has lower volume, create a "Premium Electronics" loyalty program for top spenders (like Customer C005).

Geographic Expansion: Launch marketing campaigns in the South and East regions to mirror the high transaction volume seen in the North and West.

Payment Optimization: Since 50% of users use Credit Cards, explore partnerships with banks for cashback offers to increase the average transaction size.

![Sales Charts](<img width="644" height="553" alt="Apex-Sales using matplotlib for visualization" src="https://github.com/user-attachments/assets/31fa65c2-57ca-4006-b657-4733480eae6d" />)
