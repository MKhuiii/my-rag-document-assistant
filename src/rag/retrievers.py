from langchain_core.vectorstores import VectorStoreRetriever

from src.core.vector_db import get_vector_store


def get_retriever(k: int = 3) -> VectorStoreRetriever:
    """Khởi tạo Retriever để truy vấn dữ liệu từ PGVector."""

    vector_store = get_vector_store()
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k},
    )
