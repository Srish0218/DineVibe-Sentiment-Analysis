# database.py

import sqlite3
import hashlib
import os

DATABASE_FILE = "restaurant_database.db"

def create_table():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS restaurant_owners (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                restaurant_name TEXT NOT NULL
            )
        ''')

# Add this line at the end to create the table when this script is run
create_table()

def hash_password(password):
    # Use a secure hashing algorithm (e.g., SHA-256) to hash passwords
    return hashlib.sha256(password.encode()).hexdigest()

def add_owner(username, password, restaurant_name):
    hashed_password = hash_password(password)

    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO restaurant_owners (username, password, restaurant_name)
                VALUES (?, ?, ?)
            ''', (username, hashed_password, restaurant_name))
            conn.commit()
        except sqlite3.IntegrityError:
            # Handle the error (e.g., duplicate username)
            print("Error: Duplicate username")

def get_owner_by_username(username):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM restaurant_owners WHERE username = ?', (username,))
        owner = cursor.fetchone()

    return owner

if __name__ == "__main__":
    print("Database created...")
