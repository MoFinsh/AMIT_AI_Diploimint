import pandas as pd
import pyodbc

# Reading CSV file
Branches_df = pd.read_csv("project data/Branches.csv")

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
for index, row in Branches_df.iterrows():
    cursor.execute("""
        INSERT INTO Branches (BranchID, Branch_Name, City, Branch_Address)
        VALUES (?, ?, ?, ?)
    """,
    row['BranchID'],
    row['BranchName'],
    row['City'],
    row['Address']
    )

# save changes
conn.commit()
conn.close()

print("Data inserted successfully into course_project")
