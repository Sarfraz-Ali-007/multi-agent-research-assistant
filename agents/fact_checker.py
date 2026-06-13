from llm import llm

def fact_checker_agent(state):

    prompt = f"""
    Verify these findings:

    {state['summary']}
    """

    response = llm.invoke(prompt)

    return {"fact_check": response.content}
