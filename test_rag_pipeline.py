from ragverse.rag.pipeline import RAGPipeline


pipeline = RAGPipeline()

question = "What are Imran Khan's technical skills?"

result = pipeline.prepare_prompt(question)

print("RAG pipeline prepared successfully!")
print("\nCitations:")
for citation in result["citations"]:
    print(citation)

print("\nPrompt:")
print("=" * 60)
print(result["prompt"])