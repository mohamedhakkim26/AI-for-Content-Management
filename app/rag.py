from llama_index.core.indices.vector_store import VectorStoreIndex
from llama_index.core.schema import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv
import openai

load_dotenv()

def answer_query_from_documents(documents, query):
    if is_flagged_by_moderation(query):
        return "❌ Your query was flagged as potentially unsafe. Please revise it."

    docs = [Document(text=doc) for doc in documents]
    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    index = VectorStoreIndex.from_documents(docs, embed_model=embed_model)

    llm = OpenAI(
        model="gpt-3.5-turbo",
        temperature=0.1,
        api_key=os.getenv("NEXUS_API_KEY"),
        api_base=os.getenv("NEXUS_API_URL"),
    )

    query_engine = index.as_query_engine(llm=llm)
    response = query_engine.query(query)

    # Optionally check the LLM output too
    if is_flagged_by_moderation(str(response)):
        return "⚠️ The response generated was flagged as potentially unsafe."

    return str(response)

def is_flagged_by_moderation(content: str) -> bool:
    try:
        moderation_resp = openai.Moderation.create(input=content, api_key=os.getenv("NEXUS_API_KEY"))
        return moderation_resp['results'][0]['flagged']
    except Exception as e:
        print(f"Moderation check failed: {e}")
        return False  # Fail-open approach — you can change this