from sentence_transformers import CrossEncoder


MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"


class Reranker:
    def __init__(self):
        self.model = CrossEncoder(MODEL_NAME)

    def rerank(
        self,
        query: str,
        documents: list[dict],
        top_k: int = 3,
    ) -> list[dict]:
        if not query.strip() or not documents:
            return []

        pairs = [
            [query, document["text"]]
            for document in documents
            if document.get("text")
        ]

        if not pairs:
            return []

        scores = self.model.predict(pairs)

        valid_documents = [
            document
            for document in documents
            if document.get("text")
        ]

        ranked_results = sorted(
            zip(valid_documents, scores),
            key=lambda item: float(item[1]),
            reverse=True,
        )

        results = []

        for document, score in ranked_results[:top_k]:
            results.append(
                {
                    "text": document["text"],
                    "score": float(score),
                    "document_name": document.get(
                        "document_name",
                        "Unknown Document",
                    ),
                    "chunk_id": document.get(
                        "chunk_id",
                        "unknown",
                    ),
                    "chunk_index": document.get(
                        "chunk_index",
                        0,
                    ),
                }
            )

        return results