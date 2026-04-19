from typing import TypedDict

class GraphState(TypedDict):
    bot_id: str
    persona: str
    query: str
    context: str
    post_content: dict