import speech_recognition as sr
from openai import OpenAI
from gradio_client import Client, file
import playsound
from dotenv import load_dotenv
import os
# import re
load_dotenv()
AI_LANGUAGE = "Japanese"
CHARACTER_NAME = "carlotta" 
SPEAKER_LANGUAGE = "ja"
REF_AUDIO = file(f"./character_audio/{CHARACTER_NAME}.wav")
LLM_CLIENT = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "http://localhost:1234/v1"),
    api_key=os.getenv("LLM_API_KEY", "lm-studio")
)
TTS_CLIENT = Client(os.getenv("TTS_BASE_URL", "http://localhost:9872/"))
personality_module = __import__("personality")
CHARACTER = getattr(personality_module, CHARACTER_NAME)

# Save chat history
chat_history = [
    {
        "role": "system",
        "content": CHARACTER
    }
]

def recognize_speech():
    """Menangkap suara dari mikrofon dan mengubahnya menjadi teks (Bahasa Inggris)."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language=SPEAKER_LANGUAGE)
        print(f"🗣 You Said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Can't recognize voice.")
    except sr.RequestError:
        print("❌ Error in Speech-to-Text service.")
    return None

def text_to_speech(text):
    """Convert text to speech and play it directly."""
    audio_path = TTS_CLIENT.predict(
        ref_wav_path=REF_AUDIO,
        prompt_text="",
        prompt_language=AI_LANGUAGE,
        text=text,
        text_language=AI_LANGUAGE,
        how_to_cut="Slice once every 4 sentences",
        top_k=15,
        top_p=1,
        temperature=1,
        ref_free=False,
        speed=1,
        if_freeze=False,
        inp_refs=None,
        api_name="/get_tts_wav"
    )
    playsound.playsound(audio_path)

# def clean_text(response):
#     """Menghapus deskripsi yang tidak perlu *, [], dan ()."""
#     response = re.sub(r"\*.*?\*", "", response)  # Hapus teks dalam tanda *
#     response = re.sub(r"\[.*?\]", "", response)  # Hapus teks dalam tanda []
#     response = re.sub(r"\(.*?\)", "", response)  # Hapus teks dalam tanda ()
#     return response.strip()

def get_ai_response(command):
    """Send commands to LLM with chat history and receive responses."""
    global chat_history

    # add user input to history
    chat_history.append({"role": "user", "content": command})

    # send chat and get response from LLM
    completion = LLM_CLIENT.chat.completions.create(
        model="model-identifier",
        messages=chat_history,
        # messages=[
        #         {"role": "system",
        #         "content": CHARACTER },
        #         {"role": "user", "content": command}
        #     ],
        temperature=0.7
    )
    response = completion.choices[0].message.content
    # # response = clean_text(response)  # Bersihkan dari deskripsi aksi

    chat_history.append({"role": "assistant", "content": response})
    # maximum chat history
    if len(chat_history) > 10:
        chat_history = [chat_history[0]] + chat_history[-9:]

    return response

# LLM Interaction
while True:
    command = recognize_speech()
    if command:
        response = get_ai_response(command)
        print(f"{CHARACTER_NAME.title()}: ", response)
        text_to_speech(response)
