from llm import llm

def summarizer_agent(state):

    prompt = f"""
You are an Executive Research Summarizer.

Summarize the following research findings.

Requirements:
- Keep important information.
- Remove duplication.
- Highlight major insights.
- Preserve statistics and evidence.

Research:
{state['research']}

Return:

## Executive Summary

## Major Insights

## Supporting Evidence

## Key Takeaways
"""

    response = llm.invoke(prompt)

    return {"summary": response.content}
