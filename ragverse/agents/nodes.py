from ragverse.agents.agent_state import AgentState
from ragverse.rag.adaptive_rag import AdaptiveRAG
from ragverse.rag.prompt import build_rag_prompt
from ragverse.llm.ollama_llm import OllamaLLM
from ragverse.memory.memory_manager import MemoryManager
from ragverse.graph_rag.graph_builder import build_graph_from_documents
from ragverse.graph_rag.graph_retriever import GraphRetriever


# Lazy-loaded components.
_adaptive_rag = None
_llm = None
_memory_manager = None
_graph_retriever = None


def get_adaptive_rag():
    global _adaptive_rag

    if _adaptive_rag is None:
        _adaptive_rag = AdaptiveRAG()

    return _adaptive_rag


def get_llm():
    global _llm

    if _llm is None:
        _llm = OllamaLLM()

    return _llm


def get_memory_manager():
    global _memory_manager

    if _memory_manager is None:
        _memory_manager = MemoryManager(max_history=10)

    return _memory_manager


def get_graph_retriever():
    global _graph_retriever

    if _graph_retriever is None:
        _graph_retriever = GraphRetriever()

    return _graph_retriever


def route_node(state: AgentState) -> AgentState:
    question = state["question"].strip()

    if len(question.split()) > 12:
        state["route"] = "complex"
    else:
        state["route"] = "simple"

    return state


def memory_node(state: AgentState) -> AgentState:
    memory_manager = get_memory_manager()

    state["conversation_history"] = (
        memory_manager.build_history_context()
    )

    return state


def retrieve_node(state: AgentState) -> AgentState:
    question = state["question"]

    adaptive_rag = get_adaptive_rag()

    results = adaptive_rag.retrieve(
        question=question,
        top_k=3,
    )

    state["documents"] = results

    return state


def graph_node(state: AgentState) -> AgentState:
    documents = state.get("documents", [])

    # Build graph from the documents retrieved for this query.
    graph_retriever = build_graph_from_documents(documents)

    graph_context_parts = []

    for document in documents:
        document_name = document.get("document_name")

        if not document_name:
            continue

        document_id = f"document::{document_name}"

        related_nodes = graph_retriever.retrieve_neighbors(
            document_id,
            max_hops=1,
        )

        for node in related_nodes:
            graph_context_parts.append(
                f"{node.node_type}: {node.name}"
            )

    state["graph_context"] = "\n".join(
        dict.fromkeys(graph_context_parts)
    )

    return state


def context_node(state: AgentState) -> AgentState:
    documents = state.get("documents", [])

    context_parts = []

    for index, document in enumerate(
        documents,
        start=1,
    ):
        text = document.get("text", "")

        if text:
            context_parts.append(
                f"[Context {index}]\n{text}"
            )

    state["context"] = "\n\n".join(context_parts)

    return state


def generate_answer_node(state: AgentState) -> AgentState:
    question = state["question"]

    context = state.get("context", "")
    graph_context = state.get("graph_context", "")
    conversation_history = state.get(
        "conversation_history",
        "",
    )

    documents = state.get("documents", [])

    if conversation_history:
        context = (
            "Conversation History:\n"
            f"{conversation_history}\n\n"
            "Retrieved Context:\n"
            f"{context}"
        )

    if graph_context:
        context = (
            f"{context}\n\n"
            "Knowledge Graph Context:\n"
            f"{graph_context}"
        )

    citations = []

    for index, document in enumerate(
        documents,
        start=1,
    ):
        citations.append(
            {
                "citation_id": f"[Source {index}]",
                "document_name": document.get(
                    "document_name",
                    "Retrieved Document",
                ),
                "chunk_id": document.get(
                    "chunk_id",
                    f"reranked_{index}",
                ),
                "chunk_index": document.get(
                    "chunk_index",
                    index - 1,
                ),
            }
        )

    prompt = build_rag_prompt(
        context=context,
        question=question,
        citations=citations,
    )

    llm = get_llm()

    answer = llm.generate(prompt)

    state["answer"] = answer
    state["citations"] = citations

    memory_manager = get_memory_manager()

    memory_manager.add_user_message(question)
    memory_manager.add_assistant_message(answer)

    return state