from ragverse.retrieval.advanced_retriever import AdvancedRetriever


class CorrectiveRAG:
    def __init__(self, retriever=None):
        self.retriever = retriever or AdvancedRetriever()

    def retrieve(
        self,
        question: str,
        top_k: int = 3,
        minimum_score: float = -5.0,
    ) -> list[dict]:

        results = self.retriever.retrieve(
            query=question,
            top_k=top_k,
        )

        if not results:
            return []

        relevant_results = [
            result
            for result in results
            if result.get("score", -999) >= minimum_score
        ]

        if relevant_results:
            return relevant_results

        fallback_query = f"information related to {question}"

        return self.retriever.retrieve(
            query=fallback_query,
            top_k=top_k,
        )