from ragverse.retrieval.retriever import Retriever
from ragverse.rag.citations import build_citations


retriever = Retriever()

question = "What are Imran Khan's technical skills?"

results = retriever.retrieve(
    query=question,
    top_k=3,
)

citations = build_citations(results)

print("Citations:")
print("=" * 60)

for citation in citations:
    print(citation)