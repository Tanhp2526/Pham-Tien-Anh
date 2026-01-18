from typing import List, Dict
class Memory:
    def __init_(self):
        self.items = [] #lịch sử cuộc hội thoại

    def add_memory(self, memory: dict):
        self.items.append(memory) #ghi nhớ memory

    def get_memories(self, limit: int = None) -> List[Dict]:
        return self.items[:limit]