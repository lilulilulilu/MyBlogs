#!/usr/bin/env python3
"""
测试chat_agent的功能
"""
import asyncio
from agent import chat_with_agent_async

async def test_agent():
    """测试agent功能"""
    print("🤖 开始测试Chat Agent...")
    
    # 测试问题
    test_questions = [
        "你好",
        "多模态AI在2025年的发展态势怎么样？",
        "AI Agent有哪些类型？"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 测试问题 {i}: {question}")
        print("-" * 50)
        
        try:
            response = await chat_with_agent_async(question)
            print(f"🤖 Agent回答: {response}")
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
        
        print("-" * 50)

if __name__ == "__main__":
    asyncio.run(test_agent())
