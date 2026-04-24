import os
import gradio as gr
import warnings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA

# Suppress logs
warnings.filterwarnings("ignore")

# --- CONFIGURATION ---
GROQ_API_KEY = os.environ.get("MY_GROQ_KEY")
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
rag_chain = None

def build_rag_system(file):
    global rag_chain
    if file is None: return "❌ Error: No document uploaded."
    if not GROQ_API_KEY: return "❌ Error: Groq API Key missing in Secrets!"

    try:
        loader = PyPDFLoader(file.name) if file.name.endswith(".pdf") else TextLoader(file.name)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=80)
        texts = text_splitter.split_documents(documents)
        vector_db = FAISS.from_documents(texts, embeddings)
        retriever = vector_db.as_retriever(search_kwargs={"k": 3})
        
        llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="llama-3.3-70b-versatile", temperature=0)
        
        template = """Answer ONLY using the context. If not found, say: 
        "I don't have enough information about this in the provided documents."
        
        Context: {context}
        Question: {question}
        Answer:"""
        
        QA_PROMPT = PromptTemplate.from_template(template)
        rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type_kwargs={"prompt": QA_PROMPT})
        return "✅ Vault Verified & Locked!"
    except Exception as e:
        return f"❌ System Error: {str(e)}"

def predict(message, history):
    if rag_chain is None: return "Please upload a document first."
    try:
        res = rag_chain.invoke({"query": message})
        return res["result"]
    except Exception as e:
        return f"🚨 API ERROR: {str(e)}"

# --- PROFESSIONAL UI DESIGN ---
with gr.Blocks(theme=gr.themes.Soft(primary_hue="slate", radius_size="lg"), title="VerityVault AI") as demo:
    gr.Markdown(
        """
        # 🛡️ VerityVault AI
        ### Developed by: **Bilal**
        *Grounded document intelligence with zero hallucinations.*
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="📄 Deposit Document (PDF/TXT)")
            build_btn = gr.Button("🔒 INITIALIZE VAULT", variant="primary")
            status = gr.Textbox(label="Vault Status", interactive=False)
            
        with gr.Column(scale=2):
            gr.ChatInterface(
                fn=predict,
                description="The vault only answers using your verified data."
            )

    # CRITICAL: This must be indented inside the 'with gr.Blocks' block!
    build_btn.click(
        fn=build_rag_system, 
        inputs=[file_input], 
        outputs=[status]
    )

if __name__ == "__main__":
    demo.launch()