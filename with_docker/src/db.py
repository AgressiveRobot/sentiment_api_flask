import sqlite3
import os

DB_PATH = 'reviews.db'

def init_db():
    # Создаем базу данных, если ее еще нет
    if not os.path.exists(DB_PATH):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    sentiment INTERGER NOT NULL,
                    created_at DATETIME NOT NULL
                )
            ''')
            conn.commit()

def get_connection():
    return sqlite3.connect(DB_PATH)
