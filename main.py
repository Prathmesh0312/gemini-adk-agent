"""# main.py
import json
from dotenv import load_dotenv
import os
import asyncio

#  Patch JSON encoder to handle bytes safely 
class BytesSafeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (bytes, bytearray)):
            return obj.decode("utf-8", errors="ignore")
        return super().default(obj)

json._default_encoder = BytesSafeEncoder()

#  Imports after patch
from .prompt import MAIN_PROMPT
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from .tools import fetch_url_content


# Load environment variables (Gemini API Key)
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Create agent
root_agent = LlmAgent(
    name="myagent",
    description="A simple agent for testing",
    instruction=MAIN_PROMPT,   
    tools=[fetch_url_content],
    model="gemini-2.5-flash"
)

# Create session service
APP_NAME = "GenAIWebAgent"
USER_ID = "user1"
SESSION_ID = "session1"

session_service = InMemorySessionService()

# create session before using it
session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)

runner = Runner(agent=root_agent, session_service=session_service, app_name=APP_NAME)

async def run_agent(query: str):
    # Ensure query is a string
    content = types.Content(role="user", parts=[types.Part(text=str(query))])
    final_response = "No valid response returned."

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                text_parts = []
                for p in event.content.parts:
                    if hasattr(p, "text") and isinstance(p.text, (str, bytes)):
                        # Decode bytes or cast to str
                        text_parts.append(
                            p.text.decode("utf-8") if isinstance(p.text, bytes) else str(p.text)
                        )
                final_response = "\n".join(text_parts) if text_parts else "[No text response]"
            break

    return final_response


if __name__ == "__main__":
    query = "Explain https://courses.syracuse.edu/preview_program.php?catoid=41&poid=20986&returnto=5120&redirect in 4 bullet points"
    result = asyncio.run(run_agent(query))
    print("\n=== Agent Response ===\n")
    print(result)
"""