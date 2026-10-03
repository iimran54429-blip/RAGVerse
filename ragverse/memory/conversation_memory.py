from dataclasses import dataclass, field


@dataclass
class ConversationMemory:
    """
    Stores conversation history for the current session.
    """

    messages: list[dict] = field(default_factory=list)

    def add_user_message(self, message: str) -> None:
        self.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(self, message: str) -> None:
        self.messages.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def get_history(self, limit: int = 10) -> list[dict]:
        return self.messages[-limit:]

    def clear(self) -> None:
        self.messages.clear()