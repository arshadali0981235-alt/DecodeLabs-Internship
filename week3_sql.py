import pandas as pd
import sqlite3

# STEP 1: DATA LOAD KARNA
# Hum CSV file ko read kar rahe hain taake usay SQL table mein badal saken
try:
    df = pd.read_csv('sales_data_sample.csv', encoding='Unicode_escape')
    print(" System Message: CSV File successfully loaded!")
except Exception as e:
    print(f" Error: File nahi mili ya format galat hai: {e}")

# SQL DATABASE BANANA

conn = sqlite3.connect('Internship_Project3.db')

# Hum DataFrame (df) ko 'sales_table' naam ki SQL table mein convert kar rahe hain
df.to_sql('sales_table', conn, if_exists='replace', index=False)

print("\n" + "="*40)
print("   PROJECT 3: SQL DATA ANALYSIS RESULTS   ")
print("="*40 + "\n")

#  SQL QUERIES CHALANA
# SELECT SUM(SALES) ka matlab hai SALES column ka total nikalna
query_total = "SELECT SUM(SALES) as Total_Revenue FROM sales_table"
res_total = pd.read_sql_query(query_total, conn)
print(f"1. TOTAL REVENUE: ${res_total.iloc[0,0]:,.2f}")


#  Sales by Product Line 
query_product = """
SELECT PRODUCTLINE, SUM(SALES) as Total_Sales 
FROM sales_table 
GROUP BY PRODUCTLINE 
ORDER BY Total_Sales DESC
"""
res_product = pd.read_sql_query(query_product, conn)
print("\n2. PRODUCT PERFORMANCE (Ranked by Sales):")
print(res_product)


#  Top 5 Customers 5 result show kry ga 
query_customers = """
SELECT CUSTOMERNAME, COUNTRY, SUM(SALES) as Total_Purchase 
FROM sales_table 
GROUP BY CUSTOMERNAME 
ORDER BY Total_Purchase DESC 
LIMIT 5
"""
res_customers = pd.read_sql_query(query_customers, conn)
print("\n3. TOP 5 VALUABLE CUSTOMERS:")
print(res_customers)

# Connection band karna zaroori hota hai
conn.close()

print("\n" + "="*40)
print("Analysis Successfully Completed")
print("="*40)