# database.py

import sqlite3

DATABASE_FILE = "restaurant_database.db"

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurant_owners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            restaurant_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add this line at the end to create the table when this script is run
create_table()


def add_owner(username, password, restaurant_name):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO restaurant_owners (username, password, restaurant_name)
        VALUES (?, ?, ?)
    ''', (username, password, restaurant_name))
    conn.commit()
    conn.close()

def get_owner_by_username(username):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM restaurant_owners WHERE username = ?', (username,))
    owner = cursor.fetchone()
    conn.close()
    return owner
print("Database started...")