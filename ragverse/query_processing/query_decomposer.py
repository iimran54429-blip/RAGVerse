from typing import List


class QueryDecomposer:
    """
    Breaks a complex question into smaller searchable questions.
    """

    def decompose(self, query: str) -> List[str]:
        if not query or not query.strip():
            return []

        query = query.strip()

        separators = [
            " and ",
            " also ",
            " as well as ",
            " plus ",
        ]

        query_lower = query.lower()

        for separator in separators:
            if separator in query_lower:
                parts = query_lower.split(separator)

                questions = []

                for part in parts:
                    part = part.strip(" ?.,")
                    if part:
                        questions.append(part.capitalize())

                return questions

        return [query]