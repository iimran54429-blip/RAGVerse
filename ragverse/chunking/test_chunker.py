from ragverse.chunking.chunker import chunk_text


text = """
RAGVerse is an Advanced AI Knowledge Assistant.

It uses Retrieval-Augmented Generation to answer questions
from user-provided documents.

Documents are extracted, cleaned, chunked and later converted
into embeddings for vector search.
"""


document_id = "doc_001"


chunks = chunk_text(
    text=text,
    document_id=document_id,
    chunk_size=100,
    chunk_overlap=20,
)


print("\n--- CHUNKS ---")

for chunk in chunks:
    print(f"\nChunk ID: {chunk.chunk_id}")
    print(f"Document ID: {chunk.document_id}")
    print(f"Chunk Index: {chunk.chunk_index}")
    print(f"Text: {chunk.text}")

print("\n----------------")
print(f"Total chunks: {len(chunks)}")