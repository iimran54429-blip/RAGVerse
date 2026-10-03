from ragverse.retrieval.document_store import get_all_documents
from ragverse.retrieval.hybrid_retriever import HybridRetriever


documents = get_all_documents()

print("Documents loaded:", len(documents))

retriever = HybridRetriever(documents)

question = "What are Imran Khan's technical skills?"

results = retriever.retrieve(
    query=question,
    top_k=3,
)

print("\nHybrid Results:")
print("=" * 60)

for index, result in enumerate(results, start=1):
    print(f"\n--- Result {index} ---")
    print(result)