from langchain.agents import create_react_agent, AgentExecutor
from prompts import SYSTEM_PROMPT
from tools import get_weather_for_location, get_current_location
from model import get_model

def create_weather_agent():
    llm = get_model()
    tools = [get_current_location, get_weather_for_location]

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=SYSTEM_PROMPT
    )

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )