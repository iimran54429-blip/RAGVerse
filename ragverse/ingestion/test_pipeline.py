from pathlib import Path

from ragverse.ingestion.pipeline import process_document


PDF_FILE = Path(
    r"C:\Users\TSL\Downloads\Imran_Khan_Resume.pdf"
)


result = process_document(PDF_FILE)


print("\n--- DOCUMENT ---")
print(f"Name: {result['metadata'].document_name}")
print(f"Document ID: {result['metadata'].document_id}")
print(f"File Type: {result['metadata'].file_type}")

print("\n--- CHUNKS ---")

for chunk in result["chunks"]:
    print(f"\nChunk ID: {chunk.chunk_id}")
    print(f"Chunk Index: {chunk.chunk_index}")
    print(f"Text: {chunk.text[:150]}...")

print("\n----------------")
print(f"Total chunks: {len(result['chunks'])}")