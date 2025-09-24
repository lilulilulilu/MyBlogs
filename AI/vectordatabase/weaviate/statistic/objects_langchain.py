
import weaviate
import json
from langchain_community.vectorstores import Weaviate
from langchain.docstore.document import Document
from langchain_dashscope import DashScopeEmbeddings


    
client = weaviate.Client("http://localhost:8080")

embeddings = DashScopeEmbeddings(model="text-embedding-v2")

def query_with_langchain(client, embeddings):
    """使用 LangChain 查询所有数据"""
    print("\n3. 使用 LangChain 查询所有数据：")
    
    try:
        # 获取所有类
        schema = client.schema.get()
        classes = schema.get("classes", [])
        
        for class_info in classes:
            class_name = class_info["class"]
            print(f"\n   使用 LangChain 查询类: {class_name}")
            
            try:
                # 创建 LangChain Weaviate 实例
                vectorstore = Weaviate(
                    client=client,
                    index_name=class_name,
                    text_key="content",  # 假设文本字段名为 content
                    embedding=embeddings,
                    by_text=False
                )
                
                # 查询所有文档（使用一个很通用的查询）
                docs = vectorstore.similarity_search("", k=100)  # 空查询获取所有
                
                print(f"   ✅ 通过 LangChain 找到 {len(docs)} 个文档")
                
                # 显示前几个文档
                for i, doc in enumerate(docs[:3], 1):
                    print(f"   \n   文档 {i}:")
                    print(f"     内容: {doc.page_content[:100]}...")
                    print(f"     元数据: {doc.metadata}")
                
                if len(docs) > 3:
                    print(f"   ... 还有 {len(docs) - 3} 个文档")
                    
            except Exception as e:
                print(f"   ❌ LangChain 查询类 {class_name} 失败: {e}")
                
    except Exception as e:
        print(f"   ❌ LangChain 查询失败: {e}")


if __name__ == "__main__":
    query_with_langchain(client, embeddings)