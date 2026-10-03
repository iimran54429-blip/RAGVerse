from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams


COLLECTION_NAME = "ragverse_documents"
VECTOR_SIZE = 384


class QdrantVectorStore:
    def __init__(self):
        self.client = QdrantClient(
            path="data/qdrant"
        )

    def create_collection(self):
        existing_collections = [
            collection.name
            for collection in self.client.get_collections().collections
        ]

        if COLLECTION_NAME not in existing_collections:
            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=VECTOR_SIZE,
                    distance=Distance.COSINE,
                ),
            )

    def add_chunk(
        self,
        point_id: int,
        embedding: list[float],
        payload: dict,
    ):
        self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload=payload,
                )
            ],
        )

    def search(
        self,
        query_vector: list[float],
        limit: int = 3,
    ):
        return self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=limit,
        ).points

    def get_collections(self):
        return self.client.get_collections()