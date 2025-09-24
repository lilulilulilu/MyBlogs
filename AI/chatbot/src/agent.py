import asyncio
from typing import List, Tuple
from store import MilvusStore
from autogen_agentchat.agents import AssistantAgent
from autogen_core.models import ModelFamily
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.tools import FunctionTool
from dotenv import load_dotenv

load_dotenv()

# 初始化组件
milvus_store = MilvusStore()

# 配置模型客户端
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

# 知识库检索工具
def search_knowledge_base(query: str) -> str:
    """从知识库中检索相关信息"""
    try:
        retrieved_docs = milvus_store.retrieve_from_milvus(query)
        if not retrieved_docs:
            return "知识库中没有找到相关信息。"
        
        # 构建更结构化的上下文
        context_parts = []
        for i, (doc, score) in enumerate(retrieved_docs, 1):
            # 清理文本，移除多余空格
            clean_content = " ".join(doc.page_content.split())
            context_parts.append(f"相关文档片段 {i} (相关度: {score:.3f}):\n{clean_content}")
        
        return "\n\n".join(context_parts)
    except Exception as e:
        return f"知识库检索出错: {str(e)}"

# 创建工具
knowledge_search_tool = FunctionTool(
    search_knowledge_base, 
    description="搜索AI相关信息"
)

# 创建agent
chat_agent = AssistantAgent(
    name="Chat_Assistant",
    model_client=model_client,
    tools=[knowledge_search_tool],
    description="智能聊天助手，可以搜索知识库并回答问题"
)

async def chat_with_agent_async(message: str) -> str:
    """异步处理聊天消息"""
    try:
        response = await chat_agent.run(task=message)
        # 从响应中提取文本内容
        if hasattr(response, 'messages') and response.messages:
            # 获取最后一条消息的内容
            last_message = response.messages[-1]
            if hasattr(last_message, 'content'):
                return last_message.content
            else:
                return str(last_message)
        elif hasattr(response, 'content'):
            return response.content
        else:
            return str(response)
    except Exception as e:
        return f"处理消息时出错: {str(e)}"

def chat_with_agent(message: str, history: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[str, str]]]:
    """处理聊天消息，集成知识库检索和agent响应"""
    if not message.strip():
        return "", history
    
    try:
        # 使用asyncio运行异步函数
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        ai_message = loop.run_until_complete(chat_with_agent_async(message))
        loop.close()
        
        # 更新历史记录
        history.append((message, ai_message))
        
        return "", history
        
    except Exception as e:
        error_msg = f"处理消息时出错: {str(e)}"
        history.append((message, error_msg))
        return "", history
