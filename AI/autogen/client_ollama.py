import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelFamily
# from autogen_agentchat.messages import UserMessage
from autogen_core.models import (
    SystemMessage,
    UserMessage,
    AssistantMessage
)

def get_ollama_client():
    ollama_model_client = OpenAIChatCompletionClient(
        model="deepseek-r1:7b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": False,
            "json_output": False,
            "family": ModelFamily.R1,
            "structured_output": True,
        },
    )
    return ollama_model_client


async def main():
    ollama_model_client = get_ollama_client()

    result = await ollama_model_client.create([UserMessage(content="What is the capital of France?", source="user")])  # type: ignore
    print(result)

if __name__ == "__main__":
    asyncio.run(main())