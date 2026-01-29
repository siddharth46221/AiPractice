import os
os.environ["LANGCHAIN_SANDBOX_ENABLED"] = "false"
from my_agent import create_weather_agent
from langchain_core.messages import AIMessage

agent = create_weather_agent()

response = agent.invoke({
     'messages': [
      {"role": "user", "content": "what is the weather in Mumbai? and call the tool" }
    ]
     }
    )

for msg in response["messages"]:
    
    if isinstance(msg, AIMessage):
        print(msg.content)