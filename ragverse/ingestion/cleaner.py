import re


def clean_text(text: str) -> str:
    """
    Clean extracted document text.
    """

    if not text:
        return ""

    # Replace multiple spaces/tabs with one space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace 3+ newlines with 2 newlines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove spaces at the beginning/end
    text = text.strip()

    return text