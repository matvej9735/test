FROM python:3.11-slim

WORKDIR /app

# Устанавливаем зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Явно копируем папку с модулями и весь проект
COPY infinity/ ./infinity/
COPY . .

# Создаем папку под сессию и выставляем права
RUN mkdir -p /app/sessions && chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
