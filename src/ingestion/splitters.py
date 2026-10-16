from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import settings


def get_text_splitter() -> RecursiveCharacterTextSplitter:
    """
    Chiến lược cắt văn bản linh hoạt của LangChain.
    - chunk_size=512: Mỗi đoạn chứa tối đa khoảng 512 ký tự.
    - chunk_overlap=50: 50 ký tự cuối của đoạn 1 sẽ lặp lại ở đầu đoạn 2
      để đảm bảo không bị đứt đoạn ý nghĩa ở ranh giới cắt.
    """
    return RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""],
    )
