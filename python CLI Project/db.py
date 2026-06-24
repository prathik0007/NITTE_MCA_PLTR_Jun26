import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prathik@2005",
        database="hostel_db"
    )
