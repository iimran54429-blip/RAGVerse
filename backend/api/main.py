from pathlib import Path
import shutil
import uuid

from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel

from ragverse.agents.graph import build_agent_graph
from ragverse.ingestion.pipeline import process_document


app = FastAPI(
    title="RAGVerse API",
    description="Advanced AI Knowledge Assistant API",
    version="1.0.0",
)

agent_graph = build_agent_graph()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    question: str
    answer: str
    citations: list
    route: str


@app.get("/")
def root():
    return {
        "name": "RAGVerse",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty.",
        )

    try:
        result = agent_graph.invoke(
            {
                "question": question,
            }
        )

        return QueryResponse(
            question=question,
            answer=result.get(
                "answer",
                "No answer generated.",
            ),
            citations=result.get(
                "citations",
                [],
            ),
            route=result.get(
                "route",
                "unknown",
            ),
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"RAG pipeline error: {exc}",
        ) from exc


@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
):
    allowed_extensions = {
        ".pdf",
        ".txt",
        ".docx",
    }

    extension = Path(file.filename or "").suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported file type. "
                "Use PDF, TXT, or DOCX."
            ),
        )

    document_id = uuid.uuid4().hex

    safe_filename = (
        f"{document_id}{extension}"
    )

    file_path = UPLOAD_DIR / safe_filename

    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        result = process_document(
            str(file_path)
        )

        return {
            "status": "success",
            "message": "Document indexed successfully.",
            "document_id": document_id,
            "filename": file.filename,
            "stored_as": safe_filename,
            "result": result,
        }

    except Exception as exc:
        if file_path.exists():
            file_path.unlink()

        raise HTTPException(
            status_code=500,
            detail=f"Document processing failed: {exc}",
        ) from exc