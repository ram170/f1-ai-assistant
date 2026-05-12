import chromadb

# Persistent DB storage
client = chromadb.PersistentClient(
    path="app/db/chroma_db"
)

collection = client.get_or_create_collection(
    name="f1_races"
)

def get_collection():
    return collection