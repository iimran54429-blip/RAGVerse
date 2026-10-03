from ragverse.retrieval.document_store import get_all_documents
from ragverse.reranking.reranker import Reranker


documents = get_all_documents()

reranker = Reranker()

question = "What are Imran Khan's technical skills?"

results = reranker.rerank(
    query=question,
    documents=documents,
    top_k=3,
)

print("Reranked Results:")
print("=" * 60)

for index, result in enumerate(results, start=1):
    print(f"\n--- Result {index} ---")
    print("Score:", result["score"])
    print(result["text"])