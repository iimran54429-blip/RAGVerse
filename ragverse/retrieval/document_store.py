from ragverse.retrieval.qdrant_client import (
    QdrantVectorStore,
    COLLECTION_NAME,
)


def get_all_documents() -> list[dict]:
    vector_store = QdrantVectorStore()

    points, _ = vector_store.client.scroll(
        collection_name=COLLECTION_NAME,
        limit=100,
        with_payload=True,
        with_vectors=False,
    )

    documents = []

    for point in points:
        payload = point.payload or {}
        text = payload.get("text", "")

        if text:
            documents.append(
                {
                    "text": text,
                    "document_name": payload.get(
                        "document_name",
                        "Unknown Document",
                    ),
                    "chunk_id": payload.get(
                        "chunk_id",
                        str(point.id),
                    ),
                    "chunk_index": payload.get(
                        "chunk_index",
                        0,
                    ),
                }
            )

    return documents