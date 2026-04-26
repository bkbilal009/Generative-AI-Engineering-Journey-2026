import os
import gdown
import gradio as gr
from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# --- CONFIGURATION ---
FILE_ID = "1jmHwcjA-gLIUTIKkXfQ36ucJI_VPdULS"
PDF_PATH = "finance_data.pdf"
GDRIVE_URL = f'https://drive.google.com/uc?id={FILE_ID}'

# Hugging Face Space will pull this from your "Secrets" settings
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# --- INITIALIZATION ---
def initialize_system():
    # Download PDF if not present
    if not os.path.exists(PDF_PATH):
        try:
            gdown.download(GDRIVE_URL, PDF_PATH, quiet=False)
        except Exception as e:
            print(f"Download Error: {e}")
    
    # Load and Split
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)
    
    # Embeddings using Sentence Transformers
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_documents(chunks, embeddings)

# Initialize the vector database once at startup
vector_db = initialize_system()

def process_query(user_query):
    if not GROQ_API_KEY:
        return "⚠️ Error: GROQ_API_KEY is missing. Add it to Space Secrets.", ""
    
    if not user_query.strip():
        return "Please enter a question.", ""

    try:
        # Search the PDF
        search_results = vector_db.similarity_search(user_query, k=3)
        context = "\n\n".join([res.page_content for res in search_results])
        
        # Groq API Call
        client = OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")
        
        # Construct the prompt
        prompt = f"Context: {context}\n\nQuestion: {user_query}\n\nAnswer using context only:"
        
        # Note: Using standard chat completion for maximum compatibility
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile", # Reliable high-speed Groq model
        )
        
        return chat_completion.choices[0].message.content, context
    except Exception as e:
        return f"System Error: {str(e)}", ""

# --- STYLISH PINK THEME ---
# Using Poppins font and Pink/Rose color palette
pink_theme = gr.themes.Soft(
    primary_hue="pink",
    secondary_hue="rose",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Poppins"), "sans-serif"],
).set(
    button_primary_background_fill="*primary_500",
    button_primary_background_fill_hover="*primary_600",
    button_primary_text_color="white",
)

# --- UI LAYOUT ---
with gr.Blocks(theme=pink_theme, title="Muhammad Bilal Finance RAG") as demo:
    gr.Markdown(
        """
        # <span style='color:#e91e63;'>📊 Muhammad Bilal Finance RAG App</span>
        ### AI-Powered Financial Document Analysis
        """
    )
    
    with gr.Row():
        with gr.Column(scale=2):
            query_input = gr.Textbox(
                label="Ask a Question", 
                placeholder="e.g., What are the total assets?",
                lines=2
            )
            analyze_btn = gr.Button("✨ Run Financial Analysis", variant="primary")
        
        with gr.Column(scale=3):
            answer_output = gr.Textbox(
                label="Muhammad Bilal AI Insights", 
                lines=10,
                interactive=False
            )
            
    with gr.Accordion("🔍 View Context Sources", open=False):
        context_output = gr.Markdown()

    analyze_btn.click(
        fn=process_query, 
        inputs=[query_input], 
        outputs=[answer_output, context_output]
    )

    gr.Markdown("<center>Built by Muhammad Bilal | Powered by Groq & FAISS</center>")

if __name__ == "__main__":
    demo.launch()