import pandas as pd
import pyodbc

# 1️⃣ قراءة ملف CSV
df = pd.read_csv("Sales_50000.csv")

# 2️⃣ Connection String (SQL Server)
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=course_project_1;"
    "Trusted_Connection=yes;"
)

# 3️⃣ فتح الاتصال
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# 4️⃣ إدخال البيانات صف صف
for index, row in df.iterrows():
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

# 5️⃣ حفظ التغييرات
conn.commit()
conn.close()

print("✅ Data inserted successfully into course_project_")
