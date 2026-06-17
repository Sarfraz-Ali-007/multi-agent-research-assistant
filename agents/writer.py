from llm import llm

def writer_agent(state):

    prompt = f"""
You are a Senior Research Report Writer.

Create a professional research report.

Use:

Research Plan:
{state['plan']}

Verified Findings:
{state['fact_check']}

Generate:

# Title

# Executive Summary

# Introduction

# Research Findings

# Analysis

# Opportunities

# Risks

# Future Outlook

# Conclusion

# References

Write in a professional consulting style.
"""

    response = llm.invoke(prompt)

    return {"report": response.content}
