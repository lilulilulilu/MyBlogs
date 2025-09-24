import re

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