<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&pause=1000&color=2E9EF7&center=true&vCenter=true&width=600&lines=RAG-Powered+FAQ+Support+Chatbot;Retrieval+%2B+Generation+%2B+Fallback+Handling;Built+with+FastAPI+%2B+ChromaDB+%2B+Groq" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-orange?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3%2070B-F55036?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📖 Overview

A Retrieval-Augmented Generation (RAG) chatbot that answers questions strictly from a custom FAQ knowledge base. It embeds and stores FAQ content in ChromaDB, retrieves the most relevant chunks for any incoming question, and generates a grounded answer using an LLM — falling back to a "contact support" message instead of hallucinating when a question is out of scope.

## ✨ Features

- 📥 **Ingestion pipeline** — chunks FAQ data, generates embeddings, and stores them in a persistent ChromaDB vector store
- 🔍 **Query pipeline** — embeds the user's question, retrieves the top-3 most relevant chunks via similarity search, and builds a context-grounded prompt
- 🧠 **LLM-generated answers** via Groq's Llama 3.3 70B for fast inference
- 💬 Handles greetings and small talk (Hi, Hello, Thank you) naturally
- 🚫 Falls back to *"I don't have that information, please contact support"* for out-of-scope questions
- 🖥️ Lightweight front-end chat interface

## 🏗️ Architecture

```mermaid
flowchart TD
    A[User Question] --> B[Embed Question<br/>all-MiniLM-L6-v2]
    B --> C[Query ChromaDB<br/>Top-3 Similar Chunks]
    C --> D[Build Prompt<br/>System Instructions + Context + Question]
    D --> E[Groq LLM<br/>Llama 3.3 70B Versatile]
    E --> F[Grounded Answer<br/>or Fallback Message]
```

## 🛠️ Tech Stack

| Layer             | Technology                                  |
|--------------------|----------------------------------------------|
| Backend            | FastAPI                                      |
| Vector Database    | ChromaDB (persistent client)                 |
| Embedding Model    | `all-MiniLM-L6-v2` (Sentence Transformers)   |
| LLM                | Llama 3.3 70B Versatile (via Groq API)       |
| Language           | Python                                       |

## 📁 Project Structure

```
.
├── main.py              # FastAPI app: chat endpoint + query pipeline
├── ingest.py             # Ingestion script: builds the ChromaDB vector store
├── index.html            # Front-end chat interface
├── data/                  # Source FAQ data
├── schemas/                # Pydantic request/response models
├── chroma_db/               # Persistent vector store (generated, not committed)
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/kartik99kumar1/RAG_Support_Chat_Assistant_P01.git
cd RAG_Support_Chat_Assistant_P01
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Copy `.env.example` to `.env` and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run ingestion (builds the vector store from your FAQ data)
```bash
python ingest.py
```

### 6. Start the server
```bash
uvicorn main:app --reload --port 5500
```

### 7. Open the chat interface
Navigate to `http://127.0.0.1:5500/index.html`

## 🔌 API Reference

**POST** `/chat`

**Request**
```json
{
  "question": "What is your return policy?"
}
```

**Response**
```json
{
  "answer": "You can return any item within 30 days of purchase for a full refund, as long as it is unused and in original packaging."
}
```

## 🎥 Demo

> Add a GIF or screen recording of the chat interface here, e.g.:
> `![Demo](demo.gif)`

## 🚀 Future Improvements

- [ ] Multi-turn conversation memory
- [ ] Docker deployment
- [ ] Streaming responses
- [ ] Intent classification for smarter fallback routing
- [ ] Admin panel to update FAQ data without re-running ingestion

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">
Made with ⚡ by <a href="https://github.com/kartik99kumar1">Kartik Kumar</a>
</div>



Frontend: https://kartik99kumar1.github.io/RAG_Support_Chat_Assistant_P01/
Backend: https://rag-support-chat-assistant-p01.onrender.com
