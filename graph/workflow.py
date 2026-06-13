from langgraph.graph import StateGraph
from graph.state import ResearchState

from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.summarizer import summarizer_agent
from agents.fact_checker import fact_checker_agent
from agents.writer import writer_agent

builder = StateGraph(ResearchState)

builder.add_node("planner", planner_agent)
builder.add_node("researcher", researcher_agent)
builder.add_node("summarizer", summarizer_agent)
builder.add_node("fact_checker", fact_checker_agent)
builder.add_node("writer", writer_agent)

builder.set_entry_point("planner")

builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "summarizer")
builder.add_edge("summarizer", "fact_checker")
builder.add_edge("fact_checker", "writer")

graph = builder.compile()
