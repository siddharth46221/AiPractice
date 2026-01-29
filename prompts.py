from langchain.prompts import PromptTemplate

SYSTEM_PROMPT = PromptTemplate.from_template(
    """
You are a helpful weather assistant.

You can use the following tools:
{tools}

Use this format:

Question: the input question
Thought: you should think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (repeat Thought/Action/Observation as needed)
Thought: I now know the final answer
Final Answer: the final answer to the user

Question: {input}
{agent_scratchpad}
"""
)
