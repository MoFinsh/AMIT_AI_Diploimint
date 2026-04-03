import pandas as pd
import pyodbc

# Reading CSV file
Sales_df = pd.read_csv("project data/Sales_50000.csv")

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
for index, row in Sales_df.iterrows():
    cursor.execute("""
        INSERT INTO Sales (SaleID, CustomerID, BranchID, SaleDate, TotalAmount)
        VALUES (?, ?, ?, ?, ?)
    """,
    row['SaleID'],
    row['CustomerID'],
    row['BranchID'],
    row['SaleDate'],
    row['TotalAmount']
    )

# save changes
conn.commit()
conn.close()

print("Data inserted successfully into course_project")
