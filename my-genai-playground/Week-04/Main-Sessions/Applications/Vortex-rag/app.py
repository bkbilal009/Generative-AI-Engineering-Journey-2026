import os
import requests
import warnings
import gradio as gr
from groq import Groq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Silent mode for technical logs
warnings.filterwarnings("ignore")

# --- 1. CONFIGURATION & SECRETS ---
GROQ_API_KEY = os.environ.get("MY_GROQ_SECRET")
# Initialize client safely
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)
else:
    client = None

# HIDDEN DATA SOURCE
GDRIVE_LINKS = [
    "https://drive.google.com/file/d/10D3uJqBYG9gMWsNHcpTW4I6BKmA2otfH/view?usp=sharing"
]

# --- 2. KNOWLEDGE BASE INITIALIZATION ---
def download_gdrive_pdf(url, output_path):
    try:
        file_id = url.split('/')[-2]
        download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
        response = requests.get(download_url)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            return True
    except:
        return False
    return False

print("Starting document indexing...")
all_chunks = []
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)

for i, link in enumerate(GDRIVE_LINKS):
    filename = f"temp_doc_{i}.pdf"
    if download_gdrive_pdf(link, filename):
        try:
            loader = PyPDFLoader(filename)
            all_chunks.extend(text_splitter.split_documents(loader.load()))
        finally:
            if os.path.exists(filename):
                os.remove(filename)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = FAISS.from_documents(all_chunks, embeddings)
print("Index complete.")

# --- 3. RAG LOGIC ---
def respond(message, history):
    if not client:
        return "Error: MY_GROQ_SECRET not found in Space settings."
    
    # Retrieve relevant data
    docs = vector_db.similarity_search(message, k=5)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    system_prompt = f"""
    You are Bilal's Research Assistant. 
    1. Answer ONLY using the context provided below.
    2. If the answer is NOT in the context, say: "Answer not found in provided documents."
    3. Keep responses concise and factual.
    
    CONTEXT:
    {context}
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.1,
    )
    return chat_completion.choices[0].message.content

# --- 4. UI DESIGN ---
custom_css = """
body { background-color: #0f172a; }
.gradio-container { max-width: 800px !important; margin: auto; padding-top: 20px; }
#title { text-align: center; color: #38bdf8; font-weight: 800; font-size: 2em; }
#subtitle { text-align: center; color: #94a3b8; margin-bottom: 20px; }
footer { display: none !important; }
"""

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue"), css=custom_css) as demo:
    gr.HTML("<h1 id='title'>🌀 DocuVortex</h1>")
    gr.HTML("<p id='subtitle'>Bilal's Research AI: Strict Knowledge Retrieval</p>")
    
    # Simple Interface to avoid version-specific keyword crashes
    gr.ChatInterface(
        fn=respond,
        chatbot=gr.Chatbot(height=500),
        textbox=gr.Textbox(placeholder="Ask Bilal's AI a question...", container=False, scale=7),
    )

if __name__ == "__main__":
    demo.launch()