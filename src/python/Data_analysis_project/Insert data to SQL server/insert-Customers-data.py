import pandas as pd
import pyodbc

# Reading CSV file
Customers_df = pd.read_csv("project data/Customers.csv")

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
for index, row in Customers_df.iterrows():
    cursor.execute("""
        INSERT INTO Customers (CustomerID, Customer_Name,Gender, BirthDate, Phone_Number, Email, City)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    row['CustomerID'],
    row['Name'],
    row['Gender'],
    row['BirthDate'],
    row['Phone'],
    row['Email'],
    row['City']
    )

# save changes
conn.commit()
conn.close()

print("Data inserted successfully into course_project")
