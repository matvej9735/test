import time
import asyncio

class MuteState:
    def __init__(self):
        self._mutes: dict[int, float] = {}
        self._lock = asyncio.Lock()

    async def set(self, chat_id: int, duration_sec: int):
        async with self._lock:
            self._mutes[chat_id] = time.time() + duration_sec

    async def is_muted(self, chat_id: int) -> bool:
        async with self._lock:
            until = self._mutes.get(chat_id)
            if until is None:
                return False
            if time.time() >= until:
                del self._mutes[chat_id]
                return False
            return True

    async def remove(self, chat_id: int):
        async with self._lock:
            self._mutes.pop(chat_id, None)

mute_state = MuteState()
