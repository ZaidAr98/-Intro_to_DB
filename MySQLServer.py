import mysql.connector

# Database connection details (replace with your own)
try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydb"
)
except mysql.connector.Error as err:
    print(f"Error: {err}")

mycursor = mydb.cursor()

# Create a table named `customers` (if it doesn't exist)
mycursor.execute("""
CREATE DATABASE IF NOT EXISTS alx_book_store
""")

print("Database 'alx_book_store' created successfully!")

# Close connections
mycursor.close()
mydb.close()

print("Database connection closed.")
