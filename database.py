import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="",
        port=3306,
        user="",
        password="",
        database="simpleauthentication"
    )

def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sauthusers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    """)
    conn.close()
