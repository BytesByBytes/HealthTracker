import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Fk10pr20#",
    database="health_tracker"
)

print("Connected to MySQL")