from pathlib import Path
from uuid import uuid4
from datetime import datetime

from ragverse.ingestion.extractors import (
    extract_text_from_txt,
    extract_text_from_pdf,
    extract_text_from_docx,
)
from ragverse.ingestion.cleaner import clean_text
from ragverse.ingestion.models import DocumentMetadata
from ragverse.chunking.chunker import chunk_text
from ragverse.embeddings.embedder import EmbeddingModel
from ragverse.retrieval.qdrant_client import QdrantVectorStore


def process_document(file_path: str | Path):
    """
    Extract, clean, create metadata, chunk,
    embed and store a document in Qdrant.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    file_extension = path.suffix.lower()

    if file_extension == ".txt":
        raw_text = extract_text_from_txt(path)

    elif file_extension == ".pdf":
        raw_text = extract_text_from_pdf(path)

    elif file_extension == ".docx":
        raw_text = extract_text_from_docx(path)

    else:
        raise ValueError(
            "Unsupported file type. Only TXT, PDF and DOCX are supported."
        )

    cleaned_text = clean_text(raw_text)

    metadata = DocumentMetadata(
        document_id=str(uuid4()),
        document_name=path.name,
        source="upload",
        upload_date=datetime.now(),
        file_type=file_extension.replace(".", ""),
    )

    chunks = chunk_text(
        text=cleaned_text,
        document_id=metadata.document_id,
        chunk_size=500,
        chunk_overlap=50,
    )

    embedding_model = EmbeddingModel()
    vector_store = QdrantVectorStore()

    vector_store.create_collection()

    embeddings = embedding_model.embed_texts(
        [chunk.text for chunk in chunks]
    )

    for index, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):
        vector_store.add_chunk(
            point_id=index,
            embedding=embedding,
            payload={
                "text": chunk.text,
                "document_id": chunk.document_id,
                "chunk_id": chunk.chunk_id,
                "chunk_index": chunk.chunk_index,
                "document_name": metadata.document_name,
                "source": metadata.source,
                "file_type": metadata.file_type,
            },
        )

    return {
        "text": cleaned_text,
        "metadata": metadata,
        "chunks": chunks,
        "stored_chunks": len(chunks),
    }