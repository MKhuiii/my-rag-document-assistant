from src.core.embeddings import get_embedding_model
from src.core.llm import get_llm


def test_llm_initialization():
    """Kiểm tra khởi tạo LLM thành công"""
    llm = get_llm()
    assert llm.model is not None

def test_embedding_initialization():
    """Kiểm tra khởi tạo Embedding Model thành công"""
    embed_model = get_embedding_model()
    assert embed_model.model is not None
