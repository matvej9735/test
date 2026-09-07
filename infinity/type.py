import asyncio
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r'^\.type(?:\s+(.*))?$', outgoing=True))
    async def type_handler(event):
        text = event.pattern_match.group(1)
        if not text:
            await event.edit("<b>⌨️ Использование:</b> <code>.type [текст]</code>", parse_mode="html")
            return
        
        if len(text) > 120:
            await event.edit("<b>⚠️ Максимум 120 символов.</b>", parse_mode="html")
            return

        typed = ""
        for char in text:
            typed += char
            await event.edit(f"<code>{typed}▒</code>", parse_mode="html")
            await asyncio.sleep(0.1)
        await event.edit(f"<code>{typed}</code>", parse_mode="html")