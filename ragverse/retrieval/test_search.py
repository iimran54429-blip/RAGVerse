from ragverse.embeddings.embedder import EmbeddingModel
from ragverse.retrieval.qdrant_client import QdrantVectorStore


embedding_model = EmbeddingModel()
vector_store = QdrantVectorStore()

vector_store.create_collection()

query = "What is RAGVerse?"

query_embedding = embedding_model.embed_text(query)

results = vector_store.search(
    query_vector=query_embedding,
    limit=3,
)


print("\n--- SEARCH RESULTS ---")

for result in results:
    print(f"\nScore: {result.score}")
    print(f"Text: {result.payload.get('text')}")
    print(f"Document ID: {result.payload.get('document_id')}")
    print(f"Chunk Index: {result.payload.get('chunk_index')}")

print("\n----------------------")