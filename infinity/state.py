import asyncio

class StateManager:
    def __init__(self):
        self.muted_chats = set()
        self.cloned_chats = set()
        self.clone_counters = {}

    async def set_mute(self, chat_id: int):
        self.muted_chats.add(chat_id)

    async def remove_mute(self, chat_id: int):
        self.muted_chats.discard(chat_id)

    async def is_muted(self, chat_id: int) -> bool:
        return chat_id in self.muted_chats

    async def set_clone(self, chat_id: int):
        self.cloned_chats.add(chat_id)
        self.clone_counters[chat_id] = 0

    async def remove_clone(self, chat_id: int):
        self.cloned_chats.discard(chat_id)
        self.clone_counters.pop(chat_id, None)

    async def is_cloned(self, chat_id: int) -> bool:
        return chat_id in self.cloned_chats

    async def increment_clone(self, chat_id: int) -> int:
        count = self.clone_counters.get(chat_id, 0) + 1
        self.clone_counters[chat_id] = count
        return count

mute_state = StateManager()