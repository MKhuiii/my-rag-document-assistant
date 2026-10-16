from langchain_postgres import PGVector

from src.config import settings
from src.core.embeddings import get_embedding_model


def get_vector_store() -> PGVector:
    """
    Khởi tạo kết nối tới PostgreSQL sử dụng extension pgvector.
    LangChain tự động kết hợp mô hình embedding vào database để mã hóa dữ liệu đầu vào.
    """
    return PGVector(
        embeddings=get_embedding_model(),
        collection_name="rag_documents",
        connection=settings.DATABASE_URL,
        use_jsonb=True,
    )
