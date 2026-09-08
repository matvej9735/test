import sys
import os
import asyncio
import logging
import importlib
from threading import Thread
from flask import Flask

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from telethon import TelegramClient
from telethon.sessions import StringSession
from config import API_ID, API_HASH

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)

# 1. Создаем мини-веб-сервер для Keep-Alive (чтобы Fly.io не усыплял бота)
app = Flask(__name__)

@app.route("/")
def home():
    return "Userbot is alive and running!"

def run_web():
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def load_infinity_modules(client):
    """Автоматическая регистрация хэндлеров из папки infinity"""
    folder_name = "infinity"
    infinity_path = os.path.join(os.path.dirname(__file__), folder_name)

    if not os.path.exists(infinity_path):
        logging.error("Папка '%s' не найдена!", folder_name)
        return

    for file in os.listdir(infinity_path):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = f"{folder_name}.{file[:-3]}"
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, "register"):
                    module.register(client)
            except Exception as e:
                logging.error("Ошибка загрузки модуля %s: %s", file, e)

async def main():
    session_string = os.getenv("TG_SESSION", "")
    client = TelegramClient(StringSession(session_string), API_ID, API_HASH)

    load_infinity_modules(client)

    try:
        await client.start()
    except (EOFError, RuntimeError) as e:
        logging.error("Ошибка авторизации: %s", e)
        return

    me = await client.get_me()
    logging.info("Успешно запущен! Аккаунт: %s %s (@%s)", 
                 me.first_name, me.last_name or "", me.username or "без_юзернейма")

    await client.run_until_disconnected()

if __name__ == "__main__":
    # Запускаем веб-сервер в отдельном потоке
    web_thread = Thread(target=run_web)
    web_thread.daemon = True
    web_thread.start()

    # Запускаем юзербота
    asyncio.run(main())
