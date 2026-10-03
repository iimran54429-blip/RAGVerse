from ragverse.embeddings.embedder import EmbeddingModel
from ragverse.retrieval.qdrant_client import QdrantVectorStore


class Retriever:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = QdrantVectorStore()

        self.vector_store.create_collection()

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ):
        if not query.strip():
            return []

        query_embedding = self.embedding_model.embed_text(query)

        results = self.vector_store.search(
            query_vector=query_embedding,
            limit=top_k,
        )

        return results