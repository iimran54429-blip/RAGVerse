from rank_bm25 import BM25Okapi


class BM25Retriever:
    def __init__(self, documents: list[str]):
        self.documents = documents

        tokenized_documents = [
            document.lower().split()
            for document in documents
        ]

        self.bm25 = BM25Okapi(tokenized_documents)

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ) -> list[str]:
        if not query.strip():
            return []

        tokenized_query = query.lower().split()

        results = self.bm25.get_top_n(
            tokenized_query,
            self.documents,
            n=top_k,
        )

        return results