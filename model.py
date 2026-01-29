from langchain_aws.chat_models import ChatBedrock
from dotenv import load_dotenv
import os

load_dotenv()

def get_model():
    
    return ChatBedrock(
    model_id="arn:aws:bedrock:ap-south-1:059356703210:application-inference-profile/23ug5hdxvz8i",
    provider="anthropic",
    region_name=os.getenv("AWS_DEFAULT_REGION")
)