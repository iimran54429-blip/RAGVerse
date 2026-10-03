from ragverse.retrieval.retriever import Retriever
from ragverse.retrieval.bm25_retriever import BM25Retriever


class HybridRetriever:
    def __init__(self, documents: list[dict]):
        self.vector_retriever = Retriever()
        self.documents = documents

        text_documents = [
            document["text"]
            for document in documents
            if document.get("text")
        ]

        self.bm25_retriever = BM25Retriever(text_documents)

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ) -> list[dict]:
        vector_results = self.vector_retriever.retrieve(
            query=query,
            top_k=top_k,
        )

        keyword_results = self.bm25_retriever.retrieve(
            query=query,
            top_k=top_k,
        )

        combined = []

        # Vector results
        for result in vector_results:
            payload = result.payload or {}
            text = payload.get("text", "")

            if text:
                combined.append(
                    {
                        "text": text,
                        "document_name": payload.get(
                            "document_name",
                            "Unknown Document",
                        ),
                        "chunk_id": payload.get(
                            "chunk_id",
                            str(result.id),
                        ),
                        "chunk_index": payload.get(
                            "chunk_index",
                            0,
                        ),
                    }
                )

        # BM25 results
        for text in keyword_results:
            matching_document = next(
                (
                    document
                    for document in self.documents
                    if document.get("text") == text
                ),
                None,
            )

            if matching_document:
                candidate = matching_document.copy()

                if not any(
                    item["text"] == candidate["text"]
                    for item in combined
                ):
                    combined.append(candidate)

        return combined[:top_k]