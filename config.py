import os
from dotenv import load_dotenv
from openai import OpenAI
from gradio_client import Client, file

# Load environment variables from .env file
load_dotenv()

# AI & TTS Configuration
AI_LANGUAGE = "Japanese"
CHARACTER_NAME = "carlotta"
SPEAKER_LANGUAGE = "ja"

# Reference Audio File
REF_AUDIO_PATH = os.getenv("REF_AUDIO_PATH", "")
REF_AUDIO = file(rf"{REF_AUDIO_PATH}\{CHARACTER_NAME}.wav")

# API Clients
LLM_CLIENT = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "http://localhost:1234/v1"),
    api_key=os.getenv("LLM_API_KEY", "lm-studio")
)

TTS_CLIENT = Client(os.getenv("TTS_BASE_URL", "http://localhost:9872/"))

# Load Personality
personality_module = __import__("personality")
CHARACTER = getattr(personality_module, CHARACTER_NAME)

# Chat history initialization
chat_history = [{"role": "system", "content": CHARACTER}]
