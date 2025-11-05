# 🗣️ PDF to Speech Converter

Convert **any PDF document into high-quality, natural-sounding speech** using the [ElevenLabs API](https://elevenlabs.io/) and Python.  
This project automatically extracts text from a PDF file and generates an audio narration in MP3 format — perfect for audiobooks, research papers, or study notes!

---

## 🚀 Features

- 📄 Extracts text from **any PDF** file  
- 🎧 Converts text to **realistic human-like speech** using **ElevenLabs**  
- 💾 Saves the generated audio as an **MP3** file  
- ⚙️ Simple, lightweight, and fully **automated** script  

---

## 🧠 Tech Stack

| Component | Description |
|------------|-------------|
| **Python** | Core programming language |
| **PyPDF** | Extracts text from PDF files |
| **ElevenLabs API** | Generates AI-powered realistic voices |
| **python-dotenv** | Loads API keys from environment variables |

---

## 🧩 Prerequisites

Before running the script, ensure you have:

- Python 3.8 or above  
- A valid **[ElevenLabs API key](https://elevenlabs.io/)**  
- A PDF file you want to convert  

---

## ⚙️ Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/thunderer9506/pdf-to-speech.git
   cd pdf-to-speech
   ```

2. **Install dependencies:**
   ```bash
   pip install pypdf elevenlabs python-dotenv
   ```

3. **Set up your environment variables:**
   Create a `.env` file in the root directory and add your ElevenLabs API key:
   ```
   ELEVENLABS_API_KEY=your_api_key_here
   ```

4. **Add your PDF file**  
   Place your desired PDF (e.g., `Spy_in_Erevos9_Story.pdf`) in the project directory.

---

## ▶️ Usage

Run the script:
```bash
python main.py
```

The script will:
1. Extract text from the specified PDF  
2. Send it to ElevenLabs for conversion  
3. Save the output as an MP3 file (`pdfVoice.mp3`)  
4. Automatically play the generated audio 🎶  

---

## 🧾 Example

Input:  
📘 `Spy_in_Erevos9_Story.pdf`

Output:  
🎵 `pdfVoice.mp3` — a natural, expressive narration of the story.

---

## 🧰 Folder Structure

```
pdf-to-speech/
│
├── .env
├── main.py
├── Spy_in_Erevos9_Story.pdf
├── pdfVoice.mp3
├── requirements.txt
└── README.md
```

---

## 💡 Future Enhancements

- Add **GUI interface** using Tkinter or Streamlit  
- Support for **multiple voices or languages**  
- Add **chunk-based text processing** for large PDFs  
- Option to generate **audiobooks with chapters**  

---

## ⚠️ Notes

- Very large PDFs may require splitting text into smaller parts.  
- Make sure your ElevenLabs account has sufficient credits or API quota.  

---

## 🧑‍💻 Author

**Shaurya Srivastava**  
AI/ML Engineer | Python Developer | Flask Expert  
🌐 [GitHub](https://github.com/Thunderer9506)  

---

## 📜 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.
