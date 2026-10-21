from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str  # user hoặc assistant
    content: str


class ChatRequest(BaseModel):
    question: str
    history: list[ChatMessage] = []


class ChatResponse(BaseModel):
    answer: str
