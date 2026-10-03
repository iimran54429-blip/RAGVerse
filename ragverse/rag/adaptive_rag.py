from ragverse.retrieval.advanced_retriever import AdvancedRetriever
from ragverse.rag.corrective_rag import CorrectiveRAG


class AdaptiveRAG:
    def __init__(self):
        # Create only ONE AdvancedRetriever.
        self.advanced_retriever = AdvancedRetriever()

        # Reuse the same retriever inside CorrectiveRAG.
        self.corrective_rag = CorrectiveRAG(
            retriever=self.advanced_retriever
        )

    def _is_complex(self, query: str) -> bool:
        words = query.split()

        complex_indicators = [
            "compare",
            "difference",
            "relationship",
            "why",
            "explain",
            "and",
            "also",
            "both",
            "between",
        ]

        query_lower = query.lower()

        return (
            len(words) > 12
            or any(
                indicator in query_lower
                for indicator in complex_indicators
            )
        )

    def retrieve(
        self,
        question: str,
        top_k: int = 3,
    ) -> list[dict]:

        if self._is_complex(question):
            return self.corrective_rag.retrieve(
                question=question,
                top_k=top_k,
            )

        return self.advanced_retriever.retrieve(
            query=question,
            top_k=top_k,
        )