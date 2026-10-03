from pathlib import Path

from ragverse.ingestion.extractors import extract_text_from_txt


BASE_DIR = Path(__file__).resolve().parents[2]

TEST_FILE = BASE_DIR / "data" / "uploads" / "test.txt"


text = extract_text_from_txt(TEST_FILE)

print("\n--- EXTRACTED TEXT ---")
print(text)
print("----------------------")