import os
from dotenv import load_dotenv
import chromadb
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

load_dotenv()

CHROMA_PATH = "./chroma_db"
DATA_PATH = "./data"
COLLECTION_NAME = "profile_assistant"

def build_index():
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5", device="cpu", embed_batch_size=1)
    
    print("Loading documents...")
    documents = SimpleDirectoryReader(DATA_PATH).load_data()
    print(f"Loaded {len(documents)} chunks")

    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    chroma_collection = chroma_client.get_or_create_collection(COLLECTION_NAME)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    print("Building index...")
    VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    print("Done! Index saved to chroma_db/")

if __name__ == "__main__":
    build_index()