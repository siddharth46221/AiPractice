from langchain.agents import initialize_agent
from prompts import SYSTEM_PROMPT
from tools import get_weather_for_location, get_current_location
from model import get_model

def create_weather_agent():
    
    model = get_model()
    tools = [get_weather_for_location, get_current_location]

    agent = initialize_agent(
    model,
    tools,
    system_prompt=SYSTEM_PROMPT
    )
    return agent 