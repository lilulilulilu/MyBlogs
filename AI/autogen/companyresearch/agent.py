import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_core.models import ModelFamily
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(
        model="qwen3:8b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": ModelFamily.GPT_4,
            "structured_output": True,
        },
    )
    
async def main() -> None:
    agent = AssistantAgent("assistant", model_client=model_client)
    print(await agent.run(task="Say 'Hello World!'"))
    await model_client.close()

asyncio.run(main())
