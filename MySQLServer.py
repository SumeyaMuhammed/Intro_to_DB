import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A_very_long_and_random_password_9876!",
)

mycursor = mydb.cursor()
try:
  mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
  print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

mycursor.close()
mydb.close()

