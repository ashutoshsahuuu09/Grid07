from langchain.tools import tool

@tool(description="Mock search tool for returning news headlines")
def mock_searxng_search(query: str):
    q = query.lower()

    if "crypto" in q:
        return "Bitcoin hits all-time high after ETF approvals"
    if "ai" in q:
        return "New AI model threatens developer jobs"
    if "market" in q:
        return "Markets fluctuate amid inflation concerns"

    return "Tech and finance sectors show mixed trends"