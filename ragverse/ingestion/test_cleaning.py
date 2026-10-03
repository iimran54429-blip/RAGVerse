from ragverse.ingestion.cleaner import clean_text


raw_text = """
   RAGVerse     is an Advanced AI Knowledge Assistant.


This project uses Retrieval-Augmented Generation.
"""


cleaned_text = clean_text(raw_text)

print("\n--- RAW TEXT ---")
print(raw_text)

print("\n--- CLEANED TEXT ---")
print(cleaned_text)
