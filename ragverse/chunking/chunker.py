from dataclasses import dataclass


@dataclass
class TextChunk:
    chunk_id: str
    text: str
    document_id: str
    chunk_index: int


def chunk_text(
    text: str,
    document_id: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> list[TextChunk]:
    """
    Split text into overlapping chunks with metadata.
    """

    if not text:
        return []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0.")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative.")

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size."
        )

    chunks = []

    start = 0
    chunk_index = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(
                TextChunk(
                    chunk_id=f"{document_id}_chunk_{chunk_index}",
                    text=chunk,
                    document_id=document_id,
                    chunk_index=chunk_index,
                )
            )

            chunk_index += 1

        start = end - chunk_overlap

    return chunks