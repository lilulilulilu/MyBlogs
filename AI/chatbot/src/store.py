import os
from langchain_milvus import Milvus
from langchain_ollama import OllamaEmbeddings

from load_data import get_docs, split_docs

embeddings = OllamaEmbeddings(model="embeddinggemma:latest")

from dotenv import load_dotenv
load_dotenv()


class MilvusStore:
    def __init__(self, uri: str = "milvus_example.db"):
        self.uri = uri
        self.vector_store = Milvus(
            embedding_function=embeddings,
            connection_args={"uri": uri},
            index_params={"index_type": "FLAT", "metric_type": "L2"},
        )
    
    def similarity_search(self, query, k=5):
        return self.vector_store.similarity_search(query, k)
    
    def similarity_search_with_score(self, query, k=5):
        return self.vector_store.similarity_search_with_score(query, k)
    
    def delete_documents(self, ids):
        self.vector_store.delete_documents(ids)
    
    def clean_up(self):
        if os.path.exists(self.uri):
            os.remove(self.uri)
            print(f"Deleted {self.uri}")

    def save_to_milvus(self, file_path):
        docs = get_docs(file_path)
        all_splits = split_docs(docs)
        ids = self.vector_store.add_documents(documents=all_splits)
        print(f"Added {len(ids)} documents to Milvus")

    def retrieve_from_milvus(self, query):
        retrieved_docs = self.vector_store.similarity_search_with_score(
            query,
            k=5
        )
        return retrieved_docs



if __name__ == "__main__":
    # 0. init milvus store
    milvus_store = MilvusStore()

    # 1. clean up
    milvus_store.clean_up()

    # 2. add a file to milvus
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../files/google_cloud_ai_trends_zh-cn.pdf")
    milvus_store.save_to_milvus(file_path)

    # 3. retrieve from milvus
    query = "多模态 AI 在 2025 年的发展态势怎么样？"
    retrieved_docs = milvus_store.retrieve_from_milvus(query)
    print(f"retrieved_docs: {retrieved_docs}\n\n")
    print("-" * 100)
    for doc, score in retrieved_docs:
        print(f"score: {score}")
        print(f"doc: {doc}")
        print("-" * 100)


