from langchain_core.prompts import ChatPromptTemplate

RAG_WITH_HISTORY_PROMPT = """Bạn là một trợ lý AI trung thực và chính xác. 
Hãy sử dụng ngữ cảnh (Context) được cung cấp dưới đây cùng với Lịch sử trò chuyện để trả lời câu hỏi.
Nếu ngữ cảnh không chứa đủ thông tin để trả lời, hãy nói rõ: "Tôi không tìm thấy thông tin phù hợp trong tài liệu."

Ngữ cảnh:
{context}

Lịch sử trò chuyện:
{chat_history}

Câu hỏi hiện tại: {question}
Câu trả lời:"""

qa_prompt = ChatPromptTemplate.from_template(RAG_WITH_HISTORY_PROMPT)
