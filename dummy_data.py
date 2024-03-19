import sqlite3

# Connect to SQLite database (creates new database if not exists)
conn = sqlite3.connect('sales_database.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY,
        Age INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Items (
        ItemID INTEGER PRIMARY KEY,
        Name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sales (
        SaleID INTEGER PRIMARY KEY,
        CustomerID INTEGER,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        SaleID INTEGER PRIMARY KEY,
        CustomerID INTEGER,
        ItemID INTEGER,033
        Quantity INTEGER,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
        FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
    )
''')

# Insert sample data (optional)
cursor.execute('''
    INSERT INTO Customers (CustomerID, Age)
    VALUES
        (1, 21),
        (2, 23),
        (3, 35)
''')

cursor.execute('''
    INSERT INTO Items (ItemID, Name)
    VALUES
        (1, 'X'),
        (2, 'Y'),
        (3, 'Z')
''')

cursor.execute('''
    INSERT INTO Orders (SaleID, CustomerID, ItemID, Quantity)
    VALUES
        (1, 1, 1, 10),
        (2, 2, 1, 1),
        (3, 2, 2, 1),
        (4, 2, 3, 1),
        (5, 3, 3, 2)
''')

cursor.execute('''
    INSERT INTO Sales (SaleID, CustomerID)
    VALUES
        (1, 1),
        (2, 2),
        (3, 2),
        (4, 2),
        (5, 3)
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created successfully.")
