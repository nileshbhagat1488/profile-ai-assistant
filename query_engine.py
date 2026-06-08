import os
from dotenv import load_dotenv
import chromadb
from llama_index.core import VectorStoreIndex, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

load_dotenv()

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "profile_assistant"

def get_query_engine():
    Settings.embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")
    Settings.llm = Groq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )

    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    chroma_collection = chroma_client.get_or_create_collection(COLLECTION_NAME)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    index = VectorStoreIndex.from_vector_store(vector_store)
    return index.as_query_engine(similarity_top_k=5)

def ask(question: str) -> str:
    engine = get_query_engine()
    response = engine.query(question)
    return str(response)