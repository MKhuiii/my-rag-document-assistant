from functools import lru_cache

from langchain_core.runnables import Runnable

from src.rag.chains import create_rag_chain


@lru_cache
def get_rag_chain_dep() -> Runnable:
    """Khởi tạo RAG Chain 1 lần duy nhất (Singleton) cho toàn ứng dụng."""
    return create_rag_chain()
