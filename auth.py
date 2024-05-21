from database import get_db_connection
from utils import hash_password, verify_password

def register(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO sauthusers (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
    except mysql.connector.IntegrityError:
        print("Username already exists")
    conn.close()

def login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM sauthusers WHERE username = %s", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and verify_password(result[0], password):
        return True
    return False
