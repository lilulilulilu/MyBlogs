#!/usr/bin/env python3
"""
测试Agent的自主决策能力
"""
import asyncio
from agent import chat_with_agent_async

async def test_agent_behavior():
    """测试Agent的自主决策能力"""
    print("🤖 测试Agent自主决策能力...")
    
    # 测试不同类型的问题
    test_questions = [
        "你好",  # 简单问候，不需要搜索知识库
        "今天天气怎么样？",  # 一般性问题，不需要搜索知识库
        "多模态AI在2025年的发展态势怎么样？",  # 需要搜索知识库的问题
        "什么是机器学习？",  # 一般性技术问题，可能不需要搜索知识库
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 测试问题 {i}: {question}")
        print("-" * 60)
        
        try:
            response = await chat_with_agent_async(question)
            print(f"🤖 Agent回答: {response}")
            
            # 分析Agent是否合理使用了工具
            if "相关文档片段" in response or "知识库" in response:
                print("✅ Agent使用了知识库搜索")
            else:
                print("✅ Agent直接回答了问题（未使用知识库）")
                
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
        
        print("-" * 60)

if __name__ == "__main__":
    asyncio.run(test_agent_behavior())
