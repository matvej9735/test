import os
import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH, SESSION_NAME, SESSION_DIR

async def main():
    session_path = os.path.join(SESSION_DIR, SESSION_NAME)
    client = TelegramClient(session_path, API_ID, API_HASH)
    
    print("🚀 Авторизация аккаунта...")
    await client.start()
    
    me = await client.get_me()
    print(f"✅ Успешно вошли как: {me.first_name} (@{me.username or 'без_юзернейма'})")
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())