from llm import llm

def writer_agent(state):

    prompt = f"""
    Create professional report.

    Research:
    {state['fact_check']}
    """

    response = llm.invoke(prompt)

    return {"report": response.content}
