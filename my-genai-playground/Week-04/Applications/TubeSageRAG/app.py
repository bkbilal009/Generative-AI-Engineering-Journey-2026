import os
import re
import gradio as gr
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- CONFIG ---
GROQ_KEY = os.environ.get("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# --- GLOBAL STATE ---
vector_db = None
rag_chain = None

def extract_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None

def process_video(video_url):
    global vector_db, rag_chain
    vid = extract_video_id(video_url)
    
    if not vid: 
        return "❌ Invalid YouTube URL", ""

    try:
        # YouTube Transcript with Cookie Bypass
        try:
            cookie_file = "cookies.txt"
            if os.path.exists(cookie_file):
                # Using cookies to bypass the Connection Pool / Bot block
                transcript_list = YouTubeTranscriptApi.list_transcripts(vid, cookies=cookie_file)
            else:
                transcript_list = YouTubeTranscriptApi.list_transcripts(vid)
            
            try:
                transcript = transcript_list.find_transcript(['en'])
            except:
                transcript = transcript_list.find_generated_transcript(['en'])
            
            data = transcript.fetch()
        except Exception as yt_err:
            return f"❌ Connection Error. Please upload 'cookies.txt'. Details: {str(yt_err)[:50]}", ""

        full_text = " ".join([t['text'] for t in data])
        
        # RAG Pipeline Logic (Muhammad Bilal's Signature Style)
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        chunks = splitter.split_text(full_text)
        
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        vector_db = FAISS.from_texts(chunks, embeddings)
        retriever = vector_db.as_retriever(search_kwargs={"k": 3})

        llm = ChatGroq(groq_api_key=GROQ_KEY, model_name=MODEL_NAME, temperature=0.1)
        
        template = """You are TubeSage, an AI assistant. Use the video transcript context to answer the question.
        Context: {context}
        Question: {question}
        Answer:"""
        prompt = ChatPromptTemplate.from_template(template)

        # Modern LCEL Chain
        rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        
        return "✅ TubeSage is Ready!", full_text[:400] + "..."
    
    except Exception as e:
        return f"❌ System Error: {str(e)[:50]}", ""

def chat(msg, history):
    if not rag_chain: 
        return "Please analyze a video first!"
    try:
        return rag_chain.invoke(msg)
    except Exception as e:
        return f"Error: {str(e)}"

# --- UI DESIGN ---
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;600&display=swap');
body, .gradio-container { font-family: 'Outfit', sans-serif !important; background-color: #0f172a !important; }
.main-btn { background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important; color: white !important; border: none !important; cursor: pointer; }
"""

with gr.Blocks(title="TubeSage AI") as demo:
    gr.Markdown("# 📺 TubeSage: Video Intelligence Engine")
    gr.Markdown("### 🚀 High-End RAG Portfolio Project | Built by Muhammad Bilal")
    
    with gr.Row():
        url_input = gr.Textbox(label="Paste YouTube URL", placeholder="https://www.youtube.com/watch?v=...", scale=4)
        btn = gr.Button("Analyze Video", variant="primary", elem_classes="main-btn", scale=1)
    
    with gr.Row():
        status = gr.Textbox(label="System Status", interactive=False, lines=2)
        preview = gr.Textbox(label="Transcript Insight", interactive=False, lines=2)
        
    btn.click(process_video, inputs=url_input, outputs=[status, preview])
    
    gr.ChatInterface(fn=chat)

if __name__ == "__main__":
    # Launch with Gradio 6.0 settings
    demo.launch(
        theme=gr.themes.Glass(primary_hue="indigo", secondary_hue="violet"),
        css=custom_css,
        ssr_mode=False
    )