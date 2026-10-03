from pathlib import Path

from ragverse.ingestion.extractors import extract_text_from_pdf


BASE_DIR = Path(__file__).resolve().parents[2]

PDF_FILE = Path(r"C:\Users\TSL\Downloads\Imran_Khan_Resume.pdf")


text = extract_text_from_pdf(PDF_FILE)

print("\n--- PDF EXTRACTED TEXT ---")
print(text)
print("\n--------------------------")