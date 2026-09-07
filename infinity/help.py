import asyncio
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r'^\.?help$', outgoing=True))
    async def help_handler(event):
        me = await event.client.get_me()
        
        # Если команда написана НЕ в Избранном — просто бесшумно удаляем её
        if not event.is_private or event.chat_id != me.id:
            await event.delete()
            return

        # Имитация кнопки-плитки как на скриншоте
        menu_text = (
            "Выберите нужную команду:\n\n"
            "<code>┌───────────────┬───────────────┐</code>\n"
            "<code>│     .mute     │    .unmute    │</code>\n"
            "<code>├───────────────┼───────────────┤</code>\n"
            "<code>│     .type     │      .ha      │</code>\n"
            "<code>├───────────────┼───────────────┤</code>\n"
            "<code>│     .you      │     .fuck     │</code>\n"
            "<code>├───────────────┼───────────────┤</code>\n"
            "<code>│     .love     │ .доброе утро  │</code>\n"
            "<code>├───────────────┴───────────────┤</code>\n"
            "<code>│         .сладких снов         │</code>\n"
            "<code>├───────────────────────────────┤</code>\n"
            "<code>│             .spam             │</code>\n"
            "<code>├───────────────────────────────┤</code>\n"
            "<code>│           ‹ Закрыть           │</code>\n"
            "<code>└───────────────────────────────┘</code>"
        )

        await event.edit(menu_text, parse_mode="html")