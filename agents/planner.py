from llm import llm

def planner_agent(state):

    prompt = f"""
You are an expert Research Planner.

User Query:
{state['query']}

Your task:

1. Understand the research objective.
2. Break it into subtopics.
3. Identify key questions to investigate.
4. Suggest what evidence should be collected.
5. Create a step-by-step research plan.

Return your response in markdown.

Format:

## Research Goal

## Key Questions

## Subtopics

## Research Strategy

## Expected Deliverables
"""

    response = llm.invoke(prompt)

    return {"plan": response.content}
