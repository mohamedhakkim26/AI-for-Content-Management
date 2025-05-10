import streamlit as st
from app.ocr import extract_text
from app.agent_runner import run_agent
from app.agent_tools import set_cached_documents

def run_ui():
    st.title("📄 Document Text Extractor & AI Agent QA")

    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "png", "jpg", "jpeg", "txt"])

    if uploaded_file:
        st.success("✅ File uploaded!")

        text, _ = extract_text(uploaded_file, uploaded_file.type)

        st.subheader("📤 Extracted Text")
        st.text_area("Text", text, height=200)

        if not text.strip():
            st.warning("No text extracted from the document.")
            return

        # Set the document text in global cache for the agent tool
        set_cached_documents([text])

        st.subheader("🔍 Enter Query")
        query = st.text_input("Enter your query:")

        if query.strip():
            st.info("Processing your query...")
            response = run_agent(query)
            st.subheader("🔍 Query Result")
            st.write(response)
