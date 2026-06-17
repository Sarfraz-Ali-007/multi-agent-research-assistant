from llm import llm
from tavily import TavilyClient
import os

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def researcher_agent(state):

    search_results = client.search(
        query=state["query"],
        max_results=10,
        search_depth="advanced"
    )

    context = ""

    for r in search_results["results"]:
        context += f"""
Title: {r.get('title')}

URL: {r.get('url')}

Content:
{r.get('content')}

----------------------------------
"""

    prompt = f"""
You are a Senior Research Analyst.

Research Topic:
{state['query']}

Research Plan:
{state.get('plan', '')}

Analyze the web results and provide:

## Key Findings
## Important Statistics
## Industry Trends
## Expert Opinions
## Opportunities
## Risks
## Source References

Web Results:

{context}
"""

    response = llm.invoke(prompt)

    return {"research": response.content}
