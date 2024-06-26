from typing import List
from langchain.docstore.document import Document
from ..document_chunking.Strategies import (
    get_document_chunker,
    ChunkingSettings,
    ChunkingStrategy,
)

__all__ = ["ChunkingStrategy"]


class DocumentChunking:
    def __init__(self) -> None:
        pass

    def chunk(
        self, documents: List[Document], chunking: ChunkingSettings
    ) -> List[Document]:
        chunker = get_document_chunker(chunking.chunking_strategy.value)
        if chunker is None:
            raise Exception(
                f"Unknown chunking strategy: {chunking.chunking_strategy.value}"
            )
        return chunker.chunk(documents, chunking)
