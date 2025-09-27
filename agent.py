
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# Load environment variables from .env file
load_dotenv()

def get_model():
    """
    Configures and returns the LLM model based on environment variables.

    Returns:
        An instance of OpenAIModel configured with the specified provider.
    """
    llm_choice = os.getenv("LLM_CHOICE", "gpt-4o-mini")
    llm_base_url = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
    llm_api_key = os.getenv("LLM_API_KEY", "ollama") # Default to ollama for local-first setup

    provider = OpenAIProvider(api_key=llm_api_key, base_url=llm_base_url)
    return OpenAIModel(llm_choice, provider=provider)

# Create a new agent
# For Iteration 1, we are not using any tools, just the core conversational ability.
agent = Agent(
    get_model(),
    system_prompt="You are a helpful assistant.",
)

async def get_agent_response(user_input: str) -> str:
    """
    Runs the agent with the given user input and returns the response.

    Args:
        user_input: The query or message from the user.

    Returns:
        The agent's text response.
    """
    result = await agent.run(user_input)
    return result.output
