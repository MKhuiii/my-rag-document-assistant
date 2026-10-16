from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import settings


def get_text_splitter() -> RecursiveCharacterTextSplitter:
    
    return RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""]
    )