from app.llm.ollama_client import call_ollama
from app.rag.prompt import build_prompt

def generate_defense_reply(bot_persona, parent_post, comment_history, human_reply):

    # Injection detection
    if "ignore" in human_reply.lower():
        human_reply = "[Detected malicious instruction]"

    prompt = build_prompt(
        bot_persona,
        parent_post,
        comment_history,
        human_reply
    )

    return call_ollama(prompt, temperature=0.6)