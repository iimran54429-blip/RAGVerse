from ragverse.embeddings.embedder import EmbeddingModel


model = EmbeddingModel()

text = "RAGVerse is an AI knowledge assistant."

embedding = model.embed_text(text)

print("\n--- EMBEDDING TEST ---")
print(f"Vector length: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")
print("----------------------")