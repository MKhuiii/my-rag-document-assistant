from src.core.vector_db import get_vector_store
from src.ingestion.loaders import load_single_document
from src.ingestion.splitters import get_text_splitter


def index_document(filepath: str) -> int:
    """
    Quy trình 3 bước:
    1. Đọc file văn bản thô
    2. Cắt thành các đoạn nhỏ (chunks)
    3. Tạo Embedding cho từng đoạn và lưu vào PostgreSQL (PGVector)

    Trả về: Số lượng chunks đã được lưu thành công.
    """

    # Đọc file
    document = load_single_document(filepath)

    # Cắt file
    splitter = get_text_splitter()
    chunks = splitter.split_documents(document)

    # Lưu vào PGVector
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)

    return len(chunks)
