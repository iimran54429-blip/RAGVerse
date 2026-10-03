from ragverse.ingestion.pipeline import process_document


PDF_PATH = r"C:\Users\TSL\Downloads\Imran_Khan_Resume.pdf"


result = process_document(PDF_PATH)

print("Document processed successfully!")
print("Document:", result["metadata"].document_name)
print("Chunks created:", len(result["chunks"]))
print("Chunks stored in Qdrant:", result["stored_chunks"])