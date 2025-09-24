from langchain_community.document_loaders import PyPDFLoader

import os

from langchain_core.documents import Document
current_dir = os.path.dirname(os.path.abspath(__file__))


def get_docs(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs


def split_docs(docs):
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits: list[Document] = text_splitter.split_documents(docs)

    return all_splits





if __name__ == "__main__":
    file_path = os.path.join(current_dir, "../files/google_cloud_ai_trends_zh-cn.pdf")
    docs = get_docs(file_path)
    for doc in docs:
        print(f"Page {doc.metadata['page']}: {doc.page_content}")

    all_splits = split_docs(docs)
    print(f"Split chunks: {len(all_splits)}")

    for split in all_splits:
        print(f"Split {split.metadata['page']}: {split.page_content}")
