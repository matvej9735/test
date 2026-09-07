import random
import asyncio
from telethon import events

LAUGHS = ["ахахах", "АХАХАХАХ", "ахахаххаха", "аххаха", "ыаххаха", "АХАХАХАХАХАХ"]

def register(client):
    @client.on(events.NewMessage(pattern=r'^\.ha(?:\s+(\d+))?$', outgoing=True))
    async def ha_handler(event):
        count_arg = event.pattern_match.group(1)
        if not count_arg:
            await event.edit("<b>😂 Использование:</b> <code>.ha [количество 1–100]</code>", parse_mode="html")
            return
            
        count = int(count_arg)
        if not 1 <= count <= 100:
            await event.edit("<b>⚠️ Количество должно быть от 1 до 100.</b>", parse_mode="html")
            return

        await event.delete()
        for _ in range(count):
            msg = random.choice(LAUGHS)
            await event.respond(msg)
            await asyncio.sleep(0.2)