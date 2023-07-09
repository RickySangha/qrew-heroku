from memory.local import LocalFaiss
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

try:
    from memory.pinecone import PineconeMemory
except ImportError:
    print("Pinecone not installed. Skipping import.")
    PineconeMemory = None


def get_memory():
    memory = None
    if os.environ["MEMORY"] == "pinecone":
        if not PineconeMemory:
            print(
                "Error: Pinecone is not installed. Please install pinecone"
                " to use Pinecone as a memory backend."
            )
        else:
            memory = PineconeMemory()
    if memory is None:
        memory = LocalFaiss()

    return memory
