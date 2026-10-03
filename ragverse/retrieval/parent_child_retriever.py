from dataclasses import dataclass


@dataclass
class ParentDocument:
    parent_id: str
    text: str


@dataclass
class ChildChunk:
    child_id: str
    parent_id: str
    text: str


class ParentChildRetriever:
    """
    Creates small child chunks for retrieval while keeping
    a larger parent document for context.
    """

    def __init__(
        self,
        parent_size: int = 1500,
        child_size: int = 500,
        overlap: int = 50,
    ):
        self.parent_size = parent_size
        self.child_size = child_size
        self.overlap = overlap

    def create_parent_documents(
        self,
        text: str,
    ) -> list[ParentDocument]:

        if not text:
            return []

        parents = []
        start = 0
        index = 0

        while start < len(text):
            end = start + self.parent_size

            parents.append(
                ParentDocument(
                    parent_id=f"parent_{index}",
                    text=text[start:end].strip(),
                )
            )

            index += 1
            start = end

        return parents

    def create_child_chunks(
        self,
        parent: ParentDocument,
    ) -> list[ChildChunk]:

        children = []
        start = 0
        index = 0

        while start < len(parent.text):
            end = start + self.child_size

            children.append(
                ChildChunk(
                    child_id=f"{parent.parent_id}_child_{index}",
                    parent_id=parent.parent_id,
                    text=parent.text[start:end].strip(),
                )
            )

            index += 1
            start = end - self.overlap

        return children