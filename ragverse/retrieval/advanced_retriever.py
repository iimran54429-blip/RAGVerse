from ragverse.retrieval.document_store import get_all_documents
from ragverse.retrieval.hybrid_retriever import HybridRetriever
from ragverse.reranking.reranker import Reranker
from ragverse.query_processing.query_transformer import QueryTransformer


class AdvancedRetriever:
    def __init__(self):
        self.documents = get_all_documents()
        self.hybrid_retriever = HybridRetriever(self.documents)
        self.reranker = Reranker()
        self.query_transformer = QueryTransformer()

    def retrieve(self, query: str, top_k: int = 3) -> list[dict]:
        transformed_queries = self.query_transformer.transform(query)

        all_candidates = []
        seen_texts = set()

        for transformed_query in transformed_queries:
            candidates = self.hybrid_retriever.retrieve(
                query=transformed_query,
                top_k=10,
            )

            for candidate in candidates:
                text = candidate.get("text", "")

                if text and text not in seen_texts:
                    seen_texts.add(text)
                    all_candidates.append(candidate)

        results = self.reranker.rerank(
            query=query,
            documents=all_candidates,
            top_k=top_k,
        )

        return results