def build_citations(results) -> list[dict]:
    citations = []

    for index, result in enumerate(results, start=1):
        payload = result.payload or {}

        citations.append(
            {
                "citation_id": f"[Source {index}]",
                "document_name": payload.get("document_name", "Unknown"),
                "chunk_id": payload.get("chunk_id", "Unknown"),
                "chunk_index": payload.get("chunk_index", -1),
            }
        )

    return citations