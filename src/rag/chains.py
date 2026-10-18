
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from src.core.llm import get_llm
from src.rag.retrievers import get_retriever

RAG_PROMPT_TEMPLATE = """Bạn là một trợ lý AI trung thực và chính xác. Hãy trả lời câu hỏi dựa CHỈ vào ngữ cảnh (Context) được cung cấp dưới đây.
Nếu ngữ cảnh không chứa đủ thông tin để trả lời, hãy trả lời ngắn gọn: "Tôi không tìm thấy thông tin phù hợp trong tài liệu."

Ngữ cảnh:
{context}

Câu hỏi:
{question}

Câu trả lời:"""


def format_docs(docs: list[Document]) -> str:
    """Gộp nội dung các chunks tìm được thành 1 chuỗi văn bản"""
    return "\n\n---\n\n".join(doc.page_content for doc in docs)


def create_rag_chain():
    """Khởi tạo RAG Chain bằng LCEL (LangChain Expression Language)"""
    retriever = get_retriever()
    llm = get_llm()
    prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain
