import os
from dotenv import load_dotenv
from src.ai import AIChatbot
from src.speech import SpeechRecognition
from src.tts import TextToSpeech

# Load environment variables
load_dotenv()

# Initialize components
chatbot = AIChatbot()
speech_recognition = SpeechRecognition()
tts = TextToSpeech()

def main():
    print("Your waifu is ready to talk with you...")
    
    while True:
        try:
            user_input = speech_recognition.listen()
            # if user_input.lower() in ["exit", "quit", "stop"]:
            #     print("Exiting chatbot...")
            #     break
            
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
            
            tts.speak(response)
        
        except KeyboardInterrupt:
            print("\nChatbot stopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
