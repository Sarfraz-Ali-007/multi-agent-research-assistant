from llm import llm

def summarizer_agent(state):

    prompt = f"""
    Summarize:

    {state['research']}
    """

    response = llm.invoke(prompt)

    return {"summary": response.content}
