from langchain.tools import tool
from app.rag import answer_query_from_documents

# Global variable to hold extracted documents temporarily
cached_documents = []

@tool
def document_qa_tool(query: str) -> str:
    """
    Use this tool to answer a question using previously uploaded document content.
    Make sure to upload and extract the document before using this tool.
    """
    if not cached_documents:
        return "No documents found. Please upload a document first."
    return answer_query_from_documents(cached_documents, query)

def set_cached_documents(documents):
    global cached_documents
    cached_documents = documents
