# 🤖 Codweb Lab AI Mentor Agent

A production-grade, highly scalable, and intelligent AI Mentor platform built using **FastAPI**, **Gemini Pro (Google GenAI)**, **ChromaDB**, and **LangGraph**. This project implements a strict modular architecture where the backend, frontend, asynchronous background workers, and the AI reasoning engine are completely decoupled.

---

## 🎯 What Does This AI Mentor Agent Do?

The **Codweb Lab AI Mentor Agent** is designed to act as a 24/7 autonomous technical guide for students and IT professionals. Instead of just answering generic questions, it uses advanced RAG (Retrieval-Augmented Generation) and multi-agent reasoning to provide deep, context-aware mentorship. 

**Key Capabilities:**
* 🧠 **Technical Upskilling & Mentorship:** Provides structured guidance, code reviews, and conceptual clarity for complex domains like Python, Data Analytics, Machine Learning, and Web Development.
* 📚 **Context-Aware Document Reading (RAG):** Users can upload technical PDFs, research papers, or documentation. The agent ingests this data into ChromaDB and answers highly specific queries based *only* on the provided context.
* 🛠️ **Autonomous Debugging:** Utilizing LangGraph, the agent doesn't just guess answers. It can autonomously execute tools, search for the latest documentation, and self-correct its logic before giving a final solution.
* 📈 **Career & Learning Path Mapping:** Helps professionals navigating career breaks or transitioning into new tech roles by generating step-by-step, customized learning roadmaps.
* ⚡ **Lightning Fast Responses:** By leveraging Redis caching and background Celery workers, it delivers sub-second responses for repeated architectural queries without hitting the LLM again.

---

## 🚀 Core Technologies (Tech Stack)
* **Backend:** FastAPI, Python 3.11+
* **Database:** PostgreSQL (with Asyncpg driver), SQLAlchemy, Alembic
* **AI & LLM:** Google Gemini Pro (`gemini-1.5-pro`), Langchain
* **Vector Store (RAG):** ChromaDB
* **Caching & Message Broker:** Redis
* **Background Jobs:** Celery
* **Agentic Workflows:** LangGraph
* **Frontend:** Streamlit
* **Infrastructure:** Docker, Docker Compose, GitHub Actions (CI/CD)

---

## 🗺️ Project Development Roadmap (Phase-Wise Breakdown)

This project is meticulously structured into 9 logical phases to ensure smooth, error-free development and to avoid early over-engineering:

### 🛠️ Phase 1: Foundation & Environment
* **Objective:** Establish the repository baseline and virtual environment.
* **Details:** Initialize `venv`, install required packages via `requirements.txt` (FastAPI, Langchain, Celery, etc.), and configure a robust `.gitignore` to prevent sensitive or junk files from entering version control.

### 🔐 Phase 2: Backend Core, Database & JWT Auth
* **Objective:** Secure the backend foundation.
* **Details:** Establish a non-blocking asynchronous connection to PostgreSQL using `asyncpg`. Create imperative SQLAlchemy ORM models (`Users`, `Chats`), manage structural migrations with Alembic, and secure all endpoints using asymmetric JWT tokens.

### 🧪 Phase 3: Testing & CI/CD
* **Objective:** Maintain code quality and automate regression testing.
* **Details:** Write atomic API tests using `pytest` and configure GitHub Actions (`ci.yml`) to automatically trigger validation checks upon every code push.

### 🧠 Phase 4: AI Core & RAG System (Gemini Pro)
* **Objective:** Inject document intelligence and semantic retrieval capabilities.
* **Details:** Integrate **Google Gemini Pro** as the core LLM. Build a Retrieval-Augmented Generation (RAG) engine by chunking uploaded PDFs and storing dense vector embeddings in ChromaDB.

### ⚡ Phase 5: Async Workers & Caching
* **Objective:** Offload heavy CPU tasks and accelerate query responses.
* **Details:** Introduce **Celery** to run PDF text extraction and embedding generation asynchronously. Deploy **Redis** to serve as both the Celery message broker and a high-speed caching layer for repetitive queries.

### 🤖 Phase 6: Agentic AI Workflows
* **Objective:** Evolve the AI from a simple chatbot into an autonomous reasoning mentor.
* **Details:** Utilize **LangGraph** to build multi-step self-correcting memory loops, empowering the model to analyze context, decide on external tool execution pathways (e.g., web search), and synthesize comprehensive mentoring plans.

### 🐳 Phase 7: Full Dockerization
* **Objective:** Encapsulate the architecture for absolute environment parity.
* **Details:** Write a multi-stage `Dockerfile` and `docker-compose.yml` to orchestrate the FastAPI service, PostgreSQL database, Redis cache, and Celery workers into a unified, isolated network.

### 🎨 Phase 8: Frontend UI (Streamlit)
* **Objective:** Construct a highly responsive chat dashboard.
* **Details:** Build a dynamic reactive chat interface in pure Python using **Streamlit**, avoiding frontend boilerplate while seamlessly communicating with the FastAPI backend via HTTP requests.

### 🚀 Phase 9: Production Deployment
* **Objective:** Launch the platform globally.
* **Details:** Configure immutable cloud environments (e.g., AWS, Render), provision secure secret vaults for `.env` variables, and deploy the fully containerized production stack.

---

## 💻 Getting Started (Local Setup)

Follow these instructions to run the project locally on your machine:

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/ai-mentor-agent.git](https://github.com/your-username/ai-mentor-agent.git)
```
**2. Navigate to the project directory:**
```
cd ai-mentor-agent
```

---

---
## ⚖️ License & Commercial Use

This project is open-sourced under the **GNU AGPLv3 License**. 

You are free to use, modify, and distribute this software, provided that any derivative works or network services running this code are also open-sourced under the same AGPLv3 license.

🏢 **Commercial Dual-Licensing:**
If your organization wishes to use **AI Mentor Agent** in a closed-source, proprietary, or commercial environment without the AGPLv3 obligations, a commercial license must be acquired. 
Please contact **Codweb Lab** for enterprise licensing and white-label deployments.

---