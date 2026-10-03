from pathlib import Path

from docx import Document
from pypdf import PdfReader


def extract_text_from_txt(file_path: str | Path) -> str:
    """
    Extract text from a TXT file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("This extractor only supports TXT files.")

    return path.read_text(
        encoding="utf-8",
        errors="replace",
    )


def extract_text_from_pdf(file_path: str | Path) -> str:
    """
    Extract text from a PDF file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("This extractor only supports PDF files.")

    reader = PdfReader(str(path))

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n\n".join(pages)


def extract_text_from_docx(file_path: str | Path) -> str:
    """
    Extract text from a DOCX file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".docx":
        raise ValueError("This extractor only supports DOCX files.")

    document = Document(str(path))

    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text)

    return "\n\n".join(paragraphs)