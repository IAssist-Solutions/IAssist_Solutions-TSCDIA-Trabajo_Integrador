import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='habit',
            user='root',
            password='admin'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()