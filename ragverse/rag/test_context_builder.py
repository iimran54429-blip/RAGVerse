from ragverse.rag.context_builder import build_context
from ragverse.retrieval.retriever import Retriever


retriever = Retriever()

query = "What is RAGVerse?"

results = retriever.retrieve(
    query=query,
    top_k=3,
)

context = build_context(results)


print("\n--- CONTEXT BUILDER TEST ---")
print(context)
print("\n----------------------------")