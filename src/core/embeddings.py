from langchain_ollama import OllamaEmbeddings

from src.config import EMBEDDING_DIM, EMBEDDING_MODEL, OLLAMA_HOST


def get_embedding_model() -> OllamaEmbeddings:

    return OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url=OLLAMA_HOST,
        dimensions=EMBEDDING_DIM
    )