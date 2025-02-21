# AI Voice Chatbot

## Prerequisites
Before running this project, you need to install and start GPT-SoVITS. You can find the repository here: [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS).

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/kurak57/waifu_chatbot_gpt_sovits.git
   cd waifu_chatbot_gpt_sovits
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and add the necessary configurations.

## Usage
1. Start GPT-SoVITS before running the chatbot.
2. Run the chatbot script:
   ```sh
   python main.py
   ```

## Configuration
Edit the `.env` file to set up:
- LLM API endpoint
- TTS API endpoint

## Features
- Speech-to-Text processing
- AI-powered chatbot responses
- Text-to-Speech synthesis using GPT-SoVITS
- Maintains chat history

## License
This project is licensed under the MIT License.

