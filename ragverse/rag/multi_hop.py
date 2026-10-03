from ragverse.retrieval.advanced_retriever import AdvancedRetriever


class MultiHopRAG:
    """
    Performs retrieval in multiple hops.
    The first hop gathers initial information.
    The second hop searches using the gathered context.
    """

    def __init__(self):
        self.retriever = AdvancedRetriever()

    def retrieve(
        self,
        question: str,
        top_k: int = 3,
    ) -> list[dict]:

        first_hop = self.retriever.retrieve(
            query=question,
            top_k=top_k,
        )

        if not first_hop:
            return []

        context = " ".join(
            result["text"]
            for result in first_hop
        )

        second_query = f"{question} {context[:1000]}"

        second_hop = self.retriever.retrieve(
            query=second_query,
            top_k=top_k,
        )

        combined = []
        seen = set()

        for result in first_hop + second_hop:
            text = result["text"]

            if text not in seen:
                seen.add(text)
                combined.append(result)

        return combined[:top_k]