import playsound
from config import TTS_CLIENT, REF_AUDIO, AI_LANGUAGE

def text_to_speech(text):
    """Converts text to speech and plays the generated audio."""
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
