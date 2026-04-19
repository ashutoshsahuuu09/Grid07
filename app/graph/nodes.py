import json
from app.graph.tools import mock_searxng_search
from app.llm.ollama_client import call_ollama

def decide_topic(state):
    prompt = f"""
You are a bot.

Persona:
{state['persona']}

Decide a short topic to post about.
Return ONLY a search query.
"""

    query = call_ollama(prompt).strip()
    return {"query": query}


def search(state):
    context = mock_searxng_search.invoke(state["query"])
    return {"context": context}


def generate_post(state):
    prompt = f"""
You are a social media bot.

Persona:
{state['persona']}

Context:
{state['context']}

Rules:
- Max 280 characters
- Strong opinion
- Stay in persona

Return STRICT JSON:
{{
  "bot_id": "{state['bot_id']}",
  "topic": "{state['query']}",
  "post_content": "..."
}}
"""

    raw = call_ollama(prompt)

    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        parsed = json.loads(raw[start:end])
    except:
        parsed = {
            "bot_id": state["bot_id"],
            "topic": state["query"],
            "post_content": raw[:280]
        }

    return {"post_content": parsed}