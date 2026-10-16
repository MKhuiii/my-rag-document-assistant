import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
)
from langchain_core.documents import Document


def load_single_document(file_path: str) -> list[Document]:
    """
    Tự động chọn loader phù hợp dựa trên đuôi tệp.
    """
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path, encoding="utf-8")
    elif ext in [".docx", ".doc"]:
        loader = UnstructuredWordDocumentLoader(file_path, mode="elements")
    else:
        raise ValueError(f"Định dạng tệp '{ext}' chưa được hỗ trợ.")

    return loader.load()
