from ragverse.chunking.chunker import chunk_text
from ragverse.embeddings.embedder import EmbeddingModel


text = """
RAGVerse is an Advanced AI Knowledge Assistant.

It uses Retrieval-Augmented Generation to answer questions
from user-provided documents.

Documents are extracted, cleaned, chunked and converted
into embeddings for vector search.
"""


document_id = "doc_001"


chunks = chunk_text(
    text=text,
    document_id=document_id,
    chunk_size=100,
    chunk_overlap=20,
)


embedding_model = EmbeddingModel()


print("\n--- CHUNK EMBEDDINGS ---")

for chunk in chunks:
    embedding = embedding_model.embed_text(chunk.text)

    print(f"\nChunk ID: {chunk.chunk_id}")
    print(f"Chunk Index: {chunk.chunk_index}")
    print(f"Vector Length: {len(embedding)}")
    print(f"First 5 Values: {embedding[:5]}")

print("\n------------------------")
print(f"Total chunks: {len(chunks)}")