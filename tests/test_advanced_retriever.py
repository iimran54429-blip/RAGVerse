from ragverse.retrieval.advanced_retriever import AdvancedRetriever


retriever = AdvancedRetriever()

question = "What are Imran Khan's technical skills?"

results = retriever.retrieve(
    query=question,
    top_k=3,
)

print("Advanced Retrieval Results:")
print("=" * 60)

for index, result in enumerate(results, start=1):
    print(f"\n--- Result {index} ---")
    print("Score:", result["score"])
    print(result["text"])