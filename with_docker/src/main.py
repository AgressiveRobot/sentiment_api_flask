from flask import Flask
import re
import sqlite3
import os
# HTTPERRORS!!!


# Sentiments module / Работа с отзывами
app = Flask(__name__)

# Работа с БД (перенесено из db.py для упрощения проекта)

DB_PATH = 'reviews.db'



#  Функции обработки сообщений
def get_sentiment_mark(message:str) -> int : #Определить настроение сообщения 
    sentiment_score = 0

    # Проходим по каждому типу настроения
    for sentiment, roots in keywords.items():
        for root in roots:
            # Создаем regex для поиска слов с этим корнем и любыми окончаниями
            pattern = r'\b' + re.escape(root) + r'[а-яё]*\b'
            matches = re.findall(pattern, message, flags=re.IGNORECASE)
            count = len(matches)
            if sentiment == 'positive':
                sentiment_score += count  # +1 за каждое положительное слово
            elif sentiment == 'negative':
                sentiment_score -= count  # -1 за каждое негативное слово

    return sentiment_score

#  Методы API

@app.route('/reviews', methods=['POST'])  # 1. Добавление отзыва из json-объекта
def add_review(): 
    data = request.get_json()              # Принимаем JSON { "text": "ваш отзыв" } 
    if not data or 'text' not in data:       #Проверяем данные на валидность
      return None              # !!! Обработка HTTPERRORS

    text = data['text'] 
    sentiment = get_sentiment_mark(text)
    created_at = datetime.utcnow().isoformat()
    




@app.route('/reviews', methods=['GET'])
