import re


class ContextCompressor:
    """
    Removes unnecessary text from retrieved documents
    while keeping query-relevant sentences.
    """

    def compress(
        self,
        query: str,
        documents: list[str],
        max_sentences: int = 5,
    ) -> list[str]:

        if not query.strip() or not documents:
            return []

        query_words = {
            word.lower()
            for word in re.findall(r"\b\w+\b", query)
            if len(word) > 2
        }

        compressed_documents = []

        for document in documents:
            sentences = re.split(
                r"(?<=[.!?])\s+",
                document,
            )

            scored_sentences = []

            for sentence in sentences:
                words = {
                    word.lower()
                    for word in re.findall(r"\b\w+\b", sentence)
                }

                score = len(query_words.intersection(words))

                if score > 0:
                    scored_sentences.append(
                        (score, sentence.strip())
                    )

            scored_sentences.sort(
                key=lambda item: item[0],
                reverse=True,
            )

            selected = [
                sentence
                for _, sentence in scored_sentences[:max_sentences]
            ]

            if selected:
                compressed_documents.append(
                    " ".join(selected)
                )

        return compressed_documents