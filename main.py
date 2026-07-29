from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
import os
import chromadb
from sentence_transformers import SentenceTransformer

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
app = FastAPI()







########################### THESE ARE FOR THE FRONTEND .... TO MAKE THIS APP LOOK GREATE (YOU CNIGNORE THEM OR LEARN THEM IF YOU ARE INTERESRED IN THE FRONTEND, I PREFER YOU CAN LEARN) ###################



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


#############################################################################################################################################################################################################




# Load the SAME embedding model used during ingestion (critical - must match)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to the SAME ChromaDB folder created during ingestion
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="faq_collection")

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Step 1: Convert user's question into an embedding
    query_embedding = embedding_model.encode(request.question).tolist()

    # Step 2: Search ChromaDB for the most similar chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    retrieved_chunks = results["documents"][0]
    context = "\n\n".join(retrieved_chunks)

    # Step 3: Build a prompt using retrieved context + user question
    system_prompt = f"""You are a helpful customer support assistant. 
Answer the user's question using ONLY the following context. 
If the answer is not in the context, say "I don't have that information, please contact support."

Context:
{context}
"""

    # Step 4: Send to LLM
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": request.question}
        ]
    )

    return ChatResponse(answer=response.choices[0].message.content)