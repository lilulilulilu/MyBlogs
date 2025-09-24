#!/usr/bin/env python3
"""
专门测试多模态AI问题的回答质量
"""
import asyncio
from agent import chat_with_agent_async

async def test_multimodal_ai():
    """测试多模态AI问题的回答质量"""
    print("🤖 测试多模态AI问题回答质量...")
    
    question = "多模态AI在2025年的发展态势怎么样？"
    print(f"📝 问题: {question}")
    print("-" * 80)
    
    try:
        response = await chat_with_agent_async(question)
        print(f"🤖 Agent回答:\n{response}")
        print("-" * 80)
        
        # 分析回答质量
        print("\n📊 回答质量分析:")
        if "相关文档片段" in response:
            print("❌ 问题：直接返回了检索到的原始片段")
        if len(response.split('\n')) > 10:
            print("❌ 问题：回答过于冗长，包含太多原始信息")
        if "多模态" in response and "2025" in response:
            print("✅ 优点：回答包含了关键词")
        if response.count('。') >= 2:
            print("✅ 优点：回答包含完整的句子")
            
    except Exception as e:
        print(f"❌ 错误: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_multimodal_ai())
