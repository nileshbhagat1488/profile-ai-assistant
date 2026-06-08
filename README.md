---
title: Profile AI Assistant
emoji: 🤖
colorFrom: gray
colorTo: white
sdk: docker
pinned: false
---

# 🤖 Personal Profile Assistant

An AI-powered RAG (Retrieval-Augmented Generation) chatbot that answers questions about my professional background using my LinkedIn profile and resume as knowledge sources.

🔗 LinkedIn: https://www.linkedin.com/in/your-linkedin-url
🐙 GitHub: https://github.com/nileshbhagat1488

---

## 💡 About This Project

I built this project to showcase my professional background in an interactive way.
Instead of sending a plain resume, anyone can visit this app and simply ask questions like:

- *"What are Nilesh's top skills?"*
- *"What projects has he worked on?"*
- *"What certifications does he have?"*

The app answers instantly using my actual LinkedIn profile and resume as the knowledge source — not made-up information.

The goal was to build a **real-world AI application from scratch** using modern tools like LlamaIndex, ChromaDB, and Groq — all completely free.

---

## 🧠 What is RAG?

RAG stands for **Retrieval-Augmented Generation**. Instead of relying on an LLM's general knowledge, it:

1. Loads your documents (LinkedIn PDF, Resume)
2. Splits them into small chunks
3. Converts chunks into vectors (numbers that represent meaning)
4. Stores vectors in ChromaDB
5. When a question is asked — finds the most relevant chunks
6. Passes those chunks to the LLM to generate a grounded answer

```
PDF/DOCX Documents
       ↓
  LlamaIndex splits into chunks
       ↓
  HuggingFace converts to vectors
       ↓
  ChromaDB stores vectors locally
       ↓
  User asks a question
       ↓
  ChromaDB finds relevant chunks
       ↓
  Groq LLM generates answer
       ↓
  Answer shown in chat UI
```

---

## 🛠️ Tech Stack

| Component        | Technology                          | Cost  |
|------------------|--------------------------------------|-------|
| LLM              | Groq — `llama-3.3-70b-versatile`    | Free  |
| Embeddings       | HuggingFace — `all-MiniLM-L6-v2`   | Free  |
| RAG Framework    | LlamaIndex                          | Free  |
| Vector Database  | ChromaDB                            | Free  |
| Web Framework    | Flask                               | Free  |
| Hosting          | Render                              | Free  |

**Total cost = $0**

---

## 🪜 Steps I Followed to Build This

### Step 1 — Project Setup
- Created project folder structure
- Set up Python virtual environment
- Installed all dependencies via `requirements.txt`

### Step 2 — Prepared Data Sources
- Exported LinkedIn profile as PDF
- Prepared resume as PDF
- Placed both files in the `data/` folder

### Step 3 — Built the Ingestion Pipeline (`ingest.py`)
- Used `SimpleDirectoryReader` from LlamaIndex to load PDFs
- Used HuggingFace `all-MiniLM-L6-v2` to generate embeddings (free, runs locally)
- Stored embeddings in ChromaDB (persistent local vector database)

### Step 4 — Built the Query Engine (`query_engine.py`)
- Connected LlamaIndex to ChromaDB
- Set up Groq LLM (`llama-3.3-70b-versatile`) — free and very fast
- Created a retriever that finds top 5 most relevant chunks per question

### Step 5 — Built the Flask Web App (`app.py`)
- Created REST API with two routes:
  - `GET /` → serves the chat UI
  - `POST /chat` → receives question, returns answer
- Connected Flask to the query engine

### Step 6 — Built the Chat UI
- Clean minimal white design using HTML + CSS
- Sidebar with profile photo, stats, domain tags, quick questions
- Chat window with typing animation
- Markdown rendering for formatted answers
- Fully responsive

### Step 7 — Deployed to GitHub + Render
- Pushed code to GitHub
- Deployed web service on Render (free tier)

---

## ✨ Features

- 💬 Interactive chat interface
- 📄 Powered by real LinkedIn profile and resume
- 🔍 Semantic search — understands meaning, not just keywords
- ⚡ Fast responses using Groq's custom LPU hardware
- 🆓 100% free stack
- 🎨 Clean minimal white UI
- ⌨️ Typing animation while answer loads
- 📋 Markdown formatted answers

---

## 📁 Project Structure

```
Personal-Profile-Assistant/
├── data/                  # LinkedIn PDF + Resume (not committed)
├── chroma_db/             # Vector database (auto-created by ingest.py)
├── static/
│   ├── css/style.css      # UI styling
│   ├── js/chat.js         # Chat logic
│   └── profile.png        # Profile photo
├── templates/
│   └── index.html         # Chat UI
├── ingest.py              # Run once to build vector index
├── query_engine.py        # LlamaIndex RAG logic
├── app.py                 # Flask web app
├── requirements.txt       # Python dependencies
└── .env                   # API keys (never commit this)
```

---

## ⚙️ Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/nileshbhagat1488/profile-ai-assistant.git
cd profile-ai-assistant
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free key at [console.groq.com](https://console.groq.com)

### 5. Add your documents
Place your LinkedIn PDF and Resume in the `data/` folder.

### 6. Build the vector index (run once)
```bash
python ingest.py
```

### 7. Run the app
```bash
python app.py
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 Example Questions

- *What are Nilesh's top technical skills?*
- *Summarize Nilesh's work experience*
- *What certifications does Nilesh have?*
- *What projects has Nilesh worked on?*
- *What is Nilesh's educational background?*
- *Which domains has Nilesh worked in?*

---

## 👨‍💻 About

Built by **Nilesh Bhagat** — Senior Data Engineer with 12+ years in IT and 6+ years in Data Engineering.
Domain expertise in Actuarial Analytics, Banking, and Oil & Gas.
