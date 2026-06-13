from tavily import TavilyClient
import os

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def researcher_agent(state):

    result = client.search(
        query=state["query"],
        max_results=5
    )

    text = ""

    for r in result["results"]:
        text += r["content"] + "\n"

    return {"research": text}
