import sqlite3
import os
from datetime import datetime

DB_PATH = 'reviews.db'

def init_db():
    """
    Создаёт базу данных и таблицу reviews, если их ещё нет. 
    Теперь используем все поля sentiments
    """
    if not os.path.exists(DB_PATH):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    sentiment_score INTEGER NOT NULL,
                    sentiment TEXT NOT NULL,
                    IsNegative INTEGER NOT NULL,
                    created_at DATETIME NOT NULL
                )
            ''')
            conn.commit()

def get_connection():
    """
    Возвращает новое соединение с базой данных.
    """
    return sqlite3.connect(DB_PATH)

def add_review(text, sentiment_score, sentiment, is_negative):
    """
    Добавляет новый отзыв в базу данных.
    """
    created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    is_negative_int = 1 if is_negative else 0
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reviews (text, sentiment_score, sentiment, IsNegative, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (text, sentiment_score, sentiment, is_negative_int, created_at))
        conn.commit()

def get_all_reviews():
    """
    Возвращает все отзывы из базы данных.
    Каждая запись — кортеж: (id, text, sentiment, IsNegative, created_at)
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, text, sentiment, IsNegative, created_at FROM reviews')
        return cursor.fetchall()
