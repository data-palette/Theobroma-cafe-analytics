import pandas as pd
import numpy as np

np.random.seed(42)

num_records = 500
products = ['Espresso', 'Latte', 'Cold Brew', 'Croissant', 'Matcha Latte']
regions = ['North', 'South', 'East', 'West']

data = {
    'Order_ID': np.arange(1000, 1000 + num_records),
    'Date': pd.date_range(start='2025-01-01', periods=num_records, freq='D').strftime('%Y-%m-%d'),
    'Product': np.random.choice(products, num_records),
    'Region': np.random.choice(regions, num_records),
    'Quantity': np.random.randint(1, 5, num_records),
    # Realistic INR cafe prices
    'UnitPrice': np.random.choice([150.00, 220.00, 260.00, 180.00, 290.00], num_records)
}

df = pd.DataFrame(data)
df['Total_Sales'] = df['Quantity'] * df['UnitPrice']

df.to_csv('sales_data.csv', index=False)
print("SUCCESS: Updated with INR pricing!")