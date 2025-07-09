from flask import Flask, request, jsonify
from datetime import datetime
import re
import db
"""
После долгих метаний принято решение все же не упрощать и оставить методы связанные с базой в bd.py :) 
"""
app = Flask(__name__)

# Cловарь ключевых слов
keywords = {
    'positive': ['хорош', 'отличн', 'прекрасн','крут','восхитительн'],
    'negative': ['плох', 'ужасн', 'отвратительн','вашу ма']
}

#Основные функции определения настроения
def get_sentiment(message: str) -> dict:
    """
    Анализирует сообщение и возвращает словарь с результатами:
    - sentiment: 'positive', 'negative' или 'neutral' - (Искомое значение в задании)
    - score: числовой показатель настроения (- беск до + беск, допфича, ускоряем работу с базой, ну и можем найти самых эмоциональных коммментаторов :))
    - is_negative: булевое значение, указывающее на негативный настрой (позволяет быстро найти только негативные отзывы для анализа, булевое значение экономит память)
    """
    sentiment_score = 0
    for sentiment, roots in keywords.items(): 
        for root in roots:
            pattern = r'\b' + re.escape(root) + r'[а-яё]*\b'
            matches = re.findall(pattern, message, flags=re.IGNORECASE)
            count = len(matches)

            """
            Используем регулярные выражения чтобы найти все однокоренные с разными окончаниями.
            """
            if sentiment == 'positive':
                sentiment_score += count
            elif sentiment == 'negative':
                sentiment_score -= count
            """
            После формирования SENTIMENT_SCORE - используем его чтобы установить значение SENTIMENT текстом, как просит задание, а также булевое IsNegative
            """
    if sentiment_score > 0:
        sentiment_label = 'positive'
        is_negative = False
    elif sentiment_score < 0:
        sentiment_label = 'negative'
        is_negative = True
    else:
        sentiment_label = 'neutral'
        is_negative = False

    return {
        'sentiment': sentiment_label,
        'score': sentiment_score,
        'is_negative': is_negative
    }

@app.route('/reviews', methods=['POST'])
def add_review():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing "text" field'}), 400

        text = data['text']
        result = get_sentiment(text)

        # Передача данных в базу данных
        db.add_review(
            text,
            result['score'],
            result['sentiment'],
            result['is_negative']
        )

        response = {
            'text': text,
            'sentiment': result['sentiment'],
            'created_at': datetime.utcnow().isoformat()
        }
        return jsonify(response), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reviews', methods=['GET'])
def get_reviews():
    try:
        reviews = db.get_all_reviews()
        result_list = []
        for r in reviews:
            result_list.append({
                'id': r[0],
                'text': r[1],
                'sentiment': r[2],
                'sentiment_score':r[5],
                'created_at': r[4]
            })
        return jsonify(result_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    db.init_db()
    app.run(debug=True)
