import pandas as pd
import pyodbc

# Reading CSV file
Products_df = pd.read_csv("project data/Products.csv")

# Connection String (SQL Server)
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=course_project_1;"
    "Trusted_Connection=yes;"
)

# connection
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# entering data line by line
for index, row in Products_df.iterrows():
    cursor.execute("""
        INSERT INTO Products (ProductID, Product_Name, Category, Price, Supplier)
        VALUES (?, ?, ?, ?, ?)
    """,
    row['ProductID'],
    row['ProductName'],
    row['Category'],
    row['Price'],
    row['Supplier']
    )

# save changes
conn.commit()
conn.close()

print("Data inserted successfully into course_project")
