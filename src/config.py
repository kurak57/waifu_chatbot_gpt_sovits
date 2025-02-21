import os
from dotenv import load_dotenv
from openai import OpenAI
from gradio_client import Client, handle_file
from src import personality

# Load environment variables from .env file
load_dotenv()

# AI & TTS Configuration
AI_LANGUAGE = "Japanese" # You could change to : "Japanese", "English" or "Chinese"
CHARACTER_NAME = "carlotta" #rename it based on your audio file
SPEAKER_LANGUAGE = "ja" # You can change it based on Google code for language.

# Reference Audio File
REF_AUDIO = handle_file(f"./character_audio/{CHARACTER_NAME}.wav")

# API Clients
LLM_CLIENT = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "http://localhost:1234/v1"),
    api_key=os.getenv("LLM_API_KEY", "lm-studio")
)

TTS_CLIENT = Client(os.getenv("TTS_BASE_URL", "http://localhost:9872/"))

# Load Personality
CHARACTER = getattr(personality, CHARACTER_NAME)

# Chat history initialization
chat_history = [{"role": "system", "content": CHARACTER}]
