from speech import recognize_speech
from ai import get_ai_response
from tts import text_to_speech
from config import CHARACTER_NAME

# Continuous AI interaction loop
while True:
    command = recognize_speech()
    if command:
        response = get_ai_response(command)
        print(f"{CHARACTER_NAME.title()}: {response}")
        text_to_speech(response)
