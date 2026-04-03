import pandas as pd
import pyodbc

# Reading CSV file
SaleDetails_df = pd.read_csv("project data/SaleDetails_200000.csv")

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
for index, row in SaleDetails_df.iterrows():
    cursor.execute("""
        INSERT INTO SaleDetails (SaleID, ProductID, Quantity, UnitPrice, TotalPrice)
        VALUES (?, ?, ?, ?, ?)
    """,
    row['SaleID'],
    row['ProductID'],
    row['Quantity'],
    row['UnitPrice'],
    row['TotalPrice']
    )

# save changes
conn.commit()
conn.close()

print("Data inserted successfully into course_project")
