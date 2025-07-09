# Используем официальный образ Python slim облегченный
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта внутрь контейнера
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда по умолчанию — запуск main.py
CMD ["python", "main.py"]
