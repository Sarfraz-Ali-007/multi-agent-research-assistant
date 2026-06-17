from llm import llm

def fact_checker_agent(state):

    prompt = f"""
You are a Professional Fact Checker.

Review the research summary.

Tasks:

1. Identify unsupported claims.
2. Identify possible inaccuracies.
3. Assess confidence level.
4. Mark findings as:
   - Verified
   - Likely Correct
   - Needs Verification

Summary:
{state['summary']}

Return:

## Verified Findings

## Findings Requiring Verification

## Confidence Assessment

## Final Verdict
"""

    response = llm.invoke(prompt)

    return {"fact_check": response.content}
