import pinecone
from langchain.vectorstores import Pinecone
import os
from memory.base import MemoryProviderSingleton
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


class PineconeMemory(MemoryProviderSingleton):
    def __init__(self):
        pinecone.init(
            api_key=os.environ["PINECONE_API_KEY"],
            environment=os.environ["PINECONE_ENV"],
        )
        print("Pinecone has been initialized.")

    def from_texts(self, texts, embedding, index_name, metadatas):
        self.create_index(index_name)
        return Pinecone.from_texts(
            texts=texts, embedding=embedding, metadatas=metadatas, index_name=index_name
        )

    def get_relavent(self, query, index_name, num, embedding):
        docsearch = Pinecone.from_existing_index(
            index_name=index_name, embedding=embedding
        )
        return docsearch.similarity_search(query=query, k=num)

    @staticmethod
    def create_index(index_name):
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(index_name, dimension=768)
        else:
            print("This index already exists")
