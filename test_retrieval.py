from ragverse.retrieval.retriever import Retriever


retriever = Retriever()

question = "What are Imran Khan's technical skills?"

results = retriever.retrieve(
    query=question,
    top_k=3,
)

print("Retrieved chunks:", len(results))

for index, result in enumerate(results, start=1):
    print(f"\n--- Result {index} ---")
    print(result.payload.get("text", ""))