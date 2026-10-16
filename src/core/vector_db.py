from langchain_postgres import PGVector
from src.config import DATABASE_URL
from src.core.embeddings import get_embedding_model

def get_vector_store() -> PGVector:

    return PGVector(
        embeddings=get_embedding_model(),
        collection_name="rag_documents",
        connection=DATABASE_URL,
        use_jsonb=True
    )

