import os
from dotenv import load_dotenv, find_dotenv
from google.adk.agents import LlmAgent
from .prompt import MAIN_PROMPT
from .tools import fetch_url_content

# Load environment variables
load_dotenv(find_dotenv())
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Define the root agent (must be named root_agent for ADK Web)
root_agent = LlmAgent(
    name="myagent",
    description="A simple agent for testing with ADK Web",
    instruction=MAIN_PROMPT,
    tools=[fetch_url_content],
    model="gemini-2.5-flash"
)
