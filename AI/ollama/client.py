import re
from ollama import Client


def extract_thinking_and_response(content):
    """
    从 content 中分离 thinking 文本和真正的 AI 回答
    
    Args:
        content: 包含 <think> 标签的完整内容
        
    Returns:
        tuple: (thinking_text, actual_response)
    """
    # 使用正则表达式匹配 <think>...</think> 标签
    think_pattern = r'<think>(.*?)</think>'
    
    # 提取 thinking 内容
    thinking_matches = re.findall(think_pattern, content, re.DOTALL)
    thinking_text = '\n'.join(thinking_matches).strip()
    
    # 移除 <think>...</think> 标签，得到真正的回答
    actual_response = re.sub(think_pattern, '', content, flags=re.DOTALL).strip()
    
    return thinking_text, actual_response


def chat():
    message = {'role': 'user', 'content': 'how are you?'}
    client = Client()

    # 使用 client.chat 方法,会自动启动ollama server运行指定的模型
    response = client.chat(model='deepseek-r1:7b', messages=[message]) 
    
    # Ollama 的响应结构不同，直接访问 message
    message = response['message']
    
    # 分离 thinking 和实际回答
    thinking_text, actual_response = extract_thinking_and_response(message['content'])
    
    print("=" * 50)
    print("原始内容:")
    print(f"'{message['content']}'")
    print("\n" + "=" * 50)
    print("思考过程:")
    print(f"'{thinking_text}'")
    print("\n" + "=" * 50)
    print("AI 回答:")
    print(f"'{actual_response}'")
    print("\n" + "=" * 50)
    print("完整响应信息:")
    print(response)


if __name__ == "__main__":
    chat()