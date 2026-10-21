import os
import shutil
from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile

from src.ingestion.indexer import index_document

router = APIRouter(prefix="/uploads", tags=["updates"])


@router.post("/")
def upload_document(file: Annotated[UploadFile, File()]):
    """API tải lên tài liệu và tự động Chunking/Embedding vào CSDL."""
    allowed_extensions = [".pdf", ".txt", ".docx", ".doc"]
    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Định dạng file không hỗ trợ. Chỉ hỗ trợ: {allowed_extensions}",
        )

    temp_dir = "data/raw"
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, file.filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        num_chunks = index_document(file_path)
        return {
            "message": f"Nạp tài liệu '{file.filename}' thành công!",
            "chunks_created": num_chunks,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xử lý file: {e!s}") from e
