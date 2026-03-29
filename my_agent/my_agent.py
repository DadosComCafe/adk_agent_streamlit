import vertexai
from decouple import config
from google.adk.agents import Agent
from my_agent.descriptions.agent_description import description
from my_agent.instructions.agent_instruction import instruction

vertexai.init(
    project=config("GOOGLE_CLOUD_PROJECT"),
    location=config("GOOGLE_CLOUD_LOCATION", default="us-central1"),
)

agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    description=description,
    instruction=instruction
)