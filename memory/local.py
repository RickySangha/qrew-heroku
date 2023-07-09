import pickle
import faiss
from langchain.vectorstores import FAISS


class LocalFaiss:
    # create embeddings and store them into a pickle file
    def from_docs(self, docs, embedding, index_name):
        vectorStore = FAISS.from_documents(docs, embedding)
        with open(f"local_vectorstore/{index_name}.pkl", "wb") as f:
            pickle.dump(vectorStore, f)

    def from_texts(self, texts, embedding, index_name, metadatas):
        vectorStore = FAISS.from_texts(texts, embedding, metadatas)
        with open(f"local_vectorstore/{index_name}.pkl", "wb") as f:
            pickle.dump(vectorStore, f)

    def get_relatent(self, query, index_name, num, embedding=None):
        VectorStore = self.load_index(index_name)
        retriever = VectorStore.as_retriever(search_kwargs={"k": num})
        return retriever.get_relevant_documents(query)

    @staticmethod
    def load_index(index_name):
        with open(f"local_vectorstore/{index_name}.pkl", "rb") as f:
            VectorStore = pickle.load(f)
        return VectorStore
