import sqlite3

# Connect to SQLite database (creates new database if not exists)
conn = sqlite3.connect('/content/Data Engineer_ETL Assignment.db')
cursor = conn.cursor()


cursor.execute(
    '''
    SELECT O.quantity,C.customer_id,C.age,I.item_id,I.item_name
    FROM orders as O
    LEFT JOIN sales S ON O.sales_id=S.sales_id
    LEFT JOIN items I ON O.item_id=I.item_id
    LEFT JOIN customers C ON C.customer_id=S.customer_id

    '''
)
results = cursor.fetchall()

col_df=pd.DataFrame(results,columns=["Quantity","Customer","Age","Item","Name"])
# Filter customers aged 18 to 35
filtered_sales_df = col_df[(col_df['Age'] >= 18) & (col_df['Age'] <= 35)]
# print(filtered_sales_df)
# Perform aggregation
aggregated_df = filtered_sales_df.groupby(['Customer','Age','Name','Item'])['Quantity'].sum().reset_index()
aggregated_df.rename(columns={'Quantity':'total_quantity'},inplace=True)
# Filter out items with total quantity = 0
filtered_aggregated_df=aggregated_df[aggregated_df['total_quantity']>0]
# Write results to CSV file with semicolon delimiter
filtered_aggregated_df.to_csv('customer_items_aggregated.csv', sep=';', index=False)
print("Query results stored in customer_items.csv successfully.")
# # Commit changes and close connection
conn.commit()
conn.close()

# print("Database created successfully.")
