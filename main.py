import sys
import os
import asyncio
import logging
import importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from telethon import TelegramClient
from config import API_ID, API_HASH, SESSION_NAME, SESSION_DIR

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)

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
    session_path = os.path.join(SESSION_DIR, SESSION_NAME)
    client = TelegramClient(session_path, API_ID, API_HASH)

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
    asyncio.run(main())