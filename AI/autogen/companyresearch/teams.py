import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from tools import google_search_tool, stock_analysis_tool

from autogen_agentchat.messages import BaseChatMessage
from autogen_agentchat.base import Response
from autogen_core import CancellationToken


from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core.tools import FunctionTool

from dotenv import load_dotenv
load_dotenv()

from tools import google_search_tool, stock_analysis_tool
from autogen_core.models import ModelFamily

model_client = OpenAIChatCompletionClient(
        model="qwen2.5:7b",
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

search_agent = AssistantAgent(
    name="Google_Search_Agent",
    model_client=model_client,
    tools=[google_search_tool],
    description="Search Google for information, returns top 2 results with a snippet and body content",
    system_message="You are a helpful AI assistant. Solve tasks using your tools.",
)

stock_analysis_agent = AssistantAgent(
    name="Stock_Analysis_Agent",
    model_client=model_client,
    tools=[stock_analysis_tool],
    description="Analyze stock data and generate a plot",
    system_message="Perform data analysis.",
)

report_agent = AssistantAgent(
    name="Report_Agent",
    model_client=model_client,
    description="Generate a report based the search and results of stock analysis",
    system_message="You are a helpful assistant that can generate a comprehensive report on a given topic based on search and stock analysis. When you done with generating the report, reply with TERMINATE.",
)

async def main():
    team = RoundRobinGroupChat([stock_analysis_agent, search_agent, report_agent], max_turns=3)
    stream = team.run_stream(task="Write a financial report on American airlines")
    await Console(stream)

    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())