from ragverse.retrieval.retriever import Retriever


retriever = Retriever()

query = "What is RAGVerse?"

results = retriever.retrieve(
    query=query,
    top_k=3,
)


print("\n--- RETRIEVER TEST ---")
print(f"Query: {query}")

for result in results:
    print("\nResult:")
    print(f"Score: {result.score}")
    print(f"Text: {result.payload.get('text')}")
    print(f"Document ID: {result.payload.get('document_id')}")
    print(f"Chunk Index: {result.payload.get('chunk_index')}")

print("\n----------------------")
print(f"Results found: {len(results)}")