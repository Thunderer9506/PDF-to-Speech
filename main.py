from pypdf import PdfReader
from elevenlabs.client import ElevenLabs
from elevenlabs import save
from dotenv import load_dotenv
import os

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()
    return extracted_text

text_content = extract_text_from_pdf("Spy_in_Erevos9_Story.pdf")

audio = elevenlabs.text_to_speech.convert(
    text=text_content,
    voice_id="cgSgspJ2msm6clMCkdW9",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

save(audio,"pdfVoice.mp3")

os.system("pdfVoice.mp3")

