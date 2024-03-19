import sqlite3
import csv
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('sales_database.db')
cursor = conn.cursor()

# Execute SQL query to get total quantities of each item bought per customer aged 18-35
cursor.execute('''
    SELECT O.Quantity,C.CustomerID,C.Age,I.ItemID,I.Name
    FROM Orders as O
    LEFT JOIN Sales S ON O.SaleID=S.SaleID
    LEFT JOIN Items I ON O.ItemID=I.ItemID
    LEFT JOIN Customers C ON C.CustomerID=S.CustomerID

''')

# Fetch all results
results = cursor.fetchall()
col_df=pd.DataFrame(results,columns=["Quantity","Customer","Age","Item","Name"])
# Filter customers aged 18 to 35
filtered_sales_df = col_df[(col_df['Age'] >= 18) & (col_df['Age'] <= 35)]
# Perform aggregation
aggregated_df = filtered_sales_df.groupby(['Customer','Age','Name','Item'])['Quantity'].sum().reset_index()
aggregated_df.rename(columns={'Quantity':'total_quantity'},inplace=True)
# Filter out items with total quantity = 0
filtered_aggregated_df=aggregated_df[aggregated_df['total_quantity']>0]
# # Write results to CSV file with semicolon delimiter
filtered_aggregated_df.to_csv('customer_items_aggregated.csv', sep=';', index=False)
# Close connection
conn.close()
print("Query results stored in customer_items.csv successfully.")
