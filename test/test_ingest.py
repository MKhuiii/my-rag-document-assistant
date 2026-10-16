import os

from src.ingestion.indexer import index_document


def test_ingest_document():
    """Bài test kiểm tra quy trình Chunking, Embedding và lưu vào PGVector."""
    sample_dir = "data/raw"
    os.makedirs(sample_dir, exist_ok=True)
    sample_file = os.path.join(sample_dir, "sample_test.txt")

    with open(sample_file, "w", encoding="utf-8") as f:
        f.write(
            "Dự án Local RAG Assistant được xây dựng dựa trên LangChain, PostgreSQL, pgvector và Ollama.\n"
            "Mô hình LLM chính được sử dụng là Qwen2.5:7b, kết hợp với mô hình Embedding là BGE-M3.\n"
            "Hệ thống cho phép người dùng nạp các tài liệu PDF và TXT để thực hiện tra cứu thông tin."
        )

    num_chunks = index_document(sample_file)
    assert num_chunks > 0


if __name__ == "__main__":
    test_ingest_document()
    print("Thành công!")
