import gradio as gr
from groq import Groq
import os

# 🔑 Setup API Key from Hugging Face Secrets
API_KEY = os.environ.get("GROQ_API_KEY")

def generate_linkedin_post(topic, audience, tone, length):
    if not API_KEY: 
        return "❌ Setup GROQ_API_KEY in Space Secrets!", ""
    
    client = Groq(api_key=API_KEY)
    length_style = "concise" if length == "Short" else "comprehensive"
    
    prompt = f"""
    Write a professional LinkedIn post about: {topic}. 
    Audience: {audience}. 
    Tone: {tone}. 
    Length: {length_style}. 
    Include a scroll-stopping hook, bullet points, and 3 hashtags. Use emojis.
    """
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        res = completion.choices[0].message.content
        word_count = len(res.split())
        return res, f"📊 Words: {word_count}"
    except Exception as e:
        return f"❌ Error: {str(e)}", ""

# 🎨 Stylish UI Design (CSS)
custom_css = """
.gradio-container { background-color: #f0f2f5; font-family: 'Helvetica Neue', sans-serif !important; }
.generate-btn { 
    background: linear-gradient(90deg, #0077b5, #00a0dc) !important; 
    color: white !important; 
    font-weight: bold !important; 
    border-radius: 10px !important; 
    border: none !important;
}
.generate-btn:hover { transform: scale(1.01); transition: 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
"""

# Building the App
with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center; color: #0077b5;'><span style='color: #6c5ce7;'>🚀 Bilal Prism</span> LinkedIn Post AI Architect</h1>")
    gr.Markdown("<p style='text-align: center; font-size: 1.1em;'>Craft viral professional content in seconds.</p>")
    
    with gr.Row():
        with gr.Column(scale=2):
            topic_input = gr.Textbox(
                label="Post Topic", 
                placeholder="What did you achieve or learn today?", 
                lines=4
            )
            with gr.Row():
                audience_input = gr.Dropdown(
                    choices=["Professionals", "Tech Experts", "Recruiters", "Founders"], 
                    label="Audience", 
                    value="Professionals"
                )
                tone_input = gr.Dropdown(
                    choices=["Inspirational", "Professional", "Funny", "Technical"], 
                    label="Tone", 
                    value="Inspirational"
                )
            length_input = gr.Radio(["Short", "Long"], label="Post Length", value="Short")
            submit_btn = gr.Button("✨ Generate Viral Post", elem_classes="generate-btn")
        
        with gr.Column(scale=3):
            # show_copy_button is removed to prevent Gradio 6.11 TypeError
            output_display = gr.Textbox(
                label="Your LinkedIn Draft", 
                lines=15
            )
            count_display = gr.Markdown("📊 Words: 0")

    # Linking the button to the function
    submit_btn.click(
        fn=generate_linkedin_post, 
        inputs=[topic_input, audience_input, tone_input, length_input], 
        outputs=[output_display, count_display]
    )

# 🚀 Final Launch configuration for Gradio 6.x
if __name__ == "__main__":
    demo.launch(
        theme=gr.themes.Soft(),
        css=custom_css
    )
