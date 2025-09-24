import getpass
import os
from langchain_milvus import Milvus

from langchain_dashscope import DashScopeEmbeddings

embeddings = DashScopeEmbeddings(model="text-embedding-v2")


URI = "./milvus_example.db"

vector_store = Milvus(
    embedding_function=embeddings,
    connection_args={"uri": URI},
    index_params={"index_type": "FLAT", "metric_type": "COSINE"},  # 使用余弦相似度
)