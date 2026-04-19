import os

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")  # ✅ better default
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
SIMILARITY_THRESHOLD = 0.6
MAX_TOKENS = 300