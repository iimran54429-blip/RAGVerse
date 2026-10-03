from ragverse.memory.conversation_memory import ConversationMemory


class MemoryManager:
    def __init__(self, max_history: int = 10):
        self.memory = ConversationMemory()
        self.max_history = max_history

    def add_user_message(self, message: str) -> None:
        if message and message.strip():
            self.memory.add_user_message(message.strip())

    def add_assistant_message(self, message: str) -> None:
        if message and message.strip():
            self.memory.add_assistant_message(message.strip())

    def get_history(self) -> list[dict]:
        return self.memory.get_history(limit=self.max_history)

    def build_history_context(self) -> str:
        history = self.get_history()

        if not history:
            return ""

        lines = []

        for message in history:
            role = message.get("role", "unknown").capitalize()
            content = message.get("content", "").strip()

            if content:
                lines.append(f"{role}: {content}")

        return "\n".join(lines)

    def clear(self) -> None:
        self.memory.clear()