def build_rag_prompt(
    context: str,
    question: str,
    citations: list[dict] | None = None,
) -> str:
    citation_text = ""

    if citations:
        citation_lines = []

        for citation in citations:
            citation_lines.append(
                f"{citation['citation_id']} "
                f"{citation['document_name']} "
                f"(chunk {citation['chunk_index']})"
            )

        citation_text = "\n".join(citation_lines)

    return f"""
You are RAGVerse, an AI knowledge assistant.

Answer the user's question using only the provided context.

Rules:
1. Do not make up information.
2. If the answer cannot be found in the context, say:
   "I don't have enough information in the provided context."
3. Keep the answer clear and concise.
4. Use the available source references when appropriate.

Context:
{context}

Sources:
{citation_text}

Question:
{question}

Answer:
""".strip()