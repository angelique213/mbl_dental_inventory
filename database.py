import mysql.connector

# Create database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Angelique213",
        database="mbl_dental_clinic"
    )