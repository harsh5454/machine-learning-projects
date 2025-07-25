# 🎙️ Speech Recognition System - CODTECH Internship Task 2

This project is a basic **Speech-to-Text system** built using Python and pre-trained libraries. It fulfills the requirements of **Internship Task 2** at CODTECH.

---

## ✅ Features

- Converts `.wav` audio files to text
- Uses **Google Speech Recognition API**
- Saves transcribed output to `transcription.txt`

---

## 📁 Project Structure

SpeechRecognitionProject/
│
├── audio/ # Folder containing audio input
│ └── sample.wav
│
├── main.py # Main script for speech recognition
├── requirements.txt # Python dependencies
└── transcription.txt # Output generated by script

yaml
Copy
Edit

---

## 🚀 How to Run

1. Clone/download this repo
2. Install dependencies:

```bash
pip install -r requirements.txt
Add your .wav audio file in the audio/ folder

Run the script:

bash
Copy
Edit
python main.py
📌 Dependencies
speechrecognition

pyaudio

If pyaudio fails to install:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
🎯 Output
The transcribed text will be shown in the console and saved to transcription.txt.