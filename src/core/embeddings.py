from langchain_ollama import OllamaEmbeddings

from src.config import settings


def get_embedding_model() -> OllamaEmbeddings:

    return OllamaEmbeddings(
        model=settings.EMBEDDING_MODEL,
        base_url=settings.OLLAMA_HOST,
        dimensions=settings.EMBEDDING_DIM
    )