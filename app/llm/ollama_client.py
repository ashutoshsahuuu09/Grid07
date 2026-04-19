import requests
import json
from app.config import OLLAMA_MODEL, OLLAMA_URL

def call_ollama(prompt: str, temperature=0.7):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama error: {response.text}")

    return response.json().get("response", "")