import sqlite3
import pandas as pd

df = pd.read_csv('sales_data.csv')
conn = sqlite3.connect('sales_database.db')

df.to_sql('transactions', conn, if_exists='replace', index=False)
print("SUCCESS: sales_database.db created and populated!")

query = """
SELECT 
    Product, 
    SUM(Total_Sales) AS Total_Revenue,
    COUNT(Order_ID) AS Total_Orders
FROM transactions
GROUP BY Product
ORDER BY Total_Revenue DESC;
"""

sql_result = pd.read_sql_query(query, conn)
print("\n=== THEOBROMA CAFE SUMMARY ===")
print(sql_result)

conn.close()