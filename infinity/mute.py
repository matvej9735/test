import asyncio
from telethon import events

from utils import parse_duration
from state import mute_state

LOG_BOT = "@DelInfiiBot"

def register(client):
    @client.on(events.NewMessage(pattern=r'^unmute$', outgoing=True))
    async def unmute_handler(event):
        if not event.is_private:
            return
        await mute_state.remove(event.chat_id)
        await event.edit("🔊 Мут снят")

    @client.on(events.NewMessage(pattern=r'^mute(?:\s+(.*))?$', outgoing=True))
    async def mute_handler(event):
        if not event.is_private:
            await event.edit("Мут работает только в личных чатах")
            return

        args = event.pattern_match.group(1)
        if not args or not args.strip():
            await event.edit("🤐 <code>.mute [время]</code> — автоудаление сообщений", parse_mode="html")
            return

        duration_str = args.strip()
        duration_sec = parse_duration(duration_str)

        if duration_sec is None:
            await event.edit("Неверный формат времени. Пример: mute 10m, mute 2h")
            return

        await mute_state.set(event.chat_id, duration_sec)
        await event.edit(f"🔇 Вы в мьюте на {duration_str}")

    @client.on(events.NewMessage(incoming=True))
    async def auto_delete_handler(event):
        if not event.is_private:
            return
        if not await mute_state.is_muted(event.chat_id):
            return

        try:
            # Отправляем копию сообщения в бота перед удалением
            sender = await event.get_sender()
            sender_name = getattr(sender, 'first_name', 'Неизвестный')
            username = f"(@{sender.username})" if getattr(sender, 'username', None) else ""
            
            text_to_forward = (
                f"🗑 <b>Удалено сообщение из мута</b>\n"
                f"👤 <b>От:</b> {sender_name} {username} [<code>{event.chat_id}</code>]\n\n"
                f"💬 <b>Текст:</b> {event.text or '[Медиа/Вложение]'}"
            )
            
            await event.client.send_message(LOG_BOT, text_to_forward, parse_mode="html")
            if event.media:
                await event.client.send_file(LOG_BOT, event.media)
        except Exception:
            pass

        try:
            await event.delete()
        except Exception:
            pass