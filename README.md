# 🚀 Grid07 AI Engineering Assignment

## Cognitive Routing & RAG System

---

## 📌 Overview

This project implements a **modular AI cognitive system** that simulates intelligent social media bots.
It combines:

* **Vector-based routing** (deciding which bot should respond)
* **LangGraph orchestration** (content generation with tool usage)
* **RAG-based reasoning** (context-aware replies with safety guardrails)

---

## 🧠 Architecture

```text
Post → Embedding → Router → Selected Bot
        ↓
   LangGraph Flow
   (Decide → Search → Generate)
        ↓
   RAG Defense Engine (Thread Awareness + Injection Protection)
```

---

## ⚙️ Tech Stack

* Python
* LangChain / LangGraph
* FAISS (vector similarity)
* Sentence Transformers (embeddings)
* Ollama (Local LLM - llama3 / codellama)

---

## 🧩 Features

### 🔹 Phase 1: Cognitive Routing

* Uses **vector similarity (cosine)** to match posts with relevant bot personas
* Prevents unnecessary broadcasting to all bots

---

### 🔹 Phase 2: Autonomous Content Engine

* Built using **LangGraph state machine**
* Flow:

  1. Decide topic
  2. Fetch context (mock search tool)
  3. Generate opinionated post
* Output is **strict JSON**

---

### 🔹 Phase 3: Combat Engine (RAG + Defense)

* Uses full conversation context (parent + history)
* Maintains persona consistency
* Defends against **prompt injection attacks**

---

## 🔐 Prompt Injection Defense

The system includes:

* System-level guardrails (non-overridable instructions)
* Input sanitization for malicious phrases
* Persona enforcement to prevent role switching

---

## 📁 Project Structure

```text
app/
 ├── router/        # Phase 1 (embeddings + FAISS)
 ├── graph/         # Phase 2 (LangGraph nodes & tools)
 ├── rag/           # Phase 3 (RAG + defense)
 ├── llm/           # Ollama integration
 ├── main.py

logs/
 └── execution_logs.md

run.py
requirements.txt
.env.example
README.md
```

---

## 🚀 Setup Instructions

### 1. Clone repository

```bash
git clone <your-repo-url>
cd grid07
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup Ollama (Local LLM)

```bash
ollama pull llama3
```

---

### 4. Run the project

```bash
python -m run
```

---

## 📊 Sample Outputs

### Phase 1

```text
Matched Bots: ['bot_a']
```

---

### Phase 2

```json
{
  "bot_id": "bot_a",
  "topic": "AI advancements",
  "post_content": "AI replacing developers is inevitable..."
}
```

---

### Phase 3

```text
Bot ignores malicious instruction and continues argument logically.
```

---

## ⚠️ Notes

* `.env` file is not included (use `.env.example`)
* Large files (venv, models) are excluded for optimization
* Outputs may vary depending on LLM used (llama3 recommended)
* JSON parsing includes fallback for robustness

---

## 🧠 Key Learnings

* Semantic routing using embeddings
* LLM workflow orchestration (LangGraph)
* Tool-augmented generation (RAG-lite)
* Prompt injection defense strategies

---

## 🎯 Conclusion

This project demonstrates a **mini agentic AI system** capable of:

* Intelligent decision making
* Context-aware content generation
* Safe and robust conversational behavior

---

## 👤 Author

**Ashutosh Sahu**

---

## ⭐ Recommendation

For best performance:

```bash
OLLAMA_MODEL=llama3
```
