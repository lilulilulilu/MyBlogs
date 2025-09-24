# https://docs.weaviate.io/weaviate/client-libraries/python#instantiate-a-client

from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings


from langchain_text_splitters import CharacterTextSplitter

import weaviate
from langchain_community.vectorstores import Weaviate
from langchain_weaviate.vectorstores import WeaviateVectorStore

from langchain.docstore.document import Document
from langchain_dashscope import DashScopeEmbeddings


# 1. 初始化 weaviate 客户端 (本地 8080)
# 使用 Weaviate v3 客户端（兼容性更好）
client = weaviate.Client("http://localhost:8080")

# 2. 准备 embeddings (使用简单的假 embeddings 用于测试)
embeddings = DashScopeEmbeddings(model="text-embedding-v2")

# 3. 初始化向量存储
vectorstore = Weaviate(
    client=client,
    index_name="LangChainDemo",  
    text_key="content",
    embedding=embeddings,
    by_text=False
)

# 4. 插入文档
docs = [
    Document(page_content="Weaviate is a vector database."),
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="Bosch is a company with a long history.")
]
vectorstore.add_documents(docs)

# 5. 生成查询的向量并进行向量搜索
query = "What is Weaviate?"
query_vector = embeddings.embed_query(query)

results = vectorstore.similarity_search_by_vector(query_vector, k=2)
print("向量搜索结果：")
for r in results:
    print(f"- 内容: {r.page_content}")
    print(f"  元数据: {r.metadata}")
    print()

results = vectorstore.similarity_search_with_score(query, k=2)
print("向量搜索结果（带分数）：")
for r, score in results:
    print(f"- 内容: {r.page_content}")
    print(f"  相似性分数: {score}")
    print()


# 4.2.load data from file and split into chunks
loader = TextLoader("state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)
print(f"Split document into {len(chunks)} chunks")
print(f'chunks[0]:{chunks[0]}')

# 2.embeddings and store in weaviate
print("Creating embeddings and storing in Weaviate...")
vectorstore.add_documents(chunks)
print("Successfully stored documents in Weaviate!")

retriever = vectorstore.as_retriever(search_type="mmr")
retrieved_docs = retriever.invoke("what did the president say about ketanji brown jackson?")
print(f'retrieved_docs[0]:{retrieved_docs[0]}')


# 3.2.perform a pure keyword search by adding alpha=0
print("\n=========alpha=0=========\n")
docs = vectorstore.similarity_search(query, alpha=0)
print(f'len(docs):{len(docs)}')
print(f'docs[0]:{docs[0]}')


# 4.perform a pure keyword search by adding tenant
print("\n=========index_name=========\n")
# 使用类方法创建新的向量存储实例
db_with_mt = Weaviate.from_documents(
    documents=chunks,
    embedding=embeddings,
    client=client,
    index_name="LangChainDemoWithTenant", # 指定索引名称，也即是weaviate中的class名称
    text_key="content", # 指定文本字段名称，表示使用哪个字段进行搜索
    by_text=False, # 是否将文本内容转换为向量再去搜索
)
query = "What is Weaviate?"
docs_with_mt = db_with_mt.similarity_search_with_score(query)

print(f'docs_with_mt[0]:{docs_with_mt[0]}')

