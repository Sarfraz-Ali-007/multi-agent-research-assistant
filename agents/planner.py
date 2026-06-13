from llm import llm

def planner_agent(state):

    prompt = f"""
    Create a research plan for:

    {state['query']}
    """

    response = llm.invoke(prompt)

    return {"plan": response.content}
