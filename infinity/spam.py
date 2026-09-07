import asyncio
from telethon import events


def register(client):
    @client.on(events.NewMessage(pattern=r'^\.spam(?:\s+(.*))?$', outgoing=True))
    async def spam_handler(event):
        raw_args = event.pattern_match.group(1)
        
        # Если аргументы не переданы вообще
        if not raw_args:
            await event.edit("<b>Использование:</b> <code>.spam [кол-во] [текст]</code>", parse_mode="html")
            return

        # Разделяем на [количество, текст]
        parts = raw_args.strip().split(maxsplit=1)
        
        if len(parts) < 2 or not parts[0].isdigit():
            await event.edit("<b>Использование:</b> <code>.spam [кол-во] [текст]</code>", parse_mode="html")
            return

        count = int(parts[0])
        text = parts[1]

        # Ограничение 1 000 000
        if count > 1000000:
            await event.edit("❌ <b>Ошибка:</b> Максимальное количество сообщений — 1 000 000.", parse_mode="html")
            return

        # Кадры анимации подготовки 3x4
        prep_frames = [
            "⚙️ ⚙️ ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n\n⚡️ <i>Запуск спам-модуля...</i>",
            "🔴 ⚙️ ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n\n🔥 <i>Загрузка потоков... [1/12]</i>",
            "🔴 🔴 ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n\n🔥 <i>Формирование пакетов... [2/12]</i>",
            "🔴 🔴 🔴 ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n\n🔥 <i>Обход ограничений... [3/12]</i>",
            "🔴 🔴 🔴 🔴\n⚙️ ⚙️ ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n\n🚀 <b>Канал 1 готов!</b>",
            "🔴 🔴 🔴 🔴\n💣 ⚙️ ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n\n💣 <i>Разгон шлюзов... [5/12]</i>",
            "🔴 🔴 🔴 🔴\n💣 💣 ⚙️ ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n\n💣 <i>Синхронизация... [6/12]</i>",
            "🔴 🔴 🔴 🔴\n💣 💣 💣 ⚙️\n⚙️ ⚙️ ⚙️ ⚙️\n\n💣 <i>Усиление мощности... [7/12]</i>",
            "🔴 🔴 🔴 🔴\n💣 💣 💣 💣\n⚙️ ⚙️ ⚙️ ⚙️\n\n🚀 <b>Канал 2 готов!</b>",
            "🔴 🔴 🔴 🔴\n💣 💣 💣 💣\n💥 ⚙️ ⚙️ ⚙️\n\n💥 <i>Финализация... [9/12]</i>",
            "🔴 🔴 🔴 🔴\n💣 💣 💣 💣\n💥 💥 ⚙️ ⚙️\n\n💥 <i>Готовность 99%... [10/12]</i>",
            "🔴 🔴 🔴 🔴\n💣 💣 💣 💣\n💥 💥 💥 ⚙️\n\n💥 <i>ПРОБИВАНИЕ БАРЬЕРА! [11/12]</i>",
            "🔴 🔴 🔴 🔴\n💣 💣 💣 💣\n💥 💥 💥 💥\n\n🔥 <b>ВСЕ ПОТОКИ АКТИВИРОВАНЫ!</b>",
            f"⚡️ 💥 💥 ⚡️\n🔥 💣 💣 🔥\n⚡️ 💥 💥 ⚡️\n\n🚀 <b>СТАРТ РАССЫЛКИ:</b> <code>{count}</code> сообщений!",
        ]

        # Проигрывание анимации
        for frame in prep_frames:
            await event.edit(frame, parse_mode="html")
            await asyncio.sleep(0.18)

        # Удаляем сообщение с анимацией и начинаем рассылку
        await event.delete()

        for _ in range(count):
            await event.respond(text)
            await asyncio.sleep(0.15)