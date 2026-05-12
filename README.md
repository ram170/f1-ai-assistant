# F1 AI Semantic Search Assistant

AI-powered semantic search system for Formula 1 race intelligence using:

- FastAPI
- Ollama
- ChromaDB
- Local Embedding Models
- Vector Search

This project demonstrates:
- embeddings
- vector databases
- semantic search
- retrieval pipelines
- AI backend architecture

---

# Features

- Local embedding generation using Ollama
- Persistent vector storage using ChromaDB
- Semantic similarity search
- FastAPI backend APIs
- Swagger API documentation
- F1-themed retrieval dataset

---

# Tech Stack

| Component | Technology |
|---|---|
| Backend API | FastAPI |
| Embedding Model | all-minilm (Ollama) |
| Vector Database | ChromaDB |
| Local Model Runtime | Ollama |
| Language | Python 3.12 |

---

# Project Structure

```text
f1-ai-assistant/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   └── search_routes.py
│   │
│   ├── services/
│   │   ├── embedding_service.py
│   │   ├── chroma_service.py
│   │   └── search_service.py
│   │
│   ├── data/
│   │   └── sample_races.py
│   │
│   └── db/
│       └── chroma_db/
│
├── venv/
├── requirements.txt
└── README.md
```

---

# Local Setup

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd f1-ai-assistant
```

---

## 2. Install Python

Recommended:
- Python 3.12+

Check version:

```bash
python3 --version
```

---

## 3. Create Virtual Environment

```bash
python3.12 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

OR manually:

```bash
pip install fastapi uvicorn chromadb ollama pydantic
```

---

# Ollama Setup

## Install Ollama

Official website:

https://ollama.com

OR using Homebrew:

```bash
brew install ollama
```

---

## Start Ollama

```bash
ollama serve
```

Keep this terminal running.

---

## Pull Embedding Model

```bash
ollama pull all-minilm
```

---

# Run Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application runs at:

```text
http://127.0.0.1:8000
```

---

# Swagger API Docs

FastAPI automatically generates API docs:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Ingest Sample Data

### POST `/ingest`

Generates embeddings and stores F1 race data into ChromaDB.

---

## Semantic Search

### GET `/search`

Example:

```text
/search?query=Ferrari strategy mistakes
```

Returns semantically similar race documents.

---

## Debug Stored Data

### GET `/debug/all`

Returns all stored documents from ChromaDB.

---

# How Semantic Search Works

1. Race documents are converted into embeddings
2. Embeddings are stored in ChromaDB
3. User query is converted into embedding
4. ChromaDB performs nearest-neighbor vector search
5. Most semantically similar documents are returned

---

# Example Query

Input:

```text
Ferrari strategy mistakes
```

Possible Result:

```text
Ferrari lost Monaco GP due to poor pit strategy and tire timing.
```

Even though exact keywords differ.

---

# Future Improvements

- Add metadata filtering
- Add RAG workflow
- Add local LLM responses
- Add race ingestion pipeline
- Add frontend UI
- Add hybrid search
- Add reranking

---

# Key AI Concepts Demonstrated

- Embeddings
- Vector Databases
- Semantic Search
- Similarity Search
- Retrieval Systems
- RAG Foundations
- AI Backend Architecture

---

# Notes

- ChromaDB is configured with persistent local storage
- Embeddings are generated locally using Ollama
- No paid API usage required
- Optimized for Apple Silicon Macs

---

# Useful Links

- FastAPI: https://fastapi.tiangolo.com
- Ollama: https://ollama.com
- ChromaDB: https://www.trychroma.com

---

# License

MIT