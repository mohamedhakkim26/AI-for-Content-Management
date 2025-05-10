📄 Document QA: Extract Text and Ask Questions with RAG + Streamlit

This is a simple yet powerful Document QA (Question Answering) application that allows users to upload documents (PDFs, images, or text files), extract their content using OCR/NLP, and ask questions about the content using a Retrieval-Augmented Generation (RAG) pipeline powered by LLMs (OpenAI GPT-3.5-Turbo) and Hugging Face embeddings.

---

🚀 Features

- 📤 Upload PDF, PNG, JPG, JPEG, or TXT files
- 🧠 Extract text using:
  - OCR (`pytesseract`) for images
  - Native text extraction for PDFs
- 💬 Ask natural language questions based on the uploaded document
- 🦙 Uses a RAG pipeline with:
  - `llama-index` for document indexing and retrieval
  - `langchain` and OpenAI for intelligent QA agents
- 🌐 Streamlit-based UI for easy interaction

---

📁 Project Structure

app/
├── agent_runner.py # Sets up the LangChain agent
├── agent_tools.py # LangChain tool wrapper around RAG
├── ocr.py # Text extraction from images and PDFs
├── rag.py # Core RAG logic for QA over documents
├── ui.py # Streamlit UI interface
main.py # Entry point to launch the Streamlit app
requirements.txt # Required Python packages

---

🛠️ Setup Instructions

1. Clone the repository:

git clone https://github.com/your-username/document-qa-app.git
cd document-qa-app

2. Install dependencies:

It’s recommended to use a virtual environment:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

3.Install Tesseract OCR Engine:

macOS: brew install tesseract

Ubuntu: sudo apt install tesseract-ocr

Windows: https://github.com/tesseract-ocr/tesseract

4.Create a .env file:

Create a .env file in the root directory with the following variables:

NEXUS_API_KEY=your_openai_api_key
NEXUS_API_URL=https://api.openai.com/v1

Replace with your actual OpenAI API credentials or proxy service.

▶️ Run the App : streamlit run main.py

🧪 Example Usage
Upload a document (PDF or image).

View extracted text.

Enter a natural language query such as:

“What is the main point of this document?”

“List any dates or deadlines mentioned.”

View the AI-generated answer based on the document contents.

🧰 Built With

Streamlit — For UI

LlamaIndex — For indexing and vector retrieval

LangChain — For agents and tools

OpenAI GPT-3.5 — For LLM responses

Tesseract OCR — For image-to-text

PyMuPDF — For PDF reading

📌 Notes

This project uses a fail-open approach for moderation — unsafe content detection will log a warning and return a generic message.

Future improvements could include better chunking, history-based Q&A, and support for multiple documents.

🙋‍♀️ Questions?
Feel free to open an issue or contact the maintainer.

