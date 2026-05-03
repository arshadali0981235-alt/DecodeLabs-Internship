import sqlite3
import pandas as pd

# 1. Load the same CSV
df = pd.read_csv('sales_data_sample.csv', encoding='Unicode_Escape')

# 2. Connect to SQLite
conn = sqlite3.connect('Internship_Project4.db')
df.to_sql('sales_table', conn, if_exists='replace', index=False)

def run_query(query):
    return pd.read_sql_query(query, conn)

print("="*40)
print("   PROJECT 4: ADVANCED SQL ANALYSIS")
print("="*40)

# A. Year-over-Year Sales (Kis saal kitni kamai hui)
query1 = """
SELECT YEAR_ID, SUM(SALES) as Yearly_Revenue
FROM sales_table
GROUP BY YEAR_ID
ORDER BY YEAR_ID;
"""
print("\n1. YEARLY REVENUE TREND:")
print(run_query(query1))

# B. Monthly Sales for the best year (2004)
query2 = """
SELECT MONTH_ID, SUM(SALES) as Monthly_Sales
FROM sales_table
WHERE YEAR_ID = 2004
GROUP BY MONTH_ID
ORDER BY MONTH_ID;
"""
print("\n2. MONTHLY SALES TREND (YEAR 2004):")
print(run_query(query2))

# C. Top 5 Countries by Order Count
query3 = """
SELECT COUNTRY, COUNT(ORDERNUMBER) as Total_Orders
FROM sales_table
GROUP BY COUNTRY
ORDER BY Total_Orders DESC
LIMIT 5;
"""
print("\n3. TOP 5 COUNTRIES BY ORDER VOLUME:")
print(run_query(query3))

conn.close()
print("\n" + "="*40)
print("Analysis Completed Successfully!")