from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from langchain_core.runnables import Runnable

from src.api.deps import get_rag_chain_dep
from src.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/chats", tags=["chats"])


@router.post("/api/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    rag_chain: Annotated[Runnable, Depends(get_rag_chain_dep)],
):
    """API gửi câu hỏi và nhận câu trả lời từ RAG Chain."""
    try:
        # Biến đổi lịch sử trò chuyện thành dạng text cho Prompt
        formatted_history = "\n".join(
            [f"{msg.role.capitalize()}: {msg.content}" for msg in request.history]
        )

        response = rag_chain.invoke(
            {
                "question": request.question,
                "chat_history": formatted_history
                if formatted_history
                else "Chưa có lịch sử.",
            }
        )
        return ChatResponse(answer=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi suy luận RAG: {e!s}") from e
