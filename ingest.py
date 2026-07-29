import chromadb
from sentence_transformers import SentenceTransformer

# Step A: Load the embedding model (runs locally, converts text -> vectors)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Step B: Set up ChromaDB (it will create a folder called chroma_db to store data permanently)
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="faq_collection")

# Step C: Read the FAQ file
with open("data/faq.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Step D: Chunk the content (split by double newline, since each Q&A pair is separated that way)
chunks = [chunk.strip() for chunk in content.split("\n\n") if chunk.strip()]

print(f"Total chunks created: {len(chunks)}")

# Step E: Convert each chunk into an embedding, and store it in ChromaDB
for i, chunk in enumerate(chunks):
    embedding = embedding_model.encode(chunk).tolist()
    collection.add(
        ids=[f"chunk_{i}"],
        embeddings=[embedding],
        documents=[chunk]
    )

print("Ingestion complete! All chunks stored in ChromaDB.")