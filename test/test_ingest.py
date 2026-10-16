import os
from unittest.mock import MagicMock, patch

from src.config import settings
from src.ingestion.indexer import index_document


def test_ingest_document():
    """Bài test kiểm tra quy trình Chunking và lưu vào PGVector (Mock Embedding cho CI)."""
    sample_dir = "data/raw"
    os.makedirs(sample_dir, exist_ok=True)
    sample_file = os.path.join(sample_dir, "sample_test.txt")

    with open(sample_file, "w", encoding="utf-8") as f:
        f.write(
            "Dự án Local RAG Assistant được xây dựng dựa trên LangChain, PostgreSQL, pgvector và Ollama.\n"
            "Mô hình LLM chính được sử dụng là Qwen2.5:7b, kết hợp với mô hình Embedding là BGE-M3.\n"
            "Hệ thống cho phép người dùng nạp các tài liệu PDF và TXT để thực hiện tra cứu thông tin."
        )

    # 1. Giả lập (Mock) Embedding Model trả về vector 1024 chiều (đúng kích thước bge-m3)
    mock_embedding = MagicMock()
    mock_embedding.embed_documents.side_effect = lambda texts: [
        [0.1] * settings.EMBEDDING_DIM for _ in texts
    ]
    mock_embedding.embed_query.return_value = [0.1] * settings.EMBEDDING_DIM

    # 2. Bọc hàm index_document vào trong patch context
    with patch("src.core.vector_db.get_embedding_model", return_value=mock_embedding):
        num_chunks = index_document(sample_file)
        assert num_chunks > 0


if __name__ == "__main__":
    test_ingest_document()
    print("Test ingest thành công!")
