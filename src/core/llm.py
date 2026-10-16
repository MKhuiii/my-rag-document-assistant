from langchain_ollama import ChatOllama

from src.config import settings


def get_llm() -> ChatOllama:

    return ChatOllama(
        model=settings.OLLAMA_MODEL,
        base_url=settings.OLLAMA_HOST,
        temperature=0 
    )