import pandas as pd
import matplotlib.pyplot as plt

#  Data ko file se uthana 
# read the files here
data = pd.read_csv('sales_data_sample.csv', encoding='Unicode_escape')

# Sab se zyada sale hony  wale Products 
product_analysis = data.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
print(" Product wise Sales")
print(product_analysis)

# make a graph with the help of matplotlib.pyplot
product_analysis.plot(kind='bar', color='teal', title='Kaunsa Product sab se zyada bika?')
plt.ylabel('Sales in Dollars')
plt.show()

# Kaunse mulk (Country) top par hain? 
top_countries = data.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Countries")
print(top_countries)

#  Orders ka status kya hai? 
order_status = data['STATUS'].value_counts()
print("\n Order Status (Shipped vs Cancelled)")
print(order_status)

# make a chart here
order_status.plot(kind='pie', autopct='%1.1f%%', title='Orders ki condition')
plt.show()
