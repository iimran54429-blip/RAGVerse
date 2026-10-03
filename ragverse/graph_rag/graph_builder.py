from ragverse.graph_rag.graph_retriever import GraphRetriever


def build_graph_from_documents(
    documents: list[dict],
) -> GraphRetriever:
    """
    Build a lightweight knowledge graph from indexed documents.

    Each document is connected to its chunks.
    """

    graph_retriever = GraphRetriever()

    for document in documents:
        document_name = document.get(
            "document_name",
            "Unknown Document",
        )

        chunk_id = document.get("chunk_id")

        if not chunk_id:
            continue

        document_id = f"document::{document_name}"

        graph_retriever.add_document_relationship(
            document_id=document_id,
            document_name=document_name,
            chunk_id=chunk_id,
        )

    return graph_retriever