def build_context(results) -> str:
    """
    Convert retrieved Qdrant results into a context string.
    """

    if not results:
        return ""

    context_parts = []

    for index, result in enumerate(results, start=1):
        text = result.payload.get("text", "")

        if not text:
            continue

        context_parts.append(
            f"[Context {index}]\n{text}"
        )

    return "\n\n".join(context_parts)