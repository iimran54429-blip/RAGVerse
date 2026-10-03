import re


class SelfQueryRetriever:
    """
    Extracts simple metadata filters from natural-language queries.
    """

    def parse_query(self, query: str) -> dict:
        if not query or not query.strip():
            return {
                "query": "",
                "filters": {},
            }

        filters = {}
        search_query = query.strip()

        file_types = {
            "pdf": "pdf",
            "document": "docx",
            "docx": "docx",
            "text": "txt",
            "txt": "txt",
        }

        query_lower = search_query.lower()

        for keyword, file_type in file_types.items():
            if keyword in query_lower:
                filters["file_type"] = file_type
                break

        source_match = re.search(
            r"source\s*[:=]\s*(\w+)",
            query_lower,
        )

        if source_match:
            filters["source"] = source_match.group(1)

        return {
            "query": search_query,
            "filters": filters,
        }