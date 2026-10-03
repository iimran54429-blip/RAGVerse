🤖 RAGVerse — Advanced AI Knowledge Assistant

RAGVerse is an AI-powered Knowledge Assistant built using Retrieval-Augmented Generation (RAG). It allows users to upload documents and ask questions, retrieves relevant information from those documents, reranks the results, and generates grounded answers with source citations using a local LLM.

🚀 Features

PDF, TXT and DOCX document support

Document parsing and chunking

Sentence Transformer embeddings

Local Qdrant vector database

Semantic vector search

BM25 keyword retrieval

Hybrid retrieval

Cross-encoder reranking

Query transformation

Adaptive RAG

Corrective RAG

Knowledge Graph foundation

LangGraph agent workflow

Conversation memory

Source citations

Local Ollama LLM

FastAPI backend

Streamlit frontend

🏗️ Architecture

User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
LangGraph Workflow
  │
  ├── Query Processing
  ├── Conversation Memory
  ├── Hybrid Retrieval
  │       ├── Vector Search
  │       └── BM25
  ├── Cross-Encoder Reranking
  ├── Adaptive / Corrective RAG
  ├── Knowledge Graph Context
  └── Context Construction
  │
  ▼
Ollama + Llama 3.2 3B
  │
  ▼
Answer + Citations

🔄 RAG Workflow

Document Upload
      ↓
Document Parsing
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
Qdrant Vector Database
      ↓
User Question
      ↓
Query Transformation
      ↓
Hybrid Retrieval
      ↓
Cross-Encoder Reranking
      ↓
Adaptive / Corrective RAG
      ↓
Knowledge Graph Context
      ↓
Context Construction
      ↓
Ollama LLM
      ↓
Answer + Source Citations

🛠️ Tech Stack

Programming

Python

Generative AI

Ollama

Llama 3.2 3B

LangGraph

Prompt Engineering

Retrieval-Augmented Generation

Retrieval & AI

Sentence Transformers

BM25

Hybrid Retrieval

Cross-Encoder Reranking

Adaptive RAG

Corrective RAG

Database

Qdrant Vector Database

Backend

FastAPI

Uvicorn

Pydantic

Frontend

Streamlit

Development

Git

GitHub

VS Code

📁 Project Structure

Rag Project/
│
├── backend/
│   └── api/
│       └── main.py
│
├── frontend/
│   └── app.py
│
├── ragverse/
│   ├── agents/
│   ├── graph_rag/
│   ├── llm/
│   ├── memory/
│   ├── query_processing/
│   ├── rag/
│   ├── reranking/
│   └── retrieval/
│
├── data/
│   ├── uploads/
│   └── qdrant/
│
├── tests/
│
├── .env
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository:

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd "Rag Project"

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

🤖 Ollama Setup

Install Ollama and pull the local model:

ollama pull llama3.2:3b

Make sure Ollama is running before starting RAGVerse.

RAGVerse uses a local LLM so the application does not depend on a paid cloud LLM API.

🔐 Environment Variables

Create a .env file in the project root:

APP_NAME=RAGVerse API
APP_VERSION=0.1.0
DEBUG=true

Do not commit private API keys, credentials or secrets to GitHub.

▶️ Running the Application

Start Backend

python -m uvicorn backend.api.main:app --host 127.0.0.1 --port 8000

Backend:

http://127.0.0.1:8000

Start Frontend

Open another terminal:

streamlit run frontend/app.py

Frontend:

http://localhost:8501

💬 Example

Example question:

What are my technical skills?

RAGVerse processes the question through its retrieval pipeline, finds relevant document chunks, reranks them, constructs context and generates an answer using the local Ollama model.

The response also includes source citations.

📚 Supported Documents

RAGVerse currently supports:

PDF

TXT

DOCX

Uploaded documents are processed, chunked, embedded and indexed into Qdrant.

🔍 Retrieval Pipeline

Semantic Retrieval

Questions are converted into embeddings and matched against document embeddings.

BM25 Retrieval

Keyword-based retrieval helps identify exact terms and phrases.

Hybrid Retrieval

Semantic and keyword results are combined to improve retrieval coverage.

Cross-Encoder Reranking

Retrieved documents are reranked using a cross-encoder based on query-document relevance.

Adaptive Retrieval

More complex queries can use additional corrective retrieval logic.

🧠 Advanced RAG Components

RAGVerse demonstrates multiple modern RAG concepts:

Query Transformation

Hybrid Retrieval

Cross-Encoder Reranking

Corrective RAG

Adaptive RAG

Conversation Memory

Knowledge Graph Context

LangGraph Workflow

Citation-aware Generation

🔗 API Endpoints

Health Check

GET /health

Query

POST /query

Example:

{
  "question": "What are my technical skills?"
}

Upload

POST /upload

Used to upload supported documents and index them for retrieval.

🎯 Project Objective

The goal of RAGVerse is to demonstrate an end-to-end AI Knowledge Assistant that combines document processing, information retrieval, vector databases, reranking, Generative AI, agent workflows, knowledge graph context and conversational memory.

🔮 Future Improvements

Multi-user authentication

Persistent user-specific memory

Advanced entity extraction

More sophisticated knowledge graph construction

Streaming LLM responses

Metadata filtering

Cloud deployment

RAG evaluation and observability

Additional document formats

👨‍💻 Author

Imran Khan

AI & Machine Learning | Data Science

GitHub: https://github.com/iimran54429-blip/Imran8524125-byte

LinkedIn: https://www.linkedin.com/in/imran-khan-5862aa396/

⭐ Project

RAGVerse — Advanced AI Knowledge Assistant

Built with Python, FastAPI, Streamlit, Qdrant, LangGraph, Sentence Transformers and Ollama.