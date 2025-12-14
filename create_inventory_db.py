import sqlite3

categories_data = [(1, 'Electronics'), (2, 'Clothing'), (3, 'Office')]
products_data = [
    (101, 'Laptop', 800.00, 1200.00, 1), (102, 'Phone', 500.00, 800.00, 1),
    (201, 'T-Shirt', 10.00, 25.00, 2), (202, 'Jeans', 30.00, 50.00, 2),
    (301, 'Desk Chair', 60.00, 150.00, 3)
]
sales_data = [
    (1, 101, 5, '2025-11-01'), (2, 102, 10, '2025-11-02'), (3, 201, 50, '2025-11-03'),
    (4, 301, 8, '2025-11-04'), (5, 101, 3, '2025-11-05'), (6, 202, 20, '2025-11-06'),
    (7, 201, 30, '2025-11-07')
]

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Sales")
cursor.execute("DROP TABLE IF EXISTS Products")
cursor.execute("DROP TABLE IF EXISTS Categories")

cursor.execute('''
CREATE TABLE Categories (
    category_id INT PRIMARY KEY, category_name TEXT
)''')

cursor.execute('''
CREATE TABLE Products (
    product_id INT PRIMARY KEY, product_name TEXT,
    cost_price REAL, selling_price REAL,
    category_id INT REFERENCES Categories(category_id)
)''')

cursor.execute('''
CREATE TABLE Sales (
    sale_id INT PRIMARY KEY, product_id INT REFERENCES Products(product_id),
    quantity_sold INT, sale_date TEXT
)''')

cursor.executemany("INSERT INTO Categories VALUES (?, ?)", categories_data)
cursor.executemany("INSERT INTO Products VALUES (?, ?, ?, ?, ?)", products_data)
cursor.executemany("INSERT INTO Sales VALUES (?, ?, ?, ?)", sales_data)

conn.commit()
conn.close()

print("inventory.db created successfully with all data.")
