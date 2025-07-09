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

import sqlite3
import os
from datetime import datetime

DB_PATH = 'reviews.db'

def init_db():
    # Создаем базу данных и таблицу, если их еще нет
    if not os.path.exists(DB_PATH):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    sentiment INTEGER NOT NULL,
                    created_at DATETIME NOT NULL
                )
            ''')
            conn.commit()

def get_connection():
    #Подключаемся к базе
    return sqlite3.connect(DB_PATH)

def add_review(text, sentiment):
    #Добавляем отзыв
    created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reviews (text, sentiment, created_at)
            VALUES (?, ?, ?)
        ''', (text, sentiment, created_at))
        conn.commit()

def get_all_reviews():
    #Получаем отзывы
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, text, sentiment, created_at FROM reviews')
        return cursor.fetchall()
