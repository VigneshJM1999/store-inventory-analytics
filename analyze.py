import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

sql_query = """
SELECT
  s.sale_date,
  c.category_name,
  p.product_name,
  s.quantity_sold,
  p.selling_price,
  -- Calculate total revenue for this sale
  (p.selling_price * s.quantity_sold) AS total_revenue,
  -- Calculate total profit for this sale
  ((p.selling_price - p.cost_price) * s.quantity_sold) AS total_profit
FROM
  Sales AS s
  JOIN Products AS p ON s.product_id = p.product_id
  JOIN Categories AS c ON p.category_id = c.category_id
ORDER BY
  s.sale_date;
"""

conn = sqlite3.connect('inventory.db')
df = pd.read_sql_query(sql_query, conn)
conn.close()

print("--- Here is our raw data from the SQL query ---")
print(df)
print("\n")

print("--- DataFrame Info (columns, data types) ---")
df.info()
print("\n")

print("--- Summary Statistics (for numeric columns) ---")
print(df.describe())
print("\n")

print("--- Total profit by category (calculated in Pandas) ---")
category_profit = df.groupby('category_name')['total_profit'].sum()
print(category_profit)

conn.close()

print("--- Total profit by category (calculated in Pandas) ---")
category_profit = df.groupby('category_name')['total_profit'].sum()
print(category_profit)

print("\n--- Generating plot... ---")

category_profit.plot(
    kind='bar',
    title='Total Profit by Category',
    xlabel='Category',
    ylabel='Total Profit ($)',
    color=['#1f77b4', '#ff7f0e', '#2ca02c']
)

plt.tight_layout()
plt.savefig('profit_by_category.png')
plt.show()

print("Plot window opened and 'profit_by_category.png' saved.")

