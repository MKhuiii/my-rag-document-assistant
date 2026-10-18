from unittest.mock import MagicMock, patch

from src.rag.chains import create_rag_chain


def test_rag_chain_mock():
    """Test cấu trúc RAG Chain với Mock trong môi trường CI."""
    mock_retriever = MagicMock()
    mock_retriever.invoke.return_value = []

    mock_llm = MagicMock()
    mock_llm.invoke.return_value = "Đây là câu trả lời giả lập từ LLM."

    with (
        patch("src.chains.rag_chain.get_retriever", return_value=mock_retriever),
        patch("src.chains.rag_chain.get_llm", return_value=mock_llm),
    ):
        chain = create_rag_chain()
        result = chain.invoke("Dự án này sử dụng mô hình gì?")
        assert isinstance(result, str)


if __name__ == "__main__":
    print("--- ĐANG CHẠY BÀI TEST TRUY VẤN RAG THỰC TẾ (LOCAL) ---")
    rag_chain = create_rag_chain()

    query = "Dự án Local RAG Assistant sử dụng các công nghệ chính nào?"
    print(f"\nCâu hỏi: {query}")
    print("Đang suy luận...\n")

    response = rag_chain.invoke(query)
    print("Trả lời:")
    print(response)
