import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data load karein
df = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-3')

# 2. Figures ke liye jagah banayein (Do graphs ek sath)
plt.figure(figsize=(15, 6))

# --- GRAPH 1: Product Line Sales (Paisa kitna kamaya) ---
plt.subplot(1, 2, 1) # Pehla graph
product_sales = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
ax1 = product_sales.plot(kind='bar', color='teal')
plt.title('Product wise Total Sales ')
plt.ylabel('Total Sales')

# Bars ke ooper paise likhne ke liye
for p in ax1.patches:
    ax1.annotate(f'${p.get_height():,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=8)

# --- GRAPH 2: Monthly Sales Trend (Kis mahine zyada sale hui) ---
plt.subplot(1, 2, 2) # Dusra graph
monthly_sales = df.groupby('MONTH_ID')['SALES'].sum()
monthly_sales.plot(kind='line', marker='o', color='red', linewidth=2)
plt.title('Monthly Sales Trend ')
plt.xlabel('Month (1=Jan, 12=Dec)')
plt.ylabel('Total Sales ')
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()