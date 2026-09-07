import asyncio
import random
from telethon import events


def register(client):
    @client.on(events.NewMessage(pattern=r'^mon$', outgoing=True))
    async def coin_handler(event):
        msg = event.message

        await msg.edit("🪙 Монетка подлетает и крутится...")

        for i in range(4):
            await asyncio.sleep(0.2)
            await msg.edit(f"🪙 Монетка подлетает и крутится{'.' * (i + 1)}")

        r = random.random()
        if r < 0.02:
            result = "РЕБРО"
            emoji = "🍀"
        else:
            result = random.choice(["ОРЁЛ", "РЕШКА"])
            emoji = "🦅" if result == "ОРЁЛ" else "🪙"

        await msg.edit(f"🌀 Результат подбрасывания:\n\n{emoji} Выпал {result}!")
