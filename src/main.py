from fastapi import FastAPI

from src.api.main import api_router

app = FastAPI(
    title="Local RAG Assistant API",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"status": "ok", "message": "RAG Assistant API đang hoạt động."}
