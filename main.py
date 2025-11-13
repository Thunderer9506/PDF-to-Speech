# Future Improvement
# Add a drop down button to let user choose which ever character voice they wanna hear

# Dependencies
import streamlit as st
from pypdf import PdfReader
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os
load_dotenv()

# Config
elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
st.set_page_config(page_title="PDF → Audiobook", layout="wide")

# Functions
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()
    return extracted_text

# UI
st.title("📚 PDF-to-Audiobook Converter")
st.markdown("""
Convert **any PDF** into a natural-sounding audiobook using ElevenLabs.
""")

col1,col2 = st.columns([1,1])

# Column 1
with col1:
    uploaded = st.file_uploader("Upload PDF File", type=["pdf"])

    if uploaded:
        st.pdf(uploaded)
    else:
        st.markdown("**No file uploaded — using default PDF.**")
        st.pdf("Spy_in_Erevos9_Story.pdf")

# Colummns 2
with col2:
    convert = st.button("🎧 Convert to Audiobook")

    if not convert:
        if os.path.exists("pdfVoice.mp3"):
            st.audio("pdfVoice.mp3")
        else:
            st.info("Upload a PDF or click convert.")
    else:
        if uploaded:
            pdf_source = uploaded
        else:
            pdf_source = "Spy_in_Erevos9_Story.pdf"
        with st.spinner("📖 Extracting text from PDF..."):
            text = extract_text_from_pdf(pdf_source)

        st.success("Text extracted!")

        progress = st.progress(0)
        status = st.empty()
        status.write("🎙️ Generating audio using ElevenLabs...")
        
        audio_stream = elevenlabs.text_to_speech.convert(
            text=text,
            voice_id=os.getenv("VOICE_ID"),
            model_id=os.getenv("MODEL_ID"),
            output_format=os.getenv("OUTPUT_FORMAT"),
        )
        audio_bytes = b""
        for i, chunk in enumerate(audio_stream):
            audio_bytes += chunk
            progress.progress(min((i + 1) * 0.01, 1.0))  # fake progress growth

        status.write("✅ Audio generation complete!")

        st.audio(audio_bytes, format="audio/mp3")

        st.download_button(
            label="⬇ Download MP3",
            data=audio_bytes,
            file_name="audiobook.mp3",
            mime="audio/mp3"
        )
