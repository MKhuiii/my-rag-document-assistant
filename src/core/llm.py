from langchain_ollama import ChatOllama

from src.config import OLLAMA_HOST, OLLAMA_MODEL


def get_llm() -> ChatOllama:

    return ChatOllama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_HOST,
        temperature=0 
    )