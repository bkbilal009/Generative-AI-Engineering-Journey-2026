import os
import kagglehub
import gradio as gr
import pandas as pd
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.documents import Document
from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

# ==========================================
# SYSTEM SETUP
# ==========================================
# In HF Spaces, use os.getenv to get the secret
api_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key

# Load Dataset
print("📥 Initializing Legal Database...")
path = kagglehub.dataset_download("muhammadahmad246/labeled-legal-cases-for-supreme-court-of-pakistan")

all_docs = []
for root, _, files in os.walk(path):
    for f in files:
        if f.endswith('.txt') and len(all_docs) < 150:
            try:
                with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    if len(content.strip()) > 100:
                        all_docs.append(Document(page_content=content, metadata={"source": f}))
            except: continue

# Vector Store
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = text_splitter.split_documents(all_docs)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = Chroma.from_documents(chunks, embeddings)
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# AI Setup
llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.1)

context_p = ChatPromptTemplate.from_messages([
    ("system", "Formulate a standalone legal search query based on chat history."),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])
history_retriever = create_history_aware_retriever(llm, retriever, context_p)

qa_p = ChatPromptTemplate.from_messages([
    ("system", "You are the Pakistan Supreme Court AI. Context:\n\n{context}"),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])
qa_chain = create_stuff_documents_chain(llm, qa_p)
rag_chain = create_retrieval_chain(history_retriever, qa_chain)

# ==========================================
# PROFESSIONAL PINK THEME & UI
# ==========================================
# Custom theme: Soft Pink and Slate Gray
custom_theme = gr.themes.Soft(
    primary_hue="pink",
    secondary_hue="slate",
    neutral_hue="rose",
    font=[gr.themes.GoogleFont("Poppins"), "ui-sans-serif", "system-ui", "sans-serif"]
)

history_data = []

def chat_fn(message, history):
    global history_data
    try:
        response = rag_chain.invoke({"input": message, "chat_history": history_data})
        history_data.append(HumanMessage(content=message))
        history_data.append(AIMessage(content=response["answer"]))
        if len(history_data) > 6: history_data = history_data[-6:]
        return response["answer"]
    except Exception as e:
        if "429" in str(e): return "🕒 System busy. Please wait 60 seconds."
        return f"Error: {str(e)}"

# Build UI with Muhammad Bilal's branding
with gr.Blocks(theme=custom_theme) as demo:
    gr.Markdown(
        """
        # ⚖️ Pakistan Supreme Court Legal AI
        ### Developed by: **Muhammad Bilal** | Aspiring AI Developer
        ---
        *Advanced RAG-based analysis of judicial precedents and constitutional law.*
        """
    )
    
    chatbot = gr.ChatInterface(
        fn=chat_fn,
        examples=["What are the grounds for a Review Petition?", "Summarize Article 10-A.", "Who is Muhammad Bilal?"],
        cache_examples=False
    )
    
    gr.Markdown(
        """
        ---
        *Note: This AI is for research purposes. Always consult a legal professional for actual court matters.*
        """
    )

if __name__ == "__main__":
    demo.launch()