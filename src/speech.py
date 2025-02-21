import speech_recognition as sr
from config import SPEAKER_LANGUAGE

def recognize_speech():
    """Captures voice from the microphone and converts it into text (Japanese)."""
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
