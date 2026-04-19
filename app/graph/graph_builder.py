from langgraph.graph import StateGraph
from app.graph.state import GraphState
from app.graph.nodes import decide_topic, search, generate_post

def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("decide", decide_topic)
    graph.add_node("search", search)
    graph.add_node("generate", generate_post)

    graph.set_entry_point("decide")

    graph.add_edge("decide", "search")
    graph.add_edge("search", "generate")

    return graph.compile()