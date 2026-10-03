from typing import TypedDict


class AgentState(TypedDict, total=False):
    question: str
    rewritten_query: str
    documents: list
    context: str
    answer: str
    citations: list
    route: str

    # Conversation memory
    conversation_history: str

    # Graph RAG
    graph_context: str