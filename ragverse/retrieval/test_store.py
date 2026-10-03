from ragverse.embeddings.embedder import EmbeddingModel
from ragverse.retrieval.qdrant_client import QdrantVectorStore


text = "RAGVerse is an Advanced AI Knowledge Assistant."

embedding_model = EmbeddingModel()
vector_store = QdrantVectorStore()

vector_store.create_collection()

embedding = embedding_model.embed_text(text)

vector_store.add_chunk(
    point_id=1,
    embedding=embedding,
    payload={
        "text": text,
        "document_id": "doc_001",
        "chunk_index": 0,
    },
)

print("\n--- QDRANT STORE TEST ---")
print("Chunk stored successfully!")
print(f"Vector length: {len(embedding)}")
print("-------------------------")