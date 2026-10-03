from datetime import datetime

from ragverse.ingestion.models import DocumentMetadata


metadata = DocumentMetadata(
    document_id="doc_001",
    document_name="test.txt",
    source="upload",
    upload_date=datetime.now(),
    file_type="txt",
)


print("\n--- DOCUMENT METADATA ---")
print(f"Document ID: {metadata.document_id}")
print(f"Document Name: {metadata.document_name}")
print(f"Source: {metadata.source}")
print(f"Upload Date: {metadata.upload_date}")
print(f"File Type: {metadata.file_type}")