from src.core.llm import get_llm
from src.core.embeddings import get_embedding_model
from src.core.vector_db import get_vector_store

print("Connecting LLM ...")
llm = get_llm()
print("OK. LLM Model: ", llm.model)

print("Connecting Embedding Model...")
embed_model = get_embedding_model()
print("OK. Embedding Model: ", embed_model.model)

print("Connecting PostgeSQL Vector DB...")
vector = get_vector_store()
print("OK. Connected DB successfullly!")