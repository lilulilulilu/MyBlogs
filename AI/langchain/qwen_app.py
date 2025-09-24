import os
import warnings
from langchain_community.llms import Tongyi

# 抑制所有LangChain相关的弃用警告
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain_dashscope")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain_core")

from langchain_dashscope import DashScopeEmbeddings
embeddings = DashScopeEmbeddings(model="text-embedding-v2")

# os.environ["DASHSCOPE_API_KEY"] = "sk-2a13d33333333333333333" # see ~/.zshrc


embedding = embeddings.embed_query("Hello, world!")
length = len(embedding)
print(f'length:{length}')
# print(f'embedding:{embedding}')


response = Tongyi().invoke("who are you?")
print(f'response:{response}')