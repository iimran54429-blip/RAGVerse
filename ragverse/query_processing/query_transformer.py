from typing import List


class QueryTransformer:
    """
    Transforms a user's question into better search queries
    for retrieval.
    """

    def transform(self, query: str) -> List[str]:
        if not query or not query.strip():
            return []

        query = query.strip()

        queries = [
            query,
            self._keyword_query(query),
        ]

        return list(dict.fromkeys(queries))

    def _keyword_query(self, query: str) -> str:
        words = query.lower().split()

        stop_words = {
            "what",
            "is",
            "are",
            "the",
            "a",
            "an",
            "of",
            "in",
            "on",
            "for",
            "and",
            "to",
            "does",
            "do",
            "how",
            "can",
            "tell",
            "me",
            "about",
        }

        keywords = [
            word.strip("?,.!") 
            for word in words
            if word.strip("?,.!") not in stop_words
        ]

        return " ".join(keywords)