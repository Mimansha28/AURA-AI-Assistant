# AURA - AI-Powered Virtual Assistant

AURA is a voice-activated virtual assistant built with Python that responds to voice commands using OpenAI’s language models. It integrates web browsing, news fetching, music playback, and AI-powered conversation in a simple, extensible interface — similar to Alexa or Google Assistant.

---

## Features

- Wake-word-based activation ("Aura")
- *Natural Language Processing* with OpenAI GPT (via OpenRouter API)
- Opens popular websites on command (Google, YouTube, StackOverflow, LinkedIn)
- Fetches top business news headlines using NewsAPI
- Plays music via Spotify or custom music links
- *Voice-activated interface* using speech_recognition and pyttsx3
- Speech recognition via Google Speech API

---

## Tech Stack

- Python 
- speech_recognition – for capturing voice input
- pyttsx3 – for text-to-speech output
- requests – for API integration
- webbrowser – to open web pages
- OpenAI GPT-3.5-Turbo – for intelligent responses
- NewsAPI – for fetching real-time news

---

## Project Structure
AURA/
│
├── main.py # Main application logic
├── music_library.py # Contains custom music link mappings
├── requirements.txt # Python dependencies

---
## Example Commands
-"Aura" → (Activates assistant)

-"Open Google"

-"Play music"

-"Give me the news"

-"What's the capital of France?"

