FROM python:3.11-slim

# Установка рабочей директории
WORKDIR /app

# Установка системных зависимостей (если требуются)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копирование и установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего исходного кода
COPY . .

# Настройка прав для файла запуска (если используется entrypoint.sh)
RUN chmod +x entrypoint.sh

# Запуск юзербота
CMD ["./entrypoint.sh"]
