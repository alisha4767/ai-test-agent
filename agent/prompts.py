def build_prompt(description):
    return f"""
You are an AI Test Agent.

Convert the following test description into structured JSON test steps.

Rules:
- Output ONLY valid JSON
- No explanation
- Actions allowed: open, type, click
- Assertions must include: target, contains

Test Description:
{description}
"""