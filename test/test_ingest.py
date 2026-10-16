import os

from src.ingestion.indexer import index_document

sample_dir = "data/raw"
os.makedirs(sample_dir, exist_ok=True)
sample_file = os.path.join(sample_dir, "sample_test.txt")

with open(sample_file, "w", encoding="utf-8") as f:
    f.write(
        "Dự án Local RAG Assistant được xây dựng dựa trên LangChain, PostgreSQL, pgvector và Ollama.\n"
        "Mô hình LLM chính được sử dụng là Qwen2.5:7b, kết hợp với mô hình Embedding là BGE-M3.\n"
        "Hệ thống cho phép người dùng nạp các tài liệu PDF và TXT để thực hiện tra cứu thông tin nhanh chóng và chính xác."
    )

print(f"1. Đã tạo tệp thử nghiệm tại: {sample_file}")
print("2. Đang tiến hành Chunking, Embedding và lưu vào PGVector...")

num_chunks = index_document(sample_file)

print(f"   -> Thành công! Đã xử lý và lưu {num_chunks} đoạn (chunks) vào Database.")